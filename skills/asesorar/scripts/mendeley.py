import zipfile, re, sys, json, base64, collections
sys.stdout.reconfigure(encoding='utf8')
z = zipfile.ZipFile(sys.argv[1])
x = z.read("word/document.xml").decode("utf8")
tags = re.findall(r'<w:tag w:val="MENDELEY_CITATION_v3_([^"]+)"', x)
bib = re.findall(r'<w:tag w:val="MENDELEY_BIBLIOGRAPHY[^"]*"', x)
print("citas Mendeley:", len(tags), "bibliografía Mendeley:", len(bib))
items = {}
uso = collections.Counter()
textos = []
for t in tags:
    t = t + '=' * (-len(t) % 4)
    d = json.loads(base64.b64decode(t).decode('utf8'))
    textos.append(d.get('manualOverride', {}).get('citeprocText', ''))
    for ci in d.get('citationItems', []):
        it = ci.get('itemData', {})
        k = it.get('id') or ci.get('id')
        items[k] = it
        uso[k] += 1
print("fuentes distintas:", len(items))
anios = collections.Counter()
filas = []
for k, it in items.items():
    au = it.get('author', [])
    a = ', '.join((p.get('family') or p.get('literal') or '?') for p in au[:3]) + (' et al.' if len(au) > 3 else '')
    y = (it.get('issued', {}).get('date-parts') or [['?']])[0][0]
    anios[y] += 1
    filas.append((str(y), it.get('type', ''), uso[k], a, it.get('title', '')[:80], (it.get('container-title') or it.get('publisher') or '')[:35], it.get('DOI', '')))
for f in sorted(filas):
    print(' | '.join(str(v) for v in f))
print(sorted(anios.items(), key=lambda kv: str(kv[0])))
print("ejemplos de texto:", textos[:8])
