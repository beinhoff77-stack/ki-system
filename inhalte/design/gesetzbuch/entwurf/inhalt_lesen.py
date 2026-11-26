#!/usr/bin/env python3
"""Liest den Inhalt des Mathe-Profis (Zweig origin/mathe-profi, Fassung Auftrag 11) und schreibt teile/inhalt.json.
Der Designer erfindet keinen Mathe-Inhalt: Sätze, Beispiele, Klassen und Zeichen-Vorgaben kommen wörtlich aus diesen Dateien.
Aufruf im Ordner entwurf/:  python3 inhalt_lesen.py"""
import json, pathlib, re, subprocess
hier = pathlib.Path(__file__).resolve().parent; repo = hier.parents[3]
def zeig(pfad): return subprocess.run(['git', '-C', str(repo), 'show', 'origin/mathe-profi:' + pfad], capture_output=True, text=True, check=True).stdout
stand = subprocess.run(['git', '-C', str(repo), 'rev-parse', '--short', 'origin/mathe-profi'], capture_output=True, text=True).stdout.strip()
R = 'inhalte/mathe-profi/regeln-uebersicht/'
themen = {t['thema_schluessel']: {'titel': t['titel'], 'ort': t['ort']} for t in json.loads((repo / 'inhalte' / 'themenliste.json').read_text(encoding='utf-8'))}

def bloecke(text, kopf, stopp):
    """Abschnitte, die mit `kopf` beginnen und vor der nächsten Überschrift `stopp` enden."""
    for m in re.finditer(kopf, text, re.M):
        e = re.search(stopp, text[m.end():], re.M); yield m, text[m.end(): m.end() + e.start() if e else len(text)]
def feld(block, name):
    f = re.search(r'^\*\*' + name + r'[^*\n]*\*\*:? ?(.*)$', block, re.M); return f.group(1).strip() if f else ''
def zeichen(block):
    z = re.search(r'^\*\*Zeichen-Vorgabe\*\*\n((?:- .*\n?)+)', block, re.M)
    return {a: b.strip() for a, b in re.findall(r'^- \*\*(.*?):\*\* (.*)$', z.group(1), re.M)} if z else None
def beispiele(block):
    aus = []
    for z in re.findall(r'^\| (\d+) \| (\w+) \| (.*?) \|(?: `(.*?)` \|)?$', block, re.M): aus.append({'klasse': int(z[0]), 'art': z[1], 'text': z[2].strip(), 'thema': z[3] or None})
    return aus
def eintrag(block):
    return {'satz': re.search(r'^> \*\*(.*)\*\*', block, re.M).group(1), 'genau': feld(block, 'Genau gesagt'), 'warum': feld(block, 'Warum'), 'voraus': feld(block, 'Voraussetzung'), 'fehler': feld(block, 'Häufiger Fehler'),
            'verwandt': feld(block, 'Verwandt'), 'weg': feld(block, 'Möglicher Erklärweg über'), 'klassen': beispiele(block), 'zeichen': zeichen(block)}

# Sonne
sonne = zeig(R + 'sonne.md'); etage = {}; etagen = []
for nr, name, liste in re.findall(r'^\| \*\*(\d) · (.*?)\*\* \| (.*) \|$', sonne, re.M):
    etagen.append({'nr': int(nr), 'name': name})
    for x in re.findall(r'(?:^| · )(\d+) ', liste): etage[int(x)] = int(nr)
regeln = []
for m, block in bloecke(sonne, r'^### (\d+)\. (.*)$', r'^#{2,3} '):
    nr = int(m.group(1)); regeln.append({'id': 'R%d' % nr, 'nr': nr, 'name': m.group(2), 'etage': etage[nr], **eintrag(block)})
assert len(regeln) == 14 and sorted(etage) == list(range(1, 15)) and all(r['zeichen'] and r['klassen'] for r in regeln)

# Ausgearbeitete Planeten: Ideen und Gesetze
ausf = {}; ideen_ausf = {}
for datei, planet in (('planet-flaeche-und-raum.md', 'Fläche und Raum'), ('planet-geometrie.md', 'Geometrie')):
    t = zeig(R + datei)
    for m, block in bloecke(t, r'^## Idee (\d+) · (.*)$', r'^#{2,3} '):
        ideen_ausf[(planet, int(m.group(1)))] = {'warum': feld(block, 'Warum diese Idee trägt'), 'zeichen': zeichen(block)}; assert zeichen(block)
    for m, block in bloecke(t, r'^#### ([A-Z]+\d+) · (.*)$', r'^#{2,4} '):
        e = eintrag(block); e['schulart'] = (re.search(r'^(Gymnasium: .*)$', block, re.M) or [None, ''])[1]; ausf[m.group(1)] = e
assert len(ausf) == 49, len(ausf)

# Ebene 1: die 42 Sätze
e1 = zeig(R + 'ebene1.md'); ZEILE = r'^(\d+)\. \*\*(.*?)\*\*  \n   \*Genau gesagt:\* (.*?)  \n   <sub>(.*?)</sub>$'
sonnen_satz = {int(n): (s, g, k) for n, s, g, k in re.findall(ZEILE, e1[:e1.index('## Die Planeten')], re.M)}
assert len(sonnen_satz) == 14
for r in regeln: assert (r['satz'], r['genau'], r['name']) == sonnen_satz[r['nr']], (r['nr'], r['satz'], sonnen_satz[r['nr']])
ideen = {}
for m, block in bloecke(e1[e1.index('## Die Planeten'):e1.index('## Wo der Merksatz')], r'^### (.*?) – (\d+) tragende Ideen$', r'^#{2,3} '):
    liste = []
    for n, satz, gen, sub in re.findall(ZEILE, block, re.M):
        kurz, k, gs = re.fullmatch(r'(.*?) – trägt (\d+) Gesetze: (.*)', sub).groups()
        ids = re.findall(r'(?:^|, )([A-Z]+\d+) ', gs); assert len(ids) == int(k), (satz, ids)
        liste.append({'nr': int(n), 'satz': satz, 'genau': gen, 'kurz': kurz, 'gesetze': ids, **ideen_ausf.get((m.group(1), int(n)), {})})
    assert len(liste) == int(m.group(2)); ideen[m.group(1)] = liste
assert sum(len(v) for v in ideen.values()) == 28

# Ebene 2: alle Einträge und Stichwörter
inhalt = zeig(R + 'inhalt.md'); planeten = []; gesetze = []
for m, block in bloecke(inhalt[inhalt.index('## Alle Einträge'):], r'^### (.*?) – (\d+) Einträge$', r'^#{2,3} '):
    p = {'name': m.group(1), 'zahl': int(m.group(2)), 'ideen': ideen.get(m.group(1), [])}
    for z in block.splitlines():
        sp = [s.strip() for s in z.strip().strip('|').split(' | ')] if z.startswith('| ') else []
        if len(sp) >= 8 and re.fullmatch(r'[A-Z]+\d+', sp[0]):
            e = {'id': sp[0], 'name': sp[1].strip('*'), 'satz': sp[2], 'idee': int(sp[3]) if sp[3].isdigit() else None, 'gym': sp[4], 'rs': sp[5], 'ib': sp[6], 'sonne': sp[7], 'planet': p['name']}
            if e['id'] in ausf: e.update(ausf[e['id']])
            gesetze.append(e)
    assert sum(1 for g in gesetze if g['planet'] == p['name']) == p['zahl'], p; planeten.append(p)
st = inhalt[inhalt.index('## Stichwörter'):inhalt.index('## Die Zahl')]
stichwoerter = [{'wort': a.strip(), 'ziel': ('R' + b.split()[-1]) if b.startswith('Rechenregel') else b.strip()} for a, b in re.findall(r'^\| (?!Suchwort|---)(.*?) \| (.*?) \|$', st, re.M)]
arbeit = [{'name': a, 'satz': b} for a, b in re.findall(r'^\| ([A-ZÄÖÜ][^|*]*?) \| \*\*(.*?)\*\* \|$', inhalt[inhalt.index('## Die Arbeitsweisen'):], re.M)]
benutzt = {z['thema'] for r in regeln for z in r['klassen'] if z['thema']}
aus = {'stand': stand, 'etagen': sorted(etagen, key=lambda e: e['nr']), 'regeln': regeln, 'planeten': planeten, 'gesetze': gesetze, 'stichwoerter': stichwoerter, 'arbeitsweisen': arbeit, 'themen': {k: themen[k] for k in benutzt if k in themen}}
(hier / 'teile' / 'inhalt.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1), encoding='utf-8')
print('Stand', stand, '· Regeln', len(regeln), '· Ideen', sum(len(v) for v in ideen.values()), '· Gesetze', len(gesetze), '· ausgearbeitet', len(ausf), '· Stichwörter', len(stichwoerter), '· Arbeitsweisen', len(arbeit))
print([ (p['name'], p['zahl'], len(p['ideen'])) for p in planeten]); print(regeln[5]['klassen'][2:4], regeln[5]['weg']); print([s for s in stichwoerter if 'Kegel' in s['wort'] or 'Minus' in s['wort']])
g = next(x for x in gesetze if x['id'] == 'G24'); print(g['satz'][:80], '|', g.get('voraus', '')[:60], '|', len(g.get('klassen', [])), g.get('weg'))
