# Población, muestra y muestreo

Esta referencia documenta las fórmulas y técnicas para la sub-sección 3.3.

## 3.3.1 Población

La población es el conjunto total de personas, casos o elementos que cumplen ciertas características y son objeto del estudio. Debe delimitarse por:

- **Características**: edad, grado, cargo, ubicación.
- **Cantidad estimada (N)**: aproximada si es grande, exacta si es pequeña.
- **Criterios de inclusión**: quiénes SÍ entran.
- **Criterios de exclusión**: quiénes NO entran (ausencias prolongadas, edad fuera de rango, etc.).

## 3.3.2 Muestra (cuantitativa)

La skill describe varias opciones de cálculo. El tesista elige con su asesor.

### Opción 1: Censo

Cuando la población es **accesible y de tamaño manejable** (menos de 100-150 personas), es válido estudiar a todos. No requiere fórmula.

Ejemplo: "La muestra coincide con la población total (N = 80), por lo cual se trata de un estudio censal."

### Opción 2: Fórmula para población finita (N conocido)

Carrasco y Hernández-Sampieri y Mendoza (cada uno con la clave de su obra en la biblioteca) proponen:

```
        N · Z² · p · q
n = ──────────────────────
    e²·(N-1) + Z² · p · q
```

Donde:
- N = tamaño de la población
- Z = nivel de confianza (1.96 para 95%; 2.58 para 99%)
- p = probabilidad de éxito (0.5 cuando no se conoce; máxima varianza)
- q = probabilidad de fracaso = 1 - p = 0.5
- e = margen de error (0.05 estándar; 0.03 más conservador)

Ejemplo de cálculo con N = 200, Z = 1.96, p = q = 0.5, e = 0.05:

```
       200 · (1.96)² · 0.5 · 0.5      192.08
n = ─────────────────────────────── = ────── = 132
    (0.05)²·(199) + (1.96)²·0.5·0.5   1.4579
```

n ≈ 132 estudiantes.

### Opción 3: Fórmula para población infinita o muy grande

Cuando N es muy grande o desconocida (Cochran, *Sampling Techniques*, con la clave de su ficha en la biblioteca):

```
    Z² · p · q
n = ───────────
        e²
```

Con Z = 1.96, p = q = 0.5, e = 0.05:

```
    (1.96)² · 0.5 · 0.5
n = ───────────────────── = 384
        (0.05)²
```

n ≈ 384 personas. Este es el clásico tamaño mínimo para encuestas de población masiva.

### Opción 4: Mínimo para PLS-SEM

Hair y colaboradores (con la clave de su obra en la biblioteca; confirmar la edición en la ficha) proponen para modelos estructurales con PLS-SEM:

- 10 veces el número máximo de flechas que apuntan a un constructo.
- En general, mínimo recomendado n = 100 a 200 para modelos simples.

Esta opción solo aplica si el nivel es explicativo con modelo estructural.

## 3.3.3 Muestreo (cuantitativo)

La skill pregunta al tesista sobre acceso a la población y propone técnica.

### Si "acceso total"

→ **Censo**. No requiere muestreo aleatorio.

### Si "acceso parcial probabilístico"

La skill propone según heterogeneidad:

- **Aleatorio simple**: cuando la población es homogénea y el listado completo está disponible.
- **Sistemático**: cuando hay lista ordenada (cada k-ésimo elemento, donde k = N/n).
- **Estratificado**: cuando hay sub-grupos heterogéneos (estratos por grado, género, etc.) y se quiere representación proporcional.
- **Por conglomerados**: cuando la población está agrupada (aulas, secciones) y se eligen aleatoriamente grupos completos.

### Si "voluntariado o solo quienes acepten"

→ **No probabilístico por conveniencia o intencional**. Esto reduce la generalizabilidad pero es válido en pregrado cuando no hay otra opción.

Justificar siempre: "Por razones de accesibilidad y disponibilidad de los participantes, se aplicó muestreo no probabilístico por conveniencia, lo cual limita la generalización de los hallazgos al contexto específico del estudio."

## Muestra cualitativa

No se calcula con fórmula. Se justifica por **saturación teórica**: se deja de sumar participantes cuando los nuevos datos ya no agregan información distinta.

Tamaños orientativos en pregrado:

- **Fenomenológico**: 8 a 15 participantes.
- **Estudio de caso**: 1 a 3 casos en profundidad.
- **Etnográfico**: 1 comunidad, inmersión prolongada.
- **Teoría fundamentada**: 20+ participantes por iteración.

### Muestreo cualitativo

- **Por conveniencia**: participantes accesibles.
- **Intencional o de criterio**: participantes que cumplen criterios específicos para el fenómeno estudiado.
- **Bola de nieve**: cada participante recomienda al siguiente.
- **Por cuotas**: cumple cuotas por características predefinidas.

## Plantilla de redacción

**Advertencia crítica**: los ejemplos siguientes son **ilustraciones de estructura**, no plantillas para reproducir literalmente. Sustituir cada corchete con datos reales del tesista. Si dos tesis del método reciben la misma redacción con la misma institución, misma ciudad, misma cantidad, se detecta clonación.

### 3.3.1 Población (estructura)

> La población del presente estudio está conformada por [descripción de los participantes, incluyendo grado/rol/característica principal] de [tipo de institución, sin nombre específico] del [distrito/región/localidad del tesista], durante el [año declarado por el tesista]. Se estima un tamaño poblacional de [N exacto o rango], distribuido en [aclaración de estructura interna: secciones, áreas, turnos]. Los criterios de inclusión son: [3 criterios adaptados al caso]. Los criterios de exclusión son: [criterios paralelos, no inferidos].

### 3.3.2 Muestreo (estructura, va ANTES de muestra)

> La técnica de muestreo seleccionada es [tipo probabilístico o no probabilístico + subtipo], dado que [justificación derivada del acceso real del tesista, del tamaño de la población y de su heterogeneidad]. Esta técnica permite [ventaja específica del caso] [AR…].
>
> (La clave es la de un autor rotativo: Carrasco, Hernández-Sampieri y Mendoza, Ñaupas y colaboradores o Bernal, según lo que devuelva la búsqueda. Las claves `[AR…]` de estas plantillas son marcadores.)

### 3.3.3 Muestra (estructura, se calcula DESPUÉS de decidir muestreo)

> Para determinar el tamaño muestral se aplicó [fórmula seleccionada por el tesista: Fisher para población finita / Cochran para infinita], considerando un nivel de confianza del 95 por ciento (Z = 1.96), una proporción esperada del 0.5 y un margen de error del 0.05. El cálculo arrojó un tamaño muestral de [n calculado], que se aplicará en el estudio.

### 3.3.4 Unidad de análisis (estructura, OBLIGATORIA)

> La unidad de análisis del estudio es cada [participante individual: estudiante, colaborador, paciente, etc.], sobre quien se aplica el instrumento y se registran las variables. La unidad muestral y la unidad de análisis coinciden en este diseño.

## Reglas críticas

- **Citar autor** para cada decisión (Carrasco, Hernández-Sampieri, Cochran, Hair) con la clave de su obra en la biblioteca. Si no está, se le pide al tesista que la agregue y mientras tanto va `[FALTA FUENTE]`, con aviso en el chat.
- **Justificar el muestreo no probabilístico** explicitando la limitación.
- **NO inventar el tamaño de la población**. Si el tesista no lo sabe, preguntarle.
- **Considerar criterios de inclusión y exclusión** desde el inicio, no como ajuste posterior.
