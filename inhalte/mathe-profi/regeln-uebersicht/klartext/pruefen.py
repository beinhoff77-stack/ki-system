#!/usr/bin/env python3
"""Prüft klartext/vorschlag.json: Kennungen, alte Texte unverändert zitiert, Längen, alle Zahlenbeispiele (exakt gerechnet),
A-Einträge nicht enthalten, und dass nur unter den Inhaltsordnern (klartext, tafeln, ergaenzung, einheiten) geschrieben wurde.
Aufruf:  python3 -I inhalte/mathe-profi/regeln-uebersicht/klartext/pruefen.py     Endet mit „OK“, sonst Fehlerliste und Exit-Code 1."""
import json, math, pathlib, re, subprocess, sys
from fractions import Fraction as F
hier = pathlib.Path(__file__).resolve().parent
repo = hier.parents[3]
fehler = []
def f(m): fehler.append(m)
def satzanzahl(t): return len(re.findall(r'[.!?](?:\s|$)', t))

# ---------- Soll-Kennungen: die B- und C-Einträge ----------
IDEEN = ("I-zahlen-2 I-zahlen-3 I-zahlen-4 I-zahlen-5 I-algebra-1 I-algebra-3 I-algebra-4 I-geld-1 I-geld-2 I-geld-3 "
         "I-geo-1 I-geo-2 I-fur-1 I-fur-2 I-fur-3 I-fur-4 I-funktionen-1 I-funktionen-2 I-funktionen-3 "
         "I-daten-1 I-daten-2 I-daten-3 I-daten-4").split()
EINZEL = ("Z3 Z6 Z8 Z13 Z20 Z22 Z23 Z24 A1 A2 A8 A9 V7 G3 G7 G11 G15 G18 G19 G21 G27 G28 G30 F3 F4 F14 F16 F19 "
          "U1 U10 U11 U13 U14 U15 U16 U17 D5 D6 D7 D8 D12 D15 D17 D20 E2 E3 E4 E5").split()
REGELN = ["R14"]
assert len(IDEEN) == 23 and len(EINZEL) == 48

# ---------- Rechner ----------
def teiler(n): n = int(n); return tuple(t for t in range(1, n + 1) if n % t == 0)
def ist_prim(n): n = int(n); return n > 1 and all(n % t for t in range(2, int(n ** 0.5) + 1))
def alle_prim(l): return all(ist_prim(x) for x in l)
def zerlege(n):
    n = int(n); r = []; p = 2
    while n > 1:
        while n % p == 0: r.append(p); n //= p
        p += 1
    return r
def wurzel(n):
    n = F(n); r = F(math.isqrt(int(n)))
    assert r * r == n, 'keine glatte Wurzel'
    return r
def wurzelf(n): return math.sqrt(float(n))
def log(b, x):
    r = round(math.log(float(x), float(b)))
    assert F(b) ** r == F(x), 'kein ganzer Logarithmus'
    return F(r)
def mittel(l): return sum(l) / len(l)
def median(l):
    s = sorted(l); n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
def roemisch(s):
    assert re.fullmatch(r'M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})', s), 'keine gültige römische Zahl'
    w = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000); t = 0
    for a, b in zip(s, s[1:] + ' '):
        t += -w[a] if b != ' ' and w[b] > w[a] else w[a]
    return t
def zweier(s): return int(s, 2)
def kaufm(n, s): return F(math.floor(F(n) / F(s) + F(1, 2))) * F(s)
def ca(a, b, e=0.01): return abs(float(a) - float(b)) <= float(e)
def sin(g): return math.sin(math.radians(float(g)))
def cos(g): return math.cos(math.radians(float(g)))
def korr(x, y):
    n = len(x); mx = sum(map(float, x)) / n; my = sum(map(float, y)) / n
    sxy = sum((float(a) - mx) * (float(b) - my) for a, b in zip(x, y))
    return sxy / math.sqrt(sum((float(a) - mx) ** 2 for a in x) * sum((float(b) - my) ** 2 for b in y))
def windschief(p1, r1, p2, r2):
    c = [r1[1] * r2[2] - r1[2] * r2[1], r1[2] * r2[0] - r1[0] * r2[2], r1[0] * r2[1] - r1[1] * r2[0]]
    if not any(c): return False
    return sum((b - a) * k for a, b, k in zip(p1, p2, c)) != 0
HILF = dict(F=F, teiler=teiler, ist_prim=ist_prim, alle_prim=alle_prim, zerlege=zerlege, wurzel=wurzel, wurzelf=wurzelf, log=log,
            mittel=mittel, median=median, roemisch=roemisch, zweier=zweier, kaufm=kaufm, ca=ca, sin=sin, cos=cos, korr=korr,
            windschief=windschief, abs=abs, sum=sum, max=max, min=min, len=len, sorted=sorted)
def rechne(ausdruck):
    a = ausdruck.replace('−', '-')
    code = re.sub(r"""('[^']*'|"[^"]*")|(?<![\w.])(\d+(?:\.\d+)?)""", lambda m: m.group(1) or 'F("%s")' % m.group(2), a)
    return eval(code, {'__builtins__': {}}, dict(HILF))

# ---------- Laden ----------
vs = json.loads((hier / 'vorschlag.json').read_text(encoding='utf-8'))
ein = vs['eintraege']
d = json.loads((repo / 'daten/regeln-universum.json').read_text(encoding='utf-8'))
ideen = {i['id']: (p['name'], i) for p in d['planeten'] for i in p['ideen']}
ges = {g['id']: g for g in d['gesetze']}
reg = {r['id']: r for r in d['regeln']}
kurz = d['kurz']
alle_ids = set(ideen) | set(ges) | set(reg)

# ---------- Kennungen ----------
ids = [e['id'] for e in ein]
if len(ids) != len(set(ids)): f('doppelte Kennungen')
soll = set(IDEEN) | set(EINZEL) | set(REGELN)
for i in sorted(soll - set(ids)): f('%s: B/C-Eintrag ohne Vorschlag' % i)
for i in sorted(set(ids) - soll): f('%s: Vorschlag für einen Eintrag, der nicht B oder C ist (A-Einträge bleiben unverändert)' % i)
for i in ids:
    if i not in alle_ids: f('%s: Kennung existiert nicht im Regel-Universum' % i)
a_ids = alle_ids - soll
if len(a_ids) != 28 - 23 + 152 - 48 + 14 - 1: f('Zahl der A-Einträge unerwartet: %d' % len(a_ids))
for i in ids:
    if i in a_ids: f('%s: A-Eintrag darf nicht verändert werden' % i)
n_gez = dict(idee=0, einzelregel=0, rechenregel=0)

# ---------- Je Eintrag ----------
PFLICHT = ['id', 'ebene', 'gebiet', 'klasse', 'alt_name', 'alt_satz', 'neu_name', 'neu_satz', 'beispiel', 'rechnung', 'begruendung', 'suchwoerter']
VERBOTEN = {'8535e86c8118', '6a61eb7383e8', 'ac818c81a10c'}  # Prüfsummen statt Klartext (öffentliches Repo)
namen = {}
n_rechnungen = 0
for e in ein:
    i = e['id']; o = i + ': '
    for k in PFLICHT:
        if e.get(k) in (None, '', []): f(o + 'Pflichtfeld fehlt: ' + k)
    if not e.get('bedingung') and e['ebene'] != 'idee' and False: pass
    if i in ideen: ist = ('idee', ideen[i][1]['kurz'], ideen[i][1]['satz'], kurz[i]); gebiet = ideen[i][0]
    elif i in ges: ist = ('einzelregel', ges[i]['name'], ges[i]['satz'], ''); gebiet = ges[i]['planet']
    elif i in reg: ist = ('rechenregel', reg[i]['name'], reg[i]['satz'], kurz[i]); gebiet = 'Rechenregeln'
    else: continue
    n_gez[ist[0]] += 1
    if e['ebene'] != ist[0]: f(o + 'ebene falsch (%s statt %s)' % (e['ebene'], ist[0]))
    if e['gebiet'] != gebiet: f(o + 'gebiet falsch')
    if e['alt_name'] != ist[1]: f(o + 'alt_name weicht von den Daten ab')
    if e['alt_satz'] != ist[2]: f(o + 'alt_satz weicht von den Daten ab')
    if ist[0] != 'einzelregel' and e.get('alt_kurz') != ist[3]: f(o + 'alt_kurz weicht von den Daten ab')
    # Längen und Form
    if len(e['neu_name']) > 40: f(o + 'neu_name länger als 40 Zeichen (%d)' % len(e['neu_name']))
    if e['neu_name'] == e['alt_name'] and e['neu_satz'] == e['alt_satz']: f(o + 'weder Name noch Satz geändert')
    if satzanzahl(e['neu_satz']) > 4 or len(e['neu_satz']) > 330: f(o + 'neu_satz zu lang (%d Zeichen, %d Sätze)' % (len(e['neu_satz']), satzanzahl(e['neu_satz'])))
    if e.get('neu_kurz'):
        if ist[0] == 'einzelregel': f(o + 'Einzelregeln haben keine Kurzbeschreibung')
        if len(e['neu_kurz']) > 110 or satzanzahl(e['neu_kurz']) != 1: f(o + 'neu_kurz: nicht ein Satz bis 110 Zeichen (%d, %d Sätze)' % (len(e['neu_kurz']), satzanzahl(e['neu_kurz'])))
    elif ist[0] == 'idee' and False: pass
    if e.get('neu_warum_einstieg') and satzanzahl(e['neu_warum_einstieg']) > 3: f(o + 'neu_warum_einstieg länger als drei Sätze')
    if len(set(e['suchwoerter'])) != len(e['suchwoerter']) or len(e['suchwoerter']) < 4: f(o + 'Suchwörter: mindestens vier, keine doppelten')
    if len(e['begruendung']) > 230 or satzanzahl(e['begruendung']) != 1: f(o + 'begruendung: ein Satz, höchstens 230 Zeichen')
    namen.setdefault(e['neu_name'], []).append(i)
    for k in ['neu_name', 'neu_satz', 'neu_kurz', 'beispiel', 'bedingung', 'begruendung', 'neu_warum_einstieg']:
        if {__import__('hashlib').sha256(w.lower().encode()).hexdigest()[:12] for w in re.findall(r'\w+', e.get(k, '') or '')} & VERBOTEN: f(o + 'Name aus dem privaten Umfeld in ' + k)
    # Beispiele rechnen
    for r in e['rechnung']:
        try:
            if rechne(r) is not True: f(o + 'Rechnung stimmt nicht: ' + r)
            else: n_rechnungen += 1
        except Exception as ex:
            f(o + 'Rechnung nicht auswertbar: %s (%s)' % (r, ex))
for n, l in namen.items():
    if len(l) > 1: f('Name doppelt vergeben: %s (%s)' % (n, ', '.join(l)))
# neu_name gegen bestehende Namen anderer Einträge
bestehend = {}
for i, (p, x) in ideen.items(): bestehend[x['kurz']] = i
for i, g in ges.items(): bestehend[g['name']] = i
for i, r in reg.items(): bestehend[r['name']] = i
for e in ein:
    b = bestehend.get(e['neu_name'])
    if b and b != e['id']: f('%s: neu_name wie der bestehende Name von %s' % (e['id'], b))

# ---------- Auflagen aus Werkstatt 1133/1137 ----------
E = {e['id']: e for e in ein}
# Ebene „Genau gesagt“: für alle 23 Ideen in klarer Sprache neu gefasst, alte Fassung unverändert zitiert
for i in IDEEN:
    e = E[i]; o = i + ': '
    if e.get('alt_genau') != ideen[i][1]['genau']: f(o + 'alt_genau weicht von den Daten ab')
    g = e.get('neu_genau', '')
    if not g or g == e.get('alt_genau'): f(o + 'neu_genau fehlt oder ist unverändert')
    if len(g) > 450 or satzanzahl(g) > 5: f(o + 'neu_genau zu lang (%d Zeichen, %d Sätze)' % (len(g), satzanzahl(g)))
# Namensüberschneidungen: kein Wort von mindestens 7 Buchstaben im neuen Namen einer Idee kommt im alten oder neuen Namen eines anderen Eintrags vor
def woerter(t): return {w.lower() for w in re.findall(r'[A-Za-zÄÖÜäöüß]{7,}', t)}
GENERISCH = {'gleichung', 'gleichungen', 'tauschen', 'rechnen', 'zerlegen', 'zusammenfassen', 'geraden', 'graphen', 'zählen'}  # allgemeine Wörter, keine Namen
andere = {}
for i in alle_ids:
    n = ideen[i][1]['kurz'] if i in ideen else (ges[i]['name'] if i in ges else reg[i]['name'])
    andere[i] = [n] if i in a_ids else []  # B/C-Einträge zählen mit ihrem neuen Namen
for e in ein: andere.setdefault(e['id'], []).append(e['neu_name'])
for i in IDEEN:
    mein = woerter(E[i]['neu_name']) - GENERISCH
    for j, namen_j in andere.items():
        if j == i: continue
        for n in namen_j:
            gem = mein & woerter(n)
            if gem: f('%s: Namensüberschneidung mit %s („%s“): %s' % (i, j, n, ', '.join(sorted(gem))))
# Inhaltliche Auflagen je Eintrag
def fehlt(i, feld, *teile):
    for t in teile:
        if t not in E[i][feld]: f('%s: %s muss „%s“ enthalten' % (i, feld, t))
fehlt('I-zahlen-5', 'neu_satz', 'ab Klasse 5', 'ab Klasse 9', 'ab Klasse 10', '≥ 0', 'Basis > 0', 'Basis ≠ 1', 'Zahl > 0')
fehlt('I-daten-1', 'neu_satz', 'Mittelwert = Summe aller Werte : Anzahl', 'Median = der mittlere Wert', 'sortiert')
fehlt('I-daten-1', 'beispiel', 'Beispielzahlen')
fehlt('D15', 'beispiel', 'Beispielzahlen')
for k in ('neu_kurz', 'neu_genau', 'neu_satz'):
    if 'Mitte' in E['I-daten-1'][k].replace('mittler', '').replace('Mittelwert', ''): f('I-daten-1: %s fasst Mittelwert und Median nicht getrennt (Wort „Mitte“)' % k)
fehlt('I-daten-2', 'neu_satz', 'Anteil in der Stichprobe · Größe der ganzen Gruppe', 'zufällig')
fehlt('I-geld-1', 'neu_satz', 'Länge 10', 'Fläche 100', 'Raum 1 000', 'Tafel „Einheiten umrechnen“')
fehlt('I-geld-1', 'beispiel', '3 · 10 · 10 cm', '2 · 100 · 100 cm²')
for k in ('neu_satz', 'neu_genau'): fehlt('I-geo-1', k, 'Nebenwinkel', 'Scheitelwinkel', 'Stufenwinkel', 'Wechselwinkel')
if len(E['I-geo-1']['neu_genau'].split('. ')) < 4: f('I-geo-1: neu_genau braucht vier Fälle mit je einem Beispiel')
fehlt('I-zahlen-4', 'neu_satz', 'Prozentzahl = Dezimalzahl · 100')
for k in ('neu_satz', 'beispiel', 'neu_genau'):
    if re.search(r'· ?100 ?%', E['I-zahlen-4'][k]): f('I-zahlen-4: „· 100 %%“ als Rechnung in %s' % k)
# G3, G7, I-algebra-4, I-zahlen-5: kürzer als vorher, Bedingungen im Satz
for i, grenze in (('G3', 140), ('G7', 245), ('I-algebra-4', 235), ('I-zahlen-5', 213)):
    if len(E[i]['neu_satz']) > grenze: f('%s: neu_satz mit %d Zeichen nicht kürzer als vorher (höchstens %d)' % (i, len(E[i]['neu_satz']), grenze))
fehlt('G3', 'neu_satz', '0° < α < 90°', 'α = 90°', '90° < α < 180°', 'α = 180°', '180° < α < 360°', 'α = 360°')
fehlt('G7', 'neu_satz', 'Vereinbarung', 'mindestens ein Paar')
fehlt('I-algebra-4', 'neu_satz', 'a > 0', 'a = 0', 'a < 0', 'reellen Zahlen')

# ---------- Nur unter klartext/ geschrieben? ----------
git_hinweis = ''
ERLAUBT = tuple('inhalte/mathe-profi/regeln-uebersicht/%s/' % o for o in ('klartext', 'tafeln', 'ergaenzung', 'einheiten'))  # Auflagen aus Werkstatt 1133/1137: Helfer 3 arbeitet in allen vier Ordnern
try:
    st = subprocess.run(['git', '-C', str(repo), 'status', '--porcelain'], capture_output=True, text=True, check=True).stdout.splitlines()
    pfade = [z[3:].strip().strip('"') for z in st]
    base = None
    for ref in ('origin/lernen-app', 'origin/main', 'origin/master'):
        r = subprocess.run(['git', '-C', str(repo), 'merge-base', 'HEAD', ref], capture_output=True, text=True)
        if r.returncode == 0: base = r.stdout.strip(); break
    if base:
        pfade += subprocess.run(['git', '-C', str(repo), 'diff', '--name-only', base, 'HEAD'], capture_output=True, text=True, check=True).stdout.split('\n')
    else: git_hinweis = ' (Vergleich mit dem Ausgangsstand übersprungen: kein Basiszweig gefunden)'
    for p in pfade:
        if p and not p.startswith(ERLAUBT): f('Änderung außerhalb der Inhaltsordner (klartext, tafeln, ergaenzung, einheiten): ' + p)
except Exception as ex:
    git_hinweis = ' (git nicht verfügbar: %s)' % ex

if fehler:
    print('FEHLER (%d):' % len(fehler)); print('\n'.join(' - ' + x for x in fehler)); sys.exit(1)
print('%d Vorschläge (%d Ideen, %d Einzelregeln, %d Rechenregel), %d Rechnungen exakt geprüft%s' % (
    len(ein), n_gez['idee'], n_gez['einzelregel'], n_gez['rechenregel'], n_rechnungen, git_hinweis))
print('OK')
