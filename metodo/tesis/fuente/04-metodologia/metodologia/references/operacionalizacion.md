# Operacionalización de variables

> **Subordinado al Paso 6 del SKILL.md.** La matriz de operacionalización cuantitativa ya **no se construye** en esta skill: sale completa en el Capítulo I, como Anexo 2, dentro del texto guardado de `problema-y-objetivos`, y se lee con `ver_capitulo`. Este archivo se conserva para dos cosas: **revisar la matriz recibida** con criterio, y **construir la matriz de categorización cualitativa** cuando el Anexo 2 no la trae.
>
> Las claves `[AR…]` de los ejemplos son marcadores: en el texto real va la clave que devolvió la búsqueda o la biblioteca.

## Importante: frontera con la Skill de Instrumento

La matriz llega hasta **indicadores y escala**, y en el Anexo 2 lleva además la columna **Ítems** con **rangos numéricos** (`1 a 5`, `6 a 11`), no con el texto de las preguntas. El texto de los ítems se construye en la Skill de Instrumento (Cap V), donde cada indicador se traduce en 2 a 4 preguntas concretas.

## Estructura de la matriz cuantitativa (la que llega en el Anexo 2)

Siete columnas, una tabla por variable:

| Variable | Definición conceptual | Definición operacional | Dimensiones | Indicadores | Ítems | Escala de medición |
|----------|----------------------|----------------------|-------------|-------------|-------|--------------------|

Qué revisar en cada columna:

- **Variable**: nombre exacto de V1 y V2 (igual al Cap I).
- **Definición conceptual**: del autor de la teoría base, con la clave de su fuente `[AR…]`. Una oración. Si no tiene clave, es lo primero que se señala.
- **Definición operacional**: cómo se mide en este estudio. Una oración.
- **Dimensiones**: las definitivas del Cap I. No se modifican aquí.
- **Indicadores**: 2 a 4 por dimensión. Aspectos observables o medibles.
- **Ítems**: rangos numéricos, reales o previstos.
- **Escala**: Likert 1-5, Likert 1-7, dicotómica (sí/no), ordinal, intervalo.

## Criterios para revisar los indicadores recibidos

Un indicador está bien planteado cuando:

1. **Se parece a cómo otros estudios del Cap II operacionalizaron** la misma dimensión, sin copiarlos. Si un antecedente [AR…] midió "evaluación crítica de outputs" con tres indicadores específicos, los del tesista pueden ir en la misma línea con formulación propia.
2. **Aterriza las definiciones operacionales del marco conceptual** del Cap II. Lo que se declaró en 2.3 debería reconocerse aquí.
3. **Es coherente con la población**. Debe ser observable o autoreportable por quienes responderán (no indicadores que solo apliquen a expertos si la población son adolescentes).

Si un indicador no cumple, **no se corrige por cuenta propia**: se le señala al tesista en el chat y, si decide cambiarlo, se aplica el procedimiento del Paso 6 (se corrige en el Anexo 2 y se vuelve a guardar `problema-y-objetivos` completo, con aviso).

## Ejemplo de estructura cuantitativa (ilustrativo, NO copiar literalmente)

**Advertencia crítica de uso**: el ejemplo siguiente es una **ilustración de formato**, no una plantilla. Cada tesis tiene variables, dimensiones e indicadores propios que derivan del Cap I y Cap II de ese tesista. Si dos tesis del método reciben las mismas dimensiones y los mismos indicadores para variables similares, se detecta clonación.

| Variable | Definición conceptual | Definición operacional | Dimensiones | Indicadores | Ítems | Escala de medición |
|----------|----------------------|----------------------|-------------|-------------|-------|--------------------|
| [V1 del tesista] | [Definición del autor de la teoría base] [AR…] | [Cómo se mide V1 en este estudio] | [Dimensión 1 fijada en Cap I] | [Indicador 1.1]; [1.2]; [1.3] | 1 a 6 | Likert 1-5 |
| | | | [Dimensión 2 fijada en Cap I] | [Indicador 2.1]; [2.2] | 7 a 10 | Likert 1-5 |

## Estructura de la matriz cualitativa (acá sí puede haber construcción)

Cuatro columnas:

| Categoría | Subcategorías | Indicadores observables | Técnica de recogida |
|-----------|---------------|------------------------|---------------------|

Las categorías sustituyen a las variables del cuanti. Las subcategorías son los componentes internos. Los indicadores observables son aspectos concretos detectables en el discurso o conducta. La técnica de recogida indica cómo se capturarán.

Si el Anexo 2 ya la trae, se revisa con los criterios de arriba. **Si no la trae**, se construye aquí y, con el visto bueno del tesista, se agrega al Anexo 2 de `problema-y-objetivos` siguiendo el procedimiento del Paso 6.

## Ejemplo de matriz cualitativa

| Categoría | Subcategorías | Indicadores observables | Técnica de recogida |
|-----------|---------------|------------------------|---------------------|
| Experiencia con IA generativa | Adopción inicial | Cuándo empezó a usarla; cómo la descubrió; por qué la usa | Entrevista semiestructurada |
| | Tipos de uso | Tareas en las que la usa; frecuencia; modalidad | Entrevista + observación |
| | Reflexión crítica | Cómo evalúa las respuestas; cuándo desconfía; cuándo verifica | Entrevista en profundidad |
| Significados atribuidos al pensamiento crítico | Concepción del pensamiento crítico | Qué entiende por pensar críticamente | Entrevista |
| | Relación con la IA | Cómo cree que la IA afecta su pensar | Entrevista en profundidad |

### Regla para construir indicadores sin clonar (caso cualitativo)

1. **Revisar cada antecedente del Cap II** del tesista: ¿cómo abordó ese autor esta misma categoría?
2. **Adaptar al contexto del tesista**: población, país, año, sector.
3. **NO copiar textualmente** los indicadores de un antecedente ni de este ejemplo. Reformular con lenguaje propio.
4. **Rotar la formulación**: misma idea, distinta forma.

## Que la tabla entre en la página

Los anchos de columna y el tamaño de letra los pone el Word del servidor (o la plantilla de la facultad, si el tesista la subió a su proyecto). En el texto que se guarda, la tabla va con la sintaxis de tabla APA del Paso 10 del SKILL.md: cada fila en una sola línea, todas con las mismas celdas que la cabecera, y celdas breves, con los indicadores separados por punto y coma. Si hace falta ajustar anchos, el tesista lo hace en Word.

## Cómo la skill presenta la matriz cualitativa construida

La construye y la muestra al tesista en el chat (todavía no se guarda). Pregunta con `ask_user_input_v0` (single_select):

- "Aplicar esta matriz y agregarla al Anexo 2"
- "Modificar algunos indicadores (te indico cuáles)"
- "Cambiar alguna subcategoría"
- "Te ayudo a decidirlo con ejemplos sencillos"

Solo después de validación se agrega al Anexo 2.

## Reglas críticas

- **Las dimensiones son definitivas desde el Cap I**, no se modifican aquí.
- **Las definiciones conceptuales llevan la clave de su fuente**; si no la tienen, se le señala al tesista y la definición va con `[FALTA FUENTE]` hasta que la tenga.
- **Los indicadores deben ser observables o autoreportables** por la población.
- **Cada indicador genera entre 2 y 4 ítems** en la Skill 5; su texto no se redacta aquí.
- **La escala debe ser consistente** entre dimensiones de la misma variable.
- **Una sola fuente de verdad**: si la matriz cambia, cambia en el Anexo 2, no en una copia dentro del Capítulo III.
