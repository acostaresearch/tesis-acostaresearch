# La versión en inglés

Se lee en el Paso 5, solo si la revista publica en inglés.

## Las cinco reglas que no se negocian

**1. Ninguna cifra cambia.** Ni un decimal, ni un tamaño de muestra, ni un valor
de p. Y ojo con el separador decimal: en español se escribe con coma en algunos
contextos y en inglés siempre con punto. Convertir el separador **no es cambiar
la cifra**; cambiar el número sí.

**2. Las citas y las referencias se conservan exactamente.** Autores, años,
títulos. **El título de una fuente publicada en español no se traduce**: se cita
como está publicada. Algunas normas piden agregar la traducción entre corchetes;
eso se verifica en la guía de autores.

**3. Los nombres propios de instituciones y programas no se traducen
literalmente** si tienen forma oficial. Se describe su naturaleza: "una
universidad pública peruana", no una traducción palabra por palabra que no
existe en ningún registro.

**4. Terminología consistente.** Si el constructo se tradujo de una forma en la
introducción, se mantiene en todo el documento. Es donde más se rompe una
traducción larga, y donde un revisor nota que el texto pasó por una máquina.

**5. Tiempo verbal.** Métodos y Resultados en pasado. La introducción y la
discusión admiten presente cuando describen el estado del conocimiento.

## Qué hay que mirar con cuidado

**Los términos técnicos del campo**, que rara vez son la traducción literal. El
nombre en inglés del constructo se toma de los artículos que ya se citaron: si
la literatura lo llama de una forma, esa es la forma, aunque la traducción
directa suene razonable.

**Los calcos del español**: "se evidenció que" (*it was evidenced that*),
"resulta pertinente señalar", "en tal sentido" (*in this sense*), "permitió"
(*allowed to*). No se traducen; se reemplazan por la construcción directa del
inglés académico. Se limpian con
`humanizador-academico-ingles`, que trae las reglas completas de calcos.

**Las escalas y sus anclajes.** Si el instrumento tiene una versión publicada en
inglés, se usan sus términos originales, no una traducción nueva.

## El aviso, que hay que dar sin adornarlo

**Esta traducción necesita revisión de un hablante nativo o de un servicio de
edición antes de enviar.**

El rechazo por calidad del lenguaje es frecuente en revistas Q1 y Q2, llega
rápido y no trae comentarios útiles sobre el contenido. Varias editoriales
ofrecen servicios de edición de pago, y algunas universidades lo cubren.

No significa que esta traducción no sirva. Significa que antes de enviar conviene
que la lea alguien más.

## Qué se entrega

Preguntar qué necesita la revista, porque no todas piden lo mismo:

- **Manuscrito completo en inglés**, que es lo habitual.
- **Solo el abstract y las keywords en inglés**, cuando la revista publica en
  español pero exige el resumen bilingüe.
- **Ambas versiones**, en revistas bilingües.

La versión en inglés sale como archivo propio
(`articulo_docx.py nuevo --idioma en --md manuscrito_en.md --perfil
REVISTA_[clave].json --fuentes inventario.json --out
ARTICULO_[clave]_v8_en.docx`), traducida sección por sección con las **claves
de cita sin traducir** (`[F012]`: el motor arma citas y lista) y los títulos de `estructura_en` del perfil si la revista es
bilingüe (para `verificar`, ver `ajustes_docx.md`, sección 7), y **la versión en español y su `_RESPALDO` se conservan**: si la
revista rechaza y la siguiente es hispanohablante, el reenvío parte de ahí.
