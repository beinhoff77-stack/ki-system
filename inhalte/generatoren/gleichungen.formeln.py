#!/usr/bin/env python3
"""Thema gleichungen.formeln – Formeln umstellen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, cz, ist_endlich, zt  # noqa: E402

META = {'thema_schluessel': 'gleichungen.formeln', 'thema_id': 4, 'block_id': 60, 'klasse': {'gym_by': 8}}

ETAPPEN = [
    {'lernziel': 'ein_schritt', 'titel': 'Formeln in einem Schritt umstellen',
     'regel': 'Eine Formel stellst du um wie eine Gleichung: Mit der ⟦Umkehrrechnung⟧ isolierst du die gesuchte Größe. Mal wird zu ⟦geteilt⟧, plus wird zu ⟦minus⟧.',
     'schritte': ['W = F · s nach s umstellen.', 's ist mit F multipliziert, also beide Seiten durch F teilen.', '⟦s = W : F⟧'],
     'probe': 'F = 5, s = 4 → W = 20. Und 20 : 5 = 4 ✓',
     'fehler': 'Aus W = F · s wird nicht s = W · F. Wer mit F ⟦multipliziert⟧ ist, wird durch F ⟦geteilt⟧.',
     '_verbot': ['W = F · s']},
    {'lernziel': 'zwei_schritte', 'titel': 'Formeln in zwei Schritten umstellen',
     'regel': 'Gehe ⟦rückwärts⟧ vor: Erst entfernst du, was zuletzt gerechnet wurde (meist + oder −), dann löst du das Mal oder Geteilt auf.',
     'schritte': ['s = a + v · t nach v umstellen.', '| − a: s − a = v · t', '| : t: ⟦v = (s − a) : t⟧'],
     'fehler': 'Aus s = a + v · t wird nicht v = s : t − a. Zuerst muss das ⟦+ a⟧ weg, sonst wird a auch durch t geteilt. Richtig: v = (s − a) : t.',
     '_verbot': ['s = a + v · t']},
    {'lernziel': 'einsetzen', 'titel': 'Umstellen und Werte einsetzen',
     'regel': 'Stelle zuerst die Formel nach der ⟦gesuchten Größe⟧ um, dann setze die Werte ⟦mit Einheiten⟧ ein und rechne aus.',
     'schritte': ['Ein Radfahrer fährt 45 km mit 18 km/h. Wie lange dauert es?', 'v = s : t umstellen: t = s : v', 't = 45 km : 18 km/h = ⟦2,5 h⟧'],
     'fehler': 't = v : s = 18 : 45 = 0,4 h ist falsch: Die Formel wurde falsch umgestellt. Prüfe mit den ⟦Einheiten⟧: km/h : km ergibt keine Zeit.',
     '_verbot': ['45 km mit 18 km/h']},
    {'lernziel': 'geometrie', 'titel': 'Fehlende Maße aus Formeln',
     'regel': 'Kennst du die ⟦Fläche⟧ oder das ⟦Volumen⟧, kannst du eine fehlende Länge berechnen: Formel aufschreiben, nach der Länge ⟦umstellen⟧, einsetzen.',
     'schritte': ['Ein Dreieck hat A = 24 cm² und g = 8 cm. Wie hoch ist es?', 'A = g · h : 2 → h = 2 · A : g', 'h = 48 cm² : 8 cm = ⟦6 cm⟧'],
     'fehler': 'h = A : g = 3 cm ist falsch: Beim Dreieck steht in der Formel noch ⟦: 2⟧. Beim Umstellen wird daraus · 2.',
     '_verbot': ['A = 24 cm² und g = 8 cm']},
    {'lernziel': 'pruefen', 'titel': 'Ist die Umstellung richtig?',
     'regel': 'Eine Umstellung prüfst du mit ⟦Zahlen⟧: Wähle Werte, rechne mit der Originalformel und setze in die umgestellte Formel ein. Es muss ⟦dasselbe⟧ herauskommen.',
     'schritte': ['Behauptung: Aus u = 4 · a folgt a = u − 4.', 'Test: a = 3 → u = 12. Dann u − 4 = 8, nicht 3.', 'Also ⟦falsch⟧. Richtig: a = u : 4.'],
     'fehler': 'Ein passendes Zahlenbeispiel beweist noch nichts: a = u − 4 stimmt zufällig für a = 4/3 (u = 16/3, u − 4 = 4/3). Teste deshalb ⟦zwei verschiedene⟧ Zahlen.',
     '_verbot': ['u = 4 · a']},
]

# Formel: (Anzeige, linke Seite, rechte Seite, {Variable: [(Anzeige, Python) – erste richtig]})
EIN = [
    ('v = s : t', 'v', 's/t', {'s': [('s = v · t', 'v*t'), ('s = v : t', 'v/t'), ('s = t : v', 't/v'), ('s = v + t', 'v+t')],
                               't': [('t = s : v', 's/v'), ('t = v · s', 'v*s'), ('t = v : s', 'v/s'), ('t = s − v', 's-v')]}),
    ('A = a · b', 'A', 'a*b', {'b': [('b = A : a', 'A/a'), ('b = A · a', 'A*a'), ('b = a : A', 'a/A'), ('b = A − a', 'A-a')]}),
    ('U = R · I', 'U', 'R*I', {'R': [('R = U : I', 'U/I'), ('R = U · I', 'U*I'), ('R = I : U', 'I/U')],
                               'I': [('I = U : R', 'U/R'), ('I = R : U', 'R/U'), ('I = U · R', 'U*R')]}),
    ('ρ = m : V', 'rho', 'm/V', {'m': [('m = ρ · V', 'rho*V'), ('m = ρ : V', 'rho/V'), ('m = V : ρ', 'V/rho')],
                                 'V': [('V = m : ρ', 'm/rho'), ('V = ρ : m', 'rho/m'), ('V = m · ρ', 'm*rho')]}),
    ('F = m · a', 'F', 'm*a', {'m': [('m = F : a', 'F/a'), ('m = F · a', 'F*a'), ('m = a : F', 'a/F'), ('m = F − a', 'F-a')]}),
    ('P = W : t', 'P', 'W/t', {'W': [('W = P · t', 'P*t'), ('W = P : t', 'P/t'), ('W = t : P', 't/P')],
                               't': [('t = W : P', 'W/P'), ('t = P : W', 'P/W'), ('t = W · P', 'W*P')]}),
    ('u = 4 · a', 'u', '4*a', {'a': [('a = u : 4', 'u/4'), ('a = u − 4', 'u-4'), ('a = 4 : u', '4/u'), ('a = 4 · u', '4*u')]}),
    ('V = G · h', 'V', 'G*h', {'h': [('h = V : G', 'V/G'), ('h = G : V', 'G/V'), ('h = V − G', 'V-G')],
                               'G': [('G = V : h', 'V/h'), ('G = V · h', 'V*h'), ('G = h : V', 'h/V')]}),
    ('p = F : A', 'p', 'F/A', {'F': [('F = p · A', 'p*A'), ('F = p : A', 'p/A'), ('F = A : p', 'A/p')],
                               'A': [('A = F : p', 'F/p'), ('A = p : F', 'p/F'), ('A = F · p', 'F*p')]}),
    ('d = 2 · r', 'd', '2*r', {'r': [('r = d : 2', 'd/2'), ('r = d − 2', 'd-2'), ('r = 2 · d', '2*d'), ('r = 2 : d', '2/d')]}),
    ('k = y : x', 'k', 'y/x', {'y': [('y = k · x', 'k*x'), ('y = k : x', 'k/x'), ('y = x : k', 'x/k')],
                               'x': [('x = y : k', 'y/k'), ('x = k : y', 'k/y'), ('x = k · y', 'k*y')]}),
    ('G = E − K', 'G', 'E-K', {'E': [('E = G + K', 'G+K'), ('E = G − K', 'G-K'), ('E = K − G', 'K-G')],
                               'K': [('K = E − G', 'E-G'), ('K = G − E', 'G-E'), ('K = E + G', 'E+G')]}),
]
ZWEI = [
    ('y = m · x + t', 'y', 'm*x+t', {'x': [('x = (y − t) : m', '(y-t)/m'), ('x = (y + t) : m', '(y+t)/m'), ('x = y : m − t', 'y/m-t'), ('x = (y − t) · m', '(y-t)*m')],
                                     't': [('t = y − m · x', 'y-m*x'), ('t = y + m · x', 'y+m*x'), ('t = m · x − y', 'm*x-y')]}),
    ('U = 2 · a + 2 · b', 'U', '2*a+2*b', {'a': [('a = (U − 2 · b) : 2', '(U-2*b)/2'), ('a = U : 2 − 2 · b', 'U/2-2*b'), ('a = (U − b) : 2', '(U-b)/2'), ('a = U − 2 · b', 'U-2*b')]}),
    ('A = g · h : 2', 'A', 'g*h/2', {'h': [('h = 2 · A : g', '2*A/g'), ('h = A : (2 · g)', 'A/(2*g)'), ('h = A : g', 'A/g'), ('h = 2 · g : A', '2*g/A')],
                                     'g': [('g = 2 · A : h', '2*A/h'), ('g = A : (2 · h)', 'A/(2*h)'), ('g = A · h : 2', 'A*h/2')]}),
    ('A = (a + c) · h : 2', 'A', '(a+c)*h/2', {'h': [('h = 2 · A : (a + c)', '2*A/(a+c)'), ('h = (a + c) : (2 · A)', '(a+c)/(2*A)'), ('h = 2 · A − (a + c)', '2*A-(a+c)'), ('h = A : (2 · (a + c))', 'A/(2*(a+c))')],
                                               'a': [('a = 2 · A : h − c', '2*A/h-c'), ('a = 2 · A : h + c', '2*A/h+c'), ('a = A : h − c', 'A/h-c'), ('a = 2 · A : (h − c)', '2*A/(h-c)')]}),
    ('V = G · h : 3', 'V', 'G*h/3', {'h': [('h = 3 · V : G', '3*V/G'), ('h = V : (3 · G)', 'V/(3*G)'), ('h = V : G', 'V/G'), ('h = 3 · G : V', '3*G/V')]}),
    ('F = 1,8 · C + 32', 'F', 'Fr(9,5)*C+32', {'C': [('C = (F − 32) : 1,8', '(F-32)/Fr(9,5)'), ('C = F : 1,8 − 32', 'F/Fr(9,5)-32'), ('C = (F + 32) : 1,8', '(F+32)/Fr(9,5)'), ('C = (F − 32) · 1,8', '(F-32)*Fr(9,5)')]}),
    ('Z = K · p : 100', 'Z', 'K*p/100', {'p': [('p = 100 · Z : K', '100*Z/K'), ('p = Z : (100 · K)', 'Z/(100*K)'), ('p = K · Z : 100', 'K*Z/100'), ('p = Z − K : 100', 'Z-K/100')],
                                         'K': [('K = 100 · Z : p', '100*Z/p'), ('K = Z : (100 · p)', 'Z/(100*p)'), ('K = p · Z : 100', 'p*Z/100')]}),
    ('K = G + n · p', 'K', 'G+n*p', {'n': [('n = (K − G) : p', '(K-G)/p'), ('n = K : p − G', 'K/p-G'), ('n = (K + G) : p', '(K+G)/p'), ('n = (K − G) · p', '(K-G)*p')],
                                     'p': [('p = (K − G) : n', '(K-G)/n'), ('p = K : n − G', 'K/n-G'), ('p = (K − n) : G', '(K-n)/G')]}),
    ('E = m · g · h', 'E', 'm*g*h', {'h': [('h = E : (m · g)', 'E/(m*g)'), ('h = E · m · g', 'E*m*g'), ('h = m · g : E', 'm*g/E'), ('h = E − m · g', 'E-m*g')]}),
    ('u = 2 · (a + b)', 'u', '2*(a+b)', {'a': [('a = u : 2 − b', 'u/2-b'), ('a = (u − b) : 2', '(u-b)/2'), ('a = u − 2 · b', 'u-2*b'), ('a = u : 2 + b', 'u/2+b')]}),
    ('M = (a + b) : 2', 'M', '(a+b)/2', {'a': [('a = 2 · M − b', '2*M-b'), ('a = M : 2 − b', 'M/2-b'), ('a = 2 · (M − b)', '2*(M-b)'), ('a = M − 2 · b', 'M-2*b')]}),
]
NAMEN = {'rho': 'ρ'}


def pruefe_bank():
    """Richtige Umstellung erfüllt die Formel, falsche nicht (an Zufallswerten nachgerechnet)."""
    import random
    Rp = random.Random(4)
    for anz, lhs, rhs, ziele in EIN + ZWEI:
        for var, opts in ziele.items():
            unterschied = {t: False for t, _ in opts[1:]}
            for k in range(5):
                env = {n: Fr(Rp.randint(2, 40), Rp.randint(1, 7)) + Fr(1, 11) for n in [*'vstAabUIRrmVFPWGhpdkyxEKCZnMugc', 'rho']}
                env['Fr'] = Fr
                env[lhs] = eval(rhs, {}, env)                     # passende Werte erzeugen
                soll = env[var]
                assert eval(opts[0][1], {}, env) == soll, (anz, var, opts[0])
                for t, py in opts[1:]:
                    if eval(py, {}, env) != soll: unterschied[t] = True
            assert all(unterschied.values()), (anz, unterschied)


pruefe_bank()


def umstell_aufgabe(R, bank, st, h):
    anz, lhs, rhs, ziele = R.choice(bank)
    var = R.choice(list(ziele))
    opts = ziele[var]
    v = NAMEN.get(var, var)
    return A(R, f'Stelle {anz} nach {v} um.', opts[0][0], [t for t, _ in opts[1:]],
             f'Richtig ist {opts[0][0]}. Probe mit Zahlen: Setze Werte in {anz} ein und vergleiche.', h)


def g_ein_schritt(R, st):
    if st == 3:
        # Zahl einsetzen nach dem Umstellen (Größe im Nenner)
        anz, var, frage = R.choice([('v = s : t', 't', 'v'), ('ρ = m : V', 'V', 'r'), ('p = F : A', 'A', 'p'), ('P = W : t', 't', 'P'), ('k = y : x', 'x', 'k')])
        z = Fr(R.randint(2, 25)) if R.random() < .6 else Fr(R.randint(5, 95), 10)
        g = Fr(R.randint(2, 12))
        oben = z * g
        sym = {'r': 'ρ'}.get(frage, frage)
        oben_n = {'v = s : t': 's', 'ρ = m : V': 'm', 'p = F : A': 'F', 'P = W : t': 'W', 'k = y : x': 'y'}[anz]
        return Z(f'Es gilt {anz}. Berechne {var} für {oben_n} = {zt(oben)} und {sym} = {zt(g)}.', z, f'{cz(oben)} / {cz(g)}',
                 f'Umstellen: {var} = {oben_n} : {sym} = {zt(oben)} : {zt(g)} = {zt(z)}.', f'Stelle zuerst nach {var} um. {var} steht im Nenner.')
    return umstell_aufgabe(R, EIN, st, 'Welche Rechnung wird mit der gesuchten Größe gemacht? Mache sie mit der Umkehrrechnung rückgängig.')


def g_zwei_schritte(R, st):
    if st == 1:
        bank = [f for f in ZWEI if f[0] in ('y = m · x + t', 'A = g · h : 2', 'V = G · h : 3', 'K = G + n · p', 'E = m · g · h')]
        return umstell_aufgabe(R, bank, st, 'Mache zuerst das Plus/Minus rückgängig, dann das Mal/Geteilt.')
    if st == 2 and R.random() < .55:
        return umstell_aufgabe(R, ZWEI, st, 'Gehe rückwärts: Was wurde zuletzt gerechnet? Das machst du zuerst rückgängig.')
    # Stufe 3: umstellen und Zahl berechnen
    art = R.choice(['lin', 'fahrenheit', 'trapez', 'mittel'])
    if art == 'lin':
        m, t = R.choice([2, 3, 4, 5, -2, -3]), R.randint(-9, 9)
        x = Fr(R.randint(-8, 8)); y = m * x + t
        return Z(f'Es gilt y = m · x + t mit m = {zt(m)} und t = {zt(t)}. Für welches x ist y = {zt(y)}?', x, f'({cz(y)} - ({t})) / ({m})',
                 f'x = (y − t) : m = ({zt(y)} − {"(" + zt(t) + ")" if t < 0 else zt(t)}) : {"(" + zt(m) + ")" if m < 0 else zt(m)} = {zt(x)}.', 'Stelle nach x um: x = (y − t) : m.')
    if art == 'fahrenheit':
        C = Fr(R.choice([-40, -20, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 100]))
        F = Fr(9, 5) * C + 32
        return Z(f'Für Temperaturen gilt F = 1,8 · C + 32 (F in Grad Fahrenheit, C in Grad Celsius). Wie viel Grad Celsius sind {zt(F)} °F?', C, f'({cz(F)} - 32) / 1.8',
                 f'C = (F − 32) : 1,8 = ({zt(F)} − 32) : 1,8 = {zt(C)}.', 'Stelle nach C um: erst − 32, dann : 1,8.', einheit='°C')
    if art == 'trapez':
        a, c, h = R.randint(4, 15), R.randint(2, 12), R.randint(2, 12)
        Af = Fr((a + c) * h, 2)
        return Z(f'Ein Trapez hat A = {zt(Af)} cm², a = {a} cm und h = {h} cm. Berechne c aus A = (a + c) · h : 2.', c, f'2 * {cz(Af)} / {h} - {a}',
                 f'c = 2 · A : h − a = {zt(2 * Af)} : {h} − {a} = {zt(2 * Af / h)} − {a} = {c} cm.', 'Stelle nach c um: · 2, dann : h, dann − a.', einheit='cm')
    a, b = R.randint(1, 6), R.randint(1, 6)
    M = Fr(a + b, 2)
    return Z(f'Der Mittelwert zweier Noten ist M = {zt(M)}. Eine Note ist {b}. Welche ist die andere? Nutze M = (a + b) : 2.', a, f'2 * {cz(M)} - {b}',
             f'a = 2 · M − b = {zt(2 * M)} − {b} = {a}.', 'Stelle nach a um: erst · 2, dann − b.')


def g_einsetzen(R, st):
    art = R.choice({1: ['rad', 'strom', 'dichte'], 2: ['rad', 'strom', 'dichte', 'zins_p', 'tarif'], 3: ['zins_K', 'tarif', 'kraft', 'arbeit']}[st])
    if art == 'rad':
        v = R.choice([12, 15, 16, 18, 20, 24, 25, 30, 40, 50, 60, 80, 90, 100, 120])
        t = Fr(R.choice([1, 2, 3, 5, 6, 8, 10, 12, 15]), R.choice([1, 2, 4]))
        s = v * t
        if s.denominator != 1: return g_einsetzen(R, st)
        return Z(f'Ein Fahrzeug legt {zt(s)} km mit der Durchschnittsgeschwindigkeit {v} km/h zurück. Wie lange braucht es? (v = s : t)', t, f'{cz(s)} / {v}',
                 f't = s : v = {zt(s)} km : {v} km/h = {zt(t)} h.', 'Stelle v = s : t nach t um. t steht im Nenner.', einheit='h')
    if art == 'strom':
        R_, I = R.choice([5, 10, 20, 25, 40, 50, 100, 200]), Fr(R.choice([1, 2, 3, 4, 5, 6, 8, 12]), R.choice([1, 2, 4, 10]))
        U = R_ * I
        return Z(f'An einem Widerstand von {R_} Ω liegt die Spannung {zt(U)} V. Wie groß ist die Stromstärke I? (U = R · I)', I, f'{cz(U)} / {R_}',
                 f'I = U : R = {zt(U)} V : {R_} Ω = {zt(I)} A.', 'Stelle U = R · I nach I um.', einheit='A')
    if art == 'dichte':
        stoff, rho = R.choice([('Aluminium', Fr(27, 10)), ('Eisen', Fr(79, 10)), ('Kupfer', Fr(89, 10)), ('Glas', Fr(5, 2)), ('Eis', Fr(9, 10))])
        V = Fr(R.choice([2, 4, 5, 10, 20, 25, 40, 50, 100]))
        m = rho * V
        if R.random() < .5:
            return Z(f'{stoff} hat die Dichte ρ = {zt(rho)} g/cm³. Ein Stück wiegt {zt(m)} g. Welches Volumen hat es? (ρ = m : V)', V, f'{cz(m)} / {cz(rho)}',
                     f'V = m : ρ = {zt(m)} g : {zt(rho)} g/cm³ = {zt(V)} cm³.', 'Stelle ρ = m : V nach V um.', einheit='cm³')
        return Z(f'{stoff} hat die Dichte ρ = {zt(rho)} g/cm³. Wie schwer ist ein Stück mit V = {zt(V)} cm³? (ρ = m : V)', m, f'{cz(rho)} * {cz(V)}',
                 f'm = ρ · V = {zt(rho)} · {zt(V)} = {zt(m)} g.', 'Stelle ρ = m : V nach m um.', einheit='g')
    if art == 'zins_p':
        K, p = R.choice([200, 400, 500, 800, 1000, 1200, 2000, 2500, 5000]), Fr(R.choice([5, 10, 15, 20, 25, 30, 40]), 10)
        Zi = K * p / 100
        return Z(f'Ein Guthaben von {zt(K)} € bringt in einem Jahr {zt(Zi)} € Zinsen. Wie hoch ist der Zinssatz p in Prozent? (Z = K · p : 100)', p, f'100 * {cz(Zi)} / {K}',
                 f'p = 100 · Z : K = 100 · {zt(Zi)} : {zt(K)} = {zt(p)}.', 'Stelle nach p um: erst · 100, dann : K.', einheit='%')
    if art == 'zins_K':
        K, p = R.choice([300, 600, 750, 1500, 2400, 3000, 4000, 6000]), Fr(R.choice([5, 10, 15, 20, 25, 30, 40]), 10)
        Zi = K * p / 100
        return Z(f'Bei einem Zinssatz von {zt(p)} % bekommt man in einem Jahr {zt(Zi)} € Zinsen. Wie groß ist das Guthaben K? (Z = K · p : 100)', K, f'100 * {cz(Zi)} / {cz(p)}',
                 f'K = 100 · Z : p = 100 · {zt(Zi)} : {zt(p)} = {zt(K)} €.', 'Stelle nach K um: erst · 100, dann : p.', einheit='€')
    if art == 'tarif':
        G, p = Fr(R.choice([5, 8, 10, 12, 15])), Fr(R.choice([5, 10, 15, 20, 25]), 10)
        n = R.randint(4, 30)
        K = G + n * p
        return Z(f'Ein Tarif kostet K = G + n · p mit G = {zt(G)} € und p = {zt(p)} € pro Stunde. Die Rechnung beträgt {zt(K)} €. Wie viele Stunden n wurden genutzt?', n, f'({cz(K)} - {cz(G)}) / {cz(p)}',
                 f'n = (K − G) : p = ({zt(K)} − {zt(G)}) : {zt(p)} = {n}.', 'Stelle nach n um: erst − G, dann : p.')
    if art == 'kraft':
        m, a = Fr(R.choice([2, 4, 5, 8, 10, 20, 25, 50, 80])), Fr(R.choice([1, 2, 3, 4, 5, 15, 25]), R.choice([1, 2, 10]))
        F = m * a
        return Z(f'Eine Kraft von {zt(F)} N beschleunigt einen Körper mit a = {zt(a)} m/s². Welche Masse hat er? (F = m · a)', m, f'{cz(F)} / {cz(a)}',
                 f'm = F : a = {zt(F)} : {zt(a)} = {zt(m)} kg.', 'Stelle F = m · a nach m um.', einheit='kg')
    m, h = Fr(R.choice([2, 5, 10, 20, 50, 60, 75])), Fr(R.choice([2, 3, 4, 5, 8, 10, 12, 15]))
    E = m * 10 * h
    return Z(f'Die Lageenergie ist E = m · g · h mit g = 10 N/kg. Ein Körper mit m = {zt(m)} kg hat E = {zt(E)} J. In welcher Höhe h ist er?', h, f'{cz(E)} / ({cz(m)} * 10)',
             f'h = E : (m · g) = {zt(E)} : ({zt(m)} · 10) = {zt(h)} m.', 'Stelle nach h um: durch das Produkt m · g teilen.', einheit='m')


def g_geometrie(R, st):
    art = R.choice({1: ['rechteck', 'quadrat', 'parallelogramm'], 2: ['dreieck', 'quader', 'rechteck_u', 'prisma'], 3: ['trapez', 'pyramide', 'quader', 'dreieck']}[st])
    if art == 'rechteck':
        a, b = R.randint(3, 20), R.randint(2, 15)
        return Z(f'Ein Rechteck hat den Flächeninhalt {a * b} cm² und die Länge {a} cm. Wie breit ist es?', b, f'{a * b} / {a}',
                 f'A = a · b → b = A : a = {a * b} : {a} = {b} cm.', 'Stelle A = a · b nach b um.', einheit='cm')
    if art == 'quadrat':
        a = Fr(R.randint(3, 60), R.choice([1, 2]))
        return Z(f'Ein Quadrat hat den Umfang {zt(4 * a)} cm. Wie lang ist eine Seite?', a, f'{cz(4 * a)} / 4',
                 f'u = 4 · a → a = u : 4 = {zt(4 * a)} : 4 = {zt(a)} cm.', 'Stelle u = 4 · a nach a um.', einheit='cm')
    if art == 'parallelogramm':
        g, h = R.randint(3, 20), R.randint(2, 15)
        return Z(f'Ein Parallelogramm hat A = {g * h} cm² und die Grundseite g = {g} cm. Berechne die Höhe h.', h, f'{g * h} / {g}',
                 f'A = g · h → h = A : g = {g * h} : {g} = {h} cm.', 'Stelle A = g · h nach h um.', einheit='cm')
    if art == 'dreieck':
        g, h = R.randint(3, 20), R.randint(2, 16)
        Af = Fr(g * h, 2)
        return Z(f'Ein Dreieck hat A = {zt(Af)} cm² und die Grundseite g = {g} cm. Berechne die Höhe h.', h, f'2 * {cz(Af)} / {g}',
                 f'A = g · h : 2 → h = 2 · A : g = {zt(2 * Af)} : {g} = {h} cm.', 'Stelle A = g · h : 2 nach h um. Vergiss die 2 nicht.', einheit='cm')
    if art == 'quader':
        a, b, c = R.randint(2, 12), R.randint(2, 10), R.randint(2, 15)
        return Z(f'Ein Quader hat das Volumen {a * b * c} cm³, die Länge {a} cm und die Breite {b} cm. Wie hoch ist er?', c, f'{a * b * c} / ({a} * {b})',
                 f'V = a · b · c → c = V : (a · b) = {a * b * c} : {a * b} = {c} cm.', 'Teile das Volumen durch die Grundfläche a · b.', einheit='cm')
    if art == 'rechteck_u':
        a, b = R.randint(3, 25), R.randint(2, 20)
        return Z(f'Ein Rechteck hat den Umfang {2 * (a + b)} cm und die Länge {a} cm. Wie breit ist es?', b, f'{2 * (a + b)} / 2 - {a}',
                 f'u = 2 · (a + b) → b = u : 2 − a = {a + b} − {a} = {b} cm.', 'Stelle u = 2 · (a + b) nach b um: erst : 2, dann − a.', einheit='cm')
    if art == 'prisma':
        G, h = R.randint(4, 40), R.randint(2, 15)
        return Z(f'Ein Prisma hat das Volumen {G * h} cm³ und die Grundfläche G = {G} cm². Wie hoch ist es?', h, f'{G * h} / {G}',
                 f'V = G · h → h = V : G = {G * h} : {G} = {h} cm.', 'Stelle V = G · h nach h um.', einheit='cm')
    if art == 'pyramide':
        G, h = R.randint(4, 40), R.randint(2, 15)
        V = Fr(G * h, 3)
        if not ist_endlich(V): return g_geometrie(R, st)
        return Z(f'Eine Pyramide hat das Volumen {zt(V)} cm³ und die Grundfläche {G} cm². Wie hoch ist sie? (V = G · h : 3)', h, f'3 * {cz(V)} / {G}',
                 f'h = 3 · V : G = {zt(3 * V)} : {G} = {h} cm.', 'Stelle V = G · h : 3 nach h um.', einheit='cm')
    a, c, h = R.randint(5, 16), R.randint(2, 12), R.randint(2, 12)
    Af = Fr((a + c) * h, 2)
    return Z(f'Ein Trapez hat A = {zt(Af)} cm² und die parallelen Seiten a = {a} cm und c = {c} cm. Berechne die Höhe h.', h, f'2 * {cz(Af)} / ({a} + {c})',
             f'A = (a + c) · h : 2 → h = 2 · A : (a + c) = {zt(2 * Af)} : {a + c} = {h} cm.', 'Stelle nach h um: · 2, dann durch (a + c).', einheit='cm')


def g_pruefen(R, st):
    bank = EIN if st == 1 else (ZWEI if st == 3 else EIN + ZWEI)
    anz, lhs, rhs, ziele = R.choice(bank)
    var = R.choice(list(ziele))
    opts = ziele[var]
    behauptet = R.choice(opts[:1] * 2 + opts[1:])
    richtig = behauptet == opts[0]
    falsch_rest = [t for t, _ in opts[1:] if t != behauptet[0]]
    if richtig:
        antw, andere = 'Ja, die Umstellung ist richtig.', [f'Nein, richtig wäre {t}.' for t in falsch_rest[:2]]
        if len(andere) < 2: andere.append('Nein, man kann die Formel nicht nach dieser Größe umstellen.')
    else:
        antw, andere = f'Nein, richtig wäre {opts[0][0]}.', ['Ja, die Umstellung ist richtig.'] + [f'Nein, richtig wäre {t}.' for t in falsch_rest[:1]]
    v = NAMEN.get(var, var)
    return A(R, f'Jemand stellt {anz} nach {v} um und erhält {behauptet[0]}. Stimmt das?', antw, andere,
             f'Richtig ist {opts[0][0]}. Probe: Wähle Zahlen für die anderen Größen, berechne {NAMEN.get(lhs, lhs)} mit {anz} und setze in die Umstellung ein.',
             'Mache die Probe mit einfachen Zahlen.')


GEN = {'ein_schritt': g_ein_schritt, 'zwei_schritte': g_zwei_schritte, 'einsetzen': g_einsetzen, 'geometrie': g_geometrie, 'pruefen': g_pruefen}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Umstellen', ['ein_schritt', 'zwei_schritte', 'pruefen']), ('Anwenden', ['einsetzen', 'geometrie'])],
         'Formeln aus Geometrie, Physik und Alltag nach einer gesuchten Größe auflösen und damit rechnen.',
         ['Umkehrrechnung: Mal ↔ Geteilt, Plus ↔ Minus.', 'Rückwärts vorgehen: Was zuletzt gerechnet wurde, wird zuerst rückgängig gemacht.',
          'Probe mit Zahlen zeigt, ob eine Umstellung stimmt.'])
