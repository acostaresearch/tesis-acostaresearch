# =============================================================================
# MAPEO BIBLIOMÉTRICO — Fase 3B · Acosta | IA & Research
#
# Se le entrega al investigador POR BLOQUES, uno por paso, no todo de golpe.
# Cada bloque se pega en RStudio y se ejecuta; lo que devuelve al chat es la
# salida, no el código.
#
# Funciona igual en RStudio instalado y en Posit Cloud (posit.cloud), que es
# gratuito y no requiere instalar nada. A quien no tenga R, mándalo ahí.
# =============================================================================


# --- BLOQUE 0 · Instalación (solo la primera vez) ----------------------------
#
# Tarda unos minutos. Si pregunta por compilar desde el código fuente, "No".

install.packages("bibliometrix")
install.packages("openalexR")   # solo si el corpus viene de OpenAlex

library(bibliometrix)


# --- BLOQUE 1A · Cargar un export de SCOPUS ----------------------------------
#
# Sustituir la ruta por la del archivo descargado.
#
# EN WINDOWS: las barras van al revés de como las copia el explorador.
#   mal   "C:\Users\Ana\Downloads\scopus.csv"
#   bien  "C:/Users/Ana/Downloads/scopus.csv"

M <- convert2df(
  file     = "C:/Users/TU_USUARIO/Downloads/scopus.csv",
  dbsource = "scopus",
  format   = "csv"        # usar "bibtex" si se exportó en .bib
)

# Lo que hay que devolver al chat: estas tres cifras.
cat("Documentos:", nrow(M), "\n")
cat("Periodo:", min(M$PY, na.rm = TRUE), "-", max(M$PY, na.rm = TRUE), "\n")
cat("Fuentes distintas:", length(unique(M$SO)), "\n")


# --- BLOQUE 1B · Cargar desde WEB OF SCIENCE ---------------------------------
#
# Igual, cambiando dbsource. El export de WoS suele ser .txt con formato
# "plaintext"; si se exportó en BibTeX, poner "bibtex".

M <- convert2df(
  file     = "C:/Users/TU_USUARIO/Downloads/savedrecs.txt",
  dbsource = "wos",
  format   = "plaintext"
)


# --- BLOQUE 1C · Traer el corpus desde OPENALEX ------------------------------
#
# El carril de quien NO tiene suscripción. Aquí no se descarga ningún archivo:
# R consulta OpenAlex directamente.
#
# El correo no es opcional por educación: identifica la petición y da acceso al
# grupo de tráfico rápido. Poner uno real.

library(openalexR)
options(openalexR.mailto = "TU_CORREO@ejemplo.com")

datos <- oa_fetch(
  entity      = "works",
  title_and_abstract.search = "TUS TÉRMINOS AQUÍ",
  from_publication_date = "2019-01-01",
  to_publication_date   = "2026-12-31",
  type        = "article",
  # Descomentar para acotar a producción de un país:
  # institutions.country_code = "pe",
  # Descomentar para acotar el idioma:
  # language  = "es",
  verbose     = TRUE
)

cat("Documentos traídos:", nrow(datos), "\n")

# Y se convierte al formato que entiende bibliometrix.
M <- oa2bibliometrix(datos)


# --- BLOQUE 2 · Panorama descriptivo (Paso 5) --------------------------------

resultados <- biblioAnalysis(M, sep = ";")
S <- summary(resultados, k = 15, pause = FALSE)

# Devolver al chat lo que imprime `summary`: son las tablas principales.

plot(x = resultados, k = 15, pause = FALSE)

# Ley de Bradford — el núcleo de revistas que concentra el campo.
bradford(M)

# Ley de Lotka — cómo se reparte la productividad entre autores.
lotka <- lotka(M)
lotka$AuthorProd


# --- BLOQUE 3 · Estructura conceptual (Paso 6) -------------------------------
#
# CON CORPUS DE SCOPUS O WOS: se usan las palabras clave de autor ("DE"),
# que las escribió una persona.

red_palabras <- biblioNetwork(
  M,
  analysis = "co-occurrences",
  network  = "keywords",
  sep      = ";"
)

networkPlot(
  red_palabras,
  n = 40, Title = "Coocurrencia de palabras clave",
  type = "fruchterman", labelsize = 0.8
)

# CON CORPUS DE OPENALEX: sus palabras clave las asigna un clasificador y traen
# ruido ("Context (archaeology)" en un artículo de educación). Se calcula sobre
# títulos y resúmenes, y ESO SE DECLARA EN MÉTODOS.
#
#   field = "TI"  → títulos
#   field = "AB"  → resúmenes

mapa <- thematicMap(
  M,
  field   = "DE",     # cambiar a "TI" si el corpus vino de OpenAlex
  n       = 250,
  minfreq = 5,
  size    = 0.5,
  repel   = TRUE
)

plot(mapa$map)

# La tabla que interpreta los cuadrantes. Es lo que hay que devolver al chat:
# cada cluster con su centralidad y su densidad.
mapa$clusters[, c("label", "freq", "centrality", "density")]


# --- BLOQUE 4 · Evolución temática (Paso 6, opcional) ------------------------
#
# Solo si el periodo da para partirlo. Los cortes se eligen por criterio, no
# por comodidad: un hito del campo, un cambio normativo, la pandemia.

evolucion <- thematicEvolution(M, field = "DE", years = c(2015, 2020))
plotThematicEvolution(evolucion$Nodes, evolucion$Edges)


# --- BLOQUE 5 · Estructura intelectual (Paso 7, prescindible) ----------------

# Cocitación: qué trabajos sostienen el campo.
cocitacion <- biblioNetwork(M, analysis = "co-citation", network = "references", sep = ";")
networkPlot(cocitacion, n = 30, Title = "Red de cocitación", type = "fruchterman")

# Coautoría: quién trabaja con quién.
coautoria <- biblioNetwork(M, analysis = "collaboration", network = "authors", sep = ";")
networkPlot(coautoria, n = 30, Title = "Red de coautoría", type = "fruchterman")

# Colaboración entre países.
paises <- metaTagExtraction(M, Field = "AU_CO", sep = ";")
red_paises <- biblioNetwork(paises, analysis = "collaboration", network = "countries", sep = ";")
networkPlot(red_paises, n = 25, Title = "Colaboración entre países", type = "circle")


# --- BLOQUE 6 · Exportar las figuras -----------------------------------------
#
# Para pegarlas en el Word. 300 ppp es lo que piden casi todas las revistas.

png("figura_produccion_anual.png", width = 2400, height = 1500, res = 300)
plot(x = resultados, k = 10, pause = FALSE)
dev.off()

png("figura_mapa_tematico.png", width = 2400, height = 1800, res = 300)
plot(mapa$map)
dev.off()


# --- ALTERNATIVA · biblioshiny ------------------------------------------------
#
# Todo lo anterior con menús, sin escribir código. Para quien se atasque con R:
#
#   biblioshiny()
#
# Abre una ventana en el navegador donde se sube el archivo y se pulsan
# botones. Sale lo mismo. Se ofrece a quien lo pida, pero el código de arriba
# es preferible: queda escrito, y un artículo de revisión tiene que poder
# reproducirse.
