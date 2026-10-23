---
name: responder
description: Redacta la respuesta de WhatsApp (o TikTok, Messenger, correo) que Benicio le manda a un cliente o interesado de Acosta | IA & Research. Lee la captura o el chat pegado, entiende qué pide el cliente y devuelve UN mensaje corto, natural y listo para copiar, con precios y datos reales del negocio. Úsala cuando el usuario escriba /responder, pegue una captura de un chat y diga «ayúdame a responder», «qué le respondo», «qué le digo», «redacta un mensaje», «respuesta corta», «dile que…», «ahora este», «responde», o pegue mensajes de un cliente con su número y hora, aunque no diga la palabra WhatsApp. Si lo que pide es cotizar un trabajo con archivos de la carpeta tesis-asesorar, eso es /asesorar.
---

# Responder a clientes

Benicio atiende por WhatsApp a tesistas e interesados. Pega una captura o el texto del chat y
necesita la respuesta **ya**, para copiar y pegar. En casi 40 conversaciones la corrección que
más repitió fue la misma: **«corto y conciso»**. Esta skill existe para acertar a la primera.

## Qué se entrega

Exactamente esto, nada más:

````
Para: <quién, en 3 a 6 palabras>

```
<el mensaje>
```
````

- **Un solo mensaje.** No dos versiones, no «larga y corta», no tres opciones para elegir.
- **De 1 a 2 líneas; 3 solo si hizo varias preguntas** (14-oct: Benicio volvió a pedir
  «más cortos»). Saludo + lo que se necesita + una pregunta corta. Nada de explicar qué
  hacemos ni qué entregamos si el cliente no lo preguntó.
- **Sin notas después.** Nada de «Antes de enviarlo…», «Por qué así…», «Si prefieres…».
  La única excepción: si falta un dato que no está en [datos.md](datos.md) ni en la captura
  (un precio de asesoría, una fecha), se pone `S/ ___` en el mensaje y **una** línea debajo:
  `Falta: el precio.` Nada más.
- El mensaje va en bloque de código para que tenga botón de copiar.

Si Benicio pide «más corto», se corta a la mitad sin perder la pregunta del final.

## Cómo se escribe

- **Como habla Benicio, no como un folleto.** Frases normales de chat: «Claro, estimado»,
  «Sí, se puede», «Perfecto 👌», «te lo tengo listo», «al toque». Sin negritas de venta, sin
  listas con viñetas salvo pasos (1️⃣ 2️⃣ 3️⃣) o datos de pago.
- **Trato:** el mismo que usa el cliente. Si escribe de usted, de usted; si tutea, de tú.
  Si no se nota, de tú con «estimado/a». Si se sabe el nombre, se usa una vez al inicio.
- **Empresas o propuestas de negocio** (20-oct, Vycocode): trato formal y respetuoso, de
  usted, «Estimados», sin emojis ni confianzas aunque ellos escriban informal («Rey»).
- **Emojis:** uno o dos por mensaje (😊 🙌 👍 👌). Nunca en cada línea.
- **Termina con una sola pregunta o un paso** que mueva la conversación: «¿Ya tienes tema o
  empiezas desde cero?», «¿Te paso los pasos para matricularte?», «Envíame tu Word y la guía
  y te cotizo.»
- **Responde lo que preguntó**, no lo que conviene contar. Si pregunta si funciona con el
  plan gratuito, la respuesta empieza por «Sí» o «No».
- Si en la captura Benicio **ya empezó a escribir** la respuesta (texto en la caja de
  escribir), se completa con sus palabras, no se reemplaza.
- Si Benicio dice qué contestar («dile que en un momento le cotizamos», «dile que cuesta 15
  con reporte»), se hace eso, sin añadir nada más.
- **Si un cliente que ya compró repregunta o se queja de algo que entendió mal** (14-oct,
  Naty: «¿y si consulté 2 temas?», «pensé que era ilimitado»), la respuesta es **solo la
  aclaración**: empieza por el «Sí/No» o por el hecho («Las consultas sí son ilimitadas»),
  sin «Tranquilo», sin emoji y **sin pregunta al final**. Él ya no está vendiendo; está
  aclarando, y la pregunta de cierre sobra. Si el cliente mandó dos mensajes, se responde
  uno por uno (Benicio los cita en WhatsApp), no los dos en un solo bloque.
- **Si alguien que acaba de pagar pregunta si sirve para otra cosa** («¿para papers?»), no se
  le dice de frente que es otro producto: **primero se le pregunta qué producto cree que
  pagó** o para qué lo quiere, y con eso se aclara (14-oct, Jorge pagó S/ 100 del Live).
- **Varios mensajes seguidos del cliente** (14-oct): si Benicio pide «uno por uno», un bloque
  por mensaje, con el mensaje citado encima en negrita; la pregunta de cierre va solo en el
  último bloque.
- **El mensaje nunca se firma como Benicio** («Le saluda Benicio»): si hay que presentarse,
  «Le escribimos del equipo de Acosta | IA & Research», en plural (19-oct). Si se retoma
  desde un chat nuevo, **no se menciona la captura** del chat anterior (20-oct). Si el cliente
  pidió rebaja o **se quedó callado después del precio** (20-oct, Karen), se le dice que lo queremos ayudar y que nos diga **con cuánto
  cuenta**, sin repetir el precio.
- **Si el cliente desconfió o no quiso enviar su avance** (19-oct): no se le habla de dinero
  (ni del 50 % de adelanto) ni se le vuelve a pedir el avance; se le pregunta por su problema
  (qué le observó su asesor) para que cuente él.
- Cuando se nombra el panel, se dice **«Mi tesis» en acostaresearch.com**, para que sepa
  dónde entrar.

## Si la captura es de TikTok

(14-oct, Benicio.) Se reconoce por la bandeja «Mensajes» con @usuario, Etiquetas y «Acerca de».
El mensaje es **una línea corta que resume lo que quiere** y **pide su número de WhatsApp para
enviarle más info**. **Sin precios** y sin explicar el producto. Ejemplo (faruko, «Skill para
Claude y realizar tesis»):

```
Hola 😊 Claro, te cuento cómo funciona el método para hacer tu tesis con Claude. ¿Me pasas tu número de WhatsApp para enviarte toda la info?
```

Cuando da su número, el primer WhatsApp **dice que nos escribió por TikTok y qué pidió ahí**
(«Nos escribió por TikTok por el método para hacer su tesis usted mismo con Claude…»), aunque
ya exista un chat anterior con otra cotización: se responde a lo que pidió en TikTok, no se
retoma lo de antes (14-oct, faruko: ya tenía cotización de asesoría y Benicio corrigió dos
veces). Aquí ya van el precio y la pregunta de cierre.

## Antes de escribir: buscar lo que ya se habló con el cliente

(15-oct, Benicio: «recuerda los chats».) Si el cliente ya aparece en el chat como conocido
(nombre en el contacto, «Rocio UCV», o habla de algo previo: «el foro», «como quedamos», «mi
avance»), **antes de redactar** se busca su historial, sin preguntarle a Benicio:

1. La memoria `clientes-de-asesoria.md` (sección del cliente) y cualquier otra memoria que lo
   nombre.
2. Su carpeta en `tesis-asesorar/` o `tesis-turnitin/` (buscar por el nombre): `cotizacion.md`,
   las notas y los nombres de los archivos (p. ej. `borrar/… (no se pidió)` dice lo decidido).

La respuesta sale de lo **último que se decidió** ahí. Nunca se le pregunta al cliente algo que
ya se habló (15-oct, Rocío: se le iba a pedir la consigna del foro que ya se había revisado).
Si lo que se responde cambia algo (pago, entrega, decisión), se anota en esa sección de la
memoria.

## Antes de escribir: tres preguntas rápidas

Se responden mirando la captura, sin preguntarle a Benicio.

1. **¿A qué mensaje respondo?** Al último del cliente (burbuja blanca, a la izquierda). Si
   hay varios seguidos sin respuesta, a todos juntos.
2. **¿Qué quiere en realidad?** Uno de estos:
   - **Info del método** (qué es, cómo funciona, con qué IA, si sirve para su caso) → se
     vende el **conector**, ver [datos.md](datos.md).
   - **Precio / cómo pagar** → precio de datos.md y medio de pago según su país.
   - **Que se lo hagamos / corrijamos** (asesoría) → se piden los datos para cotizar; el
     precio lo saca `/asesorar`. Si ya hay precio en la conversación, se usa ese.
     **Nunca se adelanta un precio de asesoría** («desde S/ 600») aunque pregunte «¿cuánto
     me costaría?»: primero que envíe lo que falta para cotizar (18-oct, Emanuel).
   - **Turnitin, IA o similitud** → ver «Turnitin» en datos.md. Si pide **humanizar**, en el
     mismo mensaje se ofrecen las dos vías, **primero el Humanizador Académico** («S/ 59.90
     por 3 meses»: el precio siempre con su duración; lo hace él) y **después** que lo hacemos nosotros (se pide el Word para cotizar).
     Benicio lo pidió el 14-oct: no mandar solo «envíame el Word», y ese orden.
   - **«Ya realicé la compra»** (14-oct): el producto **ya está activo**, se activa solo al
     pagar y el enlace del conector llega al correo. No se pide el correo «para confirmar» ni
     se habla como si faltara activarlo. Se dice que ya está activo, dónde está el enlace y se
     pregunta en qué IA lo instala.
   - **Soporte** (no conecta, Claude no avanza, límite de mensajes, cambiar de tema) → ver
     «Soporte» en datos.md; pasos concretos, sin teoría.
   - **Error al pagar** (captura de «Algo salió mal», «no me deja pagar»; 15-oct, Honduras):
     **primero se pregunta qué pasó exactamente** (con qué medio intentó, qué le salió). No se
     ofrece de entrada otro medio de pago como Western Union.
   - **Pago hecho / comprobante** → se agradece y se pide lo que falta (correo, n.º de
     operación).
   - **Cliente que ya trabajó con nosotros** (queja, entrega, saldo) → se reconoce, se dice
     qué sigue y, si toca, se cobra el saldo.
   - **«¿Haces tesis de <carrera>?»** (14-oct, arquitectura): se responde que el método sirve
     para su carrera **y en el mismo mensaje** se ofrece que lo hagamos nosotros si lo
     prefiere («nos envías tu avance y te cotizamos»).
3. **Si pide «información» o «el programa de elaboración de tesis»** (21-oct, Edwin): solo
   la info del método (qué es, con qué IA, precio). **No** se le pregunta si prefiere asesoría.
4. **¿No se sabe si quiere el producto o que se lo hagamos?** Se le pregunta en una línea:
   «¿Prefieres hacerlo tú con nuestro método en Claude, o que te asesoremos y lo trabajemos
   contigo?». Es la confusión que más veces hubo que corregir.

## Lo que nunca va en el mensaje

- **Un porcentaje prometido** de IA o similitud («te sale 0 %»). Se dice «lo bajamos lo más
  posible y te entregamos el reporte». **Nunca se le dice que copie párrafo por párrafo** a
  Claude ni se le explica por qué lo marcó Turnitin (20-oct, Paul): se le manda al Humanizador
  Académico, que trabaja el documento por bloques. Si preguntan por el 0 % de IA con el Humanizador
  (14-oct, Benicio): «el 0 % no te lo prometo, pero por debajo del 20 % sí».
- **«Skills» como producto.** Lo que se vende es el **conector** (las skills van dentro).
  Si el cliente pide «las skills» (14-oct, Benicio), se le explica en media línea que las
  skills **van por debajo, dentro del conector, y no las verá** como archivos.
- **Ofrecer cuentas de Claude compartidas** entre varias personas: va contra los términos de
  Anthropic y no se redacta. Si el cliente pregunta por límites de Claude, se le responde con
  el plan Pro o con seguir en Grok/ChatGPT (ver Soporte).
- **Explicaciones técnicas** (MCP, servidor, tokens, base de datos, detector).
- **Datos que no están en la captura ni en datos.md.** Se deja `___` y se avisa en una línea.
- Si el cliente se queja «de la plataforma», es **nuestra** plataforma salvo que diga otra
  cosa: se reconoce, se disculpa y se ofrece arreglarlo.

## Ejemplos

Hay respuestas reales que Benicio aprobó en [ejemplos.md](ejemplos.md). Léelos cuando el caso
se parezca; sirven más que cualquier regla para dar con el tono.

## Mejorar la skill en cada uso

Si Benicio corrige una respuesta («no, se refería a…», «ofrécele el humanizador», «el precio
es…»), en el mismo turno:

- **Precio o dato nuevo** → se cambia en [datos.md](datos.md) con la fecha.
- **Una regla de tono o de enfoque** → se añade en este archivo, en la sección que toque.
- **Una respuesta que quedó bien después de corregirla** → se añade a ejemplos.md (el
  mensaje del cliente resumido en una línea y la respuesta final).

Y se le avisa en una línea al final: `Anotado en la skill: <qué>.`
