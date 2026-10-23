# El desarrollo según el tipo de informe

El cuerpo del informe. Cambia entero según el tipo, pero **el ladrillo es siempre el mismo**:
el hallazgo de cinco piezas de `escribir_para_decidir.md`.

Lo que **no** va en el desarrollo, en ningún tipo:

- las cifras calculadas y los indicadores: van en la Fase 3;
- las conclusiones y las recomendaciones: van en la Fase 4;
- el resumen ejecutivo y la introducción: van en la Fase 4.

---

## Diagnóstico / consultoría

| Sección | Qué lleva | De dónde sale |
|---|---|---|
| La empresa y su contexto | Qué hace, tamaño, mercado, y **qué área se analizó**. Media página: no es la historia de la empresa | Él + memoria o web de la empresa |
| Situación actual | Cómo funciona hoy el proceso, paso por paso, con volúmenes y tiempos. Un mapa o una tabla del proceso ayuda | Datos internos + lo que él observó |
| Hallazgos | **Numerados y ordenados por impacto.** Cada uno con las cinco piezas | Datos + entrevistas + observación |
| Análisis de causas | La herramienta que aplique, llena con los datos del informe | `herramientas_de_analisis.md` |
| Brecha con el sector | Dónde está la empresa frente a la referencia, si hay dato para comparar | Fuentes externas |

Reglas:

- **Los hallazgos se ordenan por lo que cuestan**, no por el orden en que aparecieron.
- **La situación actual describe, no juzga.** El juicio es el hallazgo.
- **Cada hallazgo se puede rastrear a una evidencia**, y cada recomendación de la Fase 4 se
  puede rastrear a un hallazgo. Si un hallazgo no lleva a ninguna recomendación, se revisa si
  vale la pena tenerlo.
- Entre tres y ocho hallazgos. Con quince, ninguno se ejecuta.

## Gestión / resultados

| Sección | Qué lleva |
|---|---|
| Lo que se hizo en el periodo | Actividades e hitos. **Breve**: media página. Quien lo lee quiere los resultados |
| Resultados frente a la meta | La tabla de indicadores: meta, real, desvío. El detalle va en la Fase 3 |
| Análisis de los desvíos | Uno por uno, los que se desviaron: por qué, con el dato |
| Lo que no se cumplió | Qué quedó pendiente y qué lo bloqueó, sin excusas genéricas |

Reglas:

- **Se compara contra algo declarado antes del periodo**: la meta, el periodo anterior o el
  presupuesto. Una meta puesta después no es meta, y si es el caso, se dice.
- **Los desvíos buenos también se explican.** Superar la meta en 40 % significa que la meta
  estaba mal o que pasó algo: las dos cosas hay que decirlas.
- **No se infla.** Si el trimestre fue normal, el informe es corto y eso es una virtud.

## Factibilidad / plan de negocio

| Sección | Qué lleva | Cuidado con |
|---|---|---|
| La oportunidad | Qué problema o necesidad atiende, con el dato que lo muestra | No es un discurso de venta |
| El negocio propuesto | Qué se vende, a quién, cómo se entrega, qué lo diferencia | Diferenciarse «por la calidad» no es diferenciarse |
| Mercado | Demanda, oferta, competencia y precios. El cálculo del tamaño, en la Fase 3 | La cifra de tamaño sin método |
| Técnico y operativo | Qué se necesita: local, equipos, personal, capacidad, proceso | Capacidad que nadie calculó |
| Organización y legal | Estructura, personal y su costo, permisos con su plazo, régimen tributario | Permisos que tardan meses y no están en el cronograma |
| Inversión y financiamiento | En qué se invierte, cuánto, **con cotización**, y de dónde sale el dinero con su tasa real | Precios estimados en lugar de cotizaciones |

Reglas:

- **La inversión va con cotizaciones con fecha y proveedor.** «Unos S/ 80 000 en equipos» no
  sostiene una decisión de inversión.
- **Los permisos con su plazo real.** Un proyecto que arranca en el mes 1 del cronograma y
  necesita una licencia que tarda cinco meses está mal planteado, y el informe lo dice.
- **No se promete el resultado.** El informe concluye lo que salga del flujo de la Fase 3.

## Estudio de mercado

| Sección | Qué lleva | Cuidado con |
|---|---|---|
| El mercado | Cómo se delimita: geografía, segmento, producto. Y su tamaño | Un mercado «nacional» cuando el negocio atiende un distrito |
| La demanda | Quién compra, cuánto, con qué frecuencia, qué valora, cuánto paga | Confundir lo que dicen que pagarían con lo que pagan |
| Oferta y competencia | Quiénes son, qué ofrecen, a qué precio, qué participación tienen | Participaciones inventadas |
| Precios | Los del mercado, con su fuente, y el histórico si lo hay | Precios «de oferta» presentados como de transacción |
| Canales | Cómo llega el producto al cliente hoy, y qué cuesta cada canal | — |

Reglas:

- **La intención de compra declarada no es demanda.** Se escribe así: «el 62 % de los
  encuestados dijo que compraría; la conversión real en este tipo de producto suele ser
  menor, y el informe usa el rango bajo para proyectar».
- **La muestra se describe siempre**: cuántos, de cuántos, cómo se eligieron, cuándo y dónde.
- **La competencia se verifica**, no se reproduce lo que el cliente cree.

---

## Los otros ocho

### Informe técnico

Antecedentes · la situación, la falla o el requerimiento, con sus mediciones · los criterios
técnicos y las normas que aplican, **con número y año** · las alternativas evaluadas en una
tabla comparativa (cumple o no cumple cada criterio, costo, plazo, vida útil) · la
recomendada, con su especificación.

Regla: **la comparación de alternativas se hace contra criterios declarados antes**, no
después de haber elegido.

### Auditoría interna o cumplimiento

Objetivo y alcance · **el criterio**: contra qué se audita, con su versión vigente · qué se
revisó y cómo, con el universo y la muestra · **los hallazgos, uno por uno**, cada uno con las
cinco piezas de auditoría:

```
CONDICIÓN  Lo que se encontró, con la evidencia y su referencia.
CRITERIO   Lo que debía ser, citando la norma, política o cláusula.
CAUSA      Por qué ocurrió.
EFECTO     Qué riesgo o pérdida genera, medido si se puede.
RECOMEND.  Qué corregir. (El plan de acción va en la Fase 4.)
```

Reglas duras:

- **Ningún hallazgo sin su criterio escrito.** Sin criterio es una opinión.
- **La muestra se declara**: de cuántas operaciones, cuántas se revisaron y cómo se eligieron.
  Un porcentaje de incumplimiento sobre una muestra elegida a dedo no se puede extrapolar, y
  el informe lo dice.
- **Se escribe contra el proceso, no contra la persona**, salvo que el encargo pidiera
  responsables identificados.
- **Esto no es un dictamen de auditoría externa.** Si lo que piden es eso, la Fase 0 ya lo
  dijo.

### Informe de avance de proyecto

Estado general (verde, ámbar, rojo, con el criterio de cada color) · alcance: qué se entregó y
qué no · cronograma contra la línea base, **con el desvío en días** · costo contra el
presupuesto, con el desvío en soles y en porcentaje · riesgos e incidencias, con responsable
y estado · qué se hará en el siguiente periodo · **las decisiones que se le piden al
patrocinador**, numeradas.

Regla: es el informe donde más se maquilla. Un semáforo verde con el cronograma dos semanas
atrasado no es verde, y el criterio del color va escrito para que no se discuta.

### Informe de incidente o *postmortem*

Qué pasó, en una frase · **línea de tiempo con horas**: detección, escalamiento, contención,
solución · impacto medido: clientes, soles, horas de parada, datos afectados · qué lo contuvo
· **causa raíz** con los cinco por qués · qué falló en la detección (por qué no se vio antes)
· acciones correctivas, en la Fase 4.

Reglas: **contra el proceso, no contra la persona.** Y la línea de tiempo se construye con
registros —bitácoras, tickets, mensajes—, no con recuerdos; lo que venga de un recuerdo se
dice así.

### Sostenibilidad o ESG

El estándar que se sigue, **con su versión** · alcance, periodo y límites de la información ·
los grupos de interés y cómo se los consultó · los temas materiales y cómo se determinaron ·
los indicadores del estándar, cada uno con su cifra y **su método de cálculo** · metas y
avance.

Regla: **no se declara conformidad con un estándar que no se cumple entero.** Se dice qué
indicadores se reportan y cuáles no, y por qué.

### *Due diligence* comercial

Alcance y **qué no se revisó** (lo contable y lo legal van aparte, y se dice) · el negocio
objetivo · mercado y posición competitiva · clientes: concentración, contratos, rotación ·
ingresos: calidad, recurrencia, estacionalidad · el plan del vendedor, **contrastado con la
evidencia** · banderas rojas.

Regla: cada afirmación lleva su grado de firmeza, porque con esto se decide una compra:
verificado con documento, declarado por el vendedor sin verificar, o estimado.

### Desempeño de un área o de un proceso

Qué hace el área y con qué recursos · los indicadores del proceso, **con su fórmula escrita**
· resultado frente a la meta o al periodo anterior · cuellos de botella, con el dato que los
muestra · comparación con la referencia, si la hay.

### Clima laboral o satisfacción de clientes

Objetivo y qué se midió · el instrumento: qué se preguntó y por qué · **la muestra y la tasa
de respuesta** · resultados por dimensión · comparación con la medición anterior · lo que
dijeron en las preguntas abiertas, agrupado por tema y con citas textuales cortas y anónimas.

Reglas: **la tasa de respuesta va siempre** —un 18 % no representa a nadie y hay que decirlo—
y **los grupos de menos de cinco personas no se desagregan**, porque dejan de ser anónimos.

---

## Extensión orientativa del desarrollo

| Informe total | Desarrollo |
|---|---|
| 10 páginas | 4 a 6 |
| 20 páginas | 9 a 13 |
| 40 páginas | 18 a 25 |
| 60 páginas | 25 a 35 |

El resto se lo llevan el resumen ejecutivo, la introducción, el análisis de la Fase 3 y el
cierre de la Fase 4. Una página son unas 350 palabras, sin contar tablas.

## Lo que se le pregunta antes de redactar, en cada tipo

Lo que no está en ningún dato y sin lo cual el informe queda hueco:

| Tipo | Qué solo sabe él |
|---|---|
| Diagnóstico | Qué vio en la empresa, a quién entrevistó y qué le dijeron, qué le llamó la atención |
| Gestión | Por qué se desvió cada indicador, qué pasó en el periodo que no está en los números |
| Factibilidad | Por qué eligió esta solución y no otra, qué cotizó y con quién habló |
| Estudio de mercado | Cómo hizo el campo, qué le dijeron los clientes, qué observó en la competencia |
| Técnico | Qué probó, qué midió, qué descartó y por qué |
| Auditoría | Qué revisó, cómo eligió la muestra, qué le respondieron los responsables |
| Avance | Qué está bloqueando de verdad el proyecto |
| Incidente | Qué pasó minuto a minuto y quién se dio cuenta de qué |

**Si trae poco, se le repregunta lo concreto que falta. No se rellena.**
