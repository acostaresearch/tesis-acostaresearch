# Artículos de revisión: sistemática, de alcance y bibliométrica

Se lee en las Fases 1, 4, 5 y 6 cuando el tipo de estudio es una revisión. Una
revisión **no tiene Fase 3**: los estudios revisados son los Resultados.

## Qué tipo de revisión es (se fija en la Fase 1)

| Tipo | Pregunta | Guía de reporte | Producto central |
|---|---|---|---|
| Sistemática | ¿Qué dice la evidencia sobre X? (PICO / PEO) | PRISMA 2020 | Síntesis por temas o metaanálisis |
| De alcance (scoping) | ¿Qué se ha estudiado y cómo? (PCC) | PRISMA-ScR | Mapa de la evidencia |
| Bibliométrica | ¿Cómo se ha producido el campo? | Sin guía única; se declaran bases, ecuación, fecha, depuración y software (BIBLIO, si la revista la pide) | Indicadores y redes |
| Mixta (bibliométrica + sistemática) | Las dos | PRISMA 2020 para el cribado | Indicadores + síntesis de los incluidos |

## Métodos (Fase 4): orden de los subtítulos

1. **Diseño y registro.** Tipo de revisión y guía. Protocolo registrado
   (PROSPERO, OSF, INPLASY) con su código, o declaración de que no se registró.
   Nunca se inventa un código.
2. **Criterios de elegibilidad.** Inclusión y exclusión en tabla: población o
   contexto, concepto, tipo de estudio, periodo, idioma, tipo de documento.
3. **Fuentes y búsqueda.** Bases (Scopus, WoS, SciELO, ERIC, PubMed...), fecha
   exacta de la búsqueda, campo buscado (TITLE-ABS-KEY, TS=) y la **ecuación
   literal de cada base**, en tabla o en material suplementario.
4. **Selección.** Depuración de duplicados (con qué herramienta), cribado por
   título y resumen y luego a texto completo, por cuántos revisores, cómo se
   resolvieron los desacuerdos y su acuerdo (kappa de Cohen) si se calculó.
5. **Extracción de datos.** Qué variables se extrajeron (autor, año, país,
   diseño, muestra, hallazgo principal) y con qué formulario.
6. **Evaluación de calidad / riesgo de sesgo** (sistemática): herramienta
   concreta (CASP, MMAT para estudios mixtos, JBI, RoB 2, ROBINS-I). En las de
   alcance y bibliométricas suele omitirse, y se dice.
7. **Síntesis y análisis.** Síntesis temática o narrativa, o metaanálisis
   (modelo, heterogeneidad). En bibliometría: software y versión (bibliometrix
   en R, VOSviewer), unidad de análisis, umbrales, normalización.

Lo que el investigador no declare queda `[POR CONFIRMAR]`: fechas, número de
revisores, kappa, registro.

## Cómo exporta el investigador el corpus

- **Scopus:** resultados → *Export* → **CSV** (o BibTeX; los dos los lee bibliometrix; el RIS y el texto plano sirven para el inventario, no para bibliometrix) → marcar *Citation
  information*, *Bibliographical information*, *Abstract & keywords* e
  *Include references*. Máximo 2000 registros por exportación en BibTeX.
- **Web of Science:** *Export* → *Plain text file* → *Full record and cited
  references*, de 500 en 500.
- Se sube al servidor con el enlace de `trabajar_en_r` (opción `subir`), uno
  por base, y se guarda la cifra de registros de cada una: es la primera caja
  del PRISMA.

## Análisis bibliométrico en el servidor (bibliometrix, probado)

Si al subir el exporte el servidor arma solo la base bibliográfica (modo
MAPEO BIBLIOMÉTRICO de `trabajar_en_r`), usar lo que devuelve. Si no:

```r
library(bibliometrix)
M1 <- convert2df("scopus.csv", dbsource = "scopus", format = "csv")       # o "scopus.bib", format = "bibtex"
M2 <- convert2df("wos.txt",    dbsource = "wos",    format = "plaintext")
M  <- mergeDbSources(M1, M2, remove.duplicated = TRUE)   # cuántos se quitaron = caja de duplicados
# ATENCIÓN (probado con bibliometrix 5.4): tras mergeDbSources las referencias
# citadas (CR) se pierden y todos los registros quedan como DB = "ISI": la
# co-citación sale vacía y la colaboración internacional cae (0.86 % frente a
# 15.9 % reales en un corpus de prueba). Por eso:
#  - indicadores de producción, fuentes, autores, Lotka, Bradford y keywords: con M fusionado;
#  - co-citación y acoplamiento: con cada base por separado (M1 Scopus) y se declara;
#  - países y colaboración: con M1 (Scopus) o con bibliometria.py, que sí lee
#    las afiliaciones de ambas bases tras fusionar.
# Títulos bilingües de Scopus ("Título [Traducción]"): quitar la parte entre
# corchetes antes de comparar duplicados.
M$TI_n <- gsub("\\s*\\[[^]]+\\]\\s*$", "", M$TI)
# mergeDbSources no detecta un mismo trabajo indexado dos veces con DOI distinto:
# revisar títulos repetidos y retirarlos a mano, declarándolo
M$TI_n <- gsub("[^A-Z0-9]", "", M$TI_n); M[duplicated(M$TI_n) | duplicated(M$TI_n, fromLast = TRUE), c("TI", "DI", "PY")]
res <- biblioAnalysis(M, sep = ";")
sm  <- summary(res, k = 10, pause = FALSE, verbose = FALSE)
sm$MainInformationDF        # periodo, documentos, fuentes, autores, coautoría, % internacional
sm$AnnualProduction         # producción anual
sm$MostProdAuthors; sm$MostRelSources; sm$MostCitedPapers; sm$MostProdCountries
L <- lotka(M)               # en esta versión recibe M, no res
L$AuthorProd; L$Beta; L$R2
```

**Bradford: no usar `bradford(M)` en el servidor** (agota la memoria y se
pierde la orden). Calcularlo así:

```r
f <- sort(table(M$SO), decreasing = TRUE); a <- cumsum(f)
zona <- cut(a, c(0, sum(f)/3, 2*sum(f)/3, Inf), labels = c("Zona 1 (núcleo)", "Zona 2", "Zona 3"))
table(zona); names(f)[zona == "Zona 1 (núcleo)"]
```

Tasa de crecimiento anual (y advertir si el último año está incompleto):

```r
p <- sm$AnnualProduction
round(((tail(p$Articles, 1) / p$Articles[1])^(1 / (nrow(p) - 1)) - 1) * 100, 2)
```

Palabras clave y redes:

```r
tableTag(M, "DE")                                    # palabras clave de autor
NetMatrix <- biblioNetwork(M, analysis = "co-occurrences", network = "author_keywords", sep = ";")
net <- networkPlot(NetMatrix, n = 30, type = "fruchterman", Title = "", labelsize = 0.7)
ts  <- thematicMap(M, field = "DE", n = 250, minfreq = 3)   # mapa temático
```

Si el corpus mezcla idiomas y se trabaja con títulos o resúmenes
(`termExtraction`), quitar a mano las palabras vacías del español: `de`, `la`,
`en`, `el`, `los`, `las`, `del`, `y`, `para`, `con`, `una`, `por`.

Las figuras se guardan en la sesión (`png("fig2.png", 1600, 1000, res = 200)`
... `dev.off()`) y se descargan con la opción `descargar`.

### Sin R: bibliometria.py

Orden de preferencia: **1)** servidor Acosta con bibliometrix (`trabajar_en_r`);
**2)** R propio con bibliometrix (el código de arriba); **3)** `bibliometria.py`,
solo si el investigador trabaja en un chat que únicamente ejecuta Python
(ChatGPT con análisis de datos) o no tiene R.

```bash
python3 bibliometria.py informe scopus.csv savedrecs.txt --out salida/ --anio-ref 2026
```

Lee el CSV de Scopus y el texto plano de WoS; fusiona por DOI y por título
normalizado (sin la traducción entre corchetes de Scopus) y **lista para decisión
humana** los pares con mismo título y año pero DOI distinto
(`posibles_duplicados.csv`; `--quitar-doi-distinto` los retira). Entrega
`prisma_conteos.csv`, las tablas CSV (información principal, producción anual,
Bradford, autores, Lotka, países con SCP/MCP, citados, palabras clave y
co-ocurrencia con archivos para VOSviewer), figuras PNG si hay matplotlib y
`resumen_bibliometrico.md` con las tablas en la sintaxis del motor, listo para
la Fase 5. Contrastado con bibliometrix 5.4.1 sobre un corpus real: conteos
idénticos con `--modo bibliometrix`; las diferencias están explicadas en el
docstring del script.

En Métodos se declara así, sin atribuirlo a bibliometrix: «Los indicadores se
calcularon con un script propio en Python (bibliometria.py, Ruta del Artículo
Científico); la dispersión de fuentes se analizó con la ley de Bradford (1934) y
la productividad de autores con la ley de Lotka (1926), ajustada por mínimos
cuadrados en escala log-log». Las referencias de Bradford y Lotka se verifican
antes de citarlas.

## Acuerdo entre revisores y metaanálisis (servidor)

```r
# kappa de Cohen del cribado: una fila por registro, una columna por revisor (incluye/excluye)
irr::kappa2(cribado[, c("revisor1", "revisor2")])
# metaanálisis de efectos aleatorios (yi = tamaño de efecto, vi = varianza)
library(metafor)
m <- rma(yi, vi, data = efectos, method = "REML"); summary(m)   # efecto global, I², tau²
forest(m); funnel(m); regtest(m)                                 # bosque, embudo, Egger
```

`metafor`, `meta` e `irr` están instalados en el servidor (verificado en
octubre de 2026).

## Diagrama PRISMA

`prisma_flujo.py` (en las fases 4 y 5) lo dibuja a partir de los conteos y **se niega si la
aritmética no cuadra** (identificados − eliminados = cribados, etc.). El
paquete `PRISMA2020` no está en el servidor. Ejemplo:

```bash
python3 prisma_flujo.py --out figura1.png \
  --bases "Scopus=312;Web of Science=205" --duplicados 140 \
  --cribados 377 --excluidos-cribado 290 --buscados 87 --no-recuperados 4 \
  --evaluados 83 --excluidos-texto "Población distinta=21;Sin resultados=14;Idioma=3" \
  --incluidos 45
```

## Resultados (Fase 5): orden

**Bibliométrica:** (1) flujo de selección y tabla de información principal;
(2) producción anual con tasa de crecimiento; (3) fuentes más relevantes y
zonas de Bradford; (4) autores más productivos y ley de Lotka; (5) países y
colaboración; (6) documentos más citados; (7) palabras clave, co-ocurrencia y
mapa temático.

**Sistemática / de alcance:** (1) Figura PRISMA; (2) tabla de características
de los estudios incluidos (autor, año, país, diseño, muestra, hallazgo); (3)
calidad o riesgo de sesgo; (4) síntesis por pregunta o eje temático, citando
cada estudio incluido.

Cada cifra sale de la consola de R o del registro de cribado; ninguna se
redondea distinto ni se completa.

## Discusión (Fase 6) en una revisión

Se organiza **por pregunta de revisión o por eje temático**, no por hipótesis.
Los estudios incluidos sí se citan (son los Resultados); se contrastan con
revisiones previas y marcos teóricos de la Introducción. Las limitaciones
típicas: bases consultadas, idioma, periodo, sesgo de publicación, un solo
revisor.
