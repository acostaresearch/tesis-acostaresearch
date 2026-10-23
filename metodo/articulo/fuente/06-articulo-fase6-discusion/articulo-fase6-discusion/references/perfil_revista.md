# Perfil de la revista: escribir con su norma desde el principio

El artículo se escribe **desde la Fase 2 con la norma, el estilo de cita, la
estructura y el formato de la revista destino**. No se deja para el final: un
manuscrito armado en APA y convertido a Vancouver en la Fase 8 arrastra
errores en cada cita.

Para eso la Fase 0 deja un archivo `REVISTA_[clave].json` que leen todas las
fases. Si hay rechazo, la Fase 8 arma un perfil nuevo para la revista
siguiente y parte del **respaldo neutro**.

## De dónde salen los datos

De la **guía de autores** (Author guidelines, Instructions for authors, Normas
para autores) de la revista elegida, en su sitio oficial. Una sola lectura:

1. Buscar la guía (búsqueda web o el enlace que dé el investigador) y leerla
   **una vez** completa. Si no carga, pedir al investigador que pegue el texto o
   suba el PDF de la guía; no se reintenta. Si después falta un dato puntual
   (p. ej. el límite de palabras), se permite **una** lectura dirigida a ese
   dato antes de dejarlo `[POR CONFIRMAR]`.
2. Rellenar el perfil con `articulo_docx.py perfil plantilla` como base.
3. Todo campo que la guía no diga va a `"por_confirmar"` con el valor neutro de
   la ruta. Nunca se inventa una norma.
4. Validar: `articulo_docx.py perfil validar REVISTA_[clave].json`.
5. Mostrar al investigador un resumen de seis líneas (cita, estructura, límite,
   resumen, formato, tablas y figuras) y pedir confirmación en un mensaje.

## Campos

| Campo | Qué buscar en la guía | Si no lo dice |
|---|---|---|
| `estilo_cita` | APA 7, Vancouver, IEEE, Chicago, Harvard, propio | Preguntar; nunca suponer |
| `idioma` | Idiomas que acepta; si pide el manuscrito en inglés | `es` |
| `estructura` | Secciones y su título exacto (Method/Métodos, Results and Discussion juntos…) | IMRyD de la ruta |
| `estructura_en` | Títulos en inglés si la revista es bilingüe o publica en inglés | Traducción literal en la Fase 8 |
| `limite_palabras`, `limite_cuenta` | Palabras máximas y si incluye referencias, tablas, resumen | `[POR CONFIRMAR]` |
| `resumen` | Estructurado o no, máximo de palabras, idiomas | No estructurado, 250 |
| `palabras_clave` | Cuántas, si deben venir de un tesauro (UNESCO, MeSH) | 3 a 5 |
| `titulo_max_palabras` | Límite del título | 20 |
| `tablas`, `figuras` | En el texto o al final; formatos de figura | En el texto |
| `anonimizar` | Revisión doble ciego, página de título aparte | Sí |
| `formato` | Fuente, tamaño, interlineado, márgenes, alineación, sangría, numeración de líneas y páginas, estilo de títulos | Neutro de la ruta (Times 12, 1.5, 2.54 cm) |

## Cómo se usa en cada fase

- **Citas y referencias**: desde la Fase 2, en el `estilo_cita` del perfil
  (reglas en `estilos_cita.md`).
- **Títulos de sección**: los de `estructura`, con su redacción exacta.
- Si la revista no tiene sección propia de revisión de la literatura (marco
  teórico), la Fase 3 la escribe igual como sección propia y la Fase 8 la baja
  a subsecciones de la Introducción con `ajustar_docx.py` (ver abajo).
- **Word**: todas las llamadas al motor llevan `--perfil REVISTA_[clave].json`.
  El motor produce dos archivos con el mismo texto:
  - `ARTICULO_[clave]_vN.docx` — con el formato de la revista;
  - `ARTICULO_[clave]_vN_RESPALDO.docx` — con el formato neutro de la ruta.
- **Límite de palabras**: `verificar --perfil` lo controla en cada fase. La
  Fase 7 avisa si el total proyectado se pasa.

## Reubicar secciones cuando el perfil lo pide

Con `ajustar_docx.py` (Fase 8): `nivel --seccion "Revisión de la literatura"
--nivel 2` la baja a subsección (con sus subtítulos) y `mover --seccion ...
--antes-de "Método"` la deja al final de la Introducción; `unir --primera
Resultados --segunda Discusión --titulo "Resultados y discusión"` junta dos
secciones; `renombrar` cambia un título. Antes de la Fase 8 no se reubica:
`verificar` solo avisa.

## Si hay rechazo

En la Fase 8 (rama *reenvío*): se elige la revista siguiente, se arma su
perfil, y se aplica sobre la última versión de **RESPALDO** con
`normalizar ARTICULO_[clave]_vN_RESPALDO.docx --perfil REVISTA_[nueva].json`.
Si el artículo se escribió con citas por clave, ese mismo `normalizar` (con
`--fuentes inventario.json`) reconvierte citas y referencias al estilo nuevo;
si no, se convierten a mano antes de aplicar el formato (`fuentes_y_citas.md`).
