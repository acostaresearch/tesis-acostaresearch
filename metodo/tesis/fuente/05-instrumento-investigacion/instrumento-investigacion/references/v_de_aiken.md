# V de Aiken

## Qué es

Coeficiente para cuantificar el grado de acuerdo entre los expertos que evalúan un ítem. Propuesto por Aiken en 1985. En el texto guardado se cita con la clave de esa fuente; si no está en la biblioteca del tesista, se busca con `buscar_fuentes` o se añade con su permiso, y mientras no tenga clave la afirmación va con `[FALTA FUENTE]`. En pregrado peruano es el método más usado para reportar validez de contenido junto al juicio de expertos.

## Fórmula

```
        S
V = ─────────
    n · (c - 1)
```

Donde:
- **S** = suma de las valoraciones dadas por los expertos a un ítem.
- **n** = número de expertos.
- **c** = número de valores de la escala de valoración (típicamente 5 si los expertos califican de 1 a 5).

## Cálculo paso a paso (ejemplo)

Ítem 1, evaluado por 5 expertos en el criterio de claridad con escala 1-5:

| Experto | Valoración |
|---------|-----------|
| E1 | 5 |
| E2 | 4 |
| E3 | 5 |
| E4 | 5 |
| E5 | 4 |
| **Suma (S)** | **23** |

Cálculo:

```
V = 23 / (5 · (5 - 1)) = 23 / 20 = 1.15
```

Espera, hay un detalle. La fórmula original de Aiken asume que las valoraciones de los expertos parten de 0, no de 1. Si los expertos califican de 1 a 5, hay que **restar 1 a cada valoración** antes de sumar, o usar la fórmula corregida:

```
        S - n
V = ───────────────
    n · (c - 1)
```

Aplicando la fórmula corregida al ejemplo:

```
S = 23, n = 5, c = 5
V = (23 - 5) / (5 · (5 - 1)) = 18 / 20 = 0.90
```

V = 0.90 indica acuerdo alto entre expertos: el ítem se mantiene.

## Interpretación

| V | Interpretación | Acción |
|---|----------------|--------|
| V ≥ 0.80 | Validez aceptable | Mantener el ítem |
| 0.50 ≤ V < 0.80 | Validez cuestionable | Modificar el ítem según observaciones |
| V < 0.50 | Validez inaceptable | Eliminar o reformular completamente |

Algunos autores adoptan umbral más estricto (V ≥ 0.70 mínimo). En pregrado peruano lo común es **V ≥ 0.80**.

## Aplicación por criterio

Cada ítem se evalúa típicamente en 3 criterios independientes:

1. **Claridad**: ¿el ítem se entiende?
2. **Coherencia**: ¿el ítem corresponde a la dimensión que dice medir?
3. **Relevancia**: ¿el ítem es necesario para cubrir la dimensión?

Se calcula V por cada criterio. Un ítem se considera **válido** si los 3 criterios tienen V ≥ 0.80.

Si claridad < 0.80 pero coherencia y relevancia están bien, el ítem se reformula para mejorar la claridad sin cambiar su contenido conceptual.

## Cómo la skill calcula V de Aiken

Cuando el tesista pega los valores de sus expertos en chat, la skill:

1. Identifica número de expertos (n).
2. Identifica escala usada (c, típicamente 5).
3. Para cada ítem y cada criterio:
   - Suma valoraciones (S).
   - Aplica fórmula V = (S - n) / (n · (c - 1)).
4. Reporta tabla resumen con V por ítem y criterio.
5. Recomienda ajustes según los umbrales.

### Formato esperado para pegar valores

El tesista puede pegar en cualquier formato; la skill interpreta. Ejemplo aceptable:

```
Ítem 1: E1: claridad 5, coherencia 5, relevancia 5
        E2: claridad 4, coherencia 5, relevancia 4
        E3: claridad 5, coherencia 5, relevancia 5
        E4: claridad 5, coherencia 4, relevancia 5
        E5: claridad 4, coherencia 5, relevancia 5
```

O en tabla:

```
Ítem | E1 cla | E1 coh | E1 rel | E2 cla | ...
1    | 5      | 5      | 5      | 4      | ...
```

## Formato en el capítulo

La skill escribe en el capítulo guardado una tabla (con la sintaxis de tabla del SKILL.md: un bloque sin líneas en blanco, que el Word del servidor convierte en tabla APA) con:

| Ítem | Texto del ítem | Claridad (1-5) | Coherencia (1-5) | Relevancia (1-5) | Observaciones |

Una fila por ítem. El experto rellena las columnas 3, 4, 5 y 6.

Debajo de la matriz, en su propio cuadro (Campo | Valor):
- Datos del experto: nombre, grado académico, especialidad, institución.
- Fecha.
- Firma.

## Errores comunes

- **Confundir umbral**: usar V ≥ 0.50 cuando el estándar peruano es V ≥ 0.80.
- **No reportar V por criterio**: solo reportar un V global. Mejor reportar los 3 y el promedio.
- **Olvidar fórmula corregida**: aplicar V = S/(n·(c-1)) sin restar n, lo cual sobreestima el coeficiente.
- **Expertos genéricos**: pedir validación a magisters que no son del tema específico. Los expertos deben tener publicaciones o experiencia en el constructo medido.
