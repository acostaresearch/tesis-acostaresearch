---
name: tsp-fase3-experiencia
description: Capítulo III, Descripción de la experiencia, del Trabajo de Suficiencia Profesional (TSP) de Acosta | IA & Research. Es el corazón del TSP y ocupa el lugar de la metodología de una tesis. Entrevista al egresado sobre lo que de verdad hizo y lo redacta en orden con el diagnóstico de la situación inicial, la metodología o el enfoque de trabajo aplicado (método, norma, procedimiento), las actividades desarrolladas etapa por etapa con su cronograma, las herramientas y los recursos, y las dificultades con cómo se resolvieron. Une cada actividad con sus evidencias, que irán como anexos. No inventa actividades, fechas ni cifras. Guarda el capítulo y entrega el enlace del Word. ACTIVAR con "capítulo 3 del TSP", "descripción de la experiencia", "qué hice en la empresa", "desarrollo de la experiencia", "actividades realizadas".
---

# 3 · Capítulo III · Descripción de la experiencia

## Para qué sirve esta skill

Redacta el **Capítulo III**, el que el jurado lee con más atención: **qué hizo el egresado, cómo lo hizo y con qué**. En una tesis aquí iría la metodología de investigación; en un TSP va la experiencia contada de forma ordenada y verificable.

```
  Fase 0 · Tu experiencia y la empresa
  Fase 1 · Capítulo I · Introducción
  Fase 2 · Capítulo II · Marco teórico
  Fase 3 · Capítulo III · Descripción de la experiencia    ← estás aquí
  Fase 4 · Capítulo IV · Resultados
  Fase 5 · Capítulo V · Conclusiones y recomendaciones
```

Estructura por defecto:

```
3.1 Diagnóstico de la situación inicial
3.2 Metodología aplicada
3.3 Desarrollo de las actividades
    3.3.1 [Etapa u objetivo específico 1]
    3.3.2 [Etapa u objetivo específico 2]
    3.3.3 …
3.4 Herramientas y recursos utilizados
3.5 Dificultades y soluciones
```

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un .docx, un PDF ni ningún otro archivo del capítulo.** No usa la skill `docx` y no entrega archivos en el chat.

```
1. mi_proyecto        al abrir la conversación
2. ver_capitulo       tsp-fase0-experiencia, tsp-fase1-introduccion y
                      tsp-fase2-marco-teorico (`texto: true`); y este
                      capítulo si ya hay algo
3. mis_fuentes        si una actividad sigue una norma o un método citado
4. guardar_avance     metodología, actividades y herramientas, en cuanto
                      se fijen
5. guardar_capitulo   clave `tsp-fase3-experiencia`, apenas lo dé por bueno
6. revisar_evidencia  antes de entregar
7. enlace_del_word    cuando quiera el documento
```

**Las citas se marcan con la clave de la fuente:** `[AR…]`, `[AR…:n]`, `[FALTA FUENTE]`. En este capítulo se cita poco: la norma o el método que se siguió, y nada más. **Los datos de la empresa no llevan clave:** se nombra el documento de donde salen («según el kardex de enero de 2024») y en tablas y figuras lo dice la *Nota.*

**Entre corchetes, en el texto guardado, solo van** las claves, `[FALTA FUENTE]` y la marca de figura `[Insertar aquí la Figura N: archivo.png]`. Los avisos van en el chat.

**Si un guardado falla, se dice con esa palabra: no se guardó.**

El detalle está en `references/integracion_zotero.md`.

## Regla de oro: solo lo que pasó

1. **Las actividades las cuenta el egresado.** La skill pregunta, ordena y redacta; no rellena con actividades «típicas» de su cargo.
2. **Cada actividad, con su evidencia** o con la nota de que no la tiene. Lo que no se puede mostrar, el jurado lo pone en duda.
3. **Fechas y cifras, las suyas.** Si no las recuerda, se buscan en sus documentos; no se aproximan sin decirlo.
4. **Sin señalar personas** por su nombre cuando algo salió mal: se nombra el cargo o el área.
5. **La voz la decide su guía.** Muchas aceptan la primera persona al contar la experiencia («implementé», «coordiné»); otras piden impersonal («se implementó»). Pregúntalo una vez y mantenlo en todo el capítulo.

## Paso 1 — Leer lo acordado

Llama a `mi_proyecto` y lee con `ver_capitulo` (`texto: true`) la ficha `tsp-fase0-experiencia`, el capítulo `tsp-fase1-introduccion` (sobre todo los objetivos específicos) y el `tsp-fase2-marco-teorico` (lo aplicado y sus etapas).

Las etapas de 3.3 salen de ahí: **una por objetivo específico**, o una por etapa del método aplicado, lo que se entienda mejor. Propónselas y que elija.

Si ya hay texto de este capítulo (`capitulo: tsp-fase3-experiencia`), léelo y pregunta qué se corrige.

## Paso 2 — La entrevista

Antes de redactar, pregúntale en **dos tandas** (no todo de golpe), en texto libre:

**Tanda 1, el antes y el método:**
- ¿Cómo estaba el proceso o el área cuando empezaste? ¿Qué datos lo muestran?
- ¿Qué método, norma o enfoque seguiste? ¿Por qué ese y no otro?
- ¿Quién te encargó el trabajo y quién participó contigo?

**Tanda 2, para cada etapa:**
- ¿Qué hiciste exactamente, paso a paso?
- ¿Cuándo, y cuánto tiempo te tomó?
- ¿Con qué herramientas, equipos, software o formatos?
- ¿Qué evidencia tienes de esa etapa (reporte, foto, plano, acta, correo)?
- ¿Qué salió mal o costó más de lo previsto, y cómo lo resolviste?

Si responde con muy poco, repregunta lo concreto que falta. Guarda lo que se vaya fijando con `guardar_avance` (`capitulo: tsp-fase3-experiencia`, `estado: EN_CURSO`) y los `datos`: `metodologia`, `actividades` (lista, una por línea con su fecha) y `herramientas` (lista).

## Paso 3 — Diagnóstico de la situación inicial

**3.1** cuenta cómo estaba todo **antes**, con los datos de la empresa: el indicador que fallaba, cuánto, desde cuándo y por qué. Es la línea base contra la que el Capítulo IV mostrará los resultados, así que **las cifras de aquí tienen que ser las mismas que se usarán allí** como «antes».

Si usó una herramienta de diagnóstico (Ishikawa, Pareto, VSM, FODA, matriz de riesgos), va como figura o tabla con su marca y su *Nota.* Solo si la usó de verdad: un diagrama hecho para el informe que no guió ninguna decisión es relleno.

Entrega 3.1 y espera su visto bueno.

## Paso 4 — Metodología aplicada

**3.2** explica el **enfoque de trabajo**: el método, la norma o el procedimiento que siguió, con su clave si está en el Capítulo II, y **cómo lo adaptó** a la empresa. Cierra con una figura o tabla de las etapas, que es el mapa de 3.3:

```
**Tabla 2**
*Etapas de la implementación*
| Etapa | Actividades principales | Periodo | Evidencia |
|---|---|---|---|
| 1. Diagnóstico | Toma de tiempos, análisis de causas | Mar–abr 2024 | Anexo 2 |
| 2. Implementación | Clasificación y orden del almacén | May–jul 2024 | Anexo 3 |
*Nota.* Elaboración propia.
```

Aquí no van población, muestra, instrumentos ni técnicas de recolección: no es una investigación.

## Paso 5 — Desarrollo de las actividades

**3.3**, un subtítulo `###` por etapa. En cada uno, en prosa y en orden cronológico:

- Qué se hizo y para qué (qué objetivo específico atiende).
- Cómo: los pasos concretos, con quién y en cuánto tiempo.
- Con qué: herramientas, formatos, cálculos (si hay cálculos, el resultado se muestra en el Capítulo IV; aquí se dice qué se calculó y con qué).
- La evidencia: «(ver Anexo N)» o una figura con su marca.

Párrafos de 4 a 8 oraciones. Nada de listas de tareas sueltas: si su guía las pide, una tabla por etapa. Entrega **dos etapas por turno** y pregunta antes de seguir.

Las fotos, planos y capturas van como figuras:

```
**Figura 3**
*Almacén después de la etapa de orden*

[Insertar aquí la Figura 3: almacen-despues.jpg]

*Nota.* Fotografía tomada por el autor en julio de 2024.
```

## Paso 6 — Herramientas, dificultades y evidencias

**3.4 Herramientas y recursos utilizados:** software, equipos, formatos y personal, en una tabla corta o en prosa.

**3.5 Dificultades y soluciones:** dos a cuatro dificultades reales, cada una con lo que se hizo para resolverla. Es lo que más demuestra criterio profesional; no se omite ni se convierte en «todo salió bien».

Después, arma con él la **lista de evidencias** que irán como anexos (constancia de trabajo, reportes, actas, planos, fotos), en el orden en que se citan. No se guardan todavía: los anexos se fijan al final, en la Fase 5.

## Paso 7 — Guardar y entregar

1. **Guarda** con `guardar_capitulo`, clave `tsp-fase3-experiencia`. Markdown limpio: `##` para 3.1 a 3.5 y `###` para las etapas; **sin el título del capítulo**, sin portada y sin referencias. Hasta 30.000 caracteres por llamada; si pasa, por partes (la primera sin `anadir`, las siguientes con `anadir: true`), cortando entre etapas. Si la respuesta trae AVISOS DE REDACCIÓN, corrige esos párrafos con `reescribir_parrafos`.
2. **Comprueba** con `revisar_evidencia` (`capitulo: tsp-fase3-experiencia`).
3. **Registra** con `guardar_avance` (`capitulo: tsp-fase3-experiencia`): un `resumen` de dos o tres frases (método, etapas, periodo) y `estado: LISTO` solo si lo da por bueno.
4. **Da el enlace** con `enlace_del_word` y dile qué imagen va en cada marca de figura.

Cierre:

```
- [ ] Cada etapa tiene su evidencia anotada para los anexos.
- [ ] Las cifras del «antes» (3.1) son las que usaremos en Resultados.
- [ ] Revisa el capítulo con tu asesor y, si puedes, con tu jefe de entonces.
```

Lo siguiente es el **Capítulo IV, Resultados** (`tsp-fase4-resultados`).

## Lo que esta skill NO hace

- No inventa actividades, fechas, participantes ni cifras.
- No escribe población, muestra, instrumentos ni hipótesis.
- No presenta los resultados finales: eso es el Capítulo IV.
- No señala a personas por su nombre.

## Archivos de referencia

- `references/integracion_zotero.md` — Claves de cita, norma del proyecto y las herramientas de fuentes.
- `references/parafraseo.md` — Paráfrasis y patrones de escritura que delatan a la IA.
