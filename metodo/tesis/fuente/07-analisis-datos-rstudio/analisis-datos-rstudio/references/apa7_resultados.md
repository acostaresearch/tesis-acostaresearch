# APA 7 — Reglas para el capítulo de Resultados

> **Nota (septiembre de 2026)**: estas reglas APA 7 siguen valiendo como contenido; lo que cambió es cómo se consiguen. Las tablas se escriben en el capítulo con la sintaxis de tabla (un bloque sin líneas en blanco con `**Tabla N**`, `*Título*`, la tabla con `|` y `*Nota.*`) y el Word del servidor les aplica el formato. Las figuras van con su rótulo y la marca `[Insertar aquí la Figura N: archivo.png]`, y el tesista pega la imagen en el Word descargado. Ver la Fase 2 del SKILL.md.

## Estructura general del capítulo

El capítulo se organiza POR OBJETIVOS, no cronológicamente por el orden de los análisis.

```
CAPÍTULO IV — RESULTADOS

Introducción (1 párrafo)

4.1 Datos descriptivos generales
   4.1.1 Caracterización de la muestra
   4.1.2 Confiabilidad del instrumento
   4.1.3 Prueba de normalidad

4.2 Resultados por objetivo específico

   4.2.1 Objetivo específico 1: [texto del objetivo]
      - Tabla con descriptivos pertinentes (si aplica)
      - Resultado de la prueba inferencial
      - Interpretación cualitativa
      - Decisión sobre H1

   4.2.2 Objetivo específico 2: [texto del objetivo]
      - [Misma estructura]

   4.2.N Objetivo específico N

4.3 Resultados del objetivo general
   - Síntesis de hallazgos por dimensión
   - Decisión sobre la hipótesis general
```

## Reglas de formato APA 7 para tablas

### Estructura básica

```
Tabla N                                    ← negrita

Título descriptivo en cursivas             ← cursivas, sin negrita,
                                              sin punto al final
─────────────────────────────────────────  ← línea superior
Encabezados de columna                     ← negrita, centrados
─────────────────────────────────────────  ← línea divisoria
Cuerpo de la tabla, sin líneas entre filas
─────────────────────────────────────────  ← línea inferior

Nota. N = 100. *p < .05. **p < .01.        ← "Nota." en cursivas
```

### Reglas específicas

1. **Numeración consecutiva**: Tabla 1, Tabla 2, ..., Tabla N (en todo el documento, no reiniciar por capítulo).

2. **Número de tabla en negrita** ("Tabla 3"), en línea propia, alineado a la izquierda.

2b. **Título arriba de la tabla, en cursivas y sin negrita**, en la línea siguiente al número, sin punto al final. Si el reglamento de la facultad especifica otra cosa, manda el reglamento; en ausencia de indicación, cursivas.

3. **Bordes**: SIN líneas verticales en ninguna parte. SIN líneas entre las filas del cuerpo. SOLO tres líneas horizontales: encima del encabezado de columnas, debajo del encabezado, y al cierre de la tabla. El Word del servidor aplica estos bordes a toda tabla escrita con la sintaxis de tabla (ver la Fase 2 del SKILL.md).

4. **Cuerpo de la tabla**: interlineado sencillo (1.0), aunque el cuerpo del documento lleve otro. Lo pone el Word del servidor; la tipografía y el tamaño salen de la plantilla de la facultad o del formato por defecto de la plataforma.

4b. **Toda tabla y figura se cita en el texto ANTES de aparecer**: "La Tabla 3 muestra los resultados de la correlación entre...". Una tabla que aparece sin haber sido anunciada es observación segura del asesor.

4c. **Las figuras siguen el mismo esquema**: número en negrita, título en cursivas debajo, la figura, y la nota al pie con "Nota." en cursivas.

5. **Decimales**:
   - Estadísticos descriptivos: 2 decimales (M = 3.45, SD = 0.78)
   - Coeficientes de correlación: 2 decimales, sin cero antes del punto (r = .42)
   - p-values: 3 decimales (p = .001) o "p < .001" si menor
   - Alfa de Cronbach: 2 decimales, sin cero antes del punto (α = .87)

6. **Nota al pie**: solo si necesaria. Inicia con "Nota." en cursiva, seguida del texto en regular.

7. **Asteriscos para significancia**: *p < .05, **p < .01, ***p < .001.

### Ejemplos de tablas correctas

**Tabla 1 — Caracterización de la muestra**

```
Tabla 1
Caracterización de la muestra por grado y sexo

Variable           f      %
Grado
  4° secundaria    48     48.0
  5° secundaria    52     52.0
Sexo
  Femenino         54     54.0
  Masculino        46     46.0
Edad
  13-15 años       62     62.0
  16-18 años       38     38.0
Total              100    100.0

Nota. N = 100.
```

**Tabla 2 — Cronbach por variable**

```
Tabla 2
Confiabilidad del instrumento por variable y dimensión

Variable / Dimensión              Ítems   α     Interpretación
V1. Uso de IA generativa          24      .87   Buena
  D1.1 Conocimiento sobre IA      6       .79   Aceptable
  D1.2 Uso y aplicación           6       .81   Buena
  D1.3 Evaluación crítica         6       .84   Buena
  D1.4 Ética y responsabilidad    6       .78   Aceptable
V2. Disposición al pensamiento    14      .82   Buena
  D2.1 a D2.7 (7 dimensiones)     14      .65-.78
Total escala                      38      .89   Buena

Nota. α = coeficiente alfa de Cronbach. N = 100.
```

**Tabla 3 — Prueba de normalidad**

```
Tabla 3
Prueba de Kolmogorov-Smirnov con corrección de Lilliefors

Variable      D       gl    p
V1_total      .087    100   .058
V2_total      .121    100   .001

Nota. D = estadístico de Kolmogorov-Smirnov. p < .05 indica
ausencia de normalidad.
```

**Tabla 4 — Correlación**

```
Tabla 4
Correlación entre uso de IA generativa y pensamiento crítico

Variable                                  M       SD     1
1. V1. Uso de IA generativa              84.20   12.34  —
2. V2. Disposición al pensamiento crítico 52.10   7.85   .42**

Nota. N = 100. Coeficiente de Spearman.
**p < .01.
```

**Tabla 5 — Comparación de grupos**

```
Tabla 5
Comparación de V1 entre grados de secundaria

Grado          n     M       SD     U         z       p
4° sec.        48    81.50   11.20
5° sec.        52    86.70   12.80  927.00   -2.14   .032

Nota. U = estadístico de Mann-Whitney. Tamaño del efecto
r = .21 (pequeño).
```

**Tabla 6 — Regresión**

```
Tabla 6
Regresión lineal: V1 como predictor de V2

Predictor       B       SE     β     t        p
Constante       28.45   3.78          7.53    < .001
V1_total        0.28    0.05   .48    5.59    < .001

Nota. R² = .234, R² ajustado = .226, F(1, 98) = 31.26,
p < .001.
```

## Reglas de formato APA 7 para figuras

### Estructura básica

```
Figura N
Título descriptivo

[Insertar aquí la Figura N: archivo.png]

Nota. Texto explicativo si necesario.
```

### Reglas

1. **Numeración consecutiva**: Figura 1, Figura 2, ... (separada de la numeración de tablas).
2. **Título arriba de la figura**, en formato similar al de las tablas.
3. **Calidad mínima**: 300 dpi para impresión, 1000+ px de ancho.
4. **Ejes claramente etiquetados** con título y unidades.
5. **Leyenda** si hay varias series.
6. **Fuente original** si la figura es de otro autor (no aplica si la generó el tesista).

## Citación de tablas y figuras en el texto

Cada tabla y figura DEBE citarse en el texto antes de que aparezca. Ejemplos:

> "La Tabla 1 muestra la caracterización de la muestra por grado, sexo y edad."

> "Como se observa en la Figura 2, la distribución de V1 sigue una forma aproximadamente normal."

> "Los resultados de la correlación se presentan en la Tabla 4. Se encontró una asociación positiva significativa entre ambas variables (ρ = .42, p < .01)."

**No insertar tabla o figura sin que el párrafo anterior la mencione.**

## Interpretación cualitativa (sin literatura)

Después de cada tabla con resultado inferencial, redactar 1-2 párrafos que:

1. **Describan el dato** ("La correlación obtenida fue de ρ = .42").
2. **Califiquen la magnitud** ("magnitud moderada según Hernández-Sampieri y Mendoza, 2018").
3. **Declaren la significancia** ("estadísticamente significativa, p < .01").
4. **Decidan sobre la hipótesis** ("permite aceptar la H1").

NO incluir contrastes con literatura del Cap II. Eso es trabajo de la Skill 8 (Resultados y Discusión).

Ejemplo de párrafo correcto:

> Se aplicó el coeficiente de correlación de Spearman dada la ausencia de normalidad de V2. Como se aprecia en la Tabla 4, se obtuvo una correlación positiva, moderada y estadísticamente significativa entre el uso de IA generativa y la disposición al pensamiento crítico (ρ = .42, p < .01). La magnitud del coeficiente se ubica en el rango de correlación moderada según los criterios de Hernández-Sampieri y Mendoza [AR…:n]. Este resultado permite aceptar la hipótesis específica H1.

NO escribir:

> Este resultado coincide con lo reportado por Vereau Amaya et al. [AR…:n], quienes…

Esa frase es discusión académica. Pertenece al Capítulo de Discusión (Skill 8).
