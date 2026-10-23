r"""Pone el índice como lo pone Word con Referencias > Tabla de contenido > Tabla automática.

    python indice_word.py <entrada.docx> <salida.docx> [--despues "Índice de contenidos"] [--sin-titulo]
    powershell -File indice.ps1 -ruta <salida.docx con ruta completa>      (lo rellena con las páginas reales)

Es la misma pieza que inserta Word (copiada del índice que Benicio actualizó a mano el 11-oct-2026):
un control de contenido de la galería «Table of Contents» con el título «Contenido» (estilo TOC
Heading, en negro y negrita) y, dentro, un único campo  TOC \o "1-3" \h \z \u . Word lo reconoce
como tabla automática: muestra «Actualizar tabla» al hacer clic y lo rehace con clic derecho.

Los títulos entran por su nivel de esquema: o llevan estilo Título 1 a 3, o un `w:outlineLvl`
(0, 1, 2) en su `pPr`, que no cambia la letra. Este script no los marca: se marcan antes.

--despues   texto del párrafo tras el que va el índice (por defecto, el título de su hoja).
--sin-titulo  no escribe «Contenido» (cuando la hoja ya trae su propio título y basta con uno).
Si ya había un índice automático (otro control de la misma galería), lo reemplaza.
"""
import sys

from docx import Document
from docx.oxml import parse_xml

import comun  # noqa: F401

a = sys.argv[1:]
ent, sal = a[0], a[1]
despues = a[a.index("--despues") + 1] if "--despues" in a else "Índice de contenidos"
con_titulo = "--sin-titulo" not in a

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = f'xmlns:w="{W}"'
Q = "{" + W + "}"
d = Document(ent)
est = d.styles.element


def id_de(nombre):
    """El styleId del estilo con ese nombre interno («toc 1» es TDC1 en un Word en español)."""
    for s in est.findall(Q + "style"):
        n = s.find(Q + "name")
        if n is not None and n.get(Q + "val", "").lower() == nombre.lower():
            return s.get(Q + "styleId")
    return None


# estilos del índice, solo si el documento no los trae (los valores son los que crea Word)
for n, sangria in ((1, 0), (2, 240), (3, 480)):
    if not id_de(f"toc {n}"):
        ind = f'<w:ind w:left="{sangria}"/>' if sangria else ""
        est.append(parse_xml(
            f'<w:style {NS} w:type="paragraph" w:styleId="TOC{n}"><w:name w:val="toc {n}"/><w:basedOn w:val="{id_de("Normal") or "Normal"}"/>'
            f'<w:next w:val="{id_de("Normal") or "Normal"}"/><w:autoRedefine/><w:uiPriority w:val="39"/><w:unhideWhenUsed/>'
            f'<w:pPr><w:spacing w:after="100"/>{ind}</w:pPr></w:style>'))
if not id_de("TOC Heading"):
    est.append(parse_xml(
        f'<w:style {NS} w:type="paragraph" w:styleId="TOCHeading"><w:name w:val="TOC Heading"/><w:basedOn w:val="{id_de("Normal") or "Normal"}"/>'
        f'<w:next w:val="{id_de("Normal") or "Normal"}"/><w:uiPriority w:val="39"/><w:unhideWhenUsed/><w:qFormat/>'
        '<w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="240" w:line="259" w:lineRule="auto"/><w:outlineLvl w:val="9"/></w:pPr>'
        '<w:rPr><w:b/><w:bCs/><w:color w:val="000000"/><w:sz w:val="32"/><w:szCs w:val="32"/></w:rPr></w:style>'))

cuerpo = d.element.body
for sdt in list(cuerpo.findall(Q + "sdt")):
    g = sdt.find(".//" + Q + "docPartGallery")
    if (g is not None and g.get(Q + "val") == "Table of Contents") or " TOC " in "".join(t.text or "" for t in sdt.iter(Q + "instrText")):
        cuerpo.remove(sdt)

ancla = next((p for p in d.paragraphs if p.text.strip() == despues), None)
if ancla is None:
    sys.exit(f"No encuentro el párrafo «{despues}» para poner el índice detrás (--despues).")

titulo = (
    f'<w:p><w:pPr><w:pStyle w:val="{id_de("TOC Heading")}"/><w:rPr><w:b/><w:bCs/><w:color w:val="000000"/></w:rPr></w:pPr>'
    '<w:r><w:rPr><w:b/><w:bCs/><w:color w:val="000000"/></w:rPr><w:t>Contenido</w:t></w:r></w:p>'
) if con_titulo else ""
sdt = parse_xml(
    f'<w:sdt {NS}><w:sdtPr><w:docPartObj><w:docPartGallery w:val="Table of Contents"/><w:docPartUnique/></w:docPartObj></w:sdtPr>'
    f'<w:sdtContent>{titulo}'
    f'<w:p><w:pPr><w:pStyle w:val="{id_de("toc 1")}"/></w:pPr>'
    '<w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
    r'<w:r><w:instrText xml:space="preserve"> TOC \o "1-3" \h \z \u </w:instrText></w:r>'
    '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
    '<w:r><w:t>Actualice el índice: clic derecho, Actualizar campo.</w:t></w:r></w:p>'
    '<w:p><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>'
    '</w:sdtContent></w:sdt>')
ancla._p.addnext(sdt)
d.save(sal)
print(f"Índice automático puesto detrás de «{despues}». Falta rellenarlo: indice.ps1 -ruta <ruta completa>")
