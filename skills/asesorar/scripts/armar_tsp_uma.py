"""Arma un TSP de Psicología (estudio de caso) sobre la plantilla de la UMA.

    python armar_tsp_uma.py plantilla.docx datos.json texto.txt tablas.json salida.docx

datos.json: titulo, autores [..], orcid [..], asesor, declaracion, dedicatoria, agradecimiento,
resumen, palabras, abstract, keywords. Textos con *cursiva*, **negrita** y [[amarillo]].
texto.txt: «# » nivel 1 · «## » nivel 2 · «### » nivel 3 · «[TABLA id]» · «[REFERENCIAS]»…«[FIN]»
· «[SALTO]» · «[HORIZONTAL]» / «[VERTICAL]» (sección apaisada) · «> » párrafo sin sangría
(datos de filiación) · el resto, párrafos con sangría de 1,27 cm.
Copia el formato de los párrafos de la propia plantilla (títulos y cuerpo: Arial 11, doble
espacio, alineado a la izquierda, sangría de primera línea).
"""
import copy
import json
import re
import sys

from docx import Document
from docx.oxml import parse_xml
from docx.oxml.ns import qn

plantilla, datos_f, texto_f, tablas_f, salida = sys.argv[1:6]
D = json.load(open(datos_f, encoding="utf-8"))
TAB = json.load(open(tablas_f, encoding="utf-8"))
W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'

d = Document(plantilla)
body = d.element.body
P = d.paragraphs


def buscar(txt):
    for p in d.paragraphs:
        if p.text.strip() == txt:
            return p
    sys.exit(f"No encuentro «{txt}» en la plantilla")


PROTO = {
    "h1": copy.deepcopy(buscar("I. INTRODUCCIÓN")._p),
    "h2": copy.deepcopy(buscar("1.1. Situación problemática")._p),
    "h3": copy.deepcopy(buscar("Objetivo general")._p),
    "cuerpo": copy.deepcopy(next(p for p in d.paragraphs if p.text.startswith("Planteamiento de lo general"))._p),
}
RPR = PROTO["cuerpo"].find(qn("w:r")).find(qn("w:rPr"))


def limpiar_rpr(rpr):
    for t in ("w:b", "w:bCs", "w:i", "w:iCs", "w:highlight"):
        for x in rpr.findall(qn(t)):
            rpr.remove(x)


def poner_runs(p_el, txt, base_rpr=None, bold=False, italic=False, size=None):
    base = copy.deepcopy(base_rpr if base_rpr is not None else RPR)
    limpiar_rpr(base)
    for trozo in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*|\[\[[^\]]+\]\])", txt):
        if not trozo:
            continue
        b = bold or trozo.startswith("**")
        it = italic or (trozo.startswith("*") and not trozo.startswith("**"))
        am = trozo.startswith("[[")
        t = trozo[2:-2] if (trozo.startswith("**") or am) else (trozo[1:-1] if it and trozo.startswith("*") else trozo)
        r = parse_xml(f"<w:r {W}/>")
        rpr = copy.deepcopy(base)
        if b:
            rpr.append(parse_xml(f'<w:b {W}/>'))
            rpr.append(parse_xml(f'<w:bCs {W}/>'))
        if it:
            rpr.append(parse_xml(f'<w:i {W}/>'))
            rpr.append(parse_xml(f'<w:iCs {W}/>'))
        if am:
            rpr.append(parse_xml(f'<w:highlight {W} w:val="yellow"/>'))
        if size:
            for s in rpr.findall(qn("w:sz")) + rpr.findall(qn("w:szCs")):
                s.set(qn("w:val"), str(size * 2))
        # orden válido de rPr: rFonts, b, bCs, i, iCs, ..., highlight, sz
        orden = ["rFonts", "b", "bCs", "i", "iCs", "color", "highlight", "sz", "szCs", "rtl"]
        hijos = sorted(list(rpr), key=lambda e: orden.index(e.tag.split("}")[1]) if e.tag.split("}")[1] in orden else 50)
        for h in list(rpr):
            rpr.remove(h)
        for h in hijos:
            rpr.append(h)
        r.append(rpr)
        tt = parse_xml(f'<w:t {W} xml:space="preserve"></w:t>')
        tt.text = t
        r.append(tt)
        p_el.append(r)


def reescribir(p, txt, **kw):
    """Cambia el texto de un párrafo de la plantilla conservando su formato."""
    r0 = p._p.find(qn("w:r"))
    base = r0.find(qn("w:rPr")) if r0 is not None else None
    base = copy.deepcopy(base) if base is not None else None
    for r in p._p.findall(qn("w:r")):
        p._p.remove(r)
    poner_runs(p._p, txt, base, **kw)


def borrar(p):
    p._p.getparent().remove(p._p)


def clonar_despues(p, txt, **kw):
    nuevo = copy.deepcopy(p._p)
    for r in nuevo.findall(qn("w:r")):
        nuevo.remove(r)
    p._p.addnext(nuevo)
    base = p._p.find(qn("w:r"))
    poner_runs(nuevo, txt, base.find(qn("w:rPr")) if base is not None else None, **kw)
    from docx.text.paragraph import Paragraph
    return Paragraph(nuevo, p._parent)


# ---------- carátula ----------
reescribir(buscar("[TÍTULO DEL ESTUDIO DE CASO]"), D["titulo"].upper(), bold=True)
p_aut = buscar("APELLIDOS APELLIDOS, NOMBRE NOMBRE")
p_orc = buscar("https://orcid.org/XXXX-XXXX-XXXX-XXXX")
# segundo autor: autor 1, orcid 1, autor 2, orcid 2
reescribir(p_aut, D["autores"][0])
reescribir(p_orc, D["orcid"][0])
q = clonar_despues(p_orc, D["autores"][1])
clonar_despues(q, D["orcid"][1])
reescribir(buscar("[GRADO Y NOMBRE DEL ASESOR/A]"), D["asesor"])
orcs = [p for p in d.paragraphs if p.text.strip() == "https://orcid.org/XXXX-XXXX-XXXX-XXXX"]
reescribir(orcs[-1], D["orcid_asesor"])

# ---------- declaración ----------
p_yo = next(p for p in d.paragraphs if p.text.startswith("Yo, [NOMBRE"))
reescribir(p_yo, D["declaracion"][0])
p_ind = next(p for p in d.paragraphs if p.text.startswith("Indico que dicho"))
reescribir(p_ind, D["declaracion"][1])
p_con = next(p for p in d.paragraphs if p.text.startswith("Conforme a lo indicado"))
reescribir(p_con, D["declaracion"][2])
p_fecha = next(p for p in d.paragraphs if p.text.startswith("Lima, ____"))
reescribir(p_fecha, D["declaracion_fecha"])
p_linea = next(p for p in d.paragraphs if p.text.startswith("______"))
p_nom = buscar("[NOMBRE COMPLETO DEL AUTOR/A]")
reescribir(p_nom, D["firmas"][0])
x = clonar_despues(p_nom, "")
# un párrafo vacío menos tras la fecha, para que las dos firmas quepan en la hoja
sig = p_fecha._p.getnext()
if sig is not None and not "".join(sig.itertext()).strip():
    sig.getparent().remove(sig)
x2 = copy.deepcopy(p_linea._p)
x._p.addnext(x2)
from docx.text.paragraph import Paragraph
x3 = clonar_despues(Paragraph(x2, p_linea._parent), D["firmas"][1])
borrar(next(p for p in d.paragraphs if p.text.startswith("Nota: adjuntar")))

reescribir(next(p for p in d.paragraphs if p.text.startswith("[Espacio dedicado")), D["dedicatoria"])
reescribir(next(p for p in d.paragraphs if p.text.startswith("[Reconocimiento a")), D["agradecimiento"])

# ---------- resumen y abstract ----------
p_r = next(p for p in d.paragraphs if p.text.startswith("Redactado en tiempo pasado"))
lista = []
nx = p_r._p.getnext()
while nx is not None and nx.find(qn("w:pPr")) is not None and nx.find(qn("w:pPr")).find(qn("w:numPr")) is not None:
    lista.append(nx)
    nx = nx.getnext()
for e in lista:
    e.getparent().remove(e)
reescribir(p_r, D["resumen"], italic=False)
ppr = p_r._p.find(qn("w:pPr"))
ppr.insert(0, parse_xml(f'<w:ind {W} w:firstLine="720"/>')) if ppr.find(qn("w:ind")) is None else None
reescribir(next(p for p in d.paragraphs if p.text.startswith("Palabras clave:")), D["palabras"])
p_a = next(p for p in d.paragraphs if p.text.startswith("Traducción fiel"))
reescribir(p_a, D["abstract"], italic=False)
ppr = p_a._p.find(qn("w:pPr"))
if ppr.find(qn("w:ind")) is None:
    ppr.insert(0, parse_xml(f'<w:ind {W} w:firstLine="720"/>'))
reescribir(next(p for p in d.paragraphs if p.text.startswith("Keywords:")), D["keywords"])

# ---------- índices: se quitan las instrucciones ----------
for ini in ("(Para actualizar", "Listado de las tablas"):
    for p in list(d.paragraphs):
        if p.text.startswith(ini):
            borrar(p)

# ---------- se borra el cuerpo de instrucciones de la plantilla ----------
corte = next(p for p in d.paragraphs if p.text.startswith("FORMATO DE ESTUDIO DE CASO"))._p
sect = body.find(qn("w:sectPr"))
e = corte
while e is not None and e is not sect:
    sig = e.getnext()
    body.remove(e)
    e = sig


# ---------- cuerpo ----------
def nuevo(tipo, txt, sangria=True, **kw):
    el = copy.deepcopy(PROTO[tipo])
    for r in el.findall(qn("w:r")):
        el.remove(r)
    base = PROTO[tipo].find(qn("w:r")).find(qn("w:rPr"))
    if tipo == "cuerpo" and not sangria:
        ind = el.find(qn("w:pPr")).find(qn("w:ind"))
        if ind is not None:
            ind.set(qn("w:firstLine"), "0")
    poner_runs(el, txt, base, **kw)
    sect.addprevious(el)
    return el


def salto():
    el = parse_xml(f'<w:p {W}><w:r><w:br w:type="page"/></w:r></w:p>')
    sect.addprevious(el)


def seccion(horizontal):
    """Cierra la sección actual con la orientación contraria y deja la final con la pedida."""
    actual = copy.deepcopy(sect)
    for x in actual.findall(qn("w:pgNumType")):
        actual.remove(x)
    el = parse_xml(f'<w:p {W}><w:pPr/></w:p>')
    el.find(qn("w:pPr")).append(actual)
    sect.addprevious(el)
    sz = sect.find(qn("w:pgSz"))
    for x in sect.findall(qn("w:pgNumType")):
        sect.remove(x)
    if horizontal:
        sz.set(qn("w:w"), "15840"); sz.set(qn("w:h"), "12240"); sz.set(qn("w:orient"), "landscape")
    else:
        sz.set(qn("w:w"), "12240"); sz.set(qn("w:h"), "15840"); sz.set(qn("w:orient"), "portrait")


def borde(tc, lados):
    tcPr = tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f"<w:tcBorders {W}>" + "".join(
        f'<w:{l} w:val="{v}" w:sz="8" w:space="0" w:color="000000"/>' for l, v in lados.items()) + "</w:tcBorders>"))


def tabla(cfg):
    a = nuevo("cuerpo", f"Tabla {cfg['n']}", sangria=False, bold=True)
    a.find(qn("w:pPr")).append(parse_xml(f'<w:keepNext {W}/>'))
    b = nuevo("cuerpo", cfg["titulo"], sangria=False, italic=True)
    b.find(qn("w:pPr")).append(parse_xml(f'<w:keepNext {W}/>'))
    filas = [cfg["encabezado"]] + cfg["filas"]
    t = d.add_table(rows=len(filas), cols=len(cfg["encabezado"]))
    tbl = t._tbl
    sect.addprevious(tbl)
    tblPr = tbl.tblPr
    tblPr.append(parse_xml(f'<w:tblW {W} w:w="5000" w:type="pct"/>'))
    tblPr.append(parse_xml(f'<w:tblLook {W} w:val="0000" w:firstRow="0" w:lastRow="0" w:firstColumn="0" w:lastColumn="0" w:noHBand="1" w:noVBand="1"/>'))
    tam = cfg.get("letra", 10)
    for i, fila in enumerate(filas):
        for j, v in enumerate(fila):
            c = t.cell(i, j)
            pe = c.paragraphs[0]._p
            pe.append(parse_xml(f'<w:pPr {W}><w:spacing w:after="0" w:before="0" w:line="240" w:lineRule="auto"/><w:jc w:val="left"/></w:pPr>')) if pe.find(qn("w:pPr")) is None else None
            lineas = str(v).split("\n")
            for k, ln in enumerate(lineas):
                if k:
                    pe.append(parse_xml(f'<w:r {W}><w:br/></w:r>'))
                poner_runs(pe, ln, bold=(i == 0), size=tam)
            lados = {}
            if i == 0:
                lados = {"top": "single", "bottom": "single"}
            if i == len(filas) - 1:
                lados["bottom"] = "single"
            if lados:
                borde(c._tc, lados)
        trPr = t.rows[i]._tr.get_or_add_trPr()
        trPr.append(parse_xml(f"<w:cantSplit {W}/>"))
        if i == 0:
            trPr.append(parse_xml(f"<w:tblHeader {W}/>"))
    if cfg.get("anchos"):
        tblPr.replace(tblPr.find(qn("w:tblW")), parse_xml(f'<w:tblW {W} w:w="{int(sum(cfg["anchos"]) * 567)}" w:type="dxa"/>'))
        tblPr.append(parse_xml(f'<w:tblLayout {W} w:type="fixed"/>'))
        for gc, an in zip(tbl.tblGrid.findall(qn("w:gridCol")), cfg["anchos"]):
            gc.set(qn("w:w"), str(int(an * 567)))
        from docx.shared import Cm
        for j, an in enumerate(cfg["anchos"]):
            for fila in t.rows:
                fila.cells[j].width = Cm(an)
    if cfg.get("nota"):
        nt = nuevo("cuerpo", "*Nota.* " + cfg["nota"], sangria=False, size=10)
        sp = nt.find(qn("w:pPr")).find(qn("w:spacing"))
        if sp is not None:
            sp.set(qn("w:line"), "240")
        nt.find(qn("w:pPr")).append(parse_xml(f'<w:spacing {W} w:before="80"/>')) if sp is None else sp.set(qn("w:before"), "80")
    nuevo("cuerpo", "", sangria=False)


lineas = [l.rstrip("\n") for l in open(texto_f, encoding="utf-8-sig")]
en_refs = False
for l in lineas:
    l = l.strip()
    if not l:
        continue
    if l == "[FIN]":
        en_refs = False
        continue
    if en_refs:
        el = nuevo("cuerpo", l, sangria=False)
        ind = el.find(qn("w:pPr")).find(qn("w:ind"))
        if ind is None:
            ind = parse_xml(f"<w:ind {W}/>")
            el.find(qn("w:pPr")).append(ind)
        for k in list(ind.attrib):
            del ind.attrib[k]
        ind.set(qn("w:left"), "720")
        ind.set(qn("w:hanging"), "720")
        continue
    if l == "[REFERENCIAS]":
        en_refs = True
        continue
    if l == "[SALTO]":
        salto()
        continue
    if l == "[HORIZONTAL]":
        seccion(True)
        continue
    if l == "[VERTICAL]":
        seccion(False)
        continue
    if l.startswith("[TABLA "):
        tabla(TAB[l[7:-1]])
        continue
    if l.startswith("### "):
        nuevo("h3", l[4:])
        continue
    if l.startswith("## "):
        nuevo("h2", l[3:])
        continue
    if l.startswith("# "):
        nuevo("h1", l[2:])
        continue
    if l.startswith("> "):
        nuevo("cuerpo", l[2:], sangria=False)
        continue
    nuevo("cuerpo", l)

d.save(salida)
print("guardado", salida)
