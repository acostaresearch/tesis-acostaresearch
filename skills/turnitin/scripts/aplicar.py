"""Escribe las reescrituras en una copia del Word, conservando letra, tamaño y estilo.

    python aplicar.py <entrada.docx> <salida.docx> <cambios.json>

cambios.json es una lista. Cada cambio reemplaza un tramo exacto de un párrafo:

    [{"parrafo": 10, "viejo": "texto exacto tal como está en el Word", "nuevo": "reescritura"}]

«viejo» puede ser el párrafo entero o solo las oraciones marcadas. Si se omite, se reemplaza todo el
párrafo. Nada se guarda si algún cambio pierde una cita o una cifra, salvo que lleve "forzar": true.
"""
import json
import re
import sys

from docx import Document

import comun  # noqa: F401  (deja la salida en UTF-8)

ent, sal, cam = sys.argv[1:4]
d = Document(ent)
P = d.paragraphs


def citas(s):
    return sorted(x.strip() for c in re.findall(r"\(([^()]*\d{4}[^()]*)\)", s)
                  for x in c.split(";") if re.search(r"\d{4}", x))


def cifras(s):
    return sorted(re.findall(r"\d+(?:[.,]\d+)?", s))


fallos = 0
for c in json.load(open(cam, encoding="utf-8")):
    i, nuevo = c["parrafo"], c["nuevo"]
    p = P[i]
    orig = p.text
    viejo = c.get("viejo") or orig
    if c.get("ini"):
        # «ini» = cómo empieza la oración que se reemplaza; evita copiar la oración entera.
        cand = [o.strip() for o in comun.oraciones(orig) if o.strip().startswith(c["ini"])]
        if len(cand) != 1:
            print(f"¶{i} FALLA: {len(cand)} oraciones empiezan por {c['ini']!r}")
            fallos += 1
            continue
        viejo = cand[0]
    if viejo not in orig:
        print(f"¶{i} FALLA: «viejo» no está tal cual en el párrafo. Empieza por: {viejo[:60]!r}")
        fallos += 1
        continue
    if sum(len(r.text) for r in p.runs) != len(orig):
        print(f"¶{i} FALLA: el párrafo tiene texto fuera de los tramos normales "
              "(enlace o cambio con seguimiento); hay que editarlo a mano")
        fallos += 1
        continue
    prob = []
    if citas(viejo) != citas(nuevo):
        prob.append(f"citas {citas(viejo)} → {citas(nuevo)}")
    if cifras(viejo) != cifras(nuevo):
        prob.append(f"cifras {cifras(viejo)} → {cifras(nuevo)}")
    if re.search(r"[—–]", nuevo) and not re.search(r"[—–]", viejo):
        prob.append("entró una raya larga")
    if prob and not c.get("forzar"):
        print(f"¶{i} FALLA: " + " · ".join(prob))
        fallos += 1
        continue
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
    assert p.text == orig[:a0] + nuevo + orig[b0:], f"¶{i}: el párrafo no quedó como se esperaba"
    print(f"¶{i} OK · {len(viejo.split())} → {len(nuevo.split())} palabras · "
          f"citas {len(citas(viejo))} · cifras {len(cifras(viejo))}"
          + (" · FORZADO: " + " · ".join(prob) if prob else ""))

if fallos:
    sys.exit(f"\nNo se guardó nada: {fallos} cambio(s) con problema. Corrígelos y vuelve a correr.")
d.save(sal)
print(f"\nGuardado: {sal}")
