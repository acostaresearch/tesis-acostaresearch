# Citar con la biblioteca del tesista (Zotero y Mendeley incluidos)

## La regla que ordena todo lo demás

**Las citas no se escriben: se marcan con la clave de la fuente.**

El tesista conecta su Zotero o su Mendeley desde su perfil en la web (pestañas «Tu Zotero»
y «Tu Mendeley» de «Tus herramientas»), y esa colección o carpeta entra en su biblioteca del
proyecto junto con lo que subió de Scopus, Web of Science o SciELO. Puede conectar los dos:
lo de cada uno sale marcado «de tu Zotero» o «de tu Mendeley».
**Mendeley vale lo mismo que Zotero para citar.** A quien trabaja con Mendeley no se le pide
que se pase a Zotero.

Cada fuente tiene una clave del tipo `[AR2E15C80C]`. Al redactar, la skill pone esa clave en el
texto. Al armar el Word, **el servidor** la convierte en cita y en entrada de la lista de
referencias, en la norma del proyecto, y enlazada a Zotero cuando el tesista lo conectó.

De ahí se sigue lo demás:

- **La skill no escribe la cita** («(Pérez y García, 2024)», «(1)», «[1]») ni la lista de
  referencias.
- **La skill no arma el .docx.** Un archivo hecho por la skill saldría con las claves
  impresas como corchetes literales, sin norma y sin campos de Zotero.
- **La skill no cita de memoria.** Los datos bibliográficos que no salen de una búsqueda
  suelen traer el año o el DOI equivocados, y eso lo comprueba un jurado en segundos.

## Las marcas

```
Al final de la afirmación:
   …afecta al rendimiento académico [AR97D22F86].

Cuando el autor ya va nombrado en la frase:
   Braun y Clarke [AR97D22F86:n] proponen que…

Con página, para la cita textual:
   «…» [AR97D22F86:p. 45]

Varias fuentes para la misma afirmación:
   …en contextos universitarios [AR97D22F86][AR2E15C80C].

Cuando no hay fuente que respalde la afirmación:
   [FALTA FUENTE]
```

**Solo se usan claves que haya devuelto una búsqueda o la biblioteca.** Una clave recordada
o reconstruida no existe: el servidor no la encuentra y en el Word sale
«[CITA SIN LOCALIZAR: revísala]».

**La `:n` sigue al nombre del autor.** Si al reescribir el nombre del autor sale de la
frase, la marca pierde la `:n` y va al final de la afirmación. Si el nombre entra en la
frase, la marca gana la `:n` y va justo detrás del nombre. Sin eso, el Word repite el
apellido o lo pierde.

## Qué puede ir entre corchetes en el texto que se guarda

`guardar_capitulo` convierte el texto en el Word que el tesista entrega. Entre corchetes
**solo** valen:

- las claves de cita `[AR…]`, con o sin `:n` / `:p. N`;
- `[FALTA FUENTE]`;
- la marca de figura `[Insertar aquí la Figura N: nombre-del-archivo.png]`.

Todo lo demás se dice al tesista **en el chat**, no dentro del capítulo: nada de
`[VERIFICAR EN FUENTE ORIGINAL]`, `[PENDIENTE — …]`, `[revisar esto]` ni notas para
renumerar. Tampoco va dentro del capítulo una sección «Referencias» escrita a mano: el
servidor pone la suya al final del documento y saldría duplicada.

## La norma de citas

Es una sola para toda la tesis y vive en el proyecto:

1. Mirar la línea «Norma de citas» que devuelve `mi_proyecto`.
2. Si ya está elegida, no se vuelve a preguntar.
3. Si dice «sin elegir», se pregunta una vez y se guarda con `guardar_avance`, campo
   `estiloCitas` (y `idiomaCitas` si la tesis va en inglés). Nunca se supone por la
   universidad.

Con la norma guardada, el servidor escribe las citas y la lista en esa norma, con la
numeración continua de toda la tesis en Vancouver o IEEE. **Nada se convierte ni se
renumera a mano**, y si el asesor pide otra norma se cambia en el proyecto sin reescribir
ningún capítulo.

## De dónde salen las fuentes

```
HERRAMIENTA                    CUÁNDO
─────────────────────────────  ──────────────────────────────────
mis_fuentes                    Ver la biblioteca entera del
                               tesista. origen: "zotero" o
                               "mendeley" para ver solo lo que
                               trajo de uno, "subidas" para sus
                               exports. Úsala cuando pregunte
                               «qué tengo», «mi Zotero», «mi
                               Mendeley», «mis fuentes».

buscar_fuentes                 La búsqueda de todos los días.
                               Busca A LA VEZ en la biblioteca
                               de Acosta y en la del tesista,
                               Zotero y Mendeley incluidos. Es
                               AQUÍ donde se cita desde ellos.

ampliar_desde_mis_fuentes      Bola de nieve sobre su biblioteca:
                               qué trabajos citan varias de sus
                               fuentes y él no tiene. Para cuando
                               dice que no sabe qué más buscar.

buscar_en_la_literatura        OpenAlex, catálogo abierto y en
                               vivo. Para antecedentes nacionales
                               y para fuentes en español, que es
                               donde están SciELO, Redalyc y los
                               repositorios latinoamericanos.

anadir_a_mis_fuentes           Guarda por DOI las fuentes nuevas
                               que el tesista apruebe, y les da
                               clave. PREGÚNTALE ANTES: no se
                               guarda lo que no pidió.

revisar_evidencia              Qué afirmaciones tienen fuente y
                               cuáles no. Obligatoria antes de la
                               Discusión y antes de entregar.
```

Si `buscar_fuentes` no aparece entre las herramientas del conector, se trabaja con
`mis_fuentes` y se le dice al tesista que desconecte y vuelva a conectar el conector en
claude.ai para refrescar la lista de herramientas.

### Cómo se busca bien con `buscar_fuentes`

Manda **siempre los tres campos**:

- `tema`: el tema **en inglés**, en palabras del contenido, no una pregunta entera. La
  biblioteca de Acosta son artículos indexados en Scopus y Web of Science, con títulos y
  resúmenes en inglés. La skill traduce: «validez de constructo» → «construct validity».
- `temaOriginal`: **el mismo tema en español**, tal como lo dijo el tesista. Con estas
  palabras se busca dentro de SU biblioteca, que suele estar en español y no la encuentra el
  término en inglés.
- `pais`: el código de dos letras del tesista (`pe`, `co`, `mx`, `cl`). Sirve para traerle
  antecedentes nacionales, que es lo que le pide el jurado.

Si falta `temaOriginal`, su Zotero y su Mendeley quedan fuera de la búsqueda. Es el error más caro de este
paso.

### Las teorías y los autores clásicos

Hernández-Sampieri, Carrasco, Likert, Cronbach, Vygotsky… también se citan con clave. Se
buscan con `buscar_fuentes` o `mis_fuentes`; si el tesista tiene el libro o el artículo y
no está en su biblioteca, se añade con `anadir_a_mis_fuentes` (si tiene DOI) o se le pide
que lo meta en su Zotero o su Mendeley y pulse «Actualizar ahora» en esa pestaña de su perfil. Mientras no tenga clave, la afirmación
va con `[FALTA FUENTE]` y se le avisa en el chat.

## Decir de dónde viene cada fuente (regla dura)

Las tres procedencias no valen lo mismo y **no se presentan igual**:

```
PROCEDENCIA              CÓMO SE PRESENTA
───────────────────────  ─────────────────────────────────────
Biblioteca de Acosta     Llevan criterio editorial. Se pueden
                         presentar sin advertencia.

Biblioteca del tesista   Las eligió él. NO están revisadas por
(su Zotero, su Mende-    Acosta. Se dice al presentarlas.
ley, sus exports)

Catálogo abierto         OpenAlex indexa de todo, incluidos
(buscar_en_la_           repositorios y preprints. Se advierte
literatura, ampliar_     siempre, y en la bola de nieve además
desde_mis_fuentes)       se le presentan para que ELIJA, no
                         como si ya fueran suyas.
```

La respuesta de la herramienta dice de cuál viene cada una. La skill traslada ese dato al
tesista, no lo omite.

En la bola de nieve, el número que importa es **«lo citan N de tus fuentes»**: cuanto más
alto, más central es ese trabajo en su tema. Se dice así, no como «muy citado».

## Qué hacer cuando no hay fuente

Se marca `[FALTA FUENTE]` y se le dice al tesista en qué afirmación quedó. **Nunca** se
inventa una fuente, ni se estira una que dice otra cosa, ni se deja la afirmación sin marca
esperando que nadie la mire.

Si el tesista dice que en su Zotero o su Mendeley sí tiene una fuente que no aparece, la
causa probable es que no esté en la colección (o carpeta) que eligió, o que no se haya
actualizado. Se le indica: en su perfil, «Tu Zotero» o «Tu Mendeley» → «Actualizar ahora».
Los dos se actualizan solos cada noche.

Si todavía no ha conectado su gestor, lo hace desde esa misma pantalla. **La conexión hay
que empezarla y terminarla en el mismo navegador**: el permiso vuelve atado al navegador donde
pulsó «Conectar mi Zotero» (o «Conectar mi Mendeley»), así que si abre el enlace en otro —o en el móvil habiendo empezado en el
ordenador— la conexión falla y hay que repetirla entera.

## El flujo de un capítulo con citas

```
1. mi_proyecto           al abrir la conversación; trae la norma
2. ver_capitulo          antes de preguntarle nada de ese capítulo;
                         con texto: true para leer lo ya escrito
                         de los capítulos anteriores
3. buscar_fuentes        al necesitar respaldo; la cita nace atada
   (o mis_fuentes)       a su clave
4. redactar              con las claves puestas en el texto
5. guardar_capitulo      apenas el tesista lo dé por bueno; si pasa
                         de 30.000 caracteres, por partes con
                         anadir: true desde la segunda
6. revisar_evidencia     antes de la Discusión y antes de entregar
7. enlace_del_word       cuando quiera el documento
```

## Si el tesista trae su tesis ya escrita

Cuando `mi_proyecto` dice que hay un documento subido, o cuando pide «cita mi documento»,
el camino es otro y está en sus propias herramientas: `ver_mi_documento` para leerlo por
tandas, y `citar_mi_documento` para guardar dónde va cada cita.

Dos reglas de ese camino, porque se rompen fácil:

- **No se cambia ni una palabra** del párrafo: solo se añaden marcas. Un párrafo con el
  texto cambiado se rechaza.
- **Antes de guardar nada** se le enseña un resumen: cuántas citas se pondrán y con qué
  fuentes, qué fuentes nuevas se añadirían a su biblioteca, y qué afirmaciones quedarían en
  `[FALTA FUENTE]`. Solo con su visto bueno se guarda.

## Las demás herramientas del perfil

El tesista tiene en su perfil de acostaresearch.com la sección **«Tus herramientas»**. Muchos no
saben que existe: cuando una de ellas le ahorra trabajo en el paso en que está, **se le dice en
una línea**, sin hacerle un recorrido por todas.

```
PESTAÑA                        PARA QUÉ / CUÁNDO MENCIONARLA
─────────────────────────────  ──────────────────────────────────
Tus fuentes de Scopus          Buscar en Scopus, SciELO y las
                               tesis peruanas de ALICIA (RENATI)
                               desde la web, elegir y añadir a su
                               biblioteca con un clic. También
                               sube ahí los exports que traiga
                               de otra base. Al buscar
                               antecedentes.

Tu Zotero / Tu Mendeley        Conectar su gestor de referencias.
                               Cuando ya lleva sus fuentes en uno
                               de ellos, o cuando hay una fuente
                               sin DOI que guardar.

Tu análisis en R               Resultados cuantitativos: lo corre
                               Claude con trabajar_en_r. Sube su
                               matriz (Excel, CSV, SPSS, o PDF de
                               laboratorio) por el enlace que da
                               la herramienta. No instala nada.

Tu ATLAS.ti                    Resultados cualitativos
                               (entrevistas, grupos focales): lo
                               hace Claude con analisis_
                               cualitativo, sin instalar ni pagar
                               ATLAS.ti. Al final puede darle el
                               proyecto codificado (.qdpx) para
                               abrirlo en ATLAS.ti, NVivo o
                               MAXQDA si su asesor lo pide.

Mapa en VOSviewer              Mapas bibliométricos (coocurrencia
                               de palabras, coautoría, citación,
                               cocitación) hechos en la web paso a
                               paso, como en VOSviewer, con sus
                               fuentes o con una búsqueda. Se
                               lleva la imagen, la tabla en Excel
                               y los archivos para VOSviewer. Para
                               justificar el vacío del tema en el
                               marco teórico o en un mapeo.
```

- **Lo que hace Claude** (R, cualitativo, mapeo con bibliometrix) va por las herramientas del
  conector. **Lo que hace el tesista en la web** (conectar Zotero o Mendeley, buscar en Scopus,
  crear el mapa de VOSviewer) se le indica con el nombre exacto de la pestaña.
- **Una imagen hecha en la web** (el mapa de VOSviewer) entra al capítulo como figura: la marca
  `[Insertar aquí la Figura N: nombre-del-archivo.png]` y él la pega en su Word.
- **No se nombran herramientas que el tesista no necesita** en ese paso. Una línea a tiempo vale
  más que la lista entera.
