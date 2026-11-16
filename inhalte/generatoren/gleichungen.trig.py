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

if __name__ == '__main__':
    bauen('gleichungen.trig',
          'Winkel zu einem gegebenen Sinus-, Kosinus- oder Tangenswert bestimmen und die Mehrdeutigkeit im Bereich 0° bis 360° beachten.',
          ['sin x = v: x₂ = 180° − x₁. cos x = v: x₂ = 360° − x₁. tan x = v: x₂ = x₁ + 180°.', '|v| > 1 bei sin/cos: keine Lösung; v = ±1: eine Lösung.',
           'Negative Ergebnisse des Taschenrechners in den Bereich 0°–360° verschieben.', 'Im Dreieck: Winkelsumme prüfen.'],
          [('Grundgleichungen', ['sinus', 'kosinus', 'tangens']), ('Lösbarkeit und Umformen', ['anzahl', 'umformen']), ('Anwenden', ['anwendung'])],
          ETAPPEN, GEN,
          meiden={'sinus': ['sin x = 0,5 '], 'kosinus': ['cos x = −0,5 '], 'tangens': ['tan x = 1 '], 'anzahl': ['cos x = −1 '],
                  'umformen': ['4 sin x + 1 = 3'], 'anwendung': ['α = 40° und sin β = 0,5']},
          offen=['Lernkarten „sinus“, „kosinus“, „anzahl“ zeigen jetzt die Graphen mit der Geraden y = v; Aufgaben mit Graph gibt es bei „anzahl“. Für den Tangens gibt es noch keinen Graphentyp (Vorschlag der Prüfung: „tan“ ergänzen).',
                 'Lösungsbereich durchgängig 0° ≤ x < 360°; Bogenmaß ist nicht enthalten (gehört nicht zur 9. Klasse).'])
