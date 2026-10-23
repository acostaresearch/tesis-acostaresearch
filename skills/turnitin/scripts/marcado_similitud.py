"""Lo que el reporte de similitud de Turnitin (formato nuevo, con texto) resaltó, cruzado con el Word.

    python marcado_similitud.py <reporte.pdf> <documento.docx> [salida.json]

Por cada párrafo da cuántas palabras coinciden y qué oraciones cargan la coincidencia. El texto
coincidente va entre [corchetes]. No sirve para el reporte clásico, que trae las hojas como imagen.
"""
import sys

import pymupdf

from comun import cruzar_tramos

pdf, docx = sys.argv[1], sys.argv[2]
salida = sys.argv[3] if len(sys.argv) > 3 else "marcado_similitud.json"

# El resaltado de similitud son rectángulos pastel con opacidad 0,8; los tramos se cortan
# cuando aparece una palabra sin resaltar.
tramos = []
for pg in pymupdf.open(pdf):
    rects = [d["rect"] for d in pg.get_drawings()
             if d.get("fill") and 0.5 < (d.get("fill_opacity") or 1) < 1 and d["rect"].height < 40]
    if not rects:
        continue
    act = []
    for w in pg.get_text("words"):
        c = pymupdf.Point((w[0] + w[2]) / 2, (w[1] + w[3]) / 2)
        if any(r.contains(c) for r in rects):
            act.append(w[4])
        elif act:
            tramos.append(" ".join(act))
            act = []
    if act:
        tramos.append(" ".join(act))

cruzar_tramos(tramos, docx, salida)
