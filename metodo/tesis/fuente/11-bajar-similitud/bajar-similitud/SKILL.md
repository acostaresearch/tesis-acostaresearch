---
name: bajar-similitud
description: Baja el porcentaje de similitud de un trabajo académico a partir del PDF del informe de Turnitin. Con el reporte subido, ver_lo_marcado trae el porcentaje y solo los párrafos coincidentes, que se reescriben por tandas y se guardan con reescribir_parrafos o humanizar_mi_documento; sin él, lee el capítulo numerado y guarda los párrafos tocados; si es un documento externo, trabaja sobre su Word. Separa lo reescribible de lo intocable, reescribe sin meter patrones de IA y verifica que no se pierda ninguna cita, clave de cita ni cifra. Reporta lo que ninguna reescritura arregla: citas sin fuente, citas textuales sin comillas y contradicciones de datos entre capítulos. ACTIVAR cuando el usuario diga "bajar la similitud", "me salió alto el Turnitin", "reducir el porcentaje de plagio", "mi tesis tiene 25% de similitud", "necesito bajar de 20%", traiga un informe de Turnitin o pida reducir coincidencias. Para quitar patrones de IA sin tocar coincidencias, usar humanizador-academico.
---

# Bajar similitud

Esta skill se entrega entera en una sola llamada: no lleva encabezados de segundo
nivel, a propósito. Empieza por el camino normal, que es de una vez; las fases de
más abajo son la referencia de cada decisión y el camino sin reporte.

### Con el reporte subido: de una vez (el camino normal)

Si el tesista tiene el PDF del reporte de similitud, este es el camino, y manda sobre las fases de abajo.

0. **Antes de nada**, `mi_proyecto`, y en una sola pregunta lo que falte: el **umbral que exige su universidad** (cambia todo el plan: con 25 % y un 22 % actual basta afinar; con 15 % puede haber un problema de fondo) y si ya subió el reporte.
1. **Subida.** Se le da el enlace de `subir_mi_documento` para que suba el PDF del reporte. Su Word solo se sube si la tesis no está guardada en el proyecto (`mi_proyecto` lo dice).
2. **Lectura.** `ver_lo_marcado` con `"reporte": "similitud"` devuelve la anatomía del porcentaje (total, desglose en internet, publicaciones y trabajos, y las fuentes principales) y **solo los párrafos coincidentes**, cruzados con el Word subido o con los capítulos guardados. Con eso se cuenta el diagnóstico de la Fase 1 y se revisa lo de la Fase 2.
3. **Clasificar.** Cada párrafo va a su cubo de la Fase 3: intocable, estructural o reescribible. Lo que no se toca se pasa en `saltar` ("marco-teorico ¶3" o "¶12") para que no vuelva a salir.
4. **Preguntar lo que haya que preguntar**, antes de reescribir y todo junto: si un fragmento es una cita textual sin comillas (la regla de abajo), y los enunciados de la matriz, que se derivan al asesor.
5. **Reescribir por tandas** con la doble restricción de la Fase 5 y guardar cada tanda con `reescribir_parrafos` (capítulos guardados) o `humanizar_mi_documento` (Word subido), según diga la respuesta de `ver_lo_marcado`. No se reenvían capítulos enteros ni se enseña cada párrafo al tesista ni se le pide aprobación por bloques: al tesista, una línea por tanda. Lo que vuelva rechazado o con avisos se rehace. Lo reescrito no vuelve a salir; se repite `ver_lo_marcado` hasta que no quede nada reescribible.
6. **Cierre.** `enlace_del_word` y un informe corto: qué se reescribió, qué se dejó y por qué, lo que queda para el asesor y las palancas de la Fase 7.

En este modo **no hacen falta** `scripts/leer_informe.py` ni recorrer el PDF a mano (las Fases 1, 3 y 4 las hace el servidor), ni `scripts/auditar_patrones.py` (el servidor avisa y rechaza si cambian cifras, comillas, apellidos o claves). Los scripts quedan para el camino sin reporte subido y para el documento externo.

### Qué resuelve y qué no

Un porcentaje de similitud alto tiene tres causas posibles y solo una se arregla escribiendo.

La primera es **copia real**: texto tomado de una fuente sin comillas ni cita. Eso no se arregla parafraseando, se arregla citando bien. Reescribir para que el detector no lo vea es esconder el problema.

La segunda es **saturación temática**: el trabajo dice cosas comunes de la forma común del campo, y coincide con las cientos de tesis que dicen lo mismo. Esto sí se baja reescribiendo.

La tercera es **estructura obligatoria**: variables, términos técnicos, encabezados normados, enunciados de la matriz de consistencia. No se toca, y suele ser lo que fija el piso del porcentaje.

El primer trabajo de esta skill es decidir cuánto hay de cada una. Saltarse ese diagnóstico y ponerse a reescribir produce trabajos que esquivan al detector con las citas mal puestas.

### Regla que no se negocia

**Nunca parafrasear una cita textual para que deje de coincidir.** Si aparece un fragmento que parece copiado literalmente de una fuente, con comillas incompletas o sin ellas, se le pregunta al usuario si es textual. Si lo es, se marca con comillas y número de página, y se acepta que suba la coincidencia. Turnitin permite filtrar el texto citado; la deshonestidad no tiene arreglo posterior.

Lo mismo con las citas que no tienen fuente: se reportan, no se borran para que el problema desaparezca.

### Dos caminos: la tesis del proyecto o un documento externo

Antes de pedir nada, se llama a `mi_proyecto`. Lo que diga decide el camino, y el camino decide de dónde sale el texto y a dónde vuelve.

### Camino A — La tesis está en el proyecto (el camino normal)

`mi_proyecto` muestra capítulos con texto guardado. El Word que el tesista entrega a Turnitin es el que arma el servidor con ese texto, así que **las correcciones tienen que volver al servidor**: un Word corregido por fuera se pierde en cuanto el tesista pida el siguiente `enlace_del_word`, que vuelve a sacar el texto guardado.

- **El informe de Turnitin** (PDF) se sigue leyendo con `scripts/leer_informe.py`, como en la Fase 1.
- **El texto** no se pide en archivo: se lee con `ver_capitulo`, con `"texto": true, "numerado": true` (y `"desde"` si sigue), capítulo por capítulo. Cada bloque sale numerado (¶7); títulos, tablas, figuras y listas van marcados y no se reescriben.
- **Se reescribe por tandas** (Fase 5), sin enseñarle cada bloque ni pedir aprobación: solo se le consulta lo de la regla de las citas textuales y la matriz.
- **Se guardan solo los párrafos tocados**, tanda a tanda, con `reescribir_parrafos` ({capitulo, parrafos:[{p, texto}]}, hasta 40 por llamada), sin reenviar el capítulo entero. Si rechaza un párrafo porque cambió una cifra, un año, unas comillas, un apellido citado o una clave, se corrige ese párrafo y se vuelve a mandar.
- **Después**, `enlace_del_word`. **El Word «entregado» de referencia es el que baja de ese enlace**: es el que el tesista vuelve a subir a Turnitin, y con su texto se hace la comparación de la Fase 6.

Si `mi_proyecto` dice que el tesista **subió su documento para citar** (`ver_mi_documento`), ese documento no se puede volver a guardar reescrito: `citar_mi_documento` solo acepta los párrafos copiados tal cual con marcas añadidas y rechaza los que tienen el texto cambiado. Se le explica al tesista, y la reescritura sigue el camino B sobre su propio Word; si después quiere las citas puestas por el servidor, tendrá que subir desde su perfil la versión corregida y volver a citarla.

### Camino B — Documento externo que no está en el proyecto (excepción)

Un artículo, una tesis de otra plataforma o un trabajo que el tesista nunca guardó en el proyecto. Solo en este caso se trabaja sobre el archivo del usuario: el .docx tal como se entregó, reescrito en su sitio conservando el formato, y verificado con los scripts sobre ese .docx. Todo lo que en esta skill dice «.docx» se refiere a este camino.

### Las claves de cita en el camino A (regla dura)

El texto del proyecto lleva las citas como claves: `[AR97D22F86]` al final de la afirmación, `[AR97D22F86:n]` detrás del nombre del autor, `[AR97D22F86:p. 45]` con página, y `[FALTA FUENTE]` donde no hay respaldo. El servidor las convierte en citas y referencias al armar el Word. Al reescribir para bajar la similitud:

- **Ninguna clave se borra, se cambia ni se inventa**, y se copian con su modificador tal cual.
- **Cada clave viaja con su afirmación.** Si la afirmación cambia de oración o se parte en dos, la clave se va con su dato.
- **Cada párrafo sale con la misma lista de claves** que tenía; se comprueba párrafo a párrafo con `verificar_cambios.py`, no solo el total.
- **La `:n` sigue al nombre:** si el nombre del autor sale de la frase, se quita la `:n` y la clave va al final de la afirmación; si entra, se añade la `:n` detrás del nombre, y el nombre solo se escribe si se conoce por la biblioteca (`mis_fuentes`), nunca de memoria.
- **`[FALTA FUENTE]` se conserva**, y una oración con clave no se elimina sin preguntar al tesista.

**«Cambiar dónde va la cita»** (Fase 5) significa, en este camino, mover la clave con su afirmación: pasar de cita al final a cita narrativa o al revés, con la regla de la `:n`. Nunca reescribir la clave ni escribir la cita a mano como autor y año.

### Fase 0 — Insumos

Pedir lo que falte y no arrancar sin ello:

1. El PDF del informe de similitud, completo, con las páginas marcadas y no solo la portada.
2. El texto que se entregó. **Camino A:** no se pide; se lee de los capítulos guardados con `ver_capitulo`. **Camino B:** el .docx tal como se entregó.
3. **El umbral que exige la universidad** (ver el paso 0 del camino normal).

Preguntar también si el usuario tiene un informe anterior. Si lo tiene, comparar la cabecera de los dos antes de sacar conclusiones: identificador de entrega, filtros aplicados y número de fuentes. **Dos informes generados desde cuentas o con filtros distintos no son comparables**, y presentarlos como un antes y un después es engañar al usuario sobre el efecto del trabajo.

Verificar que el texto con el que se trabaja es el que se entregó. Los usuarios editan entre una cosa y otra. **Camino A:** comparar el texto del PDF contra lo que devuelve `ver_capitulo`; si el tesista cambió su Word a mano después de descargarlo, esos cambios no están en el servidor, y hay que preguntarle cuál manda antes de tocar nada. **Camino B:** comparar el texto del PDF contra los párrafos del .docx y sincronizar las diferencias. En los dos casos, entregar un texto que revierte las correcciones del usuario es peor que no hacer nada.

### Fase 1 — Anatomía del porcentaje

```bash
python scripts/leer_informe.py informe.pdf
```

Devuelve el porcentaje general, el desglose por tipo de fuente, qué se filtró, el número de fuentes, las de mayor peso, la estimación de palabras coincidentes y un diagnóstico de mosaico o bloque.

Leer con atención dos señales:

**La fuente principal.** Si aporta 1% o 2% y el resto está por debajo, el porcentaje es un mosaico de frases cortas repartidas entre decenas de fuentes. No hay nada copiado. Si una sola fuente aporta 8% o más, ir a buscarla al cuerpo antes de cualquier otra cosa.

**El solapamiento.** Cuando la suma de los cubos supera el total, la misma frase está coincidiendo con varias fuentes a la vez. Esa es la firma de la redacción estándar del campo.

Ver `references/informe-turnitin.md` para qué significa cada campo y qué palancas de configuración existen.

### Fase 2 — Errores de fondo, antes de reescribir

Revisar y reportar. No corregir por cuenta propia, porque son decisiones del autor:

- **Citas sin fuente o que faltan en la bibliografía.** **Camino A:** la bibliografía la arma el servidor a partir de las claves, así que no se buscan apellidos a mano. Se usa `revisar_evidencia` (con `capitulo` para uno, sin él para toda la tesis) y, si el tesista está por entregar, `revisar_la_tesis`. Lo que importa de su respuesta: las **citas sin enlazar** (escritas a mano como autor y año, sin clave: parecen respaldadas y no lo están) y las **afirmaciones sin fuente**. Se le presentan tal cual; buscarles fuente es trabajo de las skills que citan, no de esta. **Camino B:** buscar cada apellido citado y comprobar que aparece en las referencias. Es frecuente encontrar diez o más.
- **Comillas huérfanas.** Una comilla de cierre sin apertura suele delatar una cita textual que se quedó a medias. Preguntar.
- **Citas de segunda mano** ("X, citado por Y"). Están bien formuladas, pero avisan de texto tomado de fuentes intermedias.
- **Contradicciones de datos.** Lugar del estudio, año, tamaño de población que cambian entre capítulos. En el camino A se cotejan leyendo los capítulos guardados con `ver_capitulo`.
- **Referencias duplicadas o con desajuste de forma** entre la cita del texto y la entrada bibliográfica. En el camino A no se corrigen a mano: las escribe el servidor; si una sale mal en el Word, el problema está en la ficha de la fuente y se le dice al tesista.

Presentar esto antes que el diagnóstico de redacción. Es lo que el jurado ve primero.

### Fase 3 — Clasificar la coincidencia

Recorrer las páginas marcadas del informe y repartir lo resaltado en tres cubos.

**Intocable.** Las variables del estudio, los términos técnicos del campo, los encabezados que exige el formato, el título. Cambiarlos empeora el trabajo. Suelen ser fragmentos de tres a seis palabras que aparecen decenas de veces.

**Estructural repetido.** Los enunciados de problemas, objetivos e hipótesis. Son casi idénticos entre sí por diseño, cada uno coincide entero con cualquier tesis del mismo formato, y sumados pueden valer varios puntos porcentuales. **La decisión de variarlos es del asesor, no de la skill ni del usuario**, porque toca la matriz de consistencia. Cuantificar cuánto pesan y presentar el dato.

**Reescribible.** Prosa que dice algo común de la forma común. Aquí es donde se trabaja.

Contar palabras por cubo. Si lo reescribible es poco, decirlo: significa que la redacción ya no es la palanca.

### Fase 4 — Localizar la concentración

Las marcas no se reparten parejo. Recorrer el informe página por página y anotar dónde se agrupan. Los apartados que suelen concentrarlas son el planteamiento del problema, las definiciones de términos y la metodología, porque son los que más se parecen entre trabajos del mismo tipo.

Contar las palabras de cada tramo candidato. Esto da el orden de trabajo: primero lo que más pesa. En el camino A, anotar además en qué capítulo guardado cae cada tramo, porque es la unidad que se vuelve a guardar.

### Fase 5 — Reescribir con doble restricción

Trabajar por tandas, empezando por lo que más pesa, sin pedir aprobación de cada bloque. **Camino A:** los párrafos de cada tanda se guardan con `reescribir_parrafos`, como dice «Dos caminos». **Camino B:** se aplica sobre el .docx y se entrega el archivo al terminar.

**Qué cambiar:** la estructura sintáctica. Orden de la oración, sujeto, voz, dónde va la cita, dónde cae el corte entre oraciones. Ahí es donde vive la coincidencia. En el camino A, mover la cita es mover la clave con su afirmación.

**Qué no cambiar:**
- Los términos técnicos. "Rotación de cuentas por cobrar" se queda como está.
- Las citas y las cifras, ninguna. En el camino A, tampoco las claves `[AR…]` ni `[FALTA FUENTE]`.
- El tiempo verbal, si la guía lo exige.
- El número de párrafos. Los documentos convertidos desde PDF traen párrafos partidos a mitad de oración; conservar la bisagra exacta donde termina uno y empieza el otro.

**La doble restricción.** Al alejarse de la redacción estándar es facilísimo caer en la prosa característica de un modelo de lenguaje: tríadas paralelas, gerundios colgados, conectores de manual, cierres que resumen. Eso sube el otro indicador. Después de escribir cada bloque, auditarse antes de mostrarle nada al usuario.

Camino A, con el bloque reescrito guardado en un archivo de texto (párrafos separados por línea en blanco):

```bash
python scripts/auditar_patrones.py bloque.txt
python scripts/auditar_patrones.py capitulo.txt --parrafos 3,4,7
```

Camino B, sobre el documento del usuario:

```bash
python scripts/auditar_patrones.py documento.docx --parrafos 38,39,45,47
```

En texto plano los párrafos se cuentan desde 1; en .docx son los índices del documento, desde 0. El script quita las claves de cita antes de medir, para que no cuenten como palabras ni como dos puntos. Si un párrafo está partido por la conversión de PDF, pasar el índice de las dos mitades juntas o el script contará mal la última oración.

Los tics recurrentes al reescribir en lote son estos, y conviene buscarlos a propósito:

- **Molde de apertura.** Tres párrafos seguidos abriendo con la misma arquitectura ("En Ecuador se...", "En el Perú las...", "En Colombia se..."). Es el patrón que más delata, y aparece justo cuando se ordena un texto desordenado.
- **Verbo de atribución repetido.** Cuatro "sostiene que" en mil palabras.
- **Asimetría fabricada.** Cortar una oración a siete palabras vacías para subir la dispersión. El número mejora y el texto empeora. La salida legítima es partir oraciones que cargan dos datos, no inventar frases cortas; en el camino A, cada dato se lleva su clave.

Ver `references/patrones-al-reescribir.md` para el catálogo completo con ejemplos.

### Fase 6 — Verificar

Camino A: guardar en archivos el texto del capítulo tal como lo devolvió `ver_capitulo` (antes) y el reescrito (después), y como entregado el texto del Word que bajó de `enlace_del_word` antes de reescribir (o el que se extrae del PDF del informe):

```bash
python scripts/verificar_cambios.py antes.txt despues.txt --entregado texto_entregado.txt
```

Camino B:

```bash
python scripts/verificar_cambios.py antes.docx despues.docx --entregado texto_entregado.txt
```

Comprueba conteo de párrafos, citas perdidas, claves de cita perdidas, inventadas o cambiadas de párrafo (incluido el cambio de `:n`), cifras perdidas y cuánto texto literal se desplazó. Cualquier diferencia de claves se corrige antes de guardar, salvo un cambio de `:n` que se explique por el nombre del autor.

Mirar el resultado maquetado. **Camino A:** después de `reescribir_parrafos`, pedir `enlace_del_word` y revisar en ese Word al menos una página de cada bloque tocado, con las citas ya convertidas. **Camino B:** renderizar el documento a PDF y mirar al menos una página de cada bloque tocado, para confirmar que la maquetación no se rompió.

**Sobre el número final: no prometer nada.** No hay forma de predecir el resultado del próximo informe, porque el índice de Turnitin es cerrado. Se puede decir cuánto texto cambió y dónde. Decir "va a bajar a X%" es inventar.

Si el usuario pide verificar que la similitud no subió, explicar el límite con claridad y ofrecer el único chequeo posible: buscar en la web algunas de las frases nuevas más genéricas, para descartar lo evidente. Es un chequeo parcial y hay que presentarlo como tal.

### Fase 7 — Palancas que no son reescritura

Cuando la reescritura llega a su techo, y llega antes de lo que parece, quedan tres. A menudo rinden más que seguir escribiendo:

**Configuración del informe.** Turnitin permite excluir coincidencias por debajo de un número de palabras. En un mosaico donde casi todas las fuentes aportan menos del 1%, ese filtro elimina encabezados y fragmentos de tres a seis palabras, y puede mover el resultado varios puntos sin tocar el texto. Confirmar también que se están filtrando bibliografía y texto citado.

**Autocoincidencia.** Si la entrega anterior quedó guardada en el repositorio de la universidad, la siguiente puede coincidir consigo misma y dar un porcentaje altísimo que no tiene nada que ver con plagio. Avisar de esto siempre. Es un problema mecánico que arruina entregas.

**Los enunciados de la matriz.** Con autorización del asesor, variar la redacción entre niveles. Es la ganancia más grande que queda, y no es decisión de la skill. En el camino A la matriz vive en el texto guardado de `problema-y-objetivos`: si el asesor autoriza el cambio, se lee ese capítulo con `ver_capitulo` (`"numerado": true`), se cambian los enunciados y se guardan esos párrafos con `reescribir_parrafos`, avisando al tesista de que los capítulos que los repiten tendrán que alinearse.

### Cómo comunicar

Reportar siempre con cita literal del texto del usuario. "Hay lenguaje promocional" no sirve; "escribiste *resulta vital pues asegura niveles óptimos de liquidez*" sí.

Distinguir en voz alta lo que se midió de lo que se supone. Las métricas del script son medición. El efecto sobre el próximo informe es suposición.

Cuando una meta no se alcanza, decir por qué en vez de seguir retorciendo. Un estado del arte que enumera doce estudios con país, autor y año tiene un techo de variación que no depende de quién lo escriba.

Y cuando el usuario señale que un párrafo reescrito suena mal, creerle. Suele tener razón, y suele ser un tic introducido en la reescritura.
