# Cuando R no carga el archivo

Se lee en el Paso 4. Son los cinco tropiezos que paran al investigador, y todos
tienen arreglo en una línea. Si no se resuelven rápido, abandona aquí — porque
cree que el problema es que «no sabe programar», y no lo es.

---

## «cannot open file» o «No such file or directory»

**Casi siempre son las barras.** Windows las copia al revés de como las quiere R:

```r
# mal
"C:\Users\Ana\Downloads\scopus.csv"

# bien
"C:/Users/Ana/Downloads/scopus.csv"
```

Si sigue fallando, que compruebe dónde cree R que está:

```r
getwd()
list.files()
```

Y el atajo que evita el problema entero:

```r
M <- convert2df(file.choose(), dbsource = "scopus", format = "csv")
```

`file.choose()` abre el explorador de archivos. Se acabaron las rutas.

---

## Carga, pero con 0 documentos o columnas raras

**El `format` no coincide con el archivo.**

| Extensión | `format` |
|---|---|
| `.csv` | `"csv"` |
| `.bib` | `"bibtex"` |
| `.txt` de Web of Science | `"plaintext"` |

Y el `dbsource` tiene que ser el de la base de verdad: `"scopus"`, `"wos"`,
`"openalex"`. Un CSV de Scopus leído como `"wos"` carga sin error y sale vacío,
que es peor que fallar.

**Segunda causa: Excel.** Si abrió el CSV en Excel y lo guardó, Excel le cambió
los separadores y las comillas. Que vuelva a descargarlo de la base y **no lo
abra con nada**.

---

## El mapa temático sale vacío o con dos palabras

**Faltan las palabras clave.** En el export no marcó la casilla.

Comprobar:

```r
sum(!is.na(M$DE))   # palabras clave de autor
sum(!is.na(M$ID))   # palabras clave de la base
```

Si sale 0 o casi, hay que **volver a exportar** marcando palabras clave y
resumen. No hay forma de recuperarlas después.

Mientras tanto, o si el corpus vino de OpenAlex, se calcula sobre títulos:

```r
mapa <- thematicMap(M, field = "TI", n = 250, minfreq = 5)
```

---

## `minfreq` deja el gráfico en blanco, o ilegible

`minfreq` es cuántas veces tiene que aparecer un término para entrar.

- **Corpus de 300 documentos** → `minfreq = 3`
- **De 1.000** → `minfreq = 5`
- **De 3.000** → `minfreq = 10` o más

Si sale vacío, bajarlo. Si sale una maraña ilegible, subirlo. Se ajusta mirando,
no se acierta a la primera, y **eso se le dice** para que no crea que lo hizo mal.

---

## La cocitación tarda muchísimo o se queda colgada

Es la más pesada de todas: cruza las referencias de todos contra todos. Con un
corpus grande puede tardar minutos.

Si no termina, recortar:

```r
networkPlot(cocitacion, n = 20, ...)   # en vez de 30 o 50
```

Y recordar que **el Paso 7 es prescindible**. Muchas revisiones publicadas no
llevan cocitación. Si el equipo del investigador es lento, mejor un artículo sin
esa figura que un artículo sin terminar.

---

## No tiene R instalado, o no quiere instalarlo

**posit.cloud** — cuenta gratuita, se abre en el navegador, sube el archivo y
funciona igual. Sin instalar nada.

Es también la salida cuando la instalación falla por permisos, que en un
ordenador de universidad pasa a menudo.

---

## Regla de trato para todo este archivo

Cuando algo de esto falle, **el mensaje no puede empezar por «revisa que…»**. El
investigador ya está convencido de que la culpa es suya por no saber programar.

Se le dice qué pasó, se le da la línea corregida entera para pegar, y se sigue.
Nunca se le manda a resolverlo por su cuenta.
