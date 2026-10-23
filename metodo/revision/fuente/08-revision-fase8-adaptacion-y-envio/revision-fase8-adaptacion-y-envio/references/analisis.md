# De dónde salen las cifras

Ninguna cifra del artículo se calcula "de cabeza" ni se estima. Sale de una de
estas tres vías, y en el texto se declara cuál (software y versión en Métodos).

| Vía | Cuándo | Qué se toma |
|---|---|---|
| **A. Servidor Acosta** (`trabajar_en_r`) | Si la herramienta está conectada. Preferente | La consola de R de esta sesión |
| B. Skill `analisis-datos-rstudio` | Si el investigador ya la usó | **Solo** sus tablas y salidas; su redacción por objetivos es de tesis y no se copia |
| C. Salidas propias | SPSS, SmartPLS, JASP, AMOS, Excel, R | Las tablas tal como vienen |

**Formatear no es recalcular.** Se permite y se declara: redondear a dos
decimales (tres para *p*), quitar el cero inicial donde el estilo lo pida,
escribir *p* < .001. No se permite: recalcular, "corregir" una cifra que no
cuadra o completar una celda vacía. Si algo no cuadra, se pregunta.

## Vía A: el servidor (probado en R 4.6.1, octubre de 2026)

Reglas del servidor que hay que respetar:

- Sin conexión a internet desde R: el corpus o la base **los sube el
  investigador** por el enlace que da la herramienta. El enlace se le entrega
  tal cual, como enlace pulsable.
- No imprimir la base ni filas enteras (datos personales).
- Las cifras que vayan al texto se dejan en una tabla de la sesión y se
  descargan (`escribir_csv(tabla, "resultados.csv")` + opción `descargar`).
  `guardar_analisis` es del flujo de tesis: con claves de artículo el servidor
  la rechaza; no se usa.
- Disponibles: tidyverse, psych, lavaan, semTools, seminr, effectsize,
  bibliometrix, flextable, officer. **No** está `PRISMA2020`.

## Revisión bibliométrica y metaanálisis

Código probado (bibliometrix, Bradford manual, Lotka, kappa, metafor) y orden
de reporte en `references/revision.md`.
