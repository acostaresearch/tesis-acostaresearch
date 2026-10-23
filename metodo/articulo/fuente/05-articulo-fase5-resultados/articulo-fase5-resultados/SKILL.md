---
name: articulo-fase5-resultados
description: >-
  Fase 5 de la Ruta del Artículo Empírico: redacta Resultados y los une al mismo
  Word. Toma las cifras del análisis hecho en el servidor R de Acosta, en la
  skill analisis-datos-rstudio o en las salidas propias del investigador (SPSS,
  R, JASP, SmartPLS, Stata) y las traslada sin recalcularlas. Ordena según el
  diseño: modelo de medida y estructural en SEM, descriptivos y contraste en
  correlacional, coeficientes en regresión, conteo o multinivel, equivalencia y
  efecto en experimental, categorías en cualitativo, estructura factorial en
  instrumental. Numera tablas y figuras en continuidad. No interpreta ni
  discute: eso es la Fase 6. Escribe en español con la norma, el estilo de cita
  y el formato de la revista destino, humaniza la sección y entrega la versión
  de la revista y su respaldo neutro. ACTIVAR con resultados de mi artículo,
  reportar mis tablas, redactar mis salidas de SPSS o R, sección de resultados
  del paper, o cuando suban su documento de análisis o el Word de la Fase 4.
license: Proprietary
metadata:
  version: "2.2.0"
  fase: "5"
  ruta: "Ruta del Artículo Empírico — Acosta | IA & Research"
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
  Fase 3 · Revisión de la literatura
  Fase 4 · Métodos
  Fase 5 · Resultados                  ← estás aquí
  Fase 6 · Discusión
  Fase 7 · Conclusiones y abstract
  Fase 8 · Adaptación a la revista y envío
  Fase 9 · Respuesta a revisores
```

Insumos, entregables y quién decide cada dato: `references/ruta.md` (manda
sobre este archivo si algo no coincide).

Si el estudio es una revisión sistemática, de alcance o bibliométrica, sus
Resultados están en la **Ruta del Artículo de Revisión**.

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
7. **Las hipótesis rechazadas se reportan igual que las aceptadas**, con el
   mismo detalle y sin adjetivos.

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
   Ruta del Artículo Empírico · Fase 5

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
- "El Word y las salidas de mi análisis"
- "Tengo tablas sueltas en Excel y figuras"
- "Usé analisis-datos-rstudio"
- "Todavía no analizo mis datos"
```

**Si todavía no hay salidas**, se ofrece en una sola pregunta:

- **Correrlo en el servidor** (si `trabajar_en_r` está conectado): el
  investigador sube su archivo por el enlace que da la herramienta y se sigue
  `references/analisis.md`. Las tablas se guardan **sin redondear**
  (`escribir_csv`) y, si el investigador no quiere descargar, la consola se
  transcribe con todos los decimales a `SALIDAS_[clave].md`: de ahí sale cada
  cifra.
  El análisis lo dicta la pregunta (índice de `analisis.md`), no la costumbre.
  Toda tabla sale del **modelo final** (tras eliminar ítems), nunca del
  inicial. Bootstrap: **por tandas** de 500 a 1000 remuestreos por llamada
  (`boot_tanda` acumula y `resumen_boot` resume; un B de 5000 son 5 a 10
  llamadas), con la semilla registrada. IC del HTMT, efecto indirecto, MGA y
  MICOM: con las recetas de `analisis.md`, no improvisadas.
- **Derivar a `analisis-datos-rstudio`** y volver con sus tablas (de ella se
  toman solo las salidas, no su redacción por objetivos).
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

El orden lo da **el tipo de análisis declarado en Métodos**, no se asume SEM.
Qué cifras van en cada uno (APA 7) y en qué orden: `references/resultados_por_diseno.md`.

| Análisis | Orden |
|---|---|
| Descriptivo | Un bloque por objetivo (ponderado si hay factor de expansión) |
| Correlación / comparación de grupos | Descriptivos → supuestos → prueba → tamaño del efecto |
| Regresión (lineal, logística, ordinal, conteo) | Descriptivos y correlaciones → diagnóstico → modelo(s) → ajuste |
| Multinivel | Modelo nulo e ICC → modelos con predictores → comparación |
| Panel / series de tiempo | Descriptivos por periodo → prueba de especificación → modelo → diagnóstico |
| Mediación / moderación | Modelo → efectos directo, indirecto (IC) o interacción → efectos condicionales |
| SEM (PLS o CB) | Modelo de medida → estructural → mediación, moderación o MGA |
| Experimental | Equivalencia inicial → comparación → tamaño del efecto |
| Instrumental | Estructura factorial → ajuste → fiabilidad → validez → invarianza |
| Cualitativo | Un bloque por categoría, con citas textuales |
| Mixto | Rama cuantitativa → rama cualitativa → integración |

**Cualitativo:** cada categoría con sus subcategorías y citas textuales
identificadas con código (E1, E2). Si la codificación se hizo en el servidor
(`analisis-cualitativo`) o en Atlas.ti, **las citas y las frecuencias de
códigos se copian de esas salidas** tal cual; no se reescriben ni se cuentan a
mano.

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

## Paso 5 — Decisión de cada hipótesis

Solo en diseños con hipótesis. Una tabla de cierre y una frase por hipótesis:

| Hipótesis | Trayectoria | Estadístico | p | Decisión |
|---|---|---|---|---|

"Se acepta", "se rechaza", "se acepta parcialmente", **sin explicar por qué**.

Comprobación que evita el error más caro del artículo: **las hipótesis
reportadas son exactamente las enunciadas en la Fase 1 (Matriz) y sustentadas
en la Fase 3**, con la misma numeración y dirección. Si alguna cambió por el
camino, se señala y se pregunta.

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
- [ ] ¿Todas las tablas salen del modelo final, no del inicial?
- [ ] ¿No quedó ninguna interpretación colada?
- [ ] ¿Numeración continua desde Métodos y cada elemento citado antes?
- [ ] ¿Las hipótesis rechazadas tienen el mismo detalle que las aceptadas, y
      son las mismas de la Matriz?
- [ ] ¿En cualitativo, las citas son textuales y con código, no con nombre?
- [ ] ¿Pendientes de Métodos resueltos y listados con su valor?
- [ ] ¿Sección humanizada sin tocar cifras y `verificar --perfil` sin ✗?

Handoff:

> ARTICULO_[clave]_v5.docx — hasta Resultados. Sigue la **Fase 6 — Discusión**
> (`articulo-fase6-discusion`): sube este mismo .docx.

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
8. Reportar solo las hipótesis que se confirmaron.
9. Pulir o combinar citas textuales de participantes.
10. Ordenar como SEM un análisis que no lo es.

## Archivos de referencia

- `references/ruta.md` — Mapa de la ruta; manda sobre todo.
- `references/analisis.md` — Vías A, B y C; índice pregunta → análisis;
  bootstrap por tandas; redondear una sola vez.
- `references/resultados_por_diseno.md` — Orden y cifras por tipo de análisis.
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
