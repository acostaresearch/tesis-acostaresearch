"""Arma la tesis de Silvia Taype desde silvia_texto.txt, con las citas como campos CITATION de Word
y la bibliografía como campo BIBLIOGRAPHY (sistema de citas de Word que pide el asesor)."""
import copy, re, sys, uuid
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn
from xml.sax.saxutils import escape

ENT, TXT, SAL = sys.argv[1:4]
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
LCID = "3082"

# ---------------------------------------------------------------- fuentes
def P(*nombres):  # "Apellidos|Nombres"
    out = []
    for n in nombres:
        last, first = n.split("|")
        out.append(f"<b:Person><b:Last>{escape(last)}</b:Last><b:First>{escape(first)}</b:First></b:Person>")
    return "<b:Author><b:Author><b:NameList>" + "".join(out) + "</b:NameList></b:Author></b:Author>"

def C(org):
    return f"<b:Author><b:Author><b:Corporate>{escape(org)}</b:Corporate></b:Author></b:Author>"

def art(autor, titulo, revista, anio, vol, num, pag, doi):
    x = f"<b:SourceType>JournalArticle</b:SourceType>{autor}<b:Title>{escape(titulo)}</b:Title><b:JournalName>{escape(revista)}</b:JournalName><b:Year>{anio}</b:Year>"
    if vol: x += f"<b:Volume>{vol}</b:Volume>"
    if num: x += f"<b:Issue>{num}</b:Issue>"
    if pag: x += f"<b:Pages>{pag}</b:Pages>"
    x += f"<b:DOI>{doi}</b:DOI><b:URL>https://doi.org/{doi}</b:URL>"
    return x

def web(autor, titulo, anio, url, sitio=""):
    x = f"<b:SourceType>DocumentFromInternetSite</b:SourceType>{autor}<b:Title>{escape(titulo)}</b:Title><b:Year>{anio}</b:Year><b:URL>{escape(url)}</b:URL>"
    if sitio: x += f"<b:InternetSiteTitle>{escape(sitio)}</b:InternetSiteTitle>"
    return x

def libro(autor, titulo, anio, editorial, edicion="", url=""):
    x = f"<b:SourceType>Book</b:SourceType>{autor}<b:Title>{escape(titulo)}</b:Title><b:Year>{anio}</b:Year><b:Publisher>{escape(editorial)}</b:Publisher>"
    if edicion: x += f"<b:Edition>{edicion}</b:Edition>"
    if url: x += f"<b:URL>{escape(url)}</b:URL>"
    return x

def informe(autor, titulo, anio, editorial, url):
    return f"<b:SourceType>Report</b:SourceType>{autor}<b:Title>{escape(titulo)}</b:Title><b:Year>{anio}</b:Year><b:Publisher>{escape(editorial)}</b:Publisher><b:URL>{escape(url)}</b:URL>"

# tag: (xml, texto de la cita entre paréntesis sin paréntesis, año)
F = {
 "Agu24": (informe(P("Aguirre|Ernesto", "Gayá|Romina"), "Programas escalables para la transformación digital de las pymes con miras a la exportación", "2024", "Comisión Económica para América Latina y el Caribe", "https://hdl.handle.net/11362/68870"), "Aguirre y Gayá", "2024"),
 "AMA": (web(C("American Marketing Association"), "What is marketing?", "s.f.", "https://www.ama.org/the-definition-of-marketing-what-is-marketing/"), "American Marketing Association", "s.f."),
 "Ben25": (art(P("Benites Salas|Yolanda L.", "Vega Gonzales|Emilio Oswaldo"), "Marketing digital y posicionamiento en un centro de estudios de Lima-Perú", "Revista Espacios", "2025", "46", "5", "338-347", "10.48082/espacios-a25v46n05p30"), "Benites Salas y Vega Gonzales", "2025"),
 "Bia25": (informe(P("Bianchini|Marco", "Lasheras Sancho|Marta"), "SME digitalisation for competitiveness: The 2025 OECD D4SME survey", "2025", "OECD Publishing", "https://doi.org/10.1787/197e3077-en"), "Bianchini y Lasheras Sancho", "2025"),
 "But24": (art(P("Butkouskaya|Vera", "Llonch-Andreu|Joan", "Alarcón-del-Amo|María del Carmen"), "Market orientation, integrated marketing communications, and small and medium-sized enterprises (SMEs) performance: A comparison between developed and developing economies", "European Research on Management and Business Economics", "2024", "30", "3", "100260", "10.1016/j.iedeen.2024.100260"), "Butkouskaya et al.", "2024"),
 "Can24": (art(P("Canaza Calsina|Yilda Lisset", "Torvisco Becerra|Aldo Jeampiere", "Angulo Bustinza|Harold Delfín"), "Analysis of digital marketing and its effect on the positioning of Peruvian universities in 2023", "Suma de Negocios", "2024", "15", "33", "119-129", "10.14349/sumneg/2024.v15.n33.a5"), "Canaza Calsina et al.", "2024"),
 "Cao23": (art(P("Cao|Guangming", "Weerawardena|Jay"), "Strategic use of social media in marketing and financial performance: The B2B SME context", "Industrial Marketing Management", "2023", "111", "", "41-54", "10.1016/j.indmarman.2023.03.007"), "Cao y Weerawardena", "2023"),
 "Cha22": (libro(P("Chaffey|Dave", "Ellis-Chadwick|Fiona"), "Digital marketing: Strategy, implementation and practice", "2022", "Pearson", "8"), "Chaffey y Ellis-Chadwick", "2022"),
 "Con11": (web(C("Congreso de la República del Perú"), "Ley N.° 29733, Ley de Protección de Datos Personales", "2011", "https://www.gob.pe/institucion/congreso-de-la-republica/normas-legales/243470-29733", "Diario Oficial El Peruano"), "Congreso de la República del Perú", "2011"),
 "CMI": (web(C("Content Marketing Institute"), "What is content marketing?", "s.f.", "https://contentmarketinginstitute.com/what-is-content-marketing"), "Content Marketing Institute", "s.f."),
 "Cuz23": (art(P("Cuzme Palma|Carlos Mauricio", "Jara Jiménez|Mónica María", "Cadena Miranda|Diego Iván"), "La influencia de la publicidad en línea en el comportamiento del consumidor: estrategias, efectividad y tendencias actuales", "South Florida Journal of Development", "2023", "4", "8", "2996-3011", "10.46932/sfjdv4n8-005"), "Cuzme Palma et al.", "2023"),
 "Dia25": (art(P("Díaz Pérez|Luis Aldo", "Sánchez Ramírez|Azucena del Pilar", "Chávez Rivas|Patricia Ivonne"), "Marketing digital y posicionamiento de marca en una empresa de transporte, Chiclayo-Perú", "Revista Científica en Ciencias Sociales", "2025", "7", "", "e701108", "10.53732/rccsociales/e701108"), "Díaz Pérez et al.", "2025"),
 "GAds": (web(C("Google Ads"), "About audience segments", "s.f.", "https://support.google.com/google-ads/answer/2497941"), "Google Ads", "s.f."),
 "GBP": (web(C("Google Business Profile"), "Tips to improve your local ranking on Google", "s.f.", "https://support.google.com/business/answer/7091"), "Google Business Profile", "s.f."),
 "GSC1": (web(C("Google Search Central"), "How to get information on Google", "s.f.", "https://developers.google.com/search/docs/fundamentals/get-on-google"), "Google Search Central", "s.f.a"),
 "GSC2": (web(C("Google Search Central"), "SEO starter guide", "s.f.", "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"), "Google Search Central", "s.f.b"),
 "Gua25": (art(P("Guadalupe Rojas|Sol", "Villalba Chamorro|Andrés Abelino"), "Estrategias de marketing en el sector hotelero de la ciudad de Pilar: Innovación y competitividad en la era digital", "Ciencia Latina Revista Científica Multidisciplinar", "2025", "9", "5", "10101-10120", "10.37811/cl_rcm.v9i5.20315"), "Guadalupe Rojas y Villalba Chamorro", "2025"),
 "Gui25": (art(P("Guillen Gibaja|Gean Carlos", "Janqui Guzman|Hermogenes", "Barazorda Huaman|Jerfson Mayer"), "Estrategias de campañas publicitarias mediante Facebook Ads de la compañía Genup Coworking Cusco Perú", "Trascender", "2025", "2", "2", "35-48", "10.51343/revtrascender.v2i2.1511"), "Guillen Gibaja et al.", "2025"),
 "Her18": (libro(P("Hernández-Sampieri|Roberto", "Mendoza Torres|Christian Paulina"), "Metodología de la investigación: Las rutas cuantitativa, cualitativa y mixta", "2018", "McGraw-Hill Interamericana Editores"), "Hernández-Sampieri y Mendoza", "2018"),
 "Hur25": (art(P("Hurtado Ccorimanya|Hellen", "Laucata Huaman|Stefany Adela"), "Determinantes del éxito competitivo en micro y pequeñas empresas en Cusco, Perú: Un enfoque de modelado de ecuaciones estructurales", "Trascender", "2025", "3", "1", "83-101", "10.51343/revtrascender.v3i1.1688"), "Hurtado Ccorimanya y Laucata Huaman", "2025"),
 "Ind23": (web(C("Instituto Nacional de Defensa de la Competencia y de la Protección de la Propiedad Intelectual"), "Guía sobre fiscalización de promociones con descuentos engañosos", "2023", "https://www.gob.pe/institucion/indecopi/informes-publicaciones/4264680-guia-sobre-fiscalizacion-de-promociones-con-descuentos-enganosos"), "Indecopi", "2023"),
 "Kan17": (art(P("Kannan|P. K.", "Li|Hongshuang"), "Digital marketing: A framework, review and research agenda", "International Journal of Research in Marketing", "2017", "34", "1", "22-45", "10.1016/j.ijresmar.2016.11.006"), "Kannan y Li", "2017"),
 "Kap10": (art(P("Kaplan|Andreas M.", "Haenlein|Michael"), "Users of the world, unite! The challenges and opportunities of social media", "Business Horizons", "2010", "53", "1", "59-68", "10.1016/j.bushor.2009.09.003"), "Kaplan y Haenlein", "2010"),
 "Loz25": (art(P("Lozada Díaz|Karla Loreli", "García Yovera|Abraham José"), "Influencia del marketing digital en el posicionamiento de marca en una tienda de alta moda en la ciudad de Jaén", "Horizonte Empresarial", "2025", "12", "", "238-248", "10.26495/d15e5493"), "Lozada Díaz y García Yovera", "2025"),
 "Mat24": (art(P("Matosas-López|Luis"), "Can customer engagement in social media be used as a predictor of operating revenue in SMEs?", "Journal of Open Innovation: Technology, Market, and Complexity", "2024", "10", "4", "100380", "10.1016/j.joitmc.2024.100380"), "Matosas-López", "2024"),
 "Pre08": (web(C("Presidencia de la República del Perú"), "Decreto Legislativo N.° 1044, Ley de Represión de la Competencia Desleal", "2008", "https://www.gob.pe/institucion/indecopi/normas-legales/2274760-1044", "Diario Oficial El Peruano"), "Presidencia de la República del Perú", "2008"),
 "Pro25": (web(C("Ministerio de la Producción"), "PRODUCE impulsa la transformación digital de las MYPE: Más de 300 empresarios capacitados en marketing digital, e-commerce y pagos en línea", "2025", "https://www.gob.pe/institucion/produce/noticias/1134311-produce-impulsa-la-transformacion-digital-de-las-mype-mas-de-300-empresarios-capacitados-en-marketing-digital-e-commerce-y-pagos-en-linea"), "Ministerio de la Producción", "2025"),
 "Roj25": (art(P("Rojas Jiménez|Karla Isabel", "Míñope Cumpén|Luis Daniel", "Vásquez Rojas|María Lucía"), "Plan de marketing digital para el lanzamiento de marca \"Winti\" en Chiclayo", "Horizonte Empresarial", "2025", "12", "", "45-64", "10.26495/5srt1546"), "Rojas Jiménez et al.", "2025"),
 "Suk24": (art(P("Sukier|Harold Bernardo", "García Samper|Martha Alexandra", "Ramírez Molina|Reynier Israel", "Sandoval Karam|Michael", "Baez Palencia|Diego", "Polo Ibáñez|Nathan", "Santamaría Ruiz|Mauricio Junior"), "Analysis of strategic marketing in small and medium-sized enterprises: Case of the bakery industry in Colombia", "Procedia Computer Science", "2024", "231", "", "601-606", "10.1016/j.procs.2023.12.178"), "Sukier et al.", "2024"),
 "Tra24": (art(P("Tran|Thi Thanh Su", "Nemeth|Nora", "Sarker|Md Shamim Iqbal"), "Digital marketing in community-based enterprises: A systematic literature review and research agenda", "Journal of Open Innovation: Technology, Market, and Complexity", "2024", "10", "4", "100414", "10.1016/j.joitmc.2024.100414"), "Tran et al.", "2024"),
 "UNC24": (informe(C("United Nations Conference on Trade and Development"), "Digital economy report 2024: Shaping an environmentally sustainable and inclusive digital future", "2024", "United Nations", "https://unctad.org/publication/digital-economy-report-2024"), "UNCTAD", "2024"),
 "Val23": (art(P("Valdez-Palazuelos|Omar", "Ovalles-Toledo|Luis Vicente", "Bueno-Camacho|Fernando", "Meriño Córdoba|Víctor Hugo"), "Presencia digital en las MiPyMEs con establecimiento físico en México", "Revista Venezolana de Gerencia", "2023", "28", "102", "596-608", "10.52080/rvgluz.28.102.10"), "Valdez-Palazuelos et al.", "2023"),
 "Yup24": (art(P("Yupanqui Lima|Nancy Tupac", "Haro Zea|Karla Liliana", "Díaz Saavedra|Robin Alexander"), "Digital marketing and customer orientation as predictors of sustainability in tourism SMEs", "Innovative Marketing", "2024", "20", "1", "160-171", "10.21511/im.20(1).2024.14"), "Yupanqui Lima et al.", "2024"),
}

def sources_xml():
    s = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?><b:Sources xmlns:b="http://schemas.openxmlformats.org/officeDocument/2006/bibliography" xmlns="http://schemas.openxmlformats.org/officeDocument/2006/bibliography" SelectedStyle="\\APASixthEditionOfficeOnline.xsl" StyleName="APA" Version="6">']
    for i, (tag, (x, _, _)) in enumerate(sorted((k, v) for k, v in F.items() if k in usados), 1):  # solo las citadas: BIBLIOGRAPHY lista todo el customXml
        s.append(f"<b:Source><b:Tag>{tag}</b:Tag>{x}<b:Guid>{{{str(uuid.uuid4()).upper()}}}</b:Guid><b:LCID>{LCID}</b:LCID><b:RefOrder>{i}</b:RefOrder></b:Source>")
    s.append("</b:Sources>")
    return "".join(s)

# ---------------------------------------------------------------- documento base
d = Document(ENT)
body = d.element.body
hijos = list(body.iterchildren())
sect_final = hijos[-1]
assert sect_final.tag == qn("w:sectPr")
secciones = [el for el in hijos if el.tag == qn("w:p") and el.find(".//" + qn("w:sectPr")) is not None]
sp_vertical = copy.deepcopy(secciones[1].find(".//" + qn("w:sectPr")))     # cuerpo vertical
sp_horizontal = copy.deepcopy(secciones[2].find(".//" + qn("w:sectPr")))   # matrices apaisadas
for sp in (sp_vertical, sp_horizontal):
    for pg in sp.findall(qn("w:pgNumType")):
        pg.attrib.pop(qn("w:start"), None)
# carátula: elementos 0..16; título nuevo
TITULO = "PLAN DE MARKETING DIGITAL EN LA EMPRESA MOLLO COMPANY S.A.C., CHUMBIVILCAS – CUSCO"
ts = hijos[4].findall(".//" + qn("w:t"))
cuerpo_t = [t for t in ts if t.text and t.text.strip()]
cuerpo_t[0].text = "“" + TITULO + "”"
for t in cuerpo_t[1:]:
    t.text = ""
for el in hijos[17:-1]:
    body.remove(el)

FUENTE, TAM = "Times New Roman", Pt(12)

def nuevo_p(estilo=None):
    p = d.add_paragraph(style=estilo)
    return p

def fmt_run(r, size=None, bold=None, italic=None, hl=False):
    r.font.name = FUENTE; r._r.get_or_add_rPr().get_or_add_rFonts().set(qn("w:hAnsi"), FUENTE)
    r.font.size = size or TAM
    if bold is not None: r.bold = bold
    if italic: r.italic = True
    if hl:
        h = OxmlElement("w:highlight"); h.set(qn("w:val"), "yellow"); r._r.get_or_add_rPr().append(h)

def campo(p, instr, resultado, size=None):
    def fc(t):
        r = p.add_run(); fmt_run(r, size)
        e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), t); r._r.append(e)
    fc("begin")
    r = p.add_run(); fmt_run(r, size)
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = f" {instr} "; r._r.append(it)
    fc("separate")
    r = p.add_run(resultado); fmt_run(r, size)
    fc("end")

def cita(p, cod, size=None):
    tipo, resto = cod.split(":", 1)
    if tipo in ("cp", "np"):
        tag, pag = resto.split(":")
        tags = [tag]
    else:
        tags, pag = resto.split(","), None
    for t in tags:
        assert t in F, t
    usados.update(tags)
    instr = f"CITATION {tags[0]}"
    if pag: instr += f" \\p {pag}"
    if tipo in ("n", "np"): instr += " \\n  \\t"
    instr += f" \\l {LCID}"
    for t in tags[1:]: instr += f" \\m {t}"
    if tipo == "c":
        res = "(" + "; ".join(f"{F[t][1]}, {F[t][2]}" for t in tags) + ")"
    elif tipo == "cp":
        res = f"({F[tags[0]][1]}, {F[tags[0]][2]}, p. {pag})"
    elif tipo == "n":
        res = f"({F[tags[0]][2]})"
    else:
        res = f"({F[tags[0]][2]}, p. {pag})"
    campo(p, instr, res, size)

usados = set()
TOK = re.compile(r"(\{(?:c|n|cp|np):[^}]+\}|\*\*[^*]+\*\*|\*[^*]+\*|==[^=]+==)")

def texto(p, s, size=None, bold=None, hl=False):
    for parte in TOK.split(s):
        if not parte: continue
        if parte.startswith("{"):
            cita(p, parte[1:-1], size)
        elif parte.startswith("**"):
            r = p.add_run(parte[2:-2]); fmt_run(r, size, True, hl=hl)
        elif parte.startswith("=="):
            r = p.add_run(parte[2:-2]); fmt_run(r, size, bold, hl=True)
        elif parte.startswith("*"):
            r = p.add_run(parte[1:-1]); fmt_run(r, size, bold, True, hl=hl)
        else:
            r = p.add_run(parte); fmt_run(r, size, bold, hl=hl)

def cuerpo(s, sangria=True, hl=False):
    p = nuevo_p()
    pf = p.paragraph_format
    pf.line_spacing = 1.5; pf.space_after = Pt(0); pf.space_before = Pt(0)
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if sangria: pf.first_line_indent = Cm(1.27)
    texto(p, s, hl=hl)
    return p

def titulo(nivel, s):
    p = nuevo_p(f"Heading {nivel}")
    pf = p.paragraph_format
    pf.space_before = Pt(12 if nivel == 1 else 6); pf.space_after = Pt(6); pf.line_spacing = 1.5
    pf.keep_with_next = True
    if nivel == 1: pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
    partes = s.split("\\n")
    for i, x in enumerate(partes):
        if i: p.add_run().add_break()
        r = p.add_run(x); fmt_run(r, Pt(12), True); r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def salto():
    p = nuevo_p(); p.add_run().add_break(WD_BREAK.PAGE)

def fin_seccion(sp):
    """Cierra la sección actual con sp (la sección que termina toma ese formato)."""
    p = nuevo_p()
    p._p.get_or_add_pPr().append(copy.deepcopy(sp))

ntabla = 0
apaisado = False
def rotulo(titulo_t):
    global ntabla
    ntabla += 1
    p = nuevo_p(); pf = p.paragraph_format
    pf.space_before = Pt(12); pf.space_after = Pt(6); pf.keep_with_next = True; pf.line_spacing = 1.0
    r = p.add_run("Tabla "); fmt_run(r, None, True)
    campo(p, "SEQ Tabla \\* ARABIC", str(ntabla))
    for rr in p.runs: rr.bold = True
    br = p.add_run(); br.add_break()
    r = p.add_run(titulo_t); fmt_run(r, None, False, True)

def bordes_apa(t):
    tblPr = t._tbl.tblPr
    for old in tblPr.findall(qn("w:tblBorders")): tblPr.remove(old)
    b = parse_xml(f'<w:tblBorders xmlns:w="{W}"><w:top w:val="single" w:sz="8" w:color="000000"/><w:left w:val="nil"/><w:bottom w:val="single" w:sz="8" w:color="000000"/><w:right w:val="nil"/><w:insideH w:val="nil"/><w:insideV w:val="nil"/></w:tblBorders>')
    tblPr.append(b)
    for old in tblPr.findall(qn("w:tblW")): tblPr.remove(old)
    tblPr.append(parse_xml(f'<w:tblW xmlns:w="{W}" w:w="5000" w:type="pct"/>'))
    tblPr.append(parse_xml(f'<w:tblLook xmlns:w="{W}" w:val="0000" w:firstRow="0" w:lastRow="0" w:firstColumn="0" w:lastColumn="0" w:noHBand="1" w:noVBand="1"/>'))
    for c in t.rows[0].cells:
        tcPr = c._tc.get_or_add_tcPr()
        tcPr.append(parse_xml(f'<w:tcBorders xmlns:w="{W}"><w:bottom w:val="single" w:sz="8" w:color="000000"/></w:tcBorders>'))
    trPr = t.rows[0]._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader xmlns:w="{W}"/>'))

def tabla(filas, cuadricula=False):
    ncol = max(len(f) for f in filas)
    size = Pt(10) if ncol >= 4 else Pt(11)
    t = d.add_table(rows=len(filas), cols=ncol)
    bordes_apa(t)
    if cuadricula:
        t._tbl.tblPr.find(qn("w:tblBorders")).append(parse_xml(f'<w:insideH xmlns:w="{W}" w:val="single" w:sz="4" w:color="000000"/>'))
    for i, f in enumerate(filas):
        for j in range(ncol):
            v = f[j] if j < len(f) else ""
            c = t.cell(i, j); p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.0
            if i == 0: p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if v.strip() == "X": p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            texto(p, v, size=size, bold=True if i == 0 else None)
    # anchos según el texto de cada columna
    ancho_total = 24.6 if apaisado else 15.9
    largos = []
    for j in range(ncol):
        L = [len(re.sub(r"\{[^}]+\}", "xxxxxxxxxxxxxxxx", f[j] if j < len(f) else "")) for f in filas]
        largos.append(max(6, min(120, sum(L) / len(L) + 0.3 * max(L))))
    tot = sum(largos)
    minimos = []
    for j in range(ncol):
        pal = [len(w) for fl in filas for w in re.sub(r"\{[^}]+\}", "", fl[j] if j < len(fl) else "").split()]
        minimos.append(max(1.4, 0.2 * max(pal or [0]) + 0.4))
    anchos = [max(minimos[j], ancho_total * x / tot) for j, x in enumerate(largos)]
    k = ancho_total / sum(anchos); anchos = [a * k for a in anchos]
    grid = t._tbl.tblGrid
    for j, gc in enumerate(grid.findall(qn("w:gridCol"))):
        gc.set(qn("w:w"), str(int(anchos[j] / 2.54 * 1440)))
    for row in t.rows:
        for j, c in enumerate(row.cells):
            c.width = Cm(anchos[j])
    tl = t._tbl.tblPr
    lay = parse_xml(f'<w:tblLayout xmlns:w="{W}" w:type="fixed"/>'); tl.append(lay)
    # columnas vacías repetidas: fusionar verticalmente las celdas en blanco bajo la primera fila de datos
    return t

def nota(s):
    p = nuevo_p(); pf = p.paragraph_format; pf.space_before = Pt(4); pf.space_after = Pt(12); pf.line_spacing = 1.0
    r = p.add_run("Nota. "); fmt_run(r, Pt(10), False, True)
    texto(p, s, size=Pt(10))

def bibliografia():
    p = nuevo_p("Bibliography")
    campo(p, f"BIBLIOGRAPHY  \\l {LCID}", "Bibliografía (se actualiza con Word)")

def items_filas():
    import importlib.util
    dims = [("Presencia digital", ["Posicionamiento online", "Página web", "Perfil empresarial", "Perfil empresarial", "Posicionamiento online"]),
            ("Redes sociales", ["Frecuencia de publicaciones", "Alcance", "Interacción", "Interacción", "Alcance"]),
            ("Marketing de contenidos", ["Valor informativo", "Calidad del contenido", "Relevancia", "Valor informativo", "Relevancia"]),
            ("Publicidad digital", ["Anuncios pagados", "Segmentación", "Segmentación", "Inversión publicitaria", "Inversión publicitaria"])]
    textos = ["Cuando busco a la empresa en internet (Google, Google Maps), encuentro su información sin dificultad.",
        "La empresa tiene una página web o un perfil digital donde explica los servicios que ofrece.",
        "Los perfiles digitales de la empresa muestran datos de contacto, horario y ubicación actualizados.",
        "El nombre y el logotipo de la empresa se ven iguales en todos sus canales digitales.",
        "Cuando necesito el servicio, me resulta fácil ubicar a la empresa desde mi celular.",
        "La empresa publica en sus redes sociales con regularidad.",
        "He visto publicaciones de la empresa en Facebook, Instagram o TikTok sin haberlas buscado.",
        "La empresa responde los mensajes y comentarios que recibe en sus redes sociales.",
        "Mis consultas por redes sociales o WhatsApp reciben respuesta en un tiempo razonable.",
        "He reaccionado, comentado o compartido alguna publicación de la empresa.",
        "Las publicaciones de la empresa explican con claridad qué servicios ofrece.",
        "Las imágenes y los videos que publica la empresa son de buena calidad.",
        "Lo que publica la empresa me sirve para decidir si contrato su servicio.",
        "La empresa informa en sus canales digitales cómo solicitar el servicio y qué datos se necesitan.",
        "Lo que la empresa muestra en internet coincide con el servicio que recibo.",
        "He visto anuncios patrocinados de la empresa en redes sociales o en Google.",
        "Los anuncios de la empresa tratan de servicios que yo podría necesitar.",
        "La publicidad de la empresa llega a personas de mi zona o de mi rubro.",
        "La empresa promociona sus servicios en internet de manera constante.",
        "Alguna promoción o anuncio digital de la empresa me motivó a consultar o contratar su servicio."]
    filas, n = [], 0
    for dim, inds in dims:
        for k, ind in enumerate(inds):
            filas.append([dim if k == 0 else "", ind, f"{n+1}. {textos[n]}", "1 a 5" if n == 0 else ""])
            n += 1
    return filas

# ---------------------------------------------------------------- recorrer el texto
lineas = open(TXT, encoding="utf-8").read().split("\n")
i = 0
pend_tabla = None
while i < len(lineas):
    s = lineas[i].rstrip()
    if not s:
        i += 1; continue
    if s.startswith("[TABLA]"):
        rotulo(s[7:].strip())
        filas = []
        i += 1
        while i < len(lineas) and (lineas[i].startswith("|") or lineas[i].startswith("@@ITEMS")):
            if lineas[i].startswith("@@ITEMS"):
                filas += items_filas()
            else:
                filas.append([c.strip() for c in lineas[i].strip()[1:].split("|")])
            i += 1
        tabla(filas, cuadricula=("FODA" in s or "consistencia" in s.lower()))
        continue
    if s.startswith("[NOTA]"):
        nota(s[6:].strip())
    elif s == "[SALTO]":
        salto()
    elif s == "[HORIZONTAL]":
        fin_seccion(sp_vertical)        # lo anterior queda vertical
        apaisado = True
    elif s == "[VERTICAL]":
        fin_seccion(sp_horizontal)      # lo anterior queda apaisado
        apaisado = False
    elif s == "[BIBLIOGRAFIA]":
        bibliografia()
    elif s.startswith("[FORMULA]"):
        p = nuevo_p(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(6)
        texto(p, s[9:].strip())
    elif s.startswith("!! "):
        cuerpo(s[3:], hl=True)
    elif s.startswith("### "):
        titulo(3, s[4:])
    elif s.startswith("## "):
        titulo(2, s[3:])
    elif s.startswith("# "):
        titulo(1, s[2:])
    elif s.startswith("**"):
        cuerpo(s, sangria=False)
    else:
        cuerpo(s)
    i += 1

# el sectPr final del documento queda como estaba (vertical)
# mover sectPr final al final del body
body.remove(sect_final); body.append(sect_final)

no_usadas = set(F) - usados
print("citas usadas:", len(usados), "· sin citar:", sorted(no_usadas))
print("tablas:", ntabla)

# fuentes en customXml
for rel in d.part.package.parts:
    if str(rel.partname).startswith("/customXml/item") and b"b:Sources" in rel.blob[:400]:
        rel._blob = sources_xml().encode("utf-8")
        print("fuentes en", rel.partname)
d.save(SAL)
print("guardado", SAL)
