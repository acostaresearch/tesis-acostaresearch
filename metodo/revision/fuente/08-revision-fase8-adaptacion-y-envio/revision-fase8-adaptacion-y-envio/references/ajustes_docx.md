# Comandos de la `_v8` y del reenvío

Todo con Python y `python-docx`; nada de rehacer el documento a mano.
`S=scripts/articulo_docx.py`, `A=scripts/ajustar_docx.py` (rutas reales dentro
de esta skill). Cada archivo de revista va con su `_RESPALDO` (mismo texto,
formato neutro): **un cambio de texto se hace en los dos; uno de formato o de
posición, solo en el de la revista.**

## 1 · Crear el par `_v8` sin tocar la `_v7`

```bash
python3 $S agregar --base ARTICULO_[clave]_v7.docx --md finales.md \
        --perfil REVISTA_[clave].json --out ARTICULO_[clave]_v8.docx   # crea también _v8_RESPALDO
```

`finales.md` lleva las secciones que pide la revista al final (declaraciones,
agradecimientos, disponibilidad de datos); `agregar` las pone antes de
Referencias. Si no hay nada que agregar: `cp` de `_v7` y `_v7_RESPALDO` a
`_v8` y `_v8_RESPALDO`. Si falta el respaldo de la `_v7` (manuscrito que no
salió de la ruta): `$S normalizar ARTICULO_[clave]_v7.docx --out
ARTICULO_[clave]_v7_RESPALDO.docx` (sin perfil = formato neutro).
`ajustar_docx.py` se niega a modificar una `_v7`.

## 2 · Verificar contra el perfil

```bash
python3 $S verificar ARTICULO_[clave]_v8.docx --perfil REVISTA_[clave].json --fuentes inventario.json
```

Controla formato, límite de palabras, secciones exigidas y su orden. Los ✗ se
corrigen y se vuelve a correr; los `!` se revisan a mano (una sección que la
revista no nombra, como Declaraciones, puede ser correcta).

## 3 · Estructura y texto

```bash
python3 $A secciones  --docx ARTICULO_[clave]_v8.docx
python3 $A renombrar  --docx ARTICULO_[clave]_v8.docx --de "Método" --a "Materiales y métodos"
python3 $A mover      --docx ARTICULO_[clave]_v8.docx --seccion "Conclusiones" --antes-de "Referencias"
python3 $A quitar     --docx ARTICULO_[clave]_v8.docx --seccion "Agradecimientos"
python3 $A nivel      --docx ARTICULO_[clave]_v8.docx --seccion "Revisión de la literatura" --nivel 2
python3 $A unir       --docx ARTICULO_[clave]_v8.docx --primera "Resultados" --segunda "Discusión" \
                      --titulo "Resultados y discusión"            # --sin-subtitulo: la segunda pierde su título
python3 $A reemplazar --docx ARTICULO_[clave]_v8.docx --cambios parrafos.json
python3 $A reemplazar --docx ARTICULO_[clave]_v8_RESPALDO.docx --cambios parrafos.json
```

Una sección es su título más todo lo que sigue hasta el siguiente título del
mismo nivel o superior; el nombre se compara sin tildes ni mayúsculas.
Renombrar, mover, quitar, `nivel` y `unir` siguen la estructura de la revista:
el respaldo conserva la de la ruta, salvo que se quite contenido (eso es
texto: también en el respaldo). `nivel` lleva consigo los subtítulos (H2 → H3);
si la sección bajada no queda justo tras la Introducción, `mover --antes-de
"Método"`. Revisar con `secciones` al terminar.

`reemplazar` cambia **párrafos enteros**, sin marcas, conservando su formato:

```json
[{"buscar": "fragmento único del párrafo, copiado de `texto`",
  "reemplazar": "Párrafo nuevo completo, con *cursiva* si hace falta."}]
```

Sirve para recortes, la humanización completa y las citas tecleadas a mano.
Conserva el marcador oculto de cada cita por clave, así que **cada cita del
párrafo tiene que reaparecer tal cual** en `reemplazar` (en cualquier orden);
si falta una, no aplica el cambio y la nombra. Un recorte que quita una cita a
propósito lleva `"quitar_citas": true` y después `$S normalizar ... --fuentes
inventario.json` rehace la lista. Los `[POR CONFIRMAR]` nuevos salen en rojo.
Si un `buscar` no aparece exactamente una vez, lo informa y no lo toca: se
corrige y se repite solo ese.

**Recorte grande** (el perfil da ✗ por límite): plan por sección antes de
tocar nada, `Sección | palabras | qué se quita | ahorro`, con `texto --seccion`
para leer; el autor lo aprueba en un mensaje y se aplica con `reemplazar` en
los dos archivos. Se recorta primero lo repetido entre secciones (cifras de
Resultados repetidas en la Discusión, antecedentes que ya están en la
Revisión) y nunca una cifra, una hipótesis o una limitación. Una sección nueva en un punto dado:
`$S agregar --base ..._v8.docx --md X.md --perfil REVISTA_[clave].json
--posicion antes-de --seccion "Discusión" --out ..._v8b.docx` y se renombran
los dos resultados a `_v8`.

## 4 · Tablas y figuras al final (si el perfil lo pide)

Se hace **después del último `verificar`** (el motor lee como referencia todo
lo que sigue al título Referencias) y **solo en la `_v8`**:

```bash
python3 $A al-final --docx ARTICULO_[clave]_v8.docx --tipo tablas   # figuras | todo
```

Mueve cada tabla (rótulo, título, tabla y nota) a una sección "Tablas" tras las
Referencias, una por página; la llamada del texto queda. `--marcar` deja
`[Tabla N aquí]` donde estaba, si la guía lo pide; `--antes-de-referencias`
las pone antes. Figuras en archivos aparte: se entregan los .png y se quitan
con `--tipo figuras`, dejando solo las leyendas si la guía lo indica.

## 5 · Anonimizar (doble ciego)

```bash
python3 $A anonimizar --docx ARTICULO_[clave]_v8.docx
```

Vacía autor, última modificación y comentarios de las propiedades. **Si el
autor abre y guarda en Word, Word vuelve a poner su nombre**: debe activar
"Quitar información personal al guardar" (Windows: Archivo > Información >
Inspeccionar documento; Mac: Word > Preferencias > Seguridad). En el texto:
autocitas reveladoras según la guía, agradecimientos fuera, institución
descrita por su naturaleza si la delata.

## 6 · Reenvío tras rechazo

Base: el último respaldo (`_v9_RESPALDO` si hubo Fase 9; si no,
`_v8_RESPALDO`; abajo, `_vN`). `[revista]` es una palabra de la revista nueva;
los nombres son los de la Tarjeta.

```bash
python3 $S perfil plantilla > REVISTA_[clave]_[revista].json   # rellenar desde su guía
python3 $S perfil validar REVISTA_[clave]_[revista].json

# Versión de la revista: formato nuevo y citas reconvertidas al estilo nuevo
python3 $S normalizar ARTICULO_[clave]_vN_RESPALDO.docx --perfil REVISTA_[clave]_[revista].json \
        --fuentes inventario.json --out ARTICULO_[clave]_vN_[revista].docx
# Respaldo nuevo: formato neutro, mismo estilo de cita (apa | chicago | vancouver | ieee)
python3 $S normalizar ARTICULO_[clave]_vN_RESPALDO.docx --estilo vancouver \
        --fuentes inventario.json --out ARTICULO_[clave]_vN_[revista]_RESPALDO.docx
python3 $S verificar ARTICULO_[clave]_vN_[revista].docx --perfil REVISTA_[clave]_[revista].json \
        --fuentes inventario.json
```

Las citas por clave se reconvierten solas (APA → Vancouver renumera por orden
de aparición) aunque el Word se haya editado. Las **tecleadas a mano** (Word
que no salió de la ruta, o pegadas después) no tienen clave: se convierten con
`reemplazar` y un `cita_[revista].json` (un cambio por párrafo con citas y uno
por referencia; `estilos_cita.md`). Después: estructura del perfil nuevo
(`renombrar`, `mover`, `nivel`, `unir`), recorte si el límite es menor (en los
dos archivos) y, al final, `al-final` y `anonimizar` si se piden. Revisar con
`esquema` que el título del artículo no quedó como subtítulo.

## 7 · Versión en inglés de una revista bilingüe

`verificar --perfil` compara con `estructura` (en español). Para la `_en`,
una copia del perfil con `estructura` = `estructura_en`:

```bash
python3 -c "import json;p=json.load(open('REVISTA_[clave].json'));p['estructura']=p.get('estructura_en') or p['estructura'];json.dump(p,open('REVISTA_[clave]_en.json','w'),ensure_ascii=False,indent=1)"
python3 $S verificar ARTICULO_[clave]_v8_en.docx --perfil REVISTA_[clave]_en.json --fuentes inventario.json
```
