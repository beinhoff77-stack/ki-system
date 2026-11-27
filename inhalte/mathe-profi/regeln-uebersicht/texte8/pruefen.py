#!/usr/bin/env python3
"""Prüft die Daten in texte8/: Pflichtfelder, Längen, Kennungen, alle Zahlenbeispiele (exakt, mit Brüchen),
Verweise auf Aufgaben und Lehrplan-Quellen. Aufruf:  python3 -I inhalte/mathe-profi/regeln-uebersicht/texte8/pruefen.py
Endet mit „OK“, sonst mit Fehlerliste und Exit-Code 1."""
import json, math, pathlib, re, sys
from fractions import Fraction as F
hier = pathlib.Path(__file__).resolve().parent
repo = hier.parents[3]
fehler = []
def f(msg): fehler.append(msg)
def laden(p): return json.loads((p if isinstance(p, pathlib.Path) else hier / p).read_text(encoding='utf-8'))

# ---------- Rechner ----------
def teiler(n): n = int(n); return tuple(t for t in range(1, n + 1) if n % t == 0)
def quersumme(n): return F(sum(int(z) for z in str(int(n))))
def ist_prim(n): n = int(n); return F(1 if n > 1 and all(n % t for t in range(2, int(n ** 0.5) + 1)) else 0)
def kaufm(n, s): return F(math.floor(F(n) / F(s) + F(1, 2))) * F(s)
UMGEBUNG = {'__builtins__': {}}
HILF = {'F': F, 'teiler': teiler, 'quersumme': quersumme, 'ist_prim': ist_prim, 'kaufm': kaufm, 'abs': abs, 'sum': sum, 'W': tuple(range(1, 7))}
def wert(ausdruck, mit):
    ausdruck = ausdruck.replace('−', '-')
    code = re.sub(r'(?<![\w.])(\d+(?:\.\d+)?)', r'F("\1")', ausdruck)
    return eval(code, {**UMGEBUNG, **HILF, **{k: F(str(v)) for k, v in mit.items()}})
OPS = {'==': lambda a, b: a == b, '!=': lambda a, b: a != b, '<': lambda a, b: a < b, '>': lambda a, b: a > b, '<=': lambda a, b: a <= b, '>=': lambda a, b: a >= b}
n_pruef = 0
def pruefe(liste, ort):
    global n_pruef
    if not liste: f('%s: keine Prüfungen' % ort); return
    for p in liste:
        n_pruef += 1
        try:
            if 'bereich' in p:
                (name, (a, b)), = p['bereich'].items()
                treffer = [OPS[p['rel']](wert(p['l'], {**p.get('mit', {}), name: x}), wert(p['r'], {**p.get('mit', {}), name: x})) for x in range(a, b + 1) if x not in p.get('ohne', [])]
                ok = all(treffer) if p.get('modus') == 'alle' else not any(treffer)
            else:
                ok = OPS[p['rel']](wert(p['l'], p.get('mit', {})), wert(p['r'], p.get('mit', {})))
        except Exception as e:
            f('%s: Ausdruck nicht rechenbar %r (%s)' % (ort, p, e)); continue
        if not ok: f('%s: stimmt nicht: %s' % (ort, json.dumps(p, ensure_ascii=False)))

def klasse_in(angabe, k):
    m = re.fullmatch(r'(\d+)(?:–(\d+))?', angabe.strip())
    return bool(m) and int(m.group(1)) <= k <= int(m.group(2) or m.group(1))
def satzanzahl(t): return len(re.findall(r'[.!?](?:\s|$)', t))
def pflicht(d, felder, ort):
    for x in felder:
        if x not in d or d[x] in (None, '', []): f('%s: Pflichtfeld fehlt: %s' % (ort, x))

kenn = {k['kennung']: k for k in laden(hier.parent / 'kennungen.json')['kennungen']}
rr = [k for k, v in kenn.items() if v['art'] == 'rechenregel']; ide = [k for k, v in kenn.items() if v['art'] == 'idee']
assert len(rr) == 14 and len(ide) == 28
inh = laden(repo / 'inhalte/design/gesetzbuch/entwurf/teile/inhalt.json')
kurz = laden(repo / 'inhalte/design/gesetzbuch/entwurf7/teile/kurz.json')['texte']
themen_dir = repo / 'inhalte/themen'
themenliste = {t['thema_schluessel'] for t in laden(repo / 'inhalte/themenliste.json')}

# ---------- 1 Kurzbeschreibungen ----------
d = laden('kurzbeschreibungen.json'); E = d['eintraege']
if sorted(e['kennung'] for e in E) != sorted(rr + ide): f('kurzbeschreibungen: Kennungen stimmen nicht mit kennungen.json überein')
ber = 0
for e in E:
    o = 'kurz ' + e['kennung']
    pflicht(e, ['kennung', 'entwurf_schluessel', 'kurz_alt', 'befund', 'grund', 'endfassung'], o)
    if kurz[e['entwurf_schluessel']]['text'] != e['kurz_alt']: f(o + ': kurz_alt weicht von kurz.json ab')
    if e['befund'] not in ('in Ordnung', 'berichtigt'): f(o + ': befund unbekannt')
    if e['befund'] == 'berichtigt':
        ber += 1
        if not e['kurz_neu'] or e['kurz_neu'] != e['endfassung'] or e['kurz_neu'] == e['kurz_alt']: f(o + ': berichtigt, aber kurz_neu fehlt oder gleich alt')
    elif e['endfassung'] != e['kurz_alt']: f(o + ': in Ordnung, aber Endfassung weicht ab')
    if len(e['endfassung']) > 110: f(o + ': Endfassung länger als 110 Zeichen (%d)' % len(e['endfassung']))
    if len(e['endfassung']) < 25: f(o + ': Endfassung zu kurz')
    if satzanzahl(e['endfassung']) != 1: f(o + ': Endfassung ist nicht genau ein Satz')
    if e['endfassung_laenge'] != len(e['endfassung']): f(o + ': Längenfeld falsch')
z = d['zusammenfassung']
if (z['geprueft'], z['berichtigt'], z['in_ordnung']) != (42, ber, 42 - ber): f('kurzbeschreibungen: Zusammenfassung stimmt nicht')
merks_start = {s: kenn[k]['merksatz'] for k, s in ((e['kennung'], e['entwurf_schluessel']) for e in E)}

# ---------- 2 Merksätze ----------
d = laden('merksaetze.json'); M = d['regeln']
if [m['kennung'] for m in M] != rr: f('merksaetze: Reihenfolge oder Kennungen falsch')
for m in M:
    o = 'merksatz ' + m['kennung']
    pflicht(m, ['kennung', 'name', 'merksatz', 'urteil', 'im_bestand_gedeckt', 'luecken'], o)
    if m['merksatz'] != kenn[m['kennung']]['merksatz']: f(o + ': Merksatz weicht von kennungen.json ab')
    if m['merksatz_geaendert'] is not False and not m.get('aenderung'): f(o + ': geändert ohne alt/neu/Begründung')
    if m['merksatz_geaendert']:
        pflicht(m['aenderung'], ['alt', 'neu', 'grund'], o + ' aenderung')
    for i, l in enumerate(m['luecken']):
        pflicht(l, ['wo', 'text', 'grund', 'pruefung'], '%s lücke %d' % (o, i + 1))
        if l['wo'] not in ('genau', 'voraus', 'fehler'): f('%s lücke %d: wo unbekannt' % (o, i + 1))
        if len(l['text']) > 400: f('%s lücke %d: Text über 400 Zeichen' % (o, i + 1))
        pruefe(l['pruefung'], '%s lücke %d' % (o, i + 1))
    if 'kurzfassung' in m:
        k = m['kurzfassung']
        for x in ('haupt', 'kompakt'):
            if len(k[x]) >= len(m['merksatz']): f(o + ': Kurzfassung %s nicht kürzer als der Merksatz' % x)
        if len(k['kompakt']) > 80: f(o + ': kompakte Kurzfassung über 80 Zeichen')
        pruefe([{'l': '1/2+1/3', 'rel': '==', 'r': '3/6+2/6'}, {'l': '(2/3)*(3/4)', 'rel': '==', 'r': '(2*3)/(3*4)'}, {'l': '6/(1/2)', 'rel': '==', 'r': '6*2'}], o + ' Beispiele zur Kurzfassung')
if len(M[9]['merksatz']) < 100: f('Regel 10: Merksatz sollte der lange sein')

# ---------- 3 Arbeitsweisen ----------
d = laden('arbeitsweisen.json'); A = d['arbeitsweisen']
if [a['name'] for a in A] != [x['name'] for x in inh['arbeitsweisen']] or len(A) != 8: f('arbeitsweisen: Namen oder Zahl weichen vom Bestand ab')
for a in A:
    o = 'weise ' + a['name']
    pflicht(a, ['name', 'kurz', 'beispiel', 'erklaerung', 'merksatz', 'entwurf_schluessel'], o)
    if len(a['kurz']) > 110 or satzanzahl(a['kurz']) != 1: f(o + ': Kurzbeschreibung nicht ein Satz bis 110 Zeichen')
    if not 2 <= satzanzahl(a['erklaerung']) <= 3: f(o + ': Erklärung hat %d Sätze' % satzanzahl(a['erklaerung']))
    if len(a['beispiel']['text']) > 330: f(o + ': Beispieltext zu lang')
    if a['beispiel']['klasse'] not in (5, 6): f(o + ': Beispiel nicht Klasse 5/6')
    pruefe(a['beispiel']['pruefung'], o)

# ---------- 5 Einzelregeln ----------
d = laden('einzelregeln.json'); ges = {g['id']: g for g in inh['gesetze']}
nur_name = {i for i, g in ges.items() if 'warum' not in g and 'genau' not in g}
if len(nur_name) != 103: f('Bestand: erwartet 103 Einzelregeln ohne Ausarbeitung, gefunden %d' % len(nur_name))
alle = []
for schluessel, kl in (('klasse5', '5'), ('klasse8', '8')):
    L = d[schluessel]
    if len(L) != 15 or [x['rang'] for x in L] != list(range(1, 16)): f(schluessel + ': nicht 15 Einträge mit Rang 1 bis 15')
    for x in L:
        o = '%s %s' % (schluessel, x['id']); alle.append(x['id'])
        pflicht(x, ['id', 'name', 'begruendung', 'beispiel', 'grenze', 'pruefung'], o)
        if x['id'] not in nur_name: f(o + ': gehört nicht zu den 103 nur mit Name und Satz')
        elif not klasse_in(ges[x['id']]['gym'], int(kl)): f('%s: Klasse %s nicht in Gymnasium-Angabe %r' % (o, kl, ges[x['id']]['gym']))
        if x['name'] != ges.get(x['id'], {}).get('name'): f(o + ': Name weicht ab')
        if satzanzahl(x['begruendung']) != 1: f(o + ': Begründung nicht ein Satz')
        pflicht(x['grenze'], ['art', 'text'], o + ' grenze')
        if x['grenze']['art'] not in ('gilt nicht', 'typischer Fehler'): f(o + ': Art der Grenze unbekannt')
        pruefe(x['pruefung'], o)
if len(set(alle)) != 30: f('einzelregeln: doppelte Einträge')

# ---------- 4 Beispielaufgaben ----------
d = laden('beispielaufgaben.json'); cache = {}
def aufgaben(datei):
    if datei not in cache: cache[datei] = laden(repo / datei)['aufgaben']
    return cache[datei]
def pruefe_aufgabe(a, o):
    pflicht(a, ['datei', 'lernkarte', 'index_in_aufgaben', 'klasse', 'zweck'], o)
    try: t = aufgaben(a['datei'])[a['index_in_aufgaben']]
    except Exception as e: f('%s: Aufgabe nicht gefunden (%s)' % (o, e)); return
    if t['l'] != a['lernkarte']: f('%s: Lernkarte stimmt nicht (%s)' % (o, t['l']))
    if t['p'] not in ('uebung', 'test', 'korrektur', 'sicherung', 'bonus'): f(o + ': Art unbekannt')
for z in d['zuordnung']:
    if not z['regel'] in kenn: f('zuordnung: Kennung ' + z['regel'])
    if not 1 <= len(z['aufgaben']) <= 3: f('zuordnung %s: nicht 1 bis 3 Aufgaben' % z['regel'])
    for i, a in enumerate(z['aufgaben'] + z['weitere']): pruefe_aufgabe(a, '%s Aufgabe %d' % (z['regel'], i + 1))
zu = laden(repo / 'inhalte/mathe-profi/schritt1/kennungen-zuordnung.json')['aufgaben']
for s in d['stichprobe_bestehende_zuordnung']['ergebnis']:
    echt = sorted(a['kennung_aufgabe'] for a in zu if a['regel'] == s['regel'])
    if echt != sorted(s['zugeordnet']): f('stichprobe %s: zugeordnete Aufgaben weichen von kennungen-zuordnung.json ab' % s['regel'])
    for i, a in enumerate(s.get('vorschlag', [])): pruefe_aufgabe(a, 'stichprobe %s Vorschlag %d' % (s['regel'], i + 1))

# ---------- 6 Lehrplan ----------
d = laden('lehrplan.json')
if [r['kennung'] for r in d['regeln']] != rr: f('lehrplan: Kennungen oder Reihenfolge')
for q in d['quellen']:
    if not (repo / q).exists(): f('lehrplan: Quelle fehlt: ' + q)
for r in d['regeln']:
    o = 'lehrplan ' + r['kennung']
    pflicht(r, ['einfuehrung', 'lehrplan_kopie_neu_in_jahr', 'klassen_in_denen_die_regel_vorkommt', 'befund', 'nicht_geprueft'], o)
    if r['einfuehrung']['thema'] not in themenliste: f(o + ': Thema nicht in themenliste.json')
    if not (themen_dir / (r['einfuehrung']['thema'] + '.json')).exists(): f(o + ': Themen-Datei fehlt')
    for k in r['klassen_in_denen_die_regel_vorkommt']:
        if k['thema'] not in themenliste: f(o + ': Thema %s unbekannt' % k['thema'])

if fehler:
    print('\n'.join(fehler)); print('FEHLER: %d' % len(fehler)); sys.exit(1)
print('Prüfungen gerechnet: %d · Kurzbeschreibungen 42 (berichtigt %d) · Merksätze 14 · Arbeitsweisen 8 · Einzelregeln 30' % (n_pruef, ber))
print('OK')
