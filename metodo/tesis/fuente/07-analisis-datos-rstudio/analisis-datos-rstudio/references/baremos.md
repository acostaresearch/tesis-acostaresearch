# Baremos y niveles de la variable

Este archivo cubre el paso de convertir puntajes brutos en categorías (bajo,
medio, alto), que es lo que después permite decir "el 42% de la muestra presenta
un nivel alto de X". Acompaña al Paso 5 del SKILL.md.

## Regla que manda sobre todas las demás

**Si el instrumento que usa el tesista ya trae baremos publicados por sus
autores, se usan esos y no se calculan otros.** Recategorizar por tu cuenta un
instrumento que ya tiene normas es un error metodológico: los puntos de corte del
autor salieron de un estudio de estandarización con su propia muestra, y
reemplazarlos rompe la comparabilidad con el resto de la literatura.

En ese caso, la skill:

1. Le pide al tesista los puntos de corte tal como aparecen en el manual o en el
   artículo original del instrumento.
2. Los aplica sin modificarlos.
3. Cita la fuente de los baremos en la nota de la tabla, con la clave `[AR…]` de
   ese manual o artículo en su biblioteca. Si no está, se busca con
   `buscar_fuentes` o se añade con `anadir_a_mis_fuentes` (con su permiso); mientras
   no tenga clave, la nota lleva `[FALTA FUENTE]` y se le avisa en el chat.
4. Si el tesista no tiene el manual a mano, **no los inventa ni los aproxima**:
   se lo dice y le pide que los consiga, o se pasa al cálculo propio dejando
   constancia explícita de que son baremos de la muestra y no los del autor.

## Cuándo se calculan baremos propios

Solo en estos casos:

- El instrumento fue construido por el tesista (Skill de Instrumento).
- El instrumento es una adaptación con cambios que invalidan los baremos
  originales (se quitaron ítems, cambió la escala de respuesta, cambió la
  población de forma sustantiva).
- El instrumento original no publica baremos.

Cuando se calculan propios, **hay que declararlo en el texto**: son baremos de
esta muestra, no normas poblacionales, y no se pueden generalizar.

El método se elige con el tesista **antes** de mirar los resultados. Por defecto la
skill propone percentiles (Método 2), que es lo que usa el Paso 5; si el asesor
pide rango equidistante o media y DE, se usa ese.

## Método 1 — Rango equidistante

Se reparte el recorrido posible del puntaje en tres tramos iguales.

```
Puntaje mínimo posible = (número de ítems) × (valor mínimo de la escala)
Puntaje máximo posible = (número de ítems) × (valor máximo de la escala)
Recorrido = máximo - mínimo
Amplitud  = Recorrido / número de niveles
```

Ejemplo con 20 ítems en escala Likert de 1 a 5:

```
Mínimo    = 20 × 1 = 20
Máximo    = 20 × 5 = 100
Recorrido = 80
Amplitud  = 80 / 3 = 26.67 -> se redondea a 27

Bajo   20 a 46
Medio  47 a 73
Alto   74 a 100
```

Ventaja: es simple y reproducible. Desventaja: no dice nada sobre cómo se
distribuye la muestra real. Si todos los encuestados puntúan alto, el nivel
"bajo" queda vacío, y eso es un hallazgo que hay que reportar, no esconder.

## Método 2 — Percentiles (baremos de la muestra)

Se usan los percentiles 33 y 67 de los puntajes observados como puntos de corte
(25, 50 y 75 para cuatro niveles; 20, 40, 60 y 80 para cinco), igual que en el
código del Paso 5.

```
Bajo    por debajo del percentil 33
Medio   del percentil 33 al 67
Alto    del percentil 67 en adelante
```

Ventaja: los tres niveles quedan poblados por construcción. Desventaja: los
cortes dependen de esta muestra, así que dos tesis con el mismo instrumento no
son comparables entre sí.

**Regla dura**: si se usa este método, el texto debe decir que los niveles son
relativos a la muestra. Escribir "el 33% presenta nivel bajo" sin esa aclaración
es engañoso, porque ese 33% es una consecuencia del método, no un hallazgo.

## Método 3 — Media y desviación estándar

```
Bajo    menor que (media - 1 DE)
Medio   entre (media - 1 DE) y (media + 1 DE)
Alto    mayor que (media + 1 DE)
```

Solo tiene sentido si la distribución es aproximadamente normal. Si la prueba de
normalidad salió significativa, este método no corresponde y hay que usar
percentiles.

## Baremos por dimensión

Si la tesis reporta niveles por cada dimensión, **los cortes se calculan por
dimensión**, no se reparte el total. Cada dimensión tiene su propio número de
ítems y por lo tanto su propio recorrido.

Error frecuente: usar los cortes de la variable global para clasificar las
dimensiones. Da porcentajes sin sentido.

## Qué debe declarar la skill en la tabla

La nota de la tabla de niveles (`*Nota.* …`, en el bloque de tabla del capítulo)
lleva siempre:

- Qué método se usó (rango equidistante, percentiles, media y DE, o baremos del
  autor).
- De dónde salen los cortes, con la clave de la fuente si son del autor del
  instrumento.
- El número de ítems y el rango de la escala.
- El N sobre el que se calcularon.

Los cortes y los porcentajes que vayan al texto se guardan antes con
`guardar_analisis` (campo `resultados`), como el resto de las cifras.

## Lo que nunca se hace

- **No se inventan puntos de corte** para que los porcentajes queden "más
  presentables".
- **No se cambia de método** después de ver los resultados porque el primero dio
  una distribución poco favorable. El método se elige antes de mirar, y si se
  cambia, se dice por qué.
- **No se presentan baremos de la muestra como si fueran normas del
  instrumento.**
- **No se reporta un nivel vacío como si no existiera.** Si ningún caso cayó en
  "bajo", eso se reporta con su cero.
