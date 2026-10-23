"""Dónde están las carpetas de trabajo. Lo comparten las skills asesorar y turnitin (el archivo es el mismo).

Se leen, en este orden, de: las variables de entorno ACOSTA_TURNITIN, ACOSTA_ASESORAR y ACOSTA_METODO;
el archivo rutas-acosta.json que deja instalar.py junto a las skills (~/.claude/skills/); y, si no
hay nada, de ~/Documents/acostaresearch/{tesis-turnitin, tesis-asesorar, skills}.

    python rutas.py            muestra las tres rutas y si existen
"""
import json
import os
from pathlib import Path

CONFIG = Path(os.environ.get("ACOSTA_RUTAS") or Path(__file__).resolve().parents[2] / "rutas-acosta.json")


def _leer():
    try:
        return json.loads(CONFIG.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _ruta(clave, por_defecto):
    return Path(os.environ.get("ACOSTA_" + clave.upper()) or _leer().get(clave) or por_defecto).expanduser()


_BASE = Path.home() / "Documents" / "acostaresearch"
TURNITIN = _ruta("turnitin", _BASE / "tesis-turnitin")
ASESORAR = _ruta("asesorar", _BASE / "tesis-asesorar")
METODO = _ruta("metodo", _BASE / "skills")

if __name__ == "__main__":
    for nombre, ruta in (("turnitin", TURNITIN), ("asesorar", ASESORAR), ("metodo", METODO)):
        print(f"{nombre:9} {'existe ' if ruta.is_dir() else 'NO EXISTE'}  {ruta}")
