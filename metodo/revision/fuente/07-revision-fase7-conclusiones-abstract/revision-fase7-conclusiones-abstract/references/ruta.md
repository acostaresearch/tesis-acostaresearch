# Ruta del Artículo de Revisión: mapa único

Para revisiones sistemáticas (PRISMA 2020), de alcance (PRISMA-ScR),
bibliométricas y mixtas (bibliométrica con síntesis sistemática). **Los
artículos con datos propios (correlacional, regresión, experimental, SEM,
cualitativo) tienen su propia ruta:
la Ruta del Artículo Empírico** (skills `articulo-fase*`). Si el investigador recoge datos propios, se le dice en una
línea y se le deriva allá.

Este archivo es **idéntico en todas las skills de la ruta**. Es la única fuente
de verdad sobre fases, nombres, insumos y entregables. Si algo de un SKILL.md
parece contradecirlo, manda este archivo.

## Las nueve fases (no hay Fase 3)

| Fase | Skill | Recibe | Entrega |
|---|---|---|---|
| 0 · Tema y orientación | `revision-fase0-tema-y-orientacion` | Una inquietud | `FICHA_[clave].docx` (2 páginas) y `REVISTA_[clave].json` (perfil de la revista) |
| 1 · Protocolo (matriz de estrategia) | `revision-fase1-matriz-de-estrategia` | Ficha | `MATRIZ_[clave].xlsx`: pregunta, criterios, bases, ecuación, registro |
| 2 · Introducción | `revision-fase2-introduccion` | Ficha, Matriz, exports RIS/CSV con resumen | `ARTICULO_[clave]_v2.docx`, `TRAZABILIDAD_[clave].xlsx`, `inventario.json` |
| 4 · Métodos | `revision-fase4-metodos` | v2, Matriz, conteos de búsqueda y cribado | `_v4.docx` con el protocolo PRISMA |
| 5 · Resultados | `revision-fase5-resultados` | v4, corpus o tabla de extracción, salidas de bibliometrix | `_v5.docx` con Figura PRISMA e indicadores |
| 6 · Discusión | `revision-fase6-discusion` | v5 | `_v6.docx` |
| 7 · Conclusiones y abstract | `revision-fase7-conclusiones-abstract` | v6 | `_v7.docx`: título con el tipo de revisión, resumen estructurado, conclusiones |
| 8 · Adaptación y envío | `revision-fase8-adaptacion-y-envio` | v7 y la guía de autores | `_v8.docx`, página de título, carta, checklist PRISMA |
| 9 · Respuesta a revisores | `revision-fase9-respuesta-revisores` | v8 enviada y el dictamen | Manuscrito con control de cambios y carta de respuesta |

La numeración salta de la 2 a la 4 a propósito: en una revisión no hay
"Revisión de la literatura" aparte, porque los estudios revisados **son** los
Resultados. La Fase 4 recibe la `_v2.docx` y entrega la `_v4.docx`.

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
| Pregunta de revisión, criterios, bases y **ecuación de búsqueda del corpus** | Fase 1 (la arma y la prueba el investigador) | Matriz; la Fase 4 la reporta literal. La búsqueda de la Fase 2 es otra: solo para escribir la Introducción |
| Conteos del PRISMA | El registro de búsqueda y cribado | Matriz y Métodos |
| Indicadores bibliométricos | bibliometrix (ver `revision.md`) | Salidas de R |

## Dónde se hacen la búsqueda, el cribado y el análisis

- **La búsqueda** la ejecuta el investigador en Scopus, Web of Science y otras
  bases con la ecuación que arma la Fase 1, y exporta el corpus.
- **El cribado** (título y resumen, luego texto completo) lo hace el
  investigador, idealmente con dos revisores; la ruta le da la plantilla de
  registro y cuenta los números para el PRISMA.
- **El análisis bibliométrico** corre en el servidor del ecosistema Acosta
  (`trabajar_en_r`, con bibliometrix) o en el R/VOSviewer del investigador. Las
  recetas probadas están en `revision.md` (fases 1, 2 y 4 a 8).
- **La síntesis** de los estudios incluidos la redacta la Fase 5 desde la tabla
  de extracción, citando cada estudio.

## Cobertura por tipo de revisión

| Tipo | Guía | Fases | Lo que el investigador hace fuera |
|---|---|---|---|
| Sistemática | PRISMA 2020 | 0, 1, 2, 4 a 9 | Búsqueda, cribado con dos revisores, extracción |
| De alcance (scoping) | PRISMA-ScR | 0, 1, 2, 4 a 9 | Búsqueda, cribado, mapeo |
| Bibliométrica | Declaración de bases, ecuación, fecha y depuración | 0, 1, 2, 4 a 9 | Exportar el corpus de Scopus/WoS |
| Mixta (bibliométrica + sistemática) | PRISMA 2020 para el cribado | 0, 1, 2, 4 a 9 | Las dos anteriores |
| Metaanálisis | PRISMA 2020 | 0, 1, 2, 4 a 9 | Extracción de tamaños de efecto (el modelo se corre en el servidor con `metafor` o `meta`) |

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
