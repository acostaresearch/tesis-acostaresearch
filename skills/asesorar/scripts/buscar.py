"""Busca artículos reales para reforzar antecedentes y marco teórico. Solo devuelve lo que existe.

    python buscar.py "shared book reading oral language preschool" [--desde 2021] [--idioma en|es|pt]
                     [--n 15] [--pais PE] [--scopus]
    python buscar.py --doi 10.3389/flang.2025.1540562        ficha completa de un DOI

Por defecto usa OpenAlex (trae resumen). --scopus busca en Scopus con ELSEVIER_API_KEY del .env local
(TITLE-ABS-KEY; sin resumen, sirve para saber qué está indexado). Se cita solo lo que se leyó en el
resumen: si el resumen no dice el dato, el dato no se escribe.
"""
import sys
from urllib.parse import quote

from comun import clave_env, http_json

a = sys.argv[1:]
op = lambda n, d=None: a[a.index(n) + 1] if n in a else d


def resumen(inv):
    if not inv:
        return ""
    pos = sorted((p, w) for w, ps in inv.items() for p in ps)
    return " ".join(w for _, w in pos)


def ficha(w, largo=700):
    aut = [x["author"]["display_name"] for x in w.get("authorships", [])]
    paises = sorted({c for x in w.get("authorships", []) for c in x.get("countries", [])})
    src = ((w.get("primary_location") or {}).get("source") or {})
    b = w.get("biblio") or {}
    print(f"- {w.get('title')}")
    print(f"  {'; '.join(aut[:8])}{' …' if len(aut) > 8 else ''} ({w.get('publication_year')})")
    print(f"  {src.get('display_name', 's/revista')} · vol. {b.get('volume') or '-'}({b.get('issue') or '-'}), "
          f"pp. {b.get('first_page') or '-'}-{b.get('last_page') or '-'} · {w.get('type')} · idioma {w.get('language')} · "
          f"países {','.join(paises) or '?'} · citas {w.get('cited_by_count')}")
    print(f"  DOI: {(w.get('doi') or 'sin DOI').replace('https://doi.org/', '')}")
    r = resumen(w.get("abstract_inverted_index"))
    print(f"  Resumen: {r[:largo] + ('…' if len(r) > largo else '') if r else 'NO DISPONIBLE (no citar datos de esta fuente sin leerla)'}\n")


if "--doi" in a:
    w = http_json("https://api.openalex.org/works/https://doi.org/" + quote(op("--doi"), safe="/"))
    if "_error" in w:
        sys.exit(f"OpenAlex no lo tiene ({w['_error']}). Probar en Crossref con referencias.py.")
    ficha(w, 4000)
    sys.exit()

q = a[0]
n = int(op("--n", 15))
if "--scopus" in a:
    clave = clave_env("ELSEVIER_API_KEY")
    if not clave:
        sys.exit("No hay ELSEVIER_API_KEY en backend/.env.")
    consulta = f"TITLE-ABS-KEY({q})" + (f" AND PUBYEAR > {int(op('--desde')) - 1}" if op("--desde") else "")
    if op("--pais"):
        consulta += f" AND AFFILCOUNTRY({op('--pais')})"
    j = http_json(f"https://api.elsevier.com/content/search/scopus?count={min(n, 25)}&sort=-citedby-count&query=" + quote(consulta),
                  {"X-ELS-APIKey": clave, "Accept": "application/json"})
    if "_error" in j:
        sys.exit(f"Scopus no respondió: {j['_error']}")
    res = j["search-results"]
    print(f"Scopus · {consulta} · {res.get('opensearch:totalResults')} resultados\n")
    for e in res.get("entry", []):
        if e.get("error"):
            continue
        print(f"- {e.get('dc:title')}\n  {e.get('dc:creator')} et al. ({(e.get('prism:coverDate') or '')[:4]}) · "
              f"{e.get('prism:publicationName')} · citas {e.get('citedby-count')}\n  DOI: {e.get('prism:doi', 'sin DOI')}\n")
    print("Scopus da un solo autor y sin resumen: completar cada ficha con  buscar.py --doi <DOI>")
    sys.exit()

filtros = ["type:article|review"]
if op("--desde"):
    filtros.append(f"from_publication_date:{op('--desde')}-01-01")
if op("--idioma"):
    filtros.append(f"language:{op('--idioma')}")
if op("--pais"):
    filtros.append(f"authorships.countries:{op('--pais')}")
j = http_json(f"https://api.openalex.org/works?per-page={n}&search={quote(q)}&filter={','.join(filtros)}")
if "_error" in j:
    sys.exit(f"OpenAlex no respondió: {j['_error']} (el cupo sin clave es por día; probar --scopus)")
print(f"OpenAlex · «{q}» · {j.get('meta', {}).get('count')} resultados · se muestran {len(j.get('results', []))}\n")
for w in j.get("results", []):
    ficha(w)
