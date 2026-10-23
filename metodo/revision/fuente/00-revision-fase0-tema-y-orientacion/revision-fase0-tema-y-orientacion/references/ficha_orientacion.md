# Ficha de Orientación: contenido y topes

Se lee en el Paso 7. La Fase 0 entrega `FICHA_[clave].docx` y
`REVISTA_[clave].json` (Paso 5h); el investigador sube los dos en cada fase.

**Cómo se construye:** siempre rellenando la plantilla de `assets/` que indica
el Paso 7 y pasándola por `scripts/articulo_docx.py nuevo`. Comandos en el
Paso 7 del SKILL.md; sintaxis del motor en `formato_docx.md`.

## Límite duro: dos páginas, 700 palabras

No es un informe: es una hoja de consulta que se mira de un vistazo.

1. **Todo va en tablas.** La prosa se reserva para la frase del tema y tres
   líneas de lectura de antecedentes.
2. **Máximo 15 palabras por celda.**
3. **Máximo 700 palabras**, contadas con `articulo_docx.py contar ficha.md`
   antes de construir (cuenta también las tablas). Si se pasa, se recortan filas
   y celdas; no se achica la letra ni los márgenes.

No va en la ficha, aunque se haya conversado: qué exige el tipo de estudio, por
qué encaja cada revista, el razonamiento de la elección, la lista de fases (se
muestra en el chat) ni párrafos de transición.

**Sin cabecera de datos:** abre con `FICHA DE ORIENTACIÓN DEL ARTÍCULO` y entra
a la sección 1. Sin portada, nombre, filiación, correo, logotipo ni fecha de
emisión. Las únicas fechas son las de consulta, en las notas de tabla.

## Las ocho secciones (las mismas de la plantilla)

| Sección | Contenido | Tope |
|---|---|---|
| 1. Perfil (Tabla 1) | Área y especialidad, tipo de revisión y guía, destino elegido | 3 filas |
| 2. Tema | La frase confirmada en el Paso 3c, sin huecos | 1 frase |
| 3. Pregunta y criterios (Tabla 2) | Pregunta de revisión; criterios preliminares de inclusión y exclusión | 4 filas |
| 4. Palabras clave | Español e inglés | 2 líneas |
| 5. Antecedentes (Tabla 3) | Autor y año, título, revista, qué encontró (o "solo título"; en revisiones, tipo, bases y periodo), enlace; nota con fecha de búsqueda; lectura de lo abierto | 6 filas + 3 líneas |
| 6. Revistas candidatas (Tabla 4) | Índice y cuartil (categoría, año), cobertura y vigencia, acceso y APC, verificación, encaje; nota con fuente, año y fecha de consulta; una línea por cada candidata con señales de alarma | 4 filas |
| 7. Revista destino y perfil (Tabla 5) | Resumen de `REVISTA_[clave].json`: elegida con su cuartil (o el pendiente a la vista), alternativas, cita, estructura, límite, resumen, idioma y formato, campos por confirmar; tasa de aceptación y pronóstico de encaje | 8 filas + 2 líneas |
| 8. Pendientes y siguiente paso | `[POR CONFIRMAR]` y la fase siguiente | 6 pendientes + 2 líneas |

En la nota de la Tabla 4 se dice quién consultó el indicador: *consultado el
[fecha]* o *consultado por el investigador el [fecha]* si los datos los pegó él.

## Reglas

1. **Nada sin fuente.** Cada dato de revista con su año y fecha de consulta;
   cada antecedente con el enlace que devolvió la búsqueda.
2. **`[POR CONFIRMAR]` solo para datos externos** (indicadores, APC, guía de
   autores, comité de ética). Población, carrera, ámbito y año se preguntan.
3. **Sin datos personales.** La autoría entra en la Fase 8.
4. **Una sección que no aplica se reemplaza**, no se rellena.
5. **Ningún `{...}` puede quedar en el .md** antes de construir.
