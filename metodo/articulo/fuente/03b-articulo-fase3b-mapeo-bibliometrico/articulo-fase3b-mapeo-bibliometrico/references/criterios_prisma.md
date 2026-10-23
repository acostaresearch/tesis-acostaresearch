# Criterios de inclusión y el diagrama PRISMA

Se lee en el Paso 3, **antes de analizar nada**. Es lo primero que mira un
revisor de una revisión, y sin ello el artículo se rechaza sin llegar a los
resultados.

Lo que responde es una sola pregunta: **de cuántos partiste y con cuántos te
quedaste, y por qué.**

## Los criterios, uno por uno

Se deciden CON el investigador y se dejan escritos. Cada uno necesita un motivo,
y el motivo se escribe en el artículo.

**Periodo.** Y por qué ese. «Desde 2015» sin explicación es arbitrario; «desde
2015, año en que se publica la norma que regula X» es un criterio.

**Tipo de documento.** Normalmente artículos y revisiones. Se excluyen
editoriales, cartas al editor, erratas y actas de congreso — salvo que el campo
sea de informática, donde los congresos son la publicación principal y
excluirlos deja fuera lo mejor.

**Idioma.** Si se acota, se dice. Y se admite lo que implica: limitarse al inglés
deja fuera la producción regional, que a veces es justo la que interesaba.

**Área temática.** Si la base la ofrece. Útil cuando un término significa cosas
distintas en dos campos.

**Duplicados.** Obligatorio si se combinan dos bases. Se deduplican por DOI, y
por título los que no lo tengan.

**Exclusión por contenido.** Los que la ecuación trajo pero no van del tema. Se
revisa por título y resumen, y **se cuenta cuántos se quitaron**.

## El diagrama

```
                    IDENTIFICACIÓN
   Registros encontrados en [base]:            n = ___
   Registros de otras fuentes:                 n = ___
                         │
                         ▼
                      CRIBADO
   Duplicados eliminados:                      n = ___
   Registros cribados:                         n = ___
   Excluidos por título y resumen:             n = ___
                         │
                         ▼
                    ELEGIBILIDAD
   Evaluados en detalle:                       n = ___
   Excluidos, con motivo:                      n = ___
      · fuera de tema                          n = ___
      · tipo de documento                      n = ___
      · sin resumen disponible                 n = ___
                         │
                         ▼
                     INCLUIDOS
   Documentos del análisis final:              n = ___
```

**Las cifras salen de la base y del script, nunca de la memoria.** Si el
investigador no las tiene todavía, el diagrama se deja con los huecos y se
rellena después.

## El párrafo que lo acompaña

Va en Métodos, y tiene una forma casi fija:

> «La búsqueda se realizó en [base] el [fecha], mediante la ecuación
> [ecuación exacta]. Se recuperaron [n] registros. Tras eliminar [n]
> duplicados y aplicar los criterios de inclusión —[periodo], [tipo de
> documento], [idioma]—, el corpus final quedó en [n] documentos publicados
> entre [año] y [año].»

**La fecha de la búsqueda no es un adorno.** Un corpus descargado en marzo no es
el mismo que uno de septiembre, y el revisor lo pregunta. Si el artículo tarda
seis meses en publicarse, esa fecha es lo que hace reproducible el estudio.

## Lo que hace fallar esto

- **Criterios escritos después de ver los resultados.** Se nota, y es mala
  ciencia. Se definen antes.
- **Un diagrama con cifras que no suman.** Es lo primero que comprueba un
  revisor con la calculadora.
- **«Se excluyeron los no pertinentes»** sin decir cuántos ni con qué criterio.
- **No decir la fecha de la búsqueda.**
