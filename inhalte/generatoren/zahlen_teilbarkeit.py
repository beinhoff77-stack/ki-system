#!/usr/bin/env python3
"""Thema zahlen.teilbarkeit – Teilbarkeit und Primzahlen (Gymnasium Bayern, Klasse 5). Runde 9: Aufgaben auffüllen.

Lernkarten unverändert aus inhalte/klar/zahlen.teilbarkeit.json; neu sind nur die Aufgaben.
Schreibweise Klasse 5: Malpunkt sichtbar (4 · 9), große Zahlen mit Leerzeichen ab 10 000.
"""
import math
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _auffuellen import A, L, Z, baue, etappen_aus_klar, g4 as zt  # noqa: E402

META = {'thema_schluessel': 'zahlen.teilbarkeit', 'thema_id': 17, 'block_id': 48, 'klasse': {'gym_by': 5}}
TITEL = [('teiler', 'Teiler finden'), ('vielfache', 'Vielfache'), ('endziffer', 'Teilbar durch 2, 5 und 10'),
         ('quersumme', 'Teilbar durch 3 und 9'), ('primzahl', 'Primzahlen'), ('primfaktoren', 'In Primzahlen zerlegen'),
         ('ggt', 'Größter gemeinsamer Teiler (ggT)'), ('kgv', 'Kleinstes gemeinsames Vielfaches (kgV)')]
ETAPPEN = etappen_aus_klar(META['thema_schluessel'], TITEL)
HF = 'Trage in jedes Feld eine Zahl ein.'


def teiler(n): return [d for d in range(1, n + 1) if n % d == 0]
def prim(n): return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))
def liste(xs): return ', '.join(zt(x) for x in xs)
def qs(n): return sum(int(c) for c in str(n))
def zerlegung(n):
    f, d = [], 2
    while n > 1:
        while n % d == 0: f.append(d); n //= d
        d += 1
    return f
def kgv(a, b): return a * b // math.gcd(a, b)
UNGERADE_NICHTPRIM = [9, 15, 21, 25, 27, 33, 35, 39, 45, 49, 51, 55, 57, 63, 65, 69, 75, 77, 81, 85, 87, 91, 93, 95, 99]
PRIM = [p for p in range(2, 200) if prim(p)]


# ---------------- Teiler ----------------
def g_teiler(R, s):
    if s == 1:
        a, b = R.randint(2, 9), R.randint(2, 12)
        n = a * b
        return L(f'Ergänze das Teilerpaar von {n}: {a} · □ = {n}', f'{a} · □ = {n}', [b], [f'{n} // {a}'],
                 f'{n} : {a} = {b}, denn {a} · {b} = {n}. Also sind {a} und {b} Teiler von {n}.', f'Rechne {n} : {a}.', HF)
    n = R.choice([18, 20, 24, 28, 30, 32, 36, 40, 42, 44, 45, 48, 50, 54, 56, 60, 63, 64, 72, 75, 80, 84, 90, 96, 100])
    t = teiler(n)
    if s == 2:
        ohne_rand = [x for x in t if x not in (1, n)]
        mitte = t[len(t) // 2]
        falsch1 = ohne_rand
        falsch2 = [x for x in t if x != mitte]
        nicht = next(x for x in range(2, n) if n % x)
        falsch3 = sorted(t + [nicht])
        return A(R, f'Welche Liste enthält genau alle Teiler von {n}?', liste(t), [liste(falsch1), liste(falsch2), liste(falsch3)],
                 f'Teilerpaare: {", ".join(f"{d} · {n // d}" for d in t if d * d <= n)}. Teiler: {liste(t)} – das sind {len(t)}.',
                 'Suche Teilerpaare. Fang bei 1 an und hör auf, wenn sich die Paare wiederholen.')
    art = R.choice(['gruppen', 'fehler', 'quadrat'])
    if art == 'gruppen':
        g = [x for x in t if 2 <= x <= n // 2]
        return A(R, f'{n} Kinder sollen in gleich große Gruppen aufgeteilt werden, jede Gruppe mit mindestens 2 Kindern. Keiner bleibt übrig, es gibt mindestens 2 Gruppen. Wie viele verschiedene Gruppengrößen sind möglich?',
                 str(len(g)), [str(len(g) + 1), str(len(g) + 2), str(len(t))],
                 f'Gruppengrößen sind Teiler von {n} ohne 1 und ohne {n}: {liste(g)}. Das sind {len(g)} Möglichkeiten.',
                 f'Welche Teiler von {n} passen? 1 und {n} fallen weg.')
    if art == 'quadrat':
        q = R.choice([16, 25, 36, 49, 64, 81, 100])
        tq = teiler(q)
        r = int(q ** .5)
        return A(R, f'Wie viele Teiler hat {q}?', str(len(tq)), [str(len(tq) + 1), str(len(tq) - 1), str(len(tq) + 2)],
                 f'Teilerpaare: {", ".join(f"{d} · {q // d}" for d in tq if d * d <= q)}. Bei {r} · {r} zählt die {r} nur einmal: {liste(tq)} – {len(tq)} Teiler.',
                 'Bei einer Quadratzahl gibt es ein Paar mit zwei gleichen Zahlen.')
    k = R.choice([x for x in t if 1 < x < n])
    return A(R, f'Jemand sagt: „{k} ist ein Teiler von {n}, also ist auch {n} ein Teiler von {k}.“ Stimmt das?',
             f'Nein. {n} ist ein Vielfaches von {k}, kein Teiler.', ['Ja, Teiler funktionieren in beide Richtungen.', f'Ja, denn {n} : {k} = {n // k}.'],
             f'{k} geht in {n} auf: {n} : {k} = {n // k}. Aber {n} ist größer als {k} und passt nicht ohne Rest in {k}. Ein Teiler ist nie größer als die Zahl.',
             'Kann eine größere Zahl ein Teiler einer kleineren sein?')


# ---------------- Vielfache ----------------
def g_vielfache(R, s):
    if s == 1:
        a, k = R.randint(3, 12), R.randint(3, 10)
        if R.random() < .5:
            return Z(f'Nenne das {k}. Vielfache von {a} (zähle mit {a} als 1. Vielfachem).', a * k, f'{k} * {a}',
                     f'Die Vielfachen von {a}: {liste([a * i for i in range(1, k + 1)])}. Das {k}. ist {k} · {a} = {a * k}.', f'Das ist das Einmaleins mit {a}: {k} · {a}.')
        g = R.randint(a + 5, 10 * a)
        if g % a == 0: g += 1
        e = (g // a + 1) * a
        return Z(f'Welches ist das kleinste Vielfache von {a}, das größer als {g} ist?', e, f'({g} // {a} + 1) * {a}',
                 f'{g // a} · {a} = {g // a * a} ist noch zu klein. Das nächste Vielfache: {g // a + 1} · {a} = {e}.', f'Zähle in {a}er-Schritten bis über {g}.')
    if s == 2:
        a = R.randint(6, 15)
        if R.random() < .5:
            g = R.randint(50, 150)
            return Z(f'Wie viele Vielfache von {a} liegen zwischen 1 und {g}?', g // a, f'{g} // {a}',
                     f'{g} : {a} = {g // a} Rest {g % a}. Also gibt es {g // a} Vielfache: {a}, {2 * a}, … bis {g // a * a}.', f'Wie oft passt {a} in {g}?')
        k = R.randint(3, 9)
        w = a * k
        return A(R, f'Welche Zahl ist ein Vielfaches von {a}?', zt(w), [zt(w + 1), zt(w - 2), zt(w + a // 2 + 1)],
                 f'{w} = {k} · {a}, also ist {w} ein Vielfaches von {a}. Die anderen Zahlen liegen zwischen zwei Vielfachen.',
                 f'Teile jede Zahl durch {a}: Geht es ohne Rest?')
    art = R.choice(['packung', 'fehler', 'bus'])
    if art == 'packung':
        a, n = R.choice([4, 6, 8, 10, 12]), R.randint(25, 95)
        if n % a == 0: n += 1
        e = -(-n // a) * a
        return Z(f'Muffins gibt es nur in Packungen zu {a} Stück. Du brauchst mindestens {n} Muffins. Wie viele Muffins kaufst du mindestens?', e, f'({n} + {a} - 1) // {a} * {a}',
                 f'Vielfache von {a}: … {e - a}, {e}. {e - a} reicht nicht, {e} schon. Das sind {e // a} Packungen.', f'Suche das kleinste Vielfache von {a}, das mindestens {n} ist.')
    if art == 'bus':
        a, k = R.choice([5, 10, 12, 15, 20]), R.randint(3, 6)
        return Z(f'Ein Bus fährt um 8:00 Uhr und dann alle {a} Minuten. Wie viele Minuten nach 8:00 Uhr fährt der {k + 1}. Bus?', k * a, f'{k} * {a}',
                 f'Die Abfahrten nach 8:00 Uhr sind Vielfache von {a}: {liste([a * i for i in range(1, k + 1)])}. Der {k + 1}. Bus fährt nach {k * a} Minuten.',
                 'Der 1. Bus fährt nach 0 Minuten.')
    a, k = R.randint(3, 9), R.randint(3, 8)
    return A(R, f'Jemand sagt: „{a * k} ist ein Vielfaches von {a}, also ist {a} ein Vielfaches von {a * k}.“ Stimmt das?',
             f'Nein. {a} ist ein Teiler von {a * k}, kein Vielfaches.', ['Ja, das gilt immer in beide Richtungen.', f'Ja, denn {a * k} : {a} = {k}.'],
             f'{a * k} = {k} · {a} ist ein Vielfaches von {a}. Ein Vielfaches von {a * k} wäre aber mindestens {a * k}. {a} ist kleiner, also ein Teiler.',
             'Ein Vielfaches ist nie kleiner als die Zahl.')


# ---------------- Endziffer ----------------
def _endziffer_text(n):
    d = [k for k in (2, 5, 10) if n % k == 0]
    if not d: return 'durch keine dieser Zahlen'
    if len(d) == 3: return 'durch 2, 5 und 10'
    return 'nur durch ' + ' und '.join(map(str, d))


def g_endziffer(R, s):
    OPT = ['durch 2, 5 und 10', 'nur durch 2', 'nur durch 5', 'durch keine dieser Zahlen']
    if s == 1:
        n = R.randint(100, 9999)
        r = _endziffer_text(n)
        return A(R, f'Durch welche der Zahlen 2, 5 und 10 ist {zt(n)} teilbar?', r, [o for o in OPT if o != r],
                 f'Die Endziffer ist {n % 10}. {"Gerade: durch 2 teilbar. " if n % 2 == 0 else "Ungerade: nicht durch 2. "}'
                 f'{"0 oder 5: durch 5. " if n % 5 == 0 else "Nicht 0 oder 5: nicht durch 5. "}{"0: durch 10." if n % 10 == 0 else "Nicht 0: nicht durch 10."}',
                 'Schau nur auf die letzte Ziffer.')
    if s == 2:
        art = R.choice(['5nicht10', 'rest'])
        if art == 'rest':
            n, k = R.randint(1000, 99999), R.choice([2, 5, 10])
            return Z(f'Welcher Rest bleibt bei {zt(n)} : {k}?', n % k, f'{n} % {k}',
                     f'Bei {k} entscheidet die Endziffer {n % 10}: {n % 10} : {k} lässt den Rest {n % 10 % k}. Also bleibt Rest {n % k}.',
                     'Für 2, 5 und 10 reicht die letzte Ziffer, auch für den Rest.')
        b = R.randint(100, 999) * 10
        r = b + 5
        return A(R, 'Welche Zahl ist durch 5, aber nicht durch 10 teilbar?', zt(r), [zt(b), zt(b + 2), zt(b + 8)],
                 f'{zt(r)} endet auf 5: durch 5, aber nicht durch 10. {zt(b)} endet auf 0 und ist auch durch 10 teilbar.',
                 'Durch 10 heißt Endziffer 0, durch 5 heißt Endziffer 0 oder 5.')
    art = R.choice(['fehler', 'ziffer', 'ziffer'])
    if art == 'ziffer':
        v = R.randint(100, 999)
        wahl = R.choice([('durch 2 und durch 5', 0), ('durch 5, aber nicht durch 2', 5)])
        return L(f'Welche Ziffer muss für □ stehen, damit {v}□ {wahl[0]} teilbar ist?', f'{v}□', [wahl[1]], [f'({v} * 10 + {wahl[1]}) % 10'],
                 f'{"Durch 2 und 5 heißt: Endziffer 0." if wahl[1] == 0 else "Durch 5 heißt Endziffer 0 oder 5; nicht durch 2 heißt ungerade: also 5."} Die Zahl heißt {v}{wahl[1]}.',
                 'Welche Endziffern passen zu beiden Bedingungen?', 'Trage die fehlende Ziffer ein.')
    g = R.choice([2, 4, 6, 8])
    n = int(f'{g}{R.randint(10, 99)}{R.choice([1, 3, 5, 7, 9])}')
    return A(R, f'Jemand sagt: „{zt(n)} beginnt mit {g}, also ist die Zahl durch 2 teilbar.“ Stimmt das?', f'Nein. Die Endziffer {n % 10} ist ungerade.',
             ['Ja, die erste Ziffer ist gerade.', 'Ja, die Zahl ist groß genug.', 'Das kann man nicht prüfen.'],
             f'Für die Teilbarkeit durch 2 zählt nur die letzte Ziffer. {n % 10} ist ungerade, also ist {zt(n)} nicht durch 2 teilbar.', 'Welche Ziffer ist entscheidend?')


# ---------------- Quersumme ----------------
def g_quersumme(R, s):
    if s == 1:
        n = R.randint(1000, 99999)
        z = list(str(n))
        return Z(f'Berechne die Quersumme von {zt(n)}.', qs(n), ' + '.join(z), f'Alle Ziffern zusammenzählen: {" + ".join(z)} = {qs(n)}.', 'Zähle alle Ziffern zusammen.')
    if s == 2:
        n = R.randint(1000, 99999)
        q = qs(n)
        r = 'durch 3 und durch 9' if q % 9 == 0 else 'durch 3, aber nicht durch 9' if q % 3 == 0 else 'weder durch 3 noch durch 9'
        return A(R, f'Ist {zt(n)} durch 3 oder durch 9 teilbar?', r, [o for o in ['durch 3 und durch 9', 'durch 3, aber nicht durch 9', 'weder durch 3 noch durch 9', 'nur durch 9'] if o != r],
                 f'Quersumme: {" + ".join(str(n))} = {q}. {q} ist {"durch 9 (und damit durch 3)" if q % 9 == 0 else "durch 3, aber nicht durch 9" if q % 3 == 0 else "weder durch 3 noch durch 9"} teilbar.',
                 'Berechne die Quersumme und prüfe sie.')
    art = R.choice(['ziffer9', 'ziffer3', 'fehler'])
    if art == 'ziffer9':
        a = R.randint(10, 99)
        d = (9 - qs(a) % 9) % 9
        if d == 0: return g_quersumme(R, s)
        return L(f'Welche Ziffer muss für □ stehen, damit {a}□ durch 9 teilbar ist?', f'{a}□', [d], [f'(9 - ({" + ".join(str(a))}) % 9) % 9'],
                 f'Quersumme ohne □: {" + ".join(str(a))} = {qs(a)}. Bis zur nächsten durch 9 teilbaren Zahl {"fehlt" if d == 1 else "fehlen"} {d}. Probe: {a}{d} hat die Quersumme {qs(a) + d}.',
                 'Die Quersumme muss durch 9 teilbar sein. Wie viel fehlt bis zur nächsten Neunerzahl?', 'Trage die fehlende Ziffer ein.')
    if art == 'ziffer3':
        a = R.randint(100, 999)
        d = [x for x in range(10) if (qs(a) + x) % 3 == 0]
        return A(R, f'Welche Ziffern kann man für □ einsetzen, damit {a}□ durch 3 teilbar ist?', ', '.join(map(str, d)),
                 [', '.join(map(str, [x for x in range(10) if (qs(a) + x) % 3 == 1])), ', '.join(map(str, [x for x in range(10) if (qs(a) + x) % 3 == 2])), str(d[0])],
                 f'Quersumme ohne □: {qs(a)}. Mit {", ".join(map(str, d))} wird die Quersumme durch 3 teilbar.',
                 'Probiere, welche Ziffern die Quersumme zu einer Dreierzahl machen.')
    n = R.choice([x for x in range(100, 999) if qs(x) % 4 == 0 and x % 4 and qs(x) % 3])
    return A(R, f'Jemand sagt: „{n} hat die Quersumme {qs(n)}. {qs(n)} ist durch 4 teilbar, also auch {n}.“ Stimmt das?',
             'Nein. Die Quersummenregel gilt nur für 3 und 9.', ['Ja, die Regel gilt für alle Zahlen.', f'Ja, denn {qs(n)} : 4 = {qs(n) // 4}.'],
             f'{n} : 4 geht nicht auf (Rest {n % 4}). Die Quersumme hilft nur bei 3 und 9.', 'Für welche Teiler gilt die Quersummenregel?')


# ---------------- Primzahlen ----------------
def g_primzahl(R, s):
    if s == 1:
        p = R.choice([q for q in PRIM if 10 < q < 100])
        f = R.sample([x for x in UNGERADE_NICHTPRIM if abs(x - p) < 40], 3)
        return A(R, 'Welche Zahl ist eine Primzahl?', str(p), [str(x) for x in f],
                 f'{p} hat nur die Teiler 1 und {p}. ' + ' '.join(f'{x} = {zerlegung(x)[0]} · {x // zerlegung(x)[0]}.' for x in f),
                 'Prüfe, ob 2, 3, 5 oder 7 aufgehen.')
    if s == 2:
        if R.random() < .5:
            p = R.choice([q for q in PRIM if 30 < q < 150])
            return A(R, f'Ist {p} eine Primzahl?', 'Ja, keine der Zahlen 2, 3, 5, 7, 11 geht auf.',
                     ['Nein, sie ist durch 3 teilbar.', 'Nein, sie ist durch 7 teilbar.'],
                     f'{p} ist ungerade, die Quersumme {qs(p)} ist nicht durch 3 teilbar, die Endziffer ist nicht 0 oder 5. Auch 7 und 11 gehen nicht auf: {p} ist eine Primzahl.',
                     'Teste der Reihe nach 2, 3, 5, 7 und 11.')
        n = R.choice([x for x in range(30, 150) if x % 2 and not prim(x) and x % 5])
        q = zerlegung(n)[0]
        return A(R, f'Ist {n} eine Primzahl?', f'Nein, {n} = {q} · {n // q}.', ['Ja, sie ist ungerade.', 'Ja, sie endet nicht auf 5.'],
                 f'{n} : {q} = {n // q}. Also hat {n} mehr als zwei Teiler und ist keine Primzahl.', 'Ungerade heißt noch nicht Primzahl. Teste 3, 7, 11, 13.')
    art = R.choice(['fehler', 'zwischen', 'naechste'])
    if art == 'fehler':
        x = R.choice([1, 9, 15, 21, 27, 33, 39, 49, 51])
        if x == 1:
            return A(R, 'Jemand sagt: „1 ist eine Primzahl.“ Stimmt das?', 'Nein, 1 hat nur einen Teiler.', ['Ja, 1 ist nur durch 1 teilbar.', 'Ja, 1 ist ungerade.'],
                     'Eine Primzahl hat genau zwei verschiedene Teiler. Die 1 hat nur einen: die 1.', 'Wie viele verschiedene Teiler hat 1?')
        return A(R, f'Jemand sagt: „{x} ist ungerade, also eine Primzahl.“ Stimmt das?', f'Nein, {x} = {zerlegung(x)[0]} · {x // zerlegung(x)[0]}.',
                 ['Ja, alle ungeraden Zahlen sind Primzahlen.', 'Ja, nur gerade Zahlen haben Teiler.'],
                 f'{x} ist durch {zerlegung(x)[0]} teilbar. Nicht jede ungerade Zahl ist eine Primzahl.', 'Prüfe 3, 5 und 7.')
    if art == 'naechste':
        n = R.randint(20, 120)
        p = next(q for q in PRIM if q > n)
        return A(R, f'Welches ist die kleinste Primzahl, die größer als {n} ist?', str(p),
                 [str(x) for x in sorted({p + 2, p - 1 if p - 1 > n else p + 1, next((x for x in range(n + 1, p + 20) if x % 2 and not prim(x)), p + 4)}) if x != p],
                 f'Prüfe die Zahlen nach {n} der Reihe nach: {p} ist die erste ohne weiteren Teiler.', 'Gerade Zahlen (außer 2) fallen sofort weg.')
    a = R.choice([10, 20, 30, 40, 50, 60, 70, 80])
    pz = [q for q in PRIM if a < q < a + 10]
    return A(R, f'Wie viele Primzahlen liegen zwischen {a} und {a + 10}?', str(len(pz)), [str(len(pz) + 1), str(len(pz) + 2), str(max(0, len(pz) - 1)) if len(pz) else '5'],
             f'Primzahlen zwischen {a} und {a + 10}: {liste(pz) if pz else "keine"}. Das sind {len(pz)}.', 'Nur die ungeraden Zahlen, die nicht auf 5 enden, kommen in Frage.')


# ---------------- Primfaktoren ----------------
def g_primfaktoren(R, s):
    if s == 1:
        n = R.choice([x for x in range(12, 120) if len(zerlegung(x)) == 3])
        f = zerlegung(n)
        return L(f'Zerlege {n} in Primfaktoren: {n} = □ · □ · □', f'{n} = □ · □ · □', f, [str(x) for x in f],
                 ' '.join(f'{m} : {q} = {m // q}.' for m, q in _schritte(n)) + f' Also {n} = {" · ".join(map(str, f))}.',
                 'Teile immer wieder durch die kleinste Primzahl, die passt.', 'Primfaktoren der Größe nach, die kleinste zuerst.')
    if s == 2:
        if R.random() < .5:
            n = R.choice([x for x in range(40, 400) if len(zerlegung(x)) == 4 and x != 60])
            f = zerlegung(n)
            return L(f'Zerlege {n} in Primfaktoren: {n} = □ · □ · □ · □', f'{n} = □ · □ · □ · □', f, [str(x) for x in f],
                     ' '.join(f'{m} : {q} = {m // q}.' for m, q in _schritte(n)) + f' Also {n} = {" · ".join(map(str, f))}.',
                     'Teile immer wieder durch die kleinste Primzahl, die passt.', 'Primfaktoren der Größe nach, die kleinste zuerst.')
        f = sorted(R.choices([2, 3, 5, 7, 11], k=R.randint(3, 4)))
        n = math.prod(f)
        return Z(f'Welche Zahl hat die Primfaktorzerlegung {" · ".join(map(str, f))}?', n, ' * '.join(map(str, f)),
                 f'Malnehmen: {" · ".join(map(str, f))} = {n}.', 'Nimm alle Primfaktoren miteinander mal.')
    art = R.choice(['fehler', 'welche'])
    n = R.choice([x for x in range(24, 200) if len(zerlegung(x)) >= 3 and len(set(zerlegung(x))) >= 2])
    f = zerlegung(n)
    if art == 'welche':
        a, b = f[0] * f[1], n // (f[0] * f[1])
        falsch = [f'{a} · {b}', ' · '.join(map(str, f[:-2] + [f[-2] * f[-1]])), ' · '.join(map(str, f[1:]))]
        return A(R, f'Welche ist die Primfaktorzerlegung von {n}?', ' · '.join(map(str, f)), falsch,
                 f'Nur in {" · ".join(map(str, f))} stehen ausschließlich Primzahlen, und das Produkt ist {n}.', 'Prüfe zwei Dinge: Sind alle Faktoren Primzahlen? Stimmt das Produkt?')
    a = f[0] * f[1]
    return A(R, f'Jemand schreibt: {n} = {a} · {n // a}. Ist das eine Primfaktorzerlegung?', f'Nein, {a} ist keine Primzahl.',
             ['Ja, das Produkt stimmt.', 'Ja, man darf beliebige Faktoren nehmen.'],
             f'{a} = {f[0]} · {f[1]} lässt sich weiter zerlegen. Richtig: {n} = {" · ".join(map(str, f))}.', 'Sind alle Faktoren Primzahlen?')


def _schritte(n):
    out, d = [], 2
    while n > 1:
        while n % d == 0: out.append((n, d)); n //= d
        d += 1
    return out


# ---------------- ggT ----------------
def g_ggt(R, s):
    if s == 1:
        g = R.randint(2, 9)
        p, q = R.sample(range(1, 8), 2)
        if math.gcd(p, q) != 1: return g_ggt(R, s)
        a, b = g * p, g * q
        return Z(f'Bestimme ggT({a}, {b}).', g, f'{a} // {p}',
                 f'Teiler von {a}: {liste(teiler(a))}. Teiler von {b}: {liste(teiler(b))}. Der größte gemeinsame ist {g}.',
                 'Schreib die Teiler beider Zahlen auf und suche den größten gemeinsamen.')
    if s == 2:
        g = R.randint(3, 15)
        p, q = R.sample(range(2, 9), 2)
        if math.gcd(p, q) != 1: return g_ggt(R, s)
        a, b = g * p, g * q
        if R.random() < .5:
            return Z(f'Zwei Bänder sind {a} cm und {b} cm lang. Sie sollen ohne Rest in gleich lange Stücke geschnitten werden, die möglichst lang sind. Wie lang wird ein Stück?',
                     g, f'{a} // {p}', f'Gesucht ist ggT({a}, {b}) = {g}. Probe: {a} : {g} = {p}, {b} : {g} = {q}.', 'Die Stücklänge muss in beide Längen passen.', einheit='cm')
        return Z(f'Bestimme ggT({a}, {b}).', g, f'{a} // {p}', f'{a} = {g} · {p} und {b} = {g} · {q}. {p} und {q} haben keinen gemeinsamen Teiler mehr, also ggT = {g}.',
                 'Suche den größten Teiler, der in beiden Zahlen steckt.')
    art = R.choice(['stuecke', 'fehler'])
    g = R.randint(2, 12)
    p, q = R.sample(range(2, 9), 2)
    if math.gcd(p, q) != 1: return g_ggt(R, s)
    a, b = g * p, g * q
    if art == 'stuecke':
        return Z(f'{a} Äpfel und {b} Birnen sollen so auf Körbe verteilt werden, dass alle Körbe gleich gefüllt sind und nichts übrig bleibt. Es sollen möglichst viele Körbe sein. Wie viele Körbe sind es?',
                 g, f'{a} // {p}', f'Gesucht ist ggT({a}, {b}) = {g}. Jeder Korb bekommt {p} Äpfel und {q} Birnen.', 'Die Zahl der Körbe muss in beide Anzahlen passen.')
    k = R.choice([x for x in teiler(g) if x < g] or [1])
    return A(R, f'Jemand sagt: „ggT({a}, {b}) = {k}, denn {k} teilt beide Zahlen.“ Stimmt das?', f'Nein, {g} teilt auch beide und ist größer.',
             ['Ja, ein gemeinsamer Teiler genügt.', f'Nein, der ggT ist {a}.'],
             f'{k} ist ein gemeinsamer Teiler, aber nicht der größte. {a} : {g} = {p} und {b} : {g} = {q}, also ggT = {g}.', 'Gibt es einen größeren gemeinsamen Teiler?')


# ---------------- kgV ----------------
def g_kgv(R, s):
    if s == 1:
        a, b = R.sample(range(2, 11), 2)
        l = kgv(a, b)
        return Z(f'Bestimme kgV({a}, {b}).', l, f'{max(a, b)} * {l // max(a, b)}',
                 f'Vielfache von {max(a, b)}: {liste([max(a, b) * i for i in range(1, l // max(a, b) + 1)])}. {l} ist das erste, das auch durch {min(a, b)} teilbar ist.',
                 'Geh die Vielfachen der größeren Zahl durch.')
    if s == 2:
        a, b = R.sample([4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20], 2)
        l = kgv(a, b)
        if l > 120 or l == a * b and R.random() < .5: return g_kgv(R, s)
        if R.random() < .5:
            return Z(f'Zwei Busse fahren um 7:00 Uhr gemeinsam ab. Der eine fährt alle {a} Minuten, der andere alle {b} Minuten. Nach wie vielen Minuten fahren sie wieder gemeinsam ab?',
                     l, f'{max(a, b)} * {l // max(a, b)}', f'Gesucht ist kgV({a}, {b}) = {l}. Nach {l} Minuten fahren beide wieder gleichzeitig.', 'Suche das kleinste gemeinsame Vielfache.')
        return Z(f'Bestimme kgV({a}, {b}).', l, f'{max(a, b)} * {l // max(a, b)}',
                 f'Vielfache von {max(a, b)}: {liste([max(a, b) * i for i in range(1, l // max(a, b) + 1)])}. Das erste, das auch zu {min(a, b)} passt, ist {l}.',
                 'Geh die Vielfachen der größeren Zahl durch.')
    art = R.choice(['fehler', 'packungen'])
    a, b = R.sample([4, 6, 8, 9, 10, 12, 15], 2)
    l = kgv(a, b)
    if art == 'packungen' or a * b == l:
        return Z(f'Würstchen gibt es in Packungen zu {a}, Brötchen in Packungen zu {b}. Du willst gleich viele Würstchen wie Brötchen, möglichst wenige. Wie viele Packungen Würstchen kaufst du?',
                 l // a, f'{l} // {a}', f'kgV({a}, {b}) = {l}. {l} Würstchen sind {l} : {a} = {l // a} Packungen.', 'Erst das kgV bestimmen, dann durch die Packungsgröße teilen.')
    return A(R, f'Jemand sagt: „kgV({a}, {b}) = {a * b}, denn {a} · {b} = {a * b}.“ Stimmt das?', f'Nein, schon {l} ist ein gemeinsames Vielfaches.',
             ['Ja, das kgV ist immer das Produkt.', f'Nein, das kgV ist {max(a, b)}.'],
             f'{a * b} ist gemeinsam, aber nicht das kleinste: {l} ist durch {a} und durch {b} teilbar.', 'Gibt es ein kleineres gemeinsames Vielfaches?')


GEN = {'teiler': g_teiler, 'vielfache': g_vielfache, 'endziffer': g_endziffer, 'quersumme': g_quersumme,
       'primzahl': g_primzahl, 'primfaktoren': g_primfaktoren, 'ggt': g_ggt, 'kgv': g_kgv}
VERBOT = {'teiler': ['von 12', 'von 12:'], 'vielfache': ['von 7, das größer als 30'], 'endziffer': ['3 470', '2 465'], 'quersumme': ['4 251'],
          'primzahl': ['Ist 53 '], 'primfaktoren': ['Zerlege 60 '], 'ggt': ['ggT(12, 18)'], 'kgv': ['kgV(4, 6)', 'kgV(6, 4)']}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Teiler und Vielfache', ['teiler', 'vielfache']), ('Teilbarkeitsregeln', ['endziffer', 'quersumme']),
          ('Primzahlen', ['primzahl', 'primfaktoren']), ('ggT und kgV', ['ggt', 'kgv'])],
         'Teiler und Vielfache finden, Teilbarkeit durch 2, 3, 5, 9 und 10 erkennen, Primzahlen bestimmen, Zahlen in Primfaktoren zerlegen und ggT und kgV berechnen.',
         ['Teiler findest du in Paaren.', 'Durch 2, 5, 10: Endziffer. Durch 3, 9: Quersumme.', 'Eine Primzahl hat genau zwei Teiler.',
          'ggT: größter gemeinsamer Teiler. kgV: kleinstes gemeinsames Vielfaches.'],
         verbot=VERBOT,
         offen=['Runde 9: Thema stammt aus der Zeit vor dem Bausatz; die bisherigen Aufgaben liegen nur in der Datenbank. Dieser Generator erzeugt neue Aufgaben, '
                'die beim Einspielen mit einheit_abgleichen(…, \'lassen\') dazukommen. Dubletten zu den alten Aufgaben ließen sich hier nicht prüfen, weil diese nicht im Repository liegen.',
                'Primfaktor-Lücken (□ · □ · □): Die Faktoren sind in der Reihenfolge klein → groß einzutragen; der Hinweis sagt das. Eine andere Reihenfolge würde als falsch gewertet.'])
