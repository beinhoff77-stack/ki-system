#!/usr/bin/env python3
"""Thema sonder.logik – Aussagenlogik (ohne Lehrplan-Zuordnung, Niveau Klasse 9/10)."""
import itertools
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403
from _rsib2 import PLAN2, art3  # noqa: E402

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
    art = R.choice({1: ['wert', 'wert', 'ist_aussage'], 2: ['keine', 'keine', 'variable'], 3: ['keine', 'variable', 'wert']}[s])  # Durchsicht 19
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
    art = R.choice({1: ['wert', 'einfach'], 2: ['mengenwort', 'mengenwort', 'demorgan'], 3: ['mengenwort', 'demorgan', 'mengenwort']}[s])  # Durchsicht 19
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
    art = R.choice({1: ['und', 'oder', 'oder_beide'], 2: ['gemischt', 'gemischt', 'oder_beide'], 3: ['gemischt', 'welches', 'oder_beide']}[s])  # Durchsicht 19
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
    # Durchsicht 19: mit p ∨ q statt ¬p ∧ ¬q gab es nie genau einen wahren/falschen Ausdruck – die Art kam nie vor.
    kombis = [('p ∧ q', b1 and b2), ('¬p ∧ ¬q', (not b1) and (not b2)), ('¬p ∧ q', (not b1) and b2), ('p ∧ ¬q', b1 and not b2)]
    wahre = [k for k, v in kombis if v]
    falsche = [k for k, v in kombis if not v]
    if len(wahre) != 1 and len(falsche) != 1: return None
    if len(wahre) == 1:
        return auswahl(vor + ' Welcher Ausdruck ist wahr?', wahre[0], falsche, f'p ist {wf(b1)}, q ist {wf(b2)}. Nur {wahre[0]} ist wahr.', 'Prüfe jeden Ausdruck einzeln.')
    return auswahl(vor + ' Welcher Ausdruck ist falsch?', falsche[0], wahre, f'p ist {wf(b1)}, q ist {wf(b2)}. Nur {falsche[0]} ist falsch.', 'Prüfe jeden Ausdruck einzeln.')


def g_tafel(s):
    pool = {1: ['p ∧ q', 'p ∨ q', '¬p'], 2: ['p ∧ ¬q', '¬p ∨ q', '¬(p ∧ q)', '¬(p ∨ q)', '¬p ∧ ¬q'], 3: ['¬p ∨ ¬q', '¬(p ∨ q)', 'p ⇒ q', 'q ⇒ p', '¬q ⇒ ¬p', '¬(p ∧ q)']}[s]
    art = R.choice({1: ['spalte', 'zeile'], 2: ['spalte', 'anzahl', 'zeile'], 3: ['spalte', 'gleich', 'anzahl']}[s])  # Durchsicht 19
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
    art = R.choice({1: ['wert', 'nur_falsch', 'zahl_impl', 'zahl_impl'], 2: ['umkehrung', 'schluss', 'zahl_impl'], 3: ['umkehrung', 'kontra', 'schluss', 'zahl_impl']}[s])  # Durchsicht 19
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
    if R.random() < 0.5:  # Durchsicht 19: auch die falsche Richtung, sonst ist die Antwort immer „wahr“
        k1, k2 = k2, k1
        n = k1 * R.randint(1, 12) + (0 if R.random() < 0.3 else 0)
    p, q = n % k1 == 0, n % k2 == 0
    return auswahl(f'Für n = {n}: p: „n ist durch {k1} teilbar“, q: „n ist durch {k2} teilbar“. Welchen Wahrheitswert hat p ⇒ q?', wf((not p) or q), [W, F, 'keinen'],
                   f'p ist {wf(p)}, q ist {wf(q)}. ' + ('p falsch – die Folgerung ist dann immer wahr.' if not p else ('p und q wahr: wahr.' if q else 'p wahr, q falsch: falsch.')),
                   'Bestimme p und q, dann die Regel für ⇒.')


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-2) ----------
# Prüfungsvorbilder: IB MYP Extended / IB DP AI SL „Logic“ (Wahrheitstafeln mit drei Aussagen, Verneinung von Implikationen,
# Kontraposition), klassische Rätsel (Ritter und Lügner, Kartenaufgabe nach Wason). Eigene Formulierungen und Zahlen.
def _filter(g, s, teil, nicht=False):
    for _ in range(150):
        t = g(s)
        if t and ((teil in t['f']['text']) != nicht): return t
    return None


def _teiler(n):
    return [k for k in range(1, n + 1) if n % k == 0]


def aussagen3(art):
    if art == 'quantor':
        f = R.choice(['prim', 'quadrat', 'teilbar', 'teilbar'])
        if f == 'prim':
            a = R.randint(10, 60)
            b = a + R.randint(3, 6)
            w = any(x in PRIM or (x > 47 and all(x % t for t in range(2, x))) for x in range(a + 1, b))
            t, beg = f'Es gibt eine Primzahl zwischen {a} und {b}.', (f'Ja: {next(x for x in range(a + 1, b) if all(x % t for t in range(2, x)))} liegt dazwischen.' if w else f'Keine der Zahlen von {a + 1} bis {b - 1} ist eine Primzahl.')
        elif f == 'quadrat':
            a = R.randint(10, 90)
            b = a + R.randint(4, 9)
            qs = [x for x in range(a + 1, b) if int(x ** 0.5) ** 2 == x]
            w = bool(qs)
            t, beg = f'Es gibt eine Quadratzahl zwischen {a} und {b}.', (f'Ja: {qs[0]} = {int(qs[0] ** 0.5)}².' if w else f'Nein: Die Quadratzahlen davor und danach liegen außerhalb.')
        else:
            k = R.choice([4, 6, 8, 9, 10, 12, 15])
            m = R.choice([x for x in [2, 3, 4, 5, 6] if x != k])
            w = k % m == 0
            t = f'Jede Zahl, die durch {k} teilbar ist, ist auch durch {m} teilbar.'
            beg = f'Ja: {m} ist ein Teiler von {k}.' if w else f'Gegenbeispiel: {k} selbst ist nicht durch {m} teilbar.'
        return auswahl(f'Welchen Wahrheitswert hat „{t}“?', wf(w), [W, F, 'keinen – das ist keine Aussage'], beg,
                       '„Es gibt …“ braucht ein Beispiel, „jede …“ wird durch ein Gegenbeispiel widerlegt.')
    if art == 'loesungsmenge':
        N = R.choice([6, 8, 10, 12])
        f = R.choice(['quad', 'lin', 'teiler'])
        if f == 'quad':
            a = R.randint(10, 80)
            form, L = f'x² < {a}', [x for x in range(1, N + 1) if x * x < a]
        elif f == 'lin':
            a, b = R.randint(2, 4), R.randint(5, 25)
            form, L = f'{a}x + 1 > {b}', [x for x in range(1, N + 1) if a * x + 1 > b]
        else:
            a = R.choice([12, 18, 20, 24, 30, 36])
            form, L = f'x ist ein Teiler von {a}', [x for x in range(1, N + 1) if a % x == 0]
        if not 0 < len(L) < N: return None
        return zahl(f'Setze für x die Zahlen 1, 2, …, {N} ein. Für wie viele davon wird die Aussageform „{form}“ zu einer wahren Aussage?',
                    f'Wahr für x = {", ".join(map(str, L))}. ' + (f'Das sind {len(L)} Zahlen.' if len(L) > 1 else 'Das ist nur eine Zahl.'), 'Setze jede Zahl ein und prüfe.', len(L), f'{len(L)}')
    # ritter: Ritter sagen immer die Wahrheit, Lügner lügen immer
    S = {'B ist ein Lügner.': lambda a, b: not b, 'B ist ein Ritter.': lambda a, b: b, 'Wir sind beide Ritter.': lambda a, b: a and b,
         'Mindestens einer von uns ist ein Lügner.': lambda a, b: not (a and b), 'Wir sind beide Lügner.': lambda a, b: not a and not b,
         'Wir sind von derselben Sorte.': lambda a, b: a == b, 'Wir sind von verschiedener Sorte.': lambda a, b: a != b}
    SB = {'A ist ein Lügner.': lambda a, b: not a, 'A ist ein Ritter.': lambda a, b: a, 'Wir sind beide Ritter.': lambda a, b: a and b,
          'Wir sind beide Lügner.': lambda a, b: not a and not b, 'Wir sind von derselben Sorte.': lambda a, b: a == b, '': None}
    sa, sb = R.choice(list(S)), R.choice(list(SB))
    loes = [(a, b) for a in (True, False) for b in (True, False)
            if S[sa](a, b) == a and (SB[sb] is None or SB[sb](a, b) == b)]
    if len(loes) != 1: return None
    a, b = loes[0]
    nm = lambda x: 'Ritter' if x else 'Lügner'
    r = f'A ist {nm(a)}, B ist {nm(b)}.'
    alle = [f'A ist {nm(x)}, B ist {nm(y)}.' for x in (True, False) for y in (True, False)]
    satz_b = f' B sagt: „{sb}“' if sb else ''
    return auswahl(f'Auf einer Insel sagen Ritter immer die Wahrheit, Lügner lügen immer. A sagt: „{sa}“{satz_b} Was sind A und B?', r,
                   [x for x in alle if x != r],
                   f'Nur bei „{r[:-1]}“ passt jede Aussage zu ihrem Sprecher: Ritter sagen Wahres, Lügner Falsches.',
                   'Probiere alle vier Fälle: Ist die Aussage eines Ritters wahr, die eines Lügners falsch?')


WENN_NEG = [  # (Wenn-dann-Aussage, Verneinung, falsche Verneinungen)
    ('Wenn es regnet, nehme ich einen Schirm mit.', 'Es regnet und ich nehme keinen Schirm mit.',
     ['Wenn es nicht regnet, nehme ich keinen Schirm mit.', 'Wenn es regnet, nehme ich keinen Schirm mit.', 'Es regnet nicht und ich nehme einen Schirm mit.']),
    ('Wenn eine Zahl durch 9 teilbar ist, ist sie durch 3 teilbar.', 'Es gibt eine Zahl, die durch 9, aber nicht durch 3 teilbar ist.',
     ['Wenn eine Zahl nicht durch 9 teilbar ist, ist sie nicht durch 3 teilbar.', 'Wenn eine Zahl durch 3 teilbar ist, ist sie durch 9 teilbar.', 'Keine Zahl ist durch 9 teilbar.']),
    ('Wenn Tom Zeit hat, kommt er zur Party.', 'Tom hat Zeit und kommt nicht zur Party.',
     ['Wenn Tom keine Zeit hat, kommt er nicht zur Party.', 'Tom hat keine Zeit und kommt zur Party.', 'Wenn Tom zur Party kommt, hat er Zeit.']),
    ('Wenn das Licht rot ist, hält das Auto an.', 'Das Licht ist rot und das Auto hält nicht an.',
     ['Wenn das Licht nicht rot ist, hält das Auto nicht an.', 'Das Licht ist grün und das Auto hält an.', 'Wenn das Auto anhält, ist das Licht rot.']),
    ('Wenn ein Viereck vier rechte Winkel hat, ist es ein Rechteck.', 'Es gibt ein Viereck mit vier rechten Winkeln, das kein Rechteck ist.',
     ['Wenn ein Viereck keine vier rechten Winkel hat, ist es kein Rechteck.', 'Kein Viereck hat vier rechte Winkel.', 'Wenn ein Viereck ein Rechteck ist, hat es vier rechte Winkel.']),
    ('Wenn die Sonne scheint, gehen wir baden.', 'Die Sonne scheint und wir gehen nicht baden.',
     ['Wenn die Sonne nicht scheint, gehen wir nicht baden.', 'Die Sonne scheint nicht und wir gehen baden.', 'Wenn wir baden gehen, scheint die Sonne.']),
]
DOPPELT = [
    ('Alle Kinder haben einen Hund oder eine Katze.', 'Mindestens ein Kind hat weder einen Hund noch eine Katze.',
     ['Kein Kind hat einen Hund oder eine Katze.', 'Alle Kinder haben keinen Hund und keine Katze.', 'Mindestens ein Kind hat keinen Hund oder keine Katze.']),
    ('Jeder Spieler hat ein Tor geschossen und eine Vorlage gegeben.', 'Mindestens ein Spieler hat kein Tor geschossen oder keine Vorlage gegeben.',
     ['Kein Spieler hat ein Tor geschossen und eine Vorlage gegeben.', 'Mindestens ein Spieler hat kein Tor geschossen und keine Vorlage gegeben.', 'Jeder Spieler hat kein Tor geschossen oder keine Vorlage gegeben.']),
    ('Es gibt einen Tag, an dem es regnet und kalt ist.', 'An jedem Tag regnet es nicht oder es ist nicht kalt.',
     ['Es gibt einen Tag, an dem es nicht regnet und nicht kalt ist.', 'An keinem Tag regnet es.', 'An jedem Tag regnet es nicht und es ist nicht kalt.']),
    ('Jede Zahl im Kasten ist gerade oder größer als 10.', 'Mindestens eine Zahl im Kasten ist ungerade und höchstens 10.',
     ['Keine Zahl im Kasten ist gerade oder größer als 10.', 'Mindestens eine Zahl im Kasten ist ungerade oder höchstens 10.', 'Jede Zahl im Kasten ist ungerade und kleiner als 10.']),
    ('Es gibt ein Buch im Regal, das dick und alt ist.', 'Jedes Buch im Regal ist nicht dick oder nicht alt.',
     ['Es gibt ein Buch im Regal, das dünn und neu ist.', 'Jedes Buch im Regal ist dünn und neu.', 'Kein Buch im Regal ist dick.']),
]


DOPPELT_NICHT = [
    ('Nicht alle Kinder haben keinen Hund.', 'Mindestens ein Kind hat einen Hund.', ['Alle Kinder haben einen Hund.', 'Kein Kind hat einen Hund.', 'Mindestens ein Kind hat keinen Hund.']),
    ('Es stimmt nicht, dass keine Zahl im Kasten gerade ist.', 'Mindestens eine Zahl im Kasten ist gerade.', ['Alle Zahlen im Kasten sind gerade.', 'Keine Zahl im Kasten ist ungerade.', 'Mindestens eine Zahl im Kasten ist ungerade.']),
    ('Es ist falsch, dass höchstens 3 Plätze frei sind.', 'Mindestens 4 Plätze sind frei.', ['Höchstens 3 Plätze sind besetzt.', 'Genau 3 Plätze sind frei.', 'Mindestens 3 Plätze sind frei.']),
    ('Nicht jeder Schüler hat nicht gefehlt.', 'Mindestens ein Schüler hat gefehlt.', ['Jeder Schüler hat gefehlt.', 'Kein Schüler hat gefehlt.', 'Mindestens ein Schüler hat nicht gefehlt.']),
    ('Es stimmt nicht, dass es keinen Tag ohne Regen gab.', 'Es gab mindestens einen Tag ohne Regen.', ['An jedem Tag hat es geregnet.', 'Es gab keinen Tag mit Regen.', 'An keinem Tag hat es geregnet.']),
]


def negation3(art):
    if art == 'doppelt_nicht':
        a, r, fs = R.choice(DOPPELT_NICHT)
        return auswahl(f'Welche Aussage bedeutet dasselbe wie „{a}“?', r, fs,
                       f'Die äußere Verneinung macht aus „alle … nicht“ ein „mindestens einer“ (bzw. aus „höchstens“ ein „mindestens“). Also: „{r}“',
                       'Verneine Schritt für Schritt von außen nach innen. Zwei Verneinungen heben sich auf.')
    if art in ('wenn_neg', 'doppelt'):
        a, r, fs = R.choice(WENN_NEG if art == 'wenn_neg' else DOPPELT)
        hilfe = ('„Wenn p, dann q“ ist nur falsch, wenn p eintritt und q nicht. Die Verneinung lautet also „p und nicht q“.' if art == 'wenn_neg'
                 else 'Zweimal umbauen: „alle“ ↔ „mindestens einer … nicht“, und dazu „und“ ↔ „oder“.')
        return auswahl(f'Wie lautet die Verneinung von „{a}“?', r, fs, f'{hilfe} Also: „{r}“',
                       'Wann wäre die Aussage falsch? Genau das beschreibt die Verneinung.')
    # gegenbeispiel
    a = R.choice([4, 6, 8, 9, 10, 12])
    b = R.choice([x for x in [3, 4, 5, 6, 8] if a % x != 0 and x != a])
    vs = [n for n in range(a, 100, a) if n % b != 0]
    beide = [n for n in range(a, 100, a) if n % b == 0]
    nur_b = [n for n in range(b, 100, b) if n % a != 0]
    keins = [n for n in range(2, 60) if n % a and n % b]
    if not (vs and beide and nur_b): return None
    r, f1, f2, f3 = R.choice(vs), R.choice(beide), R.choice(nur_b), R.choice(keins)
    if len({r, f1, f2, f3}) < 4: return None
    return auswahl(f'Welche Zahl widerlegt die Aussage „Jede durch {a} teilbare Zahl ist auch durch {b} teilbar.“?', str(r), [str(f1), str(f2), str(f3)],
                   f'{r} ist durch {a} teilbar, aber nicht durch {b} – ein Gegenbeispiel. {f1} erfüllt beides, {f2} und {f3} sind nicht durch {a} teilbar und sagen nichts aus.',
                   'Ein Gegenbeispiel erfüllt den Wenn-Teil, aber nicht den Dann-Teil.')


def verknuepfen3(art):
    if art == 'zaehlen':
        N = R.choice([20, 24, 30, 40])
        a, b = R.sample([2, 3, 4, 5, 7], 2)
        op = R.choice(['∨', '∧', '∧¬'])
        L = [n for n in range(1, N + 1) if {'∨': (n % a == 0) or (n % b == 0), '∧': n % a == 0 and n % b == 0, '∧¬': n % a == 0 and n % b != 0}[op]]
        txt = {'∨': 'p ∨ q', '∧': 'p ∧ q', '∧¬': 'p ∧ ¬q'}[op]
        na, nb = N // a, N // b
        nab = len([n for n in range(1, N + 1) if n % a == 0 and n % b == 0])
        weg = {'∨': f'{na} + {nb} − {nab} (doppelt gezählte) = {len(L)}', '∧': f'durch beide teilbar: {len(L)}', '∧¬': f'{na} − {nab} = {len(L)}'}[op]
        return zahl(f'Für jede Zahl n von 1 bis {N} gilt p: „n ist durch {a} teilbar“, q: „n ist durch {b} teilbar“. Für wie viele n ist {txt} wahr?',
                    f'Durch {a} teilbar: {na}, durch {b}: {nb}, durch beide: {nab}. {txt}: {weg}.',
                    'Zähle getrennt und achte auf Zahlen, die beides erfüllen.', len(L), f'{len(L)}')
    # finde_werte: aus drei Angaben p und q bestimmen
    p, q = R.choice(ZEILEN)
    namen = ['p ∨ q', 'p ∧ q', 'p ∧ ¬q', '¬p ∨ q', '¬(p ∨ q)', '¬(p ∧ q)', 'q ⇒ p', '¬p ∧ ¬q']
    hinweise = [(t, ausdr(t)(p, q)) for t in namen]
    for _ in range(60):
        h = R.sample(hinweise, 2)
        moegl = [(x, y) for x, y in ZEILEN if all(ausdr(t)(x, y) == v for t, v in h)]
        if len(moegl) == 1: break
    else:
        return None
    r = f'p {wf(p)}, q {wf(q)}'
    return auswahl(f'Man weiß: {h[0][0]} ist {wf(h[0][1])} und {h[1][0]} ist {wf(h[1][1])}. Welche Wahrheitswerte haben p und q?', r,
                   [f'p {wf(x)}, q {wf(y)}' for x, y in ZEILEN if (x, y) != (p, q)],
                   f'Prüfe alle vier Fälle: Nur bei {r} stimmen beide Angaben.', 'Gehe die vier Zeilen der Wahrheitstafel durch.')


DREI = {
    'p ∧ q ∧ r': lambda p, q, r: p and q and r, 'p ∨ q ∨ r': lambda p, q, r: p or q or r, 'p ∧ (q ∨ r)': lambda p, q, r: p and (q or r),
    '(p ∧ q) ∨ r': lambda p, q, r: (p and q) or r, 'p ∨ (q ∧ r)': lambda p, q, r: p or (q and r), '¬p ∧ (q ∨ r)': lambda p, q, r: (not p) and (q or r),
    '(p ∨ q) ∧ ¬r': lambda p, q, r: (p or q) and not r, 'p ∧ ¬q ∧ r': lambda p, q, r: p and not q and r,
}
EXTRA = {'p ∨ ¬p': lambda p, q: True, 'p ∧ ¬p': lambda p, q: False, '(p ∧ q) ⇒ p': lambda p, q: (not (p and q)) or p, 'p ⇒ (p ∧ q)': lambda p, q: (not p) or q}


def tafel3(art):
    if art == 'drei':
        e = R.choice(list(DREI))
        n = sum(DREI[e](p, q, r) for p in (True, False) for q in (True, False) for r in (True, False))
        return zahl(f'Eine Wahrheitstafel mit drei Aussagen p, q, r hat 2³ = 8 Zeilen. In wie vielen davon ist {e} wahr?',
                    f'Geht man alle 8 Kombinationen durch, ist {e} {n}-mal wahr.', 'Schreibe die 8 Zeilen auf (wie 4 Zeilen, einmal mit r wahr, einmal mit r falsch).', n, f'{n}')
    if art == 'gesucht':
        kand = ['p ∧ q', 'p ∨ q', 'p ∧ ¬q', '¬p ∨ q', '¬(p ∧ q)', '¬(p ∨ q)', '¬p ∧ ¬q', 'q ⇒ p', '¬p ∨ ¬q']
        e = R.choice(kand)
        sp = tuple(ausdr(e)(p, q) for p, q in ZEILEN)
        gleiche = [k for k in kand if tuple(ausdr(k)(p, q) for p, q in ZEILEN) == sp]
        andere = [k for k in kand if tuple(ausdr(k)(p, q) for p, q in ZEILEN) != sp]
        r = gleiche[0] if e not in gleiche else e
        fs = R.sample(andere, 3)
        werte = ', '.join('w' if v else 'f' for v in sp)
        return auswahl(f'Die Spalte eines Ausdrucks lautet für (p, q) = ww, wf, fw, ff: {werte}. Welcher Ausdruck ist es?', r, fs,
                       f'{r} hat genau die Werte {werte}. Bei den anderen weicht mindestens eine Zeile ab.', 'Prüfe zuerst die Zeilen mit f – sie trennen die Ausdrücke am schnellsten.')
    # immer: Tautologie
    r = R.choice(['p ∨ ¬p', '(p ∧ q) ⇒ p'])
    fs = ['p ∧ ¬p', 'p ⇒ (p ∧ q)', R.choice(['p ∨ q', '¬(p ∧ q)', 'p ⇒ q'])]
    return auswahl('Welcher Ausdruck ist in allen 4 Zeilen der Wahrheitstafel wahr?', r, fs,
                   f'{r} ist in jeder Zeile wahr. p ∧ ¬p ist nie wahr, die anderen sind mindestens in einer Zeile falsch.', 'Suche für jeden Ausdruck eine Zeile, in der er falsch ist.')


def folgerung3(art):
    # karten (nach Wason): Zahl auf der einen, Buchstabe auf der anderen Seite
    g, u = R.choice([2, 4, 6, 8]), R.choice([3, 5, 7, 9])
    v, k = R.choice('AEIOU'), R.choice('BKMRT')
    r = f'{g} und {k}'
    return auswahl(f'Jede Karte hat auf einer Seite eine Zahl, auf der anderen einen Buchstaben. Man sieht: {g}, {u}, {v}, {k}. Regel: „Wenn auf einer Seite eine gerade Zahl steht, dann steht auf der anderen ein Vokal.“ '
                   'Welche Karten muss man umdrehen, um die Regel zu prüfen?', r, [f'{g} und {v}', f'nur {g}', f'{g}, {v} und {k}'],
                   f'{g}: Hinten muss ein Vokal sein. {k}: Steht hinten eine gerade Zahl, ist die Regel verletzt. {v} und {u} können die Regel nicht widerlegen.',
                   'Die Regel p ⇒ q wird nur durch „p und nicht q“ verletzt. Welche Karten könnten so ein Paar sein?')


def g2_aussagen(s):
    if s < 3: return g_aussagen(s)
    art = art3('quantor', 'loesungsmenge', 'ritter', ['quantor', 'loesungsmenge', 'ritter', 'variable', 'loesungsmenge'])
    if art == 'variable': return _filter(g_aussagen, 3, 'Wann wird')
    return aussagen3(art)


def g2_negation(s):
    if s == 1: return g_negation(1)
    if s == 2:
        teil = AKT['nr'] % 2 if AKT['pool'] == 'uebung' else R.random() < 0.5
        return g_negation(2) if teil else negation3('gegenbeispiel')
    art = art3('wenn_neg', 'doppelt', 'doppelt_nicht', ['wenn_neg', 'doppelt', 'doppelt_nicht', 'wenn_neg', 'doppelt'])
    return negation3(art)


def g2_verknuepfen(s):
    if s < 3: return g_verknuepfen(s)
    art = art3('welches', 'zaehlen', 'finde_werte', ['welches', 'zaehlen', 'finde_werte', 'zaehlen', 'finde_werte'])
    if art == 'welches': return _filter(g_verknuepfen, 3, 'Welcher Ausdruck')
    return verknuepfen3(art)


def g2_tafel(s):
    if s < 3: return g_tafel(s)
    art = art3('gleich', 'drei', 'gesucht', ['gleich', 'drei', 'gesucht', 'immer', 'drei'])
    if art == 'gleich': return _filter(g_tafel, 3, 'gleichwertig')
    return tafel3(art)


def g2_folgerung(s):
    if s < 3: return g_folgerung(s)
    art = art3('kontra', 'umkehrung', 'karten', ['kontra', 'umkehrung', 'karten', 'schluss', 'karten'])
    if art == 'kontra': return _filter(g_folgerung, 3, 'folgt sicher')
    if art == 'umkehrung': return _filter(g_folgerung, 3, 'Umkehrung (q ⇒ p)')
    if art == 'schluss': return _filter(g_folgerung, 3, 'Darf man schließen')
    return folgerung3(art)


GEN = {'aussagen': g2_aussagen, 'negation': g2_negation, 'verknuepfen': g2_verknuepfen, 'tafel': g2_tafel, 'folgerung': g2_folgerung}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import tab  # noqa: E402

_AK = ['Satz', 'Aussage?', 'Wert']


def _a(r1, r2, r3, r4):
    return tab(_AK, ['17 ist eine Primzahl.', *r1], ['Komm her!', *r2], ['12 ist ungerade.', *r3], ['x ist größer als 3.', *r4])


_PQ = [['w', 'w'], ['w', 'f'], ['f', 'w'], ['f', 'f']]


def _t(kopf, *spalten):
    return tab(['p', 'q', *kopf], *[[*pq, *[s[i] for s in spalten]] for i, pq in enumerate(_PQ)])


_FK = ['Zahl', 'durch 4', 'gerade']
UMBAU = {
    'aussagen': {
        'einstieg': '„17 ist eine Primzahl.“ Darauf kann man mit wahr oder falsch antworten. „Komm her!“ dagegen nicht. '
                    'Sätze, die entweder wahr oder falsch sind, heißen ⟦Aussagen⟧.',
        'woerter': [['Aussage', 'ein Satz, der entweder wahr oder falsch ist'],
                    ['Wahrheitswert', 'wahr (w) oder falsch (f)']],
        'bild': _a(['?', '?'], ['?', '?'], ['?', '?'], ['?', '?']),
        'schritte': [
            {'text': '„17 ist eine Primzahl“: Die Teiler sind nur 1 und 17.'},
            {'text': 'Also eine Aussage mit dem Wahrheitswert ⟦wahr⟧.', 'bild': _a(['ja', 'w'], ['?', '?'], ['?', '?'], ['?', '?'])},
            {'text': '„12 ist ungerade“ ist auch eine Aussage, nur eine falsche.', 'bild': _a(['ja', 'w'], ['?', '?'], ['ja', 'f'], ['?', '?'])},
            {'text': '„Komm her!“ und „x ist größer als 3“ sind ⟦keine Aussagen⟧.',
             'bild': _a(['ja', 'w'], ['nein', '–'], ['ja', 'f'], ['nein', '–'])},
            {'text': '„Jede …“ widerlegt ein ⟦Gegenbeispiel⟧. „Es gibt …“ belegt ein einziges Beispiel.'},
        ],
        'fehler': '„Eine falsche Aussage ist keine Aussage“ stimmt nicht. „12 ist ungerade“ ist eine Aussage, ⟦eine falsche⟧.',
        'regel': 'Eine Aussage ist ⟦entweder wahr oder falsch⟧. Fragen, Befehle und Sätze mit offenem x sind keine Aussagen.',
    },
    'negation': {
        'einstieg': 'Ein Lehrer sagt: Alle Kinder haben ein Fahrrad. Ein Kind widerspricht. Dafür reicht schon ein Kind ohne Fahrrad. '
                    'Das Gegenteil einer Aussage heißt ⟦Verneinung⟧.',
        'woerter': [['Verneinung', '¬p: das Gegenteil von p; wahr genau dann, wenn p falsch ist'],
                    ['mindestens ein', 'eins oder mehr']],
        'bild': tab(['p', '¬p'], ['w', 'f'], ['f', 'w']),
        'schritte': [
            {'text': 'p: „Alle Kinder der Klasse haben ein Fahrrad.“'},
            {'text': '¬p ist wahr, sobald ein einziges Kind keins hat.',
             'bild': tab(['Klasse', 'p', '¬p'], ['alle mit Rad', 'w', 'f'], ['einer ohne', 'f', 'w'], ['keiner mit Rad', 'f', 'w'])},
            {'text': 'Also ¬p: ⟦Mindestens ein Kind hat kein Fahrrad⟧.'},
            {'text': '„Wenn p, dann q“ verneint man mit ⟦p und nicht q⟧.'},
        ],
        'fehler': '„Kein Kind hat ein Fahrrad“ ist nicht die Verneinung. Haben manche eins, sind ⟦beide Sätze falsch⟧.',
        'fehler_bild': tab(['Klasse', 'p', '„kein Kind …“'], ['einige mit Rad', 'f', 'f ✗']),
        'regel': 'Die Verneinung liefert ⟦immer das Gegenteil⟧. Aus „alle“ wird „mindestens einer nicht“.',
    },
    'verknuepfen': {
        'einstieg': 'Ins Kino darfst du, wenn du Hausaufgaben gemacht ⟦und⟧ aufgeräumt hast. Ein Eis gibt es, wenn die Sonne scheint ⟦oder⟧ Ferien sind. '
                    'Beide Wörter verknüpfen Aussagen.',
        'woerter': [['p ∧ q', '„p und q“: nur wahr, wenn beide wahr sind'],
                    ['p ∨ q', '„p oder q“: wahr, wenn mindestens eine wahr ist']],
        'bild': _t(['p ∧ q', 'p ∨ q'], ['w', 'f', 'f', 'f'], ['w', 'w', 'w', 'f']),
        'schritte': [
            {'text': 'p: „9 ist gerade“ (falsch). q: „9 ist durch 3 teilbar“ (wahr).'},
            {'text': 'p ∧ q ist falsch, weil p falsch ist.', 'bild': tab(['p', 'q', 'p ∧ q', 'p ∨ q'], ['f', 'w', 'f', '?'])},
            {'text': 'p ∨ q ist ⟦wahr⟧, weil q wahr ist.', 'bild': tab(['p', 'q', 'p ∧ q', 'p ∨ q'], ['f', 'w', 'f', 'w'])},
            {'text': 'Zählen bei ∨: Zahlen, die beides erfüllen, ⟦nur einmal⟧ zählen.'},
        ],
        'fehler': '„Beide wahr, also ist p ∨ q falsch“ ist falsch. Das Oder in der Mathematik ⟦schließt beides ein⟧.',
        'regel': '⟦∧ braucht beide⟧, ∨ braucht mindestens eine wahre Aussage. Das Oder schließt beides ein.',
    },
    'tafel': {
        'einstieg': 'Bei zwei Aussagen gibt es vier Möglichkeiten: beide wahr, nur die erste, nur die zweite, keine. '
                    'Eine ⟦Wahrheitstafel⟧ schreibt alle vier untereinander.',
        'woerter': [['Wahrheitstafel', 'eine Tabelle mit allen Kombinationen von w und f'],
                    ['Hilfsspalte', 'eine Spalte für einen Zwischenschritt, z. B. ¬q']],
        'bild': _t([]),
        'schritte': [
            {'text': 'Ausdruck: p ∧ ¬q. Alle vier Zeilen hinschreiben.'},
            {'text': 'Hilfsspalte ¬q: f, w, f, w.', 'bild': _t(['¬q'], ['f', 'w', 'f', 'w'])},
            {'text': 'p ∧ ¬q ist nur wahr, wo p und ¬q beide wahr sind.'},
            {'text': 'Ergebnis: ⟦f, w, f, f⟧.', 'bild': _t(['¬q', 'p ∧ ¬q'], ['f', 'w', 'f', 'w'], ['f', 'w', 'f', 'f'])},
            {'text': 'Mit drei Aussagen p, q, r gibt es 2³ = ⟦8 Zeilen⟧.'},
        ],
        'fehler': '¬(p ∧ q) ist nicht ¬p ∧ ¬q. In Zeile 2 ist das erste wahr, das zweite falsch. Richtig ist ⟦¬p ∨ ¬q⟧.',
        'fehler_bild': _t(['¬(p ∧ q)', '¬p ∧ ¬q'], ['f', 'w', 'w', 'w'], ['f', 'f', 'f', 'w']),
        'regel': 'Zwei Aussagen ergeben ⟦4 Zeilen⟧. Mit Hilfsspalten von innen nach außen rechnen.',
    },
    'folgerung': {
        'einstieg': '„Wenn es regnet, ist die Straße nass.“ Ist die Straße nass, regnet es aber nicht unbedingt. '
                    'Vielleicht fuhr ein Sprengwagen vorbei. Wenn-dann-Sätze heißen ⟦Implikation⟧.',
        'woerter': [['Implikation', 'p ⇒ q: „wenn p, dann q“'],
                    ['Umkehrung', 'q ⇒ p; sie folgt nicht automatisch'],
                    ['Kontraposition', '¬q ⇒ ¬p; sie gilt genau dann, wenn p ⇒ q gilt']],
        'bild': tab(['p', 'q', 'p ⇒ q'], ['w', 'w', 'w'], ['w', 'f', 'f'], ['f', 'w', 'w'], ['f', 'f', 'w']),
        'schritte': [
            {'text': '„Wenn eine Zahl durch 4 teilbar ist, ist sie gerade.“ Das stimmt.',
             'bild': tab(_FK, ['8', 'w', 'w'], ['6', 'f', 'w'], ['7', 'f', 'f'])},
            {'text': 'Die Umkehrung „Wenn gerade, dann durch 4 teilbar“ ist falsch: 6.',
             'bild': tab(_FK, ['8', 'w', 'w'], ['6 ✗', 'f', 'w'], ['7', 'f', 'f'])},
            {'text': 'Die Kontraposition stimmt: ⟦Nicht gerade, dann nicht durch 4 teilbar⟧.'},
        ],
        'fehler': '„Die Straße ist nass, also regnet es“ ist falsch. Das ist die ⟦Umkehrung⟧, sie folgt nicht.',
        'regel': 'p ⇒ q ist ⟦nur falsch bei p wahr, q falsch⟧. Die Kontraposition gilt mit, die Umkehrung nicht.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


d = bauen('sonder.logik',
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
             'Feld klasse: {"zusatz": 10} statt {} (Prüfskript verlangt einen Eintrag) – siehe FRAGE im Postfach.'], plan=PLAN2)
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
