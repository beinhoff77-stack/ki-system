#!/usr/bin/env python3
"""Thema terme.aufstellen – Terme aufstellen und deuten (Gymnasium Bayern, Klasse 7)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl7 import A, L, Z, baue, cz, einsetzen, eur, figur, kl, lin, zt  # noqa: E402

META = {'thema_schluessel': 'terme.aufstellen', 'thema_id': 28, 'block_id': 63, 'klasse': {'rs_by': 6, 'gym_by': 7, 'ib_myp': 1}}
HW = 'Tippe den Term ein, z. B. 3x + 5 oder 2(x − 1).'

ETAPPEN = [
    {'lernziel': 'struktur', 'titel': 'Termart bestimmen',
     'regel': 'Die ⟦Termart⟧ richtet sich nach der Rechenart, die man ⟦zuletzt⟧ ausführt: Summe (+), Differenz (−), Produkt (·) oder Quotient (:). Klammern werden zuerst gerechnet.',
     'schritte': ['Term: 5 · (x + 2)', 'Zuerst die Klammer x + 2, zuletzt mal 5.', 'Der Term ist ein ⟦Produkt⟧.'],
     'fehler': '3x + 4 ist kein Produkt, obwohl „3x“ ein Mal enthält: Zuletzt wird ⟦addiert⟧ (Punkt vor Strich). Es ist eine Summe.',
     '_verbot': ['5 · (x + 2)']},
    {'lernziel': 'termwert', 'titel': 'Termwerte berechnen',
     'regel': 'Für die Variable wird eine Zahl ⟦eingesetzt⟧. Negative Zahlen kommen in ⟦Klammern⟧. Dann gilt: Klammer vor Potenz vor Punkt vor Strich.',
     'schritte': ['T(x) = 2x² − 3x für x = −2', '2 · (−2)² − 3 · (−2) = 2 · 4 + 6', '= ⟦14⟧'],
     'fehler': 'Für x = −2 ist 2x² nicht 2 · (−4): Es wird ⟦erst quadriert⟧, (−2)² = 4, dann mal 2. Also 8.',
     '_verbot': ['2x² − 3x']},
    {'lernziel': 'uebersetzen', 'titel': 'Wortterme in Terme übersetzen',
     'regel': 'Übersetze Wort für Wort: ⟦Summe⟧ +, ⟦Differenz⟧ −, ⟦Produkt⟧ ·, ⟦Quotient⟧ :, ⟦das Dreifache⟧ 3 ·, ⟦vermehrt um⟧ +, ⟦vermindert um⟧ −. Was zuerst gerechnet werden soll, kommt in ⟦Klammern⟧.',
     'schritte': ['„Das Doppelte der Summe aus x und 5“', 'Summe aus x und 5: (x + 5)', 'Das Doppelte davon: ⟦2(x + 5)⟧'],
     'fehler': '„Das Doppelte der Summe aus x und 5“ ist nicht 2x + 5. Dort wird nur x verdoppelt. Gemeint ist die ganze ⟦Summe⟧: 2(x + 5) = 2x + 10.',
     '_verbot': ['Summe aus x und 5']},
    {'lernziel': 'sachsituation', 'titel': 'Terme zu Sachsituationen',
     'regel': 'Lege fest, wofür die ⟦Variable⟧ steht (z. B. x = Anzahl der Stunden). Feste Beträge werden ⟦addiert⟧, Beträge „pro Stück“ werden ⟦mit x multipliziert⟧.',
     'schritte': ['Ein Fahrradverleih: 5 € Grundgebühr, 3 € pro Stunde.', 'x = Anzahl der Stunden', 'Kosten: ⟦3x + 5⟧ (in €)'],
     'fehler': 'Der Term 5x + 3 vertauscht die Rollen: Dann würde die ⟦Grundgebühr pro Stunde⟧ anfallen. Was pro Stunde anfällt, steht vor dem x.',
     '_verbot': ['5 € Grundgebühr, 3 € pro Stunde']},
    {'lernziel': 'muster', 'titel': 'Figurenfolgen mit Termen beschreiben',
     'regel': 'Bei einer ⟦Figurenfolge⟧ suchst du, ⟦wie viel pro Schritt dazukommt⟧. Kommen pro Figur 3 dazu, steht im Term 3 · n. Dann passt du die Zahl an, sodass Figur 1 stimmt.',
     'schritte': ['Hölzer: Figur 1: 4, Figur 2: 7, Figur 3: 10. Pro Figur kommen 3 Hölzer dazu.', 'Schau ins Bild: Ganz links steht 1 senkrechtes Holz. Jedes Quadrat bringt 3 neue Hölzer mit: oben, unten und rechts.', 'Figur n hat n Quadrate: 1 + 3 · n Hölzer, also ⟦3n + 1⟧. Figur 10: 31 Hölzer.'],
     'probe': 'n = 2: 3 · 2 + 1 = 7 ✓',
     'fehler': 'Der Term n + 3 passt nicht zu 4, 7, 10: Für n = 2 ergibt er 5. Die ⟦Zunahme pro Schritt⟧ (3) gehört vor das n.',
     'bild': figur({'_a0': [0, 0], '_a1': [1, 0], '_a2': [2, 0], '_a3': [3, 0], '_b0': [0, 1], '_b1': [1, 1], '_b2': [2, 1], '_b3': [3, 1]},
                   linien=[['_a0', '_a1'], ['_a1', '_a2'], ['_a2', '_a3'], ['_b0', '_b1'], ['_b1', '_b2'], ['_b2', '_b3'],
                           ['_a0', '_b0'], ['_a1', '_b1'], ['_a2', '_b2'], ['_a3', '_b3', 'Figur 3: 10 Hölzer']]),
     '_verbot': ['Figur 1: 4, Figur 2: 7, Figur 3: 10', 'Quadrate in einer Reihe: Figur 1: 4,']},
    {'lernziel': 'deuten', 'titel': 'Terme deuten und prüfen',
     'regel': 'Einen Term ⟦deuten⟧ heißt: sagen, was jede Zahl und jede Variable in der Situation bedeutet. Passt eine Deutung nicht zu allen Teilen, ist sie ⟦falsch⟧.',
     'schritte': ['Handytarif: K = 0,1x + 8 (x = Minuten, K in €)', '8: feste Grundgebühr; 0,1: Preis pro Minute', 'Für 50 Minuten: K = ⟦13 €⟧'],
     'fehler': 'In K = 0,1x + 8 ist 8 nicht der Preis pro Minute. Was pro Minute zählt, steht ⟦vor dem x⟧.',
     '_verbot': ['K = 0,1x + 8']},
]

ARTEN = ['Summe', 'Differenz', 'Produkt', 'Quotient']


def nz(R, lo, hi): return R.choice([k for k in range(lo, hi + 1) if k])


BAU = [  # (Beschreibung, richtig, Ablenker) – Platzhalter a, b
    ('ein Produkt, dessen erster Faktor eine Summe ist', '(x + {b}) · {a}', ['x + {b} · {a}', '{a} · x + {b}', '(x · {b}) + {a}']),
    ('eine Differenz aus einem Quotienten und einer Zahl', 'x : {a} − {b}', ['x : ({a} − {b})', '(x − {b}) : {a}', '{a} · x − {b}']),
    ('ein Quotient, dessen Dividend eine Differenz ist', '(x − {b}) : {a}', ['x − {b} : {a}', 'x : ({a} − {b})', '{a} · (x − {b})']),
    ('eine Summe aus einem Produkt und einer Zahl', '{a} · x + {b}', ['{a} · (x + {b})', 'x : {a} + {b}', '({a} + x) · {b}']),
    ('ein Produkt aus einer Zahl und einer Differenz', '{a} · (x − {b})', ['{a} · x − {b}', '{a} − {b} · x', '(x − {b}) : {a}']),
    ('eine Differenz aus einer Zahl und einem Produkt', '{b} − {a} · x', ['({b} − {a}) · x', '{a} · x − {b}', '{b} · ({a} − x)']),
]


def g_struktur(R, st):
    a, b = R.randint(2, 9), R.randint(1, 9)
    v = R.choice(['x', 'a', 'y'])
    if st == 3 and R.random() < .5:
        d, r, f = R.choice(BAU)
        a = R.randint(2, 9); b = R.choice([k for k in range(2, 10) if k != a])
        r = r.format(a=a, b=b)
        return A(R, f'Welcher Term ist {d}?', r, [x.format(a=a, b=b) for x in f],
                 f'{r}: Die zuletzt ausgeführte Rechnung bestimmt die Termart – das passt zu „{d}“.', 'Welche Rechnung kommt zuletzt? Was wird vorher in Klammern berechnet?')
    art = R.choice(ARTEN)
    if st == 1:
        t = {'Summe': f'{a}{v} + {b}', 'Differenz': f'{a}{v} − {b}', 'Produkt': f'{a} · ({v} + {b})', 'Quotient': f'({v} + {b}) : {a}'}[art]
    elif st == 2:
        c = R.randint(2, 9)
        t = {'Summe': f'{a}{v} + {v} : {c}', 'Differenz': f'({v} + {a}) − {b}{v}', 'Produkt': f'({v} − {a}) · ({v} + {b})', 'Quotient': f'({a}{v} − {b}) : {c}'}[art]
    else:
        c = R.randint(2, 9)
        t = {'Summe': f'{a} · ({v} − {b}) + {c}', 'Differenz': f'{v}² − {a}{v}', 'Produkt': f'{c} · ({a}{v} − {b})', 'Quotient': f'({v}² + {a}) : ({v} − {b})'}[art]
    zuletzt = {'Summe': 'addiert', 'Differenz': 'subtrahiert', 'Produkt': 'multipliziert', 'Quotient': 'dividiert'}[art]
    return A(R, f'Welche Termart hat der Term {t}?', art, [x for x in ARTEN if x != art],
             f'Rechenreihenfolge: Klammern, dann Punkt vor Strich. Zuletzt wird {zuletzt} – also {"eine" if art in ("Summe", "Differenz") else "ein"} {art}.', 'Welche Rechnung würdest du ganz zum Schluss ausführen?')


def g_termwert(R, st):
    if st == 1:
        m, t = nz(R, -9, 9), R.randint(-12, 12); x = R.randint(-6, 8)
        T = lin(m, t)
        return Z(f'Berechne den Wert von {T} für x = {zt(x)}.', m * x + t, f'({m}) * ({x}) + ({t})', f'x = {zt(x)} einsetzen: {einsetzen(T, x)} = {zt(m * x + t)}.',
                 'Setze die Zahl für x ein. Negative Zahlen in Klammern.')
    if st == 2 and R.random() < .35:
        return _wertetabelle(R)
    if st == 2:
        a, b, c = nz(R, -3, 3), R.randint(-6, 6), R.randint(-9, 9); x = R.randint(-5, 5)
        T = (('−' if a < 0 else '') + ('' if abs(a) == 1 else str(abs(a))) + 'x²')
        if b: T += f' {"+" if b > 0 else "−"} {lin(abs(b), 0)}'
        if c: T += f' {"+" if c > 0 else "−"} {abs(c)}'
        w = a * x * x + b * x + c
        return Z(f'Berechne den Wert von {T} für x = {zt(x)}.', w, f'({a}) * ({x}) ** 2 + ({b}) * ({x}) + ({c})', f'x = {zt(x)} einsetzen: {einsetzen(T, x)} = {zt(w)}.',
                 'Erst quadrieren, dann multiplizieren, dann addieren.')
    a, b = nz(R, -6, 6), nz(R, -6, 6)
    p, q = nz(R, -5, 5), nz(R, -5, 5)
    form = R.choice(['prod', 'quot'])
    if form == 'prod':
        T = f'{zt(p)}a − {zt(q)}b' if q > 0 else f'{zt(p)}a + {zt(-q)}b'
        T = T.replace('1a', 'a') if abs(p) == 1 else T
        w = p * a - q * b
        return Z(f'Berechne den Wert von {T} für a = {zt(a)} und b = {zt(b)}.', w, f'({p}) * ({a}) - ({q}) * ({b})',
                 f'Einsetzen: {zt(p)} · {kl(a)} {"−" if q > 0 else "+"} {zt(abs(q))} · {kl(b)} = {zt(w)}.', 'Setze für a und b jeweils die Zahl ein.')
    while True:
        a, b = R.randint(-8, 8), R.randint(-6, 6)
        if a + b != 0 and Fr(a * b, a + b).denominator in (1, 2, 4, 5): break
    w = Fr(a * b, a + b)
    return Z(f'Berechne den Wert von (a · b) : (a + b) für a = {zt(a)} und b = {zt(b)}.', w, f'({a}) * ({b}) / (({a}) + ({b}))',
             f'Zähler: {kl(a)} · {kl(b)} = {zt(a * b)}. Nenner: {kl(a)} + {kl(b)} = {zt(a + b)}. {zt(a * b)} : {kl(a + b)} = {zt(w)}.', 'Rechne Zähler und Nenner getrennt aus.')


def _wertetabelle(R):
    xs = sorted(R.sample([-3, -2, -1, 0, 1, 2, 3], 3))
    art = R.choice(['quad', 'prod', 'lin'])
    if art == 'quad':
        a, c = R.choice([1, 2, 3, -1]), R.randint(-6, 6)
        T = ('−' if a < 0 else '') + ('' if abs(a) == 1 else str(abs(a))) + 'x²' + (f' {"+" if c > 0 else "−"} {abs(c)}' if c else '')
        f, ce = (lambda x: a * x * x + c), (lambda x: f'({a}) * ({x}) ** 2 + ({c})')
    elif art == 'prod':
        p, q = R.randint(1, 4), R.randint(1, 4)
        T = f'(x + {p})(x − {q})'
        f, ce = (lambda x: (x + p) * (x - q)), (lambda x: f'(({x}) + {p}) * (({x}) - {q})')
    else:
        m, t = nz(R, -5, 5), R.randint(-8, 8)
        T = lin(m, t)
        f, ce = (lambda x: m * x + t), (lambda x: f'({m}) * ({x}) + ({t})')
    werte = [f(x) for x in xs]
    schab = '; '.join(f'x = {zt(x)}: □' for x in xs)
    return L(f'Ergänze die Wertetabelle für den Term {T}.', schab, werte, [ce(x) for x in xs],
             '; '.join(f'x = {zt(x)}: {einsetzen(T, x)} = {zt(v)}' for x, v in zip(xs, werte)) + '.', 'Setze jeden x-Wert einzeln ein. Negative Zahlen in Klammern.',
             'Trage je Feld den Termwert ein (auch negative Zahlen).')


ZAHLWORT = {2: 'Doppelte', 3: 'Dreifache', 4: 'Vierfache', 5: 'Fünffache', 6: 'Sechsfache', 10: 'Zehnfache'}


def g_uebersetzen(R, st):
    k = R.choice(list(ZAHLWORT)); b = R.randint(1, 12)
    if st == 1:
        art = R.choice(['plus', 'minus', 'summe'])
        if art == 'plus':
            txt, werte, w = f'das {ZAHLWORT[k]} von x, vermehrt um {b}', [k, b], f'{k}x + {b}'
        elif art == 'minus':
            txt, werte, w = f'das {ZAHLWORT[k]} von x, vermindert um {b}', [k, -b], f'{k}x − {b}'
        else:
            txt, werte, w = f'die Summe aus dem {ZAHLWORT[k]}n von x und {b}', [k, b], f'{k}x + {b}'
        return L(f'Schreibe als Term: {txt}.', '□x + □', werte, [str(v) for v in werte], f'{txt[0].upper() + txt[1:]}: {w}.', 'Übersetze Wort für Wort.', HW)
    if st == 2:
        art = R.choice(['diff_umgekehrt', 'klammer_summe', 'klammer_diff'])
        if art == 'diff_umgekehrt':
            return L(f'Schreibe als Term: die Differenz aus {b} und dem {ZAHLWORT[k]}n von x.', '□x + □', [-k, b], [str(-k), str(b)],
                     f'Differenz aus {b} und {k}x: {b} − {k}x.', 'Bei „Differenz aus A und B“ steht A vorne: A − B.', HW)
        if art == 'klammer_summe':
            return L(f'Schreibe als Term: das {ZAHLWORT[k]} der Summe aus x und {b}.', '□(x + □)', [k, b], [str(k), str(b)],
                     f'Summe aus x und {b}: (x + {b}). Das {ZAHLWORT[k]}: {k}(x + {b}).', 'Was zuerst gerechnet wird, kommt in eine Klammer.', HW)
        return L(f'Schreibe als Term: das {ZAHLWORT[k]} der Differenz aus x und {b}.', '□(x − □)', [k, b], [str(k), str(b)],
                 f'Differenz aus x und {b}: (x − {b}). Das {ZAHLWORT[k]}: {k}(x − {b}).', 'Was zuerst gerechnet wird, kommt in eine Klammer.', HW)
    # Stufe 3: Term → Worte (Auswahl) oder längere Wortterme
    if R.random() < .5:
        c = R.randint(2, 9)
        return L(f'Schreibe als Term und fasse zusammen: Zum {ZAHLWORT[k]}n von x wird die Summe aus x und {b} addiert, danach wird {c} subtrahiert.', '□x + □',
                 [k + 1, b - c], [f'{k} + 1', f'{b} - {c}'], f'{k}x + (x + {b}) − {c} = {lin(k + 1, b - c)}.', 'Erst aufschreiben, dann gleiche Glieder zusammenfassen.', HW)
    t = f'{k}(x − {b})'
    r = f'das {ZAHLWORT[k]} der Differenz aus x und {b}'
    return A(R, f'Welcher Wortterm passt zu {t}?', r, [f'das {ZAHLWORT[k]} von x, vermindert um {b}', f'die Differenz aus {b} und dem {ZAHLWORT[k]}n von x',
                                                       f'das {ZAHLWORT[k]} der Summe aus x und {b}'],
             f'In der Klammer steht die Differenz x − {b}, sie wird mit {k} multipliziert.', 'Was steht in der Klammer, was passiert danach?')


def g_sachsituation(R, st):
    art = R.choice({1: ['verleih', 'kino'], 2: ['verleih', 'kino', 'rechteck', 'alter', 'abo', 'taxi'], 3: ['rechteck', 'zwei', 'wert', 'vergleich', 'vergleich']}[st])
    if art == 'vergleich': return _tarifvergleich(R)
    if art == 'abo':
        g, p = R.choice([5, 8, 10, 12]), R.choice([2, 3, 4])
        return L(f'Ein Streamingdienst kostet {g} € im Monat, jeder ausgeliehene Film zusätzlich {p} €. Gib den Term für die Monatskosten (in €) bei x Filmen an.', '□x + □',
                 [p, g], [str(p), str(g)], f'{p} € je Film: {p}x. Dazu die Monatsgebühr {g} €: {p}x + {g}.', 'Was je Film anfällt, kommt vor das x.', HW)
    if art == 'taxi':
        g, p = R.choice([4, 5, 6]), R.choice([2, 3])
        return L(f'Eine Taxifahrt kostet {g} € Grundpreis und {p} € je Kilometer. Gib den Term für den Fahrpreis (in €) bei x Kilometern an.', '□x + □',
                 [p, g], [str(p), str(g)], f'{p} € je km: {p}x. Dazu der Grundpreis {g} €: {p}x + {g}.', 'Was je Kilometer anfällt, kommt vor das x.', HW)
    if art == 'verleih':
        g, p = R.choice([3, 4, 5, 6, 8, 10]), R.choice([2, 3, 4, 5, 6])
        return L(f'Ein Kanuverleih verlangt {g} € Grundgebühr und {p} € pro Stunde. Gib den Term für die Kosten (in €) bei x Stunden an.', '□x + □', [p, g], [str(p), str(g)],
                 f'{p} € pro Stunde: {p}x. Dazu die Grundgebühr {g} €: {p}x + {g}.', 'Was pro Stunde anfällt, kommt vor das x.', HW)
    if art == 'kino':
        e, s = R.choice([7, 8, 9, 10, 11, 12]), R.choice([2, 3, 4, 5])
        n = R.randint(2, 6)
        return L(f'Eine Kinokarte kostet {e} €. Eine Gruppe kauft x Karten und zusammen einmal Popcorn für {s} €. Gib den Term für den Gesamtpreis (in €) an.', '□x + □', [e, s], [str(e), str(s)],
                 f'x Karten zu {e} €: {e}x. Popcorn einmal: + {s}. Term: {e}x + {s}.', 'Was mehrfach gekauft wird, wird mit x multipliziert.', HW)
    if art == 'rechteck':
        d = R.randint(1, 9)
        if st == 3 and R.random() < .5:
            x = R.randint(3, 15)
            return Z(f'Ein Rechteck ist x cm breit und {d} cm länger als breit. Stelle einen Term für den Umfang auf und berechne ihn für x = {x}.', 4 * x + 2 * d,
                     f'4 * {x} + 2 * {d}', f'Umfang: 2 · x + 2 · (x + {d}) = 4x + {2 * d}. Für x = {x}: 4 · {x} + {2 * d} = {4 * x + 2 * d} cm.',
                     'Länge = x + Unterschied. Umfang = 2 · Breite + 2 · Länge.', 'cm')
        return L(f'Ein Rechteck ist x cm breit und {d} cm länger als breit. Gib einen Term für den Umfang (in cm) an.', '□x + □', [4, 2 * d], ['4', f'2 * {d}'],
                 f'Länge x + {d}. Umfang: 2x + 2(x + {d}) = 4x + {2 * d}.', 'Länge = x + Unterschied. Umfang = 2 · Breite + 2 · Länge.', HW)
    if art == 'alter':
        d = R.randint(2, 9)
        if R.random() < .5:
            v = R.randint(26, 38)
            return L(f'Ein Kind ist x Jahre alt. Seine Schwester ist {d} Jahre älter, der Vater ist {v} Jahre älter als das Kind. Gib einen Term für das Alter aller drei zusammen an.', '□x + □',
                     [3, d + v], ['3', f'{d} + {v}'], f'x + (x + {d}) + (x + {v}) = 3x + {d + v}.', 'Schreibe jedes Alter mit x auf und addiere.', HW)
        return L(f'Ein Kind ist x Jahre alt. Seine Schwester ist {d} Jahre älter, der Vater ist 3-mal so alt wie das Kind. Gib einen Term für das Alter aller drei zusammen an.', '□x + □',
                 [5, d], ['1 + 1 + 3', str(d)], f'x + (x + {d}) + 3x = 5x + {d}.', 'Schreibe jedes Alter mit x auf und addiere.', HW)
    if art == 'zwei':
        p1, p2 = R.choice([(1, 2), (1, 3), (2, 3), (2, 4)])
        n = R.randint(10, 30)
        return L(f'Für ein Fest werden {n} Getränke gekauft: x Flaschen Saft zu {p2} € und der Rest Wasser zu {p1} €. Gib einen Term für den Gesamtpreis (in €) an und fasse zusammen.', '□x + □',
                 [p2 - p1, p1 * n], [f'{p2} - {p1}', f'{p1} * {n}'], f'Wasser: {n} − x Flaschen. {p2}x + {p1}({n} − x) = {lin(p2 - p1, p1 * n)}.',
                 'Wie viele Wasserflaschen sind es, wenn es x Saftflaschen sind?', HW)
    if R.random() < .5:
        g, p = Fr(R.choice([5, 8, 10, 12])), Fr(R.choice([150, 200, 250, 300]), 100)
        x = R.choice([2, 3, 4, 5, 6])
        return Z(f'Ein Mobilfunktarif kostet {eur(g)} € im Monat; jedes zusätzlich gebuchte GB Datenvolumen kostet {eur(p)} €. Stelle einen Term auf und berechne die Kosten bei x = {x} zusätzlichen GB.',
                 g + p * x, f'{cz(g)} + {cz(p)} * {x}', f'Term: {zt(p)}x + {zt(g)}. Für x = {x}: {zt(p)} · {x} + {zt(g)} = {eur(g + p * x)} €.', 'Grundgebühr + Preis je GB · Anzahl.', '€')
    g, p = Fr(R.choice([5, 8, 10, 12])), Fr(R.choice([199, 299, 399]), 100)
    x = R.choice([2, 3, 4, 5])
    return Z(f'Ein Streamingdienst kostet {eur(g)} € im Monat, jeder ausgeliehene Film {eur(p)} €. Stelle einen Term auf und berechne die Monatskosten bei x = {x} Filmen.', g + p * x,
             f'{cz(g)} + {cz(p)} * {x}', f'Term: {zt(p)}x + {zt(g)}. Für x = {x}: {zt(p)} · {x} + {zt(g)} = {eur(g + p * x)} €.', 'Monatsgebühr + Preis je Film · Anzahl.', '€')


VERGLEICH = [('Kletterhalle', 'Besuch', 'Besuchen', 'je Besuch', 'Jahreskarte'), ('Schwimmbad', 'Besuch', 'Besuchen', 'je Eintritt', 'Saisonkarte'),
             ('Fahrradverleih', 'Stunde', 'Stunden', 'je Stunde', 'Grundgebühr'), ('Bootsverleih', 'Stunde', 'Stunden', 'je Stunde', 'Grundgebühr')]


def _tarifvergleich(R):
    ort, ein, mehr, je, fix = R.choice(VERGLEICH)
    for _ in range(200):
        pA = R.choice([4, 5, 6, 7, 8, 9, 10]); pB = R.choice([k for k in range(1, pA)]); gB = R.choice([10, 12, 15, 20, 24, 25, 30, 36, 40])
        d, e = gB, pA - pB
        gleich = R.random() < .5
        if gleich and d % e == 0 and 2 <= d // e <= 20: break
        if not gleich and d % e != 0 and 2 <= d // e <= 20: break
    if gleich:
        n = d // e
        return Z(f'{ort}: Tarif A kostet {pA} € {je}. Tarif B: {fix} {gB} €, dazu {pB} € {je}. Bei wie vielen {mehr} kosten beide gleich viel?', n, f'{d} / {e}',
                 f'A: {pA}x, B: {pB}x + {gB}. Gleich: {pA}x = {pB}x + {gB} → {e}x = {gB} → x = {n}. Probe: {pA * n} € = {pB * n + gB} €.',
                 'Stelle für beide Tarife einen Term auf und setze sie gleich.')
    n = d // e + 1
    return Z(f'{ort}: Tarif A kostet {pA} € {je}. Tarif B: {fix} {gB} €, dazu {pB} € {je}. Ab wie vielen {mehr} ist Tarif B billiger?', n, f'{d} // {e} + 1',
             f'A: {pA}x, B: {pB}x + {gB}. B spart je {ein} {e} €, die {fix} von {gB} € muss aufgeholt werden: {gB} : {e} ≈ {zt(Fr(str(round(d / e, 1))))}. '
             f'Bei {n - 1}: A {pA * (n - 1)} €, B {pB * (n - 1) + gB} €. Bei {n}: A {pA * n} €, B {pB * n + gB} € → ab {n}.',
             'Stelle beide Terme auf und probiere Werte in der Nähe des Gleichstands.', mehr)


def _bild_quadrate(n):
    pk = {}
    for i in range(n + 1): pk[f'_o{i}'] = [i, 1]; pk[f'_u{i}'] = [i, 0]
    li = [[f'_o{i}', f'_o{i + 1}'] for i in range(n)] + [[f'_u{i}', f'_u{i + 1}'] for i in range(n)] + [[f'_o{i}', f'_u{i}'] for i in range(n + 1)]
    return figur(pk, linien=li)


def _bild_dreiecke(n):
    pk, zz = {}, []
    for j in range(n + 2):
        name = f'_z{j}'
        pk[name] = [j // 2 if j % 2 == 0 else j // 2 + 0.5, 0 if j % 2 == 0 else 0.87]
        zz.append(name)
    li = [[zz[j], zz[j + 1]] for j in range(n + 1)]
    unten, oben = zz[0::2], zz[1::2]
    li += [[unten[j], unten[j + 1]] for j in range(len(unten) - 1)] + [[oben[j], oben[j + 1]] for j in range(len(oben) - 1)]
    return figur(pk, linien=li)


def _bild_sechsecke(n):
    pk, li = {}, []
    for i in range(n + 1):
        x = round(i * 1.74, 2)
        pk[f'_lo{i}'] = [x, 0.5]; pk[f'_lu{i}'] = [x, -0.5]
        li.append([f'_lo{i}', f'_lu{i}'])
    for i in range(n):
        x = round(i * 1.74 + 0.87, 2)
        pk[f'_t{i}'] = [x, 1]; pk[f'_b{i}'] = [x, -1]
        li += [[f'_lo{i}', f'_t{i}'], [f'_t{i}', f'_lo{i + 1}'], [f'_lu{i}', f'_b{i}'], [f'_b{i}', f'_lu{i + 1}']]
    return figur(pk, linien=li)


def _kaestchen(zellen, flaeche=None):
    """Plättchen als Quadrate (Zellen (x, y) mit Kantenlänge 1)."""
    pk, li, seen = {}, [], set()
    def pt(x, y):
        n = f'_p{x}_{y}'.replace('-', 'm'); pk[n] = [x, y]; return n
    for x, y in zellen:
        for a, b in (((x, y), (x + 1, y)), ((x, y + 1), (x + 1, y + 1)), ((x, y), (x, y + 1)), ((x + 1, y), (x + 1, y + 1))):
            if (a, b) in seen: continue
            seen.add((a, b)); li.append([pt(*a), pt(*b)])
    fl = None
    if flaeche:
        (x0, y0), (x1, y1) = flaeche
        fl = [pt(x0, y0), pt(x1, y0), pt(x1, y1), pt(x0, y1)]
    return figur(pk, linien=li, flaeche=fl)


def _bild_l(n):
    return _kaestchen([(0, j) for j in range(n)] + [(i, 0) for i in range(1, n)])


def _bild_beet(n):
    rand = [(x, 1) for x in range(n + 2)] + [(x, -1) for x in range(n + 2)] + [(0, 0), (n + 1, 0)]
    return _kaestchen(rand + [(x, 0) for x in range(1, n + 1)], flaeche=((1, 0), (n + 1, 1)))


# (Name im Text, Zunahme, Rest, Zeichnung)
MUSTER = [
    ('Streichhölzer für Quadrate in einer Reihe', 3, 1, _bild_quadrate), ('Streichhölzer für Dreiecke in einer Reihe', 2, 1, _bild_dreiecke),
    ('Streichhölzer für Sechsecke in einer Reihe', 5, 1, _bild_sechsecke), ('Sitzplätze an einer Reihe aus n zusammengeschobenen Tischen', 2, 2, None),
    ('Plättchen in einer L-Form mit Armen aus n Plättchen', 2, -1, _bild_l), ('Randplatten um ein Beet aus n Platten in einer Reihe', 2, 6, _bild_beet),
]

BEGRUENDUNG = [
    ('Streichhölzer für Quadrate in einer Reihe: Ganz links steht 1 Holz, jedes Quadrat bringt 3 neue Hölzer mit (oben, unten, rechts).', '3n + 1', ['4n', '3n', 'n + 3'], _bild_quadrate),
    ('Streichhölzer für Dreiecke in einer Reihe: Ganz links steht 1 Holz, jedes Dreieck bringt 2 neue Hölzer mit.', '2n + 1', ['3n', '2n', 'n + 2'], _bild_dreiecke),
    ('Streichhölzer für Sechsecke in einer Reihe: Ganz links steht 1 Holz, jedes Sechseck bringt 5 neue Hölzer mit.', '5n + 1', ['6n', '5n', 'n + 5'], _bild_sechsecke),
    ('Tische in einer Reihe: An jeden Tisch passen 2 Personen an die Längsseiten, an die beiden Enden der Reihe je 1 Person.', '2n + 2', ['4n', '2n', 'n + 2'], None),
    ('Ein Beet aus n Platten in einer Reihe wird mit Randplatten umlegt: oben und unten je n + 2 Platten, links und rechts je 1 Platte.', '2n + 6', ['2n + 4', 'n + 6', '4n + 2'], _bild_beet),
    ('Eine L-Form hat einen Arm aus n Plättchen nach oben und einen aus n Plättchen nach rechts; das Eckplättchen gehört zu beiden Armen.', '2n − 1', ['2n', '2n + 1', 'n + 1'], _bild_l),
]


def g_muster(R, st):
    if st == 3 and R.random() < .4:
        text, r, f, bild = R.choice(BEGRUENDUNG)
        n = R.randint(3, 4)
        a = A(R, f'{text} Welcher Term gibt die Anzahl bei Figur n an?', r, f,
              f'Feststück plus gleiches Stück pro Figur: {r}. Probe mit dem Bild oder für n = 1.', 'Was ist in jeder Figur gleich, was kommt pro Schritt dazu?')
        if bild: a['f']['grafik'] = bild(n); a['f']['text'] = a['f']['text'].replace('Welcher Term', f'Das Bild zeigt Figur {n}. Welcher Term')
        return a
    a, bild = _g_muster(R, st)
    import re
    w = re.findall(r'Figur (\d+): (\d+)', a['f']['text'])
    if bild:
        a['f']['grafik'] = bild(3)
        a['f']['text'] = a['f']['text'].replace('. ', '. Das Bild zeigt Figur 3. ', 1)
    elif w:
        a['f']['grafik'] = {'typ': 'tabelle', 'kopf': ['Figur n'] + [n for n, _ in w], 'zeilen': [['Anzahl'] + [v for _, v in w]]}
    return a


def _g_muster(R, st):
    name, m, t, bild = R.choice(MUSTER)
    if R.random() < .4:
        name, m, t, bild = 'Plättchen in einer Figurenfolge', R.randint(2, 7), R.randint(-1, 6), None
    werte = [m * n + t for n in (1, 2, 3)]
    folge = ', '.join(f'Figur {n}: {v}' for n, v in zip((1, 2, 3), werte))
    if st == 1:
        k = R.randint(4, 8)
        return Z(f'{name}: {folge}. Wie viele sind es bei Figur {k}?', m * k + t, f'{m} * {k} + ({t})',
                 f'Pro Figur kommen {m} dazu: Figur {k}: {werte[2]} + {m} · {k - 3} = {m * k + t}.', 'Wie viele kommen von Figur zu Figur dazu?'), bild
    if st == 2:
        return L(f'{name}: {folge}. Gib einen Term für die Anzahl bei Figur n an.', '□n + □', [m, t], [str(m), str(t)],
                 f'Pro Figur +{m}: {m}n. Für n = 1 muss {werte[0]} herauskommen: {m} + □ = {werte[0]} → □ = {zt(t)}. Term: {lin(m, t, "n")}.', 'Zunahme pro Schritt vor das n, dann für n = 1 anpassen.',
                 'Tippe den Term mit n ein, z. B. 3n + 1.'), bild
    if R.random() < .5:
        k = R.randint(20, 100)
        return Z(f'{name}: {folge}. Wie viele sind es bei Figur {k}?', m * k + t, f'{m} * {k} + ({t})',
                 f'Term {lin(m, t, "n")}. Für n = {k}: {m} · {k} {"+" if t >= 0 else "−"} {abs(t)} = {m * k + t}.', 'Stelle erst einen Term auf, dann setze n ein.'), bild
    k = R.randint(10, 60)
    N = m * k + t
    return Z(f'{name}: {folge}. Welche Figur braucht genau {N}?', k, f'({N} - ({t})) / {m}',
             f'{lin(m, t, "n")} = {N} → {m}n = {N - t} → n = {k}.', 'Stelle den Term auf und setze ihn gleich der Anzahl.'), bild


def g_deuten(R, st):
    kontext = R.choice(['taxi', 'handy', 'kerze', 'konto', 'parken'])
    if kontext == 'taxi':
        g, p = Fr(R.choice([35, 40, 45]), 10), Fr(R.choice([20, 22, 25]), 10)
        T, x, bm, bg = f'P = {zt(p)}x + {zt(g)}', 'x = gefahrene km, P in €', f'der Preis pro Kilometer', 'der Grundpreis'
    elif kontext == 'handy':
        g, p = Fr(R.choice([5, 8, 10])), Fr(R.choice([5, 9, 10]), 100)
        T, x, bm, bg = f'K = {zt(p)}x + {zt(g)}', 'x = Gesprächsminuten, K in €', 'der Preis pro Minute', 'die monatliche Grundgebühr'
    elif kontext == 'kerze':
        g, p = Fr(R.choice([20, 24, 30])), Fr(-R.choice([2, 3]))
        T, x, bm, bg = f'h = {zt(g)} − {zt(-p)}x', 'x = Brenndauer in Stunden, h in cm', 'die Abnahme der Höhe pro Stunde', 'die Höhe der Kerze am Anfang'
    elif kontext == 'konto':
        g, p = Fr(R.choice([50, 80, 120])), Fr(R.choice([5, 10, 15]))
        T, x, bm, bg = f'S = {zt(g)} + {zt(p)}x', 'x = Anzahl der Wochen, S in €', 'der Betrag, der jede Woche gespart wird', 'das Startguthaben'
    else:
        g, p = Fr(R.choice([1, 2])), Fr(R.choice([150, 200, 250]), 100)
        T, x, bm, bg = f'P = {zt(p)}x + {zt(g)}', 'x = Parkdauer in Stunden, P in €', 'der Preis pro Stunde', 'die Einfahrtsgebühr'
    if st == 1:
        welche = R.choice(['m', 'g'])
        zahl = abs(p) if welche == 'm' else g
        r = bm if welche == 'm' else bg
        return A(R, f'{T} ({x}). Was bedeutet die Zahl {zt(zahl)}?', r[0].upper() + r[1:], [s[0].upper() + s[1:] for s in [bg if welche == 'm' else bm, 'der Wert ganz am Ende', 'die Anzahl x']],
                 f'{zt(zahl)} ist {r}.', 'Steht die Zahl vor dem x (pro Einheit) oder allein (fest)?')
    if st == 2:
        k = R.choice([j for j in (2, 3, 4, 5, 6, 8, 10) if p * j + g > 0])
        v = p * k + g
        satz = {'taxi': lambda k, v: f'Eine Fahrt von {zt(k)} km kostet {eur(v)} €.', 'handy': lambda k, v: f'Bei {zt(k)} Minuten kostet es im Monat {eur(v)} €.',
                'kerze': lambda k, v: f'Nach {zt(k)} Stunden ist die Kerze noch {zt(v)} cm hoch.', 'konto': lambda k, v: f'Nach {zt(k)} Wochen sind {eur(v)} € gespart.',
                'parken': lambda k, v: f'Wer {zt(k)} Stunden parkt, zahlt {eur(v)} €.'}[kontext]
        je = {'taxi': f'Jeder Kilometer kostet {eur(v)} €.', 'handy': f'Jede Minute kostet {eur(v)} €.', 'kerze': f'Die Kerze brennt in jeder Stunde {zt(v)} cm ab.',
              'konto': f'Jede Woche werden {eur(v)} € gespart.', 'parken': f'Jede Stunde kostet {eur(v)} €.'}[kontext]
        falsche = [je, satz(k, abs(p) * k) if abs(p) * k != v else satz(k + 1, v), satz(v, k) if v != k and v.denominator == 1 and 0 < v <= 200 else satz(k, v + g)]
        if R.random() < .5:
            rechnung = f'{zt(g)} − {zt(-p)} · {k}' if p < 0 else f'{zt(p)} · {k} + {zt(g)}'
            frage = f'{T} ({x}). Was bedeutet die Rechnung {rechnung} = {zt(v)}?'
        else:
            frage = f'{T} ({x}). Was bedeutet {T[0]} = {zt(v)}?'
        return A(R, frage, satz(k, v), falsche, f'Für x = {k} ergibt der Term {zt(v)}. Also: {satz(k, v)}', 'Wofür steht x, wofür steht das Ergebnis?')
    # Stufe 3: Fehler finden in einer Übersetzung – Ablenker passend zur jeweiligen Aufgabe
    k, b = R.randint(2, 6), R.randint(2, 9)
    zw = ZAHLWORT.get(k, f'{k}-fache')
    fall = R.choice(['klammer', 'reihenfolge', 'richtig'])
    if fall == 'klammer':
        satz, term = f'das {zw} der Summe aus x und {b}', f'{k}x + {b}'
        r = f'Falsch: Die Summe muss in Klammern stehen, richtig ist {k}(x + {b}).'
        f = ['Richtig übersetzt.', f'Falsch: richtig ist x + {k} · {b}.', f'Falsch: richtig ist {k} · x · {b}.']
    elif fall == 'reihenfolge':
        satz, term = f'die Differenz aus {b} und x', f'x − {b}'
        r = f'Falsch: Bei „Differenz aus {b} und x“ steht {b} vorne, richtig ist {b} − x.'
        f = ['Richtig übersetzt.', f'Falsch: richtig ist x + {b}.', f'Falsch: richtig ist {b}x.']
    else:
        satz, term = f'das {zw} von x, vermehrt um {b}', f'{k}x + {b}'
        r = 'Richtig übersetzt.'
        f = [f'Falsch: richtig ist {k}(x + {b}).', f'Falsch: richtig ist {k} + x + {b}.', f'Falsch: richtig ist {k}x · {b}.']
    return A(R, f'Jemand übersetzt „{satz}“ in den Term {term}. Stimmt das?', r, f, r,
             'Übersetze selbst und vergleiche – achte auf Klammern und Reihenfolge.')


GEN = {'struktur': g_struktur, 'termwert': g_termwert, 'uebersetzen': g_uebersetzen, 'sachsituation': g_sachsituation, 'muster': g_muster, 'deuten': g_deuten}

# Verständliche Fassung (Runde 7, Maßstab inhalte/README.md „Verständliche Erklärungen“):
# Alltagssituation zuerst (einstieg), jedes neue Wort erklärt (woerter), Beispiel in kleinen Schritten, Merksatz am Ende (regel).
# Durchgehende Situation: ein Fahrradverleih am See.
KLAR = {
 'struktur': {
  'einstieg': 'Beim Fahrradverleih am See kostet ein Rad 2 € Grundgebühr und 3 € für die erste Stunde, zusammen 5 €. Eine Familie leiht 5 Räder. Die Kassiererin rechnet erst 2 + 3 und nimmt das Ergebnis dann mal 5: 25 €. Rechnet sie stattdessen erst 5 · 2 und zählt dann 3 dazu, kommen falsche 13 € heraus. So eine Rechnung heißt ⟦Term⟧, und welche Rechnung man zuletzt ausführt, bestimmt die ⟦Termart⟧.',
  'woerter': [['Term', 'eine Rechnung aus Zahlen, Buchstaben und Rechenzeichen, zum Beispiel 5 · (2 + 3) oder 3x + 4'],
              ['Variable', 'ein Buchstabe wie x als Platzhalter für eine Zahl, die man noch nicht kennt oder die sich ändern kann'],
              ['3x', 'kurz für 3 · x; vor einem Buchstaben darf das Malzeichen fehlen'], ['Termart', 'Name des Terms nach der Rechnung, die man zuletzt ausführt'],
              ['Summe / Differenz', 'zuletzt wird addiert (+) / subtrahiert (−)'], ['Produkt / Quotient', 'zuletzt wird malgenommen (·) / geteilt (:)'],
              ['Punkt vor Strich', '· und : rechnet man vor + und −']],
  'schritte': ['Der Term ist 5 · (x + 2). Schau zuerst, in welcher Reihenfolge gerechnet wird.',
               'Was in Klammern steht, rechnet man zuerst: x + 2.',
               'Danach wird das Ergebnis der Klammer mal 5 genommen. Das ist die letzte Rechnung.',
               'Die letzte Rechnung ist ein Malnehmen. Also ist der Term ein ⟦Produkt⟧.'],
  'regel': 'So bestimmst du die ⟦Termart⟧: Überlege, welche Rechnung du ⟦zuletzt⟧ ausführst. Klammern kommen zuerst, dann Punkt vor Strich. Zuletzt + heißt Summe, − Differenz, · Produkt, : Quotient.',
  'fehler': '3x + 4 ist kein Produkt, obwohl in 3x ein Mal steckt. Punkt vor Strich: Erst wird 3 · x gerechnet, ⟦zuletzt wird addiert⟧. Es ist eine Summe – wie beim Verleih, wenn man erst 3 Stunden zu je x € ausrechnet und am Ende noch 4 € Gebühr dazuzählt.'},
 'termwert': {
  'einstieg': 'Der Fahrradverleih hat eine Preistafel: „3 € pro Stunde plus 5 € Grundgebühr“. Als Term heißt das 3x + 5; x ist dabei die Anzahl der Stunden. Will ein Kunde wissen, was 4 Stunden kosten, setzt man für x die 4 ein: 3 · 4 + 5 = 17 €. Das Ergebnis heißt ⟦Termwert⟧.',
  'woerter': [['einsetzen', 'für die Variable eine bestimmte Zahl hinschreiben'], ['Termwert', 'das Ergebnis, wenn man eine Zahl eingesetzt und ausgerechnet hat'],
              ['T(x)', 'Name für einen Term mit der Variablen x; T(−2) ist sein Wert für x = −2'], ['x²', '„x hoch 2“, also x · x'], ['quadrieren', 'eine Zahl mit sich selbst malnehmen, zum Beispiel 4² = 4 · 4 = 16'],
              ['Potenz', 'eine Rechnung mit Hochzahl wie x² oder 4³'], ['(−2)²', '(−2) · (−2) = 4; die Klammer zeigt: das Minus wird mitquadriert']],
  'schritte': ['Gegeben ist T(x) = 2x² − 3x. Gesucht ist der Termwert für x = −2.',
               'Schreibe überall, wo x steht, die −2 hin – in Klammern, weil sie negativ ist: 2 · (−2)² − 3 · (−2).',
               'Zuerst die Potenz: (−2)² = 4. Dann die Malrechnungen: 2 · 4 = 8 und 3 · (−2) = −6.',
               'Zum Schluss abziehen: 8 − (−6) = 8 + 6 = ⟦14⟧.'],
  'regel': 'So berechnest du einen ⟦Termwert⟧: Für die Variable die Zahl ⟦einsetzen⟧, negative Zahlen in ⟦Klammern⟧. Dann der Reihe nach rechnen: Klammer, Potenz, Punkt, Strich.',
  'fehler': 'Für x = −2 ist 2x² nicht 2 · (−4). Es wird ⟦erst quadriert⟧: (−2)² = 4, dann mal 2, also 8. Ohne Klammer würde man nur die 2 quadrieren und das Minus hinterher davorschreiben – das ist eine andere Rechnung.'},
 'uebersetzen': {
  'einstieg': 'Die Chefin des Fahrradverleihs sagt am Telefon: „Nimm die Leihgebühr und zähl 5 € Pfand dazu – und das Ganze mal zwei, es sind zwei Kinder.“ Um das richtig zu rechnen, schreibt man den Satz als Rechnung auf. Ein Term in Worten heißt ⟦Wortterm⟧; ihn in Zeichen zu schreiben heißt ⟦übersetzen⟧.',
  'woerter': [['Wortterm', 'ein Term in Worten, zum Beispiel „das Doppelte der Summe aus x und 5“'], ['das Doppelte / das Dreifache', 'mal 2 / mal 3'],
              ['vermehrt um / vermindert um', 'plus / minus'], ['2(x + 5)', 'kurz für 2 · (x + 5): die ganze Klammer wird verdoppelt']],
  'schritte': ['Der Wortterm lautet: „das Doppelte der Summe aus x und 5“.',
               'Suche zuerst, was zusammengehört: „die Summe aus x und 5“ ist x + 5.',
               'Diese Summe soll als Ganzes verdoppelt werden. Darum kommt sie in Klammern: (x + 5).',
               'Jetzt verdoppeln: ⟦2(x + 5)⟧.'],
  'regel': 'So übersetzt du Wort für Wort: Summe +, Differenz −, Produkt ·, Quotient :, das Dreifache 3 ·, vermehrt um +, vermindert um −. Was ⟦zuerst⟧ gerechnet werden soll, kommt in ⟦Klammern⟧.',
  'fehler': '„Das Doppelte der Summe aus x und 5“ ist nicht 2x + 5. Dort wird nur das x verdoppelt – als würde für das zweite Kind nur die Leihgebühr bezahlt, aber kein Pfand. Gemeint ist die ganze ⟦Summe⟧: 2(x + 5) = 2x + 10.'},
 'sachsituation': {
  'einstieg': 'Jetzt baust du die Preistafel des Fahrradverleihs selbst: 5 € Grundgebühr, egal wie lange, und 3 € für jede Stunde. Wie viele Stunden ein Kunde fährt, ist noch offen – dafür nimmt man einen Buchstaben. So entsteht ein ⟦Term zu einer Sachsituation⟧, mit dem man jeden Preis ausrechnen kann.',
  'woerter': [['Sachsituation', 'eine Aufgabe aus dem Alltag, hier der Fahrradverleih'], ['Grundgebühr', 'ein fester Betrag, der immer einmal anfällt, egal wie lange'],
              ['pro Stunde', 'für jede Stunde einmal – das wird mit der Anzahl der Stunden malgenommen']],
  'schritte': ['Lege zuerst fest, wofür der Buchstabe steht: x ist die Anzahl der Stunden.',
               'Für jede Stunde kommen 3 € dazu. Bei x Stunden sind das 3 · x, also 3x Euro.',
               'Die Grundgebühr von 5 € kommt einmal dazu, egal wie lange: 3x + 5.',
               'Der Term für die Kosten in Euro ist ⟦3x + 5⟧. Probe mit 2 Stunden: 3 · 2 + 5 = 11 €.'],
  'regel': 'So stellst du einen Term auf: Lege fest, wofür die ⟦Variable⟧ steht (zum Beispiel x = Anzahl der Stunden). Beträge „pro Stück“ oder „pro Stunde“ werden ⟦mit x malgenommen⟧, feste Beträge werden ⟦dazugezählt⟧.',
  'fehler': 'Der Term 5x + 3 vertauscht die Rollen: Dann müsste man die 5 € Grundgebühr ⟦jede Stunde⟧ neu bezahlen und die 3 € nur einmal. Was pro Stunde anfällt, steht vor dem x.'},
 'muster': {
  'einstieg': 'Während es regnet, legt ein Kind am Fahrradverleih mit Streichhölzern Quadrate in eine Reihe: erst 1 Quadrat, dann 2, dann 3 nebeneinander. Es fragt sich: Wie viele Hölzer brauche ich für 10 Quadrate, ohne alles zu legen? Eine Reihe von Figuren, die nach einer festen Regel wächst, heißt ⟦Figurenfolge⟧.',
  'woerter': [['Figurenfolge', 'Figur 1, Figur 2, Figur 3 …, die nach einer festen Regel wächst'], ['n', 'die Nummer der Figur (1, 2, 3, …); wie x eine Variable'],
              ['Zunahme pro Schritt', 'so viele Hölzer kommen von einer Figur zur nächsten dazu']],
  'schritte': ['Zähle die Hölzer: Figur 1 hat 4, Figur 2 hat 7, Figur 3 hat 10. Von Figur zu Figur kommen 3 Hölzer dazu.',
               'Schau ins Bild: Ganz links steht 1 senkrechtes Holz. Jedes Quadrat bringt 3 neue Hölzer mit – oben, unten und rechts.',
               'Figur n hat n Quadrate. Sie braucht also 1 Holz plus 3 · n Hölzer: ⟦3n + 1⟧.',
               'Für 10 Quadrate setzt du n = 10 ein: 3 · 10 + 1 = 31 Hölzer.'],
  'regel': 'So beschreibst du eine ⟦Figurenfolge⟧ mit einem Term: Suche, ⟦wie viel pro Schritt dazukommt⟧ – diese Zahl steht vor dem n. Prüfe dann mit Figur 1, welche feste Zahl noch dazukommt.',
  'fehler': 'Der Term n + 3 passt nicht zu 4, 7, 10: Für n = 2 ergibt er 5 statt 7. Er tut so, als käme pro Quadrat nur ⟦1 Holz⟧ dazu. Die Zunahme pro Schritt (3) gehört vor das n.'},
 'deuten': {
  'einstieg': 'Der Handyvertrag der Chefin hat eine feste Monatsgebühr und kostet außerdem für jede Minute etwas. Auf der Rechnung steht nur ein Term: K = 0,1x + 8. Was bedeuten die 8 und die 0,1? Wer erklärt, wofür jede Zahl in einem Term steht, ⟦deutet⟧ den Term.',
  'woerter': [['deuten', 'erklären, was eine Zahl oder ein Buchstabe in der Situation bedeutet'], ['K', 'hier: die Kosten im Monat in Euro'], ['0,1', '0,10 €, also 10 Cent']],
  'schritte': ['Der Term ist K = 0,1x + 8. Dabei ist x die Anzahl der Minuten, K sind die Kosten in Euro.',
               'Die 0,1 steht vor dem x. Sie wird mit jeder Minute malgenommen: 0,10 € pro Minute.',
               'Die 8 kommt immer dazu, egal wie viel man telefoniert: 8 € Grundgebühr.',
               'Für 50 Minuten: K = 0,1 · 50 + 8 = 5 + 8 = ⟦13 €⟧.'],
  'regel': 'So ⟦deutest⟧ du einen Term: Die Zahl ⟦vor dem x⟧ ist der Betrag pro Einheit (pro Minute, pro Stunde), die Zahl ⟦ohne x⟧ ist der feste Betrag. Passt eine Deutung nicht zu allen Teilen, ist sie ⟦falsch⟧.',
  'fehler': 'In K = 0,1x + 8 ist 8 nicht der Preis pro Minute – sonst kosteten 50 Minuten schon 400 €. Was pro Minute zählt, steht ⟦vor dem x⟧.'},
}
for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl7.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl7 import mit_umbau  # noqa: E402

UMBAU = {
 'struktur': {
  'einstieg': 'Ein Leihrad kostet 2 € Gebühr plus 3 € für die Stunde, zusammen 5 €. Eine Familie leiht 5 Räder: 5 · (2 + 3) = 25 €. Welche Rechnung zuletzt kommt, bestimmt die ⟦Termart⟧.',
  'woerter': [['Term', 'eine Rechnung aus Zahlen, Buchstaben und Rechenzeichen'], ['Termart', 'Summe, Differenz, Produkt oder Quotient – je nach letzter Rechnung'],
              ['Produkt', 'zuletzt wird malgenommen']],
  'bild': {'typ': 'tabelle', 'kopf': ['', '5 · (x + 2)'], 'zeilen': [['zuerst', '?'], ['zuletzt', '?'], ['Termart', '?']]},
  'schritte': [{'text': 'Was in Klammern steht, rechnet man zuerst: x + 2.', 'bild': {'zeilen': [['zuerst', 'x + 2'], ['zuletzt', '?'], ['Termart', '?']]}},
               {'text': 'Danach kommt mal 5. Das ist die letzte Rechnung.', 'bild': {'zeilen': [['zuerst', 'x + 2'], ['zuletzt', '· 5'], ['Termart', '?']]}},
               {'text': 'Zuletzt wird malgenommen. Der Term ist ein ⟦Produkt⟧.', 'bild': {'zeilen': [['zuerst', 'x + 2'], ['zuletzt', '· 5'], ['Termart', 'Produkt']]}}],
  'fehler': '3x + 4 ist kein Produkt. Erst wird 3 · x gerechnet, ⟦zuletzt addiert⟧. Wie beim Verleih: Am Ende kommt die Gebühr dazu.',
  'fehler_bild': {'kopf': ['', '3x + 4'], 'zeilen': [['zuerst', '3 · x'], ['zuletzt', '+ 4'], ['Termart', 'Summe']]},
  'regel': 'Die ⟦letzte Rechnung⟧ bestimmt die Termart. Klammern zuerst, dann Punkt vor Strich.'},
 'termwert': {
  'einstieg': 'Der Fahrradverleih nimmt 3 € pro Stunde plus 5 € Gebühr. Als Term heißt das 3x + 5. Was kosten 1, 2 oder 4 Stunden? Das Ergebnis heißt ⟦Termwert⟧.',
  'woerter': [['Variable', 'ein Buchstabe wie x für eine Zahl, die sich ändern kann'], ['einsetzen', 'für x eine bestimmte Zahl hinschreiben'],
              ['Termwert', 'das Ergebnis nach dem Einsetzen']],
  'bild': {'typ': 'tabelle', 'kopf': ['Stunden x', '1', '2', '4'], 'zeilen': [['3x + 5 (in €)', '?', '?', '?']]},
  'schritte': [{'text': 'Für die Variable x die 1 einsetzen: 3 · 1 + 5 = 8.', 'bild': {'zeilen': [['3x + 5 (in €)', '8', '?', '?']]}},
               {'text': 'Für x = 2: 3 · 2 + 5 = 11.', 'bild': {'zeilen': [['3x + 5 (in €)', '8', '11', '?']]}},
               {'text': 'Für x = 4: 3 · 4 = 12, plus 5 ergibt den Termwert ⟦17⟧.', 'bild': {'zeilen': [['3x + 5 (in €)', '8', '11', '17']]}}],
  'fehler': '3 · 4 + 5 ist nicht 3 · 9 = 27. Erst malnehmen, dann die Gebühr ⟦dazuzählen⟧: 12 + 5 = 17 €.',
  'regel': 'Zahl für x ⟦einsetzen⟧ und ausrechnen. Negative Zahlen kommen in Klammern, Punkt vor Strich gilt.'},
 'uebersetzen': {
  'einstieg': 'Zwei Kinder leihen Räder. Jedes zahlt die Leihgebühr plus 5 € Pfand. Den Preis für beide schreibst du als Rechnung auf. Das heißt ⟦übersetzen⟧.',
  'woerter': [['Summe aus x und 5', 'x + 5'], ['das Doppelte', 'mal 2'], ['2(x + 5)', '2 · (x + 5): die ganze Klammer wird verdoppelt']],
  'bild': {'typ': 'tabelle', 'kopf': ['in Worten', 'in Zeichen'], 'zeilen': [['die Summe aus x und 5', '?'], ['das Doppelte davon', '?']]},
  'schritte': [{'text': 'Die Leihgebühr ist x. „Die Summe aus x und 5“ heißt x + 5.',
                'bild': {'zeilen': [['die Summe aus x und 5', 'x + 5'], ['das Doppelte davon', '?']]}},
               {'text': 'Das Doppelte gilt für die ganze Summe. Darum kommt sie in Klammern.'},
               {'text': 'Ergebnis: ⟦2(x + 5)⟧.', 'bild': {'zeilen': [['die Summe aus x und 5', 'x + 5'], ['das Doppelte davon', '2(x + 5)']]}}],
  'fehler': '2x + 5 ist falsch: Dann zahlt das zweite Kind kein Pfand. Gemeint ist die ganze Summe: 2(x + 5) = ⟦2x + 10⟧.',
  'fehler_bild': {'kopf': ['', 'Term'], 'zeilen': [['falsch', '2x + 5'], ['richtig', '2x + 10']]},
  'regel': 'Übersetze Wort für Wort in ⟦Rechenzeichen⟧. Was zuerst gerechnet wird, kommt in Klammern.'},
 'sachsituation': {
  'einstieg': 'Der Verleih will eine Preistafel: 5 € Grundgebühr und 3 € pro Stunde. Wie lange jemand fährt, ist noch offen. Dafür nimmt man einen Buchstaben und stellt einen ⟦Term⟧ auf.',
  'woerter': [['Grundgebühr', 'fester Betrag, der einmal anfällt'], ['pro Stunde', 'für jede Stunde einmal; wird mit x malgenommen']],
  'bild': {'typ': 'tabelle', 'kopf': ['Stunden', '1', '2', 'x'], 'zeilen': [['Preis in €', '?', '?', '?']]},
  'schritte': [{'text': 'x steht für die Anzahl der Stunden.'},
               {'text': 'Bei 1 Stunde: 3 · 1 + 5 = 8 €.', 'bild': {'zeilen': [['Preis in €', '8', '?', '?']]}},
               {'text': 'Bei 2 Stunden: 3 · 2 + 5 = 11 €.', 'bild': {'zeilen': [['Preis in €', '8', '11', '?']]}},
               {'text': 'Bei x Stunden: ⟦3x + 5⟧ Euro.', 'bild': {'zeilen': [['Preis in €', '8', '11', '3x + 5']]}}],
  'fehler': '5x + 3 vertauscht die Rollen. Dann kostet jede Stunde 5 € und die ⟦Grundgebühr⟧ nur 3 €. Was pro Stunde anfällt, steht vor dem x.',
  'regel': 'Was ⟦pro Stunde⟧ anfällt, wird mit x malgenommen. Feste Beträge zählst du dazu.'},
 'muster': {
  'einstieg': 'Bei Regen legt ein Kind Quadrate aus Streichhölzern in eine Reihe. Wie viele Hölzer braucht es für 10 Quadrate, ohne alles zu legen? So eine wachsende Reihe heißt ⟦Figurenfolge⟧.',
  'woerter': [['Figurenfolge', 'Figur 1, 2, 3 …, die nach einer festen Regel wächst'], ['n', 'die Nummer der Figur']],
  'bild': _bild_quadrate(3),
  'schritte': [{'text': 'Figur 1 ist ein Quadrat aus 4 Hölzern.', 'bild': _bild_quadrate(1)},
               {'text': 'Jedes neue Quadrat bringt 3 Hölzer mit. Figur 2 hat 7.', 'bild': _bild_quadrate(2)},
               {'text': 'Figur 3 hat 10: ganz links 1 Holz, dazu 3 pro Quadrat.', 'bild': _bild_quadrate(3)},
               {'text': 'Figur n braucht ⟦3n + 1⟧ Hölzer. Figur 10 braucht also 31.'}],
  'fehler': 'n + 3 passt nicht: Für Figur 2 ergibt es 5 statt 7. Pro Quadrat kommen ⟦3 Hölzer⟧ dazu, nicht 1.',
  'regel': 'Die ⟦Zunahme pro Figur⟧ steht vor dem n. Mit Figur 1 prüfst du die feste Zahl.'},
 'deuten': {
  'einstieg': 'Der Handyvertrag der Chefin hat eine feste Monatsgebühr und kostet pro Minute etwas. Auf der Rechnung steht nur: K = 0,1x + 8. Wofür jede Zahl steht, klärt man beim ⟦Deuten⟧.',
  'woerter': [['deuten', 'erklären, was jede Zahl in der Situation bedeutet'], ['K', 'die Kosten im Monat in Euro']],
  'bild': {'typ': 'tabelle', 'kopf': ['Teil', 'Bedeutung'], 'zeilen': [['0,1x', '?'], ['8', '?']]},
  'schritte': [{'text': 'x steht für die Minuten, K für die Kosten in Euro.'},
               {'text': '0,1 steht vor dem x: 10 Cent pro Minute.', 'bild': {'zeilen': [['0,1x', '10 ct pro Minute'], ['8', '?']]}},
               {'text': '8 steht ohne x: feste Grundgebühr von 8 €.', 'bild': {'zeilen': [['0,1x', '10 ct pro Minute'], ['8', '8 € im Monat']]}},
               {'text': '50 Minuten kosten 0,1 · 50 + 8 = ⟦13 €⟧.'}],
  'fehler': '8 ist nicht der Preis pro Minute – sonst kosteten 50 Minuten schon 400 €. Was pro Minute zählt, steht ⟦vor dem x⟧.',
  'regel': 'Die Zahl ⟦vor dem x⟧ zählt pro Einheit. Die Zahl ohne x ist der feste Betrag.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---------- Zehnte Runde (schwer-kl7): schwerere Übungen nach Prüfungsvorbild ----------
# Vorbilder (nur Typ und Niveau, eigene Zahlen und Einkleidung): Bayerischer Mathematik-Test 8 (ISB) 2019 B7 (Formel auswerten),
# 2021 A2 (Zahlenrätsel als Term) und A4 (Teilterme deuten), 2022 A3 / 2025 A5 (Tabellenkalkulation), 2023 A2 (Variable deuten),
# 2024 A1b und A7a (Term für einen Umfang); Jahrgangsstufentest Realschule 8 (2025, Nr. 14: gleichwertigen Term ankreuzen).
from _schwer_kl7 import Neu, anhaengen  # noqa: E402


def _tab(werte):
    return {'typ': 'tabelle', 'kopf': ['Figur n'] + [str(i + 1) for i in range(len(werte))], 'zeilen': [['Anzahl'] + [str(v) for v in werte]]}


def schwer():
    N = Neu(7028)
    P = 'pruefung'
    K = 'knobel'
    TT = 'Tippe den ganzen Term ein, z. B. 3x − 2.'
    # struktur
    N.A('struktur', 2, 'Welcher Term ist ein Produkt, dessen zweiter Faktor eine Summe ist?', '3 · (x + 4)', ['3 · x + 4', '(3 + x) · 4 − 1', '3 + (x · 4)'],
        'Bei 3 · (x + 4) wird zuletzt multipliziert (Produkt). Der zweite Faktor (x + 4) ist eine Summe.', 'Suche den Term, bei dem das Mal zuletzt gerechnet wird.')
    N.A('struktur', 2, 'Wie heißt der Term (x + 3) : 2 in Worten?', 'der Quotient aus der Summe von x und 3 und der Zahl 2',
        ['die Summe aus x und dem Quotienten von 3 und 2', 'das Produkt aus der Summe von x und 3 und der Zahl 2', 'die Summe aus x, 3 und 2'],
        'Zuletzt wird geteilt: ein Quotient. Der Dividend (x + 3) ist eine Summe, der Divisor ist 2.', 'Was wird zuletzt gerechnet?')
    N.A('struktur', 3, 'Welche Beschreibung passt zum Term 12 − 3 · (x + 1)?', 'eine Differenz, deren Subtrahend ein Produkt ist',
        ['ein Produkt, dessen zweiter Faktor eine Summe ist', 'eine Differenz, deren Subtrahend eine Summe ist', 'eine Summe, deren zweiter Summand ein Produkt ist'],
        'Zuletzt wird 12 minus etwas gerechnet: Differenz. Abgezogen wird 3 · (x + 1), also ein Produkt.', 'Erst die Termart (letzte Rechnung), dann den abgezogenen Teil ansehen.')
    N.A('struktur', 3, 'In einer Tabellenkalkulation steht in Zelle B1 die Formel =A1*(A2-3). Welche Termart hat die Formel?', 'Produkt',
        ['Differenz', 'Summe', 'Quotient'],
        'Die Klammer (A2 − 3) wird zuerst gerechnet, zuletzt wird A1 mit ihr multipliziert. Also ein Produkt, auch wenn ein Minus darin steht.',
        'Das Zeichen * bedeutet „mal“. Was wird zuletzt gerechnet?', art=P)
    N.A('struktur', 3, 'Mit der Formel =C2+C3/2 soll der Mittelwert der Zahlen in C2 und C3 berechnet werden. Was stimmt?', 'Falsch: Nur C3 wird halbiert. Richtig ist =(C2+C3)/2.',
        ['Richtig, denn man addiert und teilt durch 2.', 'Falsch: Richtig ist =C2/2+C3.', 'Falsch: Richtig ist =C2+C3*2.'],
        'Punkt vor Strich: Bei =C2+C3/2 wird zuerst C3 durch 2 geteilt. Für den Mittelwert muss die Summe in Klammern stehen: =(C2+C3)/2.',
        'Welche Rechnung macht die Tabelle zuerst?', art=P)
    N.Z('struktur', 3, 'Setze in 2 · 3 + 4 · 5 genau ein Klammerpaar so, dass das Ergebnis möglichst groß wird. Wie groß ist es?', 70, '2 * (3 + 4) * 5',
        'Möglich: (2 · 3 + 4) · 5 = 50, 2 · (3 + 4 · 5) = 46, 2 · (3 + 4) · 5 = 70. Am größten: 2 · (3 + 4) · 5 = 70.',
        'Probiere verschiedene Stellen für die Klammer. Was passiert, wenn die Summe zum Faktor wird?', art=K)
    # termwert
    N.Z('termwert', 2, 'Berechne den Wert von (2x − 1)² für x = −3.', 49, '(2 * (-3) - 1)**2',
        '2 · (−3) − 1 = −7. (−7)² = 49.', 'Zuerst die Klammer ausrechnen, dann quadrieren.')
    N.Z('termwert', 2, 'Berechne den Wert von 3a − b² für a = −2 und b = −4.', -22, '3 * (-2) - (-4)**2',
        '3 · (−2) = −6. (−4)² = 16. −6 − 16 = −22.', 'Achtung: b² = (−4)² ist positiv. Danach wird es abgezogen.')
    N.Z('termwert', 3, 'In einer Tabellenkalkulation steht in A1 die Zahl −2 und in A2 die Zahl 5. Welchen Wert zeigt die Zelle B1 mit der Formel =A2*(A1+4)-A1?', 12, '5 * ((-2) + 4) - (-2)',
        'A1 + 4 = −2 + 4 = 2. A2 · 2 = 10. 10 − A1 = 10 − (−2) = 12.', 'Setze die Zahlen ein. * heißt „mal“. Minus eine negative Zahl beachten.', art=P)
    N.Z('termwert', 3, 'Welche Zahl z muss man einsetzen, damit der Term 4x − z für x = 3 den Wert 5 hat?', 7, '4 * 3 - 5',
        'Für x = 3: 12 − z = 5. Also z = 12 − 5 = 7.', 'Setze x = 3 ein. Welche Zahl musst du von 12 abziehen, damit 5 bleibt?', art=P)
    N.Z('termwert', 3, 'Für welchen x-Wert lässt sich der Term (x + 2) : (x − 3) nicht berechnen?', 3, '3',
        'Durch 0 kann man nicht teilen. x − 3 = 0 gilt für x = 3.', 'Wann wird der Divisor null?')
    N.Z('termwert', 3, 'Setze für x die Zahlen 1, 2, 3, 4 und 5 in den Term x² − 6x + 10 ein. Welcher ist der kleinste Termwert?', 1, '3**2 - 6 * 3 + 10',
        'Werte: x = 1: 5, x = 2: 2, x = 3: 1, x = 4: 2, x = 5: 5. Der kleinste Wert ist 1 (bei x = 3).',
        'Lege eine Wertetabelle an. Achte darauf, wie die Werte erst fallen und dann steigen.', art=K)
    # uebersetzen
    N.L('uebersetzen', 2, 'Schreibe als Term: das Produkt aus der Summe von x und 2 und der Differenz aus x und 2.', '(x + □)(x − □)', [2, 2], ['2', '2'],
        'Summe von x und 2: (x + 2). Differenz aus x und 2: (x − 2). Produkt: (x + 2)(x − 2).', 'Beide Teile in eigene Klammern, dann malnehmen.', TT)
    N.L('uebersetzen', 2, 'Schreibe als Term: der Quotient aus x und 4, vermindert um 3.', 'x : □ − □', [4, 3], ['4', '3'],
        'Quotient aus x und 4: x : 4. Davon 3 abziehen: x : 4 − 3.', 'Erst den Quotienten bilden, dann vermindern.', 'Trage die beiden Zahlen ein.')
    N.Z('uebersetzen', 2, 'Zahlenrätsel: Denke dir eine Zahl. Addiere 3, nimm das Ergebnis mal 2 und subtrahiere dann das Doppelte der gedachten Zahl. Welches Ergebnis erhältst du für die Zahl 9?', 6, '(9 + 3) * 2 - 2 * 9',
        '9 + 3 = 12, 12 · 2 = 24, 24 − 18 = 6.', 'Gehe die Anweisungen der Reihe nach durch.', art=P)
    N.A('uebersetzen', 3, 'Zahlenrätsel: Denke dir eine Zahl n. Addiere 3, nimm das Ergebnis mal 2 und subtrahiere das Doppelte von n. Warum kommt für jede Zahl dasselbe heraus?',
        'Weil 2(n + 3) − 2n = 2n + 6 − 2n = 6 ist.', ['Weil 2 · 3 = 6 ist und n wegfällt, denn n ist immer 0.', 'Weil 2(n + 3) − 2n = n + 6 ist.', 'Das stimmt nicht, es hängt von n ab.'],
        'Als Term: 2(n + 3) − 2n. Ausmultiplizieren: 2n + 6 − 2n. Die 2n heben sich auf, es bleibt immer 6.', 'Stelle den Term auf und fasse zusammen.', art=P)
    N.A('uebersetzen', 3, 'Welcher Term ist gleichwertig zu: „das Doppelte der Differenz aus 4 und x, vermehrt um das Dreifache von x“?', '8 + x',
        ['8 − 5x', '8 + 2x', '5x + 8'],
        'Term: 2(4 − x) + 3x = 8 − 2x + 3x = 8 + x.', 'Erst den Term aufstellen, dann die Klammer auflösen und zusammenfassen.', art=P)
    N.A('uebersetzen', 3, 'Welcher Wortterm passt NICHT zum Term 2x + 6?', 'das Doppelte von x, vermehrt um 3',
        ['das Doppelte der Summe aus x und 3', 'die Summe aus dem Doppelten von x und 6', 'die Summe aus 6 und dem Produkt von 2 und x'],
        'Das Doppelte von x, vermehrt um 3, ist 2x + 3. Die anderen ergeben 2x + 6 – auch 2(x + 3) = 2x + 6.', 'Schreibe jeden Wortterm als Term und vereinfache.', art=K)
    N.Z('uebersetzen', 3, 'Multipliziere eine Zahl mit 5, subtrahiere 4 und teile das Ergebnis durch 2. Du erhältst 8. Mit welcher Zahl hast du begonnen?', 4, '(8 * 2 + 4) / 5',
        'Rückwärts: 8 · 2 = 16, 16 + 4 = 20, 20 : 5 = 4. Probe: (5 · 4 − 4) : 2 = 8.', 'Gehe die Schritte rückwärts und mach jeweils das Gegenteil.', art=K)
    # sachsituation
    N.L('sachsituation', 2, 'Ein Handyvertrag kostet 8 € im Monat, jede SMS 9 Cent. Gib den Term für die Monatskosten in CENT bei x SMS an.', '□x + □', [9, 800], ['9', '8 * 100'],
        '8 € = 800 Cent fest, dazu 9 Cent je SMS: 9x + 800.', 'Rechne zuerst alles in Cent um.', TT)
    N.Z('sachsituation', 2, 'Fahrradverleih A: 6 € pro Tag. Verleih B: 15 € Grundgebühr und 3 € pro Tag. Ab wie vielen ganzen Tagen ist B günstiger?', 6, '15 / 3 + 1',
        'Terme: A = 6x, B = 3x + 15. Bei 5 Tagen kosten beide 30 €. Ab 6 Tagen ist B günstiger (36 € > 33 €).', 'Berechne beide Terme für einige Tage.')
    N.L('sachsituation', 3, 'Ein Quadrat hat die Seitenlänge x cm. Ein Rechteck ist 3 cm länger und 2 cm schmaler als das Quadrat. Gib einen Term für den Umfang des Rechtecks (in cm) an und fasse zusammen.', '□x + □', [4, 2], ['4', '2 * 3 - 2 * 2'],
        'Länge x + 3, Breite x − 2. Umfang: 2(x + 3) + 2(x − 2) = 2x + 6 + 2x − 4 = 4x + 2.', 'Schreibe Länge und Breite als Term. Umfang = 2 · Länge + 2 · Breite.', TT, art=P)
    N.A('sachsituation', 3, 'Ein Konzert hat 300 Plätze, alle sind verkauft. Schüler zahlen 8 €, Erwachsene 12 €. Die Einnahmen in € beschreibt der Term 8x + 12 · (300 − x). Wofür steht x?',
        'für die Anzahl der verkauften Schülerkarten', ['für die Anzahl der verkauften Erwachsenenkarten', 'für den Preis einer Schülerkarte', 'für die Einnahmen'],
        'x wird mit 8 € multipliziert, also ist x die Anzahl der Schülerkarten. 300 − x sind dann die Erwachsenenkarten.', 'Womit wird x multipliziert?', art=P)
    N.Z('sachsituation', 3, 'Ein Konzert hat 300 Plätze, alle sind verkauft. Schüler zahlen 8 €, Erwachsene 12 €. Es wurden 120 Schülerkarten verkauft. Wie hoch sind die Einnahmen?', 3120, '8 * 120 + 12 * (300 - 120)',
        'Erwachsenenkarten: 300 − 120 = 180. Einnahmen: 8 · 120 + 12 · 180 = 960 + 2 160 = 3 120 €.', 'Wie viele Erwachsenenkarten sind es?', einheit='€', art=P)
    N.L('sachsituation', 3, 'Ein rechteckiger Garten ist x m lang und halb so breit. Rundherum führt außen ein 1 m breiter Weg. Gib einen Term für den äußeren Umfang des Weges (in m) an.', '□x + □', [3, 8], ['3', '8'],
        'Außen ist es x + 2 lang und x/2 + 2 breit. Umfang: 2(x + 2) + 2(x/2 + 2) = 2x + 4 + x + 4 = 3x + 8.',
        'Der Weg macht jede Seite um 2 m länger (1 m auf jeder Seite).', TT, art=K)
    # muster
    N.L('muster', 2, 'Plättchen in einer Figurenfolge: Figur 1: 4, Figur 2: 9, Figur 3: 14. Gib einen Term für die Anzahl bei Figur n an.', '□n + □', [5, -1], ['5', '4 - 5'],
        'Zunahme 5 pro Figur: 5n. Figur 1: 5 − 1 = 4. Term: 5n − 1.', 'Zunahme vor das n, dann mit Figur 1 die feste Zahl prüfen.', 'Tippe den ganzen Term ein, z. B. 3n − 2.', grafik=_tab([4, 9, 14]))
    N.Z('muster', 2, 'Eine Figurenfolge hat 4n + 4 Plättchen. Welche Figur hat genau 100 Plättchen?', 24, '(100 - 4) / 4',
        '4n + 4 = 100, also 4n = 96 und n = 24.', 'Setze den Term gleich 100 und rechne rückwärts.')
    N.Z('muster', 3, 'Die Anzahl der Diagonalen eines Vielecks mit n Ecken ist d = n · (n − 3) : 2. Wie viele Diagonalen hat ein Zehneck?', 35, '10 * (10 - 3) / 2',
        'n = 10: 10 · 7 : 2 = 35 Diagonalen.', 'Setze n = 10 ein.', art=P)
    N.Z('muster', 3, 'Die Anzahl der Diagonalen eines Vielecks mit n Ecken ist d = n · (n − 3) : 2. Ein Vieleck hat 20 Diagonalen. Wie viele Ecken hat es?', 8, '8',
        'Gesucht: n · (n − 3) = 40. Probieren: n = 8 gibt 8 · 5 = 40. Also 8 Ecken.', 'Rechne d · 2 und probiere passende Zahlen für n.', art=P)
    assert 8 * (8 - 3) // 2 == 20
    N.Z('muster', 3, 'Figur n ist ein Quadrat aus n · n Plättchen (Figur 1: 1, Figur 2: 4, Figur 3: 9). Wie viele Plättchen kommen dazu, wenn man von Figur 9 zu Figur 10 geht?', 19, '10**2 - 9**2',
        '10 · 10 − 9 · 9 = 100 − 81 = 19. Es kommen eine Reihe und eine Spalte dazu: 10 + 9 = 19.', 'Hier ist die Zunahme nicht immer gleich. Rechne beide Figuren aus.', art=K,
        grafik=_tab([1, 4, 9]))
    N.Z('muster', 3, 'Folge A hat 3n + 20 Plättchen, Folge B hat 5n + 4 Plättchen. Ab welcher Figur hat B mehr Plättchen als A?', 9, '(20 - 4) / (5 - 3) + 1',
        'Gleich viele bei 5n + 4 = 3n + 20, also 2n = 16, n = 8 (je 44). Ab Figur 9 hat B mehr (49 > 47).', 'Wo sind beide gleich? Danach überholt B.')
    # deuten
    N.Z('deuten', 2, 'Eine Kerze ist nach x Stunden h = 24 − 1,5x cm hoch. Nach wie vielen Stunden ist sie ganz abgebrannt?', 16, '24 / 1.5',
        'Abgebrannt heißt h = 0: 24 − 1,5x = 0, also 1,5x = 24 und x = 16 Stunden.', 'Welcher Wert gehört zu „ganz abgebrannt“?', einheit='Stunden')
    N.A('deuten', 2, 'Ein Tank enthält 500 Liter. Pro Minute fließen 12 Liter ab. Welcher Term gibt die Wassermenge in Litern nach x Minuten an?', '500 − 12x',
        ['12x − 500', '500 + 12x', '500 − 12'], 'Start 500 Liter, pro Minute 12 weniger: 500 − 12x.', 'Was ist fest, was ändert sich pro Minute?')
    N.A('deuten', 3, 'Ein Bilderrahmen ist außen 30 cm lang und 20 cm breit, die Rahmenleiste ist 2 cm breit. Wofür steht der Teilterm (30 − 4) · (20 − 4)?', 'für die Fläche des Bildes innerhalb der Leiste',
        ['für die Fläche der Rahmenleiste', 'für die Fläche des ganzen Rahmens', 'für den Umfang des Bildes'],
        'Auf beiden Seiten fehlen je 2 cm, also 4 cm pro Richtung: Innen ist es 26 cm × 16 cm. Das Produkt ist die Bildfläche.', 'Warum wird 4 abgezogen und nicht 2?', art=P)
    N.A('deuten', 3, 'Ein Bilderrahmen ist außen 30 cm lang und 20 cm breit, die Rahmenleiste ist 2 cm breit. Was berechnet der Term 30 · 20 − (30 − 4) · (20 − 4)?', 'die Fläche der Rahmenleiste',
        ['die Fläche des Bildes', 'den Umfang der Leiste', 'die Fläche des ganzen Rahmens mit Bild'],
        'Ganze Fläche minus Bildfläche innen = Fläche der Leiste: 600 − 416 = 184 cm².', 'Was bleibt übrig, wenn man das Innere vom Ganzen abzieht?', art=P)
    N.A('deuten', 3, 'Für die Fläche der Rahmenleiste (außen 30 cm × 20 cm, Leiste 2 cm breit) rechnet jemand 2 · 30 · 2 + 2 · 20 · 2. Warum ist das Ergebnis zu groß?',
        'Weil die vier Eckstücke doppelt gezählt werden.', ['Weil die Leiste nur 1 cm breit zählt.', 'Weil man den Umfang hätte nehmen müssen.', 'Es ist nicht zu groß, es stimmt genau.'],
        'Die langen Streifen (30 × 2) und die kurzen (20 × 2) überlappen sich in den vier Ecken (je 2 × 2). Darum ist 200 cm² um 4 · 4 = 16 cm² zu viel (richtig: 184 cm²).',
        'Stell dir die vier Streifen vor: Wo liegen sie übereinander?', art=P)
    N.A('deuten', 3, 'Mia sagt: „Die Terme x² und 2x sind gleichwertig, denn für x = 2 ergeben beide 4.“ Was stimmt?', 'Falsch: Ein Beispiel reicht nicht. Für x = 3 ergibt sich 9 und 6.',
        ['Richtig, denn ein Beispiel genügt.', 'Richtig, denn x² heißt x · 2.', 'Falsch: Für x = 2 ergibt x² den Wert 8.'],
        'Gleichwertig heißt: für jede Zahl gleich. Ein Gegenbeispiel genügt zum Widerlegen: x = 3 gibt 9 ≠ 6.', 'Probiere eine andere Zahl für x.', art=K)
    return N


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('terme.aufstellen', 13_7_2)
# a) lineare Zwei-Variablen-Terme sind leichter als die Stufe-2-Terme mit x² → Stufe 2
for _t in ['Berechne den Wert von 5a + 3b für a = 1 und b = −2.', 'Berechne den Wert von −a + 2b für a = −5 und b = 1.',
           'Berechne den Wert von −a + 5b für a = 6 und b = −6.']:
    BF.stufe('termwert', _t, 2)
# a) Stufe 2 gleich schwer wie Stufe 1 („(Klammer) : Zahl“)
BF.stufe('struktur', 'Welche Termart hat der Term (9y − 1) : 6?', 1)
BF.stufe('struktur', 'Welche Termart hat der Term (5y − 2) : 3?', 1)
BF.nicht_umgesetzt('sachsituation S3 „Kletterhalle … Bei wie vielen Besuchen kosten beide gleich viel?“', 'Lösung 8 richtig und durch Probieren mit dem Term lösbar; passt als Stufe 3.')
BF.nicht_umgesetzt('deuten S3 „Jemand übersetzt … in den Term … Stimmt das?“ prüft Übersetzen statt Deuten', 'Aufgaben richtig; Deuten von Teiltermen wurde in Runde 10 ergänzt. Die Karte bleibt unverändert.')

# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Klasse 7, siehe _durchsicht_kl7.py) ----
from _durchsicht_kl7 import Durchsicht, durchsicht_datei  # noqa: E402

DS = Durchsicht('terme.aufstellen', 19_7_1)
# termwert: Aufgaben nutzen Tabellenkalkulations-Formeln (LehrplanPLUS M7 1.1), die Karte zeigte sie nicht → ein Schritt dazu
DS.karte('termwert', 'Schritt zur Tabellenkalkulation ergänzt (Aufgaben nutzen Formeln wie =A2*(A1+4)-A1).',
         schritte=lambda alt: alt + [{'text': 'Tabellenprogramm: x steht in Zelle A1, der Term heißt =3*A1+5 (* heißt mal).'}])
# sachsituation: fünf Stufe-2-Aufgaben sind das Beispiel mit anderen Zahlen (Grundgebühr + Preis pro Einheit) → Stufe 1
for _t in ['Ein Kanuverleih verlangt 8 € Grundgebühr und 6 € pro Stunde. Gib den Term für die Kosten (in €) bei x Stunden an.',
           'Eine Taxifahrt kostet 4 € Grundpreis und 3 € je Kilometer. Gib den Term für den Fahrpreis (in €) bei x Kilometern an.',
           'Ein Streamingdienst kostet 10 € im Monat, jeder ausgeliehene Film zusätzlich 2 €. Gib den Term für die Monatskosten (in €) bei x Filmen an.',
           'Ein Streamingdienst kostet 12 € im Monat, jeder ausgeliehene Film zusätzlich 4 €. Gib den Term für die Monatskosten (in €) bei x Filmen an.',
           'Eine Taxifahrt kostet 6 € Grundpreis und 3 € je Kilometer. Gib den Term für den Fahrpreis (in €) bei x Kilometern an.']:
    DS.stufe('sachsituation', _t, 1)
# sachsituation: echte Stufe 2 (zwei Bezüge, Rabatt) ergänzen
DS.neu('sachsituation', 2, DS.L('Ein Heft kostet x €, ein Block 1 € mehr als ein Heft. Gib einen Term für den Preis von 3 Heften und 2 Blöcken an und fasse zusammen.',
                                '□x + □', [5, 2], ['5', '2'], '3x + 2(x + 1) = 3x + 2x + 2 = 5x + 2.',
                                'Schreib zuerst den Preis eines Blocks als Term: x + 1.'))
DS.neu('sachsituation', 2, DS.L('Der Eintritt kostet x € pro Person. Eine Gruppe aus 12 Personen bekommt 2 € Rabatt pro Person. Gib einen Term für den Gesamtpreis der Gruppe an.',
                                '□x + □', [12, -24], ['12', '-24'], 'Jede Person zahlt x − 2 €. Zusammen: 12(x − 2) = 12x − 24.',
                                'Was zahlt eine Person? Dann mal 12.'))
# deuten: zwei der vier Stufe-3-Aufgaben „Jemand übersetzt …“ prüfen Übersetzen (Karte uebersetzen), nicht Deuten → durch Deuten-Aufgaben ersetzen
DS.ersetze('deuten', 'Jemand übersetzt „die Differenz aus 8 und x“ in den Term x − 8. Stimmt das?',
           DS.A('Tarif A: K = 0,1x + 8. Tarif B: K = 0,2x + 3 (x = Minuten, K in €). Für x = 50 ergeben beide Terme 13. Was bedeutet das?',
                'Bei 50 Minuten kosten beide Tarife gleich viel, nämlich 13 €.',
                ['Beide Tarife kosten pro Minute 13 Cent.', 'Bei 13 Minuten kosten beide Tarife 50 €.', 'Tarif B ist ab 13 Minuten günstiger.'],
                '0,1 · 50 + 8 = 13 und 0,2 · 50 + 3 = 13: Bei 50 Minuten zahlt man in beiden Tarifen 13 €.',
                'Setze in Gedanken x = 50 in beide Terme ein. Wofür steht x, wofür K?'))
DS.ersetze('deuten', 'Jemand übersetzt „das Dreifache der Summe aus x und 5“ in den Term 3x + 5. Stimmt das?',
           DS.A('Eine Kerze ist nach x Stunden h = 20 − 2x cm hoch. Eine zweite Kerze ist am Anfang doppelt so hoch und brennt genauso schnell ab. Welcher Term passt zur zweiten Kerze?',
                '40 − 2x', ['40 − 4x', '20 − 4x', '2 · (20 − 2x)'],
                'Doppelt so hoch: Anfangshöhe 40 cm. Gleich schnell: weiter 2 cm pro Stunde. Also 40 − 2x. 2 · (20 − 2x) = 40 − 4x würde doppelt so schnell abbrennen.',
                'Welche Zahl im Term ist die Anfangshöhe, welche die Abnahme pro Stunde?'))
# ---- DURCHSICHT ENDE ----


# ---- STUFEN (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, siehe _stufen_kl7.py) ----
# Vorbilder (Typ und Niveau, eigene Zahlen): BMT8 (ISB) 2022 A2 / 2025 A2 (Terme im Sachzusammenhang, Tabellenkalkulation); Knobel nach der Art
# von Känguru der Mathematik (Klassenstufen 7/8) und Mathematik-Olympiade (Schulrunde): Klammern setzen, Zaubertricks, Gitter zählen.
from _stufen_kl7 import Stufen, stufen_datei  # noqa: E402

ST = Stufen('terme.aufstellen', 20_7_1)
_HT = 'Trage die Zahlen in die Lücken ein.'
# struktur
ST.leiter('struktur', 'Termart eines einfachen Terms an der letzten Rechnung erkennen.',
          'Punkt-vor-Strich-Fallen und Klammern beachten; zu einer Beschreibung den Term finden; Term in Worten.',
          'Verschachtelte Beschreibungen in Terme übersetzen, Tabellen-Formeln deuten, falsche Begründungen widerlegen, Klammern gezielt setzen.')
ST.regel('struktur', 1, 'Welche Termart hat der Term', 'direkt')
ST.regel('struktur', 2, 'Welche Termart hat der Term', 'mehrschritt')
ST.regel('struktur', 2, 'Welcher Term ist ein Produkt', 'umkehr')
ST.regel('struktur', 2, 'in Worten', 'darstellung')
ST.regel('struktur', 3, 'Welcher Term ist eine Differenz aus einer Zahl', 'rueckwaerts')
ST.regel('struktur', 3, 'Welcher Term ist ein Quotient, dessen Dividend', 'rueckwaerts')
ST.regel('struktur', 3, '(y² + ', 'verknuepfen')
ST.regel('struktur', 3, 'Welche Termart hat der Term', 'mehrschritt', neu_s=2)
ST.regel('struktur', 3, 'Welche Beschreibung passt', 'transfer')
ST.regel('struktur', 3, 'Tabellenkalkulation', 'transfer')
ST.regel('struktur', 3, 'Mittelwert', 'fehler')
ST.regel('struktur', 3, 'Klammerpaar', 'transfer')
ST.neu('struktur', 1, 'erkennen', ST.A('Welcher dieser Terme ist eine Summe?', '3x + 4', ['3 · (x + 4)', '(x + 4) : 3', '3x · 4'],
                                       'Bei 3x + 4 wird zuerst 3 · x gerechnet, zuletzt + 4: eine Summe. Die anderen enden mit mal oder geteilt.',
                                       'Welche Rechnung kommt in jedem Term zuletzt?'))
ST.neu('struktur', 3, 'begruenden', ST.A('Tom sagt: „Im Term 3 · x + 4 kommt ein Mal vor, also ist er ein Produkt.“ Was stimmt?',
                                         'Falsch: Zuletzt wird + 4 gerechnet, der Term ist eine Summe.',
                                         ['Richtig: Ein Mal-Zeichen macht den Term zum Produkt.', 'Falsch: Der Term ist eine Differenz.',
                                          'Richtig, aber nur, wenn x größer als 4 ist.'],
                                         'Die Termart richtet sich nach der letzten Rechnung, nicht danach, welche Zeichen vorkommen: 3 · x zuerst, dann + 4 → Summe.',
                                         'Entscheidend ist die Rechnung, die man zuletzt ausführt.'))
ST.knobel('struktur', ST.Z('Setze in 1 + 2 · 3 + 4 · 5 so viele Klammerpaare, wie du willst. Die Reihenfolge der Zahlen und Zeichen bleibt. Wie groß kann das Ergebnis höchstens werden?',
                           105, '(1 + 2) * (3 + 4) * 5',
                           'Ohne Klammern: 1 + 6 + 20 = 27. Malnehmen vergrößert mehr als Addieren. Deshalb sollen die Plus-Zeichen zuerst gerechnet werden: '
                           '(1 + 2) · (3 + 4) · 5 = 3 · 7 · 5 = 105. Andere Möglichkeiten bleiben kleiner, z. B. (1 + 2 · 3 + 4) · 5 = 55 oder ((1 + 2) · 3 + 4) · 5 = 65.',
                           'Welche Rechnung macht eine Zahl stärker größer: Plus oder Mal? Was sollte also zuerst passieren?'))
ST.knobel('struktur', ST.Z('Wie viele verschiedene Werte kann der Term 2 · 3 + 4 · 5 annehmen, wenn man beliebig Klammern setzt (Zahlen und Zeichen bleiben in dieser Reihenfolge)?',
                           4, '4',
                           'Klammern ändern nur etwas, wenn sie das Plus vor einem Mal rechnen lassen. Möglich sind: ohne Wirkung 6 + 20 = 26; (2 · 3 + 4) · 5 = 50; '
                           '2 · (3 + 4 · 5) = 46; 2 · (3 + 4) · 5 = 70. Jede andere Klammerung ergibt einen dieser Werte. Also 4 verschiedene Werte.',
                           'Klammern wirken nur, wenn sie ein Plus „schützen“. Wo kann das Plus mit hineingenommen werden?'))
# termwert
ST.leiter('termwert', 'Eine Zahl in einen einfachen Term einsetzen und ausrechnen.',
          'Terme mit Quadrat, zwei Variablen, negativen Zahlen; Wertetabelle ausfüllen; Sachsituation.',
          'Vom Termwert zurückrechnen, Parameter bestimmen, Fehler beim Einsetzen deuten, Aussagen über alle Zahlen prüfen, Tabellen-Formeln.')
ST.regel('termwert', 1, 'Berechne den Wert', 'direkt')
ST.regel('termwert', 2, 'Wertetabelle', 'darstellung')
ST.regel('termwert', 2, 'Berechne den Wert', 'mehrschritt')
ST.regel('termwert', 3, '(a · b) : (a + b)', 'verknuepfen')
ST.regel('termwert', 3, 'Tabellenkalkulation', 'transfer')
ST.regel('termwert', 3, 'Welche Zahl z', 'parameter')
ST.regel('termwert', 3, 'nicht berechnen', 'verknuepfen')
ST.regel('termwert', 3, 'kleinste Termwert', 'transfer')
ST.neu('termwert', 1, 'erkennen', ST.A('Welcher Term hat für x = 2 den Wert 7?', '3x + 1', ['2x + 1', 'x + 3', '4x − 2'],
                                       '3 · 2 + 1 = 7. Die anderen: 2 · 2 + 1 = 5, 2 + 3 = 5, 4 · 2 − 2 = 6.', 'Setze x = 2 in jeden Term ein.',
                                       pruef=lambda t: {'3x + 1': 7, '2x + 1': 5, 'x + 3': 5, '4x − 2': 6}[t] == 7))
ST.neu('termwert', 2, 'einkleidung', ST.Z('Eine Taxifahrt kostet 3,50 € Grundpreis und 2 € je Kilometer, also 2x + 3,5 Euro. Was kostet eine Fahrt über 7 km?', 17.5, '2 * 7 + 3.5',
                                          '2 · 7 + 3,5 = 14 + 3,5 = 17,50 €.', 'x steht für die Kilometer. Setze 7 ein.', einheit='€'))
ST.neu('termwert', 3, 'fehler', ST.A('Lea setzt x = −3 in x² + 2 ein und rechnet: −3² + 2 = −9 + 2 = −7. Was stimmt?', 'Falsch: (−3)² = 9, richtig ist 11.',
                                     ['Richtig gerechnet.', 'Falsch: Richtig ist −3 · 2 + 2 = −4.', 'Falsch: Richtig ist 9 − 2 = 7.'],
                                     'Für x wird die ganze Zahl −3 eingesetzt, also mit Klammer: (−3)² + 2 = 9 + 2 = 11. −3² bedeutet −(3²) = −9.',
                                     'Was passiert, wenn man die negative Zahl ohne Klammer einsetzt?'))
ST.neu('termwert', 3, 'rueckwaerts', ST.Z('Für eine Zahl x hat der Term 2x + 1 den Wert 9. Welchen Wert hat der Term 6x − 1 für dieselbe Zahl x?', 23, '6 * ((9 - 1) / 2) - 1',
                                          'Rückwärts: 2x + 1 = 9, also 2x = 9 − 1 = 8 und x = 8 : 2 = 4. Dann 6 · 4 − 1 = 23.', 'Finde zuerst x, dann setze es in den zweiten Term ein.'))
ST.neu('termwert', 3, 'begruenden', ST.A('Stimmt die Aussage: „Der Term x² ist für jede Zahl x größer als x“?', 'Nein: Für x = 0,5 ist x² = 0,25 kleiner als 0,5.',
                                         ['Ja: Quadrieren macht jede Zahl größer.', 'Nein: Nur für negative x ist x² kleiner.', 'Ja, außer für x = 0.'],
                                         'Ein Gegenbeispiel genügt: x = 0,5 ergibt 0,25 < 0,5 (auch x = 1 ergibt 1 = 1, also nicht größer). Für negative x ist x² dagegen größer als x.',
                                         'Probiere Zahlen zwischen 0 und 1.'))
ST.knobel('termwert', ST.Z('Für wie viele der Zahlen n = 1, 2, 3, …, 20 ist der Termwert von n² + n durch 4 teilbar?', 10, '20 / 2',
                           'n² + n heißt n · n + n: n-mal n und noch einmal n, zusammen (n + 1)-mal n. Das ist das Produkt der Nachbarzahlen n und n + 1. Durch 4 teilbar ist es, wenn eine der beiden durch 4 teilbar ist '
                           '(zwei Nachbarzahlen können nicht beide gerade sein). Das gilt für n = 3, 4, 7, 8, 11, 12, 15, 16, 19, 20 – also 10 Zahlen.',
                           'Wie oft kommt n in n · n + n vor? Was weißt du über zwei Nachbarzahlen?'))
ST.knobel('termwert', ST.Z('Ein Term hat die Form a · x + b. Für x = 1 hat er den Wert 5, für x = 2 den Wert 8. Welchen Wert hat er für x = 10?', 32, '3 * 10 + 2',
                           'Von x = 1 zu x = 2 wächst der Wert um 3, also ist a = 3 (jedes x mehr bringt a dazu). Dann 3 · 1 + b = 5, b = 2. Für x = 10: 3 · 10 + 2 = 32.',
                           'Was passiert mit dem Wert, wenn x um 1 wächst?'))
# uebersetzen
ST.leiter('uebersetzen', 'Einfache Wortterme („die Summe aus dem Vierfachen von x und 3“) direkt übersetzen.',
          'Differenzen in der richtigen Reihenfolge, „das Doppelte der Summe“ mit Klammer, Terme in Worten, Zahlenrätsel.',
          'Übersetzen und zusammenfassen, rückwärts zur gedachten Zahl, Rätsel begründen, falsche Übersetzungen finden, Parameter bestimmen.')
ST.regel('uebersetzen', 1, 'Schreibe als Term', 'direkt')
ST.regel('uebersetzen', 2, 're:Differenz aus \\d+ und dem', 'umkehr')
ST.regel('uebersetzen', 2, 'Schreibe als Term', 'mehrschritt')
ST.regel('uebersetzen', 2, 'Zahlenrätsel', 'einkleidung')
ST.regel('uebersetzen', 3, 'fasse zusammen', 'verknuepfen')
ST.regel('uebersetzen', 3, 'Welcher Wortterm passt zu', 'darstellung', neu_s=2)
ST.regel('uebersetzen', 3, 'Warum kommt für jede Zahl', 'begruenden')
ST.regel('uebersetzen', 3, 'gleichwertig', 'transfer')
ST.regel('uebersetzen', 3, 'passt NICHT', 'begruenden')
ST.regel('uebersetzen', 3, 'Mit welcher Zahl hast du begonnen', 'rueckwaerts')
ST.neu('uebersetzen', 1, 'erkennen', ST.A('Welcher Term gehört zu „das Dreifache von x“?', '3x', ['x + 3', 'x³', 'x : 3'],
                                          '„Das Dreifache“ heißt mal 3: 3 · x = 3x. x³ wäre x · x · x.', 'Dreifach heißt: dreimal so viel.'))
ST.neu('uebersetzen', 3, 'fehler', ST.A('Jemand übersetzt „die Hälfte der Summe aus x und 6“ als x + 6 : 2. Was stimmt?', 'Falsch: Die ganze Summe wird halbiert, richtig ist (x + 6) : 2.',
                                        ['Richtig übersetzt.', 'Falsch: Richtig ist x : 2 + 6.', 'Falsch: Richtig ist 2 · (x + 6).'],
                                        'Bei x + 6 : 2 wird wegen Punkt vor Strich nur die 6 halbiert. Gemeint ist die Summe, also Klammer: (x + 6) : 2.',
                                        'Was wird bei x + 6 : 2 zuerst gerechnet?'))
ST.neu('uebersetzen', 3, 'parameter', ST.Z('Für welche Zahl a ist „das a-Fache der Summe aus x und 2“ gleich dem Term 3x + 6?', 3, '6 / 2',
                                           'Setze für x eine Zahl ein, z. B. x = 0: Das a-Fache von 0 + 2 ist 2a, und 3 · 0 + 6 = 6. Also 2a = 6 und a = 3. Probe mit x = 1: 3 · (1 + 2) = 9 und 3 · 1 + 6 = 9 ✓.', 'Setze für x eine einfache Zahl ein und vergleiche beide Werte.'))
ST.knobel('uebersetzen', ST.Z('Zaubertrick: Denke dir eine Zahl, verdopple sie, addiere 10, halbiere das Ergebnis und ziehe die gedachte Zahl ab. Es kommt immer 5 heraus. '
                              'Welche Zahl muss statt 10 stehen, damit immer 7 herauskommt?', 14, '7 * 2',
                              'Mit der gedachten Zahl x und der Zahl z statt 10: Nach Verdoppeln und Addieren hat man 2x + z. Halbiert man das, wird jeder Teil halbiert: Aus 2x wird x, aus z wird die Hälfte von z. Zieht man x ab, bleibt nur die Hälfte von z. '
                              'Für 7 braucht man z = 14.',
                              'Schreibe den Trick als Term mit x und einer unbekannten Zahl statt 10. Was bleibt übrig?'))
ST.knobel('uebersetzen', ST.Z('Die Summe von drei aufeinanderfolgenden ganzen Zahlen (z. B. 4 + 5 + 6) ist immer durch eine bestimmte Zahl teilbar. Welche ist die größte Zahl, die jede solche Summe teilt?',
                              3, '3', 'Nimm von der größten der drei Zahlen 1 weg und gib es der kleinsten: Die Summe bleibt gleich, und jetzt stehen dreimal die mittlere Zahl da (4 + 5 + 6 = 5 + 5 + 5). Jede Summe ist also das Dreifache der mittleren Zahl und durch 3 teilbar. '
                              'Eine größere Zahl teilt nicht jede Summe: 1 + 2 + 3 = 6 und 2 + 3 + 4 = 9 haben als größten gemeinsamen Teiler 3.',
                              'Vergleiche die drei Zahlen mit der mittleren.'))
# sachsituation
ST.leiter('sachsituation', 'Grundgebühr plus Preis pro Einheit als Term aufschreiben.',
          'Situationen mit zwei Bezügen, Rabatt, Einheitenwechsel, Tabelle → Term, Vergleich zweier Angebote.',
          'Rest-Terme („der Rest“), Bedeutung von x deuten, Fehler im Ansatz finden, Grundgebühr rückwärts bestimmen, Kosten pro Person als Quotient.')
ST.regel('sachsituation', 1, 'Gib den Term', 'direkt')
ST.regel('sachsituation', 2, 'Rechteck', 'mehrschritt')
ST.regel('sachsituation', 2, 'CENT', 'mehrschritt')
ST.regel('sachsituation', 2, 'günstiger', 'umkehr')
ST.regel('sachsituation', 2, 'Heft', 'mehrschritt')
ST.regel('sachsituation', 2, 'Rabatt', 'einkleidung')
ST.regel('sachsituation', 3, 'Streamingdienst', 'einkleidung', neu_s=2)
ST.regel('sachsituation', 3, 'Ein Rechteck ist x cm breit', 'mehrschritt', neu_s=2)
ST.regel('sachsituation', 3, 'Getränke', 'transfer')
ST.regel('sachsituation', 3, 'Kletterhalle', 'verknuepfen')
ST.regel('sachsituation', 3, 'Quadrat', 'transfer')
ST.regel('sachsituation', 3, 'Wofür steht x', 'begruenden')
ST.regel('sachsituation', 3, 'Wie hoch sind die Einnahmen', 'einkleidung', neu_s=2)
ST.regel('sachsituation', 3, 'Garten', 'transfer')
ST.neu('sachsituation', 1, 'erkennen', ST.A('Im Kino kostet der Eintritt 8 € pro Person, dazu kommt einmal 3 € Buchungsgebühr. Welcher Term gibt den Preis für x Personen an?',
                                            '8x + 3', ['3x + 8', '11x', '8 + 3x'], 'Pro Person 8 € → 8x. Die Gebühr kommt einmal dazu: + 3.',
                                            'Was fällt pro Person an, was nur einmal?'))
ST.neu('sachsituation', 2, 'darstellung', ST.L('Ein Verleih hat diese Preistabelle: 1 Stunde 7 €, 2 Stunden 9 €, 3 Stunden 11 €. Gib den Term für x Stunden an.', '□x + □', [2, 5], ['9 - 7', '7 - 2'],
                                               'Jede Stunde mehr kostet 2 € mehr: 2x. Bei 1 Stunde 7 € → 2 · 1 + □ = 7, also + 5. Term: 2x + 5.',
                                               'Um wie viel steigt der Preis pro Stunde? Was bleibt bei 1 Stunde übrig?', 'Tippe den Term ein, z. B. 3x + 4.',
                                               grafik={'typ': 'tabelle', 'kopf': ['Stunden', '1', '2', '3'], 'zeilen': [['Preis (€)', '7', '9', '11']]}))
ST.neu('sachsituation', 3, 'fehler', ST.A('Ein Verleih verlangt 4 € Grundgebühr und 2,50 € je Stunde. Jemand schreibt den Term 4x + 2,5. Was stimmt?',
                                          'Falsch: Grundgebühr und Stundenpreis sind vertauscht, richtig ist 2,5x + 4.',
                                          ['Richtig: 4 € und 2,50 € kommen beide vor.', 'Falsch: Richtig ist 6,5x.', 'Falsch: Richtig ist 4 + 2,5 + x.'],
                                          'Was pro Stunde anfällt, steht vor dem x: 2,5x. Die Grundgebühr kommt einmal dazu: + 4. Probe: 2 Stunden kosten 9 €, mit 4x + 2,5 wären es 10,50 €.',
                                          'Was wird mit der Zahl der Stunden malgenommen?'))
ST.neu('sachsituation', 3, 'parameter', ST.Z('Ein Verleih verlangt eine Grundgebühr g € und 3 € je Stunde. Für 5 Stunden zahlt man 22 €. Wie hoch ist g?', 7, '22 - 3 * 5',
                                             '5 Stunden kosten 3 · 5 = 15 €. Der Rest von 22 € ist die Grundgebühr: 22 − 15 = 7 €.', 'Stelle den Term mit g auf und setze 5 Stunden ein.', einheit='€'))
ST.neu('sachsituation', 3, 'pruefung', ST.A('Eine Klasse fährt ins Museum. Der Bus kostet 300 € für alle, der Eintritt 6 € pro Kind. Welcher Term gibt die Kosten pro Kind an, wenn x Kinder mitfahren?',
                                            '(300 + 6x) : x', ['300 + 6x : x', '300 : x + 6x', '(300 + 6) : x'],
                                            'Gesamtkosten 300 + 6x, gerecht geteilt durch x Kinder: (300 + 6x) : x. Ohne Klammer würde nur 6x geteilt.',
                                            'Stelle zuerst die Gesamtkosten auf, dann teile.'))
ST.knobel('sachsituation', ST.Z('Kinokarten kosten einzeln 9 €, eine Fünferkarte (5 Besuche) kostet 40 €. Wie viel Euro kosten 13 Kinobesuche mindestens?',
                                107, '2 * 40 + 3 * 9',
                                'Eine Fünferkarte spart 5 € gegenüber 5 Einzelkarten. Möglichkeiten: 2 Fünferkarten + 3 einzeln = 80 + 27 = 107 €; 3 Fünferkarten = 120 € (zwei Besuche verfallen); '
                                '1 Fünferkarte + 8 einzeln = 112 €; 13 einzeln = 117 €. Am günstigsten: 107 €.',
                                'Vergleiche: Lohnt sich eine Fünferkarte auch, wenn du nicht alle 5 Besuche nutzt?', einheit='€'))
ST.knobel('sachsituation', ST.Z('Ein Taxi kostet 4 € Grundpreis und 2 € je Kilometer. Zwei Freunde fahren 6 km zusammen, dann steigt einer aus, der andere fährt noch 4 km weiter. '
                                'Den Grundpreis teilen sie halb-halb, die gemeinsamen Kilometer auch; die letzten 4 km zahlt der, der länger fährt. Wie viel zahlt er?', 16,
                                '4 / 2 + 6 * 2 / 2 + 4 * 2',
                                'Gesamtpreis: 4 + 10 · 2 = 24 €. Anteil des Längerfahrenden: halber Grundpreis 2 €, halbe gemeinsame Strecke 6 · 2 : 2 = 6 €, eigene Strecke 4 · 2 = 8 €. '
                                'Zusammen 16 € (der andere zahlt 8 €, zusammen 24 € ✓).',
                                'Teile die Rechnung in drei Teile: Grundpreis, gemeinsame Strecke, letzte Strecke.', einheit='€'))
# muster
ST.leiter('muster', 'Eine Figurenfolge um wenige Figuren fortsetzen.',
          'Den Term zur Folge aus Bild oder Tabelle aufstellen; mit dem Term große Figuren berechnen; Figur zu einer Anzahl finden.',
          'Term aus dem Aufbau begründen, rückwärts zur Figur, fremde Formeln (Diagonalen), quadratisches Wachstum, falsche Terme erkennen, Parameter.')
ST.regel('muster', 1, 'Wie viele sind es bei Figur', 'direkt')
ST.regel('muster', 2, 'Gib einen Term', 'darstellung')
ST.regel('muster', 2, 'Welche Figur hat genau', 'umkehr')
ST.regel('muster', 3, 'Welcher Term gibt die Anzahl', 'begruenden')
ST.regel('muster', 3, 'Wie viele sind es bei Figur', 'mehrschritt', neu_s=2)
ST.regel('muster', 3, 'Welche Figur braucht genau', 'rueckwaerts')
ST.regel('muster', 3, 'Wie viele Diagonalen hat ein Zehneck', 'transfer')
ST.regel('muster', 3, 'Wie viele Ecken hat es', 'rueckwaerts')
ST.regel('muster', 3, 'n · n Plättchen', 'verknuepfen')
ST.regel('muster', 3, 'Folge A', 'transfer')
ST.neu('muster', 1, 'erkennen', ST.Z('Eine Folge hat 5, 8, 11, 14 Plättchen. Wie viele Plättchen kommen von Figur zu Figur dazu?', 3, '8 - 5',
                                     'Von 5 auf 8, von 8 auf 11, von 11 auf 14: jedes Mal 3 mehr.', 'Vergleiche zwei Nachbarfiguren.'))
ST.neu('muster', 2, 'mehrschritt', ST.L('Für n Tische in einer Reihe braucht man 2n + 2 Stühle. Wie viele Stühle braucht man für 15 Tische, und wie viele Tische für 40 Stühle?',
                                        '15 Tische: □ Stühle; 40 Stühle: □ Tische', [32, 19], ['2 * 15 + 2', '(40 - 2) / 2'],
                                        '2 · 15 + 2 = 32 Stühle. Für 40 Stühle rückwärts: 40 − 2 = 38, 38 : 2 = 19 Tische. Probe: 2 · 19 + 2 = 40 ✓.',
                                        'Einmal einsetzen, einmal rückwärts denken.'))
ST.neu('muster', 3, 'fehler', ST.A('Eine Folge hat 5, 9, 13, 17 Plättchen. Jemand schreibt den Term n + 4. Was stimmt?', 'Falsch: Pro Figur kommen 4 dazu, richtig ist 4n + 1.',
                                   ['Richtig: Es kommen immer 4 dazu.', 'Falsch: Richtig ist 5n.', 'Falsch: Richtig ist 4n + 5.'],
                                   'Die Zunahme pro Figur (4) gehört vor das n: 4n. Probe mit Figur 1: 4 · 1 + 1 = 5 ✓. n + 4 ergäbe für Figur 2 nur 6.',
                                   'Setze n = 2 in den Term ein und vergleiche mit der Folge.'))
ST.neu('muster', 3, 'parameter', ST.Z('Eine Figurenfolge hat a · n + 2 Plättchen. Figur 5 hat 32 Plättchen. Wie groß ist a?', 6, '(32 - 2) / 5',
                                      'Rückwärts: 32 − 2 = 30 Plättchen sind a · 5, also a = 30 : 5 = 6. Probe: 6 · 5 + 2 = 32 ✓.', 'Setze n = 5 ein und denke rückwärts.'))
ST.knobel('muster', ST.Z('Aus Streichhölzern wird ein quadratisches Gitter aus 3 × 3 kleinen Quadraten gelegt (jede Kante ist ein Holz). Wie viele Streichhölzer braucht man?', 24, '2 * 3 * 4',
                         'Waagrechte Linien: 4 Reihen mit je 3 Hölzern = 12. Senkrechte Linien: 4 Spalten mit je 3 Hölzern = 12. Zusammen 24. '
                         '(Für n × n Quadrate allgemein 2 · n · (n + 1).)',
                         'Zähle nicht Quadrate, sondern Linien: Wie viele waagrechte und senkrechte Linien gibt es?'))
ST.knobel('muster', ST.Z('Um ein Quadrat aus n × n Plättchen wird ein Rahmen gelegt, der ein Plättchen breit ist. Wie viele Plättchen hat der Rahmen bei n = 10?', 44, '12 * 12 - 10 * 10',
                         'Mit Rahmen ist das Quadrat 12 × 12 = 144 Plättchen groß, das innere 10 × 10 = 100. Rahmen: 144 − 100 = 44. '
                         '(Oder: 4 Seiten mit je 10 Plättchen plus 4 Ecken = 44.)',
                         'Vergleiche das große Quadrat mit Rahmen mit dem inneren.'))
# deuten
ST.leiter('deuten', 'Sagen, wofür eine Zahl im Term steht (Grundgebühr, Preis pro Einheit).',
          'Eine Rechnung oder einen Termwert in der Situation deuten; vom Wert zurück zur Zeit; Term zu einer Situation wählen.',
          'Teilterme in Figuren deuten, Tarife vergleichen und deuten, Fehlschlüsse erkennen, einen Parameter aus einem Messwert bestimmen.')
ST.regel('deuten', 1, 'Was bedeutet die Zahl', 'erkennen')
ST.regel('deuten', 2, 'Was bedeutet die Rechnung', 'darstellung')
ST.regel('deuten', 2, 'Was bedeutet h =', 'umkehr')
ST.regel('deuten', 2, 'ganz abgebrannt', 'umkehr')
ST.regel('deuten', 2, 'Tank', 'einkleidung')
ST.regel('deuten', 3, 'doppelt so hoch', 'transfer')
ST.regel('deuten', 3, 'Tarif A', 'transfer')
ST.regel('deuten', 3, 'Jemand übersetzt', 'fehler')
ST.regel('deuten', 3, 'Wofür steht der Teilterm', 'begruenden')
ST.regel('deuten', 3, 'Was berechnet der Term', 'begruenden')
ST.regel('deuten', 3, 'Für die Fläche der Rahmenleiste', 'fehler')
ST.regel('deuten', 3, 'Mia', 'begruenden')
ST.neu('deuten', 1, 'direkt', ST.Z('Ein Parkhaus berechnet P = 2x + 3 (x = Stunden, P in €). Was kostet Parken für 4 Stunden?', 11, '2 * 4 + 3',
                                   '2 · 4 + 3 = 11 €.', 'Setze für x die Stunden ein.', einheit='€'))
ST.neu('deuten', 3, 'parameter', ST.Z('Ein Handytarif kostet K = 0,1x + g (x = Minuten, K in €). Bei 60 Minuten kostet er 14 €. Wie hoch ist die Grundgebühr g?', 8, '14 - 0.1 * 60',
                                      '60 Minuten kosten 0,1 · 60 = 6 €. Der Rest von 14 € ist die Grundgebühr: 14 − 6 = 8 €.', 'Setze 60 Minuten ein. Was bleibt für die Grundgebühr?', einheit='€'))
ST.knobel('deuten', ST.Z('Kerze A ist 30 cm hoch und brennt 2 cm pro Stunde ab, Kerze B ist 20 cm hoch und brennt 1 cm pro Stunde ab. Beide werden gleichzeitig angezündet. '
                         'Nach wie vielen Stunden sind beide gleich hoch?', 10, '(30 - 20) / (2 - 1)',
                         'Höhen: A = 30 − 2x, B = 20 − x. Am Anfang ist A 10 cm höher. Jede Stunde holt B 1 cm auf (A verliert 2, B nur 1). Nach 10 Stunden: A = 10 cm, B = 10 cm.',
                         'Um wie viel ist A am Anfang höher, und wie schnell schrumpft dieser Vorsprung?', einheit='Stunden'))
ST.knobel('deuten', ST.Z('Ein Rechteck hat den Umfang 30 cm. Ist eine Seite x cm lang, beschreibt x · (15 − x) den Flächeninhalt. Wie groß ist der Flächeninhalt höchstens, wenn x eine ganze Zahl ist?',
                         56, '7 * 8',
                         '15 − x ist die andere Seite (beide Seiten zusammen sind der halbe Umfang). Probieren: x = 5 → 50, x = 6 → 54, x = 7 → 56, x = 8 → 56, x = 9 → 54. '
                         'Am größten ist die Fläche, wenn die Seiten möglichst gleich lang sind: 7 · 8 = 56 cm².',
                         'Wofür steht 15 − x? Lege eine Tabelle für verschiedene x an.', einheit='cm²'))
# ---- STUFEN ENDE ----


if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Terme lesen', ['struktur', 'termwert']), ('Terme aufstellen', ['uebersetzen', 'sachsituation', 'muster']), ('Terme deuten', ['deuten'])],
         'Terme aus Texten, Sachsituationen und Mustern aufstellen, Termwerte berechnen, die Termart erkennen und Terme im Sachzusammenhang deuten.',
         ['Termart = zuletzt ausgeführte Rechnung.', 'Was zuerst gerechnet wird, kommt in Klammern.',
          'Pro Stück/Stunde/Figur → vor das x (bzw. n); fester Betrag → addieren.'],
         offen=['Lernkarte „muster“: Streichholzfolgen (Quadrate, Dreiecke, Sechsecke) sind gezeichnet. L-Form und Beet mit Randplatten als Kästchenbild (Beet grau). Tischreihe und neutrale Plättchenfolgen stehen weiter als Wertetabelle: Sitzplätze bräuchten Symbole, die die App nicht hat.',
                'Äquivalenzumformungen von Termen (Ausmultiplizieren, Zusammenfassen als eigenes Thema) sind nicht Teil dieses Themas; nur einfaches Zusammenfassen kommt in Stufe 3 vor.'])
    anhaengen(META['thema_schluessel'], schwer())
    befunde_datei(META['thema_schluessel'], BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
    durchsicht_datei(META['thema_schluessel'], DS)  # Neunzehnte Runde: zuletzt
    stufen_datei(META['thema_schluessel'], ST)  # Zwanzigste Runde: zuletzt
