#!/usr/bin/env python3
"""Diagrama de flujo PRISMA 2020 (nuevas revisiones) en PNG, a partir de conteos.

Uso:
  python3 prisma_flujo.py --out figura_prisma.png \
      --bases "Scopus=312;Web of Science=205" --otros 0 \
      --duplicados 140 --automatizados 0 --otros-eliminados 0 \
      --cribados 377 --excluidos-cribado 290 \
      --buscados 87 --no-recuperados 4 \
      --evaluados 83 --excluidos-texto "Población distinta=21;Sin datos de resultado=14;Idioma=3" \
      --incluidos 45 [--informes 45] [--idioma en]

Cada número lo da el investigador (o el registro del cribado). El script
COMPRUEBA LA ARITMÉTICA y se niega a dibujar si no cuadra: así el diagrama
nunca contradice el texto. Requiere matplotlib.
"""
import argparse
import sys
import textwrap

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch
except ImportError:
    sys.exit("Falta matplotlib (pip install matplotlib). Alternativa: pedir el diagrama en https://estech.shinyapps.io/prisma_flowdiagram/")

T = {
    "es": dict(id="Identificación", cr="Cribado", inc="Incluidos",
               reg="Registros identificados de:", dup="Registros eliminados antes del cribado:",
               dup1="Duplicados", aut="Marcados por herramientas automáticas", otr="Eliminados por otras razones",
               crib="Registros cribados", exc="Registros excluidos", busc="Informes buscados para recuperar",
               norec="Informes no recuperados", ev="Informes evaluados para elegibilidad",
               exct="Informes excluidos:", incl="Estudios incluidos en la revisión", infs="Informes de los estudios incluidos",
               otros="Otras fuentes"),
    "en": dict(id="Identification", cr="Screening", inc="Included",
               reg="Records identified from:", dup="Records removed before screening:",
               dup1="Duplicate records", aut="Records marked as ineligible by automation tools",
               otr="Records removed for other reasons", crib="Records screened", exc="Records excluded",
               busc="Reports sought for retrieval", norec="Reports not retrieved",
               ev="Reports assessed for eligibility", exct="Reports excluded:",
               incl="Studies included in review", infs="Reports of included studies", otros="Other sources"),
}


def pares(s):
    out = []
    for trozo in filter(None, (s or "").split(";")):
        k, v = trozo.rsplit("=", 1)
        out.append((k.strip(), int(v)))
    return out


def caja(ax, x, y, w, h, texto, gris=False):
    if not gris:
        ancho = int(w * 10.5)
        texto = "\n".join(textwrap.fill(l, ancho, subsequent_indent="    " if l.startswith("  ") else "")
                          for l in texto.split("\n"))
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0", fc="#E8E8E8" if gris else "white",
                                ec="black", lw=1))
    ax.text(x + w / 2 if gris else x + 0.12, y + h / 2, texto, ha="center" if gris else "left",
            va="center", fontsize=8, family="serif", rotation=90 if gris else 0, wrap=True)


def flecha(ax, x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", lw=1, color="black"))


def bibliometrico(a):
    t = T[a.idioma]
    bases = pares(a.bases)
    excl = pares(a.excluidos_texto)
    ident = sum(n for _, n in bases) + a.otros
    elim = a.duplicados + a.automatizados + a.otros_eliminados
    n_excl = a.excluidos_cribado or sum(n for _, n in excl)
    errores = []
    if ident - elim != a.cribados:
        errores.append(f"identificados ({ident}) − eliminados ({elim}) = {ident - elim}, pero cribados = {a.cribados}")
    if a.cribados - n_excl != a.incluidos:
        errores.append(f"cribados − excluidos por filtros = {a.cribados - n_excl}, pero incluidos = {a.incluidos}")
    if errores:
        print("LOS CONTEOS NO CUADRAN. No se dibuja el diagrama:")
        for e in errores:
            print("  ✗", e)
        sys.exit(1)
    es = a.idioma == "es"
    fig, ax = plt.subplots(figsize=(8.3, 6.4))
    ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis("off")
    W, XL, XR, WR = 4.3, 0.9, 5.7, 4.0
    caja(ax, 0, 5.4, 0.6, 2.4, t["id"], True)
    caja(ax, 0, 2.7, 0.6, 2.4, t["cr"], True)
    caja(ax, 0, 0.2, 0.6, 2.2, t["inc"], True)
    lineas = "\n".join(f"  {k} (n = {n})" for k, n in bases)
    caja(ax, XL, 5.7, W, 1.9, f"{t['reg']}\n{lineas}")
    caja(ax, XR, 5.7, WR, 1.9, f"{t['dup']}\n  {t['dup1']} (n = {a.duplicados})\n  {t['otr']} (n = {a.otros_eliminados})")
    flecha(ax, XL + W, 6.65, XR, 6.65)
    txt_ex = ("Excluidos por filtros de metadatos" if es else "Excluded by metadata filters") + \
        (f" (n = {n_excl})" if not excl else ":" + "".join(f"\n  {k} (n = {n})" for k, n in excl))
    caja(ax, XL, 3.2, W, 1.4, f"{t['crib']}\n(n = {a.cribados})")
    caja(ax, XR, 3.0, WR, 1.8, txt_ex)
    flecha(ax, XL + W / 2, 5.7, XL + W / 2, 4.6); flecha(ax, XL + W, 3.9, XR, 3.9)
    fin = "Documentos incluidos en el análisis bibliométrico" if es else "Documents included in the bibliometric analysis"
    caja(ax, XL, 0.6, W, 1.4, f"{fin}\n(n = {a.incluidos})")
    flecha(ax, XL + W / 2, 3.2, XL + W / 2, 2.0)
    fig.savefig(a.out, dpi=200, bbox_inches="tight")
    print(f"ok: {a.out} · identificados {ident} → incluidos {a.incluidos} (flujo bibliométrico)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--bases", required=True, help='"Scopus=312;Web of Science=205"')
    ap.add_argument("--otros", type=int, default=0, help="registros de otras fuentes (registros, webs)")
    for k in ("duplicados", "automatizados", "otros-eliminados", "cribados", "excluidos-cribado", "buscados",
              "no-recuperados", "evaluados", "incluidos"):
        ap.add_argument(f"--{k}", type=int, default=0)
    ap.add_argument("--excluidos-texto", default="", help='"Razón=n;Razón=n"')
    ap.add_argument("--informes", type=int)
    ap.add_argument("--idioma", choices=["es", "en"], default="es")
    ap.add_argument("--bibliometrico", action="store_true",
                    help="flujo sin lectura a texto completo: identificados → duplicados → filtros por metadatos → incluidos")
    a = ap.parse_args()
    if a.bibliometrico:
        return bibliometrico(a)
    t = T[a.idioma]
    bases = pares(a.bases)
    excl = pares(a.excluidos_texto)
    ident = sum(n for _, n in bases) + a.otros
    elim = a.duplicados + a.automatizados + a.otros_eliminados
    errores = []
    if ident - elim != a.cribados:
        errores.append(f"identificados ({ident}) − eliminados ({elim}) = {ident - elim}, pero cribados = {a.cribados}")
    if a.cribados - a.excluidos_cribado != a.buscados:
        errores.append(f"cribados − excluidos = {a.cribados - a.excluidos_cribado}, pero buscados = {a.buscados}")
    if a.buscados - a.no_recuperados != a.evaluados:
        errores.append(f"buscados − no recuperados = {a.buscados - a.no_recuperados}, pero evaluados = {a.evaluados}")
    # los informes evaluados se restan a informes, no a estudios (un estudio puede tener varios informes)
    inf_ok = a.informes if a.informes is not None else a.incluidos
    if a.evaluados - sum(n for _, n in excl) != inf_ok:
        errores.append(f"evaluados − excluidos a texto completo = {a.evaluados - sum(n for _, n in excl)}, "
                       f"pero informes incluidos = {inf_ok}")
    if a.informes is not None and a.incluidos > a.informes:
        errores.append(f"hay más estudios ({a.incluidos}) que informes ({a.informes})")
    if errores:
        print("LOS CONTEOS NO CUADRAN. No se dibuja el diagrama:")
        for e in errores:
            print("  ✗", e)
        sys.exit(1)

    fig, ax = plt.subplots(figsize=(8.3, 9.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 11); ax.axis("off")
    W, H, XL, XR, WR = 4.3, 1.15, 0.9, 5.7, 4.0
    caja(ax, 0, 8.2, 0.6, 2.6, t["id"], True)
    caja(ax, 0, 2.6, 0.6, 5.4, t["cr"], True)
    caja(ax, 0, 0.2, 0.6, 2.2, t["inc"], True)
    lineas = "\n".join(f"  {k} (n = {n})" for k, n in bases)
    if a.otros:
        lineas += f"\n  {t['otros']} (n = {a.otros})"
    caja(ax, XL, 8.6, W, 1.9, f"{t['reg']}\n{lineas}")
    caja(ax, XR, 8.6, WR, 1.9, f"{t['dup']}\n  {t['dup1']} (n = {a.duplicados})\n  {t['aut']}\n  (n = {a.automatizados})\n"
                                f"  {t['otr']} (n = {a.otros_eliminados})")
    flecha(ax, XL + W, 9.55, XR, 9.55)
    caja(ax, XL, 6.7, W, H, f"{t['crib']}\n(n = {a.cribados})")
    caja(ax, XR, 6.7, WR, H, f"{t['exc']}\n(n = {a.excluidos_cribado})")
    flecha(ax, XL + W / 2, 8.6, XL + W / 2, 6.7 + H); flecha(ax, XL + W, 7.27, XR, 7.27)
    caja(ax, XL, 5.0, W, H, f"{t['busc']}\n(n = {a.buscados})")
    caja(ax, XR, 5.0, WR, H, f"{t['norec']}\n(n = {a.no_recuperados})")
    flecha(ax, XL + W / 2, 6.7, XL + W / 2, 5.0 + H); flecha(ax, XL + W, 5.57, XR, 5.57)
    caja(ax, XL, 3.1, W, H, f"{t['ev']}\n(n = {a.evaluados})")
    txt = t["exct"] + "".join(f"\n  {k} (n = {n})" for k, n in excl)
    caja(ax, XR, 2.7, WR, 1.9, txt)
    flecha(ax, XL + W / 2, 5.0, XL + W / 2, 3.1 + H); flecha(ax, XL + W, 3.67, XR, 3.67)
    inf = a.informes if a.informes is not None else a.incluidos
    caja(ax, XL, 0.6, W, 1.4, f"{t['incl']}\n(n = {a.incluidos})\n{t['infs']}\n(n = {inf})")
    flecha(ax, XL + W / 2, 3.1, XL + W / 2, 2.0)
    fig.savefig(a.out, dpi=200, bbox_inches="tight")
    print(f"ok: {a.out} · identificados {ident} → incluidos {a.incluidos}")


if __name__ == "__main__":
    main()
