"""Quita los reportes que ya no mandan: de cada trabajo y tipo (IA, similitud) deja solo el más reciente.

    python limpiar.py 06-PAULA
    python limpiar.py 06-PAULA --ver     solo dice qué quitaría

Los reportes viejos van a la Papelera de reciclaje, de donde se pueden restaurar. No toca ningún Word
ni nada que no sea un reporte de Turnitin.
"""
import ctypes
import re
import sys
from ctypes import wintypes

import pymupdf

from comun import carpeta, dato, es_asesoria, norm, sub, tipo_de_reporte

base = carpeta(sys.argv[1])
ver = "--ver" in sys.argv
if es_asesoria(base):
    sys.exit(f"CARPETA  {base}\n  Tiene la organización de asesoría: sus reportes no se quitan.")
rep = sub(base, "reportes", "reporte")


def trabajo(analizado, pdf):
    """El trabajo al que pertenece el reporte: el nombre del Word sin « - humanizado 2» ni « - similitud»."""
    n = analizado if analizado != "?" else pdf.stem
    n = re.sub(r"\.docx?\b.*$", "", n, flags=re.I).replace("_", " ")
    # Puede traer dos sufijos: « - humanizado 2 - para Turnitin».
    return norm(re.sub(r"(\s*-\s*(humanizado|similitud|para turnitin)(\s*\d+)?)+\s*$", "", n, flags=re.I))


def a_la_papelera(p):
    class SHFILEOPSTRUCTW(ctypes.Structure):
        _fields_ = [("hwnd", wintypes.HWND), ("wFunc", wintypes.UINT), ("pFrom", wintypes.LPCWSTR),
                    ("pTo", wintypes.LPCWSTR), ("fFlags", ctypes.c_ushort),
                    ("fAnyOperationsAborted", wintypes.BOOL), ("hNameMappings", ctypes.c_void_p),
                    ("lpszProgressTitle", wintypes.LPCWSTR)]
    # FO_DELETE con FOF_ALLOWUNDO | FOF_NOCONFIRMATION | FOF_SILENT | FOF_NOERRORUI
    op = SHFILEOPSTRUCTW(None, 3, str(p) + "\0", None, 0x40 | 0x10 | 0x4 | 0x400, False, None, None)
    return ctypes.windll.shell32.SHFileOperationW(ctypes.byref(op)) == 0 and not p.exists()


print(f"CARPETA  {base}")
grupos = {}
for p in (sorted(rep.rglob("*.pdf"), key=lambda p: p.stat().st_mtime) if rep else []):
    t = "\n".join(pg.get_text() for pg in pymupdf.open(p))
    tipo = tipo_de_reporte(t)
    if tipo is None:
        continue
    pct = re.search(r"(\*|\d+)\s*%\s*(?:detectado como IA|Similitud general|INDICE DE SIMILITUD)", t)
    grupos.setdefault((trabajo(dato(t, "Nombre del archivo"), p), tipo), []).append(
        (p, pct.group(1) + " %" if pct else "% ?"))

# Turnitin recorta en la portada los nombres largos («ECTO_DE_TESIS_…» y «ROY_CHRISTIAN_…» son el
# mismo Word): dos claves del mismo tipo se funden cuando una termina con la otra.
fundidos = {}
for (nombre, tipo), lista in sorted(grupos.items(), key=lambda kv: -len(kv[0][0])):
    for (n2, t2) in list(fundidos):
        if t2 == tipo and len(nombre) >= 15 and (n2.endswith(nombre) or nombre.endswith(n2)):
            fundidos[(n2, t2)] = sorted(fundidos[(n2, t2)] + lista, key=lambda x: x[0].stat().st_mtime)
            break
    else:
        fundidos[(nombre, tipo)] = lista
grupos = fundidos

quitados = 0
for (nombre, tipo), lista in grupos.items():
    *viejos, (queda, pct_queda) = lista
    for p, pct in viejos:
        quitados += 1
        if ver:
            hecho = "quitaría"
        else:
            hecho = "quita  " if a_la_papelera(p) else "NO PUDO quitar"
        print(f"  {hecho}  [{tipo.upper()}] {p.relative_to(base)} · {pct}  →  manda {queda.name} · {pct_queda}")

if not quitados:
    print("  Nada obsoleto: cada trabajo tiene un solo reporte por tipo.")
elif ver:
    print("Nada se quitó: fue solo la vista previa.")
else:
    print("Listo. Lo quitado está en la Papelera de reciclaje.")
