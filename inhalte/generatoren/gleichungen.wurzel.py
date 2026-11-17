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
        b = nz(20)
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
    b = nz(15)
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
    b = nz(15)
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
        if r1 + c >= 0 and r2 + c < 0 and abs(b) <= 40 and abs(c) <= 9 and b != 0 and c != 0:
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

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import tab  # noqa: E402


def _g(*z):
    return tab(['', 'Gleichung'], *z)


_Q = [['Start', '√(3x + 1) = 5'], ['quadrieren', '3x + 1 = 25'], ['− 1, : 3', 'x = 8'], ['Probe', '√25 = 5 ✓']]
_I = [['Start', '2 · √(x − 3) + 4 = 14'], ['− 4', '2 · √(x − 3) = 10'], [': 2', '√(x − 3) = 5'], ['quadrieren', 'x − 3 = 25'],
      ['+ 3', 'x = 28']]
_ZK = ['x', 'links √(x + 7)', 'rechts x + 1']
UMBAU = {
    'definitionsmenge': {
        'einstieg': 'Tippst du √(−4) in den Taschenrechner, zeigt er „Error“. Unter einer Wurzel darf nichts Negatives stehen. '
                    'Welche x erlaubt sind, sagt die ⟦Definitionsmenge D⟧.',
        'woerter': [['Radikand', 'die Zahl oder der Term unter der Wurzel'],
                    ['Definitionsmenge D', 'alle x, die man einsetzen darf'],
                    ['D = {x | x ≥ 3}', 'gelesen: alle x, die größer oder gleich 3 sind']],
        'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 6, 'abschnitte': 6, 'beschriftet': 'alle'},
        'schritte': [
            {'text': 'Der Radikand 2x − 6 darf nicht negativ sein: 2x − 6 ≥ 0.'},
            {'text': 'Plus 6, dann durch 2: x ≥ 3.', 'bild': {'punkte': [{'wert': 3, 'name': 'x = 3'}]}},
            {'text': 'Also ⟦D = {x | x ≥ 3}⟧.', 'bild': {'bereich': {'von': 3, 'bis': 6}}},
        ],
        'fehler': 'Bei √(6 − 2x) ist x ≥ 3 falsch. Beim Teilen durch −2 ⟦dreht sich das Zeichen⟧: x ≤ 3.',
        'fehler_bild': {'bereich': {'von': 0, 'bis': 3}},
        'regel': 'Radikand ≥ 0 setzen und nach x auflösen. Das ergibt die ⟦Definitionsmenge D⟧.',
    },
    'quadrieren': {
        'einstieg': 'Tippst du 25 und dann √, zeigt der Taschenrechner 5. Tippst du danach x², steht wieder 25 da. '
                    '⟦Quadrieren⟧ macht die Wurzel rückgängig.',
        'woerter': [['quadrieren', 'eine Zahl mit sich selbst malnehmen: 5² = 25'],
                    ['Probe', 'die Lösung in die Ausgangsgleichung einsetzen und prüfen']],
        'bild': _g(_Q[0]),
        'schritte': [
            {'text': 'Beide Seiten quadrieren: 3x + 1 = 25.', 'bild': _g(*_Q[:2])},
            {'text': 'Minus 1, dann durch 3: ⟦x = 8⟧.', 'bild': _g(*_Q[:3])},
            {'text': 'Probe: √(3 · 8 + 1) = √25 = 5. Stimmt.', 'bild': _g(*_Q)},
        ],
        'fehler': '3x + 1 = 5 ist falsch. Die rechte Seite muss ⟦auch quadriert⟧ werden: 5² = 25.',
        'fehler_bild': _g(_Q[0], ['falsch', '3x + 1 = 5'], ['richtig', '3x + 1 = 25']),
        'regel': 'Steht die Wurzel allein, ⟦beide Seiten quadrieren⟧. Danach immer die Probe machen.',
    },
    'isolieren': {
        'einstieg': 'Bevor du ein Geschenk auspackst, nimmst du das Band ab. Genauso hier: Erst alles um die Wurzel herum weg, '
                    'dann quadrieren. Die Wurzel muss ⟦allein⟧ stehen.',
        'woerter': [['isoliert', 'die Wurzel steht allein auf einer Seite']],
        'bild': _g(_I[0]),
        'schritte': [
            {'text': 'Zuerst minus 4: 2 · √(x − 3) = 10.', 'bild': _g(*_I[:2])},
            {'text': 'Dann durch 2: √(x − 3) = 5. Die Wurzel ist isoliert.', 'bild': _g(*_I[:3])},
            {'text': 'Quadrieren: x − 3 = 25, also ⟦x = 28⟧.', 'bild': _g(*_I)},
            {'text': 'Probe: 2 · √25 + 4 = 14. Stimmt.'},
        ],
        'fehler': 'Zu früh quadrieren ist falsch, denn (a + b)² ist ⟦nicht a² + b²⟧. Erst die 4 abziehen, dann quadrieren.',
        'regel': 'Erst die Wurzel ⟦isolieren⟧, dann quadrieren. Zahlen davor und dahinter wie gewohnt wegbringen.',
    },
    'probe': {
        'einstieg': 'Ein Taschenrechner zeigt bei √ nie eine negative Zahl. √(x + 5) = −3 kann also nie stimmen. '
                    'Quadrieren findet trotzdem eine Zahl. Sie ist eine ⟦Scheinlösung⟧.',
        'woerter': [['Scheinlösung', 'eine Zahl, die beim Rechnen herauskommt, aber die Probe nicht besteht'],
                    ['L = { }', 'leere Lösungsmenge: Es gibt keine Lösung']],
        'bild': tab(['x', '√(x + 5)', 'rechts'], ['?', '?', '−3']),
        'schritte': [
            {'text': 'Quadrieren: x + 5 = 9, also x = 4.', 'bild': tab(['x', '√(x + 5)', 'rechts'], ['4', '?', '−3'])},
            {'text': 'Probe: √(4 + 5) = 3, nicht −3.', 'bild': tab(['x', '√(x + 5)', 'rechts'], ['4', '3', '−3'])},
            {'text': 'x = 4 ist eine Scheinlösung, also ⟦L = { }⟧.'},
        ],
        'fehler': 'L = {4} ist falsch. Die Probe zeigt ⟦3 ≠ −3⟧. Eine Wurzel ist nie negativ.',
        'regel': 'Quadrieren kann Scheinlösungen erzeugen. Darum jede Lösung mit der ⟦Probe⟧ prüfen.',
    },
    'zwei_seiten': {
        'einstieg': 'Jetzt steht auf beiden Seiten etwas mit x: √(x + 7) = x + 1. Quadrieren macht daraus eine ⟦quadratische Gleichung⟧. '
                    'Nur die Probe entscheidet, welche Lösung gilt.',
        'woerter': [['quadratische Gleichung', 'eine Gleichung mit x², z. B. x² + x − 6 = 0']],
        'bild': tab(_ZK, ['2', '?', '?'], ['−3', '?', '?']),
        'schritte': [
            {'text': 'Quadrieren: x + 7 = x² + 2x + 1.'},
            {'text': 'Umstellen: x² + x − 6 = 0. Lösungen: −3 und 2.'},
            {'text': 'Probe x = 2: √9 = 3 und 2 + 1 = 3. Stimmt.', 'bild': tab(_ZK, ['2', '3', '3 ✓'], ['−3', '?', '?'])},
            {'text': 'x = −3: links 2, rechts −2. Also ⟦L = {2}⟧.', 'bild': tab(_ZK, ['2', '3', '3 ✓'], ['−3', '2', '−2 ✗'])},
        ],
        'fehler': 'Beide Lösungen in L schreiben ist falsch. Bei x = −3 ist die rechte Seite ⟦negativ⟧, das ist eine Scheinlösung.',
        'regel': 'Quadrieren, quadratische Gleichung lösen, dann ⟦jede Lösung prüfen⟧. Nur bestandene Proben kommen in L.',
    },
    'sachaufgabe': {
        'einstieg': 'Du lässt einen Stein in einen Schacht fallen und zählst 3 Sekunden bis zum Aufprall. '
                    'Wie tief ist der Schacht? Die Formel ⟦t = √(h : 5)⟧ verrät es.',
        'woerter': [['h', 'die Fallhöhe in Metern'], ['t', 'die Fallzeit in Sekunden']],
        'bild': tab(['h in m', '5', '20', '?'], ['t in s', '1', '2', '3']),
        'schritte': [
            {'text': 'Einsetzen: √(h : 5) = 3.'},
            {'text': 'Quadrieren: h : 5 = 9.'},
            {'text': 'Mal 5: h = ⟦45⟧. Der Schacht ist 45 m tief.', 'bild': tab(['h in m', '5', '20', '45'], ['t in s', '1', '2', '3'])},
            {'text': 'Probe: √(45 : 5) = √9 = 3. Stimmt.'},
        ],
        'fehler': 'h = 15 ist falsch. Zuerst ⟦quadrieren⟧, h : 5 = 9, dann mal 5.',
        'regel': 'Gesucht ist die Größe unter der Wurzel? Wurzel isolieren, ⟦quadrieren⟧, auflösen.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-1) ----------
# Prüfungsvorbilder: Realschul-Abschlussprüfung Mathematik I (Bayern) und Jahrgangsstufentest 9 I: Definitionsmenge angeben,
# Wurzelgleichung mit Probe lösen, physikalische Formeln mit Wurzel (Fallzeit, Pendel, Sichtweite) nach der Größe unter der Wurzel
# auflösen. Typ übernommen, Wortlaut und Zahlen eigen.
def durchsicht(d):
    from _rsib1 import Z, A, L, nachtrag, finde
    T = lambda teil: finde(d, teil)
    nachtrag(d,
        umstufen={
            T('Darf man x = −5 in √(2x + 14) einsetzen?'): 2,
            T('Darf man x = 1 in √(3x − 6) einsetzen?'): 2,
            T('Darf man x = 11 in √(2x − 16) einsetzen?'): 2,
            T('Ein quadratisches Beet wird an jeder Seite um 2 m verlängert. Die neue Seitenlänge ist √A + 2 = 15 m.'): 2,
            T('Ein Ball fällt 3,5 s lang.'): 2,
        },
        ersetzen={
            T('Jemand löst √(2x − 19) = 1 so: 2x − 19 = 1, also x = 10.'):
                Z(3, 'Für welchen Wert c hat die Gleichung √(x + 1) = c die Lösung x = 15?', 4, '4',
                  'x = 15 einsetzen: √16 = 4. Also c = 4.', 'Setze x = 15 ein.'),
            T('Jemand quadriert √(x − 15) + 4 = 12 sofort'):
                Z(3, 'Löse 3 + √(2x − 1) = 2 · √(2x − 1).', 5, '(3**2 + 1)/2',
                  'Eine Wurzel weniger auf beiden Seiten: 3 = √(2x − 1). Quadrieren: 9 = 2x − 1 ⇒ x = 5. Probe: 3 + 3 = 2 · 3.',
                  'Behandle √(2x − 1) wie eine Unbekannte: Bringe alle Wurzeln auf eine Seite.'),
            T('Jemand quadriert √(x − 15) + 4 = 18 sofort'):
                Z(3, 'Löse √(x + 4) : 2 = 3.', 32, '6**2 - 4', 'Mal 2: √(x + 4) = 6. Quadrieren: x + 4 = 36 ⇒ x = 32. Probe: √36 : 2 = 3.',
                  'Erst die Wurzel allein stellen.'),
            T('Löse 5 · √(x + 1) + 17 = −23.'):
                A(3, 'Für welche Zahlen c hat die Gleichung √x = c eine Lösung?', 'für c ≥ 0', ['für jedes c', 'für c > 0', 'für c ≤ 0'],
                  'Eine Wurzel ist nie negativ. Für c ≥ 0 ist x = c² eine Lösung (auch c = 0 mit x = 0).', 'Welche Werte kann eine Wurzel annehmen?'),
            T('Ein quadratisches Beet wird an jeder Seite um 4 m verlängert. Die neue Seitenlänge ist √A + 4 = 24 m.'):
                Z(3, 'Für ein Pendel gilt näherungsweise T = 2 · √l (T in s, l in m). Ein Pendel braucht für eine Schwingung 4 s. Wie lang ist es?',
                  4, '(4/2)**2', '2 · √l = 4 ⇒ √l = 2 ⇒ l = 4 m.', 'Erst durch 2 teilen, dann quadrieren.', einheit='m'),
            T('Ein Ball fällt 1,5 s lang.'):
                Z(3, 'Für die Fallzeit gilt t = √(h : 5). Aus welcher Höhe fällt ein Stein doppelt so lange wie aus 20 m?',
                  80, '5*(2*2)**2', 'Aus 20 m: t = √4 = 2 s. Doppelt so lange: 4 s. √(h : 5) = 4 ⇒ h = 80 m – viermal so hoch.',
                  'Bestimme zuerst die Fallzeit aus 20 m.', einheit='m'),
            T('Ein quadratisches Beet wird an jeder Seite um 3 m verlängert. Die neue Seitenlänge ist √A + 3 = 6 m.'):
                Z(3, 'Für die Aufprallgeschwindigkeit gilt v = √(20 · h). Aus 5 m prallt man mit 10 m/s auf. Aus welcher Höhe prallt man mit 30 m/s auf?',
                  45, '30**2/20', '√(20h) = 30 ⇒ 20h = 900 ⇒ h = 45 m. Dreifache Geschwindigkeit braucht neunfache Höhe.', 'Quadriere beide Seiten.', einheit='m'),
            T('Aus welcher Höhe muss etwas fallen, um mit 35 m/s aufzuprallen?'):
                Z(3, 'Ein quadratisches Beet wird an jeder Seite um 3 m verlängert. Dabei wird seine Fläche viermal so groß. Wie groß war die Fläche vorher?',
                  9, '3*3', 'Alte Seite s: (s + 3)² = 4s² ⇒ s + 3 = 2s ⇒ s = 3 m. Fläche 9 m².', 'Viermal die Fläche heißt doppelte Seite.', einheit='m²'),
        },
        neu={
            'definitionsmenge': [
                L(3, 'Gib die Definitionsmenge des Terms √(x + 3) + √(5 − x) an.', 'D = {x | □ ≤ x ≤ □}', [-3, 5], ['-3', '5'],
                  'Beide Radikanden ≥ 0: x + 3 ≥ 0 ⇒ x ≥ −3 und 5 − x ≥ 0 ⇒ x ≤ 5.', 'Beide Wurzeln müssen definiert sein.'),
                L(3, 'Gib die Definitionsmenge der Gleichung √(2x + 4) = √(x − 1) + 2 an.', 'D = {x | x ≥ □}', [1], ['1'],
                  '2x + 4 ≥ 0 ⇒ x ≥ −2. x − 1 ≥ 0 ⇒ x ≥ 1. Beides zusammen: x ≥ 1.', 'Prüfe beide Wurzeln; die strengere Bedingung gilt.'),
                Z(3, 'Welche ist die kleinste ganze Zahl, die man in √(3x − 7) einsetzen darf?', 3, '3',
                  '3x − 7 ≥ 0 ⇒ x ≥ 7/3 ≈ 2,33. Die kleinste ganze Zahl ist 3.', 'Löse 3x − 7 ≥ 0 und schau auf die nächste ganze Zahl.'),
                A(3, 'Für welche x ist √(x²) definiert?', 'für alle x', ['nur für x ≥ 0', 'nur für x > 0', 'für kein x'],
                  'x² ist nie negativ, also ist der Radikand immer ≥ 0.', 'Kann x² negativ sein?'),
                Z(3, 'Für welchen Wert von a hat √(x − a) die Definitionsmenge D = {x | x ≥ −4}?', -4, '-4',
                  'x − a ≥ 0 ⇒ x ≥ a. Also a = −4.', 'Löse x − a ≥ 0 nach x auf.'),
            ],
            'quadrieren': [
                Z(3, 'Es gilt √(2x + 1) = 7. Welchen Wert hat dann √(8x + 4)?', 14, '2*7',
                  '8x + 4 = 4 · (2x + 1), also √(8x + 4) = 2 · √(2x + 1) = 14. Oder: x = 24 und √196 = 14.', 'Vergleiche 8x + 4 mit 2x + 1.'),
                L(3, 'Löse √(x² + 9) = 5.', 'x₁ = □; x₂ = □', [-4, 4], ['-4', '4'], 'Quadrieren: x² + 9 = 25 ⇒ x² = 16 ⇒ x = ±4. Probe: √25 = 5 für beide.',
                  'Nach dem Quadrieren entsteht eine reinquadratische Gleichung.'),
            ],
            'isolieren': [
                Z(3, 'Löse 10 − 2 · √(x + 1) = 4.', 8, '3**2 - 1', '−10: −2√(x + 1) = −6. Durch −2: √(x + 1) = 3 ⇒ x = 8. Probe: 10 − 2 · 3 = 4.',
                  'Achte auf das Minus vor der Wurzel.'),
                Z(3, 'Für welches c hat die Gleichung 2 · √x + c = 10 die Lösung x = 9?', 4, '10 - 2*3', 'x = 9: 2 · 3 + c = 10 ⇒ c = 4.', 'Setze x = 9 ein.'),
            ],
            'probe': [
                A(3, 'Bei √(x + 5) = 3 steht die Wurzel allein und rechts eine positive Zahl. Kann beim Quadrieren hier eine Scheinlösung entstehen?',
                  'Nein: x + 5 = 9 gibt x = 4, und √9 = 3 stimmt.', ['Ja, immer.', 'Ja: x = −4 ist eine Scheinlösung.', 'Nein, weil es gar keine Lösung gibt.'],
                  'Scheinlösungen entstehen, wenn rechts eine negative Zahl stehen könnte. Hier stimmt die Probe: √(4 + 5) = 3. Die Probe gehört trotzdem dazu.',
                  'Mach die Probe mit der gefundenen Lösung.'),
                A(3, 'Aus welcher Gleichung entsteht beim Quadrieren x − 3 = 16, sodass x = 19 eine Scheinlösung ist?', '√(x − 3) = −4',
                  ['√(x − 3) = 4', '√(x + 3) = 4', '√(x − 3) = 16'],
                  'Quadrieren von √(x − 3) = ±4 gibt x − 3 = 16. Probe mit x = 19: √16 = 4 ≠ −4, also Scheinlösung bei der Gleichung mit −4.',
                  'Welche Gleichung hat rechts eine negative Zahl?'),
            ],
            'zwei_seiten': [
                Z(3, 'Löse √(2x + 3) = x.', 3, '3', 'Quadrieren: 2x + 3 = x² ⇒ x² − 2x − 3 = 0 ⇒ x = 3 oder x = −1. Probe x = −1: √1 = 1 ≠ −1. L = {3}.',
                  'Quadrieren, quadratische Gleichung lösen, beide Werte prüfen.'),
                A(3, 'Für welche x gilt √(x²) = x?', 'für x ≥ 0', ['für alle x', 'nur für x = 0', 'für x ≤ 0'],
                  'Eine Wurzel ist nie negativ: √(x²) ist der Betrag |x|. Er ist gleich x, wenn x ≥ 0. Beispiel x = −3: √9 = 3 ≠ −3.',
                  'Probiere x = −3 aus.'),
            ],
            'sachaufgabe': [
                Z(3, 'Bis zum Horizont sieht man ungefähr d = 3,6 · √h weit (d in km, h in m Augenhöhe). Aus welcher Höhe sieht man 36 km weit?',
                  100, '(36/3.6)**2', '3,6 · √h = 36 ⇒ √h = 10 ⇒ h = 100 m.', 'Erst durch 3,6 teilen.', einheit='m'),
                Z(3, 'Für die Fallzeit gilt t = √(h : 5). Aus h Metern dauert der Fall 3 s länger als aus 20 m. Wie groß ist h?',
                  125, '5*(2 + 3)**2', 'Aus 20 m: 2 s. Also 5 s: √(h : 5) = 5 ⇒ h = 125 m.', 'Bestimme zuerst die Fallzeit aus 20 m.', einheit='m'),
                Z(3, 'Für die Aufprallgeschwindigkeit gilt v = √(20 · h). Bei welcher Höhe h (in m, h > 0) ist v in m/s genau so groß wie h?',
                  20, '20', '√(20h) = h ⇒ 20h = h² ⇒ h = 20 (h = 0 fällt weg). Probe: √400 = 20.', 'Setze v = h und quadriere.', einheit='m'),
                A(3, 'Für die Fallzeit gilt t = √(h : 5). Wie ändert sich die Fallzeit, wenn die Höhe verdoppelt wird?',
                  'Sie wird etwa 1,41-mal so lang (√2-mal).', ['Sie verdoppelt sich.', 'Sie vervierfacht sich.', 'Sie bleibt gleich.'],
                  't = √(2h : 5) = √2 · √(h : 5). √2 ≈ 1,41.', 'Probiere es mit 20 m und 40 m aus.'),
            ],
        })


# ---- STUFEN (Zwanzigste Runde, Zusatz RS/IB, Zweig stufen-rsib-1) ----
from _stufen_rsib1 import Stufen, stufen  # noqa: E402

ST = Stufen('gleichungen.wurzel', 20_91_8)
Z, A, L = ST.Z, ST.A, ST.L

# definitionsmenge
ST.stufenleiter('definitionsmenge', 'Die Definitionsmenge von √(x ± c) angeben; erkennen, ob eine Zahl eingesetzt werden darf.',
                'Radikanden mit Faktor vor x, Bereich am Zahlenstrahl, kleinste erlaubte ganze Zahl, Parameter aus der Definitionsmenge.',
                'Definitionsmenge von Gleichungen mit zwei Wurzeln, Radikand mit −x, √(x²) begründen, Fehler beim Teilen, Bedingung an a, Prüfungsaufgabe.')
ST.typ('definitionsmenge', '/^Gib die Definitionsmenge von √\\(x/', 'direkt')
ST.typ('definitionsmenge', 'Darf man x', 'erkennen')
ST.typ('definitionsmenge', 'Gib die Definitionsmenge von √(', 'mehrschritt')
ST.typ('definitionsmenge', '/^(Welche ist die kleinste ganze Zahl|Für welchen Wert von a)/', 'umkehr')
ST.typ('definitionsmenge', '/^Gib die Definitionsmenge (der Gleichung|des Terms)/', 'verknuepfen')
ST.typ('definitionsmenge', 'Welche Definitionsmenge hat', 'transfer')
ST.typ('definitionsmenge', 'Für welche x ist', 'begruenden')
ST.neu('definitionsmenge', 'darstellung', A('Welcher Bereich des Zahlenstrahls gehört zur Definitionsmenge von √(x − 3)?', 'alles ab 3 nach rechts, die 3 eingeschlossen',
       ['alles links von 3', 'alles ab −3 nach rechts', 'nur die 3'], 'x − 3 ≥ 0 heißt x ≥ 3: die 3 und alles rechts davon.', 'Wann ist x − 3 nicht negativ?'))
ST.neu('definitionsmenge', 'fehler', A('Jemand bestimmt für √(2x − 8) die Definitionsmenge D = {x | x ≥ 8}. Was stimmt?', 'Falsch: 2x − 8 ≥ 0 ⇒ 2x ≥ 8 ⇒ x ≥ 4.',
       ['Richtig.', 'Falsch: x ≥ −4.', 'Falsch: x ≥ 16.'], 'Erst 8 addieren, dann durch 2 teilen. Probe: √(2 · 5 − 8) = √2 ist erlaubt, obwohl 5 < 8.', 'Probiere x = 5.'))
ST.neu('definitionsmenge', 'parameter', A('Für welche Zahlen a liegt die 0 in der Definitionsmenge von √(x + a)?', 'für a ≥ 0', ['für a ≤ 0', 'für a > 1', 'für jedes a'],
       'x = 0 einsetzen: √a. Das ist erlaubt, wenn a ≥ 0.', 'Setze x = 0 ein.'))
ST.neu('definitionsmenge', 'pruefung', L('Gegeben ist die Gleichung √(x − 2) = √(10 − x). a) Gib die Definitionsmenge als □ ≤ x ≤ □ an. b) Löse die Gleichung.', 'a) □ ≤ x ≤ □; b) x = □', [2, 10, 6], ['2', '10', '12 // 2'],
       'a) x − 2 ≥ 0 ⇒ x ≥ 2 und 10 − x ≥ 0 ⇒ x ≤ 10. b) Quadrieren: x − 2 = 10 − x ⇒ 2x = 12 ⇒ x = 6 (liegt in D). Probe: √4 = √4.', 'Beide Radikanden müssen ≥ 0 sein.'))
ST.knobel('definitionsmenge', Z('Wie viele ganze Zahlen liegen in der Definitionsmenge von √(x + 4) + √(3 − x)?', 8, '3 - (-4) + 1',
          'x + 4 ≥ 0 ⇒ x ≥ −4 und 3 − x ≥ 0 ⇒ x ≤ 3. Ganze Zahlen von −4 bis 3: das sind 8.', 'Beide Wurzeln müssen erlaubt sein.'))
ST.knobel('definitionsmenge', L('Für welche Zahl x ist √(x − 7) + √(7 − x) definiert, und welchen Wert hat der Term dann?', 'x = □; Wert □', [7, 0], ['7', '0'],
          'x − 7 ≥ 0 heißt x ≥ 7, und 7 − x ≥ 0 heißt x ≤ 7. Beides gilt nur für x = 7. Dann ist der Term √0 + √0 = 0.', 'Schreibe beide Bedingungen auf.'))

# quadrieren
ST.stufenleiter('quadrieren', '√(x ± c) = d durch Quadrieren lösen und den ersten Schritt erkennen.',
                'Faktoren und Dezimalzahlen im Radikanden, c aus einer Lösung, Zahlenrätsel.',
                'Fehler „rechts nicht quadriert“, Wurzel aus einem Vielfachen, x² unter der Wurzel, √(x + 9) ≠ √x + 3, Parameter a, Zahlenrätsel rückwärts, Prüfungsaufgabe.')
ST.typ('quadrieren', '/^Löse √\\(x [−+] \\d+\\) = \\d+\\.$/', 'direkt')
ST.typ('quadrieren', 'Löse √(x²', 'verknuepfen')
ST.typ('quadrieren', 'Löse √(', 'mehrschritt')
ST.typ('quadrieren', 'Für welchen Wert c', 'umkehr')
ST.typ('quadrieren', 'Jemand löst', 'fehler')
ST.typ('quadrieren', 'Es gilt √(2x + 1)', 'verknuepfen')
ST.neu('quadrieren', 'erkennen', A('Was ist bei √(2x + 1) = 5 der erste Schritt?', 'beide Seiten quadrieren', ['beide Seiten durch 2 teilen', '1 von 5 abziehen', 'die Wurzel aus 5 ziehen'],
       'Die Wurzel steht allein. Quadrieren hebt sie auf: 2x + 1 = 25, dann x = 12.', 'Was macht eine Wurzel rückgängig?'))
ST.neu('quadrieren', 'einkleidung', Z('Wenn man von einer Zahl 5 abzieht, ist die Wurzel daraus 6. Welche Zahl ist es?', 41, '36 + 5',
       '√(x − 5) = 6 ⇒ x − 5 = 36 ⇒ x = 41. Probe: √36 = 6.', 'Schreibe die Aussage als Gleichung.'))
ST.neu('quadrieren', 'begruenden', A('Stimmt: √(x + 9) = √x + 3 für jede Zahl x ≥ 0?', 'Nein, z. B. x = 16: √25 = 5, aber √16 + 3 = 7.', ['Ja, immer.', 'Nur für x > 9.', 'Nein, die linke Seite ist immer größer.'],
       'Die Wurzel einer Summe ist nicht die Summe der Wurzeln. Gleich sind beide nur für x = 0.', 'Setze eine Zahl ein.'))
ST.neu('quadrieren', 'parameter', Z('Für welches a ist x = 8 die Lösung von √(a · x + 1) = 5?', 3, '(25 - 1) // 8',
       'Einsetzen: √(8a + 1) = 5 ⇒ 8a + 1 = 25 ⇒ a = 3.', 'Setze x = 8 ein und quadriere.'))
ST.neu('quadrieren', 'rueckwaerts', Z('Denk dir eine Zahl, verdopple sie, addiere 1 und ziehe die Wurzel. Du erhältst 9. Welche Zahl hast du gedacht?', 40, '(81 - 1) // 2',
       'Rückwärts: 9² = 81, 81 − 1 = 80, 80 : 2 = 40. Gleichung √(2x + 1) = 9.', 'Mache jeden Schritt rückwärts.'))
ST.neu('quadrieren', 'pruefung', L('Löse a) √(x + 7) = 5; b) √(3x − 2) = 4; c) √(x : 4) = 3.', 'a) □; b) □; c) □', [18, 6, 36], ['25 - 7', '(16 + 2) // 3', '9 * 4'],
       'a) x + 7 = 25 ⇒ 18. b) 3x − 2 = 16 ⇒ 6. c) x : 4 = 9 ⇒ 36.', 'Immer quadrieren, dann auflösen.'))
ST.knobel('quadrieren', Z('Löse √(√x) = 3.', 81, '9 * 9',
          'Quadrieren: √x = 9. Noch einmal quadrieren: x = 81. Probe: √81 = 9, √9 = 3.', 'Quadriere zweimal.'))
ST.knobel('quadrieren', Z('Für wie viele natürliche Zahlen n ≤ 100 ist √(n + 20) eine natürliche Zahl?', 6, '6',
          'n + 20 muss eine Quadratzahl zwischen 21 und 120 sein: 25, 36, 49, 64, 81, 100. Das sind 6 (n = 5, 16, 29, 44, 61, 80).', 'Welche Quadratzahlen kommen für n + 20 in Frage?'))

# isolieren
ST.stufenleiter('isolieren', 'Erst die Wurzel allein stellen (Zahl abziehen), dann quadrieren; ersten Schritt erkennen.',
                'Faktoren vor der Wurzel, Teilen, Zahlenrätsel, c aus einer Lösung.',
                'Fehler „sofort quadrieren“, Wurzel als neue Unbekannte, Wurzel mit Minus davor, Unmöglichkeit begründen, Bedingung an c, Prüfungsaufgabe mit Probe.')
ST.typ('isolieren', '/^Löse √\\(x [−+] \\d+\\) \\+ \\d+ = \\d+\\.$/', 'direkt')
ST.typ('isolieren', '/^Löse (\\d · √|√\\(x \\+ 4\\) :)/', 'mehrschritt')
ST.typ('isolieren', 'Jemand quadriert', 'fehler')
ST.typ('isolieren', 'Löse 3 + √', 'transfer')
ST.typ('isolieren', '/^Löse \\d+ −/', 'verknuepfen')
ST.typ('isolieren', 'Für welches c', 'umkehr')
ST.neu('isolieren', 'erkennen', A('Welcher erste Schritt stellt bei √(x − 1) + 6 = 10 die Wurzel allein?', 'auf beiden Seiten 6 abziehen', ['beide Seiten quadrieren', 'durch 6 teilen', '1 addieren'],
       'Erst muss die Wurzel allein stehen: √(x − 1) = 4. Dann quadrieren: x − 1 = 16, x = 17.', 'Was steht außer der Wurzel noch auf der linken Seite?'))
ST.neu('isolieren', 'einkleidung', Z('Die Wurzel aus x + 9, vermehrt um 2, ergibt 7. Wie groß ist x?', 16, '25 - 9',
       '√(x + 9) + 2 = 7 ⇒ √(x + 9) = 5 ⇒ x + 9 = 25 ⇒ x = 16.', 'Schreibe die Aussage als Gleichung.'))
ST.neu('isolieren', 'begruenden', A('Stimmt: √(x − 4) + 9 = 5 hat keine Lösung – das sieht man ohne zu rechnen?', 'Ja: Eine Wurzel ist nie negativ, also ist die linke Seite mindestens 9.',
       ['Nein, x = 0 ist eine Lösung.', 'Nein, man muss erst quadrieren.', 'Nein, x = 20 ist eine Lösung.'], '√(x − 4) ≥ 0, also √(x − 4) + 9 ≥ 9 > 5. Isoliert man, steht √(x − 4) = −4 da – unmöglich.', 'Wie klein kann eine Wurzel sein?'))
ST.neu('isolieren', 'parameter', A('Für welche Zahlen c hat √(x + 1) + c = 4 eine Lösung?', 'für c ≤ 4', ['für c ≥ 4', 'für c > 0', 'für jedes c'],
       '√(x + 1) = 4 − c. Das geht nur, wenn 4 − c ≥ 0, also c ≤ 4.', 'Stelle die Wurzel allein.'))
ST.neu('isolieren', 'pruefung', L('a) Löse √(x − 3) + 4 = 9. b) Löse 3 · √(x + 2) − 5 = 7. c) Probe zu b): Welchen Wert hat die linke Seite?', 'a) □; b) □; c) □', [28, 14, 7], ['25 + 3', '16 - 2', '3 * 4 - 5'],
       'a) √(x − 3) = 5 ⇒ x = 28. b) 3 · √(x + 2) = 12 ⇒ √(x + 2) = 4 ⇒ x = 14. c) 3 · √16 − 5 = 12 − 5 = 7. Stimmt.', 'Erst isolieren, dann quadrieren.'))
ST.knobel('isolieren', Z('Löse √x + √x + √x = 12.', 16, '4 * 4',
          '3 · √x = 12 ⇒ √x = 4 ⇒ x = 16. Wer jeden Summanden einzeln quadriert, landet bei 3x = 144 und x = 48 – das ist falsch.', 'Fasse gleiche Summanden zusammen.'))
ST.knobel('isolieren', Z('Löse √(x + 5) = √x + 1.', 4, '2 * 2',
          'Quadrieren: x + 5 = x + 2√x + 1 ⇒ 4 = 2√x ⇒ √x = 2 ⇒ x = 4. Probe: √9 = 3 und √4 + 1 = 3.', 'Quadriere – das x² taucht gar nicht auf.'))

# probe
ST.stufenleiter('probe', 'Mit einer Probe prüfen, ob eine Zahl Lösung ist; leere Lösungsmenge bei negativer rechter Seite erkennen.',
                'Definitionsmenge mitprüfen, isolieren und dann Unmöglichkeit erkennen, Gleichung zu einer Scheinlösung finden, unmögliches Zahlenrätsel.',
                'Sinn der Probe begründen, Bedingung an c, Fehler „Scheinlösung angegeben“, Parameter aus zwei Quadrierlösungen rückwärts, quadratische Gleichung mit einer echten Lösung, Prüfungsaufgabe.')
ST.typ('probe', 'Welche Lösungsmenge hat', 'erkennen')
ST.typ('probe', '/Mach die Probe\\.$/', 'direkt')
ST.typ('probe', 'Ist x =', 'mehrschritt')
ST.typ('probe', '/^Löse \\d · √/', 'mehrschritt')
ST.typ('probe', 'Aus welcher Gleichung', 'umkehr')
ST.typ('probe', '/^(Warum muss man|Bei √)/', 'begruenden')
ST.typ('probe', 'Für welche Zahlen c', 'parameter')
ST.typ('probe', 'Jemand löst', 'fehler')
ST.neu('probe', 'einkleidung', A('Jemand sagt: „Die Wurzel aus meiner Zahl plus 5 ergibt 2.“ Welche Zahl hat er?', 'Keine – die Aussage ist unmöglich.', ['9', '−9', '4'],
       '√x + 5 = 2 ⇒ √x = −3. Eine Wurzel ist nie negativ, also gibt es keine solche Zahl.', 'Stelle die Wurzel allein.'))
ST.neu('probe', 'rueckwaerts', L('Beim Quadrieren von √(x + a) = x − 1 erhielt jemand die Lösungen x = 3 und x = 0. Wie groß ist a, und welche Lösung ist echt?', 'a = □; echte Lösung x = □', [1, 3], ['(3 - 1) ** 2 - 3', '3'],
       'x = 3 eingesetzt in (x − 1)² = x + a: 4 = 3 + a ⇒ a = 1. Probe: x = 3: √4 = 2 und 3 − 1 = 2, stimmt. x = 0: √1 = 1, aber 0 − 1 = −1: Scheinlösung.', 'Setze eine der Lösungen in die quadrierte Gleichung ein.'))
ST.neu('probe', 'verknuepfen', A('Welche Lösungsmenge hat √(x − 1) = 1 − x?', 'L = {1}', ['L = { }', 'L = {1; 2}', 'L = {2}'],
       'Quadrieren: x − 1 = (1 − x)² ⇒ x² − 3x + 2 = 0 ⇒ x = 1 oder x = 2. Probe: x = 1: 0 = 0 stimmt. x = 2: √1 = 1, aber 1 − 2 = −1: Scheinlösung.', 'Quadrieren, quadratische Gleichung lösen, Probe.'))
ST.neu('probe', 'pruefung', L('Gegeben ist √(2x + 3) + 5 = 2. a) Isoliere die Wurzel: √(2x + 3) = □. b) Wie viele Lösungen hat die Gleichung?', 'a) □; b) □', [-3, 0], ['2 - 5', '0'],
       'a) √(2x + 3) = −3. b) Eine Wurzel ist nie negativ: keine Lösung, L = { }.', 'Erst isolieren, dann beurteilen.'))
ST.knobel('probe', Z('Für welche kleinste ganze Zahl k hat √(x + 4) = k − 2 eine Lösung, √(x + 4) = 2 − k aber keine?', 3, '3',
          'Die erste braucht k − 2 ≥ 0, also k ≥ 2. Die zweite soll keine Lösung haben: 2 − k < 0, also k > 2. Beides: k ≥ 3, kleinste ganze Zahl 3.', 'Wann hat √(…) = c eine Lösung?'))
ST.knobel('probe', Z('Wie viele dieser Gleichungen haben eine Lösung: √x = −1, √x = 0, √(x − 1) = 0, √(−x) = 2, √(x²) = −3?', 3, '3',
          '√x = −1: nein. √x = 0: x = 0. √(x − 1) = 0: x = 1. √(−x) = 2: −x = 4, x = −4 (erlaubt, denn −x = 4 ≥ 0). √(x²) = −3: nein. Also 3.', 'Achte auf negative rechte Seiten – und auf das Minus unter der Wurzel.'))

# zwei_seiten
ST.stufenleiter('zwei_seiten', 'Gleichungen mit je einer Wurzel auf beiden Seiten quadrieren und lösen; ersten Schritt erkennen.',
                'Wurzel = linearer Term: quadratische Gleichung lösen und Scheinlösung aussortieren, Zahlenrätsel, Parameter aus der Lösung.',
                'Probe bei zwei Kandidaten begründen, √(2x + 3) = x, √(x²) = x begründen, Fehler beim Quadrieren von x ± 1, Parameter für jedes a, Quadrate gleicher Seite, Prüfungsaufgabe.')
ST.typ('zwei_seiten', '/^Löse √\\([^)]*\\) = √/', 'direkt')
ST.typ('zwei_seiten', '/^(Löse √\\(x \\+ \\d+\\) = x|Welche Lösungsmenge hat)/', 'mehrschritt')
ST.typ('zwei_seiten', 'Beim Lösen', 'begruenden')
ST.typ('zwei_seiten', 'Löse √(2x + 3) = x', 'verknuepfen')
ST.typ('zwei_seiten', 'Für welche x gilt', 'begruenden')
ST.neu('zwei_seiten', 'erkennen', A('Was macht man bei √(2x + 1) = √(x + 5) zuerst?', 'beide Seiten quadrieren: 2x + 1 = x + 5', ['beide Seiten durch √x teilen', '2x + 1 = (x + 5)²', 'x = 5 einsetzen'],
       'Quadrieren hebt beide Wurzeln auf: 2x + 1 = x + 5 ⇒ x = 4. Probe: √9 = √9.', 'Was passiert mit √(…)²?'))
ST.neu('zwei_seiten', 'einkleidung', Z('Die Wurzel aus dem Dreifachen einer Zahl ist gleich der Wurzel aus der um 8 vergrößerten Zahl. Welche Zahl ist es?', 4, '8 // 2',
       '√(3x) = √(x + 8) ⇒ 3x = x + 8 ⇒ x = 4. Probe: √12 = √12.', 'Schreibe beide Seiten als Wurzel.'))
ST.neu('zwei_seiten', 'umkehr', Z('Die Gleichung √(4x + a) = √(2x + 10) hat die Lösung x = 3. Wie groß ist a?', 4, '16 - 12',
       'Einsetzen: √(12 + a) = √16 ⇒ 12 + a = 16 ⇒ a = 4.', 'Setze x = 3 ein.'))
ST.neu('zwei_seiten', 'fehler', A('Jemand löst √(x + 5) = x − 1 so: „x + 5 = x² + 1.“ Was stimmt?', 'Falsch: (x − 1)² = x² − 2x + 1; richtig ist x² − 3x − 4 = 0 und L = {4}.',
       ['Richtig.', 'Falsch: x + 5 = x² − 1.', 'Falsch: x + 5 = x − 1.'], 'Binomische Formel: (x − 1)² = x² − 2x + 1. Dann x² − 3x − 4 = 0 ⇒ x = 4 oder x = −1. Probe: nur x = 4 passt (√9 = 3 = 4 − 1).',
       'Multipliziere (x − 1)² aus.'))
ST.neu('zwei_seiten', 'parameter', A('Für welche Zahlen a hat √(x + a) = √(2x) die Lösung x = a?', 'für jedes a ≥ 0', ['nur für a = 0', 'nur für a = 1', 'für kein a'],
       'Einsetzen: √(2a) = √(2a) stimmt immer, solange 2a ≥ 0. Also für jedes a ≥ 0.', 'Setze x = a ein.'))
ST.neu('zwei_seiten', 'transfer', Z('Ein Quadrat hat die Fläche (3x + 4) cm², ein anderes (x + 16) cm². Für welches x sind ihre Seiten gleich lang?', 6, '12 // 2',
       'Gleiche Seiten heißt √(3x + 4) = √(x + 16), also gleiche Flächen: 3x + 4 = x + 16 ⇒ x = 6 (beide 22 cm²).', 'Die Seite ist die Wurzel aus der Fläche.'))
ST.neu('zwei_seiten', 'pruefung', L('Löse √(x + 7) = x + 1. a) Gib die beiden Lösungen der quadratischen Gleichung an (kleinere zuerst). b) Welche ist die echte Lösung?', 'a) □ und □; b) □', [-3, 2, 2], ['-3', '2', '2'],
       'Quadrieren: x + 7 = x² + 2x + 1 ⇒ x² + x − 6 = 0 ⇒ x = −3 oder x = 2. Probe: x = 2: √9 = 3 = 2 + 1. x = −3: √4 = 2, aber −3 + 1 = −2: Scheinlösung.', 'Quadrieren, lösen, Probe.'))
ST.knobel('zwei_seiten', Z('Löse √(x + √(x + √(x + …))) = 3 (die Wurzeln gehen unendlich weiter).', 6, '9 - 3',
          'Der Ausdruck unter der ersten Wurzel enthält wieder den ganzen Ausdruck, also 3: √(x + 3) = 3 ⇒ x + 3 = 9 ⇒ x = 6.', 'Was steht unter der ersten Wurzel?'))
ST.knobel('zwei_seiten', Z('Für wie viele ganze Zahlen x von −5 bis 5 gilt √(x²) = −x?', 6, '6',
          '√(x²) ist der Betrag von x. |x| = −x gilt für x ≤ 0: −5, −4, −3, −2, −1, 0. Also 6 Zahlen.', 'Was ergibt √(x²) für negative x?'))

# sachaufgabe
ST.stufenleiter('sachaufgabe', 'In t = √(h : 5), v = √(20h) oder a = √A eine Größe einsetzen und die andere bestimmen; die richtige Gleichung erkennen.',
                'Vergrößertes Beet, Fallzeit aus der Höhe, Pendel und Ball als Sachsituation.',
                'Wirkung von Verdoppeln begründen, Zeitunterschiede rückwärts, Horizont als Modell, v = h als Bedingung, Fehler „Quadrieren vergessen“, Prüfungsaufgabe.')
ST.typ('sachaufgabe', '/^Für die Fallzeit gilt t = √\\(h : 5\\) \\(h in m, t in s\\)\\. Ein Stein/', 'direkt')
ST.typ('sachaufgabe', '/^Für die Aufprallgeschwindigkeit nach einem Fall/', 'direkt')
ST.typ('sachaufgabe', 'Ein Quadrat hat die Seitenlänge', 'direkt')
ST.typ('sachaufgabe', '/Die neue Seitenlänge ist √A/', 'mehrschritt')
ST.typ('sachaufgabe', '/^(Für die Fallzeit gilt t = √\\(h : 5\\) \\(h in m, t in s\\)\\. Ein Ball|Für ein Pendel)/', 'einkleidung')
ST.typ('sachaufgabe', '/^(Für die Fallzeit gilt t = √\\(h : 5\\)\\. Aus welcher Höhe fällt|Für die Aufprallgeschwindigkeit gilt v = √\\(20 · h\\)\\. Aus 5)/', 'verknuepfen')
ST.typ('sachaufgabe', '/(viermal so groß|Aus h Metern)/', 'rueckwaerts')
ST.typ('sachaufgabe', 'Bis zum Horizont', 'transfer')
ST.typ('sachaufgabe', 'Für die Aufprallgeschwindigkeit gilt v = √(20 · h). Bei welcher', 'parameter')
ST.typ('sachaufgabe', 'Für die Fallzeit gilt t = √(h : 5). Wie ändert', 'begruenden')
ST.neu('sachaufgabe', 'erkennen', A('Für die Fallzeit gilt t = √(h : 5). Welche Gleichung muss man lösen, wenn der Fall 4 s dauert?', '√(h : 5) = 4', ['√(4 : 5) = h', 'h : 5 = 4', '√h = 4 · 5'],
       'Man setzt t = 4 ein: √(h : 5) = 4. Dann quadrieren: h : 5 = 16, h = 80 m.', 'Welche Größe ist bekannt, welche gesucht?'))
ST.neu('sachaufgabe', 'umkehr', Z('Für die Fallzeit gilt t = √(h : 5). Wie lange fällt ein Stein aus 45 m Höhe?', 3, '3',
       't = √(45 : 5) = √9 = 3 s.', 'Hier musst du nur einsetzen.', einheit='s'))
ST.neu('sachaufgabe', 'fehler', A('Jemand rechnet bei t = √(h : 5) und t = 3 s: „h = 3 · 5 = 15 m.“ Was stimmt?', 'Falsch: Erst quadrieren: h : 5 = 9, also h = 45 m.', ['Richtig.', 'Falsch: h = 3 : 5 = 0,6 m.', 'Falsch: h = 3² = 9 m.'],
       'Die Wurzel muss durch Quadrieren aufgehoben werden: h : 5 = 3² = 9. Probe: √(15 : 5) = √3 ≈ 1,7 s, nicht 3 s.', 'Mach die Probe mit 15 m.'))
ST.neu('sachaufgabe', 'pruefung', L('Für die Aufprallgeschwindigkeit gilt v = √(20 · h). a) Mit welcher Geschwindigkeit prallt etwas aus 20 m Höhe auf? b) Aus welcher Höhe prallt es mit 40 m/s auf?', 'a) □ m/s; b) □ m', [20, 80],
       ['20', '1600 // 20'], 'a) √400 = 20 m/s. b) √(20h) = 40 ⇒ 20h = 1 600 ⇒ h = 80 m.', 'Bei b) quadrieren.'))
ST.knobel('sachaufgabe', Z('Ein Stein wird aus einer Höhe fallen gelassen und schlägt nach 3 s auf (t = √(h : 5)). Ein zweiter Stein wird 1 s später an derselben Stelle losgelassen. Wie hoch ist der zweite Stein über dem Boden, wenn der erste aufschlägt?', 25, '45 - 20',
          'Die Höhe ist h = 5 · 3² = 45 m. Der zweite Stein ist erst 2 s gefallen: 5 · 2² = 20 m. Er ist noch 45 − 20 = 25 m über dem Boden.', 'Rechne aus t = √(h : 5) den Fallweg nach 2 s.', einheit='m'))
ST.knobel('sachaufgabe', Z('Bis zum Horizont sieht man etwa d = 3,6 · √h km weit (h in m). Um wie viele Meter muss man von 25 m Augenhöhe aus höher steigen, um doppelt so weit zu sehen?', 75, '4 * 25 - 25',
          'Doppelte Sichtweite heißt doppelte Wurzel, also vierfache Höhe: 4 · 25 = 100 m. Man muss 75 m höher steigen. Probe: 3,6 · 5 = 18 km, 3,6 · 10 = 36 km.', 'Wie ändert sich √h, wenn h vervierfacht wird?', einheit='m'))


if __name__ == '__main__':
    d = bauen('gleichungen.wurzel',
          'Wurzelgleichungen lösen: Definitionsmenge bestimmen, Wurzel allein stellen, quadrieren und mit der Probe Scheinlösungen erkennen.',
          ['Unter der Wurzel steht nie etwas Negatives: Radikand ≥ 0 liefert D.', 'Erst die Wurzel allein stellen, dann beide Seiten quadrieren.',
           'Eine Wurzel ist nie negativ: √(T) = negative Zahl hat keine Lösung.', 'Immer die Probe machen – Quadrieren kann Scheinlösungen erzeugen.'],
          [('Grundlagen', ['definitionsmenge', 'quadrieren', 'isolieren']), ('Probe und schwierigere Gleichungen', ['probe', 'zwei_seiten']),
           ('Anwenden', ['sachaufgabe'])],
          ETAPPEN, GEN)
    umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
    durchsicht(d)
    stufen('gleichungen.wurzel', ST)
