# El mapeo en el servidor, con `trabajar_en_r`

Es el carril para un corpus de **Scopus, Web of Science o PubMed**. R corre en el
servidor, dentro de la sesión del proyecto, con bibliometrix instalado. El
investigador no instala nada ni escribe código: sube el exporte de su
universidad —o, sin ese acceso, busca en su perfil y pulsa un botón— y lee lo
que le explicas.

**En el artículo va primero el exporte (1b)**: el mapeo es el resultado que
juzga el revisor, y el exporte trae los datos de Scopus tal cual. El perfil (1)
es para quien no tiene Scopus por su universidad, y se declara «búsqueda en
Scopus; metadatos de OpenAlex». En la tesis es al revés: el perfil es lo normal.

El carril de **OpenAlex** no va por aquí: el R del servidor no tiene internet y
`openalexR` necesita consultar OpenAlex. Ese sigue con
`script_bibliometrix.R` en su RStudio o en Posit Cloud.

## 1. Desde su perfil (sin acceso institucional)

Se le dan estas indicaciones, no un enlace:

1. **acostaresearch.com/perfil**, pestaña **«Tus fuentes de Scopus»**.
2. En **«Buscar en Scopus»**, **«Consulta avanzada»** activada: pega la ecuación
   y **Buscar**. Se afina con él hasta que el número esté en el rango.
3. Con la búsqueda final en pantalla, **«Hacer un mapeo bibliométrico con
   estos resultados»**. El botón manda la búsqueda de los resultados que se
   ven, y reemplaza lo que hubiera en su sesión de R.
4. Vuelve y dice que ya lo mandó.

Qué pasa por detrás: la web toma hasta 2000, los más citados, completa sus
datos en OpenAlex (autores con su institución y país, palabras clave, resumen y
referencias) y los deja en su sesión de R, sin exportar nada. Cuando vuelva,
`datos` ya está cargado: se comprueba como en el punto 5 de 1b, y el origen
tiene que traer SU ecuación. Dos cosas se declaran
en Métodos: las palabras clave son las de OpenAlex, y la cocitación va por
identificadores de OpenAlex, no por referencias en texto.

## 1b. Con su exporte (lo preferente en el artículo)

Cuando tiene Scopus, Web of Science o PubMed por su universidad, o ya bajó el
archivo.

1. `trabajar_en_r` sin argumentos devuelve el enlace de subida si la sesión
   está vacía; si ya tiene datos (su matriz), con `subir: true`, y lo que suba
   los reemplaza en la sesión. Dáselo como enlace que se pulsa, sin escribir la
   dirección.
2. Que suba **el archivo tal cual lo bajó**. Si lo abre y lo guarda en Excel, el
   CSV cambia de separador y de codificación y deja de ser el de Scopus.
3. El servidor lo reconoce por dentro, no por la extensión:

   | Exporte | Qué hace el servidor |
   |---|---|
   | Scopus CSV | lo lee bibliometrix |
   | Scopus BibTeX | lo lee bibliometrix |
   | Scopus texto plano (lo que baja por defecto) | lo pasa a CSV con las mismas columnas y lo lee bibliometrix |
   | WoS texto plano o BibTeX | lo lee bibliometrix |
   | PubMed MEDLINE | lo lee bibliometrix |
   | BibTeX de Zotero o Mendeley | **lo rechaza**: no trae referencias ni afiliaciones |

4. Hasta 25 MB, unos 2000 documentos con resumen y referencias. Si pasa, que
   acote el periodo o el tipo de documento, o que exporte sin el resumen y se
   haga la coocurrencia sobre palabras clave.
5. La página le dice cuántos documentos se leyeron. Cuando vuelva al chat,
   compruébalo tú:

   ```r
   cat("Documentos:", nrow(datos), "\n")
   cat("Periodo:", min(datos$PY, na.rm = TRUE), "-", max(datos$PY, na.rm = TRUE), "\n")
   cat("Fuentes:", length(unique(datos$SO)), "\n")
   cat("Con referencias:", sum(!is.na(datos$CR) & !tolower(datos$CR) %in% c("", "none")), "\n")
   ```

   Si «Con referencias» es cero, **exportó sin referencias**: la cocitación no
   va a salir. Díselo ahora, no en el paso 7.

## 2. Las funciones

`datos` ya es la tabla de bibliometrix: una fila por documento, con las
etiquetas AU, TI, SO, PY, TC, CR, DE, ID, C1…

**`resumen_bibliometrico(k = 10)`**: la información principal del corpus
(periodo, fuentes, documentos, tasa de crecimiento, citas por documento,
autores, colaboración internacional), la producción anual, los autores y las
fuentes más productivos, los países y los documentos más citados. Es la
base del paso 5.

**`figura_bibliometrica(tipo)`**: dibuja una figura, la guarda como
`figura_<tipo>.png` para el Word e imprime sus cifras en la consola.

| Paso | `tipo` | Qué imprime además de la figura |
|---|---|---|
| 5 | `produccion_anual` | documentos por año |
| 5 | `fuentes` | las n fuentes con más documentos |
| 5 | `autores` | los n autores con más documentos |
| 5 | `paises` | el país del autor de correspondencia |
| 5 | `bradford` | fuentes por zona y el núcleo (Zona 1) |
| 5 | `lotka` | autores por número de documentos; Beta, C y R² |
| 6 | `palabras` | las n palabras clave más frecuentes |
| 6 | `coocurrencia` | nodos y su cluster |
| 6 | `mapa_tematico` | cada cluster con frecuencia, centralidad y densidad |
| 7 | `cocitacion` | referencias y su cluster |
| 7 | `coautoria` | autores y su cluster |
| 7 | `colaboracion_paises` | países y su cluster |

Opciones: `n` (cuántos elementos), `campo` (`"DE"`, palabras clave de autor,
por omisión si el exporte las trae; `"ID"`, las que asigna la base; `"TI"` o
`"AB"`, los términos de dos palabras de los títulos o los resúmenes) y
`minfreq` (frecuencia mínima de una palabra en el mapa temático). **Con datos de
OpenAlex** (el buscador de la web), `palabras`, `coocurrencia` y
`mapa_tematico` van con `campo = "TI"` o `"AB"`: sus palabras clave las asigna
un clasificador.

**Si los datos llegaron desde el buscador de la web**, al llamar a
`trabajar_en_r` sin código sale «DE DÓNDE SALIERON ESTOS DATOS»: la ecuación,
la fecha y las cifras de cada paso (resultados en Scopus, con DOI, encontrados
en OpenAlex). Son las primeras cajas del PRISMA.

**Una figura por llamada.** Cada llamada tiene 45 segundos, y con miles de
documentos una red se come buena parte. Para lo que no cubren estas funciones
—evolución temática, estructura conceptual, historiógrafo— se llama a
bibliometrix tal cual (`thematicEvolution`, `conceptualStructure`,
`histNetwork`). Para dejar el PNG listo para el Word:
`png("figura_evolucion.png", width = 1600, height = 1100, res = 200); …; dev.off()`.

## 3. Cuando algo falla

- **«bibliometrix no pudo con …»**: pasa con corpus pequeños o cuando todos los
  documentos comparten país, tema o autor. No es un fallo del investigador:
  esa figura no aporta con este corpus y se deja fuera, o se prueba con un `n`
  o un `minfreq` menor.
- **Se acabó el tiempo**: la red era demasiado grande para una llamada. Probar
  con un `n` menor o sobre `campo = "DE"`.
- **Se cortó (memoria)**: el corpus es demasiado grande para el servidor. Que
  acote la búsqueda.

## 4. Lo que no cambia

- Las cifras del texto salen de la consola de esta sesión. El informe y el
  repaso de cifras lo comprueban.
- Lo que corrió queda en su análisis: `ver_analisis` lo lee, y el guion se
  puede repetir en RStudio.
- Las figuras rotulan en inglés: se nombran en español en el texto.
- bibliometrix se cita: Aria y Cuccurullo (2017), guardada con
  `anadir_a_mis_fuentes` (DOI 10.1016/j.joi.2017.08.007).
