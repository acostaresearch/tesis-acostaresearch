# Plan de programación: Informe Estudiantil

Borrador del 15 de septiembre de 2026. **Todavía no se ha programado nada.**

El contenido de las skills está en [PLAN-SKILLS-INFORME.md](PLAN-SKILLS-INFORME.md). Este
documento dice qué hay que cambiar en el backend y en la web, en qué orden, y cómo se
garantiza que **tesis, artículo y las bolsas de palabras siguen exactamente igual**.

Las rutas de archivo son relativas a `backend/` o a `acostaresearch-frontend/`. Las líneas
se leyeron el 15-sep y pueden haberse movido: se vuelven a mirar antes de tocar cada
archivo.

---

## 0. La regla que manda: no mover los productos que ya existen

1. **Todo lo nuevo es aditivo.**
   - Columnas nuevas nulas.
   - Herramientas y campos nuevos registrados **solo** para el producto de informe.
   - Ninguna columna existente se renombra ni se borra.
2. **Lo que hoy decide «tesis o artículo» pasa a un perfil de producto.** Tesis y artículo
   devuelven exactamente lo mismo que hoy. El perfil de informe es el único nuevo.
3. **Antes de tocar nada, se congelan tesis y artículo en pruebas** (Etapa A). Cada etapa
   siguiente tiene que pasar esas pruebas sin cambiarles una letra. Si una prueba de tesis o
   de artículo cambia, el cambio está mal.
4. **Una etapa, un despliegue.** Nada de juntar cuatro etapas en un solo despliegue.
5. **Mientras dure el piloto, el informe solo lo ve una cuenta**, `esteban.dioses@tecsup.edu.pe`.
   No sale en la tienda, en el asistente ni en el conector de otros administradores.

---

## 1. Lo que encontré en el código y obliga a este orden

| Hallazgo | Dónde | Consecuencia |
|---|---|---|
| **Una skill sin grupo la ve cualquier licencia** | `skill.service.js:54-57` y `:109-112` | Si una skill de informe se sube sin grupo, aparece en los conectores de tesis y de artículo. Siempre se sube ya asignada al grupo `INFORME_ESTUDIANTIL`. |
| Un plan activo sale en la tienda, en el asistente, se puede comprar escribiendo su código y **se le da a todos los administradores** | `billing.repository.js:43-49`, `asistente.service.js:45`, `payment.service.js:68-71`, `manual.service.js:118-121`, `license.service.js:325-329` | Hace falta la marca «en prueba» (Etapa B) **antes** de crear el plan. |
| Un plan inactivo le revoca la licencia al propio administrador | `license.service.js:388-395` | No sirve dejarlo inactivo para esconderlo. |
| El catálogo público de skills lista cualquier grupo | `skill.controller.js:12` (`/skills/catalogo?grupo=`) | Hay que esconder ahí el grupo en prueba. |
| Todo lo que no empieza por `ARTICULO` recibe textos de tesis | `mcp.tools.js:594-595`, `project.consejos.js:94-95` y `:215` | Hace falta el perfil de producto (Etapa C). |
| No hay un sitio central para los textos. `mcp.tools.js` tiene 134 líneas con «tesista», «tesis» o «jurado». | `mcp.tools.js` | En el piloto solo se adaptan las herramientas que más se ven. El resto, al salir del piloto. |
| El proyecto no tiene curso, docente, integrantes ni fecha de entrega | `schema.prisma:1171-1223` | Hace falta una columna nueva (Etapa D). |
| `guardar_avance` descarta `datos` de skills que no están registradas en `ETAPAS` | `project.etapas.js:245-270` | Hay que registrar las etapas del informe o guardar su ficha aparte. |
| El Word ordena las secciones por `Skill.orden` y titula cada una con el `displayName` | `project.service.js:563-655` | La introducción, que se escribe al final, saldría al final (Etapa E). |
| La portada es la de tesis | `project.docx.js:473-492` y `:608-610` | Portada por producto (Etapa E). |
| Todas las herramientas se registran para todas las licencias, y hay una prueba que exige **22** | `mcp.tools.js`, `mcp.descripciones.test.js:246-269` | El registro condicionado solo puede cambiar el informe. Tesis tiene que seguir en 22. |
| En la web, «tesis» está escrito a mano en el panel del usuario | `mi-tesis.html:37,49,298,403`, `mi-tesis.ts:409,429` | Textos por tipo de producto (Etapa G). |
| Los desplegables del admin salen de la lista pública de planes | `admin.ts:491` y `:2406-2414` | Un plan en prueba no aparecerá ahí. Para el piloto no hace falta: la licencia de Esteban se emite sola. |
| **Otra sesión está cambiando `armar` en `project.docx.js`** para rellenar el índice | `project.docx.js:56` y `:729-732`, `project.indice.js` sin comitear | La Etapa E espera a que esa sesión comitee. |

---

## 2. Decisiones que te tocan antes de empezar

| # | Decisión | Recomendación |
|---|---|---|
| P1 | Código del producto | `INFORME_ESTUDIANTIL` |
| P2 | Cómo se marca «en prueba» | **Una columna `Plan.soloPara`** con los correos separados por coma, que se edita desde el panel. La alternativa es una variable del `.env`, pero esa hay que tocarla en el servidor cada vez. |
| P3 | Dónde se guardan curso, docente, integrantes, etc. | **Una sola columna JSON nula `Project.fichaInforme`.** Así no se añaden seis columnas que tesis y artículo nunca usarán. |
| P4 | Cómo va la introducción delante | **Secciones extra declaradas en el perfil del informe** (`informe-introduccion` y `informe-resumen`), que acepta `guardar_capitulo` solo para ese producto, y que el Word coloca delante. Así no se crean skills falsas. |
| P5 | Qué hace `revisar_la_tesis` en el informe | En el piloto se registra como `revisar_el_informe` con los chequeos genéricos: citas rotas, capítulos vacíos, cifras. Revisar contra la rúbrica queda para después. |

---

## 3. Etapas

### Etapa A — Congelar tesis y artículo en pruebas. No cambia nada en producción.

**Objetivo:** que cualquier cambio posterior que afecte a tesis o artículo haga fallar una
prueba.

1. **Punto de partida:** `npm test` completo, sin recortar la salida. Se anota cuántas pasan
   y cuántas fallan.
2. **Pruebas de caracterización nuevas, para `METODO_DE_TESIS_HUMANIZADOR` y para
   `ARTICULO_SCIENTIFICOS`:**
   - nombre, título, descripción y esquema de entrada de **todas** las herramientas del
     conector, guardados como instantánea en `tests/instantaneas/`;
   - texto de `mi_proyecto` (`projectService.resumen`) con un proyecto de ejemplo;
   - textos de `project.consejos` (`redactar` de cada consejo);
   - texto del `document.xml` que sale de `armarWord` con dos capítulos y una cita;
   - lista pública de planes (`listPlans`) y licencias que emite `emitirParaAdmin`;
   - catálogo público `/skills/catalogo` con y sin `grupo`.
3. En la web no hay pruebas unitarias del panel. Se hacen **capturas de referencia** de
   `/planes`, `/perfil` (con licencia de tesis y de artículo) y `/admin` para compararlas a
   mano en la Etapa I.

**Archivos:** solo `tests/` nuevos. **Despliegue:** no hace falta, pero se comitea.

### Etapa B — Plan «en prueba». Backend y un campo en el admin.

**Objetivo:** poder crear `INFORME_ESTUDIANTIL` activo sin que nadie más lo vea.

**Backend**
1. **Migración aditiva** `AAAAMMDDHHMMSS_plan_solo_para`, con
   `ALTER TABLE plans ADD COLUMN soloPara VARCHAR(1000) NULL`. Nulo = como hoy.
2. Un único ayudante, `planVisiblePara(plan, email)`, en `billing/` o en `licensing/`.
3. **Filtros.** Cada uno sin efecto cuando `soloPara` es nulo:
   - `billing.repository.js:43-49` (`listPlans` público): excluye los que tienen `soloPara`.
   - `asistente.service.js:45` y `asistente.prompt.js`: los excluye del texto que ve Gemini.
   - `payment.service.js:68-71`, `manual.service.js:118-121` y `billing.service.js:20-26`:
     rechazan comprar o aplicar un descuento a un plan con `soloPara`.
   - `license.service.js:325-329` (`emitirParaAdmin`): un plan con `soloPara` solo cuenta
     para el administrador cuyo correo está en la lista. Para el resto, el producto no
     existe: no se les emite nada y no se les revoca nada, porque nunca lo tuvieron.
   - `skill.controller.js:12` (`/skills/catalogo`): no enseña grupos cuyo plan tenga
     `soloPara`.
   - `product.service.js` y `billing.schema.js`: aceptan `soloPara` al crear y al editar,
     validando que sean correos.
4. **Pruebas:**
   - un plan con `soloPara` no sale en ninguna de esas vías;
   - un plan sin `soloPara` sale exactamente igual que antes (las instantáneas de la Etapa A
     no cambian);
   - Esteban recibe la licencia y otro administrador no.

**Web**
5. `admin.html` y `admin.ts`, en el editor de grupo (`guardarGrupo`, `admin.ts:1197-1262`):
   campo «Solo para (correos)» y un distintivo «En prueba» en la tabla de grupos.

**Despliegue:** primero el backend y después la web, con `git status` limpio justo antes
de publicar. **Se comprueba que la tienda, el asistente y el panel de tesis y artículo se ven
igual que en las capturas.**

### Etapa C — Perfil de producto. Refactor sin cambios visibles.

**Objetivo:** que «tesis o artículo» se decida en un solo sitio y que el informe tenga su
perfil.

1. **Archivo nuevo** `src/modules/productos/producto.perfil.js`, con
   `perfilDe(productCode)`, que devuelve el tipo (`'tesis' | 'articulo' | 'informe'`), la
   obra («su tesis», «su artículo», «su informe»), la persona («el tesista»…,
   «el estudiante») y las secciones extra.
   - Tesis = el perfil por defecto de hoy.
   - Artículo = lo que hoy da `startsWith('ARTICULO')`.
   - Informe = `INFORME_ESTUDIANTIL`.
2. **Sustituir** `esArticulo` y `SU_OBRA` en `mcp.tools.js:594-595`, y `obra` en
   `project.consejos.js:94-95` y `:215`, por el perfil. **Las instantáneas de la Etapa A no
   pueden cambiar.**
3. **Prueba del perfil:** cada código conocido da su tipo, y un código desconocido da tesis,
   como hoy.

**Despliegue:** solo backend. Se comprueba que las instantáneas siguen iguales.

### Etapa D — La ficha del informe en el proyecto

**Objetivo:** que el conector guarde y enseñe curso, docente, integrantes, ciclo y sección,
fecha de entrega y tipo de informe.

1. **Migración aditiva:** `ALTER TABLE projects ADD COLUMN fichaInforme JSON NULL`.
2. **`guardar_avance`** (`mcp.tools.js:200-278`, `project.schema.js:20-65`,
   `project.service.js:445-491`): la propiedad `informe` se añade al esquema **solo si el
   perfil es informe**. Contiene `curso`, `docente`, `integrantes[{nombre, codigo}]`,
   `cicloSeccion`, `fechaEntrega`, `tipo` (curso | proyecto | caso) y `rubrica` (resumen de
   hasta 1.500 caracteres). El esquema de tesis y artículo no cambia.
3. **`mi_proyecto`** (`project.service.js:235-334`): con el perfil de informe se enseñan las
   líneas de la ficha y los días que faltan para la entrega, y no la línea del asesor
   (`lineaDeAsesor`, `:183-194`).
4. **Etapas:** se registran `informe-fase0` a `informe-fase4` en `project.etapas.js` con sus
   campos mínimos, para que `datos` no se descarte. Son entradas nuevas y no tocan las de
   tesis.
5. **Pruebas:** guardar y leer la ficha; que tesis y artículo sigan sin la propiedad
   `informe` en su esquema.

**Despliegue:** solo backend.

### Etapa E — El Word del informe

**Requisito:** que la otra sesión haya comiteado su cambio del índice en `project.docx.js`.

1. **Portada.** `armar` (`project.docx.js:578-732`) recibe un parámetro opcional
   `portadaDe`, que por defecto es la `portada()` de hoy.
   - `armarWord` le pasa `portadaInforme` solo si el perfil es informe.
   - Contenido: institución, programa, curso, tema, docente, integrantes con código, ciclo y
     sección, ciudad y fecha.
   - Si el estudiante sube la plantilla de su institución, su portada sigue mandando, como
     hoy.
2. **Secciones extra (P4).**
   - `guardar_capitulo` y `ver_capitulo` (`mcp.tools.js:782-863` y `:940-991`) aceptan
     `informe-resumen` e `informe-introduccion` **solo** con el perfil de informe.
   - `armarWord` las coloca delante de las fases, en ese orden.
   - Antes hay que comprobar que `ProjectStage.skillCode` no es clave foránea de `Skill`;
     si lo es, hay que cambiar de enfoque.
3. **Detalles del informe:**
   - nombre del archivo `informe` en vez de `tesis` (`project.docx.js:824-837`);
   - título de respaldo «Informe» (`:486` y `:662`);
   - el índice solo si pasa de cierto número de secciones.
4. **Pruebas:**
   - Word de informe con portada, resumen, introducción, desarrollo, cierre y referencias,
     en ese orden;
   - las instantáneas de Word de tesis y artículo no cambian;
   - las pruebas de plantilla (`proyecto.plantilla*.test.js`, `proyecto.portada-auto.test.js`)
     siguen pasando.

**Despliegue:** solo backend.

### Etapa F — Herramientas del conector para el informe

1. **Registro por perfil.** Tesis se queda en 22 herramientas y artículo igual que hoy. El
   informe:
   - `revisar_el_informe`, en vez de `revisar_la_tesis`, con descripción de informe;
   - `revisar_evidencia` se queda, con descripción sin «discusión» ni «jurado»;
   - `formato_de_la_universidad` conserva el nombre (renombrarla rompería skills), pero su
     descripción dice «universidad o instituto».
2. **Descripciones de informe** para las herramientas que más se ven: `mi_proyecto`,
   `guardar_capitulo`, `ver_capitulo`, `enlace_del_word`, `redactar`, `guardar_avance`,
   `listar_capitulos`. Salen de `perfil.textos` y tesis sigue leyendo su texto de siempre.
   **Las otras 120 líneas con «tesista» se aceptan en el piloto** y se reescriben al salir
   de él.
3. **Consejos** (`project.consejos.js:130-135`): «formato de su universidad o instituto» con
   el perfil de informe.
4. **Zotero:** `informe: 'INFORME_ESTUDIANTIL'` en `ETIQUETAS_DE_PRODUCTO`
   (`reference.repository.js:8-12`).
   - Las fuentes sin etiqueta siguen visibles para todos.
   - Una fuente etiquetada solo `informe` desaparece de tesis y de artículo; si sirve a los
     dos, lleva ambas etiquetas.
5. **Pruebas:**
   - `mcp.descripciones.test.js` sigue igual para tesis;
   - una prueba nueva igual para artículo y otra para informe, con su lista de herramientas.

**Despliegue:** solo backend.

### Etapa G — Web mínima para el piloto

1. **`GET /proyectos`** (`project.routes.js`) devuelve `tipo` a partir del perfil. Es un
   campo nuevo que la web vieja ignora.
2. **`mi-tesis.html` y `mi-tesis.ts`:** los textos «Qué tesis usar», «Nueva tesis», «Tu tesis
   en Word», «Tesis principal» y «Otra tesis de…» salen de una función
   `textos(tipo)`.
   - Con `tipo` tesis o artículo devuelve **las mismas cadenas de hoy**, sin retocarlas.
   - Con informe: «Tu informe en Word», etc.
   - En el informe se muestra la ficha (curso, docente, entrega) en lugar de carrera y
     asesor.
3. **No se tocan** durante el piloto:
   - `/planes`, la portada (`home.ts`) y `metodo.ts`;
   - las páginas de producto;
   - el `INCLUYE` de la tienda.

   Se hacen al salir del piloto.

**Despliegue:** solo la web, con `git status` limpio justo antes, porque publica lo que
hay en disco.

### Etapa H — Skills y alta del producto

1. **Redactar las 5 skills** según [PLAN-SKILLS-INFORME.md](PLAN-SKILLS-INFORME.md), con las
   claves de las secciones extra de P4 en la Fase 4.
2. **Empaquetar:**
   - un `.skill` por fase;
   - comprobar el `name` con `leerFrontmatter` y los tramos con `contarPasos`.
3. **Alta, en este orden exacto:**
   1. `npm run backup:traer`.
   2. `/admin` → «Crear grupo» `INFORME_ESTUDIANTIL`:
      - activo;
      - entrega `INSTRUCTIONS`;
      - **«Solo para» `esteban.dioses@tecsup.edu.pe`**;
      - precio simbólico, que no se puede comprar igual.
   3. En la ventana del grupo, **subir las 5 skills ya asignadas a ese grupo**. Nunca subirlas
      sueltas: sin grupo las verían todos.
   4. Añadir `humanizador-academico` y `bajar-similitud` al grupo, marcándolas en «Capítulos
      que incluye». Siguen en sus grupos de siempre.
   5. Esteban entra en su panel: se le emite la licencia y recibe el correo con la URL del
      conector.

### Etapa I — Prueba de punta a punta y comprobación de que nada se movió

**Del informe**, con la cuenta de Esteban y en una o dos sesiones seguidas:
- un informe académico de curso en grupo, desde la Fase 0 hasta el Word;
- un informe de proyecto individual con datos y `trabajar_en_r`.

**De los productos que ya existen**, en una lista que se marca al terminar:
- [ ] `/planes` sin sesión: no aparece el informe.
- [ ] El asistente de la web, preguntado por precios: no lo menciona.
- [ ] `POST` de compra con `planCode=INFORME_ESTUDIANTIL`: rechazado.
- [ ] `/skills/catalogo?grupo=INFORME_ESTUDIANTIL`: vacío.
- [ ] Otro administrador, si existe: no recibe la licencia.
- [ ] Conector de tesis: `listar_capitulos` y `mi_proyecto` igual que antes, sin skills
      `informe-*`.
- [ ] Conector de artículo: igual.
- [ ] Word de una tesis y de un artículo de prueba: igual que antes.
- [ ] `/perfil` con licencia de tesis y de artículo: igual que en las capturas de la
      Etapa A.
- [ ] `https://acostaresearch.com/` y `guias/guia-instalacion.pdf`: 200 con su tipo.

### Etapa J — Salir del piloto (más adelante, cuando lo digas)

- Vaciar «Solo para» del plan y fijar el precio.
- Página del producto, tarjeta en la tienda y `INCLUYE`.
- `metodo.ts` y `asistente.conocimiento.js`.
- Reescribir las descripciones de herramientas que siguen diciendo «tesista» para el
  informe.
- Revisión del informe contra la rúbrica guardada.

---

## 4. Archivos que se tocan, por riesgo

| Riesgo para tesis y artículo | Archivos | Cómo se controla |
|---|---|---|
| **Alto** | `mcp.tools.js`, `project.docx.js`, `project.service.js` (`resumen`, `armarWord`), `license.service.js` (`emitirParaAdmin`) | Instantáneas de la Etapa A; cambios solo detrás de `perfil.tipo === 'informe'` o de `soloPara` no nulo |
| Medio | `project.consejos.js`, `billing.repository.js`, `payment.service.js`, `manual.service.js`, `asistente.*`, `skill.controller.js`, `mi-tesis.*`, `admin.*` | Pruebas de filtro con `soloPara` nulo; capturas de la web |
| Bajo | `project.etapas.js` (entradas nuevas), `reference.repository.js` (etiqueta nueva), `producto.perfil.js` (nuevo), migraciones aditivas | Pruebas propias |

## 5. Orden y despliegues

```
A (pruebas) ─► B (en prueba) ─► C (perfil) ─► D (ficha) ─► E (Word)* ─► F (herramientas) ─► G (web)
                                                                                            │
                                     H (skills: se pueden redactar desde ya, en paralelo) ──┴─► I (prueba) ─► J
* E espera a que la otra sesión comitee su cambio en project.docx.js
```

**Cada despliegue:**
- `npm test` completo;
- `git add` archivo por archivo;
- `git status` antes de comitear y, en la web, justo antes de publicar.

Si aparece algo que no es de esta tarea, se para y se pregunta.

## 6. Lo que queda por comprobar al empezar

- Si `ProjectStage.skillCode` es clave foránea de `Skill`. Decide cómo se hace P4.
- Si hay otros administradores además de Esteban. Se mira en el panel, no con consultas a
  la base de producción.
- El número actual de pruebas: la guía de despliegue dice 244, pero hoy hay 80 archivos y
  bastantes más pruebas.
