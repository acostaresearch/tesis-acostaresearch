r"""Pone el índice de tablas (o de figuras) como lo pone Word con Referencias > Insertar tabla de
ilustraciones: un campo  TOC \h \z \c "Tabla"  que se arma solo con los rótulos del documento.

    python indice_tablas_word.py <entrada.docx> <salida.docx> [--rotulo Tabla] [--despues "ÍNDICE DE TABLAS"]
    powershell -File indice.ps1 -ruta <salida.docx con ruta completa>      (lo rellena con las páginas reales)

Para que Word encuentre las tablas, cada rótulo tiene que llevar su número como campo SEQ, que es
lo que hace Referencias > Insertar título. Este script lo deja así sin cambiar el aspecto APA:

    Tabla 1                      un solo párrafo:  «Tabla » + campo { SEQ Tabla \* ARABIC } +
    Título en cursiva            salto de línea (Mayús+Intro) + el título en cursiva

Si el rótulo y el título venían en dos párrafos, los une en uno con el salto de línea en medio:
se ve igual, y la entrada del índice sale «Tabla 1 Título … página». Quita las entradas que
hubiera escritas a mano debajo del título del índice (párrafos con estilo de índice).
"""
import copy
import re
import sys

from docx import Document
from docx.oxml import parse_xml

import comun  # noqa: F401

a = sys.argv[1:]
ent, sal = a[0], a[1]
rotulo = a[a.index("--rotulo") + 1] if "--rotulo" in a else "Tabla"
despues = a[a.index("--despues") + 1] if "--despues" in a else ("ÍNDICE DE TABLAS" if rotulo == "Tabla" else "ÍNDICE DE FIGURAS")

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = f'xmlns:w="{W}"'
Q = "{" + W + "}"
d = Document(ent)
P = list(d.paragraphs)

ancla = next((p for p in P if p.text.strip().lower() == despues.lower()), None)
if ancla is None:
    sys.exit(f"No encuentro el párrafo «{despues}» (--despues).")

# 1) los rótulos: número como campo SEQ y título en el mismo párrafo
ES_ROTULO = re.compile(rf"^{rotulo}\s+(\d+)\.?$", re.I)
hechos = 0
for i, p in enumerate(P):
    m = ES_ROTULO.match(p.text.strip())
    if not m or "toc" in p.style.name.lower() or "instrText" in p._p.xml:
        continue
    runs = list(p.runs)
    base = runs[0]
    rpr = base._r.find(Q + "rPr")
    rpr_xml = "" if rpr is None else re.sub(r' xmlns:\w+="[^"]*"', "", rpr.xml if hasattr(rpr, "xml") else "")
    for r in runs[1:]:
        r._r.getparent().remove(r._r)
    base.text = f"{rotulo} "

    def tramo(dentro):
        nr = copy.deepcopy(base._r)
        for h in list(nr):
            if h.tag != Q + "rPr":
                nr.remove(h)
        nr.append(parse_xml(dentro))
        return nr

    cola = base._r
    for dentro in (f'<w:fldChar {NS} w:fldCharType="begin"/>',
                   rf'<w:instrText {NS} xml:space="preserve"> SEQ {rotulo} \* ARABIC </w:instrText>',
                   f'<w:fldChar {NS} w:fldCharType="separate"/>',
                   f'<w:t {NS}>{m.group(1)}</w:t>',
                   f'<w:fldChar {NS} w:fldCharType="end"/>'):
        nr = tramo(dentro)
        cola.addnext(nr)
        cola = nr
    # el título, si viene en el párrafo siguiente, se trae a este tras un salto de línea
    sig = P[i + 1] if i + 1 < len(P) else None
    if sig is not None and sig.text.strip() and not ES_ROTULO.match(sig.text.strip()) and sig._p.getprevious() is p._p:
        nr = tramo(f'<w:br {NS}/>')
        cola.addnext(nr)
        cola = nr
        for r in list(sig._p.findall(Q + "r")):
            cola.addnext(r)
            cola = r
        sig._p.getparent().remove(sig._p)
    hechos += 1
ya = sum(1 for p in P if f"SEQ {rotulo} " in p._p.xml)
if hechos == 0 and ya:
    print(f"Los {ya} rótulos de «{rotulo}» ya traían su campo SEQ: solo se pone el índice.")
elif hechos == 0:
    sys.exit(f"No hay rótulos «{rotulo} N» en párrafo propio: no hay nada que listar.")

# 2) fuera las entradas escritas a mano bajo el título del índice
sig = ancla._p.getnext()
while sig is not None and sig.tag == Q + "p":
    est = sig.find(Q + "pPr/" + Q + "pStyle")
    nombre = est.get(Q + "val", "") if est is not None else ""
    if not re.match(r"(TOC|TDC|Tabladeilustraciones|TableofFigures)", nombre, re.I):
        break
    otro = sig.getnext()
    sig.getparent().remove(sig)
    sig = otro

# 3) el campo de Word
campo = parse_xml(
    f'<w:p {NS}><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
    rf'<w:r><w:instrText xml:space="preserve"> TOC \h \z \c "{rotulo}" </w:instrText></w:r>'
    '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
    '<w:r><w:t>Actualice el índice: clic derecho, Actualizar campo.</w:t></w:r>'
    '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>')
ancla._p.addnext(campo)
d.save(sal)
print(f"{hechos} rótulos de «{rotulo}» con campo SEQ; índice puesto detrás de «{despues}». Falta rellenarlo con indice.ps1.")
