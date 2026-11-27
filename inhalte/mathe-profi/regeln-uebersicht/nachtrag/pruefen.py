#!/usr/bin/env python3
"""Prüft den Nachtrag unter inhalte/mathe-profi/regeln-uebersicht/nachtrag/:
  nachtrag.json          zwölf neue Einträge (Dreisatz, Strahlensätze, Geschwindigkeit, Dichte, Pyramide, Kreisring, Kongruenzsätze)
  klassen-nachtrag.json  Klassen für Einträge ohne Klasse, Berichtigung zu V1
  kurzformen.md          Befund zu den sieben Kurzformen im Bau (tools/tafeln_bauen.cjs, nur gelesen)
  uebersicht.md          Stand: ergänzt / offen

Es wird nachgerechnet, nicht abgeschrieben:
  - jede Rechenprobe (l, rel, r) exakt mit Brüchen (π und Winkelfunktionen nur auf Rundungsstellen),
  - jede Gleichung der Form „Zahl · Zahl = Zahl“ im Text (mit Einheitenprüfung nur dort, wo links und rechts dieselbe Einheit steht),
  - Skizzen: Strahlensatz-Figuren exakt (Parallelität, Abschnitte), Kongruenz-Skizzen aus Koordinaten (Seiten, Winkel, Lage des Winkels),
  - Pflichtfelder, eindeutige Kennungen, keine Kollision mit bestehenden Kennungen (Tafeln, Einzelregeln, Universum),
  - Verweise (Regeln, Klassen, Belege) gegen daten/regeln-universum.json und inhalte/themen/*.json,
  - Klassen-Nachtrag (nur dort ergänzt, wo die Tafel keine Klasse hat; frühestes Vorkommen im Bestand) und die Berichtigung zu V1,
  - die Parallelogramm-Benennung in den Tafeln (g = Grundseite, a und b = Seiten),
  - die Kurzformen-Tabelle gegen die Liste SONST im Bau.
Am Ende laufen acht Negativprüfungen: Dieselbe Prüfung wird auf absichtlich verdorbene Kopien der Daten angewendet und muss jeweils anschlagen.

Aufruf:  python3 -I inhalte/mathe-profi/regeln-uebersicht/nachtrag/pruefen.py
Endet mit „OK“, sonst mit Fehlerliste und Exit-Code 1."""
import ast, copy, json, math, pathlib, re, sys
from fractions import Fraction as F

hier = pathlib.Path(__file__).resolve().parent
uebersicht = hier.parent
repo = hier.parents[3]
Z = {}
def zaehle(k, n=1): Z[k] = Z.get(k, 0) + n

# ============================================================ Rechner
PI = F('3.14159265358979323846264338327950288419716939937510582097494')
def rund(x, n):
    q = x * F(10) ** int(n)
    return F(math.floor(q + F(1, 2))) / F(10) ** int(n)
def _fl(x): return F(repr(x))
FUNK = {
    'rund': rund,
    'wurzel': lambda x: (lambda w: F(round(w)) if F(round(w)) ** 2 == x else _fl(w))(math.sqrt(x)),
    'sin_d': lambda x: _fl(math.sin(math.radians(float(x)))),
    'cos_d': lambda x: _fl(math.cos(math.radians(float(x)))),
    'asin_d': lambda x: _fl(math.degrees(math.asin(float(x)))),
    'abs': abs,
}
def ev(node):
    if isinstance(node, ast.Expression): return ev(node.body)
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool): return F(int(node.value))
        if isinstance(node.value, (int, float)): return F(repr(node.value))
        raise ValueError('Konstante %r' % (node.value,))
    if isinstance(node, ast.Name):
        if node.id == 'pi': return PI
        raise ValueError('Name %s' % node.id)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub): return -ev(node.operand)
    if isinstance(node, ast.BinOp):
        a, b = ev(node.left), ev(node.right)
        if isinstance(node.op, ast.Add): return a + b
        if isinstance(node.op, ast.Sub): return a - b
        if isinstance(node.op, ast.Mult): return a * b
        if isinstance(node.op, ast.Div): return a / b
        if isinstance(node.op, ast.Mod): return a % b
        if isinstance(node.op, ast.Pow):
            if b.denominator != 1: raise ValueError('Exponent')
            return a ** int(b)
        raise ValueError('Operator')
    if isinstance(node, ast.Compare):
        links = ev(node.left); ok = True
        for op, rechts in zip(node.ops, node.comparators):
            r = ev(rechts)
            ok = ok and {ast.Lt: links < r, ast.Gt: links > r, ast.LtE: links <= r, ast.GtE: links >= r, ast.Eq: links == r, ast.NotEq: links != r}[type(op)]
            links = r
        return F(int(ok))
    if isinstance(node, ast.BoolOp):
        w = [ev(v) != 0 for v in node.values]
        return F(int(all(w) if isinstance(node.op, ast.And) else any(w)))
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in FUNK:
        return F(FUNK[node.func.id](*[ev(a) for a in node.args]))
    raise ValueError('nicht erlaubt: %s' % type(node).__name__)
def rechne(s): return ev(ast.parse(s.replace('−', '-'), mode='eval'))
RELS = {'==': lambda a, b: a == b, '!=': lambda a, b: a != b, '<': lambda a, b: a < b, '>': lambda a, b: a > b, '<=': lambda a, b: a <= b, '>=': lambda a, b: a >= b}
def proben(liste, ort, fehler, mind=1):
    if not isinstance(liste, list) or len(liste) < mind: fehler.append('%s: weniger als %d Rechenproben' % (ort, mind)); return
    for p in liste:
        try:
            if set(p) != {'l', 'rel', 'r'} or p['rel'] not in RELS: fehler.append('%s: Rechenprobe falsch aufgebaut: %r' % (ort, p)); continue
            a, b = rechne(str(p['l'])), rechne(str(p['r']))
            if not RELS[p['rel']](a, b): fehler.append('%s: Rechenprobe falsch: %s %s %s (links %s, rechts %s)' % (ort, p['l'], p['rel'], p['r'], float(a), float(b)))
            zaehle('rechenproben')
        except (ValueError, SyntaxError, ZeroDivisionError, TypeError) as e:
            fehler.append('%s: Rechenprobe nicht auswertbar %r: %s' % (ort, p, e))

# ============================================================ Gleichungen im Text
NUM = r'\d{1,3}(?: \d{3})+(?:,\d+)?|\d+(?:,\d+)?'
UNIT = r'km/h|m/s|g/cm³|kg/m³|km|cm|dm|mm|kg|mg|g|min|h|m|€|ct|°'
OPND = r'(?:%s)[²³]?(?: ?(?:%s)[²³]?)?' % (NUM, UNIT)
KETTE = re.compile(r'(?<![\w,.])(%s(?:\s*[+−·:]\s*%s)*(?:\s*=\s*%s(?:\s*[+−·:]\s*%s)*)+)(?![\w,²³]|\.\d)' % (OPND, OPND, OPND, OPND))
def kette_pruefen(text, ort, fehler):
    """Findet Ketten wie „6 cm · 4 cm = 24 cm²“ und rechnet sie nach. Übersprungen wird, wenn davor oder danach ein Rechenzeichen, π oder
    eine Klammer steht, und wenn links und rechts verschiedene Einheiten stehen (Umrechnung, km/h usw.; dafür gibt es Rechenproben)."""
    for m in KETTE.finditer(text):
        s = m.group(1)
        vor = text[:m.start()].rstrip()[-1:]; nach = text[m.end():].lstrip()[:1]
        if vor in ('+', '−', '·', ':', '(', 'π', '√') or nach in ('+', '−', '·', ':', ')', 'π', '(', '√', '/'): zaehle('ketten-uebersprungen'); continue
        seiten = [x.strip() for x in s.split('=')]
        einh = [set(re.findall(r'(?<![\d,])(%s)[²³]?' % UNIT, x)) for x in seiten]
        if any(e != einh[0] for e in einh) or any('/' in u for e in einh for u in e): zaehle('ketten-uebersprungen'); continue
        try:
            werte = []
            for x in seiten:
                y = re.sub(r'(?<=[\d²³])\s?(?:%s)[²³]?(?![\w])' % UNIT, '', x)
                y = re.sub(r'(\d) (\d{3})', r'\1\2', y).replace(',', '.').replace('·', '*').replace(':', '/').replace('−', '-').replace('²', '**2').replace('³', '**3')
                werte.append(rechne(y))
            if any(w != werte[0] for w in werte): fehler.append('%s: Rechnung falsch: „%s“ (%s)' % (ort, s, ' | '.join(str(float(w)) for w in werte)))
            zaehle('ketten-gerechnet')
        except (ValueError, SyntaxError, ZeroDivisionError, TypeError):
            zaehle('ketten-uebersprungen')

# ============================================================ Bestand laden
def laden(p): return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
univ = laden(repo / 'daten/regeln-universum.json')
ids = {}
for r in univ['regeln']: ids[r['id']] = r['name']
for g in univ['gesetze']: ids[g['id']] = g['name']
for p in univ['planeten']:
    for i in p['ideen']: ids[i['id']] = i['kurz']
gesetze = {g['id']: g for g in univ['gesetze']}
bestand_kennungen = set(ids)
bestand_titel = set()
tafeln = {}
for p in sorted((uebersicht / 'tafeln').glob('*/*.json')):
    d = laden(p); tafeln[p.parent.name] = d
    for e in d['eintraege']: bestand_kennungen.add(e['kennung']); bestand_titel.add(e['titel'].lower())
for r in laden(uebersicht / 'ergaenzung/einzelregeln-neu.json')['regeln']: bestand_kennungen.add(r['kennung'])
themen = {}
def thema(t):
    if t not in themen:
        p = repo / 'inhalte/themen' / (t + '.json')
        themen[t] = laden(p) if p.exists() else None
    return themen[t]
alle_themen = sorted(p.stem for p in (repo / 'inhalte/themen').glob('*.json'))

def blaetter(x, pfad='', skip=()):
    if isinstance(x, str): yield pfad, x
    elif isinstance(x, list):
        for i, y in enumerate(x): yield from blaetter(y, '%s[%d]' % (pfad, i), skip)
    elif isinstance(x, dict):
        for k, y in x.items():
            if k in skip: continue
            yield from blaetter(y, pfad + '/' + k, skip)

# ============================================================ Geometrie
def dist(p, q): return math.hypot(p[0] - q[0], p[1] - q[1])
def winkel(a, s, b):
    v1 = (a[0] - s[0], a[1] - s[1]); v2 = (b[0] - s[0], b[1] - s[1])
    return math.degrees(math.acos(max(-1, min(1, (v1[0] * v2[0] + v1[1] * v2[1]) / (math.hypot(*v1) * math.hypot(*v2))))))
def loesungen(p, q, Q):
    """Dreieck mit den Seiten p (gesuchter Gegenwinkel P) und q und dem Winkel Q (gegenüber q): Anzahl der Dreiecke."""
    s = p * math.sin(math.radians(Q)) / q
    if s > 1 + 1e-12: return 0
    P1 = math.degrees(math.asin(min(1, s))); n = 0
    for P in {round(P1, 9), round(180 - P1, 9)}:
        if P + Q < 180 - 1e-9: n += 1
    return n
def zahl(t): return float(t.replace(' ', '').replace(',', '.'))
def strahl_pruefen(e, ort, fehler):
    sk = e.get('skizze') or {}
    try: pt = {k: (F(repr(v[0])), F(repr(v[1]))) for k, v in sk['punkte'].items()}
    except Exception: fehler.append('%s: Skizze ohne Punkte' % ort); return
    if set(pt) != {'S', 'A', "A'", 'B', "B'"}: fehler.append('%s: Skizze braucht S, A, A\', B, B\'' % ort); return
    def kreuz(p, q, r): return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    def d2(p, q): return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
    if kreuz(pt['S'], pt['A'], pt["A'"]) != 0: fehler.append('%s: Skizze: S, A, A\' liegen nicht auf einer Geraden' % ort)
    if kreuz(pt['S'], pt['B'], pt["B'"]) != 0: fehler.append('%s: Skizze: S, B, B\' liegen nicht auf einer Geraden' % ort)
    ab = (pt['B'][0] - pt['A'][0], pt['B'][1] - pt['A'][1]); a2b2 = (pt["B'"][0] - pt["A'"][0], pt["B'"][1] - pt["A'"][1])
    if ab[0] * a2b2[1] - ab[1] * a2b2[0] != 0: fehler.append('%s: Skizze: AB und A\'B\' sind nicht parallel' % ort)
    if not (d2(pt['S'], pt['A']) < d2(pt['S'], pt["A'"]) and d2(pt['S'], pt['B']) < d2(pt['S'], pt["B'"])): fehler.append('%s: Skizze: A, B müssen näher an S liegen als A\', B\'' % ort)
    L = lambda p, q: math.sqrt(d2(pt[p], pt[q]))
    gegeben = {m.group(1): zahl(m.group(2)) for m in re.finditer(r"(S[AB]'?|AB|A'B') = ([\d,]+) cm", e['beispiel']['aufgabe'])}
    gesucht = re.search(r'Gesucht: ([\w\']+)\.', e['beispiel']['aufgabe'])
    erg = zahl(re.match(r'([\d,]+) cm', e['beispiel']['ergebnis']).group(1))
    name = gesucht.group(1) if gesucht else ''
    if name not in ("SB'", "A'B'"): fehler.append('%s: gesuchte Strecke nicht erkannt' % ort)
    gegeben[name] = erg
    namen = {'SA': ('S', 'A'), "SA'": ('S', "A'"), 'SB': ('S', 'B'), "SB'": ('S', "B'"), 'AB': ('A', 'B'), "A'B'": ("A'", "B'")}
    for n, w in gegeben.items():
        if n not in namen: fehler.append('%s: Strecke %s unbekannt' % (ort, n)); continue
        if abs(L(*namen[n]) - w) > 1e-9: fehler.append('%s: Skizze: %s ist %s, im Text steht %s' % (ort, n, L(*namen[n]), w))
    # Verhältnisse
    if d2(pt['S'], pt['A']) * d2(pt["S"], pt["B'"]) != d2(pt['S'], pt["A'"]) * d2(pt['S'], pt['B']): fehler.append('%s: Skizze: SA : SA\' ist nicht gleich SB : SB\'' % ort)
    if d2(pt['S'], pt['A']) * d2(pt["A'"], pt["B'"]) != d2(pt['S'], pt["A'"]) * d2(pt['A'], pt['B']): fehler.append('%s: Skizze: SA : SA\' ist nicht gleich AB : A\'B\'' % ort)
    zaehle('skizzen-strahlen')
def kong_pruefen(e, ort, fehler):
    sk = e.get('skizze') or {}
    pt = sk.get('punkte'); mk = sk.get('markierungen')
    if not pt or not mk or set(pt) != {'A', 'B', 'C'}: fehler.append('%s: Skizze: Punkte A, B, C und Markierungen nötig' % ort); return
    if abs((pt['B'][0] - pt['A'][0]) * (pt['C'][1] - pt['A'][1]) - (pt['B'][1] - pt['A'][1]) * (pt['C'][0] - pt['A'][0])) < 1e-6: fehler.append('%s: Skizze: Dreieck ist entartet' % ort)
    seiten, wink = [], []
    for m in mk:
        t = m.get('text', '')
        try:
            if m['typ'] == 'seite':
                w = zahl(re.search(r'= ([\d,]+) cm', t).group(1)); is_ = dist(pt[m['von']], pt[m['nach']])
                if abs(is_ - w) > 0.01: fehler.append('%s: Skizze: Seite %s%s ist %.3f cm, im Text %s' % (ort, m['von'], m['nach'], is_, t))
                seiten.append((m['von'], m['nach'], w))
            elif m['typ'] == 'winkel':
                w = zahl(re.search(r'= ([\d,]+)°', t).group(1)); is_ = winkel(pt[m['von']], pt[m['scheitel']], pt[m['nach']])
                if abs(is_ - w) > 0.1: fehler.append('%s: Skizze: Winkel bei %s ist %.2f°, im Text %s' % (ort, m['scheitel'], is_, t))
                wink.append((m['scheitel'], m['von'], m['nach'], w))
            else: fehler.append('%s: Markierung mit unbekanntem Typ %r' % (ort, m.get('typ')))
        except (KeyError, AttributeError): fehler.append('%s: Markierung falsch aufgebaut: %r' % (ort, m))
    k = e['kennung']
    if k == 'nt-09':
        if len(seiten) != 3 or wink: fehler.append('%s: SSS braucht drei Seiten und keinen Winkel' % ort)
        elif not all(s[2] < sum(x[2] for x in seiten) - s[2] for s in seiten): fehler.append('%s: SSS: Dreiecksungleichung verletzt' % ort)
    elif k == 'nt-10':
        if len(seiten) != 2 or len(wink) != 1: fehler.append('%s: SWS braucht zwei Seiten und einen Winkel' % ort)
        else:
            s, v, n, w = wink[0]
            if not all(s in (a, b) for a, b, _ in seiten) or {v, n} != {(set(x[:2]) - {s}).pop() for x in seiten}: fehler.append('%s: SWS: Der Winkel liegt nicht zwischen den beiden Seiten' % ort)
    elif k == 'nt-11':
        if len(seiten) != 1 or len(wink) != 2: fehler.append('%s: WSW braucht eine Seite und zwei Winkel' % ort)
        else:
            a, b, _ = seiten[0]
            if {w[0] for w in wink} != {a, b}: fehler.append('%s: WSW: Die Winkel liegen nicht an den Enden der Seite' % ort)
            if sum(w[3] for w in wink) >= 180: fehler.append('%s: WSW: Winkel zusammen nicht unter 180°' % ort)
    elif k == 'nt-12':
        if len(seiten) != 2 or len(wink) != 1: fehler.append('%s: SsW braucht zwei Seiten und einen Winkel' % ort)
        else:
            s, v, n, w = wink[0]
            gegenueber = [x for x in seiten if s not in x[:2]]
            if len(gegenueber) != 1: fehler.append('%s: SsW: Der Winkel liegt keiner der beiden Seiten gegenüber' % ort)
            else:
                q = gegenueber[0]; p = [x for x in seiten if x is not q][0]
                if not q[2] > p[2]: fehler.append('%s: SsW: Der Winkel liegt nicht der längeren Seite gegenüber' % ort)
                elif loesungen(p[2], q[2], w) != 1: fehler.append('%s: SsW: Es gibt nicht genau ein Dreieck' % ort)
    zaehle('skizzen-kongruenz')

# ============================================================ Prüfung des Nachtrags
ARTEN = ('verfahren', 'satz', 'formel', 'kongruenz')
PFLICHT = ('kennung', 'titel', 'art', 'formel', 'bedingung', 'groessen', 'schritte', 'zeichnung', 'beispiel', 'pruefung', 'fehler', 'ab_klasse', 'regeln', 'stichwoerter')
def schreibweise(ort, t, fehler):
    if re.search(r'\d\.\d', t): fehler.append('%s: Dezimalpunkt statt Komma: %r' % (ort, t))
    if re.search(r'(?<![\d,./+_])\d{4,}(?!\d|-)', t): fehler.append('%s: Zahl ab 4 Stellen ohne Tausenderleerzeichen: %r' % (ort, t))
    if re.search('[      ]', t): fehler.append('%s: Sonderleerzeichen' % ort)
    if re.search(r'\d\*|\* ?\d| x (?=\d)', t): fehler.append('%s: Malzeichen falsch (Bestand: ·): %r' % (ort, t))
    if re.search(r'\d(?:km|m|cm|dm|mm|kg|g|mg|l|ml|€|ct)\b', t): fehler.append('%s: Einheit ohne Leerzeichen: %r' % (ort, t))
def pruefe_nachtrag(daten, fehler):
    es = daten['eintraege']; gesehen = set()
    for e in es:
        k = e.get('kennung', '?'); o = 'nachtrag/%s' % k
        for p in PFLICHT:
            if p not in e or e[p] in (None, '', [], {}) and p not in ('regeln',): fehler.append('%s: Pflichtfeld %s fehlt oder ist leer' % (o, p))
        if e.get('art') not in ARTEN: fehler.append('%s: art %r unbekannt' % (o, e.get('art')))
        if k in gesehen: fehler.append('%s: Kennung doppelt im Nachtrag' % o)
        gesehen.add(k)
        if k in bestand_kennungen: fehler.append('%s: Kollision: Kennung gibt es schon im Bestand (Tafeln, Einzelregeln oder Universum)' % o)
        if not re.fullmatch(r'nt-\d\d', str(k)): fehler.append('%s: Kennung muss nt-NN heißen' % o)
        if str(e.get('titel', '')).lower() in bestand_titel: fehler.append('%s: Titel gibt es schon in einer Tafel (Doppelung)' % o)
        if any(p not in e for p in PFLICHT): continue
        # Größen, Beispiel, Fehler
        for g in e['groessen']:
            if not (isinstance(g, dict) and g.get('zeichen') and g.get('name') and 'einheit' in g): fehler.append('%s: Größe ohne Zeichen, Bedeutung oder Einheit: %r' % (o, g))
        for fld in ('aufgabe', 'rechnung', 'ergebnis'):
            if not e['beispiel'].get(fld): fehler.append('%s: beispiel.%s fehlt' % (o, fld))
        for fld in ('falsch', 'richtig'):
            if not e['fehler'].get(fld): fehler.append('%s: fehler.%s fehlt' % (o, fld))
        if len(e['schritte']) < 3: fehler.append('%s: weniger als 3 Schritte' % o)
        sw = e['stichwoerter']
        if len(sw) < 4 or not all(isinstance(s, str) and s.strip() for s in sw) or len(set(sw)) != len(sw): fehler.append('%s: stichwoerter fehlen, sind leer oder doppelt' % o)
        proben(e['pruefung'], o + '/pruefung', fehler, 2)
        proben(e['fehler'].get('pruefung'), o + '/fehler/pruefung', fehler, 1)
        # Texte
        for pf, t in blaetter(e, o, skip=('kennung', 'pruefung', 'stichwoerter', 'skizze', 'wort', 'lernziel', 'thema')):
            schreibweise(pf, t, fehler)
        for pf in ('beispiel/rechnung', 'beispiel/aufgabe', 'fehler/falsch', 'fehler/richtig'):
            a, b = pf.split('/'); kette_pruefen(e[a][b], o + '/' + pf, fehler)
        for i, s in enumerate(e['schritte']): kette_pruefen(s, '%s/schritte[%d]' % (o, i), fehler)
        if not e['zeichnung'] or len(e['zeichnung']) < 40: fehler.append('%s: Zeichenbeschreibung zu kurz' % o)
        # Verweise
        for r in e['regeln']:
            if r.get('kennung') not in ids: fehler.append('%s: Regel %s nicht in regeln-universum.json' % (o, r.get('kennung')))
            elif ids[r['kennung']] != r.get('name'): fehler.append('%s: Regel %s heißt im Universum „%s“, hier „%s“' % (o, r['kennung'], ids[r['kennung']], r.get('name')))
            if not r.get('passt'): fehler.append('%s: Regel %s ohne Begründung' % (o, r.get('kennung')))
        if not e['regeln'] and not e.get('regeln_hinweis'): fehler.append('%s: keine Regeln und kein regeln_hinweis' % o)
        # Klasse
        a = e['ab_klasse']; tri = set()
        for b in a.get('beleg', []):
            t = thema(b.get('thema'))
            if not t: fehler.append('%s: Thema %s fehlt im Bestand' % (o, b.get('thema'))); continue
            et = [x for x in t['inhalt']['etappen'] if x['lernziel'] == b.get('lernziel')]
            if not et: fehler.append('%s: Lernziel %s nicht in %s' % (o, b.get('lernziel'), b['thema'])); continue
            if b['wort'] not in json.dumps(et[0], ensure_ascii=False): fehler.append('%s: Wort „%s“ steht nicht in %s/%s' % (o, b['wort'], b['thema'], b['lernziel']))
            kl = t['klasse']; tri.add((kl.get('gym_by'), kl.get('rs_by'), kl.get('ib_myp'))); zaehle('belege')
        if a.get('beleg'):
            if tri != {(a.get('gymnasium_by'), a.get('realschule_by'), a.get('ib_myp'))}: fehler.append('%s: ab_klasse %s passt nicht zu den Belegen %s' % (o, (a.get('gymnasium_by'), a.get('realschule_by'), a.get('ib_myp')), tri))
            if (a.get('gymnasium_by') is None or a.get('realschule_by') is None) and not e.get('ab_klasse_hinweis'): fehler.append('%s: Klasse offen (Gymnasium oder Realschule leer) ohne ab_klasse_hinweis' % o)
        elif any(a.get(x) is not None for x in ('gymnasium_by', 'realschule_by', 'ib_myp')) or not e.get('ab_klasse_hinweis'): fehler.append('%s: ohne Beleg muss ab_klasse leer sein und ab_klasse_hinweis stehen' % o)
        # Skizzen
        if e['art'] == 'kongruenz': kong_pruefen(e, o, fehler)
        if e['kennung'] in ('nt-03', 'nt-04'): strahl_pruefen(e, o, fehler)
        if e['art'] == 'kongruenz' and not e.get('so_liegt_es'): fehler.append('%s: so_liegt_es fehlt (wie liegen die Angaben?)' % o)
    zaehle('nachtrag-eintraege', len(es))
    # die zwölf Aufträge sind alle da
    soll = {'Dreisatz': 2, 'Strahlensatz': 2, 'Geschwindigkeit': 1, 'Dichte': 1, 'Pyramide': 1, 'Kreisring': 1, 'Kongruenzsatz': 4}
    for w, n in soll.items():
        if sum(1 for e in es if w in e.get('titel', '')) != n: fehler.append('nachtrag: %s sollte %d-mal vorkommen' % (w, n))

def pruefe_klassen(kn, fehler):
    soll = {'fg-08', 'fg-11', 'zz-09', 'zz-11', 'zz-12', 'zz-15', 'sw-08', 'sw-09', 'sw-10', 'sw-11', 'ff-13', 'ff-14', 'ff-15', 'ff-16', 'ff-17', 'zw-w01'}
    da = [x.get('kennung') for x in kn['eintraege']]
    if set(da) != soll or len(da) != len(set(da)): fehler.append('klassen: Kennungen %s ≠ Auftrag %s' % (sorted(da), sorted(soll)))
    for x in kn['eintraege']:
        o = 'klassen/%s' % x.get('kennung')
        t = tafeln.get(x.get('tafel'))
        eint = {e['kennung']: e for e in t['eintraege']} if t else {}
        if x.get('kennung') not in eint: fehler.append('%s: Eintrag %s gibt es in Tafel %s nicht' % (o, x.get('kennung'), x.get('tafel'))); continue
        orig = eint[x['kennung']]['ab_klasse']
        if any(orig.get(k) is not None for k in ('gymnasium_by', 'realschule_by')): fehler.append('%s: Tafel hat schon eine Klasse, Nachtrag überflüssig' % o)
        if x.get('titel') != eint[x['kennung']]['titel']: fehler.append('%s: Titel weicht von der Tafel ab' % o)
        if not x.get('begruendung'): fehler.append('%s: Begründung fehlt' % o)
        if x.get('status') == 'offen':
            if any(x.get(k) is not None for k in ('gymnasium_by', 'realschule_by', 'ib_myp')) or x.get('belege'): fehler.append('%s: offen, aber Klasse oder Belege angegeben' % o)
        elif x.get('status') == 'belegt_bestand':
            if not x.get('belege'): fehler.append('%s: belegt, aber ohne Belege' % o); continue
            tri = []
            for b in x['belege']:
                t2 = thema(b.get('thema'))
                if not t2: fehler.append('%s: Thema %s fehlt' % (o, b.get('thema'))); continue
                if b.get('art') != 'aufgabe' or b['wort'] not in json.dumps(t2.get('aufgaben'), ensure_ascii=False): fehler.append('%s: Wort „%s“ steht nicht in den Aufgaben von %s' % (o, b.get('wort'), b['thema']))
                tri.append(t2['klasse'])
            wort = x['belege'][0]['wort']
            for key, feld in (('gym_by', 'gymnasium_by'), ('rs_by', 'realschule_by'), ('ib_myp', 'ib_myp')):
                kleinste = min([k[key] for k in tri if k.get(key) is not None] or [None]) if any(k.get(key) is not None for k in tri) else None
                if x.get(feld) != kleinste: fehler.append('%s: %s %s ≠ kleinste Klasse der Belege %s' % (o, feld, x.get(feld), kleinste))
                # global: kein Thema mit kleinerer Klasse enthält das Wort
                for tn in alle_themen:
                    t3 = thema(tn)
                    if wort in json.dumps(t3, ensure_ascii=False) and t3['klasse'].get(key) is not None and x.get(feld) is not None and t3['klasse'][key] < x[feld]:
                        fehler.append('%s: „%s“ kommt schon in %s (%s %s) vor, früher als angegeben' % (o, wort, tn, key, t3['klasse'][key]))
        else: fehler.append('%s: status %r unbekannt' % (o, x.get('status')))
        zaehle('klassen-eintraege')
    # Berichtigung V1
    b = kn['berichtigungen'][0]
    v1 = gesetze['V1']['fehler']
    if b['alt'][:-1].split('. ')[0] not in v1 and b['neu'].split('. ')[0] not in v1: fehler.append('klassen: V1 enthält weder den alten noch den neuen Satz')
    ak = [a for a in laden(uebersicht / 'einheiten/einheiten.json')['arten'] if a['art'] == 'Fläche'][0]['ab_klasse']
    if (ak['gymnasium_by'], ak['realschule_by']) != (5, 5): fehler.append('klassen: Einheitentafel sagt für Flächen nicht Klasse 5')
    lk = laden(repo / 'inhalte/pruefung/lehrplan/lk_daten_2211.json')['punkte']
    for sa, lb in (('gym', '4.2'), ('rs', '5')):
        if not any(p['schulart'] == sa and p['klasse'] == 5 and p['lernbereich']['pfad'] == lb and p['rolle'] == 'neu' and 'einheiten' in p['etappen'] and p['thema_titel'] == 'Umfang und Flächeninhalt' for p in lk): fehler.append('klassen: Lehrplan-Beleg für %s Klasse 5 (Flächeneinheiten) fehlt in lk_daten_2211.json' % sa)
    if (thema('messen.flaechen')['klasse'].get('gym_by'), thema('messen.flaechen')['klasse'].get('rs_by')) != (5, 5): fehler.append('klassen: messen.flaechen ist nicht Klasse 5')
    for pfad in ('inhalte/pruefung/lehrplan/lk_daten_2211.json', 'inhalte/themen/messen.flaechen.json'):
        if not (repo / pfad).exists(): fehler.append('klassen: Beleg-Datei %s fehlt' % pfad)

def pruefe_tafeln_parallelogramm(fehler):
    ff = {e['kennung']: e for e in tafeln['formeln-flaechen']['eintraege']}
    g = [x for x in ff['ff-04']['groessen'] if x['zeichen'] == 'g'][0]
    if 'eine der Seiten a oder b' not in g['name']: fehler.append('tafeln: ff-04 muss sagen, dass g eine der Seiten a oder b ist')
    if 'eine der beiden Seiten a und b' not in ff['ff-04']['zeichnung'] and 'eine der beiden Seiten a und b' not in g['beschriften']: fehler.append('tafeln: ff-04 ohne Erklärung zu a und b')
    for e in tafeln['formeln-flaechen']['eintraege']:
        for x in e['groessen']:
            if 'Grundseite' in x['name'] and x['zeichen'] != 'g': fehler.append('tafeln: %s: Grundseite heißt %s, sie darf nur g heißen' % (e['kennung'], x['zeichen']))
    if 'Grundseite' in json.dumps(ff['ff-14']['groessen'], ensure_ascii=False): fehler.append('tafeln: ff-14 nennt noch eine Grundseite')
    md = (uebersicht / 'tafeln/formeln-flaechen/tafel.md').read_text(encoding='utf-8')
    if 'a = Grundseite' in md: fehler.append('tafeln: tafel.md nennt noch „a = Grundseite“')
    if 'g = Grundseite (eine der Seiten a oder b)' not in md: fehler.append('tafeln: tafel.md ff-04 nicht angepasst')

# ============================================================ Kurzformen
def sonst_lesen():
    q = (repo / 'tools/tafeln_bauen.cjs').read_text(encoding='utf-8')
    m = re.search(r'const SONST = \[(.*?)\];\n', q, re.S)
    if not m: return None
    out = {}
    for z in re.finditer(r"\{ gesetz: '(\w+)'(?:, kurz: \[(.*?)\])?(?:, bed: '(.*?)')? \}", m.group(1), re.S):
        kurz = re.findall(r"'((?:[^'\\]|\\.)*)'", z.group(2) or '')
        out[z.group(1)] = {'kurz': kurz, 'bed': z.group(3)}
    return out
SIEBEN = ('D3', 'D4', 'D13', 'U7', 'G24', 'G25', 'A19')
def pruefe_kurzformen(daten, fehler):
    sonst = sonst_lesen()
    if sonst is None: fehler.append('kurzformen: SONST in tools/tafeln_bauen.cjs nicht gefunden'); return
    kz = {g: sonst[g] for g in SIEBEN if g in sonst}
    if set(kz) != set(SIEBEN) or any(not v['kurz'] for v in kz.values()): fehler.append('kurzformen: SONST enthält nicht alle sieben Kurzformen mit Text'); return
    md = (hier / 'kurzformen.md').read_text(encoding='utf-8')
    zeilen = {}
    for z in md.splitlines():
        c = [x.strip() for x in z.strip().strip('|').split('|')]
        if len(c) == 6 and c[0] in SIEBEN: zeilen[c[0]] = c
    if set(zeilen) != set(SIEBEN): fehler.append('kurzformen.md: Zeilen für %s fehlen' % sorted(set(SIEBEN) - set(zeilen)))
    for g, c in zeilen.items():
        if g not in kz: continue
        for k in kz[g]['kurz']:
            if k not in c[2]: fehler.append('kurzformen.md/%s: Kurzform „%s“ steht nicht wie im Bau in der Spalte „Kurzform im Bau“' % (g, k))
        if kz[g]['bed'] and kz[g]['bed'] not in c[2]: fehler.append('kurzformen.md/%s: Bedingung des Baus „%s“ fehlt' % (g, kz[g]['bed']))
        if not (c[3].startswith('richtig') or c[3].startswith('so berichtigen')): fehler.append('kurzformen.md/%s: Urteil muss mit „richtig“ oder „so berichtigen“ beginnen' % g)
        if not c[4]: fehler.append('kurzformen.md/%s: Bedingung fehlt' % g)
        u = gesetze[g]
        if 'Gymnasium %s' % u['gym'] not in c[5] or 'Realschule %s' % u['rs'] not in c[5]: fehler.append('kurzformen.md/%s: Klasse stimmt nicht mit dem Universum (Gymnasium %s, Realschule %s)' % (g, u['gym'], u['rs']))
        if g in ('D4', 'G25', 'A19', 'D3') and False: pass
        if c[1] != u['name']: fehler.append('kurzformen.md/%s: Name „%s“ ≠ Universum „%s“' % (g, c[1], u['name']))
    pr = daten.get('kurzformen_proben', {})
    for g in SIEBEN:
        proben(pr.get(g), 'kurzformen_proben/%s' % g, fehler, 3)
    for n, t in enumerate(md.split('\n')): kette_pruefen(t, 'kurzformen.md:%d' % (n + 1), fehler)
    zaehle('kurzformen', len(zeilen))

# ============================================================ alles
def pruefe_alles(daten, klassen, mit_extern=True):
    fehler = []
    pruefe_nachtrag(daten, fehler)
    pruefe_klassen(klassen, fehler)
    if mit_extern:
        pruefe_tafeln_parallelogramm(fehler)
        pruefe_kurzformen(daten, fehler)
    return fehler

daten = laden(hier / 'nachtrag.json')
klassen = laden(hier / 'klassen-nachtrag.json')
fehler = pruefe_alles(daten, klassen)
# uebersicht.md nennt alle Kennungen
ue = (hier / 'uebersicht.md').read_text(encoding='utf-8') if (hier / 'uebersicht.md').exists() else ''
for e in daten['eintraege']:
    if e['kennung'] not in ue: fehler.append('uebersicht.md: Kennung %s fehlt' % e['kennung'])
for x in klassen['eintraege']:
    if x['kennung'] not in ue: fehler.append('uebersicht.md: Kennung %s fehlt' % x['kennung'])
for pfad, t in (('uebersicht.md', ue), ('kurzformen.md', (hier / 'kurzformen.md').read_text(encoding='utf-8'))):
    schreibweise(pfad, t, fehler) if False else None
    for n, z in enumerate(t.split('\n')): kette_pruefen(z, '%s:%d' % (pfad, n + 1), fehler)
    if re.search(r'(?i)\b(?:Blödorn|Norick|Sebastian)\b', t): fehler.append('%s: echter Personenname' % pfad)
for pf, t in blaetter(daten) :
    if re.search(r'(?i)(?:Blödorn|Norick|Sebastian)', t): fehler.append('nachtrag.json: echter Personenname bei %s' % pf)

# ---------- Negativprüfungen: verdorbene Kopien müssen anschlagen
def negativ():
    ergebnisse = []
    def versuch(name, erwartet, aendern):
        d, k = copy.deepcopy(daten), copy.deepcopy(klassen)
        aendern(d, k)
        f = pruefe_alles(d, k, mit_extern=False)
        ok = any(erwartet in x for x in f)
        ergebnisse.append((name, erwartet, ok, f[:1]))
    E = lambda d, kenn: [e for e in d['eintraege'] if e['kennung'] == kenn][0]
    def a(d, k): E(d, 'nt-01')['beispiel']['rechnung'] = E(d, 'nt-01')['beispiel']['rechnung'].replace('= 10,40 €', '= 10,50 €')
    versuch('1 falsche Rechnung im Text (10,50 € statt 10,40 €)', 'Rechnung falsch', a)
    def b(d, k): E(d, 'nt-06')['pruefung'][0]['r'] = '2.8'
    versuch('2 falsche Rechenprobe (ρ = 2,8 statt 2,7)', 'Rechenprobe falsch', b)
    def c(d, k): E(d, 'nt-02')['kennung'] = 'nt-01'
    versuch('3 doppelte Kennung', 'Kennung doppelt', c)
    def dd(d, k): E(d, 'nt-03')['kennung'] = 'ff-01'
    versuch('4 Kollision mit bestehender Kennung ff-01', 'Kollision', dd)
    def ee(d, k): del E(d, 'nt-07')['bedingung']
    versuch('5 Pflichtfeld bedingung fehlt', 'Pflichtfeld bedingung', ee)
    def ff(d, k): E(d, 'nt-09')['skizze']['punkte']['C'][1] += 0.5
    versuch('6 Skizze passt nicht zu den Maßen (SSS)', 'Skizze', ff)
    def gg(d, k): E(d, 'nt-03')['ab_klasse']['gymnasium_by'] = 8
    versuch('7 falsche Klasse (Strahlensatz Gymnasium 8)', 'ab_klasse', gg)
    def hh(d, k): [x for x in k['eintraege'] if x['kennung'] == 'zw-w01'][0]['gymnasium_by'] = 6
    versuch('8 falsche Klasse im Klassen-Nachtrag (Summand Gymnasium 6)', 'klassen/zw-w01', hh)
    def ii(d, k): E(d, 'nt-04')['skizze']['punkte']["B'"] = [11, 7.5]
    versuch('9 Strahlensatz-Skizze nicht parallel', 'nicht parallel', ii)
    return ergebnisse
neg = negativ()
for name, erwartet, ok, bsp in neg:
    if not ok: fehler.append('Negativprüfung „%s“ hat NICHT angeschlagen (erwartet: %s)' % (name, erwartet))
zaehle('negativpruefungen', len(neg))

if fehler:
    print('FEHLER (%d):' % len(fehler))
    for x in fehler[:60]: print(' -', x[:400])
    sys.exit(1)
print(' · '.join('%s: %d' % (k, v) for k, v in sorted(Z.items())))
for name, erwartet, ok, bsp in neg: print('  Negativprüfung angeschlagen: %s  →  %s' % (name, (bsp[0][:110] if bsp else '')))
print('OK')
