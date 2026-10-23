"""Comprueba la lista de referencias de un Word: que cada DOI exista y sea de esa fuente, y los
porcentajes que suelen pedir las guías (artículos, idioma extranjero, antigüedad).

    python referencias.py <archivo.docx> [--scopus] [--anios 5]

--scopus pregunta además a Scopus si cada DOI está indexado (usa ELSEVIER_API_KEY del .env local).
No inventa nada: lo que no tiene DOI se clasifica por cómo está escrito y se marca para mirar a mano.
"""
import re
import sys
from datetime import date
from difflib import SequenceMatcher
from urllib.parse import quote

from comun import bloques, con_estilos, clave_env, es_titulo, http_json, norm

arg = sys.argv[1:]
docx = arg[0]
con_scopus = "--scopus" in arg
anios = int(arg[arg.index("--anios") + 1]) if "--anios" in arg else 5

_d, B = bloques(docx)
SOLO = con_estilos(_d)
refs, dentro = [], False
for tipo, i, o in B:
    if tipo != "p" or not o.text.strip():
        continue
    t = o.text.strip()
    if es_titulo(o, SOLO):
        n = norm(t)
        if re.search(r"\breferencias\b|\bbibliografia\b", n) and len(t.split()) <= 5:
            dentro = True
            continue
        if dentro:
            break
    elif dentro:
        refs.append((i, t))
if not refs:
    sys.exit("No encontré la lista de referencias.")

EN = {"the", "of", "and", "in", "for", "with", "on", "to", "from", "among", "between", "study", "review"}
ES = {"el", "la", "los", "las", "de", "del", "en", "para", "con", "una", "un", "y", "sobre", "entre"}
PT = {"da", "do", "das", "dos", "em", "na", "no", "uma", "um", "para", "com", "e", "sobre", "ão", "não"}


def idioma(titulo):
    w = norm(titulo).split()
    p = {"en": sum(x in EN for x in w), "es": sum(x in ES for x in w), "pt": sum(x in PT for x in w)}
    if re.search(r"ção|ções|ã|õ", titulo.lower()):
        p["pt"] += 3
    if re.search(r"[ñ¿¡]|ción", titulo.lower()):
        p["es"] += 3
    return max(p, key=p.get) if max(p.values()) else "?"


def nombre(a):
    return ", ".join(x for x in (a.get("family") or a.get("name"), a.get("given")) if x)


def tipo_por_texto(r):
    n = norm(r)
    if re.search(r"\[tesis|\[trabajo de|tesis de (licenciatura|maestria|doctorado|pregrado)|repositorio", n):
        return "tesis"
    if re.search(r",\s*\d+\s*\(\s*[\w\s.º°-]+\)\s*,\s*[\de]|,\s*\d+\s*,\s*(art[ií]culo\s*)?[\de]", r, re.I):
        return "artículo"
    if re.search(r"\(\d+\.ª ed\.\)|\bed\.\)|editorial|mcgraw|pearson|ediciones", n):
        return "libro"
    if "http" in r:
        return "web"
    return "?"


clave = clave_env("ELSEVIER_API_KEY") if con_scopus else None
if con_scopus and not clave:
    print("AVISO: no hay ELSEVIER_API_KEY en backend/.env; se omite la comprobación en Scopus.\n")

filas, hoy = [], date.today().year
for i, r in refs:
    m = re.search(r"\(((?:19|20)\d{2})", r) or re.search(r"\b((?:19|20)\d{2})\b", r)
    anio = int(m.group(1)) if m else None
    doi = re.search(r"10\.\d{4,9}/[^\s\"<>]+", r)
    f = {"i": i, "anio": anio, "tipo": tipo_por_texto(r), "idioma": "?", "nota": [], "txt": r, "scopus": ""}
    titulo = r[m.end():] if m else r
    titulo = re.sub(r"^[a-z]?\)?\.?\s*", "", titulo).split(". ")[0]
    f["idioma"] = idioma(titulo)
    if doi:
        d = doi.group(0).rstrip(".,;)")
        j = http_json("https://api.crossref.org/works/" + quote(d, safe="/"))
        if "_error" in j:
            j2 = http_json("https://doi.org/api/handles/" + quote(d, safe="/"))
            if j2.get("responseCode") == 1:
                f["nota"].append("DOI existe, pero no está en Crossref: verificar a mano título y autores")
            else:
                f["nota"].append(f"DOI NO RESUELVE ({d})")
        else:
            msg = j["message"]
            tit = (msg.get("title") or [""])[0]
            f["tipo"] = {"journal-article": "artículo", "book": "libro", "book-chapter": "capítulo",
                         "proceedings-article": "congreso", "dissertation": "tesis"}.get(msg.get("type"), msg.get("type") or f["tipo"])
            f["idioma"] = (msg.get("language") or f["idioma"] or idioma(tit))[:2]
            if tit and norm(tit)[:25] not in norm(r) and SequenceMatcher(None, norm(tit), norm(titulo)).ratio() < 0.6:
                if idioma(tit) != idioma(titulo):
                    f["nota"].append(f"Crossref lo tiene con el título en otro idioma («{tit[:60]}»): mirar cuál es el original")
                else:
                    f["nota"].append(f"EL DOI ES DE OTRA FUENTE: «{tit[:70]}»")
            aut = msg.get("author") or []
            if aut:
                primero = norm(aut[0].get("family") or aut[0].get("name") or "")
                if primero and not any(w in norm(r[:120]).split() for w in primero.split() if len(w) > 3):
                    f["nota"].append(f"primer autor según Crossref: {nombre(aut[0])}")
                if re.search(r"\[iniciales\]|et al\.", r[:m.start() if m else 80]) or r.count(",") < 2:
                    f["nota"].append("autores completos: " + "; ".join(nombre(a) for a in aut[:8]))
            ac = (msg.get("issued", {}).get("date-parts") or [[None]])[0][0]
            if ac and anio and ac != anio:
                f["nota"].append(f"año según Crossref: {ac}")
        if clave:
            s = http_json("https://api.elsevier.com/content/search/scopus?count=1&query=" + quote(f"DOI({d})"),
                          {"X-ELS-APIKey": clave, "Accept": "application/json"})
            n = s.get("search-results", {}).get("opensearch:totalResults")
            f["scopus"] = "?" if n is None else ("Scopus" if n != "0" else "no Scopus")
    elif f["tipo"] == "artículo":
        f["nota"].append("artículo sin DOI: buscarlo y añadirlo")
    filas.append(f)

for f in filas:
    viejo = " · ANTIGUA" if f["anio"] and hoy - f["anio"] > anios else ""
    print(f"¶{f['i']} · {f['tipo']} · {f['idioma']} · {f['anio'] or 's/f'}{viejo}"
          f"{' · ' + f['scopus'] if f['scopus'] else ''} · {f['txt'][:70]}…")
    for n in f["nota"]:
        print(f"      → {n}")

n = len(filas)
art = sum(f["tipo"] in ("artículo", "congreso") for f in filas)
ext = sum(f["idioma"] not in ("es", "?") for f in filas)
rec = sum(bool(f["anio"]) and hoy - f["anio"] <= anios for f in filas)
pct = lambda x: f"{x} de {n} ({x * 100 // n} %)"
print(f"\nRESUMEN · {n} referencias")
print(f"  Artículos científicos: {pct(art)}")
print(f"  En idioma extranjero:  {pct(ext)}")
print(f"  De los últimos {anios} años: {pct(rec)}")
if clave:
    print(f"  Indexadas en Scopus:   {pct(sum(f['scopus'] == 'Scopus' for f in filas))}")
tipos = {}
for f in filas:
    tipos[f["tipo"]] = tipos.get(f["tipo"], 0) + 1
print("  Por tipo: " + ", ".join(f"{k} {v}" for k, v in sorted(tipos.items(), key=lambda x: -x[1])))
print("\nComparar estos porcentajes con lo que pida la guía. Para llegar a un mínimo de P % de artículos con N\n"
      "referencias hacen falta x más tales que (artículos + x) / (N + x) ≥ P.")
