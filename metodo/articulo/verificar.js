'use strict';

/**
 * Verifica las skills de la Ruta del Artículo y arma los .skill en
 * `listas-para-subir/`. Es el de `skills/tesis/verificar.js`, adaptado a artículo.
 *
 *   node skills/articulo/verificar.js                          todas
 *   node skills/articulo/verificar.js articulo-fase6-discusion
 *
 * Qué hace:
 *   1. Copia `_comun/anti_ia.md` a las skills que la nombran.
 *   2. Parte cada SKILL.md como lo parte el servidor (copia de `partir()` de
 *      backend/src/modules/skills/skill.delivery.js) y comprueba tramos y bloques
 *      de código.
 *   3. Busca restos del flujo viejo (.docx, V1–V8, citas a mano…) y herramientas
 *      que el conector no tiene.
 *   4. Arma el .skill y lo pasa por `skillBundle.analizar`, el mismo validador que
 *      usa /admin.
 *
 * FALLO = rompe la entrega del servidor. REVISAR = posible resto del flujo viejo;
 * cada línea hay que mirarla, porque algunas son legítimas (V1 como «variable 1»).
 */

const fs = require('node:fs');
const path = require('node:path');
const { createRequire } = require('node:module');

const RAIZ = __dirname;
const BACKEND = path.join(RAIZ, '..', '..', 'backend');
const req = createRequire(path.join(BACKEND, 'package.json'));
const AdmZip = req('adm-zip');

// El validador lee la configuración del backend, relativa a su carpeta.
const cwd = process.cwd();
process.chdir(BACKEND);
const skillBundle = req('./src/modules/skills/skill.bundle.js');
process.chdir(cwd);

/** Pasos que tiene hoy cada skill (30-sep). Cambiarlos hace saltar de tramo a quien está a mitad. */
const PASOS_ESPERADOS = {
  'articulo-fase0-tema-y-orientacion': 9,
  'articulo-fase1-matriz-de-estrategia': 11,
  'articulo-fase2-introduccion': 10,
  'articulo-fase3-revision-literatura': 10,
  'articulo-fase3b-mapeo-bibliometrico': 13,
  'articulo-fase4-metodos': 9,
  'articulo-fase5-resultados': 9,
  'articulo-fase6-discusion': 9,
  'articulo-fase7-conclusiones-abstract': 11,
  'articulo-fase8-adaptacion-y-envio': 10,
  'articulo-fase9-respuesta-revisores': 9,
};

/** Las herramientas del conector (backend/src/modules/mcp/mcp.tools.js). */
const HERRAMIENTAS = new Set([
  'listar_capitulos', 'estado_licencia', 'mi_proyecto', 'ver_capitulo', 'guardar_avance',
  'guardar_capitulo', 'continuar', 'guardar_analisis', 'ver_analisis', 'revisar_evidencia',
  'revisar_el_articulo', 'redactar', 'buscar_fuentes', 'buscar_en_la_literatura',
  'ampliar_desde_mis_fuentes', 'anadir_a_mis_fuentes', 'mis_fuentes', 'trabajar_en_r',
  'ver_mi_documento', 'citar_mi_documento', 'humanizar_mi_documento', 'subir_mi_documento',
  'formato_de_la_universidad',
  'enlace_del_word',
  'analisis_cualitativo',
  'reescribir_parrafos', 'ver_lo_marcado',
]);
/** Herramientas de claude.ai, no del conector, que las skills sí pueden nombrar. */
const DE_CLAUDE = new Set(['ask_user_input_v0', 'web_search', 'web_fetch', 'multi_select', 'single_select']);
/** Nombres con guion bajo que no son herramientas: campos de esquema. */
const CAMPOS = new Set(['estiloCitas', 'idiomaCitas', 'temaOriginal']);
/**
 * Archivos que se nombran y no van en el bundle: los scripts de la skill pública
 * `docx` de claude.ai (/mnt/skills/public/docx) y lo que la fase 9 genera al trabajar.
 */
const EXTERNOS = new Set(['manuscrito.md', 'merge_runs.py', 'validate.py', 'accept_changes.py', 'soffice.py']);

/** [etiqueta, regex, skills donde es legítimo] */
const RESTOS = [
  // Las fases 0, 1 y 9 siguen entregando su ficha, su matriz o el Word con cambios
  // (pendiente heredado del 14-sep, ver skills/LEEME.md).
  ['archivo-docx', /\.docx\b|docx-js|present_files|\/mnt\/user-data|\bDXA\b/i, [
    'articulo-fase0-tema-y-orientacion', 'articulo-fase1-matriz-de-estrategia', 'articulo-fase9-respuesta-revisores',
  ]],
  ['version-documento', /\b(el|del|al|un|tu|su|nuevo|recibe el|entrega el|devuelve el)\s+V[1-9]\b|\bV[1-9]\s*(→|->)\s*V[1-9]\b|versi[oó]n(es)?\s+V[1-9]|V1\s*(a|–|-)\s*V8/i, []],
  ['pide-subir', /s[uú]be(lo|los|me|las)\b|re-?upload|vuelve a subir|subirlo de nuevo/i, ['articulo-fase9-respuesta-revisores']],
  ['cita-a-mano', /\((Apellido|\[Autor\]|Autor)\b[^)]{0,25}(año|\d{4})[^)]*\)/, []],
  ['verificar-fuente', /VERIFICAR EN FUENTE ORIGINAL/, []],
  ['pendiente', /\[PENDIENTE/, []],
  ['convertir-a-mano', /renumer|convierto (las|este|tu)|convertir (las citas|el cap|a Vancouver|a IEEE)|heredar el estilo/i, []],
  ['ok-generar', /OK PARA GENERAR/, []],
  ['referencias-a-mano', /(sección|lista) de Referencias (APA|actualizada)|Cierra con (la sección de )?Referencias|agrega(r)? (la entrada )?a (la lista de )?Referencias/i, []],
];

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
  if (primero === -1) return { secciones, tramos: secciones, enMedio: [] };
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
fs.mkdirSync(path.join(RAIZ, 'listas-para-subir'), { recursive: true });

let fallosTotales = 0;

for (const carpeta of carpetas) {
  const base = path.join(RAIZ, 'fuente', carpeta);
  const [nombreSkill] = fs.readdirSync(base);
  if (filtro.size && !filtro.has(nombreSkill)) continue;
  const dir = path.join(base, nombreSkill);
  const skillPath = path.join(dir, 'SKILL.md');
  const fallos = [];
  const revisar = [];

  // 1. Pieza común.
  const refs = path.join(dir, 'references');
  const comunAntiIa = path.join(RAIZ, '_comun', 'anti_ia.md');
  if (/anti_ia\.md/.test(fs.readFileSync(skillPath, 'utf8'))) {
    fs.mkdirSync(refs, { recursive: true });
    fs.copyFileSync(comunAntiIa, path.join(refs, 'anti_ia.md'));
  }
  const md = fs.readFileSync(skillPath, 'utf8');

  // 2. Cabecera.
  const cabecera = skillBundle.leerFrontmatter(md);
  if (cabecera.name !== nombreSkill) fallos.push(`name «${cabecera.name}» no coincide con la carpeta`);
  if ((cabecera.description || '').length > 1024) fallos.push(`description de ${cabecera.description.length} caracteres (máx. 1024)`);

  // 3. Troceo del servidor.
  const { secciones, tramos, enMedio } = partir(md);
  const pasos = (md.match(/^##[ \t]+Paso\b/gim) || []).length;
  if (PASOS_ESPERADOS[nombreSkill] !== undefined && pasos !== PASOS_ESPERADOS[nombreSkill]) {
    fallos.push(`tiene ${pasos} pasos y hoy tiene ${PASOS_ESPERADOS[nombreSkill]}: quien esté a mitad saltaría de tramo`);
  }
  if (enMedio.length) fallos.push(`secciones «## » entre pasos que el servidor entrega como tramos sueltos: ${JSON.stringify(enMedio)}`);
  for (const s of secciones) {
    if (fencesAbiertos(s.cuerpo.join('\n'))) fallos.push(`bloque de código partido por un «## » en la sección «${s.titulo.slice(0, 50)}»`);
  }

  // 4. Materiales nombrados y presentes.
  const presentes = new Set(archivos(dir).map((f) => path.basename(f)));
  const nombrados = (md.match(/(?<![\w.-])(?:[a-z]+\/)?[a-z0-9_-]+\.(md|py)\b/g) || []).map((n) => n.split('/').pop());
  for (const nombrado of new Set(nombrados)) {
    if (nombrado === 'SKILL.md' || EXTERNOS.has(nombrado)) continue;
    if (!presentes.has(nombrado)) fallos.push(`nombra «${nombrado}» y no está en el bundle`);
  }

  // 5. Herramientas y restos, en SKILL.md y references.
  const textos = archivos(dir).filter((f) => f.endsWith('.md'));
  const desconocidas = new Set();
  for (const f of textos) {
    const rel = path.relative(dir, f).replace(/\\/g, '/');
    const lineas = fs.readFileSync(f, 'utf8').split('\n');
    lineas.forEach((linea, i) => {
      for (const [, nombre] of linea.matchAll(/`([a-z][a-z0-9]*(?:_[a-z0-9]+)+)`/g)) {
        if (/^[a-z]+(_[a-z]+)+$/.test(nombre) && !HERRAMIENTAS.has(nombre) && !DE_CLAUDE.has(nombre)) {
          if (/^(buscar|ver|guardar|revisar|listar|mis|anadir|ampliar|citar|enlace|trabajar|estado|mi|formato)_/.test(nombre)) desconocidas.add(`${rel}:${i + 1} ${nombre}`);
        }
      }
      for (const [etiqueta, re, permitido] of RESTOS) {
        if (permitido.includes(nombreSkill)) continue;
        if (re.test(linea)) revisar.push(`${etiqueta.padEnd(19)} ${rel}:${i + 1}  ${linea.trim().slice(0, 140)}`);
      }
    });
  }
  for (const d of desconocidas) fallos.push(`herramienta que el conector no tiene: ${d}`);

  // 6. Armar y validar.
  const zip = new AdmZip();
  for (const f of archivos(dir)) {
    const rel = path.relative(base, f).replace(/\\/g, '/');
    zip.addFile(rel, fs.readFileSync(f));
  }
  const buffer = zip.toBuffer();
  const destino = path.join(RAIZ, 'listas-para-subir', `${carpeta}.skill`);
  try {
    process.chdir(BACKEND);
    const r = skillBundle.analizar(buffer);
    process.chdir(cwd);
    if (r.code !== nombreSkill) fallos.push(`el validador lo reconoce como «${r.code}»`);
    fs.writeFileSync(destino, buffer);
  } catch (error) {
    process.chdir(cwd);
    fallos.push(`el validador del servidor lo rechaza: ${error.message}`);
  }

  fallosTotales += fallos.length;
  console.log(`\n${fallos.length ? '✗' : '✓'} ${nombreSkill}  pasos=${pasos} tramos=${tramos.length}  revisar=${revisar.length}`);
  for (const f of fallos) console.log(`   FALLO    ${f}`);
  for (const r of revisar) console.log(`   REVISAR  ${r}`);
}

console.log(`\n${fallosTotales ? `${fallosTotales} fallos` : 'Sin fallos de sincronía.'}`);
process.exitCode = fallosTotales ? 1 : 0;
