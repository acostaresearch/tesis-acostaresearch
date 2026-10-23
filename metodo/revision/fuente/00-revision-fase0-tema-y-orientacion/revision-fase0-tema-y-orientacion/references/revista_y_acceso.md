# Revista destino, indicadores y modelo de acceso

Se usa en el Paso 5. La revista se elige **antes** de escribir, porque fija el
límite de palabras, el estilo de cita, el idioma, la estructura de secciones y,
muchas veces, si el diseño del estudio le interesa a esa audiencia.

## Regla dura: los datos de una revista se consultan, no se recuerdan

**Nunca afirmar de memoria**: cuartil, SJR, H-index, factor de impacto, índice
en el que está, APC, tiempo de revisión, tasa de aceptación ni si sigue activa.
Todo eso cambia cada año, y varias revistas han sido excluidas de índices sin
que su propio sitio lo diga.

Si no se pudo consultar, se dice **"no lo sé"** y se deja
`[POR CONFIRMAR: cuartil e índice de la revista]`. Una recomendación equivocada
le cuesta al investigador meses de espera y un rechazo; enviarlo a una revista
discontinuada le cuesta la publicación entera.

## Dónde se buscan las candidatas

Siempre las revistas donde salieron los artículos del Paso 4, y además:

| Destino elegido en 5a | Dónde se busca |
|---|---|
| Scopus (cualquier cuartil) | Scimago (`journalsearch.php`), con términos en español y en inglés |
| SciELO o regional | SciELO, Latindex Catálogo 2.0, Redalyc y DOAJ. Scimago no las lista si no están en Scopus, y su ausencia ahí no significa nada |
| Local o institucional | El portal de revistas de las universidades del país, y el Portal ISSN para confirmar que la revista existe |

## Consultar Scimago: un intento, y si no, el investigador

Scimago Journal Rank publica los indicadores calculados a partir de Scopus.

| Recurso | URL |
|---|---|
| Búsqueda de revistas | `https://www.scimagojr.com/journalsearch.php?q=<términos>` |
| Ficha de una revista | el enlace del resultado, que lleva `&tip=sid` |
| Ranking por categoría | `journalrank.php`, no se puede leer desde la sesión |

**El sitio suele responder a la navegación automatizada con una verificación
anti-bots de Cloudflare** ("Verificación de seguridad en curso"). El orden es
fijo:

1. **Un solo intento** de leer la ficha con la búsqueda o la lectura web del
   entorno.
2. Si no carga, da error o aparece la verificación: **no reintentar ni intentar
   saltarla.** Pedirle al investigador, en un paso literal:

   > Abre `scimagojr.com`, escribe el nombre de la revista en el buscador, entra
   > a su ficha y pega aquí el texto (o una captura) con: cuartil por categoría
   > y año, SJR, *Coverage*, país, editorial e ISSN.

   Se registra con la fuente y *consultado por el investigador el [fecha]*.
3. **Vigencia en Scopus:** si el investigador tiene acceso, se contrasta además
   con la *Source list* de Scopus (lista oficial de títulos activos y
   discontinuados).
4. **JCR (Web of Science)** es otro índice, con otros cuartiles: se verifica
   aparte y requiere acceso institucional del investigador.

Si el investigador no responde o no puede (prueba sin él), el cuartil queda
`[POR CONFIRMAR]` **a la vista**, en la fila de la revista elegida de la Ficha
(Tabla 5), no escondido en una nota.

No se puede pedir "las 20 mejores Q1 de Educación" en una consulta: se compara
revista por revista. Si quiere navegar el ranking, que lo abra él, filtre por
área y categoría y pegue los nombres. Lo que nunca se hace es simular una
consulta que no se hizo, ni dar un cuartil sin categoría, año y fuente.

## Si el destino no es Scopus: índices regionales

**Scimago solo cubre Scopus.** Buscar ahí una revista de SciELO o de Latindex y
no encontrarla no dice nada sobre esa revista. Hay que ir al índice que
corresponde:

| Índice | Qué es | Dónde se verifica |
|---|---|---|
| **SciELO** | Biblioteca regional con colecciones por país; exige criterios editoriales de admisión y permanencia | El sitio de SciELO y la colección del país de la revista |
| **Latindex Catálogo 2.0** | Sistema regional iberoamericano. El **Catálogo 2.0** aplica criterios de calidad; el Directorio es solo un registro y no equivale a indexación | `latindex.org` |
| **Redalyc** | Repositorio y sistema de información con evaluación de admisión | `redalyc.org` |
| **DOAJ** | Directorio de revistas de acceso abierto con criterios de transparencia | `doaj.org` |

Una distinción que conviene explicarle al investigador, porque muchas revistas
la usan a su favor: **estar en el Directorio de Latindex no es estar en el
Catálogo 2.0.** Lo primero es un registro; lo segundo supone haber cumplido
criterios. Una revista que dice "indexada en Latindex" sin precisar cuál de los
dos merece que se verifique.

Estas revistas **no tienen cuartil**, y eso no es un defecto: el cuartil es un
indicador de Scopus y solo existe ahí. Presentarlo como carencia es engañoso.

Lo que sí hay que preguntarle al investigador, sin suponerlo: **qué le exige su
universidad o el concurso al que se presenta.** Algunas evaluaciones piden
Scopus o Web of Science; otras reconocen SciELO y Latindex. Eso decide el
destino más que cualquier recomendación general, y la respuesta la tiene él.

## Los tres datos que deciden

**a) ¿Sigue vigente?** Lo dicen los **años de cobertura**. Si terminan en el año
en curso, la revista sigue indexada. Si terminan hace tres o cuatro años, fue
discontinuada de Scopus aunque su ficha siga publicada con todos sus indicadores
históricos. Es el error más caro y el más fácil de evitar: revisarlo siempre,
aunque no lo pregunte.

**b) ¿En qué categoría es ese cuartil?** Una revista puede ser Q1 en una
categoría y Q3 en otra. Al reportarlo hay que decir **en qué categoría y de qué
año**. "Es Q1" a secas no significa nada.

**c) ¿El cuartil es estable?** El historial año por año lo muestra. Una revista
que oscila entre Q2 y Q4 puede haber caído para cuando el artículo salga.

Y una aclaración que hay que dar cuando la institución del investigador exige
Web of Science: **el cuartil de Scimago viene de Scopus.** JCR es otro índice,
con otros cuartiles, y se verifica aparte.

## Modelos de acceso y APC

Scimago no da este dato. Fuentes, en este orden, y todas sin desafío
anti-bots:

1. **API de DOAJ** (`https://doaj.org/api/search/journals/issn:XXXX-XXXX`):
   APC sí/no y monto, licencia, sello DOAJ, ISSN, URL oficial, tiempo hasta la
   publicación. Solo cubre revistas de acceso abierto; si no está, no es
   prueba de nada.
2. **API de OpenAlex** (`https://api.openalex.org/sources/issn:XXXX-XXXX`):
   ISSN-L, editorial, `is_oa`, `is_in_doaj`, `apc_usd` (cuando lo conoce) y
   producción por año. Sirve también para el encaje: qué publicó la revista
   sobre el tema (`/works?filter=primary_location.source.id:...,title_and_abstract.search:...`).
3. El sitio de la revista (*publication fees*, *article processing charges*),
   que manda si contradice a las anteriores.

| Modelo | Publicar | Leer | Qué implica para el investigador |
|---|---|---|---|
| **Suscripción** | Gratis | De pago | No hay barrera de costo. Menor difusión. |
| **Acceso abierto (oro)** | APC | Gratis | Hay que poder pagar el APC. |
| **Híbrido** | Gratis, con opción de pagar por abrir | Mixto | Se puede publicar sin pagar. |
| **Diamante** | Gratis | Gratis | Sin barrera. Muchas revistas latinoamericanas indexadas lo son. |

Preguntar por el costo **antes** de que escriba para esa revista, no después. Y
si el investigador no puede pagar APC, decirle que hay revistas indexadas de
acceso diamante y de suscripción: no es una limitación que lo deje fuera de las
revistas indexadas.

Los montos de APC **no se estiman**. Se leen en el sitio de la revista o quedan
`[POR CONFIRMAR]`.

## Normas de la revista elegida

Alcance, límite de palabras, estilo de cita, idioma, estructura y formato se
leen en la guía de autores **en el Paso 5h**, siguiendo `perfil_revista.md`.
Aquí solo se mira el alcance de cada candidata para el encaje.

## Tasa de aceptación: qué se puede decir y qué no

El investigador casi siempre quiere saber qué probabilidad tiene de que le
acepten el artículo. La respuesta honesta tiene dos partes y **hay que dar las
dos**.

### Lo que sí se puede reportar

**La tasa de aceptación que la propia revista o su editorial publican.** Algunas
lo hacen —en la página de la revista, en su sección de métricas o en la ficha
del editor— y otras no. Se busca en el sitio de la revista y se reporta con
fuente y fecha:

> *Tasa de aceptación: 18 %, dato publicado por la revista, consultado el
> [fecha].*

Si no la publica, se dice exactamente eso: **"la revista no publica su tasa de
aceptación"**. No se estima, no se infiere del cuartil, no se compara con "otras
revistas parecidas". No existe una base pública que dé la tasa de aceptación de
cualquier revista, y Scimago no la publica. Inventar un porcentaje aquí es
exactamente el error que este método existe para evitar.

Y una advertencia que conviene dar cuando el dato sí aparece: **la tasa de
aceptación mide el flujo de envíos de la revista, no la calidad del manuscrito
de quien pregunta.** Una revista con 10 % de aceptación que recibe muchos envíos
fuera de alcance rechaza a la mayoría en escritorio. Un buen manuscrito bien
dirigido no enfrenta ese 10 % como si fuera una lotería.

### Señales de capacidad, que no son la tasa de aceptación

Estos datos sí están en Scimago y orientan, pero **hay que presentarlos por lo
que son** y nunca convertirlos en un porcentaje:

- **Documentos publicados por año**. Una revista que publica 40 artículos al año
  y otra que publica 800 tienen capacidad muy distinta.
- **Historial de cuartiles**, que muestra si la revista es estable.
- **Tiempo hasta la primera decisión**, si la revista lo publica.

### El pronóstico de encaje

Lo que sí se puede evaluar con criterios verificables es el riesgo de **rechazo
de escritorio**: el que ocurre antes de la revisión, en días, sin un solo
comentario útil. Es el rechazo evitable, y es el que depende del autor.

Se reporta como alto, medio o bajo, con sus razones:

| Criterio | Pregunta | Dónde se verifica |
|---|---|---|
| Temático | ¿Esta revista ya publicó sobre este tema? | Los antecedentes del Paso 4 |
| Metodológico | ¿Publica estudios con este método? | Su último número |
| Extensión | ¿El diseño cabe en su límite de palabras? | Guía de autores |
| Idioma | ¿Acepta envíos en el idioma del autor? | Guía de autores |
| Legitimidad | ¿Pasó los chequeos antidepredadores? | `revista_depredadora.md` |

Al entregarlo, decir siempre esta frase o una equivalente: **el pronóstico de
encaje no es una probabilidad de aceptación.** La aceptación depende de la
revisión por pares y de la calidad del manuscrito terminado, que todavía no
existe. Prometer lo contrario sería vender humo.

## El encaje manda sobre el cuartil

Un Q1 cuyo alcance no corresponde rechaza el artículo **en escritorio**, sin
llegar a revisión: son semanas perdidas sin un solo comentario útil. Vale más un
Q2 que publica exactamente sobre el tema.

Tres pruebas de encaje que se pueden hacer sin ningún dato externo:

- **Temático**: ¿esta revista publicó algo parecido? La lista del Paso 4 lo
  responde.
- **Metodológico**: ¿publica estudios con este método? Algunas revistas de
  educación no publican SEM; algunas de psicometría no publican estudios sin
  validación de instrumento. Se mira su último número.
- **De extensión**: un modelo de mediación con cuatro constructos no entra en
  una revista de 4000 palabras sin sacrificar la metodología. Mejor saberlo
  ahora.

## Señales de alarma

Que una revista aparezca en Scimago significa que estuvo indexada, no que sea
buena elección hoy. Los chequeos de legitimidad y la lista de señales están en
`revista_depredadora.md`.

## Cómo se reporta

Siempre con fuente, año del indicador y fecha de consulta:

> *Q1 en Education según Scimago, dato de 2025, consultado por el investigador
> el 6 de septiembre de 2026. Cobertura 2010-2026.*

Nunca un cuartil suelto.
