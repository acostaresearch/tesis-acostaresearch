# Skills de tesis: conector + Zotero (fusión del 15-sep-2026)

Una sola línea de skills de tesis para usar con el conector. Junta dos trabajos que se
habían hecho por separado:

- `skills-solo-conector/tesis` (14-sep): norma de citas guardada en el proyecto, tablas y
  figuras del Word del servidor, lectura de capítulos con `ver_capitulo`.
- El paquete Zotero de la carpeta `skill/` (15-sep, hecho en claude.ai sobre el paquete del
  Live): bloque de claves, `integracion_zotero.md`, biblioteca y Zotero del tesista.

**Publicado.** Al 8-oct, las 14 de `listas-para-subir/` son iguales a las del servidor (incluido el humanizador 4.1). El paquete del Live (Word propio, V1–V8) sigue aparte y no se toca.

## Carpetas

- `fuente/`: las 12 skills sin comprimir. Aquí se edita.
- `listas-para-subir/`: los `.skill` listos para subir. Los regenera `verificar.js`; no se editan.
- `_comun/`: piezas que comparten todas. `verificar.js` las copia a cada skill:
  - `bloque_transversal.md`: la regla del documento del servidor y las claves (ya
    insertada en cada SKILL.md; si se cambia, hay que cambiarla en cada una).
  - `integracion_zotero.md` y `parafraseo.md`: se copian solos a `references/`.
  - `REGLAS-FUSION.md`: las reglas de sincronía con el backend que siguió la fusión.
- `verificar.js`: comprobación y armado.

## Comprobar y armar

```
node skills/tesis/verificar.js            (todas)
node skills/tesis/verificar.js discusion  (una)
```

Qué comprueba:

- parte cada SKILL.md como `partir()` del servidor: los pasos no cambian, ninguna sección
  suelta entre pasos, ningún bloque de código cortado;
- `name` y `description` (máx. 1024);
- que existan los `references/` y `scripts/` que se nombran;
- que solo se nombren herramientas del conector;
- restos del flujo viejo (.docx, V1–V8, citas a mano, `[VERIFICAR…]`…);
- arma el `.skill` y lo pasa por `skillBundle.analizar`, el validador de /admin.

Estado al cerrar la fusión: **0 fallos en las 11**. Los avisos REVISAR que quedan son
legítimos: las prohibiciones del propio bloque, la línea que enseña a reconocer una norma
(«`(Apellido, 2024)` es APA»), los huecos `[PENDIENTE]` de las cartas imprimibles de
recolección y el camino .docx de bajar-similitud para documentos externos.

## 29-sep-2026: el servidor cuenta, Claude escribe

Nueve skills dejaron de imprimir auditorías de patrones y métricas en el chat (17, 22 o 29 comprobaciones): ahora redactan con las reglas y la voz que inyecta `redactar`, guardan, y corrigen con `reescribir_parrafos` los AVISOS DE REDACCIÓN que devuelve `guardar_capitulo`. En marco-teorico los cinco elementos del antecedente siguen siendo obligatorios pero no en orden fijo. bajar-similitud y humanizador-academico (3.5) trabajan con `ver_lo_marcado` sobre el reporte de Turnitin subido (similitud o IA), en el Word subido o en los capítulos. **Necesitan el backend del 29-sep (tarde) desplegado antes de publicarse.** Las 13 pasan verificar.js sin fallos.

## Qué cambió en cada skill

| Skill | Cambios |
|---|---|
| tema-y-delimitacion | Bloque común. `web_search` solo para ideas en el chat; lo que se guarda va con clave. `[PENDIENTE]` fuera del texto guardado. Tabla en bloque APA. Pregunta la norma si falta. |
| problema-y-objetivos | Lee tema con `ver_capitulo`. Búsqueda con `buscar_fuentes` (tema/temaOriginal/pais) y catálogo abierto. Citas por clave en pasos 6.5, 7 y 9B. Sin `[VERIFICAR…]`, sin sección Referencias, sin DXA. Anexo 2 con «1 a 5 (previsto)» y *Nota.*. references reescritas. |
| marco-teorico | Pasos 1–2 del paquete Zotero: sin re-subir .txt/.ris, `mis_fuentes`, `buscar_fuentes`, `buscar_en_la_literatura`, `ampliar_desde_mis_fuentes`, procedencia de cada fuente. Teorías base con clave. Plantilla del capítulo arreglada. |
| metodologia | La matriz ya no se construye: se lee del Anexo 2. Autores clásicos con clave. Plantilla 3.1–3.8 arreglada. Remisiones rotas corregidas. `description` ≤1024. |
| instrumento-investigacion | Lee Anexo 2 y metodología; retira «(previsto)» al confirmar ítems. Plantilla arreglada. `revisar_evidencia` antes del Word. `description` ≤1024. |
| recoleccion-datos | Sigue entregando los materiales imprimibles. Ya no dice que guarda capítulo: `guardar_avance`, y solo si cambió el procedimiento corrige el 3.6 de metodología. |
| analisis-datos-rstudio | Sesión de R del servidor como vía preferente (`trabajar_en_r`, `guardar_analisis`, `ver_analisis`). El capítulo se guarda con `guardar_capitulo`; el informe de R no lo sustituye. Tramos sueltos arreglados. `baremos.md` en lugar del `paso5_niveles.md` que faltaba. `description` ≤1024. |
| discusion | `revisar_evidencia` antes de redactar y después de guardar. Solo autores con clave. Plantilla arreglada. `description` ≤1024. |
| conclusiones-abstract | `revisar_evidencia` de toda la tesis antes del Word. Plantilla arreglada. `description` ≤1024. |
| humanizador-academico | **v4.1 (6-oct): por bloques y sin reporte de IA.** Enseña hasta diez párrafos con ANTES y AHORA, el tesista aprueba el bloque en un mensaje y se guarda solo lo aprobado; la entrada es `ver_lo_marcado` con «rojo» o «todo» (el servidor ya no acepta el reporte de IA y trata «ia» como «todo»). Sigue en un solo tramo, sin `## `. **Necesita el backend del 6-oct (reporte de IA retirado) desplegado antes de publicarla.** **v4.0 (30-sep): de una vez por defecto.** La 3.5 pesaba 80 000 caracteres y el servidor la entregaba en 24 tramos (sin «Paso», cada `##` es uno), con el modo rápido en el segundo detrás del banner; y las herramientas pedían aprobación por bloques. Claude acababa en bloques de 9 párrafos con ANTES/AHORA/TRAZA. Ahora son 12 600 caracteres **sin ningún `## `** (un solo tramo), la entrada es `ver_lo_marcado` («ia», «rojo» o «todo», este nuevo: toda la prosa sin reporte) y cada tanda se guarda sin enseñarla. Catálogo de patrones condensado; la 3.5 queda en el historial de esta tabla. **Necesita el backend del 30-sep («todo» en `ver_lo_marcado`).** No añadir `## ` a esta skill. v3.4 (29-sep): con el reporte de IA de Turnitin (PDF) subido por el enlace del Word, humaniza de una vez solo lo marcado (`ver_mi_documento` con `solo_marcados`); el servidor da las reglas y la voz y revisa oraciones idénticas y muletillas. **Necesita el backend del 29-sep desplegado antes de publicarla.** v3.2 (16-sep): también humaniza el Word que el tesista subió a su perfil, con `ver_mi_documento` y `humanizar_mi_documento`; el servidor escribe los párrafos dentro de su mismo Word conservando el formato. Prohíbe editar con python-docx un .docx adjunto en el chat. **Necesita el backend con `humanizar_mi_documento` desplegado antes de publicarla.** v3.1: método de la v3.0 intacto; lee y guarda capítulos (tope de 30.000 y `anadir`); claves protegidas párrafo a párrafo. `medir.py` neutraliza claves y compara antes/después (`--claves`). |
| mapeo-bibliometrico | **Nueva el 21-sep.** Herramienta de apoyo (título sin número): mapeo con bibliometrix en la sesión de R del servidor. Uso breve (subapartado de 2.1 Antecedentes en `marco-teorico`, que se re-guarda entero) o completo (tesis de revisión: Resultados en `analisis-datos-rstudio`, protocolo en lo acordado de `metodologia`). Lo ejecutado se guarda en su propio análisis (`mapeo-bibliometrico`), no en el de Resultados. Sin publicar ni E2E. |
| aspectos-administrativos | **Nueva el 1-oct.** Sección del PROYECTO (después de Metodología, antes de Referencias): recursos, presupuesto con las cuentas a la vista, financiamiento y cronograma en meses (máx. 8 columnas), en tablas APA. Todo sale de la metodología guardada; precios, fondos y fechas los pone el tesista; clasificador del MEF solo si la guía lo pide y comprobado en la web. Clave `aspectos-administrativos`, 8 pasos. Sin publicar ni E2E. **Backend hecho el 1-oct, sin desplegar**: sale detrás de Metodología y deja de imprimirse con resultados, discusión o conclusiones guardados salvo que el esquema la nombre (`SOLO_DEL_PROYECTO`); en `ORDEN` y en `REGLAS` del Word subido. Publicar solo tras desplegar ese backend, con displayName «4B · Aspectos administrativos». |
| bajar-similitud | **30-sep: un solo tramo** (antes 14: sin «Paso», cada encabezado de segundo nivel era uno y el camino rápido iba en el tercero). Ahora no lleva encabezados de segundo nivel, empieza por el camino con el reporte (con el umbral de la universidad en la primera pregunta) y guarda por tandas sin pedir aprobación de cada bloque, también sin reporte. Dos caminos: tesis del proyecto (lee y guarda en el servidor) o documento externo (.docx). Scripts aceptan .txt/.md y controlan claves. |

Arreglos que no eran de Zotero y ya venían rotos en el conector: en siete skills la plantilla
del capítulo tenía líneas «## 2.1…» dentro de un bloque de código y el servidor la entregaba
partida (metodología salía en 23 tramos en vez de 15); cuatro descripciones pasaban de 1024
caracteres; siete skills nombraban un `parafraseo.md` que no llevaban.

## Pendiente

- **Probar de punta a punta** con un capítulo real: que las claves salgan como citas en el
  Word, que `revisar_evidencia` las cruce, y que el Anexo 2 viaje de problema a metodología
  e instrumento.
- **Numeración que decide el método**: instrumento numera su capítulo 5.x y discusión
  también 5.x; tema y problema guardan cada uno su «Tabla 1». El servidor no renumera.
- **El camino .docx** de los scripts de bajar-similitud no se probó (falta python-docx).
- **Artículo**: estas son solo las de tesis.

## Antes de publicar

1. `npm run backup:traer` en el backend.
2. Comprobar en solo lectura que las licencias de tesis siguen en `INSTRUCTIONS`.
3. Pasos que cambian respecto a lo que se cree publicado (`skills-tesis+humanizador`):
   tema 6 → 7 y problema 14 → 15 (vienen de la v6); análisis se entregaba en 12 tramos y
   queda en 10. Quien esté a mitad de esos capítulos puede saltar de paso.
4. Subir los `.skill` de `listas-para-subir/` por /admin → Capítulos → «Actualizar todos los
   archivos». El servidor reconoce cada skill por su `name`, no por el nombre del archivo.
5. Reconectar el conector en claude.ai para refrescar herramientas si hace falta.
