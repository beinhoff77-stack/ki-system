#!/usr/bin/env python3
"""Thema daten.standardabweichung – Standardabweichung (IB MYP 4, etwa Klasse 9)."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403
from _rsib2 import PLAN2, art3  # noqa: E402

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
    # Durchsicht 19: Stufe 2 = unter dem Mittelwert, größte Abweichung, Wert aus Abweichung; Stufe 3 = rückwärts, neuer Wert, Summe 0 nutzen
    art = R.choice({1: ['mittel', 'abw'], 2: ['abw_neg', 'betrag', 'rueck_wert']}[s]) if s < 3 else art3('fehlend', 'neu_dazu', 'abw_fehlt', ['fehlend', 'summe', 'neu_dazu', 'abw_fehlt'])
    if art in ('rueck_wert', 'neu_dazu', 'abw_fehlt'): return abweichung3(art)
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
    # Durchsicht 19: Stufe 3 = vergleichen, Fehler finden, zwei Werte rückwärts, Wirkung eines neuen Wertes (vorher: meist dieselbe Rechnung wie Stufe 2)
    art = R.choice({1: ['voll', 'quadrate'], 2: ['aus_abw', 'vergleich']}[s]) if s < 3 else art3('luecke_var', 'fehler', 'zwei_werte', ['luecke_var', 'fehler', 'zwei_werte', 'neuer_mw'])
    if art in ('zwei_werte', 'neuer_mw', 'luecke_var'): return varianz3(art)
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
    # Durchsicht 19: Varianz aus σ (bisher Stufe 3) ist eine Umkehrung -> Stufe 2; Stufe 3 = Sachdaten mit Einheit, Häufigkeitstabelle, gespiegelte Datensätze, Einheit der Varianz
    art = R.choice({1: ['aus_var', 'ganz'], 2: ['gerundet', 'aus_var_r', 'rueck']}[s]) if s < 3 else art3('einheit', 'haeufig', 'spiegel', ['einheit', 'haeufig', 'spiegel', 'einheit_var'])
    if art in ('haeufig', 'spiegel', 'einheit_var'): return sigma3(art)
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
    # Durchsicht 19: „mal k, dann plus d“ und „mal (−k)“ sind mehrere Schritte -> Stufe 2; Stufe 3 = Umrechnen in %, °C→°F, rückwärts, σ = 0 deuten
    art = R.choice({1: ['plus', 'gleich', 'mal'], 2: ['minus', 'mw_plus', 'beides', 'mal_neg', 'vergleich', 'mal']}[s]) if s < 3 else art3('umrechnung', 'temperatur', 'rueckwaerts', ['umrechnung', 'temperatur', 'rueckwaerts', 'null'])
    if art in ('umrechnung', 'temperatur', 'rueckwaerts', 'null'): return eigenschaften3(art)
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
    # Durchsicht 19: Zählen im Bereich und „liegt der Wert darin?“ -> Stufe 2; Stufe 3 = Mittelwert und σ zugleich deuten, Abstand in σ, Ausreißer: Median gegen σ
    art = R.choice({1: ['bereich_unten', 'bereich_oben', 'enger'], 2: ['zaehlen', 'aussage', 'einordnen']}[s]) if s < 3 else art3('zwei_merkmale', 'z_wert', 'ausreisser_sigma', ['zwei_merkmale', 'z_wert', 'ausreisser_sigma', 'sach'])
    if art in ('zwei_merkmale', 'z_wert', 'ausreisser_sigma'): return deuten3(art)
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


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-2) ----------
# Neue Arten für Stufe 2/3. Prüfungsvorbilder: IB MYP Extended (Fragenbanken/eAssessment-Stil): fehlender Wert und neuer Mittelwert,
# Streuung zweier Datensätze vergleichen, Fehler in einer Rechnung finden, Häufigkeitstabelle, Umrechnen (mal k plus d),
# „Wie viele Standardabweichungen über dem Mittelwert?“, zwei Verteilungen mit Mittelwert und σ vergleichen. Eigene Zahlen.
def abweichung3(art):
    if art == 'rueck_wert':
        m = R.randint(10, 60)
        a = R.choice([-1, 1]) * R.randint(2, 12)
        return zahl(f'Der Mittelwert eines Datensatzes ist {m}. Ein Wert hat die Abweichung {dz(a)}. Wie groß ist dieser Wert?',
                    f'Abweichung = Wert − Mittelwert, also Wert = Mittelwert + Abweichung = {m} + {kl(a)} = {m + a}.',
                    'Stelle „Abweichung = Wert − Mittelwert“ nach dem Wert um.', m + a, f'{m} + ({a})')
    if art == 'neu_dazu':
        n = R.choice([4, 5, 6, 9])
        m = R.randint(12, 40)
        x = R.randint(m - 15, m + 25)
        neu = Fr(n * m + x, n + 1)
        if x == m or not endlich(neu) or neu * 10 != int(neu * 10): return None
        return zahl(f'{n} Werte haben den Mittelwert {m}. Ein weiterer Wert {x} kommt dazu. Wie groß ist der neue Mittelwert?',
                    f'Alte Summe: {n} · {m} = {n * m}. Neue Summe: {n * m} + {x} = {n * m + x}. Neuer Mittelwert: {n * m + x} : {n + 1} = {dz(neu)}.',
                    'Rechne zuerst die Summe der alten Werte aus dem Mittelwert zurück.', neu, f'({n} * {m} + {x}) / {n + 1}')
    # abw_fehlt: Summe der Abweichungen ist 0
    n = R.choice([4, 5, 6])
    ab = [R.choice([-1, 1]) * R.randint(1, 9) for _ in range(n - 1)]
    f = -sum(ab)
    if f == 0 or abs(f) > 15: return None
    return zahl(f'Von {n} Werten kennt man {n - 1} Abweichungen vom Mittelwert: {"; ".join(dz(a) for a in ab)}. Wie groß ist die letzte Abweichung?',
                f'Alle Abweichungen zusammen ergeben 0. Bisher: {dz(sum(ab))}. Also fehlt {dz(f)}.',
                'Was ergeben alle Abweichungen zusammen?', f, f'-({" + ".join(f"({a})" for a in ab)})')


def varianz3(art):
    if art == 'zwei_werte':
        m, d = R.randint(5, 30), R.randint(2, 9)
        return luecken(f'Zwei Werte haben den Mittelwert {m} und die Varianz {d * d}. Wie heißen die beiden Werte? (kleinerer zuerst)', '□ und □', 'Zwei ganze Zahlen',
                       [m - d, m + d], f'Beide Werte liegen gleich weit vom Mittelwert weg, Abweichungen −a und a. Varianz (a² + a²) : 2 = a² = {d * d}, also a = {d}. Werte: {m - d} und {m + d}.',
                       'Bei zwei Werten sind die Abweichungen gleich groß, nur mit anderem Vorzeichen.', c=[f'{m} - {d}', f'{m} + {d}'])
    if art == 'luecke_var':
        n = R.choice([4, 5])
        xs = datensatz(n, 1, 20)
        if not xs: return None
        m, v = mw(xs), var(xs)
        if v.denominator != 1: return None
        k = R.randrange(n)
        bek = '; '.join('x' if i == k else str(x) for i, x in enumerate(xs))
        return luecken(f'Die Werte {bek} haben den Mittelwert {dz(m)}. Bestimme x und danach die Varianz der {n} Werte.', 'x = □; Varianz = □', 'Zwei ganze Zahlen',
                       [xs[k], int(v)], f'Summe: {n} · {dz(m)} = {dz(n * m)}, also x = {dz(n * m)} − {sum(xs) - xs[k]} = {xs[k]}. Varianz: ({quad_weg(xs)}) : {n} = {dz(v)}.',
                       'Mittelwert mal Anzahl ergibt die Summe – so findest du x. Dann wie gewohnt die Varianz.', c=[f'{n} * {m} - {sum(xs) - xs[k]}', f'{v}'])
    # neuer_mw: ein Wert gleich dem Mittelwert kommt dazu
    n = R.choice([3, 4])
    xs = datensatz(n, 1, 15)
    if not xs: return None
    m, v = mw(xs), var(xs)
    v2 = v * n / (n + 1)
    return auswahl(f'Werte: {liste(xs)} (x̄ = {dz(m)}, Varianz {dz(v)}). Ein neuer Wert {dz(m)} kommt dazu – genau der Mittelwert. Was passiert mit der Varianz?', 'Sie wird kleiner.',
                   ['Sie wird größer.', 'Sie bleibt gleich.', 'Sie wird 0.'],
                   f'Der Mittelwert bleibt {dz(m)}, die neue Abweichung ist 0. Die Summe der Quadrate bleibt {dz(v * n)}, wird aber durch {n + 1} statt {n} geteilt: {dz(v * n)} : {n + 1} ≈ {dz(round(float(v2), 2))}.',
                   'Welche Abweichung hat der neue Wert? Durch wie viele Werte teilst du danach?')


def sigma3(art):
    if art == 'haeufig':
        werte = sorted(R.sample(range(0, 6), R.choice([3, 4])))
        anz = [R.randint(1, 6) for _ in werte]
        xs = [w for w, a in zip(werte, anz) for _ in range(a)]
        n = len(xs)
        if n < 6 or n > 16: return None
        m, v = mw(xs), var(xs)
        w = gerundet(math.sqrt(v), 2)
        if w is None or not endlich(m): return None
        t = tabelle(['Tore'] + [str(x) for x in werte], [['Spiele'] + [str(a) for a in anz]])
        return mit_grafik(zahl(f'Die Tabelle zeigt, wie viele Tore eine Mannschaft in ihren {n} Spielen geschossen hat. Berechne die Standardabweichung der Torzahlen auf zwei Nachkommastellen.',
                               f'Mittelwert: ({" + ".join(f"{w_} · {a}" for w_, a in zip(werte, anz))}) : {n} = {dz(m)}. '
                               f'Varianz: ({" + ".join(f"{a} · {kl(w_ - m)}²" for w_, a in zip(werte, anz))}) : {n} ≈ {dz(round(float(v), 4))}. σ ≈ {dz(w)}.',
                               'Jeder Wert zählt so oft, wie er in der Tabelle vorkommt.', w, f'round({K(math.sqrt(v))}, 2)', tol=0.01), t)
    if art == 'spiegel':
        a, b = sorted(R.sample(range(2, 30), 2))
        n = R.choice([4, 5])
        A = [a] * (n - 1) + [b]
        B = [a] + [b] * (n - 1)
        q = math.sqrt(var(A))
        return auswahl(f'Datensatz A: {liste(A)}. Datensatz B: {liste(B)}. Welche Aussage stimmt?', 'Beide haben dieselbe Standardabweichung.',
                       ['A hat die größere Standardabweichung.', 'B hat die größere Standardabweichung.', 'Beide haben denselben Mittelwert.'],
                       f'B ist A „gespiegelt“: In A liegt ein Wert allein oben, in B einer allein unten. Die Abstände zum jeweiligen Mittelwert sind gleich groß, '
                       f'also gleiches σ ≈ {dz(round(q, 2))}. Die Mittelwerte ({dz(mw(A))} und {dz(mw(B))}) sind verschieden.',
                       'Vergleiche die Abstände der Werte zum eigenen Mittelwert – nicht die Werte selbst.')
    # einheit_var
    g, e = R.choice([('Zeiten', 's'), ('Längen', 'cm'), ('Massen', 'kg'), ('Längen', 'm')])
    q = R.randint(2, 9)
    return auswahl(f'{g} in {e} haben die Standardabweichung σ = {q} {e}. Welche Varianz gehört dazu?', f'{q * q} {e}²',
                   [f'{q * q} {e}', f'{q} {e}²', f'{2 * q} {e}'],
                   f'Varianz = σ² = {q}² = {q * q}. Die Einheit wird mitquadriert: {e}².', 'Die Varianz ist σ zum Quadrat – auch die Einheit.')


def eigenschaften3(art):
    if art == 'umrechnung':
        maxp, k = R.choice([(20, 5), (25, 4), (50, 2), (10, 10)])
        m = R.randint(maxp // 3, maxp - 3)
        sg = R.randint(2, 4)
        return luecken(f'Ein Test hat höchstens {maxp} Punkte. Ergebnis: x̄ = {m} Punkte, σ = {sg} Punkte. Die Lehrkraft rechnet alle Ergebnisse in Prozent um (mal {k}). '
                       'Wie groß sind danach Mittelwert und Standardabweichung?', 'x̄ = □ %; σ = □ %', 'Zwei ganze Zahlen',
                       [m * k, sg * k], f'Jeder Wert wird mit {k} multipliziert. Mittelwert: {m} · {k} = {m * k} %. Standardabweichung: {sg} · {k} = {sg * k} %.',
                       'Mal k wirkt auf den Mittelwert und auf σ.', c=[f'{m} * {k}', f'{sg} * {k}'])
    if art == 'temperatur':
        m, sg = R.randint(5, 25), R.choice([2, 3, 4, 5, Fr(5, 2)])
        return zahl(f'Tagestemperaturen eines Monats: x̄ = {m} °C, σ = {dz(sg)} °C. In Fahrenheit rechnet man F = 1,8 · C + 32. Wie groß ist σ in °F?',
                    f'Mal 1,8 vergrößert alle Abstände: {dz(sg)} · 1,8 = {dz(sg * Fr(9, 5))}. Plus 32 verschiebt nur. σ = {dz(sg * Fr(9, 5))} °F.',
                    'Welcher Teil der Umrechnung ändert die Abstände, welcher nur die Lage?', sg * Fr(9, 5), f'{float(sg)} * 1.8', einheit='°F')
    if art == 'rueckwaerts':
        if R.random() < .5:
            sg, k = R.choice([(Fr(5, 2), 4), (2, 3), (3, 5), (Fr(3, 2), 4), (4, Fr(5, 2))])
            return zahl(f'Alle Werte eines Datensatzes wurden mit derselben positiven Zahl multipliziert. Dadurch stieg σ von {dz(sg)} auf {dz(sg * k)}. Mit welcher Zahl wurde multipliziert?',
                        f'Mal k macht σ k-mal so groß: {dz(sg * k)} : {dz(sg)} = {dz(k)}.', 'Wie hängen altes σ, neues σ und der Faktor zusammen?', k, f'{float(sg * k)} / {float(sg)}')
        m, d, sg = R.randint(15, 40), R.randint(3, 9), R.randint(2, 5)
        f = Fr(m + d, m)
        return auswahl(f'Nach einer Änderung aller Werte stieg x̄ von {m} auf {m + d}, σ blieb {sg}. Was wurde gemacht?', f'Zu jedem Wert wurde {d} addiert.',
                       [f'Jeder Wert wurde mit {dz(round(float(f), 2))} multipliziert.', f'Zu jedem Wert wurde {sg} addiert.', f'Jeder Wert wurde mit {d} multipliziert.'],
                       f'σ blieb gleich, also wurde nur verschoben: {m} + {d} = {m + d}. Beim Multiplizieren hätte sich σ mit verändert.',
                       'Welche Änderung lässt σ gleich?')
    # null
    return auswahl('Ein Datensatz hat die Standardabweichung σ = 0. Welche Aussage stimmt sicher?', 'Alle Werte sind gleich.',
                   ['Alle Werte sind 0.', 'Der Mittelwert ist 0.', 'Es gibt nur einen einzigen Wert.'],
                   'σ = 0 heißt: Kein Wert weicht vom Mittelwert ab. Also sind alle Werte gleich dem Mittelwert – welcher Zahl, ist offen.',
                   'Was bedeutet es, wenn alle Abweichungen 0 sind?')


def deuten3(art):
    if art == 'zwei_merkmale':
        m1, m2 = R.sample(range(10, 20), 2)
        s1, s2 = R.sample(range(1, 7), 2)
        mehr = 'A' if m1 > m2 else 'B'
        gl = 'A' if s1 < s2 else 'B'
        opt = {(x, y): f'{x} hat im Schnitt mehr Punkte, die Ergebnisse in {y} sind gleichmäßiger.' for x in 'AB' for y in 'AB'}
        r = opt.pop((mehr, gl))
        return auswahl(f'Test mit 20 Punkten. Klasse A: x̄ = {m1}, σ = {s1}. Klasse B: x̄ = {m2}, σ = {s2}. Welche Aussage stimmt?', r, list(opt.values()),
                       f'Der Mittelwert vergleicht die Leistung: {max(m1, m2)} > {min(m1, m2)}, also {mehr}. σ vergleicht die Streuung: kleineres σ ({min(s1, s2)}) bei {gl}.',
                       'Prüfe zwei Dinge getrennt: Wer hat den größeren Mittelwert? Wer hat das kleinere σ?')
    if art == 'z_wert':
        m, sg = R.randint(20, 70), R.choice([2, 4, 5, 6, 8, 10])
        k = R.choice([Fr(1, 2), 1, Fr(3, 2), 2, Fr(5, 2), 3])
        oben = R.random() < .6
        x = m + (1 if oben else -1) * k * sg
        if x != int(x): return None
        return zahl(f'Ein Datensatz hat x̄ = {m} und σ = {sg}. Wie viele Standardabweichungen liegt der Wert {int(x)} {"über" if oben else "unter"} dem Mittelwert?',
                    f'Abstand: {abs(int(x) - m)}. In Standardabweichungen: {abs(int(x) - m)} : {sg} = {dz(k)}.',
                    'Berechne den Abstand zum Mittelwert und teile durch σ.', k, f'abs({int(x)} - {m}) / {sg}')
    if art == 'ausreisser_sigma':
        a = R.randint(5, 20)
        xs = [a, a + 1, a + 2, a + 3, a + 4]
        big = a + 4 + R.choice([30, 40, 50])
        ys = xs[:4] + [big]
        r = 'σ wird viel größer, der Median bleibt gleich.'
        return auswahl(f'Datensatz: {liste(xs)}. Der größte Wert {a + 4} wird durch {big} ersetzt. Welche Aussage stimmt?', r,
                       ['Median und σ ändern sich kaum.', 'Der Median wird viel größer, σ bleibt gleich.', 'Median und σ werden beide viel größer.'],
                       f'Der Median ist der mittlere Wert: vorher und nachher {a + 2}. σ hängt von allen Abständen ab: vorher ≈ {dz(round(math.sqrt(var(xs)), 2))}, nachher ≈ {dz(round(math.sqrt(var(ys)), 2))}.',
                       'Welcher Kennwert hängt nur vom mittleren Wert ab, welcher von allen Abständen?')
    return None


GEN = {'abweichung': g_abweichung, 'varianz': g_varianz, 'sigma': g_sigma, 'eigenschaften': g_eigenschaften, 'deuten': g_deuten}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import tab  # noqa: E402


def _zs(a, b, n, **kw):
    return {'typ': 'zahlenstrahl', 'start': a, 'ende': b, 'abschnitte': n, 'beschriftet': 'anfang_ende', **kw}


def _pk(*w):
    return [{'wert': x, 'name': n} for x, n in w]


def _var(ab, q):
    return tab(['Wert', '2', '4', '6', '8'], ['Abweichung', *ab], ['Quadrat', *q])


UMBAU = {
    'abweichung': {
        'einstieg': 'Drei Kinder springen 4 m, 7 m und 10 m weit. Im Schnitt sind das 7 m. '
                    'Wie weit liegt jeder Sprung daneben? Das ist die ⟦Abweichung⟧ vom Mittelwert.',
        'woerter': [['Mittelwert', 'x̄: Summe aller Werte geteilt durch ihre Anzahl'],
                    ['Abweichung', 'Wert minus Mittelwert']],
        'bild': _zs(0, 12, 12, punkte=_pk((4, '4'), (7, '7'), (10, '10'))),
        'schritte': [
            {'text': 'Mittelwert: (4 + 7 + 10) : 3 = 7.', 'bild': {'punkte': _pk((4, '4'), (7, 'x̄ = 7'), (10, '10'))}},
            {'text': 'Abweichung von 4: 4 − 7 = −3.', 'bild': {'boegen': [{'von': 7, 'bis': 4, 'name': '−3'}]}},
            {'text': 'Von 7: 0. Von 10: 10 − 7 = ⟦3⟧.',
             'bild': {'boegen': [{'von': 7, 'bis': 4, 'name': '−3'}, {'von': 7, 'bis': 10, 'name': '+3'}]}},
            {'text': 'Zusammen: (−3) + 0 + 3 = 0.'},
        ],
        'fehler': 'Abweichungen einfach addieren misst keine Streuung. Es kommt immer 0 heraus: ⟦Plus und Minus heben sich auf⟧.',
        'regel': 'Abweichung = ⟦Wert − Mittelwert⟧. Alle Abweichungen zusammen ergeben immer 0.',
    },
    'varianz': {
        'einstieg': 'Damit sich Plus und Minus nicht aufheben, quadriert man jede Abweichung. Dann sind alle Beiträge positiv. '
                    'Ihr Mittelwert heißt ⟦Varianz⟧.',
        'woerter': [['Varianz', 'Mittelwert der quadrierten Abweichungen'],
                    ['quadriert', 'mit sich selbst malgenommen: (−3)² = 9']],
        'bild': _var(['?'] * 4, ['?'] * 4),
        'schritte': [
            {'text': 'Werte 2; 4; 6; 8. Mittelwert: 20 : 4 = 5.'},
            {'text': 'Abweichungen: −3; −1; 1; 3.', 'bild': _var(['−3', '−1', '1', '3'], ['?'] * 4)},
            {'text': 'Quadrieren: 9; 1; 1; 9.', 'bild': _var(['−3', '−1', '1', '3'], ['9', '1', '1', '9'])},
            {'text': 'Varianz: (9 + 1 + 1 + 9) : 4 = ⟦5⟧.'},
        ],
        'fehler': '(−3)² = −9 ist falsch. Minus mal Minus ergibt Plus: ⟦(−3)² = 9⟧.',
        'fehler_bild': _var(['−3', '−1', '1', '3'], ['−9 ✗', '−1 ✗', '1', '9']),
        'regel': 'Varianz: Abweichungen ⟦quadrieren⟧, addieren, durch n teilen. Sie ist nie negativ.',
    },
    'sigma': {
        'einstieg': 'Fünf Bohnenpflanzen sind 3, 5, 7, 9 und 11 cm hoch. Die Varianz hat die Einheit cm², das passt nicht. '
                    'Die Wurzel daraus ist die ⟦Standardabweichung⟧.',
        'woerter': [['Standardabweichung σ', 'Wurzel aus der Varianz; der typische Abstand zum Mittelwert'],
                    ['σ', 'griechischer Buchstabe „sigma“']],
        'bild': _zs(0, 14, 14, punkte=_pk((3, '3'), (5, '5'), (7, '7'), (9, '9'), (11, '11'))),
        'schritte': [
            {'text': 'Mittelwert: 35 : 5 = 7.', 'bild': {'punkte': _pk((3, '3'), (5, '5'), (7, 'x̄'), (9, '9'), (11, '11'))}},
            {'text': 'Quadrierte Abweichungen: 16; 4; 0; 4; 16.'},
            {'text': 'Varianz: 40 : 5 = 8.'},
            {'text': 'Standardabweichung σ = √8 ≈ ⟦2,83 cm⟧.', 'bild': {'bereich': {'von': 4.17, 'bis': 9.83}}},
        ],
        'fehler': 'Die Varianz 8 ist nicht σ. Sie hat die Einheit cm². Erst die ⟦Wurzel⟧ ergibt σ in cm.',
        'regel': 'σ ist die ⟦Wurzel aus der Varianz⟧. Sie hat dieselbe Einheit wie die Daten.',
    },
    'eigenschaften': {
        'einstieg': 'Nach einer Klassenarbeit bekommt jedes Kind 3 Bonuspunkte. Alle rücken gleich weit nach oben. '
                    'Ändert sich dadurch die ⟦Streuung⟧?',
        'woerter': [['Streuung', 'wie weit die Werte auseinanderliegen']],
        'bild': _zs(0, 20, 20, punkte=_pk((8, '8'), (16, '16'))),
        'schritte': [
            {'text': 'Punkte 8; 8; 16; 16: Mittelwert 12, σ = 4.', 'bild': {'bereich': {'von': 8, 'bis': 16}}},
            {'text': 'Mit 3 Bonuspunkten: 11; 11; 19; 19.',
             'bild': {'punkte': _pk((8, ''), (16, ''), (11, '11'), (19, '19')), 'bereich': None, 'boegen': [{'von': 8, 'bis': 11, 'name': '+3'}, {'von': 16, 'bis': 19, 'name': '+3'}]}},
            {'text': 'Alle Abstände zum neuen Mittelwert 15 bleiben 4: ⟦σ = 4⟧.',
             'bild': {'boegen': None, 'punkte': _pk((11, '11'), (19, '19')), 'bereich': {'von': 11, 'bis': 19}}},
            {'text': 'Verdoppelt man dagegen 8; 8; 16; 16, verdoppeln sich die Abstände: ⟦σ = 8⟧.',
             'bild': _zs(0, 40, 20, punkte=_pk((16, '16'), (32, '32')), bereich={'von': 16, 'bis': 32})},
        ],
        'fehler': 'σ = 4 + 3 = 7 ist falsch. Die Werte ⟦verschieben sich gemeinsam⟧, ihre Abstände bleiben gleich.',
        'regel': 'Plus eine Zahl: ⟦σ bleibt gleich⟧. Mal k: σ wird mal |k|. Alle Werte gleich: σ = 0.',
    },
    'deuten': {
        'einstieg': 'Zwei Klassen schreiben denselben Test, beide haben im Schnitt 12 Punkte. In A liegen alle nah beieinander, '
                    'in B gibt es sehr gute und sehr schwache. σ zeigt den ⟦Unterschied⟧.',
        'woerter': [['Bereich um x̄', 'von x̄ − σ bis x̄ + σ; dort liegen viele Werte']],
        'bild': _zs(0, 24, 24, punkte=_pk((12, 'x̄ = 12'))),
        'schritte': [
            {'text': 'Klasse A: x̄ = 12, σ = 2.'},
            {'text': 'Bereich um x̄: von 12 − 2 = 10 bis ⟦14⟧.', 'bild': {'bereich': {'von': 10, 'bis': 14}}},
            {'text': 'Klasse B: σ = 5, also etwa 7 bis 17.', 'bild': {'bereich': {'von': 7, 'bis': 17}}},
            {'text': 'In A liegen die Ergebnisse ⟦enger beieinander⟧.', 'bild': {'bereich': {'von': 10, 'bis': 14}}},
        ],
        'fehler': '„B ist besser, weil σ größer ist“ ist falsch. σ sagt nicht, ⟦wer besser⟧ ist, nur wie verschieden die Ergebnisse sind.',
        'regel': '⟦Kleines σ⟧: Die Werte liegen eng beieinander. Großes σ: Die Werte streuen stark.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


d = bauen('daten.standardabweichung',
      'Die Streuung von Daten mit Varianz und Standardabweichung berechnen, ihre Eigenschaften kennen und sie in Sachzusammenhängen deuten.',
      ['Abweichung = Wert − Mittelwert; die Summe aller Abweichungen ist 0.',
       'Varianz (variance) = Mittelwert der quadrierten Abweichungen (durch n teilen).',
       'Standardabweichung (standard deviation) σ = √Varianz – gleiche Einheit wie die Daten.',
       'Verschieben ändert σ nicht; mal k ergibt σ · |k|.',
       'Kleines σ: Werte eng beieinander. Großes σ: Werte streuen stark.'],
      [('Streuung messen', ['abweichung', 'varianz', 'sigma']), ('Verstehen und deuten', ['eigenschaften', 'deuten'])],
      ETAPPEN, GEN,
      offen=['σ wird als Standardabweichung der Gesamtheit berechnet (Teilen durch n), wie im IB MYP üblich. Die Stichproben-Form (durch n − 1) ist bewusst nicht enthalten.',
             'Im IB wird σ meist mit dem Taschenrechner (GDC) bestimmt. Hier rechnen die Kinder mit kleinen Datensätzen von Hand, um die Bedeutung zu verstehen.'], plan=PLAN2)
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)


# ---- STUFEN (Zwanzigste Runde, Zusatz Realschule/IB, Zweig stufen-rsib-2) ----
import math  # noqa: E402
from _stufen_rsib2 import Stufen, stufen  # noqa: E402

ST = Stufen('daten.standardabweichung', 20_2_2)
Z, A, L = ST.Z, ST.A, ST.L
ST.vorbild += ['IB MYP eAssessment Mathematics (Extended): Streumaße berechnen und Datensätze vergleichen (mehrteilige Datenaufgabe)']

# abweichung
ST.stufenleiter('abweichung', 'Mittelwert berechnen, Abweichung eines Werts (Wert − Mittelwert) ausrechnen.',
                'Wert aus Abweichung, stärkste Abweichung finden, Abweichungen in Sachsituationen.',
                'Fehlenden Wert aus dem Mittelwert, letzte Abweichung über „Summe = 0“, Fehler beim Vorzeichen, Messfehler-Überlegung.')
ST.typ('abweichung', '/^/', 'direkt', s=1)
ST.typ('abweichung', '/Berechne die Abweichung des Wertes/', 'direkt')
ST.typ('abweichung', '/Wie groß ist dieser Wert/', 'umkehr')
ST.typ('abweichung', '/^/', 'mehrschritt', s=2)
ST.typ('abweichung', '/Wie groß ist der fehlende Wert/', 'rueckwaerts')
ST.typ('abweichung', '/Wie groß ist der neue Mittelwert/', 'mehrschritt')
ST.typ('abweichung', '/Wie groß ist die letzte Abweichung/', 'verknuepfen')
ST.typ('abweichung', '/^/', 'begruenden', s=3)
ST.neu('abweichung', 'erkennen', Z('Die Werte 4; 7; 10 haben den Mittelwert 7. Welcher Wert hat die Abweichung 0?', 7, '7',
       'Abweichung 0 heißt: Der Wert ist genau der Mittelwert. 7 − 7 = 0.', 'Wann ist Wert − Mittelwert gleich 0?'))
ST.neu('abweichung', 'einkleidung', Z('Ein Bäcker wiegt vier Brote: 495 g, 510 g, 502 g und 493 g; der Mittelwert ist 500 g. Um wie viel Gramm liegt das schwerste Brot über dem Mittelwert?', 10, '510 - 500',
       'Das schwerste wiegt 510 g: 510 − 500 = 10 g.', 'Welches Brot ist das schwerste?', einheit='g'))
ST.neu('abweichung', 'einkleidung', Z('Die Temperaturen einer Woche haben den Mittelwert 18 °C. Am Montag waren es 13 °C. Wie groß ist die Abweichung des Montags vom Mittelwert?', -5, '13 - 18',
       'Abweichung = Wert − Mittelwert = 13 − 18 = −5 °C. Negativ: Der Montag lag darunter.', 'Wert minus Mittelwert.', einheit='°C'))
ST.neu('abweichung', 'fehler', A('Jemand berechnet für 3; 5; 10 (Mittelwert 6) die Abweichungen 3; 1; 4. Was stimmt?', 'Falsch: Die Vorzeichen fehlen, richtig sind −3; −1; 4.',
       ['Richtig.', 'Falsch: Richtig sind 3; 5; 10.', 'Falsch: Richtig sind −3; 1; −4.'],
       'Abweichung = Wert − Mittelwert: 3 − 6 = −3, 5 − 6 = −1, 10 − 6 = 4. Probe: Die Summe muss 0 sein.', 'Prüfe mit der Summe der Abweichungen.'))
ST.neu('abweichung', 'transfer', A('Eine Waage zeigt bei jedem Wiegen 3 g zu viel an. Was gilt für die Abweichungen der Messwerte vom Mittelwert?', 'Sie bleiben gleich.',
       ['Jede wird um 3 g größer.', 'Jede wird um 3 g kleiner.', 'Sie werden alle 0.'],
       'Jeder Wert ist um 3 g zu groß, also auch der Mittelwert. Wert − Mittelwert ändert sich dadurch nicht.', 'Was passiert mit dem Mittelwert?'))
ST.knobel('abweichung', Z('Drei Zahlen haben den Mittelwert 10. Zwei von ihnen weichen um 4 und um −7 vom Mittelwert ab. Wie heißt die dritte Zahl?', 13, '10 + (0 - 4 + 7)',
          'Die Abweichungen ergeben zusammen 0: 4 + (−7) + d = 0 ⇒ d = 3. Die dritte Zahl ist 10 + 3 = 13. Probe: 14, 3, 13 haben die Summe 30.',
          'Was weißt du über die Summe aller Abweichungen?'))
ST.knobel('abweichung', A('Bei fünf Zahlen ist die Summe der Abweichungsbeträge |Wert − Mittelwert| gleich 0. Was folgt daraus?', 'Alle fünf Zahlen sind gleich.',
          ['Die Zahlen sind 1, 2, 3, 4, 5.', 'Der Mittelwert ist 0.', 'Das ist unmöglich.'],
          'Beträge sind nie negativ. Ihre Summe ist nur 0, wenn jeder Betrag 0 ist – jede Zahl ist also gleich dem Mittelwert.',
          'Kann eine Summe von nicht-negativen Zahlen 0 sein, wenn eine davon positiv ist?'))

# varianz
ST.stufenleiter('varianz', 'Varianz nach dem Schema (Mittelwert, Abweichungen, quadrieren, mitteln) berechnen.',
                'Varianz aus gegebenen Abweichungen, zwei Datensätze vergleichen, Varianz in einer Sachsituation.',
                'Fehlenden Wert bestimmen und dann die Varianz, Werte aus Mittelwert und Varianz, Fehler (−12)² = −144, Wirkung eines Werts genau am Mittelwert.')
ST.typ('varianz', '/^/', 'direkt', s=1)
ST.typ('varianz', '/Welcher hat die größere Varianz/', 'mehrschritt')
ST.typ('varianz', '/^/', 'umkehr', s=2)
ST.typ('varianz', '/Bestimme x und danach/', 'verknuepfen')
ST.typ('varianz', '/Mia rechnet/', 'fehler')
ST.typ('varianz', '/Zwei Werte haben/', 'rueckwaerts')
ST.typ('varianz', '/^/', 'begruenden', s=3)
ST.neu('varianz', 'erkennen', A('Welcher Schritt kommt bei der Varianz direkt nach dem Berechnen der Abweichungen?', 'Die Abweichungen quadrieren.',
       ['Die Abweichungen addieren.', 'Die Wurzel ziehen.', 'Durch die Anzahl teilen.'], 'Reihenfolge: Mittelwert, Abweichungen, quadrieren, Mittelwert der Quadrate.', 'Schau auf das Beispiel der Lernkarte.'))
ST.neu('varianz', 'einkleidung', Z('Ein Imker wiegt vier Honiggläser: 498 g, 502 g, 503 g und 497 g. Berechne die Varianz der Massen (in g²).', 6.5, '((498-500)**2 + (502-500)**2 + (503-500)**2 + (497-500)**2)/4',
       'Mittelwert 2 000 : 4 = 500 g. Abweichungen −2; 2; 3; −3. Quadrate 4; 4; 9; 9, Summe 26. Varianz 26 : 4 = 6,5 g².', 'Erst den Mittelwert.', einheit='g²'))
ST.knobel('varianz', Z('Die Werte 3; 5; 7; x (mit x > 7) haben die Varianz 5. Wie groß ist x?', 9, '9',
          'Probiere: x = 9 gibt den Mittelwert 24 : 4 = 6, Abweichungen −3; −1; 1; 3, Quadrate 9 + 1 + 1 + 9 = 20, Varianz 5. Je größer x, desto weiter liegt es vom Rest weg und desto größer wird die Varianz – es gibt nur diese Lösung.',
          'Wähle x so, dass die Werte symmetrisch um den Mittelwert liegen.'))
ST.knobel('varianz', A('Alle Werte eines Datensatzes liegen zwischen 10 und 20 (Grenzen eingeschlossen). Kann die Varianz größer als 25 sein?', 'Nein, höchstens 25.',
          ['Ja, wenn es sehr viele Werte sind.', 'Ja, bis 100.', 'Nein, höchstens 10.'],
          'Am meisten streuen die Werte, wenn die Hälfte bei 10 und die Hälfte bei 20 liegt: Mittelwert 15, jede Abweichung ±5, Varianz 25. Jeder Wert weiter innen verkleinert die Abweichungen.',
          'Wo müssen die Werte liegen, damit sie möglichst weit vom Mittelwert weg sind?'))

# sigma
s1 = round(math.sqrt(2), 2); s2 = round(math.sqrt(2.5), 2); s3 = round(math.sqrt(3), 2)
ST.stufenleiter('sigma', 'σ als Wurzel der Varianz berechnen; σ für kleine Datensätze.',
                'Varianz aus σ, σ in Sachsituationen (Runden, Füllmengen), Streuung zweier Angaben vergleichen.',
                'Häufigkeitstabelle, Datensätze vergleichen, Werte aus Mittelwert und σ, Fehler „nicht quadriert“, Parameter a, mehrteilige Aufgabe.')
ST.typ('sigma', '/^/', 'direkt', s=1)
ST.typ('sigma', 'Die Varianz ist', 'direkt')
ST.typ('sigma', '/^/', 'umkehr', s=2)
ST.typ('sigma', 'Körpergrößen in cm', 'einkleidung')
ST.typ('sigma', 'Massen in kg', 'umkehr')
ST.typ('sigma', 'Die Tabelle zeigt', 'verknuepfen')
ST.typ('sigma', '/^/', 'begruenden', s=3)
ST.neu('sigma', 'erkennen', A('Die Werte eines Datensatzes sind in cm gemessen. Welche Einheit hat die Standardabweichung σ?', 'cm', ['cm²', 'keine Einheit', '%'],
       'Die Varianz hat cm², die Wurzel daraus wieder cm. Darum ist σ leichter zu deuten als die Varianz.', 'Was macht die Wurzel aus cm²?'))
ST.neu('sigma', 'einkleidung', Z('Ein Läufer läuft fünf Runden in 60 s, 62 s, 58 s, 61 s und 59 s. Berechne σ auf zwei Nachkommastellen.', s1, f'round({math.sqrt(2)!r}, 2)',
       'Mittelwert 300 : 5 = 60 s. Abweichungen 0; 2; −2; 1; −1, Quadrate 0 + 4 + 4 + 1 + 1 = 10. Varianz 2, σ = √2 ≈ 1,41 s.', 'Erst Mittelwert, dann Varianz, dann Wurzel.', einheit='s', toleranz=0.01))
ST.neu('sigma', 'einkleidung', Z('Vier Saftflaschen enthalten 1 002 ml, 998 ml, 1 001 ml und 999 ml. Berechne σ auf zwei Nachkommastellen.', s2, f'round({math.sqrt(2.5)!r}, 2)',
       'Mittelwert 1 000 ml. Abweichungen 2; −2; 1; −1, Quadrate 4 + 4 + 1 + 1 = 10. Varianz 2,5, σ ≈ 1,58 ml.', 'Rechne mit den Abweichungen von 1 000.', einheit='ml', toleranz=0.01))
ST.neu('sigma', 'mehrschritt', A('Datensatz A hat σ = 3, Datensatz B hat die Varianz 10. Welcher streut stärker?', 'B, denn √10 ≈ 3,16 > 3', ['A, denn 3 ist eine Standardabweichung', 'beide gleich', 'B, denn 10 > 3'],
       'Vergleichbar sind nur gleiche Größen: σ von B ist √10 ≈ 3,16. Das ist etwas mehr als 3. „10 > 3“ vergleicht Äpfel mit Birnen.', 'Rechne beide in σ um.'))
ST.neu('sigma', 'rueckwaerts', L('Zwei Werte haben den Mittelwert 10 und die Standardabweichung 3. Wie heißen sie? (kleinerer zuerst)', '□ und □', [7, 13], ['10 - 3', '10 + 3'],
       'Bei zwei Werten liegen beide gleich weit vom Mittelwert: 10 − d und 10 + d. Varianz d² = 9, also σ = d = 3. Die Werte sind 7 und 13.', 'Wie liegen zwei Werte um ihren Mittelwert?'))
ST.neu('sigma', 'fehler', A('Jemand berechnet σ von 2; 4; 6; 8 so: Abweichungen −3; −1; 1; 3, Summe 0, also σ = 0. Was stimmt?', 'Falsch: Die Abweichungen müssen erst quadriert werden; σ = √5 ≈ 2,24.',
       ['Richtig.', 'Falsch: σ = 8.', 'Falsch: σ = 2.'],
       'Die Summe der Abweichungen ist immer 0. Darum quadriert man: 9 + 1 + 1 + 9 = 20, Varianz 5, σ = √5 ≈ 2,24.', 'Welcher Schritt fehlt?'))
ST.neu('sigma', 'parameter', Z('Für welches a > 0 haben die Werte 10 − a; 10; 10 + a die Varianz 6?', 3, '3',
       'Mittelwert 10. Quadrate a², 0, a², Varianz 2a² : 3 = 6 ⇒ a² = 9 ⇒ a = 3.', 'Stelle die Varianz mit a auf.'))
ST.neu('sigma', 'pruefung', L('Werte: 4; 8; 6; 10; 7. a) Mittelwert, b) Varianz, c) Standardabweichung.', 'a) □; b) □; c) □', [7, 4, 2], ['(4+8+6+10+7)/5', '(9+1+1+9+0)/5', '2'],
       'a) 35 : 5 = 7. b) Abweichungen −3; 1; −1; 3; 0, Quadrate 9 + 1 + 1 + 9 + 0 = 20, 20 : 5 = 4. c) σ = √4 = 2.', 'Arbeite die Teile nacheinander ab.'))
ST.knobel('sigma', Z('Ein Datensatz besteht nur aus den Werten 0 und 10, beide gleich oft. Wie groß ist σ?', 5, '5',
          'Mittelwert 5. Jeder Wert weicht um genau 5 ab, jedes Quadrat ist 25, die Varianz 25, σ = 5 – egal, wie viele Werte es sind.', 'Wie weit liegt jeder Wert vom Mittelwert weg?'))
ST.knobel('sigma', Z('Zu den Werten 4 und 6 soll ein dritter Wert so dazukommen, dass σ der drei Werte möglichst klein wird. Welcher Wert?', 5, '5',
          'Ein Wert genau am Mittelwert 5 trägt 0 zur Summe der Quadrate bei: σ² = (1 + 1 + 0) : 3. Jeder andere Wert verschiebt den Mittelwert und vergrößert die Quadrate.', 'Welcher Wert weicht am wenigsten ab?'))

# eigenschaften
ST.stufenleiter('eigenschaften', 'Wirkung von „+ Zahl“ (σ bleibt) und „· Zahl“ (σ mal Betrag) direkt anwenden; σ = 0 bei gleichen Werten.',
                'Zwei Schritte nacheinander, negativer Faktor, Mittelwert statt σ gesucht, Bonuspunkte.',
                'Umrechnungen (Prozent, Fahrenheit), die Änderung rückwärts erschließen, Fehler „− 5 macht σ kleiner“, negativer Faktor als Parameter.')
ST.typ('eigenschaften', 'Alle 5 Werte', 'erkennen')
ST.typ('eigenschaften', '/^/', 'direkt', s=1)
ST.typ('eigenschaften', 'Ein Datensatz hat σ = 5. Jeder Wert wird mit 2 multipliziert.', 'direkt')
ST.typ('eigenschaften', '/Wie groß ist der neue Mittelwert/', 'umkehr')
ST.typ('eigenschaften', '/^/', 'mehrschritt', s=2)
ST.typ('eigenschaften', 'Ein Test hat höchstens 20 Punkte', 'transfer')
ST.typ('eigenschaften', 'Tagestemperaturen', 'verknuepfen')
ST.typ('eigenschaften', '/Was wurde gemacht|Mit welcher Zahl wurde/', 'rueckwaerts')
ST.typ('eigenschaften', '/^/', 'begruenden', s=3)
ST.neu('eigenschaften', 'einkleidung', Z('Alle Kinder einer Klasse bekommen 2 Bonuspunkte. Vorher war σ = 3,5 Punkte. Wie groß ist σ danach?', 3.5, '3.5',
       'Jeder Wert und der Mittelwert steigen um 2; die Abstände bleiben gleich: σ = 3,5 Punkte.', 'Was passiert mit den Abständen zum Mittelwert?', einheit='Punkte'))
ST.neu('eigenschaften', 'fehler', A('Jemand sagt: „Zieht man von jedem Wert 5 ab, wird σ um 5 kleiner.“ Was stimmt?', 'Falsch: σ bleibt gleich, nur der Mittelwert sinkt um 5.',
       ['Richtig.', 'Falsch: σ wird um 25 kleiner.', 'Falsch: σ wird 0.'],
       'Die ganze Datenreihe rutscht um 5 nach unten, auch der Mittelwert. Die Abstände – und damit σ – bleiben.', 'Was passiert mit den Abständen?'))
ST.neu('eigenschaften', 'parameter', A('Jeder Wert eines Datensatzes wird mit derselben Zahl k multipliziert. Vorher war σ = 4, danach σ = 10. Welche Werte kann k haben?',
       'k = 2,5 oder k = −2,5', ['nur k = 2,5', 'k = 6 oder k = −6', 'nur k = 6'],
       'σ wird mit dem Betrag von k multipliziert: |k| · 4 = 10 ⇒ |k| = 2,5. Ein negatives k spiegelt die Werte, die Streuung bleibt gleich groß.', 'Was macht ein negativer Faktor mit den Abständen?'))
ST.knobel('eigenschaften', A('A: 1; 2; 3; 4; 5. B: 101; 102; 103; 104; 105. C: 10; 20; 30; 40; 50. Welche zwei Datensätze haben dieselbe Standardabweichung?', 'A und B',
          ['A und C', 'B und C', 'alle drei'],
          'B entsteht aus A durch + 100: σ bleibt. C entsteht aus A durch · 10: σ wird zehnmal so groß. Also haben A und B dasselbe σ (≈ 1,41).', 'Wie entsteht B aus A, wie C aus A?'))
ST.knobel('eigenschaften', L('Ein Datensatz hat x̄ = 20 und σ = 4. Aus jedem Wert x bildet man (x − 20) : 4. Welchen Mittelwert und welches σ haben die neuen Werte?', 'x̄ = □; σ = □', [0, 1], ['(20 - 20)/4', '4/4'],
          'Minus 20 verschiebt den Mittelwert auf 0, σ bleibt 4. Geteilt durch 4: Mittelwert 0, σ = 1. So vergleicht man Werte aus verschiedenen Tests („Standardisieren“).',
          'Zwei Schritte: erst verschieben, dann stauchen.'))

# deuten
ST.stufenleiter('deuten', 'Den Bereich x̄ − σ bis x̄ + σ angeben; kleineres σ = gleichmäßiger.',
                'Werte im Bereich zählen, Gruppen vergleichen, aus dem Bereich x̄ und σ zurückrechnen.',
                'Aussagen zu Klassen prüfen, Abstand in σ ausdrücken, σ aus einem Wert rückwärts, Wirkung eines Ausreißers, mehrteiliger Vergleich.')
ST.typ('deuten', 'Gewicht der Brötchen', 'erkennen')
ST.typ('deuten', '/^/', 'direkt', s=1)
ST.typ('deuten', '/^Gruppe 1/', 'einkleidung')
ST.typ('deuten', '/^/', 'mehrschritt', s=2)
ST.typ('deuten', '/Wie viele Standardabweichungen/', 'verknuepfen')
ST.typ('deuten', 'Zwei Maschinen', 'transfer')
ST.typ('deuten', '/^/', 'begruenden', s=3)
ST.neu('deuten', 'umkehr', L('Der Bereich x̄ − σ bis x̄ + σ geht von 40 bis 56. Wie groß sind x̄ und σ?', 'x̄ = □; σ = □', [48, 8], ['(40 + 56)/2', '(56 - 40)/2'],
       'x̄ liegt in der Mitte: (40 + 56) : 2 = 48. Der Bereich ist 2σ breit: 16 : 2 = 8.', 'Wo liegt der Mittelwert im Bereich?'))
ST.neu('deuten', 'rueckwaerts', Z('Der Wert 70 liegt genau 2 Standardabweichungen über dem Mittelwert 60. Wie groß ist σ?', 5, '(70 - 60)/2',
       'Abstand 70 − 60 = 10 sind 2σ, also σ = 5.', 'Welcher Abstand entspricht 2σ?'))
ST.neu('deuten', 'pruefung', A('Zwei Sprinter laufen je fünfmal 100 m (in s). A: 12,0; 12,2; 11,8; 12,1; 11,9. B: 11,6; 12,5; 11,9; 12,4; 11,6. Welche Aussage stimmt?',
       'Beide haben den Mittelwert 12,0 s; A ist konstanter.', ['B ist im Mittel schneller.', 'Beide sind gleich konstant.', 'A hat den kleineren Mittelwert.'],
       'Summen jeweils 60,0 s, also Mittelwert 12,0 s. A weicht höchstens 0,2 s ab, B bis zu 0,5 s: A hat das kleinere σ.', 'Berechne erst beide Mittelwerte, dann vergleiche die Abweichungen.'))
ST.knobel('deuten', A('Klasse 1: x̄ = 60 Punkte, σ = 10. Klasse 2: x̄ = 50 Punkte, σ = 5. Lea hat in Klasse 1 75 Punkte, Tim in Klasse 2 62 Punkte. Wer liegt im Vergleich zu seiner Klasse weiter vorn?',
          'Tim: 2,4 σ über dem Mittel, Lea nur 1,5 σ.', ['Lea, sie hat mehr Punkte.', 'Beide gleich.', 'Das kann man nicht vergleichen.'],
          'Lea: (75 − 60) : 10 = 1,5 Standardabweichungen. Tim: (62 − 50) : 5 = 2,4 Standardabweichungen. Gemessen an der eigenen Klasse ist Tim besser.',
          'Miss den Abstand zum Klassenmittel in „σ-Schritten“.'))
ST.knobel('deuten', Z('Drei Werte haben den Mittelwert 10 und σ = 0. Der Wert 14 kommt dazu. Wie groß ist σ der vier Werte? Runde auf zwei Nachkommastellen.', round(math.sqrt(3), 2), f'round({math.sqrt(3)!r}, 2)',
          'σ = 0 heißt: Alle drei Werte sind 10. Neu: 10; 10; 10; 14, Mittelwert 11. Abweichungen −1; −1; −1; 3, Quadrate 1 + 1 + 1 + 9 = 12, Varianz 3, σ = √3 ≈ 1,73.',
          'Was bedeutet σ = 0 für die drei Werte?', toleranz=0.01))

if __name__ == '__main__':
    stufen('daten.standardabweichung', ST)
