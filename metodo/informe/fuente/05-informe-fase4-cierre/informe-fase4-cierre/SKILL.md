---
name: informe-fase4-cierre
description: Última fase de la Ruta del Informe de Acosta | IA & Research, para informes de curso y de empresa. Escribe lo que va al final y revisa el informe entero antes de entregar: conclusiones, recomendaciones, introducción y resumen. En un curso, recomendaciones y resumen si la consigna los pide, y revisión criterio por criterio con la rúbrica. En una empresa, recomendaciones priorizadas con responsable, plazo, costo e indicador, plan de acción, riesgos, limitaciones, un resumen ejecutivo de una página con la decisión que se pide, y revisión contra los términos de referencia, de cifras y de tono. Guarda la introducción y el resumen aparte, que el Word pone delante, lista los anexos y da el enlace del informe. ACTIVAR con "conclusiones de mi informe", "haz la introducción", "revisa mi informe con la rúbrica", "ya casi entrego", "las recomendaciones", "el plan de acción", "el resumen ejecutivo".
---

# Fase 4 — Conclusiones

## Para qué sirve esta skill

Es la última fase de la **Ruta del Informe**. Escribe lo que se redacta cuando ya se sabe qué
dice el informe, y lo revisa antes de entregar.

```
  Fase 0 · El encargo
  Fase 1 · Las fuentes y la evidencia
  Fase 2 · El desarrollo
  Fase 3 · Análisis y resultados
  Fase 4 · Cierre: conclusiones, recomendaciones y revisión   ← estás aquí
```

**Qué ámbito es:** si `mi_proyecto` dice «Ámbito: empresa», es de empresa; si no lo dice, es de
curso. Algunos pasos son de un solo ámbito y lo dicen en su título: se saltan en el otro.

| | Curso | Empresa |
|---|---|---|
| Conclusiones | Siempre | Siempre |
| Recomendaciones | Si la consigna las pide | **Siempre**, priorizadas |
| Plan de acción y riesgos | — | **Siempre** |
| Limitaciones | — | **Siempre** |
| Introducción | Siempre | Siempre, con el alcance |
| Resumen | Si la consigna lo pide | **Resumen ejecutivo, siempre**: la página que más se lee |
| Revisión | Contra la rúbrica | Contra los términos de referencia, de cifras y de tono |

El Word sale en este orden: portada, índice, **resumen**, **introducción**, desarrollo, análisis
y resultados (si hay), **conclusiones** (con las recomendaciones, el plan de acción y las
limitaciones como subtítulos), referencias. Los anexos se pegan en Word al final.

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un archivo de Word, un PDF ni ningún otro archivo del informe.**

Esta fase guarda **tres textos distintos**, cada uno con su clave:

```
CLAVE                    QUÉ LLEVA                         DÓNDE SALE EN EL WORD
───────────────────────  ────────────────────────────────  ─────────────────────
informe-resumen          el resumen y las palabras clave   primero, tras el índice
                         (curso, si se pide) o el resumen
                         ejecutivo (empresa, siempre)
informe-introduccion     la introducción                   antes del desarrollo
informe-fase4-cierre     conclusiones, y según el caso     después de los
                         recomendaciones, plan de acción,  resultados
                         riesgos y limitaciones
```

`informe-resumen` e `informe-introduccion` son **secciones aparte**: no salen en
`listar_capitulos`, pero `guardar_capitulo` y `ver_capitulo` las aceptan en el informe, y
`mi_proyecto` dice si ya tienen texto.

```
1. mi_proyecto          al abrir (ficha con la rúbrica o los términos, norma,
                        secciones aparte)
2. ver_capitulo         con texto: true: informe-fase2-desarrollo e
                        informe-fase3-analisis-y-resultados (si existe)
3. material_del_curso   releer la consigna y la rúbrica, o los términos
4. guardar_capitulo     informe-fase4-cierre, informe-introduccion
                        e informe-resumen
5. revisar_el_informe   repaso del informe entero
6. revisar_evidencia    sin capítulo: todo el informe
7. enlace_del_word      el informe completo
```

**Citas por clave**, nunca escritas a mano. En las conclusiones no se cita (no llevan ideas
nuevas); en la introducción, solo lo necesario para el contexto; **el resumen ejecutivo no
lleva citas**. **Entre corchetes solo** claves, `[FALTA FUENTE]`, en empresa `[FALTA DATO: …]` y
`[POR CONFIRMAR CON LA EMPRESA: …]`, y la marca de figura. **Si un guardado falla, se dice: no
se guardó.** Detalle en `references/integracion_zotero.md`.

## Regla del acompañamiento

- **Un paso por turno.** Preguntas según `references/estilo_preguntas.md`.
- **La revisión se le enseña entera**, aunque salga mal. Mejor ahora que en la nota o en la
  reunión con el cliente.
- **Empresa: las recomendaciones, los responsables y los plazos se acuerdan con él.** Son una
  propuesta, no una asignación.

## Regla de oro: veracidad

1. **Las conclusiones no traen datos, cifras ni citas nuevas.** Todo lo que concluyen ya está en
   el desarrollo o en los resultados.
2. **La introducción anuncia lo que el informe hace, no lo que debería hacer.**
3. **Toda recomendación nace de una conclusión del informe.** Si hace falta decir otra cosa, va
   aparte y se dice que el informe no la cubre.
4. **El resumen no trae nada nuevo:** cada cifra que aparece está igual en el cuerpo.
5. **La revisión no se autocertifica:** cada criterio se comprueba mirando el texto guardado,
   con la sección donde se cumple.
6. **Empresa:** lo que la empresa no puede pagar ni ejecutar no se recomienda; ningún costo se
   inventa; las limitaciones no se suavizan; ninguna promesa de resultado sin cálculo.

## Lo que esta skill NO hace

- **No rehace el desarrollo ni los resultados.** Si la revisión encuentra un hueco, se dice y se
  ofrece volver a esa fase.
- **No calcula.** Si hace falta una cifra nueva, se vuelve a la Fase 3.
- **No pega los anexos.** Los lista para que los pegue en Word.
- **Empresa: no asigna responsables con nombre** sin que él lo confirme; los propone por cargo.

## Paso 1 — Leer todo

`mi_proyecto` y `ver_capitulo` con `texto: true` (y `parte` hasta la última) de
`informe-fase2-desarrollo` y, si existe, de `informe-fase3-analisis-y-resultados`. De la ficha:
ámbito, tipo, rúbrica o términos, decisión, alcance, extensión y fecha de entrega. De
`informe-fase0-encargo`: pregunta guía y esquema. De `informe-fase1-fuentes`, en empresa: las
limitaciones.

Si `mi_proyecto` dice que hay **material subido**, releer la consigna y la rúbrica, o los
términos de referencia, con `material_del_curso` (`ver` con su número): la revisión se hace
contra el original, no solo contra el resumen de la ficha.

Si alguna de las secciones aparte ya tiene texto, leerla con `ver_capitulo` y preguntar si se
corrige o se deja.

**Empresa:** enseñarle la lista de hallazgos numerados del desarrollo y preguntar si está
completa, para trabajar sobre ella.

## Paso 2 — Qué lleva el cierre

**Curso:**

```
Según tu consigna, el cierre lleva:
· Conclusiones  (siempre)
· Recomendaciones  [sí / no según la consigna]
· Resumen con palabras clave  [sí / no]
¿Está bien así?
· Sí
· Mi docente también pide [otra cosa]
· No me queda claro, dame ejemplos
```

**Empresa:** no se pregunta; se le dice en una línea lo que lleva (conclusiones,
recomendaciones priorizadas, plan de acción, riesgos, limitaciones, introducción y resumen
ejecutivo) y se confirma solo si los términos de referencia piden otra cosa.

## Paso 3 — Las conclusiones

- **Una conclusión por objetivo específico, apartado o hallazgo**, y una final que responde a la
  pregunta guía (curso) o a la decisión del encargo (empresa).
- Cada una: qué se buscaba o qué se encontró, qué significa, y en empresa qué tan firme es si
  hay una salvedad que importe. De tres a cinco oraciones.
- **Curso:** la postura del estudiante aparece en la conclusión final; se le pregunta si
  coincide. Guía en `references/introduccion_y_conclusiones.md`.
- **Empresa:** la conclusión **explica** el hallazgo, no lo repite; en una factibilidad es
  binaria y va primero (conviene, no conviene, o conviene si…). Guía en
  `references/conclusiones_y_recomendaciones.md`.
- Numeradas o en párrafos, según pida la consigna o la plantilla.

## Paso 4 — Las recomendaciones

**Curso, si se piden:** dos a cinco, **cada una apoyada en una conclusión**. A quién va dirigida
(la empresa, la institución, futuros estudiantes) y qué hacer en concreto.

**Empresa, siempre:** entre tres y ocho, cada una de una conclusión, y cada una responde cinco
preguntas:

```
QUÉ HACER             En infinitivo, concreto y verificable.
QUIÉN                 El cargo, no la persona.
PARA CUÁNDO           Una fecha, no «a la brevedad».
CUÁNTO CUESTA         En soles, o «sin costo directo». Si no se sabe, se marca.
CÓMO SE SABRÁ QUE     El indicador que va a medirlo, con su meta.
FUNCIONÓ
```

Y **se priorizan** en una tabla de impacto y esfuerzo, diciendo qué se hace este mes, este
trimestre y este año. Lo primero: alto impacto y bajo esfuerzo.

Van dentro del mismo texto que las conclusiones, bajo el subtítulo de Markdown de nivel 2
«Recomendaciones».

## Paso 5 — Plan de acción y riesgos (solo empresa)

**El plan de acción**, con `references/plan_de_accion.md`: la tabla que el cliente se lleva a la
reunión.

```
**Tabla 12**
*Plan de acción*
| N.º | Acción | Responsable | Plazo | Costo (S/) | Cómo se mide |
|---|---|---|---|---|---|
| 1 | Modificar el procedimiento de compras: umbral a S/ 1 500 | Jefe de Administración | 31-10-2026 | Sin costo directo | % de órdenes con cotización (meta 95 %) |
*Nota.* Los responsables se proponen por su función; la asignación la hace la Gerencia General.
*Fuente.* Elaboración propia a partir de las recomendaciones del informe.
```

Un responsable por acción, plazos que no se apilan, dependencias en la nota, y lo que no se sepa
marcado. **Se le dice cuáles quedaron marcados**, para cerrarlos con el cliente.

**Los riesgos de la implementación:** dos a cinco, en una tabla con probabilidad, impacto,
mitigación y responsable. **Un riesgo sin mitigación es una advertencia, no un análisis.**

Subtítulos de nivel 2: «Plan de acción» y «Riesgos de la implementación».

## Paso 6 — Limitaciones y anexos

**Limitaciones (solo empresa).** El párrafo que se abrió en la Fase 1, cerrado ahora: qué no se
pudo mirar, de qué cifra desconfiar y por qué, y **qué no debería concluirse de este informe**.
Subtítulo de nivel 2 «Limitaciones». No es una disculpa y no se suaviza.

**Anexos (los dos ámbitos).** La lista de lo que va al final, según el tipo, con la tabla de
`references/revision_con_rubrica.md` (curso) o de `references/conclusiones_y_recomendaciones.md`
(empresa). Se le dice qué archivos son y en qué orden; él los pega en el Word.

## Paso 7 — Guardar el cierre

`guardar_capitulo` con **clave `informe-fase4-cierre`**, sin el título «Conclusiones». Dentro,
según el ámbito, los subtítulos de nivel 2: «Recomendaciones», «Plan de acción», «Riesgos de la
implementación», «Limitaciones». Hasta 30.000 caracteres por llamada; si pasa, por partes con
`anadir: true`.

## Paso 8 — La introducción

Se escribe ahora porque presenta lo que el informe **ya dice**. En prosa continua.

**Curso**, con `references/introduccion_y_conclusiones.md`: contexto (con una o dos fuentes con
clave si hace falta una cifra), objetivo o pregunta guía, importancia y organización. Media
página a una página.

**Empresa:** antecedentes del encargo (quién lo pidió y por qué), objetivo (qué decisión apoya),
**alcance con sus tres listas** (qué entra, qué no entra y las limitaciones), método (qué datos,
qué periodo, qué campo, qué muestra) y organización. Una página a una y media.

Enseñarla, ajustar y guardar con `guardar_capitulo`, **clave `informe-introduccion`**, sin el
título «Introducción».

## Paso 9 — El resumen o el resumen ejecutivo

**Curso, si la consigna lo pide:** un párrafo de 150 a 250 palabras: contexto, objetivo, qué se
hizo, principal resultado o hallazgo, conclusión. Sin citas. Debajo, «**Palabras clave:**» con
tres a cinco términos.

**Empresa, siempre: el resumen ejecutivo**, con `references/resumen_ejecutivo.md`, que trae la
estructura, las ocho reglas y dos ejemplos enteros. **Leerlo antes de escribir** (con
`redactar`, `referencia: "resumen_ejecutivo.md"`). Una página, dos como máximo, en este orden:

1. De qué va y por qué se hizo, en dos frases.
2. **Qué se encontró**, con las cifras que importan.
3. **Qué se recomienda:** las tres primeras, con su costo.
4. **Qué se pide:** la decisión concreta, con fecha, y qué pasa si no se toma.

Y la limitación principal al final. Sin citas, sin método, sin «ver el punto 4.3», sin jerga. La
prueba antes de guardarlo:

```
PRUEBA DEL RESUMEN EJECUTIVO
¿Se entiende sin haber leído el informe?             SÍ / NO
¿Tiene al menos tres cifras, todas iguales en el cuerpo?  [N] de [N]
¿Dice qué decisión se pide, con fecha?                SÍ / NO
¿Está la limitación principal?                        SÍ / NO
¿Serviría para otro informe cambiando la empresa?     SÍ / NO  ← si SÍ, está mal
```

Guardar con `guardar_capitulo`, **clave `informe-resumen`**, sin título.

## Paso 10 — Auditoría anti-IA

Con `references/anti_ia.md` sobre los textos nuevos. En la introducción, las conclusiones y el
resumen aparecen más que en ningún otro sitio P1 (inflar) y P12 (cierre optimista); en empresa,
además E1 (jerga vacía) y **E3 (recomendación sin dueño)**.

**Empresa, además, la cadena:** cada conclusión se rastrea a una sección, cada recomendación a
una conclusión, cada acción a una recomendación. Lo que no se rastrea, se quita o se completa.

## Paso 11 — La revisión

**Curso: con la rúbrica**, con `references/revision_con_rubrica.md`:

1. `revisar_el_informe`: lo que no cuadra dentro del informe (secciones sin texto, citas rotas).
2. `revisar_evidencia` sin capítulo: afirmaciones sin fuente en todo el informe.
3. **La tabla de la rúbrica**, criterio por criterio, con la sección donde se cumple:

| Criterio de la rúbrica | ¿Se cumple? | Dónde | Qué falta |
|---|---|---|---|
| Introducción con objetivo | Sí | Introducción, 2.º párrafo | — |
| Mínimo 8 fuentes académicas | No | — | Hay 6: faltan 2 (Fase 1) |

**Empresa: tres revisiones**, con `references/revision_con_terminos.md`:

1. **Contra los términos de referencia**, punto por punto, con la sección donde se cumple.
2. **De cifras**, con `revisar_el_informe` y a mano: cada cifra del resumen ejecutivo igual en el
   cuerpo, los totales suman, cada tabla con su «Fuente», las proyecciones marcadas, los puntos
   porcentuales bien usados. **Si una sola línea falla, no se entrega.**
3. **De tono y riesgo:** ningún hallazgo sin evidencia, ninguna promesa sin cálculo, ninguna
   persona señalada con nombre, ninguna norma sin número, nada que no deba salir de la empresa.

Y `revisar_evidencia` sin capítulo.

**En los dos: «Sí» solo con el sitio exacto donde se cumple. Sin sitio, es «No».** Lo que falta
se corrige ahora si es de esta fase; si es de otra, se dice cuál y se ofrece volver.

**Empresa: las marcas sin resolver** (`[POR CONFIRMAR…]`, `[FALTA DATO…]`, `[FALTA FUENTE]`) se
le enseñan una por una, con qué hacer con cada una. Una marca puede quedarse si las limitaciones
la explican; si no, es un hueco.

## Paso 12 — Entregar

1. `enlace_del_word` con el informe completo.
2. **Lista de entrega:**

- [ ] Descargar el Word y abrirlo: aceptar «actualizar el índice» si Word lo ofrece.
- [ ] Pegar cada imagen en su marca de figura resaltada.
- [ ] Pegar los anexos al final: [lista].
- [ ] Revisar la portada: curso: nombres, códigos, curso, docente, fecha · empresa:
      destinatario, quién firma, periodo, fecha y la marca de confidencial.
- [ ] Comprobar la extensión: [N] páginas pedidas.
- [ ] Revisar que la norma de citas es la que piden: [norma].
- [ ] Empresa: cerrar con el cliente las [N] marcas pendientes.
- [ ] Guardar en el formato de entrega (PDF o Word) y enviarlo antes del [fecha].
- [ ] Leerlo entero una vez en voz alta y cambiar lo que no suene a ti.

3. `guardar_avance` con `capitulo: informe-fase4-cierre`, `resumen` de lo entregado y
   `estado: LISTO` si lo da por terminado.

Cierre:

```
Tu informe está completo. Aquí tienes el Word: [enlace]
(el enlace vence en media hora; si pasa, pídeme otro)

Te quedan por hacer a mano: pegar [N] imágenes y los anexos.
Entregas el [fecha]. ¡Éxitos!
```

En empresa, añadir una línea: lo primero que le van a preguntar es [el supuesto o el hallazgo
que decide el resultado], y que lo tenga a mano.

## Errores que esta skill previene

1. Una introducción que promete lo que el informe no hace.
2. Conclusiones que traen datos nuevos o repiten el desarrollo.
3. Recomendaciones que no salen de ninguna conclusión.
4. Entregar sin haber mirado la rúbrica o los términos de referencia.
5. Olvidar pegar las imágenes en sus marcas.
6. Un resumen escrito antes de terminar el informe.
7. Empresa: «se recomienda optimizar el proceso», sin quién, cuándo ni cuánto.
8. Empresa: quince recomendaciones sin prioridad.
9. Empresa: un resumen ejecutivo sin cifras, que sirve para cualquier informe.
10. Empresa: una cifra del resumen que no coincide con el cuerpo.
11. Empresa: un informe sin limitaciones, al que le atribuyen lo que no dijo.

## Archivos de referencia

- `references/estilo_preguntas.md` — Cómo se pregunta en esta ruta, según el ámbito.
- `references/integracion_zotero.md` — Claves y norma de citas.
- `references/introduccion_y_conclusiones.md` — Curso: introducción, conclusiones, recomendaciones y resumen.
- `references/revision_con_rubrica.md` — Curso: la revisión criterio por criterio y los anexos por tipo.
- `references/conclusiones_y_recomendaciones.md` — Empresa: de la evidencia a la acción, limitaciones y anexos.
- `references/plan_de_accion.md` — Empresa: la tabla del plan de acción y sus seis columnas.
- `references/resumen_ejecutivo.md` — Empresa: la estructura, las ocho reglas y dos ejemplos enteros.
- `references/revision_con_terminos.md` — Empresa: las tres revisiones y las marcas pendientes.
- `references/anti_ia.md` — Auditoría de patrones de IA.
- `references/confidencialidad.md` — Lo que no debe salir de la empresa.
