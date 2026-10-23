#!/usr/bin/env python3
"""
Inventario de fuentes citables a partir de exports bibliograficos.

Solo extrae los campos que existen en los archivos y dice que falta. No
interpreta, no resume y no completa nada. Solo biblioteca estandar.

Uso
---
    python3 inventario_fuentes.py exports/*.ris exports/*.csv --out inventario.json
    python3 inventario_fuentes.py nuevos/*.txt --previo inventario.json --out inventario.json
    (opcional) --tabla   imprime la tabla completa; --md inventario.md la guarda

Formatos que reconoce (se detectan por el contenido, no por la extension)
-------------------------------------------------------------------------
  - RIS                (TY  - ... ER  -)                     Scopus, WoS, Zotero, Mendeley
  - BibTeX             (@article{...})                       Scopus, Zotero
  - CSV de Scopus      (columnas Authors, Title, Year, Source title, DOI, Abstract,
                        Author Keywords)
  - Texto plano de WoS (etiquetas PT/AU/TI/SO/PY/DI/AB/DE/ER, "Full record")
  - Texto plano de Scopus (autores / titulo / "(2021) Revista..." / ABSTRACT:)
  - Texto etiquetado   ("Authors:", "Title:", "Year:", "Abstract:"...)
  - Fichas de la plataforma Acosta ("acosta"): el texto pegado de
    `buscar_fuentes` o `mis_fuentes` ("1. [AR51541814]  Chen, K.; ... (2025).
    Título. Revista, 126(1-2), 132-148. https://doi.org/...", "Resumen: ...").
    Conservan su clave AR como ID (no reciben F). Sus resúmenes vienen recortados
    (~400 caracteres): quedan marcados "resumen_recortado" y no se citan por
    contenido hasta tener el completo (un export posterior con el mismo DOI lo
    completa sin cambiar el ID).

Campos de cada fuente
---------------------
id, autores, anio, titulo, fuente (revista o libro), doi, abstract, keywords y,
cuando el formato los trae: autores_completos (AF de WoS, "Author full names"
de Scopus, AU completos de RIS/BibTeX), volumen, numero, paginas ("132-148"),
art_no (número de artículo), tipo (articulo | libro | capitulo | congreso | web |
otro), editorial, editores, url, consultado (fecha de consulta), origen, alias
(otras claves de la misma fuente, p. ej. la AR de Acosta). El motor del Word
(articulo_docx.py --fuentes) arma con ellos las citas y la lista de referencias.

IDs estables
------------
Cada fuente recibe un ID F001, F002... (las fichas de Acosta conservan su AR...) Se deduplica por DOI y, si falta, por
titulo normalizado. Con --previo se conservan los IDs del inventario anterior y
las fuentes nuevas se numeran a continuacion; si una fuente repetida trae ahora
el abstract que antes faltaba, se completa sin cambiarle el ID.

Si un archivo no se reconoce, se avisa (FORMATO NO RECONOCIDO), se sigue con los
demas y el codigo de salida es 2. Ese archivo se inventaria a mano: no se adivina.
"""

import argparse
import csv
import glob
import io
import json
import re
import sys
import unicodedata
from pathlib import Path

MIN_ABSTRACT_CHARS = 120  # por debajo de esto casi nunca es un abstract real
SIN_ABSTRACT = {"[no abstract available]", "no abstract available", "n/a", "na"}


# --------------------------------------------------------------------------
# Lectura y deteccion
# --------------------------------------------------------------------------
def leer(ruta: Path) -> str:
    datos = ruta.read_bytes()
    for enc in ("utf-8-sig", "utf-16", "cp1252", "latin-1"):
        try:
            texto = datos.decode(enc)
            if enc == "utf-16" and "\x00" in texto:
                continue
            return texto.replace("\r\n", "\n").replace("\r", "\n")
        except UnicodeError:
            continue
    return datos.decode("utf-8", errors="replace")


def detectar_formato(texto: str) -> str:
    if re.search(r"^TY\s{2}-", texto, re.M) and re.search(r"^ER\s{2}-", texto, re.M):
        return "ris"
    if re.search(r"^\s*@\w+\s*\{", texto, re.M):
        return "bibtex"
    if re.search(r"^(PT|FN) ", texto, re.M) and re.search(r"^ER\s*$", texto, re.M):
        return "wos"
    if len(re.findall(r"^\s*(?:\d+[.)]\s*)?\[AR\d+\]\s+\S", texto, re.M)) >= 1:
        return "acosta"
    primera = texto.lstrip().split("\n", 1)[0]
    if "," in primera or ";" in primera or "\t" in primera:
        cab = primera.lower()
        if "title" in cab and ("author" in cab or "year" in cab):
            return "csv"
    if re.search(r"^\(\d{4}\)\s", texto, re.M) and (re.search(r"^ABSTRACT:", texto, re.M)
                                                    or re.search(r"^AUTHOR FULL NAMES:", texto, re.M)):
        return "scopus_txt"
    etiquetas = len(re.findall(r"^(Authors?|Author full names|Title|Year|Abstract|Source title|DOI)\s*:",
                               texto, re.M | re.I))
    if etiquetas >= 3:
        return "etiquetado"
    return "desconocido"


CAMPOS_EXTRA = ("autores_completos", "volumen", "numero", "paginas", "art_no", "tipo", "editorial",
                "editores", "url", "consultado", "origen")


def registro(autores=None, anio="", titulo="", fuente="", doi="", abstract="", keywords="", **extra):
    ab = " ".join((abstract or "").split())
    if ab.lower() in SIN_ABSTRACT:
        ab = ""
    m = re.search(r"(19|20)\d{2}", anio or "")
    r = {
        "autores": [a for a in (autores or []) if a],
        "anio": m.group(0) if m else "",
        "titulo": " ".join((titulo or "").split()).strip(" {}."),
        "fuente": " ".join((fuente or "").split()).strip(" {}"),
        "doi": limpiar_doi(doi),
        "abstract": ab,
        "keywords": " ".join((keywords or "").split()),
    }
    # campos bibliográficos para formatear la referencia (solo si el formato los trae)
    completos = [_sin_id(a) for a in (extra.get("autores_completos") or []) if a and a.strip()]
    if completos and any(_tiene_nombre_pila(a) for a in completos):
        r["autores_completos"] = completos
    for k in ("volumen", "numero", "editorial", "url", "consultado", "origen", "art_no"):
        v = " ".join(str(extra.get(k) or "").split()).strip(" {},.")
        if v:
            r[k] = v
    pag = _paginas(extra.get("paginas") or "", extra.get("pag_fin") or "")
    if pag:
        r["paginas"] = pag
    if extra.get("editores"):
        r["editores"] = [e for e in extra["editores"] if e]
    r["tipo"] = tipo_de(extra.get("tipo") or "", bool(r["fuente"]), bool(r.get("url")))
    return r


def _sin_id(autor: str) -> str:
    return re.sub(r"\s*\(\d+\)\s*$", "", autor.strip())


def _tiene_nombre_pila(autor: str) -> bool:
    """'Hair, Joseph F.' sí; 'Hair, J. F.' / 'Hair J.F.' / 'Ford, ME' no."""
    if "," in autor:
        pila = autor.split(",", 1)[1]
        return bool(re.search(r"[^\W\d_]{2,}(?!\.)\b", pila)) and not re.fullmatch(r"\s*[A-Z]{1,4}\s*", pila)
    return False


def _paginas(ini: str, fin: str = "") -> str:
    ini, fin = " ".join(str(ini).split()), " ".join(str(fin).split())
    if fin and ini:
        return f"{ini}-{fin}"
    ini = re.sub(r"\s*[-–—]+\s*", "-", ini)
    return ini.strip(" .,")


def tipo_de(crudo: str, con_fuente=True, con_url=False) -> str:
    """Normaliza el tipo documental: articulo, libro, capitulo, congreso, web, otro."""
    t = (crudo or "").lower()
    if re.search(r"chap|incollection|inbook|cap[ií]tulo|book section|book chapter", t):
        return "capitulo"
    if re.search(r"conf|proceed|cpaper|congres|meeting", t):
        return "congreso"
    if re.search(r"\bbook\b|^b$|^libro|^s$", t) or t in ("book", "ebook", "edbook"):
        return "libro"
    if re.search(r"elec|web|online|blog|^misc$|^www$", t):
        return "web"
    if re.search(r"jour|art[ií]cul|article|review|^j$|letter|editorial|note|survey", t):
        return "articulo"
    if t and re.search(r"thes|tesis|report|rprt|patent|data|^gen$", t):
        return "otro"
    if not t and con_url and not con_fuente:
        return "web"
    return "articulo" if con_fuente else "otro"


def limpiar_doi(doi: str) -> str:
    doi = (doi or "").strip().strip("{}")
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", doi, flags=re.I)
    return doi.strip()


# --------------------------------------------------------------------------
# Parsers
# --------------------------------------------------------------------------
def parse_ris(texto: str):
    registros, actual, campo = [], None, None
    for linea in texto.split("\n"):
        m = re.match(r"^([A-Z][A-Z0-9])\s{2}-\s?(.*)$", linea)
        if m:
            campo, valor = m.group(1), m.group(2).strip()
            if campo == "TY":
                actual = {"TY": [valor]}
            elif campo == "ER":
                if actual is not None:
                    registros.append(actual)
                actual, campo = None, None
            elif actual is not None:
                actual.setdefault(campo, []).append(valor)
        elif campo and actual is not None and campo in actual and linea.strip():
            actual[campo][-1] += " " + linea.strip()
    g = lambda r, *ks: next((r[k][0] for k in ks if r.get(k)), "")
    salida = []
    for r in registros:
        au = r.get("AU") or r.get("A1") or []
        tipo = g(r, "TY")
        es_cap = tipo_de(tipo) == "capitulo"
        salida.append(registro(
            au, g(r, "PY", "Y1", "DA"), g(r, "TI", "T1"),
            g(r, "T2", "BT", "JO", "JF", "JA") if es_cap or tipo_de(tipo) != "libro" else g(r, "T2", "JO", "JF", "JA"),
            g(r, "DO"), " ".join(r.get("AB") or r.get("N2") or []), "; ".join(r.get("KW", [])),
            autores_completos=au, volumen=g(r, "VL"), numero=g(r, "IS"), paginas=g(r, "SP"), pag_fin=g(r, "EP"),
            art_no=g(r, "C7", "AN") if g(r, "C7") else "", tipo=tipo, editorial=g(r, "PB"),
            editores=r.get("A2") or r.get("ED") or [], url=g(r, "UR"), consultado=g(r, "Y2")))
    return salida


def _bib_valor(cuerpo: str, i: int):
    """Lee un valor BibTeX desde la posicion i ({...} anidado, "..." o palabra)."""
    if cuerpo[i] == "{":
        nivel, j = 0, i
        while j < len(cuerpo):
            if cuerpo[j] == "{":
                nivel += 1
            elif cuerpo[j] == "}":
                nivel -= 1
                if nivel == 0:
                    return cuerpo[i + 1:j], j + 1
            j += 1
        return cuerpo[i + 1:], len(cuerpo)
    if cuerpo[i] == '"':
        j = cuerpo.find('"', i + 1)
        j = len(cuerpo) if j < 0 else j
        return cuerpo[i + 1:j], j + 1
    m = re.match(r"[^,}\s]+", cuerpo[i:])
    return (m.group(0) if m else ""), i + (m.end() if m else 0)


def parse_bibtex(texto: str):
    salida = []
    for m in re.finditer(r"@(\w+)\s*\{", texto):
        if m.group(1).lower() in ("comment", "string", "preamble"):
            continue
        # cuerpo de la entrada: hasta la llave que la cierra
        nivel, j = 1, m.end()
        while j < len(texto) and nivel:
            nivel += {"{": 1, "}": -1}.get(texto[j], 0)
            j += 1
        cuerpo = texto[m.end():j - 1]
        campos, pos = {}, cuerpo.find(",") + 1
        for c in re.finditer(r"(\w[\w-]*)\s*=\s*", cuerpo):
            if c.start() < pos:
                continue
            valor, fin = _bib_valor(cuerpo, c.end())
            campos[c.group(1).lower()] = re.sub(r"[{}]", "", valor)
            pos = fin
        if not campos:
            continue
        autores = [a.strip() for a in re.split(r"\s+and\s+", " ".join(campos.get("author", "").split()))
                   if a.strip()]
        editores = [a.strip() for a in re.split(r"\s+and\s+", " ".join(campos.get("editor", "").split()))
                    if a.strip()]
        salida.append(registro(autores, campos.get("year", "") or campos.get("date", ""), campos.get("title", ""),
                               campos.get("journal") or campos.get("journaltitle") or campos.get("booktitle", ""),
                               campos.get("doi", ""), campos.get("abstract", ""),
                               campos.get("author_keywords") or campos.get("keywords", ""),
                               autores_completos=autores, volumen=campos.get("volume", ""),
                               numero=campos.get("number", "") or campos.get("issue", ""),
                               paginas=campos.get("pages", ""), art_no=campos.get("art_number", "")
                               or campos.get("eid", ""), tipo=m.group(1),
                               editorial=campos.get("publisher", ""), editores=editores,
                               url=campos.get("url", ""), consultado=campos.get("urldate", "")))
    return salida


def parse_wos(texto: str):
    registros, actual, campo = [], None, None
    for linea in texto.split("\n"):
        if re.match(r"^ER\s*$", linea):
            if actual:
                registros.append(actual)
            actual, campo = None, None
            continue
        m = re.match(r"^([A-Z][A-Z0-9]) (.*)$", linea)
        if m:
            campo = m.group(1)
            if campo in ("FN", "VR", "EF"):
                campo = None
                continue
            if actual is None:
                actual = {}
            actual.setdefault(campo, []).append(m.group(2).strip())
        elif linea.startswith("   ") and campo and actual is not None:
            actual[campo].append(linea.strip())
    une = lambda r, k: " ".join(r.get(k, []))
    return [registro(r.get("AU") or r.get("AF") or [], une(r, "PY"), une(r, "TI"), une(r, "SO"),
                     une(r, "DI"), une(r, "AB"), une(r, "DE"),
                     autores_completos=r.get("AF") or [], volumen=une(r, "VL"), numero=une(r, "IS"),
                     paginas=une(r, "BP"), pag_fin=une(r, "EP"), art_no=une(r, "AR"),
                     tipo=(une(r, "DT") or une(r, "PT")) + (" chapter" if "Chapter" in une(r, "DT") else ""),
                     editorial=une(r, "PU"), editores=r.get("BE") or [])
            for r in registros]


def _autores_scopus(crudo: str):
    crudo = (crudo or "").strip()
    if not crudo or crudo.lower().startswith("[no author"):
        return []
    if ";" in crudo:
        return [a.strip() for a in crudo.split(";") if a.strip()]
    return [a.strip() for a in re.split(r"(?<=\.),\s+", crudo) if a.strip()]


def parse_csv(texto: str):
    muestra = texto[:5000]
    try:
        dialecto = csv.Sniffer().sniff(muestra, delimiters=",;\t")
    except csv.Error:
        dialecto = csv.excel
    lector = csv.DictReader(io.StringIO(texto), dialect=dialecto)
    cols = {(c or "").strip().lower().lstrip("﻿"): c for c in (lector.fieldnames or [])}
    col = lambda *ns: next((cols[n] for n in ns if n in cols), None)
    c_au, c_ti, c_yr = col("authors", "author", "author full names"), col("title", "article title"), \
        col("year", "publication year")
    c_so, c_doi, c_ab = col("source title", "source", "journal"), col("doi"), col("abstract")
    c_kw = col("author keywords", "keywords")
    c_af = col("author full names", "author full name")
    c_vl, c_is = col("volume"), col("issue")
    c_ps, c_pe, c_an = col("page start", "start page"), col("page end", "end page"), col("art. no.", "article number")
    c_ty, c_pb, c_ed = col("document type"), col("publisher"), col("editors")
    salida = []
    for fila in lector:
        v = lambda c: (fila.get(c) or "") if c else ""
        if not v(c_ti).strip():
            continue
        salida.append(registro(_autores_scopus(v(c_au)), v(c_yr), v(c_ti), v(c_so), v(c_doi),
                               v(c_ab), v(c_kw),
                               autores_completos=[a.strip() for a in v(c_af).split(";")] if c_af and c_af != c_au else [],
                               volumen=v(c_vl), numero=v(c_is), paginas=v(c_ps), pag_fin=v(c_pe), art_no=v(c_an),
                               tipo=v(c_ty), editorial=v(c_pb),
                               editores=[e.strip() for e in v(c_ed).split(";") if e.strip()]))
    return salida


def parse_scopus_txt(texto: str):
    """Export 'Plain text' de Scopus. Cada registro empieza en la línea de autores,
    seguida de 'AUTHOR FULL NAMES:'; dentro del registro hay líneas en blanco, así
    que se corta por esa marca y no por las líneas vacías."""
    lineas = texto.split("\n")
    inicios = [k - 1 for k, l in enumerate(lineas) if l.startswith("AUTHOR FULL NAMES:") and k > 0]
    if not inicios:   # exports sin 'AUTHOR FULL NAMES': respaldo por bloques
        inicios = [k for k, l in enumerate(lineas) if re.match(r"^\(\d{4}\)\s", l)]
        inicios = [max(0, k - 2) for k in inicios]
    salida = []
    for n, ini in enumerate(inicios):
        fin = inicios[n + 1] if n + 1 < len(inicios) else len(lineas)
        reg = [l.rstrip() for l in lineas[ini:fin]]
        k_anio = next((k for k, l in enumerate(reg) if re.match(r"^\(\d{4}\)\s", l.strip())), None)
        if k_anio is None:
            continue
        autores = _autores_scopus(reg[0])
        cab = [l.strip() for l in reg[1:k_anio] if l.strip()
               and not l.startswith("AUTHOR FULL NAMES:") and not re.fullmatch(r"[\d;\s]+", l.strip())]
        titulo = " ".join(cab)
        m = re.match(r"^\((\d{4})\)\s*(.*)$", reg[k_anio].strip())
        fuente = re.split(r",\s*\d|,\s*pp\.|\.\s*Cited|,\s*art\. no\.", m.group(2))[0]
        campos, clave = {}, None
        for l in reg[k_anio + 1:]:
            e = re.match(r"^([A-Z][A-Z ()/-]+):\s*(.*)$", l)
            if e:
                clave = e.group(1).strip()
                campos[clave] = e.group(2)
            elif clave and l.strip() and not l.startswith("http"):
                campos[clave] += " " + l.strip()
            elif not l.strip():
                clave = None
        resto = m.group(2)
        vol = re.search(r",\s*(\d+[A-Za-z]?)\s*(?:\(([^)]*)\))?\s*(?:,|\.?$)", resto[len(fuente):])
        pp = re.search(r"pp\.\s*([\w]+)\s*-\s*([\w]+)", resto)
        an = re.search(r"art\. no\.\s*([\w.-]+?)(?:,|\.?\s*$)", resto)
        full = next((l[len("AUTHOR FULL NAMES:"):] for l in reg if l.startswith("AUTHOR FULL NAMES:")), "")
        salida.append(registro(autores, m.group(1), titulo, fuente, campos.get("DOI", ""),
                               campos.get("ABSTRACT", ""), campos.get("AUTHOR KEYWORDS", ""),
                               autores_completos=[a.strip() for a in full.split(";")],
                               volumen=vol.group(1) if vol else "", numero=(vol.group(2) or "") if vol else "",
                               paginas=pp.group(1) if pp else "", pag_fin=pp.group(2) if pp else "",
                               art_no=an.group(1) if an else "", tipo=campos.get("DOCUMENT TYPE", ""),
                               editorial=campos.get("PUBLISHER", "")))
    return salida


ALIAS = {
    "authors": "autores", "author": "autores", "author full names": "autores_completos",
    "title": "titulo", "year": "anio", "source title": "fuente", "doi": "doi",
    "abstract": "abstract", "author keywords": "keywords",
    "volume": "volumen", "issue": "numero", "pages": "paginas", "document type": "tipo",
    "publisher": "editorial", "url": "url",
}


def parse_etiquetado(texto: str):
    """Texto plano con campos 'Etiqueta: valor', registros separados por linea en blanco."""
    salida = []
    for bloque in re.split(r"\n\s*\n(?=[A-Za-z])", texto.strip()):
        campos, clave = {}, None
        for linea in bloque.split("\n"):
            m = re.match(r"^([A-Za-z][A-Za-z()' \-]{2,30})\s*:\s*(.*)$", linea)
            if m and m.group(1).strip().lower() in ALIAS:
                clave = ALIAS[m.group(1).strip().lower()]
                campos[clave] = m.group(2).strip()
            elif clave and linea.strip():
                campos[clave] += " " + linea.strip()
        if not campos.get("titulo") and not campos.get("abstract"):
            continue
        crudo = campos.get("autores_completos") or campos.get("autores", "")
        salida.append(registro([a.strip() for a in crudo.split(";") if a.strip()],
                               campos.get("anio", ""), campos.get("titulo", ""), campos.get("fuente", ""),
                               campos.get("doi", ""), campos.get("abstract", ""), campos.get("keywords", ""),
                               autores_completos=[a.strip() for a in campos.get("autores_completos", "").split(";")],
                               volumen=campos.get("volumen", ""), numero=campos.get("numero", ""),
                               paginas=campos.get("paginas", ""), tipo=campos.get("tipo", ""),
                               editorial=campos.get("editorial", ""), url=campos.get("url", "")))
    return salida


RE_ACOSTA = re.compile(r"^\s*(?:\d+[.)]\s*)?\[(AR\d+)\]\s*(.*)$")


def _cola_revista(resto: str):
    """'Título. Revista, 126(1-2), 132-148' -> (título, revista, vol, núm, págs, art_no)."""
    m = re.search(r"^(.*?),\s*(\d+[A-Za-z]?)\s*(?:\(([^)]*)\))?(?:,\s*([A-Za-z]?\d+[A-Za-z]?(?:\s*[-–]\s*[A-Za-z]?\d+)?))?\s*\.?$",
                  resto)
    if m:
        cabeza, vol, num, pag = m.group(1), m.group(2), m.group(3) or "", m.group(4) or ""
    else:
        cabeza, vol, num, pag = resto.rstrip(". "), "", "", ""
    cortes = [c.end() for c in re.finditer(r"[.?!]\s+(?=\S)", cabeza)]
    if not cortes:
        return cabeza.strip(" ."), "", vol, num, pag
    k = cortes[-1]
    titulo = cabeza[:k].strip()
    titulo = titulo[:-1] if titulo.endswith(".") else titulo
    return titulo, cabeza[k:].strip(" ."), vol, num, pag


def parse_acosta(texto: str):
    """Fichas de la plataforma Acosta (buscar_fuentes / mis_fuentes), pegadas tal cual."""
    lineas = texto.split("\n")
    inicios = [k for k, l in enumerate(lineas) if RE_ACOSTA.match(l)]
    salida = []
    for n, ini in enumerate(inicios):
        fin = inicios[n + 1] if n + 1 < len(inicios) else len(lineas)
        m = RE_ACOSTA.match(lineas[ini])
        clave, cab = m.group(1), m.group(2).strip()
        resumen, origen, en_resumen = [], "", False
        for l in lineas[ini + 1:fin]:
            t = l.strip()
            if not t:
                en_resumen = False
                continue
            if re.match(r"^(Resumen|Abstract)\s*:", t, re.I):
                en_resumen = True
                resumen.append(re.sub(r"^(Resumen|Abstract)\s*:\s*", "", t, flags=re.I))
            elif re.fullmatch(r"\[[^\]]+\]", t):
                origen = t.strip("[]")
                en_resumen = False
            elif en_resumen:
                resumen.append(t)
            elif not resumen:
                cab += " " + t          # la cabecera partida en varias líneas
        # 'mis_fuentes': "Autores (Año). Título · origen"
        if " · " in cab:
            cab, origen2 = cab.rsplit(" · ", 1)
            origen = origen or origen2.strip()
        doi = ""
        md = re.search(r"\s*(?:https?://(?:dx\.)?doi\.org/|doi:\s*)(10\.\S+?)\.?\s*$", cab, re.I)
        if md:
            doi, cab = md.group(1), cab[:md.start()]
        url = ""
        mu = re.search(r"\s*(https?://\S+?)\.?\s*$", cab)
        if mu:
            url, cab = mu.group(1), cab[:mu.start()]
        ma = re.match(r"^(.*?)\s*\(((?:19|20)\d{2}[a-z]?|s\.\s?f\.|n\.d\.)\)\.?\s*(.*)$", cab)
        if ma:
            crudo_au, anio, resto = ma.group(1), ma.group(2), ma.group(3)
        else:
            crudo_au, anio, resto = "", "", cab
        autores = [a.strip() for a in re.split(r";|\s+&\s+|\s+y\s+(?=[A-ZÁÉÍÓÚÑ][^,]*,)", crudo_au)
                   if a.strip() and a.strip() not in ("et al.", "…", "...")]
        titulo, fuente, vol, num, pag = _cola_revista(resto.strip())
        ab = " ".join(resumen).strip()
        recortado = bool(re.search(r"(\.\.\.|…)\s*$", ab))
        ab = re.sub(r"\s*(\.\.\.|…)\s*$", "", ab)
        r = registro(autores, anio, titulo, fuente, doi, ab, "", volumen=vol, numero=num,
                     paginas=pag, url=url, origen=origen or "plataforma Acosta")
        r["id"] = clave
        if ab and (recortado or len(ab) <= 450):
            r["resumen_recortado"] = True
        salida.append(r)
    return salida


PARSERS = {"ris": parse_ris, "bibtex": parse_bibtex, "wos": parse_wos, "csv": parse_csv,
           "scopus_txt": parse_scopus_txt, "etiquetado": parse_etiquetado, "acosta": parse_acosta}


# --------------------------------------------------------------------------
# Deduplicacion, IDs y cita sugerida
# --------------------------------------------------------------------------
def titulo_norm(t: str) -> str:
    t = re.sub(r"\s*\[[^\]]+\]\s*\.?$", "", t or "")   # Scopus añade la traducción entre corchetes
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())


def claves(r):
    k = []
    if r.get("doi"):
        k.append("doi:" + r["doi"].lower())
    tn = titulo_norm(r.get("titulo", ""))
    if len(tn) >= 15:
        k.append("ti:" + tn)
    return k


def apellido(autor: str) -> str:
    autor = re.sub(r"\s*\(\d+\)\s*$", "", autor.strip())  # quita ID de Scopus
    if "," in autor:
        return autor.split(",")[0].strip()
    partes = autor.split()
    if not partes:
        return ""
    if len(partes) > 1 and re.fullmatch(r"(?:[A-Z]\.?-?){1,4}", partes[-1]):
        return " ".join(partes[:-1])   # 'Van Dijk T.A.' -> 'Van Dijk'
    return partes[-1]


def completar(r):
    ab = (r.get("abstract") or "").strip()
    r["abstract_chars"] = len(ab)
    # resumen recortado (p. ej. OpenAlex devuelve ~400 caracteres): termina sin punto final
    parcial = bool(ab) and (bool(r.get("resumen_recortado")) or
                            len(ab) < 700 and not re.search(r"[.!?)\]»”©]\s*$|\d{4}\.?$", ab))
    r["resumen_parcial"] = parcial
    r["citable_por_contenido"] = len(ab) >= MIN_ABSTRACT_CHARS and not parcial
    au = r.get("autores") or []
    anio = r.get("anio") or "s. f."
    if not au:
        r["cita_sugerida"] = "[POR CONFIRMAR: autor]"
    elif len(au) == 1:
        r["cita_sugerida"] = f"{apellido(au[0])} {anio}"
    elif len(au) == 2:
        r["cita_sugerida"] = f"{apellido(au[0])} y {apellido(au[1])} {anio}"
    else:
        r["cita_sugerida"] = f"{apellido(au[0])} et al. {anio}"


def expandir(patrones):
    rutas = []
    for p in patrones:
        hallados = sorted(glob.glob(p)) if any(ch in p for ch in "*?[") else [p]
        if not hallados:
            print(f"  (sin coincidencias: {p})", file=sys.stderr)
        rutas.extend(hallados)
    vistos, unicas = set(), []
    for r in rutas:
        if r not in vistos and Path(r).is_file():
            vistos.add(r)
            unicas.append(r)
    return unicas


def main():
    ap = argparse.ArgumentParser(description="Inventario de fuentes citables (RIS, BibTeX, CSV Scopus, WoS, txt)")
    ap.add_argument("archivos", nargs="+", help="archivos o patrones: *.ris *.bib *.csv *.txt")
    ap.add_argument("--out", "--json", dest="out", default="inventario.json")
    ap.add_argument("--previo", help="inventario.json anterior: conserva sus IDs")
    ap.add_argument("--md", dest="md_out", help="guarda la tabla en Markdown")
    ap.add_argument("--tabla", action="store_true", help="imprime la tabla completa en consola")
    args = ap.parse_args()

    inventario, indice = [], {}
    if args.previo and Path(args.previo).exists():
        previo = json.loads(Path(args.previo).read_text(encoding="utf-8"))
        previo = previo.get("fuentes", previo) if isinstance(previo, dict) else previo
        for r in previo:
            inventario.append(r)
            for k in claves(r):
                indice.setdefault(k, r)
        print(f"# previo: {len(previo)} fuentes conservan su ID", file=sys.stderr)
    n_prev = len(inventario)
    siguiente = max([int(m.group(1)) for r in inventario
                     for m in [re.match(r"F(\d+)$", str(r.get("id", "")))] if m] or [0]) + 1

    duplicados, completados, fallidos = 0, 0, []
    for ruta in expandir(args.archivos):
        texto = leer(Path(ruta))
        fmt = detectar_formato(texto)
        if fmt == "desconocido":
            print(f"FORMATO NO RECONOCIDO: {ruta} (inventariar a mano; no se adivina)", file=sys.stderr)
            fallidos.append(ruta)
            continue
        nuevos = PARSERS[fmt](texto)
        print(f"# {Path(ruta).name}: formato {fmt}, {len(nuevos)} registros", file=sys.stderr)
        for r in nuevos:
            existente = next((indice[k] for k in claves(r) if k in indice), None)
            if existente is not None:
                duplicados += 1
                for campo in ("abstract", "doi", "fuente", "anio", "keywords", "titulo") + CAMPOS_EXTRA:
                    if not existente.get(campo) and r.get(campo):
                        existente[campo] = r[campo]
                        completados += campo == "abstract"
                # un resumen recortado se reemplaza por uno más largo (el completo)
                if r.get("abstract") and len(r["abstract"]) > len(existente.get("abstract") or "") + 40:
                    existente["abstract"] = r["abstract"]
                    if r.get("resumen_recortado"):
                        existente["resumen_recortado"] = True
                    else:
                        existente.pop("resumen_recortado", None)
                    completados += 1
                # misma fuente con otra clave (p. ej. la AR de Acosta): queda como alias citable
                if r.get("id") and r["id"] != existente.get("id"):
                    existente.setdefault("alias", [])
                    if r["id"] not in existente["alias"]:
                        existente["alias"].append(r["id"])
                if not existente.get("autores") and r["autores"]:
                    existente["autores"] = r["autores"]
                if existente.get("tipo") in (None, "", "otro") and r.get("tipo") not in (None, "", "otro"):
                    existente["tipo"] = r["tipo"]
                for k in claves(existente):
                    indice.setdefault(k, existente)
                continue
            if not r.get("id"):        # las fichas de Acosta traen su clave AR
                r["id"] = f"F{siguiente:03d}"
                siguiente += 1
            r["archivo"], r["formato"] = Path(ruta).name, fmt
            inventario.append(r)
            for k in claves(r):
                indice.setdefault(k, r)

    for r in inventario:
        completar(r)
    inventario.sort(key=lambda r: str(r.get("id", "")))

    filas = ["| ID | Cita sugerida | Titulo | DOI | Abstract |", "|---|---|---|---|---|"]
    for r in inventario:
        t = r.get("titulo", "")
        t = (t[:70] + "...") if len(t) > 70 else t
        estado = (f"OK ({r['abstract_chars']})" if r["citable_por_contenido"]
                  else f"RECORTADO ({r['abstract_chars']})" if r.get("resumen_parcial") else "FALTA")
        filas.append(f"| {r['id']} | {r['cita_sugerida']} | {t.replace('|', '/')} | "
                     f"{r.get('doi') or '-'} | {estado} |")
    tabla = "\n".join(filas)
    if args.tabla:
        print(tabla)

    con = [r for r in inventario if r["citable_por_contenido"]]
    sin = [r for r in inventario if not r["citable_por_contenido"]]
    print(f"TOTAL: {len(inventario)} fuentes ({n_prev} previas, {len(inventario) - n_prev} nuevas)")
    print(f"CON ABSTRACT (citables por contenido): {len(con)}")
    print(f"SIN ABSTRACT COMPLETO (solo a nivel de titulo): {len(sin)}")
    parciales = [r for r in inventario if r.get("resumen_parcial")]
    if parciales:
        print(f"RESUMEN RECORTADO (no se citan por contenido hasta conseguir el resumen completo): {len(parciales)}")
    print(f"DUPLICADOS descartados: {duplicados}" + (f" (completaron {completados} abstracts)" if completados else ""))
    if sin:
        print("Sin abstract (no se les atribuyen hallazgos ni cifras):")
        for r in sin:
            print(f"  - {r['id']} {r['cita_sugerida']}: {r.get('titulo', '')[:70]}")
    if not inventario:
        print("ADVERTENCIA: no se extrajo ningun registro. Revisar los archivos a mano.")

    Path(args.out).write_text(json.dumps(inventario, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"-> {args.out}")
    if args.md_out:
        Path(args.md_out).write_text(tabla + "\n", encoding="utf-8")
    if fallidos:
        sys.exit(2)


if __name__ == "__main__":
    main()
