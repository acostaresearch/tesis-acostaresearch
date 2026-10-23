---
name: articulo-fase4-metodos
description: >-
  Fase 4 de la Ruta del Artículo Empírico: redacta Métodos y los une al mismo
  Word. Escribe cinco subtítulos (enfoque y diseño; participantes; instrumentos;
  procedimiento y análisis de datos; aspectos éticos), describe la fuente si los
  datos son secundarios (acceso, versión, ponderadores) y calcula la Tabla 1
  desde la base de datos (en el servidor R de Acosta o con su script), no de
  memoria. Tiene estructura propia para diseños correlacionales, de regresión,
  SEM, experimentales, instrumentales, cualitativos y mixtos. Nunca inventa
  muestras, fechas, software, ítems eliminados ni aprobaciones de ética: lo que
  no conste queda como pendiente. Escribe en español con la norma, el estilo de
  cita y el formato de la revista destino, humaniza la sección y entrega la
  versión de la revista y su respaldo neutro. ACTIVAR con metodología de mi
  artículo, método del paper, participantes e instrumentos, tabla
  sociodemográfica, tabla 1, o cuando suban su base de datos o el Word de la
  Fase 3.
license: Proprietary
metadata:
  version: "2.2.0"
  fase: "4"
  ruta: "Ruta del Artículo Empírico — Acosta | IA & Research"
---

# Fase 4 — Métodos

## Dónde estás trabajando (léelo primero)

Mira qué herramientas tienes y elige **un** modo; no lo mezcles:

| Modo | Dónde | Cómo se entrega |
|---|---|---|
| **A · Con herramientas** | Claude con skills, Cowork, Claude Code, API | Scripts de esta skill (`scripts/`), archivos .docx/.xlsx reales |
| **B · Chat con código** | ChatGPT con análisis de datos, Claude.ai sin skills | Pide al usuario que suba `articulo_docx.py` (viene en la carpeta *herramientas* del paquete) y úsalo igual que en A |
| **C · Chat sin código** | Grok, ChatGPT sin análisis, cualquier chat | Entrega cada sección en un bloque de texto listo para pegar en `PLANTILLA_ARTICULO.docx`, tablas en Markdown; nunca prometas un archivo que no puedes generar |

En cualquier modo: **un paso por turno**, y si el usuario pega una
**Tarjeta de continuidad**, léela y no vuelvas a preguntar lo que ya dice.

## Para qué sirve esta skill

Escribe la sección que permite que otro investigador **repita el estudio**. Es
la que más se lee en la revisión por pares y la que más rechazos provoca, no por
mal escrita sino por incompleta.

Y es el apartado donde una invención hace más daño: un tamaño de muestra, una
fecha de búsqueda o recolección, o una aprobación que no existen comprometen al
autor ante la revista.

### La ruta completa

```
  Fase 0 · Tema y orientación
  Fase 1 · Matriz de estrategia
  Fase 2 · Introducción
  Fase 3 · Revisión de la literatura
  Fase 4 · Métodos                     ← estás aquí
  Fase 5 · Resultados
  Fase 6 · Discusión
  Fase 7 · Conclusiones y abstract
  Fase 8 · Adaptación a la revista y envío
  Fase 9 · Respuesta a revisores
```

Insumos, entregables y quién decide cada dato: `references/ruta.md` (manda
sobre este archivo si algo no coincide).

Si el estudio es una revisión sistemática, de alcance o bibliométrica, su
Métodos está en la **Ruta del Artículo de Revisión**.

## Regla de oro: veracidad absoluta

1. **La Tabla 1 se calcula desde la base**, nunca se estima.
2. **Nada se declara sin confirmación**: tipo de muestreo, tamaño de la
   población, fechas de recolección, software y versión, código del comité de
   ética. Lo que no conste queda `[POR CONFIRMAR: ...]`.
3. **No se afirma consentimiento informado, anonimato ni aprobación ética si el
   investigador no lo confirma**, una declaración a la vez.
4. **Los ítems eliminados se preguntan.** No se inventa cuáles cayeron.
5. **Si la base contradice las salidas del análisis** (otro n, otra
   institución, otro método), se señala y se pregunta **antes** de redactar. No
   se elige el dato que convenga.
6. **Métodos va en pasado.** Si el campo no ocurrió todavía, no se escribe.
7. **Datos secundarios: no se describen como propios.** No se escribe «se
   aplicó un cuestionario» a una encuesta que levantó otro: se dice quién la
   levantó, cómo se accedió y qué versión se usó.

## Regla del acompañamiento: el investigador es novato

- **Un paso por turno.**
- Toda pregunta técnica lleva como última opción `"No me queda claro, ponme
  ejemplos"`, y si sigue trabado, `"Prefiero que alguien me lo explique"`, que
  responde con el WhatsApp del equipo (+51 923 095 940) y deja el punto
  pendiente sin bloquear.
- Las preguntas de este apartado son **de memoria, no de criterio** (fechas,
  software, permisos). Si no las recuerda, decirle dónde buscarlas: el correo de
  la aprobación, el historial de búsquedas de la base, la bitácora.
- Redacción de las opciones en `references/estilo_preguntas.md`.

## Economía de la sesión

1. Cada archivo de `references/` se lee **solo en el paso que lo pide**.
2. Del Word se lee el `esquema` y, si hace falta, una sección con
   `texto --seccion`. Nunca el artículo entero.
3. Lo que el investigador ya aprobó se escribe al `.md` de la sección y no se
   vuelve a mostrar en el chat.
4. Sin prólogos ni transiciones entre pasos.

## Lo que esta skill NO hace

- **No reporta cifras de resultados.** Describe el análisis (qué, con qué
  software y versión, con qué criterios); las cifras las reporta la Fase 5. La
  única cifra que calcula es la Tabla 1 (ver `references/analisis.md`).
- **No construye ni valida el instrumento.** Eso es `instrumento-investigacion`.
- **No es para tesis.** Si aparecen "capítulo III", "asesor" o "jurado",
  derivar a `metodologia`.

---

# Flujo

## Paso 0 — Bienvenida

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Ruta del Artículo Empírico · Fase 4

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

¡Bienvenido a las Skills de Acosta!

Estás en la **Fase 4 — Métodos**. Aquí describimos exactamente qué hiciste, con qué y con quiénes.

Es la sección que un revisor lee para saber si tu estudio se puede repetir. Por eso te voy a pedir datos concretos: fechas reales, versión del software, cuántos casos quedaron después de depurar. Nada de esto lo invento; lo que no tengas, lo marcamos como pendiente.

Súbeme el Word de la fase anterior y tu base de datos.
```

## Paso 1 — Insumos

Lo primero, con el Word recibido:

```bash
python3 scripts/articulo_docx.py esquema ARTICULO_[clave]_v3.docx --acronimos
```

De ahí y de la Ficha y la Matriz salen el tipo de estudio, el diseño, el
término unificador y los acrónimos. **No se vuelven a preguntar.** Si falta la
Matriz, se piden los datos mínimos en una sola pregunta (`references/ruta.md`).

**Norma de la revista** (`REVISTA_[clave].json`, `references/perfil_revista.md`):
el título de la sección es el de `estructura`, tal cual («Método», «Métodos»,
«Materiales y métodos»), y se usa en el `#` del `.md`; las citas, en su
`estilo_cita`. Las tablas van en el texto aunque el perfil las pida al final, y
ninguna sección se reubica aquí (eso es la Fase 8 con `ajustar_docx.py`).

**Citas por clave.** Toda cita, también la metodológica (Hair, Henseler,
Bradford), se escribe con su clave del inventario (`[F012]`, `[F012:n]`,
`[AR51541814]`) y el motor la formatea con `--fuentes inventario.json`. Una
fuente que no está en el inventario entra por una de las tres vías de
`references/fuentes_y_citas.md` (en esta skill, la (c): `scripts/referencias.py
doi` con un DOI verificado); si no se puede, `[POR CONFIRMAR: referencia]`.

```
¿Qué traes?
- "El Word y mi base de datos (propia o secundaria)"
- "El Word, la base y las salidas de mi análisis"
- "Todavía no recojo los datos"
- "Ya tengo la metodología escrita, quiero mejorarla"
```

- **Sin datos todavía:** pasar antes por `instrumento-investigacion` →
  `recoleccion-datos` y volver. No se escribe Métodos en futuro.
- **Base secundaria** (encuesta nacional, base pública, registro
  administrativo): se piden además su **diccionario de variables** y su **ficha
  técnica** (diseño muestral, factor de expansión). Ver «Datos secundarios» en
  `references/analisis.md`.
- **Salidas del análisis**, si ya existen: se usan solo para el n final, los
  ítems retenidos, el software y los criterios. Las cifras se quedan para la
  Fase 5.

## Paso 2 — Confirmar lo que realmente pasó

El diseño viene de la Matriz. Aquí se pregunta **si el campo lo respetó**:

```
¿El trabajo de campo salió como estaba planeado?
- "Sí, tal como en la matriz"
- "Cambió el tipo de muestreo"
- "Conseguí menos casos de los previstos"
- "Cambiaron varias cosas, te cuento"
```

Cualquier cambio se describe **como fue**. Un muestreo por conveniencia se dice
tal cual: maquillarlo como aleatorio es un problema de integridad, y la
Discusión tendrá que reconocerlo como limitación.

**Con datos secundarios** no hubo campo propio: en lugar de esa pregunta se
confirma, en un solo mensaje, la ficha de la base (lo que falte queda
`[POR CONFIRMAR]`): fuente y propietario; año o periodo; enlace, **versión y
fecha de descarga**; unidad de análisis; módulos y variables usados; cómo se
construyeron los índices; filtros y **n final**; perdidos; factor de expansión
y variables de diseño (estrato, conglomerado); licencia de uso.

## Paso 3 — La Tabla 1, calculada desde la base

Solo en diseños con participantes (cuantitativo, experimental, instrumental,
rama cuantitativa del mixto). En cualitativo, como mucho una tabla de perfil con
códigos (E1, E2), nunca nombres.

**Libro de códigos, antes de calcular.** Si las variables vienen codificadas
(1, 2, 3…) y ni la Matriz ni el investigador dieron las etiquetas, se pide el
libro de códigos de **todas** las sociodemográficas en una sola pregunta
(código → etiqueta, y qué código es perdido). Si los tramos no cuadran con los
códigos (p. ej. 5 tramos de edad y 6 códigos), se pregunta. Sin etiqueta, la
fila queda `[POR CONFIRMAR: etiqueta del código]`; nunca se adivina.

**Vía A, servidor conectado (`trabajar_en_r`), preferente:** el investigador
sube la base por el enlace que da la herramienta y se calcula con
`frecuencias()` y `descriptivos()` según `references/analisis.md`; la tabla se
descarga como .csv. Decimales y nota, con las
mismas reglas de abajo.

**Vía local:** `scripts/tabla1.py` (requiere `pip install pandas openpyxl`).

```bash
python3 scripts/tabla1.py base.xlsx --listar --perdidos "99,NA,No sabe"
python3 scripts/tabla1.py base.xlsx --cat "Sexo, Ciclo, Facultad" --num Edad \
    --orden-natural --perdidos "99,NA,No sabe" --etiquetas "Sexo:1=Mujer,2=Hombre" --md tabla1.md
```

**Modo C (chat sin código):** el investigador pega las frecuencias de su
programa (SPSS, Excel, JASP) y se arman la tabla y la nota con estas reglas;
nada se calcula a ojo.

**Encuesta con factor de expansión** (datos secundarios con diseño complejo):
los porcentajes se calculan **con el diseño** (`survey::svydesign` +
`svymean`/`svytable`, en `references/analisis.md`), no como muestra simple. La
tabla da el n sin ponderar y el % ponderado, y la nota lo dice. `tabla1.py` no
pondera: en ese caso, vía A o el programa del investigador (Stata `svy`, SPSS
Muestras complejas). Modo C: pega la salida ponderada de su programa.

El listado se revisa **con el investigador**: qué columnas son las
sociodemográficas y qué códigos son "perdido". El script lee .xlsx y .csv en
UTF-8 o Latin-1, unifica categorías que solo difieren en espacios o
mayúsculas (`--unir-tildes` para tildes) e **imprime cada unificación para
confirmarla**, ordena ciclos y años con `--orden-natural` (romanos, números,
ordinales) y con `--md` deja el bloque `[TABLA 1]` + tabla + `[NOTA]` en la
sintaxis del motor, listo para pegar en `metodos.md`.

Reglas de la tabla:

- **Porcentaje sobre casos válidos**; la nota declara por variable los
  perdidos y el **n válido**, sin repartirlos. Si el análisis usará solo casos
  completos (p. ej. 280 de 301), se dice en Participantes.
- **Decimales fijos**: % con uno; M, DE, Mdn y RIC con dos. Si una continua es
  asimétrica (el script avisa), se usa `--mediana`.
- **Si el n de la base no coincide con el del análisis**, se muestran los dos y
  se pregunta cuál corresponde (suele ser la base depurada).
- **Nunca se completa una categoría que la base no tiene.**

## Paso 4 — Redactar los subtítulos

Estudios con datos propios de participantes, **cinco subtítulos** (detalle en
`references/subtitulos_metodo.md`):

```
1 · Enfoque, alcance y diseño
2 · Participantes                      (aquí se cita y se inserta la Tabla 1)
3 · Instrumentos
4 · Procedimiento y análisis de datos
5 · Aspectos éticos
```

La Tabla 1 es un elemento dentro de Participantes, no un subtítulo.
Cualitativo, instrumental, mixto y **datos secundarios** cambian la estructura:
ver `references/metodo_por_diseno.md`.

En **Procedimiento y análisis** se describe lo que se hizo o, si el análisis
corre en la Fase 5, **el plan ya decidido** con el investigador. El análisis se
nombra con el índice «Qué análisis según la pregunta» de
`references/analisis.md` (descriptivo, comparación, regresión lineal,
logística, ordinal o de conteo, multinivel, panel, series, mediación o
moderación, SEM, validación de escala): **no se asume SEM**. Si la Matriz no lo
fijó, se confirma en una pregunta con las dos o tres opciones que admite la
pregunta de investigación. Se declaran software y versión, criterios,
tratamiento de perdidos y, con encuestas complejas, el diseño (`survey`: pesos,
estratos, conglomerados). Lo que aún no se decidió queda
`[POR CONFIRMAR: ... (Fase 5)]` y la Fase 5 lo completa.

Con la vía A, las versiones se piden en la sesión (`R.version.string`,
`packageVersion("seminr")`). Si hay bootstrap, se declaran el **B total y la
semilla**; que se corriera por tandas no se menciona. Con el remuestreo manual
de `analisis.md` se describe como bootstrap percentil con B remuestreos en R
con seminr, no como SmartPLS; el IC del HTMT sale del mismo bootstrap. MGA y
MICOM, si se usan, se describen como pruebas de permutación (número de
permutaciones) programadas en R, según `analisis.md`.

Se muestran **de dos en dos** para que los revise sobre la marcha.

## Paso 5 — Si hay artículo modelo: estructura sí, frases no

Del modelo se toma el orden de los subtítulos y el nivel de detalle, **no sus
párrafos**. Cualquier secuencia de más de 12 palabras que coincida con el
modelo (o con artículos previos del propio autor) se reescribe.

## Paso 6 — Humanizar la sección

Según `references/anti_ia.md`: `humanizador-academico` sobre `metodos.md` (una
ronda, 1-2 bloques, una aprobación por bloque); si no está,
`humanizar_mi_documento` del servidor; si no hay ninguno, la lista de control.
Aquí abundan el 0, el 3 y el 6; la voz impersonal y los términos repetidos no
se tocan, y un párrafo con piso estructural se deja y se dice.

## Paso 7 — Unir al Word y verificar

La sección se escribe en `metodos.md` con la sintaxis de
`references/formato_docx.md`: `#` con el título del perfil, subtítulos `##`,
tablas con `[TABLA n]` citadas en el texto antes de aparecer y citas por clave.
**Sin sección de referencias en el `.md`**: el motor la regenera con todas las
fuentes citadas.

```bash
python3 scripts/articulo_docx.py agregar --base ARTICULO_[clave]_v3.docx --md metodos.md \
        --perfil REVISTA_[clave].json --fuentes inventario.json      # → _v4 + _v4_RESPALDO
python3 scripts/articulo_docx.py verificar ARTICULO_[clave]_v4.docx \
        --perfil REVISTA_[clave].json --fuentes inventario.json
```

`verificar` es **obligatorio**: si marca ✗ (tabla sin citar antes, bordes
verticales, numeración), se corrige el `.md`, se vuelve a agregar sobre la
misma base y se verifica otra vez. Los `!` se revisan a mano. La revisión
visual es opcional. **Modo C:** la sección sale en un bloque para pegar en
`PLANTILLA_ARTICULO.docx`, con la Tabla 1 en Markdown; las citas, con su clave,
más la lista y el bloque RIS de `fuentes_y_citas.md` (modo chat).

## Paso 8 — Cierre

- [ ] ¿Están los subtítulos que corresponden al diseño?
- [ ] ¿La Tabla 1 salió de la base, con % sobre válidos, perdidos y
      unificaciones en la nota?
- [ ] ¿El n coincide con el del análisis, o se explicó la diferencia?
- [ ] ¿Muestreo, ítems eliminados, fechas, software y versión son datos
      confirmados?
- [ ] ¿Las declaraciones éticas las confirmó una por una?
- [ ] ¿El análisis declarado es el que pide la pregunta (índice de
      `analisis.md`), con B total y semilla si hay bootstrap?
- [ ] Datos secundarios: ¿fuente, versión y fecha de descarga, variables,
      índices, filtros, n final, factor de expansión, diseño y licencia?
- [ ] ¿Toda cita por clave y ninguna clave ✗ en `verificar --fuentes`?
- [ ] ¿Sección humanizada y `verificar --perfil` sin ✗?

Al entregar, **listar los `[POR CONFIRMAR]`** (`verificar` los cuenta en
cuerpo, viñetas, tablas y referencias): en este apartado suelen ser justo los
que impiden enviar el artículo. Los marcados «(Fase 5)» se resuelven allí.

Handoff:

> ARTICULO_[clave]_v4.docx — hasta Métodos con la Tabla 1. Sigue la
> **Fase 5 — Resultados** (`articulo-fase5-resultados`): súbelo junto con las
> **salidas de tu análisis**. Si todavía no lo corriste, la Fase 5 te ofrece
> correrlo en el servidor o en `analisis-datos-rstudio`.

## Errores que esta skill previene

1. Inventar una fecha de recolección o una versión de software.
2. Declarar una aprobación de comité de ética que no existe.
3. Estimar la Tabla 1 o repartir los perdidos para que sume 100 %.
4. Unir categorías sin declararlo.
5. Describir como aleatorio un muestreo por conveniencia.
6. Inventar qué ítems se eliminaron.
7. Usar el n que conviene cuando base y análisis no coinciden.
8. Ponerle Tabla 1 sociodemográfica a un estudio cualitativo.
9. Adivinar la etiqueta de un código.
10. Escribir el método en futuro o calcar párrafos del artículo modelo.
11. Declarar SEM (o cualquier técnica) por costumbre y no por la pregunta.
12. Tratar una encuesta con diseño complejo como muestra simple, o una base
    secundaria como datos recogidos por el autor.

## Archivos de referencia

- `references/ruta.md` — Mapa de la ruta; manda sobre todo.
- `references/subtitulos_metodo.md` — Los cinco subtítulos estándar.
- `references/metodo_por_diseno.md` — Cualitativo, instrumental, mixto, datos
  secundarios y plan de análisis por tipo.
- `references/analisis.md` — Índice pregunta → análisis, datos secundarios
  (`survey`), Tabla 1 en el servidor, bootstrap por tandas.
- `scripts/tabla1.py` — Tabla 1 local (pandas + openpyxl; no pondera).
- `references/fuentes_y_citas.md` · `scripts/referencias.py` — Citas por clave
  y alta de fuentes por DOI verificado.
- `references/perfil_revista.md` — La norma de la revista.
- `references/formato_docx.md` · `references/documento_en_cadena.md` — El Word.
- `references/anti_ia.md` — Humanización de la sección.
- `references/estilos_cita.md` · `references/estilo_preguntas.md`
- `scripts/articulo_docx.py` · `scripts/medir_estilo.py`

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
fase y pega esta tarjeta junto con el último Word*. Un chat por fase ahorra
tokens y evita que el modelo se pierda.
