# De dónde sale el corpus: Scopus o OpenAlex

Se lee en el Paso 1. Es la bifurcación de toda la fase, y hay que contarla con
honestidad: **una opción es mejor, pero la otra permite escribir el artículo a
quien no tiene la primera.**

## La regla corta

| | |
|---|---|
| **¿Tienes acceso a Scopus o WoS por tu universidad?** | Úsalo |
| **¿No lo tienes?** | OpenAlex, y se declara en Métodos |

Nadie se queda sin artículo por no tener suscripción. Pero tampoco se le dice a
quien sí la tiene que da igual, porque no da igual.

---

## Qué gana quien usa Scopus

**Las palabras clave son de personas.** Las escribieron el autor y el indizador
de la base. Eso es lo que hace que el mapa temático signifique algo.

En OpenAlex las asigna un clasificador automático. Comprobado sobre un artículo
real de integridad académica:

```
Scopus     AI · Academic integrity · Higher education ·
           Inclusive educational environment · Student learning

OpenAlex   Safeguarding · Academic integrity · Higher education ·
           Engineering ethics · Context (archaeology) · Equity (law) ·
           Educational equity · Student engagement · Learning analytics ·
           Knowledge management · Psychology · Computer science ·
           Political science · Pedagogy · Data science · Engineering
```

Dieciséis contra cinco, pero con **«Context (archaeology)»** y **«Equity (law)»**
metidas de por medio. Esas desambiguaciones de enciclopedia ensucian los
clusters.

Y en español es peor. Un artículo chileno sobre deserción universitaria tiene
como palabras clave en OpenAlex: `Humanities · Sociology · Philosophy`. Nada
utilizable.

**El nombre también pesa.** «Corpus extraído de Scopus» en la sección de Métodos
significa algo para un evaluador. Es un hecho del oficio, no una opinión.

---

## Qué gana quien usa OpenAlex

**Cobertura latinoamericana.** Indexa Scielo, Redalyc y repositorios
universitarios que Scopus no tiene. Para un artículo que necesita antecedentes
regionales, eso no es un consuelo: es una ventaja real.

**No cuesta nada y no pide credenciales.** Ni VPN de la universidad, ni pedirle
el acceso a un colega.

**Los datos llegan al script solos.** No hay archivo que descargar ni que subir:
`oa_fetch()` los trae desde R.

---

## Lo que se pierde, exactamente

**Solo una cosa: el mapa temático sobre palabras clave de autor.**

Todo lo demás —producción anual, países, revistas, Bradford, Lotka, citas,
coautoría, cocitación— sale igual de bien, y a veces mejor, porque el corpus es
más amplio.

**El apaño es honesto y está previsto por los propios autores de la
herramienta:** la coocurrencia se calcula sobre títulos y resúmenes en lugar de
palabras clave (`field = "TI"` o `"AB"` en `thematicMap`). El resultado sirve, y
recoge el lenguaje del texto en vez del que eligió el autor.

**Se declara en Métodos.** Una frase:

> «Dado que los registros de OpenAlex no incluyen palabras clave asignadas por
> los autores, el análisis de coocurrencia se realizó sobre los términos de
> títulos y resúmenes.»

Un revisor que lea eso lo acepta. Uno que descubra que se le ocultó, no.

---

## Un riesgo del carril de OpenAlex, comprobado

**La búsqueda puede estar caída aunque la base funcione.** Es una organización sin
ánimo de lucro y su buscador se pausa a veces para usuarios anónimos:

```
"Anonymous search is paused while the search cluster recovers"
```

Comprobado en septiembre de 2026: los filtros por país, idioma, año y tipo
seguían funcionando perfectamente, y **solo la búsqueda por texto estaba
pausada.**

Qué hacer si pasa en mitad de la fase:

1. **Esperar.** Suele ser cuestión de horas.
2. **Construir el corpus por filtros** en lugar de por texto: país, idioma,
   periodo y concepto (`concepts.id`). Es menos preciso, pero funciona.
3. Si urge, **pedirle a alguien un export de Scopus.** Un compañero con acceso
   tarda cinco minutos.

Decírselo al investigador **antes** de empezar, no cuando le falle. Y no
prometerle que OpenAlex es equivalente a una suscripción institucional: es
gratis, es muy bueno, y depende de un servidor que a veces se cansa.
