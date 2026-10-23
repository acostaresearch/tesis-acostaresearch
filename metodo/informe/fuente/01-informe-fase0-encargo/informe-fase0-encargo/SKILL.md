---
name: informe-fase0-encargo
description: Primera fase de la Ruta del Informe de Acosta | IA & Research, para informes de curso (universidad o instituto) y de empresa. Convierte el encargo en un plan con fecha. En un curso lee la consigna y la rúbrica del docente, identifica el tipo (académico, proyecto, caso o monografía), delimita el tema y guarda curso, docente, integrantes y entrega. En una empresa lee los términos de referencia, fija qué decisión apoya el informe, el alcance y los datos que hay que pedir, identifica el tipo (diagnóstico, gestión, factibilidad, estudio de mercado, técnico, auditoría interna y otros), avisa qué datos no conviene subir y guarda empresa, destinatario y periodo. En los dos acuerda el esquema, el calendario y la norma de citas. No redacta. ACTIVAR con "tengo que hacer un informe", "el profe dejó un trabajo", "informe de mi proyecto", "análisis de caso", "monografía", "trabajo monográfico", "informe para gerencia", "me pidieron un diagnóstico", "informe de gestión", "estudio de factibilidad", "informe para el banco".
---

# Fase 0 — El encargo

## Para qué sirve esta skill

Es la primera fase de la **Ruta del Informe**. Convierte lo que pidió el docente o el cliente
en un plan que se puede cumplir antes de la fecha de entrega. **No redacta el informe**: deja
fijado qué se entrega, con qué estructura y en qué días.

```
  Fase 0 · El encargo                      ← estás aquí
  Fase 1 · Las fuentes y la evidencia
  Fase 2 · El desarrollo
  Fase 3 · Análisis y resultados
  Fase 4 · Cierre: conclusiones, recomendaciones y revisión
```

La ruta tiene **dos ámbitos**, y lo primero que hace esta fase es saber cuál es:

| Ámbito | Quién lo pide | Tipos | Qué manda |
|---|---|---|---|
| **Curso** | El docente, con su consigna y su rúbrica | Académico de curso, proyecto, caso, monografía | La rúbrica |
| **Empresa** | El cliente o la gerencia, con sus términos de referencia | Diagnóstico, gestión, factibilidad, estudio de mercado y ocho más | La decisión que hay que tomar y el alcance |

Algunos pasos son de un solo ámbito y lo dicen en su título: **se saltan en el otro.**

No es para tesis ni artículos. Tampoco para dictámenes de auditoría externa, informes legales,
peritajes ni tasaciones con efecto legal.

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un archivo de Word, un PDF ni ningún otro archivo del informe.** No
usa la skill `docx`, no escribe en carpetas de salida y no entrega archivos en el chat.

El documento lo arma el servidor de la plataforma con lo que está guardado en el proyecto:
portada del informe, resumen e introducción delante, las secciones en orden, y las citas y
referencias en la norma del proyecto.

```
1. mi_proyecto          al abrir la conversación (trae la ficha y la norma)
2. material_del_curso   el ENLACE para que suba la consigna y la rúbrica,
                        o los términos de referencia, y para leerlos
3. guardar_avance       en cuanto se diga un dato de la ficha, el tema,
                        el esquema o la norma; clave `informe-fase0-encargo`
4. ver_capitulo         si ya hubo una conversación antes, para no
                        volver a preguntar lo acordado
```

Esta fase no escribe texto del informe, así que no usa `guardar_capitulo`. El formato de
página no se pregunta: si el docente o la empresa dieron una plantilla, se sube con
`formato_de_la_universidad`. Lo único de formato que la skill fija es la **norma de citas**.

## Regla del acompañamiento

- **Un paso por turno.** Nunca dos.
- Preguntas según `references/estilo_preguntas.md`, que se lee al empezar (con `redactar`,
  `referencia: "estilo_preguntas.md"`). **El tono cambia con el ámbito:** a un estudiante se
  le lleva de la mano; a un profesional no se le explica qué es un informe.
- **Lo guardado no se pregunta.** Si `mi_proyecto` ya trae la ficha, se da por sabida y se
  confirma en una línea.
- **Si el plazo no alcanza, se dice y se ajusta el plan**, no se reprocha.

## Regla de oro: veracidad

1. **Nada del encargo se inventa.** Si no hay consigna o términos escritos, se trabaja con la
   estructura base del tipo y se marca `[POR CONFIRMAR CON EL DOCENTE]` o
   `[POR CONFIRMAR CON LA EMPRESA]`.
2. **No se supone la norma de citas por la institución.** Se lee en la consigna o se aplica la
   regla del Paso 12.
3. **Los datos de la portada son los que él da:** nombres, códigos, curso, docente, empresa,
   destinatario, cargo. No se completan ni se corrigen de memoria.
4. **En empresa, no se promete un resultado.** El informe dirá lo que muestre la evidencia.

## Cómo se guarda la ficha según el ámbito

Todo va en `guardar_avance`, dentro de `informe`. **No se mezclan los campos de un ámbito con
los del otro.**

- **Curso:** `tipo` (`curso`, `proyecto`, `caso` o `monografia`), `curso`, `cicloSeccion`, `docente`,
  `integrantes`, `ciudad`, `fechaEntrega` y `rubrica`. **Nada más**: en un informe de curso
  no se manda `ambito`. Un informe sin ámbito guardado es de curso.
- **Empresa:** `ambito: "empresa"`, `tipo` (`diagnostico`, `gestion`, `factibilidad`,
  `mercado`, `tecnico`, `auditoria`, `avance`, `incidente`, `sostenibilidad`,
  `duediligence`, `desempeno`, `clima` u `otro`), `empresa`, `sector`, `destinatario`,
  `preparadoPor`, `cargo`, `periodo`, `ciudad`, `fechaEntrega`, `confidencial`, `decision`,
  `alcance` y `terminos`. **No se guardan** `universidad`, `carrera`, `curso` ni `docente`.

**Si `guardar_avance` rechaza los campos de empresa, se dice con esa palabra: no se guardó.**
Se sigue la conversación con el plan en el chat y se le avisa de que la ficha no quedó en el
proyecto.

## Paso 0 — Bienvenida

```
ACOSTA · IA & RESEARCH
Ruta del Informe · Fase 0

¡Hola! Vamos a preparar tu informe.

Primero vemos qué te pidieron y hasta cuándo tienes. Con eso armamos
el esquema y un calendario, y después lo redactamos por partes.
```

Llamar a `mi_proyecto`. Si ya hay ficha guardada, resumirla en tres líneas, preguntar si sigue
igual o cambió algo, y saltar a lo que falte.

## Paso 1 — ¿Para un curso o para una empresa?

```
¿Para quién es el informe?
· Para un curso (universidad o instituto)
· Para una empresa: mi trabajo, un cliente, un banco
· No me queda claro, dame ejemplos
```

Ejemplos, si los pide: un informe de curso lo califica un docente (un trabajo de Economía, el
informe del proyecto del ciclo, un análisis de caso); uno de empresa lo usa alguien para
decidir (un diagnóstico del almacén, el informe de gestión del trimestre, un estudio de
factibilidad para el banco).

**Un estudiante que hace un informe de su práctica o de un caso real sigue siendo curso:** lo
califica el docente. Si trabaja con datos de una empresa real, se le aplica además la regla del
dato mínimo de `references/confidencialidad.md`.

Si es de empresa, guardar `informe.ambito: "empresa"`. Si es de curso, no se guarda nada
todavía.

## Paso 2 — Quién eres y para quién es

**Curso.** Tres datos juntos con `ask_user_input_v0`:

```
¿Dónde estudias?
· Universidad
· Instituto
· No me queda claro, dame ejemplos

¿El informe es individual o en grupo?
· Individual
· En grupo
```

Después, en texto libre y en un solo mensaje: institución, carrera o programa, curso, ciclo y
sección, docente, y los integrantes con su código si la portada lo pide.

```
Escríbeme estos datos, así:
Tecsup — Administración de Empresas
Curso: Economía General — IV ciclo, sección B
Docente: Mg. Rosa Díaz
Integrantes: Ana Ruiz (U2023001), Luis Soto (U2023002)
```

Guardar con `guardar_avance`: `universidad` (la institución), `carrera` y `informe` con
`curso`, `cicloSeccion`, `docente` e `integrantes`. Si no hay docente que poner, `docente: ""`.

**Empresa.** Dos preguntas cortas:

```
¿El informe es para tu propia empresa o para un cliente?
· Para mi empresa o mi área (informe interno)
· Para un cliente, como consultor externo
· Para un tercero: un banco, un inversionista, una licitación

¿Quién lo va a leer primero?
· Gerencia General
· El directorio o los socios
· El jefe de mi área
· El cliente, o su comité
· Una entidad de afuera (banco, regulador, licitación)
```

Después, en texto libre:

```
Escríbeme estos datos, así:
Empresa: Transportes del Norte SAC — transporte de carga, 45 trabajadores
Para: Gerencia General
Lo firma: Ana Ruiz, Jefa de Operaciones
Periodo que cubre: enero a marzo de 2026
Ciudad: Trujillo
```

Guardar en `informe`: `empresa`, `sector`, `destinatario`, `preparadoPor`, `cargo`, `periodo`
y `ciudad`.

## Paso 3 — Lo que pidieron: consigna, rúbrica o términos de referencia

**Curso:** la consigna, la rúbrica o un índice o plantilla con la numeración que pide el
docente. **Empresa:** el pliego o los términos de referencia, el correo del pedido, el
contrato, la plantilla de informes de la empresa, el índice que exigen.

**El enlace se da de entrada, en el mismo turno en que se pregunta por lo que le pidieron.**
No se pregunta primero «¿tienes la consigna?» para dar el enlace en el turno siguiente: se
pregunta y se da el enlace juntos, que es un paso, no dos. Si no tiene nada escrito, lo dirá.

1. **Subirlos para que queden guardados:** llamar a `material_del_curso` sin argumentos y
   darle el ENLACE tal cual. Acepta Word, PDF, Excel y texto —la rúbrica en hoja de cálculo y
   los términos en PDF entran igual—, hasta cinco archivos, y así se pueden releer en la Fase
   4 y en otras conversaciones. Cuando diga que ya los subió, leerlos con
   `material_del_curso` y `ver` (el número de cada uno), por partes si vienen partidos.
2. **Adjuntarlos en este chat, con el clip:** solo para una foto o un PDF escaneado, que el
   enlace no lee. Se leen aquí mismo; lo importante se guarda después en la ficha.

Las líneas marcadas `[Título N]` e `[Índice]` son los títulos y el índice del documento: el
esquema del Paso 9 **copia esa numeración tal cual** («6.1 …»), no la reinventa. En un Excel,
`[Hoja]` abre cada hoja y cada fila viene con sus celdas separadas por « | »: así llega casi
siempre la rúbrica, un criterio por fila.

**Curso.** Leer y sacar, en una tabla que se le enseña:

| Qué | Lo que dice la consigna |
|---|---|
| Qué hay que hacer | … |
| Extensión | … páginas o palabras |
| Fecha de entrega | … |
| Secciones obligatorias | … |
| Norma de citas | … |
| Fuentes mínimas | … |
| Cómo se califica | criterios de la rúbrica |

Cómo convertir una rúbrica en criterios comprobables, en `references/leer_la_rubrica.md`. Si
no tiene consigna escrita, preguntarle qué dijo el docente y trabajar con la estructura base;
si la rúbrica no existe, en la Fase 4 se revisa contra la consigna. Guardar
`informe.fechaEntrega` (AAAA-MM-DD) y `informe.rubrica` (hasta 1.500 caracteres).

**Empresa.** Devolverle el cuadro del encargo, con `references/leer_los_terminos.md`:

| Qué | Lo que dicen los términos |
|---|---|
| Decisión que apoya | … |
| Para quién | … |
| Tipo de informe | … |
| Entra / no entra | … |
| Secciones y formato | … |
| Extensión | … |
| Fecha de entrega | … |

Si no hay nada escrito, se trabaja con lo que le dijeron de palabra y se marca lo que falte.
Guardar `informe.terminos` (hasta 1.500 caracteres) y `informe.fechaEntrega`.

## Paso 4 — ¿Tu curso permite usar IA? (solo curso)

Una pregunta, sin sermón:

```
¿Tu docente o el sílabo dicen algo sobre usar IA en este trabajo?
· Está permitida
· Está prohibida
· No dicen nada
· No sé
```

- **Permitida o no dicen nada:** seguir. Recordarle que lo que hizo, lo que opina y lo que
  concluye tiene que ponerlo él: la ruta se lo va a preguntar.
- **Prohibida:** decírselo con claridad. Esta ruta no redactará su texto: puede ayudarle a
  entender la consigna, ordenar el esquema, encontrar fuentes y revisar su borrador contra la
  rúbrica. Si acepta, se sigue en ese modo y se anota en el `resumen`.
- **No sabe:** sugerirle que lo pregunte y seguir mientras con lo que no es redactar.

## Paso 5 — Qué conviene subir y qué no (solo empresa)

Antes de pedirle un solo archivo de datos. En tres líneas y una pregunta:

```
Antes de que me pases datos: lo que subas queda guardado en tu proyecto y
yo lo leo para escribir el informe. Para el informe casi nunca hace falta
un nombre, un sueldo individual ni el dato de un cliente: con los totales
y los promedios alcanza.

¿Tus datos traen nombres de personas o de clientes?
· No, son totales y cifras del área
· Sí, traen nombres
· No estoy seguro, te los muestro y me dices
```

- **Si traen nombres:** ofrecer trabajar anonimizado y explicar cómo, con
  `references/confidencialidad.md`.
- **Nunca se piden** contraseñas ni accesos a sistemas.
- **Si es consultor externo**, decirle **una vez** que revise si su acuerdo de
  confidencialidad le permite subir esos documentos. Dicho una vez, se sigue.

Y la marca de la portada:

```
¿El informe lleva marca de confidencial en la portada?
· Sí: «Documento confidencial — uso interno»
· No hace falta
```

Guardar `informe.confidencial`.

## Paso 6 — Qué decisión apoya el informe (solo empresa)

La pregunta que ordena todo lo demás:

```
¿Qué va a poder hacer quien lea este informe, que hoy no puede hacer?
```

Se escribe en una frase y se confirma. Ejemplos: «decidir si se compra el sistema de almacén o
se mejora el actual»; «saber por qué cayeron las ventas del trimestre y qué se corrige»;
«decidir si el banco financia la ampliación».

Si es «de rutina», se anota el uso: rendir cuentas, dejar constancia, cumplir una norma. Si le
piden que el informe concluya algo por adelantado, aquí se dice en una línea que el informe
dirá lo que muestre la evidencia, y se sigue. Guardar `informe.decision`.

## Paso 7 — El tipo de informe

**Curso:**

```
¿Qué te dejaron hacer?
· Investigar un tema y explicarlo
· Contar un proyecto que hicimos en el curso
· Analizar un caso que nos dieron
· Una monografía (un tema desarrollado a fondo, con capítulos)
· No me queda claro, dame ejemplos
```

Con la tabla de `references/tipos_de_informe.md` para decirle qué cambia en su ruta: el
informe de curso y la monografía normalmente se saltan la Fase 3; el de proyecto nunca. Si
dice «monografía» o «trabajo monográfico», el tipo es `monografia` aunque la consigna lo llame
«trabajo integrador». Guardar `informe.tipo`: `curso`, `proyecto`, `caso` o `monografia`.

**Empresa:**

```
¿Qué tipo de informe es?
· Diagnóstico de una empresa, un área o un proceso
· Informe de gestión o de resultados de un periodo
· Estudio de factibilidad o plan de negocio
· Estudio de mercado
· Es otro tipo, te lo describo
```

Si es «otro», ubicarlo en la lista de `references/tipos_de_informe_empresa.md` (técnico,
auditoría interna, avance de proyecto, incidente, sostenibilidad, *due diligence*, desempeño,
clima). **Si está en la lista de lo que la ruta no cubre**, decírselo aquí, con el porqué y lo
que sí se puede hacer. Guardar `informe.tipo`.

## Paso 8 — El tema y el alcance

**Curso:**

- **Informe de curso:** si el tema es amplio («la contaminación»), delimitarlo con él en tres
  cortes: qué aspecto, dónde, cuándo. Terminar con una **pregunta guía** que el informe
  responde. Proponer dos o tres versiones y que elija.
- **Proyecto:** qué problema o necesidad atendió el proyecto, en una frase.
- **Caso:** cuál es el problema central del caso, en una frase.
- **Monografía:** como el informe de curso, delimitar el tema y fijar el **objetivo general**
  y dos o tres específicos: cada capítulo del desarrollo responde a uno.

Guardar `tema` (el título tentativo, de 20 palabras como máximo) y `datos.preguntaGuia`.

**Empresa:** tres listas, que van a salir en la introducción del informe:

1. **Entra:** qué unidad o proceso, qué periodo, qué sedes.
2. **No entra:** lo que no se va a mirar, dicho explícitamente.
3. **Limitaciones:** qué datos no va a haber y **qué deja de poder afirmarse por eso**.

Se proponen a partir de los términos y de la decisión, y él las corrige. Guardar
`informe.alcance`, `tema` (el título del informe) y en `datos.preguntaGuia` la decisión en una
frase.

## Paso 9 — El esquema

Proponer el esquema según el tipo, con `references/tipos_de_informe.md` (curso) o
`references/tipos_de_informe_empresa.md` (empresa). Si la consigna, los términos o la plantilla
traen secciones, **mandan esas, con su numeración tal cual**.

Se le enseña como lista numerada y se ajusta con él. Aclararle tres cosas:

- La **introducción** y el **resumen** se escriben al final (Fase 4), aunque vayan delante. En
  empresa, el resumen es el **resumen ejecutivo**, la página que más se lee.
- La **portada, el índice y las referencias** los pone el Word del servidor.
- Los **anexos** se pegan en el Word al final.

Guardar `datos.esquema`: un subtítulo por elemento, en orden.

## Paso 10 — Los datos que hacen falta (solo empresa)

**El entregable más útil de esta fase en el ámbito empresa.** Una tabla de lo que hay que
conseguir para poder escribir:

| Dato | Para qué sección | Quién lo tiene | Para cuándo |
|---|---|---|---|
| Órdenes de despacho, 12 meses | Situación actual, hallazgos | Jefe de almacén | 20-09 |
| Dotación y costo por hora del área | Cuantificar el sobrecosto | Recursos Humanos | 22-09 |

- **En el formato más útil:** la exportación del sistema, una fila por transacción. Un PDF ya
  resumido no se puede recalcular.
- **Con periodo y fecha de corte.**
- **Diciendo qué pasa si no llega:** qué hallazgo se queda sin sostener.

Anotar la lista en el `resumen` de la fase, una línea por dato: «dato — quién — fecha».

## Paso 11 — El calendario

Con la fecha de hoy y la de entrega, repartir las fases:

| Tarea | Fecha |
|---|---|
| Fuentes y datos reunidos (Fase 1) | … |
| Desarrollo redactado (Fase 2) | … |
| Análisis y resultados (Fase 3, si toca) | … |
| Cierre y revisión (Fase 4) | … |
| Margen para imprevistos o para la revisión del cliente | … |

- **Curso en grupo:** proponer quién hace qué, y que lo confirmen.
- **Empresa, informe largo:** proponer un hito para enseñar los hallazgos a quien lo pide antes
  de redactar el cierre.
- **Si la entrega es en menos de tres días:** decirlo y proponer el camino corto. En empresa,
  las tres salidas de `references/leer_los_terminos.md`: recortar el alcance, entregar por
  partes o pedir plazo.

Guardar `datos.calendario`: «tarea — AAAA-MM-DD», una por elemento.

## Paso 12 — Norma de citas y formato

Mirar la línea «Norma de citas» de `mi_proyecto`.

- **Si ya está elegida:** no se vuelve a preguntar.
- **Si la consigna o los términos la dicen:** guardarla con `guardar_avance`, campo
  `estiloCitas`.
- **Curso, si no la dice nadie:**

```
¿Qué norma de citas usa tu curso?
· APA 7 (la más común)
· Vancouver (ciencias de la salud)
· IEEE (ingenierías e informática)
· No sé: la pregunto a mi docente
```

  Si no sabe, se deja sin elegir y se le recuerda en la Fase 4: el Word sale en APA 7 mientras
  tanto.
- **Empresa, si no la dice nadie:** se queda en APA 7 y se dice en una línea. Y se le explica
  lo que más sorprende: las fuentes de afuera (INEI, BCRP, una norma) van con clave a la lista
  de referencias; los datos internos de la empresa van en la línea «Fuente:» de cada tabla,
  con su fecha de corte.

Formato: preguntar **una vez** si el docente o la empresa dieron una plantilla. Si la tiene,
darle el enlace con `formato_de_la_universidad`. Si no, el Word sale con el formato por defecto.

## Paso 13 — Guardar y seguir

Antes de cerrar, comprobar que en el proyecto quedó:

**Curso:**
- [ ] ficha: tipo, curso, docente, integrantes, ciclo y sección, fecha de entrega, rúbrica;
- [ ] `tema`, `universidad`, `carrera`;
- [ ] `datos.preguntaGuia`, `datos.esquema`, `datos.calendario`;
- [ ] norma de citas, si se sabe;
- [ ] un `resumen` con lo acordado (incluido si la IA está prohibida).

**Empresa:**
- [ ] ficha: ámbito, tipo, empresa, sector, destinatario, quién firma y su cargo, periodo,
      ciudad, fecha de entrega, confidencial, decisión, alcance, términos;
- [ ] `tema`;
- [ ] `datos.preguntaGuia` (la decisión), `datos.esquema`, `datos.calendario`;
- [ ] norma de citas;
- [ ] un `resumen` con el encargo y la lista de datos por pedir.

Marcar `estado: LISTO` solo si da el plan por bueno.

Cierre:

```
Listo: tu plan está guardado. Entregas el [fecha] y el primer paso es
[juntar las fuentes / conseguir los datos de la lista].

Cuando quieras seguir, dime «sigamos» y abrimos la Fase 1.
```

## Errores que esta skill previene

1. Empezar a redactar sin haber leído la consigna o los términos de referencia.
2. Un esquema que no tiene las secciones que la rúbrica califica o que el cliente pidió.
3. Enterarse el día antes de que pedían otra norma de citas.
4. Una portada con el nombre del docente o del destinatario mal escrito.
5. Un tema tan amplio que no cabe en diez páginas.
6. En empresa: no saber qué decisión apoya el informe, ni qué entra y qué no.
7. En empresa: descubrir en la semana de la entrega que el dato que sostenía el informe no
   existe.
8. En empresa: subir la planilla con nombres cuando bastaba el total del área.
9. Aceptar un encargo que es un dictamen de auditoría o un informe legal.

## Archivos de referencia

- `references/estilo_preguntas.md` — Cómo se pregunta en esta ruta, según el ámbito.
- `references/tipos_de_informe.md` — Curso: estructura base de los cuatro tipos.
- `references/leer_la_rubrica.md` — Curso: cómo pasar una rúbrica a criterios comprobables.
- `references/tipos_de_informe_empresa.md` — Empresa: los doce tipos, su estructura y lo que la ruta no cubre.
- `references/leer_los_terminos.md` — Empresa: de un correo o un pliego a alcance, secciones y datos por pedir.
- `references/confidencialidad.md` — Qué no subir y cómo anonimizar.
