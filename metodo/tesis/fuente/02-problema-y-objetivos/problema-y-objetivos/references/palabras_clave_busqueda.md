# Palabras clave para buscar fuentes

## Por qué este archivo existe

En pruebas de campo se detectó que **generar la ecuación de búsqueda completa
para Scopus no ayuda al tesista**. Las ecuaciones largas con `AND`, `OR`,
`TITLE-ABS-KEY`, paréntesis anidados y `LIMIT-TO` suelen arrojar cero resultados,
se rompen al copiarlas por las comillas tipográficas, y el tesista no sabe qué
tocar cuando fallan.

Lo que sí funciona es entregarle **palabras clave limpias**, que él pega en la
barra de búsqueda y refina con los filtros de la interfaz.

**Regla dura: por defecto la skill entrega palabras clave, no ecuaciones.** Se
entregan las palabras clave y las instrucciones de filtrado por menú, y con eso
el tesista sale a buscar.

**Si el tesista pide la ecuación de búsqueda, se le dan las cuatro de una vez**
(Scopus, Web of Science, Science Direct y Springer Nature Link) en el mismo
mensaje, junto con las palabras clave, y sin preguntarle para cuál base la quiere.
Está desarrollado más abajo, en "Ecuaciones de búsqueda: las cuatro de una vez".

Lo que no se hace nunca es entregar una ecuación **en lugar** de las palabras
clave, ni preguntarle para qué base la necesita antes de dársela.

## La regla de las palabras clave

**Entre 3 y 5 palabras clave. Nunca menos de 3, nunca más de 5.** Salen del
título y son, en este orden:

```
1. Variable 1          (obligatoria)
2. Variable 2          (obligatoria)
3. Población           (obligatoria)
4. Contexto            (si aporta: país, sector, tipo de institución)
5. Un matiz del tema   (solo si hace falta acotar más)
```

En estudios descriptivos de una sola variable: variable, población y contexto,
que ya son tres.

Con más de cinco términos la base devuelve cero resultados. Con menos de tres,
miles. Si con las tuyas salen demasiados, **no agregues palabras**: aplicá los
filtros de la interfaz (año, tipo de documento, área temática).

## Formato de entrega: un solo campo, separado por comas

**Regla dura: las palabras clave se entregan en UNA sola línea, separadas por
comas, lista para copiar y pegar.**

**Prohibido presentarlas agrupadas por concepto.** Este es el error que más
entorpece la búsqueda del tesista, y se ve así:

```
MAL (subgrupos, no sirve para copiar):

   Variables: uso de la IA, pensamiento crítico
   Población: estudiantes universitarios
   Contexto: Perú

MAL (una por línea):

   uso de la IA
   pensamiento crítico
   estudiantes universitarios

BIEN (un campo, listo para pegar):

   Uso de la IA, Pensamiento crítico, estudiantes universitarios
```

El tesista tiene que poder seleccionar la línea entera de un arrastre y pegarla.
Cualquier etiqueta, viñeta o salto de línea dentro del campo rompe eso.

## Entrega obligatoria en dos idiomas

La skill entrega **dos líneas, una por idioma**, cada una con su propio campo
copiable. Eso no es subagrupar: es el mismo listado en dos idiomas, y el tesista
usa el que corresponda a la base donde busque.

Motivo: Scopus, Web of Science, Science Direct y Springer Nature Link indexan
casi todo en inglés. Las bases regionales (SciELO, Redalyc, Dialnet, RENATI) y
Google Académico funcionan en español.

La traducción al inglés usa el término técnico con el que el campo indexa ese
constructo, no una traducción literal. Si la skill no está segura del descriptor,
lo marca como `[término propuesto, conviene verificarlo en el tesauro de la base]`
**fuera del campo copiable**, nunca dentro.

## Bloque de entrega (formato exacto)

```
TUS PALABRAS CLAVE

En español (SciELO, Redalyc, Dialnet, RENATI, Google Académico):

Uso de la IA, Pensamiento crítico, estudiantes universitarios, Perú

En inglés (Scopus, Web of Science, Science Direct, Springer Nature Link):

artificial intelligence, critical thinking, university students, Peru

Cómo se usan: copias la línea completa y la pegas en la barra de
búsqueda. No agregues AND ni OR: la base los combina sola.

Si la base te pide comillas para frases de dos o más palabras,
escríbelas a mano. Las comillas copiadas desde un chat suelen ser
tipográficas y las bases las leen como texto plano, lo que devuelve
cero resultados.
```

Las dos líneas del ejemplo son eso, ejemplos de formato. Se reemplazan por las
del tesista.

## Bases de datos del método

**Scopus es la base por defecto del método.** Cuando el tesista tiene acceso
institucional, ahí es donde empieza. Las demás complementan:

```
BASE                      CUÁNDO SE USA
────────────────────────  ─────────────────────────────────────
Scopus                    Por defecto. Máxima calidad de
                          metadatos y el export .txt que esta
                          skill procesa mejor.

Web of Science            Complemento de Scopus. Cobertura
                          parcialmente distinta, así que vale
                          la pena correr las dos.

Science Direct            Elsevier a texto completo. Útil
                          cuando hace falta leer el artículo
                          entero, no solo el resumen.

Springer Nature Link      Buena parte en acceso abierto, así
                          que sirve aunque el acceso
                          institucional sea limitado.

Google Académico          Gratuita, sin acceso institucional.
                          Es la vía cuando no hay Scopus, y la
                          mejor para literatura nacional.
```

**Regla dura**: no se le ofrece al tesista una base que no pueda abrir. Primero se
pregunta si tiene acceso institucional, y según eso se le muestran las que le
sirven. Ofrecerle Scopus a quien no lo tiene es hacerle perder un turno.

## Ecuaciones de búsqueda: las cuatro de una vez

La entrega por defecto son las palabras clave. **Pero si el tesista pide la
ecuación de búsqueda, se le entregan las cuatro en el mismo mensaje**, sin
preguntarle para cuál base la quiere. Preguntarlo gasta un turno y él ya dijo lo
que necesitaba.

```
ECUACIONES DE BÚSQUEDA

Scopus (pégala en Advanced search):

TITLE-ABS-KEY("artificial intelligence" AND "critical thinking"
AND "university students")

Web of Science (pégala en Advanced Search, campo TS):

TS=("artificial intelligence" AND "critical thinking" AND
"university students")

Science Direct (pégala en Advanced search):

"artificial intelligence" AND "critical thinking" AND
"university students"

Springer Nature Link (pégala en Advanced search):

"artificial intelligence" AND "critical thinking" AND
"university students"
```

**Advertencias que van con las ecuaciones:**

- **Las comillas hay que escribirlas a mano** en la barra de la base. Es la causa
  número uno de "me salieron cero resultados".
- **Si da cero, se quita el término menos central** (normalmente el contexto o el
  matiz), no se agregan más.
- **Science Direct limita la cantidad de conectores booleanos** por búsqueda. Si
  rechaza la ecuación, se parte en dos búsquedas más simples.
- **Los filtros de año, tipo de documento y área se aplican con los menús**, no
  dentro de la ecuación. Meter `LIMIT-TO` en el texto pegado es lo que más
  ecuaciones rompe.

**Regla dura de honestidad**: en pruebas de campo, las ecuaciones largas
rindieron peor que las palabras clave sueltas con filtros de interfaz. Si el
tesista pide la ecuación, se le da sin discutir, pero se le dice esto en una
línea para que sepa qué esperar.


## Filtros por interfaz (reemplazan a la ecuación)

En lugar de la ecuación, la skill entrega la secuencia de filtros del menú
lateral. Es lo que de verdad reduce el ruido:

```
1. Año: últimos 5 años
2. Tipo de documento: artículo y revisión
3. Área temática: la que corresponda a la carrera
4. Keywords sugeridas: marcar las 2 a 4 más cercanas al tema
```

Ese orden importa: filtrar por año primero evita que la lista de keywords
sugeridas se llene de términos de artículos viejos.

## Scopus AI

Si el tesista declara que tiene acceso institucional a Scopus, la skill le
menciona **Scopus AI** como vía complementaria: es el asistente de IA de Scopus,
que responde en lenguaje natural y devuelve un resumen del panorama del tema con
los artículos en los que se apoya.

Para qué sirve en este flujo: para entender rápido de qué se está hablando en el
tema y detectar los autores y trabajos más relevantes, antes de armar el listado
definitivo.

**Advertencias obligatorias que la skill debe dar al mencionarlo:**

```
Tres cosas sobre Scopus AI:

1. No está habilitado en todas las suscripciones. Depende de
   lo que tenga contratado tu universidad. Si al entrar a
   Scopus no ves la opción, no la tienes disponible y no hay
   forma de activarla por tu cuenta.

2. Sirve para orientarte, no para citar. Lo que te devuelva
   hay que abrirlo, leerlo y verificarlo en el registro real
   del artículo antes de citarlo.

3. Igual necesitas exportar el listado de Scopus y cargarlo
   en «Mis fuentes» (o en tu Zotero o tu Mendeley). Scopus AI te da el
   panorama; lo que está en tu biblioteca es lo que se cita.
```

La skill **no afirma** qué funciones concretas tiene Scopus AI hoy ni qué incluye
cada plan. Si el tesista pregunta por detalles, la skill lo deriva a verificarlo
en su acceso institucional, con la marca de transparencia correspondiente.

## NotebookLM para PDFs completos

**Cuándo recomendarlo (regla dura)**: cuando el tesista dice que tiene PDFs
completos y son **más de 5**, o cuando son artículos largos (revisiones
sistemáticas, tesis completas, libros).

Motivo honesto que la skill le explica:

```
Si subes 20 PDFs completos a este chat, se consume muchísimo
espacio de contexto en texto que en su mayoría no vamos a usar
(métodos, tablas de resultados, anexos). Eso hace que la sesión
se vuelva lenta y que se pierda información del inicio.

Lo que sí necesito de cada artículo es poco: autores, año,
título, revista, DOI, el abstract y la conclusión principal.

Alternativa: pasa los PDFs por NotebookLM (u otra herramienta de
resumen de documentos), pídele un resumen por artículo con esos
campos, y pegá acá los resúmenes. Rinde mucho más.
```

**Advertencias obligatorias al recomendarlo:**

```
- El resumen es un intermediario. Si un dato del resumen se ve
  raro, hay que volver al PDF original antes de citarlo.
- Los datos de referencia (autores completos, año, revista,
  volumen, páginas, DOI) conviene sacarlos del PDF o del
  registro de la base, no del resumen, porque las herramientas
  de resumen a veces los abrevian.
- Si son pocos PDFs (5 o menos), no hace falta: subilos
  directo acá y los proceso completos.
```

La skill **no afirma** límites, precios ni funciones concretas de NotebookLM. Lo
nombra como una opción y deja que el tesista verifique qué tiene disponible.

## Qué hace la skill con las palabras clave después

Las palabras clave no se descartan tras la búsqueda. Se reutilizan en:

- La búsqueda activa que hace la propia skill (`buscar_fuentes`, `buscar_en_la_literatura` y `web_search`).
- La búsqueda complementaria de fuentes nacionales.
- La Skill de Marco Teórico, para ampliar antecedentes.

Por eso quedan registradas en el chat y se repiten en el cierre del Paso 3.
