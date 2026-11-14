#!/usr/bin/env python3
"""Thema gleichungen.wurzel – Wurzelgleichungen (Realschule Bayern, Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rs import *  # noqa: E402,F403

start(1301)


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def rad(a, b):
    """Radikand a·x + b als Text"""
    return poly(a, b)


def wz(a, b):
    return f'√({rad(a, b)})' if (a != 1 or b != 0) else '√x'


ETAPPEN = [
    {'lernziel': 'definitionsmenge', 'titel': 'Wann ist die Wurzel definiert?',
     'regel': 'Unter der Wurzel (im ⟦Radikanden⟧) darf ⟦keine negative Zahl⟧ stehen. Bei √(2x − 6) muss also ⟦2x − 6 ≥ 0⟧ gelten. Diese Ungleichung löst du – das ergibt die ⟦Definitionsmenge D⟧. Wie ein Türsteher: Nur x-Werte aus D dürfen in die Gleichung.',
     'schritte': ['√(2x − 6): 2x − 6 ≥ 0 | + 6 ⇒ 2x ≥ 6 | : 2 ⇒ x ≥ 3.', 'Also ⟦D = {x | x ≥ 3}⟧.'],
     'probe': 'x = 3: √0 = 0 ✓; x = 2: √(−2) gibt es nicht ✓',
     'fehler': 'Bei √(6 − 2x) zu schreiben D = {x | x ≥ 3} ist falsch: −2x ≥ −6 und beim Teilen durch ⟦−2 dreht sich das Zeichen⟧: x ≤ 3.'},
    {'lernziel': 'quadrieren', 'titel': 'Durch Quadrieren lösen',
     'regel': 'Steht die Wurzel allein, ⟦quadrierst du beide Seiten⟧: Aus √(T) = c wird ⟦T = c²⟧. Das ist eine Gleichung ohne Wurzel. Danach immer die ⟦Probe⟧ machen.',
     'schritte': ['√(3x + 1) = 5 | quadrieren ⇒ 3x + 1 = 25.', '3x = 24 ⇒ ⟦x = 8⟧.'],
     'probe': '√(3 · 8 + 1) = √25 = 5 ✓',
     'fehler': '√(3x + 1) = 5 ⇒ 3x + 1 = 5 ist falsch: Die rechte Seite muss ⟦auch quadriert⟧ werden: 5² = 25.'},
    {'lernziel': 'isolieren', 'titel': 'Erst die Wurzel allein stellen',
     'regel': 'Bevor du quadrierst, muss die ⟦Wurzel allein⟧ auf einer Seite stehen. Zahlen davor oder dahinter bringst du wie gewohnt weg. Quadrierst du zu früh, entsteht ein unübersichtlicher Term.',
     'schritte': ['2 · √(x − 3) + 4 = 14 | − 4 ⇒ 2 · √(x − 3) = 10 | : 2 ⇒ √(x − 3) = 5.', 'Quadrieren: x − 3 = 25 ⇒ ⟦x = 28⟧.'],
     'probe': '2 · √25 + 4 = 2 · 5 + 4 = 14 ✓',
     'fehler': '√(x − 3) + 4 = 14 gleich zu quadrieren und (x − 3) + 16 = 196 zu schreiben ist falsch: (a + b)² ist ⟦nicht a² + b²⟧. Erst die 4 abziehen.'},
    {'lernziel': 'probe', 'titel': 'Probe und Scheinlösungen',
     'regel': 'Quadrieren kann ⟦Scheinlösungen⟧ erzeugen: Aus √(T) = −3 wird T = 9, obwohl eine Wurzel ⟦nie negativ⟧ ist. Deshalb gilt: Jede Lösung mit der ⟦Probe⟧ prüfen. Fällt sie durch, gehört sie nicht zu L.',
     'schritte': ['√(x + 5) = −3 ⇒ x + 5 = 9 ⇒ x = 4.', 'Probe: √(4 + 5) = 3 ≠ −3. x = 4 ist eine Scheinlösung, also ⟦L = { }⟧.'],
     'fehler': 'Bei √(x + 5) = −3 einfach L = {4} anzugeben ist falsch: Die Probe zeigt ⟦3 ≠ −3⟧. Schon vorher erkennbar: Eine Wurzel kann nicht negativ sein.'},
    {'lernziel': 'zwei_seiten', 'titel': 'Wurzel und x auf beiden Seiten',
     'regel': 'Bei √(x + b) = x + c ergibt das Quadrieren eine ⟦quadratische Gleichung⟧: x + b = (x + c)². Sie hat oft zwei Lösungen – aber ⟦nur die mit bestandener Probe⟧ gehört zu L. Bei √(T₁) = √(T₂) quadrierst du einfach zu T₁ = T₂.',
     'schritte': ['√(x + 7) = x + 1 ⇒ x + 7 = x² + 2x + 1 ⇒ x² + x − 6 = 0 ⇒ x = −3 oder x = 2.',
                  'Probe: x = 2: √9 = 3 = 2 + 1 ✓. x = −3: √4 = 2, aber −3 + 1 = −2 ✗. Also ⟦L = {2}⟧.'],
     'fehler': 'Beide Lösungen der quadratischen Gleichung in L zu schreiben ist falsch: x = −3 macht die rechte Seite ⟦negativ⟧ – eine Scheinlösung.'},
    {'lernziel': 'sachaufgabe', 'titel': 'Formeln mit Wurzeln',
     'regel': 'Manche Formeln enthalten Wurzeln, z. B. die Fallzeit ⟦t = √(h : 5)⟧ (h in m, t in s) oder die Aufprallgeschwindigkeit ⟦v = √(20 · h)⟧ (v in m/s). Ist das Ergebnis gegeben und die Größe ⟦unter der Wurzel⟧ gesucht, löst du eine Wurzelgleichung.',
     'schritte': ['Ein Stein fällt 3 s lang: √(h : 5) = 3 | quadrieren ⇒ h : 5 = 9.', 'h = 45. Er fiel aus ⟦45 m⟧ Höhe.'],
     'probe': '√(45 : 5) = √9 = 3 ✓',
     'fehler': '√(h : 5) = 3 ⇒ h = 15 ist falsch: Zuerst ⟦quadrieren⟧ (h : 5 = 9), dann mal 5.'},
]


# ---------- Generatoren ----------
def g_definitionsmenge(s):
    if s == 1:
        b = nz(12)
        return luecken(f'Gib die Definitionsmenge von √(x {plus(b)}) an.', 'D = {x | x ≥ □}', 'Grenze als Zahl', [-b],
                       f'x {plus(b)} ≥ 0 ⇔ x ≥ {dz(-b)}. D = {{x | x ≥ {dz(-b)}}}.', 'Der Radikand muss mindestens 0 sein.', c=[f'-({b})'])
    a = R.randint(2, 6)
    g = nz(8)
    b = -a * g
    if s == 2:
        return luecken(f'Gib die Definitionsmenge von {wz(a, b)} an.', 'D = {x | x ≥ □}', 'Grenze als Zahl', [g],
                       f'{rad(a, b)} ≥ 0 ⇔ {a}x ≥ {dz(-b)} ⇔ x ≥ {dz(g)}.', 'Löse die Ungleichung Radikand ≥ 0.', c=[f'-({b}) / {a}'])
    art = R.random()
    if art < 0.4:
        return auswahl(f'Welche Definitionsmenge hat √({dz(-b)} − {a}x)?', f'D = {{x | x ≤ {dz(Fr(-b, a))}}}',
                       [f'D = {{x | x ≥ {dz(Fr(-b, a))}}}', f'D = {{x | x ≤ {dz(-Fr(-b, a))}}}', f'D = {{x | x ≥ {dz(-Fr(-b, a))}}}'],
                       f'{dz(-b)} − {a}x ≥ 0 ⇔ −{a}x ≥ {dz(b)} ⇔ x ≤ {dz(Fr(-b, a))} (Teilen durch −{a} dreht das Zeichen).',
                       'Achtung beim Teilen durch eine negative Zahl.')
    if art < 0.7:
        x0 = g + R.choice([-3, -2, -1, 1, 2, 3])
        drin = x0 >= g
        return auswahl(f'Darf man x = {dz(x0)} in {wz(a, b)} einsetzen?', 'Ja' if drin else 'Nein',
                       ['Nein' if drin else 'Ja', 'Nur, wenn das Ergebnis eine ganze Zahl ist.'],
                       f'Radikand: {a} · {kl(x0)} {plus(b)} = {dz(a * x0 + b)}. ' + ('Nicht negativ, also erlaubt.' if drin else 'Negativ, also nicht erlaubt.'),
                       'Setze ein und prüfe das Vorzeichen des Radikanden.')
    c = nz(5)
    # zwei Wurzeln: Schnitt der Bedingungen
    g2 = g + R.choice([1, 2, 3, 4])
    return luecken(f'Gib die Definitionsmenge der Gleichung √(x {plus(-g)}) = √(x {plus(-g2)}) {plus(c)} an.', 'D = {x | x ≥ □}', 'Grenze als Zahl', [g2],
                   f'x {plus(-g)} ≥ 0 ⇔ x ≥ {dz(g)} und x {plus(-g2)} ≥ 0 ⇔ x ≥ {dz(g2)}. Beides muss gelten: x ≥ {dz(g2)}.',
                   'Beide Radikanden müssen ≥ 0 sein.', c=[f'max({g}, {g2})'])


def g_quadrieren(s):
    if s == 1:
        c = R.randint(1, 12)
        b = R.randint(-20, 20)
        x = c * c - b
        return zahl(f'Löse √(x {plus(b)}) = {c}.', f'Quadrieren: x {plus(b)} = {c * c} ⇒ x = {dz(x)}. Probe: √{c * c} = {c} ✓.',
                    'Quadriere beide Seiten.', x, f'{c} ** 2 - ({b})')
    a = R.randint(2, 6)
    c = R.randint(1, 10)
    x = nz(15)
    b = c * c - a * x
    w = f'Quadrieren: {rad(a, b)} = {c * c} ⇒ {a}x = {dz(c * c - b)} ⇒ x = {dz(x)}. Probe: √({a} · {kl(x)} {plus(b)}) = √{c * c} = {c} ✓.'
    if s == 2:
        return zahl(f'Löse {wz(a, b)} = {c}.', w, 'Quadrieren, dann wie eine lineare Gleichung lösen.', x, f'({c} ** 2 - ({b})) / {a}')
    art = R.random()
    if art < 0.4:
        return auswahl(f'Jemand löst {wz(a, b)} = {c} so: {rad(a, b)} = {c}, also x = {dz(Fr(c - b, a))}. Was stimmt?',
                       f'Falsch: Rechts muss {c}² = {c * c} stehen; x = {dz(x)}.',
                       ['Richtig.', f'Falsch: x = {dz(Fr(c * c + b, a))}.', 'Falsch: Die Gleichung hat keine Lösung.'],
                       w, 'Was passiert beim Quadrieren mit der rechten Seite?') if endlich(Fr(c - b, a)) and endlich(Fr(c * c + b, a)) else None
    if art < 0.7:
        q = Fr(R.choice([1, 3, 5, 7, 9]), 2)
        x = Fr(R.randint(-10, 10))
        b = q * q - a * x
        if not endlich(b): return None
        return zahl(f'Löse √({rad(a, b)}) = {dz(q)}.', f'{rad(a, b)} = {dz(q * q)} ⇒ {a}x = {dz(q * q - b)} ⇒ x = {dz(x)}.',
                    'Auch Dezimalzahlen quadriert man: 1,5² = 2,25.', x, f'({cz(q)} ** 2 - {cz(b)}) / {a}')
    # Wurzel aus x², Bruch unter Wurzel: √(x : k) = c
    k = R.choice([2, 3, 4, 5])
    c = R.randint(2, 9)
    return zahl(f'Löse √(x : {k}) = {c}.', f'x : {k} = {c * c} ⇒ x = {c * c * k}. Probe: √({c * c * k} : {k}) = √{c * c} = {c} ✓.',
                'Quadrieren, dann mit dem Teiler multiplizieren.', c * c * k, f'{c} ** 2 * {k}')


def g_isolieren(s):
    c = R.randint(1, 9)
    b = R.randint(-15, 15)
    x = c * c - b
    if s == 1:
        d = R.randint(1, 20)
        return zahl(f'Löse √(x {plus(b)}) + {d} = {c + d}.', f'√(x {plus(b)}) = {c} ⇒ x {plus(b)} = {c * c} ⇒ x = {dz(x)}.',
                    f'Erst {d} abziehen, dann quadrieren.', x, f'({c + d} - {d}) ** 2 - ({b})')
    k = R.randint(2, 5)
    d = R.randint(-20, 20)
    e = k * c + d
    w = f'{k} · √(x {plus(b)}) = {dz(e)} {plus(-d)} = {k * c} ⇒ √(x {plus(b)}) = {c} ⇒ x {plus(b)} = {c * c} ⇒ x = {dz(x)}.'
    if s == 2:
        return zahl(f'Löse {k} · √(x {plus(b)}) {plus(d)} = {dz(e)}.', w, 'Wurzel allein stellen: erst die Zahl weg, dann durch den Faktor teilen.',
                    x, f'((({e}) - ({d})) / {k}) ** 2 - ({b})')
    art = R.random()
    if art < 0.4:
        falsch = e * e - d * d
        return auswahl(f'Jemand quadriert √(x {plus(b)}) {plus(d)} = {dz(e)} sofort und erhält x {plus(b)} {plus(d * d)} = {dz(e * e)}. Was stimmt?',
                       f'Falsch: Erst √(x {plus(b)}) allein stellen; richtig ist x = {dz((e - d) ** 2 - b)}.',
                       ['Richtig, man darf jeden Summanden einzeln quadrieren.', f'Falsch: richtig ist x = {dz(falsch - b)}.', 'Falsch: Es gibt keine Lösung.'],
                       f'(a + b)² ≠ a² + b². Richtig: √(x {plus(b)}) = {dz(e - d)} ⇒ x = {dz((e - d) ** 2 - b)}.',
                       'Darf man eine Summe gliedweise quadrieren?') if e - d > 0 else None
    if art < 0.7:
        # Wurzel steht rechts, minus davor
        f = R.randint(c + 1, c + 15)
        return zahl(f'Löse {f} − √(x {plus(b)}) = {f - c}.', f'√(x {plus(b)}) = {f} − {f - c} = {c} ⇒ x {plus(b)} = {c * c} ⇒ x = {dz(x)}.',
                    'Bring die Wurzel auf die eine Seite, die Zahlen auf die andere.', x, f'({f} - {f - c}) ** 2 - ({b})')
    a2 = R.randint(2, 4)
    x2 = nz(10)
    b2 = c * c - a2 * x2
    return zahl(f'Löse {k} · √({rad(a2, b2)}) {plus(d)} = {dz(k * c + d)}.',
                f'√({rad(a2, b2)}) = {c} ⇒ {rad(a2, b2)} = {c * c} ⇒ x = {dz(x2)}.', 'Wurzel allein stellen, quadrieren, linear lösen.',
                x2, f'((({k * c + d}) - ({d})) / {k}) ** 2 / {a2} - ({b2}) / {a2}')


def g_probe(s):
    c = R.randint(1, 9)
    b = R.randint(-15, 15)
    if s == 1:
        return auswahl(f'Welche Lösungsmenge hat √(x {plus(b)}) = −{c}?', 'L = { }', [f'L = {{{dz(c * c - b)}}}', f'L = {{{dz(-c * c - b)}}}', f'L = {{−{c}; {c}}}'],
                       f'Eine Wurzel ist nie negativ. Quadrieren liefert x = {dz(c * c - b)}, aber die Probe ergibt √{c * c} = {c} ≠ −{c}.',
                       'Kann eine Wurzel negativ sein?')
    if s == 2:
        x0 = nz(10)
        rest = x0 + b
        if rest < 0:
            return auswahl(f'Ist x = {dz(x0)} eine Lösung von √(x {plus(b)}) = {c}?', 'Nein, x liegt nicht in der Definitionsmenge.',
                           ['Ja.', 'Nein, aber nur weil die Probe eine Dezimalzahl ergibt.', f'Ja, aber nur, wenn man die Wurzel auf {c} rundet.'],
                           f'Radikand: {dz(x0)} {plus(b)} = {dz(rest)} < 0. Die Wurzel ist nicht definiert.', 'Setze ein: Was steht unter der Wurzel?')
        ist = rest == c * c
        return auswahl(f'Ist x = {dz(x0)} eine Lösung von √(x {plus(b)}) = {c}? Mach die Probe.', 'Ja' if ist else 'Nein',
                       ['Nein' if ist else 'Ja', 'Man kann es ohne Taschenrechner nicht sagen.'],
                       f'√({dz(x0)} {plus(b)}) = √{dz(rest)}' + (f' = {c} ✓' if ist else f' ≠ {c}, denn {c}² = {c * c} ≠ {dz(rest)}.'),
                       'Einsetzen und vergleichen.')
    art = R.random()
    if art < 0.4:
        k = R.randint(2, 5)
        d = R.randint(5, 25)
        e = d - k * c
        return auswahl(f'Löse {k} · √(x {plus(b)}) + {d} = {dz(e)}.', 'L = { }', [f'L = {{{dz(c * c - b)}}}', f'L = {{{dz(-c * c - b)}}}', f'L = {{{dz(Fr(e - d, k) - b) if endlich(Fr(e - d, k)) else 0}}}'],
                       f'{k} · √(x {plus(b)}) = {dz(e - d)} ⇒ √(x {plus(b)}) = {dz(Fr(e - d, k))} < 0. Unmöglich, also keine Lösung (x = {dz(c * c - b)} wäre eine Scheinlösung).',
                       'Stelle die Wurzel allein. Welches Vorzeichen hat die rechte Seite?')
    if art < 0.7:
        return auswahl(f'Jemand löst √(x {plus(b)}) = −{c} und gibt L = {{{dz(c * c - b)}}} an. Was stimmt?', f'Falsch: Die Probe ergibt {c} ≠ −{c}, also L = {{ }}.',
                       ['Richtig, die Rechnung stimmt.', f'Falsch: L = {{{dz(-c * c - b)}}}.', f'Falsch: L = {{−{c}; {c}}}.'],
                       f'Quadrieren liefert x = {dz(c * c - b)}. Probe: √{c * c} = {c}, nicht −{c}. Das ist eine Scheinlösung.',
                       'Mach die Probe.')
    return auswahl('Warum muss man bei Wurzelgleichungen immer die Probe machen?', 'Beim Quadrieren können Scheinlösungen entstehen.',
                   ['Weil Wurzeln immer gerundet werden.', 'Weil Wurzelgleichungen immer zwei Lösungen haben.', 'Weil man beim Quadrieren Lösungen verliert.'],
                   f'Quadrieren macht aus √(T) = −{c} und √(T) = {c} dieselbe Gleichung T = {c * c}. Nur die Probe zeigt, welche Lösung passt.',
                   'Was passiert mit dem Vorzeichen der rechten Seite beim Quadrieren?')


def zwei_seiten_daten():
    """√(x + b) = x + c mit einer echten Lösung r1 und einer Scheinlösung r2."""
    for _ in range(500):
        r1, r2 = R.randint(-8, 10), R.randint(-12, 6)
        if (r1 + r2) % 2 == 0 or r1 == r2: continue
        c = (1 - r1 - r2) // 2
        b = c * c - r1 * r2
        if r1 + c >= 0 and r2 + c < 0 and abs(b) <= 40 and abs(c) <= 9 and b != 0:
            return r1, r2, b, c
    raise SystemExit('keine Daten')


def g_zwei_seiten(s):
    if s == 1:
        a, c_ = R.randint(2, 6), R.randint(1, 5)
        x = nz(10)
        b = R.randint(-10, 10)
        d = (a - c_) * x + b
        if a == c_ or a * x + b < 0: return None
        return zahl(f'Löse √({rad(a, b)}) = √({rad(c_, d)}).', f'Quadrieren: {rad(a, b)} = {rad(c_, d)} ⇒ {poly(a - c_, 0)} = {dz(d - b)} ⇒ x = {dz(x)}. Probe: beide Seiten √{dz(a * x + b)} ✓.',
                    'Quadrieren beseitigt beide Wurzeln.', x, f'(({d}) - ({b})) / ({a} - {c_})')
    r1, r2, b, c = zwei_seiten_daten()
    w = (f'x {plus(b)} = (x {plus(c)})² ⇒ x² {plus_v(2 * c - 1)} {plus(c * c - b)} = 0 ⇒ x = {dz(min(r1, r2))} oder x = {dz(max(r1, r2))}. '
         f'Probe: x = {dz(r1)}: √{dz(r1 + b)} = {dz(r1 + c)} ✓; x = {dz(r2)}: √{dz(r2 + b)} = {dz(-(r2 + c))} ≠ {dz(r2 + c)} ✗. L = {{{dz(r1)}}}.')
    w = w.replace(' + 0 = 0', ' = 0').replace('x²  ', 'x² ')
    if s == 2:
        return zahl(f'Löse √(x {plus(b)}) = x {plus(c)}. (Eine der Lösungen der quadratischen Gleichung ist eine Scheinlösung.) Gib die Lösung an.', w,
                    'Quadrieren, quadratische Gleichung lösen, beide Lösungen mit der Probe prüfen.', r1, f'(-({2 * c - 1}) {"+" if r1 > r2 else "-"} {abs(r1 - r2)}) / 2')
    art = R.random()
    if art < 0.5:
        return auswahl(f'Welche Lösungsmenge hat √(x {plus(b)}) = x {plus(c)}?', f'L = {{{dz(r1)}}}',
                       [f'L = {{{dz(min(r1, r2))}; {dz(max(r1, r2))}}}', f'L = {{{dz(r2)}}}', 'L = { }'], w,
                       'Löse die quadratische Gleichung und mach mit jeder Lösung die Probe.')
    return auswahl(f'Beim Lösen von √(x {plus(b)}) = x {plus(c)} erhält jemand x = {dz(r1)} und x = {dz(r2)}. Was stimmt?',
                   f'Nur x = {dz(r1)} ist eine Lösung; x = {dz(r2)} ist eine Scheinlösung.',
                   ['Beide sind Lösungen.', f'Nur x = {dz(r2)} ist eine Lösung.', 'Keine von beiden ist eine Lösung.'],
                   w, 'Setze beide Werte in die Ausgangsgleichung ein.')


def g_sachaufgabe(s):
    art = R.choice(['fallzeit', 'aufprall', 'quadrat'])
    if art == 'fallzeit':
        t = R.randint(1, 6)
        h = 5 * t * t
        if s == 1:
            return zahl(f'Für die Fallzeit gilt t = √(h : 5) (h in m, t in s). Ein Stein fällt {t} s lang. Aus welcher Höhe fiel er?',
                        f'√(h : 5) = {t} ⇒ h : 5 = {t * t} ⇒ h = {h} m.', 'Quadrieren, dann mal 5.', h, f'{t} ** 2 * 5', einheit='m')
        t2 = Fr(R.choice([3, 5, 7]), 2)
        h2 = 5 * t2 * t2
        return zahl(f'Für die Fallzeit gilt t = √(h : 5) (h in m, t in s). Ein Ball fällt {dz(t2)} s lang. Aus welcher Höhe fiel er?',
                    f'h : 5 = {dz(t2)}² = {dz(t2 * t2)} ⇒ h = {dz(h2)} m.', 'Quadrieren, dann mal 5.', h2, f'{cz(t2)} ** 2 * 5', einheit='m')
    if art == 'aufprall':
        v = R.choice([10, 20, 30, 40, 50, 60]) if s < 3 else R.choice([5, 15, 25, 35])
        h = Fr(v * v, 20)
        if s == 3 and R.random() < 0.5:
            return auswahl(f'Für die Aufprallgeschwindigkeit gilt v = √(20 · h). Jemand rechnet für v = {v} m/s: h = {v} : 20 = {dz(Fr(v, 20))} m. Was stimmt?',
                           f'Falsch: Erst quadrieren: 20 · h = {dz(v * v)}, also h = {dz(h)} m.',
                           ['Richtig.', f'Falsch: h = {dz(v * 20)} m.', f'Falsch: h = {dz(Fr(v * v, 2))} m.'],
                           f'√(20 · h) = {v} ⇒ 20 · h = {dz(v * v)} ⇒ h = {dz(h)} m.', 'Was muss man zuerst tun, um die Wurzel loszuwerden?')
        return zahl(f'Für die Aufprallgeschwindigkeit nach einem Fall gilt näherungsweise v = √(20 · h) (v in m/s, h in m). Aus welcher Höhe muss etwas fallen, um mit {v} m/s aufzuprallen?',
                    f'√(20 · h) = {v} ⇒ 20 · h = {dz(v * v)} ⇒ h = {dz(h)} m.', 'Quadrieren, dann durch 20 teilen.', h, f'{v} ** 2 / 20', einheit='m')
    a = R.randint(3, 20)
    if s == 1:
        return zahl(f'Ein Quadrat hat die Seitenlänge a = √A. Wie groß ist die Fläche A, wenn a = {a} cm?',
                    f'√A = {a} ⇒ A = {a}² = {a * a} cm².', 'Quadrieren.', a * a, f'{a} ** 2', einheit='cm²')
    k = R.randint(2, 6)
    return zahl(f'Ein quadratisches Beet wird an jeder Seite um {k} m verlängert. Die neue Seitenlänge ist √A + {k} = {a + k} m. Wie groß war die alte Fläche A?',
                f'√A + {k} = {a + k} ⇒ √A = {a} ⇒ A = {a * a} m².', 'Wurzel allein stellen, dann quadrieren.', a * a, f'({a + k} - {k}) ** 2', einheit='m²')


GEN = {'definitionsmenge': g_definitionsmenge, 'quadrieren': g_quadrieren, 'isolieren': g_isolieren, 'probe': g_probe,
       'zwei_seiten': g_zwei_seiten, 'sachaufgabe': g_sachaufgabe}

if __name__ == '__main__':
    bauen('gleichungen.wurzel',
          'Wurzelgleichungen lösen: Definitionsmenge bestimmen, Wurzel allein stellen, quadrieren und mit der Probe Scheinlösungen erkennen.',
          ['Unter der Wurzel steht nie etwas Negatives: Radikand ≥ 0 liefert D.', 'Erst die Wurzel allein stellen, dann beide Seiten quadrieren.',
           'Eine Wurzel ist nie negativ: √(T) = negative Zahl hat keine Lösung.', 'Immer die Probe machen – Quadrieren kann Scheinlösungen erzeugen.'],
          [('Grundlagen', ['definitionsmenge', 'quadrieren', 'isolieren']), ('Probe und schwierigere Gleichungen', ['probe', 'zwei_seiten']),
           ('Anwenden', ['sachaufgabe'])],
          ETAPPEN, GEN)
