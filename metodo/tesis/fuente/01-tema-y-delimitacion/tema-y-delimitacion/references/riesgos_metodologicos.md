# Riesgos metodológicos que la skill debe detectar automáticamente

A diferencia de los errores comunes (`errores_comunes.md`), que son problemas de formulación del tema, los riesgos metodológicos son problemas que aparecen **después** de definir variables y población. La skill debe detectarlos sola y señalarlos al tesista. No esperes a que el tesista los note.

Cuando detectes uno, márcalo explícitamente con checklist y explica el porqué en una o dos frases. No maquilles.

## Riesgo 1 — Heterogeneidad de edad en la población

**Señal:** el tesista trabaja con "toda la secundaria" (1º a 5º), "toda la primaria", "estudiantes de 12 a 18 años" u otro rango etario amplio, con variables que dependen del desarrollo cognitivo o psicosocial.

**Por qué es un riesgo:** constructos como pensamiento crítico, autorregulación, identidad, comprensión lectora compleja, cambian sustancialmente entre un niño de 12 años y un adolescente de 16-17. Si correlacionas sin controlar por edad/grado, la correlación queda contaminada.

**Cómo señalarlo:**

```
- [ ] Riesgo detectado: heterogeneidad de edad en la población.
   Tu variable [V2] depende del desarrollo cognitivo. Si trabajas con
   1º a 5º de secundaria, vas a necesitar controlar por grado en el
   análisis (segmentación por grado, ANOVA, regresión con grado como
   covariable). Alternativa más simple: acotar a 4º y 5º, donde el
   constructo ya está más maduro.
```

## Riesgo 2 — Confusión entre correlacional y explicativo

**Señal:** el tesista declaró enfoque correlacional pero su título o sus preguntas usan verbos causales ("influye", "afecta", "mejora", "reduce", "genera").

**Por qué es un riesgo:** correlacional mide asociación, no causalidad. Si su título dice "influencia de X sobre Y" o "efecto de X en Y", está saltando a explicativo, lo cual exige diseño cuasi-experimental, control de variables extrañas y muestra más grande.

**Cómo señalarlo:**

```
- [ ] Riesgo detectado: direccionalidad en lenguaje correlacional.
   Tu título usa "[verbo causal]" pero declaraste enfoque correlacional.
   En correlacional NO se afirma causalidad. Dos opciones: mantén
   correlacional y reformula el título como "[V1] y [V2] en [población],
   [ciudad-año]" (SIN conector "relación", "influencia" ni "efecto";
   ver Regla 2 y Regla 3 del Paso 4 del SKILL.md), o sube a explicativo
   y ajusta tu metodología (diseño, tamaño de muestra, control de
   variables extrañas). Si subís a explicativo, usá "Influencia de [V1]
   en [V2]" si es no experimental, o "Efecto de [V1] en [V2]" si es
   experimental.
```

## Riesgo 3 — Instrumentos con licencia paga sin financiamiento

**Señal:** la variable propuesta se mide típicamente con un test que tiene licencia paga (Watson-Glaser, CCTST, MBI completo, WAIS, BAI, BDI) y el tesista no mencionó financiamiento ni acceso institucional al instrumento.

**Por qué es un riesgo:** si el tesista no puede pagar el instrumento, la tesis se queda sin medición válida. Suelta esta advertencia antes de avanzar.

**Cómo señalarlo:**

```
- [ ] Riesgo detectado: instrumento con licencia paga.
   La medición de [variable] se hace típicamente con [nombre genérico
   del instrumento], que tiene licencia paga. Verifica si tu universidad
   te lo financia o tiene acceso institucional. Alternativas: usar la
   medición por [versión alternativa libre], o usar una adaptación
   académica peruana validada en tesis previas (búscala en repositorios
   como Renati, Cybertesis o el de tu universidad).
```

## Riesgo 4 — Tema saturado sin giro propio

**Señal:** la combinación de variables del tesista corresponde a un tema con cientos de publicaciones recientes en español (por ejemplo, "uso de redes sociales y rendimiento académico", "clima organizacional y desempeño laboral", "IA y aprendizaje").

**Por qué es un riesgo:** el asesor o el jurado puede objetar la falta de aporte. Es mejor anticipar y proponer un giro.

**Cómo señalarlo:**

```
- [ ] Riesgo detectado: tema saturado.
   "[par de variables]" tiene decenas de tesis recientes en tu país.
   Posibles giros para diferenciar tu aporte:
   (a) precisar el tipo de [variable] (por ejemplo, solo IA generativa
       en vez de "IA" en general).
   (b) precisar el área curricular o la sub-población.
   (c) añadir una variable mediadora o moderadora.
   (d) trabajar con un grado o contexto no estudiado en tu zona.
   Llévalo a tu asesor para que escoja el giro que mejor encaje con
   la línea de investigación de la escuela.
```

## Riesgo 5 — Población inaccesible aunque el tesista crea que sí tiene acceso

**Señal:** el tesista declaró "acceso confirmado" pero la población son funcionarios de alto nivel, ejecutivos top, profesionales con agenda muy demandada, o requiere autorización de varios niveles jerárquicos (MINEDU, Ministerio de Salud, gerencias generales).

**Por qué es un riesgo:** "conocer a alguien dentro" no garantiza acceso real al volumen de muestra que pide pregrado (mínimo 30-50 sujetos para correlacional, idealmente 100+).

**Cómo señalarlo:**

```
- [ ] Riesgo detectado: acceso a campo posiblemente sobreestimado.
   Dijiste que tienes acceso confirmado, pero tu población es [tipo].
   Verifica que puedas alcanzar la muestra mínima (30 sujetos para
   correlacional básica, idealmente más). Si solo tienes un contacto
   facilitador pero no autorización formal de la institución, prepara
   un plan B con otra población.
```

## Riesgo 6 — Variables vagas que el tesista cree que son medibles

**Señal:** el tesista propone variables como "calidad humana", "buen servicio", "éxito empresarial", "felicidad", sin un constructo psicométrico detrás.

**Por qué es un riesgo:** sin instrumento validado, no hay tesis cuantitativa posible. Hay que reoperacionalizar.

**Cómo señalarlo:**

```
- [ ] Riesgo detectado: variable vaga.
   "[nombre de la variable]" no es un constructo medible directamente.
   Necesitas reemplazarla por un constructo con instrumento validado.
   Opciones: [proponer 2-3 constructos equivalentes con literatura
   consolidada, sin citar autores específicos].
```

## Cuándo señalar los riesgos

- Señálalos durante el **Paso 2 (diagnóstico)**, dentro del punto "Problemas anticipados".
- Si aparecen después (por ejemplo, el tesista escoge una población heterogénea en el sub-flujo de operacionalización), señálalos en el momento.
- Repítelos brevemente en el **Paso 5 (cierre)** dentro del checklist "Verifica con tu asesor".
- Inclúyelos en la fila "Observaciones para el asesor" de la tabla resumen del **Paso 6**.

## Cómo NO señalar los riesgos

- No los maquilles ("podría haber un pequeño detalle"). Si es un riesgo real, dilo claro.
- No los conviertas en obstáculos paralizantes ("esto no va a funcionar"). Siempre acompáñalos de alternativas concretas.
- No los inventes. Si el tesista no activó ninguno de los disparadores listados, no fuerces un riesgo.
