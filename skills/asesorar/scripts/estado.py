"""Qué clientes hay y en qué va cada uno; o el detalle de una carpeta.

    python estado.py                  lista de clientes
    python estado.py CURASMA          archivos de ese cliente, clasificados
"""
import re
import sys
from datetime import datetime

from comun import ETAPAS, RAIZ, carpeta, norm, texto_pdf

fecha = lambda p: datetime.fromtimestamp(p.stat().st_mtime).strftime("%d-%b %H:%M")


def etapa(d):
    hay = {x.name.lower() for x in d.iterdir() if x.is_dir()}
    cot = d / "cotizacion.md"
    est = ""
    if cot.exists():
        m = re.search(r"^Estado:\s*(.+)$", cot.read_text(encoding="utf-8"), re.M)
        est = m.group(1).strip() if m else "cotizado"
    if "05-pasadoporturnitin" in hay and any((d / "05-pasadoporturnitin").iterdir()):
        return "pasado por Turnitin" + (f" · {est}" if est else "")
    if "02-corregida" in hay or "02-reformulada" in hay:
        return "trabajo hecho" + (f" · {est}" if est else "")
    return est or "sin cotizar"


def clase(f):
    """avance, guía, reporte u otro, por lo que dice dentro y, si no alcanza, por el nombre."""
    n = norm(f.stem)
    try:
        if f.suffix.lower() == ".docx":
            from docx import Document
            t = " ".join(p.text for p in Document(f).paragraphs)
        else:
            t = texto_pdf(f)
    except Exception as e:
        return f"NO SE PUDO ABRIR ({e})", 0
    pal = len(t.split())
    tn = norm(t[:200000])
    if any(x in tn for x in ("detectado como ia", "similitud general", "indice de similitud", "informe de originalidad")):
        return "reporte de Turnitin", pal
    guia = sum(x in n for x in ("guia", "manual", "esquema", "formato", "estructura", "reglamento", "lineamiento", "plantilla"))
    guia += sum(x in tn for x in ("se redacta en", "debe describir", "no debe exceder", "se detalla", "el tesista debe",
                                  "el estudiante debe", "guia para la elaboracion", "esquema de"))
    en_nombre = any(x in n.split() for x in ("guia", "manual", "esquema", "reglamento", "lineamientos", "plantilla"))
    if en_nombre or (guia >= 2 and pal < 5000):
        return "guía de la universidad", pal
    if f.suffix.lower() == ".pdf" and pal < 150:
        return "PDF sin texto (escaneado: leerlo como imagen)", pal
    return "avance del cliente", pal


if len(sys.argv) < 2:
    print(f"CLIENTES en {RAIZ}\n")
    for d in sorted((x for x in RAIZ.iterdir() if x.is_dir()), key=lambda x: -x.stat().st_mtime):
        print(f"  {d.name} · {etapa(d)} · {fecha(d)}")
    sys.exit()

base = carpeta(sys.argv[1])
print(f"CARPETA  {base}\nETAPA    {etapa(base)}\n")
faltan = [e for e in ETAPAS if not (base / e).is_dir()]
if faltan:
    print("Subcarpetas que aún no existen: " + ", ".join(faltan) + "\n")
for f in sorted(base.rglob("*")):
    if f.is_dir() or f.name.startswith("~") or f.name == "cotizacion.md":
        continue
    rel = f.relative_to(base)
    if rel.parts[0].lower() == "borrar":
        print(f"  [obsoleto, en borrar] {rel} · {fecha(f)}")
    elif f.suffix.lower() in (".docx", ".pdf"):
        c, pal = clase(f)
        if rel.parts[0].lower()[:2] in ("02", "03", "04", "05"):
            c = "nuestro" if "reporte" not in c else c  # lo que ya entregó la skill, no material del cliente
        print(f"  [{c}] {rel} · {pal} palabras · {fecha(f)}")
    else:
        print(f"  [otro] {rel} · {fecha(f)}")
if (base / "borrar").is_dir() and any((base / "borrar").iterdir()):
    print("\nHay archivos en borrar\\: al terminar, preguntar a Benicio si se elimina esa carpeta.")
if (base / "cotizacion.md").exists():
    print("\nHay cotizacion.md: leerla antes de seguir.")
