#!/usr/bin/env python3
"""Thema mengen.grundbegriffe – Mengen und Venn-Diagramme (IB MYP 1, etwa Klasse 6)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403

start(8301)

PRIM = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}


def eig_liste(N):
    """Eigenschaften für Zahlen 1..N: (Beschreibung mit Artikel, Test)."""
    e = [(f'die Vielfachen von {k} bis {N}', (lambda k: lambda z: z % k == 0)(k)) for k in (2, 3, 4, 5, 6)]
    e += [(f'die Teiler von {k}', (lambda k: lambda z: k % z == 0)(k)) for k in (12, 18, 20, 24, 30, 36) if k <= N]
    e += [(f'die geraden Zahlen von 1 bis {N}', lambda z: z % 2 == 0), (f'die ungeraden Zahlen von 1 bis {N}', lambda z: z % 2 == 1),
          (f'die Primzahlen bis {N}', lambda z: z in PRIM), (f'die Quadratzahlen bis {N}', lambda z: int(z ** 0.5) ** 2 == z),
          (f'die Zahlen von {N // 2 + 1} bis {N}', lambda z: z > N // 2)]
    return e


def el(n):
    return '1 Element' if n == 1 else f'{n} Elemente'


def zwei_mengen(N, min_schnitt=1, max_el=12):
    for _ in range(200):
        (ta, fa), (tb, fb) = R.sample(eig_liste(N), 2)
        A = [z for z in range(1, N + 1) if fa(z)]
        B = [z for z in range(1, N + 1) if fb(z)]
        S = [z for z in A if z in B]
        if A == B or not (2 <= len(A) <= max_el and 2 <= len(B) <= max_el): continue
        if len(S) < min_schnitt or set(S) in (set(A), set(B)) and min_schnitt > 0 and R.random() < .7: continue
        return ta, A, tb, B
    return None


ETAPPEN = [
    {'lernziel': 'elemente', 'titel': 'Was gehört zu einer Menge?',
     'regel': 'Eine ⟦Menge⟧ (set) fasst Dinge zusammen, ihre ⟦Elemente⟧ (elements). Man schreibt sie in geschweifte Klammern: A = {2; 4; 6}. ⟦4 ∈ A⟧ heißt „4 ist Element von A“, ⟦5 ∉ A⟧ heißt „5 ist nicht Element von A“. Jedes Element zählt nur einmal.',
     'schritte': ['A = die Teiler von 10. Prüfe 1, 2, …, 10: 10 : 1, 10 : 2, 10 : 5, 10 : 10 gehen auf.',
                  'A = {1; 2; 5; 10}. Also ⟦2 ∈ A⟧, aber 4 ∉ A. A hat ⟦4 Elemente⟧.'],
     'probe': '1 · 10 = 10 und 2 · 5 = 10 – kein Teiler vergessen ✓',
     'fehler': 'Bei „Teiler von 10“ die 1 und die 10 selbst zu vergessen und nur {2; 5} aufzuschreiben, ist falsch: ⟦Jede Zahl ist Teiler von sich selbst, und 1 teilt jede Zahl⟧.'},
    {'lernziel': 'schnitt', 'titel': 'Die Schnittmenge A ∩ B',
     'regel': 'Die ⟦Schnittmenge⟧ (intersection) ⟦A ∩ B⟧ enthält alle Elemente, die in A ⟦und⟧ in B liegen. Im Venn-Diagramm (Venn diagram) ist das der Bereich, in dem sich die Kreise ⟦überlappen⟧. Haben A und B nichts gemeinsam, ist A ∩ B die ⟦leere Menge⟧ (empty set) { }.',
     'schritte': ['A = {1; 2; 3; 4; 6; 12} (Teiler von 12), B = {2; 4; 6; 8; 10; 12} (gerade Zahlen bis 12).',
                  'Gemeinsam sind 2, 4, 6 und 12. Also ⟦A ∩ B = {2; 4; 6; 12}⟧.'],
     'probe': 'Jede der vier Zahlen steht in beiden Listen ✓',
     'bild': venn('1; 3', '2; 4; 6; 12', '8; 10', None),
     'fehler': 'A ∩ B = {1; 2; 3; 4; 6; 8; 10; 12} ist falsch: Das sind alle Zahlen aus beiden Mengen zusammen. In die Schnittmenge kommen nur Zahlen, die in ⟦beiden⟧ Mengen stehen.'},
    {'lernziel': 'vereinigung', 'titel': 'Die Vereinigungsmenge A ∪ B',
     'regel': 'Die ⟦Vereinigungsmenge⟧ (union) ⟦A ∪ B⟧ enthält alle Elemente, die in A ⟦oder⟧ in B liegen (oder in beiden). Gemeinsame Elemente schreibt man nur ⟦einmal⟧. Für die Anzahl gilt: ⟦n(A ∪ B) = n(A) + n(B) − n(A ∩ B)⟧.',
     'schritte': ['A = {1; 3; 5; 7; 9}, B = {3; 6; 9}. Gemeinsam: 3 und 9.',
                  'A ∪ B = {1; 3; 5; 6; 7; 9}. Anzahl: 5 + 3 − 2 = ⟦6⟧.'],
     'probe': 'Abzählen: 1, 3, 5, 6, 7, 9 – sechs Zahlen ✓',
     'bild': venn('1; 5; 7', '3; 9', '6', None),
     'fehler': 'n(A ∪ B) = 5 + 3 = 8 ist falsch: 3 und 9 wurden ⟦doppelt gezählt⟧. Die gemeinsamen Elemente zieht man einmal ab: 8 − 2 = 6.'},
    {'lernziel': 'venn', 'titel': 'Mit Venn-Diagrammen zählen',
     'regel': 'Ein Rechteck steht für die ⟦Grundmenge⟧ (universal set), zwei Kreise für A und B. Es gibt ⟦vier Bereiche⟧: nur A, A und B, nur B, außerhalb beider. Fülle zuerst den ⟦Überlappungsbereich⟧, dann die anderen.',
     'schritte': ['30 Kinder: 18 spielen Fußball, 14 schwimmen, 6 tun beides.',
                  'Überlappung 6; nur Fußball 18 − 6 = 12; nur Schwimmen 14 − 6 = 8.',
                  'Weder noch: 30 − 12 − 6 − 8 = ⟦4⟧.'],
     'probe': '12 + 6 + 8 + 4 = 30 ✓',
     'bild': venn('12', '6', '8', '4', A='Fußball', B='Schwimmen', G='30 Kinder'),
     'fehler': '„Nur Fußball“ = 18 zu setzen ist falsch: Die 18 enthält auch die 6 Kinder, die zusätzlich schwimmen. Erst ⟦die Überlappung abziehen⟧: 18 − 6 = 12.'},
    {'lernziel': 'verstehen', 'titel': 'Aussagen über Mengen prüfen',
     'regel': 'Prüfe Aussagen mit einem Beispiel oder dem Venn-Diagramm: Die Schnittmenge ist ⟦nie größer⟧ als A oder B. Die Vereinigung ist ⟦nie kleiner⟧. Liegt A ganz in B (⟦Teilmenge⟧, subset: A ⊆ B), dann ist A ∩ B = A und A ∪ B = B.',
     'schritte': ['Behauptung: „A hat 5 Elemente, B hat 4. Dann hat A ∩ B 9 Elemente.“',
                  'A ∩ B liegt in A, kann also höchstens 5 Elemente haben. ⟦Die Aussage ist falsch⟧ – 9 wäre höchstens n(A ∪ B).'],
     'probe': 'Beispiel: A = {1; 2; 3; 4; 5}, B = {4; 5; 6; 7}: A ∩ B = {4; 5} ✓',
     'fehler': 'Zu meinen, A ∪ B habe immer n(A) + n(B) Elemente, ist falsch: Das stimmt ⟦nur, wenn A und B nichts gemeinsam haben⟧ (A ∩ B = { }).'},
]


# ---------- Generatoren ----------
def g_elemente(s):
    N = R.choice([20, 24, 30]) if s > 1 else R.choice([10, 12, 15, 20])
    t, f = R.choice(eig_liste(N))
    A = [z for z in range(1, N + 1) if f(z)]
    if not 2 <= len(A) <= 12: return None
    art = R.choice({1: ['in', 'in', 'anzahl'], 2: ['liste', 'anzahl', 'in'], 3: ['nicht', 'liste', 'grenze']}[s])
    vor = f'A = {t}.'
    if art == 'in':
        z = R.randint(1, N)
        r = '∈' if z in A else '∉'
        return auswahl(f'{vor} Welches Zeichen passt: {z} □ A?', f'{z} {r} A', [f'{z} ∈ A', f'{z} ∉ A', f'{z} = A'],
                       f'A = {menge(A)}. {z} {"steht" if z in A else "steht nicht"} in A, also {z} {r} A.',
                       '∈ heißt „ist Element von“, ∉ heißt „ist nicht Element von“. Prüfe die Eigenschaft an der Zahl.')
    if art == 'anzahl':
        return zahl(f'{vor} Wie viele Elemente hat A?', f'A = {menge(A)}. Das sind {el(len(A))}.',
                    'Schreibe alle Elemente auf und zähle sie.', len(A), f'{len(A)}')
    if art == 'liste' or art == 'grenze':
        falsch = []
        if len(A) > 2: falsch.append(menge(A[:-1]))                        # letztes vergessen
        falsch.append(menge([z for z in range(1, N + 1) if z not in A][:len(A)]))   # Gegenteil
        if 'Teiler' in t: falsch.append(menge([z for z in A if z not in (1, int(t.split()[3]))]))
        if 'Vielfache' in t: falsch.append(menge([0] + A[:-1]))
        if t.startswith('die Zahlen'): falsch.append(menge([N // 2] + A[:-1]))
        falsch.append(menge(A[1:]))
        return auswahl(f'{vor} Welche Aufzählung ist richtig?', menge(A), falsch,
                       f'Prüfe jede Zahl von 1 bis {N}: A = {menge(A)}.', 'Gehe die Zahlen der Reihe nach durch und achte auf die erste und letzte Zahl.')
    # nicht
    nicht = [z for z in range(1, N + 1) if z not in A]
    if len(A) < 3 or not nicht: return None
    x = R.choice(nicht)
    ins = R.sample(A, 3)
    return auswahl(f'{vor} Welche Zahl gehört NICHT zu A?', str(x), [str(i) for i in ins],
                   f'A = {menge(A)}. {x} steht nicht darin, die anderen drei Zahlen schon.', 'Prüfe jede Antwort mit der Eigenschaft von A.')


def g_schnitt(s):
    N = R.choice([12, 15, 20]) if s == 1 else R.choice([20, 24, 30])
    m = zwei_mengen(N, min_schnitt=0 if s == 3 else 1)
    if not m: return None
    ta, A, tb, B = m
    S = [z for z in A if z in B]
    U = sorted(set(A) | set(B))
    if s == 1:
        vor = f'A = {menge(A)}, B = {menge(B)}.'
    else:
        vor = f'A = {ta}, B = {tb}.'
    art = R.choice({1: ['liste', 'anzahl'], 2: ['liste', 'anzahl', 'liste'], 3: ['sach', 'leer', 'anzahl']}[s])
    if art == 'leer':
        return auswahl(vor + ' Welche Menge ist A ∩ B?', menge(S), [menge(U), menge([z for z in A if z not in B]), menge(S[:-1]) if len(S) > 1 else menge(A), '{ }' if S else menge(B)],
                       f'A = {menge(A)}, B = {menge(B)}. Gemeinsam: {menge(S)}' + ('' if S else ' – die leere Menge') + '.',
                       'Schreibe beide Mengen auf und markiere die Zahlen, die in beiden stehen.')
    if art == 'sach':
        k = R.choice([('Klasse 6a', 'Kinder in der Englisch-AG', 'Kinder, die im Chor singen'), ('Sportverein', 'Mitglieder im Tennis', 'Mitglieder im Schwimmen')])
        namen = ['Ali', 'Ben', 'Cem', 'Dana', 'Eva', 'Finn', 'Gül', 'Hanna', 'Ida', 'Jonas', 'Kim', 'Lio', 'Mia', 'Noah']
        A2 = sorted(R.sample(namen, R.randint(4, 6)))
        rest = [n for n in namen if n not in A2]
        g = R.sample(A2, R.randint(1, 3))
        B2 = sorted(g + R.sample(rest, R.randint(2, 4)))
        S2 = [n for n in A2 if n in B2]
        return auswahl(f'{k[0]}: A = {k[1]} = {menge(A2)}, B = {k[2]} = {menge(B2)}. Wer ist in A ∩ B?', menge(S2),
                       [menge(sorted(set(A2) | set(B2))), menge([n for n in A2 if n not in B2]), menge([n for n in B2 if n not in A2])],
                       f'In beiden Listen stehen {menge(S2)}.', 'A ∩ B: Wer steht in beiden Listen?')
    if art == 'anzahl':
        return zahl(vor + ' Wie viele Elemente hat A ∩ B?', f'A = {menge(A)}, B = {menge(B)}. A ∩ B = {menge(S)}, also {el(len(S))}.',
                    'Schreibe die gemeinsamen Elemente auf und zähle sie.', len(S), f'{len(S)}')
    if not S: return None
    return auswahl(vor + ' Welche Menge ist A ∩ B?', menge(S), [menge(U), menge([z for z in A if z not in B]), menge([z for z in B if z not in A])],
                   (f'A = {menge(A)}, B = {menge(B)}. ' if s > 1 else '') + f'In beiden Mengen: A ∩ B = {menge(S)}.',
                   '∩ heißt „und“: nur Zahlen, die in A und in B stehen.')


def g_vereinigung(s):
    N = R.choice([12, 15, 20]) if s == 1 else R.choice([20, 24, 30])
    m = zwei_mengen(N, max_el=8 if s == 1 else 12)
    if not m: return None
    ta, A, tb, B = m
    S = [z for z in A if z in B]
    U = sorted(set(A) | set(B))
    vor = f'A = {menge(A)}, B = {menge(B)}.' if s == 1 else f'A = {ta}, B = {tb}.'
    art = R.choice({1: ['liste', 'anzahl'], 2: ['anzahl', 'liste', 'formel'], 3: ['formel_sach', 'formel_sach', 'rueck']}[s])
    if art == 'liste':
        dop = sorted(A + B)
        falsch = [menge(S), menge(dop) if len(dop) != len(U) else menge(U[:-1]), menge([z for z in U if z not in S])]
        return auswahl(vor + ' Welche Menge ist A ∪ B?', menge(U), falsch,
                       (f'A = {menge(A)}, B = {menge(B)}. ' if s > 1 else '') + f'Alle Elemente aus A oder B, jedes einmal: {menge(U)}.',
                       '∪ heißt „oder“: alle Zahlen aus A und aus B, gemeinsame nur einmal.')
    if art == 'anzahl':
        return zahl(vor + ' Wie viele Elemente hat A ∪ B?', f'n(A) = {len(A)}, n(B) = {len(B)}, gemeinsam {len(S)}: {len(A)} + {len(B)} − {len(S)} = {len(U)}.',
                    'Zähle die gemeinsamen Elemente nur einmal.', len(U), f'{len(A)} + {len(B)} - {len(S)}')
    if art == 'formel':
        a, b = R.randint(5, 20), R.randint(5, 20)
        c = R.randint(1, min(a, b) - 1)
        return zahl(f'n(A) = {a}, n(B) = {b}, n(A ∩ B) = {c}. Berechne n(A ∪ B).', f'n(A ∪ B) = {a} + {b} − {c} = {a + b - c}.',
                    'n(A ∪ B) = n(A) + n(B) − n(A ∩ B).', a + b - c, f'{a} + {b} - {c}')
    if art == 'formel_sach':
        a, b = R.randint(8, 25), R.randint(8, 25)
        c = R.randint(2, min(a, b) - 2)
        k = R.choice([('Bei einem Schulfest', 'Kinder kaufen Waffeln', 'Kinder kaufen Saft', 'kaufen beides', 'mindestens eines von beiden'),
                      ('In einer Klasse', 'Kinder haben einen Hund', 'Kinder haben eine Katze', 'haben beides', 'mindestens ein Haustier dieser Art'),
                      ('Im Feriencamp', 'Kinder machen Kanu', 'Kinder machen Klettern', 'machen beides', 'mindestens eine der beiden Sportarten')])
        return zahl(f'{k[0]}: {a} {k[1]}, {b} {k[2]}, {c} {k[3]}. Wie viele Kinder machen {k[4]}?' if 'machen' in k[3] else
                    f'{k[0]}: {a} {k[1]}, {b} {k[2]}, {c} {k[3]}. Wie viele Kinder haben {k[4]}?' if 'haben' in k[3] else
                    f'{k[0]}: {a} {k[1]}, {b} {k[2]}, {c} {k[3]}. Wie viele Kinder kaufen {k[4]}?',
                    f'n(A ∪ B) = {a} + {b} − {c} = {a + b - c}. Die {c} Kinder mit beidem wurden sonst doppelt gezählt.',
                    'Wer beides macht, steckt in beiden Zahlen. Zieh diese Kinder einmal ab.', a + b - c, f'{a} + {b} - {c}')
    # rueck: Schnitt aus Vereinigung
    a, b = R.randint(8, 20), R.randint(8, 20)
    c = R.randint(1, min(a, b) - 1)
    u = a + b - c
    return zahl(f'n(A) = {a}, n(B) = {b} und n(A ∪ B) = {u}. Wie viele Elemente hat A ∩ B?',
                f'n(A) + n(B) = {a + b}. Das sind {a + b} − {u} = {c} mehr als n(A ∪ B) – so viele Elemente wurden doppelt gezählt: n(A ∩ B) = {c}.',
                'Vergleiche n(A) + n(B) mit n(A ∪ B). Der Unterschied sind die doppelt gezählten Elemente.', c, f'{a} + {b} - {u}')


VENN = [  # Beschriftung A, B, Gruppe, Verb A, Verb B, beides, nicht A, keins
    ('Fußball', 'Schwimmen', 'Kinder', 'spielen Fußball', 'schwimmen', 'tun beides', 'spielen nicht Fußball', 'tun keines von beiden'),
    ('Hund', 'Katze', 'Familien', 'haben einen Hund', 'haben eine Katze', 'haben beides', 'haben keinen Hund', 'haben weder Hund noch Katze'),
    ('Gitarre', 'Klavier', 'Jugendliche', 'spielen Gitarre', 'spielen Klavier', 'spielen beides', 'spielen nicht Gitarre', 'spielen keines von beiden'),
    ('Mathe-AG', 'Theater-AG', 'Kinder', 'sind in der Mathe-AG', 'sind in der Theater-AG', 'sind in beiden AGs', 'sind nicht in der Mathe-AG', 'sind in keiner der beiden AGs'),
]


def g_venn(s):
    a, c, b = R.randint(2, 15), R.randint(1, 10), R.randint(2, 15)
    d = R.randint(0, 9)
    N = a + b + c + d
    LA, LB, G, VA, VB, VC, NA, VK = R.choice(VENN)
    if s == 1:
        bild = venn(dz(a), dz(c), dz(b), dz(d), A=LA, B=LB, G=f'{N} {G}')
        frage, wert_, c_, w = R.choice([
            (f'Wie viele {G} {VA}?', a + c, f'{a} + {c}', f'Ganzer Kreis {LA}: {a} + {c} = {a + c}.'),
            (f'Wie viele {G} {VB}?', b + c, f'{b} + {c}', f'Ganzer Kreis {LB}: {b} + {c} = {b + c}.'),
            (f'Wie viele {G} {VC}?', c, f'{c}', f'Der Überlappungsbereich zeigt {c}.'),
            (f'Wie viele {G} {VK}?', d, f'{d}', f'Außerhalb der Kreise steht {d}.')])
        return mit_grafik(zahl('Lies das Venn-Diagramm ab. ' + frage, w, 'Ein ganzer Kreis besteht aus zwei Bereichen: „nur“ und Überlappung.', wert_, c_), bild)
    if s == 2:
        bild = venn(dz(a), dz(c), dz(b), dz(d), A=LA, B=LB, G=f'{N} {G}')
        frage, wert_, c_, w = R.choice([
            (f'Wie viele {G} gehören zu mindestens einem der beiden Kreise ({LA} oder {LB})?', a + b + c, f'{a} + {c} + {b}', f'Alle Bereiche in den Kreisen: {a} + {c} + {b} = {a + b + c}.'),
            (f'Wie viele {G} sind es insgesamt?', N, f'{a} + {c} + {b} + {d}', f'Alle vier Bereiche: {a} + {c} + {b} + {d} = {N}.'),
            (f'Wie viele {G} gehören zu genau einem der beiden Kreise?', a + b, f'{a} + {b}', f'Nur {LA} und nur {LB}: {a} + {b} = {a + b}.'),
            (f'Wie viele {G} {NA}?', b + d, f'{b} + {d}', f'Außerhalb des Kreises {LA}: {b} + {d} = {b + d}.')])
        return mit_grafik(zahl('Lies das Venn-Diagramm ab. ' + frage, w, 'Überlege, welche der vier Bereiche zur Frage gehören, und addiere sie.', wert_, c_), bild)
    A, B = a + c, b + c
    vor = f'{N} {G} wurden befragt: {A} {VA}, {B} {VB}, {c} {VC}.'
    bild = venn('?', dz(c), '?', '?', A=LA, B=LB, G=f'{N} {G}')
    frage, wert_, c_, w = R.choice([
        (f' Wie viele gehören nur zu „{LA}“?', a, f'{A} - {c}', f'Nur {LA}: {A} − {c} = {a}.'),
        (f' Wie viele gehören nur zu „{LB}“?', b, f'{B} - {c}', f'Nur {LB}: {B} − {c} = {b}.'),
        (f' Wie viele {VK}?', d, f'{N} - ({A} - {c}) - {c} - ({B} - {c})', f'Nur {LA}: {a}, nur {LB}: {b}. Außerhalb: {N} − {a} − {c} − {b} = {d}.')])
    return mit_grafik(zahl(vor + frage, w, 'Trage zuerst die Überlappung ein und ziehe sie von den Kreiszahlen ab.', wert_, c_), bild)


def g_verstehen(s):
    art = R.choice({1: ['schnitt_groesse', 'leer'], 2: ['teilmenge', 'fehler_union', 'schnitt_groesse'], 3: ['fehler_union', 'teilmenge', 'fehler_venn', 'grenzen']}[s])
    if art == 'schnitt_groesse':
        a, b = R.randint(3, 9), R.randint(3, 9)
        r = f'Höchstens {min(a, b)}'
        return auswahl(f'A hat {a} Elemente, B hat {b} Elemente. Wie viele Elemente kann A ∩ B höchstens haben?', r,
                       [f'Höchstens {a + b}', f'Genau {a + b}', f'Mindestens {max(a, b)}'],
                       f'A ∩ B liegt in A und in B. Also hat A ∩ B höchstens so viele Elemente wie die kleinere Menge: {min(a, b)}.',
                       'Die Schnittmenge ist ein Teil von A und auch ein Teil von B.')
    if art == 'leer':
        x = R.choice([(2, 'gerade'), (3, 'durch 3 teilbar')])
        N = R.choice([10, 20, 30])
        return auswahl(f'A = die geraden Zahlen von 1 bis {N}, B = die ungeraden Zahlen von 1 bis {N}. Welche Aussage stimmt?', 'A ∩ B = { }',
                       [f'A ∩ B = {{1; 2; …; {N}}}', 'A ∪ B = { }', 'A = B'],
                       f'Keine Zahl ist zugleich gerade und ungerade. Die Schnittmenge ist leer; die Vereinigung sind alle Zahlen 1 bis {N}.',
                       'Gibt es eine Zahl, die gerade und ungerade ist?')
    if art == 'teilmenge':
        k = R.choice([4, 6, 8, 10])
        N = R.choice([20, 24, 30, 40])
        A = [z for z in range(1, N + 1) if z % k == 0]
        B = [z for z in range(1, N + 1) if z % 2 == 0]
        aus = R.choice(['schnitt', 'union'])
        if aus == 'schnitt':
            return auswahl(f'A = die Vielfachen von {k} bis {N}, B = die geraden Zahlen bis {N}. Was ist A ∩ B?', 'A ∩ B = A',
                           ['A ∩ B = B', 'A ∩ B = { }', 'A ∩ B = A ∪ B'],
                           f'Jedes Vielfache von {k} ist gerade, also liegt A ganz in B (A ⊆ B). Dann ist die Schnittmenge A selbst: {menge(A)}.',
                           f'Ist jedes Vielfache von {k} gerade?')
        return auswahl(f'A = die Vielfachen von {k} bis {N}, B = die geraden Zahlen bis {N}. Was ist A ∪ B?', 'A ∪ B = B',
                       ['A ∪ B = A', 'A ∪ B = { }', f'A ∪ B hat {len(A) + len(B)} Elemente'],
                       f'A liegt ganz in B (A ⊆ B). Die Vereinigung bringt nichts Neues dazu: A ∪ B = B mit {len(B)} Elementen.',
                       'Kommt durch A ein Element dazu, das nicht schon in B ist?')
    if art == 'fehler_union':
        a, b = R.randint(6, 15), R.randint(6, 15)
        c = R.randint(2, min(a, b) - 1)
        r = f'Falsch: {c} Elemente wurden doppelt gezählt, richtig ist {a + b - c}.'
        return auswahl(f'n(A) = {a}, n(B) = {b}, n(A ∩ B) = {c}. Tom rechnet: n(A ∪ B) = {a} + {b} = {a + b}. Stimmt das?', r,
                       [f'Richtig, man addiert immer beide Anzahlen.', f'Falsch, richtig ist {a + b + c}.', f'Falsch, richtig ist {abs(a - b)}.'],
                       f'Die {c} gemeinsamen Elemente stecken in n(A) und in n(B). Also {a} + {b} − {c} = {a + b - c}.',
                       'Welche Elemente kommen in beiden Anzahlen vor?')
    if art == 'fehler_venn':
        A, B = R.randint(10, 20), R.randint(10, 20)
        c = R.randint(2, min(A, B) - 2)
        r = f'Falsch: Nur {B} liegt außen; in den Kreis „nur B“ gehört {B - c}.'
        return auswahl(f'{A} Kinder spielen Handball, {B} Volleyball, {c} spielen beides. Lea schreibt ins Venn-Diagramm: Überlappung {c}, nur Handball {A - c}, nur Volleyball {B}. Was ist falsch?',
                       f'„Nur Volleyball“ müsste {B - c} sein.', [f'Die Überlappung müsste {A + B} sein.', f'„Nur Handball“ müsste {A} sein.', 'Alles ist richtig.'],
                       f'Die {B} Volleyballer enthalten die {c}, die beides spielen. Nur Volleyball: {B} − {c} = {B - c}.',
                       'Prüfe jeden Bereich: Ist die Überlappung schon abgezogen?')
    # grenzen: kleinste mögliche Vereinigung
    a, b = R.randint(6, 15), R.randint(6, 15)
    return zahl(f'A hat {a} Elemente, B hat {b} Elemente. Wie viele Elemente hat A ∪ B mindestens?',
                f'Am wenigsten, wenn die kleinere Menge ganz in der größeren liegt. Dann hat A ∪ B so viele Elemente wie die größere: {max(a, b)}.',
                'Wann überlappen sich A und B am meisten?', max(a, b), f'max({a}, {b})')


GEN = {'elemente': g_elemente, 'schnitt': g_schnitt, 'vereinigung': g_vereinigung, 'venn': g_venn, 'verstehen': g_verstehen}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

def _zs(**kw):
    return {'typ': 'zahlenstrahl', 'start': 0, 'ende': 10, 'abschnitte': 10, 'beschriftet': 'alle', **kw}


def _pk(*w):
    return [{'wert': x, 'name': n} for x, n in w]


def _v(*a, **kw):
    """venn() aus _ib, aber die Kreisnamen A/B an die Außenkanten gerückt (Schrift ist seit 16.11. größer, lange Namen überlappten)."""
    b = venn(*a, **kw)
    na, nb = kw.get('A', 'A'), kw.get('B', 'B')
    for k in b['kreise']:
        if k.get('r') == 0 and k.get('name') == na:
            k['m'][0] = -4.4
        elif k.get('r') == 0 and k.get('name') == nb:
            k['m'][0] = round(7.3 - (len(nb) * 9.6 + 10) / 15.3, 3)
    return b


_FS = dict(A='Fußball', B='Schwimmen', G='30 Kinder')
UMBAU = {
    'elemente': {
        'einstieg': 'In deiner Federmappe liegen Stifte, ein Radierer und ein Lineal. Alles zusammen ist eine Sammlung. '
                    'In Mathe heißt so eine Sammlung ⟦Menge⟧, die Dinge darin sind ihre Elemente.',
        'woerter': [['Menge', 'eine Sammlung von Dingen in geschweiften Klammern, z. B. {2; 4; 6}'],
                    ['Element', 'ein Ding, das zur Menge gehört'],
                    ['∈', '„ist Element von“; ∉ heißt „ist nicht Element von“']],
        'bild': _zs(),
        'schritte': [
            {'text': 'A sind die Teiler von 10. Prüfe 1 bis 10: Was geht auf?'},
            {'text': '10 : 1, 10 : 2, 10 : 5 und 10 : 10 gehen auf.',
             'bild': {'punkte': _pk((1, '1'), (2, '2'), (5, '5'), (10, '10'))}},
            {'text': 'A = {1; 2; 5; 10} hat ⟦4 Elemente⟧.'},
            {'text': 'Also ist ⟦2 ∈ A⟧, aber 4 ∉ A.'},
        ],
        'fehler': 'Nur {2; 5} ist falsch. ⟦1 und die Zahl selbst⟧ sind immer Teiler.',
        'fehler_bild': {'punkte': _pk((1, 'fehlt'), (2, '2'), (5, '5'), (10, 'fehlt'))},
        'regel': 'Eine Menge schreibt man in { }. ⟦3 ∈ A⟧ heißt: 3 gehört zu A. Jedes Element zählt nur einmal.',
    },
    'schnitt': {
        'einstieg': 'Zwei Freunde vergleichen ihre Sticker-Listen. Welche Nummern haben beide? '
                    'Genau diese Nummern bilden die ⟦Schnittmenge⟧.',
        'woerter': [['Schnittmenge', 'A ∩ B: alles, was in A und in B ist'],
                    ['Venn-Diagramm', 'Bild mit zwei Kreisen; die Überlappung ist A ∩ B'],
                    ['leere Menge', '{ }: eine Menge ohne Elemente']],
        'bild': _v('', '', '', None),
        'schritte': [
            {'text': 'Sticker von A: die Teiler von 12. Von B: die geraden Zahlen bis 12.'},
            {'text': 'Gemeinsam sind 2, 4, 6 und 12: im Venn-Diagramm in die Mitte.', 'bild': _v('', '2; 4; 6; 12', '', None)},
            {'text': 'Der Rest kommt außen in die Kreise.', 'bild': _v('1; 3', '2; 4; 6; 12', '8; 10', None)},
            {'text': 'Also ist ⟦A ∩ B = {2; 4; 6; 12}⟧.'},
            {'text': 'Hätten sie nichts gemeinsam, wäre A ∩ B die leere Menge { }.'},
        ],
        'fehler': 'Alle Zahlen beider Listen sind nicht die Schnittmenge. In A ∩ B kommt nur, was in ⟦beiden⟧ Mengen steht.',
        'regel': 'A ∩ B: alles, was in A ⟦und⟧ in B ist. Im Venn-Diagramm ist das die Überlappung.',
    },
    'vereinigung': {
        'einstieg': 'Die beiden Freunde kleben ihre Sticker zusammen in ein Album. Doppelte Sticker kommen nur einmal hinein. '
                    'Das Album zeigt die ⟦Vereinigungsmenge⟧.',
        'woerter': [['Vereinigungsmenge', 'A ∪ B: alles, was in A oder in B ist'],
                    ['n(A)', 'die Anzahl der Elemente von A']],
        'bild': _v('', '', '', None),
        'schritte': [
            {'text': 'A = {1; 3; 5; 7; 9} und B = {3; 6; 9}.'},
            {'text': 'Gemeinsam sind 3 und 9, sie kommen in die Mitte.', 'bild': _v('', '3; 9', '', None)},
            {'text': 'A ∪ B = {1; 3; 5; 6; 7; 9}.', 'bild': _v('1; 5; 7', '3; 9', '6', None)},
            {'text': 'Anzahl: n(A) + n(B) − 2 = 5 + 3 − 2 = ⟦6⟧.'},
        ],
        'fehler': '5 + 3 = 8 ist falsch, denn 3 und 9 sind ⟦doppelt gezählt⟧. Man zieht sie einmal ab: 8 − 2 = 6.',
        'regel': 'A ∪ B: alles, was in A ⟦oder⟧ in B ist. n(A ∪ B) = n(A) + n(B) − n(A ∩ B).',
    },
    'venn': {
        'einstieg': 'In einer Klasse mit 30 Kindern spielen 18 Fußball und 14 schwimmen. 6 Kinder machen beides. '
                    'Wie viele machen keins von beiden? Das ⟦Venn-Diagramm⟧ zeigt es.',
        'woerter': [['Grundmenge', 'alle, um die es geht; im Bild das Rechteck'],
                    ['weder noch', 'in keinem der beiden Kreise']],
        'bild': _v('', '', '', None, **_FS),
        'schritte': [
            {'text': 'Die Grundmenge sind 30 Kinder. Zuerst die Überlappung: 6.', 'bild': _v('', '6', '', None, **_FS)},
            {'text': 'Nur Fußball: 18 − 6 = 12. Nur Schwimmen: 14 − 6 = 8.', 'bild': _v('12', '6', '8', None, **_FS)},
            {'text': 'Weder noch: 30 − 12 − 6 − 8 = ⟦4⟧.', 'bild': _v('12', '6', '8', '4', **_FS)},
        ],
        'fehler': '„Nur Fußball = 18“ ist falsch. Die 18 enthält auch die 6, die schwimmen. Erst ⟦die Überlappung abziehen⟧.',
        'fehler_bild': _v('18', '6', '14', '?', **_FS),
        'regel': 'Im Venn-Diagramm zuerst die ⟦Überlappung⟧ eintragen. Dann „nur A“, „nur B“ und außerhalb.',
    },
    'verstehen': {
        'einstieg': 'Jemand behauptet: „A hat 5 Elemente, B hat 4. Also hat A ∩ B 9 Elemente.“ Stimmt das? '
                    'Mit einem ⟦Beispiel⟧ kannst du solche Aussagen prüfen.',
        'woerter': [['Gegenbeispiel', 'ein Beispiel, bei dem die Aussage nicht stimmt'],
                    ['Teilmenge', 'A ⊆ B: Jedes Element von A liegt auch in B']],
        'bild': _v('1; 2; 3', '4; 5', '6; 7', None),
        'schritte': [
            {'text': 'Beispiel: A = {1; 2; 3; 4; 5}, B = {4; 5; 6; 7}.'},
            {'text': 'A ∩ B = {4; 5} hat nur 2 Elemente.'},
            {'text': 'A ∩ B liegt ganz in A, hat also höchstens 5 Elemente.'},
            {'text': '⟦Die Aussage ist falsch⟧. Das Beispiel ist ein Gegenbeispiel.'},
            {'text': 'Ist A eine Teilmenge von B, gilt sogar A ∩ B = A.'},
        ],
        'fehler': 'n(A ∪ B) = n(A) + n(B) gilt nicht immer. Es stimmt ⟦nur ohne gemeinsame Elemente⟧.',
        'regel': 'Die Schnittmenge ist ⟦nie größer⟧ als A oder B. Prüfe Aussagen mit einem Beispiel oder Venn-Diagramm.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


d = bauen('mengen.grundbegriffe',
      'Mengen aufschreiben, Schnitt- und Vereinigungsmengen bilden und mit Venn-Diagrammen zählen.',
      ['Menge (set): Elemente in { }, jedes nur einmal. 3 ∈ A: 3 gehört zu A.',
       'A ∩ B (intersection): in A und in B. A ∪ B (union): in A oder in B.',
       'n(A ∪ B) = n(A) + n(B) − n(A ∩ B).',
       'Venn-Diagramm: zuerst die Überlappung eintragen.'],
      [('Mengen', ['elemente']), ('Schnitt und Vereinigung', ['schnitt', 'vereinigung']), ('Venn-Diagramme', ['venn', 'verstehen'])],
      ETAPPEN, GEN,
      offen=['Umfang laut Themenliste: Elemente, Schnitt, Vereinigung (IB MYP 1). Komplement nur als Bereich „außerhalb“ im Venn-Diagramm, Mengen-Wahrscheinlichkeiten nicht enthalten (eigenes Thema).',
             'Venn-Diagramme mit der Figur-Zeichnung gebaut: zwei Kreise + Rechteck (Grundmenge); Beschriftungen als Namen unsichtbarer Hilfskreise (Radius 0), damit keine Punkt-Marker erscheinen. Mit dem Zeichencode der App nachgeprüft. Eine eigene Zeichenart „venn“ wäre robuster.',
             'Mengenschreibweise mit Semikolon {1; 2; 3}, damit Dezimalkommas eindeutig bleiben.'],
      vertiefung=['verstehen'])
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
