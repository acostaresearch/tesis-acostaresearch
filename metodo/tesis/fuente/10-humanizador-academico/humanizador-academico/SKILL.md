---
name: humanizador-academico
description: |
  Humaniza textos académicos en español (tesis, artículos, sustentaciones)
  escritos o asistidos con IA, por bloques de hasta diez párrafos con el antes
  y el después, para que el autor apruebe cada bloque en un solo mensaje.
  Trabaja sobre el Word que el tesista subió con el enlace, sobre los capítulos
  guardados en el proyecto o sobre texto pegado en el chat. Si el tesista
  resaltó en rojo lo que quiere humanizar, solo eso; si no, toda la prosa. No
  pide ningún reporte de Turnitin. El servidor le da los párrafos con la voz del
  autor, revisa lo guardado y avisa de lo que hay que rehacer. Las cifras, los autores, lo que va
  entre comillas y las claves de cita [AR…] y [FALTA FUENTE] no se tocan. NO
  pide fuentes. Úsala cuando el usuario diga "humaniza este texto", "humaniza
  mi tesis", "esto suena a IA", "me detectó IA", "bájale el porcentaje de IA",
  "suena robótico", o pegue un fragmento pidiendo que suene humano, aunque no
  diga "humanizar".
license: MIT
metadata:
  version: "4.2"
  base: "Adaptación al español académico de la skill humanizer 2.9.1 (Wikipedia, Signs of AI writing)"
  changelog: "4.2 — las remisiones cortas a tablas y figuras pueden quedar igual; se revisa la concordancia («se vio los resultados») y que no se pierda la remisión. 4.1 — por bloques de hasta diez con ANTES y AHORA, que el tesista aprueba antes de guardar; sin reporte de IA de Turnitin (el servidor ya no lo acepta): la entrada es ver_lo_marcado con rojo o todo; sigue en un solo tramo. 4.0 — de una vez por defecto, con o sin reporte: la entrada es ver_lo_marcado (ia, rojo o todo) y cada tanda se guarda sin enseñarla ni pedir aprobación; fuera el banner, la pregunta de diagnóstico, el inventario, los bloques con ANTES/AHORA/TRAZA y las rondas; la skill cabe en un solo tramo (antes llegaba en 24) y el catálogo de patrones queda condensado. 3.5 — ver_lo_marcado y reescribir_parrafos para capítulos guardados. 3.4 — reporte de IA de Turnitin. 3.2 — Word subido con humanizar_mi_documento. 3.0 — chequeo del contrario."
---

# Humanizador académico

Quita los rastros de redacción con IA sin tocar el contenido ni el rigor. El
texto ya es del autor: la tarea es que suene a él, no a modelo. El tesista pidió
que lo humanices **por bloques**: le enseñas hasta diez párrafos con el antes y
el después, los aprueba en un solo mensaje, los guardas y sigues. Lo que antes se revisaba en el chat
(oraciones idénticas, vocabulario de modelo, rayas, muletillas, aperturas
repetidas) lo revisa el servidor al guardar y te lo devuelve como AVISOS.

### El recorrido

1. **Qué se humaniza.** Llama a `mi_proyecto`. Pregunta solo lo que no esté claro,
   y en una sola pregunta:
   - Si hay **documento subido**, confírmale una vez que trabajas con ese (nombre y
     fecha) o que suba otro con el enlace de `subir_mi_documento`.
   - Si no hay documento y su tesis está en el proyecto, se humanizan los
     **capítulos guardados**: todos, o el que nombre.
   - Si escribió su tesis fuera y no la ha subido, dale el enlace de
     `subir_mi_documento`. Para humanizar **no hace falta ningún reporte de
     Turnitin**: el de IA ya no se acepta. Si quiere elegir qué se humaniza, que
     lo resalte en rojo en su Word antes de subirlo.
   - Si adjunta el Word en el chat, no lo edites ahí (se le borra el formato):
     dale el enlace de `subir_mi_documento` y espera a que diga que lo subió.
   - Si pega un texto corto, ve a «Texto pegado» al final.

   Los enlaces se dan como enlace que se pulsa, copiando tal cual la línea que
   devuelve la herramienta.

2. **Lee solo lo que toca, con `ver_lo_marcado`.** No leas antes el documento
   entero ni hagas inventario:
   - `"reporte": "rojo"` si dice que resaltó en rojo lo que quiere humanizar;
   - `"reporte": "todo"` si no hay rojo: toda la prosa aún sin humanizar
     (el Word subido, o los capítulos guardados; con `"capitulo"` para uno solo).

   La respuesta trae la tanda de párrafos numerados, las reglas y la **voz del
   autor**: párrafos que escribió él. Imitar esa voz vale más que cualquier regla
   de aquí.

3. **Enséñale un bloque de hasta diez párrafos.** Toma los primeros de la tanda
   (no más de diez), reescríbelos y, antes de enseñarlos, revísalos con «Lo que
   tu propia reescritura fabrica». Para cada uno:

   **¶12**
   ANTES: el texto original, completo.
   AHORA: el texto nuevo, completo.

   Sin trazas, métricas ni comentarios por párrafo; si algo no se tocó o hay que
   consultarle, una línea al final del bloque. Cierra con una sola pregunta:
   «¿Los guardo así? Si quieres cambiar alguno, dime cuál y qué.»

4. **Guarda lo que apruebe** con la herramienta que diga la respuesta:
   `humanizar_mi_documento` (Word subido) o `reescribir_parrafos` (capítulos
   guardados, un capítulo por llamada). Si pide cambiar alguno, rehazlo y
   enséñale solo ese antes de guardarlo. Lo que no apruebe no se guarda: el
   original se queda como está.

5. **Rehaz lo que vuelva.** Un párrafo RECHAZADO no quedó guardado: corrige lo que
   dice el motivo (una cifra, unas comillas, un apellido, una clave) y mándalo
   otra vez. Los AVISOS de oraciones idénticas, vocabulario o rayas se corrigen en
   el momento; las **muletillas** se cuentan en todo el documento, así que se
   cambian en las tandas que siguen.

6. **Vuelve al paso 2** para el bloque siguiente: los párrafos de la tanda que
   aún no le enseñaste vuelven a salir. Sigue hasta que diga NO QUEDA NINGUNO, o
   hasta que el tesista diga que basta. Entonces
   `enlace_del_word` y un informe de cinco líneas como mucho: cuántos párrafos,
   qué no tocaste y por qué, y lo que tiene que decidir él (oraciones del
   original que no se entendían, ideas repetidas entre párrafos, una cita que
   parece atribuida a dos autores, capítulos que el asesor ya había aprobado y
   tendrá que volver a ver). Nunca prometas un porcentaje: que lo pase otra vez
   por Turnitin y, si algo le sigue saliendo como IA, que lo resalte en rojo en
   su Word, lo suba por el mismo enlace y se repite con `"reporte": "rojo"`.

**Lo que no se reescribe sin que lo pida:** objetivos, preguntas, hipótesis o
supuestos (están atados a la matriz y a lo que aprobó el asesor), títulos,
definiciones normadas y citas textuales. Pásalos en `saltar` y nómbralos en el
informe. Si luego pide tocarlos, cambios mínimos.

**Si el tesista dice que no quiere aprobar cada bloque** («hazlo todo de una
vez», «no me enseñes nada»), guarda cada bloque al reescribirlo y dile una línea
por bloque («Bloque 3: 10 párrafos guardados, quedan 24»). Es la excepción: solo
si lo pide él.

### Reglas duras

- **Ningún dato nuevo ni cambiado.** Cifras, años, fechas, números de leyes,
  artículos, casaciones y expedientes, apellidos citados y lo que va entre
  comillas se copian tal cual. No se añaden ni se quitan ideas. Si una frase vaga
  pide un dato, se escribe sin el dato.
- **Humanizar es restar.** No se añade ninguna metáfora, verbo con color ni
  palabra culta que el autor no escribió. Lo neutro y llano es la voz humana en
  una tesis. Tampoco se meten errores a propósito ni registro hablado («montar»,
  «no llega a nada»).
- **Un párrafo sale como un párrafo**, con la misma función: la introducción
  resume, el capítulo despliega. El tiempo verbal que exige la guía (pretérito en
  metodología) se conserva.
- **Sin rayas** (— ni –) fuera de los nombres que ya las traen.
- **Las claves de cita viajan con su afirmación.** Cada `[AR…]`, con su `:n` o
  `:p. 45`, y cada `[FALTA FUENTE]` se copian carácter por carácter, y cada
  párrafo sale con la misma lista que tenía. Si la afirmación cambia de oración,
  la clave va con ella. La `:n` va pegada detrás del nombre del autor: si el
  nombre sale de la frase, se quita la `:n` y la clave va al final de la
  afirmación. El nombre de un autor solo se escribe si ya estaba o sale de
  `mis_fuentes`, nunca deducido de la clave. Las citas escritas a mano
  («Pérez (2020)») son texto del autor y se conservan con sus apellidos y años.
- **Corrige las faltas evidentes** del original (concordancia, tildes, una
  minúscula inicial) sin cambiar el sentido. Si una oración no se entiende,
  conserva su sentido lo más literal posible y anótala para el informe.

### Cómo se reescribe para que no suene a IA

Reescribe **desde la idea**: di para ti qué afirma el párrafo y redáctalo otra
vez, en otro orden, el cuerpo también. Cambiar palabras sueltas deja las
oraciones iguales y el servidor lo avisa.

**Lo que más delata, en orden de peso:**

- **El molde entre párrafos.** Párrafos comparables (antecedentes, teorías,
  dimensiones, secciones de cada ley) escritos con la misma plantilla: misma
  apertura, mismo orden, mismo largo, mismo cierre. Que cada uno entre de forma
  distinta (por el hallazgo, por quién actúa, por el dato, por la consecuencia),
  que no midan lo mismo y que alguno cierre en el dato y no en una conclusión
  tuya. No cambies un molde por otro fijo.
- **El sujeto abstracto.** «La imprecisión se mantiene», «la fiscalización tiene
  que ser continua»: nadie hace nada. Pon quién hace qué: el juez, la policía, el
  docente, el Estado.
- **Aperturas en cadena.** Conector o complemento antes del sujeto en casi todas
  las oraciones («Asimismo», «En ese sentido», «A nivel nacional», «Desde esta
  perspectiva»). La mayoría de párrafos no necesita conector de entrada.
- **La frase-etiqueta.** Una oración corta que anuncia («Eso tiene una
  consecuencia práctica», «El problema es de otro orden») y otra que desarrolla.
  Se funde o se borra. Su variante de cierre es el remate «no es X, sino Y».
- **El veredicto de cierre repetido.** Todos los párrafos terminan con una
  valoración propia sin cita. Deja el veredicto para el cierre de sección.
- **Anáforas «ese/esa + abstracto»** para enlazar («esa indefinición», «ese
  avance»). Una vez vale; en cadena expulsa a los agentes.
- **Vocabulario de modelo:** crucial, fundamental, dogmático, estriba, medular,
  robusto (fuera de estadística), holístico, sinergia, «juega un papel», «se
  erige como», «cabe destacar», «es importante mencionar», «en estrecha
  relación», «resulta indispensable», «el verdadero desafío», «un amplio
  abanico». Palabra corriente en su lugar, no otra culta.
- **Gerundios colgados** al final («…, evidenciando la relevancia de…»): casi
  siempre repiten lo dicho; se cortan.
- **Nominalizaciones en cadena** («la implementación de estrategias de
  fortalecimiento de…» → «fortalecer…») y **evitar el verbo ser** («constituye»,
  «se configura como», «posee»), salvo fórmulas de método como «la muestra
  estuvo conformada por».
- **Regla de tres de adorno**, **contrastes fabricados** («lo cierto es que», «la
  verdadera pregunta es»), **cierres optimistas** y **restos de chatbot** («a
  continuación se presenta», «en resumen»).

**Lo que tu propia reescritura fabrica** (revísalo en cada tanda antes de
guardarla, en toda la tanda y no párrafo a párrafo):

- oraciones fundidas de 45 palabras o más, dos o tres seguidas: busca la que
  carga dos datos o dos fuentes y pártela ahí;
- la misma pieza de enlace repetida («por eso», «con lo cual», «de modo que»,
  «lo que»): cuenta en la tanda, no en el párrafo;
- la misma forma nueva en párrafos vecinos (una larga y un cierre corto en todos);
- «Autor (año) + verbo» abriendo todos los antecedentes;
- palabras que no estaban: «solo», «único», una cifra calculada, un «del bien»
  que el original no decía;
- la concordancia rota al cambiar el verbo («se vio los resultados» por «se
  observaron los resultados») y la remisión a la tabla o figura que se pierde
  por el camino. Relee cada oración sola: tiene que entenderse y decir lo mismo.

**Ritmo.** Varía el largo de las oraciones, pero las cortas cargan información,
no énfasis: «Hace tres años casi no ocurría» funciona; «Y todo cambió.» suena a
guion. Tras tres o cuatro cortas, una larga con subordinadas.

**Conectores.** Sobra el que pega dos frases sin relación lógica; falta el que
marca una relación que existe y quedó implícita, y sin él el párrafo se lee como
fichas pegadas. Antes de escribir un enlace, comprueba qué relación afirma; si no
se sostiene, no la inventes.

### Lo que no es un patrón de IA

- La pasiva y la impersonal en metodología y resultados («Se aplicó el
  instrumento a 120 docentes»).
- Los términos técnicos (significativo, correlación, consistencia interna,
  hermenéutico o dogmático cuando nombran el método) y su repetición: no se
  cambian por sinónimos.
- Las fórmulas institucionales que pide la guía («El presente estudio tuvo como
  objetivo»).
- Una oración larga bien articulada: el problema es que todas midan lo mismo.
- Las remisiones cortas a tablas y figuras («En la tabla 1 se observaron los
  resultados»): pueden quedar como estaban, y el servidor no avisa de ellas.

### Cuándo parar

Si tras dos rondas por Turnitin un párrafo le sigue saliendo como IA, el problema ya no es la redacción:
hay contenidos con piso (una enumeración de teorías con autor y año, una lista de
antecedentes, un marco jurídico de siete normas). Díselo y propón una salida de
contenido, que decide él: agrupar, recortar lo que repite otro capítulo o
llevarlo a la sección donde se usa. Retorcer la prosa más allá de ese punto
cuesta registro académico y no gana nada.

### Texto pegado en el chat

Se reescribe con las mismas reglas y se devuelve con el antes y el después, por
bloques de hasta diez párrafos si es largo; el después queda listo para pegar,
con una línea de lo que no se tocó. No se guarda nada. Si quiere medirlo,
`scripts/medir.py original.txt humanizado.txt --claves` compara largo de
oraciones, aperturas, sujetos abstractos y claves de cita antes y después; es
opcional.

Esta skill no escribe capítulos, no arma el Word (lo arma el servidor con el
formato de su universidad), no pide fuentes y no baja la similitud de Turnitin:
para eso está la skill bajar-similitud.
