---
name: informe-fase3-analisis-y-resultados
description: Cuarta fase de la Ruta del Informe de Acosta | IA & Research, para informes de curso y de empresa. Presenta e interpreta lo que se obtuvo, con las cifras calculadas en R y nunca de memoria. En un curso, los resultados del proyecto (antes y después, beneficios, lecciones), los datos del caso o la comparación de posturas. En una empresa, la tabla de indicadores con fórmula, meta, real y desvío; si el informe lo pide, la evaluación financiera (flujo de caja, VAN, TIR, recuperación, punto de equilibrio) con su tabla de supuestos y su sensibilidad, o la estimación de demanda y tamaño de mercado con el método escrito y la fuente de cada factor. Presenta tablas y figuras, distingue lo medido de lo proyectado, interpreta cada resultado frente a los objetivos o la decisión, guarda la sección y da el enlace del Word. ACTIVAR con "resultados de mi proyecto", "analiza los datos", "haz las tablas", "compara las posturas", "calcula los indicadores", "hazme el VAN y la TIR", "cuánto vale el mercado".
---

# Fase 3 — Análisis y resultados

## Para qué sirve esta skill

Es la cuarta fase de la **Ruta del Informe**: lo que se obtuvo y qué significa.

```
  Fase 0 · El encargo
  Fase 1 · Las fuentes y la evidencia
  Fase 2 · El desarrollo
  Fase 3 · Análisis y resultados           ← estás aquí
  Fase 4 · Cierre: conclusiones, recomendaciones y revisión
```

**Qué ámbito es:** si `mi_proyecto` dice «Ámbito: empresa», es de empresa; si no lo dice, es de
curso.

| Tipo | ¿Se usa esta fase? |
|---|---|
| Curso: proyecto | **Siempre** |
| Curso: análisis de caso | Si el caso trae datos para calcular |
| Curso: informe académico | Solo si la consigna pide comparar posturas o analizar datos |
| Empresa: gestión, factibilidad, estudio de mercado | **Siempre**: es el corazón del informe |
| Empresa: diagnóstico, auditoría, desempeño, clima, incidente | Casi siempre |
| Empresa: técnico o normativo sin mediciones | Se salta |

En empresa hay tres bloques, y se usan los que pida el tipo:

| Bloque | Cuándo | Referencia |
|---|---|---|
| **Indicadores** | Casi siempre | `references/indicadores_por_tipo.md` |
| **Financiero** | Factibilidad, plan de negocio, evaluación de una inversión | `references/financiero.md` |
| **Mercado** | Estudio de mercado y la parte de mercado de una factibilidad | `references/tamano_de_mercado.md` |

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un archivo de Word, un PDF ni ningún otro archivo del informe.** Las
tablas y figuras se escriben en Markdown dentro del texto que se guarda, y el Word del
servidor les da el formato.

```
1. mi_proyecto        al abrir (ficha, rúbrica o decisión, norma)
2. ver_capitulo       informe-fase2-desarrollo con texto: true
                      (objetivos o hallazgos); informe-fase0-encargo
3. trabajar_en_r      si hay datos: sin argumentos da el estado y el enlace
                      para que suba su archivo; con código corre R aquí
4. guardar_analisis   empresa: cada análisis, para releerlo con ver_analisis
5. guardar_capitulo   clave `informe-fase3-analisis-y-resultados`
6. revisar_evidencia  capitulo: informe-fase3-analisis-y-resultados
7. enlace_del_word    cuando quiera ver el documento
   analisis_cualitativo  si hay entrevistas o grupos focales (Paso 3)
```

**Citas por clave** (`[AR…]`, `[AR…:n]`, `[FALTA FUENTE]`), nunca escritas a mano. En empresa,
los datos internos van con su documento y su fecha de corte en la línea «Fuente:», y existen
`[FALTA DATO: …]` y `[POR CONFIRMAR CON LA EMPRESA: …]`. **Entre corchetes solo** esas marcas y
la de figura. **Si un guardado falla, se dice: no se guardó.** Detalle en
`references/integracion_zotero.md` (con `redactar`, `referencia: "integracion_zotero.md"`).

## Regla del acompañamiento

- **Un paso por turno.** Preguntas según `references/estilo_preguntas.md`.
- **Antes de correr algo, se pregunta.** Los datos son suyos.
- **Cada tabla se explica** en palabras sencillas antes de pasar a la siguiente.
- **Empresa: los supuestos se confirman con él, uno por uno.** Los va a defender en la reunión.

## Regla de oro: las cifras se trasladan y se calculan, no se producen

1. **Toda cifra sale de los datos o de una fuente con clave.** Nunca se estima, se redondea a
   conveniencia ni se completa.
2. **Ninguna cuenta mental.** Restas, porcentajes, promedios, variaciones y proyecciones pasan
   por `trabajar_en_r`. Si R no está disponible, se dice y no se calcula a mano. Solo se usan
   tal cual los cálculos que el estudiante trae hechos, diciendo de dónde salen.
3. **Sin medición, el resultado se describe sin números:** «el tiempo de atención bajó, según
   el encargado» y no «bajó un 30 %».
4. **Un resultado malo se reporta igual.** Un proyecto que no logró un objetivo lo dice; un
   flujo que da negativo se presenta negativo.
5. **Una proyección se presenta como proyección**, con sus supuestos a la vista, y **ningún
   supuesto se ajusta para que el resultado salga como querían.** Ese escenario se evalúa como
   escenario, en la sensibilidad.
6. **Un tamaño de mercado sin método escrito no se escribe.**
7. **«Significativo» solo con prueba estadística**, y **los puntos porcentuales no son
   porcentaje**: de 95 % a 81,3 % son 13,7 puntos, no 13,7 %.
8. **Si los datos tienen datos personales** (nombres, DNI, teléfonos, sueldos con nombre), se
   pide que los quite antes de subirlos. Los grupos de menos de cinco personas no se
   desagregan.

## Lo que esta skill NO hace

- **No repite el desarrollo.** Aquí va lo que se obtuvo, no lo que se hizo.
- **No escribe conclusiones ni recomendaciones.** Eso es la Fase 4.
- **No inventa datos** para completar una tabla.
- **No dictamina sobre estados financieros.** Eso es una auditoría externa.

## Paso 1 — Leer y decidir si toca

`mi_proyecto` y `ver_capitulo` de `informe-fase2-desarrollo` (`texto: true`, y `parte` si viene
partido) y de `informe-fase0-encargo`. En empresa, además, qué hallazgos del desarrollo hay que
cuantificar y cuál es la decisión del encargo.

Si el tipo es **informe de curso** y la consigna no pide análisis ni comparación:

```
Tu consigna no pide una sección de análisis. ¿Qué prefieres?
· Pasar directo al cierre (Fase 4)
· Agregar una comparación de posturas o fuentes igual
· No me queda claro, dame ejemplos
```

Si el desarrollo no está guardado, pedir que lo pegue o volver a la Fase 2.

## Paso 2 — Qué hay para presentar

Preguntar en una tanda qué tiene:

- **Proyecto:** mediciones antes y después, pruebas del producto, encuestas de satisfacción,
  registros (tiempos, ventas, fallas), fotos o capturas, comentarios del cliente o del docente.
- **Caso:** los datos numéricos del caso (estados financieros, ventas, encuestas).
- **Curso:** qué posturas o fuentes se van a comparar, o qué datos pide analizar la consigna.
- **Entrevistas o grupos focales**, en cualquier tipo: si están transcritos, se analizan con
  `analisis_cualitativo` (Paso 3).
- **Empresa:** los datos internos que llegaron en la Fase 1, revisados: periodo, fecha de
  corte, origen, si están completos. **Si la misma cifra aparece distinta en dos fuentes
  internas, se dice, se elige una y se escribe por qué.** Nunca se promedian.

Inventario en una tabla: qué dato, de dónde sale, si hay que calcular algo.

## Paso 3 — Calcular, si hay datos

1. `trabajar_en_r` sin argumentos: da el estado y el enlace para que suba su archivo (Excel o
   CSV).
2. Explicarle en una línea qué se va a calcular y **preguntar antes** de correrlo.
3. Correr el código con `trabajar_en_r` y **copiar las cifras tal como salen de la consola**.
   En empresa, cada análisis con `guardar_analisis`.
4. Para gráficos, guardarlos como imagen desde R y decirle el nombre del archivo: irá en la
   marca de figura.

**Si lo que hay son entrevistas o grupos focales** (a clientes, colaboradores, usuarios del
proyecto o expertos), no se resumen de memoria: se codifican con `analisis_cualitativo`.

1. Sin argumentos da el enlace para que cargue las transcripciones, una por archivo (Word, PDF
   con texto o .txt). En empresa, recordarle que quite los nombres de las personas si no tiene
   su permiso para citarlas.
2. Una entrevista a la vez: leerla entera con `accion: "ver"`, **proponerle** en el chat los
   códigos (nombre, definición, categoría) y las citas de cada uno, y guardar con
   `accion: "codificar"` **solo cuando lo apruebe**. Cada cita se copia tal cual del párrafo; si
   no es literal, el servidor la rechaza. Entre 5 y 12 códigos por entrevista, reutilizando los
   que ya están, y no más de 25 o 30 en total.
3. Con todo codificado: `accion: "tablas"` da la tabla de frecuencias y la de coocurrencia,
   que se pegan tal cual (solo se cambia la X por el número de tabla); `accion: "red"` dibuja
   la red de códigos, que va como figura con `red-de-codigos.png` en la marca y se incrusta sola
   en el Word.
4. En el Paso 7, un subtítulo por categoría, con dos o tres citas de participantes distintos
   entre comillas (E2, ¶8). **Antes de guardar**, pasar el texto por `accion: "capitulo"`: busca
   cada cita en las transcripciones y, si alguna no está, no lo arma y dice cuál.

Si el cálculo muestra algo que nadie esperaba —un mes con el doble, un cliente que es el 40 % de
las ventas—, **se le dice antes de escribirlo**: puede ser un hallazgo o un error de registro.

## Paso 4 — Indicadores (sobre todo empresa)

Con `references/indicadores_por_tipo.md`:

```
**Tabla 4**
*Indicadores de despacho, primer trimestre de 2026*
| Indicador | Meta | Real | Desvío |
|---|---|---|---|
| Órdenes despachadas a tiempo (%) | 95,0 | 81,3 | -13,7 pp |
| Tiempo de ciclo del pedido (h) | 24,0 | 38,5 | +14,5 h |
*Nota.* Despacho a tiempo = órdenes entregadas dentro del plazo / órdenes totales × 100.
*Fuente.* Sistema de despacho, corte al 31 de marzo de 2026.
```

- **Cada indicador con su fórmula escrita.**
- **Se compara contra algo declarado antes del periodo:** meta, periodo anterior, presupuesto
  o referencia del sector. Si no hay con qué, es la línea base. **No se inventa una meta.**
- **Los desvíos buenos también se explican.**

En un proyecto de curso sirve igual para el antes y después.

## Paso 5 — Lo financiero, si el informe lo pide (empresa)

Con `references/financiero.md`, y en este orden, que no se cambia:

1. **La tabla de supuestos**, primero: horizonte, tasa de descuento justificada, precio,
   costos, inversión con cotizaciones, capital de trabajo, impuesto, valor residual. **Cada uno
   con su origen**; lo que no se pueda respaldar, `[POR CONFIRMAR CON LA EMPRESA: …]`.
2. **El flujo de caja proyectado.** Si da negativo, se presenta negativo.
3. **VAN, TIR, periodo de recuperación y punto de equilibrio**, con la tasa al lado del VAN.
4. **La sensibilidad, obligatoria:** los dos o tres supuestos más pesados, movidos arriba y
   abajo, y **el punto de quiebre en prosa**. Ese párrafo se usa en el resumen ejecutivo.

## Paso 6 — El mercado, si el informe lo pide (empresa)

Con `references/tamano_de_mercado.md`:

1. **Delimitar** en tres cortes: producto, geografía y segmento.
2. **Los tres niveles:** total, atendible y objetivo, con el porcentaje del objetivo
   justificado.
3. **Calcular por los dos métodos** (de arriba abajo y de abajo arriba) y comparar.
4. **La muestra se describe en el cuerpo.** Una muestra no aleatoria no lleva margen de error.
5. **La intención declarada no es demanda.**

Si no hay con qué estimar, se dice y se trabaja contra la capacidad y el punto de equilibrio.

## Paso 7 — Presentar

Curso: guía en `references/resultados_informe.md`. Empresa: además
`references/tablas_y_figuras_empresa.md`. Reglas:

- **Un subtítulo por objetivo específico** (proyecto), por pregunta de análisis (caso, curso) o
  por bloque (indicadores, financiero, mercado), como subtítulo de Markdown de nivel 2.
- Cada tabla o figura: **se anuncia en el texto, se presenta y se interpreta** en dos o tres
  oraciones.
- Tablas y figuras en su bloque, como en la Fase 2: `**Tabla N**`, `*Título*`, la tabla,
  `*Nota.* …`; `**Figura N**`, `*Título*`, `[Insertar aquí la Figura N: archivo.png]`,
  `*Nota.* …`. **En empresa, además `*Fuente.* …` siempre**, y las proyecciones lo dicen.
- La numeración sigue la de la Fase 2: si allí hubo una Tabla 1, aquí empieza en la Tabla 2.
- **Los totales suman.** Se comprueba.
- En el **proyecto**, cierra con **beneficios** (para quién y cuánto, si se midió) y
  **lecciones aprendidas**.
- En la **comparación de posturas**, una tabla de coincidencias y diferencias, y un párrafo por
  cada diferencia importante con sus claves.

## Paso 8 — Interpretar

Por cada resultado, una interpretación corta:

- **Curso:** frente al objetivo: se logró, se logró en parte o no se logró, y por qué.
- **Empresa:** frente a **la decisión del encargo**: qué dice el número sin repetir la tabla,
  qué significa para esa decisión y qué lo explica, con el verbo que corresponda a la fuerza de
  la evidencia (`references/escribir_para_decidir.md`).

Si hay una fuente que ayuda a entenderlo, con su clave.

## Paso 9 — Auditoría anti-IA y de cifras

Con `references/anti_ia.md`, más:

```
AUDITORÍA DE RESULTADOS
Cifras en el texto: [N] · con origen en los datos o una clave: [N] (deben coincidir)
Cálculos hechos en R o traídos hechos con su origen: [N] · hechos a mano: 0
Tablas: [N] · figuras: [N] · todas anunciadas en el texto: SÍ / NO
Totales que no cuadran: 0
Objetivos sin resultado: [lista] (se dicen, no se ocultan)
Empresa: tablas sin «Fuente»: 0 · proyecciones marcadas: [N] de [N]
Empresa: supuestos con origen: [N] de [N] · sensibilidad hecha: SÍ / NO / no aplica
Empresa: método del tamaño de mercado escrito: SÍ / NO / no aplica
Puntos porcentuales bien usados · «significativo» sin prueba: 0
Patrones P0 a P14 (y E1 a E4 en empresa): [PASA / MARCÓ]
Estado: OK PARA GUARDAR / RE-REDACTAR
```

Si una sola línea de cifras marca, **no se guarda**: se corrige.

## Paso 10 — Guardar y entregar

1. `guardar_capitulo` con clave `informe-fase3-analisis-y-resultados`. Markdown limpio, **sin
   el título «Análisis y resultados»** (lo pone el Word), sin referencias. Por partes con
   `anadir: true` si pasa de 30.000 caracteres.
2. `revisar_evidencia` con `capitulo: informe-fase3-analisis-y-resultados`.
3. `guardar_avance` (`capitulo: informe-fase3-analisis-y-resultados`): `resumen` con los
   resultados principales en dos o tres frases y, en empresa, los supuestos que decidieron el
   resultado.
4. `enlace_del_word`, y decirle qué imagen va en cada marca de figura.

## Paso 11 — Cierre

- [ ] ¿Cada objetivo o hallazgo tiene su resultado, aunque sea «no se logró»?
- [ ] ¿Cada cifra sale de los datos, de R o de una fuente con clave?
- [ ] ¿Cada tabla y figura está anunciada e interpretada?
- [ ] ¿Sabe qué imagen pegar en cada marca?
- [ ] Empresa: ¿sabe qué supuesto o qué indicador decide el resultado? Es lo primero que le van
      a preguntar.

Siguiente: **Fase 4**, el cierre.

## Errores que esta skill previene

1. Cifras redondeadas «para que se vean mejor».
2. Un proyecto que dice que todo salió bien sin pruebas.
3. Tablas pegadas sin explicar qué muestran.
4. Repetir en resultados lo que ya se contó en el desarrollo.
5. Subir datos con nombres y DNI de los encuestados.
6. Figuras numeradas de nuevo desde 1 después de la Fase 2.
7. Empresa: un VAN o un porcentaje calculado de memoria.
8. Empresa: un total que no suma, que hunde la credibilidad del informe entero.
9. Empresa: un tamaño de mercado inventado con el que alguien pide un préstamo.
10. Empresa: una proyección presentada como dato, o ajustada hasta que salga viable.
11. Empresa: confundir puntos porcentuales con porcentaje.

## Archivos de referencia

- `references/estilo_preguntas.md` — Cómo se pregunta en esta ruta, según el ámbito.
- `references/integracion_zotero.md` — Claves, norma de citas y cómo se cita un dato interno.
- `references/resultados_informe.md` — Curso: cómo presentar resultados, tablas y figuras.
- `references/indicadores_por_tipo.md` — Los indicadores habituales con su fórmula, y cómo se comparan.
- `references/financiero.md` — Empresa: supuestos, flujo de caja, VAN, TIR, punto de equilibrio y sensibilidad.
- `references/tamano_de_mercado.md` — Empresa: delimitar el mercado, los dos métodos y la muestra.
- `references/tablas_y_figuras_empresa.md` — Empresa: la línea «Fuente» y los gráficos que no se hacen.
- `references/escribir_para_decidir.md` — Los verbos de la causa según la fuerza de la evidencia.
- `references/anti_ia.md` — Auditoría de patrones de IA.
