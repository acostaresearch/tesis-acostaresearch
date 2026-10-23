# Citas APA 7: cómo se ven en el Word

> **Alcance**: este archivo sirve para **leer, explicar y revisar** APA 7: cómo van a salir las citas y las referencias en el Word, qué significa cada caso y cómo reconocer una fuente para buscar su clave. **No enseña a escribir citas**: en el texto que se guarda van claves `[AR…]`, y el servidor las convierte en citas y referencias en la norma del proyecto (ver `references/integracion_zotero.md`). Si la norma del proyecto no es APA 7, cómo sale cada una está en `references/estilos_citacion.md`.

La skill cita SOLO fuentes de la biblioteca del proyecto: las del Zotero o el Mendeley del tesista, sus exports cargados en «Mis fuentes», las añadidas por DOI con su visto bueno y las de la biblioteca de Acosta. Cero invenciones.

## De la clave a la cita

```
LO QUE ESCRIBE LA SKILL                    LO QUE SALE EN EL WORD (APA 7)
─────────────────────────────────────────  ─────────────────────────────────
…reduce el esfuerzo [AR97D22F86].          …reduce el esfuerzo (García, 2024).

García [AR97D22F86:n] afirmó que…          García (2024) afirmó que…

«…» [AR97D22F86:p. 12]                     «…» (García, 2024, p. 12)

…en universitarios                         …en universitarios (García, 2024;
[AR97D22F86][AR2E15C80C].                  Quispe y Rojas, 2023).

[FALTA FUENTE]                             Resaltado, para que el tesista
                                           consiga la fuente.
```

La `:n` va solo cuando el apellido ya está escrito en la frase: el servidor pone entonces el año detrás del nombre y no repite el apellido.

## APA 7 en el texto (para revisar el Word)

- Apellido y año entre paréntesis en la paráfrasis; apellido en la frase y año entre paréntesis cuando el autor la inicia.
- Página solo en las citas textuales.
- Sin nombres de pila ni iniciales: solo apellidos.

### Casos por número de autores

- **Un autor**: (García, 2024) · García (2024) afirmó que...
- **Dos autores**: siempre los dos, con "y" en español: (García y López, 2024). En inglés sería "&"; lo decide `idiomaCitas`.
- **Tres o más**: primer apellido y "et al." desde la primera mención: (García et al., 2024). Si dos referencias distintas quedarían con el mismo "et al.", APA añade nombres hasta distinguirlas; el servidor lo resuelve.
- **Autor corporativo**: la primera mención con el nombre completo y la sigla, después solo la sigla: (Organización Mundial de la Salud [OMS], 2023) y luego (OMS, 2023).
- **Sin autor identificado**: las primeras palabras del título entre comillas. En una tesis, una fuente sin autor identificable casi nunca debe usarse.

### Varias fuentes a la vez

En el Word van en un mismo paréntesis, separadas por punto y coma y en orden alfabético. En el texto que se guarda basta con poner las claves seguidas: el orden lo pone el servidor.

### Citas textuales

Llevan página. Los abstracts de Scopus no tienen número de página por frase: si no se tiene la página, se parafrasea en vez de citar textualmente.

### Citas indirectas (a través de otro autor)

APA las escribe "Vygotsky (citado en García, 2024)", y en la lista va solo García. Se desaconseja: mejor buscar la fuente original con `buscar_fuentes`. Si no hay alternativa, el autor original se nombra en la prosa y la clave es la de la fuente que se leyó: `Vygotsky, citado por García [AR97D22F86:n], sostuvo que…`.

## Cómo identificar una fuente para buscar su clave

Cuando el tesista trae una fuente al chat, lo que hace falta de ella es lo que permite encontrarla en su biblioteca o añadirla:

- **De un export de Scopus (.txt o .ris)**: autores, año, título y DOI.
- **De un PDF**: título, autores y DOI suelen estar en la primera página.
- **De un resumen pegado**: si no trae autores, año o DOI, **no se inventan**: se le pide al tesista.

Con el título o el tema se busca con `buscar_fuentes` (`tema` en inglés, `temaOriginal` en español, `pais`). Si no aparece, o el export no está cargado en «Mis fuentes», o hay que añadirla con `anadir_a_mis_fuentes` por su DOI, con el visto bueno del tesista.

Campos de un registro RIS de Scopus:

```
TY  - JOUR
AU  - Smith, J. A.
AU  - Johnson, R. B.
AU  - Lee, S. C.
PY  - 2024
TI  - Generative AI and critical thinking in secondary education
DO  - 10.xxxx/yyyy
AB  - This study investigates the relationship between...
```

Con esto se localiza la fuente. En el Word saldrá como (Smith et al., 2024), pero en el texto se escribe su clave.

## Errores que la skill NO debe cometer

- Escribir la cita a mano («(García, 2024)») en el texto que se guarda, en vez de la clave.
- Usar una clave recordada o reconstruida: solo valen las que devolvió una búsqueda o la biblioteca.
- Atribuir una idea al autor equivocado. Se comprueba en el abstract antes de poner la clave.
- Citar autores que no están en la biblioteca. Eso es invención: va `[FALTA FUENTE]`.
- Poner `:n` sin que el apellido esté en la frase, o nombrar al autor y olvidar la `:n`. El Word repite o pierde el apellido.
- Usar "según el autor" como sustituto de cita.

## Checklist antes de cerrar la redacción

```
- [ ] Cada cita es una clave [AR…] devuelta por una búsqueda
       o por la biblioteca.
- [ ] La idea corresponde a lo que dice esa fuente.
- [ ] :n solo detrás del apellido escrito en la frase.
- [ ] Citas textuales (si las hay) con :p. N.
- [ ] Ninguna cita escrita a mano; lo que no tiene fuente
       va con [FALTA FUENTE].
```

Si alguna cita no pasa el checklist, se corrige o se quita. Es preferible un párrafo con menos citas pero todas con fuente, que uno con muchas y alguna inventada.

## La lista de Referencias en APA 7 (la escribe el servidor)

**La skill no escribe la sección Referencias.** El servidor la pone al final del documento con las fuentes citadas por clave, en la norma del proyecto. Lo que sigue sirve para explicarle al tesista qué va a ver y para revisar el Word descargado.

### Cómo se ve cada tipo de fuente

**Artículo de revista (caso más común)**:

```
Apellido1, A. A., Apellido2, B. B., y Apellido3, C. C. (Año).
   Título del artículo. Nombre de la Revista en cursiva,
   Volumen en cursiva(Número), páginas. https://doi.org/xxxx
```

**Libro**:

```
Apellido, A. A. (Año). Título del libro en cursiva (Edición).
   Editorial.
```

**Capítulo de libro editado**:

```
Apellido, A. A. (Año). Título del capítulo. En B. B. Editor (Ed.),
   Título del libro en cursiva (pp. xx-xx). Editorial.
```

**Tesis**:

```
Apellido, A. A. (Año). Título de la tesis en cursiva [Tesis de
   pregrado / maestría / doctorado, Universidad]. Nombre del
   repositorio. URL
```

**Documento institucional / informe técnico**:

```
Organismo. (Año). Título del documento en cursiva (No. de informe
   si aplica). Editorial / URL.
```

Ejemplo real de artículo, tal como sale en APA 7:

```
Vereau Amaya, E. A., Soto Zavaleta, A. R., Vásquez Luján, I. G.,
   González López, G. L., Tomanguilla Reyna, J., y Ríos Gonzales,
   J. D. (2025). Between Assistance and Dependence: Artificial
   Intelligence and Critical Thinking. A Study on First-Year
   University Students. International Journal of Learning,
   Teaching and Educational Research, 24(12), 118-134.
   https://doi.org/10.26803/ijlter.24.12.6
```

### Reglas de formato de la lista (las aplica el servidor)

- **Sangría francesa**: primera línea sin sangría, las siguientes con 0.5 pulgadas.
- **Orden alfabético** por primer apellido del primer autor.
- **Cursiva en**: títulos de revistas, volúmenes (no el número), títulos de libros, de tesis y de documentos institucionales.
- **DOI** como enlace `https://doi.org/...`, sin `DOI:` delante y sin punto final.
- **Primer apellido completo e iniciales** del nombre (Vereau Amaya, E. A.).
- **Hasta 20 autores** antes de "et al." en la lista. No se trunca a tres como en la cita.
- Solo aparecen las fuentes citadas en el texto.

### Si una referencia sale mal en el Word

El dato se corrige en la biblioteca, no en el capítulo: en su Zotero o su Mendeley (y «Actualizar ahora» en su perfil) o, si vino de un export o por DOI, completando el dato en la fuente de origen y volviendo a añadirla. Nunca se inventa un campo, y nunca se deja una nota entre corchetes dentro del texto.

### Recomendación al tesista

Que conecte su Zotero o su Mendeley desde su perfil en la web. Sus fuentes entran a la biblioteca del proyecto con su clave, y las referencias del Word salen enlazadas a Zotero.
