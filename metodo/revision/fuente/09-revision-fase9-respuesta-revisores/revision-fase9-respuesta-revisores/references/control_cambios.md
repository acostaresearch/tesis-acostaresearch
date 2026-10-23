# Control de cambios en Word con `control_cambios.py`

Se lee en el Paso 3. El manuscrito revisado **nunca se regenera**: regenerarlo
destruye formato, numeración y citas, y los cambios llegarían sin marcar. El
script edita el XML del .docx enviado en su sitio y marca cada cambio como
revisión de Word (`w:ins` / `w:del`) a nombre del autor, con fecha. Solo
necesita Python 3 y `python-docx`; vale en claude.ai, Claude Code, la API u
otro cliente. Probado abriendo el resultado en Microsoft Word: muestra las
inserciones, las eliminaciones y los comentarios en el margen.

## 1 · Escribir `cambios.json`

```json
[
  {"buscar": "una universidad pública peruana",
   "reemplazar": "una universidad privada peruana",
   "comentario": "Revisor 1, obs. 3"},
  {"buscar": ", seleccionados por conveniencia", "reemplazar": ""},
  {"buscar": "Se aplicó la escala RED-Tecnoestrés en 2023.",
   "reemplazar": "Se aplicó la escala *RED-Tecnoestrés* entre marzo y mayo de 2023."},
  {"insertar_despues": "fragmento único del párrafo anterior",
   "texto": "Párrafo nuevo completo, con *cursiva* si hace falta."}
]
```

- `buscar`: texto **exacto** del manuscrito, dentro de un solo párrafo. Se copia
  de `articulo_docx.py texto enviado.docx --seccion "X"`, no de memoria. No
  importa que Word lo tenga partido en fragmentos con formatos distintos;
  espacios dobles o duros cuentan como uno.
- `reemplazar`: el texto final. Solo se marca lo que cambia (por palabras): lo
  común queda intacto con su formato, incluidas cursivas y negritas. `""`
  elimina; si `buscar` es el párrafo entero, se elimina el párrafo.
- `*cursiva*` y `**negrita**` en `reemplazar` o `texto` fuerzan ese formato; el
  resto hereda el del texto vecino.
- Si `buscar` aparece varias veces, se cambia la primera y se avisa: agregar
  contexto, o `"todas": true`. Para un valor repetido en tablas: `"tabla": 3,
  "fila": 2, "columna": 4` (desde 1, contando la fila de encabezado) apunta a una
  celda; `"ocurrencia": n` toma la n-ésima aparición del texto.

  ```json
  {"buscar": ".81", "reemplazar": ".83", "tabla": 3, "fila": 4, "columna": 2,
   "comentario": "Revisor 1, obs. 2: HTMT corregido"}
  ```

  `tabla` es la N-ésima tabla del Word en orden de aparición (la que el texto
  llama «Tabla 3» suele ser la tercera; comprobarlo con `esquema`), igual en la
  `_v8` y en el respaldo aunque las tablas se hayan movido al final. Una celda
  combinada a lo ancho cuenta una vez. `ocurrencia` se cuenta sobre el documento tal
  como va quedando: si un cambio anterior del mismo JSON ya cambió una de esas
  apariciones, cuenta una menos (preferir la celda, o poner los de
  `ocurrencia` primero). Un número de tabla, fila o columna que no existe sale
  en NO ENCONTRADOS con el motivo.
- `insertar_despues`: un fragmento del párrafo ancla; el nuevo párrafo toma su
  formato (o el del siguiente párrafo de cuerpo si el ancla es un título).
  `"formato_de": "siguiente"` lo fuerza.
- `comentario` (opcional): nota en el margen, a nombre del autor, anclada al
  cambio. Útil para remitir al número de observación. `--sin-comentarios` los
  omite si la revista no los quiere.
- **Evitar cambios que se pisen** (que un `buscar` caiga sobre el texto que otro
  acaba de insertar): se aplican bien, pero `validar` marca ✗ el primero porque
  su texto final ya no existe tal cual. Mejor unirlos en un solo cambio.

## 2 · Aplicar

```bash
C=scripts/control_cambios.py      # ruta real dentro de esta skill
python3 $C aplicar --docx ARTICULO_[clave]_v8.docx --cambios cambios.json \
        --autor "Nombre Apellido" --out ARTICULO_[clave]_v9.docx
```

Informa `✓` por cada cambio y, al final, los **NO ENCONTRADOS** con una pista
("coincide hasta «…»; ahí esperabas «X» y el documento dice «Y»"). No aborta: se
corrigen esos `buscar` en un `cambios2.json` y se aplican **sobre la `_v9`**
(`--docx ..._v9.docx --out ..._v9b.docx`, y luego se renombra).

## 3 · Validar (no se salta)

```bash
python3 $C validar --docx ARTICULO_[clave]_v9.docx --original ARTICULO_[clave]_v8.docx \
        --cambios cambios.json --autor "Nombre Apellido"
```

Comprueba que el archivo abre (ZIP y XML íntegros), cuenta inserciones y
eliminaciones **por autor**, verifica que **rechazando los cambios del autor se
recupera exactamente el original** (si no, muestra la frase cambiada sin
marcar: `…universidad [-pública-]{+privada+}`) y que, **aceptando todo**,
aparece cada `reemplazar` y desaparece cada `buscar`. Debe terminar en
`RESULTADO: VALIDADO`.

## 4 · Ver cómo queda aceptado

```bash
python3 $C aceptar --docx ARTICULO_[clave]_v9.docx --out limpio.docx
python3 scripts/articulo_docx.py verificar limpio.docx --limite N
python3 scripts/articulo_docx.py texto limpio.docx --seccion "Métodos"
```

`limpio.docx` es solo para revisar (o para la segunda ronda si la revista pide
la versión limpia); lo que se envía es la `_v9` con las marcas, salvo que la
revista pida ambas.

## 5 · Poner al día el respaldo

```bash
python3 $C respaldo --docx ARTICULO_[clave]_v8_RESPALDO.docx --cambios cambios.json \
        --out ARTICULO_[clave]_v9_RESPALDO.docx
```

Aplica el mismo JSON al respaldo neutro (sin comentarios), acepta todo y
comprueba que cada texto nuevo esté: termina en `RESPALDO: AL DÍA`. Se eligió
así, y no regenerar el respaldo desde la versión aceptada, porque conserva el
formato neutro y la posición original de tablas y figuras. Si hubo varios JSON
(`cambios2.json`), se aplican en el mismo orden, cada uno sobre la salida
anterior. Un `buscar` que cae en texto que solo cambió en la `_v8` (tablas al
final, anonimización) se ajusta al texto del respaldo.

## Comentarios del revisor dentro del Word

```bash
python3 $C comentarios --docx enviado.docx
```

Lista cada comentario con su autor y el texto al que está anclado: son
observaciones que van a la matriz igual que las de la carta del editor.

## Segunda ronda y cambios de otros

El script convive con marcas previas: si el texto a cambiar está dentro de una
inserción de otra persona, anida la eliminación como hace Word y parte esa
inserción sin reescribirla. Lo que el mismo autor insertó en esta sesión y
vuelve a cambiar simplemente se ajusta, sin marcas sobre marcas.

## Si no hay Python (modo C)

Se entrega la tabla `Sección | Texto actual | Texto nuevo`, una fila por
cambio. El autor activa **Revisar > Control de cambios** en Word, busca cada
"texto actual" (Ctrl+F) y pega el nuevo; luego repite los mismos cambios en el
respaldo con el control de cambios apagado.
