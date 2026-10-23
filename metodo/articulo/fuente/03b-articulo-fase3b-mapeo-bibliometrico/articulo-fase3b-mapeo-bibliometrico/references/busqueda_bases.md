# Guiar la búsqueda en cada base de datos

Se lee en el Paso 2. El investigador novato se traba aquí más que en ningún otro
punto: sabe que "hay que buscar en Scopus" pero no sabe qué escribir en la caja.

**La skill no busca por él en las bases suscritas.** Scopus y Web of Science
piden credenciales institucionales. Lo que sí hace, y es lo que le falta: armarle
los términos y la ecuación exacta, decirle dónde pegarla, y decirle cómo exportar
el resultado.

## De dónde salen los términos

De la **Matriz de la Fase 1**: los constructos con sus nombres alternativos, la
población y el ámbito. Nada se inventa aquí.

Antes de armar las ecuaciones, construir la tabla de términos y mostrársela:

| Concepto | Términos en español | Términos en inglés |
|---|---|---|
| Constructo 1 | | |
| Constructo 2 | | |
| Población | | |

Los sinónimos salen de dos sitios: los términos que aparecen en los papers de
referencia de la Fase 1, y los que el propio investigador conoce de su campo.
Si un constructo tiene un nombre estándar en inglés que no es la traducción
literal, decirlo: es la causa más común de búsquedas que devuelven cero.

---

## Scopus

**Dos formas, y el investigador necesita las dos.**

### a) Búsqueda simple (Search documents)

Se le entregan las palabras clave listas para pegar, con los campos ya elegidos.
Explicarle en una línea que el campo por defecto busca en título, resumen y
palabras clave.

### b) Búsqueda avanzada (Advanced document search)

Aquí va la ecuación completa. El campo más usado es `TITLE-ABS-KEY`, que busca
en título, resumen y palabras clave a la vez. Estructura:

```
TITLE-ABS-KEY ( ( "término1" OR "término2" ) AND ( "término3" OR "término4" ) )
AND PUBYEAR > 2019
```

Reglas que hay que explicarle, porque son las que hacen que funcione:

- **Comillas** para frases exactas de dos o más palabras.
- **OR entre sinónimos**, dentro de su propio paréntesis.
- **AND entre conceptos distintos.** Cada concepto es un bloque.
- **Asterisco** como comodín al final de una raíz, para cubrir variantes
  (`educat*` cubre education, educational, educator).
- **Filtro de años** cuando el tema es reciente.

Y una advertencia práctica: si la ecuación devuelve miles de resultados, sobran
conceptos amplios; si devuelve cero, sobran comillas o falta un sinónimo. Decirle
cómo ajustar en vez de dejarlo probando a ciegas.

**Los códigos de campo y los operadores se verifican en la ayuda de la propia
plataforma**, que cambia. No dictarlos de memoria como si fueran inmutables.

### c) Exportar

Este paso decide si la fase siguiente se puede hacer o no:

1. Seleccionar los documentos, o marcar todos los resultados.
2. Export → formato **CSV o texto**.
3. **Marcar la casilla de Abstract.** Sin el resumen, esas fuentes solo servirán
   para mencionarse por su título y no se les podrá atribuir ningún hallazgo.
4. Marcar también autores, año, título de la fuente y DOI.

Decírselo con esas palabras. Es el error que arruina la fase.

---

## Web of Science

El campo equivalente a `TITLE-ABS-KEY` es `TS=` (Topic), que busca en título,
resumen y palabras clave.

```
TS=( ("término1" OR "término2") AND ("término3" OR "término4") )
```

Mismos operadores booleanos y mismas comillas. El comodín también es asterisco.

**Cuidado con la diferencia que importa:** Web of Science y Scopus **no
contienen las mismas revistas**. Un artículo que aparece en una puede no estar en
la otra, y los cuartiles son de sistemas distintos. Si la institución del
investigador exige uno de los dos, buscar en ese.

Exportar con el campo de resumen incluido, igual que en Scopus.

---

## SpringerLink

Base de un solo editor, no un índice. Sirve para conseguir **textos completos**
de artículos que ya se identificaron en Scopus o Web of Science, no para hacer
la búsqueda principal.

Su búsqueda avanzada permite frase exacta, exclusión de términos y rango de
años. No exporta en el mismo formato, así que de aquí normalmente se bajan PDF.

Decirle para qué sirve y para qué no. Buscar solo en SpringerLink da una muestra
sesgada hacia un editor, y eso se nota en las referencias.

---

## Google Académico

Es el que todos usan y el que peor se usa. Sirve, con dos condiciones: se sabe
para qué, y se verifica lo que devuelve.

Operadores útiles:

- **Comillas** para frase exacta.
- `allintitle:` para que los términos estén en el título.
- **Rango de años** en el panel izquierdo.
- El botón **"Citado por"** para encontrar trabajos posteriores que citan uno
  bueno. Es su mejor función y casi nadie la usa.

Advertencias que hay que dar:

- **Indexa de todo**, incluidas revistas depredadoras, repositorios y borradores.
  Antes de citar algo encontrado aquí, verificar dónde se publicó.
- **No exporta un lote con resúmenes.** Sirve para localizar; el registro
  completo se consigue en Scopus, en Web of Science o en el sitio de la revista.

---

## Búsqueda web de Claude

En paralelo, y para algo distinto de lo anterior: **cifras y contexto**, no
artículos para citar por contenido.

Lo que sí se busca en la web: estadísticas de organismos oficiales, informes,
normativa, datos de país. El procedimiento y las reglas están en
`estadisticas_y_ods.md`.

Lo que **no** se hace: sustituir el export bibliográfico. Un artículo encontrado
en la web sin su resumen completo entra al inventario como fuente de título,
igual que cualquier otra.

---

## Cierre del paso

Antes de dejarlo ir a buscar, entregarle en un solo bloque:

1. La tabla de términos en español e inglés.
2. La ecuación lista para Scopus, para pegar tal cual.
3. La ecuación lista para Web of Science.
4. Las tres instrucciones de exportación con el resumen incluido.
5. Cuántos resultados sería razonable traer (entre 20 y 40 registros para una
   introducción suele bastar; más no se lee, menos no alcanza).

Y decirle que vuelva con el .txt. **Sin fuentes no se escribe**, y es preferible
esperar a redactar con lo que se recuerde.
