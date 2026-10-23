---
name: tsp-fase2-marco-teorico
description: Capítulo II, Marco teórico, del Trabajo de Suficiencia Profesional (TSP) de Acosta | IA & Research. Redacta los antecedentes (experiencias y estudios parecidos, nacionales e internacionales), las bases teóricas de lo que el egresado APLICÓ en su trabajo (métodos, herramientas de gestión, normas técnicas, teorías de su especialidad) y la definición de términos. Más corto que el de una tesis: sostiene la experiencia, no una hipótesis. Busca y cita solo fuentes reales con clave de la biblioteca del proyecto, su Zotero y su Mendeley incluidos. Guarda el capítulo y entrega el enlace del Word. ACTIVAR con "marco teórico de mi TSP", "capítulo 2 de suficiencia profesional", "antecedentes del TSP", "bases teóricas".
---

# 2 · Capítulo II · Marco teórico

## Para qué sirve esta skill

Redacta el **Capítulo II** del TSP. Su trabajo es mostrar que lo que el egresado hizo en la empresa **se apoya en conocimiento de su especialidad**: otros resolvieron problemas parecidos (antecedentes), y lo que él aplicó tiene un sustento teórico o técnico (bases teóricas).

```
  Fase 0 · Tu experiencia y la empresa
  Fase 1 · Capítulo I · Introducción
  Fase 2 · Capítulo II · Marco teórico           ← estás aquí
  Fase 3 · Capítulo III · Descripción de la experiencia
  Fase 4 · Capítulo IV · Resultados
  Fase 5 · Capítulo V · Conclusiones y recomendaciones
```

Estructura por defecto:

```
2.1 Antecedentes
    2.1.1 Antecedentes internacionales
    2.1.2 Antecedentes nacionales
2.2 Bases teóricas
    2.2.1 [Lo aplicado 1: método, herramienta o norma]
    2.2.2 [Lo aplicado 2]
2.3 Definición de términos básicos
```

**La diferencia con una tesis:** aquí no se sustentan variables ni dimensiones para medir. Se sustenta **lo que se aplicó**: si implementó 5S, la teoría de 5S; si diseñó una estructura, la norma técnica que siguió; si mejoró un proceso contable, el marco normativo y el método. Por eso es más corto: entre 8 y 15 páginas suele bastar, salvo que su guía diga otra cosa.

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un .docx, un PDF ni ningún otro archivo del capítulo.** No usa la skill `docx` y no entrega archivos en el chat.

```
1. mi_proyecto        al abrir la conversación (trae la norma de citas)
2. ver_capitulo       tsp-fase0-experiencia y tsp-fase1-introduccion
                      (`texto: true`); y este capítulo si ya hay algo
3. mis_fuentes        lo que ya tiene en su biblioteca, su Zotero y su Mendeley incluidos
4. buscar_fuentes     antecedentes y teoría que falten
   / buscar_en_la_literatura / ampliar_desde_mis_fuentes
5. guardar_capitulo   clave `tsp-fase2-marco-teorico`, apenas lo dé por bueno
6. revisar_evidencia  antes de entregar
7. enlace_del_word    cuando quiera el documento
```

**Las citas se marcan con la clave de la fuente, no se escriben:** `[AR97D22F86]` al final de la afirmación, `[AR97D22F86:n]` detrás del nombre del autor, `[AR97D22F86:p. 45]` con página, y `[FALTA FUENTE]` cuando no hay respaldo. Nunca la cita escrita a mano ni la lista de referencias, y nunca una fuente de memoria.

**Las normas técnicas y legales** (una NTP, el Reglamento Nacional de Edificaciones, una ley, una NIC) también se citan con clave: se buscan o se añaden a su biblioteca con `anadir_a_mis_fuentes`. Si no se puede, `[FALTA FUENTE]` y se le avisa.

**Entre corchetes, en el texto guardado, solo van** las claves, `[FALTA FUENTE]` y la marca de figura. Los avisos van en el chat.

**Si un guardado falla, se dice con esa palabra: no se guardó.**

El detalle está en `references/integracion_zotero.md`. **Leerlo antes de citar por primera vez** (con `redactar`, `referencia: "integracion_zotero.md"`).

## Regla del acompañamiento

- **Un paso por turno.** Antecedentes, bases y términos se entregan por separado.
- **Parafrasear siempre.** Cita textual solo si es imprescindible, corta y con página. Las reglas están en `references/parafraseo.md`.
- **Tercera persona, prosa continua.** Nada de listas de autores uno debajo de otro.

## Paso 1 — Leer lo acordado

Llama a `mi_proyecto` y lee con `ver_capitulo` (`texto: true`) la ficha `tsp-fase0-experiencia` y el capítulo `tsp-fase1-introduccion`. De ahí saca:

- **Qué aplicó** el egresado (métodos, herramientas, normas): será cada subtítulo de 2.2. Si no está claro, pregúntaselo ahora: «¿Qué método, herramienta o norma usaste para resolverlo?».
- Los objetivos específicos, para que la teoría responda a ellos.

Si ya hay texto de este capítulo, léelo (`capitulo: tsp-fase2-marco-teorico`) y pregunta qué se corrige. Sin Capítulo I guardado, se puede seguir, pero avísale que los objetivos aún no están fijados.

## Paso 2 — Las fuentes

1. `mis_fuentes`: lo que ya tiene. Dile cuántas hay y de qué tratan.
2. Para **antecedentes**, busca con `buscar_fuentes` o `buscar_en_la_literatura` experiencias o estudios donde se aplicó lo mismo en un contexto parecido (mismo sector o mismo problema), de los últimos cinco a siete años si su guía lo pide. Sirven también tesis y trabajos de suficiencia de repositorios universitarios.
3. Para **bases teóricas**, busca los autores de referencia de cada método o herramienta, y las normas que aplicó.
4. Si tiene una buena fuente, `ampliar_desde_mis_fuentes` encuentra las que la citan o que ella cita.

Muéstrale lo encontrado con su clave y elige con él. Cantidad orientativa: **4 a 6 antecedentes** (la mitad internacionales y la mitad nacionales) y **2 a 4 fuentes por cada base teórica**.

## Paso 3 — Antecedentes

Cada antecedente, en un párrafo de 5 a 7 oraciones con estos elementos, sin orden fijo y sin que todos los párrafos suenen igual:

- Autor y año (con la marca `:n` si el autor se nombra), y dónde se hizo.
- El problema que atendieron.
- Qué aplicaron y cómo.
- El resultado, con su cifra si la hay.
- **Qué le sirve al TSP:** en qué se parece o se diferencia de la experiencia del egresado.

Ordénalos del más lejano al más cercano (internacionales, después nacionales), y dentro de cada grupo por año. Entrega 2.1 completa y espera su visto bueno.

## Paso 4 — Bases teóricas

Un subtítulo `###` por cada cosa que aplicó. Para cada una, en prosa:

1. **Qué es**, con la definición de un autor de referencia.
2. **Sus componentes, etapas o principios** (las 5S, las fases del PDCA, los requisitos de la norma), con su fuente.
3. **Cómo se aplica** en la práctica, según la literatura.
4. **Por qué encaja** con el problema de la empresa: una o dos frases que unan la teoría con la experiencia, sin contar todavía lo que hizo (eso es el Capítulo III).

Si ayuda, una tabla con los componentes:

```
**Tabla 1**
*Etapas de la metodología 5S*
| Etapa | En qué consiste |
|---|---|
| Clasificar (Seiri) | Separar lo necesario de lo innecesario [AR…] |
| Ordenar (Seiton) | Un lugar para cada cosa [AR…] |
*Nota.* Elaborado a partir de Hirano [AR…:n].
```

Las figuras de modelos teóricos van con la marca `[Insertar aquí la Figura N: archivo.png]`.

## Paso 5 — Definición de términos básicos

Entre 8 y 12 términos que usa el trabajo y que un lector de otra especialidad no conocería. Cada uno en un párrafo corto: el término en **negrita** al inicio, su definición parafraseada con clave. Sin listas con viñetas. En orden alfabético si su guía lo pide.

## Paso 6 — Guardar y entregar

1. **Guarda** con `guardar_capitulo`, clave `tsp-fase2-marco-teorico`. Markdown limpio: `##` para 2.1 a 2.3 y `###` para sus partes; **sin el título del capítulo**, sin portada y sin referencias. Hasta 30.000 caracteres por llamada; si pasa, por partes (la primera sin `anadir`, las siguientes con `anadir: true`), cortando entre secciones y nunca dentro de una tabla. Si la respuesta trae AVISOS DE REDACCIÓN, corrige esos párrafos con `reescribir_parrafos`.
2. **Comprueba** con `revisar_evidencia` (`capitulo: tsp-fase2-marco-teorico`) qué afirmaciones quedaron sin fuente, y díselo.
3. **Registra** con `guardar_avance` (`capitulo: tsp-fase2-marco-teorico`): un `resumen` de dos o tres frases (antecedentes por nivel, bases desarrolladas) y `estado: LISTO` solo si lo da por bueno.
4. **Da el enlace** con `enlace_del_word` y recuérdale que las referencias salen solas, en una sola lista para todo el trabajo, en la norma del proyecto.

## Paso 7 — Cierre

```
- [ ] Revisa en el Word que cada cita tenga su referencia correcta.
      Si una ficha está mal, corrígela en tu Zotero, tu Mendeley o Mis fuentes.
- [ ] Cada cosa que aplicaste en la empresa tiene su base teórica.
- [ ] Llévale el capítulo a tu asesor.
```

Lo siguiente es el **Capítulo III, Descripción de la experiencia** (`tsp-fase3-experiencia`): el corazón del TSP.

## Lo que esta skill NO hace

- No sustenta variables ni dimensiones para un instrumento: un TSP no los tiene.
- No cuenta lo que hizo el egresado en la empresa: eso es el Capítulo III.
- No cita de memoria ni escribe referencias a mano.

## Archivos de referencia

- `references/integracion_zotero.md` — Claves de cita, norma del proyecto y las herramientas de fuentes.
- `references/parafraseo.md` — Paráfrasis y patrones de escritura que delatan a la IA.
