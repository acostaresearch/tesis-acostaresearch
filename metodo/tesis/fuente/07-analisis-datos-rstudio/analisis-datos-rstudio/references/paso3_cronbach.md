# Paso 3 — Alfa de Cronbach

## Por qué este paso

El alfa de Cronbach, propuesto por Cronbach en 1951 (en el texto guardado se cita con la clave de esa fuente en la biblioteca del tesista, o `[FALTA FUENTE]` si aún no la tiene), mide la consistencia interna del instrumento. Un alfa alto indica que los ítems de una variable miden el mismo constructo.

El jurado de sustentación va a esperar este número. No reportarlo es señal de tesis incompleta.

## Niveles de cálculo

La skill calcula Cronbach en TRES niveles:

1. **Por variable completa** (V1 con sus 24 ítems, V2 con sus 14 ítems).
2. **Por dimensión** (V1.D1 con 6 ítems, V1.D2 con 6 ítems, etc.).
3. **Comparativo** con el alfa del piloto (si se calculó antes).

## Código R

```r
library(psych)

# Cronbach de V1 completa (24 ítems)
alpha(datos[, paste0("ITEM_", sprintf("%02d", 1:24))])

# Cronbach de V2 completa (14 ítems)
alpha(datos[, paste0("ITEM_", sprintf("%02d", 25:38))])

# Cronbach por dimensión — V1.D1 (ítems 1-6)
alpha(datos[, paste0("ITEM_", sprintf("%02d", 1:6))])

# Cronbach por dimensión — V1.D2 (ítems 7-12)
alpha(datos[, paste0("ITEM_", sprintf("%02d", 7:12))])

# ... y así sucesivamente para cada dimensión
```

## SPSS

```
Analizar > Escala > Análisis de fiabilidad
   → Variables: selecciona los ítems de la variable o dimensión
   → Modelo: Alfa
   → Click Estadísticos
      → Estadísticos descriptivos para: Escala si se elimina el elemento
      → Inter-elementos: Correlaciones
   → Continuar > Aceptar
```

Repetir el procedimiento por variable y por dimensión.

## Salida que el tesista pega al chat

### De R

```
Reliability analysis
Call: alpha(x = datos[, ...])

  raw_alpha std.alpha G6(smc) average_r S/N    ase mean   sd
       0.87      0.88    0.92      0.24 7.1  0.013  3.5  0.6

 lower alpha upper     95% confidence boundaries
0.85  0.87   0.89

Reliability if an item is dropped:
       raw_alpha std.alpha G6(smc) average_r ...
ITEM_01    0.86     0.87    0.91     0.23
ITEM_02    0.87     0.88    0.92     0.24
...
```

### De SPSS

```
Estadísticas de fiabilidad
Alfa de Cronbach  N de elementos
       0,872            24

Estadísticas de total de elemento
                Media de escala  Alfa si se
                si se elimina    elimina el
                el elemento      elemento
ITEM_01         ...               0,865
ITEM_02         ...               0,870
...
```

## Interpretación que la skill aplica

| Alfa | Interpretación |
|------|----------------|
| ≥ 0.90 | Excelente |
| 0.80 - 0.89 | Buena |
| 0.70 - 0.79 | Aceptable (mínimo pregrado) |
| 0.60 - 0.69 | Cuestionable |
| < 0.60 | Inaceptable |

Fuentes de estos rangos: Hernández-Sampieri y Mendoza, 2018; Ñaupas Paitán et al., 2019 (en el capítulo, con su clave `[AR…]`).

## Si Cronbach < 0.70

### Diagnóstico

Revisar la columna "alpha if item deleted" (o "Alfa si se elimina el elemento" en SPSS). Los ítems que al eliminarlos hacen subir el alfa son los problemáticos.

### Decisión

1. **Si 1-2 ítems son problemáticos** y al eliminarlos el alfa sube por encima de 0.70: eliminar y reportarlo en el capítulo.

2. **Si muchos ítems son problemáticos** o el alfa sigue bajo tras eliminar: la skill **deriva a Skill 5** para reformular el instrumento. NO avanzar al Paso 4 con un instrumento inválido.

3. **Caso límite**: si el alfa está entre 0.65 y 0.70, consultar con asesor. Algunos asesores aceptan ese rango en contextos exploratorios.

## Cómo se reporta en el capítulo

Texto modelo:

> Para evaluar la consistencia interna del instrumento, se aplicó el coeficiente alfa de Cronbach. La variable Uso de IA generativa obtuvo α = .87 (24 ítems), valor considerado bueno según los rangos propuestos por Hernández-Sampieri y Mendoza [AR…:n]. La variable Disposición al Pensamiento Crítico obtuvo α = .82 (14 ítems), también en rango bueno. La Tabla 2 presenta los coeficientes por variable y por dimensión.
>
> (Aquí va el bloque de la Tabla 2: `**Tabla 2**`, `*Título*`, la tabla con `|` y `*Nota.*`, sin líneas en blanco.)

Formato APA 7: tres decimales sin cero antes del punto, así: ".87" en lugar de "0.870".

## Errores comunes

1. **Reportar solo el alfa global sin desglosar por variable**: el jurado quiere ver alfa por cada constructo.
2. **No reportar alfa por dimensión** cuando la operacionalización las usa.
3. **Inflar alfa eliminando muchos ítems sin justificación**.
4. **Olvidar comparar con el alfa del piloto**: el campo grande debería tener alfa similar o ligeramente superior. Diferencias grandes (>0.10) ameritan explicación.
