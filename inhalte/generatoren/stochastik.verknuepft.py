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
    ('Mitglieder eines Sportvereins', 'spielt Fußball', 'ist jünger als 18 Jahre'),
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


def cf(x):
    return str(float(x)) if Fr(x).denominator != 1 else str(int(x))


ETAPPEN = [
    {'lernziel': 'verknuepfen', 'titel': 'Schnitt, Vereinigung, Gegenereignis',
     'regel': '⟦A ∩ B⟧ („A und B“): beide treten ein. ⟦A ∪ B⟧ („A oder B“): mindestens eines tritt ein. ⟦Ā⟧ („nicht A“): A tritt nicht ein. Bei Laplace-Experimenten: P = Anzahl günstiger : Anzahl möglicher Ergebnisse.',
     'schritte': ['Zahl aus 1–20, A: gerade, B: durch 3 teilbar. A ∩ B = {6, 12, 18}.', 'P(A ∩ B) = 3 : 20 = ⟦0,15⟧.'],
     'probe': '6, 12, 18 sind gerade und durch 3 teilbar ✓',
     'fehler': 'A ∪ B mit „beide“ zu übersetzen ist falsch: ⟦∪ heißt „oder“⟧ (mindestens eines), ⟦∩ heißt „und“⟧ (beide).'},
    {'lernziel': 'vierfeld', 'titel': 'Vierfeldertafel ergänzen',
     'regel': 'Eine ⟦Vierfeldertafel⟧ ordnet nach zwei Merkmalen. ⟦Zeilen- und Spaltensummen⟧ müssen stimmen; unten rechts steht die Gesamtzahl. Fehlende Felder durch Ergänzen zur Summe.',
     'schritte': ['200 Befragte, 80 haben Merkmal A, davon 30 auch Merkmal B.', 'A und nicht B: 80 − 30 = ⟦50⟧; nicht A: 200 − 80 = 120.'],
     'probe': '30 + 50 = 80 ✓',
     'fehler': 'Das Feld „A und nicht B“ als 200 − 30 zu berechnen ist falsch: Man ergänzt innerhalb der ⟦Zeile A⟧ zu deren Summe 80.'},
    {'lernziel': 'tafel_wkeit', 'titel': 'Wahrscheinlichkeiten aus der Tafel',
     'regel': 'Teilt man jede Anzahl durch die ⟦Gesamtzahl⟧, erhält man eine Vierfeldertafel mit Wahrscheinlichkeiten. ⟦P(A) = P(A ∩ B) + P(A ∩ B̄)⟧ (Randsumme).',
     'schritte': ['Gesamt 400, A und B: 60, A und nicht B: 100.', 'P(A ∩ B) = 60 : 400 = 0,15; P(A) = 160 : 400 = ⟦0,4⟧.'],
     'probe': '0,15 + 0,25 = 0,4 ✓',
     'fehler': 'P(A ∩ B) = 60 : 160 ist falsch, wenn nach der Wahrscheinlichkeit unter ⟦allen⟧ gefragt ist: Man teilt durch die ⟦Gesamtzahl⟧ 400.'},
    {'lernziel': 'additionssatz', 'titel': 'Der Additionssatz',
     'regel': '⟦P(A ∪ B) = P(A) + P(B) − P(A ∩ B)⟧. Die Schnittmenge wird einmal abgezogen, weil sie sonst ⟦doppelt gezählt⟧ würde. Sind A und B ⟦unvereinbar⟧ (A ∩ B = ∅), gilt P(A ∪ B) = P(A) + P(B).',
     'schritte': ['P(A) = 0,5, P(B) = 0,3, P(A ∩ B) = 0,1.', 'P(A ∪ B) = 0,5 + 0,3 − 0,1 = ⟦0,7⟧.'],
     'probe': 'P(Ā ∩ B̄) = 1 − 0,7 = 0,3 ≥ 0 ✓',
     'fehler': 'P(A ∪ B) = 0,5 + 0,3 = 0,8 ist falsch, wenn A und B gemeinsame Ergebnisse haben: Die ⟦Schnittmenge⟧ wurde doppelt gezählt.'},
    {'lernziel': 'bedingt', 'titel': 'Bedingte Wahrscheinlichkeit',
     'regel': '⟦P_B(A)⟧ ist die Wahrscheinlichkeit von A, ⟦wenn man schon weiß⟧, dass B eingetreten ist: ⟦P_B(A) = P(A ∩ B) : P(B)⟧. In der Tafel: nur die ⟦Spalte B⟧ betrachten.',
     'schritte': ['Von 50 Personen mit B haben 20 auch A.', 'P_B(A) = 20 : 50 = ⟦0,4⟧.'],
     'probe': 'Man teilt durch die Anzahl in B, nicht durch alle ✓',
     'fehler': 'P_B(A) und P_A(B) zu verwechseln ist ein häufiger Fehler: Die ⟦Bedingung⟧ (unten) bestimmt, ⟦durch welche Anzahl⟧ geteilt wird.'},
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
    art = R.choice({1: ['schnitt', 'gegen'], 2: ['schnitt', 'vereinigung', 'gegen'], 3: ['vereinigung', 'ohne', 'wort']}[s])
    vor = f'Aus den Zahlen 1 bis {N} wird zufällig eine gezogen. A: „Die Zahl ist {ta}.“ B: „Die Zahl ist {tb}.“'
    if art == 'wort':
        r = f'Die Zahl ist {ta} oder {tb} (oder beides).'
        return auswahl(vor + ' Was bedeutet das Ereignis A ∪ B?', r,
                       [f'Die Zahl ist {ta} und {tb}.', f'Die Zahl ist weder {ta} noch {tb}.', f'Die Zahl ist {ta}, aber nicht {tb}.'],
                       'A ∪ B: mindestens eines der Ereignisse tritt ein („oder“ im einschließenden Sinn).', '∪ steht für „oder“, ∩ für „und“.')
    if art == 'schnitt':
        M, name = [k for k in A if k in B], 'A ∩ B'
    elif art == 'vereinigung':
        M, name = sorted(set(A) | set(B)), 'A ∪ B'
    elif art == 'gegen':
        M, name = [k for k in om if k not in A], '„nicht A“'
    else:
        M, name = [k for k in A if k not in B], '„A, aber nicht B“'
    if not M or len(M) == N: return None
    p = Fr(len(M), N)
    zeig = ', '.join(map(str, M)) if len(M) <= 12 else f'{len(M)} Zahlen'
    return zahl(vor + f' Berechne P({name}) als Dezimalzahl.', f'{name}: {zeig}. P = {len(M)} : {N} = {dz(p)}.',
                {'schnitt': 'Welche Zahlen erfüllen beide Bedingungen?', 'vereinigung': 'Zähle alle, die mindestens eine Bedingung erfüllen – keine doppelt.',
                 'gegen': 'Gegenereignis: P(Ā) = 1 − P(A).', 'ohne': 'Nimm die Zahlen aus A und streiche die, die auch in B liegen.'}[art],
                p, f'{len(M)} / {N}')


def g_vierfeld(s):
    N = R.choice([100, 120, 150, 200, 250, 300, 400, 500])
    aa, ab, ba, bb = zufalls_tafel(N)
    szen, ma, mb = R.choice(SZEN)
    A_, B_ = aa + ab, aa + ba
    vor = f'Untersucht werden {dz(N)} {szen}. A: „{ma}“, B: „{mb}“.'
    if s == 1:
        if R.random() < 0.5:
            return zahl(vor + f' {dz(A_)} haben Merkmal A, davon {dz(aa)} auch Merkmal B. Wie viele haben A, aber nicht B?',
                        f'In der Zeile A stehen {dz(A_)} Fälle; davon haben {dz(aa)} auch B. A ohne B: {dz(A_)} − {dz(aa)} = {dz(ab)}.', 'Ergänze innerhalb der Zeile A zur Zeilensumme.', ab, f'{A_} - {aa}')
        return zahl(vor + f' {dz(A_)} haben Merkmal A. Wie viele haben Merkmal A nicht?', f'Nicht A = Gesamt − A = {dz(N)} − {dz(A_)} = {dz(N - A_)}.',
                    'Gesamtzahl minus Anzahl mit A.', N - A_, f'{N} - {A_}')
    if s == 2:
        return zahl(vor + f' {dz(A_)} haben A, {dz(B_)} haben B, {dz(aa)} haben beides. Wie viele haben weder A noch B?',
                    f'Nicht A: {dz(N - A_)}; davon mit B: {dz(B_)} − {dz(aa)} = {dz(ba)}; weder noch: {dz(N - A_)} − {dz(ba)} = {dz(bb)}.',
                    'Fülle die Tafel Schritt für Schritt: erst Randsummen, dann die inneren Felder.', bb, f'{N} - {A_} - ({B_} - {aa})')
    if R.random() < 0.5:
        return zahl(vor + f' {dz(ab)} haben A, aber nicht B; {dz(ba)} haben B, aber nicht A; {dz(bb)} haben keines der Merkmale. Wie viele haben beide Merkmale?',
                    f'Beide = Gesamt − die drei anderen Felder: {dz(N)} − {dz(ab)} − {dz(ba)} − {dz(bb)} = {dz(aa)}.', 'Die vier inneren Felder ergeben zusammen die Gesamtzahl.',
                    aa, f'{N} - {ab} - {ba} - {bb}')
    pa = Fr(A_, N)
    if not endlich(pa): return None
    return zahl(vor + f' {dz(pa * 100)} % haben A. Unter denen mit A haben {dz(aa)} auch B. Wie viele haben A, aber nicht B?',
                f'A: {dz(pa * 100)} % von {dz(N)} = {dz(A_)}; A ohne B: {dz(A_)} − {dz(aa)} = {dz(ab)}.', 'Rechne zuerst den Prozentsatz in eine Anzahl um.', ab,
                f'{N} * {cf(pa)} - {aa}')


def g_tafel_wkeit(s):
    N = R.choice([100, 200, 250, 400, 500, 1000])
    aa, ab, ba, bb = zufalls_tafel(N)
    t = tafel_text(aa, ab, ba, bb)
    frage = R.choice({1: ['ab', 'aa', 'bb'], 2: ['A', 'B', 'nA'], 3: ['vereinigung', 'genau', 'nAnB']}[s])
    if frage == 'aa': z, name, w = aa, 'A ∩ B', f'{dz(aa)} : {dz(N)}'
    elif frage == 'ab': z, name, w = ab, '„A und nicht B“', f'{dz(ab)} : {dz(N)}'
    elif frage == 'bb': z, name, w = bb, '„weder A noch B“', f'{dz(bb)} : {dz(N)}'
    elif frage == 'A': z, name, w = aa + ab, 'A', f'({dz(aa)} + {dz(ab)}) : {dz(N)}'
    elif frage == 'B': z, name, w = aa + ba, 'B', f'({dz(aa)} + {dz(ba)}) : {dz(N)}'
    elif frage == 'nA': z, name, w = ba + bb, '„nicht A“', f'({dz(ba)} + {dz(bb)}) : {dz(N)}'
    elif frage == 'vereinigung': z, name, w = aa + ab + ba, 'A ∪ B', f'({dz(aa)} + {dz(ab)} + {dz(ba)}) : {dz(N)}'
    elif frage == 'genau': z, name, w = ab + ba, '„genau eines von A und B“', f'({dz(ab)} + {dz(ba)}) : {dz(N)}'
    else: z, name, w = N - bb, '„mindestens eines von A und B“', f'1 − {dz(bb)} : {dz(N)}'
    p = Fr(z, N)
    return zahl(f'{t} Gesamt: {dz(N)}. Eine Person/ein Fall wird zufällig ausgewählt. Berechne P({name}) als Dezimalzahl.',
                f'P = {w} = {dz(p)}.', 'Welche Felder gehören zum Ereignis? Teile ihre Summe durch die Gesamtzahl.', p, f'{z} / {N}')


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
    for _ in range(50):
        N = R.choice([100, 200, 400, 500])
        aa, ab, ba, bb = zufalls_tafel(N)
        B_ = aa + ba
        A_ = aa + ab
        kurz = lambda q: endlich(q) and 1000 % q.denominator == 0  # noqa: E731
        if s == 1:
            if kurz(Fr(aa, B_)): break
        else:
            if kurz(Fr(aa, B_)) and kurz(Fr(aa, A_)): break
    else:
        return None
    t = tafel_text(aa, ab, ba, bb)
    if s == 1:
        return zahl(f'{t} Berechne P_B(A), also die Wahrscheinlichkeit für A unter der Bedingung B.',
                    f'Nur Spalte B betrachten: {dz(B_)} Fälle, davon {dz(aa)} mit A. P_B(A) = {dz(aa)} : {dz(B_)} = {dz(Fr(aa, B_))}.',
                    'Teile durch die Anzahl in der Bedingung B, nicht durch alle.', Fr(aa, B_), f'{aa} / ({aa} + {ba})')
    if s == 2:
        return zahl(f'{t} Berechne P_A(B).', f'Nur Zeile A: {dz(A_)} Fälle, davon {dz(aa)} mit B. P_A(B) = {dz(aa)} : {dz(A_)} = {dz(Fr(aa, A_))}.',
                    'Die Bedingung steht unten: hier A.', Fr(aa, A_), f'{aa} / ({aa} + {ab})')
    pb = Fr(R.choice([2, 4, 5, 6, 8]), 10)
    pab = pb * Fr(R.choice([1, 2, 3, 4]), 4)
    if pab >= pb: return None
    q = pab / pb
    return zahl(f'Es gilt P(B) = {dz(pb)} und P(A ∩ B) = {dz(pab)}. Berechne P_B(A).', f'P_B(A) = P(A ∩ B) : P(B) = {dz(pab)} : {dz(pb)} = {dz(q)}.',
                'Formel für die bedingte Wahrscheinlichkeit.', q, f'{cf(pab)} / {cf(pb)}')


def g_verstehen(s):
    typ = R.choice({1: 'ab', 2: 'abcd', 3: 'cde'}[s])
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
          offen=['Lernkarten „vierfeld“, „tafel_wkeit“ und „bedingt“ brauchen eine Tabellen-Darstellung: Die Vierfeldertafel steht bisher als Aufzählung im Fragetext. Lernkarte „verknuepfen“ würde von einem Venn-Diagramm profitieren. Beides kann die App noch nicht zeichnen.',
                 'Bedingte Wahrscheinlichkeit P_B(A) ist im „umfang“ genannt, im LehrplanPLUS der 9. Klasse aber nicht ausdrücklich; Lernkarte „bedingt“ deshalb als Vertiefung (nicht Pflicht) markiert. Schreibweise P_B(A) im Text (Tiefstellung nicht möglich).',
                 'Ā und B̄ stehen nur in Erklärungen; in Aufgaben wird „nicht A“ ausgeschrieben, weil das Zeichen B̄ (kombinierender Strich) nicht überall sauber dargestellt wird.'])
