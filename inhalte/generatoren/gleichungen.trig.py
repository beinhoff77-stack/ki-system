#!/usr/bin/env python3
"""Thema gleichungen.trig – Trigonometrische Gleichungen (Klasse 9), Lösungen im Bereich 0° ≤ x < 360°."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(913)
B = 'im Bereich 0° ≤ x < 360°'
SIN = {Fr(0): [0, 180], Fr(1, 2): [30, 150], Fr(1): [90], Fr(-1, 2): [210, 330], Fr(-1): [270]}
COS = {Fr(1): [0], Fr(1, 2): [60, 300], Fr(0): [90, 270], Fr(-1, 2): [120, 240], Fr(-1): [180]}
TAN = {Fr(0): [0, 180], Fr(1): [45, 225], Fr(-1): [135, 315]}
TAB = {'sin': SIN, 'cos': COS, 'tan': TAN}


def loes(f, v):
    """alle Lösungen in [0°, 360°) für allgemeines v (Gleitkomma)"""
    if f == 'sin':
        if abs(v) > 1: return []
        x = asin(v)
        l = [x, 180 - x] if x >= 0 else [180 - x, 360 + x]
    elif f == 'cos':
        if abs(v) > 1: return []
        x = acos(v)
        l = [x, 360 - x]
    else:
        x = atan(v)
        if x < 0: x += 180
        l = [x, x + 180]
    out = []
    for t in l:
        t = t % 360
        if all(abs(t - u) > 1e-9 for u in out): out.append(t)
    return sorted(out)


def f1(x):
    return format(float(x), '.1f').replace('-', '−').replace('.', ',')


def schab(n):
    return 'x = □°' if n == 1 else 'x₁ = □°; x₂ = □°'


ETAPPEN = [
    {'lernziel': 'sinus', 'titel': 'Gleichungen sin x = v',
     'regel': 'sin x ist die ⟦y-Koordinate⟧ am Einheitskreis. Für −1 < v < 1 gibt es zwei Lösungen: x₁ = sin⁻¹(v) und ⟦x₂ = 180° − x₁⟧ (bei negativem v auf den Bereich 0°–360° umrechnen).',
     'schritte': ['sin x = 0,5: Taschenrechner liefert x₁ = 30°.', 'Zweite Lösung: 180° − 30° = 150°. Also ⟦x₁ = 30°, x₂ = 150°⟧.'],
     'probe': 'sin 150° = sin 30° = 0,5 ✓',
     'bild': {'typ': 'koordinaten', 'x': [0, 360], 'y': [-1.5, 1.5], 'grad': True, 'schritt_x': 30, 'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0, 'd': 0, 'name': 'sin x'}], 'waagrecht': [0.5], 'punkte': [{'x': 30, 'y': 0.5, 'name': '30°'}, {'x': 150, 'y': 0.5, 'name': '150°'}]},
     'fehler': 'Nur x = 30° anzugeben ist unvollständig: Die Gerade y = 0,5 schneidet den Einheitskreis ⟦zweimal⟧, auch bei 150°.'},
    {'lernziel': 'kosinus', 'titel': 'Gleichungen cos x = v',
     'regel': 'cos x ist die ⟦x-Koordinate⟧ am Einheitskreis. Für −1 < v < 1: x₁ = cos⁻¹(v) liegt zwischen 0° und 180°, die zweite Lösung ist ⟦x₂ = 360° − x₁⟧.',
     'schritte': ['cos x = −0,5: Taschenrechner liefert x₁ = 120°.', 'x₂ = 360° − 120° = 240°. Also ⟦x₁ = 120°, x₂ = 240°⟧.'],
     'probe': 'cos 240° = −0,5 ✓',
     'bild': {'typ': 'koordinaten', 'x': [0, 360], 'y': [-1.5, 1.5], 'grad': True, 'schritt_x': 30, 'graphen': [{'art': 'cos', 'a': 1, 'b': 1, 'c': 0, 'd': 0, 'name': 'cos x'}], 'waagrecht': [-0.5], 'senkrecht': [180], 'punkte': [{'x': 120, 'y': -0.5, 'name': '120°'}, {'x': 240, 'y': -0.5, 'name': '240°'}]},
     'fehler': 'x₂ = 180° − 120° = 60° ist falsch: cos 60° = +0,5. Beim Kosinus spiegelt man an der ⟦x-Achse⟧: x₂ = 360° − x₁.'},
    {'lernziel': 'tangens', 'titel': 'Gleichungen tan x = v',
     'regel': 'Der Tangens wiederholt sich alle ⟦180°⟧. Zu jedem Wert v gibt es im Bereich 0°–360° ⟦genau zwei⟧ Lösungen: x₁ und ⟦x₂ = x₁ + 180°⟧ (x = 90° und 270° sind ausgeschlossen).',
     'schritte': ['tan x = 1: x₁ = tan⁻¹(1) = 45°.', 'x₂ = 45° + 180° = 225°. Also ⟦x₁ = 45°, x₂ = 225°⟧.'],
     'probe': 'tan 225° = sin 225° : cos 225° = (−0,707) : (−0,707) = 1 ✓',
     'fehler': 'Bei tan x = −1 die Lösung −45° anzugeben liegt nicht im Bereich: Erst +180° rechnen: ⟦135°⟧ und 315°.'},
    {'lernziel': 'anzahl', 'titel': 'Wie viele Lösungen gibt es?',
     'regel': 'sin x und cos x liegen immer zwischen ⟦−1 und 1⟧: Für |v| > 1 gibt es ⟦keine⟧ Lösung, für v = ±1 genau ⟦eine⟧ im Bereich 0°–360°, sonst zwei. tan x = v hat immer zwei Lösungen.',
     'schritte': ['cos x = −1: Nur der Punkt (−1 | 0) am Einheitskreis hat x-Koordinate −1.', 'Genau eine Lösung: ⟦x = 180°⟧.'],
     'probe': 'cos 180° = −1 ✓',
     'bild': {'typ': 'koordinaten', 'x': [0, 360], 'y': [-1.5, 2.5], 'grad': True, 'schritt_x': 30, 'graphen': [{'art': 'cos', 'a': 1, 'b': 1, 'c': 0, 'd': 0, 'name': 'cos x'}], 'waagrecht': [-1, 2], 'punkte': [{'x': 180, 'y': -1, 'name': '180°'}]},
     'fehler': '„sin x = 1,2 hat die Lösung sin⁻¹(1,2)“ ist falsch: Der Taschenrechner meldet einen Fehler, weil ⟦sin x nie größer als 1⟧ ist. Keine Lösung.'},
    {'lernziel': 'umformen', 'titel': 'Erst umformen, dann lösen',
     'regel': 'Forme wie bei linearen Gleichungen um, bis ⟦sin x, cos x oder tan x allein⟧ steht. Gilt sin x = cos x, teilst du durch cos x: ⟦tan x = 1⟧.',
     'schritte': ['4 sin x + 1 = 3 ⇔ 4 sin x = 2 ⇔ sin x = 0,5.', 'x₁ = 30°, x₂ = 150°: ⟦L = {30°; 150°}⟧.'],
     'probe': '4 · 0,5 + 1 = 3 ✓',
     'fehler': '4 sin x = 2 ⇒ sin x = 2 − 4 ist falsch: 4 ist ein ⟦Faktor⟧, also teilen: sin x = 0,5.'},
    {'lernziel': 'anwendung', 'titel': 'Trigonometrische Gleichungen anwenden',
     'regel': 'In Anwendungen erst die Gleichung aufstellen, dann ⟦alle⟧ Lösungen bestimmen und im ⟦Sachzusammenhang⟧ prüfen (z. B. Winkelsumme im Dreieck unter 180°).',
     'schritte': ['Im Dreieck gilt sin β = 0,5 und α = 40°. Mögliche Winkel: 30° oder 150°.', '40° + 150° = 190° > 180°, also nur ⟦β = 30°⟧.'],
     'probe': '40° + 30° + 110° = 180° ✓',
     'fehler': 'Bei sin β = 0,5 im Dreieck beide Winkel 30° und 150° ungeprüft anzugeben ist falsch: Die ⟦Winkelsumme⟧ entscheidet, welcher passt.'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'sinus': {
  'einstieg': 'Ein Riesenrad hat den Radius 1 (in Zehnermetern). Eine Gondel startet rechts auf Höhe der Radmitte und dreht sich gegen den Uhrzeigersinn. Ihre Höhe über der Mitte ist der Sinus des Drehwinkels. Wann ist sie 0,5 über der Mitte? Das fragt eine ⟦trigonometrische Gleichung⟧.',
  'woerter': [['trigonometrische Gleichung', 'eine Gleichung, in der x in sin x, cos x oder tan x steckt'],
              ['x', 'hier ein Winkel in Grad zwischen 0° und 360°'],
              ['sin⁻¹', 'die Umkehrtaste: Sie liefert aus einem Sinuswert einen Winkel'],
              ['x₁, x₂', 'die erste und die zweite Lösung'],
              ['v', 'der vorgegebene Wert, hier 0,5']],
  'bild': {'typ': 'koordinaten', 'x': [0, 360], 'y': [-1.5, 1.5], 'grad': True, 'schritt_x': 30, 'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0, 'd': 0, 'name': 'Höhe y = sin x'}], 'waagrecht': [0.5], 'punkte': [{'x': 30, 'y': 0.5, 'name': 'x₁ = 30° (aufwärts)'}, {'x': 150, 'y': 0.5, 'name': 'x₂ = 150° (abwärts)'}]},
  'schritte': ['Die Gleichung heißt sin x = 0,5.',
               'Der Taschenrechner liefert mit sin⁻¹ den ersten Winkel: x₁ = 30°. Die Gondel fährt dort aufwärts.',
               'Auf dem Rückweg nach unten erreicht sie dieselbe Höhe noch einmal, spiegelbildlich: x₂ = 180° − 30° = 150°.',
               'Also ⟦x₁ = 30°, x₂ = 150°⟧.'],
  'regel': 'So löst du sin x = v: sin x ist die ⟦y-Koordinate⟧ am Einheitskreis. Für −1 < v < 1 gibt es zwei Lösungen: x₁ = sin⁻¹(v) und ⟦x₂ = 180° − x₁⟧. Ist v negativ, rechnest du die Winkel in den Bereich 0° bis 360° um.',
  'fehler': 'Nur x = 30° anzugeben ist unvollständig: Die Gondel ist zweimal auf dieser Höhe. Die Gerade y = 0,5 schneidet die Kurve ⟦zweimal⟧, auch bei 150°.'},
 'kosinus': {
  'einstieg': 'Jetzt interessiert der seitliche Abstand der Gondel von der Radachse: rechts positiv, links negativ. Dieser Abstand ist der Kosinus des Drehwinkels. Wann ist die Gondel 0,5 links von der Achse? Das fragt eine ⟦Kosinus-Gleichung⟧.',
  'woerter': [['cos x', 'der waagrechte Abstand der Gondel von der Achse (x-Koordinate)'],
              ['cos⁻¹', 'die Umkehrtaste zum Kosinus; sie liefert Winkel zwischen 0° und 180°'],
              ['360° − x₁', 'der an der x-Achse gespiegelte Winkel']],
  'bild': {'typ': 'koordinaten', 'x': [0, 360], 'y': [-1.5, 1.5], 'grad': True, 'schritt_x': 30, 'graphen': [{'art': 'cos', 'a': 1, 'b': 1, 'c': 0, 'd': 0, 'name': 'Abstand y = cos x'}], 'waagrecht': [-0.5], 'senkrecht': [180], 'punkte': [{'x': 120, 'y': -0.5, 'name': 'x₁ = 120° (oben links)'}, {'x': 240, 'y': -0.5, 'name': 'x₂ = 240° (unten links)'}]},
  'schritte': ['Die Gleichung heißt cos x = −0,5.',
               'Der Taschenrechner liefert mit cos⁻¹ den ersten Winkel: x₁ = 120°. Die Gondel ist dort oben links.',
               'Unten links hat sie denselben Abstand, gespiegelt an der x-Achse: x₂ = 360° − 120° = 240°.',
               'Also ⟦x₁ = 120°, x₂ = 240°⟧.'],
  'regel': 'So löst du cos x = v: cos x ist die ⟦x-Koordinate⟧ am Einheitskreis. Für −1 < v < 1 liegt x₁ = cos⁻¹(v) zwischen 0° und 180°, die zweite Lösung ist ⟦x₂ = 360° − x₁⟧.',
  'fehler': 'x₂ = 180° − 120° = 60° ist falsch: Bei 60° ist die Gondel rechts, cos 60° = +0,5. Beim Kosinus spiegelt man an der ⟦x-Achse⟧: x₂ = 360° − x₁.'},
 'tangens': {
  'einstieg': 'Vom Mittelpunkt des Rads aus gesehen: Wie steil zeigt die Speiche zur Gondel? Diese Steigung ist der Tangens des Drehwinkels. Eine Speiche nach rechts oben und die gegenüberliegende nach links unten liegen auf einer Linie, haben also dieselbe Steigung. Das zeigt jede ⟦Tangens-Gleichung⟧.',
  'woerter': [['tan x', 'sin x : cos x, die Steigung der Speiche'],
              ['tan⁻¹', 'die Umkehrtaste zum Tangens; sie liefert Winkel zwischen −90° und 90°'],
              ['x₁ + 180°', 'die gegenüberliegende Speiche, eine halbe Drehung weiter'],
              ['ausgeschlossen', 'bei 90° und 270° ist cos x = 0, der Tangens existiert dort nicht']],
  'schritte': ['Die Gleichung heißt tan x = 1.',
               'Der Taschenrechner liefert mit tan⁻¹ den ersten Winkel: x₁ = 45°.',
               'Eine halbe Drehung weiter liegt die gegenüberliegende Speiche mit derselben Steigung: x₂ = 45° + 180° = 225°.',
               'Also ⟦x₁ = 45°, x₂ = 225°⟧.'],
  'regel': 'So löst du tan x = v: Der Tangens wiederholt sich alle ⟦180°⟧. Zu jedem Wert v gibt es im Bereich 0° bis 360° ⟦genau zwei⟧ Lösungen: x₁ und ⟦x₂ = x₁ + 180°⟧. Die Winkel 90° und 270° sind ausgeschlossen.',
  'fehler': 'Bei tan x = −1 die Lösung −45° anzugeben liegt nicht im Bereich 0° bis 360°: Erst +180° rechnen: ⟦135°⟧, dann noch einmal: 315°.'},
 'anzahl': {
  'einstieg': 'Die Gondel kommt nie höher als 1 über die Mitte und nie weiter als 1 zur Seite. Ganz links ist sie nur in einem einzigen Moment. Bevor man rechnet, lohnt deshalb die Frage nach der ⟦Anzahl der Lösungen⟧.',
  'woerter': [['|v| > 1', 'v ist größer als 1 oder kleiner als −1'],
              ['v = ±1', 'v ist genau 1 oder genau −1'],
              ['Bereich 0°–360°', 'eine volle Umdrehung']],
  'bild': {'typ': 'koordinaten', 'x': [0, 360], 'y': [-1.5, 2.5], 'grad': True, 'schritt_x': 30, 'graphen': [{'art': 'cos', 'a': 1, 'b': 1, 'c': 0, 'd': 0, 'name': 'y = cos x'}], 'waagrecht': [-1, 2], 'punkte': [{'x': 180, 'y': -1, 'name': 'nur x = 180°'}]},
  'schritte': ['Die Gleichung heißt cos x = −1. Gesucht ist die Stellung ganz links.',
               'Am Einheitskreis hat nur der Punkt (−1 | 0) die x-Koordinate −1.',
               'Im Bild berührt die Linie y = −1 die Kurve nur an ihrem tiefsten Punkt.',
               'Also genau eine Lösung: ⟦x = 180°⟧.'],
  'regel': 'So bestimmst du die Anzahl: sin x und cos x liegen immer zwischen ⟦−1 und 1⟧. Für |v| > 1 gibt es ⟦keine⟧ Lösung, für v = ±1 genau ⟦eine⟧ im Bereich 0° bis 360°, sonst zwei. tan x = v hat dort immer zwei Lösungen.',
  'fehler': '„sin x = 1,2 hat die Lösung sin⁻¹(1,2)“ ist falsch: So hoch kommt die Gondel nie, der Taschenrechner meldet einen Fehler. ⟦sin x ist nie größer als 1⟧, es gibt keine Lösung.'},
 'umformen': {
  'einstieg': 'Manchmal steckt der Sinus in einer längeren Rechnung, zum Beispiel bei einer Gondel auf einem Turm: viermal die Höhe plus 1 ergibt 3. Dann holt man zuerst den Sinus allein heraus und löst erst danach. Das heißt ⟦erst umformen, dann lösen⟧.',
  'woerter': [['umformen', 'auf beiden Seiten dasselbe rechnen, damit die Gleichung wahr bleibt'],
              ['Faktor', 'eine Zahl, mit der malgenommen wird, z. B. die 4 in 4 sin x'],
              ['⇔', '„ist gleichwertig mit“: beide Gleichungen haben dieselben Lösungen'],
              ['L = {30°; 150°}', 'die Lösungsmenge']],
  'schritte': ['Die Gleichung heißt 4 sin x + 1 = 3.',
               'Auf beiden Seiten 1 abziehen: 4 sin x = 2.',
               'Beide Seiten durch 4 teilen: sin x = 0,5.',
               'Wie beim Riesenrad: x₁ = 30°, x₂ = 150°. Also ⟦L = {30°; 150°}⟧.'],
  'regel': 'So gehst du vor: Forme wie bei linearen Gleichungen um, bis ⟦sin x, cos x oder tan x allein⟧ steht. Dann wie gewohnt lösen. Gilt sin x = cos x, teilst du durch cos x und erhältst ⟦tan x = 1⟧.',
  'fehler': '4 sin x = 2 ⇒ sin x = 2 − 4 ist falsch: 4 ist ein ⟦Faktor⟧, also teilen: sin x = 0,5.'},
 'anwendung': {
  'einstieg': 'In einer Dreiecksaufgabe kommt sin β = 0,5 heraus. Die Gleichung hat zwei Lösungen, aber ein Dreieck hat nur Platz für Winkel, die zusammen 180° ergeben. Also muss man jede Lösung an der Situation prüfen. So wendet man ⟦trigonometrische Gleichungen⟧ an.',
  'woerter': [['Winkelsumme', 'alle drei Winkel im Dreieck ergeben zusammen 180°'],
              ['Sachzusammenhang', 'die Situation, zu der die Lösung passen muss'],
              ['α, β, γ', 'die drei Winkel des Dreiecks']],
  'schritte': ['Im Dreieck ist α = 40° und sin β = 0,5.',
               'Die Gleichung sin β = 0,5 hat zwei Lösungen: β = 30° oder β = 150°.',
               'Prüfen mit der Winkelsumme: 40° + 150° = 190°. Das ist schon mehr als 180°, für γ bleibt nichts.',
               'Also passt nur ⟦β = 30°⟧. Dann ist γ = 180° − 40° − 30° = 110°.'],
  'regel': 'So wendest du sie an: Gleichung aufstellen, ⟦alle⟧ Lösungen bestimmen und jede im ⟦Sachzusammenhang⟧ prüfen – im Dreieck etwa, ob die Winkelsumme unter 180° bleibt.',
  'fehler': 'Bei sin β = 0,5 im Dreieck beide Winkel 30° und 150° ungeprüft anzugeben ist falsch: Die ⟦Winkelsumme⟧ entscheidet, welcher passt.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
def _k(art, **z):
    b = {'typ': 'koordinaten', 'x': [0, 360], 'y': [-1.5, 1.5], 'grad': True, 'schritt_x': 30,
         'graphen': [{'art': art, 'a': 1, 'b': 1, 'c': 0, 'd': 0, 'name': f'{art} x'}]}
    b.update(z); return b
P = lambda x, y, n, offen=False: {'x': x, 'y': y, 'name': n, **({'offen': True} if offen else {})}
UMBAU = {
 'sinus': {
  'einstieg': 'Eine Riesenradgondel dreht sich. Ihre Höhe über der Achse ist der Sinus des Drehwinkels. Wann ist sie 0,5 über der Achse? Das fragt eine ⟦trigonometrische Gleichung⟧.',
  'woerter': [['trigonometrische Gleichung', 'eine Gleichung mit sin x, cos x oder tan x'],
              ['sin⁻¹', 'die Umkehrtaste: Sie macht aus einem Sinuswert einen Winkel']],
  'bild': _k('sin', waagrecht=[0.5]),
  'schritte': [{'text': 'Die Gleichung heißt sin x = 0,5.'},
               {'text': 'sin⁻¹(0,5) liefert x₁ = 30°: Die Gondel fährt aufwärts.', 'bild': {'punkte': [P(30, 0.5, '30°')]}},
               {'text': 'Abwärts ist sie gleich hoch bei x₂ = 180° − 30° = 150°.', 'bild': {'punkte': [P(30, 0.5, '30°'), P(150, 0.5, '150°')]}},
               {'text': 'Also ⟦x₁ = 30°, x₂ = 150°⟧.'}],
  'fehler': 'Nur 30° ist unvollständig. Die Gondel ist zweimal auf dieser Höhe, auch bei 150°.',
  'fehler_bild': {'punkte': [P(30, 0.5, '30°'), P(150, 0.5, '150° vergessen', True)]},
  'regel': 'sin x = v hat ⟦zwei Lösungen⟧: x₁ und 180° − x₁. Den Winkel x₁ liefert sin⁻¹(v).'},
 'kosinus': {
  'einstieg': 'Der seitliche Abstand der Gondel von der Achse ist der Kosinus: rechts plus, links minus. Wann ist sie 0,5 links? Das fragt eine ⟦Kosinus-Gleichung⟧.',
  'woerter': [['cos⁻¹', 'die Umkehrtaste zum Kosinus; sie liefert Winkel bis 180°'],
              ['360° − x₁', 'der an der x-Achse gespiegelte Winkel']],
  'bild': _k('cos', waagrecht=[-0.5]),
  'schritte': [{'text': 'Die Gleichung heißt cos x = −0,5.'},
               {'text': 'cos⁻¹(−0,5) liefert x₁ = 120°: Die Gondel ist links oben.', 'bild': {'punkte': [P(120, -0.5, '120°')]}},
               {'text': 'Links unten ist sie gleich weit weg: x₂ = 360° − x₁ = 240°.',
                'bild': {'punkte': [P(120, -0.5, '120°'), P(240, -0.5, '240°')]}},
               {'text': 'Also ⟦x₁ = 120°, x₂ = 240°⟧.'}],
  'fehler': 'x₂ = 180° − 120° = 60° ist falsch. Bei 60° ist die Gondel rechts: cos 60° = +0,5.',
  'fehler_bild': {'punkte': [P(120, -0.5, '120°'), P(240, -0.5, '240°'), P(60, 0.5, '60°?', True)]},
  'regel': 'cos x = v: ⟦x₂ = 360° − x₁⟧. Den Winkel x₁ liefert cos⁻¹(v).'},
 'tangens': {
  'einstieg': 'Von der Radmitte zeigt jede Speiche schräg nach außen. Gegenüberliegende Speichen haben dieselbe Steigung. Deshalb wiederholt sich der ⟦Tangens⟧ alle 180°.',
  'woerter': [['tan x', 'sin x : cos x, die Steigung der Speiche'],
              ['tan⁻¹', 'die Umkehrtaste zum Tangens']],
  'bild': _k('tan', y=[-3, 3], schritt_x=45, waagrecht=[1], senkrecht=[90, 270]),
  'schritte': [{'text': 'Die Gleichung heißt tan x = 1.'},
               {'text': 'tan⁻¹(1) liefert x₁ = 45°.', 'bild': {'punkte': [P(45, 1, '45°')]}},
               {'text': 'Die Gegenspeiche eine halbe Drehung weiter: x₂ = 45° + 180° = 225°.',
                'bild': {'punkte': [P(45, 1, '45°'), P(225, 1, '225°')]}},
               {'text': 'Also ⟦x₁ = 45°, x₂ = 225°⟧.'}],
  'fehler': 'Bei tan x = −1 liegt −45° nicht zwischen 0° und 360°. Plus 180° ergibt 135°, dann 315°.',
  'regel': 'tan x = v: ⟦x₂ = x₁ + 180°⟧. Bei 90° und 270° gibt es keinen Tangens.'},
 'anzahl': {
  'einstieg': 'Die Gondel ist höchstens 1 über der Achse und höchstens 1 daneben. Ganz links ist sie nur einen Moment. Darum klärst du zuerst die ⟦Anzahl der Lösungen⟧.',
  'woerter': [['v = ±1', 'v ist genau 1 oder genau −1'],
              ['|v| > 1', 'v ist größer als 1 oder kleiner als −1']],
  'bild': _k('cos', y=[-1.5, 2.5]),
  'schritte': [{'text': 'Die Gleichung heißt cos x = −1. Gesucht ist die Stellung ganz links.'},
               {'text': 'Die Linie y = −1 berührt die Kurve nur einmal.', 'bild': {'waagrecht': [-1], 'punkte': [P(180, -1, '180°')]}},
               {'text': 'Bei v = ±1 gibt es genau eine Lösung: ⟦x = 180°⟧.'},
               {'text': 'Bei |v| > 1 gibt es keine Lösung, etwa bei cos x = 2.', 'bild': {'waagrecht': [-1, 2]}}],
  'fehler': 'sin x = 1,2 hat keine Lösung. So hoch kommt die Gondel nie, der Taschenrechner meldet einen Fehler.',
  'fehler_bild': {'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0, 'd': 0, 'name': 'sin x'}], 'waagrecht': [1.2], 'punkte': []},
  'regel': '|v| > 1: keine, v = ±1: ⟦eine⟧, sonst zwei Lösungen. tan x = v hat immer zwei.'},
 'umformen': {
  'einstieg': 'Die Gondel hängt an einem Turm: Viermal ihre Höhe plus 1 ergibt 3. Erst holst du den Sinus heraus, dann löst du. Das heißt ⟦umformen⟧.',
  'woerter': [['umformen', 'auf beiden Seiten dasselbe rechnen'],
              ['Faktor', 'eine Zahl, mit der malgenommen wird, hier die 4']],
  'bild': _k('sin'),
  'schritte': [{'text': 'Die Gleichung heißt 4 sin x + 1 = 3.'},
               {'text': 'Minus 1 auf beiden Seiten: 4 sin x = 2.'},
               {'text': 'Die 4 ist ein Faktor. Durch 4 teilen: sin x = 0,5.', 'bild': {'waagrecht': [0.5]}},
               {'text': 'Wie beim Riesenrad: ⟦L = {30°; 150°}⟧.', 'bild': {'punkte': [P(30, 0.5, '30°'), P(150, 0.5, '150°')]}}],
  'fehler': '4 sin x = 2 heißt nicht sin x = 2 − 4. Die 4 ist ein Faktor, also teilen: sin x = 0,5.',
  'regel': 'Forme um, bis ⟦sin x allein⟧ steht. Dann löst du wie gewohnt.'},
 'anwendung': {
  'einstieg': 'In einer Dreiecksaufgabe kommt sin β = 0,5 heraus. Zwei Winkel passen dazu. Aber im Dreieck ist nur Platz für 180°: Du ⟦prüfst die Lösungen⟧.',
  'woerter': [['Winkelsumme', 'die drei Winkel im Dreieck ergeben zusammen 180°'],
              ['Sachzusammenhang', 'die Situation, zu der die Lösung passen muss']],
  'bild': {'typ': 'tabelle', 'kopf': ['β', 'α + β', 'passt?'], 'zeilen': [['30°', '?', '?'], ['150°', '?', '?']]},
  'schritte': [{'text': 'Im Dreieck ist α = 40° und sin β = 0,5.'},
               {'text': 'Mögliche Winkel: β = 30° oder β = 150°.'},
               {'text': 'Winkelsumme: 40° + 150° = 190°, das ist zu viel.',
                'bild': {'zeilen': [['30°', '70°', '?'], ['150°', '190°', 'nein']]}},
               {'text': 'Im Sachzusammenhang passt nur ⟦β = 30°⟧. Dann ist γ = 110°.',
                'bild': {'zeilen': [['30°', '70°', 'ja'], ['150°', '190°', 'nein']]}}],
  'fehler': 'Beide Winkel ungeprüft anzugeben ist falsch. Die Winkelsumme 180° entscheidet, welcher passt.',
  'regel': 'Alle Lösungen bestimmen, dann ⟦im Sachzusammenhang prüfen⟧.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def g_exakt(f, s):
    v = R.choice(list(TAB[f]))
    l = TAB[f][v]
    if s == 1 and len(l) == 1: return None
    return luecken(f'Löse {f} x = {dz(v)} {B}.', schab(len(l)), 'kleinere Lösung zuerst' if len(l) > 1 else 'die Lösung', l,
                   f'Besondere Werte am Einheitskreis: {f} x = {dz(v)} für ' + ' und '.join(f'{t}°' for t in l) + '.',
                   'Nutze die besonderen Werte (0°, 30°, 45°, 60°, 90°) und die Symmetrie am Einheitskreis.', c=[str(t) for t in l])


def g_allg(f, s, welche, vz=0):
    v = Fr(R.randint(-95, 95), 100) if f != 'tan' else Fr(R.randint(-500, 500), 100)
    if vz and v * vz <= 0: return None
    if v == 0 or v in TAB[f] or abs(v) == 1: return None
    l = loes(f, float(v))
    if len(l) != 2: return None
    i = 0 if welche == 'kleinere' else 1
    wahr = l[i]
    w_ = gerundet(wahr, 1)
    if w_ is None: return None
    andere = gerundet(l[1 - i], 1)
    if andere is None: return None
    return zahl(f'Löse {f} x = {dz(v)} {B}. Gib die {welche} Lösung auf eine Nachkommastelle an.',
                f'{f}⁻¹({dz(v)}) ≈ {f1(round({"sin": asin, "cos": acos, "tan": atan}[f](float(v)), 1))}°; Lösungen ≈ {f1(gerundet(l[0], 1))}° und {f1(gerundet(l[1], 1))}°. {welche.capitalize()}: {f1(w_)}°.',
                {'sin': 'Zweite Lösung über 180° − x₁; negative Werte in den Bereich bis 360° verschieben.',
                 'cos': 'Zweite Lösung über 360° − x₁.', 'tan': 'Zweite Lösung über x₁ + 180°.'}[f],
                w_, f'round({K(wahr)}, 1)', einheit='°')


def g_zweite(f):
    a = R.randint(5, 85) if f != 'cos' else R.randint(5, 175)
    if f == 'cos' and a == 90: return None
    v = {'sin': sin, 'cos': cos, 'tan': tan}[f](a)
    z = {'sin': 180 - a, 'cos': 360 - a, 'tan': a + 180}[f]
    regel = {'sin': f'180° − {a}°', 'cos': f'360° − {a}°', 'tan': f'{a}° + 180°'}[f]
    return zahl(f'Eine Lösung von {f} x ≈ {dz(round(v, 4))} {B} ist x₁ = {a}°. Bestimme die zweite Lösung.',
                f'Beim {"Sinus" if f == "sin" else "Kosinus" if f == "cos" else "Tangens"} gilt x₂ = {regel} = {z}°.',
                {'sin': 'Spiegle am Einheitskreis an der y-Achse.', 'cos': 'Spiegle am Einheitskreis an der x-Achse.', 'tan': 'Der Tangens wiederholt sich alle 180°.'}[f],
                z, {'sin': f'180 - {a}', 'cos': f'360 - {a}', 'tan': f'{a} + 180'}[f], einheit='°')


def g_negativ_beide(f):
    v = -Fr(R.randint(5, 95), 100)
    l = loes(f, float(v))
    r = [gerundet(t, 0) for t in l]
    if None in r or len(r) != 2: return None
    x1 = {'sin': asin, 'cos': acos}[f](float(v))
    regel = (f'sin⁻¹({dz(v)}) ≈ {f1(round(x1, 1))}° liegt nicht im Bereich. 180° + {f1(round(-x1, 1))}° ≈ {r[0]}° und 360° − {f1(round(-x1, 1))}° ≈ {r[1]}°.'
             if f == 'sin' else f'cos⁻¹({dz(v)}) ≈ {f1(round(x1, 1))}°; zweite Lösung 360° − {f1(round(x1, 1))}° ≈ {r[1]}°.')
    return luecken(f'Löse {f} x = {dz(v)} {B}. Runde auf ganze Grad.', 'x₁ ≈ □°; x₂ ≈ □°', 'kleinere Lösung zuerst', r, regel,
                   'Negativer Sinus: Der Punkt liegt unterhalb der x-Achse (3. und 4. Quadrant).' if f == 'sin' else 'Die zweite Lösung ist 360° − x₁.',
                   c=[f'round({K(l[0])}, 0)', f'round({K(l[1])}, 0)'])


def g_sinus(s):
    if s == 1: return g_exakt('sin', s) if R.random() < 0.3 else g_zweite('sin')
    if s == 2: return g_allg('sin', s, R.choice(['kleinere', 'größere']), vz=1) if R.random() < 0.6 else g_exakt('sin', s)
    if R.random() < 0.6: return g_negativ_beide('sin')
    if R.random() < 0.5:
        w = R.choice([30, 10, 20, 40, 50])
        v = -sin(w)
        vt = dz(round(v, 2)) if w != 30 else '−0,5'
        return auswahl(f'Jemand löst sin x = {vt} {B} so: x₁ = −{w}°, x₂ = 180° − (−{w}°) = {180 + w}°. Was ist falsch?',
                       f'−{w}° liegt nicht im Bereich; richtig ist 360° − {w}° = {360 - w}°, also {180 + w}° und {360 - w}°.',
                       ['Nichts, beide Lösungen stimmen.', f'Die zweite Lösung muss 180° − {w}° = {180 - w}° heißen.', f'Richtig wären {w}° und {180 - w}°.'],
                       f'Der Taschenrechner liefert −{w}°. Im Bereich 0° bis 360° entspricht das {360 - w}°. Zusammen mit {180 + w}° sind das die beiden Lösungen.',
                       'Liegen beide Angaben im Bereich 0° bis 360°?')
    v = Fr(R.randint(10, 90), 100)
    x1 = asin(float(v))
    a, b = gerundet(x1, 1), gerundet(180 - x1, 1)
    c_ = gerundet(360 - x1, 1)
    if None in (a, b, c_): return None
    return auswahl(f'Jemand gibt für sin x = {dz(v)} {B} die Lösungen {f1(a)}° und {f1(c_)}° an. Was stimmt?',
                   f'Falsch: Das ist die Regel für den Kosinus; richtig sind {f1(a)}° und {f1(b)}°.',
                   ['Richtig.', f'Falsch: richtig sind {f1(a)}° und {f1(a + 180)}°.', 'Falsch: Es gibt nur eine Lösung.'],
                   f'Beim Sinus spiegelt man an der y-Achse: x₂ = 180° − x₁ ≈ {f1(b)}°. Probe: sin {f1(c_)}° ist negativ.',
                   'Mache für die zweite Angabe die Probe am Einheitskreis.')


def g_kosinus(s):
    if s == 1: return g_exakt('cos', s) if R.random() < 0.3 else g_zweite('cos')
    if s == 2:
        typ = R.random()
        if typ < 0.35:
            v = Fr(R.randint(-90, 90), 100)
            if v == 0 or abs(v) == Fr(1, 2): return None
            x1 = acos(float(v))
            r = [gerundet(t, 1) for t in (x1, 360 - x1, 180 - x1, x1 + 180)]
            if None in r: return None
            return auswahl(f'cos x = {dz(v)} hat die Lösung x₁ ≈ {f1(r[0])}°. Welche ist die zweite Lösung {B}?', f'{f1(r[1])}°',
                           [f'{f1(r[2])}°', f'{f1(r[3])}°', f'−{f1(r[0])}°'],
                           f'Beim Kosinus spiegelt man an der x-Achse: x₂ = 360° − x₁ ≈ {f1(r[1])}°. (180° − x₁ wäre die Sinus-Regel, x₁ + 180° die Tangens-Regel.)',
                           'Welche Spiegelung am Einheitskreis lässt die x-Koordinate gleich?')
        return g_allg('cos', s, R.choice(['kleinere', 'größere'])) if typ < 0.7 else g_exakt('cos', s)
    return g_negativ_beide('cos') if R.random() < 0.5 else g_allg('cos', s, R.choice(['kleinere', 'größere']), vz=-1)


def g_tangens(s):
    if s == 1: return g_exakt('tan', s) if R.random() < 0.3 else g_zweite('tan')
    if s == 2: return g_exakt('tan', s) if R.random() < 0.4 else g_allg('tan', s, R.choice(['kleinere', 'größere']))
    typ = R.random()
    if typ < 0.35:
        if R.random() < 0.5:
            L, h = R.choice([(12, Fr(3, 2)), (10, 1), (20, 3), (8, Fr(1, 2)), (15, 2), (25, 4), (16, Fr(5, 2))])
            wahr = atan(float(h / L))
            v = gerundet(wahr, 1)
            if v is None: return None
            return zahl(f'Eine Rampe steigt auf {L} m waagrechter Länge um {dz(h)} m. Unter welchem Winkel steigt sie? Runde auf eine Nachkommastelle.',
                        f'tan α = {dz(h)} : {L} = {dz(h / L)} ⇒ α = tan⁻¹({dz(h / L)}) ≈ {f1(v)}°.', 'Höhe : waagrechte Länge ist der Tangens des Steigungswinkels.',
                        v, f'round({K(wahr)}, 1)', einheit='°')
        p_ = R.choice([6, 8, 12, 15, 18, 22, 25])
        wahr = atan(p_ / 100)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Ein Weg hat {p_} % Steigung. Wie groß ist der Steigungswinkel? Runde auf eine Nachkommastelle.',
                    f'tan α = {dz(Fr(p_, 100))} ⇒ α ≈ {f1(v)}°.', '{p} % Steigung heißt tan α = {p}/100.'.format(p=p_), v, f'round({K(wahr)}, 1)', einheit='°')
    if typ < 0.5:
        v = R.choice([20, 25, 40, 50, 100])
        return auswahl(f'tan x = {v} hat im Bereich 0° bis 90° eine Lösung nahe bei 90°. Warum?', 'Weil tan x für x nahe 90° beliebig groß wird.',
                       ['Weil der Taschenrechner auf 90° rundet.', f'Weil {v} : 90 fast 1 ist.', 'Weil tan 90° = 1 ist.'],
                       'tan x = sin x : cos x. Für x → 90° geht cos x gegen 0, der Quotient wird riesig. Große Tangenswerte gehören zu Winkeln nahe 90°.',
                       'Was passiert mit cos x, wenn x sich 90° nähert?')
    return g_allg('tan', s, R.choice(['kleinere', 'größere']), vz=-1)


def g_anzahl(s):
    f = R.choice(['sin', 'cos', 'tan'])
    if s == 1:
        v = R.choice([Fr(R.randint(12, 30), 10), Fr(-R.randint(12, 30), 10), Fr(R.randint(2, 8), 10), Fr(-R.randint(2, 8), 10)])
    else:
        v = R.choice([Fr(R.randint(11, 30), 10) * R.choice([1, -1]), Fr(R.randint(1, 99), 100) * R.choice([1, -1]), Fr(1), Fr(-1), Fr(0)])
    if f == 'tan': n = 2
    elif abs(v) > 1: n = 0
    elif abs(v) == 1: n = 1
    else: n = 2
    txt = {0: 'keine Lösung', 1: 'genau eine Lösung', 2: 'zwei Lösungen'}
    if s < 3:
        grund = ('tan x nimmt jeden Wert an, mit Periode 180°: zwei Lösungen.' if f == 'tan' else
                 f'|{dz(v)}| > 1, aber {f} x liegt zwischen −1 und 1: keine Lösung.' if n == 0 else
                 f'{f} x = {dz(v)} nur an einem Punkt des Einheitskreises: eine Lösung.' if n == 1 else
                 f'Die Gerade y = {dz(v)} schneidet den Graphen im Bereich zweimal: zwei Lösungen.')
        a_ = auswahl(f'Wie viele Lösungen hat {f} x = {dz(v)} {B}?', txt[n], list(txt.values()), grund,
                     'Liegt der Wert zwischen −1 und 1? Ist er genau ±1? Beim Tangens ist alles erlaubt.')
        if f != 'tan' and s == 2 and R.random() < 0.5 and abs(v) <= 2:
            a_['f']['text'] = f'Im Bild siehst du den Graphen von y = {f} x und die Gerade y = {dz(v)}. Wie viele Lösungen hat {f} x = {dz(v)} {B}?'
            bild(a_, {'typ': 'koordinaten', 'x': [0, 360], 'y': [-2.5, 2.5], 'grad': True, 'schritt_x': 90,
                      'graphen': [{'art': f, 'a': 1, 'b': 1, 'c': 0, 'd': 0, 'name': f'{f} x'}], 'waagrecht': [wert(v)]})
        return a_
    typ = R.random()
    if typ < 0.35:
        v = Fr(R.randint(11, 19), 10)
        g = R.choice(['sin', 'cos'])
        x_ = gerundet(({'sin': asin, 'cos': acos}[g])(float(v - 1)), 1)
        return auswahl(f'Jemand löst {g} x = {dz(v)}, bekommt am Taschenrechner eine Fehlermeldung und rechnet stattdessen {g}⁻¹({dz(v - 1)}) ≈ {f1(x_)}°. Was stimmt?',
                       f'Falsch: {g} x ≤ 1, die Gleichung hat keine Lösung.',
                       [f'Richtig, {dz(v)} − 1 = {dz(v - 1)}.', f'Falsch: x ≈ {f1(360 - x_ if g == "cos" else 180 - x_)}°.', 'Falsch: Es gibt unendlich viele Lösungen.'],
                       f'Die Fehlermeldung ist richtig: Am Einheitskreis sind Sinus und Kosinus Koordinaten, also höchstens 1. {dz(v)} > 1 ist unmöglich.',
                       'Welche Werte kann sin x bzw. cos x annehmen?')
    if typ < 0.7:
        if R.random() < 0.5:
            k = R.randint(2, 5)
            return auswahl(f'Für welche Werte von a hat {k} sin x = a {B} genau eine Lösung?', f'a = {k} oder a = −{k}',
                           ['a = 1 oder a = −1', 'a = 0', f'für alle a mit −{k} < a < {k}'],
                           f'sin x = a/{k} hat genau eine Lösung, wenn a/{k} = 1 oder a/{k} = −1, also a = ±{k} (x = 90° bzw. 270°).',
                           f'Teile durch {k}. Wann hat sin x = Wert genau eine Lösung?')
        k, d = R.randint(2, 5), R.randint(1, 6)
        return auswahl(f'{k} cos x + {d} = b hat {B} keine Lösung, wenn …', f'b > {k + d} oder b < {d - k}',
                       [f'b > {k} oder b < −{k}', f'b > 1 oder b < −1', f'{d - k} < b < {k + d}'],
                       f'{k} cos x + {d} liegt zwischen {k} · (−1) + {d} = {d - k} und {k} · 1 + {d} = {k + d}. Außerhalb davon gibt es keine Lösung.',
                       'Welche Werte kann der linke Term annehmen, wenn cos x zwischen −1 und 1 liegt?')
    v = R.choice([Fr(1), Fr(-1)])
    g = R.choice(['sin', 'cos'])
    l = TAB[g][v]
    zweite = (l[0] + 180) % 360
    return auswahl(f'Jemand gibt für {g} x = {dz(v)} {B} die Lösungen {l[0]}° und {zweite}° an. Was stimmt?',
                   f'Falsch: Es gibt nur die Lösung {l[0]}°.',
                   ['Richtig.', 'Falsch: Es gibt keine Lösung.', f'Falsch: Nur {zweite}° ist Lösung.'],
                   f'{g} {zweite}° = {dz(-v)} ≠ {dz(v)}. Der Wert {dz(v)} ist ein Extremwert; nur ein Punkt am Einheitskreis hat diese Koordinate: x = {l[0]}°.',
                   'Setze beide Winkel zur Probe ein.')


ZAEHL = {}
TEXTE = set()


def frei(l, text):
    """Jede Lösungsmenge höchstens zweimal je Lernkarte (gezählt über verschiedene Aufgabentexte)."""
    if text in TEXTE: return True
    if ZAEHL.get(tuple(l), 0) >= 2: return False
    ZAEHL[tuple(l)] = ZAEHL.get(tuple(l), 0) + 1
    TEXTE.add(text)
    return True


def g_umformen(s):
    if s == 3:
        typ = R.random()
        if typ < 0.4:
            f = R.choice(['sin', 'cos'])
            v = R.choice([x for x in TAB[f] if len(TAB[f][x]) == 2 and x != 0])
            l = TAB[f][v]
            k = R.randint(2, 6)
            m = R.randint(1, k - 1)
            d = R.randint(-6, 6)
            # (k) f x + d = m f x + e  ⇒ (k − m) f x = e − d
            e = (k - m) * v + d
            if e.denominator != 1: return None
            lt = f'{k} {f} x' + (f' {plus(d)}' if d else '')
            rt = (f'{m} {f} x' if m > 1 else f'{f} x') + (f' {plus(e)}' if e else '')
            if not frei(l, lt + rt): return None
            return luecken(f'Löse {lt} = {rt} {B}.', schab(2), 'kleinere Lösung zuerst', l,
                           f'{f} x auf eine Seite: {k - m} {f} x = {dz(e - d)} ⇒ {f} x = {dz(v)} ⇒ ' + ' und '.join(f'{u}°' for u in l) + '.',
                           f'Bringe alle {f}-x-Glieder auf eine Seite wie bei einer linearen Gleichung.', c=[str(u) for u in l])
        if typ < 0.7:
            if R.random() < 0.5:
                k = R.choice([4, 2])
                if k == 4:
                    return luecken(f'Löse 4 (sin x)² = 1 {B}.', 'x₁ = □°; x₂ = □°; x₃ = □°; x₄ = □°', 'aufsteigend', [30, 150, 210, 330],
                                   '(sin x)² = 0,25 ⇒ sin x = 0,5 oder sin x = −0,5 ⇒ 30°, 150°, 210°, 330°.',
                                   'Ziehe die Wurzel: Denke an beide Vorzeichen.', c=['30', '150', '210', '330'])
                return luecken(f'Löse 2 (cos x)² = 0,5 {B}.', 'x₁ = □°; x₂ = □°; x₃ = □°; x₄ = □°', 'aufsteigend', [60, 120, 240, 300],
                               '(cos x)² = 0,25 ⇒ cos x = ±0,5 ⇒ 60°, 120°, 240°, 300°.', 'Ziehe die Wurzel: Denke an beide Vorzeichen.', c=['60', '120', '240', '300'])
            if R.random() < 0.5:
                if not frei([0, 180], 'cos²'): return None
                return luecken(f'Löse (cos x)² = 1 {B}.', schab(2), 'kleinere Lösung zuerst', [0, 180],
                               'cos x = 1 oder cos x = −1 ⇒ x = 0° oder x = 180°.', 'Ziehe die Wurzel: Denke an beide Vorzeichen.', c=['0', '180'])
            if not frei([90, 270], 'sin²'): return None
            return luecken(f'Löse (sin x)² = 1 {B}.', schab(2), 'kleinere Lösung zuerst', [90, 270],
                           'sin x = 1 oder sin x = −1 ⇒ x = 90° oder x = 270°.', 'Ziehe die Wurzel: Denke an beide Vorzeichen.', c=['90', '270'])
        k = R.choice([1, -1])
        f_ = R.choice([1, 2, 3])
        if k == 1:
            t = 'sin x = cos x' if f_ == 1 else f'{f_} sin x = {f_} cos x'
            if not frei([45, 225], t): return None
            return luecken(f'Löse {t} {B}.', schab(2), 'kleinere Lösung zuerst', [45, 225],
                           'Durch cos x teilen (cos x ≠ 0): tan x = 1 ⇒ x₁ = 45°, x₂ = 225°.', 'Teile beide Seiten durch cos x.', c=['45', '45 + 180'])
        t = 'sin x = −cos x' if f_ == 1 else f'{f_} sin x + {f_} cos x = 0'
        if not frei([135, 315], t): return None
        return luecken(f'Löse {t} {B}.', schab(2), 'kleinere Lösung zuerst', [135, 315],
                       'Umformen zu sin x = −cos x, durch cos x teilen: tan x = −1 ⇒ x₁ = 135°, x₂ = 315°.', 'Teile beide Seiten durch cos x.', c=['180 - 45', '360 - 45'])
    if s == 2 and R.random() < 0.45:
        f = R.choice(['sin', 'cos'])
        a, b = R.randint(2, 8), R.randint(-6, 6)
        v = Fr(R.randint(-9, 9), 10)
        if v == 0 or abs(v) == Fr(1, 2): return None
        rechts = a * v + b
        l = loes(f, float(v))
        r = [gerundet(t, 0) for t in l]
        if None in r or len(r) != 2: return None
        t = f'Löse {a} {f} x {plus(b) if b else ""}'.rstrip() + f' = {dz(rechts)} {B}. Runde auf ganze Grad.'
        if not frei(r, t): return None
        return luecken(t, 'x₁ ≈ □°; x₂ ≈ □°', 'kleinere Lösung zuerst', r,
                       f'{a} {f} x = {dz(rechts - b)} ⇒ {f} x = {dz(v)} ⇒ x ≈ {r[0]}° und x ≈ {r[1]}°.',
                       'Erst nach ' + f + ' x umstellen, dann mit dem Taschenrechner beide Lösungen bestimmen.', c=[f'round({K(l[0])}, 0)', f'round({K(l[1])}, 0)'])
    f = R.choice(['sin', 'cos'] if s == 1 else ['sin', 'cos', 'tan'])
    v = R.choice([x for x in TAB[f] if (s > 1 or len(TAB[f][x]) == 2)])
    l = TAB[f][v]
    a = R.randint(2, 6)
    b = R.randint(-9, 9)
    if s == 1:
        b = 0
    rechts = a * v + b
    if rechts.denominator != 1: return None
    t = f'Löse {a} {f} x {plus(b) if b else ""}'.rstrip() + f' = {dz(rechts)} {B}.'
    if not frei(l, t): return None
    return luecken(t, schab(len(l)), 'kleinere Lösung zuerst' if len(l) > 1 else 'die Lösung', l,
                   f'{a} {f} x = {dz(rechts - b)} ⇒ {f} x = {dz(v)} ⇒ ' + ' und '.join(f'{u}°' for u in l) + '.',
                   'Bringe die Zahl auf die andere Seite und teile durch den Faktor.', c=[str(u) for u in l])


def g_anwendung(s):
    if s == 1:
        v = R.choice([Fr(1, 2), Fr(-1, 2)])
        r = R.choice([5, 8, 10, 12, 15, 20])
        m = r + R.randint(1, 5)
        h = m - r * v
        l = COS[v]
        return luecken(f'Die Höhe einer Gondel eines Riesenrads ist h(x) = {m} − {r} · cos x (in m, x = Drehwinkel in Grad). Für welche Winkel {B} ist die Gondel {dz(h)} m hoch?',
                       schab(2), 'kleinerer Winkel zuerst', l, f'{m} − {r} cos x = {dz(h)} ⇒ cos x = {dz(v)} ⇒ x = {l[0]}° oder {l[1]}°.',
                       'Stelle nach cos x um.', c=[str(u) for u in l])
    if s == 2:
        art = R.choice(['eins', 'zwei', 'kein'])
        for _ in range(50):
            al = R.randint(20, 160)
            v = Fr(R.randint(20, 95), 100)
            b1 = asin(float(v)); b2 = 180 - b1
            n = sum(1 for b in (b1, b2) if al + b < 180 - 1e-6)
            if {'eins': 1, 'zwei': 2, 'kein': 0}[art] == n and min(abs(al + b1 - 180), abs(al + b2 - 180)) > 1: break
        else:
            return None
        txt = {1: 'genau ein Winkel', 2: 'zwei Winkel', 0: 'kein Winkel'}
        return auswahl(f'In einem Dreieck ist α = {al}° und sin β = {dz(v)}. Wie viele Werte kommen für β in Frage?', txt[n], list(txt.values()),
                       f'sin β = {dz(v)} ⇒ β ≈ {f1(round(b1, 1))}° oder β ≈ {f1(round(b2, 1))}°. ' +
                       ' '.join(f'{al}° + {f1(round(b, 1))}° {"<" if al + b < 180 else "≥"} 180°.' for b in (b1, b2)) + f' Also {txt[n]}.',
                       'Bestimme beide Winkel zum Sinuswert und prüfe die Winkelsumme.')
    if R.random() < 0.4:
        m, r = R.choice([(5, 2), (4, 2), (6, 3), (8, 4), (3, 1)])
        v = R.choice([Fr(1, 2), Fr(-1, 2)])
        h = m + r * v
        l = SIN[v]
        return luecken(f'Die Wassertiefe in einem Hafen ist t(x) = {m} + {r} · sin x (in m; x in Grad, 360° entsprechen einem Tag). Für welche x {B} ist das Wasser {dz(h)} m tief?',
                       schab(2), 'kleinerer Wert zuerst', l, f'{m} + {r} sin x = {dz(h)} ⇒ sin x = {dz(v)} ⇒ x = {l[0]}° oder {l[1]}°.',
                       'Stelle nach sin x um.', c=[str(u) for u in l])
    al = R.randint(20, 60)
    v = Fr(R.randint(20, 95), 100)
    b1, b2 = asin(float(v)), 180 - asin(float(v))
    if al + b2 >= 180: return None
    ga = 180 - al - b2
    if ga >= b2 - 1: return None
    w_ = gerundet(b2, 1)
    if w_ is None: return None
    return zahl(f'In einem Dreieck ist α = {al}° und sin β = {dz(v)}. β ist der größte Winkel des Dreiecks. Berechne β (auf eine Nachkommastelle).',
                f'β₁ = sin⁻¹({dz(v)}) ≈ {f1(round(b1, 1))}° wäre kleiner als der dritte Winkel {f1(round(180 - al - b1, 1))}°. Also β = 180° − β₁ ≈ {f1(w_)}° (dann γ ≈ {f1(round(ga, 1))}°).',
                'Zu einem Sinuswert gibt es einen spitzen und einen stumpfen Winkel. Welcher kann der größte Winkel sein?', w_, f'round(180 - {K(b1)}, 1)', einheit='°')


GEN = {'sinus': g_sinus, 'kosinus': g_kosinus, 'tangens': g_tangens, 'anzahl': g_anzahl, 'umformen': g_umformen, 'anwendung': g_anwendung}

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9913, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Abschlussprüfung Realschule Bayern Mathematik I
# (2023 Teil A: Sinusgleichung ohne Taschenrechner mit Lösungsmenge in [0°; 180°]; 2025 A 2.4/B 2.3: Flächeninhalt bzw.
# Volumen als Term mit sin/tan aufstellen und den Winkel zu einem gegebenen Wert bestimmen; 2024 B 4.3: Winkel aus einer
# Formel), Bayerischer Mathematik-Test 10 2025 (Gleichung ohne Lösung angeben). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402
from _kl9 import K as _K  # noqa: E402


def schwer():
    P, Kn, O = 'pruefung', 'knobel', ''
    r1 = lambda x: round(x, 1)
    c1 = lambda x: f'round({_K(x)}, 1)'
    L2, L4 = 'x₁ = □°; x₂ = □°', 'x₁ = □°; x₂ = □°; x₃ = □°; x₄ = □°'
    H = 'Grad-Zahlen, kleinere zuerst'
    rg = lambda x: f'round({_K(x)}, 0)'
    return [
        # sinus
        ('sinus', 3, P, luecken('Löse 2 · sin x − 1 = 0 für 0° ≤ x ≤ 180° ohne Taschenrechner.', L2, H, [30, 150],
                                '2 sin x = 1 ⇒ sin x = 0,5. Im Bereich 0° bis 180°: x = 30° und x = 180° − 30° = 150°.', 'Erst sin x allein stellen. sin 30° = 0,5 kennst du.', ['30', '180 - 30'])),
        ('sinus', 3, P, zahl('Ein Dreieck hat die Seiten 6 cm und 8 cm, die den Winkel φ einschließen. Sein Flächeninhalt ist A(φ) = 24 · sin φ (in cm²). Für welchen spitzen Winkel φ ist A = 18 cm²? Runde auf eine Nachkommastelle.',
                             '24 · sin φ = 18 ⇒ sin φ = 0,75 ⇒ φ ≈ 48,6° (spitz; der stumpfe Winkel 131,4° hätte dieselbe Fläche).', 'Setze A = 18 und stelle nach sin φ um.',
                             r1(asin(0.75)), c1(asin(0.75)), einheit='°')),
        ('sinus', 3, Kn, zahl('Wie viele Lösungen hat sin x = 0,3 im Bereich 0° ≤ x < 720°?', 'In jeder vollen Umdrehung (360°) gibt es zwei Lösungen. 720° sind zwei Umdrehungen: 2 · 2 = 4 Lösungen.',
                              'Wie viele Lösungen gibt es in einer Umdrehung? Wie viele Umdrehungen sind 720°?', 4, '2 * 2')),
        ('sinus', 3, O, luecken('Löse sin x = −0,5 im Bereich 0° ≤ x < 360° ohne Taschenrechner.', L2, H, [210, 330],
                                'sin x < 0: unterhalb der Mitte. Bezugswinkel 30°: x = 180° + 30° = 210° und x = 360° − 30° = 330°.', 'Bezugswinkel 30°, dann in die beiden unteren Viertel.',
                                ['180 + 30', '360 - 30'])),
        ('sinus', 2, O, luecken('Löse sin x = 0,9 im Bereich 0° ≤ x < 360°. Runde auf ganze Grad.', L2, H, [round(asin(0.9)), round(180 - asin(0.9))],
                                'sin⁻¹(0,9) ≈ 64,2°, zweite Lösung 180° − 64,2° ≈ 115,8°. Gerundet 64° und 116°.', 'x₂ = 180° − x₁.', [rg(asin(0.9)), rg(180 - asin(0.9))])),
        ('sinus', 2, O, auswahl('sin x = 0,4 hat die Lösung x₁ ≈ 23,6°. Welche zweite Lösung gibt es im Bereich 0° ≤ x < 360°?', '156,4°', ['203,6°', '336,4°', '66,4°'],
                                'Beim Sinus gilt x₂ = 180° − x₁ = 156,4°.', 'Sinus: an der y-Achse spiegeln.')),
        # kosinus
        ('kosinus', 3, P, luecken('Löse 2 · cos x + 1 = 0 im Bereich 0° ≤ x < 360° ohne Taschenrechner.', L2, H, [120, 240],
                                  'cos x = −0,5. Bezugswinkel 60°, Kosinus negativ links: x = 180° − 60° = 120° und x = 360° − 120° = 240°.', 'cos 60° = 0,5. Wo ist der Kosinus negativ?',
                                  ['180 - 60', '360 - 120'])),
        ('kosinus', 3, P, zahl('Eine Strecke hat die Länge d(φ) = 10 · cos φ (in cm) für 0° < φ < 90°. Für welchen Winkel φ ist sie 7 cm lang? Runde auf eine Nachkommastelle.',
                               '10 · cos φ = 7 ⇒ cos φ = 0,7 ⇒ φ ≈ 45,6°.', 'Setze d = 7 und stelle nach cos φ um.', r1(acos(0.7)), c1(acos(0.7)), einheit='°')),
        ('kosinus', 3, Kn, auswahl('Für welche x im Bereich 0° ≤ x < 360° gilt cos x = cos 40°?', 'x = 40° und x = 320°', ['x = 40° und x = 140°', 'nur x = 40°', 'x = 40° und x = 220°'],
                                   'Gleicher Kosinus heißt gleiche x-Koordinate: Spiegelung an der x-Achse, also 360° − 40° = 320°. 140° hätte den gleichen Sinus.',
                                   'Wo auf dem Einheitskreis haben zwei Punkte die gleiche x-Koordinate?')),
        ('kosinus', 3, O, luecken('Löse cos x = 1 im Bereich 0° ≤ x ≤ 720°.', 'x₁ = □°; x₂ = □°; x₃ = □°', H, [0, 360, 720], 'cos x = 1 ganz rechts auf dem Einheitskreis: bei 0°, nach einer Runde bei 360° und nach zwei Runden bei 720° (Grenze gehört dazu).',
                                  'Der Bereich umfasst zwei volle Runden – und das Ende 720° gehört dazu.', ['0', '360', '2 * 360'])),
        ('kosinus', 2, O, luecken('Löse cos x = 0,3 im Bereich 0° ≤ x < 360°. Runde auf ganze Grad.', L2, H, [round(acos(0.3)), round(360 - acos(0.3))],
                                  'cos⁻¹(0,3) ≈ 72,5°, zweite Lösung 360° − 72,5° ≈ 287,5°. Gerundet 73° und 287°.', 'x₂ = 360° − x₁. Runde jede Lösung einzeln.',
                                  [rg(acos(0.3)), rg(360 - acos(0.3))])),
        ('kosinus', 2, O, auswahl('cos x = −0,8 hat die Lösung x₁ ≈ 143,1°. Welche zweite Lösung gibt es im Bereich 0° ≤ x < 360°?', '216,9°', ['36,9°', '323,1°', '323,9°'],
                                  'Beim Kosinus gilt x₂ = 360° − x₁ = 216,9°.', 'Kosinus: an der x-Achse spiegeln.')),
        # tangens
        ('tangens', 3, P, zahl('Das Volumen eines Prismas ist V(φ) = 12 · tan φ (in cm³) für 0° < φ < 90°. Für welchen Winkel φ ist V = 30 cm³? Runde auf eine Nachkommastelle.',
                               '12 · tan φ = 30 ⇒ tan φ = 2,5 ⇒ φ ≈ 68,2°.', 'Setze V = 30 und stelle nach tan φ um.', r1(atan(2.5)), c1(atan(2.5)), einheit='°')),
        ('tangens', 3, P, luecken('Löse tan x = −√3 im Bereich 0° ≤ x < 360° ohne Taschenrechner (tan 60° = √3).', L2, H, [120, 300],
                                  'Bezugswinkel 60°. Tangens negativ links oben und rechts unten: x = 180° − 60° = 120° und x = 120° + 180° = 300°.',
                                  'Der Tangens wiederholt sich alle 180°.', ['180 - 60', '120 + 180'])),
        ('tangens', 3, Kn, zahl('Wie viele Lösungen hat tan x = 5 im Bereich 0° ≤ x < 900°?', 'Der Tangens wiederholt sich alle 180°: genau eine Lösung pro 180°-Abschnitt. 900° : 180° = 5 Lösungen.',
                                'Wie oft passt 180° in 900°?', 5, '900 // 180')),
        ('tangens', 3, O, zahl('Löse 3 · tan x − 2 = 0 im Bereich 0° ≤ x < 360°. Gib die größere Lösung auf eine Nachkommastelle an.', 'tan x = 2/3 ⇒ x₁ ≈ 33,7°, x₂ = x₁ + 180° ≈ 213,7°.',
                               'Erst tan x allein stellen, dann + 180°.', r1(atan(2 / 3) + 180), c1(atan(2 / 3) + 180), einheit='°')),
        ('tangens', 2, O, zahl('Löse tan x = 0,5 im Bereich 0° ≤ x < 360°. Gib die kleinere Lösung auf eine Nachkommastelle an.', 'tan⁻¹(0,5) ≈ 26,6°.', 'Umkehrtaste tan⁻¹.',
                               r1(atan(0.5)), c1(atan(0.5)), einheit='°')),
        ('tangens', 2, O, auswahl('tan x = 2 hat die Lösung x₁ ≈ 63,4°. Welche zweite Lösung gibt es im Bereich 0° ≤ x < 360°?', '243,4°', ['116,6°', '296,6°', '153,4°'],
                                  'Beim Tangens gilt x₂ = x₁ + 180° = 243,4°.', 'Tangens: plus 180°.')),
        # anzahl
        ('anzahl', 3, P, auswahl('Für welche Zahl c hat die Gleichung 3 · sin x = c im Bereich 0° ≤ x < 360° keine Lösung?', 'c = 4', ['c = 3', 'c = −2', 'c = 0'],
                                 'sin x = c/3 braucht −1 ≤ c/3 ≤ 1, also −3 ≤ c ≤ 3. Nur c = 4 liegt außerhalb.', 'Stelle nach sin x um. Welche Werte kann sin x annehmen?')),
        ('anzahl', 3, P, auswahl('Wie viele Lösungen hat cos x = 0,5 im Bereich 0° ≤ x ≤ 180°?', 'genau eine', ['zwei', 'keine', 'drei'],
                                 'Im ganzen Kreis wären es 60° und 300°. Im Bereich bis 180° liegt nur 60°.', 'Bestimme alle Lösungen und prüfe, welche im Bereich liegen.')),
        ('anzahl', 3, Kn, zahl('Wie viele Lösungen hat sin x = cos x im Bereich 0° ≤ x < 720°?', 'In einer Umdrehung: 45° und 225° (tan x = 1). In zwei Umdrehungen: 4 Lösungen.',
                               'Teile durch cos x: Welche Gleichung entsteht? Wie oft passt ihre Periode hinein?', 4, '2 * 2')),
        ('anzahl', 3, O, auswahl('Wie viele Lösungen hat (sin x)² = 1 im Bereich 0° ≤ x < 360°?', 'zwei', ['eine', 'vier', 'keine'],
                                 'sin x = 1 (bei 90°) oder sin x = −1 (bei 270°): zwei Lösungen.', 'Aus (sin x)² = 1 folgt sin x = 1 oder sin x = −1.')),
        ('anzahl', 2, O, auswahl('Wie viele Lösungen hat cos x = −1,5?', 'keine', ['eine', 'zwei'], 'cos x liegt immer zwischen −1 und 1.', 'Welche Werte kann der Kosinus annehmen?')),
        ('anzahl', 2, O, auswahl('Wie viele Lösungen hat sin x = −1 im Bereich 0° ≤ x < 360°?', 'genau eine', ['zwei', 'keine'], 'Nur bei 270° ist sin x = −1.', 'Tiefster Punkt des Einheitskreises.')),
        # umformen
        ('umformen', 3, P, luecken('Löse 6 · sin x + 1 = 4 im Bereich 0° ≤ x < 360°.', L2, H, [30, 150], '6 sin x = 3 ⇒ sin x = 0,5 ⇒ x = 30° oder x = 150°.', 'Erst 1 abziehen, dann durch 6 teilen.',
                                   ['30', '180 - 30'])),
        ('umformen', 3, P, luecken('Löse 3 · cos x + 2 = cos x + 1 im Bereich 0° ≤ x < 360°.', L2, H, [120, 240], '2 cos x = −1 ⇒ cos x = −0,5 ⇒ x = 120° oder x = 240°.',
                                   'Bringe alle cos x auf eine Seite.', ['180 - 60', '180 + 60'])),
        ('umformen', 3, Kn, luecken('Löse sin x · cos x = 0 im Bereich 0° ≤ x < 360°.', L4, H, [0, 90, 180, 270],
                                    'Ein Produkt ist 0, wenn ein Faktor 0 ist: sin x = 0 (0°, 180°) oder cos x = 0 (90°, 270°).', 'Satz vom Nullprodukt – wie bei quadratischen Gleichungen.',
                                    ['0', '90', '180', '270'])),
        ('umformen', 3, O, luecken('Löse 2 · (sin x)² = sin x im Bereich 0° ≤ x < 360°.', L4, H, [0, 30, 150, 180],
                                   'sin x · (2 sin x − 1) = 0: sin x = 0 (0°, 180°) oder sin x = 0,5 (30°, 150°). Falle: Durch sin x teilen verliert 0° und 180°.',
                                   'Nicht durch sin x teilen! Ausklammern.', ['0', '30', '150', '180'])),
        ('umformen', 2, O, luecken('Löse 2 · cos x = 1 im Bereich 0° ≤ x < 360°.', L2, H, [60, 300], 'cos x = 0,5 ⇒ x = 60° oder x = 300°.', 'Durch 2 teilen.', ['60', '360 - 60'])),
        ('umformen', 2, O, luecken('Löse sin x + 1 = 0 im Bereich 0° ≤ x < 360°.', 'x = □°', 'Grad-Zahl', [270], 'sin x = −1 nur bei 270°.', 'Stelle sin x allein.', ['270'])),
        # anwendung
        ('anwendung', 3, P, zahl('Eine Gondel im Riesenrad ist h(x) = 20 − 18 · cos x Meter hoch (x Drehwinkel in Grad). Bei welchem Drehwinkel zwischen 0° und 180° ist sie 29 m hoch?',
                                 '20 − 18 cos x = 29 ⇒ cos x = −0,5 ⇒ x = 120° (im Bereich 0° bis 180° die einzige Lösung).', 'Gleichung aufstellen und nach cos x umstellen.', 120, '180 - 60',
                                 einheit='°')),
        ('anwendung', 3, P, zahl('Ein Dreieck hat die Seiten a = 5 cm und b = 8 cm und den Flächeninhalt 10 cm². Der Winkel γ zwischen a und b ist stumpf. Wie groß ist γ?',
                                 '1/2 · 5 · 8 · sin γ = 10 ⇒ sin γ = 0,5 ⇒ γ = 30° oder 150°. Stumpf: γ = 150°.', 'Flächenformel, dann beide Lösungen bedenken.', 150, '180 - 30', einheit='°')),
        ('anwendung', 3, Kn, zahl('Eine Gondel ist h(x) = 25 − 20 · cos x Meter hoch (x Drehwinkel in Grad, eine Runde 0° bis 360°). Über wie viele Grad der Drehung ist sie höher als 35 m?',
                                  'h > 35 ⇔ cos x < −0,5. Das gilt zwischen 120° und 240°: über 240° − 120° = 120°, also ein Drittel der Runde.',
                                  'Bestimme die beiden Winkel mit h = 35 m. Dazwischen ist die Gondel höher.', 120, '240 - 120', einheit='°')),
        ('anwendung', 3, O, zahl('Im Dreieck ABC ist a = 9 cm, b = 12 cm und α = 40°. Der Winkel β ist stumpf. Berechne β (auf eine Nachkommastelle).',
                                 'sin β = 12 · sin 40° : 9 ≈ 0,857 ⇒ 59,0° oder 180° − 59,0° = 121,0°. Stumpf: β ≈ 121,0° (40° + 121° < 180° passt).',
                                 'Der Taschenrechner liefert nur den spitzen Winkel. Rechne 180° minus.', r1(180 - asin(12 * sin(40) / 9)), c1(180 - asin(12 * sin(40) / 9)), einheit='°')),
        ('anwendung', 2, O, luecken('Die Tageslänge an einem Ort ist d(x) = 12 + 4 · sin x Stunden (x in Grad, 360° entsprechen einem Jahr). Für welche x ist der Tag genau 14 Stunden lang?', L2, H,
                                    [30, 150], '12 + 4 sin x = 14 ⇒ sin x = 0,5 ⇒ x = 30° oder x = 150°.', 'Gleichung aufstellen, sin x allein stellen.', ['30', '180 - 30'])),
        ('anwendung', 2, O, zahl('Die Auslenkung eines Pendels ist s(x) = 10 · sin x (in cm). Für welchen Winkel x zwischen 0° und 90° ist s = 5 cm?', '10 sin x = 5 ⇒ sin x = 0,5 ⇒ x = 30°.',
                                 'Nach sin x umstellen.', 30, '180 / 6', einheit='°')),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('gleichungen.trig', 13_9_13)
# c) praktisch Dublette (sin x = −0,7 und −0,69 haben dieselbe gerundete Lösung) → anderer Wert
BF.ersetze('sinus', 'Löse sin x = −0,69 im Bereich 0° ≤ x < 360°. Runde auf ganze Grad.', BF.L(
    'Löse sin x = −0,9 im Bereich 0° ≤ x < 360°. Runde auf ganze Grad.', 'x₁ ≈ □°; x₂ ≈ □°', [244, 296],
    ['round(244.158067236833, 0)', 'round(295.841932763167, 0)'],
    'sin⁻¹(−0,9) ≈ −64,2° liegt nicht im Bereich. 180° + 64,2° ≈ 244° und 360° − 64,2° ≈ 296°.',
    'Negativer Sinus: Der Punkt liegt unterhalb der x-Achse (3. und 4. Quadrant).', hinweis='kleinere Lösung zuerst'))
# a) Routine „Löse … = −0,xx, runde auf ganze Grad“ → Stufe 2
for _w in ('−0,7', '−0,72', '−0,46', '−0,31'):
    BF.stufe('sinus', f'Löse sin x = {_w} im Bereich 0° ≤ x < 360°. Runde auf ganze Grad.', 2)
for _w in ('−0,57', '−0,61', '−0,68', '−0,46', '−0,2'):
    BF.stufe('kosinus', f'Löse cos x = {_w} im Bereich 0° ≤ x < 360°. Runde auf ganze Grad.', 2)
BF.nicht_umgesetzt('tangens S3 Rampe/„22 % Steigung“ gehören inhaltlich zu trigo.rechtwinklig',
                   'Lösungen richtig; tan x = Wert mit spitzem Winkel ist ein Sonderfall der Gleichung. Die Zuordnung zum Thema betrifft den Plan.')

# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    d = bauen('gleichungen.trig',
          'Winkel zu einem gegebenen Sinus-, Kosinus- oder Tangenswert bestimmen und die Mehrdeutigkeit im Bereich 0° bis 360° beachten.',
          ['sin x = v: x₂ = 180° − x₁. cos x = v: x₂ = 360° − x₁. tan x = v: x₂ = x₁ + 180°.', '|v| > 1 bei sin/cos: keine Lösung; v = ±1: eine Lösung.',
           'Negative Ergebnisse des Taschenrechners in den Bereich 0°–360° verschieben.', 'Im Dreieck: Winkelsumme prüfen.'],
          [('Grundgleichungen', ['sinus', 'kosinus', 'tangens']), ('Lösbarkeit und Umformen', ['anzahl', 'umformen']), ('Anwenden', ['anwendung'])],
          ETAPPEN, GEN,
          meiden={'sinus': ['sin x = 0,5 '], 'kosinus': ['cos x = −0,5 '], 'tangens': ['tan x = 1 '], 'anzahl': ['cos x = −1 '],
                  'umformen': ['4 sin x + 1 = 3'], 'anwendung': ['α = 40° und sin β = 0,5']},
          offen=['Lernkarten „sinus“, „kosinus“, „anzahl“ zeigen jetzt die Graphen mit der Geraden y = v; Aufgaben mit Graph gibt es bei „anzahl“. Für den Tangens gibt es noch keinen Graphentyp (Vorschlag der Prüfung: „tan“ ergänzen).',
                 'Lösungsbereich durchgängig 0° ≤ x < 360°; Bogenmaß ist nicht enthalten (gehört nicht zur 9. Klasse).'])
    anhaengen(d, 9913, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden


# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl9) ----
from _durchsicht_kl9 import Befunde as _DSB, durchsicht  # noqa: E402

DS = _DSB('gleichungen.trig', 19_9_13)
# sinus: negative Werte brauchen den Schritt über 180° (Stufe 2); dieselbe Aufgabe stand auf Stufe 1 und 3
DS.stufe('sinus', 'Löse sin x = −0,5 im Bereich 0° ≤ x < 360°.', 2)
DS.stufe('sinus', 'Löse sin x = −0,9 im Bereich 0° ≤ x < 360°. Runde auf ganze Grad.', 2)
# kosinus: kleinere Lösung runden ist Stufe 2; neue Stufe-3-Aufgabe verbindet cos und sin
DS.stufe('kosinus', 'Löse cos x = −0,05 im Bereich 0° ≤ x < 360°. Gib die kleinere Lösung auf eine Nachkommastelle an.', 2)
DS.neu('kosinus', 3, DS.L('Für welche x im Bereich 0° ≤ x < 360° gilt cos x = sin 30°? Ohne Taschenrechner.', 'x₁ = □°; x₂ = □°', [60, 300], ['60', '300'],
                          'sin 30° = 0,5. cos x = 0,5 gilt für x = 60° und x = 360° − 60° = 300°.', 'Rechne zuerst sin 30° aus.'))
# tangens: ein Winkel aus tan⁻¹ ist Stufe 1, die zweite Lösung bei negativem v wie Stufe 2
for _t in ('Eine Rampe steigt auf 8 m waagrechter Länge um 0,5 m. Unter welchem Winkel steigt sie? Runde auf eine Nachkommastelle.',
           'Ein Weg hat 22 % Steigung. Wie groß ist der Steigungswinkel? Runde auf eine Nachkommastelle.',
           'Ein Weg hat 18 % Steigung. Wie groß ist der Steigungswinkel? Runde auf eine Nachkommastelle.'):
    DS.stufe('tangens', _t, 1)
for _t in ('Löse tan x = −1,82 im Bereich 0° ≤ x < 360°. Gib die kleinere Lösung auf eine Nachkommastelle an.',
           'Löse tan x = −1,12 im Bereich 0° ≤ x < 360°. Gib die größere Lösung auf eine Nachkommastelle an.',
           'Löse tan x = −0,35 im Bereich 0° ≤ x < 360°. Gib die größere Lösung auf eine Nachkommastelle an.'):
    DS.stufe('tangens', _t, 2)
# umformen: a sin x + b = c und sin x auf beiden Seiten sind Stufe 2
for _t in ('Löse 6 · sin x + 1 = 4 im Bereich 0° ≤ x < 360°.', 'Löse 3 sin x − 3 = sin x − 2 im Bereich 0° ≤ x < 360°.',
           'Löse 5 sin x − 2 = 3 sin x − 3 im Bereich 0° ≤ x < 360°.', 'Löse 3 · cos x + 2 = cos x + 1 im Bereich 0° ≤ x < 360°.'):
    DS.stufe('umformen', _t, 2)
# anwendung: je eine Hafen-Aufgabe auf Stufe 2; Sinussatz und Flächenformel kommen erst in trigo.allgemein (Reihenfolge 14)
DS.stufe('anwendung', 'Die Wassertiefe in einem Hafen ist t(x) = 8 + 4 · sin x (in m; x in Grad, 360° entsprechen einem Tag). Für welche x im Bereich 0° ≤ x < 360° ist das Wasser 10 m tief?', 2)
DS.stufe('anwendung', 'Die Wassertiefe in einem Hafen ist t(x) = 4 + 2 · sin x (in m; x in Grad, 360° entsprechen einem Tag). Für welche x im Bereich 0° ≤ x < 360° ist das Wasser 5 m tief?', 2)
DS.ersetze('anwendung', 'Im Dreieck ABC ist a = 9 cm, b = 12 cm und α = 40°. Der Winkel β ist stumpf. Berechne β (auf eine Nachkommastelle).',
           DS.Z('In einem Dreieck ist α = 25° und sin β = 0,9. Der Winkel β ist stumpf. Wie groß ist γ? Runde auf eine Nachkommastelle.', 39.2, '180 - 25 - (180 - 64.158482002216)',
                'sin⁻¹(0,9) ≈ 64,2°. Stumpf: β = 180° − 64,2° ≈ 115,8°. γ = 180° − 25° − 115,8° ≈ 39,2°.',
                'Erst den stumpfen Winkel β bestimmen, dann die Winkelsumme.', einheit='°', toleranz=0.1))
DS.ersetze('anwendung', 'Ein Dreieck hat die Seiten a = 5 cm und b = 8 cm und den Flächeninhalt 10 cm². Der Winkel γ zwischen a und b ist stumpf. Wie groß ist γ?',
           DS.Z('Ein Dreieck hat die Seiten a = 5 cm und b = 8 cm und den Flächeninhalt A = 1/2 · a · b · sin γ = 10 cm². Der Winkel γ zwischen a und b ist stumpf. Wie groß ist γ?', 150, '180 - 30',
                '1/2 · 5 · 8 · sin γ = 10 ⇒ sin γ = 0,5 ⇒ γ = 30° oder 150°. Stumpf: γ = 150°.',
                'Setze die Zahlen in die Formel ein und löse nach sin γ auf.', einheit='°'))
DS.fuer_nutzer('gleichungen.trig (Reihenfolge 13) steht vor trigo.allgemein (14). Der Einheitskreis, sin(180° − α) und die Flächenformel werden aber erst dort erklärt. Vorschlag: Reihenfolge tauschen.')

if __name__ == '__main__':
    durchsicht('gleichungen.trig', DS)


# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl9) ----
from _stufen_kl9 import Stufen, stufen  # noqa: E402

ST = Stufen('gleichungen.trig', 20_9_13)
Z, A, L = ST.Z, ST.A, ST.L
B = 'im Bereich 0° ≤ x < 360°'

# sinus
ST.stufenleiter('sinus', 'Aus einer Lösung von sin x = v die zweite mit x₂ = 180° − x₁ bestimmen.',
                'Ganze Gleichung lösen, auch mit negativem v und Runden, Riesenrad, Wert v aus einer Lösung.',
                'Ohne Taschenrechner, mehrere Umdrehungen, Abstand der Lösungen, Fehler „360° − x₁“, Bedingung für zwei Lösungen, Begründung mit dem Vorzeichen.')
ST.typ('sinus', '/^/', 'direkt', s=1)
ST.typ('sinus', '/^/', 'mehrschritt', s=2)
ST.typ('sinus', 'Jemand', 'fehler')
ST.typ('sinus', 'Ein Dreieck hat die Seiten 6 cm', 'transfer')
ST.typ('sinus', '/^/', 'verknuepfen', s=3)
ST.neu('sinus', 'erkennen', A('Wie bekommt man bei sin x = v aus der ersten Lösung x₁ die zweite Lösung?', 'x₂ = 180° − x₁', ['x₂ = 360° − x₁', 'x₂ = x₁ + 180°', 'x₂ = −x₁'],
       'Am Riesenrad ist die Gondel bei x₁ und bei 180° − x₁ gleich hoch (Spiegelung an der senkrechten Achse).', 'Wo ist die Gondel gleich hoch?'))
ST.neu('sinus', 'einkleidung', L(f'Eine Gondel ist y = 10 · sin x Meter über der Achse des Riesenrads (x Drehwinkel). Bei welchen Winkeln {B} ist sie 8 m über der Achse? Runde auf ganze Grad.',
       'x₁ ≈ □°; x₂ ≈ □°', [53, 127], ['round(53.13010235415599, 0)', 'round(180 - 53.13010235415599, 0)'],
       '10 sin x = 8 ⇒ sin x = 0,8 ⇒ x₁ ≈ 53,1° ≈ 53°, x₂ = 180° − 53,1° ≈ 126,9° ≈ 127°.', 'Teile zuerst durch 10.', hinweis='kleinerer Winkel zuerst'))
ST.neu('sinus', 'direkt', Z('Bestimme mit dem Taschenrechner die Lösung von sin x = 0,25 zwischen 0° und 90°. Runde auf eine Nachkommastelle.', 14.5, '14.477512185929925',
       'sin⁻¹(0,25) ≈ 14,5°. (Die zweite Lösung wäre 180° − 14,5° = 165,5°.)', 'Taste sin⁻¹, Rechner auf DEG.', einheit='°', toleranz=0.1))
ST.neu('sinus', 'umkehr', Z(f'Die Gleichung sin x = v hat {B} die Lösung x = 210°. Wie groß ist v?', -0.5, '-0.5',
       '210° = 180° + 30°: Die Gondel steht so tief unter der Achse wie bei 30° darüber. sin 210° = −sin 30° = −0,5.', 'Vergleiche 210° mit 30°.'))
ST.neu('sinus', 'parameter', A(f'Für welche Werte v hat sin x = v {B} genau zwei Lösungen?', 'für −1 < v < 1', ['für −1 ≤ v ≤ 1', 'für alle v', 'für v > 1'],
       'Bei |v| > 1 gibt es keine Lösung, bei v = 1 oder v = −1 genau eine (90° bzw. 270°), dazwischen immer zwei.', 'Was passiert bei v = 1?'))
ST.neu('sinus', 'begruenden', A(f'Stimmt: Hat sin x = v die Lösung 40°, dann hat sin x = −v {B} die Lösungen 220° und 320°?', 'Ja: 220° = 40° + 180° und 320° = 360° − 40° liegen so tief unter der Achse wie 40° darüber.',
       ['Nein, die Lösungen sind −40° und 140°.', 'Nein, sin x = −v hat keine Lösung.', 'Nur wenn v größer als 0,5 ist.'],
       'Eine halbe Drehung weiter (x + 180°) und die Spiegelung 360° − x kehren das Vorzeichen des Sinus um: sin 220° = sin 320° = −sin 40°.', 'Zeichne die Gondel bei 40°, 220° und 320°.'))
ST.neu('sinus', 'rueckwaerts', L('Die beiden Lösungen einer Gleichung sin x = v liegen zwischen 0° und 180° und sind 100° voneinander entfernt. Wie heißen sie?',
       'x₁ = □°; x₂ = □°', [40, 140], ['(180 - 100) // 2', '(180 + 100) // 2'],
       'Es gilt x₂ = 180° − x₁ und x₂ − x₁ = 100°. Also 180° − 2x₁ = 100°, x₁ = 40°, x₂ = 140°.', 'Nutze x₂ = 180° − x₁.', hinweis='kleinere Lösung zuerst'))
ST.neu('sinus', 'pruefung', L(f'Löse ohne Taschenrechner {B}: a) sin x = 1, b) sin x = 0, c) sin x = −1.', 'a) x = □°; b) x₁ = □°, x₂ = □°; c) x = □°', [90, 0, 180, 270],
       ['90', '0', '180', '270'], 'a) ganz oben: 90°. b) auf Höhe der Achse: 0° und 180°. c) ganz unten: 270°.', 'Denk an die Gondel ganz oben, auf Achsenhöhe und ganz unten.'))
ST.knobel('sinus', Z('Wie viele Lösungen hat sin x = 0,2 im Bereich 0° ≤ x < 1 080°?', 6, '3 * 2',
          'Bei jeder vollen Drehung um 360° ist die Gondel zweimal auf der Höhe 0,2 (einmal aufwärts, einmal abwärts). 1 080° sind 3 volle Drehungen, also 3 · 2 = 6 Lösungen.',
          'Wie viele volle Drehungen sind 1 080°?'))
ST.knobel('sinus', L(f'Für welche x {B} gilt sin x = sin(x + 180°)?', 'x₁ = □°; x₂ = □°', [0, 180], ['0', '180'],
          'Eine halbe Drehung weiter ist die Gondel genau gegenüber: sin(x + 180°) = −sin x. Aus sin x = −sin x folgt sin x = 0, also x = 0° oder x = 180°.',
          'Wo ist die Gondel eine halbe Drehung später?', hinweis='kleinere Lösung zuerst'))

# kosinus
ST.stufenleiter('kosinus', 'Aus einer Lösung von cos x = v die zweite mit x₂ = 360° − x₁ bestimmen.',
                'Ganze Gleichung lösen, negative Werte, mehrere Umdrehungen, waagrechter Abstand am Riesenrad, Wert v aus einer Lösung.',
                'Ohne Taschenrechner, cos x = cos 40°, Fehler „180° − x₁“, genau eine Lösung bis 180°, Begründung bei cos x = 0, mehrteilige Aufgabe.')
ST.typ('kosinus', '/^/', 'direkt', s=1)
ST.typ('kosinus', '/^/', 'mehrschritt', s=2)
ST.typ('kosinus', 'Löse cos x = 1 im Bereich 0° ≤ x ≤ 720°', 'mehrschritt')
ST.typ('kosinus', 'Eine Strecke', 'transfer')
ST.typ('kosinus', '/^/', 'verknuepfen', s=3)
ST.neu('kosinus', 'erkennen', A('Wie bekommt man bei cos x = v aus der ersten Lösung x₁ die zweite Lösung?', 'x₂ = 360° − x₁', ['x₂ = 180° − x₁', 'x₂ = x₁ + 180°', 'x₂ = x₁ − 90°'],
       'Der waagrechte Abstand von der Achse ist bei x₁ und bei 360° − x₁ gleich (Spiegelung an der waagrechten Achse).', 'Wo ist die Gondel gleich weit rechts?'))
ST.neu('kosinus', 'einkleidung', L(f'Der waagrechte Abstand einer Gondel von der Achse des Riesenrads ist d = 10 · cos x (in m, rechts positiv). Bei welchen Drehwinkeln {B} ist sie 6 m rechts der Achse? Runde auf ganze Grad.',
       'x₁ ≈ □°; x₂ ≈ □°', [53, 307], ['round(53.13010235415599, 0)', 'round(360 - 53.13010235415599, 0)'],
       '10 cos x = 6 ⇒ cos x = 0,6 ⇒ x₁ ≈ 53,1° ≈ 53°, x₂ = 360° − 53,1° ≈ 306,9° ≈ 307°.', 'Teile zuerst durch 10.', hinweis='kleinerer Winkel zuerst'))
ST.neu('kosinus', 'umkehr', Z(f'Die Gleichung cos x = v hat {B} die Lösung x = 300°. Wie groß ist v?', 0.5, '0.5',
       '300° = 360° − 60°, also cos 300° = cos 60° = 0,5. Die zweite Lösung ist 60°.', 'Welcher Winkel gehört zu 300° als Partner?'))
ST.neu('kosinus', 'fehler', A(f'Jemand löst cos x = 0,2 {B} und gibt 78,5° und 101,5° an. Was stimmt?', 'Falsch: Beim Kosinus ist x₂ = 360° − 78,5° = 281,5°.',
       ['Richtig.', 'Falsch: x₂ = 78,5° + 180° = 258,5°.', 'Falsch: Es gibt nur eine Lösung.'],
       'x₂ = 180° − x₁ ist die Regel für den Sinus. Probe: cos 101,5° ist negativ, cos 281,5° ≈ 0,2.', 'Mache die Probe mit cos 101,5°.'))
ST.neu('kosinus', 'parameter', A('Für welche Werte v hat cos x = v im Bereich 0° ≤ x ≤ 180° genau eine Lösung?', 'für alle v mit −1 ≤ v ≤ 1', ['nur für v = 1 und v = −1', 'für keinen Wert v', 'für alle v'],
       'Von 0° bis 180° fährt die Gondel von ganz rechts nach ganz links, cos x fällt dabei von 1 auf −1 und nimmt jeden Wert dazwischen genau einmal an.', 'Wie ändert sich cos x von 0° bis 180°?'))
ST.neu('kosinus', 'begruenden', A(f'Stimmt: cos x = 0 hat {B} genau die Lösungen 90° und 270°?', 'Ja: Ganz oben und ganz unten ist der waagrechte Abstand 0; dazu passt 270° = 360° − 90°.',
       ['Nein, nur 90°.', 'Nein, die Lösungen sind 0° und 180°.', 'Nein, die Lösungen sind 90° und 180°.'],
       'cos x ist der waagrechte Abstand von der Achse. Er ist 0, wenn die Gondel senkrecht über oder unter der Achse steht: 90° und 270°.', 'Wo ist die Gondel direkt über oder unter der Achse?'))
ST.neu('kosinus', 'pruefung', L(f'Löse {B}: a) cos x = −0,3 (ganze Grad), b) cos x = −1, c) Wie viele Lösungen hat 2 cos x = 3?', 'a) x₁ ≈ □°, x₂ ≈ □°; b) x = □°; c) □ Lösungen', [107, 253, 180, 0],
       ['round(107.4576031237221, 0)', 'round(360 - 107.4576031237221, 0)', '180', '0'],
       'a) cos⁻¹(−0,3) ≈ 107,5° ≈ 107°, x₂ = 360° − 107,5° ≈ 252,5° ≈ 253°. b) ganz links: 180°. c) cos x = 1,5 > 1: keine Lösung.', 'Bei c) erst durch 2 teilen.'))
ST.knobel('kosinus', L(f'Die beiden Lösungen einer Gleichung cos x = v {B} liegen genau 100° auseinander. Wie heißen sie?', 'x₁ = □°; x₂ = □°', [130, 230], ['(360 - 100) // 2', '(360 + 100) // 2'],
          'Es gilt x₂ = 360° − x₁ und x₂ − x₁ = 100°. Also 360° − 2x₁ = 100°, x₁ = 130°, x₂ = 230°. Probe: cos 130° = cos 230° ≈ −0,64. (Mit x₁ = 50° wären es 260° Abstand.)',
          'Nutze x₂ = 360° − x₁.', hinweis='kleinere Lösung zuerst'))
ST.knobel('kosinus', Z('Wie viele Lösungen hat cos x = 0,3 im Bereich −360° < x < 360°?', 4, '2 + 2',
          'Von 0° bis 360° gibt es zwei Lösungen (≈ 72,5° und ≈ 287,5°). Rückwärts gedreht (−360° bis 0°) wiederholt sich alles: ≈ −72,5° und ≈ −287,5°. Zusammen 4.',
          'Ein negativer Winkel heißt: im Uhrzeigersinn drehen.'))

# tangens
ST.stufenleiter('tangens', 'Aus einer Lösung von tan x = v die zweite mit x₂ = x₁ + 180° bestimmen, Steigungswinkel.',
                'Ganze Gleichung mit negativem v lösen, Zeiger auf einer Geraden, Wert v aus einer Lösung.',
                'Ohne Taschenrechner, Volumen über tan, viele Lösungen, Fehler „180° − x₁“, Lösungen für jedes v, Lage der Lösungen begründen.')
ST.typ('tangens', '/^/', 'direkt', s=1)
ST.typ('tangens', '/^/', 'mehrschritt', s=2)
ST.typ('tangens', 'Das Volumen', 'transfer')
ST.typ('tangens', '/^/', 'verknuepfen', s=3)
ST.neu('tangens', 'erkennen', A('Nach wie viel Grad wiederholen sich die Werte des Tangens?', 'nach 180°', ['nach 360°', 'nach 90°', 'nach 45°'],
       'Die Gegenspeiche eine halbe Drehung weiter hat dieselbe Steigung: tan(x + 180°) = tan x.', 'Denk an die Gegenspeiche.'))
ST.neu('tangens', 'darstellung', L(f'Ein Zeiger zeigt vom Ursprung auf einen Punkt der Geraden y = 3x. Welchen Winkel kann er mit der positiven x-Achse bilden ({B})? Runde auf ganze Grad.',
       'x₁ ≈ □°; x₂ ≈ □°', [72, 252], ['round(71.56505117707799, 0)', 'round(71.56505117707799 + 180, 0)'],
       'Die Steigung der Geraden ist tan x = 3 ⇒ x₁ ≈ 71,6° ≈ 72°. Auf die andere Seite der Geraden zeigt x₂ ≈ 251,6° ≈ 252°.', 'Steigung = tan x.', hinweis='kleinerer Winkel zuerst'))
ST.neu('tangens', 'umkehr', Z(f'Die Gleichung tan x = v hat {B} die Lösung x = 225°. Wie groß ist v?', 1, '1',
       '225° = 45° + 180°. Der Tangens wiederholt sich alle 180°: tan 225° = tan 45° = 1.', 'Ziehe 180° ab.'))
ST.neu('tangens', 'fehler', A(f'Jemand löst tan x = 3 {B} und gibt 71,6° und 108,4° an. Was stimmt?', 'Falsch: Beim Tangens ist x₂ = 71,6° + 180° = 251,6°.',
       ['Richtig.', 'Falsch: x₂ = 360° − 71,6° = 288,4°.', 'Falsch: Es gibt nur eine Lösung.'],
       '180° − x₁ ist die Regel für den Sinus. Probe: tan 108,4° ist negativ, tan 251,6° ≈ 3.', 'Mache die Probe mit tan 108,4°.'))
ST.neu('tangens', 'parameter', A(f'Für welche Werte v hat tan x = v {B} genau zwei Lösungen?', 'für alle v', ['nur für −1 ≤ v ≤ 1', 'nur für v > 0', 'für keinen Wert v'],
       'Der Tangens nimmt jeden Wert an (jede Steigung ist möglich), und zwar alle 180° wieder. Im Bereich bis 360° also immer zweimal.', 'Gibt es eine Steigung, die keine Gerade hat?'))
ST.neu('tangens', 'begruenden', A(f'Stimmt: tan x = −2 hat {B} eine Lösung zwischen 90° und 180° und eine zwischen 270° und 360°?', 'Ja: tan⁻¹(−2) ≈ −63,4°; plus 180° gibt 116,6°, plus 360° gibt 296,6°.',
       ['Nein, beide liegen zwischen 0° und 90°.', 'Nein, es gibt keine Lösung.', 'Nein, die Lösungen sind 63,4° und 243,4°.'],
       'Negative Steigung heißt: Der Zeiger zeigt nach links oben oder nach rechts unten. Das sind die Bereiche 90° bis 180° und 270° bis 360°.', 'In welchen Bereichen ist die Steigung negativ?'))
ST.neu('tangens', 'pruefung', L(f'Löse {B} (ganze Grad): a) tan x = 1, b) tan x = −1, c) tan x = 0,4.', 'a) □° und □°; b) □° und □°; c) □° und □°', [45, 225, 135, 315, 22, 202],
       ['45', '45 + 180', '135', '135 + 180', 'round(21.80140948635181, 0)', 'round(21.80140948635181 + 180, 0)'],
       'a) 45°, 225°. b) tan⁻¹(−1) = −45° ⇒ 135° und 315°. c) tan⁻¹(0,4) ≈ 21,8° ≈ 22° und 201,8° ≈ 202°.', 'Immer x₂ = x₁ + 180°.'))
ST.knobel('tangens', Z('Wie viele Lösungen hat tan x = 2 im Bereich 0° ≤ x < 1 000°?', 6, '6',
          'tan⁻¹(2) ≈ 63,4°. Alle 180° kommt eine Lösung dazu: 63,4°, 243,4°, 423,4°, 603,4°, 783,4°, 963,4°. Die nächste, 1 143,4°, ist zu groß. Also 6 Lösungen.',
          'Zähle 63,4° + k · 180° ab.'))
ST.knobel('tangens', Z('Für einen spitzen Winkel x gilt tan x = 4 · tan(90° − x). Wie groß ist x? Runde auf eine Nachkommastelle.', 63.4, '63.43494882292201',
          'Im rechtwinkligen Dreieck tauschen für 90° − x Gegen- und Ankathete die Rollen: tan(90° − x) = 1 : tan x. Also tan x = 4 : tan x, (tan x)² = 4, tan x = 2 (x spitz), x ≈ 63,4°.',
          'Was ist tan(90° − x) im rechtwinkligen Dreieck?', einheit='°', toleranz=0.1))

# anzahl
ST.stufenleiter('anzahl', 'Am Wert v ablesen: keine, eine oder zwei Lösungen.',
                'Sonderfälle v = ±1 und |v| > 1, Graph mit Gerade, Wert v zu genau einer Lösung, Gondel zu hoch.',
                'Parameter für keine oder genau eine Lösung, sin x = cos x und Quadrate, Fehler bei ±1 und |v| > 1, mehrteilige Aufgabe.')
ST.typ('anzahl', '/^/', 'erkennen', s=1)
ST.typ('anzahl', 'Im Bild', 'darstellung')
ST.typ('anzahl', '/^/', 'mehrschritt', s=2)
ST.typ('anzahl', 'Jemand', 'fehler')
ST.typ('anzahl', '/^(Für welche|4 cos x)/', 'parameter')
ST.typ('anzahl', '/^/', 'verknuepfen', s=3)
ST.neu('anzahl', 'direkt', Z(f'sin x = 1 hat {B} genau eine Lösung. Gib sie an.', 90, '90',
       'sin x = 1 heißt: Die Gondel ist ganz oben. Das ist nur bei x = 90° so.', 'Wo ist die Gondel ganz oben?', einheit='°'))
ST.neu('anzahl', 'umkehr', A(f'Für welchen Wert v hat cos x = v {B} genau eine Lösung, nämlich x = 0°?', 'v = 1', ['v = 0', 'v = −1', 'v = 0,5'],
       'Bei x = 0° steht die Gondel ganz rechts: cos 0° = 1, und nur dort.', 'Wo steht die Gondel bei 0°?'))
ST.neu('anzahl', 'einkleidung', A('Eine Gondel hat die Höhe h(x) = 13 − 10 · cos x (in m). Wie oft während einer Umdrehung (0° ≤ x < 360°) ist sie genau 25 m hoch?', 'nie', ['einmal', 'zweimal', 'viermal'],
       '13 − 10 cos x = 25 ⇒ cos x = −1,2 < −1: keine Lösung. Höchstens ist die Gondel 13 + 10 = 23 m hoch.', 'Stelle nach cos x um.'))
ST.neu('anzahl', 'pruefung', L(f'Wie viele Lösungen haben die Gleichungen {B}? a) sin x = 0,9 b) cos x = −1 c) tan x = 7 d) 2 sin x = 3', 'a) □; b) □; c) □; d) □', [2, 1, 2, 0],
       ['2', '1', '2', '0'], 'a) |0,9| < 1: zwei. b) v = −1: eine (180°). c) Tangens: immer zwei. d) sin x = 1,5 > 1: keine.', 'Erst prüfen: Liegt v zwischen −1 und 1?'))
ST.knobel('anzahl', Z(f'Wie viele Lösungen hat (cos x)² = 0,25 {B}?', 4, '2 + 2',
          '(cos x)² = 0,25 heißt cos x = 0,5 oder cos x = −0,5. Jede der beiden Gleichungen hat zwei Lösungen: 60°, 300° und 120°, 240°. Zusammen 4.',
          'Welche Zahlen ergeben quadriert 0,25?'))
ST.knobel('anzahl', Z(f'Für wie viele ganze Zahlen a mit −5 ≤ a ≤ 5 hat a · sin x = 2 {B} genau zwei Lösungen?', 6, '6',
          'Für a = 0 steht 0 = 2 da: keine Lösung. Sonst sin x = 2 : a. Genau zwei Lösungen gibt es bei −1 < 2 : a < 1, also bei |a| > 2: a = ±3, ±4, ±5. Das sind 6 Zahlen. (a = ±2 ergibt sin x = ±1: nur eine Lösung.)',
          'Teile durch a. Was ist mit a = 0 und a = ±2?'))

# umformen
ST.stufenleiter('umformen', 'a · sin x = b durch Teilen auf sin x = v bringen und lösen.',
                'Erst Zahl auf die andere Seite, sin x auf beiden Seiten, Kolben, Zahl in der Gleichung rückwärts.',
                'Durch cos x teilen, Quadrate, Produkt gleich null, Fehler beim Umstellen, wann lösbar, mehrteilige Aufgabe.')
ST.typ('umformen', '/^/', 'direkt', s=1)
ST.typ('umformen', '/^/', 'mehrschritt', s=2)
ST.typ('umformen', '/· cos x = 0|\\(sin x\\)² = sin x/', 'transfer')
ST.typ('umformen', '/^/', 'verknuepfen', s=3)
ST.neu('umformen', 'erkennen', A('Was ist bei 4 sin x − 1 = 1 der erste Umformungsschritt?', 'auf beiden Seiten 1 addieren', ['durch sin teilen', 'sin⁻¹ auf die 4 anwenden', 'mit 4 multiplizieren'],
       'Erst die Zahl ohne sin wegschaffen: 4 sin x = 2. Dann durch 4 teilen: sin x = 0,5.', 'Wie bei einer linearen Gleichung.'))
ST.neu('umformen', 'umkehr', Z('Für welche Zahl c hat 2 sin x + c = 3 die Lösung x = 90°?', 1, '3 - 2',
       'sin 90° = 1, also 2 · 1 + c = 3 und c = 1.', 'Setze x = 90° ein.'))
ST.neu('umformen', 'einkleidung', L(f'Ein Kolben steht beim Drehwinkel x bei s = 5 + 4 · cos x (in cm). Bei welchen Winkeln {B} steht er bei 3 cm?', 'x₁ = □°; x₂ = □°', [120, 240], ['180 - 60', '360 - 120'],
       '5 + 4 cos x = 3 ⇒ 4 cos x = −2 ⇒ cos x = −0,5 ⇒ x = 120° oder x = 240°.', 'Stelle nach cos x um.', hinweis='kleinerer Winkel zuerst'))
ST.neu('umformen', 'fehler', A('Jemand löst 3 sin x + 2 = 5 so: sin x = 5 − 2 − 3 = 0, also x = 0° oder 180°. Was stimmt?', 'Falsch: 3 sin x = 3, also sin x = 1 und x = 90°.',
       ['Richtig.', 'Falsch: sin x = 7 : 3, keine Lösung.', 'Falsch: x = 30° oder 150°.'],
       'Die 3 ist ein Faktor und wird durch Teilen entfernt, nicht durch Abziehen: 3 sin x = 3 ⇒ sin x = 1.', 'Ist die 3 ein Summand oder ein Faktor?'))
ST.neu('umformen', 'parameter', A(f'Für welche Zahlen c hat 2 cos x + 3 = c {B} Lösungen?', 'für 1 ≤ c ≤ 5', ['für −1 ≤ c ≤ 1', 'für 0 ≤ c ≤ 3', 'für alle c'],
       'cos x = (c − 3) : 2 muss zwischen −1 und 1 liegen: −2 ≤ c − 3 ≤ 2, also 1 ≤ c ≤ 5.', 'Stelle nach cos x um.'))
ST.neu('umformen', 'pruefung', L(f'Löse {B}: a) 2 sin x + 3 = 4, b) 5 tan x = 5, c) 4 cos x = 4.', 'a) □° und □°; b) □° und □°; c) □°', [30, 150, 45, 225, 0],
       ['30', '180 - 30', '45', '45 + 180', '0'], 'a) sin x = 0,5: 30°, 150°. b) tan x = 1: 45°, 225°. c) cos x = 1: 0°.', 'Immer zuerst sin x, tan x oder cos x allein stellen.'))
ST.knobel('umformen', L(f'Löse (2 sin x − 1) · (sin x + 1) = 0 {B}.', 'x₁ = □°; x₂ = □°; x₃ = □°', [30, 150, 270], ['30', '180 - 30', '270'],
          'Ein Produkt ist null, wenn ein Faktor null ist. Erster Faktor: 2 sin x − 1 = 0, also sin x = 0,5 mit den Lösungen 30° und 180° − 30° = 150°. Zweiter Faktor: sin x + 1 = 0, also sin x = −1, die Gondel ganz unten: 270°. Zusammen drei Lösungen.',
          'Wann ist ein Produkt null?', hinweis='der Größe nach'))
ST.knobel('umformen', L(f'Löse (sin x)² = 3 · (cos x)² {B}.', 'x₁ = □°; x₂ = □°; x₃ = □°; x₄ = □°', [60, 120, 240, 300], ['60', '180 - 60', '180 + 60', '360 - 60'],
          'Teile durch (cos x)² (cos x = 0 ist keine Lösung, denn dann wäre auch sin x = 0): (tan x)² = 3, tan x = √3 oder tan x = −√3. tan x = √3: 60°, 240°. tan x = −√3: 120°, 300°.',
          'Teile durch (cos x)².', hinweis='der Größe nach'))

# anwendung
ST.stufenleiter('anwendung', 'Riesenrad-Höhe auf cos x = v umstellen und lösen.',
                'Hafen, Tageslänge, Pendel, Winkel im Dreieck über die Winkelsumme prüfen, Faktor aus einem Wert bestimmen.',
                'Größter oder stumpfer Winkel, Flächenformel, Drehwinkel-Bereiche, Fehler „nur eine Lösung“, Bedingung an α, mehrteilige Gondel-Aufgabe.')
ST.typ('anwendung', '/^/', 'direkt', s=1)
ST.typ('anwendung', '/^In einem Dreieck/', 'mehrschritt', s=2)
ST.typ('anwendung', '/^/', 'einkleidung', s=2)
ST.typ('anwendung', 'Die Wassertiefe', 'einkleidung', s=3)
ST.typ('anwendung', 'In einem Dreieck', 'verknuepfen', s=3)
ST.typ('anwendung', '/^/', 'transfer', s=3)
ST.neu('anwendung', 'erkennen', A('Im Dreieck gilt sin β = 0,6. Welche Winkel kommen für β zunächst in Frage?', 'etwa 36,9° und 143,1°', ['nur etwa 36,9°', 'etwa 36,9° und 323,1°', 'etwa 53,1° und 126,9°'],
       'sin⁻¹(0,6) ≈ 36,9°, dazu 180° − 36,9° = 143,1°. Ein Dreieckswinkel liegt zwischen 0° und 180°, darum kommt 323,1° nicht in Frage.', 'Zweite Lösung beim Sinus: 180° − x₁.'))
ST.neu('anwendung', 'direkt', L('Die Gondel eines Riesenrads ist h(x) = 15 − 10 · cos x Meter hoch (x Drehwinkel). Bei welchen Winkeln 0° ≤ x < 360° ist sie genau 15 m hoch?', 'x₁ = □°; x₂ = □°', [90, 270], ['90', '360 - 90'],
       '15 − 10 cos x = 15 ⇒ cos x = 0 ⇒ x = 90° oder x = 270°.', 'Stelle nach cos x um.', hinweis='kleinerer Winkel zuerst'))
ST.neu('anwendung', 'umkehr', Z('Die Wassertiefe ist t(x) = 8 + a · sin x (in m). Bei x = 90° ist das Wasser 11 m tief. Wie groß ist a?', 3, '11 - 8',
       'sin 90° = 1, also 8 + a = 11 und a = 3 m.', 'Setze x = 90° ein.', einheit='m'))
ST.neu('anwendung', 'fehler', A('In einem Dreieck ist α = 30° und sin β = 0,8. Jemand gibt nur β ≈ 53,1° an. Was stimmt?', 'Unvollständig: Auch β ≈ 126,9° passt, denn 30° + 126,9° < 180°.',
       ['Richtig, nur 53,1° ist möglich.', 'Falsch: nur 126,9° ist möglich.', 'Falsch: Es gibt kein solches Dreieck.'],
       'sin β = 0,8 ⇒ β ≈ 53,1° oder β ≈ 126,9°. Beide lassen mit α = 30° noch Platz für γ: γ ≈ 96,9° oder γ ≈ 23,1°.', 'Prüfe beide Winkel mit der Winkelsumme.'))
ST.neu('anwendung', 'parameter', A('In einem Dreieck ist sin β = 0,8, also β ≈ 53,1° oder β ≈ 126,9°. Für welche Winkel α sind beide Werte möglich?', 'für α < 53,1°', ['für α < 126,9°', 'für alle α', 'für α > 53,1°'],
       'Auch der stumpfe Wert muss passen: α + 126,9° < 180°, also α < 53,1°.', 'Wann hat der stumpfe Wert noch Platz?'))
ST.neu('anwendung', 'pruefung', L('Eine Gondel hat die Höhe h(x) = 25 − 20 · cos x (in m). a) Wie hoch ist sie bei x = 0°? b) Wie hoch ist sie höchstens? c) Bei welchen Winkeln 0° ≤ x < 360° ist sie 35 m hoch?',
       'a) □ m; b) □ m; c) □° und □°', [5, 45, 120, 240], ['25 - 20', '25 + 20', '180 - 60', '360 - 120'],
       'a) cos 0° = 1: 25 − 20 = 5 m. b) bei cos x = −1: 25 + 20 = 45 m. c) 25 − 20 cos x = 35 ⇒ cos x = −0,5 ⇒ 120° und 240°.', 'Für c) nach cos x umstellen.'))
ST.knobel('anwendung', Z('Die Tageslänge an einem Ort ist d(x) = 12 + 4 · sin x Stunden (x in Grad, 360° entsprechen einem Jahr). Über wie viele Grad des Jahres ist der Tag länger als 14 Stunden?', 120, '150 - 30',
          '12 + 4 sin x > 14 heißt sin x > 0,5. Die Grenzen sind 30° und 150°; dazwischen ist sin x größer als 0,5. Das sind 150° − 30° = 120°, also ein Drittel des Jahres.',
          'Bestimme erst, wann der Tag genau 14 Stunden lang ist.', einheit='°'))
ST.knobel('anwendung', Z('In einem Dreieck gilt sin α = 0,5 und sin β = 0,5. Wie groß ist γ?', 120, '180 - 30 - 30',
          'α und β sind jeweils 30° oder 150°. Zweimal 150° ist zu viel. 30° und 150° ergeben schon 180°, dann bleibt für γ nichts. Also α = β = 30° und γ = 120°.',
          'Probiere alle Paare aus 30° und 150°.', einheit='°'))

if __name__ == '__main__':
    stufen('gleichungen.trig', ST)


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('gleichungen.trig')
# ---- BEREINIGEN ENDE ----
