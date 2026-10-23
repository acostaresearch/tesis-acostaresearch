"""Herramientas para rehacer el Word de Lander conservando las citas de Mendeley Cite."""
import base64, copy, json, random, re, uuid
from docx.oxml.ns import qn
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
Q = "{" + W + "}"
TAG = "MENDELEY_CITATION_v3_"


def txt(el):
    return "".join(t.text or "" for t in el.iter(Q + "t"))


def leer_json(sdt):
    v = sdt.find(f"{Q}sdtPr/{Q}tag").get(Q + "val")
    b = v[len(TAG):]
    return json.loads(base64.b64decode(b + "=" * (-len(b) % 4)).decode("utf8"))


def poner_json(sdt, js):
    b = base64.b64encode(json.dumps(js, ensure_ascii=False).encode("utf8")).decode()
    sdt.find(f"{Q}sdtPr/{Q}tag").set(Q + "val", TAG + b)


def poner_texto_sdt(sdt, texto):
    ts = list(sdt.find(Q + "sdtContent").iter(Q + "t"))
    ts[0].text = texto
    ts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    for t in ts[1:]:
        t.text = ""


class Citas:
    def __init__(self, body):
        self.lista = []
        for el in body.iter(Q + "sdt"):
            tg = el.find(f"{Q}sdtPr/{Q}tag")
            if tg is not None and tg.get(Q + "val", "").startswith(TAG):
                self.lista.append(el)
        self.items = {}
        for el in self.lista:
            for ci in leer_json(el)["citationItems"]:
                self.items[ci["id"]] = ci["itemData"]
        self.molde = self.lista[0]

    def item(self, familia, anio, con_doi=None):
        cands = [i for i in self.items.values()
                 if any(familia.lower() == (a.get("family") or "").lower() for a in i.get("author", [])[:1])
                 and (i.get("issued", {}).get("date-parts") or [[0]])[0][0] == anio]
        if con_doi is not None:
            cands = [i for i in cands if bool(i.get("DOI")) == con_doi] or cands
        if not cands:
            raise KeyError(f"{familia} {anio}")
        return cands[0]

    def corregir(self, n, texto, items=None):
        """Cambia el texto visible de la cita n (y su texto manual en Mendeley)."""
        el = self.lista[n]
        js = leer_json(el)
        js["manualOverride"]["isManuallyOverridden"] = True
        js["manualOverride"]["manualOverrideText"] = texto
        if items is not None:
            js["citationItems"] = [{"id": i["id"], "itemData": i, "isTemporary": False} for i in items]
        poner_json(el, js)
        poner_texto_sdt(el, texto)

    def clonar(self, n, texto=None):
        el = copy.deepcopy(self.lista[n])
        el.find(f"{Q}sdtPr/{Q}id").set(Q + "val", str(random.randint(-2**31, 2**31 - 1)))
        js = leer_json(el)
        js["citationID"] = "MENDELEY_CITATION_" + str(uuid.uuid4())
        if texto is not None:
            js["manualOverride"]["isManuallyOverridden"] = True
            js["manualOverride"]["manualOverrideText"] = texto
            poner_texto_sdt(el, texto)
        poner_json(el, js)
        return el

    def nueva(self, items, texto, parentetica):
        el = copy.deepcopy(self.molde)
        el.find(f"{Q}sdtPr/{Q}id").set(Q + "val", str(random.randint(-2**31, 2**31 - 1)))
        js = {"citationID": "MENDELEY_CITATION_" + str(uuid.uuid4()), "properties": {"noteIndex": 0}, "isEdited": False,
              "manualOverride": {"isManuallyOverridden": not parentetica, "citeprocText": parentetica_txt(items),
                                 "manualOverrideText": "" if parentetica else texto},
              "citationItems": [{"id": i["id"], "itemData": i, "isTemporary": False} for i in items]}
        poner_json(el, js)
        poner_texto_sdt(el, texto)
        return el


def parentetica_txt(items):
    partes = []
    for i in items:
        au = i.get("author", [])
        f = lambda a: a.get("family") or a.get("literal")
        if len(au) == 1:
            n = f(au[0])
        elif len(au) == 2:
            n = f"{f(au[0])} & {f(au[1])}"
        else:
            n = f"{f(au[0])} et al."
        partes.append(f"{n}, {i['issued']['date-parts'][0][0]}")
    return "(" + "; ".join(partes) + ")"


ORDEN_RPR = ["rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike", "dstrike", "outline", "shadow",
             "emboss", "imprint", "noProof", "snapToGrid", "vanish", "webHidden", "color", "spacing", "w", "kern",
             "position", "sz", "szCs", "highlight", "u", "effect", "bdr", "shd", "fitText", "vertAlign", "rtl", "cs",
             "em", "lang", "eastAsianLayout", "specVanish", "oMath"]


def ordenar_rpr(pr):
    def clave(e):
        n = etree.QName(e).localname
        return ORDEN_RPR.index(n) if n in ORDEN_RPR and etree.QName(e).namespace == W else 99
    hijos = sorted(list(pr), key=clave)
    for h in hijos:
        pr.remove(h)
    for h in hijos:
        pr.append(h)


def fijar(pr, nombre, val=None, quitar=False):
    e = pr.find(Q + nombre)
    if quitar:
        if e is not None:
            pr.remove(e)
        return
    if e is None:
        e = etree.SubElement(pr, Q + nombre)
    if val is not None:
        e.set(Q + "val", str(val))
    return e


def run(texto, rpr=None, it=False, b=False, amarillo=False, sup=False, sub=False, sz=None):
    r = etree.Element(Q + "r")
    pr = copy.deepcopy(rpr) if rpr is not None else etree.Element(Q + "rPr")
    for k in ("highlight", "vertAlign", "u"):
        fijar(pr, k, quitar=True)
    if b: fijar(pr, "b")
    if it: fijar(pr, "i")
    if amarillo: fijar(pr, "highlight", "yellow")
    if sup or sub: fijar(pr, "vertAlign", "superscript" if sup else "subscript")
    if sz: fijar(pr, "sz", sz); fijar(pr, "szCs", sz)
    ordenar_rpr(pr)
    r.append(pr)
    t = etree.SubElement(r, Q + "t"); t.text = texto
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    return r
