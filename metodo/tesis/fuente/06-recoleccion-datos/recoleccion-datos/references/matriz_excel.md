# Matriz de datos en Excel

Estructura del archivo `06_Matriz_datos.xlsx` que la skill genera para que el tesista registre las respuestas del trabajo de campo.

## Tres hojas obligatorias

### Hoja 1 — Codebook

Diccionario de variables. Define cada columna de la matriz: qué representa, qué valores acepta, cómo se interpreta.

Estructura genérica (el codebook REAL depende de los datos sociodemográficos que declaró el Cap III y del instrumento de la Skill 5):

| Código | Nombre de la variable | Tipo | Valores válidos | Descripción |
|--------|----------------------|------|-----------------|-------------|
| ID | Identificador del participante | Texto | P001 a P### | Código único, no se repite |
| [SOCIO_1] | [nombre del primer dato sociodemográfico] | [tipo] | [valores según Cap III] | [descripción] |
| [SOCIO_2] | [nombre del segundo dato] | [tipo] | [valores] | [descripción] |
| ... | ... | ... | ... | ... |
| ITEM_01 | Ítem 1 del cuestionario | Numérico | [1-N según escala del instrumento] | [Likert 1-5 acuerdo / frecuencia / 1-7 según instrumento] |
| ... | ... | ... | ... | ... |
| ITEM_[N] | Ítem [N] del cuestionario | Numérico | [1-N] | [según escala] |

**Advertencia crítica de uso**: los campos sociodemográficos y el número de ítems **NO son fijos**. Dependen de:
- La operacionalización del Cap III (qué datos sociodemográficos se declaran: grado, edad, sección, sexo, cargo, área, antigüedad, servicio, según carrera).
- La versión final del instrumento (número real de ítems tras juicio de expertos y pilotaje).

Si dos tesistas reciben la MISMA estructura de codebook con las MISMAS columnas específicas (GRADO, SECCION, EDAD, 38 ítems), se detecta clonación. La skill debe **derivar la estructura del Cap III y del instrumento reales del tesista actual**, no copiar la del ejemplo.

Notas en el Codebook:
- El campo ID se genera al asignar el participante (P001, P002, etc.), no se modifica después.
- Los nombres reales NO se incluyen en la matriz. Si el tesista necesita rastreabilidad, mantiene una lista de equivalencias por separado, en archivo cifrado con acceso restringido.

### Hoja 2 — Datos

La matriz propiamente dicha. Cada fila es un participante, cada columna un ítem.

Estructura (adaptada a la carrera y al instrumento del tesista, no copiar literal):

| ID | [SOCIO_1] | [SOCIO_2] | [SOCIO_3] | ITEM_01 | ITEM_02 | ... | ITEM_[N] |
|----|-----------|-----------|-----------|---------|---------|-----|----------|
| P001 | | | | | | | |
| P002 | | | | | | | |
| ... | | | | | | | |

La skill genera N filas (donde N = tamaño muestral declarado en el Cap III) pre-rellenadas con los IDs P001, P002, ..., P###. El tesista solo llena las celdas con valores.

### Hoja 3 — Validación

Hoja que ejecuta validaciones automáticas con fórmulas. Detecta errores comunes en el registro.

Estructura:

| Verificación | Fórmula | Resultado |
|--------------|---------|-----------|
| Total participantes | =COUNTA(Datos!A2:A1000) | [valor] |
| IDs duplicados | =SUMPRODUCT((COUNTIF(Datos!A2:A1000,Datos!A2:A1000)>1)*1)/2 | 0 = OK |
| Valores fuera de rango (Likert) | fórmula que detecta cualquier valor < 1 o > 5 en columnas ITEM_* | 0 = OK |
| Filas completamente vacías | conteo de filas donde todas las celdas están vacías | 0 = OK |
| Grados fuera de rango | =SUMPRODUCT((Datos!B2:B1000<4)*(Datos!B2:B1000>0))+SUMPRODUCT((Datos!B2:B1000>5)*1) | 0 = OK |

Una columna adicional al lado de cada verificación con texto "OK" si pasa o "REVISAR" si no.

## Reglas críticas del registro

### Codificación

- **Códigos únicos**: cada participante tiene un ID irrepetible. La skill propone formato P001, P002... pero el tesista puede usar otro (E_4A_01 = estudiante 4° A, primer participante).
- **No usar nombres**: nunca registrar nombre, DNI, correo o datos identificables en la matriz de datos.
- **Si el cuestionario es virtual** (Google Forms): exportar como CSV, abrir en Excel, asignar IDs, eliminar la columna "marca temporal" o "correo" (si por error quedó activada).

### Errores típicos a evitar

1. **Filas en blanco intercaladas**: si un participante abandona, su fila queda con menos respuestas pero NO se elimina ni se deja en blanco completamente. Se marca con un código de descarte (D001) y se reporta en bitácora.
2. **Valores fuera de rango**: un 6 o un 0 en una escala 1-5 indica error de digitación. La hoja de validación lo detecta.
3. **Duplicados de ID**: si por error se asigna el mismo ID a dos participantes, la validación lo detecta.
4. **Inconsistencia de tipo**: texto en columnas numéricas. Excel lo permite pero rompe los análisis.

### Backup

- Guardar dos copias: una local cifrada (con contraseña), otra en nube institucional.
- NUNCA confiar en una sola copia.
- Hacer backup diario durante el periodo de aplicación.

## Convención de naming

Ejemplo genérico (ADAPTAR AL INSTRUMENTO REAL del tesista, no copiar literal):

Si el cuestionario tiene [N] ítems totales organizados en dos variables:
- ITEM_01 a ITEM_[X]: V1 ([X] ítems)
- ITEM_[X+1] a ITEM_[N]: V2 ([N-X] ítems)

Opcional: agregar prefijo de variable y dimensión
- V1_D1_01: Variable 1, Dimensión 1, ítem 1
- V2_D3_02: Variable 2, Dimensión 3, ítem 2

Los números [N], [X], las variables y dimensiones se toman del **instrumento real** validado por Skill 5, NO se copian del ejemplo.

La skill consulta al tesista qué convención prefiere antes de generar la matriz.

## Frontera con Skill 7

Esta skill entrega la MATRIZ VACÍA estructurada. La Skill 7 (Análisis de Datos con RStudio):

- Recibe la matriz con los datos ya llenados por el tesista.
- Ejecuta limpieza adicional si quedan errores.
- Calcula descriptivas (frecuencias, medias, desviaciones).
- Calcula confiabilidad (alfa de Cronbach).
- Aplica pruebas inferenciales (Pearson, Spearman, según normalidad).
- Reporta resultados.
