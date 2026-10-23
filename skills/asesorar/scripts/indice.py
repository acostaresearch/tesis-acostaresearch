import sys, copy, docx
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn

d = docx.Document(sys.argv[1])
P = d.paragraphs
W = nsdecls("w")

# estilos del índice (toc 1-3), con el ancho de texto de la página vertical: 11906 - 1701 - 1440
for n, sangria in ((1, 0), (2, 240), (3, 480)):
    d.styles.element.append(parse_xml(
        f'<w:style {W} w:type="paragraph" w:styleId="TDC{n}"><w:name w:val="toc {n}"/><w:basedOn w:val="Normal"/>'
        f'<w:next w:val="Normal"/><w:uiPriority w:val="39"/><w:unhideWhenUsed/><w:pPr>'
        f'<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="8765"/></w:tabs>'
        f'<w:spacing w:after="0" w:line="360" w:lineRule="auto"/><w:ind w:left="{sangria}"/></w:pPr>'
        + ('<w:rPr><w:b/><w:bCs/></w:rPr>' if n == 1 else '') + '</w:style>'))

def titulo(texto):
    return parse_xml(f'<w:p {W}><w:pPr><w:pageBreakBefore/><w:spacing w:after="240" w:line="360" w:lineRule="auto"/>'
                     f'<w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t>{texto}</w:t></w:r></w:p>')

def campo(instr, estilo, antes=""):
    return (f'{antes}<w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> {instr} </w:instrText></w:r>'
            f'<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>0</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r>')

nuevos = [titulo("ÍNDICE"),
          parse_xml(f'<w:p {W}><w:pPr><w:pStyle w:val="TDC1"/></w:pPr>' + campo(r'TOC \o "1-3" \h \z \u', "TDC1") + '</w:p>'),
          titulo("ÍNDICE DE TABLAS")]

# una línea por tabla, con marcador en su leyenda y PAGEREF
k = 0
for i, p in enumerate(P):
    t = p.text.strip()
    if t.startswith("Tabla ") and t[6:].isdigit():
        k += 1
        marca = f"_TablaIdx{k}"
        p._p.insert(1, parse_xml(f'<w:bookmarkStart {W} w:id="{900 + k}" w:name="{marca}"/>'))
        p._p.append(parse_xml(f'<w:bookmarkEnd {W} w:id="{900 + k}"/>'))
        nombre = P[i + 1].text.strip().replace("&", "&amp;")
        nuevos.append(parse_xml(f'<w:p {W}><w:pPr><w:pStyle w:val="TDC2"/><w:ind w:left="0"/></w:pPr>'
                                f'<w:r><w:t xml:space="preserve">{t}. {nombre}</w:t></w:r><w:r><w:tab/></w:r>'
                                + campo(rf'PAGEREF {marca} \h', "TDC2") + '</w:p>'))

corte = P[15]._p  # el párrafo que cierra la sección de la carátula
assert corte.find(qn("w:pPr")).find(qn("w:sectPr")) is not None
for e in nuevos:
    corte.addprevious(e)
d.save(sys.argv[2])
print("tablas en el índice:", k)
