# De dónde salen las cifras

Ninguna cifra del artículo se calcula "de cabeza" ni se estima. Sale de una de
estas tres vías, y en el texto se declara cuál (software y versión en Métodos).

| Vía | Cuándo | Qué se toma |
|---|---|---|
| **A. Servidor Acosta** (`trabajar_en_r`) | Si la herramienta está conectada. Preferente | La consola de R de esta sesión |
| B. Skill `analisis-datos-rstudio` | Si el investigador ya la usó | **Solo** sus tablas y salidas; su redacción por objetivos es de tesis y no se copia |
| C. Salidas propias | SPSS, SmartPLS, JASP, AMOS, Excel, R | Las tablas tal como vienen |

**Formatear no es recalcular.** Se permite y se declara: redondear a dos
decimales (tres para *p*), quitar el cero inicial donde el estilo lo pida,
escribir *p* < .001. No se permite: recalcular, "corregir" una cifra que no
cuadra o completar una celda vacía. Si algo no cuadra, se pregunta.

## Vía A: el servidor (probado en R 4.6.1, octubre de 2026)

Reglas del servidor que hay que respetar:

- Sin conexión a internet desde R: el corpus o la base **los sube el
  investigador** por el enlace que da la herramienta. El enlace se le entrega
  tal cual, como enlace pulsable.
- No imprimir la base ni filas enteras (datos personales).
- Las cifras que vayan al texto se dejan en una tabla de la sesión y se
  descargan (`escribir_csv(tabla, "resultados.csv")` + opción `descargar`).
  `guardar_analisis` es del flujo de tesis: con claves de artículo el servidor
  la rechaza; no se usa.
- Disponibles: tidyverse, psych, lavaan, semTools, seminr, effectsize,
  bibliometrix, flextable, officer. **No** está `PRISMA2020`.

## Qué análisis según la pregunta (no todo es SEM)

| Pregunta / diseño | Datos | Prueba o modelo | En R (servidor) | Qué se reporta |
|---|---|---|---|---|
| Describir | primarios o secundarios | Frecuencias, M, DE, Mdn | `frecuencias()`, `descriptivos()` | n, %, M (DE) |
| Relación entre dos variables | cuantitativas | Pearson / Spearman | `cor.test()` | r o ρ, IC 95 %, p |
| Asociación entre categorías | cualitativas | χ², exacta de Fisher | `chisq.test()`, `fisher.test()` | χ²(gl), p, V de Cramér |
| Comparar 2 grupos | cuantitativa | t de Student/Welch, U de Mann-Whitney | `t.test()`, `wilcox.test()` | t(gl), p, d de Cohen |
| Comparar 3+ grupos | cuantitativa | ANOVA, Kruskal-Wallis, ANCOVA | `aov()`, `kruskal.test()`, `car::Anova()` | F(gl), p, η²; post hoc `emmeans` |
| Pre-post / medidas repetidas | cuantitativa | t pareada, Wilcoxon, ANOVA mixto | `t.test(paired=TRUE)`, `lme4::lmer()` | t, p, d; efecto de interacción |
| Predecir una variable continua | cualquiera | Regresión lineal múltiple | `lm()`, `car::vif()` | B, β, EE, t, p, R², R² ajustado |
| Predecir sí/no | cualquiera | Regresión logística | `glm(family = binomial)` | OR, IC 95 %, p, pseudo-R² |
| Predecir categorías ordenadas / nominales | cualquiera | Logística ordinal / multinomial | `ordinal::clm()`, `nnet::multinom()` | OR, umbrales |
| Predecir conteos | cualquiera | Poisson, binomial negativa, ceros inflados | `glm(poisson)`, `MASS::glm.nb()`, `pscl::zeroinfl()` | IRR, sobredispersión |
| Datos anidados (alumnos en escuelas) | cualquiera | Multinivel | `lme4::lmer()`, `glmer()` | efectos fijos, ICC |
| Mismos sujetos o países en varios años | secundarios (panel) | Efectos fijos / aleatorios | `plm::plm()`, `fixest::feols()` | coeficientes, Hausman |
| Evolución en el tiempo | secundarios | Series de tiempo | `forecast::auto.arima()`, `tseries` | modelo, AIC, pronóstico |
| Mediación / moderación | cuantitativa | Regresión con interacción, efecto indirecto bootstrap | `lm(y ~ x*m)`; bootstrap manual (ver PLS) | a·b, IC 95 % |
| Modelo con variables latentes | escalas | PLS-SEM, CB-SEM | `seminr`, `lavaan` | ver abajo |
| Validar una escala | escalas | AFE, AFC, fiabilidad, invarianza | `psych::fa()`, `lavaan::cfa()`, `semTools` | cargas, ajuste, ω |

Antes de elegir: nivel de medida de la variable dependiente, normalidad
(`normalidad()`), tamaño de grupos y, en datos secundarios, el diseño muestral.

## Datos secundarios (bases públicas o institucionales)

Encuestas nacionales (ENAHO, ENDES, censos), bases internacionales (Banco
Mundial, PISA, OCDE), registros administrativos o datos abiertos.

- **Métodos debe decir**: fuente y propietario, año o periodo, unidad de
  análisis, cómo se accedió (enlace, fecha de descarga, versión), qué módulos y
  variables se usaron, cómo se construyeron los índices, filtros aplicados y
  tamaño final, tratamiento de perdidos, y si se usaron **factores de expansión**.
- **Encuestas con diseño complejo** (estratos, conglomerados, pesos): los
  porcentajes y modelos se calculan con el diseño, no como muestra simple:

```r
library(survey)
dis <- svydesign(ids = ~conglomerado, strata = ~estrato, weights = ~factor07, data = datos, nest = TRUE)
svymean(~pobreza, dis, na.rm = TRUE); svytable(~sexo + pobreza, dis)
svyglm(pobreza ~ edad + educacion, design = dis, family = quasibinomial())
```

- **Ética**: datos anonimizados y públicos suelen estar exentos de comité; se
  declara igual, con la licencia de uso de la base.
- **Disponibilidad de datos** (Fase 8): se cita la base con su DOI o URL; no se
  sube de nuevo si la licencia no lo permite.
- No instalados en el servidor: `srvyr`, `MatchIt`, `marginaleffects`,
  `mediation`, `modelsummary`. Para emparejamiento o efectos marginales, se usa
  la alternativa disponible o el programa del investigador, y se dice.

### Tabla 1 (sociodemográfica) — Fase 4

```r
frecuencias(datos$sexo)          # función del servidor: n y % sobre válidos
descriptivos(datos[, c("edad")]) # M, DE, mín., máx.
```

Porcentajes sobre casos válidos; los perdidos se declaran en la nota.

### Fiabilidad y validez del instrumento

```r
alfa_de_cronbach(datos[, c("TE1","TE2","TE3","TE4")])   # función del servidor
psych::omega(datos[, items], nfactors = 1, plot = FALSE)$omega.tot
```

### PLS-SEM con seminr

```r
library(seminr)
mm <- constructs(composite("TE", multi_items("TE", 1:4)),
                 composite("BO", multi_items("BO", 1:4)),
                 composite("DD", multi_items("DD", 1:4)))
sm <- relationships(paths(from = "TE", to = c("BO", "DD")),
                    paths(from = "BO", to = "DD"))
pls <- estimate_pls(datos, mm, sm)
s <- summary(pls)
s$loadings; s$reliability          # cargas; alfa, rhoA, rhoC (CR), AVE
s$validity$htmt; s$validity$fl_criteria
s$paths                            # betas y R²
s$vif_items
```

**Bootstrap: `bootstrap_model()` falla en el servidor** ("object 'cl' not
found", también con `cores = 1`). Se usa este remuestreo manual **por tandas**
(medido en octubre de 2026: unos 20 remuestreos por segundo con HTMT; una
llamada aguanta 500 a 1000). Para 5000 remuestreos: 5 a 10 llamadas que
acumulan en `r`. Devuelve los valores **sin redondear**.

```r
boot_tanda <- function(datos, mm, sm, B = 500, semilla = 1, previo = NULL,
                       indirectos = list(), htmt = TRUE) {
  set.seed(semilla)
  coefs <- function(m) { p <- m$path_coef; idx <- which(p != 0, arr.ind = TRUE)
    v <- setNames(p[idx], paste(rownames(p)[idx[,1]], "->", colnames(p)[idx[,2]]))
    for (nm in names(indirectos)) v[nm] <- prod(v[indirectos[[nm]]])   # efecto indirecto a*b
    if (htmt) { ht <- summary(m)$validity$htmt; ix <- which(lower.tri(ht), arr.ind = TRUE)
      v <- c(v, setNames(ht[ix], paste("HTMT", rownames(ht)[ix[,1]], colnames(ht)[ix[,2]]))) }
    v }
  rbind(previo, t(replicate(B, { i <- sample(nrow(datos), replace = TRUE)
    coefs(suppressMessages(estimate_pls(datos[i, ], mm, sm))) })))
}
resumen_boot <- function(datos, mm, sm, res, indirectos = list(), htmt = TRUE) {
  base <- suppressMessages(estimate_pls(datos, mm, sm)); p <- base$path_coef
  idx <- which(p != 0, arr.ind = TRUE)
  orig <- setNames(p[idx], paste(rownames(p)[idx[,1]], "->", colnames(p)[idx[,2]]))
  for (nm in names(indirectos)) orig[nm] <- prod(orig[indirectos[[nm]]])
  if (htmt) { ht <- summary(base)$validity$htmt; ix <- which(lower.tri(ht), arr.ind = TRUE)
    orig <- c(orig, setNames(ht[ix], paste("HTMT", rownames(ht)[ix[,1]], colnames(ht)[ix[,2]]))) }
  res <- res[, names(orig), drop = FALSE]; se <- apply(res, 2, sd, na.rm = TRUE)
  ci <- apply(res, 2, quantile, c(.025, .975), na.rm = TRUE)
  data.frame(efecto = names(orig), estimado = orig, DE = se, t = orig / se,
             p = 2 * pnorm(-abs(orig / se)), IC2.5 = ci[1, ], IC97.5 = ci[2, ],
             B = nrow(res), row.names = NULL)                 # SIN redondear
}
# llamada 1:  r <- boot_tanda(d, mm, sm, B = 500, semilla = 1, indirectos = list("TS->AIT->PR" = c("TS -> AIT", "AIT -> PR")))
# llamada 2…: r <- boot_tanda(d, mm, sm, B = 500, semilla = 2, previo = r, indirectos = ...)
# final:      tb <- resumen_boot(d, mm, sm, r, indirectos = ...); escribir_csv(tb, "estructural.csv")
```

**Redondear una sola vez.** Las tablas de R se guardan con todos los
decimales (`escribir_csv`) y el redondeo lo hace la Fase 5 al escribir, desde
ese valor completo. Nunca se redondea un valor ya redondeado (.0648 → .065 →
.07 es un error; lo correcto es .06). La semilla y el número total de
remuestreos se reportan en Métodos.

Efecto indirecto (mediación): se declara en `indirectos` como el producto de
sus caminos; es significativo si su IC no incluye el 0. El IC del HTMT sale de
la misma tabla (validez discriminante si el límite superior < .85 o .90).

**Comparación entre grupos (MGA) e invarianza (MICOM):** no hay paquete en el
servidor; se programan con remuestreo: estimar el modelo en cada grupo, tomar
la diferencia de cada camino y obtener su distribución permutando la etiqueta
de grupo (1000 permutaciones, por tandas). Para MICOM, paso 2: correlación
entre las puntuaciones de cada constructo calculadas con los pesos de cada
grupo, contra su distribución por permutación. Se declara el procedimiento.
Q² requiere PLSpredict (`predict_pls(pls, technique = predict_DA, noFolds = 10)`);
si no corre, se omite y se dice, no se estima.

### CB-SEM / AFC con lavaan

```r
library(lavaan)
m <- 'TE =~ TE1 + TE2 + TE3 + TE4
      BO =~ BO1 + BO2 + BO3 + BO4
      BO ~ TE'
f <- sem(m, data = datos, estimator = "MLR")
fitMeasures(f, c("chisq.scaled","df","cfi.robust","tli.robust","rmsea.robust","srmr"))
standardizedSolution(f)
```

Para bootstrap en lavaan: `se = "bootstrap", bootstrap = 2000` (sin
`parallel`).

### Regresión, conteo y multinivel (probados)

```r
m  <- lm(DD ~ TE + BO + edad, data = datos); summary(m); car::vif(m)
ml <- glm(aprobado ~ TE + sexo, family = binomial, data = datos); exp(coef(ml))   # OR
mp <- glm(y ~ x, family = poisson, data = datos)
sum(residuals(mp, type = "pearson")^2) / df.residual(mp)   # > 1.5: sobredispersión → binomial negativa
mn <- MASS::glm.nb(y ~ x, data = datos)                     # binomial negativa
mz <- pscl::zeroinfl(y ~ x | x, dist = "negbin", data = datos)  # inflado en ceros
mm <- lme4::lmer(y ~ x + (1 | escuela), data = datos)        # multinivel lineal (lmerTest para p)
mg <- lme4::glmer.nb(y ~ x + (1 | escuela), data = datos)    # multinivel de conteo
performance::icc(mm); performance::r2(mm)
```

Disponibles: MASS, pscl, lme4, lmerTest, nlme, mgcv, emmeans, performance,
car, effectsize, ggeffects, sjPlot, broom.mixed, haven (lee .sav de SPSS).
**No** instalados: glmmTMB, DHARMa, brms. El servidor rechaza código que llame
a un paquete ausente: no se intenta, se usa la alternativa o se avisa.

### Correlacional y comparación

```r
normalidad(datos$puntaje_TE)                               # del servidor
cor.test(datos$TE, datos$DD, method = "spearman")
t.test(DD ~ sexo, data = datos); effectsize::cohens_d(DD ~ sexo, data = datos)
wilcox.test(DD ~ sexo, data = datos)
```

## Matriz de criterios (para reportar en Resultados)

| Índice | Criterio | Fuente del criterio |
|---|---|---|
| Carga externa | ≥ .708 | Hair et al. (2019) |
| Alfa, rhoA, CR | .70 a .95 | Hair et al. (2019) |
| AVE | ≥ .50 | Fornell y Larcker (1981) |
| HTMT | < .85 (< .90 constructos parecidos) | Henseler et al. (2015) |
| VIF | < 3 (ideal), < 5 | Hair et al. (2019) |
| R² | .25 / .50 / .75 débil, moderado, sustancial | Hair et al. (2019) |
| f² | .02 / .15 / .35 | Cohen (1988) |
| CFI, TLI | ≥ .95 (≥ .90 aceptable) | Hu y Bentler (1999) |
| RMSEA, SRMR | ≤ .06 / ≤ .08 | Hu y Bentler (1999) |

Las fuentes de criterio se citan solo si el investigador las tiene o se
verifican en esta sesión; si no, `[POR CONFIRMAR: referencia del criterio]`.

