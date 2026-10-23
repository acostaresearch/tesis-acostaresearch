# Ruta del Artículo Empírico: mapa único

Para artículos empíricos con **datos primarios** (recogidos por el
investigador) o **secundarios** (bases existentes): descriptivos,
correlacionales, comparativos, de regresión (lineal, logística, ordinal, de
conteo), multinivel, de panel, experimentales y cuasiexperimentales, SEM (PLS y
CB), validación de escalas, cualitativos y mixtos. El análisis se elige por la
pregunta, no por costumbre: ver el índice de `analisis.md`. **Las revisiones sistemáticas, de alcance y
bibliométricas tienen su propia ruta: la Ruta del Artículo de Revisión**
(skills `revision-fase*`). Si el investigador quiere una revisión, se le dice en
una línea y se le deriva allá.

Este archivo es **idéntico en todas las skills de la ruta**. Es la única fuente
de verdad sobre fases, nombres, insumos y entregables. Si algo de un SKILL.md
parece contradecirlo, manda este archivo.

## Las diez fases

| Fase | Skill | Recibe | Entrega |
|---|---|---|---|
| 0 · Tema y orientación | `articulo-fase0-tema-y-orientacion` | Una inquietud | `FICHA_[clave].docx` (2 páginas) y `REVISTA_[clave].json` (perfil de la revista) |
| 1 · Matriz de estrategia | `articulo-fase1-matriz-de-estrategia` | Ficha | `MATRIZ_[clave].xlsx` |
| 2 · Introducción | `articulo-fase2-introduccion` | Ficha, Matriz, exports RIS/CSV con resumen | `ARTICULO_[clave]_v2.docx`, `TRAZABILIDAD_[clave].xlsx`, `inventario.json` |
| 3 · Revisión de la literatura | `articulo-fase3-revision-literatura` | v2, Matriz, trazabilidad, inventario | `_v3.docx`, trazabilidad actualizada |
| 4 · Métodos | `articulo-fase4-metodos` | v3, Matriz, base de datos | `_v4.docx` con la Tabla 1 |
| 5 · Resultados | `articulo-fase5-resultados` | v4 y las **salidas del análisis** | `_v5.docx` |
| 6 · Discusión | `articulo-fase6-discusion` | v5 | `_v6.docx` |
| 7 · Conclusiones y abstract | `articulo-fase7-conclusiones-abstract` | v6 | `_v7.docx`: título definitivo, resumen, abstract, palabras clave, conclusiones |
| 8 · Adaptación y envío | `articulo-fase8-adaptacion-y-envio` | v7 y la guía de autores | `_v8.docx`, página de título con autoría, carta, declaraciones |
| 9 · Respuesta a revisores | `articulo-fase9-respuesta-revisores` | v8 enviada y el dictamen | Manuscrito con control de cambios y carta de respuesta |

`[clave]` es una palabra del tema (p. ej. `tecnoestres`), fijada en la Fase 0 y
la misma en todos los archivos. El número de versión del .docx coincide con la
fase que lo produjo.

**Cada fase entrega dos Word con el mismo texto:** `ARTICULO_[clave]_vN.docx`
con el formato de la revista destino y `ARTICULO_[clave]_vN_RESPALDO.docx` con
el formato neutro de la ruta, por si hay rechazo y hay que reenviar a otra
revista. Los dos los produce el motor en la misma llamada (`--perfil`). Ver
`perfil_revista.md`.

**Idioma de redacción: español.** Cada fase humaniza la sección que escribe
con `humanizador-academico` (ver `anti_ia.md`). El inglés solo aparece en el
abstract y, si la revista lo pide, en la traducción de la Fase 8.

## Quién es dueño de qué (para no preguntar dos veces)

| Dato | Se decide en | Después se lee, no se pregunta |
|---|---|---|
| Tipo de estudio y diseño | Fase 0 (tentativo), Fase 1 (cerrado) | Matriz, primera hoja («Diseño y muestra» o «Diseño de la revisión») |
| Revista destino, estilo de cita, estructura, límite, formato | Fase 0 | `REVISTA_[clave].json` (y Ficha, sección 7) |
| Acrónimos | Fase 2 en adelante | `articulo_docx.py esquema --acronimos` |
| Fuentes citables y sus claves | Fase 2 (inventario), crece en 3 y 6 | `inventario.json`; citas por clave (ver `fuentes_y_citas.md`) |
| Gestor de referencias (Zotero o Mendeley) | Lo elige el investigador | Entrada RIS/BibTeX o plataforma Acosta; salida `CITADAS_[clave].ris` |
| **Autores, filiación, ORCID, correspondencia, CRediT** | **Fase 8** | Nunca antes: la Ficha y el manuscrito van sin datos personales |
| Declaraciones (conflicto, financiamiento, ética, IA) | Fase 8, confirmadas por el autor | — |
| Término unificador (influencia / relación) | Fase 0 | Ficha, sección 1 |
| Objetivos, preguntas, hipótesis | Fase 1 | Matriz |
| Cifras del estudio | El análisis (ver abajo) | Salidas del análisis |

## Dónde se hace el análisis de datos

Ninguna fase del artículo calcula estadística por su cuenta. Las cifras salen,
en este orden de preferencia, de:

1. **El servidor del ecosistema Acosta** (herramienta `trabajar_en_r`, si está
   conectada): sesión de R real con tidyverse, psych, lavaan, seminr, lme4,
   MASS, pscl, etc. Ver `analisis.md` en las fases 4, 5 y 9.
2. La skill de tesis `analisis-datos-rstudio` (de ella se toman **solo las
   tablas y salidas**, no su redacción por objetivos, que es de tesis).
3. Las salidas que trae el investigador (SPSS, SmartPLS, JASP, Stata, R, Excel).

La Fase 4 **describe** el análisis y calcula solo la Tabla 1; la Fase 5
**reporta** las cifras. Si el investigador llega a la Fase 5 sin salidas, la
Fase 5 puede correr el análisis en el servidor siguiendo `analisis.md`
(o derivarlo a `analisis-datos-rstudio`); nunca lo estima.

## Cobertura por tipo de estudio

| Tipo | Fases | Variantes cubiertas | Lo que el investigador hace fuera |
|---|---|---|---|
| Cuantitativo (descriptivo, correlacional, regresión, predictivo) | 0 a 9 | — | Recoger los datos |
| SEM (PLS-SEM, CB-SEM), mediación y moderación | 0 a 9 | Modelo de medida y estructural | Recoger los datos |
| Experimental, cuasi, preexperimental | 0 a 9 | Equivalencia de grupos, efecto | Recoger los datos |
| Validación de escala (instrumental) | 0 a 9 | Estructura factorial, fiabilidad, invarianza | Recoger los datos |
| Cualitativo | 0 a 9 | Métodos y Resultados por categorías; Fase 3 sin hipótesis | Entrevistas y codificación (apoyo: `analisis-cualitativo` del servidor o Atlas.ti) |
| Mixto | 0 a 9 | Cada fase trata las dos ramas por separado | Recoger ambos datos |
| **Datos secundarios** (encuestas nacionales, bases públicas o institucionales, panel, series de tiempo) | 0 a 9 | Fuente, acceso y versión de la base; diccionario de variables; factores de expansión; licencia | Descargar la base y su diccionario |

## Skills de apoyo

- `instrumento-investigacion`, `recoleccion-datos`, `analisis-datos-rstudio`:
  skills de la ruta de tesis que sirven igual para un artículo, entre la Fase 1
  y la Fase 4, si todavía no hay datos.

## Humanizador

Cada fase humaniza **su sección** con `humanizador-academico` (español; una
ronda, 1 o 2 bloques) y el texto en inglés con `humanizador-academico-ingles`
(modo breve). Protocolo en `anti_ia.md` (fases 2 a 9). La pasada completa al
manuscrito es opcional, en la Fase 8.

## Si el investigador llega a mitad de camino

- Trae un .docx de otra fuente: se lee con `articulo_docx.py esquema` y se
  sigue desde la fase que le toca. Si su documento no salió de la ruta, se pasa
  primero por `articulo_docx.py nuevo` con su texto para unificar el formato.
- Trae un manuscrito avanzado **sin perfil de revista**: se arma el perfil
  (Fase 0, paso del perfil) y se pone al día en tres órdenes: copia
  `_vN_SIN_PERFIL.docx`; `normalizar ... --perfil REVISTA_[clave].json --out
  _vN.docx` (versión de la revista); `normalizar ... --out _vN_RESPALDO.docx`
  (respaldo neutro). Después, títulos al perfil con `reemplazar` y, si las
  citas están a mano, se dejan así (el motor las respeta) o se pasan a claves
  con el inventario.
- Falta la Ficha o la Matriz: se piden los datos mínimos (tipo de estudio,
  revista, estilo de cita, objetivos o pregunta) en **una sola pregunta** y se
  sigue. No se le devuelve a la Fase 0.
