# Fuentes y búsqueda de literatura científica

Esta referencia documenta cómo guiar al tesista a reunir fuentes científicas reales para el Capítulo I. Sin fuentes, la skill no redacta. El objetivo es que el tesista llegue a **mínimo 20 fuentes en su biblioteca del proyecto**, cada una con su clave `[AR…]`, porque solo lo que tiene clave se puede citar.

## La biblioteca del proyecto: de dónde sale cada clave

```
DE DÓNDE VIENE                CÓMO ENTRA A LA BIBLIOTECA
────────────────────────────  ─────────────────────────────────────
Su Zotero/Mendeley conectado  Ya está. Si añade algo, lo mete en la
                              colección elegida y pulsa «Actualizar
                              ahora» en su perfil.

Export de Scopus, WoS,        Lo carga en «Mis fuentes» de la
Science Direct, SciELO        plataforma. Si además lo trae al chat,
(.ris, .bib, .csv, .txt)      la skill lo usa para filtrar, pero la
                              clave sale de la biblioteca.

Artículo con DOI (Scholar     anadir_a_mis_fuentes con sus DOI, solo
Labs, Google Académico, un    los que el tesista apruebe.
PDF, web_search, OpenAlex)

Biblioteca de Acosta          buscar_fuentes la trae con clave.

Sin DOI (tesis de             Se le pide que lo guarde en su Zotero o su Mendeley.
repositorio, informe,         Mientras no tenga clave, la afirmación
libro)                        va [FALTA FUENTE] y se le avisa.
```

Las herramientas, las marcas de cita y cómo decir de dónde viene cada fuente están en `references/integracion_zotero.md`.

## Por qué el corpus base lo trae el tesista

El **corpus principal** lo aporta el tesista, por cuatro razones:

1. **Garantía de calidad científica**: las fuentes seleccionadas por el tesista pasan por su criterio (acceso institucional, relevancia, año reciente).
2. **Verificabilidad**: el tesista puede revisar cada fuente y mostrarla al asesor.
3. **Rigor académico**: los exports de Scopus, Science Direct o SpringerLink equivalen a bases indexadas reales, que son las que el asesor exige en sustentación.
4. **Trazabilidad**: cada cita del texto es una clave que apunta a una fuente de su biblioteca.

## Cuándo SÍ busca la skill

Esto **no** significa que la skill tenga prohibido buscar. `buscar_fuentes` (con `tema` en inglés, `temaOriginal` en español y `pais`) es la búsqueda de todos los días y devuelve fuentes con clave. Además hay tres casos en los que la skill sale a buscar fuera de la biblioteca, siempre con transparencia y confirmación del tesista:

1. **Fuentes nacionales insuficientes** (menos de 3 tras procesar lo suyo). Es el caso más común: las bases indexadas en inglés traen poca literatura del país del tesista. La skill usa `buscar_en_la_literatura` con `pais` y completa con `web_search` en RENATI, SciELO regional, ALICIA y repositorios universitarios. Ver "Búsqueda complementaria automática de fuentes nacionales" en el SKILL.md.
2. **Estadísticas oficiales para los tres niveles** (Paso 6.5): cifras de organismos internacionales, nacionales y locales para anclar el planteamiento. Ver "Vinculación con ODS y refuerzo estadístico" en el SKILL.md.
3. **Datos de una fuente incompleta**: si a un registro le falta el DOI, la skill puede buscar ese dato puntual, mostrarlo con su enlace y, con el visto bueno del tesista, añadir la fuente con `anadir_a_mis_fuentes`.

**Regla dura que gobierna los tres casos**: toda fuente o cifra que la skill encuentre fuera de la biblioteca se entrega marcada como encontrada por la skill, con enlace verificable, y **no entra a la biblioteca hasta que el tesista la acepte explícitamente**. Nunca se cita algo que la skill no haya mostrado antes con su enlace, ni algo que no tenga clave.

**Lo que sigue prohibido sin excepción**: inventar una fuente, un autor, un año, un DOI, una cifra o una clave. Buscar y verificar es legítimo; fabricar no lo es nunca.

**Si el tesista pide ayuda para conseguir nacionales, la skill NO responde que no busca fuentes.** Esa respuesta era correcta en versiones anteriores del método y ya no lo es. Activa el caso 1.

## Construcción de la ecuación de búsqueda

La skill arma la ecuación a partir de las variables del tesista, **solo si él la pide** (la regla del Paso 3.0 manda palabras clave y filtros de interfaz). Estructura genérica:

```
( "[Variable 1]"  OR  "[sinónimo 1]"  OR  "[sinónimo 2]" )
AND
( "[Variable 2]"  OR  "[sinónimo 1]"  OR  "[sinónimo 2]" )
AND
( "[Población]"  OR  "[sinónimo]" )
```

Reglas para armar buenos términos de búsqueda:

- **Idioma**: priorizar inglés (Scopus indexa más en inglés). Si el tesista necesita fuentes en español, hacer una búsqueda paralela en SciELO o Latindex.
- **Comillas dobles** para frases exactas: `"critical thinking"` no `critical AND thinking`.
- **Sinónimos**: por cada variable, listar 2-3 sinónimos académicos (no coloquiales).
- **Operadores booleanos**: `AND` para combinar variables, `OR` para alternativas, `AND NOT` para excluir.
- **Truncamiento**: usar asterisco al final de raíces para capturar variantes (`student*` captura student, students, studentship).

### Ejemplo aplicado

Para el caso del tesista de Lengua y Literatura sobre IA generativa y disposición al pensamiento crítico en secundaria:

```
( "generative AI"  OR  "ChatGPT"  OR  "generative artificial intelligence" )
AND
( "critical thinking"  OR  "critical thinking disposition"  OR  "CCTDI" )
AND
( "secondary student*"  OR  "high school student*"  OR  "adolescent*" )
```

Para búsqueda en español:

```
( "inteligencia artificial generativa"  OR  "ChatGPT" )
AND
( "pensamiento crítico"  OR  "disposición al pensamiento crítico" )
AND
( "estudiantes secundaria"  OR  "estudiantes secundarios"  OR  "adolescentes" )
```

## Cómo exportar de Scopus (recomendado)

Scopus es la base preferida. Acceso institucional requerido.

1. Entrar a https://www.scopus.com con credenciales institucionales.
2. En el buscador, pegar las palabras clave (o la ecuación, si la pidió).
3. Filtrar resultados por: año (últimos 5 años), tipo de documento (article, review), idioma (English, Spanish).
4. Seleccionar los resultados relevantes con el checkbox.
5. Click en "Export" (botón en la parte superior).
6. Elegir formato:
   - **RIS (.ris)** para cargarlo en «Mis fuentes» o importarlo en Zotero o Mendeley. Es el que da las claves.
   - **CSV con abstracts** o **plain text**, si además quiere que la skill filtre el listado en el chat.
7. Marcar las opciones de inclusión: citation information, abstract, keywords.
8. Descargar el archivo.
9. **Cargar el .ris en «Mis fuentes»** de la plataforma (o importarlo en su Zotero o su Mendeley conectado).

## Cómo exportar de Science Direct (alternativa Elsevier)

Si Scopus no está disponible pero la universidad tiene acceso a Elsevier:

1. Entrar a https://www.sciencedirect.com con credenciales.
2. Pegar las palabras clave (sintaxis similar a Scopus).
3. Filtrar por año y tipo.
4. Seleccionar resultados.
5. Click en "Export citations" o "Download".
6. Elegir formato RIS o BibTeX.
7. Cargar el archivo en «Mis fuentes» o en su Zotero o su Mendeley.

## Cómo sacar fuentes de Google Scholar (sin acceso institucional)

Google Scholar es menos riguroso pero accesible sin credenciales. Limitaciones: incluye preprints y trabajos no revisados por pares.

1. Entrar a Google Académico buscándolo en Google. No usar
   un enlace pegado desde un chat: Google bloquea los accesos
   que llegan desde enlaces externos y devuelve rechazo o
   pantalla de verificación.
2. Pegar las palabras clave del Paso 3.0.
3. Para cada resultado relevante, anotar el DOI (en la página del artículo) o usar el botón "Guardar en Zotero" del conector de Zotero en el navegador.

Google Scholar NO permite exportación masiva. Lo práctico es que el tesista pase a la skill los resultados o los DOI de los que le interesan: la skill los confirma con él y los añade con `anadir_a_mis_fuentes`.

## Zotero (gestión de referencias)

Zotero es la vía más cómoda para toda la tesis, porque lo que el tesista guarda ahí entra a la biblioteca del proyecto con su clave y las referencias del Word salen enlazadas.

1. Descargar Zotero gratuito desde https://www.zotero.org e instalarlo.
2. Importar los .ris que ya tenga: File → Import → seleccionar el archivo.
3. Conectarlo desde su perfil en la web («Tu Zotero») y elegir la colección de la tesis.
4. Cada vez que añada algo, pulsar «Actualizar ahora» en su perfil.

## Mendeley (si ya lo usa)

Si el tesista ya lleva sus fuentes en **Mendeley**, no se le pide que se pase a Zotero: vale igual.

1. En su perfil en la web, «Tus herramientas» → «Tu Mendeley» → «Conectar mi Mendeley».
2. Elegir la carpeta de la tesis, o toda su biblioteca.
3. Lo que entra sale marcado «de tu Mendeley» y se cita por clave como lo demás. Se actualiza solo cada noche; para no esperar, «Actualizar ahora».

## Buscar desde la web, sin exportar nada

En su perfil, «Tus herramientas» → **«Tus fuentes de Scopus»**: busca en Scopus, SciELO y las tesis peruanas de ALICIA (RENATI), y añade a su biblioteca con un clic las que elija. Para quien no tiene acceso a Scopus por su universidad, o no quiere lidiar con exports.

## Cuántas fuentes pedir

- **Mínimo absoluto**: 20 fuentes con clave. Sin este número, la skill no redacta.
- **Recomendado**: 30-40 fuentes para el Capítulo I.
- **Total de la tesis**: 50-70 referencias en pregrado, 60-80 en posgrado.

Distribución sugerida del Capítulo I:
- 60% internacionales (12 de 20 mínimo).
- 30% nacionales del país declarado (6 de 20).
- 10% libros o capítulos clásicos para teoría base (2 de 20). También con clave.

## Qué hacer cuando el tesista regrese con las fuentes

1. `mis_fuentes` para ver qué entró a su biblioteca (`origen: "subidas"` para sus exports, `"zotero"` para su Zotero, `"mendeley"` para su Mendeley).
2. `buscar_fuentes` con los tres campos para localizar las del tema, las suyas y las de la biblioteca de Acosta.
3. Leer los abstracts (de la búsqueda o de lo que trajo al chat) y clasificar: nacional vs internacional según el país declarado, y relevancia para cada variable (V1, V2, ambas, marco teórico general).
4. Las que eligió y no tienen clave: añadirlas con `anadir_a_mis_fuentes` (por DOI, con su visto bueno) o pedirle que las guarde en su Zotero o su Mendeley.
5. Confirmar el conteo de fuentes con clave y pedir validación antes de avanzar al Paso 4.

## Si el tesista no logra reunir 20 fuentes

No bajar el mínimo. Si el tesista regresa con 10-15 fuentes:

- `ampliar_desde_mis_fuentes`: qué trabajos citan varias de sus fuentes y él todavía no tiene (necesita 5 o más).
- `buscar_en_la_literatura` con `pais`, para antecedentes nacionales y fuentes en español.
- Pídele que amplíe las palabras clave (sinónimos, rango de años más amplio).
- Pídele que busque tesis de pregrado y posgrado en RENATI, Cybertesis o equivalente de su país, y que las guarde en su Zotero o su Mendeley.
- Sugiérele revistas científicas de su área específicamente, no solo búsquedas generales.

No avances con menos de 20 fuentes con clave. El rigor es más importante que la velocidad.
