# Estilos de cita: APA 7 y Chicago author-date

> **Este archivo no sirve para convertir citas a mano.** Sirve para explicarle
> al autor cómo se ve cada estilo y para leer la guía de autores de la revista.
> En el texto guardado las citas van siempre con su clave (`[AR97D22F86]`,
> `[AR97D22F86:n]` después del nombre del autor, `[AR97D22F86:p. 45]` con
> página). La norma se guarda en el proyecto con `guardar_avance`
> (`estiloCitas`, `idiomaCitas`) y el servidor escribe las citas y la lista de
> referencias —orden y numeración incluidos— al descargar el Word. Nunca se
> convierten, se ordenan ni se numeran referencias a mano.

El estilo lo fija la revista destino, no la costumbre. Se lee en la línea
«Norma de citas» de `mi_proyecto`; si dice «sin elegir» y el autor no sabe cuál
usa la revista, pedir la guía de autores o el nombre de la revista. Como el
servidor escribe todas las citas en una sola norma, el manuscrito no mezcla
estilos: lo que hay que evitar es guardar una norma distinta de la que pide la
revista.

El conector entre autores sigue el idioma del manuscrito: **y** en español,
**and** en inglés. En APA se usa `&` solo dentro del paréntesis y en la lista
de referencias; fuera del paréntesis va la palabra completa.

---

## APA 7 (séptima edición)

### En el texto

| Autores | Paréntesis | Narrativa |
|---|---|---|
| 1 | (Romi, 2024) | Romi (2024) |
| 2 | (Fornell & Larcker, 1981) | Fornell y Larcker (1981) |
| 3 o más | (Hair et al., 2019) | Hair et al. (2019) |

- Coma antes del año, siempre.
- `et al.` desde la primera cita cuando hay tres o más autores.
- Varias obras en un paréntesis: orden alfabético, separadas por punto y coma
  → (Demirdis, 2024; Hair et al., 2019).
- Cita textual: agregar página → (Romi, 2024, p. 12).

### Lista de referencias

Orden alfabético, sangría francesa. Se listan hasta 20 autores; con 21 o más,
los primeros 19, puntos suspensivos y el último.

- **Artículo**: Apellido, I. I., Apellido, I. I., & Apellido, I. I. (Año).
  Título del artículo en formato oración. *Nombre de la Revista, Volumen*(número),
  páginas. https://doi.org/xxx
  - `Hair, J. F., Risher, J. J., & Sarstedt, M. (2019). When to use and how to report the results of PLS-SEM. `*`European Business Review, 31`*`(1), 2–24. https://doi.org/10.1108/EBR-11-2018-0203`
- **Libro**: Apellido, I. I. (Año). *Título del libro* (edición). Editorial.
- **Capítulo**: Apellido, I. I. (Año). Título del capítulo. En I. Editor (Ed.),
  *Título del libro* (pp. xx–xx). Editorial.
- Van en cursiva el nombre de la revista **y el volumen**; el número entre
  paréntesis, sin cursiva.
- El título del artículo va en formato oración (solo la primera palabra y los
  nombres propios en mayúscula).

---

## Chicago author-date (17.ª ed.)

### En el texto

| Autores | Paréntesis | Narrativa |
|---|---|---|
| 1 | (Romi 2024) | Romi (2024) |
| 2 | (Fornell y Larcker 1981) | Fornell y Larcker (1981) |
| 3 | (Zhao, Lynch y Chen 2010) | Zhao, Lynch y Chen (2010) |
| 4 o más | (Hair et al. 2022) | Hair et al. (2022) |

- **Sin coma antes del año.** Es la diferencia visible más frecuente con APA.
- La regla estándar lista los tres autores cuando son tres, y pasa a `et al.`
  desde el cuarto. Algunas revistas piden simplificar a `et al.` desde el
  tercero: si la guía lo pide, decírselo al autor y revisar cómo sale en el Word
  que genera el servidor, en vez de retocar citas a mano.
- Varias obras: separadas por punto y coma → (Demirdis 2024; Konishi 2026).
- Cita textual: (Romi 2024, 12), sin "p.".

### Lista de referencias

Orden alfabético, sangría francesa. **Nombres de pila completos**, no
iniciales: es lo que Chicago pide y lo que exigen catálogos como CGScholar.
El primer autor va invertido (Apellido, Nombre); los siguientes en orden
natural.

- **Artículo**: Apellido, Nombre, Nombre Apellido, y Nombre Apellido. Año.
  "Título del Artículo." *Nombre de la Revista* Vol (Núm): páginas.
  https://doi.org/xxx.
  - `Hair, Joseph F., Jeffrey J. Risher, y Marko Sarstedt. 2019. "When to Use and How to Report the Results of PLS-SEM." `*`European Business Review`*` 31 (1): 2–24. https://doi.org/10.1108/EBR-11-2018-0203.`
- **Libro**: Apellido, Nombre. Año. *Título del Libro*. Edición. Editorial.
- **Capítulo**: Apellido, Nombre. Año. "Título del Capítulo." En *Título del
  Libro*, editado por Nombre Apellido, páginas. Editorial.
- Título del artículo o capítulo entre comillas; revista o libro en cursiva.
- Cada referencia termina en punto, incluido el DOI.

---

## Diferencias visibles entre APA y Chicago

| APA | Chicago |
|---|---|
| (Hair et al., 2022) | (Hair et al. 2022) |
| (Fornell & Larcker, 1981) | (Fornell y Larcker 1981) |
| (Stone, 1974; Geisser, 1974) | (Geisser 1974; Stone 1974) |
| Hair, J. F., & Sarstedt, M. (2019). | Hair, Joseph F., y Marko Sarstedt. 2019. |

Sirven para reconocer el estilo en la guía de autores o en un artículo modelo, y
para explicarle al autor qué va a cambiar. **No son pasos para aplicar a mano**:
si la revista pide Chicago y el proyecto está en APA, se cambia la norma con
`guardar_avance` y el servidor rehace todas las citas y la lista al descargar el
Word.

**El nombre de pila completo no se deduce.** Si la fuente solo trae iniciales,
no se completa de memoria: se avisa al autor y se marca
`[POR CONFIRMAR: nombre completo del autor]`. Inventar un nombre a partir de
una inicial es fabricar una referencia.

## Reglas de contenido, válidas en los dos estilos

- Se cita por contenido solo lo que tiene abstract o texto completo verificado.
- Sin abstract, la mención se limita a lo que el título respalda.
- No se inventan DOIs, páginas, volúmenes ni años. Lo que falte se marca
  `[POR CONFIRMAR: ...]`.
- Toda fuente citada va con su clave `[AR…]`, y así el servidor la pone en la
  lista; en la lista no entra nada que no se haya citado. No se inventan claves
  ni fuentes: una afirmación sin respaldo se marca `[FALTA FUENTE]`.
