# Los datos internos: qué pedir y en qué formato

Es lo que sostiene un informe de empresa. Y es donde se pierde el tiempo: se piden mal, llegan
resumidos, y en la Fase 3 no se pueden recalcular.

## La regla del formato

**Se pide el dato detallado, no el reporte ya resumido.**

| Se pide | No se pide |
|---|---|
| Hoja de cálculo con **una fila por transacción** (venta, orden, ticket, registro) | Un PDF con el total del mes |
| Todas las columnas que trae el sistema | Las tres columnas que él cree que hacen falta |
| El periodo completo, con los meses de comparación | Solo el mes del problema |
| La exportación cruda del sistema | Una tabla que él copió a mano |

Por qué: un total no se puede abrir. Con el detalle se puede ver la concentración, la
estacionalidad, los casos raros y los errores de registro, y **eso es la mitad de los
hallazgos de un informe**. Con el resumen solo se puede repetir lo que ya sabían.

Cómo se le dice, en una línea:

> Mejor mándame la exportación del sistema tal como sale, aunque tenga columnas de más. Si me
> mandas el reporte ya sumado, no puedo abrirlo para buscar dónde se concentra el problema.

## Qué pedir según el tipo de informe

### Diagnóstico de un área o proceso

| Dato | Para qué |
|---|---|
| Las transacciones del proceso, 12 meses, una fila cada una | Volumen, estacionalidad, tiempos, casos raros |
| El procedimiento escrito, si existe | Comparar lo que se hace con lo que debía hacerse |
| Dotación del área: cuántos, en qué turno, con qué costo por hora | Cuantificar el sobrecosto en soles |
| Reclamos o incidencias del periodo | El efecto en el cliente |
| Los indicadores que ya miden, con su fórmula | No reinventar lo que ya existe |
| Organigrama del área | Quién decide qué |

### Gestión / resultados

Las metas del periodo, escritas y de antes de empezar (una meta puesta después no es meta) ·
el resultado de cada indicador, con su fórmula · el periodo anterior y el mismo periodo del
año anterior · el presupuesto contra el ejecutado · los hitos y actividades del periodo.

### Factibilidad / plan de negocio

Cotizaciones de la inversión (no precios estimados: cotizaciones con fecha y proveedor) ·
costos operativos, fijos y variables, del negocio actual o de uno comparable · precios del
producto o servicio · la capacidad instalada y la proyectada · el financiamiento disponible y
su tasa real · los permisos que hacen falta y cuánto tardan.

### Estudio de mercado

La base de clientes actuales, con su facturación · los precios de la empresa y su histórico ·
la encuesta o las entrevistas de campo, con sus respuestas una a una · lo que la empresa sabe
de su competencia, **marcado como percepción**.

### Auditoría interna o cumplimiento

El criterio: la norma, la política, el procedimiento o el contrato, en su versión vigente · el
universo de operaciones del periodo y de ahí la muestra · la evidencia de cada caso de la
muestra · los controles que dicen tener.

### Incidente

Los registros con hora: bitácoras, mensajes, tickets · qué se hizo y cuándo · el impacto
medido: clientes afectados, horas de parada, soles, datos · el procedimiento que debía haberse
seguido.

### Clima laboral o satisfacción

El instrumento que se aplicó · las respuestas una a una, anonimizadas · cuántos podían
responder y cuántos respondieron · la medición anterior, si hay.

## Lo que se pregunta de cada archivo que llega

Cuatro cosas, siempre, antes de usarlo:

1. **Qué periodo cubre y cuál es la fecha de corte.**
2. **De qué sistema salió**, o si se llevó a mano.
3. **Qué significa cada columna que no se entienda.** Sobre todo los estados y los códigos.
4. **Si está completo**: si falta un mes, si hay sedes que no están, si hubo un cambio de
   sistema en el periodo. **Un cambio de sistema a mitad del periodo rompe cualquier
   comparación**, y hay que saberlo antes de calcular.

## Las señales de que un dato no sirve como está

- **Meses con cero** en medio de un año con actividad: falta información, no es un cero.
- **Totales que no cuadran** con lo que dijo la gerencia: se pregunta antes de escribir, no
  después.
- **La misma cifra distinta en dos fuentes internas.** Pasa siempre (facturación contra
  contabilidad). Se dice en el informe, se elige una y se explica por qué.
- **Fechas imposibles**, duplicados, montos negativos sin explicación.
- **Todo llevado a mano** en una hoja de cálculo: se puede usar, diciendo que es un registro
  manual y no una exportación de sistema.

Lo que se encuentre así se anota y se le pregunta. **No se corrige en silencio.**

## Lo que no llega

Va derecho a la lista de limitaciones, con esta forma:

```
DATO QUE NO LLEGÓ          QUÉ DEJA DE PODERSE AFIRMAR
─────────────────────────  ─────────────────────────────────────────
Costo por orden de         El sobrecosto se cuantifica en horas,
despacho                   no en soles. La cifra en soles del
                           Hallazgo 3 usa el costo por hora promedio.

Reclamos de 2024           No se puede comparar la evolución de
                           reclamos: solo hay 2025 y 2026.
```

Dos reglas:

- **No se estima un dato que la empresa tiene y no entregó.** Se pide otra vez o se limita el
  informe. Estimarlo es inventarlo con otro nombre.
- **Sí se puede usar un dato aproximado que él confirme**, diciendo que es aproximado y de
  dónde sale: «según el jefe de almacén, unas 40 órdenes diarias; no hay registro».

## Cómo entran los archivos

- **Que los suba** con `material_del_curso`: quedan guardados y se pueden releer en las
  otras fases y en otras conversaciones. Acepta Word, PDF, Excel y texto.
- **Una matriz de datos que haya que calcular** va por `trabajar_en_r`, no por aquí: subir el
  Excel como material sirve para leer lo que dice, no para sacarle medias ni pruebas.
- **Una foto o un PDF escaneado** se adjunta en el chat, con el clip.
- Antes de subir nada, la regla del dato mínimo de `confidencialidad.md`.
