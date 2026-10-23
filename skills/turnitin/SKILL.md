---
name: turnitin
description: Trabaja los documentos de las carpetas tesis-turnitin y tesis-asesorar del usuario. Pregunta si hay que humanizar (bajar el porcentaje de IA) o bajar la similitud, de cuál de las dos carpetas y en qué subcarpeta (01-Katy Manuelita Pazos Llenque, Diana Maribel Silva Nicolas…), lee el Word y el reporte de Turnitin que corresponde sin que se lo indiquen, reescribe solo lo marcado y deja el Word completo para el tesista en Listo y la copia recortada en «Subir a Turnitin» (tesis-turnitin), o todo en 03-turnitin (tesis-asesorar), sin cambiar la organización de la carpeta. La meta de IA es siempre 0 % («*%» no vale) y todo Word sale humanizado con el humanizador-academico, aunque solo se pida similitud. Úsala cuando el usuario escriba /turnitin, o diga «humaniza el de la carpeta», «bájale la IA al 02», «baja la similitud del artículo», «ya puse el reporte», «mira el reporte nuevo», «ordena la carpeta», «borra lo obsoleto» o nombre una subcarpeta de tesis-turnitin, aunque no diga la palabra Turnitin.
---

# Turnitin: humanizar o bajar similitud desde la carpeta

El usuario baja el porcentaje de IA y de similitud a trabajos académicos ajenos (tesis,
artículos) y los entrega pasados por Turnitin. Viven en dos raíces, `tesis-turnitin` y
`tesis-asesorar`, cada una con su organización fija, de modo que nunca hace falta que diga
dónde está el Word ni cuál es el reporte: eso lo averigua la skill.

Quiere rapidez. No se le pide aprobación párrafo por párrafo ni se le muestra el antes y el
después; se trabaja de corrido y se le informa al final. Se le responde siempre en español.

**La meta de IA es siempre 0 %, en todo trabajo** (lo pidió el 14-oct-2026). Esto no se
pregunta ni hace falta que lo diga:

- **«*%» no es un resultado.** Un reporte de IA en «*%» (o en cualquier número por encima de
  0) quiere decir que hay que seguir. No se da por terminado, no se entrega «Envía al tesista»
  y no se presenta como «ya casi»: se sigue la Ruta 0 % (Paso 3A).
- **Todo Word que sale de esta skill pasa por el `humanizador-academico`**, aunque solo se haya
  pedido similitud. Se quitan los patrones de IA sin que haya que pedirlo (ver el final del
  Paso 3B).

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
<TURNITIN>\
└── 10-Roy Christian Carbajal Huicho\   una subcarpeta por persona, con su nombre completo
    ├── actual\             el Word tal como llegó. No se modifica nunca.
    ├── Listo\              el Word completo ya trabajado: es el que se envía al tesista.
    ├── Subir a Turnitin\   la copia recortada (sin carátula, índices ni anexos) que sube el usuario.
    └── reportes\           los PDF de Turnitin, que coloca el usuario
        ├── ia\
        └── similitud\
```

**Dos salidas, cada una en su carpeta** (lo pidió el 12-oct-2026). La skill solo escribe en
`Listo` y en `Subir a Turnitin`:

- `Listo` lleva el documento completo, con su carátula, índices y anexos, y con el texto ya
  reescrito. Es lo que el usuario le manda al tesista. Ahí no va ningún recortado.
- `Subir a Turnitin` lleva el mismo documento pasado por `para_turnitin.py`, con el mismo
  nombre más ` - para Turnitin`. Es lo único que se sube.

Cada vez que se escribe una versión en `Listo` se genera su gemela en `Subir a Turnitin`:

```
python <skill>/scripts/para_turnitin.py "<Listo\salida.docx>" "<Subir a Turnitin\salida - para Turnitin.docx>"
```

El reporte que vuelve analizó la gemela recortada, pero **se reescribe siempre sobre el Word
completo** (su gemelo de `Listo`, o el de `actual` en la primera ronda): los scripts de marcado
cruzan por el texto, así que lo resaltado se encuentra igual, y de ese modo el tesista nunca
pierde carátula ni anexos. `estado.py` lista las tres carpetas y puede decir que el reporte
corresponde al de `Subir a Turnitin`; el Word de trabajo es entonces el del mismo nombre, sin
` - para Turnitin`, en `Listo`.

Las carpetas con la organización de asesoría no tienen `Subir a Turnitin`: ahí el recortado se
queda en `03-turnitin`, al lado, como hasta ahora.

### La otra raíz: tesis-asesorar

Los clientes de asesoría (skill `/asesorar`) tienen otra organización, y **se queda como
está**: no se crea `actual`, `Listo` ni `reportes`, no se mueve nada y no se corre `ordenar.py`
ni `limpiar.py` (los dos se niegan solos).

```
<ASESORAR>\
└── 04-Diana Maribel Silva Nicolas\
    ├── 01-original\            no se toca
    ├── 02-corregida\           no se toca
    ├── 03-turnitin\            el Word que se pasó por Turnitin, y aquí mismo la salida
    ├── 04-revision\            no se toca
    └── 05-pasadoporturnitin\   los reportes, de IA y de similitud juntos
```

Todo lo que el resto de esta skill dice de `actual` y de `Listo` vale aquí para `03-turnitin`,
y lo que dice de `reportes`, para `05-pasadoporturnitin`:

- El Word de entrada es el de `03-turnitin` que el reporte analizó, y no se modifica.
- La salida se escribe en `03-turnitin`, al lado, con el sufijo de siempre
  (`<nombre> - humanizado.docx`, ` - similitud.docx`, y el número en las rondas siguientes).
  No se sobrescribe nada ni se manda nada a `borrar\`: llevar el resultado a `02-corregida`
  es trabajo de `/asesorar`.
- El tipo de cada reporte sale de lo que dice el PDF, no de su nombre ni de una subcarpeta.
- Ningún reporte se quita por iniciativa propia. **Si él pide «borra lo obsoleto»** (lo pidió
  el 13-oct-2026, con Elisai: nueve reportes de rondas anteriores), en `05-pasadoporturnitin`
  se deja solo el reporte más reciente de IA y el más reciente de similitud, y los demás van a
  la Papelera de reciclaje (`Microsoft.VisualBasic.FileIO.FileSystem.DeleteFile` con
  `SendToRecycleBin`; `limpiar.py` aquí no corre). Antes se comprueba que los porcentajes de
  cada ronda estén anotados en la bitácora de `cotizacion.md`. No se toca ningún Word.
- **Lo que se le manda al cliente va junto en `06-enviar`** (lo pidió el 13-oct-2026): cuando
  una ronda cambia el Word completo de `02-corregida` o llega un reporte que ya da el resultado
  buscado, se rehace esa carpeta como dice la skill `/asesorar` (Word completo y su PDF,
  archivos aparte, informe de revisión y los reportes válidos con nombre claro), y la línea
  «📨 Envía al tesista» nombra esa carpeta, no un archivo suelto. Un reporte de similitud con
  filtros distintos de los de la universidad no entra.

**Documento de más de 30 000 palabras en dos partes** (Eduardo Sime, 17-oct-2026): Turnitin no mide la IA por encima de
30 000, así que se sube en `_parte1` y `_parte2`. Los cuatro reportes se cruzan con `marcado_ia.py` y
`marcado_similitud_clasico.py` directamente contra el Word completo de `02-corregida` (copiado al scratchpad), que
encuentra el texto de las dos partes; se trabaja y se aplica sobre ese Word y se vuelven a sacar las partes. Si el
Word tiene números de página escritos (cuadros del Anexo con «p. N»), se rehacen tras actualizar el índice, porque
la reescritura mueve las páginas.

A los scripts se les pasa la carpeta como `asesorar\Diana Maribel Silva Nicolas` (o la ruta completa):
`python <skill>/scripts/estado.py "asesorar\Diana Maribel Silva Nicolas"`.

**La misma regla vale para una carpeta de `tesis-turnitin` que llegó con esa organización**
(copiada de asesoría, con `03-turnitin` y sin `actual`): se trabaja igual, sin reordenarla.
`estado.py` lo detecta solo y lo dice en su segunda línea. `08-Diana Maribel Silva Nicolas` es la excepción: se
reordenó a mano el 12-oct-2026, antes de esta regla, y sigue con `actual` y `Listo`.

### Ponerle a la carpeta el nombre completo de la persona

Las subcarpetas de las **dos raíces** se llaman por la persona dueña del documento, con su
nombre completo (todos los nombres y los dos apellidos), no por el tipo de trabajo ni por un
apodo: en `tesis-turnitin` es `NN-Nombres Apellidos` (se conserva el número con que empieza) y
en `tesis-asesorar` es `NN-Nombres Apellidos - WhatsApp` (numerada también desde el 17-oct-2026,
por fecha de creación; una nueva lleva el siguiente número libre, que pone `nombrar.py`). Así el registro de trabajos queda por
persona (lo pidió el 14-oct-2026; ese día se renombraron las diez de `tesis-turnitin` y las de
`tesis-asesorar` que tenían apodo: `Luna` pasó a `Diana Maribel Silva Nicolas`, `josue-silva` a
`Josué Segundo Silva Ora`, `renzo` a `Renzo Rodrigo Cruz Huamani`). Con dos autores van los dos
unidos por «y» (`05-Analiz Curasma Solano y Karen Garcia Sanchez`). La misma regla está en la
skill `/asesorar`, que la aplica al cotizar.

Cuando el usuario no sabe todavía de quién es, crea la carpeta como `NN-cambiarnombre` (o con
un apodo) y suelta el Word dentro. La skill le pone el nombre sin preguntar, **antes de ordenar**:

```
python <skill>/scripts/nombrar.py 10-cambiarnombre
python <skill>/scripts/nombrar.py "asesorar\Luna" --forzar      una de asesoría con apodo
```

El nombre sale, en este orden, de la línea «Cliente:» de `cotizacion.md` (la escribe
`/asesorar` y es la fuente más fiable; también entiende «la autora que figura en la carátula
es …»), de la carátula del Word (AUTOR, Autora:, Tesista, «1.2 Investigadores», Presentado
por…; entiende «Apellidos, Nombres» y también «Nombres, Apellidos») y, por último, de las
propiedades del archivo, que solo valen si coinciden con el nombre de la carpeta o del archivo,
porque suelen traer al dueño de la plantilla (en Irwin decían «Gonzalo Carrillo»). Descarta los
rótulos de plantilla («Apellidos, Nombres»). Si no lo encuentra, no renombra y lo dice: entonces
se mira a mano, y la portada del reporte de Turnitin es otra fuente (en 02 dio «Alejandra
Milagros Sosa Enciso», que el Word no traía); se renombra con `--forzar` o a mano y se le avisa
al usuario de dónde salió el nombre. Solo renombra carpetas que se llamen «cambiarnombre», salvo
con `--forzar`; `--ver` enseña el nombre que pondría. En el informe se dice en una línea cómo
quedó. A partir de ahí, todos los comandos, la memoria y el informe usan el nombre nuevo, y la
línea «Cliente:» de `cotizacion.md` lleva el mismo nombre completo. Si el nombre completo se
conoce después (el cliente lo dice por WhatsApp, llega la carátula), se renombra en ese momento.

### Ordenar la carpeta, siempre antes de mirar el estado

El usuario suele crear la subcarpeta y soltar dentro los Word tal cual (así llegó `06-Paula Andrea Vanegas Rincón`,
con tres Word en la raíz y ninguna subcarpeta). La skill la deja como las demás sin preguntar:

```
python <skill>/scripts/ordenar.py 06-Paula Andrea Vanegas Rincón
```

Crea `actual`, `Listo`, `Subir a Turnitin` y `reportes\ia|similitud` si faltan, y coloca cada
archivo suelto: los Word en `actual` (en `Listo` si ya son una salida ` - humanizado` o
` - similitud`, y en `Subir a Turnitin` si terminan en ` - para Turnitin`, también los que
quedaron en `Listo` de antes), y cada PDF
según lo que dice dentro, no por su nombre: reporte de IA a `reportes\ia`, de similitud a
`reportes\similitud`, y el que no es de Turnitin a `actual`, porque es el documento del
cliente. También recoloca los reportes sueltos en `reportes` o metidos en la subcarpeta del
otro tipo. Respeta las carpetas viejas (`reporte`, mayúsculas) en vez de duplicarlas.

Solo mueve: no borra, no renombra y no sobrescribe; si en el destino ya hay un archivo con ese
nombre, lo deja donde está y lo dice. Lo que no es Word ni PDF se queda en su sitio. Con
`--ver` enseña lo que haría sin mover nada. Al usuario se le dice en una línea qué se movió.

Esto es solo para las carpetas de `tesis-turnitin` con archivos sueltos o con su organización
propia. Las de asesoría (ver arriba) no se ordenan.

Se corre al empezar cualquier trabajo, y también solo, cuando pide «ordena la carpeta» sin
pedir nada más. Una carpeta puede traer varios trabajos (los tres de `06-Paula Andrea Vanegas Rincón`): todos van a
`actual` y cada reporte se empareja después con su Word en el paso 2.

### Quitar los reportes obsoletos

Cuando el usuario vuelve con el reporte nuevo, el anterior del mismo trabajo y del mismo tipo
ya no sirve y estorba: confunde cuál manda. Después de ordenar y de mirar el estado se corre:

```
python <skill>/scripts/limpiar.py 06-Paula Andrea Vanegas Rincón
```

De cada trabajo y tipo (IA, similitud) deja solo el reporte más reciente y manda los
anteriores a la Papelera de reciclaje, de donde se pueden restaurar. Agrupa por el Word que
Turnitin analizó, sin el sufijo ` - humanizado` o ` - similitud`, así que el reporte del
original y el del humanizado cuentan como el mismo trabajo. No toca ningún Word (ni los de
`actual` ni las versiones de `Listo`) ni el reporte del otro tipo. `--ver` enseña lo que
quitaría sin quitar nada.

Antes de correrlo, el porcentaje del reporte que se va se anota en la memoria del proyecto y
se le dice al usuario en el informe («IA 75 % → *%»): es el «antes» de la comparación y
después ya no estará en la carpeta. Se le dice en una línea qué se quitó. También se corre
solo cuando pide «borra lo obsoleto» o «limpia la carpeta».

### Dejar el Word listo para subir, sin reporte todavía

Cuando el trabajo llega sin ningún reporte y el usuario pide «ubícala para subirla», «quítale
lo que no va en Turnitin» o «prepárala para Turnitin», no se reescribe nada:

```
python <skill>/scripts/para_turnitin.py "<actual\word.docx>" "<Subir a Turnitin\word - para Turnitin.docx>"
```

Quita las páginas preliminares (carátulas, jurado, declaratoria, ficha, dedicatoria,
agradecimientos, índices) y los anexos, y conserva del resumen a las referencias con sus
tablas y figuras. Busca el inicio en el título RESUMEN (o INTRODUCCIÓN / CAPÍTULO I / GENERALIDADES, que es como arranca un proyecto de tesis) y el
final en el título ANEXOS; `--ver` dice cuántas palabras quitaría sin guardar. Las referencias
se quedan y se descuentan con «Excluir bibliografía». Los reportes que vuelvan analizarán ese
archivo de `Subir a Turnitin`, y las rondas siguientes se trabajan sobre el Word completo de
`actual` (ver «Dos salidas»).

**Mirar siempre qué subió el cliente y cortar igual** (15-Karla y Rosmery, 18-oct-2026). Si el índice va DESPUÉS
del resumen, `para_turnitin.py` lo deja dentro (allí 1 621 palabras), y si los anexos empiezan con «ANEXO 1:» sin
un título «ANEXOS», no los quita. La primera gemela salió con 19 078 palabras cuando el cliente había subido 14 245
(solo Introducción → Recomendaciones). Antes de la primera salida se leen las primeras y últimas páginas del
reporte del cliente (PyMuPDF) y la gemela se corta con `partir.py` en esos mismos párrafos, comprobando el primero y
el último.

## Paso 1: preguntar qué y dónde

Antes de preguntar se listan las subcarpetas de las dos raíces, con su fecha (no se asumen de
memoria). Después, con una sola llamada a AskUserQuestion, tres preguntas:

1. **Qué necesita**: «Humanizar (bajar IA)», «Bajar similitud» o «Las dos». «Bajar
   similitud» también termina con la pasada de IA hacia 0 %. Lo que cambia es dónde se pone
   el esfuerzo, no si se humaniza.
2. **De cuál carpeta**: «tesis-turnitin» o «tesis-asesorar». De la respuesta depende la
   organización que se respeta (ver «La carpeta»).
3. **Qué trabajo**: las subcarpetas más recientes, hasta cuatro, mezclando las dos raíces y con
   la raíz dicha en la descripción de cada opción («Diana Maribel Silva Nicolas · tesis-asesorar»); él escribe otra
   si no está. Si el nombre que elige o escribe solo existe en una raíz, esa manda aunque en
   la pregunta 2 haya marcado la otra; si existe en las dos, manda la pregunta 2.

4. **Solo si pidió similitud y no lo ha dicho: qué porcentaje exige la universidad.** Cambia el
   plan entero: con el número se sabe cuántas palabras hay que quitar (cada punto son las
   palabras del documento, sin bibliografía, entre 100) y si hace falta usar las jugadas
   fuertes desde la primera ronda. En la primera tesis se supo en la cuarta ronda que era
   «menos de 18» y se perdieron tres vueltas.

Se salta la pregunta que el usuario ya contestó en su mensaje («humaniza el 02» contesta las
tres, porque `02` solo existe en `tesis-turnitin`; «bájale la IA al de Luna de asesorar»
también). Si ya dijo todo, no se pregunta nada.

## Paso 2: ordenar y ver el estado

```
python <skill>/scripts/nombrar.py 10-cambiarnombre     (solo si se llama «cambiarnombre» o tiene apodo)
python <skill>/scripts/ordenar.py 10-Roy Christian Carbajal Huicho
python <skill>/scripts/estado.py 10-Roy Christian Carbajal Huicho
python <skill>/scripts/limpiar.py 10-Roy Christian Carbajal Huicho
```

(`limpiar.py` va después de `estado.py`, para haber visto y anotado el porcentaje anterior.
Y si el reporte de IA que se va a quitar es el primero con marcas, antes se guarda su
`primer-reporte.json`, como dice el paso 0 de la Ruta 0 %: sin él no se sabe qué era limpio.)

En una carpeta con la organización de asesoría solo se corre `estado.py "asesorar\<cliente>"`:
no se ordena ni se limpia.

Devuelve los Word de `actual` y `Listo`, y cada reporte con su tipo, su porcentaje, la fecha de
entrega, el archivo que Turnitin analizó y **a qué Word de la carpeta corresponde**. Con eso se
decide sin preguntar:

- **Reporte que manda**: el más reciente del tipo pedido.
- **Word sobre el que se trabaja**: el que ese reporte analizó. En la primera ronda es el de
  `actual`; en las siguientes es el último de `Listo`, porque el usuario ya lo pasó por
  Turnitin. Nunca se trabaja sobre un Word de otra versión que la que el reporte analizó: lo
  marcado no coincidiría. Si lo analizado fue el recortado de `Subir a Turnitin`, se trabaja
  sobre su gemelo completo de `Listo`, que tiene el mismo texto (ver «Dos salidas»).
- **Nombre de salida**, siempre en `Listo` (en `03-turnitin` si la carpeta tiene la
  organización de asesoría): `<nombre original> - humanizado.docx` para IA y
  `<nombre original> - similitud.docx` para similitud; en rondas siguientes se añade el número
  (` - humanizado 2.docx`). No se sobrescribe una versión anterior.

Hay que detenerse y decírselo al usuario, en una línea, solo en estos casos:

- No hay reporte del tipo pedido. Sin reporte no se trabaja a ciegas: se le pide que lo coloque.
- El reporte más reciente ya da el resultado buscado. **Para IA el resultado buscado es siempre
  0 %** (lo dijo el 14-oct-2026: «Siempre los necesito en 0%»): un reporte en «*%» (menos de
  20 %, sin nada resaltado) no termina el trabajo ni se pregunta; se sigue la Ruta 0 % (Paso 3A)
  sobre el último Word de `Listo`. Solo con 0 % se le dice que ese
  trabajo ya está y no se toca.
- El reporte no corresponde a ningún Word de la carpeta.

**Cuando el cliente subió su propia mezcla y su Word no está.** Pasó con `02-Alejandra Milagros Sosa Enciso`: la
clienta armó un archivo con trozos del humanizado y trozos del original, lo subió a la
universidad y el usuario solo trajo los reportes. Se le pide el Word una vez; si vuelve a
llamar la skill sin ponerlo, no se insiste: el cuerpo se reconstruye desde el texto del propio
reporte (PyMuPDF) sobre una copia del Word de `actual` en el scratchpad, con `aplicar.py` y
`"forzar": true`, y se comprueba que `marcado_ia.py` encuentra todas las palabras resaltadas.
Sobre esa base se trabaja como siempre y la salida se llama `<archivo del cliente> -
humanizado.docx`. En el informe se dice que es solo el cuerpo: carátula y referencias las pone
el cliente, y tiene que pegar el cuerpo entero, sin volver a mezclar.

Si pidió «las dos», va primero la similitud y después la IA, las dos sobre el mismo Word y con
una sola salida. El orden importa porque bajar similitud reescribe más texto, y lo que se
reescribe puede volver a marcarse como IA.

## Paso 3A: humanizar (IA) por la Ruta 0 %

**Se lee y se sigue `references/ruta-ia-cero.md`**, el único protocolo para la IA, sin
excepciones por caso. Resumido:

0. Antes de `limpiar.py`, el primer reporte con marcas se guarda como
   `reportes\ia\primer-reporte.json` (en asesoría, `05-pasadoporturnitin\primer-reporte.json`).
   Ese archivo no se borra nunca.
1. Ronda 1 en una sola pasada: lo limpio no se toca (si hay similitud, solo cirugía mínima de
   tramos). Lo marcado se reescribe una vez desde la idea con la voz del propio autor, y desde
   esta ronda entran los enunciados, las notas, las celdas y los párrafos cortos marcados. Se
   rompe la plantilla de los párrafos hermanos.
2. Cierre que hace la sesión principal: dos pasadas sobre el documento entero,
   `repeticiones.py`, lectura línea por línea y `control_cero.py` con el primer reporte. Si
   dice NO ENTREGAR, no se entrega.
3. Si vuelve en «*%», la ruta dice qué mirar y en qué orden. En la ronda 3 se empieza de cero
   lo marcado. Después de eso se le ofrecen caminos al usuario en lugar de seguir a ciegas.

Sin bloques ni aprobación: las fichas y la relectura se hacen, pero no se muestran. La
excepción es cuando el usuario pide el humanizador «por bloques»: entonces cada bloque se
muestra después de leer línea por línea sus oraciones nuevas junto a las vecinas.

**La voz del usuario.** Antes de reescribir se lee `<skill>/voz.md`, con las reglas de uso que
trae el propio archivo. Cuando el usuario dé frases nuevas, o corrija una reescritura con sus
palabras, se añaden a ese archivo en el momento. La voz del propio autor (`voz_tesista.txt`)
va antes que la del usuario.

La historia de cada caso, con todo lo que se probó, está en `references/casos-ia.md`.

**Cuando el usuario trae el Word del conector.** El conector humaniza lo que él le sube, que es
el recortado de `Subir a Turnitin`. Si vuelve con ese Word y su reporte, el recortado tiene los
mismos párrafos que su gemelo completo de `Listo`, corridos un número fijo (en Roy fueron 27,
los de la carátula). Se comprueba que todos los párrafos sin cambios coinciden con ese
desfase. Después se pasan los párrafos cambiados al Word completo con `aplicar.py` (párrafo
entero, sin `viejo`), se corre `restaurar_rotulos.py` y se vuelve a correr `para_turnitin.py`.
El recortado tiene que salir idéntico al que trajo, párrafo a párrafo. Si el conector pasó una
cita de narrativa a parentética y conservó autor y año, `aplicar.py` lo frena; se revisa y se
pasa con `forzar`. El Word del conector, que es el que se midió, se guarda en
`Subir a Turnitin` con el nombre de la gemela.

## Paso 3B: bajar similitud

Aquí está integrado el método de la skill `bajar-similitud`: sus fases, sus scripts y sus dos
referencias viven dentro de esta skill, así que no hace falta cargarla. Se sigue en este orden.
Lo único que cambia respecto de ella es la forma de entregar: de corrido, sin pedir aprobación
por bloque, y con la salida en `Listo`.

### Qué se arregla escribiendo y qué no

Un porcentaje alto tiene tres causas y solo una se baja reescribiendo:

- **Copia real**: texto tomado de una fuente sin comillas ni cita. Se arregla citando bien, no
  parafraseando.
- **Saturación temática**: el trabajo dice cosas comunes de la forma común del campo. Esto sí
  se baja reescribiendo.
- **Estructura obligatoria**: variables, términos, encabezados normados, enunciados de la
  matriz. No se toca, y es lo que fija el piso.

**Regla que no se negocia: nunca se parafrasea una cita textual para que deje de coincidir.**
Lo que va entre comillas con su cita se queda igual; se baja con el filtro «Excluir citas». Las
citas del cuerpo tampoco se borran. Un tramo largo que parece copiado literal y no lleva
comillas se le señala al usuario antes de tocarlo.

### Fase 1: anatomía del informe

```
python <skill>/scripts/informe.py <reporte.pdf> --meta 18
```

Sirve para los dos formatos. Da el porcentaje y su desglose, los filtros, el número de fuentes
y las que más pesan, si es **mosaico** (muchas fuentes pequeñas: no hay nada copiado y
reescribir rinde poco) o **bloque** (una fuente con 8 % o más: ir a buscarla al cuerpo antes
que nada), y con `--meta` cuántas palabras coincidentes hay que quitar. `--meta` es el
porcentaje que el usuario dijo en el paso 1.

**Dos reportes del mismo texto con porcentajes distintos.** Pasa cuando el usuario lo sube a su
cuenta y el cliente a la de su universidad: un artículo dio 16 % en una y 22 % en la otra el
mismo día. Manda siempre el de la cuenta de la universidad (se reconoce porque la portada trae
el curso y la tarea). La diferencia sale de la base de comparación (23 fuentes contra 13), de
la carátula que el cliente añade y de los filtros; las referencias, si están excluidas, no
llevan marcas y no son la causa. Se trabaja sobre el Word de la carpeta aunque el cliente haya
subido otro archivo, si el cuerpo coincide. Si `informe.py` dice «Falta pdftotext» con un
reporte nuevo, la portada y la lista de fuentes se leen con PyMuPDF (`pymupdf`), que sí está.

**Otra cuenta, otra base, otras marcas.** En 11-Claudia el primer reporte (39 %) no marcaba el
marco teórico de insectos, y el de otra cuenta (34 %, reporte clásico) lo marcó casi entero,
porque su base incluía pdfcoffee, museocostarica e insectopedia. Cuando llega el reporte de una
cuenta nueva se cruza otra vez el Word entero con él, no solo lo ya trabajado, y las rondas
siguientes trabajan contra los dos `ms*.json` a la vez.

Si hay un informe anterior, **antes de decir que bajó** se comparan identificador de entrega,
filtros, número de fuentes y palabras totales. Dos informes de cuentas o filtros distintos no
son un antes y un después, y hay que decírselo. El detalle de cada campo y de los filtros está
en `references/informe-turnitin.md`.

### Fase 2: errores de fondo, que se reportan y no se corrigen

Se miran antes de reescribir y van en el informe final, porque son decisión del autor y es lo
que el jurado ve primero:

- citas del cuerpo que no están en la bibliografía, y números de referencia repetidos para
  autores distintos;
- comillas huérfanas, que suelen delatar una cita textual a medias;
- citas de segunda mano («X, citado por Y»);
- contradicciones de datos entre capítulos (lugar, año, tamaño de la población);
- referencias duplicadas.

### Fases 3 y 4: clasificar lo marcado y ver dónde se concentra

Lo marcado sale con el script que corresponde al formato. Reporte nuevo (el que trae texto):

```
python <skill>/scripts/marcado_similitud.py <reporte.pdf> <word.docx> <scratchpad>/ms.json
```

Reporte clásico (portada «por <nombre>», hojas del documento como foto, texto coincidente sobre
fondo pastel), leído con el OCR de Windows en español:

```
python <skill>/scripts/marcado_similitud_clasico.py <reporte.pdf> <word.docx> <scratchpad>/ms.json --por-hoja
```

Los dos dan, por párrafo y por oración, cuántas palabras coinciden, con el tramo coincidente
entre corchetes. `--por-hoja` añade cuántas palabras resaltadas hay en cada hoja, que es la
manera rápida de ver dónde vive el porcentaje. El clásico necesita los paquetes `winrt` (ya
instalados en este equipo; si faltan: `pip install winrt-runtime winrt-Windows.Media.Ocr
winrt-Windows.Graphics.Imaging winrt-Windows.Storage.Streams winrt-Windows.Globalization
winrt-Windows.Foundation winrt-Windows.Foundation.Collections`).

Con esa salida se reparte lo marcado en tres cubos y se cuentan las palabras de cada uno:

- **Intocable**: variables, términos técnicos, nombres de instituciones, encabezados, título,
  citas entre comillas, referencias.
- **Estructural repetido**: problema, objetivos, hipótesis y su copia en la matriz de
  consistencia. Variarlos lo decide el asesor; se cuantifica y se le presenta el dato.
- **Reescribible**: prosa que dice algo común de la forma común. Aquí se trabaja.

Si lo reescribible es menos que las palabras que pide la meta, se le dice **antes de empezar**:
la redacción sola no va a alcanzar y harán falta los filtros o las jugadas fuertes.

### Fase 5: reescribir, en una sola pasada a fondo

El usuario no quiere dar varias vueltas por Turnitin. En la primera tesis se necesitaron cuatro
rondas (25 → 23 → 21 → 19 %) porque cada una atacó un poco más que la anterior; todo se pudo
hacer en la primera. Por eso, desde la primera ronda:

1. Se reescribe **toda oración de prosa con 4 o más palabras coincidentes**, no solo las de
   tramo largo.
2. **Se cambia la estructura, no las palabras**: orden de la oración, sujeto, voz, dónde va la
   cita, dónde cae el corte entre oraciones. Ahí vive la coincidencia.
3. Para los tramos cortos, tres jugadas: cambiar el orden de una enumeración cuando el orden no
   significa nada (regiones, estructuras); sustituir el término repetido por «esta enfermedad»,
   «esta neoplasia» o el sinónimo que el propio documento ya usa; y pasar un sustantivo con
   «de» a verbo («actividades de promoción de la salud» → «actividades con las que se promueve
   la salud»). La sustitución del término se puede hacer en bloque sobre las oraciones
   marcadas: «cáncer de piel» → «cáncer cutáneo» rompió 22 tramos de una vez. Nunca en título,
   objetivos, hipótesis, variables ni definiciones.
4. **No cambian**: los términos técnicos donde son la variable, las citas, las cifras, el tiempo
   verbal y el número de párrafos. Los documentos convertidos desde PDF traen párrafos partidos
   a mitad de oración; se conserva la bisagra.
5. **Jugadas fuertes, solo cuando la meta no se alcanza con lo anterior**, y se le informan una
   por una porque quitan o mueven texto: quitar del cuerpo el título de una tesis o instrumento
   que ya está en las referencias, dejando autor, año y número de cita; quitar una enumeración
   que el documento ya dio antes («la regla ABCDE, ya explicada»); borrar el párrafo que
   duplica al siguiente (el original que quedó junto a su paráfrasis); y reescribir cómo se
   puntúa un instrumento («deficiente (0 a 8 puntos)» → «deficiente cuando se obtienen de 0 a 8
   puntos»).

**La doble restricción.** Al alejarse de la redacción estándar es fácil caer en prosa de
modelo, que sube el porcentaje de IA: aperturas con el mismo molde en párrafos seguidos, el
mismo verbo de atribución repetido («los autores concluyen» cuatro veces), tríadas paralelas,
gerundios colgados, cierres que no informan, y oraciones cortadas a propósito para mover un
número. El catálogo con ejemplos está en `references/patrones-al-reescribir.md` y se audita
antes de entregar:

```
python <skill>/scripts/auditar_patrones.py "<Listo\salida.docx>" --parrafos 125,127,129
```

También aquí se usa `voz.md`: sus enlaces («pero», «ya que», «para que», «además») antes que
los de manual.

### Fase 6: verificar, con bucle interno

1. Se vuelve a correr el script de marcado contra el Word de `Listo` y se rehace lo que siga
   coincidiendo en tramos de 7 o más palabras. Se entrega cuando los tramos largos que quedan
   son solo nombres, términos o enunciados fijos. Una reescritura propia también puede caer en
   la frase común de otra fuente («una de cada cinco personas tendrá cáncer de piel en algún
   momento de su vida»): se rehace con otra construcción.
   **Con el reporte clásico, contar por largo de tramo** (13-Pamela, 17-oct-2026). El cruce por OCR
   cuenta también fragmentos de 1 a 4 palabras («en las empresas comerciales») que Turnitin ya no
   resalta cuando la frase de la fuente se rompió. Por eso se suman aparte los tramos de 6 y de 8
   palabras o más de cada `ms*.json`, y se informa el rango entre esa cifra y la del cruce entero. En
   Pamela (39 %, tope de menos de 15 %, sin filtros), la ronda 1 dejó 2 755 palabras en el cuerpo
   pero solo 1 336 en tramos de 6 o más. La ronda 2 atacó solo esos tramos y además acortó la
   delimitación («en las empresas del sector comercial de Lima, periodo 2026») en los enunciados
   específicos, H0/H1 y sus repeticiones, sin tocar los enunciados generales. Así bajaron a 641.
   Antes de unir los JSON de los agentes se busca en cada párrafo reescrito un resto del texto
   viejo pegado al final. En Pamela, un `viejo` parcial dejó 98 palabras del original detrás de la
   reescritura.
   **Reescribir con las variables completas vuelve a coincidir** (17-Julio Llavilla, 20-oct-2026: 34 → 23 → 21 %,
   tope de menos de 15 %). En un tema con muchas tesis de las mismas variables, la ronda 2 cambió los enunciados a
   otra forma común («el clima de seguridad laboral se relaciona de forma positiva y significativa con…») y cuatro
   fuentes nuevas los marcaron: el resaltado solo bajó de 1 195 a 1 129 palabras. Desde la segunda ronda se nombra
   cada variable completa una vez por párrafo («ese clima», «esa conducta», «ambas variables») y se evitan las
   fórmulas del campo. Al quitar un índice con python-docx, el párrafo vacío de antes puede cerrar el campo del
   índice anterior (`fldChar end`): no se borra.
2. `python <skill>/scripts/verificar_cambios.py <antes.docx> <despues.docx>` comprueba el
   conteo de párrafos y que no se perdió ninguna cita ni cifra. Si se borró un párrafo
   duplicado, el conteo cambia y se explica.
3. **No se promete un número.** Lo que se puede decir es cuántas palabras coincidentes del
   reporte ya no están en el Word y cuántas pedía la meta. Límite de la medición: el cruce solo
   lee párrafos, así que las tablas del Word y las hojas apaisadas (la matriz de consistencia,
   que repite objetivos e hipótesis) cuentan para Turnitin y no para el script. **Se mira
   también el texto de las celdas** (`docx.Document(...).tables`): en 11-Claudia, la
   interpretación de la Tabla 7, que parecía faltar, estaba metida dentro de una celda con la
   fórmula vieja sin reescribir. La prosa de una celda se reescribe a mano con python-docx, y se
   le dice al usuario que conviene sacarla de la tabla.
4. **Párrafos con hipervínculo o con campo de cita** (`aplicar.py` dice «texto fuera de los
   tramos normales»): se editan a mano con python-docx cambiando solo los `w:r` sueltos, sin
   tocar el `w:hyperlink` ni el `w:sdt` de la cita, que en `.text` no aparece (en 11-Claudia,
   «Ibáñez  señala» llevaba el (2024) dentro de un `sdt`).
5. **Títulos de tesis citadas que no están en las referencias** (la jugada fuerte solo vale si
   la referencia existe): si el usuario lo autoriza, un agente busca cada tesis en su
   repositorio (ALICIA, handle), se añade la referencia APA 7 en su sitio alfabético, copiando
   el formato de una referencia vecina con el título en cursiva, y el título sale del cuerpo.
   En 11-Claudia salieron de paso tres citas mal hechas (un año distinto, y «Velasque e Isaac»,
   donde Isaac era el nombre de pila): se corrigen con `forzar` y se informan.

**Word con citas de Mendeley Cite** (Lander Lacuta, 18-oct-2026): las citas son controles `w:sdt` que
`p.text` no ve, y `aplicar.py` no puede reescribir esos párrafos sin perderlas. Se usa
`python <skill>/scripts/fichas.py <word> <ms.json> <salida> 4`, que vuelca cada párrafo marcado del cuerpo con
fichas `⟦C1|(Pérez, 2019)⟧` (cita) y `⟦F1|texto⟧` (formato propio: resaltado, negrita, cursiva) y lo reparte en
tramos, y `python <skill>/scripts/aplicar_fichas.py <entrada> <salida> cambios_h*.json [--probar]`, que exige
las mismas fichas y cifras y vuelve a poner el `w:sdt` original. Los agentes escriben el párrafo entero y
pueden mover las fichas. En Lander, 117 párrafos bajaron los tramos de 6 o más palabras de 1 508 a 356 en una
pasada, con las 162 citas intactas. Los títulos de tabla (rótulo con campo `SEQ`) se cambian aparte, en el
último `w:t` tras el salto de línea, y luego se corre `indice.ps1` de `/asesorar`.

### Fase 7: palancas que no son reescritura

Van siempre en el informe al usuario, para que las aplique antes de volver a pasar el
documento. En un mosaico rinden más que seguir escribiendo:

- **Filtros del informe.** `informe.py` dice cuáles están apagados. «Excluir coincidencias» de
  menos de 10 a 15 palabras elimina de golpe los tramos de terminología; «Excluir citas»
  descuenta lo que va entre comillas. Suelen mover varios puntos sin tocar el texto.
- **Autocoincidencia.** Si una entrega anterior quedó guardada en el repositorio de la
  universidad, la siguiente coincide consigo misma y el porcentaje se dispara. Avisarlo antes
  de una reentrega con depósito.
- **Los enunciados de la matriz.** Variar objetivos e hipótesis entre niveles, con permiso del
  asesor. Es la ganancia más grande que queda.

Lo que no se hace nunca: letras de otro alfabeto, texto blanco, espaciado alterado o palabras
invisibles. Turnitin lo detecta y lo reporta como manipulación, que es peor que el porcentaje,
y además es fraude.

### Fase 8: la pasada de IA, siempre (aunque solo pidiera similitud)

La meta de IA es 0 % también aquí, así que al terminar la similitud se carga el
`humanizador-academico` y se hace el Paso 3A sobre la salida de `Listo`, sin preguntar:

- Si hay reporte de IA, con sus marcas. Si da «*%» o no hay reporte, se sigue la Ruta 0 % (Paso 3A),
  y lo que el primer reporte con marcas dejó limpio no se toca.
- Siempre se pasan `auditar_patrones.py`, `cobertura.py` y `ficha.py` del humanizador sobre
  todo el cuerpo, no solo sobre lo reescrito. Se arregla todo patrón fuerte que aparezca.
- Después se vuelve a correr el marcado de similitud, para que la humanización no haya traído
  de vuelta tramos coincidentes (Fase 6, punto 1).

## Paso 4: escribir el Word

Las reescrituras van a un JSON y se aplican sobre una copia:

```
python <skill>/scripts/aplicar.py <word de entrada> <Listo\salida.docx> cambios.json
```

```json
[{"parrafo": 10, "viejo": "tramo exacto tal como está en el Word", "nuevo": "reescritura"}]
```

`viejo` es el tramo que se reemplaza; si se omite, se reemplaza el párrafo entero. En vez de
`viejo` se puede dar `"ini"`, que es cómo empieza la oración que se reemplaza (tiene que haber
una sola que empiece así en el párrafo); ahorra copiar la oración completa. El script conserva letra, tamaño y estilo, y **no guarda
nada** si algún cambio pierde o altera una cita o una cifra, o mete una raya larga. Cuando
falla, lo que está mal es la reescritura: se corrige y se vuelve a correr. `"forzar": true`
existe solo para una corrección deliberada que cambia una cifra o una cita, y esa corrección se
le informa al usuario.

**Rótulos en negrita.** Reemplazar el párrafo entero cuando empieza con un rótulo en negrita
(«Primera (Objetivo específico 1):», «Estadística descriptiva:») extiende la negrita a todo el
párrafo. En esos párrafos se da `viejo` con lo que sigue al rótulo, y antes de entregar se
corre `python <skill>/scripts/restaurar_rotulos.py <word de antes> <Listo\salida.docx>`, que
devuelve la negrita solo al rótulo y dice cuántos arregló.

Se edita siempre el documento original en vez de armar uno nuevo, para no perder tablas,
figuras, notas ni formato.

## Lo que no se toca

Citas, autores, años, cifras, tablas, títulos, notas de tabla y de figura, referencias, y todo
lo que vaya entre comillas. No entra ningún dato ni idea que el original no tenga, ni ninguna
falta de ortografía a propósito.

Las erratas y contradicciones del original se tratan así: las que caen dentro de un tramo
marcado se corrigen al reescribir y se le informan, para que pueda revertirlas; las que están
fuera se le listan y no se tocan.

## Paso 5: informar

Corto, y en este orden:

1. Dónde quedó el archivo, y que falta pasarlo por Turnitin. No se promete un porcentaje.
2. Una tabla breve: qué párrafos se tocaron y qué se hizo en cada uno.
3. Erratas corregidas dentro de lo marcado.
4. Erratas vistas fuera de lo marcado, sin tocar.

Si el usuario lleva memoria de proyecto, se anota la ronda (carpeta, porcentaje de partida y
qué se reescribió) para compararla cuando vuelva con el reporte nuevo. Cuando un trabajo
llega a 0 % de IA, o se cierra sin llegar, se añade su línea en `references/casos-ia.md`
(«Resultado por trabajo»): ronda en que salió, o la causa del «*%».

**Las dos últimas líneas de todo mensaje que deja un archivo listo son siempre estas**, al
final y sin nada después:

> 📤 **Sube a Turnitin:** `<ruta completa del archivo>`
> 📥 **Deja el reporte en:** `<ruta completa de la carpeta>`

La segunda dice dónde colocar el PDF que le devuelva Turnitin, sin que lo pida (lo pidió el
12-oct-2026). En `tesis-turnitin` es `<trabajo>\reportes\ia` o `<trabajo>\reportes\similitud`
según lo que se trabajó; si fueron las dos, se dan las dos carpetas en esa línea. En una carpeta
con la organización de asesoría es `<cliente>\05-pasadoporturnitin`, que recibe los dos tipos
juntos. Si la carpeta no existe, se crea antes de nombrarla. También se da esta línea, sola,
cuando la skill se detiene porque falta el reporte.

**El archivo que se sube va sin carátula, índices ni anexos** (lo recordó el
12-oct-2026, con `09-Samuel Auccahuaqui Rosa`), **salvo cuando la universidad pasa el
documento completo** (la UCV, o el tesista lo sube entero en su aula). Entonces se sube el Word
completo, con carátula, declaratorias, índices, referencias y anexos, y lo único que se le quita
es el logo de la universidad: `python <SKILLS>/asesorar/scripts/sin_logo.py
<Word completo> <copia para Turnitin>`, que borra solo las imágenes de la carátula. Esa copia es
la que se nombra en «Sube a Turnitin», y el Word para el tesista sigue con su logo (lo pidió
Benicio el 21-oct-2026, con Zulma Pacompia). Antes de informar se corre `para_turnitin.py` sobre la salida de
`Listo` y se deja la gemela en `Subir a Turnitin`; esa es la que se nombra en «Sube a
Turnitin». Cuando el reporte ya da el resultado buscado (IA en 0 %, nunca «*%», y la
similitud por debajo del tope de la universidad), el informe añade una tercera línea,
antes de las otras dos: «📨 **Envía al tesista:** `<ruta del Word de Listo>`».

**Cómo lo mide la universidad, dicho siempre** (lo pidió el 13-oct-2026, con Elisai Galarreta).
Un porcentaje solo vale si se sacó como lo saca la universidad. Antes de informar un resultado
de similitud se averigua, en este orden: lo que diga `cotizacion.md` o la memoria del trabajo,
la guía, la plantilla o la declaratoria que venga en la carpeta (la de la UCV dice «sin
filtros, ni exclusiones»), y el propio reporte, cuyos filtros lista `informe.py`. Y se le dice
al usuario en un párrafo corto: qué pide la universidad (con su frase textual y el tope), con
qué filtros salió el reporte que se está leyendo, y si el archivo analizado es el mismo que
subirá el cliente (cuerpo solo o documento completo con carátula y anexos). Si no coinciden, el
número no se da por bueno: se avisa que el de la universidad puede salir más alto y se le pide
una pasada más, del Word completo y con los filtros de la universidad, nombrando ese archivo en
«Sube a Turnitin». Si no se sabe qué pide la universidad, se dice que no se sabe y se le pide
que lo pregunte al cliente; no se supone que excluye la bibliografía.

Un solo archivo, con su ruta completa para que la copie. Si hay Word y PDF, se nombra el Word.
Si conviene encender un filtro al subirlo («Excluir bibliografía», «Excluir citas»), va en la
misma línea, entre paréntesis. Si hay copias del mismo archivo en otra carpeta, no se mencionan
ahí: él solo necesita saber cuál subir.
