# Búsqueda de antecedentes nacionales y locales

Los antecedentes locales son los más difíciles de encontrar porque rara vez están en Scopus o Web of Science. Suelen estar en repositorios universitarios y bases regionales. Esta referencia documenta dónde buscarlos y cómo hacer que entren a la biblioteca del tesista con su clave.

## Principio general

**Primero las herramientas de la biblioteca, después los repositorios.**

1. `buscar_fuentes` con `tema` en inglés, `temaOriginal` en español y `pais` del tesista: busca a la vez en la biblioteca de Acosta y en la suya, Zotero y Mendeley incluidos.
2. `buscar_en_la_literatura` con el tema en español y el `pais`: el catálogo abierto indexa SciELO, Redalyc y muchos repositorios latinoamericanos.
3. `ampliar_desde_mis_fuentes` cuando ya no sabe qué más buscar: trae lo que citan varias de sus fuentes.
4. En Perú, las tesis de ALICIA (RENATI): el tesista las busca en su perfil, «Tus herramientas» → «Tus fuentes de Scopus», en la parte de tesis peruanas (ALICIA), y las añade a su biblioteca con un clic, ya con clave.
5. Los repositorios de tesis por país (abajo), que muchas veces no están en el catálogo abierto: ahí busca el tesista con el tutorial, o la skill con `web_search` cuando va a declarar ausencia (Paso 3 del SKILL.md).

Nada entra al capítulo sin clave. Lo que tenga DOI se añade con `anadir_a_mis_fuentes`, con el permiso del tesista. Lo que no tenga DOI (la mayoría de tesis de repositorio) lo agrega el tesista a su Zotero, su Mendeley o «Mis fuentes» de su perfil, y después se busca de nuevo para tomar la clave.

Toda fuente que no venga de la biblioteca de Acosta se presenta diciendo su procedencia: las del catálogo abierto y las de la web no están revisadas por Acosta.

## Por país hispanohablante

### Perú

- **Renati** (sunedu.gob.pe/renati): repositorio nacional de tesis. Cubre pregrado, maestría y doctorado de todas las universidades peruanas reconocidas.
- **ALICIA** (alicia.concytec.gob.pe): repositorio nacional de investigación científica del Concytec. Incluye tesis y artículos.
- **SciELO Perú** (scielo.org.pe): revistas peruanas indexadas.
- **Repositorios institucionales** de la universidad del tesista y de las universidades vecinas (UNT, UPAO, UCV, USS, UNPRG, USMP, etc. según región).

### México

- **TESIUNAM** (tesiunam.dgb.unam.mx): tesis de la UNAM.
- **Red Mexicana de Repositorios Institucionales** (REMERI).
- **SciELO México**.

### Colombia

- **Renata** (renata.edu.co): red nacional académica.
- **Biblioteca Digital de Colombia**.
- **SciELO Colombia**.

### Chile

- **Memoria Académica** y repositorios institucionales por universidad.
- **SciELO Chile**.

### Argentina

- **SeDiCI** (sedici.unlp.edu.ar) y otros repositorios institucionales.
- **SciELO Argentina**.

### Ecuador

- **Repositorio Digital Senescyt**.
- **SciELO Ecuador**.

### Bolivia, Paraguay, Uruguay y Centroamérica

- Repositorios institucionales por universidad.
- SciELO regional cuando aplica.

### España

- **TESEO** (educacion.gob.es/teseo): base de datos de tesis doctorales.
- **DIALNET** (dialnet.unirioja.es): revistas, tesis, libros.
- **SciELO España**.

## Ecuación de búsqueda sugerida

Para repositorios nacionales (que rara vez aceptan operadores booleanos avanzados), usar **términos simples y combinaciones cortas**:

```
[variable 1] AND [población]
[variable 1] AND [ubicación]
[variable 1] [variable 2]
```

Ejemplo aplicado al caso de prueba:

```
inteligencia artificial estudiantes secundaria
ChatGPT educación secundaria
pensamiento crítico secundaria Perú
IA generativa adolescentes
```

Las mismas palabras en español son las que van en `temaOriginal` de `buscar_fuentes` y en el tema de `buscar_en_la_literatura`.

## Tutorial paso a paso para el tesista

La skill puede entregarle al tesista este micro-tutorial:

```
1. Entra a [URL del repositorio nacional según país].
2. En el buscador, prueba con esta ecuación primero:
   "[tu variable 1] [población]"
3. Filtra por:
   · Año: últimos 5 años
   · Tipo: tesis de pregrado, maestría o doctorado
   · Modalidad: completa (no solo resúmenes)
4. Descarga el PDF si lo tiene disponible y léelo.
5. Repite con 2-3 ecuaciones alternativas.
6. Agrega a tu biblioteca las que te sirvan:
   · si tienen DOI, pásame el DOI y la agrego yo;
   · si no, agrégala a tu Zotero o tu Mendeley (y pulsa
     «Actualizar ahora» en tu perfil) o cárgala en «Mis
     fuentes».
7. Avísame y la busco para tomar su clave.
```

## Regla crítica: si no hay antecedentes locales

Si después de las herramientas de la biblioteca y de buscar en al menos 3 repositorios distintos no aparecen antecedentes locales:

1. **La skill NO inventa** antecedentes locales.
2. **La skill NO declara** "no hay datos" prematuramente.
3. **La skill sugiere** ampliar criterios:
   - Buscar en regiones vecinas (no solo su ciudad).
   - Buscar tesis de los últimos 10 años, no solo 5.
   - Buscar variables relacionadas (no idénticas).
4. **Si tras estos ajustes sigue sin haber resultados**, redactar en el capítulo:
   > "La revisión de los principales repositorios nacionales y regionales no identificó antecedentes locales específicos sobre el tema en el periodo revisado, lo cual refuerza la pertinencia y novedad del presente estudio."

Esta declaración es académicamente válida y aporta al argumento de novedad.

## Si el antecedente es una tesis

Las tesis son válidas como antecedentes locales y nacionales. Algunos puntos a cuidar:

- **La ficha en su biblioteca debe tener como autor al tesista, no al asesor.** Si en su Zotero o su Mendeley figura el asesor, que lo corrija ahí.
- **El tipo de documento, el grado** (pregrado / maestría / doctorado), **la universidad y el repositorio** van en la ficha (en Zotero, tipo «Tesis»). Con eso el servidor escribe bien la referencia en la norma del proyecto.
- **Verificar que la tesis esté sustentada y aprobada**, no en borrador.

## Cómo llega cada fuente a la biblioteca

- **Con DOI**: la añade la skill con `anadir_a_mis_fuentes`, con el permiso del tesista y solo con DOI que vengan de una búsqueda.
- **Sin DOI**: el tesista la agrega a su Zotero o su Mendeley (manual, por ISBN o desde el navegador) o a «Mis fuentes».
- **Si el tesista pega en el chat la ficha y el resumen**, eso sirve para decidir si el estudio es pertinente, pero no para citarlo: primero tiene que entrar a la biblioteca.

## Si el tesista no quiere antecedentes locales

Es válido tener un Capítulo II sin antecedentes locales si:

- El tema es muy nuevo en el país.
- El estudio es exploratorio en su contexto.
- El reglamento de la universidad no los exige.

En estos casos, la skill omite la sub-sección 2.1.3 y deja constancia en 2.1.2 o en una nota final de 2.1.
