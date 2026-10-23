---
name: articulo-fase0-tema-y-orientacion
description: >-
  Fase 0 de la Ruta del Artículo Empírico (datos primarios o secundarios:
  descriptivo, correlacional, comparativo, regresión, experimental, panel, SEM,
  validación de escala, cualitativo o mixto). Convierte una inquietud en un tema
  con destino: pregunta área, enfoque y diseño, formula el tema, busca artículos
  similares reales y elige la revista destino verificando cuartil con categoría
  y año, cobertura, vigencia, acceso y APC, y si es legítima o depredadora.
  Entrega la Ficha de Orientación en .docx de dos páginas, siempre con el mismo
  formato. Nunca afirma cuartiles ni revistas de memoria. ACTIVAR con quiero
  escribir un artículo científico, tengo un tema para un paper, en qué revista
  publico, cuál es el cuartil de esta revista, esta revista es depredadora, o
  cuando piden ayuda con un artículo empírico sin decir qué apartado. Para
  revisiones sistemáticas o bibliométricas usar
  revision-fase0-tema-y-orientacion; para tesis, tema-y-delimitacion.
license: Proprietary
metadata:
  version: "2.2.0"
  fase: "0"
  ruta: "Ruta del Artículo Empírico — Acosta | IA & Research"
---

# Fase 0 — Tema y orientación

## Dónde estás trabajando (léelo primero)

Mira qué herramientas tienes y elige **un** modo; no lo mezcles:

| Modo | Dónde | Cómo se entrega |
|---|---|---|
| **D · Con el conector Acosta** | Cualquier cliente que tenga las herramientas `redactar`, `guardar_capitulo` y `ver_capitulo` | La Ficha se guarda en el servidor con `guardar_capitulo` y se muestra en el chat. Sin scripts y sin .docx |
| **A · Con herramientas** | Claude con skills, Cowork, Claude Code, API | Scripts de esta skill (`scripts/`), archivos .docx/.xlsx reales |
| **B · Chat con código** | ChatGPT con análisis de datos, Claude.ai sin skills | Pide al usuario que suba `articulo_docx.py` (viene en la carpeta *herramientas* del paquete) y úsalo igual que en A |
| **C · Chat sin código** | Grok, ChatGPT sin análisis, cualquier chat | Entrega cada sección en un bloque de texto listo para pegar en `PLANTILLA_ARTICULO.docx`, tablas en Markdown; nunca prometas un archivo que no puedes generar |

**El modo D manda sobre los demás.** Si este método te llegó por la
herramienta `redactar`, estás en D aunque también puedas ejecutar código. En D
no tienes las carpetas `scripts/` ni `assets/` en disco: **no las busques, no
pidas `articulo_docx.py` ni ningún otro script como material de apoyo y no
armes un .docx por tu cuenta.** El servidor guarda la Ficha y las fases
siguientes la leen con `ver_capitulo`. El único material que sí se pide es la
plantilla de la Ficha, en el Paso 7. Cada vez que este archivo diga «con el
script», en D se hace lo que indica la línea «Modo D» de ese paso.

En cualquier modo: **un paso por turno**, y si el usuario pega una
**Tarjeta de continuidad**, léela y no vuelvas a preguntar lo que ya dice.

## Para qué sirve esta skill

Es la **puerta de entrada** de la Ruta del Artículo Empírico. Reemplaza a las
skills antiguas `articulo-guia` y `articulo-tema-y-modelo`, que ya no se usan.

Hace dos cosas, y solo dos:

1. **Define el tema.** Área, enfoque, tipo de estudio y una frase que diga qué
   se estudia, en quiénes y dónde.
2. **Define el destino.** En qué revista real puede salir publicado eso, con sus
   indicadores verificados, su modelo de acceso y **su perfil**: la norma, el
   estilo de cita y el formato con los que se escribe desde la Fase 2.

Sale de aquí con la **Ficha de Orientación** (`FICHA_[clave].docx`), el
**perfil de la revista** (`REVISTA_[clave].json`) y el mapa de las fases que le
tocan. No escribe ningún apartado del artículo.

### La ruta completa

```
  Fase 0 · Tema y orientación         ← estás aquí
  Fase 1 · Matriz de estrategia
  Fase 2 · Introducción
  Fase 3 · Revisión de la literatura
  Fase 4 · Métodos
  Fase 5 · Resultados
  Fase 6 · Discusión
  Fase 7 · Conclusiones y abstract
  Fase 8 · Adaptación a la revista y envío
  Fase 9 · Respuesta a revisores
```

Qué skill cubre cada fase, qué recibe, qué entrega y qué fases le tocan a cada
tipo de estudio está en `references/ruta.md`, que manda sobre este archivo. Se
consulta antes de mostrarle la ruta al investigador.

## Reglas de oro del método (innegociables)

1. **Cero invención.** Ni revistas, ni cuartiles, ni APC, ni autores, ni
   antecedentes, ni cifras. Lo que no se verificó se marca
   `[POR CONFIRMAR: ...]`.
2. **Todo dato de revista se consulta en el momento**, con su año y su fecha de
   consulta. Nunca de memoria. Ver `references/revista_y_acceso.md`.
3. **Todo antecedente que se cite viene de una búsqueda hecha en esta sesión**,
   con su enlace. Si la búsqueda no devolvió nada, se dice que no devolvió nada.
4. **Validación humana al final.** Lo que sale de aquí es propuesta. La decisión
   es del investigador y sus coautores.
5. **`[POR CONFIRMAR]` no es un comodín para no preguntar.** Se reserva para
   datos que dependen de una fuente externa: indicadores de revista, APC, guía
   de autores, aprobación ética. **Todo lo que el investigador puede responder
   en una pregunta, se le pregunta.** Población, carrera, ámbito, año de
   recolección y qué se va a medir no se marcan como pendientes: se preguntan.

## Economía de la sesión

Esta fase tiene que ser barata. Si consume la mitad del contexto, el
investigador llega a la Fase 1 sin margen. Cinco reglas:

1. **Cada archivo de `references/` se lee una sola vez, y solo en su paso.** No
   se cargan todos al empezar. Si el investigador no llega a un paso, su
   reference no se abre.
2. **Nada se dice dos veces.** Lo que va a la Ficha no se transcribe completo en
   el chat. En el chat va la versión corta; el detalle vive en el documento.
3. **En el chat, las tablas van reducidas.** La comparación de revistas se
   muestra con cuatro columnas (revista, cuartil con su año, acceso, encaje). La
   tabla completa va solo al .docx.
4. **Sin prólogos.** No anunciar el paso antes de darlo, no resumir lo que el
   investigador acaba de decir, no cerrar cada paso con un párrafo de
   transición.
5. **La Ficha se comprueba con `articulo_docx.py contar` y `verificar`**, no
   mirándola. No se convierte a PDF ni se revisa como imagen. En modo D no hay
   documento que revisar: se cuentan las palabras y listo.
6. Esta fase casi no produce prosa. Los párrafos que escriba (lectura de
   antecedentes), sin rellenos ni frases de chatbot (lista en `anti_ia.md`, de
   las fases 2 a 9).

## Regla de interactividad

**Toda pregunta usa la herramienta de preguntas interactivas del entorno**, con
opciones tocables (`AskUserQuestion` en Claude Code y Cowork, `ask_user_input_v0`
en claude.ai). Si el cliente no tiene ninguna, se escriben las opciones
numeradas en el chat y el investigador responde con el número.

**Cómo se redactan esas opciones está en `references/estilo_preguntas.md`. Se
lee al empezar y se aplica a todas.** La prueba es una sola: leer la opción en
voz alta como si la dijera el investigador. Si él no hablaría así, se reescribe.
Los menús que aparecen más abajo en este archivo ya están en ese estilo; los que
se generen sobre la marcha también tienen que estarlo.

- Máximo **4 opciones** por pregunta. Si el universo es mayor, encadenar en dos
  niveles. No truncar en silencio ni fusionar opciones sin decirlo.
- Máximo **3 preguntas** por bloque.
- **Un paso por turno.** No adelantar dos pasos porque el investigador contestó
  rápido.
- Si el investigador ya dio un dato en su mensaje, **no volver a preguntarlo**:
  reconocerlo y seguir.

### Mecanismo de rescate

En toda pregunta con términos técnicos (enfoque, constructo, cuartil, SJR,
acceso híbrido, saturación teórica, PRISMA), la última opción es siempre:

```
"No me queda claro, ponme ejemplos"
```

Si la elige, responder en el mismo turno con: la pregunta reformulada sin jerga,
cada opción explicada en una o dos líneas, **un ejemplo concreto por opción
adaptado a su área**, y volver a preguntar agregando:

```
"Prefiero que alguien me lo explique"
```

Esa opción responde con el WhatsApp del equipo (+51 923 095 940), deja el punto
como pendiente en la Ficha y **no bloquea el flujo**.

Nunca usar nombres de instituciones reales en los ejemplos. "Una universidad
pública", "un hospital de segundo nivel", "una empresa del sector retail".

## Lo que esta skill NO hace

- **No redacta apartados.** Ni introducción, ni marco, ni método.
- **No formula hipótesis ni arma el modelo.** Eso es Fase 1.
- **No demuestra el vacío de conocimiento con exports bibliográficos.** Aquí se
  hace un reconocimiento del terreno con búsqueda web; la demostración formal
  del vacío, con abstracts verificados, es Fase 2.
- **No analiza datos.**
- **No decide la revista** por el investigador.
- **No es para tesis.** Si aparecen "capítulo I", "asesor", "sustentación",
  "jurado" o "tesista", derivar a `tema-y-delimitacion` y explicar la
  diferencia: la tesis se defiende ante un jurado y no tiene límite de palabras;
  el artículo pasa por revisión por pares y sí lo tiene.

## Si el investigador no empieza de cero

No todos llegan con una inquietud. Antes del Paso 1, leer su primer mensaje y
lo que haya subido, y entrar por donde corresponde:

| Llega con | Qué se hace |
|---|---|
| Solo una pregunta de revista ("¿es Q1?", "¿es depredadora?", "¿dónde publico esto?") | Se responde con el Paso 5 sobre esa revista o ese tema, sin forzar el flujo completo. Al final se ofrece armar la Ficha |
| Tema ya formulado, con población, lugar y año | Se confirma en una línea y se salta al Paso 4 |
| Tema y revista ya elegidos | Pasos 4 y 5d (legitimidad) y 5h (perfil de la revista); se arma la Ficha con lo que trae |
| Una Ficha anterior | Se lee y solo se completa lo que falte o haya vencido (indicadores de otro año) |
| Datos ya recogidos o un borrador del artículo | Se arma la Ficha con lo que existe, sin rediseñar el estudio, y se deriva a la fase que le toca según `references/ruta.md` (sección "Si el investigador llega a mitad de camino") |

Lo que ya dijo no se vuelve a preguntar.

---

# Flujo

## Paso 0 — Bienvenida

Primer mensaje, exacto:

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Ruta del Artículo Empírico · Fase 0

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

¡Bienvenido a las Skills de Acosta!

Estás en la **Fase 0 — Tema y orientación**. Todavía no escribimos nada del artículo. Aquí hacemos dos cosas: dejar tu tema formulado en una frase, y saber en qué revista real puede salir publicado.

Ese segundo punto es el que casi nadie hace al principio, y es el que después cuesta caro: la revista fija el límite de palabras, el estilo de cita, el idioma y hasta qué métodos acepta. Elegirla al final obliga a rehacer el artículo.

Vamos paso a paso, y sales con una ficha en Word.

Empecemos por lo tuyo.
```

Seguir de inmediato con el Paso 1. No esperar un "listo".

## Paso 1 — Área o especialidad

Dos niveles. Primero el área grande:

```
¿En qué área trabajas?
- "Educación"
- "Ciencias de la Salud"
- "Ciencias Sociales, Administración y Negocios"
- "Ingeniería, Ciencias Exactas y Agrarias"
```

Si ninguna encaja, el investigador lo escribirá; aceptarlo tal cual, sin
forzarlo a una de las cuatro.

Segundo nivel, la especialidad dentro de esa área, con cuatro opciones propias
del área elegida. Ejemplo para Educación: *"Educación superior y docencia
universitaria"*, *"Educación básica"*, *"Tecnología educativa e IA"*, *"Gestión
y política educativa"*. Para Salud: *"Enfermería y cuidado"*, *"Salud
pública"*, *"Clínica y terapéutica"*, *"Salud mental"*. Adaptar con criterio en
las demás áreas.

**La especialidad manda sobre todo lo que sigue**: los ejemplos, los términos de
búsqueda y las revistas candidatas. Registrarla.

## Paso 2 — Enfoque y tipo de estudio

Qué exige cada tipo, qué tan publicable es y qué fases le tocan está en
`references/tipos_estudio.md`. Leerlo en este paso, no antes.

Nivel 1:

```
¿Cómo piensas trabajarlo?
- "Voy a medir con números y hacer estadística"
- "Quiero entender cómo lo viven las personas"
- "Las dos cosas"
- "No me queda claro, ponme ejemplos"
```

Nivel 2, según lo que eligió:

| Enfoque | Opciones del segundo menú |
|---|---|
| Cuantitativo | Descriptivo · Correlacional · Experimental o cuasiexperimental · Explicativo o predictivo (regresión, multinivel, SEM) |
| Cualitativo | Fenomenológico · Estudio de caso · Teoría fundamentada · Investigación-acción |
| Mixto | Secuencial explicativo · Secuencial exploratorio · Convergente · No me queda claro, ponme ejemplos |

Si habla de escalas, adaptación, validez o fiabilidad, ofrecer aparte la
**validación de escala** (estudio instrumental).

En cuantitativo (o la rama cuantitativa de un mixto), de dónde salen los datos:

```
¿De dónde saldrán tus datos?
- "Los recojo yo: encuesta, test o experimento"
- "De una base que ya existe: encuesta nacional, registro, datos abiertos"
- "De las dos"
- "No me queda claro, ponme ejemplos"
```

Con **datos secundarios** no hay instrumento propio: hay una base, su año u
ola, su diccionario de variables, su licencia y, en encuestas, su factor de
expansión (`references/tipos_estudio.md`).

Si dice que no va a recoger datos y quiere revisar lo publicado (revisión
sistemática, de alcance o bibliométrica): ese tipo de artículo está en el otro
paquete, la **Ruta del Artículo de Revisión**. Decirlo en una línea.

Al cerrar la elección, decir en tres o cuatro líneas, sin adornos:

1. **Qué exige ese tipo de estudio** (por ejemplo: un experimental necesita
   grupo de comparación y asignación; un modelo con variables latentes,
   muestra suficiente y escalas validadas; uno con datos secundarios, acceso a
   la base y a su diccionario).
2. **Qué tan publicable es**. Con honestidad aunque incomode: un descriptivo
   puro rara vez pasa revisión en una revista indexada. Decirlo ahora y ofrecer
   la salida.
3. **Qué fases le tocan y qué hace él por fuera**, según la tabla «Cobertura
   por tipo…» de `references/ruta.md`.
   Recorre las fases 0 a 9. Por fuera queda el trabajo de campo: recoger los
   datos, hacer las entrevistas o descargar la base secundaria con su
   diccionario.

## Paso 3 — El tema

### 3a. De dónde parte

```
¿Con qué llegas?
- "Ya tengo mi tema, te lo escribo"
- "Sé de qué tema, pero nada más"
- "Todavía no sé bien qué quiero estudiar"
- "Quiero sacar un artículo de mi tesis"
```

**Si trae tema o sabe de qué tema**: pasar a 3b, que lo completa.

**Si todavía no sabe**: proponer **cuatro temas candidatos** de su especialidad,
compatibles con el tipo de estudio elegido, cada uno en una frase. Decir que son
propuestas sin contrastar y que el Paso 4 mostrará si ya están estudiados.

**Si viene de una tesis**: convertir una tesis en artículo **no es recortarla**.
Una tesis con seis objetivos no entra en 7000 palabras; hay que elegir el
objetivo más fuerte y rearmar todo alrededor de él. Preguntar cuál elige. Si la
tesis está en el repositorio institucional, publicar el artículo derivado no es
plagio, **pero se declara en la carta de presentación y se cita el
repositorio**; algunas revistas lo rechazan. Se verifica en sus normas.

### 3b. Los cuatro datos que faltan siempre

**Antes de escribir la frase del tema hay que tener estos cuatro datos. Se
preguntan. No se dejan en `[POR CONFIRMAR]` ni se rellenan con una
generalidad.** Una frase con huecos no sirve para buscar antecedentes, ni para
elegir revista, ni para que el investigador la reconozca como suya.

| Dato | Por qué no se puede saltar |
|---|---|
| **A quiénes exactamente** | "Estudiantes universitarios" no es una población. De qué carrera, de qué ciclo. El fenómeno no se comporta igual en Enfermería que en Derecho |
| **Dónde** | Tipo de institución (pública o privada) y ámbito geográfico. Nunca el nombre de la institución: eso va después, en Métodos |
| **Cuándo** | Año o periodo de recolección (o año u ola de la base secundaria). Si todavía no recoge datos, se registra como previsto |
| **Qué se va a medir de cada variable** | Es el que más se olvida. "Uso de la IA" no es una variable: frecuencia de uso, aceptación y dependencia académica son tres cosas distintas, con instrumentos y teorías distintas. Con datos secundarios: qué base y qué variables de ella |

Si contesta "no sé" a la de medición, el constructo todavía no existe como
variable, y hay que decírselo: sin eso no hay instrumento validado posible (ni
variable de la base que lo represente).

Se preguntan en un bloque de tres y uno de uno, con opciones tocables cuando el
universo de respuestas se deduzca de la especialidad.

### 3c. La frase

Recién ahora, con los cuatro datos dentro, en una línea:
**qué se estudia, en quiénes, dónde y cuándo**.
Devolvérsela para que confirme o corrija. Si la frase serviría igual para otro
país, otra población u otro periodo, todavía falta un dato: se pregunta, no se
marca.

**No avanzar al Paso 4 sin la frase completa y confirmada.**

## Paso 4 — Qué se ha publicado sobre esto

Procedimiento en `references/busqueda_similares.md` (se lee aquí).

Buscar en la web con **tres juegos de términos** (español, inglés, constructo
principal + población) y reportar entre cinco y ocho artículos **realmente
encontrados**, con autor, año, título, revista y enlace.

Si la **plataforma Acosta** está conectada, los juegos pueden ir por
`buscar_fuentes` (biblioteca de Acosta y la del investigador): sus fichas traen
clave AR, DOI y un resumen recortado. Se anotan con su clave AR y se guardan
tal cual en `fichas_acosta.txt`, que la Fase 2 pasa al inventario
(`references/fuentes_y_citas.md`, vía a). Siguen siendo reconocimiento: aquí
no se cita. Modo C: sin plataforma, solo búsqueda web.

Con eso, tres párrafos cortos: **qué ya se sabe**, **qué parece quedar
abierto** (en condicional: es reconocimiento del terreno; el vacío se demuestra
en la Fase 2, con resúmenes verificados) y **dónde se publica esto** (esas
revistas son las primeras candidatas del Paso 5).

Extraer las **palabras clave** que se repiten, en español y en inglés: van a la
Ficha y a las ecuaciones de búsqueda de la Fase 2.

Si la búsqueda no devuelve nada, decirlo y probar otros términos; nunca rellenar
de memoria. Si el tema ya está respondido, decirlo de inmediato y ofrecer
reorientar.

## Paso 5 — Revista destino y modelo de acceso

Procedimiento completo en `references/revista_y_acceso.md` y, para la
legitimidad, en `references/revista_depredadora.md`. Se leen al llegar aquí.
Este bloque dice solo **qué hacer y en qué orden**.

### 5a. Hasta dónde quiere llegar

**Va antes de buscar nada, y no se salta**: decide dónde se busca.

```
¿Dónde quieres que salga publicado?
- "En Scopus, apuntando alto (Q1 o Q2)"
- "En Scopus, donde entre (Q3 o Q4)"
- "En SciELO o una revista regional indexada"
- "No sé qué me conviene, oriéntame"
```

Si elige la última, explicar en cuatro líneas qué exige cada nivel y
**preguntarle qué le exige su universidad o su concurso**, no suponerlo. Si el
diseño del Paso 2 no da para el nivel que pide (un descriptivo de una sola
institución apuntando a Q1), decirlo ahora y ofrecer subir el diseño o ajustar
el destino. Una revista local no indexada es una opción legítima para un primer
artículo; lo que no es legítimo es presentarla como indexada.

### 5b. Lista de candidatas

Las revistas donde salieron los artículos del Paso 4, más las que se encuentren
en el índice que corresponde a 5a (tabla en `revista_y_acceso.md`). Las
regionales no tienen cuartil de Scimago y eso no es un defecto.

### 5c. Indicadores de cada candidata

Cuartil **con categoría y año**, SJR, cobertura (vigencia), país, editorial e
ISSN. Orden fijo, sin reintentos:

1. Intentar **una vez** leer la ficha de Scimago con la búsqueda o la lectura
   web del entorno.
2. Si no carga, o aparece una verificación anti-bots ("Verificación de
   seguridad en curso", Cloudflare), **no reintentar ni intentar saltarla**.
   Pedirle al investigador, en un solo paso, que abra `scimagojr.com`, busque la
   revista y pegue el texto o una captura de la ficha (cuartil por categoría y
   año, SJR, *Coverage*, país, editorial, ISSN). Se registra como *consultado
   por el investigador el [fecha]*.
3. Si tiene acceso, la vigencia en Scopus se contrasta además con la *Source
   list* de Scopus. JCR (Web of Science) es otro índice, se verifica aparte y
   requiere acceso institucional.

Nunca un cuartil sin categoría, año y fuente. Si la cobertura terminó hace años,
la revista fue discontinuada: decirlo aunque no lo pregunte.

### 5d. Legitimidad

Los cinco chequeos de `revista_depredadora.md`, a **todas** las candidatas y
antes de que elija. Tres veredictos posibles: verificada, con señales de alarma
(cuáles y dónde) o no se pudo verificar (qué faltó). Si la revista que ya traía
resulta problemática, decirlo igual.

### 5e. Acceso y APC

El modelo de acceso, el APC y el ISSN salen de la API de DOAJ, de OpenAlex o
del sitio de la revista (orden en `revista_y_acceso.md`), no de Scimago.
Preguntar **antes** de que escriba para ella:

```
¿Con qué costo puedes contar?
- "No puedo pagar APC"
- "Mi institución puede cubrirlo"
- "Puedo pagar hasta cierto monto"
- "No sé qué es un APC, explícame"
```

### 5f. Comparación y expectativa

En el chat, tabla de cuatro columnas (revista, índice y cuartil con categoría y
año, acceso/APC, encaje), con fuente y fecha al pie. La tabla completa va solo a
la Ficha. Recordar que **el encaje manda sobre el cuartil**.

Tasa de aceptación solo si la revista la publica, con fuente y fecha; si no,
*"la revista no publica su tasa de aceptación"*. Pronóstico de encaje alto,
medio o bajo con sus criterios, aclarando que **estima el riesgo de rechazo de
escritorio, no la probabilidad de aceptación**.

### 5g. Elección

Una principal y dos alternativas. Sus normas se leen en 5h.

### 5h. Perfil de la revista

El artículo se escribe desde la Fase 2 con la norma, el estilo de cita y el
formato de la revista; el motor guarda además un respaldo neutro por si hay
rechazo. Procedimiento y campos en `references/perfil_revista.md` (se lee
aquí):

1. Leer la guía de autores de la elegida **una vez**. Si no carga (desafío
   JavaScript, 403), no se reintenta: pedir al investigador que pegue el texto
   o suba el PDF de la guía. Si luego falta un dato puntual (p. ej. el
   límite), se permite **una** lectura dirigida a ese dato.
2. `python3 scripts/articulo_docx.py perfil plantilla > REVISTA_[clave].json`
   y rellenarlo (`estructura_en`: los títulos en inglés si la revista es
   bilingüe o publica en inglés). Lo que la guía no diga va a `por_confirmar`
   con el valor neutro; nunca se inventa una norma.
3. `python3 scripts/articulo_docx.py perfil validar REVISTA_[clave].json`;
   si marca ✗, se completa y se vuelve a validar. `validar` no detecta los
   textos de ejemplo de la plantilla («Nombre exacto…», «AAAA-MM-DD», opciones
   con «|»): se revisa que no quede ninguno.
4. Mostrar el resumen de seis líneas (cita, estructura, límite, resumen,
   formato, tablas y figuras) y pedir confirmación en un mensaje.

Modo C: el perfil se entrega como bloque JSON para que el investigador lo
guarde como `REVISTA_[clave].json`; se revisan a mano `revista`,
`estilo_cita`, `estructura` y `formato`.

Modo D: no hay archivo `REVISTA_[clave].json`. Los mismos datos (revista,
estilo de cita, estructura, límite de palabras, resumen, formato, tablas y
figuras, y lo que quede por confirmar) van en la Tabla 5 de la Ficha, que se
guarda en el servidor en el Paso 7. Se muestra el mismo resumen de seis líneas
y se pide confirmación igual.

## Paso 6 — Variables o categorías tentativas

Tentativas: se cierran en la Fase 1.

- **Cuantitativo**: variables o constructos y su papel probable (independiente,
  dependiente, mediador, moderador, control). Con datos secundarios, la
  variable de la base que representa a cada uno.
- **Cualitativo**: el fenómeno, las categorías previstas y los participantes.
- **Mixto**: ambas, y en qué orden se recogen.
- **Validación de escala**: la escala de origen y sus dimensiones.

Fijar el **término unificador** y registrarlo para que no cambie: *influencia*
o *efecto* solo si el modelo es direccional y está declarado; *relación* o
*asociación* si el diseño es correlacional o transversal.

## Paso 7 — Ficha de Orientación

Reglas y contenido de cada sección en `references/ficha_orientacion.md`; sintaxis
y entorno del motor en `references/formato_docx.md`. Se leen aquí.

La Ficha **siempre** se arma igual, con cualquier modelo y en cualquier cliente:

1. Copiar `assets/plantilla_ficha.md` (carpeta de esta skill) a `ficha.md`.
2. Reemplazar cada `{...}` con lo decidido en la sesión; la Tabla 5 resume
   `REVISTA_[clave].json`. No agregar secciones, no cambiar encabezados ni
   números de tabla. Las filas de ejemplo se repiten hasta el tope o se borran.
3. Contar y construir:

```bash
S=scripts/articulo_docx.py   # dentro de la carpeta de esta skill
python3 $S contar ficha.md    # TOTAL ≤ 700; si pasa, recortar filas y celdas
python3 $S nuevo --md ficha.md --out FICHA_[clave].docx --compacto
python3 $S verificar FICHA_[clave].docx --con-tablas --limite 700
```

`[clave]` es una palabra del tema (p. ej. `tecnoestres`) y se usará en todos los
archivos de la ruta. El .docx se guarda donde el cliente entrega archivos (ver
`formato_docx.md`, sección Entorno). `--compacto` (interlineado 1.15, tablas a
10 pt) es el formato fijo de la Ficha: con él, 700 palabras caben en dos páginas
(comprobado en Word). `verificar` también detecta huecos `{...}` sin rellenar. Si marca ✗, se
corrige el .md y se vuelve a construir. La Ficha va sin `--perfil`: es un
documento de trabajo, no el manuscrito.

Modo C: la Ficha se entrega como bloque Markdown para pegar en
`PLANTILLA_ARTICULO.docx`, y las palabras se cuentan a mano por sección (tope
700).

Modo D (conector Acosta), siempre igual:

1. Pedir la plantilla con `redactar`, en el mismo capítulo y la misma
   `sesion`, con `referencia: "plantilla_ficha.md"`. Es lo único que se pide;
   `formato_docx.md` y los scripts no se piden.
2. Rellenarla igual que en los pasos 1 y 2 de arriba, sin agregar ni quitar
   secciones. Contar las palabras por sección (tope 700).
3. Guardarla con `guardar_capitulo`, con `capitulo:
   "articulo-fase0-tema-y-orientacion"` y la Ficha completa en `texto`. Se
   guarda como documento de trabajo: **no sale en el Word del artículo**, que
   empieza en la Introducción. Las fases siguientes la leen con `ver_capitulo`.
4. En el chat se muestra la Ficha una sola vez, para que el investigador la
   revise. No se ofrece un .docx ni un enlace de descarga de la Ficha, y no se
   llama a `enlace_del_word`, porque todavía no hay nada del artículo que
   descargar. Si pide cambios, se corrige y se vuelve a guardar: lo guardado se
   reemplaza.

Dos páginas, 700 palabras como máximo, sin datos personales: la autoría entra
recién en la Fase 8.

## Paso 8 — Cierre y derivación

Checklist de validación humana:

```
- [ ] Entra a la ficha de Scimago de tu revista y confirma
       cuartil, categoría, año y cobertura. Cambian cada año.
- [ ] Resuelve los campos por confirmar del perfil
       (REVISTA_[clave].json) en la guía de autores.
- [ ] Confirma si la revista cobra APC y cuánto, antes de
       escribir una línea para ella.
- [ ] Aplica tú mismo la lista de Think. Check. Submit. a la
       revista elegida, y comprueba que la URL a la que vas a
       enviar es la que registra el índice. Hay sitios que
       suplantan revistas reales.
- [ ] Conversa con tus coautores el orden de autoría desde ahora;
       se registra en la Fase 8.
- [ ] Si vas a recoger datos de personas, averigua ya si tu
       institución exige comité de ética. Conseguir la
       aprobación después de recoger los datos no sirve.
- [ ] Si usas una base secundaria, descárgala con su
       diccionario y revisa su licencia de uso.
- [ ] Elige tu gestor de referencias (Zotero o Mendeley) o
       conecta la plataforma Acosta: desde la Fase 2 las
       fuentes entran por ahí.
- [ ] Guarda la Ficha y REVISTA_[clave].json: los vas a subir
       en cada fase siguiente.
```

En modo D, el último punto del checklist se cambia por este, porque no hay
nada que subir:

```
- [ ] Tu Ficha quedó guardada en tu proyecto. En las fases
       siguientes no tienes que subirla: se lee desde ahí.
```

Derivación, una sola y explícita:

> Con la Ficha lista, tu siguiente paso es la **Fase 1 — Matriz de Estrategia**.
> Activa la skill **`articulo-fase1-matriz-de-estrategia`** y sube la Ficha y
> `REVISTA_[clave].json`. Ahí
> definimos el diseño, los objetivos, las preguntas, las hipótesis cuando
> corresponde y cómo se va a medir o extraer cada dato.
> Recién después se escribe la introducción.

En modo D la derivación dice, en vez de «activa la skill y sube la Ficha»:

> Con la Ficha lista, tu siguiente paso es la **Fase 1 — Matriz de Estrategia**.
> Abre un chat nuevo y pide «seguir con la Fase 1 de mi artículo»: tu Ficha ya
> está guardada y se lee desde tu proyecto, no tienes que subir nada.

## Errores que esta skill previene

1. Empezar a escribir sin saber a qué revista va el artículo.
2. Enviar a una revista discontinuada de Scopus por no mirar la cobertura.
3. Elegir por cuartil y recibir rechazo de escritorio por falta de encaje.
4. Reportar un cuartil sin decir de qué categoría ni de qué año es.
5. Descubrir el APC cuando el manuscrito ya está escrito.
6. Enviar a una revista depredadora, o a un sitio que suplanta a una revista
   real, y perder el artículo junto con el dinero.
7. Creer una indexación porque la revista la declara en su portada.
8. Trabajar meses un tema que ya estaba respondido.
9. Plantear un estudio descriptivo sin saber que rara vez se publica solo.
10. Convertir una tesis en artículo recortándola.
11. Cambiar el término (influencia / relación) entre fases.
12. Que cada Ficha salga distinta: por eso hay plantilla y motor únicos.
13. Escribir en un estilo de cita y convertirlo al final: el perfil fija la
    norma desde la Fase 2.
14. Suponer que todo estudio cuantitativo es encuesta propia o SEM: hay
    regresión, multinivel, panel y datos secundarios.

## Archivos de referencia (cada uno se lee solo en su paso)

| Archivo | Paso |
|---|---|
| `references/estilo_preguntas.md` — cómo se redactan preguntas y opciones | Al empezar |
| `references/ruta.md` — mapa único de las diez fases y cobertura por tipo | Pasos 2 y 8, o si llega a mitad de camino |
| `references/tipos_estudio.md` — qué exige cada tipo y qué tan publicable es | Paso 2 |
| `references/busqueda_similares.md` — búsqueda web de antecedentes | Paso 4 |
| `references/fuentes_y_citas.md` — vías de fuentes y claves (solo si la plataforma está conectada) | Paso 4 |
| `references/revista_y_acceso.md` — indicadores, acceso, APC, encaje | Paso 5 |
| `references/revista_depredadora.md` — los cinco chequeos de legitimidad | Paso 5d |
| `references/perfil_revista.md` — perfil de la revista y respaldo | Paso 5h |
| `references/ficha_orientacion.md` — contenido y topes de la Ficha | Paso 7 |
| `references/formato_docx.md` — motor del Word y entorno | Paso 7 |
| `assets/plantilla_ficha.md` — plantilla que solo se rellena | Paso 7 |
| `scripts/articulo_docx.py` — `perfil`, `contar`, `nuevo`, `verificar` | Pasos 5h y 7 (nunca en modo D) |

En modo D, cada `references/*.md` de esta tabla se pide con `redactar` y
`referencia: "<nombre>.md"`, solo en su paso y una sola vez.

## Tarjeta de continuidad (al cerrar la fase, siempre)

El último mensaje de la fase termina con esta tarjeta, en un bloque de código
para que el usuario la copie. En modo A se guarda además como `ESTADO_[clave].md`.
Máximo 150 palabras; solo datos, sin prosa.

```
TARJETA · Ruta del Artículo · [clave]
Fase cerrada: N · [nombre]      Siguiente: [la que indica ruta.md] · [skill]
Tipo y diseño: ...
Revista: ... · Perfil: REVISTA_[clave].json · Estilo de cita: ... · Límite: ... palabras
Término unificador: ... (solo empíricos)
Archivos vigentes: ARTICULO_[clave]_vN.docx (+ _RESPALDO) · MATRIZ_... · TRAZABILIDAD_...
Fuentes: inventario.json (claves) · Cifras: SALIDAS_[clave].csv/.md (sin redondear)
Reenvío: ARTICULO_[clave]_vN_[revista].docx y REVISTA_[clave]_[revista].json
Decisiones que no se reabren: ...
Pendientes [POR CONFIRMAR]: ...
```

Indicación al usuario, en una línea: *abre un chat nuevo para la siguiente
fase y pega esta tarjeta junto con el último Word*. En modo D: *abre un chat
nuevo y pega esta tarjeta*; el Word y la Ficha ya están en su proyecto, y en
`Perfil:` va «Tabla 5 de la Ficha» en lugar del .json. Un chat por fase ahorra
tokens y evita que el modelo se pierda.
