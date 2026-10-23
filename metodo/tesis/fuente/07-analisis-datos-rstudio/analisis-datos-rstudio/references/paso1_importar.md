# Paso 1 — Importar y revisar los datos

## Variantes según formato del archivo

### Excel (.xlsx) — el más común en pregrado peruano

R:
```r
library(readxl)
datos <- read_excel("matriz_datos.xlsx", sheet = "Datos")
```

SPSS:
```
Archivo > Abrir > Datos
   → Selecciona archivo .xlsx
   → Marca "La primera fila contiene nombres de variables"
```

### CSV (descargado de Google Forms)

R:
```r
library(readr)
datos <- read_csv("matriz_datos.csv", locale = locale(decimal_mark = ","))
```

SPSS:
```
Archivo > Importar datos > CSV
   → Selecciona el separador (coma o punto y coma)
   → Verifica los tipos de variables
```

### Archivo SPSS (.sav) cuando se cambia a R

R:
```r
library(haven)
datos <- read_sav("matriz_datos.sav")
```

## Lo que el tesista debe pegar al chat

Después de ejecutar, copiar del output:

```
Lo siguiente:
- Número total de filas (debe coincidir con n declarado en Cap III)
- Número de columnas
- Nombres de las primeras 5-10 columnas
- Si hay valores faltantes (NA), cuántos
- Cualquier error o warning
```

## Validaciones que la skill aplica

### Validación 1: n declarado vs n real

Si el Cap III declara n = 100 pero la matriz tiene 87 filas con datos, la skill pregunta:

- ¿La diferencia es por no respuesta?
- ¿Hubo participantes que abandonaron?
- ¿Se debe actualizar el n declarado en Cap III?

Documentar la respuesta en la bitácora (Skill 6) y reportar n real en el Cap de Resultados.

### Validación 2: nombres de columnas

Verificar que los nombres coincidan con el codebook de la matriz. Si la convención fue V1_D1_01 ... V2_D7_02, debe haber 38 columnas de ítems + variables sociodemográficas.

### Validación 3: tipos de variables

- ID debe ser texto.
- GRADO, SECCION, EDAD: numéricas o categóricas.
- ITEM_01 a ITEM_38 (o V1_D1_01...): numéricas en rango 1-5 (si Likert 1-5).

Si algún ITEM tiene valores fuera de rango o tipo incorrecto, NO avanzar al Paso 2. Volver a Skill 6 a corregir la matriz.

## Caso especial: datos perdidos (NA)

Si hay valores faltantes:

R:
```r
# Cuántos NA por columna
sapply(datos, function(x) sum(is.na(x)))

# Si los NA son pocos (<5%): eliminar filas con NA
datos_limpio <- na.omit(datos)

# Si son muchos: imputar (consultar al asesor antes)
```

SPSS:
```
Transformar > Reemplazar valores perdidos
```

NO imputar sin justificación metodológica documentada en el Cap III.

## Errores frecuentes en este paso

1. **Ruta de archivo incorrecta**: usar `setwd()` en R o copiar archivo a la carpeta del proyecto.
2. **Encoding mal interpretado**: si aparecen caracteres raros en lugar de tildes, agregar `locale = locale(encoding = "UTF-8")` en `read_csv()`.
3. **Columnas con espacios en el nombre**: usar comillas inversas `` `nombre con espacios` `` o renombrar antes.
4. **Hoja Excel equivocada**: especificar `sheet = "Datos"` explícitamente.
