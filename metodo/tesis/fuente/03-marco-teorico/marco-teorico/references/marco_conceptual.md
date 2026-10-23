# Marco conceptual

El marco conceptual es la sección más corta del Capítulo II, pero la más leída en sustentación. Aquí se definen los términos clave del estudio. Cada definición es corta, citada y aplicable al estudio del tesista.

> Las claves `[AR…]` de los ejemplos son marcadores: en el texto real va la clave que devolvió la búsqueda o la biblioteca. El servidor la convierte en la cita según la norma del proyecto.

## Cuántos términos definir

- **Mínimo**: 8 términos.
- **Máximo**: 12 términos.
- **Si el reglamento de la universidad pide un número específico**, respetar el reglamento.

## Cómo elegir los términos

La skill propone una lista inicial al tesista. La lista se construye con:

### Términos obligatorios

1. **Las dos variables** principales del estudio.
2. **Cada dimensión** de cada variable (las del Anexo 2 del Capítulo I). Si V1 tiene 4 dimensiones y V2 tiene 7, hay 11 dimensiones que potencialmente entran. En este caso, se priorizan las dimensiones que aparecen en hipótesis específicas o tienen mayor peso analítico.

### Términos técnicos clave

3. **Instrumentos mencionados**: CCTDI, AI Literacy Scale, etc.
4. **Constructos teóricos asociados**: si la tesis trabaja "disposición al pensamiento crítico", también suelen definirse "pensamiento crítico" general, "razonamiento", etc.
5. **Términos estadísticos relevantes**: alfa de Cronbach, correlación de Pearson, validez de contenido (si son centrales en la metodología).
6. **Términos del contexto**: por ejemplo, "educación secundaria", "I.E. pública", si requieren definición operacional.

### Cómo presenta la skill la propuesta

Usar `ask_user_input_v0` con multi_select. Presentar 10-15 términos candidatos para que el tesista marque los que incluir. Después puede agregar nuevos por texto libre.

Antes de redactar, cada término elegido necesita una fuente con clave que lo defina: se busca con `buscar_fuentes` (`tema` en inglés, `temaOriginal` en español, `pais`) o en `mis_fuentes`. Si un término no tiene fuente, se le dice al tesista en el chat y la definición citada va con `[FALTA FUENTE]` hasta que la tenga.

## Estructura de cada definición

Cada término tiene dos partes obligatorias:

1. **Definición citada**: del autor de referencia, con la clave de su fuente.
2. **Definición operacional**: cómo se entiende el término en el contexto del estudio del tesista.

Aunque cada término es un bloque autocontenido, los términos se redactan **en prosa académica continua**, no en lista con bullets.

## Formato visual de cada término

```
**[Nombre del término]**. [Autor] [AR…:n] define… (o la
definición parafraseada con la clave al final [AR…]).
En el presente estudio, [definición operacional aplicada al
contexto del tesista].
```

El nombre del término va en negrita o cursiva al inicio del párrafo. Luego sigue inmediatamente la prosa con las dos partes.

## Ejemplos por área

### Educación / Tecnología educativa

```
**Disposición al pensamiento crítico**. Facione [AR…:n] define
este constructo como la predisposición actitudinal de un
individuo a aplicar procesos de razonamiento estructurado,
búsqueda de verdad, análisis y juicio prudente al enfrentar
problemas o información compleja. En el presente estudio se
entiende disposición al pensamiento crítico como la tendencia,
medida con el CCTDI adaptado, de los estudiantes de cuarto y
quinto de secundaria a cuestionar, analizar y verificar la
información que reciben de herramientas de inteligencia
artificial generativa, en sus siete dimensiones operacionales.

**Alfabetización en inteligencia artificial**. Long y Magerko
[AR…:n] proponen este constructo como el conjunto de
competencias que permiten a un usuario no especializado
interactuar críticamente con sistemas de inteligencia
artificial. En el presente estudio, la alfabetización en IA se
operacionaliza en cuatro dimensiones (conocimiento, uso,
evaluación crítica y ética) que serán medidas con un
cuestionario adaptado a estudiantes de secundaria.

**IA generativa**. Tang et al. [AR…:n] describen la IA
generativa como una familia de sistemas computacionales basados
en grandes modelos de lenguaje capaces de producir texto,
imágenes o código a partir de instrucciones del usuario. En el
presente estudio se consideran como IA generativa
específicamente las herramientas ChatGPT y Gemini, que son las
de mayor adopción en la población estudiada.
```

### Administración / Psicología organizacional

```
**Clima organizacional**. Litwin y Stringer [AR…:n] lo definen
como la percepción compartida que los miembros de una
organización construyen sobre su ambiente de trabajo,
integrando dimensiones de liderazgo, estructura, recompensa y
relaciones interpersonales. En el presente estudio, el clima
organizacional se entiende como la percepción de los
colaboradores de la empresa retail estudiada respecto a las
condiciones laborales, el liderazgo de sus jefes directos y las
relaciones con sus compañeros.
```

### Ciencias de la salud

```
**Adherencia al tratamiento**. La Organización Mundial de la
Salud [AR…:n] define la adherencia como el grado en que el
comportamiento de una persona en cuanto a tomar medicamentos,
seguir un régimen alimentario o cambiar estilos de vida
corresponde con las recomendaciones acordadas con un
profesional de la salud. En el presente estudio, la adherencia
al tratamiento se evaluará en pacientes con diabetes tipo 2
atendidos en el centro de salud estudiado, mediante el
cuestionario MMAS-8 adaptado al español.
```

## Reglas críticas

### Sobre las fuentes

- **Solo fuentes académicas**. Prohibido citar Wikipedia, blogs personales, sitios sin autor académico o sin revisión por pares.
- **Clave obligatoria** en la definición citada. Nada de citas escritas a mano: el año y el formato los pone el servidor según la norma del proyecto.
- **Sin citas textuales largas**. Si la definición del autor pasa de 40 palabras, parafrasear con cambio estructural y mantener la clave.

### Sobre la definición operacional

- **Debe ser específica al estudio del tesista**, no genérica.
- **Conecta con el instrumento** y la población. Por ejemplo: "se medirá con el CCTDI adaptado en estudiantes de 4° y 5° de secundaria de una I.E. pública".
- **Sin redundancia con la definición citada**. Si la operacional dice lo mismo que la citada con otras palabras, falta especificidad.

### Sobre la prosa

- **Cada término es un párrafo**. No mezclar definiciones de varios términos en el mismo párrafo.
- **Sin transiciones forzadas** entre términos. El orden suele ser alfabético o por relevancia conceptual (variable principal → dimensiones → términos asociados).
- **Tercera persona** siempre.

## Antiejemplos

### Antiejemplo 1: definición sin cita

```
**Pensamiento crítico**. Es la capacidad de pensar de manera
reflexiva y razonada. Sirve para tomar buenas decisiones.
```

Problema: sin fuente académica, sin definición operacional. Es definición de diccionario.

### Antiejemplo 2: definición operacional ausente

```
**Pensamiento crítico**. Facione [AR…:n] define el pensamiento
crítico como el juicio autorregulado y propositivo basado en
interpretación, análisis y evaluación.
```

Problema: solo está la mitad. Falta cómo se entiende en este estudio específico.

### Antiejemplo 3: lista con bullets

```
**Términos clave**:
• Pensamiento crítico
• IA generativa
• Disposición
• Alfabetización
```

Problema: solo enumeración, sin definiciones. Esto no es marco conceptual.

### Antiejemplo 4: definición de Wikipedia

```
**IA generativa**. Según Wikipedia, es un tipo de inteligencia
artificial que puede generar texto, imágenes u otro tipo de
medios en respuesta a las peticiones del usuario.
```

Problema: fuente no académica. Inaceptable en tesis.
