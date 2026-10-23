# El documento, la portada y el formato

## Quién arma el documento

**El servidor de la plataforma, no la skill.**

La skill redacta el capítulo, lo guarda en el proyecto y pide el enlace. El
servidor arma el Word con todo lo guardado: portada, índice, capítulos en orden,
y las citas y las referencias escritas en la norma del proyecto, con los campos
de Zotero si el tesista lo conectó.

```
LA SKILL                      EL SERVIDOR
────────────────────────────  ──────────────────────────────────
Redacta el capítulo           Arma el archivo Word
guardar_avance                Pone portada e índice
guardar_capitulo              Ordena los capítulos
enlace_del_word               Escribe citas y referencias en
                                la norma del proyecto
                              Aplica el formato del proyecto
```

## Qué cambió respecto de la versión anterior

La versión anterior de esta skill:

1. Pedía al tesista la plantilla Word de su universidad en el Paso 2.
2. Armaba el Word por su cuenta y lo entregaba en el chat.
3. Versionaba el archivo como V1, V2, V3 y le pedía al tesista que lo volviera a
   subir en la siguiente skill.
4. Medía márgenes, tipografía e interlineado del archivo generado antes de
   entregarlo.

**Los cuatro puntos quedan derogados.** La skill no arma archivos, así que no
tiene sentido pedir una plantilla, ni versionar por fuera, ni verificar un
formato que no controla. El documento del tesista es uno solo, vive en su
proyecto y siempre está actualizado: no hay que guardarlo ni volver a subirlo
entre skills.

## Qué sí necesita la skill del proyecto

Solo dos cosas, y las dos por una razón concreta:

```
DATO              POR QUÉ HACE FALTA
────────────────  ──────────────────────────────────────────
Norma de citas    De ella salen las citas y las referencias
(estiloCitas)     del Word. Si no está elegida, se pregunta
                  UNA vez y se guarda con guardar_avance.

Asesor            Sale en la portada. Se pregunta UNA vez.
                  Si todavía no tiene, se guarda vacío y NO
                  se vuelve a preguntar nunca.
```

Universidad y carrera también van en la portada; normalmente ya están en el
proyecto. Si faltan, se preguntan junto con lo anterior, en el mismo turno.

Se guardan con `guardar_avance`, en sus campos `universidad`, `carrera` y
`asesor`; la norma, en `estiloCitas`.

## Qué NO se pregunta nunca

- Márgenes, tipo y tamaño de letra, interlineado, sangría, numeración de página.
- Si tiene la plantilla de su universidad en Word, en PDF o impresa.
- Si quiere que el documento salga "en formato A4 con Times New Roman 12".

Todo eso es configuración del proyecto en la plataforma. Preguntarlo en el chat
gasta un turno y no cambia el archivo que va a descargar.

## Qué responder cuando el tesista pregunta por el formato de su universidad

Respuesta honesta, sin promesas:

> El documento se arma en la plataforma con la configuración de tu proyecto: de
> ahí salen la portada, el orden de los capítulos y la norma de citas. Los
> parámetros tipográficos finos (márgenes, tipo y tamaño de letra, interlineado)
> revísalos contra el reglamento de tu universidad sobre el archivo que
> descargues. Ten en cuenta que cada vez que pides el enlace el servidor vuelve a
> armar el archivo, así que esos ajustes conviene dejarlos para la copia final.

**Reglas duras de honestidad:**

- **No prometer** que el Word saldrá con el formato exacto de su universidad.
- **No pedirle que suba su plantilla al chat.** No cambiaría nada.
- **No armar un Word "bien formateado"** como favor. Sería un segundo documento
  compitiendo con el de la plataforma, sin la norma de citas ni los campos de
  Zotero, y el tesista terminaría sin saber cuál de los dos vale.
- Si insiste en que necesita el formato institucional exacto, se le dice dónde se
  configura (su proyecto en la plataforma) y que, si ahí no está disponible, lo
  ajuste a mano sobre la copia final que va a imprimir.

## Datos de portada: qué hace la skill y qué no

**Hace**: pregunta una vez, agrupado en un turno, los datos que `mi_proyecto`
muestre sin dato (universidad, carrera, asesor) y los guarda con
`guardar_avance`.

**No hace**: completar ninguno por suposición. Ni el asesor, ni el grado al que
opta, ni la línea de investigación, ni el ORCID. Lo que el tesista no sepa se
declara pendiente en el chat y se le dice dónde completarlo.

Los campos que la plataforma no guarda (ORCID, línea de investigación en la
portada, grado exacto) **no se piden en el chat**: se le indica que los revise en
la configuración de su proyecto.

## Qué se guarda y en qué orden

```
1. guardar_avance    Lo acordado, por campos: problemaGeneral,
                     objetivoGeneral, objetivosEspecificos,
                     hipotesis, variables. Más el resumen en
                     dos o tres frases.
                     estado: LISTO solo si el tesista lo dio
                     por bueno; si no, EN_CURSO.

2. guardar_capitulo  El texto del capítulo, clave
                     problema-y-objetivos, en Markdown limpio:
                     ## para subtítulos, párrafos separados por
                     línea en blanco, sin comentarios de la
                     skill. Si pasa de 30.000 caracteres, por
                     partes con anadir.

3. revisar_evidencia Qué afirmaciones tienen fuente y cuáles
                     no, antes de entregar.

4. enlace_del_word   El enlace de descarga. Caduca a la media
                     hora; si se vence, se pide otro.
```

**Si una llamada falla**, se le dice al tesista con esa palabra: no se guardó. No
se inventa que quedó guardado ni se entrega un archivo armado por la skill como
reemplazo.

## Lo que sigue en el texto del capítulo

El texto que se guarda contiene el Capítulo I y sus anexos. **No lleva carátula,
ni dedicatoria, ni agradecimiento, ni índice, ni lista de referencias**: eso lo
pone el servidor.

El resumen y el abstract tampoco van acá, porque no se pueden escribir sin
resultados. Son trabajo de la Skill de Conclusiones y Abstract.

## Las referencias

Las escribe el servidor a partir de las claves citadas en el texto, en la norma del
proyecto y con los campos de Zotero. **El texto que se guarda no lleva sección
Referencias**: saldría duplicada. Si un dato de una referencia sale mal, se corrige
en la biblioteca (su Zotero, su Mendeley o «Mis fuentes»), no en el capítulo.
