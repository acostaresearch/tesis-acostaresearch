#!/usr/bin/env python3
"""Extrae la cabecera de un informe de similitud de Turnitin en PDF.

Uso:  python leer_informe.py informe.pdf

Devuelve el porcentaje general, el desglose por tipo de fuente, qué se filtro,
el numero de fuentes y las de mayor peso. Sirve para decidir si el porcentaje
es un bloque copiado o un mosaico de coincidencias cortas, que se atacan de
formas completamente distintas.

Requiere pdftotext (poppler-utils).
"""
import re
import subprocess
import sys


def extraer_texto(pdf):
    try:
        return subprocess.run(
            ["pdftotext", "-layout", pdf, "-"],
            capture_output=True, text=True, check=True,
        ).stdout
    except FileNotFoundError:
        sys.exit("Falta pdftotext. Instalar poppler-utils.")
    except subprocess.CalledProcessError as e:
        sys.exit(f"pdftotext fallo: {e}")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    t = extraer_texto(sys.argv[1])

    def buscar(patron, defecto="no encontrado"):
        m = re.search(patron, t, re.I)
        return m.group(1).strip() if m else defecto

    general = buscar(r"(\d+)\s*%\s*Similitud general")
    internet = buscar(r"(\d+)\s*%\s*\n?\s*(?:\S+\s+)?Fuentes de Internet")
    public = buscar(r"(\d+)\s*%\s*\n?\s*(?:\S+\s+)?Publicaciones")
    entregados = buscar(r"(\d+)\s*%\s*\n?\s*(?:\S+\s+)?Trabajos entregados")
    palabras = buscar(r"([\d.,]+)\s+palabras")
    paginas = buscar(r"(\d+)\s+p[áa]ginas")
    entrega = buscar(r"(trn:oid:+[\d:]+)")

    filtros = []
    bloque = re.search(r"Filtrado desde el informe(.*?)(Fuentes principales|Marcas)", t, re.S | re.I)
    if bloque:
        for linea in bloque.group(1).splitlines():
            linea = linea.strip()
            if linea and len(linea) < 40:
                filtros.append(linea)

    fuentes = re.findall(r"\n\s*(\d{1,3})\s+(Internet|Publicaci[óo]n|Trabajos)", t)
    n_fuentes = max((int(n) for n, _ in fuentes), default=0)
    top = re.findall(r"\n(\S[^\n]{3,70}?)\s+(\d+)%\s*\n", t)
    top = [(nombre.strip(), pct) for nombre, pct in top if not nombre.startswith("Fuentes")][:6]

    alerta = "SI" if re.search(r"no se han detectado manipulaciones", t, re.I) else "revisar"

    print(f"Identificador de entrega : {entrega}")
    print(f"Similitud general        : {general}%")
    print(f"  Internet               : {internet}%")
    print(f"  Publicaciones          : {public}%")
    print(f"  Trabajos entregados    : {entregados}%")
    print(f"Filtrado                 : {', '.join(filtros) if filtros else 'no declarado'}")
    print(f"Palabras / paginas       : {palabras} / {paginas}")
    print(f"Fuentes listadas         : {n_fuentes}")
    print(f"Sin marcas de integridad : {alerta}")
    if top:
        print("Fuentes de mayor peso:")
        for nombre, pct in top:
            print(f"  {pct:>3}%  {nombre}")

    print()
    try:
        g = int(general)
        pal = int(re.sub(r"[.,]", "", palabras))
        print(f"Palabras coincidentes (estimado): ~{round(pal * g / 100)}")
    except (ValueError, TypeError):
        pass

    try:
        suma = int(internet) + int(public) + int(entregados)
        if suma > int(general):
            print(f"Solapamiento: los cubos suman {suma}% y el total es {general}%.")
            print("  Una misma frase coincide con varias fuentes a la vez, que es la")
            print("  firma de una redaccion estandar del campo, no de una copia.")
    except (ValueError, TypeError):
        pass

    if top:
        try:
            if int(top[0][1]) <= 3:
                print("\nMOSAICO: ninguna fuente pasa del 3%. No hay bloque copiado.")
                print("  El porcentaje se reparte en coincidencias cortas. La palanca")
                print("  principal suele ser la configuracion del informe, no reescribir.")
            else:
                print(f"\nBLOQUE: la fuente principal aporta {top[0][1]}%. Localizarla en el")
                print("  cuerpo y revisar si es cita mal marcada antes de tocar la redaccion.")
        except ValueError:
            pass


if __name__ == "__main__":
    main()
