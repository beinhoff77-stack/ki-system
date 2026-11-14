#!/usr/bin/env python3
"""Thema trigo.rechtwinklig – Trigonometrie im rechtwinkligen Dreieck (Klasse 9)."""
import sys
from math import isqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(911)
TRIPEL = sorted({(a, b, c) for a in range(1, 80) for b in range(1, 80)
                 for c in [isqrt(a * a + b * b)] if c * c == a * a + b * b and c <= 100 and a != b})
FUNK = {'sin': sin, 'cos': cos, 'tan': tan}


def cf(x):
    return str(float(x)) if Fr(x).denominator != 1 else str(int(x))


ETAPPEN = [
    {'lernziel': 'seiten', 'titel': 'Ankathete, Gegenkathete, Hypotenuse',
     'regel': 'Im rechtwinkligen Dreieck liegt die ⟦Hypotenuse⟧ dem rechten Winkel gegenüber. Bezogen auf einen spitzen Winkel ist die ⟦Gegenkathete⟧ die Kathete gegenüber, die ⟦Ankathete⟧ die Kathete, die am Winkel anliegt.',
     'schritte': ['Dreieck ABC mit γ = 90°: Hypotenuse ist c (gegenüber C).', 'Für α (bei A): Gegenkathete ⟦a⟧, Ankathete ⟦b⟧.'],
     'probe': 'Für β tauschen An- und Gegenkathete: Gegenkathete b, Ankathete a ✓',
     'fehler': '„Die Ankathete von α ist c, weil c an A anliegt“ ist falsch: c liegt zwar an A, ist aber die ⟦Hypotenuse⟧. Ankathete ist nur eine ⟦Kathete⟧.'},
    {'lernziel': 'verhaeltnisse', 'titel': 'Sinus, Kosinus, Tangens als Verhältnis',
     'regel': '⟦sin α = Gegenkathete : Hypotenuse⟧, ⟦cos α = Ankathete : Hypotenuse⟧, ⟦tan α = Gegenkathete : Ankathete⟧.',
     'schritte': ['γ = 90°, a = 8 cm, b = 15 cm, c = 17 cm.', 'sin α = 8/17, cos α = 15/17, ⟦tan α = 8/15⟧.'],
     'probe': 'sin α und cos α sind kleiner als 1 (Hypotenuse ist am längsten) ✓',
     'fehler': 'sin α = b/c ist falsch, wenn γ = 90°: b ist die ⟦Ankathete⟧ von α. Richtig: sin α = a/c.'},
    {'lernziel': 'seite', 'titel': 'Seitenlängen berechnen',
     'regel': 'Wähle die Funktion, in der die ⟦gesuchte und die bekannte Seite⟧ vorkommen. Stelle um, z. B. ⟦a = c · sin α⟧ oder ⟦c = a : sin α⟧.',
     'schritte': ['γ = 90°, α = 35°, c = 10 cm, gesucht a (Gegenkathete von α).', 'a = 10 cm · sin 35° ≈ 10 · 0,5736 ≈ ⟦5,7 cm⟧.'],
     'probe': 'a < c ✓',
     'fehler': 'a = 10 : sin 35° ≈ 17,4 cm ist falsch: Aus sin α = a/c folgt a = ⟦c · sin α⟧. Eine Kathete kann nicht länger als die Hypotenuse sein.'},
    {'lernziel': 'winkel', 'titel': 'Winkel berechnen',
     'regel': 'Kennst du zwei Seiten, berechnest du das Verhältnis und benutzt die ⟦Umkehrtaste⟧: α = sin⁻¹(…), cos⁻¹(…) oder tan⁻¹(…). Der Taschenrechner muss auf ⟦DEG⟧ stehen.',
     'schritte': ['γ = 90°, a = 4 cm, b = 7 cm: tan α = 4/7 ≈ 0,5714.', 'α = tan⁻¹(4/7) ≈ ⟦29,7°⟧.'],
     'probe': 'β = 90° − 29,7° = 60,3°; tan 60,3° ≈ 1,75 = 7/4 ✓',
     'fehler': 'α = 4/7 ≈ 0,57° ist falsch: 4/7 ist der ⟦Tangenswert⟧, nicht der Winkel. Erst tan⁻¹ liefert den Winkel.'},
    {'lernziel': 'beziehungen', 'titel': 'Beziehungen zwischen sin, cos, tan',
     'regel': 'Für spitze Winkel gilt: ⟦sin² α + cos² α = 1⟧, ⟦tan α = sin α : cos α⟧ und ⟦sin α = cos(90° − α)⟧. Besondere Werte: sin 30° = cos 60° = 0,5; tan 45° = 1.',
     'schritte': ['sin α = 0,28 (α spitz): cos² α = 1 − 0,0784 = 0,9216.', 'cos α = ⟦0,96⟧, tan α = 0,28 : 0,96 = 7/24.'],
     'probe': '0,28² + 0,96² = 0,0784 + 0,9216 = 1 ✓',
     'fehler': 'cos α = 1 − sin α = 0,72 ist falsch: Es gilt sin² α + cos² α = 1 – mit den ⟦Quadraten⟧.'},
    {'lernziel': 'anwendung', 'titel': 'Trigonometrie anwenden',
     'regel': 'Skizze, ⟦rechtwinkliges Dreieck⟧ finden, Winkel und Seiten zuordnen. ⟦Steigung in %⟧ = tan(Steigungswinkel) · 100. ⟦Höhenwinkel⟧ wird von der Waagrechten aus gemessen.',
     'schritte': ['Eine Straße steigt mit 8 %: tan α = 0,08.', 'α = tan⁻¹(0,08) ≈ ⟦4,6°⟧.'],
     'probe': '8 m Höhe auf 100 m waagrecht ✓',
     'fehler': '8 % Steigung als Winkel 8° anzugeben ist falsch: 8 % bedeutet ⟦tan α = 0,08⟧, also etwa 4,6°.'},
]


def g_seiten(s):
    if s < 3:
        w = R.choice(['α', 'β'])
        art = R.choice(['Gegenkathete', 'Ankathete', 'Hypotenuse'])
        r = {('α', 'Gegenkathete'): 'a', ('α', 'Ankathete'): 'b', ('β', 'Gegenkathete'): 'b', ('β', 'Ankathete'): 'a'}.get((w, art), 'c')
        if s == 1:
            return auswahl(f'Im Dreieck ABC ist γ = 90°. Welche Seite ist die {art} von {w}?', r, ['a', 'b', 'c'],
                           f'Hypotenuse c liegt gegenüber dem rechten Winkel. Für {w}: Gegenkathete {"a" if w == "α" else "b"}, Ankathete {"b" if w == "α" else "a"}.',
                           'Welche Seite liegt dem Winkel gegenüber, welche liegt an ihm an?')
        rechts = R.choice(['α', 'β'])
        andere = 'β' if rechts == 'α' else 'α'
        hyp = 'a' if rechts == 'α' else 'b'
        w2 = R.choice([andere, 'γ'])
        tab = {('β', 'γ', 'Gegenkathete'): 'c', ('β', 'γ', 'Ankathete'): 'b', ('α', 'γ', 'Gegenkathete'): 'c', ('α', 'γ', 'Ankathete'): 'a'}
        if w2 == 'γ':
            r = tab[(andere, 'γ', art)] if art != 'Hypotenuse' else hyp
        else:
            ankathete = 'c'
            gegen = 'b' if andere == 'β' else 'a'
            r = {'Gegenkathete': gegen, 'Ankathete': ankathete, 'Hypotenuse': hyp}[art]
        return auswahl(f'Im Dreieck ABC ist {rechts} = 90°. Welche Seite ist die {art} von {w2}?', r, ['a', 'b', 'c'],
                       f'Der rechte Winkel liegt bei {"A" if rechts == "α" else "B"}, also ist {hyp} die Hypotenuse. Die {art} von {w2} ist {r}.',
                       'Bestimme zuerst die Hypotenuse: Sie liegt dem rechten Winkel gegenüber.')
    pkt = R.sample(['P', 'Q', 'R', 'K', 'L', 'M', 'D', 'E', 'F'], 3)
    recht, w, dritt = pkt
    art = R.choice(['Gegenkathete', 'Ankathete'])
    r = f'{recht}{dritt}' if art == 'Gegenkathete' else f'{w}{recht}'
    falsch = [f'{w}{dritt}', f'{dritt}{recht}' if art == 'Ankathete' else f'{w}{recht}', f'{recht}{dritt}' if art == 'Ankathete' else f'{w}{dritt}']
    return auswahl(f'Im Dreieck {"".join(sorted(pkt))} ist der Winkel bei {recht} ein rechter. Welche Strecke ist die {art} des Winkels bei {w}?', r,
                   [f'{w}{dritt}', f'{recht}{dritt}', f'{w}{recht}'],
                   f'Hypotenuse ist {w}{dritt} (gegenüber {recht}). Am Winkel bei {w} liegt die Kathete {w}{recht} an; gegenüber liegt {recht}{dritt}.',
                   'Hypotenuse zuerst: gegenüber dem rechten Winkel.')


def g_verhaeltnisse(s):
    if s == 1:
        f, w = R.choice(list(FUNK)), R.choice(['α', 'β'])
        gg, an = ('a', 'b') if w == 'α' else ('b', 'a')
        r = {'sin': f'{gg}/c', 'cos': f'{an}/c', 'tan': f'{gg}/{an}'}[f]
        return auswahl(f'Im Dreieck ABC ist γ = 90°. Welcher Term ist {f} {w}?', r, [f'{gg}/c', f'{an}/c', f'{gg}/{an}', f'{an}/{gg}'],
                       f'{f} = {"Gegenkathete : Hypotenuse" if f == "sin" else "Ankathete : Hypotenuse" if f == "cos" else "Gegenkathete : Ankathete"}; für {w} ist {gg} die Gegenkathete, {an} die Ankathete: {f} {w} = {r}.',
                       'Bestimme zu dem Winkel zuerst An- und Gegenkathete.')
    a, b, c = R.choice(TRIPEL)
    f = R.choice(list(FUNK))
    w = R.choice(['α', 'β'])
    gg, an = (a, b) if w == 'α' else (b, a)
    q = {'sin': Fr(gg, c), 'cos': Fr(an, c), 'tan': Fr(gg, an)}[f]
    if not endlich(q) or q.denominator > 100: return None
    if s == 3 and R.random() < 0.5:
        k = R.choice([Fr(1, 10), Fr(1, 2), 2, 3])
        a, b, c = a * k, b * k, c * k
        if not all(endlich(x) for x in (a, b, c)): return None
        gg, an = (a, b) if w == 'α' else (b, a)
        return zahl(f'Im Dreieck ABC ist γ = 90°, a = {dz(a)} cm, b = {dz(b)} cm. Berechne zuerst c und dann {f} {w} als Dezimalzahl.',
                    f'c = √({dz(a * a)} + {dz(b * b)}) = {dz(c)} cm; {f} {w} = {dz(gg if f != "cos" else an)} : {dz(c if f != "tan" else an)} = {dz(q)}.',
                    'Erst Pythagoras, dann das passende Verhältnis.', q,
                    f'{cf(gg if f != "cos" else an)} / ({cf(a)} ** 2 + {cf(b)} ** 2) * {cf(c)}' if f != 'tan' else f'{cf(gg)} / {cf(an)}')
    return zahl(f'Im Dreieck ABC ist γ = 90°, a = {a} cm, b = {b} cm, c = {c} cm. Berechne {f} {w} als Dezimalzahl.',
                f'{f} {w} = {"Gegenkathete : Hypotenuse" if f == "sin" else "Ankathete : Hypotenuse" if f == "cos" else "Gegenkathete : Ankathete"} = {gg if f != "cos" else an} : {c if f != "tan" else an} = {dz(q)}.',
                'Welche Seiten gehören zu diesem Winkel und dieser Funktion?', q,
                f'{gg if f != "cos" else an} / {c if f != "tan" else an}')


def g_seite(s):
    al = R.randint(12, 78)
    if s == 1:
        c = R.randint(4, 20)
        f = R.choice(['sin', 'cos'])
        wahr = c * FUNK[f](al)
        v = gerundet(wahr, 1)
        if v is None: return None
        ziel = 'a' if f == 'sin' else 'b'
        return zahl(f'Im Dreieck ABC ist γ = 90°, α = {al}° und c = {c} cm. Berechne {ziel} (auf eine Nachkommastelle).',
                    f'{ziel} ist {"Gegen" if f == "sin" else "An"}kathete von α: {ziel} = c · {f} α = {c} · {f} {al}° ≈ {dz(v)} cm.',
                    f'Welche Funktion verbindet {ziel} und c?', v, f'round({c} * {K(FUNK[f](al))}, 1)', einheit='cm')
    if s == 2:
        b = R.randint(3, 20)
        wahr = b * tan(al)
        v = gerundet(wahr, 1)
        if v is None or wahr > 80: return None
        return zahl(f'Im Dreieck ABC ist γ = 90°, α = {al}° und b = {b} cm. Berechne a (auf eine Nachkommastelle).',
                    f'tan α = a/b ⇒ a = b · tan α = {b} · tan {al}° ≈ {dz(v)} cm.', 'a ist Gegenkathete, b Ankathete von α.', v,
                    f'round({b} * {K(tan(al))}, 1)', einheit='cm')
    a = R.randint(3, 15)
    f = R.choice(['sin', 'tan', 'cos'])
    if f == 'sin':
        wahr = a / sin(al)
        t, w = f'α = {al}° und a = {a} cm. Berechne c', f'sin α = a/c ⇒ c = a : sin α = {a} : sin {al}°'
        c_ = f'round({a} / {K(sin(al))}, 1)'
    elif f == 'tan':
        wahr = a / tan(al)
        t, w = f'α = {al}° und a = {a} cm. Berechne b', f'tan α = a/b ⇒ b = a : tan α = {a} : tan {al}°'
        c_ = f'round({a} / {K(tan(al))}, 1)'
    else:
        wahr = a / cos(al)
        t, w = f'β = {90 - al}° und a = {a} cm. Berechne c', f'a ist Ankathete von β: cos β = a/c ⇒ c = a : cos β = {a} : cos {90 - al}°'
        wahr = a / cos(90 - al)
        c_ = f'round({a} / {K(cos(90 - al))}, 1)'
    v = gerundet(wahr, 1)
    if v is None or wahr > 100: return None
    return zahl(f'Im Dreieck ABC ist γ = 90°, {t} (auf eine Nachkommastelle).', f'{w} ≈ {dz(v)} cm.',
                'Die gesuchte Seite steht im Nenner: Stelle die Gleichung durch Multiplizieren und Teilen um.', v, c_, einheit='cm')


def g_winkel(s):
    a, b = R.randint(2, 15), R.randint(2, 15)
    if a == b: return None
    if s == 1:
        f = 'tan'
        q = a / b
        wahr = atan(q)
        t = f'a = {a} cm und b = {b} cm. Berechne α'
        w = f'tan α = a/b = {a}/{b} ⇒ α = tan⁻¹({a}/{b})'
    elif s == 2:
        c = R.randint(max(a, b) + 1, max(a, b) + 10)
        if R.random() < 0.5:
            wahr = asin(a / c)
            t, w = f'a = {a} cm und c = {c} cm. Berechne α', f'sin α = a/c = {a}/{c} ⇒ α = sin⁻¹({a}/{c})'
        else:
            wahr = acos(b / c)
            t, w = f'b = {b} cm und c = {c} cm. Berechne α', f'cos α = b/c = {b}/{c} ⇒ α = cos⁻¹({b}/{c})'
    else:
        c = R.randint(max(a, b) + 1, max(a, b) + 10)
        wahr = 90 - asin(a / c)
        t, w = f'a = {a} cm und c = {c} cm. Berechne β', f'a ist Ankathete von β: cos β = a/c = {a}/{c} ⇒ β = cos⁻¹({a}/{c})'
    v = gerundet(wahr, 1)
    if v is None: return None
    return zahl(f'Im Dreieck ABC ist γ = 90°, {t} (in Grad, auf eine Nachkommastelle).', f'{w} ≈ {dz(v)}°.',
                'Bilde das passende Seitenverhältnis und benutze die Umkehrtaste (DEG-Modus).', v, f'round({K(wahr)}, 1)', einheit='°')


def g_beziehungen(s):
    trip = [(3, 4, 5), (7, 24, 25), (44, 117, 125), (336, 527, 625)]
    if s == 1:
        typ = R.random()
        if typ < 0.5:
            w, wert = R.choice([('sin 30°', Fr(1, 2)), ('cos 60°', Fr(1, 2)), ('tan 45°', Fr(1)), ('sin 90°', Fr(1)), ('cos 0°', Fr(1)), ('sin 0°', Fr(0)), ('tan 0°', Fr(0))])
            return zahl(f'Gib den exakten Wert von {w} an.', f'{w} = {dz(wert)} (besonderer Wert, z. B. am halben gleichseitigen bzw. gleichschenklig-rechtwinkligen Dreieck).',
                        'Denke an das halbe gleichseitige Dreieck (30°/60°) und das gleichschenklig-rechtwinklige (45°).', wert, f'{cf(wert)}')
        al = R.randint(5, 85)
        return auswahl(f'Welcher Ausdruck ist gleich sin {al}°?', f'cos {90 - al}°', [f'cos {al}°', f'sin {90 - al}°', f'tan {al}°'],
                       f'Im rechtwinkligen Dreieck ist die Gegenkathete von α die Ankathete von 90° − α: sin {al}° = cos {90 - al}°.',
                       'Was ist der andere spitze Winkel im rechtwinkligen Dreieck?')
    p, q, r = R.choice(trip)
    if R.random() < 0.5: p, q = q, p
    sn, cs = Fr(p, r), Fr(q, r)
    if not (endlich(sn) and endlich(cs)): return None
    if s == 2:
        typ = R.random()
        if typ < 0.3:
            return zahl(f'Für einen spitzen Winkel α gilt sin α = {dz(sn)}. Berechne cos α.', f'cos² α = 1 − {dz(sn)}² = {dz(1 - sn * sn)}, cos α = {dz(cs)} (positiv, da α spitz).',
                        'Nutze sin² α + cos² α = 1.', cs, f'(1 - {cf(sn)} ** 2) / {cf(cs)}')
        if typ < 0.55:
            return zahl(f'Für einen spitzen Winkel β gilt cos β = {dz(cs)}. Berechne sin β.', f'sin² β = 1 − {dz(cs)}² = {dz(1 - cs * cs)}, sin β = {dz(sn)} (positiv, da β spitz).',
                        'Nutze sin² β + cos² β = 1.', sn, f'(1 - {cf(cs)} ** 2) / {cf(sn)}')
        if typ < 0.75:
            return zahl(f'Für einen spitzen Winkel α gilt sin α = {dz(sn)}. Wie groß ist cos(90° − α)?', f'cos(90° − α) = sin α = {dz(sn)}.',
                        'Im rechtwinkligen Dreieck ist 90° − α der andere spitze Winkel.', sn, f'{cf(sn)}')
        al = R.randint(5, 85)
        return auswahl(f'Welcher Ausdruck ist gleich cos {al}°?', f'sin {90 - al}°', [f'sin {al}°', f'cos {90 - al}°', f'tan {90 - al}°'],
                       f'Die Ankathete von {al}° ist die Gegenkathete von {90 - al}°: cos {al}° = sin {90 - al}°.', 'Was ist der andere spitze Winkel?')
    if R.random() < 0.5:
        tn = sn / cs
        if not endlich(tn): return None
        return zahl(f'Für einen spitzen Winkel α gilt cos α = {dz(cs)}. Berechne tan α.', f'sin α = √(1 − {dz(cs)}²) = {dz(sn)}; tan α = {dz(sn)} : {dz(cs)} = {dz(tn)}.',
                    'Erst sin α über sin² + cos² = 1, dann tan = sin : cos.', tn, f'{cf(sn)} / {cf(cs)}')
    return auswahl(f'Jemand behauptet: „Für einen spitzen Winkel gilt sin α = {dz(sn)} und cos α = {dz(1 - sn)}, weil sin α + cos α = 1.“ Was stimmt?',
                   f'Falsch: Es gilt sin² α + cos² α = 1, also cos α = {dz(cs)}.',
                   ['Richtig.', f'Falsch: cos α = {dz(sn)}, weil Sinus und Kosinus gleich sind.', f'Falsch: cos α = {dz(1 + sn)}.'],
                   f'{dz(sn)}² + {dz(cs)}² = {dz(sn * sn)} + {dz(cs * cs)} = 1. Mit {dz(1 - sn)} wäre {dz(sn)}² + {dz(1 - sn)}² = {dz(sn * sn + (1 - sn) ** 2)} ≠ 1.',
                   'Prüfe mit sin² α + cos² α = 1.')


def g_anwendung(s):
    typ = R.random()
    if s == 1:
        p = R.choice([2, 3, 4, 5, 6, 8, 10, 12, 15, 20])
        wahr = atan(p / 100)
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Eine Straße hat {p} % Steigung. Wie groß ist der Steigungswinkel (in Grad, auf eine Nachkommastelle)?',
                    f'tan α = {p}/100 = {dz(Fr(p, 100))} ⇒ α ≈ {dz(v)}°.', 'Steigung in % ist der Tangens des Steigungswinkels mal 100.', v,
                    f'round({K(wahr)}, 1)', einheit='°')
    if s == 2:
        if typ < 0.5:
            d, w = R.randint(20, 150), R.randint(15, 60)
            wahr = d * tan(w)
            v = gerundet(wahr, 1)
            if v is None: return None
            return zahl(f'Aus {d} m Entfernung sieht man die Spitze eines Turms unter dem Höhenwinkel {w}° (Augenhöhe vernachlässigt). Wie hoch ist der Turm?',
                        f'tan {w}° = h/{d} ⇒ h = {d} · tan {w}° ≈ {dz(v)} m.', 'Entfernung ist die Ankathete, Turmhöhe die Gegenkathete.', v,
                        f'round({d} * {K(tan(w))}, 1)', einheit='m')
        l, w = R.randint(3, 8), R.randint(60, 78)
        wahr = l * sin(w)
        v = gerundet(wahr, 2)
        if v is None: return None
        return zahl(f'Eine {l} m lange Leiter lehnt unter einem Winkel von {w}° zum Boden an einer Wand. In welcher Höhe berührt sie die Wand (auf cm genau, in m)?',
                    f'sin {w}° = h/{l} ⇒ h = {l} · sin {w}° ≈ {dz(v)} m.', 'Die Leiter ist die Hypotenuse, die Höhe die Gegenkathete zum Bodenwinkel.', v,
                    f'round({l} * {K(sin(w))}, 2)', einheit='m')
    if typ < 0.35:
        h, w = R.choice([30, 40, 50, 60, 75, 80, 100, 120]), R.randint(4, 12)
        l = R.randint(5, 20) * 10
        wahr = atan(h / (l * 10))
        v = gerundet(wahr, 1)
        if v is None: return None
        return zahl(f'Eine Rampe überwindet {h} cm Höhe auf {l * 10} cm waagrechter Länge. Wie groß ist der Neigungswinkel (auf eine Nachkommastelle)?',
                    f'tan α = {h}/{l * 10} ⇒ α ≈ {dz(v)}°.', 'Höhe und waagrechte Länge sind Gegen- und Ankathete.', v, f'round({K(wahr)}, 1)', einheit='°')
    if typ < 0.7:
        weg, w = R.randint(2, 20) * 100, R.randint(3, 15)
        wahr = weg * sin(w)
        v = gerundet(wahr, 0)
        if v is None: return None
        return zahl(f'Ein Wanderweg ist {dz(weg)} m lang und steigt gleichmäßig unter dem Winkel {w}° an. Wie viele Höhenmeter überwindet er (auf ganze Meter)?',
                    f'h = {dz(weg)} · sin {w}° ≈ {dz(v)} m.', 'Die Weglänge ist die Hypotenuse (schräg), die Höhe die Gegenkathete.', v,
                    f'round({weg} * {K(sin(w))}, 0)', einheit='m')
    h, w1 = R.randint(20, 80), R.randint(20, 40)
    wahr = h / tan(w1)
    v = gerundet(wahr, 1)
    if v is None: return None
    return zahl(f'Von einem {h} m hohen Leuchtturm sieht man ein Boot unter dem Tiefenwinkel {w1}° (gemessen von der Waagrechten nach unten). Wie weit ist das Boot vom Fuß des Turms entfernt?',
                f'Der Tiefenwinkel ist gleich dem Höhenwinkel vom Boot aus (Wechselwinkel): tan {w1}° = {h}/e ⇒ e = {h} : tan {w1}° ≈ {dz(v)} m.',
                'Zeichne die Waagrechte am Turm; der Tiefenwinkel taucht unten am Boot als Wechselwinkel wieder auf.', v,
                f'round({h} / {K(tan(w1))}, 1)', einheit='m')


GEN = {'seiten': g_seiten, 'verhaeltnisse': g_verhaeltnisse, 'seite': g_seite, 'winkel': g_winkel,
       'beziehungen': g_beziehungen, 'anwendung': g_anwendung}

if __name__ == '__main__':
    bauen('trigo.rechtwinklig',
          'Sinus, Kosinus und Tangens als Seitenverhältnisse im rechtwinkligen Dreieck nutzen, um Seiten und Winkel zu berechnen.',
          ['sin α = Gegenkathete : Hypotenuse; cos α = Ankathete : Hypotenuse; tan α = Gegenkathete : Ankathete.',
           'Seite gesucht: Gleichung nach der Seite umstellen. Winkel gesucht: Umkehrtaste (DEG).', 'sin² α + cos² α = 1; tan α = sin α : cos α; sin α = cos(90° − α).',
           'Steigung in % = tan α · 100.'],
          [('Grundbegriffe', ['seiten', 'verhaeltnisse']), ('Berechnen', ['seite', 'winkel', 'beziehungen']), ('Anwenden', ['anwendung'])],
          ETAPPEN, GEN,
          meiden={'verhaeltnisse': ['a = 8 cm, b = 15 cm, c = 17 cm'], 'seite': ['α = 35° und c = 10 cm'], 'winkel': ['a = 4 cm und b = 7 cm. Berechne α'],
                  'beziehungen': ['sin α = 0,28'], 'anwendung': ['8 % Steigung']},
          offen=['Alle Lernkarten brauchen eigentlich eine Dreieckskizze (rechter Winkel, Bezeichnungen a, b, c, α, β). Bisher Standardbezeichnung „Dreieck ABC mit γ = 90°“ in Worten; Anwendungsaufgaben (Höhenwinkel, Tiefenwinkel) würden von einer Skizze stark profitieren.',
                 'Rechenausdruck c: sin/cos/tan-Werte stehen als 12-stellige Konstanten, weil das Prüfskript keine Winkelfunktionen kennt. Werte nahe an Rundungsgrenzen werden vom Generator verworfen.'])
