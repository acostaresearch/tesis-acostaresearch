# Errores comunes en la Discusión

Esta referencia documenta los 8 errores frecuentes al redactar la Discusión, detectados en tesis de pregrado y posgrado hispanoamericanas. La skill los previene activamente.

## Error 1: Mezclar Resultados con Discusión

### Síntoma

El tesista escribe "se halló r = .58, lo cual coincide con Pérez (2022)" en la sección de Resultados.

### Por qué es grave

Las dos secciones tienen funciones distintas:
- **Resultados**: dice QUÉ se halló (sin opiniones, sin comparaciones).
- **Discusión**: dice QUÉ SIGNIFICA lo que se halló (con literatura, con interpretación).

Mezclar empobrece ambas secciones y confunde al jurado.

### Cómo lo previene la skill

La skill 8 NUNCA repite los descriptivos completos. Solo recuerda el estadístico clave (Movimiento 1). El reporte completo está en la Skill 7.

### Prueba rápida

Si la Discusión NO menciona "coincide", "contrasta", "esto sugiere", "según Pérez" o "este resultado puede explicarse", entonces no hay Discusión, hay un duplicado de Resultados.

## Error 2: Repetir tablas que ya estaban en Resultados

### Síntoma

El tesista pega la misma tabla de descriptivos o de prueba de hipótesis en la Discusión.

### Por qué es grave

La tabla pertenece a Resultados. En la Discusión solo se menciona el dato necesario, sin re-presentar la tabla.

### Cómo lo previene la skill

La skill 8 entrega prosa continua **SIN TABLAS** (la decisión 3 del diseño lo confirmó). Si el tesista necesita ver el dato, vuelve al capítulo de Resultados (Skill 7).

## Error 3: Discutir hallazgos que no aparecen en Resultados

### Síntoma

El tesista discute "la diferencia entre hombres y mujeres" cuando esa prueba no se aplicó.

### Por qué es grave

Si el dato no está en Resultados, NO puede discutirse. Es invención.

### Cómo lo previene la skill

La skill 8 cruza cada hallazgo discutido con el capítulo de Resultados guardado (lo lee con `ver_capitulo` y `texto: true`, o con el texto que pegó el tesista si lo escribió fuera) antes de redactar. Si un hallazgo no está, NO se discute.

## Error 4: No comparar con antecedentes (Discusión sin literatura)

### Síntoma

El tesista escribe párrafos de "interpretación" sin citar a nadie. Solo dice "esto demuestra que..." sin contraste.

### Por qué es grave

Discusión sin literatura es opinión, no análisis académico. Sin el Movimiento 2, el párrafo pierde su valor académico.

### Cómo lo previene la skill

Los 4 movimientos son obligatorios. La skill SIEMPRE incluye el Movimiento 2 (comparar con literatura). Si no hay antecedentes pertinentes en el Cap II, la skill lo declara explícitamente (no inventa).

## Error 5: Usar voz personal ("yo creo", "pienso que")

### Síntoma

> "Yo creo que estos resultados muestran que..."
> "Pienso que las variables se relacionan porque..."

### Por qué es grave

La tesis académica usa voz IMPERSONAL. La primera persona del singular suena coloquial.

### Cómo lo previene la skill

La skill 8 redacta SIEMPRE en tercera persona o voz impersonal:
- "El presente estudio halló..."
- "Estos resultados sugieren..."
- "Una posible explicación es..."
- "Cabe señalar que..."

NUNCA usa "yo", "mi", "me parece", "creo".

## Error 6: Citar autores sin clave o por lo que no dijeron

### Síntoma

El tesista cita en la Discusión a Martínez, que no aparece en el Cap II ni en su biblioteca, o le atribuye un hallazgo que Martínez no reportó.

### Por qué es grave

- El jurado verifica las referencias.
- Si un autor aparece en Discusión pero no en el Cap II, la coherencia del marco teórico está rota.
- Puede sugerir que el autor fue agregado a último momento para "rellenar" la discusión.

### Cómo lo previene la skill

La skill 8 SOLO contrasta con autores que tienen clave `[AR…]`: los del Cap II guardado o fuentes de la biblioteca del tesista (`buscar_fuentes`, `mis_fuentes`). Antes de redactar llama a `revisar_evidencia` sin capítulo, para no apoyarse en afirmaciones del Cap II que no tienen fuente, y cruza cada cita con lo que dice su fuente. Si entra un antecedente que no estaba en el Cap II, se lo avisa al tesista y le sugiere añadirlo también al marco teórico. Un autor sin clave no entra: la afirmación queda con `[FALTA FUENTE]` o se elimina.

## Error 7: Olvidar la honestidad académica al reportar divergencias

### Síntoma

El tesista esconde hallazgos que contradicen sus hipótesis o fuerza interpretaciones para que coincidan con la literatura.

### Por qué es grave

El jurado lee con detalle la Discusión. La deshonestidad académica se nota rápido y resta credibilidad.

### Cómo lo previene la skill

Ver `references/honestidad_academica.md` para detalle. Los tres caminos válidos:
1. Atribuir la diferencia al contexto.
2. Atribuir la diferencia a la metodología.
3. Reconocer la limitación.

NUNCA forzar coincidencias inexistentes.

## Error 8: Confundir Discusión con Conclusiones

### Síntoma

El tesista escribe conclusiones definitivas en la Discusión: "Se concluye que el clima organizacional influye en el desempeño..."

### Por qué es grave

Las Conclusiones son sección aparte (Skill 9). La Discusión INTERPRETA, las Conclusiones SINTETIZAN.

### Cómo lo previene la skill

La skill 8 NO escribe "se concluye que" en ningún párrafo. Usa formulaciones interpretativas:
- "Estos hallazgos sugieren..."
- "Una posible interpretación es..."
- "Los resultados aportan evidencia de..."

Las Conclusiones se redactarán en Skill 9.

## Resumen de prevención

| Error | Cómo lo previene la skill |
|-------|---------------------------|
| Mezclar Resultados con Discusión | Solo Movimientos 1-4, sin descriptivos completos |
| Repetir tablas | La skill entrega prosa pura, sin tablas |
| Discutir hallazgos inexistentes | Cruce con el capítulo de Resultados |
| No comparar con antecedentes | Movimiento 2 obligatorio |
| Voz personal | Redacción en tercera persona obligatoria |
| Citar autores sin clave o por lo que no dijeron | Solo claves [AR…] + `revisar_evidencia` antes y después |
| Forzar coincidencias | Los 3 caminos honestos del Cap 8.11 |
| Confundir con Conclusiones | NO usar "se concluye que" |
