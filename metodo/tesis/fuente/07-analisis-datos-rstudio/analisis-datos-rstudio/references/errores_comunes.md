# Errores comunes en el análisis de datos

Esta referencia documenta los errores frecuentes que la skill debe prevenir activamente. Está basada en el Capítulo 7.17 del ebook del método.

## Error 1: Empezar inferencial sin verificar normalidad

### Síntoma

El tesista pega directamente código de Pearson, t-Student o ANOVA sin haber hecho la prueba de normalidad del Paso 4.

### Por qué es grave

Las pruebas paramétricas (Pearson, t-Student, ANOVA, regresión) asumen distribución normal. Si los datos no son normales, los p-values son sospechosos y la decisión sobre la hipótesis puede ser incorrecta.

### Cómo lo previene la skill

La skill no avanza al Paso 5 (inferencial) sin haber recibido los outputs del Paso 4 (normalidad). Si el tesista intenta saltar, la skill se niega y explica el riesgo.

## Error 2: Reportar p sin reportar tamaño del efecto

### Síntoma

El tesista escribe "se encontró diferencia significativa (p = .03)" y se detiene ahí.

### Por qué es grave

Significancia (p) no es lo mismo que magnitud. Con muestras grandes (n > 500), incluso diferencias triviales son estadísticamente significativas. El tamaño del efecto dice si la diferencia importa en la práctica.

### Cómo lo previene la skill

En el Paso 5, la skill SIEMPRE incluye el tamaño del efecto pertinente:
- Pearson/Spearman: el coeficiente mismo es magnitud.
- t-Student: d de Cohen.
- ANOVA: eta cuadrado o omega cuadrado.
- Chi²: V de Cramer.
- Regresión: R², R² ajustado, β estandarizados.

Si el tesista omite reportar tamaño del efecto, la skill lo recuerda.

## Error 3: Confundir correlación con causalidad

### Síntoma

El tesista escribe "el uso de IA causa mayor pensamiento crítico" cuando solo aplicó una correlación.

### Por qué es grave

Una correlación no implica causalidad. Para hablar de causa, se necesita un diseño experimental con grupo control, asignación aleatoria y manipulación de la variable independiente. Un diseño correlacional describe asociación, no causalidad.

### Cómo lo previene la skill

En el reporte cualitativo del Paso 5, la skill redacta:
- "Se encontró asociación significativa" ✓
- "Se relacionan significativamente" ✓
- "Existe correlación positiva moderada" ✓
- "El uso de IA causa mayor pensamiento crítico" ✗
- "El uso de IA produce mayor pensamiento crítico" ✗

Si el tesista usa lenguaje causal en diseño correlacional, la skill propone reformular.

## Error 4: Eliminar outliers sin justificar

### Síntoma

El tesista detecta valores atípicos (outliers) y los elimina sin más, "para limpiar los datos".

### Por qué es grave

Los outliers pueden ser:
- Errores de digitación → eliminar es correcto.
- Respuestas reales pero extremas → eliminarlas sesga el análisis.
- Casos que aportan información (por ejemplo, en un estudio sobre uso de IA, un estudiante con uso muy bajo o muy alto puede ser interesante).

Eliminar sin distinguir empobrece el análisis y se considera mala práctica.

### Cómo lo previene la skill

Cuando el tesista detecta outliers, la skill propone:
1. Verificar si el valor está dentro del rango posible de la escala (1-5 para Likert 1-5). Si no, es error de digitación, corregir o eliminar.
2. Si está dentro del rango, mantener pero reportar. Considerar pruebas robustas a outliers.
3. Si se decide eliminar, documentar criterio explícito en la metodología.

## Error 5: Aceptar/rechazar hipótesis sin contrastar con marco teórico

### Síntoma

El tesista decide la hipótesis solo con base en el p-value, sin discutir si el hallazgo es coherente con los antecedentes del Cap II.

### Por qué es grave

La estadística inferencial es UNA herramienta para decidir. Pero el sentido del hallazgo se construye en diálogo con la literatura. Sin esa discusión, la tesis pierde su valor académico.

### Cómo lo previene la skill

Aquí hay una frontera clave: **la Skill 7 NO hace la discusión académica con literatura**. Eso es trabajo de la Skill 8. La Skill 7 solo declara la decisión estadística ("se acepta H1 dado que p < .05").

La skill 7 entrega los números y la decisión. La skill 8 contrasta con la literatura. Esta división es deliberada.

## Error 6: Pegar código sin entenderlo

### Síntoma

El tesista copia el código R que la skill generó sin saber qué hace cada línea. En sustentación, el jurado pregunta "¿qué hace `aov()`?" y el tesista no sabe responder.

### Por qué es grave

El jurado puede invalidar resultados si percibe que el tesista no comprende lo que ejecutó. Es además una cuestión ética: una tesis es del autor, no del Agente IA.

### Cómo lo previene la skill

En cada Paso, la skill incluye junto al código:

```
Explicación línea por línea:
- library(psych): carga el paquete psych que tiene la función alpha
- alpha(...): calcula el coeficiente alfa de Cronbach
- datos[, paste0("ITEM_", sprintf("%02d", 1:24))]: selecciona los
   24 ítems de V1
```

Y al cerrar cada paso, la skill pregunta al tesista si comprende lo que ejecutó. Si responde "no sé", la skill explica con más detalle.

## Otros errores específicos del análisis

### 7. Omitir prueba post-hoc tras ANOVA significativa

Si ANOVA da p < .05, hay diferencia entre AL MENOS dos grupos, pero no se sabe cuáles. La prueba de Tukey (paramétrica) o Dunn (no paramétrica) identifica los pares específicos.

La skill SIEMPRE incluye post-hoc cuando ANOVA o Kruskal-Wallis son significativos.

### 8. Reportar correlaciones simultáneas sin corrección

Cuando se hacen muchas correlaciones (por ejemplo, 15 dimensiones × 15 dimensiones), la probabilidad de falsos positivos aumenta. Se recomienda corrección de Bonferroni o Holm.

La skill lo menciona si el tesista hace más de 5 correlaciones bivariadas en el mismo análisis.

### 9. Olvidar verificar supuestos de regresión

Una regresión lineal asume:
- Normalidad de residuos.
- Homocedasticidad.
- Independencia.
- Linealidad.

Si los supuestos se incumplen, los coeficientes pueden ser sesgados. La skill ofrece `plot(modelo)` para verificación visual y pruebas formales.

### 10. Confundir dimensión con variable

Si V1 tiene 4 dimensiones y se reporta "Cronbach de V1.D1 = .79" pero se interpreta como "Cronbach de V1", el lector se confunde. La skill mantiene clara la distinción en cada reporte.
