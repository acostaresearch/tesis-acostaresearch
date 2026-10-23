# La Matriz de Estrategia en Excel

Se lee en el Paso 9, con todo el contenido ya decidido. La matriz se genera
**siempre** con `scripts/matriz_excel.py` (Python con `openpyxl`, sin rutas
fijas). No se arma a mano ni con otra plantilla: así sale idéntica en cualquier
sesión y con cualquier modelo.

```bash
S=scripts/matriz_excel.py                  # dentro de la carpeta de esta skill
python3 $S --ejemplo <tipo> > matriz.json  # cuantitativo | secundarios | cualitativo | escala | mixto | revision
python3 $S --json matriz.json --out MATRIZ_[clave].xlsx
```

`--ejemplo` imprime el JSON completo de ese tipo, con el formato exacto de cada
clave (también `pendientes`: objetos `{pendiente, quien, como}`); se reemplaza
cada `<...>`. Si el archivo ya existe, el script guarda `MATRIZ_[clave]_v2.xlsx`
(y así) sin pisar la anterior. Sale con ✗ y sin escribir si falta el objetivo
general, si hay más de 5 específicos, si queda una celda vacía o un `<...>`, o
si una fila de la hoja 3 no tiene el número de columnas del tipo.

## Las cinco hojas (fijas, en este orden)

Encabezados en negrita, primera fila congelada, filtros, ajuste de texto, sin
celdas combinadas.

| Hoja | Contenido | Clave del JSON |
|---|---|---|
| 1 · Diseño y muestra (en revisiones: Diseño de la revisión) | Dos columnas, Campo y Contenido, con los campos fijos del tipo. Un campo sin dato sale `[POR CONFIRMAR: ...]` y avisa | `diseno` |
| 2 · Objetivos | El general en la primera fila (`nivel: "General"`), luego OE1 a OE4 (OE5 se acepta con aviso). Es también el chequeo de coherencia del Paso 8 | `objetivos`, `nota_objetivos` |
| 3 · Operacionalización (en revisiones: Variables de extracción) | Columnas según el tipo (abajo) | `operacionalizacion` (en revisiones, `variables_extraccion`): lista de filas |
| 4 · Papers de referencia | Una fila por artículo del Paso 3, nota con la fecha de búsqueda. Celda sin dato: "no consta en el resultado" | `papers`, `fecha_busqueda` |
| 5 · Pendientes | Los declarados más todos los `[POR CONFIRMAR]` de las hojas 1 a 4, que el script reúne solo. Si no hay: "No quedaron pendientes" | `pendientes` |

### Hoja 1 con datos secundarios: claves propias

`enfoque`, `diseno_especifico`, `fuente_datos`, `acceso` (enlace, fecha de
descarga, versión), `periodo` (año u ola), `unidad_analisis`, `poblacion`,
`diseno_muestral`, `ponderador`, `variables_base`, `diccionario`, `filtros`,
`perdidos`, `licencia`, `termino_unificador` y `etica`. Clave sin dato →
`[POR CONFIRMAR]` y a Pendientes; clave desconocida → ✗.

### Hoja 2: qué significan `unidad` y `medio`

| Tipo | Columna "hipotesis" | `unidad` | `medio` |
|---|---|---|---|
| cuantitativo | Hipótesis | Variables | Instrumento |
| secundarios | Hipótesis | Variables | Fuente y variable de la base |
| escala | Modelo de medida esperado | Escala y dimensiones | Instrumento (versión original) |
| cualitativo | Hipótesis ("no aplica") | Categorías | Técnica e instrumento |
| mixto | Hipótesis (solo rama cuanti) | Variables o categorías | Instrumento o técnica |
| revision | Hipótesis ("no aplica") | Criterio de elegibilidad | Variable de extracción |

En diseños sin hipótesis, la columna dice **"no aplica"** en todas las filas y
`nota_objetivos` explica el motivo en una línea. No se borra la columna: quien
reciba la matriz tiene que ver que la decisión fue deliberada.

### Hoja 3: columnas por tipo

| Tipo | Columnas |
|---|---|
| cuantitativo | Variable (acrónimo) · Papel · Definición conceptual (fuente) · Definición operacional · Dimensiones · Indicadores · Escala de medición · Instrumento propuesto (autor, año, ítems) · Estado |
| secundarios | Variable (acrónimo) · Papel · Definición conceptual (fuente) · Variable(s) de la base (código) · Módulo, año u ola · Construcción o recodificación · Escala de medición · Fuente de datos · Estado |
| escala | Escala y versión original (autor, año) · Dimensión · N.º de ítems · Formato de respuesta · Idioma original · Propiedad a examinar · Estado |
| cualitativo | Categoría · Subcategorías · Indicadores observables · Técnica · Instrumento · Origen (previa o emergente) · Estado |
| mixto | Rama (cuanti o cuali) · Variable o categoría · Papel · Definición conceptual (fuente) · Definición operacional o subcategorías · Indicadores · Escala o técnica · Instrumento propuesto (autor, año) · Estado |
| revision | Variable de extracción · Qué se registra · Pregunta que responde · Estado |

## Reglas del contenido

1. **Ninguna celda vacía.** O tiene dato, o `[POR CONFIRMAR: ...]`, o "no aplica
   a este diseño". El script lo exige.
2. **Nada de relleno.** Si el diseño no lleva hipótesis, no se inventan.
3. **Cada dato con su fuente** donde corresponde: definiciones, instrumentos,
   bases, papers; con su clave (`[F012]`, `[AR51541814]`) si ya la tiene.
4. **Sin datos personales.** La autoría entra en la Fase 8.
5. **Frases, no párrafos.** Más de dos líneas en una celda: se resume, el
   desarrollo es de la fase que corresponde.
