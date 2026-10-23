# Tablas y figuras en un informe empresarial

El Word lo arma el servidor. La skill escribe el bloque en Markdown y el servidor le pone el
formato de la norma del proyecto. **Cada bloque va sin líneas en blanco dentro**, o el
servidor lo parte en dos.

## La diferencia con un trabajo académico: la línea «Fuente»

En esta ruta **toda tabla y toda figura lleva su origen debajo**, y no es opcional. Quien lee
el informe va a preguntar de dónde salió ese número, y si no está escrito, el informe pierde.

```
*Nota.*   ← explica cómo se leen los datos, o qué se calculó
*Fuente.* ← dice DE DÓNDE salieron los datos
```

Pueden ir las dos, y si solo va una, va «Fuente». Cómo se escribe según de dónde venga:

| De dónde | Cómo se escribe la línea |
|---|---|
| Un dato interno | `*Fuente.* Reporte de facturación, área comercial, al 31 de marzo de 2026.` |
| Un cálculo propio con datos internos | `*Fuente.* Elaboración propia con los registros de despacho de enero a marzo de 2026.` |
| Una fuente externa | `*Fuente.* INEI [AR97D22F86].` |
| Varias | `*Fuente.* Elaboración propia con datos de facturación de la empresa y del BCRP [AR2E15C80C].` |
| Una encuesta que se hizo | `*Fuente.* Encuesta a 84 clientes, aplicada del 3 al 14 de marzo de 2026.` |
| Una proyección | `*Fuente.* Proyección propia. Supuestos en la Tabla 7.` |

**Una proyección dice que es proyección en su propia línea de fuente.** Es la salvedad que
más se olvida y la que más cara sale.

## Tablas

Para **comparar** (antes y después, meta y real, dos alternativas) o para datos que no caben
en una frase. Dos o tres números van en el texto, no en una tabla.

```
**Tabla 2**
*Ventas por línea de producto, primer trimestre de 2025 y 2026*
| Línea | 2025 (S/) | 2026 (S/) | Variación |
|---|---|---|---|
| Carga general | 1 204 500 | 1 042 800 | -13,4 % |
| Carga refrigerada | 486 200 | 511 900 | +5,3 % |
| Total | 1 690 700 | 1 554 700 | -8,0 % |
*Fuente.* Reporte de facturación, área comercial, al 31 de marzo de 2026.
```

Reglas:

- **Unidades en la cabecera**, entre paréntesis: `Ventas (S/)`, `Tiempo (min)`, `Peso (t)`.
- **Decimales iguales en toda la columna.** Porcentajes con un decimal.
- **Miles con espacio**, no con coma: `1 554 700`. La coma es el decimal.
- **Los totales suman.** Se comprueba. Una tabla cuyo total no cuadra hunde el informe entero.
- **Pocas columnas.** Más de seis no se lee en un Word vertical; si hacen falta, va al anexo y
  en el cuerpo queda el resumen.
- **La variación se calcula**, no se estima a ojo: va por `trabajar_en_r`.
- Si una celda no tiene dato, `[FALTA DATO]` o un guion con su explicación en la nota. **No se
  deja en blanco y no se rellena con cero**: cero es un dato y significa otra cosa.

## Figuras

Para **tendencias** (una línea en el tiempo), **composición** (barras) o para mostrar algo
(foto, captura, plano, diagrama).

```
**Figura 2**
*Ventas mensuales de carga general, enero de 2025 a marzo de 2026*
[Insertar aquí la Figura 2: ventas-carga-general.png]
*Fuente.* Elaboración propia con el reporte de facturación de la empresa.
```

- El nombre del archivo en la marca **es el que él va a pegar**. Se le dice cuál va en cada
  marca.
- El Word deja la marca resaltada donde va la imagen.
- Si la figura sale de `trabajar_en_r`, el nombre del archivo es el que devolvió R.

## Gráficos: lo que no se hace

| No | Por qué | Qué va en su lugar |
|---|---|---|
| Torta con más de cinco porciones | No se comparan porciones parecidas | Barras horizontales ordenadas de mayor a menor |
| Eje que no empieza en cero, en barras | Exagera la diferencia | Eje desde cero, o líneas en vez de barras |
| Dos ejes verticales distintos | Se puede hacer decir cualquier cosa | Dos gráficos, o índices con la misma base |
| 3D, sombras, degradados | Deforman la lectura | Plano |
| Línea que une puntos de categorías | Una línea sugiere continuidad | Barras |
| Todo el año en un gráfico para mostrar un mes | Esconde el hallazgo | El periodo que importa, y el resto al anexo |

## El orden de cada tabla o figura en el texto

1. **Anunciar, con el hallazgo:** «La Tabla 2 muestra que la caída se concentra en carga
   general.» No «A continuación se presenta la Tabla 2».
2. **El bloque.**
3. **Interpretar:** qué significa para la decisión, en dos o tres oraciones. Sin repetir los
   números de la tabla uno por uno.

Una tabla que no se menciona en el texto se quita o se manda al anexo.

## Numeración

Tablas y figuras se numeran **cada una en su serie y seguido en todo el informe**: Tabla 1,
Tabla 2… y Figura 1, Figura 2… No se reinicia por sección. Como cada fase guarda su texto por
separado, antes de numerar se mira con `ver_capitulo` cuántas hay en las secciones anteriores
y se sigue desde ahí.

## Anexos

Va al anexo lo que quien decide no necesita para decidir, pero alguien puede querer revisar:
la tabla de 300 filas, los cálculos detallados, la guía de entrevista, las cotizaciones, el
detalle de la muestra. En el cuerpo queda el resumen y una línea: «el detalle está en el
Anexo 3».

Los anexos **no los pega la skill**: se listan para que él los pegue al final del Word,
después de las referencias.
