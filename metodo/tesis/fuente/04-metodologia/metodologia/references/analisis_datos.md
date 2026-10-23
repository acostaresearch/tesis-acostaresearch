# Análisis de datos

Esta referencia documenta la sub-sección 3.8. Describe a **alto nivel** las técnicas de análisis. NO ejecuta el análisis (eso es la Skill de Análisis con RStudio, Cap VII del método).

## Si enfoque cuantitativo

### Limpieza de la base de datos (PRIMER momento obligatorio)

Antes de cualquier análisis estadístico, la base debe depurarse. Este paso debe estar declarado explícitamente en 3.8, no dejarse para después. Elementos que se declaran:

- **Depuración de casos incompletos**: regla clara de exclusión o imputación. Ej. "se excluyen los casos con más del 20% de ítems en blanco" o "se imputa por la media de la dimensión si faltan hasta 2 ítems".
- **Codificación inversa de ítems negativos**: los ítems formulados en negativo (ej. "no me siento capaz de…") se recodifican para que puntuaciones altas siempre indiquen presencia alta de la variable.
- **Detección de valores atípicos** (outliers): puntajes que superan ±3 desviaciones estándar de la media, o se identifican con boxplot. Se decide si se conservan, se transforman o se excluyen (con justificación).
- **Verificación de consistencia**: puntajes fuera del rango posible de la escala (ej. un 7 en una Likert de 1-5) se corrigen o se marcan.

Sin esta declaración, 3.8 queda incompleto. La skill que redacte 3.8 sin limpieza está omitiendo un momento obligatorio.

### Estadística descriptiva (segundo momento)

Para cada variable y cada dimensión:

- **Frecuencias** y **porcentajes** (variables categóricas o niveles).
- **Medias** y **desviaciones estándar** (variables continuas o sumatorios Likert).
- **Medianas** y **rangos intercuartílicos** (si la distribución es asimétrica).

### Pruebas de normalidad (paso previo a la inferencial)

Determinan si los datos siguen distribución normal, lo que define si la inferencial será paramétrica o no:

- **Kolmogorov-Smirnov**: muestras grandes (n > 50).
- **Shapiro-Wilk**: muestras pequeñas (n ≤ 50).

Si p > 0.05, los datos son normales → pruebas paramétricas (Pearson, t-Student, ANOVA).
Si p ≤ 0.05, los datos no son normales → pruebas no paramétricas (Spearman, U de Mann-Whitney, Kruskal-Wallis).

### Estadística inferencial (tercer momento) según nivel

#### Correlacional simple

- **Coeficiente de Pearson** (r): cuando los datos son normales y la relación es lineal.
- **Coeficiente de Spearman** (ρ): cuando los datos no son normales o son ordinales.

Interpretación de magnitud:
- |r| < 0.30: correlación baja.
- 0.30 ≤ |r| < 0.50: correlación moderada.
- 0.50 ≤ |r| < 0.70: correlación alta.
- |r| ≥ 0.70: correlación muy alta.

#### Correlacional causal / predictivo

- **Regresión lineal simple** (1 predictor): cuando hay una variable predictora.
- **Regresión lineal múltiple** (varios predictores): cuando hay varias variables predictoras.
- **Regresión logística**: cuando la variable dependiente es dicotómica.

#### Explicativo con modelo estructural

- **PLS-SEM** (Hair y colaboradores, con la clave de su obra en la biblioteca): para modelos con varias variables latentes y relaciones complejas.
- **CB-SEM**: si la población es grande y las variables son continuas con distribución normal.

#### Comparativo

- **t-Student**: dos grupos independientes con datos normales.
- **U de Mann-Whitney**: dos grupos independientes con datos no normales.
- **ANOVA**: tres o más grupos con datos normales.
- **Kruskal-Wallis**: tres o más grupos con datos no normales.

### Nivel de significancia

Estándar en pregrado peruano: **p < 0.05**.

Más estricto: p < 0.01.

### Software referencial

- **SPSS**: muy común en pregrado peruano.
- **R con RStudio**: gratuito, potente, recomendado por el método de Acosta IA Research.
- **JASP**: gratuito y con interfaz visual, alternativa a SPSS.
- **SmartPLS**: para PLS-SEM.

## Si enfoque cualitativo

### Codificación

- **Codificación abierta**: identificar conceptos y propiedades en los datos brutos.
- **Codificación axial**: agrupar códigos en categorías y establecer relaciones.
- **Codificación selectiva**: identificar la categoría central que articula la teoría (solo si teoría fundamentada).

### Análisis temático vs análisis de contenido

- **Análisis temático**: identifica temas recurrentes en los datos.
- **Análisis de contenido**: cuantifica la frecuencia de aparición de categorías.

### Software referencial

- **ATLAS.ti**: software comercial, muy potente.
- **NVivo**: software comercial, alternativa a ATLAS.
- **Codificación manual con matrices en Excel**: válido para pregrado con muestras pequeñas.

### Triangulación

Para fortalecer la validez:

- **Triangulación de fuentes**: comparar datos de distintos participantes o documentos.
- **Triangulación de investigadores**: dos o más codificadores independientes.
- **Triangulación teórica**: interpretar datos desde varias perspectivas teóricas.

## Plantilla de redacción

### Si cuanti

> Los datos recogidos se procesarán mediante técnicas de estadística descriptiva e inferencial. En el plano descriptivo, se calcularán frecuencias y porcentajes para los niveles de cada variable y dimensión, así como medias y desviaciones estándar para las puntuaciones globales de las escalas Likert.
>
> Antes de aplicar pruebas inferenciales, se evaluará la distribución de los datos mediante la prueba de Kolmogorov-Smirnov (dado que la muestra es superior a 50 participantes). Si los datos siguen distribución normal (p > 0.05), se aplicará el coeficiente de correlación de Pearson para evaluar las hipótesis. En caso contrario, se utilizará el coeficiente de correlación de Spearman [AR…].
>
> El nivel de significancia adoptado es p < 0.05, estándar en investigación educativa cuantitativa [AR…]. El procesamiento se realizará con [SPSS / R con RStudio / JASP], según disponibilidad del tesista. La ejecución detallada de los análisis se desarrollará en el Capítulo VII con la Skill de Análisis de Datos del método.

### Si cuali

> Los datos recogidos mediante entrevistas serán transcritos y analizados con técnicas propias del enfoque cualitativo. Se aplicará codificación abierta para identificar conceptos emergentes, seguida de codificación axial para agrupar códigos en categorías. [Si es teoría fundamentada: y codificación selectiva para identificar la categoría central].
>
> Para fortalecer la validez interpretativa se aplicará triangulación de fuentes mediante la comparación de datos de distintos participantes. El procesamiento se realizará con [ATLAS.ti / NVivo / codificación manual en matrices Excel], según disponibilidad del tesista.

## Reglas críticas

- **NO ejecutar análisis estadísticos** aquí. Solo describir las técnicas que se usarán.
- **Citar autor** para cada técnica (Pearson, Spearman, Hair, Hernández-Sampieri) con la clave de su obra en la biblioteca, buscada con `buscar_fuentes`. Si no está, se le pide al tesista que la agregue y mientras tanto la afirmación va con `[FALTA FUENTE]`. Las plantillas de abajo muestran dónde va cada clave `[AR…]`: es un marcador, en el texto real va la clave que devolvió la búsqueda.
- **Coherencia con el nivel**: si el nivel es correlacional, no proponer regresión múltiple. Si es explicativo, sí.
- **Cerrar con remisión a la Skill 7**: "La ejecución detallada se desarrolla en la Skill de Análisis con RStudio".
