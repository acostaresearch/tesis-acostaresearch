# La revisión antes de entregar

Tres revisiones, en este orden. La primera es contra lo que pidió el cliente; la segunda, la
que hunde informes; la tercera, la que evita un problema con una persona.

---

## 1. Contra los términos de referencia

## Cómo se hace

1. Tomar lo que pidió el cliente de `informe.terminos` (la ficha de `mi_proyecto`). **Si hay
   documentos subidos, releerlos con `material_del_curso`**: la revisión se hace contra
   el original, no contra el resumen de la ficha.
2. Leer el texto guardado de cada sección con `ver_capitulo` (`texto: true`).
3. Por cada cosa pedida, **buscar en el texto dónde se cumple** y anotar la sección. Si no se
   encuentra, no se cumple.
4. Enseñar la tabla completa, aunque salga mal.

```
REVISIÓN CONTRA LOS TÉRMINOS DE REFERENCIA
| Lo que se pidió | ¿Se cumple? | Dónde | Qué falta |
|---|---|---|---|
| Diagnóstico del proceso de almacén | Sí | Desarrollo, secciones 3 y 4 | — |
| Comparación con el sector | En parte | Sección 7 | Falta el dato de tiempo de ciclo del sector |
| Propuesta con costos | Sí | Plan de acción, Tabla 12 | — |
| Máximo 30 páginas | Por verificar | — | Lo comprueba en el Word descargado |

Se cumple: [N] de [M]
Por corregir ahora: [lista]
Por corregir en otra fase: [lista, con la fase]
Lo comprueba él en el Word: [lista]
```

**Regla dura:** «Sí» solo con el sitio exacto donde se cumple. Sin sitio, es «No».

## Qué se comprueba cuando no hay términos escritos

- El informe responde a la decisión guardada en `informe.decision`.
- Cada sección del esquema acordado tiene su texto.
- Hay resumen ejecutivo, introducción con alcance, conclusiones, recomendaciones y plan de
  acción.
- Las limitaciones están escritas.
- Toda afirmación externa lleva su clave; `revisar_evidencia` sin capítulo no deja
  afirmaciones sin respaldo o las tiene todas avisadas.
- `revisar_el_informe` no marca secciones vacías ni citas rotas.

## Lo que él tiene que comprobar en el Word descargado

No se puede verificar desde el texto guardado, y se le dice como tarea:

| Qué | Cómo lo comprueba |
|---|---|
| Extensión en páginas | Las páginas del Word, sin portada, referencias ni anexos |
| Formato, membrete, portada de la empresa | Si hay plantilla, que la suba con `formato_de_la_universidad` |
| Las imágenes | Que cada marca de figura resaltada tenga su imagen pegada |
| El índice | Aceptar «actualizar el índice» al abrir el Word |
| Los anexos | Pegados al final, en el orden de la lista |
| El formato de entrega | Guardar como PDF si así se entrega |

---

## 2. Revisión de cifras

**La que hunde informes.** Un total que no cuadra en la página 12 deja en duda las otras
cuarenta, y es lo primero que encuentra quien recibe el informe.

Se hace con `revisar_el_informe` y además a mano, una por una:

```
REVISIÓN DE CIFRAS
| Comprobación | Resultado |
|---|---|
| Cada cifra del resumen ejecutivo aparece igual en el cuerpo | [N] de [N] |
| Los totales de cada tabla suman | [N] de [N] tablas |
| Cada tabla y figura tiene su línea «Fuente» | [N] de [N] |
| Las proyecciones dicen que son proyecciones | [N] de [N] |
| Puntos porcentuales usados donde corresponde | SÍ / NO |
| Las cifras del plan de acción coinciden con las del análisis | SÍ / NO |
| Tablas y figuras numeradas seguido, sin saltos ni repetidas | SÍ / NO |
| Cada tabla y figura se menciona en el texto | [N] de [N] |
| No queda ninguna cifra sin origen | SÍ / NO |
| Unidades y monedas coherentes; tipo de cambio con su fecha | SÍ / NO |
```

**Los tres errores que más aparecen**, y hay que buscarlos a propósito:

1. **La cifra del resumen ejecutivo que no coincide** con el cuerpo, porque el cuerpo se
   corrigió después.
2. **El total de una tabla que no suma**, porque se editó una fila a mano.
3. **Los puntos porcentuales dichos como porcentaje.**

Si una sola línea de esta tabla falla, **no se entrega**: se corrige.

---

## 3. Revisión de tono y de riesgo

Tres cosas, y cualquiera de las tres puede costarle el trabajo a alguien o costarle un cliente
a él:

```
REVISIÓN DE TONO
| Comprobación | Resultado |
|---|---|
| Ningún hallazgo sin evidencia al lado | [N] casos |
| Ninguna promesa de resultado sin cálculo | [N] casos |
| Ninguna persona señalada con nombre donde va el cargo o el proceso | [N] casos |
| Ninguna afirmación sobre la competencia sin verificar o sin decir que es percepción | [N] casos |
| Ninguna norma sin su número y su año | [N] casos |
| Ningún dato personal que no haga falta | [N] casos |
| Si el informe sale de la empresa: sin márgenes por cliente ni sueldos | SÍ / NO |
```

Ejemplos de lo que se busca:

| Se corrige | Queda así |
|---|---|
| «La implementación aumentará las ventas un 30 %.» | «La implementación recupera unas 6 horas semanales; su efecto en ventas no se midió.» |
| «El jefe de almacén no hizo el inventario.» | «No se registran tomas de inventario desde 2024; el procedimiento no fija una frecuencia.» |
| «La competencia tiene el 40 % del mercado.» | «La empresa estima que su principal competidor tiene alrededor del 40 %; no se encontró una fuente que lo mida.» |
| «Se incumple la normativa laboral vigente.» | «Se incumple el artículo 9 del Decreto Supremo 011-2019-TR [AR…].» |

---

## La lista de entrega

Lo último, y se le entrega a él como lista para marcar:

- [ ] Extensión y formato que pedían los términos de referencia.
- [ ] Resumen ejecutivo que se entiende leído solo, con cifras y con la decisión que se pide.
- [ ] Introducción con el alcance: qué entra, qué no entra y las limitaciones.
- [ ] Plan de acción con responsable por cargo, plazo, costo e indicador.
- [ ] Riesgos de la implementación, con su mitigación.
- [ ] **Ningún `[POR CONFIRMAR]`, `[FALTA DATO]` ni `[FALTA FUENTE]` sin resolver.**
- [ ] Portada con el destinatario, quién lo firma y, si corresponde, la marca de confidencial.
- [ ] Imágenes pegadas en sus marcas.
- [ ] Anexos pegados al final, en orden.
- [ ] Datos personales fuera o anonimizados.
- [ ] Leído una vez entero, de corrido, antes de mandarlo.

## Las marcas que quedan sin resolver

Es el punto que más se salta. Antes de entregar, se le enseñan **una por una**, con lo que hay
que hacer con cada una:

```
QUEDAN 3 MARCAS SIN RESOLVER

1. [POR CONFIRMAR CON LA EMPRESA: presupuesto disponible]
   En el plan de acción, acción 5. Pregúntaselo a Gerencia antes de
   entregar, o cambia la acción por «cotizar» sin monto.

2. [FALTA DATO: costo por orden de despacho]
   En el Hallazgo 3. Ya está dicho en las limitaciones, así que puede
   quedarse: el informe explica que la cifra es un orden de magnitud.

3. [FALTA FUENTE]
   En la sección 7, el tiempo de ciclo del sector. Dos salidas: buscamos
   la fuente, o la comparación sale sin cifra.
```

**Una marca puede quedarse si la limitación la explica.** Lo que no puede quedarse es una
marca que el informe no explica: eso es un hueco, y quien lo lea lo va a encontrar.
