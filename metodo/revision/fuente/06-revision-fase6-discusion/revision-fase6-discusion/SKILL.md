---
name: revision-fase6-discusion
description: >-
  Fase 6 de la Ruta del Artículo de Revisión: redacta la Discusión y la une al
  mismo Word. La organiza por pregunta de revisión o por eje temático,
  interpreta lo que muestra la evidencia en conjunto, la contrasta con
  revisiones previas y marcos teóricos de la Introducción, identifica vacíos y
  tendencias, y cierra con implicaciones para la investigación y la práctica, y
  limitaciones (bases, idioma, periodo, sesgo de publicación, revisores). Sin
  cifras sueltas ni citas fantasma: solo estudios incluidos o ya citados, salvo
  autorización para buscar nuevos. Escribe en español con la norma, el estilo de
  cita y el formato de la revista destino, humaniza la sección y entrega la
  versión de la revista y su respaldo neutro. ACTIVAR con discusión de mi
  revisión, interpretar mis resultados bibliométricos, vacíos de investigación,
  o cuando suban el Word de la Fase 5.
license: Proprietary
metadata:
  version: "2.2.0"
  fase: "6"
  ruta: "Ruta del Artículo de Revisión — Acosta | IA & Research"
---

# Fase 6 — Discusión

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

Es donde el artículo dice **qué significan** los hallazgos. Resultados reportó;
aquí se interpreta y se contrasta con lo que ya sabía el campo.

Es también la sección que más distingue un artículo publicable de uno rechazado.
Una discusión que repite los resultados con otras palabras no aporta nada, y es
la observación más frecuente de los revisores.

### La ruta completa

```
  Fase 0 · Tema y orientación
  Fase 1 · Matriz de estrategia
  Fase 2 · Introducción
  Fase 4 · Métodos (protocolo)
  Fase 5 · Resultados
  Fase 6 · Discusión                   ← estás aquí
  Fase 7 · Conclusiones y abstract
  Fase 8 · Adaptación a la revista y envío
  Fase 9 · Respuesta a revisores
```

Insumos, entregables y quién decide cada dato: `references/ruta.md` (manda
sobre este archivo si algo no coincide).

Si el estudio tiene datos propios (cuantitativo, cualitativo, mixto,
instrumental), su Discusión está en la **Ruta del Artículo Empírico**.

## Regla de oro

1. **Sin valores estadísticos.** Ni *r*, ni *p*, ni β, ni intervalos: ya están
   en Resultados. Aquí se interpreta el significado.
2. **Cero citas fantasma.** Por defecto solo se citan autores **que ya están en
   el artículo**:
   los de la Introducción (revisiones previas, marcos teóricos) y los
   **estudios incluidos**, que son los Resultados de la revisión y sí se citan.
   Se citan **por clave del inventario** (`[F012]`, `[F012:n]`); el motor da
   el formato y la lista. Si el investigador autoriza buscar citas nuevas,
   cada una entra **solo por las tres vías de `references/fuentes_y_citas.md`**
   (plataforma Acosta, su gestor, o DOI verificado), se lee su resumen y se
   suma a la trazabilidad antes de usarse. Nunca se fabrica una referencia
   plausible ni se escribe una referencia a mano.
   Una fuente con resumen **recortado** (o sin resumen) solo respalda lo que
   dice su título: si el contraste depende de la dirección del efecto y el
   resumen no la informa, se dice así en el texto.
3. **Si algo es incierto, se dice.** Si no hay antecedentes comparables o la
   evidencia previa es mixta, se declara en vez de forzar la comparación.

## Regla del acompañamiento: el investigador es novato

- **Un paso por turno.**
- Toda pregunta técnica lleva `"No me queda claro, ponme ejemplos"` y, si sigue
  trabado, `"Prefiero que alguien me lo explique"`, que responde con el WhatsApp
  del equipo (+51 923 095 940) y deja el punto pendiente sin bloquear.
- Redacción de las opciones en `references/estilo_preguntas.md`.

## Economía de la sesión

1. Cada archivo de `references/` se lee **solo en el paso que lo pide**.
2. Del Word se leen el `esquema` y la sección Resultados con `texto --seccion`.
   Lo que dice cada fuente citable se toma de `TRAZABILIDAD_[clave].xlsx`
   (frase del abstract), no releyendo la Introducción entera.
3. Lo aprobado se escribe al `.md` y no se repite en el chat.

## Lo que esta skill NO hace

- **No reporta cifras.**
- **No escribe conclusiones ni abstract.** Eso es la Fase 7.
- **No inventa limitaciones genéricas** que no correspondan al estudio.
- **No es para tesis.** Si aparecen "capítulo V", "asesor" o "jurado", derivar a
  `discusion`.

---

# Flujo

## Paso 0 — Bienvenida

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Ruta del Artículo de Revisión · Fase 6

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

¡Bienvenido a las Skills de Acosta!

Estás en la **Fase 6 — Discusión**. Aquí explicamos qué significa lo que encontraste y lo comparamos con lo que ya decía la literatura.

Dos cosas antes de empezar. Aquí no van cifras: ya están en Resultados. Y las citas salen de lo que ya está en tu artículo, salvo que me autorices a buscar más y verificarlas una por una.

Súbeme el Word de la Fase 5 y tu matriz de trazabilidad.
```

## Paso 1 — Insumos

```bash
python3 scripts/articulo_docx.py esquema ARTICULO_[clave]_v5.docx --acronimos
python3 scripts/articulo_docx.py texto ARTICULO_[clave]_v5.docx --seccion "Resultados"   # título del perfil
```

**Norma de la revista** (`REVISTA_[clave].json`, `references/perfil_revista.md`):
título de la sección según `estructura` y citas en su `estilo_cita` (las pone
el motor desde las claves). Si la revista junta «Resultados y discusión», esta
fase escribe igual su `# Discusión`: **las secciones se unen o reubican solo en
la Fase 8** (`ajustar_docx.py unir`); antes, `verificar` solo avisa.

```
¿Qué traes?
- "El Word de la Fase 5 y la matriz de trazabilidad"
- "Solo el Word"
- "Ya tengo una discusión escrita, quiero mejorarla"
```

- **Sin Resultados no se avanza.**
- **Sin la matriz de trazabilidad**, las fuentes disponibles y sus claves se
  toman de `inventario.json` (o de la lista de referencias del Word), y lo que
  se les atribuya debe estar ya dicho en el artículo; si hace falta más, se
  pide la matriz o los abstracts.

## Paso 2 — Cómo se organiza

**Siempre se pregunta. No se asume.**

```
¿Cómo prefieres ordenar la discusión?
- "Por pregunta de revisión"
- "Por eje temático de la síntesis"
- "Como aparecen en mis Resultados"
- "No sé cuál me conviene, dime la diferencia"
```

Si pide la diferencia: por pregunta, cuando la revisión tiene varias preguntas
(PICO/PCC) explícitas; por eje temático, cuando la síntesis de Resultados ya se
organizó en temas. Nunca por hipótesis: una revisión no las tiene.

**Si la guía de autores de la revista exige una forma, manda esa.**

## Paso 3 — De dónde salen las citas

```
¿De dónde tomamos las citas para comparar?
- "Solo de lo que ya está en mi artículo"
- "Autorizo buscar más si faltan"
```

**La primera es la recomendada**: cero riesgo de citas inventadas y coherencia
con lo ya declarado.

Si autoriza la segunda, cada cita nueva entra por **una de las tres vías** de
`references/fuentes_y_citas.md`, nunca de memoria:

- **(a) Plataforma Acosta** (`buscar_fuentes`, `ampliar_desde_mis_fuentes`):
  la ficha trae su clave AR y su DOI; el DOI se da de alta con la vía (c) o la
  ficha se pasa al inventario con `inventario_fuentes.py` (Fases 2 y 3).
- **(b) Su gestor** (Zotero o Mendeley): exporta la referencia en RIS y se
  agrega igual (o por su DOI con la vía c).
- **(c) Búsqueda web**: solo con DOI verificado,
  `python3 scripts/referencias.py doi 10.xxxx/yyyy --inventario inventario.json`.

Luego, antes de usarla: se lee su resumen (que diga ese hallazgo, con esa
dirección); se añade a `TRAZABILIDAD_[clave].xlsx` con **su ID del
inventario**, la ubicación en la Discusión, la afirmación y la frase textual
(`references/trazabilidad.md`); se cita por esa clave; y se le avisa al
investigador cuáles son nuevas, por si quiere sumarlas también a la
Introducción o a la Revisión de la literatura.

## Paso 4 — Redactar el cuerpo

Detalle en `references/movimientos_discusion.md`.

**El cuerpo va en prosa continua, sin subtítulos.** Un párrafo (o dos) por
pregunta de revisión o eje temático,
con cuatro movimientos:

1. **Recordar el hallazgo sin cifras.**
2. **Contrastar con hasta cuatro o cinco citas, si existen**, y por cada una
   decir si el hallazgo propio es **refutación**, **complemento**,
   **actualización** o **novedad** respecto de ella. Si hay menos antecedentes
   comparables, se usan los que hay y se declara.
   En una revisión, el contraste es entre lo que mostraron los estudios
   incluidos y lo que decían las revisiones previas o los marcos teóricos de
   la Introducción.
3. **Explicar el significado** de lo confirmado o lo convergente, en la
   población y el contexto estudiados.
4. **Argumentar el porqué** de lo rechazado o lo divergente. Si la evidencia es
   parcial, se dice así.

Antes del primer párrafo, dos o tres oraciones que anuncien el orden. Al final
del cuerpo, un párrafo que integre la lectura general.

Se muestran **de dos en dos** para que los revise sobre la marcha.

## Paso 5 — Los dos subtítulos de cierre

Exactamente estos dos, en este orden:

### Aporte teórico y práctico

- **Teórico**: qué añade al conocimiento o al modelo usado.
- **Práctico**: qué pueden hacer distinto los actores relevantes. Concreto.

### Limitaciones y estudios futuros

- **Solo las limitaciones que efectivamente aplican** según Métodos y
  Resultados. Nada genérico de manual.
- Las típicas de una revisión, solo si aplican: bases consultadas, idioma,
  periodo, sesgo de publicación, un solo revisor en el cribado.
- **Las líneas futuras se desprenden de esas limitaciones** o de hallazgos no
  concluyentes del propio artículo.

Tono: **no disculparse.** Reconocer las limitaciones fortalece el artículo.

Si la `estructura` del perfil trae alguno de estos dos como sección propia (p.
ej. «Limitaciones»), va como `#` con ese título.

## Paso 6 — Humanizar la sección

Según `references/anti_ia.md`: `humanizador-academico` sobre `discusion.md`,
incluidos los dos subtítulos de cierre (una ronda, 1-2 bloques, una aprobación
por bloque); si no está, `humanizar_mi_documento` del servidor; si no hay
ninguno, la lista de control. Aquí abundan el 0 (contrastes con la misma
arquitectura: variar como indica `movimientos_discusion.md`), el 10 ("no es X
sino Y"), el 2 y el 11. No se añade cifra, nombre ni cita.

## Paso 7 — Unir al Word y verificar

La sección se escribe en `discusion.md` con la sintaxis de
`references/formato_docx.md`: `#` con el título del perfil, el cuerpo sin subtítulos,
`## Aporte teórico y práctico`, `## Limitaciones y estudios futuros`, citas
por clave y **sin sección de referencias**: el motor regenera la lista con
las fuentes nuevas incluidas.

```bash
python3 scripts/trazabilidad.py agregar --base TRAZABILIDAD_[clave].xlsx \
        --filas filas_f6.json --inventario inventario.json          # solo si hay citas nuevas
python3 scripts/articulo_docx.py agregar --base ARTICULO_[clave]_v5.docx --md discusion.md \
        --perfil REVISTA_[clave].json --fuentes inventario.json      # → _v6 + _v6_RESPALDO
python3 scripts/articulo_docx.py verificar ARTICULO_[clave]_v6.docx \
        --perfil REVISTA_[clave].json --fuentes inventario.json
```

`verificar` es **obligatorio**. Si marca ✗ (también una clave sin fuente), se
corrige el `.md` o el inventario, se vuelve a agregar sobre la `_v5` y se
verifica otra vez. Los avisos `!` de "posibles citas sin referencia" se
revisan uno por uno (una sigla institucional como «PCM, 2025» puede ser falso
positivo). La revisión visual es opcional.
**Modo C:** la sección sale en un bloque para pegar en
`PLANTILLA_ARTICULO.docx`; las citas nuevas, como filas para la trazabilidad y
con la lista y el RIS del modo chat de `fuentes_y_citas.md`.

## Paso 8 — Cierre

- [ ] ¿Cada hallazgo tiene hasta cuatro o cinco citas de contraste, o se
      declaró que hay menos?
- [ ] ¿Cada cita está clasificada (refutación, complemento, actualización,
      novedad)?
- [ ] ¿Quedó algún valor estadístico colado? Quitarlo.
- [ ] ¿Toda cita va por clave, y cada fuente nueva entró por una de las tres
      vías y está en la trazabilidad (`trazabilidad.py verificar` sin ✗)?
- [ ] ¿Cuerpo sin subtítulos y los dos finales exactos?
- [ ] ¿Limitaciones reales y líneas futuras que salen de ellas?
- [ ] ¿Quedó algún remate "no es X sino Y"?
- [ ] ¿Sección humanizada y `verificar --perfil` sin ✗?

Handoff:

> ARTICULO_[clave]_v6.docx — hasta la Discusión. Sigue la **Fase 7 —
> Conclusiones y abstract** (`revision-fase7-conclusiones-abstract`): sube
> este mismo .docx.

## Errores que esta skill previene

1. Repetir los resultados con otras palabras.
2. Dejar cifras estadísticas en la Discusión.
3. Inventar una cita que suena plausible, o usar una nueva sin registrarla en
   la trazabilidad.
4. Decir solo "coincide con" sin clasificar el tipo de contraste.
5. Despachar un hallazgo rechazado o divergente sin argumentar por qué.
6. Cinco párrafos de contraste con la misma arquitectura.
7. Cerrar con "no es X sino Y".
8. Poner limitaciones genéricas de manual.
9. Proponer líneas futuras desconectadas del propio hallazgo.
10. Organizar la discusión de una revisión por hipótesis.

## Archivos de referencia

- `references/ruta.md` — Mapa de la ruta; manda sobre todo.
- `references/movimientos_discusion.md` — Los cuatro movimientos y los cuatro
  tipos de contraste.
- `references/revision.md` — La Discusión en una revisión.
- `references/fuentes_y_citas.md` — Citas por clave y las tres vías para
  fuentes nuevas.
- `references/trazabilidad.md` · `scripts/trazabilidad.py` — Registro de las
  citas nuevas.
- `scripts/referencias.py` — Alta de fuentes por DOI verificado.
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
