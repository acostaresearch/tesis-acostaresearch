"""Escribe las correcciones en una copia del Word, conservando letra, tamaño y estilo.

    python aplicar.py <entrada.docx> <salida.docx> <cambios.json>

Los números de párrafo (¶) y de tabla (T) son los de leer.py sobre el Word de ENTRADA; no se corren
aunque se inserte o borre, porque todo se resuelve antes de tocar nada. cambios.json es una lista:

    {"parrafo": 10, "nuevo": "párrafo entero reescrito"}
    {"parrafo": 10, "viejo": "tramo exacto", "nuevo": "tramo corregido"}
    {"despues_de": 12, "texto": "párrafo nuevo", "como": 12}       «como» = párrafo del que copia el formato
    {"borrar": 15}
    {"celda": [3, 1, 2], "nuevo": "S/ 25.00"}                       [tabla, fila, columna]

En «nuevo» y «texto», *así* queda en cursiva (títulos de revista y de libro en las referencias).
No se guarda nada si algún cambio falla o mete una raya larga.
"""
import copy
import json
import re
import sys

from docx import Document
from docx.text.paragraph import Paragraph

import comun  # noqa: F401  (deja la salida en UTF-8)

ent, sal, cam = sys.argv[1:4]
d = Document(ent)
P = list(d.paragraphs)
T = list(d.tables)


def escribir(p, texto):
    """Deja el párrafo con ese texto y el formato de su primer tramo; *…* va en cursiva."""
    runs = list(p.runs)
    base = runs[0] if runs else p.add_run("")
    for r in runs[1:]:
        r._r.getparent().remove(r._r)
    for h in p._p.findall("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hyperlink"):
        p._p.remove(h)
    trozos = [x for x in re.split(r"(\*[^*\n]+\*)", texto) if x]
    base.text = ""
    ultimo = base
    for k, tr in enumerate(trozos):
        cur = tr.startswith("*") and tr.endswith("*") and len(tr) > 2
        if k == 0:
            r = base
        else:
            nuevo = copy.deepcopy(base._r)
            ultimo._r.addnext(nuevo)
            r = type(base)(nuevo, p)
        r.text = tr[1:-1] if cur else tr
        if cur:
            r.italic = True
        elif k and base.italic:
            r.italic = base.italic
        ultimo = r


fallos, hechos, cola = 0, 0, {}
for c in json.load(open(cam, encoding="utf-8")):
    nuevo = c.get("nuevo", c.get("texto", ""))
    if re.search(r"[—–]", nuevo) and not c.get("forzar"):
        print(f"FALLA: entró una raya larga en {json.dumps(c, ensure_ascii=False)[:90]}")
        fallos += 1
        continue
    if re.search(r"\[[^\]\d]{0,40}\]", nuevo) and "[Tesis" not in nuevo and "[Trabajo" not in nuevo:
        print(f"AVISO: queda un hueco entre corchetes en: {nuevo[:80]}")
    try:
        if "celda" in c:
            t, f, k = c["celda"]
            celda = T[t].rows[f].cells[k]
            ps = celda.paragraphs
            escribir(ps[0], nuevo)
            for p in ps[1:]:
                p._p.getparent().remove(p._p)
            print(f"T{t} f{f} c{k} OK")
        elif "borrar" in c:
            p = P[c["borrar"]]
            p._p.getparent().remove(p._p)
            print(f"¶{c['borrar']} borrado")
        elif "despues_de" in c:
            ancla = cola.get(c["despues_de"], P[c["despues_de"]]._p)
            el = copy.deepcopy(P[c.get("como", c["despues_de"])]._p)
            ancla.addnext(el)
            escribir(Paragraph(el, P[c["despues_de"]]._parent), nuevo)
            cola[c["despues_de"]] = el
            print(f"nuevo tras ¶{c['despues_de']} OK · {len(nuevo.split())} palabras")
        else:
            i = c["parrafo"]
            p = P[i]
            orig = p.text
            viejo = c.get("viejo")
            if viejo is None or viejo == orig:
                escribir(p, nuevo)
            else:
                if viejo not in orig:
                    raise ValueError(f"«viejo» no está tal cual. Empieza por: {viejo[:60]!r}")
                if sum(len(r.text) for r in p.runs) != len(orig):
                    raise ValueError("tiene texto fuera de los tramos normales (enlace); reemplazar el párrafo entero")
                a0 = orig.index(viejo)
                b0 = a0 + len(viejo)
                pos, puesto = 0, False
                for r in list(p.runs):
                    t = r.text
                    a, b = pos, pos + len(t)
                    pos = b
                    if b <= a0 or a >= b0:
                        continue
                    antes = t[:a0 - a] if a < a0 else ""
                    resto = t[b0 - a:] if b > b0 else ""
                    if not puesto:
                        r.text = antes + nuevo + resto
                        puesto = True
                    elif resto:
                        r.text = resto
                    else:
                        r._r.getparent().remove(r._r)
            print(f"¶{i} OK · {len((viejo or orig).split())} → {len(nuevo.split())} palabras")
        hechos += 1
    except Exception as e:
        print(f"FALLA en {json.dumps(c, ensure_ascii=False)[:70]}: {e}")
        fallos += 1

if fallos:
    sys.exit(f"\nNo se guardó nada: {fallos} cambio(s) con problema. Corrígelos y vuelve a correr.")
d.save(sal)
print(f"\nGuardado: {sal} · {hechos} cambios")
