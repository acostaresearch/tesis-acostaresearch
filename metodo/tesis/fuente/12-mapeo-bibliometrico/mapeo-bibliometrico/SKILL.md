---
name: mapeo-bibliometrico
description: Herramienta de apoyo de la tesis para mapear un campo con bibliometría (bibliometrix en R). Dos usos. BREVE, para el marco teórico - dos a cuatro figuras que muestran cómo ha crecido el tema, qué se estudia y qué falta, y entran como un subapartado de los Antecedentes. COMPLETO, para una tesis de revisión sistemática o bibliométrica - protocolo con criterios y PRISMA para la Metodología, y el mapeo entero (producción, fuentes, Bradford, Lotka, países, coocurrencia, mapa temático, cocitación y el vacío) como capítulo de Resultados. Con un exporte de Scopus, Web of Science o PubMed, R corre en el servidor con trabajar_en_r y el tesista solo sube su archivo; con OpenAlex, se le da el código para RStudio. Interpreta cada figura y guarda el texto en el capítulo que toca. Nunca inventa cifras, autores ni conclusiones que las figuras no sostengan. ACTIVAR con mapeo bibliométrico, análisis bibliométrico, bibliometrix, revisión bibliométrica, tesis de revisión sistemática, mapa temático, o cómo ha crecido mi tema.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Mapeo bibliométrico

## Para qué sirve esta skill

Mapea el campo de la tesis con bibliometría: cuántos trabajos hay y cómo han
crecido, dónde se publican, quién los firma, de qué temas hablan y cuáles están
vivos o agotados. Responde con figuras lo que en un marco teórico suele
responderse con opiniones.

Es una **herramienta de apoyo**, no una fase: se abre cuando el tesista la pide,
esté donde esté de su tesis, y deja el texto en el capítulo que corresponde.

Tiene **dos usos**, y lo primero es saber cuál:

| Uso | Para quién | Qué sale | Dónde se guarda |
|---|---|---|---|
| **Breve** | Cualquier tesis que quiera respaldar sus antecedentes | 2 a 4 figuras y 3 a 6 párrafos | Un subapartado de 2.1 Antecedentes, en `marco-teorico` |
| **Completo** | Tesis de revisión sistemática o bibliométrica | El mapeo entero, con PRISMA | Resultados en `analisis-datos-rstudio`; el protocolo, en lo acordado de `metodologia` |

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un .docx, un PDF ni ningún otro archivo del capítulo.** No usa la skill `docx`, no escribe en `/mnt/user-data/outputs/`, no usa `present_files` y no entrega archivos en el chat. Las figuras las dibuja R en la sesión del proyecto y el Word las incrusta solas.

El documento lo arma el servidor de la plataforma con lo que está guardado en el proyecto: portada, índice, capítulos en orden, y las citas y las referencias escritas en la norma del proyecto, enlazadas a Zotero cuando el tesista lo conectó. La skill **redacta, guarda y entrega el enlace**.

```
1. mi_proyecto        al abrir la conversación (trae la norma de citas)
2. ver_capitulo       antes de preguntarle nada del capítulo;
                      lee `problema-y-objetivos` y `marco-teorico`
                      con `texto: true`
3. buscar_fuentes     al necesitar respaldo; la cita nace atada a
   / mis_fuentes      su clave de biblioteca, Zotero y Mendeley incluidos
4. guardar_capitulo   clave `marco-teorico` (breve) o
                      `analisis-datos-rstudio` (completo)
5. revisar_evidencia  antes de entregar
6. enlace_del_word    cuando quiera el documento
```

**Las citas se marcan con la clave de la fuente, no se escriben.** Así:

```
…afecta al rendimiento académico [AR97D22F86].
Braun y Clarke [AR97D22F86:n] proponen que…
«…» [AR97D22F86:p. 45]
[FALTA FUENTE]   cuando no hay respaldo
```

La skill **no escribe la cita** en texto («(Pérez y García, 2024)», «(1)», «[1]»), **no escribe la lista de referencias** y **no cita de memoria**. Solo usa claves que haya devuelto una búsqueda o la biblioteca. Al armar el Word, el servidor convierte cada clave en su cita y su referencia.

**Un solo documento, siempre al día.** No hay versiones V1, V2… del documento: el servidor mantiene uno solo con los capítulos en orden. Lo guardado se lee con `ver_capitulo` (`texto: true`). Solo se le pide que pegue algo si ese capítulo no está guardado.

**El formato no se pregunta.** Márgenes, tipografía e interlineado son configuración del proyecto en la plataforma. Lo único de formato que la skill sí necesita es la **norma de citas**: si `mi_proyecto` no la trae, se pregunta una vez y se guarda con `guardar_avance` (`estiloCitas`). Nada se convierte ni se renumera a mano.

**Entre corchetes, en el texto guardado, solo van** las claves `[AR…]`, `[FALTA FUENTE]` y la marca de figura `[Insertar aquí la Figura N: archivo.png]`. Los avisos para el tesista van en el chat, nunca dentro del capítulo.

**Si un guardado falla, se dice con esa palabra: no se guardó.** No se inventa que quedó guardado ni se entrega un archivo armado por la skill como reemplazo.

El detalle de la biblioteca, las marcas de cita, la norma y las seis herramientas de fuentes está en `references/integracion_zotero.md`. **Leerlo antes de citar por primera vez** (con `redactar`, `referencia: "integracion_zotero.md"`). Al final de ese archivo están **las demás herramientas de su perfil** (Scopus con SciELO y ALICIA, Zotero, Mendeley, R, ATLAS.ti y el mapa en VOSviewer) y cuándo nombrarlas.

## Regla de oro: veracidad absoluta

1. **Ninguna cifra que no venga de una salida real de R.** Ni un total de
   documentos, ni un año de pico, ni un nombre de autor. Si todavía no se ha
   ejecutado el análisis, no hay números que escribir.
2. **Ningún hallazgo que la figura no sostenga.** Un mapa temático con cuatro
   clusters permite decir que la coocurrencia agrupó los términos en cuatro
   conjuntos, no que el campo tiene cuatro líneas consolidadas.
3. **Ninguna interpretación causal.** La bibliometría describe qué se ha
   publicado, no por qué. Un pico en 2020 es un pico en 2020; «por la
   pandemia» es una conjetura del tesista y se escribe como tal.
4. **bibliometrix se cita siempre**: su licencia lo exige. Se guarda la fuente
   con `anadir_a_mis_fuentes` (DOI 10.1016/j.joi.2017.08.007: Aria y
   Cuccurullo, 2017, *Journal of Informetrics*) y se cita con su clave donde se
   nombra el programa.

## Regla del acompañamiento

- **Un paso por turno.** El tesista suele ser novato en bibliometría.
- Toda pregunta técnica lleva como última opción «No me queda claro, ponme
  ejemplos».
- **No instala nada si el corpus viene de Scopus, WoS o PubMed**: R corre en el
  servidor. Solo el carril de OpenAlex necesita su RStudio o Posit Cloud, porque
  el R del servidor no tiene internet.
- Sin biblioshiny: el código escrito es lo que hace el mapeo reproducible.

## Paso 1 — Punto de partida y uso

Leer `mi_proyecto`, y con `ver_capitulo` (`texto: true`, y `parte` mientras haya
más) `problema-y-objetivos` y `marco-teorico`. De ahí salen las variables, la
población y el estado de los antecedentes.

**Y mirar la sesión de R ANTES de preguntar nada del corpus**: `trabajar_en_r`
sin argumentos. Si ya hay un exporte cargado —y sobre todo si sale «DE DÓNDE
SALIERON ESTOS DATOS», que es la búsqueda que mandó desde el buscador de Scopus
de la web—, el corpus ya está: no se le pregunta cómo exportó ni se le pide
exportar otra vez. Se le dice lo que hay (de dónde salió, cuántos documentos) y,
tras preguntar el uso, se salta del Paso 2 al 4 para comprobarlo; el Paso 3
(criterios y PRISMA) sigue valiendo en el uso completo, con las cifras del
origen como primeras cajas. Si el tesista dice «ya cargué mis resultados», es
esto: mirarlo, no suponerlo.

Preguntar **para qué lo quiere**, con las dos opciones de la tabla de arriba:

- «Quiero respaldar mis antecedentes con un panorama del tema» → **breve**.
- «Mi tesis es una revisión sistemática o bibliométrica» → **completo**.
- «No me queda claro, ponme ejemplos».

En el uso **breve**, mirar si el marco teórico ya tiene 2.1 Antecedentes
guardado. Si no lo tiene, decírselo: el análisis se puede hacer ya, pero el
subapartado se escribe cuando los antecedentes estén guardados, para no
pisarlos.

## Paso 2 — De dónde sale el corpus y la ecuación

| Opción | Cuándo | Dónde corre R |
|---|---|---|
| **Scopus o Web of Science** | Tiene acceso por su universidad | En el servidor |
| **PubMed** | Ciencias de la salud | En el servidor |
| **El buscador de Scopus de la web** (acostaresearch.com → Mi perfil) | No tiene cuenta en scopus.com, o no quiere exportar | En el servidor, con los datos de OpenAlex |
| **OpenAlex** | No tiene acceso | En su RStudio o Posit Cloud |

**Si solo necesita un mapa al estilo VOSviewer** (una figura para el marco teórico, no el análisis completo), no hace falta la sesión de R: en su perfil, «Tus herramientas» → «Mapa en VOSviewer» → «Crear mapa», con una búsqueda o con sus fuentes, y se lleva la imagen, la tabla en Excel y los archivos para VOSviewer de escritorio. Se le ofrece esa vía antes de armar el corpus.

**El camino por defecto es su perfil, no exportar.** La búsqueda se prueba y
se manda desde el buscador de Scopus de acostaresearch.com, y se le dan estas
indicaciones, no un enlace:

1. Entra en **acostaresearch.com/perfil**, pestaña **«Tus fuentes de Scopus»**.
2. En **«Buscar en Scopus»**, activa **«Consulta avanzada»**, pega la ecuación
   y pulsa **Buscar**. Ahí ve cuántos documentos salen: se afina la ecuación
   con él hasta que el número esté en el rango.
3. Con la búsqueda final en pantalla, pulsa **«Hacer un mapeo bibliométrico
   con estos resultados»**, debajo del número. Tarda unos segundos; si tiene
   dos licencias, elige el proyecto.
4. Vuelve a la conversación y dice que ya lo mandó.

No hace falta cuenta en scopus.com ni exportar nada. **El enlace de subida
(`trabajar_en_r` con `subir: true`) es solo para quien YA tiene un archivo**
exportado de scopus.com, Web of Science o PubMed, o si su asesor exige el
exporte oficial: entonces sí se le explica cómo exportar con todos los campos.

La diferencia, dicha con honestidad, está en `references/openalex_vs_scopus.md`:
con Scopus el mapa temático sale mejor, porque sus palabras clave las
escribieron personas.

La ecuación se arma con `references/busqueda_bases.md`, a partir de las
variables de su matriz de consistencia. El tamaño del resultado decide si sirve:

- **Menos de 150 documentos** → la ecuación es demasiado estrecha.
- **De 300 a 3000** → el rango bueno. En el uso breve, desde 150 ya da un
  panorama.
- **Más de 5000** → sobra un término amplio, o falta acotar periodo o tipo de
  documento.

**Al exportar, marcar TODOS los campos**, o como mínimo resumen, palabras
clave, afiliaciones y **referencias**: sin referencias no hay cocitación.
Formatos que lee el servidor: de Scopus, CSV, BibTeX o el texto plano que baja
por defecto; de WoS, texto plano o BibTeX; de PubMed, MEDLINE. Un archivo por
análisis, de hasta 25 MB.

## Paso 3 — Criterios de inclusión y PRISMA

**Solo en el uso completo**; en el breve se anota el periodo y el tipo de
documento y se pasa al Paso 4.

Definir con él y dejar escrito: periodo y por qué, tipo de documento, idioma,
área temática y duplicados si combina bases. Con eso se arma el diagrama PRISMA,
con la plantilla de `references/criterios_prisma.md`.

Registrarlo con `guardar_avance` en el capítulo `metodologia`: la base, la
ecuación exacta, la fecha de la búsqueda, los criterios y las cifras del PRISMA.
Es el protocolo que la Metodología de una tesis de revisión redacta como su
diseño, y así lo encuentra cuando se trabaje ese capítulo.

## Paso 4 — Cargar el corpus en R

**Desde su perfil (lo normal).** Las indicaciones del Paso 2: pestaña «Tus
fuentes de Scopus», buscar con la ecuación final y pulsar «Hacer un mapeo
bibliométrico con estos resultados». No se le da ningún enlace. Cuando diga
que ya lo mandó, `trabajar_en_r` sin argumentos: tiene que salir «DE DÓNDE
SALIERON ESTOS DATOS» con SU ecuación. Si sale otra, lo mandó con otra
búsqueda en pantalla: que la repita.

**Si ya tiene un archivo exportado** (scopus.com, WoS, PubMed). Llamar a
`trabajar_en_r` sin argumentos, o con `subir: true` si la sesión ya tiene
datos: devuelve el enlace de subida. Dárselo como enlace que se pulsa y
pedirle que suba el exporte **tal cual lo bajó**, sin abrirlo en Excel.

En los dos casos, cuando vuelva, comprobar
con `codigo` los documentos, el periodo, las fuentes y cuántos traen
referencias. Si su tesis ya tiene una matriz en la sesión de R, avisarle
antes: **la sesión es una sola, y el exporte ocupa el sitio de la matriz**. Su
análisis de Resultados ya guardado no se toca —lo del mapeo se guarda aparte y
se lee con `ver_analisis` (`capitulo: "mapeo-bibliometrico"`)—, pero si luego
quiere seguir analizando su matriz, tendrá que volver a subirla. Lo mejor es
hacer el mapeo antes o después del análisis de su matriz, no en medio. Todo el
carril, con las funciones y los límites, en `references/r_en_el_servidor.md`.

**Carril de RStudio (OpenAlex).** El código completo y comentado de
`references/script_bibliometrix.R`; él lo corre y pega las salidas.

Si el número de documentos no se parece a lo que exportó, algo falló en la
carga: `references/errores_comunes.md`.

## Paso 5 — El panorama descriptivo

`resumen_bibliometrico()` y, una por llamada, las figuras que tocan:

- **Breve**: `produccion_anual` siempre; `paises` o `fuentes` si aportan a su
  tema.
- **Completo**: `produccion_anual`, `fuentes`, `bradford`, `autores`, `lotka` y
  `paises`, más la tabla de documentos más citados del resumen.

Cómo se lee cada figura y qué NO se puede afirmar de ella:
`references/leer_las_figuras.md`. Interpretar, no describir: «la producción
crece desde 2018» describe; «el tema se consolida a partir de 2018, cuando
aparecen las revistas del núcleo de Bradford» interpreta.

## Paso 6 — La estructura conceptual

- **Breve**: `mapa_tematico`, que es la figura que más aporta a unos
  antecedentes: qué temas son motores, cuáles básicos, cuáles nicho y cuáles
  emergentes.
- **Completo**: `palabras`, `coocurrencia` y `mapa_tematico`; y la evolución
  temática con `thematicEvolution` si el periodo da para partirlo.

Si el corpus vino de OpenAlex, esto se calculó sobre títulos y resúmenes, y se
declara.

## Paso 7 — La estructura intelectual

**Solo en el uso completo, y prescindible.** `cocitacion`, `coautoria` y
`colaboracion_paises`: qué trabajos sostienen el campo y qué grupos lo trabajan
por separado. Si viene agotado, se ofrece cerrar sin él.

## Paso 8 — El vacío

Lo que convierte el mapeo en algo útil para la tesis: **qué no se ha
estudiado**. El tema del cuadrante emergente que nadie desarrolla, la población
que no aparece, el país sin producción. En el uso breve, el vacío es el puente
con el problema de su tesis: se dice cómo su estudio lo atiende. **No se
inventa**: si las figuras no muestran un vacío claro, se dice y se plantea
como agenda.

## Paso 9 — Redactar y guardar

Redactar con las salidas delante y pasar el humanizador si lo pide. Las figuras
van en bloque, con el nombre del PNG tal como lo guardó `figura_bibliometrica`
—el Word lo incrusta solo—, y siguen la numeración de figuras que ya lleve el
capítulo:

```
**Figura 4**
*Producción científica anual sobre [tema], [periodo]*
[Insertar aquí la Figura 4: figura_produccion_anual.png]
*Nota.* Elaboración propia a partir de datos de Scopus, procesados con bibliometrix [ARxxxxxxxx].
```

Las figuras de bibliometrix rotulan en inglés («Motor Themes»): en el texto se
nombran en español.

**Uso breve.** Un subapartado al final de 2.1, con el número que le toque
(«### 2.1.4 Panorama bibliométrico del tema»), de tres a seis párrafos y sus
figuras. El capítulo guardado se reemplaza entero, así que:

1. Leer el `marco-teorico` guardado **entero**, todas sus partes.
2. Enseñarle dónde entra el subapartado y pedir su visto bueno.
3. Guardar el capítulo completo con el subapartado dentro: la primera parte
   sin `anadir`, las siguientes con `anadir: true`, cortando entre secciones.
4. Comprobar que las palabras que devuelve `guardar_capitulo` son las de antes
   más las nuevas. Si son menos, se perdió texto: se dice y se vuelve a guardar.

**Uso completo.** El capítulo de Resultados (`analisis-datos-rstudio`) con esta
estructura, adaptada a lo que se hizo:

- `## 4.1 Resultados de la búsqueda (PRISMA)`
- `## 4.2 Panorama del campo`
- `## 4.3 Estructura conceptual`
- `## 4.4 Estructura intelectual` (si se hizo)
- `## 4.5 Vacíos y agenda de investigación`

Antes de redactar, las cifras que van al texto se guardan con
`guardar_analisis` (`capitulo: "analisis-datos-rstudio"`, solo `resultados`,
sin `script` ni `salida`): así el repaso de la tesis las encuentra. Si pasa de
30.000 caracteres, por partes. Y `guardar_avance` en `analisis-datos-rstudio`
con el tamaño del corpus, la fecha de la búsqueda y las figuras incluidas.

Antes de entregar, `revisar_evidencia` sobre el capítulo guardado.

## Paso 10 — Cierre

Dar el enlace con `enlace_del_word`. Decirle qué se escribió, dónde quedó y qué
sigue: en el uso breve, volver a su capítulo; en el completo, la Metodología
con el protocolo del Paso 3, y después la Discusión.

Y una advertencia honesta: si vuelve a descargar el corpus más adelante, las
cifras cambiarán. Lo escrito corresponde a la búsqueda de esa fecha, y así se
declara.

## Errores que esta skill previene

- **Un corpus de cuarenta registros**: no produce mapas, produce ruido.
- **Exportar sin referencias ni palabras clave**: se descubre tarde y arruina
  las figuras que más aportan.
- **Pisar el marco teórico**: el capítulo se guarda entero; por eso se lee
  entero antes.
- **Describir en vez de interpretar**, y **afirmar causas**.
- **Olvidar citar bibliometrix**, que su licencia exige.

## Archivos de referencia

| Archivo | Cuándo se lee |
|---|---|
| `integracion_zotero.md` | Antes de citar por primera vez |
| `busqueda_bases.md` | Paso 2 — la ecuación |
| `openalex_vs_scopus.md` | Paso 2 — elegir carril |
| `criterios_prisma.md` | Paso 3 — inclusión, exclusión y el diagrama |
| `r_en_el_servidor.md` | Pasos 4 a 7 — el carril del servidor |
| `script_bibliometrix.R` | Pasos 4 a 7 — el carril de RStudio (OpenAlex) |
| `leer_las_figuras.md` | Pasos 5 a 7 — qué dice cada figura y qué no |
| `errores_comunes.md` | Paso 4 — cuando no carga |
