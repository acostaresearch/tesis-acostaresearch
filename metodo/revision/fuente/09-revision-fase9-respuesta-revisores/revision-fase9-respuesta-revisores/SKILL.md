---
name: revision-fase9-respuesta-revisores
description: >-
  Fase 9 de la Ruta del Artículo de Revisión: responde a los revisores. Ordena
  las observaciones del dictamen en una matriz, decide con el autor qué se
  acepta, se matiza o se refuta con argumento, aplica los cambios a la versión
  enviada con control de cambios real de Word firmado por el autor y validado,
  actualiza también el respaldo neutro, y redacta la carta de respuesta punto
  por punto en el idioma del manuscrito, humanizada. Si un revisor pide
  reanalizar, lo deriva al servidor R o a la herramienta de análisis. Si el
  dictamen es un rechazo, deja la matriz y el respaldo listos y deriva al
  reenvío de la Fase 8. Nada se inventa ni se cambia sin marcar. ACTIVAR con
  respuesta a revisores, me devolvieron el artículo con observaciones, major
  revision, minor revision, carta de respuesta, control de cambios, o cuando
  suban el dictamen de la revista.
license: Proprietary
metadata:
  version: "2.2.0"
  fase: "9"
  ruta: "Ruta del Artículo de Revisión — Acosta | IA & Research"
---

# Fase 9 — Respuesta a revisores

Atiende una ronda de revisión por pares en cualquier revista. Llega un correo
con observaciones y el autor no sabe si tiene que aceptarlas todas. **No tiene
que aceptarlas todas**: buena parte del trabajo es distinguir qué procede.

### La ruta completa

```
  Fase 0 · Tema y orientación
  Fase 1 · Matriz de estrategia
  Fase 2 · Introducción
  Fase 4 · Métodos
  Fase 5 · Resultados
  Fase 6 · Discusión
  Fase 7 · Conclusiones y abstract
  Fase 8 · Adaptación a la revista y envío
  Fase 9 · Respuesta a revisores       ← estás aquí
```

Mapa de fases y entregables: `references/ruta.md` (manda). **El control de
cambios se aplica sobre la `_v8` enviada** (la versión de la revista), tal como
se subió a la plataforma; si el autor no la guardó, se descarga de la
plataforma. El mismo cambio se lleva, ya aceptado, al `_v8_RESPALDO`.
**Tras un reenvío** la enviada es `_vN_[revista]` y la salida
`_v9_[revista]` (+ `_RESPALDO`): abajo, `_v8` y `_v9` valen con ese sufijo.

## Dónde estás trabajando (léelo primero)

Mira qué herramientas tienes y elige **un** modo; no lo mezcles:

| Modo | Dónde | Cómo se entrega |
|---|---|---|
| **A · Con herramientas** | Claude con skills, Cowork, Claude Code, API | Scripts de esta skill (`scripts/`), archivos .docx/.xlsx reales |
| **B · Chat con código** | ChatGPT con análisis de datos, Claude.ai sin skills | Pide al usuario que suba `articulo_docx.py` (viene en la carpeta *herramientas* del paquete) y úsalo igual que en A |
| **C · Chat sin código** | Grok, ChatGPT sin análisis, cualquier chat | Entrega cada sección en un bloque de texto listo para pegar en `PLANTILLA_ARTICULO.docx`, tablas en Markdown; nunca prometas un archivo que no puedes generar |

En cualquier modo: **un paso por turno**, y si el usuario pega una
**Tarjeta de continuidad**, léela y no vuelvas a preguntar lo que ya dice.

## Entregables

| Archivo | Qué es |
|---|---|
| `ARTICULO_[clave]_v9.docx` | La `_v8` enviada con control de cambios a nombre del autor |
| `ARTICULO_[clave]_v9_RESPALDO.docx` | El respaldo neutro con los mismos cambios ya aceptados (sin marcas) |
| `RESPUESTA_[clave].docx` | Carta de respuesta punto por punto |
| `MATRIZ_OBSERVACIONES_[clave].docx` | Una fila por observación, con decisión y dónde se atendió |

## Regla de oro (no negociable)

1. **No se eliminan citas ni se altera el orden de las referencias**, salvo que
   una observación lo pida.
2. **Evitar agregar citas.** Si hace falta una, se le pide al autor; si autoriza
   buscarla, se verifica que exista (autor, año, revista, DOI y el hallazgo
   atribuido) antes de insertarla.
3. **Todo cambio va con control de cambios**, y validado.
4. **Se atiende lo académicamente razonable.** Lo fuera de alcance, lo
   contradictorio o lo que los datos no permiten se declina con argumento, no
   se finge cumplir.
5. **Nada se inventa**: ni un análisis que no se corrió, ni una limitación
   falsa, ni una cifra.

## Acompañamiento: el autor está nervioso

- **Un paso por turno.** Opciones según `references/estilo_preguntas.md`.
- Toda pregunta técnica lleva como última opción `"No me queda claro, ponme
  ejemplos"` y, si sigue trabado, `"Prefiero que alguien me lo explique"`, que
  responde con el WhatsApp del equipo (+51 923 095 940) y deja el punto
  pendiente **sin bloquear**.
- **Decirle temprano que declinar una observación es normal** y se hace con
  argumento.

## Lo que esta skill NO hace

- **No responde por el autor**: la matriz se confirma con él antes de tocar el
  manuscrito.
- **No corre análisis nuevos por su cuenta.** Si un revisor pide un
  reanálisis, se obtiene por la vía de `references/analisis.md` (servidor
  `trabajar_en_r` si está conectado, la skill `analisis-datos-rstudio`, o las
  salidas que traiga el autor) y se vuelve con el resultado. En el servidor:
  los objetos de la sesión anterior pueden no estar (se rearman desde la base
  y el modelo de Métodos), el bootstrap va **por tandas** con la receta de
  `analisis.md` y la tabla se guarda **sin redondear**; se redondea una sola
  vez al escribir el cambio. Semilla y remuestreos, a Métodos.
- **No cambia el estilo de cita** salvo que el editor lo pida.
- **No prepara el reenvío a otra revista**: tras un rechazo, esta fase solo
  arma la matriz y pone al día el respaldo; el reenvío es la Fase 8 (Paso 9).
- **No sube la respuesta a la plataforma.** Si la revista es de la red
  CGScholar, sus formularios de respuesta difieren: se adapta el documento de
  respuesta a lo que pida la plataforma.
- Artículos con datos propios: están en la Ruta del Artículo Empírico.

---

# Flujo

## Paso 0 — Bienvenida

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Ruta del Artículo de Revisión · Fase 9

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

¡Bienvenido a las Skills de Acosta!

Estás en la **Fase 9 — Respuesta a revisores**. Llegaron las observaciones y vamos a atenderlas una por una.

Antes de empezar, algo que tranquiliza a mucha gente: **no tienes que aceptar todas.** Un revisor puede pedir algo fuera del alcance de tu estudio, contradecir a otro revisor, o exigir un análisis que tus datos no permiten. Eso se declina con argumento, y es perfectamente normal.

Súbeme tu manuscrito tal como lo enviaste (la v8), su _RESPALDO y las reseñas.
```

## Paso 1 — Insumos

```
¿Qué traes?
- "El manuscrito enviado y las reseñas"
- "Solo las reseñas, el manuscrito lo busco"
- "Las observaciones vienen como comentarios en el Word"
- "Me piden rehacer un análisis"
```

En el mismo bloque:

```
¿Cuál fue la decisión editorial?
- "Revisión menor"
- "Revisión mayor"
- "Rechazo con invitación a reenviar"
- "No me queda claro, te paso el correo"
```

Esa decisión cambia cuánto se puede reescribir sin generar otra ronda. Con
**rechazo** (o si el autor prefiere ir a otra revista): solo la matriz (Paso 2)
y los cambios útiles sobre el respaldo (`control_cambios.py respaldo`, Paso 3),
sin `_v9` marcada ni carta. Luego, Fase 8, Paso 9 (reenvío) con el
`_v9_RESPALDO`.

También hace falta, en una sola pregunta: **el nombre exacto del autor** con el
que se firmarán las marcas ("Nombre Apellido"), el **idioma de la respuesta**
(normalmente el del manuscrito) y, si no es evidente, el **estilo de cita**.

## Paso 2 — Inventariar las observaciones

Leer sin volcar el manuscrito entero:

```bash
python3 scripts/articulo_docx.py esquema enviado.docx --acronimos
python3 scripts/articulo_docx.py texto enviado.docx --seccion "Métodos"   # solo lo que se toca
python3 scripts/control_cambios.py comentarios --docx enviado.docx        # si el revisor comentó en el Word
```

Matriz de observaciones, una fila por observación:

| # | Revisor | Sección | Observación (resumen fiel) | Decisión | Cambio aplicado | Respuesta |
|---|---|---|---|---|---|---|

`Decisión`: *procede*, *procede parcialmente*, *no procede*.

- **Contradicciones entre revisores:** no se atiende a los dos; se elige una, se
  explica el criterio en ambas respuestas y se deja la decisión final al editor.
- **Observaciones repetidas** con otras palabras: un solo cambio, pero **se
  responden por separado**, porque cada revisor lee solo su bloque.

**Mostrar la matriz al autor y confirmar las que no proceden antes de tocar el
manuscrito.** Es el punto de control de toda la fase.

**Fuentes nuevas.** Si un revisor pide citar algo, la fuente entra por una de
las tres vías de `references/fuentes_y_citas.md`, nunca de memoria:
plataforma Acosta o su Zotero/Mendeley (RIS o BibTeX) con
`scripts/inventario_fuentes.py nuevas.ris --previo inventario.json --out
inventario.json`, o un DOI verificado con `scripts/referencias.py doi DOI
--inventario inventario.json`. Queda en el inventario con su clave, para que
un reenvío la conozca, y en la `_v9` se escribe a mano en el estilo vigente
(Paso 5), con su referencia en la lista.

## Paso 3 — Aplicar los cambios con control de cambios

Procedimiento en `references/control_cambios.md`. En corto: los cambios van en
un `cambios.json` (`buscar` = texto exacto del manuscrito, `reemplazar`,
`comentario` opcional; párrafos nuevos con `insertar_despues`) y:

```bash
C=scripts/control_cambios.py
python3 $C aplicar --docx ARTICULO_[clave]_v8.docx --cambios cambios.json \
        --autor "Nombre Apellido" --out ARTICULO_[clave]_v9.docx
python3 $C validar --docx ARTICULO_[clave]_v9.docx --original ARTICULO_[clave]_v8.docx \
        --cambios cambios.json --autor "Nombre Apellido"
```

Los `buscar` no encontrados se corrigen copiando el texto real y se aplican
sobre la `_v9`. **No se entrega hasta que `validar` diga VALIDADO.**

**Un valor que se repite** (una cifra de tabla, «.81», «-.10») nunca va como
`buscar` suelto, que cambia la primera aparición: se apunta a la celda con
`"tabla": 3, "fila": 2, "columna": 4` (desde 1, el encabezado es la fila 1; la
tabla es la tercera del documento) o con `"ocurrencia": n`, contada sobre el
texto tal como queda tras los cambios anteriores del mismo JSON. Detalle en
`references/control_cambios.md`.

**Cambios de estructura** («Resultados y discusión» en una sola sección, la
Revisión como subsección): el título se cambia o se elimina con un cambio
marcado normal (`buscar` = el título entero, con `"ocurrencia"` si esa
palabra aparece antes en el texto), y el nivel con `python3
scripts/ajustar_docx.py nivel --docx ARTICULO_[clave]_v9.docx --seccion
"Discusión" --nivel 2` después de `aplicar` y antes de `validar` (no cambia
texto, así que valida igual). El cambio de nivel no queda marcado: se dice en
el comentario del título y en la respuesta.

Con el JSON definitivo (el mismo, o la unión de los que se aplicaron), se pone
al día el respaldo:

```bash
python3 $C respaldo --docx ARTICULO_[clave]_v8_RESPALDO.docx --cambios cambios.json \
        --out ARTICULO_[clave]_v9_RESPALDO.docx      # debe decir RESPALDO: AL DÍA
```

Aplica el mismo JSON y acepta los cambios: el respaldo queda con el texto
revisado, en formato neutro y sin marcas. Si las tablas de la `_v8` se movieron
al final o se anonimizó texto, un `buscar` de esas zonas puede no estar en el
respaldo: se ajusta ese cambio y se repite solo él sobre el `_v9_RESPALDO`.

**Modo C (chat sin código):** en vez de `cambios.json`, una tabla
`Sección | Texto actual | Texto nuevo` para que el autor active **Revisar >
Control de cambios** en Word y pegue cada fila; luego copia los mismos cambios
en el respaldo con el control de cambios apagado. Una línea por herramienta
nueva: `"tabla"/"fila"/"columna"` u `"ocurrencia"` → la fila de la tabla dice
«Tabla 3, fila 2, columna 4» o «la 2.ª aparición»; `ajustar_docx.py nivel` →
cambiar en Word el estilo del título (Título 1 → Título 2) con el control de
cambios activo; `referencias.py doi` → el autor abre `https://doi.org/` + el
DOI y confirma autor, año, revista y título antes de citar.

**Criterio de extensión.** Se responde a lo que se pidió, con las palabras que
la observación amerita. Si una observación exige contenido sustancial, avisar
del impacto en el límite de palabras.

## Paso 4 — La carta de respuesta punto por punto

```
Respuesta a los revisores
Manuscrito: [título]        ID: [si lo hay]

[Agradecimiento breve al editor y a los revisores, una sola vez.]

## Revisor 1
**Observación 1.** [texto literal o resumen fiel]
**Respuesta.** [dos o tres líneas: qué se cambió y dónde, o por qué no procede]
```

- **Dos o tres líneas por observación**, concretas: qué se cambió y en qué
  sección o párrafo. "Se atendió la observación" no es una respuesta.
- Si ayuda, citar entre comillas la frase nueva con su sección, sin pegar
  párrafos enteros.
- **Todas se responden**: las que no proceden (con argumento, ni sumiso ni
  defensivo), las valorativas positivas y las ya resueltas, indicando dónde.
- En el idioma del manuscrito.

```bash
python3 scripts/articulo_docx.py nuevo --md respuesta.md --out RESPUESTA_[clave].docx --compacto  # --idioma en si va en inglés
python3 scripts/articulo_docx.py nuevo --md matriz.md --out MATRIZ_OBSERVACIONES_[clave].docx --compacto
```

Modo C: la carta y la matriz en un bloque cada una, para pegar en Word.

## Paso 5 — Estilo de cita

Se detecta el del manuscrito y **se conserva**. Detalle en
`references/estilos_cita.md`.

- **APA 7 y Chicago author-date**: alfabético; una referencia nueva entra en su
  lugar alfabético.
- **IEEE y Vancouver**: numeración por orden de aparición. Agregar o quitar una
  fuente **obliga a renumerar desde ese punto y corregir cada llamada**:
  confirmarlo con el autor, incluir cada llamada renumerada en `cambios.json` y
  revisar la lista completa después.
- Las citas que entran por `control_cambios.py` quedan escritas, sin clave:
  un reenvío posterior con `normalizar --fuentes` no las reconvierte. Se anotan
  en la Tarjeta («citas a mano: …») para convertirlas con `reemplazar`.

## Paso 6 — Humanizar la respuesta

**Obligatorio** sobre la carta de respuesta, en versión breve
(`references/anti_ia.md`): en español, `humanizador-academico`; en inglés,
`humanizador-academico-ingles` en modo breve. Sin la skill, la lista de control
de `anti_ia.md`. Los párrafos nuevos del manuscrito se revisan con la misma
lista antes de entrar en `cambios.json`.

El patrón que aparece sin falta es el **0, paralelismo de plantilla**: veinte
respuestas que empiezan igual ("We thank the reviewer for this valuable
comment", "Agradecemos la observación…"). Se agradece **una sola vez, al
inicio**, y cada respuesta entra directo: unas por el cambio, otras por la
sección, otras por el argumento. Vigilar también el **3** (promocional) y el
**12** (cierres optimistas), que aquí suenan a súplica.

## Paso 7 — Verificación antes de entregar

```bash
python3 $C aceptar --docx ARTICULO_[clave]_v9.docx --out limpio.docx      # cómo quedaría aceptando todo
python3 scripts/articulo_docx.py verificar limpio.docx --perfil REVISTA_[clave].json --fuentes inventario.json
```

`verificar` es para el manuscrito: sobre `RESPUESTA` y `MATRIZ` da falsos
avisos (tablas «sin citar»), así que en ellos no se corre.

Comprobar que las referencias siguen completas y en orden, que ninguna llamada
quedó huérfana y que la extensión no se disparó. Y contar: **observaciones en
la matriz frente a respuestas en la carta. Tienen que coincidir.** La revisión
visual (abrir en Word o LibreOffice) es opcional, solo si algo hace sospechar.

## Paso 8 — Checklist

- [ ] ¿Todas las observaciones de todos los revisores están en la matriz?
- [ ] ¿Cada una tiene respuesta, incluidas las que no procedieron?
- [ ] ¿`validar` dio VALIDADO, con el nombre del autor?
- [ ] ¿`respaldo` dijo AL DÍA (el `_v9_RESPALDO` tiene el mismo texto)?
- [ ] ¿Se conservaron las citas y el orden de las referencias?
- [ ] ¿Las citas agregadas están verificadas y, en estilo numérico, renumeradas?
- [ ] ¿Las contradicciones entre revisores se resolvieron explícitamente?
- [ ] ¿La extensión añadida es proporcional a lo pedido?
- [ ] ¿Respuesta en el idioma del manuscrito, sin fórmulas repetidas?
- [ ] ¿Se listaron al autor los `[POR CONFIRMAR]`?

Entrega: los cuatro archivos y un resumen de pocas líneas (cuántas observaciones
se atendieron, cuáles se declinaron y con qué argumento). Recordarle que revise
las respuestas con sus coautores, sobre todo las que declinan. **Segunda
ronda:** se parte de la versión que se reenvió (con los cambios aceptados, si
así la subió) y del `_v9_RESPALDO`, y se repite el flujo; las marcas nuevas
conviven con las de la ronda anterior.

## Errores que esta skill previene

1. Aceptar todas las observaciones, incluidas las que desfiguran el estudio.
2. Fingir que se atendieron dos observaciones contradictorias.
3. Responder "se atendió la observación" sin decir qué ni dónde.
4. Dejar sin respuesta las que no procedieron.
5. Cambiar texto sin marcarlo, o firmar las marcas con otro nombre.
6. Un respaldo desactualizado: reenviar a otra revista sin los cambios ya hechos.
7. Inventar un análisis o una limitación para contentar a un revisor.
8. Agregar una cita sin verificar que existe, o romper la numeración.
9. Veinte respuestas que empiezan con la misma fórmula.

## Archivos de referencia

- `references/ruta.md` — Mapa de fases (manda).
- `references/control_cambios.md` — Control de cambios con `control_cambios.py`.
- `references/estilos_cita.md` — APA 7, Chicago, IEEE y Vancouver.
- `references/analisis.md` — Dónde se corre un análisis nuevo.
- `references/anti_ia.md` — Humanización.
- `references/perfil_revista.md` — El perfil de la revista y el respaldo.
- `references/formato_docx.md` — El motor del Word.
- `references/estilo_preguntas.md` — Cómo se redactan las opciones.
- `references/fuentes_y_citas.md` — Las tres vías para una fuente nueva.
- `scripts/control_cambios.py` — Aplicar (también por celda u ocurrencia),
  validar, aceptar, poner al día el respaldo, leer comentarios.
- `scripts/ajustar_docx.py` — Cambiar el nivel de una sección (el mismo de la
  Fase 8).
- `scripts/referencias.py`, `scripts/inventario_fuentes.py` — Alta de una
  fuente nueva (DOI verificado, fichas de la plataforma o export del gestor).
- `scripts/articulo_docx.py` — Leer el manuscrito y armar respuesta y matriz.

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
