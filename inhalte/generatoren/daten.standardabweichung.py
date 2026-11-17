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
