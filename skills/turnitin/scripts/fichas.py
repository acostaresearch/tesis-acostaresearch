"""Vuelca los párrafos con coincidencias como texto con fichas protegidas.

⟦C3|Pérez (2019)⟧ = cita de Mendeley (w:sdt), ⟦F2|texto⟧ = tramo con formato propio
(cursiva, resaltado, superíndice). El texto llano es lo único reescribible.
Uso: fichas.py doc.docx ms.json salida_dir ntramos
"""
import sys, json, re, collections
from docx import Document
from docx.oxml.ns import qn

sys.stdout.reconfigure(encoding="utf-8")
W = qn


def rpr_key(r):
    rpr = r.find(W("w:rPr"))
    if rpr is None:
        return ""
    import copy
    c = copy.deepcopy(rpr)
    for t in ("w:lang", "w:noProof", "w:rFonts", "w:sz", "w:szCs", "w:color", "w:kern", "w:shd"):
        for e in c.findall(W(t)):
            c.remove(e)
    for e in list(c):
        if "w14" in e.tag or e.tag.endswith("}ligatures"):
            c.remove(e)
    if len(c) == 0:
        return ""
    from lxml import etree
    return etree.tostring(c).decode()


def run_text(r):
    out = []
    for e in r:
        if e.tag == W("w:t"):
            out.append(e.text or "")
        elif e.tag == W("w:tab"):
            out.append("\t")
        elif e.tag in (W("w:br"), W("w:cr")):
            out.append("\n")
    return "".join(out)


def piezas(p):
    """Lista de (tipo, elementos, texto). tipo: T texto llano, C cita, F formato propio, X otro."""
    hijos = [e for e in p if e.tag != W("w:pPr")]
    runs = [e for e in hijos if e.tag == W("w:r")]
    peso = collections.Counter()
    for r in runs:
        peso[rpr_key(r)] += len(run_text(r))
    dom = peso.most_common(1)[0][0] if peso else ""
    out = []
    for e in hijos:
        if e.tag == W("w:r"):
            if e.find(".//" + W("w:fldChar")) is not None or e.find(".//" + W("w:instrText")) is not None or e.find(".//" + W("w:drawing")) is not None:
                return None, dom
            t = run_text(e)
            tipo = "T" if rpr_key(e) == dom else "F"
            if out and out[-1][0] == tipo and (tipo == "T" or rpr_key(out[-1][1][-1]) == rpr_key(e)):
                out[-1][1].append(e)
                out[-1][2] += t
            else:
                out.append([tipo, [e], t])
        elif e.tag == W("w:sdt"):
            t = "".join(x.text or "" for x in e.iter(W("w:t")))
            out.append(["C", [e], t])
        elif e.tag in (W("w:proofErr"), W("w:bookmarkStart"), W("w:bookmarkEnd")):
            out.append(["X", [e], ""])
        else:
            return None, dom  # hipervínculos, ecuaciones, etc.: no se toca
    return out, dom


def con_fichas(ps):
    s, nc, nf = [], 0, 0
    for tipo, els, t in ps:
        if tipo == "T":
            s.append(t)
        elif tipo == "C":
            nc += 1
            s.append(f"⟦C{nc}|{t}⟧")
        elif tipo == "F":
            if t.strip() == "":
                s.append(t)
                continue
            nf += 1
            s.append(f"⟦F{nf}|{t}⟧")
    return "".join(s)


if __name__ == "__main__":
    doc, ms, sal, n = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
    d = Document(doc)
    P = d.paragraphs
    ini = next(i for i, p in enumerate(P) if p.text.strip().upper().endswith("INTRODUCCIÓN") and p.style.name.lower().startswith(("ttulo", "heading", "título")))
    fin = next(i for i, p in enumerate(P) if i > ini and "BIBLIOGRAF" in p.text.upper() and p.style.name.lower().startswith(("ttulo", "heading", "título")))
    m = {x["parrafo"]: x for x in json.load(open(ms, encoding="utf8"))}
    items = []
    for i in range(ini, fin):
        x = m.get(i)
        if not x:
            continue
        p = P[i]
        if p.style.name.lower().startswith(("ttulo", "heading", "título", "caption", "descripci")):
            continue
        if len(p.text.split()) < 8:
            continue
        ps, _ = piezas(p._p)
        if ps is None:
            continue
        marcadas = [o["visto"] for o in x["oraciones"] if o["coinciden"] >= 4]
        if not marcadas:
            continue
        items.append({"parrafo": i, "estilo": p.style.name, "coinciden": x["coinciden"], "texto": con_fichas(ps), "marcadas": marcadas})
    tot = sum(len(it["texto"].split()) for it in items)
    print("inicio", ini, "fin", fin, "párrafos", len(items), "palabras", tot, "coincidentes", sum(it["coinciden"] for it in items))
    meta = tot / n
    tramo, acc, k = [], 0, 1
    for it in items:
        tramo.append(it)
        acc += len(it["texto"].split())
        if acc >= meta * k and k < n:
            json.dump(tramo, open(f"{sal}/tramo{k}.json", "w", encoding="utf8"), ensure_ascii=False, indent=1)
            print("tramo", k, len(tramo), "párrafos", tramo[0]["parrafo"], "-", tramo[-1]["parrafo"])
            tramo, k = [], k + 1
    json.dump(tramo, open(f"{sal}/tramo{k}.json", "w", encoding="utf8"), ensure_ascii=False, indent=1)
    print("tramo", k, len(tramo), "párrafos", tramo[0]["parrafo"], "-", tramo[-1]["parrafo"])
