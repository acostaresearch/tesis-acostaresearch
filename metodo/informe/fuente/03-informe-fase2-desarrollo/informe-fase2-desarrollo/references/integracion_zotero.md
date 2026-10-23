# Citar con la biblioteca del proyecto (Zotero y Mendeley incluidos)

## La regla que ordena todo lo demás

**Las citas no se escriben: se marcan con la clave de la fuente.**

Cada fuente de la biblioteca del proyecto tiene una clave del tipo `[AR2E15C80C]`. Al
redactar, la skill pone esa clave en el texto. Al armar el Word, **el servidor** la
convierte en cita y en entrada de la lista de referencias, en la norma del proyecto.

- **La skill no escribe la cita** en texto ni la lista de referencias.
- **La skill no arma el Word.** Uno hecho por la skill saldría con las claves impresas
  como corchetes y sin norma.
- **La skill no cita de memoria.** Los datos que no salen de una búsqueda suelen traer el
  año o el autor equivocados, y quien lee lo nota: un docente, y más aún un gerente que
  conoce su sector.

## Las marcas

```
Al final de la afirmación:
   …la informalidad laboral supera el 70 % [AR97D22F86].

Cuando el autor o el organismo ya va nombrado en la frase:
   Porter [AR97D22F86:n] propone que…

Con página, para la cita textual:
   «…» [AR97D22F86:p. 45]

Varias fuentes para la misma afirmación:
   …en las mypes de Lima [AR97D22F86][AR2E15C80C].

Cuando no hay fuente que respalde la afirmación:
   [FALTA FUENTE]
```

**Solo se usan claves que haya devuelto una búsqueda o la biblioteca.** Una clave
recordada no existe: el servidor no la encuentra y en el Word sale un aviso de cita sin
localizar.

**La `:n` sigue al nombre del autor.** Si el nombre sale de la frase, la marca pierde la
`:n` y va al final de la afirmación.

## Ámbito empresa: dos evidencias que no se citan igual

Un informe de empresa se sostiene sobre todo en **datos de la propia empresa**, y esos no son
fuentes de la biblioteca:

| Evidencia | Ejemplo | Cómo se cita |
|---|---|---|
| **Externa** | INEI, BCRP, una norma, un artículo, un informe del sector | Con su clave `[AR…]`, como cualquier fuente |
| **Interna** | La base de ventas, la planilla, un acta, una entrevista | **En el texto y en la línea «Fuente:» de la tabla.** Sin clave y sin entrar a la lista de referencias |

Confundirlas es el error de citas más común del ámbito empresa. Cómo se cita un dato interno:

```
En el texto, la primera vez:
   Las ventas del trimestre fueron de S/ 1 842 300, según el reporte de
   facturación entregado por el área comercial el 3 de abril de 2026.

En la tabla, siempre:
   *Fuente.* Reporte de facturación, área comercial, al 31 de marzo de 2026.

De una entrevista:
   El jefe de almacén señaló que las devoluciones se registran a mano desde
   2024 (entrevista del 12 de marzo de 2026).
```

- **Con fecha de corte.** «Las ventas» sin fecha no se puede comprobar.
- **Con quién lo entregó**, por área o cargo, no por nombre.
- **Si el documento está subido**, se lee con `material_del_curso`; si lo subió como documento
  del proyecto, `ver_mi_documento` y `citar_mi_documento` dan la referencia exacta.

Y dos marcas más que solo existen en este ámbito:

```
Cuando falta un dato que tiene que dar la empresa:
   [FALTA DATO: costo unitario de 2025]

Cuando algo lo tiene que confirmar quien encargó el informe:
   [POR CONFIRMAR CON LA EMPRESA: presupuesto disponible]
```

**Una norma se cita con su número y su año**, o no se cita: «el Decreto Supremo 011-2019-TR
[AR…]», nunca «la normativa vigente». Si no se pudo comprobar que sigue vigente, se dice.

## Qué puede ir entre corchetes en el texto que se guarda

Solo:

- las claves de cita `[AR…]`, con o sin `:n` / `:p. N`;
- `[FALTA FUENTE]`;
- en el ámbito empresa, `[FALTA DATO: …]` y `[POR CONFIRMAR CON LA EMPRESA: …]`;
- la marca de figura `[Insertar aquí la Figura N: nombre-del-archivo.png]`.

Todo lo demás se dice **en el chat**, no dentro del informe. Tampoco va dentro del informe
una sección «Referencias» escrita a mano: el servidor pone la suya al final y saldría
repetida.

## La norma de citas

Es una sola para todo el informe y vive en el proyecto:

1. Mirar la línea «Norma de citas» que devuelve `mi_proyecto`.
2. Si ya está elegida, no se vuelve a preguntar.
3. Si dice «sin elegir»:
   - **curso:** se toma la que diga la consigna del docente; si no dice nada, se pregunta una
     vez;
   - **empresa:** se queda en APA 7, que es con la que el servidor arma la lista, y se dice en
     una línea. Solo se cambia si la empresa o el cliente piden otra.

   Se guarda con `guardar_avance`, campo `estiloCitas`.

Nada se convierte ni se numera a mano: si piden otra norma, se cambia en el proyecto y el Word
sale entero en la nueva.

## De dónde salen las fuentes

```
HERRAMIENTA                    CUÁNDO
─────────────────────────────  ──────────────────────────────────
mis_fuentes                    Ver lo que ya tiene.
                               origen: "zotero", "mendeley"
                               o "subidas".

buscar_fuentes                 La búsqueda de todos los días: la
                               biblioteca de Acosta y la suya a la
                               vez. Manda SIEMPRE tema (en inglés),
                               temaOriginal (en español) y pais.

buscar_en_la_literatura        Catálogo abierto (OpenAlex). Para
                               fuentes en español y del país:
                               SciELO, Redalyc, repositorios.

ampliar_desde_mis_fuentes      Qué trabajos citan varias de sus
                               fuentes y él no tiene.

anadir_a_mis_fuentes           Guarda por DOI las que apruebe y les
                               da clave. PREGÚNTALE ANTES.

revisar_evidencia              Qué afirmaciones tienen fuente y
                               cuáles no. Antes de entregar.

web_search / web_fetch         Organismos oficiales, normas, gremios
                               y reguladores: lo que no tiene DOI.
```

Si falta `temaOriginal` en `buscar_fuentes`, su Zotero y su Mendeley quedan fuera de la búsqueda.

## Fuentes sin DOI: sitios oficiales, normas, libros del curso

INEI, OIT, BCRP, un ministerio, un gremio, una norma técnica o el libro que dejó el docente no
suelen tener DOI, así que `anadir_a_mis_fuentes` no los puede guardar. En un informe de empresa
**son la mayoría de las fuentes**. Cómo tenerlos con clave:

- **Con Zotero:** guardar la página o el libro en su Zotero (el conector del navegador lo
  hace con un clic), y en su perfil de acostaresearch.com, «Tu Zotero» → «Actualizar ahora».
- **Con Mendeley:** lo mismo en su Mendeley, y en su perfil «Tu Mendeley» → «Actualizar
  ahora». Vale igual que Zotero: no se le pide que se cambie.
- **Sin gestor:** en su perfil, «Mis fuentes».

Mientras la fuente no tenga clave, la afirmación va con `[FALTA FUENTE]` y se le dice en el
chat cuál es. **La cifra no se escribe sin fuente aunque sea correcta.**

## Decir de dónde viene cada fuente

```
PROCEDENCIA              CÓMO SE PRESENTA
───────────────────────  ─────────────────────────────────────
Organismo oficial        Con su nombre y el año del dato.
                         Sin advertencia.

Biblioteca de Acosta     Con criterio editorial. Sin advertencia.

Biblioteca propia        Las eligió él. No están revisadas por
                         Acosta: se dice al presentarlas.

Catálogo abierto         Indexa de todo, también preprints. Se
                         advierte siempre y se le dan a ELEGIR.
```

## Qué hacer cuando no hay fuente

Se marca `[FALTA FUENTE]` y se le dice en qué afirmación quedó. **Nunca** se inventa una
fuente, ni se estira una que dice otra cosa, ni se atribuye a un organismo una cifra que no
publicó.

## Las demás herramientas del perfil

En su perfil de acostaresearch.com, la sección **«Tus herramientas»** tiene más de lo que
muchos saben. Cuando una le ahorra trabajo en el paso en que está, **se le dice en una línea**,
sin recorrerlas todas.

```
PESTAÑA                        PARA QUÉ / CUÁNDO MENCIONARLA
─────────────────────────────  ──────────────────────────────────
Tus fuentes de Scopus          Buscar en Scopus, SciELO y las
                               tesis peruanas de ALICIA y añadir
                               a su biblioteca con un clic. Al
                               buscar estudios del sector.

Tu Zotero / Tu Mendeley        Conectar su gestor de referencias.
                               Cuando ya lleva sus fuentes en uno,
                               o hay que guardar una fuente sin
                               DOI.

Tu análisis en R               Datos numéricos (encuesta, ventas,
                               indicadores): lo corre Claude con
                               trabajar_en_r. Sube su Excel o CSV
                               por el enlace que da la
                               herramienta. No instala nada.

Tu ATLAS.ti                    Entrevistas o grupos focales: lo
                               hace Claude con analisis_
                               cualitativo, sin instalar ni pagar
                               ATLAS.ti. El .qdpx es opcional.

Mapa en VOSviewer              Mapas bibliométricos hechos en la
                               web paso a paso. Rara vez hacen
                               falta en un informe: solo si piden
                               un estado del arte.
```

Lo que hace Claude va por las herramientas del conector; lo que hace él en la web se le indica
con el nombre exacto de la pestaña. Una imagen hecha en la web entra como figura, con su marca
`[Insertar aquí la Figura N: nombre-del-archivo.png]`.
