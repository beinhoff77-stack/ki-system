#!/usr/bin/env python3
"""W2 – Prüfung einer Runde „Verstehen in Tests“ (Stufe 1, inhalte/mathe-profi/vtest-1/plan.md) und gemeinsame Regeln für W1 (tools/vtest_sql.py).

Aufruf:  python3 -I tools/vtest_pruefen.py --runde 1               -> prüft inhalte/mathe-profi/vtest-1/*.json gegen auswahl.json (Runde 1)
         python3 -I tools/vtest_pruefen.py --runde 1 --nur-auswahl -> prüft nur die Auswahl der Verstehens-Lernziele (alle Runden)
         Testumgebung: --auswahl DATEI --ordner DIR --plan DATEI --themen DIR (statt der Vorgaben unter inhalte/)
Rückgabe 0 = keine FEHLER (HINWEISE sind zum Nachsehen von Hand), 1 = FEHLER.

Was geprüft wird (FEHLER = W1 baut kein Paket):
  Auswahl (auswahl.json): je Einheit genau ⌈n/2⌉ Verstehens-Lernziele (n = Lernziele der Einheit, Reihenfolge wie in rollend-einheiten.json „lz“),
    nie zwei Rechen-Lernziele nebeneinander, nie drei Verstehens-Lernziele nebeneinander; jedes Lernziel hat eine Test-Aufgabe im Bestand (inhalte/themen).
  Vollständigkeit: je Verstehens-Lernziel der Runde genau `mengen.test` Test-, mindestens `mengen.korrektur` Korrektur- und `mengen.sicherung`
    Sicherungs-Aufgaben (höchstens zwei mehr); keine Aufgabe für ein Rechen-Lernziel oder eine Einheit außerhalb der Runde; Kennungen eindeutig (<KÜRZEL>-nnn).
  Verbote (aus inhalte/plan/neuer-stil/didaktik.md, geschärft; Entscheidungen 28.11.):
    V1 kein Lückenweg (form lueckenweg)                       V2 zaehlt muss „ja“ sein (nie „nein“, nie leer)
    V3 Stufe nur 2 oder 3                                     V4 typ (Feld g) Pflicht, einer der 13 Übungs-Typen, nicht knobel/direkt
    V5 Verstehens-Aufgabe: typ in V-Typen ODER form in V-Formen (didaktik.md Abschnitt 2; anwenden nur mit typ transfer)
    V6 Antworttyp nur zahl, luecken, auswahl (text/markierung/bedingung erst in einer späteren Stufe)
    V7 auswahl: mindestens 4 verschiedene Möglichkeiten (Ratechance höchstens 25 %), Lösungsindex gültig
    V8 Fehler-Detektiv (form fehler_detektiv oder typ fehler): ENTWEDER luecken „Zeile □ … richtig □“ (erste Lücke = Zeilennummer 1..n, mindestens
       ein Berichtigungswert, mindestens 3 Zeilen) ODER auswahl mit mindestens 4 Zeilen im Text und mindestens 4 Möglichkeiten, die jede eine Zeile UND
       eine Begründung nennen („In Zeile 2, weil …“); sonst verboten (keine reine Zeilenwahl, kein „in keiner Zeile“ als einzige Begründung)
    V9 keine Toleranz in der Lösung (verlangte Rundung = genau ein richtiger Wert)
    V10 Lösung nachrechenbar: „loesung_rechnung“ (zahl: ein Ausdruck, luecken: je Lücke einer) ergibt genau den Lösungswert (mit „runden“: auf so viele
       Nachkommastellen kaufmännisch gerundet)
    V11 Fehlbilder: zahl/luecken mindestens 2, jedes mit „rechnung“, die genau die Fehlantwort ergibt; auswahl: zu JEDER falschen Möglichkeit ein
       Fehlbild (Index + Beschreibung; ist die Möglichkeit eine Zahl, auch „rechnung“); alle von tools/regelbezug_sql.fehlbilder übernehmbar
    V12 Regel-Kennung aus inhalte/mathe-profi/regeln-uebersicht/kennungen.json (leer nur, wenn die Lernkarte in regelbezug-lernkarten.json offen ist)
    V13 Lehrplan: Feld „lehrplan“ = LehrplanPLUS-Lernbereich der Einheit (inhalte/themenliste.json, gym_by)
    V14 Lösungsweg (w) und Abgrenzung (Satz: wie sich die Aufgabe von den Übungen der Etappe unterscheidet) nicht leer
    V15 nicht ähnlich (siehe aehnlich()): weder einer Aufgabe derselben Etappe im Bestand (inhalte/themen: alle Vorräte; inhalte/mathe-profi/rollend-*:
       Übungen) noch einer anderen neuen Aufgabe derselben Etappe
    V16 Teilfähigkeit t aus „tf“ der Einheit oder die der alten Test-Aufgabe; l = Lernkarte; p = pool
"""
import glob
import json
import math
import re
import sys
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WURZEL / 'tools'))
import regelbezug_sql as R  # noqa: E402
import vorrat_pruefen as VP  # noqa: E402

POOLS = ('test', 'korrektur', 'sicherung')
TYPEN = ('direkt', 'erkennen', 'mehrschritt', 'einkleidung', 'umkehr', 'darstellung', 'rueckwaerts', 'verknuepfen', 'begruenden', 'fehler',
         'transfer', 'parameter', 'pruefung')
V_TYPEN = ('begruenden', 'fehler', 'darstellung', 'parameter', 'umkehr', 'rueckwaerts', 'transfer')          # didaktik.md Abschnitt 2
V_FORMEN = ('fehler_detektiv', 'verfahren_waehlen', 'zwei_wege', 'bruecke', 'umkehren', 'viele_antworten')
FORMEN = ('lueckenweg', 'fehler_detektiv', 'verfahren_waehlen', 'zwei_wege', 'umkehren', 'bruecke', 'anwenden', 'viele_antworten')
ANTWORTTYPEN = ('zahl', 'luecken', 'auswahl')
FELDER = ('l', 't', 'p', 's', 'g', 'y', 'f', 'a', 'o', 'h', 'w')
SCHWELLE_WORT = 0.75     # Jaccard der Wörter (ohne Zahlen, ab 3 Buchstaben) ab hier „gleicher Wortlaut“
SCHWELLE_WORT_ZAHL = 0.5 # ... und ab hier zusammen mit fast gleichen Zahlen


def lesen(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))


def basis(schluessel):
    """Themen-Datei einer Teil-Einheit (…_teil2) ist die der Grund-Einheit (bestand.md f))."""
    return re.sub(r'_teil\d+$', '', schluessel)


# ---------- Rechnen ----------
def rechne(ausdruck):
    """Exakter Wert (Fraction) eines Rechenausdrucks; erlaubt · × : − Komma, Klammern, ², ³, ** und abs(). Sonst ValueError."""
    if not isinstance(ausdruck, str) or not ausdruck.strip():
        raise ValueError('leer')
    s = VP.text_zu_ausdruck(ausdruck)
    if re.search(r'[A-Za-z_]', s.replace('abs(', '')):
        raise ValueError(f'Buchstaben in „{ausdruck}“')
    return VP.rechne(s)


def gerundet(wert, stellen):
    if stellen is None: return Fraction(wert)
    q = Decimal(wert.numerator) / Decimal(wert.denominator)
    return Fraction(q.quantize(Decimal(1).scaleb(-int(stellen)), rounding=ROUND_HALF_UP))


def gleich(ausdruck, soll, stellen=None):
    """(ok, Text) – ergibt der Ausdruck genau den Sollwert?"""
    try:
        v = gerundet(rechne(ausdruck), stellen)
    except Exception as ex:  # noqa: BLE001
        return False, f'„{ausdruck}“ lässt sich nicht ausrechnen ({ex.__class__.__name__})'
    try:
        s = Fraction(str(soll))
    except Exception:  # noqa: BLE001
        return False, f'Sollwert {soll!r} ist keine Zahl'
    return v == s, f'„{ausdruck}“ ergibt {float(v):g}' + (f' (gerundet auf {stellen})' if stellen is not None else '') + f', erwartet {soll}'


# ---------- Ähnlichkeit (V15) ----------
def _text(a):
    f = a.get('f') or {}
    teile = [str(f.get('text', '')), str(f.get('schablone', ''))]
    if isinstance(a.get('a'), list): teile += [str(x) for x in a['a']]
    g = f.get('grafik')
    if g is not None: teile.append(json.dumps(g, ensure_ascii=False, sort_keys=True))
    return ' '.join(teile)


def merkmale(a):
    t = VP.ohne_tausender(_text(a)).lower()
    zahlen = Counter(m.replace(',', '.') for m in re.findall(r'\d+(?:[.,]\d+)?', t))
    woerter = {w for w in re.findall(r'[a-zäöüß]{3,}', t)}
    norm = re.sub(r'\s+', ' ', re.sub(r'[^\w]+', ' ', t)).strip()
    return norm, zahlen, woerter


def aehnlich(a, b):
    """Einfacher, dokumentierter Vergleich zweier Aufgaben (Feld f/a). Rückgabe: Grund oder None.
    (1) gleicher Text nach Normierung; (2) mindestens 3 Zahlen und dieselben Zahlen (als Menge mit Vielfachheit) – „nur andere Zahlen“ andersherum:
    gleiche Zahlen, anderer Wortlaut ist dieselbe Rechnung; (3) Wörter (ab 3 Buchstaben, ohne Zahlen) zu mindestens 75 % gleich (Jaccard) bei
    mindestens 6 Wörtern – „nur andere Zahlen“; (4) Wörter zu mindestens 50 % gleich UND mindestens 80 % der Zahlen gemeinsam."""
    na, za, wa = merkmale(a)
    nb, zb, wb = merkmale(b)
    if na and na == nb: return 'gleicher Text'
    if sum(za.values()) >= 3 and za == zb: return f'dieselben Zahlen ({", ".join(sorted(za))})'
    ja = len(wa & wb) / len(wa | wb) if (wa | wb) else 0
    if min(len(wa), len(wb)) >= 6 and ja >= SCHWELLE_WORT: return f'fast gleicher Wortlaut (Wörter {ja:.0%} gleich)'
    gem = sum((za & zb).values())
    if ja >= SCHWELLE_WORT_ZAHL and sum(za.values()) >= 2 and gem >= 0.8 * max(sum(za.values()), sum(zb.values())):
        return f'ähnlicher Wortlaut ({ja:.0%}) und fast dieselben Zahlen'
    return None


# ---------- Laden ----------
def kontext(runde=None, auswahl_datei=None, ordner=None, plan_datei=None, themen_dir=None, rollend_glob=None, themenliste=None):
    auswahl_datei = Path(auswahl_datei or WURZEL / 'inhalte/mathe-profi/vtest-1/auswahl.json')
    aw = lesen(auswahl_datei)
    if runde is None: runde = aw.get('vorgabe_runde', 1)
    rinfo = aw['runden'][str(runde)]
    ordner = Path(ordner or WURZEL / rinfo['ordner'])
    plan = lesen(plan_datei or WURZEL / 'inhalte/plan/rollend-einheiten.json')['einheiten']
    themen_dir = Path(themen_dir or WURZEL / 'inhalte/themen')
    tl = {t['thema_schluessel']: t for t in lesen(themenliste or WURZEL / 'inhalte/themenliste.json')}
    kenn = {k['kennung'] for k in lesen(WURZEL / 'inhalte/mathe-profi/regeln-uebersicht/kennungen.json')['kennungen']}
    rbl = lesen(WURZEL / 'inhalte/plan/regelbezug-lernkarten.json')['themen']
    bestand = defaultdict(list)     # (schluessel, lz) -> [(Quelle, Aufgabe)] (alle Vorräte aus inhalte/themen, Übungen aus den Runden)
    alt_test = {}                   # (schluessel, lz) -> alte Test-Aufgabe (inhalte/themen)
    for e in aw['einheiten']:
        s = e['schluessel']
        tf = themen_dir / f'{basis(s)}.json'
        if not tf.exists(): continue
        for i, a in enumerate(lesen(tf)['aufgaben']):
            if a.get('l') not in plan.get(s, {}).get('lz', []): continue
            bestand[(s, a['l'])].append((f'{tf.name}#{i} ({a["p"]})', a))
            if a['p'] == 'test':
                if (s, a['l']) in alt_test: alt_test[(s, a['l'])] = 'mehrere'
                else: alt_test[(s, a['l'])] = a
    for p in sorted(glob.glob(rollend_glob or str(WURZEL / 'inhalte/mathe-profi/rollend-*/*.json'))):
        try: d = lesen(p)
        except Exception: continue  # noqa: BLE001
        for x in d.get('aufgaben', []):
            if isinstance(x, dict) and 'aufgabe' in x and (x.get('thema'), x['aufgabe'].get('l')) in bestand:
                bestand[(x['thema'], x['aufgabe']['l'])].append((f'{Path(p).parent.name}/{x.get("kennung")}', x['aufgabe']))
    eintraege = []
    if ordner.exists():
        for p in sorted(ordner.glob('*.json')):
            if p.name == auswahl_datei.name and p.resolve() == auswahl_datei.resolve(): continue
            d = lesen(p)
            if 'aufgaben' not in d: continue
            for x in d['aufgaben']: eintraege.append((p.name, x))
    return dict(runde=int(runde), kuerzel=rinfo['kuerzel'], aw=aw, ordner=ordner, plan=plan, tl=tl, kenn=kenn, rbl=rbl, bestand=bestand,
                alt_test=alt_test, eintraege=eintraege, mengen=aw['mengen'])


# ---------- Auswahl ----------
def auswahl_pruefen(k):
    fehler, zeilen = [], []
    gesehen = set()
    for e in k['aw']['einheiten']:
        s = e['schluessel']
        if s in gesehen: fehler.append(f'Auswahl: Einheit {s} doppelt'); continue
        gesehen.add(s)
        pe = k['plan'].get(s)
        if pe is None: fehler.append(f'Auswahl: Einheit {s} fehlt in rollend-einheiten.json'); continue
        if pe['id'] != e['id']: fehler.append(f'Auswahl: Einheit {s} hat id {pe["id"]}, nicht {e["id"]}')
        lz = pe['lz']
        v = e['verstehen']
        unbekannt = [x for x in v if x not in lz]
        if unbekannt: fehler.append(f'Auswahl {s}: Lernziele {unbekannt} gibt es nicht (lz: {lz})')
        if len(set(v)) != len(v): fehler.append(f'Auswahl {s}: Lernziel doppelt')
        muster = ''.join('V' if x in v else 'R' for x in lz)
        soll = math.ceil(len(lz) / 2)
        if muster.count('V') != soll: fehler.append(f'Auswahl {s}: {muster.count("V")} Verstehens-Lernziele, Soll ⌈{len(lz)}/2⌉ = {soll} ({muster})')
        if 'RR' in muster: fehler.append(f'Auswahl {s}: zwei Rechen-Lernziele nebeneinander ({muster})')
        if 'VVV' in muster: fehler.append(f'Auswahl {s}: drei Verstehens-Lernziele nebeneinander ({muster})')
        for x in lz:
            a = k['alt_test'].get((s, x))
            if a is None: fehler.append(f'Auswahl {s}/{x}: keine Test-Aufgabe im Bestand (inhalte/themen/{basis(s)}.json)')
            elif a == 'mehrere': fehler.append(f'Auswahl {s}/{x}: mehrere Test-Aufgaben im Bestand – welche ersetzt wird, ist nicht eindeutig')
        if not (e.get('begruendung') or '').strip(): fehler.append(f'Auswahl {s}: Begründung fehlt')
        zeilen.append((e.get('runde'), s, e['id'], muster, len(lz), muster.count('V')))
    return fehler, zeilen


# ---------- eine Aufgabe ----------
def zeilen_im_text(a):
    return [int(i) for i, _ in VP.ZEILE.findall((a.get('f') or {}).get('text', ''))]


def aufgabe_pruefen(x, s, l, k, alt):
    """Fehler und Hinweise einer Aufgabe (Verbote V1–V16). x = Eintrag der Rundendatei."""
    f, h = [], []
    a = x.get('aufgabe') or {}
    kn = x.get('kennung', '?')
    pool = x.get('pool')
    if pool not in POOLS: f.append(f'{kn}: pool „{pool}“ (erlaubt: {", ".join(POOLS)})')
    if a.get('p') != pool: f.append(f'{kn}: aufgabe.p „{a.get("p")}“ ≠ pool „{pool}“')
    if a.get('l') != l: f.append(f'{kn}: aufgabe.l „{a.get("l")}“ ≠ lernkarte „{l}“')
    form = x.get('form')
    if form is not None and form not in FORMEN: f.append(f'{kn}: form „{form}“ unbekannt')
    if form == 'lueckenweg': f.append(f'{kn}: V1 Lückenweg ist im Test verboten (Gerüst)')
    if x.get('zaehlt') != 'ja': f.append(f'{kn}: V2 zaehlt muss „ja“ sein (ist {x.get("zaehlt")!r})')
    st = a.get('s')
    if st not in (2, 3) or isinstance(st, bool): f.append(f'{kn}: V3 Stufe {st!r} – im Test nur 2 oder 3')
    if x.get('stufe') is not None and x.get('stufe') != st: f.append(f'{kn}: stufe {x.get("stufe")} ≠ aufgabe.s {st}')
    g = a.get('g')
    if not g: f.append(f'{kn}: V4 typ (aufgabe.g) fehlt – Pflicht')
    elif g not in TYPEN: f.append(f'{kn}: V4 typ „{g}“ unbekannt oder im Test verboten (erlaubt: {", ".join(TYPEN)}; nicht knobel)')
    elif g == 'direkt': f.append(f'{kn}: V4 typ direkt = reine Reproduktion, im Test verboten')
    if g and not (g in V_TYPEN or form in V_FORMEN or (form == 'anwenden' and g == 'transfer')):
        f.append(f'{kn}: V5 keine Verstehens-Aufgabe (typ {g}, form {form}); nötig: typ in {"/".join(V_TYPEN)} oder form in {"/".join(V_FORMEN)}')
    y = a.get('y')
    o = a.get('o') or {}
    opts = a.get('a')
    if y not in ANTWORTTYPEN: f.append(f'{kn}: V6 Antworttyp „{y}“ im Test nicht erlaubt (nur {", ".join(ANTWORTTYPEN)})')
    if 'toleranz' in o: f.append(f'{kn}: V9 Toleranz ist verboten (verlangte Rundung: genau ein Wert)')
    fz = a.get('f') or {}
    if not isinstance(fz.get('text'), str) or not fz['text'].strip(): f.append(f'{kn}: Aufgabentext fehlt')
    if y == 'auswahl':
        if not isinstance(opts, list) or len(opts) < 4: f.append(f'{kn}: V7 Auswahl mit {len(opts) if isinstance(opts, list) else 0} Möglichkeiten – im Test mindestens 4')
        elif len({str(z).strip() for z in opts}) != len(opts): f.append(f'{kn}: V7 zwei gleiche Möglichkeiten')
        if not isinstance(o.get('index'), int) or not isinstance(opts, list) or not 0 <= o['index'] < len(opts): f.append(f'{kn}: Lösungsindex ungültig')
    elif opts is not None:
        f.append(f'{kn}: Feld a (Möglichkeiten) nur bei auswahl')
    if y == 'zahl':
        if isinstance(o.get('wert'), bool) or not isinstance(o.get('wert'), (int, float)): f.append(f'{kn}: zahl ohne Zahlwert o.wert')
    if y == 'luecken':
        w = o.get('werte')
        if not isinstance(w, list) or not w or any(isinstance(v, bool) or not isinstance(v, int) for v in w):
            f.append(f'{kn}: luecken braucht ganze Zahlen in o.werte (Bewertung nimmt nur ganze Zahlen)')
        elif str(fz.get('schablone', '')).count('□') != len(w): f.append(f'{kn}: Schablone hat {str(fz.get("schablone", "")).count("□")} Felder □, Lösung {len(w)} Werte')
    # V8 Fehler-Detektiv
    if form == 'fehler_detektiv' or g == 'fehler':
        zl = zeilen_im_text(a)
        if y == 'luecken':
            w = o.get('werte') or []
            if 'Zeile' not in str(fz.get('schablone', '')): f.append(f'{kn}: V8 Fehler-Detektiv als luecken: Schablone muss „Zeile □“ enthalten')
            if len(zl) < 3: f.append(f'{kn}: V8 Fehler-Detektiv: mindestens 3 Zeilen („Zeile 1: …“), gefunden {len(zl)}')
            if len(w) < 2: f.append(f'{kn}: V8 Fehler-Detektiv: Zeile nennen UND richtigstellen (mindestens 2 Lücken)')
            elif zl and w[0] not in zl: f.append(f'{kn}: V8 erste Lücke ({w[0]}) ist keine Zeilennummer des Textes {zl}')
        elif y == 'auswahl':
            if len(zl) < 4: f.append(f'{kn}: V8 Fehler-Detektiv als Auswahl: mindestens 4 Zeilen im Text, gefunden {len(zl)}')
            if isinstance(opts, list) and not all(re.search(r'Zeile \d', str(z)) and re.search(r'\b(weil|denn|da)\b', str(z)) for z in opts):
                f.append(f'{kn}: V8 Fehler-Detektiv als Auswahl: JEDE Möglichkeit nennt eine Zeile UND eine Begründung („In Zeile 2, weil …“)')
        else:
            f.append(f'{kn}: V8 Fehler-Detektiv nur als luecken (Zeile + richtig) oder Auswahl mit Begründung')
        if y in ('luecken', 'auswahl') and zl:
            err = (o.get('werte') or [None])[0] if y == 'luecken' else None
            if err is None and y == 'auswahl' and isinstance(opts, list) and isinstance(o.get('index'), int) and 0 <= o['index'] < len(opts):
                m = re.search(r'Zeile (\d+)', str(opts[o['index']])); err = int(m.group(1)) if m else None
            for i, t in VP.ZEILE.findall(fz.get('text', '')):
                for kette, ok in VP.gleichungsketten(t):
                    if err is not None and int(i) < err and not ok: h.append(f'{kn}: Zeile {i} vor der Fehlerzeile {err} rechnet falsch: {kette}')
    # V10 Lösung nachrechenbar
    rd = x.get('runden')
    lr = x.get('loesung_rechnung')
    if y == 'zahl' and isinstance(o.get('wert'), (int, float)):
        ok, t = gleich(lr, o['wert'], rd) if isinstance(lr, str) else (False, 'loesung_rechnung fehlt (ein Ausdruck)')
        if not ok: f.append(f'{kn}: V10 Lösung nicht nachgerechnet: {t}')
    elif y == 'luecken' and isinstance(o.get('werte'), list):
        if not isinstance(lr, list) or len(lr) != len(o['werte']): f.append(f'{kn}: V10 loesung_rechnung: je Lücke ein Ausdruck ({len(o["werte"])})')
        else:
            for i, (ex, w) in enumerate(zip(lr, o['werte']), 1):
                ok, t = gleich(ex, w, rd)
                if not ok: f.append(f'{kn}: V10 Lücke {i}: {t}')
    # V11 Fehlbilder
    fb = x.get('fehlbilder') or []
    if y in ('zahl', 'luecken'):
        if len(fb) < 2: f.append(f'{kn}: V11 mindestens 2 Fehlbilder (je eine nachrechenbare Fehlrechnung), vorhanden {len(fb)}')
        for j, b in enumerate(fb, 1):
            if not isinstance(b.get('rechnung'), str): f.append(f'{kn}: V11 Fehlbild {j}: „rechnung“ fehlt'); continue
            ok, t = gleich(b['rechnung'], b.get('antwort'), b.get('runden', rd))
            if not ok: f.append(f'{kn}: V11 Fehlbild {j}: {t}')
    elif y == 'auswahl' and isinstance(opts, list) and isinstance(o.get('index'), int):
        idx = {b.get('index') for b in fb}
        fehlt = [i for i in range(len(opts)) if i != o['index'] and i not in idx]
        if fehlt: f.append(f'{kn}: V11 zu den falschen Möglichkeiten {fehlt} fehlt ein Fehlbild')
        for b in fb:
            i = b.get('index')
            if isinstance(i, int) and 0 <= i < len(opts) and re.fullmatch(r'\s*[−-]?\d+(?:[.,]\d+)?\s*', str(opts[i])):
                if not isinstance(b.get('rechnung'), str): f.append(f'{kn}: V11 Möglichkeit {i} ist eine Zahl: Fehlbild braucht „rechnung“')
                else:
                    ok, t = gleich(b['rechnung'], str(opts[i]).strip().replace(',', '.').replace('−', '-'))
                    if not ok: f.append(f'{kn}: V11 Fehlbild zu Möglichkeit {i}: {t}')
    for j, b in enumerate(fb, 1):
        if not (b.get('beschreibung') or '').strip(): f.append(f'{kn}: V11 Fehlbild {j}: Beschreibung fehlt')
    row = zeile(x)
    gut, weg = R.fehlbilder(x, row)
    if weg: f.append(f'{kn}: V11 Fehlbilder nicht übernehmbar: {dict(weg)}')
    # V12 Regel
    rg = x.get('regel')
    lk = ((k['rbl'].get(basis(s)) or {}).get('lernkarten') or {}).get(l) or {}
    if rg is None:
        if lk.get('regel'): f.append(f'{kn}: V12 Regel fehlt (Lernkarte hat {lk["regel"]})')
    elif rg not in k['kenn']: f.append(f'{kn}: V12 Regel „{rg}“ steht nicht in regeln-uebersicht/kennungen.json')
    elif lk.get('regel') and rg != lk['regel'] and rg not in (lk.get('weitere') or []):
        h.append(f'{kn}: Regel {rg} weicht von der Lernkarte ab ({lk["regel"]})')
    # V13 Lehrplan
    lb = (k['plan'].get(s) or {}).get('lernbereich') or ((k['tl'].get(basis(s)) or {}).get('lernbereich') or {}).get('gym_by')
    if not lb: f.append(f'{kn}: V13 Lernbereich der Einheit unbekannt (themenliste)')
    elif x.get('lehrplan') != lb: f.append(f'{kn}: V13 lehrplan „{x.get("lehrplan")}“ – soll „{lb}“')
    # V14
    if not (a.get('w') or '').strip(): f.append(f'{kn}: V14 Lösungsweg (w) fehlt')
    if not (x.get('abgrenzung') or '').strip(): f.append(f'{kn}: V14 Abgrenzung zu den Übungen der Etappe fehlt')
    # V16
    tf = set((k['plan'].get(s) or {}).get('tf') or []) | ({alt.get('t')} if isinstance(alt, dict) else set())
    if a.get('t') not in tf: f.append(f'{kn}: V16 Teilfähigkeit „{a.get("t")}“ nicht in tf der Einheit {sorted(x for x in tf if x)}')
    if rd is not None and (not isinstance(rd, int) or isinstance(rd, bool) or not 0 <= rd <= 6): f.append(f'{kn}: runden muss eine ganze Zahl 0..6 sein')
    if rd is not None and y == 'zahl' and isinstance(o.get('wert'), (int, float)) and Fraction(str(o['wert'])) != gerundet(Fraction(str(o['wert'])), rd):
        f.append(f'{kn}: V9 Lösung {o["wert"]} hat mehr Nachkommastellen als verlangt ({rd})')
    if y == 'zahl' and re.search(r'\brunde|gerundet', fz.get('text', ''), re.I) and rd is None:
        h.append(f'{kn}: Text verlangt Runden, Feld „runden“ fehlt (Fehlbilder/Lösung werden exakt verglichen)')
    return f, h


def zeile(x):
    """Aufgaben-JSON für schule.aufgaben_einfuegen (ohne r)."""
    a = x.get('aufgabe') or {}
    r = {k: a[k] for k in FELDER if a.get(k) is not None}
    r['form'], r['zaehlt'] = x.get('form'), x.get('zaehlt')
    return r


# ---------- Runde ----------
def runde_pruefen(k):
    fehler, hinweise = auswahl_pruefen(k)[0], []
    ein = {e['schluessel']: e for e in k['aw']['einheiten'] if e.get('runde') == k['runde']}
    if not ein: fehler.append(f'Runde {k["runde"]}: keine Einheit in auswahl.json')
    kenn = Counter(x.get('kennung') for _, x in k['eintraege'])
    for kk, n in kenn.items():
        if n > 1: fehler.append(f'Kennung {kk} kommt {n}-mal vor')
        if not re.fullmatch(re.escape(k['kuerzel']) + r'-\d{3}', str(kk)): fehler.append(f'Kennung {kk}: Schema {k["kuerzel"]}-nnn')
    je = defaultdict(list)
    for datei, x in k['eintraege']:
        s, l = x.get('thema'), x.get('lernkarte')
        if s not in ein: fehler.append(f'{x.get("kennung")}: Einheit {s} gehört nicht zu Runde {k["runde"]}'); continue
        if l not in ein[s]['verstehen']: fehler.append(f'{x.get("kennung")}: Lernziel {s}/{l} ist kein Verstehens-Lernziel der Auswahl (Rechen-Lernziele bleiben in Stufe 1 unverändert)'); continue
        if datei != f'{s}.json': hinweise.append(f'{x.get("kennung")}: steht in {datei}, erwartet {s}.json')
        je[(s, l)].append(x)
    for s, e in ein.items():
        for l in e['verstehen']:
            xs = je.get((s, l), [])
            c = Counter(x.get('pool') for x in xs)
            m = k['mengen']
            if c['test'] != m['test']: fehler.append(f'{s}/{l}: {c["test"]} Test-Aufgaben, Soll genau {m["test"]}')
            for p in ('korrektur', 'sicherung'):
                if not m[p] <= c[p] <= m[p] + 2: fehler.append(f'{s}/{l}: {c[p]} {p}-Aufgaben, Soll {m[p]} (höchstens {m[p] + 2})')
            alt = k['alt_test'].get((s, l))
            for x in xs:
                ff, hh = aufgabe_pruefen(x, s, l, k, alt)
                fehler += ff; hinweise += hh
            # V15 Ähnlichkeit: gegen den Bestand der Etappe und untereinander
            for x in xs:
                a = x.get('aufgabe') or {}
                for q, b in k['bestand'].get((s, l), []):
                    gr = aehnlich(a, b)
                    if gr: fehler.append(f'{x.get("kennung")}: V15 zu ähnlich zu {q}: {gr}')
            for i in range(len(xs)):
                for j in range(i + 1, len(xs)):
                    gr = aehnlich(xs[i].get('aufgabe') or {}, xs[j].get('aufgabe') or {})
                    if gr: fehler.append(f'{xs[i].get("kennung")}/{xs[j].get("kennung")}: V15 zu ähnlich untereinander: {gr}')
    return fehler, hinweise, je, ein


def optionen(argv):
    def wert(n):
        if n in argv:
            i = argv.index(n)
            if i + 1 >= len(argv): sys.exit(f'{n} braucht einen Wert')
            return argv[i + 1]
        return None
    r = wert('--runde')
    return dict(runde=int(r) if r else None, auswahl_datei=wert('--auswahl'), ordner=wert('--ordner'), plan_datei=wert('--plan'),
                themen_dir=wert('--themen'), rollend_glob=wert('--rollend'), themenliste=wert('--themenliste'))


def main():
    argv = sys.argv[1:]
    k = kontext(**optionen(argv))
    if '--nur-auswahl' in argv:
        fehler, zeilen = auswahl_pruefen(k)
        print('| Runde | Einheit | id | Muster (Lernziele in Reihenfolge, V = Verstehen) | Lernziele | V |\n|---|---|---|---|---|---|')
        for z in zeilen: print('| ' + ' | '.join(map(str, z)) + ' |')
        print(f'zusammen {sum(z[5] for z in zeilen)} Verstehens-Lernziele von {sum(z[4] for z in zeilen)}')
    else:
        fehler, hinweise, je, ein = runde_pruefen(k)
        print(f'Runde {k["runde"]} ({k["kuerzel"]}, {k["ordner"]}): {len(k["eintraege"])} Aufgaben, {len(ein)} Einheiten')
        for s, e in ein.items():
            for l in e['verstehen']:
                xs = je.get((s, l), [])
                print(f'  {s}/{l}: ' + ', '.join(f'{p} {sum(1 for x in xs if x.get("pool") == p)}' for p in POOLS)
                      + f'; Stufen {dict(Counter((x.get("aufgabe") or {}).get("s") for x in xs))}')
        if hinweise:
            print(f'== {len(hinweise)} HINWEISE (von Hand nachsehen)')
            for t in hinweise: print('  ' + t)
    if fehler:
        print(f'== {len(fehler)} FEHLER')
        for t in fehler: print('  ' + t)
        return 1
    print('OK – keine Fehler')
    return 0


if __name__ == '__main__':
    sys.exit(main())
