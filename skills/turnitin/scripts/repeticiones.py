#!/usr/bin/env python3
"""Busca los moldes que se repiten ENTRE párrafos en todo el documento.

Uso:
  python repeticiones.py doc.docx                 todo el cuerpo (párrafos de 25+ palabras)
  python repeticiones.py doc.docx --min 3         avisa desde 3 apariciones (por defecto)
  python repeticiones.py doc.docx --desde 27 --hasta 180

Existe por 10-Roy (14-oct-2026): ocho rondas locales en «*%», con cuatro agentes
que reescribían cada uno su tramo, y ninguno veía que «Con esa clasificación»,
«Con ese criterio», «Con esa pauta»… abrían párrafos en los cuatro tramos. El
humanizador del conector, con dos pasadas de «verifica todo nuevamente a ver si
hay patrones IA y quítalos», cazó justo estas repeticiones y dio 0 % en una ronda.

No reescribe nada: lista cada molde con los párrafos donde aparece, para variar
las apariciones que sobran (se deja una o dos, no se borran todas).
"""
import argparse
import re
import sys
from collections import defaultdict

import docx

sys.stdout.reconfigure(encoding='utf-8')

# Molde -> regex (se busca en todo el párrafo, sin distinguir mayúsculas)
MOLDES = {
    "«Lo que … es/será» (oración partida)": r"\blo que [^.]{0,60}?\b(es|será|son|fue|hará|pide|interesa)\b",
    "«Se trata de»": r"\bse trata de\b",
    "«De ahí»": r"\bde ahí\b",
    "«Ahora bien»": r"\bahora bien\b",
    "«Por ese/esa motivo/razón/…»": r"\bpor (ese|esa|este|esta) (motivo|razón|diferencia|causa)\b",
    "«de modo que / de manera que»": r"\bde (modo|manera) que\b",
    "«entonces»": r"\bentonces\b",
    "«ayuda a / servirá para / permite»": r"\b(ayuda a|ayudará a|servirá para|sirve para|permitirá)\b",
    "«No es X, sino Y»": r"\bno (es|son|se trata de) [^.]{0,60}?, sino\b",
    "Lista anunciada con número y dos puntos («tres ejes: …»)": r"\b(dos|tres|cuatro|cinco|seis) [a-záéíóúñ]+( [a-záéíóúñ]+)?:\s",
    "«Este/En este eje, criterio, …»": r"(^|\. )(en )?(este|esta|ese|esa) (eje|criterio|pauta|subcategoría|categoría|dimensión|enfoque)\b",
    "«Con este trabajo / Con ese …» de cierre": r"(^|\. )con (este|esta|ese|esa|estos|esas|ellas|ellos) \w+",
}

ART = {"el", "la", "los", "las", "un", "una", "en", "con", "por", "para", "de", "del", "al", "a", "se", "lo"}


def cuerpo(doc, desde, hasta):
    for i, p in enumerate(doc.paragraphs):
        if i < desde or (hasta is not None and i > hasta):
            continue
        t = p.text.strip()
        if len(t.split()) < 25:
            continue
        estilo = (p.style.name or "").lower()
        if "heading" in estilo or "título" in estilo or "caption" in estilo:
            continue
        yield i, t


def oraciones(t):
    t = t.replace("et al.", "et al\x00")
    return [o.replace("\x00", ".") for o in re.split(r"(?<=[.?!])\s+", t) if o.strip()]


def arranque(o, n=2):
    w = re.findall(r"[\wáéíóúñü]+", o.lower())
    if not w:
        return ""
    # «Con esa …», «En este …»: si empieza con preposición/artículo, se toman dos palabras
    return " ".join(w[:n]) if w[0] in ART else w[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("--min", type=int, default=3)
    ap.add_argument("--desde", type=int, default=0)
    ap.add_argument("--hasta", type=int)
    a = ap.parse_args()

    doc = docx.Document(a.docx)
    pars = list(cuerpo(doc, a.desde, a.hasta))
    print(f"{len(pars)} párrafos de prosa revisados\n")

    hallado = False

    aper = defaultdict(list)
    for i, t in pars:
        aper[arranque(t)].append(i)
    rep = {k: v for k, v in aper.items() if k and len(v) >= a.min}
    if rep:
        hallado = True
        print("APERTURAS DE PÁRRAFO REPETIDAS")
        for k, v in sorted(rep.items(), key=lambda x: -len(x[1])):
            print(f"  «{k.capitalize()}…» ×{len(v)}: ¶" + ", ¶".join(map(str, v)))
        print()

    oaper = defaultdict(list)
    for i, t in pars:
        for o in oraciones(t)[1:]:
            k = arranque(o, 1)
            if k in {"también", "además", "así", "esto", "eso", "ello", "pero", "sin"}:
                oaper[k].append(i)
    rep = {k: v for k, v in oaper.items() if len(v) >= a.min + 1}
    if rep:
        hallado = True
        print("ORACIONES QUE ARRANCAN IGUAL")
        for k, v in sorted(rep.items(), key=lambda x: -len(x[1])):
            print(f"  «{k.capitalize()}…» ×{len(v)}: ¶" + ", ¶".join(map(str, sorted(set(v)))))
        print()

    print("MOLDES FIJOS")
    for nombre, rx in MOLDES.items():
        donde = [i for i, t in pars for _ in re.finditer(rx, t, re.I)]
        if len(donde) >= a.min:
            hallado = True
            print(f"  {nombre} ×{len(donde)}: ¶" + ", ¶".join(map(str, sorted(set(donde)))))
    if not hallado:
        print("  Nada se repite tanto. Ya no quedan moldes entre párrafos.")


if __name__ == "__main__":
    main()
