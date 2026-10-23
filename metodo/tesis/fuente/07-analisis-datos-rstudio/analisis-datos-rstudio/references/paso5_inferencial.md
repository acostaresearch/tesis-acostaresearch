# Paso 5 — Análisis inferencial

## Árbol de decisión completo

```
Tipo de hipótesis    Datos normales      Datos NO normales
─────────────────────────────────────────────────────────────
Relación 2 cuanti    Pearson (r)         Spearman (ρ)
Diferencia 2 grupos  t-Student           U de Mann-Whitney
Diferencia 3+ grupos ANOVA + Tukey       Kruskal-Wallis + Dunn
Asociación 2 categ.  Chi² (χ²)           Chi² (igual)
Predicción 1 var.    Regresión simple    Regresión robusta o
                                          transformar datos
Predicción varias    Regresión múltiple  Regresión robusta
```

## 1. Correlación de Pearson (datos normales)

### Código R

```r
# Correlación
cor.test(datos$V1_total, datos$V2_total, method = "pearson")

# Matriz de correlaciones (para varias variables)
library(Hmisc)
rcorr(as.matrix(datos[, c("V1_total", "V2_total")]), type = "pearson")

# Gráfico de dispersión
plot(datos$V1_total, datos$V2_total,
     main = "Relación V1 - V2",
     xlab = "V1: Uso de IA", ylab = "V2: Pensamiento crítico",
     pch = 16, col = "steelblue")
abline(lm(V2_total ~ V1_total, data = datos), col = "red", lwd = 2)
```

### SPSS

```
Analizar > Correlaciones > Bivariadas
   → Variables: V1_total, V2_total
   → Coeficientes de correlación: Pearson
   → Prueba de significación: Bilateral
   → Marcar las correlaciones significativas
   → Aceptar
```

### Interpretación de r

| Valor de r | Magnitud |
|------------|----------|
| 0.00 – 0.10 | Nula o muy débil |
| 0.11 – 0.30 | Débil |
| 0.31 – 0.50 | Moderada |
| 0.51 – 0.70 | Considerable |
| 0.71 – 0.90 | Muy fuerte |
| 0.91 – 1.00 | Casi perfecta |

Fuente de estos rangos: Hernández-Sampieri y Mendoza, 2018 (en el capítulo, con su clave `[AR…]`).

### Reporte tipo

> Se encontró una correlación positiva, moderada y estadísticamente significativa entre el uso de IA generativa y la disposición al pensamiento crítico (r = .42, p < .001, IC 95% [.25, .57]). Este resultado permite aceptar la hipótesis H1, que postulaba que ambas variables se relacionan significativamente.

## 2. Correlación de Spearman (datos no normales)

### Código R

```r
cor.test(datos$V1_total, datos$V2_total, method = "spearman")
```

### SPSS

```
Analizar > Correlaciones > Bivariadas
   → Coeficientes: Spearman
   → Aceptar
```

### Interpretación

Igual que Pearson: ρ (rho) se interpreta con los mismos rangos.

## 3. t de Student (2 grupos, datos normales)

### Código R

```r
library(car)

# Prueba de Levene para igualdad de varianzas
leveneTest(V1_total ~ as.factor(GRADO), data = datos)

# t de Student
t.test(V1_total ~ GRADO, data = datos, var.equal = TRUE)
# Si Levene es significativo (p < 0.05), cambiar a var.equal = FALSE

# Tamaño del efecto: d de Cohen
library(effsize)
cohen.d(V1_total ~ as.factor(GRADO), data = datos)

# Boxplot
boxplot(V1_total ~ GRADO, data = datos,
        names = c("4° secundaria", "5° secundaria"),
        col = c("lightblue", "lightcoral"))
```

### SPSS

```
Levene (incluida automáticamente):
Analizar > Comparar medias > Prueba T para muestras independientes
   → Variables de prueba: V1_total
   → Variable de agrupación: GRADO (definir grupos 4 y 5)
   → Aceptar
```

### Interpretación de d de Cohen

| d | Magnitud |
|---|----------|
| 0.0 – 0.2 | Trivial |
| 0.2 – 0.5 | Pequeña |
| 0.5 – 0.8 | Mediana |
| > 0.8 | Grande |

## 4. U de Mann-Whitney (2 grupos, datos no normales)

### Código R

```r
wilcox.test(V1_total ~ GRADO, data = datos)

# Tamaño del efecto: r de Mann-Whitney
library(rstatix)
wilcox_effsize(datos, V1_total ~ GRADO)
```

### SPSS

```
Analizar > Pruebas no paramétricas > Cuadros de diálogo antiguos > 2 muestras independientes
   → Lista de variables: V1_total
   → Variable de agrupación: GRADO
   → Tipo: U de Mann-Whitney
```

## 5. ANOVA (3+ grupos, datos normales)

### Código R

```r
# ANOVA de un factor
modelo_anova <- aov(V1_total ~ as.factor(SECCION), data = datos)
summary(modelo_anova)

# Post-hoc Tukey (solo si ANOVA es significativa)
TukeyHSD(modelo_anova)

# Tamaño del efecto: eta cuadrado
library(effectsize)
eta_squared(modelo_anova)
```

### SPSS

```
Analizar > Comparar medias > ANOVA de un factor
   → Dependiente: V1_total
   → Factor: SECCION
   → Click Post Hoc > Tukey
   → Click Opciones > Descriptivos, Homogeneidad de varianzas
   → Aceptar
```

## 6. Kruskal-Wallis (3+ grupos, datos no normales)

### Código R

```r
kruskal.test(V1_total ~ as.factor(SECCION), data = datos)

# Post-hoc Dunn
library(dunn.test)
dunn.test(datos$V1_total, datos$SECCION, method = "bonferroni")
```

### SPSS

```
Analizar > Pruebas no paramétricas > Cuadros de diálogo antiguos > K muestras independientes
   → Tipo: H de Kruskal-Wallis
```

## 7. Chi cuadrado (variables categóricas)

### Código R

```r
# Tabla de contingencia
tabla <- table(datos$GRADO, datos$SECCION)
tabla

# Chi cuadrado
chisq.test(tabla)

# Tamaño del efecto: V de Cramer
library(rcompanion)
cramerV(tabla)
```

### SPSS

```
Analizar > Estadísticos descriptivos > Tablas cruzadas
   → Filas: GRADO
   → Columnas: SECCION
   → Click Estadísticos > Chi-cuadrado, V de Cramer
   → Aceptar
```

## 8. Regresión lineal simple

### Código R

```r
modelo <- lm(V2_total ~ V1_total, data = datos)
summary(modelo)

# Supuestos del modelo
par(mfrow = c(2, 2))
plot(modelo)
par(mfrow = c(1, 1))

# Predicción
predict(modelo, newdata = data.frame(V1_total = c(60, 80, 100)),
        interval = "confidence")
```

### SPSS

```
Analizar > Regresión > Lineales
   → Dependiente: V2_total
   → Independiente: V1_total
   → Click Estadísticos > Estimaciones, Ajuste del modelo, Durbin-Watson
   → Click Gráficos > ZPRED en X, ZRESID en Y
   → Aceptar
```

### Qué reportar

- R² (porcentaje de varianza explicada)
- Coeficiente β (no estandarizado)
- β estandarizado (comparable entre variables)
- p-value del coeficiente
- Supuestos verificados (normalidad de residuos, homocedasticidad)

## 9. Regresión múltiple

### Código R

```r
modelo_mult <- lm(V2_total ~ V1_total + EDAD + as.factor(GRADO), data = datos)
summary(modelo_mult)

# Coeficientes estandarizados
library(lm.beta)
lm.beta(modelo_mult)

# Multicolinealidad (VIF)
library(car)
vif(modelo_mult)
```

VIF > 10 indica multicolinealidad problemática.

### SPSS

```
Analizar > Regresión > Lineales
   → Dependiente: V2_total
   → Independientes: V1_total, EDAD, GRADO
   → Método: Introducir (o Por pasos si quieres modelo final óptimo)
   → Click Estadísticos > Cambio en R², Diagnósticos de colinealidad
   → Aceptar
```

## Tamaño del efecto — siempre reportarlo

Significancia (p) NO es magnitud. Un p < 0.05 con n = 1000 puede tener tamaño del efecto trivial. Siempre reportar:

- Pearson/Spearman: el coeficiente mismo (r o ρ)
- t-Student: d de Cohen
- ANOVA: eta cuadrado (η²) o omega cuadrado (ω²)
- Chi²: V de Cramer
- Regresión: R², R² ajustado, β estandarizados
