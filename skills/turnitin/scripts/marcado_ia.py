"""Lo que el reporte de IA de Turnitin resaltó, cruzado oración por oración con el Word.

    python marcado_ia.py <reporte.pdf> <documento.docx> [salida.json]

Imprime cada párrafo con al menos una oración marcada y guarda el detalle en JSON.
"""
import json
import sys

import pymupdf

from comun import norm, oraciones, parrafos

pdf, docx = sys.argv[1], sys.argv[2]
salida = sys.argv[3] if len(sys.argv) > 3 else "marcado.json"

marc, hojas = "", []
for n, pg in enumerate(pymupdf.open(pdf)):
    # El resaltado de IA son rectángulos rellenos y semitransparentes (opacidad 0,4).
    rects = [d["rect"] for d in pg.get_drawings() if d.get("fill") and (d.get("fill_opacity") or 1) < 1]
    if not rects:
        continue
    hit = [w[4] for w in pg.get_text("words")
           if any(r.contains(pymupdf.Point((w[0] + w[2]) / 2, (w[1] + w[3]) / 2)) for r in rects)]
    if hit:
        hojas.append(n + 1)
        marc += " " + " ".join(hit)
M = norm(marc)
if not M:
    sys.exit("El reporte no tiene nada resaltado. Por debajo de 20 % Turnitin muestra «*%» y no resalta: no hay nada que cruzar.")

res = []
for i, t in enumerate(parrafos(docx)):
    if len(t.split()) < 8:
        continue
    ors = []
    for o in oraciones(t):
        w = norm(o).split()
        v = [" ".join(w[k:k + 5]) for k in range(0, max(1, len(w) - 4), 3)]
        ors.append({"texto": o, "marcada": bool(w) and sum(x in M for x in v) / len(v) > 0.5})
    if any(o["marcada"] for o in ors):
        res.append({"parrafo": i, "entero": all(o["marcada"] for o in ors), "oraciones": ors})

json.dump(res, open(salida, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
tot = sum(len(o["texto"].split()) for r in res for o in r["oraciones"] if o["marcada"])
print(f"Hojas del reporte con resaltado: {hojas}")
print(f"Párrafos con algo marcado: {len(res)} · palabras marcadas: {tot} · detalle en {salida}\n")
if len(marc.split()) > 30 and tot < 0.5 * len(marc.split()):
    print(f"OJO: el reporte resalta {len(marc.split())} palabras y en el Word solo encontré {tot}. "
          "Puede que este Word no sea el que se analizó.\n")
for r in res:
    print(f"¶{r['parrafo']} · {'ENTERO' if r['entero'] else 'EN PARTE'}")
    for o in r["oraciones"]:
        print(f"   {'MARCADA' if o['marcada'] else '  ·    '} {o['texto'].strip()}")
    print()
