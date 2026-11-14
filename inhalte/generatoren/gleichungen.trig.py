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


def schab(n):
    return 'x = □°' if n == 1 else 'x₁ = □°; x₂ = □°'


ETAPPEN = [
    {'lernziel': 'sinus', 'titel': 'Gleichungen sin x = v',
     'regel': 'sin x ist die ⟦y-Koordinate⟧ am Einheitskreis. Für −1 < v < 1 gibt es zwei Lösungen: x₁ = sin⁻¹(v) und ⟦x₂ = 180° − x₁⟧ (bei negativem v auf den Bereich 0°–360° umrechnen).',
     'schritte': ['sin x = 0,5: Taschenrechner liefert x₁ = 30°.', 'Zweite Lösung: 180° − 30° = 150°. Also ⟦x₁ = 30°, x₂ = 150°⟧.'],
     'probe': 'sin 150° = sin 30° = 0,5 ✓',
     'fehler': 'Nur x = 30° anzugeben ist unvollständig: Die Gerade y = 0,5 schneidet den Einheitskreis ⟦zweimal⟧, auch bei 150°.'},
    {'lernziel': 'kosinus', 'titel': 'Gleichungen cos x = v',
     'regel': 'cos x ist die ⟦x-Koordinate⟧ am Einheitskreis. Für −1 < v < 1: x₁ = cos⁻¹(v) liegt zwischen 0° und 180°, die zweite Lösung ist ⟦x₂ = 360° − x₁⟧.',
     'schritte': ['cos x = −0,5: Taschenrechner liefert x₁ = 120°.', 'x₂ = 360° − 120° = 240°. Also ⟦x₁ = 120°, x₂ = 240°⟧.'],
     'probe': 'cos 240° = −0,5 ✓',
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


def g_exakt(f, s):
    v = R.choice(list(TAB[f]))
    l = TAB[f][v]
    if s == 1 and len(l) == 1: return None
    return luecken(f'Löse {f} x = {dz(v)} {B}.', schab(len(l)), 'kleinere Lösung zuerst' if len(l) > 1 else 'die Lösung', l,
                   f'Besondere Werte am Einheitskreis: {f} x = {dz(v)} für ' + ' und '.join(f'{t}°' for t in l) + '.',
                   'Nutze die besonderen Werte (0°, 30°, 45°, 60°, 90°) und die Symmetrie am Einheitskreis.', c=[str(t) for t in l])


def g_allg(f, s, welche):
    v = Fr(R.randint(-95, 95), 100)
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
                f'{f}⁻¹({dz(v)}) ≈ {dz(round({"sin": asin, "cos": acos, "tan": atan}[f](float(v)), 1))}°; Lösungen ≈ {dz(gerundet(l[0], 1))}° und {dz(gerundet(l[1], 1))}°. {welche.capitalize()}: {dz(w_)}°.',
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


def g_sinus(s):
    if s == 1: return g_exakt('sin', s) if R.random() < 0.3 else g_zweite('sin')
    return g_allg('sin', s, R.choice(['kleinere', 'größere'])) if s == 3 or R.random() < 0.5 else g_exakt('sin', s)


def g_kosinus(s):
    if s == 1: return g_exakt('cos', s) if R.random() < 0.3 else g_zweite('cos')
    return g_allg('cos', s, R.choice(['kleinere', 'größere'])) if s == 3 or R.random() < 0.5 else g_exakt('cos', s)


def g_tangens(s):
    if s == 1: return g_exakt('tan', s) if R.random() < 0.3 else g_zweite('tan')
    if s == 2 and R.random() < 0.4: return g_exakt('tan', s)
    if R.random() < 0.6:
        return g_allg('tan', s, R.choice(['kleinere', 'größere']))
    v = R.randint(2, 30) * R.choice([1, -1])
    l = loes('tan', v)
    w_ = gerundet(l[1], 1)
    if w_ is None: return None
    return zahl(f'Löse tan x = {dz(v)} {B}. Gib die größere Lösung auf eine Nachkommastelle an.',
                f'tan⁻¹({dz(v)}) ≈ {dz(round(atan(v), 1))}°; Lösungen ≈ {dz(gerundet(l[0], 1))}° und {dz(w_)}°.',
                'Zweite Lösung über x₁ + 180°; negative Werte erst in den Bereich verschieben.', w_, f'round({K(l[1])}, 1)', einheit='°')


def g_anzahl(s):
    f = R.choice(['sin', 'cos', 'tan'])
    if s == 1:
        v = R.choice([Fr(R.randint(11, 30), 10), Fr(-R.randint(11, 30), 10), Fr(R.randint(1, 9), 10), Fr(-R.randint(1, 9), 10)])
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
                 f'Die Gerade schneidet den Einheitskreis zweimal: zwei Lösungen.')
        return auswahl(f'Wie viele Lösungen hat {f} x = {dz(v)} {B}?', txt[n], list(txt.values()), grund,
                       'Liegt der Wert zwischen −1 und 1? Ist er genau ±1? Beim Tangens ist alles erlaubt.')
    typ = R.random()
    if typ < 0.5:
        v = Fr(R.randint(11, 25), 10)
        g = R.choice(['sin', 'cos'])
        return auswahl(f'Jemand löst {g} x = {dz(v)} und schreibt x ≈ {dz(round(v * 30, 1))}°. Was stimmt?', f'Falsch: {g} x ≤ 1, die Gleichung hat keine Lösung.',
                       ['Richtig.', f'Falsch: x ≈ {dz(round(v * 60, 1))}°.', 'Falsch: Es gibt unendlich viele Lösungen.'],
                       f'Am Einheitskreis sind Sinus und Kosinus Koordinaten, also höchstens 1. {dz(v)} > 1 ist unmöglich.',
                       'Welche Werte kann sin x bzw. cos x annehmen?')
    v = R.choice([Fr(1), Fr(-1)])
    g = R.choice(['sin', 'cos'])
    l = TAB[g][v]
    zweite = (l[0] + 180) % 360
    return auswahl(f'Jemand gibt für {g} x = {dz(v)} {B} die Lösungen {l[0]}° und {zweite}° an. Was stimmt?',
                   f'Falsch: Es gibt nur die Lösung {l[0]}°.',
                   ['Richtig.', 'Falsch: Es gibt keine Lösung.', f'Falsch: Nur {zweite}° ist Lösung.'],
                   f'{g} {zweite}° = {dz(-v)} ≠ {dz(v)}. Der Wert {dz(v)} ist ein Extremwert; nur ein Punkt am Einheitskreis hat diese Koordinate: x = {l[0]}°.',
                   'Setze beide Winkel zur Probe ein.')


def g_umformen(s):
    f = R.choice(['sin', 'cos'] if s < 3 else ['sin', 'cos', 'tan'])
    v = R.choice([x for x in TAB[f] if (s > 1 or len(TAB[f][x]) == 2)])
    l = TAB[f][v]
    a = R.randint(2, 6)
    b = R.randint(-9, 9)
    if s == 1:
        b = 0
    rechts = a * v + b
    if rechts.denominator != 1: return None
    if s == 3 and R.random() < 0.4:
        if f == 'tan': return None
        return luecken(f'Löse sin x = cos x {B}.', schab(2), 'kleinere Lösung zuerst', [45, 225],
                       'Durch cos x teilen (cos x ≠ 0): tan x = 1 ⇒ x₁ = 45°, x₂ = 225°.', 'Teile beide Seiten durch cos x.', c=['45', '45 + 180']) if R.random() < 0.5 else \
            luecken(f'Löse sin x = −cos x {B}.', schab(2), 'kleinere Lösung zuerst', [135, 315],
                    'Durch cos x teilen: tan x = −1 ⇒ x₁ = 135°, x₂ = 315°.', 'Teile beide Seiten durch cos x.', c=['180 - 45', '360 - 45'])
    t = f'Löse {a} {f} x {plus(b) if b else ""}'.rstrip() + f' = {dz(rechts)} {B}.'
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
        al = R.randint(20, 120)
        v = Fr(R.randint(20, 95), 100)
        b1 = asin(float(v))
        b2 = 180 - b1
        moegl = [b for b in (b1, b2) if al + b < 180 - 1e-9]
        n = len(moegl)
        txt = {1: 'genau ein Winkel', 2: 'zwei Winkel', 0: 'kein Winkel'}
        return auswahl(f'In einem Dreieck ist α = {al}° und sin β = {dz(v)}. Wie viele Werte kommen für β in Frage?', txt[n], list(txt.values()),
                       f'sin β = {dz(v)} ⇒ β ≈ {dz(round(b1, 1))}° oder β ≈ {dz(round(b2, 1))}°. ' +
                       ' '.join(f'{al}° + {dz(round(b, 1))}° {"<" if al + b < 180 else "≥"} 180°.' for b in (b1, b2)) + f' Also {txt[n]}.',
                       'Bestimme beide Winkel zum Sinuswert und prüfe die Winkelsumme.')
    al = R.randint(20, 60)
    v = Fr(R.randint(20, 95), 100)
    b1, b2 = asin(float(v)), 180 - asin(float(v))
    if al + b2 >= 180: return None
    w_ = gerundet(b2, 1)
    if w_ is None: return None
    return zahl(f'In einem Dreieck ist α = {al}° und sin β = {dz(v)}; außerdem ist β stumpf. Berechne β (auf eine Nachkommastelle).',
                f'β₁ = sin⁻¹({dz(v)}) ≈ {dz(round(b1, 1))}° ist spitz; stumpf: β = 180° − β₁ ≈ {dz(w_)}° (Winkelsumme: {al}° + {dz(w_)}° < 180° ✓).',
                'Zu einem Sinuswert gibt es einen spitzen und einen stumpfen Winkel.', w_, f'round(180 - {K(b1)}, 1)', einheit='°')


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
          offen=['Alle Lernkarten brauchen den Einheitskreis bzw. die Graphen von sin, cos, tan als Zeichnung (waagrechte Gerade y = v schneidet den Kreis/Graphen). Bisher nur in Worten.',
                 'Lösungsbereich durchgängig 0° ≤ x < 360°; Bogenmaß ist nicht enthalten (gehört nicht zur 9. Klasse).'])
