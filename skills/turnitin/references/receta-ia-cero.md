# Receta que dio 0 % de IA (tesis 07, 11-oct-2026)

Desde el 18-oct-2026 el orden lo da `ruta-ia-cero.md`; de aquí se toma el reparto y el encargo de
los agentes.

Tesis de maestría de 13 700 palabras. Partía de IA «*%» (menos de 20 %, sin nada resaltado) y
similitud 28 %. Con esta receta, en una sola ronda, el reporte de IA dio **0 %**. Se repite
igual cada vez que el usuario pida 0 % o diga «usa la configuración que dio 0».

## Orden

1. `para_turnitin.py` si el Word trae preliminares y anexos.
2. Similitud primero (paso 3B), sobre el Word que el reporte analizó → copia intermedia en el
   scratchpad (`sim.docx`).
3. Humanización de TODA la prosa sobre esa copia intermedia → `Listo\<nombre> - humanizado.docx`.
4. `restaurar_rotulos.py`, `verificar_cambios.py` y otra vez el marcado de similitud; los
   tramos de 7 o más palabras que la humanización haya devuelto se retocan a mano con `viejo`.
5. **Dos pasadas de `repeticiones.py` sobre el documento entero**, que hace la sesión
   principal y no los agentes, para variar las aperturas, los conectores y los moldes que se
   repiten entre tramos (ver `casos-ia.md`, «Antes de entregar cualquier humanización»). Es el paso
   que faltaba en 10-Roy: hubo ocho rondas en «*%» con los pasos 1 a 4, y el reporte dio 0 %
   cuando el conector hizo estas dos pasadas.

## Reparto

Cuatro agentes `general-purpose` a la vez en cada pasada, uno por tramo de párrafos con un
número parecido de palabras de prosa (se cuentan los párrafos de 25 palabras o más que no son
Heading ni Caption y se corta en los cuartiles). Cada agente escribe su `cambios_N.json`
(`cambios_hN.json` en la humanización), lo prueba él mismo con `aplicar.py` hasta que pasa sin
`forzar`, y devuelve solo un informe: párrafos reescritos, los que dejó y por qué, erratas.
Los JSON se unen y se aplican de una vez.

**El encargo va en un archivo, no en cada mensaje** (12-oct-2026, 09-Samuel Auccahuaqui Rosa). El texto común se
escribe una vez en `<scratchpad>\encargo.md` y a cada agente se le da solo la ruta, su número N
y la lista de párrafos de su tramo. Copiar el encargo entero con huecos por rellenar hizo que un
agente saliera sin tramo, y al corregirlo y relanzarlo se trabajó dos veces el mismo rango. Los
párrafos que no se tocan (títulos de tabla, «Nota.», encabezados, referencias, rótulos) se
listan por número en el encargo, sacados de `marcado_ia.py`.

**Similitud e IA en la misma reescritura** (15-oct-2026, Renzo Cruz, tesis-asesorar: similitud 27 % sin
filtros con tope de 20 %, e IA «*%»). Cada agente hizo las dos cosas sobre su tramo en una sola pasada:
romper los tramos coincidentes de `ms.json` y escribir con el registro de `muestra-ia-cero.txt`. Bastaron
cinco agentes (tramos de 12 a 21 párrafos). En el encargo se dice que lean el Word con
`python -I -X utf8`: con `-I` se ignora `PYTHONIOENCODING` y la consola cp1252 rompe con «₀» o «≤».
Cuando la UCV mide sin filtros, las referencias ponen un piso que no se toca (en Renzo, unos 10 puntos);
el resto sale del cuerpo y de acortar los enunciados específicos, que repetían la delimitación completa.

Con un reporte que sí trae marcas (42 % en 09-Samuel Auccahuaqui Rosa) el reparto es el mismo, cortando por
caracteres marcados y no por palabras de prosa, y cada agente reescribe solo lo marcado.

## Lo que se le dice al agente de humanización

- No hay párrafos marcados: recorre toda la prosa de su tramo; si un párrafo está limpio de
  verdad, no lo toca.
- Lee antes de escribir: el `SKILL.md` del `humanizador-academico` con `catalogo_patrones.md`,
  `auditoria_de_la_salida.md` y `evidencia-caso-no-funciono.md` (están en
  `<SKILLS>\synced\…\humanizador-academico\references\`, que se busca con Glob
  `**/humanizador-academico/references/catalogo_patrones.md`; en `<METODO>\tesis\fuente\10-humanizador-academico`
  solo está el SKILL.md, y los agentes de Zulma Pacompia, 20-oct-2026, no los encontraron); `voz.md`; y
  `references/muestra-ia-cero.txt` como registro al que hay que llegar (arranca desde el hecho o
  el estudio; funde con «y», «pero», «ya que», «de modo que», «para que»; oraciones de largo
  desigual; vocabulario plano; ningún cierre que anuncie importancia).
- Sin bloques ni aprobación: fichas y relectura de la propia salida en silencio, hasta tres
  intentos por párrafo.
- Reescribir DESDE LA IDEA y también el cuerpo (regla de cobertura), cambiando el orden de la
  información y fundiendo oraciones con un conector que diga una relación que sí existe.
- Romper el molde entre párrafos vecinos, que es lo que más pesó: antecedentes que abren todos
  «Autor (n), en año, en ciudad»; marco teórico «definición del autor + aplicación»;
  «Actividades del objetivo específico 1…5» con la misma plantilla; párrafos de tabla que abren
  «La Tabla N muestra»; discusión «hallazgo → coincide con Autor → explicación → implicancia».
  Que uno arranque desde el estudio ajeno, otro integre dos estudios en una oración, otro cierre
  con la cita en vez de con un veredicto propio.
- Lo que más se quitó: anáforas «Esta realidad / Esto implica», «Sin embargo» y «Asimismo» de
  apertura, «Según…» y «Para Autor (n),…» como marco, dos puntos de bisagra, «es esencial /
  fundamental / los autores subrayan lo importante que es», gerundios colgados, tríadas.
- Humanizar es restar: ni metáforas ni adorno nuevo, ninguna falta a propósito.
- Fidelidad: mismas cifras, estadísticos, años, autores y números de cita, cada cita con su
  afirmación; mismo tiempo verbal y número de párrafos; nada entre comillas; sin rayas largas.
- No volver a la fórmula de manual ni a la redacción de la fuente que la pasada de similitud
  acaba de romper.
- No se tocan títulos, captions, «Nota:» y «Fuente:», palabras clave, problema, hipótesis,
  objetivos y sus repeticiones como rótulo, H0/H1. En párrafos con rótulo en negrita se usa
  `viejo` con lo que sigue al rótulo.
- Comprobar con `cobertura.py` y `ficha.py` del humanizador (la alerta «cierran sin cita» es
  falsa cuando las citas son numéricas).

## Cómo quedó el texto

75 párrafos humanizados sobre 113 tocados en total; el resto de la prosa ya estaba plana y no
se tocó. Las oraciones quedaron más largas (media de unas 30 a unas 37 palabras) porque se
fundieron, y aun así dio 0 %: no hay que partirlas para «parecer humano».
