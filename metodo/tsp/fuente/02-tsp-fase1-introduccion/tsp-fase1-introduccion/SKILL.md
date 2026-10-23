---
name: tsp-fase1-introduccion
description: Capítulo I, Introducción, del Trabajo de Suficiencia Profesional (TSP) de Acosta | IA & Research. Redacta la realidad problemática del sector y de la empresa con fuentes reales, la descripción de la empresa (datos generales, misión, visión, organigrama, productos o servicios), el cargo y las funciones del egresado, el problema, los objetivos general y específicos SIN hipótesis, y la justificación. Parte de la ficha de la experiencia guardada en la Fase 0. Cita solo con claves de la biblioteca del proyecto y no inventa datos de la empresa. Guarda el capítulo y entrega el enlace del Word que arma el servidor. ACTIVAR con "capítulo 1 de mi TSP", "introducción del TSP", "descripción de la empresa", "realidad problemática", "objetivos de mi suficiencia profesional".
---

# 1 · Capítulo I · Introducción

## Para qué sirve esta skill

Redacta el **Capítulo I** del Trabajo de Suficiencia Profesional. Es el capítulo que sitúa al jurado: qué empresa, qué problema tenía, qué papel tuvo el egresado y qué se propuso lograr con su experiencia.

```
  Fase 0 · Tu experiencia y la empresa
  Fase 1 · Capítulo I · Introducción             ← estás aquí
  Fase 2 · Capítulo II · Marco teórico
  Fase 3 · Capítulo III · Descripción de la experiencia
  Fase 4 · Capítulo IV · Resultados
  Fase 5 · Capítulo V · Conclusiones y recomendaciones
```

Estructura por defecto (la de la guía de la UPN, que sirve para casi todas las universidades):

```
1.1 Realidad problemática
1.2 Descripción de la empresa
    1.2.1 Datos generales
    1.2.2 Misión y visión
    1.2.3 Organigrama
    1.2.4 Productos o servicios
1.3 Descripción del cargo y funciones
1.4 Formulación del problema        (si su guía lo pide)
1.5 Objetivos
    1.5.1 Objetivo general
    1.5.2 Objetivos específicos
1.6 Justificación
```

**Sin hipótesis.** En un TSP no se contrasta nada: se cuenta y se demuestra lo que se hizo. Si su guía pide hipótesis, que lo diga; si no, no se ponen.

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un .docx, un PDF ni ningún otro archivo del capítulo.** No usa la skill `docx` y no entrega archivos en el chat. El Word lo arma el servidor con lo guardado: portada, índice, capítulos en orden y las referencias en la norma del proyecto.

```
1. mi_proyecto        al abrir la conversación (trae la norma de citas)
2. ver_capitulo       tsp-fase0-experiencia (la ficha), y este capítulo
                      con `texto: true` si ya hay algo guardado
3. buscar_fuentes     para la realidad problemática del sector
   / mis_fuentes
4. guardar_capitulo   clave `tsp-fase1-introduccion`, apenas lo dé por bueno
5. revisar_evidencia  antes de entregar
6. enlace_del_word    cuando quiera el documento
```

**Las citas se marcan con la clave de la fuente, no se escriben:**

```
…el sector creció 4,2 % en 2024 [AR97D22F86].
Según Hernández [AR97D22F86:n], …
[FALTA FUENTE]   cuando no hay respaldo
```

La skill **no escribe la cita** a mano, **no escribe la lista de referencias** y **no cita de memoria**. Solo usa claves que haya devuelto una búsqueda o la biblioteca.

**Los datos de la empresa no llevan clave:** se cuentan como lo que son, información de la empresa, y si salen de un documento interno se nombra («según el reporte de despachos de 2024»). En las tablas y figuras, la línea *Nota.* dice de dónde salen.

**Entre corchetes, en el texto guardado, solo van** las claves `[AR…]`, `[FALTA FUENTE]` y la marca de figura `[Insertar aquí la Figura N: archivo.png]`. Los avisos van en el chat.

**Si un guardado falla, se dice con esa palabra: no se guardó.**

El detalle está en `references/integracion_zotero.md`. **Leerlo antes de citar por primera vez** (con `redactar`, `referencia: "integracion_zotero.md"`).

## Regla del acompañamiento

- **Un paso por turno.** Se entrega por secciones, no el capítulo entero de golpe.
- **Lo de la empresa lo pone el egresado.** Misión, visión, organigrama, funciones y cifras salen de él o de los documentos de la empresa. Si no los tiene, se le dice dónde conseguirlos (web de la empresa, recursos humanos, su jefe); no se redactan «genéricos».
- **Prosa en tercera persona**, salvo que su guía pida primera persona para contar la experiencia. Párrafos de 4 a 8 oraciones.

## Paso 1 — Leer lo acordado

Llama a `mi_proyecto` y lee la ficha con `ver_capitulo` (`capitulo: tsp-fase0-experiencia`, `texto: true`). De ahí salen la empresa, el cargo, el periodo, la experiencia, el problema y las evidencias.

- **Sin ficha:** proponer hacer antes la Fase 0 con `redactar` (`tsp-fase0-experiencia`). Si insiste en seguir, pedirle esos datos en un solo mensaje.
- **Si ya hay texto de este capítulo,** léelo con `ver_capitulo` (`capitulo: tsp-fase1-introduccion`, `texto: true`) y pregunta qué se corrige.
- **Si su guía pide otra estructura de capítulos** (por ejemplo, un Capítulo I «Aspectos generales de la empresa» y un II «Fundamentación de la experiencia»), pídele la lista completa, repítesela y, cuando la confirme, fíjala con `estructura_de_la_tesis` usando las claves `tsp-fase1-introduccion`, `tsp-fase2-marco-teorico`, `tsp-fase3-experiencia`, `tsp-fase4-resultados` y `tsp-fase5-conclusiones`. La ficha `tsp-fase0-experiencia` nunca va en la estructura.

## Paso 2 — Los datos de la empresa y del cargo

Pídele en un solo mensaje lo que falte para 1.2 y 1.3:

- Razón social (o el nombre acordado), RUC si su guía lo pide, ubicación, año de fundación, rubro, tamaño (trabajadores, sedes).
- Misión y visión **tal como las tiene la empresa** (no se redactan nuevas).
- Organigrama: que lo describa o lo tenga en imagen; irá como figura.
- Productos o servicios principales y clientes.
- Su cargo, el área, a quién reportaba, desde cuándo, y sus **funciones** reales (cinco a ocho).

Si la empresa es confidencial, se usa el nombre acordado y se omiten RUC y datos que la identifiquen.

## Paso 3 — Fuentes para la realidad problemática

La realidad problemática va **de lo general a lo particular**: el sector en el mundo o la región, el sector en el Perú (o su país) y, al final, la empresa. Lo general se sostiene con fuentes; lo de la empresa, con sus datos.

1. Mira primero `mis_fuentes`: lo que ya tiene en su biblioteca.
2. Busca lo que falte con `buscar_fuentes` (el tema en español e inglés, y el país). Para cifras del sector sirven informes de organismos (INEI, ministerios, gremios, CEPAL, OIT) y artículos con datos.
3. Muéstrale las fuentes encontradas con su clave y elige con él cuáles usar. Entre 6 y 10 suele bastar para este capítulo.

**Ninguna cifra del sector sin clave.** Si no aparece una fuente para algo, la frase va con `[FALTA FUENTE]` y se le avisa en el chat.

## Paso 4 — Redactar 1.1, 1.2 y 1.3

**1.1 Realidad problemática.** Tres o cuatro movimientos, en prosa continua:

1. El problema en el sector, en el mundo o la región, con dato y clave.
2. El problema en el país, con dato y clave.
3. El problema en la empresa: qué pasaba, desde cuándo, cuánto costaba o qué afectaba, con los datos de la empresa.
4. Qué se hizo frente a eso: una o dos frases que anuncian la experiencia, sin contar todavía cómo (eso es el Capítulo III).

**1.2 Descripción de la empresa.** Datos generales en prosa o en una tabla corta; misión y visión entre comillas, tal cual; el organigrama como figura:

```
**Figura 1**
*Organigrama de la empresa*

[Insertar aquí la Figura 1: organigrama.png]

*Nota.* Tomado de la empresa (2025).
```

**1.3 Descripción del cargo y funciones.** Cargo, área, dependencia y periodo, y las funciones en prosa (o en lista si su guía lo pide). Una frase final que conecte el cargo con la experiencia elegida.

Entrega 1.1 primero y, cuando la apruebe, 1.2 y 1.3 juntas.

## Paso 5 — Problema y objetivos

**1.4 Formulación del problema**, solo si su guía la pide: un problema general en pregunta («¿Cómo reducir los tiempos de despacho en el almacén de…?») y, si la guía lo exige, dos a cuatro problemas específicos.

**1.5 Objetivos.** Son **lo que se logró con la experiencia**, no lo que se investigó:

- **Objetivo general:** verbo en infinitivo + qué se mejoró + dónde + cuándo. «Reducir los tiempos de despacho del almacén de la empresa X mediante la implementación de la metodología 5S, en 2024.»
- **Objetivos específicos:** dos a cuatro, uno por cada parte de la experiencia. Cada uno tendrá **su resultado en el Capítulo IV**: si no se puede mostrar un resultado para un objetivo, ese objetivo sobra. Verbos útiles: diagnosticar, diseñar, implementar, estandarizar, capacitar, evaluar, reducir, incrementar.

Cuando los apruebe, guárdalos con `guardar_avance` (`capitulo: tsp-fase1-introduccion`, `estado: EN_CURSO`) y los `datos`: `problemaGeneral`, `objetivoGeneral`, `objetivosEspecificos` (lista).

## Paso 6 — Justificación

**1.6 Justificación**, en tres o cuatro párrafos cortos, solo los que apliquen:

- **Práctica:** qué problema concreto resolvió en la empresa.
- **Económica:** ahorro, ingresos o costos evitados, si los hay y con su dato.
- **Social o ambiental:** a quién benefició fuera de la empresa, si aplica.
- **Profesional o académica:** qué demuestra de su formación y qué deja como referencia a otros profesionales.

Sin frases infladas («de vital importancia», «aporte invaluable»). Cada justificación, con un hecho.

## Paso 7 — Guardar y entregar

Antes de guardar, revisa con él que cada objetivo específico se pueda demostrar con lo que tiene (evidencias de la ficha). Después:

1. **Guarda** con `guardar_capitulo`, clave `tsp-fase1-introduccion`. Markdown limpio: `##` para 1.1 a 1.6 y `###` para sus partes; **sin el título del capítulo** (lo pone el Word), sin portada y sin referencias. Hasta 30.000 caracteres por llamada; si pasa, por partes: la primera sin `anadir` y las siguientes con `anadir: true`. Si la respuesta trae AVISOS DE REDACCIÓN, corrige esos párrafos con `reescribir_parrafos` antes de seguir.
2. **Comprueba** con `revisar_evidencia` (`capitulo: tsp-fase1-introduccion`) y dile qué afirmaciones quedaron sin fuente.
3. **Registra** con `guardar_avance` (`capitulo: tsp-fase1-introduccion`): un `resumen` de dos o tres frases y `estado: LISTO` solo si lo da por bueno.
4. **Da el enlace** con `enlace_del_word`:

```
Tu Capítulo I quedó guardado. Aquí está tu trabajo en Word: [enlace]

Sale con portada, índice y las referencias en [norma]. El organigrama
no va dentro: pégalo donde dice [Insertar aquí la Figura 1: …] y borra
la marca. El enlace vence a la media hora; si pasó, pídeme otro.
```

## Paso 8 — Cierre

```
- [ ] Revisa con tu asesor el problema y los objetivos antes de seguir.
- [ ] Confirma misión, visión y organigrama con la empresa.
- [ ] Cada objetivo específico tiene evidencias para el Capítulo IV.
```

Lo siguiente es el **Capítulo II, Marco teórico** (`tsp-fase2-marco-teorico`).

## Lo que esta skill NO hace

- No plantea hipótesis ni variables, salvo que su guía lo exija y él lo pida.
- No inventa misión, visión, organigrama, funciones ni cifras de la empresa.
- No cuenta todavía cómo se hizo la experiencia: eso es el Capítulo III.
- No escribe referencias ni arma el Word.

## Archivos de referencia

- `references/integracion_zotero.md` — Claves de cita, norma del proyecto y las herramientas de fuentes.
- `references/parafraseo.md` — Paráfrasis y patrones de escritura que delatan a la IA.
