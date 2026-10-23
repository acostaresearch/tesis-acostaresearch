"""Vuelca un Word (o PDF) a texto con el número de cada párrafo y hace el chequeo mecánico.

    python leer.py <archivo.docx|pdf> <salida.txt>

El .txt trae «¶n [estilo] texto» y las tablas como «T<n> f<fila> | celda | celda». Esos números son los
que usa aplicar.py. Por pantalla: secciones con sus palabras y párrafos sin cita, huecos sin completar,
y el cruce entre lo citado en el texto y la lista de referencias.
"""
import re
import sys
from pathlib import Path

from comun import bloques, con_estilos, es_titulo, norm, texto_pdf

ent, sal = Path(sys.argv[1]), sys.argv[2]
if ent.suffix.lower() == ".pdf":
    t = texto_pdf(ent)
    open(sal, "w", encoding="utf-8").write(t)
    print(f"PDF: {len(t.split())} palabras → {sal}. El chequeo mecánico solo se hace con Word.")
    if len(t.split()) < 150:
        print("Casi no trae texto: es un escaneado. Leerlo como imagen con Read (pages=…).")
    sys.exit()

d, B = bloques(ent)
SOLO = con_estilos(d)
lin, secs, refs, cuerpo = [], [], [], []
zona = "cuerpo"
act = None
AP = r"[A-ZÁÉÍÓÚÑ][\wáéíóúñüç'’-]+"
CITA = r"\(\s*[^()]*\b(?:19|20)\d{2}[a-z]?\b[^()]*\)|\[\d+(?:[-,–]\s*\d+)*\]"


def seccion(titulo, nivel):
    return {"titulo": titulo, "nivel": nivel, "pal": 0, "parr": 0, "sin": [], "tablas": 0, "zona": zona}


for tipo, i, o in B:
    if tipo == "t":
        for f, fila in enumerate(o.rows):
            vistas, celdas = set(), []
            for c in fila.cells:
                if c._tc in vistas:
                    continue
                vistas.add(c._tc)
                celdas.append(" ".join(p.text for p in c.paragraphs).strip())
            lin.append(f"T{i} f{f} | " + " | ".join(celdas))
        if act:
            act["tablas"] += 1
        continue
    t = o.text.strip()
    if not t:
        continue
    niv = es_titulo(o, SOLO)
    lin.append(f"¶{i} [{o.style.name if o.style is not None else "sin estilo"}] {t}")
    if niv:
        n = norm(t)
        if re.search(r"\breferencias\b|\bbibliografia\b", n) and len(t.split()) <= 5:
            zona = "refs"
        elif re.search(r"\banexos?\b|\bapendices?\b", n) and len(t.split()) <= 6 and zona != "cuerpo":
            zona = "anexos"
        act = seccion(t, niv)
        secs.append(act)
        continue
    if zona == "refs":
        refs.append((i, t))
        continue
    if act is None:
        act = seccion("(antes del primer título)", 1)
        secs.append(act)
    act["pal"] += len(t.split())
    act["parr"] += 1
    if zona == "cuerpo":
        cuerpo.append((i, t))
        if len(t.split()) >= 40 and not re.search(CITA, t):
            act["sin"].append(i)

open(sal, "w", encoding="utf-8").write("\n".join(lin))
total = sum(len(t.split()) for _, t in cuerpo)
print(f"{ent.name}\nCuerpo: {total} palabras · {len(cuerpo)} párrafos · {len(d.tables)} tablas · "
      f"{len(d.inline_shapes)} imágenes · {len(refs)} referencias → {sal}\n")

print("SECCIONES (palabras · párrafos · párrafos de 40+ palabras sin ninguna cita)")
for s in secs:
    if s["zona"] != "cuerpo" and s["nivel"] > 2:
        continue
    marca = f" · sin cita: ¶{', ¶'.join(map(str, s['sin']))}" if s["sin"] else ""
    print(f"  {'  ' * (s['nivel'] - 1)}{s['titulo'][:70]} · {s['pal']} · {s['parr']}{marca}")
print("  (Una sección en 0 seguida de subtítulos no está vacía; una en 0 sin subtítulos, sí.)")

print("\nHUECOS SIN COMPLETAR")
hue = 0
for l in lin:
    cuerpo_l = re.sub(r"^¶\d+ \[[^\]]*\] ", "", l)
    m = re.findall(r"\[[^\]\d]{0,60}\]|_{5,}|\bXXX+\b|\bcompletar\b|\bpor definir\b|\bLorem\b", cuerpo_l, re.I)
    m = [x for x in m if not re.fullmatch(r"\[(Tesis|Trabajo|Art[ií]culo|Archivo|Video)[^\]]*\]", x, re.I)]
    if m:
        hue += 1
        print(f"  {l.split(' ', 1)[0]} {', '.join(sorted(set(m)))[:110]}")
if not hue:
    print("  ninguno")

print("\nCITAS ↔ REFERENCIAS (solo vale para normas autor-año: APA, ISO 690 autor-fecha)")
if not refs:
    sys.exit("  No encontré la lista de referencias (¿título distinto de «Referencias» o «Bibliografía»?).")
R = []
for i, r in refs:
    m = re.search(r"\(((?:19|20)\d{2})[a-z]?\b[^)]*\)", r) or re.search(r"\b((?:19|20)\d{2})\b", r)
    anio = m.group(1) if m else "?"
    autores = r[:m.start()] if m else r[:80]
    R.append({"i": i, "anio": anio, "autores": norm(autores), "txt": r, "citada": False})
todo = " ".join(t for _, t in cuerpo)
if re.search(r"\[\d+\]|\(\d{1,3}\)", todo) and not re.search(rf"{AP}[^()]{{0,40}}\((?:19|20)\d{{2}}", todo):
    sys.exit("  El texto cita con números (Vancouver/IEEE): el cruce autor-año no aplica; se revisa a mano.")
citas = set()
patron = (rf"({AP})(?:\s+(?:de|del|la|da|dos|van|von)\s+{AP}|\s+{AP})*"
          rf"(?:\s+et al\.?|\s+(?:y|&|e|and)\s+{AP}(?:\s+{AP})?)?,?\s+\(((?:19|20)\d{{2}})")
for m in re.finditer(patron, todo):
    citas.add((norm(m.group(0).split("(")[0]), m.group(2)))
for par in re.findall(r"\(([^()]*(?:19|20)\d{2}[^()]*)\)", todo):
    for trozo in par.split(";"):
        m = re.search(rf"({AP}[^;]*?),?\s+((?:19|20)\d{{2}})", trozo)
        if m:
            citas.add((norm(m.group(1)), m.group(2)))
MUDAS = {"et", "al", "and", "del", "los", "las", "segun", "como", "para", "por", "entre", "desde", "con", "que",
         "de", "la", "da", "el", "en", "un", "se", "su", "lo", "es", "no", "si", "ya", "do"}
sin_ref = []
for aut, anio in sorted(citas):
    pal = [w for w in aut.split() if len(w) > 1 and w not in MUDAS]  # apellidos de dos letras: Wu, Li, Xu
    ok = False
    for x in R:
        if x["anio"] == anio and any(w in x["autores"].split() for w in pal):
            x["citada"] = ok = True
    if not ok and pal:
        sin_ref.append(f"{aut} ({anio})")
print("  Citadas en el texto que NO están en la lista: " + ("; ".join(sin_ref) if sin_ref else "ninguna"))
nc = [f"¶{x['i']} {x['txt'][:60]}…" for x in R if not x["citada"]]
print("  En la lista y NO citadas en el texto: " + ("\n    " + "\n    ".join(nc) if nc else "ninguna"))
print("  (Revisar a ojo lo que salga: apellidos compuestos e instituciones pueden dar falsos avisos.)")
