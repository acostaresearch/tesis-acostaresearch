# Plan de trabajo: Ruta del Informe Estudiantil

Borrador del 15 de septiembre de 2026. Todavía no hay skills ni código.

## Qué es

Una ruta nueva, **aparte de tesis y de artículo**, para estudiantes de universidad o de
instituto que tienen que entregar un informe en un curso.

**Cubre dos tipos:**
- **Informe académico de curso:** el docente deja un tema y el estudiante lo investiga en
  fuentes y lo desarrolla.
- **Informe de proyecto o de caso:** el estudiante cuenta un proyecto que hizo en el
  curso, o analiza un caso que le dieron.

**No cubre:** tesis, artículos, informes de laboratorio, visitas técnicas ni prácticas
preprofesionales.

**Va con el conector**, como las skills de `skills-solo-conector`:
- las citas van con clave `[AR…]`;
- la norma de citas se guarda en el proyecto;
- el Word lo arma el servidor.

Es **un producto propio**, con su licencia y su grupo de skills. No se mezcla con la
licencia de tesis ni con la de artículo.

**Las skills de tesis y artículo solo sirven de modelo.** De ahí se copian las reglas y la
forma de escribir, pero ninguna skill de informe llama a una de ellas ni las necesita.

## En qué se diferencia de tesis y artículo

| | Tesis / artículo | Informe estudiantil |
|---|---|---|
| Quién lo pide | Jurado, revista | **El docente, con su consigna y su rúbrica** |
| Extensión | 60–150 páginas / 6.000–9.000 palabras | **5 a 25 páginas** |
| Plazo | Meses | **Días o semanas** |
| Hipótesis, instrumento, muestra | Sí | **No** |
| Fuentes | 20 a 80, indexadas | **5 a 15** confiables, según la consigna |
| Portada | Tesista, asesor, carrera | **Curso, docente, integrantes, ciclo y sección, fecha** |
| Quién escribe | Un investigador | **Un estudiante de primeros ciclos**, a veces en grupo |

La consecuencia de diseño es que **la consigna y la rúbrica mandan**. La ruta empieza
leyéndolas y termina revisando el informe contra ellas, punto por punto.

---

## 1. La ruta

```
  Fase 0 · El encargo: consigna, rúbrica, tema y esquema
  Fase 1 · Las fuentes
  Fase 2 · El desarrollo
  Fase 3 · Análisis y resultados        (proyecto o caso; opcional en el de curso)
  Fase 4 · Introducción, conclusiones y revisión con la rúbrica
  Apoyo   · humanizador-academico · bajar-similitud   (ya existen; se suman al grupo)
```

Cinco fases y no siete ni nueve: un informe de curso se hace en días. Cada fase debe poder
terminarse en una o dos sesiones.

---

## 2. Qué debe contener cada skill

### Fase 0 — `informe-fase0-encargo`

**Qué hace.** Convierte la consigna del docente en un plan con fecha. No redacta el
informe.

**Pasos**

- **Paso 0 — Bienvenida.** Explica la ruta en cinco líneas y avisa de que se empieza por
  lo que pidió el docente.
- **Paso 1 — Quién es.** Universidad o instituto, carrera, ciclo, curso, docente, y si el
  trabajo es individual o en grupo. Si es en grupo, nombres y códigos para la portada.
- **Paso 2 — La consigna y la rúbrica.** Se pide que las suban (foto, PDF o texto). De
  ahí se sacan:
  - tipo de informe;
  - extensión;
  - fecha de entrega;
  - secciones obligatorias;
  - norma de citas;
  - número mínimo de fuentes;
  - criterios con los que se calificará.

  **Sin consigna no se inventa una:** se ofrece la estructura base y se marca
  `[POR CONFIRMAR CON EL DOCENTE]`.
- **Paso 3 — Uso de IA en el curso.** Si la consigna o el sílabo prohíben la IA, se le dice
  con claridad y se ofrece solo orientación: esquema, fuentes, revisión con la rúbrica. No
  se redacta.
- **Paso 4 — Tipo de informe.** Académico de curso, de proyecto o de caso, con una tabla
  de lo que cambia en cada uno.
- **Paso 5 — Tema.** Si es amplio, se delimita (lugar, periodo, aspecto) y se formula una
  pregunta guía o un objetivo. En proyecto o caso, qué problema atiende.
- **Paso 6 — Esquema.** Secciones y subtítulos según el tipo y la consigna. Se le enseña
  y se ajusta con él.
- **Paso 7 — Calendario.** Tareas desde hoy hasta la fecha de entrega, calculadas con la
  fecha actual. Si en grupo, quién hace qué.
- **Paso 8 — Norma de citas y formato.** Se lee en `mi_proyecto`. Si dice «sin elegir»,
  se toma la de la consigna y se guarda con `guardar_avance` (`estiloCitas`). Si el
  docente dio plantilla, `formato_de_la_universidad`.
- **Paso 9 — Guardar y derivar.** `guardar_avance` con tema, tipo, curso, docente,
  integrantes, fecha de entrega, esquema y un resumen de la rúbrica. Deriva a la Fase 1.

**Referencias**
- `tipos_de_informe.md`: estructura base de los tres tipos.
- `leer_la_rubrica.md`: cómo pasar una rúbrica a una lista de criterios verificables.
- `delimitar_tema.md`: embudo corto, adaptado de tesis 01.
- `estilo_preguntas.md`.

**No hace:** no escribe texto del informe y no elige el tema por el estudiante; le
propone opciones.

### Fase 1 — `informe-fase1-fuentes`

**Qué hace.** Consigue las fuentes y le enseña a distinguir una fuente confiable de una
que no se cita.

**Pasos**

- **Paso 1 — Qué sirve y qué no.** Sí: libros, artículos, sitios oficiales, repositorios,
  normas. No: Wikipedia, blogs, apuntes sin autor ni respuestas de una IA. Se explica en
  una tabla corta, sin sermón.
- **Paso 2 — Palabras clave.** En español y en inglés, a partir del esquema.
- **Paso 3 — Buscar.** Con `mis_fuentes`, `buscar_fuentes`, `buscar_en_la_literatura` y
  `ampliar_desde_mis_fuentes`, y con la web para sitios oficiales. Si el docente dio
  lecturas del curso, se suben y entran primero.
- **Paso 4 — Elegir.** Las que elija se guardan con `anadir_a_mis_fuentes`. El mínimo lo
  pone la consigna; si no dice nada, entre 5 y 10.
- **Paso 5 — Qué aporta cada una.** Una tabla: fuente, qué dice, a qué subtítulo del
  esquema sirve.
- **Paso 6 — Cobertura.** Si un subtítulo se queda sin fuente, se avisa ahora y no al
  redactar.
- **Paso 7 — Guardar y derivar.** `guardar_avance` con la tabla de cobertura resumida.

**Referencias**
- `fuentes_confiables.md`.
- `busqueda_basica.md`: versión corta de `busqueda_bases.md` del artículo, sin Scopus
  obligatorio.
- `estilo_preguntas.md`.

**Regla dura:** una fuente se cita por lo que dice su resumen o su texto. Lo que no se ha
leído no se atribuye.

### Fase 2 — `informe-fase2-desarrollo`

**Qué hace.** Redacta el cuerpo del informe, que cambia según el tipo.

| Tipo | Contenido del desarrollo |
|---|---|
| Académico de curso | Un apartado por subtítulo del esquema. Cada uno con la idea, lo que dicen las fuentes con cita, un ejemplo (de preferencia local) y la postura del estudiante |
| Proyecto | Problema o necesidad, objetivos, propuesta o diseño, desarrollo o implementación, recursos y costos, cronograma |
| Caso | Hechos del caso, problema central, análisis con la teoría del curso, alternativas y la decisión que se recomienda |

**Pasos**

- **Paso 1 — Leer lo guardado.** `ver_capitulo` y `mi_proyecto`: esquema, tipo y fuentes.
  No se vuelve a preguntar nada de eso.
- **Paso 2 — Lo que solo sabe el estudiante.** En proyecto: qué hizo, con qué, qué
  decisiones tomó, qué salió mal. En caso: qué opina. En académico: su postura. **Se le
  pregunta antes de redactar.**
- **Paso 3 — Redactar.** De dos apartados en dos, para que los revise.
- **Paso 4 — Tablas y figuras.** Si ayudan: tablas en bloque APA en Markdown; figuras con
  rótulo y la marca «[Insertar aquí la Figura N: archivo]».
- **Paso 5 — Humanizador.** Obligatorio: `humanizador-academico` y la lista de
  `anti_ia.md`.
- **Paso 6 — Guardar.** `guardar_capitulo` con clave `informe-fase2-desarrollo`, en partes
  si pasa de 30.000 caracteres. Luego `guardar_avance` y `enlace_del_word`.

**Referencias**
- `desarrollo_por_tipo.md`.
- `parafraseo.md`: adaptado de tesis 03.
- `formato_docx.md`: el del artículo, con ejemplos de informe.
- `anti_ia.md`.
- `estilos_cita.md`.

**Regla dura:** en un proyecto no se inventa lo que el estudiante hizo, ni en un caso su
opinión. Si trae poco, se le pregunta; no se rellena.

### Fase 3 — `informe-fase3-analisis-y-resultados`

**Cuándo se usa.** Siempre en proyecto. En caso, si hay datos. En académico de curso, solo
si la consigna pide análisis o comparación; si no, se salta.

**Pasos**

- **Paso 1 — Qué hay.** Resultados, pruebas, mediciones, encuestas del curso, datos del
  caso.
- **Paso 2 — Calcular.** Si hay datos, con `trabajar_en_r` y `guardar_analisis`. Nada de
  cifras de memoria.
- **Paso 3 — Presentar.** Tablas APA y figuras marcadas, cada una mencionada en el texto
  antes de aparecer.
- **Paso 4 — Interpretar.** Qué significa cada resultado, en relación con los objetivos.
- **Paso 5 — Académico de curso, si aplica.** Comparación de posturas o de fuentes, en
  una tabla y en prosa.
- **Paso 6 — Humanizador.**
- **Paso 7 — Guardar.** `guardar_capitulo` con su clave y `enlace_del_word`.

**Referencias**
- `tablas_y_figuras.md`: del artículo 5.
- `resultados_informe.md`.
- `anti_ia.md`.

**Regla:** las cifras se trasladan, no se producen. Sin medición, el resultado se
describe sin números.

### Fase 4 — `informe-fase4-cierre`

**Qué hace.** Escribe lo que se escribe al final y revisa el informe entero contra la
rúbrica antes de entregar.

**Pasos**

- **Paso 1 — Leer todo lo guardado.** `ver_capitulo` con `texto: true` de las fases 2 y 3.
- **Paso 2 — Introducción.** Se escribe ahora, cuando ya se sabe qué dice el informe:
  - contexto;
  - objetivo o pregunta guía;
  - por qué importa;
  - cómo está organizado el informe.
- **Paso 3 — Conclusiones.** Una por objetivo o por subtítulo, sin datos nuevos y sin
  citas nuevas.
- **Paso 4 — Recomendaciones.** Solo si la consigna las pide.
- **Paso 5 — Resumen.** Solo si la consigna lo pide, con palabras clave.
- **Paso 6 — Anexos.** Lista de lo que va al final: evidencias del proyecto, datos,
  material del caso.
- **Paso 7 — Revisión con la rúbrica.** Una tabla: criterio, dónde se cumple en el
  informe, qué falta. Lo que falta se corrige o se le dice con claridad.
- **Paso 8 — Lista de entrega.**
  - Extensión.
  - Norma de citas.
  - Todas las citas con clave.
  - Ningún `[POR CONFIRMAR]` sin resolver.
  - Portada con integrantes.
  - Fecha.
- **Paso 9 — Guardar y entregar.** `guardar_capitulo` y `enlace_del_word`, con una línea
  de qué trae el Word.

**Referencias**
- `introduccion_y_conclusiones.md`.
- `revision_con_rubrica.md`.
- `anti_ia.md`.

---

## 3. Reglas comunes a las cinco skills

Se copian de las fases del artículo, que son las más limpias con el conector.

**Cabecera del SKILL.md**
- `name:` con prefijo `informe-`. El servidor reconoce la skill por ese nombre.
- `description:` con qué hace, qué entrega y la línea «ACTIVAR con …». Frases del
  estudiante: «tengo que hacer un informe», «el profe dejó un trabajo sobre…», «informe
  de mi proyecto», «análisis de caso».
- `metadata:` con `version`, `fase` y
  `ruta: "Ruta del Informe Estudiantil — Acosta | IA & Research"`.

**Secciones, en este orden**
- «Para qué sirve», con el mapa de la ruta y «← estás aquí».
- «Regla del acompañamiento».
- «Regla de oro: veracidad».
- «Economía de la sesión».
- «Lo que esta skill NO hace».
- Los pasos, cada uno con `## Paso N — …`, porque el conector parte la skill en tramos
  por esos encabezados. No escribir «## Paso» dentro de los bloques de ejemplo.
- «Errores que esta skill previene».
- «Archivos de referencia».

**Tono**
- El estudiante es de primeros ciclos. Un paso por turno.
- Toda pregunta con opción «No me queda claro, ponme ejemplos».
- Nada de jerga de tesis: ni «variables», ni «operacionalización», ni «matriz de
  consistencia».

**Veracidad**
- Nada se inventa: ni fuentes, ni cifras, ni lo que hizo el estudiante.
- Lo que falta va como `[POR CONFIRMAR: …]` y lo que no tiene fuente como `[FALTA FUENTE]`.

**Citas**
- Siempre con clave (`[AR…]`, `[AR…:n]`, `[AR…:p. 45]`).
- La lista de referencias nunca se escribe a mano.

**Word**
- Nunca se arma con código. Se guarda con `guardar_capitulo` y se entrega con
  `enlace_del_word`.

**Grupo**
- Si el informe es grupal, las decisiones las confirma quien lleva la sesión. La skill no
  reparte culpas ni califica a los integrantes.

**Derivación**
- Si aparecen «tesis», «asesor», «jurado» o «hipótesis», se deriva a la ruta de tesis.
- Si aparecen «revista» o «revisores», se deriva a la de artículo.
- Si aparecen «laboratorio» o «prácticas», se dice que esta ruta no los cubre todavía.

### Referencias compartidas

Se escriben una vez en `informe/_comun/` y se copian en cada skill.

| Archivo | Sale de | Qué cambia |
|---|---|---|
| `estilo_preguntas.md` | artículo | Ejemplos de estudiante |
| `estilos_cita.md` | artículo | Nada |
| `anti_ia.md` | artículo | Nada |
| `formato_docx.md` | artículo | Ejemplos de informe |
| `informe_en_cadena.md` | `documento_en_cadena.md` | Claves `informe-*`, sin portada de tesis |
| `tipos_de_informe.md` | nuevo | Estructura base de académico, proyecto y caso |

---

## 4. Cambios en el backend

Sin estos cambios, las skills no se pueden vender aparte o el Word sale como una tesis.

1. **Producto propio.**
   - Plan `LICENSE` con `productCode` nuevo (`INFORME_ESTUDIANTIL`) y
     `delivery = INSTRUCTIONS`.
   - Grupo con las 5 fases más `humanizador-academico` y `bajar-similitud`.
   - Precio pensado para estudiantes.
2. **Cómo se nombra al usuario y a su obra.** Hoy el código solo distingue artículo o
   tesis: [mcp.tools.js:594](../../backend/src/modules/mcp/mcp.tools.js#L594) (`esArticulo`,
   `SU_OBRA`) y [project.consejos.js:215](../../backend/src/modules/projects/project.consejos.js#L215).
   Hay que pasarlo a una función por producto: «su informe», «el estudiante». Muchas
   descripciones de herramientas dicen «tesista» escrito a mano; hay que revisarlas.
3. **Datos del proyecto.** `guardar_avance` y `mi_proyecto` tienen que aceptar y devolver
   estos datos, que hoy no existen:
   - curso;
   - docente;
   - integrantes, con su código;
   - ciclo y sección;
   - fecha de entrega;
   - tipo de informe.
4. **Portada y títulos del Word.**
   - [project.docx.js:471](../../backend/src/modules/projects/project.docx.js#L471) arma la
     portada de tesis (tema, carrera, universidad, nombre, asesor). El informe necesita
     institución, programa, curso, tema, docente, integrantes, ciclo y sección, ciudad y
     fecha.
   - Sin «Capítulo I».
   - Índice solo si el informe es largo.
   - El artículo tiene el mismo pendiente: conviene resolver la portada por producto para
     los dos a la vez.
5. **La introducción va primero pero se escribe al final.** El Word ordena por skill, y
   `guardar_capitulo` solo acepta claves de skills del grupo. Si la Fase 4 la guarda con
   su clave, la introducción sale al final del Word. Hay dos salidas:
   - **(a)** Que `guardar_capitulo` acepte una sección `introduccion` para este producto y
     el Word la ponga delante. **Recomendada.**
   - **(b)** Una skill mínima `informe-introduccion` con orden 1, que solo sirve de clave.

   Hay que decidir antes de escribir la Fase 4.
6. **Título de las secciones.** El servidor titula cada sección con el nombre de la fase
   («Desarrollo»). En un informe de curso los títulos deberían ser los del esquema. Hay
   que ver si basta con que la skill guarde sus subtítulos como `##` o si hay que ocultar
   el título de la fase.
7. **Revisión.** `revisar_la_tesis` y `revisar_evidencia` asumen objetivos e hipótesis de
   tesis. Se dejan fuera del grupo, o se adaptan para revisar contra la rúbrica guardada.
8. **Zotero.** Etiqueta `informe` en `ETIQUETAS_DE_PRODUCTO`
   ([reference.repository.js:8](../../backend/src/modules/references/reference.repository.js#L8)).
9. **Web y asistente.**
   - Página del producto.
   - Tienda.
   - Panel «Mi informe».
   - `metodo.ts`.
   - `asistente.conocimiento.js`.
10. **Tests.** Los del MCP, del proyecto y del Word con el nuevo producto. `npm test`
    completo, sin recortar.

---

## 5. Etapas del trabajo

| Etapa | Qué se hace | Entregable | Depende de |
|---|---|---|---|
| **0. Insumos** | Juntar 5 a 8 consignas y rúbricas reales de cursos (universidad e instituto) y 3 informes aprobados. Decidir el punto 5 de la sección 4 y el precio. | Estructura base confirmada | — |
| **1. Base común** | Plantilla de SKILL.md y referencias de `_comun/` | `informe/_comun/` | 0 |
| **2. Fases 0 y 1** | Redactar y revisar | 2 skills | 1 |
| **3. Fases 2 y 3** | Redactar; son las que más cuidado piden en veracidad | 2 skills | 2 |
| **4. Fase 4 y LEEME** | Redactar; añadir `informe/` al `LEEME.md` de `skills-solo-conector` | 1 skill + LEEME | 3 |
| **5. Backend** | Sección 4, con tests. Va en paralelo a las etapas 2 a 4. | Commit, sin desplegar | 0 |
| **6. Web** | Página, tienda y panel | Commit, sin desplegar | 5 |
| **7. Empaquetar** | Un `.skill` por fase: zip con `carpeta/SKILL.md` y `references/`. Comprobar que `leerFrontmatter` lee el `name` y que `contarPasos` da los pasos esperados. | 5 `.skill` | 4 |
| **8. Prueba de punta a punta** | Dos casos ficticios: un informe académico de curso en grupo y un informe de proyecto individual, desde la Fase 0 hasta el Word. Con la licencia de ADMIN, una o dos sesiones en serie. | Lista de fallos | 5, 6, 7 |
| **9. Publicar** | `npm run backup:traer`; backend y web juntos; crear el grupo y subir las skills desde `/admin` → Capítulos. | En producción | 8 |

---

## 6. Riesgos

- **Integridad académica.** Un informe de curso evalúa lo que aprendió el estudiante. La
  ruta está hecha para que lo que solo él sabe lo aporte él: qué hizo, qué opina, qué
  concluye. Además, el Paso 3 de la Fase 0 respeta la política de IA del curso.
- **Consignas vagas.** Muchos docentes dan una línea. La estructura base y la marca
  `[POR CONFIRMAR CON EL DOCENTE]` lo cubren sin inventar requisitos.
- **Fuentes pobres.** El estudiante trae Wikipedia y blogs. La Fase 1 lo resuelve antes
  de redactar.
- **Plazos cortos.** Si la entrega es mañana, la Fase 0 lo detecta y ofrece un camino
  mínimo: esquema, fuentes, desarrollo y cierre en una sesión cada uno.
- **Word con cara de tesis** hasta que se hagan los puntos 3 a 6 de la sección 4.
