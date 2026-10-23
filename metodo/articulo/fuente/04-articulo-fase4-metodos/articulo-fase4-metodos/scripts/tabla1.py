#!/usr/bin/env python3
"""
Tabla 1 sociodemografica calculada desde la base de datos real
(Ruta del Articulo Cientifico, Fase 4 - Acosta | IA & Research).

Requisitos: Python 3 con pandas y openpyxl  ->  pip install pandas openpyxl
Si el servidor Acosta (trabajar_en_r) esta conectado, la via preferente es R:
frecuencias() y descriptivos() (ver references/analisis.md). Este script es la
via local, con las mismas reglas.

Uso
---
  1) Ver que columnas hay (SIEMPRE primero):
       python3 tabla1.py base.xlsx --listar
  2) Calcular la tabla y dejarla lista para el motor del Word:
       python3 tabla1.py base.xlsx --cat "Sexo, Ciclo, Facultad" --num Edad \
           --orden-natural --perdidos "99,NA,No sabe" --md tabla1.md

Opciones
--------
  --hoja NOMBRE      hoja del .xlsx (por defecto, la primera)
  --cat A,B          columnas categoricas -> n y % sobre casos validos
  --num X,Y          columnas numericas   -> n, M, DE, Mdn, RIC, min, max
  --perdidos "..."   codigos que cuentan como perdido (p. ej. "99,NA,No sabe");
                     las celdas vacias siempre son perdido
  --orden-natural    ordena categorias por su numero, romano u ordinal
                     (Ciclo I < II < X; 1er < 2do; primero < segundo);
                     sin esta opcion, por frecuencia descendente
  --sin-normalizar   no unifica categorias (por defecto se unifican las que
                     solo difieren en espacios o mayusculas/minusculas)
  --unir-tildes      ademas unifica las que solo difieren en tildes
  --etiquetas "..."  libro de codigos: "Sexo:1=Mujer,2=Hombre;Edad:1=18-20,2=21-23"
                     (columnas separadas por ;, codigos por ,). Sin etiqueta,
                     un codigo numerico sale como [POR CONFIRMAR] en la tabla
  --mediana X,Y      en el .md, esas numericas se reportan como Mdn (RIC)
  --md salida.md     escribe [TABLA n] + tabla + [NOTA] en la sintaxis de
                     articulo_docx.py, para pegar en la seccion de Metodos
  --numero N         numero de la tabla (por defecto 1)
  --titulo "..."     titulo de la tabla

Decimales (fijos y declarados en la nota): % con 1 decimal; M, DE, Mdn y RIC
con 2. El porcentaje es SOBRE CASOS VALIDOS; los perdidos van en la nota.
Toda unificacion de categorias se imprime y se declara en la nota.
"""

import argparse
import csv
import difflib
import io
import re
import sys
import unicodedata
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("Falta pandas. Instalar con: pip install pandas openpyxl")


# ---------------------------------------------------------------- lectura

def _leer_csv(p: Path) -> pd.DataFrame:
    crudo = p.read_bytes()
    texto, cod = None, None
    for c in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            texto, cod = crudo.decode(c), c
            break
        except UnicodeDecodeError:
            continue
    try:
        sep = csv.Sniffer().sniff(texto[:20000], delimiters=",;\t|").delimiter
    except csv.Error:
        sep = ","
    df = pd.read_csv(io.StringIO(texto), sep=sep, dtype=str, keep_default_na=False)
    if cod != "utf-8-sig":
        print(f"(CSV leido con codificacion {cod})", file=sys.stderr)
    return df


def cargar(ruta: str, hoja=None) -> pd.DataFrame:
    p = Path(ruta)
    if not p.exists():
        sys.exit(f"No existe el archivo: {ruta}")
    suf = p.suffix.lower()
    if suf in (".xlsx", ".xlsm", ".xls"):
        try:
            xl = pd.ExcelFile(p)
        except ImportError:
            sys.exit("Falta openpyxl para leer Excel. Instalar con: pip install openpyxl")
        if hoja and hoja not in xl.sheet_names:
            sys.exit(f"La hoja '{hoja}' no existe. Hojas disponibles: {', '.join(xl.sheet_names)}")
        return xl.parse(hoja if hoja else 0, dtype=str, keep_default_na=False)
    if suf in (".csv", ".txt"):
        return _leer_csv(p)
    sys.exit(f"Extension no soportada: {suf} (usar .xlsx, .xls, .csv o .txt)")


def _texto(v) -> str:
    """Celda -> texto limpio (99.0 -> '99')."""
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return ""
    s = re.sub(r"\s+", " ", str(v)).strip()
    if re.fullmatch(r"-?\d+\.0+", s):
        s = s.split(".")[0]
    return s


def marcar_perdidos(s: pd.Series, codigos) -> pd.Series:
    cod = {c.lower() for c in codigos}
    t = s.map(_texto)
    return t.where(~((t == "") | t.str.lower().isin(cod)), None)


# ---------------------------------------------------------------- categorias

def _sin_tildes(s: str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFD", s) if unicodedata.category(ch) != "Mn")


def normalizar(s: pd.Series, tildes: bool):
    """Unifica variantes; la etiqueta final es la variante mas frecuente."""
    validos = s.dropna()
    clave = validos.str.lower()
    if tildes:
        clave = clave.map(_sin_tildes)
    uniones, mapa = [], {}
    for k, grupo in validos.groupby(clave):
        variantes = grupo.value_counts()
        # preferir la forma con tildes y con mayuscula inicial (no TODO MAYUS
        # ni todo minus); a igualdad, la mas frecuente
        etiqueta = max(variantes.index, key=lambda v: (
            v != _sin_tildes(v), v[:1].isupper() and not v.isupper(), variantes[v]))
        for v in variantes.index:
            mapa[v] = etiqueta
        if len(variantes) > 1:
            uniones.append((etiqueta, list(variantes.index)))
    return s.map(lambda v: mapa.get(v, v) if v is not None else None), uniones


ORDINALES = {
    "primer": 1, "primero": 1, "primera": 1, "segundo": 2, "segunda": 2,
    "tercer": 3, "tercero": 3, "tercera": 3, "cuarto": 4, "cuarta": 4,
    "quinto": 5, "quinta": 5, "sexto": 6, "sexta": 6, "septimo": 7, "septima": 7,
    "setimo": 7, "octavo": 8, "octava": 8, "noveno": 9, "novena": 9,
    "decimo": 10, "decima": 10, "undecimo": 11, "duodecimo": 12,
}
ROMANOS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}


def _romano(tok: str):
    if not tok or not re.fullmatch(r"[IVXLC]+", tok):
        return None
    total, prev = 0, 0
    for ch in reversed(tok):
        v = ROMANOS[ch]
        total = total - v if v < prev else total + v
        prev = max(prev, v)
    # solo romanos bien formados (evita 'IIII', 'VX'...)
    a_rom = []
    n = total
    for val, sim in ((100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                     (5, "V"), (4, "IV"), (1, "I")):
        while n >= val:
            a_rom.append(sim)
            n -= val
    return total if "".join(a_rom) == tok else None


def clave_natural(etiqueta: str):
    base = _sin_tildes(etiqueta).lower()
    for tok in re.findall(r"[a-z]+", base):
        if tok in ORDINALES:
            return (0, ORDINALES[tok], base)
    m = re.search(r"\d+(?:[.,]\d+)?", base)
    if m:
        return (0, float(m.group().replace(",", ".")), base)
    for tok in re.findall(r"[A-Za-z]+", etiqueta):
        if tok.isupper() or etiqueta.strip().upper() == tok:
            r = _romano(tok.upper())
            if r:
                return (0, r, base)
    return (1, 0, base)


def tabla_categorica(s: pd.Series, orden_natural: bool):
    validos = s.dropna()
    conteo = validos.value_counts()
    if orden_natural:
        etiquetas = sorted(conteo.index, key=clave_natural)
    else:
        etiquetas = sorted(conteo.index, key=lambda e: (-conteo[e], e.lower()))
    nv = len(validos)
    filas = [(e, int(conteo[e]), 100.0 * conteo[e] / nv) for e in etiquetas]
    sin_clave = orden_natural and all(clave_natural(e)[0] == 1 for e in etiquetas)
    empates = []
    if orden_natural:
        por_clave = {}
        for e in etiquetas:
            k = clave_natural(e)
            if k[0] == 0:
                por_clave.setdefault(k[1], []).append(e)
        empates = [v for v in por_clave.values() if len(v) > 1]
    return filas, nv, sin_clave, empates


# ---------------------------------------------------------------- numericas

def resumen_numerico(s: pd.Series):
    t = s.dropna().str.replace(",", ".", regex=False)
    x = pd.to_numeric(t, errors="coerce")
    no_num = int(x.isna().sum())
    x = x.dropna()
    if x.empty:
        return None, no_num
    q1, q3 = x.quantile(0.25), x.quantile(0.75)
    return {"n": int(x.size), "m": x.mean(), "de": x.std(ddof=1), "mdn": x.median(),
            "q1": q1, "q3": q3, "ric": q3 - q1, "min": x.min(), "max": x.max(),
            "asim": x.skew() if x.size > 2 else 0.0}, no_num


def _f2(v):
    return f"{v:.2f}"


def _ext(v):
    return f"{v:.0f}" if float(v).is_integer() else f"{v:.2f}"


# ---------------------------------------------------------------- listado

def listar(df: pd.DataFrame, perdidos):
    print(f"Filas: {len(df)}   Columnas: {df.shape[1]}")
    print("| # | Columna | Validos | Perdidos | Unicos | Ejemplos |")
    print("|---|---|---|---|---|---|")
    for i, c in enumerate(df.columns, 1):
        s = marcar_perdidos(df[c], perdidos)
        v = s.dropna()
        ej = ", ".join(x[:18] for x in v.unique()[:3]).replace("|", "/")
        print(f"| {i} | {c} | {len(v)} | {s.isna().sum()} | {v.nunique()} | {ej} |")
    print("Revisar con el investigador: columnas sociodemograficas, codigos de "
          "perdido (99, NA...) y categorias escritas de varias formas.")


# ---------------------------------------------------------------- main

def _etiquetas(txt):
    """'Sexo:1=Mujer,2=Hombre;Edad:1=18-20' -> {'Sexo': {'1': 'Mujer', ...}}"""
    out = {}
    for bloque in (txt or "").split(";"):
        if ":" not in bloque:
            continue
        col, pares = bloque.split(":", 1)
        m = {}
        for par in pares.split(","):
            if "=" in par:
                k, v = par.split("=", 1)
                m[_texto(k)] = v.strip()
        out[re.sub(r"\s+", " ", col).strip()] = m
    return out


def _lista(txt):
    return [c.strip() for c in (txt or "").split(",") if c.strip()]


def main():
    ap = argparse.ArgumentParser(description="Tabla 1 sociodemografica desde la base real")
    ap.add_argument("base")
    ap.add_argument("--hoja")
    ap.add_argument("--cat", default="")
    ap.add_argument("--num", default="")
    ap.add_argument("--perdidos", default="")
    ap.add_argument("--orden-natural", action="store_true")
    ap.add_argument("--sin-normalizar", action="store_true")
    ap.add_argument("--unir-tildes", action="store_true")
    ap.add_argument("--mediana", default="")
    ap.add_argument("--etiquetas", default="")
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--md")
    ap.add_argument("--numero", type=int, default=1)
    ap.add_argument("--titulo", default="Características sociodemográficas de los participantes")
    a = ap.parse_args()

    df = cargar(a.base, a.hoja)
    df.columns = [re.sub(r"\s+", " ", str(c)).strip() for c in df.columns]
    perdidos = _lista(a.perdidos)
    libro = _etiquetas(a.etiquetas)

    cats, nums, medianas = _lista(a.cat), _lista(a.num), set(_lista(a.mediana))
    if a.listar or not (cats or nums):
        listar(df, perdidos)
        return

    faltan = [c for c in cats + nums if c not in df.columns]
    if faltan:
        for c in faltan:
            sug = difflib.get_close_matches(c, list(df.columns), n=2, cutoff=0.6)
            print(f"Columna inexistente: '{c}'" + (f" (¿quisiste decir {', '.join(sug)}?)" if sug else ""),
                  file=sys.stderr)
        sys.exit("No se inventan columnas. Correr con --listar y usar los nombres reales.")

    N = len(df)
    md = ["| Característica | n | % |", "|---|---|---|"]
    nota_perd, nota_union, avisos = [], [], []
    suma_no_100 = False

    for col in cats:
        s = marcar_perdidos(df[col], perdidos)
        mapa = libro.get(col, {})
        codigos = {v for v in s.dropna() if re.fullmatch(r"-?\d+", v)}
        sin_etiqueta = sorted(codigos - set(mapa), key=lambda x: int(x))
        if sin_etiqueta:
            avisos.append(f"{col}: codigos sin etiqueta ({', '.join(sin_etiqueta)}); pedir el libro de codigos "
                          "y correr con --etiquetas. No se adivinan.")
        s = s.map(lambda v: v if v is None else (mapa[v] if v in mapa else
                  (f"{v} [POR CONFIRMAR: etiqueta del código]" if v in codigos else v)))
        if not a.sin_normalizar:
            s, uniones = normalizar(s, a.unir_tildes)
            for etiqueta, variantes in uniones:
                nota_union.append(f"{col}: {' / '.join(variantes)} → {etiqueta}")
        filas, nv, sin_clave, empates = tabla_categorica(s, a.orden_natural)
        if sin_clave:
            avisos.append(f"{col}: sin numeros, romanos ni ordinales; quedo en orden alfabetico")
        for grupo in empates:
            avisos.append(f"{col}: {' / '.join(grupo)} tienen el mismo orden; "
                          "¿son la misma categoria? Preguntar; no se unen solas")
        md.append(f"| **{col}** |  |  |")
        for e, n, pct in filas:
            md.append(f"| {e.replace('|', '/')} | {n} | {pct:.1f} |")
        if round(sum(round(p, 1) for _, _, p in filas), 1) != 100.0:
            suma_no_100 = True
        if N - nv:
            nota_perd.append(f"{col} = {N - nv} (n válido = {nv})")

    for col in nums:
        s = marcar_perdidos(df[col], perdidos)
        r, no_num = resumen_numerico(s)
        np_ = int(s.isna().sum()) + no_num
        if r is None:
            avisos.append(f"{col}: sin valores numericos validos; no se calculo")
            continue
        if no_num:
            avisos.append(f"{col}: {no_num} celda(s) no numericas contadas como perdido; revisar en la base")
        if abs(r["asim"]) > 1 and col not in medianas:
            avisos.append(f"{col}: asimetria = {r['asim']:.2f}; considerar --mediana {col}")
        if col in medianas:
            md.append(f"| **{col}**, Mdn (RIC) | {_f2(r['mdn'])} ({_f2(r['ric'])}) |  |")
        else:
            md.append(f"| **{col}**, M (DE) | {_f2(r['m'])} ({_f2(r['de'])}) |  |")
        md.append(f"| Mín.–máx. | {_ext(r['min'])}–{_ext(r['max'])} |  |")
        if np_:
            nota_perd.append(f"{col} = {np_} (n válido = {N - np_})")

    partes = [f"N = {N}. Porcentajes calculados sobre los casos válidos de cada variable; "
              "porcentajes con un decimal y medidas de resumen con dos."]
    usa_md = any(c not in medianas for c in nums)
    abrev = []
    if usa_md:
        abrev.append("M = media; DE = desviación estándar")
    if medianas & set(nums):
        abrev.append("Mdn = mediana; RIC = rango intercuartílico")
    if abrev:
        partes.append("; ".join(abrev) + ".")
    if nota_perd:
        partes.append("Casos sin dato: " + "; ".join(nota_perd) + ".")
    if perdidos:
        partes.append("Se trataron como perdidos los códigos " + ", ".join(f"«{p}»" for p in perdidos) + ".")
    if nota_union:
        partes.append("Se unificaron categorías que solo diferían en escritura (" + "; ".join(nota_union) + ").")
    if suma_no_100:
        partes.append("Por redondeo, algunos porcentajes pueden no sumar 100.")
    nota = " ".join(partes)

    tabla_md = "\n".join(md)
    print(tabla_md)
    print(f"\nNOTA: {nota}")
    if nota_union:
        print("\nUNIFICACIONES (confirmar con el investigador):")
        for u in nota_union:
            print(f"  - {u}")
    for w in avisos:
        print(f"  ! {w}")

    if a.md:
        bloque = f"[TABLA {a.numero}] {a.titulo}\n{tabla_md}\n[NOTA] {nota}\n"
        Path(a.md).write_text(bloque, encoding="utf-8")
        print(f"\n.md listo para articulo_docx.py: {a.md} (el texto debe citar la Tabla {a.numero} antes)")


if __name__ == "__main__":
    main()
