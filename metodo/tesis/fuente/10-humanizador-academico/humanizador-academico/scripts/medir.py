#!/usr/bin/env python3
"""Mide los indicadores estilometricos que usan los detectores de IA.

Uso:
    python3 medir.py archivo.txt [otro.txt ...]
    python3 medir.py antes.txt despues.txt --claves
    cat texto.txt | python3 medir.py -

Reporta: numero de oraciones, largo medio, desviacion, minimo y maximo,
dispersion relativa, porcentaje de palabras funcionales, largo medio de
palabra, oraciones cortas (<=8 palabras), signos de interrogacion y
trigramas repetidos.

Anadido (hallazgos de la sesion Zarzosa, patrones 0d a 0g): dispersion del
largo de parrafo, aperturas con complemento antepuesto, sujetos con nombre
abstracto, oraciones enlazadas y cierres sin cita. Los indicadores anteriores
no cambian.

Anadido (3.1, claves de cita del proyecto): antes de medir se neutralizan las
claves [AR1234ABCD], [AR1234ABCD:n], [AR1234ABCD:p. 45] y [FALTA FUENTE], para
que no cuenten como palabras ni corten oraciones en "p. 45". Un parrafo que
termina en una clave cuenta como parrafo que cierra con cita ([FALTA FUENTE]
no es cita). Los bloques que no son prosa (subtitulos #, tablas |, rotulos
**Tabla N** / **Figura N**, notas *Nota.*) no entran en la medicion, pero si
en la numeracion de parrafos y en la lista de claves.

Con --claves imprime la lista de claves de cada parrafo. Con --claves y dos
archivos (antes y despues) compara las listas parrafo a parrafo: cada parrafo
tiene que salir con las mismas claves y los mismos modificadores.
"""
import re
import sys
import statistics
import unicodedata

FUNC = set("""
el la los las un una unos unas lo al del de a ante bajo cabe con contra desde
durante en entre hacia hasta mediante para por segun sin so sobre tras y e ni o
u pero sino aunque porque pues que si como cuando donde mientras aunque yo tu el
ella nosotros nosotras ustedes ellos ellas me te se nos os les le lo la los las
mi mis tu tus su sus nuestro nuestra nuestros nuestras este esta esto estos
estas ese esa eso esos esas aquel aquella aquello aquellos aquellas es son era
eran fue fueron ser sea sean hay ha han he has habia habian hemos esta estan
estaba estaban estar mas menos muy ya no si tambien tampoco solo aun todavia asi
ahi alli aqui cual cuales quien quienes cuyo cuya cuyos cuyas uno una algo alguien
todo toda todos todas cada otro otra otros otras mismo misma tan tanto cuanto
""".split())


# --- anadido 3.1: claves de cita del proyecto ---
# La misma marca que acepta el servidor.
RE_CLAVE = re.compile(r'\[(AR[0-9A-F]{8})(?::([^\]\n]{1,40}))?\]')
RE_FALTA = re.compile(r'\[FALTA FUENTE\]')
# Centinelas de uso privado: no son \w (no cuentan como palabra) y no son
# puntuacion (no cortan oraciones).
CENT_CLAVE = ''
CENT_FALTA = ''
RE_NO_PROSA = re.compile(r'^\s*(#|\||\*\*(Tabla|Figura)\s+\d|\*Nota\.\*|\[Insertar aqu)')


def neutralizar(texto):
    """Sustituye cada clave y cada [FALTA FUENTE] por un centinela pegado a la
    palabra anterior, para que no altere el conteo de palabras ni de oraciones."""
    texto = RE_CLAVE.sub(lambda m: CENT_CLAVE, texto)
    texto = RE_FALTA.sub(CENT_FALTA, texto)
    return re.sub(r'[ \t]+(?=[])', '', texto)


def bloques_de(texto):
    """Parrafos separados por linea en blanco, numerados desde 1."""
    return [p.strip() for p in re.split(r'\n\s*\n', texto) if p.strip()]


def es_prosa(bloque):
    return not RE_NO_PROSA.match(bloque)


def claves_de(bloque):
    """Lista ordenada de marcas de un parrafo: 'AR1234ABCD', 'AR1234ABCD:n',
    'AR1234ABCD:p. 45' o 'FALTA FUENTE'."""
    marcas = []
    for m in re.finditer(r'\[(AR[0-9A-F]{8})(?::([^\]\n]{1,40}))?\]|\[FALTA FUENTE\]', bloque):
        if m.group(1):
            marcas.append(m.group(1) + (':' + m.group(2) if m.group(2) else ''))
        else:
            marcas.append('FALTA FUENTE')
    return marcas


# --- anadido: lexicos para los indicadores 0d a 0g ---
RE_ANTEPUESTO = re.compile(
    r'^(De|A|En|Sobre|Dentro|Frente|Junto|Por|Con|Aun|Asi|Asií|Ese|Esa|Esos|Esas|'
    r'Donde|Si|Para|Lo mismo|El resultado|Tras|Desde|Segun|Según)\b')
RE_ABSTRACTO = re.compile(
    r'\b\w*(cion|ción|sion|sión|miento|encia|ancia|idad|eza|anza|aje)\b|'
    r'\b(retraso|peligro|demora|avance|exigencia|imprecision|imprecisión|indefinicion|'
    r'indefinición|recorrido|acceso|riesgo|marco|eficacia|barreras|norma|causal|'
    r'logica|lógica|literatura|evidencia|proceso|enfoque|impacto)\b', re.I)
RE_ENLACE = re.compile(
    r'\b(esa|ese|eso|esas|esos|esta|este|esto|dicha|dicho|misma|mismo|sin embargo|'
    r'ademas|además|en cambio|por su parte|tambien|también|tampoco|aunque|pero|'
    r'frente a|junto a|dentro de|a eso|por eso|de ahi|de ahí|con lo que|aun asi|'
    r'aun así|donde|asi|así|entonces)\b', re.I)
# Cita entre parentesis con anio, o clave del proyecto ya neutralizada.
RE_CITA = re.compile(r'\(?[^()]{0,60}(?:1[89]\d\d|20\d\d)[^()]{0,30}\)|' + CENT_CLAVE)
ABREV_CORTE = re.compile(r'(et al\.|vs\.|N\.°|art\.|arts\.|Ed\.|vol\.)\s*$')


def oraciones_de(texto):
    """Corta en oraciones reuniendo los falsos cortes por abreviatura."""
    bruto = re.split(r'(?<=[.?!])\s+(?=[A-ZÁÉÍÓÚÑ¿])', texto.strip())
    fin = []
    for s in bruto:
        if fin and ABREV_CORTE.search(fin[-1]):
            fin[-1] += ' ' + s
        else:
            fin.append(s)
    return [s.strip() for s in fin if s.strip()]


def medir_arquitectura(texto, nombre=""):
    """Indicadores 0d a 0g. No sustituye a medir(): se ejecuta despues."""
    numerados = [(i, neutralizar(b)) for i, b in enumerate(bloques_de(texto), 1) if es_prosa(b)]
    parrafos = [p for _, p in numerados]
    largos_p = [len(palabras(p)) for p in parrafos]
    tot = ant = enl = abst = agente = 0
    cierres_sin_cita = 0
    peores = []
    for idx, p in numerados:
        ss = oraciones_de(p.replace('\n', ' '))
        if not ss:
            continue
        tot += len(ss)
        sueltas = 0
        for k, s in enumerate(ss):
            cabeza = ' '.join(s.split()[:8])
            if RE_ANTEPUESTO.match(s.strip()):
                ant += 1
            if RE_ABSTRACTO.search(' '.join(s.split()[:6])):
                abst += 1
            if k > 0:
                if RE_ENLACE.search(cabeza):
                    enl += 1
                else:
                    sueltas += 1
        if not RE_CITA.search(ss[-1]):
            cierres_sin_cita += 1
        if len(ss) > 2 and sueltas / (len(ss) - 1) >= 0.6:
            peores.append(f"parrafo {idx} ({sueltas}/{len(ss)-1} sueltas)")
        racha = mayor = 0
        for s in ss:
            racha = racha + 1 if len(s.split()) >= 30 else 0
            mayor = max(mayor, racha)
        if mayor >= 3:
            peores.append(f"parrafo {idx}: {mayor} oraciones seguidas de 30+ (patron 0)")
        if len(palabras(p)) > 200:
            peores.append(f"parrafo {idx}: {len(palabras(p))} palabras (>200)")

    print(f"--- {nombre} :: arquitectura ---")
    if not tot:
        print("(sin prosa que medir)\n")
        return
    no_iniciales = max(tot - len(parrafos), 1)
    if len(largos_p) > 1:
        m = statistics.mean(largos_p)
        d = statistics.pstdev(largos_p) / m
        print(f"parrafos: {len(largos_p)} | largos: {largos_p}")
        print(f"dispersion del largo de parrafo: {d:.2f}  (ALERTA si <0.20)")
    print(f"aperturas con complemento antepuesto: {100*ant/tot:.0f}%  (ALERTA si >40%)")
    print(f"sujeto con nombre abstracto: {100*abst/tot:.0f}%  (ALERTA si >40%)")
    print(f"oraciones enlazadas: {100*enl/no_iniciales:.0f}%  (ALERTA si <30%)")
    print(f"parrafos que cierran sin cita: {cierres_sin_cita} de {len(parrafos)}  (ALERTA si >60%)"
          f"  [clave [AR...] = cita; [FALTA FUENTE] = sin cita]")
    for z in peores:
        print(f"  AVISO: {z}")
    print()


def sin_tildes(palabra):
    return ''.join(
        c for c in unicodedata.normalize('NFD', palabra.lower())
        if unicodedata.category(c) != 'Mn'
    )


def palabras(texto):
    return re.findall(r"\b[\wáéíóúüñÁÉÍÓÚÜÑ]+\b", texto)


def medir(texto, nombre=""):
    # Solo prosa, y con las claves de cita neutralizadas.
    texto = '\n\n'.join(neutralizar(b) for b in bloques_de(texto) if es_prosa(b))
    # Proteger abreviaturas frecuentes para no cortar oraciones donde no toca
    protegido = texto
    for abrev in ("et al.", "Dr.", "Dra.", "Sr.", "Sra.", "etc.", "p. ej.", "Ed.", "vol.", "núm."):
        protegido = protegido.replace(abrev, abrev.replace(".", "\x00"))
    oraciones = [s.replace("\x00", ".").strip()
                 for s in re.split(r'(?<=[.?!])\s+', protegido.strip()) if s.strip()]
    largos = [len(palabras(o)) for o in oraciones]
    todas = [sin_tildes(w) for w in palabras(texto)]
    if not todas or not largos:
        print(f"--- {nombre} --- (texto vacio)")
        return
    funcionales = sum(1 for w in todas if w in FUNC)
    trigramas = [tuple(todas[i:i + 3]) for i in range(len(todas) - 2)]
    vistos = set()
    repetidos = 0
    for g in trigramas:
        if g in vistos:
            repetidos += 1
        vistos.add(g)
    media = statistics.mean(largos)
    desv = statistics.pstdev(largos)
    cortas = sum(1 for n in largos if n <= 8)

    print(f"--- {nombre} ---")
    print(f"oraciones: {len(oraciones)} | palabras: {len(todas)}")
    print(f"largo medio de oracion: {media:.1f}  (referencia humana ~23)")
    print(f"desviacion: {desv:.1f} | dispersion relativa: {desv / media:.2f}  (meta >=0.45)")
    print(f"min-max: {min(largos)}-{max(largos)}")
    print(f"oraciones cortas (<=8 palabras): {cortas} de {len(largos)}  (meta >=15%)")
    print(f"palabras funcionales: {100 * funcionales / len(todas):.1f}%  (meta >=40%)")
    print(f"largo medio de palabra: {statistics.mean(len(w) for w in todas):.2f}  (meta <=5.3)")
    print(f"signos de interrogacion: {texto.count('?')}")
    print(f"trigramas repetidos: {repetidos}")
    racha = mayor = 0
    for n in largos:
        racha = racha + 1 if n >= 30 else 0
        mayor = max(mayor, racha)
    if mayor >= 3:
        print(f"ALERTA: {mayor} oraciones seguidas de 30 palabras o mas. "
              f"Revisar paralelismo de plantilla (patron 0).")
    print(f"largos por oracion: {largos}")
    print()


# --- anadido 3.1: control de claves por parrafo ---
def listar_claves(texto, nombre=""):
    bloques = bloques_de(texto)
    print(f"--- {nombre} :: claves por parrafo ---")
    total = 0
    for i, b in enumerate(bloques, 1):
        marcas = claves_de(b)
        total += len(marcas)
        if marcas:
            print(f"P{i}: {' | '.join(marcas)}")
    print(f"total: {total} marcas en {len(bloques)} parrafos")
    print()


def _ids(marcas):
    return [m.split(':', 1)[0] for m in marcas]


def _sin_n(marcas):
    return [m[:-2] if m.endswith(':n') else m for m in marcas]


def comparar_claves(texto_a, texto_b, nombre_a, nombre_b):
    ba, bb = bloques_de(texto_a), bloques_de(texto_b)
    print(f"--- claves: {nombre_a} -> {nombre_b} ---")
    problemas = 0
    if len(ba) != len(bb):
        print(f"AVISO: {len(ba)} parrafos antes y {len(bb)} despues. Si se partio un parrafo "
              f"con aprobacion del autor, la numeracion se corre desde ahi: comparar a mano la "
              f"suma de los dos nuevos con el original.")
    for i in range(max(len(ba), len(bb))):
        a = claves_de(ba[i]) if i < len(ba) else []
        b = claves_de(bb[i]) if i < len(bb) else []
        if not a and not b:
            continue
        if a == b:
            estado = "igual"
        elif _sin_n(a) == _sin_n(b):
            estado = "CAMBIO DE :n (comprobar que el nombre del autor entro o salio de la frase)"
            problemas += 1
        elif sorted(a) == sorted(b):
            estado = "ORDEN CAMBIADO (comprobar que cada clave sigue con su afirmacion)"
            problemas += 1
        else:
            faltan = [m for m in a if m not in b] + [m for m in a if m in b and a.count(m) > b.count(m)]
            sobran = [m for m in b if m not in a] + [m for m in b if m in a and b.count(m) > a.count(m)]
            estado = (f"DIFERENTE  faltan: {sorted(set(faltan)) or '-'}  "
                      f"sobran: {sorted(set(sobran)) or '-'}")
            problemas += 1
        print(f"P{i + 1}: antes [{' | '.join(a) or '-'}]  despues [{' | '.join(b) or '-'}]  {estado}")
    ta = [m for x in ba for m in claves_de(x)]
    tb = [m for x in bb for m in claves_de(x)]
    print(f"total: {len(ta)} -> {len(tb)} marcas"
          f"{'' if sorted(_ids(ta)) == sorted(_ids(tb)) else '  <<< NO COINCIDEN LAS CLAVES'}")
    print("resultado: " + ("sin diferencias" if not problemas else
                           f"{problemas} parrafo(s) a revisar antes de ensenar o guardar"))
    print()


def main():
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass
    args = sys.argv[1:]
    con_claves = "--claves" in args
    rutas = [a for a in args if a != "--claves"]
    if not rutas:
        print(__doc__)
        return
    textos = []
    for ruta in rutas:
        if ruta == "-":
            texto, nombre = sys.stdin.read(), "entrada estandar"
        else:
            with open(ruta, encoding="utf-8") as f:
                texto, nombre = f.read(), ruta
        textos.append((texto, nombre))
        medir(texto, nombre)
        medir_arquitectura(texto, nombre)
        if con_claves:
            listar_claves(texto, nombre)
    if con_claves and len(textos) == 2:
        comparar_claves(textos[0][0], textos[1][0], textos[0][1], textos[1][1])


if __name__ == "__main__":
    main()
