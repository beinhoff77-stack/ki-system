#!/usr/bin/env python3
"""Prüft einzelregeln-neu.json: Pflichtfelder und Längen, Schreibweise, Kennungen (keine Kollision mit dem Bestand),
Verweise auf Ideen, Einzelregeln, Lernkarten und Klassen im Repo, und rechnet jedes Zahlenbeispiel nach
(exakt mit Brüchen; Winkelfunktionen und π nur auf Rundungsstellen).
Aufruf:  python3 -I inhalte/mathe-profi/regeln-uebersicht/ergaenzung/pruefen.py
Endet mit „OK“, sonst mit Fehlerliste und Exit-Code 1."""
import json, math, pathlib, re, sys
from fractions import Fraction as F
hier = pathlib.Path(__file__).resolve().parent
repo = hier.parents[3]
fehler, warn = [], []
def f(m): fehler.append(m)
def laden(p): return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))

# ---------- Rechner ----------
def roemisch(s):
    w = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}; t = 0
    for i, ch in enumerate(s):
        v = w[ch]; t += -v if i + 1 < len(s) and w[s[i + 1]] > v else v
    return F(t)
def zahl_roem(n):
    n = int(n); out = ''
    for v, z in ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v: out += z; n -= v
    return out
def dual(n): return F(int(str(int(n)), 2))
def rund(x, n): return F(str(round(float(x), int(n))))
def sin_d(x): return math.sin(math.radians(float(x)))
def cos_d(x): return math.cos(math.radians(float(x)))
def tan_d(x): return math.tan(math.radians(float(x)))
HILF = {'F': F, 'abs': abs, 'roemisch': roemisch, 'zahl_roem': zahl_roem, 'dual': dual, 'rund': rund, 'sin_d': sin_d, 'cos_d': cos_d, 'tan_d': tan_d, 'pi': math.pi}
def wert(ausdruck, mit):
    code = re.sub(r'(?<![\w.])(\d+(?:\.\d+)?)', r'F("\1")', ausdruck.replace('−', '-'))
    return eval(code, {'__builtins__': {}}, {**HILF, **{k: F(str(v)) for k, v in mit.items()}})
OPS = {'==': lambda a, b: a == b, '!=': lambda a, b: a != b, '<': lambda a, b: a < b, '>': lambda a, b: a > b, '<=': lambda a, b: a <= b, '>=': lambda a, b: a >= b}
n_pruef = 0
def pruefe(liste, ort):
    global n_pruef
    if len(liste) < 3: f('%s: weniger als 3 Rechenproben' % ort)
    for p in liste:
        n_pruef += 1
        for k in p:
            if k not in ('l', 'rel', 'r', 'mit', 'falsch', 'fuer'): f('%s: unbekanntes Feld %s' % (ort, k))
        belegungen = [p.get('mit', {})]
        if 'fuer' in p:
            (name, werte), = p['fuer'].items(); belegungen = [{**p.get('mit', {}), name: w} for w in werte]
        for b in belegungen:
            try:
                ok = OPS[p['rel']](wert(p['l'], b), wert(p['r'], b))
            except Exception as e:
                f('%s: Ausdruck nicht rechenbar %r (%s)' % (ort, p, e)); break
            if p.get('falsch'): ok = not ok
            if not ok: f('%s: stimmt nicht: %s %s' % (ort, json.dumps(p, ensure_ascii=False), b)); break

# ---------- Bestand ----------
uni = laden(repo / 'daten/regeln-universum.json')
ids = {g['id']: g for g in uni['gesetze']}
ids.update({r['id']: r for r in uni['regeln']})
ideen = {i['id']: p['name'] for p in uni['planeten'] for i in p['ideen']}
aw = {a['name'] for a in uni['arbeitsweisen']}
AW_KENNUNGEN = {a['kennung_vorschlag'] for a in laden(repo / 'inhalte/mathe-profi/regeln-uebersicht/texte8/arbeitsweisen.json')['arbeitsweisen']}  # feste Kennungen der Arbeitsweisen
THEMEN = repo / 'inhalte/themen'
_th = {}
def thema(t):
    if t not in _th:
        p = THEMEN / (t + '.json'); _th[t] = laden(p) if p.exists() else None
    return _th[t]
def lernkarte_da(t, l):
    d = thema(t)
    return bool(d) and any(e['lernziel'] == l for e in d['inhalt']['etappen'])

D = laden(hier / 'einzelregeln-neu.json')
R, V = D['regeln'], D['verweise']
BUCH = {'Zahlen': 'Z', 'Algebra': 'A', 'Geld und Verhältnisse': 'V', 'Geometrie': 'G', 'Fläche und Raum': 'F', 'Funktionen': 'U', 'Daten und Zufall': 'D'}
GRENZE = {'name': (3, 60), 'satz': (40, 420), 'beispiel': (15, 420), 'voraus': (15, 520), 'fehler': (15, 340), 'bezug_bestand': (10, 400)}
PFLICHT = ['kennung', 'name', 'satz', 'beispiel', 'voraus', 'fehler', 'gym', 'rs', 'gebiet', 'gehoert_zu', 'status', 'ergaenzt', 'bezug_bestand', 'stichwoerter', 'verwandt', 'lernkarten', 'pruefung']
VERBOTEN = {'8535e86c8118', '6a61eb7383e8', 'ac818c81a10c'}  # Prüfsummen statt Klartext (öffentliches Repo)

def klasse_start(a):
    m = re.fullmatch(r'(\d+)(?:–(\d+))?', a); return int(m.group(1)) if m else None

def text_pruefen(t, ort):
    if re.search(r'\d\.\d', t): f('%s: Dezimalpunkt statt Komma: %r' % (ort, t))
    if '*' in t: f('%s: Stern statt Malpunkt' % ort)
    if '&#' in t or '<' in t.replace('<br', '') and False: f('%s: Markup' % ort)
    if {__import__('hashlib').sha256(w.lower().encode()).hexdigest()[:12] for w in re.findall(r'\w+', t)} & VERBOTEN: f('%s: Name oder Familienbezug im Text' % ort)
    if re.search(r'\d,\s*\d{3}\b(?! ?(?:cm|m|km|€|%))', t) is None and False: pass
    if '  ' in t: f('%s: doppeltes Leerzeichen' % ort)

# Einheiten: gleiche Größenart links und rechts von „=“
DIM = {}
for d_, us in {'L': 'km m dm cm mm', 'A': 'km² ha a m² dm² cm² mm²', 'V': 'm³ dm³ cm³ mm³ l ml', 'M': 't kg g mg', 'T': 'd h min s', 'E': '€ ct'}.items():
    for u in us.split(): DIM[u] = d_
def einheiten(s):
    return {DIM[u] for u in re.findall(r'\d[\d ,]*\s(km²|ha|a|m²|dm²|cm²|mm²|km|dm|cm|mm|m³|dm³|cm³|mm³|kg|mg|min|ml|ct|€|m|l|t|g|h|s|d)(?![\w²³/])', s) if u in DIM}
def gleichung_dim(t, ort):
    for teil in re.split(r'(?<=[a-zäöüß²³)\d])[.;:,] |\. | denn | also | und ', t):
        seiten = teil.split(' = ')
        if len(seiten) < 2: continue
        ds = [einheiten(s) for s in seiten]
        belegt = [d for d in ds if d]
        if len(belegt) >= 2 and any(d != belegt[0] for d in belegt): f('%s: Größenarten links/rechts verschieden: %r' % (ort, teil))

kenn, namen = set(), set()
zaehler = {}
alle_n = {r.get('kennung') for r in R}
for r in R:
    o = r.get('kennung', '?')
    for k in PFLICHT:
        if k not in r or r[k] in (None, '') or (k not in ('ergaenzt', 'lernkarten', 'verwandt') and r[k] == []): f('%s: Pflichtfeld fehlt: %s' % (o, k))
    if set(r) - set(PFLICHT): f('%s: unbekannte Felder %s' % (o, sorted(set(r) - set(PFLICHT))))
    if not re.fullmatch(r'N-[ZAVGFUD]\d\d', o): f('%s: Kennung nicht N-<Gebiet><nn>' % o)
    if o in kenn or o in ids: f('%s: Kennung doppelt oder im Bestand' % o)
    kenn.add(o)
    if r.get('name') in namen: f('%s: Name doppelt' % o)
    namen.add(r.get('name'))
    for k, (a, b) in GRENZE.items():
        if k in r and not a <= len(r[k]) <= b: f('%s: %s hat %d Zeichen (erlaubt %d bis %d)' % (o, k, len(r[k]), a, b))
    for k in ('name', 'satz', 'beispiel', 'voraus', 'fehler', 'bezug_bestand'): text_pruefen(r.get(k, ''), '%s %s' % (o, k))
    if not r.get('satz', '.').endswith(('.', ')')): f('%s: satz endet nicht mit Punkt' % o)
    for k in ('beispiel', 'fehler'): gleichung_dim(r.get(k, ''), '%s %s' % (o, k))
    # Gebiet und Idee
    g = r.get('gehoert_zu', {})
    if g.get('gebiet') != r.get('gebiet'): f('%s: gebiet und gehoert_zu.gebiet verschieden' % o)
    if BUCH.get(r.get('gebiet')) != o[2:3]: f('%s: Buchstabe passt nicht zum Gebiet %s' % (o, r.get('gebiet')))
    if g.get('idee') not in ideen: f('%s: Idee %s gibt es nicht' % (o, g.get('idee')))
    elif ideen[g['idee']] != r.get('gebiet'): f('%s: Idee %s gehört zum Gebiet %s, nicht %s' % (o, g['idee'], ideen[g['idee']], r.get('gebiet')))
    if len(g.get('begruendung', '')) < 20: f('%s: gehoert_zu.begruendung fehlt oder zu kurz' % o)
    # Status
    if r.get('status') not in ('neu', 'ausarbeitung'): f('%s: status unbekannt' % o)
    if r.get('status') == 'ausarbeitung' and not r.get('ergaenzt'): f('%s: ausarbeitung ohne ergaenzt' % o)
    if r.get('status') == 'neu' and r.get('ergaenzt'): f('%s: neu, aber ergaenzt gesetzt' % o)
    for e in r.get('ergaenzt', []):
        if e not in ids: f('%s: ergaenzt %s gibt es nicht' % (o, e))
    for v in r.get('verwandt', []):
        if v not in ids and v not in ideen and v not in alle_n: f('%s: verwandt %s gibt es nicht' % (o, v))
    # Klassen und Lernkarten
    gym = r.get('gym', ''); gs = klasse_start(gym)
    if gs is None: f('%s: gym %r hat falsche Form' % (o, gym))
    seen = set(); gyms, rss = [], []
    for l in r.get('lernkarten', []):
        key = (l.get('thema'), l.get('lernkarte'))
        if key in seen: f('%s: Lernkarte doppelt %s' % (o, key))
        seen.add(key)
        if not lernkarte_da(*key): f('%s: Lernkarte %s/%s gibt es nicht' % (o, *key)); continue
        k = thema(key[0])['klasse']; gyms.append(k.get('gym_by')); rss.append(k.get('rs_by'))
    gyms = [x for x in gyms if x]; rss = [x for x in rss if x]
    if gyms and gs != min(gyms): f('%s: gym %s, aber kleinste Klasse der Lernkarten ist %s' % (o, gym, min(gyms)))
    if r.get('rs') != (str(min(rss)) if rss else '–'): f('%s: rs %s, aus den Lernkarten %s' % (o, r.get('rs'), min(rss) if rss else '–'))
    if not r.get('lernkarten'): warn.append('%s: keine Lernkarte im Bestand (siehe bezug_bestand)' % o)
    if not r.get('stichwoerter') or any(not isinstance(x, str) or not x.strip() for x in r.get('stichwoerter', [])): f('%s: stichwoerter fehlen' % o)
    pruefe(r.get('pruefung', []), o)
    zaehler[gs] = zaehler.get(gs, 0) + 1
    r_gesamt = r  # noqa

# ---------- Verweise ----------
vk = set()
for v in V:
    o = v.get('kennung', '?')
    for k in ('kennung', 'was', 'ziel', 'begruendung', 'stichwoerter', 'lernkarten'):
        if not v.get(k): f('%s: Pflichtfeld fehlt: %s' % (o, k))
    if o in vk: f('%s: doppelt' % o)
    vk.add(o)
    z = v.get('ziel', '')
    if z in ids: pass
    elif z in AW_KENNUNGEN: pass
    elif z.startswith('Arbeitsweise '):
        if z[len('Arbeitsweise '):] not in aw and not any(a.startswith(z[len('Arbeitsweise '):]) for a in aw): f('%s: Arbeitsweise %s gibt es nicht' % (o, z))
    elif z == 'T-einheiten':
        if not (hier.parent / 'einheiten' / 'einheiten.json').exists(): f('%s: einheiten/einheiten.json fehlt' % o)
    else: f('%s: Ziel %s gibt es nicht' % (o, z))
    for l in v.get('lernkarten', []):
        if not lernkarte_da(l['thema'], l['lernkarte']): f('%s: Lernkarte %s/%s gibt es nicht' % (o, l['thema'], l['lernkarte']))
    for k in ('was', 'begruendung', 'vorschlag'): text_pruefen(v.get(k, ''), '%s %s' % (o, k))

# ---------- Zählung gegen die Übersicht ----------
md = (hier / 'uebersicht.md').read_text(encoding='utf-8')
for r in R:
    if '`%s`' % r['kennung'] not in md: f('uebersicht.md nennt %s nicht' % r['kennung'])
for v in V:
    if '`%s`' % v['kennung'] not in md: f('uebersicht.md nennt %s nicht' % v['kennung'])
neu = sum(1 for r in R if r['status'] == 'neu'); aus = len(R) - neu
m = re.search(r'\*\*(\d+) Regeln\*\* \((\d+) neu, (\d+) Ausarbeitung[^)]*\), \*\*(\d+) Verweise', md)
if not m or tuple(map(int, m.groups())) != (len(R), neu, aus, len(V)): f('uebersicht.md: Zählzeile stimmt nicht (%s)' % (m.groups() if m else 'fehlt'))

# ---------- Auflagen aus Werkstatt 1133/1137 ----------
RR = {r['kennung']: r for r in R}
def muss(k, feld, *teile):
    for t in teile:
        if t not in RR[k][feld]: f('%s: %s muss „%s“ enthalten' % (k, feld, t))
muss('N-G14', 'satz', 'Bereich 0° bis 360°', 'plus 360°', 'minus 360°', 'der Größe nach')
muss('N-G14', 'beispiel', '−45°', '315°', '135°')
if (-45 + 360, (-45 + 360 + 180) % 360) != (315, 135): f('N-G14: tan-Beispiel rechnet nicht')
muss('N-D02', 'satz', 'Zählregel'); muss('N-D02', 'voraus', 'keine Wahrscheinlichkeiten', 'Pfadregel', 'D19')
if 'D19' not in RR['N-D02']['verwandt']: f('N-D02: Verweis auf die Pfadregel D19 fehlt in verwandt')
muss('N-F09', 'satz', 'Aufgabe oder Zeichnung'); muss('N-F09', 'voraus', 'vorn', 'oben')
muss('N-Z05', 'satz', 'ℕ hier mit 0'); muss('N-Z05', 'voraus', 'ℕ zählt hier die 0 mit')
for k in ('N-U06', 'N-U07', 'N-A03'):
    muss(k, 'voraus', 'Die Grundmenge steht in der Aufgabe (oft ℚ, ab Klasse 9 ℝ)')
if 'W = ℚ \\ {c}' in RR['N-U07']['satz'] and 'hängt von D ab' not in RR['N-U07']['satz']: f('N-U07: Wertemenge ohne Abhängigkeit von D')
muss('N-U07', 'satz', 'hängt von D ab', 'ℝ \\ {c}')
if 'D = ℚ \\ {2; −4}' in RR['N-A03']['beispiel'] and 'Grundmenge ℚ' not in RR['N-A03']['beispiel']: f('N-A03: Beispiel nennt die Grundmenge nicht')
muss('N-F08', 'satz', 'üblicherweise', 'kann andere Werte vorgeben'); muss('N-F08', 'voraus', 'übliche Vereinbarung', 'abweichen')
muss('N-V01', 'voraus', '2,040 km = 2,04 km', 'Null am Ende', 'ändert den Wert nicht')
# Auflagen aus Werkstatt 1138/1139
muss('N-Z07', 'satz', 'ganzen Zehnerteil der Stellensumme'); muss('N-Z07', 'beispiel', 'Drei Summanden')
if 58 + 69 + 37 != 164 or 8 + 9 + 7 != 24 or 5 + 6 + 3 + 2 != 16: f('N-Z07: Dreier-Beispiel rechnet nicht')
muss('N-Z12', 'voraus', 'a ≠ 0')
if '495' in RR['N-G14']['beispiel'] or '495' in RR['N-G14']['satz']: f('N-G14: Zwischenwert über 360° im Text')
muss('N-G14', 'satz', 'Bring auch x₂ in den Bereich', 'der Größe nach')
muss('N-G08', 'voraus', 'd ist größer als 0', 'd = 0')
muss('N-D03', 'voraus', 'höchstens n')
muss('N-U03', 'satz', 'positivem Nenner', 'negativ')
muss('N-U01', 'satz', 'Grundmenge der Aufgabe'); muss('N-U01', 'voraus', 'oft ℚ, ab Klasse 9 ℝ', 'hängt von D ab')
muss('N-G03', 'satz', '0,5°', '6°'); muss('N-G03', 'beispiel', '3:30', '75°')
if 3 * 30 + 30 * F(1, 2) != 105 or 30 * 6 - 105 != 75: f('N-G03: 3:30 rechnet nicht')
va = {v['kennung']: v for v in V}
if va['V-01']['ziel'] != 'aw.ueberschlag' or va['V-21']['ziel'] != 'aw.skizze': f('V-01/V-21: Ziel muss die feste Kennung der Arbeitsweise sein')
if 'T-einheiten' in va['V-14']['ziel'] and not va['V-14'].get('ziel_offen'): f('V-14: Abhängigkeit von der Einheiten-Tafel nicht als offen vermerkt')
# Auflagen aus Werkstatt 1143
muss('N-U07', 'voraus', 'a, b und c gehören zur Grundmenge', 'ℚ bzw. ℝ')
if RR['N-U07']['voraus'].index('gehören zur Grundmenge') > RR['N-U07']['voraus'].index('W = ℚ'): f('N-U07: Voraussetzung muss vor der Wertemenge stehen')
if 'kürzen' in [w.lower() for w in va['V-06']['stichwoerter']]: f('V-06: „kürzen“ gehört zu R9 (Doppelbelegung)')
for k in ('V-01', 'V-21'):
    if 'beim Einbau vergeben' not in va[k].get('ziel_hinweis', ''): f('%s: Kennung „wird beim Einbau vergeben“ nicht vermerkt' % k)
if 'Offen bis zum Einbau' not in va['V-14'].get('ziel_offen', ''): f('V-14: „offen bis zum Einbau“ fehlt')
# Verweise-Abgleich: Datei vorhanden, nennt alle Verweise und jedes Ziel, das im Universum fehlt
ab = (hier / 'verweise-abgleich.md').read_text(encoding='utf-8')
bestand = set(ids) | {'Arbeitsweise ' + a for a in aw} | AW_KENNUNGEN
for v in V:
    if '`%s`' % v['kennung'] not in ab: f('verweise-abgleich.md nennt %s nicht' % v['kennung'])
    if v['ziel'] not in bestand and ('`%s`' % v['ziel'] not in ab or 'fehlt im Bestand' not in ab): f('verweise-abgleich.md benennt das fehlende Ziel %s nicht' % v['ziel'])
sw_alt = {s['wort'].lower(): s['ziel'] for s in uni['stichwoerter']}
for v in V:
    for w in v['stichwoerter']:
        if w.lower() in sw_alt and sw_alt[w.lower()] != v['ziel'] and w not in ab: f('verweise-abgleich.md nennt den Konflikt um „%s“ nicht' % w)

for w in warn: print('Hinweis:', w)
if fehler:
    print('\n'.join(fehler)); print('FEHLER: %d' % len(fehler)); sys.exit(1)
print('Regeln %d (neu %d, Ausarbeitung %d) · je Klasse %s · Verweise %d · Rechenproben %d' % (len(R), neu, aus, ', '.join('%s: %d' % (k, zaehler[k]) for k in sorted(zaehler)), len(V), n_pruef))
print('OK')
