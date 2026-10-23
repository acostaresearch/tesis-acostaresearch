"""Pone a la carpeta de un trabajo el nombre de la persona dueña del documento.

    python nombrar.py 10-cambiarnombre            renombra si la carpeta se llama «cambiarnombre»
    python nombrar.py 10-cambiarnombre --ver      solo dice qué nombre le pondría
    python nombrar.py 04-tesis --forzar           renombra aunque ya tenga otro nombre

El nombre nuevo es el nombre completo de la persona, «NN-Nombres Apellidos», en las dos raíces
(se conserva el número con que empieza la carpeta). tesis-asesorar va numerada desde el 17-oct-2026:
si la carpeta no tiene número se le da el siguiente libre, y se añade el WhatsApp del cliente si
cotizacion.md lo trae: «NN-Nombres Apellidos - 929365434» (sin el +51 de Perú; con su código si es de
otro país). Una carpeta de tesis-asesorar a la que le falta el número de orden o el WhatsApp se renombra
sin --forzar. El autor se lee de la carátula del Word (AUTOR,
Autora:, Tesista, Investigadores, Presentado por…) y, si no hay carátula, de las
propiedades del archivo. Si no lo encuentra, no renombra y lo dice. El registro de
trabajos queda así por persona, no por «tesis» o «artículo».
"""
import glob
import io
import os
import re
import sys
import unicodedata

from docx import Document

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rutas import ASESORAR, TURNITIN  # noqa: E402
RAICES = [str(TURNITIN), str(ASESORAR)]
ROTULO = re.compile(r'^(?:\d+(?:\.\d+)*\.?\s*)?(autor(a|es|\(es\)|\(a\))?|tesista(s)?|investigador(a|es)?|bachiller(es)?|'
                    r'estudiante(s)?|presentad[oa] por|elaborad[oa] por|realizad[oa] por|alumn[oa](s)?)\s*[:.]?\s*(.*)$', re.I)
TITULOS = re.compile(r'^(br|bach|lic|mg|mgtr|dr|dra|ing|abog|prof|sr|sra|srta|mtro|mtra|est|ms|msc|phd)\.?\s+', re.I)
NO_NOMBRE = re.compile(r'orcid|@|http|universidad|escuela|facultad|programa|asesor|docente|jurado|'
                       r'c[oó]digo|dni|tel[eé]fono|correo|l[ií]nea|segunda especialidad|\d{4}', re.I)
NO_AUTOR_META = {'', 'usuario', 'user', 'hp', 'un-named', 'unnamed', 'windows', 'admin', 'pc', 'lenovo',
                 'a&e', 'microsoft', 'office', 'personal', 'equipo', 'home'}


def llano(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


def limpiar(t):
    t = re.sub(r'\(.*?\)', '', t)          # (orcid…)
    t = re.sub(r'https?://\S+', '', t)
    t = TITULOS.sub('', t.strip())
    t = re.sub(r'\s+', ' ', t).strip(' .:;,-')
    return t


GENERICAS = {'apellidos', 'nombres', 'apellido', 'nombre', 'tipo', 'investigacion', 'autor', 'autora',
             'titulo', 'tesista', 'estudiante', 'bachiller', 'carpeta', 'cliente', 'grado', 'maestria'}


def es_nombre(t):
    t = limpiar(t)
    toks = [x for x in re.split(r'[\s,]+', t) if x]
    if not (2 <= len(toks) <= 8) or NO_AUTOR_META.intersection({t.lower()}) or NO_NOMBRE.search(t):
        return False
    if any(llano(x) in GENERICAS for x in toks):
        return False
    return all(re.match(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ'’-]+$", x) for x in toks) and any(x[0].isupper() for x in toks)


NOMBRES_PILA = set("""maria mary marya mari marita jose josue juan luis carlos jorge pedro pablo miguel angel manuel
francisco diego daniel david roy samuel josue analiz karen katy katia kathy paula diana luna ana rosa
carmen elena elisa elisai irwin julio renzo maritza dayra teresa sandra patricia claudia andrea andres
cesar ricardo roberto raul victor hugo oscar fernando alberto alejandro alex alexander gabriel rafael
sergio edgar edwin erick eric kevin jhon john jean brian bryan jesus mario marco marcos martin mateo
lucia luciana sofia valeria vanessa veronica yesica jessica jesica yessenia yolanda zoila milagros
rocio rosario pilar esther estefany estefania fiorella flor gloria grace isabel ivonne janet jazmin
jenny karina katherine liliana lizbeth lorena lourdes lucero luz magaly margarita marisol melissa
mercedes miriam mirian mónica monica nancy natalia nelly noemi olga rosmery ruth silvia susana
tatiana vilma yanet yesenia alicia angela beatriz blanca brenda camila cecilia cinthia cintia cristina
daniela delia dora edith elizabeth emily erika eva fabiola fanny gabriela gisela giuliana guadalupe
ines irma jackeline jimena johana jhoana julia juliana leslie lesly leticia lidia lisbeth lorena lucy
magda maribel marina mariela marilyn marleny martha marta mayra mia micaela milagritos nicole noelia
olinda paola pamela pierina raquel rebeca reyna rosa rossana roxana sara sarita shirley sonia stefany
tania thalia ursula wendy ximena yadira yanina yuli zully abel adrian aldo alonso amador anderson
antonio armando arturo augusto benicio benjamin bruno christian cristian cristhian dante dario
denis dennis eduardo efrain elmer emilio enrique ernesto esteban eugenio fabian felipe felix fidel
franco frank freddy gerardo german gilberto gonzalo guillermo gustavo henry hernan hector ignacio
isaac ivan jaime javier jefferson jeferson jhonatan jonathan joel jorge jose josé juan julian julio
leonardo lenin lino lorenzo luis marcelo mauricio max maximo moises nelson nestor nicolas omar
orlando pablo paolo patricio percy rafael ramiro raymundo renato rene ricardo richard rodrigo rolando
ronald ruben santiago saul sebastian segundo simon teodoro tomas ulises valentin walter wilfredo
william wilmer wilson yan yonatan""".split())


def completo(t):
    """«Pazos Llenque, Katy Manuelita» → Katy Manuelita Pazos Llenque · «Br. Roy Carbajal» → Roy Carbajal."""
    t = limpiar(t)
    if ',' in t and not re.search(r'[yY]', t):
        a, b = [x.strip() for x in t.split(',', 1)]
        ap, no = a.split(), b.split()
        if not (ap and no):
            return t
        # lo normal en carátula es «Apellidos, Nombres»; pero «Mary Carmen, Ramírez Casternoque»
        # va al revés y se reconoce porque lo de antes de la coma es un nombre de pila
        if llano(ap[0]) in NOMBRES_PILA and llano(no[0]) not in NOMBRES_PILA:
            ap, no = no, ap
        return ' '.join(no + ap)
    return t


def cap(t):
    out = []
    for x in t.split():
        if x.lower() in ('y', 'e', 'de', 'del', 'la', 'las', 'los'):
            out.append(x.lower())
        else:
            out.append(x if x[:1].isupper() and not x.isupper() else x.capitalize())
    return ' '.join(out)


def autor_de(path):
    d = Document(path)
    ps = [p.text.strip() for p in d.paragraphs[:120] if p.text.strip()]
    for i, t in enumerate(ps[:60]):
        m = ROTULO.match(t)
        if not m:
            continue
        resto = m.group(m.lastindex).strip()
        cand = [resto] if resto else ps[i + 1:i + 4]
        for c in cand:
            if es_nombre(c):
                return cap(completo(c)), c, 'carátula'
            if resto:
                break
    for i, t in enumerate(ps[:60]):
        if re.search(r'^(autor|tesista|investigador|bachiller|estudiante)', t, re.I) and i + 1 < len(ps) \
                and es_nombre(ps[i + 1]):
            return cap(completo(ps[i + 1])), ps[i + 1], 'carátula'
    meta = (d.core_properties.author or '').split(';')[0].strip()
    if meta.lower() not in NO_AUTOR_META and es_nombre(meta):
        # las propiedades suelen traer al dueño de la plantilla, no al autor: solo valen si algún
        # trozo del nombre aparece en el nombre de la carpeta o del archivo
        pista = llano(os.path.basename(os.path.dirname(os.path.dirname(path))) + ' ' + os.path.basename(path))
        if any(llano(x) in pista for x in meta.split() if len(x) >= 3):
            return cap(completo(meta)), meta, 'propiedades del archivo'
        print(f'  (las propiedades de {os.path.basename(path)} dicen «{meta}», pero no coincide con la carpeta: no se usa)')
    return None, None, None


def autor_de_cotizacion(carp):
    """En tesis-asesorar, la primera línea «Cliente: …» de cotizacion.md es la fuente más fiable."""
    p = os.path.join(carp, 'cotizacion.md')
    if not os.path.exists(p):
        return None, None, None
    txt = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'(?:autora?|persona) que figura en la car[aá]tula es ([^.(,\n]+)', txt, re.I)
    if m and es_nombre(m.group(1)):
        return cap(completo(m.group(1))), m.group(1).strip(), 'cotizacion.md'
    m = re.search(r'^Cliente:\s*(.+)$', txt, re.M)
    if not m:
        return None, None, None
    linea = m.group(1)
    cand = re.split(r' · | \(|,? \+\d|\. | - | – ', linea)[0].strip()
    # «Galarreta Ruiz, Elisai Mariter, +51 …» ya quedó sin el teléfono; «Analiz … y Karen …» va entero
    if es_nombre(cand):
        return cap(completo(cand)), cand, 'cotizacion.md'
    return None, None, None


def telefono_de(carp):
    """Número de WhatsApp de la línea «Cliente:» de cotizacion.md (o «Teléfono:»), sin el +51 de Perú."""
    p = os.path.join(carp, 'cotizacion.md')
    if not os.path.exists(p):
        return ''
    txt = open(p, encoding='utf-8', errors='replace').read()
    for pat in (r'^Cliente:.*?(\+?\d[\d ]{7,}\d)', r'^(?:Tel[eé]fono|WhatsApp|Celular):\s*(\+?\d[\d ]{7,}\d)'):
        m = re.search(pat, txt, re.M | re.I)
        if m:
            dig = re.sub(r'\D', '', m.group(1))
            if dig.startswith('51') and len(dig) == 11:
                dig = dig[2:]
            return dig if len(dig) >= 8 else ''
    return ''


def carpeta_de(arg):
    if os.path.isdir(arg):
        return os.path.abspath(arg)
    for r in RAICES:
        p = os.path.join(r, re.sub(r'^asesorar[\\/]', '', arg))
        if os.path.isdir(p):
            return p
    sys.exit(f'No encuentro la carpeta {arg}')


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    ver, forzar = '--ver' in sys.argv, '--forzar' in sys.argv
    carp = carpeta_de(args[0])
    nombre = os.path.basename(carp)
    m = re.match(r'^(\d+)[-_ ]*(.*)$', nombre)
    num, resto = (m.group(1), m.group(2)) if m else ('', nombre)
    print(f'CARPETA  {carp}')
    asesorar = os.path.basename(os.path.dirname(carp)) == 'tesis-asesorar'
    tel = telefono_de(carp) if asesorar else ''
    falta_tel = bool(tel) and tel not in re.sub(r'\D', '', nombre)
    falta_num = asesorar and not num
    if falta_num:  # tesis-asesorar también va numerada (17-oct-2026): el siguiente número libre
        usados = [int(x.group(1)) for x in (re.match(r'^(\d+)-', d) for d in os.listdir(os.path.dirname(carp))) if x]
        num = f'{max(usados, default=0) + 1:02d}'
    if 'cambiarnombre' not in unicodedata.normalize('NFD', resto.lower()).replace(' ', '') and not forzar \
            and not falta_tel and not falta_num:
        print('Ya tiene nombre propio; no se renombra (usa --forzar para cambiarlo).')
        return
    words = []
    for sub in ('actual', '01-original', '03-turnitin', '', 'Listo', '02-corregida'):
        words += sorted(glob.glob(os.path.join(carp, sub, '*.docx')))
    words = [w for w in words if not os.path.basename(w).startswith('~$')]
    if not words and not os.path.exists(os.path.join(carp, 'cotizacion.md')):
        sys.exit('No hay ningún Word del que leer el autor.')
    hallado = None
    n, linea, de = autor_de_cotizacion(carp)
    if n:
        hallado = (n, linea, de, '')
    for w in words if not hallado else []:
        try:
            n, linea, de = autor_de(w)
        except Exception as e:  # noqa
            print(f'  no pude leer {os.path.basename(w)}: {e}')
            continue
        if n:
            hallado = (n, linea, de, w)
            break
    if not hallado:
        sys.exit('No encontré al autor en la carátula ni en las propiedades: ponle el nombre a mano.')
    n, linea, de, w = hallado
    print(f'Autor: {linea}  ({de}' + (f' de {os.path.basename(w)}' if w else '') + ')')
    nuevo = (f'{num}-' if num else '') + n + (f' - {tel}' if tel else '')
    destino = os.path.join(os.path.dirname(carp), nuevo)
    print(f'Nombre nuevo: {nuevo}')
    if ver:
        return
    if os.path.exists(destino):
        sys.exit(f'Ya existe {nuevo}; no se renombra.')
    os.rename(carp, destino)
    print(f'Renombrada: {nombre}  →  {nuevo}')


if __name__ == '__main__':
    main()
