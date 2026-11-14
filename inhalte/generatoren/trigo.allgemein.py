#!/usr/bin/env python3
"""Thema trigo.allgemein – Allgemeine Trigonometrie: Einheitskreis, Sinus- und Kosinussatz, Flächenformel (Klasse 9)."""
import sys
from math import isqrt, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(912)
# ganzzahlige Dreiecke mit γ = 60° bzw. 120° (Kosinussatz geht glatt auf)
G60 = [(a, b, isqrt(a * a + b * b - a * b)) for a in range(2, 30) for b in range(a + 1, 30)
       if isqrt(a * a + b * b - a * b) ** 2 == a * a + b * b - a * b]
G120 = [(a, b, isqrt(a * a + b * b + a * b)) for a in range(2, 30) for b in range(a + 1, 30)
        if isqrt(a * a + b * b + a * b) ** 2 == a * a + b * b + a * b]
EXAKT = {0: (0, 1), 30: (Fr(1, 2), None), 90: (1, 0), 150: (Fr(1, 2), None), 180: (0, -1), 210: (Fr(-1, 2), None),
         270: (-1, 0), 330: (Fr(-1, 2), None), 60: (None, Fr(1, 2)), 120: (None, Fr(-1, 2)), 240: (None, Fr(-1, 2)), 300: (None, Fr(1, 2)), 360: (0, 1)}


def cf(x):
    return str(float(x)) if Fr(x).denominator != 1 else str(int(x))


ETAPPEN = [
    {'lernziel': 'einheitskreis', 'titel': 'Sinus und Kosinus am Einheitskreis',
     'regel': 'Am ⟦Einheitskreis⟧ (Radius 1) hat der Punkt zum Winkel α die Koordinaten ⟦(cos α | sin α)⟧. So sind sin und cos für alle Winkel von 0° bis 360° erklärt. Es gilt ⟦sin(180° − α) = sin α⟧ und ⟦cos(180° − α) = −cos α⟧.',
     'schritte': ['cos 120°: 120° = 180° − 60°.', 'cos 120° = −cos 60° = ⟦−0,5⟧ (der Punkt liegt links der y-Achse).'],
     'probe': 'sin 120° = sin 60° > 0: Punkt liegt oberhalb der x-Achse ✓',
     'fehler': '„cos 120° = 0,5, weil cos 60° = 0,5“ ist falsch: Für Winkel zwischen 90° und 180° ist der Kosinus ⟦negativ⟧.'},
    {'lernziel': 'flaeche', 'titel': 'Flächeninhalt mit dem Sinus',
     'regel': 'Kennt man zwei Seiten und den ⟦eingeschlossenen⟧ Winkel, gilt ⟦A = ½ · a · b · sin γ⟧ (entsprechend mit anderen Seiten und Winkeln).',
     'schritte': ['a = 6 cm, b = 9 cm, γ = 30°: A = ½ · 6 · 9 · sin 30°.', 'A = 27 · 0,5 = ⟦13,5 cm²⟧.'],
     'probe': 'Höhe auf b: h = a · sin γ = 3 cm; A = ½ · 9 · 3 = 13,5 ✓',
     'fehler': 'A = ½ · a · b ohne sin γ gilt nur für γ = 90°. Sonst ist ⟦a · sin γ⟧ die Höhe, nicht a selbst.'},
    {'lernziel': 'sinussatz_seite', 'titel': 'Sinussatz: Seite berechnen',
     'regel': 'In jedem Dreieck gilt der ⟦Sinussatz⟧: ⟦a : sin α = b : sin β = c : sin γ⟧. Kennst du zwei Winkel und eine Seite, berechnest du jede andere Seite.',
     'schritte': ['α = 40°, β = 75°, a = 8 cm. Gesucht b.', 'b = a · sin β : sin α = 8 · sin 75° : sin 40° ≈ ⟦12,0 cm⟧.'],
     'probe': 'Größerer Winkel β liegt gegenüber der größeren Seite b ✓',
     'fehler': 'b = 8 · sin 40° : sin 75° ist falsch: Zur Seite b gehört der ⟦gegenüberliegende⟧ Winkel β; er gehört in den Zähler.'},
    {'lernziel': 'sinussatz_winkel', 'titel': 'Sinussatz: Winkel berechnen',
     'regel': 'Aus ⟦sin β = b · sin α : a⟧ folgt β. Achtung: Zu einem Sinuswert gibt es zwei Winkel β und ⟦180° − β⟧. Ist die gegebene Gegenseite a die ⟦größere⟧ (a ≥ b), ist β eindeutig spitz.',
     'schritte': ['a = 10 cm, b = 7 cm, α = 50°: sin β = 7 · sin 50° : 10 ≈ 0,5362.', 'β ≈ 32,4° (180° − 32,4° = 147,6° ist zu groß, weil b < a): ⟦β ≈ 32,4°⟧.'],
     'probe': '50° + 32,4° < 180° ✓',
     'fehler': 'Immer nur den spitzen Winkel zu nehmen ist falsch: Ist b > a, kann auch ⟦180° − β⟧ passen – dann gibt es zwei Dreiecke.'},
    {'lernziel': 'kosinussatz_seite', 'titel': 'Kosinussatz: Seite berechnen',
     'regel': 'Kennt man zwei Seiten und den ⟦eingeschlossenen⟧ Winkel, gilt der ⟦Kosinussatz⟧: c² = a² + b² − 2ab · cos γ. Für γ = 90° ist das der Satz des Pythagoras.',
     'schritte': ['a = 5 cm, b = 8 cm, γ = 60°: c² = 25 + 64 − 2 · 5 · 8 · 0,5 = 49.', 'c = ⟦7 cm⟧.'],
     'probe': 'γ = 60° liegt zwischen den anderen Winkeln, c zwischen a und b ✓',
     'fehler': 'c² = 25 + 64 − 2 · 5 · 8 = 9 ist falsch: Der Faktor ⟦cos γ⟧ fehlt. Bei γ = 120° ist cos γ negativ, dann wird c² sogar größer.'},
    {'lernziel': 'kosinussatz_winkel', 'titel': 'Kosinussatz: Winkel berechnen',
     'regel': 'Sind ⟦alle drei Seiten⟧ bekannt, stellst du um: ⟦cos γ = (a² + b² − c²) : (2ab)⟧. Ein negativer Wert bedeutet einen ⟦stumpfen⟧ Winkel – hier ist die Lösung eindeutig.',
     'schritte': ['a = 3 cm, b = 5 cm, c = 7 cm: cos γ = (9 + 25 − 49) : 30 = −0,5.', 'γ = ⟦120°⟧ (stumpf).'],
     'probe': 'c ist die längste Seite, γ der größte Winkel ✓',
     'fehler': 'cos γ = (a² + b² + c²) : (2ab) ist falsch: Das Quadrat der ⟦gegenüberliegenden⟧ Seite wird ⟦subtrahiert⟧.'},
    {'lernziel': 'satz_waehlen', 'titel': 'Welcher Satz passt?',
     'regel': 'Gegeben ⟦SSS⟧ oder ⟦SWS⟧: Kosinussatz. Gegeben ⟦WSW/SWW⟧ oder ⟦SsW⟧ (Seite und Gegenwinkel bekannt): Sinussatz. Fehlt ein Winkel, hilft die ⟦Winkelsumme 180°⟧.',
     'schritte': ['Gegeben: a, b und γ (der Winkel zwischen a und b) – das ist SWS.', 'Erst c mit dem ⟦Kosinussatz⟧, danach die anderen Winkel.'],
     'probe': 'Für den Sinussatz bräuchte man ein Paar aus Seite und Gegenwinkel – das fehlt hier ✓',
     'fehler': 'Bei SWS den Sinussatz zu nehmen geht nicht: Zu keiner gegebenen Seite ist der ⟦gegenüberliegende⟧ Winkel bekannt.'},
]


def g_einheitskreis(s):
    if s == 1:
        w = R.choice([0, 30, 90, 150, 180, 210, 270, 330, 60, 120, 240, 300, 360])
        sn, cs = EXAKT[w]
        f, v = ('sin', sn) if sn is not None else ('cos', cs)
        if sn is not None and cs is not None and R.random() < 0.5: f, v = 'cos', cs
        return zahl(f'Gib den exakten Wert von {f} {w}° an.', f'Am Einheitskreis: {f} {w}° = {dz(v)}.',
                    'Wo liegt der Punkt zum Winkel auf dem Einheitskreis? Nutze 30°, 60° und die Symmetrie.', v, cf(v))
    if s == 2:
        typ = R.random()
        al = R.randint(5, 85)
        if typ < 0.4:
            return zahl(f'Welcher zweite Winkel zwischen 0° und 180° hat denselben Sinuswert wie {al}°?', f'sin(180° − α) = sin α: 180° − {al}° = {180 - al}°.',
                        'Spiegle am Einheitskreis an der y-Achse.', 180 - al, f'180 - {al}', einheit='°')
        if typ < 0.7:
            w = 180 - al
            return luecken(f'Ergänze: cos {w}° = −cos □°.', 'cos ' + str(w) + '° = −cos □°', 'Winkel in Grad', [al],
                           f'cos(180° − α) = −cos α mit α = {al}°: cos {w}° = −cos {al}°.', 'Schreibe den Winkel als 180° − α.', c=[f'180 - {w}'])
        w = R.choice(range(5, 356, 5))
        if w % 90 == 0: return None
        q = (w // 90) + 1
        f = R.choice(['sin', 'cos'])
        pos = (f == 'sin' and q in (1, 2)) or (f == 'cos' and q in (1, 4))
        return auswahl(f'Welches Vorzeichen hat {f} {w}°?', 'positiv' if pos else 'negativ', ['positiv', 'negativ', 'null'],
                       f'{w}° liegt im {q}. Quadranten; dort ist {"die y-" if f == "sin" else "die x-"}Koordinate {"positiv" if pos else "negativ"}.',
                       'In welchem Quadranten liegt der Punkt? sin = y-Koordinate, cos = x-Koordinate.')
    typ = R.random()
    if typ < 0.4:
        v = R.choice([Fr(1, 2), Fr(-1, 2)])
        f = R.choice(['sin', 'cos'])
        if f == 'sin':
            l = (30, 150) if v > 0 else (210, 330)
        else:
            l = (60, 300) if v > 0 else (120, 240)
        return luecken(f'Für welche Winkel zwischen 0° und 360° gilt {f} α = {dz(v)}?', 'α₁ = □°; α₂ = □°', 'kleinerer Winkel zuerst', list(l),
                       f'Am Einheitskreis gibt es zwei Punkte mit {"y" if f == "sin" else "x"}-Koordinate {dz(v)}: α = {l[0]}° und α = {l[1]}°.',
                       'Zeichne die waagrechte bzw. senkrechte Gerade durch den Wert und suche beide Schnittpunkte.', c=[str(l[0]), str(l[1])])
    if typ < 0.7:
        al = R.randint(91, 179)
        return auswahl(f'Jemand sagt: „cos {al}° ist positiv, weil {al}° ein Winkel im Dreieck sein kann.“ Was stimmt?',
                       f'Falsch: {al}° ist stumpf, der Punkt liegt links der y-Achse, cos {al}° < 0.',
                       ['Richtig.', f'Falsch: cos {al}° = 0.', f'Falsch: cos {al}° ist nicht definiert.'],
                       f'Für 90° < α < 180° ist die x-Koordinate am Einheitskreis negativ: cos {al}° = −cos {180 - al}° < 0.',
                       'Wo liegt der Punkt zu einem stumpfen Winkel am Einheitskreis?')
    al = R.randint(5, 85)
    return zahl(f'Es gilt sin {al}° ≈ {dz(round(sin(al), 4))}. Wie groß ist sin {180 + al}° (vier Nachkommastellen)?',
                f'Der Punkt zu {180 + al}° ist der am Ursprung gespiegelte Punkt zu {al}°: sin {180 + al}° = −sin {al}° ≈ {dz(-round(sin(al), 4))}.',
                'Punktspiegelung am Ursprung ändert das Vorzeichen beider Koordinaten.', -round(sin(al), 4), f'-{round(sin(al), 4)}')


def g_flaeche(s):
    a, b = R.randint(3, 15), R.randint(3, 15)
    if s == 1:
        g = R.choice([30, 150, 90])
        A = Fr(a * b, 2) * (Fr(1, 2) if g != 90 else 1)
        return zahl(f'Ein Dreieck hat a = {a} cm, b = {b} cm und den eingeschlossenen Winkel γ = {g}°. Berechne den Flächeninhalt.',
                    f'A = ½ · {a} · {b} · sin {g}° = {dz(Fr(a * b, 2))} · {dz(Fr(1, 2) if g != 90 else 1)} = {dz(A)} cm².', 'Formel A = ½ · a · b · sin γ; sin 30° = sin 150° = 0,5.',
                    A, f'0.5 * {a} * {b} * {"0.5" if g != 90 else "1"}', einheit='cm²')
    g = R.randint(20, 160)
    if s == 2:
        wahr = 0.5 * a * b * sin(g)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Ein Dreieck hat a = {a} cm, b = {b} cm und γ = {g}°. Berechne den Flächeninhalt (auf eine Nachkommastelle).',
                    f'A = ½ · {a} · {b} · sin {g}° ≈ {dz(v)} cm².', 'Zwei Seiten und der eingeschlossene Winkel.', v,
                    f'round(0.5 * {a} * {b} * {K(sin(g))}, 1)', einheit='cm²')
    if R.random() < 0.5:
        A = R.randint(10, 60)
        wahr = 2 * A / (a * sin(g))
        v = gerundet(wahr, 1)
        if v is None or wahr > 100: return None
        return zahl(f'Ein Dreieck hat den Flächeninhalt {A} cm², die Seite a = {a} cm und γ = {g}°. Wie lang ist b (auf eine Nachkommastelle)?',
                    f'{A} = ½ · {a} · b · sin {g}° ⇒ b = 2 · {A} : ({a} · sin {g}°) ≈ {dz(v)} cm.', 'Stelle die Flächenformel nach b um.', v,
                    f'round(2 * {A} / ({a} * {K(sin(g))}), 1)', einheit='cm')
    w = R.randint(30, 150)
    wahr = a * b * sin(w)
    v = gerundet(wahr, 1)
    if v is None: return None
    return zahl(f'Ein Parallelogramm hat die Seiten {a} cm und {b} cm, die einen Winkel von {w}° einschließen. Berechne den Flächeninhalt (auf eine Nachkommastelle).',
                f'Die Diagonale teilt es in zwei gleiche Dreiecke: A = 2 · ½ · {a} · {b} · sin {w}° ≈ {dz(v)} cm².', 'Ein Parallelogramm besteht aus zwei kongruenten Dreiecken.',
                v, f'round({a} * {b} * {K(sin(w))}, 1)', einheit='cm²')


def g_sinussatz_seite(s):
    al, be = R.randint(20, 100), R.randint(20, 100)
    ga = 180 - al - be
    if ga < 10: return None
    a = R.randint(3, 15)
    if s == 1:
        wahr = a * sin(be) / sin(al)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Im Dreieck ABC ist α = {al}°, β = {be}° und a = {a} cm. Berechne b (auf eine Nachkommastelle).',
                    f'b : sin β = a : sin α ⇒ b = {a} · sin {be}° : sin {al}° ≈ {dz(v)} cm.', 'Sinussatz: Seite und Gegenwinkel bilden ein Paar.', v,
                    f'round({a} * {K(sin(be))} / {K(sin(al))}, 1)', einheit='cm')
    wahr = a * sin(ga) / sin(al)
    v = gerundet(wahr, 1)
    if v is None: return None
    if s == 2:
        return zahl(f'Im Dreieck ABC ist α = {al}°, β = {be}° und a = {a} cm. Berechne c (auf eine Nachkommastelle).',
                    f'γ = 180° − {al}° − {be}° = {ga}°. c = {a} · sin {ga}° : sin {al}° ≈ {dz(v)} cm.', 'Berechne zuerst γ mit der Winkelsumme.', v,
                    f'round({a} * {K(sin(ga))} / {K(sin(al))}, 1)', einheit='cm')
    d = R.randint(50, 400)
    wahr = d * sin(be) / sin(ga)
    v = gerundet(wahr, 0)
    if v is None: return None
    return zahl(f'Zwei Beobachter A und B stehen {d} m voneinander entfernt. Sie sehen einen Baum C auf der anderen Seite eines Sees unter den Winkeln α = {al}° (bei A) und β = {be}° (bei B) zur Strecke AB. Wie weit ist der Baum von A entfernt (auf ganze Meter)?',
                f'γ = 180° − {al}° − {be}° = {ga}°. AC = b = {d} · sin {be}° : sin {ga}° ≈ {dz(v)} m.', 'AC liegt gegenüber von β; AB liegt gegenüber von γ.', v,
                f'round({d} * {K(sin(be))} / {K(sin(ga))}, 0)', einheit='m')


def g_sinussatz_winkel(s):
    al = R.randint(25, 70)
    a = R.randint(6, 15)
    if s < 3:
        b = R.randint(3, a - 1)
        x = b * sin(al) / a
        wahr = asin(x)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Im Dreieck ABC ist a = {a} cm, b = {b} cm und α = {al}°. Berechne β (auf eine Nachkommastelle).',
                    f'sin β = {b} · sin {al}° : {a} ≈ {dz(round(x, 4))}; β ≈ {dz(v)}° (eindeutig, weil b < a).', 'Sinussatz nach sin β umstellen, dann sin⁻¹.', v,
                    f'round({K(wahr)}, 1)', einheit='°')
    b = R.randint(a + 1, a + 8)
    x = b * sin(al) / a
    if R.random() < 0.6:
        n = 'zwei Dreiecke' if x < 1 else 'genau ein Dreieck' if abs(x - 1) < 1e-9 else 'kein Dreieck'
        if n != 'zwei Dreiecke' and x < 1: return None
        return auswahl(f'Gegeben a = {a} cm, b = {b} cm, α = {al}°. Wie viele Dreiecke gibt es?', n, ['zwei Dreiecke', 'genau ein Dreieck', 'kein Dreieck'],
                       f'sin β = {b} · sin {al}° : {a} ≈ {dz(round(x, 4))}' + (f' < 1, und weil b > a passen β und 180° − β: zwei Dreiecke.' if x < 1 else ' > 1: kein Winkel möglich, kein Dreieck.'),
                       'Berechne sin β. Ist der Wert kleiner als 1? Ist die gegebene Gegenseite a die kleinere?')
    if x >= 1: return None
    b1 = asin(x)
    b2 = 180 - b1
    if al + b2 >= 180: return None
    v = gerundet(b2, 1)
    if v is None: return None
    return zahl(f'Gegeben a = {a} cm, b = {b} cm, α = {al}°. Es gibt zwei Dreiecke. Berechne den stumpfen Winkel β (auf eine Nachkommastelle).',
                f'sin β ≈ {dz(round(x, 4))}: β₁ ≈ {dz(round(b1, 1))}°, β₂ = 180° − β₁ ≈ {dz(v)}° (und {al}° + {dz(v)}° < 180°).',
                'Zu einem Sinuswert gibt es β und 180° − β.', v, f'round(180 - {K(b1)}, 1)', einheit='°')


def g_kosinussatz_seite(s):
    if s < 3 and R.random() < 0.7:
        g, (a, b, c) = (60, R.choice(G60)) if s == 1 or R.random() < 0.5 else (120, R.choice(G120))
        if R.random() < 0.5: a, b = b, a
        cs = Fr(1, 2) if g == 60 else Fr(-1, 2)
        return zahl(f'Im Dreieck ABC ist a = {a} cm, b = {b} cm und γ = {g}°. Berechne c.',
                    f'c² = {a}² + {b}² − 2 · {a} · {b} · cos {g}° = {a * a} + {b * b} {"−" if g == 60 else "+"} {a * b} = {c * c}, c = {c} cm.',
                    f'Kosinussatz; cos {g}° = {dz(cs)}.', c, f'({a} ** 2 + {b} ** 2 - 2 * {a} * {b} * ({cf(cs)})) / {c}', einheit='cm')
    a, b, g = R.randint(3, 15), R.randint(3, 15), R.randint(20, 160)
    wahr = sqrt(a * a + b * b - 2 * a * b * cos(g))
    v = gerundet(wahr, 1)
    if v is None: return None
    if s == 3 and R.random() < 0.5:
        return zahl(f'Ein Schiff fährt {a} km nach Osten, dreht dann um {180 - g}° nach links und fährt {b} km weiter. Wie weit ist es vom Start entfernt (auf eine Nachkommastelle)?',
                    f'Der Winkel im Dreieck am Wendepunkt ist 180° − {180 - g}° = {g}°. d² = {a}² + {b}² − 2 · {a} · {b} · cos {g}°, d ≈ {dz(v)} km.',
                    'Skizze! Der Innenwinkel am Wendepunkt ist 180° minus Drehwinkel.', v,
                    f'round({K(wahr)}, 1)', einheit='km')
    return zahl(f'Im Dreieck ABC ist a = {a} cm, b = {b} cm und γ = {g}°. Berechne c (auf eine Nachkommastelle).',
                f'c² = {a * a} + {b * b} − 2 · {a} · {b} · cos {g}° ≈ {dz(round(wahr * wahr, 2))}, c ≈ {dz(v)} cm.', 'Kosinussatz mit dem eingeschlossenen Winkel γ.', v,
                f'round({K(wahr)}, 1)', einheit='cm')


def g_kosinussatz_winkel(s):
    if s < 3 and R.random() < 0.6:
        g, (a, b, c) = (60, R.choice(G60)) if R.random() < 0.5 else (120, R.choice(G120))
        if R.random() < 0.5: a, b = b, a
        return zahl(f'Ein Dreieck hat die Seiten a = {a} cm, b = {b} cm, c = {c} cm. Berechne γ.',
                    f'cos γ = ({a * a} + {b * b} − {c * c}) : (2 · {a} · {b}) = {dz(Fr(a * a + b * b - c * c, 2 * a * b))} ⇒ γ = {g}°.',
                    'Das Quadrat der Gegenseite von γ wird subtrahiert.', g,
                    f'90 - 60 * (({a} ** 2 + {b} ** 2 - {c} ** 2) / (2 * {a} * {b}))', einheit='°')
    a, b = R.randint(3, 15), R.randint(3, 15)
    c = R.randint(abs(a - b) + 1, a + b - 1)
    x = (a * a + b * b - c * c) / (2 * a * b)
    wahr = acos(x)
    v = gerundet(wahr, 1)
    if v is None: return None
    if s == 3 and R.random() < 0.5:
        return zahl(f'Ein dreieckiges Grundstück hat die Seiten {a * 10} m, {b * 10} m und {c * 10} m. Wie groß ist der Winkel gegenüber der {c * 10}-m-Seite (auf eine Nachkommastelle)?',
                    f'cos γ = ({a * 10}² + {b * 10}² − {c * 10}²) : (2 · {a * 10} · {b * 10}) ≈ {dz(round(x, 4))} ⇒ γ ≈ {dz(v)}°.',
                    'Kosinussatz nach cos γ umstellen; γ liegt gegenüber der genannten Seite.', v, f'round({K(wahr)}, 1)', einheit='°')
    return zahl(f'Ein Dreieck hat die Seiten a = {a} cm, b = {b} cm, c = {c} cm. Berechne γ (auf eine Nachkommastelle).',
                f'cos γ = ({a * a} + {b * b} − {c * c}) : {2 * a * b} ≈ {dz(round(x, 4))} ⇒ γ ≈ {dz(v)}°.', 'Kosinussatz nach cos γ umstellen, dann cos⁻¹.', v,
                f'round({K(wahr)}, 1)', einheit='°')


def g_satz_waehlen(s):
    typen = [
        ('a, b und c', 'Kosinussatz', 'SSS: Alle drei Seiten sind bekannt, aber kein Winkel – Kosinussatz nach dem Winkel umstellen.'),
        ('a, b und γ', 'Kosinussatz', 'SWS: γ liegt zwischen a und b; zu keiner Seite ist der Gegenwinkel bekannt – Kosinussatz.'),
        ('b, c und α', 'Kosinussatz', 'SWS: α liegt zwischen b und c – Kosinussatz.'),
        ('a, α und β', 'Sinussatz', 'Seite a mit Gegenwinkel α bekannt – Sinussatz.'),
        ('c, α und β', 'Sinussatz', 'WSW: γ über die Winkelsumme, dann c mit Gegenwinkel γ – Sinussatz.'),
        ('a, b und α', 'Sinussatz', 'SsW: Seite a mit Gegenwinkel α bekannt – Sinussatz (auf Mehrdeutigkeit achten).'),
        ('b, c und β', 'Sinussatz', 'SsW: b mit Gegenwinkel β bekannt – Sinussatz.'),
        ('a, c und β', 'Kosinussatz', 'SWS: β liegt zwischen a und c – Kosinussatz.'),
        ('b, α und γ', 'Sinussatz', 'WSW: β über die Winkelsumme, dann b mit Gegenwinkel β – Sinussatz.'),
    ]
    if s < 3:
        geg, r, w = R.choice(typen)
        ziel = R.choice(['eine fehlende Seite', 'einen fehlenden Winkel'])
        return auswahl(f'Im Dreieck ABC sind {geg} gegeben. Mit welchem Satz beginnst du, um {ziel} zu berechnen?', r,
                       ['Sinussatz', 'Kosinussatz', 'Satz des Pythagoras', 'Flächenformel'], w,
                       'Gibt es ein bekanntes Paar aus Seite und gegenüberliegendem Winkel?')
    typ = R.random()
    if typ < 0.5:
        a, b, g = R.randint(3, 12), R.randint(3, 12), R.randint(30, 150)
        return auswahl(f'Gegeben a = {a} cm, b = {b} cm, γ = {g}°. Jemand will c mit dem Sinussatz berechnen. Was stimmt?',
                       'Das geht nicht direkt: Es fehlt ein Paar Seite/Gegenwinkel. Erst c mit dem Kosinussatz.',
                       ['Das geht: c = a · sin γ : sin α.', 'Das geht nur, wenn γ = 90° ist.', 'Man braucht dafür die Flächenformel.'],
                       f'Bekannt sind a, b und der eingeschlossene Winkel γ (SWS). Zu a und b fehlen α und β – der Sinussatz lässt sich nicht ansetzen.',
                       'Welche Größen braucht der Sinussatz?')
    a, b, c = sorted(R.sample(range(3, 15), 3))
    if a + b <= c: return None
    x = (a * a + b * b - c * c) / (2 * a * b)
    stumpf = x < 0
    return auswahl(f'Ein Dreieck hat die Seiten {a} cm, {b} cm und {c} cm. Ist der größte Winkel spitz, recht oder stumpf?',
                   'stumpf' if stumpf else 'recht' if x == 0 else 'spitz', ['spitz', 'recht', 'stumpf'],
                   f'Der größte Winkel liegt gegenüber {c} cm: cos γ = ({a * a} + {b * b} − {c * c}) : {2 * a * b} = {br(Fr(a * a + b * b - c * c, 2 * a * b))}'
                   + (' < 0: stumpf.' if stumpf else ' = 0: recht.' if x == 0 else ' > 0: spitz.'),
                   'Vorzeichen von a² + b² − c² für die längste Seite c entscheidet.')


GEN = {'einheitskreis': g_einheitskreis, 'flaeche': g_flaeche, 'sinussatz_seite': g_sinussatz_seite, 'sinussatz_winkel': g_sinussatz_winkel,
       'kosinussatz_seite': g_kosinussatz_seite, 'kosinussatz_winkel': g_kosinussatz_winkel, 'satz_waehlen': g_satz_waehlen}

if __name__ == '__main__':
    bauen('trigo.allgemein',
          'Sinus und Kosinus am Einheitskreis deuten und in beliebigen Dreiecken mit Sinussatz, Kosinussatz und Flächenformel rechnen.',
          ['Einheitskreis: Punkt (cos α | sin α); sin(180° − α) = sin α, cos(180° − α) = −cos α.', 'A = ½ · a · b · sin γ.',
           'Sinussatz: a : sin α = b : sin β = c : sin γ (Seite mit Gegenwinkel).', 'Kosinussatz: c² = a² + b² − 2ab · cos γ (SSS, SWS).'],
          [('Einheitskreis und Fläche', ['einheitskreis', 'flaeche']), ('Sinussatz', ['sinussatz_seite', 'sinussatz_winkel']),
           ('Kosinussatz', ['kosinussatz_seite', 'kosinussatz_winkel']), ('Strategie', ['satz_waehlen'])],
          ETAPPEN, GEN,
          meiden={'einheitskreis': ['cos 120°'], 'flaeche': ['a = 6 cm, b = 9 cm und den eingeschlossenen Winkel γ = 30°'],
                  'sinussatz_seite': ['α = 40°, β = 75° und a = 8 cm'], 'sinussatz_winkel': ['a = 10 cm, b = 7 cm und α = 50°'],
                  'kosinussatz_seite': ['a = 5 cm, b = 8 cm und γ = 60°'], 'kosinussatz_winkel': ['a = 3 cm, b = 5 cm, c = 7 cm']},
          offen=['Lernkarte „einheitskreis“ braucht Zeichnung: Einheitskreis mit Punkt (cos α | sin α), Quadranten und Spiegelungen. Bisher nur in Worten und über Werte.',
                 'Lernkarten zu Sinus-/Kosinussatz brauchen eine Dreieckskizze mit Standardbezeichnung (a gegenüber α usw.); Anwendungsaufgaben (See, Schiff, Grundstück) würden von einer Skizze stark profitieren.',
                 'Additionstheoreme (im „umfang“ der Themenliste genannt) sind bewusst weggelassen: Der LehrplanPLUS-Eintrag dieses Themas nennt nur Sinus- und Kosinussatz; Additionstheoreme gehören nicht zum Stoff der 9. Klasse. Bitte bei der Prüfung bestätigen.',
                 'Rechenausdruck c: Winkelfunktionswerte als 12-stellige Konstanten (Prüfskript kennt sin/cos nicht).'])
