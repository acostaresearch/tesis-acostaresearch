# Título tentativo — Guía completa

> **Nota sobre los años en los ejemplos**: los ejemplos de este archivo usan un año fijo con fines ilustrativos. La skill NUNCA copia ese año: lo sustituye por el que corresponde al tesista, derivado de la fecha actual del contexto y del año de sustentación que él declaró en la Tanda 3 del Paso 1.


Cuatro reglas duras se aplican SIEMPRE, en cualquier país hispanohablante, en pregrado, maestría y doctorado:

1. **Anonimato institucional**: sin nombre real ni siglas del centro.
2. **Sin "Relación de/entre"** al inicio de correlacionales.
3. **Verbo correcto según el nivel de investigación** (descriptivo, correlacional, comparativo, explicativo experimental o no experimental, aplicado).
4. **Máximo 20 palabras** contando después de aplicar las tres reglas anteriores.

## Estructura según el nivel de investigación

| Nivel                         | Estructura del título                                                          |
|-------------------------------|--------------------------------------------------------------------------------|
| Descriptivo                   | [Fenómeno o V1] en [Población anonimizada], [Ciudad, año]                      |
| Correlacional                 | [V1] y [V2] en [Población anonimizada], [Ciudad, año]                          |
| Comparativo                   | [V1] según [Factor de agrupamiento] en [Población anonimizada], [Ciudad, año]  |
| Explicativo no experimental   | Influencia de [V1] en [V2] en [Población anonimizada], [Ciudad, año]           |
| Explicativo experimental      | Efecto de [Intervención o V1] en [V2] en [Población anonimizada], [Ciudad, año]|
| Aplicada / propositiva        | [Producto o modelo] para [Fenómeno o problema] en [Población anonimizada], [Ciudad, año] |

**La tabla anterior aplica solo al enfoque CUANTITATIVO.** Para cualitativo y mixto, ver las dos tablas siguientes.

## Estructura según el diseño CUALITATIVO

En cualitativo el título NUNCA lleva "y" entre variables, ni "relación", ni "influencia", ni "efecto". El título debe delatar que el estudio es comprensivo, no medidor.

| Diseño                  | Estructura del título                                                        |
|-------------------------|------------------------------------------------------------------------------|
| Fenomenológico          | Experiencia de [fenómeno] en [Población anonimizada], [Ciudad, año] · o "Vivencias de..." · o "Significados de [fenómeno] para..." |
| Estudio de caso         | [Fenómeno] en [caso delimitado y anonimizado]: estudio de caso, [Ciudad, año] |
| Etnográfico             | Prácticas de [fenómeno] en [Población anonimizada], [Ciudad, año] · o "Cultura de..." |
| Teoría fundamentada     | [Fenómeno] en [Población anonimizada]: una aproximación desde la teoría fundamentada, [Ciudad, año] |
| Narrativo / biográfico  | Trayectorias de [fenómeno] en [Población anonimizada], [Ciudad, año] · o "Historias de vida de..." |
| Investigación-acción    | [Intervención o mejora] mediante investigación-acción en [Población anonimizada], [Ciudad, año] |

Ejemplos que cumplen las 4 reglas:

- Vivencias de docentes noveles en su primer año de aula en una institución educativa pública, Trujillo-2026. (16 palabras)
- Gestión del voluntariado en una organización no gubernamental: estudio de caso, Lima-2026. (12 palabras)
- Significados del retorno migratorio para adultos jóvenes de una comunidad andina, Cusco-2026. (13 palabras)

## Estructura según el enfoque MIXTO

| Situación                            | Estructura del título                                                  |
|--------------------------------------|------------------------------------------------------------------------|
| Una fase domina                      | [V1 o fenómeno principal] en [Población anonimizada]: un estudio de métodos mixtos, [Ciudad, año] |
| Ambas fases con el mismo peso        | [V1] y [V2] en [Población anonimizada]: aproximación mixta, [Ciudad, año] |

Ejemplo:

- Clima organizacional y rotación de personal en una empresa retail privada: aproximación mixta, Lima-2026. (15 palabras)

## Regla dura de coherencia enfoque-título

El título debe delatar el enfoque sin necesidad de leer la metodología.

```
MAL:  Título cualitativo que dice "Relación entre X y Y"
MAL:  Título cuantitativo que dice "Vivencias de..."
MAL:  Título fenomenológico que dice "Influencia de X en Y"
MAL:  Título correlacional que dice "estudio de caso"
```

Antes de entregar cualquier alternativa, verificá que la estructura elegida corresponda al enfoque y al diseño declarados por el tesista en la Tanda 2 del Paso 1.

### Cómo elegir entre "Influencia" y "Efecto" para explicativos

- **Efecto de** → cuando el tesista **aplicará una intervención** (programa, taller, capacitación, protocolo, tratamiento) y medirá antes/después. Diseño experimental o cuasi-experimental.
- **Influencia de** → cuando el tesista **solo medirá dos variables ya existentes** en la población y buscará que una explique estadísticamente a la otra sin manipular nada. Diseño explicativo no experimental (regresión lineal, regresión logística, análisis de senderos).

Si el tesista no sabe cuál corresponde, hay que preguntarle con `ask_user_input_v0` antes de generar el título:

```
Para tu tesis explicativa, ¿vas a aplicar una intervención
(programa, taller, capacitación) o solo vas a medir dos
variables ya existentes?

- Voy a aplicar una intervención y medir antes/después
- Solo voy a medir dos variables sin manipular nada
- No sé, ayúdame a decidir
```

## Regla 1 — Anonimato del centro

**Prohibido** escribir en el título:
- Nombres propios de universidades, empresas, hospitales, colegios, ministerios, bancos, municipios, ONG.
- Siglas del centro (UNT, UCV, UNMSM, USS, MINSA, INEI, etc.).

**Reemplazos correctos** (usá el que corresponda al tipo de centro):

| Centro real                   | Cómo aparece en el título                                        |
|-------------------------------|------------------------------------------------------------------|
| Universidad pública           | "una universidad pública"                                        |
| Universidad privada           | "una universidad privada"                                        |
| Empresa privada (industrial)  | "una empresa privada del sector industrial" o "una empresa industrial privada" |
| Empresa privada (retail)      | "una empresa privada del sector retail" o "una empresa retail privada" |
| Empresa pública               | "una empresa pública del sector [rubro]"                         |
| Hospital público              | "un hospital público"                                            |
| Clínica privada               | "una clínica privada"                                            |
| Institución educativa pública | "una institución educativa pública"                              |
| Institución educativa privada | "una institución educativa privada"                              |
| Municipalidad distrital       | "una municipalidad distrital"                                    |
| Municipalidad provincial      | "una municipalidad provincial"                                   |
| Ministerio                    | "una entidad pública del sector [rubro]"                         |
| Banco                         | "una entidad bancaria"                                           |
| Cooperativa financiera        | "una entidad financiera cooperativa"                             |
| Call center                   | "una empresa de servicios de contact center"                     |
| ONG                           | "una organización no gubernamental"                              |
| Fuerzas armadas / policiales  | "una entidad castrense" o "una entidad policial"                 |

El nombre real de la institución **sí va** en la tabla resumen (Capítulo 1, campo "Población" o "Contexto") y en el Capítulo 3 (Metodología, subsección Población y muestra). En el TÍTULO no.

## Regla 2 — Sin "Relación de/entre" al inicio (correlacional)

Para tesis correlacionales, el conector entre las dos variables es la simple **"y"**. No lleva verbo al inicio. "Relación de", "Relación entre", "Asociación entre", "Vínculo entre" son palabras de OBJETIVO (Capítulo 2), no de TÍTULO.

```
MAL:  "Relación entre clima laboral y desempeño en trabajadores..."
BIEN: "Clima laboral y desempeño laboral en trabajadores..."

MAL:  "Asociación de estrés y burnout en enfermeras..."
BIEN: "Estrés laboral y síndrome de burnout en enfermeras..."

MAL:  "Vínculo entre uso de TIC y rendimiento académico..."
BIEN: "Uso de TIC y rendimiento académico..."
```

## Ejemplos que cumplen las 4 reglas

**Correlacionales**:

- Clima organizacional y desempeño laboral en colaboradores de una empresa retail privada, Trujillo-2026. (13 palabras)
- Uso de redes sociales y rendimiento académico en estudiantes de Ingeniería Civil de una universidad pública, Trujillo-2026. (17 palabras)
- Estrategias docentes y motivación lectora en estudiantes de quinto grado de primaria de una institución educativa pública, Cajamarca-2026. (18 palabras)

**Descriptivas**:

- Clima organizacional en colaboradores de una empresa retail privada, Trujillo-2026. (10 palabras)
- Niveles de ansiedad académica en estudiantes de quinto año de Medicina de una universidad privada, Lima-2026. (16 palabras)

**Comparativas**:

- Síndrome de burnout en docentes según tipo de gestión, instituciones educativas de Chiclayo-2026. (13 palabras)

**Explicativas no experimentales**:

- Influencia del liderazgo transformacional en el compromiso organizacional en colaboradores de una empresa industrial privada, Lima-2026. (16 palabras)
- Influencia del uso de herramientas de IA generativa en el pensamiento crítico en estudiantes de Educación de una universidad pública, Trujillo-2026. (21 palabras — pasa por 1)

Ese último caso muestra qué hacer cuando el título pasa por poco: aplicar el algoritmo de recorte.

**Explicativas experimentales**:

- Efecto del programa "Leer contigo" en la comprensión lectora en estudiantes de sexto grado de una institución educativa pública, Trujillo-2026. (19 palabras)

**Aplicadas o propositivas**:

- Modelo de gestión por competencias para una municipalidad distrital, La Libertad-2026. (11 palabras)

## Reglas de validación (checklist)

Antes de entregar cualquier título tentativo:

- [ ] ≤ 20 palabras (contá cada palabra, los conectores cuentan; verificá DESPUÉS de aplicar las 3 reglas siguientes).
- [ ] Sin nombre real ni siglas del centro (Regla 1).
- [ ] Sin "Relación de/entre" al inicio si es correlacional (Regla 2).
- [ ] Coherencia enfoque-título: si es cualitativo NO dice "relación", "influencia" ni "efecto"; si es cuantitativo NO dice "vivencias", "significados" ni "trayectorias".
- [ ] Coherencia nivel académico: el alcance corresponde a pregrado, maestría o doctorado según lo declarado.
- [ ] Verbo correcto según el nivel de investigación (Regla 3).
- [ ] Sin verbos de objetivo: nada de "Analizar", "Determinar", "Identificar", "Establecer", "Evaluar".
- [ ] Variables o fenómeno central claros.
- [ ] Población especificada con anonimato (con el grado de generalidad que permita el acceso a campo).
- [ ] Ciudad incluida.
- [ ] Año incluido.
- [ ] Entendible para alguien ajeno a la carrera.
- [ ] Sin jergas innecesarias.
- [ ] Sin em dashes ni guiones largos.

## Antiejemplos (qué NO hacer)

- "Analizar el clima organizacional en empresas". → Verbo de objetivo, sin población, sin contexto, sin año.
- "Relación entre uso de IA generativa y pensamiento crítico en estudiantes de Educación de la UNT, Trujillo, 2026". → Viola Regla 2 (empieza con "Relación entre") y Regla 1 (menciona UNT).
- "Uso de herramientas de IA generativa y pensamiento crítico en estudiantes de Educación, UNT, Trujillo, 2026". → Viola Regla 1 (UNT). Corrección: "…en estudiantes de Educación de una universidad pública, Trujillo-2026".
- "El impacto significativo y transformador del uso intensivo de las redes sociales en el rendimiento académico de los estudiantes universitarios de pregrado de la carrera de Ingeniería Civil de una universidad pública, Trujillo, 2026". → 32 palabras. Sobrecargado con adjetivos valorativos.
- "Clima y desempeño". → Demasiado corto, sin población, sin contexto.
- "La educación peruana en tiempos modernos". → Tema de libro, no de tesis.

## Algoritmo de recorte cuando pasa de 20 palabras

Si el título supera las 20 palabras, recortar en este orden:

1. **Quitar "Estudio de", "Análisis de", "Investigación sobre"** al inicio (casi siempre sobran).
2. **Quitar adjetivos valorativos**: "significativo", "transformador", "importante", "profundo", "integral", "exhaustivo". No aportan precisión.
3. **Compactar la descripción del centro anonimizado**: "una empresa privada del sector industrial" → "una empresa industrial privada".
4. **Simplificar la población**: "estudiantes universitarios de pregrado de la carrera de X" → "estudiantes de X".
5. **Unificar "Ciudad, año" con guion**: "Trujillo, 2026" → "Trujillo-2026" (ahorra una coma pero cuenta como dos palabras igual; el ahorro es en fluidez, no en conteo).
6. **Quitar el "de [Ciudad]" si ya es evidente por el contexto** o si se está usando dos veces la misma ciudad.
7. **Como último recurso**: reducir el número de variables (si son 3, ir a 2; si son 2, ver si una es una dimensión y no una variable independiente).

Si después de aplicar los 7 pasos sigue pasando de 20 palabras, el tema está demasiado cargado. Reducir el número de variables o sub-poblaciones antes de forzar el título.

**Regla anti-inflación**: si el recorte deja lugar (ej. quedó en 15 palabras), NO volver a inflar con palabras decorativas. Un título de 15 palabras es mejor que uno de 20 con relleno.

## Cuando el tesista pida variantes

Entregar 2 o 3 alternativas, todas bajo las mismas 4 reglas. Marcar con checklist cuál cumple cada criterio y dejar que el tesista elija con base informada.

Ejemplo de entrega:

```
Alternativa 1: [título A] ([N] palabras)
Alternativa 2: [título B] ([N] palabras)
Alternativa 3: [título C] ([N] palabras)

Diferencias:
- Alternativa 1: correlacional, dos variables, población amplia.
- Alternativa 2: correlacional, dos variables, población acotada por grado o sede.
- Alternativa 3: explicativa no experimental (usa "Influencia de"), foco predictivo.
```

Si una alternativa resuelve un riesgo metodológico que las otras tienen, decirlo honestamente al final ("La Alternativa 2 evita el riesgo de heterogeneidad porque acota a un solo grado").
