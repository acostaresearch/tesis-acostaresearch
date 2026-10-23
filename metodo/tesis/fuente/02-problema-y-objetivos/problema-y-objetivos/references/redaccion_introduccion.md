# Redacción de la introducción y planteamiento del problema

Esta es la pieza central de la skill. El output principal del Capítulo I es la introducción en prosa científica, con citas por clave de las fuentes de la biblioteca del tesista. Esta referencia documenta cómo redactarla bien, integrando los 17 patrones de detección de escritura con IA adaptados del método humanizador-academico.

**Principio de fondo**: la redacción humana es imperfecta. Un párrafo escrito por una persona tiene una parte que se alarga porque el autor sabía más de eso, una aclaración que sobra, una palabra repetida porque no buscó el sinónimo, alguna oración que cierra torcida. Lo que delata a la redacción con IA no es un error: es que no hay ninguno.

**Segunda regla dura: humanizar es RESTAR, no reemplazar**. No cambiar "se sustenta en" por "sostienen" (dos adornos), ni "extendido al contexto de" por "llevaron al terreno de". Cambiar "se sustenta en" por "usa" o "se basa en". Se quita el adorno, no se reemplaza.

## Estructura obligatoria: 6 párrafos en este orden

```
Párrafo 1 — Problemática internacional
Párrafo 2 — Problemática nacional (país declarado)
Párrafo 3 — Problemática local (observaciones del tesista)
Párrafo 4 — Pregunta de investigación
Párrafo 5 — Objetivos
Párrafo 6 — Justificación
```

No alterar el orden. No mezclar contenidos entre párrafos.

## Reglas transversales (válidas para los 6 párrafos)

### Voz y persona

- **Tercera persona obligatoria.** Nada de "nosotros", "yo", "se considera importante" en primera persona impersonal.
- Aceptable: "el estudio plantea", "los hallazgos sugieren", "la literatura reciente coincide".
- Inaceptable: "consideramos importante", "creemos que", "en nuestra opinión".

### Tipo de citas

En el texto que se guarda las citas **van por clave**, nunca escritas a mano:

- **Paráfrasis**: la clave al final de la afirmación: `…reduce el esfuerzo cognitivo [AR97D22F86].`
- **Autor al inicio de la frase**: el apellido y la clave con `:n` detrás: `Braun y Clarke [AR97D22F86:n] proponen…`. El servidor pone el año (o el número) según la norma.
- **Varias fuentes**: las claves seguidas: `[AR97D22F86][AR2E15C80C]`.
- **Cita textual**: con la página: `«…» [AR97D22F86:p. 45]`.
- **Sin fuente**: `[FALTA FUENTE]`, y aviso en el chat.
- Detalle en `references/integracion_zotero.md`. Cómo se ve cada caso en APA 7, en `references/apa7_citas.md`.

### Densidad de citas

- **Párrafo internacional**: 3-5 citas con clave de su biblioteca.
- **Párrafo nacional**: 3-5 citas con clave de su biblioteca.
- **Párrafo local**: sin citas. Observaciones del tesista marcadas como "observación de campo del autor".
- **Párrafos 4, 5 y 6**: sin citas obligatorias. Si la justificación menciona aporte teórico, puede llevar 1-2 citas.

### Citas de coherencia y discrepancia

En los párrafos 1 y 2, integrar al menos un autor que coincida con la postura del estudio (coherencia) y al menos un autor que matice o discrepa (discrepancia). No rotular explícitamente; el lector debe sentir el debate.

Ejemplo de integración natural:

> "El uso de IA generativa en aula ha mostrado efectos positivos en la autonomía del estudiante [AR97D22F86]. Sin embargo, Quispe [AR2E15C80C:n] advierte que esa misma autonomía puede reducir el esfuerzo cognitivo."

## Los 17 patrones anti-IA (obligatorios en la auditoría)

Estos patrones vienen del método humanizador-academico. La skill los aplica en la redacción y los verifica en la auditoría post-redacción de cada párrafo.

### Patrón 0 — Paralelismo de plantilla (el más grave)

Cuando el párrafo enumera elementos comparables (tres teorías, tres antecedentes, cuatro dimensiones), el modelo los describe con oraciones gemelas: misma arquitectura, mismo largo, mismo orden de componentes.

**MAL** (oraciones gemelas):
> "Autor1 [AR…:n], aplicado por Autor2 [AR…:n], permite comprender X. Autor3 [AR…:n], retomado por Autor4 [AR…:n], aporta a la comprensión de Y. Autor5 [AR…:n], extendido por Autor6 [AR…:n], ilumina Z."

**BIEN** (cada elemento con construcción distinta y peso distinto):
> "Autor1 [AR…:n] demostró que X está asociado con Y en muestras universitarias. Ese hallazgo fue confirmado por Autor2 [AR…:n] en una réplica con muestra latinoamericana. Autor3 [AR…:n], en cambio, matiza: la asociación se atenúa cuando se controla por nivel socioeconómico."

**Cómo romperlo en redacción**: cada elemento con construcción distinta. Uno con dos puntos, otro con el autor como sujeto, otro con oración corta más larga. Un autor que domina el tema se detiene en la teoría que más le importa y despacha la otra en una línea.

### Patrón 0b — Los seis tics de la reescritura

Estos aparecen cuando un modelo REESCRIBE para sonar humano. Aunque no se aplique aquí como reescritura, la skill los vigila en cada párrafo generado.

**Apertura sentenciosa que no se retoma**: "En América Latina la brecha es estructural." — Y la oración siguiente arranca por otro lado. Si al leer solo las dos primeras oraciones no se ve el enlace, la apertura sobra.

**Transición que promete sin entregar**: "Esa distancia tiene, en Suecia, una explicación de otro orden." — Anuncia y obliga a la siguiente oración a resolverlo.

**Cierre o bisagra que anuncia importancia**: "El aporte para esta tesis es directo: si la competencia tecnológica condiciona la disposición…" — La primera mitad no informa, solo avisa que lo que viene importa.

**Enumeración yuxtapuesta con dos puntos**: tres elementos seguidos con dos puntos, ninguno desarrollado ni enlazado. Máximo UN párrafo por página puede usar este recurso.

**Simetría interna del párrafo**: cuatro movimientos del mismo tamaño, cada uno cerrado en sí mismo. Un párrafo bien escrito es asimétrico: una parte desarrollada porque importa más, otra apenas mencionada.

**Aposición que mete al autor en el medio**: "El modelo TPACK de Mishra y Koehler [AR…:n], que Galindo-Domínguez et al. [AR…:n] llevaron al terreno de la IA, es la base teórica de..." — El sujeto se enuncia, se interrumpe con la atribución y el verbo llega al final. Mejor: "Mishra y Koehler [AR…:n] propusieron el modelo TPACK. Galindo-Domínguez et al. [AR…:n] lo aplicaron al terreno de la IA."

### Patrón 0c — La frase-etiqueta y su desarrollo

Una oración corta etiqueta lo que viene y la siguiente lo desarrolla. La etiqueta no informa.

**MAL**: "El problema no se reduce al acceso." (y después vienen los datos)
**MAL**: "Ese uso ocurre en dos planos." (y después los dos planos)

**BIEN**: fundir la etiqueta con lo que desarrolla, o borrarla. Si al fundir se forman oraciones muy largas, buscar en el párrafo una oración sobrecargada (que cargue dos datos con dos fuentes distintas) y partirla.

Variante de cierre: "no es X sino Y", "no basta con X, se requiere Y". Suenan a sentencia y solo reordenan lo ya dicho.

### Patrón 1 — Inflar la importancia

Marcadores prohibidos: **constituye un hito, marca un antes y un después, ha dejado de ser X para convertirse en Y, juega un papel fundamental / crucial / clave, se erige como, refleja una tendencia más amplia, deja una huella imborrable, pilar fundamental, en un mundo cada vez más**.

El molde delata más que la palabra. "Ha dejado de ser una promesa para convertirse en una realidad" sirve para cualquier tema, y por eso no dice nada del tuyo.

### Patrón 2 — Gerundios colgados al final

Marcadores prohibidos: **evidenciando, destacando, permitiendo, fomentando, reflejando, contribuyendo a, consolidando, abarcando**.

Antes: "El modelo explicó el 45% de la varianza, evidenciando la relevancia del constructo."
Después: "El modelo explicó el 45% de la varianza."

Casi siempre la coletilla repite en gerundio lo que la oración ya dijo.

### Patrón 3 — Lenguaje promocional

Marcadores prohibidos: **enriquecedor, invaluable, robusto (fuera de estadística), integral, holístico, sinergia, amplio abanico, profundo, riguroso, novedoso, innovador, de vanguardia**.

Cuidado: "robusto" es término técnico cuando se habla de errores estándar robustos o de una prueba robusta a la no normalidad. Ahí no se toca.

### Patrón 4 — Atribución vaga

Marcadores prohibidos: **diversos autores señalan, la literatura sugiere, los expertos coinciden, numerosos estudios, se ha demostrado ampliamente**.

En un texto con referencias (como este), se reemplaza por el autor concreto que ya está citado. No inventar el autor jamás. Si no hay un autor concreto en la biblioteca del tesista para respaldar, la afirmación se elimina o se marca `[FALTA FUENTE]`, con aviso en el chat.

### Patrón 5 — Evitar el verbo ser

Marcadores prohibidos: **constituye, representa, se configura como, se erige como, deviene en, cuenta con, posee, ostenta**.

Excepción: "La muestra estuvo constituida por 120 docentes" es fórmula de tesis y muchas veces el asesor la exige. Ahí se respeta. Fuera de la metodología, "es" suele ser mejor.

### Patrón 6 — Nominalización en cadena

Antes: "la implementación de estrategias de fortalecimiento de las competencias digitales del profesorado"
Después: "fortalecer las competencias digitales de los docentes"

Este es el patrón que más sube el largo de palabra y más baja las palabras funcionales. Atacarlo mueve dos indicadores a la vez.

### Patrón 7 — Regla de tres ornamental

Distinguir. Tres elementos que son tres hechos distintos se quedan. Tres que dicen lo mismo con distinta palabra se recortan a uno.

MAL: "cómo, en qué medida y con qué efectos" (es una sola pregunta escrita tres veces).
MAL: "novedoso, innovador y disruptivo".
BIEN: "cómo".

### Patrón 8 — Rotación de sinónimos

En texto académico esto es doblemente grave: cambiar "variable latente" por "constructo subyacente" y luego por "dimensión no observada" confunde al lector y viola la norma de precisión terminológica. El término técnico se repite, no se rota. Los detectores además leen la repetición local como señal humana.

### Patrón 9 — Rayas largas

La versión final no lleva ninguna raya larga (—) ni corta (–). Se reemplazan por punto, coma, dos puntos o paréntesis. Antes de entregar, buscar el carácter Unicode U+2014 (—) y U+2013 (–) en el documento y sustituir.

### Patrón 10 — Contrastes fabricados y falsa profundidad

Marcadores prohibidos: **sin embargo, esto contrasta con un fenómeno menos visible; lo cierto es que; en el fondo; la verdadera pregunta es; más allá de**.

Anuncian una revelación y entregan una idea corriente. Se dice la idea y ya.

### Patrón 11 — Conectores en exceso

Marcadores prohibidos: **asimismo, además, por consiguiente, en este sentido, cabe destacar, es importante mencionar, en tal sentido, por otro lado**.

Uno o dos por página es escritura normal. Uno por párrafo es tic. "Cabe destacar que" y "es importante mencionar que" casi siempre se borran enteros sin pérdida.

### Patrón 12 — Cierres optimistas

Marcadores prohibidos: **"El futuro se presenta prometedor", "queda un camino por recorrer", "sin duda representa un aporte"**.

Se corta el párrafo y se termina en el último dato concreto.

### Patrón 13 — Restos de chatbot

Marcadores prohibidos: **"Espero que esto te ayude", "a continuación se presenta", "en resumen", "¿te gustaría que profundice?"**.

A veces quedan pegados en el documento.

### Patrón 14 — Formato

Prohibido: **negritas mecánicas, listas con encabezado en negrita y dos puntos, títulos con Mayúscula En Cada Palabra, emojis, comillas curvas**.

En prosa académica formal, la negrita se reserva para títulos de sección. Nada de negritas dentro del párrafo.

## Metas numéricas de estilo (auditoría cuantitativa)

Estas metas salen de calibración real contra detectores de IA con textos de tesis en español. Son un piso, no una garantía: prosa académica formal escrita por humanos puntúa alto en estos sistemas de forma rutinaria.

### Metas por párrafo

- **Dispersión relativa de largos de oración** (desviación estándar sobre media): ≥ 0.45. Este es el indicador más fuerte. La IA escribe todas las oraciones del mismo largo.
- **Largo medio de palabra**: ≤ 5.3 caracteres. Bajarlo se logra prefiriendo la palabra corriente sobre la culta cuando ambas dicen lo mismo: "usar" en vez de "utilizar", "muestra" en vez de "evidencia", "sobre" en vez de "en torno a". No aplica a terminología técnica.
- **Palabras funcionales por encima del 40%** (artículos, preposiciones, conjunciones, pronombres). Suben solas cuando se rompen las cadenas nominales en verbos y se usan pronombres.
- **Al menos un 15% de oraciones de 8 palabras o menos**.
- **Largo medio de oración**: apuntar a 20 aproximadamente, sin obsesionarse. La media importa menos que la variación.

### Cómo subir la variación sin sonar entrecortado

Aquí hay una tensión real. Encadenar frases cortas genera drama fabricado, que es a su vez un patrón de IA. Pero la variación exige frases cortas.

**Regla que resuelve el conflicto**: las frases cortas cargan información, no énfasis. "Hace tres años casi no ocurría" es un dato en cinco palabras y funciona. "Y todo cambió." es una frase corta vacía y suena a guion.

El otro recurso: intercalar de verdad. Después de tres o cuatro oraciones cortas conviene una larga de 30-40 palabras con subordinadas, para que el ritmo no se vuelva uniforme por el otro extremo.

### Auditoría post-redacción cuantitativa (obligatoria)

Después de redactar cada párrafo, la skill mide y reporta:

```
AUDITORÍA CUANTITATIVA — Párrafo [N]

Métricas:
- Cantidad de oraciones: [N]
- Largo medio de oración: [N] palabras
- Dispersión relativa (DE / media): [N] → META ≥ 0.45
- Largo medio de palabra: [N] caracteres → META ≤ 5.3
- % palabras funcionales: [N]% → META ≥ 40%
- % oraciones ≤ 8 palabras: [N]% → META ≥ 15%
- Oración más larga: [N] palabras (regla: no pasar de 45)

Auditoría de 17 patrones:
- Patrón 0 (paralelismo): [PASA / MARCÓ, línea X]
- Patrón 0b (tics reescritura): [PASA / MARCÓ, cuál]
- Patrón 0c (frase-etiqueta): [PASA / MARCÓ, cuál]
- Patrón 1 (inflar importancia): [PASA / MARCÓ, palabra]
- Patrón 2 (gerundios colgados): [PASA / MARCÓ, palabra]
- Patrón 3 (lenguaje promocional): [PASA / MARCÓ, palabra]
- Patrón 4 (atribución vaga): [PASA / MARCÓ, dónde]
- Patrón 5 (evitar verbo ser): [PASA / MARCÓ, palabra]
- Patrón 6 (nominalización cadena): [PASA / MARCÓ, dónde]
- Patrón 7 (regla de tres): [PASA / MARCÓ, dónde]
- Patrón 8 (rotación sinónimos): [PASA / MARCÓ, término técnico]
- Patrón 9 (rayas largas): [PASA / MARCÓ, cantidad]
- Patrón 10 (contrastes fabricados): [PASA / MARCÓ, dónde]
- Patrón 11 (conectores en exceso): [PASA / MARCÓ, cuántos]
- Patrón 12 (cierres optimistas): [PASA / MARCÓ, dónde]
- Patrón 13 (restos chatbot): [PASA / MARCÓ, cuál]
- Patrón 14 (formato): [PASA / MARCÓ, cuál]

Resumen: [X de 17 checks PASAN]

Si algún check MARCÓ, re-redactar el párrafo antes de avanzar.
```

## Cuándo parar de reescribir

Si tras dos reescrituras el párrafo sigue marcando patrones, el problema ya no es la redacción sino el CONTENIDO. Hay contenidos con piso: una enumeración de teorías con autor y año, una lista de antecedentes, una descripción de diseño metodológico. Esa es la forma que tiene ese contenido.

Ahí lo honesto es decirlo y proponer una salida de contenido, no de estilo. Ejemplo: si el párrafo internacional tiene 5 teorías y no logra bajar el paralelismo, la solución es reducir a 3 teorías con distinto peso, no seguir retorciendo la prosa. Cinco teorías merecen el capítulo II, no el párrafo 1 del Cap I.

## Falsos positivos del texto académico

Esta lista importa tanto como el catálogo. Un auditor que no la respeta destroza el trabajo.

- **La voz pasiva y la impersonal** son norma del género en metodología y resultados. "Se aplicó el instrumento a 120 docentes" está bien escrito.
- **Términos técnicos**: "significativo", "significancia", "robusto" (en estadística), "correlación", "consistencia interna". No son vocabulario inflado.
- **La repetición del término técnico es obligatoria**. No es pobreza léxica.
- **Fórmulas institucionales** ("El presente estudio tuvo como objetivo", "La muestra estuvo conformada por") suelen venir exigidas por la guía de la universidad. Preguntar antes de tocarlas.
- **Citas textuales, referencias, datos estadísticos, nombres de autores, títulos de tablas y figuras**: no se tocan nunca, ni para mejorar la redacción.
- **Oraciones largas por sí solas no prueban nada**. Un párrafo de discusión bien articulado puede tener 45 palabras en una oración. El problema es que TODAS tengan 45.

## Reglas específicas por párrafo

### Párrafo 1 — Problemática internacional

**Propósito**: mostrar que el problema es relevante a escala global, con evidencia científica reciente.

**Contenido**:

- Iniciar con un dato concreto del fenómeno a nivel internacional. Usar preferentemente la **cifra oficial verificada en el Paso 6.5** (UNESCO, OMS, OIT, OCDE, Banco Mundial, según el tema), con la clave del informe del organismo (si no está en su biblioteca, `[FALTA FUENTE]` y aviso). NO abrir con "En el panorama global..." ni "En el contexto internacional actual...".
- Si en el Paso 6.5 no se consiguió cifra internacional verificable, abrir con el hallazgo más concreto del corpus de fuentes. NUNCA inventar una cifra ni atribuirla a un organismo sin haberla verificado.
- Citar 3-5 autores que han abordado el problema (de las fuentes internacionales de su biblioteca, con clave).
- Incluir al menos una cita de coherencia y una de discrepancia.
- Aterrizar el problema en términos de la práctica académica, laboral o profesional de la población del estudio.
- **Mencionar el ODS** confirmado en el Paso 6.5. Va acá y en ningún otro párrafo. Es una mención breve, de una frase, que conecta el problema global con el objetivo de desarrollo sostenible al que la tesis aporta.

**Cómo se redacta la mención al ODS (regla dura)**

Se integra en la prosa, no se anuncia. Formas que funcionan:

```
BIEN: "...una brecha que compromete directamente el ODS 4,
       Educación de calidad, en su meta de asegurar
       competencias pertinentes para el empleo."

BIEN: "El problema se inscribe en la agenda del ODS 3, Salud
       y bienestar, donde la cobertura de atención prenatal
       sigue siendo una deuda pendiente en la región."

MAL:  "Cabe destacar que la presente investigación se alinea
       con el ODS 4." (anuncio vacío, patrón de IA)

MAL:  "Este estudio contribuye a los ODS 3, 4, 5 y 10."
       (enumeración sin contenido)
```

Reglas:

- **Un solo ODS.** El que el tesista confirmó en el Paso 6.5. Si confirmó dos, se menciona el principal y el segundo se omite.
- **Se nombra con su número Y su título** la primera vez ("ODS 4, Educación de calidad"), no solo el número.
- **No se inventa la meta.** Si se menciona una meta concreta del ODS, tiene que ser una meta real de ese objetivo. Si no se está seguro de la redacción exacta de la meta, se menciona el ODS sin bajar a la meta.
- **Si el tesista no confirmó ningún ODS** en el Paso 6.5, el párrafo se escribe sin la mención. No se elige uno por cuenta propia.

**Estructura sugerida** (con asimetría deliberada, ROMPER el paralelismo):

1. Frase de apertura con un dato o hallazgo internacional concreto (12-18 palabras).
2. Una oración desarrollada con la cita más relevante (25-35 palabras).
3. Dos oraciones cortas con datos adicionales (8-14 palabras cada una).
4. Una oración larga que introduce discrepancia (30-40 palabras).
5. Frase de cierre que vincula con la población concreta y, en la misma o en la siguiente, la mención al ODS (15-25 palabras).

**Extensión**: 150-220 palabras.

### Párrafo 2 — Problemática nacional

**Propósito**: mostrar cómo el problema se manifiesta en el país declarado, con evidencia local.

**Contenido**:

- Datos del país: usar la **cifra nacional verificada en el Paso 6.5** (INEI/INEGI/DANE/INE/INEC según país), con su clave. Complementar con estudios nacionales de su biblioteca o de la búsqueda complementaria del Paso 3, ya añadidos con su clave.
- Distinguir siempre el año del dato del año del informe: "según el censo de 2022, publicado por el INEI en 2024".
- 3-5 citas de autores que han estudiado el fenómeno en el país.
- Vincular con la práctica nacional o regional de la población.

**Estructura sugerida** (asimétrica):

1. Frase de apertura con dato nacional concreto (no genérico).
2. Una oración con la cita más importante del país.
3. Una oración corta con dato regional.
4. Una oración que aterriza el problema en el tipo de institución del tesista.

**Extensión**: 150-220 palabras.

### Párrafo 3 — Problemática local

**Propósito**: aterrizar el problema en el contexto específico del tesista (su institución, su población concreta).

**Regla dura**: este párrafo NO se puede redactar sin haber ejecutado el Paso 6 (recoger observaciones del tesista). Si el checkpoint del Paso 6 está en PENDIENTE, NO redactar el párrafo local. NUNCA inventar observaciones.

**Contenido**:

- Observaciones recogidas en el Paso 6 de la skill.
- Sin citas científicas. Frases tipo "se ha observado en la institución...", "el autor identificó que...", "en conversaciones informales con docentes/colaboradores...".
- Puede incluir datos locales si el tesista los tiene (matrículas, indicadores institucionales).

**Extensión**: 120-180 palabras.

### Párrafo 4 — Pregunta de investigación

**Propósito**: formular la pregunta general y las específicas.

**Contenido**:

- Frase de transición breve.
- Pregunta general con la estructura: ¿[verbo: cómo se relaciona / qué efecto tiene / cuál es el nivel de] [V1] [conector: con / en / sobre] [V2] en [Población] de [Contexto], [Año]?
- Preguntas específicas: una por cada dimensión de V1.

**Extensión**: 100-150 palabras.

### Párrafo 5 — Objetivos

**Propósito**: declarar el objetivo general y los específicos.

**Contenido**:

- Frase de transición de la pregunta al objetivo.
- Objetivo general: empieza con verbo en infinitivo (Determinar, Analizar, Establecer, Comprender).
- Objetivos específicos: misma cantidad que las preguntas específicas; verbos como Identificar, Describir, Caracterizar, Comparar, Medir.

**Extensión**: 100-150 palabras.

### Párrafo 6 — Justificación

**Propósito**: argumentar por qué vale la pena hacer esta investigación, desde cuatro ángulos integrados en prosa (no separados con subtítulos).

**Contenido**:

1. **Justificación práctica**: cómo los resultados pueden mejorar la práctica.
2. **Justificación teórica**: cómo el estudio amplía conocimiento o aporta al debate.
3. **Justificación metodológica**: qué aporte hace en instrumento o método.
4. **Justificación social**: qué impacto tiene en la comunidad o sector más amplio. **El ODS NO se menciona acá**: su única aparición es en el párrafo 1 (problemática internacional). Repetirlo en la justificación suena a relleno y el jurado lo lee como tal. Si el aporte social del estudio coincide con el ODS, se describe el aporte concreto sin volver a nombrar el objetivo.

**Extensión**: 200-280 palabras.

## Antes de redactar: chequeo de fuentes

Antes de empezar el párrafo 1, la skill debe haber:

- [ ] Confirmado que las fuentes del corpus están en su biblioteca, con clave (`buscar_fuentes` / `mis_fuentes`).
- [ ] Leído autores, año y abstract de cada una.
- [ ] Clasificado fuentes en internacionales vs nacionales.
- [ ] Ejecutado búsqueda complementaria de nacionales si eran < 3.
- [ ] Identificado al menos 3 autores con datos concretos para el párrafo internacional.
- [ ] Identificado al menos 3 autores con datos concretos para el párrafo nacional.
- [ ] Recogido las observaciones locales del tesista (Paso 6 completado con checkpoint verde).

Si falta alguno, no redactar. Volver al paso correspondiente.

## Después de redactar: checklist de validación

Marcar al cierre, antes de avanzar al Paso 8:

```
- [ ] Párrafo 1: 3-5 citas con clave, mezcla coherencia y discrepancia,
       ejemplos concretos, tercera persona, auditoría cuantitativa
       aprobada, auditoría 17 patrones aprobada.
- [ ] Párrafo 2: 3-5 citas con clave del país declarado, mezcla
       coherencia y discrepancia, ejemplos concretos, auditoría OK.
- [ ] Párrafo 3: observaciones locales del tesista recogidas
       en Paso 6, sin citas inventadas, marca de "observación
       de campo".
- [ ] Párrafo 4: pregunta general bien estructurada, específicas
       coherentes con dimensiones.
- [ ] Párrafo 5: objetivos con verbos en infinitivo, alineados
       1 a 1 con preguntas.
- [ ] Párrafo 6: 4 ángulos de justificación integrados sin
       subtítulos visibles.
- [ ] Toda cita es una clave [AR…] de su biblioteca; ninguna escrita a mano.
- [ ] Cero em dashes.
- [ ] Cero patrones de los 14 sin resolver.
- [ ] Metas cuantitativas: dispersión ≥ 0.45, largo palabra
       ≤ 5.3, funcionales ≥ 40%, oraciones cortas ≥ 15%.
```

Si una clave no salió de una búsqueda, BUSCAR la fuente con `buscar_fuentes` antes de avanzar. Si no se encuentra, la afirmación va `[FALTA FUENTE]` o se elimina. No guardar nada sin respaldo.
