# Estilos de cita: APA 7, Chicago author-date, IEEE y Vancouver

El estilo **y su edición** los fija la revista destino (Ficha, sección 7), no la
costumbre. Si no consta, se pide la guía de autores antes de redactar. Mezclar
estilos en un manuscrito es motivo de devolución editorial.

**Con ejecución de código, las citas y la lista las formatea el motor**
(`articulo_docx.py --fuentes`, citas por clave; ver `fuentes_y_citas.md`). Estas
reglas sirven para **revisar** lo que sale y para el **modo chat** sin código,
donde la lista se arma a mano.

El conector entre autores sigue el idioma del manuscrito: **y** en español,
**and** en inglés. En APA, `&` solo dentro del paréntesis y en la lista.

## Resumen de la regla de et al.

| Estilo | En el texto | En la lista de referencias |
|---|---|---|
| APA 7 | 1–2 autores: todos; 3 o más: `et al.` desde la primera cita | Hasta 20 autores, todos; 21 o más: los 19 primeros, `...` y el último |
| Chicago 18.ª (2024, vigente) | 1–2: todos; 3 o más: `et al.` | Hasta 6, todos; 7 o más: los 3 primeros y `et al.` |
| Chicago 17.ª | 1–3: todos; 4 o más: `et al.` | Hasta 10, todos; 11 o más: los 7 primeros y `et al.` |
| IEEE | Solo el número; si se nombra: 1–2 todos, 3 o más `et al.` | Hasta 6, todos; 7 o más: el primero y `et al.` |
| Vancouver (ICMJE/NLM) | Solo el número; si se nombra: 1–2 todos, 3 o más `et al.` | Hasta 6, todos; 7 o más: los 6 primeros y `et al.` |

Chicago: si la guía dice solo "Chicago author-date", se usa la 18.ª y se le
dice al autor; si dice 17.ª, la 17.ª. Una sola regla en todo el manuscrito.

---

## APA 7 (séptima edición)

### En el texto

| Autores | Paréntesis | Narrativa |
|---|---|---|
| 1 | (Romi, 2024) | Romi (2024) |
| 2 | (Fornell & Larcker, 1981) | Fornell y Larcker (1981) |
| 3 o más | (Hair et al., 2019) | Hair et al. (2019) |

- Coma antes del año, siempre. Varias obras: orden alfabético, punto y coma →
  (Demirdis, 2024; Hair et al., 2019). Cita textual con página → (Romi, 2024, p. 12).

### Lista de referencias

Orden alfabético, sangría francesa.

- **Artículo**: Apellido, I. I., Apellido, I. I., & Apellido, I. I. (Año).
  Título en formato oración. *Nombre de la Revista, Volumen*(número), páginas.
  https://doi.org/xxx
  - `Hair, J. F., Risher, J. J., Sarstedt, M., & Ringle, C. M. (2019). When to use and how to report the results of PLS-SEM. `*`European Business Review, 31`*`(1), 2–24. https://doi.org/10.1108/EBR-11-2018-0203`
- **Libro**: Apellido, I. I. (Año). *Título del libro* (2.ª ed.). Editorial.
- **Capítulo**: Apellido, I. I. (Año). Título del capítulo. En I. Editor (Ed.),
  *Título del libro* (pp. xx–xx). Editorial.
- **Web**: Autor u Organización. (Año, día de mes). *Título de la página*.
  Sitio. URL
- Cursiva en el nombre de la revista **y el volumen**; el número entre
  paréntesis, sin cursiva. Título del artículo en formato oración.

---

## Chicago author-date

### En el texto

| Autores | Paréntesis | Narrativa |
|---|---|---|
| 1 | (Romi 2024) | Romi (2024) |
| 2 | (Fornell y Larcker 1981) | Fornell y Larcker (1981) |
| 3 (18.ª) | (Zhao et al. 2010) | Zhao et al. (2010) |
| 3 (17.ª) | (Zhao, Lynch y Chen 2010) | Zhao, Lynch y Chen (2010) |
| 4 o más | (Hair et al. 2022) | Hair et al. (2022) |

- **Sin coma antes del año**: la diferencia visible más frecuente con APA.
- Varias obras: punto y coma → (Demirdis 2024; Konishi 2026).
- Cita textual: (Romi 2024, 12), sin "p.".

### Lista de referencias

Orden alfabético, sangría francesa, **nombres de pila completos** (no
iniciales). Primer autor invertido; los siguientes en orden natural.

- **Artículo**: Apellido, Nombre, Nombre Apellido, y Nombre Apellido. Año.
  "Título del Artículo." *Nombre de la Revista* Vol (Núm): páginas.
  https://doi.org/xxx.
  - `Hair, Joseph F., Jeffrey J. Risher, Marko Sarstedt, y Christian M. Ringle. 2019. "When to Use and How to Report the Results of PLS-SEM." `*`European Business Review`*` 31 (1): 2–24. https://doi.org/10.1108/EBR-11-2018-0203.`
- **Libro**: Apellido, Nombre. Año. *Título del Libro*. 2.ª ed. Editorial.
- **Capítulo**: Apellido, Nombre. Año. "Título del Capítulo." En *Título del
  Libro*, editado por Nombre Apellido, páginas. Editorial.
- **Web**: Apellido, Nombre (u Organización). Año. "Título de la Página."
  Sitio. Mes día, año. URL.
- Cada referencia termina en punto, incluido el DOI.

### Conversión APA → Chicago

| APA | Chicago |
|---|---|
| (Hair et al., 2022) | (Hair et al. 2022) |
| (Fornell & Larcker, 1981) | (Fornell y Larcker 1981) |
| (Stone, 1974; Geisser, 1974) | (Geisser 1974; Stone 1974) |
| Hair, J. F., & Sarstedt, M. (2019). | Hair, Joseph F., y Marko Sarstedt. 2019. |

Quitar la coma antes del año; `&` → `y`/`and`; en la lista, año después de los
autores, nombres de pila completos, título entre comillas, volumen sin
paréntesis. **El nombre de pila no se deduce**: se busca la fuente real (DOI,
sitio de la revista) o se marca `[POR CONFIRMAR: nombre completo del autor]`.

---

## IEEE

### En el texto

- Número entre corchetes por **orden de primera aparición**: [1], [2]. Un
  número por fuente, que se reutiliza si vuelve a citarse.
- Varias: [1], [3] o rango [4]–[7]. Con página: [5, p. 12].
- El número funciona como sustantivo: "como muestra [3]"; con nombre:
  "Hair et al. [3]".

### Lista de referencias

Por orden numérico (no alfabético). Iniciales antes del apellido; título del
artículo entre comillas; revista abreviada en cursiva.

- **Artículo**: [1] A. B. Apellido, C. Apellido, and D. Apellido, "Título del
  artículo," *Abrev. Revista*, vol. 31, no. 1, pp. 2–24, Mes. Año, doi: xxx.
  - `[1] J. F. Hair, J. J. Risher, M. Sarstedt, and C. M. Ringle, "When to use and how to report the results of PLS-SEM," `*`Eur. Bus. Rev.`*`, vol. 31, no. 1, pp. 2–24, 2019, doi: 10.1108/EBR-11-2018-0203.`
- **Libro**: [2] A. Apellido, *Título del Libro*, 2nd ed. Ciudad, País:
  Editorial, Año.
- **Capítulo**: [3] A. Apellido, "Título del capítulo," in *Título del Libro*,
  B. Editor, Ed. Ciudad, País: Editorial, Año, pp. xx–xx.
- **Web**: [4] Autor u Organización, "Título de la página," Sitio. Accessed:
  Mes día, Año. [Online]. Available: URL

---

## Vancouver (ICMJE / NLM)

### En el texto

- Número arábigo por **orden de primera aparición**, en el formato que pida la
  revista: (1), [1] o superíndice¹. Varias: (1,3) o rango (4–7).
- Con nombre: "Hair et al. (3)".

### Lista de referencias

Por orden numérico. Apellido e iniciales sin puntos ni comas entre ellas;
revista abreviada según NLM, sin cursiva.

- **Artículo**: 1. Apellido AB, Apellido CD, Apellido EF. Título del artículo.
  Abrev Revista. Año;Vol(Núm):páginas. doi:xxx
  - `1. Hair JF, Risher JJ, Sarstedt M, Ringle CM. When to use and how to report the results of PLS-SEM. Eur Bus Rev. 2019;31(1):2-24. doi:10.1108/EBR-11-2018-0203`
- **Libro**: 2. Apellido AB. Título del libro. 2.ª ed. Ciudad: Editorial; Año.
- **Capítulo**: 3. Apellido AB. Título del capítulo. En: Editor CD, editor.
  Título del libro. Ciudad: Editorial; Año. p. xx-xx.
- **Web**: 4. Autor u Organización. Título de la página [Internet]. Ciudad:
  Editor; Año [citado Año Mes día]. Disponible en: URL

---

## Estilos numéricos (IEEE, Vancouver): renumerar

Agregar o quitar una fuente **obliga a renumerar desde ese punto** la lista y
cada llamada del texto. Con citas por clave lo hace el motor en cada `agregar`
(y en `normalizar`). Solo con referencias escritas a mano la renumeración de las
llamadas sigue siendo tarea de la fase que agrega la fuente; el motor ordena esa
lista por número y `verificar` avisa si hay saltos o desorden.

## Reglas de contenido, válidas en todos los estilos

- Se cita por contenido solo lo que tiene resumen o texto completo verificado.
  Sin resumen, la mención se limita a lo que el título respalda.
- No se inventan DOIs, páginas, volúmenes ni años: lo que falte va
  `[POR CONFIRMAR: ...]`.
- Toda obra citada está en la lista, y toda obra de la lista está citada.
