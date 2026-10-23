# De la evidencia a la acción

La cadena que hace que un informe se ejecute. Si se rompe en un eslabón, el informe se
archiva.

```
EVIDENCIA  ─►  HALLAZGO  ─►  CONCLUSIÓN  ─►  RECOMENDACIÓN  ─►  ACCIÓN
(el dato)      (qué pasa)    (qué significa)  (qué hacer)      (quién, cuándo,
                                                                cuánto)
```

**Cada eslabón se puede rastrear hacia atrás.** Una recomendación que no sale de una
conclusión, y una conclusión que no sale de un hallazgo del informe, no entran.

## Un ejemplo completo

```
EVIDENCIA       De las 210 órdenes de compra del trimestre, 80 no tienen
                cotización adjunta (reporte de compras al 31-03-2026). En
                esas 80, el precio unitario promedio fue 9 % más alto.

HALLAZGO 2      El 38 % de las órdenes se emite sin cotización previa, con
(Fase 2)        un sobrecosto estimado de S/ 21 400 en el trimestre.

CONCLUSIÓN 2    El procedimiento de compras no protege el precio en los
(Fase 4)        montos menores: exige cotización solo sobre S/ 5 000, y el
                74 % de las órdenes está por debajo de ese umbral.

RECOMENDACIÓN 2 Bajar el umbral de cotización obligatoria a S/ 1 500 y
(Fase 4)        exigir tres cotizaciones sobre S/ 5 000.

ACCIÓN          Modificar el procedimiento de compras · Jefe de
(Fase 4)        Administración · 31-10-2026 · sin costo directo ·
                se mide con el % de órdenes con cotización adjunta.
```

Lo que hace que funcione: la conclusión **explica** el hallazgo en vez de repetirlo, y la
recomendación ataca lo que la conclusión identificó, no el síntoma.

## Las conclusiones

Una por objetivo o por hallazgo que la pida. Tres a cinco oraciones cada una.

Estructura:

1. **Qué se encontró**, resumido y sin repetir la cifra entera.
2. **Qué significa** para la decisión del encargo.
3. **Qué tan firme es**, si hay una salvedad que importa.

Reglas duras:

- **Sin datos nuevos.** Todo lo que se concluye ya está en el desarrollo o en el análisis.
- **Sin citas nuevas.** Si hace falta citar, no es una conclusión: es desarrollo.
- **Sin recomendar todavía.** La conclusión dice qué significa; la recomendación, qué hacer.
- **Se pueden rastrear.** Cada una a una sección del informe.
- **No todas las conclusiones llevan recomendación.** Una puede ser «el proceso de recepción
  funciona bien y no requiere cambios», y decirlo tiene valor.

| Mal | Bien |
|---|---|
| «Se concluye que existen oportunidades de mejora en el área de compras.» | «El procedimiento de compras no protege el precio en los montos menores: el umbral de cotización deja fuera al 74 % de las órdenes.» |
| «Se concluye que las ventas cayeron 12 %.» (es el hallazgo, no la conclusión) | «La caída de 12 % se explica por la pérdida de dos clientes que concentraban el 21 % de la facturación, no por una contracción del mercado, que creció 4 % en el periodo.» |
| «El proyecto presenta indicadores favorables.» | «El proyecto es viable solo si el financiamiento baja del 14 % al 11 %: a la tasa actual el VAN es negativo en S/ 52 340.» |

Y la apertura se varía: no todas empiezan con «se concluye que».

## Las recomendaciones

Cada una responde cinco preguntas. Si falta una, la recomendación no se ejecuta:

```
QUÉ HACER        En infinitivo, concreto y verificable.
QUIÉN            El cargo, no la persona.
PARA CUÁNDO      Una fecha, no «a la brevedad».
CUÁNTO CUESTA    En soles, o «sin costo directo». Si no se sabe, se marca.
CÓMO SE SABRÁ    El indicador que va a medir si funcionó.
QUE FUNCIONÓ
```

| Mal | Bien |
|---|---|
| «Se recomienda optimizar el proceso de compras.» | «Bajar el umbral de cotización obligatoria de S/ 5 000 a S/ 1 500, modificando el procedimiento de compras. Jefe de Administración, 31-10-2026, sin costo directo. Se mide con el porcentaje de órdenes con cotización adjunta, con meta del 95 %.» |
| «Se recomienda capacitar al personal.» | «Capacitar a los cuatro operarios de despacho en el uso del módulo de ubicaciones, 8 horas. Jefe de Almacén, noviembre de 2026, S/ 1 200 según la cotización del Anexo 6. Se mide con el tiempo de búsqueda por orden.» |
| «Se recomienda implementar un sistema ERP.» | Falta el dato del costo: «Cotizar un sistema de gestión de almacén con al menos tres proveedores, con los requisitos del Anexo 7. Jefe de Sistemas, 30-11-2026. `[POR CONFIRMAR CON LA EMPRESA: presupuesto disponible]`. La decisión de compra se toma con las cotizaciones en mano.» |

Tres reglas más:

- **Lo que la empresa no puede hacer, no se recomienda.** Si no hay presupuesto ni personal,
  una recomendación de S/ 200 000 es una forma elegante de no recomendar nada. Se recomienda
  el paso que sí puede dar.
- **Entre tres y ocho recomendaciones.** Con quince, no se ejecuta ninguna.
- **Lo que no sale del informe no se recomienda**, por buena que sea la idea. Si hace falta
  decirlo, va aparte y se dice así: «esto no lo cubre el informe, pero conviene mirarlo».

## Priorizar: lo que convierte una lista en un plan

Diez recomendaciones sin orden no se ejecutan; tres priorizadas sí. La matriz de impacto y
esfuerzo, que se le enseña y él ajusta:

```
**Tabla 10**
*Priorización de las recomendaciones*
| N.º | Recomendación | Impacto | Esfuerzo | Cuándo |
|---|---|---|---|---|
| 2 | Bajar el umbral de cotización | Alto | Bajo | Este mes |
| 4 | Ubicaciones fijas en almacén | Alto | Medio | Este trimestre |
| 1 | Capacitar a los operarios | Medio | Bajo | Este mes |
| 5 | Sistema de gestión de almacén | Alto | Alto | Este año |
| 3 | Inventario cíclico semanal | Medio | Medio | Este trimestre |
*Nota.* Impacto estimado sobre el sobrecosto identificado en los hallazgos. Esfuerzo en
horas y costo de implementación.
*Fuente.* Elaboración propia.
```

Lo primero: **alto impacto y bajo esfuerzo.** Y se dice explícitamente qué se hace este mes,
este trimestre y este año, porque eso es lo que el gerente va a repartir el lunes.

## Los riesgos de la recomendación

Lo que casi ningún informe trae y lo que lo hace creíble: **qué puede salir mal si se ejecuta
lo que se recomienda.**

```
**Tabla 11**
*Riesgos de la implementación*
| Riesgo | Probabilidad | Impacto | Mitigación | Responsable |
|---|---|---|---|---|
| El umbral más bajo retrasa las compras urgentes | Media | Medio | Mantener un procedimiento de excepción con visto bueno de gerencia | Jefe de Administración |
| El personal no usa el módulo de ubicaciones | Alta | Alto | Capacitación y revisión semanal el primer mes | Jefe de Almacén |
*Fuente.* Elaboración propia.
```

**Un riesgo sin mitigación es una advertencia, no un análisis.**

## Las limitaciones

El párrafo que se abrió en la Fase 1 se cierra aquí, y va en el informe. Dice qué no se pudo
mirar y **qué no debería concluirse de este informe**:

> El informe cubre el proceso de almacén de la sede principal entre abril de 2025 y marzo de
> 2026. No incluye compras, transporte ni las otras dos sedes, así que sus hallazgos no se
> pueden extender a la operación completa. El costo por orden se estimó con el costo por hora
> promedio del área, porque el sistema no registra el costo por orden: la cifra del Hallazgo 3
> es un orden de magnitud y no un costo exacto. No se tuvo acceso a los reclamos de 2024, de
> modo que la evolución de reclamos se analiza solo sobre 2025 y 2026.

Tres cosas que hace: **acota el alcance**, dice de qué cifra desconfiar y por qué, y protege
el informe de que le atribuyan lo que no dijo. No es una disculpa: es parte del oficio.

## Los anexos

Se listan aquí y él los pega al final del Word, después de las referencias. Los habituales:

| Tipo de informe | Anexos |
|---|---|
| Diagnóstico | Datos completos, guías de entrevista, mapa del proceso, fotos |
| Gestión | Detalle de indicadores, el presupuesto contra el ejecutado |
| Factibilidad | Cotizaciones, flujo detallado por mes, cálculos, permisos |
| Estudio de mercado | El cuestionario, la base de respuestas, el detalle de la muestra |
| Auditoría | La evidencia de cada hallazgo, la muestra, las respuestas de los responsables |
| Técnico | Especificaciones, planos, resultados de las pruebas |
| Incidente | Bitácoras completas, capturas, la línea de tiempo detallada |

Va al anexo lo que quien decide no necesita para decidir, pero alguien puede querer revisar.
