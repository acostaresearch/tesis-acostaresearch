# Indicadores: los habituales, con su fórmula

Un indicador sin fórmula escrita no se puede reproducir, y lo primero que hace quien recibe el
informe es querer reproducirlo. **Cada indicador del informe lleva su fórmula**, en la tabla o
en una nota.

## Las cuatro reglas

1. **La fórmula va escrita.** «Rotación de personal: salidas del periodo / dotación promedio
   del periodo × 100».
2. **El periodo y la unidad van con el número.** «14,2 % (enero a marzo de 2026)».
3. **Se compara contra algo declarado:** la meta, el periodo anterior, el presupuesto o la
   referencia del sector. Un indicador solo no dice nada.
4. **Se calcula, no se estima.** Todo por `trabajar_en_r`, incluidas las restas y los
   porcentajes. Una cuenta mental en un informe es un error esperando salir.

## Cómo se presenta la tabla

```
**Tabla 4**
*Indicadores de despacho, primer trimestre de 2026*
| Indicador | Meta | Real | Desvío |
|---|---|---|---|
| Órdenes despachadas a tiempo (%) | 95,0 | 81,3 | -13,7 pp |
| Tiempo de ciclo del pedido (h) | 24,0 | 38,5 | +14,5 h |
| Costo por orden (S/) | 12,00 | 15,40 | +28,3 % |
*Nota.* Despacho a tiempo = órdenes entregadas dentro del plazo comprometido / órdenes
totales × 100. Tiempo de ciclo = horas entre la confirmación del pedido y la salida del
vehículo.
*Fuente.* Sistema de despacho, corte al 31 de marzo de 2026.
```

**Los puntos porcentuales no son porcentaje.** De 95 % a 81,3 % la caída es de 13,7 **puntos
porcentuales**, no de 13,7 %. Confundirlos es el error de cifras más común de esta ruta.

## Los habituales por tipo de informe

### Operaciones y logística

| Indicador | Fórmula |
|---|---|
| Cumplimiento de entregas | Entregas dentro del plazo / entregas totales × 100 |
| Tiempo de ciclo | Tiempo entre el inicio y el fin del proceso, promedio |
| Exactitud de inventario | Unidades contadas que coinciden / unidades contadas × 100 |
| Rotación de inventario | Costo de ventas del periodo / inventario promedio |
| Días de inventario | 365 / rotación de inventario |
| Productividad | Unidades procesadas / horas-hombre |
| Costo unitario del proceso | Costo total del proceso / unidades procesadas |
| Nivel de servicio | Pedidos atendidos completos / pedidos recibidos × 100 |

### Comercial

| Indicador | Fórmula |
|---|---|
| Crecimiento de ventas | (Ventas del periodo − del periodo base) / del periodo base × 100 |
| Ticket promedio | Ventas / número de transacciones |
| Concentración de clientes | Ventas de los N mayores clientes / ventas totales × 100 |
| Tasa de conversión | Cierres / oportunidades × 100 |
| Retención de clientes | Clientes del periodo que ya eran del anterior / clientes del anterior × 100 |
| Margen bruto | (Ventas − costo de ventas) / ventas × 100 |

**Cuidado con el crecimiento:** si el periodo base es chico, el porcentaje engaña. Se pone
también la cifra absoluta.

### Financieros

| Indicador | Fórmula |
|---|---|
| Margen operativo | Utilidad operativa / ventas × 100 |
| Margen neto | Utilidad neta / ventas × 100 |
| Liquidez corriente | Activo corriente / pasivo corriente |
| Endeudamiento | Pasivo total / activo total × 100 |
| Periodo de cobro | Cuentas por cobrar / ventas × días del periodo |
| Periodo de pago | Cuentas por pagar / compras × días del periodo |
| Rentabilidad del activo | Utilidad neta / activo total × 100 |
| Punto de equilibrio | Costos fijos / (precio − costo variable unitario) |

**No se calculan sobre estados financieros que no se tienen.** Si solo llegó el estado de
resultados, no hay liquidez ni endeudamiento, y eso va en las limitaciones.

### Personas

| Indicador | Fórmula |
|---|---|
| Rotación | Salidas del periodo / dotación promedio × 100 |
| Ausentismo | Horas no trabajadas / horas programadas × 100 |
| Horas extra | Horas extra / horas ordinarias × 100 |
| Costo por trabajador | Costo total de personal / dotación promedio |
| Cobertura de capacitación | Trabajadores capacitados / dotación × 100 |

**Los indicadores de personas no se desagregan en grupos de menos de cinco**: dejan de ser
anónimos.

### Calidad y servicio

| Indicador | Fórmula |
|---|---|
| Tasa de defectos | Unidades defectuosas / unidades producidas × 100 |
| Reclamos | Reclamos recibidos / transacciones × 100 (o por cada 1 000) |
| Tiempo de respuesta | Horas entre la recepción y la solución, promedio |
| Reproceso | Unidades reprocesadas / unidades producidas × 100 |
| Satisfacción | Promedio de la escala, **con la escala escrita** y la tasa de respuesta |

### Proyectos

| Indicador | Fórmula |
|---|---|
| Avance físico | Entregables completados / entregables planificados × 100 |
| Desvío de cronograma | Días de atraso frente a la línea base |
| Desvío de costo | (Costo real − presupuestado) / presupuestado × 100 |
| Índice de desempeño del costo | Valor ganado / costo real |
| Riesgos abiertos | Riesgos sin mitigación / riesgos identificados |

### Cumplimiento y auditoría

| Indicador | Fórmula |
|---|---|
| Tasa de incumplimiento | Casos que incumplen / casos revisados × 100 |
| Cobertura de la revisión | Casos revisados / universo × 100 |
| Hallazgos por nivel de riesgo | Conteo, en tabla |
| Hallazgos anteriores corregidos | Corregidos / hallazgos de la revisión previa × 100 |

**La tasa de incumplimiento solo se extrapola si la muestra fue aleatoria.** Si se eligió a
dedo, se dice: «de los 30 casos revisados, 11 incumplen; la muestra no fue aleatoria, así que
esta proporción no se puede llevar al universo».

## Cuando no hay con qué comparar

Es frecuente: la empresa nunca midió eso. Tres salidas, en orden:

1. **El periodo anterior**, aunque haya que calcularlo ahora con los mismos datos.
2. **La referencia del sector**, si hay una fuente externa que la publique.
3. **Dejarlo como línea base:** «este es el primer registro del indicador; sirve como punto de
   partida para medir la mejora». Es una respuesta perfectamente válida y honesta.

Lo que no se hace es **inventar una meta** para que el indicador tenga con qué compararse.

## Cómo se interpreta un indicador

Tres oraciones, no más:

1. **Qué dice el número**, sin repetir la tabla: «el cumplimiento está 13,7 puntos por debajo
   de la meta».
2. **Qué significa para la decisión:** «una de cada cinco órdenes llega tarde, y los reclamos
   del trimestre se concentran en esas».
3. **Qué lo explica**, con el verbo que corresponda a la fuerza de la evidencia.

Lo que no se hace: decir que un resultado es «significativo» sin prueba estadística, ni
«preocupante» sin decir para qué.
