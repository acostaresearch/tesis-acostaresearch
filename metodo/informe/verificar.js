'use strict';

/**
 * Verifica las skills de la Ruta del Informe (ámbitos curso y empresa) y arma
 * los .skill.
 *
 *   node skills/informe/verificar.js                      todas
 *   node skills/informe/verificar.js informe-fase2-desarrollo
 *
 * Es el de `skills/tesis/verificar.js`, adaptado al informe:
 *   1. Copia a `references/` las piezas de `_comun/` que el SKILL.md nombra.
 *   2. Parte cada SKILL.md como el servidor (`partir()` de skill.delivery.js).
 *   3. Comprueba lo propio del informe: `name` con prefijo `informe-` y título
 *      «Fase N — …», que decide el título de la sección en el Word y que el panel
 *      la cuente como fase (`esApoyo`).
 *   4. Busca herramientas que el conector no tiene y restos del flujo viejo.
 *   5. Arma el .skill en `listas-para-subir/` y lo pasa por `skillBundle.analizar`.
 *
 * FALLO = rompe la entrega del servidor. REVISAR = hay que mirarlo a mano.
 */

const fs = require('node:fs');
const path = require('node:path');
const { createRequire } = require('node:module');

const RAIZ = __dirname;
const BACKEND = path.join(RAIZ, '..', '..', 'backend');
const req = createRequire(path.join(BACKEND, 'package.json'));
const AdmZip = req('adm-zip');

const cwd = process.cwd();
process.chdir(BACKEND);
const skillBundle = req('./src/modules/skills/skill.bundle.js');
process.chdir(cwd);

/** Las herramientas del conector del informe (backend/src/modules/mcp/mcp.tools.js). */
const HERRAMIENTAS = new Set([
  'listar_capitulos', 'estado_licencia', 'mi_proyecto', 'ver_capitulo', 'guardar_avance',
  'guardar_capitulo', 'continuar', 'guardar_analisis', 'ver_analisis', 'revisar_evidencia',
  'revisar_el_informe', 'redactar', 'buscar_fuentes', 'buscar_en_la_literatura',
  'ampliar_desde_mis_fuentes', 'anadir_a_mis_fuentes', 'mis_fuentes', 'trabajar_en_r',
  'ver_mi_documento', 'citar_mi_documento', 'formato_de_la_universidad', 'enlace_del_word',
  'material_del_curso', 'analisis_cualitativo',
]);
const DE_CLAUDE = new Set(['ask_user_input_v0', 'web_search', 'web_fetch']);

/** Claves que acepta el informe fuera del catálogo: sus secciones aparte. */
const SECCIONES_APARTE = new Set(['informe-resumen', 'informe-introduccion']);

const RESTOS = [
  ['archivo-docx', /\.docx\b|docx-js|present_files|\/mnt\/user-data|\bDXA\b/i],
  ['version-documento', /\b(el|del|al|un|tu|su|nuevo)\s+V[1-9]\b|versi[oó]n(es)?\s+V[1-9]/i],
  ['pide-subir', /s[uú]be(lo|los|me|las)\b|vuelve a subir|subirlo de nuevo/i],
  ['cita-a-mano', /\((Apellido|\[Autor\]|Autor)\b[^)]{0,25}(año|\d{4})[^)]*\)/],
  ['pendiente', /\[PENDIENTE|VERIFICAR EN FUENTE ORIGINAL/],
  ['convertir-a-mano', /renumer|heredar el estilo|convertir (las citas|a Vancouver|a IEEE)/i],
  ['ok-generar', /OK PARA GENERAR/],
  ['jerga-de-tesis', /\btesista\b|\bjurado\b|\basesor\b/i],
  // Ámbito empresa. El tercer elemento, `salvo`, exime la línea: casi todos los
  // contraejemplos van entre guillemets, en una cita de bloque o en una fila de
  // tabla, y marcarlos sería ruido en cada pasada.
  ['jerga-de-consultora', /\bsinergias?\b|\bapalancar\b|hol[ií]stic|\baccionables?\b|poner en valor|transversalizar|\bdisruptiv/i, /«|^\s*>|^\s*\|/],
  ['promesa-de-resultado', /(aumentar|incrementar|reducir|mejorar|duplicar)[aá]n?\b[^.]{0,40}\d+\s*%/i, /«|^\s*>|^\s*\||sin c[aá]lculo|se corrige/i],
  ['norma-sin-numero', /normativa (laboral )?vigente|el reglamento del sector|la ley vigente/i, /«|^\s*>|^\s*\||Mal:|nunca/i],
];

/**
 * Toda tabla o figura de ejemplo lleva su línea «Fuente» o «Nota».
 *
 * Se mira por bloque de código, no por línea: el rótulo y la nota están a varias
 * líneas de distancia. En empresa la regla es «Fuente» siempre; aquí basta con
 * una de las dos porque los ejemplos de curso usan «Nota».
 */
function tablasSinFuente(texto) {
  const sueltas = [];
  const bloques = texto.split(/^```.*$/m);
  for (let i = 1; i < bloques.length; i += 2) {
    const bloque = bloques[i];
    if (!/\*\*(Tabla|Figura) \d+\*\*/.test(bloque)) continue;
    if (/^\*(Fuente|Nota)\.\*/m.test(bloque)) continue;
    sueltas.push((bloque.match(/\*\*(Tabla|Figura) \d+\*\*/) || ['?'])[0]);
  }
  return sueltas;
}

function partir(skillMd) {
  const secciones = [];
  let actual = { titulo: 'Presentación', cuerpo: [] };
  for (const linea of skillMd.split('\n')) {
    if (linea.startsWith('## ')) {
      if (actual.cuerpo.length > 0) secciones.push(actual);
      actual = { titulo: linea.slice(3).trim(), cuerpo: [linea] };
    } else {
      actual.cuerpo.push(linea);
    }
  }
  if (actual.cuerpo.length > 0) secciones.push(actual);
  const esPaso = (s) => /^Paso\b/i.test(s.titulo);
  const primero = secciones.findIndex(esPaso);
  if (primero === -1) return { secciones, tramos: [], enMedio: [] };
  let ultimo = primero;
  for (let i = secciones.length - 1; i >= primero; i -= 1) if (esPaso(secciones[i])) { ultimo = i; break; }
  const tramos = secciones.slice(primero, ultimo + 1);
  return { secciones, tramos, enMedio: tramos.filter((s) => !esPaso(s)).map((s) => s.titulo) };
}

const fencesAbiertos = (texto) => ((texto.match(/^\s*(```|~~~)/gm) || []).length % 2) !== 0;

function archivos(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) =>
    e.isDirectory() ? archivos(path.join(dir, e.name)) : [path.join(dir, e.name)]);
}

const filtro = new Set(process.argv.slice(2));
const carpetas = fs.readdirSync(path.join(RAIZ, 'fuente')).sort();
const comunes = fs.readdirSync(path.join(RAIZ, '_comun')).filter((f) => f.endsWith('.md'));
fs.mkdirSync(path.join(RAIZ, 'listas-para-subir'), { recursive: true });

let fallosTotales = 0;
const claves = new Set();

for (const carpeta of carpetas) {
  const base = path.join(RAIZ, 'fuente', carpeta);
  const [nombreSkill] = fs.readdirSync(base);
  claves.add(nombreSkill);
  if (filtro.size && !filtro.has(nombreSkill)) continue;
  const dir = path.join(base, nombreSkill);
  const md = fs.readFileSync(path.join(dir, 'SKILL.md'), 'utf8');
  const fallos = [];
  const revisar = [];

  // 1. Piezas comunes que nombra.
  const refs = path.join(dir, 'references');
  for (const comun of comunes) {
    if (md.includes(comun)) {
      fs.mkdirSync(refs, { recursive: true });
      fs.copyFileSync(path.join(RAIZ, '_comun', comun), path.join(refs, comun));
    }
  }

  // 2. Cabecera y título.
  const cabecera = skillBundle.leerFrontmatter(md);
  if (cabecera.name !== nombreSkill) fallos.push(`name «${cabecera.name}» no coincide con la carpeta`);
  if (!String(cabecera.name).startsWith('informe-')) fallos.push('el name no empieza por «informe-»');
  if ((cabecera.description || '').length > 1024) fallos.push(`description de ${cabecera.description.length} caracteres (máx. 1024)`);
  const titulo = (md.match(/^# (.+)$/m) || [])[1] || '';
  if (!/^Fase \d+ — \S/.test(titulo)) fallos.push(`el título «${titulo}» no empieza por «Fase N — »`);

  // 3. Troceo del servidor.
  const { secciones, tramos, enMedio } = partir(md);
  const pasos = (md.match(/^##[ \t]+Paso\b/gim) || []).length;
  if (pasos === 0) fallos.push('no tiene ningún «## Paso»');
  if (enMedio.length) fallos.push(`secciones «## » entre pasos: ${JSON.stringify(enMedio)}`);
  for (const s of secciones) {
    if (fencesAbiertos(s.cuerpo.join('\n'))) fallos.push(`bloque de código partido en «${s.titulo.slice(0, 50)}»`);
  }

  // 4. Materiales nombrados y presentes.
  const presentes = new Set(archivos(dir).map((f) => path.basename(f)));
  const nombrados = (md.match(/(?<![\w.-])(?:[a-z]+\/)?[a-z0-9_-]+\.(md|py)\b/g) || []).map((n) => n.split('/').pop());
  for (const nombrado of new Set(nombrados)) {
    if (nombrado !== 'SKILL.md' && !presentes.has(nombrado)) fallos.push(`nombra «${nombrado}» y no está en el bundle`);
  }

  // 5. Herramientas, claves de capítulo y restos.
  for (const f of archivos(dir).filter((x) => x.endsWith('.md'))) {
    const rel = path.relative(dir, f).replace(/\\/g, '/');
    const texto = fs.readFileSync(f, 'utf8');
    for (const suelta of tablasSinFuente(texto)) {
      revisar.push(`tabla-sin-fuente    ${rel}  ${suelta} sin línea «Fuente» ni «Nota»`);
    }
    texto.split('\n').forEach((linea, i) => {
      for (const [, nombre] of linea.matchAll(/`([a-z][a-z0-9]*(?:_[a-z0-9]+)+)`/g)) {
        if (/^[a-z]+(_[a-z]+)+$/.test(nombre) && !HERRAMIENTAS.has(nombre) && !DE_CLAUDE.has(nombre)
          && /^(buscar|ver|guardar|revisar|listar|mis|anadir|ampliar|citar|enlace|trabajar|estado|mi|formato)_/.test(nombre)) {
          fallos.push(`herramienta que el conector no tiene: ${rel}:${i + 1} ${nombre}`);
        }
      }
      for (const [clave] of linea.matchAll(/\binforme-[a-z0-9-]+\b/g)) {
        if (!SECCIONES_APARTE.has(clave) && !/^informe-fase\d/.test(clave)) {
          revisar.push(`clave-desconocida   ${rel}:${i + 1}  ${clave}`);
        }
      }
      for (const [etiqueta, re, salvo] of RESTOS) {
        if (re.test(linea) && !(salvo && salvo.test(linea))) revisar.push(`${etiqueta.padEnd(19)} ${rel}:${i + 1}  ${linea.trim().slice(0, 140)}`);
      }
    });
  }

  // 6. Armar y validar.
  const zip = new AdmZip();
  for (const f of archivos(dir)) zip.addFile(path.relative(base, f).replace(/\\/g, '/'), fs.readFileSync(f));
  const buffer = zip.toBuffer();
  let sugerido = '';
  try {
    process.chdir(BACKEND);
    const r = skillBundle.analizar(buffer);
    process.chdir(cwd);
    sugerido = r.displayNameSugerido;
    if (r.code !== nombreSkill) fallos.push(`el validador lo reconoce como «${r.code}»`);
    fs.writeFileSync(path.join(RAIZ, 'listas-para-subir', `${carpeta}.skill`), buffer);
  } catch (error) {
    process.chdir(cwd);
    fallos.push(`el validador del servidor lo rechaza: ${error.message}`);
  }

  fallosTotales += fallos.length;
  console.log(`\n${fallos.length ? '✗' : '✓'} ${nombreSkill}  «${sugerido}»  pasos=${pasos} tramos=${tramos.length}  revisar=${revisar.length}`);
  for (const f of fallos) console.log(`   FALLO    ${f}`);
  for (const r of revisar) console.log(`   REVISAR  ${r}`);
}

// Las claves de capítulo que nombran las skills tienen que existir.
for (const carpeta of carpetas) {
  const base = path.join(RAIZ, 'fuente', carpeta);
  const [nombreSkill] = fs.readdirSync(base);
  const md = fs.readFileSync(path.join(base, nombreSkill, 'SKILL.md'), 'utf8');
  for (const [clave] of md.matchAll(/\binforme-fase\d[a-z0-9-]*\b/g)) {
    if (!claves.has(clave)) {
      fallosTotales += 1;
      console.log(`   FALLO    ${nombreSkill} nombra la clave «${clave}», que no es ninguna skill`);
    }
  }
}

console.log(`\n${fallosTotales ? `${fallosTotales} fallos` : 'Sin fallos de sincronía.'}`);
process.exitCode = fallosTotales ? 1 : 0;
