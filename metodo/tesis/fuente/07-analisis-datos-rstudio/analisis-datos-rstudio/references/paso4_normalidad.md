# Paso 4 — Prueba de normalidad

## Regla operativa que la skill aplica

| Tamaño muestral | Prueba recomendada |
|----------------|-------------------|
| n < 50 | Shapiro-Wilk |
| n ≥ 50 | Kolmogorov-Smirnov con corrección de Lilliefors |

Algunos autores prefieren Shapiro-Wilk siempre (es más potente). Si el asesor lo exige, aplicar Shapiro-Wilk independiente del n.

## Código R

### Shapiro-Wilk (n < 50)

```r
shapiro.test(datos$V1_total)
shapiro.test(datos$V2_total)
```

### Kolmogorov-Smirnov con Lilliefors (n ≥ 50)

```r
library(nortest)
lillie.test(datos$V1_total)
lillie.test(datos$V2_total)

# Alternativa con la prueba KS clásica (menos recomendada)
ks.test(datos$V1_total, "pnorm",
        mean(datos$V1_total),
        sd(datos$V1_total))
```

### QQ plot (visual)

```r
qqnorm(datos$V1_total, main = "Q-Q plot — V1")
qqline(datos$V1_total, col = "blue", lwd = 2)

qqnorm(datos$V2_total, main = "Q-Q plot — V2")
qqline(datos$V2_total, col = "blue", lwd = 2)
```

### Histograma con curva normal superpuesta

```r
hist(datos$V1_total, prob = TRUE,
     main = "V1 — Distribución",
     xlab = "Puntaje", col = "lightblue")
curve(dnorm(x, mean = mean(datos$V1_total),
            sd = sd(datos$V1_total)),
      add = TRUE, col = "red", lwd = 2)
```

## SPSS

### KS con Lilliefors

```
Analizar > Estadísticos descriptivos > Explorar
   → Variables: V1_total, V2_total
   → Click Gráficos
      → Gráficos de normalidad con pruebas
      → Continuar > Aceptar
```

SPSS reporta automáticamente Kolmogorov-Smirnov con Lilliefors Y Shapiro-Wilk (ambos en la misma tabla).

### Solo KS clásico (sin Lilliefors)

```
Analizar > Pruebas no paramétricas > Cuadros de diálogo antiguos > K-S de 1 muestra
   → Lista de variables: V1_total, V2_total
   → Distribución: Normal
   → Aceptar
```

## Interpretación

```
Hipótesis de la prueba:
   H0: los datos siguen distribución normal
   H1: los datos NO siguen distribución normal
```

- **p > 0.05** → no se rechaza H0 → **datos normales** → pruebas paramétricas
- **p ≤ 0.05** → se rechaza H0 → **datos no normales** → pruebas no paramétricas

## Salida que el tesista pega al chat

### R

```
> lillie.test(datos$V1_total)

   Lilliefors (Kolmogorov-Smirnov) normality test
data:  datos$V1_total
D = 0.087, p-value = 0.058

> lillie.test(datos$V2_total)

D = 0.121, p-value = 0.001
```

### SPSS

```
Pruebas de normalidad
                  Kolmogorov-Smirnov(a)
                  Estadístico  gl    Sig.
V1_total          0,087       100   ,058
V2_total          0,121       100   ,001
```

## Decisión que la skill toma automáticamente

Con los valores anteriores:

- V1_total: p = 0.058 → **datos normales** → en el Paso 5 usar pruebas paramétricas para V1.
- V2_total: p = 0.001 → **datos no normales** → en el Paso 5 usar pruebas no paramétricas para V2.
- Para hipótesis que involucran AMBAS variables (correlación entre V1 y V2), la skill aplica el criterio más restrictivo: **si CUALQUIERA de las dos variables es no normal, usar no paramétrica**.

## Aviso importante

La mayoría de tesis de pregrado peruano con encuestas Likert obtiene datos no normales. La skill lo dice abiertamente al tesista:

> No te alarmes si tu prueba sale con p < 0.05. Es lo más común en pregrado con encuestas Likert. La solución es usar la prueba no paramétrica equivalente, que es igual de defendible. Tu Agente IA conoce las equivalencias.

## Reporte en el capítulo

Texto modelo:

> Para determinar la prueba estadística apropiada, se aplicó la prueba de Kolmogorov-Smirnov con corrección de Lilliefors. La variable V1 obtuvo D = 0.087, p = .058, evidenciando distribución normal. La variable V2 obtuvo D = 0.121, p = .001, indicando ausencia de normalidad. En consecuencia, para los análisis bivariados que involucran V2 se aplicaron pruebas no paramétricas.

Tabla 3 con los resultados.

## QQ plot — interpretación visual

- Si los puntos siguen aproximadamente la línea diagonal → datos normales.
- Si los puntos se desvían sistemáticamente (curva, cola pesada) → datos no normales.

Útil para complementar la prueba formal, especialmente cuando el p está cerca de 0.05.

## Errores comunes

1. Aplicar Shapiro-Wilk con n > 50 (técnicamente válido pero más sensible).
2. No reportar normalidad y aplicar Pearson sin justificación.
3. Confiar solo en el visual (histograma) sin la prueba formal.
4. Cuando una variable es normal y otra no, aplicar Pearson sin criterio: la skill recomienda Spearman por defecto en este caso.
