# Fuentes y citas: del gestor al Word y de vuelta

Toda fuente citable entra a **un solo inventario** (`inventario.json`) con una
**clave** (F012, o la AR de Acosta). El texto se escribe con claves; el motor
del Word las convierte al estilo de la revista y **genera** la lista de
referencias. Nunca se escribe a mano ni la cita ni la referencia.

## Tres vías para traer fuentes (las elige el investigador)

**(a) Plataforma Acosta conectada.** Sus herramientas trabajan sobre la
biblioteca de Acosta (indexada en Scopus y WoS) y la del investigador (su Zotero
y su Mendeley conectados desde la web, sus exports de Scopus/WoS y lo guardado
por DOI):

- `buscar_fuentes`: fichas numeradas `[AR51541814]  Autores (Año). Título.
  Revista, vol(núm), págs. https://doi.org/...` con un resumen **recortado**
  (~400 caracteres).
- `mis_fuentes`: la biblioteca del investigador, `[ARxxxx] Autores (Año). Título · origen`.
- `ampliar_desde_mis_fuentes`: bola de nieve a partir de lo que ya tiene.
- `anadir_a_mis_fuentes`: guarda en su biblioteca **solo DOIs salidos de una
  búsqueda** (no DOIs escritos de memoria).

Las fichas se pegan tal cual en un .txt y conservan su clave AR:

```bash
python3 scripts/inventario_fuentes.py fichas_acosta.txt --previo inventario.json --out inventario.json
```

Un resumen recortado no basta para citar por contenido: el inventario lo marca
y, si después llega el export de Scopus/WoS con el mismo DOI, lo completa sin
cambiar la clave (la AR queda como alias de la misma fuente).

**(b) Su gestor: Zotero o Mendeley.** Exportar la colección del artículo en
**RIS** (preferido) o **BibTeX** y pasarla al inventario. Sirven también los
exports de Scopus (CSV, RIS, txt) y WoS (txt). Se capturan volumen, número,
páginas o número de artículo, tipo (artículo, libro, capítulo, congreso, web),
editorial y nombres completos de autores cuando el formato los trae.

**(c) Búsqueda web del modelo.** Solo entra una fuente con **DOI verificado**:

```bash
python3 scripts/referencias.py doi 10.1108/EBR-11-2018-0203 --inventario inventario.json
```

Consulta Crossref (y doi.org si Crossref no lo tiene), agrega los metadatos
oficiales con un ID nuevo y rechaza el DOI que no existe. Sin red, lo dice y
propone la vía (a) o (b). Si hay plataforma, después `anadir_a_mis_fuentes`
con ese DOI para que quede en la biblioteca del investigador. Nunca se
inventan metadatos.

## Cómo se cita en el .md

| Escribe | APA 7 | Vancouver | IEEE |
|---|---|---|---|
| `[F012]` | (Hair et al., 2019) | (3) | [3] |
| `[F012:n]` | Hair et al. (2019) | Hair et al. (3) | Hair et al. [3] |
| `[F012:p. 45]` | (Hair et al., 2019, p. 45) | (3, p. 45) | [3, p. 45] |
| `[F012:n, p. 45]` | Hair et al. (2019, p. 45) | Hair et al. (3, p. 45) | Hair et al. [3, p. 45] |
| `[F012][AR51541814]` | (Chen et al., 2025; Hair et al., 2019) | (3,4) | [3], [4] |

Chicago autor-fecha 18.ª sale igual que APA sin coma ni «p.»: (Hair et al. 2019, 45).
El estilo lo fija `estilo_cita` del perfil de la revista; sin perfil, APA 7.

```bash
python3 scripts/articulo_docx.py nuevo   --md intro.md --out ARTICULO_x_v2.docx --fuentes inventario.json --perfil REVISTA_x.json
python3 scripts/articulo_docx.py agregar --base ARTICULO_x_v2.docx --md metodos.md --fuentes inventario.json --perfil REVISTA_x.json
python3 scripts/articulo_docx.py verificar ARTICULO_x_v3.docx --fuentes inventario.json --perfil REVISTA_x.json
```

- La sección **no** lleva `# Referencias`: el motor la genera con todas las
  fuentes citadas en el documento (Vancouver/IEEE por orden de primera
  aparición, renumerado en cada `agregar`; APA/Chicago en orden alfabético, con
  2019a/2019b si hace falta).
- Clave que no está en el inventario → `[POR CONFIRMAR: fuente F099]` en rojo y
  ✗ en `verificar`. Se agrega la fuente al inventario (vías a–c) y se regenera.
- Solo se cita por **contenido** lo que tiene resumen completo o texto; con
  resumen recortado o sin resumen, solo lo que dice el título.

## Reenvío a otra revista con otro estilo

El Word guarda, invisibles, la clave de cada cita y una copia de las fuentes
citadas. Al cambiar de revista:

```bash
python3 scripts/articulo_docx.py normalizar ARTICULO_x_v7_RESPALDO.docx --perfil REVISTA_nueva.json --fuentes inventario.json --out ARTICULO_x_v8.docx
```

reescribe citas y lista en el estilo nuevo (p. ej. APA → Vancouver) y
renumera, aunque el Word se haya editado; solo las citas tecleadas o pegadas a
mano se revisan aparte. Con el perfil de siempre, la misma orden **refresca**
las referencias tras corregir el inventario.

## Vuelta al gestor

```bash
python3 scripts/referencias.py exportar --inventario inventario.json --docx ARTICULO_x_v8.docx \
    --ris CITADAS_x.ris --bib CITADAS_x.bib --dois DOIS_x.txt
```

Solo exporta las fuentes **citadas**.

- **Zotero**: Archivo → Importar → `CITADAS_x.ris` en la colección `[clave]`.
  Para citas vivas: `normalizar ARTICULO_x_v8.docx --estilo zotero --out
  ARTICULO_x_ZOTERO.docx` deja las citas como `{Hair et al., 2019}` (el formato
  que lee Zotero) y quita la lista; se guarda como RTF en Word y se pasa por
  Herramientas → RTF Scan, que crea las citas vivas y la bibliografía.
- **Mendeley**: importar `CITADAS_x.ris` (o `.bib`) en la colección; para citas
  vivas, insertarlas con Mendeley Cite buscándolas en esa colección (o por
  `DOIS_x.txt`).

Las citas vivas son opcionales y van al final: desde ahí manda el gestor.

## Modo chat (sin ejecución de código)

El modelo escribe con claves `[F012]` y al final entrega: (1) la lista de
referencias de las fuentes citadas, formateada a mano según `estilos_cita.md`, y
(2) un bloque RIS con esas fuentes (`TY  - JOUR` … `ER  - `) para importarlas
en Zotero o Mendeley.
