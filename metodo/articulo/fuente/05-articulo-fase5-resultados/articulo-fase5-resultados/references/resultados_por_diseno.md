# Orden de presentación y cifras según el tipo de análisis

Estudios empíricos con datos primarios o secundarios. Las revisiones tienen su
propia ruta. El tipo de análisis es el que declaró Métodos (índice de
`analisis.md`); **no se asume SEM**.

El orden no es una preferencia de estilo: el revisor lee esperando esa secuencia
y busca cada índice en su lugar. Alterarlo se lee como desconocimiento.

Todas las cifras, en formato APA 7 (estadístico en cursiva, gl entre
paréntesis, *p* exacta con tres decimales o *p* < .001, IC 95 % entre
corchetes) y **redondeadas una sola vez** desde el valor completo.

## Resumen: qué cifras lleva cada análisis

| Análisis | Cifras que se reportan |
|---|---|
| Descriptivo | n, %, *M* (*DE*) o *Mdn* (RIC); con factor de expansión: n sin ponderar y % ponderado |
| Correlación | *r* o ρ, IC 95 %, *p*, n |
| Asociación (χ², Fisher) | χ²(gl, *N*), *p*, *V* de Cramér |
| Comparación de 2 grupos | *M* (*DE*) por grupo, *t*(gl) o *U*, *p*, *d* de Cohen (o *r*) con IC |
| Comparación de 3+ grupos | *F*(gl1, gl2) o *H*, *p*, η² (o ε²), post hoc con corrección |
| Regresión lineal | *B*, *EE*, β, *t*, *p*, IC 95 %; *R²*, *R²* ajustado, *F*(gl); VIF máximo |
| Logística (binaria, ordinal, multinomial) | OR con IC 95 %, *p*; categoría de referencia; pseudo-*R²* (Nagelkerke o McFadden); umbrales en ordinal |
| Conteo | IRR con IC 95 %, *p*; prueba de sobredispersión y modelo elegido; parte de ceros si es inflado |
| Multinivel | Modelo nulo con ICC; efectos fijos (*B*, *EE*, IC, *p*); varianzas aleatorias; *R²* marginal y condicional; AIC/BIC o razón de verosimilitud |
| Panel | Coeficientes con *EE* agrupados; prueba de Hausman; *R²* intra; n de unidades y periodos |
| Series de tiempo | Prueba de estacionariedad, modelo (p, d, q), AIC, diagnóstico de residuos (Ljung-Box), pronóstico con intervalo |
| Mediación / moderación | Caminos *a*, *b*, *c'*; efecto indirecto con IC bootstrap (B); interacción con *B*, *p* y efectos condicionales |
| SEM | Ver abajo |
| Validación de escala | Ver «Instrumental» abajo |

---

## Descriptivo, correlación y comparación de grupos

```
1 · Descriptivos de las variables (ponderados si hay diseño complejo)
2 · Supuestos (normalidad, homogeneidad) que justifican la prueba
3 · Prueba o correlaciones
4 · Tamaño del efecto y decisión de las hipótesis
```

La prueba de supuestos **justifica** el estadístico usado, así que va antes.
Si se usó Spearman o una no paramétrica, aquí tiene que verse por qué. Las
correlaciones van en matriz, con la significancia marcada según la convención
de la revista; el texto destaca las que responden a las hipótesis.

## Regresión (lineal, logística, ordinal, de conteo)

```
1 · Descriptivos y correlaciones de las variables del modelo
2 · Diagnóstico (VIF, residuos; sobredispersión en conteo; líneas paralelas en ordinal)
3 · Modelo o modelos (por bloques si se ingresaron así)
4 · Ajuste y decisión de las hipótesis
```

Una tabla por modelo, con todos los predictores (también los no
significativos). En logística y conteo se reportan OR o IRR, no los
coeficientes en escala logarítmica, salvo que la revista los pida.

## Multinivel, panel y series de tiempo

```
Multinivel: modelo nulo e ICC → predictores de nivel 1 → de nivel 2 → comparación de modelos
Panel:      descriptivos por periodo → Hausman → modelo elegido → diagnóstico
Series:     gráfico de la serie → estacionariedad → modelo → residuos → pronóstico
```

El ICC del modelo nulo justifica el multinivel: va primero.

## Mediación y moderación (sin SEM)

Efecto total, directo e indirecto con su IC bootstrap; en moderación, el
término de interacción y los efectos condicionales (o la región de
Johnson-Neyman si se calculó). El tipo de mediación se nombra, no se interpreta.

---

## SEM (PLS-SEM o CB-SEM)

```
1 · Modelo de medida
2 · Modelo estructural
3 · Mediación, moderación o comparación de grupos (MICOM + MGA), si aplica
```

**1. Modelo de medida.** Cargas factoriales de cada ítem, fiabilidad (alfa y
compuesta), varianza extraída media, y validez discriminante por HTMT o
Fornell-Larcker. Se reportan **todos** los constructos, no solo los que
cumplieron. Si algún ítem se eliminó, ya se declaró en Métodos; aquí se muestran
las cargas finales.

**2. Modelo estructural.** Primero el diagnóstico de colinealidad (VIF), después
los coeficientes de trayectoria (β, *t*, *p*, IC bootstrap con B), y los índices
de poder explicativo y predictivo (R², Q² o PLSpredict, f²). La figura del
modelo con los coeficientes va aquí. El HTMT, con su IC bootstrap, en el modelo
de medida. **Todas las tablas salen del modelo final** (tras eliminar ítems).

**3. Mediación, moderación o grupos.** Efecto directo, indirecto y total, con
su intervalo de confianza. En comparación de grupos: primero la invarianza
(MICOM: pasos 2 y 3 con su *p* de permutación) y después las diferencias de
caminos (MGA) con su *p* de permutación; si no hay invarianza composicional, se
reporta y la comparación de ese constructo no se hace. **El tipo de mediación se nombra, no se interpreta**: se dice si es
total o parcial según el criterio, sin explicar todavía qué significa para la
teoría.

En CB-SEM, además, los índices de ajuste global que la revista pida. Reportar
los que se declararon en Métodos, no una lista distinta.

---

## Experimental, cuasi o preexperimental

```
1 · Equivalencia inicial de los grupos
2 · Comparación entre grupos o entre momentos
3 · Tamaño del efecto
```

**La equivalencia inicial no es opcional en un cuasiexperimental**: sin
aleatorización, es lo primero que el revisor busca para saber si la diferencia
final se puede atribuir a la intervención.

**El tamaño del efecto se reporta siempre**, junto a la significancia. Un
resultado significativo con tamaño de efecto trivial dice algo distinto, y
omitirlo es de las observaciones más frecuentes.

En preexperimental, decir explícitamente que no hubo grupo de comparación. La
limitación se desarrolla en la Fase 6, pero el dato va aquí.

---

## Descriptivo (un bloque por objetivo)

```
Un bloque por objetivo específico, en el orden de la Matriz
```

Cada bloque: la tabla con frecuencias o medidas de tendencia central, y un
párrafo que destaca lo que importa. Nada más.

El riesgo aquí es el relleno: cinco tablas y cinco párrafos que las leen en voz
alta. Si un bloque no aporta a un objetivo, la tabla va a material
suplementario o se quita.

---

## Cualitativo

```
Un bloque por categoría
```

Cada bloque: la categoría, sus subcategorías, y **citas textuales de los
participantes** que la ilustran, identificadas con seudónimo o código (E1, E2) y
nunca con nombres.

Reglas propias:

- **Las citas son textuales.** No se corrigen, no se pulen, no se combinan
  fragmentos de dos participantes. Si se omite algo dentro de una cita, se marca.
- **Si se codificó en el servidor (`analisis-cualitativo`) o en Atlas.ti**, las
  citas y las frecuencias de códigos (número de citas por código,
  enraizamiento) se copian de esas salidas tal cual, con el código del
  participante. No se reescriben ni se recuentan a mano.
- **No se convierte lo cualitativo en porcentajes de participantes** ("el 60%
  de los entrevistados"). Fuera de las frecuencias que dio el software, se usa
  lenguaje de frecuencia relativa: la mayoría, algunos, uno de los
  participantes.
- **El análisis va aquí, la interpretación en la Fase 6.** La diferencia:
  describir qué dijeron es resultado; explicar por qué lo dicen y contrastarlo
  con la literatura es discusión.
- Si hubo matriz de categorías o red semántica, va como figura.

---

## Instrumental o de validación de escala

```
1 · Análisis factorial exploratorio, si se hizo
2 · Análisis factorial confirmatorio e índices de ajuste
3 · Fiabilidad
4 · Validez convergente y discriminante
5 · Invarianza, si aplica
```

Se reportan **los índices de ajuste que se declararon en Métodos**, con sus
valores y el criterio de referencia con su fuente. Si alguno no alcanzó el
criterio, se reporta igual y se discute en la Fase 6; omitirlo es de las cosas
que un revisor detecta comparando índices.

Las cargas factoriales van completas, por ítem. Es lo que permite que otro
investigador use la escala.

---

## Mixto

Los resultados de cada rama en su propio bloque, **y un tercer bloque de
integración**: dónde convergen, dónde divergen y qué explica la parte
cualitativa de lo que mostró la cuantitativa.

Sin ese tercer bloque el artículo son dos estudios pegados, y así lo señala el
revisor.
