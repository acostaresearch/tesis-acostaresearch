# Casos de IA: la historia detrás de la Ruta 0 %

Lo que estaba en el Paso 3A de SKILL.md hasta el 18-oct-2026, tal cual. Es historia y consulta:
lo que manda es `ruta-ia-cero.md`. Si algo de aquí contradice la ruta, manda la ruta.

## Resultado por trabajo (una línea cada uno al terminar)

- 07 Josué: llegó en «*%» → 0 % en la ronda 1 (toda la prosa, receta).
- 08 Diana: llegó en «*%» → 0 % en la ronda 1 (receta).
- 09 Samuel: 42 % → 0 % en la ronda 1 (solo lo marcado).
- 10 Roy: 76 % → «*%» en ocho rondas → 0 % con el conector y dos pasadas sobre el documento entero. Causa: párrafos limpios reescritos, primer reporte perdido.
- 11 Claudia y Flor: similitud + toda la prosa → 0 % en la ronda 1.
- 12 Milagros: 78 % → «*%» → 0 % en la ronda 2 (dos pasadas sobre el documento entero).
- 13 Pamela: 27 % → «*%» en unas quince rondas → 0 % el 19-oct partiendo el documento para diagnosticar: cada apartado daba 0 % solo; mitades → marco teórico + metodología → el marco solo dio 41 % con resaltado. Causa real: el marco recorría los componentes de COSO uno por uno con enumeraciones de 3-4 acciones paralelas (¶88-90). Dos rondas sobre esos tres párrafos (41 → 25 → 0 %) y el documento entero salió en 0 %.
- 14 Parte I: «*%» tras dos rondas. Hipótesis: la plantilla de la segunda mitad.
- Eduardo Sime (asesoría): «*%» ocho rondas. Causa: párrafos limpios reescritos; notas, celdas y párrafos cortos marcados sin tocar.
- Jimena Mayhua (asesoría): llegó en «*%» → «*%» en las rondas 1 y 2 (reescritas una encima de la otra) → 0 % en la ronda 3: vuelta al original, toda la prosa con arquitectura distinta de la ronda fallida (se dio a los agentes como contraejemplo), enunciados específicos acortados y dos pasadas sobre el documento entero.
- Silvia Taype (asesoría 21, avance con citas de Word, 19-oct): llegó en «*%» con similitud 26 % → IA 0 % y similitud 20 % en la ronda 1 (toda la prosa reescrita sobre el texto fuente marcado y rearmada con el armador, 4 agentes + pasada completa + lectura). Ronda 2 solo de similitud: cirugía mínima de 30 tramos en 28 párrafos para no tocar lo que ya daba 0 %.
- Luis Huete (asesoría 15, proyecto UCV de maestría escrito por nosotros desde el texto fuente, 20-oct): llegó en «*%» con similitud 11 % → IA 0 % y similitud 8 % en la ronda 1 (44 párrafos de toda la prosa con 4 agentes sobre el texto fuente, problema y objetivos intactos, una pasada que rompió 3 moldes y partió las oraciones de más de 60 palabras, y una segunda de verificación; rearmado con el armador). El ritmo quedó largo (media de 39 palabras) y dio 0 % igual.
- Wilmer (asesoría, TA nivel 1 UCV escrito por nosotros desde un texto marcado, 21-oct): llegó en «*%» con similitud 12 % → IA 0 % y similitud 10 % en la ronda 1. Toda la prosa (32 párrafos) en 4 agentes con un verificador de citas y cifras, una pasada de moldes entre tramos, otra de fidelidad contra el texto previo y las fuentes, y lectura línea por línea. Se editó el texto fuente y se rearmó el Word, no el Word con aplicar.py.

- Milagros Leon (asesoría 26, proyecto UCV Huaraz con introducción redactada por nosotros, 21-oct): Turnitin 1 «*%» con similitud 39 % → ronda 1 (5 agentes) similitud 9 % pero «*%»; ronda 2 (plantilla de antecedentes y conceptos) «*%». Diagnóstico: las 5 secciones solas y la mitad 1 daban 0 %, la mitad 2 (metodología + administrativos) «*%». Los administrativos solos no llegan a 300 palabras de prosa y no se miden, pero junto a la metodología sí. Partiendo hasta trozos de unas 500 palabras salió M2b con 32 % y marcas: el plan de análisis (procesamiento, Spearman) y la ética. La primera reescritura «de manual» siguió marcada (33 %); pasó al escribirla anclada en el caso (los cuestionarios impresos, esta ferretería, qué dice el signo y el valor). → IA 0 % y similitud 10 % en la ronda 5, sin la lista de referencias.

## Paso 3A: humanizar (IA)

```
python <skill>/scripts/marcado_ia.py <reporte.pdf> <word.docx> <scratchpad>/marcado.json
```

Lista los párrafos con algo resaltado y, dentro de cada uno, qué oraciones están marcadas. Si
avisa que casi nada del resaltado aparece en el Word, el Word no es el analizado: volver al
paso 2.

Después se carga la skill `humanizador-academico` y se reescribe con sus reglas de redacción y
de fidelidad, con estas diferencias, que son decisiones del usuario:

- **Solo lo marcado.** Un párrafo marcado en parte se reescribe en esa parte. Lo limpio no se
  toca aunque parezca mejorable: reescribirlo es la forma más fácil de que empiece a marcarse.
- **Sin bloques ni aprobación.** Las fichas y la relectura de la propia salida se hacen, pero
  no se muestran. Los tres intentos por párrafo ocurren en silencio.
- **Una sola pasada a fondo también aquí**: se reescribe todo lo marcado con el cambio de orden
  desde el primer intento, sin dejar párrafos «casi iguales» para una segunda ronda.
- **Lo que ha funcionado en sus trabajos**: reescribir desde la idea, cambiar el orden de la
  información y fundir oraciones con un conector que diga una relación que sí existe, de modo
  que queden de largo desigual. Un artículo pasó así de 25 % a 0 % en una ronda, y una tesis de
  77 % a 20 %.
- **Lo que siguió marcado** fue siempre lo que quedó cerca del original: las mismas
  enumeraciones en el mismo orden, la misma secuencia de ideas, oraciones partidas y parejas.
  La Metodología es donde más pasa, porque invita a conservar la fórmula. Cambiar sinónimos no
  mueve nada.

**La voz del usuario.** Antes de reescribir se lee `<skill>/voz.md`, donde están las frases y
giros que él usa al redactar. Sirven de muestra de voz para el humanizador, con las reglas de
uso que el propio archivo trae. Cuando el usuario dé frases nuevas, o corrija una reescritura
con sus palabras, se añaden a ese archivo en el momento.

Ronda 2 en adelante: se reescribe solo lo que el reporte nuevo sigue marcando, y con un
planteamiento distinto del intento anterior, no con un retoque encima.

### Cuando el reporte de IA da «*%» (y siempre se quiere 0 %)

El usuario necesita siempre 0 %, así que esto no se pregunta: se hace. «*%» viene sin nada resaltado, así que no hay marcas que seguir: se humaniza toda la prosa del
cuerpo (párrafos de 25 palabras o más que no sean título ni rótulo fijo), con el catálogo del
`humanizador-academico` y sus `cobertura.py` y `ficha.py`, y se dejan sin tocar los párrafos
que ya salen limpios. **Lo que el primer reporte con marcas dejó sin marcar en el Word de `actual`
es texto que pasa: no se reescribe nunca**, ni en esta pasada ni en las siguientes; se cruza ese
reporte con `marcado_ia.py` y esos párrafos se excluyen del encargo (10-Roy, 14-oct-2026: la
metodología, los términos y un antecedente estaban limpios en el original, se humanizaron en la
ronda 2 y el documento quedó cinco rondas en «*%»; en la 6 se devolvieron al texto original, con
su formato). Si el reporte se mandó a la Papelera, se recupera de ahí. Cuando varias rondas encima de
reescrituras no bajan de «*%», se empieza de cero en las partes que siguen en «*%» (no en las que
ya dieron 0 %): se devuelven al texto de `actual` y se reescriben una sola vez solo las oraciones
marcadas en el primer reporte, con `viejo` = la oración exacta (10-Roy, ronda 7). Además de `voz.md` se lee `references/muestra-ia-cero.txt`, la prosa de
un proyecto del usuario que dio 0 %: arranca desde el hecho o el estudio, funde con «y»,
«pero», «ya que», «de modo que», y no cierra anunciando importancia. Un documento largo se
reparte en cuatro tramos de palabras parecidas, uno por agente, cada uno con su
`cambios_hN.json` probado con `aplicar.py`. Si antes se bajó similitud, la humanización va
sobre esa salida y al terminar se vuelve a correr el marcado de similitud: en la tesis de 07
devolvió unas 70 palabras coincidentes de 1 550 ganadas, que se retocaron a mano.

Si el usuario dice que el reporte dio «*%» y no trae el PDF (ese reporte no marca nada, así
que no hace falta), se trabaja igual con su palabra. Y si no pidió similitud, se salta esa
pasada y se humaniza sobre el Word de `actual`; al final se cruza con el reporte de similitud
que haya, antes y después, solo para comprobar que no subieron las coincidencias.

**Antes de otra pasada sobre la prosa, mirar el residuo protegido** (lección de 10-Roy, 14-oct-2026: tres rondas de prosa y seguía en «*%»). Se cruza el `marcado.json` de la ronda 1 con todos los `cambios_*.json` y se suman las palabras que Turnitin marcó y que nunca se reescribieron porque la skill las protege: título, pregunta del problema, objetivos, subtítulos, referencias. En Roy eran 334 palabras, el 3,8 % de lo subido, y eso solo basta para «*%». Entonces, con la meta de 0 %:

- Los **subtítulos propios del autor** (no los normados como «Marco teórico») se reescriben más llanos: «Fundamento técnico: persistencia diferenciada y orden de volatilidad» → «Por qué unos datos duran más que otros».
- La **pregunta del problema y los objetivos marcados** se reformulan lo mínimo, con las mismas variables, el mismo verbo de objetivo y el mismo alcance («Determinar de qué manera… durante el periodo 2025» → «Determinar cómo incide… en 2025»), y se le dice al usuario que el asesor tiene que estar de acuerdo. Si se repiten en la matriz o en una tabla, se cambian igual allí.
- El **título** no se toca (está inscrito), y se le avisa.
- **Problemas, objetivos e hipótesis en lista de tres gemelos** («1. ¿De qué manera X se relaciona con D1…? 2. ¿De qué manera X se relaciona con D2…?») y los **H₀/H₁ de cada contraste** son residuo aunque se hayan reformulado: el original de 13-Pamela los tenía marcados enteros, y nueve rondas los conservaron como lista (18-oct-2026). Se deja el enunciado general entero y los específicos pasan a una oración que nombra las tres dimensiones («Después esa pregunta se llevó a cada dimensión…»); los H₀/H₁ quedan cortos y llanos («entre ambas variables no hay una relación significativa»). El asesor tiene que aprobarlo.
- **Lo que la skill reescribió fuera del cuerpo** (anexos, instrucciones del instrumento) siendo texto que el primer reporte dejó limpio vuelve al original con cirugía de tramos.
- Las **notas y fuentes de tabla, los párrafos de menos de 25 palabras y el texto de las celdas** tampoco entran nunca en el reparto por tramos. Si el primer reporte los marcó, se reescriben a mano conservando el rótulo «Nota.» o «Fuente.» con `viejo`, y las celdas con frases de plantilla («El ítem está redactado de manera…») se rehacen con python-docx (Eduardo Sime, 17-oct-2026: parte 2 en «*%» tras seis rondas; quedaban la Nota y la Fuente de la Tabla 11, dos párrafos cortos, un subtítulo y los criterios de la Tabla 14).
- Las **referencias** no se pueden reescribir. Se deja en `Subir a Turnitin` una copia de prueba sin referencias: si esa da 0 % y la completa no, el resto viene de las referencias y se le explica.
- La prosa solo se vuelve a reescribir si sus números están lejos de los textos que dieron 0 % (`muestra-ia-cero.txt`, 07, 09); si ya se parecen, otra pasada no mueve nada.

**Si después de una pasada por tramos sigue en «*%», NO se parte: se hacen dos pasadas del `humanizador-academico` sobre el documento ENTERO** (lo pidió el 15-oct-2026, con Renzo Cruz: «No por partes no, quita los patrones IA y encárgate de no generar más»). Un agente lee todo el cuerpo de una vez (volcado a un .txt con números de párrafo), lista los patrones que se repiten entre secciones (conectores, moldes, cierres, «esta tesis», «Como/Con» al abrir) y los quita; luego un segundo agente nuevo verifica todo otra vez, quita lo que quede y lo que metió la primera pasada («porque», «Para» al abrir, «la misma X que») sin reescribir lo limpio. El encargo de las dos está en el scratchpad de esa sesión como modelo: entrada, JSON y prueba con `aplicar.py`, y después se comprueba que la similitud no subió. Lo de abajo sobre partir queda solo como historia; no se propone.

**Si tras las dos pasadas sigue en «*%», medir contra la parte que dio 0 %** (Eduardo Sime, 17-oct-2026): la parte 1 dio 0 % y la
parte 2 seguía en «*%» incluso sin referencias. `medir.py` del humanizador sobre la prosa de las dos mostró que la pasada de
verificación, al quitar conectores repetidos, había bajado las oraciones enlazadas de 15 % a 8 % (la parte 1 tenía 20 %): «fichas
sueltas». Se hizo una pasada solo de enlaces reales y variados (ningún conector más de 4 o 5 veces) hasta igualar la parte en 0 %.
Al quitar conectores repetidos hay que mirar siempre que el % de enlazadas no caiga. La subida de similitud de 5 % a 22 % en la
misma tarea era autocoincidencia con las entregas anteriores; en otra tarea dio 5 %. Tras cuatro rondas en «*%» apareció la causa de fondo: 72 de los 90 párrafos que el primer reporte dejó limpios se habían reescrito en las rondas 2 a 4. **Antes de cualquier ronda 3 o posterior se cruza el primer reporte con marcas contra el Word de esa ronda (`borrar\…(antes de humanizar)`) y se compara cada párrafo no marcado con el actual (difflib); los que cambiaron se devuelven a su texto copiando el `w:p` entero**, salvo los que traigan una corrección de contenido posterior (se buscan cifras, citas y palabras clave que cambien entre versiones y se leen esos). Cuando después pide «humanizar a 0 % sin reporte», la pasada de agentes es de **verificación** sobre los párrafos ya reescritos (los que el primer reporte marcó), con el resto de la parte como contexto que no se toca, y no una reescritura de toda la prosa (Eduardo, ronda 6: 43 de 48 corregidos, 5 limpios). Los JSON se escriben con Write o Python, nunca con `Out-File -Encoding utf8` de PowerShell 5.1: mete un BOM y `aplicar.py` falla con «Unexpected UTF-8 BOM». **Los párrafos limpios de IA que se reescribieron para bajar similitud también se devuelven, pero con cirugía mínima** (13-Pamela, 18-oct-2026; corrige la «excepción» que se puso el 17-oct). Con la excepción, Pamela pasó SIETE rondas en «*%»: para bajar el 39 % se había reescrito todo el cuerpo, solo el 9 % seguía siendo texto de la tesista y cada pasada de IA (tramos, documento entero, ritmo) reescribía texto de modelo con más texto de modelo. El usuario: «Sigue sin funcionar… qué estás haciendo mal». Lo que se hace, en cuanto una ronda de IA sobre texto ya reescrito por similitud vuelve en «*%»:
1. `devolver.py` (modelo en el scratchpad de la sesión d73276e4): por cada párrafo del cuerpo, cuántas palabras marcó el primer reporte de IA, y los tramos de similitud del original (primer reporte de similitud cruzado contra `actual`) frente a los de hoy.
2. Los párrafos que el primer reporte de IA dejó **limpios** vuelven al `w:p` del original (copia profunda; se saltan los que tengan imagen o vínculo). En Pamela fueron 69 párrafos, 5 921 palabras.
3. Dos agentes hacen **cirugía mínima** sobre ese texto original (encargo_rest.md): solo los tramos de 3 o más palabras que coincidían, con `viejo` corto y en la voz de la tesista, sin corregir estilo ni muletillas, que son justamente lo que pasa como humano.
4. Los párrafos que el primer reporte marcó como IA siguen con su reescritura.
Desde el principio, cuando se pidan «las dos» con un tope de similitud bajo, la similitud se baja así en los párrafos limpios de IA (original + cirugía de tramos) y solo se reescribe desde la idea lo marcado como IA.

**Parte en «*%» casi toda original** (Eduardo Sime, 18-oct-2026): la P2A (3.1-3.2) seguía en «*%» y el resto de la parte 2 ya daba 0 %. Al cruzar el primer reporte con marcas, 3.1-3.2 era casi todo texto original no marcado y sin cambios (difflib 1,0); el residuo eran solo los 8 párrafos reescritos en rondas anteriores (unas 450 palabras, 11 % del trozo, incluidas Nota y Fuente de tabla). Se reescribieron una vez desde la idea con la voz de los párrafos originales vecinos (oración simple, futuro, sin enlaces de manual) y no se tocó nada más. Antes de reescribir un trozo en «*%», listar por párrafo: marcado en ronda 1 sí/no y parecido con el original; lo que tiene 1,0 y no fue marcado no entra. **Pero si con eso sigue en «*%»** (Eduardo, ronda 8, 10:29), el residuo está en el propio original no marcado: lo que la ronda 1 no marcó dentro de 14 000 palabras sí pesa en un trozo de 4 000. Se mide con `medir.py` contra la parte que dio 0 % (en Eduardo: oración media 31 frente a 26, palabra 5,44 frente a 5,09, sujeto abstracto 46 % frente a 28 %) y se reescribe toda la prosa del trozo con esa parte como muestra de voz (2 agentes, `encargo_r9.md` en el scratchpad de esa sesión). Al leer la salida línea por línea apareció el molde «X será Y.» abriendo enfoque, tipo, nivel, diseño y muestreo, «Con X se…» cuatro veces y «Por eso» tres: se rehacen antes de aplicar. Si cambia el número de páginas y Word se cuelga al actualizar el índice, los números se corrigen en el XML entrada por entrada contra el PDF nuevo, nunca con una resta global (dentro de 3.1-3.4 unas secciones bajaron una página y otras no).

**Historia: partir** (10-Roy, 14-oct-2026: cuatro rondas en «*%»). Por debajo de 20 % Turnitin no resalta nada, pero en un trozo pequeño lo que queda de IA pasa del 20 % de ese trozo y sí aparece resaltado. Se deja en `Subir a Turnitin\partes\` el último Word de `Listo` cortado por secciones en tres o cuatro archivos de al menos 300 palabras cada uno (el mínimo de Turnitin para medir IA; las referencias, en una parte aparte). El usuario sube cada parte y deja los reportes en `reportes\ia`; con `marcado_ia.py` contra el Word completo de `Listo` se ve exactamente qué oraciones son, y solo esas se reescriben, con otra arquitectura. Una parte que dé 0 % ya no se toca. Se corta con `python <skill>/scripts/partir.py <word> <salida> <desde> <hasta>` (índices de párrafo de `estado`/`aplicar`). **No se vuelve a partir** (el usuario lo rechazó el 14-oct-2026: «son demasiadas partes a subir»). Si una parte vuelve en «*%», las partes que dieron 0 % son la muestra de lo que pasa: se mide la prosa de las dos con `medir.py` del humanizador y `auditar_patrones.py`, se leen las aperturas de cada párrafo, se busca qué patrones del catálogo tiene la que sigue en «*%» y no la que dio 0 % (en 10-Roy: molde repetido en los antecedentes, frases-etiqueta 0c, «X no es Y» en cadena, oraciones sin enlazar), y se humanizan solo esas partes con el `humanizador-academico`, usando la parte en 0 % como muestra de voz. Al quitar frases-etiqueta fundiéndolas, se miran después los largos de oración por párrafo: en 10-Roy la primera pasada dejó todas entre 22 y 43 palabras y hubo que rehacerla para que cada párrafo tuviera una oración de 12 o menos y otra de 38 o más, como la parte que dio 0 %.

**Antes de entregar cualquier humanización de toda la prosa: dos pasadas de repeticiones sobre
el documento entero** (10-Roy, 14-oct-2026). Hubo ocho rondas locales en «*%» con todo lo
anterior. El usuario subió el recortado al conector (`humanizar_mi_documento`) y le pidió dos
veces «verifica todo nuevamente a ver si hay patrones IA, en caso hubieran quítalo y no
generes más». El reporte dio **0 % en una sola subida**. La diferencia fue que el conector miró
el documento completo de una vez. Los cuatro agentes trabajan cada uno su tramo, y ninguno ve
que su apertura es la misma que la de los otros tres. Por eso, cuando los agentes terminan y
los JSON ya están aplicados, la sesión principal (no un agente por tramo) hace esto dos veces:

```
python <skill>/scripts/repeticiones.py "<Listo\salida.docx>"
```

El script lista las aperturas de párrafo repetidas tres o más veces, las oraciones que arrancan
igual («También…», «Además…») y los moldes fijos, cada uno con sus párrafos. Lo que el conector
encontró y quitó en Roy fue esto:

- Aperturas con el mismo molde: «Con esa clasificación / Con ese criterio / Con esa pauta /
  Con ellas…» en nueve párrafos, «Este eje… / En este eje…» en cada subcategoría y
  «También…» abriendo oraciones en párrafos seguidos.
- Oraciones partidas del tipo «Lo que se hará es…» o «Lo que pide es…», que pasan a oración
  directa.
- Listas anunciadas con número y dos puntos («cuatro fases: …», «tres ejes: …»), que se meten
  en la oración.
- Conectores y cierres que vuelven una y otra vez: «De ahí», «Ahora bien», «entonces», «Por ese
  motivo / Por esa razón», «Se trata de», «de modo que», «ayuda a / servirá para», y el cierre
  «Con este trabajo…».

De cada molde se dejan una o dos apariciones y las demás se cambian con `viejo` por una
construcción distinta, sin tocar cifras, autores ni títulos entre comillas. La segunda pasada
va sobre el resultado de la primera, porque al variar salen moldes nuevos («Por ese motivo»
apareció al quitar «De ahí»). No se busca dejar el contador en cero. El Word que dio 0 % todavía
tiene tres «La investigación…», seis «También…» y nueve «permite / ayuda a» en 112 párrafos. Lo
que no puede quedar es un mismo arranque en cinco o más párrafos, ni un molde repetido en casi
todas las subcategorías.

**Cuando humaniza por bloques: leer línea por línea antes de mostrar** (13-Pamela, 18-oct-2026). El
usuario pidió el `humanizador-academico` «por bloques» sobre el Word de `Listo`, y al ver el bloque 3
respondió: «Tienes que analizar línea por línea para identificar si no se crearon nuevos patrones
IA». Esa lectura encontró 13 patrones metidos por las propias correcciones, que `cobertura.py` y
`ficha.py` no ven:
- complementos antepuestos al reordenar («Con solo un 4.4%…», «De la verificabilidad, …»);
- el mismo arranque en párrafos vecinos («Las respuestas sobre…» ×2, «En Ecuador, Autor…» y luego
  «En el Perú, Autor…»);
- un dato repetido del párrafo anterior;
- un «Sus» que pasó a referirse a otro sujeto;
- un agente que se perdió;
- un «se ubicó» con el sentido cambiado;
- una fusión de 59 palabras.

Desde entonces, cada bloque se muestra solo después de listar sus oraciones nuevas con su largo y
sus primeras palabras, junto a las de los párrafos vecinos aunque no se toquen. Se relee contra el
catálogo y se rehace lo que aparezca, en dos o tres vueltas. En la TRAZA se dice qué metió la
primera versión. Los párrafos de resultados con ecuaciones de Word solo admiten cambios entre
ecuación y ecuación (se ven con `[r.text for r in p.runs]`), así que su molde «El X % … Bajo …
Medio … Alto» se varía en el verbo y no en el orden.

**Cuando el usuario trae el Word del conector.** El conector humaniza lo que él le sube, que es
el recortado de `Subir a Turnitin`. Si vuelve con ese Word y su reporte, el recortado tiene los
mismos párrafos que su gemelo completo de `Listo`, corridos un número fijo (en Roy fueron 27,
los de la carátula). Se comprueba que todos los párrafos sin cambios coinciden con ese
desfase. Después se pasan los párrafos cambiados al Word completo con `aplicar.py` (párrafo
entero, sin `viejo`), se corre `restaurar_rotulos.py` y se vuelve a correr `para_turnitin.py`.
El recortado tiene que salir idéntico al que trajo, párrafo a párrafo. Si el conector pasó una
cita de narrativa a parentética y conservó autor y año, `aplicar.py` lo frena; se revisa y se
pasa con `forzar`. El Word del conector, que es el que se midió, se guarda en
`Subir a Turnitin` con el nombre de la gemela.

**Esta receta dio 0 % de IA en una ronda** (tesis 07, 11-oct-2026). El paso a paso, el reparto
en agentes y lo que se le dice a cada uno están en `references/receta-ia-cero.md`: se lee y se
sigue tal cual cuando el usuario pide 0 % o «la configuración que dio 0».

**Caso B sin marcas, tesis entera en una ronda** (16 Carla Tarrillo, asesoría, 22-oct-2026). Llegó en «*%» sin nada resaltado y similitud 13 %. Se humanizó toda la prosa del cuerpo (130 párrafos) con 5 agentes y un `encargo.md` común (tramos por capítulo, romper el molde entre párrafos vecinos, no tocar rótulos, fórmulas ni el párrafo de objetivos), más una pasada global de la sesión principal (38 retoques: frases repetidas entre secciones y conectores). Turnitin 2: **IA 0 %** y similitud 13 → 11 % en la primera vuelta.
