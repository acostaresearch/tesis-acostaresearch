"""Trae al repositorio los cambios hechos en las skills instaladas (para subirlos a GitHub).

    python sincronizar.py        copia ~/.claude/skills/{asesorar,turnitin,responder} a ./skills

Va en este sentido (instalado -> repositorio). Para lo contrario, python instalar.py.
No copia los trabajos de clientes (asesorar/trabajos) ni los __pycache__.
"""
import shutil
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SKILLS = Path.home() / ".claude" / "skills"
for nombre in ("asesorar", "turnitin", "responder"):
    shutil.copytree(SKILLS / nombre, AQUI / "skills" / nombre, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "trabajos"))
    print("copiada", nombre)
