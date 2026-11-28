#!/usr/bin/env python3
"""Bestandsberichtigung 1: baut vorschlag.json aus den Bestandsaufgaben (nur LESEND; keine Quelldatei wird geändert).

Aufruf:  python3 -I inhalte/mathe-profi/bestand-berichtigung-1/bauen.py            -> schreibt vorschlag.json, prüft alles, meldet OK
         python3 -I inhalte/mathe-profi/bestand-berichtigung-1/bauen.py --pruefen  -> prüft nur (vorschlag.json muss dem Neuaufbau gleichen)

Je Vorschlag: die vollständige berichtigte Aufgabe im Format der Quelldatei (Wrapper wie rollend-*: kennung, thema, lernkarte, stufe, typ, form,
antwortform, regel, zaehlt, fehlbilder, aufgabe) plus `ersetzt` (Kennung/Platz/alter Fragetext) und `grund`.
Geprüft wird: Nachrechnung (tools/inhalt_pruefen.pruefe_antwort), Fehlbild nie gleich der richtigen Antwort, Fehlbilder paarweise verschieden,
Aufgabentyp g passt zur Stufe, kein Fragetext doppelt in der Einheit (Zahlen durch # ersetzt), Quelldateien unverändert (md5 gegen git HEAD).
"""
import copy
import glob
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent.parent
HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(WURZEL / 'tools'))
import inhalt_pruefen as IP  # noqa: E402

STAND = '2026-11-28'
TYP_STUFE = {1: ('direkt', 'erkennen'), 2: ('mehrschritt', 'einkleidung', 'umkehr', 'darstellung'),
             3: ('rueckwaerts', 'verknuepfen', 'begruenden', 'fehler', 'transfer', 'parameter', 'pruefung')}


# ---------- Quellen ----------
def laden():
    """Alle Aufgaben aus inhalte/themen und rollend-*: Liste von Dicts (datei, idx, thema, kennung, a, roll)."""
    out = []
    for f in sorted(glob.glob(str(WURZEL / 'inhalte/themen/*.json'))):
        d = json.loads(Path(f).read_text(encoding='utf-8'))
        for i, a in enumerate(d['aufgaben']):
            out.append(dict(datei=str(Path(f).relative_to(WURZEL)), idx=i, thema=d['thema_schluessel'], kennung=None, a=a, roll=None))
    for f in sorted(glob.glob(str(WURZEL / 'inhalte/mathe-profi/rollend-*/*.json'))):
        d = json.loads(Path(f).read_text(encoding='utf-8'))
        if not isinstance(d, dict) or 'aufgaben' not in d: continue
        for i, e in enumerate(d['aufgaben']):
            out.append(dict(datei=str(Path(f).relative_to(WURZEL)), idx=i, thema=e.get('thema'), kennung=e.get('kennung'), a=e['aufgabe'], roll=e))
    return out


ALLE = laden()
KENN = {e['kennung']: e for e in ALLE if e['kennung']}
PLAN = json.loads((WURZEL / 'inhalte/plan/rollend-einheiten.json').read_text(encoding='utf-8'))['einheiten']


def themen(datei, idx):
    return next(e for e in ALLE if e['datei'] == datei and e['idx'] == idx and not e['roll'])


def norm(t):
    return re.sub(r'\d+([.,]\d+)?', '#', re.sub(r'\s+', ' ', t)).strip()


def fb(antwort, beschreibung, c=None, luecke=None, index=None):
    d = {}
    if luecke is not None: d['luecke'] = luecke
    if index is not None: d['index'] = index
    d.update({'antwort': antwort, 'fehlbild': None, 'regel_des_fehlbilds': None, 'beschreibung': beschreibung})
    if c is not None: d['c'] = c
    return d


def alt(e):
    """Block `ersetzt`: Kennung/Platz und alter Fragetext (die Datenbank erkennt Aufgaben an Frage + Antworten)."""
    a = e['a']
    return {'kennung': e['kennung'], 'datei': e['datei'], 'index_in_datei': e['idx'], 'thema': e['thema'],
            'einheit_id': (PLAN.get(e['thema']) or {}).get('id'), 'lernkarte': a['l'], 'pool': a['p'], 'stufe': a['s'],
            'alter_fragetext': a['f']['text'], 'alte_frage_json': a['f'], 'alte_antworten': a.get('a')}


def hülle(e, neu_kennung, teil, grund, aufgabe, fehlbilder, **ueber):
    """Wrapper wie in rollend-*: bei Quellen aus rollend-* übernommen, bei themen-Dateien neutral (typ/form/regel leer, zaehlt ja)."""
    r = e['roll'] or {}
    w = {'kennung': neu_kennung, 'teil': teil, 'ersetzt': alt(e), 'grund': grund,
         'thema': e['thema'], 'lernkarte': aufgabe['l'], 'stufe': aufgabe['s'],
         'typ': r.get('typ'), 'form': r.get('form'), 'antwortform': aufgabe['y'],
         'regel': r.get('regel'), 'regel_name': r.get('regel_name'), 'zaehlt': r.get('zaehlt', 'ja'),
         'fehlbilder': fehlbilder, 'aufgabe': aufgabe}
    w.update(ueber)
    return w


V = []   # Vorschläge


def neu(e, **felder):
    a = copy.deepcopy(e['a'])
    for k, v in felder.items():
        a[k] = v
    return a


# ---------- a) Stellenwert-Aufgaben: Ziffer ausdrücklich ----------
for nr, (idx, zahl, ziffern) in enumerate([(6, '1 097', [1, 0, 9, 7]), (31, '4 114', [4, 1, 1, 4])], 1):
    e = themen('inhalte/themen/zahlen.natuerlich.json', idx)
    a = copy.deepcopy(e['a'])
    assert a['f']['text'] == f'Zerlege {zahl} in Stellenwerte.' and a['o']['werte'] == ziffern
    a['f']['text'] = f'Zerlege {zahl} in Stellenwerte. Trage in jedes Feld die Ziffer ein, die an dieser Stelle steht.'
    a['f']['hinweis'] = 'Trage in jedes Feld eine Ziffer von 0 bis 9 ein.'
    a['w'] = a['w'] + f' In die Felder kommen die Ziffern {", ".join(map(str, ziffern[:-1]))} und {ziffern[-1]}.'
    betrag = [z * 10 ** (3 - i) for i, z in enumerate(ziffern)]   # 1000, 0, 90, 7
    if idx == 6:
        fbs = [fb(1000, 'den Betrag der Tausenderstelle (1 000) statt der Ziffer eingetragen', '1 * 1000', luecke=1),
               fb(90, 'den Betrag der Zehnerstelle (90) statt der Ziffer eingetragen', '9 * 10', luecke=3),
               fb(9, 'die Ziffer der Zehner in das Hunderter-Feld gesetzt (die 0 übersprungen)', '9', luecke=2)]
    else:
        fbs = [fb(4000, 'den Betrag der Tausenderstelle (4 000) statt der Ziffer eingetragen', '4 * 1000', luecke=1),
               fb(100, 'den Betrag der Hunderterstelle (100) statt der Ziffer eingetragen', '1 * 100', luecke=2),
               fb(10, 'den Betrag der Zehnerstelle (10) statt der Ziffer eingetragen', '1 * 10', luecke=3)]
    V.append(hülle(e, f'BB1-A{nr}', 'a', 'Mehrdeutig: Felder T/H/Z/E konnten als Ziffer (1/0/9/7) oder als Betrag (1000/0/90/7) gelesen werden; '
                   'Fragetext und Hinweis sagen jetzt ausdrücklich „die Ziffer“.', a, fbs))

# ---------- b) Klasse-7-Stoff in der Klasse-6-Einheit bruch.prozent ----------
e = KENN['K6-V117']
a = copy.deepcopy(e['a'])
a['f'] = {'text': 'Ein Fahrrad wird um 20 % billiger. Man spart dabei 70 €. Wie viel Euro kostet das Fahrrad jetzt?'}
a['g'] = 'verknuepfen'
a['o'] = {'wert': 280, 'einheit': '€'}
a['c'] = '70 / 0.2 - 70'
a['h'] = '70 € sind 20 % vom alten Preis. Wie viel Euro sind dann 100 %?'
a['w'] = ('20 % vom alten Preis sind 70 €. 10 % sind 35 €, also sind 100 % genau 350 €. Jetzt kostet das Fahrrad 350 € − 70 € = 280 €. '
          'Probe: 20 % von 350 € = 70 €.')
V.append(hülle(e, 'BB1-B1', 'b', 'Klasse-7-Stoff in der Klasse-6-Einheit: Preis nach Rabatt → alter Preis (verminderter Grundwert rückwärts). '
               'Ersatz bleibt in Klasse 6: Grundwert aus Rabattbetrag und Rabattsatz, dann der neue Preis (Stufe 3, Typ verknuepfen).', a,
               [fb(350, 'den Preis vor dem Rabatt angegeben, nicht den Preis danach', '70 / 0.2'),
                fb(14, '20 % von 70 € gerechnet statt den Grundwert zu suchen', '70 * 0.2'),
                fb(420, 'den Rabatt zum alten Preis dazugezählt: 350 € + 70 €', '70 / 0.2 + 70')],
               typ='Umkehren', form='umkehren'))

e = themen('inhalte/themen/bruch.prozent.json', 232)
a = copy.deepcopy(e['a'])
a['f'] = {'text': 'Ein Händler gibt auf eine Jacke 25 % Rabatt, das sind 20 €. Auf einen Pullover gibt er 20 % Rabatt, das sind 30 €. '
                  'Um wie viel Euro war der Pullover vor dem Rabatt teurer als die Jacke?'}
a['o'] = {'wert': 70, 'einheit': '€'}
a['c'] = '30 / 0.2 - 20 / 0.25'
a['h'] = 'Wie viel Euro sind 1 % bei der Jacke? Und beim Pullover?'
a['w'] = ('Jacke: 25 % sind 20 €, also 1 % = 0,80 € und 100 % = 80 €. Pullover: 20 % sind 30 €, also 1 % = 1,50 € und 100 % = 150 €. '
          'Unterschied: 150 € − 80 € = 70 €.')
V.append(hülle(e, 'BB1-B2', 'b', '„Händleraufgabe“ (Aufschlag +25 %, dann Rabatt −20 %, Prozentfaktoren hintereinander) ist Klasse-7-Stoff; die Einheit nennt sie unter '
               '„offen“ selbst als entfernt. Ersatz: Knobelaufgabe (Bonus, Stufe 3) mit Grundwert aus dem Prozentwert, Klasse 6.', a,
               [fb(10, 'nur die beiden Rabattbeträge verglichen: 30 € − 20 €', '30 - 20'),
                fb(80, 'nur den alten Preis der Jacke angegeben', '20 / 0.25'),
                fb(150, 'nur den alten Preis des Pullovers angegeben', '30 / 0.2')]))

e = KENN['K6-V114']
a = copy.deepcopy(e['a'])
a['f'] = {'text': 'Ein Händler verkauft ein Spiel und macht dabei 6 € Gewinn. Das sind 12 % vom Einkaufspreis. Wie viel Euro hat das Spiel im Einkauf gekostet?'}
a['o'] = {'wert': 50, 'einheit': '€'}
a['c'] = '6 / 0.12'
a['h'] = '6 € sind 12 % vom Einkaufspreis. Wie viel Euro ist dann 1 %?'
a['w'] = '12 % vom Einkaufspreis sind 6 €. 1 % sind 6 € : 12 = 0,50 €. 100 % sind 50 €. Probe: 12 % von 50 € = 6 €.'
V.append(hülle(e, 'BB1-B3', 'b', 'Zweite Händleraufgabe: Verkaufspreis mit 8 % Gewinn → Einkaufspreis (vermehrter Grundwert rückwärts) ist Klasse-7-Stoff. '
               'Ersatz bleibt in Klasse 6: Grundwert aus Gewinn (Prozentwert) und Gewinnsatz.', a,
               [fb(0.72, '12 % von 6 € gerechnet statt den Einkaufspreis zu suchen', '6 * 0.12'),
                fb(56, 'den Gewinn zum Einkaufspreis addiert (das wäre der Verkaufspreis): 50 € + 6 €', '6 / 0.12 + 6'),
                fb(72, '6 mal 12 gerechnet', '6 * 12')]))

# ---------- c) Beschriftungsfehler in Zeichnungen ----------
e = KENN['R8-V079']
a = copy.deepcopy(e['a'])
a['f']['grafik']['name_x'] = 't'
a['f']['grafik']['name_y'] = 'h'
V.append(hülle(e, 'BB1-C1', 'c', 'Achsenname „t in min“ rechts abgeschnitten („t in mi“): Rechts der x-Achse bleiben im Zeichencode (lernKoordinaten, name_x bei px(x1) + 14) nur etwa '
               '24 px Platz, das reicht für ein bis zwei Zeichen. Einheiten stehen im Fragetext (h in Metern, t in Minuten).', a,
               e['roll']['fehlbilder']))

e = KENN['R8-V115']
a = copy.deepcopy(e['a'])
a['f']['grafik'] = {'typ': 'koordinaten', 'x': [0, 8], 'y': [0, 6], 'punkte': [{'x': 1, 'y': 2, 'name': 'P'}, {'x': 4, 'y': 3, 'name': 'Z'}]}
a['a'] = ['P′(4 | 3)', 'P′(7 | 4)', 'P′(7 | 2)', 'P′(3 | 1)']
a['o'] = {'index': 1}
a['w'] = ('P hat die Koordinaten (1 | 2), Z hat (4 | 3). Von P nach Z sind es 3 Schritte nach rechts und 1 nach oben. '
          'Derselbe Weg noch einmal von Z aus führt zu (4 + 3 | 3 + 1) = (7 | 4). Z ist die Mitte der Strecke von P bis P′.')
V.append(hülle(e, 'BB1-C2', 'c', 'Punktname „P“ überdeckt die Achsenzahl „2“ der y-Achse (P lag bei x = −1 direkt neben der Achse). Ersatz: beide Punkte im '
               'ersten Feld (x ab 0), Abstand zur y-Achse mehr als eine Einheit; gleiche Aufgabenidee, andere Zahlen.', a,
               [fb(None, 'das Zentrum selbst als Bildpunkt genannt: der Weg von P nach Z wurde nicht noch einmal gegangen', index=0),
                fb(None, 'nur in x-Richtung weitergegangen und die y-Koordinate von P übernommen', index=2),
                fb(None, 'den Vektor von P nach Z als Koordinaten des Bildpunkts genommen', index=3)]))
for f_ in V[-1]['fehlbilder']:
    f_['antwort'] = a['a'][f_['index']]

e = KENN['R5-V129']
a = copy.deepcopy(e['a'])
a['f']['text'] = ('Die Zeichnung zeigt ein Rechteck ABCD. Von der Ecke A gehen die Strecken [AE] und [AF] aus. '
                  'Es gilt α = ∠BAE = 25° und γ = ∠FAD = 30°. Wie groß ist β = ∠EAF?')
a['f']['grafik']['winkel'] = [['A', 'B', 'E', 'α'], ['A', 'E', 'F', 'β'], ['A', 'F', 'D', 'γ']]
a['w'] = ('Der Eckwinkel des Rechtecks bei A ist 90°. Er besteht aus α = 25°, β und γ = 30°. Also β = 90° − 25° − 30° = 35°. Probe: 25° + 35° + 30° = 90°.')
V.append(hülle(e, 'BB1-C3', 'c', 'Drei Winkelmarken („25°“, „?“, „30°“) liegen im 90°-Winkel bei A auf Radius 35 px nur etwa 18 px auseinander und überdecken die Linien '
               '(lernFigur: Marke auf der Winkelhalbierenden bei d + 13). Ersatz: Marken α, β, γ (je ein Zeichen), die Werte stehen im Fragetext. '
               'Nicht an der Aufgabe lösbar: leere Stellenwert-Kacheln „T H Z E“ bei Klasse ≤ 6 (App).', a, e['roll']['fehlbilder']))

e = KENN['R8-V121']
a = copy.deepcopy(e['a'])
a['f']['text'] = ('In der Zeichnung ist ein Parallelogramm ABCD zu sehen. Der Winkel α bei A hat die Größe (x + 30)°, der Winkel β bei B die Größe (2x + 30)°. '
                  'Benachbarte Winkel im Parallelogramm ergänzen sich zu 180°. Welche Zahl ist x?')
a['f']['grafik']['winkel'] = [['A', 'B', 'D', 'α'], ['B', 'C', 'A', 'β']]
V.append(hülle(e, 'BB1-C4', 'c', 'Die langen Winkelangaben „(x + 30)°“ und „(2x + 30)°“ (rund 70 px breit) liegen auf der Winkelhalbierenden bei 35 px Abstand und '
               'berühren Grundlinie und Bogen. Ersatz: Marken α und β in der Zeichnung, die Terme im Fragetext.', a, e['roll']['fehlbilder']))

e = KENN['K6-V121']
a = copy.deepcopy(e['a'])
a['f']['schablone'] = '① = □ ② = □ ③ = □ ④ = □'
V.append(hülle(e, 'BB1-C5', 'c', 'Vierfach-Lücke: der Zeilenumbruch fällt zwischen Eingabefeld und „;“, die zweite Zeile beginnt mit einem einzelnen „;“. '
               'Ersatz ohne Strichpunkte: Umbrüche fallen dann nur noch vor eine Nummer. (Dieselbe Bauart: 282 Bestandsaufgaben mit vier und mehr Lücken, siehe Zusatzfunde.)',
               a, e['roll']['fehlbilder']))


# ---------- c) Zu breite Tabellen: Tabelle drehen (Zeilen statt Spalten) ----------
def drehen(g, kopf0=None):
    m = [g['kopf']] + g['zeilen']
    t = [list(z) for z in zip(*m)]
    return {'typ': 'tabelle', 'kopf': t[0], 'zeilen': t[1:]}


TABELLEN = [  # Kennung, neue Kopfzellen (None = aus der Drehung), Änderungen an Tipp/Text
    ('K9A-V161', ['Ziffer', 'Treffer'], {}),
    ('K9A-V128', ['Zahl', 'in A', 'in B'], {}),
    ('S3-V038', ['Minute', 'Becken A (l)', 'Becken B (l)'], {}),
    ('K9A-V011', ['n', 'n²'], {'h': 'Suche in der rechten Spalte die beiden Zahlen, zwischen denen 200 liegt. Die Wurzeln stehen in der linken Spalte.'}),
    ('S3-V018', ['Person', 'Stand in €'], {}),
    ('R8-V059', ['Kind', 'Hausnummer'], {}),
    ('S3-V027', ['Grundfläche', 'Ecken', 'Flächen', 'Kanten'], {}),
    ('S3-V058', ['Körperhöhe in cm', 'Volumen in cm³'], {}),
    ('K9A-V143', ['Gruppe', 'Schüler'], {}),
    ('K9A-V137', ['Bereich', 'Kinder'], {}),
    ('R8-V031', ['x', 'T(x)'], {}),
    ('S3-V008', ['Schritt', 'Rechnung'], {}),
    ('R8-V125', ['Ecke', 'Koordinaten'], {}),
]
for nr, (k, kopf, aend) in enumerate(TABELLEN, 1):
    e = KENN[k]
    a = copy.deepcopy(e['a'])
    g = a['f']['grafik']
    spalten = len(g['kopf'])
    n = drehen(g)
    assert len(n['kopf']) == len(kopf), (k, n['kopf'])
    n['kopf'] = kopf
    a['f']['grafik'] = n
    a.update(aend)
    schwer = k in ('K9A-V161', 'K9A-V128', 'S3-V038', 'K9A-V011', 'S3-V018', 'R8-V059')
    V.append(hülle(e, f'BB1-T{nr:02d}', 'c',
                   f'Tabelle mit {spalten} Spalten ist am Handy (Tabellenfeld 334 px) zu breit: Zellen brechen buchstabenweise oder mitten in der Zahl um'
                   f'{" (Sichtprüfung 27.11.: kaputt/gemessen)" if schwer else " (Sichtprüfung 27.11.: leichter, nur gemessen)"}. '
                   f'Ersatz: Tabelle gedreht, {len(n["kopf"])} Spalten und {len(n["zeilen"])} Zeilen; Inhalt und Lösung unverändert.', a, e['roll']['fehlbilder']))


# ---------- Prüfungen ----------
def pruefen():
    fehler, warn = [], []
    F, W = fehler.append, warn.append
    kenn = set()
    for v in V:
        k, a = v['kennung'], v['aufgabe']
        assert k not in kenn; kenn.add(k)
        IP.pruefe_antwort(k, a, F, W)
        if a.get('g') and a['g'] != 'knobel' and a['g'] not in TYP_STUFE[a['s']]: F(f'{k}: Typ {a["g"]} passt nicht zur Stufe {a["s"]}')
        if a['s'] != v['stufe'] or a['l'] != v['lernkarte'] or a['y'] != v['antwortform']: F(f'{k}: Wrapper passt nicht zur Aufgabe')
        if not a.get('h') and a['p'] != 'sicherung' and a['p'] != 'test' and a['p'] != 'korrektur': F(f'{k}: Tipp fehlt')
        o = a['o']; fbs = v['fehlbilder']
        if len(fbs) < 2: F(f'{k}: weniger als 2 Fehlbilder')
        schluessel = set()
        for f_ in fbs:
            s_ = (f_.get('luecke'), f_.get('index'), json.dumps(f_.get('antwort')))
            if s_ in schluessel: F(f'{k}: Fehlbild doppelt {s_}')
            schluessel.add(s_)
            ant = f_.get('antwort')
            if a['y'] == 'zahl' and abs(float(ant) - float(o['wert'])) < 1e-9: F(f'{k}: Fehlbild {ant} gleich der richtigen Antwort')
            if a['y'] == 'luecken' and abs(float(ant) - float(o['werte'][f_['luecke'] - 1])) < 1e-9: F(f'{k}: Fehlbild {ant} in Lücke {f_["luecke"]} gleich der richtigen Antwort')
            if a['y'] == 'auswahl':
                if f_['index'] == o['index'] or a['a'][f_['index']] != ant: F(f'{k}: Fehlbild index/antwort passt nicht')
            if 'c' in f_ and a['y'] != 'auswahl':
                if float(IP.rechne(f_['c'])) != float(ant): F(f'{k}: Fehlbild c „{f_["c"]}“ = {float(IP.rechne(f_["c"]))} ≠ {ant}')
        # Quelle unverändert und Fragetext nicht schon vorhanden (gleiche Einheit, Zahlen durch # ersetzt)
        e_alt = v['ersetzt']
        if json.dumps(e_alt['alte_frage_json'], sort_keys=True) == json.dumps(a['f'], sort_keys=True): F(f'{k}: Frage unverändert (Datenbank erkennt sie als dieselbe Aufgabe)')
        gleich = [x for x in ALLE if x['thema'] == v['thema'] and x['a']['l'] == a['l'] and json.dumps(x['a']['f'], sort_keys=True) == json.dumps(a['f'], sort_keys=True)]
        if gleich: F(f'{k}: gleiche Frage steht schon in {gleich[0]["datei"]}')
        if v['teil'] == 'b':
            gl = [x for x in ALLE if x['thema'] == v['thema'] and x['a']['l'] == a['l'] and norm(x['a']['f']['text']) == norm(a['f']['text'])]
            if gl: F(f'{k}: gleicher Satzbau wie {gl[0]["datei"]}#{gl[0]["idx"]}')
    return fehler, warn


def quellen_unveraendert():
    """Alle Aufgaben-Dateien (themen, rollend-*, tools/tests/aus) gleich git HEAD (keine Änderung im Arbeitsbaum)."""
    p = subprocess.run(['git', 'status', '--porcelain', '--', 'inhalte/themen', 'inhalte/mathe-profi', 'tools/tests/aus'], cwd=WURZEL, capture_output=True, text=True)
    zeilen = [z for z in p.stdout.splitlines() if 'bestand-berichtigung-1' not in z]
    return zeilen


def ausgabe():
    return {'stand': STAND, 'paket': 'bestand-berichtigung-1',
            'hinweis': ('VORSCHLÄGE, nichts eingespielt, keine Quelldatei geändert. Je Eintrag: die vollständige berichtigte Aufgabe (`aufgabe`, Format der Quelldatei, '
                        'Wrapper wie rollend-*) plus `ersetzt` (Kennung/Platz/alter Fragetext der Bestandsaufgabe) und `grund`. Die neuen Kennungen BB1-* sind Platzhalter. '
                        'Bei Quellen aus inhalte/themen ist typ/form/regel leer (Bestandsaufgaben haben keine). Berichtigung = neue Aufgabe + alte Fassung sperren, siehe befund.md.'),
            'anzahl': len(V), 'aufgaben': V}


def main():
    fehler, warn = pruefen()
    for w in warn: print('Hinweis:', w)
    if fehler:
        print('\n'.join('FEHLER ' + f for f in fehler)); sys.exit(1)
    geaendert = quellen_unveraendert()
    if geaendert:
        print('FEHLER: Quelldateien im Arbeitsbaum geändert:\n' + '\n'.join(geaendert)); sys.exit(1)
    text = json.dumps(ausgabe(), ensure_ascii=False, indent=1) + '\n'
    ziel = HIER / 'vorschlag.json'
    if '--pruefen' in sys.argv:
        assert ziel.read_text(encoding='utf-8') == text, 'vorschlag.json entspricht nicht dem Neuaufbau (bauen.py ohne --pruefen laufen lassen)'
    else:
        ziel.write_text(text, encoding='utf-8')
    je = {}
    for v in V: je[v['teil']] = je.get(v['teil'], 0) + 1
    print(f'OK: {len(V)} Vorschläge ({je}), Nachrechnung, Fehlbilder, Typ/Stufe, Doppelte geprüft; Quelldateien unverändert.')


if __name__ == '__main__':
    main()
