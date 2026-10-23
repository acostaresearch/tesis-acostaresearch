#!/usr/bin/env python3
"""Verifica que una reescritura no rompio el documento.

Uso:
  python verificar_cambios.py antes.md despues.md
  python verificar_cambios.py antes.md despues.md --entregado texto_entregado.txt
  python verificar_cambios.py antes.docx despues.docx --entregado texto_entregado.txt

Acepta .docx (camino del documento externo) y texto plano o Markdown (.txt,
.md), que es como sale el capitulo de ver_capitulo y como se guarda con
guardar_capitulo. En texto plano, un parrafo es un bloque separado por linea
en blanco.

Comprueba lo que se rompe con facilidad al reescribir en lote: citas perdidas,
claves de cita [AR...] perdidas, inventadas o cambiadas de parrafo, cifras
perdidas y cambios en el numero de parrafos. Lo ultimo importa porque los
documentos convertidos desde PDF traen parrafos partidos a mitad de oracion, y
fusionarlos por descuido descuadra la maquetacion; y porque en el texto del
proyecto cada parrafo tiene que salir con las mismas claves.

Cuentan como cita: las claves del proyecto [AR1234ABCD], [AR1234ABCD:n],
[AR1234ABCD:p. 45], la marca [FALTA FUENTE] y las citas entre parentesis con
anio (Autor, 2021).

Con --entregado calcula ademas cuanto texto literal se desplazo respecto de la
version que ya se entrego. Ese numero mide el trabajo hecho, NO predice la
similitud: Turnitin compara contra su indice, no contra la version anterior.
Las claves se quitan antes de comparar, porque en el Word entregado ya salen
convertidas en citas.
"""
import argparse
import re
import sys
from collections import Counter

RE_MARCA = re.compile(r"\[(AR[0-9A-F]{8})(?::([^\]\n]{1,40}))?\]|\[FALTA FUENTE\]")


def parrafos(ruta):
    if ruta.lower().endswith(".docx"):
        try:
            from docx import Document
        except ImportError:
            sys.exit("Falta python-docx:  pip install python-docx --break-system-packages")
        return [p.text for p in Document(ruta).paragraphs]
    texto = open(ruta, encoding="utf-8", errors="replace").read()
    return [re.sub(r"\s*\n\s*", " ", p.strip()) for p in re.split(r"\n\s*\n", texto) if p.strip()]


def marcas(t):
    """Lista ordenada de claves con su modificador, y [FALTA FUENTE]."""
    fuera = []
    for m in RE_MARCA.finditer(t):
        if m.group(1):
            fuera.append(m.group(1) + (":" + m.group(2) if m.group(2) else ""))
        else:
            fuera.append("FALTA FUENTE")
    return fuera


def sin_marcas(t):
    return re.sub(r"[ \t]*" + RE_MARCA.pattern, "", t)


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


def comparar_marcas(a, b, cambiados):
    """Claves por parrafo: cada parrafo tocado tiene que salir con las mismas."""
    print("\nClaves de cita [AR...] y [FALTA FUENTE]:")
    total_a = [m for p in a for m in marcas(p)]
    total_b = [m for p in b for m in marcas(p)]
    print(f"  Total: {len(total_a)} -> {len(total_b)}")
    ids = lambda ms: Counter(m.split(":", 1)[0] for m in ms)
    faltan = ids(total_a) - ids(total_b)
    sobran = ids(total_b) - ids(total_a)
    if faltan:
        print(f"  CLAVES PERDIDAS en todo el texto: {sorted(faltan.elements())}")
    if sobran:
        print(f"  CLAVES NUEVAS en todo el texto (inventadas o duplicadas): {sorted(sobran.elements())}")
    avisos = 0
    for i in cambiados:
        ma, mb = marcas(a[i]), marcas(b[i])
        if ma == mb:
            continue
        avisos += 1
        quita_n = lambda ms: [m[:-2] if m.endswith(":n") else m for m in ms]
        if quita_n(ma) == quita_n(mb):
            motivo = "cambio de :n (el nombre del autor entro o salio de la frase?)"
        elif Counter(ma) == Counter(mb):
            motivo = "orden cambiado (cada clave sigue con su afirmacion?)"
        else:
            motivo = (f"faltan {sorted((Counter(ma) - Counter(mb)).elements()) or '-'}, "
                      f"sobran {sorted((Counter(mb) - Counter(ma)).elements()) or '-'}")
        print(f"  Parrafo {i + 1}: [{' | '.join(ma) or '-'}] -> [{' | '.join(mb) or '-'}]  {motivo}")
    if not avisos and not faltan and not sobran:
        print("  Cada parrafo tocado conserva sus claves: ok")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("antes", help=".docx, .txt o .md")
    ap.add_argument("despues", help=".docx, .txt o .md")
    ap.add_argument("--entregado", help="txt con el texto de la version ya entregada")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass

    a, b = parrafos(args.antes), parrafos(args.despues)

    print(f"Parrafos: {len(a)} -> {len(b)}", end="  ")
    if len(a) != len(b):
        print("<<< CAMBIO. Revisar: se fusionaron o partieron parrafos.")
    else:
        print("ok")

    cambiados = [i for i in range(min(len(a), len(b))) if a[i].strip() != b[i].strip()]
    print(f"Parrafos modificados: {len(cambiados)}"
          + (f"  ({', '.join(str(i + 1) for i in cambiados)})" if cambiados else ""))

    txt_a = " ".join(a[i] for i in cambiados)
    txt_b = " ".join(b[i] for i in cambiados)
    limpio_a, limpio_b = sin_marcas(txt_a), sin_marcas(txt_b)

    perdidas = citas(limpio_a) - citas(limpio_b)
    movidas = {c for c in perdidas
               if re.split(r"[,;]", c)[0].strip() in " ".join(autores_narrativos(limpio_b))}
    reales = perdidas - movidas
    print(f"Citas entre parentesis perdidas: {sorted(reales) if reales else 'ninguna'}")
    if movidas:
        print(f"  (convertidas a cita narrativa, no perdidas: {sorted(movidas)})")

    perd_num = cifras(limpio_a) - cifras(limpio_b)
    print(f"Cifras perdidas: {sorted(perd_num) if perd_num else 'ninguna'}")
    if perd_num:
        print("  Revisar una por una: puede ser un dato borrado o un numero escrito en letra.")

    palabras_a = len(re.findall(r"\b\w+\b", limpio_a))
    palabras_b = len(re.findall(r"\b\w+\b", limpio_b))
    print(f"Palabras en los tramos tocados: {palabras_a} -> {palabras_b}")

    comparar_marcas(a, b, cambiados)

    if args.entregado:
        ref = re.sub(r"\s+", " ", sin_marcas(open(args.entregado, encoding="utf-8", errors="replace").read()))
        vs = ventanas(limpio_b)
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
