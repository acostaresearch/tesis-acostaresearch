---
name: discusion
description: Acompaña a tesistas hispanohablantes a redactar el capítulo de Discusión de su tesis. Lee del proyecto el Cap II (Marco Teórico), el capítulo de Resultados (Skill 7) y los objetivos del Cap I, y redacta el Capítulo V — Discusión organizado POR OBJETIVOS específicos; lo guarda en el proyecto y da el enlace al Word que arma el servidor, con citas y referencias en la norma del proyecto. Para cada objetivo redacta un párrafo con los 4 movimientos del método: recordar el hallazgo sin repetir tablas, comparar con antecedentes que tengan clave en su biblioteca, interpretar el porqué en la población del tesista y señalar la implicancia. Antes de redactar comprueba qué afirmaciones tienen fuente. Incluye opcionalmente limitaciones del estudio según el diseño. NO incluye Recomendaciones (Skill 9). Prosa académica, sin bullets ni tablas. ACTIVAR cuando el usuario diga "discusión", "discutir resultados", "contrastar con literatura", "limitaciones". Es la OCTAVA skill del método.
---

# Skill de Discusión

## Para qué sirve esta skill

Esta es la octava skill del método de tesis con Agente IA. Acompaña al tesista a redactar el **Capítulo V — Discusión** de su tesis, donde los hallazgos numéricos de la Skill 7 se convierten en interpretación académica con literatura.

Esta skill NO cubre el capítulo de Resultados (eso lo hace la Skill 7). Cubre ÚNICAMENTE la Discusión.

Pertenece al método de Acosta IA Research y respeta sus tres reglas de oro:

1. **Cero referencias inventadas.** La skill solo contrasta con autores que tienen clave `[AR…]`: los del Cap II del tesista y, si hace falta, fuentes de su biblioteca. NO inventa antecedentes ni fabrica coincidencias.
2. **Contexto siempre.** Antes de redactar, la skill verifica antecedentes disponibles, hallazgos por objetivo, decisiones de hipótesis. Si falta información, pregunta.
3. **Validación humana al final.** Lo que la skill produce es propuesta. El asesor revisa antes de incorporar a la tesis. La voz académica final es del tesista.

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un .docx, un PDF ni ningún otro archivo del capítulo.** No usa la skill `docx`, no escribe en `/mnt/user-data/outputs/`, no usa `present_files` y no entrega archivos en el chat.

El documento lo arma el servidor de la plataforma con lo que está guardado en el proyecto: portada, índice, capítulos en orden, y las citas y las referencias escritas en la norma del proyecto, enlazadas a Zotero cuando el tesista lo conectó. La skill **redacta, guarda y entrega el enlace**.

```
1. mi_proyecto        al abrir la conversación (trae la norma de citas)
2. ver_capitulo       antes de preguntarle nada del capítulo;
                      lee `marco-teorico`, `analisis-datos-rstudio`
                      y `problema-y-objetivos` con `texto: true`
3. buscar_fuentes     al necesitar respaldo; la cita nace atada a
   / mis_fuentes      su clave de biblioteca, Zotero y Mendeley incluidos
4. guardar_capitulo   clave `discusion`, apenas el tesista lo dé por bueno
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

**TODA pregunta usa `ask_user_input_v0` con opciones tocables.** Campo `question` siempre presente. Máximo 3 preguntas por bloque.

## Frontera importante (lo que esta skill NO hace)

- **No redacta Resultados**. Eso lo hace Skill 7.
- **No incluye Recomendaciones**. Eso lo hace Skill 9, después de las Conclusiones.
- **No inventa antecedentes**. Si un hallazgo del tesista no tiene comparación clara con antecedentes con clave (del Cap II o de su biblioteca), la skill lo declara honestamente.
- **No fabrica coincidencias** que no existen. Si dos antecedentes contradicen, la skill explica la divergencia con honestidad académica. Ver `references/honestidad_academica.md`.
- **No discute hipótesis que no aparezcan en Resultados**. Si el tesista aporta una hipótesis que no aplicó pruebas, la skill no inventa una decisión.

## Cómo se activa

- El tesista llega con el Cap II y el capítulo de Resultados (Skill 7) guardados en su proyecto (o escritos fuera, y los pega).
- Pregunta por "discusión", "contraste con literatura", "limitaciones del estudio", "interpretar resultados".
- Reactiva la skill después de guardar el capítulo para ajustar párrafos específicos.

## Paso 1 — Verificar punto de partida

Pregunta interactiva (single_select):

- "Los trabajé con las Skills 1, 3 y 7 (léelos de mi proyecto)"
- "Pego manualmente los antecedentes y los hallazgos por objetivo"
- "Aún no tengo el capítulo de Resultados terminado"

Si tercera opción, deriva a Skill 7 y termina.

### Leer los capítulos del proyecto

El tesista no sube ni pega los capítulos que escribió con el método: la skill los lee con `ver_capitulo`, con `texto: true`:

- **Cap II**: `capitulo: marco-teorico`.
- **Resultados**: `capitulo: analisis-datos-rstudio`.
- **Cap I** (objetivos e hipótesis, en el orden en que se discuten): `capitulo: problema-y-objetivos`.

Cada respuesta trae una parte de hasta 24.000 caracteres y dice «parte N de M» y cuál pedir después. Se sigue pidiendo con `parte` (2, 3…) hasta la última: el Cap II casi siempre viene en varias partes, y discutir con la mitad de los antecedentes es discutir mal. Nunca se le pide el Word de un capítulo. Las claves exactas son las que muestra `mi_proyecto` o `listar_capitulos`. En el texto guardado las citas vienen como claves `[AR…]` (autor y año de cada una salen de `mis_fuentes`), las tablas en su bloque APA y las figuras con su rótulo.

**Solo si `ver_capitulo` dice que el capítulo no tiene texto guardado** (por ejemplo, porque el tesista lo escribió fuera de la plataforma), se le pide que lo pegue en el chat.

### Lectura sin repeticiones (P1 del patrón Skill 6)

No volver a pedir una parte que ya se leyó en esta conversación. Si el tesista pega un capítulo que ya se leyó del proyecto, NO releerlo: confirmar que ya está leído y seguir.

### Insistencia en ambos capítulos (P2 del patrón Skill 6)

Hacen falta los dos, el Cap II y Resultados. Si uno no tiene texto guardado y el tesista no lo pegó, pausar y pedirlo explícitamente. NO avanzar con uno solo.

### Si segunda opción, pide:

```
Datos clave que necesito:
- Título tentativo de la tesis
- Tesista, carrera, universidad
- Objetivo general
- Objetivos específicos (todos)
- Hipótesis (general y específicas, si las tiene)
- Diseño metodológico (transversal/longitudinal, descriptivo/
   correlacional/explicativo, no experimental/experimental)
- Población y tamaño muestral final
- Para cada objetivo específico:
   · Prueba estadística aplicada
   · Resultado numérico (r, ρ, t, F, etc.)
   · p-value
   · Tamaño del efecto (si aplica)
   · Decisión sobre la hipótesis (aceptada/rechazada)
- Lista de antecedentes del Cap II con sus hallazgos clave
```

Si primera opción, lee los capítulos completos del proyecto (o el texto que pegó el tesista) y extrae automáticamente: del Cap I, los objetivos y las hipótesis; del Cap II, los antecedentes con sus claves y hallazgos; de Resultados, los estadísticos, las tablas y la decisión sobre cada hipótesis, por objetivo.

### Validación previa antes de avanzar

- ¿Cada objetivo específico tiene su hallazgo numérico?
- ¿Cada hallazgo tiene su decisión sobre la hipótesis?
- ¿Hay antecedentes con clave (en el Cap II o en su biblioteca) que comparen con cada hallazgo?

Si falta algo crítico, pausar y pedir antes de redactar.

## Paso 2 — Confirmar alcance del capítulo

Pregunta interactiva (single_select):

- "Solo Discusión por objetivos (sin limitaciones ni futuras investigaciones)"
- "Discusión + Limitaciones del estudio"
- "Discusión + Limitaciones + Sugerencias para futuras investigaciones"
- "No estoy seguro, dame pros y contras"

Si cuarta opción, la skill explica:

```
- Discusión por objetivos: es OBLIGATORIA. Sin ella, el capítulo
   pierde su sentido.

- Limitaciones del estudio: OPCIONAL. Algunos asesores las
   exigen, otros las dejan como sub-sección de las Conclusiones.
   El reglamento de tu universidad puede decirlo. Si no estás
   seguro, inclúyelas (suman, no restan).

- Futuras investigaciones: OPCIONAL aquí. En la mayoría de
   tesis peruanas van DESPUÉS de las Conclusiones (Skill 9),
   no en la Discusión. Recomendado: dejarlas para Skill 9.

Recomendación default: Discusión por objetivos + Limitaciones.
```

## Paso 3 — Confirmar numeración del documento

Pregunta interactiva (single_select):

- "CAPÍTULO V — DISCUSIÓN (numeración tesis, después de IV Resultados — RECOMENDADO)"
- "CAPÍTULO VIII — DISCUSIÓN (si tu tesis numera los capítulos incluyendo los preliminares)"
- "Sin numerar, solo título 'DISCUSIÓN'"

Default recomendado: CAPÍTULO V — DISCUSIÓN.

## Paso 3.5 — Nivel académico y extensión (obligatorio antes de redactar)

La Discusión de una tesis de pregrado y la de un doctorado no se parecen ni en extensión ni en profundidad. Un doctorando que entrega la discusión de un bachiller recibe observación segura, y un bachiller que entrega la de un doctorado invierte semanas de más sin que nadie se lo pida.

Pregunta obligatoria con `ask_user_input_v0`:

```
¿Para qué nivel es tu tesis?

· Pregrado (bachiller, licenciatura o título profesional)
· Maestría
· Doctorado
· Te ayudo a decidirlo con ejemplos sencillos
```

### Qué cambia con el nivel

```
NIVEL       PÁRRAFO POR      QUÉ SE ESPERA DE LA DISCUSIÓN
            OBJETIVO
──────────  ───────────────  ─────────────────────────────────
Pregrado    200-300 palabras Contrastar cada hallazgo con 2 o 3
            (4 movimientos   antecedentes del Cap II, explicar
            completos)       el porqué en la población, señalar
                             la implicancia práctica.
                             Extensión total orientativa:
                             4 a 6 páginas.

Maestría    300-450 palabras Todo lo de pregrado, más:
                             contrastar con 3 a 5 antecedentes
                             por objetivo, discutir por qué
                             los estudios difieren entre sí
                             (no solo respecto del propio),
                             y vincular el hallazgo con la
                             teoría base del Cap II.
                             Extensión total: 8 a 12 páginas.

Doctorado   450-600 palabras Todo lo de maestría, más:
                             discutir qué aporta el hallazgo a
                             la TEORÍA, no solo a la práctica;
                             señalar qué supuesto del marco
                             teórico se confirma, se matiza o
                             se pone en cuestión; y ubicar el
                             estudio en el debate del campo.
                             Extensión total: 15 a 25 páginas.
```

**Regla dura**: estas cifras son orientativas. Si el reglamento de la universidad del tesista dice otra cosa, manda el reglamento. La skill lo pregunta:

```
· Usar la extensión sugerida para [nivel declarado]
· Mi reglamento pide otra extensión (te la digo)
· No sé qué pide mi reglamento, usá la sugerida
```

**Regla dura de calibración**: el nivel no cambia solo el largo, cambia **qué se discute**. Alargar un párrafo de pregrado hasta 500 palabras no lo convierte en discusión de doctorado: lo convierte en un párrafo de pregrado con relleno. Si el tesista es de doctorado, la skill debe incorporar el movimiento de aporte teórico; si es de pregrado, NO debe incorporarlo, porque le exige algo que su nivel no pide.

**Regla dura anti-relleno**: si un objetivo tiene un hallazgo simple y honesto, su párrafo puede ser más corto que el rango sugerido. Es preferible un párrafo de 200 palabras que dice algo, a uno de 450 que estira. La skill lo declara al tesista cuando pasa: "este objetivo quedó en [N] palabras porque el hallazgo no daba para más sin repetir; si tu reglamento exige una extensión mínima por sección, avisame y vemos qué se puede profundizar de verdad."

## Paso 4 — Redactar la Discusión por objetivos (todo de golpe)

La skill redacta UN párrafo por cada objetivo específico, siguiendo los **4 movimientos del método**. Antes, pasa el control de evidencia.

### Antes de redactar: `revisar_evidencia` sin capítulo (regla dura)

La Discusión es donde se contrasta lo encontrado con la literatura, y contrastarlo de memoria es como se cuelan autores que no dijeron eso: un antecedente del Cap II parafraseado sin fuente, o una afirmación estirada hasta decir otra cosa, pasa a la Discusión como si fuera un hallazgo publicado.

Por eso, antes de escribir el primer párrafo:

1. Se llama a `revisar_evidencia` **sin capítulo**, para repasar todo lo escrito, y se le reporta al tesista qué afirmaciones tienen fuente y cuáles no.
2. Las afirmaciones del Cap II sin fuente **no se usan para contrastar** hasta resolverlas: o se les busca respaldo con `buscar_fuentes` (con `tema` en inglés, `temaOriginal` en español y `pais`), o quedan con `[FALTA FUENTE]` y él sabe dónde.
3. Si para un hallazgo hace falta un antecedente que no está en el Cap II, se busca con `buscar_fuentes` o `mis_fuentes`, se le presenta diciendo de dónde viene, y solo con su permiso se añade con `anadir_a_mis_fuentes`. Se le avisa de que ese autor no estaba en su marco teórico.

`revisar_evidencia` dice si una afirmación tiene de dónde agarrarse, **no si la fuente dice lo que la frase le atribuye**: eso se lee en la ficha y el resumen de la fuente (`mis_fuentes`, `buscar_fuentes`) antes de usarla para contrastar.

**Regla dura**: en la Discusión solo se contrasta con autores que tienen clave `[AR…]` (del Cap II o de su biblioteca), y solo por lo que esa fuente dice. Un autor sin clave no entra.

### Los 4 movimientos obligatorios

1. **Recordar el hallazgo** sin repetir tablas. Mencionar el estadístico clave y la decisión sobre la hipótesis. Ejemplo: "El presente estudio halló una correlación positiva moderada entre V1 y V2 (ρ = .42, p < .01), lo que permitió aceptar la hipótesis H1."

2. **Comparar con la literatura con clave** (primero la del Cap II; si falta, la de su biblioteca). Identificar 1-3 antecedentes pertinentes y declarar si los resultados coinciden o difieren. Ejemplo: "Este resultado coincide con lo reportado por Paiva et al. [AR…:n], quienes encontraron asociación similar en estudiantes de secundaria portugueses (ρ = .38). En cambio, se distancia de los hallazgos de Vereau Amaya et al. [AR…:n], quienes reportaron una correlación negativa en universitarios trujillanos (ρ = -.21)."

3. **Interpretar el porqué** en la población del tesista. Proponer una explicación contextualizada. Ejemplo: "La divergencia con Vereau Amaya et al. [AR…:n] puede atribuirse al nivel educativo de la población: los estudiantes de secundaria estarían usando IA como apoyo exploratorio sin reemplazar su razonamiento, mientras los universitarios estudiados por Vereau Amaya podrían estar en una fase de mayor dependencia."

4. **Señalar la implicancia**. Qué aporta el hallazgo, qué consecuencia práctica tiene. Ejemplo: "Estos hallazgos sugieren la pertinencia de incorporar el desarrollo del pensamiento crítico como contenido transversal en la formación secundaria, particularmente en contextos donde el uso de IA generativa es habitual."

### Estructura de párrafo

Cada párrafo: 6 a 10 oraciones, prosa continua, justificado, sangría primera línea.

### Cuándo NO se puede aplicar el movimiento 2

Si ni el Cap II ni la biblioteca del tesista tienen antecedentes con clave que comparen con un hallazgo específico, la skill lo declara con honestidad:

> "No se encontraron antecedentes directamente comparables a este hallazgo en la literatura revisada. Esta dimensión del fenómeno aparece poco estudiada en el contexto peruano, lo cual constituye una oportunidad para futuras investigaciones."

NO citar autores sin clave ni de memoria. NO atribuir hallazgos a antecedentes que no los reporten.

### Si el hallazgo CONTRADICE la literatura

Tres caminos honestos (ver `references/honestidad_academica.md`):

1. **Atribuir al contexto**: diferencias de población, sector, momento histórico.
2. **Atribuir a la metodología**: diferentes instrumentos, tamaño muestral, diseño.
3. **Reconocer limitación**: posibles sesgos del estudio actual.

NO ocultar los resultados que contradicen la hipótesis. NO forzar interpretaciones para que coincidan.

Ver `references/cuatro_movimientos.md` para ejemplos detallados.

## Paso 5 — Limitaciones del estudio (opcional)

Solo si el tesista lo eligió en el Paso 2.

### Cómo opera la skill

La skill identifica automáticamente las limitaciones aplicables al diseño del tesista:

| Característica del estudio | Limitación correspondiente |
|---------------------------|---------------------------|
| Diseño transversal | No permite establecer causalidad ni cambios en el tiempo |
| Auto-reporte (cuestionario) | Riesgo de sesgo de deseabilidad social y memoria |
| Muestra de una sola institución | Generalización limitada a contextos similares |
| Tamaño muestral pequeño (n < 100) | Limita la potencia estadística |
| Sin grupo control | No permite atribuir efectos a una intervención |
| Sin variables moderadoras consideradas | Pueden existir factores no controlados |
| Sin saturación cualitativa documentada | (Para cuali) Posible información no recogida |
| Acceso restringido a datos | Limitación operativa |

Para cada limitación aplicable, la skill redacta UN párrafo siguiendo la fórmula documentada en `references/limitaciones.md`:

> "El presente estudio presenta algunas limitaciones que conviene reconocer. En primer lugar, [limitación 1 + por qué]. En segundo lugar, [limitación 2 + por qué]. Finalmente, [limitación 3 + por qué]."

### Tono

Mantener voz académica, NO disculparse. Las limitaciones reconocidas FORTALECEN la tesis (Cap 8.12).

Ver `references/limitaciones.md`.

## Paso 5.5 — Redacción sin moldes y estilo de citación (antes de guardar)

### Patrones de modelo que se evitan al redactar

La Discusión es prosa pura, sin tablas ni bullets, así que está más expuesta que ningún otro capítulo a los tics de redacción de modelo. El catálogo completo, con ejemplos y falsos positivos, está en `references/parafraseo.md` de la Skill 3 (Marco Teórico). Resumen aplicado a este capítulo:

- **P0 (paralelismo de plantilla)**: el riesgo número uno acá. Si hay cuatro objetivos, la tentación es escribir cuatro párrafos con la misma arquitectura: hallazgo, "estos resultados coinciden con", "esto puede explicarse porque", "lo cual implica que". Cuatro párrafos gemelos delatan el capítulo de inmediato. Cada objetivo debe abrirse distinto y repartir el peso distinto: uno puede dedicar la mitad a la comparación y otro a la interpretación, según dónde esté lo interesante.
- **P0b (tics de reescritura)**: no aperturas sentenciosas que no se retoman, no cierres que anuncian importancia ("Este hallazgo resulta particularmente significativo porque..."), no aposiciones que meten al autor en el medio ("El estudio de Apellido [AR…:n], retomado por Apellido2 [AR…:n], encontró...").
- **P0c (frase-etiqueta)**: no abrir con una oración que solo anuncia ("Este resultado admite dos lecturas.").
- **P1 (inflar importancia)**: cero "estos hallazgos constituyen un aporte fundamental al campo", "marcan un antes y un después". La discusión de una tesis aporta a su población y su contexto; decir más es falso.
- **P2 (gerundios colgados)**: eliminar "coincidiendo con lo hallado por", "evidenciando la relación esperada", "confirmando lo planteado". Casi siempre repiten en gerundio lo que la oración ya dijo.
- **P3 (lenguaje promocional)**: cero "análisis integral", "discusión exhaustiva", "aporte invaluable". "Robusto" solo en su sentido técnico estadístico.
- **P4 (atribución vaga)**: **crítico en este capítulo**. Cero "diversos autores coinciden", "la literatura sugiere", "numerosos estudios han demostrado". En la Discusión cada comparación se hace con un autor concreto que tiene clave (del Capítulo II o de su biblioteca). Si no hay un autor que sostenga la afirmación, la afirmación se elimina.
- **P5 (evitar verbo ser)**: reducir "constituye una coincidencia con", "representa una divergencia respecto de".
- **P6 (nominalización en cadena)**: convertir "la existencia de una coincidencia entre los resultados obtenidos y los hallazgos reportados" en "los resultados coinciden con lo que reportó".
- **P7 (regla de tres ornamental)**: si tres verbos dicen lo mismo ("coincide, concuerda y converge con"), dejar UNO.
- **P8 (rotación de sinónimos técnicos)**: "correlación" no se rota por "asociación" ni "vínculo". "Significativo" no se rota por "relevante": significan cosas distintas.
- **P9 (rayas largas — o –)**: cero rayas en el texto final.
- **P10 (contrastes fabricados)**: cero "sin embargo, lo cierto es que", "más allá de los números", "la verdadera pregunta es". La Discusión sí tiene contrastes reales (los que existen entre estudios); no hacen falta los fabricados.
- **P11 (conectores en exceso)**: máximo 2 por página. Cero "cabe destacar", "es importante mencionar", "en tal sentido" al inicio de párrafo.
- **P12 (cierres optimistas)**: cero "estos resultados abren un camino prometedor para futuras investigaciones". Las líneas futuras van en la Skill 9, no acá.
- **P13 (restos chatbot)**: cero "a continuación se discute", "en resumen".
- **P14 (formato)**: cero negritas dentro de los párrafos. La Discusión va en prosa continua sin resaltados.

### Rotación de abridores por objetivo (anti-clonación)

La skill NO abre todos los párrafos igual. Rota entre variantes, y dentro del mismo documento no repite ninguna:

**Movimiento 1, recordar el hallazgo** (elegir 1 por objetivo):
- "El primer objetivo específico buscaba [...]. Los datos mostraron que [...]"
- "Respecto de [variable o dimensión], el análisis arrojó [...]"
- "En cuanto a [objetivo], se obtuvo [...]"
- "El resultado para [objetivo] fue [...]"

**Movimiento 2, comparar con la literatura** (elegir 1):
- "Este resultado coincide con lo reportado por [Autor] [AR…:n], quien [...]"
- "[Autor] [AR…:n] encontró un patrón similar en [...]"
- "La dirección de este hallazgo se aparta de lo que reportó [Autor] [AR…:n] [...]"
- "A diferencia de [Autor] [AR…:n], acá [...]"

**Movimiento 3, interpretar el porqué** (elegir 1):
- "Una explicación posible está en [...]"
- "Esto puede deberse a que [...]"
- "El contexto de [población] ayuda a entender por qué [...]"
- "La diferencia se explica, al menos en parte, por [...]"

**Movimiento 4, implicancia** (elegir 1):
- "Para [institución o sector], esto significa que [...]"
- "En términos prácticos, el hallazgo sugiere [...]"
- "La consecuencia para [población] es [...]"

### Sin auditorías de estilo en el chat

La skill escribe con estas reglas y con las que ya trae `redactar` (sin moldes, con la voz del tesista). No imprime conteos de oraciones, dispersión, largo de palabra ni checks de patrones: al guardar, `guardar_capitulo` devuelve los AVISOS DE REDACCIÓN que calcula el servidor (vocabulario de modelo, rayas, párrafos que abren igual, muletillas repetidas) y esos párrafos se corrigen con `reescribir_parrafos` (capítulo `discusion`).

### Norma de citas

La Discusión es, después del Marco Teórico, el capítulo con más citas, y casi todas son de fuentes que ya aparecieron en el Capítulo II: con claves, cada una sale igual que allí, con el mismo número en las normas numéricas. Las citas van con la **clave de cada fuente entre corchetes**, nunca escritas a mano: `[AR97D22F86]` para una cita normal, `[AR97D22F86:n]` detrás del nombre si el autor va en la frase («Hernández-Sampieri [AR97D22F86:n] sostiene…»), `[AR97D22F86:p. 45]` con página, y varias seguidas (`[AR…][AR…]`) para una cita con varias fuentes. Las claves salen de `mis_fuentes`, `buscar_fuentes` o `anadir_a_mis_fuentes`.

Al descargar el Word, el servidor de Acosta escribe cada cita y la lista de referencias en la norma del proyecto, en el orden que esa norma pide y con la numeración continua de toda la tesis en Vancouver e IEEE. Por eso **no se convierte, no se numera y no se arma a mano la lista de referencias**: la norma es una sola para toda la tesis, así que los capítulos coinciden solos, y si el asesor pide otra más adelante se cambia sin reescribir ningún capítulo.

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

Antes de la revisión de contenido, comprobá además que ninguna cita esté escrita a mano, que toda afirmación con fuente lleve su clave y que no haya una lista de referencias armada a mano. **Regla dura**: nunca inventar una clave ni una fuente. Si una fuente que el tesista trajo al chat (por ejemplo, de su export de Scopus) no tiene clave, pedile permiso y añadila con `anadir_a_mis_fuentes` por su DOI; si no tiene DOI, que la suba en «Mis fuentes» de su perfil o la tenga en su Zotero o su Mendeley. Lo que quede sin respaldo se marca `[FALTA FUENTE]` y se le avisa. Ya guardado, `revisar_evidencia` con el capítulo `discusion` lo comprueba (Paso 6).

### Revisión de contenido (obligatoria antes de guardar el capítulo)

```
REVISIÓN DE LA DISCUSIÓN

EXTENSIÓN (según nivel declarado: [pregrado/maestría/doctorado]):
   Objetivo 1: [N] palabras → rango [X-Y] → [OK / CORTO / LARGO]
   Objetivo 2: [N] palabras → ...
   (una línea por objetivo)
   Total del capítulo: [N] palabras ≈ [N] páginas

CITAS:
   Total de citas: [N]
   revisar_evidencia sin capítulo antes de redactar: SÍ / NO
   Todas con autor concreto y clave (Cap II o biblioteca): SÍ / NO
   Antecedentes que no estaban en el Cap II: [N] (avisados)
   Atribuciones vagas detectadas ("diversos autores"): [N]
      (deben ser 0)
   Citas con clave [AR…]: [N]; escritas a mano: 0;
   [FALTA FUENTE]: [N]
   Norma del proyecto: [X] (la escribe el servidor)

Estado: OK PARA GUARDAR / RE-REDACTAR
```

**Regla dura**: si hay atribuciones vagas, citas sin clave o un objetivo fuera de rango, la skill re-redacta antes de guardar el capítulo.

**Regla dura anti-autocertificación**: no escribir "todo correcto" sin haber contado las palabras por objetivo y verificado las citas una por una.

## Paso 6 — Guardar el capítulo y entregar el Word

**Se guarda automáticamente** al terminar el Paso 5 (o Paso 4 si no hay limitaciones) y la revisión de contenido del Paso 5.5, sin pedir confirmación adicional. Si el tesista pide ver el capítulo completo antes, se le muestra en la conversación y se guarda cuando lo apruebe.

### Estructura del capítulo (el texto que se guarda)

**REGLA CRÍTICA**: el capítulo se redacta como PROSA CONTINUA sin subtítulos numerados por defecto. La organización por objetivos se mantiene mediante conectores discursivos que insertan el objetivo dentro del propio párrafo. Subtítulos solo si el tesista los solicita explícitamente.

Lo que se guarda es el texto en Markdown, con los párrafos separados por una línea en blanco. **Sin título del capítulo ni datos personales**: el Word del servidor escribe el título de cada capítulo guardado y la portada. El texto empieza en el párrafo introductorio y no lleva sección «Referencias» al final.

```
[Párrafo introductorio de 3-4 oraciones que anuncia que se
discutirán los hallazgos en el orden de los objetivos
específicos planteados en el Capítulo I, para concluir con
la discusión del objetivo general.]

[Párrafo del objetivo específico 1, que INSERTA el objetivo
en el primer enunciado del párrafo, no como subtítulo.
Ejemplos de aperturas válidas:
   - "Respecto al primer objetivo específico, orientado a
      determinar la relación entre X y Y, los resultados
      mostraron..."
   - "En cuanto al primer objetivo, que buscó determinar..."
   - "Al examinar el primer objetivo específico, dirigido a
      determinar..."
Continúa con los 4 movimientos del método.]

[Párrafo del objetivo específico 2, con apertura distinta:
   - "En relación con el segundo objetivo específico..."
   - "Por su parte, el segundo objetivo específico..."
   - "El segundo objetivo específico, que buscó determinar..."
Continúa con los 4 movimientos.]

[Párrafo del objetivo específico N, con apertura distinta
para evitar repetición monótona de conectores.]

[Párrafo del objetivo general, con apertura que articula los
hallazgos parciales:
   - "Considerando los hallazgos parciales discutidos, el
      objetivo general del estudio, orientado a..."
   - "La lectura integrada de los hallazgos por objetivo
      específico permite responder al objetivo general,
      que buscó..."
Continúa con los 4 movimientos en clave de síntesis.]

[Párrafo de Limitaciones — solo si aplica.
   Apertura: "El presente estudio presenta algunas limitaciones
   que conviene reconocer. En primer lugar..."]
```

### Conectores discursivos para evitar repetición

La skill mantiene una lista interna de aperturas variadas para los párrafos por objetivo, de modo que ningún párrafo empiece igual. Patrones válidos:

- "Respecto al / En cuanto al / En relación con el / Por su parte, el / Al examinar el / Sobre el [N-ésimo] objetivo específico..."
- "El [N-ésimo] objetivo específico se orientó a / buscó determinar / tuvo como propósito..."

### Excepción: el tesista pide subtítulos

Si durante el Paso 2 el tesista solicita explícitamente subtítulos numerados (porque su universidad o asesor los exige), la skill los agrega con formato APA 7 nivel 2:

- `## 5.1 Discusión del objetivo específico 1` — y debajo, el párrafo con los 4 movimientos.
- `## 5.2 Discusión del objetivo específico 2` — igual, con otra apertura.
- Una sección por objetivo, y la del objetivo general al final.

En ese caso, las aperturas de párrafo pueden simplificarse, pero los conectores discursivos siguen siendo recomendados para no leer "telegráfico".

### Pregunta explícita al tesista

Antes del Paso 6, la skill incluye una pregunta interactiva (single_select) para confirmar:

- "Prosa continua sin subtítulos numerados (RECOMENDADO; texto académico más fluido)"
- "Con subtítulos numerados (5.1, 5.2, ...) si tu universidad lo exige"

### Reglas del texto

- Sin bullets, sin tablas, sin listas dentro de los párrafos.
- **Sin subtítulos numerados por defecto**. El cambio de objetivo se marca solo con cambio de párrafo y conectores discursivos al inicio de cada uno. Subtítulos solo si el tesista los solicitó en el Paso 2; en ese caso van con `##`.
- Cada cita con su clave dentro del párrafo: `[AR…]` detrás de la idea, o `Apellido [AR…:n] reportó...` si el autor va en la frase (ver «Norma de citas» en el Paso 5.5). Nunca la cita escrita a mano (apellido y año entre paréntesis, o un número) en el texto que se guarda.

### Referencias: las arma el servidor

El capítulo no lleva lista de referencias. Casi todas las fuentes de la Discusión ya están citadas en el Capítulo II: en la **única lista** que arma el Word del servidor para toda la tesis aparecen una sola vez, en la norma del proyecto, y nunca se unen a mano. Si una ficha tiene datos mal o incompletos, se corrige en el Zotero o el Mendeley del tesista, o en «Mis fuentes», y la próxima descarga sale corregida.

### Formato de página

Lo aplica el Word del servidor: la plantilla de la facultad si el tesista la subió; si no, el formato por defecto de la plataforma. No se configura a mano. Si el reglamento de su universidad pide algo distinto y no subió la plantilla, decíselo: puede subirla o ajustar el documento en Word.

### Guardar y entregar

**Regla dura** (ver la regla transversal): la skill no genera ningún archivo ni escribe una lista de referencias. El Word y la bibliografía los arma el servidor; uno hecho a mano no llevaría la norma del proyecto ni coincidiría con las fichas de las fuentes.

1. **Guardá el capítulo** con `guardar_capitulo`, clave `discusion` (la que muestra `listar_capitulos`). Cada llamada admite hasta 30.000 caracteres. Si el capítulo es más largo, mandalo por partes, cortando entre párrafos: la primera parte sin `anadir` y las siguientes con `anadir: true`. Si más adelante el tesista corrige el capítulo entero, se manda completo otra vez, sin `anadir`. Si la respuesta trae AVISOS DE REDACCIÓN, corregí esos párrafos con `reescribir_parrafos` antes de dar el enlace.
2. **Registrá lo acordado** con `guardar_avance` (capítulo `discusion`): un resumen de dos o tres frases con lo que quedó decidido (alcance, limitaciones incluidas, coincidencias y divergencias principales). Marcá `estado: LISTO` solo si el tesista dice que da el capítulo por bueno; si no, `EN_CURSO`.
3. **Revisá la evidencia del capítulo** con `revisar_evidencia`, `capitulo: discusion`. Reportale al tesista qué comparaciones quedaron sin fuente antes de darle el enlace. Si algo se corrige, se vuelve a guardar el capítulo completo, sin `anadir`.
4. **Dale el enlace** con `enlace_del_word` y explicáselo:

```
Tu capítulo de Discusión quedó guardado. Acá tenés el
enlace para descargar tu tesis en Word: [enlace]

El Word lo arma el servidor con todos los capítulos que
tenés guardados, en orden, con portada e índice. Las citas
y la lista de referencias salen en la norma de tu proyecto
([norma]), en una sola lista para toda la tesis. El enlace
vence a la media hora; si ya pasó, pedime otro.
```

Si un guardado falla, se le dice con esa palabra: no se guardó.

## Paso 7 — Cierre y validación humana

Checklist final al tesista:

```
- [ ] Descarga el Word y llévalo a tu asesor antes de avanzar a Skill 9
       (Conclusiones y Abstract).
- [ ] Lee tu Discusión en voz alta. Si suena a "Claude",
       reescribe con tu voz: cambia conectores, ajusta
       expresiones repetidas, dale tono propio.
- [ ] Verifica que cada autor citado en la Discusión diga
       de verdad lo que se le atribuye. Si alguno no estaba
       en el Cap II (Marco Teórico), valora con tu asesor
       añadirlo también ahí.
- [ ] Confirma que cada hallazgo discutido coincide con el
       reporte del capítulo de Resultados (Skill 7). No deben
       haber discrepancias.
- [ ] Si tu asesor te pide reorganizar (por hipótesis en lugar
       de objetivos, o incluir recomendaciones aquí), reactiva
       esta skill.
```

Cuando el asesor apruebe:

> Reactiva la **Skill 9 (Conclusiones y Abstract)** para cerrar tu tesis con las conclusiones por objetivo, las recomendaciones para acción y el abstract final.

## Errores comunes que la skill previene

Ver `references/errores_comunes.md` para detalles. Los 8 errores documentados:

1. Mezclar resultados con discusión.
2. Repetir tablas que ya estaban en Resultados.
3. Discutir hallazgos que no aparecen en Resultados (inventar o exagerar).
4. No comparar con antecedentes (discusión sin literatura = opinión).
5. Usar voz personal ("yo creo", "pienso que").
6. Citar autores sin clave o por lo que no dijeron.
7. Olvidar la honestidad académica al reportar divergencias.
8. Pegar tablas de R/SPSS sin formatear APA 7 (esto NO aplica aquí porque no usamos tablas).

## Archivos de referencia

- `references/cuatro_movimientos.md` — Detalle de los 4 movimientos con ejemplos por tipo de prueba (Pearson, Spearman, t-Student, ANOVA, Chi², regresión).
- `references/limitaciones.md` — Mapeo de diseños metodológicos a limitaciones típicas + plantillas de redacción.
- `references/honestidad_academica.md` — Cómo manejar hallazgos que contradicen la literatura, los tres caminos del Cap 8.11.
- `references/apa7_discusion.md` — Cómo se marcan las citas con clave en los párrafos de discusión.
- `references/integracion_zotero.md` — Biblioteca, marcas de cita, norma y herramientas de fuentes.
- `references/errores_comunes.md` — Los 8 errores del Cap 8.14 y cómo prevenirlos.
