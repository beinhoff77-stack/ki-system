#!/usr/bin/env python3
"""Thema stochastik.verknuepft – Verknüpfte Ereignisse (Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(914)

PRIM = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
EREIG = [
    ('gerade', lambda k: k % 2 == 0),
    ('ungerade', lambda k: k % 2 == 1),
    ('durch 3 teilbar', lambda k: k % 3 == 0),
    ('durch 4 teilbar', lambda k: k % 4 == 0),
    ('durch 5 teilbar', lambda k: k % 5 == 0),
    ('eine Primzahl', lambda k: k in PRIM),
    ('eine Quadratzahl', lambda k: int(k ** 0.5) ** 2 == k),
]
SZEN = [  # (Gesamtheit, Merkmal A, Merkmal B)
    ('Schülerinnen und Schüler einer Schule', 'hat ein Haustier', 'fährt mit dem Rad zur Schule'),
    ('Besucher eines Freibads', 'ist Erwachsener', 'hat eine Jahreskarte'),
    ('Teilnehmende einer Umfrage', 'liest täglich Nachrichten', 'ist älter als 40 Jahre'),
    ('Mitglieder eines Fußballvereins', 'spielt in einer Mannschaft', 'ist jünger als 18 Jahre'),
    ('Fahrgäste eines Zuges', 'hat einen Sitzplatz reserviert', 'fährt in der 1. Klasse'),
    ('Kunden eines Online-Shops', 'zahlt per Rechnung', 'bestellt zum ersten Mal'),
]


def tafel_text(aa, ab, ba, bb, A='A', B='B'):
    return (f'Vierfeldertafel (Anzahlen): {A} und {B}: {dz(aa)}; {A} und nicht {B}: {dz(ab)}; '
            f'nicht {A} und {B}: {dz(ba)}; nicht {A} und nicht {B}: {dz(bb)}.')


def zufalls_tafel(N):
    while True:
        cuts = sorted(R.sample(range(1, N), 3))
        t = [cuts[0], cuts[1] - cuts[0], cuts[2] - cuts[1], N - cuts[2]]
        if min(t) >= max(2, N // 25): return t


SZEN_W = {  # Gesamtheit -> (Einzelner, Merkmal A kurz, nicht A, Merkmal B kurz, nicht B)
    'Schülerinnen und Schüler einer Schule': ('ein Kind dieser Schule', 'Haustier', 'kein Haustier', 'Rad', 'kein Rad'),
    'Besucher eines Freibads': ('ein Besucher', 'erwachsen', 'Kind', 'Jahreskarte', 'keine Jahreskarte'),
    'Teilnehmende einer Umfrage': ('eine teilnehmende Person', 'liest täglich', 'liest nicht täglich', 'über 40', 'höchstens 40'),
    'Mitglieder eines Fußballvereins': ('ein Vereinsmitglied', 'Mannschaft', 'keine Mannschaft', 'unter 18', 'mindestens 18'),
    'Fahrgäste eines Zuges': ('ein Fahrgast', 'reserviert', 'nicht reserviert', '1. Klasse', '2. Klasse'),
    'Kunden eines Online-Shops': ('eine Kundin oder ein Kunde', 'Rechnung', 'andere Zahlung', 'Erstbestellung', 'Stammkunde'),
}


def tafel(aa, ab, ba, bb, zeige, frage=None, kopfA=('A', 'nicht A'), kopfB=('B', 'nicht B'), fmt=None):
    """Vierfeldertafel als Tabelle. zeige: Menge der sichtbaren Felder aus aa ab ba bb A nA B nB N; frage: Feld mit '?'."""
    fmt = fmt or dz
    w = {'aa': aa, 'ab': ab, 'ba': ba, 'bb': bb, 'A': aa + ab, 'nA': ba + bb, 'B': aa + ba, 'nB': ab + bb, 'N': aa + ab + ba + bb}
    z = lambda k: '?' if k == frage else (fmt(w[k]) if k in zeige else '')  # noqa: E731
    return {'typ': 'tabelle', 'kopf': ['', kopfB[0], kopfB[1], 'Summe'],
            'zeilen': [[kopfA[0], z('aa'), z('ab'), z('A')], [kopfA[1], z('ba'), z('bb'), z('nA')], ['Summe', z('B'), z('nB'), z('N')]]}


def cf(x):
    return str(float(x)) if Fr(x).denominator != 1 else str(int(x))


ETAPPEN = [
    {'lernziel': 'verknuepfen', 'titel': 'Schnitt, Vereinigung, Gegenereignis',
     'regel': '⟦A ∩ B⟧ („A und B“): beide treten ein. ⟦A ∪ B⟧ („A oder B“): mindestens eines tritt ein. ⟦Ā⟧ („nicht A“): A tritt nicht ein. Bei Laplace-Experimenten: P = Anzahl günstiger : Anzahl möglicher Ergebnisse.',
     'schritte': ['Zahl aus 1–20, A: gerade, B: durch 3 teilbar. A ∩ B = {6, 12, 18}.', 'P(A ∩ B) = 3 : 20 = ⟦0,15⟧.'],
     'probe': '6, 12, 18 sind gerade und durch 3 teilbar ✓',
     'bild': {'typ': 'figur', 'punkte': {'_M1': [0, 0], '_M2': [4, 0], 'A': [-2.6, 2.6], 'B': [6.6, 2.6], '6, 12, 18': [2, 0]}, 'kreise': [{'m': '_M1', 'r': 3.5}, {'m': '_M2', 'r': 3.5}]},
     'fehler': 'A ∪ B mit „beide“ zu übersetzen ist falsch: ⟦∪ heißt „oder“⟧ (mindestens eines), ⟦∩ heißt „und“⟧ (beide).'},
    {'lernziel': 'additionssatz', 'titel': 'Der Additionssatz',
     'regel': '⟦P(A ∪ B) = P(A) + P(B) − P(A ∩ B)⟧. Die Schnittmenge wird einmal abgezogen, weil sie sonst ⟦doppelt gezählt⟧ würde. Sind A und B ⟦unvereinbar⟧ (A ∩ B = ∅), gilt P(A ∪ B) = P(A) + P(B).',
     'schritte': ['P(A) = 0,5, P(B) = 0,3, P(A ∩ B) = 0,1.', 'P(A ∪ B) = 0,5 + 0,3 − 0,1 = ⟦0,7⟧.'],
     'probe': 'P(Ā ∩ B̄) = 1 − 0,7 = 0,3 ≥ 0 ✓',
     'bild': {'typ': 'figur', 'punkte': {'_M1': [0, 0], '_M2': [4, 0], 'A': [-2.6, 2.6], 'B': [6.6, 2.6], '6, 12, 18': [2, 0]}, 'kreise': [{'m': '_M1', 'r': 3.5}, {'m': '_M2', 'r': 3.5}]},
     'fehler': 'P(A ∪ B) = 0,5 + 0,3 = 0,8 ist falsch, wenn A und B gemeinsame Ergebnisse haben: Die ⟦Schnittmenge⟧ wurde doppelt gezählt.'},
    {'lernziel': 'vierfeld', 'titel': 'Vierfeldertafel ergänzen',
     'regel': 'Eine ⟦Vierfeldertafel⟧ ordnet nach zwei Merkmalen. ⟦Zeilen- und Spaltensummen⟧ müssen stimmen; unten rechts steht die Gesamtzahl. Fehlende Felder durch Ergänzen zur Summe.',
     'schritte': ['200 Befragte, 80 haben Merkmal A, davon 30 auch Merkmal B.', 'A und nicht B: 80 − 30 = ⟦50⟧; nicht A: 200 − 80 = 120.'],
     'probe': '30 + 50 = 80 ✓',
     'bild': {'typ': 'tabelle', 'kopf': ['', 'B', 'nicht B', 'Summe'], 'zeilen': [['A', '30', '?', '80'], ['nicht A', '', '', '?'], ['Summe', '', '', '200']]},
     'fehler': 'Das Feld „A und nicht B“ als 200 − 30 zu berechnen ist falsch: Man ergänzt innerhalb der ⟦Zeile A⟧ zu deren Summe 80.'},
    {'lernziel': 'tafel_wkeit', 'titel': 'Wahrscheinlichkeiten aus der Tafel',
     'regel': 'Teilt man jede Anzahl durch die ⟦Gesamtzahl⟧, erhält man eine Vierfeldertafel mit Wahrscheinlichkeiten. ⟦P(A) = P(A ∩ B) + P(A ∩ B̄)⟧ (Randsumme).',
     'schritte': ['Gesamt 400, A und B: 60, A und nicht B: 100.', 'P(A ∩ B) = 60 : 400 = 0,15; P(A) = 160 : 400 = ⟦0,4⟧.'],
     'probe': '0,15 + 0,25 = 0,4 ✓',
     'bild': {'typ': 'tabelle', 'kopf': ['', 'B', 'nicht B', 'Summe'], 'zeilen': [['A', '60 → 0,15', '100 → 0,25', '160 → 0,4'], ['Summe', '', '', '400 → 1']]},
     'fehler': 'P(A ∩ B) = 60 : 160 ist falsch, wenn nach der Wahrscheinlichkeit unter ⟦allen⟧ gefragt ist: Man teilt durch die ⟦Gesamtzahl⟧ 400.'},
    {'lernziel': 'bedingt', 'titel': 'Bedingte Wahrscheinlichkeit',
     'regel': '⟦P_B(A)⟧ ist die Wahrscheinlichkeit von A, ⟦wenn man schon weiß⟧, dass B eingetreten ist: ⟦P_B(A) = P(A ∩ B) : P(B)⟧. In der Tafel: nur die ⟦Spalte B⟧ betrachten.',
     'schritte': ['200 Personen, davon 50 mit B. Von diesen 50 haben 20 auch A.', 'Du weißt schon: B ist eingetreten. Dann zählt nur die ⟦Spalte B⟧ mit 50 Personen.', 'P_B(A) = 20 : 50 = ⟦0,4⟧.'],
     'probe': 'Man teilt durch die Anzahl in B, nicht durch alle ✓',
     'fehler': 'P_B(A) und P_A(B) verwechseln. P_B(A) = 20 : 50 = 0,4 (unter allen mit B). P_A(B) = 20 : 80 = 0,25 (unter allen mit A). Die ⟦Bedingung⟧ unten bestimmt, ⟦durch welche Summe⟧ du teilst.',
     'bild': {'typ': 'tabelle', 'kopf': ['', 'B', 'nicht B', 'Summe'], 'zeilen': [['A', '20', '60', '80'], ['nicht A', '30', '90', '120'], ['Summe', '50', '150', '200']]}},
    {'lernziel': 'verstehen', 'titel': 'Aussagen über Ereignisse prüfen',
     'regel': 'Prüfe Aussagen mit Mengen und Zahlen: ⟦unvereinbar⟧ heißt A ∩ B = ∅. Das ⟦Gegenereignis⟧ von „mindestens eins“ ist „keins“. Wahrscheinlichkeiten liegen zwischen ⟦0 und 1⟧.',
     'schritte': ['Behauptung: P(A) = 0,7 und P(B) = 0,6, also sind A und B unvereinbar.', 'Wären sie unvereinbar, wäre P(A ∪ B) = 1,3 > 1 – unmöglich. ⟦A und B müssen sich überschneiden⟧.'],
     'probe': 'P(A ∩ B) ≥ 0,7 + 0,6 − 1 = 0,3 ✓',
     'fehler': 'Das Gegenereignis von „mindestens ein Treffer“ ist nicht „mindestens ein Fehlschuss“, sondern ⟦„kein Treffer“⟧.'},
]


def g_verknuepfen(s):
    N = R.choice([20, 25, 50, 100]) if s > 1 else 20
    (ta, fa), (tb, fb) = R.sample(EREIG, 2)
    om = range(1, N + 1)
    A = [k for k in om if fa(k)]
    B = [k for k in om if fb(k)]
    art = R.choice({1: ['schnitt', 'gegen', 'wort'], 2: ['schnitt', 'vereinigung', 'symbol', 'symbol'], 3: ['ohne', 'weder', 'anzahl']}[s])
    vor = f'Aus den Zahlen 1 bis {N} wird zufällig eine gezogen. A: „Die Zahl ist {ta}.“ B: „Die Zahl ist {tb}.“'
    if art == 'wort':
        r = f'Die Zahl ist {ta} oder {tb} (oder beides).'
        return auswahl(vor + ' Was bedeutet das Ereignis A ∪ B?', r,
                       [f'Die Zahl ist {ta} und {tb}.', f'Die Zahl ist weder {ta} noch {tb}.', f'Die Zahl ist {ta}, aber nicht {tb}.'],
                       'A ∪ B: mindestens eines der Ereignisse tritt ein („oder“ im einschließenden Sinn).', '∪ steht für „oder“, ∩ für „und“.')
    if art == 'symbol':
        sz, ma, mb = R.choice(SZEN)
        varianten = [(f'{ma} und {mb}', 'A ∩ B'), (f'{ma}, aber nicht: {mb}', 'A ∩ B̄'), (f'nicht: {ma}, aber: {mb}', 'Ā ∩ B'),
                     (f'weder „{ma}“ noch „{mb}“', 'Ā ∩ B̄'), (f'mindestens eines von beiden', 'A ∪ B')]
        wort, r = R.choice(varianten)
        return auswahl(f'Untersucht werden {sz}. A: „{ma}“, B: „{mb}“. Wie schreibt man das Ereignis „{wort}“?', r,
                       ['A ∩ B', 'A ∪ B', 'Ā ∩ B', 'A ∩ B̄', 'Ā ∩ B̄', 'Ā ∪ B̄'],
                       f'Der Strich bedeutet „nicht“, ∩ „und“, ∪ „oder“. „{wort}“ ist {r}.',
                       'Übersetze Wort für Wort: „nicht“ = Strich, „und“ = ∩, „oder“ = ∪.')
    if art == 'schnitt':
        M, name = [k for k in A if k in B], 'A ∩ B'
    elif art == 'vereinigung':
        M, name = sorted(set(A) | set(B)), 'A ∪ B'
    elif art == 'gegen':
        vor = f'Aus den Zahlen 1 bis {N} wird zufällig eine gezogen. A: „Die Zahl ist {ta}.“'
        M, name = [k for k in om if k not in A], 'Ā („nicht A“)'
    elif art == 'ohne':
        M, name = [k for k in A if k not in B], 'A ∩ B̄ („A, aber nicht B“)'
    elif art == 'weder':
        M, name = [k for k in om if k not in A and k not in B], 'Ā ∩ B̄ („weder A noch B“)'
    else:
        wahl = R.choice(['A ∩ B', 'A ∩ B̄', 'Ā ∩ B'])
        M = {'A ∩ B': [k for k in A if k in B], 'A ∩ B̄': [k for k in A if k not in B], 'Ā ∩ B': [k for k in B if k not in A]}[wahl]
        if not M or len(M) > 15: return None
        return luecken(vor + f' Wie viele Zahlen liegen in {wahl}?', 'Anzahl: □', 'Anzahl der Zahlen', [len(M)],
                       f'{wahl}: {", ".join(map(str, M))} – das sind {len(M)} Zahlen.', 'Schreibe die passenden Zahlen auf und zähle.', c=[str(len(M))])
    if not M or len(M) == N: return None
    p = Fr(len(M), N)
    zeig = ', '.join(map(str, M)) if len(M) <= 12 else f'{len(M)} Zahlen'
    return zahl(vor + f' Berechne P({name}) als Dezimalzahl.', f'{name.split(" (")[0]}: {zeig}. P = {len(M)} : {N} = {dz(p)}.',
                {'schnitt': 'Welche Zahlen erfüllen beide Bedingungen?', 'vereinigung': 'Zähle alle, die mindestens eine Bedingung erfüllen – keine doppelt.',
                 'gegen': 'Gegenereignis: P(Ā) = 1 − P(A).', 'ohne': 'Nimm die Zahlen aus A und streiche die, die auch in B liegen.',
                 'weder': 'Zähle die Zahlen, die keine der beiden Bedingungen erfüllen.'}[art],
                p, f'{len(M)} / {N}')


def g_vierfeld(s):
    N = R.choice([100, 120, 150, 200, 250, 300, 400, 500])
    aa, ab, ba, bb = zufalls_tafel(N)
    szen, ma, mb = R.choice(SZEN)
    A_, B_ = aa + ab, aa + ba
    vor = f'Untersucht werden {dz(N)} {szen}. A: „{ma}“, B: „{mb}“.'
    W = {'aa': aa, 'ab': ab, 'ba': ba, 'bb': bb, 'A': A_, 'nA': N - A_, 'B': B_, 'nB': N - B_, 'N': N}
    NAME = {'aa': 'A und B', 'ab': 'A und nicht B', 'ba': 'nicht A und B', 'bb': 'nicht A und nicht B', 'A': 'Summe A', 'nA': 'Summe nicht A',
            'B': 'Summe B', 'nB': 'Summe nicht B'}
    if s == 1:
        frage, zeige, w = R.choice([('ab', {'aa', 'A'}, f'Zeile A: {dz(A_)} − {dz(aa)} = {dz(ab)}.'),
                                    ('ba', {'aa', 'B'}, f'Spalte B: {dz(B_)} − {dz(aa)} = {dz(ba)}.'),
                                    ('nA', {'A', 'N'}, f'Gesamt − A: {dz(N)} − {dz(A_)} = {dz(N - A_)}.'),
                                    ('aa', {'ab', 'A'}, f'Zeile A: {dz(A_)} − {dz(ab)} = {dz(aa)}.')])
        return bild(zahl(vor + f' Ergänze das Feld „?“ ({NAME[frage]}).', w, 'Ergänze innerhalb einer Zeile oder Spalte zu ihrer Summe.', W[frage],
                         {'ab': f'{A_} - {aa}', 'ba': f'{B_} - {aa}', 'nA': f'{N} - {A_}', 'aa': f'{A_} - {ab}'}[frage]),
                    tafel(aa, ab, ba, bb, zeige | {'N'}, frage))
    if s == 2:
        if R.random() < 0.5:
            return bild(zahl(vor + f' Ergänze das Feld „?“ (weder A noch B).',
                             f'Nicht A: {dz(N)} − {dz(A_)} = {dz(N - A_)}; nicht A und B: {dz(B_)} − {dz(aa)} = {dz(ba)}; weder noch: {dz(N - A_)} − {dz(ba)} = {dz(bb)}.',
                             'Fülle die Tafel Schritt für Schritt: erst Randsummen, dann die inneren Felder.', bb, f'{N} - {A_} - ({B_} - {aa})'),
                        tafel(aa, ab, ba, bb, {'aa', 'A', 'B', 'N'}, 'bb'))
        return zahl(vor + f' {dz(A_)} haben A, {dz(B_)} haben B, {dz(aa)} haben beides. Wie viele haben weder A noch B?',
                    f'Nicht A: {dz(N - A_)}; davon mit B: {dz(B_)} − {dz(aa)} = {dz(ba)}; weder noch: {dz(N - A_)} − {dz(ba)} = {dz(bb)}.',
                    'Lege eine Vierfeldertafel an: erst Randsummen, dann die inneren Felder.', bb, f'{N} - {A_} - ({B_} - {aa})')
    typ = R.random()
    if typ < 0.35:
        falsch = R.choice(['nA', 'nB'])
        d = R.choice([-10, -5, 5, 10])
        if W[falsch] + d <= 0: return None
        t = tafel(aa, ab, ba, bb, set(W))
        zi, sp = (1, 3) if falsch == 'nA' else (2, 2)
        t['zeilen'][zi][sp] = dz(W[falsch] + d)
        r = f'Die {"Zeilensumme „nicht A“" if falsch == "nA" else "Spaltensumme „nicht B“"} muss {dz(W[falsch])} sein.'
        return bild(auswahl(vor + ' In der Tafel ist genau eine Summe falsch. Welche?', r,
                            [f'Die Zeilensumme „A“ muss {dz(A_ + 10)} sein.', f'Die Spaltensumme „B“ muss {dz(B_ - 10)} sein.',
                             f'Die Gesamtzahl muss {dz(N + d)} sein.', 'Die Zeilensumme „nicht A“ muss ' + dz(W['nA'] + 5) + ' sein.' if falsch == 'nB' else 'Die Spaltensumme „nicht B“ muss ' + dz(W['nB'] + 5) + ' sein.'],
                            f'Prüfe jede Zeile und Spalte: {dz(ba)} + {dz(bb)} = {dz(W["nA"])} (nicht A), {dz(ab)} + {dz(bb)} = {dz(W["nB"])} (nicht B).',
                            'Addiere die inneren Felder jeder Zeile und Spalte und vergleiche mit der Summe.'), t)
    if typ < 0.65:
        return bild(zahl(vor + ' Ergänze das Feld „?“.',
                         f'Gesamt − die drei anderen inneren Felder: {dz(N)} − {dz(ab)} − {dz(ba)} − {dz(bb)} = {dz(aa)}.', 'Die vier inneren Felder ergeben zusammen die Gesamtzahl.',
                         aa, f'{N} - {ab} - {ba} - {bb}'), tafel(aa, ab, ba, bb, {'ab', 'ba', 'bb', 'N'}, 'aa'))
    proz = R.choice([20, 25, 30, 40, 45, 50, 60, 70, 75, Fr(125, 10), Fr(375, 10)])
    A2 = N * Fr(proz) / 100
    if A2.denominator != 1 or A2 <= aa: return None
    A2 = int(A2)
    return zahl(vor + f' {dz(proz)} % haben A. Unter denen mit A haben {dz(aa)} auch B. Wie viele haben A, aber nicht B?',
                f'A: {dz(proz)} % von {dz(N)} = {dz(A2)}; A ohne B: {dz(A2)} − {dz(aa)} = {dz(A2 - aa)}.', 'Rechne zuerst den Prozentsatz in eine Anzahl um.', A2 - aa,
                f'{N} * {cf(Fr(proz) / 100)} - {aa}')


def g_tafel_wkeit(s):
    if s == 2 and R.random() < 0.35:
        pa = Fr(R.randint(2, 7), 10)
        pab = Fr(R.randint(1, int(pa * 100) - 1), 100)
        pb = Fr(R.randint(int(pab * 100) + 1, 90), 100)
        if pa + pb - pab >= 1: return None
        aa, ab, ba = pab, pa - pab, pb - pab
        bb = 1 - aa - ab - ba
        frage, zeige, w, c = R.choice([
            ('ab', {'aa', 'A'}, f'P(A ∩ B̄) = P(A) − P(A ∩ B) = {dz(pa)} − {dz(pab)} = {dz(ab)}.', f'{cf(pa)} - {cf(pab)}'),
            ('bb', {'ab', 'ba', 'aa', 'N'}, f'P(Ā ∩ B̄) = 1 − {dz(aa)} − {dz(ab)} − {dz(ba)} = {dz(bb)}.', f'1 - {cf(aa)} - {cf(ab)} - {cf(ba)}'),
            ('ba', {'aa', 'B'}, f'P(Ā ∩ B) = P(B) − P(A ∩ B) = {dz(pb)} − {dz(pab)} = {dz(ba)}.', f'{cf(pb)} - {cf(pab)}')])
        return bild(zahl('Die Tafel enthält Wahrscheinlichkeiten. Berechne den Wert im Feld „?“.', w,
                         'Auch mit Wahrscheinlichkeiten gilt: Innere Felder ergeben die Randsumme, alles zusammen 1.',
                         {'ab': ab, 'bb': bb, 'ba': ba}[frage], c), tafel(aa, ab, ba, bb, zeige | {'N'}, frage))
    N = R.choice([100, 200, 250, 400, 500, 1000])
    aa, ab, ba, bb = zufalls_tafel(N)
    sz, ma, mb = R.choice(SZEN)
    ein, ka, kna, kb, knb = SZEN_W[sz]
    frage = R.choice({1: ['ab', 'aa', 'bb'], 2: ['A', 'B', 'nA'], 3: ['vereinigung', 'genau', 'nAnB']}[s])
    T = {'aa': (aa, f'„{ma}“ und „{mb}“', f'{dz(aa)} : {dz(N)}'),
         'ab': (ab, f'„{ma}“, aber nicht „{mb}“', f'{dz(ab)} : {dz(N)}'),
         'bb': (bb, f'weder „{ma}“ noch „{mb}“', f'{dz(bb)} : {dz(N)}'),
         'A': (aa + ab, f'„{ma}“', f'({dz(aa)} + {dz(ab)}) : {dz(N)}'),
         'B': (aa + ba, f'„{mb}“', f'({dz(aa)} + {dz(ba)}) : {dz(N)}'),
         'nA': (ba + bb, f'nicht „{ma}“', f'({dz(ba)} + {dz(bb)}) : {dz(N)}'),
         'vereinigung': (aa + ab + ba, f'„{ma}“ oder „{mb}“ (mindestens eines)', f'({dz(aa)} + {dz(ab)} + {dz(ba)}) : {dz(N)}'),
         'genau': (ab + ba, f'genau eines von beiden', f'({dz(ab)} + {dz(ba)}) : {dz(N)}'),
         'nAnB': (N - bb, f'mindestens eines von beiden', f'1 − {dz(bb)} : {dz(N)}')}
    z, name, w = T[frage]
    p = Fr(z, N)
    return bild(zahl(f'Die Tafel zeigt {dz(N)} {sz}. A: „{ma}“, B: „{mb}“. {ein[0].upper() + ein[1:]} wird zufällig ausgewählt. Mit welcher Wahrscheinlichkeit gilt: {name}? Gib das Ergebnis als Dezimalzahl an.',
                     f'P = {w} = {dz(p)}.', 'Welche Felder gehören zum Ereignis? Teile ihre Summe durch die Gesamtzahl.', p, f'{z} / {N}'),
                tafel(aa, ab, ba, bb, {'aa', 'ab', 'ba', 'bb', 'A', 'nA', 'B', 'nB', 'N'}, kopfA=('A', 'nicht A'), kopfB=('B', 'nicht B')))


def g_additionssatz(s):
    pa, pb = Fr(R.randint(2, 7), 10), Fr(R.randint(2, 7), 10)
    pab = Fr(R.randint(1, min(int(pa * 10), int(pb * 10)) * 10 - 1), 100) if s > 1 else Fr(R.randint(1, min(int(pa * 10), int(pb * 10)) - 1 or 1), 10)
    if pab <= 0 or pab >= min(pa, pb) or pa + pb - pab > 1: return None
    pu = pa + pb - pab
    if s == 1:
        return zahl(f'Es gilt P(A) = {dz(pa)}, P(B) = {dz(pb)} und P(A ∩ B) = {dz(pab)}. Berechne P(A ∪ B).',
                    f'P(A ∪ B) = {dz(pa)} + {dz(pb)} − {dz(pab)} = {dz(pu)}.', 'Additionssatz: die Schnittmenge einmal abziehen.', pu,
                    f'{cf(pa)} + {cf(pb)} - {cf(pab)}')
    if s == 2:
        if R.random() < 0.5:
            return zahl(f'Es gilt P(A) = {dz(pa)}, P(B) = {dz(pb)} und P(A ∪ B) = {dz(pu)}. Berechne P(A ∩ B).',
                        f'P(A ∩ B) = P(A) + P(B) − P(A ∪ B) = {dz(pa)} + {dz(pb)} − {dz(pu)} = {dz(pab)}.', 'Stelle den Additionssatz nach P(A ∩ B) um.', pab,
                        f'{cf(pa)} + {cf(pb)} - {cf(pu)}')
        return zahl(f'Es gilt P(A) = {dz(pa)}, P(B) = {dz(pb)} und P(A ∩ B) = {dz(pab)}. Mit welcher Wahrscheinlichkeit tritt keines der beiden Ereignisse ein?',
                    f'P(A ∪ B) = {dz(pu)}; keines: 1 − {dz(pu)} = {dz(1 - pu)}.', '„Keines“ ist das Gegenereignis von A ∪ B.', 1 - pu,
                    f'1 - ({cf(pa)} + {cf(pb)} - {cf(pab)})')
    if R.random() < 0.5:
        if R.random() < 0.5:
            i_, sp, bd = R.choice([(40, 50, 15), (30, 45, 10), (35, 60, 20), (25, 40, 5), (50, 55, 25), (45, 30, 15)])
            k = 100 - (i_ + sp - bd)
            return zahl(f'In einer Klasse spielen {i_} % ein Instrument, {sp} % machen Sport im Verein und {bd} % beides. Wie viel Prozent machen keins von beiden?',
                        f'Instrument oder Sport: {i_} % + {sp} % − {bd} % = {i_ + sp - bd} %. Keins: 100 % − {i_ + sp - bd} % = {k} %.',
                        'Erst P(A ∪ B) mit dem Additionssatz, dann das Gegenereignis.', k, f'100 - ({i_} + {sp} - {bd})', einheit='%')
        pr, pg, prg = R.choice([(Fr(3, 10), Fr(1, 2), Fr(1, 10)), (Fr(2, 5), Fr(1, 2), Fr(1, 5)), (Fr(1, 4), Fr(1, 2), Fr(1, 8)), (Fr(3, 10), Fr(2, 5), Fr(1, 10))])
        return zahl(f'Bei einem Glücksrad ist P(rot) = {dz(pr)}, P(Zahl gerade) = {dz(pg)} und P(rot und gerade) = {dz(prg)}. Man gewinnt bei „rot oder gerade“. Mit welcher Wahrscheinlichkeit gewinnt man?',
                    f'P = {dz(pr)} + {dz(pg)} − {dz(prg)} = {dz(pr + pg - prg)}.', 'Additionssatz: „rot und gerade“ ist in beiden enthalten.', pr + pg - prg,
                    f'{cf(pr)} + {cf(pg)} - {cf(prg)}')
    N = R.choice([20, 25, 50])
    (ta, fa), (tb, fb) = R.sample(EREIG, 2)
    A = [k for k in range(1, N + 1) if fa(k)]
    B = [k for k in range(1, N + 1) if fb(k)]
    AB = [k for k in A if k in B]
    if not AB: return None
    U = len(A) + len(B) - len(AB)
    return zahl(f'Aus 1 bis {N} wird zufällig eine Zahl gezogen. A: „{ta}“, B: „{tb}“. Berechne P(A ∪ B) mit dem Additionssatz als Dezimalzahl.',
                f'P(A) = {len(A)}/{N}, P(B) = {len(B)}/{N}, P(A ∩ B) = {len(AB)}/{N} ({", ".join(map(str, AB))}). P(A ∪ B) = {U}/{N} = {dz(Fr(U, N))}.',
                'Bestimme P(A), P(B) und P(A ∩ B) einzeln.', Fr(U, N), f'{len(A)} / {N} + {len(B)} / {N} - {len(AB)} / {N}')


def g_bedingt(s):
    if s == 3:
        typ = R.random()
        if typ < 0.4:
            if R.random() < 0.5:
                n, br_, bm, m = R.choice([(200, 50, 20, 90), (300, 60, 24, 150), (100, 30, 12, 40), (250, 50, 15, 120)])
                return auswahl(f'Von {n} Schülerinnen und Schülern tragen {br_} eine Brille; {bm} davon sind Mädchen. Insgesamt sind es {m} Mädchen. Was ist P_Mädchen(Brille), also die Wahrscheinlichkeit für eine Brille, wenn es ein Mädchen ist?',
                               f'{bm}/{m}', [f'{bm}/{br_}', f'{bm}/{n}', f'{br_}/{m}'],
                               f'Bedingung: Mädchen ({m}). Davon tragen {bm} eine Brille: {bm}/{m}. ({bm}/{br_} wäre P_Brille(Mädchen).)',
                               'Durch welche Anzahl teilst du? Die Bedingung bestimmt die Gesamtheit.')
            k, pk, g, pg = R.choice([(20, 18, 180, 9), (10, 9, 190, 19), (50, 45, 950, 19), (40, 36, 160, 12)])
            pos = pk + pg
            return auswahl(f'Ein Test zeigt bei {pk} von {k} Kranken und bei {pg} von {g} Gesunden ein positives Ergebnis. Wie groß ist P_positiv(krank)?',
                           f'{pk}/{pos}', [f'{pk}/{k}', f'{pk}/{k + g}', f'{pg}/{pos}'],
                           f'Bedingung: positiv – das sind {pk} + {pg} = {pos}. Davon krank: {pk}. P = {pk}/{pos}. ({pk}/{k} ist P_krank(positiv) – die Verwechslung ist der typische Fehler.)',
                           'Zähle zuerst alle positiven Ergebnisse.')
        pa = Fr(R.choice([2, 3, 4, 5, 6]), 10)
        pba = Fr(R.choice([1, 2, 3, 4]), 4) if R.random() < 0.5 else Fr(R.choice([1, 2, 3, 4]), 5)
        pbna = Fr(R.choice([1, 2, 3]), 4) if R.random() < 0.5 else Fr(R.choice([1, 2]), 5)
        pb = pa * pba + (1 - pa) * pbna
        g = {'typ': 'baum', 'aeste': [{'text': 'A', 'p': br(pa), 'aeste': [{'text': 'B', 'p': br(pba)}, {'text': 'B̄', 'p': br(1 - pba)}]},
                                      {'text': 'Ā', 'p': br(1 - pa), 'aeste': [{'text': 'B', 'p': br(pbna)}, {'text': 'B̄', 'p': br(1 - pbna)}]}]}
        if typ < 0.7:
            if not endlich(pb): return None
            return bild(zahl('Berechne mit dem Baumdiagramm P(B) als Dezimalzahl.',
                             f'P(B) = {br(pa)} · {br(pba)} + {br(1 - pa)} · {br(pbna)} = {dz(pa * pba)} + {dz((1 - pa) * pbna)} = {dz(pb)}.',
                             'Addiere die Pfadwahrscheinlichkeiten aller Pfade, die bei B enden.', pb,
                             f'{cf(pa)} * {cf(pba)} + (1 - {cf(pa)}) * {cf(pbna)}' if endlich(pba) and endlich(pbna) else f'{pb.numerator} / {pb.denominator}'), g)
        q = pa * pba / pb
        return bild(luecken('Berechne mit dem Baumdiagramm P_B(A) als gekürzten Bruch.', '□/□', 'Zähler / Nenner', [q.numerator, q.denominator],
                            f'P(A ∩ B) = {br(pa)} · {br(pba)} = {br(pa * pba)}; P(B) = {br(pa * pba)} + {br((1 - pa) * pbna)} = {br(pb)}. P_B(A) = {br(pa * pba)} : {br(pb)} = {br(q)}.',
                            'P_B(A) = P(A ∩ B) : P(B). Bestimme beide aus dem Baum.', c=[str(q.numerator), str(q.denominator)]), g)
    for _ in range(50):
        N = R.choice([100, 200, 400, 500])
        aa, ab, ba, bb = zufalls_tafel(N)
        B_ = aa + ba
        A_ = aa + ab
        kurz = lambda q: endlich(q) and 1000 % q.denominator == 0  # noqa: E731
        if kurz(Fr(aa, B_)) and kurz(Fr(aa, A_)): break
    else:
        return None
    if s == 1:
        return bild(zahl('Berechne P_B(A), also die Wahrscheinlichkeit für A unter der Bedingung B, als Dezimalzahl.',
                         f'Nur Spalte B betrachten: {dz(B_)} Fälle, davon {dz(aa)} mit A. P_B(A) = {dz(aa)} : {dz(B_)} = {dz(Fr(aa, B_))}.',
                         'Teile durch die Anzahl in der Bedingung B, nicht durch alle.', Fr(aa, B_), f'{aa} / ({aa} + {ba})'),
                    tafel(aa, ab, ba, bb, {'aa', 'ab', 'ba', 'bb', 'A', 'nA', 'B', 'nB', 'N'}))
    sz, ma, mb = R.choice(SZEN)
    ein = SZEN_W[sz][0]
    return bild(zahl(f'Die Tafel zeigt {dz(N)} {sz}. A: „{ma}“, B: „{mb}“. {ein[0].upper() + ein[1:]} mit Merkmal A wird zufällig ausgewählt. Mit welcher Wahrscheinlichkeit gilt dann auch B? Gib P_A(B) als Dezimalzahl an.',
                     f'Bedingung A: Nur Zeile A mit {dz(A_)} Fällen, davon {dz(aa)} mit B. P_A(B) = {dz(aa)} : {dz(A_)} = {dz(Fr(aa, A_))}.',
                     'Die Bedingung steht unten: hier A. Teile durch die Zeilensumme A.', Fr(aa, A_), f'{aa} / ({aa} + {ab})'),
                tafel(aa, ab, ba, bb, {'aa', 'ab', 'ba', 'bb', 'A', 'nA', 'B', 'nB', 'N'}))


def g_verstehen(s):
    typ = R.choice({1: 'ab', 2: 'bcd', 3: 'cdeff'}[s])
    if typ == 'f':
        pa, pb = Fr(R.randint(4, 8), 10), Fr(R.randint(3, 7), 10)
        if R.random() < 0.5:
            lo, hi = max(Fr(0), pa + pb - 1), min(pa, pb)
            if hi - lo < Fr(2, 10): return None
            r = (lo + hi) / 2
            r = Fr(round(r * 20), 20)
            if not (lo < r < hi): return None
            falsch = [dz(max(lo - Fr(5, 100), Fr(1, 100))) if lo > 0 else dz(hi + Fr(5, 100)), dz(hi + Fr(5, 100)), dz(pa + pb)]
            return auswahl(f'P(A) = {dz(pa)}, P(B) = {dz(pb)}. Welcher Wert ist für P(A ∩ B) möglich?', dz(r), falsch,
                           f'P(A ∩ B) ist höchstens so groß wie die kleinere der beiden ({dz(hi)}) und mindestens P(A) + P(B) − 1 = {dz(lo)}, weil P(A ∪ B) ≤ 1.',
                           'Kann die Schnittmenge größer sein als A oder B? Wie groß muss sie mindestens sein?')
        lo, hi = max(pa, pb), min(Fr(1), pa + pb)
        if hi - lo < Fr(2, 10): return None
        r = Fr(round((lo + hi) / 2 * 20), 20)
        if not (lo < r < hi): return None
        return auswahl(f'P(A) = {dz(pa)}, P(B) = {dz(pb)}. Welcher Wert ist für P(A ∪ B) möglich?', dz(r),
                       [dz(min(pa, pb) - Fr(1, 10)) if min(pa, pb) > Fr(1, 10) else '0', dz(pa + pb + Fr(1, 10)), dz(lo - Fr(5, 100))],
                       f'P(A ∪ B) ist mindestens so groß wie die größere ({dz(lo)}) und höchstens P(A) + P(B) bzw. 1, also höchstens {dz(hi)}.',
                       'A ∪ B enthält A und B. Wie groß kann es höchstens werden?')
    if typ == 'a':
        pa, pb = Fr(R.randint(1, 5), 10), Fr(R.randint(1, 5), 10)
        return auswahl(f'A und B sind unvereinbar, P(A) = {dz(pa)}, P(B) = {dz(pb)}. Was gilt für P(A ∪ B)?', f'P(A ∪ B) = {dz(pa + pb)}',
                       [f'P(A ∪ B) = {dz(pa * pb)}', f'P(A ∪ B) = {dz(pa + pb - pa * pb)}', 'Das kann man nicht berechnen.'],
                       f'Unvereinbar: A ∩ B = ∅, P(A ∩ B) = 0. Also P(A ∪ B) = {dz(pa)} + {dz(pb)} = {dz(pa + pb)}.', 'Was bedeutet „unvereinbar“ für A ∩ B?')
    if typ == 'b':
        n = R.randint(2, 6)
        ding = R.choice(['Würfelwürfen', 'Münzwürfen', 'Torschüssen', 'Losen'])
        ziel = {'Würfelwürfen': 'eine Sechs', 'Münzwürfen': 'Kopf', 'Torschüssen': 'ein Treffer', 'Losen': 'ein Gewinn'}[ding]
        nicht = {'Würfelwürfen': 'keine Sechs', 'Münzwürfen': 'nicht Kopf', 'Torschüssen': 'kein Treffer', 'Losen': 'kein Gewinn'}[ding]
        return auswahl(f'Bei {n} {ding} ist A: „mindestens einmal {ziel}“. Was ist das Gegenereignis Ā?', f'„kein einziges Mal {ziel}“',
                       [f'„höchstens einmal {ziel}“', f'„genau einmal {ziel}“', f'„mindestens einmal {nicht}“'],
                       'Das Gegenereignis umfasst genau die Ergebnisse, die nicht zu A gehören. Nicht „mindestens einmal“ heißt „keinmal“.',
                       'Welche Ergebnisse gehören nicht zu A?')
    if typ == 'c':
        pa, pb = Fr(R.randint(5, 9), 10), Fr(R.randint(3, 9), 10)
        if pa + pb <= 1: return None
        return auswahl(f'Jemand behauptet: „P(A) = {dz(pa)} und P(B) = {dz(pb)}; A und B können unvereinbar sein.“ Was stimmt?',
                       f'Falsch: Dann wäre P(A ∪ B) = {dz(pa + pb)} > 1. Es gilt P(A ∩ B) ≥ {dz(pa + pb - 1)}.',
                       ['Richtig, das ist möglich.', f'Falsch: P(A ∩ B) = {dz(pa * pb)} muss gelten.', 'Falsch: Wahrscheinlichkeiten kann man nicht addieren.'],
                       f'Bei unvereinbaren Ereignissen addieren sich die Wahrscheinlichkeiten: {dz(pa)} + {dz(pb)} = {dz(pa + pb)} > 1 ist unmöglich.',
                       'Kann eine Wahrscheinlichkeit größer als 1 sein?')
    if typ == 'd':
        N = R.choice([100, 200, 400])
        aa, ab, ba, bb = zufalls_tafel(N)
        if not (endlich(Fr(aa, aa + ba)) and endlich(Fr(aa, aa + ab))) or aa + ba == aa + ab: return None
        return auswahl(f'{tafel_text(aa, ab, ba, bb)} Jemand berechnet P_B(A) = {dz(aa)} : {dz(aa + ab)} = {dz(Fr(aa, aa + ab))}. Was stimmt?',
                       f'Falsch: Das ist P_A(B). Richtig: P_B(A) = {dz(aa)} : {dz(aa + ba)} = {dz(Fr(aa, aa + ba))}.',
                       ['Richtig.', f'Falsch: P_B(A) = {dz(aa)} : {dz(N)} = {dz(Fr(aa, N))}.', f'Falsch: P_B(A) = {dz(aa + ba)} : {dz(N)} = {dz(Fr(aa + ba, N))}.'],
                       f'Bei P_B(A) ist B die Bedingung: Man teilt durch alle Fälle mit B ({dz(aa + ba)}).', 'Wer steht unten als Bedingung?')
    pa, pb = Fr(R.randint(2, 6), 10), Fr(R.randint(2, 6), 10)
    pab = Fr(R.randint(1, 9), 100)
    if pab >= min(pa, pb): return None
    return auswahl(f'P(A) = {dz(pa)}, P(B) = {dz(pb)}, P(A ∩ B) = {dz(pab)}. Jemand rechnet P(A ∪ B) = {dz(pa + pb)}. Was stimmt?',
                   f'Falsch: Die Schnittmenge wurde doppelt gezählt; P(A ∪ B) = {dz(pa + pb - pab)}.',
                   ['Richtig.', f'Falsch: P(A ∪ B) = {dz(pa + pb + pab)}.', f'Falsch: P(A ∪ B) = {dz(pab)}.'],
                   f'Additionssatz: {dz(pa)} + {dz(pb)} − {dz(pab)} = {dz(pa + pb - pab)}.', 'Sind A und B unvereinbar?')


GEN = {'verknuepfen': g_verknuepfen, 'vierfeld': g_vierfeld, 'tafel_wkeit': g_tafel_wkeit, 'additionssatz': g_additionssatz,
       'bedingt': g_bedingt, 'verstehen': g_verstehen}

if __name__ == '__main__':
    bauen('stochastik.verknuepft',
          'Ereignisse verknüpfen (und, oder, nicht), Vierfeldertafeln nutzen und Wahrscheinlichkeiten mit dem Additionssatz und als bedingte Wahrscheinlichkeit berechnen.',
          ['A ∩ B: A und B. A ∪ B: A oder B (mindestens eines). Ā: nicht A, P(Ā) = 1 − P(A).', 'Vierfeldertafel: Zeilen- und Spaltensummen.',
           'P(A ∪ B) = P(A) + P(B) − P(A ∩ B).', 'P_B(A) = P(A ∩ B) : P(B).'],
          [('Ereignisse verknüpfen', ['verknuepfen', 'additionssatz']), ('Vierfeldertafel', ['vierfeld', 'tafel_wkeit']),
           ('Bedingte Wahrscheinlichkeit und Verstehen', ['bedingt', 'verstehen'])],
          ETAPPEN, GEN, vertiefung=('bedingt',),
          meiden={'verknuepfen': [], 'additionssatz': ['P(A) = 0,5, P(B) = 0,3 und P(A ∩ B) = 0,1.']},
          offen=['Vierfeldertafeln werden jetzt als Tabelle (f.grafik) gezeigt, das Venn-Diagramm als „figur“ mit zwei Kreisen (die Beschriftung der Schnittmenge ist ein Punkt mit Namen). Reihenfolge der Lernkarten an die Abschnitte angepasst (Additionssatz direkt nach „verknuepfen“).',
                 'Bedingte Wahrscheinlichkeit P_B(A) ist im „umfang“ genannt, im LehrplanPLUS der 9. Klasse aber nicht ausdrücklich; Lernkarte „bedingt“ deshalb als Vertiefung (nicht Pflicht) markiert. Schreibweise P_B(A) im Text (Tiefstellung nicht möglich).',
                 'Ā und B̄ stehen jetzt auch in Aufgaben (Prüfvorschlag „Ereignis in Symbolen“); bitte in der App prüfen, ob der Strich über B (B̄) sauber dargestellt wird.'])
