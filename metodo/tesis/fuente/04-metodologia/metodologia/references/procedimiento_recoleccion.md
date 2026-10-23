# Procedimiento de recolección

Esta referencia documenta cómo redactar la sub-sección 3.6 a partir de las respuestas reales del tesista. La skill NO genera plantillas genéricas: pregunta uno por uno los 5 elementos y construye prosa específica al contexto.

## Los 5 elementos obligatorios

### 1. Coordinación inicial

Cómo se solicitó (o se solicitará) el permiso para aplicar el instrumento. Debe incluir:

- A quién se dirigió la solicitud (autoridad académica, gerencia, director, etc.).
- Tipo de documento (carta formal, oficio, correo institucional).
- Estado actual (gestionada, en trámite, pendiente).

Pregunta de la skill al tesista (texto libre):

> "¿A quién pediste o pedirás autorización para aplicar el instrumento? Indica el cargo y la institución. ¿Ya tienes la carta de autorización o está pendiente?"

### 2. Pilotaje

Aplicación previa del instrumento a un grupo pequeño para detectar problemas. No siempre se exige, depende del asesor y reglamento.

Pregunta de la skill (single_select):

- "Sí, aplicaré pilotaje con un grupo pequeño antes de la aplicación final"
- "No, mi asesor no exige pilotaje"
- "No estoy seguro, depende de mi asesor"

Si "sí", preguntar cuántas personas y de qué perfil similar.

### 3. Aplicación

Cómo, cuándo y dónde se aplicará el instrumento.

Preguntas de la skill:

- Modalidad (single_select): presencial / virtual / híbrida.
- Fechas tentativas (texto libre).
- Duración estimada de cada aplicación (texto libre).

### 4. Consentimiento informado

Toda recolección con personas exige consentimiento. Si la población son menores de edad, exige consentimiento del padre/madre/tutor MÁS asentimiento del menor.

Pregunta de la skill (single_select):

- "Sí, tengo formato de consentimiento informado físico o digital"
- "Sí, mi instrumento incluirá una primera sección de consentimiento"
- "No, mi población son menores de edad: necesito asentimiento + consentimiento de padres"

Si la población son menores, advertir sobre la doble exigencia.

### 5. Resguardo de datos

Cómo se protegen los datos personales recogidos.

Pregunta de la skill (single_select):

- "Anonimización completa: los participantes no son identificables"
- "Codificación: cada participante tiene un código que solo el investigador conoce"
- "Datos identificables (requiere justificación ética adicional)"

## Plantilla de redacción

A partir de las respuestas reales, la skill redacta prosa continua. **Esta plantilla muestra el contenido de cada etapa, no sus aperturas**: al redactar, cada etapa se abre con una de las variantes rotativas del Paso 7 del SKILL.md (nunca "La primera / La segunda / La tercera…" en serie, que es paralelismo de plantilla), sin negritas dentro de los párrafos, y con al menos una cita metodológica con su clave `[AR…]` (Paso 10: cobertura por sub-sección).

> El procedimiento de recolección de datos contempla cinco etapas. La primera consiste en la **coordinación inicial** con [persona/institución], a quien se ha remitido [tipo de documento] solicitando autorización formal para aplicar el instrumento en la población objeto del estudio. [Estado del trámite].
>
> La segunda etapa corresponde al **pilotaje** del instrumento, [aplicar/no aplicar] con un grupo de [N] personas con perfil similar a la muestra final, con el propósito de detectar problemas de comprensión de los ítems, tiempo de aplicación y necesidad de ajustes. [Si no aplica, justificar].
>
> La tercera etapa es la **aplicación efectiva del instrumento**, prevista para [fechas tentativas], en modalidad [presencial/virtual/híbrida]. La duración estimada de cada aplicación es de [minutos]. [Si presencial: lugar. Si virtual: plataforma].
>
> La cuarta etapa contempla el **consentimiento informado**. [Adaptar según respuesta del tesista. Si menores: doble exigencia].
>
> Finalmente, la quinta etapa consiste en el **resguardo de los datos** recogidos. [Adaptar según anonimización/codificación].

## Caso especial: población de menores de edad

Cuando la población son menores de edad (típico en estudios de secundaria), la skill debe agregar:

- **Asentimiento del menor**: documento firmado por el propio estudiante que acepta participar voluntariamente.
- **Consentimiento del padre/madre/tutor**: documento firmado por el adulto responsable.
- **Doble registro**: ambos documentos se conservan archivados.
- **Reglamento institucional**: si la I.E. tiene normas específicas, mencionarlas.

## Reglas críticas

- **NO inventar fechas, nombres de personas o instituciones**. Solo lo que el tesista declare.
- **NO usar plantillas genéricas tipo "se aplicará el instrumento a los participantes"**. La prosa debe ser específica al contexto del tesista.
- **Si el tesista no tiene aún la carta de autorización**, escribir "está en trámite" o "se gestionará al inicio del periodo de aplicación", no fingir que está obtenida.
- **El consentimiento informado debe estar siempre presente**. Si el tesista dice que no lo va a usar, advertir que es obligatorio.
