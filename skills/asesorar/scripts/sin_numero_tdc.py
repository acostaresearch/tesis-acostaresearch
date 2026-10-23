import sys
from docx import Document
from lxml import etree
Q = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
d = Document(sys.argv[1])
n = 0
for p in d.element.body.iter(Q + "p"):
    st = p.find(f"{Q}pPr/{Q}pStyle")
    if st is not None and ("TDC" in st.get(Q + "val") or "TOCHeading" in st.get(Q + "val")) and p.find(f"{Q}pPr/{Q}numPr") is None:
        pp = p.find(Q + "pPr")
        np_ = etree.Element(Q + "numPr")
        il = etree.SubElement(np_, Q + "ilvl"); il.set(Q + "val", "0")
        ni = etree.SubElement(np_, Q + "numId"); ni.set(Q + "val", "0")
        st.addnext(np_)
        n += 1
d.save(sys.argv[2])
print("títulos de índice sin número:", n)
