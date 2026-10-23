# Ruta 0 % de IA

El protocolo único para llegar a 0 % de IA. Desde el 18-oct-2026 manda sobre todo lo demás. La
historia de cada caso está en `casos-ia.md`: se consulta, pero no se sigue paso a paso. El
encargo detallado para los agentes sigue en `receta-ia-cero.md`.

## Lo que enseñaron los trabajos

- **Salieron en 0 % en una o dos rondas** 07, 08, 09, 11, 12 y TA 02. En todos se reescribió lo
  marcado (o toda la prosa, si no había marcas), se hicieron dos pasadas sobre el documento
  entero y **no se tocó lo que el reporte dejaba limpio**.
- **Se quedaron de 6 a 10 rondas en «*%»** Roy, Eduardo, Pamela y 14-Parte I. Causas:
  1. Se reescribieron párrafos que el primer reporte dejaba limpios. Roy y Eduardo salieron
     del «*%» cuando se devolvieron al original, y Pamela tenía 78.
  2. Se perdió el primer reporte con marcas: `limpiar.py` lo mandó a la Papelera y las rondas
     siguientes no sabían qué era limpio.
  3. Quedó texto marcado sin reescribir porque «no se toca»: enunciados en lista gemela,
     H₀/H₁, subtítulos propios, notas de tabla, celdas y párrafos cortos.
  4. Se mantuvo la plantilla de la segunda mitad: descriptivos, contrastes, discusión,
     conclusiones y recomendaciones con el mismo esqueleto por objetivo.
  5. Se reescribió a ciegas, ronda tras ronda, sobre texto ya reescrito.
- **Lo que NO separa el 0 % del «*%»** (calibrado el 18-oct con `control_cero.py`): el ritmo
  (oración media, dispersión, oraciones cortas) y el porcentaje de texto que sigue siendo del
  autor. Los 0 % conservan entre el 14 y el 23 % del texto, y 11 y 12 tienen peor ritmo que
  Pamela. **No se hacen rondas para «mejorar el ritmo».**
- **Ningún método garantiza 0 % siempre**: el detector es estadístico. Lo que se busca es que
  salga a la primera, y que una ronda en «*%» tenga una causa concreta que corregir.

## Paso 0: guardar el primer reporte con marcas (antes de todo)

Del primer reporte de IA que traiga marcas (por encima de 20 %), antes de `limpiar.py`:

```
python <skill>/scripts/marcado_ia.py <primer reporte.pdf> <Word de actual> "<trabajo>\reportes\ia\primer-reporte.json"
```

En asesoría va a `05-pasadoporturnitin\primer-reporte.json`. Ese JSON no se borra nunca:
`limpiar.py` solo quita PDF. Dice qué fue limpio para toda la vida del trabajo. Si el trabajo
llegó ya en «*%», no hay JSON y se dice así en la memoria del trabajo.

## Ronda 1: una sola pasada que lo deje en 0 %

### A. Con reporte con marcas

1. **Lo limpio no se toca.** Si además hay que bajar similitud, en los párrafos limpios solo
   se hace cirugía mínima de los tramos coincidentes de 3 o más palabras, con `viejo` corto y
   en la voz del autor, sin corregir su estilo ni sus muletillas, porque eso es lo que pasa como
   humano.
2. **Lo marcado se reescribe una sola vez, desde la idea.** Se cambia el orden de la
   información y se funde con conectores que expresen una relación real. La muestra de voz va
   en este orden: `voz_tesista.txt`, que son los párrafos limpios del propio original volcados
   al scratchpad; después `voz.md`; después `muestra-ia-cero.txt`.
3. **Lo marcado que antes se protegía entra desde esta ronda, no como residuo:**
   - subtítulos propios del autor, más llanos (los normados, como «Marco teórico», no se tocan);
   - problema y objetivos marcados, reformulados lo mínimo, con las mismas variables, el mismo
     verbo y el mismo alcance («de qué manera… durante el periodo 2025» → «cómo… en 2025»), y
     cambiados igual en la matriz;
   - problemas, objetivos e hipótesis específicos en lista de tres gemelos: el enunciado
     general se queda entero y los específicos pasan a una oración que nombra las dimensiones;
   - H₀/H₁ cortas y llanas;
   - notas y fuentes de tabla (con `viejo` para conservar el rótulo), párrafos de menos de 25
     palabras y prosa dentro de celdas (con python-docx).

   El título inscrito no se toca. Todo enunciado cambiado se lista para que **lo apruebe el
   asesor**.
4. **Se rompe la plantilla de la segunda mitad.** Cuando varios párrafos hermanos están
   marcados (los descriptivos de cada dimensión, los contrastes, la discusión, las
   conclusiones y las recomendaciones por objetivo), cada uno toma una arquitectura distinta.
   Uno entra por la cifra, otro por la dimensión, otro por el estudio previo. En los
   contrastes no se repite «H₀ → Rho → figura → se respalda». El encargo dice qué arquitectura
   le toca a cada hermano, para que dos agentes no elijan la misma.
5. **Reparto:** de 4 a 5 agentes por tramos, cortando por palabras marcadas, con el encargo en
   `<scratchpad>\encargo.md` (modelo en `receta-ia-cero.md`). Cada agente prueba su JSON con
   `aplicar.py` (o `aplicar_fichas.py` si hay citas de Mendeley o de Zotero).

### B. Sin marcas (llegó en «*%» o sin reporte)

Se humaniza toda la prosa del cuerpo con `receta-ia-cero.md` (así dieron 0 % 07 y 08). Siguen
valiendo los puntos 3 y 4: los enunciados y la plantilla entran también aquí.

### Cierre de la ronda, que hace la sesión principal y no los agentes

6. Se aplican los JSON, y después `restaurar_rotulos.py` y `verificar_cambios.py`.
7. **Dos pasadas sobre el documento entero.** Primero, un agente lee todo el cuerpo de una
   vez (volcado a .txt con número de párrafo), quita los moldes que se repiten entre secciones
   y corre `repeticiones.py`. Después, un segundo agente nuevo verifica todo y quita lo que haya
   metido la primera pasada. Hay que cuidar que las oraciones enlazadas no caigan al quitar
   conectores: con ninguno repetido más de 4 o 5 veces, las enlazadas no bajan del 20 %.
8. **Lectura línea por línea** de cada oración nueva junto a las de los párrafos vecinos:
   complementos antepuestos, mismo arranque en párrafos vecinos, referentes rotos y datos
   repetidos.
9. Si se pidió similitud, se vuelve a cruzar con el reporte de similitud y se retocan los
   tramos de 7 o más palabras que hayan vuelto.
10. **Control antes de entregar:**

    ```
    python <skill>/scripts/control_cero.py "<Listo\salida.docx>" --original "<actual\word.docx>" --marcado "<reportes\ia\primer-reporte.json>"
    ```

    Si dice **NO ENTREGAR** (más de 2 párrafos limpios reescritos), esos párrafos se devuelven
    a su `w:p` original, con cirugía mínima si había similitud, y se corre otra vez. Sus avisos
    (arranques repetidos, ritmo) se miran, pero no frenan la entrega.

## Si vuelve en «*%»: ronda 2, sin reescribir a ciegas

En este orden, y se para en el primer paso que encuentre algo:

1. **`control_cero.py` con el primer reporte:** se devuelven los párrafos limpios que se hayan
   reescrito.
2. **Residuo marcado que no se reescribió:** se cruza `primer-reporte.json` con todos los
   `cambios_*.json` y se cuentan las palabras marcadas que siguen iguales (enunciados, notas,
   celdas, referencias). Si suman más del 1 % de lo subido, se reescriben. Las referencias no
   se tocan: se deja en `Subir a Turnitin` una copia sin referencias para comprobarlo.
3. **Plantilla:** se leen las aperturas de la segunda mitad. Si los hermanos siguen el mismo
   esqueleto, se rehacen con arquitecturas distintas (punto 4 de la ronda 1).
4. **Verificación, no reescritura:** un agente revisa solo los párrafos ya reescritos (los
   que marcó el primer reporte), con el resto como contexto que no se toca. Así lo hizo
   Eduardo en la ronda 6: corrigió 43 párrafos y dejó 5 que estaban limpios.

## Ronda 3 en «*%»: empezar de cero lo marcado

Se devuelve todo el cuerpo al Word de `actual` (con los anexos), menos lo que ya se comprobó
que dio 0 % por separado. Se reescriben una sola vez solo las oraciones del
`primer-reporte.json`, con `viejo` = la oración exacta y una arquitectura distinta de la de la
ronda 1. Después se hace el cierre completo (pasos 6 a 10).

## Si después de la ronda 3 sigue en «*%»

No se hace una cuarta ronda a ciegas. Se le dice al usuario qué se probó y se le ofrecen dos
caminos, para que elija:

- Subir el recortado al conector (`humanizar_mi_documento`) y pedir dos veces «verifica todo
  nuevamente a ver si hay patrones IA, en caso hubieran quítalo y no generes más». Así salió
  Roy. El Word que vuelve se pasa al completo como dice SKILL.md, en «Cuando el usuario trae
  el Word del conector».
- Un detector externo que marque oración por oración (GPTZero, Originality.ai o Sapling), que
  da la señal que Turnitin esconde por debajo del 20 %. No está montado y tiene costo.

Partir el documento en trozos no se propone como entrega: el usuario lo rechazó el 14-oct-2026.
Como diagnóstico sí funciona (13-Pamela, 19-oct-2026, tras doce rondas a ciegas): cada apartado
daba 0 % solo y el conjunto «*%». Se partió por mitades (Introducción + Metodología «*%»,
Resultados → Recomendaciones 0 %), luego la mitad que marcaba (marco teórico + metodología «*%»,
antecedentes + metodología 0 %), y el marco teórico solo, de 891 palabras, dio **41 % con
resaltado**: en un archivo pequeño lo marcado pasa del 20 % y Turnitin deja de esconderlo. Era el
recorrido componente por componente de COSO con ejemplos del almacén. Cada prueba se arma sobre la
gemela, quitando bloques del cuerpo (párrafos y tablas), sin cambiar una palabra, y se pide el PDF
en cuanto una salga con número.

## Mantener esta ruta

Cada trabajo que termine se anota en `casos-ia.md` en una línea: ronda en que dio 0 %, o qué
causa tenía el «*%». Si una causa nueva se repite en dos trabajos, se sube a esta ruta. Si
aparece una medida que separe el 0 % del «*%», se calibra en `control_cero.py` con los Word de
`Listo` y se anota arriba, en «Lo que NO separa».
