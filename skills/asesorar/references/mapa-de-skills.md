# Qué skill del método manda en cada parte

Las skills del método de Acosta | IA & Research viven en
`<METODO>\<producto>\fuente\<nn-nombre>\<nombre>\SKILL.md`.
Se leen **en el momento**, desde ahí, para usar siempre la versión vigente. No se copian.

Antes de diagnosticar o de redactar una sección se lee la skill que le toca (el `SKILL.md` y
los `references/` que nombre para esa parte). De ella se toma **el método**: qué debe traer la
sección, en qué orden, cuántos antecedentes, cómo se arma un párrafo, qué se comprueba.

## Qué se toma y qué no

Esas skills están escritas para el conector y para acompañar al tesista paso a paso. Aquí se
trabaja en local y de corrido, así que:

| De la skill | Aquí |
|---|---|
| Estructura de la sección, criterios de calidad, reglas de redacción, cantidades | **Se sigue tal cual.** |
| Reglas de fuentes: nada inventado, cada dato sale de una fuente leída, antecedentes que no favorecen | **Se sigue tal cual.** |
| Herramientas del conector (`mi_proyecto`, `guardar_capitulo`, `mis_fuentes`, `buscar_fuentes`, `enlace_del_word`…) | No existen aquí. Las fuentes se buscan con `buscar.py` y el Word se edita con `aplicar.py`. |
| Citas por clave `[AR…]` | Se escriben directamente en la norma de la universidad (APA 7, ISO 690, Vancouver). |
| Menús, preguntas al tesista, bienvenida, aprobación paso a paso | No se hacen. Lo que solo el cliente sabe va a la lista de preguntas para el cliente. |
| «El Word lo arma el servidor» | El Word es el del cliente, corregido sobre una copia. |

## Detectar el producto

| Señales en el avance o en la guía | Producto | Carpeta |
|---|---|---|
| Proyecto, plan o informe de tesis; hipótesis, variables, población y muestra, instrumento | Tesis | `skills/tesis/fuente/` |
| «Suficiencia profesional», experiencia laboral, empresa, cargo; sin hipótesis ni instrumento | TSP | `skills/tsp/fuente/` |
| Trabajo de curso, informe académico, monografía, informe para una empresa | Informe | `skills/informe/fuente/` |
| Manuscrito con datos propios para una revista (IMRyD) | Artículo empírico | `skills/articulo/fuente/` |
| Revisión sistemática, narrativa o bibliométrica para revista | Artículo de revisión | `skills/revision/fuente/` |

Si la universidad pide otra estructura, manda la guía de la universidad para el orden y los
nombres de las secciones, y la skill para el contenido de cada una.

## Tesis (`skills/tesis/fuente/`)

| Parte del documento | Skill |
|---|---|
| Título, delimitación, línea de investigación | `01-tema-y-delimitacion` |
| Realidad o situación problemática, formulación del problema, justificación, objetivos, hipótesis, matriz de consistencia | `02-problema-y-objetivos` |
| Antecedentes, bases teóricas, marco conceptual o definición de términos | `03-marco-teorico` |
| Tipo, nivel, diseño, variables y operacionalización, población y muestra, técnicas, análisis de datos, aspectos éticos | `04-metodologia` |
| Cronograma, presupuesto, financiamiento | `04b-aspectos-administrativos` |
| Cuestionario, guía de observación, ficha técnica, validez y confiabilidad | `05-instrumento-investigacion` |
| Cartas, consentimiento informado, protocolo de aplicación | `06-recoleccion-datos` |
| Resultados cuantitativos (descriptivos, normalidad, prueba inferencial) | `07-analisis-datos-rstudio` |
| Resultados cualitativos (categorías, codificación) | `07b-analisis-cualitativo` |
| Discusión y limitaciones | `08-discusion` |
| Conclusiones, recomendaciones, resumen y abstract | `09-conclusiones-abstract` |
| Texto que suena a IA | `10-humanizador-academico` (y `/turnitin` cuando ya hay reporte) |
| Similitud alta con reporte | `/turnitin` |

Las piezas comunes están en `skills/tesis/_comun/` (`parafraseo.md` sirve siempre que se
redacta a partir de una fuente).

## TSP (`skills/tsp/fuente/`)

| Parte | Skill |
|---|---|
| Ficha de la experiencia (empresa, cargo, periodo, problema, evidencias) | `01-tsp-fase0-experiencia` |
| Capítulo I · Introducción | `02-tsp-fase1-introduccion` |
| Capítulo II · Marco teórico | `03-tsp-fase2-marco-teorico` |
| Capítulo III · Descripción de la experiencia | `04-tsp-fase3-experiencia` |
| Capítulo IV · Resultados | `05-tsp-fase4-resultados` |
| Capítulo V · Conclusiones, recomendaciones, resumen, anexos | `06-tsp-fase5-conclusiones` |

El TSP no lleva hipótesis, instrumento ni muestra. Si el avance del cliente los trae, se
señala en el diagnóstico: suele ser una tesis mal encaminada o una guía que sí los pide.

## Informe (`skills/informe/fuente/`)

| Parte | Skill |
|---|---|
| El encargo, tipo de informe (curso, empresa, monografía), estructura | `01-informe-fase0-encargo` |
| Fuentes | `02-informe-fase1-fuentes` |
| Desarrollo | `03-informe-fase2-desarrollo` |
| Análisis y resultados | `04-informe-fase3-analisis-y-resultados` |
| Cierre: conclusiones, resumen, anexos | `05-informe-fase4-cierre` |

## Artículo empírico y de revisión (`skills/articulo/fuente/`, `skills/revision/fuente/`)

Mismas fases en las dos carpetas, con el prefijo `articulo-` o `revision-`:
fase 0 tema y orientación, fase 1 matriz de estrategia, fase 2 introducción, fase 3 revisión de
la literatura (solo artículo), fase 4 métodos, fase 5 resultados, fase 6 discusión, fase 7
conclusiones y abstract, fase 8 adaptación y envío a la revista, fase 9 respuesta a revisores.
No confundir las dos carpetas: un artículo empírico tiene datos propios; una revisión, no.

## Si la skill y la guía de la universidad se contradicen

Manda la guía de la universidad, y se anota en el informe de revisión. Ejemplo: la skill de
marco teórico pide antecedentes de cualquier base indexada y la guía de la UPRIT exige que el
60 % de las referencias sean artículos y el 30 % en otro idioma.
