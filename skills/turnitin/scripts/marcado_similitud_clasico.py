"""Lo que resaltó el reporte de similitud CLÁSICO de Turnitin, cruzado con el Word.

    python marcado_similitud_clasico.py <reporte.pdf> <documento.docx> [salida.json] [--por-hoja]

En el reporte clásico las hojas del documento son fotos y el texto coincidente va sobre un fondo
pastel. Se lee cada hoja con el OCR de Windows (español) y se toma por coincidente la palabra
cuyo fondo tiene color. Necesita los paquetes winrt (ver SKILL.md). La salida es la misma
que la de marcado_similitud.py.
"""
import asyncio
import sys

import numpy as np
import pymupdf
from winrt.windows.globalization import Language
from winrt.windows.graphics.imaging import BitmapDecoder
from winrt.windows.media.ocr import OcrEngine
from winrt.windows.storage.streams import DataWriter, InMemoryRandomAccessStream

from comun import cruzar_tramos

_pos = [a for a in sys.argv[1:] if not a.startswith("--")]
pdf, docx = _pos[0], _pos[1]
salida = _pos[2] if len(_pos) > 2 else "marcado_similitud.json"
ZOOM = 2.5

idiomas = [l.language_tag for l in OcrEngine.available_recognizer_languages]
esp = next((t for t in idiomas if t.startswith("es")), None)
if esp is None:
    sys.exit(f"Windows no tiene OCR en español instalado (hay: {idiomas}).")
motor = OcrEngine.try_create_from_language(Language(esp))


async def leer(png):
    flujo = InMemoryRandomAccessStream()
    w = DataWriter(flujo)
    w.write_bytes(png)
    await w.store_async()
    flujo.seek(0)
    bmp = await (await BitmapDecoder.create_async(flujo)).get_software_bitmap_async()
    res = await motor.recognize_async(bmp)
    return [(p.text, p.bounding_rect) for linea in res.lines for p in linea.words]


def clase(img, r):
    """'marca' si la palabra está sobre fondo pastel, 'ficha' si es el numerito de la fuente, o None."""
    x0, y0 = max(0, int(r.x)), max(0, int(r.y))
    z = img[y0:int(r.y + r.height) + 1, x0:int(r.x + r.width) + 1].astype(int)
    if z.size == 0:
        return None
    mx, mn = z.max(axis=2), z.min(axis=2)
    matiz = mx - mn
    if (matiz > 90).mean() > 0.5:          # recuadro de color vivo con el número en blanco
        return "ficha"
    papel = mn >= 150                      # el fondo, sin la tinta negra
    if papel.sum() and ((matiz > 18) & papel).sum() / papel.sum() > 0.5:
        return "marca"
    return None


async def main():
    """Devuelve los tramos resaltados y, por hoja, cuántas palabras hay, cuántas resaltadas y de qué fuente."""
    tramos, resumen = [], []
    doc = pymupdf.open(pdf)
    for n, pg in enumerate(doc, 1):
        if len(pg.get_text()) > 200 or not pg.get_images():
            continue                       # portada y lista de fuentes: traen texto, no foto
        pix = pg.get_pixmap(matrix=pymupdf.Matrix(ZOOM, ZOOM), alpha=False)
        img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)
        act, fuente, total, marc, por_fuente, inicio = [], "?", 0, 0, {}, ""
        for texto, r in await leer(pix.tobytes("png")):
            c = clase(img, r)
            if c == "ficha":
                fuente = texto if texto.isdigit() else "?"   # el numerito va justo antes de su tramo
                continue
            total += 1
            if total <= 8:
                inicio += texto + " "
            if c == "marca":
                act.append(texto)
                marc += 1
                por_fuente[fuente] = por_fuente.get(fuente, 0) + 1
            elif act:
                tramos.append(" ".join(act))
                act = []
        if act:
            tramos.append(" ".join(act))
        resumen.append((n, total, marc, por_fuente, inicio.strip()))
    return tramos, resumen


tramos, resumen = asyncio.run(main())
print(f"Hojas leídas con OCR: {len(resumen)}")
if "--por-hoja" in sys.argv:
    # Dónde vive el porcentaje: sirve para ver cuánto pesan anexos, tablas y cada fuente.
    todo, fuentes = 0, {}
    for n, total, marc, pf, inicio in resumen:
        todo += marc
        for k, v in pf.items():
            fuentes[k] = fuentes.get(k, 0) + v
        top = ", ".join(f"f{k}:{v}" for k, v in sorted(pf.items(), key=lambda x: -x[1])[:4])
        print(f"  hoja {n:>2} · {marc:>3} de {total:>3} resaltadas · {top:<28} · {inicio[:50]}")
    print(f"Total resaltado: {todo} palabras. Por fuente: "
          + ", ".join(f"f{k}:{v}" for k, v in sorted(fuentes.items(), key=lambda x: -x[1])[:10]))
cruzar_tramos(tramos, docx, salida)
