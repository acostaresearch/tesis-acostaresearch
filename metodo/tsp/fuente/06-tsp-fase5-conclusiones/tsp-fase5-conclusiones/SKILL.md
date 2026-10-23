---
name: tsp-fase5-conclusiones
description: Capítulo V, Conclusiones y recomendaciones, del Trabajo de Suficiencia Profesional (TSP) de Acosta | IA & Research, y cierre del trabajo. Redacta una conclusión por objetivo, cada una con el hallazgo y su cifra del Capítulo IV; recomendaciones con responsable y plazo a la empresa, a otros profesionales y a la universidad; el resumen y el abstract con palabras clave; y fija los anexos de evidencias (constancia de trabajo, reportes, fotos, planos) en el Word. No introduce datos ni citas nuevas. Guarda el capítulo y entrega el enlace del Word, con lo que falta revisar antes de presentarlo. ACTIVAR con "conclusiones del TSP", "recomendaciones", "resumen y abstract de mi suficiencia profesional", "anexos del TSP", "terminar mi TSP".
---

# 5 · Capítulo V · Conclusiones y recomendaciones

## Para qué sirve esta skill

Cierra el TSP: redacta el **Capítulo V**, el **resumen** y el **abstract**, y deja los **anexos de evidencias** en el Word.

```
  Fase 0 · Tu experiencia y la empresa
  Fase 1 · Capítulo I · Introducción
  Fase 2 · Capítulo II · Marco teórico
  Fase 3 · Capítulo III · Descripción de la experiencia
  Fase 4 · Capítulo IV · Resultados
  Fase 5 · Capítulo V · Conclusiones y recomendaciones    ← estás aquí
```

Lo que se guarda:

```
5.1 Conclusiones
    5.1.1 …  (una por objetivo: primero el general, después cada específico)
5.2 Recomendaciones
    5.2.1 A la empresa
    5.2.2 A otros profesionales
    5.2.3 A la universidad
Resumen       (con sus palabras clave)
Abstract      (con sus keywords)
```

En el texto guardado, `##` para 5.1, 5.2, Resumen y Abstract, y `###` para sus partes.

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un .docx, un PDF ni ningún otro archivo.** No usa la skill `docx` y no entrega archivos en el chat.

```
1. mi_proyecto           al abrir la conversación
2. ver_capitulo          tsp-fase1-introduccion (objetivos),
                         tsp-fase3-experiencia y tsp-fase4-resultados,
                         `texto: true`
3. ver_analisis          las cifras guardadas del Capítulo IV
4. guardar_capitulo      clave `tsp-fase5-conclusiones`
5. estructura_de_la_tesis   para los anexos, con la lista completa
6. revisar_la_tesis      el repaso de todo el trabajo
7. enlace_del_word       al final
```

**Sin citas nuevas.** Si alguna hace falta, con su clave `[AR…]`. Entre corchetes, en el texto guardado, solo van las claves, `[FALTA FUENTE]` y la marca de figura.

**Si un guardado falla, se dice con esa palabra: no se guardó.**

El detalle está en `references/integracion_zotero.md`.

## Regla de oro

1. **Cada conclusión responde a un objetivo** del Capítulo I, con la misma redacción, y lleva el hallazgo con su cifra **tal como está en el Capítulo IV**. Nada que no se haya mostrado antes.
2. **Cada recomendación sale de un resultado o de una dificultad** del trabajo, y dice quién la hace y en qué plazo.
3. **Lo que no se logró se dice** en la conclusión que corresponde.

## Paso 1 — Leer lo acordado

Llama a `mi_proyecto`, lee con `ver_capitulo` (`texto: true`) los objetivos (`tsp-fase1-introduccion`), las dificultades (`tsp-fase3-experiencia`, 3.5) y los resultados (`tsp-fase4-resultados`), y las cifras con `ver_analisis`.

Si falta el Capítulo IV, díselo: sin resultados no hay conclusiones. Si ya hay texto de este capítulo (`capitulo: tsp-fase5-conclusiones`), léelo y pregunta qué falta; las partes nuevas se añaden con `anadir: true` para no borrar lo guardado.

## Paso 2 — Conclusiones

**5.1**, una conclusión por objetivo, cada una en un párrafo de tres a cinco oraciones con tres movimientos:

1. El objetivo, parafraseado (no copiado).
2. Lo que se logró, con la cifra del Capítulo IV.
3. Lo que significa para la empresa o para la práctica profesional.

Ejemplo: «Respecto a reducir los tiempos de despacho, la implementación de las 5S en el almacén bajó el tiempo promedio de 48,2 a 26,0 horas entre el primer y el último trimestre de 2024, un 46,1 % menos. Con ello la empresa dejó de pagar penalidades por entrega tardía a sus dos principales clientes.»

Primero la del objetivo general, después una por cada específico. Entrégalas y espera su visto bueno.

## Paso 3 — Recomendaciones

**5.2**, entre 6 y 10 en total, como lista numerada dentro de cada destinatario:

- **A la empresa:** qué mantener, ampliar o corregir, con responsable (cargo o área) y plazo. Salen de los resultados y de las dificultades.
- **A otros profesionales:** qué conviene repetir o evitar al aplicar lo mismo en otra empresa del sector.
- **A la universidad:** qué contenido de la carrera le habría servido más, o qué conviene reforzar. Breve, concreta y sin quejas.

## Paso 4 — Resumen y abstract

**Resumen**, un solo párrafo de 200 a 300 palabras (o lo que pida su guía): el problema de la empresa, lo que se aplicó, cómo, los resultados principales con cifras y la conclusión central. Después, *Palabras clave:* con 3 a 5 términos.

**Abstract**, el mismo contenido en inglés académico, no una traducción palabra por palabra, y *Keywords:*.

Van al final del texto guardado, después de las recomendaciones: el Word pone cada capítulo bajo su título y no tiene sitio para páginas preliminares. Al dar el enlace, dile que los mueva en Word delante del índice si su guía lo pide así.

## Paso 5 — Guardar el capítulo

Guarda con `guardar_capitulo`, clave `tsp-fase5-conclusiones`. Markdown limpio, **sin el título del capítulo**, sin portada y sin referencias; empieza en `## 5.1 Conclusiones`. Si la respuesta trae AVISOS DE REDACCIÓN, corrige esos párrafos con `reescribir_parrafos`.

Registra con `guardar_avance` (`capitulo: tsp-fase5-conclusiones`): un `resumen` de dos frases y `estado: LISTO` solo si lo da por bueno.

## Paso 6 — Los anexos de evidencias

Recupera con él la lista de evidencias del Capítulo III y ordénala como se citan en el texto. Lo habitual:

1. Constancia o certificado de trabajo.
2. Autorización de la empresa para usar su información (si la usa con su nombre).
3. Las evidencias de cada etapa: reportes, registros, planos, actas, fotos.

Para que salgan en el Word, fija la estructura con `estructura_de_la_tesis`. **Repítele la lista y espera su confirmación antes de guardarla**, porque reordena el documento. Manda la lista completa, en orden: los cinco capítulos con sus claves y, detrás, un capítulo propio por anexo:

```
Capítulo I: Introducción                      de: tsp-fase1-introduccion
Capítulo II: Marco teórico                    de: tsp-fase2-marco-teorico
Capítulo III: Descripción de la experiencia   de: tsp-fase3-experiencia
Capítulo IV: Resultados                       de: tsp-fase4-resultados
Capítulo V: Conclusiones y recomendaciones    de: tsp-fase5-conclusiones
Anexo 1: Constancia de trabajo                (sin fases)
Anexo 2: Reporte de despachos 2024            (sin fases)
…
```

Si ya tenía una estructura fijada en la Fase 1, respeta sus títulos y solo añade los anexos. La ficha `tsp-fase0-experiencia` no va. Las referencias no se nombran: el Word las pone solas, antes de los anexos.

La respuesta dice la clave de cada anexo. Guarda cada uno con `guardar_capitulo` y esa clave: una línea que diga qué es y la marca de la imagen.

```
Constancia emitida por el área de Recursos Humanos de la empresa.

[Insertar aquí la Figura 12: constancia-de-trabajo.jpg]
```

## Paso 7 — Repaso final y entrega

1. Pasa `revisar_la_tesis` y cuéntale lo que marque, empezando por lo grave (un objetivo sin conclusión, cifras que no cuadran, capítulos sin texto).
2. Da el enlace con `enlace_del_word`:

```
Tu trabajo de suficiencia profesional está completo. Aquí está en Word: [enlace]

Antes de presentarlo:
- Mueve el Resumen y el Abstract delante del índice si tu guía lo pide.
- Pega cada imagen donde dice [Insertar aquí la Figura N: …] y borra la marca.
- Revisa la portada: tu nombre, tu asesor y el título exacto.
- Lleva el documento a tu asesor y, si quieres, pásalo por el humanizador
  académico o por bajar similitud antes del Turnitin.

El enlace vence a la media hora; si pasó, pídeme otro.
```

## Lo que esta skill NO hace

- No introduce datos, cifras ni citas que no estén en los capítulos anteriores.
- No escribe la dedicatoria ni los agradecimientos: son del egresado.
- No arma el Word ni escribe la lista de referencias.

## Archivos de referencia

- `references/integracion_zotero.md` — Claves de cita, norma del proyecto y las herramientas de fuentes.
- `references/parafraseo.md` — Paráfrasis y patrones de escritura que delatan a la IA.
