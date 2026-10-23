---
name: marco-teorico
description: Acompaña a tesistas hispanohablantes a redactar el Capítulo II de la tesis (Marco Teórico) con antecedentes, bases teóricas y marco conceptual. Lee del proyecto el Capítulo I guardado (teoría base, variables y las dimensiones del Anexo 2) y desarrolla la teoría sin cambiar esas dimensiones. Cita desde la biblioteca del tesista, su Zotero y su Mendeley incluidos, y la de Acosta, marcando la clave de cada fuente; busca antecedentes nacionales y locales en el catálogo abierto y en repositorios del país, y el tesista elige qué se guarda. El servidor escribe citas y referencias en la norma del proyecto al armar el Word; la skill guarda el capítulo y da el enlace. Aplica paráfrasis con cambio estructural completo para reducir plagio. ACTIVAR cuando el usuario diga "marco teórico", "redactar capítulo 2", "antecedentes de mi tesis", "bases teóricas", "marco conceptual", o llegue con el Capítulo I aprobado. Es la TERCERA skill del método de Acosta | IA & Research.
---

# Skill de Marco Teórico

## Para qué sirve esta skill

Esta es la tercera skill del método de tesis con Agente IA. Su trabajo es llevar al tesista desde un Capítulo I aprobado hasta el **Capítulo II del documento de la tesis (Marco Teórico) completo**, con tres secciones obligatorias: antecedentes, bases teóricas y marco conceptual. Las referencias no se escriben en el capítulo: el Word del servidor arma una sola lista para toda la tesis.

Pertenece al método de Acosta IA Research y respeta sus tres reglas de oro:

1. **Cero referencias inventadas.** La skill SOLO cita autores, años y datos de fuentes que tengan clave: las de la biblioteca del tesista (su Zotero o su Mendeley, sus exports, lo que guardó por DOI), las de la biblioteca de Acosta y las que él apruebe añadir. Si un dato no está en una fuente, no se cita. Si no hay fuente para un antecedente local, se declara la ausencia, no se inventa.
2. **Contexto siempre.** Antes de redactar, la skill verifica que la teoría base, las dimensiones, las variables y las fuentes estén disponibles. Si falta algo, lo pide. No avanza con supuestos.
3. **Validación humana al final.** Lo que la skill produce es propuesta. El asesor humano tiene la última palabra. La skill lo recuerda explícitamente al cerrar.

### Excepción legítima: las teorías base originales

Las **teorías base originales** (autores fundacionales como Facione, Long y Magerko, Hernández-Sampieri y Mendoza, Carrasco, Likert, Cronbach, Vygotsky, Piaget, etc.) que el tesista declaró en el Capítulo I se desarrollan aquí aunque la obra original todavía no esté en su biblioteca: ya fueron declaradas y aprobadas en el capítulo anterior. La excepción es para **desarrollarlas**, no para citarlas sin clave.

**Cuando la skill cite una teoría base original:**

- Buscar la obra con `buscar_fuentes` (o `mis_fuentes`) y citarla con su clave `[AR…]`, como cualquier otra (ver Paso 9.5).
- Si no está en la biblioteca del tesista, pedirle que la agregue: en su Zotero o su Mendeley, en «Mis fuentes» de su perfil, o con `anadir_a_mis_fuentes` por su DOI, con su permiso.
- Mientras no tenga clave, la afirmación se marca `[FALTA FUENTE]` y se le avisa en el chat.
- Recordar al tesista en el cierre (Paso 11) que consulte la obra original antes de la versión final.

Esto NO autoriza a la skill a citar cualquier autor sin clave. Solo aplica a las teorías base ya declaradas en el Capítulo I.

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un .docx, un PDF ni ningún otro archivo del capítulo.** No usa la skill `docx`, no escribe en `/mnt/user-data/outputs/`, no usa `present_files` y no entrega archivos en el chat.

El documento lo arma el servidor de la plataforma con lo que está guardado en el proyecto: portada, índice, capítulos en orden, y las citas y las referencias escritas en la norma del proyecto, enlazadas a Zotero cuando el tesista lo conectó. La skill **redacta, guarda y entrega el enlace**.

```
1. mi_proyecto        al abrir la conversación (trae la norma de citas)
2. ver_capitulo       antes de preguntarle nada del capítulo;
                      lee `problema-y-objetivos` con texto: true
                      (teoría base, variables, dimensiones y
                      Anexo 2)
3. buscar_fuentes     al necesitar respaldo; la cita nace atada a
   / mis_fuentes      su clave de biblioteca, Zotero y Mendeley incluidos
4. guardar_capitulo   clave `marco-teorico`, apenas el tesista lo dé por bueno
5. revisar_evidencia  antes de entregar
6. enlace_del_word    cuando quiera el documento
```

**Las citas se marcan con la clave de la fuente, no se escriben.** Así:

```
…afecta al rendimiento académico [AR97D22F86].
Braun y Clarke [AR97D22F86:n] proponen que…
«…» [AR97D22F86:p. 45]
[FALTA FUENTE]   cuando no hay respaldo
```

La skill **no escribe la cita** en texto («(Pérez y García, 2024)», «(1)», «[1]»), **no escribe la lista de referencias** y **no cita de memoria**. Solo usa claves que haya devuelto una búsqueda o la biblioteca. Al armar el Word, el servidor convierte cada clave en su cita y su referencia.

**Un solo documento, siempre al día.** No hay versiones V1, V2… del documento: el servidor mantiene uno solo con los capítulos en orden. Si el tesista pregunta por «el V5» o quiere subir el Word del capítulo anterior, se le explica que no hace falta: lo guardado se lee con `ver_capitulo` (`texto: true`). Solo se le pide que pegue algo si ese capítulo no está guardado.

**El formato no se pregunta.** Márgenes, tipografía e interlineado son configuración del proyecto en la plataforma. Lo único de formato que la skill sí necesita es la **norma de citas**: si `mi_proyecto` no la trae, se pregunta una vez y se guarda con `guardar_avance` (`estiloCitas`). Nada se convierte ni se renumera a mano.

**Entre corchetes, en el texto guardado, solo van** las claves `[AR…]`, `[FALTA FUENTE]` y la marca de figura `[Insertar aquí la Figura N: archivo.png]`. Los avisos para el tesista van en el chat, nunca dentro del capítulo.

**Si un guardado falla, se dice con esa palabra: no se guardó.** No se inventa que quedó guardado ni se entrega un archivo armado por la skill como reemplazo.

El detalle de la biblioteca, las marcas de cita, la norma y las seis herramientas de fuentes está en `references/integracion_zotero.md`. **Leerlo antes de citar por primera vez** (con `redactar`, `referencia: "integracion_zotero.md"`). Al final de ese archivo están **las demás herramientas de su perfil** (Scopus con SciELO y ALICIA, Zotero, Mendeley, R, ATLAS.ti y el mapa en VOSviewer) y cuándo nombrarlas.

## Regla crítica de interactividad

**TODA pregunta que la skill haga al tesista debe usar `ask_user_input_v0` con opciones para tocar.** No usar nunca listas A/B/C en texto plano para que el tesista responda escribiendo. Excepción única: preguntas de texto libre absolutamente necesarias (por ejemplo, "pega el contexto que tienes hasta ahora"), donde el contenido no se puede anticipar con opciones.

**Recordatorio técnico**: cada objeto de pregunta dentro de `ask_user_input_v0` DEBE incluir el campo `question` con el texto literal de la pregunta. Sin este campo, la herramienta falla silenciosamente o muestra opciones sin contexto. Verificar siempre que `question` esté presente antes de invocar la herramienta.

## Cómo se activa

Tres situaciones disparan esta skill:

- El tesista llega **con el Capítulo I aprobado** y quiere avanzar al Capítulo II.
- El tesista llega con el **Capítulo I ya guardado** por la Skill de Problema y Objetivos y dice "ya tengo esto aprobado, ¿qué sigue?".
- El tesista llega **trabajando directamente esta fase**: "ayúdame con el marco teórico", "redacta mis antecedentes", "necesito las bases teóricas".

Si el tesista llega sin Capítulo I terminado, la skill **no procede** y lo deriva a la Skill de Problema y Objetivos.

## Mecanismo de rescate para tesistas principiantes (regla transversal)

Un principio operativo que aplica a **toda pregunta compleja** de esta skill: los tesistas de pregrado suelen no dominar la terminología metodológica. Preguntar directamente por "cantidad de antecedentes por bloque", "teoría base con autor", "tipo de antecedente (Coherencia / Discrepancia / Matiz / Cualitativo perceptual)" a alguien que recién arranca lo bloquea.

Regla: **en TODA pregunta que use términos metodológicos** (alcance de antecedentes, cantidad por bloque, categoría del antecedente, selección de términos del marco conceptual), la última opción del menú tocable debe ser siempre:

```
"Te ayudo a decidirlo con ejemplos sencillos"
```

Si el tesista elige esa opción, la skill responde en el mismo turno con:

1. **Reformulación en lenguaje simple** de la pregunta original, sin jerga.
2. **Explicación breve de cada opción** (30-40 palabras cada una).
3. **Un ejemplo concreto por cada opción, adaptado a la CARRERA del tesista** (recuperada del Cap I o preguntada). No dar ejemplos genéricos.
4. **Volver a preguntar** con `ask_user_input_v0` incluyendo las mismas opciones + una nueva:

```
"Sigo con dudas, quiero contactar al equipo de soporte"
```

Si el tesista elige esta última opción, la skill responde con el contacto directo:

```
Sin problema. Escríbenos al equipo Acosta para ayudarte
personalmente con tu caso:

📱 WhatsApp: +51 923 095 940

Mientras tanto, marco esta pregunta como PENDIENTE para
que la revises con el equipo o con tu asesor. Sigo con
las demás preguntas del capítulo.
```

Y continúa el flujo dejando la respuesta como "pendiente" en el checklist final.

### Cómo aprovechar la carrera para dar ejemplos

Ejemplos por carrera (guía interna, no exhaustiva):

- **Educación**: hablar de aulas, docentes, sesiones de clase, calificaciones, PISA, ECE.
- **Ciencias de la Salud**: hablar de pacientes, servicios de salud, hospitales, adherencia a tratamiento, indicadores clínicos.
- **Administración**: hablar de empresas, colaboradores, rotación de personal, ventas, satisfacción del cliente.
- **Contabilidad**: hablar de empresas, control interno, rentabilidad, evasión tributaria, estados financieros.
- **Psicología**: hablar de pacientes o participantes, tests estandarizados, sesiones de intervención.
- **Derecho**: hablar de expedientes, jurisprudencia, casos concretos, comparación normativa. Ojo: en Derecho la mayoría de tesis son cualitativas o dogmáticas, ajustar ejemplos.
- **Ingeniería**: hablar de procesos, sistemas, medición de indicadores técnicos, prototipo, propuesta de mejora.
- **Comunicación**: hablar de audiencias, medios, contenidos, campañas.

Si la carrera declarada NO está en esta lista, adapta con sentido común. Nunca inventes ejemplos específicos con nombres de instituciones reales; usa términos genéricos ("un hospital público", "una empresa comercial", "una I.E. pública").

## Regla técnica de menús interactivos

`ask_user_input_v0` acepta **máximo 4 opciones tocables por pregunta**. Nunca superar ese límite. Cuando el universo de opciones sea mayor, encadenar en 2 niveles (una pregunta que ramifica en otra). No truncar en silencio, no fusionar opciones sin decirle al tesista.

## Paso 0 — Bienvenida (siempre, primer mensaje)

Antes de cualquier pregunta, muestra el bloque de bienvenida. Es fijo en su estructura (banner + saludo) pero adaptado a la fase de esta skill (Marco Teórico, redacción del Capítulo II).

**Formato exacto del primer mensaje** (respetar espacios en blanco y caracteres):

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

   ACOSTA · IA & RESEARCH
   Método de Tesis con Agente IA

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

¡Bienvenido a las Skills de Acosta!

Estás en la **Skill 3 — Marco Teórico**. Aquí redactamos tu Capítulo II completo: antecedentes internacionales/nacionales/locales, bases teóricas por variable y marco conceptual. Este capítulo sostiene lo que vas a discutir después en el Capítulo V, así que la calidad de las fuentes que uses aquí decide la calidad de la discusión.

Necesito una cosa para trabajar bien: tu Capítulo I aprobado por tu asesor. Si lo guardaste con la Skill 2, lo leo yo de tu proyecto; si lo escribiste fuera, me lo pegas. Tus fuentes ya están en tu biblioteca, tu Zotero y tu Mendeley incluidos: aunque hayas abierto este chat desde cero, nada se perdió.
```

Después de este bloque, arrancas de inmediato con el Paso 1 (verificación de punto de partida). No pidas confirmación al tesista, no esperes que responda "listo" o "empecemos". La primera pregunta va en el mismo turno o en el siguiente inmediato.

Excepción: si `mi_proyecto` ya muestra el Capítulo I guardado, o el tesista dio los datos clave en su primer mensaje, muestra la bienvenida y luego reconoce lo que ya está decidido. No repitas preguntas cuyo dato ya tienes; salta directo a lo que falta.

### Regla dura del punto de partida — sale del proyecto, no de archivos

**Antes de preguntarle nada, la skill llama a `mi_proyecto` y a `ver_capitulo`.** Ahí están su tema, su universidad, su norma de citas, el estado de cada capítulo y lo acordado en los anteriores. Eso reemplaza a pedirle el Word del capítulo previo y a pedirle que pegue los datos a mano.

También reemplaza a la recuperación en chat nuevo: aunque el tesista abra una conversación desde cero, el proyecto y su biblioteca siguen ahí. No hay nada que rescatar del contexto.

**Solo se le pregunta lo que el proyecto no tenga.** Y cuando falte algo, se pregunta ese dato concreto, no el capítulo entero. Las fuentes no se piden: están en su biblioteca y se buscan con `buscar_fuentes` y `mis_fuentes`.

La vía de pegar los datos a mano se conserva **solo** para el tesista que trabajó fuera del método y no tiene el Capítulo I guardado.

## Paso 1 — Verificar punto de partida y continuidad con Cap I

Antes de cualquier cosa, la skill verifica que el tesista tenga el Capítulo I cerrado. Si `mi_proyecto` ya lo muestra guardado, no se pregunta: se lee directamente como en la primera opción. Si no, pregunta interactiva (single_select):

- "Lo trabajé con la Skill de Problema y Objetivos (léelo de mi proyecto)"
- "Pego manualmente los datos del Capítulo I (título, variables, dimensiones, teoría base)"
- "Aún no tengo el Capítulo I aprobado"

Si elige la tercera opción, la skill deriva a la Skill de Problema y Objetivos y termina la sesión.

**De dónde sale cada cosa:**

```
Teoría por variable    Indicada en el Capítulo I: nombre, autor
                       y año. Desarrollarla es trabajo de ESTA
                       skill.

Dimensiones            Fijadas en el ANEXO 2 del Capítulo I
                       (matriz de operacionalización), que viene
                       dentro del texto guardado de
                       problema-y-objetivos. NO se redefinen acá:
                       las bases teóricas se escriben para
                       sostener esas dimensiones, no otras.

Fuentes                Su biblioteca del proyecto (su Zotero o
                       Mendeley, sus exports, lo guardado por
                       DOI) y la de
                       Acosta. Las del Cap I ya están ahí.
```

**Regla dura**: si al desarrollar la teoría descubrís que las dimensiones del Anexo 2 no se sostienen en ella, **no las cambies por tu cuenta**. Decíselo al tesista y explicale que cambiarlas obliga a rehacer objetivos específicos, hipótesis y las dos matrices del Capítulo I. Si con su asesor decide cambiarlas, eso se hace en la Skill de Problema y Objetivos, que vuelve a guardar el Capítulo I completo con el Anexo 2 corregido; después se retoma aquí.

Si elige la primera opción, lee el Capítulo I con `ver_capitulo` (`capitulo: problema-y-objetivos`, `texto: true`; la clave exacta es la que muestra `mi_proyecto` o `listar_capitulos`). Cada respuesta trae una parte de hasta 24.000 caracteres y dice «parte N de M» y cuál pedir después: se sigue con `parte` (2, 3…) hasta la última, porque el Anexo 2 va al final. De ahí extrae automáticamente teoría base, variables, población, las dimensiones del Anexo 2 y las fuentes que cita (en el texto guardado vienen como claves `[AR…]`, y las matrices en su bloque de tabla). Solo si `ver_capitulo` dice que el capítulo no tiene texto guardado (lo escribió fuera de la plataforma), se le pide que lo pegue en el chat. Si falta algún campo, lo pregunta.

Si elige la segunda, pide en el siguiente turno:

```
- Título tentativo aprobado:
- Variable 1 (con sus dimensiones definitivas):
- Variable 2 (con sus dimensiones definitivas):
- Teoría base de V1 (autor + año):
- Teoría base de V2 (autor + año):
- Población:
- Contexto geográfico (ciudad, país):
- Año del estudio:
- Enfoque (cuantitativo / cualitativo / mixto):
- Nivel de investigación:
```

### Detección automática de inconsistencias

Antes de avanzar al Paso 2, la skill verifica:

- Teoría base de cada variable: ¿está claramente identificada con autor y año?
- Dimensiones: ¿las del Anexo 2 coinciden con las que la teoría base propone?
- Si hay inconsistencia, pausar y resolver con el tesista. No avanzar con datos contradictorios.

### Regla de escalamiento de datos críticos no respondidos

Esta skill no pide nombre, universidad, ciudad ni fecha: la portada la arma el Word del servidor con los datos del proyecto. Pero si pide un dato crítico **para el capítulo** (la teoría base de una variable, sus dimensiones, el país para los antecedentes) y el tesista no responde en el mismo turno o en el siguiente, la skill **no puede** seguir adelante como si nada. Debe:

1. **Reformular la pregunta como interactiva tocable** en el turno siguiente. Ejemplo: "Teoría base de V2" → 3 opciones: `Te la escribo ahora / Búscala en mi Capítulo I guardado / La confirmo con mi asesor y vuelvo`.
2. **Si tras la reformulación tampoco responde**, no se inventa el dato ni se deja una nota entre corchetes en el capítulo: se le dice en el chat qué falta y qué parte queda sin redactar, y el capítulo se guarda con `estado: EN_CURSO`.
3. **En el checklist del Paso 11**, listar todos los datos que quedaron pendientes para que el tesista los complete.

En pruebas de campo se detectó que la skill volvía a pedir el mismo dato hasta 4 turnos consecutivos sin respuesta y terminaba guardando el capítulo con huecos silenciosos. Esta regla lo previene.

## Paso 2 — Verificar fuentes disponibles

En pruebas de campo se detectó que la mayoría de tesistas **abre un chat nuevo** para cada capítulo. Antes eso obligaba a recuperar las fuentes de la Skill 2 a mano. **Ya no:** su biblioteca del proyecto guarda su Zotero o su Mendeley conectado, lo que trajo de Scopus, Web of Science o SciELO, y lo que guardó por DOI. Está ahí entre capítulos y entre conversaciones.

### Las fuentes ya están: no se le piden de nuevo (regla dura)

Lo que hace la skill, en este orden:

1. **`mis_fuentes`** para ver qué tiene y cuántas. Si quiere ver solo lo de su Zotero, `origen: "zotero"`; lo de su Mendeley, `origen: "mendeley"`.
2. **`buscar_fuentes`** por cada bloque temático que toque redactar (cada variable, cada nivel de antecedentes), **siempre con los tres campos**: `tema` en inglés, `temaOriginal` en español y `pais`. Busca a la vez en la biblioteca de Acosta y en la suya. Sin `temaOriginal` su Zotero y su Mendeley quedan fuera de la búsqueda.
3. **`buscar_en_la_literatura`** para los antecedentes nacionales y para fuentes en español, que es donde están SciELO, Redalyc y los repositorios latinoamericanos.
4. **`ampliar_desde_mis_fuentes`** cuando el tesista diga que no sabe qué más buscar, o cuando las búsquedas por palabras ya no den nada nuevo. Se le presentan para que **elija**, diciendo «lo citan N de tus fuentes», no «muy citado».
5. **`anadir_a_mis_fuentes`** con los DOI de las que apruebe. **Preguntar antes**: no se guarda lo que no pidió.

Con el resultado de `mis_fuentes` a la vista, pregunta con `ask_user_input_v0` (single_select):

- "Trabajemos con lo que hay en mi biblioteca"
- "Quiero agregar fuentes nuevas además de las del Cap I"
- "En mi Zotero (o Mendeley) tengo fuentes que no aparecen"
- "Te ayudo a decidirlo con ejemplos sencillos"

**Qué se le pide al tesista y qué no**:

```
NO se le pide              SÍ se le pide
─────────────────────────  ──────────────────────────────
Que traiga de nuevo sus    Que confirme qué fuentes nuevas
 exports de Scopus          quiere guardar en su biblioteca
Que pegue resultados        Que conecte o actualice su
 que ya están guardados      Zotero o Mendeley si falta
                             algo suyo
Que repita lo del Cap I
```

Si dice que en su Zotero o su Mendeley tiene una fuente que no aparece: en su perfil, «Tu Zotero» o «Tu Mendeley» → «Actualizar ahora». O puede que esa fuente no esté en la colección que eligió.

Si le faltan antecedentes, sobre todo nacionales, se le recuerda que en su perfil, «Tus herramientas» → «Tus fuentes de Scopus», busca a la vez en Scopus y SciELO, y en las tesis peruanas de ALICIA, y añade a su biblioteca con un clic las que elija. Si quiere una figura que muestre cómo se estudia el tema (qué conceptos van juntos, quiénes publican), «Mapa en VOSviewer», del mismo perfil, la hace; entra al capítulo como figura, con su marca `[Insertar aquí la Figura N: …]`. Si pega resultados copiados de Scholar Labs o Google Académico, esas fuentes todavía no tienen clave: se le ofrece añadir por DOI las que quiera usar, con `anadir_a_mis_fuentes`.

Si `buscar_fuentes` no aparece entre las herramientas del conector, se trabaja con `mis_fuentes` y se le dice que desconecte y vuelva a conectar el conector en claude.ai para refrescar la lista.

### Decir de dónde viene cada fuente (regla dura)

Las tres procedencias no valen lo mismo y **no se presentan igual**. La respuesta de cada herramienta dice de cuál viene cada fuente, y la skill traslada ese dato al tesista:

```
PROCEDENCIA              CÓMO SE PRESENTA
───────────────────────  ─────────────────────────────────────
Biblioteca de Acosta     Lleva criterio editorial. Se presenta
                         sin advertencia.

Biblioteca del tesista   La eligió él y NO está revisada por
(su Zotero, su Mende-    Acosta. Se dice al presentarla.
ley, sus exports)

Catálogo abierto         OpenAlex indexa de todo, incluidos
(buscar_en_la_           repositorios y preprints. Se advierte
literatura, ampliar_     siempre, y se presenta para que ELIJA,
desde_mis_fuentes)       no como si ya fuera suya.
```

### Cobertura respecto del Capítulo I

Antes de avanzar, la skill compara lo que va a citar en el Cap II con lo citado en el Cap I, que ya leyó con `ver_capitulo` en el Paso 1 (las claves `[AR…]` del texto guardado). Reporta:

```
Fuentes en tu biblioteca: [N]
Citadas en el Cap I: [N]
Se reutilizan en el Cap II: [N]
Nuevas que entran: [N]
```

Reutilizar fuentes del Cap I es lo esperable y **no es un problema**: es lo que da continuidad al argumento. Lo que sí se señala es lo contrario, que el Cap II **no reutilice ninguna**, porque entonces los dos capítulos están hablando de cosas distintas:

```
Ninguna de las fuentes que citaste en el Capítulo I aparece
en lo que vamos a usar ahora. ¿Es intencional (el Cap II
abre literatura nueva) o conviene retomar algunas?
```

### Nunca fingir que están

Si `mis_fuentes` devuelve la biblioteca vacía, o casi, se dice tal cual: "Tu biblioteca tiene [N] fuentes". Se le indica que conecte su Zotero o su Mendeley desde su perfil o que cargue sus exports en «Mis fuentes», y mientras tanto se busca con `buscar_fuentes` y `buscar_en_la_literatura`. Nunca se redacta como si hubiera fuentes que no aparecen en ninguna herramienta.

## Paso 3 — Decidir alcance de antecedentes

Pregunta interactiva al tesista (single_select):

- "Antecedentes internacionales + nacionales + locales"
- "Solo internacionales + nacionales (sin locales)"
- "Solo internacionales (mi tema es muy nuevo en mi país)"
- "Te ayudo a decidirlo con ejemplos sencillos"

### Si incluye antecedentes nacionales o locales — dónde se buscan

Primero se mira lo que ya tiene: `buscar_fuentes` con `tema` en inglés, `temaOriginal` en español y `pais` (el código de dos letras del tesista). Después, `buscar_en_la_literatura` con el mismo tema en español y el `pais`: ahí están SciELO, Redalyc y los repositorios latinoamericanos que indexa el catálogo abierto. Lo que aparezca se presenta diciendo su procedencia (Paso 2) y el tesista elige qué se añade.

Las tesis de repositorios universitarios muchas veces no están en el catálogo abierto. Para esas, se le sugiere la búsqueda en:

- Repositorio nacional del país (Renati, ALICIA si Perú; equivalentes para México, Colombia, Ecuador, Chile, Argentina, España).
- Repositorios institucionales de universidades de la región/ciudad del tesista.
- SciELO del país.

**Búsqueda obligatoria antes de declarar ausencia**: cuando el tesista declare NO tener antecedentes locales o pida directamente "declara que no existen", la skill **DEBE** ejecutar las búsquedas de arriba y una búsqueda web mínima antes de aceptar la ausencia. Esta regla existe porque:

1. Los antecedentes locales son los que más peso dan al párrafo local del Cap I y a la Discusión (Skill 8).
2. Declarar "no existen antecedentes locales" sin haber buscado es una afirmación falsa que expone al tesista frente al jurado.
3. La búsqueda de tesis y artículos en repositorios abiertos del país declarado NO es "hacer la tesis por el tesista": es verificación mínima de contexto.

### Protocolo obligatorio de búsqueda web de antecedentes locales

Si el tesista declara "no tengo antecedentes locales" o pide declarar la ausencia, la skill ejecuta:

1. **Mínimo 3 consultas de web_search** dirigidas al país declarado. Ejemplos para Perú:
   - `[variable 1] [variable 2] tesis Perú site:renati.sunedu.gob.pe`
   - `[variable 1] [variable 2] tesis Perú site:alicia.concytec.gob.pe`
   - `[variable 1] [variable 2] [ciudad del tesista] repositorio universidad`
   - Para otros países, adaptar el `site:` al repositorio equivalente.

2. **Web_fetch de los resultados relevantes** para verificar que son fuentes reales con autor, año, universidad, tipo de estudio.

3. **Presentar al tesista lo encontrado** con este formato exacto en el chat:

```
Búsqueda web de antecedentes locales — [PAÍS]

Realicé 3 consultas y encontré [N] fuentes candidatas:

1. Ruiz, C. (2023). [Título completo].
   Tesis de pregrado, [Universidad], [Ciudad].
   URL de descarga: https://[repositorio]/[id-tesis]
   Aporte al tema: [1-2 líneas sobre por qué es relevante]

2. Jiménez Esquivel, M. (2021). [Título completo].
   [Tipo de documento], [Institución].
   URL de descarga: https://[repositorio]/[id-tesis]
   Aporte al tema: [...]

3. [siguiente...]

IMPORTANTE — Advertencia obligatoria:
Estas fuentes NO las has leído tú y NO están revisadas
por Acosta. Yo las encontré por búsqueda web y validé
metadatos, pero para citarlas en tu tesis debes:
(a) Descargar el PDF desde la URL indicada.
(b) Leerlas y confirmar que aportan lo que digo.
(c) Tenerlas en tu biblioteca para que lleven clave:
    las que tengan DOI las agrego yo si me das permiso;
    las demás las agregas a tu Zotero, tu Mendeley o «Mis fuentes».
(d) Solo entonces autorizarme a incluirlas en el capítulo.

¿Cómo procedemos?
```

4. **Preguntar con `ask_user_input_v0`** (single_select):

```
· Las leo y las agrego a mi biblioteca (te aviso cuando estén)
· Agrega por DOI las que lo tengan; las leo antes de entregar
· No las incluyas, declara honestamente la ausencia
   ("la búsqueda realizada el [fecha] no identificó
   antecedentes locales")
· Te ayudo a decidirlo con ejemplos sencillos
```

Una fuente sin clave no entra al capítulo: mientras no esté en su biblioteca, el antecedente no se redacta, o la afirmación que la necesitaba va con `[FALTA FUENTE]` y se le avisa en el chat.

5. **Solo si las 3 consultas web devuelven vacío** puede la skill declarar honestamente la ausencia, especificando que la búsqueda web se ejecutó y no encontró resultados. La declaración debe incluir la fecha de la búsqueda y los repositorios consultados, para que el asesor pueda verificar.

**Prohibido**: redactar "luego de una búsqueda no se identificaron antecedentes" si esa búsqueda no consta en la conversación. Es una afirmación de procedimiento inexistente que expone al tesista.

Ver `references/busqueda_antecedentes.md` para tutorial detallado por país.

## Paso 4 — Definir cantidad de antecedentes

El default del método es **4 antecedentes internacionales, 4 nacionales y 3 locales**. Es un punto medio deliberado: alcanza para sostener el capítulo y para alimentar la discusión de la Skill 8, sin inflar el trabajo del tesista ni el capítulo. Si necesita más, lo pide y la skill lo amplía sin objetar.

Esta cifra es **sugerencia**, no exigencia. Cada universidad tiene reglamentos distintos: una I.E. pública del MINEDU, una universidad privada con reglamento APA estricto, la UNT, la UCV, la USS, la UNPRG, todas piden cantidades diferentes. **El tesista conoce su reglamento mejor que el método**, y la skill debe respetar su decisión.

### Cómo preguntar al tesista (2 niveles para respetar el límite de 4 opciones)

Debido al límite técnico de `ask_user_input_v0` (máximo 4 opciones), la pregunta se hace en 2 niveles: primero un shortcut, luego el detalle.

**Nivel 1 — Preferencia general** (`ask_user_input_v0`, single_select):

```
· Aplicar el default del método (4 internacionales, 4 nacionales, 3 locales)
· Quiero más antecedentes (te doy detalle bloque por bloque)
· Mi reglamento pide cantidad exacta distinta (te la digo)
· Te ayudo a decidirlo con ejemplos sencillos
```

Si elige "Aplicar el default", la skill usa **4 internacionales, 4 nacionales y 3 locales** y avanza sin más preguntas. Es el camino más rápido y el que cubre la mayoría de los casos.

Si elige "Quiero más antecedentes", la skill activa el **Nivel 2** con tres preguntas encadenadas:

**Nivel 2a — Internacionales**:

```
· 4 (default del método)
· 5-6 (ampliado)
· 7-8 (extenso, si tu reglamento lo pide)
· Otro número, lo escribo (texto libre)
```

**Nivel 2b — Nacionales**:

```
· 4 (default del método)
· 5-6 (ampliado)
· 3 (compacto, si hay poca literatura nacional)
· Otro número, lo escribo (texto libre)
```

**Nivel 2c — Locales** (solo si el tesista los incluyó en el Paso 3):

```
· 3 (default del método)
· 4-5 (ampliado)
· 2 (mínimo, si hay poca literatura local)
· No incluir
· Otro número, lo escribo (texto libre)
```

Si el tesista pide un número fuera del rango sugerido (por ejemplo, 3 internacionales), la skill **respeta su decisión sin cuestionar**, asumiendo que es lo que su reglamento exige. NO pausa para preguntar "¿estás seguro?". El criterio del tesista, sustentado por su reglamento universitario, prevalece.

### Validación de disponibilidad + búsqueda web complementaria (regla dura)

Si el tesista pide un número **mayor al disponible** (ej. pide 4 internacionales pero `buscar_fuentes` solo devuelve 2 pertinentes, o pide 4 nacionales y solo hay 1), la skill NO fuerza el número ni fabrica citas. Antes de aceptar la brecha, **ofrece ampliar la búsqueda**.

**Cuándo se activa**: automáticamente cuando `N_disponibles < N_solicitados` para cualquiera de las tres categorías (internacionales, nacionales, locales).

**Cómo se ofrece** (con `ask_user_input_v0`):

```
Detecté que pediste [N_solicitados] antecedentes 
[internacionales/nacionales] pero entre tu biblioteca y la
de Acosta solo hay [N_disponibles] pertinentes.

¿Te ayudo a buscar [N_faltantes] fuentes académicas más?
Primero busco en el catálogo abierto y a partir de las
fuentes que ya tienes; si no alcanza, en la web (SciELO
regional, DOAJ, repositorios universitarios del [país
declarado]). Te traigo cada fuente con su procedencia y
nada entra sin tu confirmación explícita.

· Sí, buscá y traé [N_faltantes] opciones para revisar
· No, prefiero buscar yo y agregarlas a mi Zotero o Mendeley
· Trabajemos con las [N_disponibles] que hay (asumo el
  riesgo de bloque más corto)
· Te ayudo a decidirlo con ejemplos sencillos
```

**Si el tesista acepta la búsqueda** (opción 1), la skill sigue este orden:

1. `buscar_en_la_literatura` con el tema y, para nacionales, el `pais` del tesista (y `idioma` español si conviene).
2. `ampliar_desde_mis_fuentes`, que devuelve lo que citan varias de sus fuentes y él no tiene («lo citan N de tus fuentes»).
3. Solo si con eso no alcanza, `web_search` con las consultas según el tipo de antecedente:

**Para antecedentes INTERNACIONALES**:

```
Consultas web_search sugeridas:
· [V1] [V2] [población] site:scholar.google.com filetype:pdf
· [V1] [V2] site:doaj.org (Directory of Open Access Journals)
· [V1] [V2] [población] scielo (regional en español)
· [V1] [V2] "systematic review" 2022..2026 (últimos 4 años)
· [V1] [V2] "meta-analysis" 2022..2026
· [V1] [V2] site:frontiersin.org (Frontiers, open access)
· [V1] [V2] site:mdpi.com (MDPI, open access)
```

**Para antecedentes NACIONALES** (adaptar `site:` al país):

```
Perú:
· [V1] [V2] site:renati.sunedu.gob.pe
· [V1] [V2] site:alicia.concytec.gob.pe
· [V1] [V2] site:scielo.org.pe

Colombia:
· [V1] [V2] site:funes.uniandes.edu.co
· [V1] [V2] site:scielo.org.co
· [V1] [V2] site:redib.org filter:CO

México:
· [V1] [V2] site:redalyc.org pais:México
· [V1] [V2] site:scielo.org.mx

Ecuador:
· [V1] [V2] site:dspace.utpl.edu.ec
· [V1] [V2] site:repositorio.puce.edu.ec

Chile:
· [V1] [V2] site:scielo.conicyt.cl
· [V1] [V2] site:repositorio.uchile.cl

Argentina:
· [V1] [V2] site:scielo.org.ar
· [V1] [V2] site:ri.conicet.gov.ar

España:
· [V1] [V2] site:dialnet.unirioja.es
· [V1] [V2] site:tdx.cat

País no listado:
· [V1] [V2] tesis repositorio universitario [país]
· [V1] [V2] SciELO [país]
```

**Regla dura de transparencia (idéntica a la de antecedentes locales)**: cada fuente que Claude traiga por `buscar_en_la_literatura`, `ampliar_desde_mis_fuentes` o `web_search` se entrega con marca visible de su procedencia:

```
FUENTE COMPLEMENTARIA [INTERNACIONAL/NACIONAL] #N — 
[encontrada por Claude en catálogo abierto / web,
 no está en tu biblioteca ni revisada por Acosta]

  Fuente: [OpenAlex / Google Scholar / DOAJ / SciELO / repositorio X]
  Lo citan: [N] de tus fuentes (solo si vino de la bola de nieve)
  URL verificada: [URL]
  Título: "[título completo]"
  Autores: [autores con formato APA]
  Año: [año]
  Tipo: [artículo revisado por pares / tesis pregrado / 
        tesis maestría / revisión sistemática / meta-análisis]
  País/región de la investigación: [si aparece]
  Aporte al tema: [1-2 líneas por qué es relevante]
  Fragmento clave del abstract: "[cita literal breve]"

  ⚠ Fuente encontrada por Claude, no leída por vos. Para
    citarla en tu tesis debés:
    (a) Descargar el PDF desde la URL.
    (b) Leer el abstract completo.
    (c) Confirmar que aporta lo que digo.
    (d) Recién entonces autorizame a guardarla en tu
        biblioteca (con `anadir_a_mis_fuentes` si tiene
        DOI; si no, la agregás a tu Zotero, Mendeley o «Mis
        fuentes») para que lleve clave y entre al
        capítulo.
```

**Regla dura anti-invención**: la skill NUNCA fabrica una fuente. Si `web_search` no devuelve resultados relevantes tras 3 consultas distintas, la skill lo declara así:

```
Ejecuté 3 consultas en [bases usadas] y no encontré 
fuentes académicas [internacionales/nacionales] 
pertinentes sobre este tema con los criterios actuales.

Opciones:
· Ampliamos con búsqueda por una sola variable (V1 sola)
· Ampliamos con búsqueda por sinónimos de V1 (te propongo cuáles)
· Aceptamos el bloque con las [N] fuentes que ya tenés + nota
   explícita al asesor sobre la brecha de literatura (puede
   convertirse en fortaleza de la tesis: "línea de investigación
   poco explorada")
· Te ayudo a decidirlo con ejemplos sencillos
```

**Regla dura de confirmación por fuente**: cada fuente encontrada por Claude requiere `ask_user_input_v0` explícito antes de agregarla a su biblioteca y al bloque:

```
· Acepto esta fuente: guardala en mi biblioteca y sumala al bloque
· Descarto esta fuente (no me convence)
· La reviso y decido después
· Sigo revisando las demás que trajiste
```

Una fuente encontrada por Claude NUNCA se agrega en silencio al bloque ni a su biblioteca. El tesista siempre confirma una por una, y solo con su sí se llama a `anadir_a_mis_fuentes` con los DOI que vinieron de la búsqueda (nunca uno recordado).

## Paso 5 — Seleccionar y redactar antecedentes

Este paso tiene dos sub-pasos obligatorios. **NO redactar directamente sin validar la selección con el tesista.**

### Paso 5a — Presentar selección al tesista (ANTES de redactar)

#### Regla de balance: antecedentes que NO favorecen (obligatoria)

**El sesgo que esta regla corrige**: al seleccionar antecedentes, la tendencia natural es quedarse con los estudios que confirman lo que el tesista espera encontrar. El resultado es un marco teórico que parece cerrado antes de recoger los datos, y un tesista sin munición cuando llegue a la discusión.

**Por qué importa tanto**: los antecedentes son el insumo principal del Capítulo de Discusión (Skill 8). Si todos apuntan en la misma dirección y los resultados salen distintos, el tesista se queda sin con qué contrastar. Y si salen iguales, la discusión se reduce a "coincide con todos", que es la discusión más pobre posible.

**Regla dura**: de la selección total de antecedentes, **entre 2 y 3 deben presentar resultados que NO favorecen la hipótesis o expectativa del tesista**. Pueden ser de cualquiera de los tres bloques (internacional, nacional o local).

Qué cuenta como antecedente que no favorece:

```
· Encontró relación NO significativa donde el tesista
   espera significativa
· Encontró relación en sentido CONTRARIO al esperado
· Encontró que el efecto desaparece al controlar por otra
   variable (mediación o moderación que el tesista no
   contempla)
· Encontró resultados distintos en una población parecida
   a la del tesista
· Cuestiona la validez del instrumento o del constructo
   que el tesista va a usar
```

Qué NO cuenta:

```
· Un estudio de otro tema que simplemente no habla del
   asunto
· Un estudio con población o contexto tan distinto que la
   comparación no es legítima
· Un estudio metodológicamente débil citado solo para
   descartarlo
```

**Cómo la skill lo maneja**:

1. Al armar la selección, marca cada antecedente con su categoría: **Coherencia** (apoya lo esperado), **Discrepancia** (no lo apoya), **Matiz** (lo apoya con condiciones).
2. Si tras la selección hay **menos de 2 discrepancias**, lo declara y ofrece buscar:

```
En tu selección de [N] antecedentes, [N] apoyan lo que
esperás encontrar y solo [N] presenta resultados distintos.

Eso te va a jugar en contra en la discusión: si tus
resultados salen distintos a lo esperado, no vas a tener
con qué contrastarlos, y si salen iguales, tu discusión se
reduce a "coincide con todos".

· Buscá 2 o 3 estudios con resultados distintos
· Revisá otra vez mi biblioteca, capaz hay alguno que descartaste
· Sigo con esta selección (asumo el riesgo en la discusión)
· Te ayudo a decidirlo con ejemplos sencillos
```

3. Si acepta la búsqueda, la skill primero **revisa la biblioteca del tesista** (`buscar_fuentes` con `temaOriginal`, o `mis_fuentes`) buscando estudios con resultados no significativos o contrarios, que suelen haberse descartado en la primera pasada precisamente por no encajar. Después prueba `buscar_en_la_literatura` y `ampliar_desde_mis_fuentes`. Solo si ahí no aparecen, ejecuta `web_search` con consultas orientadas:

```
· [V1] [V2] "no significant" OR "no relationship" [población]
· [V1] [V2] "negative relationship" OR "inverse" [población]
· [V1] [V2] "mixed results" OR "contradictory findings"
· [V1] [V2] "failed to replicate" OR "null findings"
```

Toda fuente encontrada se entrega marcada como tal y requiere aceptación explícita del tesista, igual que el resto de la búsqueda complementaria.

**Regla dura de honestidad**: si tras revisar su biblioteca, el catálogo abierto y la web no aparecen estudios discrepantes, **no inventar uno ni forzar la lectura de un estudio para que parezca discrepante**. Se declara al tesista:

```
No encontré estudios con resultados contrarios sobre este
tema. Puede ser que la literatura sea consistente, y eso
también es un hallazgo: conviene decirlo explícitamente en
tu capítulo ("la literatura revisada converge en...") y
retomarlo en la discusión si tus resultados se apartan.
```

4. En la redacción, las discrepancias **no se esconden ni se relativizan**. Se integran con la misma extensión que las coherencias. Frases como "aunque algunos estudios aislados encontraron..." minimizan y quedan mal: si el estudio es serio, se presenta como serio.

#### Presentación de la selección

La skill analiza lo que devolvieron `buscar_fuentes`, `buscar_en_la_literatura` y `ampliar_desde_mis_fuentes`, y selecciona los antecedentes más pertinentes según criterios de score (presencia de V1, V2, secundaria/población similar, año reciente). Antes de invertir tiempo en redacción, la skill presenta su propuesta al tesista en formato de checklist con esta información:

```
Para cada antecedente propuesto:
- Apellido del primer autor + año
- Procedencia: biblioteca de Acosta / tu biblioteca /
   catálogo abierto (este último, pendiente de tu OK para
   guardarlo y darle clave)
- País del estudio (si aparece en abstract)
- Categoría: Coherencia / Discrepancia / Matiz / Cualitativo perceptual
- Una línea con el aporte principal al estudio
- Si tiene rasgo especial (mismo contexto geográfico, mismo nivel
   educativo, etc.), destacarlo con un símbolo (⭐)

BALANCE DE LA SELECCIÓN
   Coherencia:   [N]
   Discrepancia: [N]   → mínimo 2, ideal 3
   Matiz:        [N]
   Total:        [N]
```

Luego pregunta al tesista con `ask_user_input_v0`:

- "Sí, redacta los X antecedentes con esta selección"
- "Cambiar 1-2 antecedentes (te indico cuáles)"
- "Quiero ver más opciones antes de decidir"
- "Te ayudo a decidirlo con ejemplos sencillos"

**Regla dura**: si el balance muestra menos de 2 discrepancias, la skill ejecuta primero el bloque de arriba y recién después presenta esta pregunta. No se avanza a la redacción con una selección sesgada sin habérselo dicho al tesista.

Solo después de validación, pasa al Paso 5b.

### Paso 5b — Redactar antecedentes en prosa

Cada antecedente se redacta como **párrafo en prosa académica**, no como ficha. Contenido obligatorio de cada párrafo:

1. **Autor con su clave**: el apellido en la frase y la clave detrás, `Apellido [AR…:n]` (el año y el formato los pone el servidor según la norma).
2. **Objetivo del estudio** (qué se propuso investigar).
3. **Metodología** (enfoque, diseño, población, muestra).
4. **Hallazgo principal** (el resultado más relevante para tu tesis).
5. **Aporte a tu estudio** (qué te sirve, qué validas, qué complementas).

**Los cinco elementos son contenido, no un orden fijo.** Cada antecedente los lleva en el orden que mejor le sirva. No todos abren con «Apellido [AR…:n] se propuso…»: unos entran por el hallazgo, otros por el contexto o el método, y alguno puede integrar dos estudios en una misma oración. Tampoco miden todos lo mismo: uno se extiende en el método y otro apenas lo menciona. Los antecedentes que siguen todos el mismo molde son lo que Turnitin marcó en un capítulo real al 86 % de IA.

**Longitud sugerida: 100 a 180 palabras por antecedente**, variando de uno a otro. El rango original del método (80-130) es demasiado corto para cubrir los 5 elementos con prosa fluida. Se ajustó al rango actual basado en prueba de campo.

### Sub-secciones y prosa continua

Cada bloque (internacionales / nacionales / locales) lleva un subtítulo numerado (2.1.1, 2.1.2, 2.1.3), pero dentro del bloque la redacción es **prosa continua** con conectores entre antecedentes. NO listar antecedentes como bullets. Articular el debate entre los estudios.

**Regla crítica anti-clonación**: la skill NO usa siempre los mismos conectores entre antecedentes. Rota entre variantes según la relación con el antecedente anterior. Si dos tesis del método usan los mismos conectores en el mismo orden, se detecta clonación.

**La mayoría de los antecedentes no necesita conector de apertura**: basta con que el párrafo retome lo que dijo el anterior o entre directo por el estudio. Las variantes que siguen son solo ejemplos para cuando la relación sí pide conector, y la lista no se recorre en orden.

**Ejemplos de conectores por tipo de relación**:

**Coincidencia con antecedente anterior** (elegir 1 cada vez, rotar):
- "De manera similar, Apellido [AR…:n] ..."
- "En la misma dirección, Apellido [AR…:n] ..."
- "Coincidiendo con lo anterior, Apellido [AR…:n] ..."
- "En sintonía con este hallazgo, Apellido [AR…:n] ..."

**Cambio de enfoque, misma variable** (elegir 1):
- "Por su parte, Apellido [AR…:n] ..."
- "Desde una perspectiva complementaria, Apellido [AR…:n] ..."
- "Con un enfoque distinto, Apellido [AR…:n] ..."
- "Abordando el fenómeno desde otro ángulo, Apellido [AR…:n] ..."

**Contraste o discrepancia** (elegir 1):
- "En contraste, Apellido [AR…:n] ..."
- "A diferencia de los estudios anteriores, Apellido [AR…:n] ..."
- "Un hallazgo divergente lo aporta Apellido [AR…:n], quien ..."
- "Frente a esa postura, Apellido [AR…:n] reporta ..."

**Matiz o condición** (elegir 1):
- "Un matiz relevante lo introduce Apellido [AR…:n], al observar que ..."
- "Con una condición importante, Apellido [AR…:n] señala ..."
- "Apellido [AR…:n] precisa que estos resultados solo se sostienen cuando ..."

Regla operativa: dentro del mismo bloque (ej. 2.1.1 Internacionales), la skill **no repite el mismo conector**.

**Al guardar**: `guardar_capitulo` devuelve AVISOS DE REDACCIÓN cuando varios párrafos abren igual o seguidos con el autor y su cita. Esos párrafos se corrigen con `reescribir_parrafos`, sin listar conectores en el chat.

Ver `references/antecedentes.md` para reglas detalladas y ejemplos de redacción.


## Paso 6 — Redactar bases teóricas

Estructura obligatoria: **por variable**. Primero V1 con su teoría base, luego V2 con la suya. Cada bloque ocupa **entre 1 y 2 páginas** del documento final.

### Paso 6.0 — Validación de aplicaciones recientes + búsqueda web complementaria (regla dura)

Antes de redactar cada bloque (V1 y V2), la skill busca con `buscar_fuentes` (`tema` en inglés con el nombre de la teoría, `temaOriginal` en español, `pais`) y cuenta cuántas fuentes con clave aplican **la teoría base declarada en el Cap I** a estudios recientes (últimos 5 años). Este es el sustento del movimiento 7 de la estructura interna ("Aplicaciones recientes").

**Cuándo se activa**: automáticamente cuando `N_aplicaciones < 3` para cualquiera de las dos variables (V1 o V2).

**Cómo se ofrece** (con `ask_user_input_v0`):

```
Para tu Variable [1/2] la teoría base es [nombre de la 
teoría] de [autor original].

Detecté entre tu biblioteca y la de Acosta
[N_aplicaciones] fuentes recientes (últimos 5 años) que
aplican esta teoría. Para redactar un bloque de bases
teóricas sólido conviene tener al menos 3 aplicaciones
recientes.

¿Te ayudo a buscar aplicaciones recientes de [teoría]?
Busco primero en el catálogo abierto y a partir de tus
fuentes; si no alcanza, en la web (Google Scholar,
Frontiers, MDPI, SciELO, DOAJ), artículos que usen
[teoría] entre 2021 y 2026. Sigo el mismo protocolo de
transparencia y confirmación explícita por fuente.

· Sí, buscá aplicaciones recientes de [teoría]
· Redactá con las [N_aplicaciones] que tengo (asumo 
  bloque más apoyado en el autor original)
· Te ayudo a decidirlo con ejemplos sencillos
```

**Si el tesista acepta la búsqueda** (opción 1), la skill usa primero `buscar_en_la_literatura` (con el nombre de la teoría y un `desdeAnio` de hace cinco años) y `ampliar_desde_mis_fuentes`. Solo si con eso no llega a 3, ejecuta:

```
Consultas web_search sugeridas:
· "[teoría base]" [variable] 2022..2026 filetype:pdf
· "[teoría base]" [población] "empirical study" 2022..2026
· "[teoría base]" [contexto/región] site:scielo.org
· "[teoría base]" [aplicación esperada] site:frontiersin.org
· "[teoría base]" [aplicación esperada] site:mdpi.com
· "[teoría base]" "cross-sectional" 2023..2026 (o el 
   diseño metodológico similar al del tesista)
```

**Entrega al tesista con la misma marca visible que los antecedentes complementarios**:

```
FUENTE COMPLEMENTARIA PARA TEORÍA BASE #N — 
[encontrada por Claude en catálogo abierto / web,
 no está en tu biblioteca ni revisada por Acosta]

  Fuente: [OpenAlex / Google Scholar / Frontiers / MDPI / SciELO]
  URL verificada: [URL]
  Título: "[título completo]"
  Autores: [autores APA]
  Año: [año]
  Aplicación de [teoría]: [1-2 líneas sobre cómo el
    artículo aplica la teoría al fenómeno relevante para
    tu variable]
  Contexto de la aplicación: [país, población, sector]
  Fragmento clave: "[cita literal breve del abstract 
    donde se ve la aplicación de la teoría]"

  ⚠ Fuente encontrada por Claude, no leída por vos. Para
    citarla debés: descargar el PDF, leer, confirmar, y
    autorizar explícitamente que la guarde en tu biblioteca
    para que tenga clave.
```

**Regla dura anti-invención**: si tras 3 consultas distintas no aparecen aplicaciones recientes de la teoría, la skill lo declara honestamente y propone alternativas:

```
Ejecuté 3 consultas y no encontré aplicaciones recientes
publicadas de [teoría] al [fenómeno de interés]. Esto
puede significar:

(a) La teoría es sólida pero se aplica poco al contexto
    específico (oportunidad de aporte).
(b) Los términos de búsqueda necesitan ajuste.
(c) La aplicación reciente existe pero en literatura
    no indexada libremente.

Opciones:
· Ampliamos búsqueda con sinónimos de [teoría]
   (te propongo cuáles)
· Ampliamos búsqueda con aplicaciones a poblaciones 
   diferentes de la tuya
· Redactamos el bloque destacando al autor original + las
   [N] fuentes que ya tenés, con nota sobre la escasez de
   aplicaciones recientes como oportunidad de aporte
· Te ayudo a decidirlo con ejemplos sencillos
```

**Regla dura de confirmación por fuente**: cada aplicación reciente encontrada por Claude requiere `ask_user_input_v0` explícito antes de guardarla en su biblioteca (`anadir_a_mis_fuentes` con el DOI que vino de la búsqueda) y citarla con su clave en el bloque de bases teóricas. Nunca se agrega en silencio al bloque.

### Estructura interna de cada bloque (V1, V2)

Subtítulo con el nombre de la variable (2.2.1 [Nombre V1], 2.2.2 [Nombre V2]).

**Problema detectado en campo que esta estructura corrige**: las bases teóricas salían débiles, como una sucesión de ideas aisladas ("la teoría dice A. También dice B. Otro autor dice C"). El lector no veía por qué esa teoría y no otra, ni cómo cada postulado aterriza en la variable del tesista. El resultado era un bloque que se podía copiar a cualquier tesis cambiando el nombre de la variable.

**Regla del hilo argumental**: el bloque no es un resumen de la teoría, es un **argumento** que responde una pregunta: por qué esta teoría es la adecuada para estudiar esta variable en esta población. Cada movimiento se encadena con el anterior. Si un párrafo se puede borrar sin que el resto pierda sentido, ese párrafo no estaba argumentando.

Dentro del subtítulo, prosa continua que cubra estos siete movimientos:

1. **Origen y problema que la teoría vino a resolver**: autor original, año, y sobre todo **qué vacío o pregunta buscaba responder**. No basta con "Autor [AR…:n] propuso la teoría X". Hay que decir contra qué reaccionaba: qué explicación previa resultaba insuficiente. Es lo que le da sentido a todo lo que sigue.

2. **Postulados centrales, jerarquizados**: no listar todos con el mismo peso. Desarrollar en profundidad los dos o tres que sostienen la variable del tesista y despachar el resto en una línea. Un autor que domina la teoría se detiene donde importa.

3. **Evolución de la teoría**: cómo se modificó o amplió desde el planteamiento original. Qué autores posteriores la corrigieron, la extendieron o la discutieron. Una teoría presentada como si no hubiera cambiado desde su origen suena a manual, no a marco teórico.

4. **Por qué esta teoría y no las alternativas**: mencionar en dos o tres líneas qué otras teorías compiten para explicar la variable y por qué se descartaron para este estudio. **No desarrollarlas** (la regla de una teoría base por variable sigue vigente), solo justificar la elección. Este movimiento es el que más levanta la calidad del bloque y el que casi siempre falta.

5. **Cómo aterriza en la variable del tesista**: la teoría se formuló en un contexto y el tesista la aplica en otro. Explicitar el puente: qué se conserva, qué se adapta, qué supuestos hay que asumir para usarla en esta población.

6. **Dimensiones sustentadas**: cada dimensión definitiva (las del Anexo 2 del Capítulo I, fijadas en la Skill de Problema y Objetivos) con el autor que la sustenta y su clave y con su definición conceptual. En prosa, no en viñetas. Acompañadas de la **Tabla de dimensiones** (ver más abajo).

7. **Aplicaciones recientes**: cómo otros autores usaron la teoría en estudios similares en los últimos cinco años, de las fuentes de la biblioteca o de la búsqueda del Paso 6.0. Con qué población, con qué resultados, con qué limitaciones.

### Tabla y figura obligatorias por variable

La prosa sola no alcanza para que el jurado vea la estructura del constructo. Cada bloque de bases teóricas se acompaña de una tabla y una figura.

**Tabla de dimensiones** (una por variable). Así se ve en el Word; en el texto que se guarda se escribe como bloque de tabla (Paso 10):

```
Tabla [N]

Dimensiones de [nombre de la variable] según [Autor]

Dimensión          Definición conceptual        Autor que la sustenta
─────────────────  ───────────────────────────  ─────────────────────
[D1]               [definición en una o dos     [Autor] [AR…:n]
                    líneas, parafraseada]
[D2]               [...]                        [Autor] [AR…:n]
[D3]               [...]                        [Autor] [AR…:n]

Nota. Elaboración propia a partir de [Autor] [AR…:n].
```

Formato APA 7 estricto, que aplica el Word del servidor: número de tabla en negrita, título en cursivas, sin bordes verticales, solo tres líneas horizontales (encima y debajo del encabezado y al final), nota al pie con "Nota." en cursivas, interlineado sencillo dentro de la tabla.

**Figura del modelo teórico** (una por variable, o una integrada para ambas):

```
Figura [N]

Modelo teórico de [nombre de la variable] según [Autor]

[Diagrama: el constructo al centro y sus dimensiones
 alrededor o debajo, con las relaciones que la teoría
 postula entre ellas]

Nota. Adaptado de [Autor] [AR…:n].
```

**Reglas duras de la figura**:

- El Word del servidor no inserta imágenes. En el texto que se guarda van el rótulo de la figura, un párrafo con la marca `[Insertar aquí la Figura N: modelo-teorico-v1.png]` y la nota (ver Paso 10). La figura es un diagrama simple de cajas y conectores: la skill le describe al tesista las cajas y las flechas, y él la dibuja (en Word, PowerPoint u otra herramienta), la guarda con ese nombre de archivo y la pega en el lugar marcado del Word descargado. Nada de imágenes decorativas ni descargadas.
- Si la teoría no postula relaciones entre dimensiones (solo las enumera), la figura muestra el constructo y sus dimensiones sin flechas. **No inventar relaciones que la teoría no plantea.**
- Si el tesista prefiere solo la tabla, se respeta. La skill pregunta con `ask_user_input_v0` antes de generar la figura:

```
· Tabla y figura para cada variable (recomendado)
· Solo la tabla de dimensiones
· Solo la figura del modelo
· Ninguna de las dos, prosa nada más
```

- La numeración de tablas y figuras es **continua a lo largo del capítulo** y arranca donde corresponda si el Capítulo I ya trajo tablas. La skill pregunta al tesista con qué número debe empezar.
- Toda tabla y figura se **cita en el texto antes de aparecer**: "La Tabla 1 resume las dimensiones de [variable] según [Autor]". Una tabla que aparece sin haber sido anunciada es una observación segura del asesor.

### Refuerzo de la teoría con el documento original

Si la biblioteca del tesista no incluye la obra original de la teoría base (lo habitual: tiene a quienes la aplican, no a quien la formuló), el bloque queda apoyado en fuentes de segunda mano. La skill lo detecta con `buscar_fuentes` y `mis_fuentes` y lo ofrece resolver:

```
Tu teoría base para [variable] es [teoría] de [autor original,
año], pero en tu biblioteca no veo la obra original: las [N]
fuentes que citan esa teoría son de autores que la aplican.

Eso se nota en el capítulo, porque los postulados quedan
contados por terceros.

· Buscá el documento original y lo revisamos
· Lo tengo: lo agrego a mi Zotero, mi Mendeley o «Mis fuentes»
· Trabajamos con lo que hay (queda apoyado en fuentes
  secundarias, lo declaro en el texto)
· Te ayudo a decidirlo con ejemplos sencillos
```

Si acepta la búsqueda, la skill prueba primero `buscar_en_la_literatura` con el nombre de la teoría y del autor. Si no aparece, ejecuta `web_search` orientada a la obra original:

```
· "[nombre de la teoría]" [autor original] [año] filetype:pdf
· "[nombre de la teoría]" [autor] original paper
· [autor] [año] "[título de la obra]" texto completo
· "[nombre de la teoría]" site:researchgate.net
· "[nombre de la teoría]" site:scielo.org OR site:redalyc.org
```

**Regla dura**: la skill entrega lo que encuentre con la marca de origen y el enlace, y el tesista confirma antes de que se use; para citarla, la obra tiene que entrar a su biblioteca y tener clave. Si no encuentra la obra original en acceso abierto, lo dice y propone la salida honesta: redactar apoyándose en la fuente secundaria más citada y **declararlo en el texto** ("según la lectura que [Autor secundario] [AR…:n] hace de la propuesta original de [Autor]", con la clave de la fuente secundaria). Nunca citar una obra original que no se pudo consultar.

### Reglas críticas

- **Una teoría base por variable**, no varias rivales. El método de Acosta IA Research lo dice explícitamente: "no metas 5 teorías rivales en el mismo capítulo". La teoría ya fue elegida en el Capítulo I (Skill de Problema y Objetivos), esta skill la desarrolla, no la cambia.
- **Prosa continua**, no listado de dimensiones con viñetas. Cada dimensión se integra en el párrafo que describe la teoría.
- **Sin citas textuales largas**. Toda la cita debe ser paráfrasis con cambio estructural. Solo cita textual si la frase es absolutamente esencial y no se puede parafrasear, máximo 40 palabras.

Ver `references/bases_teoricas.md` para reglas detalladas y plantilla de redacción.

## Paso 7 — Redactar marco conceptual

La skill propone una lista inicial de términos para definir, basada en:

- Las 2 variables del estudio.
- Las dimensiones de cada variable (las definitivas del Anexo 2 del Capítulo I).
- Términos técnicos clave que aparecen en el estudio (instrumentos como CCTDI, AI Literacy; estadísticos como alfa de Cronbach, correlación de Pearson; constructos asociados).

### Cantidad de términos y advertencia sobre longitud

El método de Acosta IA Research sugiere entre **8 y 12 términos**. El ebook describe esta sección como "la más corta del Capítulo II", pero esto solo se cumple cuando se eligen 8 términos compactos. **Importante**: con 10-12 términos, esta sección puede llegar a 4-5 páginas y desbalancear el capítulo. Si el tesista quiere muchos términos, la skill debe advertirle de esta consecuencia visual antes de proceder.

Como referencia de balance:
- 8 términos → ~2-3 páginas (recomendado).
- 10 términos → ~3-4 páginas.
- 12 términos → ~4-5 páginas (advertir al tesista que esta sección dejará de ser "la más corta" y rivalizará con las bases teóricas).

### Cómo presentar la lista al tesista

La skill propone una lista de 10 a 12 candidatos agrupados por categoría (variables, dimensiones, constructos asociados, términos técnicos). Luego ofrece al tesista cuatro caminos con `ask_user_input_v0` (single_select):

- "Aplicar la recomendación de la skill (8 términos seleccionados)" → atajo de un toque
- "Incluir todos los términos propuestos"
- "Yo elijo cuáles quiero (te indico con multi_select)"
- "Te ayudo a decidirlo con ejemplos sencillos"

Si el tesista quiere agregar términos que no están en la lista, puede escribirlos en texto libre después de elegir "yo elijo cuáles quiero".

Si el tesista elige "yo elijo cuáles quiero", la skill **debe usar una segunda llamada de `ask_user_input_v0` con tipo `multi_select`** ofreciendo todos los candidatos en formato de checkbox, en lugar de pedirle al tesista que escriba números en texto libre. El multi_select es más rápido en mobile y reduce errores.

### Estructura de cada definición

Cada término tiene dos partes obligatorias:

1. **Definición citada**: del autor de referencia (teoría base o autor consolidado), con la clave de su fuente.
2. **Definición operacional**: cómo se entiende el término en el contexto del estudio del tesista.

Aunque cada término es un bloque definido, los términos se redactan **en prosa académica continua**, no en lista con bullets. El subtítulo del término va en negrita o cursiva al inicio del párrafo, seguido inmediatamente de la prosa.

Ejemplo de redacción esperada:

> **Disposición al pensamiento crítico**. Facione [AR…:n] define este constructo como la predisposición actitudinal de un individuo a aplicar procesos de razonamiento estructurado, búsqueda de verdad, análisis y juicio prudente al enfrentar problemas o información compleja. En el presente estudio se entiende disposición al pensamiento crítico como la tendencia, medida con el CCTDI adaptado, de los estudiantes de cuarto y quinto de secundaria a cuestionar, analizar y verificar la información que reciben de herramientas de inteligencia artificial generativa, en sus siete dimensiones operacionales.

Ver `references/marco_conceptual.md` para reglas y más ejemplos.

### Revisión ortográfica final del bloque (obligatoria y visible)

Después de redactar el marco conceptual, la skill debe pasar una revisión ortográfica **explícita** antes de guardar el capítulo. NO ejecutarla "internamente" ni saltarla. Reportar al tesista en el chat:

```
REVISIÓN ORTOGRÁFICA — Cap II

Errores detectados y corregidos:
- "arquitectónicas" → "arquitecturas" (2 ocurrencias)
- "aliniamiento" → "alineamiento" (1 ocurrencia)

Repeticiones de muletillas detectadas y variadas:
- "el presente estudio" aparecía 8 veces → 4 sustituidas
   por "esta investigación" / "este trabajo"
- "los autores señalan" aparecía 6 veces → 3 sustituidas
   por "los autores reportan" / "los autores destacan"

Comas y punto y coma agregados: [N]

Estado: OK / con correcciones aplicadas
```

Solo entonces cerrar el Paso 7 y avanzar al Paso 8.


## Paso 8 — Paráfrasis y prevención de plagio (paso OBLIGATORIO, no interno)

Toda la redacción de los Pasos 5, 6 y 7 debe pasar por las reglas de paráfrasis del método. **No se permite el copy-paste con sinónimos**, considerado plagio disfrazado.

Este paso NO es una verificación "interna" opcional. Es un **paso obligatorio y visible** que produce un entregable revisable por el tesista antes de guardar el capítulo. Un tesista que no vea la auditoría en el chat, sabe que no se ejecutó.

### Reglas de paráfrasis del método

Una buena paráfrasis cambia tres cosas a la vez:

1. **La estructura de la oración**: si el original es "sujeto + verbo + complemento", la paráfrasis puede empezar por el complemento, usar pasiva, o dividir en dos oraciones.
2. **Las palabras conectoras y la sintaxis**: no solo sustantivos, también verbos y conectores.
3. **La voz**: la paráfrasis debe sonar a redacción académica latinoamericana, no al inglés técnico o al estilo del original.

### Riesgo asimétrico según idioma de la fuente

Fuentes en inglés → paráfrasis en español obliga a traducir. La traducción fuerza reescritura estructural. El riesgo de coincidencia textual es bajo.

Fuentes en español (típicamente locales y nacionales) → paráfrasis en español puede quedar peligrosamente cerca del original si no se aplica **reescritura estructural forzada**:

- Cambiar orden sujeto-verbo-complemento (usar pasiva, empezar por complemento).
- Partir oraciones largas en dos cortas.
- Sustituir verbos comunes por sinónimos académicos (analiza → examina, encuentra → reporta, muestra → evidencia).
- Cambiar el conector inicial de la idea.
- **Ninguna cadena de 5+ palabras del original debe sobrevivir** salvo nombres propios, listas de dimensiones fijas o terminología metodológica sin sinónimo ("diseño no experimental", "alfa de Cronbach", "pensamiento crítico").

### Auditoría de paráfrasis (entregable OBLIGATORIO antes de guardar el capítulo)

Antes de guardar el capítulo, la skill audita **cada paráfrasis** contra su original y muestra al tesista una tabla resumen en el chat. NO se guarda el capítulo sin este paso.

Formato exacto del entregable (mostrar en el chat, no ocultar):

```
AUDITORÍA DE PARÁFRASIS — Skill 3

┌─────────────────────────────────┬──────────┬──────────────┬─────────┐
│ Antecedente / bloque            │ Idioma   │ Coincidencias│ Estado  │
│                                 │ fuente   │ 5+ palabras  │         │
├─────────────────────────────────┼──────────┼──────────────┼─────────┤
│ 1. Sk y Halder (2024)           │ Inglés   │ 0            │ OK      │
│ 2. Christodoulakis (2023)       │ Inglés   │ 1 (nombre)   │ OK      │
│ ...                             │ ...      │ ...          │ ...     │
│ 8. Ruiz (2023) - LOCAL          │ Español  │ 25           │ PLAGIO  │
│ 9. Jiménez Esquivel (2021) LOCAL│ Español  │ 21           │ PLAGIO  │
│ Bases teóricas V1               │ Inglés   │ 2 (concepto) │ OK      │
│ Bases teóricas V2               │ Inglés   │ 1 (concepto) │ OK      │
│ Marco conceptual                │ Mixto    │ 3            │ RIESGO  │
└─────────────────────────────────┴──────────┴──────────────┴─────────┘

TOTAL de cadenas idénticas detectadas: [N]
Umbral aceptable: máximo 3 cadenas por antecedente
   (solo si son nombres propios, dimensiones o metodología fija)

Estado global: OK / REQUIERE REESCRITURA

Antecedentes con PLAGIO o RIESGO detectado:
- [Apellido, año] — cadenas problemáticas:
   · "[cadena de 5+ palabras del original]"
   · "[otra cadena]"
   → Acción: reescribiendo automáticamente ahora.
```

### Regla dura de reescritura

Si el estado global es "REQUIERE REESCRITURA", la skill:

1. Reescribe automáticamente cada párrafo con estado PLAGIO o RIESGO aplicando reescritura estructural forzada.
2. Vuelve a auditar los párrafos reescritos.
3. Solo cuando TODOS los estados sean OK, avanza al Paso 10 (guardar el capítulo y entregar el Word).
4. Muestra al tesista el diff (antes / después) de las reescrituras principales para transparencia.

No se acepta "auto-certificación" ("todo correcto") sin haber mostrado la tabla de conteo real.

### Redacción sin moldes: la cuenta la hace el servidor

La skill escribe siguiendo las reglas de redacción que ya trae `redactar` (sin moldes, con la voz del tesista) y las del Paso 10. No imprime en el chat auditorías de patrones ni métricas (conteos de oraciones, dispersión, largo de palabra, checks). Al guardar, `guardar_capitulo` devuelve los AVISOS DE REDACCIÓN que calcula el servidor; los párrafos señalados se corrigen con `reescribir_parrafos` (capítulo `marco-teorico`), sin reenviar el capítulo entero. Si tras dos reescrituras un aviso persiste, el problema es de contenido y no de estilo: se dice y se propone una salida de contenido (menos aplicaciones, otro orden, quitar una dimensión redundante). `references/parafraseo.md` Parte 2 sigue sirviendo de catálogo para reescribir.

### Nota honesta al tesista al cierre del Paso 8

Al terminar la auditoría, la skill declara:

```
La auditoría automática detectó [N] cadenas de 5+ palabras
idénticas al original y las reescribí. Aun así, Turnitin
puede marcar terminología metodológica fija ("diseño no
experimental", nombres de instrumentos, dimensiones de
teoría) que NO se puede parafrasear. En pregrado peruano
suele aceptarse hasta 20% de coincidencias siempre que sean
de este tipo. Si tu porcentaje sale alto, revisa qué está
subrayado antes de asumir que es problema del capítulo.
```

Ver `references/parafraseo.md` para ejemplos de paráfrasis correcta vs. plagio disfrazado.

## Paso 9 — Errores comunes a evitar

La skill debe detectar y evitar estos 6 errores del método de Acosta IA Research:

1. **Marco teórico con citas antiguas únicamente**: si todas las fuentes son de hace 15-20 años, agregar al menos 30% de fuentes de los últimos 5 años.
2. **Antecedentes sin aporte explícito**: cada antecedente debe terminar diciendo qué le aporta al estudio actual. Si no se dice, falta el cierre.
3. **Bases teóricas sin teoría**: si una sección de "base teórica" solo lista definiciones de varios autores sin desarrollar UNA teoría, hay que reescribir.
4. **Marco conceptual con fuentes no académicas**: prohibido citar Wikipedia, blogs, sitios sin autor académico.
5. **Citas textuales largas**: si una cita textual pasa de 40 palabras, parafrasear.
6. **Ausencia de voz propia**: el capítulo debe leerse como un argumento construido por el tesista, no como una colección de párrafos pegados.

## Paso 9.5 — Norma de citas (la pone el servidor, no se convierte a mano)

Las citas van con la **clave de cada fuente entre corchetes**, nunca escritas a mano: `[AR97D22F86]` para una cita normal, `[AR97D22F86:n]` detrás del nombre si el autor va en la frase («Hernández-Sampieri [AR97D22F86:n] sostiene…»), `[AR97D22F86:p. 45]` con página, y varias seguidas (`[AR…][AR…]`) para una cita con varias fuentes. Las claves salen de `mis_fuentes`, `buscar_fuentes` o `anadir_a_mis_fuentes`.

Al descargar el Word, el servidor de Acosta escribe cada cita y la lista de referencias en la norma del proyecto, en el orden que esa norma pide y con la numeración continua de toda la tesis en Vancouver e IEEE. Por eso **no se convierte, no se numera y no se arma a mano la lista de referencias**: la norma es una sola para toda la tesis, así que los capítulos coinciden solos, y si el asesor pide otra más adelante se cambia sin reescribir ningún capítulo.

### Sub-paso 9.5.1 — Confirmar la norma

Mirá la línea «Norma de citas» que devuelve `mi_proyecto`.

- **Si ya está elegida**: no se vuelve a preguntar. Es la de toda la tesis.
- **Si dice «sin elegir»**: preguntala con `ask_user_input_v0` y guardala con `guardar_avance` (campo `estiloCitas`):

```
¿Qué norma de citas te pide tu universidad o tu asesor?

· APA 7 (la más común)
· Vancouver (Ciencias de la Salud)
· IEEE (Ingenierías e informática)
· Otra (me decís cuál)
```

Si elige «Otra», buscala entre las que acepta `guardar_avance` (APA, IEEE, Vancouver, AMA, ACS, Nature, MLA, Chicago, Harvard, APSA, ASA, MHRA y otras). Si la que pide no está, decíselo tal cual y no la aproximes sin su acuerdo. Nunca la supongas por la universidad. Si escribe la tesis en inglés, guardá también `idiomaCitas`.

Si el tesista no sabe qué norma usa, que abra un capítulo ya aprobado y mire una cita: `(Apellido, 2024)` es APA, `(1)` es Vancouver, `[1]` es IEEE.

### Sub-paso 9.5.2 — Auditoría de citas (obligatoria antes de guardar el Capítulo II)

```
AUDITORÍA DE CITAS

Norma del proyecto: [X] (ya elegida / preguntada y guardada)
Afirmaciones con fuente: [N]
   Todas con su clave [AR…]: SÍ / NO (cuáles faltan)
Citas escritas a mano —(Apellido, 2024), (1), [1]—: [N] → deben ser 0
Claves que no salieron de una búsqueda o de la biblioteca: [N] → deben ser 0
Lista de referencias escrita a mano en el capítulo: NO
Afirmaciones que necesitan fuente y no la tienen: [lista]
   → marcadas [FALTA FUENTE] y avisadas al tesista

Estado: OK PARA GUARDAR / CORREGIR
```

**Regla dura**: nunca inventar una clave ni una fuente. Si una fuente que el tesista trajo al chat (por ejemplo, de su export de Scopus) no tiene clave, pedile permiso y añadila con `anadir_a_mis_fuentes` por su DOI; si no tiene DOI, que la suba en «Mis fuentes» de su perfil o la tenga en su Zotero o su Mendeley. Lo que quede sin respaldo se marca `[FALTA FUENTE]` y se le avisa. `revisar_evidencia` sirve para comprobar el capítulo guardado.

**Regla dura**: el formato APA 7 de las **tablas** no cambia con la norma de citas: es diseño editorial, no citación.

## Paso 10 — Guardar el capítulo y entregar el Word

Esta es la entrega final. **Se guarda automáticamente** al terminar el marco conceptual (Paso 7) y las verificaciones de los Pasos 8 y 9.5, sin preguntar al tesista si lo quiere y sin pedir confirmación adicional.

Razón: el tesista ya validó cada bloque (antecedentes, bases teóricas, marco conceptual) en su momento. Pedir una confirmación más antes de guardar introduce un turno innecesario y fricciona la experiencia. La regla es: tras validar el último bloque (marco conceptual), la skill guarda el capítulo, da el enlace del Word y avanza al Paso 11 (cierre). Si el tesista pide ver el capítulo completo antes, se le muestra en la conversación y se guarda cuando lo apruebe.

Antes de guardar, la auditoría de paráfrasis del Paso 8 y la del Sub-paso 9.5.2 (citas: todas con clave `[AR…]`, ninguna escrita a mano, cada `[FALTA FUENTE]` avisado) tienen que estar en OK. Si alguna no lo está, se corrige primero.

### Estructura del capítulo (el texto que se guarda)

Lo que se guarda es el texto del capítulo en Markdown, tal como va a la tesis: `##` y `###` para los subtítulos numerados, párrafos separados por una línea en blanco, `**negrita**` y `*cursiva*`, citas con clave y tablas en bloque. **Sin encabezado con datos personales ni título del capítulo**: la portada y el título de cada capítulo guardado los pone el Word del servidor. El texto empieza en 2.1.

Este es el orden de los subtítulos y lo que va debajo de cada uno. Aquí se muestran como lista para que se lean bien; en el texto que se guarda, cada subtítulo va en su propia línea, sin viñeta ni sangría, empezando por `##` o `###`:

- `## 2.1 Antecedentes`
  - `### 2.1.1 Antecedentes internacionales` — prosa continua con los antecedentes internacionales acordados en el Paso 4 (4 por defecto), redactados en párrafos cortos articulados con conectores académicos, cada estudio con su clave `[AR…]`.
  - `### 2.1.2 Antecedentes nacionales` — prosa continua con los antecedentes nacionales acordados en el Paso 4 (4 por defecto).
  - `### 2.1.3 Antecedentes locales` — prosa continua con los antecedentes locales acordados en el Paso 4 (3 por defecto). Si no hay, se omite la sub-sección y se declara la ausencia en 2.1.2 o en una observación al final de 2.1.
- `## 2.2 Bases teóricas`
  - `### 2.2.1 [Nombre Variable 1]` — prosa de 1-2 páginas con los 7 movimientos: origen y vacío que la teoría vino a resolver, postulados jerarquizados, evolución, por qué esta teoría y no las alternativas, cómo aterriza en la variable del tesista, dimensiones sustentadas, aplicaciones recientes. Después, la tabla de dimensiones de V1 (bloque de tabla) y la figura del modelo teórico de V1 (rótulo, marca y nota).
  - `### 2.2.2 [Nombre Variable 2]` — igual estructura para V2, con su tabla y su figura.
- `## 2.3 Marco conceptual` — prosa con 8-12 términos. Cada término inicia con su nombre en `**negrita**` seguido de prosa con definición citada (con clave) y definición operacional. Sin listas con bullets.

El capítulo no lleva sección «Referencias» al final.

**Tabla de dimensiones** (si el tesista la eligió en el Paso 6). Un solo bloque, sin líneas en blanco; el Word le aplica el formato APA 7 (número en negrita, título en cursiva, tres líneas horizontales, ninguna vertical, interlineado sencillo, nota debajo):

```
**Tabla N**
*Dimensiones de [nombre de la variable] según [Autor]*
| **Dimensión** | **Definición conceptual** | **Autor que la sustenta** |
|---|---|---|
| [D1] | [definición en una o dos líneas, parafraseada] | [Autor] [AR…:n] |
| [D2] | [...] | [Autor] [AR…:n] |
*Nota.* Elaboración propia a partir de [Autor] [AR…:n].
```

Cada fila va en una sola línea y con las mismas celdas que la cabecera; una barra literal dentro de una celda se escribe `\|`.

**Figura del modelo teórico** (si el tesista la eligió en el Paso 6). El Word del servidor no inserta imágenes: en el texto van el rótulo, un párrafo con la marca y el nombre del archivo, y la nota.

```
**Figura N**
*Modelo teórico de [nombre de la variable] según [Autor]*

[Insertar aquí la Figura N: modelo-teorico-v1.png]

*Nota.* Adaptado de [Autor] [AR…:n].
```

La marca se escribe siempre igual, `[Insertar aquí la Figura N: archivo.png]`, para que el tesista la encuentre con Buscar y pegue ahí el diagrama que dibujó.

### Reglas de redacción en prosa

- **Subtítulos como organización, no como fragmentación**: los subtítulos 2.1.1, 2.2.1, etc. organizan el documento pero la redacción dentro de cada subtítulo es **prosa continua**, no bullets ni listas.
- **Conectores académicos entre párrafos** solo cuando la relación los pide (muchos párrafos no llevan; no repetir siempre el mismo ni seguir este orden): "De manera similar...", "Por su parte...", "En contraste...", "Desde otra perspectiva...", "Estos hallazgos coinciden con...", "Una postura alternativa propone...".
- **Tercera persona obligatoria**.
- **Cero de los 14 patrones anti-IA** (ver `references/parafraseo.md` Parte 2 para catálogo completo). Resumen crítico:
   - P0 (paralelismo de plantilla): no describir 3 antecedentes/dimensiones/teorías con oraciones GEMELAS.
   - P0b (tics de reescritura): no aperturas sentenciosas sin retomar, no aposiciones que metan al autor en el medio.
   - P0c (frase-etiqueta): no etiquetar con oración corta lo que la siguiente desarrolla.
   - P1 (inflar importancia): cero "constituye un hito", "marca un antes y un después", "pilar fundamental".
   - P2 (gerundios colgados): eliminar "evidenciando", "permitiendo", "contribuyendo a" al final de oraciones.
   - P3 (lenguaje promocional): cero "holístico", "integral", "novedoso", "de vanguardia", "robusto" fuera de estadística.
   - P4 (atribución vaga): cero "diversos autores", "la literatura sugiere", "numerosos estudios". Reemplazar por autor concreto de la biblioteca, con su clave.
   - P5 (evitar verbo ser): reducir "constituye", "representa", "se erige como" a formas con "es" o verbos plenos.
   - P6 (nominalización en cadena): convertir "la implementación de estrategias de fortalecimiento" en "fortalecer".
   - P7 (regla de tres ornamental): si tres elementos dicen lo mismo con distinta palabra, dejar UNO.
   - P8 (rotación de sinónimos): términos técnicos SE REPITEN, no se rotan.
   - P9 (rayas largas): cero rayas (— y –). Reemplazar por coma, punto, dos puntos o paréntesis.
   - P10 (contrastes fabricados): cero "en el fondo", "la verdadera pregunta es", "más allá de".
   - P11 (conectores en exceso): máximo 2 por página. Cero "cabe destacar", "es importante mencionar", "asimismo".
   - P12 (cierres optimistas): cero "el futuro se presenta prometedor", "sin duda representa un aporte".
   - P13 (restos chatbot): cero "a continuación se presenta", "en resumen".
   - P14 (formato): cero negritas dentro de párrafos (excepción: primera aparición del término definido en marco conceptual).
- **Sin auditorías de estilo en el chat**: se escribe con estas reglas, se guarda y se corrigen con `reescribir_parrafos` los AVISOS DE REDACCIÓN que devuelva `guardar_capitulo` (ver Paso 8).

### Formato de página

Lo aplica el Word del servidor: la plantilla de la facultad si el tesista la subió; si no, el formato por defecto de la plataforma. No se configura a mano. Los subtítulos numerados (2.1, 2.1.1, etc.) se escriben con `##` y `###`, y su estilo lo pone el Word. Si el reglamento de su universidad pide algo distinto y no subió la plantilla, decíselo: puede subirla o ajustar el documento en Word.

### Referencias: las arma el servidor

El capítulo no lleva lista de referencias. Al descargar el Word, el servidor arma **una sola lista** con todas las fuentes citadas en cualquier capítulo guardado, en la norma del proyecto. Las fuentes del Capítulo I que se vuelven a citar en el Capítulo II aparecen una sola vez, y nunca hace falta pedirle al tesista la lista del Capítulo I ni unirla a mano.

Si los datos de una fuente están mal o incompletos (por ejemplo, le falta el DOI), no se corrigen en el capítulo: se corrigen en el Zotero o el Mendeley del tesista, o en «Mis fuentes» de su perfil, y la próxima descarga del Word sale corregida. Nunca se inventa un dato que falta.

Para las teorías base originales que no están entre las fuentes del tesista vale la excepción del inicio: se buscan con `buscar_fuentes`; si no están, se le pide que las agregue, y si no se puede, la afirmación va con `[FALTA FUENTE]`.

### Guardar y entregar

**Regla dura**: no armes el Word ni ningún otro archivo con código ni con ninguna otra herramienta, y no escribas una lista de referencias. El Word y la bibliografía los arma el servidor; uno hecho a mano no llevaría la norma del proyecto ni coincidiría con las fichas de las fuentes.

1. **Guardá el capítulo** con `guardar_capitulo`, clave `marco-teorico` (la que muestra `listar_capitulos`). Cada llamada admite hasta 30.000 caracteres. El Capítulo II suele pasar de ese largo: mandalo por partes, cortando entre secciones o entre párrafos y nunca dentro de una tabla, la primera parte sin `anadir` y las siguientes con `anadir: true`. Si más adelante el tesista corrige el capítulo entero, se manda completo otra vez, sin `anadir`. Si la respuesta trae AVISOS DE REDACCIÓN, corregí esos párrafos con `reescribir_parrafos` antes de dar el enlace.
2. **Registrá lo acordado** con `guardar_avance` (capítulo `marco-teorico`): un resumen de dos o tres frases con lo que quedó decidido (antecedentes por nivel, teorías base desarrolladas, términos del marco conceptual). Marcá `estado: LISTO` solo si el tesista dice que da el capítulo por bueno; si no, `EN_CURSO`.
3. **Dale el enlace** con `enlace_del_word` y explicáselo:

```
Tu Capítulo II quedó guardado. Acá tenés el enlace para
descargar tu tesis en Word: [enlace]

El Word lo arma el servidor con todos los capítulos que
tenés guardados, en orden, con portada e índice. Las citas
y la lista de referencias salen en la norma de tu proyecto
([norma]), en una sola lista para toda la tesis.

Las figuras no van dentro: pegá cada diagrama donde dice
[Insertar aquí la Figura N: …] y borrá la marca. El enlace
vence a la media hora; si ya pasó, pedime otro.
```

(Si no hay figuras, se omite ese párrafo.) Ya guardado, `revisar_evidencia` comprueba que cada afirmación tenga respaldo en sus fuentes.

### Frontera con el documento de cierre de tesis

Esta skill escribe SOLO el Capítulo II. NO incluye dedicatoria, agradecimientos, resumen ni otras páginas preliminares. Eso es trabajo de la Skill de Revisión Final. La portada y el índice los pone el Word del servidor.

## Paso 11 — Cierre y validación humana

Checklist final al tesista:

```
- [ ] Lleva el documento a tu asesor antes de avanzar al Capítulo III.
- [ ] Revisa en el Word que cada cita tenga su referencia con
       los datos correctos. Si una ficha está mal o incompleta,
       corrígela en tu Zotero, tu Mendeley o «Mis fuentes» y vuelve a
       descargar el Word.
- [ ] Si quedó alguna afirmación con [FALTA FUENTE], consigue
       esa fuente y agrégala a tu biblioteca antes de la
       versión final. [Listar aquí cuáles.]
- [ ] Consulta la obra original de cada teoría base antes de
       la versión final, sobre todo si el bloque quedó apoyado
       en fuentes secundarias.
- [ ] Completa los datos que quedaron pendientes en esta
       sesión. [Listar aquí cuáles, si hay.]
- [ ] Si tu universidad usa Turnitin, pásalo antes de entregar.
       El objetivo es menos de 20% de coincidencias en pregrado
       peruano. Si sale más alto, marca los párrafos problemáticos
       y reescríbelos.
- [ ] Confirma con tu asesor que las teorías base desarrolladas
       son las que tu línea de investigación acepta.
- [ ] No avances al Capítulo III (Metodología) hasta tener el
       Capítulo II validado.
```

Después del checklist, invita al siguiente paso:

> Cuando tu asesor apruebe el Capítulo II, regresa y activa la **Skill de Metodología** (Skill 4, Capítulo III de la tesis). Ahí construimos el tipo, nivel, diseño, población, muestra, técnicas e instrumentos del estudio.

## Lo que esta skill NO hace

- **No diseña la metodología** del estudio: técnicas, instrumentos, validación, muestreo. Eso es la Skill de Metodología (Cap III de la tesis).
- **No construye el instrumento ni los ítems**: eso es la Skill de Instrumento (Cap V).
- **No elige ni guarda fuentes por el tesista**: busca en su biblioteca y en la de Acosta, en el catálogo abierto y, cuando hace falta, en la web (Pasos 2 a 6), pero presenta cada fuente con su procedencia y **el tesista decide** qué entra. Nada se añade a su biblioteca sin su permiso. Antes de declarar que no hay antecedentes locales, la búsqueda es obligatoria (Paso 3).
- **No inventa autores, años ni datos**: si una fuente no tiene clave en la biblioteca, no se cita.
- **No genera carátula ni páginas preliminares**: eso es trabajo de la Skill de Revisión Final.

Si el tesista pide algo de esa lista, derívalo a la skill correspondiente.

## Archivos de referencia

- `references/antecedentes.md` — Cómo redactar antecedentes en prosa, ejemplos buenos y malos, conectores entre párrafos, cómo articular debate.
- `references/bases_teoricas.md` — Estructura de las bases teóricas por variable, cómo presentar postulados, dimensiones sustentadas, aplicaciones recientes.
- `references/marco_conceptual.md` — Cómo elegir los 8-12 términos, plantilla de definición citada + operacional, ejemplos por área.
- `references/parafraseo.md` — Las 3 reglas de paráfrasis del método, ejemplos de paráfrasis correcta vs. plagio disfrazado, antipatrones prohibidos.
- `references/busqueda_antecedentes.md` — Cómo buscar antecedentes locales en repositorios nacionales (Renati, ALICIA si Perú; equivalentes para otros países hispanohablantes).
- `references/apa7_referencias.md` — Formato APA 7 de las referencias, como conocimiento para revisar la lista que arma el Word del servidor (la lista no se escribe a mano).
