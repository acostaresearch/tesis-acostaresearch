# Normas de citas: cómo sale cada una en el Word

La norma de citas es **una sola para toda la tesis y vive en el proyecto**. Se lee de `mi_proyecto`; si no está elegida, se pregunta una vez y se guarda con `guardar_avance` (`estiloCitas`). El texto se redacta siempre igual, con claves `[AR…]`, y **el servidor escribe las citas y la lista de referencias en la norma guardada**. En las normas numéricas, los números siguen el orden de aparición en toda la tesis.

**La skill no convierte citas, no toca la numeración y no reescribe referencias.** Si el asesor pide otra norma, se cambia `estiloCitas` y el Word siguiente sale en la nueva sin tocar ningún capítulo.

Este archivo sirve para explicarle al tesista cómo se verán sus citas y para revisar el Word descargado. El detalle de APA 7 está en `references/apa7_citas.md`.

## Normas que ofrece la plataforma

```
LO QUE PIDE EL TESISTA               VALOR DE estiloCitas
───────────────────────────────────  ─────────────────────────────────────
APA 7                                apa
IEEE                                 ieee
Vancouver                            nlm-citation-sequence
AMA 11.ª edición                     american-medical-association
ACS                                  american-chemical-society
Nature                               nature
MLA 9.ª edición                      modern-language-association
Chicago autor-fecha                  chicago-author-date
Chicago notas y bibliografía         chicago-notes-bibliography
Chicago notas abreviadas             chicago-shortened-notes-bibliography
Harvard (Cite Them Right)            harvard-cite-them-right
Elsevier Harvard                     elsevier-harvard
ISO 690 autor-fecha (España)         iso690-author-date-es
ISO 690 notas (España)               iso690-full-note-es
APSA                                 american-political-science-association
ASA                                  american-sociological-association
MHRA (notas)                         mhra-notes
```

El idioma de las citas va aparte, en `idiomaCitas`: `es-ES` por defecto, `es-MX`, `es-CL` o `en-US`. Decide «y» o «and», «s. f.» o «n.d.». Solo se cambia si la tesis va en inglés o si se lo piden.

Si el tesista pide una norma que no está en la lista, se le dice que la plataforma no la tiene y se acuerda con él la más cercana. No se guarda una distinta sin decírselo, y no se imita a mano.

## Tabla de decisión rápida

| Carrera típica | Norma esperada |
|---|---|
| Educación, Psicología, Ciencias Sociales, Administración | APA 7 |
| Medicina, Enfermería, Obstetricia, Nutrición, Tecnología Médica | Vancouver |
| Ingenierías, Informática, enseñanzas técnicas | IEEE |

Esto es orientativo. **Manda el reglamento de la universidad, no la carrera.** Si el tesista dice que su reglamento pide otra, se respeta sin discusión.

## APA 7 (la más común)

Sistema **autor-fecha**.

```
LO QUE ESCRIBE LA SKILL        LO QUE SALE EN EL WORD
─────────────────────────────  ──────────────────────────────────
…afirmación [AR…].             …afirmación (García, 2024).
García [AR…:n] sostiene…       García (2024) sostiene…
[AR…][AR…][AR…]                (García, 2024; López, 2023; Ríos, 2025)
                               → orden alfabético dentro del paréntesis
«…» [AR…:p. 45]                «…» (García, 2024, p. 45)

REFERENCIA (artículo de revista)
   García, A. A., y López, B. B. (2024). Título del
      artículo. Nombre de la Revista, 12(3), 45-67.
      https://doi.org/10.xxxx/yyyy

ORDEN DE LA LISTA
   Alfabético por primer apellido del primer autor.
```

## Vancouver (Ciencias de la Salud)

Sistema **numérico por orden de aparición**. Nació de la reunión de Vancouver de 1978, que dio origen al ICMJE (Comité Internacional de Editores de Revistas Médicas).

```
LO QUE ESCRIBE LA SKILL        LO QUE SALE EN EL WORD
─────────────────────────────  ──────────────────────────────────
…afirmación [AR…].             …afirmación (1).
García [AR…:n] demostró…       García (1) demostró…
[AR…][AR…][AR…]                (1,3,5)  o rango (1-4)

REFERENCIA (artículo de revista)
   1. García AA, López BB, Ríos CC. Título del
      artículo. Abrev Revista. 2024;12(3):45-67.

   Sin coma entre apellido e iniciales. Sin puntos en las
   iniciales. Revista ABREVIADA según MEDLINE.

ORDEN DE LA LISTA
   Numérico, por orden de aparición. NO alfabético.
```

El número lo asigna el servidor. Si se reordena un párrafo o se añade un capítulo, el Word siguiente sale con la numeración al día sin que nadie la toque.

**Autores**: los seis primeros y "et al." si son más. Algunas universidades piden todos: si el tesista lo dice, se le explica que eso depende de la norma elegida en el proyecto.

## IEEE (Ingenierías)

Sistema **numérico entre corchetes**, por orden de aparición.

```
LO QUE ESCRIBE LA SKILL        LO QUE SALE EN EL WORD
─────────────────────────────  ──────────────────────────────────
…afirmación [AR…].             …afirmación [1].
García [AR…:n] propone…        García [1] propone…
[AR…][AR…][AR…]                [1], [3], [5]  o rango [1]-[4]

REFERENCIA (artículo de revista)
   [1] A. A. García, B. B. López, y C. C. Ríos,
       "Título del artículo," Abrev Revista, vol. 12,
       no. 3, pp. 45-67, 2024.

ORDEN DE LA LISTA
   Numérico, por orden de aparición. NO alfabético.
```

Misma lógica que Vancouver: la numeración es del servidor.

## ISO 690 y otras que no están en la lista

**ISO 690 no es un estilo sino una norma**. La UNE-ISO 690:2024 (traducción de la ISO 690:2021) da directrices para redactar referencias pero no prescribe un formato único: admite tres métodos de citación (autor-fecha, numérico y notas al pie). Lo que exige es coherencia dentro del documento.

Si un tesista la declara, se le pregunta qué método pide su universidad y se elige con él la norma de la lista que corresponde a ese método (por ejemplo, una autor-fecha o una numérica). Se le dice con claridad que el Word saldrá en esa norma, no en una guía institucional hecha a mano, para que lo confirme con su asesor.

## Qué cambia y qué no cambia con la norma

```
CAMBIA (lo hace el servidor)
   · Formato de la cita en el texto
   · Formato de cada referencia
   · Orden de la lista de referencias (alfabético vs aparición)
   · La numeración, en las normas numéricas

NO CAMBIA
   · El texto guardado: siempre con claves [AR…]
   · La estructura de seis párrafos de la introducción
   · La meta de cobertura del 70% del corpus
   · La matriz de consistencia y su formato APA 7 de tabla
     (el formato de TABLA es igual con cualquier norma: es
      diseño editorial, no norma de citas)
   · Los checkpoints obligatorios
   · La auditoría anti-IA de 17 patrones
   · La búsqueda complementaria de fuentes nacionales
   · El Paso 6.5 de ODS y estadísticas
```

## Auditoría de marcas (Paso 9.5)

La auditoría de antes revisaba una conversión hecha a mano. Ahora no hay conversión: se revisa que el texto esté listo para que el servidor la haga. El bloque completo está en el Sub-paso 9.5.2 del SKILL.md. Lo esencial:

- Norma guardada en el proyecto con `guardar_avance`.
- Toda cita es una clave `[AR…]` devuelta por una búsqueda o por la biblioteca.
- Ninguna cita escrita a mano, en ninguna norma.
- Entre corchetes, solo claves, `[FALTA FUENTE]` y marcas de figura.
- Sin lista de referencias escrita a mano.

Estado: **OK PARA GUARDAR / CORREGIR**.
