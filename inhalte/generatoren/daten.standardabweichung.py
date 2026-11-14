#!/usr/bin/env python3
"""Thema daten.standardabweichung – Standardabweichung (IB MYP 4, etwa Klasse 9)."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403

start(7904)


def liste(xs):
    return '; '.join(dz(x) for x in xs)


def mw(xs):
    return Fr(sum(xs), len(xs))


def var(xs):
    m = mw(xs)
    return sum((Fr(x) - m) ** 2 for x in xs) / len(xs)


def datensatz(n, lo, hi, quadrat=None, ganz_mw=True, var_endlich=True):
    """Zufällige Werte mit ganzzahligem Mittelwert; quadrat=True: Varianz ist Quadratzahl (σ ganz)."""
    for _ in range(3000):
        xs = [R.randint(lo, hi) for _ in range(n)]
        if len(set(xs)) < 3: continue
        m = mw(xs)
        if ganz_mw and m.denominator != 1: continue
        v = var(xs)
        if v == 0: continue
        if quadrat is True:
            if v.denominator != 1 or math.isqrt(int(v)) ** 2 != int(v): continue
        elif quadrat is False:
            if v.denominator == 1 and math.isqrt(int(v)) ** 2 == int(v): continue
        if var_endlich and not endlich(v): continue
        return xs
    return None


def quad_weg(xs):
    m = mw(xs)
    return ' + '.join(f'{kl(Fr(x) - m)}²' for x in xs)


ETAPPEN = [
    {'lernziel': 'abweichung', 'titel': 'Abweichungen vom Mittelwert',
     'regel': 'Der ⟦Mittelwert⟧ (mean) x̄ ist die Summe aller Werte geteilt durch ihre Anzahl. Die ⟦Abweichung⟧ (deviation) eines Wertes ist ⟦Wert − Mittelwert⟧. Sie ist positiv über und negativ unter dem Mittelwert. Alle Abweichungen zusammen ergeben immer ⟦0⟧.',
     'schritte': ['Werte: 4; 7; 10. Mittelwert: (4 + 7 + 10) : 3 = 7.', 'Abweichungen: 4 − 7 = −3, 7 − 7 = 0, 10 − 7 = ⟦3⟧.'],
     'probe': '(−3) + 0 + 3 = 0 ✓',
     'bild': {'typ': 'koordinaten', 'x': [0, 12], 'y': [0, 2], 'schritt_y': 1, 'name_y': ' ', 'senkrecht': [7],
              'punkte': [{'x': 4, 'y': 1, 'name': '4 (−3)'}, {'x': 7, 'y': 1, 'name': 'x̄ = 7'}, {'x': 10, 'y': 1, 'name': '10 (+3)'}],
              'strecken': [[4, 0.6, 7, 0.6, 'gestrichelt'], [7, 0.6, 10, 0.6, 'gestrichelt']]},
     'fehler': 'Die Abweichungen einfach zu addieren, um die Streuung zu messen, geht nicht: (−3) + 0 + 3 = 0, obwohl die Werte streuen. ⟦Plus und Minus heben sich auf⟧ – deshalb quadriert man sie.'},
    {'lernziel': 'varianz', 'titel': 'Die Varianz berechnen',
     'regel': 'Die ⟦Varianz⟧ (variance) ist der ⟦Mittelwert der quadrierten Abweichungen⟧: jede Abweichung quadrieren, alles addieren, durch die ⟦Anzahl n⟧ teilen. Durch das Quadrieren werden alle Beiträge positiv.',
     'schritte': ['Werte: 2; 4; 6; 8. Mittelwert: 20 : 4 = 5.', 'Abweichungen: −3; −1; 1; 3. Quadrate: 9; 1; 1; 9.', 'Varianz: (9 + 1 + 1 + 9) : 4 = ⟦5⟧.'],
     'probe': 'Alle Quadrate sind positiv, die Varianz kann nicht negativ sein ✓',
     'fehler': '(−3)² = −9 ist falsch: Minus mal Minus ergibt Plus, ⟦(−3)² = 9⟧. Eine Varianz ist nie negativ.'},
    {'lernziel': 'sigma', 'titel': 'Die Standardabweichung σ',
     'regel': 'Die ⟦Standardabweichung⟧ (standard deviation) ⟦σ⟧ ist die ⟦Wurzel aus der Varianz⟧. Sie hat dieselbe Einheit wie die Daten und gibt an, wie weit die Werte ⟦typischerweise⟧ vom Mittelwert entfernt liegen.',
     'schritte': ['Werte: 3; 5; 7; 9; 11 (in cm). Mittelwert: 35 : 5 = 7.', 'Quadrate der Abweichungen: 16; 4; 0; 4; 16. Varianz: 40 : 5 = 8.', 'σ = √8 ≈ ⟦2,83 cm⟧.'],
     'probe': '2,83² ≈ 8,0 ✓',
     'fehler': 'Die Varianz 8 als Standardabweichung anzugeben ist falsch: Die Varianz hat die Einheit cm². Erst die ⟦Wurzel⟧ ergibt σ in cm.'},
    {'lernziel': 'eigenschaften', 'titel': 'Wie verändert sich σ?',
     'regel': 'Addiert man zu allen Werten ⟦dieselbe Zahl⟧, verschiebt sich nur der Mittelwert, ⟦σ bleibt gleich⟧. Multipliziert man alle Werte mit k, wird ⟦σ mit |k| multipliziert⟧. Sind alle Werte gleich, ist ⟦σ = 0⟧.',
     'schritte': ['Klassenarbeit: σ = 4 Punkte. Jeder bekommt 3 Bonuspunkte.', 'Alle Werte rücken um 3 nach oben, die Abstände bleiben: ⟦σ = 4⟧.'],
     'probe': 'Beispiel 1; 5 (σ = 2) → 4; 8 (σ = 2) ✓',
     'fehler': 'Bei 3 Bonuspunkten σ = 4 + 3 = 7 zu rechnen ist falsch: Die Werte ⟦verschieben sich gemeinsam⟧, der Abstand zum Mittelwert ändert sich nicht.'},
    {'lernziel': 'deuten', 'titel': 'Streuung vergleichen und deuten',
     'regel': 'Bei ähnlichem Mittelwert gilt: ⟦kleines σ⟧ = Werte liegen ⟦eng beieinander⟧ (gleichmäßig), ⟦großes σ⟧ = Werte ⟦streuen stark⟧. Viele Werte liegen im Bereich ⟦x̄ − σ bis x̄ + σ⟧.',
     'schritte': ['Klasse A: x̄ = 12 Punkte, σ = 2. Klasse B: x̄ = 12 Punkte, σ = 5.', 'Gleicher Durchschnitt, aber in A liegen die Ergebnisse ⟦enger beieinander⟧. Bereich in A: 10 bis 14 Punkte.'],
     'probe': '12 − 2 = 10 und 12 + 2 = 14 ✓',
     'fehler': '„Klasse B ist besser, weil ihr σ größer ist“ ist falsch: σ sagt nichts darüber, ⟦wer besser⟧ ist, nur wie ⟦unterschiedlich⟧ die Ergebnisse sind.'},
]


def g_abweichung(s):
    n = R.choice([4, 5, 6]) if s == 1 else R.choice([5, 6, 8])
    xs = datensatz(n, 2, 30 if s < 3 else 60, var_endlich=False)
    if not xs: return None
    m = mw(xs)
    art = R.choice({1: ['mittel', 'abw'], 2: ['abw', 'abw_neg', 'mittel'], 3: ['fehlend', 'summe', 'betrag']}[s])
    if art == 'mittel':
        return zahl(f'Berechne den Mittelwert x̄ der Werte {liste(xs)}.', f'Summe {sum(xs)}, Anzahl {n}: x̄ = {sum(xs)} : {n} = {dz(m)}.',
                    'Alle Werte addieren und durch die Anzahl teilen.', m, f'({" + ".join(map(str, xs))}) / {n}')
    if art in ('abw', 'abw_neg'):
        kand = [x for x in xs if (x < m) == (art == 'abw_neg') and x != m]
        if not kand: return None
        x = R.choice(kand)
        return zahl(f'Werte: {liste(xs)} (Mittelwert {dz(m)}). Berechne die Abweichung des Wertes {x} vom Mittelwert.', f'Abweichung = {x} − {dz(m)} = {dz(x - m)}.',
                    'Abweichung = Wert − Mittelwert. Unter dem Mittelwert ist sie negativ.', x - m, f'{x} - {m}')
    if art == 'fehlend':
        k = R.randrange(n)
        rest = xs[:k] + xs[k + 1:]
        return zahl(f'{n} Werte haben den Mittelwert {dz(m)}. Bekannt sind {liste(rest)}. Wie groß ist der fehlende Wert?',
                    f'Summe aller Werte: {n} · {dz(m)} = {dz(n * m)}. Fehlender Wert: {dz(n * m)} − {sum(rest)} = {xs[k]}.',
                    'Mittelwert mal Anzahl ergibt die Summe aller Werte.', xs[k], f'{n} * {m} - {sum(rest)}')
    if art == 'summe':
        r = '0 – die Abweichungen heben sich immer auf.'
        return auswahl(f'Werte: {liste(xs)}, Mittelwert {dz(m)}. Wie groß ist die Summe aller Abweichungen vom Mittelwert?', r,
                       [f'{dz(sum(abs(x - m) for x in xs))}', f'{dz(m)}', f'{dz(sum(xs))}'],
                       f'Abweichungen: {"; ".join(dz(x - m) for x in xs)}. Ihre Summe ist 0 – das gilt für jeden Datensatz.',
                       'Rechne zwei, drei Abweichungen aus – was fällt beim Addieren auf?')
    # betrag: größte Abweichung
    gr = max(xs, key=lambda x: abs(x - m))
    if sum(1 for x in xs if abs(x - m) == abs(gr - m)) > 1: return None
    return zahl(f'Werte: {liste(xs)}. Welcher Wert weicht am stärksten vom Mittelwert ab? Gib den Wert an.',
                f'x̄ = {dz(m)}. Abweichungen: {"; ".join(dz(x - m) for x in xs)}. Am weitesten weg ist {gr} (Abstand {dz(abs(gr - m))}).',
                'Berechne zuerst den Mittelwert und vergleiche dann die Abstände ohne Vorzeichen.', gr, f'{gr}')


def g_varianz(s):
    n = R.choice([4, 5]) if s == 1 else R.choice([4, 5, 8])
    xs = datensatz(n, 1, 12 if s == 1 else 25)
    if not xs: return None
    m, v = mw(xs), var(xs)
    art = R.choice({1: ['voll', 'quadrate'], 2: ['voll', 'voll', 'aus_abw'], 3: ['fehler', 'voll', 'vergleich']}[s])
    weg = f'x̄ = {dz(m)}. Quadrate der Abweichungen: {quad_weg(xs)} = {dz(v * n)}. Varianz: {dz(v * n)} : {n} = {dz(v)}.'
    c = f'(({") ** 2 + (".join(f"{x} - {m}" for x in xs)}) ** 2) / {n}'
    if art == 'voll':
        return zahl(f'Berechne die Varianz der Werte {liste(xs)}.', weg, 'Mittelwert, Abweichungen, Quadrate, Summe, durch n teilen.', v, c)
    if art == 'quadrate':
        return zahl(f'Werte: {liste(xs)}, Mittelwert {dz(m)}. Berechne die Summe der quadrierten Abweichungen.',
                    f'{quad_weg(xs)} = {dz(v * n)}.', 'Jede Abweichung quadrieren, dann addieren.', v * n, f'({") ** 2 + (".join(f"{x} - {m}" for x in xs)}) ** 2')
    if art == 'aus_abw':
        ab = [Fr(x) - m for x in xs]
        return zahl(f'Die Abweichungen von {n} Werten vom Mittelwert sind {liste(ab)}. Berechne die Varianz.',
                    f'Quadrate: {"; ".join(dz(a * a) for a in ab)}. Summe {dz(v * n)}, geteilt durch {n}: {dz(v)}.',
                    'Die Abweichungen sind schon da: quadrieren, addieren, durch die Anzahl teilen.', v, c)
    if art == 'fehler':
        neg = [x for x in xs if x < m]
        if not neg: return None
        x = neg[0]
        r = f'({dz(x - m)})² = {dz((x - m) ** 2)}, nicht {dz(-(x - m) ** 2)}. Die Varianz ist {dz(v)}.'
        falsch_v = sum((Fr(y) - m) ** 2 if y >= m else -(Fr(y) - m) ** 2 for y in xs) / n
        return auswahl(f'Werte: {liste(xs)}, x̄ = {dz(m)}. Mia rechnet die Varianz und erhält {dz(falsch_v)}, weil sie ({dz(x - m)})² = {dz(-(x - m) ** 2)} gesetzt hat. Was stimmt?', r,
                       [f'Mia hat recht, die Varianz ist {dz(falsch_v)}.', f'Man muss durch {n - 1} teilen, dann stimmt es.', f'Die Varianz ist {dz(v * n)}.'],
                       f'Quadrate sind nie negativ. Richtig: {weg}', 'Was ergibt eine negative Zahl zum Quadrat?')
    ys = datensatz(n, 1, 25)
    if not ys or var(ys) == v: return None
    gr = 'A' if v > var(ys) else 'B'
    return auswahl(f'Datensatz A: {liste(xs)}. Datensatz B: {liste(ys)}. Welcher hat die größere Varianz?', f'Datensatz {gr}',
                   ['Datensatz A', 'Datensatz B', 'Beide gleich'],
                   f'Varianz A = {dz(v)}, Varianz B = {dz(var(ys))}. Größer ist {gr}.', 'Berechne beide Varianzen oder schätze, welche Werte weiter auseinanderliegen.')


def g_sigma(s):
    art = R.choice({1: ['aus_var', 'ganz'], 2: ['ganz', 'gerundet', 'aus_var_r'], 3: ['gerundet', 'einheit', 'rueck']}[s])
    if art == 'aus_var':
        q = R.randint(2, 15)
        return zahl(f'Die Varianz eines Datensatzes ist {q * q}. Wie groß ist die Standardabweichung σ?', f'σ = √{q * q} = {q}, denn {q} · {q} = {q * q}.',
                    'σ ist die Wurzel aus der Varianz.', q, f'{q}')
    if art == 'aus_var_r':
        v = R.choice([x for x in range(3, 60) if math.isqrt(x) ** 2 != x])
        w = gerundet(math.sqrt(v), 2)
        if w is None: return None
        return zahl(f'Die Varianz ist {v}. Berechne σ auf zwei Nachkommastellen.', f'σ = √{v} ≈ {dz(w)} (Taschenrechner, auf zwei Stellen gerundet).', 'Wurzel ziehen, dann runden.',
                    w, f'round({K(math.sqrt(v))}, 2)', tol=0.01)
    if art == 'ganz':
        n = R.choice([4, 5, 6, 8])
        xs = datensatz(n, 1, 20, quadrat=True)
        if not xs: return None
        m, v = mw(xs), var(xs)
        q = math.isqrt(int(v))
        return zahl(f'Berechne die Standardabweichung der Werte {liste(xs)}.', f'x̄ = {dz(m)}. Quadrate: {quad_weg(xs)} = {dz(v * n)}. Varianz {dz(v * n)} : {n} = {dz(v)}. σ = √{dz(v)} = {q}.',
                    'Erst die Varianz, dann die Wurzel.', q, f'{q}')
    if art in ('gerundet', 'einheit'):
        n = R.choice([4, 5])
        xs = datensatz(n, 1 if art == 'gerundet' else 140, 20 if art == 'gerundet' else 175, quadrat=False)
        if not xs: return None
        m, v = mw(xs), var(xs)
        w = gerundet(math.sqrt(v), 1 if art == 'einheit' else 2)
        if w is None: return None
        if art == 'einheit':
            return zahl(f'Körpergrößen in cm: {liste(xs)}. Berechne σ auf eine Nachkommastelle (in cm).',
                        f'x̄ = {dz(m)} cm. Quadrate: {quad_weg(xs)} = {dz(v * n)}. Varianz {dz(v)} cm². σ = √{dz(v)} ≈ {dz(w)} cm.',
                        'Die Varianz hat die Einheit cm² – erst die Wurzel gibt cm.', w, f'round({K(math.sqrt(v))}, 1)', einheit='cm', tol=0.1)
        return zahl(f'Berechne die Standardabweichung der Werte {liste(xs)} auf zwei Nachkommastellen.',
                    f'x̄ = {dz(m)}. Quadrate: {quad_weg(xs)} = {dz(v * n)}. Varianz: {dz(v)}. σ = √{dz(v)} ≈ {dz(w)}.',
                    'Mittelwert → Abweichungen → Quadrate → Mittelwert der Quadrate → Wurzel.', w, f'round({K(math.sqrt(v))}, 2)', tol=0.01)
    # rueck: σ gegeben, Varianz
    q = R.choice([Fr(3, 2), Fr(5, 2), 3, 4, Fr(12, 10), Fr(7, 2), 6])
    return zahl(f'Ein Datensatz hat die Standardabweichung σ = {dz(q)}. Wie groß ist die Varianz?', f'Varianz = σ² = {dz(q)}² = {dz(q * q)}.',
                'Die Umkehrung der Wurzel ist das Quadrieren.', q * q, f'{float(q)} ** 2')


def g_eigenschaften(s):
    sg = R.choice([2, 3, 4, 5, Fr(5, 2), Fr(3, 2), 6])
    m = R.randint(10, 60)
    art = R.choice({1: ['plus', 'gleich', 'plus'], 2: ['mal', 'plus', 'minus', 'mw_plus'], 3: ['beides', 'mal_neg', 'vergleich', 'beides']}[s])
    if art == 'plus':
        d = R.randint(2, 10)
        return zahl(f'Ein Datensatz hat x̄ = {m} und σ = {dz(sg)}. Zu jedem Wert wird {d} addiert. Wie groß ist die neue Standardabweichung?',
                    f'Alle Werte verschieben sich um {d}. Die Abstände bleiben: σ = {dz(sg)} (nur x̄ wird {m + d}).',
                    'Ändern sich die Abstände zwischen den Werten?', sg, f'{float(sg)}')
    if art == 'minus':
        d = R.randint(2, 9)
        return zahl(f'Bei einem Test war x̄ = {m} Punkte und σ = {dz(sg)} Punkte. Wegen einer fehlerhaften Aufgabe werden jedem {d} Punkte abgezogen. Wie groß ist das neue σ?',
                    f'Alle verlieren gleich viel; die Streuung bleibt σ = {dz(sg)}.', 'Verschieben ändert die Streuung nicht.', sg, f'{float(sg)}')
    if art == 'mw_plus':
        d = R.randint(2, 9)
        return zahl(f'x̄ = {m}, σ = {dz(sg)}. Zu jedem Wert wird {d} addiert. Wie groß ist der neue Mittelwert?', f'Der Mittelwert verschiebt sich mit: {m} + {d} = {m + d}. σ bleibt {dz(sg)}.',
                    'Der Mittelwert macht die Verschiebung mit.', m + d, f'{m} + {d}')
    if art == 'gleich':
        w = R.randint(3, 40)
        k = R.randint(4, 8)
        return zahl(f'Alle {k} Werte eines Datensatzes sind gleich {w}. Wie groß ist die Standardabweichung?', f'Jeder Wert ist gleich dem Mittelwert {w}. Alle Abweichungen sind 0, also σ = 0.',
                    'Wie weit ist jeder Wert vom Mittelwert entfernt?', 0, '0')
    if art == 'mal':
        k = R.choice([2, 3, 10, Fr(1, 2)])
        ein = R.choice([('m', 'cm', 100), ('kg', 'g', 1000)]) if k == 10 else None
        if ein:
            return zahl(f'Längen in m haben σ = {dz(sg)} m. Man rechnet alle Werte in cm um. Wie groß ist σ in cm?', f'Alle Werte werden mit 100 multipliziert, σ auch: {dz(sg)} · 100 = {dz(sg * 100)} cm.',
                        'Umrechnen heißt: jeden Wert mit derselben Zahl multiplizieren.', sg * 100, f'{float(sg)} * 100', einheit='cm')
        return zahl(f'Ein Datensatz hat σ = {dz(sg)}. Jeder Wert wird mit {dz(k)} multipliziert. Wie groß ist die neue Standardabweichung?',
                    f'Alle Abstände werden {dz(k)}-mal so groß: σ = {dz(k)} · {dz(sg)} = {dz(k * sg)}.', 'Beim Multiplizieren werden auch die Abstände multipliziert.', k * sg, f'{float(k)} * {float(sg)}')
    if art == 'mal_neg':
        k = R.choice([-2, -3])
        return zahl(f'Ein Datensatz hat σ = {dz(sg)}. Jeder Wert wird mit {kl(k)} multipliziert. Wie groß ist die neue Standardabweichung?',
                    f'Die Abstände werden {abs(k)}-mal so groß; die Richtung spielt keine Rolle: σ = {abs(k)} · {dz(sg)} = {dz(abs(k) * sg)}.',
                    'σ ist ein Abstand – kann er negativ werden?', abs(k) * sg, f'abs({k}) * {float(sg)}')
    if art == 'beides':
        k, d = R.choice([2, 3]), R.randint(2, 9)
        return zahl(f'Ein Datensatz hat σ = {dz(sg)}. Jeder Wert wird zuerst mit {k} multipliziert, danach wird {d} addiert. Wie groß ist die neue Standardabweichung?',
                    f'Mal {k}: σ wird {dz(k * sg)}. Plus {d}: keine Änderung. Neues σ = {dz(k * sg)}.', 'Nur das Multiplizieren ändert die Streuung.', k * sg, f'{k} * {float(sg)}')
    d = R.randint(5, 20)
    base = sorted(R.sample(range(1, 30), 5))
    r = 'Beide haben dieselbe Standardabweichung.'
    return auswahl(f'Datensatz A: {liste(base)}. Datensatz B: {liste([x + d for x in base])}. Welche Aussage stimmt?', r,
                   ['B hat die größere Standardabweichung.', 'A hat die größere Standardabweichung.', f'σ von B ist um {d} größer.'],
                   f'B entsteht aus A, indem man zu jedem Wert {d} addiert. Die Abstände bleiben gleich, also auch σ.',
                   'Vergleiche die Abstände der Werte untereinander.')


def g_deuten(s):
    art = R.choice({1: ['bereich_unten', 'bereich_oben', 'enger'], 2: ['enger', 'bereich_unten', 'zaehlen', 'aussage'], 3: ['zaehlen', 'aussage', 'sach', 'einordnen']}[s])
    if art in ('bereich_unten', 'bereich_oben'):
        m = R.randint(20, 80)
        sg = R.randint(2, 12)
        if art == 'bereich_unten':
            return zahl(f'Ein Datensatz hat x̄ = {m} und σ = {sg}. Wo beginnt der Bereich x̄ − σ bis x̄ + σ?', f'x̄ − σ = {m} − {sg} = {m - sg}.',
                        'Ziehe σ vom Mittelwert ab.', m - sg, f'{m} - {sg}')
        return zahl(f'Ein Datensatz hat x̄ = {m} und σ = {sg}. Wo endet der Bereich x̄ − σ bis x̄ + σ?', f'x̄ + σ = {m} + {sg} = {m + sg}.',
                    'Addiere σ zum Mittelwert.', m + sg, f'{m} + {sg}')
    if art == 'enger':
        kontext = R.choice([('Fahrzeit zweier Buslinien zur Schule (in min)', 'Linie', (15, 35)), ('Gewicht der Brötchen zweier Bäckereien (in g)', 'Bäckerei', (50, 70)),
                            ('Ergebnisse zweier Klassen im Test (Punkte)', 'Klasse', (20, 40))])
        m = R.randint(*kontext[2])
        s1, s2 = R.sample(range(1, 9), 2)
        gl = 'A' if s1 < s2 else 'B'
        return auswahl(f'{kontext[0]}: {kontext[1]} A hat x̄ = {m}, σ = {s1}; {kontext[1]} B hat x̄ = {m}, σ = {s2}. Bei welcher sind die Werte gleichmäßiger?',
                       f'{kontext[1]} {gl}', [f'{kontext[1]} A', f'{kontext[1]} B', 'Kann man nicht sagen, der Mittelwert ist gleich'],
                       f'Gleicher Mittelwert; das kleinere σ ({min(s1, s2)}) bedeutet: Die Werte liegen enger beieinander.', 'Kleineres σ heißt weniger Streuung.')
    if art == 'zaehlen':
        n = R.choice([6, 8, 10])
        xs = datensatz(n, 2, 20, quadrat=True)
        if not xs: return None
        m, q = mw(xs), math.isqrt(int(var(xs)))
        k = sum(1 for x in xs if m - q <= x <= m + q)
        return zahl(f'Werte: {liste(sorted(xs))}. Es gilt x̄ = {dz(m)} und σ = {q}. Wie viele Werte liegen im Bereich x̄ − σ bis x̄ + σ (Grenzen eingeschlossen)?',
                    f'Bereich {dz(m - q)} bis {dz(m + q)}. Darin liegen {k} der {n} Werte.', 'Berechne zuerst die Grenzen und zähle dann.', k, f'{k}')
    if art == 'aussage':
        m1, m2 = R.randint(50, 70), R.randint(50, 70)
        s1, s2 = R.randint(2, 6), R.randint(8, 15)
        r = 'In Gruppe 2 sind die Ergebnisse unterschiedlicher als in Gruppe 1.'
        return auswahl(f'Gruppe 1: x̄ = {m1}, σ = {s1}. Gruppe 2: x̄ = {m2}, σ = {s2}. Welche Aussage folgt sicher?', r,
                       ['Gruppe 2 ist besser, weil ihr σ größer ist.', 'In Gruppe 1 haben alle genau dasselbe Ergebnis.', 'Gruppe 2 hat mehr Teilnehmer.'],
                       'σ misst nur die Streuung, nicht die Leistung oder die Gruppengröße. Größeres σ = unterschiedlichere Ergebnisse.',
                       'Was misst σ – und was nicht?')
    if art == 'sach':
        soll = R.choice([500, 750, 1000])
        s1, s2 = R.randint(2, 6), R.randint(8, 20)
        r = f'Maschine A – bei gleichem Mittelwert schwankt die Füllmenge weniger.'
        return auswahl(f'Zwei Maschinen füllen {soll}-ml-Flaschen. Beide füllen im Mittel {soll} ml ein. Maschine A: σ = {s1} ml, Maschine B: σ = {s2} ml. Welche ist zuverlässiger?', r,
                       [f'Maschine B – sie füllt öfter mehr als {soll} ml ein.', 'Beide gleich – der Mittelwert ist gleich.', 'Maschine B – größeres σ heißt genauer.'],
                       f'Gleicher Mittelwert. Bei A liegen typische Füllmengen zwischen {soll - s1} und {soll + s1} ml, bei B zwischen {soll - s2} und {soll + s2} ml.',
                       'Zuverlässig heißt: möglichst wenig Abweichung vom Sollwert.')
    # einordnen: liegt Wert innerhalb x̄ ± σ?
    m = R.randint(30, 70)
    sg = R.randint(3, 10)
    x = m + R.choice([-1, 1]) * R.randint(1, 2 * sg)
    if abs(x - m) == sg: return None
    innen = abs(x - m) < sg
    return ja_nein(f'Bei einer Messreihe ist x̄ = {m} und σ = {sg}. Liegt der Wert {x} im Bereich x̄ − σ bis x̄ + σ?', innen,
                   f'Bereich: {m - sg} bis {m + sg}. {x} liegt {"darin" if innen else "außerhalb"}.', 'Berechne beide Grenzen.')


GEN = {'abweichung': g_abweichung, 'varianz': g_varianz, 'sigma': g_sigma, 'eigenschaften': g_eigenschaften, 'deuten': g_deuten}

bauen('daten.standardabweichung',
      'Die Streuung von Daten mit Varianz und Standardabweichung berechnen, ihre Eigenschaften kennen und sie in Sachzusammenhängen deuten.',
      ['Abweichung = Wert − Mittelwert; die Summe aller Abweichungen ist 0.',
       'Varianz (variance) = Mittelwert der quadrierten Abweichungen (durch n teilen).',
       'Standardabweichung (standard deviation) σ = √Varianz – gleiche Einheit wie die Daten.',
       'Verschieben ändert σ nicht; mal k ergibt σ · |k|.',
       'Kleines σ: Werte eng beieinander. Großes σ: Werte streuen stark.'],
      [('Streuung messen', ['abweichung', 'varianz', 'sigma']), ('Verstehen und deuten', ['eigenschaften', 'deuten'])],
      ETAPPEN, GEN,
      offen=['σ wird als Standardabweichung der Gesamtheit berechnet (Teilen durch n), wie im IB MYP üblich. Die Stichproben-Form (durch n − 1) ist bewusst nicht enthalten.',
             'Im IB wird σ meist mit dem Taschenrechner (GDC) bestimmt. Hier rechnen die Kinder mit kleinen Datensätzen von Hand, um die Bedeutung zu verstehen.'])
