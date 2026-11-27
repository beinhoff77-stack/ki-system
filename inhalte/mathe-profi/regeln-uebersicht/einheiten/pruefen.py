#!/usr/bin/env python3
"""Prüft einheiten.json und tafel.md: jeden Treppenfaktor gegen die wahren SI-Verhältnisse, jede Gleichung, jedes Beispiel
(exakt mit Brüchen, kein Float), Zahlenschreibweise, Klassenangaben und Kennungen gegen den Bestand im Repo.
Aufruf:  python3 -I inhalte/mathe-profi/regeln-uebersicht/einheiten/pruefen.py
Endet mit „OK“, sonst mit Fehlerliste und Exit-Code 1."""
import json, pathlib, re, sys
from fractions import Fraction as F
from collections import deque

hier = pathlib.Path(__file__).resolve().parent
repo = hier.parents[3]
fehler = []
def f(msg): fehler.append(msg)
zaehler = {'faktoren': 0, 'gleichungen': 0, 'beispiele': 0, 'stolperstellen': 0, 'rechnungen': 0}

# ---------- Zahlen und Größen ----------
ZAHL = r'\d+(?: \d{3})*(?:,\d+)?'
EINH = r'[A-Za-z€²³]+(?:/[A-Za-z²³]+)?'
SEG = r'(?:%s) (?:%s)(?![\w²³/])' % (ZAHL, EINH)
Q = r'%s(?: %s)*' % (SEG, SEG)
def zahl(s):
    s = s.strip().replace('−', '-')
    assert re.fullmatch(ZAHL, s), 'Zahl falsch geschrieben: %r' % s
    return F(s.replace(' ', '').replace(',', '.'))

# wahre Verhältnisse (SI), unabhängig von der Datei: Wert in der Grundeinheit der Größenart
K, M, MI = F(1000), F(1, 1000), F(1, 1000000)
WAHR = {
 'Länge': {'km': K, 'm': F(1), 'dm': F(1, 10), 'cm': F(1, 100), 'mm': M},
 'Fläche': {'km²': K * K, 'ha': F(10000), 'a': F(100), 'm²': F(1), 'dm²': F(1, 100), 'cm²': F(1, 10000), 'mm²': MI},
 'Volumen und Hohlmaße': {'m³': F(1), 'dm³': M, 'cm³': MI, 'mm³': M * MI, 'hl': F(100) * M, 'l': M, 'dl': M / 10, 'cl': M / 100, 'ml': MI},
 'Masse': {'t': K, 'kg': F(1), 'g': M, 'mg': MI},
 'Zeit': {'d': F(86400), 'h': F(3600), 'min': F(60), 's': F(1)},
 'Geld': {'€': F(1), 'ct': F(1, 100)},
}
EINHEIT_ART = {u: art for art, t in WAHR.items() for u in t}
assert len(EINHEIT_ART) == sum(len(t) for t in WAHR.values()), 'Einheit doppelt in WAHR'
DIM = {'Länge': 'L', 'Fläche': 'F', 'Volumen und Hohlmaße': 'V', 'Masse': 'M', 'Zeit': 'T', 'Geld': 'G'}

def einheit(u):
    """-> (Dimension, Wert in SI-Grundeinheit) oder KeyError"""
    if '/' in u:
        a, b = u.split('/')
        da, va = einheit(a); db, vb = einheit(b)
        return '%s/%s' % (da, db), va / vb
    art = EINHEIT_ART[u]
    return DIM[art], WAHR[art][u]

def menge(text):
    """'1 h 30 min' -> (Dimension, Wert) ; KeyError bei unbekannter Einheit"""
    segs = list(re.finditer(r'(%s) (%s)(?![\w²³/])' % (ZAHL, EINH), text))
    if not segs or ' '.join(m.group(0) for m in segs) != text.strip(): raise ValueError('keine Größe: %r' % text)
    dim, summe = None, F(0)
    for m in segs:
        d, v = einheit(m.group(2))
        if dim not in (None, d): raise ValueError('verschiedene Größen in %r' % text)
        dim = d; summe += zahl(m.group(1)) * v
    return dim, summe

def gleich(text):
    """prüft 'A = B' (beliebig viele Glieder). True/False; ValueError bei verschiedenen Größen; KeyError bei unbekannter Einheit"""
    teile = [menge(t) for t in text.split(' = ')]
    for t in teile[1:]:
        if t[0] != teile[0][0]: raise ValueError('links und rechts verschiedene Größen: %s' % text)
    return all(t[1] == teile[0][1] for t in teile[1:])

# ---------- Daten laden ----------
doc = json.loads((hier / 'einheiten.json').read_text(encoding='utf-8'))
arten = doc['arten']
namen = [a['art'] for a in arten]
if namen != ['Länge', 'Fläche', 'Volumen und Hohlmaße', 'Masse', 'Zeit', 'Geld', 'Geschwindigkeit', 'Dichte']: f('Größenarten oder Reihenfolge unerwartet: %s' % namen)

def alle_texte(x, pfad=''):
    if isinstance(x, str): yield pfad, x
    elif isinstance(x, list):
        for i, y in enumerate(x): yield from alle_texte(y, '%s[%d]' % (pfad, i))
    elif isinstance(x, dict):
        for k, y in x.items():
            if k == 'pruefung' and pfad.endswith(']') and 'stolperstellen' in pfad: continue  # absichtlich falsche Gleichungen, getrennt geprüft
            if k == 'stand': continue
            yield from alle_texte(y, pfad + '/' + k)

# ---------- 1 Schreibweise in allen Texten ----------
for pfad, t in alle_texte(doc):
    if re.search(r'\d\.\d', t): f('%s: Dezimalpunkt statt Komma: %r' % (pfad, t))
    if re.search(r'(?<![\d,.])\d{4,}(?!\d)', t): f('%s: Zahl ab 4 Stellen ohne Tausenderleerzeichen: %r' % (pfad, t))
    if re.search(r'[   ]', t): f('%s: Sonderleerzeichen (Bestand nutzt gewöhnliches Leerzeichen)' % pfad)
    if re.search(r'\d\*|\* ?\d| x ', t): f('%s: Malzeichen falsch (Bestand: ·): %r' % (pfad, t))
    if re.search(r'\d(?:km|m|cm|dm|mm|kg|g|mg|t|l|ml|h|min|s|d|€|ct)\b', t): f('%s: Einheit ohne Leerzeichen: %r' % (pfad, t))
    # jede Gleichung zwischen Größen im Fließtext nachrechnen
    for m in re.finditer(r'(?<![\w,])(%s)(?: = (%s))+' % (Q, Q), t):
        try: ok = gleich(m.group(0))
        except KeyError: continue
        except ValueError as e: f('%s: %s' % (pfad, e)); continue
        zaehler['gleichungen'] += 1
        if not ok: f('%s: Gleichung falsch: %s' % (pfad, m.group(0)))

# ---------- 2 Treppen und Faktoren ----------
def kanten(a):
    """Liste (groß, klein, Faktor) aus allen Treppen der Art; plus Verbindungen mit Faktor 1"""
    ks = []
    for tr in [a['treppe']] + [w['treppe'] for w in a.get('weitere_treppen', [])]:
        for x, y in zip(tr, tr[1:]):
            if x['zur_naechsten'] is None: f('%s: %s hat keinen Faktor, ist aber nicht die letzte Einheit' % (a['art'], x['einheit']))
            ks.append((x['einheit'], y['einheit'], zahl(x['zur_naechsten'])))
        if tr[-1]['zur_naechsten'] is not None: f('%s: letzte Einheit %s darf keinen Faktor haben' % (a['art'], tr[-1]['einheit']))
    for v in a.get('verbindung', []):
        l, r = menge(v['links']), menge(v['rechts'])
        lu, ru = v['links'].split(' ')[1], v['rechts'].split(' ')[1]
        if l[0] != r[0]: f('%s: Verbindung %s = %s verbindet verschiedene Größen' % (a['art'], v['links'], v['rechts']))
        ks.append((lu, ru, F(1)))
    return ks

def darst(tr):
    return tr[0]['einheit'] + ''.join(' –%s→ %s' % (x['zur_naechsten'], y['einheit']) for x, y in zip(tr, tr[1:]))

wege = {}  # je Art: Nachbarschaft
for a in arten:
    art = a['art']
    if a['darstellung'] != darst(a['treppe']): f('%s: darstellung stimmt nicht mit treppe überein' % art)
    for w in a.get('weitere_treppen', []):
        if w['darstellung'] != darst(w['treppe']): f('%s/%s: darstellung stimmt nicht' % (art, w['name']))
    ks = kanten(a)
    # Faktoren gegen die wahren Verhältnisse
    for g, k, fa in ks:
        zaehler['faktoren'] += 1
        try: dg, vg = einheit(g); dk, vk = einheit(k)
        except KeyError as e: f('%s: Einheit unbekannt in der Prüftabelle: %s' % (art, e)); continue
        if dg != dk: f('%s: %s und %s sind verschiedene Größen' % (art, g, k))
        if vg != fa * vk: f('%s: Faktor %s → %s ist %s, wahr ist %s' % (art, g, k, fa, vg / vk))
    # Produkt der Stufen = direkter Faktor (alle Paare derselben Treppe)
    for tr in [a['treppe']] + [w['treppe'] for w in a.get('weitere_treppen', [])]:
        for i in range(len(tr)):
            for j in range(i + 1, len(tr)):
                p = F(1)
                for x in tr[i:j]: p *= zahl(x['zur_naechsten'])
                try: dv, vv = einheit(tr[i]['einheit']); dn, vn = einheit(tr[j]['einheit'])
                except KeyError: continue
                zaehler['faktoren'] += 1
                if vv != p * vn: f('%s: Produkt der Stufen %s → %s = %s, direkter Faktor ist %s' % (art, tr[i]['einheit'], tr[j]['einheit'], p, vv / vn))
    wege[art] = ks
    # Gleichungen der Art
    if not a.get('gleichungen'): f('%s: keine gleichungen' % art)
    for g in a.get('gleichungen', []):
        zaehler['gleichungen'] += 1
        try:
            if not gleich(g): f('%s: Gleichung falsch: %s' % (art, g))
        except (KeyError, ValueError) as e: f('%s: Gleichung nicht prüfbar %r (%s)' % (art, g, e))
    for h in a.get('herleitung', []):
        for g in h['gleichungen']:
            zaehler['gleichungen'] += 1
            try:
                if not gleich(g): f('%s: Herleitung, Gleichung falsch: %s' % (art, g))
            except (KeyError, ValueError) as e: f('%s: Herleitung nicht prüfbar %r (%s)' % (art, g, e))

def weg(art, von, nach):
    """kürzester Weg als Liste (Richtung, Faktor); Faktor-1-Schritte (gleiche Größe, andere Schreibweise) fehlen"""
    nb = {}
    for g, k, fa in wege[art]:
        nb.setdefault(g, []).append((k, 'ab', fa)); nb.setdefault(k, []).append((g, 'auf', fa))
    q = deque([(von, [])]); gesehen = {von}
    while q:
        u, p = q.popleft()
        if u == nach: return [x for x in p if x[1] != 1]
        for v, r, fa in nb.get(u, []):
            if v not in gesehen: gesehen.add(v); q.append((v, p + [(r, fa)]))
    return None

# ---------- 3 Beispiele ----------
def kopf(text): return re.fullmatch(r'(%s) (%s)' % (ZAHL, EINH), text.strip())
for a in arten:
    art = a['art']; bs = a['beispiele']
    if not 3 <= len(bs) <= 4: f('%s: %d Beispiele (verlangt 3 bis 4)' % (art, len(bs)))
    tags = set()
    hat_zwei_stufen_moeglich = not a.get('zusammengesetzt') and len(a['treppe']) >= 3
    for b in bs:
        zaehler['beispiele'] += 1
        o = '%s: Beispiel %s = %s' % (art, b['von'], b['nach'])
        try:
            dv, vv = menge(b['von']); dn, vn = menge(b['nach'])
        except (KeyError, ValueError) as e: f('%s: nicht lesbar (%s)' % (o, e)); continue
        if dv != dn: f(o + ': verschiedene Größen'); continue
        if vv != vn: f('%s: stimmt nicht (links %s, rechts %s)' % (o, vv, vn))
        try:
            if not gleich(b['denn']): f(o + ': „denn“-Gleichung falsch: ' + b['denn'])
        except (KeyError, ValueError) as e: f('%s: „denn“ nicht prüfbar (%s)' % (o, e))
        soll = '%s = %s, denn %s.' % (b['von'], b['nach'], b['denn']) + (' ' + b['achtung'] if b.get('achtung') else '')
        if b['text'] != soll: f(o + ': text weicht von von/nach/denn/achtung ab')
        # Rechnung: a op b op c = r, von links nach rechts, exakt
        m = re.fullmatch(r'(%s)((?: [·:] %s)+) = (%s)' % (ZAHL, ZAHL, ZAHL), b['rechnung'])
        if not m: f(o + ': rechnung nicht lesbar: ' + b['rechnung']); continue
        zaehler['rechnungen'] += 1
        ops = re.findall(r'([·:]) (%s)' % ZAHL, m.group(2))
        x = zahl(m.group(1))
        for op, y in ops: x = x * zahl(y) if op == '·' else x / zahl(y)
        mv = kopf(b['von']); mn = kopf(b['nach'])
        if x != zahl(m.group(3)): f('%s: Rechnung ergibt %s, steht aber %s' % (o, x, m.group(3)))
        if zahl(m.group(1)) != zahl(mv.group(1)): f(o + ': Rechnung beginnt nicht mit der Zahl links')
        if zahl(m.group(3)) != zahl(mn.group(1)): f(o + ': Rechnung endet nicht mit der Zahl rechts')
        u_von, u_nach = mv.group(2), mn.group(2)
        verh = einheit(u_von)[1] / einheit(u_nach)[1]
        if 'kleinere' in b['typ'] and not verh > 1: f(o + ': „kleinere“, aber die Zielenheit ist nicht kleiner')
        if 'groessere' in b['typ'] and not verh < 1: f(o + ': „groessere“, aber die Zieleinheit ist nicht größer')
        if 'komma' in b['typ'] and ',' not in b['von'] + b['nach']: f(o + ': „komma“, aber kein Komma')
        if '/' not in u_von + u_nach:
            w = weg(art, u_von, u_nach)
            if w is None: f(o + ': kein Weg auf der Treppe'); continue
            erwartet = [('·' if r == 'ab' else ':', fa) for r, fa in w]
            gegeben = [(op, zahl(y)) for op, y in ops]
            zusammen = len(gegeben) == 1 and gegeben[0][1] == (verh if verh > 1 else 1 / verh)  # ein Schritt mit dem direkten Faktor
            if erwartet != gegeben and not zusammen:
                f('%s: Rechenschritte %s passen nicht zu den Stufen %s' % (o, gegeben, erwartet))
            if 'zwei_stufen' in b['typ'] and len(w) < 2: f(o + ': „zwei_stufen“, aber nur ein Schritt')
        tags |= set(b['typ'])
        if b.get('nicht'):
            n = ' '.join('%s %s' % tuple(x) for x in b['nicht'])
            dn2, vn2 = menge(n)
            if dn2 != dn or vn2 == vn: f(o + ': „nicht“-Angabe %s ist gleich oder andere Größe' % n)
    for pflicht in ('kleinere', 'groessere', 'komma'):
        if pflicht not in tags: f('%s: kein Beispiel vom Typ %s' % (art, pflicht))
    if hat_zwei_stufen_moeglich and 'zwei_stufen' not in tags: f('%s: kein Beispiel über zwei Stufen' % art)
    if art == 'Zeit':
        if not any(b['von'] == '1,5 h' and b['nach'] == '90 min' for b in bs): f('Zeit: Beispiel 1,5 h = 90 min fehlt')
        w = [b for b in bs if 'warnung' in b['typ']]
        if not w or '1,30 h' not in w[0]['von'] or 'nicht 1 h 30 min' not in w[0]['achtung']: f('Zeit: Warnung zu 1,30 h fehlt')

# ---------- 4 Stolperstellen, Merksatz, Schritte ----------
def saetze(t): return len(re.findall(r'[.!?](?:\s|$)', t))
kenn = json.loads((repo / 'inhalte/mathe-profi/regeln-uebersicht/kennungen.json').read_text(encoding='utf-8'))['kennungen']
fehlbilder = {fb['kennung'] for k in kenn for fb in k.get('fehlbilder', [])}
for a in arten:
    art = a['art']
    if saetze(a['merksatz']) != 1 or len(a['merksatz']) > 110: f('%s: Merksatz nicht ein Satz bis 110 Zeichen (%d)' % (art, len(a['merksatz'])))
    if not 2 <= len(a['so_gehts']) <= 3: f('%s: so_gehts hat %d Schritte' % (art, len(a['so_gehts'])))
    if not 3 <= len(a['stolperstellen']) <= 5: f('%s: %d Stolperstellen' % (art, len(a['stolperstellen'])))
    for s in a['stolperstellen']:
        zaehler['stolperstellen'] += 1
        if s.get('fehlbild') and s['fehlbild'] not in fehlbilder: f('%s: Fehlbild-Kennung unbekannt: %s' % (art, s['fehlbild']))
        for p in s.get('pruefung', []):
            try: ok = gleich(p['gleichung'])
            except (KeyError, ValueError) as e: f('%s: Stolperstelle nicht prüfbar %r (%s)' % (art, p['gleichung'], e)); continue
            if ok != p['stimmt']: f('%s: Stolperstelle „%s“ ist %s, in der Datei steht %s' % (art, p['gleichung'], ok, p['stimmt']))
    if art == 'Zeit' and not any(p['gleichung'] == '1,30 h = 1 h 30 min' and not p['stimmt'] for s in a['stolperstellen'] for p in s.get('pruefung', [])): f('Zeit: Stolperstelle 1,30 h fehlt')
    if art == 'Fläche' and not any(s.get('fehlbild') == 'fb.groesse.flaeche_mit_zehn' and any(p['gleichung'] == '3 m² = 30 dm²' and not p['stimmt'] for p in s['pruefung']) for s in a['stolperstellen']): f('Fläche: Stolperstelle 10 statt 100 fehlt')

# ---------- 5 Klassen und Etappen gegen den Bestand ----------
themen = {}
def thema(t):
    if t not in themen:
        p = repo / 'inhalte/themen' / (t + '.json')
        if not p.exists(): f('Thema fehlt im Bestand: ' + t); themen[t] = None
        else: themen[t] = (json.loads(p.read_text(encoding='utf-8')), p.read_text(encoding='utf-8'))
    return themen[t]
for a in arten:
    art = a['art']; k = a['ab_klasse']
    gesehen = set()
    for b in k['beleg']:
        t = thema(b['thema'])
        if not t: continue
        if b['lernziel'] not in {e['lernziel'] for e in t[0]['inhalt']['etappen']}: f('%s: Lernziel %s nicht in %s' % (art, b['lernziel'], b['thema']))
        kl = t[0]['klasse']
        gesehen.add((kl.get('gym_by'), kl.get('rs_by'), kl.get('ib_myp')))
    if k['beleg']:
        if gesehen != {(k['gymnasium_by'], k['realschule_by'], k['ib_myp'])}: f('%s: ab_klasse %s passt nicht zu den belegten Themen %s' % (art, (k['gymnasium_by'], k['realschule_by'], k['ib_myp']), gesehen))
    elif any(k[x] is not None for x in ('gymnasium_by', 'realschule_by', 'ib_myp')) or not a.get('ab_klasse_hinweis'): f('%s: ohne Beleg muss ab_klasse leer sein und ab_klasse_hinweis stehen' % art)
    for e in a['etappen_im_bestand']:
        t = thema(e['thema'])
        if t and {x['lernziel']: x['titel'] for x in t[0]['inhalt']['etappen']}.get(e['lernziel']) != e['titel']: f('%s: Etappentitel %r weicht vom Bestand ab' % (art, e['titel']))
    for v in a.get('vorkommen_im_bestand', []): thema(v['thema'])
    # jede Einheit, die nicht als Zusatz markiert ist, muss im Bestand dieser Art vorkommen
    quellen = [e['thema'] for e in a['etappen_im_bestand']] + [v['thema'] for v in a.get('vorkommen_im_bestand', [])] + [b['thema'] for b in k['beleg']]
    for tr in [a['treppe']] + [w['treppe'] for w in a.get('weitere_treppen', [])]:
        for u in tr:
            if u.get('zusatz'): continue
            if not any(thema(q) and re.search(r'(?<![\w²³/])%s(?![\w²³/])' % re.escape(u['einheit']), thema(q)[1]) for q in quellen): f('%s: Einheit %s nicht im Bestand gefunden und nicht als „zusatz“ markiert' % (art, u['einheit']))
if not any(u.get('zusatz') for a in arten if a['art'] == 'Volumen und Hohlmaße' for w in a['weitere_treppen'] for u in w['treppe']): f('Zusatz-Markierung hl/dl/cl fehlt')

# ---------- 6 Kennungen der Regeln ----------
md = (repo / 'inhalte/mathe-profi/regeln-uebersicht/inhalt.md').read_text(encoding='utf-8')
kurz = json.loads((repo / 'inhalte/mathe-profi/regeln-uebersicht/texte8/kurzbeschreibungen.json').read_text(encoding='utf-8'))['eintraege']
schluessel = {e['entwurf_schluessel']: e for e in kurz}
for a in arten:
    if not a['regeln']: f('%s: keine regeln' % a['art'])
    for r in a['regeln']:
        k = r['kennung']
        if k in schluessel:
            if schluessel[k]['kennung'] != r.get('lang') or schluessel[k]['name'] != r['name']: f('%s: Kennung %s passt nicht zu kurzbeschreibungen.json' % (a['art'], k))
        else:
            m = re.search(r'^\| %s \| \*\*(.+?)\*\* \|' % re.escape(k), md, re.M)
            if not m or m.group(1) != r['name']: f('%s: Regel %s (%s) nicht in inhalt.md' % (a['art'], k, r['name']))
        if not r.get('passt'): f('%s: Regel %s ohne Begründung (passt)' % (a['art'], k))

# ---------- 7 tafel.md ----------
tafel = (hier / 'tafel.md').read_text(encoding='utf-8')
if len(tafel.splitlines()) > 90: f('tafel.md zu lang für eine Seite (%d Zeilen)' % len(tafel.splitlines()))
for a in arten:
    if a['darstellung'] not in tafel: f('tafel.md: Treppe %s fehlt' % a['darstellung'])
    for w in a.get('weitere_treppen', []):
        if w['darstellung'] not in tafel: f('tafel.md: Treppe %s fehlt' % w['darstellung'])
    for b in a['beispiele']:
        if '%s = %s' % (b['von'], b['nach']) not in tafel: f('tafel.md: Beispiel %s = %s fehlt' % (b['von'], b['nach']))
    if a['merksatz'] not in tafel: f('tafel.md: Merksatz %s fehlt' % a['art'])
for pfad, t in alle_texte({'t': tafel}):
    for m in re.finditer(r'(?<![\w,])(%s)(?: = (%s))+' % (Q, Q), t):
        try: ok = gleich(m.group(0))
        except KeyError: continue
        except ValueError as e: f('tafel.md: %s' % e); continue
        zaehler['gleichungen'] += 1
        if not ok: f('tafel.md: Gleichung falsch: ' + m.group(0))
    if re.search(r'(?<![\d,.])\d{4,}(?!\d)', t): f('tafel.md: Zahl ab 4 Stellen ohne Tausenderleerzeichen')

if fehler:
    print('FEHLER (%d):' % len(fehler)); [print(' -', x) for x in fehler]; sys.exit(1)
print('%d Größenarten, %d Beispiele, %d Rechnungen, %d Faktoren und %d Gleichungen gerechnet, %d Stolperstellen' % (len(arten), zaehler['beispiele'], zaehler['rechnungen'], zaehler['faktoren'], zaehler['gleichungen'], zaehler['stolperstellen']))
print('OK')
