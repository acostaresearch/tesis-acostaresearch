# Copia un Word dejando solo los párrafos a..b (índices de doc.paragraphs) y las tablas entre ellos.
# Uso: python partir.py <word.docx> <salida.docx> <desde> <hasta>
import sys, copy, docx
from docx.oxml.ns import qn
src, out, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
d = docx.Document(src)
body = d.element.body
i = -1; keep_prev = False; words = 0
for el in list(body):
    if el.tag == qn('w:p'):
        i += 1
        keep_prev = a <= i <= b
        if not keep_prev: body.remove(el)
        else: words += len(''.join(t.text or '' for t in el.iter(qn('w:t'))).split())
    elif el.tag == qn('w:sectPr'):
        continue
    elif not keep_prev:
        body.remove(el)
d.save(out)
print(f'{out.split("/")[-1]}: ¶{a}-{b}, {words} palabras')
