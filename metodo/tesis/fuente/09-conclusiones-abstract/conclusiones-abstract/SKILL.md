---
name: conclusiones-abstract
description: Acompaña a tesistas hispanohablantes a redactar el capítulo final de cierre. Lee del proyecto el Cap I (Objetivos), los Resultados (Skill 7) y la Discusión (Skill 8) —o el texto que pegue el tesista si los escribió fuera— y guarda UN capítulo con CUATRO elementos. (1) Conclusiones, una por objetivo, con subtítulos 6.1.1, 6.1.2..., en tres partes (objetivo parafraseado + hallazgo + implicancia). (2) Recomendaciones a tres destinatarios (lugar de estudio con plazos, otros profesionales, futuros investigadores), entre 8 y 13, cada una respaldada en un hallazgo. (3) Resumen en español IMRyD con extensión según el nivel académico. (4) Abstract en inglés académico equivalente. Palabras clave en ambos idiomas. NO redacta limitaciones (eso fue Skill 8). Maneja con honestidad las hipótesis rechazadas. ACTIVAR cuando el usuario diga "conclusiones", "recomendaciones", "resumen", "abstract". Es la NOVENA skill del método.
---

# Skill de Conclusiones, Recomendaciones y Abstract

## Para qué sirve esta skill

Esta es la novena skill del método de tesis con Agente IA. Cierra el cuerpo de la tesis produciendo cuatro elementos exigentes en un solo documento:

1. **Conclusiones**: una por cada objetivo, en correspondencia uno a uno.
2. **Recomendaciones**: a tres destinatarios (lugar de estudio, otros profesionales, futuros investigadores).
3. **Resumen** en español: síntesis condensada de la tesis completa.
4. **Abstract** en inglés: equivalente académico del resumen.

El jurado lee PRIMERO el abstract y las conclusiones. Si están mal, llega al resto de la tesis predispuesto en contra. Este capítulo es desproporcionadamente importante respecto a su longitud.

Pertenece al método de Acosta IA Research y respeta sus tres reglas de oro:

1. **Cero referencias inventadas.** La skill no introduce información nueva en las conclusiones, solo sintetiza lo que aparece en Resultados y Discusión.
2. **Contexto siempre.** Antes de redactar, la skill verifica objetivos, hallazgos por objetivo y decisiones de hipótesis. Si falta algo, pregunta.
3. **Validación humana al final.** El tesista revisa cada conclusión y cada recomendación. La voz académica final es del tesista.

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un .docx, un PDF ni ningún otro archivo del capítulo.** No usa la skill `docx`, no escribe en `/mnt/user-data/outputs/`, no usa `present_files` y no entrega archivos en el chat.

El documento lo arma el servidor de la plataforma con lo que está guardado en el proyecto: portada, índice, capítulos en orden, y las citas y las referencias escritas en la norma del proyecto, enlazadas a Zotero cuando el tesista lo conectó. La skill **redacta, guarda y entrega el enlace**.

```
1. mi_proyecto        al abrir la conversación (trae la norma de citas)
2. ver_capitulo       antes de preguntarle nada del capítulo;
                      lee `problema-y-objetivos`,
                      `analisis-datos-rstudio` y `discusion`,
                      con `texto: true`
3. buscar_fuentes     al necesitar respaldo; la cita nace atada a
   / mis_fuentes      su clave de biblioteca, Zotero y Mendeley incluidos
4. guardar_capitulo   clave `conclusiones-abstract`, apenas el tesista lo dé por bueno
5. revisar_evidencia  antes de entregar
6. enlace_del_word    cuando quiera el documento
```

**Las citas se marcan con la clave de la fuente, no se escriben.** Así:

```
…afecta al rendimiento académico [AR97D22F86].
Braun y Clarke [AR97D22F86:n] proponen que…
«…» [AR97D22F86:p. 45]
[FALTA FUENTE]   cuando no hay respaldo
```

La skill **no escribe la cita** en texto («(Pérez y García, 2024)», «(1)», «[1]»), **no escribe la lista de referencias** y **no cita de memoria**. Solo usa claves que haya devuelto una búsqueda o la biblioteca. Al armar el Word, el servidor convierte cada clave en su cita y su referencia.

**Un solo documento, siempre al día.** No hay versiones V1, V2… del documento: el servidor mantiene uno solo con los capítulos en orden. Si el tesista pregunta por «el V5» o quiere subir el Word del capítulo anterior, se le explica que no hace falta: lo guardado se lee con `ver_capitulo` (`texto: true`). Solo se le pide que pegue algo si ese capítulo no está guardado.

**El formato no se pregunta.** Márgenes, tipografía e interlineado son configuración del proyecto en la plataforma. Lo único de formato que la skill sí necesita es la **norma de citas**: si `mi_proyecto` no la trae, se pregunta una vez y se guarda con `guardar_avance` (`estiloCitas`). Nada se convierte ni se renumera a mano.

**Entre corchetes, en el texto guardado, solo van** las claves `[AR…]`, `[FALTA FUENTE]` y la marca de figura `[Insertar aquí la Figura N: archivo.png]`. Los avisos para el tesista van en el chat, nunca dentro del capítulo.

**Si un guardado falla, se dice con esa palabra: no se guardó.** No se inventa que quedó guardado ni se entrega un archivo armado por la skill como reemplazo.

El detalle de la biblioteca, las marcas de cita, la norma y las seis herramientas de fuentes está en `references/integracion_zotero.md`. **Leerlo antes de citar por primera vez** (con `redactar`, `referencia: "integracion_zotero.md"`). Al final de ese archivo están **las demás herramientas de su perfil** (Scopus con SciELO y ALICIA, Zotero, Mendeley, R, ATLAS.ti y el mapa en VOSviewer) y cuándo nombrarlas.

## Regla crítica de interactividad

**TODA pregunta usa `ask_user_input_v0` con opciones tocables.** Campo `question` siempre presente. Máximo 3 preguntas por bloque.

## Frontera importante (lo que esta skill NO hace)

- **No redacta Limitaciones**. Eso lo hace Skill 8 (Discusión).
- **No revisa antiplagio ni arma el documento a mano**. La skill guarda el capítulo de cierre; el Word con portada, índice y capítulos en orden lo arma el servidor. Las páginas preliminares propias (dedicatoria, agradecimientos) y el antiplagio quedan a cargo del tesista con su asesor.
- **No escribe la carátula, el índice ni los preliminares** de la tesis: la portada y el índice los pone el Word del servidor. Solo redacta el Resumen y el Abstract, que se guardan al final del capítulo y el tesista mueve a sus preliminares si su reglamento lo pide.
- **No introduce hallazgos nuevos** en las Conclusiones que no aparezcan en Resultados.
- **No recomienda lo que la tesis no estudió** (regla del Cap 9.4).

## Cómo se activa

- El tesista llega con el Cap I, Resultados (Skill 7) y Discusión (Skill 8) terminados: guardados en su proyecto, o escritos fuera de la plataforma para pegarlos.
- Pregunta por "conclusiones", "recomendaciones", "resumen", "abstract", "palabras clave".

## Paso 1 — Verificar punto de partida

Pregunta interactiva (single_select):

- "Los trabajé con las skills del método (léelos de mi proyecto)"
- "Pego manualmente objetivos + hallazgos + decisiones de hipótesis"
- "Aún me falta la Discusión"

Si tercera opción, deriva a Skill 8 y termina.

### Leer los tres capítulos del conector

El tesista no sube ni pega los capítulos que escribió con el método: la skill los lee con `ver_capitulo`, con `texto: true`:

- **Cap I**: `capitulo: problema-y-objetivos`.
- **Resultados**: `capitulo: analisis-datos-rstudio`.
- **Discusión**: `capitulo: discusion`.

Cada respuesta trae una parte de hasta 24.000 caracteres y dice «parte N de M» y cuál pedir después. Se sigue pidiendo con `parte` (2, 3…) hasta la última. Las claves exactas son las que muestra `mi_proyecto` o `listar_capitulos`. En el texto guardado las citas vienen como claves `[AR…]`, las tablas en su bloque APA y las figuras con su rótulo.

**Solo si `ver_capitulo` dice que un capítulo no tiene texto guardado** (por ejemplo, porque el tesista lo escribió fuera de la plataforma), se le pide que lo pegue en el chat.

### Lectura sin repeticiones y exigencia de los TRES capítulos (patrones P1 y P2 del ecosistema)

No volver a pedir una parte que ya se leyó en esta conversación. Si el tesista pega un capítulo que ya se leyó del conector, NO releerlo: confirmar que ya está leído y seguir.

Hacen falta los tres. Si alguno no tiene texto guardado y el tesista no lo pegó, pausar y pedir el faltante. NO avanzar con capítulos incompletos.

### Si segunda opción, pide:

```
Datos clave que necesito:
- Título tentativo de la tesis
- Tesista, carrera, universidad
- Año del estudio
- Objetivo general (textual del Cap I)
- Objetivos específicos (textuales del Cap I)
- Hipótesis (general y específicas)
- Para cada objetivo específico:
   · Hallazgo numérico clave (de Resultados)
   · Decisión sobre la hipótesis (aceptada/rechazada)
   · Implicancia identificada en la Discusión
- Diseño metodológico (transversal/longitudinal, descriptivo/
   correlacional/explicativo)
- Población y tamaño muestral final
- Lugar de aplicación (institución, sector, ciudad)
- Instrumento aplicado (cuestionario tipo Likert con N ítems)
- Confiabilidad obtenida (alfa de Cronbach por variable)
- Software estadístico usado (R, SPSS, JASP)
```

Si primera opción, lee los tres capítulos completos del conector (o el texto que pegó el tesista) y extrae automáticamente.

### Validación previa antes de avanzar

- ¿Hay 1 hallazgo claro por cada objetivo específico?
- ¿Hay decisión explícita (aceptada/rechazada) para cada hipótesis?
- ¿La cantidad de objetivos coincide con la cantidad de hallazgos?

Si falta algo, pausar y preguntar.

## Paso 2 — Confirmar alcance del capítulo

Por defecto, la skill redacta los 4 elementos y los guarda juntos en el mismo capítulo. Pero confirma:

Pregunta interactiva (single_select):
- "Generar los 4 elementos completos (RECOMENDADO): Conclusiones + Recomendaciones + Resumen + Abstract"
- "Solo Conclusiones + Recomendaciones (sin Resumen/Abstract todavía)"
- "Solo Resumen + Abstract (ya tengo Conclusiones y Recomendaciones)"

## Paso 3 — Verificar correspondencia objetivo-conclusión

La skill aplica la regla del Cap 9.2: **una conclusión por cada objetivo**.

Si el Cap I tiene 1 objetivo general + 4 objetivos específicos → 5 conclusiones.

Si la cantidad no coincide, la skill lo declara y pregunta cómo proceder:

Pregunta interactiva (single_select):
- "Tienes 5 objetivos en Cap I. Genero 5 conclusiones (RECOMENDADO)"
- "Quiero una conclusión final extra que sintetice todo el estudio"
- "Quiero menos conclusiones, te explico cuáles fusionar"

## Paso 3.5 — Nivel académico y extensión (obligatorio antes de redactar)

Igual que en la Discusión, el cierre de una tesis de pregrado y el de un doctorado no se parecen. Pregunta obligatoria con `ask_user_input_v0`:

```
¿Para qué nivel es tu tesis?

· Pregrado (bachiller, licenciatura o título profesional)
· Maestría
· Doctorado
· Te ayudo a decidirlo con ejemplos sencillos
```

### Qué cambia con el nivel

```
                    PREGRADO      MAESTRÍA      DOCTORADO
──────────────────  ────────────  ────────────  ─────────────
Conclusión por      80-120        120-180       180-250
objetivo (palabras)

Recomendaciones     8-10          10-13         12-15
(total)

Resumen español     150-250       200-300       250-350
(palabras)

Abstract inglés     equivalente al resumen en los tres niveles

Palabras clave      3-5           4-6           5-6
```

**Qué se agrega en cada nivel** (no es solo largo):

- **Pregrado**: la conclusión recuerda el objetivo, indica el hallazgo y cierra con la implicancia práctica. Las recomendaciones son operativas y con plazo.
- **Maestría**: además, cada conclusión señala qué cambia el hallazgo para la práctica del sector, no solo para la institución estudiada. Las recomendaciones incluyen al menos dos de alcance sectorial.
- **Doctorado**: además, cada conclusión declara **qué aporta el hallazgo al conocimiento del campo**: qué supuesto teórico se confirma, se matiza o queda en cuestión. Las recomendaciones a futuros investigadores son más específicas: qué diseño, qué población, qué variable no controlada convendría incorporar.

**Regla dura de calibración**: si el tesista es de pregrado, la skill NO agrega el movimiento de aporte teórico. Exigirle a un bachiller que declare qué le aporta su tesis a la teoría del campo es pedirle algo que su nivel no requiere y que casi siempre sale forzado.

**Regla dura sobre el reglamento**: estas cifras son orientativas. Muchas universidades fijan el rango del resumen (150-250 es lo más común, pero hay reglamentos que piden 300). La skill pregunta:

```
· Usar las extensiones sugeridas para [nivel declarado]
· Mi reglamento pide otra extensión de resumen (te la digo)
· No sé qué pide mi reglamento, usá la sugerida
```

**Regla dura anti-relleno**: una conclusión que dice lo que tiene que decir en 90 palabras no se estira a 180 para cumplir un rango. Si el hallazgo es simple, la conclusión es corta y la skill lo declara en lugar de inflar.

## Paso 4 — Redactar Conclusiones (con subtítulos numerados)

Cada conclusión sigue la estructura de 3 partes del método (detalle en `references/conclusiones.md`):

1. **Recordar el objetivo** (parafraseado, no copiado textual).
2. **Indicar el hallazgo principal** (con estadístico clave).
3. **Cerrar con una frase de implicancia o aporte**.

### Formato con subtítulos numerados

```
6.1 Conclusiones

   6.1.1 Conclusión del objetivo general
   [Párrafo siguiendo la estructura de 3 partes]

   6.1.2 Conclusión del objetivo específico 1
   [Párrafo siguiendo la estructura de 3 partes]

   6.1.3 Conclusión del objetivo específico 2
   [Párrafo]

   ... y así sucesivamente
```

### Orden obligatorio

La PRIMERA conclusión responde al **objetivo general**. Las siguientes responden a los específicos en el mismo orden del Cap I.

### Manejo de hipótesis rechazadas

Si una hipótesis específica fue rechazada, la conclusión correspondiente lo declara con honestidad. NO inventar coincidencias. Por ejemplo:

> "Respecto al segundo objetivo específico, orientado a determinar la relación entre uso y aplicación de IA y disposición al pensamiento crítico, el estudio NO halló asociación estadísticamente significativa (ρ = .18, p = .081), por lo que se rechazó la hipótesis H2. Este hallazgo aporta evidencia de que el uso de IA por sí mismo no se relaciona con el pensamiento crítico en la población estudiada, lo cual sugiere que la calidad reflexiva del uso es más relevante que su frecuencia."

Ver `references/conclusiones.md` para reglas detalladas.

## Paso 5 — Redactar Recomendaciones (tres destinatarios)

### Estructura

```
6.2 Recomendaciones

   6.2.1 Al lugar de estudio
   [Entre 3 y 5 recomendaciones operacionales con plazo]

   6.2.2 A otros profesionales del campo
   [Entre 2 y 3 recomendaciones sectoriales]

   6.2.3 A futuros investigadores
   [Entre 3 y 5 recomendaciones académicas]
```

Total ideal: entre 8 y 13 recomendaciones (Cap 9.9).

### Recomendaciones al lugar de estudio (Cap 9.6)

Cada una incluye:
- **A quién** específicamente va dirigida (gerencia, dirección, área de gestión humana, jefatura de docencia, etc.).
- **Qué acción concreta** debe realizar.
- **En qué plazo** sugerido (corto, mediano, largo).
- **Por qué** es necesaria, según un hallazgo del estudio.

Plantilla:

> "Se recomienda a [destinatario específico] [acción concreta] en un plazo [corto/mediano/largo], considerando que [hallazgo específico del estudio]."

### Recomendaciones a otros profesionales del campo (Cap 9.7)

Tres reglas:
1. Limitar alcance al sector específico, no generalizar a "todos".
2. Hablar en condicional: "podrían considerar", "sería pertinente".
3. Reconocer que los hallazgos vienen de un contexto particular y otros pueden adaptarlos, no copiarlos.

Plantilla:

> "Se recomienda a [profesionales del sector específico] considerar [práctica/adaptación], dado que [hallazgo específico] puede tener aplicabilidad en contextos similares al estudiado."

### Recomendaciones a futuros investigadores (Cap 9.8)

Tipos comunes:
- Replicar el estudio en otras poblaciones (sectores, regiones, países).
- Cambiar el diseño metodológico (transversal a longitudinal, cuanti a mixto).
- Ampliar el tamaño de muestra.
- Agregar variables moderadoras o mediadoras.
- Validar el instrumento adaptado con análisis factorial confirmatorio.
- Profundizar dimensiones con enfoque cualitativo complementario.

Plantilla:

> "Para futuras investigaciones se recomienda [acción metodológica específica], con el fin de [propósito relacionado con un hallazgo o limitación del estudio actual]."

### Validación de cada recomendación

La skill aplica la prueba de control del Cap 9.4: **¿se desprende esta recomendación de un hallazgo de este estudio?**

Si la respuesta es NO, la skill la elimina o reformula.

Ver `references/recomendaciones.md`.

## Paso 6 — Redactar Resumen en español (IMRyD)

### Estructura de los 4 movimientos (Cap 9.12)

1. **Introducción** (objetivo): "El presente estudio tuvo como objetivo determinar..."
2. **Método** (enfoque, diseño, muestra, instrumento): "Se utilizó un enfoque cuantitativo, diseño no experimental transversal correlacional. La muestra estuvo conformada por [n] [participantes]. Se aplicó un cuestionario tipo Likert de [n] ítems con un alfa de Cronbach de [valor]..."
3. **Resultados** (hallazgo principal con estadísticos): "Los resultados arrojaron una correlación [tipo] y estadísticamente significativa (r = [valor], p < [valor])..."
4. **Conclusión + implicancia**: "Se concluye que [variable 1] se relaciona significativamente con [variable 2] en el contexto estudiado, lo cual sustenta [implicancia práctica]."

### Longitud

Extensión según el nivel académico declarado en el Paso 3.5: pregrado 150-250 palabras, maestría 200-300, doctorado 250-350. Si el reglamento del tesista fija otro rango, manda el reglamento. La skill cuenta automáticamente y ajusta si excede.

### Palabras clave

3 a 5 palabras clave después del resumen. Deben reflejar conceptos centrales: variables, sector, tipo de estudio.

Ver `references/resumen_abstract.md`.

## Paso 7 — Redactar Abstract en inglés

### Reglas

1. Mantener estructura IMRyD del resumen en español.
2. Terminología académica correcta:
   - "Colaboradores" → "employees" (NO "collaborators")
   - "Cuestionario" → "questionnaire" (NO "questionary")
   - "Plana docente" → "teaching staff"
   - "Tesista" → "researcher" o "thesis author"
   - "Pregrado" → "undergraduate"
3. Tiempo verbal en pasado: "This study aimed to...", "The results showed...", "It is concluded that..."
4. Siglas locales explicadas en su primera mención: "the National Institute of Statistics and Informatics (INEI)"
5. Mismo número de palabras que el resumen en español, aproximadamente.

### Keywords

Equivalentes (no necesariamente literales) a las palabras clave del español. Por ejemplo, "clima organizacional" → "organizational climate" no "organizational weather".

## Paso 7.5 — Revisión y estilo de citación (antes de guardar)

### Redacción

Es el capítulo que más se lee: el jurado suele empezar por el resumen y las conclusiones. Se escribe con las reglas sin moldes y la voz del tesista que inyecta `redactar`, sin imprimir auditorías ni métricas de estilo en el chat. Dos riesgos propios del cierre:

- Las conclusiones van numeradas y en serie: cada una abre distinto y reparte el peso distinto, nunca con la arquitectura «El objetivo N buscaba X. Se encontró Y. Esto implica Z.».
- Cierran en el hallazgo y su implicancia, sin agrandar el aporte ni proyecciones emotivas («el futuro se presenta prometedor»).

Al guardar, los **AVISOS DE REDACCIÓN** que devuelva `guardar_capitulo` se corrigen con `reescribir_parrafos` (ver «Guardar y entregar»).

### Riesgo específico del resumen y el abstract

El resumen es el texto más comprimido de la tesis, y la compresión empuja hacia la plantilla. Dos reglas propias:

- **No usar el molde IMRyD como etiquetas visibles**. El resumen no dice "Objetivo: ... Metodología: ... Resultados: ... Conclusión: ...". Eso es un resumen estructurado, que solo se usa si el reglamento lo exige explícitamente. En prosa continua, los cuatro momentos se encadenan sin rótulos.
- **El abstract no es una traducción literal**. Traducir palabra por palabra produce inglés rígido que se detecta. Se redacta en inglés académico, respetando el contenido pero no la sintaxis del español. Y la terminología técnica se traduce por su equivalente aceptado en la literatura del campo, no por su equivalente literal.

### Norma de citas

Las conclusiones no llevan citas nuevas; si aparece alguna (excepcional, pero ocurre en recomendaciones a futuros investigadores), va con clave como en el resto de la tesis. Las citas van con la **clave de cada fuente entre corchetes**, nunca escritas a mano: `[AR97D22F86]` para una cita normal, `[AR97D22F86:n]` detrás del nombre si el autor va en la frase («Hernández-Sampieri [AR97D22F86:n] sostiene…»), `[AR97D22F86:p. 45]` con página, y varias seguidas (`[AR…][AR…]`) para una cita con varias fuentes. Las claves salen de `mis_fuentes`, `buscar_fuentes` o `anadir_a_mis_fuentes`.

Al descargar el Word, el servidor de Acosta escribe cada cita y la lista de referencias en la norma del proyecto, en el orden que esa norma pide y con la numeración continua de toda la tesis en Vancouver e IEEE. Por eso **no se convierte, no se numera y no se arma a mano la lista de referencias**: la norma es una sola para toda la tesis, así que los capítulos coinciden solos, y si el asesor pide otra más adelante se cambia sin reescribir ningún capítulo.

Mirá la línea «Norma de citas» que devuelve `mi_proyecto`.

- **Si ya está elegida**: no se vuelve a preguntar. Es la de toda la tesis.
- **Si dice «sin elegir»**: preguntala con `ask_user_input_v0` y guardala con `guardar_avance` (campo `estiloCitas`):

```
¿Qué norma de citas te pide tu universidad o tu asesor?

· APA 7 (la más común)
· Vancouver (Ciencias de la Salud)
· IEEE (Ingenierías e informática)
· Otra (me decís cuál)
```

Si elige «Otra», buscala entre las que acepta `guardar_avance` (APA, IEEE, Vancouver, AMA, ACS, Nature, MLA, Chicago, Harvard, APSA, ASA, MHRA y otras). Si la que pide no está, decíselo tal cual y no la aproximes sin su acuerdo. Nunca la supongas por la universidad. Si escribe la tesis en inglés, guardá también `idiomaCitas`.

Si el tesista no sabe qué norma usa, que abra un capítulo ya aprobado y mire una cita: `(Apellido, 2024)` es APA, `(1)` es Vancouver, `[1]` es IEEE.

Antes de la revisión del capítulo, comprobá además que ninguna cita esté escrita a mano, que toda afirmación con fuente lleve su clave y que no haya una lista de referencias armada a mano. **Regla dura**: nunca inventar una clave ni una fuente. Si una fuente que el tesista trajo al chat (por ejemplo, de su export de Scopus) no tiene clave, pedile permiso y añadila con `anadir_a_mis_fuentes` por su DOI; si no tiene DOI, que la suba en «Mis fuentes» de su perfil o la tenga en su Zotero o su Mendeley. Lo que quede sin respaldo se marca `[FALTA FUENTE]` y se le avisa. `revisar_evidencia` sirve para comprobar el capítulo guardado.

### Revisión (obligatoria antes de guardar el capítulo)

```
REVISIÓN DEL CAPÍTULO DE CIERRE

EXTENSIÓN (nivel declarado: [pregrado/maestría/doctorado]):
   Conclusión 1: [N] palabras → rango [X-Y] → [OK/CORTA/LARGA]
   Conclusión 2: [N] palabras → ...
   (una línea por conclusión)
   Recomendaciones: [N] → rango [X-Y] → [OK/POCAS/MUCHAS]
   Resumen: [N] palabras → rango [X-Y] → [OK/CORTO/LARGO]
   Abstract: [N] palabras → equivalente al resumen: SÍ/NO
   Palabras clave ES: [N] → rango [X-Y] → [OK/NO]
   Palabras clave EN: [N] → mismo número que ES: SÍ/NO

CORRESPONDENCIA:
   Objetivos específicos del Cap I: [N]
   Conclusiones redactadas: [N]
   Correspondencia 1 a 1: SÍ / NO (cuál falta)
   Cada recomendación respaldada en un hallazgo: [N] de [N]

RESUMEN Y ABSTRACT:
   Resumen sin rótulos IMRyD visibles: SÍ / NO
   Abstract en inglés académico, no traducción literal: SÍ / NO
   Palabras clave EN equivalentes, no literales: SÍ / NO

CITAS (si hay alguna):
   Citas con clave [AR…]: [N]; escritas a mano: 0;
   [FALTA FUENTE]: [N]

Estado: OK PARA GUARDAR / RE-REDACTAR
```

**Regla dura**: si alguna extensión queda fuera de rango, o falta correspondencia con algún objetivo, la skill re-redacta antes de guardar el capítulo.

**Regla dura**: no escribir "todo correcto" sin haber contado las palabras de cada conclusión, del resumen y del abstract con números reales.

## Paso 8 — Guardar el capítulo y entregar el Word

**Se guarda** al terminar el Paso 7 y la revisión del Paso 7.5, apenas el tesista lo da por bueno: cada conclusión y cada recomendación ya las fue validando por el camino, así que no se añade un «¿apruebas y guardo?» repetido. Si el tesista pide ver el capítulo completo antes, se le muestra en la conversación y se guarda cuando lo apruebe.

### Estructura del capítulo (el texto que se guarda)

Lo que se guarda es el texto en Markdown: `##` y `###` para los subtítulos, párrafos separados por una línea en blanco. **Sin encabezado con datos personales ni título del capítulo**: la portada (tesista, carrera, universidad) y el título de cada capítulo guardado los pone el Word del servidor. El texto empieza en 6.1 y no lleva sección «Referencias» al final.

```
    ## 6.1 Conclusiones

    ### 6.1.1 Conclusión del objetivo general

    [Párrafo]

    ### 6.1.2 Conclusión del objetivo específico 1

    [Párrafo]

    ...

    ## 6.2 Recomendaciones

    ### 6.2.1 Al lugar de estudio

    [3-5 recomendaciones operacionales numeradas con plazo]

    ### 6.2.2 A otros profesionales del campo

    [2-3 recomendaciones sectoriales]

    ### 6.2.3 A futuros investigadores

    [3-5 recomendaciones académicas]

    ## Resumen

    [Párrafo IMRyD, extensión según nivel académico]

    *Palabras clave:* [3-5 palabras clave en español]

    ## Abstract

    [Equivalent paragraph in academic English]

    *Keywords:* [3-5 keywords in English]
```

**Dónde van el Resumen y el Abstract**: en el texto guardado van al final, después de las Recomendaciones, porque el Word del servidor pone cada capítulo después de la portada y el índice, bajo su propio título, y no tiene un lugar para páginas preliminares. Casi todos los reglamentos los piden antes del índice: al entregar el enlace, decile al tesista que los mueva en Word a las páginas preliminares.

**Si solo se redacta una parte** (Paso 2): mirá antes con `ver_capitulo` (`capitulo: conclusiones-abstract`, `texto: true`) qué texto hay guardado. Si ya están las Conclusiones y las Recomendaciones y ahora se escriben el Resumen y el Abstract, se mandan con `anadir: true` para no borrar lo guardado. Si se reescribe el capítulo entero, se manda completo, sin `anadir`.

### Reglas del texto

- Subtítulos numerados 6.1.1, 6.1.2, etc., escritos con `###`.
- Sin bullets dentro de los párrafos de conclusiones.
- Para recomendaciones individuales, sí se permite numeración o viñetas según el reglamento del tesista: se escriben como lista (`1.` o `-`), un elemento por línea.
- Sin citas nuevas; si aparece alguna, con su clave `[AR…]` (ver «Norma de citas» en el Paso 7.5).

### Referencias y formato de página

El capítulo no lleva lista de referencias: si cita alguna fuente, entra en la **única lista** que arma el Word del servidor para toda la tesis, en la norma del proyecto. El formato de página lo aplica el Word del servidor (la plantilla de la facultad si el tesista la subió; si no, el formato por defecto de la plataforma); no se configura a mano. Si el reglamento pide algo distinto y no hay plantilla, se le avisa al tesista para que la suba o lo ajuste en Word.

### Guardar y entregar

**Regla dura**: no generes un .docx con código ni con ninguna otra herramienta, y no escribas una lista de referencias. El Word y la bibliografía los arma el servidor; uno hecho a mano no llevaría la norma del proyecto ni coincidiría con las fichas de las fuentes.

1. **Guardá el capítulo** con `guardar_capitulo`, clave `conclusiones-abstract` (la que muestra `listar_capitulos`). Cada llamada admite hasta 30.000 caracteres. Si el capítulo es más largo, mandalo por partes, cortando entre secciones: la primera parte sin `anadir` y las siguientes con `anadir: true`.
   - Si `guardar_capitulo` devuelve **AVISOS DE REDACCIÓN**, corregí esos párrafos con `reescribir_parrafos` (leyendo el capítulo con `ver_capitulo`, `"texto": true, "numerado": true`), sin reenviar el capítulo ni imprimir auditorías ni métricas en el chat. Lo mismo si el tesista pide cambiar unos párrafos ya guardados.
2. **Registrá lo acordado** con `guardar_avance` (capítulo `conclusiones-abstract`): un resumen de dos o tres frases (cuántas conclusiones, qué hipótesis se aceptaron o rechazaron, destinatarios de las recomendaciones). Marcá `estado: LISTO` solo si el tesista dice que da el capítulo por bueno; si no, `EN_CURSO`.
3. **Revisá la evidencia de toda la tesis** con `revisar_evidencia`, **sin `capitulo`**: este es el último capítulo y lo que se entrega es el documento entero. Contale al tesista, capítulo por capítulo, qué afirmaciones quedaron sin fuente o con `[FALTA FUENTE]`, y ofrecé resolverlas antes de que lo lleve al asesor.
4. **Dale el enlace** con `enlace_del_word` y explicáselo:

```
Tu capítulo de cierre quedó guardado. Acá tenés el enlace
para descargar tu tesis en Word: [enlace]

El Word lo arma el servidor con todos los capítulos que
tenés guardados, en orden, con portada e índice. Las citas
y la lista de referencias salen en la norma de tu proyecto
([norma]), en una sola lista para toda la tesis.

El Resumen y el Abstract quedaron al final del capítulo:
si tu reglamento los pide en las páginas preliminares,
movelos ahí en Word. El enlace vence a la media hora; si
ya pasó, pedime otro.
```

Con este capítulo la tesis queda completa en contenido: ofrecé el repaso con `revisar_la_tesis` antes de que la entregue.

## Paso 9 — Cierre y validación humana

Checklist final al tesista:

```
- [ ] Verifica que la cantidad de conclusiones coincide
       exactamente con la cantidad de objetivos.
- [ ] Lee cada conclusión: ¿el objetivo está parafraseado
       (no copiado textual)?
- [ ] Verifica que cada recomendación se respalde en un
       hallazgo específico del estudio.
- [ ] Confirma que el Resumen esté dentro del rango de tu nivel académico (o el que fije tu reglamento).
- [ ] Compara el Resumen con el Abstract: deben decir lo
       MISMO en distintos idiomas. Si retraduces el Abstract
       a español y no coincide con el Resumen, ajusta.
- [ ] Verifica el tiempo verbal en pasado en el Abstract.
- [ ] Verifica que las keywords en inglés sean equivalentes
       conceptuales (no literales) de las palabras clave en
       español.
- [ ] Descarga el Word y llévalo a tu asesor. Con este capítulo tu tesis queda completa en contenido.
       (Revisión Final y Antiplagio).
```

Cuando el asesor apruebe:

> Con este capítulo tu tesis queda completa en contenido. Lo que sigue no lo cubre el método y queda de tu lado, con tu asesor:
>
> 1. Revisar el Word descargado. Ya trae unidos todos los capítulos guardados, en orden, con portada, índice y una sola lista de referencias en la norma de tu proyecto. Al abrirlo, actualizar el índice (clic derecho sobre el índice > Actualizar campos), revisar que las tablas y figuras tengan numeración continua e insertar cada figura donde dice [Insertar aquí la Figura N: …].
> 2. Completar dedicatoria, agradecimientos y demás páginas preliminares según el formato de tu universidad, y mover ahí el Resumen y el Abstract si tu reglamento lo pide.
> 3. Si a una referencia le falta un dato o tiene uno equivocado, corregirlo en tu Zotero, tu Mendeley o «Mis fuentes» y volver a descargar el Word, en lugar de tocar la lista a mano. Antes de entregar, pedir el repaso final de la tesis, que marca citas rotas y afirmaciones sin fuente.
> 4. Pasar el documento por el antiplagio que exija tu universidad (Turnitin u otro) y revisar los párrafos que salgan marcados.
> 5. Preparar la presentación de sustentación.

## Errores comunes que la skill previene

Ver `references/errores_comunes.md` para detalle. Los principales (Cap 9.3 y 9.11):

### En conclusiones

1. Escribir más conclusiones que objetivos.
2. Repetir literalmente los resultados estadísticos sin interpretación.
3. Introducir información nueva que no apareció en Resultados.
4. Usar voz personal ("yo concluyo").
5. Olvidar el orden: la primera conclusión debe responder al objetivo general.

### En recomendaciones

1. Una sola lista sin distinguir destinatarios.
2. Recomendaciones sin respaldo en hallazgos del estudio.
3. Recomendaciones a actores que no pueden actuar.
4. Voz autoritaria en lugar de sugerencia.
5. Olvidar el plazo en las recomendaciones operacionales.

### En resumen/abstract

1. Resumen demasiado largo o demasiado corto.
2. Falta uno de los 4 movimientos IMRyD.
3. Traducción literal de Google Translate con errores.
4. Tiempo verbal incorrecto en el Abstract.

## Archivos de referencia

- `references/conclusiones.md` — Estructura de la conclusión, manejo de hipótesis rechazadas, ejemplos por tipo de hallazgo.
- `references/recomendaciones.md` — Tres destinatarios con plantillas y ejemplos por sector.
- `references/resumen_abstract.md` — IMRyD, plantilla bilingüe, glosario español-inglés de términos académicos comunes.
- `references/errores_comunes.md` — Errores frecuentes y cómo prevenirlos.
