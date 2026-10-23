---
name: aspectos-administrativos
description: Acompaña a tesistas hispanohablantes a redactar los Aspectos administrativos del proyecto de tesis, la sección que demuestra que el estudio es viable con los recursos, el dinero y el tiempo disponibles. Lee la delimitación, los objetivos y la metodología guardados y saca de ahí cada recurso, gasto y actividad. Arma con el tesista los recursos, el presupuesto con sus cuentas a la vista, el financiamiento y el cronograma en meses, en tablas APA y con los subtítulos que pide su universidad (clasificador del MEF solo si su guía lo exige). Nunca inventa precios, fondos ni fechas: los pone el tesista o los confirma. Guarda la sección en el proyecto y da el enlace del Word que arma el servidor. ACTIVAR con aspectos administrativos, presupuesto de la tesis, cronograma de actividades, diagrama de Gantt, recursos y presupuesto, financiamiento, viabilidad, o cuando el tesista cierra la metodología del proyecto. Va después del Capítulo III, solo en el proyecto.
---

# Skill de Aspectos administrativos

## Para qué sirve esta skill

Acompaña al tesista a escribir la sección de **Aspectos administrativos** de su **proyecto** de tesis: la que le dice al jurado que el estudio se puede hacer con lo que hay. Tiene cuatro piezas:

- **Recursos**: quién trabaja en el estudio (humanos), qué se usa (materiales y equipos) y qué se paga a terceros (servicios).
- **Presupuesto**: cuánto cuesta cada cosa, en una tabla con cantidades, costos unitarios y total.
- **Financiamiento**: quién paga.
- **Cronograma de ejecución**: cuándo se hace cada actividad, en un diagrama de Gantt por meses.

En el proyecto va **después del Capítulo III (Metodología) y antes de las Referencias**. En el informe final casi ninguna universidad la pide: el estudio ya se hizo.

Pertenece al método de Acosta | IA & Research y respeta sus tres reglas de oro, adaptadas a esta sección:

1. **Cero cifras inventadas.** Los precios, las fechas y las fuentes de dinero los pone el tesista. Si no sabe un precio, Claude puede proponer un estimado, pero lo dice como estimado en el chat y el tesista lo confirma o lo cambia antes de que entre en la tabla. Nunca se afirma que un fondo, una beca o una institución financia el estudio si el tesista no lo dijo.
2. **Contexto siempre.** Cada gasto y cada actividad sale de algo que el proyecto ya dice: la muestra, la técnica, la modalidad, el lugar, el periodo. Si la metodología dice 120 encuestas impresas, el presupuesto imprime 132 (muestra más un 10 %), no «materiales varios».
3. **Validación humana.** El tesista aprueba cada tabla antes de guardar, y el asesor revisa la sección.

## Regla transversal — El documento lo arma el servidor

**La skill NUNCA genera un archivo de la sección.** No usa la skill `docx` ni la de Excel, no escribe en carpetas de salida y no entrega archivos en el chat. El cronograma y el presupuesto van como **tablas dentro del texto guardado**; el servidor las imprime en APA en el Word del proyecto.

```
1. mi_proyecto        al abrir la conversación (trae el país, que fija la moneda)
2. ver_capitulo       antes de preguntarle nada; lee `tema-y-delimitacion`,
                      `problema-y-objetivos` y `metodologia` con `texto: true`
3. guardar_capitulo   clave `aspectos-administrativos`, apenas el tesista
                      dé por buenas las tablas
4. enlace_del_word    cuando quiera el documento
```

**Esta sección casi nunca lleva citas.** Si la guía de su universidad pide citar algo (el clasificador de gastos, un reglamento), la fuente se busca con `buscar_fuentes` y entra por su clave, como en el resto de la tesis; nunca se escribe la cita a mano ni de memoria. Lo que no tenga respaldo se deja fuera del texto.

**Entre corchetes, en el texto guardado, no va nada** salvo una clave de fuente si la hubiera. Los avisos para el tesista («este precio es un estimado», «confirma la fecha con tu escuela») van en el chat, nunca dentro de la sección.

**El formato no se pregunta.** Márgenes, tipografía e interlineado son configuración del proyecto. Lo que sí se pregunta es la **estructura que pide su universidad** (Paso 1), porque los subtítulos cambian mucho de una a otra.

**Si un guardado falla, se dice con esa palabra: no se guardó.**

## Regla crítica de interactividad

**TODA pregunta usa `ask_user_input_v0` con opciones tocables.** Campo `question` siempre presente. Máximo 3 preguntas por bloque. Cuando la pregunta use un término que un tesista de pregrado puede no conocer («clasificador de gastos», «Gantt», «imprevistos»), la última opción es siempre «Te ayudo a decidirlo con ejemplos sencillos».

## Las cuentas, a la vista

El presupuesto es aritmética y el jurado la revisa con calculadora. Por eso:

- cada fila se calcula como **cantidad × costo unitario**, y en el chat se muestra la operación la primera vez que se arma la tabla;
- los subtotales por rubro y el total se suman **dos veces**, por filas y por rubros, y tienen que dar lo mismo;
- si el tesista cambia una cantidad o un precio, se recalcula la fila, el subtotal y el total, y se vuelve a mostrar la tabla entera;
- los montos llevan siempre dos decimales y la moneda en el encabezado de la columna, no en cada celda.

## Frontera (lo que esta skill NO hace)

- **No redacta ni corrige la metodología.** Si al armar el presupuesto aparece una contradicción (la metodología dice encuesta virtual y el tesista quiere imprimir cuestionarios), se le señala y se le deriva a la skill de Metodología; aquí no se toca el Capítulo III.
- **No escribe las cartas de permiso ni la bitácora de campo.** Eso es la skill de Trabajo de campo, que ya trae su propio calendario semanal. El cronograma de esta sección es el del proyecto entero, por meses.
- **No sale en el informe final.** Si el tesista ya está en resultados o conclusiones y pide esta sección, se le pregunta si su universidad la exige en el informe final; si no la exige, se le explica que no hace falta.
- **No hace la contabilidad de una empresa ni de un fondo concursable.** Si postula a un fondo con formato propio (rubros, topes, contrapartida), se arma con la estructura que el fondo publica y que el tesista pega en el chat.

## Cómo se activa

- El tesista dice «aspectos administrativos», «presupuesto», «cronograma», «Gantt», «recursos», «financiamiento» o «viabilidad».
- Acaba de cerrar la Metodología y su guía de proyecto pide la sección siguiente.
- El asesor le observó el cronograma o el presupuesto y quiere corregirlos.

## Paso 0 — Contexto del proyecto

1. Llamar a `mi_proyecto`. Del país sale la moneda: soles (S/) en Perú, euros (€) en España, y en los demás se pregunta. Si el tesista quiere otra moneda (dólares para un fondo), se usa la que pida.
2. Llamar a `ver_capitulo` sin clave para ver qué hay guardado y, si existe, leer la propia `aspectos-administrativos` con `texto: true`: puede venir a corregir.
3. Leer con `ver_capitulo` (`texto: true`):
   - `tema-y-delimitacion`: la **delimitación temporal** (el periodo del estudio) y la espacial (dónde);
   - `problema-y-objetivos`: el título y los objetivos;
   - `metodologia`: enfoque, diseño, población y muestra, técnica e instrumento, modalidad de aplicación (presencial, virtual, mixta), procedimiento y análisis de datos (software).
4. Si la metodología **no está guardada**, decírselo: la sección se puede hacer, pero sale menos precisa. Preguntarle solo lo mínimo, en un bloque: tamaño de la muestra, cómo va a recoger los datos y dónde.
5. Resumir en el chat, en cinco o seis líneas, lo que se va a usar: muestra, técnica, modalidad, lugar, periodo y software. Pedir que lo confirme antes de seguir.

## Paso 1 — La estructura que pide su universidad

Preguntar con `ask_user_input_v0`, en un solo bloque:

1. **Subtítulos de la sección:**
   - «Recursos y presupuesto · Financiamiento · Cronograma de ejecución» (tres subtítulos; la forma más común en Perú);
   - «Recursos · Presupuesto · Financiamiento · Cronograma» (cuatro subtítulos, recursos separados);
   - «Mi guía dice otra cosa (pego los subtítulos)»;
   - «Te ayudo a decidirlo con ejemplos sencillos».
2. **Número del capítulo:** IV (lo habitual cuando la metodología es el III), V, u «otro (lo escribo)».
3. **Códigos del clasificador de gastos:** «Mi guía los pide», «No los pide», «No sé».

Reglas:

- Si pega los subtítulos de su guía, **mandan ellos**, con su orden y su numeración, aunque falte alguna pieza. Si su guía no pide financiamiento, no se escribe.
- Si los **códigos del clasificador** se piden, se usan los del Clasificador de Gastos Públicos del MEF **vigente**, comprobados con `web_search` y `web_fetch` en la página del MEF antes de ponerlos. Nunca se escriben de memoria. Si no los pide o no sabe, la tabla va sin columna de código. Ver `references/rubros_y_costos.md`.
- Si dice «no sé» a todo, se usa la primera opción y el número IV, y se le dice que lo confirme con su asesor.

## Paso 2 — Recursos

Armar con el tesista la lista de recursos **a partir de la metodología**, no de una lista genérica. Usar la guía de `references/rubros_y_costos.md`, que dice qué recurso trae cada técnica y cada modalidad.

1. Proponer en el chat la lista en tres grupos:
   - **Humanos**: el investigador y el asesor siempre; solo si el estudio los necesita, encuestadores, transcriptor, estadístico o traductor. Ninguno se inventa: se pregunta.
   - **Materiales y equipos**: lo que se compra o se usa (impresiones del instrumento, útiles, laptop, grabadora).
   - **Servicios**: lo que se paga a terceros (internet, movilidad, fotocopias, empastado, plataforma de encuestas, transcripción).
2. Preguntar con `ask_user_input_v0` (selección múltiple) qué quita y qué falta.
3. **Lo que el tesista ya tiene** (su laptop, su celular) se lista como recurso disponible y no se presupuesta, salvo que su guía pida valorizarlo.
4. **El software libre** (R, Jamovi, QualCoder, Zotero, Mendeley) se lista con costo cero. Si la metodología nombra un software de pago (SPSS, ATLAS.ti), preguntar si tiene licencia por su universidad; si la tiene, también va con costo cero.

## Paso 3 — Presupuesto

1. Pedir los **precios** en un bloque, rubro por rubro, con cantidades ya propuestas desde la metodología. Ejemplos de cantidades que salen solas:
   - cuestionarios impresos = hojas del instrumento × (muestra + 10 %);
   - movilidad = número de visitas al lugar × costo por viaje de ida y vuelta (las visitas salen del procedimiento: permiso, piloto, aplicación);
   - internet = meses del cronograma × costo mensual, solo la parte que usa para el estudio si así lo quiere presentar.
2. Si no sabe un precio, proponer un **estimado razonable para su ciudad** y decir que es un estimado; entra en la tabla solo cuando el tesista lo acepta.
3. **Imprevistos**: preguntar si su guía los pide. Si sí, se agregan como una fila aparte con el porcentaje que diga la guía (suele estar entre el 5 y el 10 % del subtotal). Si la guía no dice nada, no se agregan.
4. Armar la tabla y mostrarla entera en el chat, con la operación de cada fila la primera vez (ver «Las cuentas, a la vista»). El formato está en `references/plantilla_capitulo.md`.
5. Pedir aprobación con `ask_user_input_v0`: «Está bien así», «Quiero cambiar cantidades o precios», «Quiero quitar o añadir un rubro».

Una tabla de presupuesto lleva como máximo **seis columnas**: código (solo si se pide), rubro o descripción, unidad, cantidad, costo unitario y total. Más columnas no caben en una página vertical.

## Paso 4 — Financiamiento

Preguntar con `ask_user_input_v0`:

- «Autofinanciado (lo pago yo)»;
- «Lo financia mi universidad o una institución (la nombro)»;
- «Fondo concursable o beca (lo nombro)»;
- «Mixto (una parte cada uno)».

Reglas:

- Se escribe **solo lo que el tesista dice**. Si nombra un fondo, beca o convenio, se escribe con el nombre que él da; si postuló pero aún no lo ganó, se escribe como postulación, no como financiamiento obtenido.
- Si es mixto, el párrafo dice cuánto pone cada parte y la suma tiene que dar el total del presupuesto.
- Un párrafo breve basta: quién financia, cuánto y, si aplica, qué cubre cada fuente.

## Paso 5 — Cronograma de ejecución

1. Preguntar en un bloque:
   - **cuándo empieza** (mes y año) y **cuándo tiene que sustentar o entregar**, si lo sabe;
   - **unidad**: meses (lo habitual) o semanas agrupadas por mes (solo si su guía lo pide así);
   - si el cronograma cubre **solo la ejecución** (desde la aprobación del proyecto) o **todo el proceso** (desde la elaboración del proyecto).
2. Proponer las actividades **a partir del método y de su metodología**, con la guía de `references/cronograma.md`: la validación del instrumento solo si la metodología la prevé, el piloto solo si lo dice el procedimiento, la codificación solo si es cualitativa.
3. Repartir las actividades en los meses y mostrar el Gantt en el chat. Comprobar antes de mostrarlo:
   - la **recolección de datos cae dentro del periodo** que dice la delimitación temporal; si no, se le avisa, porque es la observación más común del jurado;
   - ninguna actividad empieza antes de la que necesita (no se aplica el instrumento antes de validarlo, no se analiza antes de recoger);
   - entre la solicitud de permiso y la aplicación quedan al menos dos o tres semanas;
   - el último mes termina antes de la fecha de sustentación o entrega que dio.
4. **Columnas**: actividad más un máximo de **ocho periodos**. Si el proyecto dura más de ocho meses, se agrupa por bimestres o trimestres y se dice en la nota de la tabla. Un Gantt de doce columnas no cabe en una página vertical.
5. Pedir aprobación con `ask_user_input_v0`.

## Paso 6 — Redactar y guardar

1. Redactar la sección con la estructura del Paso 1 y el formato de `references/plantilla_capitulo.md`:
   - cada subtítulo abre con **uno o dos párrafos breves** que dicen qué muestra la tabla y lo esencial (el total, quién financia, cuántos meses dura), sin repetir la tabla fila por fila;
   - cada tabla se nombra en el texto antes de aparecer («La Tabla 3 detalla…»);
   - las tablas se numeran **siguiendo las del proyecto**: se cuentan las que ya tienen los capítulos guardados y se continúa desde ahí. Si no se puede saber, se empieza en la siguiente a la última que el tesista recuerde y se le avisa en el chat;
   - nada de viñetas en la prosa: las listas de recursos van en tabla o en un párrafo.
2. Las reglas de redacción y la voz del tesista las inyecta `redactar` en el primer tramo: se escribe siguiendo eso, sin imprimir auditorías de estilo en el chat.
3. Mostrar la sección completa en el chat y pedir aprobación.
4. **Guardar** con `guardar_capitulo`, clave `aspectos-administrativos`. Si el tesista corrige luego una tabla, se manda la sección entera otra vez, sin `anadir`.
5. Si la respuesta trae **AVISOS DE REDACCIÓN**, corregir esos párrafos con `reescribir_parrafos` (capítulo `aspectos-administrativos`). Las tablas no se tocan: esas herramientas no las reescriben.
6. Si `guardar_capitulo` falla, decir que **no se guardó** y por qué, y no seguir como si estuviera guardado.

## Paso 7 — Entregar y cerrar

1. Dar el enlace con `enlace_del_word`, como enlace que se pulsa, y decirle dónde va a encontrar la sección: después de la Metodología y antes de las Referencias.
2. Recordarle en el chat, en una o dos líneas:
   - qué montos son **estimados** y conviene confirmar (cotizar la imprenta, preguntar el costo del empastado en su ciudad);
   - que el cronograma depende de la fecha de aprobación del proyecto: si la aprobación se retrasa, se corre todo y basta con volver a esta skill para moverlo.
3. Explicarle que esta sección es **del proyecto**: cuando pase al informe final y ya tenga resultados guardados, el Word deja de imprimirla, salvo que la estructura de su facultad la nombre. Lo guardado no se borra.
4. Ofrecer el siguiente paso del método: si el proyecto está completo, la skill de Instrumento; si su asesor tiene que aprobar primero el proyecto, que lo lleve tal cual.
