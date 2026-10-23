# Auditoría de patrones de IA

Se lee en el paso del humanizador, y se aplica a **todo texto que esta fase
escriba**. No es una relectura: es escribir, guardar, leer los avisos del
servidor y corregir esos párrafos.

## El catálogo vive en la skill `humanizador-academico`

**No se duplica aquí.** Esa skill tiene el catálogo completo; con el conector se
pide con `redactar` solo cuando el autor quiere humanizar un texto entero. Este
archivo solo trae la lista de control, para verificar que no quedó ninguno sin
revisar.

## Medición: la hace el servidor

No se mide ni se imprimen métricas en el chat (dispersión, largo de palabra,
palabras funcionales), y no hay scripts que correr. Al guardar, `guardar_capitulo`
devuelve los AVISOS DE REDACCIÓN que calcula el servidor: vocabulario de modelo,
rayas, párrafos que abren igual, antecedentes en fila con la misma plantilla y
muletillas de todo el manuscrito. Esos párrafos se corrigen con
`reescribir_parrafos`, sin reenviar la sección entera.

La señal a ojo, antes de guardar, es la uniformidad: si todas las oraciones del
párrafo miden entre 30 y 55 palabras, es paralelismo de plantilla.

## Lista de control: los 14 patrones, más la familia 0

Se revisan **todos**, uno por uno, sobre el texto ya escrito. Marcar cuál se
encontró y qué se hizo.

**Los tres que la medición no detecta y hay que buscar leyendo:**

- [ ] **0 · Paralelismo de plantilla.** Párrafos con la misma arquitectura
      interna. Es el patrón más fuerte y el más frecuente en el sustento de
      hipótesis.
- [ ] **0b · El tic de la reescritura.** El patrón que aparece en la salida
      propia al corregir, no en el original. Revisar sus formas una por una.
- [ ] **0c · La frase-etiqueta y su desarrollo.** Frase corta que rotula, y
      detrás el desarrollo. Seis párrafos así pueden pasar sin avisos y seguir
      sonando a máquina.

**Los catorce numerados:**

- [ ] **1 · Inflar la importancia**
- [ ] **2 · Gerundios colgados al final**
- [ ] **3 · Lenguaje promocional**
- [ ] **4 · Atribución vaga**
- [ ] **5 · Evitar el verbo ser**
- [ ] **6 · Nominalización en cadena** — el que más sube el largo de palabra y
      más baja las funcionales
- [ ] **7 · Regla de tres ornamental**
- [ ] **8 · Rotación de sinónimos**
- [ ] **9 · Rayas largas**
- [ ] **10 · Contrastes fabricados y falsa profundidad**
- [ ] **11 · Conectores en exceso**
- [ ] **12 · Cierres optimistas**
- [ ] **13 · Restos de chatbot**
- [ ] **14 · Formato**

## Las dos reglas duras que se traen de esa skill

1. **Humanizar es restar.** Al reescribir **no se introduce ningún dato, cifra,
   nombre ni cita nueva**. Si el texto se alarga, se hizo mal.
2. **La reincidencia se vigila en la propia salida.** El patrón 0b existe
   precisamente porque la corrección introduce sus propios tics. Después de
   reescribir, auditar lo reescrito.

## Falsos positivos del texto académico

Un artículo científico tiene rasgos que **no** son patrones de IA y no se
corrigen: terminología repetida a propósito (el acrónimo del constructo se
repite y así debe ser), estructura fija de los apartados, y la voz impersonal.
La skill `humanizador-academico` los detalla; conviene revisarlos antes de
"corregir" algo que estaba bien.

## Cuándo parar

**Si tras dos reescrituras con enfoques distintos un párrafo sigue con avisos,
se dice con honestidad** en vez de seguir
retorciendo la prosa. Un texto sobrecorregido se nota tanto como uno sin
corregir.
