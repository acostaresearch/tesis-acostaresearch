r"""Instala las skills /asesorar, /turnitin y /responder en este equipo.

    python instalar.py                          carpetas de clientes en ~/Documents/asesoria-acosta
    python instalar.py --base D:\trabajo         otra carpeta para tesis-turnitin y tesis-asesorar
    python instalar.py --metodo D:\skills        usar un método que ya tienes (por defecto, el de este repositorio)
    python instalar.py --pip                    además instala las librerías de Python

Copia las skills a ~/.claude/skills, crea las carpetas de clientes si faltan y escribe
~/.claude/skills/rutas-acosta.json, que es de donde las skills leen dónde está todo.
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SKILLS = Path.home() / ".claude" / "skills"
IGNORAR = shutil.ignore_patterns("__pycache__", "*.pyc")

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--base", help="carpeta donde van tesis-turnitin y tesis-asesorar")
ap.add_argument("--metodo", help="carpeta con tesis/, tsp/, informe/, articulo/ y revision/")
ap.add_argument("--pip", action="store_true", help="instalar requirements.txt")
a = ap.parse_args()

config_f = SKILLS / "rutas-acosta.json"
previa = json.loads(config_f.read_text(encoding="utf-8")) if config_f.exists() else {}
base = Path(a.base).expanduser() if a.base else None
config = {
    "turnitin": str(base / "tesis-turnitin") if base else previa.get("turnitin") or str(Path.home() / "Documents" / "asesoria-acosta" / "tesis-turnitin"),
    "asesorar": str(base / "tesis-asesorar") if base else previa.get("asesorar") or str(Path.home() / "Documents" / "asesoria-acosta" / "tesis-asesorar"),
    "metodo": str(Path(a.metodo).expanduser()) if a.metodo else previa.get("metodo") or str(AQUI / "metodo"),
}

SKILLS.mkdir(parents=True, exist_ok=True)
for origen in sorted((AQUI / "skills").iterdir()):
    if origen.is_dir():
        shutil.copytree(origen, SKILLS / origen.name, dirs_exist_ok=True, ignore=IGNORAR)
        print(f"skill  {origen.name} -> {SKILLS / origen.name}")
for clave in ("turnitin", "asesorar"):
    Path(config[clave]).mkdir(parents=True, exist_ok=True)
config_f.write_text(json.dumps(config, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"rutas  {config_f}")
for k, v in config.items():
    print(f"         {k:9} {v}")
if a.pip:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(AQUI / "requirements.txt")])
print("\nListo. Reinicia Claude Code y escribe /asesorar, /turnitin o /responder.")
