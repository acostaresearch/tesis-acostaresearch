---
name: revision-fase1-matriz-de-estrategia
description: >-
  Fase 1 de la Ruta del Artículo de Revisión: arma el protocolo antes de buscar.
  Fija el tipo de revisión y su guía (PRISMA 2020, PRISMA-ScR o bibliométrica),
  la pregunta con PICO, PEO o PCC, los objetivos, los criterios de inclusión y
  exclusión, las bases de datos, el periodo, la ecuación de búsqueda de cada
  base, las variables de extracción, la evaluación de calidad y el análisis
  previsto (síntesis temática, metaanálisis o bibliometrix), y si conviene
  registrar el protocolo en PROSPERO u OSF. Cierra con un chequeo de coherencia
  pregunta-criterio-extracción-análisis y entrega la Matriz en Excel. Nunca
  inventa códigos de registro ni ecuaciones probadas. ACTIVAR con protocolo de
  mi revisión, pregunta PICO, criterios de inclusión, ecuación de búsqueda para
  la revisión, o cuando traen la Ficha de la Fase 0.
license: Proprietary
metadata:
  version: "2.2.0"
  fase: "1"
  ruta: "Ruta del Artículo de Revisión — Acosta | IA & Research"
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
- **No demuestra el vacío de conocimiento** con resúmenes verificados: Fase 2.
- **No analiza datos** ni ejecuta la búsqueda definitiva en bases.
- **No es para tesis.** Si aparecen "capítulo I", "asesor" o "jurado", derivar a
  `problema-y-objetivos` y explicar la diferencia.

---

# Flujo

## Paso 0 — Bienvenida

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Ruta del Artículo de Revisión · Fase 1

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
| Viene de su tesis | Elegir el objetivo más fuerte; una tesis no se convierte en artículo recortándola |

## Paso 2 — Diseño de investigación

Qué exige cada diseño, qué objetivos e hipótesis admite y qué análisis le
corresponde: `references/disenos.md` (se lee aquí). Si la Ficha ya trae el tipo
de estudio, solo se pregunta el nivel que falte.

```
¿Qué tipo de revisión es?
- "Sistemática, con PRISMA"
- "De alcance, para mapear lo que hay"
- "Bibliométrica, con indicadores"
- "No me queda claro, ponme ejemplos"
```

Segundo nivel solo si hace falta: la sistemática, ¿con metaanálisis o sin él?;
la bibliométrica, ¿sola o con síntesis sistemática de una parte del corpus
(mixta)?

Si va a recoger datos propios: ese tipo de artículo está en el otro paquete, la
**Ruta del Artículo Empírico**.

Al cerrar la elección, decir en tres líneas qué exige ese diseño y **qué
hipótesis admite o no admite**. No adornar.

## Paso 3 — Papers de referencia

Procedimiento en `references/papers_referencia.md` (se lee aquí).

Buscar en la web, en español y en inglés, y reportar **entre tres y cinco
artículos parecidos realmente encontrados**, con autor, año, revista y enlace.
Aquí se buscan **revisiones parecidas**. De cada una: tipo de revisión, guía de
reporte, bases y periodo, número de estudios incluidos, análisis (síntesis
temática, metaanálisis, bibliometrix, VOSviewer).

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

Una revisión **no lleva hipótesis**: lleva preguntas de revisión. La columna
dice "no aplica" y se explica en una línea. Este paso se salta.

## Paso 6 — Operacionalización

En una revisión, la operacionalización es la **hoja de diseño de la revisión**
y las **variables de extracción**. Detalle en `references/revision.md`
(secciones "Qué tipo de revisión es" y "Métodos"), que se lee aquí.

Se fija, campo por campo:

- Tipo de revisión y **guía de reporte** (PRISMA 2020, PRISMA-ScR, o la
  declaración propia de la bibliométrica).
- Pregunta de revisión en formato PICO, PEO o PCC.
- **Bases** a las que el investigador tiene acceso de verdad, **periodo**,
  idiomas y tipo de documento.
- **Ecuación de búsqueda literal por base** (obligatoria), con los términos de
  la Ficha. **Esta fase es su dueña:** el investigador la prueba en cada base y
  anota registros y fecha; la Fase 2 no la cambia (su búsqueda es otra, para
  escribir la Introducción) y la Fase 4 la reporta tal cual. Si una base queda
  sin probar, `[POR CONFIRMAR]` y va a Pendientes.
- **Registro del protocolo** (PROSPERO, OSF, INPLASY) o la decisión de no
  registrarlo. Nunca se inventa un código.
- Criterios de inclusión y exclusión, revisores del cribado y herramienta de
  calidad si es sistemática.
- **Análisis previsto**: síntesis temática o narrativa, metaanálisis, o
  bibliometrix y VOSviewer en la bibliométrica.
- **Variables de extracción**: qué se saca de cada estudio (autor, año, país,
  diseño, muestra, hallazgo) y a qué pregunta responde cada una.

## Paso 7 — Muestra

En una revisión la "muestra" es el corpus: se resolvió en el Paso 6 con bases,
periodo y criterios. Aquí solo se comprueba que el investigador puede exportar
de esas bases (acceso institucional) y que tiene un segundo revisor si es
sistemática. Lo que no tenga se dice ahora.

## Paso 8 — Chequeo de coherencia

El paso que justifica la fase entera. Es la hoja Objetivos de la matriz, una
fila por objetivo:

| Objetivo | Pregunta de revisión | Criterio de elegibilidad | Variable de extracción | Análisis previsto |
|---|---|---|---|---|

Cinco preguntas, una línea cada una en el chat:

1. ¿Cada objetivo tiene su pregunta de revisión?
2. ¿Cada pregunta tiene un criterio que decide qué estudios entran?
3. ¿Cada pregunta tiene al menos una variable de extracción que la responde?
4. ¿El análisis previsto (síntesis o indicadores) responde la pregunta?
5. ¿Las bases y el periodo alcanzan para ese análisis?

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
- [ ] Revisa la matriz con tus coautores antes de buscar.
- [ ] Prueba la ecuación en cada base y anota cuántos registros
       devuelve y la fecha: es la primera caja del PRISMA.
- [ ] Si vas a registrar el protocolo (PROSPERO, OSF, INPLASY),
       hazlo antes de cribar.
- [ ] Confirma quién será tu segundo revisor.
- [ ] Si la revista no estaba clara en el perfil, confirma que
       tus objetivos caben en su límite de palabras.
```

Derivación:

> Con la matriz cerrada, sigue la **Fase 2 — Introducción**. Activa la skill
> **`revision-fase2-introduccion`** y sube la Ficha, `REVISTA_[clave].json` y
> esta matriz.
> Ahí buscamos en las bases, demostramos el vacío con fuentes verificadas y
> redactamos la Introducción.
> Tu artículo no lleva Fase 3: después de la Introducción se pasa a Métodos.

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
| `references/revision.md` — tipos de revisión, guías, protocolo, análisis | Paso 6 (revisiones) |
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
