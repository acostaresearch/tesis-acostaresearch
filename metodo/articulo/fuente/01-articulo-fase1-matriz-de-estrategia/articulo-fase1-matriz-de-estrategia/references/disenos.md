# Diseños de investigación

Se lee en el Paso 2 (y la tabla de análisis, en el Paso 8). Para cada diseño:
qué exige, qué objetivos admite, si lleva hipótesis y qué análisis le
corresponde. Ningún diseño es el "normal": SEM es uno entre varios.

Regla al presentarlos: **describir lo que exige, no prometer resultados**, y no
afirmar tasas de aceptación ni tiempos de revisión de ningún diseño.

---

## Medir variables

### Descriptivo
Mide el nivel o la frecuencia de una o más variables. No vincula.

- **Objetivos**: describir, identificar, caracterizar.
- **Hipótesis**: normalmente no. Forzarlas produce hipótesis huecas del tipo "el
  nivel es alto".
- **Análisis**: frecuencias, medias, desviaciones.
- **Advertencia honesta**: solo, rara vez pasa revisión en revista indexada.
  Ofrecer convertirlo en correlacional agregando una segunda variable.

### Correlacional
Examina cómo se vinculan dos o más variables sin manipular ninguna.

- **Objetivos**: determinar la relación, establecer la asociación.
- **Hipótesis**: sí, de asociación. **Nunca con lenguaje causal.**
- **Análisis**: correlación de Pearson o Spearman según normalidad; χ² si las
  dos son categóricas. Si compara grupos (sexo, institución), t o ANOVA y sus
  alternativas no paramétricas.
- **Cuidado con el término**: aquí se dice *relación* o *asociación*, no
  *influye* ni *efecto*.

### Predictivo o de regresión
Estima en qué medida unas variables predicen otra.

- **Objetivos**: determinar en qué medida X predice Y.
- **Hipótesis**: sí, direccionales.
- **Análisis**: según la variable dependiente: lineal (continua), logística
  (sí/no), ordinal o multinomial (categorías), Poisson o binomial negativa
  (conteos); **multinivel** si los casos están anidados (alumnos en escuelas);
  **panel** o series si son los mismos casos en varios años. Supuestos
  verificados.

### Modelo estructural (PLS-SEM o CB-SEM)
Pone a prueba un modelo completo de relaciones entre constructos latentes.

- **Objetivos**: explicar, contrastar el modelo, determinar el efecto directo e
  indirecto.
- **Hipótesis**: sí, una por trayectoria. Mediación y moderación se declaran
  aparte.
- **Análisis**: modelo de medida (fiabilidad, validez convergente y
  discriminante) y modelo estructural (coeficientes, R², efectos).
- **Exige**: escalas validadas para cada constructo, muestra suficiente para el
  número de trayectorias, y **teoría que justifique la dirección**. Sin teoría,
  el revisor lo lee como una corazonada con estadística encima.
- **PLS-SEM y CB-SEM no son intercambiables.** La elección se justifica; si el
  investigador no sabe cuál, se le explica y **se verifica cuál usa la
  literatura de su campo** en los papers del Paso 3, en vez de decidir por él.

---

## Probar si algo funciona

### Preexperimental
Un solo grupo, con medición antes y después, o solo después.

- **Objetivos**: determinar el cambio tras la intervención.
- **Hipótesis**: sí, pero **lo que se puede afirmar es muy limitado**: sin grupo
  de comparación no se puede atribuir el cambio a la intervención. Decirlo antes
  de que diseñe, no después.
- **Análisis**: prueba para muestras relacionadas.

### Cuasiexperimental
Dos grupos sin asignación aleatoria.

- **Objetivos**: determinar el efecto de la intervención.
- **Hipótesis**: sí, direccionales.
- **Análisis**: comparación entre grupos, y de preferencia control de las
  diferencias iniciales.
- **Exige**: justificar por qué no hubo aleatorización y reconocer el sesgo de
  selección en limitaciones.

### Experimental puro
Dos o más grupos con asignación aleatoria.

- **Objetivos**: determinar el efecto causal.
- **Hipótesis**: sí, y es el único diseño de esta lista donde el lenguaje causal
  es legítimo.
- **Exige**: aleatorización documentada, y casi siempre aprobación de comité de
  ética. Algunas revistas piden registro previo del ensayo. Preguntar qué exige
  la revista destino en vez de suponerlo.

---

## Entender experiencias

Fenomenológico, estudio de caso, teoría fundamentada e investigación-acción.

- **Objetivos**: comprender, explorar, interpretar, describir el proceso.
- **Hipótesis**: **no.** Un cualitativo no formula hipótesis sustantivas.
  Ponerlas es la señal más clara de que se copió una plantilla cuantitativa, y
  un revisor lo detecta en la primera página.
- **En la matriz**, la columna de hipótesis dice "no aplica" y las variables se
  reemplazan por **categorías de análisis**: categoría, subcategorías,
  indicadores observables, técnica e instrumento (guía de entrevista, matriz de
  observación).
- **Exige**: muestreo por criterio hasta saturación, consentimiento informado y,
  cuando hay grabación, permiso explícito.
- **En la ruta**: recorre las fases 0 a 9; la Fase 3 va sin hipótesis y Métodos
  y Resultados se organizan por categorías.

---

## Mixto

Una rama cuantitativa y una cualitativa (secuencial explicativo, secuencial
exploratorio o convergente). Cada rama se arma con sus propias reglas de este
archivo, y la matriz dice en qué orden se recogen y cómo se integran. Las
hipótesis solo van en la rama cuantitativa.

---

## Con datos secundarios

No es un diseño aparte: cualquiera de los de "Medir variables" puede hacerse
con una base existente (encuesta nacional, evaluación internacional, registro
administrativo, datos abiertos, panel, serie).

- **En la matriz** (tipo `secundarios`): en vez de instrumento, la fuente de
  datos, la variable de la base con su código, el año u ola, el diccionario,
  el factor de expansión y la licencia.
- **Exige**: que la base tenga variables que representen de verdad los
  constructos (si no, se cambia la pregunta, no se fuerza la variable) y, en
  encuestas con diseño complejo, analizar con el diseño muestral y los pesos.
- **Ética**: suele estar exenta por ser anónima y pública; se declara igual.

---

## Validación de escala (propiedades psicométricas)

Adapta o valida un instrumento en una población nueva. **Es un diseño propio, no
un correlacional con extras.**

- **Objetivos**, y son estos, no otros: analizar la estructura interna (factorial
  exploratoria o confirmatoria), estimar la fiabilidad (consistencia interna y,
  si aplica, estabilidad), examinar la validez convergente y discriminante, y
  cuando el estudio lo permite, evaluar la invarianza de medición entre grupos.
- **Hipótesis**: **no lleva hipótesis sustantivas.** Lleva un modelo de medida
  esperado, que es otra cosa: se espera que los ítems carguen en tales factores.
  Confundirlo con hipótesis de relación entre variables es un error frecuente y
  visible.
- **En la matriz**, la operacionalización se invierte: la unidad no es la
  variable sino **la escala y sus dimensiones**, con número de ítems, formato de
  respuesta y versión original con su autor.
- **Exige**: la escala original con permiso de uso cuando corresponde,
  traducción y retrotraducción si viene de otro idioma, juicio de expertos, y
  una muestra adecuada para el análisis factorial previsto.
- **Advertencia útil**: mucha gente llega aquí sin querer, porque su variable no
  tenía instrumento. Si ese es el caso, decirlo claro: **el estudio cambió de
  naturaleza** y ahora el aporte es el instrumento, no la relación que quería
  probar.

Si el investigador pide una revisión sistemática, de alcance o bibliométrica:
ese tipo de artículo está en el otro paquete, la **Ruta del Artículo de
Revisión**.

---

## Cómo elegir cuando no sabe

No preguntarle el nombre del diseño. Preguntarle qué quiere saber:

| Lo que quiere saber | Diseño |
|---|---|
| Cuánto hay de algo | Descriptivo |
| Si dos cosas van juntas | Correlacional |
| Si dos o más grupos difieren | Comparativo |
| Cuánto predice una a otra | Predictivo (regresión) |
| Lo mismo con casos anidados o en varios años | Multinivel o panel |
| Cómo funciona un sistema de constructos latentes | Modelo estructural |
| Si una intervención sirve | Experimental, cuasi o pre |
| Cómo lo viven las personas | Cualitativo |
| Si un cuestionario mide bien | Validación de escala |

Y la pregunta de realidad que ahorra disgustos: **a cuántos casos tiene acceso y
en cuánto tiempo** (o si existe una base que ya los tenga). Si el acceso es
limitado, se simplifica el diseño ahora.

## Qué análisis según la pregunta (Paso 8)

| Pregunta | Análisis previsto |
|---|---|
| Describir | Frecuencias, M, DE (con pesos si la base los trae) |
| Relación entre dos variables | Pearson o Spearman; χ² o Fisher si son categóricas |
| Comparar 2 grupos / 3 o más | t o U de Mann-Whitney / ANOVA o Kruskal-Wallis |
| Antes y después | t pareada o Wilcoxon; ANOVA mixto con grupo control |
| Predecir algo continuo | Regresión lineal múltiple |
| Predecir sí/no · categorías ordenadas · conteos | Logística · ordinal o multinomial · Poisson o binomial negativa |
| Casos anidados | Multinivel |
| Mismos casos en varios años · evolución | Panel (efectos fijos o aleatorios) · series de tiempo |
| Mediación o moderación | Regresión con interacción o efecto indirecto con bootstrap |
| Modelo con constructos latentes | PLS-SEM o CB-SEM |
| Validar una escala | AFE, AFC, fiabilidad, invarianza |

Detalle y código en `analisis.md` (fases 4, 5 y 9). Aquí solo se nombra el
análisis y se comprueba que responde la pregunta.
