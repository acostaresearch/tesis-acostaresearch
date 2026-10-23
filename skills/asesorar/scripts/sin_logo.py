"""Copia del Word completo para Turnitin: igual al original, solo sin el logo de la carátula.

Uso: python sin_logo.py <entrada.docx> <salida.docx>

Quita las imágenes (w:drawing y w:pict) de la carátula, es decir, de los párrafos y tablas
anteriores al primer salto de sección. No toca el resto: declaratorias, índices, cuerpo,
referencias y anexos se quedan como están, también sus imágenes. Si la carátula no tiene
imágenes, lo dice y guarda la copia igual.
"""
import sys

import docx

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def main(entrada, salida):
    d = docx.Document(entrada)
    cuerpo = d.element.body
    quitadas = 0
    for el in list(cuerpo):
        if el.tag == W + "sectPr":
            break
        for tag in ("drawing", "pict"):
            for img in list(el.iter(W + tag)):
                r = img.getparent()
                # se borra el tramo entero si solo lleva la imagen; si no, solo la imagen
                otros = [c for c in r if c.tag not in (W + "rPr", W + tag)]
                if r.tag == W + "r" and not otros:
                    r.getparent().remove(r)
                else:
                    r.remove(img)
                quitadas += 1
        # el primer párrafo con salto de sección cierra la carátula
        if el.tag == W + "p" and el.find(W + "pPr/" + W + "sectPr") is not None:
            break
    d.save(salida)
    if quitadas:
        print(f"logo quitado: {quitadas} imagen(es) de la carátula -> {salida}")
    else:
        print(f"la carátula no tiene imágenes; copia guardada igual -> {salida}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
