# Trabajo de Suficiencia Profesional (TSP)

Producto aparte del método de tesis, hecho el 5-oct-2026. El egresado se titula contando
una experiencia de su trabajo: **sin hipótesis, sin instrumento y sin muestra**.

## Las 6 skills

Estructura de la guía de la UPN, que sirve para casi todas las universidades.

| Archivo | Clave | Nombre en el catálogo | ¿Va al Word? |
|---|---|---|---|
| `01-tsp-fase0-experiencia` | `tsp-fase0-experiencia` | 0 · Tu experiencia y la empresa | No: es la ficha (empresa, cargo, periodo, problema, evidencias) |
| `02-tsp-fase1-introduccion` | `tsp-fase1-introduccion` | 1 · Capítulo I · Introducción | Sí |
| `03-tsp-fase2-marco-teorico` | `tsp-fase2-marco-teorico` | 2 · Capítulo II · Marco teórico | Sí |
| `04-tsp-fase3-experiencia` | `tsp-fase3-experiencia` | 3 · Capítulo III · Descripción de la experiencia | Sí |
| `05-tsp-fase4-resultados` | `tsp-fase4-resultados` | 4 · Capítulo IV · Resultados | Sí |
| `06-tsp-fase5-conclusiones` | `tsp-fase5-conclusiones` | 5 · Capítulo V · Conclusiones y recomendaciones | Sí, con resumen, abstract y anexos |

El nombre del catálogo sale solo del primer título (`# …`) de cada `SKILL.md`: tiene que
empezar por un número para que cuente como fase y no como herramienta de apoyo.

Si la universidad pide otra estructura, Claude la fija con `estructura_de_la_tesis`
(Fase 1). Los anexos de evidencias se fijan igual, en la Fase 5.

## Comprobar y armar

```
node skills/tsp/verificar.js
```

Tiene que terminar en «Sin fallos de sincronía». Los avisos REVISAR que quedan son los
mismos que en tesis: las prohibiciones del propio texto.

## Cómo se publica

1. En `/admin` → Grupos, crear el grupo con el código **`TSP_SUFICIENCIA_PROFESIONAL`**
   (cualquier código que empiece por `TSP` vale). Para probarlo primero, «Solo para» con
   el correo de quien prueba.
2. Subir los 6 `.skill` de `listas-para-subir/` **en orden, de la 0 a la 5**.
3. Marcar también `humanizador-academico` y `bajar-similitud` en «Capítulos que incluye».
4. Crear el plan con su precio. La página de planes ya sabe nombrarlo y listar sus fases.

## Lo que hace el servidor con un TSP

Lo trata como una tesis (portada, páginas preliminares, panel, Word) con estas diferencias:

- `mi_proyecto` dice «Modalidad: Trabajo de Suficiencia Profesional».
- `guardar_avance` solo enseña los campos de las fases del TSP.
- La Fase 0 no se imprime en el Word.
- El Word se descarga como `suficiencia-profesional-…`.
- El análisis de R cae en `tsp-fase4-resultados`.
- `revisar_la_tesis` comprueba que cada objetivo tenga su conclusión.
- Un Word subido se reparte por capítulos también con los títulos de un TSP.
