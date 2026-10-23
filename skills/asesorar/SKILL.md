---
name: asesorar
description: Atiende a los clientes de asesoría de la carpeta tesis-asesorar del usuario. Primero cotiza, leyendo sola el avance del cliente y la guía de su universidad, comparándolos, comprobando las referencias y devolviendo diagnóstico, precio según lo que necesita, plazo y el mensaje de WhatsApp. Cuando el cliente paga, hace el trabajo en local con el método de las skills de Acosta | IA & Research (tesis, TSP, informe, artículo, revisión) y deja el Word corregido, la versión para Turnitin y el informe de revisión. Úsala cuando el usuario escriba /asesorar, pegue un chat de WhatsApp de alguien que pide que le hagan o le revisen la tesis, diga «cotiza», «cuánto le cobro», «los archivos están en la carpeta», «ya pagó», «empieza con el de…», «llegaron sus respuestas», o nombre una subcarpeta de tesis-asesorar, aunque no diga la palabra asesoría.
---

# Asesorar: cotizar y hacer el trabajo desde la carpeta

Benicio recibe por WhatsApp a personas que quieren que les hagan, corrijan o terminen su
tesis, proyecto, TSP, informe o artículo. Guarda lo que le mandan en una carpeta por cliente y
necesita dos cosas, en este orden: **cuánto cobrar y en cuánto tiempo**, y después **el trabajo
hecho**. Entre una y otra está el pago: no se redacta nada antes de que él diga que pagaron.

Quiere rapidez. Se trabaja de corrido, sin pedirle aprobación por sección, y se le informa al
final. Se le responde siempre en español.

## Rutas (leer primero)

Este texto no lleva rutas de una máquina concreta; usa tres nombres que se resuelven así:

- `<SKILLS>`: la carpeta de skills del usuario, `~/.claude/skills` (la `~` es su carpeta personal:
  al ejecutar un comando se escribe la ruta completa).
- `<TURNITIN>` y `<ASESORAR>`: las carpetas `tesis-turnitin` y `tesis-asesorar` de los clientes.
- `<METODO>`: la carpeta con las skills del método (`tesis`, `tsp`, `informe`, `articulo`, `revision`,
  cada una con su `fuente\`).

Las tres últimas salen de `<SKILLS>/rutas-acosta.json` (lo crea `instalar.py` del repositorio) o de las
variables de entorno `ACOSTA_TURNITIN`, `ACOSTA_ASESORAR` y `ACOSTA_METODO`. Para ver cuáles son en
esta máquina: `python <SKILLS>/turnitin/scripts/rutas.py`. Si una no existe, se le pregunta al
usuario dónde la tiene y se corrige el json; no se inventa otra.

## La carpeta

```
<ASESORAR>\
└── 11-Edheliza Cardenas Juarez - 929365434\   una por cliente: número de orden, nombre completo y WhatsApp
    ├── cotizacion.md           diagnóstico, precio, plazo, mensaje y estado. Lo escribe la skill.
    ├── 01-original\            lo que mandó el cliente. No se modifica nunca.
    ├── 02-corregida\           el Word trabajado
    ├── 03-turnitin\            la versión sin carátula ni anexos, lista para pasar
    ├── 04-revision\            el informe de revisión y las preguntas para el cliente
    ├── 05-pasadoporturnitin\   los reportes, que coloca él
    ├── 06-enviar\              todo lo que se le manda al cliente, junto y listo para adjuntar
    └── borrar\                 lo que quedó obsoleto. Se crea solo cuando hace falta.
```

### El nombre de la carpeta es el nombre completo del cliente

La subcarpeta de cada cliente se llama con su nombre completo, todos los nombres y los dos
apellidos, tal como figura en la carátula de su trabajo (`Elisai Galarreta Ruiz`), y no
con el apodo de WhatsApp ni con un nombre suelto (lo pidió Benicio el 14-oct-2026: así el
registro queda por persona y se encuentra igual desde `/turnitin`, cuyas carpetas siguen la
misma regla con un número delante). Con dos autores van los dos unidos por «y»
(`Analiz Curasma Solano y Karen Garcia Sanchez`). Si hay tilde en el nombre, se escribe con
tilde.

Delante del nombre va un número de orden de dos cifras, como en `tesis-turnitin`
(`11-Edheliza Cardenas Juarez - 929365434`): lo pidió Benicio el 17-oct-2026 y ese día se
numeraron las quince carpetas por fecha de creación. Una carpeta nueva lleva el siguiente número
libre; `nombrar.py` se lo pone solo si falta, y nunca se renumeran las que ya lo tienen.

Detrás del nombre va el número de WhatsApp del cliente, separado por « - »:
`Edheliza Cardenas Juarez - 929365434` (lo pidió Benicio el 17-oct-2026, para encontrar el chat
desde la carpeta). Va sin espacios y sin el +51 de Perú; si el cliente es de otro país, se deja su
código (`Lucía Pérez Gómez - 593987654321`). El número sale del encabezado del chat o de la captura
de WhatsApp y se escribe siempre en la línea «Cliente:» de `cotizacion.md` (`+51 929 365 434`),
que es de donde lo toma `nombrar.py`. Si la captura no muestra el número (el contacto está
guardado con nombre), se le pide a Benicio en la cotización y la carpeta se renombra cuando lo dé.

Benicio suele crear la carpeta con lo primero que sabe («Luna», «renzo», «cambiarnombre»).
Al cotizar, en cuanto la carátula o el chat dan el nombre completo, se escribe en la línea
«Cliente:» de `cotizacion.md` y se renombra la carpeta con el script de la skill `/turnitin`,
que lee esa línea (y, si no la hay, la carátula del Word):

```
python <SKILLS>/turnitin/scripts/nombrar.py "asesorar\Luna" --forzar
```

`--ver` enseña el nombre que pondría sin renombrar. En la línea «Cliente:» el nombre va solo y seguido de « · » (`Cliente: Nestor Carlos Sifuentes Zavaleta · Ingeniería…`): con una coma y una nota detrás («, WhatsApp sin número visible»), `nombrar.py` metió la nota en el nombre de la carpeta (21-oct-2026). Se corre siempre `--ver` antes de `--forzar`. Una carpeta que ya tiene el nombre completo
pero no el número se renombra sin `--forzar`. Si el nombre completo no se conoce todavía
(`Julio`, `Dayra`), la carpeta se queda con lo que hay y en `cotizacion.md` se apunta como
pregunta para el cliente; se renombra cuando conteste. En el informe a Benicio se dice en una
línea cómo quedó la carpeta. Las referencias de la memoria y de `cotizacion.md` usan desde
entonces el nombre nuevo.

### La carpeta `borrar`

En las carpetas de trabajo (`02`, `03`, `04`) queda **solo la versión válida** de cada archivo,
con su nombre limpio, sin «v2» ni «final». Cuando una versión nueva reemplaza a otra (un
cambio que pidió Benicio, las respuestas del cliente, una ronda de observaciones), la anterior
no se sobrescribe ni se borra: se **mueve** a `borrar\` dentro de la carpeta del cliente, con
una nota entre paréntesis en el nombre que diga por qué quedó atrás («(título cambiado)»,
«(antes de las respuestas)»), y la nueva ocupa su lugar con el nombre de siempre. Lo mismo con
el Word y el PDF de `03-turnitin` y con el informe, si cambiaron.

Si el archivo viejo está abierto en Word y no se deja mover, la nueva se guarda al lado con
« v2», se le pide a Benicio que cierre el Word y, en cuanto se pueda, se mueve la vieja a
`borrar\` y se le quita el « v2» a la buena.

**Al final de cada trabajo o ronda**, si `borrar\` tiene algo, se le pregunta con
AskUserQuestion: «¿Borro la carpeta borrar de <cliente>?», listando lo que contiene. Solo si
dice que sí se elimina la carpeta entera; si dice que no, se queda y se vuelve a preguntar al
cierre de la ronda siguiente. Nunca se borra sin preguntar, y nunca entra en `borrar\` nada de
`01-original` ni de `05-pasadoporturnitin`: lo que mandó el cliente y los reportes no son
obsoletos.

### La carpeta `06-enviar`

Benicio no quiere ir carpeta por carpeta buscando qué adjuntar (lo pidió el 13-oct-2026, con
Elisai Galarreta). Todo lo que se le manda al cliente va **copiado** en `06-enviar\`, y solo
eso: el Word completo de `02-corregida` y su PDF, los archivos que la universidad pide aparte
(matriz de consistencia, instrumentos, Excel), el informe de revisión y los reportes de
Turnitin que valen como resultado, con nombre claro (`Reporte_Turnitin_IA_0.pdf`,
`Reporte_Turnitin_similitud_17.pdf`). No entra la versión recortada de `03-turnitin`, ni
reportes de rondas anteriores, ni un reporte de similitud sacado con filtros distintos de los
que pide la universidad.

Son copias: los originales siguen en sus carpetas de trabajo. La carpeta se rehace cada vez que
cambia un entregable (se vacía y se vuelve a llenar, para que no quede una versión vieja al
lado de la nueva; no pasa por `borrar\` porque no guarda nada propio) y se crea desde la
primera entrega, aunque todavía falte el reporte. En el informe a Benicio se lista lo que
contiene y se dice qué falta para que esté completa.

Al cotizar, los archivos suelen estar sueltos en la carpeta del cliente: se leen ahí, sin
moverlos. Las subcarpetas se crean recién en la etapa 2, y es entonces cuando lo que mandó el
cliente se mueve a `01-original` (mover, no copiar; no se borra nada). Las carpetas viejas
tienen otros nombres (`02-reformulada`, `TESIS UCV - RENZO`): se respetan.

`<skill>` es `<SKILLS>/asesorar`. Los archivos de paso (volcados de
texto, JSON de cambios) van al scratchpad, nunca a la carpeta del cliente.

## Paso 0: qué carpeta y en qué etapa

```
python <skill>/scripts/estado.py                lista de clientes y en qué va cada uno
python <skill>/scripts/estado.py CURASMA        archivos de ese cliente, clasificados
```

Si el usuario no dijo qué cliente, se le pregunta con AskUserQuestion ofreciendo las carpetas
más recientes. Si lo dijo, o pegó una ruta, no se pregunta nada.

La etapa la decide `cotizacion.md`:

- **No existe** → etapa 1, cotizar (si falta la guía, primero se pide; ver 1.1).
- **Existe con `Estado: falta la guía`** → se espera la guía. Cuando llegue, se lee y se
  termina la cotización sobre el diagnóstico que ya está.
- **Existe con `Estado: cotizado`** → se espera el pago. Si el usuario dice «ya pagó»,
  «empieza», «hazlo», se cambia a `Estado: pagado` con la fecha y el monto, y se pasa a la
  etapa 2. Si dice que el cliente regateó o cambió lo que pide, se rehace la cotización.
- **Existe con `Estado: pagado` o `en trabajo`** → etapa 2, se retoma donde quedó.
- **`Estado: entregado`** → solo rondas: respuestas del cliente, observaciones del asesor o
  un reporte nuevo.

El chat de WhatsApp que el usuario pegue (texto o captura) se lee entero antes de nada: de ahí
salen la fecha de entrega, la carrera, la universidad y lo que el cliente dice querer. Las
fechas relativas («el miércoles», «la otra semana») se convierten a fecha exacta.

Los audios de WhatsApp (`.ogg`) que estén en la carpeta se transcriben siempre, porque traen
pedidos que no salen en el texto (con Luna, el 12-oct-2026, «la profesora pide fuentes desde
2022»). Hay `faster-whisper` pero su `av` no abre archivos: se convierte cada audio con
`ffmpeg -i a.ogg -ar 16000 -ac 1 -f f32le a.raw` y se le pasa a `WhisperModel("small")` como
`numpy.fromfile(..., float32)` con `language="es"`. Los videos (`.mp4`) se transcriben igual,
sacando el audio con el mismo `ffmpeg`.

Cuando la asesora ya revisó una versión, solo se le hacen los cambios que pidió, aunque una guía
general diga otra cosa. Con Diana Silva (18-oct-2026), quitar los subtítulos según la guía de
maestría hizo que la asesora rechazara el trabajo y que la IA subiera al 33 %: hubo que volver
a la versión anterior. Si la guía choca con lo que pide la asesora, se le pregunta a Benicio
antes de tocar el texto.

Si el asesor manda su «plantilla esquematizada» (subtítulos en colores con indicaciones), el
documento se reordena con esos subtítulos, sin el texto de las indicaciones, y el índice se hace
como el de la plantilla: si ella solo lista los títulos de nivel 1, los subtítulos van en negrita
sin nivel de esquema. Cuando piden los Excel «en captura» para los anexos (para que no cuenten en
Turnitin), la captura se saca con Excel por COM: `Range.CopyPicture(1,2)`, pegar en un
`ChartObject` y `Chart.Export` a PNG (`PageSetup` falla si no hay impresora). Las filas de modelo
de la plantilla se recortan de la imagen y no se ocultan, porque al ocultarlas Excel baja la
resolución. Cada captura entra como figura con rótulo APA y se dimensiona por la altura para que el
rótulo, la imagen y la nota quepan en una hoja (Luna, 14-oct-2026).

La guía de posgrado de la UCV (PP-G-02.03, 2026) pide la Introducción y la Metodología «sin
subtítulos, sin viñetas, sin negrita» y, tras la carátula, las dos declaratorias (del asesor y de
originalidad), que van en el índice. Pero manda lo que pida el asesor del programa: si su plantilla
o su revisión dicen otra cosa, se sigue al asesor y se le avisa a Benicio del choque. A Diana Silva
se le quitaron los subtítulos el 16-oct y la asesora rechazó esa versión el 18-oct. Las matrices
de los anexos van en imagen, porque la UCV pasa la tesis entera por Turnitin. Las tesis no se
citan como antecedentes ni como referencias si el asesor lo prohíbe («prohibido tesis»): se
reemplazan por artículos con DOI.

La guía de tesis de la UTP (formato general, p. 78) pide Arial 11 a doble espacio, márgenes de 3 cm (izquierdo e inferior) y 2,5 cm (derecho y superior), párrafos al margen, RESUMEN, INTRODUCCIÓN, CONCLUSIONES y BIBLIOGRAFÍA en la línea 8 (centrados, mayúsculas, negrita y subrayado), «CAPÍTULO 1» en arábigos en la línea 6 y su título en la línea 8, subtítulos numerados en negrita y subrayados, la bibliografía a espacio simple con cuatro líneas simples tras el título, la introducción en romanos y el texto en arábigos desde el Capítulo 1, con el número abajo a la derecha. Las «líneas» se cuentan como las cuenta el tesista: párrafos vacíos a doble espacio delante del título. `scripts/formato_utp.py <entrada> <salida>` lo aplica a un Word con capítulos «CAPÍTULO I» + salto de línea + título, y después va `indice.ps1` (Soledad Sonco y Karol Mamani, 18-oct-2026: la clienta lo reclamó tras la entrega porque los títulos estaban en la línea 1).

El instituto Khipu (Cusco) pide las citas «con el sistema de Word» (su esquema trae campos `CITATION` y una fuente en `customXml`), y las definiciones conceptuales de la matriz como citas textuales con página. `scripts/armar_con_citas_word.py <avance.docx> <texto.txt> <salida.docx>` arma el Word desde un texto marcado (`#` títulos, `{c:Tag}`, `{n:Tag}`, `{cp:Tag:pág}`, `{np:Tag:pág}`, `[TABLA]`, `[NOTA]`, `[HORIZONTAL]`, `!!` en amarillo, `[BIBLIOGRAFIA]`), con cada cita como campo y las fuentes en el `customXml`; `indice.ps1` las rellena con el estilo APA de Word. El ejemplo está en `trabajos/21-silvia_texto.txt` (Silvia Taype, 19-oct-2026). Si el cliente pide «simular» los datos o manda una base que dice ser ficticia, no se redacta el capítulo de resultados: se le da el cuestionario y una guía para aplicarlo.

Si el cliente manda una guía APA de su universidad, las referencias se comparan con ella y no
solo con APA 7: la de la UCV («Guía de redacción de textos estilo APA», 2023) une los autores con
«y» y no con «&», y las referencias van alineadas a la izquierda con sangría francesa (justificadas
salen con espacios estirados). Si su formato de letra choca con la plantilla del asesor, se
pregunta a Benicio (Luna, 14-oct-2026: se quedó Arial de la plantilla y se añadió la sangría de
1,27 cm de la guía).

Las revisiones de literatura (segunda especialidad UCV, guía PP-G-02.07) suelen traer una matriz
de 40 a 50 estudios armada con IA, con «por verificar» y «pendiente de extracción»: cada estudio se
busca por autor y tema en OpenAlex y Crossref y se descarta el que no aparece (con Edheliza Cardenas,
17-oct-2026, no existían 9 de 50). El corpus final sale solo de fichas verificadas con resumen, y los
datos de la matriz, de esos resúmenes. Si el Word es un PDF convertido (tamaño carta, una sección por
hoja, márgenes rotos), se rehace desde cero con python-docx en el formato de la guía y se reutiliza
solo el logo de la carátula.

Cuando la revisión sistemática no tiene búsqueda hecha (Zulma Pacompia, 20-oct-2026), la búsqueda se
hace de verdad y se guarda cada número: Scopus por API (sin comodines dentro de frases: con
`"cognitive behavio*"` la API se cuelga), PubMed por E-utilities (`esearch` + `efetch`, trae el resumen)
y OpenAlex con términos en español y portugués y `language:es|pt` para lo latinoamericano (SciELO
devuelve 403). Se unen por DOI y título; el cribado y la extracción con RoB 2 o ROBINS-I se reparten
entre dos agentes con criterios cerrados, y sus casos límite se deciden a mano. El PRISMA sale de
`prisma_flujo.py` de la skill de revisión (fase 5), con `--incluidos` = estudios e `--informes` =
artículos cuando un ensayo tiene dos. Una tabla apaisada en medio del texto deja casi una hoja en
blanco: mejor vertical y con menos columnas. Si Word no exporta a PDF ni un documento vacío («servidor
RPC no disponible»), el fallo es de Word en la PC: se entrega el Word y Benicio guarda el PDF a mano.

**El trabajo sale sí o sí con el formato de su universidad** (lo pidió Benicio el 21-oct-2026,
con Zulma Pacompia: se entregó «hasta la discusión» sin conclusiones, recomendaciones, resumen ni
abstract, y hubo que añadirlos después). El formato se pide siempre, en cada cliente, aunque la
universidad sea conocida: la guía, el esquema o la plantilla. Antes de entregar, el Word se compara
con el esquema de la guía parte por parte, de la carátula a los anexos (declaratorias, dedicatoria,
agradecimiento, índices, resumen y abstract incluidos), y con su orden, sus nombres y su letra. Lo
que falte se le dice a Benicio en el momento 1 de 2.9, en una tabla «parte de la guía · ¿está?», con
quién la tiene que hacer: lo nuestro se ofrece (y se cotiza si no estaba en el encargo), y lo que
solo da el cliente (firmas, DNI, dedicatoria) se le pide. Nunca se da un trabajo por completo
mientras falte una parte del esquema sin haberlo dicho.

**Si el cliente manda su propio Word, se toma su formato** (lo pidió Benicio el 21-oct-2026, con
Zulma Pacompia: «el tipo de letra, los espacios y todo ello quiero que los tomes»): letra y tamaño,
interlineado, espacio entre párrafos, sangría de primera línea, alineación de los títulos de
capítulo y de «REFERENCIAS», sangría francesa y espacio entre referencias, y la carátula (qué va en
negrita y en qué tamaño). Se mide en lo que se ve, no en los estilos: se exporta su Word a PDF y se
leen con pymupdf la fuente, el tamaño y el salto entre líneas (`get_text('dict')`), y se mira una
hoja en imagen, porque en un Word convertido de PDF todo viene heredado. Lo que la guía no fija se
copia del cliente; lo que la guía fija (márgenes, numeración) manda la guía. Después se actualiza
el índice y se comprueba que el texto no cambió.

Un TA nivel 1 de segunda especialidad UCV (Wilmer, 21-oct-2026) se rehízo desde cero con `scripts/armar_ta_ucv.py` (texto marcado con `#`, `##`, `[TABLA id]`, `[REFERENCIAS]`…`[FIN]`, `[ANEXOS]`, `*cursiva*`, `[[amarillo]]`). Sirvió repartir las fuentes en tres agentes a la vez (comprobar las citas del avance, armar el corpus con búsquedas reales y buscar conceptos y teorías) y, al final, uno que audite la fidelidad de cada dato contra los resúmenes: encontró 17 exageraciones («pequeño» para un efecto que la fuente llama medio, un pre-post presentado como ensayo). Con dos obras del mismo autor y año, la letra a/b va por orden alfabético del título (sin «The»), no por el orden del corpus. Los DOI de *Interdisciplinaria* que da Scopus pueden no resolver: se cita con el enlace de Redalyc. `para_turnitin.py --hasta "Anexos"` deja al final la sección apaisada vacía: se pasa su `sectPr` al cuerpo antes de exportar.

El TSP de Psicología de la UMA (estudio de caso clínico, Eda Aguirre y Mirella Garrido, 21-oct-2026) se arma sobre la propia plantilla de la universidad con `scripts/armar_tsp_uma.py plantilla.docx datos.json texto.txt tablas.json salida.docx`: conserva la carátula con el logo y copia el formato de los títulos y del cuerpo de la plantilla; `datos.json` lleva carátula, declaración de dos autoras, resumen y abstract, y el texto admite `###`, `> ` (líneas sin sangría), `**negrita**` y `[HORIZONTAL]`/`[VERTICAL]` para la tabla de sesiones del programa. Después van `indice_word.py --despues "ÍNDICE" --sin-titulo`, `indice_tablas_word.py` e `indice.ps1`. En el MCMI-IV, una TB de 60 a 74 en un patrón de personalidad es un «estilo» y no un rasgo patológico, y en los síndromes clínicos la presencia empieza en TB 75: los avances suelen leerlo mal. Los niveles del IDE de Aiquipa van por percentiles (manual de 2012: 1-30 bajo o normal, 31-50 moderado, 51-70 alto, 71-99 muy alto). Los clientes suelen poner el percentil como si fuera el puntaje y sumar mal a mano: se pide el cuestionario respondido y se recalcula con la clave (MR 5, 9, 14, 15, 17, 22, 26, 27, 28 · MIS 4, 6, 13, 18, 19, 21, 24, 25, 29, 31, 46 · PP 30, 32, 33, 35, 37, 40, 43, 45 · NAP 10, 11, 12, 23, 34, 48 · DEX 16, 36, 41, 42, 49 · SS 1, 2, 3, 7, 8 · DCD 20, 38, 39, 44, 47) y con la tabla de baremos del manual (Eda Aguirre, 22-oct-2026: dos factores mal sumados, y la subordinación, que era moderada, figuraba como baja). Si aplicaron el MCMI-III y no el IV, se reporta como MCMI-III, nunca como IV. La hoja de depresión de la OMS se actualizó en septiembre de 2026 (322 millones, 5,2 % de adultos): no se copian las cifras viejas del avance.

Cuando los datos son fichas de inspección en Word (una tabla por vivienda, con registro de lesiones y fotos; Carla Tarrillo, UNPRG, 22-oct-2026), cada lesión se transcribe a una base en un script del scratchpad. Las frecuencias se cuentan dos veces, sobre las lesiones y sobre las viviendas, y las fotos se sacan de cada tabla por su `r:embed` para hacer láminas de figuras en resultados. Antes de usar las fichas se cruzan sus fotos con lo registrado: las fichas copiadas de una a otra suelen tener ubicaciones que la foto contradice, y eso va al informe como dato por confirmar. Si el asesor o el docente quitó un objetivo y no hay datos para otro (entrevistas sin aplicar), se pregunta a Benicio y los objetivos se ajustan a lo que miden las fichas.

Las fuentes inventadas también pueden estar en lo que el docente ya aprobó (en verde): se comprueban todas, no solo las de la parte observada. Con Milagros Leon (21-oct-2026) un estudio de ferreterías de Áncash con cifras de fidelidad (40/40/8/12) estaba en la realidad problemática aprobada y no existía, igual que tres tesis citadas en la metodología. Si el cliente pide «las referencias en otro documento», se entregan en un Word aparte, y la versión de `03-turnitin` lleva esas referencias al final para que el porcentaje sea el del trabajo entero.

Antes de dar una entrega por cerrada se comprueba que **cada** entregable cotizado esté en
`06-enviar` (o la carpeta de entrega que tenga el cliente): a Luna le faltó la matriz en Word,
que se había hecho y acabó en la papelera.

---

# Etapa 1: cotizar

## 1.1 Leer todo

```
python <skill>/scripts/leer.py <archivo> <scratchpad>/avance.txt
```

Se corre sobre el avance y sobre la guía, y después **se leen los dos .txt enteros**. El
script da además, para un Word, las secciones con sus palabras, los párrafos largos sin cita,
los huecos sin completar (`[ ]`, `____`, «completar») y el cruce entre lo citado y la lista de
referencias. Un PDF escaneado no trae texto: se lee como imagen con Read.

Si el cliente solo tiene el PDF (Soledad Sonco y Karol Mamani, 18-oct-2026), el Word se **rehace**:
no sirve convertirlo. pdf2docx deja una sección por hoja, los números de página como texto y los
párrafos partidos, y Word por COM se cuelga al abrir un PDF, porque espera el aviso de conversión.
Se extrae el texto con pymupdf: cada línea sale como bloque, y un párrafo termina en la línea que no
llega al margen derecho. Se pasa a un archivo marcado (`#` títulos, `[TABLA]`, `[FIGURA]`, `[NOTA]`), se
corrige con un script de reemplazos que falle si un texto viejo no está, y se arma con python-docx:
títulos con estilo de título, tablas APA rehechas a mano, figuras sacadas del PDF por su xref y, después,
los índices de la skill. Las cartas firmadas (juicio de expertos) van como imagen de su hoja, sin
retocarlas. Si Word se cuelga al abrir un archivo que ya se trabajó, suele ser porque otra instancia lo
tiene bloqueado: se actualiza sobre una copia con nombre nuevo, con `Start-Job` y `Wait-Job -Timeout`,
y solo se cierran los Word ocultos que abrió esta sesión.

Si el avance es un `.doc` antiguo, `leer.py` falla («is not a Word file»): se convierte antes con
Word por COM a `.docx` en el scratchpad (`SaveAs2(ruta, 16)`). Word por COM se cuelga a veces sin
avisar; se lanza dentro de `Start-Job` con `Wait-Job -Timeout` y, si vence, se cierran solo los
Word ocultos que abrió la sesión (Luis Huete, 20-oct-2026). Si OpenAlex agotó su cupo diario
(HTTP 429), las fuentes se buscan con `buscar.py --scopus` (así ya quedan comprobadas como
indexadas) y la ficha y el resumen de cada DOI se bajan de Crossref, con OpenAlex sin `mailto` de
respaldo.

Si el nombre del archivo lleva ñ o tildes, PowerShell se lo pasa mal a Python y `leer.py` dice
que no existe: se copia al scratchpad con un nombre simple (`Get-ChildItem -Filter "DISE*.docx"`)
y se lee esa copia. Si el título «Referencias» es un párrafo normal en negrita y no un estilo de
título, `leer.py` y `referencias.py` no encuentran la lista: los DOI se comprueban uno por uno
con `buscar.py --doi`. Si el texto de `leer.py` sale con huecos donde van las citas (« .») y la
sección de referencias en 0 palabras, las citas son de **Mendeley Cite** (controles `w:sdt` con la
etiqueta `MENDELEY_CITATION_v3_…` en base64) y `leer.py` no las lee: no están perdidas.
`python <skill>/scripts/mendeley.py <avance.docx>` las decodifica y da cada fuente con año, tipo,
veces citada y DOI (Lander Lacuta, 16-oct-2026). Por lo mismo, un «citado por .» o un «Según ,» en
la salida de `leer.py` no es una cita rota: hay que mirarlo con `mendeley.py` antes de cotizarlo como
error (con Lander se cotizó así y no lo era). Para trabajar ese Word sin romper Mendeley,
`scripts/mendeley_citas.py` clona citas existentes, corrige su texto manual y crea citas nuevas con
su ficha CSL dentro; las referencias nuevas se añaden a la bibliografía de Mendeley y se entrega un
`.ris` para que el cliente las importe. Si la plantilla numera los títulos con un estilo de lista, el
título «Contenido» del índice automático hereda el «I.» y corre los capítulos: se arregla con
`scripts/sin_numero_tdc.py` antes de `indice.ps1`. Cuando el cliente manda matrices de antecedentes (Word o Excel), llenarlas
es parte del encargo; los Excel se escriben con R (`openxlsx`), y en el registro de búsqueda solo
van ecuaciones que se corrieron de verdad en esta sesión, con su número real de resultados.

El Word del cliente suele traer resaltados y letras de color (marcas suyas o de la plantilla),
y un párrafo reescrito hereda el formato del que reemplaza. Antes de entregar se quitan del
cuerpo todos los `highlight`, `color` y `shd` de los tramos, se ponen los subtítulos en negrita
con «conservar con el siguiente», y solo queda en amarillo lo que el cliente debe confirmar.

### El índice: siempre la tabla automática de Word

El índice de contenidos se entrega hecho, nunca una hoja vacía ni un «se llena al final», y se
hace **como lo hace Word** con Referencias > Tabla de contenido > Tabla automática. Así lo dejó
Benicio a mano el 11-oct-2026 (trabajo de Luna) después de rechazar dos índices armados de otra
forma, y así se hace siempre:

1. **Los títulos llevan su nivel.** O tienen estilo Título 1 a 3, o se les pone el nivel de
   esquema en el `pPr` (`<w:outlineLvl w:val="0"/>`, 1 o 2), que no cambia la letra. Nivel 1:
   capítulos, Referencias, Anexos y el propio «Índice de contenidos»; nivel 2: apartados; nivel
   3: subapartados (problema general, objetivos específicos, cada categoría, cada teoría).
2. **Se inserta la tabla automática**: `python <skill>/scripts/indice_word.py <entrada.docx>
   <salida.docx>`. Es la pieza de Word tal cual: un control de contenido de la galería «Table
   of Contents», el título «Contenido» (estilo TOC Heading, negro y negrita) y un solo campo
   `TOC \o "1-3" \h \z \u`. Va detrás del párrafo «Índice de contenidos» (`--despues "…"` para
   otro), y si la plantilla ya traía una tabla automática, la reemplaza.
3. **Se rellena con Word**: `powershell -File <skill>/scripts/indice.ps1 -ruta <ruta completa>`
   actualiza la tabla con las páginas reales e imprime las entradas. El Word no puede estar
   abierto.
4. **Se mira**: se exporta a PDF y se ve la hoja del índice en imagen (pymupdf) antes de avisar.

**El índice de tablas y el de figuras van igual, con la pieza de Word** (Referencias > Insertar
tabla de ilustraciones), nunca con entradas escritas a mano: `python <skill>/scripts/
indice_tablas_word.py <entrada.docx> <salida.docx> [--rotulo Figura]` y después `indice.ps1`.
El script pone el campo `TOC \h \z \c "Tabla"` detrás de «ÍNDICE DE TABLAS» y deja cada rótulo
como lo deja Insertar título: «Tabla » + campo `SEQ Tabla` y, tras un salto de línea, el título
en cursiva, todo en un párrafo. Se ve igual que el rótulo APA de dos líneas y la entrada sale
«Tabla 1 Título … página». Benicio lo pidió así el 11-oct-2026 (proyecto de Analiz).

Lo que no se hace: campos `TC`, quitarle la negrita o la cursiva a las entradas, escribir las
entradas a mano o cualquier retoque sobre lo que deja Word. El índice queda con el aspecto de
Word, para que el cliente lo actualice con clic derecho. Las hojas de «Índice de tablas» e
«Índice de figuras» de una plantilla no se dejan vacías: si el documento no tiene tablas ni
figuras, se quitan y se avisa. Si una sección reinicia la numeración donde no debe (anexos que
vuelven a la página 1), se le quita el `w:start` a su `pgNumType`. En `para_turnitin.py`,
`--desde` tiene que ser el título real y no la entrada del índice («Introducción», no «I.»).

El avance puede traer un índice escrito a mano dentro de un control de contenido (`w:sdt`) y, al
final, una captura de Turnitin de una entrega anterior pegada en un título vacío: el índice se
reemplaza por la tabla automática y la captura vieja se retira y se avisa. Para saber si un
párrafo lleva imagen se busca `<w:drawing` en su XML, no «drawing» a secas (está en los espacios
de nombres de todos). Si `add_section` copia un `pgNumType w:start`, se le quita para que los
anexos no vuelvan a la página 1; y a la versión de `03-turnitin` se le quita el salto de sección
apaisada que queda al final, o sale con una hoja en blanco (Elisai Galarreta, 13-oct-2026).

`leer.py` no muestra los comentarios al margen del Word. Suelen ser las observaciones de la
asesora y son la lista de trabajo más fiable: se leen siempre de `word/comments.xml` (con
`zipfile`) antes de cotizar, se atienden uno por uno, se responden en una tabla del informe y
se quitan del Word corregido (`commentRangeStart`, `commentRangeEnd` y el tramo con
`commentReference`), porque si quedan parecen observaciones sin levantar.

**Siempre se trabaja con la rúbrica** (lo pidió Benicio el 21-oct-2026, con Wilmer: «es sumamente necesaria»). Es la que dice con qué se califica cada parte, así que se busca en la guía, en la plantilla, en el sílabo o en las capturas del aula. Si no está, se pide al cliente en el mensaje de cotización junto con la guía, y se vuelve a pedir en cada mensaje hasta que llegue. Si se trabaja sin ella porque no llegó, se dice en la cotización y en el informe a Benicio. Al terminar, el documento se repasa criterio por criterio contra la rúbrica (en el informe a Benicio, una línea por criterio: dónde se cumple) y, si el cliente la tiene llenada por el docente, cada observación es parte de la lista de trabajo.

Antes de cotizar se pide el chat si no está: Benicio a veces ya dio un precio al cliente, y
ese precio manda sobre el que salga de la tabla.

**Sin la guía de la universidad no se cotiza** (lo pidió Benicio el 17-oct-2026, con Carla
Tarrillo: se cotizó sin la guía de la UNPRG y el precio quedó a ciegas). Si en la carpeta no
está la guía, el esquema o el reglamento de su universidad o del curso, se lee el avance igual
y se guarda el diagnóstico en `cotizacion.md` con `Estado: falta la guía`, **sin precio ni
plazo**. A Benicio se le da: lo que se ve del avance en tres o cuatro líneas, lo que no se puede
saber sin la guía (estructura que exige, tope de similitud, norma de citas, extensión) y un
mensaje corto de WhatsApp que pide la guía o el reglamento, la plantilla si la hay, el tope de
similitud con sus condiciones, la fecha de entrega y los datos que hagan falta (fichas,
encuestas, base). El mensaje no lleva precio. Cuando llega la guía se sigue desde 1.3 y se
termina la cotización. Solo se cotiza sin guía si Benicio lo dice expresamente («cotiza igual»)
o si el cliente contesta que su universidad no tiene; entonces se usa la estructura de la skill
del método y se avisa en la cotización. Si falta el avance (quiere todo desde cero), se
cotiza como trabajo desde cero con lo que diga el chat, con la misma regla de la guía.

## 1.2 Qué producto es y qué skill manda

Se lee `<skill>/references/mapa-de-skills.md` y se decide si es tesis, TSP, informe, artículo
o revisión. Para cada sección importante se abre la skill del método que le corresponde, en
`<METODO>\<producto>\fuente\`, y se usa como vara: qué debería traer esa sección
y qué le falta a la del cliente. No hace falta leerlas todas para cotizar; sí las de las
secciones que se vean flojas, porque de ahí sale el tamaño real del trabajo.

## 1.3 Comparar con la guía

Punto por punto, en el orden de la guía:

- ¿Está cada sección que la guía pide, con el nombre y el orden que pide?
- ¿Cumple lo que la guía dice de esa sección? (tiempo verbal, extensión, antigüedad de los
  antecedentes, qué va en la tabla de operacionalización, máximo de páginas de anexos…)
- Los números que la guía exija se cuentan, no se estiman: palabras del título, porcentaje de
  artículos, porcentaje en otro idioma, años de antigüedad, tope de similitud y **con qué
  programa** (Turnitin, Compilatio…). Si el programa no es Turnitin, se dice.
- **Con qué condiciones mide la similitud la universidad**, que es lo que decide qué archivo se
  sube y con qué filtros. Se busca en la guía, en la plantilla y en las declaratorias (la de la
  UCV dice «sin filtros, ni exclusiones») y en el chat o las capturas del aula: si se excluye
  la bibliografía, las citas o las coincidencias pequeñas; si se sube el documento completo
  (con carátula, declaratorias y anexos) o solo el cuerpo; quién lo sube (el cliente en su
  aula, el asesor o nosotros); y el tope. Lo que se encuentre se dice a Benicio en la
  cotización y se anota en la línea «Similitud» de `cotizacion.md`, con la frase textual de la
  universidad. Lo que no aparezca en ningún lado se dice igual («la guía no dice el tope ni
  los filtros») y va como pregunta para el cliente; no se supone.

## 1.4 Comprobar las referencias

```
python <skill>/scripts/referencias.py <avance.docx> --scopus
```

Comprueba cada DOI en Crossref (que exista y que sea de esa fuente), clasifica cada referencia
y da los porcentajes. `--scopus` dice cuáles están indexadas. Lo que hay que mirar:

- DOI que no resuelve o que es de otra fuente: referencia inventada o mal copiada. Es la señal
  más fuerte de un texto hecho con IA sin revisar, y multiplica el trabajo.
- Autores incompletos, `[iniciales]`, «et al.» en la lista: el script trae los nombres reales.
- Citas en el texto que no están en la lista, y al revés (lo da `leer.py`).
- Cuántas referencias faltan para llegar al mínimo de la guía: con N referencias y A artículos,
  hacen falta x tales que (A + x) / (N + x) ≥ el porcentaje pedido.

Las tesis y los libros no tienen DOI: se comprueba el enlace del repositorio de dos o tres al
azar si hay dudas, no de todas.

**Una referencia dudosa la comprobamos nosotros, nunca se le pide al cliente** (lo pidió Benicio
el 21-oct-2026, con Zulma Pacompia: se le había dejado «confirme Saffioti y Delgado»). Un libro
o capítulo sin DOI se busca en la web (Google Books, la librería o la editorial, WorldCat,
ResearchGate) por autor y título. Si existe, se completa (con Delgado salió que era un capítulo
de un libro colectivo de Comares, con sus directoras y páginas). Si no existe con esos datos, se
cambia por la obra real del autor que diga esas ideas, con su edición comprobada (el «Género,
violencia y poder» de Saffioti no existe; se citó *Gênero, patriarcado, violência*, 2004), o por un
artículo con DOI. Se corrigen la referencia y sus citas en el texto, y se cuenta en el informe de
revisión, en «Por qué se cambiaron algunas cosas».

## 1.5 Coherencia interna

Lo que ningún script ve y más pesa en una sustentación:

- Título ↔ problema ↔ objetivos ↔ hipótesis ↔ matriz de consistencia: mismas variables, misma
  población, mismo lugar y año, mismos enunciados.
- Dimensiones del marco teórico = las de la operacionalización = las del instrumento.
- Tipo, nivel y diseño que no se contradigan; población, muestra y muestreo que digan lo mismo
  (un «censal» con «muestreo por conveniencia» es contradicción).
- Que la muestra alcance para la estadística que anuncia.
- Párrafos repetidos, frases cortadas, cifras que cambian de un capítulo a otro.
- Si suena a IA: corchetes sin completar, párrafos de largo idéntico, secciones enteras sin una
  sola cita, la misma fórmula al cerrar cada antecedente. Cuenta como trabajo (humanizar).

## 1.6 Poner precio y plazo

Se lee `<skill>/precios.md` y se arma el precio **con lo que el cliente necesita**: se suman
los renglones que apliquen, se ajusta por nivel y urgencia y se redondea. Siempre se da:

- el precio recomendado y el piso si regatea;
- el plazo con fecha exacta de entrega (un día antes de la fecha del cliente, para que revise);
- contra qué casos anteriores se comparó, en una línea.

Si el caso no encaja en ningún renglón, se propone un precio razonado y se le dice a Benicio
que es nuevo, para que lo confirme. Lo que él decida se anota en `precios.md` en ese momento:
el renglón nuevo y la fila del historial. Si el cliente tiene tiempo y poco presupuesto, se
menciona la alternativa de venderle el método (está en `precios.md`).

## 1.7 Entregar la cotización

En el chat, corto y en este orden:

1. **Precio y plazo**, arriba de todo.
2. Lo que está bien (tres o cuatro líneas: da confianza al cotizar y evita rehacer de más).
3. Lo que hay que arreglar, numerado, lo más grave primero, con el dato exacto («6 de 13 son
   artículos, 46 %; la guía pide 60 %»).
4. Avisos que cambian el trato: otro programa de similitud, referencias inventadas, plazo
   imposible, algo que solo el cliente puede dar.
5. **El mensaje de WhatsApp**, listo para pegar, precedido de la línea «Escrito para: …».

El mensaje va en prosa, corto, tratando al cliente como lo trata Benicio en el chat (de tú o
de usted, según la captura). Dice primero lo bueno, después qué falta en palabras del cliente,
el precio, el 50 % para empezar, la fecha de entrega y una o dos preguntas que hagan falta
para arrancar. Termina con el Yape. No promete porcentajes de Turnitin ni de IA, no menciona
la IA y no lleva rayas largas.

Si el cliente pregunta qué garantía tiene («¿hay contrato?», «que no me dejes plantada»), **no
se ofrece un contrato ni un acuerdo por escrito** (lo pidió Benicio el 17-oct-2026, con Carla
Tarrillo: «así no, yo soy serio»). La respuesta se apoya en quién es Benicio: investigador
registrado en RENACYT, conocido en TikTok, con seguidores y tesistas que lo respaldan, y en
que el segundo 50 % se paga recién al recibir el trabajo.

**Si el cliente no mandó lo de su universidad, el mensaje lo pide siempre** (lo pidió Benicio
el 17-oct-2026, con Luis David Huete; desde Carla Tarrillo, ese mismo día, sin la guía no hay
precio: ver 1.1, y esta regla queda para lo que falte tras recibirla o cuando Benicio pidió
cotizar igual): la guía o el esquema de su universidad o del curso, la
plantilla con la estructura que pide y el tope de similitud con sus condiciones. Va en una frase
propia, antes del precio, aunque la universidad sea una que ya conocemos (la UCV cambia de guía
por programa y por curso), y en `cotizacion.md` queda en «Preguntas para el cliente». Se vuelve
a pedir en cada mensaje siguiente (respuesta a un regateo, confirmación de pago, inicio del
trabajo) hasta que llegue. Una guía de otro cliente de la misma universidad sirve solo de
referencia: lo que se tome de ella se le dice a Benicio como «por confirmar con su guía», nunca
como lo que pide la universidad del cliente.

Lo mismo se guarda en `cotizacion.md` dentro de la carpeta del cliente:

```
# Cotización · <cliente>
Estado: cotizado
Fecha: 10-oct-2026
Cliente: <nombre, teléfono si se ve, carrera, universidad, nivel>
Producto: <tesis | proyecto | TSP | informe | artículo | revisión>
Norma de citas: <APA 7 | ISO 690 | Vancouver> · Similitud: <tope y programa>
Fecha que pide: <fecha exacta> · Entrega ofrecida: <fecha exacta>
Precio: S/ <n> (piso S/ <n>) · Pago: 50 % + 50 %

## Lo que está bien
## Lo que hay que arreglar        (numerado; es la lista de trabajo de la etapa 2)
## Preguntas para el cliente
## Mensaje enviado
## Bitácora                       (una línea por día: qué se hizo, qué falta)
```

Y ahí se detiene la skill. No se crea ninguna otra carpeta ni se toca el Word.

---

# Etapa 2: hacer el trabajo

Empieza cuando Benicio dice que el cliente pagó. Se anota en `cotizacion.md` (`Estado:
pagado`, monto y fecha), se crean las cinco subcarpetas y se mueve a `01-original` lo que
mandó el cliente.

## 2.1 Plan de trabajo

La lista «Lo que hay que arreglar» de la cotización es el plan. Se ordena así, porque cada
paso condiciona el siguiente:

1. **Columna vertebral**: título, problema, objetivos, hipótesis, variables y dimensiones. Si
   esto cambia, cambia todo lo demás; se cierra primero.
2. **Fuentes**: buscar y verificar las que faltan.
3. **Antecedentes y marco teórico**, con las fuentes ya en la mano.
4. **Metodología** y matriz de consistencia, alineadas con el punto 1.
5. **Lo administrativo y los anexos**: presupuesto, cronograma, instrumentos, fichas.
6. **Referencias**: lista completa, en la norma, sin huérfanas.
7. **Redacción**: que no suene a IA.

Solo se hace lo que se cotizó. Si al trabajar aparece algo grande que no estaba (un capítulo
que hay que rehacer entero), se le avisa a Benicio antes de hacerlo, porque cambia el precio.
Cuando el cliente dice «revisa el foro» o «revisa como quedamos», se lee para ver si pide algún
cambio en lo encargado: si lo pide, se aplica y se le dice que ya está; si no tiene relación, se le
dice eso. No se hace la actividad del foro por iniciativa propia ni se le ofrece; si el cliente
la pide aparte, se cobra como encargo nuevo (Rocío Zegarra, 15-oct-2026: foro IFA de ~20 líneas,
dos preguntas y dos comentarios, S/ 20) y se le envía el Word para que lo publique él. Un foro también se pasa por Turnitin antes de enviarlo, porque el aula lo mide al publicar: el de Rocío salió con 40 % y el docente le puso 12 (22-oct-2026); se cita con paráfrasis propia y sin cifras ni oraciones tomadas del artículo.

En un informe de curso sobre una empresa real (no una tesis), el docente puede no querer
literatura: con Rocío Zegarra (UCV, 17-oct-2026) pidió poco texto antes de las tablas, una sola
cifra citada, solo la normativa que haga falta, nada de normas ISO de adorno, y ninguna
conclusión ni lista de referencias dentro del punto: van al final del informe del grupo. Si el
cliente solo hace un punto, se le entrega aparte un Word con la conclusión y las referencias de
ese punto para quien arme el final. Si llegan audios del grupo o de la grabación, se transcriben
y se toma solo lo que toca al punto del cliente.

## 2.2 El método de cada sección

Antes de escribir una sección se lee la skill del método que le toca, según
`references/mapa-de-skills.md`, y se sigue su método con las adaptaciones de ese archivo: sin
herramientas del conector, sin menús ni preguntas al tesista, con las citas escritas en la
norma de la universidad. Cuando la skill y la guía de la universidad chocan, manda la guía.

### La metodología lleva siempre la muestra con su fórmula

Falla del 13-oct-2026 (Elisai Galarreta, UCV): se entregó la metodología con «estudio censal,
no se extrae muestra» y la clienta reclamó a los quince minutos que faltaban la fórmula y lo de
la muestra. Benicio pidió que no vuelva a pasar. En todo proyecto o tesis cuantitativa:

- La metodología nombra por separado **población, muestra y muestreo**, aunque se trabaje con
  toda la población. Nunca se despacha con «no se extrae muestra».
- **La fórmula del tamaño de muestra va escrita, en su propia línea, con sus valores y el
  resultado**: población finita, n = (N · Z² · p · q) / (e² · (N - 1) + Z² · p · q), con
  Z = 1,96, p = q = 0,5 y e = 0,05 salvo que la guía o el asesor digan otra cosa; población
  desconocida o muy grande, n = (Z² · p · q) / e². El cálculo se hace con Python y se escribe
  el número que sale y su redondeo hacia arriba.
- Si la población es pequeña y el resultado queda cerca de N (50 docentes dan 45), se dice eso
  mismo y se trabaja con todos como **muestra censal**; si no, la muestra es la calculada y se
  nombra la técnica de muestreo con su cita. Lo que el avance del cliente ya decía (censal,
  por conveniencia, aleatorio) se respeta si no contradice el cálculo.
- La matriz de consistencia y los anexos dicen lo mismo que el texto (N, n y tipo de muestra).

Antes de dar por terminada cualquier sección se revisa además **lo que la plantilla espera de
ella aunque no lo diga en el título**: su cronograma de actividades y su lista de anexos
suelen enumerar el contenido (la de la UCV lista «Población, muestra y muestreo», «Validez y
confiabilidad» y un anexo de «cálculo del tamaño de la muestra»). Cada elemento que aparezca
ahí tiene que estar en el documento, con ese nombre.

## 2.3 Fuentes: solo las que existen

```
python <skill>/scripts/buscar.py "términos en inglés" --desde 2021 --idioma en --n 15
python <skill>/scripts/buscar.py "términos" --pais PE --idioma es          antecedentes nacionales
python <skill>/scripts/buscar.py "términos" --scopus --desde 2021           qué hay en Scopus
python <skill>/scripts/buscar.py --doi 10.xxxx/yyyy                          ficha y resumen completos
```

Reglas que no se negocian:

- **No se inventa ninguna fuente, autor, año, página ni cifra.** Toda referencia nueva sale de
  una búsqueda de esta sesión y lleva DOI comprobado.
- **Se escribe solo lo que el resumen dice.** Si el resumen no trae la muestra, el coeficiente
  o la conclusión, ese dato no entra. Una fuente sin resumen disponible no se usa para datos.
- La antigüedad, el idioma y el tipo de fuente los fija la guía. Se buscan de más y se eligen
  las que de verdad tratan las variables del cliente, en una población parecida.
- Los libros que se añaden (también los de metodología) son de los últimos 5 años y, como
  máximo, de hace 10; si la guía no dice otra cosa, una edición más vieja (Hernández Sampieri
  2014) se cambia por una más reciente o por artículos con DOI (lo pidió Benicio el 18-oct-2026,
  con Jimena Mayhua). Los libros viejos que ya trae el cliente se avisan, no se tocan si no se cotizó.
- Una página citada (p. 93) solo se pone si se leyó en esta sesión. Para las definiciones de
  metodología con página se usa un libro de acceso abierto que se pueda descargar y leer:
  Arias Gonzáles et al. (2022), *El método ARIAS…*, INUDI, CC BY, DOI 10.35622/inudi.b.016
  (PDF en editorial.inudi.edu.pe/editorialinudi/es/catalog/download/22/16/32; investigación
  aplicada p. 107, diseño correlacional p. 97). Si el cliente pide «los libros» para ver las
  páginas, se le manda ese PDF, que se puede compartir; los libros comerciales no se envían
  (Jimena Mayhua, 20-oct-2026: Baena p. 19 y Hernández-Sampieri p. 93 no se pudieron comprobar).
- Entre los antecedentes va al menos uno que no favorezca del todo la hipótesis, si existe.
- Las teorías clásicas (Vygotsky, Bruner, Piaget…) se citan por la obra, con sus datos reales
  de edición; si no se puede comprobar la edición, se cita a través de un artículo reciente
  que la aplique, y se dice así.
- Scopus con esta clave da un solo autor y sin resumen: cada hallazgo se completa con `--doi`.
  El cupo de OpenAlex sin clave es diario; si se agota, se sigue con `--scopus` y Crossref.

Al terminar se vuelve a correr `referencias.py` sobre el Word corregido: los porcentajes de la
guía tienen que cumplirse, sin ningún DOI en rojo. Si la guía o el dictamen miden la
**antigüedad media**, se calcula también (año en curso menos el año de cada referencia): las
obras clásicas de estadística la suben rápido. Con Eduardo Sime (17-oct-2026) la lista pasó
de 7,7 a 8,4 años al añadir fuentes de método, y se bajó a 6,9 cambiando artículos antiguos
prescindibles por otros recientes. Si OpenAlex agota su cupo, Crossref
(`api.crossref.org/works?query.bibliographic=…&filter=has-abstract:true`) trae resúmenes de
revistas latinoamericanas, y DataCite (`api.datacite.org/dois/…`) los de tesis con DOI. Un
informe oficial en PDF (INDECI, MINEDU) que WebFetch devuelve en bruto se lee con pymupdf desde
el archivo que guarda la herramienta.

## 2.4 Escribir en el Word

Se edita siempre una copia del Word del cliente, para no perder tablas, figuras, estilos ni
numeración. Los cambios van a un JSON y se aplican de una vez:

```
python <skill>/scripts/aplicar.py <01-original\avance.docx> <02-corregida\Nombre_CORREGIDO.docx> cambios.json
```

```json
[{"parrafo": 186, "viejo": "aula.periodo de observación.", "nuevo": "aula."},
 {"parrafo": 77, "nuevo": "párrafo entero reescrito"},
 {"despues_de": 80, "texto": "párrafo nuevo", "como": 80},
 {"borrar": 199},
 {"celda": [2, 2, 2], "nuevo": "S/ 25.00"}]
```

Los números de párrafo y de tabla son los de `leer.py` sobre el Word de entrada y no se corren
aunque se inserte o se borre. `*así*` queda en cursiva (títulos de revista en las
referencias). El script no guarda nada si un cambio falla o mete una raya larga. Para una
segunda tanda de cambios se vuelve a correr `leer.py` sobre el Word ya corregido y se parte
de sus números.

`aplicar.py` deja cada párrafo con el formato de su primer tramo. Un párrafo que empieza con una
entrada en negrita («Validez.», «Comprensión oral.») no se le pasa entero, porque saldría todo
en negrita: se reescribe antes, en un script corto del scratchpad que conserva el primer tramo
y cambia el resto, sin añadir ni quitar párrafos para que los números no se corran. El amarillo
de los datos por confirmar y los reemplazos generales (comillas, «y» por «&») van en otro
script, después de `aplicar.py`. Ningún script del scratchpad se llama como un módulo de Python
(`inspect.py`, `json.py`, `copy.py`): rompe la carga de python-docx.

Si la asesora anotó el esquema de la guía (cuántos antecedentes, cuántos párrafos, qué
subtítulos lleva cada variable), esas notas mandan sobre la guía impresa y se cumplen una por
una. Los códigos del clasificador de gastos del MEF no se bajan de gob.pe ni de mef.gob.pe
(devuelven 403): se comprueban en sites.google.com/site/mundosiaf y se le dice al cliente que
los confirme con su asesor.

Lo que el script no hace (insertar una tabla o una figura nuevas, cambiar un título de nivel)
se hace con python-docx en un script corto del scratchpad, copiando el formato de una tabla
que ya exista en el documento.

Si hay que poner el índice (aunque la guía no lo pida, el cliente o el asesor lo suelen pedir),
se usa la tabla automática de Word de «El índice: siempre la tabla automática de Word». Solo
cuando el Word no trae hoja de índice y hay que crearla con su índice de tablas sirve además
`python <skill>/scripts/indice.py <entrada.docx> <salida.docx>`, que lo inserta tras la carátula, en
hojas sin numerar, con los títulos de nivel 1 a 3 y un índice de tablas. Supone que el párrafo 15
cierra la sección de la carátula y una hoja vertical con márgenes 3 y 2,54 cm: se ajusta si el
Word es otro. Después se abre con Word por COM (`TablesOfContents.Update()` y `Fields.Update()`)
para que salgan los números de página, y se comprueba contra un PDF exportado. La versión de
`03-turnitin` no cambia, porque va sin índices.

Si no hay avance y se escribe desde cero, se parte de la plantilla de la universidad si la
mandaron (es un Word: se rellena con `aplicar.py`); si no, se arma el documento con
python-docx siguiendo el esquema de la guía, con estilos de título reales.

## 2.5 Cómo se redacta

- Prosa académica en español, tercera persona, sin viñetas dentro de los capítulos salvo donde
  la guía las pida.
- El tiempo verbal que diga la guía (un proyecto va en futuro; un informe final, en pasado).
- Antes de redactar se lee `<SKILLS>/turnitin/voz.md` y las reglas de
  `<METODO>\tesis\fuente\10-humanizador-academico`: se escribe desde la idea, con oraciones de
  largo desigual y conectores que digan una relación que existe, sin fórmulas de cierre
  repetidas ni tríadas. Es más barato escribir bien que humanizar después.
- **Se redacta ya para 0 % de IA** (desde el 18-oct-2026), evitando lo que, según
  `references/ruta-ia-cero.md` de `/turnitin`, dejó a otros trabajos en «*%»:
  - Lo que el cliente escribió y no hace falta corregir se queda con sus palabras. No se
    «mejora» el estilo de un párrafo correcto: su texto es lo que pasa como humano y sirve de
    voz (`voz_tesista.txt`) para lo que sí se redacta.
  - Problemas, objetivos e hipótesis específicos no van en lista de tres gemelos que repiten
    la misma frase con otra dimensión. Si la guía no exige la lista, el enunciado general va
    entero y los específicos en una oración que nombra las dimensiones. Si la exige, cada uno
    se redacta con otro verbo y otro orden. H₀/H₁, cortas y llanas.
  - Los párrafos hermanos (descriptivos por dimensión, contrastes, discusión, conclusiones y
    recomendaciones por objetivo) no comparten esqueleto: cada uno entra por otro lado, sea la
    cifra, la dimensión o el estudio previo.
  - Las notas de tabla, los párrafos cortos y la prosa de las celdas se escriben con el mismo
    cuidado que el cuerpo, porque Turnitin también los marca.
- Un antecedente no se redacta siguiendo el resumen del artículo frase por frase: Turnitin lo
  empareja con el propio artículo. En el proyecto de Analiz la primera pasada dio 33 %, y la
  fuente de más peso era la revista de dos antecedentes. Desde la primera versión se cambia el
  orden de la información (se entra por el lugar, por la muestra o por el hallazgo) y se evitan
  las fórmulas «tuvo como objetivo determinar…», «Se llegó a la conclusión de que…» y «Este
  antecedente aporta al presente estudio…» repetidas en todos. Tampoco se alarga cada problema,
  objetivo e hipótesis específicos con la delimitación completa: se repite doce veces y cuenta.
- Nada de rayas largas, ni corchetes de «completar», ni notas al cliente dentro del documento.
  Lo que falte va a la lista de preguntas, y en el Word queda resaltado en amarillo solo el
  dato exacto que el cliente debe confirmar.
- No se cambian los datos del cliente: nombres, institución, cifras propias, lo que observó.
  Si algo de eso parece un error, se pregunta.

## 2.6 Lo que solo el cliente sabe

Número real de participantes, nombre del asesor, montos, si la institución ya autorizó, lo que
observó en el aula o en la empresa, resultados de un piloto. **No se inventa.** Se resuelve
así: se redacta con el dato que el avance ya trae, se deja el dato en amarillo y se anota la
pregunta. Los montos de un presupuesto sí se pueden estimar con precios de mercado razonables,
avisando que son estimados.

Si se entrega con amarillos que llena el propio cliente (DNI, fecha y % de similitud de las
declaratorias), el mensaje de entrega lo dice con todas las letras: «llenen lo amarillo y
quítenle el color antes de subirlo». Rocío Zegarra (19-oct-2026) presentó la S7 con los
puntos suspensivos en amarillo y preguntó después si «así era para presentar».

## 2.7 Verificar antes de entregar

1. `leer.py` sobre el Word corregido: ningún hueco, ninguna sección vacía, ninguna cita sin
   referencia ni referencia sin cita.
2. `referencias.py`: porcentajes de la guía cumplidos, DOI todos válidos.
3. Releer de corrido título, problema, objetivos, hipótesis y matriz: tienen que decir lo
   mismo con las mismas palabras clave.
4. Repasar la guía una vez más, punto por punto, contra el documento final.
   En la metodología se comprueba a ojo que estén, con su nombre: tipo, enfoque, nivel,
   diseño, variables, población, muestra **con la fórmula y su resultado**, muestreo, técnica,
   instrumentos, validez, confiabilidad, análisis de datos y aspectos éticos.
5. Abrir el Word generado con python-docx para confirmar que carga y contar tablas e imágenes:
   tienen que ser las mismas del original más las que se añadieron a propósito.
6. **El cierre de la Ruta 0 %** (pasos 7 y 8 de `ruta-ia-cero.md` de `/turnitin`), sobre el
   Word de `02-corregida` y antes de sacar el de `03-turnitin`: dos pasadas sobre el documento
   entero (`python <SKILLS>/turnitin/scripts/repeticiones.py <word>`
   y un agente que lea todo el cuerpo de una vez) y lectura línea por línea de lo redactado.
   Después se corre `control_cero.py <word>` para ver los arranques repetidos y la plantilla;
   sin reporte todavía no frena, solo avisa. Cuando vuelva el primer reporte de IA con marcas,
   se guarda en `05-pasadoporturnitin\primer-reporte.json` y desde ahí sigue `/turnitin`.

## 2.8 Los entregables

```
python <skill>/scripts/para_turnitin.py <02-corregida\X.docx> <03-turnitin\X_TURNITIN.docx> --desde "I. GENERALIDADES" --hasta "VI. ANEXOS" --pdf
python <skill>/scripts/informe.py <scratchpad>/informe.md <04-revision\Informe_de_revision.docx>
```

- `02-corregida\`: el Word limpio. Si el cliente o su asesor necesitan ver qué cambió, una
  segunda copia con los cambios en verde.
- `03-turnitin\`: sin carátula, índices ni anexos; se dejan las referencias (se descuentan con
  el filtro de bibliografía). En Word y en PDF.
  **Excepción: cuando la universidad pasa el documento completo** (la UCV, o el cliente lo sube
  entero en su aula), lo que va a `03-turnitin` es el Word completo, con carátula,
  declaratorias, índices, referencias y anexos, y **lo único que se le quita es el logo de la
  universidad**: `python <skill>/scripts/sin_logo.py <02-corregida\X.docx>
  <03-turnitin\X_COMPLETO.docx>`. El script borra solo las imágenes de la carátula (lo que hay
  antes del primer salto de sección) y deja todo lo demás igual. Lo pidió Benicio el 21-oct-2026,
  con Zulma Pacompia. El Word que se le entrega al cliente en `02-corregida` sí lleva el logo:
  si la carátula del avance lo traía y el Word nuevo no, se repone antes de entregar,
  recortándolo de su PDF con pymupdf (`get_pixmap(dpi=300, clip=<rect del logo>, alpha=False)`,
  porque `extract_image` lo saca con fondo negro cuando trae transparencia) y comprobando que la
  carátula siga en una sola hoja.
- `04-revision\`: el informe de revisión, de una o dos páginas, **escrito para el cliente**:
  qué se corrigió y por qué (en sus palabras, no en las nuestras), qué cumple ahora de la guía
  con sus números, y las preguntas pendientes. No habla de IA ni de cómo se hizo.

### Cuando el encargo es solo el análisis estadístico

Llega una base (Excel) y la matriz de consistencia, sin Word ni guía. La carpeta puede estar
fuera de `tesis-asesorar` (por ejemplo `cotiza\02`): se trabaja ahí mismo, con las mismas
subcarpetas. El Excel se lee con R (`readxl`, `openxlsx`), porque esta PC no tiene openpyxl;
R está en `C:\Program Files\R\R-4.6.1\bin\Rscript.exe` y no en el PATH. Se entrega en
`02-corregida` el capítulo de resultados en Word (armado con python-docx, tablas APA de tres
líneas), el script de R, un Excel con todas las cifras y las figuras. Con datos que no vienen
de un cuestionario (ratios financieros por año) no hay alfa de Cronbach, los cruces se hacen
indicador por indicador y la regla para decidir cada hipótesis se escribe en el capítulo. Con
series anuales cortas se revisa Durbin-Watson y se avisa en el informe de la tendencia común.
`para_turnitin.py --pdf` necesita rutas completas; con rutas relativas dice que guardó el PDF
y no lo guarda (con Renzo, el 15-oct-2026, tampoco lo guardó con rutas completas con barras `/`): se
comprueba que el PDF exista y, si no, se exporta con Word por COM (`ExportAsFixedFormat(ruta, 17)`).
Turnitin solo da el reporte de IA entre 300 y 30 000 palabras (cuenta también tablas y referencias). Si
la versión de `03-turnitin` pasa de 30 000, se saca además en dos partes con `--desde`/`--hasta`
(`_parte1`, `_parte2`, cortando en un capítulo) para la IA, y la similitud se toma del archivo entero
(Eduardo Sime, 17-oct-2026: 39 856 palabras).
Word por COM puede no guardar el PDF dentro de la carpeta del cliente sin dar error (`ExportAsFixedFormat` y
`SaveAs2` callaron, Eduardo Sime, 17-oct-2026): se exporta en el scratchpad y se copia, y siempre se comprueba con
`Test-Path` que el PDF nuevo exista antes de copiarlo a `06-enviar`. Si tampoco sale así, se prueba con un documento en
blanco (`Documents.Add()`): si Word se cae también («servidor RPC no disponible»), el fallo es de Word y no del archivo; se
entrega solo el Word, se saca de `06-enviar` el PDF viejo para que no quede desfasado y se avisa a Benicio (Rocío Zegarra,
20-oct-2026).

## 2.9 Informar a Benicio

La entrega se informa en **dos momentos** (lo pidió Benicio el 17-oct-2026, con Edheliza
Cardenas). Al terminar el trabajo no se le da todavía el mensaje para el cliente: primero tiene
que saber si se cumplió lo encargado y pasar el documento por Turnitin.

**Momento 1, al terminar el trabajo.** Corto, y en este orden:

1. **Lo que pidió el cliente**: cada cosa encargada, en una tabla de tres columnas (lo que
   pidió, sale del chat y de la cotización · ¿hecho? ✅ / ⚠️ parcial / ❌ no · dónde quedó o
   por qué no). Se cuenta cada encargo por separado, no por capítulo: «mejorar la
   introducción según la guía», «llenar las matrices», «50 referencias», «Turnitin».
2. **Lo que falta**, en una lista: lo pendiente, de quién depende (Benicio, el cliente, el
   asesor) y si impide subir a Turnitin. Si no falta nada, se dice en una línea.
3. Dónde quedó cada archivo.
4. Qué se hizo, en una tabla breve por sección, y los números de la guía antes y después.
5. Decisiones que se tomaron sin preguntar y preguntas para el cliente, si las hay.
6. Al final, según lo que falte: si el documento está completo, «Cómo lo mide la
   universidad» (si aplica) y las dos líneas de Turnitin; si no, la línea ⏳. Nada después.

En este momento **no** va la línea 📨 de envío ni el mensaje de entrega para el cliente.

**Momento 2, cuando Benicio deja el reporte en `05-pasadoporturnitin`** (o dice «ya subí»,
«ya está el reporte»). Se lee el reporte (IA y similitud, con sus filtros) y:

- Si cumple: se copia el reporte a `06-enviar` con nombre claro, se rehace `06-enviar` y recién
  entonces se da la línea «📨 **Envía al cliente:** `<ruta de 06-enviar>`» y el mensaje de
  entrega para WhatsApp, precedido de «Escrito para: …», con los porcentajes del reporte que
  vale para la universidad y el recordatorio del saldo.
- Si no cumple: se dice qué porcentaje salió y cuánto falta, y se sigue con 2.10 (`/turnitin`).
  El mensaje para el cliente espera hasta que el reporte cumpla.

Se actualiza `cotizacion.md` (`Estado: entregado`, y la bitácora) y la memoria del proyecto si
la sesión la lleva: cliente, monto pagado y pendiente, qué falta.

Si quedó algo en `borrar\`, se hace la pregunta de si se elimina esa carpeta.

La línea de envío va solo en el momento 2, con la carpeta y no con un archivo suelto:
«📨 **Envía al cliente:** `<ruta completa de 06-enviar>`».

**Solo se manda a subir a Turnitin cuando el documento está completo** (lo pidió Benicio el
13-oct-2026, con Maritza Rodríguez: se le dijo «sube» con el año y dos anexos todavía en
amarillo y una pregunta abierta). Completo quiere decir: ningún dato en amarillo, ninguna
pregunta al cliente sin responder y ningún cambio pedido sin aplicar, en todo el Word y no solo
en el cuerpo que va a Turnitin. No vale el argumento de que lo pendiente «no mueve el
porcentaje»: se sube una sola vez, con el documento cerrado.

Mientras falte algo, el mensaje **no lleva las dos líneas** y termina con esta, sin nada después:

> ⏳ **Todavía no se sube a Turnitin.** Falta: `<lo pendiente, en una línea, y de quién depende>`

y en el punto 1 se dice que el de `03-turnitin` aún no está para subir.

Cuando ya está completo, las dos últimas líneas del mensaje son siempre estas, al final y sin
nada después:

> 📤 **Sube a Turnitin:** `<ruta completa del Word de 03-turnitin>`
> 📥 **Deja el reporte en:** `<ruta completa de 05-pasadoporturnitin del cliente>`

La segunda dice dónde colocar los PDF que devuelva Turnitin (IA y similitud, juntos), sin que
lo pida (lo pidió el 12-oct-2026). Si la carpeta no existe, se crea antes de nombrarla.

**Si la universidad mide de otra forma, se dice ahí mismo y se sube como ella lo mide** (lo
pidió el 13-oct-2026, con Elisai Galarreta: la UCV exige el reporte «sin filtros, ni
exclusiones» y la clienta sube el documento completo en su aula, mientras que el 16 % que
teníamos era del cuerpo solo y con la bibliografía excluida). Antes de las dos líneas va un
párrafo corto, «Cómo lo mide la universidad», con: la frase textual de la guía o de la
declaratoria, qué archivo sube el cliente y quién lo sube, el tope si se conoce, y en qué se
diferencia de nuestra pasada. Cuando la universidad no admite exclusiones o el cliente sube el
documento completo, se hacen **dos pasadas** y se piden las dos: la del cuerpo de
`03-turnitin`, que es la que sirve para el reporte de IA y para trabajar con `/turnitin`, y la
del Word completo con todos los filtros apagados, que es el número que verá la universidad.
Ese Word completo no es el de `02-corregida` tal cual, sino su copia en `03-turnitin` sin el
logo de la universidad (`sin_logo.py`, ver 2.8). El porcentaje de la primera nunca se le da al cliente como si fuera el de su
universidad. Al leer un reporte que vuelve se miran sus filtros (`informe.py` de la skill
`/turnitin` los lista) y, si no son los de la universidad, se avisa antes de dar el resultado
por bueno.

Fuera de ese caso, un solo archivo, con su ruta completa para que la copie: el Word de `03-turnitin`, nunca el de
`02-corregida` (lleva carátula y anexos) ni una copia de otra carpeta. Si conviene encender un
filtro al subirlo («Excluir bibliografía»), va en la misma línea, entre paréntesis. Vale
también para las rondas: cada vez que el Word cambia, la versión de `03-turnitin` se regenera
y, si ya no queda nada pendiente, se le vuelve a decir cuál subir.

Benicio decide qué se le pregunta al cliente. Los datos que el avance ya trae (número de
participantes, autoría de los instrumentos, el título) se dan por buenos y no se convierten en
preguntas ni en amarillo, salvo que se contradigan dentro del propio documento. El título no se
cambia sin que él lo diga, aunque la guía pida otra cosa: se le avisa y decide él.

## 2.10 Después del reporte de Turnitin

Benicio pasa el documento y deja el PDF en `05-pasadoporturnitin`. Es el momento 2 de 2.9: si el
reporte cumple, se da ahí el envío y el mensaje para el cliente. Si el porcentaje de IA o
de similitud no cumple, **no se rehace aquí**: se usa la skill `/turnitin`, que es la que sabe
leer el reporte y reescribir solo lo marcado. Para eso se prepara la carpeta que ella espera:

```
tesis-turnitin\<nn>-<cliente>\actual\      copia del Word de 03-turnitin
tesis-turnitin\<nn>-<cliente>\reportes\ia\ o \similitud\   copia del reporte
```

y se carga `/turnitin` sobre esa carpeta. El resultado de su `Listo\` se trae de vuelta a
`02-corregida` (restituyendo carátula y anexos) y a `03-turnitin`.

---

## Rondas siguientes

- **Llegaron las respuestas del cliente**: se aplican sobre el último Word de `02-corregida`
  (la versión anterior pasa a `borrar\` y la nueva queda con el nombre de siempre), se quita
  el amarillo de lo resuelto y se regenera la versión de Turnitin.
- **Una revisión de terceros** (una tabla de «Pendientes» que el cliente pasó por otra IA o por un revisor, a veces un Excel convertido a Word): primero se mira sobre qué versión se hizo, porque suele ser una anterior a la que se le mandó; cada punto se comprueba en el Word vigente y en el informe se separa lo que «ya estaba corregido» de lo que se corrigió ahora. Si las fotos de los anexos muestran el logo o el nombre de una empresa que la tesis deja anónima, se difumina con PIL (pixelar y desenfocar solo esa zona, sin tocar las caras) y se reemplaza el blob de la imagen en el Word (Soledad Sonco y Karol Mamani, 19-oct-2026).
- **El cliente devuelve nuestro Word con sus cambios**: se compara párrafo a párrafo con la versión de la que partió (`difflib` sobre los textos). Si lo editó en Google Docs (etiquetas `goog_rdk` en `w:sdt`, campos que pasan de cientos a 3, tablas que faltan o capturas de pantalla en su lugar), no se trabaja sobre su archivo: sus cambios de contenido se meten en nuestro Word, que conserva índices, rótulos y tablas (Soledad Sonco y Karol Mamani, 21-oct-2026). Al añadir párrafos comparativos cada 3 antecedentes, se varía el cierre: con nueve terminando en «esta tesis… en una empresa de…» el molde salta a la vista.
- **«Las citas no aparecen»** suele querer decir que el texto nombra a un autor que no está en la
  bibliografía: un «Según X (1993), citado por Y» o una cita escrita a mano con otro año. Se deja
  solo la fuente que está en la lista. En un Word con Mendeley Cite no se usa `aplicar.py` (borra
  los controles de las citas): se cambia el texto de los `w:t` de los tramos sin cruzar un `w:sdt`,
  como en `trabajos/13-lander_ronda_obs.py` (Lander Lacuta, 21-oct-2026). «Los libros sin sus
  páginas» no se completa a ciegas: se le piden los PDF de los libros, se vuelcan a texto (con la
  página impresa, no la del PDF) y se reparten las citas entre agentes que devuelven la página y la
  cita textual. Si un libro no llega, la cita se cambia a otro libro recibido que diga lo mismo; si
  la frase trae un dato que ningún libro dice (una cifra, una lista), se quita ese dato. Así quedaron
  71 citas con página en la tesis de Lander (21-oct-2026).
- **Observaciones del asesor o del jurado**: se leen (captura, PDF o Word con comentarios), se
  responde una por una en una tabla (observación, qué se hizo, dónde quedó) y se corrige. Una
  primera ronda de observaciones entra en el precio; a partir de la segunda, o si piden algo
  que no se cotizó, se avisa a Benicio para que decida si cobra.

Antes de aplicar una ronda se comprueba que el Word de `02-corregida` sea el que el cliente
leyó: si sus observaciones citan frases que no están ahí, lo que recibió fue la versión
humanizada de `tesis-turnitin\<nn>\Listo` (va sin carátula ni anexos). Entonces se funde primero
ese cuerpo en el Word completo, párrafo a párrafo (mismos números con un desfase fijo), y las
correcciones se aplican sobre el resultado. Así pasó con Josué Silva el 12-oct-2026.

Cuando Benicio dice que el humanizado de `Listo` «ya está, pero le falta carátula, índice y
anexos», el encargo es esa misma fusión: el cuerpo humanizado entra en el Word completo, que va
a `02-corregida` con su PDF, y el cuerpo solo queda en `03-turnitin`. Si en `02-corregida` ya no
está el Word completo (lo pisó el humanizado), se busca en la papelera con
`(New-Object -ComObject Shell.Application).Namespace(10).Items()` y se copia desde ahí sin
restaurarlo. Antes de fundir se comprueba que cada párrafo del Word completo sea igual al de la
versión de `03-turnitin` anterior a humanizar; después se quitan los párrafos vacíos que dejen
una hoja en blanco antes de los anexos y se actualiza el índice. Así se hizo con Luna el
12-oct-2026.

Si piden que los números no se separen de su palabra al final de la línea («44 observaciones»,
«40,9 %», «ρ = 0,792»), se cambian esos espacios por el de no separación (U+00A0) y el guion
de «KR-20» o «II-2» por `<w:noBreakHyphen/>`, solo del resumen a las recomendaciones. El
carácter U+2060 no sirve: Word corta igual y cambia el alto de la línea.

La salida de `indice.ps1` no se corta con `Select-Object -First`: mata el script antes de
guardar, Word queda abierto con el documento y la siguiente apertura se cuelga. Si pasa, se
cierran los Word sin ventana, se borra el `~$…docx` y se actualiza sobre una copia.

Cuando el cliente manda sus notas del pretest y postest (Excel con columnas SI/NO por ítem), los
resultados se recalculan con R desde los ítems y no desde sus «promedios» redondeados (0,3; 0,6):
con los redondeos cambian los empates y el Z de Wilcoxon sale distinto. Se comprueba también el
KR-20 que declara la tesis; si con sus datos no sale, no se corrige ni se inventa: queda en
amarillo y se le pregunta de qué piloto viene. Cuando mande el sustento (captura, salida `.spv`
y base `.sav` de SPSS), el `.sav` se lee con R (`haven::read_sav`) y se recalcula: si el valor
sale, se quita el amarillo y el texto queda tal cual. Se mira además el N de la salida, si esos
casos son los niños del estudio (se comparan fila por fila con el Excel de notas) y la fecha de
creación del `.spv` (está en el XML de dentro del zip); si son otros casos, se le dice a Benicio,
porque la tesis tendrá que decir que fue una prueba piloto y con cuántos.

Si los datos llegan como informes de laboratorio en PDF, uno por animal (VetScan HM5 y SKYLA en
veterinaria), `python <skill>/scripts/laboratorio_vet.py <carpeta con las dos subcarpetas> <salida.csv>`
los pasa a una tabla. Antes de calcular se cruzan hemograma y bioquímica del mismo animal: nombre,
sexo (el VetScan distingue castrado, la bioquímica no) y fecha de la prueba, porque un hemograma de
otra fecha no es de la misma toma (Lander Lacuta, 17-oct-2026: 2 sexos cruzados y 3 fechas distintas).

Antes de calcular con la base del cliente se buscan en todo el Excel (celdas, títulos, comentarios)
«simulado», «ficticio», «ejemplo» o códigos como `SIM-…`: con Renzo Cruz (15-oct-2026) el postest venía
rotulado «SIMULADO» y se paró a preguntar. Si el cliente confirma que son datos reales, se trabaja con
ellos y se le pide quitar la etiqueta y poner los expedientes reales; nunca se redacta como real algo que
el propio archivo marca como simulado. Al rehacer un capítulo de resultados se procura dejar el mismo
número de tablas, para no correr la numeración de los anexos.

Y se compara el Word con el PDF que mandó antes,
porque pueden no ser la misma versión (a Maritza Rodríguez le faltaba la dedicatoria en el Word,
12-oct-2026). Las tablas nuevas hechas con python-docx necesitan ancho (`tblW` en pct 5000) y
`tblLook` con `noHBand`, o salen angostas y con franjas grises.

## Lo que no se hace nunca

- Inventar fuentes, datos, resultados, validaciones de expertos o un alfa de Cronbach.
  Si el cliente no tiene datos, el capítulo de resultados no se escribe: se cotiza el análisis
  cuando los tenga.
- Trucos contra el detector: letras de otro alfabeto, texto blanco, espacios raros. Turnitin
  lo reporta como manipulación.
- Prometer un porcentaje, una nota o una aprobación.
- Subir el trabajo de un cliente al conector: la cuenta conectada es de otro tesista.
- Modificar o borrar lo que mandó el cliente.

## Mantener la skill

Cada uso la mejora. Si aparece una guía con una regla que los scripts no cuentan, un formato
que `leer.py` no entiende, un tipo de trabajo sin renglón en `precios.md` o un precio que
Benicio corrige, se actualiza en ese mismo trabajo (SKILL.md, scripts, `precios.md` o
`references/`) y al final se le dice en una línea qué se añadió.

Tesis cuantitativa de pregrado UCV con base de datos (Pamela Hinostroza y Noemi Mamani, 22-oct-2026): antes de tocar los resultados se reproducen con la base los números del Word (alfa, rho, D de Lilliefors, frecuencias por nivel). En ese caso salieron todos, y de ahí se vio que la tesista había sumado mal dos dimensiones (representación fiel con los ítems 12-13 y verificabilidad con 14-17, cuando su propia tabla de ítems dice 12-14 y 15-17) y que los niveles de la variable 2 usaban cortes distintos de los de la variable 1. La agrupación correcta se saca de la tabla ítem-indicador del Anexo 2, no del texto. Los 14 cuadros, las 12 figuras y las 4 correlaciones se rehacen con `elem24`/`figuras24` (en `trabajos/24-hinostroza/`, con `stats24.py`, `build24.py` y el resto del armado: guardan tablas APA con línea arriba, abajo y bajo el encabezado, rótulo «Tabla N»/título en cursiva en dos párrafos y figuras con X = control, Y = dimensión). Para los datos se añade siempre un Anexo con la sintaxis de SPSS, la base anonimizada y el diccionario (lo pide la UCV). Si el Word por COM falla con «servidor RPC no disponible» justo después de matar un Word oculto, el siguiente intento suele funcionar; el primero tras `Stop-Process` falla siempre.
