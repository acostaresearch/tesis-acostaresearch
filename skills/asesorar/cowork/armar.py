"""Arma asesorar.zip para Claude Cowork a partir de esta skill local.

    python armar.py                      deja el zip en Descargas
    python armar.py <salida.zip>

La skill de Cowork trabaja sobre la carpeta «asesoria» (C:\\Users\\Usuario\\Documents\\asesoria en
Windows; en Cowork, la carpeta conectada con ese nombre) y lleva dentro lo que en local lee de
fuera: las piezas de /turnitin que usa (nombrar, repeticiones, control_cero, voz y referencias) y
las skills del método (skills/<producto>/fuente y _comun). Se vuelve a correr cada vez que cambie
la skill local; la local no se toca.
"""
import re
import sys
import zipfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SKILL = AQUI.parent
TURNITIN = SKILL.parent / "turnitin"
sys.path.insert(0, str(SKILL / "scripts"))
from rutas import METODO  # noqa: E402
SALIDA = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "Downloads" / "asesorar.zip"
TEXTO = {".md", ".py", ".txt", ".R", ".js", ".json", ".csv"}

for _s in (sys.stdout, sys.stderr):
    _s.reconfigure(encoding="utf-8")


def limpio(b):
    """Sin BOM y con saltos de línea de Unix: Cowork rechaza un SKILL.md que no empieza por «---»."""
    if b.startswith(b"\xef\xbb\xbf"):
        b = b[3:]
    return b.replace(b"\r\n", b"\n")


def juntar(d):
    """Una skill del método en un solo texto: primero su SKILL.md, después cada archivo con su ruta."""
    fs = sorted((f for f in d.rglob("*") if f.is_file() and "__pycache__" not in f.parts),
                key=lambda f: (f.name != "SKILL.md", f.relative_to(d).as_posix()))
    partes = [f"<!-- Skill del método «{d.name}», con todos sus archivos juntos. -->\n"]
    for f in fs:
        t = limpio(f.read_bytes()).decode("utf-8", errors="replace")
        rel = f.relative_to(d).as_posix()
        if f.suffix == ".md":
            partes.append(f"\n\n<!-- ===== archivo: {rel} ===== -->\n\n{t}")
        else:
            partes.append(f"\n\n<!-- ===== archivo: {rel} ===== -->\n\n````{f.suffix.lstrip('.')}\n{t}\n````")
    return "".join(partes).encode("utf-8")


def cambiar(texto, pares, archivo):
    for viejo, nuevo in pares:
        if viejo not in texto:
            sys.exit(f"{archivo}: ya no aparece «{viejo[:60]}»; ajustar armar.py")
        texto = texto.replace(viejo, nuevo)
    return texto


RAIZ_PY = '''def _raiz():
    """La carpeta «asesoria»: ASESORIA_RAIZ, la de Documentos o, en Cowork, la carpeta conectada."""
    import os
    if os.environ.get("ASESORIA_RAIZ"):
        return Path(os.environ["ASESORIA_RAIZ"])
    aqui = Path.cwd()
    for c in (aqui, *aqui.parents, Path.home() / "Documents" / "asesoria",
              Path(r"C:\\Users\\Usuario\\Documents\\asesoria")):
        if c.name.lower() == "asesoria" and c.is_dir():
            return c
    for patron in ("asesoria", "*/asesoria", "*/*/asesoria"):
        for base in (aqui, Path.home(), Path("/sessions"), Path("/mnt")):
            try:
                hay = [d for d in base.glob(patron) if d.is_dir()]
            except OSError:
                hay = []
            if hay:
                return hay[0]
    return aqui


RAIZ = _raiz()
REPO = RAIZ'''


def comun_py(t):
    t = cambiar(t, [('from rutas import ASESORAR as RAIZ\n\nREPO = RAIZ.parent', RAIZ_PY)], "comun.py")
    # La clave de Scopus: variable de entorno o .env dentro de la carpeta asesoria.
    return cambiar(t, [('    f = REPO / "backend" / ".env"\n',
                        '    import os\n    if os.environ.get(nombre):\n        return os.environ[nombre]\n'
                        '    f = RAIZ / ".env"\n')], "comun.py")


def nombrar_py(t):
    return cambiar(t, [
        ("sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\n"
         "from rutas import ASESORAR, TURNITIN  # noqa: E402\n"
         "RAICES = [str(TURNITIN), str(ASESORAR)]",
         "sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\n"
         "from comun import RAIZ as _RAIZ  # noqa: E402\n"
         "RAICES = [str(_RAIZ)]"),
        ("asesorar = os.path.basename(os.path.dirname(carp)) == 'tesis-asesorar'",
         "asesorar = os.path.basename(os.path.dirname(carp)).lower() in ('tesis-asesorar', 'asesoria')"),
    ], "nombrar.py")


EN_COWORK = """
## En Cowork (léelo antes que todo lo demás)

Esta copia de la skill corre en Claude Cowork, en una máquina Linux y no en el Windows de
Benicio. Lo que el resto del texto dice de rutas de Windows se traduce así:

- **La raíz de clientes es la carpeta `asesoria`** (en Windows, `C:\\Users\\Usuario\\Documents\\asesoria`).
  Cowork la monta con otra ruta: los scripts la encuentran solos (`python <skill>/scripts/estado.py`
  dice dónde la ve en su primera línea). Si no aparece, se le pide a Benicio que conecte esa
  carpeta a la tarea; si la ve con otro nombre, se exporta `ASESORIA_RAIZ=<ruta>` antes de cada
  script. Donde el texto diga `tesis-asesorar`, es esta carpeta.
- **`<skill>` es la carpeta de este SKILL.md.** Las piezas de `/turnitin` que se usan aquí van
  dentro: `nombrar.py`, `repeticiones.py` y `control_cero.py` en `<skill>/scripts/`, y `voz.md`,
  `ruta-ia-cero.md` y las demás referencias en `<skill>/references/turnitin/`. Cada skill del
  método va en un solo archivo, `<skill>/metodo/<producto>/<nn-nombre>.md` (su SKILL.md primero y
  después sus `references/` y scripts, cada uno tras una línea `===== archivo: … =====`), y las
  piezas comunes en `<skill>/metodo/<producto>/_comun.md`. Si hace falta correr un script del
  método, se copia su bloque a `/tmp/asesorar/`. `prisma_flujo.py` ya está en `<skill>/scripts/`.
- **El scratchpad** es una carpeta temporal fuera de `asesoria` (`/tmp/asesorar/`).
- **No hay Word por COM ni PowerShell.** `indice.ps1`, `ExportAsFixedFormat`, `SaveAs2` y la
  papelera de Windows no existen aquí. El índice y las tablas de ilustraciones se insertan igual
  con `indice_word.py` e `indice_tablas_word.py` (quedan como campos), y el Word se entrega con
  el aviso de que, al abrirlo, se actualizan con clic derecho → Actualizar campos → toda la tabla;
  en el informe a Benicio va como pendiente suyo. El PDF se saca con
  `soffice --headless --convert-to pdf` si LibreOffice está; si no, se entrega el Word y el PDF
  queda pendiente para Benicio. Un `.doc` antiguo se convierte también con `soffice`.
- **R**: se usa `Rscript` si está en el PATH; si no, el cálculo se hace en Python (pandas,
  scipy) y se dice en el informe. Los audios se transcriben con `faster-whisper` si se puede
  instalar; si no, se le pide a Benicio el texto del audio.
- **Scopus** necesita `ELSEVIER_API_KEY` como variable de entorno o en un `.env` dentro de
  `asesoria`. Sin ella, `--scopus` se omite y se sigue con OpenAlex y Crossref.
- **`/turnitin` no está en Cowork.** Cuando el reporte no cumple (2.10), se le dice a Benicio
  qué salió y cuánto falta, y que la bajada se hace en Claude Code con `/turnitin`.
"""


def skill_md(t):
    t = cambiar(t, [
        ("de la carpeta tesis-asesorar del usuario", "de la carpeta asesoria del usuario"),
        ("o nombre una subcarpeta de tesis-asesorar", "o nombre una subcarpeta de asesoria"),
        ("<ASESORAR>\\", "asesoria\\"),
        ("`<skill>` es `<SKILLS>/asesorar`", "`<skill>` es la carpeta de este SKILL.md"),
        ("`<METODO>\\<producto>\\fuente\\`", "`<skill>/metodo/<producto>/<nn-nombre>.md`"),
        ("`<METODO>\\tesis\\fuente\\10-humanizador-academico`", "`<skill>/metodo/tesis/10-humanizador-academico.md`"),
        ("<SKILLS>/turnitin/voz.md", "<skill>/references/turnitin/voz.md"),
        ("python <SKILLS>/turnitin/scripts/nombrar.py \"asesorar\\Luna\" --forzar",
         "python <skill>/scripts/nombrar.py \"Luna\" --forzar"),
        ("python <SKILLS>/turnitin/scripts/repeticiones.py",
         "python <skill>/scripts/repeticiones.py"),
    ], "SKILL.md")
    # El bloque de rutas de Windows no aplica en Cowork.
    t = re.sub(r"## Rutas \(leer primero\).*?(?=## La carpeta)", "", t, flags=re.S)
    t = t.replace("`control_cero.py <word>`", "`python <skill>/scripts/control_cero.py <word>`")
    t = re.sub(r"`references/ruta-ia-cero\.md` de `/turnitin`", "`<skill>/references/turnitin/ruta-ia-cero.md`", t)
    t = t.replace("`ruta-ia-cero.md` de `/turnitin`", "`<skill>/references/turnitin/ruta-ia-cero.md`")
    # La sección de Cowork va justo después del título.
    fin = t.index("\n", t.index("\n# ") + 1)
    return t[:fin + 1] + EN_COWORK + t[fin + 1:]


def mapa_md(t):
    return cambiar(t, [
        ("`<METODO>\\<producto>\\fuente\\<nn-nombre>\\<nombre>\\SKILL.md`.\n"
         "Se leen **en el momento**, desde ahí, para usar siempre la versión vigente. No se copian.",
         "`<skill>/metodo/<producto>/<nn-nombre>.md`: cada skill en un solo archivo, con su SKILL.md primero\n"
         "y sus `references/` detrás (copia hecha al armar el zip). Las piezas comunes, en\n"
         "`<skill>/metodo/<producto>/_comun.md`. Donde abajo dice `skills/<producto>/fuente/` + `NN-nombre`,\n"
         "es `<skill>/metodo/<producto>/NN-nombre.md`; y `skills/tesis/_comun/`, `<skill>/metodo/tesis/_comun.md`."),
    ], "mapa-de-skills.md")


def main():
    archivos = {}  # ruta dentro del zip -> bytes
    for f in sorted(SKILL.rglob("*")):
        rel = f.relative_to(SKILL)
        if f.is_dir() or "__pycache__" in rel.parts or rel.parts[0] == "cowork" or f.suffix == ".ps1":
            continue
        archivos[rel.as_posix()] = f.read_bytes()
    for nombre in ("nombrar.py", "repeticiones.py", "control_cero.py"):
        archivos[f"scripts/{nombre}"] = (TURNITIN / "scripts" / nombre).read_bytes()
    archivos["references/turnitin/voz.md"] = (TURNITIN / "voz.md").read_bytes()
    for f in sorted((TURNITIN / "references").glob("*")):
        archivos[f"references/turnitin/{f.name}"] = f.read_bytes()
    # Cowork admite 200 archivos por zip: cada skill del método va en un solo .md con todos sus archivos.
    for producto in ("tesis", "tsp", "informe", "articulo", "revision"):
        fuente = METODO / producto / "fuente"
        for d in sorted(fuente.iterdir()) if fuente.is_dir() else []:
            if d.is_dir():
                archivos[f"metodo/{producto}/{d.name}.md"] = juntar(d)
        if (METODO / producto / "_comun").is_dir():
            archivos[f"metodo/{producto}/_comun.md"] = juntar(METODO / producto / "_comun")
    archivos["scripts/prisma_flujo.py"] = (METODO / "revision" / "fuente" / "05-revision-fase5-resultados" /
                                           "revision-fase5-resultados" / "scripts" / "prisma_flujo.py").read_bytes()

    arreglos = {"SKILL.md": skill_md, "scripts/comun.py": comun_py, "scripts/nombrar.py": nombrar_py,
                "references/mapa-de-skills.md": mapa_md}
    for ruta, fn in arreglos.items():
        archivos[ruta] = fn(limpio(archivos[ruta]).decode("utf-8")).encode("utf-8")

    if len(archivos) > 200:
        sys.exit(f"Son {len(archivos)} archivos y Cowork admite 200 como máximo.")
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(SALIDA, "w", zipfile.ZIP_DEFLATED) as z:
        for ruta, b in sorted(archivos.items()):
            z.writestr(f"asesorar/{ruta}", limpio(b) if Path(ruta).suffix in TEXTO else b)
    print(f"{SALIDA} · {len(archivos)} archivos · {SALIDA.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
