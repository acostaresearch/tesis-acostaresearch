// Plantilla verificada para artículos científicos (docx-js v9).
// Uso: cd /home/claude && npm install docx && node build.js
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, HeadingLevel, convertMillimetersToTwip,
} = require("docx");
const fs = require("fs");

// ---------- texto y párrafos ----------
const t = (text, o = {}) =>
  new TextRun({ text, bold: !!o.bold, italics: !!o.italics, superScript: !!o.sup,
                size: o.size || 24, font: "Times New Roman", color: "000000" });

// Párrafo de cuerpo: justificado, interlineado 1.5, sangría de primera línea.
// runs puede ser un string o un arreglo de TextRun (para cursivas internas).
const body = (runs, o = {}) => new Paragraph({
  alignment: AlignmentType.JUSTIFIED,
  spacing: { line: 360, after: 120 },
  indent: { firstLine: o.sangria === false ? 0 : 720 },
  children: typeof runs === "string" ? [t(runs)] : runs,
});

const h1 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1, spacing: { before: 240, after: 120 },
  children: [t(text, { bold: true })],
});

const h2 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 120 },
  children: [t(text, { bold: true, italics: true })],
});

// Referencia con sangría francesa. parts = [{text, italic?}, ...]
const ref = (parts) => new Paragraph({
  spacing: { line: 360, after: 120 },
  indent: { left: 720, hanging: 720 },
  children: parts.map((p) => t(p.text, { italics: !!p.italic })),
});

// ---------- tabla APA 7 (solo reglas horizontales) ----------
const NB = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const RULE = { style: BorderStyle.SINGLE, size: 4, color: "000000" };

function apaCell(text, w, o = {}) {
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    borders: { top: o.top ? RULE : NB, bottom: o.bottom ? RULE : NB, left: NB, right: NB },
    margins: { top: 50, bottom: 50, left: 90, right: 90 },
    children: [new Paragraph({
      alignment: o.center ? AlignmentType.CENTER : AlignmentType.LEFT,
      spacing: { after: 0, line: 300 },
      children: [t(text, { bold: !!o.bold })],
    })],
  });
}

// rows[0] es el encabezado. centerCols = índices de columnas numéricas.
function apaTable(rows, widths, centerCols) {
  if (!centerCols) centerCols = rows[0].map((_, i) => i).filter((i) => i > 0);
  const last = rows.length - 1;
  return new Table({
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: widths,
    borders: { top: NB, bottom: NB, left: NB, right: NB, insideHorizontal: NB, insideVertical: NB },
    rows: rows.map((r, ri) => new TableRow({
      children: r.map((c, ci) => apaCell(c, widths[ci], {
        bold: ri === 0, top: ri === 0, bottom: ri === 0 || ri === last,
        center: centerCols.indexOf(ci) >= 0,
      })),
    })),
  });
}

const tnum = (n) => new Paragraph({ spacing: { before: 200 }, children: [t("Tabla " + n, { bold: true })] });
const tcap = (s) => new Paragraph({ spacing: { after: 80 }, children: [t(s, { italics: true })] });
const tnota = (s) => new Paragraph({
  spacing: { before: 80, after: 200 },
  children: [t("Nota. ", { italics: true, size: 22 }), t(s, { size: 22 })],
});

// ---------- documento ----------
const doc = new Document({
  // Sin esto, Word pinta los encabezados de azul y en Calibri Light.
  styles: {
    default: {
      document: { run: { font: "Times New Roman", size: 24, color: "000000" } },
      heading1: { run: { font: "Times New Roman", size: 24, bold: true, color: "000000" } },
      heading2: { run: { font: "Times New Roman", size: 24, bold: true, italics: true, color: "000000" } },
    },
  },
  sections: [{
    properties: {
      page: {
        size: { width: convertMillimetersToTwip(210), height: convertMillimetersToTwip(297) },
        margin: {
          top: convertMillimetersToTwip(25.4), bottom: convertMillimetersToTwip(25.4),
          left: convertMillimetersToTwip(25.4), right: convertMillimetersToTwip(25.4),
        },
      },
    },
    children: [
      h1("Metodología"),
      h2("Participantes"),
      body("Participaron 120 estudiantes de una universidad pública peruana. La Tabla 1 presenta sus características."),
      tnum(1),
      tcap("Características sociodemográficas de los participantes"),
      apaTable(
        [["Variable", "f", "%"], ["Femenino", "66", "56.4"], ["Masculino", "51", "43.6"]],
        [4600, 1400, 1400]
      ),
      tnota("n = 117. Tres casos sin dato en la variable sexo; los porcentajes son sobre casos válidos."),
      h1("Referencias"),
      ref([
        { text: "Hair, Joseph F., Jeffrey J. Risher, y Marko Sarstedt. 2019. “When to Use and How to Report the Results of PLS-SEM.” " },
        { text: "European Business Review", italic: true },
        { text: " 31 (1): 2–24. https://doi.org/10.1108/EBR-11-2018-0203." },
      ]),
    ],
  }],
});

Packer.toBuffer(doc).then((b) => {
  fs.writeFileSync("salida.docx", b);
  console.log("ok: salida.docx");
});
