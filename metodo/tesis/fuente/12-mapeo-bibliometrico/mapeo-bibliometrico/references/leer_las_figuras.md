# Qué dice cada figura, y qué no

Se lee en los Pasos 5, 6 y 7. Es el archivo que decide si el artículo se publica
o se rechaza, porque el error que hunde una revisión bibliométrica no es
calcular mal: es **describir en vez de interpretar**.

```
Describir:    "La Figura 2 muestra 15 países."
Interpretar:  "La producción se concentra en tres países que aportan el 60%
               de los documentos, lo que sugiere que el campo todavía no se
               ha internacionalizado."
```

La primera frase el revisor ya la sabe: está mirando la figura. La segunda es
por lo que le paga la revista al autor.

---

## Producción anual

**Qué es.** Documentos publicados por año.

**Qué se puede decir.** Si el campo crece, se estanca o decae. Dónde está el
punto de inflexión. Si el último año está incompleto —lo está casi siempre,
porque la indexación va con retraso— **hay que decirlo**, o parece una caída.

**Qué NO se puede decir.** Por qué. Un pico en 2020 es un pico en 2020. Atribuirlo
a la pandemia es una conjetura del autor, y se escribe como tal: «coincide con»,
no «se debe a».

**La trampa.** Un crecimiento exponencial no significa que el campo sea
importante: **toda la producción científica crece**. Si se quiere afirmar que
crece más que la media, hay que compararlo con algo.

---

## Países

**Qué se puede decir.** Dónde se produce el conocimiento del campo, y si hay
colaboración internacional o cada país trabaja solo.

**Qué NO se puede decir.** Que un país «lidera» el campo. Produce más, que no es
lo mismo. Estados Unidos y China producen más de casi todo porque tienen más
investigadores.

**Lo que sí vale la pena mirar**, y casi nadie lo hace: **si tu país está o no
está.** Un campo con 1.200 documentos y cuatro peruanos es, en sí mismo, el vacío
que justifica el artículo.

---

## Revistas y ley de Bradford

**Qué es.** Bradford parte las revistas en tres zonas con el mismo número de
artículos cada una. La primera zona —el **núcleo**— suele ser un puñado de
revistas que concentra un tercio de todo.

**Qué se puede decir.** Cuáles son las revistas del campo. Y algo práctico que
el autor agradece: **ese núcleo es su lista de destinos para enviar el
artículo.**

**Qué NO se puede decir.** Que las del núcleo sean las mejores. Son las que más
publican de este tema.

---

## Autores y ley de Lotka

**Qué es.** Lotka describe cómo se reparte la productividad: muchos autores con
un solo artículo, poquísimos con muchos.

**Qué se puede decir.** Si el campo tiene grupos consolidados o es de gente que
pasó una vez. Un campo donde el 90% firmó un solo artículo está disperso, sin
escuelas formadas.

**Qué NO se puede decir.** Que los autores más productivos sean los más
influyentes. Para eso está la cocitación.

**La trampa.** Los nombres se desambiguan mal. «Wang, Y.» pueden ser cuarenta
personas. Antes de nombrar a alguien en el texto, comprobar que existe.

---

## Documentos más citados

**Qué se puede decir.** Cuáles son los trabajos de referencia. Estos sí **hay que
leerlos** —son diez o quince— y se citan por contenido en el artículo.

**Qué NO se puede decir.** Que sean los mejores. Las citas se acumulan con el
tiempo: un artículo de 2015 con 200 citas y uno de 2024 con 20 no se comparan.
Si la base lo ofrece, mirar **citas por año**.

---

## Coocurrencia de palabras clave

**Qué es.** Qué términos aparecen juntos en los mismos documentos. Los grupos que
se forman son los subtemas del campo.

**Qué se puede decir.** Qué se investiga junto con qué. Qué términos son el centro
y cuáles periféricos.

**Qué NO se puede decir.** Que dos términos unidos tengan relación causal ni
teórica. Aparecen en los mismos artículos. Nada más.

**La trampa.** Los términos del propio tema de búsqueda salen enormes y en el
centro, porque estaban en la ecuación. Eso no es un hallazgo: es la definición
del corpus. Conviene excluirlos del gráfico y decir que se excluyeron.

---

## Mapa temático — los cuatro cuadrantes

La figura estrella, y la que nadie sabe leer. Dos ejes:

- **Centralidad** (horizontal): cuánto se relaciona ese tema con el resto del
  campo. Su importancia.
- **Densidad** (vertical): cuánto se relacionan entre sí los términos de dentro.
  Su desarrollo interno.

```
   densidad
      ▲
      │  NICHO              MOTORES
      │  muy desarrollados  desarrollados Y
      │  pero aislados      centrales: el
      │                     corazón del campo
      │─────────────────────────────────────
      │  EMERGENTES         BÁSICOS
      │  o EN DECLIVE       importantes pero
      │  poco de todo       poco desarrollados
      └─────────────────────────────► centralidad
```

**Cómo se escribe cada uno:**

- **Motores.** «Los temas consolidados del campo son X e Y: aparecen relacionados
  con casi todo lo demás y tienen literatura propia madura.»
- **Básicos.** «Z es transversal al campo pero está poco desarrollado: se
  menciona en muchos trabajos y pocos lo estudian a fondo.» ← **aquí suelen estar
  los vacíos**.
- **Nicho.** «W forma una literatura densa y separada: una comunidad que trabaja
  sola.»
- **Emergentes o en declive.** «V aparece poco y disperso.» **La figura no
  distingue si nace o si muere.** Para saberlo hay que mirar la evolución
  temática o el año de los documentos. Si no se mira, se escribe «emergente o en
  declive», tal cual.

**La trampa grande.** Un cluster no es una línea de investigación: es un grupo de
palabras que aparecieron juntas. Escribir «el campo tiene cuatro líneas
consolidadas» es afirmar más de lo que el análisis sostiene. Se escribe «el
análisis de coocurrencia agrupó los términos en cuatro conjuntos».

**Si el corpus vino de OpenAlex**, este mapa se calculó sobre títulos y
resúmenes, no sobre palabras clave de autor. Se declara en Métodos. No es peor,
es distinto: recoge el lenguaje del texto en vez del que eligió el autor.

---

## Evolución temática

**Qué se puede decir.** Qué temas se mantienen, cuáles se dividen, cuáles
desaparecen. Es lo que convierte una foto en una película.

**La trampa.** Los cortes de periodo cambian el resultado. Se eligen por un
motivo —un hito del campo, un cambio normativo— y **ese motivo se escribe**. Si
se eligieron para que saliera bonito, se nota.

---

## Cocitación

**Qué es.** Dos trabajos citados juntos por un tercero. Si pasa mucho, pertenecen
a la misma base intelectual.

**Qué se puede decir.** Sobre qué se ha construido el campo, y si tiene una raíz
común o varias escuelas separadas.

**Qué NO se puede decir.** Que los autores estén de acuerdo. Se les cita juntos;
a veces precisamente porque discrepan.

---

## Acoplamiento bibliográfico

**Qué es.** Al revés que la cocitación: dos trabajos que citan lo mismo. Mira el
presente en vez del pasado.

**Qué se puede decir.** Qué grupos trabajan hoy sobre la misma base, aunque no se
citen entre ellos. Suele revelar comunidades que se ignoran.

---

## Regla final, para todos los párrafos

Cada párrafo de esta sección tiene que poder terminar con **«y esto importa
porque…»**. Si no se puede, ese párrafo describe una figura que el lector ya está
viendo, y sobra.
