"""Aplica reescrituras con fichas ⟦C1|…⟧ / ⟦F1|…⟧ conservando las citas de Mendeley.

Uso: aplicar_fichas.py entrada.docx salida.docx cambios1.json [cambios2.json ...] [--probar]
Cada cambio: {"parrafo": N, "nuevo": "texto con todas las fichas del original, una vez cada una"}
Comprueba: mismas fichas, mismas cifras, sin raya larga. --probar valida sin guardar.
"""
import sys, re, json, copy, collections
from docx import Document
from docx.oxml.ns import qn
from fichas import piezas, con_fichas

sys.stdout.reconfigure(encoding="utf-8")
FICHA = re.compile(r"⟦([CF])(\d+)\|[^⟧]*⟧")
NUM = re.compile(r"\d+(?:[.,]\d+)*")


def cifras(s):
    return collections.Counter(NUM.findall(FICHA.sub(" ", s)))


def run_con(texto, modelo):
    r = copy.deepcopy(modelo)
    for e in list(r):
        if e.tag != qn("w:rPr"):
            r.remove(e)
    t = r.makeelement(qn("w:t"), {})
    t.text = texto
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    r.append(t)
    return r


def aplicar(p, nuevo, i):
    ps, _ = piezas(p)
    if ps is None:
        return f"¶{i}: el párrafo tiene campos o hipervínculos"
    viejo = con_fichas(ps)
    a = sorted(m.group(1) + m.group(2) for m in FICHA.finditer(viejo))
    b = sorted(m.group(1) + m.group(2) for m in FICHA.finditer(nuevo))
    if a != b:
        return f"¶{i}: fichas distintas {a} vs {b}"
    if cifras(viejo) != cifras(nuevo):
        return f"¶{i}: cifras distintas {dict(cifras(viejo) - cifras(nuevo))} faltan, {dict(cifras(nuevo) - cifras(viejo))} sobran"
    if "—" in nuevo or "–" in FICHA.sub("", nuevo) and "–" not in FICHA.sub("", viejo):
        return f"¶{i}: raya larga"
    # elementos por ficha
    fichas, nc, nf, modelo = {}, 0, 0, None
    for tipo, els, t in ps:
        if tipo == "C":
            nc += 1
            fichas[f"C{nc}"] = els
        elif tipo == "F" and t.strip():
            nf += 1
            fichas[f"F{nf}"] = els
        elif tipo == "T" and modelo is None:
            modelo = els[0]
    if modelo is None:
        modelo = next(e for tipo, els, t in ps if tipo in "TF" for e in els)
    for e in [e for e in p if e.tag != qn("w:pPr")]:
        p.remove(e)
    pos = 0
    for m in FICHA.finditer(nuevo):
        if m.start() > pos:
            p.append(run_con(nuevo[pos:m.start()], modelo))
        for e in fichas[m.group(1) + m.group(2)]:
            p.append(e)
        pos = m.end()
    if pos < len(nuevo):
        p.append(run_con(nuevo[pos:], modelo))
    return None


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    probar = "--probar" in sys.argv
    ent, sal, jsons = args[0], args[1], args[2:]
    d = Document(ent)
    P = d.paragraphs
    errores, n = [], 0
    for j in jsons:
        for c in json.load(open(j, encoding="utf8")):
            err = aplicar(P[c["parrafo"]]._p, c["nuevo"], c["parrafo"])
            if err:
                errores.append(f"{j}: {err}")
            else:
                n += 1
    for e in errores:
        print("ERROR", e)
    print(f"{n} párrafos aplicados, {len(errores)} errores")
    if not errores and not probar:
        d.save(sal)
        print("guardado", sal)
    sys.exit(1 if errores else 0)
