# El ámbito empresa dentro de la Ruta del Informe

16 de septiembre de 2026. **Las skills están escritas y los puntos 1 a 8 (backend y web) están
hechos y probados, sin comitear ni desplegar.** Ver «Estado del backend» al final.

## Qué se decidió

El informe empresarial **no es un producto aparte**: es un segundo ámbito de la Ruta del
Informe, con la misma licencia, el mismo grupo y las mismas cinco fases que el estudiantil.

- La Fase 0 pregunta primero si el informe es **para un curso o para una empresa**, y según eso
  cambian las preguntas, la ficha, la portada y la revisión.
- Las cinco skills conservan su `name` (`informe-fase0-encargo` … `informe-fase4-cierre`) y su
  título. **No hay claves nuevas**: los proyectos que ya existen no se tocan.
- Los pasos que solo aplican a un ámbito lo dicen en su título («(solo empresa)») y se saltan en
  el otro.
- En empresa, la Fase 4 hace lo que en el diseño separado eran dos fases: recomendaciones, plan
  de acción, riesgos, limitaciones, **resumen ejecutivo** y la revisión contra los términos de
  referencia.

Lo que ya no hace falta, frente al producto aparte: un cuarto perfil, un producto nuevo, la
herramienta `documentos_de_la_empresa` (se usa `material_del_curso`) y las claves
`empresarial-*`. El diseño separado quedó en `_retirado/empresarial-separado-2026-09-16/`.

## La regla que protege a los estudiantes

**La rama de curso guarda exactamente lo mismo que hoy.**

El esquema de `guardar_avance` del informe (`ESQUEMA_GUARDAR_AVANCE_INFORME`, en `mcp.tools.js`)
tiene `additionalProperties: false` y el tipo solo admite `curso`, `proyecto` y `caso`. Si la
rama de curso mandara un campo nuevo —por ejemplo `ambito: "curso"`—, el servidor de hoy
rechazaría el guardado. Por eso:

- en curso no se manda `ambito`: **un informe sin ámbito es de curso**;
- solo la rama de empresa manda `ambito: "empresa"` y los campos nuevos;
- los `datos` que no están registrados en `project.etapas.js` (la lista de datos por pedir, las
  limitaciones, los supuestos) van en el `resumen` de la fase, que no se descarta.

Así, **las skills nuevas se pueden subir antes que el backend sin romper la ruta de curso.** Lo
que no funcionaría hasta el backend es la rama de empresa: `guardar_avance` rechazaría su ficha
y la skill diría «no se guardó».

## Lo que falta en el backend

Por orden. **Las tres primeras son imprescindibles** para que la rama de empresa funcione.

| # | Qué | Dónde | Por qué |
|---|---|---|---|
| 1 | Aceptar la ficha de empresa: `ambito` (`curso` \| `empresa`), los tipos nuevos (`diagnostico`, `gestion`, `factibilidad`, `mercado`, `tecnico`, `auditoria`, `avance`, `incidente`, `sostenibilidad`, `duediligence`, `desempeno`, `clima`, `otro`) y los campos `empresa`, `sector`, `destinatario`, `preparadoPor`, `cargo`, `periodo`, `confidencial` (booleano), `decision` (300), `alcance` (1500) y `terminos` (1500) | `project.ficha-informe.js` (Zod) y `ESQUEMA_GUARDAR_AVANCE_INFORME` en `mcp.tools.js` | Hoy los dos rechazan la ficha de empresa |
| 2 | **Que `mi_proyecto` escriba la línea «Ámbito: empresa»** y las líneas de la ficha de empresa, y que **no pida el docente** cuando el ámbito es empresa | `lineasDeFicha` en `project.ficha-informe.js` | Las cinco skills deciden el ámbito leyendo esa línea. Y hoy, sin docente guardado, `mi_proyecto` le dice a Claude que lo pregunte |
| 3 | Nombres de los tipos nuevos | `NOMBRE_DE_TIPO` en `project.ficha-informe.js` | Si no, `mi_proyecto` enseña «Tipo: diagnostico» tal cual |
| 4 | Portada de empresa: la empresa, el título, el tipo, «Preparado para», «Preparado por» con su cargo, el periodo, la ciudad y la fecha, y la marca «Documento confidencial — uso interno» si `confidencial` | `portadaDeInforme` en `project.docx.js` y `datosDePortadaInforme` en `project.service.js` | Hoy saldría con «Curso:» y «Docente:» vacíos y firmada por quien tiene la cuenta |
| 5 | Título «Resumen ejecutivo» para `informe-resumen` cuando el ámbito es empresa | `perfil.seccionesAparte` se usa en `armarWord`: el título tiene que depender de la ficha | Hoy sale «Resumen» |
| 6 | Textos que dicen solo «estudiantil», «docente» o «curso»: el encabezado «Ruta del informe estudiantil» del método, las descripciones de `material_del_curso` y de `formato_de_la_universidad`, y el aviso de `project.material.js` | `mcp.tools.js`, `project.material.js`, `project.consejos.js` | Que la herramienta hable también de los términos de referencia y de la plantilla de la empresa |
| 7 | Etiquetas de la plantilla para los campos de empresa | `project.portada-auto.js` | Solo si una empresa sube su plantilla con portada |
| 8 | En el panel, un bloque de ficha para empresa (empresa, destinatario, entrega) en vez de curso y docente | `mi-tesis.html` (web) | Hoy enseña solo curso y docente |

**Pruebas:**
- antes de tocar nada, congelar el informe en instantáneas, como tesis y artículo (hoy
  `tests/productos.*.instantanea.test.js` no lo recorren);
- `informe.ficha.test.js`: una ficha de empresa se guarda y se lee, y una de curso sale
  **idéntica** a hoy;
- `informe.word.test.js`: portada de empresa y título «Resumen ejecutivo»; la de curso, igual.

**Sin migración de base de datos:** todo va en la columna `Project.fichaInforme`, que ya es JSON.

## Cómo se publica

1. Backend, con los puntos 1 a 3 como mínimo (mejor 1 a 6), `npm test` completo y las
   instantáneas de curso sin cambios.
2. `node skills/informe/verificar.js`, sin FALLO.
3. En `/admin` → Capítulos, **«cambiar archivo»** en las cinco fases del grupo del informe,
   **las cinco**: la Fase 0 ya no es la de antes y las demás dan por hecho el ámbito. Sustituye
   también el pendiente de «resubir fases 0 y 4».
4. Prueba de punta a punta con la cuenta del piloto:
   - un informe de curso completo, para confirmar que **nada cambió** para el estudiante;
   - un diagnóstico de empresa con documentos subidos;
   - un estudio de factibilidad con VAN, TIR y sensibilidad;
   - pedirle a propósito el tamaño de un mercado sin darle datos y comprobar que **no lo
     inventa**.

## Si hay que volver atrás

Las cinco skills tal como estaban antes de este cambio están en
`_retirado/informe-solo-estudiantil-2026-09-16/`, con sus `.skill` listos para subir.

## Estado del backend (16-sep, noche)

Hecho en el disco, **sin comitear ni desplegar**:

| # | Estado | Dónde |
|---|---|---|
| 1 | Hecho: la ficha de empresa en Zod y en el esquema del conector (que sigue rechazando lo que no conoce) | `project.ficha-informe.js`, `ESQUEMA_GUARDAR_AVANCE_INFORME` en `mcp.tools.js` |
| 2 | Hecho: «Ámbito: empresa» como primera línea, sin pedir docente; decisión, alcance y términos viajan con el método | `lineasDeEmpresa` en `project.ficha-informe.js` |
| 3 | Hecho | `NOMBRE_DE_TIPO` |
| 4 | Hecho: `portadaDeEmpresa`, con la marca de confidencial solo si se pidió | `project.docx.js`, `datosDePortadaInforme` |
| 5 | Hecho: «Resumen ejecutivo» en el Word y en el panorama | `seccionesAparteDe` en `project.service.js` |
| 6 | Hecho: encabezado, `material_del_curso`, `formato_de_la_universidad` (título, descripción y respuestas según el ámbito), y en el panorama las líneas de material («Material del encargo»), formato («Formato de la empresa») y norma (en empresa no se pregunta); los consejos de norma y formato | `mcp.tools.js`, `project.material.js`, `project.service.js` (`esInformeDeEmpresa`), `project.consejos.js` |
| 7 | Hecho: con ámbito empresa, la portada de la plantilla reconoce «Empresa/Cliente», «Preparado para/Dirigido a», «Preparado por/Elaborado por/Responsable», «Cargo» y «Periodo», y el Word los rellena con la ficha (sin «Preparado por», firma quien tiene la cuenta). En curso esas etiquetas no se buscan | `project.portada-auto.js`, `CAMPO_DE_MARCA` en `project.plantilla-partes.js`, `project.docx.js`, `guardarPlantilla` |
| 8 | Hecho (web): el panel enseña empresa, a quién va, quién lo prepara, periodo y la marca de confidencial; las páginas de subir material y formato cambian sus textos con el `ambito` que ahora devuelven `GET /proyectos/material/:token` y `/formato/:token` | `mi-tesis.html`, `subir-material`, `subir-formato`, `proyecto.routes.js` |

El ámbito tiene que estar guardado **antes** de subir la plantilla: la Fase 0 lo guarda en el
Paso 1 y pide la plantilla en el 12. Una plantilla subida antes de elegir empresa se lee como de
curso; basta volver a subirla.

Pruebas:
- **Instantáneas nuevas del informe de curso**, generadas ANTES del cambio: `proyecto.INFORME_ESTUDIANTIL.json` y `word.informe-curso.txt`. Siguen idénticas después de los puntos 1 a 8.
- `tests/informe.empresa.test.js`: 26 pruebas (17 de los puntos 1-5, 9 de los 6-7). Rompiendo a propósito la detección del ámbito caían 7 de las 17 primeras.
- `npm test` completo tras los puntos 6-8: 1097, 1092 pasan, 2 omitidas y **3 fallan: las instantáneas `conector.*` de tesis y artículo**, por el cambio en curso de otra sesión («dáselo como enlace que se pulsa»), no por este trabajo.
- Web: `ng build` sin errores.

Al comitear, **ojo con `mcp.tools.js`**: tiene en el disco cambios de otra sesión (la herramienta
`humanizar_mi_documento`) mezclados con estos. Hay que comitear solo los trozos de esta tarea
(el esquema de la ficha, el encabezado «Ruta del informe» y la descripción de
`material_del_curso`). No se añadió el informe a la instantánea del conector por lo mismo: habría
congelado la herramienta a medias de la otra sesión.
