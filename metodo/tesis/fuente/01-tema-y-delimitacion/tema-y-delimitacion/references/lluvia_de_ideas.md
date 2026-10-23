# Lluvia de ideas con literatura real (solo Ruta A)

## Cuándo se usa

**Solo en la Ruta A**, cuando el tesista marcó "No tengo nada todavía, ayúdame a
encontrar tema". No se usa en la Ruta B: quien ya trae un tema no necesita que le
propongan otros, y ejecutar búsquedas ahí solo alarga la sesión.

El propósito es que las 5 propuestas del Paso 2 **salgan de lo que se está
investigando de verdad en su campo**, y no de lo que al asistente le suena
plausible. Un tema inventado de memoria puede ser razonable y estar, aun así,
completamente saturado o sin literatura que lo sostenga.

## Lo que cambia respecto de versiones anteriores

La versión anterior de esta skill decía que no buscaba ni citaba papers, solo
sugería campos de búsqueda. **Eso ya no aplica en la Ruta A**: acá la skill sí
busca con `web_search` y sí muestra artículos reales, con su enlace, para que el
tesista los abra.

Lo que no cambió, y no cambia nunca: **no se cita nada que no se haya
recuperado y verificado en la búsqueda**. Ni un autor, ni un año, ni un título.

**Alcance de esa regla**: se aplica a los resultados de web abierta, donde un
enlace puede estar roto, apuntar a un agregador o no corresponder al estudio que
dice. **No se aplica a las referencias que vengan de Scopus**, que es un índice
curado y cuyos registros son publicaciones reales con DOI. La distinción está
desarrollada en la sección de Scopus AI, más abajo, y hay que respetarla: mandar
al tesista a comprobar si existe un paper indexado en Scopus le hace perder el
tiempo.

## Antes de buscar

El tesista ya respondió, en la Tanda 2, la petición de "tres áreas o problemas
que te llamen la atención, aunque sean vagos". Ese es el insumo. Si no respondió
o respondió con una sola palabra ("educación", "empresas"), **preguntá otra vez
antes de buscar**, con `ask_user_input_v0` cuando se pueda acotar en opciones:

```
Para buscarte literatura de verdad necesito algo más concreto
que el área. ¿Cuál de estas te mueve más?

- Un problema que viste en tu práctica o en tu trabajo
- Algo que te llamó la atención en un curso
- Un tema del que ya oíste hablar y querés entender mejor
- Todavía no sé, mostrame qué se está investigando en mi carrera
```

La última opción es válida y frecuente. Ahí se busca por carrera y país, sin
tema previo, y se le muestra el panorama.

## Cómo se arma la búsqueda

Se hacen **entre 2 y 4 búsquedas**, no una sola. Cada una con un ángulo distinto,
para no quedarse con el primer resultado que aparezca.

```
BÚSQUEDA   QUÉ BUSCA                        CÓMO SE ARMA
─────────  ───────────────────────────────  ──────────────────────
1          Panorama reciente del tema en    [interés] + [carrera] +
           su campo                          "investigación" + últimos
                                             años

2          Lo mismo en inglés, porque la    [interés en inglés] +
           mayoría de la literatura         [población en inglés] +
           indexada está en ese idioma       "study"

3          Literatura del país o la          [interés] + [país] +
           región del tesista                "tesis" o "repositorio"
                                             o el nombre de una
                                             revista regional

4          Vacíos y agenda futura            [interés] + "líneas
           (opcional, si las tres            futuras de investigación"
           anteriores dieron poco)           o "research agenda"
```

**Reglas duras de la búsqueda:**

- **Solo entran resultados que se pudieron abrir y leer**, con título, autores,
  año y enlace o DOI. Si un resultado aparece en el listado pero no se puede
  confirmar, se descarta y no se menciona.
- **Nada de memoria.** Si al asistente "le suena" un estudio clásico del área y no
  apareció en la búsqueda, no se nombra. La regla 1 del método no tiene
  excepciones.
- **No se afirma cuartil, factor de impacto ni indexación** de ninguna revista sin
  haberlo verificado en la fuente. Si el tesista pregunta, se le dice que eso se
  verifica en la Skill de Artículos o en Scimago, no acá.
- **No se promete acceso.** Que un artículo aparezca no significa que el tesista
  pueda leerlo completo. Cuando el resultado sea de acceso cerrado, decirlo.
- **Si la búsqueda no arroja nada útil, se declara.** "Busqué con tres ángulos
  distintos y no encontré literatura reciente y accesible sobre esto". Es un
  hallazgo, no un fracaso: puede significar que el tema es muy nuevo, muy local o
  está mal formulado. No se rellena con resultados de otro tema para tener algo
  que mostrar.

## Cómo se le presenta al tesista

Antes de las 5 propuestas, un bloque corto. **Máximo 6 artículos**, no una
bibliografía:

```
LO QUE ENCONTRÉ EN TU CAMPO

Busqué literatura reciente sobre [interés declarado] en
[carrera]. Esto es lo que se está publicando:

1. [Apellido y año] — [qué estudió, en una línea]
   [enlace]

2. [Apellido y año] — [qué estudió, en una línea]
   [enlace]

...

Qué veo en conjunto:

- Lo que más se repite: [patrón real observado en los resultados]
- Lo que casi no aparece: [hueco real, no supuesto]
- Poblaciones que se están usando: [las que viste]

Dos advertencias honestas: esto es un vistazo rápido, no una
revisión sistemática, y algunos de estos artículos pueden estar
de pago. Ábrelos antes de comprometerte con un tema.
```

**Regla dura sobre "lo que casi no aparece"**: solo se declara un vacío si de
verdad se buscó y no se encontró. No se afirma que algo "está poco estudiado"
porque no salió en cuatro búsquedas: se dice "no apareció en mi búsqueda", que es
distinto y es lo único que se puede sostener.

## Complemento: Scopus AI (opcional, lo ejecuta el tesista)

Después de mostrar el bloque de artículos, ofrecele a Scopus AI como vía
complementaria para ver **tendencias** del campo, que es algo que una búsqueda web
no muestra bien. La búsqueda de la skill trae artículos sueltos; Scopus AI resume
hacia dónde va el área y qué vacíos declaran los propios autores.

**Regla dura: el prompt lo escribe la skill, no el tesista.** Él solo copia y pega.
Pedirle que lo redacte es devolverle el problema que vino a resolver.

**Regla dura: el prompt va en inglés.** Scopus AI trabaja sobre literatura indexada
en inglés y responde mucho mejor en ese idioma, aunque el tesista escriba en
español. La skill le explica eso en una línea para que no crea que es un descuido.

### Cómo se ofrece

```
¿Tienes acceso a Scopus por tu universidad?

- Sí, y quiero ver las tendencias de mi área
- No tengo acceso a Scopus
- No sé si mi universidad me lo da
- Te explico qué es y para qué sirve
```

Si no tiene acceso, **no se insiste y no se frena el flujo**: se sigue con las 5
propuestas a partir de los artículos ya encontrados. Scopus AI es un complemento,
no un requisito.

### El prompt que se le entrega

Dos prompts, con los campos ya rellenados con lo que el tesista declaró. Se le
entregan en un bloque para copiar, sin explicación adentro:

```
PROMPT 1 — Tendencias del área

What are the main research trends in [tema o interés declarado]
among [población declarada] published between [año actual menos 5]
and [año actual]? Which specific subtopics are growing, and which
appear to be saturated? List the most cited papers behind each
trend.

PROMPT 2 — Vacíos para delimitar

Based on recent research on [variable 1] and [variable 2] in
[población declarada], what research gaps do the authors
explicitly state as future work? Are there studies conducted in
[país declarado] or in similar contexts? If not, say so.
```

Reglas de armado de los prompts:

- **Se rellenan con lo que el tesista declaró**, no con supuestos. Si todavía no
  hay variables (es la Ruta A, puede que no las haya), se usa el Prompt 1 solo.
- **Los años se calculan desde la fecha actual del contexto**, igual que en el
  resto de la skill. Nunca se quema un año.
- **La frase "If not, say so"** del Prompt 2 no es decorativa: obliga a la
  herramienta a declarar la ausencia en lugar de rellenar. Se conserva.
- No se agregan filtros de cuartil ni de revista al prompt. Eso es trabajo de la
  Skill de Artículos, no de la delimitación del tema.

### Advertencias obligatorias al entregarlo

```
Tres cosas antes de que lo uses:

1. Scopus AI no está habilitado en todas las suscripciones.
   Depende de lo que tenga contratado tu universidad. Si al
   entrar no ves la opción, no la tienes y no hay forma de
   activarla por tu cuenta.

2. Las referencias que te devuelva son reales: Scopus es un
   índice curado y cada registro corresponde a una
   publicación existente, con su DOI. Para citarlas en tu
   tesis tienen que entrar a tu biblioteca: si me lo pides,
   las guardo ahí con su DOI. Lo que sí conviene contrastar
   es el resumen: que lo que la herramienta dice que un
   estudio encontró coincida con lo que el estudio realmente
   concluye.

3. Va en inglés a propósito. Scopus indexa casi todo en ese
   idioma y responde mejor así, aunque tú escribas en español.
```

**Nota para la skill sobre el punto 2**: la diferencia importa y no se debe
confundir. **Las fuentes de Scopus son verificables**: están indexadas, tienen
metadatos completos y DOI, y no hay riesgo de que el estudio no exista. Lo que sí
es una capa de interpretación es **lo que la herramienta dice sobre ellas**: la
frase que resume un hallazgo y, sobre todo, el veredicto de "esto está creciendo"
o "esto está saturado", que es una síntesis y no un dato del registro.

Tratar una referencia de Scopus como si pudiera ser inventada es un error de la
skill, y le hace perder tiempo al tesista mandándolo a comprobar algo que ya está
comprobado.

### Qué hace la skill con lo que el tesista traiga de vuelta

Si pega la respuesta de Scopus AI:

- **Las referencias son fuentes reales.** No hay que "verificar que existan". Si
  el tesista quiere alguna en el bloque de artículos, se incluye, indicando que
  llegó por Scopus AI. Si además la quiere conservar para citarla más adelante, se
  le pregunta y se guarda con `anadir_a_mis_fuentes` por su DOI: desde ahí tiene
  clave.
- **Lo que se marca como pendiente de contrastar es la afirmación, no la
  fuente.** Cuando la skill traslade un hallazgo al chat, la marca correcta es
  `[hallazgo según el resumen de Scopus AI, conviene leer el estudio]`, y aplica
  solo a la frase que interpreta el estudio.
- **El veredicto de tendencia o saturación es una síntesis**, no un dato del
  índice. Se atribuye: "Scopus AI lo reporta como un subtema en crecimiento", no
  "este subtema está en crecimiento".
- **Se usa para afinar las 5 propuestas**, sobre todo el chequeo de saturación: si
  Scopus AI dice que un subtema está saturado y la búsqueda web mostraba lo mismo,
  la advertencia al tesista es mucho más sólida y se le dice que dos fuentes
  coinciden.
- **Si Scopus AI contradice lo que encontró la búsqueda web, se declara la
  contradicción** en lugar de elegir en silencio cuál tiene razón. En esa
  contradicción, Scopus pesa más que un resultado de web abierta, y se dice por
  qué: uno es un índice curado y el otro no.

### Qué significa "tema de alto impacto" y qué no

Cuando se le diga al tesista que un tema tiene más potencial que otro, hay que
decir en qué se basa esa afirmación. Un tema con potencial, en esta skill, es el
que cumple tres cosas observables:

```
1. La literatura reciente sobre él está creciendo, no cayendo.
2. Hay autores que declaran explícitamente ese vacío como
   trabajo futuro.
3. El tesista puede ejecutarlo con el acceso a campo y el
   plazo que declaró.
```

**Lo que NO significa, y hay que decirlo si el tesista lo pregunta**: no garantiza
publicación, no predice citas, y no dice nada sobre el cuartil de la revista donde
podría terminar. Esa evaluación es de la ruta de artículos, con la revista
destino a la vista, no de la delimitación del tema. Prometer impacto acá sería
venderle una expectativa que esta skill no puede sostener.

Y el tercer criterio manda sobre los otros dos: un tema con literatura creciente y
vacío declarado que el tesista no puede ejecutar en su plazo no es de alto
impacto, es una tesis que no se sustenta.

## Cómo se pasa de la literatura a las 5 propuestas

Después del bloque anterior, se pregunta con `ask_user_input_v0`:

```
¿Con qué seguimos?

- Me interesa la línea 1, armá propuestas por ahí
- Me interesa la línea 2, armá propuestas por ahí
- Mezclá las dos
- Ninguna me convence, busquemos otra cosa
```

Recién entonces se generan las 5 propuestas del Paso 2, con todas sus reglas
duras de filtrado. **Cada propuesta declara de qué se apoya:**

```
Propuesta N

Título de trabajo: [...]
Variables o categorías: [...]
Población: [...]
Nivel de investigación: [...]
Tipo de aporte: [...]
Por qué encaja con tu acceso a campo: [...]

Se apoya en: [Apellido y año] de los artículos que te mostré,
o "no se apoya en ninguno de los encontrados, es una
combinación propia" si ese es el caso.
```

Ese último campo es obligatorio y se responde con honestidad. Si una propuesta no
sale de ninguno de los artículos recuperados, se dice, y el tesista decide si
igual le interesa.

## Chequeo de saturación

Con los resultados a la vista se puede hacer algo que antes no se podía: decirle
al tesista si su idea ya está muy trabajada.

- **Si aparecen muchos estudios recientes con el mismo par de variables y
  poblaciones parecidas**, se le advierte que el tema está saturado y que
  necesita un giro (otra población, otra mediación, otro contexto).
- **Si no aparece casi nada**, se le advierte lo contrario: puede quedarse sin
  antecedentes para el Capítulo II, que es donde más duele.
- En los dos casos se muestra en qué resultados se basa la advertencia.

Este chequeo reemplaza la casilla "Literatura suficiente" y "No saturado" del
checklist de viabilidad del Paso 2, que antes se marcaba a ojo. Ahora se marca
con evidencia y se dice cuál.

## Del chat a la biblioteca

Los artículos del bloque se muestran con apellido, año y enlace **en el chat**. No
se escriben en el texto que se guarda: la tabla resumen del Paso 6 no lleva citas.

Si el tesista quiere quedarse con alguno para el Capítulo I o el marco teórico, se
le pregunta cuáles y se guardan con `anadir_a_mis_fuentes`, pasando sus DOI. Desde
ahí tienen clave `[AR…]` y las skills siguientes los encuentran con
`buscar_fuentes`. Lo que no tenga DOI (una tesis de repositorio, un informe) lo
mete él en su Zotero o su Mendeley conectado. Nunca se guarda en su biblioteca algo que no pidió.

Complemento: `buscar_fuentes` (`tema` en inglés, `temaOriginal` en español,
`pais`) busca en la biblioteca de Acosta y en la del tesista. Puede lanzarse junto
con las búsquedas web: lo que devuelve ya viene con clave y con criterio editorial.

## Lo que esta búsqueda NO hace

- **No arma el marco teórico ni los antecedentes.** Eso es la Skill de Marco
  Teórico, con su propio corpus y sus propias reglas.
- **No reemplaza la búsqueda del Capítulo I.** La Skill de Problema y Objetivos
  pide un mínimo de 20 fuentes, que entran a su biblioteca del proyecto (su Zotero o
  Mendeley, sus exports o por DOI) y se citan por clave. Lo de acá son 6
  artículos para orientar la elección del tema, nada más. Decírselo, para que no
  crea que ya tiene su bibliografía.
- **No valida el tema ante el asesor.** Sigue siendo una propuesta.
