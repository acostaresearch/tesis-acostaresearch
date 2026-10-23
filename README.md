# tesis-acostaresearch

Las skills de Claude Code que usa Benicio para atender clientes de asesoría: **/asesorar** (cotiza y
hace el trabajo), **/turnitin** (baja IA y similitud) y **/responder** (redacta la respuesta de
WhatsApp), con el método que necesitan (`metodo/`: tesis, TSP, informe, artículo, revisión).

> Repositorio **privado**: `skills/asesorar/precios.md` y `skills/responder/*.md` traen precios y
> ejemplos reales del negocio. No contiene datos de clientes (ni Word, ni PDF, ni `trabajos/`).

## Instalar en otra PC

Necesitas Claude Code, Python 3.10+ y Git.

```
git clone https://github.com/acostaresearch/tesis-acostaresearch.git
cd tesis-acostaresearch
python instalar.py --pip
```

`instalar.py` copia las skills a `~/.claude/skills`, crea `~/Documents/asesoria-acosta/tesis-turnitin`
y `.../tesis-asesorar` (los clientes van en esas dos carpetas) y escribe
`~/.claude/skills/rutas-acosta.json`. Opciones: `--base <carpeta>` para poner los clientes en otro
sitio, `--metodo <carpeta>` si ya tienes el método en otra parte. Reinicia Claude Code y escribe
`/asesorar`, `/turnitin` o `/responder`.

`python ~/.claude/skills/turnitin/scripts/rutas.py` muestra qué carpetas está usando.
Las rutas también se pueden fijar con las variables `ACOSTA_TURNITIN`, `ACOSTA_ASESORAR` y `ACOSTA_METODO`.

La clave de Scopus (si se usa `--scopus`) se toma de la variable de entorno `ELSEVIER_API_KEY`.

## Mantenerlo al día

Las skills se editan donde están instaladas (`~/.claude/skills`). Para subir los cambios:

```
python sincronizar.py
git add -A && git commit -m "..." && git push
```

En la otra PC: `git pull` y `python instalar.py`.

## Qué hay

| Carpeta | Contenido |
|---|---|
| `skills/asesorar` | /asesorar: cotización, trabajo, scripts, `precios.md`, `cowork/armar.py` (zip para Cowork) |
| `skills/turnitin` | /turnitin: Ruta 0 % de IA, similitud, scripts, `voz.md` |
| `skills/responder` | /responder: `datos.md` y `ejemplos.md` |
| `metodo/` | las skills del método (`<producto>/fuente/…` y `_comun`) que /asesorar lee |

Las skills no llevan rutas de una máquina: usan `<SKILLS>`, `<TURNITIN>`, `<ASESORAR>` y `<METODO>`,
definidos al inicio de cada `SKILL.md`.
