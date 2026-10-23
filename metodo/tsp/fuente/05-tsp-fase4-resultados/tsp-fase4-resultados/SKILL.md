---
name: tsp-fase4-resultados
description: Capítulo IV, Resultados, del Trabajo de Suficiencia Profesional (TSP) de Acosta | IA & Research. Muestra lo que logró la experiencia, objetivo por objetivo, con los indicadores de antes y después tomados de los datos de la empresa, en tablas y figuras APA. Los cálculos (variaciones, ahorros, promedios y, si hay datos suficientes, una prueba antes-después) se hacen en la sesión de R del servidor o los trae el egresado, nunca de cabeza, y las cifras se guardan para que el repaso detecte cualquier número que no salga de ahí. Cierra con el aporte profesional y un análisis breve frente a los antecedentes. Guarda el capítulo y entrega el enlace del Word. ACTIVAR con "resultados del TSP", "capítulo 4 de suficiencia profesional", "indicadores antes y después", "logros de mi experiencia".
---

# 4 · Capítulo IV · Resultados

## Para qué sirve esta skill

Redacta el **Capítulo IV** del TSP: la prueba de que la experiencia funcionó. Cada objetivo específico del Capítulo I recibe aquí su resultado, con datos.

```
  Fase 0 · Tu experiencia y la empresa
  Fase 1 · Capítulo I · Introducción
  Fase 2 · Capítulo II · Marco teórico
  Fase 3 · Capítulo III · Descripción de la experiencia
  Fase 4 · Capítulo IV · Resultados              ← estás aquí
  Fase 5 · Capítulo V · Conclusiones y recomendaciones
```

Estructura por defecto:

```
4.1 Resultados por objetivo
    4.1.1 [Objetivo específico 1]
    4.1.2 [Objetivo específico 2]
    4.1.3 …
4.2 Aporte profesional y beneficios para la empresa
4.3 Análisis de los resultados
```

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un .docx, un PDF ni ningún otro archivo del capítulo.** No usa la skill `docx` y no entrega archivos en el chat.

```
1. mi_proyecto        al abrir la conversación
2. ver_capitulo       tsp-fase1-introduccion (objetivos) y
                      tsp-fase3-experiencia (el «antes»), `texto: true`
3. trabajar_en_r      para los cálculos, si hay datos que calcular
   / guardar_analisis las cifras, con capítulo `tsp-fase4-resultados`
4. ver_analisis       para leer lo ya calculado
5. guardar_capitulo   clave `tsp-fase4-resultados`, apenas lo dé por bueno
6. revisar_evidencia  antes de entregar
7. enlace_del_word    cuando quiera el documento
```

**Las citas se marcan con la clave de la fuente:** `[AR…]`, `[AR…:n]`, `[FALTA FUENTE]`. Aquí solo se cita en 4.3, al comparar con los antecedentes. **Los datos de la empresa no llevan clave:** se dice de qué documento salen y la *Nota.* de cada tabla lo repite.

**Entre corchetes, en el texto guardado, solo van** las claves, `[FALTA FUENTE]` y la marca de figura. Los avisos van en el chat.

**Si un guardado falla, se dice con esa palabra: no se guardó.**

El detalle está en `references/integracion_zotero.md`.

## Regla de oro: ninguna cifra se escribe sola

1. **Cada número sale de un dato de la empresa o de un cálculo guardado.** Nada de «aproximadamente el 30 %» sin cuenta detrás.
2. **Los cálculos no se hacen de cabeza.** Se hacen en la sesión de R con `trabajar_en_r`, o los trae el egresado de su Excel y se guardan tal cual con `guardar_analisis`.
3. **El «antes» es el del Capítulo III.** Si la cifra de partida no coincide con la de 3.1, se aclara cuál es la buena y se corrige donde esté mal.
4. **Un resultado que no mejoró se cuenta igual,** con su explicación. Ocultarlo es lo que más descalifica un TSP en la sustentación.

## Paso 1 — Leer lo acordado

Llama a `mi_proyecto` y lee con `ver_capitulo` (`texto: true`) los objetivos de `tsp-fase1-introduccion` y el diagnóstico (3.1) y las etapas de `tsp-fase3-experiencia`. Si ya hay cifras guardadas, léelas con `ver_analisis`.

Arma con él la **tabla de correspondencia**: cada objetivo específico, su indicador y de dónde saldrá el dato.

| Objetivo específico | Indicador | Antes | Después | Fuente del dato |
|---|---|---|---|---|
| … | Tiempo promedio de despacho (h) | ? | ? | Sistema de despachos |

Si ya hay texto de este capítulo (`capitulo: tsp-fase4-resultados`), léelo y pregunta qué se corrige.

## Paso 2 — Los datos

Pídele los datos de antes y después de cada indicador, con su periodo y el documento de donde salen. Lo más útil es la serie (mes a mes, semana a semana); si solo tiene dos valores, sirve igual.

- **Si tiene la serie en Excel o CSV,** que la suba por la sesión de R (`trabajar_en_r` le da el enlace) para calcular ahí.
- **Si solo tiene los totales,** que los dicte y anótalos en la tabla.
- **Si un indicador no tiene dato,** se dice. Ese objetivo se respalda con un resultado cualitativo con evidencia (un procedimiento aprobado, un acta de conformidad, una certificación), o se replantea con su asesor.

## Paso 3 — Los cálculos

Lo habitual en un TSP:

- **Variación:** absoluta (después − antes) y porcentual ((después − antes) / antes × 100).
- **Ahorro o beneficio económico:** horas ahorradas × costo por hora, merma evitada × precio, etc., con los supuestos dichos.
- **Promedios y dispersión** por periodo, si hay serie.
- **Prueba antes-después** (t de Student para muestras relacionadas o Wilcoxon), **solo si hay serie suficiente** (al menos 8 a 10 periodos por lado) y su guía o su asesor la piden. No es obligatoria en un TSP.

Haz los cálculos con `trabajar_en_r` y muéstrale el resultado. Si los trae de su Excel, revísalos con él y guárdalos con `guardar_analisis`. En los dos casos, **guarda las cifras** con `guardar_analisis` (`capitulo: tsp-fase4-resultados`, `resultados`: una por línea con su etiqueta, como «Tiempo de despacho antes = 48,2 h»). Desde ese momento, cualquier cifra del capítulo que no esté guardada saldrá marcada en el repaso.

Anota también los indicadores en `guardar_avance` (`capitulo: tsp-fase4-resultados`, `estado: EN_CURSO`, `datos.indicadores`, una línea por indicador: «Tiempo de despacho: 48,2 h → 26,0 h (−46 %)»).

## Paso 4 — Resultados por objetivo

**4.1**, un subtítulo `###` por objetivo específico, con el mismo orden y la misma redacción del Capítulo I. En cada uno:

1. Una frase que recuerda qué se buscaba.
2. La tabla o la figura con el antes y el después, mencionada en el texto antes de aparecer.
3. Un párrafo que interpreta: qué cambió, cuánto y por qué (por la actividad del Capítulo III que lo explica).

Tabla, en un solo bloque:

```
**Tabla 5**
*Tiempo promedio de despacho antes y después de la implementación*
| Indicador | Antes (ene–mar 2024) | Después (oct–dic 2024) | Variación |
|---|---|---|---|
| Tiempo de despacho (h) | 48,2 | 26,0 | −46,1 % |
| Pedidos con retraso (%) | 18,3 | 6,1 | −12,2 p. p. |
*Nota.* Elaborado con datos del sistema de despachos de la empresa.
```

Figura (un gráfico de barras o de líneas hecho en R o en Excel):

```
**Figura 6**
*Evolución mensual del tiempo de despacho, 2024*

[Insertar aquí la Figura 6: tiempo-despacho-2024.png]

*Nota.* Elaborado con datos del sistema de despachos de la empresa.
```

Si el gráfico salió de la sesión de R, dile qué archivo descargar para pegarlo en esa marca. La cifra va antes del adjetivo: «bajó 46 %», no «bajó considerablemente».

## Paso 5 — Aporte profesional y beneficios

**4.2**, en prosa:

- **Para la empresa:** el beneficio económico calculado, lo que quedó funcionando (un procedimiento, un formato, un sistema) y quién lo usa hoy.
- **Profesional:** qué competencias de su carrera aplicó y qué aprendió. Concreto, sin frases de autoayuda.

## Paso 6 — Análisis de los resultados

**4.3**, en dos a cuatro párrafos: compara los resultados con los **antecedentes del Capítulo II** (con sus claves): en qué coinciden, en qué no y por qué, por las condiciones de la empresa. Si algún objetivo no se logró del todo, aquí se explica. Sin conclusiones todavía: esas son el Capítulo V.

## Paso 7 — Guardar y entregar

1. **Guarda** con `guardar_capitulo`, clave `tsp-fase4-resultados`. Markdown limpio: `##` para 4.1 a 4.3 y `###` para cada objetivo; **sin el título del capítulo**, sin portada y sin referencias. Hasta 30.000 caracteres por llamada; si pasa, por partes, nunca dentro de una tabla. Si la respuesta trae AVISOS DE REDACCIÓN, corrige esos párrafos con `reescribir_parrafos`.
2. **Comprueba** con `revisar_evidencia` (`capitulo: tsp-fase4-resultados`): marca las cifras que no están entre las guardadas y las afirmaciones sin fuente. Corrige antes de dar el enlace.
3. **Registra** con `guardar_avance` (`capitulo: tsp-fase4-resultados`): un `resumen` de dos o tres frases, los `datos.logros` (uno por objetivo) y `estado: LISTO` solo si lo da por bueno.
4. **Da el enlace** con `enlace_del_word` y dile qué gráfico va en cada marca de figura.

Cierre:

```
- [ ] Cada objetivo específico tiene su resultado con dato o evidencia.
- [ ] Las cifras de partida coinciden con las del Capítulo III.
- [ ] Guarda los archivos de datos: el jurado puede pedirlos.
```

Lo siguiente es el **Capítulo V, Conclusiones y recomendaciones** (`tsp-fase5-conclusiones`).

## Lo que esta skill NO hace

- No calcula de cabeza ni redondea a conveniencia.
- No oculta un resultado que no mejoró.
- No escribe conclusiones ni recomendaciones: eso es el Capítulo V.
- No exige pruebas estadísticas que un TSP no necesita.

## Archivos de referencia

- `references/integracion_zotero.md` — Claves de cita, norma del proyecto y las herramientas de fuentes.
- `references/parafraseo.md` — Paráfrasis y patrones de escritura que delatan a la IA.
