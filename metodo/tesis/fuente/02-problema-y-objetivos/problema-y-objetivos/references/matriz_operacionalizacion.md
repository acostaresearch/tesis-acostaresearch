# Matriz de operacionalización de variables

## Qué es y por qué sale en esta skill

La matriz de operacionalización es el puente entre el concepto y el instrumento.
Toma cada variable del título, la baja a dimensiones, cada dimensión a
indicadores, y cada indicador a ítems concretos con su escala de medición.

**Decisión de método (setiembre 2026)**: esta matriz sale **completa en el
Capítulo I**, como Anexo 2, no en Metodología. Motivos:

- Es el insumo directo de la Skill de Instrumento. Tenerla desde el Capítulo I
  evita que el tesista llegue a construir el cuestionario sin saber qué mide.
- La matriz de consistencia (Anexo 1) ya declara variables y dimensiones. Partir
  ambas matrices entre dos capítulos producía versiones que no coincidían.
- El asesor revisa las dos matrices juntas. Entregarlas en el mismo documento es
  lo que él espera ver.

**Consecuencia que hay que respetar**: la Skill de Metodología **no vuelve a
generar** esta matriz. La cita, la retoma y, si el tesista cambió algo, la
actualiza. No la construye de cero.

## Dónde quedaron la teoría y las dimensiones

En esta versión del método, el Capítulo I **indica la teoría a emplear** por
cada variable (nombre, autor, año) y nada más. No se desarrolla, no se justifica
con extracción automática desde el corpus, y no lleva anexo propio. El desarrollo
de la teoría es trabajo de la Skill de Marco Teórico.

**Las dimensiones y los indicadores viven acá**, en la matriz de
operacionalización. Es su único lugar en el documento. La columna "Dimensiones"
de la matriz de consistencia se llena copiando de acá, no al revés.

## Estructura obligatoria: 7 columnas

```
| Variable | Definición   | Definición   | Dimensiones | Indicadores | Ítems | Escala de |
|          | conceptual   | operacional  |             |             |       | medición  |
```

Una tabla por variable, o una sola tabla con las dos variables separadas por
filas con `rowSpan`. Para A4 portrait conviene **una tabla por variable**: con
dos variables en una sola tabla las celdas quedan ilegibles.

### Columna 1 — Variable

El nombre exacto de la variable tal como aparece en el título y en la matriz de
consistencia. Sin sinónimos, sin variantes. Si en el título dice "competencia
digital docente", acá dice "competencia digital docente".

### Columna 2 — Definición conceptual

Qué es la variable según un autor real. **Regla dura**: lleva la clave `[AR…]` de
una fuente de su biblioteca. Si ninguna fuente define la variable, va
`[FALTA FUENTE]`, se le avisa en el chat y se busca una con `buscar_fuentes` (o se
añade la que él tenga). No se define con palabras propias sin respaldo.

Extensión: 2 a 4 líneas.

### Columna 3 — Definición operacional

Cómo se va a medir la variable en este estudio concreto. No es la definición del
diccionario: es el procedimiento. Formato típico:

```
Se medirá mediante [instrumento] compuesto por [N] ítems
distribuidos en [N] dimensiones, con respuesta en escala
[tipo] de [N] puntos, aplicado a [población].
```

Si el instrumento todavía no está decidido, en la parte del instrumento se escribe
«(se define en la Skill de Instrumento)», entre paréntesis y no entre corchetes,
y se completa el resto.

### Columna 4 — Dimensiones

Las dimensiones definitivas de la variable. Cada una con su nombre corto.

**Regla dura de coherencia**: el número de dimensiones de la Variable 1 determina
el número de objetivos específicos y de filas específicas de la matriz de
consistencia. Si acá hay 4 dimensiones, allá hay 4 objetivos específicos. Si no
coinciden, la skill lo declara y corrige antes de guardar el capítulo.

De dónde salen las dimensiones, en este orden de prioridad:

1. Del **instrumento validado** que el tesista va a usar o adaptar, si ya lo
   tiene. Es la fuente más segura, porque las dimensiones del instrumento son
   las que él va a poder medir de verdad.
2. De la **teoría indicada** en el Capítulo I, si el autor propone dimensiones.
3. De las **fuentes de su biblioteca**, cuando varias coinciden en las mismas dimensiones.

Si ninguna de las tres vías da dimensiones claras, la skill lo dice y le pide al
tesista que consulte con su asesor. No las inventa.

### Columna 5 — Indicadores

Qué se observa concretamente en cada dimensión. Dos a cuatro indicadores por
dimensión es lo usual. Se redactan como conductas o rasgos observables, no como
preguntas.

```
MAL:  "¿El docente usa herramientas digitales?"
BIEN: "Uso de herramientas digitales en la sesión de clase"
```

### Columna 6 — Ítems

**El rango de ítems que corresponde a cada dimensión**, expresado en números:
`1 a 5`, `6 a 11`, etc. No el texto de los ítems: eso es la Skill de Instrumento.

Si el tesista adapta un instrumento validado y ya conoce la distribución de
ítems, se pone la real. Si todavía no la tiene, se pone la distribución prevista
con la palabra «(previsto)» en la celda (`1 a 5 (previsto)`), y la tabla cierra con
`*Nota.* Los ítems marcados como previstos se confirman en la Skill de Instrumento.`
Sin corchetes. La Skill de Instrumento retira esa marca al volver a guardar el
Anexo 2.

### Columna 7 — Escala de medición

Dos datos en la misma celda:

```
Nivel de medición: [nominal / ordinal / intervalo / razón]
Escala de respuesta: [ej. Likert de 5 puntos,
   1 = Nunca a 5 = Siempre]
```

Para variables categóricas (sexo, condición laboral, grupo) el nivel es nominal
y no hay escala de respuesta tipo Likert: se listan las categorías.

## Filas de niveles y rangos (opcional pero recomendada)

Debajo de la tabla, muchas universidades piden los **niveles de la variable** con
sus rangos de puntaje:

```
Niveles y rangos de [Variable 1]

Bajo:    [rango de puntaje]
Medio:   [rango de puntaje]
Alto:    [rango de puntaje]
```

**Regla dura**: los rangos se calculan desde el número de ítems y los puntos de
la escala, no se inventan. Si el número de ítems todavía es previsto, los rangos
también van marcados como previstos. Si el tesista no sabe si su universidad los
pide, la skill se lo pregunta y no los incluye por defecto.

## Formato APA 7 de la tabla

Igual que la matriz de consistencia: la skill escribe el bloque y el servidor pone
el formato (tres líneas horizontales, sin bordes verticales, tipografía).

```
**Tabla 2**
*Matriz de operacionalización de la variable [nombre]*
| Variable | Definición conceptual | Definición operacional | Dimensiones | Indicadores | Ítems | Escala de medición |
|---|---|---|---|---|---|---|
| [nombre] | [definición] [AR…] | Se medirá mediante… | 1. … | … | 1 a 5 (previsto) | Ordinal; Likert de 5 puntos |
| | | | 2. … | … | 6 a 11 (previsto) | |
*Nota.* Los ítems marcados como previstos se confirman en la Skill de Instrumento.
```

- Número de tabla en negrita, en su propia línea. Como va en anexo, se numera
  según lo que pida la universidad; por defecto `Tabla 2` si la matriz de
  consistencia es `Tabla 1`.
- Sin líneas en blanco dentro del bloque.
- La `*Nota.*` sobre los ítems previstos va solo si hay alguno previsto; si hace
  falta aclarar de dónde salieron las dimensiones, se añade en la misma nota.
- Si la tabla sale ilegible en el Word, se acortan los textos de las celdas
  (definiciones de 2 a 4 líneas, indicadores breves); el formato no se toca.

## Checkpoint obligatorio

Antes de guardar el capítulo, la skill declara:

```
CHECKPOINT — MATRIZ DE OPERACIONALIZACIÓN

Variables operacionalizadas: [N] de [N]
Definiciones conceptuales con clave: [N] de [N]
   Sin fuente que las respalde: [N] → [lista]
Dimensiones de V1: [N]  ←→ Objetivos específicos: [N]
   Coherencia: [COINCIDEN / NO COINCIDEN]
Indicadores totales: [N]
Ítems: [reales del instrumento / previstos]
Escala declarada por variable: [SÍ / NO]
Niveles y rangos: [incluidos / no los pide la universidad /
   pendientes de confirmar]

Estado: [COMPLETADO / PENDIENTE]
```

Si "NO COINCIDEN", la skill **no avanza**: vuelve al Paso 9 y ajusta objetivos
específicos o dimensiones hasta que la cadena cierre.

## Errores frecuentes que la skill debe detectar

- **Dimensiones que son sinónimos de la variable.** Si la variable es "clima
  laboral" y una dimensión es "clima organizacional", no es una dimensión: es la
  misma cosa con otro nombre.
- **Indicadores redactados como preguntas.** Van como rasgos observables.
- **Definición operacional que repite la conceptual.** La operacional dice cómo
  se mide, no qué es.
- **Número de dimensiones que no coincide con el número de objetivos
  específicos.** Es el error que más rebota en sustentación.
- **Escala declarada como "Likert" a secas**, sin decir de cuántos puntos ni qué
  significa cada extremo.
- **Ítems inventados.** Si el instrumento no está definido, los ítems van como
  previstos y marcados, nunca como si ya existieran.
