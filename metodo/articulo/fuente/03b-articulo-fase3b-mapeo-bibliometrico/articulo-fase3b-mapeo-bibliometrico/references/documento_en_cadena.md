# El documento en cadena

Regla de toda la ruta, no solo de esta fase.

## Un manuscrito, no doce

El artículo es **un solo manuscrito que crece fase a fase, guardado en el
servidor**. La Fase 2 guarda la Introducción; cada fase siguiente guarda su
sección con `guardar_capitulo`, bajo la clave de su fase tal como aparece en
`listar_capitulos` (el nombre de la skill, como `articulo-fase4-metodos`).
Ningún .docx pasa de una fase a otra: al pedir el enlace con `enlace_del_word`,
el servidor arma el Word con todas las fases guardadas, en orden, con las citas
y una sola lista de referencias en la norma del proyecto.

Sin esto, el investigador termina con nueve archivos sueltos, referencias
repetidas en cada uno, acrónimos que cambian entre secciones y la certeza de que
alguno quedó desactualizado.

**Nunca se construye un .docx con código ni se escribe la lista de
referencias.**

## Cómo se guarda

- **Markdown limpio**, sin comentarios ni notas para el investigador: lo que se
  guarda es lo que sale en el Word. Subtítulos, tablas, figuras y citas se
  escriben como indica `formato_docx.md`.
- **El título de la sección lo pone el servidor** con el nombre de la fase: no
  se repite al comienzo del texto. Si la revista la llama de otra forma, se
  cambia en Word.
- **El título del artículo no va en el texto**: la portada del Word sale con el
  tema del proyecto, que se guarda con `guardar_avance` (`tema`).
- **Máximo 30.000 caracteres por llamada.** Una sección más larga va por partes:
  la primera sin marca y las siguientes con `anadir: true`, en orden.
- **Si se corrige la sección entera**, se vuelve a guardar completa sin
  `anadir`, y reemplaza lo anterior. Si el investigador quiere conservar la
  versión previa, que descargue el Word antes.
- **Lo acordado va aparte, con `guardar_avance`** (`capitulo` con la clave de la
  fase y `resumen` en dos o tres frases): acrónimos, término unificador y
  decisiones de la fase. Es lo que la fase siguiente lee con `ver_capitulo`.

## Lo que queda guardado al cerrar la Fase 3

Clave `articulo-fase3-revision-literatura`:

```
## Teorías base
[prosa]

## [Un acápite por constructo]
[prosa]

## Sustento de hipótesis
[un párrafo por hipótesis, cerrado con su enunciado]
```

En el Word: portada, Introducción, Revisión de la literatura y Referencias (las
arma el servidor al descargar el Word).

Las secciones que todavía no existen **no se guardan con encabezados vacíos**.
Un documento con seis títulos y un solo párrafo debajo confunde al investigador
y no sirve para nada.

## Cómo lo recibe la fase siguiente

Ninguna fase pide el .docx de la anterior. Empieza con `mi_proyecto` —el
panorama y la línea «Norma de citas»— y con `ver_capitulo` de las fases
anteriores, que sin `texto` devuelve lo acordado en cada una. De ahí saca tres cosas que no
debe volver a preguntar:

1. Los acrónimos ya definidos.
2. El término unificador (influencia o relación).
3. Las fuentes ya citadas, para no buscarlas de nuevo (sus claves están en
   `mis_fuentes`).

**Con `texto: true`, `ver_capitulo` devuelve el texto guardado de la sección.**
Si para trabajar hace falta leer tal cual una sección anterior —los hallazgos de
Resultados para la Discusión, la Discusión para no repetirla en las
Conclusiones—, se lee así, con la clave de su fase (por ejemplo
`capitulo: articulo-fase5-resultados`, `texto: true`). Llega en partes de hasta
24.000 caracteres, cortadas entre párrafos: cada respuesta dice «parte N de M» y
cuál pedir después, y se sigue con `parte` hasta la última. Trae las citas con su
clave `[AR…]`, las tablas en su bloque APA y los rótulos de las figuras con su
marcador. No se le pide al investigador que la pegue ni que la copie del Word.

Solo si `ver_capitulo` dice que la fase no tiene texto guardado —porque trabajó
fuera de la plataforma—, se le pide que pegue el texto de esa fase y, si está de
acuerdo, se guarda con su clave antes de seguir, para que el Word salga completo. Si trae un
manuscrito ya terminado, puede subirlo por el enlace que da `subir_mi_documento`, aquí en la conversación: el perfil no tiene dónde subirlo.

**El estilo de cita no se hereda de ningún documento.** Se lee en la línea
«Norma de citas» de `mi_proyecto`. Si la revista pide otro, se cambia con
`guardar_avance` (`estiloCitas`) y no se reescribe nada.

Y una regla de integración: **las citas van siempre con su clave**
(`[AR97D22F86]`; `[AR97D22F86:n]` justo después del nombre del autor cuando
está en la oración; `[AR97D22F86:p. 45]` con página; `[AR…][AR…]` para varias)
y **la lista de referencias no se escribe, no se ordena ni se numera a mano**.
El servidor arma una sola, con todas las fuentes citadas y en la norma del
proyecto, cuando se descarga el Word con `enlace_del_word`. No se inventan
claves ni fuentes: lo que no tiene respaldo se marca `[FALTA FUENTE]`.

## La matriz de trazabilidad va aparte

Es lo único que no se integra al manuscrito: es material de auditoría, no parte
del artículo. No se guarda con `guardar_capitulo`; se entrega aparte y se
actualiza en cada fase que agregue citas.

## Al entregar

Guardar la sección, dar el enlace con `enlace_del_word` y decir en una línea qué
trae el Word. El enlace caduca a la media hora; si se pasó, se pide otro.

> Tu Word trae la Introducción y la Revisión de la literatura, con las
> referencias en una sola lista. En la Fase 4 seguimos desde aquí: no hace falta
> que subas nada.
