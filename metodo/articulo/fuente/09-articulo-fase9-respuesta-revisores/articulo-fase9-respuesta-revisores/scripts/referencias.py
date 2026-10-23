#!/usr/bin/env python3
"""Fuentes citadas: vuelta al gestor (Zotero/Mendeley) y alta de fuentes por DOI verificado.

Solo biblioteca estándar. Trabaja con el inventario.json de inventario_fuentes.py y
con las claves de cita del artículo ([F012], [AR51541814]...).

Subcomandos
-----------
  exportar   Solo las fuentes CITADAS en el artículo, para importarlas en la colección
             del investigador en Zotero o Mendeley:
               python3 referencias.py exportar --inventario inventario.json \\
                   --docx ARTICULO_x_v5.docx --ris CITADAS_x.ris --bib CITADAS_x.bib --dois DOIS_x.txt
             (o --md seccion1.md seccion2.md ... en lugar de --docx). Del .docx lee el
             mapa de citas que guarda articulo_docx.py; si una clave ya no está en el
             inventario, usa la copia de la fuente guardada en el Word.
  doi        Verifica DOIs en Crossref (y, si Crossref no lo tiene, en doi.org) y agrega
             sus metadatos al inventario con un ID nuevo (F...):
               python3 referencias.py doi 10.1108/EBR-11-2018-0203 10.xxxx/yyy --inventario inventario.json
             Un DOI que no existe NO se agrega. Sin red, lo dice y propone la vía
             alternativa. Nunca completa un dato que el registro no trae.
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

RE_ITEM = re.compile(r"\[([A-Z]{1,3}\d{2,})(?::[^\[\]\n]*)?\]")
AGENTE = "RutaArticulo-referencias/1.0 (Acosta IA & Research; python-urllib)"


# ------------------------------------------------------------------ inventario
def cargar(ruta):
    if not ruta or not Path(ruta).exists():
        return []
    datos = json.loads(Path(ruta).read_text(encoding="utf-8"))
    return datos.get("fuentes", datos) if isinstance(datos, dict) else datos


def indice(inv):
    idx = {}
    for r in inv:
        for k in [r.get("id")] + list(r.get("alias") or []):
            if k:
                idx[str(k)] = r
    return idx


# ------------------------------------------------------------------ claves citadas
def claves_docx(ruta):
    """(claves en orden de aparición, copia de fuentes guardada en el Word)."""
    with zipfile.ZipFile(ruta) as z:
        doc = z.read("word/document.xml").decode("utf-8")
        custom = z.read("docProps/custom.xml").decode("utf-8") if "docProps/custom.xml" in z.namelist() else ""
    trozos = sorted(re.findall(r'name="(AcostaCitas_\d+)"[^>]*>\s*<vt:lpwstr>(.*?)</vt:lpwstr>', custom, re.S))
    if not trozos:
        # Word sin mapa: claves que hayan quedado escritas tal cual
        texto = re.sub(r"<[^>]+>", "", doc)
        return list(dict.fromkeys(RE_ITEM.findall(texto))), {}
    import html
    mapa = json.loads(html.unescape("".join(t for _, t in trozos)))
    vivos = re.findall(r'<w:bookmarkStart [^>]*w:name="(_AcCita\d+)"', doc)
    claves = []
    for nombre in vivos:
        claves += RE_ITEM.findall(mapa.get("citas", {}).get(nombre, ""))
    return list(dict.fromkeys(claves)), mapa.get("fuentes") or {}


def claves_md(rutas):
    claves = []
    for r in rutas:
        claves += RE_ITEM.findall(Path(r).read_text(encoding="utf-8"))
    return list(dict.fromkeys(claves))


# ------------------------------------------------------------------ RIS / BibTeX
TY_RIS = {"articulo": "JOUR", "libro": "BOOK", "capitulo": "CHAP", "congreso": "CPAPER", "web": "ELEC", "otro": "GEN"}
TY_BIB = {"articulo": "article", "libro": "book", "capitulo": "incollection", "congreso": "inproceedings",
          "web": "misc", "otro": "misc"}


def _autores(r):
    comp, base = r.get("autores_completos") or [], r.get("autores") or []
    return comp if comp and (len(comp) == len(base) or not base) else base


def _pags(r):
    p = re.split(r"\s*[-–—]+\s*", r.get("paginas") or "", maxsplit=1)
    return (p[0], p[1] if len(p) > 1 else "")


def a_ris(r, clave):
    L = [("TY", TY_RIS.get(r.get("tipo") or "articulo", "GEN"))]
    L += [("AU", a) for a in _autores(r)]
    L += [("TI", r.get("titulo")), ("PY", r.get("anio")),
          ("T2", r.get("fuente")), ("VL", r.get("volumen")), ("IS", r.get("numero"))]
    sp, ep = _pags(r)
    L += [("SP", sp), ("EP", ep), ("C7", r.get("art_no")), ("PB", r.get("editorial"))]
    L += [("ED", e) for e in r.get("editores") or []]
    L += [("DO", r.get("doi")), ("UR", r.get("url") or (f"https://doi.org/{r['doi']}" if r.get("doi") else "")),
          ("Y2", r.get("consultado")), ("AB", r.get("abstract"))]
    L += [("KW", k.strip()) for k in (r.get("keywords") or "").split(";") if k.strip()]
    L += [("ID", clave), ("N1", f"Clave en la Ruta del Artículo: {clave}")]
    out = [f"{t}  - {' '.join(str(v).split())}" for t, v in L if v]
    return "\n".join(out + ["ER  - ", ""])


def _bib_esc(v):
    v = " ".join(str(v).split())
    return re.sub(r"([&%$#_])", r"\\\1", v).replace("{", "").replace("}", "")


def a_bib(r, clave):
    campos = [("author", " and ".join(_autores(r))), ("title", "{" + _bib_esc(r.get("titulo") or "") + "}"),
              ("year", r.get("anio"))]
    fte = r.get("fuente")
    tipo = r.get("tipo") or "articulo"
    campos.append(("journal" if tipo == "articulo" else "booktitle" if tipo in ("capitulo", "congreso")
                   else "howpublished", fte))
    sp, ep = _pags(r)
    campos += [("volume", r.get("volumen")), ("number", r.get("numero")),
               ("pages", f"{sp}--{ep}" if ep else sp), ("article-number", r.get("art_no")),
               ("publisher", r.get("editorial")), ("editor", " and ".join(r.get("editores") or [])),
               ("doi", r.get("doi")), ("url", r.get("url")), ("urldate", r.get("consultado")),
               ("keywords", r.get("keywords")), ("abstract", r.get("abstract")), ("note", f"Clave en la Ruta del Artículo: {clave}")]
    cuerpo = ",\n".join(f"  {k} = {{{v if k == 'title' else _bib_esc(v)}}}" for k, v in campos if v and v != "{}")
    return f"@{TY_BIB.get(tipo, 'misc')}{{{clave},\n{cuerpo}\n}}\n"


def cmd_exportar(a):
    idx = indice(cargar(a.inventario))
    if a.docx:
        claves, snap = claves_docx(a.docx)
    else:
        claves, snap = claves_md(a.md), {}
    for k, r in snap.items():
        idx.setdefault(k, r)
        for al in r.get("alias") or []:
            idx.setdefault(al, r)
    citadas, vistos, faltan = [], set(), []
    for k in claves:
        r = idx.get(k)
        if r is None:
            faltan.append(k)
        elif r["id"] not in vistos:
            vistos.add(r["id"])
            citadas.append(r)
    if not claves:
        sys.exit("No encontré citas por clave ([F012]) en el documento.")
    if a.ris:
        Path(a.ris).write_text("\n".join(a_ris(r, r["id"]) for r in citadas), encoding="utf-8")
    if a.bib:
        Path(a.bib).write_text("\n".join(a_bib(r, r["id"]) for r in citadas), encoding="utf-8")
    if a.dois:
        Path(a.dois).write_text("\n".join(r["doi"] for r in citadas if r.get("doi")) + "\n", encoding="utf-8")
    sin_doi = [r["id"] for r in citadas if not r.get("doi")]
    print(f"CITADAS: {len(citadas)} fuentes ({len(claves)} claves distintas en el texto)")
    for destino in (a.ris, a.bib, a.dois):
        if destino:
            print(f"-> {destino}")
    if sin_doi:
        print(f"Sin DOI (no van en {a.dois or 'la lista de DOIs'}; se importan por el RIS/BibTeX): {', '.join(sin_doi)}")
    if faltan:
        print(f"✗ Claves que no están en el inventario (no se exportan): {', '.join(faltan)}")
        sys.exit(1)


# ------------------------------------------------------------------ DOI
def _get(url, accept="application/json"):
    req = urllib.request.Request(url, headers={"User-Agent": AGENTE, "Accept": accept})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _limpia(t):
    t = t[0] if isinstance(t, list) else t
    return " ".join(re.sub(r"<[^>]+>", " ", t or "").split())


def _registro_csl(m, doi):
    """Mensaje de Crossref o CSL-JSON de doi.org → registro del inventario (solo lo que trae)."""
    autores, completos = [], []
    for au in m.get("author") or []:
        fam, giv = (au.get("family") or "").strip(), (au.get("given") or "").strip()
        if fam:
            ini = " ".join("-".join(p[0] + "." for p in tok.split("-") if p)
                           for tok in re.split(r"[\s.]+", giv) if tok and tok[0].isupper())
            autores.append(f"{fam}, {ini}".rstrip(", "))
            completos.append(f"{fam}, {giv}".rstrip(", "))
        elif au.get("name") or au.get("literal"):
            autores.append(au.get("name") or au.get("literal"))
            completos.append(au.get("name") or au.get("literal"))
    editores = [f"{e.get('family', '')}, {e.get('given', '')}".strip(", ") for e in m.get("editor") or []]
    fecha = None
    for k in ("published-print", "published-online", "issued", "published", "created"):
        dp = (m.get(k) or {}).get("date-parts") or [[None]]
        if dp and dp[0] and dp[0][0]:
            fecha = dp[0][0]
            break
    tipo = {"journal-article": "articulo", "book": "libro", "monograph": "libro", "edited-book": "libro",
            "book-chapter": "capitulo", "book-section": "capitulo", "chapter": "capitulo",
            "proceedings-article": "congreso", "paper-conference": "congreso", "posted-content": "otro",
            "article-journal": "articulo", "webpage": "web", "dataset": "otro"}.get(m.get("type", ""), "otro")
    r = {"autores": autores, "anio": str(fecha or ""), "titulo": _limpia(m.get("title")).rstrip("."),
         "fuente": _limpia(m.get("container-title")), "doi": doi.strip(),
         "abstract": _limpia(m.get("abstract")), "keywords": "; ".join(m.get("subject") or [])}
    if any(re.search(r",\s*\w{2,}", c) for c in completos):
        r["autores_completos"] = completos
    extra = {"volumen": m.get("volume"), "numero": m.get("issue"),
             "paginas": re.sub(r"\s*[-–—]+\s*", "-", str(m.get("page") or "")),
             "art_no": m.get("article-number"), "editorial": m.get("publisher"),
             "url": f"https://doi.org/{doi}"}
    for k, v in extra.items():
        if v:
            r[k] = str(v)
    if editores:
        r["editores"] = editores
    r["tipo"] = tipo
    return r


def verificar_doi(doi):
    """(registro | None, estado). estado: 'ok', 'no existe', 'sin red'."""
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", doi.strip(), flags=re.I)
    try:
        m = _get("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/"))["message"]
        return _registro_csl(m, doi), "ok (Crossref)"
    except urllib.error.HTTPError as e:
        if e.code != 404:
            return None, f"error {e.code} de Crossref"
    except (urllib.error.URLError, TimeoutError, OSError):
        return None, "sin red"
    try:   # DOI de otra agencia (DataCite, mEDRA...): negociación de contenido en doi.org
        m = _get("https://doi.org/" + urllib.parse.quote(doi, safe="/"), "application/vnd.citationstyles.csl+json")
        return _registro_csl(m, doi), "ok (doi.org)"
    except urllib.error.HTTPError as e:
        return None, "no existe" if e.code == 404 else f"error {e.code} de doi.org"
    except (urllib.error.URLError, TimeoutError, OSError, ValueError):
        return None, "sin red"


def _completar(r):
    try:
        sys.dont_write_bytecode = True          # no dejar __pycache__ en la carpeta de la skill
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from inventario_fuentes import completar
        completar(r)
    except ImportError:
        ab = r.get("abstract") or ""
        r["abstract_chars"] = len(ab)
        r["resumen_parcial"] = False
        r["citable_por_contenido"] = len(ab) >= 120
        ap = [a.split(",")[0] for a in r.get("autores") or []]
        r["cita_sugerida"] = (" y ".join(ap) if len(ap) <= 2 else ap[0] + " et al.") + " " + (r.get("anio") or "s. f.") \
            if ap else "[POR CONFIRMAR: autor]"


def cmd_doi(a):
    inv = cargar(a.inventario)
    por_doi = {(r.get("doi") or "").lower(): r for r in inv if r.get("doi")}
    sig = max([int(m.group(1)) for r in inv for m in [re.match(r"F(\d+)$", str(r.get("id", "")))] if m] or [0]) + 1
    agregados, sin_red, malos = 0, [], []
    for doi in a.dois:
        limpio = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", doi.strip(), flags=re.I)
        if limpio.lower() in por_doi:
            print(f"= {limpio}: ya está en el inventario como {por_doi[limpio.lower()]['id']}")
            continue
        r, estado = verificar_doi(limpio)
        if r is None:
            print(f"✗ {limpio}: {estado.upper()}")
            (sin_red if estado == "sin red" else malos).append(limpio)
            continue
        r["id"] = f"F{sig:03d}"
        sig += 1
        r["archivo"], r["formato"], r["doi_verificado"] = "doi.org", "crossref", True
        _completar(r)
        inv.append(r)
        por_doi[r["doi"].lower()] = r
        agregados += 1
        au = r["autores"][0].split(",")[0] + (" et al." if len(r["autores"]) > 2 else "") if r["autores"] else "?"
        print(f"✓ {limpio}: {estado} → {r['id']}  {au} ({r['anio'] or 's. f.'}). {r['titulo'][:70]}"
              + ("" if r.get("abstract") else "  [sin resumen: se cita solo por el título]"))
    if agregados:
        Path(a.out or a.inventario).write_text(json.dumps(inv, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"-> {a.out or a.inventario} ({agregados} fuentes nuevas)")
    if malos:
        print("Los DOIs marcados ✗ no se agregan: comprobar que estén bien copiados (doi.org/<DOI> en el navegador)."
              " No se cita una fuente cuyo DOI no resuelve.")
    if sin_red:
        print("SIN CONEXIÓN: no pude verificar " + ", ".join(sin_red) + ". Alternativas: (1) con la plataforma Acosta"
              " conectada, buscar la fuente con `buscar_fuentes` y pegar su ficha en el inventario (formato «acosta»);"
              " (2) exportarla desde Zotero o Mendeley en RIS o BibTeX y pasarla por inventario_fuentes.py;"
              " (3) volver a correr este comando cuando haya red. No se escriben metadatos a mano.")
    sys.exit(0 if not (malos or sin_red) else (3 if sin_red and not malos else 1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("exportar", help="RIS/BibTeX/DOIs de las fuentes citadas")
    p.add_argument("--inventario", required=True)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--docx")
    g.add_argument("--md", nargs="+")
    p.add_argument("--ris"); p.add_argument("--bib"); p.add_argument("--dois")
    p.set_defaults(f=cmd_exportar)
    p = sub.add_parser("doi", help="verifica DOIs y los agrega al inventario")
    p.add_argument("dois", nargs="+")
    p.add_argument("--inventario", required=True, help="inventario.json (se crea si no existe)")
    p.add_argument("--out", help="otro archivo de salida (por defecto, el mismo inventario)")
    p.set_defaults(f=cmd_doi)
    a = ap.parse_args()
    if a.cmd == "exportar" and not (a.ris or a.bib or a.dois):
        ap.error("indica al menos --ris, --bib o --dois")
    a.f(a)


if __name__ == "__main__":
    main()
