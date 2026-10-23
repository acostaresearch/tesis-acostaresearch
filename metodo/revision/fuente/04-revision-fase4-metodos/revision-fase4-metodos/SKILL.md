---
name: revision-fase4-metodos
description: >-
  Fase 4 de la Ruta del Artículo de Revisión: redacta Métodos como protocolo
  reproducible y los une al Word de la Introducción (no hay Fase 3). Escribe
  diseño y registro, criterios de elegibilidad, fuentes con fecha y ecuación
  literal de cada base, selección con depuración de duplicados, cribado y
  acuerdo entre revisores, extracción, evaluación de calidad o riesgo de sesgo,
  y síntesis o análisis bibliométrico con software y versión. Nunca inventa
  fechas, conteos, kappas ni códigos de registro: lo que no conste queda
  pendiente. Escribe en español con la norma, el estilo de cita y el formato de
  la revista destino, humaniza la sección y entrega la versión de la revista y
  su respaldo neutro. ACTIVAR con metodología de mi revisión, protocolo PRISMA,
  cómo describo mi búsqueda, criterios de inclusión y exclusión, o cuando suban
  el Word de la Fase 2.
license: Proprietary
metadata:
  version: "2.2.0"
  fase: "4"
  ruta: "Ruta del Artículo de Revisión — Acosta | IA & Research"
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
  Fase 4 · Métodos (protocolo)         ← estás aquí
  Fase 5 · Resultados
  Fase 6 · Discusión
  Fase 7 · Conclusiones y abstract
  Fase 8 · Adaptación a la revista y envío
  Fase 9 · Respuesta a revisores
```
En una revisión no hay Fase 3: los estudios revisados son los Resultados.

Insumos, entregables y quién decide cada dato: `references/ruta.md` (manda
sobre este archivo si algo no coincide).

Si el estudio tiene datos propios (cuantitativo, cualitativo, mixto,
instrumental), su Métodos está en la **Ruta del Artículo Empírico**.

## Regla de oro: veracidad absoluta

1. **Nada se declara sin confirmación**: bases, fecha exacta de cada búsqueda,
   ecuación literal, número de revisores, kappa, herramienta de calidad,
   software y versión. Lo que no conste queda `[POR CONFIRMAR: ...]`.
2. **Un código de registro (PROSPERO, OSF, INPLASY) nunca se inventa.** Si no
   se registró, se dice.
3. **Si una sola persona hizo el cribado, se dice.**
4. **Los conteos del cribado salen del registro del investigador**, no se
   reconstruyen. Si no cuadran entre sí, se pregunta.
5. **Métodos va en pasado.** Si la búsqueda no se hizo todavía, no se escribe.

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

- **No reporta cifras de resultados** ni dibuja el diagrama PRISMA: describe el
  protocolo; el flujo y los indicadores los reporta la Fase 5.
- **No hace el cribado.** Lo hace el investigador, idealmente con dos
  revisores.
- **No es para tesis.** Si aparecen "capítulo III", "asesor" o "jurado",
  derivar a `metodologia`.

---

# Flujo

## Paso 0 — Bienvenida

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Ruta del Artículo de Revisión · Fase 4

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

¡Bienvenido a las Skills de Acosta!

Estás en la **Fase 4 — Métodos**. Aquí describimos tu protocolo: dónde buscaste, con qué ecuación, qué criterios aplicaste y cómo seleccionaste los estudios.

Es la sección que un revisor usa para saber si tu revisión se puede repetir. Por eso te voy a pedir datos concretos: fechas exactas de búsqueda, ecuaciones tal como las corriste, cuántos revisores cribaron. Nada de esto lo invento; lo que no tengas, lo marcamos como pendiente.

Súbeme el Word de la Fase 2 y el registro de tu búsqueda y cribado.
```

## Paso 1 — Insumos

Lo primero, con el Word recibido (en revisión viene de la Fase 2):

```bash
python3 scripts/articulo_docx.py esquema ARTICULO_[clave]_v2.docx --acronimos
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
- "El Word de la Fase 2 y el registro de búsqueda y cribado"
- "Solo las ecuaciones y los exportes de las bases"
- "Todavía no hago la búsqueda"
- "Ya tengo la metodología escrita, quiero mejorarla"
```

- **Sin búsqueda todavía:** la ecuación del corpus es de la Fase 1
  (`revision-fase1-matriz-de-estrategia`, queda en la Matriz); el investigador
  la corre, criba y vuelve con el registro. Aquí se reporta **literal**, no se
  rehace (la búsqueda de la Fase 2 es otra: solo sirvió para la Introducción).
- **Sin registro del cribado:** decírselo claro; sin esos conteos la revisión
  no se puede reportar y habrá que reconstruir el proceso con las bases.

## Paso 2 — Confirmar lo que realmente pasó

El tipo de revisión y la pregunta (PICO, PEO o PCC) vienen de la Matriz. Aquí
se pregunta **si la búsqueda y el cribado siguieron el plan**:

```
¿La búsqueda salió como estaba planeada?
- "Sí, con las bases y criterios de la matriz"
- "Cambié o añadí bases"
- "Ajusté los criterios durante el cribado"
- "Cambiaron varias cosas, te cuento"
```

Un criterio ajustado después de ver los resultados se declara como tal: es
una desviación del protocolo y los revisores la buscan.

## Paso 3 — Conteos del registro

Se confirman con el registro los conteos de cada caja (identificados por base,
duplicados, cribados, excluidos, incluidos) y que cuadren entre sí. Si se
depuró con bibliometrix, `mergeDbSources` no quita los duplicados internos de
una base: revisarlos según `references/revision.md` y declarar cuántos se
retiraron a mano. Los umbrales del análisis que todavía no se fijaron quedan
`[POR CONFIRMAR: ... (Fase 5)]`. En una bibliométrica sin lectura a texto
completo, la selección se describe como filtros por metadatos (año, tipo de
documento, idioma), que es lo que dibujará `prisma_flujo.py --bibliometrico`
en la Fase 5; no se declaran cajas de texto completo que no existieron.

## Paso 4 — Redactar el protocolo

Se siguen los **siete subtítulos** de `references/revision.md`, en ese orden:

```
1 · Diseño y registro
2 · Criterios de elegibilidad
3 · Fuentes y búsqueda
4 · Selección
5 · Extracción de datos
6 · Evaluación de calidad o riesgo de sesgo
7 · Síntesis y análisis
```

- No hay Tabla 1 sociodemográfica. La primera tabla del artículo suele ser la
  de criterios de elegibilidad (Tabla 1) y la de ecuaciones por base
  (Tabla 2), si no van a material suplementario.
- Se piden, si no están en la Matriz: bases, **fecha exacta** de cada
  búsqueda, campo buscado, herramienta de duplicados, número de revisores, cómo se resolvieron
  desacuerdos, kappa si se calculó, herramienta de calidad, código de registro.
- En las de alcance y bibliométricas el subtítulo 6 suele omitirse, y se dice.
- En bibliométricas, el subtítulo 7 declara software y versión (bibliometrix,
  VOSviewer), unidad de análisis y umbrales. Con el servidor, la versión se
  pide en la sesión (`packageVersion("bibliometrix")`). Si se fusionaron
  Scopus y WoS con `mergeDbSources`, se declara que la co-citación se calculó
  con una sola base y los países con Scopus o con `scripts/bibliometria.py`
  (`references/revision.md`). Si todo se hizo con `bibliometria.py`, se
  declara con la fórmula de `revision.md`, sin atribuirlo a bibliometrix.
- La ecuación de cada base se copia de la Matriz, literal (si falta, se pide
  tal como se corrió).
- El diagrama PRISMA va en Resultados (Fase 5).

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
python3 scripts/articulo_docx.py agregar --base ARTICULO_[clave]_v2.docx --md metodos.md \
        --out ARTICULO_[clave]_v4.docx --perfil REVISTA_[clave].json --fuentes inventario.json
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

- [ ] ¿Están los siete subtítulos del protocolo (o se dijo por qué falta el 6)?
- [ ] ¿Fecha exacta, ecuación literal y bases de cada búsqueda, o sus
      pendientes?
- [ ] ¿Registro con su código real, o la declaración de que no se registró?
- [ ] ¿Número de revisores y resolución de desacuerdos confirmados?
- [ ] ¿Toda cita por clave y ninguna clave ✗ en `verificar --fuentes`?
- [ ] ¿Sección humanizada y `verificar --perfil` sin ✗?

Al entregar, **listar los `[POR CONFIRMAR]`** (`verificar` los cuenta en
cuerpo, viñetas, tablas y referencias): en este apartado suelen ser justo los
que impiden enviar el artículo. Los marcados «(Fase 5)» se resuelven allí.

Handoff:

> ARTICULO_[clave]_v4.docx — hasta Métodos (protocolo). Sigue la
> **Fase 5 — Resultados** (`revision-fase5-resultados`): súbelo junto con los
> **conteos del cribado** y, si es bibliométrica, los exportes del corpus o las
> salidas de bibliometrix.

## Errores que esta skill previene

1. Inventar una fecha de búsqueda o un código de registro.
2. Reconstruir una ecuación "parecida" en vez de la que se corrió.
3. Ocultar que el cribado lo hizo una sola persona.
4. Presentar criterios ajustados a posteriori como si fueran previos.
5. Ponerle Tabla 1 sociodemográfica a una revisión.
6. Rehacer la ecuación de búsqueda en vez de copiar la de la Matriz.
7. Escribir el método en futuro o calcar párrafos del artículo modelo.

## Archivos de referencia

- `references/ruta.md` — Mapa de la ruta; manda sobre todo.
- `references/revision.md` — Protocolo de las revisiones (siete subtítulos) y
  aviso sobre `mergeDbSources`.
- `references/analisis.md` — Reglas del servidor R (descargas, paquetes).
- `scripts/bibliometria.py` — Bibliometría en Python si no hay R.
- `scripts/prisma_flujo.py` — Lo usa la Fase 5; aquí no se dibuja el flujo.
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
