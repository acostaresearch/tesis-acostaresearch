#!/usr/bin/env python3
"""
Analisis bibliometrico sin R: alternativa en Python a bibliometrix.

Para cuando el investigador trabaja en un chat que solo ejecuta Python (por
ejemplo ChatGPT con analisis de datos) o no tiene R. Solo biblioteca estandar;
matplotlib es opcional (si esta, se generan las figuras PNG).

Orden de preferencia de la ruta (references/revision.md):
  1) servidor Acosta con bibliometrix (`trabajar_en_r`);
  2) R propio con bibliometrix;
  3) este script. Sus resultados se declaran en Metodos como calculados con un
     script propio de la ruta (bibliometria.py), citando los metodos clasicos
     (ley de Bradford, 1934; ley de Lotka, 1926), no como bibliometrix.

Uso
---
    python3 bibliometria.py informe scopus.csv savedrecs.txt --out salida/
    python3 bibliometria.py fusionar scopus.csv savedrecs.txt --out salida/
Opciones: --anio-ref 2026 (anio de referencia para edad y citas por anio; por
defecto el actual), --top 10, --prioridad wos|scopus (que registro se conserva
en un duplicado; wos por defecto, como bibliometrix), --quitar-doi-distinto
(retira tambien los posibles duplicados con DOI distinto en lugar de solo
listarlos), --tabla-inicial N y --figura-inicial N (numeracion del Markdown),
--min-kw 5 (frecuencia minima para la red de VOSviewer).

Entrada (se detecta por el contenido): CSV de Scopus (Export > CSV, con
Abstract & keywords e Include references) y texto plano de Web of Science
(Full record and cited references). Varios archivos de cada base se suman.

Salidas en --out
----------------
  resumen_bibliometrico.md   cifras clave y tablas en la sintaxis del motor
                             ([TABLA n] titulo / tabla con barras / [NOTA]) y
                             [FIGURA n] titulo | archivo.png, para la Fase 5
  prisma_conteos.csv         registros por base, duplicados, cribados
  posibles_duplicados.csv    mismo titulo y anio con DOI distinto (decision humana)
  corpus_fusionado.csv       un registro por documento tras la fusion
  informacion_principal.csv, produccion_anual.csv, fuentes_bradford.csv,
  autores.csv, lotka.csv, paises_autor_correspondencia.csv,
  produccion_paises.csv, mas_citados.csv, palabras_clave_autor.csv,
  coocurrencia_pares.csv, coocurrencia_matriz.csv (top 50, cuadrada),
  vosviewer_map.txt + vosviewer_network.txt (Open > Map file / Network file)
  fig_produccion_anual.png, fig_bradford.png, fig_lotka.png,
  fig_fuentes.png, fig_palabras_clave.png        (si hay matplotlib)

Reglas de calculo (las mismas que bibliometrix 5.4 salvo donde se indica)
-----------------------------------------------------------------------
  Fusion: se leen primero los registros de WoS y luego los de Scopus (como
    mergeDbSources). Duplicado 1: mismo DOI (sin distinguir mayusculas).
    Duplicado 2: mismo titulo normalizado + mismo anio cuando al menos uno de
    los dos no tiene DOI. El titulo se normaliza en mayusculas, sin la
    traduccion final entre corchetes que agrega Scopus ("...; [Titulo
    original]"), sin tildes y sin signos. Mismo titulo y anio con DOI
    distinto: NO se retira, se lista en posibles_duplicados.csv para decision
    humana (bibliometrix lo retira sin avisar). Con --quitar-doi-distinto se
    retiran y el conteo coincide con bibliometrix.
  Autores: en mayusculas, sin puntos ni comas. Si se mezclan bases, cada
    nombre se reduce a "PRIMER-TOKEN + iniciales" (Mercado Rivas R.Y. ->
    MERCADO R R; Ford, ME -> FORD M), igual que mergeDbSources, para que el
    mismo autor coincida entre Scopus y WoS. Con una sola base se conserva el
    nombre tal cual. Los apellidos compuestos quedan partidos: es la misma
    limitacion que bibliometrix y debe revisarse a mano en el top de autores.
  Fuentes: titulo de la fuente en mayusculas sin comas, sin unificar
    variantes entre bases (SUSTAINABILITY vs SUSTAINABILITY (SWITZERLAND));
    las variantes probables se listan en el resumen para revisar.
  Palabras clave (DE, ID): mayusculas; separador ";"; puntos y comas -> espacio.
  Crecimiento anual compuesto: ((n_ultimo / n_primero)^(1/(anios-1)) - 1)*100;
    se avisa si el ultimo anio es el de referencia (incompleto) y se da
    tambien la tasa sin ese anio.
  Edad media: anio_ref - media(PY). Citas por anio: TC / (anio_ref - PY + 1).
  Bradford: fuentes ordenadas por documentos; zonas por tercios del
    acumulado (zona 1 si acumulado <= N/3, zona 2 si <= 2N/3).
  Lotka: distribucion observada de autores por numero de documentos;
    regresion de minimos cuadrados log10(proporcion) ~ log10(n);
    beta = |pendiente|, C = 10^intercepto, R2 (identico a lotka() de
    bibliometrix).
  Paises: se busca el pais en la ultima parte de cada afiliacion. Pais del
    documento = pais del autor de correspondencia (RP); si el documento no
    trae RP, el de la primera afiliacion (bibliometrix deja ese documento sin
    pais). SCP/MCP y % de coautoria internacional = documentos con autores de
    mas de un pais, usando todas las afiliaciones.

Validacion contra bibliometrix 5.4.1 (R), corpus real de la ruta (Scopus CSV
1134 + WoS texto plano 50 registros; anio de referencia 2026)
---------------------------------------------------------------------------
Con --modo bibliometrix (replica mergeDbSources) coinciden EXACTAMENTE:
documentos tras fusion 1159 (25 duplicados), produccion anual anio por anio
(2015 = 43 ... 2026 = 162), tasa de crecimiento 12.82 %, edad media 4.07,
citas medias 8.041 y por anio 1.384, top 15 de fuentes con sus conteos, top
15 de autores (completo y fraccionado: LI Y 7 / BENITES L 2.00), top 15 de
palabras clave de autor con sus frecuencias, Keywords Plus 1426, top 15 de
citados (TC y TC por anio), tipos de documento. Diferencias, todas
atribuibles a bibliometrix y explicadas:
  - Fuentes 574 vs 577: read_csv(trim_ws = FALSE) deja un espacio final en
    3 titulos de Scopus ("JOURNAL OF ... PRACTICE ") y los cuenta como
    fuentes distintas; aqui se recortan.
  - Autores 4624 vs 4625, apariciones 5024 vs 5025, autores de documentos de
    un solo autor 161 vs 162, documentos de un solo autor 162 vs 163,
    coautores por documento 4.33 vs 4.34, Lotka beta 4.3032 vs 4.3033 (C
    0.9857 y R2 0.9989 iguales): bibliometrix cuenta el marcador de Scopus
    "No authorship indicated" como un autor; aqui ese documento queda sin
    autores.
  - Palabras clave de autor distintas 3415 vs 3417: dos palabras con espacio
    duro (U+00A0) que R no unifica y Python si ("RESEARCH ACTIVITIES" 6 vs
    5 + 1).
  - Coautoria internacional 16.57 % vs 0.95 %: al fusionar, bibliometrix
    marca todo como ISI y busca "PAIS." (formato WoS) en las afiliaciones de
    Scopus, que terminan en "Pais;", y casi nunca halla dos paises. En la
    base Scopus sola, donde bibliometrix lee bien su formato: 16.49 % aqui vs
    15.34 % en bibliometrix (este script suma tambien el pais del autor de
    correspondencia).
  - Paises por autor de correspondencia: en 916 de los 932 documentos con
    pais en ambos el pais coincide; las 16 diferencias son errores de
    bibliometrix al buscar el nombre del pais en todo el texto (GEORGIA el
    estado de EE. UU., JORDAN como apellido, NEW MEXICO) o eleccion del
    primer pais por orden alfabetico, y Taiwan, que bibliometrix suma a
    China y aqui se informa como Taiwan. Ademas, bibliometrix deja sin pais
    227 documentos (sin "Correspondence Address"); aqui se toma la primera
    afiliacion y quedan 7 sin pais. Por eso USA 364 vs 302.
  - Referencias citadas: bibliometrix pone "NA" en CR al fusionar bases
    (informa 1 referencia); aqui se informan las de cada base por separado.
Con el modo por defecto (ruta) cambian dos registros respecto de
bibliometrix, por diseno: (a) "Research Competences in University Training;
[Las competencias investigadoras...]" de Scopus, sin DOI, se retira como
duplicado del registro de WoS (bibliometrix no lo ve porque no quita la
traduccion entre corchetes); (b) dos registros de Scopus con el mismo titulo
y anio (2015) y DOI distinto se conservan y se listan en
posibles_duplicados.csv (bibliometrix retira uno sin avisar). El total sigue
siendo 1159 por compensacion; la produccion anual cambia en 2015 (44 vs 43)
y 2021 (74 vs 75), la tasa de crecimiento queda en 12.58 % y Lotka en beta
4.2660. Si el investigador confirma que el par es duplicado, se usa
--quitar-doi-distinto (1158 documentos).
Empates en los top-k: orden alfabetico, como en R (R ordena segun el idioma
del sistema y Python por codigo Unicode; con tildes puede variar un empate).
"""

import argparse
import csv
import datetime
import io
import math
import os
import re
import sys
import unicodedata
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

try:
    csv.field_size_limit(2 ** 31 - 1)
except OverflowError:  # pragma: no cover
    csv.field_size_limit(10 ** 8)


# --------------------------------------------------------------------------
# Lectura
# --------------------------------------------------------------------------
def leer(ruta):
    datos = Path(ruta).read_bytes()
    for enc in ("utf-8-sig", "utf-16", "cp1252", "latin-1"):
        try:
            texto = datos.decode(enc)
            if enc == "utf-16" and "\x00" in texto:
                continue
            return texto.replace("\r\n", "\n").replace("\r", "\n")
        except UnicodeError:
            continue
    return datos.decode("utf-8", errors="replace")


def detectar(texto):
    if re.search(r"^(PT|FN) ", texto, re.M) and re.search(r"^ER\s*$", texto, re.M):
        return "wos"
    cab = texto.lstrip().split("\n", 1)[0].lower()
    if "source title" in cab and "title" in cab:
        return "scopus_csv"
    return None


def mayus(s):
    """Mayusculas como toupper de R (no convierte la eszett en SS)."""
    return "".join(c if c == "\u00df" else c.upper() for c in s)


def _sep(valor, sep=";"):
    return [v.strip() for v in valor.split(sep) if v.strip()]


def _limpia_espacios(s):
    return re.sub(r"\s+", " ", s or "").strip()


def _anio(valor):
    m = re.search(r"\d{4}", valor or "")
    return int(m.group(0)) if m else None


def _entero(valor):
    m = re.search(r"\d+", valor or "")
    return int(m.group(0)) if m else 0


def _registro(db):
    return {"DB": db, "AU": [], "TI": "", "SO": "", "PY": None, "DI": "", "TC": 0,
            "DE": [], "ID": [], "C1": [], "RP": "", "CR": [], "DT": "", "UT": "",
            "LA": ""}


def parse_scopus_csv(texto):
    regs = []
    for fila in csv.DictReader(io.StringIO(texto)):
        f = {k.strip().lstrip("﻿"): (v or "") for k, v in fila.items() if k}
        r = _registro("SCOPUS")
        au = f.get("Authors", "")
        if "no author" in au.lower() or "no authorship" in au.lower():
            au = ""
        r["AU"] = [mayus(_limpia_espacios(a.replace(".", "").replace(",", "")))
                   for a in au.split(";") if a.strip()]
        r["TI"] = _limpia_espacios(f.get("Title", ""))
        r["SO"] = _limpia_espacios(f.get("Source title", ""))
        r["PY"] = _anio(f.get("Year", ""))
        r["DI"] = f.get("DOI", "").strip()
        r["TC"] = _entero(f.get("Cited by", ""))
        r["DE"] = _sep(f.get("Author Keywords", ""))
        r["ID"] = _sep(f.get("Index Keywords", ""))
        r["C1"] = _sep(f.get("Affiliations", ""))
        r["RP"] = f.get("Correspondence Address", "").strip()
        r["CR"] = _sep(f.get("References", ""))
        r["DT"] = f.get("Document Type", "").strip()
        r["UT"] = f.get("EID", "").strip()
        r["LA"] = f.get("Language of Original Document", "").strip()
        regs.append(r)
    return regs


def parse_wos(texto):
    regs, actual, tag = [], None, None
    for linea in texto.split("\n"):
        if not linea.strip():
            continue
        if linea.startswith("   ") and actual is not None and tag:
            actual.setdefault(tag, []).append(linea.strip())
            continue
        t, resto = linea[:2], linea[3:].strip() if len(linea) > 3 else ""
        if t in ("FN", "VR", "EF"):
            continue
        if t == "PT":
            actual, tag = {"PT": [resto]}, "PT"
            continue
        if t == "ER":
            if actual is not None:
                regs.append(actual)
            actual, tag = None, None
            continue
        if actual is not None:
            tag = t
            actual.setdefault(tag, []).append(resto)
    out = []
    for d in regs:
        j = lambda k: _limpia_espacios(" ".join(d.get(k, [])))
        r = _registro("WOS")
        r["AU"] = [mayus(_limpia_espacios(a.replace(",", " ")))
                   for a in d.get("AU", []) if a.strip()]
        r["TI"] = j("TI")
        r["SO"] = j("SO")
        r["PY"] = _anio(j("PY")) or _anio(j("EA"))
        r["DI"] = j("DI")
        r["TC"] = _entero(j("TC"))
        r["DE"] = _sep(j("DE"))
        r["ID"] = _sep(j("ID"))
        r["C1"] = [re.sub(r"^\[[^\]]*\]\s*", "", c).strip() for c in d.get("C1", [])]
        r["RP"] = j("RP")
        r["CR"] = [c for c in d.get("CR", []) if c]
        r["DT"] = j("DT")
        r["UT"] = j("UT")
        r["LA"] = j("LA")
        out.append(r)
    return out


def cargar(rutas):
    registros, por_base, problemas = [], OrderedDict(), []
    for ruta in rutas:
        texto = leer(ruta)
        fmt = detectar(texto)
        if fmt == "wos":
            regs = parse_wos(texto)
            base = "Web of Science"
        elif fmt == "scopus_csv":
            regs = parse_scopus_csv(texto)
            base = "Scopus"
        else:
            problemas.append(str(ruta))
            continue
        por_base[base] = por_base.get(base, 0) + len(regs)
        for r in regs:
            r["ARCHIVO"] = Path(ruta).name
        registros.extend(regs)
    return registros, por_base, problemas


# --------------------------------------------------------------------------
# Normalizacion
# --------------------------------------------------------------------------
def sin_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def doi_norm(d):
    d = (d or "").strip().lower()
    d = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", d)
    return d


def titulo_norm(t):
    t = re.sub(r";?\s*\[[^\]]*\]\s*$", "", t or "")   # traduccion final de Scopus
    t = sin_tildes(t).upper()
    t = "".join(c if (c.isalnum() or c == " ") else "" for c in t)
    return re.sub(r"\s+", " ", t).strip()


def autor_fusion(nombre):
    """Apellido (primer token) + iniciales, como mergeDbSources de bibliometrix."""
    partes = nombre.replace(",", " ").strip().split(" ")
    partes = [p for p in partes if p != ""] or [""]
    return (partes[0] + " " + " ".join(p[0] for p in partes[1:])).strip()


def kw_norm(k):
    return re.sub(r"\s+|\.|,", " ", mayus(k)).strip()


def fuente_norm(s):
    return _limpia_espacios(mayus(s).replace(",", ""))


# --------------------------------------------------------------------------
# Paises
# --------------------------------------------------------------------------
PAISES = [
    "AFGHANISTAN", "ALBANIA", "ALGERIA", "ANDORRA", "ANGOLA", "ANTIGUA", "ARGENTINA",
    "ARMENIA", "AUSTRALIA", "AUSTRIA", "AZERBAIJAN", "BAHAMAS", "BAHRAIN", "BANGLADESH",
    "BARBADOS", "BELARUS", "BELGIUM", "BELIZE", "BENIN", "BHUTAN", "BOLIVIA", "BOSNIA",
    "BOTSWANA", "BRAZIL", "BRUNEI", "BULGARIA", "BURKINA FASO", "BURUNDI", "CABO VERDE",
    "CAMBODIA", "CAMEROON", "CANADA", "CENTRAL AFRICAN REPUBLIC", "CHAD", "CHILE", "CHINA",
    "COLOMBIA", "COMOROS", "CONGO", "COSTA RICA", "COTE D IVOIRE", "CROATIA", "CUBA",
    "CYPRUS", "CZECH REPUBLIC", "DENMARK", "DJIBOUTI", "DOMINICA", "DOMINICAN REPUBLIC",
    "ECUADOR", "EGYPT", "EL SALVADOR", "EQUATORIAL GUINEA", "ERITREA", "ESTONIA",
    "SWAZILAND", "ETHIOPIA", "FAROE", "FIJI", "FINLAND", "FRANCE", "GABON", "GAMBIA",
    "GEORGIA", "GERMANY", "GHANA", "GREECE", "GUAM", "GUATEMALA", "GUINEA",
    "GUINEA BISSAU", "HAITI", "HONDURAS", "HONG KONG", "HUNGARY", "ICELAND", "INDIA",
    "INDONESIA", "IRAN", "IRAQ", "IRELAND", "ISRAEL", "ITALY", "JAMAICA", "JAPAN",
    "JORDAN", "KAZAKHSTAN", "KENYA", "KIRIBATI", "KOREA", "KOSOVO", "KUWAIT",
    "KYRGYZSTAN", "LAOS", "LATVIA", "LEBANON", "LESOTHO", "LIBERIA", "LIBYA",
    "LIECHTENSTEIN", "LITHUANIA", "LUXEMBOURG", "MACEDONIA", "MADAGASCAR", "MALAWI",
    "MALAYSIA", "MALDIVES", "MALI", "MALTA", "MARSHALL ISLANDS", "MAURITANIA",
    "MAURITIUS", "MEXICO", "MICRONESIA", "MOLDOVA", "MONACO", "MONGOLIA", "MONTENEGRO",
    "MOROCCO", "MOZAMBIQUE", "MYANMAR", "NAMIBIA", "NAURU", "NEPAL", "NETHERLANDS",
    "NEW ZEALAND", "NICARAGUA", "NIGER", "NIGERIA", "NORTH KOREA", "NORWAY", "OMAN",
    "PAKISTAN", "PALAU", "PALESTINE", "PANAMA", "PAPUA NEW GUINEA", "PARAGUAY", "PERU",
    "PHILIPPINES", "POLAND", "PORTUGAL", "PUERTO RICO", "QATAR", "ROMANIA", "RUSSIA",
    "RWANDA", "SAINT KITTS AND NEVIS", "SAINT LUCIA", "SAMOA", "SAN MARINO",
    "SAO TOME AND PRINCIPE", "SAUDI ARABIA", "SENEGAL", "SERBIA", "SEYCHELLES",
    "SIERRA LEONE", "SINGAPORE", "SLOVAKIA", "SLOVENIA", "SOLOMON ISLANDS", "SOMALIA",
    "SOUTH AFRICA", "SOUTH SUDAN", "SPAIN", "SRI LANKA", "SUDAN", "SURINAME", "SWEDEN",
    "SWITZERLAND", "SYRIA", "TAIWAN", "TAJIKISTAN", "TANZANIA", "THAILAND", "TOGO",
    "TONGA", "TRINIDAD AND TOBAGO", "TUNISIA", "TURKEY", "TURKMENISTAN", "UGANDA",
    "UKRAINE", "UNITED ARAB EMIRATES", "UNITED KINGDOM", "URUGUAY", "USA", "UZBEKISTAN",
    "VANUATU", "VATICAN", "VENEZUELA", "VIETNAM", "YEMEN", "ZAMBIA", "ZIMBABWE",
    "MACAO", "LUXEMBURG",
]
ALIAS = {
    "UNITED STATES": "USA", "UNITED STATES OF AMERICA": "USA", "U S A": "USA",
    "ENGLAND": "UNITED KINGDOM", "SCOTLAND": "UNITED KINGDOM", "WALES": "UNITED KINGDOM",
    "NORTH IRELAND": "UNITED KINGDOM", "NORTHERN IRELAND": "UNITED KINGDOM",
    "RUSSIAN FEDERATION": "RUSSIA", "TURKIYE": "TURKEY", "CZECHIA": "CZECH REPUBLIC",
    "ESWATINI": "SWAZILAND", "SOUTH KOREA": "KOREA", "REPUBLIC OF KOREA": "KOREA",
    "VIET NAM": "VIETNAM", "U ARAB EMIRATES": "UNITED ARAB EMIRATES", "UAE": "UNITED ARAB EMIRATES",
    "NORTH MACEDONIA": "MACEDONIA", "BRUNEI DARUSSALAM": "BRUNEI", "MACAU": "MACAO",
    "LUXEMBURG": "LUXEMBOURG", "VATICANO": "VATICAN", "SYRIAN ARAB REPUBLIC": "SYRIA",
    "LAO PEOPLE S DEMOCRATIC REPUBLIC": "LAOS", "IVORY COAST": "COTE D IVOIRE",
    "CAPE VERDE": "CABO VERDE", "STATE OF PALESTINE": "PALESTINE",
}
_NOMBRES = sorted(set(PAISES) | set(ALIAS), key=len, reverse=True)
_RE_PAIS = re.compile(r"\b(" + "|".join(re.escape(n) for n in _NOMBRES) + r")\b")


def _norm_geo(s):
    s = sin_tildes(s or "").upper()
    return re.sub(r"\s+", " ", re.sub(r"[^A-Z0-9 ]", " ", s)).strip()


def pais_de(afiliacion):
    """Pais de una afiliacion: ultima coincidencia en la ultima parte; si no, en todo el texto."""
    if not afiliacion:
        return None
    partes = [p for p in afiliacion.split(",") if p.strip()]
    for trozo in ([partes[-1]] if partes else []) + [afiliacion]:
        hall = _RE_PAIS.findall(_norm_geo(trozo))
        if hall:
            n = hall[-1]
            return ALIAS.get(n, n)
    return None


def pais_correspondencia(r):
    rp = r["RP"]
    if not rp:
        return None
    if r["DB"] == "WOS":
        for trozo in re.split(r"\.\s*;\s*", rp):
            trozo = re.sub(r"^.*?\((corresponding|reprint) author\)\s*,?\s*", "", trozo, flags=re.I)
            p = pais_de(trozo.rstrip("."))
            if p:
                return p
        return None
    for trozo in rp.split(";"):
        t = trozo.strip()
        if not t or t.lower().startswith("email") or "," not in t:
            continue
        p = pais_de(t)
        if p:
            return p
    return None


# --------------------------------------------------------------------------
# Fusion y deduplicacion
# --------------------------------------------------------------------------
def titulo_norm_bibliometrix(t):
    """Clave de mergeDbSources: mayusculas, sin signos, espacios simples (no quita corchetes)."""
    t = "".join(c for c in mayus(t or "") if c.isalnum() or c == " ")
    return re.sub(r"\s+", " ", t).strip()


def fusionar(registros, prioridad="wos", quitar_doi_distinto=False, modo="ruta"):
    """modo="ruta": reglas descritas arriba. modo="bibliometrix": replica
    mergeDbSources (DOI literal; luego titulo sin signos + anio, sin quitar la
    traduccion entre corchetes y retirando tambien los de DOI distinto). Solo
    para validar contra R."""
    orden = {"WOS": 0, "SCOPUS": 1} if prioridad == "wos" else {"SCOPUS": 0, "WOS": 1}
    regs = sorted(registros, key=lambda r: orden.get(r["DB"], 2))   # sort estable
    if modo == "bibliometrix":
        quitar_doi_distinto = True
    por_doi, por_tit = {}, {}
    finales, quitados_doi, quitados_tit, posibles = [], [], [], []
    for r in regs:
        if modo == "bibliometrix":
            d = (r["DI"] or "").strip()
            tk = (titulo_norm_bibliometrix(r["TI"]), r["PY"])
        else:
            d = doi_norm(r["DI"])
            tk = (titulo_norm(r["TI"]), r["PY"])
        if d and d in por_doi:
            quitados_doi.append((r, por_doi[d]))
            continue
        previo = por_tit.get(tk) if tk[0] else None
        if previo is not None:
            dp = doi_norm(previo["DI"])
            if not d or not dp or modo == "bibliometrix":
                quitados_tit.append((r, previo))
                continue
            posibles.append((r, previo))
            if quitar_doi_distinto:
                continue
        finales.append(r)
        if d:
            por_doi[d] = r
        if tk[0] and tk not in por_tit:
            por_tit[tk] = r
    bases = set(r["DB"] for r in finales)
    for r in finales:
        r["AUN"] = [autor_fusion(a) for a in r["AU"]] if len(bases) > 1 else list(r["AU"])
        r["AUN"] = [a for a in r["AUN"] if a]
    return finales, quitados_doi, quitados_tit, posibles


# --------------------------------------------------------------------------
# Indicadores
# --------------------------------------------------------------------------
def orden_desc(contador):
    return sorted(contador.items(), key=lambda kv: (-kv[1], kv[0]))


def regresion(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b = sxy / sxx if sxx else float("nan")
    a = my - b * mx
    sst = sum((y - my) ** 2 for y in ys)
    sse = sum((y - (a + b * x)) ** 2 for x, y in zip(xs, ys))
    r2 = 1 - sse / sst if sst else float("nan")
    return a, b, r2


def analizar(docs, anio_ref, top=10):
    R = {}
    n = len(docs)
    anios = [d["PY"] for d in docs if d["PY"]]
    prod = Counter(anios)
    a0, a1 = min(anios), max(anios)
    serie = [(y, prod.get(y, 0)) for y in range(a0, a1 + 1)]
    R["serie"] = serie
    ny = a1 - a0
    cagr = ((serie[-1][1] / serie[0][1]) ** (1.0 / ny) - 1) * 100 if ny and serie[0][1] else float("nan")
    R["cagr"] = cagr
    R["incompleto"] = a1 >= anio_ref
    if R["incompleto"] and ny > 1 and serie[0][1]:
        R["cagr_sin_ultimo"] = ((serie[-2][1] / serie[0][1]) ** (1.0 / (ny - 1)) - 1) * 100
    else:
        R["cagr_sin_ultimo"] = None

    # Autores
    aut, frac = Counter(), defaultdict(float)
    n_au = []
    primeros_solo = set()
    for d in docs:
        lst = d["AUN"]
        n_au.append(len(lst))
        for a in lst:
            aut[a] += 1
            frac[a] += 1.0 / len(lst)
        if len(lst) == 1:
            primeros_solo.add(lst[0])
    R["autores"] = aut
    R["autores_frac"] = frac
    R["n_autores"] = len(aut)
    R["apariciones"] = sum(n_au)
    R["docs_un_autor"] = sum(1 for k in n_au if k == 1)
    R["autores_un_autor"] = len(primeros_solo)
    R["docs_sin_autor"] = sum(1 for k in n_au if k == 0)
    R["coautores_doc"] = sum(n_au) / n

    # Lotka
    dist = Counter(aut.values())
    filas = sorted(dist.items())
    tot = sum(v for _, v in filas)
    xs = [math.log10(k) for k, _ in filas]
    ys = [math.log10(v / tot) for _, v in filas]
    a, b, r2 = regresion(xs, ys) if len(filas) > 1 else (float("nan"),) * 3
    R["lotka"] = {"dist": [(k, v, v / tot) for k, v in filas], "beta": abs(b),
                  "C": 10 ** a, "R2": r2}

    # Fuentes y Bradford
    fuentes = Counter(fuente_norm(d["SO"]) for d in docs if d["SO"])
    R["fuentes"] = fuentes
    ordf = orden_desc(fuentes)
    total = sum(fuentes.values())
    acum, brad = 0, []
    for rango, (s, k) in enumerate(ordf, 1):
        acum += k
        zona = 1 if acum <= total / 3 else (2 if acum <= 2 * total / 3 else 3)
        brad.append((rango, s, k, acum, zona))
    R["bradford"] = brad
    zonas = OrderedDict()
    for z in (1, 2, 3):
        zonas[z] = (sum(1 for b_ in brad if b_[4] == z), sum(b_[2] for b_ in brad if b_[4] == z))
    R["zonas"] = zonas
    # variantes probables del nombre de una fuente
    grupos = defaultdict(set)
    for s in fuentes:
        clave = re.sub(r"\s*\(.*?\)\s*", " ", s)
        clave = re.sub(r"[^A-Z0-9]", "", sin_tildes(clave).replace("&", "AND"))
        grupos[clave].add(s)
    R["variantes_fuente"] = [sorted(v) for v in grupos.values() if len(v) > 1]

    # Citas
    tc = [d["TC"] for d in docs]
    R["tc_medio"] = sum(tc) / n
    tcy = [d["TC"] / (anio_ref - d["PY"] + 1) for d in docs if d["PY"]]
    R["tcy_medio"] = sum(tcy) / len(tcy)
    R["edad_media"] = anio_ref - sum(anios) / len(anios)
    media_anio = defaultdict(list)
    for d in docs:
        media_anio[d["PY"]].append(d["TC"])
    citados = []
    for d in docs:
        m = sum(media_anio[d["PY"]]) / len(media_anio[d["PY"]])
        tpy = d["TC"] / (anio_ref - d["PY"] + 1) if d["PY"] else 0
        citados.append((d, d["TC"], tpy, d["TC"] / m if m else 0))
    citados.sort(key=lambda t: -t[1])
    R["citados"] = citados

    # Palabras clave
    de, idk = Counter(), Counter()
    for d in docs:
        for k in d["DE"]:
            k2 = kw_norm(k)
            if k2:
                de[k2] += 1
        for k in d["ID"]:
            k2 = kw_norm(k)
            if k2:
                idk[k2] += 1
    R["de"], R["id"] = de, idk
    pares = Counter()
    kws_doc = []
    for d in docs:
        s = sorted(set(kw_norm(k) for k in d["DE"] if kw_norm(k)))
        kws_doc.append(s)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                pares[(s[i], s[j])] += 1
    R["pares"] = pares
    R["kws_doc"] = kws_doc
    R["docs_con_de"] = sum(1 for s in kws_doc if s)

    # Referencias citadas (por base, sin cruzar formatos)
    refs = defaultdict(Counter)
    for d in docs:
        for c in d["CR"]:
            refs[d["DB"]][_limpia_espacios(c).upper()] += 1
    R["refs"] = {b_: (sum(c.values()), len(c)) for b_, c in refs.items()}

    # Paises
    pais_doc, origen = Counter(), Counter()
    scp, mcp = Counter(), Counter()
    prod_pais = Counter()
    con_paises = 0
    multi = 0
    for d in docs:
        set_p = set(p for p in (pais_de(c) for c in d["C1"]) if p)
        pc = pais_correspondencia(d)
        fuente = "RP"
        if not pc:
            fuente = "C1"
            pc = pais_de(d["C1"][0]) if d["C1"] else None
            if not pc:
                firsts = [pais_de(c) for c in d["C1"]]
                firsts = [p for p in firsts if p]
                pc = firsts[0] if firsts else None
        d["PAIS"] = pc
        d["PAIS_ORIGEN"] = fuente if pc else ""
        if pc:
            set_p.add(pc)
        d["PAISES"] = sorted(set_p)
        if set_p:
            con_paises += 1
            if len(set_p) > 1:
                multi += 1
        for p in set_p:
            prod_pais[p] += 1
        if pc:
            pais_doc[pc] += 1
            origen[fuente] += 1
            if len(set_p) > 1:
                mcp[pc] += 1
            else:
                scp[pc] += 1
    R["pais_doc"], R["scp"], R["mcp"] = pais_doc, scp, mcp
    R["origen_pais"] = origen
    R["prod_pais"] = prod_pais
    R["intl"] = multi / n * 100 if n else 0
    R["docs_con_pais"] = con_paises
    R["tipos"] = Counter(d["DT"].lower() for d in docs)
    R["n"] = n
    R["anios"] = (a0, a1)
    return R


# --------------------------------------------------------------------------
# Salidas
# --------------------------------------------------------------------------
def fnum(x, dec=2):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "NA"
    if isinstance(x, int):
        return str(x)
    return ("{:." + str(dec) + "f}").format(x)


def escribir_csv(ruta, cab, filas):
    with open(ruta, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(cab)
        for fila in filas:
            w.writerow(fila)


def ref_corta(d):
    a = d["AUN"][0] if d["AUN"] else "SIN AUTOR"
    return "{}, {}, {}".format(a, d["PY"], fuente_norm(d["SO"]))


def info_principal(R, docs, por_base):
    filas = [
        ("Periodo", "{}-{}".format(*R["anios"])),
        ("Fuentes (revistas, libros, etc.)", len(R["fuentes"])),
        ("Documentos", R["n"]),
        ("Tasa de crecimiento anual compuesta (%)", fnum(R["cagr"])),
        ("Edad media de los documentos (años)", fnum(R["edad_media"])),
        ("Citas medias por documento", fnum(R["tc_medio"], 3)),
        ("Citas medias por año por documento", fnum(R["tcy_medio"], 3)),
        ("Palabras clave de autor (DE, distintas)", len(R["de"])),
        ("Keywords Plus / indexadas (ID, distintas)", len(R["id"])),
        ("Autores", R["n_autores"]),
        ("Apariciones de autores", R["apariciones"]),
        ("Autores de documentos de un solo autor", R["autores_un_autor"]),
        ("Documentos de un solo autor", R["docs_un_autor"]),
        ("Coautores por documento", fnum(R["coautores_doc"])),
        ("Coautoría internacional (%)", fnum(R["intl"])),
    ]
    for b_, (tot, uni) in sorted(R["refs"].items()):
        filas.append(("Referencias citadas {} (total / distintas)".format(b_), "{} / {}".format(tot, uni)))
    for t, k in orden_desc(R["tipos"]):
        filas.append(("Tipo de documento: " + (t or "sin dato"), k))
    return filas


def tabla_md(cab, filas):
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for f in filas:
        out.append("| " + " | ".join(str(c).replace("|", "/") for c in f) + " |")
    return out


def figuras(R, out, top):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return []
    hechas = []
    gris, azul = "#444444", "#2b5c8a"

    def guardar(fig, nombre):
        fig.tight_layout()
        fig.savefig(os.path.join(out, nombre), dpi=200)
        plt.close(fig)
        hechas.append(nombre)

    xs = [y for y, _ in R["serie"]]
    ys = [k for _, k in R["serie"]]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(xs, ys, marker="o", color=azul)
    if R["incompleto"]:
        ax.plot(xs[-1], ys[-1], marker="o", mfc="white", color=azul)
        ax.annotate("año incompleto", (xs[-1], ys[-1]), textcoords="offset points",
                    xytext=(0, -16), ha="center", fontsize=8, color=gris)
    ax.set_xlabel("Año")
    ax.set_ylabel("Documentos")
    ax.set_xticks(xs)
    ax.tick_params(axis="x", rotation=45)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    guardar(fig, "fig_produccion_anual.png")

    fig, ax = plt.subplots(figsize=(7, 4))
    rk = [b_[0] for b_ in R["bradford"]]
    ac = [b_[3] for b_ in R["bradford"]]
    ax.plot(rk, ac, color=azul)
    ax.set_xscale("log")
    lim1 = max([b_[0] for b_ in R["bradford"] if b_[4] == 1] or [1])
    lim2 = max([b_[0] for b_ in R["bradford"] if b_[4] <= 2] or [1])
    ax.axvspan(1, lim1, color=azul, alpha=0.12, label="Zona 1 (núcleo)")
    ax.axvspan(lim1, lim2, color=azul, alpha=0.05, label="Zona 2")
    ax.set_xlabel("Rango de la fuente (escala log)")
    ax.set_ylabel("Documentos acumulados")
    ax.legend(frameon=False, fontsize=8)
    guardar(fig, "fig_bradford.png")

    L = R["lotka"]
    fig, ax = plt.subplots(figsize=(6, 4))
    kx = [k for k, _, _ in L["dist"]]
    obs = [p * 100 for _, _, p in L["dist"]]
    fit = [L["C"] * k ** (-L["beta"]) * 100 for k in kx]
    ax.plot(kx, obs, marker="o", color=azul, label="Observado")
    ax.plot(kx, fit, linestyle="--", color=gris,
            label="Ajuste (beta = {:.2f}, R2 = {:.3f})".format(L["beta"], L["R2"]))
    ax.set_xlabel("Documentos por autor")
    ax.set_ylabel("% de autores")
    ax.legend(frameon=False, fontsize=8)
    guardar(fig, "fig_lotka.png")

    for nombre, cont, xl in (("fig_fuentes.png", R["fuentes"], "Documentos"),
                             ("fig_palabras_clave.png", R["de"], "Frecuencia")):
        it = orden_desc(cont)[:top][::-1]
        if not it:
            continue
        fig, ax = plt.subplots(figsize=(7, 0.35 * len(it) + 1))
        ax.barh([s[:55] for s, _ in it], [k for _, k in it], color=azul)
        ax.set_xlabel(xl)
        ax.tick_params(axis="y", labelsize=7)
        guardar(fig, nombre)
    return hechas


def informe(args, solo_fusion=False):
    regs, por_base, problemas = cargar(args.archivos)
    for p in problemas:
        print("FORMATO NO RECONOCIDO (se omite): " + p, file=sys.stderr)
    if not regs:
        print("No hay registros legibles.", file=sys.stderr)
        return 2
    out = args.out
    os.makedirs(out, exist_ok=True)
    docs, qd, qt, posibles = fusionar(regs, args.prioridad, args.quitar_doi_distinto, args.modo)
    identificados = len(regs)
    eliminados = len(qd) + len(qt) + (len(posibles) if args.quitar_doi_distinto else 0)
    pr = [("Registros " + b_, k) for b_, k in por_base.items()]
    pr += [("Registros identificados", identificados),
           ("Duplicados por DOI", len(qd)),
           ("Duplicados por título y año (sin DOI en uno)", len(qt)),
           ("Posibles duplicados con DOI distinto", len(posibles)),
           ("  retirados" if args.quitar_doi_distinto else "  conservados (decidir a mano)", len(posibles)),
           ("Duplicados eliminados (total)", eliminados),
           ("Registros tras la fusión", len(docs))]
    escribir_csv(os.path.join(out, "prisma_conteos.csv"), ["concepto", "n"], pr)
    escribir_csv(os.path.join(out, "posibles_duplicados.csv"),
                 ["titulo", "anio", "base_A", "doi_A", "base_B", "doi_B", "decision"],
                 [(a["TI"], a["PY"], a["DB"], a["DI"], b_["DB"], b_["DI"],
                   "retirado" if args.quitar_doi_distinto else "PENDIENTE")
                  for a, b_ in posibles])
    escribir_csv(os.path.join(out, "duplicados_retirados.csv"),
                 ["motivo", "titulo", "anio", "base_retirado", "doi_retirado", "base_conservado", "doi_conservado"],
                 [("DOI", a["TI"], a["PY"], a["DB"], a["DI"], b_["DB"], b_["DI"]) for a, b_ in qd]
                 + [("titulo+anio", a["TI"], a["PY"], a["DB"], a["DI"], b_["DB"], b_["DI"]) for a, b_ in qt])
    print("Identificados {} | duplicados DOI {} | titulo {} | posibles DOI distinto {} | quedan {}".format(
        identificados, len(qd), len(qt), len(posibles), len(docs)))
    if solo_fusion:
        guardar_corpus(docs, out)
        return 0

    anio_ref = args.anio_ref or datetime.date.today().year
    R = analizar(docs, anio_ref, args.top)
    guardar_corpus(docs, out)
    top = args.top
    ip = info_principal(R, docs, por_base)
    escribir_csv(os.path.join(out, "informacion_principal.csv"), ["descripcion", "resultado"], ip)
    acum = 0
    filas_pa = []
    for y, k in R["serie"]:
        acum += k
        filas_pa.append((y, k, fnum(k / R["n"] * 100), acum))
    escribir_csv(os.path.join(out, "produccion_anual.csv"), ["anio", "documentos", "porcentaje", "acumulado"], filas_pa)
    escribir_csv(os.path.join(out, "fuentes_bradford.csv"), ["rango", "fuente", "documentos", "acumulado", "zona"], R["bradford"])
    fr = sorted(R["autores_frac"].items(), key=lambda kv: (-kv[1], kv[0]))
    escribir_csv(os.path.join(out, "autores.csv"), ["autor", "documentos", "documentos_fraccionados"],
                 [(a, k, fnum(R["autores_frac"][a], 3)) for a, k in orden_desc(R["autores"])])
    L = R["lotka"]
    escribir_csv(os.path.join(out, "lotka.csv"), ["documentos_escritos", "n_autores", "proporcion", "proporcion_ajustada"],
                 [(k, v, fnum(p, 4), fnum(L["C"] * k ** (-L["beta"]), 4)) for k, v, p in L["dist"]])
    escribir_csv(os.path.join(out, "paises_autor_correspondencia.csv"), ["pais", "documentos", "frecuencia", "SCP", "MCP", "MCP_ratio"],
                 [(p, k, fnum(k / sum(R["pais_doc"].values()), 4), R["scp"][p], R["mcp"][p], fnum(R["mcp"][p] / k, 4))
                  for p, k in orden_desc(R["pais_doc"])])
    escribir_csv(os.path.join(out, "produccion_paises.csv"), ["pais", "documentos_con_al_menos_un_autor"], orden_desc(R["prod_pais"]))
    escribir_csv(os.path.join(out, "mas_citados.csv"), ["documento", "titulo", "doi", "TC", "TC_por_anio", "TC_normalizado"],
                 [(ref_corta(d), d["TI"], d["DI"], tc, fnum(tpy), fnum(ntc)) for d, tc, tpy, ntc in R["citados"]])
    escribir_csv(os.path.join(out, "palabras_clave_autor.csv"), ["palabra_clave", "frecuencia"], orden_desc(R["de"]))
    escribir_csv(os.path.join(out, "keywords_plus.csv"), ["palabra_clave", "frecuencia"], orden_desc(R["id"]))
    pares = sorted(R["pares"].items(), key=lambda kv: (-kv[1], kv[0]))
    escribir_csv(os.path.join(out, "coocurrencia_pares.csv"), ["palabra_1", "palabra_2", "coocurrencias"],
                 [(a, b_, k) for (a, b_), k in pares])
    top50 = [k for k, _ in orden_desc(R["de"])[:50]]
    matriz = []
    for a in top50:
        fila = [a]
        for b_ in top50:
            fila.append(R["de"][a] if a == b_ else R["pares"].get(tuple(sorted((a, b_))), 0))
        matriz.append(fila)
    escribir_csv(os.path.join(out, "coocurrencia_matriz.csv"), [""] + top50, matriz)
    sel = [k for k, v in orden_desc(R["de"]) if v >= args.min_kw]
    ids = {k: i + 1 for i, k in enumerate(sel)}
    with open(os.path.join(out, "vosviewer_map.txt"), "w", encoding="utf-8") as f:
        f.write("id\tlabel\tweight<Occurrences>\n")
        for k in sel:
            f.write("{}\t{}\t{}\n".format(ids[k], k.lower(), R["de"][k]))
    with open(os.path.join(out, "vosviewer_network.txt"), "w", encoding="utf-8") as f:
        for (a, b_), k in pares:
            if a in ids and b_ in ids:
                f.write("{}\t{}\t{}\n".format(ids[a], ids[b_], k))

    figs = figuras(R, out, top) if not args.sin_figuras else []
    md = resumen_md(R, pr, ip, posibles, por_base, anio_ref, args, figs, len(qd) + len(qt))
    with open(os.path.join(out, "resumen_bibliometrico.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    print("Salidas en " + os.path.abspath(out) + (" (sin matplotlib: sin figuras)" if not figs and not args.sin_figuras else ""))
    return 0


def guardar_corpus(docs, out):
    escribir_csv(os.path.join(out, "corpus_fusionado.csv"),
                 ["base", "autores", "titulo", "anio", "fuente", "doi", "citas", "tipo",
                  "palabras_clave_autor", "pais_correspondencia", "origen_pais", "paises", "archivo"],
                 [(d["DB"], "; ".join(d.get("AUN", d["AU"])), d["TI"], d["PY"], d["SO"], d["DI"], d["TC"],
                   d["DT"], "; ".join(d["DE"]), d.get("PAIS") or "", d.get("PAIS_ORIGEN", ""),
                   "; ".join(d.get("PAISES", [])), d.get("ARCHIVO", "")) for d in docs])


def resumen_md(R, pr, ip, posibles, por_base, anio_ref, args, figs, n_dup):
    top = args.top
    t = [args.tabla_inicial]
    fgn = [args.figura_inicial]
    md = []

    def tabla(titulo, cab, filas, nota):
        md.append("[TABLA {}] {}".format(t[0], titulo))
        md.extend(tabla_md(cab, filas))
        md.append("[NOTA] " + nota)
        md.append("")
        t[0] += 1

    def figura(titulo, archivo, nota=None):
        if archivo in figs:
            md.append("[FIGURA {}] {} | {}".format(fgn[0], titulo, archivo))
            if nota:
                md.append("[NOTA] " + nota)
            md.append("")
            fgn[0] += 1

    metodo = ("Calculado con bibliometria.py, script propio de la Ruta del Artículo de Revisión "
              "(Python), no con bibliometrix.")
    md.append("# Resumen bibliométrico (bibliometria.py)")
    md.append("")
    md.append("[SIN SANGRIA] Generado el {} con año de referencia {}. {} Las cifras se trasladan "
              "a la Fase 5 sin recalcular ni redondear distinto. Renumerar tablas y figuras según "
              "el manuscrito.".format(datetime.date.today().isoformat(), anio_ref, metodo))
    md.append("")
    md.append("## Cifras clave")
    md.append("")
    bases = "; ".join("{} = {}".format(b_, k) for b_, k in por_base.items())
    md.append("- Registros identificados: {} ({}). Duplicados eliminados: {}. Documentos analizados: {}.".format(
        sum(por_base.values()), bases, n_dup + (len(posibles) if args.quitar_doi_distinto else 0), R["n"]))
    if posibles:
        md.append("- [POR CONFIRMAR: {} posibles duplicados con DOI distinto (mismo título y año) en "
                  "posibles_duplicados.csv; {}.]".format(
                      len(posibles), "ya retirados" if args.quitar_doi_distinto else "siguen en el corpus hasta que el investigador decida"))
    md.append("- Periodo {}-{}; tasa de crecimiento anual compuesta {} %.".format(R["anios"][0], R["anios"][1], fnum(R["cagr"])))
    if R["incompleto"]:
        md.append("- [POR CONFIRMAR: el año {} está incompleto (año de referencia {}); sin ese año la tasa es {} %. "
                  "Decidir cuál se reporta.]".format(R["anios"][1], anio_ref, fnum(R["cagr_sin_ultimo"])))
    md.append("- {} fuentes; núcleo de Bradford (zona 1): {} fuentes con {} documentos.".format(
        len(R["fuentes"]), R["zonas"][1][0], R["zonas"][1][1]))
    L = R["lotka"]
    md.append("- {} autores; ley de Lotka: beta = {}, C = {}, R² = {}.".format(
        R["n_autores"], fnum(L["beta"], 4), fnum(L["C"], 4), fnum(L["R2"], 4)))
    md.append("- Citas medias por documento {}; coautoría internacional {} %.".format(fnum(R["tc_medio"], 3), fnum(R["intl"])))
    if R["origen_pais"].get("C1"):
        md.append("- País del documento: autor de correspondencia en {} documentos; primera afiliación en {} "
                  "(sin dirección de correspondencia); sin país identificable: {}.".format(
                      R["origen_pais"].get("RP", 0), R["origen_pais"]["C1"], R["n"] - sum(R["origen_pais"].values())))
    if R["docs_sin_autor"]:
        md.append("- {} documento(s) sin autor (marcador \"No authorship indicated\"), excluidos del conteo de autores.".format(R["docs_sin_autor"]))
    if R["variantes_fuente"]:
        md.append("- [POR CONFIRMAR: posibles variantes del mismo título de fuente, sin unificar: " +
                  "; ".join(" = ".join(v) for v in R["variantes_fuente"][:8]) + "]")
    md.append("")
    md.append("## Tablas y figuras")
    md.append("")

    filas = [(d, v) for d, v in ip if not d.startswith("Referencias")]
    tabla("Información principal del corpus", ["Descripción", "Resultado"], filas,
          "Corpus fusionado de {} tras eliminar duplicados. {}".format(bases, metodo))

    acum = 0
    filas = []
    for y, k in R["serie"]:
        acum += k
        filas.append((y, k, fnum(k / R["n"] * 100), acum))
    nota = "Tasa de crecimiento anual compuesta = {} %.".format(fnum(R["cagr"]))
    if R["incompleto"]:
        nota += " El año {} está incompleto a la fecha de la búsqueda (sin él, {} %).".format(R["anios"][1], fnum(R["cagr_sin_ultimo"]))
    tabla("Producción científica anual", ["Año", "Documentos", "%", "Acumulado"], filas, nota)
    figura("Producción científica anual", "fig_produccion_anual.png")

    filas = [(r_, s, k, z) for r_, s, k, _, z in R["bradford"][:top]]
    tabla("Fuentes más relevantes", ["Rango", "Fuente", "Documentos", "Zona de Bradford"], filas,
          "Ordenadas por número de documentos; empates en orden alfabético.")
    figura("Fuentes más relevantes", "fig_fuentes.png")
    filas = [("Zona {}{}".format(z, " (núcleo)" if z == 1 else ""), nf, nd, fnum(nd / R["n"] * 100))
             for z, (nf, nd) in R["zonas"].items()]
    tabla("Zonas de Bradford", ["Zona", "Fuentes", "Documentos", "% de documentos"], filas,
          "Zonas por tercios del acumulado de documentos (Bradford, 1934).")
    figura("Distribución de fuentes según la ley de Bradford", "fig_bradford.png")

    oa = orden_desc(R["autores"])[:top]
    of = sorted(R["autores_frac"].items(), key=lambda kv: (-kv[1], kv[0]))[:top]
    filas = [(a, k, af, fnum(kf)) for (a, k), (af, kf) in zip(oa, of)]
    tabla("Autores más productivos", ["Autor", "Documentos", "Autor (fraccionado)", "Documentos fraccionados"], filas,
          "Conteo completo y fraccionado (1/n autores por documento). Nombres normalizados a apellido e iniciales.")
    filas = [(k, v, fnum(p, 4), fnum(L["C"] * k ** (-L["beta"]), 4)) for k, v, p in L["dist"]]
    tabla("Productividad de autores según la ley de Lotka", ["Documentos por autor", "Autores", "Proporción observada", "Proporción ajustada"],
          filas, "Ajuste por mínimos cuadrados en escala log-log (Lotka, 1926): beta = {}, C = {}, R² = {}.".format(
              fnum(L["beta"], 4), fnum(L["C"], 4), fnum(L["R2"], 4)))
    figura("Ley de Lotka: distribución observada y ajustada", "fig_lotka.png")

    totp = sum(R["pais_doc"].values())
    filas = [(p, k, fnum(k / totp * 100), R["scp"][p], R["mcp"][p], fnum(R["mcp"][p] / k, 3))
             for p, k in orden_desc(R["pais_doc"])[:top]]
    tabla("Países más productivos según el autor de correspondencia", ["País", "Documentos", "%", "SCP", "MCP", "MCP ratio"], filas,
          "SCP = publicaciones de un solo país; MCP = publicaciones con autores de varios países. "
          "Coautoría internacional del corpus: {} %.".format(fnum(R["intl"])))

    filas = [(ref_corta(d), d["DI"] or "s. d.", tc, fnum(tpy)) for d, tc, tpy, _ in R["citados"][:top]]
    tabla("Documentos más citados", ["Documento", "DOI", "Citas totales", "Citas por año"], filas,
          "Citas según la base de la que procede el registro, a la fecha de exportación; citas por año = citas / ({} − año + 1).".format(anio_ref))

    pares = sorted(R["pares"].items(), key=lambda kv: (-kv[1], kv[0]))[:top]
    filas = [(k, v) for k, v in orden_desc(R["de"])[:top]]
    tabla("Palabras clave de autor más frecuentes", ["Palabra clave", "Frecuencia"], filas,
          "{} palabras clave distintas en {} documentos con palabras clave de autor.".format(len(R["de"]), R["docs_con_de"]))
    figura("Palabras clave de autor más frecuentes", "fig_palabras_clave.png")
    tabla("Pares de palabras clave con mayor co-ocurrencia", ["Palabra clave 1", "Palabra clave 2", "Documentos"],
          [(a, b_, k) for (a, b_), k in pares],
          "Red completa en coocurrencia_pares.csv; vosviewer_map.txt y vosviewer_network.txt (frecuencia ≥ {}) se abren en VOSviewer.".format(args.min_kw))
    return md


def main(argv=None):
    ap = argparse.ArgumentParser(description="Analisis bibliometrico sin R (Scopus CSV + WoS texto plano).")
    sub = ap.add_subparsers(dest="cmd")
    for nombre in ("informe", "fusionar"):
        p = sub.add_parser(nombre)
        p.add_argument("archivos", nargs="+")
        p.add_argument("--out", default="bibliometria_salida")
        p.add_argument("--anio-ref", type=int, default=None)
        p.add_argument("--top", type=int, default=10)
        p.add_argument("--prioridad", choices=["wos", "scopus"], default="wos")
        p.add_argument("--quitar-doi-distinto", action="store_true")
        p.add_argument("--tabla-inicial", type=int, default=1)
        p.add_argument("--figura-inicial", type=int, default=1)
        p.add_argument("--min-kw", type=int, default=5)
        p.add_argument("--sin-figuras", action="store_true")
        p.add_argument("--modo", choices=["ruta", "bibliometrix"], default="ruta",
                       help="bibliometrix: replica mergeDbSources (solo para validar)")
    args = ap.parse_args(argv)
    if not args.cmd:
        ap.print_help()
        return 1
    return informe(args, solo_fusion=(args.cmd == "fusionar"))


if __name__ == "__main__":
    sys.exit(main())
