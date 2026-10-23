---
name: revision-fase2-introduccion
description: >-
  Fase 2 de la Ruta del Artículo de Revisión: redacta la Introducción y crea el
  Word del artículo, que crece en cada fase. Guía la búsqueda de antecedentes en
  Scopus, Web of Science y Google Académico con ecuación lista y exportación en
  RIS o CSV con resumen, inventaría las fuentes y separa las citables por
  contenido. Redacta los cinco bloques adaptados a una revisión: problema,
  necesidad de la revisión (no hay revisiones previas, están desactualizadas o
  se contradicen), contexto regional, pregunta y objetivos de la revisión, y
  aporte. Entrega la matriz de trazabilidad. Nunca inventa citas, cifras ni
  fuentes. Cita por clave desde el Zotero o Mendeley del investigador, la
  plataforma Acosta o DOI verificado. Escribe en español con la norma, el estilo
  de cita y el formato de la revista destino, humaniza la sección y entrega la
  versión de la revista y su respaldo neutro. ACTIVAR con introducción de mi
  revisión, justificar mi revisión sistemática, antecedentes de mi revisión, o
  cuando suban la Matriz de la Fase 1.
license: Proprietary
metadata:
  version: "3.2.0"
  fase: "2"
  ruta: "Ruta del Artículo de Revisión — Acosta | IA & Research"
---

# Fase 2 — Introducción

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

Es la **primera fase que escribe texto del artículo**, y la que crea el
documento Word que va a crecer hasta el envío. Se escribe en español y **con la
norma de la revista destino** desde ya: su estilo de cita, sus títulos de
sección y su límite de palabras (`REVISTA_[clave].json`).

Hace tres cosas que el investigador novato no sabe hacer solo: armarle la
ecuación de búsqueda para cada base de datos, conseguir cifras reales para
sostener la problemática, y escribir los cinco bloques en el orden que espera un
revisor.

### La ruta completa

```
  Fase 0 · Tema y orientación
  Fase 1 · Matriz de estrategia
  Fase 2 · Introducción                ← estás aquí
  Fase 4 · Métodos
  Fase 5 · Resultados
  Fase 6 · Discusión
  Fase 7 · Conclusiones y abstract
  Fase 8 · Adaptación a la revista y envío
  Fase 9 · Respuesta a revisores
```

Insumos, entregables y quién decide cada dato: `references/ruta.md`, que manda
sobre este archivo si algo no coincide.

## Regla del acompañamiento: el investigador es novato

- **Un paso por turno.** Nunca dos.
- **Ninguna pregunta con jerga sin salida.** Toda pregunta técnica lleva como
  última opción `"No me queda claro, ponme ejemplos"`, y si sigue trabado,
  `"Prefiero que alguien me lo explique"`, que responde con el WhatsApp del
  equipo (+51 923 095 940) y deja el punto pendiente **sin bloquear el flujo**.
- **Cuando se le pide que haga algo fuera del chat** (buscar en Scopus,
  exportar) se le dan las instrucciones completas y literales: dónde hacer clic,
  qué casilla marcar, qué pegar.
- **Si vuelve con algo distinto de lo pedido**, se trabaja con lo que trajo y se
  le dice qué falta.
- Redacción de las opciones de menú (máximo cuatro): `references/estilo_preguntas.md`,
  que se lee al empezar.

## Regla de oro: veracidad absoluta

1. **Cita de contenido solo con resumen completo y real.** Se le atribuye a una
   fuente un hallazgo, una cifra o una definición únicamente si su resumen
   completo está en el inventario. Los resúmenes generados por IA (ScopusAI y
   similares) sirven para orientarse, **no para citar**.
2. **Resumen recortado = sin resumen.** Si el inventario marca `RECORTADO`
   (p. ej. `buscar_fuentes`, OpenAlex o `buscar_en_la_literatura` entregan ~400
   caracteres), la fuente **no se cita por contenido** hasta conseguir el
   resumen completo (si llega el export de Scopus/WoS con el mismo DOI, el
   inventario lo completa sin cambiar la clave):
   abrir su DOI y copiar el resumen literal de la página de la revista, o pedir
   al investigador el export de Scopus/WoS de ese registro. El resumen completo
   se pega en el campo `abstract` de ese ID en `inventario.json` (el ID no
   cambia) y se marca citable.
3. **Cita a nivel de título.** Sin resumen completo, la fuente se menciona por
   lo que el título respalda, sin atribuirle resultados.
4. **Ninguna cifra de memoria.** Las estadísticas se buscan en esta sesión y se
   reportan con fuente y año. Ver `references/estadisticas_y_ods.md`.
5. **Nada se inventa**: ni nombres, ni años, ni revistas, ni DOI, ni metas de
   los ODS. Lo que falte se marca `[POR CONFIRMAR: ...]`.
6. **Ninguna afirmación cuelga de una cita que no la sostiene.** Por eso el
   Paso 7 es obligatorio.

## Economía de la sesión

1. Cada archivo de `references/` se lee **solo en su paso**.
2. En el chat va lo que el investigador necesita decidir; el texto completo vive
   en el .docx. **Nada se escribe dos veces.**
3. Sin prólogos ni párrafos de transición entre pasos.
4. El documento se comprueba con `articulo_docx.py verificar`, no con revisión
   visual.

## Entorno

Scripts en `scripts/` de esta skill (si no aparecen, buscar `articulo_docx.py`
por nombre). Archivos y caso sin código: `references/formato_docx.md`, Entorno.

## Lo que esta skill NO hace

- **No define objetivos ni hipótesis.** Eso es Fase 1.
- **No arma ni cambia la ecuación de búsqueda del corpus.** Es de la Fase 1
  (está en la Matriz) y la Fase 4 la reporta literal. Aquí solo se hace una
  búsqueda de contexto para escribir la Introducción.
- **No busca dentro de Scopus ni Web of Science por el investigador**: son bases
  suscritas. Le arma la ecuación y le explica cómo exportar.
- **No es para tesis.** Si aparecen "capítulo I", "asesor" o "jurado", derivar a
  `problema-y-objetivos`.

---

# Flujo

## Paso 0 — Bienvenida

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Ruta del Artículo de Revisión · Fase 2

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

¡Bienvenido a las Skills de Acosta!

Estás en la **Fase 2 — Introducción**. Aquí sí escribimos.

Vamos en dos tiempos. Primero te armo las ecuaciones de búsqueda para Scopus, Web of Science y las demás bases, y te digo exactamente cómo exportar los resultados. Después, con esos archivos en la mano, redactamos.

Ese orden importa: sin fuentes reales no se escribe una introducción, se inventa una.

Empecemos por lo que ya tienes.
```

## Paso 1 — Insumos

```
¿Qué traes?
- "La matriz de la Fase 1"
- "Tengo objetivos e hipótesis, pero no la matriz"
- "Tengo la introducción escrita en otro lado"
- "Vengo directo, sin nada de eso"
```

Qué se hace con cada respuesta:

- **"La matriz de la Fase 1"** → leer la Matriz, la Ficha y el perfil de la
  revista. Si además trae exports con resumen, saltar al Paso 3 (y volver al
  Paso 2 solo para exportar si el inventario muestra resúmenes ausentes o
  recortados); si no, Paso 2.
- **"Tengo objetivos e hipótesis, pero no la matriz"** → pedir en **una sola
  pregunta** los datos mínimos: tipo de estudio, objetivos (e hipótesis si las
  hay), constructos, población y país, y revista destino. Con eso se sigue al
  Paso 2; no se le devuelve a la Fase 1.
- **"Tengo la introducción escrita en otro lado"** → pedir el texto o el .docx
  (si es .docx, leerlo con `articulo_docx.py texto`). Contrastarlo con los cinco
  bloques y decirle en tres líneas qué bloque falta o flojea. Sus citas también
  pasan por el inventario: se piden los exports de esas fuentes (Paso 2 solo
  para exportar) y se sigue en el Paso 3. Al final su texto corregido entra al
  Word con `articulo_docx.py nuevo --perfil`, para unificar el formato.
- **"Vengo directo, sin nada de eso"** → si ya sabe qué quiere estudiar y con
  qué objetivo, la misma pregunta única de datos mínimos y se sigue. Si todavía
  no tiene objetivo, la Introducción no se puede escribir: derivar a
  `revision-fase1-matriz-de-estrategia` y terminar.

De la **Matriz** salen constructos, objetivos, preguntas, hipótesis, **tipo de
estudio y diseño** (primera hoja, *Diseño y muestra* o *Diseño de la revisión*)
y la ecuación de búsqueda del corpus.
De la **Ficha**, población y país. Del **perfil `REVISTA_[clave].json`**
(Fase 0): estilo de cita, título exacto de la sección de introducción en
`estructura` y límite de palabras. **Nada de eso se vuelve a preguntar.** Si
falta el perfil, se pide; si tampoco existe, se crea en un paso con
`references/perfil_revista.md` antes de redactar.

Decirle en una línea qué le queda por delante: una revisión **no lleva Fase 3**;
de aquí pasa directo a Métodos, donde se reporta el protocolo. Si la Matriz dice
que es un estudio con datos propios, decirle que esa ruta está en el otro
paquete (Ruta del Artículo Empírico) y terminar.

## Paso 2 — Búsqueda en las bases de datos

Procedimiento completo, con la sintaxis de cada base y la exportación, en
`references/busqueda_bases.md`.

**La ecuación del corpus ya está en la Matriz (Fase 1)**; no se rehace. Para
la Introducción basta una **búsqueda de contexto**: la ecuación de la Matriz
con el filtro de revisiones (detalle en `references/busqueda_bases.md`), para
reunir las revisiones previas que justifican la nueva, más los registros del
corpus que sirvan de contexto. Si el corpus ya está exportado, no se pide otro
export grande: se inventaría y se eligen de ahí las revisiones previas.

**Un formato por base**: Scopus en RIS (o CSV), WoS en texto plano *Full
Record*. Nunca el mismo export en dos o tres formatos: se duplican fuentes.
Sin resumen, esas fuentes no se podrán citar por contenido. **Sin fuentes no se
avanza.** Si la ecuación devolvió cero o miles, ajustarla con él.

**Por dónde llegan las fuentes** (`references/fuentes_y_citas.md`; las tres
vías se combinan):

```
¿Dónde tienes o buscas tus fuentes?
- "Exporto de Scopus o Web of Science con tu ecuación"
- "Ya las tengo en mi Zotero o en mi Mendeley"
- "Usa la plataforma Acosta, la tengo conectada"
- "No me queda claro, ponme ejemplos"
```

- **(a) Plataforma Acosta**: `buscar_fuentes` con los términos de la tabla
  (busca en la biblioteca de Acosta y en la del investigador: su Zotero o
  Mendeley conectado y sus exports), `mis_fuentes`, `ampliar_desde_mis_fuentes`
  para bola de nieve. Las fichas se pegan **tal cual** en `fichas_acosta.txt`
  y conservan su clave AR. `anadir_a_mis_fuentes` solo con DOI salido de una
  búsqueda.
- **(b) Su gestor**: exportar la colección del artículo de Zotero o Mendeley en
  **RIS** (o BibTeX).
- **(c) Búsqueda web del modelo**: solo entra con **DOI verificado**
  (`referencias.py doi`); sin DOI verificable, no entra.

Preguntar también qué gestor usa (Zotero o Mendeley): ahí vuelve lo citado al
cerrar la fase.

## Paso 3 — Inventario de fuentes

```bash
python3 scripts/inventario_fuentes.py scopus.ris wos.txt zotero.ris fichas_acosta.txt --out inventario.json
python3 scripts/referencias.py doi 10.xxxx/yyyy --inventario inventario.json   # vía (c)
```

Un archivo por base o vía, en el formato del Paso 2. El script quita duplicados,
asigna IDs estables (F001…) y marca cada resumen `OK`, `RECORTADO` o `FALTA`.
Si un archivo sale `FORMATO NO RECONOCIDO`, ese archivo se inventaría a mano:
**no se adivina el contenido de un registro**. Modo C: inventario a mano en una
tabla Markdown (ID, cita, ¿resumen completo?).

Mostrar en cuatro líneas: cuántas fuentes tienen resumen completo, cuántas
recortado (con la regla de oro 2 para completarlas), cuántas ninguno, cuántos
duplicados se quitaron, y la **cobertura por constructo** contada a mano con
`--tabla` (si un constructo no tiene ninguna fuente citable, avisar ahora). Si
las citables por contenido son menos de ocho, decirlo y ofrecer seguir o volver
al Paso 2. Si después trae más exports, se corre de nuevo con
`--previo inventario.json`: los IDs existentes no cambian.

## Paso 4 — Estadísticas y ODS

Reglas en `references/estadisticas_y_ods.md`. Buscar en la web una o dos cifras
internacionales y una o dos nacionales, **cada una con fuente, año y ámbito**,
comprobadas en la fuente original (no en el resumen del buscador); si no
aparece, `[POR CONFIRMAR: dato nacional sobre X]`. Proponer **un solo ODS**
que encaje de verdad, con una oración que diga en qué se conecta. Mostrarle las
cifras antes de redactar.

## Paso 5 — Redactar los cinco bloques

Detalle en `references/cinco_bloques.md`.

```
1 · Problema y su relevancia internacional   (con cifra y ODS)
2 · Necesidad de la revisión                 (revisiones previas con su año)
3 · Contexto regional o nacional
4 · Pregunta(s) de revisión y objetivo, en prosa, sin hipótesis
5 · Aporte teórico y práctico
```

La Introducción puede citar estudios del corpus **solo como contexto**, sin
adelantar la síntesis de Resultados.

Todo en prosa continua, sin subtítulos internos ni viñetas, escrito en un
`intro.md` con la sintaxis de `references/formato_docx.md`: título provisional
con `[TITULO]` y la sección con el **título exacto** que da la `estructura` del
perfil (p. ej. `# Introducción` o `# Introduction`). Las citas van **por clave
del inventario**: `[F012]`, narrativa `[AR51541814:n]`, con página
`[F012:p. 45]`, agrupada `[F012][F020]`. **No se escribe `# Referencias`**: el
motor convierte las claves al estilo del perfil y genera la lista
(`references/fuentes_y_citas.md`). Extensión: 15–20 % del `limite_palabras`
del perfil; decírsela antes de redactar.

Entregar los bloques **de dos en dos** para que los revise sobre la marcha. Un
novato que recibe tres páginas de una vez no corrige nada.

## Paso 6 — Humanizar la sección

Según `references/anti_ia.md`: `humanizador-academico` sobre `intro.md` (una
ronda, 1-2 bloques, el autor aprueba cada bloque en un mensaje); si no está, el
servidor (`humanizar_mi_documento`); si no hay ninguno, la lista de control.
En la Introducción vigilar sobre todo el 1 (inflar la importancia), el 3
(lenguaje promocional) y el 4 (atribución vaga). En el chat, una línea: qué se
tocó.

## Paso 7 — Matriz de trazabilidad

Obligatoria. Siete columnas y criterios en `references/trazabilidad.md`. Escribir
las filas (una por cita y una por cifra) en `filas.json` y:

```bash
python3 scripts/trazabilidad.py crear --out TRAZABILIDAD_[clave].xlsx --filas filas.json --inventario inventario.json
```

Si marca ✗ (frase que no está en el resumen, fuente sin resumen completo usada
por contenido), se corrige el texto y se vuelve a correr. **No existe la
categoría "aproximada".** Modo C: la misma tabla de siete columnas en Markdown.

## Paso 8 — Crear el Word

Reglas en `references/documento_en_cadena.md`; motor y sintaxis en
`references/formato_docx.md`; perfil en `references/perfil_revista.md`.

```bash
python3 scripts/articulo_docx.py nuevo --md intro.md --out ARTICULO_[clave]_v2.docx --perfil REVISTA_[clave].json --fuentes inventario.json
python3 scripts/articulo_docx.py verificar ARTICULO_[clave]_v2.docx --perfil REVISTA_[clave].json --fuentes inventario.json
```

`nuevo` produce `ARTICULO_[clave]_v2.docx` (formato de la revista) y
`ARTICULO_[clave]_v2_RESPALDO.docx` (formato neutro, mismo texto). Contienen
título provisional, Introducción y Referencias (generadas con las citadas),
sin encabezados vacíos de secciones futuras. Si `verificar` marca ✗ (p. ej. una
clave sin fuente: se agrega por las vías a–c y se regenera), se corrige el .md
y se vuelve a generar. Luego, lo citado vuelve a su gestor:

```bash
python3 scripts/referencias.py exportar --inventario inventario.json --docx ARTICULO_[clave]_v2.docx --ris CITADAS_[clave].ris
```

(Zotero o Mendeley: importar `CITADAS_[clave].ris` en la colección del
artículo.) Modo C: la sección en un bloque listo para pegar en
`PLANTILLA_ARTICULO.docx`, con las claves; al final, la lista de referencias
formateada a mano en el estilo del perfil y un bloque RIS de las citadas.

## Paso 9 — Cierre

- [ ] ¿Los cinco bloques están, en orden y en prosa continua?
- [ ] ¿Cada cifra tiene organismo, año y ámbito? ¿El ODS es uno solo y encaja?
- [ ] ¿Toda cita de contenido tiene su resumen **completo** en el inventario?
- [ ] ¿Todas las citas van por clave, sin `# Referencias` a mano, y se
      exportó `CITADAS_[clave].ris`?
- [ ] ¿Citas, título de sección y extensión siguen el perfil de la revista?
- [ ] ¿`trazabilidad.py` y `articulo_docx.py verificar` pasaron sin ✗?
- [ ] ¿Se humanizó la sección?
- [ ] ¿Quedó algún `[POR CONFIRMAR]` sin listar al investigador?

Entregar `ARTICULO_[clave]_v2.docx` y `ARTICULO_[clave]_v2_RESPALDO.docx`,
`TRAZABILIDAD_[clave].xlsx`, `inventario.json` y `CITADAS_[clave].ris`, con la
línea de handoff:

> ARTICULO_[clave]_v2.docx (+ _RESPALDO) — título provisional, Introducción y
> Referencias. Sigue la **Fase 4**, skill `revision-fase4-metodos`: súbele los
> dos Word, la Matriz (con la ecuación y los criterios), `REVISTA_[clave].json`
> y tus conteos de búsqueda y cribado. Ahí el .docx pasa a `_v4`.

## Errores que esta skill previene

1. Mandar al investigador a Scopus sin decirle qué escribir.
2. Exportar sin el resumen, o en tres formatos a la vez, y descubrirlo tarde.
3. Citar por contenido una fuente cuyo resumen llegó recortado.
4. Inventar una cifra nacional porque el párrafo la pedía.
5. Forzar un ODS o citar una meta con el número equivocado.
6. Atribuirle a un autor un hallazgo que su resumen no dice.
7. Declarar el vacío en vez de demostrarlo.
8. Escribir en APA cuando la revista pide otro estilo, y convertirlo al final;
   o teclear citas y referencias a mano en vez de citar por clave.
9. Volver a preguntar lo que ya está en la Matriz, la Ficha o el perfil.
10. Terminar con varios Word sueltos en vez de uno que crece.

## Archivos de referencia

- `references/ruta.md` — Mapa único de la ruta (manda sobre todo).
- `references/estilo_preguntas.md` — Cómo se redactan preguntas y opciones.
- `references/perfil_revista.md` — Perfil de la revista y Word de respaldo.
- `references/busqueda_bases.md` — Términos, ecuaciones y exportación por base.
- `references/estadisticas_y_ods.md` — Cifras verificables y vínculo con un ODS.
- `references/cinco_bloques.md` — Los cinco bloques de la Introducción.
- `references/trazabilidad.md` — La matriz cita por cita.
- `references/documento_en_cadena.md` — El .docx único que crece fase a fase.
- `references/formato_docx.md` — Motor del Word, sintaxis del .md y entorno.
- `references/anti_ia.md` — Humanización de la sección.
- `references/estilos_cita.md` — APA 7, Chicago, IEEE y Vancouver.
- `references/fuentes_y_citas.md` — Tres vías de fuentes, citas por clave y
  vuelta a Zotero o Mendeley.
- `scripts/referencias.py` — Alta por DOI verificado y exportación de lo citado.
- `scripts/inventario_fuentes.py` — Inventario de fuentes con IDs estables.
- `scripts/trazabilidad.py` — Crea y verifica la matriz de trazabilidad.
- `scripts/articulo_docx.py` — Crea y verifica el Word del artículo.
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
