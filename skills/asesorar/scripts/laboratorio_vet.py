import pymupdf, glob, os, re, sys, csv
base = sys.argv[1]
HEMO = ["LEU","LIN","MON","NEU","EOS","BAS","LYM%","MON%","NEU%","EOS%","BAS%","ERI","Hb","HCT","VCM","HCM","CHCM","RDWc","RDWs","PLT","VPM","PCT","PDWc","PDWs"]
BIO = ["ALB","TP","GLU","ALP","AST","GGT","TBIL","CPK","BUN","CREA","tCO2","Ca","Na","K","#GLOB","#UREA","#C-Ca","#A/G","#B/C","#Na/K"]
num = re.compile(r"^[<>]?-?\d+(\.\d+)?$")

def lines(f):
    return [l.strip() for p in pymupdf.open(f) for l in p.get_text().splitlines()]

rows = {}
for f in sorted(glob.glob(base + "/resultadosdehem*/*.pdf")):
    L = lines(f); cab = int(re.search(r"(\d+)", os.path.basename(f)).group(1))
    r = rows.setdefault(cab, {"cab": cab})
    try:
        i = L.index("ID del paciente"); r["nombre_h"] = L[i+1].replace("Edad","").strip()
        r["edad"] = L[i+2]
        i = L.index("Especie"); r["sexo_h"] = L[i+2]
        i = L.index("Fecha de la prueba"); r["fecha_h"] = L[i+1].split()[0]
        r["formato_h"] = "normal"
    except Exception:
        r["formato_h"] = "OTRO"
        r["nombre_h"] = L[3].split()[0]; r["edad"] = next(x for x in L if re.match(r"^\d+ a$", x)); r["sexo_h"] = next(x for x in L if x in ("Macho","Hembra"))
        r["fecha_h"] = next(x for x in L if re.match(r"^\d\d/\d\d/\d{4}", x)).split()[0]
    r["medico_h"] = L[L.index("Médico")+1] if "Médico" in L else ""
    seen = set()
    for k, x in enumerate(L):
        if x in HEMO and x not in seen and k+1 < len(L):
            tok = L[k+1].split()[0] if L[k+1].split() else ""
            if num.match(tok) and not L[k+1].endswith("fl") or (num.match(tok) and x in ("VCM","RDWs","VPM","PDWs") and k > 60):
                r["h_"+x] = tok; seen.add(x)
    r["flags_h"] = " | ".join(L[L.index("Indicadores de diagnóstico")+1:L.index("PrVW")]) if "PrVW" in L and "Indicadores de diagnóstico" in L else ""

for f in sorted(glob.glob(base + "/resultadosdeval*/*.pdf")):
    L = lines(f); cab = int(re.search(r"(\d+)", os.path.basename(f)).group(1))
    r = rows.setdefault(cab, {"cab": cab})
    r["nombre_b"] = L[L.index("Nombre pac.")+1].lstrip(": ").strip()
    r["sexo_b"] = L[L.index("Sexo")+1].lstrip(": ").strip()
    r["raza_b"] = L[L.index("Raza")+1].lstrip(": ").strip()
    r["dueno"] = L[L.index("Dueño")+1].lstrip(": ").strip()
    r["id_b"] = L[L.index("Id del pac.")+1].lstrip(": ").strip()
    r["fecha_b"] = L[L.index("Fecha")+1].lstrip(": ").strip()
    r["ind"] = next((x for x in L if x.startswith("LIP:")), "")
    seen = set()
    for k, x in enumerate(L):
        if x in BIO and x not in seen and k+1 < len(L):
            r["b_"+x.lstrip("#")] = L[k+1]; seen.add(x)
    r["pags_b"] = len(pymupdf.open(f))

cols = []
for r in rows.values():
    for c in r:
        if c not in cols: cols.append(c)
with open(sys.argv[2], "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, cols); w.writeheader(); [w.writerow(rows[k]) for k in sorted(rows)]
print(len(rows), "caballos;", len(cols), "columnas")

