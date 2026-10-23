# Formato del documento (referencia editorial)

> Nota: el .docx ya no se construye en la skill: lo arma el servidor y se descarga con `enlace_del_word`. Este archivo queda solo como referencia del formato editorial; no se ejecuta ningún script ni se arma un Word con código.

## Base del documento

La referencia editorial de la ruta: Times New Roman 12 pt, interlineado 1.5,
A4, márgenes de 2.54 cm, cuerpo justificado con sangría de primera línea de
0.5", y encabezados en negro, en la misma fuente del cuerpo.

En el Word del servidor el formato de página lo pone la plantilla que haya
subido el investigador o, sin ella, la de por defecto. Si la revista pide otra
cosa, se aplica en Word siguiendo la guía de autores.

## Cómo se escribe cada elemento en el texto guardado

El texto de cada fase se guarda con `guardar_capitulo`, en Markdown:

| En el texto guardado | En el Word |
|---|---|
| `## Subtítulo`, `### Subtítulo`, `#### Subtítulo` | Encabezados, del más alto al más bajo |
| Párrafos separados por una línea en blanco | Párrafos de cuerpo |
| Líneas que empiezan con `-` o `1.` | Listas |
| `**negrita**` y `*cursiva*` | Negrita y cursiva |
| `[AR97D22F86]`, `[AR97D22F86:n]`, `[AR97D22F86:p. 45]` | Citas en la norma del proyecto |
| `[FALTA FUENTE]` | Marca de afirmación sin fuente |

El título de cada sección (Introducción, Métodos…) lo pone el servidor con el
nombre de la fase; no se repite al comienzo del texto. La lista de referencias
tampoco se escribe: la arma el servidor, una sola y en la norma del proyecto.

## Tablas en APA 7

APA 7 = solo reglas horizontales (sobre el encabezado, bajo el encabezado y al
cierre), sin bordes verticales, sin sombreado, sin color. El número de tabla va
en negrita en su propia línea, el título en cursiva debajo, y la nota debajo de
la tabla empezando con "Nota." en cursiva.

En el texto guardado la tabla va en **un solo bloque, sin líneas en blanco**, y
el servidor la dibuja con ese formato:

```
**Tabla 1**
*Características sociodemográficas de los participantes*
| Variable | f | % |
|---|---|---|
| Femenino | 66 | 56.4 |
| Masculino | 51 | 43.6 |
*Nota.* n = 117. Tres casos sin dato en la variable sexo; los porcentajes son sobre casos válidos.
```

Las celdas admiten citas con clave. Una línea en blanco dentro del bloque parte
la tabla y la deja como texto suelto.

## Figuras

El Word del servidor **no inserta imágenes**. En el texto va el rótulo de la
figura y, debajo, un párrafo que marca dónde va la imagen:

```
**Figura 1**
*Título de la figura*

[Insertar aquí la Figura 1: nombre-del-archivo.png]
```

Si la figura lleva nota, va debajo del marcador, empezando con `*Nota.*`. Al dar
el enlace del Word, decirle al investigador qué imagen pega en cada marcador: en
Word, borra el marcador y usa *Insertar → Imágenes* en ese lugar. La imagen,
exportada desde el programa a 300 ppp, no como captura de pantalla.

## Lo que el servidor no hace

Numeración de líneas, doble columna, página de título anonimizada o aparte,
tablas y figuras al final o en archivos separados: si la guía de autores lo
pide, lo aplica el investigador en Word antes de enviar. Se le dice qué y dónde,
en concreto.

## Antes de dar el Word por bueno

Pedirle al investigador que lo abra y confirme tres cosas: que los encabezados
salen bien, que ninguna tabla se parte entre páginas ni tiene bordes verticales,
y que cada marcador de figura quedó reemplazado por su imagen.
