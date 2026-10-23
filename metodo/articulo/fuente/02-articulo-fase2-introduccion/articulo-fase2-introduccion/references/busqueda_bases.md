# Guiar la búsqueda en cada base de datos

Se lee en la Fase 2 (Paso 2).
También en la Fase 3, cuando falta respaldo para una hipótesis o un constructo
(búsqueda complementaria).

**Alcance.** Esta búsqueda alimenta la Introducción y la Revisión de la
literatura: 20 a 40 registros con resumen.

**La skill no busca por él en las bases suscritas.** Scopus y Web of Science
piden credenciales institucionales. Le arma los términos y la ecuación exacta,
le dice dónde pegarla y cómo exportar.

## De dónde salen los términos

De la **Matriz de la Fase 1**: constructos con sus nombres alternativos,
población y ámbito. Nada se inventa. Antes de las ecuaciones, mostrarle la
tabla y pedirle que agregue los sinónimos de su campo:

| Concepto | Términos en español | Términos en inglés |
|---|---|---|
| Constructo 1 | | |
| Constructo 2 | | |
| Población | | |

Si un constructo tiene un nombre estándar en inglés que no es la traducción
literal, decirlo: es la causa más común de búsquedas que devuelven cero.

## Scopus

**a) Búsqueda simple (*Search documents*).** Las palabras clave listas para
pegar; el campo por defecto busca en título, resumen y palabras clave.

**b) Búsqueda avanzada (*Advanced document search*).** La ecuación completa:

```
TITLE-ABS-KEY ( ( "término1" OR "término2" ) AND ( "término3" OR "término4" ) )
AND PUBYEAR > 2019
```

Reglas que se le explican: comillas para frases exactas; OR entre sinónimos
dentro de su paréntesis; AND entre conceptos distintos; asterisco al final de
una raíz (`educat*`); filtro de años si el tema es reciente. Si devuelve miles,
sobran conceptos amplios; si devuelve cero, sobran comillas o falta un
sinónimo. Los códigos de campo se verifican en la ayuda de la plataforma, que
cambia; no se dictan de memoria como inmutables.

**c) Exportar.** Este paso decide si la fase se puede hacer:

1. Marcar los documentos (o *Select all*) → **Export** → **RIS** (o **CSV**):
   **uno solo de los dos**. El mismo export en RIS, CSV y TXT a la vez duplica
   fuentes; el TXT de Scopus es el formato menos fiable.
2. En los campos, marcar *Citation information*, *Bibliographical information*
   y **Abstract & keywords**. Sin el resumen, esas fuentes solo se podrán
   mencionar por su título.
3. Guardar el archivo tal cual, sin abrirlo ni editarlo en Excel.

## Web of Science

`TS=` (Topic) equivale a `TITLE-ABS-KEY`:

```
TS=( ("término1" OR "término2") AND ("término3" OR "término4") )
```

Mismos operadores, comillas y comodín. WoS y Scopus **no contienen las mismas
revistas** y sus cuartiles son de sistemas distintos: si la institución exige
uno, se busca en ese.

**Exportar:** **Export** → **Plain text file** → *Record content*:
**Full Record**. Hasta 500 registros por exportación.

## SpringerLink

Base de un solo editor, no un índice. Sirve para conseguir **textos completos**
de artículos ya identificados, no para la búsqueda principal: buscar solo ahí
sesga las referencias hacia un editor.

## Google Académico

Sirve para localizar, con dos condiciones: se sabe para qué y se verifica lo
que devuelve. Operadores: comillas, `allintitle:`, rango de años y el botón
**"Citado por"** (trabajos posteriores que citan uno bueno). Advertencias:
**indexa de todo**, incluidas revistas depredadoras, y **no exporta lotes con
resumen**: el registro completo se consigue en Scopus, WoS o la revista.

## Búsqueda web del asistente

Para **cifras y contexto** (organismos oficiales, informes, normativa), con las
reglas de `estadisticas_y_ods.md` en la Fase 2. No sustituye el export: un
artículo hallado en la web sin su resumen completo entra al inventario como
fuente de título.

**OpenAlex y `buscar_en_la_literatura` (servidor Acosta)** sirven para
localizar, pero entregan el resumen **recortado** (~400 caracteres): el
inventario lo marca `RECORTADO` y esa fuente no se cita por contenido. Para
inventariarlas se usa texto etiquetado (`Authors:`, `Title:`, `Year:`,
`Source title:`, `DOI:`, `Abstract:`; un registro por bloque separado por
una línea en blanco; autores como `Apellido, Nombre`). El resumen
completo se consigue abriendo el DOI (página de la revista) o con el export de
Scopus/WoS de ese registro, y se pega literal en el campo `abstract` de su ID
en `inventario.json`.

## Cierre del paso

Entregarle en un solo bloque: la tabla de términos, la ecuación para Scopus, la
de WoS, las instrucciones de exportación con el resumen incluido, y cuántos
registros traer (20 a 40). **Un archivo por base**: RIS o CSV de Scopus y
texto plano de WoS (el inventario lee también BibTeX y texto etiquetado).
Modo C (sin código): el investigador pega los registros y el inventario se
arma a mano en una tabla Markdown (ID, cita, ¿resumen completo?).
**Sin fuentes no se escribe.**
