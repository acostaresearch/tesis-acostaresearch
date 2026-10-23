# El documento en cadena

Regla de toda la ruta.

## Un archivo que crece

El artículo vive en **un solo .docx que crece fase a fase**. La Fase 2 lo crea
con `articulo_docx.py nuevo`; cada fase siguiente lo recibe y le añade su
sección con `articulo_docx.py agregar`, que guarda la versión siguiente sin
tocar lo anterior.

```
ARTICULO_[clave]_v[N].docx            formato de la revista (perfil)
ARTICULO_[clave]_v[N]_RESPALDO.docx   mismo texto, formato neutro (por si hay rechazo)
N = número de la fase que lo produjo
```

Las dos versiones avanzan juntas: el motor las actualiza en la misma llamada
(`--perfil REVISTA_[clave].json`). El investigador trabaja sobre la primera; la
segunda solo se usa si hay que reenviar a otra revista.

Nunca se sobrescribe una versión: el investigador conserva el historial.

## Estructura según la fase

| Al cerrar | Contiene |
|---|---|
| Fase 2 | Título provisional · Introducción · Referencias |
| Fase 4 | + Métodos (protocolo PRISMA, criterios, búsqueda, selección, análisis) |
| Fase 5 | + Resultados: Figura 1 PRISMA, tablas de indicadores o de estudios incluidos, síntesis |
| Fase 6 | + Discusión por pregunta de revisión o eje temático + Limitaciones |
| Fase 7 | Título con el tipo de revisión · Resumen estructurado · Abstract · ... · + Conclusiones |
| Fase 8 | Ajustado a la guía de la revista; página de título aparte; checklist PRISMA |

No hay Fase 3: la Fase 4 recibe la `_v2` y entrega la `_v4`
(`--out ARTICULO_[clave]_v4.docx`).

Las secciones que todavía no existen **no se anuncian con encabezados vacíos**.

## Al empezar cada fase

1. `articulo_docx.py esquema ARTICULO_..._vN.docx --acronimos`: estructura,
   tablas, figuras, número de referencias, pendientes y acrónimos.
2. Leer de la Ficha y la Matriz el estilo de cita, el término unificador (en estudios empíricos) y el
   tipo de estudio. **No se vuelven a preguntar.**
3. `articulo_docx.py texto ... --seccion "X"` solo para las secciones que la
   fase necesita leer de verdad (p. ej. la Discusión lee Resultados).

## Citas y referencias

Las citas se escriben **por clave** (`[F012]`, `[AR51541814:n]`,
`[F012:p. 45]`), nunca a mano: el motor (`--fuentes inventario.json`) las
convierte al estilo del perfil y arma él solo la lista de referencias con todo
lo citado, ordenada y sin repetidos. Si cambia la revista y su estilo, el
motor reconvierte las citas del Word existente. Las fuentes llegan por
la plataforma Acosta, el Zotero o Mendeley del investigador o la web con DOI
verificado (ver `fuentes_y_citas.md`). Al final, `referencias.py exportar`
devuelve lo citado a su gestor.

## La matriz de trazabilidad va aparte

`TRAZABILIDAD_[clave].xlsx`, siete columnas (ver `trazabilidad.md`
en las fases que citan). No se integra al manuscrito: es material de
auditoría. La crea la Fase 2; cada fase posterior que agregue citas le añade filas
conservando los ID de fuente (F001, F002...).

## Al entregar

Una línea: qué versión es, qué contiene y qué subir en la fase siguiente.

> ARTICULO_tecnoestres_v4.docx — hasta Métodos con la Tabla 1. Para la Fase 5
> súbelo junto con las salidas de tu análisis.
