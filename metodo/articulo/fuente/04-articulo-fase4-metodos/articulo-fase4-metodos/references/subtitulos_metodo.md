# Los cinco subtítulos de Métodos

Para estudios cuantitativos con participantes. Cualitativos, instrumentales,
mixtos y con datos secundarios tienen su estructura en `metodo_por_diseno.md`. La Tabla 1 es un
elemento de Participantes, no un subtítulo.

---

## 1 · Enfoque, alcance y diseño

Enfoque (cuantitativo, cualitativo, mixto), alcance sustentado en un autor
metodológico, diseño (experimental o no experimental) y temporalidad
(transversal o longitudinal).

Si el estudio usa SEM, **justificar la elección de la técnica**: PLS-SEM por su
idoneidad para modelos predictivos con variables latentes y sin exigencia de
normalidad multivariada; CB-SEM cuando el objetivo es confirmar una teoría con
buen ajuste global. La justificación se apoya en un autor metodológico
verificable, no en una afirmación general.

De aquí sale el término que se usa en todo el artículo, y ya viene fijado desde
la Fase 1: *influencia* o *efecto* con modelo direccional declarado; *relación*
o *asociación* con diseño correlacional o transversal.

## 2 · Participantes

- Población y su tamaño, cuando se conoce.
- Unidad de análisis.
- **Tipo de muestreo con su justificación y su autor.**
- **n recogido y n final tras depuración**, con el motivo de las bajas.
- Remisión a la Tabla 1, que va justo después del párrafo que la cita.

Si el muestreo fue no probabilístico por conveniencia, **se dice tal cual**.
Maquillarlo como aleatorio es un problema de integridad, y la Discusión tendrá
que reconocerlo como limitación de todos modos.

**La Tabla 1**: número, título en cursiva y nota, APA 7 (solo reglas
horizontales). La nota declara N, que los porcentajes son sobre casos válidos,
los perdidos y el n válido por variable, los códigos tratados como perdido,
toda unificación de categorías y los decimales (% con uno; M y DE con dos).
Las etiquetas salen del libro de códigos, no se suponen. `tabla1.py --md` la
deja así.

## 3 · Instrumentos

Un párrafo por instrumento:

- Qué mide.
- **De quién es la escala original**, o si es de elaboración propia.
- Si se adaptó, cómo: traducción, retrotraducción, juicio de expertos.
- Número de ítems iniciales por constructo.
- **Ítems eliminados tras el análisis factorial y total retenido.**
- Escala de respuesta, con sus anclajes (por ejemplo, Likert de 5 puntos de
  "totalmente en desacuerdo" a "totalmente de acuerdo").
- Modalidad de aplicación.

Si fue formulario en línea, describir su estructura: sección de presentación y
consentimiento informado con pregunta ramificada, sección sociodemográfica y
sección de ítems.

Los ítems eliminados se reportan **con su criterio real**: "se eliminaron los
ítems X, Y y Z por presentar cargas factoriales inferiores a 0.70 y afectar la
fiabilidad y el AVE del constructo". **Los identificadores se piden; no se
inventan.**

## 4 · Procedimiento y análisis de datos

- **Fechas reales de recolección.**
- Tipo de institución donde se hizo el trabajo de campo, descrita de forma
  genérica.
- **Software con su versión** (con el servidor: `R.version.string` y
  `packageVersion()` en la sesión).
- La secuencia del análisis, según la vía de `analisis.md`: lo hecho o el plan
  ya decidido (B de bootstrap, tratamiento de perdidos, invarianza). Aquí se
  **describe**; las cifras las reporta la Fase 5, que completa lo que quedó
  `[POR CONFIRMAR]`.

El análisis se elige por la pregunta con el índice de `analisis.md`; qué
declarar de cada tipo (regresión, conteo, multinivel, panel, series,
mediación) está en `metodo_por_diseno.md`. No todo es SEM.

Para SEM: depuración de la base; modelo de medida (cargas, fiabilidad compuesta
y alfa, AVE, validez discriminante por HTMT con su IC bootstrap o
Fornell-Larcker); modelo estructural (VIF, R², Q², f²); bootstrap con el **B
total efectivamente usado y la semilla**; el procedimiento de mediación si
aplica; MGA o MICOM, si se compararon grupos, como pruebas de permutación.

Para diseños no SEM: pruebas de normalidad, estadístico de contraste elegido y
por qué, y tamaño del efecto.

Citar solo los clásicos metodológicos que se puedan verificar, **por su clave
del inventario** (si no está, se agrega por DOI verificado con
`referencias.py doi`, ver `fuentes_y_citas.md`). Si no se puede, marcarla como
pendiente en vez de reconstruirla de memoria.

## 5 · Aspectos éticos

Voluntariedad, consentimiento informado, anonimato, confidencialidad y
tratamiento de los datos.

Si hubo aprobación de un comité, **su nombre y su código**. Si no la hubo o no
se sabe, se marca pendiente y se le dice al investigador que muchas revistas la
exigen y que conseguirla después de recoger los datos no sirve.

**Cada declaración de este subtítulo se confirma una por una.** No se escriben
en bloque porque "siempre van".

---

## Tiempo verbal

Métodos se escribe **en pasado**: describe lo que ocurrió. Si aparece futuro
("se aplicará", "se analizará"), es señal de que el texto viene del proyecto y
no del estudio ejecutado.

## Longitud

Suele ocupar entre el 15% y el 25% del artículo. Un método más corto que eso
casi siempre está incompleto; uno más largo suele traer detalles que van a
material suplementario.
