# La carta de presentación

Se lee en el Paso 3 (y en el reenvío, con la revista nueva). Modelo de **tono y estructura**, no de contenido: cada
carta lleva solo los datos de este envío.

## De dónde sale cada dato

| Dato | Fuente |
|---|---|
| Título exacto | `ARTICULO_[clave]_v8.docx` |
| Autor de correspondencia, filiación, correo, coautores | Página de título (Paso 2) |
| Hallazgos y cifras | Resumen / abstract del `_v8`, tal cual |
| Encaje con la revista | Alcance publicado de la revista y aporte que el propio manuscrito declara |
| Declaraciones | Las confirmadas en el Paso 3; lo no confirmado, `[POR CONFIRMAR: ...]` |

El .md se escribe con `[SIN SANGRIA]` en cada línea del encabezado y se arma con
`articulo_docx.py nuevo --md carta.md --out CARTA_[clave].docx --compacto`
(`--idioma en` si va en inglés). Modo C: la carta en un bloque para pegar.
Antes de entregarla, humanización breve: `humanizador-academico` en español,
`humanizador-academico-ingles` en modo breve en inglés.

## Versión en inglés

```
[Nombre del autor de correspondencia]
[Filiación]
[Ciudad, País]
[Correo]

[Fecha]

Editor-in-Chief
[Nombre de la revista]

Dear Editor,

We are pleased to submit our manuscript entitled "[Título exacto]" for
consideration for publication in [Nombre de la revista] as a [tipo de artículo].

[Qué se estudió, con quién, método a alto nivel y resultados clave con las
cifras exactas del abstract. Tono: "This study examines how X and Y relate to Z
among N participants from [contexto]. Using [método], we found that X had a
positive and significant effect on Z (β = .XXX; p < .XXX). Together, these
results point to [conclusión breve, sin adjetivos inflados]."]

[Encaje con la revista en prosa, sin "First/Second/Third": "We think the
manuscript fits the journal's scope. It offers [aporte 1]. It also [aporte 2]."]

This manuscript is original, has not been published previously, and is not
under consideration for publication elsewhere, in whole or in part. All authors
have approved the manuscript and agree with its submission to [Nombre de la
revista]. [POR CONFIRMAR: conflicto de intereses]

We appreciate your consideration and look forward to your response.

Sincerely,

[Autor de correspondencia]
On behalf of all co-authors: [Lista de coautores]
```

## Versión en español

```
[Nombre del autor de correspondencia]
[Filiación]
[Ciudad, País]
[Correo]

[Ciudad, fecha]

Señor(a) Editor(a)
[Nombre de la revista]

Estimado(a) Editor(a):

Presentamos el manuscrito titulado «[Título exacto]» para su evaluación y
posible publicación en [Nombre de la revista], en la sección [tipo de artículo].

[Qué se estudió, con quién, método y resultados clave con las cifras exactas
del resumen. Tono: "El estudio analiza la relación entre X e Y en N docentes de
[contexto]. Mediante [método] se encontró que X se asocia de forma positiva con
Y (r = .XX; p < .XXX)."]

[Encaje con la revista en prosa: qué aporta al alcance de la revista, tomado
de lo que el propio manuscrito declara como contribución.]

Declaramos que el manuscrito es original, no ha sido publicado previamente ni
se encuentra en evaluación en otra revista, y que todos los autores aprobaron
su versión final y su envío. [POR CONFIRMAR: conflicto de intereses]
[Si procede de una tesis: "El artículo se deriva de la tesis [título],
disponible en [repositorio y enlace]."]

Agradecemos su atención.

Atentamente,

[Autor de correspondencia]
En representación de los coautores: [Lista de coautores]
```

## Notas de estilo

- Las cifras van tal cual están en el resumen o el abstract; nunca redondeadas
  ni reinterpretadas.
- Sin raya larga (—): coma o dos oraciones.
- Sin lenguaje promocional ("pionero", "de gran relevancia") ni cierres
  optimistas.
- Originalidad, aprobación de los autores y conflicto de intereses son
  fórmulas del género, pero **el autor las confirma**: la línea de conflicto
  de intereses solo se completa con lo que él declaró en el Paso 3.
