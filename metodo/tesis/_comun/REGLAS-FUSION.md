# Reglas de la fusión: skills del conector + paquete Zotero

Documento de trabajo para quien edite `fuente/`. No va dentro de ningún .skill.

## De dónde sale cada cosa

- **Base** (lo que hay en `fuente/`): la versión del conector del 14-sep, que ya resolvía
  la norma en el proyecto, las tablas APA del servidor, la marca de figura y la lectura de
  capítulos con `ver_capitulo`. Tema y problema-y-objetivos parten de la versión del
  paquete Zotero, que es la v6 del conector más el bloque de claves.
- **Paquete Zotero** (solo para leer y tomar piezas):
  `C:\Users\Usuario\AppData\Local\Temp\claude\c--Users-Usuario-Documents-acostaresearch\78916cfb-a41a-4a82-8076-0a2e8067ad09\scratchpad\nuevas\<skill>\<skill>\`
  Se construyó sobre el paquete tradicional del Live, así que sus pasos finales vuelven al
  Word propio. De ahí se toman solo las piezas que se indican en cada encargo.
- **Piezas comunes** en `_comun/`. No se editan desde una skill:
  - `bloque_transversal.md`: va en todas las que citan, justo después de «## Para qué
    sirve esta skill» (o de la primera sección de presentación). Se rellenan
    `{{CLAVE}}`, `{{LECTURAS}}` (qué capítulos lee con `ver_capitulo` y `texto: true`) y
    `{{EXCEPCION_ARCHIVOS}}` (vacío salvo en recolección de datos). Si la base ya tiene un
    bloque equivalente, se sustituye por este, no se duplica.
  - `integracion_zotero.md` y `parafraseo.md`: los copia `verificar.js` a `references/`.

## Reglas de sincronía con el backend (duras)

1. **Ninguna línea puede empezar por `## ` salvo las secciones reales.** El servidor corta
   el SKILL.md en cada línea que empieza por `## `, aunque esté dentro de un bloque de
   código. Las plantillas de estructura del capítulo («## 2.1 Antecedentes»…) se escriben
   como lista: `` - `## 2.1 Antecedentes` — qué va ahí ``, o dentro de un bloque de código
   con las líneas sangradas 4 espacios. Los `### ` y `#### ` no cortan.
2. **El número de `## Paso` no cambia** (ver `PASOS_ESPERADOS` en `verificar.js`), y entre
   el primer y el último `## Paso` no puede haber otra sección `## `: el servidor la
   entregaría como tramo suelto.
3. **Solo herramientas que existen**, con sus parámetros reales
   (`backend/src/modules/mcp/mcp.tools.js`):
   - `mi_proyecto` · `listar_capitulos` · `continuar` · `estado_licencia`: sin argumentos.
   - `ver_capitulo`: `capitulo`, `texto` (true = leer lo guardado), `parte`.
   - `guardar_avance`: `capitulo`, `estado` (PENDIENTE/EN_CURSO/LISTO), `resumen`, `tema`,
     `carrera`, `universidad`, `asesor`, `estiloCitas`, `idiomaCitas`, `datos` (campos por
     capítulo: tema-y-delimitacion: tema, poblacion, ambito, periodo · problema-y-objetivos:
     problemaGeneral, objetivoGeneral, objetivosEspecificos, hipotesis, variables ·
     metodologia: enfoque, diseno, nivel, muestra, muestreo, tecnica, instrumento, analisis ·
     instrumento-investigacion: nombre, dimensiones, items, escala, validez, confiabilidad ·
     analisis-datos-rstudio: pruebas, software, hallazgos).
   - `guardar_capitulo`: `capitulo`, `texto` (Markdown, máx. 30.000 caracteres), `anadir`
     (true desde la segunda parte).
   - `revisar_evidencia`: `capitulo` opcional (sin él, toda la tesis).
   - `redactar`: `capitulo`, `paso`, `referencia` (nombre de un archivo de references/).
   - `buscar_fuentes`: `tema` (inglés), `temaOriginal` (español), `pais`, `desde`, `cuantas`.
   - `mis_fuentes`: `pagina`, `origen` (todas/zotero/subidas).
   - `anadir_a_mis_fuentes`: `dois`.
   - `trabajar_en_r`, `guardar_analisis`, `ver_analisis`, `buscar_en_la_literatura`,
     `ampliar_desde_mis_fuentes`, `ver_mi_documento`, `citar_mi_documento`,
     `formato_de_la_universidad`, `enlace_del_word`: mirar su esquema antes de nombrar un
     parámetro.
   - De claude.ai valen `ask_user_input_v0` y `web_search`.
4. **El texto que se guarda** con `guardar_capitulo`:
   - Markdown con `##`, `###` y `####` para subtítulos, sin título del capítulo ni datos
     personales (los pone el Word).
   - Tablas en un solo bloque sin líneas en blanco: `**Tabla N**`, `*Título*`, cabecera
     `| A | B |`, `|---|---|`, filas, y `*Nota.* …` si hace falta.
   - Figuras en un solo bloque: `**Figura N**`, `*Título*`,
     `[Insertar aquí la Figura N: archivo.png]`, `*Nota.* …`.
   - Entre corchetes solo: claves `[AR…]`, `[FALTA FUENTE]` y la marca de figura.
   - Sin sección «Referencias» escrita a mano (saldría duplicada).
   - Tras guardar: `enlace_del_word`. Antes de entregar: `revisar_evidencia`.
5. **Norma de citas**: se lee de `mi_proyecto`; si falta, se pregunta una vez y se guarda
   con `guardar_avance` (`estiloCitas`). Prohibido convertir, heredar el estilo de otro
   capítulo o renumerar a mano. La sección modelo es el «Paso 9.5 — Norma de citas» de
   `fuente/03-marco-teorico`.
6. **Capítulos anteriores**: se leen con `ver_capitulo` (`texto: true`, y `parte` si viene
   partido). Solo se pide que los pegue si no están guardados. Nunca «súbeme el .docx».
   El «Anexo 2» (matriz de operacionalización) vive dentro del texto guardado de
   `problema-y-objetivos`: se lee con `ver_capitulo` de ese capítulo. Si hay que cambiarlo,
   se lee el capítulo entero, se corrige el anexo y se vuelve a guardar
   `problema-y-objetivos` completo, avisando al tesista.
7. **Fuera**: generar .docx, docx-js, anchos en DXA, `present_files`, `/mnt/user-data`
   (salvo los materiales imprimibles de recolección de datos), versiones V1–V8 del
   documento (V1/V2 como «variable 1/2» sí valen), «recuperación en chat nuevo» a base de
   subir archivos, «(Apellido, año)» como forma de citar en el texto que se guarda,
   `[VERIFICAR EN FUENTE ORIGINAL]`, `[PENDIENTE …]`, «OK PARA GENERAR» (pasa a «OK PARA
   GUARDAR»), preguntar márgenes o tipografía.
8. **Los autores clásicos** (Hernández-Sampieri, Carrasco, Cronbach…) también van con
   clave: se buscan en la biblioteca; si no están, `anadir_a_mis_fuentes` o pedirle que los
   meta en su Zotero; mientras tanto `[FALTA FUENTE]` y aviso en el chat.
9. **La `description`** de la cabecera: máx. 1024 caracteres, sin prometer un .docx ni
   «subir» archivos de capítulos anteriores. `name` no cambia.
10. **No se recorta método.** Lo pedagógico (cómo redactar, criterios, ejemplos,
    auditorías de patrones) se conserva. Solo cambia lo que toca documento, citas,
    entrada de datos y entrega. Si un paso remite a otro («la verificación del Paso 10»),
    ese otro tiene que existir.

## Cómo comprobar

```
node skills/tesis/verificar.js <name-de-la-skill> [otra…]
```

Tiene que terminar sin FALLO. Cada REVISAR se mira a mano: se corrige o se deja solo si es
legítimo (por ejemplo, un ejemplo de lo que NO se hace), y eso se dice en el informe.
