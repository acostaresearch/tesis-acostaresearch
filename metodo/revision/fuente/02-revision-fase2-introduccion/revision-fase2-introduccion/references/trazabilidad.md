# Matriz de trazabilidad

Un solo archivo para todo el artículo: **`TRAZABILIDAD_[clave].xlsx`**. Lo crea
la Fase 2; las fases siguientes que citan le **agregan filas**, nunca crean otro.
En una revisión es la Fase 6 (los estudios incluidos se trazan en la tabla de
características de la Fase 5, no aquí).

Se arma antes de pasar la sección al .docx y se entrega aparte: no va en el
manuscrito.

## Las siete columnas (fijas en todas las fases)

| Cita en el texto | ID | Ubicación | Afirmación que sostiene | Frase textual del abstract o de la fuente | Tipo | Dirección coincide |
|---|---|---|---|---|---|---|

- **Cita en el texto**: tal como aparece, con su año.
- **ID**: el del `inventario.json` (F001, F002…), que no se renumera nunca. Las
  cifras estadísticas buscadas en la web llevan `WEB`.
- **Ubicación**: `Introducción, bloque 1` a `bloque 5`; en la Discusión, el
  hallazgo, la hipótesis o la pregunta de revisión.
- **Afirmación que sostiene**: qué dice el artículo apoyándose en esa cita. En
  una cifra: organismo, año y ámbito.
- **Frase textual**: copiada, no parafraseada. Es el punto entero de la matriz.
- **Tipo**: `contenido` (hay resumen **completo**; uno marcado `RECORTADO` en
  el inventario no vale), `titulo` (solo se menciona) o `cifra`.
- **Dirección coincide**: `si` / `no` / `no informa` / `no aplica`. Se llena en
  las filas de hipótesis. `no informa` = el resumen no dice la dirección: esa
  fila no respalda la hipótesis. Si una hipótesis solo tiene filas `no informa`,
  se declara en el texto con respaldo escaso o se busca más.

## Cómo se genera (scripts/trazabilidad.py)

La fase escribe sus filas en un `filas.json` (lista de objetos con las claves
`cita, id, ubicacion, afirmacion, frase, tipo, direccion`) y:

```bash
T=scripts/trazabilidad.py      # ruta real del script de esta skill
python3 $T crear   --out TRAZABILIDAD_clave.xlsx --filas filas.json --inventario inventario.json   # Fase 2
python3 $T agregar --base TRAZABILIDAD_clave.xlsx --filas filas.json --inventario inventario.json  # fases siguientes
python3 $T verificar TRAZABILIDAD_clave.xlsx --inventario inventario.json
```

`agregar` conserva las filas previas y omite las repetidas. Con `--inventario`
el script comprueba que cada ID exista, que una fila de contenido tenga
abstract y que **la frase aparezca literal en ese abstract**, y marca ✗ toda
`Dirección = no`. Si marca ✗, se corrige el texto (o la fila) y se vuelve a
correr. Requiere `openpyxl` (`pip install openpyxl`). Sin ejecución de código
(modo C), se entrega la tabla en Markdown con las mismas siete columnas y la
misma revisión hecha a mano.

## Cómo se revisa

Fila por fila: **¿la frase dice efectivamente lo que el artículo le atribuye?**
Sí: queda. Aproximadamente: no sirve; se ajusta la afirmación a lo que la
fuente dice o se busca otra fuente (**no existe la categoría "aproximada"**).
No: se corrige el texto o se elimina la afirmación. En las filas de hipótesis,
además: **¿la dirección del estudio coincide con la de la hipótesis?**

Una fila de tipo `titulo` solo puede afirmar lo que el título respalda; si
atribuye un hallazgo, una cifra o una dirección, está mal.

## Qué se le dice al investigador al entregar

Cuatro líneas: cuántas fuentes por contenido y cuántas por título; cuántas filas
se corrigieron; **qué hipótesis quedaron con respaldo escaso**, nombrándolas;
los `[POR CONFIRMAR]` abiertos.

## Por qué existe

El error más grave no es no encontrar fuentes: es escribir una idea plausible y
colgarle un autor del inventario que dice otra cosa. Con la frase textual al
lado de la afirmación, la discrepancia salta sola.
