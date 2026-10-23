# Tablas, figuras y reporte numérico

---

## Numeración

**Continua en todo el artículo**, no por sección. Resultados sigue después de
la última tabla y figura de Métodos, que se ven con `articulo_docx.py esquema`.
Si Métodos trae la tabla de criterios (Tabla 1) y la de ecuaciones (Tabla 2),
Resultados empieza en la **Tabla 3**. El diagrama PRISMA suele ser la
Figura 1.

`verificar` detecta saltos, repetidos y tablas no citadas antes de aparecer.

## Citación en el texto

**Cada tabla y cada figura se menciona en el texto antes de aparecer.**

> En la Tabla 3 se presentan los coeficientes de trayectoria del modelo
> estructural.

Una tabla que nadie llama en el texto sobra, y una llamada que apunta al número
equivocado es de las observaciones más frecuentes en revisión.

## El texto no repite la tabla

La tabla trae todos los valores; el texto destaca **los que responden a las
hipótesis** y remite al resto.

Un párrafo que recorre la tabla fila por fila es relleno y ocupa palabras que la
revista cuenta.

## Formato APA 7

- Solo **reglas horizontales**: sobre el encabezado, bajo el encabezado y al
  cierre. Sin bordes verticales, sin sombreado, sin color.
- **Número de tabla en negrita**, en su propia línea.
- **Título en cursiva**, debajo del número.
- **Nota** debajo de la tabla, empezando con "Nota." en cursiva, a 11 puntos.
- Columnas numéricas centradas; la columna de etiquetas, a la izquierda.

En la nota van: los casos perdidos, las abreviaturas usadas, la convención de
significancia y cualquier normalización.

## Figuras

- Insertadas en el documento, no como archivo aparte.
- Con número, título y nota, igual que las tablas.
- **Legibles en escala de grises**, porque muchas revistas imprimen así. Si la
  figura solo se entiende en color, hay que rehacerla.
- Resolución suficiente. Una captura de pantalla del software pixelada se
  rechaza; conviene exportar la figura desde el programa.

Se insertan con la sintaxis del motor, `[FIGURA n] Título | figura.png`, con el
.png en la misma carpeta del `.md` (ver `formato_docx.md`). Si falta el
archivo, el motor deja un `[POR CONFIRMAR]`.

---

## Reglas de reporte numérico

**Formatear no es recalcular** (`analisis.md`). Las cifras se toman de las
salidas y solo se formatean: dos decimales para coeficientes y estadísticos,
tres para *p*, sin cero inicial donde el estilo lo pida. Eso se declara en la
nota. No se recalcula, no se "corrige" una cifra que no cuadra y no se completa
una celda vacía: si algo no cuadra, se pregunta.

**Redondear una sola vez.** Cada cifra se redondea desde el valor completo de
la salida (las tablas de R se guardan sin redondear; `analisis.md`). Nunca se
redondea un valor que ya venía redondeado: .0648 → .06 es correcto; .0648 →
.065 → .07 es un error que ningún `verificar` detecta. Una cifra que termina
en 5 tras un primer redondeo es la señal para volver al valor completo.

**Decimales consistentes** en todo el artículo: los porcentajes con uno (como
la Tabla 1), los estadísticos con dos y *p* con tres.

**El valor de p nunca se reporta como `p = 0.000`.** Ningún software calcula una
probabilidad de cero: lo que muestra es un valor menor al que puede representar.
Se reporta como `p < .001`.

**El cero a la izquierda** se omite en valores que no pueden pasar de 1 (p, r,
coeficientes estandarizados): `p < .001`, `r = .42`. Se mantiene en los que sí
pueden: `M = 3.24`, `DE = 0.87`.

**Los estadísticos van en cursiva**: *p*, *r*, *M*, *DE*, *t*, *F*, *R²*, *n*.

**Los intervalos de confianza se reportan** cuando el análisis los produce,
sobre todo en mediación. Un efecto indirecto sin su intervalo no se puede
evaluar.

**El tamaño del efecto acompaña a la significancia**, siempre que el análisis lo
permita.

## Sin adjetivos valorativos

Estas expresiones no van en Resultados:

| No | Sí |
|---|---|
| "excelente ajuste" | el índice, con su criterio de referencia |
| "fuerte correlación" | el valor de *r* |
| "resultados alentadores" | el resultado |
| "como era de esperarse" | nada; eso es Discusión |
| "sorprendentemente" | nada |

El valor y su criterio dicen todo lo que hay que decir. El juicio va en la
Fase 6.

## Comprobación final antes de unir

1. ¿La numeración es continua y sin repetidos, contando la Tabla 1 de Métodos?
2. ¿Cada tabla y figura se cita en el texto, y el número coincide?
3. ¿Los decimales son los mismos en todo el documento?
4. ¿Ninguna p aparece como 0.000?
5. ¿Cada cifra es la de la salida, solo formateada y redondeada una sola vez
   desde el valor completo?
6. ¿`articulo_docx.py verificar` pasó sin ✗?
