# Citas dentro de los párrafos de la Discusión

Cómo se marcan las citas en la Discusión. La forma final de cada cita (paréntesis,
«et al.», número en Vancouver o IEEE, orden de varias fuentes) **la escribe el
servidor** al armar el Word, en la norma del proyecto. La skill solo pone la clave
de la fuente en el lugar correcto. El detalle está en `references/integracion_zotero.md`.

## Las dos formas de citar

### Cita al final de la afirmación (en APA sale entre paréntesis)

```
… afirmación [AR97D22F86].
… afirmación [AR97D22F86][AR2E15C80C].
```

Ejemplos:

> Este resultado coincide con investigaciones previas en contextos similares [AR…].

> La asociación entre estas variables ha sido documentada en estudios recientes [AR…][AR…].

### Cita narrativa (el autor es sujeto de la oración)

El apellido se escribe en la frase y la clave va **justo detrás**, con `:n`. El
servidor pone solo el año (o el número) y no repite el apellido.

```
Paiva, Costa y Reis [AR…:n] reportaron …
Vereau Amaya et al. [AR…:n] encontraron …
```

Ejemplos:

> Paiva, Costa y Reis [AR…:n] reportaron una asociación moderada entre uso de IA y pensamiento crítico en estudiantes portugueses.

> Vereau Amaya et al. [AR…:n] encontraron una correlación negativa entre dependencia de IA y pensamiento crítico en universitarios trujillanos.

Si al reescribir el apellido sale de la frase, la clave pierde la `:n` y va al final
de la afirmación. Si entra, la gana y va detrás del apellido.

## Varios autores y «et al.»

Cómo se nombran los autores en la frase (uno, dos, tres o más con «et al.») se toma
de la ficha de la fuente en la biblioteca (`mis_fuentes`), tal como la muestra el
Cap II guardado. En la cita que pone el servidor, «et al.» y el número de autores
salen solos según la norma: no se escriben a mano.

## La misma fuente varias veces en el párrafo

Después de la primera mención, las siguientes pueden nombrar solo el apellido si no
hay ambigüedad, pero **cada afirmación atribuida lleva su clave**:

> Paiva et al. [AR…:n] reportaron una asociación moderada. Los resultados del presente estudio coinciden con esta tendencia, aunque Paiva et al. [AR…:n] señalaron además…

## Cita textual con página

En la Discusión se parafrasea; las citas literales son del marco teórico (Skill 3).
Si hace falta una:

```
«…» [AR97D22F86:p. 45]
```

## Varios estudios que apoyan o contradicen un punto

```
… en contextos diversos [AR…][AR…][AR…].
```

El orden dentro de la cita (alfabético en APA, numérico en Vancouver) lo pone el
servidor.

## Desacuerdo entre autores

> Mientras Paiva, Costa y Reis [AR…:n] reportaron una asociación positiva, Vereau Amaya et al. [AR…:n] encontraron una asociación negativa, lo cual evidencia la heterogeneidad del fenómeno según el nivel educativo.

## Reglas críticas que la skill respeta

### 1. Solo autores con clave

La skill solo contrasta con autores que tienen clave `[AR…]`: primero los del Cap II
del tesista (el texto guardado que lee con `ver_capitulo` y `texto: true`, o el que
pegó si lo escribió fuera) y, si hace falta un antecedente más, fuentes de su
biblioteca encontradas con `buscar_fuentes` o `mis_fuentes`. Si entra uno que no
estaba en el Cap II, se le avisa al tesista y se le sugiere añadirlo también al
marco teórico. Un autor sin clave no entra: la afirmación va con `[FALTA FUENTE]`
o se elimina.

Los autores clásicos del modelo teórico (Cronbach, Hernández-Sampieri, Long y
Magerko…) también van con su clave.

### 2. Solo lo que la fuente dice

Antes de redactar se pasa `revisar_evidencia` sin capítulo: una afirmación del
Cap II sin respaldo no se usa para contrastar, porque así es como se cuelan autores
que no dijeron eso. Después de guardar, `revisar_evidencia` con el capítulo
`discusion`.

### 3. Apellidos exactos

La skill escribe los apellidos como figuran en la ficha de la fuente. Algunos
investigadores hispanos usan apellidos compuestos (ej. «Hernández-Sampieri» o
«Acosta Enríquez»). El año no se escribe en la frase: lo pone el servidor.

## Plantilla integrada (Movimiento 2 con las claves puestas)

```
"Este resultado coincide con lo reportado por [Apellido] [AR…:n],
quien en [contexto] halló [hallazgo similar]. De manera
congruente, [Apellido2] [AR…:n] reportó [hallazgo similar] en
[contexto]. En cambio, los resultados se distancian del estudio
de [Apellido3] [AR…:n], realizado en [contexto distinto], donde
se encontró [hallazgo distinto]."
```

## Verificación final

Antes de guardar el capítulo, la skill verifica:

- [ ] Cada cita lleva una clave `[AR…]` devuelta por la biblioteca o una búsqueda
- [ ] Ninguna cita escrita a mano con apellido y año entre paréntesis, ni números
- [ ] Cada clave narrativa (`:n`) va justo detrás del apellido
- [ ] Los autores que no estaban en el Cap II están avisados al tesista
- [ ] Lo que no tiene fuente va con `[FALTA FUENTE]`
- [ ] Sin lista de referencias escrita a mano
