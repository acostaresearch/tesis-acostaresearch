# El Word del artículo: un solo motor

Todas las fases arman el .docx con **`scripts/articulo_docx.py`**, que viene
dentro de esta skill. Nunca se arma el documento "a mano" ni con otra
plantilla: así sale idéntico en cualquier sesión, con cualquier modelo.

Formato fijo: A4, márgenes 2.54 cm, Times New Roman 12, interlineado 1.5,
cuerpo justificado con sangría de 1.27 cm, encabezados en negro (no en el azul
de Word), tablas APA 7 con solo reglas horizontales, referencias con sangría
francesa, `[POR CONFIRMAR: ...]` en rojo.

## Entorno (vale para claude.ai, Claude Code, la API o cualquier otro cliente)

- **Requisito único:** Python 3 con `python-docx`. Si falta:
  `pip install python-docx` (en claude.ai ya está).
- **Ruta del script:** `scripts/articulo_docx.py` dentro de la carpeta de esta
  skill. En claude.ai suele estar en `/mnt/skills/user/<nombre-de-la-skill>/`;
  si no, buscarlo por nombre (`find / -name articulo_docx.py 2>/dev/null | head -1`).
  No se asume ninguna ruta fija.
- **Archivos del investigador:** donde el cliente los deje (en claude.ai,
  `/mnt/user-data/uploads/`). **Entregables:** donde el cliente los entregue (en
  claude.ai, `/mnt/user-data/outputs/`; en Claude Code, la carpeta del proyecto).
- **Rutas con tildes (Mac):** R (`readxl`) y algunas herramientas no abren
  archivos cuya carpeta lleva tildes o eñes (p. ej. `ARTÍCULOS`). Si un archivo
  "no se puede cargar", copiarlo primero a una carpeta sin tildes.
- **Si no hay ejecución de código** (algunos clientes con modelos de otros
  proveedores): entregar el .md de la sección con la sintaxis de abajo y decirle
  al investigador que lo pegue en Word; el formato fino queda a su cargo. Es el
  único caso en que se entrega sin .docx.

## Cómo se usa

La fase escribe su sección en un archivo `.md` con la sintaxis mínima, y luego:

```bash
S=scripts/articulo_docx.py            # ruta real del script
python3 $S nuevo   --md seccion.md --out ARTICULO_clave_v2.docx --perfil REVISTA_clave.json --fuentes inventario.json   # Fase 2
python3 $S nuevo   --md ficha.md --out FICHA_clave.docx --compacto        # Fase 0, carta y documentos de trabajo
python3 $S verificar FICHA_clave.docx --con-tablas --limite 700          # Fase 0: la Ficha cuenta sus tablas
python3 $S agregar --base ARTICULO_clave_v3.docx --md seccion.md --perfil REVISTA_clave.json --fuentes inventario.json   # Fases 3 a 8
python3 $S perfil plantilla > REVISTA_clave.json                         # Fase 0: perfil de la revista
python3 $S esquema ARTICULO_clave_v4.docx --acronimos                     # lo primero en cada fase
python3 $S texto   ARTICULO_clave_v4.docx --seccion "Métodos"             # leer solo lo que hace falta
python3 $S verificar ARTICULO_clave_v5.docx --perfil REVISTA_clave.json --fuentes inventario.json   # antes de entregar, siempre
python3 $S reemplazar ARTICULO_clave_v5.docx --buscar "[POR CONFIRMAR: ...]" --por "dato"   # en el Word y su RESPALDO
```

`agregar` **no reescribe** lo que ya estaba: inserta la sección nueva antes de
Referencias, fusiona las referencias nuevas con las existentes (ordenadas, sin
duplicados) y guarda con el número de versión siguiente. Nunca sobrescribe la
versión anterior. Opciones:

- `--posicion inicio`: inserta después del título (resumen y abstract, Fase 7).
- `--posicion antes-de --seccion "Introducción"`: delante de una sección dada.
- `--titulo "..."`: reemplaza el título provisional (Fase 7).
- `--idioma en`: "Table", "Figure", "Note.", "References".
- `--out NOMBRE.docx`: cuando el número de versión no debe ser el siguiente
  (p. ej. revisión que pasa de `_v2` a `_v4`).

**Economía:** con `esquema` y `texto --seccion` la fase lee solo lo que
necesita. No se vuelca el artículo entero al chat, ni se reescribe el documento
completo para añadir una sección.

## Perfil de la revista y respaldo

Con `--perfil REVISTA_[clave].json` (lo arma la Fase 0, ver
`perfil_revista.md`), `nuevo` y `agregar` producen **dos archivos con el mismo
texto**: `_vN.docx` con el formato de la revista (fuente, tamaño, interlineado,
márgenes, alineación, numeración de líneas y páginas, estilo de títulos) y
`_vN_RESPALDO.docx` con el formato neutro de la ruta. `agregar` actualiza los
dos si existe el respaldo de la versión anterior. `verificar --perfil` controla
además el límite de palabras, las secciones exigidas y su orden. Sin perfil, el
motor usa el formato neutro y no genera respaldo.

## Sintaxis del .md

```
[TITULO] Título del artículo
# Introducción
Párrafo con *cursiva*, **negrita** y [POR CONFIRMAR: dato que falta].

## Subtítulo
[SIN SANGRIA] Párrafo sin sangría.
- viñeta

[TABLA 2] Título de la tabla en cursiva
| Variable | M | DE |
|---|---|---|
| Tecnoestrés | 3.21 | 0.84 |
[NOTA] n = 312. M = media; DE = desviación estándar.

[FIGURA 1] Modelo estructural estimado | figura1.png
[NOTA] Coeficientes estandarizados. *** p < .001.

[SALTO]

Cita por clave del inventario [F012], narrativa [F012:n], con página
[F012:p. 45] (o [F012:n, p. 45]) y agrupada [F012][AR51541814].
```

## Citas por clave y referencias generadas

Con `--fuentes inventario.json` (en `nuevo`, `agregar`, `verificar` y
`normalizar`) las claves se convierten al `estilo_cita` del perfil (sin perfil,
APA 7; también Chicago autor-fecha 18.ª, Vancouver e IEEE) y el motor **genera**
`# Referencias` con todas las fuentes citadas: la sección **no** la escribe a
mano. Vancouver/IEEE numeran por primera aparición en todo el documento y se
renumeran en cada `agregar`. Una clave ausente sale `[POR CONFIRMAR: fuente
F099]` en rojo y `verificar` la marca ✗. El `_RESPALDO` usa el mismo estilo de
cita. Cada cita va entre marcadores ocultos y el Word guarda en sus propiedades
el mapa cita→clave y una copia de las fuentes citadas: `normalizar --perfil
REVISTA_nueva.json` reconvierte citas y lista al estilo de otra revista
(reenvío) y `normalizar --estilo zotero` deja marcas para el RTF Scan de Zotero.
Detalle y vuelta a Zotero/Mendeley: `fuentes_y_citas.md`.

Las fases de la ruta **no** escriben referencias a mano. (Solo por
compatibilidad con documentos antiguos, el motor sigue aceptando una sección de
referencias escrita a mano y la fusiona; no se usa al redactar.)

Reglas: el número de tabla y figura lo pone quien escribe (continuo, la Tabla
1 es la sociodemográfica); el texto cita cada tabla **antes** de que aparezca;
las celdas numéricas se centran solas; la figura se inserta desde un .png que
esté en la misma carpeta del .md (si no existe, sale un `[POR CONFIRMAR]`).

## Verificación

`verificar` revisa formato, numeración continua de tablas y figuras, que cada
una se cite antes de aparecer, bordes verticales, referencias duplicadas o
desordenadas, posibles citas sin referencia, claves sin fuente o sin convertir,
pendientes y palabras contra el límite. **Se corre siempre antes de entregar**; si marca ✗, se corrige y se
vuelve a correr. Los avisos `!` se revisan a mano.

La revisión visual (convertir a PDF y mirar) **no es obligatoria**: solo si el
entorno tiene LibreOffice o Word y algo en `verificar` hace sospechar. No se
gastan turnos en ella cuando la verificación pasó.
