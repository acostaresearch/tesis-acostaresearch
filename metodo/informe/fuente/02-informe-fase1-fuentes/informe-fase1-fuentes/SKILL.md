---
name: informe-fase1-fuentes
description: Segunda fase de la Ruta del Informe de Acosta | IA & Research, para informes de curso y de empresa. Junta lo que va a sostener el informe antes de redactar. En un curso consigue las fuentes y enseña a distinguir una confiable de una que no se cita. En una empresa junta además los datos internos (revisa periodo, fecha de corte, origen y si están completos) y busca en organismos oficiales, reguladores, gremios y normas con su número y año. Busca en la biblioteca de Acosta, en la propia (Zotero y Mendeley incluidos), en el catálogo abierto y en la web oficial, deja elegir y guarda las elegidas con su clave. Termina con la tabla de qué sostiene cada subtítulo y, en empresa, las limitaciones: qué dato no llegó y qué deja de poder afirmarse. No redacta. ACTIVAR con "fuentes para mi informe", "puedo usar Wikipedia", "busca bibliografía", "ya tengo los datos de la empresa", "de dónde saco las cifras del sector", "me falta información para el informe".
---

# Fase 1 — Las fuentes

## Para qué sirve esta skill

Es la segunda fase de la **Ruta del Informe**. Junta lo que va a sostener el informe **antes**
de redactar.

```
  Fase 0 · El encargo
  Fase 1 · Las fuentes y la evidencia      ← estás aquí
  Fase 2 · El desarrollo
  Fase 3 · Análisis y resultados
  Fase 4 · Cierre: conclusiones, recomendaciones y revisión
```

**Qué ámbito es:** si `mi_proyecto` dice «Ámbito: empresa», es de empresa; si no lo dice, es de
curso. Algunos pasos son de un solo ámbito y lo dicen en su título: se saltan en el otro.

| Ámbito | Qué se junta |
|---|---|
| **Curso** | Fuentes: libros, artículos, organismos. Y se le enseña qué se puede citar |
| **Empresa** | **Dos evidencias:** los datos internos de la empresa y las fuentes externas (oficiales, sectoriales, normas) |

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un archivo de Word, un PDF ni ningún otro archivo del informe.**

Las fuentes se guardan en la biblioteca del proyecto y cada una tiene una clave `[AR…]`. Al
armar el Word, el servidor convierte cada clave en su cita y su referencia, en la norma del
proyecto. **Los datos internos de una empresa no son fuentes de la biblioteca:** se citan por su
documento y su fecha de corte.

```
1. mi_proyecto          al abrir (ficha: ámbito, tipo, fuentes mínimas)
2. ver_capitulo         capitulo: informe-fase0-encargo (esquema, pregunta
                        guía o decisión, alcance)
3. material_del_curso   empresa: para que suba los datos que llegaron
4. mis_fuentes          lo que ya tiene
5. buscar_fuentes /     buscar; la fuente nace atada a su clave
   buscar_en_la_literatura
6. web_search           organismos oficiales, normas, reguladores, gremios
7. anadir_a_mis_fuentes solo las que apruebe
8. guardar_avance       clave `informe-fase1-fuentes`
```

Esta fase no escribe texto del informe, así que no usa `guardar_capitulo`. El detalle de
claves, búsquedas, fuentes sin DOI y cómo se cita un dato interno está en
`references/integracion_zotero.md`. **Leerlo antes de buscar** (con `redactar`,
`referencia: "integracion_zotero.md"`).

## Regla del acompañamiento

- **Un paso por turno.** Preguntas según `references/estilo_preguntas.md`.
- **Instrucciones literales** para lo que haga fuera del chat: en qué menú de su perfil,
  qué botón.
- **Sin sermón:** explicar por qué una fuente no sirve en una línea, con un ejemplo.
- **Empresa:** un dato que dijo que no tiene no se vuelve a pedir. Se anota como limitación.

## Regla de oro: veracidad

1. **Una fuente se cita por lo que dice su resumen o su texto.** Lo que no se ha leído no se
   le atribuye.
2. **Ninguna fuente de memoria.** Solo las que devuelve una búsqueda o la biblioteca.
3. **Ninguna clave inventada.** Sin clave, `[FALTA FUENTE]` y aviso.
4. **Una cifra se cita de quien la midió**, no de quien la repite. Si no se encuentra quién la
   midió, no entra.
5. **Empresa:** no se estima un dato que la empresa tiene y no entregó; un dato interno que no
   cuadra no se corrige en silencio: se pregunta; una norma va con número y año; lo que el
   cliente cree de su competencia es percepción.

## Lo que esta skill NO hace

- **No redacta.** Eso es la Fase 2.
- **No calcula.** Los cálculos con los datos son la Fase 3.
- **No guarda fuentes sin permiso.** `anadir_a_mis_fuentes` solo con su visto bueno.
- **No da por buena una fuente del catálogo abierto sin decir de dónde viene.**
- **No pide datos personales** que el informe no necesita (`references/confidencialidad.md`).

## Paso 1 — Leer lo acordado

`mi_proyecto` y `ver_capitulo` con `capitulo: informe-fase0-encargo`. De ahí salen el ámbito,
el tipo, la pregunta guía o la decisión, el esquema, el alcance y, en curso, cuántas fuentes
pide la rúbrica.

**Si la Fase 0 no tiene esquema guardado,** decírselo y ofrecer volver a la Fase 0: buscar sin
saber para qué apartado es buscar a ciegas.

Cuántas fuentes externas, si nadie lo dijo:

| Tipo | Fuentes orientativas |
|---|---|
| Informe de curso | 6 a 10 |
| Proyecto | 3 a 6 |
| Caso | 4 a 8 |
| Empresa: gestión | 0 a 3 (es todo interno) |
| Empresa: diagnóstico, técnico | 5 a 12 |
| Empresa: estudio de mercado, factibilidad | 10 a 30 |

## Paso 2 — Los datos internos (solo empresa)

Repasar la lista de datos por pedir que quedó en el resumen de la Fase 0 y preguntar qué llegó.
Lo que llegó, que lo suba con `material_del_curso` —Word, PDF, Excel o texto— o, si es una
matriz de datos que habrá que calcular, que la deje para `trabajar_en_r` en la Fase 3.

**De cada archivo se pregunta lo mismo**, con `references/datos_internos.md`:

1. Qué periodo cubre y cuál es la fecha de corte.
2. De qué sistema salió, o si se llevó a mano.
3. Qué significan las columnas que no se entiendan.
4. Si está completo: meses que faltan, sedes que no están, **cambios de sistema en el periodo**.

Y se revisa antes de darlo por bueno: meses en cero en medio de un año con actividad,
duplicados, totales que no cuadran con lo que dijo la gerencia, la misma cifra distinta en dos
fuentes internas. **Lo que aparezca se le pregunta; no se corrige por cuenta propia.**

Antes de que suba nada, la regla del dato mínimo: si los archivos traen nombres, sueldos
individuales o datos de clientes, ofrecer anonimizar (`references/confidencialidad.md`).

**Lo que no llegó** se anota tal cual, con lo que deja de poder afirmarse. No se estima.

## Paso 3 — Qué sirve y qué no

**Curso**, con `references/fuentes_confiables.md`:

| Sí se cita | No se cita |
|---|---|
| Libros y capítulos con autor y editorial | Wikipedia (sirve para orientarse, no para citar) |
| Artículos de revistas académicas | Blogs, Monografías.com, Brainly, Scribd sin autor |
| Informes de organismos (INEI, OIT, CEPAL, ministerios) | Respuestas de ChatGPT u otra IA |
| Normas y leyes, en su fuente oficial | Apuntes o diapositivas sin autor |
| Tesis de repositorios universitarios | Videos sin fuente verificable |
| Las lecturas que dejó el docente | Páginas que venden algo |

**Empresa**, con `references/fuentes_de_empresa.md`:

| Sí | No | Con cuidado |
|---|---|---|
| INEI, BCRP, SUNAT, ministerios, reguladores | Blogs y notas de LinkedIn | Agregadores de pago: citan a un tercero, y se cita el tercero |
| Gremios y cámaras del sector | Cifras sin quién las midió | Notas de prensa: valen para un hecho, no para una cifra |
| Normas vigentes, con número y año | Lo que dijo una IA | Informes de consultoras: diciendo de quién son y de cuándo |
| Memorias anuales y estados financieros públicos | Resúmenes y trabajos de terceros | Lo que el cliente cree de su competencia: es percepción |

Si ya trae fuentes de las que no se citan, decirle cuál y por qué, y buscar un reemplazo.

## Paso 4 — Las palabras clave

A partir del esquema, una tabla de términos en español y en inglés por subtítulo. Enseñársela
y pedirle que añada los términos que usa su curso o su sector.

| Subtítulo | En español | En inglés |
|---|---|---|
| 1. Causas de la informalidad | informalidad laboral, empleo informal | informal employment, labor informality |

**Si el docente dejó lecturas o la empresa dio documentos de referencia,** entran primero.

## Paso 5 — Buscar

En este orden:

1. `mis_fuentes`: lo que ya tiene, Zotero y Mendeley incluidos.
2. `buscar_fuentes` con `tema` en inglés, `temaOriginal` en español y `pais`, por subtítulo.
3. `buscar_en_la_literatura` con el tema en español y `pais`, para fuentes del país.
4. `web_search` para **organismos oficiales, normas, reguladores y gremios**. En empresa es la
   búsqueda principal; se comprueba que el sitio es de quien dice ser y se anota el año del
   dato. Estas fuentes no tienen DOI: ver «Fuentes sin DOI» en `integracion_zotero.md`.

Presentar como mucho **seis por subtítulo**, cada una con: título, autor u organismo y año, de
dónde viene (Acosta, su biblioteca, catálogo abierto o web oficial) y en una línea qué aporta.

**Empresa, si el informe toca algo regulado** (laboral, tributario, seguridad, ambiental,
sanitario, protección de datos): qué norma aplica, **con número y año**, de dónde se leyó, y si
no se pudo comprobar que sigue vigente, se anota para decirlo en el informe.

## Paso 6 — Elegir

```
¿Cuáles guardamos para tu informe?
· Todas las que marqué como útiles
· Elijo yo (dime los números)
· Ninguna, busquemos otras
```

- Las que tienen DOI y no están en su biblioteca: `anadir_a_mis_fuentes` con sus `dois`.
- Las de organismos sin DOI: explicarle cómo tenerlas con clave (su Zotero, su Mendeley o «Mis fuentes») y
  que avise cuando estén; mientras, se anotan como pendientes en el chat.

## Paso 7 — Qué aporta cada una

**Curso:**

| Clave | Fuente | Qué dice | Para qué subtítulo |
|---|---|---|---|
| [AR97D22F86] | OIT (2023) | 71 % de empleo informal en Perú | 1. Causas |

**Empresa**, con las dos evidencias en la misma tabla:

| Evidencia | Interna o externa | De dónde salió | A qué sección sirve |
|---|---|---|---|
| Órdenes de despacho, 12 meses | Interna | Sistema de despacho, corte 31-03-2026 | 4. Situación actual |
| Tiempo de ciclo del sector | Externa | Gremio logístico [AR…] | 7. Brecha con el sector |

«Qué dice» sale del resumen o del texto de la fuente, no de lo que se espera que diga.

## Paso 8 — Cobertura y limitaciones

Contar lo que sostiene cada subtítulo. **Un subtítulo sin respaldo se avisa ahora**, no al
redactar:

```
El subtítulo «3. Consecuencias en la salud» no tiene ninguna fuente.
· Busquemos más para ese subtítulo
· Lo quito o lo junto con otro
· Lo dejo: ahí va mi opinión (se dirá que es opinión)
```

En empresa, la tercera salida es «sale como comparación sin cifra, y se dice en las
limitaciones».

Si el total no llega al mínimo de la rúbrica, decirlo con el número.

**Empresa: las limitaciones.** Redactar ya el párrafo que irá en el informe, con la forma de
`references/datos_internos.md`: qué dato no se tuvo, por qué, y **qué deja de poder afirmarse
por eso**. Se cierra en la Fase 4.

## Paso 9 — Guardar y seguir

`guardar_avance` con `capitulo: informe-fase1-fuentes`:

- `datos.cobertura`: «subtítulo — N fuentes» (o «N evidencias»), uno por elemento;
- `resumen`: las claves elegidas por subtítulo, lo que quedó pendiente y, en empresa, los datos
  que llegaron con su fecha de corte y **las limitaciones**, una por línea;
- `estado: LISTO` solo si da la evidencia por buena.

Cierre:

```
Tus fuentes quedaron guardadas: [N] en total, y todos los subtítulos
tienen respaldo. Siguiente paso: redactar el desarrollo (Fase 2).
```

## Errores que esta skill previene

1. Un informe citado con Wikipedia, blogs o una respuesta de IA.
2. Descubrir al redactar que un apartado no tiene ni una fuente.
3. Atribuirle a un autor algo que su texto no dice.
4. Citas escritas de memoria con el año equivocado.
5. Una cifra oficial sin su organismo ni su año.
6. Menos fuentes de las que pide la rúbrica.
7. Empresa: una cifra de mercado repetida de una nota de prensa que no la midió.
8. Empresa: un reporte en PDF ya resumido, que en la Fase 3 no se puede recalcular.
9. Empresa: comparar dos periodos entre los que hubo un cambio de sistema.
10. Empresa: citar una norma sin número, o una derogada.
11. Empresa: entregar sin limitaciones escritas.

## Archivos de referencia

- `references/estilo_preguntas.md` — Cómo se pregunta en esta ruta, según el ámbito.
- `references/integracion_zotero.md` — Claves, búsquedas, fuentes sin DOI y cómo se cita un dato interno.
- `references/fuentes_confiables.md` — Curso: qué se cita y qué no, con ejemplos.
- `references/fuentes_de_empresa.md` — Empresa: fuentes oficiales y sectoriales, dónde buscar y cuántas.
- `references/datos_internos.md` — Empresa: qué datos pedir por tipo, en qué formato y qué revisar de cada archivo.
- `references/confidencialidad.md` — El dato mínimo y cómo anonimizar.
