#!/usr/bin/env python3
"""Thema daten.normalverteilung – Normalverteilung (ohne Lehrplan-Zuordnung, Niveau Klasse 9/10)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403
from _rsib2 import PLAN2, art3  # noqa: E402

start(8010)

# Anteile nach der 68-95-99,7-Regel (in Prozent), Bereiche in σ-Schritten ab μ
STREIFEN = {(-3, -2): Fr(235, 100), (-2, -1): Fr(135, 10), (-1, 0): 34, (0, 1): 34, (1, 2): Fr(135, 10), (2, 3): Fr(235, 100)}
AUSSEN = Fr(15, 100)  # jeweils jenseits von ±3σ


def anteil(a, b):
    """Anteil in % zwischen μ + aσ und μ + bσ (a, b ganze Zahlen, −4 = −∞, 4 = +∞)."""
    t = Fr(0)
    for (u, o), p in STREIFEN.items():
        if a <= u and o <= b: t += p
    if a <= -4: t += AUSSEN
    if b >= 4: t += AUSSEN
    return t


# Sachkontexte: (Größe, Einheit, μ-Auswahl, σ-Auswahl)
KONTEXT = [
    ('Körpergröße 15-jähriger Jungen', 'cm', [170, 172, 175], [6, 7, 8]),
    ('Gewicht neugeborener Babys', 'g', [3300, 3400, 3500], [400, 450, 500]),
    ('Füllmenge von Saftflaschen', 'ml', [500, 750, 1000], [4, 5, 8]),
    ('Ergebnis in einem Test', 'Punkte', [60, 65, 70], [8, 10, 12]),
    ('Lebensdauer von Glühbirnen', 'h', [1000, 1200, 1500], [50, 80, 100]),
    ('Fahrzeit zur Schule', 'min', [25, 30, 35], [3, 4, 5]),
]
ART = {'Gewicht neugeborener Babys': 'Das', 'Ergebnis in einem Test': 'Das'}


def der(g):
    return ART.get(g, 'Die')


def dativ(gen):
    """„unter 40 Punkte“ → „unter 40 Punkten“ in Frage, Lösungsweg und Antworten."""
    import re
    f = lambda t: re.sub(r'((?:unter|über|als|und|bis|zwischen|von)\s[\d\s,]+)\sPunkte\b', r'\1 Punkten', t)  # noqa: E731
    def w(g):
        def h(st):
            a = g(st)
            if a:
                a['f']['text'] = f(a['f']['text'])
                a['w'] = f(a['w'])
                if 'a' in a: a['a'] = [f(x) for x in a['a']]
            return a
        return h
    return {k: w(v) for k, v in gen.items()}

GLOCKE = [{'name': n, 'wert': w} for n, w in zip(['μ−3σ', '', 'μ−σ', 'μ', 'μ+σ', '', 'μ+3σ'], [2, 9, 23, 32, 23, 9, 2])]


def kxt():
    g, e, ms, ss = R.choice(KONTEXT)
    return g, e, R.choice(ms), R.choice(ss)


def grenzwort(k):
    return 'μ' if k == 0 else (f'μ + {k}σ' if k > 1 else 'μ + σ' if k == 1 else f'μ − {-k}σ' if k < -1 else 'μ − σ')


ETAPPEN = [
    {'lernziel': 'eigenschaften', 'titel': 'Die Glockenkurve',
     'regel': 'Viele Messgrößen (Körpergrößen, Füllmengen, Messfehler) sind ⟦normalverteilt⟧ (normal distribution): Die meisten Werte liegen nahe beim ⟦Mittelwert μ⟧, je weiter weg, desto seltener. Das Histogramm sieht aus wie eine ⟦Glocke⟧, ⟦symmetrisch⟧ um μ. Mittelwert, Median und Modus fallen zusammen. Die ⟦Standardabweichung σ⟧ bestimmt die Breite.',
     'schritte': ['Füllmengen: μ = 500 ml, σ = 5 ml.', 'Die Glocke hat ihre Spitze bei ⟦500 ml⟧; Füllmengen wie 495 ml und 505 ml sind ⟦gleich häufig⟧.'],
     'probe': 'Symmetrie: 500 − 5 = 495 und 500 + 5 = 505 ✓',
     'bild': {'typ': 'saeulen', 'einheit': 'Anteil in %', 'werte': GLOCKE, 'zahlen': False},
     'fehler': '„Bei größerem σ wird die Glocke höher“ ist falsch: Größeres σ heißt ⟦breiter und dafür flacher⟧ – die Gesamtfläche bleibt 100 %.'},
    {'lernziel': 'regel', 'titel': 'Die 68-95-99,7-Regel',
     'regel': 'Bei einer Normalverteilung liegen etwa ⟦68 %⟧ der Werte zwischen μ − σ und μ + σ, etwa ⟦95 %⟧ zwischen μ − 2σ und μ + 2σ und etwa ⟦99,7 %⟧ zwischen μ − 3σ und μ + 3σ (empirical rule).',
     'schritte': ['Körpergröße: μ = 170 cm, σ = 6 cm.', 'μ − 2σ = 158 cm, μ + 2σ = 182 cm.', 'Etwa ⟦95 %⟧ sind zwischen 158 cm und 182 cm groß.'],
     'probe': '2 · 6 = 12; 170 ± 12 ✓',
     'bild': {'typ': 'tabelle', 'kopf': ['Bereich', 'Anteil'], 'zeilen': [['μ ± σ', '≈ 68 %'], ['μ ± 2σ', '≈ 95 %'], ['μ ± 3σ', '≈ 99,7 %']]},
     'fehler': '„Zwischen μ − 2σ und μ + 2σ liegen 2 · 68 % = 136 %“ ist falsch: Mehr als 100 % geht nicht. Die Anteile wachsen ⟦nicht proportional⟧: 68 %, 95 %, 99,7 %.'},
    {'lernziel': 'anteile', 'titel': 'Anteile in Teilbereichen',
     'regel': 'Wegen der ⟦Symmetrie⟧ teilt man die Anteile in Hälften: Zwischen μ und μ + σ liegen ⟦34 %⟧, zwischen μ + σ und μ + 2σ ⟦13,5 %⟧, zwischen μ + 2σ und μ + 3σ ⟦2,35 %⟧, darüber 0,15 %. Über μ + σ liegen also ⟦16 %⟧, über μ + 2σ ⟦2,5 %⟧.',
     'schritte': ['Testergebnisse: μ = 60, σ = 10. Wie viel % haben mehr als 70 Punkte?', '70 = μ + σ. Darüber: (100 % − 68 %) : 2 = ⟦16 %⟧.'],
     'probe': '34 % + 34 % + 16 % + 16 % = 100 ✓',
     'bild': {'typ': 'saeulen', 'einheit': 'Anteil in %; Bereiche in σ-Schritten ab μ', 'werte': [{'name': 'unter −2', 'wert': 2.5}, {'name': '−2…−1', 'wert': 13.5}, {'name': '−1…0', 'wert': 34},
                                                           {'name': '0…1', 'wert': 34}, {'name': '1…2', 'wert': 13.5}, {'name': 'über 2', 'wert': 2.5}], 'zahlen': True},
     'fehler': '„Über μ + σ liegen 32 %“ ist falsch: Die 32 % außerhalb von μ ± σ verteilen sich auf ⟦beide Seiten⟧ – oben nur die Hälfte, 16 %.'},
    {'lernziel': 'zwert', 'titel': 'Der z-Wert',
     'regel': 'Der ⟦z-Wert⟧ (z-score) gibt an, ⟦wie viele Standardabweichungen⟧ ein Wert x vom Mittelwert entfernt ist: ⟦z = (x − μ) : σ⟧. Positiv: über dem Mittelwert, negativ: darunter. Umgekehrt: x = μ + z · σ.',
     'schritte': ['μ = 170 cm, σ = 6 cm, x = 182 cm.', 'z = (182 − 170) : 6 = 12 : 6 = ⟦2⟧.', 'Die Person ist 2 Standardabweichungen größer als der Durchschnitt.'],
     'probe': '170 + 2 · 6 = 182 ✓',
     'fehler': 'z = 182 : 6 ≈ 30,3 ist falsch: Zuerst den ⟦Abstand zum Mittelwert⟧ bilden (182 − 170), dann durch σ teilen.'},
    {'lernziel': 'vergleichen', 'titel': 'Vergleichen und beurteilen',
     'regel': 'Mit z-Werten kann man Ergebnisse aus ⟦verschiedenen Verteilungen⟧ vergleichen: Der größere z-Wert ist ⟦relativ besser⟧. Werte mit ⟦|z| > 2⟧ gelten als ⟦ungewöhnlich⟧ (nur etwa 5 % liegen so weit außen).',
     'schritte': ['Mathe: 78 Punkte bei μ = 70, σ = 4 → z = 2. Deutsch: 85 Punkte bei μ = 75, σ = 10 → z = 1.', 'Trotz weniger Punkten ist ⟦Mathe das bessere Ergebnis⟧ im Vergleich zur Gruppe.'],
     'probe': '(78 − 70) : 4 = 2 und (85 − 75) : 10 = 1 ✓',
     'fehler': 'Nur die Punktzahlen zu vergleichen (85 > 78) ist falsch, wenn die Tests ⟦verschieden verteilt⟧ sind. Erst in z-Werte umrechnen.'},
]


def g_eigenschaften(s):
    art = R.choice({1: ['spitze', 'symmetrie', 'median'], 2: ['breite', 'symmetrie_wert', 'histogramm'], 3: ['breite', 'histogramm', 'fehler', 'symmetrie_wert']}[s])  # Durchsicht 19
    g, e, mu, sg = kxt()
    if art == 'spitze':
        return zahl(f'{der(g)} {g} ist normalverteilt mit μ = {dz(mu)} {e} und σ = {dz(sg)} {e}. Bei welchem Wert hat die Glockenkurve ihre Spitze?',
                    f'Die Spitze liegt beim Mittelwert μ = {dz(mu)} {e}.', 'Wo liegen die meisten Werte?', mu, f'{mu}', einheit=e)
    if art == 'median':
        return zahl(f'{der(g)} {g} ist normalverteilt mit μ = {dz(mu)} {e} und σ = {dz(sg)} {e}. Wie groß ist der Median?',
                    f'Wegen der Symmetrie sind Median und Mittelwert gleich: {dz(mu)} {e}.', 'Die Glocke ist symmetrisch – wo liegt die Mitte der Daten?', mu, f'{mu}', einheit=e)
    if art == 'symmetrie':
        d = R.randint(1, 3) * sg
        r = f'Gleich häufig, weil die Kurve symmetrisch ist.'
        return auswahl(f'{der(g)} {g} ist normalverteilt mit μ = {dz(mu)} {e}. Was ist häufiger: Werte um {dz(mu - d)} {e} oder Werte um {dz(mu + d)} {e}?', r,
                       [f'Werte um {dz(mu - d)} {e}', f'Werte um {dz(mu + d)} {e}', 'Das kann man ohne σ nicht sagen.'],
                       f'{dz(mu - d)} und {dz(mu + d)} liegen gleich weit (je {dz(d)} {e}) vom Mittelwert entfernt.', 'Die Glockenkurve ist spiegelsymmetrisch zum Mittelwert.')
    if art == 'symmetrie_wert':
        d = R.choice([1, 2]) * sg
        p = anteil(-4, -(d // sg))
        return zahl(f'{der(g)} {g} ist normalverteilt mit μ = {dz(mu)} {e}. {dz(p)} % der Werte liegen unter {dz(mu - d)} {e}. Wie viel % liegen über {dz(mu + d)} {e}?',
                    f'{dz(mu - d)} und {dz(mu + d)} liegen symmetrisch zu μ. Also auch {dz(p)} %.', 'Spiegele am Mittelwert.', p, f'{float(p)}', einheit='%')
    if art == 'breite':
        s1, s2 = sorted(R.sample([2, 3, 4, 5, 6, 8, 10], 2))
        r = f'Die Kurve mit σ = {s2} ist breiter und flacher.'
        return auswahl(f'Zwei Normalverteilungen haben denselben Mittelwert μ = {dz(mu)}, aber σ = {s1} bzw. σ = {s2}. Was stimmt?', r,
                       [f'Die Kurve mit σ = {s2} ist schmaler und höher.', f'Die Kurve mit σ = {s2} liegt weiter rechts.', 'Beide Kurven sehen gleich aus.'],
                       'σ bestimmt die Breite: größeres σ – Werte streuen mehr – Glocke breiter und (gleiche Fläche) flacher. μ bestimmt nur die Lage.',
                       'Was bedeutet ein größeres σ für die Streuung der Werte?')
    if art == 'histogramm':
        glocke = [2, 7, 18, 26, 18, 7, 2]
        schief = R.choice([[3, 22, 26, 18, 11, 6, 4], [4, 6, 11, 18, 26, 22, 3]])
        flach = [14, 15, 14, 14, 15, 14, 14]
        zwei = [5, 20, 10, 4, 10, 20, 5]
        opts = [('A', glocke), ('B', schief), ('C', flach), ('D', zwei)]
        R.shuffle(opts)
        richtig = next(n for n, w in opts if w == glocke)
        tab = tabelle(['Diagramm'] + [str(i) for i in range(1, 8)], [[n] + w for n, w in opts])
        return mit_grafik(auswahl('Die Tabelle zeigt die Säulenhöhen (in %) von vier Histogrammen. Welches passt am besten zu einer Normalverteilung?', f'Diagramm {richtig}',
                                  [f'Diagramm {n}' for n, _ in opts],
                                  f'Diagramm {richtig} ist symmetrisch, hat eine Spitze in der Mitte und fällt nach beiden Seiten ab. Die anderen sind schief, flach oder haben zwei Gipfel.',
                                  'Achte auf: eine Spitze in der Mitte, symmetrisch, nach außen kleiner.'), tab)
    r = 'Falsch: Bei einer Normalverteilung sind Mittelwert und Median gleich.'
    return auswahl(f'Jemand behauptet: „{der(g)} {g} ist normalverteilt, aber der Median liegt deutlich über dem Mittelwert.“ Stimmt das?', r,
                   ['Richtig, der Median ist immer größer.', 'Richtig, wenn σ groß ist.', 'Falsch: Der Median ist immer kleiner.'],
                   'Symmetrische Verteilung: Die Hälfte der Werte liegt unter μ, die Hälfte darüber. Also Median = μ.', 'Was folgt aus der Symmetrie?')


def g_regel(s):
    g, e, mu, sg = kxt()
    k = R.choice([1, 2, 3]) if s > 1 else R.choice([1, 2])
    p = {1: 68, 2: 95, 3: Fr(997, 10)}[k]
    art = R.choice({1: ['prozent', 'grenzen'], 2: ['anzahl', 'grenzen', 'welches_k'], 3: ['anzahl', 'welches_k', 'grenzen_dez']}[s])  # Durchsicht 19: „welcher Bereich“ ist kein Stufe-3-Gedanke
    if art == 'prozent':
        return zahl(f'{der(g)} {g} ist normalverteilt mit μ = {dz(mu)} {e} und σ = {dz(sg)} {e}. Wie viel Prozent der Werte liegen etwa zwischen {dz(mu - k * sg)} {e} und {dz(mu + k * sg)} {e}?',
                    f'{dz(mu - k * sg)} = μ − {k if k > 1 else ""}σ und {dz(mu + k * sg)} = μ + {k if k > 1 else ""}σ. Nach der Regel: etwa {dz(p)} %.',
                    'Wie viele σ sind die Grenzen vom Mittelwert entfernt?', p, f'{float(p)}', einheit='%')
    if art == 'grenzen':
        return luecken(f'{der(g)} {g} ist normalverteilt mit μ = {dz(mu)} {e} und σ = {dz(sg)} {e}. Zwischen welchen Werten liegen etwa {dz(p)} % der Werte?',
                       f'□ {e} bis □ {e}', 'zwei ganze Zahlen', [mu - k * sg, mu + k * sg], f'{dz(p)} % ↔ μ ± {k if k > 1 else ""}σ: {dz(mu)} ∓ {dz(k * sg)} = {dz(mu - k * sg)} bis {dz(mu + k * sg)}.',
                       f'{dz(p)} % gehört zu μ ± {k if k > 1 else ""}σ.', c=[f'{mu} - {k} * {sg}', f'{mu} + {k} * {sg}'])
    if art == 'anzahl':
        N = R.choice([200, 500, 1000, 2000])
        n = Fr(N) * Fr(p) / 100
        if not endlich(n) or n.denominator != 1: return None
        return zahl(f'{dz(N)} Messwerte ({g}, μ = {dz(mu)} {e}, σ = {dz(sg)} {e}): Etwa wie viele Werte liegen zwischen {dz(mu - k * sg)} {e} und {dz(mu + k * sg)} {e}?',
                    f'Bereich μ ± {k if k > 1 else ""}σ: etwa {dz(p)} %. {dz(p)} % von {dz(N)} = {dz(n)}.', 'Erst den Prozentsatz bestimmen, dann von der Gesamtzahl berechnen.', n,
                    f'{N} * {float(p)} / 100')
    if art == 'welches_k':
        r = f'μ ± {k if k > 1 else ""}σ'
        return auswahl(f'In welchem Bereich liegen bei einer Normalverteilung etwa {dz(p)} % der Werte?', r, ['μ ± σ', 'μ ± 2σ', 'μ ± 3σ', 'μ ± 0,5σ'],
                       f'68 % ↔ μ ± σ, 95 % ↔ μ ± 2σ, 99,7 % ↔ μ ± 3σ.', 'Merke die drei Zahlen der Regel.')
    sg2 = R.choice([Fr(5, 2), Fr(3, 2), Fr(7, 2), Fr(9, 2)])
    mu2 = R.choice([20, 35, 50])
    return luecken(f'Ein Messwert ist normalverteilt mit μ = {mu2} und σ = {dz(sg2)}. Gib die Grenzen des Bereichs an, in dem etwa 95 % liegen.', '□ bis □', 'zwei ganze Zahlen',
                   [mu2 - int(2 * sg2), mu2 + int(2 * sg2)], f'95 % ↔ μ ± 2σ. 2σ = 2 · {dz(sg2)} = {dz(2 * sg2)}. {mu2} − {dz(2 * sg2)} = {dz(mu2 - 2 * sg2)}, {mu2} + {dz(2 * sg2)} = {dz(mu2 + 2 * sg2)}.',
                   'Welcher Bereich gehört zu 95 %? Rechne 2σ aus.', c=[f'{mu2} - 2 * {float(sg2)}', f'{mu2} + 2 * {float(sg2)}'])


def g_anteile(s):
    g, e, mu, sg = kxt()
    art = R.choice({1: ['ueber', 'unter'], 2: ['ueber', 'zwischen', 'unter', 'anzahl'], 3: ['zwischen_asym', 'anzahl', 'aussen']}[s])
    if art in ('ueber', 'unter'):
        k = R.choice([1, 2]) if s == 1 else R.choice([0, 1, 2, 3])
        if art == 'ueber':
            p, x = anteil(k, 4), mu + k * sg
            txt, w = f'mehr als {dz(x)} {e}', f'{dz(x)} = {grenzwort(k)}. Darüber liegen etwa {dz(p)} %.'
        else:
            p, x = anteil(-4, -k), mu - k * sg
            txt, w = f'weniger als {dz(x)} {e}', f'{dz(x)} = {grenzwort(-k)}. Darunter liegen etwa {dz(p)} %.'
        return zahl(f'{der(g)} {g} ist normalverteilt mit μ = {dz(mu)} {e} und σ = {dz(sg)} {e}. Wie viel Prozent haben etwa {txt}?', w,
                    'Rechne die Grenze in σ-Schritte um und nutze die Symmetrie (Hälften der 68/95/99,7 %).', p, f'{float(p)}', einheit='%')
    if art in ('zwischen', 'zwischen_asym'):
        a, b = sorted(R.sample([-3, -2, -1, 0, 1, 2, 3], 2))
        if art == 'zwischen' and not (a == 0 or b == 0): return None
        p = anteil(a, b)
        return zahl(f'{der(g)} {g} ist normalverteilt mit μ = {dz(mu)} {e} und σ = {dz(sg)} {e}. Wie viel Prozent liegen etwa zwischen {dz(mu + a * sg)} {e} und {dz(mu + b * sg)} {e}?',
                    f'Grenzen: {grenzwort(a)} und {grenzwort(b)}. Streifen addieren: etwa {dz(p)} %.', 'Teile den Bereich in σ-Streifen (34 %, 13,5 %, 2,35 %) und addiere.',
                    p, f'{float(p)}', einheit='%')
    if art == 'anzahl':
        N = R.choice([200, 400, 1000, 2000])
        k = R.choice([1, 2])
        p = anteil(k, 4)
        n = Fr(N) * p / 100
        if n.denominator != 1: return None
        return zahl(f'{dz(N)} Messwerte ({g}, μ = {dz(mu)} {e}, σ = {dz(sg)} {e}). Etwa wie viele liegen über {dz(mu + k * sg)} {e}?',
                    f'Über {grenzwort(k)}: etwa {dz(p)} %. {dz(p)} % von {dz(N)} = {dz(n)}.', 'Erst den Anteil, dann die Anzahl.', n, f'{N} * {float(p)} / 100')
    p = 100 - anteil(-2, 2)
    return zahl(f'{der(g)} {g} ist normalverteilt mit μ = {dz(mu)} {e} und σ = {dz(sg)} {e}. Wie viel Prozent liegen außerhalb von {dz(mu - 2 * sg)} bis {dz(mu + 2 * sg)} {e}?',
                f'Innerhalb μ ± 2σ: 95 %. Außerhalb: 100 % − 95 % = 5 % (je 2,5 % auf jeder Seite).', 'Was bleibt übrig, wenn 95 % innen liegen?', p, f'100 - {float(anteil(-2, 2))}', einheit='%')


def g_zwert(s):
    g, e, mu, sg = kxt()
    art = R.choice({1: ['z', 'z'], 2: ['z_neg', 'x', 'x_neg', 'z_dez'], 3: ['z_dez', 'x_neg', 'sigma']}[s])  # Durchsicht 19
    if art in ('z', 'z_neg'):
        z = R.choice([1, 2, 3]) * (-1 if art == 'z_neg' else 1)
        x = mu + z * sg
        return zahl(f'{g}: μ = {dz(mu)} {e}, σ = {dz(sg)} {e}. Berechne den z-Wert für x = {dz(x)} {e}.', f'z = ({dz(x)} − {dz(mu)}) : {dz(sg)} = {dz(x - mu)} : {dz(sg)} = {dz(z)}.',
                    'z = (x − μ) : σ. Unter dem Mittelwert wird z negativ.', z, f'({x} - {mu}) / {sg}')
    if art == 'z_dez':
        z = R.choice([Fr(1, 2), Fr(3, 2), Fr(-1, 2), Fr(5, 2), Fr(-3, 2), Fr(1, 4) * 3])
        x = mu + z * sg
        if not endlich(x): return None
        return zahl(f'{g}: μ = {dz(mu)} {e}, σ = {dz(sg)} {e}. Berechne den z-Wert für x = {dz(x)} {e}.', f'z = ({dz(x)} − {dz(mu)}) : {dz(sg)} = {dz(x - mu)} : {dz(sg)} = {dz(z)}.',
                    'Der z-Wert muss keine ganze Zahl sein.', z, f'({float(x)} - {mu}) / {sg}')
    if art in ('x', 'x_neg'):
        z = R.choice([1, 2, Fr(3, 2), Fr(1, 2)]) * (-1 if art == 'x_neg' else 1)
        x = mu + z * sg
        if not endlich(x): return None
        return zahl(f'{g}: μ = {dz(mu)} {e}, σ = {dz(sg)} {e}. Welcher Wert x hat den z-Wert {dz(z)}?', f'x = μ + z · σ = {dz(mu)} + {kl(z)} · {dz(sg)} = {dz(x)}.',
                    'x = μ + z · σ.', x, f'{mu} + ({float(z)}) * {sg}', einheit=e)
    z = R.choice([2, 3, -2, Fr(1, 2) * 3])
    sg2 = R.choice([4, 5, 8, 10])
    x = mu + z * sg2
    if not endlich(x): return None
    return zahl(f'{g}: μ = {dz(mu)} {e}. Der Wert x = {dz(x)} {e} hat den z-Wert {dz(z)}. Wie groß ist σ?', f'z = (x − μ) : σ ⇒ σ = (x − μ) : z = {dz(x - mu)} : {kl(z) if z == int(z) else dz(z)} = {dz(sg2)}.',
                'Stelle die z-Formel nach σ um.', sg2, f'({float(x)} - {mu}) / ({float(z)})', einheit=e)


FAECHER = [('Mathe', 'Deutsch'), ('Weitsprung', 'Sprint'), ('Test A', 'Test B'), ('Physik', 'Englisch')]


def g_vergleichen(s):
    art = R.choice({1: ['besser', 'ungewoehnlich'], 2: ['ungewoehnlich', 'zvergleich'], 3: ['besser_falle', 'ungewoehnlich_wert', 'zvergleich']}[s])  # Durchsicht 19
    if art in ('besser', 'besser_falle', 'zvergleich'):
        for _ in range(100):
            m1, s1, m2, s2 = R.choice([50, 60, 70]), R.choice([4, 5, 8, 10]), R.choice([40, 55, 65, 75]), R.choice([4, 5, 8, 10])
            z1, z2 = R.choice([Fr(1, 2), 1, Fr(3, 2), 2, Fr(5, 2)]), R.choice([Fr(1, 2), 1, Fr(3, 2), 2, Fr(5, 2)])
            x1, x2 = m1 + z1 * s1, m2 + z2 * s2
            if z1 != z2 and x1.denominator == 1 and x2.denominator == 1:
                if art != 'besser_falle' or ((x1 > x2) != (z1 > z2)): break
        else:
            return None
        f1, f2 = R.choice(FAECHER)
        vor = f'Ergebnis {f1}: {dz(x1)} Punkte (μ = {m1}, σ = {s1}). Ergebnis {f2}: {dz(x2)} Punkte (μ = {m2}, σ = {s2}).'
        if art == 'zvergleich':
            return zahl(vor + f' Um wie viel ist der z-Wert in {f1} größer als in {f2}?' if z1 > z2 else vor + f' Um wie viel ist der z-Wert in {f2} größer als in {f1}?',
                        f'z({f1}) = ({dz(x1)} − {m1}) : {s1} = {dz(z1)}; z({f2}) = ({dz(x2)} − {m2}) : {s2} = {dz(z2)}. Unterschied: {dz(abs(z1 - z2))}.',
                        'Berechne beide z-Werte und bilde die Differenz.', abs(z1 - z2), f'abs(({x1} - {m1}) / {s1} - ({x2} - {m2}) / {s2})')
        r = f1 if z1 > z2 else f2
        return auswahl(vor + ' In welchem Fach ist das Ergebnis im Vergleich zu den anderen besser?', r, [f1, f2, 'In beiden gleich gut'],
                       f'z({f1}) = {dz(z1)}, z({f2}) = {dz(z2)}. Der größere z-Wert ist relativ besser: {r}.', 'Vergleiche die z-Werte, nicht die Punkte.')
    g, e, mu, sg = kxt()
    if art == 'ungewoehnlich':
        z = R.choice([Fr(1, 2), 1, Fr(3, 2), Fr(5, 2), 3, -3, Fr(-5, 2), -1])
        x = mu + z * sg
        if not endlich(x): return None
        un = abs(z) > 2
        return ja_nein(f'{g}: μ = {dz(mu)} {e}, σ = {dz(sg)} {e}. Ist der Wert {dz(x)} {e} ungewöhnlich (|z| > 2)?', un,
                       f'z = ({dz(x)} − {dz(mu)}) : {dz(sg)} = {dz(z)}. |z| {">" if un else "≤"} 2: {"ungewöhnlich" if un else "nicht ungewöhnlich"}.',
                       'Berechne z und vergleiche den Betrag mit 2.')
    lo, hi = mu - 2 * sg, mu + 2 * sg
    return luecken(f'{g}: μ = {dz(mu)} {e}, σ = {dz(sg)} {e}. Ab welchen Werten gilt ein Ergebnis als ungewöhnlich klein bzw. groß (|z| > 2)? Gib die Grenzen an.',
                   f'unter □ {e} oder über □ {e}', 'zwei ganze Zahlen', [lo, hi], f'|z| > 2 heißt mehr als 2σ = {dz(2 * sg)} {e} vom Mittelwert entfernt: unter {dz(lo)} oder über {dz(hi)}.',
                   'Rechne μ − 2σ und μ + 2σ.', c=[f'{mu} - 2 * {sg}', f'{mu} + 2 * {sg}'])


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-2) ----------
# Prüfungsvorbilder: IB MYP Extended / Verlagsinhalt Normalverteilung (Glocken vergleichen, μ und σ aus einem 95-%-Bereich, Anteil zwischen
# μ − σ und μ + 2σ, „wie viele von n liegen außerhalb“, gleich gute Leistung in zwei Tests, z-Wert → Anteil). Eigene Zahlen.
def eigen3(art):
    if art == 'zwei_kurven':
        m1, m2 = R.sample([40, 50, 60, 70], 2)
        s1, s2 = R.sample([4, 6, 8, 10], 2)
        lo, hi = min(m1, m2) - 3 * max(s1, s2), max(m1, m2) + 3 * max(s1, s2)
        b = {'typ': 'koordinaten', 'x': [lo, hi], 'y': [0, 1.2], 'schritt_x': 10, 'schritt_y': 0.5, 'name_y': ' ',
             'graphen': [{'art': 'glocke', 'a': round(min(s1, s2) / s1, 3), 'mu': m1, 'sigma': s1, 'name': 'A', 'name_x': m1},
                         {'art': 'glocke', 'a': round(min(s1, s2) / s2, 3), 'mu': m2, 'sigma': s2, 'name': 'B', 'name_x': m2}]}
        groesser_mu = 'A' if m1 > m2 else 'B'
        groesser_s = 'A' if s1 > s2 else 'B'
        opt = {(m, s_): f'{m} hat den größeren Mittelwert, {s_} streut stärker.' for m in 'AB' for s_ in 'AB'}
        r = opt.pop((groesser_mu, groesser_s))
        return mit_grafik(auswahl('Die Zeichnung zeigt zwei Normalverteilungen A und B. Welche Aussage stimmt?', r, list(opt.values()),
                                  f'Die Spitze von A liegt bei {m1}, die von B bei {m2}: größerer Mittelwert bei {groesser_mu}. Die breitere, flachere Glocke ({groesser_s}) hat das größere σ.',
                                  'Mittelwert: Wo ist die Spitze? Streuung: Welche Glocke ist breiter?'), b)
    # nicht_normal
    r = 'die Augenzahl beim Würfeln mit einem fairen Würfel'
    return auswahl('Welche Größe ist am wenigsten normalverteilt?', r,
                   ['die Körpergröße erwachsener Frauen', 'die Füllmenge von Saftflaschen aus einer Maschine', 'das Gewicht von Äpfeln einer Sorte'],
                   'Beim fairen Würfel ist jede Augenzahl 1 bis 6 gleich wahrscheinlich: Das Säulendiagramm ist flach, keine Glocke. Die anderen Größen häufen sich um einen Mittelwert.',
                   'Gibt es einen Wert, um den sich die Ergebnisse häufen und nach außen seltener werden?')


def regel3(art):
    g, e, mu, sg = kxt()
    if art == 'sigma_aus_bereich':
        k = R.choice([1, 2])
        p = {1: '68', 2: '95'}[k]
        return luecken(f'{der(g)} {g} ist normalverteilt. Etwa {p} % der Werte liegen zwischen {dz(mu - k * sg)} {e} und {dz(mu + k * sg)} {e}. Bestimme μ und σ.',
                       'μ = □; σ = □', 'zwei ganze Zahlen', [mu, sg],
                       f'μ liegt in der Mitte: ({dz(mu - k * sg)} + {dz(mu + k * sg)}) : 2 = {dz(mu)}. {p} % gehören zu μ ± {k if k > 1 else ""}σ: {dz(mu + k * sg)} − {dz(mu)} = {dz(k * sg)}'
                       + (f', also σ = {dz(k * sg)} : {k} = {dz(sg)}.' if k > 1 else f' = σ.'),
                       f'Die Mitte des Bereichs ist μ. Welcher Bereich (μ ± σ, μ ± 2σ, …) gehört zu {p} %?', c=[str(mu), str(sg)])
    if art == 'anzahl_ausserhalb':
        n = R.choice([400, 600, 800, 1000, 2000])
        k = R.choice([2, 2, 3])
        p = {2: Fr(5), 3: Fr(3, 10)}[k]
        anz = n * p / 100
        if anz.denominator != 1: return None
        return zahl(f'{dz(n)} Werte: {g}, μ = {dz(mu)} {e}, σ = {dz(sg)} {e}. Etwa wie viele Werte liegen nicht zwischen {dz(mu - k * sg)} {e} und {dz(mu + k * sg)} {e}?',
                    f'Der Bereich ist μ ± {k}σ mit etwa {"95" if k == 2 else "99,7"} %. Außerhalb: {dz(p)} %. {dz(p)} % von {dz(n)} = {dz(anz)}.',
                    'Welcher Anteil liegt im Bereich? Der Rest liegt außerhalb.', anz, f'{n} * {float(p)} / 100')
    # modell: passt eine Normalverteilung?
    mu2, sg2 = R.choice([(10, 6), (8, 5), (6, 4), (12, 7)])
    r = f'Nein: μ − 2σ = {dz(mu2 - 2 * sg2)} min wäre eine negative Zeit, trotzdem müssten dort noch etwa 2,5 % liegen.'
    return auswahl(f'Fahrzeiten zur Schule haben μ = {mu2} min und σ = {sg2} min. Passt dazu eine Normalverteilung gut?', r,
                   ['Ja, Fahrzeiten sind immer normalverteilt.', 'Ja, weil σ kleiner als μ ist.', 'Nein, weil σ größer als 5 min ist.'],
                   f'Bei einer Normalverteilung lägen etwa 2,5 % unter μ − 2σ = {dz(mu2 - 2 * sg2)} min. Negative Fahrzeiten gibt es nicht: Das Modell passt schlecht (die echte Verteilung ist schief).',
                   'Berechne μ − 2σ. Ist so ein Wert in der Wirklichkeit möglich?')


def anteile3(art):
    g, e, mu, sg = kxt()
    if art == 'zusammengesetzt':
        a, b = R.choice([(-1, 2), (-2, 1), (-3, 1), (-1, 3), (-3, -1), (1, 3), (-2, 0)])
        p = anteil(a, b)
        return zahl(f'{der(g)} {g} ist normalverteilt mit μ = {dz(mu)} {e} und σ = {dz(sg)} {e}. Wie viel Prozent liegen etwa zwischen {dz(mu + a * sg)} {e} und {dz(mu + b * sg)} {e}?',
                    f'{dz(mu + a * sg)} ist {grenzwort(a)}, {dz(mu + b * sg)} ist {grenzwort(b)}. Streifen addieren: '
                    + ' + '.join(dz(STREIFEN[(u, u + 1)]) + ' %' for u in range(a, b)) + f' = {dz(p)} %.',
                    'Teile den Bereich in σ-Streifen (34 %, 13,5 %, 2,35 %) und addiere.', p, f'{float(p)}', einheit='%')
    # grenze_gesucht
    k, p = R.choice([(1, '16'), (2, '2,5')])
    oben = R.random() < .5
    gr = mu + k * sg if oben else mu - k * sg
    return zahl(f'{der(g)} {g} ist normalverteilt mit μ = {dz(mu)} {e} und σ = {dz(sg)} {e}. Ab welchem Wert gehört man zu den {p} % mit den {"größten" if oben else "kleinsten"} Werten?',
                f'{p} % liegen {"über" if oben else "unter"} {grenzwort(k if oben else -k)} = {dz(mu)} {"+" if oben else "−"} {dz(k * sg)} = {dz(gr)} {e}.',
                f'Welche σ-Grenze schneidet {p} % ab?', gr, f'{mu} {"+" if oben else "-"} {k} * {sg}', einheit=e)


def z3(art):
    g, e, mu, sg = kxt()
    if art == 'z_anteil':
        z = R.choice([-2, -1, 1, 2])
        oben = R.random() < .5
        p = anteil(z, 4) if oben else anteil(-4, z)
        return zahl(f'{g}: μ = {dz(mu)} {e}, σ = {dz(sg)} {e}. Ein Wert hat den z-Wert {dz(z)}. Wie viel Prozent der Werte liegen etwa {"darüber" if oben else "darunter"}?',
                    f'z = {dz(z)} heißt: der Wert liegt bei {grenzwort(z)}. {"Darüber" if oben else "Darunter"} liegen etwa {dz(p)} % (68-95-99,7-Regel, halbiert und addiert).',
                    'Übersetze den z-Wert in eine σ-Grenze und nutze die Faustregel.', p, f'{float(p)}', einheit='%')
    # mu_aus_z
    z = R.choice([-2, -1.5, -1, 1, 1.5, 2])
    x = mu + z * sg
    if x != int(x): return None
    return zahl(f'{g}: σ = {dz(sg)} {e}. Der Wert {dz(int(x))} {e} hat den z-Wert {dz(z)}. Wie groß ist μ?',
                f'z = (x − μ) : σ ⇒ x − μ = z · σ = {dz(z * sg)} ⇒ μ = {dz(int(x))} − {kl(z * sg)} = {dz(mu)} {e}.',
                'Stelle z = (x − μ) : σ nach μ um.', mu, f'{int(x)} - ({z}) * {sg}', einheit=e)


def vergl3(art):
    if art == 'gleich_gut':
        m1, s1, m2, s2 = R.choice([50, 60, 70]), R.choice([4, 5, 8, 10]), R.choice([55, 65, 75]), R.choice([4, 5, 8, 10])
        z = R.choice([0.5, 1, 1.5, 2, -1])
        x1, x2 = m1 + z * s1, m2 + z * s2
        if x1 != int(x1) or x2 != int(x2) or (m1, s1) == (m2, s2): return None
        return zahl(f'Test A: μ = {m1}, σ = {s1}. Test B: μ = {m2}, σ = {s2}. Wie viele Punkte in Test B sind genauso gut wie {int(x1)} Punkte in Test A?',
                    f'z in A: ({int(x1)} − {m1}) : {s1} = {dz(z)}. Gleich gut heißt gleicher z-Wert: x = {m2} + {kl(z)} · {s2} = {dz(int(x2))}.',
                    'Berechne den z-Wert in Test A und übertrage ihn auf Test B.', int(x2), f'{m2} + ({int(x1)} - {m1}) / {s1} * {s2}')
    if art == 'drei':
        faecher = ['Mathe', 'Deutsch', 'Englisch']
        zs = R.sample([-1, 0.5, 1, 1.5, 2], 3)
        daten = []
        for f, z in zip(faecher, zs):
            m, s_ = R.choice([50, 60, 70]), R.choice([4, 5, 8, 10])
            x = m + z * s_
            if x != int(x): return None
            daten.append((f, int(x), m, s_, z))
        best = max(daten, key=lambda d: d[4])
        return auswahl('Ergebnisse: ' + '; '.join(f'{f}: {x} Punkte (μ = {m}, σ = {s_})' for f, x, m, s_, _ in daten) + '. In welchem Fach ist das Ergebnis im Vergleich am besten?',
                       best[0], [d[0] for d in daten if d != best] + ['In allen gleich gut'],
                       'z-Werte: ' + '; '.join(f'{f}: ({x} − {m}) : {s_} = {dz(z)}' for f, x, m, s_, z in daten) + f'. Am größten: {best[0]}.',
                       'Rechne für jedes Fach den z-Wert aus.')
    # prozent_besser
    g, e, mu, sg = kxt()
    z = R.choice([1, 2, -1])
    x = mu + z * sg
    p = anteil(z, 4)
    return zahl(f'{g}: μ = {dz(mu)} {e}, σ = {dz(sg)} {e}. Jemand hat den Wert {dz(x)} {e}. Wie viel Prozent haben etwa einen größeren Wert?',
                f'z = ({dz(x)} − {dz(mu)}) : {dz(sg)} = {dz(z)}. Über {grenzwort(z)} liegen etwa {dz(p)} %.',
                'Erst den z-Wert, dann die Faustregel.', p, f'{float(p)}', einheit='%')


def _filter(g, s, teil, nicht=False):
    for _ in range(120):
        t = g(s)
        if t and ((teil in t['f']['text']) != nicht): return t
    return None


def g2_eigenschaften(s):
    if s < 3: return g_eigenschaften(s)
    art = art3('fehler', 'zwei_kurven', 'nicht_normal', ['fehler', 'zwei_kurven', 'zwei_kurven', 'fehler', 'zwei_kurven'])
    if art == 'fehler': return _filter(g_eigenschaften, 3, 'behauptet')
    return eigen3(art)


def g2_regel(s):
    if s < 3: return g_regel(s)
    art = art3('sigma_aus_bereich', 'anzahl_ausserhalb', 'modell', ['sigma_aus_bereich', 'anzahl_ausserhalb', 'modell', 'grenzen_dez', 'sigma_aus_bereich'])
    if art == 'grenzen_dez': return _filter(g_regel, 3, 'Grenzen')
    return regel3(art)


def g2_anteile(s):
    if s < 3: return g_anteile(s)
    art = art3('zusammengesetzt', 'aussen', 'grenze_gesucht', ['zusammengesetzt', 'aussen', 'grenze_gesucht', 'anzahl', 'zusammengesetzt'])
    if art == 'aussen': return _filter(g_anteile, 3, 'außerhalb')
    if art == 'anzahl': return _filter(g_anteile, 3, 'Messwerte')
    return anteile3(art)


def g2_zwert(s):
    if s < 3: return g_zwert(s)
    art = art3('z_anteil', 'mu_aus_z', 'sigma', ['z_anteil', 'mu_aus_z', 'sigma', 'z_dez', 'z_anteil'])
    if art == 'sigma': return _filter(g_zwert, 3, 'Wie groß ist σ')
    if art == 'z_dez': return _filter(g_zwert, 3, 'Berechne den z-Wert')
    return z3(art)


def g2_vergleichen(s):
    if s == 1: return g_vergleichen(1)
    if s == 2: return g_vergleichen(R.choice([2, 3]))
    return vergl3(art3('gleich_gut', 'drei', 'prozent_besser', ['gleich_gut', 'drei', 'prozent_besser', 'gleich_gut', 'drei']))


GEN = dativ({'eigenschaften': g2_eigenschaften, 'regel': g2_regel, 'anteile': g2_anteile, 'zwert': g2_zwert, 'vergleichen': g2_vergleichen})

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

import math  # noqa: E402

from _umbau_rest import ko, pkte, tab  # noqa: E402


def _dichte(x, mu, s):
    return round(math.exp(-((x - mu) ** 2) / (2 * s * s)), 3)


def _fl(mu, s, a, b):
    """Fläche unter der Glocke (Höhe 1) von a bis b als Vieleck."""
    n = 24
    xs = [a + (b - a) * i / n for i in range(n + 1)]
    return {'punkte': [[a, 0]] + [[round(x, 3), _dichte(x, mu, s)] for x in xs] + [[b, 0]]}


def _gl(mu, s, name_x, **kw):
    g = [{'art': 'glocke', 'a': 1, 'mu': mu, 'sigma': s}] + kw.pop('mehr', [])
    return ko([mu - 4 * s, mu + 4 * s], [0, 1.2], schritt=0, schritt_x=2 * s, schritt_y=0.5, name_x=name_x, name_y=' ', graphen=g, **kw)


def _z(zm, zd):
    return tab(['Fach', 'Punkte', 'μ', 'σ', 'z'], ['Mathe', '78', '70', '4', zm], ['Deutsch', '85', '75', '10', zd])


UMBAU = {
    'eigenschaften': {
        'einstieg': 'Eine Maschine füllt Saftflaschen mit 500 ml. Mal sind es 498 ml, mal 503 ml, ganz selten 485 ml. '
                    'Die Häufigkeiten bilden eine Glocke. Man sagt: Die Füllmenge ist ⟦normalverteilt⟧.',
        'woerter': [['normalverteilt', 'die meisten Werte liegen nahe beim Mittelwert, symmetrisch wie eine Glocke'],
                    ['μ', 'griechisch „mü“: der Mittelwert'],
                    ['σ', 'griechisch „sigma“: die Standardabweichung; sie bestimmt die Breite']],
        'bild': _gl(500, 5, 'ml'),
        'schritte': [
            {'text': 'Füllmengen: μ = 500 ml und σ = 5 ml.'},
            {'text': 'Die Spitze der Glocke liegt bei ⟦500 ml⟧.', 'bild': {'punkte': pkte({'μ': (500, 1)})}},
            {'text': '495 ml und 505 ml liegen gleich weit weg: gleich häufig.', 'bild': {'senkrecht': [495, 505]}},
            {'text': 'Wegen der Symmetrie ist auch der Median ⟦500 ml⟧.'},
        ],
        'fehler': '„Größeres σ macht die Glocke höher“ ist falsch. Größeres σ heißt ⟦breiter und flacher⟧, die Gesamtfläche bleibt 100 %.',
        'fehler_bild': {'graphen': [{'art': 'glocke', 'a': 1, 'mu': 500, 'sigma': 5, 'name': 'σ = 5', 'name_x': 505},
                                    {'art': 'glocke', 'a': 0.5, 'mu': 500, 'sigma': 10, 'name': 'σ = 10', 'name_x': 513}], 'punkte': None, 'senkrecht': None},
        'regel': 'Normalverteilt: eine Glocke, ⟦symmetrisch um μ⟧. σ bestimmt die Breite.',
    },
    'regel': {
        'einstieg': 'Die Körpergröße 15-jähriger Jungen ist normalverteilt mit μ = 170 cm und σ = 6 cm. Wie viele sind zwischen 158 cm und 182 cm groß? '
                    'Es hilft die ⟦68-95-99,7-Regel⟧.',
        'woerter': [['μ ± σ', 'der Bereich von μ − σ bis μ + σ'],
                    ['68-95-99,7-Regel', 'Faustregel für die Anteile in den Bereichen μ ± σ, μ ± 2σ, μ ± 3σ']],
        'bild': _gl(170, 6, 'cm'),
        'schritte': [
            {'text': 'μ ± σ: 164 cm bis 176 cm, das sind etwa 68 %.', 'bild': {'flaechen': [_fl(170, 6, 164, 176)]}},
            {'text': 'μ − 2σ = 158 cm und μ + 2σ = 182 cm.', 'bild': {'flaechen': [_fl(170, 6, 158, 182)]}},
            {'text': 'Dazwischen liegen etwa ⟦95 %⟧ der Jungen.'},
            {'text': 'μ ± 3σ umfasst etwa 99,7 %.', 'bild': {'flaechen': [_fl(170, 6, 152, 188)]}},
        ],
        'fehler': '„Bei μ ± 2σ sind es 2 · 68 % = 136 %“ ist falsch. Mehr als 100 % geht nicht: ⟦68, 95, 99,7⟧.',
        'regel': 'Faustregel: ⟦68 %, 95 %, 99,7 %⟧. Das gilt für μ ± σ, μ ± 2σ und μ ± 3σ.',
    },
    'anteile': {
        'einstieg': 'Ein Test ist normalverteilt mit μ = 60 Punkten und σ = 10. Wie viele haben mehr als 70 Punkte? '
                    'Die Glocke ist auf beiden Seiten gleich. Das nutzt man: ⟦Symmetrie⟧.',
        'woerter': [['Symmetrie', 'links und rechts von μ sieht die Glocke gleich aus']],
        'bild': _gl(60, 10, 'Pkt'),
        'schritte': [
            {'text': '70 Punkte sind μ + σ.', 'bild': {'senkrecht': [70]}},
            {'text': 'Außerhalb von μ ± σ liegen 100 % − 68 % = 32 %.',
             'bild': {'flaechen': [_fl(60, 10, 20, 50), _fl(60, 10, 70, 100)]}},
            {'text': 'Wegen der Symmetrie liegt die Hälfte oben: ⟦16 %⟧.', 'bild': {'flaechen': [_fl(60, 10, 70, 100)]}},
        ],
        'fehler': '„Über μ + σ liegen 32 %“ ist falsch. Die 32 % verteilen sich auf ⟦beide Seiten⟧, oben ist nur die Hälfte.',
        'regel': 'Wegen der Symmetrie die Anteile ⟦halbieren⟧. Über μ + σ liegen 16 %, über μ + 2σ 2,5 %.',
    },
    'zwert': {
        'einstieg': 'Ein Junge ist 182 cm groß. Ist das viel? Das hängt davon ab, wie stark die Größen streuen. '
                    'Der ⟦z-Wert⟧ sagt, wie viele σ er über dem Mittelwert liegt.',
        'woerter': [['z-Wert', 'z = (x − μ) : σ, der Abstand zum Mittelwert in σ-Schritten']],
        'bild': _gl(170, 6, 'cm', senkrecht=[170]),
        'schritte': [
            {'text': 'Gegeben: μ = 170 cm, σ = 6 cm, x = 182 cm.'},
            {'text': 'Abstand zum Mittelwert: 182 − 170 = 12 cm.', 'bild': {'senkrecht': [170, 182], 'pfeile': [[170, 0.3, 182, 0.3, '12']]}},
            {'text': 'In σ-Schritten: z = 12 : 6 = ⟦2⟧.', 'bild': {'pfeile': [[170, 0.3, 176, 0.3, 'σ'], [176, 0.3, 182, 0.3, 'σ']]}},
        ],
        'fehler': 'z = 182 : 6 ist falsch. Zuerst den ⟦Abstand zum Mittelwert⟧ bilden, dann durch σ teilen.',
        'regel': '⟦z = (x − μ) : σ⟧. Positiv heißt über dem Mittelwert, negativ darunter.',
    },
    'vergleichen': {
        'einstieg': 'Mathe: 78 Punkte. Deutsch: 85 Punkte. Welches Ergebnis ist besser? Das hängt davon ab, wie die anderen abgeschnitten haben. '
                    'Mit z-Werten kann man ⟦fair vergleichen⟧.',
        'woerter': [['ungewöhnlich', 'ab |z| > 2; nur etwa 5 % liegen so weit außen']],
        'bild': _z('?', '?'),
        'schritte': [
            {'text': 'Mathe: z = (78 − 70) : 4 = 2.', 'bild': _z('2', '?')},
            {'text': 'Deutsch: z = (85 − 75) : 10 = 1.', 'bild': _z('2', '1')},
            {'text': 'Größerer z-Wert: ⟦Mathe ist relativ besser⟧, trotz weniger Punkten.'},
            {'text': 'Ab |z| > 2 gilt ein Ergebnis als ungewöhnlich.'},
        ],
        'fehler': 'Nur 85 > 78 vergleichen ist falsch. Die Tests sind ⟦verschieden verteilt⟧, erst in z-Werte umrechnen.',
        'regel': 'Verschiedene Verteilungen: in ⟦z-Werte⟧ umrechnen und vergleichen. Ab |z| > 2 ist ein Wert ungewöhnlich.',
    },
}
UMBAU_OFFEN = ['Umbau (Paket UR): Die Lernkarten zeigen jetzt echte Glockenkurven (Graph-Art glocke) mit gefärbten Flächen (flaechen). '
               'Die Aufgaben-Grafiken bleiben unverändert (Säulen in Glockenform).']
UMBAU_WEG = ['App-Wunsch: Graphart „Glockenkurve“']
# ---------- Ende UMBAU ----------


d = bauen('daten.normalverteilung',
      'Die Normalverteilung als Modell kennen, Anteile mit der 68-95-99,7-Regel abschätzen, z-Werte berechnen und Ergebnisse vergleichen.',
      ['Normalverteilung (normal distribution): Glockenkurve, symmetrisch um μ; Mittelwert = Median = Modus.',
       'σ bestimmt die Breite: größer = breiter und flacher.',
       '68 % in μ ± σ, 95 % in μ ± 2σ, 99,7 % in μ ± 3σ.',
       'Hälften: 34 % | 13,5 % | 2,35 % je Seite; über μ + σ: 16 %, über μ + 2σ: 2,5 %.',
       'z-Wert (z-score): z = (x − μ) : σ; |z| > 2 gilt als ungewöhnlich.'],
      [('Das Modell', ['eigenschaften', 'regel']), ('Anteile', ['anteile']), ('Standardisieren', ['zwert', 'vergleichen'])],
      ETAPPEN, GEN,
      offen=['Ohne Lehrplan-Zuordnung (Verlagsinhalt IB Extended); Niveau Klasse 9/10 angenommen. Rechnung nur mit der 68-95-99,7-Regel, keine Tabellen der Standardnormalverteilung und keine Taschenrechner-Funktionen (normalcdf).',
             'App-Wunsch: Graphart „Glockenkurve“ (Normalverteilungsdichte mit μ und σ, Fläche zwischen zwei Grenzen färbbar). Bisher Ersatz: Säulendiagramm in Glockenform und Tabelle der Streifen-Anteile.',
             'Feld klasse: {"zusatz": 10} statt {} (Prüfskript verlangt einen Eintrag) – siehe FRAGE im Postfach.'], plan=PLAN2)
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
