# Humanización de la sección

El artículo se redacta en **español** y cada fase humaniza **solo la sección
que acaba de escribir**, antes de pasarla al Word. Lo que ya se humanizó en
fases anteriores no se vuelve a tocar.

## Qué herramienta se usa (la primera que esté disponible)

1. **Skill `humanizador-academico`** (viene en el paquete): se invoca sobre el
   texto de la sección con esta indicación: *"una sección de artículo, una
   ronda, bloques de hasta 10 párrafos, el autor aprueba cada bloque en un
   mensaje"*. Una sección de fase cabe en 1 o 2 bloques. Se respetan sus reglas
   duras (no añade datos ni citas; no reescribe lo que no tiene patrones).
2. **Servidor Acosta conectado** (`humanizar_mi_documento`): si el cliente lo
   tiene, se usa sobre la sección.
3. **Ninguna de las dos** (chat sin la skill): se aplica la lista de control de
   abajo, una pasada sobre la sección completa.

Textos en **inglés** (abstract, traducción, cover letter, respuesta a
revisores en inglés): `humanizador-academico-ingles` en su *modo breve*.

**Revisión profunda opcional:** en la Fase 8, antes de enviar, el autor puede
pedir la pasada completa del humanizador sobre todo el manuscrito (hasta tres
rondas). Es la única vez que se trabaja el documento entero.

## Medición (opcional, orienta; no es meta que perseguir)

```bash
python3 scripts/medir_estilo.py seccion.md        # ruta real del script de esta skill
```

Reporta por párrafo la dispersión del largo de oración, el porcentaje de
oraciones cortas, el largo medio de palabra y las palabras funcionales, y marca
los párrafos uniformes. Señales de alarma: dispersión < 0.35, ninguna oración
de 8 palabras o menos en un párrafo de más de 5, largo medio de palabra > 5.6,
palabras funcionales < 38 %. Se corrige el párrafo marcado, no la sección
entera.

## Lista de control: los 14 patrones, más la familia 0

Se recorre la lista una vez sobre la sección completa. En el chat solo se
informa qué patrones se encontraron y cuántos párrafos se tocaron.

**Los tres que la medición no detecta y hay que buscar leyendo:**

- [ ] **0 · Paralelismo de plantilla.** Párrafos con la misma arquitectura
      interna. Es el patrón más fuerte y el más frecuente en el sustento de
      hipótesis.
- [ ] **0b · El tic de la reescritura.** El patrón que aparece en la salida
      propia al corregir, no en el original. Revisar sus formas una por una.
- [ ] **0c · La frase-etiqueta y su desarrollo.** Frase corta que rotula, y
      detrás el desarrollo. Seis párrafos así pueden medir perfecto y seguir
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
Antes de "corregir" algo, comprobar que no sea uno de estos.

## Cuándo parar

Una pasada de corrección y una de revisión de lo reescrito. Si un párrafo sigue
uniforme tras dos enfoques distintos, se deja y se dice. Un texto sobrecorregido
se nota tanto como uno sin corregir.
