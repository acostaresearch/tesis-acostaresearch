---
name: revision-fase8-adaptacion-y-envio
description: >-
  Fase 8 de la Ruta del Artículo de Revisión: prepara el envío de una revisión
  que ya se escribió con la norma, el estilo de cita y el formato de la revista
  destino desde la Fase 2. Verifica el cumplimiento final contra el perfil de la
  revista, arma la página de título con autoría, ORCID y CRediT, y lo propio de
  una revisión: registro del protocolo, checklist PRISMA 2020 o PRISMA-ScR,
  diagrama de flujo y ecuaciones como material suplementario. Redacta la carta y
  las declaraciones, ofrece la humanización completa y la traducción si la
  revista la pide, y entrega la versión de la revista y su respaldo neutro.
  Incluye la rama de reenvío tras un rechazo: nuevo perfil aplicado sobre el
  respaldo. Nunca inventa datos de la revista ni declaraciones no confirmadas.
  ACTIVAR con preparar el envío de mi revisión, checklist PRISMA, cover letter,
  declaraciones, datos de autores, me rechazaron y quiero enviarla a otra
  revista.
license: Proprietary
metadata:
  version: "2.2.0"
  fase: "8"
  ruta: "Ruta del Artículo de Revisión — Acosta | IA & Research"
---

# Fase 8 — Cumplimiento final y envío

El manuscrito ya viene con la norma, el estilo de cita y el formato de la
revista desde la Fase 2 (`REVISTA_[clave].json`, ver `references/perfil_revista.md`).
Esta fase **comprueba** que cumple, agrega lo que solo se decide al final
(autoría, declaraciones, carta) y arma el paquete. Si la revista rechaza, aquí
mismo se prepara el reenvío a otra.

### La ruta completa

```
  Fase 0 · Tema y orientación
  Fase 1 · Matriz de estrategia
  Fase 2 · Introducción
  Fase 4 · Métodos
  Fase 5 · Resultados
  Fase 6 · Discusión
  Fase 7 · Conclusiones y abstract
  Fase 8 · Cumplimiento y envío        ← estás aquí
  Fase 9 · Respuesta a revisores
```

Insumos, entregables y quién decide cada dato: `references/ruta.md` (manda).
**La autoría se decide aquí y en ninguna fase anterior.**

## Dónde estás trabajando (léelo primero)

Mira qué herramientas tienes y elige **un** modo; no lo mezcles:

| Modo | Dónde | Cómo se entrega |
|---|---|---|
| **A · Con herramientas** | Claude con skills, Cowork, Claude Code, API | Scripts de esta skill (`scripts/`), archivos .docx/.xlsx reales |
| **B · Chat con código** | ChatGPT con análisis de datos, Claude.ai sin skills | Pide al usuario que suba `articulo_docx.py` (viene en la carpeta *herramientas* del paquete) y úsalo igual que en A |
| **C · Chat sin código** | Grok, ChatGPT sin análisis, cualquier chat | Entrega cada sección en un bloque de texto listo para pegar en `PLANTILLA_ARTICULO.docx`, tablas en Markdown; nunca prometas un archivo que no puedes generar |

En cualquier modo: **un paso por turno**, y si el usuario pega una
**Tarjeta de continuidad**, léela y no vuelvas a preguntar lo que ya dice.

## Dos ramas

| Rama | Cuándo | Parte de |
|---|---|---|
| **Envío** (Pasos 1 a 8) | Primer envío a la revista del perfil | `_v7.docx` + `_v7_RESPALDO.docx` + `REVISTA_[clave].json` |
| **Reenvío tras rechazo** (Paso 9) | La revista rechazó (de escritorio o tras revisión) y se va a otra | El **último `_RESPALDO`** (`_v9_RESPALDO` si pasó por la Fase 9; si no, `_v8_RESPALDO`) |

Si el autor dice "me rechazaron", se va directo al Paso 9.

## Entregables

| Archivo | Qué es |
|---|---|
| `ARTICULO_[clave]_v8.docx` | Versión de la revista, verificada (anonimizada si es doble ciego) |
| `ARTICULO_[clave]_v8_RESPALDO.docx` | Mismo texto, formato neutro (base de un reenvío) |
| `PAGINA_TITULO_[clave].docx` | Título, autores, filiaciones, ORCID, correspondencia, CRediT, declaraciones |
| `CARTA_[clave].docx` | Carta de presentación |
| `ARTICULO_[clave]_v8_en.docx` | Traducción, solo si la revista publica en inglés |
| `CITADAS_[clave].ris` / `.bib` | Las fuentes citadas, para importarlas en su Zotero o Mendeley |
| Archivos de la revisión | Checklist PRISMA 2020, diagrama de flujo, ecuaciones como material suplementario |

En el reenvío, con `[revista]` = una palabra de la revista nueva (los mismos
nombres de la Tarjeta): `ARTICULO_[clave]_vN_[revista].docx` + su `_RESPALDO`
(N = la última versión, 8 o 9), `REVISTA_[clave]_[revista].json` y
`CARTA_[clave]_[revista].docx`. La Fase 9 sigue con `_v9_[revista]`.

## Regla de oro

1. **El perfil manda; la guía se relee solo para lo que el perfil no cubre** o
   si se consultó hace más de 30 días. Ningún requisito se afirma de memoria.
2. **Ninguna declaración se escribe sin que el autor la confirme**, una por una.
3. **Los datos de los autores no se completan ni se deducen.** Un ORCID
   inventado es un problema serio.
4. **La traducción conserva cifras y citas exactamente.**
5. **Nada se recorta sin avisar.** Se propone qué quitar y el autor decide.
6. **La `_v7` y los `_RESPALDO` no se tocan** salvo para reflejar el mismo
   cambio de texto que la versión de la revista.

## Acompañamiento: el investigador es novato

- **Un paso por turno.** Opciones según `references/estilo_preguntas.md`.
- Cuando se le pide algo fuera del chat (abrir la guía, buscar el ORCID de un
  coautor) se le dice **dónde exactamente** y qué buscar.
- Toda pregunta técnica lleva `"No me queda claro, ponme ejemplos"` y, si sigue
  trabado, `"Prefiero que alguien me lo explique"`, que responde con el
  WhatsApp del equipo (+51 923 095 940) y deja el punto pendiente sin bloquear.

## Lo que esta skill NO hace

- No sube el artículo a la plataforma. No verifica revistas nuevas: eso es de
  la Fase 0 (en el reenvío, un solo paso).
- No reescribe el contenido científico: si algo de fondo no cuadra, lo señala.
- No reemplaza la revisión de un hablante nativo.
- Artículos con datos propios: están en la Ruta del Artículo Empírico.

**Modo C (chat sin código), una línea por script:** `verificar` → tabla de
cumplimiento hecha leyendo el texto pegado; `ajustar_docx.py` (mover, tablas
al final, anonimizar) → instrucciones de Word paso a paso; `nivel` → cambiar
en Word el estilo del título (Título 1 → Título 2) y de sus subtítulos;
`unir` → renombrar el primer título y cambiar el estilo del segundo (o
borrarlo); `reemplazar` → tabla "párrafo actual → párrafo nuevo" para pegar;
página de título, carta y declaraciones → un bloque cada una para pegar en
Word; `normalizar --perfil --fuentes` (reenvío) → lista de ajustes de formato
del perfil nuevo y las citas y referencias reescritas a mano en el estilo
nuevo (`estilos_cita.md`); `referencias.py exportar` → bloque RIS de las
fuentes citadas para importar en Zotero o Mendeley; `normalizar --estilo
zotero` → no aplica: las citas vivas se insertan con el complemento del gestor
en Word.

---

# Flujo

## Paso 0 — Bienvenida

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Ruta del Artículo de Revisión · Fase 8

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

¡Bienvenido a las Skills de Acosta!

Estás en la **Fase 8 — Cumplimiento y envío**. Tu artículo ya está escrito con la norma de tu revista; ahora comprobamos que cumple todo, ponemos los autores y armamos el paquete del envío.

Súbeme tu ARTICULO_[clave]_v7.docx, su _RESPALDO y tu REVISTA_[clave].json (o pega la Tarjeta de continuidad).

¿Te rechazaron y quieres enviarlo a otra revista? Dímelo y vamos por ese camino.
```

## Paso 1 — Cumplimiento contra el perfil → `_v8`

Detalle de cada comando en `references/ajustes_docx.md`.

1. **Crear el par `_v8`** sin tocar la `_v7`: con las secciones finales que pida
   la revista (declaraciones, agradecimientos, disponibilidad de datos),
   `articulo_docx.py agregar --base _v7 --md finales.md --perfil REVISTA_[clave].json
   --out ARTICULO_[clave]_v8.docx` (actualiza también el respaldo); si no hay
   nada que agregar, copiar `_v7` y `_v7_RESPALDO` como `_v8`. Con citas por
   clave, `--fuentes inventario.json` en `agregar` y en `verificar`
   (`references/fuentes_y_citas.md`).
2. **Verificar**: `articulo_docx.py verificar ARTICULO_[clave]_v8.docx --perfil
   REVISTA_[clave].json` (límite, secciones exigidas y su orden, formato).
3. **La guía, solo lo que falta**: si `consultado` del perfil tiene más de 30
   días, releerla (`references/guia_de_autores.md`) y actualizar el perfil.
   Siempre se confirma lo que el perfil no trae: declaraciones exigidas,
   archivos del envío, máximo de tablas y figuras, APC y los `por_confirmar`.
   Si falta el **límite**, se permite una lectura dirigida a ese dato (p. ej.
   la plantilla o la página de envíos); si sigue sin aparecer, `[POR
   CONFIRMAR]` y se le pide al autor que lo confirme antes de recortar.
4. **Cotejo de coherencia** (`texto --seccion`):
   preguntas de revisión frente a lo sintetizado; cifras del flujo PRISMA
   iguales en Métodos, Resultados, resumen y diagrama; título frente a lo
   encontrado.
   Un desajuste se señala y se pregunta; **no se corrige en silencio**.

Resultado en el chat, una tabla corta: `Requisito | Perfil | Manuscrito | Acción`.
Si hay que recortar, se propone de dónde y el autor decide: plan por sección
(`Sección | palabras | qué se quita | ahorro`, leyendo con `texto --seccion`),
aprobado en un mensaje y aplicado con `reemplazar` en los dos archivos. Más de
dos mil palabras es una sesión aparte (`references/guia_de_autores.md`).

5. **Ajustes** sobre la `_v8` (`scripts/ajustar_docx.py`, detalle en
   `references/ajustes_docx.md`): secciones con la estructura del perfil
   (`renombrar`, `mover`; `nivel` baja la Revisión de la literatura a
   subsección de la Introducción si la revista no la tiene propia; `unir` hace
   «Resultados y discusión»), solo en la versión de la revista. Un cambio de
   texto va **a los dos archivos** con `reemplazar`, que conserva el marcador
   de cada cita (la cita debe reaparecer tal cual en el texto nuevo).
   Al final, y en este orden: `verificar` otra vez, **tablas o
   figuras al final** si el perfil lo pide (`al-final`, solo en la `_v8`; el
   respaldo las deja en el texto) y **anonimizar** si es doble ciego (autocitas
   reveladoras, agradecimientos, institución que delate, y `anonimizar` para
   los metadatos).

**En una revisión**, además: registro del protocolo (PROSPERO, OSF, INPLASY)
con su código en Métodos o declarado como no registrado, nunca inventado;
checklist PRISMA 2020 (o PRISMA-ScR) llenado leyendo la `_v8` ítem por ítem;
diagrama de flujo como figura aparte si la revista lo pide; ecuaciones de
búsqueda completas como material suplementario.

## Paso 2 — Página de título y autoría

**Aquí, y no antes, entran los autores.** Se piden autor por autor: nombre
completo como figura en sus publicaciones, filiación (institución, ciudad,
país), **ORCID real** (si no tiene, cómo crearlo en orcid.org; nunca se
completa ni se deduce), autor de correspondencia con correo institucional,
orden confirmado con todos y **contribución CRediT** de cada uno
(`references/declaraciones.md`). Las autorías de cortesía son un problema de
integridad.

```bash
python3 scripts/articulo_docx.py nuevo --md titulo.md --out PAGINA_TITULO_[clave].docx --compacto
```

En doble ciego la página va **aparte** y la `_v8` no lleva ningún dato
personal. Si la revista lo quiere todo en un archivo: `agregar --posicion
inicio` sobre la `_v8` (no sobre el respaldo).

## Paso 3 — Declaraciones y carta de presentación

**Declaraciones** (`references/declaraciones.md`): conflicto de intereses de
todos los autores, financiamiento con código, ética con comité y código,
consentimiento, disponibilidad de datos y uso de IA. **Cada una se pregunta y
se confirma**; lo que no aplica se declara como no aplicable. Van donde diga la
revista.

**Carta** (`references/plantilla_carta.md`): título de la `_v8`, autores de la
página de título, hallazgos con las cifras del resumen tal cual, encaje con el
alcance de la revista y declaraciones confirmadas (lo demás, `[POR CONFIRMAR]`).
Si procede de una tesis, se declara.

```bash
python3 scripts/articulo_docx.py nuevo --md carta.md --out CARTA_[clave].docx --compacto   # --idioma en si va en inglés
```

**Humanización breve** de la carta: en español, `humanizador-academico`; en
inglés, `humanizador-academico-ingles` en modo breve (`references/anti_ia.md`).
Vigilar el patrón 3 (promocional) y el 12 (cierres optimistas).

## Paso 4 — Humanización completa (opcional, solo si el autor la pide)

Es **la única vez** que el manuscrito entero pasa por `humanizador-academico`:
hasta tres rondas, bloques de hasta 10 párrafos, el autor aprueba cada bloque.
Los párrafos aprobados se llevan al Word con `ajustar_docx.py reemplazar`
(JSON `buscar` → `reemplazar`, con cada cita del párrafo tal cual), **una vez
sobre la `_v8` y otra sobre el `_RESPALDO`**. Después, `verificar --perfil`. Sin cifras, citas ni datos
nuevos.

## Paso 5 — Traducción (solo si la revista pide inglés)

Reglas en `references/traduccion.md`. Sección por sección (`texto --seccion`),
cifras y claves de cita intactas, y se arma con `nuevo --idioma en --md
manuscrito_en.md --perfil REVISTA_[clave].json --fuentes inventario.json --out
ARTICULO_[clave]_v8_en.docx`. Los títulos de sección, de `estructura_en` del
perfil si la revista es bilingüe (si no, traducción literal). Los calcos se
limpian con `humanizador-academico-ingles`, una sección por llamada. Costo: el
manuscrito completo es una sesión aparte (unas 8 secciones); si la revista
pide el inglés solo tras la aceptación, se deja para entonces.
Aviso, sin adornarlo: **necesita revisión de un hablante nativo o de
un servicio de edición antes de enviar.**

## Paso 6 — Checklist de envío

- [ ] ¿`verificar --perfil` sin ✗ (límite, secciones, orden, formato)?
- [ ] ¿Perfil al día (guía consultada hace menos de 30 días)?
- [ ] ¿Estilo de cita exacto y `verificar --fuentes` sin claves `[POR CONFIRMAR: fuente …]`?
- [ ] ¿Tablas y figuras donde las pide la revista?
- [ ] ¿Doble ciego: `_v8` sin datos personales ni metadatos, página de título aparte?
- [ ] ¿Objetivos y título coherentes con lo encontrado?
- [ ] ¿Cada declaración confirmada; ORCID y correos reales; orden de autoría confirmado?
- [ ] ¿`_v7` intacta y `_v8_RESPALDO` con el mismo texto que la `_v8`?
- [ ] ¿Quedó algún `[POR CONFIRMAR]`? Listarlos.
- [ ] ¿Registro del protocolo, checklist PRISMA, diagrama y material suplementario listos?

Decirle qué pedirá la plataforma: manuscrito, página de título, carta, datos de
coautores con ORCID, palabras clave y, a veces, sugerencia de revisores.

## Paso 7 — Entrega

Los cuatro archivos (`_v8`, `_v8_RESPALDO`, `PAGINA_TITULO`, `CARTA`; más
`_v8_en` si hubo traducción) y una línea por archivo.

**Referencias para su gestor** (Zotero o Mendeley, el que use;
`references/fuentes_y_citas.md`, *Vuelta al gestor*):

```bash
python3 scripts/referencias.py exportar --inventario inventario.json --docx ARTICULO_[clave]_v8.docx \
        --ris CITADAS_[clave].ris --bib CITADAS_[clave].bib --dois DOIS_[clave].txt
```

Se importan en la colección `[clave]`. **Citas vivas**, solo si la revista o el
autor las quieren y siempre al final: Zotero → `articulo_docx.py normalizar
ARTICULO_[clave]_v8.docx --estilo zotero --out ARTICULO_[clave]_ZOTERO.docx`,
guardarlo en Word como RTF y pasar Herramientas → RTF Scan; Mendeley → insertar
cada cita con Mendeley Cite desde la colección importada. Desde ahí manda el
gestor: la ruta ya no regenera esas citas.

## Paso 8 — Handoff

> Cuando la revista responda con observaciones, activa la **Fase 9 —
> Respuesta a revisores**. Guarda la `_v8` **tal como la enviaste** y su
> `_RESPALDO`: sobre la primera se marcan los cambios; el segundo se mantiene
> al día por si hay que ir a otra revista.

## Paso 9 — Rama: reenvío tras rechazo

Se usa **solo** cuando la revista rechazó y el autor va a otra. Si el rechazo
trajo dictamen con observaciones útiles, **primero la Fase 9** (matriz de
observaciones y cambios sobre el respaldo, sin carta de respuesta) y se vuelve
aquí con su `_v9_RESPALDO`. Comandos en `references/ajustes_docx.md`, sección
*Reenvío*.

1. **Revista siguiente.** Si está entre las alternativas de la Ficha, se usa;
   si no, la Fase 0 la verifica en un solo paso (cuartil, alcance, legitimidad,
   APC) antes de seguir.
2. **Perfil nuevo**: `REVISTA_[clave]_[revista].json` desde su guía
   (`references/perfil_revista.md`), validado y confirmado con el autor.
3. **Citas y formato en una orden** (citas por clave): desde el último
   respaldo, `normalizar ARTICULO_[clave]_vN_RESPALDO.docx --perfil
   REVISTA_[clave]_[revista].json --fuentes inventario.json --out
   ARTICULO_[clave]_vN_[revista].docx` reconvierte citas y referencias al
   estilo nuevo (p. ej. APA → Vancouver) y aplica el formato. El respaldo
   nuevo: `normalizar` del mismo respaldo con `--estilo [nuevo] --fuentes
   inventario.json --out ARTICULO_[clave]_vN_[revista]_RESPALDO.docx`. Las citas
   tecleadas a mano (sin clave) se convierten aparte con `reemplazar`
   (`references/estilos_cita.md`): se buscan en `texto` las que siguen en el
   estilo anterior.
4. **Estructura y límite**: secciones con el nombre y nivel exactos del perfil
   (`renombrar`, `mover`, `nivel`, `unir`), recorte si el límite es menor y
   `verificar --perfil`; al final tablas al final y anonimizar si se piden.
5. **Carta nueva** (Paso 3) para la nueva revista; la página de título solo se
   rehace si cambia el formato que pide.
6. Checklist del Paso 6, `CITADAS` de nuevo si cambió la lista, y entrega con
   la Tarjeta: en «Fase cerrada» va «8 · reenvío a [revista]» y en «Reenvío» los
   archivos nuevos (la revista anterior queda solo en «Decisiones»).

## Errores que esta skill previene

1. Enviar por encima del límite o con secciones fuera de orden.
2. Descubrir el APC después de la aceptación.
3. Enviar sin anonimizar (o con el nombre en los metadatos) a doble ciego.
4. Declarar una aprobación ética o un "sin conflicto de intereses" no confirmado.
5. Inventar un ORCID o una filiación.
6. Anunciar cuatro objetivos y reportar tres.
7. Reenviar a otra revista con el formato y el estilo de cita de la anterior.
8. Una carta escrita como folleto publicitario.

## Archivos de referencia

- `references/ruta.md` — Mapa de fases (manda).
- `references/perfil_revista.md` — El perfil de la revista y el respaldo.
- `references/ajustes_docx.md` — Comandos de la `_v8` y del reenvío.
- `references/guia_de_autores.md` — Qué releer de la guía y cuándo.
- `references/declaraciones.md` — Declaraciones y CRediT.
- `references/plantilla_carta.md` — Carta en inglés y en español.
- `references/traduccion.md` — Versión en inglés.
- `references/estilos_cita.md` — APA 7, Chicago, IEEE y Vancouver.
- `references/fuentes_y_citas.md` — Citas por clave, reenvío con otro estilo y vuelta al gestor.
- `references/anti_ia.md` — Humanización.
- `references/formato_docx.md`, `references/documento_en_cadena.md` — El Word.
- `references/estilo_preguntas.md` — Cómo se redactan las opciones.
- `scripts/articulo_docx.py` — Motor del Word. `scripts/ajustar_docx.py` —
  Renombrar, mover, quitar, cambiar de nivel, unir, reemplazar párrafos,
  tablas al final, anonimizar. `scripts/referencias.py` — `CITADAS` para el gestor.

## Tarjeta de continuidad (al cerrar la fase, siempre)

El último mensaje de la fase termina con esta tarjeta, en un bloque de código
para que el usuario la copie. En modo A se guarda además como `ESTADO_[clave].md`.
Máximo 150 palabras; solo datos, sin prosa.

```
TARJETA · Ruta del Artículo · [clave]
Fase cerrada: N · [nombre]      Siguiente: [la que indica ruta.md] · [skill]
Tipo y diseño: ...
Revista: ... · Perfil: REVISTA_[clave].json · Estilo de cita: ... · Límite: ... palabras
Término unificador: ... (solo empíricos)
Archivos vigentes: ARTICULO_[clave]_vN.docx (+ _RESPALDO) · MATRIZ_... · TRAZABILIDAD_...
Fuentes: inventario.json (claves) · Cifras: SALIDAS_[clave].csv/.md (sin redondear)
Reenvío: ARTICULO_[clave]_vN_[revista].docx y REVISTA_[clave]_[revista].json
Decisiones que no se reabren: ...
Pendientes [POR CONFIRMAR]: ...
```

Indicación al usuario, en una línea: *abre un chat nuevo para la siguiente
fase y pega esta tarjeta junto con el último Word*. Un chat por fase ahorra
tokens y evita que el modelo se pierda.
