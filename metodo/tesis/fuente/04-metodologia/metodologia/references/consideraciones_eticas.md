# Consideraciones éticas

Esta referencia documenta cómo redactar la sub-sección 3.7. Es estándar en pregrado peruano contemporáneo y los asesores la observan si falta.

## Estructura obligatoria

Cinco elementos en prosa continua, no listados:

### 1. Principios éticos generales

Referencia al **Informe Belmont** (Belmont Report, 1979), citado con la clave de su ficha en la biblioteca, que articula tres principios:

- **Respeto a las personas**: reconocer la autonomía del participante para decidir si participa.
- **Beneficencia**: el estudio busca beneficio y minimiza daño.
- **Justicia**: distribución equitativa de beneficios y cargas de la investigación.

Adicionalmente, mencionar la **Declaración de Helsinki** (Asociación Médica Mundial, 1964, con revisiones) **solo si el estudio es biomédico o clínico** (ver Paso 8 del SKILL.md), también con su clave.

Como toda fuente, el Informe Belmont, la Declaración de Helsinki y la ley de protección de datos del país se buscan con `buscar_fuentes` o `mis_fuentes`. Si no están en la biblioteca, se le pide al tesista que los agregue a su Zotero o a «Mis fuentes»; mientras tanto, la afirmación va con `[FALTA FUENTE]` y se le avisa en el chat.

### 2. Consentimiento informado

Detallar:

- Cómo se obtuvo (físico firmado, digital con check, embebido en el instrumento).
- Qué información se proporcionó al participante (objetivo del estudio, duración, derechos, contacto del investigador).
- Voluntariedad: el participante puede retirarse sin consecuencias.

### 3. Anonimización y confidencialidad

Cómo se protegen los datos personales:

- **Anonimización**: ningún dato identificable se incluye en el análisis.
- **Codificación**: cada participante recibe un código (P001, P002...) y solo el investigador conoce la equivalencia.
- **Almacenamiento**: archivos cifrados, acceso restringido al investigador y asesor.
- **Tiempo de conservación**: típicamente 5 años según reglamentos universitarios.

### Caso especial: aplicación virtual con Google Forms o Microsoft Forms + anonimización

Cuando la modalidad de aplicación es virtual con Google Forms o Microsoft Forms y el tesista declara "anonimización completa", la skill debe **advertir proactivamente** sobre la configuración técnica necesaria y declararla en la sub-sección 3.7:

1. **Desactivar la opción "Recolectar dirección de correo"** en la configuración del formulario. Por defecto, Google Forms registra el correo del usuario si está logueado con cuenta Google, lo cual rompe la anonimización.
2. **No incluir ítems que pidan datos identificables**: nombre, DNI, código de estudiante, contacto personal.
3. **Limitar variables sociodemográficas a las estrictamente necesarias**: grado y sección son aceptables porque no identifican individuos; edad exacta y otros datos pueden permitir reidentificación en muestras pequeñas.
4. **Configurar acceso restringido al enlace del formulario** para evitar respuestas externas no controladas.

Esta advertencia se redacta como parte de la sub-sección 3.7, no como nota al pie. Es contenido sustantivo del capítulo.

### 4. Riesgos y beneficios para los participantes

- **Riesgos previsibles**: en estudios educativos suele ser nulo o mínimo (responder un cuestionario no implica daño físico ni psicológico relevante).
- **Beneficios directos**: aprendizaje, reflexión, retroalimentación al participante.
- **Beneficios indirectos**: aporte al conocimiento educativo, mejora institucional, base para políticas.

Declarar explícitamente si hay riesgos identificados y cómo se mitigan.

### 5. Aprobación institucional

Si la universidad tiene Comité de Ética en Investigación (cada vez más común en pregrado peruano), mencionar:

- Que el estudio fue (o será) sometido al comité.
- Número de aprobación si ya existe.
- Si no aplica comité, mencionar que el estudio sigue los reglamentos internos de investigación de la facultad.

## Caso especial: población de menores de edad

Cuando la población son menores de edad, agregar dos puntos:

### Asentimiento informado del menor

Documento simplificado, redactado en lenguaje accesible para el menor, donde el propio estudiante declara aceptar participar. Debe incluir:

- Explicación del estudio en lenguaje claro.
- Derecho a no responder cualquier pregunta.
- Derecho a retirarse en cualquier momento.
- Que sus respuestas son confidenciales.

### Consentimiento informado del padre/madre/tutor

Documento formal donde el adulto responsable autoriza la participación del menor. Más detallado que el asentimiento.

### Doble registro

Ambos documentos (asentimiento + consentimiento) se conservan archivados como anexos de la tesis. Sin estos, la aplicación no puede proceder.

## Plantilla de redacción

> El presente estudio se desarrolla bajo los principios éticos articulados en el Informe Belmont [AR…], que reconoce el respeto a las personas, la beneficencia y la justicia como base de toda investigación con seres humanos. [Solo si es biomédico o clínico: añadir la Declaración de Helsinki con su clave.]
>
> En cumplimiento del principio de respeto a las personas, se obtuvo consentimiento informado de cada participante antes de la aplicación del instrumento. [Adaptar a respuesta real: físico/digital/embebido]. El documento de consentimiento incluyó información sobre el objetivo del estudio, la duración aproximada de la participación, los derechos del participante (voluntariedad, anonimato, retiro sin consecuencias) y los datos de contacto del investigador para consultas.
>
> [Si menores: agregar párrafo sobre doble exigencia de asentimiento y consentimiento]
>
> Para garantizar la confidencialidad, todos los datos recogidos serán [anonimizados/codificados]. [Detallar mecanismo]. Los archivos digitales se conservarán en almacenamiento cifrado con acceso restringido al investigador y al asesor durante un periodo de cinco años, tras el cual serán eliminados.
>
> Los riesgos previsibles para los participantes son [mínimos/nulos], dado que [justificación]. Los beneficios directos incluyen [aprendizaje, reflexión]. Los beneficios indirectos contemplan el aporte al conocimiento sobre [tema] en el contexto [país/región].
>
> Finalmente, el estudio [se sometió / se someterá] al Comité de Ética en Investigación de [universidad], conforme a los reglamentos institucionales vigentes. [O bien: dado que la universidad no cuenta con comité formal, el estudio se rige por los reglamentos internos de investigación de la facultad].

## Reglas críticas

- **Toda recolección con personas exige consentimiento informado**, sin excepción.
- **Menores de edad exigen DOBLE documento**: asentimiento + consentimiento de padres.
- **Anonimización es preferible** a codificación cuando es operativamente posible.
- **NO inventar número de aprobación de comité** si no se ha tramitado. Decir "se gestionará" o "se gestionó con fecha [fecha]".
- **Datos identificables solo se justifican** en estudios de caso muy específicos y siempre requieren justificación ética adicional.
