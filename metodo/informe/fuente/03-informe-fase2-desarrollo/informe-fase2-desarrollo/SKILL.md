---
name: informe-fase2-desarrollo
description: Tercera fase de la Ruta del Informe de Acosta | IA & Research, para informes de curso y de empresa. Redacta el cuerpo del informe según su tipo. En un curso, el informe académico con la idea, las fuentes, un ejemplo y la postura del estudiante; el de proyecto con problema, objetivos, propuesta e implementación; el caso con hechos, problema, análisis y alternativas. En una empresa, el diagnóstico con la situación actual, los hallazgos numerados por impacto y sus causas; el de gestión con los desvíos; la factibilidad con el negocio, lo técnico, lo legal y la inversión; el estudio de mercado con demanda, oferta y precios. Antes de redactar pregunta lo que solo sabe quien escribe y no lo inventa. En empresa escribe con la conclusión primero y la cifra antes del adjetivo. Aplica la auditoría anti-IA, guarda la sección y da el enlace del Word. ACTIVAR con "redacta mi informe", "ayúdame con el desarrollo", "cuenta mi proyecto", "analiza el caso", "escribe el diagnóstico", "los hallazgos".
---

# Fase 2 — Desarrollo

## Para qué sirve esta skill

Es la tercera fase de la **Ruta del Informe** y la primera que escribe texto del informe: el
**desarrollo**, que es el cuerpo.

```
  Fase 0 · El encargo
  Fase 1 · Las fuentes y la evidencia
  Fase 2 · El desarrollo                   ← estás aquí
  Fase 3 · Análisis y resultados
  Fase 4 · Cierre: conclusiones, recomendaciones y revisión
```

**Qué ámbito es:** si `mi_proyecto` dice «Ámbito: empresa», es de empresa; si no lo dice, es de
curso.

| Ámbito | El ladrillo del desarrollo | Referencia |
|---|---|---|
| **Curso** | El apartado: idea, fuentes, ejemplo y postura del estudiante | `references/desarrollo_por_tipo.md` |
| **Empresa** | El **hallazgo de cinco piezas**: qué pasa, cómo se sabe, cuánto cuesta, por qué pasa y qué se puede hacer | `references/desarrollo_por_tipo_empresa.md` y `references/escribir_para_decidir.md` |

## Regla transversal — El documento lo arma el servidor, las citas van por clave

**La skill NUNCA genera un archivo de Word, un PDF ni ningún otro archivo del informe.** No
usa la skill `docx` y no entrega archivos en el chat.

El Word lo arma el servidor con lo guardado: portada del informe, resumen e introducción
delante, esta sección con el título «Desarrollo», las demás en orden, y las citas y
referencias en la norma del proyecto.

```
1. mi_proyecto        al abrir (ficha: ámbito, tipo, rúbrica o decisión,
                      entrega; norma)
2. ver_capitulo       informe-fase0-encargo (esquema, pregunta guía o decisión)
                      e informe-fase1-fuentes (claves por subtítulo,
                      limitaciones)
3. buscar_fuentes     si un apartado necesita más respaldo
   / mis_fuentes
4. guardar_capitulo   clave `informe-fase2-desarrollo`, apenas lo dé por bueno
5. revisar_evidencia  capitulo: informe-fase2-desarrollo, al guardar
6. enlace_del_word    cuando quiera ver el documento
```

**Las citas se marcan con la clave de la fuente, no se escriben:** `[AR97D22F86]`,
`[AR97D22F86:n]` detrás del nombre del autor, `[AR97D22F86:p. 45]` con página,
`[FALTA FUENTE]` sin respaldo. Nunca la cita escrita a mano ni la lista de referencias.

**En empresa, los datos internos se citan por su documento y su fecha de corte**, en el texto y
en la línea «Fuente:» de la tabla, sin clave. Y existen dos marcas más: `[FALTA DATO: …]` y
`[POR CONFIRMAR CON LA EMPRESA: …]`.

**Entre corchetes, en el texto guardado, solo van** las claves, `[FALTA FUENTE]`, esas dos
marcas de empresa y la marca de figura. Los avisos van en el chat.

**Si un guardado falla, se dice con esa palabra: no se guardó.**

El detalle está en `references/integracion_zotero.md`. **Leerlo antes de citar** (con
`redactar`, `referencia: "integracion_zotero.md"`).

## Regla del acompañamiento

- **Un paso por turno.** Preguntas según `references/estilo_preguntas.md`.
- **De dos apartados en dos.** Nadie corrige cinco páginas de golpe.
- **El texto es de quien lo entrega.** Se le pregunta lo suyo antes de redactar y se le pide
  que lo revise con su voz. En empresa, además, lo va a defender en una reunión: lo que no pueda
  explicar no entra.

## Regla de oro: veracidad

1. **Lo que solo sabe quien escribe lo pone él:** qué hizo en el proyecto, qué opina del caso,
   qué vio en la empresa, a quién entrevistó, qué le dijeron, qué decidió. **Si trae poco, se
   le pregunta; no se rellena.**
2. **Cada idea tomada de una fuente, con su clave.** Sin clave, `[FALTA FUENTE]`.
3. **Ninguna cifra de memoria y ninguna cuenta mental.** Cada cifra, con su fuente; los
   cálculos, en la Fase 3.
4. **Nada de lo que dice una fuente se estira** para que encaje en el apartado.
5. **Empresa: un hallazgo sin evidencia no es un hallazgo.** Si el dato no llegó,
   `[FALTA DATO: …]`. Y la causa se nombra por lo que la evidencia sostiene: demostrada,
   probable o no establecida (la tabla de verbos está en `references/escribir_para_decidir.md`).
6. **Si la IA está prohibida en el curso** (lo dice el resumen de la Fase 0), esta fase no
   redacta: revisa el borrador que escriba el estudiante contra el esquema y la rúbrica, y le
   dice qué falta.

## Lo que esta skill NO hace

- **No escribe la introducción, las conclusiones, las recomendaciones ni el resumen.** Eso es
  la Fase 4.
- **No presenta resultados con cifras calculadas ni indicadores.** Eso es la Fase 3.
- **No inventa experiencias, opiniones ni datos.**
- **Empresa: no señala a una persona con nombre** donde corresponde el proceso o el cargo
  (`references/confidencialidad.md`).

## Paso 1 — Leer lo acordado

`mi_proyecto`, y `ver_capitulo` de `informe-fase0-encargo` y de `informe-fase1-fuentes`. De
ahí: ámbito, tipo, esquema, pregunta guía o decisión, rúbrica o alcance, extensión, qué
sostiene cada subtítulo y, en empresa, las limitaciones.

- **Sin esquema guardado:** volver a la Fase 0.
- **Sin fuentes guardadas en un informe de curso:** ofrecer la Fase 1 antes. En un proyecto se
  puede seguir con pocas.
- **Empresa, con secciones sin evidencia:** decirlo antes de empezar y acordar qué se hace.
- **Si ya hay texto guardado de esta fase,** leerlo con `ver_capitulo` (`capitulo:
  informe-fase2-desarrollo`, `texto: true`, y `parte` si viene partido) y preguntar qué se
  corrige, en vez de empezar de cero.

Reparto de extensión: la acordada, menos introducción, resultados y cierre, repartida entre los
apartados.

## Paso 2 — Lo que solo sabe quien escribe

Preguntarlo en una sola tanda, en texto libre, **antes de redactar**.

**Curso**, con `references/desarrollo_por_tipo.md`:

- **Informe de curso:** su postura sobre el tema, en una o dos frases, y si conoce un ejemplo
  cercano (su ciudad, su trabajo, una noticia).
- **Proyecto:** qué problema vieron, qué hicieron paso a paso, con qué herramientas, cuánto
  duró, qué costó, qué salió mal y cómo lo resolvieron, quién hizo qué.
- **Caso:** qué le parece el problema central y qué decisión tomaría él.

**Empresa**, con la tabla del final de `references/desarrollo_por_tipo_empresa.md`:

- **Diagnóstico:** qué vio cuando estuvo ahí, a quién entrevistó y qué le dijo cada uno, qué le
  llamó la atención.
- **Gestión:** por qué se desvió cada indicador, qué pasó en el periodo que no está en los
  números.
- **Factibilidad:** por qué eligió esta solución y no otra, qué cotizó y con quién.
- **Estudio de mercado:** cómo hizo el campo, qué le dijeron los clientes, qué observó en la
  competencia.
- **Auditoría, incidente u otro:** qué revisó, cómo eligió la muestra, qué pasó minuto a minuto.

**Si responde con muy poco,** repreguntar lo concreto que falta; no redactar con huecos
rellenados.

## Paso 3 — Redactar

**Curso.** Estructura de cada tipo en `references/desarrollo_por_tipo.md`. Reglas:

- Prosa continua; listas solo donde la consigna o el contenido lo pidan.
- Párrafos de 4 a 8 oraciones.
- Cada apartado de un informe de curso **cierra con la postura del estudiante**, no con la
  última cita.
- Lo que se toma de una fuente, parafraseado y con su clave. Cita textual solo si es
  imprescindible, corta y con página.

**Empresa.** Estructura de cada tipo en `references/desarrollo_por_tipo_empresa.md`, y la
forma de escribir en `references/escribir_para_decidir.md`:

- **La conclusión primero.** Cada sección y casi cada párrafo abren diciendo qué se encontró,
  no qué se hizo para encontrarlo.
- **Una idea por párrafo**, de 3 a 6 oraciones.
- **La cifra antes del adjetivo.** «Cayó 12 %», no «cayó considerablemente».
- **Los hallazgos numerados y ordenados por impacto**, entre tres y ocho.
- **Cada afirmación con su evidencia al lado**, en la misma frase o la siguiente.
- Si el tipo pide una herramienta de análisis (causas, FODA, cinco fuerzas), pasa antes la
  prueba de las tres preguntas de `references/herramientas_de_analisis.md`. Un cuadro que no
  cambia ninguna recomendación se queda fuera.

**En los dos:** un subtítulo por elemento del esquema, como subtítulo de Markdown de nivel 2
(nivel 3 para sus partes), con la numeración del esquema si la exigieron.

Entregar **dos apartados**, preguntar si van bien o qué cambiar, y seguir con los dos
siguientes.

## Paso 4 — Tablas y figuras

Solo si ayudan a entender (una comparación, un cronograma, un diagrama del proceso).

Tabla, en un solo bloque sin líneas en blanco:

```
**Tabla 1**
*Cronograma de actividades del proyecto*
| Actividad | Semana | Responsable |
|---|---|---|
| Diagnóstico del problema | 1-2 | Ana Ruiz |
*Nota.* Elaboración propia.
```

Figura, también en un solo bloque:

```
**Figura 1**
*Diagrama del proceso propuesto*
[Insertar aquí la Figura 1: diagrama-proceso.png]
*Nota.* Elaboración propia.
```

**En empresa, toda tabla y toda figura lleva su línea «Fuente»**, con la fecha de corte si es
un dato interno, y los totales se comprueban. El detalle en
`references/tablas_y_figuras_empresa.md`:

```
**Tabla 1**
*Órdenes de despacho con retraso, por mes*
| Mes | Órdenes | Con retraso | % |
|---|---|---|---|
| Enero 2026 | 412 | 68 | 16,5 |
| Febrero 2026 | 388 | 91 | 23,5 |
*Fuente.* Sistema de despacho, corte al 31 de marzo de 2026.
```

Cada tabla y figura se menciona en el texto antes de aparecer. El Word pone el formato y deja
resaltada la marca donde va la imagen: decirle cuál va en cada marca.

## Paso 5 — Auditoría anti-IA

Obligatoria antes de guardar. Lista de control y metas en `references/anti_ia.md`. En empresa
cuentan además E1 a E4: jerga vacía, párrafo sin cifra, recomendación sin dueño y adjetivo sin
medida.

```
AUDITORÍA DEL DESARROLLO
Apartados: [N] · Palabras: [N] (meta: [N])
Patrones P0 a P14: [PASA / MARCÓ, con la frase exacta]
Empresa, E1 a E4: [PASA / MARCÓ] · párrafos sin cifra ni hecho: [N] (meta 0)
Oraciones de 8 palabras o menos: [N] %  (meta ≥ 15 %)
Oración más larga: [N] palabras  (máx. 40 en curso, 35 en empresa)
Citas con clave: [N] · [FALTA FUENTE]: [N] · escritas a mano: 0
Empresa: hallazgos sin evidencia: 0 · tablas sin línea «Fuente»: 0
Lo aportado por quien escribe está en cada apartado: SÍ / NO
Estado: OK PARA GUARDAR / RE-REDACTAR
```

Si algo marca, se reescribe antes de guardar. Si dice que suena a IA, se abre la herramienta de
apoyo `humanizador-academico` con `redactar`.

## Paso 6 — Guardar y entregar

1. **Guardar** con `guardar_capitulo`, clave `informe-fase2-desarrollo`. Markdown limpio,
   **sin el título «Desarrollo»** (lo pone el Word), sin portada y sin sección de referencias.
   Hasta 30.000 caracteres por llamada; si pasa, por partes: la primera sin `anadir` y las
   siguientes con `anadir: true`. Si se corrige entero, completo y sin `anadir`.
2. **Comprobar** con `revisar_evidencia` (`capitulo: informe-fase2-desarrollo`) qué
   afirmaciones quedaron sin fuente, y decírselo.
3. **Registrar** con `guardar_avance` (`capitulo: informe-fase2-desarrollo`): un `resumen` de
   dos o tres frases (apartados, postura central o hallazgos principales, lo que quedó
   pendiente). `estado: LISTO` solo si lo da por bueno.
4. **Dar el enlace** con `enlace_del_word`:

```
Tu desarrollo quedó guardado. Aquí puedes ver cómo va tu informe en Word:
[enlace]

Sale con tu portada y las referencias en [norma]. La introducción y el
cierre los escribimos al final. El enlace vence en media hora.
```

## Paso 7 — Cierre

- [ ] ¿Cada subtítulo del esquema tiene su apartado?
- [ ] ¿Cada apartado tiene lo que aportó quien escribe?
- [ ] ¿Toda idea tomada de una fuente lleva su clave?
- [ ] ¿La extensión va de acuerdo con lo acordado?
- [ ] Empresa: ¿hallazgos numerados, por impacto, cada uno con su evidencia?
- [ ] Empresa: ¿cada tabla con su línea «Fuente» y sus totales cuadrados?
- [ ] ¿Pasó la auditoría anti-IA?

Siguiente fase:

> **Proyecto, caso con datos, o casi cualquier informe de empresa:** Fase 3, análisis y
> resultados.
> **Informe de curso o monografía sin comparación ni datos, o informe técnico o normativo sin cifras:**
> directo a la Fase 4.

## Errores que esta skill previene

1. Un informe que es una lista de citas sin la voz de quien lo entrega.
2. Un proyecto contado con actividades que nadie hizo.
3. Cinco apartados con la misma estructura de plantilla.
4. Una cifra sin fuente.
5. Un apartado que responde a otra pregunta que la del esquema.
6. Escribir la introducción antes de saber qué dice el informe.
7. Empresa: un informe que describe datos y no dice qué encontró.
8. Empresa: llamar «causa» a lo que solo es una relación.
9. Empresa: quince hallazgos, de los que no se ejecuta ninguno.
10. Empresa: señalar a una persona donde correspondía señalar el proceso.

## Archivos de referencia

- `references/estilo_preguntas.md` — Cómo se pregunta en esta ruta, según el ámbito.
- `references/integracion_zotero.md` — Claves, norma de citas y cómo se cita un dato interno.
- `references/desarrollo_por_tipo.md` — Curso: qué lleva el desarrollo en cada tipo.
- `references/desarrollo_por_tipo_empresa.md` — Empresa: qué lleva el cuerpo en cada tipo, y qué preguntar antes.
- `references/escribir_para_decidir.md` — Empresa: la conclusión primero, el hallazgo de cinco piezas y los verbos de la causa.
- `references/herramientas_de_analisis.md` — FODA, cinco fuerzas, Ishikawa y las demás: cuándo sirven y cuándo son relleno.
- `references/tablas_y_figuras_empresa.md` — Empresa: la línea «Fuente» y los gráficos que no se hacen.
- `references/anti_ia.md` — Auditoría de patrones de IA.
- `references/confidencialidad.md` — Cómo se escribe un hallazgo sin señalar personas.
