---
name: articulo-fase7-conclusiones-abstract
description: >-
  Fase 7 de la Ruta del Artículo Empírico: cierra el manuscrito con las
  Conclusiones, el título definitivo, el resumen en español, el abstract en
  inglés y las palabras clave, y lo une al mismo Word. Las conclusiones integran
  los hallazgos, dicen qué implican para el campo y exponen la novedad del
  estudio, sin repetir la Discusión ni incluir limitaciones. El resumen sigue
  IMRyD en un párrafo con el conteo de palabras contra el límite de la revista,
  y el abstract es su equivalente en inglés académico. Escribe en español con la
  norma, el estilo de cita y el formato de la revista destino, humaniza la
  sección y entrega la versión de la revista y su respaldo neutro. ACTIVAR con
  conclusiones de mi artículo, resumen y abstract, palabras clave, título final,
  o cuando suban el Word de la Fase 6.
license: Proprietary
metadata:
  version: "2.2.0"
  fase: "7"
  ruta: "Ruta del Artículo Empírico — Acosta | IA & Research"
---

# Fase 7 — Conclusiones y abstract

Cierra el manuscrito y escribe las dos partes que más se leen: el título y el
resumen. Un editor decide con ellas si sigue leyendo.

### La ruta completa

```
  Fase 0 · Tema y orientación
  Fase 1 · Matriz de estrategia
  Fase 2 · Introducción
  Fase 3 · Revisión de la literatura
  Fase 4 · Métodos
  Fase 5 · Resultados
  Fase 6 · Discusión
  Fase 7 · Conclusiones y abstract     ← estás aquí
  Fase 8 · Adaptación a la revista y envío
  Fase 9 · Respuesta a revisores
```

Insumos, entregables y quién decide cada dato: `references/ruta.md` (manda
sobre este archivo).

## Dónde estás trabajando (léelo primero)

Mira qué herramientas tienes y elige **un** modo; no lo mezcles:

| Modo | Dónde | Cómo se entrega |
|---|---|---|
| **A · Con herramientas** | Claude con skills, Cowork, Claude Code, API | Scripts de esta skill (`scripts/`), archivos .docx/.xlsx reales |
| **B · Chat con código** | ChatGPT con análisis de datos, Claude.ai sin skills | Pide al usuario que suba `articulo_docx.py` (viene en la carpeta *herramientas* del paquete) y úsalo igual que en A |
| **C · Chat sin código** | Grok, ChatGPT sin análisis, cualquier chat | Entrega cada sección en un bloque de texto listo para pegar en `PLANTILLA_ARTICULO.docx`, tablas en Markdown; nunca prometas un archivo que no puedes generar |

En cualquier modo: **un paso por turno**, y si el usuario pega una
**Tarjeta de continuidad**, léela y no vuelvas a preguntar lo que ya dice.

## Regla de oro

1. **Las conclusiones no repiten la Discusión.** Se lee la Discusión antes de
   escribir; una oración que ya está allí se reformula.
2. **Exponen la novedad**, no reformulan resultados. Si el aporte es modesto,
   se dice modesto.
3. **Sin limitaciones ni líneas futuras**: ya están en la Fase 6.
4. **El resumen se cuenta**, no se estima.
5. **Sin autores ni filiaciones.** El manuscrito sigue sin datos personales; la
   página de título con la autoría se arma en la Fase 8.
6. **Nada se inventa**: ninguna cifra del resumen que no esté en Resultados.

## Acompañamiento: el investigador es novato

- **Un paso por turno.** Opciones redactadas según `references/estilo_preguntas.md`.
- Toda pregunta técnica lleva `"No me queda claro, ponme ejemplos"` y, si sigue
  trabado, `"Prefiero que alguien me lo explique"`, que responde con el
  WhatsApp del equipo (+51 923 095 940) y deja el punto pendiente sin bloquear.

## Lo que esta skill NO hace

- No redacta limitaciones, estudios futuros ni recomendaciones por destinatario.
- No adapta el manuscrito a la revista ni pone autores (Fase 8).
- Artículos de revisión (sistemática, de alcance, bibliométrica): están en la
  Ruta del Artículo de Revisión.
- No es para tesis. Si aparecen "capítulo VI" o "tesista", se sugiere la skill
  de tesis `conclusiones-abstract` (externa y opcional; no viene en esta ruta).

---

# Flujo

## Paso 0 — Bienvenida

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Ruta del Artículo Empírico · Fase 7

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

¡Bienvenido a las Skills de Acosta!

Estás en la **Fase 7 — Conclusiones y abstract**. Con esto tu manuscrito queda completo.

Aquí escribimos las dos partes que más se leen: el título y el resumen. Un editor decide con esas dos si sigue leyendo el resto, así que les vamos a dedicar el tiempo que merecen.

Súbeme el Word de la fase anterior (ARTICULO_[clave]_v6.docx).
```

## Paso 1 — Leer lo justo

Con la `_v6.docx` (o un .docx de otra fuente, ver `references/ruta.md`):

```bash
python3 scripts/articulo_docx.py esquema ARTICULO_[clave]_v6.docx --acronimos
python3 scripts/articulo_docx.py texto ARTICULO_[clave]_v6.docx --seccion "Discusión"
python3 scripts/articulo_docx.py texto ARTICULO_[clave]_v6.docx --seccion "Resultados"
```

(`--seccion` con los títulos del perfil.) Del esquema salen el título
provisional, la estructura y los acrónimos. La Discusión se lee para no
repetirla; Resultados, para tomar el estadístico clave del resumen. Del
objetivo basta el último párrafo de la Introducción. Tipo de estudio, de la
Matriz.

**Norma de la revista** (`REVISTA_[clave].json`, `references/perfil_revista.md`),
sin volver a preguntar: `resumen` (estructurado o no, `max_palabras`, idiomas),
`palabras_clave`, `titulo_max_palabras`, `limite_palabras` y `limite_cuenta`,
y el título exacto de las Conclusiones en `estructura`. Si la estructura no
tiene Conclusiones, se pregunta en una línea si van como cierre de la
Discusión (`.md` sin `#`) o se omiten. Sin perfil, los valores neutros de
`perfil_revista.md`, marcados `[POR CONFIRMAR]`. **Revista bilingüe o en
inglés:** los rótulos en inglés (Abstract, Keywords) salen de `estructura_en`
del perfil; si está vacío, la traducción literal y se avisa. Secciones que la
revista une o reubica (p. ej. la Revisión de la literatura dentro de la
Introducción) no se tocan aquí: eso es la Fase 8 con `ajustar_docx.py`.

Si trae conclusiones o un resumen previos, se leen también, para no calcarlos.

## Paso 2 — Alcance

```
¿Qué necesitas de esta fase?
- "Conclusiones, título, resumen y abstract"
- "Solo las conclusiones"
- "Solo el resumen y el abstract"
- "Solo el título y las palabras clave"
```

## Paso 3 — Las conclusiones

Detalle en `references/conclusiones.md`. Prosa continua, sin cifras crudas, con
cuatro movimientos: recapitulación integrada, significado para el campo,
novedad concreta (solo la que aplique) y postura del investigador apoyada en lo
que los datos sostienen.

No se organizan hipótesis por hipótesis ni objetivo por objetivo: eso ya lo
hizo la Discusión.

## Paso 4 — El título definitivo

Reglas y ejemplos en `references/titulo_y_claves.md`. Con los resultados en la
mano, el título refleja lo realmente encontrado, nombra la población y no la
institución, y no usa siglas sin explicar, preguntas ni frases de efecto.
Ninguna versión pasa de `titulo_max_palabras`; se cuenta cada una.

Ofrecer tres versiones y dejar que elija.

## Paso 5 — El resumen en español

Detalle en `references/resumen_abstract.md`.

Según `resumen.tipo` del perfil: no estructurado, IMRyD en **un solo párrafo
continuo** (objetivo, método, resultado principal con el estadístico clave,
conclusión con su implicancia); estructurado, con los subtítulos de la guía.

Se cuenta con `python3 scripts/articulo_docx.py contar resumen.md` contra
`resumen.max_palabras` (modo C: el investigador lo cuenta en Word). No copia
frases de las conclusiones ni de la Discusión.

## Paso 6 — El abstract en inglés

Si `resumen.idiomas` lo incluye (casi siempre). Mismo contenido y estructura,
en pasado ("This study aimed to…", "The results showed…"), siglas locales
explicadas, longitud equivalente y dentro del mismo máximo. Aviso honesto: una
traducción pulida no sustituye la revisión de un hablante nativo.

## Paso 7 — Palabras clave

Las que fije `palabras_clave` del perfil (número y tesauro), en ambos idiomas. Que **no
repitan palabras del título**, con términos de tesauro si el campo lo tiene, y
keywords equivalentes conceptuales, no traducción literal. Detalle en
`references/titulo_y_claves.md`.

## Paso 8 — Humanizar

Según `references/anti_ia.md`, una sola ronda:

- **Conclusiones y resumen (español):** `humanizador-academico` (1 bloque, una
  aprobación); si no está, `humanizar_mi_documento` del servidor; si nada, la
  lista de control.
- **Abstract (inglés):** `humanizador-academico-ingles` en modo breve.

Abundan el 12 (cierres optimistas), el 7, el 10 ("no solo… sino también") y
el 1. No se toca ninguna cifra; tras humanizar, se recuenta el resumen.

## Paso 9 — Unir al documento

Dos archivos .md con la sintaxis de `references/formato_docx.md`:

- `conclusiones.md` → `#` con el título del perfil y su texto.
- `resumen.md` → `# Resumen` (o el rótulo de la revista), el texto, `[SIN SANGRIA] **Palabras clave:** a;
  b; c`, y luego `# Abstract` (o su rótulo de `estructura_en`), el párrafo y
  `[SIN SANGRIA] **Keywords:** ...`. (Si se cuenta este archivo, la línea de
  palabras clave suma: descontarla.)

Si las conclusiones citan algo, va por clave; ninguno de los dos `.md` lleva
sección de referencias. Los comandos se escriben **completos, sin guardar
`--perfil` en una variable** (en zsh, la shell de macOS, `$P` llega como un
solo argumento y falla):

```bash
python3 scripts/articulo_docx.py agregar --base ARTICULO_[clave]_v6.docx --md conclusiones.md \
        --out ARTICULO_[clave]_v7a.docx --perfil REVISTA_[clave].json --fuentes inventario.json
python3 scripts/articulo_docx.py agregar --base ARTICULO_[clave]_v7a.docx --md resumen.md \
        --posicion inicio --titulo "Título definitivo" --out ARTICULO_[clave]_v7.docx \
        --perfil REVISTA_[clave].json --fuentes inventario.json      # + _v7_RESPALDO
python3 scripts/articulo_docx.py verificar ARTICULO_[clave]_v7.docx \
        --perfil REVISTA_[clave].json --fuentes inventario.json
```

La `_v7a` (y su respaldo) es intermedia: se borra al final. Si `verificar`
marca ✗, se corrige y se vuelve a correr.

**Límite del manuscrito.** `verificar --perfil` cuenta según `limite_cuenta`
(con referencias, con tablas o todo el manuscrito) y, si el perfil trae
`limite_paginas`, estima las páginas. Sobre ese total se proyecta lo que
llegará a la Fase 8 (más la página de título y las declaraciones, unas 150 a
300 palabras). Si se pasa, se avisa con cuántas palabras sobran y qué
secciones son más largas; no se recorta sin aprobación.

**Fuentes citadas al gestor.** Con el manuscrito cerrado, se exportan solo las
fuentes citadas para la colección del investigador en Zotero o Mendeley:

```bash
python3 scripts/referencias.py exportar --inventario inventario.json --docx ARTICULO_[clave]_v7.docx \
        --ris CITADAS_[clave].ris --bib CITADAS_[clave].bib --dois DOIS_[clave].txt
```

Se importa `CITADAS_[clave].ris` (o `.bib`) en la colección `[clave]`; las
citas vivas, si las quiere, siguen `references/fuentes_y_citas.md`. La Fase 8
lo repite si el reenvío cambia las citas.

**Modo C:** título, resumen, abstract y conclusiones en bloques para pegar en
`PLANTILLA_ARTICULO.docx`, y el bloque RIS de las fuentes citadas (modo chat de
`fuentes_y_citas.md`). Resultado:

```
ARTICULO_[clave]_v7.docx
  Título definitivo · Resumen · Palabras clave · Abstract · Keywords
  Introducción · … · Discusión · Conclusiones · Referencias
```

## Paso 10 — Cierre

- [ ] ¿Conclusiones integradas, con la novedad concreta y sin repetir la Discusión?
- [ ] ¿Sin limitaciones ni líneas futuras?
- [ ] ¿El título refleja lo encontrado, nombra la población y cabe en el máximo?
- [ ] ¿Resumen con el formato del perfil y **contado** contra su máximo?
- [ ] ¿Total del manuscrito proyectado contra el límite, con aviso si se pasa?
- [ ] ¿Abstract en pasado, siglas explicadas?
- [ ] ¿Palabras clave sin repetir el título?
- [ ] ¿Humanizado (español y abstract) y `verificar --perfil --fuentes` sin ✗?
- [ ] ¿`CITADAS_[clave].ris`/`.bib` exportados para Zotero o Mendeley?

Entrega en una línea:

> ARTICULO_[clave]_v7.docx — manuscrito completo, con título definitivo,
> resumen y abstract. Para la **Fase 8 — Adaptación y envío** súbelo junto con
> la guía de autores de la revista, y ten a mano nombres completos, filiación,
> ORCID y correo de cada coautor: ahí se arma la página de título.

## Errores que esta skill previene

1. Conclusiones que son la Discusión con otras palabras, o una lista por hipótesis.
2. Inventarle novedad a un estudio que aporta poco.
3. Repetir las limitaciones en las conclusiones.
4. Un resumen que excede el límite porque nadie contó.
5. Un abstract traducido palabra por palabra.
6. Palabras clave que repiten el título.
7. Poner el resumen al final porque se escribió al final.
8. Meter autores en el manuscrito antes de saber si la revisión es doble ciego.

## Archivos de referencia

- `references/ruta.md` — Mapa de fases, insumos y entregables (manda).
- `references/conclusiones.md` — Los cuatro movimientos.
- `references/titulo_y_claves.md` — Título definitivo y palabras clave.
- `references/resumen_abstract.md` — Resumen, abstract y conteo.
- `references/perfil_revista.md` — La norma de la revista.
- `references/formato_docx.md` y `references/documento_en_cadena.md` — El Word.
- `references/anti_ia.md` — Humanización.
- `references/estilos_cita.md` — Estilos de cita.
- `references/fuentes_y_citas.md` · `scripts/referencias.py` — Citas por clave
  y exportación de las citadas al gestor.
- `references/estilo_preguntas.md` — Cómo se redactan las opciones.
- `scripts/articulo_docx.py` — Motor del Word. `scripts/medir_estilo.py` — Medición opcional.

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
