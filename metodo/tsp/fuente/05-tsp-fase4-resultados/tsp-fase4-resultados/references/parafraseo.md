# Paráfrasis y prevención de plagio + auditoría anti-IA

Esta referencia cubre dos frentes en un solo documento porque son inseparables en la práctica:

1. **Paráfrasis correcta**: para evitar plagio (causa #1 de observación grave en sustentación).
2. **Auditoría anti-IA**: para evitar redacción que suene a modelo, con los 17 patrones del método humanizador-academico adaptados al capítulo de marco teórico.

**Principio de fondo**: la redacción humana es imperfecta. Un párrafo escrito por una persona tiene una parte que se alarga porque el autor sabía más de eso, una aclaración que sobra, alguna oración que cierra torcida. Lo que delata a la redacción con IA no es un error: es que no hay ninguno.

**Segunda regla dura: humanizar es RESTAR, no reemplazar**. No cambiar "se sustenta en" por "sostienen" (dos adornos), ni "extendido al contexto de" por "llevaron al terreno de". Cambiar "se sustenta en" por "usa" o "se basa en". Se quita el adorno, no se reemplaza.

## Parte 1 — Paráfrasis (prevención de plagio)

### Las 3 reglas obligatorias de paráfrasis del método

Una buena paráfrasis cambia **tres cosas a la vez**:

1. **La estructura de la oración**. Si el original es "sujeto + verbo + complemento", la paráfrasis puede empezar por el complemento, usar voz pasiva, o partir la oración en dos.
2. **Las palabras conectoras y la sintaxis**. No solo sustantivos: también verbos y conectores deben cambiar.
3. **La voz**. La paráfrasis debe sonar a redacción académica latinoamericana, no al inglés técnico ni al estilo del original.

### Cómo aplicar la regla a cada cita

Para cada idea que la skill toma de una fuente subida:

1. Lee el fragmento original del abstract.
2. Identifica la idea central (qué dice realmente, no cómo lo dice).
3. Reescribe la idea con cambio estructural completo en español académico.
4. Marca la cita con la clave de la fuente al final de la afirmación: `[AR97D22F86]`, o `[AR97D22F86:n]` detrás del nombre si el autor va en la frase (ver `integracion_zotero.md`). Nunca «(Apellido, año)» escrito a mano: el servidor la escribe en la norma del proyecto.
5. Verifica que la paráfrasis **no comparta más de 5 palabras consecutivas** con el original.

Si la paráfrasis suena demasiado al original, reformularla antes de incluir en el documento.

### Test de calidad de paráfrasis

Antes de incluir cualquier cita parafraseada, la skill aplica este test interno:

```
- [ ] ¿La estructura sintáctica es distinta al original?
- [ ] ¿Los verbos principales son distintos?
- [ ] ¿Los conectores son distintos?
- [ ] ¿No hay más de 5 palabras seguidas iguales al original?
- [ ] ¿La voz es académica latinoamericana, no calco del inglés?
- [ ] ¿La afirmación lleva su clave [AR…] (o [FALTA FUENTE]) donde corresponde?
```

Si todas las casillas están marcadas, la paráfrasis es válida.

### Ejemplos de paráfrasis correcta vs. plagio disfrazado

**Caso 1**

Original (Tian y Zhang, 2025, abstract):

> "The intensive use of generative artificial intelligence among undergraduate students is significantly associated with a decrease in critical thinking skills, mediated by cognitive fatigue and moderated by AI literacy levels."

**Plagio disfrazado** (cambio solo de sinónimos):

> El uso intensivo de la inteligencia artificial generativa entre los estudiantes universitarios está significativamente asociado con una disminución de las habilidades de pensamiento crítico, mediada por la fatiga cognitiva y moderada por los niveles de alfabetización en IA (Tian y Zhang, 2025).

Problema: misma estructura, mismo orden de ideas, mismos verbos, mismos conectores. Es traducción, no paráfrasis.

**Paráfrasis correcta** (cambio estructural + voz):

> Tian y Zhang (2025) identificaron una asociación negativa entre la intensidad de uso de IA generativa y el pensamiento crítico en universitarios. Esta relación, según los autores, se explica parcialmente por el efecto mediador de la fatiga cognitiva, y se modifica según el nivel de alfabetización en IA que tenga el estudiante.

Lo que cambió: la oración se partió en dos, el sujeto se invirtió (ahora son los autores quienes "identificaron"), los verbos cambiaron, los conectores son nuevos.

**Caso 2**

Original (Wu y Zhang, 2025):

> "Generative AI use in secondary education shows asymmetric effects depending on student profile, with stronger benefits for high-performing students and risks of dependency for struggling learners."

**Paráfrasis correcta**:

> Wu y Zhang (2025) advierten que la IA generativa en secundaria no produce efectos uniformes en todos los estudiantes. Sus hallazgos sugieren que los adolescentes con mejor rendimiento académico aprovechan estas herramientas como apoyo, mientras que aquellos con dificultades de aprendizaje tienden a desarrollar patrones de dependencia.

**Caso 3**

Original (Marín et al., 2025):

> "The academic use of AI in Peruvian universities presents unresolved ethical challenges, including the lack of institutional criteria to distinguish legitimate use from use that substitutes the student's cognitive effort."

**Plagio disfrazado**:

> El uso académico de la IA en universidades peruanas presenta retos éticos no resueltos, incluyendo la falta de criterios institucionales para distinguir el uso legítimo del uso que sustituye el esfuerzo cognitivo del estudiante (Marín et al., 2025).

Problema: traducción casi calcada.

**Paráfrasis correcta**:

> Marín et al. (2025) advierten que las universidades peruanas aún no han resuelto varios dilemas éticos vinculados al uso académico de la IA. Entre los problemas destacados, los autores señalan la ausencia de marcos institucionales claros para diferenciar entre un uso legítimo de la tecnología y un uso que reemplaza el trabajo cognitivo que se espera del estudiante.

### Cita textual: cuándo y cómo

La cita textual debe ser excepcional. Reglas:

- **Máximo 40 palabras** entre comillas.
- **Solo si la frase es absolutamente esencial** y no se puede parafrasear sin perder significado.
- **Siempre con la clave y la página**: `«…» [AR97D22F86:p. 45]`, si la fuente la provee.
- **Traducir al español** si el original está en inglés, indicando "(traducción propia)" después de la cita.

### Recomendación al tesista al cerrar

Sugerir al tesista que, antes de entregar al asesor, pase el documento por Turnitin (si la universidad lo facilita en borradores) o por una herramienta similar. Objetivo: **menos de 20% de coincidencias** en pregrado peruano, idealmente menos de 15%. Si sale más alto, los párrafos problemáticos deben reescribirse aplicando las 3 reglas.

## Parte 2 — Los 17 patrones anti-IA

Estos patrones vienen del método humanizador-academico. La skill los aplica en la redacción de bases teóricas, antecedentes y marco conceptual, y los verifica en la auditoría post-redacción de cada bloque.

### Patrón 0 — Paralelismo de plantilla (el más grave)

Cuando el bloque enumera elementos comparables (tres teorías rivales, cuatro dimensiones, cinco antecedentes), el modelo los describe con oraciones gemelas: misma arquitectura, mismo largo, mismo orden de componentes.

**MAL** (oraciones gemelas para describir 3 antecedentes):

> "Autor1 (2023), aplicado por Autor2 (2024), permite comprender X. Autor3 (2023), retomado por Autor4 (2024), aporta a la comprensión de Y. Autor5 (2023), extendido por Autor6 (2024), ilumina Z."

**BIEN** (cada elemento con construcción distinta):

> "Autor1 (2023) demostró que X está asociado con Y en muestras universitarias. Ese hallazgo fue confirmado por Autor2 (2024) en una réplica con muestra latinoamericana. Autor3 (2023), en cambio, matiza: la asociación se atenúa cuando se controla por nivel socioeconómico."

Dónde aparece con más fuerza en el Cap II: bloque de antecedentes internacionales (varios estudios en cadena), descripción de dimensiones (una tras otra), bases teóricas cuando se listan aportaciones de la teoría.

### Patrón 0b — Los seis tics de la reescritura

**Apertura sentenciosa que no se retoma**: "En América Latina la brecha es estructural." — Y la oración siguiente arranca por otro lado. Si al leer solo las dos primeras oraciones no se ve el enlace, la apertura sobra.

**Transición que promete sin entregar**: "Esa distancia tiene, en el ámbito educativo, una explicación de otro orden."

**Cierre o bisagra que anuncia importancia**: "El aporte para esta tesis es directo: si X condiciona Y..." — La primera mitad no informa, solo avisa.

**Enumeración yuxtapuesta con dos puntos**: tres elementos seguidos con dos puntos, ninguno desarrollado. Máximo UN párrafo por página puede usar este recurso.

**Simetría interna del párrafo**: cuatro movimientos del mismo tamaño, cada uno cerrado en sí mismo. Un párrafo bien escrito es asimétrico.

**Aposición que mete al autor en el medio**: "El modelo TPACK de Mishra y Koehler (2006), que Galindo-Domínguez et al. (2024) llevaron al terreno de la IA, es la base teórica de..." — El sujeto se enuncia, se interrumpe con la atribución y el verbo llega al final. Mejor: "Mishra y Koehler (2006) propusieron el modelo TPACK. Galindo-Domínguez et al. (2024) lo aplicaron al terreno de la IA."

### Patrón 0c — La frase-etiqueta y su desarrollo

Una oración corta etiqueta lo que viene y la siguiente lo desarrolla. La etiqueta no informa.

**MAL**: "El problema no se reduce al acceso." (y después vienen los datos)
**MAL**: "Ese uso ocurre en dos planos." (y después los dos planos)

**BIEN**: fundir la etiqueta con lo que desarrolla, o borrarla.

### Patrón 1 — Inflar la importancia

Marcadores prohibidos: **constituye un hito, marca un antes y un después, ha dejado de ser X para convertirse en Y, juega un papel fundamental / crucial / clave, se erige como, refleja una tendencia más amplia, pilar fundamental, en un mundo cada vez más**.

El molde delata más que la palabra.

### Patrón 2 — Gerundios colgados al final

Marcadores prohibidos: **evidenciando, destacando, permitiendo, fomentando, reflejando, contribuyendo a, consolidando, abarcando**.

Antes: "El modelo explicó el 45% de la varianza, evidenciando la relevancia del constructo."
Después: "El modelo explicó el 45% de la varianza."

### Patrón 3 — Lenguaje promocional

Marcadores prohibidos: **enriquecedor, invaluable, robusto (fuera de estadística), integral, holístico, sinergia, amplio abanico, profundo, riguroso, novedoso, innovador, de vanguardia**.

Cuidado: "robusto" es término técnico cuando se habla de errores estándar robustos o de una prueba robusta a la no normalidad. Ahí no se toca.

### Patrón 4 — Atribución vaga

Marcadores prohibidos: **diversos autores señalan, la literatura sugiere, los expertos coinciden, numerosos estudios, se ha demostrado ampliamente**.

En marco teórico, reemplazar por el autor concreto que ya está citado. NO inventar autor jamás. Si no hay respaldo en el corpus del tesista, la afirmación se elimina o se marca `[FALTA FUENTE]` y se le avisa al tesista en el chat.

### Patrón 5 — Evitar el verbo ser

Marcadores prohibidos: **constituye, representa, se configura como, se erige como, deviene en, cuenta con, posee, ostenta**.

Excepción: "La muestra estuvo constituida por 120 docentes" es fórmula de tesis. Fuera de metodología, "es" suele ser mejor.

### Patrón 6 — Nominalización en cadena

Antes: "la implementación de estrategias de fortalecimiento de las competencias digitales del profesorado"
Después: "fortalecer las competencias digitales de los docentes"

Este es el patrón que más sube el largo de palabra y más baja las palabras funcionales. Atacarlo mueve dos indicadores a la vez.

### Patrón 7 — Regla de tres ornamental

Tres elementos que dicen lo mismo con distinta palabra → dejar UNO.

MAL: "novedoso, innovador y disruptivo".
BIEN: "novedoso" (o el término más preciso).

### Patrón 8 — Rotación de sinónimos técnicos

En texto académico esto es doblemente grave: cambiar "variable latente" por "constructo subyacente" y luego por "dimensión no observada" confunde al lector y viola la norma de precisión terminológica. **El término técnico se repite, no se rota**. Los detectores además leen la repetición local como señal humana.

### Patrón 9 — Rayas largas

La versión final no lleva ninguna raya larga (—) ni corta (–). Se reemplazan por punto, coma, dos puntos o paréntesis. Antes de entregar, buscar los caracteres Unicode U+2014 (—) y U+2013 (–) en el documento y sustituir.

### Patrón 10 — Contrastes fabricados y falsa profundidad

Marcadores prohibidos: **sin embargo, esto contrasta con un fenómeno menos visible; lo cierto es que; en el fondo; la verdadera pregunta es; más allá de**.

Anuncian una revelación y entregan una idea corriente.

### Patrón 11 — Conectores en exceso

Marcadores prohibidos: **asimismo, además, por consiguiente, en este sentido, cabe destacar, es importante mencionar, en tal sentido, por otro lado**.

Uno o dos por página es escritura normal. Uno por párrafo es tic. "Cabe destacar que" y "es importante mencionar que" casi siempre se borran enteros sin pérdida.

### Patrón 12 — Cierres optimistas

Marcadores prohibidos: **"El futuro se presenta prometedor", "queda un camino por recorrer", "sin duda representa un aporte"**.

Se corta el párrafo y se termina en el último dato concreto.

### Patrón 13 — Restos de chatbot

Marcadores prohibidos: **"Espero que esto te ayude", "a continuación se presenta", "en resumen", "¿te gustaría que profundice?"**.

A veces quedan pegados en el documento por copy-paste.

### Patrón 14 — Formato

Prohibido: **negritas mecánicas dentro de párrafos, listas con encabezado en negrita y dos puntos, títulos con Mayúscula En Cada Palabra, emojis, comillas curvas**.

Excepción en marco conceptual: la primera aparición del término definido va en negrita (norma del método), pero no dentro de la definición.

## Metas cuantitativas de estilo (auditoría cuantitativa)

Estas metas salen de calibración real contra detectores de IA con textos de tesis en español. Son un piso, no una garantía.

### Metas por bloque redactado (antecedente individual, bloque de bases teóricas, definición del marco conceptual)

- **Dispersión relativa de largos de oración** (DE / media): ≥ 0.45. La IA escribe todas las oraciones del mismo largo.
- **Largo medio de palabra**: ≤ 5.3 caracteres. Prefirir palabra corriente sobre culta: "usar" > "utilizar", "muestra" > "evidencia", "sobre" > "en torno a". No aplica a terminología técnica.
- **Palabras funcionales por encima del 40%** (artículos, preposiciones, conjunciones, pronombres).
- **Al menos un 15% de oraciones de 8 palabras o menos**.
- **Ninguna oración de más de 45 palabras**.

### Cómo subir la variación sin sonar entrecortado

Las frases cortas cargan información, no énfasis. "Hace tres años casi no ocurría" es un dato en cinco palabras y funciona. "Y todo cambió." es una frase corta vacía y suena a guion.

Intercalar de verdad: después de tres o cuatro oraciones cortas conviene una larga de 30-40 palabras con subordinadas.

## Auditoría post-redacción cuantitativa (obligatoria)

Después de redactar cada bloque (cada antecedente, cada bloque de bases teóricas por variable, cada bloque del marco conceptual), la skill mide y reporta:

```
AUDITORÍA COMPLETA — [Nombre del bloque redactado]

CONTROLES ESTRUCTURALES:
- Citas detectadas: [listar cada clave [AR…] con el autor que devolvió la búsqueda]
- Citas escritas a mano —(Apellido, 2024), (1), [1]—: [N] → deben ser 0
- Total: N citas
- Extensión: [N palabras]

MÉTRICAS CUANTITATIVAS:
- Cantidad de oraciones: [N]
- Largo medio de oración: [N] palabras
- Dispersión relativa (DE/media): [N] → META ≥ 0.45 → [PASA/NO]
- Largo medio de palabra: [N] caracteres → META ≤ 5.3 → [PASA/NO]
- % oraciones ≤ 8 palabras: [N]% → META ≥ 15% → [PASA/NO]
- Oración más larga: [N] palabras (regla: ≤ 45) → [PASA/NO]

AUDITORÍA DE 17 PATRONES ANTI-IA:
- P0  (paralelismo de plantilla): [PASA / MARCÓ en línea X]
- P0b (tics de reescritura): [PASA / MARCÓ cuál]
- P0c (frase-etiqueta): [PASA / MARCÓ cuál]
- P1  (inflar importancia): [PASA / MARCÓ palabra X]
- P2  (gerundios colgados): [PASA / MARCÓ palabra X]
- P3  (lenguaje promocional): [PASA / MARCÓ palabra X]
- P4  (atribución vaga): [PASA / MARCÓ dónde]
- P5  (evitar verbo ser): [PASA / MARCÓ palabra X]
- P6  (nominalización cadena): [PASA / MARCÓ dónde]
- P7  (regla de tres): [PASA / MARCÓ dónde]
- P8  (rotación sinónimos): [PASA / MARCÓ término técnico X]
- P9  (rayas largas — o –): [PASA / MARCÓ N ocurrencias]
- P10 (contrastes fabricados): [PASA / MARCÓ dónde]
- P11 (conectores en exceso): [PASA / MARCÓ cuántos]
- P12 (cierres optimistas): [PASA / MARCÓ dónde]
- P13 (restos chatbot): [PASA / MARCÓ cuál]
- P14 (formato): [PASA / MARCÓ cuál]

VERIFICACIONES ADICIONALES:
- Tercera persona en 100% del texto: SÍ / NO
- Cada cita con clave [AR…] salida de una búsqueda: SÍ / NO (cuál falla)
- Paráfrasis pasa test (< 5 palabras seguidas iguales al
  original): SÍ / NO

RESUMEN: [X de 27 checks PASAN]
Estado: OK PARA AVANZAR / RE-REDACTAR
```

**Regla dura**: si CUALQUIER verificación devuelve MARCÓ, NO, o falla una meta cuantitativa, la skill **debe re-redactar el bloque** antes de avanzar.

**Regla dura anti-autocertificación**: la skill NO puede escribir "todo correcto" sin haber listado las citas una por una, contado las oraciones, y ejecutado las 5 métricas cuantitativas con números reales. Si el modelo no puede calcular alguna métrica con precisión (por ejemplo, palabras funcionales sin etiquetado POS), lo declara explícitamente en lugar de inventar el número.

Lo que la skill SÍ puede contar con seguridad: cantidad de oraciones, cantidad de palabras por oración (aproximada por espacios), oración más larga, rayas largas (buscando U+2014 y U+2013), y los 17 patrones anti-IA por búsqueda de marcadores literales.

## Cuándo parar de reescribir

Si tras dos reescrituras el bloque sigue marcando patrones, el problema ya no es la redacción sino el CONTENIDO. Hay contenidos con piso: una enumeración de dimensiones con autor y año, una lista de antecedentes similares en diseño, una descripción de teoría clásica. Esa es la forma que tiene ese contenido.

Ahí lo honesto es decirlo y proponer una salida de contenido, no de estilo. Ejemplo: si el bloque de bases teóricas tiene 5 aplicaciones y no logra bajar el paralelismo, reducir a 3 aplicaciones con distinto peso, no seguir retorciendo la prosa.

## Falsos positivos del texto académico

Esta lista importa tanto como el catálogo. Un auditor que no la respeta destroza el trabajo.

- **La voz pasiva y la impersonal** son norma del género en metodología y resultados. "Se aplicó el instrumento a 120 docentes" está bien escrito.
- **Términos técnicos** ("significativo", "significancia", "robusto" en estadística, "correlación", "consistencia interna", "constructo") no son vocabulario inflado.
- **La repetición del término técnico es obligatoria**. No es pobreza léxica.
- **Fórmulas institucionales** ("El presente estudio tuvo como objetivo", "La muestra estuvo conformada por") suelen venir exigidas por la guía de la universidad. Preguntar antes de tocarlas.
- **Citas textuales, referencias, datos estadísticos, nombres de autores, títulos de tablas**: no se tocan nunca.
- **Oraciones largas por sí solas no prueban nada**. Un párrafo de discusión bien articulado puede tener 45 palabras en una oración. El problema es que TODAS tengan 45.
