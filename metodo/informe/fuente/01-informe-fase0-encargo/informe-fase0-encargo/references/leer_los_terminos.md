# Cómo leer los términos de referencia

Los términos de referencia son lo que pidió el cliente. Rara vez llegan como un pliego
formal: casi siempre son **un correo de tres líneas** o lo que dijo un gerente en una reunión.
Leerlos bien es convertir eso en un encargo con bordes.

## Los ocho datos que hay que sacar

| Qué | Por qué importa | Si no está |
|---|---|---|
| **Qué decisión se quiere tomar** | Ordena todo el informe | Se pregunta. Es el único que no se puede dejar en blanco |
| **Quién lo recibe** | Decide el tono y el resumen ejecutivo | Se pregunta |
| **Tipo de informe** | Decide la estructura | Se deduce de la decisión y se confirma |
| **Alcance** | Es lo que se discute al entregar | Se propone y se marca `[POR CONFIRMAR CON QUIEN LO PIDE]` |
| **Secciones y formato** | Si la empresa tiene plantilla, manda | Estructura base del tipo |
| **Extensión** | Un informe de 60 páginas para quien quería 10 se lee mal | Se propone la habitual del tipo |
| **Fecha de entrega** | Decide el calendario y qué se puede hacer | Se pregunta |
| **Qué datos habrá** | Decide qué se puede afirmar | Se hace la lista de lo que hay que pedir |

## De un correo de tres líneas a un encargo

Lo que llega:

> «Hola, necesito que revises el área de almacén, hay problemas. Para fin de mes.»

Lo que se le devuelve, para que lo confirme:

```
Así entiendo el encargo. Corrígeme lo que esté mal:

Decisión que apoya   Decidir qué cambiar en el almacén para reducir los
                     problemas de despacho.
Para                 Gerencia General.
Tipo                 Diagnóstico de un proceso.
Entra                El proceso de almacén de la sede principal: recepción,
                     almacenamiento, picking y despacho. Periodo: últimos
                     12 meses.
No entra             Compras, transporte y las otras sedes.
                     [POR CONFIRMAR CON QUIEN LO PIDE]
Extensión            20 a 30 páginas, más anexos.
Entrega              30 de septiembre de 2026.
Datos que necesito   Órdenes de despacho del año, tomas de inventario,
                     reclamos de clientes, dotación del área.
```

Tres cosas que hace ese cuadro: **cierra el alcance**, deja por escrito lo que no entra, y
convierte «hay problemas» en una decisión.

## Cuando dice «hay problemas»

Es lo más común y no es un encargo: es un síntoma. Se le pregunta **una vez**, con opciones:

```
¿Qué te hizo pedir este informe?
· Nos están reclamando los clientes
· Se está gastando más de lo que debería
· Alguien de arriba pidió que se revise
· Hubo un problema concreto y hay que entender por qué
· Otra cosa, te la cuento
```

La respuesta se guarda en `informe.decision`. Todo el informe se mide contra ella.

## Qué NO se deduce de los términos de referencia

- **El resultado.** Si el correo dice «necesito el informe para justificar la compra del
  sistema», el informe no arranca justificando nada. Se le dice en una línea: el informe va a
  decir lo que muestre la evidencia, y eso es lo que lo hace útil frente a gerencia.
- **Que el problema esté donde lo señalan.** Un diagnóstico empieza en el proceso completo del
  alcance, no en la causa que ya trae el cliente en la cabeza. Si la evidencia apunta a otro
  lado, se dice.
- **Que los datos existen.** «Sí, tenemos todo eso» suele significar que está en hojas de
  cálculo sueltas. De ahí el Paso de la lista de datos por pedir.

## Cuando la empresa tiene plantilla

Si hay plantilla de informes o un índice exigido, **manda esa numeración**. Se copia tal cual,
con sus números, y el esquema se ajusta a ella aunque la estructura base del tipo sea otra. Lo
que la plantilla no tenga y el informe necesite se propone como sección adicional y se
pregunta si se puede añadir.

La plantilla de **formato de página** (márgenes, fuente, membrete, portada) es otra cosa: esa
se sube con `formato_de_la_universidad` y el Word la respeta.

## El alcance se escribe en el informe

No es solo un acuerdo de la Fase 0: las tres listas van en la introducción del informe final.

- **Entra:** qué unidad, qué proceso, qué periodo, qué sedes.
- **No entra:** lo que no se miró, dicho explícitamente.
- **Limitaciones:** qué datos no se tuvieron y **qué deja de poder afirmarse por eso**.

La tercera es la que protege el informe. Ejemplo:

> No se tuvo acceso al costo por orden de despacho, porque el sistema no lo registra. Por eso
> el informe cuantifica el sobrecosto en horas de trabajo y no en soles, y la estimación en
> soles del Hallazgo 3 usa el costo por hora promedio del área, no el real por orden.

## Cuando el plazo no alcanza

Se dice en la Fase 0, no en la Fase 4. Si la entrega es en cuatro días y el encargo es un
diagnóstico de 40 páginas, hay tres salidas y se le dan las tres:

1. **Recortar el alcance:** un proceso en vez de cuatro, bien hecho.
2. **Entregar por partes:** un avance con los hallazgos en la fecha, y el informe completo
   después.
3. **Pedir más plazo**, con el argumento a mano: qué datos faltan y cuánto tardan en llegar.

Lo que no se hace es aceptar el plazo y rellenar.
