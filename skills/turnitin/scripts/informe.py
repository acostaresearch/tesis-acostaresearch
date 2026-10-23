"""Anatomía de un informe de similitud de Turnitin, en formato nuevo o clásico.

    python informe.py <reporte.pdf> [--meta 18]

Dice el porcentaje, el desglose, los filtros, cuántas fuentes hay y cuáles pesan más, si es un
mosaico o hay un bloque, y con --meta cuántas palabras coincidentes hay que quitar, a ojo.
El formato nuevo lo lee leer_informe.py (de la skill bajar-similitud); el clásico, este script.
"""
import re
import subprocess
import sys
from pathlib import Path

import pymupdf

import comun  # noqa: F401  (deja la salida en UTF-8)

pdf = sys.argv[1]
meta = int(sys.argv[sys.argv.index("--meta") + 1]) if "--meta" in sys.argv else None
t = "\n".join(pg.get_text() for pg in pymupdf.open(pdf))

if "INDICE DE SIMILITUD" not in t:
    subprocess.run([sys.executable, str(Path(__file__).with_name("leer_informe.py")), pdf],
                   env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
    m = re.search(r"(\d+)\s*%\s*Similitud general", t)
    pal = re.search(r"([\d.]+)\s+palabras", t)
    total = int(m.group(1)) if m else None
    palabras = int(pal.group(1).replace(".", "")) if pal else None
else:
    num = lambda etq: (re.search(r"(\d+)%\n" + etq, t) or [None, "?"])[1]
    total = int(num("INDICE DE SIMILITUD"))
    pal = re.search(r"Total de palabras:\s*(\d+)", t)
    palabras = int(pal.group(1)) if pal else None
    filtros = dict(re.findall(r"(Excluir citas|Excluir bibliografía|Excluir coincidencias)\n([^\n]+)", t))
    pcts = re.findall(r"\n\d+\n(<?\d+)%", t[t.index("INDICE DE SIMILITUD"):])
    nombres = re.findall(r"\n([^\n]+)\n(?:Fuente de Internet|Trabajo del estudiante|Publicación)", t)
    fuentes = list(zip(pcts, nombres))
    internet, publ, trab = num("FUENTES DE INTERNET"), num("PUBLICACIONES"), num("TRABAJOS DEL ESTUDIANTE")
    print("Formato                  : clásico (hojas como foto)")
    print(f"Identificador de entrega : {comun.dato(t, 'Identificador de la entrega')}")
    print(f"Archivo analizado        : {comun.dato(t, 'Nombre del archivo')}")
    print(f"Similitud general        : {total}%")
    print(f"  Internet {internet}% · Publicaciones {publ}% · Trabajos de estudiantes {trab}%")
    print(f"Palabras del documento   : {palabras}")
    print("Filtros                  : " + " · ".join(f"{k}: {v}" for k, v in filtros.items()))
    print(f"Fuentes listadas         : {len(pcts)}")
    print("Fuentes de mayor peso:")
    for p, n in fuentes[:8]:
        print(f"   {p:>3}%  {n}")
    suma = sum(int(x) for x in (internet, publ, trab) if x.isdigit())
    if suma > total:
        print(f"\nSolapamiento: los cubos suman {suma}% y el total es {total}%: la misma frase coincide con "
              "varias fuentes, que es la firma de la redacción estándar del campo.")
    mayor = int(pcts[0].lstrip("<")) if pcts else 0
    if mayor >= 8:
        print(f"\nBLOQUE: la fuente principal aporta {mayor}%. Buscarla en el cuerpo antes que nada: "
              "puede ser una cita textual mal marcada.")
    else:
        print(f"\nMOSAICO: {len(pcts)} fuentes y la mayor aporta {mayor}%. No hay un bloque copiado; "
              "son tramos cortos repartidos. Reescribir rinde poco y los filtros rinden más.")
    apagados = [k for k, v in filtros.items() if v.strip().lower().startswith("apag")]
    if apagados:
        print("Filtros apagados que bajarían el número sin tocar el texto: " + ", ".join(apagados))

if meta is not None and total is not None and palabras:
    falta = total - meta + 1
    if falta <= 0:
        print(f"\nMeta: menos de {meta}%. El informe ya la cumple ({total}%).")
    else:
        print(f"\nMeta: menos de {meta}%. Hay que bajar unos {falta} puntos, que son alrededor de "
              f"{falta * palabras // 100} palabras coincidentes menos (estimado: Turnitin no dice cómo redondea).")
