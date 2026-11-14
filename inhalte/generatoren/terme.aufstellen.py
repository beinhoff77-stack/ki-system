#!/usr/bin/env python3
"""Thema terme.aufstellen – Terme aufstellen und deuten (Gymnasium Bayern, Klasse 7)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl7 import A, L, Z, baue, cz, einsetzen, eur, figur, kl, lin, zt  # noqa: E402

META = {'thema_schluessel': 'terme.aufstellen', 'thema_id': 28, 'block_id': 63, 'klasse': {'gym_by': 7, 'rs_by': 6}}
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
     'schritte': ['Hölzer: Figur 1: 4, Figur 2: 7, Figur 3: 10', 'Pro Figur +3: Term 3n + □. Für n = 1: 3 + □ = 4 → □ = 1', '⟦3n + 1⟧; Figur 10: 31 Hölzer'],
     'probe': 'n = 2: 3 · 2 + 1 = 7 ✓',
     'fehler': 'Der Term n + 3 passt nicht zu 4, 7, 10: Für n = 2 ergibt er 5. Die ⟦Zunahme pro Schritt⟧ (3) gehört vor das n.',
     'bild': figur({'_a0': [0, 0], '_a1': [1, 0], '_a2': [2, 0], '_a3': [3, 0], '_b0': [0, 1], '_b1': [1, 1], '_b2': [2, 1], '_b3': [3, 1]},
                   linien=[['_a0', '_a1'], ['_a1', '_a2'], ['_a2', '_a3'], ['_b0', '_b1'], ['_b1', '_b2'], ['_b2', '_b3'],
                           ['_a0', '_b0'], ['_a1', '_b1'], ['_a2', '_b2'], ['_a3', '_b3', 'Figur 3: 10 Hölzer']]),
     '_verbot': ['Figur 1: 4, Figur 2: 7, Figur 3: 10']},
    {'lernziel': 'deuten', 'titel': 'Terme deuten und prüfen',
     'regel': 'Einen Term ⟦deuten⟧ heißt: sagen, was jede Zahl und jede Variable in der Situation bedeutet. Passt eine Deutung nicht zu allen Teilen, ist sie ⟦falsch⟧.',
     'schritte': ['Handytarif: K = 0,1x + 8 (x = Minuten, K in €)', '8: feste Grundgebühr; 0,1: Preis pro Minute', 'Für 50 Minuten: K = ⟦13 €⟧'],
     'fehler': 'In K = 0,1x + 8 ist 8 nicht der Preis pro Minute. Was pro Minute zählt, steht ⟦vor dem x⟧.',
     '_verbot': ['K = 0,1x + 8']},
]

ARTEN = ['Summe', 'Differenz', 'Produkt', 'Quotient']


def nz(R, lo, hi): return R.choice([k for k in range(lo, hi + 1) if k])


def g_struktur(R, st):
    a, b = R.randint(2, 9), R.randint(1, 9)
    v = R.choice(['x', 'a', 'y'])
    art = R.choice(ARTEN)
    if st == 1:
        t = {'Summe': f'{a}{v} + {b}', 'Differenz': f'{a}{v} − {b}', 'Produkt': f'{a} · ({v} + {b})', 'Quotient': f'({v} + {b}) : {a}'}[art]
    elif st == 2:
        c = R.randint(2, 9)
        t = {'Summe': f'{a} · {v} + {b} · {c}', 'Differenz': f'({v} + {a}) − {b}{v}', 'Produkt': f'({v} − {a}) · ({v} + {b})', 'Quotient': f'{a}{v} : ({b} + {c})'}[art]
    else:
        c = R.randint(2, 9)
        t = {'Summe': f'{a} · ({v} − {b}) + {c}', 'Differenz': f'{v}² − {a} · {b}', 'Produkt': f'{c} · ({a}{v} − {b})', 'Quotient': f'({v}² + {a}) : ({v} − {b})'}[art]
    zuletzt = {'Summe': 'addiert', 'Differenz': 'subtrahiert', 'Produkt': 'multipliziert', 'Quotient': 'dividiert'}[art]
    return A(R, f'Welche Termart hat der Term {t}?', art, [x for x in ARTEN if x != art],
             f'Rechenreihenfolge: Klammern, dann Punkt vor Strich. Zuletzt wird {zuletzt} – also {"eine" if art in ("Summe", "Differenz") else "ein"} {art}.', 'Welche Rechnung würdest du ganz zum Schluss ausführen?')


def g_termwert(R, st):
    if st == 1:
        m, t = nz(R, -9, 9), R.randint(-12, 12); x = R.randint(-6, 8)
        T = lin(m, t)
        return Z(f'Berechne den Wert von {T} für x = {zt(x)}.', m * x + t, f'({m}) * ({x}) + ({t})', f'x = {zt(x)} einsetzen: {einsetzen(T, x)} = {zt(m * x + t)}.',
                 'Setze die Zahl für x ein. Negative Zahlen in Klammern.')
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
            return L(f'Schreibe als Term: das {ZAHLWORT[k]} der Summe aus x und {b}.', '□(□x + □)', [k, 1, b], [str(k), '1', str(b)],
                     f'Summe aus x und {b}: (x + {b}). Das {ZAHLWORT[k]}: {k}(x + {b}).', 'Was zuerst gerechnet wird, kommt in eine Klammer.', HW)
        return L(f'Schreibe als Term: das {ZAHLWORT[k]} der Differenz aus x und {b}.', '□(□x + □)', [k, 1, -b], [str(k), '1', str(-b)],
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
    art = R.choice({1: ['verleih', 'kino'], 2: ['verleih', 'kino', 'rechteck', 'alter'], 3: ['rechteck', 'alter', 'zwei', 'wert']}[st])
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
        d = R.randint(2, 9); k = R.choice([2, 3])
        return L(f'Ein Kind ist x Jahre alt. Seine Schwester ist {d} Jahre älter, der Vater ist {k}-mal so alt wie das Kind. Gib einen Term für das Alter aller drei zusammen an.', '□x + □',
                 [2 + k, d], [f'2 + {k}', str(d)], f'x + (x + {d}) + {k}x = {2 + k}x + {d}.', 'Schreibe jedes Alter mit x auf und addiere.', HW)
    if art == 'zwei':
        p1, p2 = R.choice([(2, 3), (3, 5), (4, 6), (5, 8)])
        n = R.randint(10, 30)
        return L(f'Für ein Fest werden {n} Getränke gekauft: x Flaschen Saft zu {p2} € und der Rest Wasser zu {p1} €. Gib einen Term für den Gesamtpreis (in €) an und fasse zusammen.', '□x + □',
                 [p2 - p1, p1 * n], [f'{p2} - {p1}', f'{p1} * {n}'], f'Wasser: {n} − x Flaschen. {p2}x + {p1}({n} − x) = {lin(p2 - p1, p1 * n)}.',
                 'Wie viele Wasserflaschen sind es, wenn es x Saftflaschen sind?', HW)
    g, p = Fr(R.choice([3, 4, 5])), Fr(R.choice([5, 8, 10, 12, 15]), 100)
    x = R.choice([20, 40, 50, 60, 100, 120])
    return Z(f'Ein Handytarif kostet {eur(g)} € im Monat plus {eur(p)} € pro SMS. Stelle einen Term auf und berechne die Kosten für x = {x} SMS.', g + p * x,
             f'{cz(g)} + {cz(p)} * {x}', f'Term: {zt(p)}x + {zt(g)}. Für x = {x}: {zt(p)} · {x} + {zt(g)} = {eur(g + p * x)} €.', 'Grundgebühr + Preis pro SMS · Anzahl.', '€')


MUSTER = [
    ('Streichhölzer für Quadrate in einer Reihe', 3, 1), ('Streichhölzer für Dreiecke in einer Reihe', 2, 1), ('Sitzplätze an einer Reihe zusammengeschobener Tische', 2, 2),
    ('Plättchen in einer L-Form', 2, -1), ('Punkte in einer Treppe aus Rahmen', 4, 0), ('Plättchen in einer T-Form', 3, -1), ('Bausteine in einem Turm mit Sockel', 2, 3),
    ('Streichhölzer für Sechsecke in einer Reihe', 5, 1), ('Kreise in einer Kette mit Endkappen', 3, 2), ('Kacheln um ein Beet herum', 2, 6),
]


def g_muster(R, st):
    a = _g_muster(R, st)
    import re
    w = re.findall(r'Figur (\d+): (\d+)', a['f']['text'])
    if w:
        a['f']['grafik'] = {'typ': 'tabelle', 'kopf': ['Figur n'] + [n for n, _ in w], 'zeilen': [['Anzahl'] + [v for _, v in w]]}
    return a


def _g_muster(R, st):
    name, m, t = R.choice(MUSTER)
    if R.random() < .5:
        name, m, t = R.choice(['Plättchen in einem Muster', 'Perlen an einer Kette', 'Steine in einer Mauerreihe', 'Stühle in einem Saal']), R.randint(2, 7), R.randint(-1, 6)
    werte = [m * n + t for n in (1, 2, 3)]
    folge = ', '.join(f'Figur {n}: {v}' for n, v in zip((1, 2, 3), werte))
    if st == 1:
        k = R.randint(4, 8)
        return Z(f'{name}: {folge}. Wie viele sind es bei Figur {k}?', m * k + t, f'{m} * {k} + ({t})',
                 f'Pro Figur kommen {m} dazu: Figur {k}: {werte[2]} + {m} · {k - 3} = {m * k + t}.', 'Wie viele kommen von Figur zu Figur dazu?')
    if st == 2:
        return L(f'{name}: {folge}. Gib einen Term für die Anzahl bei Figur n an.', '□n + □', [m, t], [str(m), str(t)],
                 f'Pro Figur +{m}: {m}n. Für n = 1 muss {werte[0]} herauskommen: {m} + □ = {werte[0]} → □ = {zt(t)}. Term: {lin(m, t, "n")}.', 'Zunahme pro Schritt vor das n, dann für n = 1 anpassen.',
                 'Tippe den Term mit n ein, z. B. 3n + 1.')
    if R.random() < .5:
        k = R.randint(20, 100)
        return Z(f'{name}: {folge}. Wie viele sind es bei Figur {k}?', m * k + t, f'{m} * {k} + ({t})',
                 f'Term {lin(m, t, "n")}. Für n = {k}: {m} · {k} {"+" if t >= 0 else "−"} {abs(t)} = {m * k + t}.', 'Stelle erst einen Term auf, dann setze n ein.')
    k = R.randint(10, 60)
    N = m * k + t
    return Z(f'{name}: {folge}. Welche Figur braucht genau {N}?', k, f'({N} - ({t})) / {m}',
             f'{lin(m, t, "n")} = {N} → {m}n = {N - t} → n = {k}.', 'Stelle den Term auf und setze ihn gleich der Anzahl.')


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
        k = R.choice([j for j in (3, 4, 5, 6, 8, 10) if p * j + g >= 0])
        return Z(f'{T} ({x}). Berechne {T[0]} für x = {k}.', p * k + g, f'{cz(p)} * {k} + {cz(g)}', f'x = {k} einsetzen: {T[0]} = {zt(p)} · {k} + {zt(g)} = {zt(p * k + g)}.',
                 'Setze x ein.')
    # Stufe 3: Fehler finden in einem Term
    k, b = R.randint(2, 6), R.randint(2, 9)
    fall = R.choice(['klammer', 'reihenfolge', 'richtig'])
    if fall == 'klammer':
        satz, term = f'das {ZAHLWORT.get(k, str(k) + "-fache")} der Summe aus x und {b}', f'{k}x + {b}'
        r = f'Falsch: Die Summe muss in Klammern stehen, richtig ist {k}(x + {b}).'
    elif fall == 'reihenfolge':
        satz, term = f'die Differenz aus {b} und x', f'x − {b}'
        r = f'Falsch: Bei „Differenz aus {b} und x“ steht {b} vorne, richtig ist {b} − x.'
    else:
        satz, term = f'das {ZAHLWORT.get(k, str(k) + "-fache")} von x, vermehrt um {b}', f'{k}x + {b}'
        r = 'Richtig übersetzt.'
    alle = [f'Falsch: Die Summe muss in Klammern stehen, richtig ist {k}(x + {b}).', f'Falsch: Bei „Differenz aus {b} und x“ steht {b} vorne, richtig ist {b} − x.',
            'Richtig übersetzt.', f'Falsch: richtig wäre {k + b}x.']
    return A(R, f'Jemand übersetzt „{satz}“ in den Term {term}. Stimmt das?', r, [s for s in alle if s != r], r,
             'Übersetze selbst und vergleiche – achte auf Klammern und Reihenfolge.')


GEN = {'struktur': g_struktur, 'termwert': g_termwert, 'uebersetzen': g_uebersetzen, 'sachsituation': g_sachsituation, 'muster': g_muster, 'deuten': g_deuten}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Terme lesen', ['struktur', 'termwert']), ('Terme aufstellen', ['uebersetzen', 'sachsituation', 'muster']), ('Terme deuten', ['deuten'])],
         'Terme aus Texten, Sachsituationen und Mustern aufstellen, Termwerte berechnen, die Termart erkennen und Terme im Sachzusammenhang deuten.',
         ['Termart = zuletzt ausgeführte Rechnung.', 'Was zuerst gerechnet wird, kommt in Klammern.',
          'Pro Stück/Stunde/Figur → vor das x (bzw. n); fester Betrag → addieren.'],
         offen=['Lernkarte „muster“: Die Erklärung zeigt die Streichholzfigur 3 als Zeichnung, die Aufgaben zeigen die Anzahlen als Tabelle. Zeichnungen aller Figurenfolgen je Aufgabe wären möglich, sind aber aufwendig; bei Bedarf nachziehen.',
                'Äquivalenzumformungen von Termen (Ausmultiplizieren, Zusammenfassen als eigenes Thema) sind nicht Teil dieses Themas; nur einfaches Zusammenfassen kommt in Stufe 3 vor.'])
