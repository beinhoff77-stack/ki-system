#!/usr/bin/env python3
"""Thema messen.volumen – Volumen (Gymnasium Bayern, Klasse 6, LehrplanPLUS M6 2.2 „Volumen“).

Achtzehnte Runde, Teil A (Zweig luecken-neu). Baut auf messen.koerper_berechnung (Klasse 5: Quader beschreiben, Oberfläche, Volumen nur als
Vertiefungskarte ohne Einheiten) auf. Lehrplan M6 2.2: Quaderformel über Einheitswürfel plausibel machen, Größe der Einheitswürfel vorstellen,
Volumeneinheiten einschließlich Liter und Milliliter umrechnen und das Vorgehen begründen, Quaderformel flexibel anwenden, Näherungswerte für
Körper aus der Erfahrungswelt, Volumen durch Zerlegen und Ergänzen bestimmen (auch im Kopf). Keine Gleichungen mit x (Klasse 6).

Je Lernkarte: 18 Übungen (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8; davon 2 nach Prüfungsvorbild und 1 Knobelaufgabe), 1 Test, 3 Korrektur, 6 Sicherung.
Prüfungsvorbilder (nur Typ und Niveau, eigene Zahlen und Einkleidung): Bayerischer Mathematik-Test 8 (ISB) 2005 A5, 2007 A3, 2008, 2009 A1, 2013 B3,
2018 A4, 2022 A6, 2023 A, 2025 A; Jahrgangsstufentest Realschule 6 (ISB) 2010 Nr. 18; VERA-8 2012 Modul C („Würfelkörper“).

    python3 -I inhalte/generatoren/messen.volumen.py
    python3 -I tools/inhalt_pruefen.py inhalte/themen/messen.volumen.json
"""
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.dont_write_bytecode = True
HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
from _luecken_neu import A, K, P, Z, aufgaben, d, fig, gr, schraeg_prisma, schraeg_quader, schreiben, wahl, z  # noqa: E402

ZIEL = HIER.parent / 'themen' / 'messen.volumen.json'
META = {'thema_schluessel': 'messen.volumen', 'thema_id': 100, 'block_id': 114, 'klasse': {'gym_by': 6}}
SEED = 7100
STUFE = {'m³': 0, 'dm³': 1, 'cm³': 2, 'mm³': 3}
NAME = {'m³': 'Kubikmeter', 'dm³': 'Kubikdezimeter', 'cm³': 'Kubikzentimeter', 'mm³': 'Kubikmillimeter'}


def ganz(b):
    out = dict(b)
    for k in ('flaeche', 'rechter_winkel', 'kreise', 'winkel'):
        out.setdefault(k, [])
    return out


def dz(R, lo, hi, schritt=Fr(1, 10)):
    while True:
        x = R.randint(int(lo / schritt), int(hi / schritt)) * schritt
        if x.denominator != 1: return x


def tab(kopf, zeilen):
    return {'typ': 'tabelle', 'kopf': kopf, 'zeilen': zeilen}


def wasser(a, b, c, hw, e='dm', lhw=True):
    """Quader (a vorn, b Tiefe, c Höhe) mit Wasser bis zur Höhe hw: Vorderseite des Wassers gefärbt, Wasserlinie rechts und hinten."""
    f = schraeg_quader(a, b, c, e)
    dd = float(b) * 0.5 / math.sqrt(2)
    pk = dict(f['punkte'])
    pk.update({'_w0': [0, float(hw)], '_w1': [float(a), float(hw)], '_w2': [round(float(a) + dd, 3), round(float(hw) + dd, 3)], '_w3': [round(dd, 3), round(float(hw) + dd, 3)]})
    lin = [x for x in f['linien']] + [['_w0', '_w1'], ['_w1', '_w2'], ['_w2', '_w3', '', 'gestrichelt']]
    if lhw:
        pk['_wt'] = [round(float(a) / 2, 3), round(float(hw) / 2, 3)]      # Beschriftung frei in der Wasserfläche (Strecke der Länge 0)
        lin.append(['_wt', '_wt', 'Wasser: ' + (gr(hw, e) if lhw is True else lhw), 'gestrichelt'])
    return {**f, 'punkte': pk, 'linien': lin, 'flaeche': ['_v0', '_v1', '_w1', '_w0']}


def treppe(stufen, tief, e='dm', labels=True):
    """Treppe: stufen = [(Breite, Höhe), …] von unten nach oben, jede Stufe beginnt links bei x = 0. Schrägbild mit Tiefe tief."""
    pts = [(0, 0)]
    y = 0
    for b, h in stufen:
        if pts[-1][0] != b: pts.append((b, y))
        y += h
        pts.append((b, y))
    pts.append((0, y))
    f = schraeg_prisma(pts, tief, e, labels={0: gr(pts[1][0], e)} if labels else {})
    if labels:
        y = 0
        f['punkte']['_l0'] = [0, 0]
        for i, (b, h) in enumerate(stufen):
            f['punkte'][f'_l{i + 1}'] = [0, float(y + h)]
            f['linien'].append([f'_l{i}', f'_l{i + 1}', gr(h, e)])
            y += h
    return f


# ---------- Bilder der Lernkarten ----------
B_EW = schraeg_quader(4, 3, 2, 'cm', gitter=True)
B_QU = schraeg_quader(6, 4, 5, 'dm')
B_EI = tab(['Einheit', 'so viel in der nächstkleineren'], [['1 m³', '1 000 dm³'], ['1 dm³', '1 000 cm³'], ['1 cm³', '1 000 mm³']])
B_LI = tab(['Volumen', 'Hohlmaß'], [['1 m³', '1 000 l'], ['1 dm³', '1 l'], ['1 cm³', '1 ml'], ['1 l', '1 000 ml']])
B_RW = wasser(6, 4, 5, 2, 'dm', lhw='? dm')
B_ZU = treppe([(6, 2), (3, 2)], 5, 'dm')
B_VE = schraeg_quader(9, 7, 3, 'm')

ETAPPEN = [
    {'lernziel': 'einheitswuerfel', 'titel': 'Volumen mit Einheitswürfeln',
     'einstieg': 'Beim Umzug soll ein Karton mit Bauklötzen gefüllt werden. Jeder Klotz ist ein Würfel mit 1 cm Kante. Wie viele passen hinein? Das ist das ⟦Volumen⟧.',
     'woerter': [['Volumen', 'wie viel Raum ein Körper einnimmt; Zeichen V'], ['Einheitswürfel', 'Würfel mit 1 cm (oder 1 dm, 1 m) Kantenlänge'],
                 ['cm³', 'Kubikzentimeter: so viel Raum wie ein Würfel mit 1 cm Kante']],
     'bild': B_EW,
     'schritte': [{'text': 'Der Karton ist 4 cm lang, 3 cm tief und 2 cm hoch.'},
                  {'text': 'Auf den Boden passt eine Schicht: 4 · 3 = 12 Einheitswürfel.', 'bild': ganz(schraeg_quader(4, 3, 1, 'cm', gitter=True))},
                  {'text': 'Es passen 2 Schichten übereinander: 2 · 12 = 24.', 'bild': ganz(B_EW)},
                  {'text': 'Das Volumen ist ⟦24 cm³⟧.'}],
     'fehler': 'Nur die sichtbaren Würfel zählen ist falsch. Innen und hinten liegen auch Würfel. Rechne Schichten mal Würfel je Schicht.',
     'regel': 'Volumen: ⟦Würfel je Schicht mal Zahl der Schichten⟧. Man misst es in cm³, dm³ oder m³.'},
    {'lernziel': 'quader', 'titel': 'Volumen von Quader und Würfel',
     'einstieg': 'Zum Umzug gibt es Kartons in vielen Größen. Wie viel passt in einen? Mit der ⟦Quaderformel⟧ rechnest du das Volumen, ohne Würfel zu zählen.',
     'woerter': [['Quaderformel', 'V = a · b · c: Länge mal Breite mal Höhe'], ['Würfel', 'Quader mit lauter gleich langen Kanten: V = a · a · a']],
     'bild': B_QU,
     'schritte': [{'text': 'Der Karton ist 6 dm lang, 4 dm breit und 5 dm hoch.'},
                  {'text': 'Boden: 6 dm · 4 dm = 24 dm². Darauf passen 24 Würfel.'},
                  {'text': 'Er ist 5 Schichten hoch: 24 · 5 = ⟦120 dm³⟧.'},
                  {'text': 'Quaderformel: V = 6 dm · 4 dm · 5 dm = 120 dm³.'},
                  {'text': 'Ein Würfel mit 3 dm Kante: 3 · 3 · 3 = 27 dm³.', 'bild': ganz(schraeg_quader(3, 3, 3, 'dm'))}],
     'fehler': 'Verschiedene Einheiten nicht einfach malnehmen. Erst umrechnen: 40 cm sind 4 dm. Dann 6 · 4 · 5.',
     'fehler_bild': ganz(schraeg_quader(6, 4, 5, 'dm', lb='40 cm')),
     'regel': 'Quader: ⟦V = a · b · c⟧. Rechne vorher alle Kanten in dieselbe Einheit um.'},
    {'lernziel': 'einheiten', 'titel': 'Volumeneinheiten umrechnen',
     'einstieg': 'Ein Würfel mit 1 dm Kante ist innen 10 cm lang, breit und hoch. Darin stecken 10 · 10 · 10 Würfelchen mit 1 cm Kante. '
                 'Darum ist die ⟦Umrechnungszahl⟧ 1 000.',
     'woerter': [['Umrechnungszahl', 'Faktor zwischen zwei benachbarten Einheiten; bei Volumen 1 000'], ['dm³', 'Kubikdezimeter: Würfel mit 1 dm Kante'],
                 ['m³', 'Kubikmeter: Würfel mit 1 m Kante']],
     'bild': B_EI,
     'schritte': [{'text': 'Gesucht: 2,5 dm³ in cm³. Von dm³ zu cm³ ist es ein Schritt.'},
                  {'text': 'Zur kleineren Einheit mal 1 000: 2,5 · 1 000 = ⟦2 500 cm³⟧.'},
                  {'text': 'Umgekehrt durch 1 000: 3 500 cm³ = 3,5 dm³.'},
                  {'text': 'Von m³ zu cm³ sind es zwei Schritte: mal 1 000 000.'}],
     'fehler': 'Nicht mit 100 umrechnen wie bei Flächen. 2,5 dm³ sind 2 500 cm³, nicht 250 cm³.',
     'fehler_bild': tab(['Rechnung', 'Ergebnis'], [['2,5 · 100', '250 cm³ – falsch'], ['2,5 · 1 000', '2 500 cm³ – richtig']]),
     'regel': 'Volumen: ⟦Umrechnungszahl 1 000⟧. Bei m³, dm³, cm³, mm³ ist jeder Schritt mal oder durch 1 000.'},
    {'lernziel': 'liter', 'titel': 'Liter und Milliliter',
     'einstieg': 'Auf der Saftpackung steht 1 l, auf der Medizinflasche 50 ml. Liter und Milliliter messen auch Volumen. Ein Liter passt genau in einen ⟦Würfel mit 1 dm Kante⟧.',
     'woerter': [['Liter (l)', '1 l = 1 dm³; so viel passt in einen Würfel mit 10 cm Kante'], ['Milliliter (ml)', '1 ml = 1 cm³; der tausendste Teil eines Liters']],
     'bild': B_LI,
     'schritte': [{'text': 'Ein Aquarium ist 50 cm lang, 30 cm breit und 40 cm hoch.', 'bild': schraeg_quader(50, 30, 40, 'cm')},
                  {'text': 'In dm: 5 dm · 3 dm · 4 dm = 60 dm³.', 'bild': ganz(schraeg_quader(5, 3, 4, 'dm'))},
                  {'text': '1 dm³ ist 1 Liter. Das Aquarium fasst ⟦60 l⟧.'},
                  {'text': 'Ein Glas mit 250 cm³ fasst 250 Milliliter.'}],
     'fehler': '1 l ist nicht 1 cm³, sondern 1 dm³. Wer 60 000 cm³ als 60 000 l liest, hat 1 000-mal zu viel.',
     'fehler_bild': tab(['', 'Liter'], [['60 000 cm³', '60 l'], ['60 000 dm³', '60 000 l']]),
     'regel': '⟦1 l = 1 dm³⟧ und 1 ml = 1 cm³. Außerdem: 1 l = 1 000 ml, 1 m³ = 1 000 l.'},
    {'lernziel': 'rueckwaerts', 'titel': 'Fehlende Kante und Füllhöhe',
     'einstieg': 'In ein leeres Aquarium werden 48 Liter Wasser gefüllt. Wie hoch steht das Wasser? Du rechnest ⟦rückwärts⟧ vom Volumen zur Höhe.',
     'woerter': [['Grundfläche', 'die Bodenfläche: Länge mal Breite'], ['Füllhöhe', 'wie hoch das Wasser im Gefäß steht']],
     'bild': B_RW,
     'schritte': [{'text': 'Das Aquarium hat eine Grundfläche von 6 dm · 4 dm = 24 dm².'},
                  {'text': '48 l sind 48 dm³. Das Wasser ist ein Quader mit diesem Boden.'},
                  {'text': 'Rückwärts: 48 : 24 = 2. Die Füllhöhe ist ⟦2 dm⟧.', 'bild': ganz(wasser(6, 4, 5, 2, 'dm'))}],
     'fehler': 'Nicht durch eine Kante teilen: 48 : 6 = 8 ist keine Höhe. Teile durch die ganze Grundfläche 24 dm².',
     'regel': 'Rückwärts: ⟦Höhe = Volumen : Grundfläche⟧. Wähle vorher passende Einheiten.'},
    {'lernziel': 'zusammengesetzt', 'titel': 'Zusammengesetzte Körper',
     'einstieg': 'Eine Stufe aus Beton ist kein Quader. Sie ist ein zusammengesetzter Körper. Du ⟦zerlegst⟧ sie in Quader und addierst deren Volumen.',
     'woerter': [['zusammengesetzter Körper', 'Körper aus mehreren Quadern'], ['Restkörper', 'was übrig bleibt, wenn man ein Stück herausschneidet']],
     'bild': B_ZU,
     'schritte': [{'text': 'Zerlege die Stufe in zwei Quader.', 'bild': {'punkte': {**B_ZU['punkte'], '_t0': [0, 2]}, 'linien': B_ZU['linien'] + [['_t0', '_v2', '', 'gestrichelt']]}},
                  {'text': 'Unten: 6 dm · 5 dm · 2 dm = 60 dm³.'},
                  {'text': 'Oben: 3 dm · 5 dm · 2 dm = 30 dm³.'},
                  {'text': 'Zusammen: 60 dm³ + 30 dm³ = ⟦90 dm³⟧.'},
                  {'text': 'Oder ergänzen: Quader 120 dm³ minus Restkörper-Lücke 30 dm³.'}],
     'fehler': 'Nicht die äußeren Maße malnehmen. 6 · 5 · 4 = 120 dm³ wäre ein ganzer Quader. Oben rechts fehlt ein Stück.',
     'fehler_bild': ganz({**B_ZU, 'punkte': {**B_ZU['punkte'], '_x1': [6, 4]}, 'linien': B_ZU['linien'] + [['_v2', '_x1', '', 'gestrichelt'], ['_x1', '_v4', 'fehlt', 'gestrichelt']]}),
     'regel': '⟦Zerlegen⟧ in Quader und addieren. Oder zum Quader ergänzen und das Fehlende abziehen.'},
    {'lernziel': 'verstehen', 'titel': 'Volumen schätzen und beurteilen',
     'einstieg': 'Wie viel Luft ist in deinem Klassenzimmer? Genau messen kannst du das nicht. Mit einem Quader findest du aber einen ⟦Näherungswert⟧.',
     'woerter': [['Näherungswert', 'ein ungefähr richtiger Wert'], ['abschätzen', 'mit runden Zahlen ungefähr ausrechnen']],
     'bild': B_VE,
     'schritte': [{'text': 'Das Zimmer ist etwa 9 m lang, 7 m breit und 3 m hoch.'},
                  {'text': 'Abschätzen: 9 m · 7 m · 3 m = ⟦189 m³⟧, rund 190 m³.'},
                  {'text': 'Schränke und Menschen brauchen auch Platz. Es bleibt ein Näherungswert.'},
                  {'text': 'Alle Kanten doppelt so lang: Volumen 2 · 2 · 2 = 8-mal so groß.'}],
     'fehler': 'Doppelt so lange Kanten heißt nicht doppeltes Volumen. Jede der drei Kanten verdoppelt sich: 8-mal so viel.',
     'regel': 'Prüfe Ergebnisse mit einem ⟦Näherungswert⟧. Doppelte Kanten ergeben das 8-fache Volumen.'},
]


# ---------- Aufgaben-Generatoren ----------
def gen_einheitswuerfel(R, st):
    if st == 1:
        a, b, c = R.randint(2, 6), R.randint(2, 5), R.randint(1, 4)
        if wahl(R, 'ew1', ['alle', 'schicht']) == 'alle':
            return Z(f'Der Quader ist aus Würfeln mit 1 cm Kante gebaut: {a} cm lang, {b} cm tief, {c} cm hoch. Wie viele Würfel sind es?', a * b * c, f'{a} * {b} * {c}',
                     f'Eine Schicht: {a} · {b} = {a * b} Würfel. {c} Schichten: {c} · {a * b} = {a * b * c} Würfel, also {a * b * c} cm³.', 'Würfel je Schicht mal Schichten.', None,
                     grafik=schraeg_quader(a, b, c, 'cm', gitter=True))
        return Z(f'Ein Quader ist {a} cm lang, {b} cm tief und {c} cm hoch. Wie viele Einheitswürfel (1 cm³) liegen in der untersten Schicht?', a * b, f'{a} * {b}',
                 f'Die unterste Schicht ist {a} Würfel lang und {b} Würfel tief: {a} · {b} = {a * b}.', 'Nur die Bodenschicht zählen.', None,
                 grafik=schraeg_quader(a, b, c, 'cm', gitter=True))
    if st == 2:
        art = wahl(R, 'ew2', ['wuerfel', 'dm_cm', 'schichten', 'vorstellung', 'zwei_cm'])
        if art == 'wuerfel':
            a = R.randint(2, 6)
            return Z(f'Ein großer Würfel mit {a} cm Kantenlänge soll aus Würfeln mit 1 cm Kante gebaut werden. Wie viele kleine Würfel braucht man?', a ** 3, f'{a} * {a} * {a}',
                     f'Eine Schicht: {a} · {a} = {a * a}. {a} Schichten: {a * a} · {a} = {a ** 3}.', 'Würfel je Schicht mal Schichten.', None)
        if art == 'dm_cm':
            n = R.choice([2, 3, 4, 5])
            return Z(f'Wie viele Würfel mit 1 cm Kante passen in {n} Würfel mit je 1 dm Kante?', n * 1000, f'{n} * 10 * 10 * 10',
                     f'1 dm = 10 cm. In einen dm-Würfel passen 10 · 10 · 10 = 1 000 Zentimeterwürfel. {n} solche: {z(n * 1000)}.', 'Wie viele cm sind 1 dm?', None)
        if art == 'schichten':
            a, b, c = R.randint(3, 8), R.randint(2, 6), R.randint(2, 6)
            return Z(f'Ein Quader aus {a * b * c} Würfeln hat in jeder Schicht {a * b} Würfel. Wie viele Schichten hat er?', c, f'{a * b * c} / {a * b}',
                     f'{a * b * c} : {a * b} = {c} Schichten.', 'Wie oft passt eine Schicht hinein?', None)
        if art == 'vorstellung':
            obj, rich, fal = R.choice([('ein Zuckerwürfel', '1 cm³', ['1 dm³', '1 m³', '1 mm³']), ('eine Milchtüte (1 l)', '1 dm³', ['1 cm³', '1 m³', '10 cm³']),
                                       ('ein Kühlschrank', 'etwa 0,3 m³', ['etwa 3 m³', 'etwa 30 dm³', 'etwa 300 cm³']), ('ein Stecknadelkopf', 'etwa 1 mm³', ['etwa 1 cm³', 'etwa 1 dm³', 'etwa 1 m³'])])
            return A(R, f'Welches Volumen hat ungefähr {obj}?', rich, fal, f'{obj[0].upper() + obj[1:]} hat ungefähr {rich.replace("etwa ", "")}. Vergleiche: 1 cm³ ist ein Zuckerwürfel, 1 dm³ eine Milchtüte, 1 m³ eine große Kiste.',
                     'Denke an Zuckerwürfel (cm³) und Milchtüte (dm³).')
        a, b, c = R.choice([(10, 6, 4), (8, 6, 4), (12, 8, 6), (10, 10, 4), (14, 6, 4), (8, 8, 8)])
        return Z(f'Ein Karton ist innen {a} cm lang, {b} cm breit und {c} cm hoch. Wie viele Würfel mit 2 cm Kante passen hinein?', (a // 2) * (b // 2) * (c // 2),
                 f'({a} / 2) * ({b} / 2) * ({c} / 2)', f'Je Richtung passen {a // 2}, {b // 2} und {c // 2} Würfel: {a // 2} · {b // 2} · {c // 2} = {(a // 2) * (b // 2) * (c // 2)}.',
                 'Wie viele 2-cm-Würfel passen in jede Richtung?', None)
    art = wahl(R, 'ew3', ['loch', 'stapel', 'turm', 'rot', 'verteilen'])
    if art == 'loch':
        a, b, c = R.randint(4, 6), R.randint(3, 5), R.randint(3, 4)
        k = R.randint(1, 2)
        return Z(f'Ein Quader aus 1-cm-Würfeln ist {a} cm · {b} cm · {c} cm groß. Aus einer Ecke wird ein Würfel mit {k + 1} cm Kante herausgenommen. Wie viele kleine Würfel bleiben?',
                 a * b * c - (k + 1) ** 3, f'{a} * {b} * {c} - {k + 1} * {k + 1} * {k + 1}',
                 f'Vorher {a * b * c} Würfel. Die Ecke besteht aus {k + 1} · {k + 1} · {k + 1} = {(k + 1) ** 3} Würfeln. Es bleiben {a * b * c - (k + 1) ** 3}.', 'Erst alle, dann die Ecke abziehen.', None)
    if art == 'stapel':
        n, s = R.randint(3, 6), R.randint(4, 9)
        return Z(f'In einem Regal liegen {n} gleiche Stapel. Jeder Stapel hat {s} Schichten aus je 6 Würfeln (1 cm³). Wie viel cm³ sind es zusammen?', n * s * 6, f'{n} * {s} * 6',
                 f'Ein Stapel: {s} · 6 = {s * 6} cm³. {n} Stapel: {n * s * 6} cm³.', 'Ein Stapel zuerst.', 'cm³')
    if art == 'turm':
        n = R.randint(3, 6)
        summe = sum(k * k for k in range(1, n + 1))
        return Z(f'Eine Pyramide aus Würfeln hat {n} Schichten: oben 1 Würfel, darunter 2 · 2, dann 3 · 3 und so weiter. Wie viele Würfel sind es?', summe,
                 ' + '.join(f'{k} * {k}' for k in range(1, n + 1)), f'{" + ".join(str(k * k) for k in range(1, n + 1))} = {summe}.', 'Zähle jede Schicht einzeln.', None)
    if art == 'rot':
        n = R.randint(3, 6)
        return Z(f'Ein Würfel aus {n} · {n} · {n} kleinen Würfeln wird außen rot angemalt. Wie viele kleine Würfel haben gar keine rote Fläche?', (n - 2) ** 3,
                 f'({n} - 2) * ({n} - 2) * ({n} - 2)', f'Ohne Farbe sind nur die inneren Würfel: in jeder Richtung {n} − 2 = {n - 2}. Also {n - 2} · {n - 2} · {n - 2} = {(n - 2) ** 3}.',
                 'Welche Würfel berühren den Rand nicht?', None)
    a, b = R.randint(3, 6), R.randint(3, 6)
    c = R.randint(2, 5)
    return Z(f'{a * b * c} gleiche Würfel sollen zu einem Quader mit einer Grundfläche von {a} · {b} Würfeln gestapelt werden. Wie hoch wird der Quader (in Würfeln)?', c,
             f'{a * b * c} / ({a} * {b})', f'Eine Schicht: {a} · {b} = {a * b}. {a * b * c} : {a * b} = {c} Schichten.', 'Wie viele Würfel hat eine Schicht?', None)


def gen_quader(R, st):
    if st == 1:
        e = R.choice(['cm', 'dm', 'm'])
        if wahl(R, 'qu1', ['quader', 'wuerfel']) == 'quader':
            a, b, c = R.randint(2, 12), R.randint(2, 9), R.randint(2, 8)
            return Z(f'Berechne das Volumen des Quaders: {a} {e} lang, {b} {e} breit, {c} {e} hoch.', a * b * c, f'{a} * {b} * {c}',
                     f'V = a · b · c = {a} {e} · {b} {e} · {c} {e} = {gr(a * b * c, e + "³")}.', 'Länge mal Breite mal Höhe.', e + '³', grafik=schraeg_quader(a, b, c, e))
        a = R.randint(2, 10)
        return Z(f'Ein Würfel hat {a} {e} Kantenlänge. Wie groß ist sein Volumen?', a ** 3, f'{a} * {a} * {a}', f'V = {a} · {a} · {a} = {gr(a ** 3, e + "³")}.',
                 'Beim Würfel sind alle Kanten gleich.', e + '³', grafik=schraeg_quader(a, a, a, e))
    if st == 2:
        art = wahl(R, 'qu2', ['dez', 'einheit', 'wuerfel_dez', 'sand', 'auswahl'])
        if art == 'dez':
            a, b, c = dz(R, 1, 9, Fr(1, 2)), R.randint(2, 8), R.choice([2, 4, 5, 10])
            return Z(f'Ein Quader ist {gr(a, "cm")} lang, {b} cm breit und {c} cm hoch. Berechne sein Volumen.', a * b * c, f'{d(a)} * {b} * {c}',
                     f'V = {z(a)} · {b} · {c} = {gr(a * b * c, "cm³")}.', 'Auch mit Kommazahlen: a · b · c.', 'cm³', grafik=schraeg_quader(a, b, c, 'cm'))
        if art == 'einheit':
            am, bdm, ccm = Fr(R.randint(1, 3)), R.randint(3, 9), R.choice([20, 30, 40, 50])
            V = am * 10 * bdm * Fr(ccm, 10)
            return Z(f'Eine Kiste ist {z(am)} m lang, {bdm} dm breit und {ccm} cm hoch. Wie groß ist ihr Volumen in dm³?', V, f'{d(am)} * 10 * {bdm} * {ccm} / 10',
                     f'In dm: {z(am * 10)} dm, {bdm} dm, {z(Fr(ccm, 10))} dm. V = {z(am * 10)} · {bdm} · {z(Fr(ccm, 10))} = {gr(V, "dm³")}.', 'Alle Kanten zuerst in dm.', 'dm³')
        if art == 'wuerfel_dez':
            a = R.choice([Fr(3, 2), Fr(5, 2), Fr(1, 2), Fr(12, 10), Fr(2, 10), Fr(3, 10)])
            return Z(f'Ein Würfel hat die Kantenlänge {gr(a, "m")}. Berechne sein Volumen in m³.', a ** 3, f'{d(a)} * {d(a)} * {d(a)}', f'V = {z(a)} · {z(a)} · {z(a)} = {gr(a ** 3, "m³")}.',
                     'Dreimal die Kante.', 'm³')
        if art == 'sand':
            a, b, c = Fr(R.choice([2, 3])), Fr(R.choice([15, 20, 25]), 10), Fr(R.choice([2, 3, 4]), 10)
            return Z(f'Ein Sandkasten ist {z(a)} m lang und {z(b)} m breit. Er wird {z(c * 100)} cm hoch mit Sand gefüllt. Wie viele m³ Sand braucht man?', a * b * c,
                     f'{d(a)} * {d(b)} * {d(c)}', f'{z(c * 100)} cm = {z(c)} m. V = {z(a)} · {z(b)} · {z(c)} = {gr(a * b * c, "m³")}.', 'Die Höhe zuerst in m.', 'm³')
        a, b, c = R.randint(3, 9), R.randint(2, 6), R.randint(2, 5)
        return A(R, f'Ein Quader ist {a} cm lang, {b} cm breit und {c} cm hoch. Welche Rechnung liefert sein Volumen?', f'{a} · {b} · {c}',
                 [f'{a} + {b} + {c}', f'2 · ({a} · {b} + {a} · {c} + {b} · {c})', f'4 · ({a} + {b} + {c})'],
                 f'V = a · b · c = {a * b * c} cm³. Die anderen Rechnungen geben a + b + c, die Oberfläche bzw. die Länge aller 12 Kanten.', 'Volumen: Länge mal Breite mal Höhe.')
    art = wahl(R, 'qu3', ['wuerfel_kante', 'kanten', 'vergleich', 'preis', 'stapel'])
    if art == 'wuerfel_kante':
        a = R.randint(2, 10)
        return Z(f'Ein Würfel hat das Volumen {z(a ** 3)} cm³. Wie lang ist eine Kante?', a, f'{a}', f'Probieren: {a} · {a} · {a} = {z(a ** 3)}. Die Kante ist {a} cm lang.',
                 'Welche Zahl dreimal mit sich selbst malgenommen ergibt das Volumen?', 'cm')
    if art == 'kanten':
        a, b, c = R.randint(3, 9), R.randint(2, 7), R.randint(2, 6)
        k = 4 * (a + b + c)
        return Z(f'Das Kantenmodell eines Quaders braucht {k} cm Draht. Er ist {a} cm lang und {b} cm breit. Wie groß ist sein Volumen?', a * b * c, f'{a} * {b} * ({k} / 4 - {a} - {b})',
                 f'Je 4 Kanten sind gleich lang: {k} : 4 = {k // 4} cm = Länge + Breite + Höhe. Höhe: {k // 4} − {a} − {b} = {c} cm. V = {a} · {b} · {c} = {a * b * c} cm³.',
                 'Ein Quader hat je 4 gleich lange Kanten.', 'cm³')
    if art == 'vergleich':
        a, b, c = R.randint(3, 8), R.randint(3, 8), R.randint(2, 6)
        a2, b2, c2 = b, c, a + 1
        return Z(f'Karton A ist {a} dm · {b} dm · {c} dm groß, Karton B {a2} dm · {b2} dm · {c2} dm. Um wie viel dm³ ist B größer als A?', a2 * b2 * c2 - a * b * c,
                 f'{a2} * {b2} * {c2} - {a} * {b} * {c}', f'A: {a * b * c} dm³. B: {a2 * b2 * c2} dm³. Unterschied: {a2 * b2 * c2 - a * b * c} dm³.', 'Rechne beide aus.', 'dm³')
    if art == 'preis':
        a, b, c = Fr(R.choice([4, 5, 6])), Fr(R.choice([3, 4])), Fr(R.choice([5, 8]), 10)
        p = R.choice([90, 110, 120])
        return Z(f'Für ein Fundament ({z(a)} m lang, {z(b)} m breit, {z(c * 100)} cm tief) wird Beton bestellt. 1 m³ kostet {p} €. Wie teuer ist der Beton?', a * b * c * p,
                 f'{d(a)} * {d(b)} * {d(c)} * {p}', f'V = {z(a)} · {z(b)} · {z(c)} = {gr(a * b * c, "m³")}. Preis: {z(a * b * c)} · {p} € = {z(a * b * c * p)} €.',
                 'Tiefe in m, Volumen, dann der Preis.', '€')
    n = R.choice([2, 3, 4])
    a, b, c = R.randint(3, 6), R.randint(2, 4), R.randint(1, 3)
    return Z(f'{n * n * n} gleiche Päckchen ({a} cm · {b} cm · {c} cm) werden zu einem großen Paket gestapelt: {n} in die Länge, {n} in die Breite, {n} in die Höhe. '
             f'Wie groß ist das Volumen des großen Pakets?', (n * a) * (n * b) * (n * c), f'({n} * {a}) * ({n} * {b}) * ({n} * {c})',
             f'Maße: {n * a} cm · {n * b} cm · {n * c} cm = {z((n * a) * (n * b) * (n * c))} cm³. Probe: {n ** 3} · {a * b * c} cm³ = {z(n ** 3 * a * b * c)} cm³.',
             'Rechne die Maße des großen Pakets aus – oder Päckchen mal Volumen.', 'cm³')


def _um(R, st):
    paare = [('dm³', 'cm³'), ('cm³', 'mm³'), ('m³', 'dm³'), ('cm³', 'dm³'), ('dm³', 'm³'), ('mm³', 'cm³')]
    if st >= 2: paare += [('m³', 'cm³'), ('cm³', 'm³')]
    return R.choice(paare)


def gen_einheiten(R, st):
    von, nach = _um(R, st)
    schritte = STUFE[nach] - STUFE[von]
    f = Fr(1000) ** schritte
    if st == 1:
        x = R.randint(2, 30) if schritte > 0 else R.randint(1, 30) * 1000
        return Z(f'Rechne um: {gr(x, von)} = ? {nach}', x * f, f'{x} * {d(f)}' if f >= 1 else f'{x} / {d(1 / f)}',
                 f'{"Zur kleineren Einheit mal" if f > 1 else "Zur größeren Einheit durch"} {z(f if f > 1 else 1 / f)}: {gr(x, von)} = {gr(x * f, nach)}.',
                 'Bei Volumen ist die Umrechnungszahl 1 000.', nach)
    if st == 2:
        art = wahl(R, 'ei2', ['komma', 'gemischt', 'groesste', 'zwei'])
        if art == 'komma':
            x = dz(R, Fr(1, 10), 9, Fr(1, 100)) if schritte > 0 else Fr(R.randint(5, 999))
            w = x * f
            if w.denominator not in (1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000) or (abs(schritte) != 1): return gen_einheiten(R, st)
            return Z(f'Rechne um: {gr(x, von)} = ? {nach}', w, f'{d(x)} * {d(f)}' if f >= 1 else f'{d(x)} / {d(1 / f)}',
                     f'{"Mal" if f > 1 else "Durch"} 1 000: {gr(x, von)} = {gr(w, nach)}.', 'Verschiebe das Komma um drei Stellen.', nach)
        if art == 'gemischt':
            a, b = R.randint(1, 9), R.randint(5, 950)
            return Z(f'Schreibe {a} m³ {b} dm³ in m³ (Kommazahl).', a + Fr(b, 1000), f'{a} + {b} / 1000', f'{b} dm³ = {z(Fr(b, 1000))} m³. Zusammen {z(a + Fr(b, 1000))} m³.',
                     'Jede kleinere Einheit bekommt drei Stellen nach dem Komma.', 'm³')
        if art == 'groesste':
            return A(R, 'Welche Angabe ist das größte Volumen?', '2 500 cm³', ['2,1 dm³', '0,3 dm³', '300 000 mm³'],
                     'In dm³: 2 500 cm³ = 2,5 dm³, 2,1 dm³, 0,3 dm³, 300 000 mm³ = 0,3 dm³. Am größten: 2 500 cm³.', 'Rechne alles in dm³ um.')
        x = R.randint(2, 9)
        return Z(f'Rechne um: {x} m³ = ? cm³', x * 1000000, f'{x} * 1000 * 1000', f'Zwei Schritte: m³ → dm³ → cm³, also mal 1 000 000. {x} m³ = {z(x * 1000000)} cm³.',
                 'Von m³ über dm³ zu cm³.', 'cm³')
    art = wahl(R, 'ei3', ['summe', 'fehler', 'kette', 'ordnen', 'liter_nein'])
    if art == 'summe':
        a, b, c = R.randint(1, 5), R.randint(100, 900), R.randint(10, 900)
        return Z(f'Berechne {a} dm³ + {b} cm³ + {c} mm³ in cm³.', a * 1000 + b + Fr(c, 1000), f'{a} * 1000 + {b} + {c} / 1000',
                 f'{a} dm³ = {z(a * 1000)} cm³, {c} mm³ = {z(Fr(c, 1000))} cm³. Summe: {z(a * 1000 + b + Fr(c, 1000))} cm³.', 'Erst alles in cm³ umrechnen.', 'cm³')
    if art == 'fehler':
        x = dz(R, 1, 9, Fr(1, 10))
        return A(R, f'Tom rechnet: {z(x)} dm³ = {z(x * 100)} cm³. Was stimmt?', f'Falsch, richtig ist {z(x * 1000)} cm³ (mal 1 000).',
                 ['Richtig, man rechnet mal 100.', f'Falsch, richtig ist {z(x * 10)} cm³.', f'Falsch, richtig ist {z(x * 10000)} cm³.'],
                 f'Bei Volumen ist die Umrechnungszahl 1 000: {z(x)} · 1 000 = {z(x * 1000)} cm³. Mal 100 gilt bei Flächen.', 'Wie viele cm³ hat 1 dm³?')
    if art == 'kette':
        x = R.choice([Fr(5, 1000), Fr(25, 1000), Fr(4, 100), Fr(125, 1000), Fr(7, 1000)])
        return Z(f'Rechne um: {gr(x, "m³")} = ? cm³', x * 1000000, f'{d(x)} * 1000000', f'{z(x)} m³ = {z(x * 1000)} dm³ = {z(x * 1000000)} cm³.', 'Zwei Schritte mal 1 000.', 'cm³')
    if art == 'ordnen':
        return A(R, 'Welche Reihenfolge ist von klein nach groß richtig?', '800 cm³ < 1 dm³ < 1 200 cm³ < 0,002 m³',
                 ['1 dm³ < 800 cm³ < 0,002 m³ < 1 200 cm³', '0,002 m³ < 800 cm³ < 1 dm³ < 1 200 cm³', '800 cm³ < 0,002 m³ < 1 dm³ < 1 200 cm³'],
                 'In cm³: 800, 1 000, 1 200 und 0,002 m³ = 2 000 cm³.', 'Rechne alles in cm³ um.')
    x = R.randint(2, 9)
    return Z(f'Ein Würfel mit {x} cm Kante wird in Würfel mit 1 mm Kante zerlegt. Wie viele sind es?', (10 * x) ** 3, f'({x} * 10) ** 3',
             f'{x} cm = {10 * x} mm. Würfelchen: {10 * x} · {10 * x} · {10 * x} = {z((10 * x) ** 3)}. Das sind {x ** 3} cm³ = {z(x ** 3 * 1000)} mm³.', 'Rechne die Kante in mm um.', None)


def gen_liter(R, st):
    if st == 1:
        art = wahl(R, 'li1', ['l_ml', 'ml_l', 'dm_l', 'cm_ml'])
        if art == 'l_ml':
            x = R.choice([Fr(1, 2), Fr(1, 4), Fr(3, 4), Fr(2), Fr(3, 2), Fr(5), Fr(1, 5)])
            return Z(f'Rechne um: {gr(x, "l")} = ? ml', x * 1000, f'{d(x)} * 1000', f'1 l = 1 000 ml, also {gr(x, "l")} = {z(x * 1000)} ml.', '1 l = 1 000 ml.', 'ml')
        if art == 'ml_l':
            x = R.choice([250, 500, 750, 1500, 2000, 330, 200])
            return Z(f'Rechne um: {z(x)} ml = ? l', Fr(x, 1000), f'{x} / 1000', f'Durch 1 000: {z(x)} ml = {z(Fr(x, 1000))} l.', '1 000 ml sind 1 l.', 'l')
        if art == 'dm_l':
            x = R.randint(2, 90)
            return Z(f'Ein Eimer fasst {x} dm³. Wie viele Liter sind das?', x, f'{x}', f'1 dm³ = 1 l, also {x} dm³ = {x} l.', 'Wie viel ist 1 dm³ in Liter?', 'l')
        x = R.randint(20, 900)
        return Z(f'Ein Becher fasst {x} cm³. Wie viele ml sind das?', x, f'{x}', f'1 cm³ = 1 ml, also {x} cm³ = {x} ml.', 'Wie viel ist 1 cm³ in ml?', 'ml')
    if st == 2:
        art = wahl(R, 'li2', ['aquarium', 'm3', 'glaeser', 'flasche', 'dm3_ml'])
        if art == 'aquarium':
            a, b, c = R.choice([40, 50, 60, 80, 100]), R.choice([20, 30, 40]), R.choice([30, 40, 50])
            V = Fr(a * b * c, 1000)
            return Z(f'Ein Aquarium ist {a} cm lang, {b} cm breit und {c} cm hoch. Wie viele Liter fasst es?', V, f'{a} * {b} * {c} / 1000',
                     f'In dm: {z(Fr(a, 10))} · {z(Fr(b, 10))} · {z(Fr(c, 10))} = {z(V)} dm³ = {z(V)} l.', 'Rechne in dm um, dann ist dm³ gleich Liter.', 'l',
                     grafik=schraeg_quader(a, b, c, 'cm'))
        if art == 'm3':
            x = R.choice([Fr(3, 2), Fr(5, 2), Fr(12), Fr(1, 2), Fr(3, 4), Fr(30)])
            return Z(f'{"Ein Planschbecken" if x < 2 else "Ein Pool"} fasst {gr(x, "m³")} Wasser. Wie viele Liter sind das?', x * 1000, f'{d(x)} * 1000', f'1 m³ = 1 000 dm³ = 1 000 l. {gr(x, "m³")} = {z(x * 1000)} l.',
                     'Wie viele dm³ hat 1 m³?', 'l')
        if art == 'glaeser':
            fl, gl = R.choice([(Fr(3, 2), 250), (Fr(1), 200), (Fr(3, 4), 150), (Fr(2), 250), (Fr(1, 2), 125), (Fr(3), 200)])
            return Z(f'Aus einer Flasche mit {gr(fl, "l")} Saft werden Gläser mit je {gl} ml gefüllt. Wie viele volle Gläser gibt es?', fl * 1000 / gl, f'{d(fl)} * 1000 / {gl}',
                     f'{gr(fl, "l")} = {z(fl * 1000)} ml. {z(fl * 1000)} : {gl} = {z(fl * 1000 / gl)} Gläser.', 'Rechne die Flasche in ml um.', None)
        if art == 'flasche':
            x = R.choice([Fr(33, 100), Fr(75, 100), Fr(15, 10), Fr(5, 100), Fr(2, 10)])
            return Z(f'Eine Flasche enthält {gr(x, "l")}. Wie viel cm³ sind das?', x * 1000, f'{d(x)} * 1000', f'{gr(x, "l")} = {z(x * 1000)} ml = {z(x * 1000)} cm³.',
                     '1 l = 1 000 ml und 1 ml = 1 cm³.', 'cm³')
        x = dz(R, Fr(1, 10), 5, Fr(1, 10))
        return Z(f'Rechne um: {gr(x, "dm³")} = ? ml', x * 1000, f'{d(x)} * 1000', f'{gr(x, "dm³")} = {gr(x, "l")} = {z(x * 1000)} ml.', '1 dm³ = 1 l = 1 000 ml.', 'ml')
    art = wahl(R, 'li3', ['regen_flaeche', 'rand', 'tank', 'vergleich', 'eimer'])
    if art == 'regen_flaeche':
        mm, fl = R.choice([(4, 25), (6, 50), (12, 20), (8, 15), (5, 120)])
        return Z(f'Auf ein Garagendach mit {fl} m² fallen {mm} mm Regen. Wie viele Liter Wasser sind das?', mm * fl, f'{mm} * {fl}',
                 f'Auf 1 m² ist das ein Quader 10 dm · 10 dm · {z(Fr(mm, 100))} dm = {mm} dm³ = {mm} l. Auf {fl} m²: {mm} · {fl} = {mm * fl} l.',
                 'Wie viel Wasser fällt auf 1 m²? Rechne in dm.', 'l')
    if art == 'rand':
        a, b, c, r = R.choice([(60, 30, 40, 5), (80, 40, 50, 10), (100, 40, 50, 5), (50, 25, 30, 4)])
        V = Fr(a * b * (c - r), 1000)
        return Z(f'Ein Aquarium ({a} cm lang, {b} cm breit, {c} cm hoch) wird bis {r} cm unter den Rand gefüllt. Wie viele Liter Wasser sind darin?', V, f'{a} * {b} * ({c} - {r}) / 1000',
                 f'Wasserhöhe: {c} − {r} = {c - r} cm. V = {a} · {b} · {c - r} = {z(a * b * (c - r))} cm³ = {z(V)} l.', 'Wie hoch steht das Wasser?', 'l',
                 grafik=wasser(a, b, c, c - r, 'cm'))
    if art == 'tank':
        a, b, c = Fr(R.choice([2, 3])), Fr(R.choice([1, 2])), Fr(R.choice([5, 8]), 10)
        t = R.choice([20, 25, 40, 50])
        V = a * b * c * 1000
        if (V / t).denominator != 1: return gen_liter(R, st)
        return Z(f'Ein Regentank ist {z(a)} m lang, {z(b)} m breit und {z(c)} m hoch. Pro Tag werden {t} l für den Garten entnommen. Nach wie vielen Tagen ist der volle Tank leer?',
                 V / t, f'{d(a)} * {d(b)} * {d(c)} * 1000 / {t}', f'V = {z(a)} · {z(b)} · {z(c)} = {z(a * b * c)} m³ = {z(V)} l. {z(V)} : {t} = {z(V / t)} Tage.',
                 'Erst das Volumen in Liter.', None)
    if art == 'vergleich':
        return A(R, 'Welcher Behälter fasst am meisten?', 'ein Würfel mit 2 dm Kante', ['eine 5-l-Flasche', '6 000 cm³ in einer Schüssel', 'ein Quader 10 cm · 10 cm · 50 cm'],
                 'Würfel: 2 · 2 · 2 = 8 dm³ = 8 l. Die Flasche fasst 5 l, die Schüssel 6 l, der Quader 1 · 1 · 5 = 5 dm³ = 5 l.', 'Rechne alles in Liter um.')
    n, v = R.choice([(12, 10), (8, 15), (20, 5), (15, 12)])
    a, b = R.choice([(50, 40), (60, 40), (80, 50)])
    return Z(f'Ein Kind gießt {n} Eimer mit je {v} l Wasser in ein leeres Becken ({a} cm lang, {b} cm breit). Wie hoch steht das Wasser in cm?', Fr(n * v * 1000, a * b),
             f'{n} * {v} * 1000 / ({a} * {b})', f'Wasser: {n} · {v} = {n * v} l = {z(n * v * 1000)} cm³. Grundfläche {a} · {b} = {z(a * b)} cm². Höhe: {z(n * v * 1000)} : {z(a * b)} = {z(Fr(n * v * 1000, a * b))} cm.',
             'Liter in cm³, dann durch die Grundfläche.', 'cm') if Fr(n * v * 1000, a * b).denominator in (1, 2, 4, 5, 10) else gen_liter(R, st)


def gen_rueckwaerts(R, st):
    if st == 1:
        a, b, c = R.randint(2, 10), R.randint(2, 8), R.randint(2, 9)
        if wahl(R, 'rw1', ['hoehe', 'breite']) == 'hoehe':
            return Z(f'Ein Quader hat {a * b * c} cm³. Er ist {a} cm lang und {b} cm breit. Wie hoch ist er?', c, f'{a * b * c} / ({a} * {b})',
                     f'Grundfläche: {a} · {b} = {a * b} cm². Höhe: {a * b * c} : {a * b} = {c} cm.', 'Volumen durch Grundfläche.', 'cm', grafik=schraeg_quader(a, b, c, 'cm', lc='?'))
        return Z(f'Ein Quader hat {a * b * c} dm³. Er ist {a} dm lang und {c} dm hoch. Wie breit ist er?', b, f'{a * b * c} / ({a} * {c})',
                 f'{a} · {c} = {a * c}. {a * b * c} : {a * c} = {b} dm.', 'Teile durch das Produkt der beiden bekannten Kanten.', 'dm')
    if st == 2:
        art = wahl(R, 'rw2', ['fuell', 'grundflaeche', 'dez', 'liter_hoehe'])
        if art == 'fuell':
            a, b = R.choice([(6, 4), (5, 4), (8, 5), (10, 4), (5, 3)])
            hw = R.choice([Fr(3, 2), Fr(2), Fr(5, 2), Fr(3), Fr(1)])
            c = int(hw) + 2
            return Z(f'Ein Aquarium hat einen Boden von {a} dm · {b} dm. Es werden {z(a * b * hw)} l Wasser eingefüllt. Wie hoch steht das Wasser?', hw, f'{d(a * b * hw)} / ({a} * {b})',
                     f'{z(a * b * hw)} l = {z(a * b * hw)} dm³. Grundfläche {a * b} dm². Füllhöhe: {z(a * b * hw)} : {a * b} = {gr(hw, "dm")}.', 'Liter sind dm³. Dann durch die Grundfläche.', 'dm',
                     grafik=wasser(a, b, c, hw, 'dm', lhw='? dm'))
        if art == 'grundflaeche':
            G, h = R.randint(12, 60), R.randint(2, 9)
            return Z(f'Ein Quader hat das Volumen {G * h} cm³ und ist {h} cm hoch. Wie groß ist seine Grundfläche?', G, f'{G * h} / {h}',
                     f'Grundfläche · Höhe = Volumen. {G * h} : {h} = {G} cm².', 'Volumen durch Höhe.', 'cm²')
        if art == 'dez':
            a, b = R.choice([(4, 5), (2, 5), (8, 5), (4, 2)])
            c = dz(R, 1, 9, Fr(1, 10))
            return Z(f'Ein Quader hat {gr(a * b * c, "m³")}, eine Länge von {a} m und eine Breite von {b} m. Wie hoch ist er?', c, f'{d(a * b * c)} / ({a} * {b})',
                     f'{a} · {b} = {a * b} m². {z(a * b * c)} : {a * b} = {gr(c, "m")}.', 'Volumen durch Grundfläche.', 'm')
        a, b = R.choice([(50, 40), (40, 30), (60, 50), (80, 25)])
        h = R.choice([10, 15, 20, 30])
        L_ = Fr(a * b * h, 1000)
        return Z(f'In ein leeres Becken ({a} cm lang, {b} cm breit) werden {z(L_)} l Wasser gegossen. Wie hoch steht das Wasser in cm?', h, f'{d(L_)} * 1000 / ({a} * {b})',
                 f'{z(L_)} l = {z(L_ * 1000)} cm³. Grundfläche: {a} · {b} = {z(a * b)} cm². Höhe: {z(L_ * 1000)} : {z(a * b)} = {h} cm.', 'Liter in cm³ umrechnen.', 'cm')
    art = wahl(R, 'rw3', ['umfuellen', 'wuerfel_gleich', 'stein', 'kiste', 'karton'])
    if art == 'umfuellen':
        a1, b1, h1 = R.choice([(20, 20, 15), (30, 20, 10), (40, 10, 30), (25, 20, 12)])
        a2, b2 = R.choice([(30, 10), (40, 20), (50, 20), (20, 15)])
        h2 = Fr(a1 * b1 * h1, a2 * b2)
        if h2.denominator not in (1, 2, 4, 5, 10): return gen_rueckwaerts(R, st)
        return Z(f'Wasser steht in Gefäß A ({a1} cm · {b1} cm Grundfläche) {h1} cm hoch. Es wird in Gefäß B ({a2} cm · {b2} cm Grundfläche) umgefüllt. Wie hoch steht es dort?', h2,
                 f'{a1} * {b1} * {h1} / ({a2} * {b2})', f'Wasser: {a1} · {b1} · {h1} = {z(a1 * b1 * h1)} cm³. In B: {z(a1 * b1 * h1)} : {a2 * b2} = {z(h2)} cm.',
                 'Das Volumen bleibt gleich.', 'cm')
    if art == 'wuerfel_gleich':
        a, b = R.choice([(2, 54), (3, 24), (4, 32), (5, 40), (6, 48)])
        k = round((a * a * b) ** (1 / 3))
        assert k ** 3 == a * a * b
        return Z(f'Eine Säule ist {a} cm lang, {a} cm breit und {b} cm hoch. Ein Würfel soll das gleiche Volumen haben. Wie lang ist seine Kante?', k, f'{k}',
                 f'V = {a} · {a} · {b} = {z(a * a * b)} cm³. Probieren: {k} · {k} · {k} = {z(k ** 3)}. Die Kante ist {k} cm.', 'Welche Zahl dreimal malgenommen ergibt das Volumen?', 'cm')
    if art == 'stein':
        a, b, s = R.choice([(40, 25, 2), (50, 30, 1), (60, 40, 3), (30, 20, 5)])
        return Z(f'Ein Stein wird in ein Aquarium ({a} cm · {b} cm Grundfläche) gelegt und ist ganz unter Wasser. Das Wasser steigt um {s} cm. Wie groß ist das Volumen des Steins?',
                 a * b * s, f'{a} * {b} * {s}', f'Der Stein verdrängt genau sein Volumen: {a} · {b} · {s} = {z(a * b * s)} cm³.', 'Das gestiegene Wasser ist ein flacher Quader.', 'cm³')
    if art == 'kiste':
        a, b, c = R.choice([(40, 30, 20), (50, 40, 30), (60, 40, 25)])
        f = R.choice([Fr(1, 2), Fr(3, 4), Fr(1, 4)])
        return Z(f'Eine Kiste ({a} cm · {b} cm · {c} cm) ist zu {"halb" if f == Fr(1, 2) else ("drei Viertel" if f == Fr(3, 4) else "einem Viertel")} mit Sand gefüllt. '
                 f'Wie viele Liter Sand sind darin?', Fr(a * b * c, 1000) * f, f'{a} * {b} * {c} / 1000 * {d(f)}',
                 f'Ganze Kiste: {z(Fr(a * b * c, 1000))} l. Davon {"die Hälfte" if f == Fr(1, 2) else ("drei Viertel" if f == Fr(3, 4) else "ein Viertel")}: {z(Fr(a * b * c, 1000) * f)} l.',
                 'Erst die ganze Kiste in Liter.', 'l')
    V, a, b = R.choice([(48, 60, 40), (96, 80, 40), (36, 40, 30), (54, 60, 30)])
    h = Fr(V * 1000, a * b)
    return Z(f'Ein Umzugskarton fasst {V} l. Er ist {a} cm lang und {b} cm breit. Wie hoch ist er?', h, f'{V} * 1000 / ({a} * {b})',
             f'{V} l = {z(V * 1000)} cm³. Grundfläche {z(a * b)} cm². Höhe: {z(V * 1000)} : {z(a * b)} = {z(h)} cm.', 'Liter in cm³.', 'cm')


def gen_zusammengesetzt(R, st):
    if st == 1:
        a, h1, a2, h2, t = R.randint(5, 9), R.randint(1, 3), R.randint(2, 4), R.randint(1, 3), R.randint(3, 6)
        if a2 >= a: return gen_zusammengesetzt(R, st)
        V = a * h1 * t + a2 * h2 * t
        return Z(f'Die Stufe besteht aus zwei Quadern: unten {a} dm · {t} dm · {h1} dm, oben {a2} dm · {t} dm · {h2} dm. Wie groß ist ihr Volumen?', V,
                 f'{a} * {t} * {h1} + {a2} * {t} * {h2}', f'Unten {a * t * h1} dm³, oben {a2 * t * h2} dm³. Zusammen {V} dm³.', 'Zerlegen in zwei Quader.', 'dm³',
                 grafik=treppe([(a, h1), (a2, h2)], t))
    if st == 2:
        art = wahl(R, 'zu2', ['hohl', 'treppe3', 'aufgesetzt', 'ergaenzen'])
        if art == 'hohl':
            a, b, c, w = R.choice([(10, 8, 6, 1), (12, 10, 8, 1), (20, 15, 10, 2), (14, 10, 8, 2)])
            V = a * b * c - (a - 2 * w) * (b - 2 * w) * (c - w)
            return Z(f'Eine Holzkiste ohne Deckel ist außen {a} cm · {b} cm · {c} cm groß. Wände und Boden sind {w} cm dick. Wie viel cm³ Holz hat sie?', V,
                     f'{a} * {b} * {c} - ({a} - 2 * {w}) * ({b} - 2 * {w}) * ({c} - {w})',
                     f'Außen: {z(a * b * c)} cm³. Innenraum: {a - 2 * w} · {b - 2 * w} · {c - w} = {z((a - 2 * w) * (b - 2 * w) * (c - w))} cm³. Holz: {z(V)} cm³.',
                     'Außen minus Innenraum. Oben ist kein Deckel.', 'cm³')
        if art == 'treppe3':
            s, t = R.choice([(2, 5), (3, 4), (2, 8), (3, 6)])
            n = 3
            V = sum((s * k) * s * t for k in range(1, n + 1))
            return Z(f'Eine Treppe hat 3 Stufen. Jede Stufe ist {s} dm hoch und {s} dm tief, die Treppe ist {t} dm breit. Wie groß ist ihr Volumen (massiv)?', V,
                     ' + '.join(f'{s * k} * {s} * {t}' for k in range(1, n + 1)),
                     f'Zerlegen in waagrechte Schichten: unten {3 * s} dm, dann {2 * s} dm, oben {s} dm lang, je {s} dm hoch und {t} dm breit: '
                     f'{" + ".join(str(s * k * s * t) for k in (3, 2, 1))} = {V} dm³.', 'Zerlege in drei Schichten.', 'dm³',
                     grafik=treppe([(3 * s, s), (2 * s, s), (s, s)], t, labels=False) | {})
        if art == 'aufgesetzt':
            a, b, c, k = R.randint(6, 10), R.randint(4, 8), R.randint(2, 5), R.randint(2, 4)
            if k > min(a, b): return gen_zusammengesetzt(R, st)
            return Z(f'Auf einen Quader ({a} cm · {b} cm · {c} cm) wird ein Würfel mit {k} cm Kante geklebt. Wie groß ist das Volumen zusammen?', a * b * c + k ** 3,
                     f'{a} * {b} * {c} + {k} * {k} * {k}', f'Quader: {a * b * c} cm³, Würfel: {k ** 3} cm³. Zusammen {a * b * c + k ** 3} cm³.', 'Beide Volumen addieren.', 'cm³')
        a, h, a2, h2, t = R.randint(6, 10), R.randint(2, 4), R.randint(2, 4), R.randint(2, 4), R.randint(3, 6)
        if a2 >= a: return gen_zusammengesetzt(R, st)
        V = a * (h + h2) * t - (a - a2) * h2 * t
        return Z(f'Eine Stufe ist {a} dm lang, {t} dm breit und insgesamt {h + h2} dm hoch. Oben rechts fehlt ein Quader ({a - a2} dm lang, {h2} dm hoch, so breit wie die Stufe). '
                 f'Berechne das Volumen durch Ergänzen.', V, f'{a} * {h + h2} * {t} - {a - a2} * {h2} * {t}',
                 f'Ganzer Quader: {a} · {t} · {h + h2} = {a * t * (h + h2)} dm³. Fehlend: {a - a2} · {t} · {h2} = {(a - a2) * t * h2} dm³. Volumen: {V} dm³.',
                 'Ganzer Quader minus fehlendes Stück.', 'dm³', grafik=treppe([(a, h), (a2, h2)], t))
    art = wahl(R, 'zu3', ['becken', 'rahmen', 'kopf', 'u_form', 'mauer'])
    if art == 'becken':
        l, b, t1, l2, t2 = R.choice([(25, 10, 2, 8, Fr(1)), (20, 8, 2, 6, Fr(1)), (25, 12, 2, 10, Fr(1, 2)), (16, 8, 2, 6, Fr(1))])
        V = l * b * t1 - l2 * b * (t1 - t2)
        return Z(f'Ein Schwimmbecken ist {l} m lang und {b} m breit. Es ist {t1} m tief, nur ein {l2} m langer Nichtschwimmerteil (ganze Breite) ist {z(t2)} m tief. '
                 f'Wie viele m³ Wasser passen hinein?', V, f'{l} * {b} * {t1} - {l2} * {b} * ({t1} - {d(t2)})',
                 f'Ganz tief wären {l} · {b} · {t1} = {z(l * b * t1)} m³. Im Nichtschwimmerteil fehlen {l2} · {b} · {z(t1 - t2)} = {z(l2 * b * (t1 - t2))} m³. Wasser: {z(V)} m³.',
                 'Ergänze zum tiefen Becken und ziehe ab.', 'm³')
    if art == 'rahmen':
        a, b, h, w = R.choice([(10, 8, 3, 1), (12, 10, 5, 2), (20, 12, 4, 2)])
        V = a * b * h - (a - 2 * w) * (b - 2 * w) * h
        return Z(f'Ein Rahmen aus Holz ist außen {a} cm · {b} cm groß, {h} cm hoch, und die Wände sind {w} cm dick (kein Boden). Wie viel cm³ Holz hat er?', V,
                 f'{a} * {b} * {h} - ({a} - 2 * {w}) * ({b} - 2 * {w}) * {h}', f'Außen: {a * b * h} cm³. Loch: {a - 2 * w} · {b - 2 * w} · {h} = {(a - 2 * w) * (b - 2 * w) * h} cm³. Holz: {V} cm³.',
                 'Außen minus Loch.', 'cm³')
    if art == 'kopf':
        a = R.choice([5, 10, 20, 25])
        return Z(f'Rechne im Kopf: Ein Quader ist {a} cm · 4 cm · 25 cm groß. Wie groß ist sein Volumen?', a * 100, f'{a} * 4 * 25',
                 f'Geschickt rechnen: 4 · 25 = 100. Dann {a} · 100 = {z(a * 100)} cm³.', 'Welche zwei Zahlen ergeben zusammen 100?', 'cm³')
    if art == 'u_form':
        a, b, c, w = R.choice([(8, 5, 4, 2), (10, 6, 5, 2), (12, 4, 6, 3)])
        V = a * b * c - (a - 2 * w) * b * (c - w)
        return Z(f'Ein U-förmiger Betonblock ist {a} dm breit, {b} dm tief und {c} dm hoch. Von oben ist eine Rinne ausgespart: {a - 2 * w} dm breit, {c - w} dm tief, über die ganze Tiefe. '
                 f'Wie viel Beton ist das?', V, f'{a} * {b} * {c} - ({a} - 2 * {w}) * {b} * ({c} - {w})',
                 f'Ganzer Block: {a * b * c} dm³. Rinne: {a - 2 * w} · {b} · {c - w} = {(a - 2 * w) * b * (c - w)} dm³. Beton: {V} dm³.', 'Block minus Rinne.', 'dm³')
    l, h, d_ = R.choice([(Fr(12), Fr(1), Fr(3, 10)), (Fr(8), Fr(15, 10), Fr(24, 100)), (Fr(20), Fr(1, 2), Fr(2, 10))])
    tor = Fr(1) * h * d_
    V = l * h * d_ - tor
    return Z(f'Eine Mauer ist {z(l)} m lang, {z(h)} m hoch und {gr(d_ * 100, "cm")} dick. Ein 1 m breiter Durchgang geht durch die ganze Höhe. Wie viele m³ Mauerwerk sind es?', V,
             f'{d(l)} * {d(h)} * {d(d_)} - 1 * {d(h)} * {d(d_)}', f'Ganze Mauer: {z(l)} · {z(h)} · {z(d_)} = {z(l * h * d_)} m³. Durchgang: 1 · {z(h)} · {z(d_)} = {z(tor)} m³. Mauerwerk: {z(V)} m³.',
             'Dicke in m umrechnen. Dann den Durchgang abziehen.', 'm³')


def gen_verstehen(R, st):
    if st == 1:
        art = wahl(R, 've1', ['einheit', 'badewanne'])
        if art == 'einheit':
            ding, e, fal = R.choice([('eines Klassenzimmers', 'm³', ['cm³', 'mm³', 'ml']), ('eines Zuckerwürfels', 'cm³', ['m³', 'l', 'dm³']), ('einer Wasserflasche', 'l', ['m³', 'mm³', 'km'])])
            return A(R, f'In welcher Einheit gibt man das Volumen {ding} sinnvoll an?', e, fal, f'Für das Volumen {ding} passt {e}: Die Zahl ist dann weder riesig noch winzig.', 'Welche Einheit gibt eine handliche Zahl?')
        ding, rich, fal = R.choice([('eine Badewanne', '150 l', ['15 l', '1 500 l', '15 ml']), ('einen Esslöffel', '15 ml', ['15 l', '150 ml', '1,5 l']),
                                    ('einen Putzeimer', '10 l', ['1 l', '100 l', '10 ml'])])
        return A(R, f'Wie viel Wasser passt ungefähr in {ding}?', rich, fal, f'Ein sinnvoller Näherungswert für {ding} ist {rich}.', 'Vergleiche mit einer 1-l-Flasche.')
    if st == 2:
        art = wahl(R, 've2', ['verdopplung', 'naeherung', 'fehler', 'halbieren'])
        if art == 'verdopplung':
            V = R.choice([12, 15, 20, 24, 30, 40])
            k, txt = R.choice([(2, 'eine Kante wird verdoppelt'), (4, 'zwei Kanten werden verdoppelt'), (8, 'alle drei Kanten werden verdoppelt'), (3, 'eine Kante wird verdreifacht')])
            return Z(f'Ein Quader hat {V} cm³. {txt[0].upper() + txt[1:]}. Wie groß ist das neue Volumen?', V * k, f'{V} * {k}',
                     f'Wird eine Kante doppelt (dreimal) so lang, wird das Volumen doppelt (dreimal) so groß. Hier wird es {k}-mal so groß: {V} · {k} = {V * k} cm³.', 'Wie oft passt der alte Quader in den neuen?', 'cm³')
        if art == 'naeherung':
            a, b, c = R.choice([(7, 6, 24), (9, 6, 19), (6, 6, 28), (7, 7, 20)])
            V = a * b * c
            rund = round(V / 100) * 100
            return A(R, f'Eine Getränkepackung ist etwa {a} cm · {b} cm · {c} cm groß. Wie viel passt ungefähr hinein?', f'etwa {z(rund)} ml',
                     [f'etwa {z(rund // 10)} ml', f'etwa {z(rund * 10)} ml', f'etwa {z(rund)} l'], f'{a} · {b} · {c} = {z(V)} cm³ ≈ {z(rund)} ml.', 'Volumen in cm³ ist gleich ml.')
        if art == 'fehler':
            a, b, c = R.randint(10, 30), R.randint(10, 20), R.randint(10, 30)
            return A(R, f'Lena rechnet: {a} cm · {b} cm · {c} cm = {z(a * b * c)} cm³ = {z(Fr(a * b * c, 100))} l. Was stimmt?', f'Falsch: {z(a * b * c)} cm³ sind {z(Fr(a * b * c, 1000))} l.',
                     ['Richtig.', f'Falsch: Es sind {z(a * b * c)} l.', f'Falsch: Es sind {z(Fr(a * b * c, 10))} l.'],
                     f'1 l = 1 000 cm³. Also {z(a * b * c)} : 1 000 = {z(Fr(a * b * c, 1000))} l.', 'Wie viele cm³ hat ein Liter?')
        V = R.choice([48, 64, 80, 96, 120])
        return Z(f'Ein Quader hat {V} cm³. Er wird genau in der Mitte durchgeschnitten, parallel zu einer Seitenfläche. Wie groß ist eine Hälfte?', Fr(V, 2), f'{V} / 2',
                 f'Beide Hälften sind gleich groß: {V} : 2 = {z(Fr(V, 2))} cm³.', 'Welche Kante wird halbiert?', 'cm³')
    art = wahl(R, 've3', ['aussagen', 'oberflaeche', 'schaetzen', 'raum', 'gewicht'])
    if art == 'aussagen':
        return A(R, 'Welche Aussage ist richtig?', 'Ein Würfel mit 1 dm Kante fasst so viel wie 1 000 Würfel mit 1 cm Kante.',
                 ['Ein Würfel mit 1 dm Kante fasst so viel wie 100 Würfel mit 1 cm Kante.', '1 m³ sind 100 Liter.', 'Ein Liter ist so groß wie ein Würfel mit 1 cm Kante.'],
                 '1 dm = 10 cm, also 10 · 10 · 10 = 1 000 cm³. 1 m³ = 1 000 l, und 1 l = 1 dm³.', 'Rechne jede Aussage nach.')
    if art == 'oberflaeche':
        return A(R, 'Zwei Quader haben beide 24 cm³: 1 cm · 1 cm · 24 cm und 2 cm · 3 cm · 4 cm. Was stimmt?', 'Gleiches Volumen, aber verschiedene Oberflächen (98 cm² und 52 cm²).',
                 ['Sie haben auch die gleiche Oberfläche.', 'Der lange Quader hat das größere Volumen.', 'Der kurze Quader hat die größere Oberfläche.'],
                 'Oberflächen: 2 · (1 + 24 + 24) = 98 cm² und 2 · (6 + 8 + 12) = 52 cm². Das Volumen ist bei beiden 24 cm³.', 'Rechne beide Oberflächen aus.')
    if art == 'schaetzen':
        return A(R, 'Ein Klassenzimmer ist etwa 8 m lang, 7 m breit und 3 m hoch. Wie viele Liter Luft sind darin ungefähr?', 'etwa 170 000 l',
                 ['etwa 170 l', 'etwa 1 700 l', 'etwa 17 000 000 l'], '8 · 7 · 3 = 168 m³ ≈ 170 m³. 1 m³ = 1 000 l, also etwa 170 000 l.', 'Erst m³, dann Liter.')
    if art == 'raum':
        a, b = R.choice([(4, 3), (5, 4), (6, 4)])
        return Z(f'Ein Kinderzimmer ist {a} m lang, {b} m breit und 2,5 m hoch. Pro Person sollte man mindestens 10 m³ Luft rechnen. Für wie viele Personen reicht der Raum höchstens?',
                 Fr(a * b * 5, 2) // 10, f'{a} * {b} * 2.5 // 10', f'V = {a} · {b} · 2,5 = {z(Fr(a * b * 5, 2))} m³. {z(Fr(a * b * 5, 2))} : 10 = {z(Fr(a * b * 5, 20))} – also höchstens {Fr(a * b * 5, 2) // 10} Personen.',
                 'Volumen ausrechnen, dann durch 10; nur ganze Personen.', None)
    a = R.choice([2, 3, 4, 5])
    return Z(f'1 l Wasser wiegt 1 kg. Wie viel kg wiegt das Wasser in einem vollen Würfel mit {a} dm Kante?', a ** 3, f'{a} * {a} * {a}',
             f'V = {a} · {a} · {a} = {a ** 3} dm³ = {a ** 3} l. Das wiegt {a ** 3} kg.', 'Volumen in Liter.', 'kg')


GEN = {'einheitswuerfel': gen_einheitswuerfel, 'quader': gen_quader, 'einheiten': gen_einheiten, 'liter': gen_liter, 'rueckwaerts': gen_rueckwaerts,
       'zusammengesetzt': gen_zusammengesetzt, 'verstehen': gen_verstehen}


def fest(R):
    F = {}
    F['einheitswuerfel'] = [
        Z('Ein Treppenkörper ist aus Würfeln gebaut: 3 Würfel tief, unten 4 Würfel breit, in der Mitte 3, oben 2. Wie viele Würfel fehlen, damit ein Quader (4 · 3 · 3 Würfel) entsteht?', 9,
          '4 * 3 * 3 - (4 * 3 + 3 * 3 + 2 * 3)', 'Vorhanden: 4 · 3 + 3 · 3 + 2 · 3 = 12 + 9 + 6 = 27 Würfel. Quader: 4 · 3 · 3 = 36. Es fehlen 36 − 27 = 9 Würfel.',
          'Zähle Schicht für Schicht.', None, art=P, grafik=treppe([(4, 1), (3, 1), (2, 1)], 3, 'cm', labels=False)),
        Z('Ein Karton ist innen 30 cm lang, 20 cm breit und 20 cm hoch. Wie viele Würfel mit 5 cm Kante passen hinein?', 96, '(30 / 5) * (20 / 5) * (20 / 5)',
          'Je Richtung: 30 : 5 = 6, 20 : 5 = 4, 20 : 5 = 4. Zusammen 6 · 4 · 4 = 96 Würfel.', 'Wie viele 5-cm-Würfel passen in jede Richtung?', None, art=P),
        Z('Ein Würfel aus 4 · 4 · 4 kleinen Würfeln wird außen rot angemalt. Wie viele kleine Würfel haben genau eine rote Fläche?', 24, '6 * (4 - 2) * (4 - 2)',
          'Genau eine Fläche rot haben die Würfel in der Mitte jeder Außenfläche: je 2 · 2 = 4. Der Würfel hat 6 Flächen: 6 · 4 = 24.', 'Welche Würfel liegen auf einer Fläche, aber nicht am Rand?', None, art=K)]
    F['quader'] = [
        A(R, 'Ein Umzugskarton ist 60 cm lang, 40 cm breit und 40 cm hoch. Ein kleinerer Karton soll halb so viel fassen. Welche Maße passen?', '60 cm · 40 cm · 20 cm',
          ['30 cm · 20 cm · 20 cm', '50 cm · 30 cm · 30 cm', '60 cm · 40 cm · 30 cm'],
          'Groß: 60 · 40 · 40 = 96 000 cm³. Halb: 48 000 cm³ = 60 · 40 · 20. Halbiert man alle Kanten (30 · 20 · 20 = 12 000 cm³), ist es nur ein Achtel; '
          '50 · 30 · 30 = 45 000 cm³ und 60 · 40 · 30 = 72 000 cm³ sind nicht die Hälfte.',
          'Halbiere genau eine Kante.', art=P),
        Z('Ein Würfel mit 4 cm Kante wird entlang einer Diagonale von oben nach unten in zwei gleiche Teile geschnitten. Wie groß ist das Volumen eines Teils?', 32, '4 * 4 * 4 / 2',
          'Würfel: 4 · 4 · 4 = 64 cm³. Die beiden Teile sind gleich groß: 64 : 2 = 32 cm³.', 'Wie groß ist der ganze Würfel?', 'cm³', art=P),
        Z('Wie viele verschiedene Quader mit ganzzahligen Kantenlängen (in cm) haben genau 24 cm³? Quader, die nur gedreht sind, zählen als gleich.', 6, '6',
          'Kanten a ≤ b ≤ c mit a · b · c = 24: 1·1·24, 1·2·12, 1·3·8, 1·4·6, 2·2·6, 2·3·4. Das sind 6 Quader.', 'Beginne mit der kleinsten Kante 1, dann 2.', None, art=K)]
    F['einheiten'] = [
        A(R, 'Welche Angabe beschreibt das gleiche Volumen wie 0,2 dm³?', '200 cm³', ['20 cm³', '2 000 cm³', '0,2 m³'],
          '0,2 dm³ = 0,2 · 1 000 cm³ = 200 cm³. 0,2 m³ wären 200 dm³.', 'Rechne in cm³ um.', art=P),
        Z('Berechne 2 m³ + 300 dm³ + 4 000 cm³ in dm³.', 2304, '2 * 1000 + 300 + 4000 / 1000', '2 m³ = 2 000 dm³, 4 000 cm³ = 4 dm³. Summe: 2 000 + 300 + 4 = 2 304 dm³.',
          'Alles in dm³ umrechnen.', 'dm³', art=P),
        Z('Ein Würfel mit 1 m Kante wird in Würfel mit 1 cm Kante zerschnitten. Man legt alle in eine Reihe. Wie viele km ist die Reihe lang?', 10, '100 * 100 * 100 / 100000',
          '1 m³ = 1 000 000 cm³, also 1 000 000 Würfelchen zu je 1 cm. Reihe: 1 000 000 cm = 10 000 m = 10 km.', 'Wie viele cm³ hat 1 m³?', 'km', art=K)]
    F['liter'] = [
        Z('Auf ein Flachdach mit 40 m² fallen in einer Nacht 15 mm Regen. Wie viele Liter Wasser sind das?', 600, '40 * 15', 'Auf 1 m²: 10 dm · 10 dm · 0,15 dm = 15 dm³ = 15 l. Auf 40 m²: 40 · 15 = 600 l.',
          'Rechne den Regen auf 1 m² als flachen Quader in dm.', 'l', art=P),
        Z('Ein Messbecher fasst 0,5 l. Wie oft muss man ihn ausleeren, um ein Aquarium (40 cm lang, 25 cm breit, 30 cm hoch) ganz zu füllen?', 60, '40 * 25 * 30 / 1000 / 0.5',
          'Aquarium: 4 dm · 2,5 dm · 3 dm = 30 dm³ = 30 l. 30 l : 0,5 l = 60-mal.', 'Rechne das Aquarium in Liter um.', None, art=P),
        Z('Ein Wasserhahn tropft jede Sekunde. Ein Tropfen hat 0,05 ml. Wie viele Liter gehen an einem Tag verloren?', Fr(432, 100), '0.05 * 60 * 60 * 24 / 1000',
          'Ein Tag hat 24 · 60 · 60 = 86 400 Sekunden. 86 400 · 0,05 ml = 4 320 ml = 4,32 l.', 'Wie viele Sekunden hat ein Tag?', 'l', art=K)]
    F['rueckwaerts'] = [
        Z('Ein aufblasbares Luftkissen hat laut Hersteller 360 l Volumen. Ein Quader mit gleichem Volumen ist 30 dm lang und 8 dm breit. Wie hoch ist dieser Quader?', Fr(3, 2), '360 / (30 * 8)',
          '360 l = 360 dm³. Grundfläche: 30 · 8 = 240 dm². Höhe: 360 : 240 = 1,5 dm.', 'Liter sind dm³.', 'dm', art=P),
        Z('Ein Umzugskarton fasst 72 l. Er ist 60 cm lang und 40 cm breit. Wie hoch ist er?', 30, '72 * 1000 / (60 * 40)', '72 l = 72 000 cm³. Grundfläche 2 400 cm². 72 000 : 2 400 = 30 cm.',
          'Liter in cm³.', 'cm', art=P),
        Z('In einem Aquarium (50 cm · 30 cm Grundfläche) steht das Wasser 20 cm hoch. Ein Stein wird hineingelegt, danach steht es 21,5 cm hoch. Wie viel cm³ hat der Stein?', 2250,
          '50 * 30 * (21.5 - 20)', 'Das Wasser steigt um 1,5 cm. Der Stein verdrängt einen flachen Quader: 50 · 30 · 1,5 = 2 250 cm³.', 'Um wie viel steigt das Wasser?', 'cm³', art=K)]
    F['zusammengesetzt'] = [
        Z('Aus einem Quader (12 cm · 9 cm · 8 cm) wird an einer Ecke ein Würfel mit 5 cm Kante herausgeschnitten. Wie groß ist das Volumen des Restkörpers?', 739, '12 * 9 * 8 - 5 * 5 * 5',
          'Quader: 864 cm³. Würfel: 125 cm³. Restkörper: 864 − 125 = 739 cm³.', 'Ganzer Quader minus Würfel.', 'cm³', art=P),
        Z('Ein Bauteil aus Beton hat die Form eines L: 6 dm lang, 4 dm breit, an der linken Seite 5 dm hoch, sonst nur 2 dm hoch. Der hohe Teil ist 2 dm lang. Alle Ecken sind rechte Winkel. Volumen?',
          72, '6 * 4 * 2 + 2 * 4 * (5 - 2)', 'Unten: 6 · 4 · 2 = 48 dm³. Hoher Teil darüber: 2 · 4 · 3 = 24 dm³. Zusammen 72 dm³.', 'Zerlege in einen flachen und einen hohen Quader.', 'dm³',
          art=P, grafik=treppe([(6, 2), (2, 3)], 4)),
        Z('Ein Würfel aus 3 · 3 · 3 Holzwürfeln wird durchbohrt: von vorn, von oben und von der Seite je genau durch die Mitte (durch eine ganze Reihe). Wie viele Holzwürfel bleiben?', 20,
          '27 - (3 + 3 + 3 - 2)', 'Jede Bohrung nimmt 3 Würfel. Der mittelste Würfel wird dreimal gezählt: 3 + 3 + 3 − 2 = 7 entfernt. Es bleiben 27 − 7 = 20.',
          'Welcher Würfel liegt in allen drei Bohrungen?', None, art=K)]
    F['verstehen'] = [
        A(R, 'Ein Bauteil wird im Maßstab 1 : 10 als Modell gebaut. Wie groß ist das Volumen des Originals im Vergleich zum Modell?', '1 000-mal so groß',
          ['10-mal so groß', '100-mal so groß', '30-mal so groß'], 'Jede der drei Kanten ist 10-mal so lang: 10 · 10 · 10 = 1 000.', 'Wie oft wird jede Kante länger?', art=P),
        A(R, 'Stimmt die Aussage? „Haben zwei Quader das gleiche Volumen, so haben sie auch die gleiche Oberfläche.“', 'Nein: 1 cm · 1 cm · 8 cm und 2 cm · 2 cm · 2 cm haben 8 cm³, aber 34 cm² und 24 cm².',
          ['Ja, Volumen und Oberfläche hängen fest zusammen.', 'Ja, aber nur bei Würfeln.', 'Nein, gleich große Quader gibt es nicht.'],
          'Ein Gegenbeispiel genügt: 2 · (1 + 8 + 8) = 34 cm² und 6 · 4 = 24 cm² bei gleichem Volumen 8 cm³.', 'Suche ein Gegenbeispiel.', art=P),
        Z('Ein Würfel hat 27 cm³. Ein zweiter Würfel hat eine dreimal so lange Kante. Wie viel cm³ hat er?', 729, '27 * 3 * 3 * 3',
          'Erster Würfel: Kante 3 cm. Zweiter: 9 cm, Volumen 9 · 9 · 9 = 729 cm³ – das 27-fache.', 'Wie lang ist die Kante des ersten Würfels?', 'cm³', art=K)]
    return F


def datei():
    auf, anz = aufgaben(ETAPPEN, GEN, fest, SEED)
    lz = [e['lernziel'] for e in ETAPPEN]
    return {
        **META, 'autor': 'Claude (Achtzehnte Runde, Teil A; Generator messen.volumen.py)',
        'inhalt': {
            'ziel': 'Volumen mit Einheitswürfeln verstehen, mit der Quaderformel berechnen, Volumeneinheiten mit Liter und Milliliter umrechnen, fehlende Kanten und Füllhöhen '
                    'rückwärts bestimmen, zusammengesetzte Körper zerlegen und ergänzen und Volumen im Alltag abschätzen.',
            'merke': ['Volumen: Würfel je Schicht mal Zahl der Schichten.', 'Quader: V = a · b · c, Würfel: V = a · a · a.', 'Volumeneinheiten: Umrechnungszahl 1 000.',
                      '1 l = 1 dm³, 1 ml = 1 cm³, 1 m³ = 1 000 l.', 'Rückwärts: Höhe = Volumen : Grundfläche.', 'Doppelte Kanten: 8-faches Volumen.'],
            'abschnitte': [{'titel': 'Volumen und Quader', 'lernziele': ['einheitswuerfel', 'quader']},
                           {'titel': 'Einheiten', 'lernziele': ['einheiten', 'liter']},
                           {'titel': 'Flexibel anwenden', 'lernziele': ['rueckwaerts', 'zusammengesetzt', 'verstehen']}],
            'etappen': ETAPPEN,
            'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in ETAPPEN],
            'bewertung': {'lernziele_pflicht': lz, 'lernziele_vertiefung': [], 'testaufgaben_je_lernziel': 1, 'hilfen_im_test': False},
            'quellen': {'erklaerungen': 'Eigene Fassung (Claude).',
                        'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern, Gymnasium M6 2.2 „Volumen“ (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/6/mathematik).',
                        'pruefungsvorbilder': 'Typ und Niveau nach: Bayerischer Mathematik-Test 8 (ISB) 2005 A5 (Umzugskartons), 2007 A3 (Einheiten umwandeln), 2008 (Restkörper), '
                                              '2009 A1 (geteilter Würfel), 2013 B3 (Niederschlag als Quader), 2018 A4 (Aussagen beurteilen), 2022 A6 (gleiches Volumen erkennen), '
                                              '2023 A (Volumen in Litern, Quaderhöhe), 2025 A (Bauelement, Maßstab und Volumen); Jahrgangsstufentest Realschule 6 (ISB) 2010 Nr. 18 '
                                              '(Volumen eines Messbechers); VERA-8 2012 Modul C („Würfelkörper“). Eigene Zahlen und Einkleidung.'},
        },
        'aufgaben': auf,
        'offen': ['Schrägbilder von Quadern und Stufen sind als Figur aus Strecken gezeichnet (Tiefe halb so lang unter 45°, verdeckte Kanten gestrichelt), Maßstab per Skript geprüft.',
                  'Messen mit Hohlmaßen (Umfüllen, Messbecher) kann das Kind in der App nicht selbst; es kommt als Sachaufgabe vor.',
                  'Keine Gleichungen mit x (erst Klasse 7): fehlende Kanten und Füllhöhen werden rückwärts gerechnet (Volumen : Grundfläche).'],
    }, anz


if __name__ == '__main__':
    d_, anz = datei()
    schreiben(ZIEL, d_, anz)
