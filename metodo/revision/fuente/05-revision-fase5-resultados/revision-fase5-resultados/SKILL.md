---
name: revision-fase5-resultados
description: >-
  Fase 5 de la Ruta del Artículo de Revisión: redacta Resultados y los une al
  mismo Word. Dibuja el diagrama de flujo PRISMA desde los conteos y se niega si
  no cuadran; en bibliométricas reporta información principal, producción anual
  con crecimiento, fuentes y Bradford, autores y Lotka, países, documentos más
  citados y palabras clave, con cifras tomadas de bibliometrix en el servidor R
  de Acosta o de sus salidas; en sistemáticas presenta la tabla de estudios
  incluidos, su calidad y la síntesis por pregunta o eje temático. Numera tablas
  y figuras en continuidad. No discute. Escribe en español con la norma, el
  estilo de cita y el formato de la revista destino, humaniza la sección y
  entrega la versión de la revista y su respaldo neutro. ACTIVAR con resultados
  de mi revisión, diagrama PRISMA, análisis bibliométrico, bibliometrix, tabla
  de estudios incluidos, o cuando suban el Word de la Fase 4 o su corpus.
license: Proprietary
metadata:
  version: "2.2.0"
  fase: "5"
  ruta: "Ruta del Artículo de Revisión — Acosta | IA & Research"
---

# Fase 5 — Resultados

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

Convierte las salidas del análisis en la sección que las reporta. **Reporta, no
interpreta.** Esa frontera es la que más se cruza y la que más comentarios
recibe en revisión: un resultado que ya viene explicado deja a la Discusión sin
nada que decir y repite todo dos veces.

### La ruta completa

```
  Fase 0 · Tema y orientación
  Fase 1 · Matriz de estrategia
  Fase 2 · Introducción
  Fase 4 · Métodos (protocolo)
  Fase 5 · Resultados                  ← estás aquí
  Fase 6 · Discusión
  Fase 7 · Conclusiones y abstract
  Fase 8 · Adaptación a la revista y envío
  Fase 9 · Respuesta a revisores
```

Insumos, entregables y quién decide cada dato: `references/ruta.md` (manda
sobre este archivo si algo no coincide).

Si el estudio tiene datos propios (cuantitativo, cualitativo, mixto,
instrumental), sus Resultados están en la **Ruta del Artículo Empírico**.

## Regla de oro: las cifras se trasladan, no se producen

1. **Cada número sale de las salidas del análisis** (vías A, B o C de
   `references/analisis.md`). No se recalcula, no se "corrige" una cifra que no
   cuadra y no se completa una celda vacía.
2. **Formatear no es recalcular.** Se permite, y se declara en la nota: dos
   decimales (tres para *p*), quitar el cero inicial donde el estilo lo pida,
   escribir *p* < .001. Nada más.
3. **Redondear una sola vez**, desde el valor completo de la salida (tabla sin
   redondear, `SALIDAS_[clave].csv` o `.md`). **Prohibido redondear un valor ya
   redondeado**: .0648 → .06 (no .065 → .07); −.0948 → −.09 (no −.095 → −.10).
   Si la salida solo trae valores redondeados a tres decimales, se pide la
   completa o se reportan con esos tres decimales.
4. **Si falta un dato que la sección necesita** (un intervalo de confianza, un
   tamaño del efecto, el n por grupo), se pide o se obtiene de la misma vía del
   análisis. No se estima.
5. **No se interpreta.** Ni "lo que sugiere que", ni "esto se debe a", ni
   comparaciones con otros estudios. Eso es la Fase 6.
6. **Si las salidas contradicen lo declarado en Métodos** (otro n, otro
   software, otro número de ítems o de estudios), se señala y se pregunta antes
   de escribir.

## Regla del acompañamiento: el investigador es novato

- **Un paso por turno.**
- Toda pregunta técnica lleva `"No me queda claro, ponme ejemplos"` y, si sigue
  trabado, `"Prefiero que alguien me lo explique"`, que responde con el WhatsApp
  del equipo (+51 923 095 940) y deja el punto pendiente sin bloquear.
- **Aquí se traba más que en ninguna fase**, porque los términos son
  estadísticos. Antes de pedir un índice, explicar en una línea qué es: "El
  HTMT es el índice que muestra que dos constructos no están midiendo lo mismo;
  ¿lo tienes en tus salidas?".
- Redacción de las opciones en `references/estilo_preguntas.md`.

## Economía de la sesión

1. Cada archivo de `references/` se lee **solo en el paso que lo pide**.
2. Del Word se lee el `esquema` y la sección Métodos con `texto --seccion`.
   Nunca el artículo entero.
3. De las salidas se toma solo lo que va a la sección; no se vuelcan al chat.
4. Lo aprobado se escribe al `.md` y no se repite en el chat.

## Lo que esta skill NO hace

- **No interpreta ni contrasta con literatura.** Eso es la Fase 6.
- **No decide qué análisis correspondía.** Eso se decidió en la Fase 1 y se
  describió en la Fase 4.
- **No inventa ni estima cifras.** Si no hay salidas, ofrece obtenerlas por una
  vía de `references/analisis.md` (Paso 1).
- **No es para tesis.** Los resultados de tesis van por objetivos con
  interpretación; derivar a `analisis-datos-rstudio`.

---

# Flujo

## Paso 0 — Bienvenida

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Ruta del Artículo de Revisión · Fase 5

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

¡Bienvenido a las Skills de Acosta!

Estás en la **Fase 5 — Resultados**. Aquí reportamos lo que encontraste, sin explicarlo todavía.

Esa distinción parece un detalle y no lo es: si aquí escribimos por qué salió así, la Discusión se queda sin nada y el revisor ve todo repetido. Lo interpretamos en la fase siguiente.

Súbeme el Word de la Fase 4 y las salidas de tu análisis.
```

## Paso 1 — Insumos

```bash
python3 scripts/articulo_docx.py esquema ARTICULO_[clave]_v4.docx --acronimos
python3 scripts/articulo_docx.py texto ARTICULO_[clave]_v4.docx --seccion "Métodos"   # título del perfil
```

El `esquema` dice cuál es la **última tabla y figura** ya numeradas (Resultados
sigue desde ahí). Métodos dice qué se declaró: n, software, criterios, y qué
quedó `[POR CONFIRMAR: ... (Fase 5)]`. La Matriz da el orden de los objetivos.

**Norma de la revista** (`REVISTA_[clave].json`, `references/perfil_revista.md`):
el título es el de `estructura`, tal cual. Si la revista junta «Resultados y
discusión», aquí se escribe igual `# Resultados` y la Fase 6 `# Discusión`:
**las secciones solo se unen o reubican en la Fase 8** (`ajustar_docx.py
unir`); hasta entonces `verificar` solo avisa. Tablas en el texto aunque el
perfil las pida al final (las mueve la Fase 8). Citas, por clave del
inventario (`references/fuentes_y_citas.md`).

```
¿Qué traes?
- "El Word, los conteos del cribado y mi tabla de estudios incluidos"
- "El exporte de Scopus o WoS para el análisis bibliométrico"
- "Ya tengo las salidas de bibliometrix o VOSviewer"
- "Todavía no termino el cribado"
```

**Si todavía no hay salidas**, se ofrece en una sola pregunta:

- **Correrlo en el servidor** (si `trabajar_en_r` está conectado): el
  investigador sube su archivo por el enlace que da la herramienta y se sigue
  `references/analisis.md`. Las tablas se guardan **sin redondear**
  (`escribir_csv`) y, si el investigador no quiere descargar, la consola se
  transcribe con todos los decimales a `SALIDAS_[clave].md`: de ahí sale cada
  cifra.
  En bibliometría, con el código probado de `references/revision.md`
  (`bradford()` no se usa en el servidor). **Tras `mergeDbSources` se pierden
  las referencias citadas y los países**: producción, fuentes, autores, Lotka,
  Bradford y palabras clave con el corpus fusionado; co-citación con una sola
  base (Scopus); países y colaboración con Scopus o con
  `scripts/bibliometria.py`. Sin R (chat que solo ejecuta Python):
  `python3 scripts/bibliometria.py informe scopus.csv savedrecs.txt --out salida/`
  da tablas, `prisma_conteos.csv` y un `resumen_bibliometrico.md` listo.
- **Traer sus propias salidas** (SPSS, SmartPLS, JASP, R, Excel, VOSviewer).

El análisis es de la vía elegida; esta fase solo reporta lo que esa vía
devolvió. **Modo C (chat sin código):** solo la vía de las salidas propias,
pegadas en el chat.

**Pendientes de Métodos.** Lo que Métodos dejó para esta fase (B de bootstrap,
tratamiento de perdidos, umbrales, versiones) se toma de la misma vía y al
cierre se reemplaza en Métodos en los dos .docx con
`articulo_docx.py reemplazar ARTICULO_[clave]_v5.docx --cambios cambios.json`
(un objeto `{"buscar": "[POR CONFIRMAR: ...]", "por": "valor"}` por pendiente).

## Paso 2 — Inventario de lo que hay

Antes de escribir, una línea por cada tabla y figura disponible y **qué falta**
según el diseño:

| Elemento | ¿Existe? | Falta |
|---|---|---|

Si falta algo (el HTMT, el tamaño del efecto, el n por grupo, un conteo del
cribado), se pide antes de empezar. No se escribe el párrafo con un hueco.

## Paso 3 — Orden de presentación

Confirmarlo antes de redactar. **El orden no se altera para que quede mejor**:
el revisor lo lee esperando esa secuencia.

Orden de `references/revision.md`:

- **Sistemática o de alcance:** (1) Figura PRISMA; (2) tabla de
  características de los estudios incluidos; (3) calidad o riesgo de sesgo;
  (4) síntesis por pregunta o eje temático, citando cada estudio incluido.
- **Bibliométrica:** (1) flujo de selección y tabla de información principal;
  (2) producción anual y tasa de crecimiento; (3) fuentes y zonas de Bradford;
  (4) autores y ley de Lotka; (5) países y colaboración; (6) documentos más
  citados; (7) palabras clave, co-ocurrencia y mapa temático.

**El diagrama PRISMA** se dibuja con los conteos de Métodos (incluidos los
duplicados retirados a mano; ver `references/revision.md`):

```bash
python3 scripts/prisma_flujo.py --out figura1.png \
  --bases "Scopus=312;Web of Science=205" --duplicados 140 \
  --cribados 377 --excluidos-cribado 290 --buscados 87 --no-recuperados 4 \
  --evaluados 83 --excluidos-texto "Población distinta=21;Sin resultados=14" \
  --incluidos 48
```

En una **bibliométrica** (sin lectura a texto completo) se usa
`--bibliometrico`: identificados → duplicados → filtros por metadatos →
incluidos, sin cajas vacías de recuperación ni de elegibilidad
(`python3 scripts/prisma_flujo.py --help` da los argumentos; con
`bibliometria.py`, los conteos están en `prisma_conteos.csv`).

Si la aritmética no cuadra, el script se niega: se pregunta al investigador,
no se ajusta un número para que cuadre. El .png queda en la carpeta del `.md`.
**Modo C:** se entrega la tabla de conteos por caja y el investigador arma la
figura en la plantilla oficial de PRISMA 2020.

**Los estudios incluidos se citan por su clave** en la tabla de
características y en la síntesis (sistemática o de alcance); el motor arma la
lista. En una bibliométrica se citan solo los que el texto nombra (más
citados, nodos de co-citación). Un estudio que no está en el inventario entra
por las vías de `references/fuentes_y_citas.md` (el export del corpus o
`referencias.py doi`); nunca se escribe su referencia a mano.

## Paso 4 — Redactar

Reglas de reporte numérico, numeración y citación en
`references/tablas_y_figuras.md`. Lo esencial:

- **Cada tabla y figura se cita en el texto antes de aparecer.**
- **La numeración continúa la de Métodos** (lo dice el `esquema`): si la última
  tabla es la 1, aquí se empieza en la Tabla 2.
- **El texto no repite la tabla.** Destaca lo que responde a los objetivos y
  remite al resto.
- **Decimales consistentes**, redondeados una sola vez desde el valor completo;
  *p* nunca como `p = 0.000`.
- **Sin adjetivos valorativos**: nada de "excelente ajuste" ni "fuerte
  relación". El valor y su criterio.

Se muestran los bloques **de dos en dos** para que los revise sobre la marcha.

## Paso 6 — Humanizar la sección

Según `references/anti_ia.md`: `humanizador-academico` sobre la prosa de
`resultados.md` (una ronda, 1-2 bloques, una aprobación por bloque); si no
está, `humanizar_mi_documento` del servidor; si no hay ninguno, la lista de
control. **No se toca ninguna cifra, estadístico ni nombre o número de tabla y
figura**; tablas y notas quedan fuera. Aquí abundan el 0 ("En la Tabla X se
observa…"), el 1 y el 11. **No se meten conectores para subir el porcentaje de
oraciones «enlazadas»** ni se fuerza la cita en cada párrafo: en Resultados la
yuxtaposición de datos es lo normal; si el humanizador lo marca, se deja y se
dice.

## Paso 7 — Unir al Word y verificar

La sección se escribe en `resultados.md` con la sintaxis de
`references/formato_docx.md`: `#` con el título del perfil, tablas `[TABLA n]` con su
`[NOTA]`, figuras `[FIGURA n] Título | figura.png` (el .png en la misma
carpeta del `.md`), citas por clave y **sin sección de referencias** (la
genera el motor).

```bash
python3 scripts/articulo_docx.py agregar --base ARTICULO_[clave]_v4.docx --md resultados.md \
        --perfil REVISTA_[clave].json --fuentes inventario.json      # → _v5 + _v5_RESPALDO
python3 scripts/articulo_docx.py verificar ARTICULO_[clave]_v5.docx \
        --perfil REVISTA_[clave].json --fuentes inventario.json
```

`verificar` es **obligatorio**: numeración continua, cada tabla y figura citada
antes de aparecer, sin bordes verticales. Si marca ✗, se corrige el `.md`, se
vuelve a agregar sobre la `_v4` y se verifica otra vez. La revisión visual es
opcional. **Modo C:** la sección sale en un bloque para pegar en
`PLANTILLA_ARTICULO.docx`, tablas en Markdown; las figuras las exporta el
investigador desde su programa; las citas nuevas, con la lista y el RIS del
modo chat de `fuentes_y_citas.md`.

## Paso 8 — Cierre

- [ ] ¿Cada cifra coincide con las salidas, solo formateada?
- [ ] **Control de redondeo:** cada cifra del texto y las tablas se cotejó
      con su valor completo en `SALIDAS_[clave]`; ninguna salió de redondear
      otra ya redondeada (mirar sobre todo f², β pequeños, límites de IC, HTMT,
      diferencias de MGA y valores que terminan en 5).
- [ ] ¿No quedó ninguna interpretación colada?
- [ ] ¿Numeración continua desde Métodos y cada elemento citado antes?
- [ ] ¿El PRISMA cuadra con lo declarado en Métodos (`--bibliometrico` si no
      hubo texto completo)?
- [ ] Sistemática o de alcance: ¿cada estudio incluido está citado por su
      clave? Bibliométrica: ¿co-citación y países sin la fusión de
      `mergeDbSources`?
- [ ] ¿Pendientes de Métodos resueltos y listados con su valor?
- [ ] ¿Sección humanizada sin tocar cifras y `verificar --perfil` sin ✗?

Handoff:

> ARTICULO_[clave]_v5.docx — hasta Resultados. Sigue la **Fase 6 — Discusión**
> (`revision-fase6-discusion`): sube este mismo .docx.

Y un aviso: **los objetivos anunciados en la Introducción tienen que coincidir
con lo encontrado.** Ese cotejo se hace en la Fase 8; queda anotado.

## Errores que esta skill previene

1. Interpretar en Resultados y repetirlo todo en Discusión.
2. Recalcular, "corregir" o completar una cifra del análisis.
3. Adjetivar los índices.
4. Escribir `p = 0.000`.
5. Romper la numeración que venía de Métodos.
6. Insertar una tabla o figura que el texto nunca menciona.
7. Redondear dos veces (.0648 → .065 → .07).
8. Ajustar un conteo para que el PRISMA cuadre.
9. Enumerar estudio por estudio en vez de sintetizar.
10. Calcular co-citación o países sobre el corpus fusionado con
    `mergeDbSources`.

## Archivos de referencia

- `references/ruta.md` — Mapa de la ruta; manda sobre todo.
- `references/analisis.md` — Vías A, B y C; índice pregunta → análisis;
  bootstrap por tandas; redondear una sola vez.
- `references/revision.md` — Orden de reporte, bibliometrix (aviso sobre
  `mergeDbSources`) y PRISMA.
- `scripts/prisma_flujo.py` — Diagrama PRISMA 2020; `--bibliometrico` sin
  texto completo (requiere matplotlib).
- `scripts/bibliometria.py` — Indicadores en Python si no hay R.
- `references/fuentes_y_citas.md` · `scripts/referencias.py` — Citas por clave.
- `references/tablas_y_figuras.md` — Numeración, citación y reporte numérico.
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
