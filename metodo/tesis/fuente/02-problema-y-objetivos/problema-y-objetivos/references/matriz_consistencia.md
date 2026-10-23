# Matriz de consistencia

La matriz de consistencia pone en **una sola tabla integrada** toda la cadena lógica del Capítulo I. Es lo que el asesor revisa primero. La skill la genera siempre como una sola tabla con 6 columnas, sin separar en tablas auxiliares.

## Estructura única: 6 columnas

| Columna | Qué contiene |
|---------|--------------|
| 1. Problema | PG en la fila 1, PE1, PE2, PEn en las siguientes. |
| 2. Objetivo | OG en la fila 1, OE1, OE2, OEn en las siguientes. |
| 3. Hipótesis | HG (H1 + H0 general) en la fila 1, HE1, HE2, HEn en las siguientes. |
| 4. Variables | Una sola celda con `rowSpan` que abarca todas las filas. Solo nombres de variables. |
| 5. Dimensiones | Una sola celda con `rowSpan`. Lista numerada de dimensiones por variable. |
| 6. Metodología | Una sola celda con `rowSpan`. Tipo, nivel, diseño, enfoque, población, muestra referencial, técnica, instrumento referencial, técnicas de análisis. |

Cantidad de filas específicas: igual al número de dimensiones de V1 (Paso 4 de la skill).

## Por qué una sola tabla con rowSpan

Los asesores y jurados de pregrado peruano están acostumbrados a leer la matriz como un todo integrado, no fragmentado. Tres ventajas:

- **Visualmente compacta**: una sola tabla cabe en una página A4 portrait, lo que facilita imprimirla y revisarla.
- **Refleja la lógica**: las columnas Variables, Dimensiones y Metodología describen el estudio completo (no fila por fila), por eso van con rowSpan.
- **Estándar académico**: es la estructura que aparece en la mayoría de reglamentos de tesis de universidades peruanas.

## Ejemplo completo aplicado (correlacional)

Caso: tesista de Lengua y Literatura sobre uso de IA generativa y disposición al pensamiento crítico en estudiantes de 4° y 5° de secundaria de una I.E. pública de Trujillo, 2026. V1 tiene 4 dimensiones (AI Literacy), V2 tiene 7 dimensiones (Facione).

```
| Problema | Objetivo | Hipótesis | Variables       | Dimensiones        | Metodología   |
|----------|----------|-----------|-----------------|--------------------|---------------|
| PG: ¿... | OG: Det. | HG: H1+H0 | V1: Uso de IA   | V1 (AI Literacy):  | Tipo:Aplicada |
|          |          |           | generativa.     |   1. Conoc. IA     | Nivel:Correl. |
|          |          |           | V2: Disposic.   |   2. Uso y aplic.  | Diseño:No exp |
| PE1: ¿C. | OE1: Est.| HE1: rel  | al pensam.      |   3. Eval. crítica | Enfoque:Cuant |
|          |          |           | crítico.        |   4. Ética         | Pobl: 4°-5°   |
|          |  ROWSPAN ABARCA   |  ROWSPAN ABARCA |  ROWSPAN ABARCA    | sec. I.E.     |
| PE2:...  | OE2:...  | HE2:...   |  5 FILAS        | V2 (Facione, CCTDI)| Muestra:Cap IV|
|          |          |           |                 |   1. Búsq. verdad  | Técnica:Encue |
|          |          |           |                 |   2. Mente abierta | Instr:cuest.  |
| PE3:...  | OE3:...  | HE3:...   |                 |   3. Análisis      | adaptado      |
|          |          |           |                 |   4. Sistemat.     | Análisis:Pear |
|          |          |           |                 |   5. Autoconfian.  | son/Spearman  |
| PE4:...  | OE4:...  | HE4:...   |                 |   6. Curiosidad    | Detalle:Cap IV|
|          |          |           |                 |   7. Madurez       |               |
```

## Reglas de llenado

### Cantidad de filas específicas

- Igual al número de dimensiones de V1.
- Si V1 tiene 3 dimensiones, hay 3 PE / 3 OE / 3 HE.
- Si V1 tiene 4 dimensiones, hay 4 PE / 4 OE / 4 HE.
- **NO** se incluye OE descriptivo del tipo "identificar el nivel de V1" o "identificar el nivel de V2". El nivel se reporta en resultados, no se plantea como objetivo.

### Coherencia 1 a 1 obligatoria

- PE1 ↔ OE1 ↔ HE1: las tres tratan de la misma dimensión.
- Redacción paralela: si PE1 dice "¿cómo se relaciona X con Y?", OE1 dice "establecer la relación entre X y Y", HE1 dice "H1: existe relación entre X y Y. H0: no existe relación".

### Las columnas 4, 5 y 6 en Markdown

- En Markdown no hay celdas combinadas: la fila 1 lleva las 6 celdas, con Variables, Dimensiones y Metodología completas.
- Las filas 2 a N llevan contenido solo en las 3 primeras celdas (Problema, Objetivo, Hipótesis); las otras tres quedan vacías.

### Si la tabla no entra legible

Los anchos y la tipografía los pone el servidor. Si V2 tiene muchas dimensiones (por ejemplo, Facione con 7) y la celda de Dimensiones se satura, se acortan los nombres (abreviaturas explicadas en la nota) en vez de tocar el formato.

## Casos especiales

### Estudio descriptivo puro

- Columna Hipótesis: "No aplica al diseño descriptivo" en todas las filas.
- PE y OE pueden ser sobre caracterización de cada dimensión.

### Estudio cualitativo

- Columna Hipótesis → "Supuestos".
- Columna Variables → "Categorías de análisis".
- Columna Dimensiones → "Sub-categorías".

### Estudio explicativo / causal

- HE afirman influencia o efecto, no solo relación.
- Estructura: H1.1: La dimensión X de V1 influye significativamente en V2. H0.1: La dimensión X no influye.

### Estudio comparativo

- HE en formato de diferencias entre grupos.

## Formato APA 7 obligatorio para la matriz

La matriz sale en el Word con **formato APA 7 de tabla**: número en negrita, título en cursivas, tres líneas horizontales sin bordes verticales y nota al pie. La skill escribe el contenido; el servidor pone las líneas, la tipografía y el interlineado.

### Lo que escribe la skill (un solo bloque, sin líneas en blanco)

```
**Tabla 1**
*Matriz de consistencia*
| Problema | Objetivo | Hipótesis | Variables | Dimensiones | Metodología |
|---|---|---|---|---|---|
| PG: … | OG: … | HG: … | V1: … V2: … | V1 (teoría [AR…]): … | Tipo: … |
| PE1: … | OE1: … | HE1: … | | | |
*Nota.* Elaboración propia. PG: Problema General; PE: Problema Específico; OG: Objetivo General; OE: Objetivo Específico; HG: Hipótesis General; HE: Hipótesis Específica.
```

Una línea en blanco dentro del bloque lo parte y el Word deja de reconocer la tabla.

### Numeración de la tabla

Si el Capítulo I solo tiene esta tabla, es "Tabla 1". Si el reglamento de la universidad exige numeración por capítulo, entonces "Tabla 1.1". La skill pregunta al tesista antes de guardar el capítulo cuál sistema usa su reglamento.

## Verificación final de la matriz

Antes de guardar el capítulo, marcar checklist:

```
- [ ] Una sola tabla integrada de 6 columnas (no dos tablas
       separadas).
- [ ] Variables, Dimensiones y Metodología con rowSpan que
       abarca todas las filas.
- [ ] Cantidad de filas específicas = cantidad de dimensiones de V1.
- [ ] Ningún OE es "identificar el nivel de V1 o V2".
- [ ] Coherencia 1 a 1: PE1-OE1-HE1, PE2-OE2-HE2, etc.
- [ ] Variables y población idénticas a las del título.
- [ ] Dimensiones definitivas (no tentativas).
- [ ] Sin ítems del instrumento (eso es Cap 5).
- [ ] Sin operacionalización profunda (eso es Cap 4).
- [ ] Bloque de tabla sin líneas en blanco: **Tabla N**,
       *título*, cabecera, |---|, filas y *Nota.*
```

Si una fila no encaja, no la metas con calzador. Mejor una matriz con menos filas pero coherente que una con muchas filas inconsistentes.
