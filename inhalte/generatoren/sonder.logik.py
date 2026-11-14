#!/usr/bin/env python3
"""Thema sonder.logik – Aussagenlogik (ohne Lehrplan-Zuordnung, Niveau Klasse 9/10)."""
import itertools
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403

start(8410)

PRIM = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
W, F = 'wahr', 'falsch'
HZ = 'je Zeile 1 (wahr) oder 0 (falsch)'


def zahlaussage():
    """Zufällige mathematische Aussage mit Wahrheitswert."""
    n = R.randint(2, 50)
    k = R.choice([2, 3, 4, 5, 6, 7, 9])
    art = R.choice(['prim', 'teilbar', 'gerade', 'quadrat', 'groesser', 'gleichung'])
    if art == 'prim': return f'{n} ist eine Primzahl', n in PRIM
    if art == 'teilbar': return f'{n} ist durch {k} teilbar', n % k == 0
    if art == 'gerade': return f'{n} ist gerade', n % 2 == 0
    if art == 'quadrat':
        m = R.randint(2, 9)
        e = m * m + R.choice([0, 0, 1, -1, 2])
        return f'{m}² = {e}', m * m == e
    if art == 'groesser':
        a, b = R.randint(-9, 9), R.randint(-9, 9)
        if a == b: b += 1
        return f'{dz(a)} < {dz(b)}', a < b
    a, b = R.randint(2, 12), R.randint(2, 12)
    c = a * b + R.choice([0, 0, 1, -2])
    return f'{a} · {b} = {c}', a * b == c


def wf(b):
    return W if b else F


def ausdr(name):
    """Ausdrücke für Wahrheitstafeln: (Text, Funktion)."""
    return {
        'p ∧ q': lambda p, q: p and q, 'p ∨ q': lambda p, q: p or q, '¬p': lambda p, q: not p,
        'p ∧ ¬q': lambda p, q: p and not q, '¬p ∨ q': lambda p, q: (not p) or q, '¬(p ∧ q)': lambda p, q: not (p and q),
        '¬(p ∨ q)': lambda p, q: not (p or q), 'p ⇒ q': lambda p, q: (not p) or q, '¬p ∧ ¬q': lambda p, q: (not p) and (not q),
        'q ⇒ p': lambda p, q: (not q) or p, '¬p ∨ ¬q': lambda p, q: (not p) or (not q), '¬q ⇒ ¬p': lambda p, q: q or not p,
    }[name]


ZEILEN = [(True, True), (True, False), (False, True), (False, False)]


def tafel_bild(spalten, frage):
    kopf = ['p', 'q'] + spalten + [frage]
    z = []
    for p, q in ZEILEN:
        z.append(['w' if p else 'f', 'w' if q else 'f'] + ['w' if ausdr(sp)(p, q) else 'f' for sp in spalten] + ['?'])
    return {'typ': 'tabelle', 'kopf': kopf, 'zeilen': z}


ETAPPEN = [
    {'lernziel': 'aussagen', 'titel': 'Was ist eine Aussage?',
     'regel': 'Eine ⟦Aussage⟧ (proposition) ist ein Satz, der ⟦entweder wahr oder falsch⟧ ist – nie beides, nie keins. Fragen, Befehle und Sätze mit unbestimmter Variable („x ist größer als 3“) sind ⟦keine Aussagen⟧. Man kürzt Aussagen mit Buchstaben p, q, … ab.',
     'schritte': ['„17 ist eine Primzahl.“ – wahr oder falsch? Wahr.', 'Also ist es eine Aussage mit ⟦Wahrheitswert wahr⟧ (truth value).'],
     'probe': '17 hat nur die Teiler 1 und 17 ✓',
     'fehler': '„Eine falsche Aussage ist keine Aussage“ stimmt nicht: „12 ist ungerade“ ist eine Aussage – ⟦eine falsche⟧. Entscheidend ist nur, dass sie wahr oder falsch ⟦sein kann⟧.'},
    {'lernziel': 'negation', 'titel': 'Aussagen verneinen',
     'regel': 'Die ⟦Verneinung⟧ (negation) ⟦¬p⟧ („nicht p“) ist genau dann wahr, wenn p falsch ist. Achtung bei Mengenwörtern: Die Verneinung von „⟦alle⟧ … sind …“ ist „⟦mindestens einer⟧ … ist ⟦nicht⟧ …“, die von „es gibt ein …“ ist „⟦kein⟧ …“.',
     'schritte': ['p: „Alle Kinder der Klasse haben ein Fahrrad.“', '¬p: „⟦Mindestens ein Kind der Klasse hat kein Fahrrad.⟧“'],
     'probe': 'Genau eine der beiden Aussagen ist wahr ✓',
     'fehler': '„Kein Kind hat ein Fahrrad“ als Verneinung von „Alle Kinder haben ein Fahrrad“ ist falsch: Beide können ⟦gleichzeitig falsch⟧ sein (wenn manche ein Fahrrad haben). Die Verneinung muss ⟦immer das Gegenteil⟧ liefern.'},
    {'lernziel': 'verknuepfen', 'titel': 'Und und Oder',
     'regel': '⟦p ∧ q⟧ („p und q“, conjunction) ist nur wahr, wenn ⟦beide⟧ wahr sind. ⟦p ∨ q⟧ („p oder q“, disjunction) ist wahr, wenn ⟦mindestens eine⟧ wahr ist – auch wenn beide wahr sind (einschließendes Oder).',
     'schritte': ['p: „9 ist gerade“ (falsch), q: „9 ist durch 3 teilbar“ (wahr).', 'p ∧ q: falsch, weil p falsch ist.', 'p ∨ q: ⟦wahr⟧, weil q wahr ist.'],
     'probe': 'Für ∨ reicht eine wahre Teilaussage ✓',
     'bild': {'typ': 'tabelle', 'kopf': ['p', 'q', 'p ∧ q', 'p ∨ q'], 'zeilen': [['w', 'w', 'w', 'w'], ['w', 'f', 'f', 'w'], ['f', 'w', 'f', 'w'], ['f', 'f', 'f', 'f']]},
     'fehler': '„p ∨ q ist falsch, weil p und q beide wahr sind“ ist falsch: Das mathematische ⟦Oder schließt beides ein⟧. Nur wenn beide falsch sind, ist p ∨ q falsch.'},
    {'lernziel': 'tafel', 'titel': 'Wahrheitstafeln ausfüllen',
     'regel': 'Eine ⟦Wahrheitstafel⟧ (truth table) listet ⟦alle Kombinationen⟧ der Wahrheitswerte auf: bei zwei Aussagen ⟦4 Zeilen⟧ (ww, wf, fw, ff). Zusammengesetzte Ausdrücke rechnet man ⟦von innen nach außen⟧, mit Hilfsspalten.',
     'schritte': ['Ausdruck p ∧ ¬q. Hilfsspalte ¬q: f, w, f, w.', 'p ∧ ¬q: nur in Zeile 2 (p wahr, ¬q wahr) wahr.', 'Ergebnis-Spalte: ⟦f, w, f, f⟧.'],
     'probe': 'Nur bei p wahr und q falsch ist „p und nicht q“ erfüllt ✓',
     'bild': {'typ': 'tabelle', 'kopf': ['p', 'q', '¬q', 'p ∧ ¬q'], 'zeilen': [['w', 'w', 'f', 'f'], ['w', 'f', 'w', 'w'], ['f', 'w', 'f', 'f'], ['f', 'f', 'w', 'f']]},
     'fehler': '¬(p ∧ q) mit ¬p ∧ ¬q gleichzusetzen ist falsch: In Zeile 2 (p w, q f) ist ¬(p ∧ q) wahr, ¬p ∧ ¬q aber falsch. Richtig ist ⟦¬(p ∧ q) = ¬p ∨ ¬q⟧ (De Morgan).'},
    {'lernziel': 'folgerung', 'titel': 'Wenn …, dann …',
     'regel': 'Die ⟦Implikation⟧ (implication) ⟦p ⇒ q⟧ („wenn p, dann q“) ist ⟦nur falsch⟧, wenn p wahr und q falsch ist. Aus p ⇒ q folgt die ⟦Kontraposition⟧ ¬q ⇒ ¬p (gleichwertig), aber ⟦nicht⟧ die ⟦Umkehrung⟧ q ⇒ p (converse).',
     'schritte': ['„Wenn eine Zahl durch 4 teilbar ist, dann ist sie gerade.“ (wahr)', 'Umkehrung: „Wenn gerade, dann durch 4 teilbar.“ – falsch (Gegenbeispiel 6).', 'Kontraposition: „⟦Wenn nicht gerade, dann nicht durch 4 teilbar⟧.“ – wahr.'],
     'probe': '6 ist gerade, aber 6 : 4 geht nicht auf ✓',
     'bild': {'typ': 'tabelle', 'kopf': ['p', 'q', 'p ⇒ q'], 'zeilen': [['w', 'w', 'w'], ['w', 'f', 'f'], ['f', 'w', 'w'], ['f', 'f', 'w']]},
     'fehler': 'Aus „Wenn es regnet, ist die Straße nass“ zu schließen „Die Straße ist nass, also regnet es“ ist falsch: Das ist die ⟦Umkehrung⟧ – die Straße kann auch aus anderen Gründen nass sein.'},
]


KEINE = ['Ist 7 eine Primzahl?', 'Rechne 5 + 3 aus!', 'x ist größer als 3.', 'Mathe ist das schönste Fach.', 'Schließ bitte das Fenster.', 'Wie spät ist es?', 'n ist eine gerade Zahl.']


def g_aussagen(s):
    art = R.choice({1: ['wert', 'wert', 'ist_aussage'], 2: ['wert', 'ist_aussage', 'keine'], 3: ['keine', 'variable', 'wert']}[s])
    if art == 'wert':
        t, b = zahlaussage()
        return auswahl(f'Welchen Wahrheitswert hat die Aussage „{t}“?', wf(b), [W, F, 'keinen – das ist keine Aussage'],
                       f'„{t}“ ist {wf(b)}.', 'Rechne oder prüfe die Behauptung nach.')
    if art == 'ist_aussage':
        t, b = zahlaussage()
        return auswahl(f'Ist „{t}.“ eine Aussage?', 'Ja, sie ist ' + wf(b) + '.', ['Ja, sie ist wahr.', 'Ja, sie ist falsch.', 'Nein, das ist keine Aussage.'],
                       f'Der Satz ist eindeutig wahr oder falsch – hier {wf(b)}. Also eine Aussage.', 'Kann man eindeutig sagen, ob der Satz stimmt?')
    if art == 'keine':
        k = R.choice(KEINE)
        t, _ = zahlaussage()
        return auswahl('Welcher Satz ist KEINE Aussage im Sinne der Logik?', f'„{k}“', [f'„{t}.“', '„Berlin liegt in Frankreich.“', '„Ein Quadrat hat vier Ecken.“'],
                       f'„{k}“ ist eine Frage, ein Befehl, eine Meinung oder enthält eine unbestimmte Variable – man kann nicht eindeutig wahr oder falsch sagen. Die anderen Sätze sind wahr oder falsch.',
                       'Eine Aussage muss eindeutig wahr oder falsch sein – auch „falsch“ zählt.')
    x = R.randint(1, 9)
    r = f'Erst wenn man für x eine Zahl einsetzt, z. B. x = {x}: Dann ist es {"wahr" if x > 3 else "falsch"}.'
    return auswahl('„x ist größer als 3.“ Wann wird daraus eine Aussage?', r, ['Es ist schon eine Aussage, sie ist wahr.', 'Nie – Sätze mit Buchstaben sind nie Aussagen.', 'Wenn man ein Fragezeichen anhängt.'],
                   f'Mit unbestimmter Variable ist der Satz eine Aussageform. Für x = {x} ist „{x} > 3“ {"wahr" if x > 3 else "falsch"}.', 'Kann man ohne Wert für x sagen, ob der Satz stimmt?')


NEG = [  # (Aussage, richtige Verneinung, typische falsche)
    ('Alle Schüler der Klasse sind älter als 12.', 'Mindestens ein Schüler der Klasse ist nicht älter als 12.', ['Kein Schüler der Klasse ist älter als 12.', 'Alle Schüler der Klasse sind jünger als 12.']),
    ('Es gibt eine gerade Primzahl.', 'Es gibt keine gerade Primzahl.', ['Es gibt eine ungerade Primzahl.', 'Alle Primzahlen sind gerade.']),
    ('Jede Quadratzahl ist positiv.', 'Mindestens eine Quadratzahl ist nicht positiv.', ['Keine Quadratzahl ist positiv.', 'Jede Quadratzahl ist negativ.']),
    ('Mindestens 3 Kinder haben einen Hund.', 'Höchstens 2 Kinder haben einen Hund.', ['Mindestens 3 Kinder haben keinen Hund.', 'Genau 3 Kinder haben einen Hund.']),
    ('Alle Bäume im Park sind Laubbäume.', 'Mindestens ein Baum im Park ist kein Laubbaum.', ['Alle Bäume im Park sind Nadelbäume.', 'Kein Baum im Park ist ein Laubbaum.']),
    ('Der Zug kommt pünktlich und ist sauber.', 'Der Zug kommt nicht pünktlich oder ist nicht sauber.', ['Der Zug kommt nicht pünktlich und ist nicht sauber.', 'Der Zug kommt pünktlich, aber nicht sauber.']),
    ('Es regnet oder es ist kalt.', 'Es regnet nicht und es ist nicht kalt.', ['Es regnet nicht oder es ist nicht kalt.', 'Es regnet und es ist kalt.']),
    ('Höchstens 5 Plätze sind frei.', 'Mindestens 6 Plätze sind frei.', ['Höchstens 5 Plätze sind besetzt.', 'Mindestens 5 Plätze sind frei.']),
    ('Es gibt einen Tag ohne Hausaufgaben.', 'An jedem Tag gibt es Hausaufgaben.', ['Es gibt einen Tag mit Hausaufgaben.', 'An keinem Tag gibt es Hausaufgaben.']),
    ('Jede Zahl, die durch 6 teilbar ist, ist gerade.', 'Mindestens eine durch 6 teilbare Zahl ist nicht gerade.', ['Keine durch 6 teilbare Zahl ist gerade.', 'Jede durch 6 teilbare Zahl ist ungerade.']),
]


def g_negation(s):
    art = R.choice({1: ['wert', 'einfach'], 2: ['mengenwort', 'wert', 'einfach'], 3: ['mengenwort', 'demorgan', 'mengenwort']}[s])
    if art == 'wert':
        t, b = zahlaussage()
        return auswahl(f'p: „{t}“. Welchen Wahrheitswert hat ¬p?', wf(not b), [W, F, 'Das hängt von q ab.'],
                       f'p ist {wf(b)}, also ist ¬p {wf(not b)}.', 'Die Verneinung kehrt den Wahrheitswert um.')
    if art == 'einfach':
        n = R.randint(2, 40)
        k = R.choice([3, 5, 7])
        r = f'„{n} ist nicht durch {k} teilbar.“'
        return auswahl(f'Verneine die Aussage „{n} ist durch {k} teilbar.“', r,
                       [f'„{n} ist durch {k + 1} teilbar.“', f'„{n + 1} ist durch {k} teilbar.“', f'„{n} ist ungerade.“'],
                       'Die Verneinung sagt genau das Gegenteil derselben Aussage – einfach „nicht“ einfügen.', 'Was ist genau das Gegenteil?')
    if art in ('mengenwort', 'demorgan'):
        pool = NEG if art == 'mengenwort' else [x for x in NEG if ' und ' in x[0] or ' oder ' in x[0]]
        a, r, fs = R.choice(pool)
        return auswahl(f'Wie lautet die Verneinung von „{a}“?', r, fs,
                       f'Die Verneinung muss genau dann wahr sein, wenn die Aussage falsch ist: „{r}“',
                       '„Alle“ wird zu „mindestens einer … nicht“, „und“ wird zu „oder“ (und umgekehrt), „mindestens n“ zu „höchstens n − 1“.')


def g_verknuepfen(s):
    t1, b1 = zahlaussage()
    t2, b2 = zahlaussage()
    if t1.split()[0] == t2.split()[0] and t1 == t2: return None
    art = R.choice({1: ['und', 'oder'], 2: ['und', 'oder', 'gemischt'], 3: ['gemischt', 'welches', 'oder_beide']}[s])
    vor = f'p: „{t1}“, q: „{t2}“.'
    if art == 'und':
        r = b1 and b2
        return auswahl(vor + ' Ist p ∧ q wahr oder falsch?', wf(r), [W, F, 'keines von beiden'],
                       f'p ist {wf(b1)}, q ist {wf(b2)}. „Und“ ist nur wahr, wenn beide wahr sind: {wf(r)}.', 'Bestimme zuerst den Wahrheitswert von p und von q.')
    if art in ('oder', 'oder_beide'):
        if art == 'oder_beide' and not (b1 and b2): return None
        r = b1 or b2
        return auswahl(vor + ' Ist p ∨ q wahr oder falsch?', wf(r), [W, F, 'keines von beiden'],
                       f'p ist {wf(b1)}, q ist {wf(b2)}. „Oder“ ist wahr, wenn mindestens eine wahr ist: {wf(r)}.', 'Für ∨ reicht eine wahre Teilaussage.')
    if art == 'gemischt':
        ausdruck = R.choice(['p ∧ ¬q', '¬p ∨ q', '¬p ∧ ¬q', '¬(p ∨ q)', '¬(p ∧ q)'])
        r = ausdr(ausdruck)(b1, b2)
        return auswahl(vor + f' Welchen Wahrheitswert hat {ausdruck}?', wf(r), [W, F, 'keinen'],
                       f'p ist {wf(b1)}, q ist {wf(b2)}. Von innen nach außen: {ausdruck} ist {wf(r)}.', 'Rechne zuerst die Verneinungen und Klammern aus.')
    kombis = [('p ∧ q', b1 and b2), ('p ∨ q', b1 or b2), ('¬p ∧ q', (not b1) and b2), ('p ∧ ¬q', b1 and not b2)]
    wahre = [k for k, v in kombis if v]
    falsche = [k for k, v in kombis if not v]
    if len(wahre) != 1 and len(falsche) != 1: return None
    if len(wahre) == 1:
        return auswahl(vor + ' Welcher Ausdruck ist wahr?', wahre[0], falsche, f'p ist {wf(b1)}, q ist {wf(b2)}. Nur {wahre[0]} ist wahr.', 'Prüfe jeden Ausdruck einzeln.')
    return auswahl(vor + ' Welcher Ausdruck ist falsch?', falsche[0], wahre, f'p ist {wf(b1)}, q ist {wf(b2)}. Nur {falsche[0]} ist falsch.', 'Prüfe jeden Ausdruck einzeln.')


def g_tafel(s):
    pool = {1: ['p ∧ q', 'p ∨ q', '¬p'], 2: ['p ∧ ¬q', '¬p ∨ q', '¬(p ∧ q)', '¬(p ∨ q)', '¬p ∧ ¬q'], 3: ['¬p ∨ ¬q', '¬(p ∨ q)', 'p ⇒ q', 'q ⇒ p', '¬q ⇒ ¬p', '¬(p ∧ q)']}[s]
    art = R.choice({1: ['spalte', 'zeile'], 2: ['spalte', 'zeile', 'anzahl'], 3: ['spalte', 'gleich', 'anzahl']}[s])
    e = R.choice(pool)
    werte = [1 if ausdr(e)(p, q) else 0 for p, q in ZEILEN]
    if art == 'spalte':
        bild = tafel_bild([], e)
        return mit_grafik(luecken(f'Fülle die Spalte {e} der Wahrheitstafel aus (1 = wahr, 0 = falsch).', 'Zeile 1: □; Zeile 2: □; Zeile 3: □; Zeile 4: □', HZ, werte,
                                  f'{e} für (p, q) = ww, wf, fw, ff: ' + ', '.join('w' if v else 'f' for v in werte) + '.',
                                  'Gehe Zeile für Zeile vor; bei Verneinungen zuerst eine Hilfsspalte denken.', c=[str(v) for v in werte]), bild)
    if art == 'zeile':
        i = R.randrange(4)
        p, q = ZEILEN[i]
        return auswahl(f'p ist {wf(p)}, q ist {wf(q)}. Welchen Wahrheitswert hat {e}?', wf(werte[i]), [W, F, 'keinen'],
                       f'Mit p = {wf(p)}, q = {wf(q)}: {e} ist {wf(werte[i])}.', 'Setze die Wahrheitswerte ein und rechne von innen nach außen.')
    if art == 'anzahl':
        return mit_grafik(zahl(f'In wie vielen der 4 Zeilen der Wahrheitstafel ist {e} wahr?', f'Spalte {e}: ' + ', '.join('w' if v else 'f' for v in werte) + f' – {sum(werte)}-mal wahr.',
                               'Fülle die Spalte im Kopf aus und zähle die w.', sum(werte), f'{" + ".join(map(str, werte))}'), tafel_bild([], e))
    paare = [('¬(p ∧ q)', '¬p ∨ ¬q', True), ('¬(p ∨ q)', '¬p ∧ ¬q', True), ('p ⇒ q', '¬q ⇒ ¬p', True), ('p ⇒ q', 'q ⇒ p', False),
             ('¬(p ∧ q)', '¬p ∧ ¬q', False), ('p ⇒ q', '¬p ∨ q', True), ('¬(p ∨ q)', '¬p ∨ ¬q', False)]
    a, b, gl = R.choice(paare)
    wa = ['w' if ausdr(a)(p, q) else 'f' for p, q in ZEILEN]
    wb = ['w' if ausdr(b)(p, q) else 'f' for p, q in ZEILEN]
    return ja_nein(f'Haben {a} und {b} in allen Zeilen denselben Wahrheitswert (sind sie gleichwertig)?', gl,
                   f'{a}: {", ".join(wa)}. {b}: {", ".join(wb)}. ' + ('Gleich in allen Zeilen.' if gl else 'In mindestens einer Zeile verschieden.'),
                   'Stelle für beide Ausdrücke die Spalte auf und vergleiche Zeile für Zeile.')


FOLG = [  # (wenn, dann, Gegenbeispiel zur Umkehrung)
    ('eine Zahl durch 6 teilbar ist', 'sie gerade', '8 ist gerade, aber nicht durch 6 teilbar'),
    ('ein Viereck ein Quadrat ist', 'es ein Rechteck', 'ein Rechteck mit 2 cm und 5 cm ist kein Quadrat'),
    ('eine Zahl durch 10 teilbar ist', 'sie durch 5 teilbar', '15 ist durch 5, aber nicht durch 10 teilbar'),
    ('es regnet', 'die Straße nass', 'die Straße kann auch durch einen Rasensprenger nass sein'),
    ('ein Tier ein Hund ist', 'es ein Säugetier', 'eine Katze ist ein Säugetier, aber kein Hund'),
    ('eine Zahl größer als 10 ist', 'sie größer als 5', '7 ist größer als 5, aber nicht größer als 10'),
]


def g_folgerung(s):
    art = R.choice({1: ['wert', 'nur_falsch', 'zahl_impl', 'zahl_impl'], 2: ['wert', 'umkehrung', 'kontra', 'zahl_impl'], 3: ['umkehrung', 'kontra', 'schluss', 'zahl_impl']}[s])
    if art == 'wert':
        p, q = R.choice(ZEILEN)
        return auswahl(f'p ist {wf(p)}, q ist {wf(q)}. Welchen Wahrheitswert hat p ⇒ q?', wf((not p) or q), [W, F, 'keinen'],
                       f'p ⇒ q ist nur falsch, wenn p wahr und q falsch ist. Hier: {wf((not p) or q)}.', 'Wann ist ein Versprechen „wenn p, dann q“ gebrochen?')
    if art == 'nur_falsch':
        return auswahl('In welchem Fall ist „Wenn p, dann q“ falsch?', 'p wahr, q falsch', ['p falsch, q wahr', 'p falsch, q falsch', 'p wahr, q wahr'],
                       'Nur wenn die Bedingung p erfüllt ist und q trotzdem nicht eintritt, ist die Folgerung widerlegt.', 'Denke an ein Versprechen: Wann wurde es gebrochen?')
    w, d, gg = R.choice(FOLG)
    if art == 'umkehrung':
        r = 'Nein, die Umkehrung muss nicht gelten.'
        return auswahl(f'Die Aussage „Wenn {w}, dann ist {d}.“ ist wahr (p: Wenn-Teil, q: Dann-Teil). Folgt daraus die Umkehrung (q ⇒ p)?', r,
                       ['Ja, Wenn-dann-Aussagen gelten immer in beide Richtungen.', 'Ja, weil die ursprüngliche Aussage wahr ist.', 'Nein, die Umkehrung ist immer falsch.'],
                       f'Gegenbeispiel: {gg}. Die Umkehrung kann wahr oder falsch sein – sie folgt nicht automatisch.', 'Suche ein Gegenbeispiel für die umgekehrte Richtung.')
    if art == 'kontra':
        r = 'Wenn q nicht gilt, dann gilt auch p nicht (¬q ⇒ ¬p).'
        return auswahl(f'„Wenn {w}, dann ist {d}.“ ist wahr (p ⇒ q; p: Wenn-Teil, q: Dann-Teil). Welche Aussage folgt sicher daraus?', r,
                       ['Wenn q gilt, dann gilt auch p (q ⇒ p).', 'Wenn p nicht gilt, dann gilt auch q nicht (¬p ⇒ ¬q).', 'p und q sind beide wahr.'],
                       'Die Kontraposition ¬q ⇒ ¬p ist gleichwertig zu p ⇒ q (gleiche Wahrheitstafel). Umkehrung und „¬p ⇒ ¬q“ folgen nicht.',
                       'Vergleiche die Wahrheitstafeln: Welche Folgerung ist gleichwertig?')
    if art == 'schluss':
        r = 'Nein – das ist ein Fehlschluss (Umkehrung).'
        return auswahl(f'Es gilt: „Wenn {w}, dann ist {d}.“ Man beobachtet: q ist eingetreten. Darf man schließen, dass auch p gilt?', r,
                       ['Ja, weil q eingetreten ist.', 'Ja, wenn die Aussage wahr ist.', 'Nein, dann gilt sicher ¬p.'],
                       f'q kann auch ohne p eintreten: {gg}.', 'Ist p die einzige Möglichkeit, wie q eintreten kann?')
    n = R.randint(2, 40)
    k1 = R.choice([4, 6, 8, 9, 10])
    k2 = {4: 2, 6: 3, 8: 4, 9: 3, 10: 5}[k1]
    p, q = n % k1 == 0, n % k2 == 0
    return auswahl(f'Für n = {n}: p: „n ist durch {k1} teilbar“, q: „n ist durch {k2} teilbar“. Welchen Wahrheitswert hat p ⇒ q?', wf((not p) or q), [W, F, 'keinen'],
                   f'p ist {wf(p)}, q ist {wf(q)}. ' + ('p falsch – die Folgerung ist dann immer wahr.' if not p else f'p und q wahr: wahr.'),
                   'Bestimme p und q, dann die Regel für ⇒.')


GEN = {'aussagen': g_aussagen, 'negation': g_negation, 'verknuepfen': g_verknuepfen, 'tafel': g_tafel, 'folgerung': g_folgerung}

bauen('sonder.logik',
      'Aussagen erkennen, verneinen und mit und, oder sowie wenn–dann verknüpfen; Wahrheitstafeln aufstellen und Folgerungen beurteilen.',
      ['Aussage (proposition): eindeutig wahr oder falsch.',
       '¬p ist wahr, wenn p falsch ist. ¬(alle …) = mindestens einer … nicht.',
       'p ∧ q: beide wahr. p ∨ q: mindestens eine wahr.',
       'p ⇒ q: nur falsch bei p wahr, q falsch. Kontraposition ¬q ⇒ ¬p ist gleichwertig, die Umkehrung q ⇒ p nicht.',
       'Wahrheitstafel (truth table): 4 Zeilen bei zwei Aussagen.'],
      [('Aussagen', ['aussagen', 'negation']), ('Verknüpfungen', ['verknuepfen', 'tafel']), ('Folgerungen', ['folgerung'])],
      ETAPPEN, GEN,
      offen=['Ohne Lehrplan-Zuordnung (Verlagsinhalt); Niveau Klasse 9/10 angenommen. Äquivalenz (⇔) und ausschließendes Oder nur am Rand (nicht als eigene Lernkarte).',
             'Wahrheitswerte in Lücken als 1 (wahr) / 0 (falsch), weil Lücken nur ganze Zahlen erlauben. In der Tabelle stehen w/f.',
             'Feld klasse: {"zusatz": 10} statt {} (Prüfskript verlangt einen Eintrag) – siehe FRAGE im Postfach.'])
