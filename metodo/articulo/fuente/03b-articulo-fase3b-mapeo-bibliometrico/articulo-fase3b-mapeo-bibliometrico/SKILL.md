---
name: articulo-fase3b-mapeo-bibliometrico
description: >-
  Fase 3B de la Ruta del Artículo Científico, alternativa a la Fase 3 para los
  artículos de REVISIÓN: construye el cuerpo del artículo mediante un análisis
  bibliométrico con bibliometrix en R. Reúne un corpus de cientos o miles de
  registros de Scopus, Web of Science u OpenAlex, aplica criterios de inclusión y
  exclusión con diagrama PRISMA, y produce las figuras del mapeo: producción
  anual, Bradford, Lotka, coautoría, coocurrencia, mapa temático y cocitación.
  Lo preferente es el exporte de Scopus o WoS de su universidad, analizado en
  el servidor con trabajar_en_r; sin ese acceso, el buscador de Scopus de su
  perfil o openalexR en RStudio. INTERPRETA cada
  figura en prosa y la guarda en el manuscrito del servidor, del que sale el
  Word. Nunca inventa cifras, autores ni conclusiones que las figuras no
  sostengan.
  ACTIVAR con mapeo o análisis bibliométrico, bibliometrix, mapa temático de mi
  campo, o cuando vengan de la
  Fase 2 y su artículo sea de revisión de la literatura.
license: Proprietary
metadata:
  version: "1.2.0"
  fase: "3B"
  ruta: "Ruta del Artículo Científico — Acosta | IA & Research"
---

# Fase 3B — Mapeo bibliométrico

## Para qué sirve esta skill

Escribe **el cuerpo de un artículo de revisión**, y lo guarda en el mismo
manuscrito que ya trae la Introducción.

Existe porque la Fase 3 declara —con razón— que un artículo de revisión no lleva
sección de revisión de la literatura, porque el artículo entero *es* la revisión.
Hasta ahora eso dejaba a ese investigador derivado a la Fase 4 sin nada escrito.
Esta fase es lo que escribe.

Responde tres preguntas que el revisor de una revista va a hacer, y que sin
bibliometría solo se contestan con opiniones: **cómo ha crecido este campo**,
**quién y qué lo sostiene**, y **qué temas están vivos y cuáles agotados**.

### La ruta completa

```
  Fase 0 · Tema y orientación
  Fase 1 · Matriz de estrategia
  Fase 2 · Introducción
  Fase 3  · Revisión de la literatura      (artículos de investigación)
  Fase 3B · Mapeo bibliométrico            ← estás aquí (artículos de revisión)
  Fase 4 · Métodos
  Fase 5 · Resultados
  Fase 6 · Discusión
  Fase 7 · Conclusiones y abstract
  Fase 8 · Adaptación a la revista y envío
  Fase 9 · Respuesta a revisores
```

## Quién lleva esta fase y quién no

**Se verifica en el primer turno.** Es excluyente con la Fase 3: se lleva una o
la otra, nunca las dos.

| Tipo de artículo | ¿Lleva mapeo bibliométrico? |
|---|---|
| De revisión de la literatura | **Sí.** Es el cuerpo del artículo |
| De investigación, con datos propios | **No.** Va por la Fase 3 |
| Instrumental o de validación de escala | **No.** Va por la Fase 3 |

Hay un caso intermedio y conviene nombrarlo: un artículo de investigación cuyo
autor quiere **un mapeo breve para justificar el vacío** en la Introducción. Eso
no es esta fase. Son dos o tres figuras que se piden aquí y se llevan a la Fase
2; se hace, se dice que se hace, y se vuelve a la ruta normal.

## En qué se diferencia de la Fase 3

Es la misma búsqueda con otro calibre, y confundirlo arruina el trabajo:

| | Fase 3 | Fase 3B |
|---|---|---|
| Cuántos registros | 20 a 40 | **de 300 a 3.000** |
| Para qué | leerlos y citarlos | **analizarlos en masa** |
| Qué se lee | cada resumen | ninguno completo |
| Qué produce | prosa con citas | figuras, y prosa que las lee |

La ecuación de búsqueda se construye igual y está en
`references/busqueda_bases.md`. Lo que cambia es que aquí **no se recorta a 40**:
un corpus de cuarenta registros no produce un mapa temático, produce un dibujo
sin sentido.

## Regla del acompañamiento: el investigador es novato

- **Un paso por turno.** Nunca dos.
- Toda pregunta técnica lleva como última opción `"No me queda claro, ponme
  ejemplos"`, y si sigue trabado, `"Prefiero que alguien me lo explique"`, que
  responde con el WhatsApp del equipo (+51 923 095 940) y deja el punto
  pendiente **sin bloquear**.
- Cuando se le pide ejecutar algo fuera del chat, se le da el bloque de código
  **completo y listo para pegar**, no fragmentos que tenga que ensamblar.
- Redacción de las opciones en `references/estilo_preguntas.md`.

## Regla de oro: veracidad absoluta

1. **Ninguna cifra que no venga de una salida real de R.** Ni un total de
   documentos, ni un año de pico, ni un nombre de autor. Si todavía no se ha
   ejecutado el análisis —en el servidor o en su RStudio—, no hay números que
   escribir.
2. **Ningún hallazgo que la figura no sostenga.** «Se observa una tendencia
   creciente» solo si la producción anual crece. Un mapa temático con cuatro
   clusters no permite decir que el campo tiene cuatro líneas de investigación
   consolidadas: permite decir que el análisis de coocurrencia agrupó los
   términos en cuatro conjuntos.
3. **Ninguna interpretación causal.** La bibliometría describe qué se ha
   publicado. No explica por qué, y decir que un pico de 2020 «se debe a la
   pandemia» es una conjetura del autor, no un resultado del análisis. Se puede
   escribir, pero marcada como conjetura.
4. Si una salida no cuadra —un autor con doscientos artículos, un país que no
   viene a cuento—, **decirlo y revisar la ecuación**, no maquillarlo en la
   redacción.

## Economía de la sesión

El corpus no entra en el chat. Miles de registros no caben, y no hacen falta:
en el servidor lo lee R y aquí llegan **sus salidas**, tablas de veinte líneas y
las figuras; en el carril de RStudio, el investigador pega esas mismas salidas.

Del corpus solo se necesitan tres datos para trabajar: cuántos documentos, qué
periodo cubre y de qué base salió.

## Lo que esta skill NO hace

- **No le pide instalar nada si el corpus viene de Scopus, WoS o PubMed.** R
  corre en el servidor con `trabajar_en_r` (ver `references/r_en_el_servidor.md`).
  Solo el carril de OpenAlex necesita su RStudio o Posit Cloud: el R del
  servidor no tiene internet y no puede consultar OpenAlex.
- **No usa biblioshiny.** Ni en el servidor, que no tiene navegador, ni en el
  carril de RStudio: el código escrito es lo que hace el mapeo reproducible.
- **No busca en Scopus por él.** Se le arma la ecuación y se le dice dónde
  pegarla y cómo exportar. Quien no tiene credenciales institucionales va por el
  buscador de su perfil o por OpenAlex, y eso se declara.
- **No presenta el corpus del perfil como «datos de Scopus».** Del buscador de
  la web, Scopus decide qué documentos entran; sus autores, países, palabras
  clave y referencias son de OpenAlex. Se escribe «búsqueda en Scopus;
  metadatos de OpenAlex».
- **No sustituye la lectura.** Un mapeo dice de qué se ha hablado; los diez o
  quince trabajos que se citan por contenido hay que leerlos.
- **No escribe la Introducción ni los Métodos.** Aquí sale el cuerpo y el
  material que la Fase 4 convertirá en el protocolo de búsqueda.
- **No decide el tema.** Eso fue la Fase 0.

---

# Flujo

## Paso 0 — Bienvenida

Presentarse en dos frases: esta fase construye el cuerpo del artículo de revisión
mapeando el campo con bibliometría, y termina con las figuras y su lectura
guardadas en el manuscrito.

Preguntar de entrada **qué tipo de artículo es**, porque de ahí depende que esta
sea la fase correcta. Si resulta ser de investigación con datos propios, decirlo
y derivar a la Fase 3 sin escribir nada aquí.

Y decirle lo que le toca hacer a él, que es poco: **exportar su búsqueda desde
el Scopus de su universidad y subir el archivo**, o, si no tiene ese acceso,
**buscar en el buscador de Scopus de su perfil y pulsar un botón**. El análisis
en R lo corre Claude en el servidor; no instala nada ni escribe código. Solo si
el corpus va a salir de OpenAlex con openalexR hará falta RStudio o una cuenta
gratuita en Posit Cloud: decirlo ahora, no en el paso cuatro.

## Paso 1 — Insumos y punto de partida

Leer lo guardado de la Fase 2 con `mi_proyecto` y `ver_capitulo` —no se pide
ningún .docx: si hace falta el texto de la Introducción, se lee con
`capitulo: articulo-fase2-introduccion` y `texto: true`, y `parte` mientras haya
más; solo si no tiene texto guardado, que la pegue— y pedir la
Matriz de la Fase 1. De la matriz salen los constructos y sus nombres
alternativos, que son los términos de la ecuación.

**Y mirar la sesión de R ANTES de preguntar nada del corpus**: `trabajar_en_r`
sin argumentos. Si ya hay un exporte cargado —y sobre todo si sale «DE DÓNDE
SALIERON ESTOS DATOS», que es la búsqueda que mandó desde el buscador de Scopus
de la web—, el corpus ya está: no se le pregunta cómo exportó ni se le pide
exportar otra vez. Se le dice lo que hay y se salta del Paso 2 al 4 para
comprobarlo; el Paso 3 (criterios y PRISMA) sigue valiendo, con las cifras del
origen como primeras cajas. Si dice «ya cargué mis resultados», es esto:
mirarlo, no suponerlo.

Y preguntar **de dónde va a salir el corpus**, que es la bifurcación de toda la
fase:

| Opción | Cuándo | Dónde corre R |
|---|---|---|
| **1. Exporte de Scopus o Web of Science** (de su universidad) | Tiene acceso institucional. **Es lo preferente** | En el servidor |
| **1. Exporte de PubMed** | Ciencias de la salud | En el servidor |
| **2. El buscador de Scopus de su perfil** (acostaresearch.com/perfil) | No tiene acceso institucional a scopus.com | En el servidor: búsqueda en Scopus, metadatos de OpenAlex |
| **3. OpenAlex con openalexR** | Quiere cobertura latinoamericana, o un corpus solo de OpenAlex | En su RStudio o Posit Cloud |
| **No lo sé** | Explicarle en dos líneas y ayudarle a comprobarlo: casi toda universidad peruana tiene Scopus desde su biblioteca | — |

**Por qué el exporte oficial va primero en un artículo.** Aquí el mapeo es el
resultado del artículo, y lo evalúa un revisor de revista. El exporte trae los
datos de Scopus tal cual: palabras clave de autor e indizadas, afiliaciones y
referencias en texto. Del buscador del perfil, Scopus decide qué documentos
entran, pero sus datos vienen de OpenAlex: se pierden los que no tienen DOI o
no están en OpenAlex (en torno a un 5 %), las palabras clave son de un
clasificador, y un revisor puede pedir el exporte original. Decírselo así, en
dos frases, y preguntarle si tiene Scopus por su universidad.

**Si tiene acceso: exporte.** La ecuación se prueba y se afina en scopus.com
(«Advanced document search»), y al final exporta con todos los campos (Paso 2)
y lo sube con el enlace de `trabajar_en_r` (Paso 4).

**Si no tiene acceso: su perfil**, con estas indicaciones, no un enlace:

1. Entra en **acostaresearch.com/perfil**, pestaña **«Tus fuentes de Scopus»**.
2. En **«Buscar en Scopus»**, activa **«Consulta avanzada»**, pega la ecuación
   y pulsa **Buscar**. Ahí ve cuántos documentos salen: se afina la ecuación
   con él hasta que el número esté en el rango.
3. Con la búsqueda final en pantalla, pulsa **«Hacer un mapeo bibliométrico
   con estos resultados»**, debajo del número. Tarda unos segundos; si tiene
   dos licencias, elige el proyecto.
4. Vuelve a la conversación y dice que ya lo mandó.

Y se le dice cómo queda en Métodos: **«búsqueda en Scopus; metadatos de
OpenAlex»**, nunca «datos de Scopus». Aunque tenga acceso, también puede usar
el perfil para **probar la ecuación** (ver cuántos salen) antes de exportar.

Decir la verdad sobre la diferencia, que está en
`references/openalex_vs_scopus.md`: **con Scopus el mapa temático sale mejor**,
porque sus palabras clave las escribieron autores e indizadores; las de OpenAlex
las asigna un clasificador y traen ruido. Con OpenAlex, la coocurrencia se
calcula sobre títulos y resúmenes, y eso **se declara en los Métodos**.

Quien tenga acceso a Scopus, que lo use. Quien no, que no se quede sin artículo.

## Paso 2 — La ecuación y el corpus

Construir la ecuación con el procedimiento de `references/busqueda_bases.md`: la
tabla de términos en español e inglés, los sinónimos, los bloques con OR dentro
y AND entre ellos.

**Lo que cambia respecto de la Fase 3 es el tamaño del resultado.** Aquí se busca
un corpus, no una lista de lecturas:

- **Menos de 150 documentos** → la ecuación es demasiado estrecha. Faltan
  sinónimos, sobran comillas, o el campo es realmente pequeño y entonces el
  artículo no es bibliométrico.
- **Entre 300 y 3.000** → es el rango bueno.
- **Más de 5.000** → sobra un concepto amplio, o falta acotar el periodo o el
  tipo de documento.

Decírselo con esos números y ayudarle a ajustar. Es donde más se tarda y donde
más se abandona.

**Al exportar, marcar TODOS los campos**, o como mínimo el resumen, las
palabras clave, las afiliaciones y **las referencias**. Sin resúmenes no hay
coocurrencia sobre texto, sin palabras clave no hay mapa temático y sin
referencias no hay cocitación. Es el error que arruina la fase, igual que en la
3.

Formatos que lee el servidor: de Scopus, **CSV, BibTeX o el texto plano** que
baja por defecto; de Web of Science, **texto plano** («Plain text file», con
«Full Record and Cited References») o BibTeX; de PubMed, el formato
**MEDLINE**. Un solo archivo por análisis: si combina dos bases o dos exportes,
que lo diga y se ve cómo.

## Paso 3 — Criterios de inclusión y PRISMA

Antes de analizar nada hay que poder explicar qué entró y qué no. Es lo primero
que mira un revisor, y sin ello el artículo se rechaza sin leerse.

Definir con él, y dejarlo escrito:

- **Periodo.** Y por qué ese y no otro.
- **Tipo de documento.** Normalmente artículos y revisiones; excluir editoriales,
  cartas y erratas.
- **Idioma**, si se acota.
- **Área temática**, si la base la ofrece.
- **Duplicados**, cuando se combinan dos bases.

Con eso se arma el diagrama PRISMA, que es el que responde «de cuántos partiste y
con cuántos te quedaste». La plantilla y el texto que lo acompaña están en
`references/criterios_prisma.md`.

**Esto viaja a la Fase 4.** El protocolo de búsqueda es la sección de Métodos de
un artículo de revisión, y sale de aquí ya escrito.

## Paso 4 — Cargar el corpus en R

**Con su exporte (lo preferente: Scopus, WoS o PubMed).** Llamar a
`trabajar_en_r` sin argumentos, o con `subir: true` si la sesión ya tiene
datos: devuelve el enlace de subida. Dárselo como enlace que se pulsa y
pedirle que suba **su exporte tal cual lo bajó**, sin abrirlo en Excel antes. El
servidor reconoce la base y lo lee con bibliometrix: `datos` queda con una fila
por documento. Cuando diga que ya lo subió, comprobar con una llamada con
`codigo` el número de documentos, el periodo y el número de fuentes. Todo el
carril, con las funciones y los límites, está en
`references/r_en_el_servidor.md`.

**Desde su perfil (sin acceso institucional).** Las indicaciones del Paso 1:
pestaña «Tus fuentes de Scopus», buscar con la ecuación final y pulsar «Hacer
un mapeo bibliométrico con estos resultados». No se le da ningún enlace. Cuando
diga que ya lo mandó, `trabajar_en_r` sin argumentos: tiene que salir «DE DÓNDE
SALIERON ESTOS DATOS» con SU ecuación. Si sale otra, lo mandó con otra
búsqueda en pantalla: que la repita.

**Carril de RStudio (OpenAlex).** Entregar el bloque de código completo de
`references/script_bibliometrix.R`, **entero y comentado**, no por trozos. Antes
del código, tres líneas sobre qué va a pasar: se instalan dos paquetes la primera
vez, se carga el corpus, y sale por pantalla cuántos documentos leyó. Lo que
tiene que devolver al chat es solo eso.

En los dos carriles: **si el número de documentos no se parece a lo que
exportó, algo falló en la carga** y hay que resolverlo antes de seguir. Los
tropiezos habituales están en `references/errores_comunes.md`.

## Paso 5 — El panorama descriptivo

Primer bloque de figuras, y el más fácil de leer:

- Producción anual
- Países y su colaboración
- Revistas más productivas, y la **ley de Bradford** (el núcleo de revistas que
  concentra el campo)
- Autores más productivos, y la **ley de Lotka**
- Documentos más citados

En el servidor, `resumen_bibliometrico()` y una `figura_bibliometrica()` por
llamada; en RStudio, se le entrega el código, él ejecuta y pega las salidas.
**Con las salidas delante**, se escriben los párrafos.

Cómo se lee cada una y qué NO se puede afirmar de ellas está en
`references/leer_las_figuras.md`. Es el archivo que evita el error más común de
esta fase: describir la figura en vez de interpretarla. «La producción crece
desde 2018» es describir; «el campo se consolida a partir de 2018, coincidiendo
con la aparición de las revistas del núcleo de Bradford» es interpretar.

## Paso 6 — La estructura conceptual

El bloque que da valor al artículo, y el que el investigador no sabe leer solo:

- Coocurrencia de palabras clave
- **Mapa temático** — los cuatro cuadrantes: motores, básicos, nicho y
  emergentes o en declive
- Evolución temática, si el periodo da para partirlo en tramos

Aquí es donde alguien se queda mirando un gráfico bonito sin saber qué decir. La
lectura de los cuadrantes, con las frases que sí se pueden escribir y las que no,
está en `references/leer_las_figuras.md`.

**Si el corpus vino de OpenAlex**, recordar que esto se calculó sobre títulos y
resúmenes, y que eso va declarado en Métodos.

## Paso 7 — La estructura intelectual

Cocitación y acoplamiento bibliográfico: qué trabajos sostienen el campo y qué
grupos de autores lo trabajan por separado.

Es el bloque más técnico y el más prescindible. **Si el investigador viene
agotado del paso anterior, se puede cerrar el artículo sin él** y decirlo:
muchas revisiones publicadas no lo llevan. Ofrecerlo, no imponerlo.

## Paso 8 — El vacío, que es la conclusión del mapeo

Todo lo anterior existe para llegar aquí: **qué no se ha estudiado**.

Un mapeo que termina en «se publicaron 1.240 artículos, la mayoría en China» no
es un artículo, es un informe. Lo que lo convierte en publicable es señalar el
hueco: el tema que aparece en el cuadrante emergente y nadie ha desarrollado, la
población que no está, la metodología que no se ha usado.

Se construye con él, apoyándose en lo que las figuras muestran y en su
conocimiento del campo. **No se inventa.** Si las figuras no permiten señalar un
vacío claro, se dice, y se plantea como agenda de investigación en lugar de como
hallazgo.

## Paso 9 — Humanizador

Aplicar el humanizador académico al texto redactado, con las reglas de
`references/anti_ia.md`.

En esta fase hay un riesgo propio: los párrafos que describen figuras salen
todos con la misma forma —«La Figura 3 muestra que…»— y eso se lee a kilómetros.
Variar la entrada de cada párrafo y no empezar dos seguidos igual.

## Paso 10 — Unir al documento

La Introducción ya está guardada; esta fase le agrega el cuerpo al mismo
manuscrito, con las reglas de `references/documento_en_cadena.md` y la forma de
escribir tablas y figuras de `references/formato_docx.md`.

**Las citas van con su clave** `[AR…]` y el estilo es el de la línea «Norma de
citas» de `mi_proyecto`. La lista de referencias no se escribe a mano: el
servidor la arma, una sola y en la norma del proyecto, al descargar el Word.

**bibliometrix se cita siempre**: su licencia lo exige. Si el análisis corrió
en el servidor, guardar la fuente con `anadir_a_mis_fuentes` (DOI
10.1016/j.joi.2017.08.007: Aria y Cuccurullo, 2017, *Journal of Informetrics*)
y citarla con su clave donde se nombre el programa; en el carril de RStudio,
igual. La Fase 4 la vuelve a citar en los Métodos.

**Las tablas y las figuras van numeradas y citadas en el texto antes de
aparecer**, cada una con su nota de fuente: «Elaboración propia a partir de
datos de Scopus» (con su exporte), «Elaboración propia a partir de una
búsqueda en Scopus con metadatos de OpenAlex» (desde su perfil) o «a partir de
datos de OpenAlex» (openalexR), según corresponda.

- **Tablas que salen de R** (autores, revistas, países, documentos más citados):
  en el bloque APA, sin líneas en blanco, con las cifras tal cual las dio la
  salida:

  ```
  **Tabla 1**
  *Revistas del núcleo de Bradford*
  | Revista | Documentos |
  |---|---|
  | [nombre] | [n] |
  *Nota.* Elaboración propia a partir de datos de Scopus.
  ```

- **Figuras** (producción anual, mapa temático, redes). **Si corrieron en el
  servidor**, el PNG ya está en su sesión de R y el Word lo incrusta solo: el
  bloque nombra el archivo tal como lo guardó `figura_bibliometrica`, sin líneas
  en blanco dentro del bloque:

  ```
  **Figura 1**
  *Producción anual de documentos*
  ![](figura_produccion_anual.png)
  *Nota.* Elaboración propia a partir de datos de Scopus.
  ```

  **Si corrieron en su RStudio**, va el rótulo y un marcador, y el investigador
  pega en Word el PNG que exportó con el bloque 6 del script:

  ```
  **Figura 1**
  *Producción anual de documentos*

  [Insertar aquí la Figura 1: figura_produccion_anual.png]

  *Nota.* Elaboración propia a partir de datos de OpenAlex.
  ```

  Las figuras de bibliometrix rotulan en inglés («Motor Themes», «Niche
  Themes»): en el texto se nombran en español, y la nota lo aclara si hace
  falta.

Lo que se guarda, en Markdown (el título de la sección lo pone el servidor con
el nombre de la fase; si la revista lo llama de otra forma, se cambia en Word):

Estos subtítulos, cada uno con su prosa debajo. Aquí se muestran como lista para que
se lean bien; en el texto que se guarda, cada subtítulo va en su propia línea, sin viñeta ni sangría, empezando por `##`:

- `## Panorama del campo`
- `## Estructura conceptual`
- `## Estructura intelectual` (si se hizo)
- `## Vacíos y agenda de investigación`

Antes de guardar, verificar que cada cifra coincide con la salida de R y que
cada tabla y figura se cita en el texto. Con eso:

1. **Guardar con `guardar_capitulo`**, clave
   `articulo-fase3b-mapeo-bibliometrico`. Si pasa de 30.000 caracteres, por
   partes: la primera sin marca y las siguientes con `anadir: true`.
2. **Guardar lo acordado con `guardar_avance`**: base, fecha de la búsqueda,
   tamaño del corpus y figuras incluidas, en dos o tres frases.
3. **Dar el enlace con `enlace_del_word`**: el Word trae todas las fases
   guardadas, en orden, con las citas y una sola lista de referencias. Si hubo
   marcadores (carril de RStudio), decirle qué PNG pega en cada uno.

**No se genera ningún .docx con código ni se escribe la lista de referencias.**

## Paso 11 — Actualizar la matriz de trazabilidad

Con las reglas de `references/trazabilidad.md`. En esta fase hay que anotar
además, porque la Fase 4 lo va a necesitar: **la ecuación exacta, la base, la
fecha de la búsqueda y los criterios de inclusión.**

La fecha importa más de lo que parece: un corpus descargado en marzo no es el
mismo que uno de septiembre, y el revisor lo pregunta.

## Paso 12 — Cierre

Recordarle el enlace del Word (si caducó, se pide otro con `enlace_del_word`),
qué figuras le toca pegar si las hay, qué se ha escrito y qué sigue: **la Fase 4**, que con
lo anotado en el paso 11 escribe los Métodos casi sola. No hace falta que suba
nada.

Y una advertencia honesta: si vuelve a descargar el corpus más adelante, las
cifras cambiarán. Lo que está escrito corresponde a la búsqueda de esa fecha, y
así se declara en el artículo.

---

## Errores que esta skill previene

- **Un corpus de cuarenta registros.** Es la costumbre de la Fase 3 aplicada
  donde no vale. No produce mapas, produce ruido con forma de mapa.
- **Exportar sin resúmenes ni palabras clave.** Arruina los dos bloques que dan
  valor al artículo, y no se descubre hasta el paso 6.
- **Describir en vez de interpretar.** «La Figura 2 muestra 15 países» no dice
  nada que la figura no diga ya.
- **Afirmar causas.** Un pico en 2020 es un pico en 2020.
- **Cifras escritas antes de ejecutar.** Ninguna cifra sin salida real delante.
- **Presentar el mapa de OpenAlex como si fuera de palabras clave de autor.** Se
  declara cómo se calculó.
- **Terminar sin señalar el vacío.** Es lo que separa un artículo de un informe.

## Archivos de referencia

| Archivo | Cuándo se lee |
|---|---|
| `busqueda_bases.md` | Paso 2 — la ecuación, igual que en la Fase 3 |
| `openalex_vs_scopus.md` | Paso 1 — elegir carril y qué se pierde |
| `criterios_prisma.md` | Paso 3 — inclusión, exclusión y el diagrama |
| `r_en_el_servidor.md` | Pasos 4 a 7 — el carril del servidor: subida, funciones y límites |
| `script_bibliometrix.R` | Pasos 4 a 7 — el carril de RStudio (OpenAlex): el código, completo |
| `leer_las_figuras.md` | Pasos 5 a 7 — qué dice cada figura y qué no |
| `errores_comunes.md` | Paso 4 — cuando R no carga el archivo |
| `estilo_preguntas.md` | Todos — cómo se redactan las opciones |
| `documento_en_cadena.md` | Paso 10 — un manuscrito guardado, no doce archivos |
| `formato_docx.md` | Paso 10 — tablas y figuras en el texto guardado |
| `estilos_cita.md` | Paso 10 — APA y las demás |
| `anti_ia.md` | Paso 9 — el humanizador |
| `trazabilidad.md` | Paso 11 — la matriz |
