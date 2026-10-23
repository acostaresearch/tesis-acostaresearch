---
name: articulo-fase1-matriz-de-estrategia
description: >-
  Fase 1 de la Ruta del Artículo Empírico: arma el esqueleto antes de escribir.
  Define el diseño (correlacional, comparativo, regresión, experimental, panel,
  SEM, cualitativo, mixto o validación de escala) y si los datos son primarios o
  de una base secundaria, objetivo general y específicos, preguntas, hipótesis
  cuando el diseño las admite, operacionalización de cada variable hasta el
  instrumento o la variable de la base, la muestra y el análisis previsto. Busca
  artículos parecidos para ver qué diseños e instrumentos se usan. Cierra con un
  chequeo de coherencia
  objetivo-pregunta-hipótesis-variable-instrumento-análisis y entrega la Matriz
  de Estrategia en Excel. Nunca inventa instrumentos, autores de escalas ni
  criterios de muestra. ACTIVAR con matriz de consistencia, matriz de
  estrategia, objetivos e hipótesis de mi artículo, operacionalización de
  variables, qué diseño uso, o cuando traen la Ficha de Orientación de la Fase
  0.
license: Proprietary
metadata:
  version: "2.2.0"
  fase: "1"
  ruta: "Ruta del Artículo Empírico — Acosta | IA & Research"
---

# Fase 1 — Matriz de Estrategia

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

Es el **esqueleto de la investigación**. La Fase 0 dejó el tema y la revista;
aquí se define qué se va a hacer exactamente, antes de escribir la primera
línea del artículo.

Existe porque el error más caro no es escribir mal: es escribir bien un estudio
que no cuadra. Objetivos que no coinciden con las hipótesis, hipótesis que la
muestra no puede probar, variables sin instrumento, análisis que no responde la
pregunta. Todo eso se detecta aquí, en una tabla, y no en la revisión por pares.

Sale de aquí con la **Matriz de Estrategia** en Excel (`MATRIZ_[clave].xlsx`).

### La ruta completa

```
  Fase 0 · Tema y orientación
  Fase 1 · Matriz de estrategia       ← estás aquí
  Fase 2 · Introducción
  Fase 3 · Revisión de la literatura
  Fase 4 · Métodos
  Fase 5 · Resultados
  Fase 6 · Discusión
  Fase 7 · Conclusiones y abstract
  Fase 8 · Adaptación a la revista y envío
  Fase 9 · Respuesta a revisores
```

Insumos, entregables y cobertura por tipo de estudio: `references/ruta.md`, que
manda sobre este archivo.

## Reglas de oro (innegociables)

1. **Cero invención.** Ni instrumentos, ni autores de escalas, ni años, ni
   criterios de tamaño muestral, ni artículos, ni bases de datos que el
   investigador no tenga. Todo sale de la búsqueda hecha en esta sesión o de lo
   que el investigador aporta.
2. **`[POR CONFIRMAR]` no es comodín para no preguntar.** Se reserva para datos
   externos: permisos, tamaño real de la población, disponibilidad de una
   escala, código de registro de un protocolo. Lo que el investigador puede
   contestar, se le pregunta.
3. **Coherencia antes que cantidad.** Una matriz con tres objetivos alineados
   vale más que una con seis que no cierran.
4. **Validación humana al final.** Lo que sale de aquí es propuesta y la revisan
   el investigador y sus coautores.

## Economía de la sesión

1. Cada archivo de `references/` se lee **solo en su paso**, y no se abre si el
   paso no aplica a su diseño.
2. **Lo que está en la Ficha y en `REVISTA_[clave].json` no se vuelve a
   preguntar**: tema, población, ámbito, año, tipo de estudio, revista,
   estructura, límite de palabras y estilo de cita (del perfil), término
   unificador (de la Ficha). Se confirma en una línea.
3. En el chat va la versión corta; el detalle vive en el Excel. **Nada se
   escribe dos veces.**
4. Sin prólogos, sin resumir lo que el investigador acaba de decir, sin párrafos
   de transición. Un paso por turno.
5. Esta fase casi no produce prosa. Si escribe un párrafo, sin rellenos ni
   frases de chatbot (la lista de patrones es `anti_ia.md`, de las fases 2 a 9).

## Preguntas

Toda pregunta usa la herramienta interactiva del entorno (`AskUserQuestion` en
Claude Code y Cowork, `ask_user_input_v0` en claude.ai); si el cliente no tiene
ninguna, opciones numeradas en el chat. Máximo 4 opciones y 3 preguntas por
bloque.

**Cómo se redactan las opciones está en `references/estilo_preguntas.md`, y se
lee al empezar.** La prueba: leerla en voz alta como si la dijera el
investigador. Si él no hablaría así, se reescribe.

Rescate en toda pregunta técnica: última opción `"No me queda claro, ponme
ejemplos"`, y si sigue trabado, `"Prefiero que alguien me lo explique"`, que
responde con el WhatsApp del equipo (+51 923 095 940) y deja el punto pendiente
sin bloquear.

## Lo que esta skill NO hace

- **No redacta.** La Introducción es la Fase 2.
- **No redacta la Revisión de la literatura.** Es la Fase 3.
- **No demuestra el vacío de conocimiento** con resúmenes verificados: Fase 2.
- **No construye el instrumento** ni elabora ítems. Aquí se identifica cuál
  existe y quién lo validó; construirlo o adaptarlo es la skill
  `instrumento-investigacion` (ver `references/ruta.md`, "Skills de apoyo").
- **No analiza datos** ni ejecuta la búsqueda definitiva en bases.
- **No es para tesis.** Si aparecen "capítulo I", "asesor" o "jurado", derivar a
  `problema-y-objetivos` y explicar la diferencia.

---

# Flujo

## Paso 0 — Bienvenida

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Ruta del Artículo Empírico · Fase 1

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

¡Bienvenido a las Skills de Acosta!

Estás en la **Fase 1 — Matriz de Estrategia**. Aquí armamos el esqueleto: qué te propones, qué preguntas respondes, con qué diseño y con qué variables.

Es la fase que menos se ve y la que más rechazos evita. Un artículo con objetivos que no cuadran con el análisis se cae en revisión aunque esté bien escrito.

Empecemos.
```

Seguir directo al Paso 1.

## Paso 1 — Insumos

Si en su primer mensaje ya subió la Ficha u otro material, no se pregunta: se
lee y se sigue. Si no:

```
¿Con qué llegas?
- "Traigo la Ficha de la Fase 0, te la subo"
- "No tengo Ficha, te cuento mi tema"
- "Ya tengo objetivos escritos, quiero que los revises"
- "Ya recogí los datos o ya tengo el corpus"
```

| Llega con | Qué se hace |
|---|---|
| La Ficha y `REVISTA_[clave].json` | Leerlos; confirmar en una línea tema, tipo de estudio, revista y límite de palabras; seguir al Paso 2 sin repreguntar |
| La Ficha sin el perfil | Tomar revista, cita y límite de la sección 7 de la Ficha; el perfil se arma luego con la Fase 0 (Paso 5h) o, como tarde, antes de la Fase 2 |
| Sin Ficha | Pedir en **una sola pregunta** lo mínimo: tema en una frase (con población, ámbito y año), tipo de estudio, revista destino y estilo de cita si los tiene. No se le devuelve a la Fase 0 |
| Objetivos escritos | Se toman como borrador y se pasan por los Pasos 4 y 8 |
| Datos ya recogidos o corpus exportado | La matriz **registra lo que se hizo** (instrumento aplicado, muestra real, bases y fecha de búsqueda reales), no propone otra cosa. Lo que ya no se puede cambiar se anota como limitación |
| Una base secundaria ya elegida | Se registra la base, su año u ola, sus variables, su diccionario y su ponderador; no se propone instrumento |
| Viene de su tesis | Elegir el objetivo más fuerte; una tesis no se convierte en artículo recortándola |

## Paso 2 — Diseño de investigación

Qué exige cada diseño, qué objetivos e hipótesis admite y qué análisis le
corresponde: `references/disenos.md` (se lee aquí). Si la Ficha ya trae el tipo
de estudio, solo se pregunta el nivel que falte.

Nivel 1:

```
¿Qué vas a hacer con tus datos?
- "Medir variables y ver cómo se relacionan"
- "Probar si algo funciona, con grupo de comparación"
- "Entender experiencias, sin medir"
- "Comprobar si un cuestionario mide bien"
```

Nivel 2, según lo que eligió:

| Respuesta | Segundo menú |
|---|---|
| Medir y relacionar | Descriptivo · Correlacional o comparativo · Predictivo (regresión, multinivel, panel) · Modelo estructural (PLS-SEM o CB-SEM) |
| Probar si funciona | Preexperimental · Cuasiexperimental · Experimental puro · No me queda claro, ponme ejemplos |
| Entender experiencias | Fenomenológico · Estudio de caso · Teoría fundamentada · Investigación-acción |
| Cuestionario | Validación de escala con propiedades psicométricas (no lleva hipótesis sustantivas) |

Si las dos ramas (medir y entender) le interesan, es mixto: se arma cada rama y
se dice cómo se integran.

Si la Ficha no dice **de dónde salen los datos**, se pregunta: propios
(encuesta, test, experimento) o **secundarios** (encuesta nacional, base
pública o institucional, panel, serie). Con secundarios, la matriz es del tipo
`secundarios` (Paso 9) y no hay instrumento sino base.

Si dice que no recoge datos y va a revisar lo publicado: ese tipo de artículo
está en el otro paquete, la **Ruta del Artículo de Revisión**.

Al cerrar la elección, decir en tres líneas qué exige ese diseño y **qué
hipótesis admite o no admite**. No adornar.

## Paso 3 — Papers de referencia

Procedimiento en `references/papers_referencia.md` (se lee aquí).

Buscar en la web, en español y en inglés, y reportar **entre tres y cinco
artículos parecidos realmente encontrados**, con autor, año, revista y enlace.
De cada uno: diseño, instrumentos y quién los validó (o la base de datos que
usó), tamaño y tipo de muestra, análisis aplicado.

Solo se anota lo que el resultado muestra; si solo se tiene el título, nada
más. Si aparece un estudio que ya hizo lo mismo en la misma población (o una
revisión reciente con la misma pregunta), decirlo ahora.

## Paso 4 — Objetivos y preguntas

Reglas, verbos por alcance y errores típicos en
`references/objetivos_y_preguntas.md` (se lee aquí).

- **Un objetivo general**, con el verbo del alcance, las variables (o el
  concepto revisado), la población y el ámbito. Sale casi entero de la frase del
  tema de la Ficha.
- **Entre dos y cuatro específicos.** Si el caso trae más, primero se agrupan
  (un específico puede reunir varias hipótesis); si quedan cinco, se aceptan
  avisando. Más de cinco, no. Se contrasta con `limite_palabras` del perfil.
- **Una pregunta por objetivo, en espejo.** Si un objetivo no se puede convertir
  en pregunta, está mal formulado.

**Checkpoint:** cada específico tiene su pregunta y aporta al general. Si uno no
aporta, sobra. Decirlo.

## Paso 5 — Hipótesis y modelo

Solo si el diseño las admite. En cualitativo y en validación de escala **no se
formulan hipótesis sustantivas** (la validación lleva un modelo de medida
esperado); se explica en una línea en vez de inventarlas.

Cuando aplican:

- **Una hipótesis, una relación.** Nada de hipótesis con dos verbos.
- **Dirección justificada** por los papers del Paso 3. Si la evidencia es
  mixta, se formula reconociendo la tensión.
- **Estilo de conjetura.** Todavía no hay datos.
- **Coherencia con el diseño.** Transversal admite modelo direccional pero no
  lenguaje causal. El término unificador viene de la Ficha y no cambia.

Si hay modelo, entregarlo también como esquema en texto plano:

```
        H3
   X ─────────→ Y
   │            ↑
   │ H1         │ H2
   └────→ M ────┘
   H4: M media la relación entre X e Y
```

Advertencia obligatoria si aparece un mediador: **necesita precedentes de
mediación**, no dos correlaciones sueltas.

## Paso 6 — Operacionalización

Columnas y reglas en `references/operacionalizacion.md` (se lee aquí).

Por cada variable: definición conceptual **con su fuente**, definición
operacional, dimensiones, indicadores, escala de medición, **instrumento
propuesto con su autor y año**, y número de ítems si se conoce. En cualitativo,
categorías y subcategorías; en validación, la escala y sus dimensiones. Con
**datos secundarios**, en vez de instrumento: fuente de datos, variable de la
base (código), año u ola, cómo se construye o recodifica, diccionario y factor
de expansión.

La fuente del instrumento (o de la base) se anota **con su clave** si ya está
en el inventario o salió de `buscar_fuentes` (`[F012]`, `[AR51541814]`), o con
autor, año y DOI; así la Fase 4 la cita sin buscarla otra vez
(`fuentes_y_citas.md`, en las fases 2 a 9).

1. **El instrumento propuesto sale del Paso 3 o del investigador.** Si ninguna
   de las dos fuentes lo da, la celda queda `[POR CONFIRMAR: instrumento para
   esta variable]`. **Jamás se inventa una escala ni se le atribuye a un autor.**
2. **Adaptar una escala validada y citarla es mejor que construir una.** Si una
   variable no tiene instrumento, se presentan las salidas: cambiar la variable,
   convertir el estudio en validación de escala o construir el instrumento.
   Si los datos **ya se recogieron con una escala propia** sin validación
   publicada, se registra así y se declara como limitación (ver
   `operacionalizacion.md`).

## Paso 7 — Muestra

Población, muestra prevista, tipo de muestreo y criterios de inclusión y
exclusión.

**Sobre el tamaño, honestidad estricta.** No se afirma de memoria ningún mínimo:
se toman como referencia los tamaños de los papers del Paso 3 (diciendo de dónde
salen), el mínimo se justifica con una fuente citable o un cálculo (G*Power, o
el criterio de la revista) y queda `[POR CONFIRMAR: justificación del tamaño
muestral]` hasta que exista. Si el diseño no cabe en el acceso real (cuatro
constructos con sesenta casos), decirlo y simplificar ahora.

## Paso 8 — Chequeo de coherencia

El paso que justifica la fase entera. Es la hoja Objetivos de la matriz, una
fila por objetivo:

| Objetivo | Pregunta | Hipótesis | Variables | Instrumento o variable de la base | Análisis previsto |
|---|---|---|---|---|---|

El análisis previsto se elige **por la pregunta y la variable dependiente**, no
por costumbre: tabla «Qué análisis según la pregunta» de
`references/disenos.md` (correlación, comparación de grupos, regresión lineal,
logística, ordinal o de conteo, multinivel, panel, series, mediación o
moderación, SEM, validación de escala).

Cinco preguntas, una línea cada una en el chat:

1. ¿Cada objetivo tiene su pregunta?
2. ¿Cada hipótesis corresponde a un objetivo, y solo a uno?
3. ¿Cada variable de una hipótesis tiene instrumento (o variable en la base)?
4. ¿El análisis previsto responde efectivamente la pregunta?
5. ¿La muestra alcanza para ese análisis?

**Cualquier "no" se corrige aquí.** Cuesta veinte minutos; en la revisión por
pares cuesta seis meses.

## Paso 9 — Matriz de Estrategia en Excel

Estructura en `references/excel_matriz.md` (se lee aquí). La matriz **siempre**
se genera con el script de esta skill, para que salga igual en cualquier sesión:

```bash
S=scripts/matriz_excel.py                 # dentro de la carpeta de esta skill
python3 $S --ejemplo <tipo> > matriz.json # esqueleto con los campos exactos
# rellenar matriz.json con lo decidido (nada de <...> sin reemplazar)
python3 $S --json matriz.json --out MATRIZ_[clave].xlsx
```

`<tipo>` es `cuantitativo`, `secundarios` (cuantitativo con base existente:
hoja 1 con `fuente_datos`, `acceso`, `periodo`, `ponderador`, `variables_base`,
`diccionario`, `licencia`…), `cualitativo`, `escala`, `mixto` o `revision`.
`[clave]` es la de la Ficha. `--ejemplo` trae el JSON completo, con el formato
de cada clave (también `pendientes`). El script fija las cinco hojas, rechaza
celdas vacías o `<...>` y junta solos los `[POR CONFIRMAR]` en Pendientes. Si
marca ✗, se corrige el JSON y se vuelve a correr. El .xlsx se guarda donde el
cliente entrega archivos. Solo necesita `openpyxl`.

**Modo B:** `matriz_excel.py` no viene en *herramientas*; si el usuario no lo
puede subir desde la carpeta de esta skill, se entrega como en el modo C.
**Modo C:** la matriz como cinco tablas Markdown, una por hoja, con los mismos
encabezados, para pegar en Excel. Las fuentes se anotan con su clave si la hay,
o con autor, año y DOI.

## Paso 10 — Cierre

```
- [ ] Revisa la matriz con tus coautores antes de recoger un
       solo dato. Cambiar el diseño después cuesta la muestra.
- [ ] Consigue el instrumento de cada variable y confirma que
       puedes usarlo. Algunas escalas piden permiso del autor.
       Con datos secundarios: descarga la base y su diccionario,
       y anota versión, fecha y licencia.
- [ ] Justifica el tamaño de tu muestra con una fuente o un
       cálculo. Es lo primero que pregunta un revisor.
- [ ] Si recoges datos de personas, empieza ya el trámite del
       comité de ética.
- [ ] Si la revista no estaba clara en el perfil, confirma que
       tus objetivos caben en su límite de palabras.
```

Derivación:

> Con la matriz cerrada, sigue la **Fase 2 — Introducción**. Activa la skill
> **`articulo-fase2-introduccion`** y sube la Ficha, `REVISTA_[clave].json` y
> esta matriz.
> Ahí buscamos en las bases, demostramos el vacío con fuentes verificadas y
> redactamos la Introducción.
> La Revisión de la literatura viene después, en la Fase 3.

Si todavía no tiene datos, recordarle que entre esta fase y la Fase 4 puede
apoyarse en `instrumento-investigacion`, `recoleccion-datos` y
`analisis-datos-rstudio` (ver `references/ruta.md`).

## Errores que esta skill previene

1. Escribir la introducción sin saber qué se va a medir o revisar.
2. Objetivos específicos que no aportan al general.
3. Seis objetivos en un artículo de 6000 palabras, o preguntar de nuevo el
   límite que ya está en el perfil.
4. Hipótesis en un cualitativo, una validación de escala o una revisión.
5. Variables sin instrumento, descubierto en pleno trabajo de campo.
6. Inventar una escala o atribuírsela a un autor que no la hizo.
7. Un modelo que la muestra alcanzable no soporta.
8. Análisis que no responde la pregunta formulada.
9. Lenguaje causal en un diseño transversal.
10. Elegir SEM o encuesta propia por costumbre cuando la pregunta pide otro
    análisis u otra fuente de datos.
11. Una revisión sin bases accesibles, sin ecuación o sin segundo revisor.
12. Que cada matriz salga distinta: por eso hay un script único.

## Archivos de referencia (cada uno se lee solo en su paso)

| Archivo | Paso |
|---|---|
| `references/estilo_preguntas.md` — cómo se redactan preguntas y opciones | Al empezar |
| `references/ruta.md` — mapa único de las fases e insumos | Pasos 1 y 10, o si llega a mitad de camino |
| `references/disenos.md` — diseños, datos secundarios, hipótesis y análisis según la pregunta | Pasos 2 y 8 |
| `references/papers_referencia.md` — búsqueda de artículos parecidos | Paso 3 |
| `references/objetivos_y_preguntas.md` — verbos y regla del espejo | Paso 4 |
| `references/operacionalizacion.md` — columnas e instrumento propuesto | Paso 6 |
| `references/excel_matriz.md` — las cinco hojas | Paso 9 |
| `scripts/matriz_excel.py` — genera `MATRIZ_[clave].xlsx` | Paso 9 |

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
