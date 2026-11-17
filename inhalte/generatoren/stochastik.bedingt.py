#!/usr/bin/env python3
"""Thema stochastik.bedingt – Bedingte Wahrscheinlichkeit (IB MYP 4 Extended, etwa Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403
from _rsib2 import PLAN2, art3  # noqa: E402

start(8204)

# Gesamtheit, A, nicht A, B, nicht B, Einzelner
SZEN = [
    ('Schülerinnen und Schüler', 'Brille', 'keine Brille', 'Fahrrad', 'kein Fahrrad', 'ein Kind'),
    ('Besucher eines Kinos', 'Erwachsene', 'Kinder', 'Popcorn gekauft', 'kein Popcorn', 'ein Besucher'),
    ('Mitglieder eines Sportvereins', 'Fußball', 'andere Sportart', 'unter 18', 'ab 18', 'ein Mitglied'),
    ('Fahrgäste eines Busses', 'Monatskarte', 'Einzelticket', 'pendelt täglich', 'pendelt nicht täglich', 'ein Fahrgast'),
    ('Befragte einer Umfrage', 'liest E-Books', 'liest keine E-Books', 'unter 30', 'ab 30', 'eine befragte Person'),
]


def tafel_bild(aa, ab, ba, bb, A, nA, B, nB, frage=None):
    w = {'aa': aa, 'ab': ab, 'ba': ba, 'bb': bb}
    z = lambda k: '?' if k == frage else dz(w[k])  # noqa: E731
    return {'typ': 'tabelle', 'kopf': ['', B, nB, 'Summe'],
            'zeilen': [[A, z('aa'), z('ab'), dz(aa + ab)], [nA, z('ba'), z('bb'), dz(ba + bb)], ['Summe', dz(aa + ba), dz(ab + bb), dz(aa + ab + ba + bb)]]}


def zuf_tafel(N):
    while True:
        cuts = sorted(R.sample(range(1, N), 3))
        t = [cuts[0], cuts[1] - cuts[0], cuts[2] - cuts[1], N - cuts[2]]
        if min(t) >= max(3, N // 20): return t


def bruch_oder_dez(text, q, w, h, c):
    q = Fr(q)
    if endlich(q) and (q * 1000).denominator == 1 and R.random() < .5:
        return zahl(text + ' Gib das Ergebnis als Dezimalzahl an.', w, h, q, c)
    return bruch_luecke(text + ' Gib das Ergebnis als gekürzten Bruch an.', q, w, h, c=[str(q.numerator), str(q.denominator)])


ETAPPEN = [
    {'lernziel': 'tafel', 'titel': 'P(A | B) aus der Vierfeldertafel',
     'regel': '⟦P(A | B)⟧ (lies: „A unter der Bedingung B“, conditional probability) ist die Wahrscheinlichkeit von A, ⟦wenn man schon weiß⟧, dass B eingetreten ist. In der Tafel betrachtest du nur die ⟦Spalte (oder Zeile) von B⟧: P(A | B) = Anzahl „A und B“ : ⟦Anzahl B⟧.',
     'schritte': ['200 Kinder; 50 fahren Rad, davon tragen 20 eine Brille.', 'Bedingung „fährt Rad“: Nur die 50 Radfahrer zählen.', 'P(Brille | Rad) = 20 : 50 = ⟦0,4⟧.'],
     'probe': 'Geteilt wird durch die Spaltensumme 50, nicht durch 200 ✓',
     'bild': {'typ': 'tabelle', 'kopf': ['', 'Rad', 'kein Rad', 'Summe'], 'zeilen': [['Brille', '20', '40', '60'], ['keine Brille', '30', '110', '140'], ['Summe', '50', '150', '200']]},
     'fehler': 'P(Brille | Rad) = 20 : 200 = 0,1 ist falsch: Das ist P(Brille ∩ Rad). Unter der Bedingung „Rad“ teilt man durch die ⟦Anzahl der Radfahrer⟧ (50).'},
    {'lernziel': 'formel', 'titel': 'Die Formel P(A | B)',
     'regel': 'Mit Wahrscheinlichkeiten gilt: ⟦P(A | B) = P(A ∩ B) : P(B)⟧. Umgestellt: ⟦P(A ∩ B) = P(B) · P(A | B)⟧ – die Multiplikationsregel.',
     'schritte': ['P(B) = 0,4 und P(A ∩ B) = 0,1.', 'P(A | B) = 0,1 : 0,4 = ⟦0,25⟧.'],
     'probe': '0,4 · 0,25 = 0,1 ✓',
     'fehler': 'P(A | B) = 0,1 · 0,4 = 0,04 ist falsch: Für die bedingte Wahrscheinlichkeit wird ⟦geteilt⟧, nicht multipliziert. Multipliziert wird nur für P(A ∩ B).'},
    {'lernziel': 'baum', 'titel': 'Ziehen ohne Zurücklegen',
     'regel': 'Beim Ziehen ⟦ohne Zurücklegen⟧ ändern sich die Wahrscheinlichkeiten auf der zweiten Stufe: Es ist eine Kugel weniger da. Die Äste der zweiten Stufe sind ⟦bedingte Wahrscheinlichkeiten⟧. Pfadwahrscheinlichkeit: ⟦entlang des Pfades multiplizieren⟧.',
     'schritte': ['Urne: 3 rote, 2 blaue Kugeln. Zwei Züge ohne Zurücklegen.', 'P(1. rot) = 3/5. Danach 2 rote von 4: P(2. rot | 1. rot) = 2/4.', 'P(rot, rot) = 3/5 · 2/4 = ⟦3/10⟧.'],
     'probe': 'Alle vier Pfade: 6/20 + 6/20 + 6/20 + 2/20 = 1 ✓',
     'bild': {'typ': 'baum', 'aeste': [{'text': 'rot', 'p': '3/5', 'aeste': [{'text': 'rot', 'p': '2/4'}, {'text': 'blau', 'p': '2/4'}]},
                                       {'text': 'blau', 'p': '2/5', 'aeste': [{'text': 'rot', 'p': '3/4'}, {'text': 'blau', 'p': '1/4'}]}]},
     'fehler': 'P(rot, rot) = 3/5 · 3/5 ist falsch, wenn ⟦nicht zurückgelegt⟧ wird: Beim zweiten Zug sind nur noch 2 rote von 4 Kugeln da.'},
    {'lernziel': 'unabhaengig', 'titel': 'Abhängig oder unabhängig?',
     'regel': 'A und B sind ⟦unabhängig⟧ (independent), wenn das Wissen über B die Wahrscheinlichkeit von A nicht ändert: ⟦P(A | B) = P(A)⟧. Gleichwertig: ⟦P(A ∩ B) = P(A) · P(B)⟧. Sonst sind sie ⟦abhängig⟧.',
     'schritte': ['P(A) = 0,5, P(B) = 0,4, P(A ∩ B) = 0,2.', 'P(A) · P(B) = 0,5 · 0,4 = 0,2 = P(A ∩ B).', 'Also sind A und B ⟦unabhängig⟧.'],
     'probe': 'P(A | B) = 0,2 : 0,4 = 0,5 = P(A) ✓',
     'fehler': '„A und B schließen sich aus, also sind sie unabhängig“ ist falsch: Wenn A eintritt, ⟦kann B nicht mehr eintreten⟧ – das Wissen ändert P(B) auf 0. Unvereinbare Ereignisse (mit P > 0) sind ⟦abhängig⟧.'},
    {'lernziel': 'rueckschluss', 'titel': 'Rückschlüsse mit 1000 Fällen',
     'regel': 'Fragt man „umgekehrt“ (z. B. P(krank | Test positiv)), hilft es, sich ⟦1 000 Fälle⟧ vorzustellen: erst nach der ersten Stufe aufteilen, dann nach der zweiten. Dann ⟦nur die Fälle mit der Bedingung⟧ zählen.',
     'schritte': ['10 % von 1 000 Geräten sind defekt: 100 defekt, 900 in Ordnung. Ein Prüfgerät meldet (2. Stufe „ja“) 90 % der defekten (90) und irrtümlich 5 % der guten (45).',
                  'Gemeldet werden 90 + 45 = 135 Geräte.', 'P(defekt | gemeldet) = 90 : 135 = ⟦2/3⟧ ≈ 0,67.'],
     'probe': '90 + 10 = 100 defekte, 45 + 855 = 900 gute ✓',
     'bild': {'typ': 'baum', 'aeste': [{'text': 'defekt (100)', 'p': '0,1', 'aeste': [{'text': 'ja', 'p': '0,9'}, {'text': 'nein', 'p': '0,1'}]},
                                       {'text': 'ok (900)', 'p': '0,9', 'aeste': [{'text': 'ja', 'p': '0,05'}, {'text': 'nein', 'p': '0,95'}]}]},
     'fehler': 'P(defekt | gemeldet) = 0,9 ist falsch: 0,9 ist P(gemeldet | defekt). Die Bedingung ⟦vertauscht⟧ zu haben ist der häufigste Fehler – unter allen ⟦gemeldeten⟧ Geräten sind auch 45 gute.'},
    {'lernziel': 'verstehen', 'titel': 'Bedingungen richtig lesen',
     'regel': 'Achte darauf, ⟦was gegeben ist⟧ (die Bedingung, hinter dem Strich) und ⟦was gefragt ist⟧ (vor dem Strich). ⟦P(A | B) und P(B | A)⟧ sind meist verschieden, weil durch verschiedene Gruppen geteilt wird.',
     'schritte': ['„70 % der Hundebesitzer gehen täglich spazieren.“', 'Das ist ⟦P(spazieren | Hund) = 0,7⟧ – nicht P(Hund | spazieren).'],
     'probe': 'Bedingung „Hundebesitzer“ steht hinter dem Strich ✓',
     'fehler': '„90 % der Lottogewinner haben Lotto gespielt, also gewinnt man beim Spielen mit 90 %“ ist falsch: Das verwechselt ⟦P(gespielt | gewonnen)⟧ mit ⟦P(gewonnen | gespielt)⟧.'},
]


def g_tafel(s):
    N = R.choice([100, 200, 400, 500]) if s < 3 else R.choice([120, 240, 300, 600])
    aa, ab, ba, bb = zuf_tafel(N)
    G, A, nA, B, nB, ein = R.choice(SZEN)
    bild = tafel_bild(aa, ab, ba, bb, A, nA, B, nB)
    art = R.choice({1: ['AgB', 'BgA'], 2: ['nAgB', 'AgnB', 'nAgnB', 'luecke'], 3: ['luecke', 'vergleich', 'nAgnB']}[s])  # Durchsicht 19: Stufe 2 = Gegenteil als Bedingung / fehlendes Feld
    vor = f'Die Vierfeldertafel zeigt {dz(N)} {G}.'
    if art in ('AgB', 'BgA', 'nAgB', 'AgnB', 'nAgnB'):
        zael, nenn, bed, ziel = {'AgB': (aa, aa + ba, B, A), 'BgA': (aa, aa + ab, A, B), 'nAgB': (ba, aa + ba, B, nA),
                                 'AgnB': (ab, ab + bb, nB, A), 'nAgnB': (bb, ab + bb, nB, nA)}[art]
        q = Fr(zael, nenn)
        return mit_grafik(bruch_oder_dez(f'{vor} Berechne P({ziel} | {bed}).', q,
                                         f'Bedingung „{bed}“: nur diese {dz(nenn)} zählen. Davon „{ziel}“: {dz(zael)}. P = {dz(zael)} : {dz(nenn)}' + (f' = {br(q)}' if q.denominator != nenn else '') + (f' = {dz(q)}.' if endlich(q) and (q * 1000).denominator == 1 else '.'),
                                         'Hinter dem Strich steht die Bedingung – durch deren Summe wird geteilt.', f'{zael} / {nenn}'), bild)
    if art == 'luecke':
        bild = tafel_bild(aa, ab, ba, bb, A, nA, B, nB, frage='aa')
        q = Fr(aa, aa + ba)
        return mit_grafik(bruch_oder_dez(f'{vor} Ein Feld fehlt. Berechne P({A} | {B}).', q,
                                         f'Fehlendes Feld: {dz(aa + ab)} − {dz(ab)} = {dz(aa)}. P({A} | {B}) = {dz(aa)} : {dz(aa + ba)} = {br(q)}.',
                                         'Ergänze zuerst das fehlende Feld über die Zeilensumme.', f'({aa + ab} - {ab}) / {aa + ba}'), bild)
    p1, p2 = Fr(aa, aa + ba), Fr(aa, aa + ab)
    if p1 == p2: return None
    r = f'P({A} | {B})' if p1 > p2 else f'P({B} | {A})'
    return mit_grafik(auswahl(f'{vor} Welche Wahrscheinlichkeit ist größer?', r, [f'P({A} | {B})', f'P({B} | {A})', 'Beide sind gleich'],
                              f'P({A} | {B}) = {dz(aa)} : {dz(aa + ba)} ≈ {dz(round(float(p1), 3))}; P({B} | {A}) = {dz(aa)} : {dz(aa + ab)} ≈ {dz(round(float(p2), 3))}.',
                              'Gleicher Zähler (A und B), aber verschiedene Nenner: Welche Summe ist kleiner?'), bild)


def g_formel(s):
    for _ in range(100):
        pB = Fr(R.randint(1, 9), 10) if s == 1 else Fr(R.choice([2, 4, 5, 8, 25, 40, 50, 60, 75, 80]), 100)
        q = Fr(R.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]), 10) if s < 3 else Fr(R.choice([1, 2, 3, 4, 5, 6, 8, 9, 15, 25, 75]), R.choice([10, 20, 100]))
        pAB = pB * q
        if 0 < q < 1 and endlich(pAB) and endlich(q) and pAB.denominator <= 1000: break
    art = R.choice({1: ['bedingt'], 2: ['bedingt', 'schnitt'], 3: ['bedingt_gegen', 'rueck_pB', 'schnitt_prozent']}[s])
    if art == 'bedingt':
        return zahl(f'P(B) = {dz(pB)}, P(A ∩ B) = {dz(pAB)}. Berechne P(A | B).', f'P(A | B) = {dz(pAB)} : {dz(pB)} = {dz(q)}.',
                    'P(A | B) = P(A ∩ B) : P(B).', q, f'{float(pAB)} / {float(pB)}')
    if art == 'schnitt':
        return zahl(f'P(B) = {dz(pB)}, P(A | B) = {dz(q)}. Berechne P(A ∩ B).', f'P(A ∩ B) = P(B) · P(A | B) = {dz(pB)} · {dz(q)} = {dz(pAB)}.',
                    'Multiplikationsregel: P(A ∩ B) = P(B) · P(A | B).', pAB, f'{float(pB)} * {float(q)}')
    if art == 'bedingt_gegen':
        return zahl(f'P(B) = {dz(pB)}, P(A ∩ B) = {dz(pAB)}. Berechne P(nicht A | B).', f'P(A | B) = {dz(pAB)} : {dz(pB)} = {dz(q)}. P(nicht A | B) = 1 − {dz(q)} = {dz(1 - q)}.',
                    'Unter derselben Bedingung ergänzen sich A und nicht A zu 1.', 1 - q, f'1 - {float(pAB)} / {float(pB)}')
    if art == 'rueck_pB':
        return zahl(f'P(A ∩ B) = {dz(pAB)} und P(A | B) = {dz(q)}. Berechne P(B).', f'P(A ∩ B) = P(B) · P(A | B) ⇒ P(B) = {dz(pAB)} : {dz(q)} = {dz(pB)}.',
                    'Stelle die Multiplikationsregel nach P(B) um.', pB, f'{float(pAB)} / {float(q)}')
    pz_ = int(pB * 100)
    qz = q * 100
    if not endlich(qz): return None
    return zahl(f'{pz_} % der Gäste eines Hotels sind Familien. Von den Familien buchen {dz(qz)} % ein Zimmer mit Balkon. Wie groß ist die Wahrscheinlichkeit, dass ein zufälliger Gast eine Familie ist und mit Balkon bucht? (Dezimalzahl)',
                f'P(Familie ∩ Balkon) = P(Familie) · P(Balkon | Familie) = {dz(pB)} · {dz(q)} = {dz(pAB)}.',
                'Die Prozentangabe „von den Familien“ ist eine bedingte Wahrscheinlichkeit.', pAB, f'{float(pB)} * {float(q)}')


def g_baum(s):
    r, b = R.randint(2, 7), R.randint(2, 7)
    n = r + b
    f1, f2 = R.choice([('rot', 'blau'), ('grün', 'gelb'), ('weiß', 'schwarz')])
    art = R.choice({1: ['zweite', 'rr', 'bb'], 2: ['rb', 'zweite_b', 'verschieden', 'gleich'], 3: ['verschieden', 'mind_eine', 'gleich']}[s])  # Durchsicht 19
    vor = f'In einer Urne liegen {r} {f1}e und {b} {f2}e Kugeln. Es werden zwei Kugeln ohne Zurücklegen gezogen.'
    bild = {'typ': 'baum', 'aeste': [{'text': f1, 'p': f'{r}/{n}', 'aeste': [{'text': f1, 'p': f'{r - 1}/{n - 1}'}, {'text': f2, 'p': f'{b}/{n - 1}'}]},
                                     {'text': f2, 'p': f'{b}/{n}', 'aeste': [{'text': f1, 'p': f'{r}/{n - 1}'}, {'text': f2, 'p': f'{b - 1}/{n - 1}'}]}]}
    if s < 3: bild = None if R.random() < .5 else bild
    rr, rb, br_, bb = Fr(r * (r - 1), n * (n - 1)), Fr(r * b, n * (n - 1)), Fr(b * r, n * (n - 1)), Fr(b * (b - 1), n * (n - 1))
    h = 'Nach dem ersten Zug ist eine Kugel weniger in der Urne.'
    if art == 'zweite':
        return mit_grafik(bruch_luecke(vor + f' Die erste Kugel ist {f1}. Wie groß ist P(2. Kugel {f1} | 1. Kugel {f1})?', Fr(r - 1, n - 1),
                                       f'Übrig: {r - 1} {f1}e von {n - 1} Kugeln. P = {r - 1}/{n - 1}' + (f' = {br(Fr(r - 1, n - 1))}.' if Fr(r - 1, n - 1).denominator != n - 1 else '.'),
                                       h, c=[str(Fr(r - 1, n - 1).numerator), str(Fr(r - 1, n - 1).denominator)]), bild)
    if art == 'zweite_b':
        q = Fr(b, n - 1)
        return mit_grafik(bruch_luecke(vor + f' Die erste Kugel ist {f1}. Wie groß ist P(2. Kugel {f2} | 1. Kugel {f1})?', q,
                                       f'Alle {b} {f2}en sind noch da, aber nur noch {n - 1} Kugeln insgesamt: P = {b}/{n - 1}' + (f' = {br(q)}.' if q.denominator != n - 1 else '.'), h,
                                       c=[str(q.numerator), str(q.denominator)]), bild)
    pfad = {'rr': (rr, f'zweimal {f1}', f'{r}/{n} · {r - 1}/{n - 1}'), 'bb': (bb, f'zweimal {f2}', f'{b}/{n} · {b - 1}/{n - 1}'),
            'rb': (rb, f'erst {f1}, dann {f2}', f'{r}/{n} · {b}/{n - 1}')}
    if art in pfad:
        q, wort, rech = pfad[art]
        return mit_grafik(bruch_luecke(vor + f' Berechne P({wort}).', q, f'P = {rech} = {br(q)}.', 'Multipliziere die Wahrscheinlichkeiten entlang des Pfades.',
                                       c=[str(q.numerator), str(q.denominator)]), bild)
    if art == 'verschieden':
        q = rb + br_
        return mit_grafik(bruch_luecke(vor + ' Berechne die Wahrscheinlichkeit, zwei verschiedenfarbige Kugeln zu ziehen.', q,
                                       f'Zwei Pfade: {r}/{n} · {b}/{n - 1} + {b}/{n} · {r}/{n - 1} = {br(rb)} + {br(br_)} = {br(q)}.',
                                       'Welche Pfade passen? Pfade addieren, entlang eines Pfades multiplizieren.', c=[str(q.numerator), str(q.denominator)]), bild)
    if art == 'mind_eine':
        q = 1 - bb
        return mit_grafik(bruch_luecke(vor + f' Berechne die Wahrscheinlichkeit, mindestens eine {f1}e Kugel zu ziehen.', q,
                                       f'Gegenereignis: zweimal {f2}: {b}/{n} · {b - 1}/{n - 1} = {br(bb)}. P = 1 − {br(bb)} = {br(q)}.',
                                       '„Mindestens eine“: Rechne mit dem Gegenereignis.', c=[str(q.numerator), str(q.denominator)]), bild)
    q = rr + bb
    return mit_grafik(bruch_luecke(vor + ' Berechne die Wahrscheinlichkeit, zwei gleichfarbige Kugeln zu ziehen.', q,
                                   f'P({f1}, {f1}) + P({f2}, {f2}) = {br(rr)} + {br(bb)} = {br(q)}.', 'Zwei Pfade gehören dazu.',
                                   c=[str(q.numerator), str(q.denominator)]), bild)


def g_unabhaengig(s):
    art = R.choice({1: ['schnitt_rechnen', 'pruefen'], 2: ['pruefen', 'tafel', 'schnitt_rechnen'], 3: ['tafel', 'ausschluss', 'muenze', 'bedingt_gleich']}[s])
    if art == 'schnitt_rechnen':
        a, b = Fr(R.randint(1, 9), 10), Fr(R.randint(1, 9), 10)
        return zahl(f'A und B sind unabhängig. P(A) = {dz(a)}, P(B) = {dz(b)}. Berechne P(A ∩ B).', f'Unabhängig: P(A ∩ B) = P(A) · P(B) = {dz(a)} · {dz(b)} = {dz(a * b)}.',
                    'Bei unabhängigen Ereignissen darf man die Einzelwahrscheinlichkeiten multiplizieren.', a * b, f'{float(a)} * {float(b)}')
    if art == 'pruefen':
        a, b = Fr(R.randint(1, 9), 10), Fr(R.randint(1, 9), 10)
        un = R.random() < .5
        ab = a * b if un else a * b + Fr(R.choice([-1, 1]) * R.randint(1, 5), 100)
        if not 0 < ab < min(a, b): return None
        return ja_nein(f'P(A) = {dz(a)}, P(B) = {dz(b)}, P(A ∩ B) = {dz(ab)}. Sind A und B unabhängig?', un,
                       f'P(A) · P(B) = {dz(a * b)}' + (' = P(A ∩ B): unabhängig.' if un else f' ≠ {dz(ab)}: abhängig.'),
                       'Vergleiche P(A ∩ B) mit P(A) · P(B).')
    if art == 'tafel':
        G, A, nA, B, nB, ein = R.choice(SZEN)
        N = R.choice([100, 200, 400])
        un = AKT['nr'] % 2 == 0  # Durchsicht 19: abwechselnd, vorher meist „unabhängig“ (Wiederholungen bevorzugten den einfachen Fall)
        for _ in range(200):
            pa, pb = Fr(R.randint(2, 8), 10), Fr(R.randint(2, 8), 10)
            aa = pa * pb * N
            if un and aa.denominator == 1: aa = int(aa); break
            if not un:
                aa = int(pa * pb * N) + R.choice([-12, -8, 8, 12])
                if aa > 0 and aa < min(pa, pb) * N: break
        else:
            return None
        ab, ba = int(pa * N) - aa, int(pb * N) - aa
        bb = N - aa - ab - ba
        if min(ab, ba, bb) <= 0: return None
        bild = tafel_bild(aa, ab, ba, bb, A, nA, B, nB)
        return mit_grafik(ja_nein(f'Die Vierfeldertafel zeigt {N} {G}. Sind die Merkmale „{A}“ und „{B}“ unabhängig?', un,
                                  f'P({A}) = {dz(pa)}, P({A} | {B}) = {aa} : {aa + ba} = {dz(Fr(aa, aa + ba)) if endlich(Fr(aa, aa + ba)) else br(Fr(aa, aa + ba))}. ' +
                                  ('Gleich: unabhängig.' if un else 'Verschieden: abhängig.'),
                                  f'Vergleiche den Anteil „{A}“ unter allen mit dem Anteil „{A}“ in der Spalte „{B}“.'), bild)
    if art == 'ausschluss':
        a, b = Fr(R.randint(1, 4), 10), Fr(R.randint(1, 4), 10)
        r = 'Abhängig: Tritt A ein, kann B nicht mehr eintreten.'
        return auswahl(f'A und B schließen sich aus (A ∩ B = ∅), P(A) = {dz(a)}, P(B) = {dz(b)}. Sind A und B unabhängig?', r,
                       ['Unabhängig: Sie haben ja nichts miteinander zu tun.', 'Unabhängig, weil P(A ∩ B) = 0 ist.', 'Das kann man ohne weitere Angaben nicht sagen.'],
                       f'P(A ∩ B) = 0, aber P(A) · P(B) = {dz(a * b)} ≠ 0. Also abhängig.', 'Vergleiche P(A ∩ B) = 0 mit P(A) · P(B).')
    if art == 'muenze':
        k = R.randint(3, 6)
        r = '1/2 – die Münze hat kein Gedächtnis.'
        return auswahl(f'Eine faire Münze zeigte {k}-mal hintereinander Kopf. Wie groß ist die Wahrscheinlichkeit, dass der nächste Wurf Kopf zeigt?', r,
                       [f'1/{2 ** (k + 1)}', 'kleiner als 1/2, Zahl ist jetzt fällig', 'größer als 1/2, Kopf ist gerade dran'],
                       'Die Würfe sind unabhängig. P(Kopf | vorher Kopf-Serie) = P(Kopf) = 1/2.',
                       'Hängt der nächste Wurf von den vorherigen ab?')
    a = Fr(R.randint(2, 8), 10)
    return zahl(f'A und B sind unabhängig, P(A) = {dz(a)} und P(B) = {dz(Fr(R.randint(2, 8), 10))}. Wie groß ist P(A | B)?',
                f'Unabhängig heißt: Das Wissen über B ändert nichts. P(A | B) = P(A) = {dz(a)}.', 'Was bedeutet „unabhängig“ für die bedingte Wahrscheinlichkeit?',
                a, f'{float(a)}')


EIN = {'Geräte': 'Ein Gerät', 'Pflanzen': 'Eine Pflanze', 'E-Mails': 'Eine E-Mail'}


def g_rueckschluss(s):
    for _ in range(200):
        pk = R.choice([1, 2, 5, 10, 20]) if s == 3 else R.choice([10, 20, 25, 40, 50])     # Prozent
        se = R.choice([80, 90, 95, 100])
        fp = R.choice([5, 10, 20])
        N = 1000
        k = N * pk // 100
        tp = k * se // 100
        f = (N - k) * fp // 100
        if k * se % 100 == 0 and (N - k) * fp % 100 == 0 and tp + f > 0: break
    ctx = R.choice([('Geräte', 'defekt', 'in Ordnung', 'Ein Prüfgerät meldet', 'gemeldet', 'defekt', 'ok', 'Alarm'),
                    ('Pflanzen', 'von Schädlingen befallen', 'gesund', 'Ein Schnelltest erkennt', 'als befallen erkannt', 'befallen', 'gesund', 'Alarm'),
                    ('E-Mails', 'Spam', 'kein Spam', 'Ein Filter markiert', 'markiert', 'Spam', 'kein Spam', 'markiert')])
    D, K, G, T, T2, KK, GK, TK = ctx
    vor = f'{pk} % der {D} sind {K}. {T} {se} % dieser {D}, aber irrtümlich auch {fp} % der übrigen. Stelle dir {dz(N)} {D} vor.'
    art = R.choice({1: ['anzahl_k', 'anzahl_tp'], 2: ['anzahl_pos', 'anzahl_tp', 'anzahl_f'], 3: ['bayes', 'bayes', 'vergleich']}[s])
    if art == 'anzahl_k':
        return zahl(vor + f' Wie viele davon sind {K}?', f'{pk} % von {dz(N)} = {dz(k)}.', 'Prozent von 1 000 berechnen.', k, f'{N} * {pk} / 100')
    if art == 'anzahl_tp':
        return zahl(vor + f' Wie viele {D} sind {K} und werden {T2}?', f'{K[0].upper() + K[1:]}: {dz(k)}. Davon {se} %: {dz(tp)}.', 'Erst die Gruppe bestimmen, dann den Prozentsatz davon.',
                    tp, f'{N} * {pk} / 100 * {se} / 100')
    if art == 'anzahl_f':
        return zahl(vor + f' Wie viele {D} sind {G}, werden aber trotzdem {T2}?', f'{G[0].upper() + G[1:]}: {dz(N - k)}. Davon {fp} %: {dz(f)}.',
                    'Wie viele sind nicht betroffen? Davon den Fehler-Prozentsatz.', f, f'({N} - {N} * {pk} / 100) * {fp} / 100')
    if art == 'anzahl_pos':
        return zahl(vor + f' Wie viele {D} werden insgesamt {T2}?', f'Richtig {T2}: {dz(tp)}; irrtümlich {T2}: {dz(f)}. Zusammen {dz(tp + f)}.',
                    'Addiere beide Gruppen, die ein Signal bekommen.', tp + f, f'{tp} + {f}')
    q = Fr(tp, tp + f)
    if art == 'bayes':
        bild = {'typ': 'baum', 'aeste': [{'text': f'{KK} ({k})', 'p': dz(Fr(pk, 100)), 'aeste': [{'text': 'ja', 'p': dz(Fr(se, 100))}, {'text': 'nein', 'p': dz(1 - Fr(se, 100))}]},
                                         {'text': f'{GK} ({N - k})', 'p': dz(1 - Fr(pk, 100)), 'aeste': [{'text': 'ja', 'p': dz(Fr(fp, 100))}, {'text': 'nein', 'p': dz(1 - Fr(fp, 100))}]}]}
        return mit_grafik(bruch_luecke(vor + f' {EIN[D]} wurde {T2}. Wie groß ist die Wahrscheinlichkeit, dass {"sie" if D != "Geräte" else "es"} wirklich {K} ist? Gib einen gekürzten Bruch an. (Im Baum: 2. Stufe „ja“ = {T2}.)', q,
                                       f'{T2.capitalize()}: {dz(tp)} + {dz(f)} = {dz(tp + f)}. Davon wirklich {K}: {dz(tp)}. P = {dz(tp)}/{dz(tp + f)}' + (f' = {br(q)}' if q.denominator != tp + f else '') + f' ≈ {dz(round(float(q), 2))}.',
                                       f'Bedingung „{T2}“: Zähle alle {T2}en und davon die wirklich {K}en.', c=[str(q.numerator), str(q.denominator)]), bild)
    r = f'Kleiner: P({K} | {T2}) ≈ {dz(round(float(q), 2))}' if q < Fr(se, 100) else f'Größer oder gleich: ≈ {dz(round(float(q), 2))}'
    return auswahl(vor + f' Ist P({K} | {T2}) größer oder kleiner als {se} %?', r,
                   [f'Genau {se} %, das steht ja in der Aufgabe.', f'Kleiner: P({K} | {T2}) ≈ {dz(round(float(q), 2))}', f'Größer oder gleich: ≈ {dz(round(float(q), 2))}', f'Genau {pk} %.'],
                   f'{se} % ist P({T2} | {K}). Umgekehrt: {dz(tp)} von {dz(tp + f)} {T2}en sind {K}, also ≈ {dz(round(float(q), 2))}.',
                   'Unterscheide P(Signal | betroffen) und P(betroffen | Signal).')


SAETZE = [  # (Satz, Gesamtheit/Bedingung, Gefragtes)
    ('60 % der Radfahrer tragen einen Helm.', 'Helm', 'Radfahrer'),
    ('Von den Gewinnern des Turniers haben 80 % täglich trainiert.', 'täglich trainiert', 'Gewinner'),
    ('Unter den Kunden mit Kundenkarte zahlen 40 % mit dem Handy.', 'zahlt mit dem Handy', 'Kundenkarte'),
    ('90 % der Hundebesitzer gehen täglich spazieren.', 'geht täglich spazieren', 'Hundebesitzer'),
    ('Von den Schülern mit Note 1 lesen 75 % regelmäßig.', 'liest regelmäßig', 'Note 1'),
    ('30 % der Pendler, die mit dem Zug fahren, kommen zu spät.', 'kommt zu spät', 'fährt Zug'),
    ('Von den verspäteten Flügen fanden 70 % bei Schnee statt.', 'Schnee', 'verspätet'),
]


def g_verstehen(s):
    art = R.choice({1: ['notation'], 2: ['notation', 'aussage', 'gleich'], 3: ['aussage', 'tausch', 'gleich', 'groesser']}[s])
    if art == 'notation':
        satz, A, B = R.choice(SAETZE)
        pr = satz.split('%')[0].split()[-1]
        rr = f'P({A} | {B}) = {dz(Fr(int(pr), 100))}'
        return auswahl(f'„{satz}“ Wie schreibt man das als Wahrscheinlichkeit?', rr,
                       [f'P({B} | {A}) = {dz(Fr(int(pr), 100))}', f'P({A} ∩ {B}) = {dz(Fr(int(pr), 100))}', f'P({A}) = {dz(Fr(int(pr), 100))}'],
                       f'Die Gruppe, auf die sich die Prozentangabe bezieht („{B}“), ist die Bedingung und steht hinter dem Strich.',
                       'Auf welche Gruppe bezieht sich die Prozentzahl? Diese steht hinter dem Strich.')
    if art == 'aussage':
        satz, A, B = R.choice(SAETZE)
        pr = satz.split('%')[0].split()[-1]
        r = f'Nein, gegeben ist P({A} | {B}), gefragt wäre P({B} | {A}).'
        return auswahl(f'„{satz}“ Jemand folgert: „Also gehören {pr} % aller mit „{A}“ zur Gruppe „{B}“.“ Stimmt das?', r,
                       ['Ja, das ist dieselbe Aussage.', f'Ja, wenn mehr als {pr} Personen befragt wurden.', 'Nein, es müssten dann 100 % sein.'],
                       f'Die Bedingung wurde vertauscht. Ohne die Größe beider Gruppen kann man P({B} | {A}) nicht angeben.',
                       'Welche Gruppe ist die Bedingung – vorher und nachher?')
    if art == 'gleich':
        a, b = R.randint(20, 80), R.randint(20, 80)
        if a == b: return None
        c = R.randint(5, min(a, b) - 1)
        r = 'Nein: P(A | B) = ' + f'{c}/{b}, P(B | A) = {c}/{a}.'
        return auswahl(f'In einer Gruppe haben {a} Personen Merkmal A, {b} Merkmal B und {c} beide. Ist P(A | B) = P(B | A)?', r,
                       ['Ja, es geht beide Male um dieselben ' + str(c) + ' Personen.', f'Ja, beide sind {c}/{a + b}.', f'Nein: P(A | B) = {c}/{a}, P(B | A) = {c}/{b}.'],
                       f'Der Zähler {c} ist gleich, aber geteilt wird durch die Bedingung: bei P(A | B) durch {b}, bei P(B | A) durch {a}.',
                       'Gleicher Zähler – durch welche Gruppe wird jeweils geteilt?')
    if art == 'tausch':
        a, b = R.randint(20, 60), R.randint(100, 300)
        c = R.randint(5, a - 2)
        q = Fr(c, b)
        return bruch_luecke(f'Von {b} Kindern einer Schule spielen {a} im Schulorchester. {c} der Orchesterkinder spielen Geige, außerhalb des Orchesters niemand. Wie groß ist P(Geige | Kind dieser Schule), also der Anteil der Geigenspieler an allen Kindern?', q,
                            f'Gesucht ist der Anteil unter allen {b} Kindern: {c}/{b} = {br(q)}. (P(Geige | Orchester) wäre {c}/{a}.)', 'Durch welche Gruppe wird geteilt?',
                            c=[str(q.numerator), str(q.denominator)])
    return auswahl(f'Alle Personen mit Merkmal A haben auch Merkmal B, aber nicht umgekehrt. Welche Wahrscheinlichkeit ist größer?', 'P(B | A) – sie ist sogar 1.',
                   ['P(A | B)', 'Beide sind gleich groß.', 'Das lässt sich nicht sagen.'],
                   'Wer A hat, hat sicher B: P(B | A) = 1. Unter den B gibt es aber auch Personen ohne A, also P(A | B) < 1.',
                   'Was weißt du sicher über jemanden mit Merkmal A?')


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-2) ----------
# Prüfungsvorbilder: IB MYP Extended (Venn-Diagramm, P(A ∪ B), „given that“-Fragen, unabhängige Ausfälle, Ziehen ohne Zurücklegen
# mit „mindestens eins“, Vierfeldertafel aus Prozentangaben), Abschlussprüfung Realschule Bayern (Vierfeldertafel / Baum im Sachzusammenhang).
def tafel3(art):
    if art == 'prozent_tafel':
        N = R.choice([200, 400, 500])
        m = R.choice([x for x in range(N // 5, N * 4 // 5 + 1, 10)])
        pm, pj = R.sample([10, 15, 20, 25, 30, 40, 50, 60], 2)
        rm, rj = m * pm / 100, (N - m) * pj / 100
        if rm != int(rm) or rj != int(rj) or rm + rj == 0: return None
        q = Fr(int(rm), int(rm + rj))
        return bruch_luecke(f'An einer Schule mit {N} Kindern sind {m} Mädchen. {pm} % der Mädchen und {pj} % der Jungen fahren mit dem Rad zur Schule. '
                            'Ein Kind, das mit dem Rad kommt, wird zufällig ausgewählt. Mit welcher Wahrscheinlichkeit ist es ein Mädchen? (gekürzter Bruch)', q,
                            f'Radfahrende Mädchen: {pm} % von {m} = {int(rm)}. Radfahrende Jungen: {pj} % von {N - m} = {int(rj)}. Bedingung „Rad“: {int(rm)} + {int(rj)} = {int(rm + rj)}. '
                            f'P(Mädchen | Rad) = {int(rm)}/{int(rm + rj)}' + (f' = {br(q)}.' if q.denominator != rm + rj else '.'),
                            'Lege eine Vierfeldertafel an: Mädchen/Jungen und Rad/kein Rad. Die Bedingung ist „Rad“.', c=[str(q.numerator), str(q.denominator)])
    if art == 'rueck':
        N = R.choice([200, 300, 400])
        b = R.choice(range(N // 5, N // 2, 10))
        p = Fr(R.choice([1, 2, 3, 4, 5, 6, 7]), R.choice([10, 20]))
        aa = b * p
        a = R.choice(range(N // 5, N // 2, 10))
        if aa.denominator != 1 or not 0 < aa < min(a, b): return None
        q = Fr(int(aa), a)
        return bruch_luecke(f'Von {N} Kindern fahren {b} mit dem Rad, {a} tragen eine Brille. Es gilt P(Brille | Rad) = {dz(p)}. Berechne P(Rad | Brille). (gekürzter Bruch)', q,
                            f'Radfahrer mit Brille: {dz(p)} · {b} = {int(aa)}. Bedingung „Brille“: {a} Kinder. P(Rad | Brille) = {int(aa)}/{a}' + (f' = {br(q)}.' if q.denominator != a else '.'),
                            'Bestimme zuerst die Anzahl der Kinder mit Rad und Brille.', c=[str(q.numerator), str(q.denominator)])
    return None


def formel3(art):
    if art == 'venn':
        a, ab, b, au = R.randint(3, 20), R.randint(2, 12), R.randint(3, 20), R.randint(2, 15)
        frage = R.choice(['AgB', 'BgA'])
        z, n = (ab, ab + b) if frage == 'AgB' else (ab, a + ab)
        q = Fr(z, n)
        G = a + ab + b + au
        bild = venn(a, ab, b, au, A='T', B='F', G='')
        return mit_grafik(bruch_luecke(f'Das Venn-Diagramm zeigt {G} Jugendliche: T spielt Tennis, F spielt Fußball. Berechne {"P(T | F)" if frage == "AgB" else "P(F | T)"}. (gekürzter Bruch)', q,
                                       f'Bedingung {"F" if frage == "AgB" else "T"}: ganzer Kreis {"F" if frage == "AgB" else "T"} = {n}. Davon in beiden Kreisen: {z}. P = {z}/{n}' + (f' = {br(q)}.' if q.denominator != n else '.'),
                                       'Die Bedingung ist der ganze Kreis hinter dem Strich – zähle beide Teile dieses Kreises.', c=[str(q.numerator), str(q.denominator)]), bild)
    if art == 'vereinigung':
        for _ in range(100):
            pa, pb = Fr(R.randint(2, 7), 10), Fr(R.randint(2, 7), 10)
            pab = Fr(R.randint(1, 5), 10)
            if pab < min(pa, pb) and pa + pb - pab <= 1 and endlich(pab / pb): break
        else:
            return None
        pu = pa + pb - pab
        return zahl(f'Es gilt P(A) = {dz(pa)}, P(B) = {dz(pb)} und P(A ∪ B) = {dz(pu)}. Berechne P(A | B).',
                    f'P(A ∩ B) = P(A) + P(B) − P(A ∪ B) = {dz(pa)} + {dz(pb)} − {dz(pu)} = {dz(pab)}. P(A | B) = {dz(pab)} : {dz(pb)} = {dz(pab / pb)}.',
                    'Bestimme zuerst P(A ∩ B) mit dem Additionssatz.', pab / pb, f'({float(pa)} + {float(pb)} - {float(pu)}) / {float(pb)}')
    if art == 'beide':
        for _ in range(100):
            pab = Fr(R.choice([1, 2, 3, 4, 6]), R.choice([10, 20]))
            q1, q2 = Fr(R.choice([1, 2, 3, 4, 5, 6, 8]), 10), Fr(R.choice([1, 2, 3, 4, 5, 6, 8]), 10)
            pb, pa = pab / q1, pab / q2
            if q1 != q2 and pa < 1 and pb < 1 and endlich(pa) and endlich(pb): break
        else:
            return None
        return zahl(f'Es gilt P(A ∩ B) = {dz(pab)}, P(A | B) = {dz(q1)} und P(B | A) = {dz(q2)}. Wie groß ist P(A)?',
                    f'P(B | A) = P(A ∩ B) : P(A), also P(A) = {dz(pab)} : {dz(q2)} = {dz(pa)}. (P(A | B) wird dafür nicht gebraucht; P(B) wäre {dz(pab)} : {dz(q1)} = {dz(pb)}.)',
                    'Bei welcher der beiden Angaben steht A hinter dem Strich?', pa, f'{float(pab)} / {float(q2)}')
    # fehler_formel
    pb, q = Fr(R.choice([2, 4, 5, 8]), 10), Fr(R.choice([2, 4, 5, 6]), 10)
    pab = pb * q
    r = f'Tim hat multipliziert statt geteilt. Richtig: {dz(pab)} : {dz(pb)} = {dz(q)}.'
    return auswahl(f'P(B) = {dz(pb)}, P(A ∩ B) = {dz(pab)}. Tim rechnet P(A | B) = {dz(pab)} · {dz(pb)} = {dz(pab * pb)}. Was stimmt?', r,
                   [f'Tim hat recht.', f'Tim hätte durch P(A) teilen müssen; das Ergebnis ist {dz(pab * 2)}.', f'Richtig wäre {dz(pb)} : {dz(pab)} = {dz(pb / pab)}.'],
                   f'P(A | B) = P(A ∩ B) : P(B) = {dz(pab)} : {dz(pb)} = {dz(q)}. Eine bedingte Wahrscheinlichkeit kann nicht kleiner sein als P(A ∩ B).',
                   'Wie lautet die Formel – wird geteilt oder multipliziert?')


def baum3(art):
    if art == 'kontext':
        m, j = R.randint(6, 15), R.randint(6, 15)
        n = m + j
        q = Fr(2 * m * j, n * (n - 1))
        return bruch_luecke(f'In einer Klasse sind {m} Mädchen und {j} Jungen. Für die Klassensprecher werden nacheinander zwei Namen ausgelost (niemand zweimal). '
                            'Mit welcher Wahrscheinlichkeit sind es ein Mädchen und ein Junge? (gekürzter Bruch)', q,
                            f'Zwei Pfade: M, J: {m}/{n} · {j}/{n - 1}; J, M: {j}/{n} · {m}/{n - 1}. Zusammen {2 * m * j}/{n * (n - 1)} = {br(q)}.',
                            'Zeichne einen Baum mit zwei Stufen. Welche Pfade passen?', c=[str(q.numerator), str(q.denominator)])
    if art == 'mindestens':
        r, b = R.randint(2, 6), R.randint(3, 8)
        n = r + b
        f1, f2 = R.choice([('rot', 'blau'), ('grün', 'gelb'), ('weiß', 'schwarz')])
        bb = Fr(b * (b - 1), n * (n - 1))
        q = 1 - bb
        return bruch_luecke(f'In einer Urne liegen {r} {f1}e und {b} {f2}e Kugeln. Es werden zwei Kugeln ohne Zurücklegen gezogen. Berechne die Wahrscheinlichkeit, mindestens eine {f1}e Kugel zu ziehen.', q,
                            f'Gegenereignis „keine {f1}e“ = zweimal {f2}: {b}/{n} · {b - 1}/{n - 1} = {br(bb)}. P = 1 − {br(bb)} = {br(q)}.',
                            '„Mindestens eine“: Rechne mit dem Gegenereignis.', c=[str(q.numerator), str(q.denominator)])
    if art == 'rueck_anzahl':
        n = R.choice([6, 8, 9, 10, 12, 15, 16])
        r = R.randint(2, n - 2)
        q = Fr(r * (r - 1), n * (n - 1))
        if sum(1 for k in range(n + 1) if Fr(k * (k - 1), n * (n - 1)) == q) != 1: return None
        return zahl(f'In einer Urne liegen {n} Kugeln, einige davon rot. Zieht man zwei Kugeln ohne Zurücklegen, ist P(zweimal rot) = {br(q)}. Wie viele rote Kugeln sind in der Urne?',
                    f'Mit r roten Kugeln: r/{n} · (r − 1)/{n - 1} = {br(q)}, also r · (r − 1) = {br(q)} · {n * (n - 1)} = {r * (r - 1)}. Probieren: {r} · {r - 1} = {r * (r - 1)}. Also {r} rote.',
                    'Stelle P(zweimal rot) mit einer Unbekannten r auf und probiere kleine Zahlen.', r, f'{r}')
    # mit_ohne
    r, b = R.randint(2, 6), R.randint(2, 6)
    n = r + b
    f1 = R.choice(['rot', 'grün', 'weiß'])
    mit, ohne = Fr(r * r, n * n), Fr(r * (r - 1), n * (n - 1))
    return auswahl(f'Urne mit {r} {f1}en und {b} anderen Kugeln, zwei Züge. Wann ist P(zweimal {f1}) größer: mit oder ohne Zurücklegen?', 'mit Zurücklegen',
                   ['ohne Zurücklegen', 'bei beiden gleich', 'Das hängt vom Glück ab.'],
                   f'Mit Zurücklegen: {r}/{n} · {r}/{n} = {br(mit)}. Ohne: {r}/{n} · {r - 1}/{n - 1} = {br(ohne)}. Ohne Zurücklegen fehlt beim zweiten Zug eine {f1}e Kugel – das macht {f1} seltener.',
                   'Was ändert sich beim zweiten Zug, wenn die erste Kugel nicht zurückkommt?')


def unabh3(art):
    if art == 'tafel_ergaenzen':
        N = R.choice([100, 200, 400, 500])
        pa, pb = Fr(R.randint(1, 9), 10), Fr(R.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]), 10)
        aa = pa * pb * N
        if aa.denominator != 1 or aa < 2: return None
        return zahl(f'Von {N} Befragten treiben {int(pa * N)} Sport (A), {int(pb * N)} spielen ein Instrument (B). Wie viele müssen beides tun, damit A und B unabhängig sind?',
                    f'Unabhängig: P(A ∩ B) = P(A) · P(B) = {dz(pa)} · {dz(pb)} = {dz(pa * pb)}. Anzahl: {dz(pa * pb)} · {N} = {int(aa)}.',
                    'Rechne mit Anteilen: P(A) · P(B), dann mal die Gesamtzahl.', aa, f'{int(pa * N)} / {N} * {int(pb * N)} / {N} * {N}')
    if art == 'ausfall':
        a, b = Fr(R.choice([1, 2, 5]), R.choice([10, 20, 100])), Fr(R.choice([1, 2, 3, 4]), R.choice([10, 20]))
        if not (0 < a < 1 and 0 < b < 1): return None
        q = 1 - (1 - a) * (1 - b)
        return zahl(f'Zwei Pumpen arbeiten unabhängig voneinander. Pumpe 1 fällt an einem Tag mit der Wahrscheinlichkeit {dz(a)} aus, Pumpe 2 mit {dz(b)}. '
                    'Wie groß ist die Wahrscheinlichkeit, dass an einem Tag mindestens eine Pumpe ausfällt?',
                    f'Gegenereignis: beide laufen. Unabhängig: {dz(1 - a)} · {dz(1 - b)} = {dz((1 - a) * (1 - b))}. P = 1 − {dz((1 - a) * (1 - b))} = {dz(q)}.',
                    '„Mindestens eine“: Rechne erst die Wahrscheinlichkeit, dass keine ausfällt.', q, f'1 - (1 - {float(a)}) * (1 - {float(b)})')
    return None


def rueck3(art):
    for _ in range(200):
        pk = R.choice([1, 2, 5, 10, 20])
        se = R.choice([80, 90, 95, 100])
        fp = R.choice([5, 10, 20])
        N = 1000
        k = N * pk // 100
        tp, f = k * se // 100, (N - k) * fp // 100
        if k * se % 100 == 0 and (N - k) * fp % 100 == 0 and se < 100: break
    ctx = R.choice([('Geräte', 'defekt', 'gemeldet', 'Ein Prüfgerät meldet', 'nicht gemeldet', 'es'), ('E-Mails', 'Spam', 'markiert', 'Ein Filter markiert', 'nicht markiert', 'sie')])
    D, K, T2, T, NT, pron = ctx
    vor = f'{pk} % der {D} sind {K}. {T} {se} % dieser {D}, aber irrtümlich auch {fp} % der übrigen. Stelle dir 1 000 {D} vor.'
    if art == 'negativ':
        fn, tn = k - tp, (N - k) - f
        q = Fr(fn, fn + tn)
        return bruch_luecke(vor + f' {"Ein Gerät" if D == "Geräte" else "Eine E-Mail"} wurde {NT}. Wie groß ist die Wahrscheinlichkeit, dass {pron} trotzdem {K} ist? (gekürzter Bruch)', q,
                            f'{NT.capitalize()}: {K} {fn} (= {k} − {tp}) und übrige {tn} (= {N - k} − {f}), zusammen {fn + tn}. P = {fn}/{fn + tn}' + (f' = {br(q)}.' if q.denominator != fn + tn else '.'),
                            f'Die Bedingung ist jetzt „{NT}“. Zähle beide Gruppen ohne Signal.', c=[str(q.numerator), str(q.denominator)])
    # basisrate
    r = f'Es gibt viel mehr {D} ohne Befund; schon {fp} % von ihnen sind mehr Fälle als die richtig erkannten.'
    q = Fr(tp, tp + f)
    if f <= tp: return None
    gruppe = 'der defekten Geräte' if D == 'Geräte' else 'der Spam-E-Mails'
    return auswahl(vor + f' Nur etwa {dz(round(float(q) * 100))} % der {T2}en {D} sind wirklich {K}, obwohl {se} % {gruppe} gefunden werden. Woran liegt das?', r,
                   [f'Das Gerät arbeitet schlecht: Es findet nur {100 - se} % der Fälle.', f'Man hat falsch gerechnet; richtig wären {se} %.', f'Weil {pk} % eine kleine Zahl ist, ist auch die Wahrscheinlichkeit klein.'],
                   f'{K.capitalize()} und {T2}: {tp}. Ohne Befund, aber {T2}: {f} – mehr als {tp}, weil es {N - k} {D} ohne Befund gibt. Darum ist P({K} | {T2}) = {tp}/{tp + f} ≈ {dz(round(float(q), 2))} klein.',
                   'Vergleiche die Anzahl der richtigen und der falschen Meldungen unter 1 000.')


def verstehen3(art):
    if art == 'welche_gruppe':
        m, f, mf = R.randint(40, 90), R.randint(20, 60), R.randint(8, 19)
        r = f'{mf} : {m}'
        return auswahl(f'An einer Schule sind {m} Mädchen, {f} Kinder spielen Fußball, {mf} Mädchen spielen Fußball. Gefragt: „Wie viel Prozent der Mädchen spielen Fußball?“ Welche Rechnung passt?', r,
                       [f'{mf} : {f}', f'{f} : {m}', f'{m} : {mf}'],
                       f'„der Mädchen“ ist die Gruppe (Bedingung): P(Fußball | Mädchen) = {mf} : {m} ≈ {dz(round(mf / m * 100, 1))} %.',
                       'Auf welche Gruppe bezieht sich „Prozent der …“? Durch deren Anzahl wird geteilt.')
    if art == 'gleich_wann':
        r = 'Wenn A und B gleich viele Personen umfassen.'
        return auswahl('Wann gilt P(A | B) = P(B | A) (mit P(A ∩ B) > 0)?', r,
                       ['Nie.', 'Immer, es geht ja um dieselben Personen.', 'Wenn A und B unabhängig sind.'],
                       'P(A | B) = Anzahl(A und B) : Anzahl(B), P(B | A) = Anzahl(A und B) : Anzahl(A). Der Zähler ist gleich, also müssen die Nenner gleich sein: Anzahl(A) = Anzahl(B).',
                       'Schreibe beide Brüche mit Anzahlen auf. Was ist gleich, was verschieden?')
    return None


def g2_tafel(s):
    if s < 3: return g_tafel(s)
    art = art3('vergleich', 'prozent_tafel', 'rueck', ['luecke', 'vergleich', 'prozent_tafel', 'rueck'])
    if art in ('luecke', 'vergleich'):
        for _ in range(50):
            a = g_tafel(3)
            if a and (('fehlt' in a['f']['text']) == (art == 'luecke')) and ('größer' in a['f']['text'] or art == 'luecke'): return a
        return None
    return tafel3(art)


def g2_formel(s):
    if s == 1: return g_formel(1)
    if s == 2:  # Stufe 2: umstellen, Gegenereignis unter der Bedingung, Prozent-Sachaufgabe (vorher Stufe 3)
        return g_formel(R.choice([2, 3]))
    return formel3(art3('venn', 'vereinigung', 'beide', ['venn', 'vereinigung', 'beide', 'fehler_formel']))


def g2_baum(s):
    if s == 1: return g_baum(1)
    if s == 2:  # Stufe 2: ein Pfad oder zwei Pfade addieren (vorher Stufe 3)
        return g_baum(2)
    return baum3(art3('kontext', 'mindestens', 'rueck_anzahl', ['kontext', 'mindestens', 'rueck_anzahl', 'mit_ohne']))


def g2_unabhaengig(s):
    if s == 1: return g_unabhaengig(1)
    if s == 2:
        for _ in range(80):  # Stufe 2: an der Vierfeldertafel prüfen, P(A | B) = P(A) nutzen (vorher Stufe 3)
            a = g_unabhaengig(3)
            if a and ('Vierfeldertafel' in a['f']['text'] or 'Wie groß ist P(A | B)' in a['f']['text']): return a
        return None
    art = art3('tafel_ergaenzen', 'ausfall', 'ausschluss', ['tafel_ergaenzen', 'ausfall', 'ausschluss', 'muenze'])
    if art in ('tafel_ergaenzen', 'ausfall'): return unabh3(art)
    for _ in range(80):
        a = g_unabhaengig(3)
        t = a['f']['text'] if a else ''
        if a and {'ausschluss': 'schließen sich aus', 'muenze': 'Münze', 'bedingt_gleich': 'Wie groß ist P(A | B)'}[art] in t: return a
    return None


def g2_rueckschluss(s):
    if s < 3: return g_rueckschluss(s)
    art = art3('bayes', 'negativ', 'basisrate', ['bayes', 'negativ', 'basisrate', 'vergleich'])
    if art in ('bayes', 'vergleich'):
        for _ in range(80):
            a = g_rueckschluss(3)
            if a and (('größer oder kleiner' in a['f']['text']) == (art == 'vergleich')) and '100 %?' not in a['f']['text']: return a
        return None
    return rueck3(art)


def g2_verstehen(s):
    if s == 1: return g_verstehen(1)
    if s == 2:
        for _ in range(50):
            a = g_verstehen(R.choice([2, 3]))
            if a and ('Ist P(A | B) = P(B | A)' in a['f']['text'] or 'Jemand folgert' in a['f']['text']): return a
        return None
    art = art3('welche_gruppe', 'tausch', 'gleich_wann', ['welche_gruppe', 'tausch', 'groesser'])
    if art in ('welche_gruppe', 'gleich_wann'): return verstehen3(art)
    for _ in range(80):
        a = g_verstehen(3)
        if a and (('Geige' in a['f']['text']) == (art == 'tausch')) and ('Merkmal A haben auch' in a['f']['text'] or art == 'tausch'): return a
    return None


GEN = {'tafel': g2_tafel, 'formel': g2_formel, 'baum': g2_baum, 'unabhaengig': g2_unabhaengig, 'rueckschluss': g2_rueckschluss, 'verstehen': g2_verstehen}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import tab  # noqa: E402

_VT = tab(['', 'Rad', 'kein Rad', 'Summe'], ['Brille', '20', '40', '60'], ['keine Brille', '30', '110', '140'], ['Summe', '50', '150', '200'])


def _ast(text, p=None, *unter):
    a = {'text': text}
    if p:
        a['p'] = p
    if unter:
        a['aeste'] = list(unter)
    return a


def _w(*z):
    return tab(['', 'Wert'], ['P(Kopf)', '0,5'], ['P(Rot)', '0,4'], ['P(Kopf ∩ Rot)', '0,2'], *z)


_HU = tab(['', 'Hund', 'kein Hund', 'Summe'], ['spazieren', '70', '330', '400'], ['nicht', '30', '570', '600'], ['Summe', '100', '900', '1 000'])
UMBAU = {
    'tafel': {
        'einstieg': 'An einer Schule mit 200 Kindern fahren 50 mit dem Rad. Wie viele Radfahrer tragen eine Brille? '
                    'Wer nur auf die Radfahrer schaut, rechnet eine ⟦bedingte Wahrscheinlichkeit⟧ aus.',
        'woerter': [['Bedingung', 'was schon feststeht; in P(A | B) steht sie hinter dem Strich'],
                    ['Vierfeldertafel', 'Tabelle mit vier Feldern und den Summen']],
        'bild': _VT,
        'schritte': [
            {'text': 'In der Vierfeldertafel: 50 fahren Rad, 20 davon mit Brille.'},
            {'text': 'Bedingung „fährt Rad“: Nur die Spalte Rad zählt.',
             'bild': tab(['', 'Rad'], ['Brille', '20'], ['keine Brille', '30'], ['Summe', '50'])},
            {'text': 'P(Brille | Rad) = 20 : 50 = ⟦0,4⟧.'},
        ],
        'fehler': '20 : 200 = 0,1 ist falsch, das ist P(Brille ∩ Rad). Unter der Bedingung teilt man durch die ⟦50 Radfahrer⟧.',
        'regel': 'P(A | B): nur die ⟦Gruppe B⟧ betrachten. Teile „A und B“ durch die Anzahl von B.',
    },
    'formel': {
        'einstieg': 'Statt Anzahlen kennst du manchmal nur Wahrscheinlichkeiten. 40 % der Kinder fahren Rad, '
                    '10 % fahren Rad und tragen Brille. Dann hilft die ⟦Formel⟧.',
        'woerter': [['A ∩ B', 'A und B treten beide ein, hier: Rad und Brille']],
        'bild': {'typ': 'bruchstreifen', 'teile': 10, 'gefaerbt': 4, 'ganzes': 'alle Kinder', 'teil_text': 'Rad: 0,4'},
        'schritte': [
            {'text': 'P(B) = P(Rad) = 0,4 und P(A ∩ B) = 0,1.'},
            {'text': 'Von den 0,4 Radfahrern ist 0,1 mit Brille.',
             'bild': {'zeilen': [{'teile': 4, 'gefaerbt': 1}]}},
            {'text': 'P(A | B) = 0,1 : 0,4 = ⟦0,25⟧.'},
        ],
        'fehler': '0,1 · 0,4 = 0,04 ist falsch. Für P(A | B) wird ⟦geteilt⟧, multipliziert wird nur für P(A ∩ B).',
        'regel': '⟦P(A | B) = P(A ∩ B) : P(B)⟧. Umgestellt: P(A ∩ B) = P(B) · P(A | B).',
    },
    'baum': {
        'einstieg': 'In einem Beutel sind 3 rote und 2 blaue Bonbons. Du nimmst eins und isst es, dann noch eins. '
                    'Beim zweiten Griff ist eins weniger da: ⟦ohne Zurücklegen⟧.',
        'woerter': [['ohne Zurücklegen', 'das Gezogene kommt nicht zurück; die zweite Stufe ändert sich'],
                    ['Pfad', 'ein Weg durch das Baumdiagramm']],
        'bild': {'typ': 'baum', 'aeste': [_ast('rot', '3/5'), _ast('blau', '2/5')]},
        'schritte': [
            {'text': 'Erster Griff: P(rot) = 3/5.'},
            {'text': 'Danach sind noch 2 rote von 4 da: 2/4.',
             'bild': {'aeste': [_ast('rot', '3/5', _ast('rot', '2/4'), _ast('blau', '2/4')), _ast('blau', '2/5')]}},
            {'text': 'Pfad rot, rot: 3/5 · 2/4 = ⟦3/10⟧.',
             'bild': {'aeste': [_ast('rot', '3/5', _ast('rot', '2/4'), _ast('blau', '2/4')),
                                _ast('blau', '2/5', _ast('rot', '3/4'), _ast('blau', '1/4'))]}},
        ],
        'fehler': '3/5 · 3/5 ist falsch, denn das erste Bonbon ist ⟦gegessen⟧. Beim zweiten Griff sind nur noch 2 rote von 4 da.',
        'fehler_bild': {'aeste': [_ast('rot', '3/5', _ast('rot', '3/5 ✗'), _ast('blau', '?')), _ast('blau', '2/5')]},
        'regel': 'Ohne Zurücklegen ⟦ändert sich die zweite Stufe⟧. Entlang des Pfades multiplizieren.',
    },
    'unabhaengig': {
        'einstieg': 'Eine Münze zeigt Kopf, ein Glücksrad bleibt auf Rot stehen. Das eine beeinflusst das andere nicht. '
                    'Solche Ereignisse heißen ⟦unabhängig⟧.',
        'woerter': [['unabhängig', 'das Wissen über B ändert die Wahrscheinlichkeit von A nicht'],
                    ['abhängig', 'das Wissen über B ändert die Wahrscheinlichkeit von A']],
        'bild': _w(),
        'schritte': [
            {'text': 'P(Kopf) = 0,5, P(Rot) = 0,4, P(beides) = 0,2.'},
            {'text': 'P(Kopf) · P(Rot) = 0,5 · 0,4 = 0,2.', 'bild': _w(['P(Kopf) · P(Rot)', '0,2'])},
            {'text': 'Das ist genau P(beides): ⟦unabhängig⟧.', 'bild': _w(['P(Kopf) · P(Rot)', '0,2 ✓'])},
        ],
        'fehler': '„A und B können nie zusammen eintreten, also unabhängig“ ist falsch. Tritt A ein, ist B ausgeschlossen: ⟦abhängig⟧.',
        'regel': 'Unabhängig, wenn ⟦P(A ∩ B) = P(A) · P(B)⟧. Sonst sind A und B abhängig.',
    },
    'rueckschluss': {
        'einstieg': 'Ein Prüfgerät soll defekte Handys finden. Es meldet aber auch manchmal gute. '
                    'Wie sicher ist ein gemeldetes Handy defekt? Stell dir ⟦1 000 Fälle⟧ vor.',
        'woerter': [['gemeldet', 'das Prüfgerät schlägt Alarm']],
        'bild': {'typ': 'baum', 'aeste': [_ast('defekt', '0,1'), _ast('gut', '0,9')]},
        'schritte': [
            {'text': '10 % von 1 000 sind defekt: 100 defekt, 900 gut.',
             'bild': {'aeste': [_ast('defekt: 100', '0,1'), _ast('gut: 900', '0,9')]}},
            {'text': 'Gemeldet werden 90 % der defekten (90) und 5 % der guten (45).',
             'bild': {'aeste': [_ast('defekt: 100', '0,1', _ast('ja: 90', '0,9'), _ast('nein: 10', '0,1')),
                                _ast('gut: 900', '0,9', _ast('ja: 45', '0,05'), _ast('nein: 855', '0,95'))]}},
            {'text': 'Insgesamt gemeldet: 90 + 45 = 135.'},
            {'text': 'P(defekt | gemeldet) = 90 : 135 = ⟦2/3⟧.'},
        ],
        'fehler': '0,9 ist falsch, das ist P(gemeldet | defekt). Die Bedingung ist ⟦vertauscht⟧: Unter den gemeldeten sind auch 45 gute.',
        'regel': 'Mit 1 000 Fällen rechnen. Dann ⟦nur die Fälle mit der Bedingung⟧ zählen und den Anteil bilden.',
    },
    'verstehen': {
        'einstieg': 'Eine Umfrage sagt: 70 % der Hundebesitzer gehen täglich spazieren. Haben dann 70 % der Spaziergänger einen Hund? Nein! '
                    'Entscheidend ist, ⟦wer die Gruppe⟧ ist.',
        'woerter': [['hinter dem Strich', 'dort steht in P(A | B) die Bedingung, also die Gruppe']],
        'bild': _HU,
        'schritte': [
            {'text': 'Die Gruppe sind die Hundebesitzer. Sie stehen hinter dem Strich.'},
            {'text': 'Also ⟦P(spazieren | Hund) = 0,7⟧: 70 von 100.',
             'bild': tab(['', 'Hund'], ['spazieren', '70'], ['nicht', '30'], ['Summe', '100'])},
            {'text': 'Umgekehrt: Von 400 Spaziergängern haben nur 70 einen Hund.',
             'bild': tab(['', 'Hund', 'Summe'], ['spazieren', '70', '400'])},
            {'text': 'P(Hund | spazieren) = 70 : 400 ≈ 0,18. Ganz anders!'},
        ],
        'fehler': '„70 % der Spaziergänger haben einen Hund“ ist falsch. Das vertauscht die ⟦Bedingung⟧: Es sind nur 70 von 400.',
        'regel': 'Erst die ⟦Gruppe⟧ finden, sie steht hinter dem Strich. P(A | B) und P(B | A) sind meist verschieden.',
    },
}
UMBAU_OFFEN = ['Umbau (Paket UR): Die Vierfeldertafel der Karte verstehen (Hund/Spaziergänger, 1 000 Personen) zeigt Beispielzahlen; '
               'nur der Satz „70 % der Hundebesitzer …“ stammt aus dem bisherigen Beispiel.']
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


d = bauen('stochastik.bedingt',
      'Bedingte Wahrscheinlichkeiten aus Tafeln, Formeln und Baumdiagrammen bestimmen, Unabhängigkeit prüfen und Rückschlüsse mit Häufigkeiten ziehen.',
      ['P(A | B) (conditional probability): Wahrscheinlichkeit von A, wenn B schon feststeht.',
       'P(A | B) = P(A ∩ B) : P(B); P(A ∩ B) = P(B) · P(A | B).',
       'Unabhängig (independent): P(A | B) = P(A), also P(A ∩ B) = P(A) · P(B).',
       'Ohne Zurücklegen: zweite Stufe ändert sich.',
       'P(A | B) ≠ P(B | A) – die Bedingung steht hinter dem Strich.'],
      [('Bedingte Wahrscheinlichkeit', ['tafel', 'formel', 'baum']), ('Abhängigkeit', ['unabhaengig']), ('Schließen und verstehen', ['rueckschluss', 'verstehen'])],
      ETAPPEN, GEN,
      offen=['Schreibweise P(A | B) wie im IB; im bayerischen Gymnasium heißt das P_B(A). Bei der ersten Erklärung beides erwähnen? Bisher nur IB-Schreibweise.',
             'Überschneidung mit stochastik.verknuepft (Gymnasium Klasse 9, Lernkarte „bedingt“): Hier ausführlicher (Formel, Ziehen ohne Zurücklegen, Unabhängigkeit, Rückschlüsse).',
             'Satz von Bayes nur über natürliche Häufigkeiten (1 000 Fälle), ohne Formel – passend zu MYP 4.'],
      vertiefung=['rueckschluss'], plan=PLAN2)
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
