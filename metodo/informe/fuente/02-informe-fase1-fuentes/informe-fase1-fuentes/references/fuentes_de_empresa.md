# Qué fuente externa se cita en un informe empresarial

Un informe de curso se sostiene en artículos y libros. Uno de empresa se sostiene en **datos
oficiales, normas y datos del sector**, y cita poca academia. Esa es la diferencia principal.

## Cuatro preguntas para cualquier fuente

1. **¿Quién midió el dato?** No quién lo repite: **quién lo midió**. Una nota de prensa que
   dice «según un estudio, el mercado crece 8 %» no es la fuente: la fuente es el estudio.
2. **¿De cuándo es?** Con fecha, y para cifras, de los últimos tres años. Un dato de 2019
   sirve para el contexto, no para sostener una proyección.
3. **¿Qué mide exactamente?** «Ventas del sector» puede ser facturación, unidades o valor
   FOB. Si no se sabe qué mide, no se usa.
4. **¿Para qué se publicó?** Informar o regular, no vender. Un informe de mercado de quien
   vende ese mercado se cita diciendo quién lo pagó.

Si falla una de las cuatro, se busca otra.

## Sí, no, y con cuidado

| Sí se cita | No se cita | Con cuidado |
|---|---|---|
| Organismos oficiales: INEI, BCRP, SUNAT, MEF, MINCETUR, PRODUCE, MTPE | Blogs y notas de LinkedIn | Agregadores de pago (Statista y similares): **citan a un tercero; se cita el tercero** |
| Reguladores y supervisores: SBS, SMV, OSIPTEL, OSINERGMIN, SUNASS, INDECOPI | Cifras «de mercado» sin quién las midió | Notas de prensa: valen para un hecho con fecha, no para una cifra |
| Gremios y cámaras: SNI, COMEXPERÚ, cámaras de comercio, asociaciones del sector | Lo que dijo una IA | Informes de consultoras: sí, diciendo de quién son y de cuándo |
| Normas técnicas y legales vigentes, con número y año | Trabajos de estudiantes, resúmenes, Monografías, Scribd | Wikipedia: sirve para orientarse y para llegar a la fuente del pie. Se cita el pie |
| Memorias anuales y estados financieros públicos de empresas del sector | Foros y grupos | Encuestas de medios: se mira la ficha técnica antes |
| Organismos internacionales: Banco Mundial, CEPAL, OIT, OCDE, FAO, OMS | Comparaciones «de mercado» sin fuente | Datos de portales inmobiliarios o de precios: sirven como referencia, se dice que son de oferta y no de transacción |
| Artículos y libros, para el marco conceptual y los métodos | Precios que alguien «escuchó» | Datos del propio cliente sobre su competencia: son percepción, y así se escriben |

## Dónde buscar, por lo que se necesita

| Qué se necesita | Dónde |
|---|---|
| Población, hogares, empleo, pobreza, empresas por tamaño | INEI |
| Tipo de cambio, inflación, tasas, PBI por sector, expectativas | BCRP |
| Recaudación, importaciones y exportaciones por partida, contribuyentes | SUNAT |
| Producción y empresas por sector | PRODUCE, MINCETUR, MINAGRI según el sector |
| Normas y leyes | El Peruano, SPIJ, la página del regulador |
| Sueldos y planillas del mercado | MTPE, y encuestas salariales del sector |
| Precios de insumos y de referencia | Bolsas y gremios del producto; SEACE para compras del Estado |
| Estados financieros de empresas | SMV para las que reportan; memorias anuales |
| Empresas y su situación | Consulta RUC de SUNAT, Registros Públicos |
| Comparaciones del sector, artículos, métodos | `buscar_fuentes` y `buscar_en_la_literatura` |

Lo que se encuentre ahí se guarda en Zotero, en Mendeley o en «Mis fuentes» para que tenga clave: el detalle
está en `integracion_zotero.md`.

## El caso que más aparece: «el mercado vale X»

Es la cifra que más se inventa y la que más se pide. Tres formas de escribirla, de mejor a
peor:

1. **Con la fuente que la midió:** «el mercado de transporte de carga por carretera movió
   US$ 1 240 millones en 2024 [AR…]».
2. **Calculada, con el método a la vista:** «con 2 800 empresas formales del sector y un
   ticket promedio de S/ 18 000 al mes (facturación de la empresa y del gremio [AR…]), el
   mercado estaría en unos S/ 600 millones al año. Es una estimación propia, no un dato
   medido.»
3. **Dicho que no se sabe:** «no se encontró una medición del tamaño de este mercado; el
   informe trabaja con la demanda de la zona de influencia, que sí se pudo estimar.»

**La cuarta forma, inventar una cifra redonda, no existe en esta ruta.** El método de cálculo
está en `tamano_de_mercado.md`, en la Fase 3.

## Cuando la fuente que hace falta no existe

Pasa seguido: sectores chicos, mercados informales, datos que nadie publica. Lo que se hace,
en este orden:

1. **Buscar el dato más cercano** y decir que es cercano: el del sector que lo contiene, el
   del país en vez del de la región, el del año anterior.
2. **Sustituirlo por un dato propio:** la empresa sí tiene su facturación, sus clientes y sus
   precios.
3. **Dejarlo como limitación**, en la lista de la Fase 1 que se cierra en la Fase 4.

Y se dice en el informe cuál de las tres se usó.

## Cómo se presenta cada fuente al cliente

```
PROCEDENCIA              CÓMO SE PRESENTA
───────────────────────  ─────────────────────────────────────
Organismo oficial        Con su nombre y el año del dato.
                         Sin advertencia.

Biblioteca de Acosta     Con criterio editorial. Sin advertencia.

Su propia biblioteca     Las eligió él. No están revisadas por
                         Acosta: se dice al presentarlas.

Catálogo abierto         Indexa de todo, también preprints. Se
                         advierte siempre y se le dan a ELEGIR.

Web (buscador)           Se dice de qué sitio salió y de cuándo,
                         y se comprueba que el sitio es de quien
                         dice ser.
```

## Cuántas fuentes externas

No hay mínimo académico. Lo que manda es la cobertura:

| Tipo de informe | Fuentes externas habituales |
|---|---|
| Gestión / resultados | 0 a 3. Puede no llevar ninguna: es todo interno |
| Diagnóstico | 5 a 12: la referencia del sector y las normas que aplican |
| Técnico | 3 a 10, casi todas normas y especificaciones |
| Auditoría interna | Las del criterio: la norma, la política, el contrato |
| Estudio de mercado | 10 a 25 |
| Factibilidad | 15 a 30 |

**Un informe de gestión con veinte citas académicas está mal.** No es un trabajo de curso: si
las cifras son de la empresa, las fuentes externas sobran.
