"""Estado de una carpeta de trabajo: qué Word hay, qué reportes hay y a qué Word corresponde cada uno.

    python estado.py 02-articulo
"""
import re
import sys
from datetime import datetime

import pymupdf

from comun import SALIDA, SUBIR, subir, carpeta, dato, docx_de, es_asesoria, mismo_nombre, norm, parecido, sitios, tipo_de_reporte

base = carpeta(sys.argv[1])
asesoria = es_asesoria(base)
nombres, actual, listo, rep = sitios(base)
fecha = lambda p: datetime.fromtimestamp(p.stat().st_mtime).strftime("%d-%b %H:%M")

print(f"CARPETA  {base}")
if asesoria:
    print("  organización de asesoría: se trabaja sin crear ni mover carpetas")
for nombre, d in dict(zip(nombres, (actual, listo, rep))).items():
    if d is None:
        print(f"  FALTA la subcarpeta «{nombre}»")

if asesoria:
    # El Word analizado y las salidas de la skill conviven en 03-turnitin: se distinguen por el sufijo.
    words = [(x, "03-turnitin, salida" if SALIDA.search(x.stem) else "03-turnitin") for x in docx_de(actual)]
else:
    words = ([(x, "actual") for x in docx_de(actual)] + [(x, "Listo") for x in docx_de(listo)]
             + [(x, SUBIR) for x in docx_de(subir(base))])
print("\nWORD")
for w, donde in words:
    print(f"  [{donde}] {w.name} · {fecha(w)}")
if not words:
    print("  ninguno")

print("\nREPORTES (del más viejo al más nuevo)")
pdfs = sorted(rep.rglob("*.pdf"), key=lambda p: p.stat().st_mtime) if rep else []
vistos = {}
for p in pdfs:
    t = "\n".join(pg.get_text() for pg in pymupdf.open(p))
    tipo = tipo_de_reporte(t)
    sitio = p.parent.name if asesoria or p.parent != rep else "(suelto)"
    if tipo is None:
        print(f"  [?] {p.name} · en {sitio} · no parece un reporte de Turnitin")
        continue
    ident = dato(t, "Identificador de la entrega")
    pct = re.search(r"(\*|\d+)\s*%\s*(?:detectado como IA|Similitud general|INDICE DE SIMILITUD)", t)
    analizado = dato(t, "Nombre del archivo")
    repetido = vistos.get((tipo, ident))
    vistos.setdefault((tipo, ident), p.name)
    tn = norm(t)
    punt = [(round(parecido(tn, w), 2), w.stat().st_mtime, w, donde) for w, donde in words]
    print(f"  [{tipo.upper()}] {p.name} · en {sitio} · {pct.group(1) + ' %' if pct else '% ?'} · entregado {dato(t, 'Fecha de entrega')}")
    print(f"        archivo analizado: {analizado}")
    if repetido:
        print(f"        REPETIDO: es la misma entrega que {repetido}")
    por_nombre = [(w, donde) for w, donde in words if mismo_nombre(analizado, w)]
    if punt and max(punt)[0] >= 0.5:
        s, _, w, donde = max(punt)
        print(f"        corresponde a: [{donde}] {w.name} (coincide {s:.0%} del texto)")
    elif por_nombre:
        print(f"        corresponde a: [{por_nombre[-1][1]}] {por_nombre[-1][0].name} (por el nombre del archivo)")
    elif words:
        print("        NO corresponde a ningún Word de la carpeta: es de otra versión")
    if not asesoria and sitio.lower() not in (tipo, "(suelto)"):
        print(f"        OJO: está en la carpeta «{sitio}» pero es un reporte de {tipo}")
if not pdfs:
    print("  ninguno")
