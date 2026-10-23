#!/usr/bin/env python3
"""Mide la uniformidad de la prosa, párrafo por párrafo (español o inglés).

Uso:  python3 medir_estilo.py seccion.md [--idioma es|en]
      python3 medir_estilo.py ARTICULO_x_v4.docx --seccion "Métodos"

Solo orienta: marca los párrafos con señales de prosa de plantilla. No es una
meta que perseguir ni un detector de IA. Sin dependencias (python-docx solo si
se mide un .docx).
"""
import argparse
import re
import statistics
import sys

FUNC_ES = set("""a al algo ante antes aquel aquella aquellas aquellos aqui así aun aunque bajo bien cada como con
contra cual cuales cuando de del desde donde dos e el ella ellas ellos en entre era eran es esa esas ese eso esos esta
estaba estas este esto estos fue fueron ha han hasta hay la las le les lo los mas más me mi mientras muy ni no nos o
otra otras otro otros para pero poco por porque que qué se sea ser si sí sin sino sobre son su sus tal también tan
tanto te todo todos tras tu u un una uno unos unas y ya""".split())
FUNC_EN = set("""a about above after again against all also an and any are as at be because been before being
below between both but by can could did do does doing during each few for from further had has have having he her
here hers him his how i if in into is it its itself just may might more most no nor not of off on once only or other
our out over own same she should so some such than that the their them then there these they this those through to
too under until up very was we were what when where which while who whom why will with would you""".split())


def oraciones(p):
    p = re.sub(r"\b(et al|e\.g|i\.e|cf|vs|p|pp|Fig|Tab|n|N|M|DE|SD)\.", lambda m: m.group(0).replace(".", "§"), p)
    trozos = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿¡(\"“])", p)
    return [t.replace("§", ".") for t in trozos if t.strip()]


def palabras(t):
    return re.findall(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü'’-]+", t)


def parrafos_md(texto):
    out, buf = [], []
    for ln in texto.splitlines():
        s = ln.strip()
        if not s or s.startswith("#") or s.startswith("|") or s.startswith("["):
            if buf:
                out.append(" ".join(buf)); buf = []
            continue
        buf.append(s)
    if buf:
        out.append(" ".join(buf))
    return out


def parrafos_docx(ruta, seccion):
    from docx import Document
    doc, actual, out = Document(ruta), "", []
    for p in doc.paragraphs:
        if p.style.name.lower().startswith(("heading", "título")):
            if p.style.name.endswith("1"):
                actual = p.text.strip()
            continue
        if seccion and actual.lower() != seccion.lower():
            continue
        if len(p.text.split()) > 25:
            out.append(p.text.strip())
    return out


def medir(p, func):
    ors = oraciones(p)
    largos = [len(palabras(o)) for o in ors]
    pals = palabras(p)
    if not pals or not largos:
        return None
    disp = statistics.pstdev(largos) / statistics.mean(largos) if len(largos) > 1 else 0.0
    cortas = sum(1 for n in largos if n <= 8) / len(largos)
    largo_pal = sum(len(w) for w in pals) / len(pals)
    funcionales = sum(1 for w in pals if w.lower() in func) / len(pals)
    alarmas = []
    if len(largos) > 2 and disp < 0.35:
        alarmas.append("oraciones de largo parejo")
    if len(largos) > 5 and cortas == 0:
        alarmas.append("ninguna oración corta")
    if largo_pal > 5.6:
        alarmas.append("palabras largas (nominalización)")
    if funcionales < 0.38:
        alarmas.append("pocas palabras funcionales")
    return dict(n=len(pals), o=len(largos), disp=disp, cortas=cortas, lp=largo_pal, fun=funcionales, alarmas=alarmas)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("archivo")
    ap.add_argument("--idioma", choices=["es", "en"], default="es")
    ap.add_argument("--seccion")
    a = ap.parse_args()
    func = FUNC_EN if a.idioma == "en" else FUNC_ES
    if a.archivo.lower().endswith(".docx"):
        pars = parrafos_docx(a.archivo, a.seccion)
    else:
        with open(a.archivo, encoding="utf-8") as f:
            texto = f.read()
        # sin referencias; con --seccion, solo esa sección (# Título)
        texto = re.split(r"^#\s+(Referencias|References)\s*$", texto, flags=re.M | re.I)[0]
        if a.seccion:
            partes = re.split(r"^#\s+(.+)$", texto, flags=re.M)
            sec = [partes[k + 1] for k in range(1, len(partes) - 1, 2) if partes[k].strip().lower() == a.seccion.lower()]
            texto = "\n".join(sec)
        pars = parrafos_md(texto)
    marcados = 0
    print("par  palabras  oraciones  dispersión  cortas  largo_pal  funcionales  señales")
    for i, p in enumerate(pars, 1):
        m = medir(p, func)
        if not m:
            continue
        marcados += bool(m["alarmas"])
        print(f"{i:>3}  {m['n']:>8}  {m['o']:>9}  {m['disp']:>10.2f}  {m['cortas']:>5.0%}  {m['lp']:>9.2f}  {m['fun']:>10.0%}  "
              + ("; ".join(m["alarmas"]) or "—"))
    print(f"\n{marcados} de {len(pars)} párrafos con señales. Corregir solo esos.")


if __name__ == "__main__":
    sys.exit(main())
