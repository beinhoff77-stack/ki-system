#!/usr/bin/env python3
"""Thema geometrie.winkel – Winkel (Klasse 5): Winkel ergänzen, Winkel an Geraden und um einen Punkt, Uhr, Drehungen, Winkel in Figuren.
Winkelsätze (Stufen-/Wechselwinkel, Innenwinkelsummen) sind laut LehrplanPLUS Stoff der Jahrgangsstufe 7 und fehlen hier bewusst."""
import math
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5_rest import *  # noqa: E402,F403

R = random.Random(43)
E = eintrag_laden('geometrie.winkel')


def strahl(grad, l=5):
    w = math.radians(grad)
    return [round(l * math.cos(w), 3), round(l * math.sin(w), 3)]


def uhrbild(h, m=0, text=None):
    """Zifferblatt als Figur: 12 Striche, Zahlen 12/3/6/9, Stundenzeiger kurz, Minutenzeiger lang (Prüfung: Uhr ist mit „figur“ zeichenbar)."""
    pk = {'M': [0, 0]}
    lin = []
    for k in range(12):
        w = math.radians(90 - 30 * k)
        pk[f'_t{k}a'] = [round(4.4 * math.cos(w), 3), round(4.4 * math.sin(w), 3)]
        pk[f'_t{k}b'] = [round(5 * math.cos(w), 3), round(5 * math.sin(w), 3)]
        lin.append([f'_t{k}a', f'_t{k}b'])
    for zahl, k in (('12', 0), ('3', 3), ('6', 6), ('9', 9)):
        pk[zahl] = pk[f'_t{k}b']
    ws = math.radians(90 - (30 * (h % 12) + m / 2)); wm = math.radians(90 - 6 * m)
    pk['_h'] = [round(2.6 * math.cos(ws), 3), round(2.6 * math.sin(ws), 3)]
    pk['_m'] = [round(4 * math.cos(wm), 3), round(4 * math.sin(wm), 3)]
    lin += [['M', '_h'], ['M', '_m']]
    g = {'typ': 'figur', 'punkte': pk, 'kreise': [{'m': 'M', 'r': 5}], 'linien': lin}
    if text: g['winkel'] = [['M', '_m', '_h', text]]
    return g


def windrose():
    pk = {'_M': [0, 0]}
    kurz = ['N', 'NO', 'O', 'SO', 'S', 'SW', 'W', 'NW']
    for k, n in enumerate(kurz):
        w = math.radians(90 - 45 * k)
        pk[n] = [round(4 * math.cos(w), 3), round(4 * math.sin(w), 3)]
    return {'typ': 'figur', 'punkte': pk, 'linien': [['_M', n, '', '' if k % 2 == 0 else 'gestrichelt'] for k, n in enumerate(kurz)]}


def facher(richtungen, beschr, gerade=False):
    """Strahlen von S aus; Winkel zwischen benachbarten Strahlen beschriftet."""
    pk = {'S': [0, 0]}
    for i, g in enumerate(richtungen): pk[f'_P{i}'] = strahl(g)
    lin = [['S', f'_P{i}'] for i in range(len(richtungen))]
    win = [['S', f'_P{i}', f'_P{i + 1}', t] for i, t in enumerate(beschr) if t]
    return {'typ': 'figur', 'punkte': pk, 'linien': lin, 'winkel': win}


ETAPPEN = [
    {'lernziel': 'ergaenzen', 'titel': 'Winkel ergänzen',
     'regel': 'Liegen zwei Winkel ⟦nebeneinander⟧ (gemeinsamer Schenkel), werden ihre Größen ⟦addiert⟧. Zusammen bilden sie oft einen rechten Winkel (⟦90°⟧), einen gestreckten Winkel (⟦180°⟧) oder einen Vollwinkel (⟦360°⟧). Der fehlende Winkel ist dann der ⟦Rest⟧.',
     'schritte': ['α = 50° und β liegen nebeneinander und bilden zusammen einen gestreckten Winkel (180°).', 'β = 180° − 50° = ⟦130°⟧.'],
     'probe': '50° + 130° = 180° ✓',
     'bild': facher([0, 50, 180], ['α = 50°', 'β = ?']),
     'fehler': 'β = 90° − 50° = 40° ist falsch, wenn die beiden Winkel einen ⟦gestreckten⟧ Winkel bilden: Der hat 180°, nicht 90°. Schau genau, ob 90°, 180° oder 360° gemeint ist.'},
    {'lernziel': 'kreuzung', 'titel': 'Winkel an einer Geradenkreuzung',
     'regel': 'Schneiden sich zwei Geraden, entstehen ⟦vier Winkel⟧. Zwei benachbarte Winkel ergeben zusammen ⟦180°⟧ (gestreckter Winkel). Gegenüberliegende Winkel sind deshalb ⟦gleich groß⟧. Alle vier zusammen ergeben 360°.',
     'schritte': ['Zwei Geraden schneiden sich, α = 70°. Der Nachbarwinkel β ergänzt α zu 180°: β = 180° − 70° = 110°.', 'Der Winkel gegenüber von α ergänzt β zu 180°: γ = 180° − 110° = ⟦70°⟧, also gleich groß wie α.'],
     'bild': facher([0, 70, 180, 250, 360], ['α = 70°', 'β', 'γ', 'δ']),
     'fehler': 'β = 70° anzunehmen, nur weil β neben α liegt, ist falsch: ⟦Benachbarte⟧ Winkel ergänzen sich zu 180°. Gleich groß sind nur die ⟦gegenüberliegenden⟧ Winkel.'},
    {'lernziel': 'um_punkt', 'titel': 'Mehrere Winkel um einen Punkt',
     'regel': 'Liegen mehrere Winkel ⟦lückenlos um einen Punkt⟧, ergeben sie zusammen ⟦360°⟧. Liegen sie auf einer Seite einer Geraden, ergeben sie zusammen ⟦180°⟧. Fehlender Winkel = Gesamtwinkel ⟦minus alle bekannten⟧.',
     'schritte': ['Um einen Punkt liegen α = 100°, β = 80°, γ = 120° und δ.', 'δ = 360° − 100° − 80° − 120° = ⟦60°⟧.'],
     'probe': '100° + 80° + 120° + 60° = 360° ✓',
     'bild': facher([0, 100, 180, 300, 360], ['α = 100°', 'β = 80°', 'γ = 120°', 'δ = ?']),
     'fehler': 'Nur einen der bekannten Winkel abzuziehen ist ein Fehler: ⟦Alle⟧ bekannten Winkel müssen vom Vollwinkel abgezogen werden.'},
    {'lernziel': 'uhr', 'titel': 'Winkel an der Uhr',
     'regel': 'Der ⟦Minutenzeiger⟧ dreht sich in 60 min einmal ganz herum (360°), also ⟦6° pro Minute⟧. Zwischen zwei Stundenzahlen auf dem Zifferblatt liegen ⟦30°⟧ (360° : 12).',
     'schritte': ['Um 4:00 Uhr zeigt der große Zeiger auf 12, der kleine auf 4. Dazwischen liegen 4 Stundenabstände.', '4 · 30° = ⟦120°⟧.'],
     'fehler': 'Die Minuten wie Grad zu zählen ist falsch: In 15 min dreht sich der Minutenzeiger nicht um 15°, sondern um 15 · 6° = ⟦90°⟧.'},
    {'lernziel': 'drehungen', 'titel': 'Drehungen und Himmelsrichtungen',
     'regel': 'Eine ⟦ganze Drehung⟧ sind 360°, eine ⟦halbe⟧ 180°, eine ⟦Vierteldrehung⟧ 90°. Zwischen zwei benachbarten Himmelsrichtungen der Windrose (N, NO, O, SO, S, SW, W, NW) liegen ⟦45°⟧.',
     'schritte': ['Du schaust nach Norden und drehst dich im Uhrzeigersinn bis Südosten: N → NO → O → SO.', 'Das sind 3 Schritte zu 45°: 3 · 45° = ⟦135°⟧.'],
     'fehler': 'Von Norden nach Osten 180° anzunehmen ist falsch: Norden und Osten liegen nur eine ⟦Vierteldrehung⟧ auseinander, also 90°. 180° wäre von Norden nach Süden.'},
    {'lernziel': 'figuren', 'titel': 'Winkel in Rechteck und Quadrat',
     'regel': 'In ⟦Rechteck und Quadrat⟧ ist jeder Eckwinkel 90°. Teilt eine Diagonale einen solchen Winkel, ergeben die beiden Teile zusammen ⟦90°⟧. Im ⟦Quadrat⟧ teilt die Diagonale den Eckwinkel in zwei gleiche Teile: je ⟦45°⟧.',
     'schritte': ['Im Rechteck ABCD teilt die Diagonale [AC] den Winkel bei A. Ein Teil ist 35°.', 'Der andere Teil ist 90° − 35° = ⟦55°⟧.'],
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [7, 0], 'C': [7, 4.9], 'D': [0, 4.9]}, 'flaeche': ['A', 'B', 'C', 'D'],
              'linien': [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['A', 'C', '', 'gestrichelt']], 'winkel': [['A', 'B', 'C', '35°'], ['A', 'C', 'D', '?']]},
     'fehler': 'Den zweiten Teil auch 35° zu nennen ist nur im ⟦Quadrat⟧ richtig (dort 45°). Im Rechteck sind die beiden Teile ⟦verschieden⟧ – sie ergeben zusammen 90°.'},
    {'lernziel': 'verstehen', 'titel': 'Winkelaussagen prüfen',
     'regel': 'Prüfe Aussagen über Winkel mit den ⟦Bezugswinkeln⟧ 90°, 180° und 360° und mit einer ⟦Skizze⟧. Ein Gegenbeispiel genügt, um eine Aussage zu widerlegen.',
     'schritte': ['Aussage: „Zwei stumpfe Winkel nebeneinander ergeben immer einen überstumpfen Winkel.“ Beispiel: 100° + 100° = 200°.', 'Stumpf heißt größer als 90°, zwei davon sind also mehr als 180°. Die Aussage ist ⟦richtig⟧.'],
     'fehler': 'Eine Aussage nur an einem Beispiel zu prüfen, das zufällig passt, ist unsicher. Überlege, ob es ⟦immer⟧ gilt – oder suche gezielt ein ⟦Gegenbeispiel⟧.'},
]

PRUEFUNG = pruefung_erklaerungen(ETAPPEN, 'geometrie.winkel')   # uhr (Stundenzeiger, Bild), drehungen (Windrose als Bild)

MERKE = ['Nebeneinander liegende Winkel werden addiert.', 'Gestreckter Winkel 180°, Vollwinkel 360°, rechter Winkel 90°.',
         'Geradenkreuzung: Nachbarwinkel ergeben 180°, gegenüberliegende sind gleich groß.', 'Uhr: Minutenzeiger 6° pro Minute, zwischen zwei Stundenzahlen 30°.',
         'Windrose: zwischen benachbarten Richtungen 45°.']


# ---------- 1 Ergänzen ----------
def g_erg(st):
    if st == 1:
        ziel = R.choice([90, 180])
        a = R.randint(10, ziel - 10)
        fig = facher([0, a, ziel], [f'α = {a}°', 'β = ?'])
        return {'y': 'zahl', 'f': {'text': f'α = {a}° und β liegen nebeneinander und bilden zusammen einen {"rechten" if ziel == 90 else "gestreckten"} Winkel. Wie groß ist β?', 'grafik': fig},
                'o': {'wert': ziel - a, 'einheit': '°'}, 'c': f'{ziel} - {a}', 'w': f'β = {ziel}° − {a}° = {ziel - a}°.', 'h': f'Ein {"rechter" if ziel == 90 else "gestreckter"} Winkel hat {ziel}°.'}
    if st == 2:
        a = R.randint(20, 340)
        if R.random() < .5 and a < 180:
            b = R.randint(10, 179 - a) if a < 170 else 5
            return {'y': 'zahl', 'f': {'text': f'Zwei Winkel α = {a}° und β = {b}° liegen nebeneinander. Wie groß ist der Winkel, der zusammen mit beiden einen gestreckten Winkel ergibt?',
                                       'grafik': facher([0, a, a + b, 180], [f'{a}°', f'{b}°', '?'])},
                    'o': {'wert': 180 - a - b, 'einheit': '°'}, 'c': f'180 - {a} - {b}', 'w': f'180° − {a}° − {b}° = {180 - a - b}°.', 'h': 'Ziehe beide bekannten Winkel von 180° ab.'}
        return {'y': 'zahl', 'f': {'text': f'Ein Winkel α = {a}° wird durch einen zweiten Winkel β zum Vollwinkel ergänzt. Wie groß ist β?'}, 'o': {'wert': 360 - a, 'einheit': '°'}, 'c': f'360 - {a}',
                'w': f'β = 360° − {a}° = {360 - a}°.', 'h': 'Ein Vollwinkel hat 360°.'}
    art = R.randrange(3)
    if art == 0:
        a = R.randint(5, 85)
        return {'y': 'zahl', 'f': {'text': f'Ein Winkel ist um {a}° größer als ein rechter Winkel. Um wie viel Grad muss man ihn noch vergrößern, damit er gestreckt ist?'},
                'o': {'wert': 90 - a, 'einheit': '°'}, 'c': f'180 - (90 + {a})', 'w': f'Der Winkel ist 90° + {a}° = {90 + a}°. Bis 180° fehlen {90 - a}°.', 'h': 'Rechne zuerst die Größe des Winkels aus.'}
    if art == 1 and R.random() < .5:      # Fehler finden (Prüfung)
        if R.random() < .5:
            a = R.randint(10, 80)
            text = f'Jemand rechnet: α = {a}° und β bilden einen rechten Winkel, also β = 180° − {a}° = {180 - a}°. Was ist falsch?'
            r, f = f'Ein rechter Winkel hat 90°: β = 90° − {a}° = {90 - a}°.', ['Nichts, das stimmt.', f'Man muss 360° − {a}° = {360 - a}° rechnen.']
        else:
            a = R.randint(190, 350)
            text = f'Jemand rechnet: α = {a}° wird zum Vollwinkel ergänzt, also β = {a}° − 180° = {a - 180}°. Was ist falsch?'
            r, f = f'Ein Vollwinkel hat 360°: β = 360° − {a}° = {360 - a}°.', ['Nichts, das stimmt.', f'Man muss 180° − {a}° rechnen.']
        return {**wahl_rund(R, r, f, 3), 'f': {'text': text}, 'w': r, 'h': 'Wie groß ist der Winkel, der ergänzt werden soll: 90°, 180° oder 360°?'}
    if art == 1:
        a = 2 * R.randint(5, 40)          # gerader Unterschied: ganze Gradzahlen (Prüfung)
        return {'y': 'zahl', 'f': {'text': f'α und β liegen nebeneinander und ergeben zusammen 180°. β ist {a}° größer als α. Wie groß ist α?'},
                'o': {'wert': wert(Fr(180 - a, 2)), 'einheit': '°'}, 'c': f'(180 - {a}) / 2', 'w': f'α + (α + {a}°) = 180°, also 2 · α = {180 - a}° und α = {zt(Fr(180 - a, 2))}°. Probe: {zt(Fr(180 - a, 2))}° + {zt(Fr(180 + a, 2))}° = 180°.',
                'h': 'Nimm den Unterschied weg, dann bleiben zwei gleich große Winkel.'}
    n = R.choice([2, 3, 4, 5, 6])
    ziel = R.choice([90, 180])
    return {'y': 'zahl', 'f': {'text': f'Ein {"rechter" if ziel == 90 else "gestreckter"} Winkel wird in {n} gleich große Winkel geteilt. Wie groß ist jeder?'},
            'o': {'wert': wert(Fr(ziel, n)), 'einheit': '°'}, 'c': f'{ziel} / {n}', 'w': f'Ein {"rechter" if ziel == 90 else "gestreckter"} Winkel hat {ziel}°: {ziel}° : {n} = {zt(Fr(ziel, n))}°.', 'h': 'Teile die Gesamtgröße durch die Anzahl.'}


# ---------- 2 Kreuzung ----------
def g_kreuz(st):
    a = R.randint(20, 160)
    if a == 90: a = 75
    fig = facher([0, a, 180, 180 + a, 360], ['α = ' + str(a) + '°', 'β', 'γ', 'δ'])
    if st == 1:
        frage = R.choice(['β', 'γ'])
        r = 180 - a if frage == 'β' else a
        return {'y': 'zahl', 'f': {'text': f'Zwei Geraden schneiden sich. α = {a}°. Wie groß ist {frage}?', 'grafik': fig}, 'o': {'wert': r, 'einheit': '°'},
                'c': f'180 - {a}' if frage == 'β' else f'180 - (180 - {a})',
                'w': f'β ist Nachbarwinkel von α: 180° − {a}° = {180 - a}°.' + (f' γ liegt α gegenüber: γ = 180° − {180 - a}° = {a}°.' if frage == 'γ' else ''),
                'h': 'Nachbarwinkel ergänzen sich zu 180°.'}
    if st == 2:
        b = 180 - a
        frage = R.choice(['α', 'δ'])
        fig2 = facher([0, a, 180, 180 + a, 360], ['α', f'β = {b}°', 'γ', 'δ'])
        r = a if frage == 'α' else b
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Zwei Geraden schneiden sich. β = {b}°. Wie groß ist {frage}?', 'grafik': fig2}, 'o': {'wert': r, 'einheit': '°'},
                    'c': f'180 - {b}' if frage == 'α' else f'{b}', 'w': f'α = 180° − {b}° = {a}°. δ liegt β gegenüber, also δ = {b}°.', 'h': 'Benachbart: zusammen 180°. Gegenüber: gleich groß.'}
        return {'y': 'zahl', 'f': {'text': f'Zwei Geraden schneiden sich. Zwei gegenüberliegende Winkel sind zusammen {2 * a}°. Wie groß ist einer der beiden anderen Winkel?'},
                'o': {'wert': 180 - a, 'einheit': '°'}, 'c': f'180 - {2 * a} / 2', 'w': f'Gegenüberliegende Winkel sind gleich: je {a}°. Der Nachbarwinkel: 180° − {a}° = {180 - a}°.',
                'h': 'Gegenüberliegende Winkel sind gleich groß.'}
    art = R.randrange(3)
    if art == 0:
        d = R.randint(10, 60)
        x = Fr(180 + d, 2)
        if x.denominator != 1: d += 1; x = Fr(180 + d, 2)
        return {'y': 'zahl', 'f': {'text': f'An einer Geradenkreuzung ist ein Winkel um {d}° größer als sein Nachbarwinkel. Wie groß ist der größere Winkel?'},
                'o': {'wert': wert(x), 'einheit': '°'}, 'c': f'(180 + {d}) / 2', 'w': f'Zusammen 180°, Unterschied {d}°: kleiner Winkel (180° − {d}°) : 2 = {zt(Fr(180 - d, 2))}°, großer {zt(x)}°.',
                'h': 'Nachbarwinkel ergeben 180°. Nimm den Unterschied weg und halbiere.'}
    if art == 1:          # ersetzt „alle vier Winkel zusammen“ (immer 360°, Prüfung)
        k = R.choice([2, 3, 4, 5])
        kl2 = 180 // (k + 1)
        return {'y': 'zahl', 'f': {'text': f'Zwei Geraden schneiden sich. Ein Winkel ist {k}-mal so groß wie sein Nachbarwinkel. Wie groß ist der größere Winkel?'}, 'o': {'wert': k * kl2, 'einheit': '°'},
                'c': f'{k} * 180 / ({k} + 1)', 'w': f'Zusammen 180°, das sind {k + 1} gleiche Teile: 180° : {k + 1} = {kl2}°. Der größere Winkel: {k} · {kl2}° = {k * kl2}°.',
                'h': f'Die beiden Nachbarwinkel bestehen zusammen aus {k + 1} gleichen Teilen.'}
    k = R.randint(2, 4)
    kl_ = Fr(180, k + 1)
    if kl_.denominator != 1: return g_kreuz(3)
    return {'y': 'zahl', 'f': {'text': f'An einer Geradenkreuzung ist ein Winkel {k}-mal so groß wie sein Nachbarwinkel. Wie groß ist der kleinere Winkel?'}, 'o': {'wert': int(kl_), 'einheit': '°'},
            'c': f'180 / ({k} + 1)', 'w': f'Kleiner + {k}-mal kleiner = 180°, also {k + 1} gleiche Teile: 180° : {k + 1} = {zt(kl_)}°.', 'h': f'Die beiden Winkel bestehen zusammen aus {k + 1} gleichen Teilen.'}


# ---------- 3 Um einen Punkt ----------
def g_punkt(st):
    n = {1: 2, 2: 3, 3: R.choice([3, 4])}[st]
    ges = 360 if st > 1 or R.random() < .5 else 180
    while True:
        ws = [R.randint(20, 150) for _ in range(n)]
        rest = ges - sum(ws)
        if 10 <= rest <= 170: break
    richt, s = [0], 0
    for w_ in ws + [rest]:
        s += w_
        richt.append(s)
    fig = facher(richt, [f'{w_}°' for w_ in ws] + ['?'])
    if st == 3 and R.random() < .35:      # Torte/Pizza (Prüfung)
        n = R.choice([6, 8, 10, 12])
        ding = R.choice(['Torte', 'Pizza'])
        if R.random() < .4:
            return {'y': 'zahl', 'f': {'text': f'Eine {ding} wird in {n} gleiche Stücke geschnitten. Wie groß ist der Winkel eines Stücks an der Spitze?'}, 'o': {'wert': 360 // n, 'einheit': '°'},
                    'c': f'360 / {n}', 'w': f'Alle Stücke liegen um den Mittelpunkt: 360° : {n} = {360 // n}°.', 'h': 'Alle Stücke zusammen ergeben einen Vollwinkel.'}
        k = R.randint(1, n - 1)
        return {'y': 'zahl', 'f': {'text': f'Eine {ding} wird in {n} gleiche Stücke geschnitten, {k} {"Stück ist" if k == 1 else "Stücke sind"} gegessen. Wie groß ist der Winkel des Rests (an der Mitte gemessen)?'},
                'o': {'wert': (n - k) * 360 // n, 'einheit': '°'}, 'c': f'({n} - {k}) * 360 / {n}',
                'w': f'Ein Stück: 360° : {n} = {360 // n}°. Übrig sind {n - k} Stücke: {n - k} · {360 // n}° = {(n - k) * 360 // n}°.', 'h': 'Rechne zuerst den Winkel eines Stücks aus.'}
    if st == 3 and R.random() < .5:
        k = R.choice([2, 3])
        a = Fr(360, 2 + k)
        if a.denominator != 1: return g_punkt(3)
        return {'y': 'zahl', 'f': {'text': f'Um einen Punkt liegen drei Winkel: α, β = α und γ = {k} · α. Zusammen ergeben sie einen Vollwinkel. Wie groß ist α?'},
                'o': {'wert': int(a), 'einheit': '°'}, 'c': f'360 / (1 + 1 + {k})', 'w': f'α + α + {k}α = {2 + k}α = 360°, also α = 360° : {2 + k} = {zt(a)}°.', 'h': 'Zähle, wie viele α-Teile es insgesamt sind.'}
    return {'y': 'zahl', 'f': {'text': ('Um einen Punkt liegen lückenlos die Winkel ' if ges == 360 else 'Auf einer Seite einer Geraden liegen nebeneinander die Winkel ') + ', '.join(f'{w_}°' for w_ in ws) + ' und ein weiterer Winkel. Wie groß ist er?', 'grafik': fig},
            'o': {'wert': rest, 'einheit': '°'}, 'c': f'{ges} - ' + ' - '.join(map(str, ws)), 'w': f'{ges}° − ' + ' − '.join(f'{w_}°' for w_ in ws) + f' = {rest}°.',
            'h': f'Alle Winkel zusammen ergeben {ges}°.'}


# ---------- 4 Uhr ----------
def g_uhr(st):
    if st == 1:
        if R.random() < .5:
            m = R.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
            return {'y': 'zahl', 'f': {'text': f'Um wie viel Grad dreht sich der Minutenzeiger in {m} Minuten?'}, 'o': {'wert': 6 * m, 'einheit': '°'}, 'c': f'{m} * 6',
                    'w': f'6° pro Minute: {m} · 6° = {6 * m}°.', 'h': 'In 60 Minuten dreht er sich um 360°.'}
        h = R.randint(1, 6)
        return {'y': 'zahl', 'f': {'text': f'Wie groß ist der kleinere Winkel zwischen den Zeigern um {h}:00 Uhr?', 'grafik': uhrbild(h, 0, '?')}, 'o': {'wert': 30 * h, 'einheit': '°'}, 'c': f'{h} * 30',
                'w': f'Der große Zeiger zeigt auf 12, der kleine auf {h}. {h} Abstände · 30° = {30 * h}°.', 'h': 'Zwischen zwei Stundenzahlen liegen 30°.'}
    if st == 2:
        art = R.randrange(4)
        if art == 3:          # Uhrzeit am Bild ablesen und Winkel bestimmen (Prüfung)
            h = R.randint(1, 11)
            k = min(h, 12 - h)
            return {'y': 'zahl', 'f': {'text': 'Die Uhr zeigt eine volle Stunde. Wie groß ist der kleinere Winkel zwischen den Zeigern?', 'grafik': uhrbild(h, 0)},
                    'o': {'wert': 30 * k, 'einheit': '°'}, 'c': f'{k} * 30', 'w': f'Die Uhr zeigt {h}:00 Uhr. Kürzester Weg zwischen 12 und {h}: {k} Abstände · 30° = {30 * k}°.',
                    'h': 'Lies zuerst die Uhrzeit ab. Zwischen zwei Stundenzahlen liegen 30°.'}
        if art == 0:
            h = R.randint(7, 11)
            return {'y': 'zahl', 'f': {'text': f'Wie groß ist der kleinere Winkel zwischen den Zeigern um {h}:00 Uhr?', 'grafik': uhrbild(h, 0, '?')}, 'o': {'wert': 30 * (12 - h), 'einheit': '°'}, 'c': f'(12 - {h}) * 30',
                    'w': f'Von {h} bis 12 sind es {12 - h} Abstände: {12 - h} · 30° = {30 * (12 - h)}°. (Der andere Winkel wäre {30 * h}°.)', 'h': 'Zähle den kürzeren Weg zwischen den Zeigern.'}
        if art == 1:
            g = R.choice([90, 120, 150, 180, 210, 240, 270, 300])
            return {'y': 'zahl', 'f': {'text': f'Der Minutenzeiger hat sich um {g}° gedreht. Wie viele Minuten sind vergangen?'}, 'o': {'wert': g // 6, 'einheit': 'min'}, 'c': f'{g} / 6',
                    'w': f'{g}° : 6° = {g // 6} min.', 'h': 'Der Minutenzeiger schafft 6° pro Minute.'}
        a = R.randint(1, 11)
        b = R.randint(1, 11)
        if a == b: b = (a % 11) + 1
        d = abs(a - b)
        k = min(d, 12 - d)
        return {'y': 'zahl', 'f': {'text': f'Wie groß ist der kleinere Winkel zwischen den Zahlen {a} und {b} auf dem Zifferblatt (vom Mittelpunkt aus gesehen)?'},
                'o': {'wert': 30 * k, 'einheit': '°'}, 'c': f'min(abs({a} - {b}), 12 - abs({a} - {b})) * 30', 'w': f'Kürzester Weg: {k} Abstände · 30° = {30 * k}°.', 'h': 'Zähle die Stundenabstände auf dem kürzeren Weg.'}
    art = R.randrange(3)
    if art == 0:
        h = R.randint(1, 11)
        g = abs(30 * h + 15 - 180)
        g = min(g, 360 - g)
        return {'y': 'zahl', 'f': {'text': f'Um {h}:30 Uhr steht der Stundenzeiger genau zwischen {h} und {h % 12 + 1}. Wie groß ist der kleinere Winkel zwischen den Zeigern?', 'grafik': uhrbild(h, 30, '?')},
                'o': {'wert': g, 'einheit': '°'}, 'c': f'min(abs({h} * 30 + 15 - 180), 360 - abs({h} * 30 + 15 - 180))',
                'w': f'Minutenzeiger auf 6 (180°), Stundenzeiger bei {h}½ ({30 * h + 15}°). Unterschied: {g}°.', 'h': 'Der Stundenzeiger bewegt sich in 30 Minuten um 15° weiter.'}
    if art == 1:
        m = R.choice([20, 40, 90, 120, 150, 180])
        return {'y': 'zahl', 'f': {'text': f'Um wie viel Grad dreht sich der Stundenzeiger in {m} Minuten?'}, 'o': {'wert': wert(Fr(m, 2)), 'einheit': '°'}, 'c': f'{m} / 60 * 30',
                'w': f'In 60 min dreht er sich um 30°, also 0,5° pro Minute: {m} · 0,5° = {zt(Fr(m, 2))}°.', 'h': 'Der Stundenzeiger braucht 60 Minuten für 30°.'}
    m = R.choice([75, 90, 100, 105, 135, 150])
    return {'y': 'zahl', 'f': {'text': f'Um wie viel Grad dreht sich der Minutenzeiger in {m} Minuten?'}, 'o': {'wert': 6 * m, 'einheit': '°'}, 'c': f'{m} * 6',
            'w': f'{m} · 6° = {6 * m}° (das ist mehr als eine ganze Drehung).', 'h': 'Pro Minute 6° – auch über 360° hinaus.'}


# ---------- 5 Drehungen ----------
ROSE = ['Norden', 'Nordosten', 'Osten', 'Südosten', 'Süden', 'Südwesten', 'Westen', 'Nordwesten']


def g_dreh(st):
    if st == 1:
        if R.random() < .5:
            t, g = R.choice([('eine Vierteldrehung', 90), ('eine halbe Drehung', 180), ('eine Dreivierteldrehung', 270), ('eine ganze Drehung', 360), ('zwei ganze Drehungen', 720), ('eine Achteldrehung', 45)])
            return {'y': 'zahl', 'f': {'text': f'Wie viel Grad sind {t}?'}, 'o': {'wert': g, 'einheit': '°'}, 'c': f'{g} / 360 * 360', 'w': f'Eine ganze Drehung hat 360°. {t[0].upper() + t[1:]}: {g}°.',
                    'h': 'Eine ganze Drehung sind 360°.'}
        i, k = R.randrange(8), R.randint(1, 4)
        return {'y': 'zahl', 'f': {'text': f'Du schaust nach {ROSE[i]} und drehst dich im Uhrzeigersinn nach {ROSE[(i + k) % 8]}. Um wie viel Grad drehst du dich (kürzester Weg im Uhrzeigersinn)?'},
                'o': {'wert': 45 * k, 'einheit': '°'}, 'c': f'{k} * 45', 'w': f'{k} {"Schritt" if k == 1 else "Schritte"} auf der Windrose zu je 45°: {45 * k}°.', 'h': 'Zwischen benachbarten Richtungen der Windrose liegen 45°.'}
    if st == 2:
        i = R.randrange(8)
        g = R.choice([45, 90, 135, 180, 225, 270, 315])
        r = ROSE[(i + g // 45) % 8]
        return {**wahl(R, r, [ROSE[(i - g // 45) % 8], ROSE[(i + g // 45 + 1) % 8], ROSE[(i + g // 90) % 8]] if ROSE[(i - g // 45) % 8] != r else [ROSE[(i + 1) % 8], ROSE[(i + 2) % 8], ROSE[(i + 3) % 8]]),
                'f': {'text': f'Ein Wanderer schaut nach {ROSE[i]} und dreht sich um {g}° im Uhrzeigersinn. In welche Richtung schaut er jetzt?', 'grafik': windrose()},
                'w': f'{g}° : 45° = {g // 45} {"Schritt" if g == 45 else "Schritte"} im Uhrzeigersinn von {ROSE[i]}: {r}.', 'h': 'Ein Schritt auf der Windrose sind 45°. Im Uhrzeigersinn: N → NO → O …'}
    art = R.randrange(3)
    if art == 2:          # gegen den Uhrzeigersinn (Prüfung)
        i, k = R.randrange(8), R.choice([1, 2, 3, 5, 6, 7])
        r = ROSE[(i - k) % 8]
        f = [ROSE[(i + k) % 8], ROSE[(i - k - 1) % 8], ROSE[(i - k + 1) % 8]]
        return {**wahl_rund(R, r, [x for x in f if x != r]), 'f': {'text': f'Du schaust nach {ROSE[i]} und drehst dich um {45 * k}° gegen den Uhrzeigersinn. Wohin schaust du jetzt?', 'grafik': windrose()},
                'w': f'{45 * k}° : 45° = {k} {"Schritt" if k == 1 else "Schritte"} gegen den Uhrzeigersinn (N → NW → W …) von {ROSE[i]} aus: {r}.',
                'h': 'Gegen den Uhrzeigersinn geht es auf der Windrose N → NW → W → SW …'}
    if art == 0:
        a, b = R.choice([90, 135, 180, 45]), R.choice([90, 45, 180, 270])
        s = (a + b) % 360
        return {'y': 'zahl', 'f': {'text': f'Ein Roboter dreht sich zuerst um {a}° und dann noch einmal um {b}° in dieselbe Richtung. Um wie viel Grad müsste er sich noch weiter drehen, bis er wieder in die Startrichtung schaut?'},
                'o': {'wert': (360 - s) % 360 or 360, 'einheit': '°'}, 'c': f'360 - ({a} + {b}) % 360' if s else '360',
                'w': f'Bisher {a}° + {b}° = {a + b}°. ' + (f'Bis 360° fehlen {360 - s}°.' if a + b < 360 else f'Das ist mehr als eine Drehung; bis zur nächsten vollen Drehung fehlen {(360 - s) % 360 or 360}°.'),
                'h': 'Eine volle Drehung sind 360°.'}
    n = R.choice([3, 4, 5, 6, 8, 9, 10, 12])
    return {'y': 'zahl', 'f': {'text': f'Ein Karussell hat {n} Gondeln in gleichen Abständen. Um wie viel Grad muss es sich drehen, damit die nächste Gondel an die Stelle der vorigen kommt?'},
            'o': {'wert': wert(Fr(360, n)), 'einheit': '°'}, 'c': f'360 / {n}', 'w': f'360° : {n} = {zt(Fr(360, n))}°.', 'h': 'Eine ganze Drehung wird in gleiche Teile geteilt.'}


# ---------- 6 Figuren ----------
FIG = {'groesser': 0}


def g_fig(st):
    if st == 1:
        a = R.randint(15, 75)
        if a == 45: a = 40
        l = 7
        h = round(l * math.tan(math.radians(a)), 3)
        fig = {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [l, 0], 'C': [l, h], 'D': [0, h]}, 'flaeche': ['A', 'B', 'C', 'D'],
               'linien': [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['A', 'C', '', 'gestrichelt']], 'winkel': [['A', 'B', 'C', f'{a}°'], ['A', 'C', 'D', '?']]}
        return {'y': 'zahl', 'f': {'text': f'Im Rechteck ABCD teilt die Diagonale [AC] den Winkel bei A. Ein Teil ist {a}°. Wie groß ist der andere Teil?', 'grafik': fig},
                'o': {'wert': 90 - a, 'einheit': '°'}, 'c': f'90 - {a}', 'w': f'Der Eckwinkel ist 90°: 90° − {a}° = {90 - a}°.', 'h': 'Jeder Eckwinkel im Rechteck ist 90°.'}
    if st == 2:
        if R.random() < .3:          # Quadrat-Diagonale (Prüfung)
            if R.random() < .4:
                aw = wahl_rund(R, '45°', ['90°', '30°', '60°'])
                return {**aw, 'f': {'text': 'Im Quadrat teilt die Diagonale den Eckwinkel in zwei Teile. Wie groß ist jeder Teil?'},
                        'w': 'Im Quadrat sind beide Teile gleich groß: 90° : 2 = 45°.', 'h': 'Der Eckwinkel ist 90°. Im Quadrat sind beide Teile gleich.'}
            a = R.choice([x for x in range(15, 76) if x != 45])
            aw = wahl_rund(R, f'Nein: Der andere Teil ist 90° − {a}° = {90 - a}°.', ['Ja: Die Diagonale halbiert den Eckwinkel immer.', f'Nein: Der andere Teil ist 180° − {a}° = {180 - a}°.'], 3)
            return {**aw, 'f': {'text': f'Im Rechteck (kein Quadrat) teilt die Diagonale den Eckwinkel in {a}° und einen zweiten Teil. Stimmt die Aussage „Beide Teile sind 45°“?'},
                    'w': f'Nur im Quadrat sind beide Teile 45°. Hier: 90° − {a}° = {90 - a}°.', 'h': 'Beide Teile ergeben zusammen den rechten Eckwinkel.'}
        art = R.randrange(2)
        if art == 1 and FIG['groesser'] >= 4: art = 0          # höchstens 4 Aufgaben „um x° größer“ (Prüfung)
        if art == 1: FIG['groesser'] += 1
        if art == 0:
            k = R.choice([2, 3, 5, 6])
            return {'y': 'zahl', 'f': {'text': f'Ein rechter Winkel wird durch {k - 1} Strahlen in {k} gleich große Winkel geteilt. Wie groß ist jeder?'}, 'o': {'wert': wert(Fr(90, k)), 'einheit': '°'},
                    'c': f'90 / {k}', 'w': f'Ein rechter Winkel hat 90°: 90° : {k} = {zt(Fr(90, k))}°.', 'h': 'Ein rechter Winkel hat 90°.'}
        d = 2 * R.randint(3, 35)
        return {'y': 'zahl', 'f': {'text': f'Im Rechteck teilt eine Strecke von einer Ecke aus den Eckwinkel in zwei Teile. Ein Teil ist um {d}° größer als der andere. Wie groß ist der größere Teil?'},
                'o': {'wert': (90 + d) // 2, 'einheit': '°'}, 'c': f'(90 + {d}) / 2', 'w': f'Zusammen 90°. Ohne den Unterschied: 90° − {d}° = {90 - d}°, halbiert {(90 - d) // 2}°. Der größere Teil: {(90 - d) // 2}° + {d}° = {(90 + d) // 2}°.',
                'h': 'Nimm den Unterschied weg, dann bleiben zwei gleich große Teile.'}
    art = R.randrange(3)
    if art == 0:
        return {'y': 'zahl', 'f': {'text': 'Im Quadrat ABCD zeichnet man beide Diagonalen. Wie groß ist der Winkel zwischen der Diagonale [AC] und der Seite [AB]?',
                                   'grafik': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [5, 0], 'C': [5, 5], 'D': [0, 5]}, 'flaeche': ['A', 'B', 'C', 'D'],
                                              'linien': [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['A', 'C', '', 'gestrichelt'], ['B', 'D', '', 'gestrichelt']], 'winkel': [['A', 'B', 'C', '?']]}},
                'o': {'wert': 45, 'einheit': '°'}, 'c': '90 / 2', 'w': 'Im Quadrat teilt die Diagonale den rechten Winkel in zwei gleiche Teile: 90° : 2 = 45°.', 'h': 'Im Quadrat sind beide Teile gleich groß.'} if R.random() < .3 else \
            {'y': 'zahl', 'f': {'text': f'Von einer Ecke eines Rechtecks gehen zwei Strecken aus, die den Eckwinkel in drei Teile teilen. Zwei Teile sind {(x := R.randint(10, 40))}° und {(y := R.randint(10, 40))}°. Wie groß ist der dritte Teil?'},
             'o': {'wert': 90 - x - y, 'einheit': '°'}, 'c': f'90 - {x} - {y}', 'w': f'Der Eckwinkel im Rechteck ist 90°: 90° − {x}° − {y}° = {90 - x - y}°.', 'h': 'Alle drei Teile ergeben zusammen den Eckwinkel.'}
    if art == 1:
        a = R.randint(10, 80)
        return {'y': 'zahl', 'f': {'text': f'Eine Schranke liegt waagrecht. Sie wird um {a}° nach oben gedreht. Um wie viel Grad muss sie noch weiter gedreht werden, bis sie senkrecht steht?'},
                'o': {'wert': 90 - a, 'einheit': '°'}, 'c': f'90 - {a}', 'w': f'Von waagrecht bis senkrecht sind es 90°. Es fehlen 90° − {a}° = {90 - a}°.', 'h': 'Waagrecht und senkrecht bilden einen rechten Winkel.'}
    k = R.choice([2, 4, 5, 8])          # ersetzt die Raute-Aufgabe (Raute wird in dieser Karte nicht erklärt, Prüfung)
    t = 90 // (k + 1)
    return {'y': 'zahl', 'f': {'text': f'Im Rechteck teilt eine Strecke von einer Ecke aus den Eckwinkel in zwei Teile. Ein Teil ist {k}-mal so groß wie der andere. Wie groß ist der größere Teil?'},
            'o': {'wert': k * t, 'einheit': '°'}, 'c': f'{k} * 90 / ({k} + 1)', 'w': f'Zusammen 90°, das sind {k + 1} gleiche Teile: 90° : {k + 1} = {t}°. Der größere Teil: {k} · {t}° = {k * t}°.',
            'h': f'Die beiden Teile bestehen zusammen aus {k + 1} gleichen Stücken.'}


# ---------- 7 Verstehen ----------
# Prüfung: alle Antworten gleich gebaut, jeweils mit Zahl oder Begründung
def g_vers(st):
    a = R.randint(20, 80)
    if st == 1:
        m = R.choice([10, 15, 20, 25, 40, 45, 50])
        aussagen = [(f'In {m} Minuten dreht sich der Minutenzeiger um {6 * m}°.', f'Ja, denn {m} · 6° = {6 * m}°.', [f'Nein, denn {m} · 30° = {zt(30 * m)}°.', f'Nein, denn {m} · 3° = {3 * m}°.']),
                    (f'In {m} Minuten dreht sich der Minutenzeiger um {m}°.', f'Nein, denn {m} · 6° = {6 * m}°.', ['Ja, denn in 1 Minute dreht er sich um 1°.', f'Nein, denn {m} · 30° = {zt(30 * m)}°.']),
                    (f'Ein Winkel von {a}° und einer von {180 - a}° nebeneinander ergeben einen gestreckten Winkel.', f'Ja, denn {a}° + {180 - a}° = 180°.', ['Nein, ein gestreckter Winkel hat 360°.', 'Nein, ein gestreckter Winkel hat 90°.']),
                    (f'Ein Winkel von {a}° und einer von {100 - a}° nebeneinander ergeben einen rechten Winkel.', f'Nein, denn {a}° + {100 - a}° = 100°, nicht 90°.', [f'Ja, denn {a}° + {100 - a}° = 90°.', 'Ja, denn zwei spitze Winkel ergeben immer einen rechten Winkel.']),
                    ('Eine halbe Drehung sind 90°.', 'Nein, eine halbe Drehung sind 360° : 2 = 180°.', ['Ja, denn 360° : 4 = 90°.', 'Nein, eine halbe Drehung sind 360°.']),
                    ('In 30 Minuten dreht sich der Minutenzeiger um 180°.', 'Ja, denn 30 · 6° = 180°.', ['Nein, denn 30 · 30° = 900°.', 'Nein, denn 30 · 3° = 90°.'])]
    elif st == 2:
        h = R.randint(1, 11)
        n = min(h, 12 - h); k = n * 30
        b = R.randint(20, 80)
        c = R.randint(95, 170)
        falsch_h = h * 10 if h * 10 != k else h * 10 + 30
        if 6 * h in (k, falsch_h, 10 * h) or 15 * h == k: return g_vers(st)          # keine Ablenker mit dem richtigen Wert
        art_ = 'stumpfen' if a + b > 90 else ('rechten' if a + b == 90 else 'spitzen')
        anders = 'spitzen' if a + b > 90 else 'stumpfen'
        aussagen = [(f'An einer Geradenkreuzung mit α = {a}° ist der gegenüberliegende Winkel ebenfalls {a}°.', 'Ja, denn beide ergänzen denselben Nachbarwinkel zu 180°.', [f'Nein, er ist 180° − {a}° = {180 - a}°.', f'Nein, er ist 360° − {a}° = {360 - a}°.']),
                    (f'An einer Geradenkreuzung mit α = {a}° ist der Nachbarwinkel ebenfalls {a}°.', f'Nein, Nachbarwinkel ergeben zusammen 180°: 180° − {a}° = {180 - a}°.', ['Ja, an einer Kreuzung sind alle Winkel gleich.', f'Nein, er ist 360° − {a}° = {360 - a}°.']),
                    (f'Die spitzen Winkel {a}° und {b}° nebeneinander ergeben einen {art_} Winkel.', f'Ja, denn {a}° + {b}° = {a + b}°.', [f'Nein, zwei spitze Winkel ergeben immer einen {anders} Winkel.', 'Nein, sie ergeben einen gestreckten Winkel.']),
                    (f'Die spitzen Winkel {a}° und {b}° nebeneinander ergeben einen {anders} Winkel.', f'Nein, denn {a}° + {b}° = {a + b}°, also ein {art_[:-1]} Winkel.', [f'Ja, zwei spitze Winkel ergeben immer einen {anders} Winkel.', 'Nein, sie ergeben einen gestreckten Winkel.']),
                    (f'Um {h}:00 Uhr bilden die Zeiger einen Winkel von {k}°.', f'Ja, denn {n} {"Abstand" if n == 1 else "Abstände"} · 30° = {k}°.', [f'Nein, denn {h} · 10° = {10 * h}°.' if 10 * h != k else f'Nein, denn {h} · 15° = {15 * h}°.', f'Nein, denn {h} · 6° = {6 * h}°.']),
                    (f'Um {h}:00 Uhr bilden die Zeiger einen Winkel von {falsch_h}°.', f'Nein, zwischen zwei Stundenzahlen liegen 30°: {n} · 30° = {k}°.', [f'Ja, denn {h} · 10° = {10 * h}°.' if falsch_h == 10 * h else f'Ja, denn {h} · 10° + 30° = {falsch_h}°.', f'Nein, denn {h} · 6° = {6 * h}°.']),
                    (f'Ein stumpfer Winkel von {c}° und ein Winkel von {180 - c}° ergeben zusammen einen gestreckten Winkel.', f'Ja, denn {c}° + {180 - c}° = 180°.', ['Nein, ein stumpfer und ein spitzer Winkel ergeben immer einen stumpfen Winkel.', 'Nein, ein gestreckter Winkel hat 360°.'])]
    else:
        i = R.randrange(8); kk = R.randint(1, 7)
        n4 = R.choice([3, 4, 5, 6, 8])
        gegen = ROSE[(i - kk) % 8] if (i - kk) % 8 != (i + kk) % 8 else ROSE[(i + kk + 1) % 8]
        aussagen = [(f'Wer von {ROSE[i]} aus um {45 * kk}° im Uhrzeigersinn dreht, schaut nach {ROSE[(i + kk) % 8]}.', f'Ja, denn {kk} {"Schritt" if kk == 1 else "Schritte"} zu 45° sind {45 * kk}°.', [f'Nein, man schaut nach {gegen}.', f'Nein, denn {45 * kk}° sind {kk} Schritte zu 90°.']),
                    (f'Wer von {ROSE[i]} aus um {45 * kk}° im Uhrzeigersinn dreht, schaut nach {gegen}.', f'Nein, im Uhrzeigersinn kommt man nach {ROSE[(i + kk) % 8]}.', ['Ja, die Drehrichtung ist egal.', f'Ja, denn {kk} {"Schritt" if kk == 1 else "Schritte"} zu 45° sind {45 * kk}°.']),
                    (f'{n4} gleich große Winkel um einen Punkt sind je {zt(Fr(360, n4))}° groß.', f'Ja, denn 360° : {n4} = {zt(Fr(360, n4))}°.', [f'Nein, denn 180° : {n4} = {zt(Fr(180, n4))}°.', f'Nein, denn 90° : {n4} = {zt(Fr(90, n4))}°.']),
                    (f'{n4} gleich große Winkel um einen Punkt sind je {zt(Fr(180, n4))}° groß.', f'Nein, um einen Punkt sind es 360°: 360° : {n4} = {zt(Fr(360, n4))}°.', [f'Ja, denn 180° : {n4} = {zt(Fr(180, n4))}°.', f'Nein, denn 90° : {n4} = {zt(Fr(90, n4))}°.']),
                    ('Zwei stumpfe Winkel nebeneinander ergeben immer mehr als 180°.', 'Ja, jeder ist größer als 90°, zusammen also mehr als 180°.', ['Nein, z. B. 100° + 70° = 170°.', 'Nein, zusammen sind es immer genau 180°.']),
                    ('Drei spitze Winkel um einen Punkt können einen Vollwinkel ergeben.', 'Nein, drei Winkel unter 90° ergeben zusammen weniger als 270°.', ['Ja, z. B. 120° + 120° + 120° = 360°.', 'Ja, wenn jeder Winkel 90° ist.']),
                    ('Wer sich von Norden aus um 270° im Uhrzeigersinn dreht, schaut nach Westen.', 'Ja, 270° sind drei Vierteldrehungen: N → O → S → W.', ['Nein, 270° im Uhrzeigersinn führen nach Osten.', 'Nein, 270° führen nach Süden.']),
                    ('Im Rechteck teilt die Diagonale den Eckwinkel immer in zwei gleiche Teile.', 'Nein, nur im Quadrat (je 45°). Im Rechteck sind die Teile verschieden.', ['Ja, die Diagonale halbiert jeden Eckwinkel.', 'Ja, beide Teile sind immer 45°.']),
                    ('Vier gleich große Winkel um einen Punkt sind rechte Winkel.', 'Ja, denn 360° : 4 = 90°.', ['Nein, denn 180° : 4 = 45°.', 'Nein, denn 360° : 4 = 80°.'])]
    s_, r, f = R.choice(aussagen)
    return {**wahl_rund(R, r, f, 3), 'f': {'text': f'Stimmt die Aussage? „{s_}“'}, 'w': r, 'h': 'Rechne mit 90°, 180° oder 360° nach oder mach eine Skizze.'}


GEN = {'ergaenzen': g_erg, 'kreuzung': g_kreuz, 'um_punkt': g_punkt, 'uhr': g_uhr, 'drehungen': g_dreh, 'figuren': g_fig, 'verstehen': g_vers}

DATEI = datei(E, 'Winkel ergänzen und an Geradenkreuzungen, um einen Punkt, an der Uhr, bei Drehungen und in Rechtecken berechnen.', MERKE,
              [('Winkel zusammensetzen', ['ergaenzen', 'kreuzung', 'um_punkt']),
               ('Winkel im Alltag', ['uhr', 'drehungen']),
               ('Figuren und Verstehen', ['figuren', 'verstehen'])],
              ETAPPEN, GEN,
              offen=['WICHTIG: themenliste.json ordnet „Winkelsätze“ Kl. 5 zu, nennt aber keinen lehrplan_gym-Wortlaut. Laut LehrplanPLUS Gymnasium Kl. 5 gibt es nur „Winkel bis 360° messen, zeichnen, beschreiben“. Stufen-/Wechselwinkel und Innenwinkelsummen (Dreieck, Viereck) sind Stoff der Jahrgangsstufe 7 und wurden weggelassen. Vorschlag: dieses Thema für Kl. 5 so lassen und die eigentlichen Winkelsätze als Kl.-7-Thema führen.',
                     'Nachbarwinkel an der Geradenkreuzung werden nur über „ergänzen zu 180°“ begründet, ohne die Fachbegriffe Neben-/Scheitelwinkel einzuführen (Kl. 7).',
                     'Zeichnungen: Strahlenfächer und Geradenkreuzung als Figur mit Winkelbögen, Rechteck/Quadrat mit Diagonale; Uhr (Zifferblatt mit Zeigern) und Windrose als Figur in den Lernkarten uhr und drehungen und in Aufgaben.'])

# Umbau U5 (Achte Runde, Vorgabe 16.11.): Lernkarten nach dem neuen Muster – einstieg, woerter (≤ 3), Kartenbild,
# Bildergeschichte (schritte mit bild), „Pass auf!“ (fehler + fehler_bild), MERKE (regel).
# Situationen: Pizza, Straßenkreuzung, Torte, Uhr, Kompass, Blatt Papier. Die vorhandenen Figuren bleiben Kartenbild;
# die Schritte ändern nur die Winkelbeschriftungen (Feld winkel).
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl5.py) – die Aufgaben bleiben wörtlich gleich.
import math  # noqa: E402

from _umbau_kl5 import umbau  # noqa: E402

KREUZ = lambda b, g, d: {'winkel': [['S', '_P0', '_P1', 'α = 70°'], ['S', '_P1', '_P2', b], ['S', '_P2', '_P3', g], ['S', '_P3', '_P4', d]]}
STRAHL = lambda w: [round(5 * math.cos(math.radians(w)), 3), round(5 * math.sin(math.radians(w)), 3)]

KARTEN = {
 'ergaenzen': {
  'einstieg': 'Zwei Pizzastücke nebeneinander ergeben zusammen eine breitere Spitze. Bei Winkeln ist es genauso: Nebeneinander werden sie addiert. Fehlt ein Stück bis zu einem bekannten Ganzen, ⟦ergänzt⟧ du es.',
  'woerter': [['ergänzt', 'den fehlenden Teil bis zum Ganzen ausgerechnet'], ['gestreckten Winkel', '180°: Die Schenkel bilden eine gerade Linie'],
              ['β', 'der griechische Buchstabe „beta“, ein Name für einen Winkel']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'α = 50° und β liegen nebeneinander an einer geraden Linie.'},
               {'text': 'Zusammen bilden sie einen gestreckten Winkel: 180°.'},
               {'text': 'Also ist β = 180° − 50° = ⟦130°⟧.', 'bild': {'winkel': [['S', '_P0', '_P1', 'α = 50°'], ['S', '_P1', '_P2', 'β = 130°']]}}],
  'fehler': 'β = 90° − 50° = 40° ist falsch. Die Linie ist gerade, das Ganze sind also 180°, nicht 90°.',
  'regel': 'Fehlender Winkel = ⟦Ganzes minus bekannter Winkel⟧. Das Ganze ist 90°, 180° oder 360°.'},
 'kreuzung': {
  'einstieg': 'Wo sich zwei gerade Straßen kreuzen, entstehen vier Ecken. Gegenüberliegende Ecken sind gleich groß. Ecken nebeneinander ergeben zusammen eine gerade Straßenseite: So ist es an jeder ⟦Geradenkreuzung⟧.',
  'woerter': [['Nachbarwinkel', 'zwei Winkel nebeneinander an der Kreuzung; zusammen 180°'], ['gegenüberliegende Winkel', 'liegen sich gegenüber; sie sind gleich groß']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'α = 70°. Sein Nachbarwinkel β ergänzt ihn zu 180°: β = 110°.', 'bild': KREUZ('β = 110°', 'γ', 'δ')},
               {'text': 'γ ist Nachbarwinkel von β: 180° − 110° = 70°.', 'bild': KREUZ('β = 110°', 'γ = 70°', 'δ')},
               {'text': 'Also sind gegenüberliegende Winkel gleich: ⟦γ = α = 70°⟧, δ = β = 110°.', 'bild': KREUZ('β = 110°', 'γ = 70°', 'δ = 110°')}],
  'fehler': 'β = 70° annehmen, nur weil β neben α liegt, ist falsch. Gleich groß sind nur die gegenüberliegenden Winkel.',
  'regel': '⟦Gegenüberliegende Winkel⟧ sind gleich groß. Nachbarwinkel ergeben zusammen 180°.'},
 'um_punkt': {
  'einstieg': 'Eine runde Torte wird in Stücke geschnitten, die in der Mitte zusammenstoßen. Alle Spitzen zusammen ergeben eine ganze Drehung. So ergeben ⟦Winkel um einen Punkt⟧ zusammen 360°.',
  'woerter': [['lückenlos', 'ohne Lücke und ohne Überlappung'], ['Vollwinkel', '360°, eine ganze Drehung']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'Um einen Punkt liegen lückenlos 100°, 80°, 120° und δ.'},
               {'text': 'Zusammen bilden sie einen Vollwinkel: 360°.'},
               {'text': 'δ = 360° − 100° − 80° − 120° = ⟦60°⟧.',
                'bild': {'winkel': [['S', '_P0', '_P1', 'α = 100°'], ['S', '_P1', '_P2', 'β = 80°'], ['S', '_P2', '_P3', 'γ = 120°'], ['S', '_P3', '_P4', 'δ = 60°']]}}],
  'fehler': 'Nur einen Winkel abziehen: 360° − 120° = 240°. Das wäre für ein einziges Stück fast die ganze Torte.',
  'regel': 'Winkel um einen Punkt ergeben ⟦360°⟧. Auf einer Seite einer Geraden ergeben sie 180°.'},
 'uhr': {
  'einstieg': 'Der große Uhrzeiger dreht sich in einer Stunde einmal ganz herum, also 360°. Das Zifferblatt hat 12 Zahlen in gleichen Abständen. So rechnest du ⟦Winkel an der Uhr⟧ aus.',
  'woerter': [['Zifferblatt', 'die Scheibe der Uhr mit den Zahlen 1 bis 12'], ['Stundenabstand', 'Abstand zweier Nachbarzahlen: 360° : 12 = 30°']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'Ein Stundenabstand ist 360° : 12 = 30°.', 'bild': {'winkel': []}},
               {'text': 'Um 4:00 Uhr zeigen die Zeiger auf 12 und auf 4.'},
               {'text': 'Dazwischen liegen 4 Stundenabstände: 4 · 30° = ⟦120°⟧.', 'bild': {'winkel': [['M', '_z12', '_z4', '120°']]}}],
  'fehler': 'In 15 Minuten dreht sich der Minutenzeiger nicht um 15°. Er schafft 6° pro Minute, also 90°.',
  'regel': 'Zwischen zwei Zahlen liegen ⟦30°⟧. Der Minutenzeiger dreht 6° pro Minute, der Stundenzeiger 0,5° pro Minute.'},
 'drehungen': {
  'einstieg': 'Ein Kompass zeigt Norden, Osten, Süden, Westen und die Richtungen dazwischen. Von einer Richtung zur anderen drehst du dich um einen Winkel. So rechnest du mit ⟦Drehungen⟧.',
  'woerter': [['Windrose', 'Bild mit 8 Himmelsrichtungen: N, NO, O, SO, S, SW, W, NW'], ['im Uhrzeigersinn', 'rechts herum, wie die Uhrzeiger']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'Die Windrose teilt 360° in 8 gleiche Teile: je 45°.', 'bild': {'winkel': [['_M', 'N', 'NO', '45°']]}},
               {'text': 'Von N im Uhrzeigersinn bis SO: N → NO → O → SO.'},
               {'text': 'Das sind 3 Schritte: 3 · 45° = ⟦135°⟧.', 'bild': {'winkel': [['_M', 'N', 'SO', '135°']]}}],
  'fehler': 'Von Norden nach Osten 180° annehmen ist falsch. Das ist eine Vierteldrehung, also 90°. 180° wäre bis Süden.',
  'fehler_bild': {'winkel': [['_M', 'N', 'O', '90°']]},
  'regel': 'Zwischen zwei Nachbarrichtungen liegen ⟦45°⟧. Ganze Drehung 360°, halbe 180°, Vierteldrehung 90°.'},
 'figuren': {
  'einstieg': 'Ein Blatt Papier hat vier rechte Ecken. Faltest du es schräg von Ecke zu Ecke, teilt der Knick eine Ecke. Diese schräge Linie heißt ⟦Diagonale⟧.',
  'woerter': [['Diagonale', 'die Strecke zwischen zwei gegenüberliegenden Ecken'], ['[AC]', 'die Diagonale von A nach C']],
  'bild': 'BEHALTEN',
  'schritte': [{'text': 'Im Rechteck ABCD ist der Winkel bei A ein rechter Winkel: 90°.'},
               {'text': 'Die Diagonale [AC] teilt ihn. Ein Teil ist 35°.'},
               {'text': 'Der andere Teil ist 90° − 35° = ⟦55°⟧.', 'bild': {'winkel': [['A', 'B', 'C', '35°'], ['A', 'C', 'D', '55°']]}}],
  'fehler': 'Den zweiten Teil auch 35° nennen ist falsch. Gleich groß sind die beiden Teile nur im Quadrat: je 45°.',
  'regel': 'In Rechteck und Quadrat ist jede Ecke ⟦90°⟧. Die Teile einer geteilten Ecke ergeben zusammen 90°.'},
 'verstehen': {
  'einstieg': 'Jemand behauptet: „Zwei stumpfe Winkel nebeneinander ergeben immer mehr als 180°.“ Stimmt das immer? So eine Behauptung ist eine ⟦Aussage⟧, die du prüfst.',
  'woerter': [['Aussage', 'ein Satz, der richtig oder falsch ist'], ['stumpf', 'zwischen 90° und 180°'], ['überstumpf', 'zwischen 180° und 360°']],
  'bild': {'typ': 'figur', 'punkte': {'S': [0, 0], '_P0': [5, 0], '_P1': STRAHL(100), '_P2': STRAHL(200)},
           'linien': [['S', '_P0'], ['S', '_P1'], ['S', '_P2']], 'winkel': [['S', '_P0', '_P1', '100°'], ['S', '_P1', '_P2', '100°']]},
  'schritte': [{'text': 'Beispiel: 100° + 100° = 200°. Ein Beispiel reicht aber nicht für „immer“.'},
               {'text': 'Jeder stumpfe Winkel ist größer als 90°. Zwei sind größer als 180°.'},
               {'text': 'Jeder ist kleiner als 180°. Zwei sind kleiner als 360°.'},
               {'text': 'Die Summe ist immer überstumpf. Die Aussage ist ⟦richtig⟧.'}],
  'fehler': 'Nur ein Beispiel prüfen, das zufällig passt, ist unsicher. Für „immer“ brauchst du eine Begründung oder ein Gegenbeispiel.',
  'regel': 'Für „immer“ brauchst du eine ⟦Begründung⟧ für alle Fälle. Zum Widerlegen genügt ein Gegenbeispiel.'},
}
umbau(DATEI, KARTEN)


if __name__ == '__main__':
    schreibe(DATEI)
