#!/usr/bin/env python3
"""Thema funktionen.linear – Lineare Funktionen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, L, Z, baue, cz, eur, ist_endlich, kl, lin, mit_bild, zt  # noqa: E402

META = {'thema_schluessel': 'funktionen.linear', 'thema_id': 33, 'block_id': 72, 'klasse': {'gym_by': 8, 'rs_by': 8}}

ETAPPEN = [
    {'lernziel': 'ablesen', 'titel': 'Steigung m und Achsenabschnitt t',
     'regel': 'Der Graph von y = m · x + t ist eine ⟦Gerade⟧. ⟦m⟧ ist die Steigung: Gehst du 1 nach rechts, geht es m nach oben (bei negativem m nach unten) – wie eine Straße bergauf oder bergab. ⟦t⟧ ist der y-Achsenabschnitt: Dort schneidet die Gerade die y-Achse.',
     'schritte': ['y = 5 − 2x umsortieren: y = −2x + 5.', '⟦t = 5⟧: Die Gerade schneidet die y-Achse bei (0 | 5).',
                  '⟦m = −2⟧: Von jedem Punkt aus 1 nach rechts und 2 nach unten – die Gerade fällt. Das zeigt das Steigungsdreieck im Bild.'],
     'fehler': 'Bei y = 5 − 2x ist m nicht 5. Die Steigung ist die Zahl ⟦vor dem x⟧, mit Vorzeichen: m = −2.',
     'bild': {'typ': 'koordinaten', 'x': [-1, 4], 'y': [-2, 6], 'graphen': [{'art': 'linear', 'm': -2, 't': 5, 'name': 'y = −2x + 5'}],
              'punkte': [{'x': 0, 'y': 5, 'name': '(0 | 5)'}], 'strecken': [[1, 3, 2, 3, 'gestrichelt'], [2, 3, 2, 1, 'gestrichelt']]},
     '_verbot': ['y = 5 − 2x']},
    {'lernziel': 'zwei_punkte', 'titel': 'Steigung aus zwei Punkten',
     'regel': 'Durch zwei Punkte P(x₁ | y₁) und Q(x₂ | y₂) geht genau eine Gerade. Ihre Steigung ist ⟦m = (y₂ − y₁) : (x₂ − x₁)⟧ („Höhenunterschied durch Längenunterschied“).',
     'schritte': ['P(1 | 3), Q(4 | 9). Von P nach Q gehst du 4 − 1 = 3 nach rechts.', 'Dabei steigst du 9 − 3 = 6 nach oben.',
                  '6 nach oben auf 3 nach rechts heißt: 2 nach oben auf 1 nach rechts. ⟦m = 6 : 3 = 2⟧.'],
     'fehler': 'm = (4 − 1) : (9 − 3) = 0,5 ist falsch: Die ⟦y-Differenz⟧ gehört nach oben (in den Zähler), die x-Differenz nach unten.',
     'bild': {'typ': 'koordinaten', 'x': [-1, 6], 'y': [-1, 11], 'graphen': [{'art': 'linear', 'm': 2, 't': 1}],
              'punkte': [{'x': 1, 'y': 3, 'name': 'P'}, {'x': 4, 'y': 9, 'name': 'Q'}], 'strecken': [[1, 3, 4, 3, 'gestrichelt'], [4, 3, 4, 9, 'gestrichelt']]},
     '_verbot': ['P(1 | 3), Q(4 | 9)']},
    {'lernziel': 'proportional', 'titel': 'Proportionalität: Ursprungsgerade',
     'regel': 'Bei einer ⟦direkten Proportionalität⟧ gilt y = k · x. Der Graph ist eine Gerade durch den ⟦Ursprung⟧ (t = 0). k ist der Proportionalitätsfaktor, z. B. der Preis pro Stück.',
     'schritte': ['3 kg Äpfel kosten 7,50 €.', 'k = 7,50 € : 3 kg = 2,50 € pro kg', '⟦y = 2,5 · x⟧, also kosten 8 kg 20 €.'],
     'fehler': 'y = 2x + 1 ist ⟦keine⟧ Proportionalität: Für x = 0 ist y = 1, die Gerade geht nicht durch den Ursprung. Verdoppelt man x, verdoppelt sich y nicht.',
     'bild': {'typ': 'koordinaten', 'x': [0, 4], 'y': [0, 10], 'graphen': [{'art': 'linear', 'm': 2.5, 't': 0, 'name': 'y = 2,5x'}, {'art': 'linear', 'm': 2, 't': 1, 'name': 'y = 2x + 1'}],
              'punkte': [{'x': 0, 'y': 0, 'name': 'O'}, {'x': 0, 'y': 1}], 'name_x': 'kg', 'name_y': '€'},
     '_verbot': ['3 kg Äpfel kosten 7,50 €']},
    {'lernziel': 'aufstellen', 'titel': 'Geradengleichung aufstellen',
     'regel': 'Kennst du m und einen Punkt P(a | b), setzt du P in y = m · x + t ein und berechnest ⟦t = b − m · a⟧. Bei zwei Punkten berechnest du ⟦zuerst m⟧.',
     'schritte': ['m = 3, Punkt P(2 | 1). Setze x = 2 und y = 1 in y = 3x + t ein.', '1 = 3 · 2 + t, also t = 1 − 6 = −5.', '⟦y = 3x − 5⟧',
                  'Anschaulich: Von P(2 | 1) gehst du 2 nach links bis zur y-Achse. Bei Steigung 3 geht es dabei 2 · 3 = 6 nach unten: 1 − 6 = −5 = t.'],
     'probe': '3 · 2 − 5 = 1 ✓',
     'fehler': 'Bei P(2 | 1) setzt man x = 2 und y = 1 ein – nicht umgekehrt. 2 = 3 · 1 + t führt zu ⟦t = −1⟧ und einer falschen Geraden.',
     '_verbot': ['P(2 | 1)']},
    {'lernziel': 'schnittpunkte', 'titel': 'Schnittpunkte berechnen',
     'regel': 'Schnitt mit der ⟦x-Achse⟧: y = 0 setzen (Nullstelle). Schnitt mit der ⟦y-Achse⟧: x = 0, also (0 | t). Schnitt zweier Geraden: Im Schnittpunkt haben beide ⟦dasselbe x und dasselbe y⟧. Deshalb setzt du die Terme ⟦gleich⟧.',
     'schritte': ['g: y = 2x − 1, h: y = −x + 5', '2x − 1 = −x + 5 → 3x = 6 → x = 2', 'y = 2 · 2 − 1 = 3: ⟦S(2 | 3)⟧'],
     'fehler': 'Der Schnittpunkt mit der x-Achse von y = 2x − 1 ist nicht (0 | −1). Das ist der Schnitt mit der ⟦y-Achse⟧. Für die x-Achse gilt y = 0: x = 0,5.',
     'bild': {'typ': 'koordinaten', 'x': [-1, 5], 'y': [-2, 6], 'graphen': [{'art': 'linear', 'm': 2, 't': -1, 'name': 'g'}, {'art': 'linear', 'm': -1, 't': 5, 'name': 'h'}],
              'punkte': [{'x': 2, 'y': 3, 'name': 'S(2 | 3)'}]},
     '_verbot': ['y = 2x − 1, h']},
    {'lernziel': 'lage', 'titel': 'Parallel oder senkrecht?',
     'regel': 'Gleiche Steigung (m₁ = m₂): Die Geraden sind ⟦parallel⟧. Ist ⟦m₁ · m₂ = −1⟧, stehen sie ⟦senkrecht⟧ aufeinander. Warum? Drehst du das Steigungsdreieck „1 nach rechts, 2 nach oben“ um 90°, wird daraus „2 nach rechts, 1 nach unten“. Die neue Steigung ist −1/2, und 2 · (−1/2) = −1.',
     'schritte': ['g: y = 2x + 1, h: y = −0,5x + 3.', 'm₁ · m₂ = 2 · (−0,5) = −1.', '⟦g und h sind senkrecht zueinander.⟧'],
     'fehler': 'y = 2x + 1 und y = −2x + 1 stehen nicht senkrecht: 2 · (−2) = −4 ≠ −1. Für senkrecht braucht man den ⟦negativen Kehrwert⟧: −1/2.',
     'bild': {'typ': 'koordinaten', 'x': [-2, 4], 'y': [-1, 5], 'streckung': 1.14,
              'graphen': [{'art': 'linear', 'm': 2, 't': 1, 'name': 'g'}, {'art': 'linear', 'm': -0.5, 't': 3, 'name': 'h'}],
              'strecken': [[0, 1, 1, 1, 'gestrichelt'], [1, 1, 1, 3, 'gestrichelt'], [0, 3, 2, 3, 'gestrichelt'], [2, 3, 2, 2, 'gestrichelt']]},
     '_verbot': ['y = −0,5x + 3']},
    {'lernziel': 'deuten', 'titel': 'Lineare Funktionen im Sachzusammenhang',
     'regel': 'In Anwendungen ist ⟦t der Startwert⟧ (bei x = 0) und ⟦m die Änderung pro Einheit⟧ von x. Ein negatives m heißt: Die Größe nimmt ab.',
     'schritte': ['Eine Kerze: h(x) = −1,5x + 20 (h in cm, x in Stunden)', 't = 20: Anfangs ist die Kerze 20 cm hoch. m = −1,5: Pro Stunde wird sie 1,5 cm kürzer.',
                  'Abgebrannt bei h = 0: 1,5x = 20 → ⟦x ≈ 13,3 h⟧'],
     'fehler': 'm = −1,5 heißt nicht, dass die Kerze 1,5 cm hoch ist. m ist eine ⟦Änderung⟧ pro Stunde, keine Höhe.',
     '_verbot': ['Kerze: h(x) = −1,5x + 20']},
]


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'ablesen': {
  'einstieg': 'Eine Taxifahrt kostet 3 € Grundpreis und 2 € pro Kilometer. Trägt man Strecke und Preis in ein Koordinatensystem ein, liegen alle Punkte auf einer geraden Linie. Die 3 € liest man dort ab, wo die Linie die senkrechte Achse trifft; die 2 € pro km zeigen, wie steil sie ist. So eine Zuordnung heißt ⟦lineare Funktion⟧.',
  'woerter': [['lineare Funktion', 'eine Funktion, deren Graph eine Gerade ist: y = m · x + t'], ['m (Steigung)', 'so viel geht es nach oben, wenn man 1 nach rechts geht'],
              ['t (y-Achsenabschnitt)', 'dort schneidet die Gerade die y-Achse – der Startwert'], ['Steigungsdreieck', 'das kleine Dreieck „1 nach rechts, m nach oben“ im Bild'],
              ['(0 | 5)', 'der Punkt mit x = 0 und y = 5']],
  'schritte': ['Gegeben ist y = 5 − 2x. Zuerst umsortieren, damit das x vorne steht: y = −2x + 5.',
               'Die Zahl ohne x ist ⟦t = 5⟧. Die Gerade schneidet die y-Achse also bei (0 | 5).',
               'Die Zahl vor dem x ist ⟦m = −2⟧: Von jedem Punkt aus geht es 1 nach rechts und 2 nach unten. Die Gerade fällt.',
               'Genau das zeigt das gestrichelte Steigungsdreieck im Bild.'],
  'regel': 'So liest du ab: die Gleichung in die Form ⟦y = m · x + t⟧ bringen. ⟦m⟧ ist die Zahl vor dem x (mit Vorzeichen), ⟦t⟧ die Zahl ohne x.',
  'fehler': 'Bei y = 5 − 2x ist m nicht 5. Die Steigung ist die Zahl ⟦vor dem x⟧, mit Vorzeichen: m = −2. Beim Taxi wäre das, als würde man den Grundpreis für den Kilometerpreis halten.'},
 'zwei_punkte': {
  'einstieg': 'Ein Wanderweg steigt gleichmäßig an: Nach 3 km Weg bist du 6 m höher als am Start. Pro Kilometer sind das 6 : 3 = 2 m. Genauso berechnest du die Steigung einer Geraden aus zwei Punkten: Höhenunterschied geteilt durch den Unterschied nach rechts. Das Ergebnis ist die ⟦Steigung m⟧.',
  'woerter': [['P(1 | 3)', 'Punkt P mit x = 1 und y = 3'], ['x₁, y₁ und x₂, y₂', 'die Koordinaten des ersten und des zweiten Punkts (die kleine Zahl ist nur eine Nummer)'],
              ['Differenz', 'Unterschied, das Ergebnis einer Minus-Rechnung'], ['m = (y₂ − y₁) : (x₂ − x₁)', 'Steigung = Unterschied nach oben : Unterschied nach rechts']],
  'schritte': ['Gegeben sind P(1 | 3) und Q(4 | 9).', 'Von P nach Q geht es nach rechts: 4 − 1 = 3.', 'Dabei geht es nach oben: 9 − 3 = 6.',
               'Steigung = nach oben : nach rechts = 6 : 3, also ⟦m = 2⟧.']},
 'proportional': {
  'einstieg': 'Am Obststand kostet 1 kg Äpfel 2,50 €. Kaufst du doppelt so viel, zahlst du doppelt so viel; kaufst du nichts, zahlst du nichts. So eine Zuordnung heißt ⟦direkt proportional⟧. Ihr Graph ist eine Gerade durch den Nullpunkt.',
  'woerter': [['direkt proportional', 'doppelt so viel → doppelt so teuer; 0 kg → 0 €'], ['k (Proportionalitätsfaktor)', 'der Preis für 1 kg – allgemein: y für x = 1'],
              ['Ursprung O', 'der Nullpunkt (0 | 0)'], ['y = 2,5 · x', 'Preis y in € für x kg']],
  'schritte': ['3 kg Äpfel kosten 7,50 €.', 'Preis für 1 kg: 7,50 € : 3 = 2,50 €. Das ist k.', 'Die Funktion heißt also ⟦y = 2,5 · x⟧.', 'Damit kosten 8 kg: 2,5 · 8 = 20 €.'],
  'regel': 'So erkennst du ⟦direkte Proportionalität⟧: Die Gleichung hat die Form y = k · x, der Graph geht durch den ⟦Ursprung⟧. k berechnest du als y : x.'},
 'aufstellen': {
  'einstieg': 'Ein Wanderer kennt die Steigung seines Weges und weiß, an welcher Stelle er gerade steht. Daraus kann er berechnen, auf welcher Höhe der Weg angefangen hat. Bei Geraden ist es genauso: Aus der Steigung m und einem Punkt berechnest du den Startwert t – du ⟦stellst die Geradengleichung auf⟧.',
  'woerter': [['Geradengleichung', 'die Gleichung y = m · x + t mit bestimmten Zahlen für m und t'], ['P(2 | 1)', 'Punkt mit x = 2 und y = 1'],
              ['t = b − m · a', 'Formel für t, wenn der Punkt P(a | b) bekannt ist']],
  'schritte': ['Gegeben: m = 3 und der Punkt P(2 | 1). Gesucht ist t.', 'Setze x = 2 und y = 1 in y = 3x + t ein: 1 = 3 · 2 + t, also 1 = 6 + t.',
               'Auf beiden Seiten 6 abziehen: t = −5.', 'Die Geradengleichung lautet ⟦y = 3x − 5⟧.']},
 'schnittpunkte': {
  'einstieg': 'Zwei Freunde laufen dieselbe Strecke; einer startet früher, der andere läuft schneller. Wann holt der Schnellere den anderen ein? In diesem Moment sind beide zur selben Zeit am selben Ort. Im Koordinatensystem ist das der Punkt, an dem sich ihre Geraden treffen: der ⟦Schnittpunkt⟧.',
  'woerter': [['Schnittpunkt S', 'der Punkt, der auf beiden Geraden liegt'], ['x-Achse / y-Achse', 'die waagrechte / die senkrechte Achse im Koordinatensystem'],
              ['gleichsetzen', 'die beiden Terme für y gleich setzen, weil y im Schnittpunkt gleich ist']],
  'schritte': ['g: y = 2x − 1 und h: y = −x + 5. Im Schnittpunkt haben beide dasselbe y.', 'Deshalb die Terme gleichsetzen: 2x − 1 = −x + 5.',
               'Auf beiden Seiten x und 1 dazuzählen: 3x = 6, also x = 2.', 'x = 2 in g einsetzen: y = 2 · 2 − 1 = 3. Der Schnittpunkt ist ⟦S(2 | 3)⟧.']},
 'lage': {
  'einstieg': 'Bahngleise laufen nebeneinander her und treffen sich nie – sie sind parallel. Eine Straße, die eine andere im rechten Winkel kreuzt, steht senkrecht auf ihr. Ob zwei Geraden parallel oder ⟦senkrecht⟧ sind, kannst du an ihren Steigungen ablesen, ohne zu zeichnen.',
  'woerter': [['parallel', 'gleiche Richtung, kein gemeinsamer Punkt'], ['senkrecht', 'die Geraden kreuzen sich im rechten Winkel (90°)'],
              ['m₁, m₂', 'die Steigungen der ersten und der zweiten Geraden'], ['negativer Kehrwert', 'Bruch umdrehen und Vorzeichen wechseln: von 2 ist es −1/2']],
  'schritte': ['g: y = 2x + 1 hat die Steigung m₁ = 2. h: y = −0,5x + 3 hat die Steigung m₂ = −0,5.', 'Die Steigungen sind verschieden, also sind g und h nicht parallel.',
               'Produkt der Steigungen: 2 · (−0,5) = −1.', 'Das Produkt ist −1, also sind ⟦g und h senkrecht zueinander⟧.']},
 'deuten': {
  'einstieg': 'Eine Kerze ist anfangs 20 cm hoch und wird pro Stunde 1,5 cm kürzer. In der Funktion h(x) = −1,5x + 20 steckt diese ganze Geschichte. Jede Zahl hat eine Bedeutung: Die 20 ist der Anfang, die −1,5 die Änderung pro Stunde. Diese Bedeutung herauszulesen heißt ⟦deuten⟧.',
  'woerter': [['h(x)', 'Höhe der Kerze in cm nach x Stunden'], ['Startwert', 'der Wert am Anfang, also bei x = 0 – hier t = 20'],
              ['Änderung pro Einheit', 'um so viel ändert sich der Wert, wenn x um 1 wächst – hier m = −1,5'], ['≈', '„ungefähr gleich“ (gerundet)']],
  'schritte': ['Kerze: h(x) = −1,5x + 20, h in cm, x in Stunden.', 't = 20 ist der Wert bei x = 0: Anfangs ist die Kerze 20 cm hoch.',
               'm = −1,5 ist die Änderung pro Stunde: Die Kerze wird jede Stunde 1,5 cm kürzer.', 'Abgebrannt ist sie bei h = 0: 1,5x = 20, also ⟦x ≈ 13,3 h⟧.']},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----


def nz(R, lo=-6, hi=6):
    return R.choice([k for k in range(lo, hi + 1) if k])


def zufall_m(R, st):
    if st == 1: return Fr(nz(R, -6, 6))
    if st == 2: return Fr(nz(R, -8, 8), R.choice([1, 1, 2]))
    return Fr(nz(R, -9, 9), R.choice([2, 3, 4, 5]))


def gm(m):
    return float(m) if Fr(m).denominator != 1 else int(m)


def fenster(m, t, xa=-4, xb=4):
    ys = [m * xa + t, m * xb + t, 0, t]
    return [xa, xb], [int(min(ys)) - 1, int(max(ys)) + 1]


def g_ablesen(R, st):
    if R.random() < .4:
        art = R.choice({1: ['term'], 2: ['term', 'dreieck', 'bruch'], 3: ['dreieck', 'bruch']}[st])
        if art == 'term':
            m, t = nz(R, -3, 3), R.randint(-4, 4)
            X, Y = fenster(m, t, -3, 3)
            gr = {'typ': 'koordinaten', 'x': X, 'y': Y, 'graphen': [{'art': 'linear', 'm': m, 't': t}]}
            return mit_bild(L('Gib die Gleichung der gezeichneten Geraden an: y = …', '□x + □', [m, t], [str(m), str(t)],
                              f'Schnitt mit der y-Achse bei (0 | {zt(t)}): t = {zt(t)}. Von dort 1 nach rechts und {zt(abs(m))} nach {"oben" if m > 0 else "unten"}: m = {zt(m)}. y = {lin(m, t)}.',
                              'Lies zuerst t an der y-Achse ab. Dann gehe 1 nach rechts: Wie weit geht es hoch oder runter?', 'Tippe den Term ein, z. B. 2x − 1.'), gr)
        if art == 'dreieck':
            while True:
                x1, y1 = R.randint(-3, 1), R.randint(-3, 3)
                dx = R.choice([1, 2, 3, 4]); dy = nz(R, -6, 6)
                m = Fr(dy, dx)
                if ist_endlich(m) and (m.denominator != 1 or st == 2): break
            x2, y2 = x1 + dx, y1 + dy
            t = y1 - m * x1
            gr = {'typ': 'koordinaten', 'x': [x1 - 2, x2 + 2], 'y': [min(y1, y2) - 2, max(y1, y2) + 2], 'graphen': [{'art': 'linear', 'm': gm(m), 't': gm(t)}],
                  'punkte': [{'x': x1, 'y': y1}, {'x': x2, 'y': y2}], 'strecken': [[x1, y1, x2, y1, 'gestrichelt'], [x2, y1, x2, y2, 'gestrichelt']]}
            return mit_bild(Z('Das Bild zeigt eine Gerade mit Steigungsdreieck. Wie groß ist die Steigung m?', m, f'({dy}) / ({dx})',
                              f'Das Dreieck geht {dx} nach rechts und {abs(dy)} nach {"oben" if dy > 0 else "unten"}: m = {zt(dy)} : {dx} = {zt(m)}.',
                              'Zähle die Kästchen: wie weit nach rechts, wie weit nach oben oder unten? m = hoch : rechts.'), gr)
        t = R.randint(-3, 3); m = Fr(nz(R, -3, 3), 2)
        if m.denominator == 1: m = Fr(1, 2)
        X, Y = fenster(m, t)
        gr = {'typ': 'koordinaten', 'x': X, 'y': Y, 'graphen': [{'art': 'linear', 'm': gm(m), 't': t}], 'punkte': [{'x': 0, 'y': t}, {'x': 2, 'y': gm(t + 2 * m)}]}
        return mit_bild(A(R, 'Welche Gleichung gehört zur gezeichneten Geraden?', f'y = {lin(m, t)}',
                          [f'y = {lin(-m, t)}', f'y = {lin(1 / m, t)}', f'y = {lin(m, -t)}' if t else f'y = {lin(-1 / m, t)}'],
                          f'y-Achsenabschnitt t = {zt(t)}. Von (0 | {zt(t)}) nach (2 | {zt(t + 2 * m)}): 2 nach rechts, {zt(abs(2 * m))} nach {"oben" if m > 0 else "unten"}. m = {zt(2 * m)} : 2 = {zt(m)}.',
                          'Lies t an der y-Achse ab. Für m: Wie weit geht es hoch oder runter, wenn du 2 nach rechts gehst?'), gr)
    m = zufall_m(R, st)
    t = Fr(R.randint(-9, 9)) if st < 3 else Fr(R.randint(-20, 20), R.choice([1, 2]))
    if st == 1:
        G = f'y = {lin(m, t)}'
    elif st == 2:
        G = R.choice([f'y = {zt(t)} {"+" if m > 0 else "−"} {lin(abs(m), 0)}' if t else f'y = {lin(m, 0)}', f'y = {lin(m, t)}'])
    else:
        k = R.choice([2, 3, 4, -2])
        G = f'{zt(k) if k != -1 else "−"}y = {lin(k * m, k * t)}' if (k * m).denominator == 1 and (k * t).denominator == 1 else f'y = {lin(m, t)}'
    if not ist_endlich(m):
        frage = 't'
    else:
        frage = R.choice(['m', 't'])
    if frage == 'm':
        return Z(f'Gib die Steigung m der Geraden {G} an.', m, cz(m),
                 f'In der Form y = m · x + t: y = {lin(m, t)}. Steigung m = {zt(m)}.', 'Bringe die Gleichung in die Form y = m · x + t. m steht vor dem x.')
    return Z(f'Gib den y-Achsenabschnitt t der Geraden {G} an.', t, cz(t),
             f'In der Form y = m · x + t: y = {lin(m, t)}. y-Achsenabschnitt t = {zt(t)}.', 'Bringe die Gleichung in die Form y = m · x + t. t ist die Zahl ohne x.')


ZP = __import__('collections').Counter()


def g_zwei_punkte(R, st):
    arten = {1: ['rechnen', 'rechnen', 'bild'], 2: ['rechnen', 'fehler', 'drei', 'bild'], 3: ['sonder', 'fehler', 'drei', 'rechnen']}[st]
    arten = [a for a in arten if ZP[(st, a)] < 6] or ['rechnen']
    art = R.choice(arten)
    ZP[(st, art)] += 1
    if art == 'sonder':
        x1, y1 = R.randint(-5, 5), R.randint(-5, 5)
        if R.random() < .5:
            x2 = x1 + nz(R, -6, 6)
            return A(R, f'Berechne die Steigung der Geraden durch P({zt(x1)} | {zt(y1)}) und Q({zt(x2)} | {zt(y1)}).', 'm = 0 (waagrechte Gerade)',
                     ['Es gibt keine Steigung.', f'm = {zt(x2 - x1)}', 'm = 1'],
                     f'm = ({zt(y1)} − {kl(y1)}) : ({zt(x2)} − {kl(x1)}) = 0 : {kl(x2 - x1)} = 0. Beide Punkte gleich hoch: waagrecht.',
                     'Was passiert, wenn beide y-Werte gleich sind?')
        y2 = y1 + nz(R, -6, 6)
        return A(R, f'Berechne die Steigung der Geraden durch P({zt(x1)} | {zt(y1)}) und Q({zt(x1)} | {zt(y2)}).',
                 'Es gibt keine Steigung, die Gerade ist senkrecht (keine Funktion).', ['m = 0', f'm = {zt(y2 - y1)}', 'm = 1'],
                 f'x₂ − x₁ = {zt(x1)} − {kl(x1)} = 0. Durch 0 kann man nicht teilen. Die Gerade läuft senkrecht und ist kein Graph einer Funktion.',
                 'Was steht im Nenner, wenn beide x-Werte gleich sind?')
    if art == 'fehler':
        while True:
            x1, x2 = sorted(R.sample(range(-3, 7), 2)); m = Fr(nz(R, -4, 4)); y1 = R.randint(-4, 5); y2 = y1 + m * (x2 - x1)
            if y2 != y1: break
        fehl = R.choice(['nenner', 'tausch'])
        if fehl == 'nenner':
            rech = f'm = ({zt(y2)} − {kl(y1)}) : ({zt(x1)} − {kl(x2)}) = {zt(-m)}'
            ri = f'Im Nenner wurde andersherum subtrahiert; richtig {zt(y2 - y1)} : {zt(x2 - x1)} = {zt(m)}.'
        else:
            rech = f'm = ({zt(x2)} − {kl(x1)}) : ({zt(y2)} − {kl(y1)}) = {zt(1 / m)}'
            ri = f'x und y vertauscht; richtig ({zt(y2)} − {kl(y1)}) : ({zt(x2)} − {kl(x1)}) = {zt(m)}.'
        fa = ['Die Rechnung ist richtig.', f'Es fehlt ein Minus; richtig ist {zt(-m) if fehl == "tausch" else zt(-1 / m) if ist_endlich(-1 / m) else "−1"}.',
              'Man muss die Punkte addieren statt subtrahieren.']
        if not ist_endlich(1 / m) and fehl == 'tausch': return g_zwei_punkte(R, st)
        return A(R, f'Jemand rechnet für P({zt(x1)} | {zt(y1)}), Q({zt(x2)} | {zt(y2)}): {rech}. Was ist falsch?', ri, fa,
                 f'm = (y₂ − y₁) : (x₂ − x₁) = {zt(y2 - y1)} : {zt(x2 - x1)} = {zt(m)}.', 'Rechne selbst m = (y₂ − y₁) : (x₂ − x₁) und vergleiche.')
    if art == 'drei':
        m1 = Fr(nz(R, -3, 3)); xa = R.randint(-3, 0); ya = R.randint(-2, 3)
        xb, xc = xa + 2, xa + 4
        yb = ya + m1 * 2
        auf = R.random() < .5
        m2 = m1 if auf else m1 + R.choice([Fr(-1, 2), Fr(1, 2), Fr(1)])
        yc = yb + m2 * 2
        ri = f'Ja, beide Steigungen sind {zt(m1)}.' if auf else f'Nein, AB hat Steigung {zt(m1)}, BC hat {zt(m2)}.'
        fa = ['Ja, alle Punkte haben verschiedene x-Werte.', f'Nein, AB hat Steigung {zt(m1)}, BC hat {zt(m2 if auf else m1 + 1)}.' if auf else f'Ja, beide Steigungen sind {zt(m1)}.',
              'Das kann man nur mit einer Zeichnung entscheiden.']
        return A(R, f'Liegen A({zt(xa)} | {zt(ya)}), B({zt(xb)} | {zt(yb)}) und C({zt(xc)} | {zt(yc)}) auf einer Geraden?', ri, fa,
                 f'm(AB) = ({zt(yb)} − {kl(ya)}) : 2 = {zt(m1)}; m(BC) = ({zt(yc)} − {kl(yb)}) : 2 = {zt(m2)}. ' + ('Gleich, also eine Gerade.' if auf else 'Verschieden, also keine Gerade.'),
                 'Berechne die Steigung von A nach B und von B nach C.')
    if art == 'bild':
        x1, y1 = R.randint(-3, 0), R.randint(-3, 2)
        dx, dy = R.choice([1, 2, 3]), nz(R, -5, 5)
        x2, y2 = x1 + dx, y1 + dy
        m = Fr(dy, dx)
        if not ist_endlich(m): return g_zwei_punkte(R, st)
        gr = {'typ': 'koordinaten', 'x': [x1 - 2, x2 + 2], 'y': [min(y1, y2) - 2, max(y1, y2) + 2],
              'punkte': [{'x': x1, 'y': y1, 'name': 'P'}, {'x': x2, 'y': y2, 'name': 'Q'}], 'strecken': [[x1, y1, x2, y2]]}
        return mit_bild(Z('Lies die Koordinaten von P und Q ab und berechne die Steigung der Strecke PQ.', m, f'({y2} - ({y1})) / ({x2} - ({x1}))',
                          f'P({zt(x1)} | {zt(y1)}), Q({zt(x2)} | {zt(y2)}). m = ({zt(y2)} − {kl(y1)}) : ({zt(x2)} − {kl(x1)}) = {zt(dy)} : {dx} = {zt(m)}.',
                          'Erst die Punkte ablesen, dann m = (y₂ − y₁) : (x₂ − x₁).'), gr)
    while True:
        x1, x2 = R.sample(range(-6, 9), 2)
        if st == 1: m = Fr(nz(R, -5, 5))
        else: m = Fr(nz(R, -12, 12), R.choice([1, 2, 4, 5]))
        y1 = Fr(R.randint(-8, 8)); y2 = y1 + m * (x2 - x1)
        if st == 3: x1, x2 = Fr(x1, 2), Fr(x2, 2); y2 = y1 + m * (x2 - x1)
        if ist_endlich(m) and ist_endlich(y2) and len(zt(y2)) <= 6: break
    P, Q = f'P({zt(x1)} | {zt(y1)})', f'Q({zt(x2)} | {zt(y2)})'
    return Z(f'Berechne die Steigung der Geraden durch {P} und {Q}.', m, f'({cz(y2)} - ({cz(y1)})) / ({cz(x2)} - ({cz(x1)}))',
             f'm = ({zt(y2)} − {kl(y1)}) : ({zt(x2)} − {kl(x1)}) = {zt(y2 - y1)} : {kl(x2 - x1)} = {zt(m)}.',
             'm = (y₂ − y₁) : (x₂ − x₁). Achte auf negative Zahlen.')


SACH_AUF = [
    ('Eine Kerze ist {t} cm lang und brennt pro Stunde {m} cm ab. Gib die Höhe h(x) nach x Stunden an.', -1, [(20, 2), (24, 3), (15, 1), (30, 2)]),
    ('Ein Handwerker berechnet {t} € Anfahrt und {m} € pro Stunde. Gib die Kosten K(x) für x Stunden an.', 1, [(35, 40), (30, 45), (25, 50), (40, 38)]),
    ('Ein Wassertank enthält {t} Liter. Pro Minute fließen {m} Liter ab. Gib den Inhalt V(x) nach x Minuten an.', -1, [(200, 5), (150, 4), (300, 6)]),
    ('Ein Sparschwein enthält {t} €. Jede Woche kommen {m} € dazu. Gib den Betrag B(x) nach x Wochen an.', 1, [(12, 3), (20, 5), (8, 2)]),
]


def g_aufstellen(R, st):
    h = 'Bestimme m und t und tippe die Gerade als Term ein, z. B. 3x − 5.'
    if st >= 2 and R.random() < .3:
        t_, vz, werte = R.choice(SACH_AUF)
        t0, m0 = R.choice(werte)
        m, t = vz * m0, t0
        return L(t_.format(t=t0, m=m0), '□x + □', [m, t], [str(m), str(t)],
                 f'Startwert (bei x = 0): t = {t}. Änderung pro Einheit: m = {zt(m)} ({"Abnahme" if m < 0 else "Zunahme"}). Term: {lin(m, t)}.',
                 'Was ist der Wert am Anfang (t)? Um wie viel ändert er sich pro Einheit (m)?', 'Tippe den Term ein, z. B. −2x + 20.')
    m, t = nz(R, -5, 5), R.randint(-9, 9)
    if st == 1:
        text = f'Eine Gerade hat die Steigung {zt(m)} und schneidet die y-Achse bei {zt(t)}. Gib den Funktionsterm an.'
        weg = f'm = {zt(m)}, t = {zt(t)}: y = {lin(m, t)}.'
    elif st == 2:
        a = nz(R, -5, 5); b = m * a + t
        text = f'Eine Gerade hat die Steigung {zt(m)} und geht durch P({zt(a)} | {zt(b)}). Gib den Funktionsterm an.'
        weg = f'{zt(b)} = {zt(m)} · {kl(a)} + t → t = {zt(b)} − {kl(m * a)} = {zt(t)}. y = {lin(m, t)}.'
    else:
        a, c = R.sample(range(-5, 7), 2)
        b, d = m * a + t, m * c + t
        text = f'Eine Gerade geht durch P({zt(a)} | {zt(b)}) und Q({zt(c)} | {zt(d)}). Gib den Funktionsterm an.'
        weg = f'm = ({zt(d)} − {kl(b)}) : ({zt(c)} − {kl(a)}) = {zt(m)}. t = {zt(b)} − {kl(m)} · {kl(a)} = {zt(t)}. y = {lin(m, t)}.'
    return L(text, '□x + □', [m, t], [str(m), str(t)], weg, h, 'Tippe den Term ein, z. B. 3x − 5 oder −x + 2.')


def g_proportional(R, st):
    if st == 1:
        ware, einheit, k = R.choice([('Äpfel', 'kg', Fr(5, 2)), ('Kartoffeln', 'kg', Fr(6, 5)), ('Benzin', 'l', Fr(18, 10)), ('Stoff', 'm', Fr(8)),
                                     ('Kirschen', 'kg', Fr(9, 2)), ('Käse', 'kg', Fr(16)), ('Saft', 'l', Fr(3, 2))])
        x1 = R.choice([2, 3, 4, 5, 6]); x2 = R.choice([j for j in (1, 7, 8, 10, 12, 15, 20) if j != x1])
        return Z(f'{x1} {einheit} {ware} kosten {eur(k * x1)} €. Wie viel kosten {x2} {einheit}?', k * x2, f'{cz(k * x1)} / {x1} * {x2}',
                 f'k = {eur(k * x1)} : {x1} = {eur(k)} € pro {einheit}. y = {zt(k)} · {x2} = {eur(k * x2)} €.', 'Berechne zuerst den Preis für 1 Einheit (k).', einheit='€')
    if st == 2:
        k = Fr(nz(R, -9, 9), R.choice([1, 2, 4]))
        a = nz(R, -6, 6); b = k * a
        x2 = R.choice([j for j in range(-8, 13) if j not in (0, a)])
        return Z(f'Die Gerade y = k · x geht durch P({zt(a)} | {zt(b)}). Berechne y für x = {zt(x2)}.', k * x2, f'{cz(b)} / ({a}) * ({x2})',
                 f'k = {zt(b)} : {kl(a)} = {zt(k)}. y = {zt(k)} · {kl(x2)} = {zt(k * x2)}.', 'Berechne zuerst k = y : x.')
    # Stufe 3: Erkennen (mindestens die Hälfte „Nein“)
    art = R.choice(['ja', 'linear', 'nichtlin', 'taxi'])
    if art == 'taxi':
        g, p = R.choice([Fr(9, 2), Fr(4), Fr(7, 2)]), R.choice([Fr(9, 5), Fr(2), Fr(11, 5)])
        km = R.choice([5, 10, 20])
        return A(R, f'Ein Taxi: 0 km → {eur(g)} €, {km} km → {eur(g + p * km)} €. Ist der Preis proportional zur Strecke?', f'Nein, bei 0 km kostet es schon {eur(g)} €.',
                 [f'Ja, y = {zt((g + p * km) / km) if ist_endlich((g + p * km) / km) else zt(p)} · x.', 'Ja, weil der Preis mit der Strecke wächst.', 'Nein, weil der Preis zu hoch ist.'],
                 f'Eine Proportionalität hat bei x = 0 den Wert 0. Hier gibt es einen Grundpreis von {eur(g)} € – die Gerade geht nicht durch den Ursprung.',
                 'Was müsste bei 0 km herauskommen, wenn es proportional wäre?')
    if art == 'nichtlin':
        xs = sorted(R.sample(range(1, 6), 3))
        ps = ', '.join(f'({x} | {x * x})' for x in xs)
        return A(R, f'Ist die Zuordnung {ps} proportional?', 'Nein, die Quotienten y : x sind verschieden.',
                 [f'Ja, y = {xs[0]} · x.', 'Ja, weil y mit x wächst.', 'Nein, die Gerade geht nicht durch den Ursprung.'],
                 'Quotienten: ' + '; '.join(f'{x * x} : {x} = {x}' for x in xs) + '. Verschieden, also nicht proportional (hier gilt y = x²).',
                 'Berechne für jedes Paar den Quotienten y : x.')
    k = Fr(nz(R, 2, 9)); t = 0 if art == 'ja' else nz(R, -5, 5)
    xs = sorted(R.sample(range(1, 10), 3))
    ps = ', '.join(f'({x} | {zt(k * x + t)})' for x in xs)
    if t == 0:
        r, f = f'Ja, y = {zt(k)} · x.', [f'Nein, die Gerade geht nicht durch den Ursprung.', f'Ja, y = {zt(k)} · x + {zt(k)}.', 'Nein, die Quotienten y : x sind verschieden.']
        w = f'Alle Quotienten y : x sind gleich {zt(k)}. Also proportional mit k = {zt(k)}.'
    else:
        r = 'Nein, die Quotienten y : x sind verschieden.'
        f = [f'Ja, y = {zt(k)} · x.', f'Ja, y = {zt(Fr(k * xs[0] + t, xs[0]))} · x.', 'Ja, weil y mit x wächst.']
        w = f'{zt(k * xs[0] + t)} : {xs[0]} = {zt(Fr(k * xs[0] + t, xs[0]))}, aber {zt(k * xs[1] + t)} : {xs[1]} = {zt(Fr(k * xs[1] + t, xs[1]))}. Nicht proportional (es gilt y = {lin(k, t)}).'
    return A(R, f'Ist die Zuordnung {ps} proportional?', r, f, w, 'Berechne für jedes Paar den Quotienten y : x.')


def g_schnittpunkte(R, st):
    if st == 1:
        while True:
            m = Fr(nz(R, -8, 8)); x0 = Fr(R.randint(-10, 10), R.choice([1, 2]))
            t = -m * x0
            if t.denominator == 1 and x0: break
        if R.random() < .4:
            return Z(f'In welchem Punkt schneidet y = {lin(m, t)} die y-Achse? Gib den y-Wert an.', t, cz(t),
                     f'Auf der y-Achse ist x = 0: y = {zt(m)} · 0 {"+" if t >= 0 else "−"} {abs(t)} = {zt(t)}.', 'Auf der y-Achse ist x = 0.')
        return Z(f'Berechne die Nullstelle von y = {lin(m, t)} (Schnitt mit der x-Achse).', x0, f'-({cz(t)}) / {cz(m)}',
                 f'{lin(m, t)} = 0' + (f' → {lin(m, 0)} = {zt(-t)}' if t else '') + (f' → x = {zt(x0)}.' if m != 1 else '.'), 'Auf der x-Achse ist y = 0.')
    while True:
        m1, m2 = Fr(nz(R, -5, 5)), Fr(nz(R, -5, 5))
        if st == 3: m1, m2 = m1 / R.choice([1, 2]), m2 / R.choice([1, 2])
        if m1 == m2: continue
        x = Fr(R.randint(-6, 6)); t1 = Fr(R.randint(-8, 8)); y = m1 * x + t1; t2 = y - m2 * x
        if t2.denominator == 1 and abs(t2) <= 20: break
    g, h = f'g: y = {lin(m1, t1)}', f'h: y = {lin(m2, t2)}'
    weg = (f'{lin(m1, t1)} = {lin(m2, t2)} → {lin(m1 - m2, 0)} = {zt(t2 - t1)}' + ('' if m1 - m2 == 1 else f' → x = {zt(x)}')
           + f'. In g: y = {zt(y)}. S({zt(x)} | {zt(y)}).')
    if y.denominator == 1 and R.random() < .7:
        return L(f'Berechne den Schnittpunkt von {g} und {h}.', 'S(□ | □)', [x, y], [f'({cz(t2)} - ({cz(t1)})) / ({cz(m1)} - ({cz(m2)}))', f'{cz(m1)} * ({cz(x)}) + ({cz(t1)})'],
                 weg, 'Setze die beiden Terme gleich. Mit x berechnest du dann y.', hinweis='Trage x und y des Schnittpunkts ein.')
    if R.random() < .5:
        return Z(f'Berechne den Schnittpunkt S von {g} und {h}. Gib die x-Koordinate an.', x, f'({cz(t2)} - ({cz(t1)})) / ({cz(m1)} - ({cz(m2)}))', weg,
                 'Setze die beiden Terme gleich.')
    return Z(f'Berechne den Schnittpunkt S von {g} und {h}. Gib die y-Koordinate an.', y,
             f'{cz(m1)} * ({cz(t2)} - ({cz(t1)})) / ({cz(m1)} - ({cz(m2)})) + ({cz(t1)})', weg, 'Setze gleich, berechne x und setze x in eine der Gleichungen ein.')


LAGE = ['parallel', 'senkrecht zueinander', 'schneiden sich, aber nicht senkrecht', 'identisch (dieselbe Gerade)']


def g_lage(R, st):
    if (st == 3 and R.random() < .55) or (st == 2 and R.random() < .25):
        m = Fr(nz(R, -6, 6), R.choice([1, 2, 4, 5]))
        if not ist_endlich(-1 / m): m = Fr(nz(R, -5, 5))
        welche = R.choice(['senkrecht', 'parallel'])
        if welche == 'parallel':
            return Z(f'Gib die Steigung einer Geraden an, die parallel zu y = {lin(m, R.randint(-9, 9))} ist.', m, cz(m),
                     f'Parallele Geraden haben dieselbe Steigung: m = {zt(m)}.', 'Parallel heißt: gleiche Steigung.')
        return Z(f'Gib die Steigung einer Geraden an, die senkrecht auf y = {lin(m, R.randint(-9, 9))} steht.', -1 / m, f'-1 / {cz(m)}',
                 f'm₂ = −1 : m₁ = −1 : {kl(m)} = {zt(-1 / m)}. Probe: {zt(m)} · {kl(-1 / m)} = −1.', 'Senkrecht: m₁ · m₂ = −1. Nimm den negativen Kehrwert.')
    art = R.choice(LAGE[:3] + ([LAGE[3]] if st >= 2 else []))
    m1 = Fr(nz(R, -5, 5), R.choice([1, 2])) if st > 1 else Fr(nz(R, -5, 5))
    t1 = R.randint(-6, 6)
    if art == 'parallel': m2, t2 = m1, t1 + nz(R, -5, 5)
    elif art.startswith('senkrecht'): m2, t2 = -1 / m1, R.randint(-6, 6)
    elif art.startswith('identisch'): m2, t2 = m1, t1
    else:
        m2 = R.choice([x for x in (-m1, m1 + 1, 2 * m1, Fr(1) / m1) if x != m1 and x * m1 != -1])
        t2 = R.randint(-6, 6)
    if not ist_endlich(m2): return g_lage(R, st)
    G2 = f'y = {lin(m2, t2)}'
    if art.startswith('identisch'):
        G2 = f'{2}y = {lin(2 * m2, 2 * t2)}' if (2 * m2).denominator == 1 else f'y − {lin(m2, 0)} = {zt(t2)}'
    grund = {'parallel': f'Gleiche Steigung {zt(m1)}, verschiedene y-Achsenabschnitte.', 'senkrecht zueinander': f'Produkt der Steigungen: {zt(m1)} · {kl(m2)} = −1.',
             'schneiden sich, aber nicht senkrecht': f'Verschiedene Steigungen, und {zt(m1)} · {kl(m2)} = {zt(m1 * m2)} ≠ −1.',
             'identisch (dieselbe Gerade)': f'Umgeformt ist die zweite Gleichung y = {lin(m2, t2)} – genau die erste Gerade.'}[art]
    return A(R, f'Wie liegen die Geraden g: y = {lin(m1, t1)} und h: {G2} zueinander?', art, [x for x in LAGE if x != art][:3] if st >= 2 else [x for x in LAGE[:3] if x != art] + [LAGE[3]],
             grund, 'Bringe beide Gleichungen in die Form y = m · x + t und vergleiche die Steigungen.')


def g_deuten(R, st):
    kontext = R.choice(['kerze', 'tank', 'handy', 'taxi', 'pool'])
    if kontext == 'kerze':
        intro = 'Eine Kerze brennt ab:'
        h0, r = R.choice([15, 18, 20, 24, 25, 30]), Fr(R.choice([5, 10, 15, 20, 25, 30]), 10)
        f, x, y = f'h(x) = {lin(-r, h0)}', 'x in Stunden', 'h in cm'
        bed_m, bed_t = f'Die Kerze wird pro Stunde {zt(r)} cm kürzer.', f'Die Kerze ist am Anfang {h0} cm hoch.'
        frage_null, null = 'Nach wie vielen Stunden ist die Kerze abgebrannt?', Fr(h0) / r
        m, t = -r, h0
    elif kontext == 'tank':
        intro = 'Ein Auto fährt, der Tankinhalt sinkt:'
        h0, r = R.choice([40, 45, 50, 60]), Fr(R.choice([5, 6, 8, 10, 15]), 2)
        f, x, y = f'V(x) = {lin(-r, h0)}', 'x in Stunden Fahrt', 'V in Litern'
        bed_m, bed_t = f'Pro Stunde Fahrt werden {zt(r)} Liter verbraucht.', f'Am Anfang sind {h0} Liter im Tank.'
        frage_null, null = 'Nach wie vielen Stunden ist der Tank leer?', Fr(h0) / r
        m, t = -r, h0
    elif kontext == 'handy':
        intro = 'Ein Handytarif:'
        g, p = R.choice([5, 8, 10, 12]), Fr(R.choice([5, 9, 10, 15, 20]), 100)
        f, x, y = f'K(x) = {lin(p, g)}', 'x in Minuten', 'K in €'
        bed_m, bed_t = f'Jede Minute kostet {eur(p)} €.', f'Die Grundgebühr beträgt {g} €.'
        B = g + p * R.choice([20, 40, 50, 60, 100])
        frage_null, null = f'Wie viele Minuten wurde telefoniert, wenn {eur(B)} € zu zahlen sind?', (B - g) / p
        m, t = p, g
    elif kontext == 'taxi':
        intro = 'Eine Taxifahrt:'
        g, p = Fr(R.choice([7, 8, 9]), 2), Fr(R.choice([18, 20, 22, 24, 25]), 10)
        f, x, y = f'P(x) = {lin(p, g)}', 'x in km', 'P in €'
        bed_m, bed_t = f'Jeder Kilometer kostet {eur(p)} €.', f'Der Grundpreis beträgt {eur(g)} €.'
        km = R.choice([4, 5, 8, 10, 12, 15])
        frage_null, null = f'Wie weit ist man gefahren, wenn {eur(g + p * km)} € zu zahlen sind?', Fr(km)
        m, t = p, g
    else:
        intro = 'Ein Planschbecken wird befüllt:'
        h0, r = R.choice([2, 4, 5, 6]), Fr(R.choice([3, 4, 5, 6]), 10)
        f, x, y = f'h(x) = {lin(r, h0)}', 'x in Minuten', 'h in cm'
        bed_m, bed_t = f'Der Wasserstand steigt pro Minute um {zt(r)} cm.', f'Am Anfang steht das Wasser {h0} cm hoch.'
        Ziel = h0 + r * R.choice([20, 30, 40, 50])
        frage_null, null = f'Nach wie vielen Minuten steht das Wasser {zt(Ziel)} cm hoch?', (Ziel - h0) / r
        m, t = r, h0
    if st == 1:
        welche = R.choice(['m', 't'])
        if welche == 'm':
            return A(R, f'{intro} {f} ({x}, {y}). Was bedeutet die Steigung {zt(m)}?', bed_m, [bed_t, f'Nach {zt(abs(m))} Stunden ist der Vorgang vorbei.' if kontext in ('kerze', 'tank') else f'Man muss mindestens {zt(abs(m))} bezahlen.', 'Die Steigung hat hier keine Bedeutung.'],
                     f'm = {zt(m)} ist die Änderung von y, wenn x um 1 wächst. {bed_m}', 'Die Steigung ist die Änderung pro Einheit von x.')
        return A(R, f'{intro} {f} ({x}, {y}). Was bedeutet die Zahl {zt(t)}?', bed_t, [bed_m, 'Es ist der Wert am Ende.', 'Es ist die Nullstelle.'],
                 f't = {zt(t)} ist der Wert für x = 0, also zu Beginn. {bed_t}', 't ist der Wert bei x = 0.')
    if st == 2 or ist_endlich(null) and R.random() < .6:
        if not ist_endlich(null):
            return Z(f'{intro} {f} ({x}, {y}). Berechne den Wert für x = 4.', m * 4 + t, f'{cz(m)} * 4 + {cz(t)}',
                     f'{zt(m)} · 4 + {zt(t)} = {zt(m * 4 + t)}.', 'Setze x = 4 ein.')
        return Z(f'{intro} {f} ({x}, {y}). {frage_null}', null, f'({cz(null * m + t)} - {cz(t)}) / {cz(m)}',
                 f'{lin(m, t)} = {zt(m * null + t)} → {lin(m, 0)} = {zt(m * null)}' + ('' if m == 1 else f' → x = {zt(null)}') + '.',
                 'Setze den Funktionsterm gleich dem gesuchten Wert und löse nach x.')
    if R.random() < .4:
        # Tarifvergleich am Graphen
        while True:
            m1, t1 = R.choice([Fr(2), Fr(5, 2), Fr(3)]), R.choice([2, 3, 4])
            m2 = m1 - R.choice([Fr(1, 2), Fr(1)])
            x0 = R.choice([2, 4, 6, 8])
            t2 = t1 + (m1 - m2) * x0
            if t2.denominator == 1: break
        gr = {'typ': 'koordinaten', 'x': [0, 2 * x0], 'y': [0, int(m1 * 2 * x0 + t1) + 2], 'name_x': 'km', 'name_y': '€',
              'graphen': [{'art': 'linear', 'm': gm(m1), 't': t1, 'name': 'A'}, {'art': 'linear', 'm': gm(m2), 't': gm(t2), 'name': 'B'}]}
        return mit_bild(A(R, f'Zwei Taxi-Tarife: A: y = {lin(m1, t1)}, B: y = {lin(m2, t2)} (x in km, y in €). Ab welcher Strecke ist B billiger?', f'ab mehr als {x0} km',
                          [f'bis {x0} km', f'ab mehr als {zt(t2)} km', 'B ist nie billiger'],
                          f'Die Geraden schneiden sich bei x = {x0} (beide {eur(m1 * x0 + t1)} €). Danach liegt B unter A, weil B flacher ansteigt.',
                          'Suche den Schnittpunkt. Welche Gerade liegt rechts davon tiefer?'), gr)
    aussagen_w = [bed_m, bed_t]
    aussagen_f = [f'Der Graph ist eine Ursprungsgerade.', f'Die Steigung ist {zt(t)}.', f'Für x = 1 ist der Wert {zt(t)}.', f'Der Wert ändert sich pro Einheit von x um {zt(t)}.']
    r_ = R.choice(aussagen_w)
    return A(R, f'{intro} {f} ({x}, {y}). Welche Aussage ist richtig?', r_, R.sample(aussagen_f, 3),
             f'{r_} Denn m = {zt(m)} ist die Änderung pro Einheit, t = {zt(t)} der Anfangswert.', 'Ordne m und t ihre Bedeutung zu.')


GEN = {'ablesen': g_ablesen, 'zwei_punkte': g_zwei_punkte, 'aufstellen': g_aufstellen, 'proportional': g_proportional,
       'schnittpunkte': g_schnittpunkte, 'lage': g_lage, 'deuten': g_deuten}


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

_KO = lambda **k: {'typ': 'koordinaten', **k}
UMBAU = {
 'ablesen': {
  'einstieg': 'Ein Taxi kostet 3 € Grundpreis und 2 € pro Kilometer. Im Koordinatensystem liegen alle Preise auf einer geraden Linie. So eine Zuordnung heißt ⟦lineare Funktion⟧.',
  'woerter': [['lineare Funktion', 'ihr Graph ist eine Gerade: y = m · x + t'], ['m (Steigung)', 'so viel geht es hoch, wenn man 1 nach rechts geht'], ['t (y-Achsenabschnitt)', 'der Startwert: dort trifft die Gerade die y-Achse']],
  'bild': _KO(x=[-1, 5], y=[0, 14], graphen=[{'art': 'linear', 'm': 2, 't': 3, 'name': 'Taxi'}], name_x='km', name_y='€', schritt_y=2),
  'schritte': [{'text': 'Preis = 3 + 2x. Umsortiert, mit x vorne: y = 2x + 3.'},
               {'text': 'Die Zahl ohne x ist ⟦t = 3⟧: der Grundpreis bei 0 km.', 'bild': {'punkte': [{'x': 0, 'y': 3, 'name': '(0 | 3)'}]}},
               {'text': 'Die Zahl vor x ist ⟦m = 2⟧: 1 km weiter, 2 € mehr.', 'bild': {'strecken': [[1, 5, 2, 5, 'gestrichelt'], [2, 5, 2, 7, 'gestrichelt']]}}],
  'fehler': 'Bei y = 5 − 2x ist m nicht 5. Die Steigung ist die Zahl ⟦vor dem x⟧, mit Vorzeichen: −2. Die Gerade fällt.',
  'fehler_bild': {'graphen': [{'art': 'linear', 'm': -2, 't': 5, 'name': '5 − 2x'}], 'punkte': [{'x': 0, 'y': 5, 'name': 't = 5'}], 'strecken': [[1, 3, 2, 3, 'gestrichelt'], [2, 3, 2, 1, 'gestrichelt']]},
  'regel': '⟦m⟧ steht vor dem x, ⟦t⟧ steht allein. Vorher in die Form y = m · x + t bringen und das Vorzeichen mitnehmen.'},
 'zwei_punkte': {
  'einstieg': 'Ein Wanderweg steigt gleichmäßig. Von Kilometer 1 bis Kilometer 4 gewinnst du 6 m Höhe. Höhenunterschied geteilt durch Wegunterschied ist die ⟦Steigung⟧.',
  'woerter': [['Steigung', 'Höhenunterschied : Unterschied nach rechts'], ['P(1 | 3)', 'Punkt bei x = 1 und y = 3']],
  'bild': _KO(x=[-1, 6], y=[-1, 11], graphen=[{'art': 'linear', 'm': 2, 't': 1}], punkte=[{'x': 1, 'y': 3, 'name': 'P'}, {'x': 4, 'y': 9, 'name': 'Q'}]),
  'schritte': [{'text': 'Die Punkte sind P(1 | 3) und Q(4 | 9).'},
               {'text': 'Nach rechts: 4 − 1 = 3.', 'bild': {'strecken': [[1, 3, 4, 3, 'gestrichelt']]}},
               {'text': 'Nach oben: 9 − 3 = 6.', 'bild': {'strecken': [[1, 3, 4, 3, 'gestrichelt'], [4, 3, 4, 9, 'gestrichelt']]}},
               {'text': 'Steigung: 6 : 3, also ⟦m = 2⟧.'}],
  'fehler': 'm = 3 : 6 = 0,5 ist falsch. Der Höhenunterschied kommt ⟦nach oben⟧ in den Bruch, die Strecke nach rechts nach unten.',
  'regel': 'Steigung = ⟦nach oben : nach rechts⟧. Mit zwei Punkten: m = (y₂ − y₁) : (x₂ − x₁).'},
 'proportional': {
  'einstieg': 'Am Obststand kostet 1 kg Äpfel 2,50 €. Doppelt so viel kostet doppelt so viel, nichts kostet nichts. So eine Zuordnung heißt ⟦direkt proportional⟧.',
  'woerter': [['direkt proportional', 'doppelt so viel → doppelt so teuer, 0 → 0'], ['k', 'der Preis für 1 kg, allgemein y : x'], ['Ursprung O', 'der Nullpunkt (0 | 0)']],
  'bild': _KO(x=[0, 4], y=[0, 10], graphen=[{'art': 'linear', 'm': 2.5, 't': 0, 'name': '2,5x'}], punkte=[{'x': 0, 'y': 0, 'name': 'O'}], name_x='kg', name_y='€'),
  'schritte': [{'text': '3 kg kosten 7,50 €.', 'bild': {'punkte': [{'x': 0, 'y': 0, 'name': 'O'}, {'x': 3, 'y': 7.5, 'name': '(3 | 7,5)'}]}},
               {'text': 'Preis für 1 kg: 7,50 € : 3 = 2,50 €. Das ist k.', 'bild': {'punkte': [{'x': 0, 'y': 0, 'name': 'O'}, {'x': 1, 'y': 2.5, 'name': '(1 | 2,5)'}, {'x': 3, 'y': 7.5, 'name': '(3 | 7,5)'}]}},
               {'text': 'Die Funktion heißt ⟦y = 2,5 · x⟧. Sie geht durch den Ursprung O.'}],
  'fehler': 'y = 2x + 1 ist ⟦nicht⟧ proportional: Bei 0 kg müsstest du 1 € zahlen. Die Gerade verfehlt den Ursprung.',
  'fehler_bild': {'graphen': [{'art': 'linear', 'm': 2.5, 't': 0, 'name': '2,5x'}, {'art': 'linear', 'm': 2, 't': 1, 'name': '2x + 1'}], 'punkte': [{'x': 0, 'y': 0, 'name': 'O'}, {'x': 0, 'y': 1, 'name': '1 €?'}]},
  'regel': 'Proportional heißt ⟦y = k · x⟧, Gerade durch den Ursprung. k berechnest du als y : x.'},
 'aufstellen': {
  'einstieg': 'Du kennst die Steigung eines Weges und einen Punkt, an dem du gerade bist. Daraus berechnest du, wo der Weg beginnt. So stellst du die ⟦Geradengleichung⟧ auf.',
  'woerter': [['Geradengleichung', 'y = m · x + t mit festen Zahlen für m und t']],
  'bild': _KO(x=[-1, 4], y=[-6, 6], punkte=[{'x': 2, 'y': 1, 'name': 'P(2 | 1)'}]),
  'schritte': [{'text': 'Gegeben: m = 3 und P(2 | 1). Gesucht ist t.'},
               {'text': 'P einsetzen: 1 = 3 · 2 + t, also 1 = 6 + t.'},
               {'text': '6 abziehen: ⟦t = −5⟧.', 'bild': {'punkte': [{'x': 2, 'y': 1, 'name': 'P(2 | 1)'}, {'x': 0, 'y': -5, 'name': '(0 | −5)'}]}},
               {'text': 'Die Geradengleichung lautet y = 3x − 5.', 'bild': {'graphen': [{'art': 'linear', 'm': 3, 't': -5}]}}],
  'fehler': 'Bei P(2 | 1) ist x = 2 und y = 1, nicht umgekehrt. Vertauscht kommt ⟦t = −1⟧ heraus – die Gerade verfehlt P.',
  'fehler_bild': {'graphen': [{'art': 'linear', 'm': 3, 't': -1, 'name': 'falsch'}], 'punkte': [{'x': 2, 'y': 1, 'name': 'P'}]},
  'regel': 'Setze den Punkt ein und ⟦löse nach t auf⟧. Bei zwei Punkten berechnest du zuerst m.'},
 'schnittpunkte': {
  'einstieg': 'Zwei Freunde laufen dieselbe Strecke, einer startet früher, der andere ist schneller. Beim Einholen sind beide zur selben Zeit am selben Ort. Im Bild ist das der ⟦Schnittpunkt⟧.',
  'woerter': [['Schnittpunkt', 'der Punkt, der auf beiden Geraden liegt'], ['gleichsetzen', 'die beiden Terme für y gleich setzen']],
  'bild': _KO(x=[-1, 5], y=[-2, 6], graphen=[{'art': 'linear', 'm': 2, 't': -1, 'name': 'g'}, {'art': 'linear', 'm': -1, 't': 5, 'name': 'h'}]),
  'schritte': [{'text': 'g: y = 2x − 1 und h: y = −x + 5.'},
               {'text': 'Im Schnittpunkt ist y gleich, also gleichsetzen: 2x − 1 = −x + 5.'},
               {'text': 'x und 1 dazuzählen: 3x = 6, also x = 2.'},
               {'text': 'In g: y = 2 · 2 − 1 = 3. ⟦S(2 | 3)⟧', 'bild': {'punkte': [{'x': 2, 'y': 3, 'name': 'S(2 | 3)'}]}}],
  'fehler': '(0 | −1) ist der Schnitt mit der ⟦y-Achse⟧, nicht mit der x-Achse. Für die x-Achse setzt du y = 0: x = 0,5.',
  'fehler_bild': {'punkte': [{'x': 0, 'y': -1, 'name': 'y-Achse'}, {'x': 0.5, 'y': 0, 'name': 'x-Achse'}]},
  'regel': 'Für den Schnittpunkt ⟦setzt du die Terme gleich⟧. Mit der x-Achse: y = 0. Mit der y-Achse: x = 0.'},
 'lage': {
  'einstieg': 'Bahngleise treffen sich nie, sie sind parallel. Eine Straße, die eine andere im rechten Winkel kreuzt, steht ⟦senkrecht⟧ auf ihr. Das erkennst du an den Steigungen.',
  'woerter': [['parallel', 'gleich steil, ohne Schnittpunkt'], ['senkrecht', 'im rechten Winkel, wie ein Kreuz'], ['m₁', 'die Steigung der ersten Geraden; m₂ die der zweiten']],
  'bild': _KO(x=[-2, 4], y=[-1, 5], streckung=1.14, graphen=[{'art': 'linear', 'm': 2, 't': 1, 'name': 'g'}, {'art': 'linear', 'm': -0.5, 't': 3, 'name': 'h'}]),
  'schritte': [{'text': 'g: y = 2x + 1 hat die Steigung m₁ = 2.', 'bild': {'strecken': [[0, 1, 1, 1, 'gestrichelt'], [1, 1, 1, 3, 'gestrichelt']]}},
               {'text': 'h: y = −0,5x + 3 hat m₂ = −0,5.', 'bild': {'strecken': [[0, 1, 1, 1, 'gestrichelt'], [1, 1, 1, 3, 'gestrichelt'], [0, 3, 2, 3, 'gestrichelt'], [2, 3, 2, 2, 'gestrichelt']]}},
               {'text': 'Verschiedene Steigungen: nicht parallel. Produkt: 2 · (−0,5) = −1.'},
               {'text': 'Produkt −1 heißt: ⟦g und h stehen senkrecht⟧.'}],
  'fehler': 'y = 2x + 1 und y = −2x + 1 sind nicht senkrecht: 2 · (−2) = −4. Nötig ist der ⟦negative Kehrwert⟧ −1/2.',
  'fehler_bild': {'graphen': [{'art': 'linear', 'm': 2, 't': 1, 'name': 'g'}, {'art': 'linear', 'm': -2, 't': 1, 'name': 'nicht ⊥'}], 'strecken': []},
  'regel': 'Gleiche Steigung: ⟦parallel⟧. Produkt der Steigungen −1: ⟦senkrecht⟧.'},
 'deuten': {
  'einstieg': 'Eine Kerze ist anfangs 20 cm hoch und wird pro Stunde 1,5 cm kürzer. Jede Zahl der Funktion erzählt davon. Diese Bedeutung herauszulesen heißt ⟦deuten⟧.',
  'woerter': [['deuten', 'sagen, was eine Zahl in der Geschichte bedeutet'], ['h(x)', 'die Höhe der Kerze nach x Stunden'], ['≈', '„ungefähr gleich“']],
  'bild': _KO(x=[0, 15], y=[0, 22], graphen=[{'art': 'linear', 'm': -1.5, 't': 20, 'name': 'Kerze', 'bereich': [0, 13.4]}], name_x='h', name_y='cm', schritt_y=5),
  'schritte': [{'text': 'Die Funktion ist h(x) = −1,5x + 20.'},
               {'text': 't = 20 ist der Start: 20 cm bei x = 0.', 'bild': {'punkte': [{'x': 0, 'y': 20, 'name': 'Start'}]}},
               {'text': 'm = −1,5: Jede Stunde wird sie 1,5 cm kürzer.', 'bild': {'strecken': [[2, 17, 3, 17, 'gestrichelt'], [3, 17, 3, 15.5, 'gestrichelt']]}},
               {'text': 'Abgebrannt bei h = 0: 1,5x = 20, also ⟦x ≈ 13,3 h⟧.', 'bild': {'punkte': [{'x': 0, 'y': 20, 'name': 'Start'}, {'x': 13.33, 'y': 0, 'name': 'leer'}]}}],
  'fehler': 'm = −1,5 heißt nicht, dass die Kerze 1,5 cm hoch ist. m ist eine ⟦Änderung⟧ pro Stunde, keine Höhe.',
  'regel': '⟦t ist der Start, m die Änderung⟧ pro Einheit. Ein negatives m heißt: Die Größe nimmt ab.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Steigung und Achsenabschnitt', ['ablesen', 'zwei_punkte', 'proportional']), ('Geraden bestimmen', ['aufstellen', 'schnittpunkte', 'lage']),
          ('Anwenden', ['deuten'])],
         'Lineare Funktionen y = m · x + t deuten, Geradengleichungen aufstellen, Schnittpunkte und Lage von Geraden bestimmen.',
         ['m = Steigung (Änderung pro 1 nach rechts), t = y-Achsenabschnitt.', 'm = (y₂ − y₁) : (x₂ − x₁).',
          'Parallel: m₁ = m₂. Senkrecht: m₁ · m₂ = −1.', 'Proportional: y = k · x, Gerade durch den Ursprung.'],
         offen=['Graphen selbst zeichnen lassen (Kind zeichnet die Gerade) kann die App noch nicht; Ablesen am Graphen und Steigungsdreieck sind jetzt eingebaut.'])
