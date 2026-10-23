# Teoría base y dimensiones

Las dimensiones no son tentativas. Son el cimiento sobre el que se construyen los antecedentes (Cap 3), la operacionalización (Cap 4), el instrumento (Cap 5) y los resultados (Cap 7). Por eso se establecen aquí en el Capítulo 2, basadas en teorías reconocidas, y se fijan para todo el resto de la tesis.

## Qué es una teoría base

Una teoría base es un modelo conceptual reconocido por la comunidad académica que:

1. **Define la variable** con precisión.
2. **Propone dimensiones** que la componen.
3. **Está validada en literatura** con uso recurrente.
4. **Tiene instrumentos asociados** que se han usado para medirla.

No es lo mismo que una cita aislada. Una autora que dice "el clima organizacional es importante" no es una teoría. Una teoría es un sistema de constructos relacionados.

## Cómo extraer teorías base desde las fuentes de su biblioteca

Cuando el tesista no tiene teoría base elegida, la skill las extrae automáticamente. El proceso:

### Paso 1 — Análisis automático de las fuentes

1. Leer los abstracts y keywords de las fuentes de su biblioteca (las que devuelven `buscar_fuentes` y `mis_fuentes`, más lo que el tesista trajo al chat).
2. Para cada variable, identificar:
   - Autores que aparecen citados repetidamente en marcos teóricos.
   - Nombres de modelos o escalas mencionados (ejemplo: "modelo de Litwin y Stringer", "escala de Facione").
   - Constructos relacionados que se usan como sinónimos de la variable.
3. Generar una lista de teorías candidatas ordenada por frecuencia de aparición.

### Paso 2 — Filtrado por calidad

De la lista candidata, descartar:

- Teorías mencionadas en una sola fuente (poca consolidación).
- Autores citados sin un modelo claro asociado.
- Teorías muy antiguas (más de 30 años) si hay alternativas más recientes y consolidadas.
- Teorías de áreas distintas a la del tesista.

### Paso 3 — Presentación de 2-3 teorías al tesista

Para cada variable, presentar 2-3 candidatas con esta estructura:

```
Teoría: [nombre del modelo]
Autor original: [Apellido(s)], [año]
Idea central: "[paráfrasis breve extraída de una fuente
              de su biblioteca, con su clave]"
Dimensiones que propone:
  - Dimensión 1
  - Dimensión 2
  - Dimensión N
Frecuencia en tus fuentes: aparece en [N] de [X] fuentes
Por qué encajaría con tu estudio: [1-2 frases con base en
   el tema y población del tesista]
Fuente principal donde aparece: [Apellido(s), año y su clave [AR…]]
```

### Paso 4 — Confirmación del tesista

Usar `ask_user_input_v0` con single_select por cada variable. El tesista elige UNA teoría por variable.

Si rechaza todas, ofrecer:
- "Busquemos fuentes de otra teoría que tengas en mente" (con `buscar_fuentes`)
- "Conversa con tu asesor para que te recomiende una teoría base específica de tu línea de investigación"

No avances sin teoría base elegida.

## Cómo validar una teoría que el tesista ya tiene

Si el tesista llega con teoría base elegida, validar contra fuentes:

1. Buscar el nombre de la teoría (y del autor) en los abstracts y keywords.
2. Contar cuántas fuentes la mencionan.
3. Si aparece en al menos 3 fuentes: validada, avanza.
4. Si aparece en 1-2 fuentes: advertir al tesista que su teoría está poco respaldada en su literatura actual, sugerir buscar más fuentes (`buscar_fuentes`) o reconsiderar.
5. Si no aparece: advertir que su teoría no está en su biblioteca. Dos caminos: buscar y añadir fuentes que la respalden (`buscar_fuentes`, `anadir_a_mis_fuentes` por DOI o su Zotero), o reconsiderar la teoría.

## Ejemplos de teorías base por área

Estos son referenciales, no exhaustivos. La skill siempre extrae teorías desde las fuentes del tesista, no desde esta lista. Esta lista sirve solo para que la skill reconozca patrones comunes. No se cita de aquí: los autores clásicos también entran al texto con su clave.

### Administración / Gestión

- **Clima organizacional**: modelo de Litwin y Stringer (1968), modelo de Likert (1967), modelo de Brunet (1987).
- **Cultura organizacional**: modelo de Schein (1985), modelo de Cameron y Quinn (1999).
- **Liderazgo**: liderazgo transformacional de Bass (1985), modelo de Likert.
- **Compromiso organizacional**: modelo de Meyer y Allen (1991) con sus tres componentes.
- **Satisfacción laboral**: teoría bifactorial de Herzberg (1959), modelo JDI.

### Educación

- **Aprendizaje**: teoría socio-constructivista de Vygotsky, aprendizaje significativo de Ausubel.
- **Competencias digitales**: marco DigComp de la Comisión Europea, marco TPACK de Mishra y Koehler (2006).
- **Pensamiento crítico**: modelo de Facione (1990 Delphi Report), modelo de Paul y Elder.
- **Motivación**: teoría de autodeterminación de Deci y Ryan (1985), teoría de metas de logro.
- **Estrategias docentes**: aprendizaje significativo de Ausubel, taxonomía de Bloom revisada.

### Psicología

- **Burnout**: modelo de Maslach (1981) con tres dimensiones (agotamiento, despersonalización, realización personal).
- **Inteligencia emocional**: modelo de Goleman (1995), modelo de Mayer y Salovey.
- **Resiliencia**: modelo de Wagnild y Young (1993), modelo de Connor y Davidson.

### Ciencias de la Salud

- **Adherencia terapéutica**: modelo de creencias en salud de Becker (1974), modelo transteórico de Prochaska.
- **Calidad de vida**: modelo de la OMS WHOQOL.
- **Cuidado**: teoría del cuidado humano de Watson, teoría del autocuidado de Orem.

### Tecnología educativa / IA en educación

- **Adopción tecnológica**: modelo TAM de Davis (1989), UTAUT de Venkatesh.
- **Aprendizaje con IA**: marcos emergentes (AI Literacy de Long y Magerko, 2020).

## Cómo derivar objetivos e hipótesis desde las dimensiones

Una vez fijadas las dimensiones, los objetivos específicos y las hipótesis específicas se derivan así:

### Caso 1 — Estudio correlacional clásico

V1 tiene 3 dimensiones, V2 tiene 1 dimensión (o se trata como variable única).

Objetivos específicos = 1 por cada dimensión de V1 que se relaciona con V2:
- Objetivo específico 1: relación entre dimensión 1 de V1 y V2.
- Objetivo específico 2: relación entre dimensión 2 de V1 y V2.
- Objetivo específico 3: relación entre dimensión 3 de V1 y V2.

Hipótesis específicas: misma cantidad, con H1 y H0 cada una.

### Caso 2 — Estudio correlacional con dos variables multidimensionales

V1 tiene 3 dimensiones, V2 tiene 3 dimensiones.

No necesariamente 9 hipótesis (sería excesivo en pregrado). Estructura más común:
- Objetivo específico 1: caracterizar V1 (sus 3 dimensiones).
- Objetivo específico 2: caracterizar V2 (sus 3 dimensiones).
- Objetivo específico 3: relación entre V1 (global) y V2 (global).
- Objetivo específico 4 (opcional): relación entre las dimensiones de V1 y V2.

### Caso 3 — Estudio descriptivo

Sin hipótesis (regla general) o con hipótesis si es descriptivo-comparativo o epidemiológico en salud.

Objetivos específicos: 1 por cada dimensión que se busca describir o caracterizar.

### Caso 4 — Estudio explicativo

V1 (independiente) tiene N dimensiones, V2 (dependiente) es la variable predicha.

Objetivos específicos: 1 por cada dimensión de V1 que se quiere probar como predictor de V2.

Hipótesis específicas: H1 afirma efecto/influencia, H0 niega efecto significativo.

## Cierre del Paso 4 en la skill

Una vez teoría y dimensiones fijadas:

1. Confirmar al tesista por escrito qué teoría y qué dimensiones quedaron seleccionadas.
2. Indicar explícitamente: "Estas dimensiones quedan fijas. Si tu asesor las cambia, será necesario rehacer la matriz, los antecedentes y la operacionalización."
3. Sugerir conversar con el asesor antes de avanzar al Paso 5 si hay duda.
