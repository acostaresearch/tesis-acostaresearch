# El resumen y el abstract

Se lee en los Pasos 5 y 6. Son la parte más leída del artículo y la que más se
escribe con prisa. Las palabras clave están en `titulo_y_claves.md`.

---

## El resumen en español

**Resumen estructurado**, salvo que la revista pida otro formato.

Revisión sistemática — **PRISMA 2020 for Abstracts** (12 ítems; se cubren
todos los que apliquen, con los subtítulos que use la revista):

| Bloque | Qué lleva |
|---|---|
| Título | Identifica el trabajo como revisión sistemática (o metaanálisis) |
| Objetivos | La pregunta o el objetivo principal |
| Métodos | Criterios de elegibilidad; fuentes con la **fecha de la última búsqueda**; herramienta de riesgo de sesgo; método de síntesis |
| Resultados | Número de estudios y de participantes incluidos; resultados principales (con el efecto e intervalo si hubo metaanálisis) |
| Discusión | Limitaciones de la evidencia; interpretación general |
| Otros | Financiamiento; **registro** con nombre y código (PROSPERO, OSF…) o "no registrada" |

Revisión de alcance — **PRISMA-ScR**: antecedentes, objetivos, criterios de
elegibilidad, fuentes de evidencia, método de extracción (*charting*),
resultados y conclusiones.

Bibliométrica — sin guía única: objetivo; bases, ecuación resumida, periodo y
fecha de búsqueda; número de documentos tras la depuración; software
(bibliometrix, VOSviewer); indicadores principales; conclusión.

Ninguna cifra (estudios, participantes, fechas, código de registro) se escribe
si no está en Métodos o Resultados: lo que falte va `[POR CONFIRMAR]`.

Lo que **no** va en un resumen: antecedentes extensos, citas de otros autores,
abreviaturas sin explicar, ni aperturas del tipo "en los últimos años el
interés por…".

## El conteo

**Se cuentan las palabras, no se estiman**:
`python3 scripts/articulo_docx.py contar resumen.md`.

Límite exacto: `resumen.max_palabras` del perfil de la revista. Si el perfil lo
tiene `por_confirmar`, 150 a 250 como referencia **y decir que hay que
verificarlo**: hay revistas de 150 y de 300. El abstract respeta el mismo
máximo. Se ajusta recortando; lo primero que sale es el detalle metodológico, lo
último, el resultado.

## No copia frases

El resumen es una **síntesis propia del artículo completo**. Si repite
oraciones literales de las conclusiones o de la Discusión, se nota, y los
detectores de similitud lo marcan contra el propio manuscrito.

---

## El abstract en inglés

Mismo contenido y estructura, en inglés académico, en **pasado**:

> This study aimed to… A cross-sectional design was used… The results showed…
> It is concluded that…

- **Siglas locales explicadas** en su primera mención.
- **Longitud equivalente** a la del resumen.
- **Instituciones y programas** con forma oficial no se traducen literalmente:
  se describe su naturaleza ("a Peruvian public university").
- **Calcos del español** que delatan traducción ("it was evidenced that", "in
  this sense", "allowed to"): se reemplazan por la construcción directa del
  inglés académico. Lo limpia `humanizador-academico-ingles` en modo breve
  (Paso 8).

## El aviso sobre la traducción

Hay que darlo, sin adornarlo: **una traducción pulida no sustituye la revisión
de un hablante nativo o de un servicio de edición.** El rechazo por lenguaje es
frecuente en Q1 y Q2, y evitable.
