# La evaluación financiera de un proyecto

Es la parte del informe con la que se decide invertir dinero. Y es donde una cifra inventada
hace el daño más grande de toda la plataforma.

**Todo se calcula con `trabajar_en_r` y se guarda con `guardar_analisis`.** Ni un VAN de
memoria, ni una TIR aproximada, ni un flujo redondeado a ojo.

## La tabla de supuestos: primero y obligatoria

Antes del flujo. Sin ella, el flujo no significa nada, porque nadie sabe de dónde salió cada
número.

```
**Tabla 6**
*Supuestos de la evaluación*
| Supuesto | Valor | De dónde sale |
|---|---|---|
| Horizonte de evaluación | 5 años | Vida útil del equipo principal, según la cotización |
| Tasa de descuento | 14 % anual | Costo del préstamo ofrecido por el banco (12 %) más 2 pp de prima |
| Precio de venta unitario | S/ 38 | Precio actual de la empresa, marzo de 2026 |
| Crecimiento de la demanda | 4 % anual | Crecimiento del sector 2021-2025 [AR…] |
| Costo variable unitario | S/ 22,50 | Estructura de costos de la empresa, 2025 |
| Costos fijos anuales | S/ 186 000 | Planilla y alquiler cotizados |
| Inversión inicial | S/ 420 000 | Cotizaciones de marzo de 2026 (Anexo 4) |
| Capital de trabajo | S/ 45 000 | 30 días de costo operativo |
| Impuesto a la renta | 29,5 % | Régimen general vigente |
| Valor residual | S/ 60 000 | 15 % de la inversión en equipos |
*Fuente.* Elaboración propia. El detalle del cálculo está en el Anexo 5.
```

Reglas de la tabla:

- **Cada supuesto con su origen.** «Estimado» no es un origen. Si el origen es lo que él cree,
  se escribe: «estimación del área comercial, sin registro histórico».
- **Un supuesto que nadie pudo respaldar va marcado** `[POR CONFIRMAR CON LA EMPRESA: …]`.
- **La tasa de descuento se justifica.** Es el número que más mueve el VAN y el que más se
  pone «porque sí». Si no hay forma de justificarla, se evalúa con tres tasas y se dice.

## El flujo de caja

```
**Tabla 7**
*Flujo de caja proyectado (S/)*
| Concepto | Año 0 | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |
|---|---|---|---|---|---|---|
| Ingresos | — | 456 000 | 474 240 | 493 210 | 512 938 | 533 456 |
| Costos variables | — | -270 000 | -280 800 | -292 032 | -303 713 | -315 862 |
| Costos fijos | — | -186 000 | -186 000 | -186 000 | -186 000 | -186 000 |
| Depreciación | — | -72 000 | -72 000 | -72 000 | -72 000 | -72 000 |
| Utilidad antes de impuestos | — | -72 000 | -64 560 | -56 822 | -48 775 | -40 406 |
| Impuesto | — | 0 | 0 | 0 | 0 | 0 |
| Depreciación (se devuelve) | — | 72 000 | 72 000 | 72 000 | 72 000 | 72 000 |
| Inversión | -420 000 | — | — | — | — | — |
| Capital de trabajo | -45 000 | — | — | — | — | 45 000 |
| Valor residual | — | — | — | — | — | 60 000 |
| **Flujo neto** | **-465 000** | **0** | **7 440** | **15 178** | **23 225** | **136 594** |
*Fuente.* Proyección propia. Supuestos en la Tabla 6.
```

Lo que hay que cuidar:

- **La línea de fuente dice «proyección».** Es la salvedad que más se olvida.
- **La depreciación entra para el impuesto y sale del flujo:** no es una salida de caja.
- **El capital de trabajo se recupera** al final del horizonte.
- **Los años sin utilidad no pagan impuesto**, y si hay pérdida arrastrable, se dice.
- **Si el flujo da negativo, se presenta negativo.** No se ajusta un supuesto para que salga.

## VAN, TIR y lo demás

| Indicador | Qué es | Cómo se lee |
|---|---|---|
| **VAN** | Valor presente de los flujos, descontados a la tasa, menos la inversión | Positivo: conviene a esa tasa. Negativo: no conviene |
| **TIR** | La tasa a la que el VAN es cero | Se compara con la tasa de descuento. Por debajo, no conviene |
| **Periodo de recuperación** | En cuántos años se recupera la inversión | Mejor descontado que simple; se dice cuál se usó |
| **Punto de equilibrio** | Costos fijos / (precio − costo variable unitario) | En unidades y en soles, y cuánto es frente a la capacidad |
| **Relación beneficio-costo** | Valor presente de los ingresos / valor presente de los costos | Mayor que 1: conviene |

Y cómo se presentan:

```
**Tabla 8**
*Resultado de la evaluación*
| Indicador | Resultado | Criterio |
|---|---|---|
| VAN (tasa 14 %) | S/ -52 340 | Negativo: no conviene a esa tasa |
| TIR | 9,8 % | Por debajo del 14 % exigido |
| Periodo de recuperación descontado | No se recupera en 5 años | — |
| Punto de equilibrio | 11 990 unidades al año | 78 % de la capacidad instalada |
*Fuente.* Elaboración propia con el flujo de la Tabla 7.
```

Tres cosas que no se hacen:

- **No se calcula la TIR de un flujo que cambia de signo varias veces** sin advertirlo: puede
  tener más de una solución, y entonces la TIR no sirve para decidir. Se usa el VAN.
- **No se compara la TIR con la inflación** ni con «lo que rinde el banco»: se compara con la
  tasa de descuento del proyecto.
- **No se presenta un VAN sin decir a qué tasa.** Un VAN sin tasa no es un número.

## La sensibilidad: obligatoria, no opcional

Un flujo proyectado es un conjunto de supuestos. La sensibilidad dice **cuál de ellos decide
el resultado**, que es lo que el gerente o el banco realmente quieren saber.

Lo mínimo: los dos o tres supuestos más pesados, movidos hacia abajo y hacia arriba.

```
**Tabla 9**
*Sensibilidad del VAN (S/)*
| Escenario | VAN | ¿Conviene? |
|---|---|---|
| Base | -52 340 | No |
| Precio -10 % | -238 100 | No |
| Precio +10 % | 133 420 | Sí |
| Demanda -15 % | -186 750 | No |
| Costo variable +10 % | -165 200 | No |
| Tasa de descuento 10 % | 8 940 | Sí, al límite |
*Fuente.* Elaboración propia. Un supuesto por escenario; los demás en su valor base.
```

Y el párrafo que la acompaña dice **el punto de quiebre**:

> El resultado depende sobre todo del precio: el proyecto alcanza un VAN positivo a partir de
> S/ 40,20 por unidad, un 5,8 % por encima del precio actual. Con el precio de hoy no conviene
> a una tasa del 14 %, y sí conviene si el financiamiento baja al 10 %.

Ese párrafo es el que se usa en el resumen ejecutivo.

## Cómo se concluye

**La conclusión es binaria y va arriba**, en una de estas tres formas:

1. **Conviene.** «El proyecto es viable: VAN de S/ 133 000 a una tasa del 14 % y TIR del
   21,4 %.»
2. **No conviene.** «El proyecto no es viable a las condiciones actuales: VAN negativo de
   S/ 52 340 y TIR del 9,8 %, por debajo del 14 % exigido.»
3. **Conviene si.** «El proyecto es viable solo si se consigue financiamiento por debajo del
   11 % o el precio sube al menos 6 %. A las condiciones actuales, no.»

Un estudio de factibilidad que no concluye no sirve para nada. Y **la tercera forma es la más
frecuente y la más útil**: dice qué hay que negociar.

## Lo que nunca se hace

- **Ajustar un supuesto para que el VAN salga positivo.** Si el cliente lo pide, se le dice
  que se puede evaluar ese escenario **como escenario**, en la tabla de sensibilidad, y que el
  caso base se queda con los supuestos respaldados.
- **Inventar un flujo cuando no hay datos.** Sin precio, sin costo variable o sin demanda no
  hay evaluación financiera. Se dice qué falta y se ofrece el punto de equilibrio, que necesita
  menos datos.
- **Redondear hacia arriba.** Ni los ingresos ni el valor residual.
- **Proyectar diez años** cuando la empresa no tiene tres de historia. El horizonte se
  justifica.
- **Mezclar soles y dólares** en la misma tabla sin decir el tipo de cambio y su fecha.
- **Presentar la proyección como dato.** Siempre «proyección propia» en la línea de fuente.
