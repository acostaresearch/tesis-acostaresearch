# SPSS — Menús para los 6 pasos del análisis

Esta referencia consolida los menús SPSS para tesistas que eligen este camino. Cubre los 6 pasos secuenciales.

## Paso 1 — Importar datos

```
Archivo > Abrir > Datos
   → Selecciona el archivo .xlsx o .csv
   → Marca "La primera fila contiene nombres de variables"
   → Click Aceptar

Verás la pestaña "Vista de datos" con las respuestas y la pestaña
"Vista de variables" con los nombres y tipos.
```

### Verificación de tipos de variables

En la pestaña "Vista de variables", confirmar:
- ID: tipo Cadena (Texto)
- GRADO, SECCION, EDAD: tipo Numérico
- ITEM_01 a ITEM_38 (o V1_D1_01 a V2_D7_02): tipo Numérico, escala Likert

Si algún ítem aparece como Cadena, cambiar a Numérico antes de continuar.

## Paso 2 — Estadísticos descriptivos

### Crear puntajes totales (antes de descriptivos)

```
Transformar > Calcular variable
   → Variable de destino: V1_total
   → Expresión numérica: SUM(ITEM_01 TO ITEM_24)
   → Aceptar

Repetir para V2_total: SUM(ITEM_25 TO ITEM_38)
```

### Crear puntajes por dimensión (promedio)

```
Transformar > Calcular variable
   → Variable de destino: V1_D1
   → Expresión numérica: MEAN(ITEM_01 TO ITEM_06)
   → Aceptar
```

### Frecuencias demográficas

```
Analizar > Estadísticos descriptivos > Frecuencias
   → Variables: GRADO, SECCION, EDAD
   → Click Estadísticos > Media, Desv. típica, Mín, Máx, Asimetría, Curtosis
   → Click Gráficos > Gráfico de barras
   → Aceptar
```

### Descriptivos de variables cuantitativas

```
Analizar > Estadísticos descriptivos > Descriptivos
   → Variables: V1_total, V2_total, todos los V1_D*, V2_D*
   → Click Opciones > Media, Desv. típica, Mín, Máx
   → Aceptar
```

### Histograma

```
Gráficos > Cuadros de diálogo antiguos > Histograma
   → Variable: V1_total
   → Marcar "Mostrar curva normal"
   → Aceptar
```

## Paso 3 — Alfa de Cronbach

```
Analizar > Escala > Análisis de fiabilidad
   → Elementos: selecciona los ítems de UNA variable o dimensión
   → Modelo: Alfa
   → Click Estadísticos
      → Marcar:
         - Estadísticos descriptivos para: Elemento, Escala, Escala si se elimina elemento
         - Inter-elementos: Correlaciones
         - Resumen: Medias, Varianzas, Correlaciones
   → Continuar > Aceptar

REPETIR para cada variable y cada dimensión.
```

Salida importante:
- "Alfa de Cronbach" (valor principal)
- "Alfa de Cronbach basada en elementos estandarizados"
- "Alfa si se elimina el elemento" (para identificar ítems problemáticos)

## Paso 4 — Normalidad

```
Analizar > Estadísticos descriptivos > Explorar
   → Lista de dependientes: V1_total, V2_total
   → Click Gráficos
      → Marcar "Gráficos de normalidad con pruebas"
   → Continuar > Aceptar
```

SPSS entrega tanto Kolmogorov-Smirnov con corrección de Lilliefors como Shapiro-Wilk en la misma tabla.

Reportar Shapiro-Wilk si n < 50; Lilliefors si n ≥ 50.

## Paso 5 — Pruebas inferenciales

### Pearson o Spearman (correlación)

```
Analizar > Correlaciones > Bivariadas
   → Variables: V1_total, V2_total
   → Coeficientes:
      - Pearson (si datos normales)
      - Spearman (si datos no normales)
   → Prueba de significación: Bilateral
   → Marcar las correlaciones significativas
   → Aceptar
```

### t de Student (2 grupos)

```
Analizar > Comparar medias > Prueba T para muestras independientes
   → Variables de prueba: V1_total
   → Variable de agrupación: GRADO
      → Definir grupos: Grupo 1 = 4, Grupo 2 = 5
   → Aceptar

SPSS incluye automáticamente la prueba de Levene.
Si Levene p > 0.05, leer la fila "Asumiendo varianzas iguales".
Si Levene p ≤ 0.05, leer la fila "No asumiendo varianzas iguales".
```

### Mann-Whitney (2 grupos, no normales)

```
Analizar > Pruebas no paramétricas > Cuadros de diálogo antiguos > 2 muestras independientes
   → Lista de variables: V1_total
   → Variable de agrupación: GRADO (definir grupos)
   → Tipo: U de Mann-Whitney
   → Aceptar
```

### ANOVA (3+ grupos, normales)

```
Analizar > Comparar medias > ANOVA de un factor
   → Dependiente: V1_total
   → Factor: SECCION
   → Click Post Hoc > Tukey
   → Click Opciones > Descriptivos, Homogeneidad de varianzas
   → Aceptar
```

### Kruskal-Wallis (3+ grupos, no normales)

```
Analizar > Pruebas no paramétricas > Cuadros de diálogo antiguos > K muestras independientes
   → Lista de variables: V1_total
   → Variable de agrupación: SECCION (definir rango)
   → Tipo: H de Kruskal-Wallis
   → Aceptar
```

### Chi cuadrado (categóricas)

```
Analizar > Estadísticos descriptivos > Tablas cruzadas
   → Filas: GRADO
   → Columnas: SECCION
   → Click Estadísticos > Chi-cuadrado, V de Cramer
   → Click Casillas > Observado, Esperado, Porcentaje fila
   → Aceptar
```

### Regresión lineal

```
Analizar > Regresión > Lineales
   → Dependiente: V2_total
   → Independientes: V1_total (o varias si es múltiple)
   → Método: Introducir
   → Click Estadísticos
      → Marcar: Estimaciones, Intervalos de confianza, Ajuste del modelo,
         Cambio en R², Diagnósticos de colinealidad, Durbin-Watson
   → Click Gráficos
      → ZPRED en X, ZRESID en Y (para verificar homocedasticidad)
   → Aceptar
```

## Paso 6 — Exportar para Fase 2

### Exportar tablas a Excel

```
En el Visor de Resultados:
- Clic derecho en la tabla
- Copiar
- Pegar en Excel (Word también funciona, pero Excel mantiene mejor formato)
```

### Exportar figuras a PNG

```
En el Visor de Resultados:
- Clic derecho en el gráfico
- Exportar
- Tipo: PNG
- Aceptar
```

### Guardar archivo de sintaxis (opcional pero recomendado)

Para tener respaldo del análisis:

```
Archivo > Nuevo > Sintaxis

Pegar manualmente los comandos ejecutados, o:
- En cualquier ventana de diálogo, click "Pegar" en lugar de "Aceptar"
- Esto vuelca el comando a una ventana de sintaxis
- Guardar con Archivo > Guardar como > tipo .sps
```

## Diferencias clave entre R y SPSS para el tesista

| Aspecto | R/RStudio | SPSS |
|---------|-----------|------|
| Costo | Gratis | Pagado (universidades dan licencia limitada) |
| Curva de aprendizaje | Más empinada | Más amigable al inicio |
| Reproducibilidad | Excelente (script .R) | Limitada (hay que recordar menús) |
| Output | Texto en consola | Tablas formateadas (Visor de Resultados) |
| Tablas APA 7 | Hay que armarlas | Más cerca del formato APA pero requieren ajustes |
| Recomendación del método | Camino principal | Camino válido pero menos eficiente |
