#!/usr/bin/env python3
"""Verifica que una reescritura no rompio el documento.

Uso:
  python verificar_cambios.py antes.docx despues.docx
  python verificar_cambios.py antes.docx despues.docx --entregado texto_entregado.txt

Comprueba tres cosas que se rompen con facilidad al reescribir en lote:
citas perdidas, cifras perdidas y cambios en el numero de parrafos. Lo ultimo
importa porque los documentos convertidos desde PDF traen parrafos partidos a
mitad de oracion, y fusionarlos por descuido descuadra la maquetacion.

Con --entregado calcula ademas cuanto texto literal se desplazo respecto de la
version que ya se entrego. Ese numero mide el trabajo hecho, NO predice la
similitud: Turnitin compara contra su indice, no contra la version anterior.
"""
import argparse
import re
import sys

try:
    from docx import Document
except ImportError:
    sys.exit("Falta python-docx:  pip install python-docx --break-system-packages")


def parrafos(ruta):
    return [p.text for p in Document(ruta).paragraphs]


def citas(t):
    """Citas entre parentesis. Las narrativas (Autor (2021) dice) se cuentan aparte."""
    return set(re.findall(r"\(([^)]*\d{4}[^)]*)\)", t))


def autores_narrativos(t):
    return set(re.findall(r"([A-ZÁÉÍÓÚÑ][\wÁÉÍÓÚÑáéíóúñ\-]+(?:\s+(?:y|et al\.)\s+[\wÁÉÍÓÚÑáéíóúñ\-]+)?)\s*\(\d{4}\)", t))


def cifras(t):
    return set(re.findall(r"\b\d[\d.,]*%?\b", t))


def ventanas(texto, n=7):
    w = re.sub(r"\s+", " ", texto).split()
    return [" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("antes")
    ap.add_argument("despues")
    ap.add_argument("--entregado", help="txt con el texto de la version ya entregada")
    args = ap.parse_args()

    a, b = parrafos(args.antes), parrafos(args.despues)

    print(f"Parrafos: {len(a)} -> {len(b)}", end="  ")
    if len(a) != len(b):
        print("<<< CAMBIO. Revisar: se fusionaron o partieron parrafos.")
    else:
        print("ok")

    cambiados = [i for i in range(min(len(a), len(b))) if a[i].strip() != b[i].strip()]
    print(f"Parrafos modificados: {len(cambiados)}")

    txt_a = " ".join(a[i] for i in cambiados)
    txt_b = " ".join(b[i] for i in cambiados)

    perdidas = citas(txt_a) - citas(txt_b)
    movidas = {c for c in perdidas
               if re.split(r"[,;]", c)[0].strip() in " ".join(autores_narrativos(txt_b))}
    reales = perdidas - movidas
    print(f"Citas perdidas: {sorted(reales) if reales else 'ninguna'}")
    if movidas:
        print(f"  (convertidas a cita narrativa, no perdidas: {sorted(movidas)})")

    perd_num = cifras(txt_a) - cifras(txt_b)
    print(f"Cifras perdidas: {sorted(perd_num) if perd_num else 'ninguna'}")
    if perd_num:
        print("  Revisar una por una: puede ser un dato borrado o un numero escrito en letra.")

    palabras_a = len(re.findall(r"\b\w+\b", txt_a))
    palabras_b = len(re.findall(r"\b\w+\b", txt_b))
    print(f"Palabras en los tramos tocados: {palabras_a} -> {palabras_b}")

    if args.entregado:
        ref = re.sub(r"\s+", " ", open(args.entregado, encoding="utf-8", errors="replace").read())
        vs = ventanas(txt_b)
        sobreviven = sum(1 for v in vs if v in ref)
        if vs:
            pct = 100 * sobreviven / len(vs)
            print(f"\nSecuencias de 7 palabras identicas a lo ya entregado: "
                  f"{sobreviven}/{len(vs)} = {pct:.1f}%")
            print(f"Texto literal desplazado: {100 - pct:.1f}%")
            print("Esto mide cuanto cambio la redaccion. NO predice el porcentaje de")
            print("similitud, porque Turnitin compara contra su indice y no contra esta version.")


if __name__ == "__main__":
    main()
