"""Ordena una carpeta de trabajo: crea actual, Listo, Subir a Turnitin y reportes\\ia|similitud, y pone cada archivo suelto en su sitio.

    python ordenar.py 06-PAULA
    python ordenar.py 06-PAULA --ver     solo dice qué haría

Mueve, nunca borra ni sobrescribe: si en el destino ya hay un archivo con ese nombre, lo deja donde está y avisa.
"""
import re
import sys

import pymupdf

from comun import SUBIR, carpeta, es_asesoria, sub, tipo_de_reporte

base = carpeta(sys.argv[1])
ver = "--ver" in sys.argv
if es_asesoria(base):
    sys.exit(f"CARPETA  {base}\n  Tiene la organización de asesoría: se conserva y no se ordena.")


def asegurar(padre, *nombres):
    d = sub(padre, *(n.lower() for n in nombres)) if padre.is_dir() else None
    if d is None:
        d = padre / nombres[0]
        print(f"  crea   {d.relative_to(base)}\\")
        if not ver:
            d.mkdir(parents=True, exist_ok=True)
    return d


def mover(f, destino):
    if f.parent == destino:
        return
    if (destino / f.name).exists():
        print(f"  QUEDA  {f.relative_to(base)} · ya hay uno con ese nombre en {destino.relative_to(base)}\\")
        return
    print(f"  mueve  {f.relative_to(base)}  →  {destino.relative_to(base)}\\")
    if not ver:
        f.rename(destino / f.name)


def tipo_pdf(p):
    try:
        return tipo_de_reporte("\n".join(pg.get_text() for pg in pymupdf.open(p)))
    except Exception:
        return None


print(f"CARPETA  {base}")
actual = asegurar(base, "actual")
listo = asegurar(base, "Listo")
para_subir = asegurar(base, SUBIR)
# Los recortados que quedaron en Listo antes de existir la carpeta: Listo es solo lo que se envía al tesista.
for f in sorted(listo.glob("*.docx")) if listo.is_dir() else []:
    if re.search(r" - para turnitin( \d+)?$", f.stem, re.I) and not f.name.startswith("~"):
        mover(f, para_subir)
rep =asegurar(base, "reportes", "reporte")
destino = {"ia": asegurar(rep, "ia"), "similitud": asegurar(rep, "similitud")}

# Lo suelto en la raíz: los Word van a actual (o a Listo si ya son una salida de la skill);
# los PDF, a su carpeta de reporte, y si no son de Turnitin son el documento del cliente.
for f in sorted(base.iterdir()):
    if not f.is_file() or f.name.startswith("~"):
        continue
    ext = f.suffix.lower()
    if ext in (".docx", ".doc"):
        salida = re.search(r" - (humanizado|similitud)( \d+)?$", f.stem)
        recortado = re.search(r" - para turnitin( \d+)?$", f.stem, re.I)
        mover(f, para_subir if recortado else listo if salida else actual)
    elif ext == ".pdf":
        t = tipo_pdf(f)
        mover(f, destino[t] if t else actual)
    else:
        print(f"  QUEDA  {f.name} · no es Word ni PDF")

# Los PDF que ya estaban en reportes, sueltos o en la subcarpeta del otro tipo.
if rep.is_dir():
    for p in sorted(rep.rglob("*.pdf")):
        t = tipo_pdf(p)
        if t is None:
            print(f"  QUEDA  {p.relative_to(base)} · no parece un reporte de Turnitin")
        else:
            mover(p, destino[t])

print("Listo." if not ver else "Nada se movió: fue solo la vista previa.")
