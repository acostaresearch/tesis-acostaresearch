---
name: articulo-fase3-revision-literatura
description: >-
  Fase 3 de la Ruta del Artículo Empírico: redacta la Revisión de la literatura
  y el sustento de las hipótesis, y la une al mismo Word que trae la
  Introducción. Escribe las teorías base, un acápite por constructo y un párrafo
  de sustento por hipótesis, verificando en el resumen de cada estudio citado
  que la dirección coincida con la de la hipótesis. En estudios instrumentales
  trabaja el modelo de medida y en cualitativos las categorías y antecedentes,
  sin hipótesis. Si falta respaldo, guía una búsqueda complementaria con la
  ecuación lista. Actualiza la matriz de trazabilidad. Nunca inventa citas,
  teorías ni hallazgos. Escribe en español con la norma, el estilo de cita y el
  formato de la revista destino, humaniza la sección y entrega la versión de la
  revista y su respaldo neutro. ACTIVAR con revisión de la literatura de mi
  artículo, marco teórico del paper, sustento de las hipótesis, fundamento
  teórico, o cuando suban el Word de la Fase 2.
license: Proprietary
metadata:
  version: "2.2.0"
  fase: "3"
  ruta: "Ruta del Artículo Empírico — Acosta | IA & Research"
---

# Fase 3 — Revisión de la literatura

## Dónde estás trabajando (léelo primero)

Mira qué herramientas tienes y elige **un** modo; no lo mezcles:

| Modo | Dónde | Cómo se entrega |
|---|---|---|
| **A · Con herramientas** | Claude con skills, Cowork, Claude Code, API | Scripts de esta skill (`scripts/`), archivos .docx/.xlsx reales |
| **B · Chat con código** | ChatGPT con análisis de datos, Claude.ai sin skills | Pide al usuario que suba `articulo_docx.py` (viene en la carpeta *herramientas* del paquete) y úsalo igual que en A |
| **C · Chat sin código** | Grok, ChatGPT sin análisis, cualquier chat | Entrega cada sección en un bloque de texto listo para pegar en `PLANTILLA_ARTICULO.docx`, tablas en Markdown; nunca prometas un archivo que no puedes generar |

En cualquier modo: **un paso por turno**, y si el usuario pega una
**Tarjeta de continuidad**, léela y no vuelvas a preguntar lo que ya dice.

## Para qué sirve esta skill

Escribe la sección que sigue a la Introducción y **la une al mismo documento**,
en español y con la norma de la revista destino (`REVISTA_[clave].json`).
Responde tres preguntas que el revisor va a hacer: qué teorías dan base a los
constructos, qué se sabe de cada uno, y por qué es razonable esperar las
relaciones que el estudio plantea.

### La ruta completa

```
  Fase 0 · Tema y orientación
  Fase 1 · Matriz de estrategia
  Fase 2 · Introducción
  Fase 3 · Revisión de la literatura   ← estás aquí
  Fase 4 · Métodos
  Fase 5 · Resultados
  Fase 6 · Discusión
  Fase 7 · Conclusiones y abstract
  Fase 8 · Adaptación a la revista y envío
  Fase 9 · Respuesta a revisores
```

Insumos, entregables y quién decide cada dato: `references/ruta.md`, que manda
sobre este archivo si algo no coincide.

## Qué cambia según el tipo de estudio

El tipo se **lee en la Matriz** (primera hoja, *Diseño y muestra* o *Diseño de la revisión*: Enfoque y Diseño
específico). No se vuelve a preguntar.

| Tipo | Qué lleva esta sección |
|---|---|
| Cuantitativo (correlacional, regresión, multinivel, SEM), experimental, con datos propios o secundarios | Teorías, acápite por constructo, sustento de cada hipótesis |
| Instrumental (validación de escala) | Teoría del constructo, versiones previas del instrumento, **modelo de medida esperado**. Sin hipótesis sustantivas |
| Cualitativo | Enfoque o teoría orientadora, **categorías y sus antecedentes**. Sin hipótesis |
| Mixto | Cada rama por separado |
| Revisión sistemática, de alcance o bibliométrica | **No lleva esta sección** (ver abajo) |

Si es una revisión: decirle que su artículo no tiene Fase 3 porque los estudios
revisados son los Resultados, y que su ruta está en el otro paquete (Ruta del
Artículo de Revisión): sigue en la Fase 4, `revision-fase4-metodos`, con su
`_v2.docx` y el protocolo. No se escribe nada aquí.

## Regla del acompañamiento: el investigador es novato

- **Un paso por turno.** Nunca dos.
- Toda pregunta técnica lleva como última opción `"No me queda claro, ponme
  ejemplos"`, y si sigue trabado, `"Prefiero que alguien me lo explique"`, que
  responde con el WhatsApp del equipo (+51 923 095 940) y deja el punto
  pendiente **sin bloquear**.
- Cuando se le pide buscar fuera del chat, se le dan las instrucciones completas
  y la ecuación lista para pegar.
- Redacción de las opciones en `references/estilo_preguntas.md`.

## Regla de oro: veracidad absoluta

1. **Cita de contenido solo con resumen completo y real** en el inventario.
   Sin resumen, la fuente se menciona por su título y no se le atribuye ningún
   hallazgo. Un resumen marcado `RECORTADO` (OpenAlex, `buscar_en_la_literatura`:
   ~400 caracteres) cuenta como sin resumen hasta conseguir el completo: abrir
   el DOI y copiarlo literal de la página de la revista, o pedir el export de
   Scopus/WoS de ese registro; se pega en el campo `abstract` de su ID en
   `inventario.json` (el ID no cambia). Sin el resumen completo no hay control
   de dirección posible.
2. **No se atribuye una teoría a una fuente que no la nombra.** Es el error más
   frecuente de esta sección. Si ningún resumen del inventario menciona la teoría
   que sostiene el modelo, se dice y se pide material específico sobre ese marco.
3. **Control de dirección obligatorio.** Antes de usar un estudio como respaldo,
   verificar en su resumen que la dirección coincide con la de la hipótesis. Si
   el resumen no la informa, ese estudio no respalda la dirección.
4. **Estilo de conjetura, siempre.** Aunque el investigador ya tenga resultados,
   esta sección se escribe como si no existieran.
5. **Nada se inventa**: ni definiciones, ni años, ni autores. Lo que falte queda
   `[POR CONFIRMAR: ...]`.

## Economía de la sesión

1. Cada archivo de `references/` se lee **solo en su paso**.
2. Del .docx se lee el `esquema` y, si hace falta, `texto --seccion
   "Introducción"`; no se vuelca el artículo entero al chat.
3. En el chat va lo que el investigador debe decidir; el texto vive en el .docx.
4. El documento se comprueba con `articulo_docx.py verificar`, no con revisión
   visual.

## Entorno

Scripts en `scripts/` de esta skill (si no aparecen, buscar `articulo_docx.py`
por nombre). Archivos y caso sin código: `references/formato_docx.md`, Entorno.

## Lo que esta skill NO hace

- **No reescribe la Introducción.** Si detecta una incoherencia con ella, la
  señala y pregunta; no la corrige por su cuenta.
- **No formula hipótesis nuevas.** Vienen de la Matriz de la Fase 1.
- **No discute resultados.**
- **No es para tesis.** Si aparecen "capítulo II", "asesor" o "jurado", derivar
  a `marco-teorico`.

---

# Flujo

## Paso 0 — Bienvenida

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Ruta del Artículo Empírico · Fase 3

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

¡Bienvenido a las Skills de Acosta!

Estás en la **Fase 3 — Revisión de la literatura**. Aquí se explica por qué tu estudio tiene sentido: qué teoría lo sostiene, qué se sabe de cada variable y por qué es razonable esperar lo que planteas.

Trabajamos sobre el mismo Word de la Fase 2. Al terminar tendrás un solo archivo con la introducción y esta sección, no dos sueltos.

Súbeme lo que tengas.
```

## Paso 1 — Insumos

Lo que hace falta, todo salido de la Fase 2 y la Fase 1:

- `ARTICULO_[clave]_v2.docx` y su `_v2_RESPALDO.docx`
- `REVISTA_[clave].json` (perfil de la revista, Fase 0)
- `MATRIZ_[clave].xlsx` (hipótesis con su trayectoria, constructos o
  categorías, tipo de estudio y diseño)
- `TRAZABILIDAD_[clave].xlsx`
- `inventario.json` (y, si quiere, fuentes nuevas: exports con resumen, fichas
  de la plataforma Acosta o la colección de su Zotero o Mendeley en RIS)

```
¿Qué traes?
- "El Word de la Fase 2 y lo demás"
- "Solo el Word de la Fase 2"
- "Tengo la introducción escrita en otro lado"
- "Vengo directo, sin la fase anterior"
```

Qué se hace con cada respuesta:

- **"El Word de la Fase 2 y lo demás"** → correr
  `python3 scripts/articulo_docx.py esquema ARTICULO_[clave]_v2.docx --acronimos`,
  leer la Matriz y pasar al Paso 2.
- **"Solo el Word de la Fase 2"** → el mismo `esquema`, y pedir lo que falte:
  la Matriz (o, si no la tiene, en **una sola pregunta** tipo de estudio,
  hipótesis o categorías, constructos y estilo de cita); sin `inventario.json`,
  los exports de sus fuentes para rehacerlo en el Paso 2; sin la trazabilidad,
  se crea en el Paso 7 con `crear` en vez de `agregar`.
- **"Tengo la introducción escrita en otro lado"** → pedir el texto; pasarlo a
  un .md y crear la `_v2` con `articulo_docx.py nuevo --perfil` para unificar el formato
  (ver `references/ruta.md`); pedir la Matriz y los exports, y seguir como en
  la opción anterior.
- **"Vengo directo, sin la fase anterior"** → la pregunta única de datos
  mínimos y los exports. Sin Introducción, la sección se crea sola con
  `articulo_docx.py nuevo --md revision_lit.md --out ARTICULO_[clave]_v3.docx --perfil REVISTA_[clave].json`,
  y se le dice que la Introducción se añade después con
  `articulo-fase2-introduccion` (`agregar --posicion antes-de --seccion
  "Revisión de la literatura"`).

Del `esquema` salen los acrónimos y las referencias ya listadas; del **perfil**,
el estilo de cita, el título exacto de esta sección en `estructura` y el límite
de palabras; de la Ficha, el término unificador. **No se vuelven a preguntar ni
se duplican.** Si falta el perfil, se pide; si no existe, se crea en un paso
con `references/perfil_revista.md`. El tipo de estudio sale de la Matriz y
decide la rama (tabla de arriba). Si el
estudio lleva hipótesis y no vienen enunciadas, derivar a
`articulo-fase1-matriz-de-estrategia`.

## Paso 2 — Inventario y cobertura

Si trae exports nuevos:

```bash
python3 scripts/inventario_fuentes.py scopus_nuevo.ris fichas_acosta.txt --previo inventario.json --out inventario.json
python3 scripts/referencias.py doi 10.xxxx/yyyy --inventario inventario.json   # fuente web con DOI verificado
```

Un archivo por base o vía (RIS o CSV de Scopus, texto plano de WoS, RIS o
BibTeX de Zotero o Mendeley, fichas de `buscar_fuentes` o
`ampliar_desde_mis_fuentes` pegadas tal cual), nunca el mismo export en varios
formatos (`references/fuentes_y_citas.md`). Conserva los IDs de la Fase 2 y numera los nuevos a
continuación. Si no trae nada nuevo, se trabaja con el `inventario.json` tal
cual. Modo C: se amplía a mano la tabla Markdown del inventario (ID, cita,
¿resumen completo?).

Lo importante no es el conteo general: es **la cobertura por hipótesis** (o por
categoría en cualitativo, por versión previa del instrumento en instrumental),
que decide si la sección se puede escribir.

| Hipótesis / categoría | Trayectoria | Fuentes con resumen (IDs) | ¿Suficiente? |
|---|---|---|---|

Cada hipótesis necesita **dos o tres fuentes con resumen completo que hablen de
esa relación en concreto e informen su dirección**; las de resumen recortado o
que no informan la dirección no cuentan. Mostrar la tabla antes de redactar. Si alguna queda sin respaldo
(pasa casi siempre con la de mediación), ofrecer dos caminos:

1. **Buscar más fuentes**: la ecuación específica para esa relación con
   `references/busqueda_bases.md` y esperar el nuevo export; o, con la
   plataforma conectada, `buscar_fuentes` con esa relación (sus fichas llegan
   recortadas: no informan dirección hasta tener el resumen completo).
2. **Sustentarla de forma indirecta**, encadenando las trayectorias que sí
   tienen respaldo y **declarando en el propio texto** que el precedente directo
   no se localizó.

Lo que no se hace: escribir el párrafo igual y colgarle citas que hablan de otra
cosa.

## Pasos 3 a 5 — Redactar la sección

Detalle de cada bloque y de las variantes por tipo de estudio en
`references/literatura_e_hipotesis.md`. Todo va en `revision_lit.md`, bajo
el **título exacto** que da la `estructura` del perfil (p. ej.
`# Revisión de la literatura` o `# Marco teórico`), con `##` por acápite. Citas
**por clave** (`[F012]`, `[AR51541814:n]`, `[F012:p. 45]`, `[F012][F020]`);
**sin `# Referencias`**: el motor las formatea en el estilo del perfil y
regenera la lista única con todo lo citado (`references/fuentes_y_citas.md`).
Si la `_v2` traía referencias escritas a mano (modo antiguo), se respetan.
Extensión acorde al `limite_palabras` del perfil; decírsela antes de redactar.

**Paso 3 — Teorías base.** ¿Qué teoría explica por qué estos constructos
deberían vincularse? Solo teorías que las fuentes verificadas nombren; qué
postula y qué parte usa el estudio; si son dos, cómo se articulan.

**Paso 4 — Un acápite por constructo** (o por categoría, o el constructo y las
versiones del instrumento): definición con cita, cómo se operacionalizó, qué se
sabe en poblaciones parecidas y cierre con lo que queda abierto. Los acápites no
tienen por qué medir lo mismo.

**Paso 5 — Sustento.** Según el tipo:

- **Con hipótesis**: un párrafo por hipótesis, de 2 a 4 citas verificadas,
  terminado con su enunciado (`H1: ...`). Estilo de conjetura, control de
  dirección y mediación solo con precedente de mediación (o declarado). Si la
  evidencia es mixta, se dice.
- **Instrumental**: el **modelo de medida esperado** (estructura factorial y su
  base). Sin hipótesis sustantivas; las de validez, si la Matriz las trae, se
  sustentan con control de dirección.
- **Cualitativo**: cierre con lo que los antecedentes no explican y el estudio va
  a explorar. Sin hipótesis ni anticipación de lo que dirán los participantes.

Cerrar con un párrafo breve que integre el modelo (o el marco de categorías); si
el artículo lleva figura del modelo, remitir a ella.

## Paso 6 — Humanizar la sección

Según `references/anti_ia.md`: `humanizador-academico` sobre `revision_lit.md`
(una ronda, 1-2 bloques, el autor aprueba cada bloque en un mensaje); si no
está, el servidor (`humanizar_mi_documento`); si no hay ninguno, la lista de
control. Esta sección es la más delatora del artículo: vigilar sobre todo el 0
(párrafos de sustento con la misma arquitectura), el 6 (nominalización al
definir constructos) y el 4 ("diversos autores señalan" sin nombrar a ninguno).
**No darles a todas las hipótesis el mismo espacio si su respaldo es
desigual.** En el chat, una línea: qué se tocó.

## Paso 7 — Actualizar la matriz de trazabilidad

Se **agregan filas** a la matriz de la Fase 2. Columnas y criterios en
`references/trazabilidad.md`. Filas en `filas.json` y:

```bash
python3 scripts/trazabilidad.py agregar --base TRAZABILIDAD_[clave].xlsx --filas filas.json --inventario inventario.json
```

En esta fase manda **Dirección coincide**: cualquier `no` (✗) obliga a corregir
el texto antes de entregar, igual que una frase que no está en el abstract. Una
hipótesis cuyas filas son todas `no informa` se declara en el texto con
respaldo escaso o se vuelve al Paso 2 a buscar más. Modo C: las filas nuevas en
la tabla Markdown de siete columnas.

## Paso 8 — Unir al documento

Reglas en `references/documento_en_cadena.md`.

```bash
python3 scripts/articulo_docx.py agregar --base ARTICULO_[clave]_v2.docx --md revision_lit.md --perfil REVISTA_[clave].json --fuentes inventario.json
python3 scripts/articulo_docx.py verificar ARTICULO_[clave]_v3.docx --perfil REVISTA_[clave].json --fuentes inventario.json
python3 scripts/referencias.py exportar --inventario inventario.json --docx ARTICULO_[clave]_v3.docx --ris CITADAS_[clave].ris
```

`agregar` deja la Introducción intacta, inserta la sección antes de Referencias,
regenera la lista con todo lo citado (en Vancouver/IEEE, renumerada) y guarda
`ARTICULO_[clave]_v3.docx` (formato de la revista) y `_v3_RESPALDO.docx`
(neutro, mismo texto). Si `verificar` marca ✗, se corrige el .md y se vuelve a
agregar sobre la `_v2`. Antes de entregar, comprobar con el `esquema` que los
acrónimos coinciden con la Introducción, y con la Ficha y el perfil, el término
unificador y el estilo de cita; si algo no coincide, señalarlo y preguntar.
`CITADAS_[clave].ris` (todo lo citado hasta aquí) se importa en la colección
del artículo en Zotero o Mendeley.
Modo C: la sección en un bloque listo para pegar en `PLANTILLA_ARTICULO.docx`
(o en el Word de la Fase 2), antes de Referencias, con claves; al final, la
lista de referencias de las nuevas citadas formateada a mano en el estilo del
perfil y un bloque RIS con ellas.

## Paso 9 — Cierre

- [ ] ¿Hay acápite de teorías y uno por constructo (o categoría)?
- [ ] ¿Cada teoría mencionada aparece explícitamente en una fuente verificada?
- [ ] ¿Cada hipótesis tiene su párrafo de sustento y su enunciado (o, según el
      tipo, el modelo de medida o el cierre de categorías)?
- [ ] ¿Todo está en conjetura, sin resultados propios colados?
- [ ] ¿`trazabilidad.py` y `articulo_docx.py verificar` pasaron sin ✗?
- [ ] ¿Toda cita de contenido tiene resumen completo (ninguna `RECORTADO`)?
- [ ] ¿Todas las citas van por clave y se exportó `CITADAS_[clave].ris`?
- [ ] ¿Citas, título de sección y extensión siguen el perfil de la revista?
- [ ] ¿Se humanizó la sección?

Al entregar, decir **qué hipótesis quedaron con respaldo escaso**, nombrándolas.
Y la línea de handoff:

> ARTICULO_[clave]_v3.docx (+ _RESPALDO) — Introducción y Revisión de la
> literatura, con `TRAZABILIDAD_[clave].xlsx`, `inventario.json` y
> `CITADAS_[clave].ris` actualizados. Sigue la **Fase 4**, skill
> `articulo-fase4-metodos`: súbele los dos Word, la Matriz,
> `REVISTA_[clave].json`, `inventario.json` y **tu base de datos** (de ahí se
> calcula la Tabla 1; si es secundaria, también su diccionario). Si todavía no
> recogiste datos, antes pasas por `instrumento-investigacion` y
> `recoleccion-datos`.

## Errores que esta skill previene

1. Atribuir una teoría a un autor que no la menciona.
2. Sustentar una hipótesis con un estudio de dirección contraria.
3. Poner mediación sin ningún precedente de mediación.
4. Escribir el sustento como si los resultados ya existieran.
5. Exigir hipótesis a un estudio instrumental o cualitativo.
6. Cambiar los acrónimos o el término unificador respecto de la Introducción.
7. Meterle revisión de literatura a un artículo de revisión.
8. Dejar dos listas de referencias, un Word por sección o referencias
   tecleadas a mano en vez de claves.
9. Sustentar una hipótesis con resúmenes recortados que no dicen la dirección.

## Archivos de referencia

- `references/ruta.md` — Mapa único de la ruta (manda sobre todo).
- `references/estilo_preguntas.md` — Cómo se redactan preguntas y opciones.
- `references/literatura_e_hipotesis.md` — Teorías, acápites, sustento con
  control de dirección y variantes por tipo de estudio.
- `references/perfil_revista.md` — Perfil de la revista y Word de respaldo.
- `references/busqueda_bases.md` — Ecuaciones para la búsqueda complementaria.
- `references/trazabilidad.md` — La matriz cita por cita.
- `references/documento_en_cadena.md` — Cómo se une al .docx existente.
- `references/formato_docx.md` — Motor del Word, sintaxis del .md y entorno.
- `references/anti_ia.md` — Humanización de la sección.
- `references/estilos_cita.md` — APA 7, Chicago, IEEE y Vancouver.
- `references/fuentes_y_citas.md` — Vías de fuentes, citas por clave, vuelta
  al gestor.
- `scripts/referencias.py` — Alta por DOI verificado y exportación de lo citado.
- `scripts/inventario_fuentes.py` — Inventario con IDs estables (`--previo`).
- `scripts/trazabilidad.py` — Agrega y verifica filas de la trazabilidad.
- `scripts/articulo_docx.py` — Esquema, agregar y verificar el Word.
- `scripts/medir_estilo.py` — Medición opcional de la prosa.

## Tarjeta de continuidad (al cerrar la fase, siempre)

El último mensaje de la fase termina con esta tarjeta, en un bloque de código
para que el usuario la copie. En modo A se guarda además como `ESTADO_[clave].md`.
Máximo 150 palabras; solo datos, sin prosa.

```
TARJETA · Ruta del Artículo · [clave]
Fase cerrada: N · [nombre]      Siguiente: [la que indica ruta.md] · [skill]
Tipo y diseño: ...
Revista: ... · Perfil: REVISTA_[clave].json · Estilo de cita: ... · Límite: ... palabras
Término unificador: ... (solo empíricos)
Archivos vigentes: ARTICULO_[clave]_vN.docx (+ _RESPALDO) · MATRIZ_... · TRAZABILIDAD_...
Fuentes: inventario.json (claves) · Cifras: SALIDAS_[clave].csv/.md (sin redondear)
Reenvío: ARTICULO_[clave]_vN_[revista].docx y REVISTA_[clave]_[revista].json
Decisiones que no se reabren: ...
Pendientes [POR CONFIRMAR]: ...
```

Indicación al usuario, en una línea: *abre un chat nuevo para la siguiente
fase y pega esta tarjeta junto con el último Word*. Un chat por fase ahorra
tokens y evita que el modelo se pierda.
