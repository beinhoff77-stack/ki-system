#!/usr/bin/env python3
"""Thema messen.flaechen_vielecke – Flächen von Parallelogramm, Dreieck und Trapez (Gymnasium Bayern, Klasse 6, LehrplanPLUS M6 2.1 „Flächeninhalt“).

Achtzehnte Runde, Teil A (Zweig luecken-neu). Baut auf messen.flaechen (Klasse 5: Rechteck, Einheiten, Zerlegen in Rechtecke) und
messen.koerper_berechnung (Klasse 5: Oberfläche des Quaders) auf und wiederholt deren Inhalte nicht.
Lehrplan M6 2.1: Formeln für Parallelogramm, Dreieck und Trapez aus der Rechteckformel durch Zerlegen und Ergänzen herleiten, flexibel anwenden
(die jeweils relevanten Strecken bestimmen), Flächeninhalte in Sachsituationen über Modelle näherungsweise bestimmen, Figuren vergleichen,
Oberflächeninhalte einfacher Körper planvoll berechnen. Keine Gleichungen mit x (Klasse 6); fehlende Längen durch Rückwärtsrechnen.

Je Lernkarte: 18 Übungen (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8; davon 2 nach Prüfungsvorbild und 1 Knobelaufgabe), 1 Test, 3 Korrektur, 6 Sicherung.
Prüfungsvorbilder (nur Typ und Niveau, eigene Zahlen und Einkleidung): Bayerischer Mathematik-Test 8 (ISB) 2005 A8, 2006, 2007 A8, 2008, 2010 B, 2011 A2,
2015 B2, 2018 A4, 2022 A7, 2025 A7; VERA-8 2012 Modul C („Würfelkörper“).

    python3 -I inhalte/generatoren/messen.flaechen_vielecke.py
    python3 -I tools/inhalt_pruefen.py inhalte/themen/messen.flaechen_vielecke.json
"""
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.dont_write_bytecode = True
HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
from _luecken_neu import (A, K, P, Z, aufgaben, d, dreieck, fig, gr, parallelogramm, schraeg_prisma, schreiben, trapez, vieleck, wahl, z,  # noqa: E402
                          netz_rechtecke, netz_keil, hoehe_text)
from _luecken_neu import dreieck as _dreieck, parallelogramm as _parallelogramm, trapez as _trapez  # noqa: E402

ZIEL = HIER.parent / 'themen' / 'messen.flaechen_vielecke.json'
META = {'thema_schluessel': 'messen.flaechen_vielecke', 'thema_id': 99, 'block_id': 114, 'klasse': {'gym_by': 6}}
SEED = 7099


def ganz(b):
    """Vollständiges Bild für Schritte/fehler_bild: alle Felder setzen, damit nichts aus dem vorigen Zustand übrig bleibt."""
    out = dict(b)
    for k in ('flaeche', 'rechter_winkel', 'kreise', 'winkel'):
        out.setdefault(k, [])
    return out


def koord(punkte_xy, namen, x, y, extra=None):
    """Vieleck im Koordinatensystem (1 Kästchen = 1 cm)."""
    n = len(punkte_xy)
    b = {'typ': 'koordinaten', 'x': x, 'y': y, 'punkte': [{'x': p[0], 'y': p[1], 'name': nm} for p, nm in zip(punkte_xy, namen)],
         'strecken': [[*punkte_xy[i], *punkte_xy[(i + 1) % n]] for i in range(n)], 'flaechen': [{'punkte': [list(p) for p in punkte_xy]}]}
    if extra: b.update(extra)
    return b


def mit_hoehe(pk, linien, x, y0, y1, text, poly, flaeche=None, rechte=None):
    """Figur mit frei beschrifteter Höhe (siehe hoehe_text); rechte: rechter Winkel am Fußpunkt _F zu diesem Punkt."""
    pk, linien = dict(pk), list(linien)
    hoehe_text(pk, linien, x, y0, y1, text, poly)
    return fig(pk, linien, flaeche, [['_F', '_H', rechte]] if rechte else None)


def dz(R, lo, hi, schritt=Fr(1, 10)):
    """Zufällige Dezimalzahl lo … hi im Raster schritt, nicht ganzzahlig."""
    while True:
        k = R.randint(int(lo / schritt), int(hi / schritt))
        x = k * schritt
        if x.denominator != 1: return x


EINH = ['cm', 'm', 'dm']


# ---------- Bilder der Lernkarten ----------
B_PG = _parallelogramm(6, 3, 2, 'm', hx=2)
_PGR = ganz({**B_PG, 'punkte': {**B_PG['punkte'], '_G': [8, 0]},
             'linien': [['_F', '_G', '6 m'], ['_G', 'C', '3 m'], ['C', 'D'], ['D', '_F'], ['A', '_F', '', 'gestrichelt'], ['A', 'D', '', 'gestrichelt'], ['B', 'C', '', 'gestrichelt']],
             'flaeche': ['_F', '_G', 'C', 'D'], 'rechter_winkel': [['_F', '_G', 'D'], ['_G', 'C', '_F']]})
B_DR = _dreieck(6, 4, 2, 'm')
_DRP = {'punkte': {**B_DR['punkte'], '_E': [8, 4]}, 'linien': B_DR['linien'] + [['B', '_E', '', 'gestrichelt'], ['_E', 'C', '', 'gestrichelt']]}
B_TR = _trapez(5, 3, 2, 1, 'm')
_TR0 = _trapez(5, 3, 2, 1, 'm', lc=None, lh=None)
_TRP = {'punkte': {**_TR0['punkte'], '_D2': [8, 0], '_A2': [9, 2]},
        'linien': _TR0['linien'] + [['B', '_D2', '3 m', 'gestrichelt'], ['_D2', '_A2', '', 'gestrichelt'], ['_A2', 'C', '5 m', 'gestrichelt']]}
B_HO = _parallelogramm(8, 3, 2, 'm', lh='h = ?')
_HO3 = _parallelogramm(8, 3, 2, 'm')
_HAUS = {'A': (0, 0), 'B': (8, 0), 'C': (8, 4), 'E': (4, 7), 'D': (0, 4)}
B_ZU = fig(_HAUS, [['A', 'B', '8 m'], ['B', 'C', '4 m'], ['C', 'E'], ['E', 'D'], ['D', 'A']], ['A', 'B', 'C', 'E', 'D'])
_ZU_T = {'linien': B_ZU['linien'] + [['D', 'C', '', 'gestrichelt']]}
_zp, _zl = dict(_HAUS), list(_ZU_T['linien'])
hoehe_text(_zp, _zl, 4, 4, 7, '3 m', [(0, 4), (8, 4), (4, 7)])
_ZU3 = {'punkte': {k: list(map(float, v)) for k, v in _zp.items()}, 'linien': _zl, 'flaeche': ['D', 'C', 'E'], 'rechter_winkel': [['_F', 'C', 'E']]}
_fp, _fl = dict(_HAUS), list(_ZU_T['linien'])
hoehe_text(_fp, _fl, 4, 0, 7, '7 m', list(_HAUS.values()))
B_OB = schraeg_prisma([(0, 0), (6, 0), (3, 4)], 10, 'cm', labels={0: '6 cm', 1: '5 cm'})
B_OB_NETZ = ganz({**netz_rechtecke([5, 6, 5], 10, 'cm', oben=[(1, [(3, 4)], None)], unten=[(2, [(Fr(18, 5), Fr(-24, 5))], None)], lage=['u', 'u', 'o']), 'flaeche': []})
B_VE = fig({'A': (0, 0), 'B': (4, 0), '_C1': (4, 3), '_D1': (0, 3), '_C2': (7, 3), '_D2': (3, 3)},
           [['A', 'B', 'g = 4 m'], ['B', '_C1'], ['_C1', '_D1'], ['_D1', 'A', 'h = 3 m'], ['B', '_C2', '', 'gestrichelt'], ['_C2', '_D2', '', 'gestrichelt'],
            ['_D2', 'A', '', 'gestrichelt']], ['A', 'B', '_C2', '_D2'], [['A', 'B', '_D1']])

ETAPPEN = [
    {'lernziel': 'parallelogramm', 'titel': 'Flächeninhalt des Parallelogramms',
     'einstieg': 'Im Schulgarten liegt ein schiefes Beet. Seine gegenüberliegenden Seiten sind parallel: Es ist ein ⟦Parallelogramm⟧. Wie groß ist seine Fläche?',
     'woerter': [['Parallelogramm', 'Viereck, bei dem gegenüberliegende Seiten parallel sind'], ['Grundseite g', 'die Seite, auf der die Figur „steht“'],
                 ['Höhe h', 'senkrechter Abstand zur Gegenseite – nicht die schräge Seite']],
     'bild': B_PG,
     'schritte': [{'text': 'Das Beet: Grundseite g = 6 m, Höhe h = 3 m.'},
                  {'text': 'Schneide links an der Höhe ein Dreieck ab.', 'bild': {'flaeche': ['A', '_F', 'D']}},
                  {'text': 'Lege das Dreieck rechts an. Es entsteht ein Rechteck.', 'bild': _PGR},
                  {'text': 'Rechteck: 6 m · 3 m = ⟦18 m²⟧. Das Beet ist genauso groß.'}],
     'fehler': 'Die schräge Seite ist nicht die Höhe. 6 m · 3,6 m ergäbe zu viel Beet. Die Höhe steht senkrecht auf g.',
     'fehler_bild': ganz({**B_PG, 'linien': [x if x[:2] != ['D', 'A'] else ['D', 'A', '3,6 m'] for x in B_PG['linien']]}),
     'regel': 'Parallelogramm: ⟦A = g · h⟧. Die Höhe h steht senkrecht auf der Grundseite g.'},
    {'lernziel': 'dreieck', 'titel': 'Flächeninhalt des Dreiecks',
     'einstieg': 'Ein Beet im Schulgarten ist dreieckig. Zwei gleiche Dreiecke kann man zu einem Parallelogramm zusammenlegen. Also ist ein Dreieck die ⟦Hälfte⟧ davon.',
     'woerter': [['zugehörige Höhe', 'die Höhe, die senkrecht auf der gewählten Grundseite steht'], ['stumpfwinklig', 'ein Winkel ist größer als 90°; eine Höhe liegt dann außen']],
     'bild': B_DR,
     'schritte': [{'text': 'Das Beet: Grundseite g = 6 m, zugehörige Höhe h = 4 m.'},
                  {'text': 'Ein zweites, gedrehtes Dreieck ergänzt es zum Parallelogramm.', 'bild': _DRP},
                  {'text': 'Parallelogramm: 6 m · 4 m = 24 m².'},
                  {'text': 'Das Dreieck ist die Hälfte: 24 m² : 2 = ⟦12 m²⟧.', 'bild': ganz(B_DR)},
                  {'text': 'Ist das Dreieck stumpfwinklig, liegt die Höhe außen. Die Formel bleibt gleich.', 'bild': ganz(_dreieck(4, 3, 6, 'm'))}],
     'fehler': 'Das Halbieren vergessen: 6 m · 4 m = 24 m² ist das ganze Parallelogramm. Das Beet ist nur halb so groß.',
     'fehler_bild': ganz({**B_DR, **_DRP, 'linien': B_DR['linien'] + [['B', '_E', '', 'gestrichelt'], ['_E', 'C', 'zwei Beete', 'gestrichelt']]}),
     'regel': 'Dreieck: ⟦A = g · h : 2⟧. Jede Seite kann Grundseite sein, mit ihrer zugehörigen Höhe.'},
    {'lernziel': 'trapez', 'titel': 'Flächeninhalt des Trapezes',
     'einstieg': 'Das dritte Beet hat zwei parallele Seiten, die verschieden lang sind. So ein Viereck heißt ⟦Trapez⟧. Zwei gleiche Trapeze ergeben zusammen ein Parallelogramm.',
     'woerter': [['Trapez', 'Viereck mit zwei parallelen Seiten; sie heißen a und c']],
     'bild': B_TR,
     'schritte': [{'text': 'Das Beet: a = 5 m, c = 3 m, Höhe h = 2 m.'},
                  {'text': 'Ein zweites, gedrehtes Trapez ergänzt es zum Parallelogramm.', 'bild': _TRP},
                  {'text': 'Dessen Grundseite ist a + c = 5 m + 3 m = 8 m.'},
                  {'text': 'Parallelogramm: 8 m · 2 m = 16 m².'},
                  {'text': 'Das Trapez ist die Hälfte: ⟦8 m²⟧.', 'bild': ganz(B_TR)}],
     'fehler': 'Nur a · h ist falsch. 5 m · 2 m = 10 m² ist zu viel. Das Beet ist oben schmaler.',
     'fehler_bild': ganz({**B_TR, 'punkte': {**B_TR['punkte'], '_X': [0, 2], '_Y': [5, 2]},
                          'linien': B_TR['linien'] + [['A', '_X', '', 'gestrichelt'], ['_X', '_Y', '', 'gestrichelt'], ['_Y', 'B', 'zu viel', 'gestrichelt']]}),
     'regel': 'Trapez: ⟦A = (a + c) · h : 2⟧. Dabei sind a und c die parallelen Seiten.'},
    {'lernziel': 'rueckwaerts', 'titel': 'Fehlende Länge berechnen',
     'einstieg': 'Der Hausmeister plant ein Beet mit 24 m². Es soll 8 m lang sein. Wie breit wird es? Er rechnet ⟦rückwärts⟧ von der Fläche zur Länge.',
     'woerter': [['rückwärts rechnen', 'von der Fläche zurück zur fehlenden Länge'], ['zugehörig', 'Grundseite und Höhe gehören zusammen, wenn h senkrecht auf g steht']],
     'bild': B_HO,
     'schritte': [{'text': 'Parallelogramm: A = 24 m², g = 8 m. Gesucht ist die zugehörige Höhe.'},
                  {'text': 'Rückwärts rechnen: Welche Zahl mal 8 ergibt 24? Das ist 3.'},
                  {'text': 'Also ist ⟦h = 3 m⟧, denn 8 m · 3 m = 24 m².', 'bild': {'punkte': _HO3['punkte'], 'linien': _HO3['linien']}},
                  {'text': 'Beim Dreieck zuerst verdoppeln: 2 · A, dann durch g teilen.', 'bild': ganz(_dreieck(6, 4, 2, 'm', lh='h = ?'))}],
     'fehler': 'Verdoppeln vergessen? Bei A = 12 m² und g = 6 m ist h = 4 m. Mit 12 : 6 = 2 m wäre h zu klein.',
     'fehler_bild': ganz(_dreieck(6, 4, 2, 'm', lh='h = 4 m')),
     'regel': 'Rückwärts: ⟦h = A : g⟧ beim Parallelogramm. Beim Dreieck rechnest du h = 2 · A : g.'},
    {'lernziel': 'zusammengesetzt', 'titel': 'Zusammengesetzte Flächen',
     'einstieg': 'Der Schulgarten hat die Form eines Hauses: unten ein Rechteck, oben ein Dreieck. Man ⟦zerlegt⟧ ihn in Teile, die man berechnen kann.',
     'woerter': [['Teilfläche', 'ein Stück der Figur, das man einzeln berechnet'], ['ergänzen', 'zu einer einfachen Figur auffüllen und das Zuviel abziehen']],
     'bild': B_ZU,
     'schritte': [{'text': 'Zerlege den Garten in ein Rechteck und ein Dreieck.', 'bild': _ZU_T},
                  {'text': 'Rechteck: 8 m · 4 m = 32 m².', 'bild': {'flaeche': ['A', 'B', 'C', 'D']}},
                  {'text': 'Dreieck: 8 m · 3 m : 2 = 12 m².',
                   'bild': _ZU3},
                  {'text': 'Beide Teilflächen addieren: 32 m² + 12 m² = ⟦44 m²⟧.', 'bild': {'flaeche': ['A', 'B', 'C', 'E', 'D']}},
                  {'text': 'Ergänzen geht auch: Rechteck 8 m · 7 m minus zwei Ecken.'}],
     'fehler': 'Für das Dach die ganze Höhe 7 m nehmen ist falsch. Das Dreieck selbst ist nur 3 m hoch.',
     'fehler_bild': ganz({**B_ZU, 'punkte': {k: list(map(float, v)) for k, v in _fp.items()}, 'linien': _fl}),
     'regel': '⟦Zerlegen⟧ in bekannte Figuren und addieren. Oder ergänzen und das Zuviel abziehen.'},
    {'lernziel': 'oberflaeche', 'titel': 'Oberfläche einfacher Körper',
     'einstieg': 'Eine Schokolade steckt in einer Schachtel mit dreieckigen Enden. Klappst du die Schachtel flach auf, siehst du ihr ⟦Netz⟧.',
     'woerter': [['Netz', 'die Hülle eines Körpers, flach aufgeklappt'], ['Oberfläche', 'alle Außenflächen eines Körpers zusammen']],
     'bild': B_OB,
     'schritte': [{'text': 'Die Schachtel hat 2 Dreiecke und 3 Rechtecke.'},
                  {'text': 'Klappe sie auf: Das Netz zeigt alle fünf Flächen.', 'bild': B_OB_NETZ},
                  {'text': 'Dreiecke: 2 · (6 cm · 4 cm : 2) = 24 cm².'},
                  {'text': 'Rechtecke: (5 cm + 6 cm + 5 cm) · 10 cm = 160 cm².'},
                  {'text': 'Oberfläche: 24 cm² + 160 cm² = ⟦184 cm²⟧.'}],
     'fehler': 'Die Schachtel hat zwei Enden. Wer nur ein Dreieck zählt, hat 12 cm² zu wenig.',
     'fehler_bild': ganz({**B_OB_NETZ, 'flaeche': ['_u2', '_b0_0', '_u3']}),
     'regel': 'Oberfläche: ⟦alle Flächen des Netzes⟧ addieren. Gleiche Flächen zählen mehrfach.'},
    {'lernziel': 'verstehen', 'titel': 'Flächen vergleichen und beurteilen',
     'einstieg': 'Zwei Beete haben die gleiche Grundseite und die gleiche Höhe. Eins ist schief, eins gerade. Sind sie ⟦flächengleich⟧?',
     'woerter': [['flächengleich', 'gleich großer Flächeninhalt, auch wenn die Form verschieden ist'], ['Modell', 'eine einfache Figur, die eine echte Form ungefähr beschreibt']],
     'bild': B_VE,
     'schritte': [{'text': 'Rechteck und Parallelogramm haben beide g = 4 m und h = 3 m.'},
                  {'text': 'Beide haben 4 m · 3 m = ⟦12 m²⟧. Sie sind flächengleich.'},
                  {'text': 'Ein Teich ist krumm. Als Modell nimmst du ein Trapez oder Rechteck.'},
                  {'text': 'Das Ergebnis ist dann nur ungefähr richtig.'}],
     'fehler': 'Schiefe Figuren wirken größer, weil die Seiten länger sind. Für die Fläche zählt aber nur die Höhe.',
     'fehler_bild': ganz({**B_VE, 'linien': [x if x[:2] != ['B', '_C2'] else ['B', '_C2', '≈ 4,2 m', 'gestrichelt'] for x in B_VE['linien']]}),
     'regel': 'Gleiche Grundseite und gleiche Höhe: ⟦gleicher Flächeninhalt⟧. Die Form ist dabei egal.'},
]


# ---------- Aufgaben-Generatoren ----------
# In Aufgabenbildern stehen keine Eckennamen (die Texte brauchen sie nicht); das macht kleine Figuren lesbar.
def parallelogramm(*a, **k): return _parallelogramm(*a, namen=('_A', '_B', '_C', '_D'), **k)
def dreieck(*a, **k): return _dreieck(*a, namen=('_A', '_B', '_C'), **k)
def trapez(*a, **k): return _trapez(*a, namen=('_A', '_B', '_C', '_D'), **k)

def _pg_maße(R, st):
    e = R.choice(EINH)
    if st == 1:
        g, h = R.randint(3, 12), R.randint(2, 9)
    else:
        g, h = (dz(R, 2, 12, Fr(1, 2)), R.randint(2, 8)) if R.random() < .5 else (R.randint(3, 12), dz(R, 1, 8, Fr(1, 2)))
    v = R.choice([Fr(1), Fr(2), Fr(3, 2), Fr(5, 2)])
    return e, Fr(g), Fr(h), min(v, Fr(g) - 1) if Fr(g) > 2 else Fr(1, 2)


def gen_parallelogramm(R, st):
    if st == 1:
        e, g, h, v = _pg_maße(R, 1)
        art = wahl(R, 'pg1', ['bild', 'text'])
        if art == 'bild':
            return Z(f'Berechne den Flächeninhalt des Parallelogramms mit g = {gr(g, e)} und h = {gr(h, e)}.', g * h, f'{d(g)} * {d(h)}',
                     f'A = g · h = {gr(g, e)} · {gr(h, e)} = {gr(g * h, e + "²")}.', 'Grundseite mal Höhe.', e + '²', grafik=parallelogramm(g, h, v, e))
        s = h + R.randint(1, 3)
        return Z(f'Ein Parallelogramm hat die Grundseite {gr(g, e)}, die zugehörige Höhe {gr(h, e)} und die schräge Seite {gr(s, e)}. Wie groß ist sein Flächeninhalt?',
                 g * h, f'{d(g)} * {d(h)}', f'Die schräge Seite brauchst du nicht. A = {gr(g, e)} · {gr(h, e)} = {gr(g * h, e + "²")}.', 'Welche Länge steht senkrecht auf g?', e + '²')
    if st == 2:
        art = wahl(R, 'pg2', ['dez', 'einheit', 'rechnung', 'seite_b', 'sach'])
        if art == 'dez':
            e, g, h, v = _pg_maße(R, 2)
            return Z(f'Ein Parallelogramm hat g = {gr(g, e)} und h = {gr(h, e)}. Berechne seinen Flächeninhalt.', g * h, f'{d(g)} * {d(h)}',
                     f'A = {gr(g, e)} · {gr(h, e)} = {gr(g * h, e + "²")}.', 'Grundseite mal Höhe, auch mit Kommazahlen.', e + '²', grafik=parallelogramm(g, h, v, e))
        if art == 'einheit':
            gm = Fr(R.randint(11, 30), 10); hc = R.randint(3, 9) * 10
            gc = gm * 100
            return Z(f'Ein Parallelogramm hat die Grundseite {gr(gm, "m")} und die Höhe {gr(hc, "cm")}. Gib den Flächeninhalt in cm² an.', gc * hc, f'{d(gm)} * 100 * {hc}',
                     f'Erst in eine Einheit: {gr(gm, "m")} = {gr(gc, "cm")}. A = {gr(gc, "cm")} · {gr(hc, "cm")} = {gr(gc * hc, "cm²")}.', 'Rechne zuerst beide Längen in cm um.', 'cm²')
        if art == 'rechnung':
            e = 'cm'; g, h = R.randint(5, 10), R.randint(3, 6); v = 2
            s = math.hypot(v, h)
            s1 = Fr(round(s * 10), 10)
            b = parallelogramm(g, h, v, e, seite=f'{z(s1)} cm')
            return A(R, f'Welche Rechnung liefert den Flächeninhalt dieses Parallelogramms (g = {g} cm, h = {h} cm, schräge Seite {z(s1)} cm)?', f'{g} · {h}',
                     [f'{g} · {z(s1)}', f'{g} · {h} : 2', f'2 · {g} + 2 · {z(s1)}'],
                     f'Grundseite mal zugehörige Höhe: {g} cm · {h} cm = {g * h} cm². Die schräge Seite ist nicht die Höhe; 2 · g + 2 · s wäre der Umfang.',
                     'Die Höhe steht senkrecht auf der Grundseite.', grafik=b)
        if art == 'seite_b':
            a_, b_ = R.randint(7, 12), R.randint(4, 7); hb = R.randint(3, b_)
            if hb >= a_: return gen_parallelogramm(R, st)
            return Z(f'Ein Parallelogramm hat die Seiten a = {a_} cm und b = {b_} cm. Die Höhe, die senkrecht auf b steht, ist {hb} cm lang. Wie groß ist der Flächeninhalt?',
                     b_ * hb, f'{b_} * {hb}', f'Hier ist b die Grundseite und {hb} cm die zugehörige Höhe: A = {b_} cm · {hb} cm = {b_ * hb} cm².',
                     'Welche Seite gehört zu der angegebenen Höhe?', 'cm²')
        n = R.randint(6, 15); g = Fr(R.choice([25, 30]), 10); h = R.choice([5, Fr(11, 2), 6])
        return Z(f'Auf einem Parkplatz ist jedes Feld ein Parallelogramm mit g = {gr(g, "m")} und h = {gr(h, "m")}. Wie viel Fläche haben {n} solche Felder zusammen?',
                 n * g * h, f'{n} * {d(g)} * {d(h)}', f'Ein Feld: {gr(g, "m")} · {gr(h, "m")} = {gr(g * h, "m²")}. {n} Felder: {n} · {gr(g * h, "m²")} = {gr(n * g * h, "m²")}.',
                 'Erst ein Feld berechnen.', 'm²')
    art = wahl(R, 'pg3', ['fehler', 'aendern', 'zwei_hoehen', 'sach', 'diagonale'])
    if art == 'fehler':
        g, h = R.randint(6, 12), R.randint(3, 7); s = h + R.randint(1, 3)
        return Z(f'Jonas berechnet ein Parallelogramm mit g = {g} cm, schräger Seite {s} cm und Höhe {h} cm so: {g} · {s} = {g * s} cm². Wie groß ist der Flächeninhalt wirklich?',
                 g * h, f'{g} * {h}', f'Jonas hat die schräge Seite statt der Höhe genommen. Richtig: {g} cm · {h} cm = {g * h} cm².', 'Welche Länge steht senkrecht auf g?', 'cm²')
    if art == 'aendern':
        g, h = R.randint(4, 10), R.randint(2, 8)
        kg, kh = R.choice([(2, 1), (3, 1), (2, 2), (1, 3)])
        return Z(f'Ein Parallelogramm hat {g * h} cm². Die Grundseite wird {"verdoppelt" if kg == 2 else ("verdreifacht" if kg == 3 else "nicht verändert")}, '
                 f'die Höhe {"verdoppelt" if kh == 2 else ("verdreifacht" if kh == 3 else "bleibt gleich")}. Wie groß ist der neue Flächeninhalt?', g * h * kg * kh,
                 f'{g * h} * {kg} * {kh}', f'A = g · h. Mal {kg} bei g und mal {kh} bei h macht mal {kg * kh}: {g * h} cm² · {kg * kh} = {g * h * kg * kh} cm².',
                 'Wie oft steckt das alte Parallelogramm im neuen?', 'cm²')
    if art == 'zwei_hoehen':
        a_, b_ = R.choice([(8, 5), (10, 4), (12, 5), (9, 6), (10, 8), (12, 8), (15, 6)])
        ha = R.randint(2, b_ - 1)
        hb = Fr(a_ * ha, b_)
        if hb.denominator not in (1, 2, 4, 5, 10) or hb >= a_: return gen_parallelogramm(R, st)
        return Z(f'Ein Parallelogramm hat die Seiten a = {a_} cm und b = {b_} cm. Die Höhe zu a ist {ha} cm. Wie lang ist die Höhe zu b?', hb, f'{a_} * {ha} / {b_}',
                 f'Flächeninhalt mit a: {a_} cm · {ha} cm = {a_ * ha} cm². Dieselbe Fläche mit b: {a_ * ha} : {b_} = {z(hb)}. Die Höhe zu b ist {gr(hb, "cm")}.',
                 'Berechne zuerst die Fläche. Sie ist für beide Seiten gleich.', 'cm')
    if art == 'sach':
        g, h = R.choice([(Fr(12, 10), Fr(8, 10)), (Fr(15, 10), Fr(6, 10)), (Fr(2), Fr(5, 10)), (Fr(14, 10), Fr(5, 10))])
        n = R.choice([10, 20, 25, 40])
        p = R.choice([12, 15, 18, 24])
        return Z(f'Für eine Fassade werden {n} Platten in Parallelogrammform gebraucht: g = {gr(g, "m")}, h = {gr(h, "m")}. 1 m² kostet {p} €. Wie teuer sind die Platten?',
                 n * g * h * p, f'{n} * {d(g)} * {d(h)} * {p}', f'Eine Platte: {gr(g, "m")} · {gr(h, "m")} = {gr(g * h, "m²")}. {n} Platten: {gr(n * g * h, "m²")}. '
                 f'Preis: {z(n * g * h)} · {p} € = {z(n * g * h * p)} €.', 'Fläche einer Platte, dann alle Platten, dann der Preis.', '€')
    t = R.choice([12, 15, 18, 21, 24, 27])
    return Z(f'Eine Diagonale teilt ein Parallelogramm in zwei Dreiecke. Eines davon hat {t} cm². Wie groß ist das Parallelogramm?', 2 * t, f'2 * {t}',
             f'Die beiden Dreiecke sind gleich groß (eins ist das gedrehte andere). Also A = 2 · {t} cm² = {2 * t} cm².', 'Sind die beiden Dreiecke gleich groß?', 'cm²')


def _dr(R, st):
    e = R.choice(EINH)
    while True:
        g, h = R.randint(3, 12), R.randint(2, 10)
        if st > 1 and R.random() < .5: g = dz(R, 2, 12, Fr(1, 2))
        if Fr(g * h, 2).denominator in (1, 2, 4): return e, Fr(g), Fr(h)


def gen_dreieck(R, st):
    if st == 1:
        e, g, h = _dr(R, 1)
        A_ = g * h / 2
        xc = R.choice([Fr(1), g / 2, g - 1])
        return Z(f'Berechne den Flächeninhalt des Dreiecks mit g = {gr(g, e)} und h = {gr(h, e)}.', A_, f'{d(g)} * {d(h)} / 2',
                 f'A = g · h : 2 = {gr(g, e)} · {gr(h, e)} : 2 = {gr(A_, e + "²")}.', 'Grundseite mal Höhe, dann halbieren.', e + '²', grafik=dreieck(g, h, xc, e))
    if st == 2:
        art = wahl(R, 'dr2', ['dez', 'rechtwinklig', 'stumpf', 'einheit', 'auswahl'])
        if art == 'dez':
            e, g, h = _dr(R, 2)
            if g.denominator == 1: h = dz(R, 2, 9, Fr(1, 2))
            A_ = g * h / 2
            return Z(f'Ein Dreieck hat g = {gr(g, e)} und h = {gr(h, e)}. Berechne seinen Flächeninhalt.', A_, f'{d(g)} * {d(h)} / 2',
                     f'A = {gr(g, e)} · {gr(h, e)} : 2 = {gr(g * h, e + "²")} : 2 = {gr(A_, e + "²")}.', 'Erst g · h, dann durch 2.', e + '²', grafik=dreieck(g, h, g / 3, e))
        if art == 'rechtwinklig':
            a_, b_ = R.randint(3, 12), R.randint(3, 12)
            c_ = math.hypot(a_, b_)
            return Z(f'Ein rechtwinkliges Dreieck hat die Seiten {a_} cm und {b_} cm am rechten Winkel. Die längste Seite ist etwa {z(Fr(round(c_ * 10), 10))} cm. Wie groß ist der Flächeninhalt?',
                     Fr(a_ * b_, 2), f'{a_} * {b_} / 2', f'Die beiden Seiten am rechten Winkel stehen senkrecht aufeinander: eine ist g, die andere h. A = {a_} · {b_} : 2 = {z(Fr(a_ * b_, 2))} cm².',
                     'Welche Seiten stehen senkrecht aufeinander?', 'cm²', grafik=dreieck(a_, b_, 0, 'cm', lg=None, lh=None) | {'linien': [['_A', '_B', f'{a_} cm'], ['_C', '_B', f'≈ {z(Fr(round(c_ * 10), 10))} cm'], ['_C', '_A', f'{b_} cm']]})
        if art == 'stumpf':
            g, h = R.randint(3, 8), R.randint(2, 6)
            ueber = R.randint(1, 3)
            A_ = Fr(g * h, 2)
            return Z(f'Das Dreieck ist stumpfwinklig. Die Höhe h = {h} cm liegt außen, die Grundseite ist g = {g} cm. Wie groß ist der Flächeninhalt?', A_, f'{g} * {h} / 2',
                     f'Auch wenn die Höhe außen liegt: A = g · h : 2 = {g} · {h} : 2 = {z(A_)} cm².', 'Die Formel gilt auch, wenn die Höhe außen liegt.', 'cm²',
                     grafik=dreieck(g, h, g + ueber, 'cm'))
        if art == 'einheit':
            gm = Fr(R.randint(11, 25), 10); hc = R.choice([40, 50, 60, 80])
            A_ = gm * 100 * hc / 2
            return Z(f'Ein dreieckiger Wimpel hat die Grundseite {gr(gm, "m")} und die Höhe {hc} cm. Wie groß ist er in cm²?', A_, f'{d(gm)} * 100 * {hc} / 2',
                     f'{gr(gm, "m")} = {gr(gm * 100, "cm")}. A = {z(gm * 100)} · {hc} : 2 = {gr(A_, "cm²")}.', 'Erst beide Längen in cm.', 'cm²')
        g, h = R.randint(4, 10), R.randint(3, 8); s = h + R.randint(1, 2)
        return A(R, f'Ein Dreieck hat g = {g} cm, die zugehörige Höhe {h} cm und eine schräge Seite {s} cm. Welche Rechnung gibt den Flächeninhalt?', f'{g} · {h} : 2',
                 [f'{g} · {h}', f'{g} · {s} : 2', f'{g} + {h} + {s}'], f'Grundseite mal zugehörige Höhe, halbiert: {g} · {h} : 2 = {z(Fr(g * h, 2))} cm².',
                 'Die Hälfte von Grundseite mal Höhe.')
    art = wahl(R, 'dr3', ['fehler', 'im_rechteck', 'sach', 'vergleich', 'drachen'])
    if art == 'fehler':
        g, h = R.randint(5, 12), R.randint(3, 9)
        return Z(f'Lea berechnet ein Dreieck mit g = {g} cm und h = {h} cm: {g} · {h} = {g * h} cm². Was ist der richtige Flächeninhalt?', Fr(g * h, 2), f'{g} * {h} / 2',
                 f'Lea hat das Parallelogramm berechnet. Das Dreieck ist die Hälfte: {g * h} : 2 = {z(Fr(g * h, 2))} cm².', 'Wie viele solche Dreiecke passen in ein Parallelogramm mit derselben Grundseite und derselben Höhe?', 'cm²')
    if art == 'im_rechteck':
        a_, b_ = R.randint(5, 12), R.randint(4, 10)
        return Z(f'In ein Rechteck ({a_} cm lang, {b_} cm breit) wird ein Dreieck gezeichnet. Seine Grundseite ist die untere Rechteckseite, seine Spitze liegt auf der oberen. '
                 f'Wie groß ist die Fläche außerhalb des Dreiecks?', Fr(a_ * b_, 2), f'{a_} * {b_} - {a_} * {b_} / 2',
                 f'Rechteck: {a_ * b_} cm². Dreieck: {a_} · {b_} : 2 = {z(Fr(a_ * b_, 2))} cm². Rest: {z(Fr(a_ * b_, 2))} cm² – genau die Hälfte.', 'Wie hoch ist das Dreieck?', 'cm²',
                 grafik=fig({'A': (0, 0), 'B': (a_, 0), '_C': (a_, b_), '_D': (0, b_), 'S': (Fr(a_ * 2, 5), b_)},
                            [['A', 'B', f'{a_} cm'], ['B', '_C', f'{b_} cm'], ['_C', '_D'], ['_D', 'A'], ['A', 'S'], ['S', 'B']], ['A', 'B', 'S']))
    if art == 'sach':
        g, h = R.choice([(Fr(32, 10), Fr(5, 2)), (Fr(4), Fr(3)), (Fr(36, 10), Fr(2)), (Fr(5), Fr(24, 10)), (Fr(28, 10), Fr(3))])
        p = R.choice([8, 12, 15])
        A_ = g * h / 2
        return Z(f'Ein Hausgiebel ist ein Dreieck: {gr(g, "m")} breit und {gr(h, "m")} hoch. Ein Liter Farbe reicht für {p} m². Wie viele Liter brauchst du für 2 Anstriche? '
                 f'Gib das genaue Ergebnis an.', 2 * A_ / p, f'2 * {d(g)} * {d(h)} / 2 / {p}',
                 f'Giebel: {z(g)} · {z(h)} : 2 = {gr(A_, "m²")}. Zwei Anstriche: {gr(2 * A_, "m²")}. Liter: {z(2 * A_)} : {p} = {z(2 * A_ / p)}.',
                 'Fläche, dann zweimal, dann durch die Fläche pro Liter.', 'l') if (2 * A_ / p).denominator in (1, 2, 4, 5, 10, 20, 25) else gen_dreieck(R, st)
    if art == 'vergleich':
        g1, h1 = R.randint(4, 10), R.randint(3, 8)
        g2, h2 = g1 * 2, Fr(h1, 2) if h1 % 2 == 0 else None
        if h2 is None: return gen_dreieck(R, st)
        return A(R, f'Dreieck 1: g = {g1} cm, h = {h1} cm. Dreieck 2: g = {g2} cm, h = {z(h2)} cm. Was stimmt?', 'Beide sind gleich groß.',
                 ['Dreieck 2 ist doppelt so groß.', 'Dreieck 1 ist doppelt so groß.', 'Dreieck 2 ist viermal so groß.'],
                 f'Dreieck 1: {g1} · {h1} : 2 = {z(Fr(g1 * h1, 2))} cm². Dreieck 2: {g2} · {z(h2)} : 2 = {z(g2 * h2 / 2)} cm². Gleich groß.', 'Rechne beide aus.')
    e1, e2 = R.randint(4, 10), R.randint(3, 8)
    return Z(f'Ein Drachen besteht aus zwei Dreiecken mit gemeinsamer Grundseite {2 * e2} dm (Querstab). Die Spitzen sind {e1} dm und {e1 + 2} dm von der Grundseite entfernt. '
             f'Wie groß ist der Drachen?', Fr(2 * e2 * e1, 2) + Fr(2 * e2 * (e1 + 2), 2), f'{2 * e2} * {e1} / 2 + {2 * e2} * {e1 + 2} / 2',
             f'Dreieck 1: {2 * e2} · {e1} : 2 = {e2 * e1} dm². Dreieck 2: {2 * e2} · {e1 + 2} : 2 = {e2 * (e1 + 2)} dm². Zusammen {e2 * e1 + e2 * (e1 + 2)} dm².',
             'Zwei Dreiecke mit derselben Grundseite.', 'dm²')


def _zerlegt(a_, c_, h, l):
    t = trapez(a_, c_, h, l, 'cm', lh=None)
    pk = {**t['punkte'], '_P': [l, 0], '_Q': [l + c_, 0]}
    lin = [x for x in t['linien'] if x[0] not in ('_F', '_ht')] + [['_D', '_P', f'{h} cm', 'gestrichelt'], ['_C', '_Q', '', 'gestrichelt']]
    return {**t, 'punkte': pk, 'linien': lin, 'rechter_winkel': [['_P', '_D', '_B']]}


def gen_trapez(R, st):
    def mass(st):
        e = R.choice(EINH)
        while True:
            a_ = R.randint(5, 14); c_ = R.randint(2, a_ - 2); h = R.randint(2, 8)
            if st > 1 and R.random() < .5: h = dz(R, 1, 6, Fr(1, 2))
            if ((a_ + c_) * Fr(h) / 2).denominator in (1, 2, 4): return e, a_, c_, Fr(h)
    if st == 1:
        e, a_, c_, h = mass(1)
        A_ = (a_ + c_) * h / 2
        return Z(f'Berechne den Flächeninhalt des Trapezes mit a = {gr(a_, e)}, c = {gr(c_, e)} und h = {gr(h, e)}.', A_, f'({a_} + {c_}) * {d(h)} / 2',
                 f'A = (a + c) · h : 2 = ({a_} + {c_}) · {z(h)} : 2 = {z(a_ + c_)} · {z(h)} : 2 = {gr(A_, e + "²")}.', 'Erst a + c, dann mal h, dann halbieren.', e + '²',
                 grafik=trapez(a_, c_, h, Fr(a_ - c_, 2), e))
    if st == 2:
        art = wahl(R, 'tr2', ['dez', 'rechtwinklig', 'einheit', 'auswahl', 'gross'])
        if art in ('dez', 'gross'):
            e, a_, c_, h = mass(2)
            if art == 'gross': a_, c_, h, e = a_ * 10, c_ * 10, h * 10, 'm'
            A_ = (a_ + c_) * h / 2
            return Z(f'Ein {"Grundstück" if art == "gross" else "Trapez"} hat die parallelen Seiten {gr(a_, e)} und {gr(c_, e)}. Ihr Abstand ist {gr(h, e)}. Wie groß ist der Flächeninhalt?',
                     A_, f'({a_} + {c_}) * {d(h)} / 2', f'A = ({a_} + {c_}) · {z(h)} : 2 = {gr(A_, e + "²")}.', 'Der Abstand der parallelen Seiten ist die Höhe.', e + '²',
                     grafik=trapez(a_, c_, h, Fr(a_ - c_, 3), e))
        if art == 'rechtwinklig':
            a_, c_, h = R.randint(6, 12), R.randint(2, 5), R.randint(2, 6)
            A_ = Fr((a_ + c_) * h, 2)
            return Z(f'Ein Trapez hat zwei rechte Winkel: a = {a_} cm, c = {c_} cm, h = {h} cm. Berechne den Flächeninhalt.', A_, f'({a_} + {c_}) * {h} / 2',
                     f'Die senkrechte Seite ist die Höhe. A = ({a_} + {c_}) · {h} : 2 = {z(A_)} cm².', 'Welche Seite steht senkrecht auf a und c?', 'cm²', grafik=trapez(a_, c_, h, 0, 'cm'))
        if art == 'einheit':
            am, cm_, hdm = Fr(R.randint(12, 30), 10), Fr(R.randint(5, 10), 10), R.choice([4, 5, 6, 8])
            if cm_ >= am: return gen_trapez(R, st)
            A_ = (am * 10 + cm_ * 10) * hdm / 2
            return Z(f'Ein Trapez hat a = {gr(am, "m")}, c = {gr(cm_, "m")} und h = {hdm} dm. Gib den Flächeninhalt in dm² an.', A_, f'({d(am)} * 10 + {d(cm_)} * 10) * {hdm} / 2',
                     f'In dm: a = {z(am * 10)} dm, c = {z(cm_ * 10)} dm. A = ({z(am * 10)} + {z(cm_ * 10)}) · {hdm} : 2 = {gr(A_, "dm²")}.', 'Alle Längen zuerst in dm.', 'dm²')
        a_, c_, h = R.randint(6, 12), R.randint(2, 5), R.randint(2, 6)
        return A(R, f'Ein Trapez hat a = {a_} cm, c = {c_} cm und h = {h} cm. Welche Rechnung gibt den Flächeninhalt?', f'({a_} + {c_}) · {h} : 2',
                 [f'{a_} · {c_} · {h} : 2', f'({a_} + {c_}) · {h}', f'{a_} · {h} : 2 + {c_}'],
                 f'A = (a + c) · h : 2 = ({a_} + {c_}) · {h} : 2 = {z(Fr((a_ + c_) * h, 2))} cm².', 'Zuerst die beiden parallelen Seiten addieren.')
    art = wahl(R, 'tr3', ['fehler', 'mittel', 'zerlegt', 'sach', 'dach'])
    if art == 'fehler':
        a_, c_, h = R.randint(7, 14), R.randint(3, 6), R.choice([2, 4, 6, 8])
        return Z(f'Tim rechnet für ein Trapez (a = {a_} cm, c = {c_} cm, h = {h} cm): {a_} + {c_} · {h} : 2 = {z(a_ + Fr(c_ * h, 2))} cm². Wie groß ist das Trapez wirklich?',
                 Fr((a_ + c_) * h, 2), f'({a_} + {c_}) * {h} / 2', f'Tim hat die Klammer vergessen und nur c mit h multipliziert. Richtig: ({a_} + {c_}) · {h} : 2 = {z(Fr((a_ + c_) * h, 2))} cm².',
                 'Was muss zuerst gerechnet werden?', 'cm²')
    if art == 'mittel':
        a_, c_ = R.randint(8, 16), R.randint(2, 6)
        if (a_ + c_) % 2: c_ += 1
        h = R.randint(3, 9)
        m = (a_ + c_) // 2
        return Z(f'Bei einem Trapez ist a = {a_} cm und c = {c_} cm. Die Strecke genau in halber Höhe, parallel zu a, ist halb so lang wie a und c zusammen. '
                 f'Das Trapez ist {h} cm hoch. Wie groß ist es?', m * h, f'({a_} + {c_}) / 2 * {h}',
                 f'Die Strecke in halber Höhe: ({a_} + {c_}) : 2 = {m} cm. Das Trapez ist so groß wie ein Rechteck {m} cm · {h} cm = {m * h} cm².', 'Vergleiche (a + c) : 2 mit der Trapezformel.', 'cm²')
    if art == 'zerlegt':
        c_, l, r, h = R.randint(3, 8), R.randint(1, 4), R.randint(1, 4), R.randint(2, 6)
        a_ = l + c_ + r
        A_ = Fr((a_ + c_) * h, 2)
        return Z(f'Ein Trapez wird in ein Rechteck ({c_} cm · {h} cm) und zwei rechtwinklige Dreiecke zerlegt. Die Dreiecke sind unten {l} cm und {r} cm breit und {h} cm hoch. '
                 f'Wie groß ist das ganze Trapez?', A_, f'{c_} * {h} + {l} * {h} / 2 + {r} * {h} / 2',
                 f'Rechteck {c_ * h} cm², Dreiecke {z(Fr(l * h, 2))} cm² und {z(Fr(r * h, 2))} cm². Zusammen {z(A_)} cm². Probe mit der Formel: ({a_} + {c_}) · {h} : 2 = {z(A_)} cm².',
                 'Drei Teilflächen addieren.', 'cm²', grafik=_zerlegt(a_, c_, h, l))
    if art == 'sach':
        a_, c_, h = R.choice([(Fr(12), Fr(8), Fr(5)), (Fr(9), Fr(5), Fr(4)), (Fr(10), Fr(6), Fr(Fr(7, 2))), (Fr(16), Fr(10), Fr(6))])
        p = R.choice([3, 4, 5])
        A_ = (a_ + c_) * h / 2
        return Z(f'Eine Wiese ist trapezförmig: die parallelen Seiten sind {gr(a_, "m")} und {gr(c_, "m")} lang, ihr Abstand {gr(h, "m")}. Für 1 m² braucht man {p} g Grassamen. '
                 f'Wie viel g Samen braucht man?', A_ * p, f'({d(a_)} + {d(c_)}) * {d(h)} / 2 * {p}', f'A = ({z(a_)} + {z(c_)}) · {z(h)} : 2 = {gr(A_, "m²")}. Samen: {z(A_)} · {p} g = {z(A_ * p)} g.',
                 'Erst die Fläche, dann mal die Menge pro m².', 'g')
    a_, c_, h = R.choice([(10, 4, 3), (12, 6, 4), (9, 3, 4), (11, 5, 3), (14, 8, 5)])
    A_ = Fr((a_ + c_) * h, 2)
    return Z(f'Eine Dachfläche ist ein Trapez: unten {a_} m, oben {c_} m lang; die Höhe des Trapezes (die Dachschräge hinauf) ist {h} m. Wie viele m² Dachziegel braucht man für beide gleich großen Dachseiten?', 2 * A_,
             f'2 * ({a_} + {c_}) * {h} / 2', f'Eine Seite: ({a_} + {c_}) · {h} : 2 = {z(A_)} m². Zwei Seiten: {z(2 * A_)} m².', 'Erst eine Dachseite.', 'm²')


def gen_rueckwaerts(R, st):
    if st == 1:
        art = wahl(R, 'rw1', ['pg', 'rechteck'])
        g, h = R.randint(3, 12), R.randint(2, 9)
        if art == 'pg':
            return Z(f'Ein Parallelogramm hat {g * h} cm² und die Grundseite {g} cm. Wie lang ist die zugehörige Höhe?', h, f'{g * h} / {g}',
                     f'Rückwärts: Welche Zahl mal {g} ergibt {g * h}? {g * h} : {g} = {h}. Die Höhe ist {h} cm.', 'Teile die Fläche durch die Grundseite.', 'cm',
                     grafik=parallelogramm(g, h, 1, 'cm', lh='h = ?'))
        return Z(f'Ein Parallelogramm hat {g * h} m². Seine Höhe ist {h} m. Wie lang ist die Grundseite?', g, f'{g * h} / {h}',
                 f'{g * h} : {h} = {g}. Die Grundseite ist {g} m lang.', 'Welche Zahl mal die Höhe ergibt die Fläche?', 'm')
    if st == 2:
        art = wahl(R, 'rw2', ['dr_h', 'dr_g', 'pg_dez', 'auswahl', 'tr_h'])
        if art in ('dr_h', 'dr_g'):
            g, h = R.randint(3, 12), R.randint(2, 10)
            if (g * h) % 2: g += 1
            A_ = g * h // 2
            if art == 'dr_h':
                return Z(f'Ein Dreieck hat den Flächeninhalt {A_} cm² und die Grundseite {g} cm. Wie lang ist die zugehörige Höhe?', h, f'2 * {A_} / {g}',
                         f'Verdoppeln: 2 · {A_} = {2 * A_} (das ganze Parallelogramm). Dann {2 * A_} : {g} = {h}. h = {h} cm.', 'Zuerst verdoppeln, dann durch g teilen.', 'cm',
                         grafik=dreieck(g, h, g / 2, 'cm', lh='h = ?'))
            return Z(f'Ein Dreieck hat {A_} cm² und die Höhe {h} cm. Wie lang ist die zugehörige Grundseite?', g, f'2 * {A_} / {h}',
                     f'2 · {A_} = {2 * A_}. {2 * A_} : {h} = {g}. g = {g} cm.', 'Zuerst verdoppeln, dann durch h teilen.', 'cm')
        if art == 'pg_dez':
            g = R.choice([4, 5, 8]); h = dz(R, 1, 9, Fr(1, 10))
            A_ = g * h
            return Z(f'Ein Parallelogramm hat {gr(A_, "m²")} und die Grundseite {g} m. Wie hoch ist es?', h, f'{d(A_)} / {g}', f'{z(A_)} : {g} = {z(h)}. Die Höhe ist {gr(h, "m")}.',
                     'Fläche durch Grundseite.', 'm')
        if art == 'tr_h':
            a_, c_, h = R.randint(6, 12), R.randint(2, 5), R.randint(2, 8)
            A_ = Fr((a_ + c_) * h, 2)
            if A_.denominator != 1: return gen_rueckwaerts(R, st)
            return Z(f'Ein Trapez hat a = {a_} cm, c = {c_} cm und den Flächeninhalt {z(A_)} cm². Wie hoch ist es?', h, f'2 * {z(A_)} / ({a_} + {c_})',
                     f'Verdoppeln: {z(2 * A_)}. Das ist (a + c) · h = {a_ + c_} · h. {z(2 * A_)} : {a_ + c_} = {h}. h = {h} cm.', 'Verdoppeln, dann durch a + c teilen.', 'cm')
        g, h = R.randint(4, 10), R.randint(2, 8)
        A_ = g * h
        return A(R, f'Ein Dreieck hat {A_} cm² und die Grundseite {g} cm. Wie findest du die Höhe?', f'2 · {A_} : {g}',
                 [f'{A_} : {g}', f'{A_} · {g} : 2', f'{A_} : 2 : {g}'], f'Das Dreieck ist die Hälfte von g · h. Also g · h = 2 · {A_}, und h = 2 · {A_} : {g} = {2 * h} cm.',
                 'Beim Dreieck musst du vorher verdoppeln.')
    art = wahl(R, 'rw3', ['tr_c', 'einheit', 'quadrat', 'sach', 'gleich'])
    if art == 'tr_c':
        a_, c_, h = R.randint(8, 14), R.randint(2, 6), R.choice([2, 4, 6])
        A_ = (a_ + c_) * h // 2
        return Z(f'Ein Trapez ist {h} cm hoch und hat {A_} cm². Die Seite a ist {a_} cm lang. Wie lang ist die parallele Seite c?', c_, f'2 * {A_} / {h} - {a_}',
                 f'Verdoppeln: {2 * A_}. Durch h: {2 * A_} : {h} = {a_ + c_} = a + c. Also c = {a_ + c_} − {a_} = {c_} cm.', 'Zuerst a + c bestimmen.', 'cm')
    if art == 'einheit':
        g = R.choice([20, 25, 40, 50]); hm = Fr(R.randint(6, 30), 10)
        A_ = Fr(g, 100) * hm
        return Z(f'Ein Parallelogramm hat {gr(A_, "m²")}. Seine Grundseite ist {g} cm lang. Wie hoch ist es in m?', hm, f'{d(A_)} / ({g} / 100)',
                 f'{g} cm = {z(Fr(g, 100))} m. h = {z(A_)} : {z(Fr(g, 100))} = {gr(hm, "m")}.', 'Grundseite zuerst in m umrechnen.', 'm')
    if art == 'quadrat':
        s = R.randint(4, 12)
        g = R.choice([x for x in (2, 3, 4, 6, 8, 9, 12, 16, 18) if x != s and (s * s * 2) % x == 0 and 2 * s * s / x <= 40] or [s * 2])
        return Z(f'Ein Dreieck mit der Grundseite {g} cm soll so groß sein wie ein Quadrat mit {s} cm Seitenlänge. Wie hoch muss das Dreieck sein?', Fr(2 * s * s, g),
                 f'2 * {s} * {s} / {g}', f'Quadrat: {s * s} cm². Dreieck: g · h = 2 · {s * s} = {2 * s * s}. h = {2 * s * s} : {g} = {z(Fr(2 * s * s, g))} cm.',
                 'Wie groß ist das Quadrat? Dann rückwärts beim Dreieck.', 'cm')
    if art == 'sach':
        a_, c_ = R.choice([(9, 5), (8, 4), (10, 6), (12, 8)])
        h = R.choice([3, 5, 6])
        A_ = (a_ + c_) * h // 2
        return Z(f'Ein Beet in Trapezform soll {A_} m² haben. Die parallelen Seiten sind {a_} m und {c_} m. Wie weit liegen sie auseinander?', h, f'2 * {A_} / ({a_} + {c_})',
                 f'2 · {A_} = {2 * A_}. a + c = {a_ + c_}. {2 * A_} : {a_ + c_} = {h} m.', 'Der Abstand der parallelen Seiten ist die Höhe.', 'm')
    g1 = R.randint(4, 9); h1 = R.randint(3, 8); g2 = R.choice([x for x in range(2, 13) if (g1 * h1) % x == 0 and x != g1])
    return Z(f'Ein Parallelogramm (g = {g1} cm, h = {h1} cm) und ein zweites Parallelogramm mit der Grundseite {g2} cm sind gleich groß. Wie hoch ist das zweite?',
             Fr(g1 * h1, g2), f'{g1} * {h1} / {g2}', f'Fläche: {g1} · {h1} = {g1 * h1} cm². Zweites: {g1 * h1} : {g2} = {z(Fr(g1 * h1, g2))} cm.', 'Erst die Fläche des ersten.', 'cm')


def _haus(R):
    b, w, d_ = R.randint(4, 10), R.randint(3, 7), R.randint(2, 5)
    return b, w, d_


def gen_zusammengesetzt(R, st):
    if st == 1:
        art = wahl(R, 'zu1', ['haus', 'l'])
        if art == 'haus':
            b, w, d_ = _haus(R)
            if (b * d_) % 2: b += 1
            A_ = b * w + b * d_ // 2
            pk = {'A': (0, 0), 'B': (b, 0), 'C': (b, w), 'E': (b / 2, w + d_), 'D': (0, w), '_H': (b / 2, w)}
            return Z(f'Ein Fünfeck besteht aus einem Rechteck ({b} cm · {w} cm) und einem Dreieck darauf ({d_} cm hoch). Wie groß ist es?', A_, f'{b} * {w} + {b} * {d_} / 2',
                     f'Rechteck: {b * w} cm². Dreieck: {b} · {d_} : 2 = {b * d_ // 2} cm². Zusammen {A_} cm².', 'Zerlege in Rechteck und Dreieck.', 'cm²',
                     grafik=mit_hoehe({k: v for k, v in pk.items() if k != '_H'}, [['A', 'B', f'{b} cm'], ['B', 'C', f'{w} cm'], ['C', 'E'], ['E', 'D'], ['D', 'A'], ['D', 'C', '', 'gestrichelt']],
                                      b / 2, w, w + d_, f'{d_} cm', [pk['D'], pk['C'], pk['E']], ['A', 'B', 'C', 'E', 'D'], 'C'))
        a_, b_, c_, e_ = R.randint(6, 10), R.randint(5, 9), R.randint(2, 4), R.randint(2, 4)
        if c_ >= a_ or e_ >= b_: return gen_zusammengesetzt(R, st)
        A_ = a_ * e_ + c_ * (b_ - e_)
        pk = {'A': (0, 0), 'B': (a_, 0), 'C': (a_, e_), 'D': (c_, e_), 'E': (c_, b_), 'F': (0, b_)}
        return Z(f'Die L-Form ist unten {a_} m breit und links {b_} m hoch. Der untere Streifen ist {e_} m hoch, der linke Streifen {c_} m breit. Wie groß ist die Fläche?', A_,
                 f'{a_} * {e_} + {c_} * ({b_} - {e_})', f'Unterer Streifen: {a_} · {e_} = {a_ * e_} m². Darüber: {c_} · ({b_} − {e_}) = {c_ * (b_ - e_)} m². Zusammen {A_} m².',
                 'Zerlege in zwei Rechtecke.', 'm²', grafik=vieleck(pk, {('A', 'B'): f'{a_} m', ('B', 'C'): f'{e_} m', ('E', 'F'): f'{c_} m', ('F', 'A'): f'{b_} m'}))
    if st == 2:
        art = wahl(R, 'zu2', ['ausschnitt', 'rechteck_trapez', 'pfeil', 'ecken'])
        if art == 'ausschnitt':
            a_, b_ = R.randint(8, 14), R.randint(5, 9)
            g, h = R.randint(2, a_ - 3), R.randint(2, b_ - 2)
            if (g * h) % 2: h += 1 if h + 1 < b_ else -1
            if (g * h) % 2 or h < 1: return gen_zusammengesetzt(R, st)
            A_ = a_ * b_ - g * h // 2
            x0 = Fr(a_ - g, 2)
            pk = {'A': (0, 0), 'B': (a_, 0), 'C': (a_, b_), 'D': (0, b_), '_P': (x0, 0), '_Q': (x0 + g, 0), '_S': (x0 + Fr(g, 2), h), '_T': (x0 + Fr(g, 2), 0)}
            return Z(f'Aus einem Rechteck ({a_} cm · {b_} cm) wird unten ein Dreieck ausgeschnitten: Grundseite {g} cm, Höhe {h} cm. Wie groß ist die Restfläche?', A_,
                     f'{a_} * {b_} - {g} * {h} / 2', f'Rechteck: {a_ * b_} cm². Dreieck: {g} · {h} : 2 = {g * h // 2} cm². Rest: {a_ * b_} − {g * h // 2} = {A_} cm².',
                     'Ganzes Rechteck minus Ausschnitt.', 'cm²',
                     grafik=mit_hoehe({k: v for k, v in pk.items() if k != '_T'}, [['A', 'B'], ['B', 'C', f'{b_} cm'], ['C', 'D', f'{a_} cm'], ['D', 'A'], ['_P', '_S'], ['_S', '_Q', ''],
                                                                                    ['_P', '_Q', f'{g} cm']], x0 + Fr(g, 2), 0, h, f'{h} cm', [pk['_P'], pk['_Q'], pk['_S']], None, '_Q'))
        if art == 'rechteck_trapez':
            a_, w, c_, h = R.randint(6, 10), R.randint(2, 5), R.randint(2, 5), R.randint(2, 4)
            if c_ >= a_: return gen_zusammengesetzt(R, st)
            if ((a_ + c_) * h) % 2: h += 1
            A_ = a_ * w + (a_ + c_) * h // 2
            xd = Fr(a_ - c_, 2)
            pk = {'A': (0, 0), 'B': (a_, 0), 'C': (a_, w), 'D': (xd + c_, w + h), 'E': (xd, w + h), 'F': (0, w), '_H': (xd, w)}
            return Z(f'Die Figur besteht aus einem Rechteck ({a_} m · {w} m) und einem Trapez darauf (oben {c_} m, {h} m hoch). Wie groß ist sie?', A_,
                     f'{a_} * {w} + ({a_} + {c_}) * {h} / 2', f'Rechteck: {a_ * w} m². Trapez: ({a_} + {c_}) · {h} : 2 = {(a_ + c_) * h // 2} m². Zusammen {A_} m².',
                     'Die Trennlinie ist die untere Seite des Trapezes.', 'm²',
                     grafik=mit_hoehe({k: v for k, v in pk.items() if k != '_H'}, [['A', 'B', f'{a_} m'], ['B', 'C', f'{w} m'], ['C', 'D'], ['D', 'E', f'{c_} m'], ['E', 'F'], ['F', 'A'],
                                                                                    ['F', 'C', '', 'gestrichelt']], xd + Fr(c_, 2), w, w + h, f'{h} m', [pk['F'], pk['C'], pk['D'], pk['E']],
                                      ['A', 'B', 'C', 'D', 'E', 'F'], 'C'))
        if art == 'pfeil':
            l, b, s, sh = R.randint(5, 10), R.randint(2, 4), R.randint(3, 5), R.randint(2, 4)
            sb = b + 2 * R.randint(1, 2)
            if (sb * sh) % 2: sh += 1
            A_ = l * b + sb * sh // 2
            return Z(f'Ein Pfeil besteht aus einem Rechteck ({l} cm lang, {b} cm breit) und einer Dreiecksspitze (Grundseite {sb} cm, Höhe {sh} cm). Wie groß ist der Pfeil?', A_,
                     f'{l} * {b} + {sb} * {sh} / 2', f'Rechteck: {l * b} cm². Spitze: {sb} · {sh} : 2 = {sb * sh // 2} cm². Zusammen {A_} cm².', 'Zerlege in Rechteck und Dreieck.', 'cm²')
        a_, b_, k = R.randint(8, 14), R.randint(6, 10), R.randint(1, 3)
        A_ = a_ * b_ - 2 * k * k
        return Z(f'Von einem Rechteck ({a_} cm · {b_} cm) werden zwei Ecken abgeschnitten. Jede Ecke ist ein rechtwinkliges Dreieck mit {k} cm und {2 * k} cm am rechten Winkel. '
                 f'Wie groß ist die Restfläche?', A_, f'{a_} * {b_} - 2 * {k} * {2 * k} / 2',
                 f'Rechteck: {a_ * b_} cm². Eine Ecke: {k} · {2 * k} : 2 = {k * k} cm². Zwei Ecken: {2 * k * k} cm². Rest: {A_} cm².', 'Ergänzen: Rechteck minus Ecken.', 'cm²')
    art = wahl(R, 'zu3', ['rahmen', 'wand', 'koord', 'fehlend', 'stern'])
    if art == 'rahmen':
        a_, b_, r = R.randint(10, 20), R.randint(8, 15), R.randint(1, 3)
        A_ = a_ * b_ - (a_ - 2 * r) * (b_ - 2 * r)
        return Z(f'Ein Bilderrahmen ist außen {a_} cm · {b_} cm groß und überall {r} cm breit. Wie groß ist die Fläche des Rahmens?', A_,
                 f'{a_} * {b_} - ({a_} - 2 * {r}) * ({b_} - 2 * {r})', f'Außen: {a_ * b_} cm². Innen: {a_ - 2 * r} · {b_ - 2 * r} = {(a_ - 2 * r) * (b_ - 2 * r)} cm². Rahmen: {A_} cm².',
                 'Innen ist jede Seite um zweimal die Rahmenbreite kürzer.', 'cm²')
    if art == 'wand':
        b, w, d_ = R.choice([(8, 3, 2), (10, Fr(5, 2), 3), (9, 3, 2), (12, 3, 4), (6, Fr(5, 2), 2)])
        tb, th = Fr(1), Fr(2)
        A_ = Fr(b) * w + Fr(b) * d_ / 2 - tb * th
        return Z(f'Eine Giebelwand besteht aus einem Rechteck ({b} m breit, {z(w)} m hoch) und einem Dreieck darauf ({d_} m hoch). Die Tür ist 1 m breit und 2 m hoch. '
                 f'Wie viele m² Wand werden gestrichen?', A_, f'{b} * {d(w)} + {b} * {d_} / 2 - 1 * 2',
                 f'Rechteck: {z(b * w)} m². Dreieck: {b} · {d_} : 2 = {z(Fr(b * d_, 2))} m². Tür: 2 m². Wand: {z(A_)} m².', 'Zerlegen, dann die Tür abziehen.', 'm²')
    if art == 'koord':
        x1, x2, y1 = R.randint(1, 3), R.randint(6, 9), R.randint(4, 6)
        xs = R.randint(x1 + 1, x2 - 1)
        pts = [(x1, 1), (x2, 1), (x2, y1), (xs, y1 + 2), (x1, y1)]
        A_ = (x2 - x1) * (y1 - 1) + Fr((x2 - x1) * 2, 2)
        return Z(f'Berechne den Flächeninhalt des Fünfecks ABCDE (1 Kästchen = 1 cm).', A_, f'({x2} - {x1}) * ({y1} - 1) + ({x2} - {x1}) * 2 / 2',
                 f'Rechteck ABCE: {x2 - x1} · {y1 - 1} = {(x2 - x1) * (y1 - 1)} cm². Dreieck ECD: Grundseite {x2 - x1}, Höhe 2: {z(Fr((x2 - x1) * 2, 2))} cm². Zusammen {z(A_)} cm².',
                 'Zerlege in ein Rechteck und ein Dreieck.', 'cm²', grafik=koord(pts, 'ABCDE', [0, 10], [0, y1 + 3]))
    if art == 'fehlend':
        b, w = R.randint(6, 12), R.randint(3, 6)
        d_ = R.choice([2, 4, 6])
        A_ = b * w + b * d_ // 2
        return Z(f'Ein Fünfeck aus Rechteck ({b} cm · {w} cm) und Dreieck darauf hat {A_} cm². Wie hoch ist das Dreieck?', d_, f'2 * ({A_} - {b} * {w}) / {b}',
                 f'Dreieck: {A_} − {b * w} = {A_ - b * w} cm². Rückwärts: 2 · {A_ - b * w} : {b} = {d_} cm.', 'Ziehe zuerst das Rechteck ab.', 'cm')
    s = R.choice([4, 6, 8, 10])
    t = R.choice([2, 3, 4])
    A_ = s * s + 4 * Fr(s * t, 2)
    return Z(f'Auf jede Seite eines Quadrats (Seite {s} cm) wird außen ein Dreieck gesetzt, das {t} cm hoch ist. Wie groß ist der ganze Stern?', A_, f'{s} * {s} + 4 * {s} * {t} / 2',
             f'Quadrat: {s * s} cm². Ein Dreieck: {s} · {t} : 2 = {z(Fr(s * t, 2))} cm². Vier Dreiecke: {z(4 * Fr(s * t, 2))} cm². Zusammen {z(A_)} cm².', 'Quadrat plus vier gleiche Dreiecke.', 'cm²')


DREIECKE = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 6, 10)]


def _keil(R):
    """Rechtwinkliges Dreieck (Seiten am rechten Winkel p, q; lange Seite r) als Stirnfläche, Länge l."""
    p, q, r = R.choice(DREIECKE)
    l = R.randint(5, 15)
    return p, q, r, l


def gen_oberflaeche(R, st):
    if st == 1:
        art = wahl(R, 'ob1', ['keil', 'flaechen'])
        if art == 'keil':
            p, q, r, l = _keil(R)
            O = p * q + (p + q + r) * l
            return Z(f'Ein Keil hat vorn und hinten ein rechtwinkliges Dreieck ({p} cm und {q} cm am rechten Winkel, lange Seite {r} cm). Er ist {l} cm lang. Berechne seine Oberfläche.',
                     O, f'2 * {p} * {q} / 2 + ({p} + {q} + {r}) * {l}',
                     f'Zwei Dreiecke: 2 · {p} · {q} : 2 = {p * q} cm². Drei Rechtecke: {p} · {l} + {q} · {l} + {r} · {l} = {(p + q + r) * l} cm². Oberfläche: {O} cm².',
                     'Zwei Dreiecke und drei Rechtecke.', 'cm²', grafik=schraeg_prisma([(0, 0), (p, 0), (0, q)], l, 'cm', labels={0: f'{p} cm', 2: f'{q} cm'}))
        n = R.choice([3, 4, 5, 6, 8])
        nm = {3: 'Dreieck', 4: 'Viereck', 5: 'Fünfeck', 6: 'Sechseck', 8: 'Achteck'}[n]
        return Z(f'Ein Körper hat vorn und hinten je ein gleiches {nm}. Dazwischen liegen nur Rechtecke. Aus wie vielen Flächen besteht seine Oberfläche?', n + 2, f'{n} + 2',
                 f'Jede Seite des {nm}s gehört zu einem Rechteck: {n} Rechtecke. Dazu vorn und hinten: {n} + 2 = {n + 2} Flächen.', 'Zähle die Rechtecke und die beiden Enden.', None)
    if st == 2:
        art = wahl(R, 'ob2', ['dach', 'trog', 'netz', 'ohne_boden'])
        if art == 'dach':
            g, h, s = R.choice([(6, 4, 5), (8, 3, 5), (16, 6, 10), (12, 8, 10), (24, 5, 13)])
            l = R.randint(8, 20)
            O = g * h + (g + 2 * s) * l
            return Z(f'Eine Schachtel hat vorn und hinten ein gleichschenkliges Dreieck (Grundseite {g} cm, Höhe {h} cm, schräge Seiten je {s} cm). Sie ist {l} cm lang. Wie groß ist ihre Oberfläche?',
                     O, f'2 * {g} * {h} / 2 + ({g} + 2 * {s}) * {l}', f'Dreiecke: 2 · {g} · {h} : 2 = {g * h} cm². Rechtecke: ({g} + {s} + {s}) · {l} = {(g + 2 * s) * l} cm². Zusammen {O} cm².',
                     'Die drei Rechtecke sind alle gleich lang.', 'cm²',
                     grafik=schraeg_prisma([(0, 0), (g, 0), (g / 2, h)], l, 'cm', labels={0: f'{g} cm', 1: f'{s} cm'}))
        if art == 'trog':
            a_, c_, h, s = R.choice([(10, 4, 4, 5), (16, 4, 8, 10), (14, 2, 8, 10), (11, 5, 4, 5), (12, 6, 4, 5)])
            l = R.choice([20, 25, 30, 40])
            O = (a_ + c_) * h + (a_ + c_ + 2 * s) * l
            return Z(f'Ein geschlossener Behälter hat vorn und hinten ein Trapez (a = {a_} cm, c = {c_} cm, h = {h} cm, schräge Seiten je {s} cm). Er ist {l} cm lang. Wie groß ist seine Oberfläche?',
                     O, f'2 * ({a_} + {c_}) * {h} / 2 + ({a_} + {c_} + 2 * {s}) * {l}',
                     f'Zwei Trapeze: 2 · ({a_} + {c_}) · {h} : 2 = {(a_ + c_) * h} cm². Rechtecke: ({a_} + {c_} + {s} + {s}) · {l} = {(a_ + c_ + 2 * s) * l} cm². Oberfläche: {O} cm².',
                     'Zwei Trapeze und vier Rechtecke.', 'cm²',
                     grafik=schraeg_prisma([(0, 0), (a_, 0), (Fr(a_ + c_, 2), h), (Fr(a_ - c_, 2), h)], l, 'cm', labels={0: f'{a_} cm', 2: f'{c_} cm'}))
        if art == 'netz':
            p, q, r, l = _keil(R)
            O = p * q + (p + q + r) * l
            return Z(f'Das Netz zeigt einen Keil: drei Rechtecke ({p} cm, {q} cm und {r} cm breit, {l} cm lang) und zwei rechtwinklige Dreiecke ({p} cm und {q} cm am rechten Winkel). '
                     f'Wie groß ist das Netz?', O, f'({p} + {q} + {r}) * {l} + 2 * {p} * {q} / 2',
                     f'Streifen: ({p} + {q} + {r}) · {l} = {(p + q + r) * l} cm². Dreiecke: 2 · {p} · {q} : 2 = {p * q} cm². Zusammen {O} cm².', 'Streifen plus zwei Dreiecke.', 'cm²',
                     grafik=netz_keil(p, q, r, l))
        g, h, s = R.choice([(Fr(24, 10), Fr(9, 10), Fr(15, 10)), (Fr(16, 10), Fr(6, 10), Fr(1)), (Fr(32, 10), Fr(12, 10), Fr(2))])
        l = R.choice([2, 3])
        O = g * h + 2 * s * l
        return Z(f'Ein Zelt hat vorn und hinten ein Dreieck (Grundseite {gr(g, "m")}, Höhe {gr(h, "m")}) und zwei schräge Rechteckseiten ({gr(s, "m")} breit, {l} m lang). '
                 f'Den Boden gibt es nicht. Wie viel Stoff braucht man?', O, f'2 * {d(g)} * {d(h)} / 2 + 2 * {d(s)} * {l}',
                 f'Dreiecke: 2 · {z(g)} · {z(h)} : 2 = {gr(g * h, "m²")}. Seiten: 2 · {z(s)} · {l} = {gr(2 * s * l, "m²")}. Ohne Boden: {gr(O, "m²")}.', 'Welche Flächen hat das Zelt wirklich?', 'm²')
    art = wahl(R, 'ob3', ['haus', 'vergleich', 'farbe', 'kanten', 'deckel'])
    if art == 'haus':
        b, t, w, dh, s = R.choice([(6, 8, 3, 4, 5), (8, 10, 3, 3, 5), (6, 10, 4, 4, 5), (16, 10, 3, 6, 10)])
        O = 2 * b * w + 2 * t * w + 2 * Fr(b * dh, 2) + 2 * s * t
        return Z(f'Ein Spielhaus ist unten ein Quader ({b} dm breit, {t} dm tief, {w} dm hoch) mit Satteldach: vorn und hinten Dreiecke ({dh} dm hoch), die Dachflächen {s} dm breit. '
                 f'Wie groß ist die Außenfläche ohne Boden?', O, f'2 * {b} * {w} + 2 * {t} * {w} + 2 * {b} * {dh} / 2 + 2 * {s} * {t}',
                 f'Wände: 2 · {b} · {w} + 2 · {t} · {w} = {2 * b * w + 2 * t * w} dm². Giebel: 2 · {b} · {dh} : 2 = {b * dh} dm². Dach: 2 · {s} · {t} = {2 * s * t} dm². '
                 f'Zusammen {z(O)} dm².', 'Wände, Giebel und Dach einzeln berechnen.', 'dm²')
    if art == 'vergleich':
        p, q, r, l = _keil(R)
        mehr = 2 * r * l
        return Z(f'Zwei gleiche Keile (rechtwinkliges Dreieck mit {p} cm und {q} cm am rechten Winkel, lange Seite {r} cm, Länge {l} cm) ergeben zusammengesetzt einen Quader. '
                 f'Um wie viel cm² sind beide Keil-Oberflächen zusammen größer als die Quader-Oberfläche?', mehr, f'2 * {r} * {l}',
                 f'Beim Zusammensetzen liegen die beiden schrägen Rechtecke ({r} cm · {l} cm) aufeinander und sind innen. Sie fehlen außen: 2 · {r} · {l} = {mehr} cm².',
                 'Welche Flächen verschwinden beim Zusammensetzen im Inneren?', 'cm²')
    if art == 'farbe':
        a_, c_, h, s = R.choice([(10, 4, 4, 5), (11, 5, 4, 5), (12, 6, 4, 5)])
        l = R.choice([50, 60, 80])
        innen = (a_ + c_) * h + (c_ + 2 * s) * l
        return Z(f'Ein Futtertrog ist oben offen. Vorn und hinten ist er ein Trapez (oben {a_} cm, unten {c_} cm, {h} cm hoch, schräge Seiten je {s} cm), er ist {l} cm lang. '
                 f'Wie viele cm² Blech braucht man?', innen, f'2 * ({a_} + {c_}) * {h} / 2 + ({c_} + 2 * {s}) * {l}',
                 f'Zwei Trapeze: {(a_ + c_) * h} cm². Boden: {c_} · {l} = {c_ * l} cm². Schräge Seiten: 2 · {s} · {l} = {2 * s * l} cm². Oben offen. Zusammen {innen} cm².',
                 'Welche Fläche fehlt, weil der Trog offen ist?', 'cm²')
    if art == 'kanten':
        p, q, r, l = _keil(R)
        return Z(f'Ein Keil (Dreieck mit {p} cm, {q} cm und {r} cm, Länge {l} cm) soll aus Draht als Kantenmodell gebaut werden. Wie viel cm Draht braucht man?', 2 * (p + q + r) + 3 * l,
                 f'2 * ({p} + {q} + {r}) + 3 * {l}', f'Zwei Dreiecke: 2 · ({p} + {q} + {r}) = {2 * (p + q + r)} cm. Drei Längskanten: 3 · {l} = {3 * l} cm. Zusammen {2 * (p + q + r) + 3 * l} cm.',
                 'Kanten sind Linien, keine Flächen.', 'cm')
    g, h, s = R.choice([(6, 4, 5), (8, 3, 5), (12, 8, 10)])
    l = R.randint(10, 20)
    O = g * h + (g + 2 * s) * l
    return Z(f'Eine Schachtel (Dreieck: g = {g} cm, h = {h} cm, schräge Seiten {s} cm; Länge {l} cm) wird aus Karton gebaut. '
             f'Für Klebelaschen kommt noch ein Zehntel der Oberfläche dazu. Wie viel cm² Karton braucht man?', O + Fr(O, 10), f'({g} * {h} + ({g} + 2 * {s}) * {l}) * 1.1',
             f'Oberfläche: {g} · {h} + ({g} + {s} + {s}) · {l} = {O} cm². Ein Zehntel davon: {O} : 10 = {z(Fr(O, 10))} cm². Zusammen: {O} + {z(Fr(O, 10))} = {z(O + Fr(O, 10))} cm².', 'Berechne zuerst die Oberfläche, dann ein Zehntel davon.', 'cm²')


def gen_verstehen(R, st):
    if st == 1:
        art = wahl(R, 've1', ['gleich', 'aussage'])
        if art == 'gleich':
            g, h = R.randint(3, 8), R.randint(2, 6)
            if g == h: return gen_verstehen(R, st)
            return A(R, f'Ein Rechteck ist {g} cm lang und {h} cm breit. Welche Figur ist flächengleich?', f'ein Parallelogramm mit g = {g} cm und h = {h} cm',
                     [f'ein Dreieck mit g = {g} cm und h = {h} cm', f'ein Parallelogramm mit g = {g} cm und schräger Seite {h} cm', f'ein Quadrat mit {g} cm Seitenlänge'],
                     f'Rechteck: {g * h} cm². Parallelogramm mit gleicher Grundseite und Höhe: auch {g * h} cm². Das Dreieck hat nur die Hälfte; mit schräger Seite ist das Parallelogramm kleiner.',
                     'Gleiche Grundseite und gleiche Höhe?')
        g, h = R.randint(4, 9), R.randint(2, 6)
        return A(R, f'Ein Parallelogramm wird schiefer gedrückt. Grundseite ({g} cm) und Höhe ({h} cm) bleiben gleich. Was passiert mit dem Flächeninhalt?', 'Er bleibt gleich.',
                 ['Er wird größer.', 'Er wird kleiner.', 'Er halbiert sich.'], f'A = g · h = {g * h} cm² hängt nur von g und h ab, nicht davon, wie schief die Figur ist.',
                 'Welche Längen stehen in der Formel?')
    if st == 2:
        art = wahl(R, 've2', ['modell', 'verdoppeln', 'dreieck_pg', 'aussagen', 'umfang'])
        if art == 'modell':
            a_, c_, h = R.choice([(80, 50, 30), (120, 60, 40), (90, 70, 50), (60, 40, 25)])
            return Z(f'Ein Teich ist ungefähr ein Trapez: die parallelen Ufer sind etwa {a_} m und {c_} m lang, ihr Abstand etwa {h} m. Wie groß ist der Teich ungefähr?',
                     Fr((a_ + c_) * h, 2), f'({a_} + {c_}) * {h} / 2', f'Modell Trapez: ({a_} + {c_}) · {h} : 2 = {z(Fr((a_ + c_) * h, 2))} m². Der echte Teich ist ungefähr so groß.',
                     'Rechne mit dem Trapez als Modell.', 'm²')
        if art == 'verdoppeln':
            g, h = R.randint(3, 9), R.randint(2, 6)
            A_ = Fr(g * h, 2)
            return Z(f'Ein Dreieck hat g = {g} cm und h = {h} cm. Grundseite und Höhe werden beide verdoppelt. Wie groß ist das neue Dreieck?', 4 * A_, f'2 * {g} * 2 * {h} / 2',
                     f'Neu: {2 * g} · {2 * h} : 2 = {z(4 * A_)} cm². Das ist das Vierfache von {z(A_)} cm² – nicht das Doppelte.', 'Rechne mit den neuen Längen.', 'cm²')
        if art == 'dreieck_pg':
            g, h = R.randint(4, 10), R.randint(2, 8)
            return Z(f'Ein Parallelogramm und ein Dreieck haben dieselbe Grundseite ({g} cm) und dieselbe Höhe ({h} cm). Wie viel cm² ist das Parallelogramm größer?', Fr(g * h, 2),
                     f'{g} * {h} - {g} * {h} / 2', f'Parallelogramm {g * h} cm², Dreieck {z(Fr(g * h, 2))} cm². Unterschied {z(Fr(g * h, 2))} cm² – das Dreieck ist genau die Hälfte.',
                     'Das Dreieck ist die Hälfte.', 'cm²')
        if art == 'aussagen':
            return A(R, R.choice(['Welche Aussage stimmt immer?', 'Welche Aussage ist richtig?']), 'Zwei Dreiecke mit gleicher Grundseite und gleicher Höhe sind gleich groß.',
                     ['Zwei Dreiecke mit gleichem Umfang sind gleich groß.', 'Ein schiefes Parallelogramm ist größer als ein Rechteck mit gleichen Seiten.',
                      'Ein Trapez ist immer halb so groß wie ein Rechteck mit der Seite a.'],
                     'Der Flächeninhalt hängt nur von Grundseite und Höhe ab. Gleicher Umfang heißt nicht gleiche Fläche, und ein schiefes Parallelogramm ist kleiner als das Rechteck mit gleichen Seiten.',
                     'Denke an die Formel A = g · h : 2.')
        a_, b_ = R.randint(5, 9), R.randint(3, 4)
        hb = R.randint(1, b_ - 1)
        return Z(f'Ein Rechteck ({a_} cm · {b_} cm) wird zu einem Parallelogramm schief gedrückt; die Seiten bleiben gleich lang, die Höhe ist dann nur noch {hb} cm. '
                 f'Um wie viel cm² ist die Fläche kleiner geworden?', a_ * (b_ - hb), f'{a_} * {b_} - {a_} * {hb}',
                 f'Vorher {a_ * b_} cm², nachher {a_} · {hb} = {a_ * hb} cm². Unterschied: {a_ * (b_ - hb)} cm². Der Umfang ist gleich geblieben.', 'Rechne vorher und nachher.', 'cm²')
    art = wahl(R, 've3', ['karte', 'fehler', 'modell_wahl', 'dreiviertel', 'umfang_gleich'])
    if art == 'karte':
        a_, c_, h = R.choice([(4, 2, 3), (6, 2, 2), (5, 3, 2), (3, 1, 4)])
        mst = R.choice([10000, 20000])
        f = Fr(mst, 100000)
        A_ = Fr((a_ + c_) * h, 2) * f * f
        return Z(f'Auf einer Karte im Maßstab 1 : {z(mst)} ist ein Feld ungefähr ein Trapez (a = {a_} cm, c = {c_} cm, h = {h} cm). Wie viel km² hat es in Wirklichkeit ungefähr?',
                 A_, f'({a_} + {c_}) * {h} / 2 * {d(f)} * {d(f)}',
                 f'1 cm auf der Karte sind {z(mst)} cm = {z(f)} km. 1 cm² auf der Karte sind {z(f)} · {z(f)} = {z(f * f)} km². '
                 f'Karte: ({a_} + {c_}) · {h} : 2 = {z(Fr((a_ + c_) * h, 2))} cm², also {z(A_)} km².', 'Wie viel km² ist 1 cm² auf der Karte?', 'km²')
    if art == 'fehler':
        a_, c_, h = R.randint(6, 12), R.randint(2, 5), R.randint(3, 7)
        return A(R, f'Mara sagt: „Ein Trapez mit a = {a_} cm, c = {c_} cm und h = {h} cm hat {a_ * h} cm², denn ich nehme das Rechteck a · h.“ Was stimmt?',
                 f'Zu groß: Das Trapez ist oben schmaler; richtig sind {z(Fr((a_ + c_) * h, 2))} cm².',
                 [f'Richtig, denn a ist die längste Seite.', f'Zu klein: Man muss {a_ + c_} · {h} rechnen.', f'Zu groß: Richtig ist {a_} · {h} : 2 = {z(Fr(a_ * h, 2))} cm².'],
                 f'A = (a + c) · h : 2 = ({a_} + {c_}) · {h} : 2 = {z(Fr((a_ + c_) * h, 2))} cm². a · h ist das Rechteck um das Trapez – zu viel.', 'Rechne mit der Trapezformel nach.')
    if art == 'modell_wahl':
        return A(R, 'Ein Spielplatz hat ungefähr die Form eines Dreiecks mit leicht gebogenen Seiten. Welches Vorgehen gibt einen guten Näherungswert?',
                 'Ein Dreieck einzeichnen, Grundseite und Höhe abmessen und g · h : 2 rechnen.',
                 ['Alle Seiten addieren.', 'Die längste Seite mal sich selbst nehmen.', 'Das umgebende Rechteck berechnen und nicht abziehen.'],
                 'Ein passendes Modell (hier ein Dreieck) liefert einen Näherungswert. Der Umfang ist keine Fläche, und das ganze Rechteck wäre viel zu groß.', 'Welche Figur passt am besten?')
    if art == 'dreiviertel':
        g, h = R.choice([(8, 6), (12, 4), (10, 6), (6, 8)])
        return A(R, f'Ein Parallelogramm (g = {g} cm, h = {h} cm) und ein Dreieck haben denselben Flächeninhalt und dieselbe Grundseite. Wie hoch ist das Dreieck?', f'{2 * h} cm',
                 [f'{h} cm', f'{h // 2} cm', f'{h + 2} cm'], f'Parallelogramm: {g * h} cm². Dreieck: g · h : 2 = {g * h} → g · h = {2 * g * h} → h = {2 * h} cm. Das Dreieck ist doppelt so hoch.',
                 'Das Dreieck braucht die doppelte Höhe, um gleich groß zu sein.')
    a_, b_ = R.choice([(6, 4), (8, 2), (7, 3), (9, 1)])
    s = a_ + b_
    return A(R, f'Zwei Rechtecke haben beide den Umfang {2 * s} cm: {a_} cm · {b_} cm und {z(Fr(s, 2))} cm · {z(Fr(s, 2))} cm. Was stimmt?',
             f'Das Quadrat ist größer ({z(Fr(s * s, 4))} cm² statt {a_ * b_} cm²).',
             ['Beide sind gleich groß, weil der Umfang gleich ist.', f'Das schmale Rechteck ist größer, weil es länger ist.', 'Man kann es ohne Messen nicht sagen.'],
             f'{a_} · {b_} = {a_ * b_} cm², {z(Fr(s, 2))} · {z(Fr(s, 2))} = {z(Fr(s * s, 4))} cm². Gleicher Umfang heißt nicht gleicher Flächeninhalt.', 'Rechne beide Flächen aus.')


GEN = {'parallelogramm': gen_parallelogramm, 'dreieck': gen_dreieck, 'trapez': gen_trapez, 'rueckwaerts': gen_rueckwaerts,
       'zusammengesetzt': gen_zusammengesetzt, 'oberflaeche': gen_oberflaeche, 'verstehen': gen_verstehen}


def fest(R):
    F = {}
    F['parallelogramm'] = [
        Z('Die Punkte A(1|1), B(6|1), C(8|4) und D(3|4) bilden ein Parallelogramm (1 Kästchen = 1 cm). Berechne seinen Flächeninhalt.', 15, '(6 - 1) * (4 - 1)',
          'Grundseite [AB]: von x = 1 bis x = 6, also 5 cm. Höhe: von y = 1 bis y = 4, also 3 cm. A = 5 · 3 = 15 cm².', 'Lies g und h an den Kästchen ab.', 'cm²', art=P,
          grafik=koord([(1, 1), (6, 1), (8, 4), (3, 4)], 'ABCD', [0, 9], [0, 5])),
        Z('Ein Parallelogramm hat die Seiten a = 10 cm und b = 6 cm. Die Höhe zu a ist 4,5 cm lang. Wie lang ist die Höhe zu b?', Fr(15, 2), '10 * 4.5 / 6',
          'A = 10 cm · 4,5 cm = 45 cm². Mit b als Grundseite: 45 : 6 = 7,5. Die Höhe zu b ist 7,5 cm.', 'Die Fläche ist mit beiden Seiten gleich.', 'cm', art=P),
        Z('Ein Rahmen aus vier Leisten (zweimal 12 cm, zweimal 5 cm) ist rechteckig. Er wird schief gedrückt, bis er nur noch 3 cm hoch ist. Wie viel cm² umschließt er jetzt?',
          36, '12 * 3', 'Die Leisten bleiben gleich lang, die Höhe zur 12-cm-Seite ist jetzt 3 cm: A = 12 · 3 = 36 cm² statt vorher 60 cm². Der Umfang ist gleich geblieben.',
          'Welche Länge ist jetzt die Höhe?', 'cm²', art=K)]
    F['dreieck'] = [
        Z('Ein Rechteck ist 6 cm hoch. Darin liegt ein Dreieck: Grundseite auf der unteren Seite, Spitze auf der oberen. Das Dreieck hat 27 cm². Wie lang ist seine Grundseite?',
          9, '2 * 27 / 6', 'Das Dreieck ist 6 cm hoch (so hoch wie das Rechteck). g · 6 : 2 = 27, also g · 6 = 54 und g = 9 cm.', 'Wie hoch ist das Dreieck?', 'cm', art=P),
        Z('Das Parallelogramm ABCD hat A(1|1), B(5|1), C(7|4), D(3|4) (1 Kästchen = 1 cm). Ein Dreieck ABE soll genauso groß sein. Wie hoch muss es über [AB] sein?', 6,
          '2 * (5 - 1) * (4 - 1) / (5 - 1)', 'Parallelogramm: 4 · 3 = 12 cm². Dreieck mit g = 4 cm: 4 · h : 2 = 12, also h = 6 cm. E liegt also 6 Kästchen über [AB], auf der Höhe 7 (zweite Koordinate 7).',
          'Das Dreieck braucht die doppelte Höhe.', 'cm', art=P, grafik=koord([(1, 1), (5, 1), (7, 4), (3, 4)], 'ABCD', [0, 9], [0, 8])),
        Z('In einem Quadrat mit 10 cm Seitenlänge wird ein Punkt P auf der oberen Seite mit den beiden unteren Ecken verbunden. Wie groß ist das Dreieck – egal, wo P liegt?',
          50, '10 * 10 / 2', 'Grundseite 10 cm (untere Seite), Höhe 10 cm (P liegt immer oben). A = 10 · 10 : 2 = 50 cm² – immer die Hälfte des Quadrats.',
          'Ändert sich die Höhe, wenn P wandert?', 'cm²', art=K)]
    F['trapez'] = [
        A(R, 'Warum steht in der Trapezformel A = (a + c) · h : 2 die Summe a + c?', 'Zwei gleiche Trapeze ergeben ein Parallelogramm mit der Grundseite a + c.',
          ['Weil man immer alle Seiten addiert.', 'Weil a und c gleich lang sind.', 'Weil das Trapez aus zwei Rechtecken besteht.'],
          'Legt man ein gedrehtes, gleiches Trapez an, entsteht ein Parallelogramm mit Grundseite a + c und Höhe h. Das Trapez ist die Hälfte davon.',
          'Denke an die Herleitung mit zwei Trapezen.', art=P),
        Z('Die Punkte A(1|1), B(9|1), C(7|5) und D(3|5) bilden ein Trapez (1 Kästchen = 1 cm). Berechne seinen Flächeninhalt.', 24, '((9 - 1) + (7 - 3)) * (5 - 1) / 2',
          'a = 8 cm (von x = 1 bis 9), c = 4 cm (von x = 3 bis 7), h = 4 cm. A = (8 + 4) · 4 : 2 = 24 cm².', 'Lies a, c und h an den Kästchen ab.', 'cm²', art=P,
          grafik=koord([(1, 1), (9, 1), (7, 5), (3, 5)], 'ABCD', [0, 10], [0, 6])),
        Z('Von einem Rechteck (10 cm · 4 cm) werden oben links und oben rechts je ein rechtwinkliges Dreieck abgeschnitten (2 cm breit, 4 cm hoch). Es bleibt ein Trapez. Wie groß ist es?',
          32, '10 * 4 - 2 * 2 * 4 / 2', 'Rechteck 40 cm² minus zwei Dreiecke je 4 cm²: 32 cm². Probe mit der Formel: c = 10 − 2 − 2 = 6 cm, (10 + 6) · 4 : 2 = 32 cm².',
          'Ergänzen oder die Formel – beide Wege gehen.', 'cm²', art=K)]
    F['rueckwaerts'] = [
        Z('Ein Parallelogramm hat die Seiten a = 8 cm und b = 5 cm. Die Höhe zu b ist 6,4 cm. Wie lang ist die Höhe zu a?', 4, '5 * 6.4 / 8',
          'A = 5 cm · 6,4 cm = 32 cm². Mit a als Grundseite: 32 : 8 = 4. Die Höhe zu a ist 4 cm.', 'Berechne zuerst die Fläche mit b.', 'cm', art=P),
        Z('Ein Dreieck soll dieselbe Grundseite und denselben Flächeninhalt haben wie ein Parallelogramm mit g = 7 cm und h = 4 cm. Wie hoch muss das Dreieck sein?', 8,
          '2 * 7 * 4 / 7', 'Parallelogramm: 28 cm². Dreieck: 7 · h : 2 = 28, also 7 · h = 56 und h = 8 cm.', 'Das Dreieck braucht eine größere Höhe.', 'cm', art=P),
        Z('Ein Dreieck hat die Seiten a = 6 cm und b = 8 cm. Die Höhe zu a ist 4 cm lang. Wie lang ist die Höhe zu b?', 3, '6 * 4 / 8',
          'A = 6 · 4 : 2 = 12 cm². Mit b als Grundseite: 8 · h : 2 = 12, also 8 · h = 24 und h = 3 cm.', 'Die Fläche bleibt gleich, egal welche Seite unten liegt.', 'cm', art=K)]
    F['zusammengesetzt'] = [
        Z('Berechne den Flächeninhalt des Vierecks ABCD mit A(3|1), B(8|3), C(6|6) und D(1|4) (1 Kästchen = 1 cm).', 19, '7 * 5 - 5 * 2 / 2 - 2 * 3 / 2 - 5 * 2 / 2 - 2 * 3 / 2',
          'Ergänzen zum Rechteck von x = 1 bis 8 und y = 1 bis 6: 7 · 5 = 35 cm². Vier rechtwinklige Eckdreiecke abziehen: 5 · 2 : 2 = 5, 2 · 3 : 2 = 3, 5 · 2 : 2 = 5, '
          '2 · 3 : 2 = 3, zusammen 16 cm². Viereck: 35 − 16 = 19 cm².',
          'Umgib das Viereck mit einem Rechteck und ziehe die Ecken ab.', 'cm²', art=P, grafik=koord([(3, 1), (8, 3), (6, 6), (1, 4)], 'ABCD', [0, 9], [0, 7])),
        Z('Aus einem Rechteck (12 cm · 8 cm) wird ein dreieckiges Loch geschnitten. Das Loch soll genau ein Viertel der Rechteckfläche haben. Seine Grundseite ist 8 cm. Wie hoch ist es?',
          6, '2 * (12 * 8 / 4) / 8', 'Rechteck 96 cm², ein Viertel: 24 cm². Dreieck: 8 · h : 2 = 24, also 8 · h = 48 und h = 6 cm.', 'Wie groß soll das Loch sein?', 'cm', art=P),
        Z('In ein Quadrat mit 8 cm Seitenlänge zeichnet man ein zweites Quadrat, dessen Ecken die Mitten der Seiten sind. Wie groß ist das innere Quadrat?', 32, '8 * 8 - 4 * 4 * 4 / 2',
          'Außen 64 cm². In jeder Ecke bleibt ein rechtwinkliges Dreieck mit 4 cm und 4 cm: 8 cm². Vier Ecken: 32 cm². Innen: 64 − 32 = 32 cm² – genau die Hälfte.',
          'Ergänzen: Was bleibt in den vier Ecken übrig?', 'cm²', art=K)]
    F['oberflaeche'] = [
        Z('Aus einem Würfel mit 6 cm Kantenlänge wird an einer Ecke ein kleiner Würfel mit 2 cm Kantenlänge herausgeschnitten. Wie groß ist die Oberfläche des Restkörpers?', 216,
          '6 * 6 * 6', 'Es fallen außen drei Quadrate (je 4 cm²) weg, aber innen kommen drei gleich große Quadrate dazu. Die Oberfläche bleibt 6 · 6 · 6 = 216 cm².',
          'Welche Flächen fallen weg, welche kommen dazu?', 'cm²', art=P),
        Z('Vier Würfel (Kante 2 cm) liegen in einer Reihe und sind zusammengeklebt. Wie groß ist die Oberfläche des Körpers?', 72, '(4 * 6 - 2 * 3) * 2 * 2',
          'Vier Würfel hätten 4 · 6 = 24 Quadrate. Drei Klebestellen verdecken je 2 Quadrate: 24 − 6 = 18 Quadrate zu je 4 cm²: 72 cm².', 'Zähle die sichtbaren Quadrate.', 'cm²', art=P),
        Z('Zwei gleiche Keile (Dreieck mit 6 cm und 8 cm am rechten Winkel, lange Seite 10 cm, Länge 12 cm) werden zu einem Quader zusammengelegt. Wie groß ist die Oberfläche des Quaders?',
          432, '2 * (6 * 8 + 6 * 12 + 8 * 12)', 'Quader 6 cm · 8 cm · 12 cm: 2 · (48 + 72 + 96) = 432 cm². Probe: zwei Keile je 48 + 288 = 336, zusammen 672, minus die zwei inneren '
          'Rechtecke 2 · 120 = 240 → 432 cm².', 'Welcher Quader entsteht?', 'cm²', art=K)]
    F['verstehen'] = [
        A(R, 'Stimmt die Aussage? „Haben zwei Rechtecke den gleichen Flächeninhalt, so haben sie auch den gleichen Umfang.“',
          'Nein: 2 cm · 8 cm und 4 cm · 4 cm haben beide 16 cm², aber 20 cm und 16 cm Umfang.',
          ['Ja, denn Fläche und Umfang hängen immer zusammen.', 'Ja, aber nur bei Quadraten.', 'Nein, gleich große Rechtecke gibt es nicht.'],
          'Ein Gegenbeispiel genügt: 2 · 8 = 4 · 4 = 16 cm², die Umfänge sind 2 · (2 + 8) = 20 cm und 4 · 4 = 16 cm.', 'Suche ein Gegenbeispiel.', art=P),
        Z('Ein See ist auf einer Karte im Maßstab 1 : 50 000 ungefähr ein Rechteck von 4 cm · 2 cm. Wie viel km² hat er ungefähr?', 2, '4 * 0.5 * 2 * 0.5',
          '1 cm auf der Karte sind 50 000 cm = 500 m = 0,5 km. Der See ist etwa 2 km · 1 km = 2 km² groß.', 'Rechne die Seiten zuerst in km um.', 'km²', art=P),
        A(R, 'Ein Dreieck und ein Parallelogramm haben die gleiche Grundseite und den gleichen Flächeninhalt. Was gilt für ihre Höhen?', 'Das Dreieck ist doppelt so hoch.',
          ['Beide sind gleich hoch.', 'Das Parallelogramm ist doppelt so hoch.', 'Das hängt von der Form ab.'],
          'Ein Dreieck ist nur halb so groß wie ein Parallelogramm mit derselben Grundseite und derselben Höhe. Damit es trotzdem gleich groß ist, muss es doppelt so hoch sein. Beispiel: g = 4 cm, Parallelogramm 3 cm hoch: 12 cm². Dreieck 6 cm hoch: 4 · 6 : 2 = 12 cm².', 'Vergleiche die beiden Formeln: Was hat das Dreieck zusätzlich?', art=K)]
    return F


def datei():
    auf, anz = aufgaben(ETAPPEN, GEN, fest, SEED)
    lz = [e['lernziel'] for e in ETAPPEN]
    return {
        **META, 'autor': 'Claude (Achtzehnte Runde, Teil A; Generator messen.flaechen_vielecke.py)',
        'inhalt': {
            'ziel': 'Flächeninhalte von Parallelogramm, Dreieck und Trapez durch Zerlegen und Ergänzen herleiten und berechnen, fehlende Längen rückwärts bestimmen, '
                    'zusammengesetzte Figuren berechnen, Oberflächen einfacher Körper über ihr Netz bestimmen und Flächen vergleichen und abschätzen.',
            'merke': ['Parallelogramm: A = g · h. Die Höhe steht senkrecht auf g.', 'Dreieck: A = g · h : 2.', 'Trapez: A = (a + c) · h : 2.',
                      'Rückwärts: h = A : g (Parallelogramm), h = 2 · A : g (Dreieck).', 'Zusammengesetzte Figuren zerlegen oder ergänzen.',
                      'Oberfläche: alle Flächen des Netzes addieren.'],
            'abschnitte': [{'titel': 'Formeln herleiten', 'lernziele': ['parallelogramm', 'dreieck', 'trapez']},
                           {'titel': 'Flexibel anwenden', 'lernziele': ['rueckwaerts', 'zusammengesetzt', 'oberflaeche']},
                           {'titel': 'Verstehen', 'lernziele': ['verstehen']}],
            'etappen': ETAPPEN,
            'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in ETAPPEN],
            'bewertung': {'lernziele_pflicht': lz, 'lernziele_vertiefung': [], 'testaufgaben_je_lernziel': 1, 'hilfen_im_test': False},
            'quellen': {'erklaerungen': 'Eigene Fassung (Claude).',
                        'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern, Gymnasium M6 2.1 „Flächeninhalt“ (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/6/mathematik).',
                        'pruefungsvorbilder': 'Typ und Niveau nach: Bayerischer Mathematik-Test 8 (ISB) 2005 A8 (See schätzen), 2006 A (flächengleiches Dreieck), 2007 A8 (Viereck), '
                                              '2008 A (Restkörper), 2010 B (Teilflächen, Länge gesucht), 2011 A2 (Trapezformel über Parallelogramm), 2015 B2 (Viereck im Gitter), '
                                              '2018 A4 (Aussagen beurteilen), 2022 A7 (Parallelogramm, zwei Höhen), 2025 A7 (Parallelogramm in Koordinaten, flächengleiches Dreieck); '
                                              'VERA-8 2012 Modul C („Würfelkörper“). Eigene Zahlen und Einkleidung.'},
        },
        'aufgaben': auf,
        'offen': ['Das Kind zeichnet und misst nicht selbst (kann die App nicht); Höhen und Längen sind angegeben. Zeichnungen maßstäblich (per Skript geprüft).',
                  'Schrägbilder von Körpern (Prismen, Keile) sind als Figur aus Strecken gezeichnet; Netze als Rechteckstreifen mit angesetzten Dreiecken.',
                  'Keine Gleichungen mit x (erst Klasse 7): fehlende Längen werden durch Rückwärtsrechnen bestimmt.'],
    }, anz


# ---------- STUFEN (Zwanzigste Runde, Zweig stufen-kl6) ----------
from _stufen_kl6 import Stufen, stufen_datei  # noqa: E402

ST = Stufen('messen.flaechen_vielecke', 20_6_10)
SZ, SA, SN, SK, STB = ST.Z, ST.A, ST.neu, ST.knobel, ST.typ_bau

lz = 'parallelogramm'
ST.leiter(lz, 'A = g · h mit gegebener Grundseite und Höhe; die richtige Höhe erkennen.', 'Einheiten umrechnen, mehrere Flächen in Sachsituationen, die passende Höhe zur gewählten Seite.',
          'Fläche im Koordinatensystem, Höhe zu einer anderen Seite, Verdoppeln begründen, schief gedrückter Rahmen, Diagonale, Kosten, Fehler deuten.')
for t, g in (('Die Punkte', 'verknuepfen'), ('Ein Parallelogramm hat die Seiten a = 10 cm und b = 6', 'pruefung'), ('Ein Rahmen', 'transfer'), ('Ein Parallelogramm hat 27', 'begruenden'),
             ('Für eine Fassade', 'transfer'), ('Ein Parallelogramm hat die Seiten a = 10 cm und b = 4', 'rueckwaerts'), ('Eine Diagonale', 'transfer'), ('Jonas', 'fehler')):
    STB(lz, 3, t, g)
SK(lz, SZ('knobel', 'Ein Parallelogramm hat die Seiten 8 cm und 5 cm. Wie groß kann sein Flächeninhalt höchstens sein?', 40, '8 * 5',
         'A = g · h. Mit g = 8 cm kann die Höhe höchstens so lang sein wie die andere Seite, 5 cm – dann steht sie senkrecht und das Parallelogramm ist ein Rechteck. Größter Flächeninhalt: 40 cm².',
         'Wie lang kann die Höhe höchstens werden?', einheit='cm²'))
SK(lz, SZ('knobel', 'In einem Parallelogramm mit 60 cm² verbindet man die Mittelpunkte der vier Seiten. Wie groß ist das innere Viereck?', 30, '60 / 2',
         'Zeichne die beiden Mittellinien ein (sie verbinden gegenüberliegende Seitenmitten und sind parallel zu den Seiten). Sie teilen das Parallelogramm in 4 gleiche kleine Parallelogramme mit je 60 : 4 = 15 cm². Jede Seite des inneren Vierecks ist eine Diagonale eines kleinen Parallelogramms und teilt es in zwei gleiche Dreiecke. Von jedem kleinen Parallelogramm liegt also genau die Hälfte innen: 4 · 7,5 cm² = 30 cm².',
         'Zeichne die Mittellinien parallel zu den Seiten ein.', einheit='cm²'))

lz = 'dreieck'
ST.leiter(lz, 'A = g · h : 2 mit gegebener Grundseite und Höhe; erkennen, was die Höhe ist.', 'Höhe außen, rechtwinklige Dreiecke, Einheiten, die passende Rechnung auswählen.',
          'Dreieck im Rechteck rückwärts, Koordinaten, wandernde Spitze, Drachen, Fehler deuten, gleiche Fläche begründen.')
STB(lz, 1, 'Berechne den Flächeninhalt', 'direkt'); STB(lz, 2, 'Ein dreieckiger Wimpel', 'einkleidung')
for t, g in (('Ein Rechteck ist 6 cm hoch', 'rueckwaerts'), ('Das Parallelogramm ABCD', 'verknuepfen'), ('In einem Quadrat', 'transfer'), ('Lea', 'fehler'),
             ('Dreieck 1', 'begruenden'), ('Ein Drachen', 'pruefung'), ('In ein Rechteck', 'transfer')):
    STB(lz, 3, t, g)
SN(lz, SA('erkennen', 'Welche Aussage über die Höhe eines Dreiecks stimmt?', 'Sie steht senkrecht auf der Grundseite und geht durch die gegenüberliegende Ecke.',
         ['Sie ist immer die längste Seite.', 'Sie ist immer eine der drei Seiten.'], 'Die Höhe ist der Abstand der Spitze von der Grundseite – senkrecht gemessen. Nur im rechtwinkligen Dreieck kann sie eine Seite sein.', 'Wie misst man einen Abstand?'))
SK(lz, SZ('knobel', 'Die Grundseite AB eines Dreiecks ist 6 cm lang. Die Spitze C liegt irgendwo auf einer Linie, die 4 cm über AB parallel zu AB verläuft. Wie groß ist der Flächeninhalt, egal wo C liegt?', 12, '6 * 4 / 2',
         'Wo C auch liegt: Die Höhe ist immer der Abstand der Linie von AB, also 4 cm. A = 6 cm · 4 cm : 2 = 12 cm². Alle diese Dreiecke sind gleich groß.', 'Was ändert sich, wenn C wandert – und was nicht?', einheit='cm²'))
SK(lz, SZ('knobel', 'Ein rechtwinkliges Dreieck hat die Seiten 6 cm und 8 cm am rechten Winkel und die längste Seite 10 cm. Wie lang ist die Höhe auf die längste Seite?', 4.8, '6 * 8 / 10',
         'Fläche mit den Seiten am rechten Winkel: 6 · 8 : 2 = 24 cm². Dieselbe Fläche mit der langen Seite als Grundseite: 10 · h : 2 = 24, also h = 4,8 cm.', 'Berechne die Fläche auf zwei Arten.', einheit='cm'))

lz = 'trapez'
ST.leiter(lz, 'A = (a + c) · h : 2 mit gegebenen Maßen; die parallelen Seiten erkennen.', 'Grundstücke und rechtwinklige Trapeze, Einheiten, die passende Rechnung auswählen.',
          'Formel begründen, Koordinaten, Rechteck mit abgeschnittenen Ecken, Mittellinie, Kosten einer Wiese, Zerlegen, Fehler bei Punkt vor Strich.')
STB(lz, 1, 'Berechne den Flächeninhalt', 'direkt')
STB(lz, 2, 'Ein Grundstück', 'einkleidung'); STB(lz, 2, 'Ein Trapez hat die parallelen Seiten 7', 'einkleidung'); STB(lz, 2, 'Ein Trapez hat a = 1,3', 'mehrschritt')
for t, g in (('Warum', 'begruenden'), ('Die Punkte', 'verknuepfen'), ('Von einem Rechteck', 'transfer'), ('Eine Dachfläche', 'transfer'), ('Eine Wiese', 'pruefung'),
             ('Bei einem Trapez', 'transfer'), ('Ein Trapez wird in', 'rueckwaerts'), ('Tim', 'fehler')):
    STB(lz, 3, t, g)
SN(lz, SA('erkennen', 'Welche Seiten eines Trapezes sind parallel?', 'die beiden Grundseiten a und c', ['die beiden Schenkel b und d', 'alle vier Seiten'], 'Ein Trapez hat (mindestens) ein Paar paralleler Seiten: a und c. Ihr Abstand ist die Höhe.', 'Welche Seiten kommen in der Formel vor?'))
SK(lz, SZ('knobel', 'Ein Trapez hat a = 10 cm, c = 4 cm und h = 6 cm. Eine Diagonale teilt es in zwei Dreiecke. Wie groß ist das größere Dreieck?', 30, '10 * 6 / 2',
         'Beide Dreiecke haben die Höhe 6 cm. Das eine hat die Grundseite a = 10 cm (30 cm²), das andere c = 4 cm (12 cm²). Zusammen 42 cm² = Trapezfläche. Das größere hat 30 cm².', 'Welche Grundseite und welche Höhe hat jedes Dreieck?', einheit='cm²'))
SK(lz, SZ('knobel', 'Ein Trapez hat a = 12 cm und h = 5 cm. Es soll doppelt so groß sein wie ein Dreieck mit der Grundseite 12 cm und der Höhe 5 cm. Wie lang muss c sein?', 12, '2 * 12 * 5 / 2 * 2 / 5 - 12',
         'Dreieck: 12 · 5 : 2 = 30 cm², doppelt 60 cm². (12 + c) · 5 : 2 = 60 ergibt 12 + c = 24, also c = 12 cm. Das „Trapez“ ist dann sogar ein Parallelogramm.', 'Wie groß muss das Trapez sein?', einheit='cm'))

lz = 'rueckwaerts'
ST.leiter(lz, 'Aus Fläche und einer Länge die fehlende Länge beim Parallelogramm bestimmen.', 'Fehlende Höhe oder Grundseite bei Dreieck und Trapez, mit Einheiten.',
          'Höhe zu einer anderen Seite, gleich große Figuren, Einheitenwechsel, fehlende parallele Seite, Abstand der Seiten in einer Sachsituation.')
for t, g in (('Ein Parallelogramm hat die Seiten a = 8', 'pruefung'), ('Ein Dreieck soll dieselbe', 'verknuepfen'), ('Ein Dreieck hat die Seiten', 'transfer'),
             ('Ein Dreieck mit der Grundseite 8', 'verknuepfen'), ('Ein Parallelogramm (g = 7', 'transfer'), ('Ein Parallelogramm hat 0,14', 'verknuepfen'),
             ('Ein Trapez ist 4 cm hoch', 'rueckwaerts'), ('Ein Beet', 'rueckwaerts')):
    STB(lz, 3, t, g)
SK(lz, SZ('knobel', 'Ein Trapez ist 4 cm hoch und hat 30 cm². Die Seite a ist 3 cm länger als die Seite c. Wie lang ist a?', 9, '(30 * 2 / 4 + 3) / 2',
         '(a + c) · 4 : 2 = 30 ergibt a + c = 15. a ist 3 cm länger als c. Nimm die 3 cm von 15 cm weg: Es bleiben 12 cm, das ist zweimal c. Also c = 6 cm und a = 6 cm + 3 cm = 9 cm. Probe: (9 + 6) · 4 : 2 = 30.', 'Bestimme zuerst a + c.', einheit='cm'))
SK(lz, SZ('knobel', 'Ein Dreieck hat 36 cm². Grundseite und Höhe sind ganze Zentimeter. Wie viele Möglichkeiten gibt es für die Länge der Grundseite?', 12, '12',
         'g · h : 2 = 36 heißt g · h = 72. g kann jeder Teiler von 72 sein: 1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72 – das sind 12 Möglichkeiten.', 'Was muss g · h ergeben?'))

lz = 'zusammengesetzt'
ST.leiter(lz, 'Eine Figur in Rechtecke und Dreiecke zerlegen und die Teile addieren.', 'Abschneiden oder Ausschneiden (subtrahieren), Figuren aus mehreren Grundformen.',
          'Vierecke im Koordinatensystem, Loch mit vorgegebener Größe, Quadrat in Quadrat, Rahmen, Giebelwand, fehlende Höhe rückwärts.')
STB(lz, 1, 'Ein Fünfeck', 'direkt'); STB(lz, 1, 'Die L-Form', 'direkt'); STB(lz, 2, 'Ein Pfeil', 'einkleidung')
for t, g in (('Berechne den Flächeninhalt des Vierecks', 'verknuepfen'), ('Aus einem Rechteck', 'rueckwaerts'), ('In ein Quadrat', 'transfer'), ('Auf jede Seite', 'transfer'),
             ('Ein Bilderrahmen', 'transfer'), ('Berechne den Flächeninhalt des Fünfecks', 'verknuepfen'), ('Eine Giebelwand', 'pruefung'), ('Ein Fünfeck aus', 'rueckwaerts')):
    STB(lz, 3, t, g)
SN(lz, SA('erkennen', 'In welche Teilflächen zerlegst du eine L-förmige Figur am einfachsten?', 'in zwei Rechtecke', ['in ein Rechteck und ein Dreieck', 'in zwei Dreiecke'], 'Ein L hat nur rechte Winkel. Ein Schnitt zerlegt es in zwei Rechtecke.', 'Welche Winkel hat ein L?'))
SK(lz, SZ('knobel', 'Ein Kreuz besteht aus 5 gleichen Quadraten (eines in der Mitte, an jeder Seite eines). Sein Umfang ist 48 cm. Wie groß ist sein Flächeninhalt?', 80, '5 * (48 / 12) ** 2',
         'Der Rand des Kreuzes besteht aus 12 Quadratseiten. 48 cm : 12 = 4 cm. Ein Quadrat hat 16 cm², fünf Quadrate 80 cm².', 'Zähle, wie viele Quadratseiten den Rand bilden.', einheit='cm²'))
SK(lz, SZ('knobel', 'In einem Rechteck (12 cm · 8 cm) verbindet man die Mittelpunkte der vier Seiten. Wie groß ist das entstehende Viereck?', 48, '12 * 8 / 2',
         'Die Verbindungen schneiden vier gleiche rechtwinklige Dreiecke (6 cm · 4 cm : 2 = 12 cm²) ab. 96 cm² − 4 · 12 cm² = 48 cm² – genau die Hälfte.', 'Was wird an den Ecken abgeschnitten?', einheit='cm²'))

lz = 'oberflaeche'
ST.leiter(lz, 'Oberfläche eines Prismas aus Grundflächen und Rechtecken zusammensetzen; Flächen eines Körpers erkennen.', 'Schachteln, Zelte, Behälter und Netze mit Dreieck oder Trapez als Grundfläche.',
          'Würfel mit herausgenommener Ecke begründen, zusammengeklebte Körper, Kantenmodell, Schachtel aus Karton, Spielhaus, offener Trog.')
STB(lz, 2, 'Ein geschlossener Behälter', 'mehrschritt')
for t, g in (('Aus einem Würfel', 'begruenden'), ('Vier Würfel', 'pruefung'), ('Zwei gleiche Keile (Dreieck mit 6', 'transfer'), ('Ein Keil', 'verknuepfen'),
             ('Zwei gleiche Keile (rechtwinkliges', 'transfer'), ('Eine Schachtel', 'pruefung'), ('Ein Spielhaus', 'verknuepfen'), ('Ein Futtertrog', 'transfer')):
    STB(lz, 3, t, g)
SK(lz, SZ('knobel', 'Ein Würfel mit 3 cm Kante wird in 27 Würfel mit 1 cm Kante zersägt. Um wie viele cm² ist die Oberfläche aller kleinen Würfel zusammen größer als die des großen Würfels?', 108, '27 * 6 - 6 * 9',
         'Großer Würfel: 6 · 9 cm² = 54 cm². Kleine Würfel: 27 · 6 cm² = 162 cm². Unterschied: 108 cm² – so viel Fläche entsteht durch die Schnitte.', 'Rechne beide Oberflächen aus.', einheit='cm²'))
SK(lz, SZ('knobel', '12 Würfel mit 1 cm Kante werden zu einem Quader zusammengelegt. Wie groß ist die kleinstmögliche Oberfläche?', 32, '2 * (2 * 2 + 2 * 3 + 2 * 3)',
         'Möglich sind 1 · 1 · 12 (50 cm²), 1 · 2 · 6 (40 cm²), 1 · 3 · 4 (38 cm²) und 2 · 2 · 3 (32 cm²). Je „würfelähnlicher“, desto kleiner: 32 cm².', 'Schreibe alle Quader mit 12 Würfeln auf.', einheit='cm²'))

lz = 'verstehen'
ST.leiter(lz, 'Flächen vergleichen und einfache Aussagen beurteilen; Flächeninhalt eines Rechtecks berechnen.', 'Schief drücken, verdoppeln, gleiche Grundseite und Höhe, fehlende Seite eines Rechtecks, Fläche schätzen.',
          'Fläche und Umfang unterscheiden, Maßstab, gleiche Fläche begründen, schätzen bei gebogenen Rändern, Fehler deuten, fehlende Höhe.')
for t, g in (('Stimmt die Aussage', 'begruenden'), ('Ein See', 'pruefung'), ('Ein Dreieck und ein Parallelogramm', 'transfer'), ('Ein Spielplatz', 'transfer'),
             ('Zwei Rechtecke', 'begruenden'), ('Ein Parallelogramm (g = 10', 'rueckwaerts'), ('Mara', 'fehler'), ('Auf einer Karte', 'verknuepfen')):
    STB(lz, 3, t, g)
SN(lz, SZ('direkt', 'Ein Rechteck ist 6 cm lang und 4,5 cm breit. Wie groß ist sein Flächeninhalt?', 27, '6 * 4.5', 'A = 6 cm · 4,5 cm = 27 cm².', 'Länge mal Breite.', einheit='cm²'))
SN(lz, SZ('umkehr', 'Ein Rechteck hat 48 cm² und ist 8 cm lang. Wie breit ist es?', 6, '48 / 8', '48 cm² : 8 cm = 6 cm.', 'Welche Zahl mal 8 ergibt 48?', einheit='cm'))
SK(lz, SZ('knobel', 'Ein Rechteck hat den Umfang 24 cm und ganzzahlige Seiten. Wie groß kann sein Flächeninhalt höchstens sein?', 36, '6 * 6',
         'Länge + Breite = 12 cm. Möglich: 1 · 11, 2 · 10, 3 · 9, 4 · 8, 5 · 7, 6 · 6. Die Flächen 11, 20, 27, 32, 35, 36 cm² – am größten beim Quadrat: 36 cm².', 'Wie groß ist Länge plus Breite?', einheit='cm²'))
SK(lz, SZ('knobel', 'Wie viele verschiedene Rechtecke mit ganzzahligen Seiten (in cm) haben den Flächeninhalt 36 cm²? (Gedrehte zählen nicht doppelt.)', 5, '5',
         '36 = 1 · 36 = 2 · 18 = 3 · 12 = 4 · 9 = 6 · 6. Das sind 5 Rechtecke (das letzte ist ein Quadrat).', 'Zerlege 36 in zwei Faktoren.'))

if __name__ == '__main__':
    d_, anz = datei()
    schreiben(ZIEL, d_, anz)
    stufen_datei('messen.flaechen_vielecke', ST)
