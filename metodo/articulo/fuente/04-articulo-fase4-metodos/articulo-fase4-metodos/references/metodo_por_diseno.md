# Métodos según el diseño

Los cinco subtítulos de `subtitulos_metodo.md` sirven para estudios
cuantitativos con participantes. Cualitativo, instrumental, mixto y datos
secundarios tienen su propia estructura, y usarles la plantilla cuantitativa se
nota en la primera página. Las revisiones tienen su propia ruta. Al final, qué
declarar del análisis según su tipo.

---

## Cualitativo

```
1 · Enfoque y diseño
2 · Participantes y muestreo
3 · Técnicas e instrumentos de recolección
4 · Procedimiento
5 · Análisis de la información
6 · Rigor y aspectos éticos
```

**Qué cambia respecto del cuantitativo:**

- **No hay Tabla 1 sociodemográfica.** Se describen los participantes en prosa,
  o en una tabla de perfil con seudónimos si son pocos: código, rol, años de
  experiencia. Nunca nombres.
- **El muestreo es por criterio, teórico o por conveniencia**, y se justifica con
  su autor. El número de participantes se explica por **saturación**, y hay que
  decir cómo se determinó, no solo afirmarla.
- **Las técnicas se describen con detalle**: cuántas entrevistas, de qué
  duración, presenciales o virtuales, grabadas o no. Si hubo grabación, el
  permiso explícito.
- **El análisis dice qué se hizo, no solo su nombre**: codificación abierta,
  categorías previas o emergentes, si hubo software (Atlas.ti, NVivo, con su
  versión) o si fue manual, y si codificó más de una persona.
- **Rigor** es un subtítulo propio y no es opcional: credibilidad,
  transferibilidad, dependibilidad y confirmabilidad, con lo que se hizo para
  cada una (triangulación, verificación con los participantes, auditoría
  externa). Enumerar los cuatro criterios sin decir qué se hizo es relleno.

**Apoyo para el análisis**: si la codificación se hizo en el servidor
(`analisis-cualitativo`) o en Atlas.ti, se declara así, con la versión, y se
describe lo que se hizo con esa herramienta (libro de códigos, codificación
abierta o deductiva, quién codificó). Los resultados por categoría son de la
Fase 5.

---

## Instrumental o de validación de escala

```
1 · Enfoque y diseño
2 · Participantes                      (con la Tabla 1)
3 · Instrumento
4 · Procedimiento de adaptación
5 · Análisis de las propiedades psicométricas
6 · Aspectos éticos
```

**Lo propio de este diseño:**

- **El subtítulo 3 es el centro del artículo**, no un párrafo más. Versión
  original con su autor y año, número de ítems, dimensiones, formato de
  respuesta, idioma original y en qué poblaciones se validó antes.
- **El subtítulo 4 describe la adaptación paso a paso**: traducción directa,
  retrotraducción, comité de expertos con su número y perfil, prueba piloto con
  su n. Cada etapa con lo que efectivamente se hizo.
- **El subtítulo 5 declara qué propiedades se examinaron y con qué**: análisis
  factorial exploratorio o confirmatorio y con qué método de estimación,
  índices de ajuste que se van a reportar, fiabilidad por consistencia interna,
  validez convergente y discriminante, y si aplica, invarianza entre grupos.
- **La muestra suele dividirse** para exploratorio y confirmatorio. Si se
  dividió, decir cómo y en qué proporción.
- **El permiso de uso del instrumento original**, cuando corresponde, va en
  aspectos éticos. Es un dato que las revistas piden y que casi nadie reporta.

---

## Mixto

Lleva los subtítulos de las dos ramas, **más uno propio**: cómo se integran los
resultados de ambas fases y en qué momento. Sin ese subtítulo, el artículo se
lee como dos estudios cortos pegados, y así lo señala el revisor.

Además se declara el diseño mixto específico (secuencial explicativo,
secuencial exploratorio o convergente) y el orden real en que se recogieron los
datos.

---

## Datos secundarios (encuestas nacionales, bases públicas o institucionales)

```
1 · Enfoque, alcance y diseño
2 · Fuente de datos y muestra          (con la Tabla 1, ponderada si aplica)
3 · Variables y medición
4 · Análisis de datos
5 · Aspectos éticos y licencia de uso
```

- **Fuente de datos y muestra**: quién levantó la base (propietario), año o
  periodo, diseño muestral original (estratos, conglomerados), cómo se accedió
  (enlace, **versión y fecha de descarga**), unidad de análisis, filtros
  aplicados en orden y **n final** tras cada filtro.
- **Variables y medición**: módulo y nombre de cada variable en el
  diccionario, su codificación, y cómo se construyó cada índice (ítems,
  recodificación, suma o promedio, fiabilidad si es escala). Nada de
  «se aplicó un cuestionario».
- **Análisis**: tratamiento de perdidos; si se usó el **factor de expansión** y
  el diseño (`survey::svydesign` con pesos, estratos y conglomerados), y que
  los porcentajes y modelos se estimaron con él.
- **Ética**: datos anonimizados y públicos suelen estar exentos de comité, pero
  se declara igual, con la licencia de la base. La cita de la base (DOI o URL)
  entra al inventario como cualquier fuente.
- Panel o series: los años o periodos usados y si el panel está balanceado.

---

## Qué declarar del análisis según su tipo

El tipo sale del índice de `analisis.md` (pregunta → análisis). Una línea por
tipo; las cifras son de la Fase 5.

| Tipo | Se declara en Métodos |
|---|---|
| Descriptivo | Estadísticos usados; ponderación si la hay |
| Comparación (t, ANOVA, no paramétricas, χ²) | Criterio de normalidad y de elección de la prueba; post hoc; tamaño del efecto |
| Regresión lineal | Variables y su ingreso, supuestos revisados (VIF, residuos), errores robustos si se usaron |
| Logística, ordinal, multinomial | Categoría de referencia, OR con IC 95 %; prueba de líneas paralelas (ordinal) |
| Conteo | Poisson o binomial negativa según sobredispersión; ceros inflados si aplica |
| Multinivel | Niveles, efectos aleatorios, modelo nulo e ICC, estimador |
| Panel | Efectos fijos o aleatorios y la prueba de Hausman; errores agrupados |
| Series de tiempo | Estacionariedad, criterio de selección del modelo (AIC) |
| Mediación / moderación | Modelo, efecto indirecto con IC bootstrap (B y semilla); interacción centrada si se centró |
| SEM (PLS o CB) | Ver `subtitulos_metodo.md`, subtítulo 4 |
| Validación de escala | Ver «Instrumental» arriba |

Software y versión siempre. Lo que no esté decidido queda
`[POR CONFIRMAR: ... (Fase 5)]`.
