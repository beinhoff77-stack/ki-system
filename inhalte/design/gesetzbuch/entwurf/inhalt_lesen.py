#!/usr/bin/env python3
"""Liest den Inhalt des Mathe-Profis (Zweig origin/mathe-profi) und schreibt teile/inhalt.json.
Der Designer erfindet keinen Mathe-Inhalt: Sätze, Beispiele und Klassen kommen wörtlich aus diesen Dateien.
Aufruf im Ordner entwurf/:  python3 inhalt_lesen.py"""
import json, pathlib, re, subprocess
hier = pathlib.Path(__file__).resolve().parent; repo = hier.parents[3]
def zeig(pfad): return subprocess.run(['git', '-C', str(repo), 'show', 'origin/mathe-profi:' + pfad], capture_output=True, text=True, check=True).stdout
stand = subprocess.run(['git', '-C', str(repo), 'rev-parse', '--short', 'origin/mathe-profi'], capture_output=True, text=True).stdout.strip()
R = 'inhalte/mathe-profi/regeln-uebersicht/'
themen = {t['thema_schluessel']: {'titel': t['titel'], 'ort': t['ort'], 'gebiet': t['gebiet']} for t in json.loads((repo / 'inhalte' / 'themenliste.json').read_text(encoding='utf-8'))}

def einzeln(text, kopf):
    aus = []
    for m in re.finditer(kopf, text, re.M):
        ende = re.search(r'^#{2,3} ', text[m.end():], re.M); block = text[m.end(): m.end() + ende.start() if ende else len(text)]
        def feld(name): 
            f = re.search(r'\*\*' + name + r'[^*]*\*\*:? ?(.*)', block); return f.group(1).strip() if f else ''
        zeilen = []
        for z in re.findall(r'^\| (\d+) \| (.*?) \|(?: `(.*?)` \|)?$', block, re.M):
            zeilen.append({'klasse': int(z[0]), 'text': z[1].strip(), 'thema': z[2] or None})
        aus.append({'kopf': m.groups(), 'merksatz': re.search(r'^> \*\*(.*)\*\*', block, re.M).group(1), 'warum': feld('Warum das gilt'), 'nicht': feld('Wo es nicht gilt'),
                    'klassen': zeilen, 'baut': feld('Baut auf'), 'bild': feld('Bild'), 'schulart': (re.search(r'^(Gymnasium .*)$', block, re.M) or [None, ''])[1]})
    return aus

sonne = zeig(R + 'sonne.md'); regeln = []
braucht = {int(a): [int(x) for x in re.findall(r'(\d+) ', b + ' ')] for a, b in re.findall(r'^- \*\*(\d+) .*?\*\* braucht: (.*)$', sonne, re.M)}
etage = {}
for nr, name, liste in re.findall(r'^\| \*\*(\d) · (.*?)\*\* \| (.*) \|$', sonne, re.M):
    for x in re.findall(r'(\d+) ', liste): etage[int(x)] = int(nr)
etagen = [{'nr': int(nr), 'name': name} for nr, name, _ in re.findall(r'^\| \*\*(\d) · (.*?)\*\* \| (.*) \|$', sonne, re.M)]
for e in einzeln(sonne, r'^### (\d+)\. (.*)$'):
    nr = int(e['kopf'][0]); regeln.append({'id': 'R%d' % nr, 'nr': nr, 'name': e['kopf'][1], 'etage': etage[nr], 'braucht': ['R%d' % x for x in braucht.get(nr, [])], **{k: e[k] for k in ('merksatz', 'warum', 'nicht', 'klassen', 'bild')}})
assert len(regeln) == 14 and sorted(etage) == list(range(1, 15))

planet_md = zeig(R + 'planet-flaeche-und-raum.md'); ausf = {}
for e in einzeln(planet_md, r'^### (F\d+) · (.*)$'):
    ausf[e['kopf'][0]] = {k: e[k] for k in ('merksatz', 'warum', 'nicht', 'klassen', 'bild', 'baut', 'schulart')}
assert len(ausf) == 19

inhalt = zeig(R + 'inhalt.md'); planeten = []; gesetze = []
for m in re.finditer(r'^### (.*?) – (\d+) Gesetze \((.*?)\)$', inhalt, re.M):
    ende = re.search(r'^#{2,3} ', inhalt[m.end():], re.M); block = inhalt[m.end(): m.end() + ende.start()]
    p = {'name': m.group(1), 'zahl': int(m.group(2)), 'lage': m.group(3), 'abschnitte': []}; abschnitt = None
    for z in block.splitlines():
        a = re.match(r'^\| \| \*(.*?)\* \|', z)
        if a: abschnitt = a.group(1); p['abschnitte'].append(abschnitt); continue
        g = re.match(r'^\| ([A-Z]+\d+) \| \*\*(.*?)\*\* \| (.*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|$', z)
        if g:
            e = {'id': g.group(1), 'name': g.group(2), 'satz': g.group(3).strip(), 'gym': g.group(4).strip(), 'rs': g.group(5).strip(), 'ib': g.group(6).strip(), 'sonne': g.group(7).strip(), 'planet': p['name'], 'abschnitt': abschnitt}
            if e['id'] in ausf: e.update(ausf[e['id']])
            gesetze.append(e)
    p['gezaehlt'] = sum(1 for g in gesetze if g['planet'] == p['name']); planeten.append(p)
arbeit = [{'name': a, 'satz': b} for a, b in re.findall(r'^\| ([A-ZÄÖÜ][^|*]*?) \| \*\*(.*?)\*\* \|$', inhalt[inhalt.index('## Die Arbeitsweisen'):], re.M)]
aus = {'stand': stand, 'etagen': etagen, 'regeln': regeln, 'planeten': planeten, 'gesetze': gesetze, 'arbeitsweisen': arbeit, 'themen': {k: v for k, v in themen.items() if any(z['thema'] == k for r in regeln for z in r['klassen'])}}
(hier / 'teile' / 'inhalt.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1), encoding='utf-8')
print('Stand', stand, '· Regeln', len(regeln), '· Gesetze', len(gesetze), '· Arbeitsweisen', len(arbeit))
for p in planeten: print(' ', p['name'], p['zahl'], 'gezählt', p['gezaehlt'], p['abschnitte'])
print(etagen); print(regeln[5]['klassen'][0], regeln[5]['braucht']); print([g['id'] for g in gesetze if 'warum' in g][:3], gesetze[0]); print(aus['themen'].get('zahlen.rechengesetze'))
