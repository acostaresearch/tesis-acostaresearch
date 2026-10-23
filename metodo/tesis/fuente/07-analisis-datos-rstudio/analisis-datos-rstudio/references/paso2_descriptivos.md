# Paso 2 — Estadísticos descriptivos

## Qué reportar

### Para variables categóricas (demográficas)

- Frecuencias absolutas (n) y relativas (%)
- Tabla en formato APA 7

Ejemplo de tabla esperada:

```
Tabla 1
Caracterización de la muestra por grado

Grado          n     %
4° secundaria  48    48.0
5° secundaria  52    52.0
Total          100   100.0
```

### Para variables cuantitativas (puntajes totales o ítems)

- Media (M)
- Desviación estándar (SD)
- Mínimo (Mín)
- Máximo (Máx)
- Asimetría (Skew) y curtosis (Kurt) si se requiere para normalidad

## Código R

```r
library(psych)

# Frecuencias demográficas
table(datos$GRADO)
prop.table(table(datos$GRADO)) * 100

# Cruce GRADO × SECCION
table(datos$GRADO, datos$SECCION)

# Descriptivos de ítems individuales
describe(datos[, paste0("ITEM_", sprintf("%02d", 1:38))])

# Crear puntajes totales por variable
datos$V1_total <- rowSums(datos[, paste0("ITEM_", sprintf("%02d", 1:24))])
datos$V2_total <- rowSums(datos[, paste0("ITEM_", sprintf("%02d", 25:38))])

# Descriptivos de los totales
describe(datos[, c("V1_total", "V2_total")])

# Por dimensión (ejemplo con V1.D1, 6 ítems)
datos$V1_D1 <- rowMeans(datos[, paste0("ITEM_", sprintf("%02d", 1:6))])

# Histograma
hist(datos$V1_total,
     main = "Distribución de V1: Uso de IA generativa",
     xlab = "Puntaje total",
     col = "lightblue",
     border = "black")

# Boxplot por grupo
boxplot(V1_total ~ GRADO, data = datos,
        main = "V1 por grado",
        xlab = "Grado", ylab = "Puntaje V1")
```

## SPSS — menús

### Frecuencias demográficas

```
Analizar > Estadísticos descriptivos > Frecuencias
   → Variables: GRADO, SECCION, EDAD
   → Click Estadísticos > Media, Mediana, Desv. típica, Mín, Máx
   → Click Gráficos > Gráfico de barras
   → Aceptar
```

### Descriptivos de variables cuantitativas

```
Analizar > Estadísticos descriptivos > Descriptivos
   → Variables: V1_total, V2_total (después de crearlas con
      Transformar > Calcular variable)
   → Click Opciones > Media, Desv. típica, Mín, Máx,
      Asimetría, Curtosis
   → Aceptar
```

### Crear puntajes totales en SPSS

```
Transformar > Calcular variable
   → Variable de destino: V1_total
   → Expresión numérica: SUM(ITEM_01 TO ITEM_24)
   → Aceptar
```

## Decisión: usar puntaje total o promedio

- **Puntaje total**: suma de todos los ítems. Rango más amplio (ej. 24-120 para V1 de 24 ítems Likert 1-5).
- **Puntaje promedio**: media de los ítems. Rango siempre 1-5 (más interpretable directamente en términos de la escala).

Recomendación pregrado peruano: reportar promedio para que el lector entienda directamente "los estudiantes promedio respondieron en 3.4, ligeramente por encima del punto medio".

## Salida que el tesista pega al chat

```
La skill espera:
- Tabla de frecuencias de cada variable categórica (cuántos
   estudiantes en cada categoría con porcentaje)
- Para cada variable cuantitativa: M, SD, Mín, Máx
- Si aplica, asimetría y curtosis
```

## Lo que la skill hace con esos datos

1. Guarda las cifras de los descriptivos que irán al texto con `guardar_analisis` (campo `resultados`; si el tesista pegó la salida de su programa, también `salida`) para la Fase 2 (redacción del capítulo).
2. Verifica que las medias estén dentro del rango esperado (Likert 1-5: la media debe estar entre 1 y 5).
3. Si detecta medias atípicas (todas en 5.0 o todas en 1.0), pregunta al tesista si revisó la matriz.
