#!/usr/bin/env python3
"""Thema funktionen.reihen – Reihen (IB MYP 4, etwa Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403
from _rsib2 import PLAN2, art3  # noqa: E402

start(7604)

TIEF = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')


def a(n):
    if isinstance(n, int): return 'a' + str(n).translate(TIEF)
    return 'a' + n.replace('n', 'ₙ').translate(TIEF)


def S(n):
    if isinstance(n, int): return 'S' + str(n).translate(TIEF)
    return 'Sₙ'


def summe(u, o, term):
    """Summenzeichen: ∑ₖ₌₁⁵ (2k + 1)."""
    t = f'({term})' if (' + ' in term or ' − ' in term or term.startswith('−')) else term
    return f'∑ₖ₌{str(u).translate(TIEF)}{str(o).translate(HOCHZ)} {t}'


def folge_txt(xs):
    return '; '.join(dz(x) for x in xs) + '; …'


ETAPPEN = [
    {'lernziel': 'summenzeichen', 'titel': 'Das Summenzeichen ∑',
     'regel': 'Eine ⟦Reihe⟧ (series) ist die ⟦Summe⟧ von Folgengliedern. Kurz schreibt man sie mit dem ⟦Summenzeichen ∑⟧ (sigma notation): ∑ₖ₌₁⁵ (2k + 1) heißt: Setze k = 1, 2, 3, 4, 5 ein und ⟦addiere alle Ergebnisse⟧.',
     'schritte': ['∑ₖ₌₁⁴ (3k − 1): k = 1, 2, 3, 4 einsetzen.', 'Glieder: 2; 5; 8; 11.', 'Summe: 2 + 5 + 8 + 11 = ⟦26⟧.'],
     'probe': 'Vier Summanden für k = 1 bis 4 ✓',
     'fehler': '∑ₖ₌₁⁴ (3k − 1) = 3 · 4 − 1 = 11 ist falsch: Das ist nur das ⟦letzte Glied⟧. Das Summenzeichen verlangt, ⟦alle Glieder zu addieren⟧.'},
    {'lernziel': 'arith', 'titel': 'Arithmetische Reihen',
     'regel': 'Für eine arithmetische Folge gilt: ⟦Sₙ = n · (a₁ + aₙ) : 2⟧. Idee (wie beim jungen Gauß): Erstes und letztes Glied, zweites und vorletztes, … ergeben ⟦immer dieselbe Summe⟧.',
     'schritte': ['1 + 2 + 3 + … + 100: n = 100, a₁ = 1, a₁₀₀ = 100.', 'S₁₀₀ = 100 · (1 + 100) : 2 = ⟦5 050⟧.'],
     'probe': '50 Paare mit je 101: 50 · 101 = 5 050 ✓',
     'fehler': 'S₁₀₀ = 100 · (1 + 100) = 10 100 ist falsch: Jedes Paar wurde so ⟦doppelt⟧ gezählt. Man muss durch ⟦2⟧ teilen.'},
    {'lernziel': 'geom', 'titel': 'Geometrische Reihen',
     'regel': 'Für eine geometrische Folge mit q ≠ 1 gilt: ⟦Sₙ = a₁ · (qⁿ − 1) : (q − 1)⟧. Die Summe wächst bei q > 1 sehr schnell.',
     'schritte': ['3 + 6 + 12 + 24 + 48: a₁ = 3, q = 2, n = 5.', 'S₅ = 3 · (2⁵ − 1) : (2 − 1) = 3 · 31 = ⟦93⟧.'],
     'probe': '3 + 6 + 12 + 24 + 48 = 93 ✓',
     'fehler': 'S₅ = 3 · (2⁴ − 1) : 1 = 45 ist falsch: In der Summenformel steht ⟦qⁿ⟧ mit n = 5 (Anzahl der Glieder), nicht qⁿ⁻¹ wie in der Formel für das letzte Glied.'},
    {'lernziel': 'sach', 'titel': 'Reihen in Sachaufgaben',
     'regel': 'Erst klären: ⟦Kommt immer gleich viel dazu⟧ (arithmetisch) oder ⟦wird immer mit demselben Faktor multipliziert⟧ (geometrisch)? Dann a₁, d bzw. q und die ⟦Anzahl n⟧ der Glieder bestimmen und die passende Summenformel nutzen.',
     'schritte': ['Training: Woche 1 läuft Mia 5 km, jede Woche 2 km mehr. Gesamtstrecke in 8 Wochen?', 'Arithmetisch: a₁ = 5, d = 2, a₈ = 5 + 7 · 2 = 19.', 'S₈ = 8 · (5 + 19) : 2 = ⟦96 km⟧.'],
     'probe': '5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = 96 ✓',
     'fehler': 'Die Strecke der ⟦8. Woche⟧ (19 km) als Gesamtstrecke anzugeben ist falsch: Gefragt ist die ⟦Summe⟧ aller Wochen.'},
    {'lernziel': 'verstehen', 'titel': 'Fehler bei Reihen finden',
     'regel': 'Typische Fehler: ⟦aₙ und Sₙ verwechseln⟧, die ⟦Anzahl der Glieder⟧ falsch zählen (von k = 3 bis 10 sind es 8 Glieder), ⟦qⁿ und qⁿ⁻¹⟧ verwechseln. Prüfe immer mit den ersten Gliedern.',
     'schritte': ['∑ₖ₌₃¹⁰ k: Wie viele Summanden?', 'k = 3, 4, …, 10: 10 − 3 + 1 = ⟦8 Summanden⟧.'],
     'probe': '3, 4, 5, 6, 7, 8, 9, 10 – acht Zahlen ✓',
     'fehler': '10 − 3 = 7 Summanden ist falsch: Beim Zählen von 3 bis 10 muss man ⟦beide Enden mitzählen⟧: 10 − 3 + 1 = 8.'},
]


def g_summenzeichen(s):
    art = R.choice({1: ['rechnen', 'rechnen', 'ausschreiben'], 2: ['rechnen', 'anzahl', 'quadrat'], 3: ['schreiben', 'rechnen_ab', 'konstant']}[s])
    m, t = R.choice([1, 2, 3, 4, 5, -2]), R.randint(-5, 6)
    if art == 'rechnen':
        o = R.randint(3, 5) if s == 1 else R.randint(5, 8)
        gl = [m * k + t for k in range(1, o + 1)]
        return zahl(f'Berechne {summe(1, o, poly(m, t, v="k"))}.', f'Glieder: {"; ".join(dz(g) for g in gl)}. Summe: {dz(sum(gl))}.',
                    'Setze k = 1, 2, 3, … bis zur oberen Zahl ein und addiere.', sum(gl), ' + '.join(f'({m} * {k} + ({t}))' for k in range(1, o + 1)))
    if art == 'ausschreiben':
        o = 4
        gl = [m * k + t for k in range(1, o + 1)]
        return luecken(f'Schreibe die Glieder von {summe(1, o, poly(m, t, v="k"))} auf.', '□ + □ + □ + □', 'vier ganze Zahlen', gl,
                       f'k = 1: {dz(gl[0])}; k = 2: {dz(gl[1])}; k = 3: {dz(gl[2])}; k = 4: {dz(gl[3])}.', 'Setze k = 1, 2, 3, 4 nacheinander ein.',
                       c=[f'{m} * {k} + ({t})' for k in range(1, o + 1)])
    if art == 'anzahl':
        u = R.randint(2, 10)
        o = u + R.randint(5, 30)
        return zahl(f'Wie viele Summanden hat {summe(u, o, poly(m, t, v="k"))}?', f'k läuft von {u} bis {o}: {o} − {u} + 1 = {o - u + 1} Summanden.',
                    'Beide Grenzen zählen mit.', o - u + 1, f'{o} - {u} + 1')
    if art == 'quadrat':
        o = R.randint(3, 6)
        gl = [k * k for k in range(1, o + 1)]
        return zahl(f'Berechne {summe(1, o, "k²")}.', f'{" + ".join(map(str, gl))} = {sum(gl)}.', 'Quadriere k = 1, 2, … und addiere.', sum(gl),
                    ' + '.join(f'{k} ** 2' for k in range(1, o + 1)))
    if art == 'rechnen_ab':
        u = R.randint(2, 4)
        o = u + R.randint(2, 4)
        gl = [m * k + t for k in range(u, o + 1)]
        return zahl(f'Berechne {summe(u, o, poly(m, t, v="k"))}.', f'k = {u} bis {o}: {"; ".join(dz(g) for g in gl)}. Summe: {dz(sum(gl))}.',
                    f'Beginne mit k = {u}, nicht mit 1.', sum(gl), ' + '.join(f'({m} * {k} + ({t}))' for k in range(u, o + 1)))
    if art == 'konstant':
        c, o = R.randint(2, 9), R.randint(5, 20)
        return zahl(f'Berechne {summe(1, o, str(c))}.', f'Der Term hängt nicht von k ab: {o} Summanden, jeder {c}. Summe: {o} · {c} = {o * c}.',
                    'Was wird für jedes k addiert?', o * c, f'{o} * {c}')
    d = R.choice([2, 3, 4, 5])
    st = R.randint(1, 6)
    o = R.randint(4, 7)
    gl = [st + d * (k - 1) for k in range(1, o + 1)]
    r = summe(1, o, poly(d, st - d, v='k'))
    return auswahl(f'Welche Schreibweise passt zu {" + ".join(map(str, gl))}?', r,
                   [summe(1, o, poly(d, st, v='k')), summe(1, o - 1, poly(d, st - d, v='k')), summe(0, o, poly(d, st - d, v='k'))],
                   f'Die Glieder wachsen um {d}: Term {poly(d, st - d, v="k")} (k = 1 ergibt {st}). {o} Glieder: k von 1 bis {o}.',
                   'Prüfe den Term mit k = 1 und zähle die Glieder.')


def g_arith(s):
    art = R.choice({1: ['gauss', 'formel'], 2: ['ohne_an', 'folge', 'folge_lang'], 3: ['folge_lang', 'bereich', 'gerade']}[s])  # Durchsicht 19
    if art == 'gauss':
        n = R.choice([10, 20, 30, 40, 50, 60, 80, 100, 200])
        return zahl(f'Berechne 1 + 2 + 3 + … + {n}.', f'Sₙ = {n} · (1 + {n}) : 2 = {dz(n * (n + 1) // 2)}.', 'Paare bilden: erstes + letztes, zweites + vorletztes …',
                    n * (n + 1) // 2, f'{n} * (1 + {n}) / 2')
    a1, d = R.randint(-5, 15), R.choice([2, 3, 4, 5, -2, -3])
    n = R.randint(8, 25)
    an = a1 + (n - 1) * d
    Sn = Fr(n * (a1 + an), 2)
    if art == 'formel':
        return zahl(f'Arithmetische Reihe mit n = {n}, {a(1)} = {dz(a1)} und {a(n)} = {dz(an)}. Berechne {S(n)}.', f'{S(n)} = {n} · ({dz(a1)} {plus(an)}) : 2 = {dz(Sn)}.',
                    'Sₙ = n · (a₁ + aₙ) : 2.', Sn, f'{n} * ({a1} + ({an})) / 2')
    if art == 'ohne_an':
        return zahl(f'Arithmetische Folge mit {a(1)} = {dz(a1)} und d = {dz(d)}. Berechne die Summe der ersten {n} Glieder.',
                    f'{a(n)} = {dz(a1)} + {n - 1} · {kl(d)} = {dz(an)}. {S(n)} = {n} · ({dz(a1)} {plus(an)}) : 2 = {dz(Sn)}.',
                    'Berechne zuerst das letzte Glied aₙ.', Sn, f'{n} * ({a1} + {a1} + ({n} - 1) * ({d})) / 2')
    if art in ('folge', 'folge_lang'):
        if art == 'folge_lang': n = R.randint(20, 50); an = a1 + (n - 1) * d; Sn = Fr(n * (a1 + an), 2)
        return zahl(f'Berechne die Summe der ersten {n} Glieder der Folge {folge_txt([a1 + d * i for i in range(4)])}',
                    f'd = {dz(d)}, {a(n)} = {dz(a1)} + {n - 1} · {kl(d)} = {dz(an)}. {S(n)} = {n} · ({dz(a1)} {plus(an)}) : 2 = {dz(Sn)}.',
                    'Bestimme d, dann aₙ, dann Sₙ.', Sn, f'{n} * ({a1} + {a1} + ({n} - 1) * ({d})) / 2')
    if art == 'bereich':
        u = R.randint(10, 40)
        o = u + R.randint(10, 40)
        n = o - u + 1
        return zahl(f'Berechne {u} + {u + 1} + {u + 2} + … + {o}.', f'n = {o} − {u} + 1 = {n} Glieder. S = {n} · ({u} + {o}) : 2 = {dz(Fr(n * (u + o), 2))}.',
                    'Zähle zuerst die Glieder (beide Enden mitzählen).', Fr(n * (u + o), 2), f'({o} - {u} + 1) * ({u} + {o}) / 2')
    k = R.choice([2, 3, 5])
    o = k * R.randint(10, 40)
    n = o // k
    return zahl(f'Berechne die Summe aller Vielfachen von {k} von {k} bis {o}.', f'{k} + {2 * k} + … + {o}: n = {n} Glieder, S = {n} · ({k} + {o}) : 2 = {dz(Fr(n * (k + o), 2))}.',
                'Arithmetische Reihe mit d = ' + str(k) + '. Wie viele Vielfache sind es?', Fr(n * (k + o), 2), f'{n} * ({k} + {o}) / 2')


def g_geom(s):
    a1, q = R.randint(1, 6), R.choice([2, 3])
    n = R.randint(4, 6) if s == 1 else R.randint(5, 9)
    Sn = a1 * (q ** n - 1) // (q - 1)
    art = R.choice({1: ['formel', 'klein'], 2: ['folge', 'q_neg', 'folge'], 3: ['folge', 'halb', 'n_aus_S', 'q_neg']}[s])  # Durchsicht 19
    if art == 'klein':
        gl = [a1 * q ** i for i in range(n)]
        return zahl(f'Berechne {" + ".join(map(str, gl))}.', f'a₁ = {a1}, q = {q}, n = {n}: S = {a1} · ({q}^{n} − 1) : ({q} − 1) = {dz(Sn)}. (Probe: Glieder addieren.)',
                    'Direkt addieren oder die Summenformel nutzen.', Sn, ' + '.join(map(str, gl)))
    if art == 'formel':
        return zahl(f'Geometrische Reihe mit {a(1)} = {a1}, q = {q}. Berechne {S(n)}.', f'{S(n)} = {a1} · ({q}^{n} − 1) : ({q} − 1) = {a1} · {q ** n - 1} : {q - 1} = {dz(Sn)}.',
                    'Sₙ = a₁ · (qⁿ − 1) : (q − 1).', Sn, f'{a1} * ({q} ** {n} - 1) / ({q} - 1)')
    if art == 'folge':
        return zahl(f'Berechne die Summe der ersten {n} Glieder der Folge {folge_txt([a1 * q ** i for i in range(4)])}',
                    f'q = {q}. {S(n)} = {a1} · ({q}^{n} − 1) : ({q} − 1) = {dz(Sn)}.', 'Bestimme q und setze in die Summenformel ein.', Sn, f'{a1} * ({q} ** {n} - 1) / ({q} - 1)')
    if art == 'q_neg':
        q = -2
        n = R.randint(4, 7)
        Sn = Fr(a1 * (q ** n - 1), q - 1)
        return zahl(f'Geometrische Reihe mit {a(1)} = {a1} und q = −2. Berechne {S(n)}.', f'{S(n)} = {a1} · ((−2)^{n} − 1) : (−2 − 1) = {a1} · ({dz(q ** n - 1)}) : (−3) = {dz(Sn)}.',
                    'Achte auf die Klammern bei der negativen Basis.', Sn, f'{a1} * ((-2) ** {n} - 1) / (-2 - 1)')
    if art == 'halb':
        a1 = R.choice([64, 128, 256, 512])
        n = R.randint(4, 7)
        Sn = Fr(a1) * (1 - Fr(1, 2) ** n) / Fr(1, 2)
        return zahl(f'Berechne die Summe der ersten {n} Glieder der Folge {folge_txt([Fr(a1, 2 ** i) for i in range(4)])}',
                    f'q = 0,5. {S(n)} = {a1} · (0,5^{n} − 1) : (0,5 − 1) = {dz(Sn)}.', 'Die Formel gilt auch für q < 1 – achte auf die Vorzeichen.', Sn,
                    f'{a1} * (0.5 ** {n} - 1) / (0.5 - 1)')
    n = R.randint(4, 8)
    Sn = a1 * (q ** n - 1) // (q - 1)
    return zahl(f'Geometrische Reihe mit {a(1)} = {a1} und q = {q}. Wie viele Glieder muss man addieren, damit die Summe {dz(Sn)} ist?',
                f'{a1} · ({q}ⁿ − 1) : {q - 1} = {dz(Sn)} ⇒ {q}ⁿ − 1 = {dz(Sn * (q - 1) // a1)} ⇒ {q}ⁿ = {dz(q ** n)} ⇒ n = {n}.',
                'Stelle nach qⁿ um und probiere Potenzen.', n, f'{n}')


def g_sach(s):
    art = R.choice({1: ['training', 'sitze'], 2: ['training', 'sitze', 'sparen', 'stapel'], 3: ['kette', 'schach', 'turnier', 'sparen_rueck']}[s])
    if art == 'training':
        a1, d, n = R.choice([2, 3, 4, 5]), R.choice([1, 2]), R.randint(6, 12)
        an = a1 + (n - 1) * d
        return zahl(f'Ein Läufer läuft in der ersten Woche {a1} km und steigert seine Strecke jede Woche um {d} km. Wie viele km läuft er in {n} Wochen insgesamt?',
                    f'Arithmetisch: {a(n)} = {a1} + {n - 1} · {d} = {an}. S = {n} · ({a1} + {an}) : 2 = {dz(Fr(n * (a1 + an), 2))} km.',
                    'Kommt jede Woche gleich viel dazu? Dann arithmetische Reihe.', Fr(n * (a1 + an), 2), f'{n} * ({a1} + {an}) / 2', einheit='km')
    if art == 'sitze':
        a1, d, n = R.randint(14, 24), R.choice([2, 3, 4]), R.randint(10, 25)
        an = a1 + (n - 1) * d
        return zahl(f'Ein Stadion-Block hat {n} Reihen. Reihe 1 hat {a1} Plätze, jede Reihe {d} Plätze mehr als die vorige. Wie viele Plätze hat der Block?',
                    f'{a(n)} = {a1} + {n - 1} · {d} = {an}. S = {n} · ({a1} + {an}) : 2 = {dz(Fr(n * (a1 + an), 2))}.',
                    'Gesucht ist die Summe aller Reihen.', Fr(n * (a1 + an), 2), f'{n} * ({a1} + {an}) / 2')
    if art == 'sparen':
        a1, d, n = R.choice([5, 10, 20]), R.choice([2, 5]), 12
        an = a1 + (n - 1) * d
        return zahl(f'Lea spart im ersten Monat {a1} € und legt jeden Monat {d} € mehr zurück als im Vormonat. Wie viel hat sie nach einem Jahr gespart?',
                    f'{a(12)} = {a1} + 11 · {d} = {an}. S₁₂ = 12 · ({a1} + {an}) : 2 = {dz(6 * (a1 + an))} €.', '12 Monate = 12 Glieder.', 6 * (a1 + an),
                    f'12 * ({a1} + {an}) / 2', einheit='€')
    if art == 'stapel':
        un = R.randint(10, 20)
        return zahl(f'Baumstämme werden gestapelt: unten {un}, darüber jeweils einer weniger, ganz oben 1. Wie viele Stämme sind es?',
                    f'1 + 2 + … + {un} = {un} · ({un} + 1) : 2 = {un * (un + 1) // 2}.', 'Von oben gelesen: 1, 2, 3, …', un * (un + 1) // 2, f'{un} * ({un} + 1) / 2')
    if art == 'kette':
        tage = R.randint(5, 8)
        return zahl(f'Eine Nachricht wird am 1. Tag an 3 Personen geschickt. Jede Person schickt sie am nächsten Tag an 3 neue Personen weiter. Wie viele Personen haben sie nach {tage} Tagen insgesamt erhalten?',
                    f'Geometrisch: 3; 9; 27; … mit q = 3. S = 3 · (3^{tage} − 1) : 2 = {dz(3 * (3 ** tage - 1) // 2)}.', 'Pro Tag verdreifacht sich die Zahl der neuen Empfänger.',
                    3 * (3 ** tage - 1) // 2, f'3 * (3 ** {tage} - 1) / 2')
    if art == 'schach':
        f = R.randint(6, 10)
        return zahl(f'Auf das 1. Feld eines Schachbretts legt man 1 Reiskorn, auf jedes weitere doppelt so viele wie auf das vorige. Wie viele Körner liegen auf den ersten {f} Feldern zusammen?',
                    f'1 + 2 + 4 + … : a₁ = 1, q = 2, n = {f}. S = (2^{f} − 1) : 1 = {dz(2 ** f - 1)}.', 'Geometrische Reihe mit q = 2.', 2 ** f - 1, f'2 ** {f} - 1')
    if art == 'turnier':
        t = R.randint(6, 16)
        return zahl(f'Bei einem Turnier spielt jede der {t} Mannschaften genau einmal gegen jede andere. Wie viele Spiele gibt es? (Mannschaft 1 spielt {t - 1}-mal, Mannschaft 2 noch {t - 2}-mal gegen neue Gegner …)',
                    f'{t - 1} + {t - 2} + … + 1 = {t - 1} · {t} : 2 = {(t - 1) * t // 2}.', 'Arithmetische Reihe von 1 bis t − 1.', (t - 1) * t // 2, f'({t} - 1) * {t} / 2')
    a1, d = R.choice([10, 20]), R.choice([5, 10])
    n = R.randint(5, 12)
    an = a1 + (n - 1) * d
    Sn = n * (a1 + an) // 2
    return zahl(f'Jemand spart im 1. Monat {a1} € und dann jeden Monat {d} € mehr. Nach wie vielen Monaten hat er insgesamt {dz(Sn)} € gespart?',
                f'Probieren mit Sₙ = n · ({a1} + {a1} + (n − 1) · {d}) : 2: Für n = {n} ergibt sich {dz(Sn)} €.', 'Setze Werte für n ein oder stelle eine Gleichung auf.', n, f'{n}')


def g_verstehen(s):
    art = R.choice({1: ['an_sn', 'anzahl'], 2: ['anzahl', 'an_sn', 'halb'], 3: ['qn', 'halb', 'teil', 'an_sn']}[s])
    if art == 'an_sn':
        a1, d, n = R.randint(1, 9), R.randint(2, 6), R.randint(8, 20)
        an = a1 + (n - 1) * d
        Sn = Fr(n * (a1 + an), 2)
        r = f'Falsch: {dz(an)} ist nur {a(n)}, die Summe ist {S(n)} = {dz(Sn)}.'
        return auswahl(f'Arithmetische Folge mit {a(1)} = {a1}, d = {d}. Gefragt: Summe der ersten {n} Glieder. Ben antwortet: {a1} + {n - 1} · {d} = {an}. Stimmt das?', r,
                       ['Richtig.', f'Falsch: richtig ist {a1} + {n} · {d} = {a1 + n * d}.', f'Falsch: richtig ist {n} · {an} = {dz(n * an)}.'],
                       f'Ben hat das letzte Glied berechnet. Die Summe: {n} · ({a1} + {an}) : 2 = {dz(Sn)}.', 'Ist nach einem Glied oder nach der Summe gefragt?')
    if art == 'anzahl':
        u = R.randint(2, 9)
        o = u + R.randint(5, 20)
        r = f'{o - u + 1}'
        return auswahl(f'Wie viele Summanden hat {summe(u, o, "k")}?', r, [f'{o - u}', f'{o}', f'{o - u + 2}'],
                       f'{o} − {u} + 1 = {o - u + 1}: Beide Grenzen gehören dazu.', 'Teste mit kleinen Zahlen: Von 3 bis 5 sind es 3, 4, 5.')
    if art == 'halb':
        n = R.choice([20, 30, 40, 50, 100])
        r = f'Falsch: Es fehlt das Teilen durch 2; richtig ist {dz(n * (n + 1) // 2)}.'
        return auswahl(f'Eva rechnet 1 + 2 + … + {n} = {n} · ({n} + 1) = {dz(n * (n + 1))}. Stimmt das?', r,
                       ['Richtig.', f'Falsch: richtig ist {n} · {n} = {dz(n * n)}.', f'Falsch: richtig ist ({n} + 1) : 2 = {dz(Fr(n + 1, 2))}.'],
                       f'n · (a₁ + aₙ) zählt jedes Paar doppelt. {n} · {n + 1} : 2 = {dz(n * (n + 1) // 2)}.', 'Probiere mit 1 + 2 + 3: Was liefert Evas Formel?')
    if art == 'qn':
        a1, q, n = R.randint(1, 4), 2, R.randint(5, 8)
        richtig = a1 * (2 ** n - 1)
        r = f'Falsch: Es muss 2^{n} heißen, also {dz(richtig)}.'
        return auswahl(f'Geometrische Reihe mit {a(1)} = {a1}, q = 2, n = {n}. Tom rechnet {S(n)} = {a1} · (2^{n - 1} − 1) : 1 = {dz(a1 * (2 ** (n - 1) - 1))}. Stimmt das?', r,
                       ['Richtig.', f'Falsch: Es muss {a1} · 2^{n - 1} = {dz(a1 * 2 ** (n - 1))} heißen.', f'Falsch: Man muss durch 2 teilen: {dz(Fr(a1 * (2 ** (n - 1) - 1), 2))}.'],
                       f'In der Summenformel steht qⁿ. Probe mit n = 1: S₁ = {a1} · (2¹ − 1) = {a1} ✓.', 'Teste die Formel mit n = 1: Muss a₁ herauskommen?')
    a1, d, n = R.randint(1, 5), R.randint(2, 5), R.randint(5, 10)
    gl = [a1 + d * i for i in range(n + 3)]
    S_n, S_m = sum(gl[:n]), sum(gl[:n + 3])
    return zahl(f'Für eine Folge ist {S(n)} = {S_n} und {S(n + 3)} = {S_m}. Wie groß ist {a(n + 1)} + {a(n + 2)} + {a(n + 3)}?',
                f'{S(n + 3)} − {S(n)} = {S_m} − {S_n} = {S_m - S_n}: genau die drei Glieder danach.', 'Was bleibt übrig, wenn man von der längeren Summe die kürzere abzieht?',
                S_m - S_n, f'{S_m} - {S_n}')


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-2) ----------
# Prüfungsvorbilder: IB MYP Extended / MYP-Fragenbanken (Summenschreibweise, Summe aller Zahlen von u bis o, Anzahl der Glieder
# für eine gegebene Summe, Turnier im K.-o.-System, aₙ = Sₙ − Sₙ₋₁). Eigene Zahlen und Einkleidungen.
def summenzeichen3(art):
    # aufteilen: Summe in Teile zerlegen
    n = R.choice([6, 8, 10, 12, 20])
    m, c = R.choice([2, 3, 4, 5]), R.randint(1, 9)
    sk = n * (n + 1) // 2
    return zahl(f'Es gilt {summe(1, n, "k")} = {sk}. Berechne damit {summe(1, n, f"{m}k + {c}")}.',
                f'{summe(1, n, f"{m}k + {c}")} = {m} · ({summe(1, n, "k")}) + {n} · {c} = {m} · {sk} + {n * c} = {m * sk + n * c}.',
                f'Jeder Summand ist {m} · k plus {c}. Der Teil „plus {c}“ kommt {n}-mal vor.', m * sk + n * c, f'{m} * {sk} + {n} * {c}')


def arith3(art):
    if art == 'n_gesucht':
        a1, d = R.randint(1, 9), R.choice([2, 3, 4])
        n = R.randint(6, 14)
        Sn = n * (2 * a1 + (n - 1) * d) // 2
        xs = [a1 + d * i for i in range(3)]
        return zahl(f'Wie viele Glieder der Folge {folge_txt(xs)} muss man addieren, damit die Summe {dz(Sn)} ergibt?',
                    f'{S("n")} = n · ({a1} + {a1} + (n − 1) · {d}) : 2. Probieren: Für n = {n} ist {a(n)} = {a1 + (n - 1) * d} und {S(n)} = {n} · ({a1} + {a1 + (n - 1) * d}) : 2 = {dz(Sn)}.',
                    'Rechne Summen für einige n aus (oder stelle Sₙ als Term in n auf) und nähere dich an.', n, f'{n}')
    # vielfache: Summe aller Vielfachen von k in einem Bereich
    k = R.choice([3, 4, 6, 7, 8, 9])
    u, o = R.choice([(10, 99), (1, 100), (20, 80), (50, 150)])
    erst, letzt = -(-u // k) * k, o // k * k
    anz = (letzt - erst) // k + 1
    Sn = anz * (erst + letzt) // 2
    return zahl(f'Berechne die Summe aller Vielfachen von {k} zwischen {u} und {o}.',
                f'Erstes Vielfaches: {erst}, letztes: {letzt}. Anzahl: ({letzt} − {erst}) : {k} + 1 = {anz}. Summe: {anz} · ({erst} + {letzt}) : 2 = {dz(Sn)}.',
                'Bestimme das erste und das letzte Vielfache im Bereich und zähle, wie viele es sind.', Sn, f'{anz} * ({erst} + {letzt}) / 2')


def geom3(art):
    if art == 'turnier':
        n = R.choice([4, 5, 6, 7])
        t = 2 ** n
        return zahl(f'Bei einem Turnier mit {t} Spielern scheidet in jedem Spiel der Verlierer aus (K.-o.-System). In Runde 1 gibt es {t // 2} Spiele, in jeder Runde halb so viele wie in der vorigen, bis zum Finale. Wie viele Spiele gibt es insgesamt?',
                    f'{" + ".join(str(t // 2 ** i) for i in range(1, n + 1))}: geometrische Reihe mit a₁ = {t // 2}, q = 1/2, n = {n}. Summe {t - 1}. (Probe: Jeder außer dem Sieger verliert genau einmal: {t} − 1.)',
                    'Schreibe die Spiele je Runde auf, bis nur noch ein Spiel übrig ist.', t - 1, f'{t} - 1')
    # a1_gesucht
    a1, q, n = R.randint(2, 9), R.choice([2, 3]), R.randint(4, 6)
    Sn = a1 * (q ** n - 1) // (q - 1)
    return zahl(f'Eine geometrische Reihe hat q = {q} und {S(n)} = {dz(Sn)}. Wie groß ist {a(1)}?',
                f'{S(n)} = {a(1)} · ({q}^{n} − 1) : {q - 1} = {a(1)} · {dz((q ** n - 1) // (q - 1))}. Also {a(1)} = {dz(Sn)} : {dz((q ** n - 1) // (q - 1))} = {a1}.',
                'Setze in die Summenformel ein. Alles außer a₁ ist bekannt.', a1, f'{Sn} / (({q} ** {n} - 1) / ({q} - 1))')


def sach3(art):
    # verdopplung: linear gegen exponentiell
    a1 = R.choice([5, 10, 20])
    for n in range(1, 60):
        A = a1 * n * (n + 1) // 2
        B = (2 ** n - 1)
        if B > A * 100: break
    return zahl(f'Angebot A: am 1. Tag {a1} €, jeden Tag {a1} € mehr. Angebot B: am 1. Tag 1 Cent, jeden Tag doppelt so viel wie am Vortag. '
                'Nach wie vielen Tagen hat man mit B insgesamt mehr Geld als mit A?',
                f'A nach n Tagen: {a1} · n · (n + 1) : 2 €. B nach n Tagen: (2ⁿ − 1) Cent. Für n = {n - 1}: A = {dz(a1 * (n - 1) * n // 2)} €, B = {dz(Fr(2 ** (n - 1) - 1, 100))} €. '
                f'Für n = {n}: A = {dz(a1 * n * (n + 1) // 2)} €, B = {dz(Fr(2 ** n - 1, 100))} €. Also ab Tag {n}.',
                'Rechne beide Summen für einige Tage aus. Achtung: B ist in Cent.', n, f'{n}')


def verstehen3(art):
    # an aus Sn
    p, q = R.randint(1, 3), R.randint(-3, 5)
    n = R.randint(4, 10)
    Sf = lambda k: p * k * k + q * k  # noqa: E731
    return zahl(f'Für eine Folge gilt für jedes n: {S("n")} = {poly(p, q, 0, v="n")}. Wie groß ist {a(n)}?',
                f'{a(n)} = {S(n)} − {S(n - 1)} = {dz(Sf(n))} − {dz(Sf(n - 1))} = {dz(Sf(n) - Sf(n - 1))}.',
                f'{S(n)} enthält alle Glieder bis {a(n)}, {S(n - 1)} alle bis {a(n - 1)}.', Sf(n) - Sf(n - 1), f'{Sf(n)} - ({Sf(n - 1)})')


def _filter(g, s, teil, nicht=False):
    for _ in range(80):
        t = g(s)
        if t and ((teil in t['f']['text']) != nicht): return t
    return None


def g2_summenzeichen(s):
    if s < 3: return g_summenzeichen(s)
    art = art3('schreiben', 'aufteilen', 'konstant', ['schreiben', 'rechnen_ab', 'aufteilen', 'konstant', 'rechnen_ab'])
    if art == 'aufteilen': return summenzeichen3(art)
    for _ in range(80):
        t = g_summenzeichen(3)
        if not t: continue
        x = t['f']['text']
        if {'schreiben': 'Schreibweise' in x, 'konstant': x.startswith('Berechne') and '(' not in x.split('.')[0], 'rechnen_ab': 'ₖ₌₁' not in x and 'Schreibweise' not in x}[art]: return t
    return None


def g2_arith(s):
    if s < 3: return g_arith(s)
    art = art3('bereich', 'n_gesucht', 'vielfache', ['bereich', 'n_gesucht', 'vielfache', 'bereich', 'n_gesucht'])
    if art == 'bereich': return _filter(g_arith, 3, ' + … + ')
    return arith3(art)


def g2_geom(s):
    if s < 3: return g_geom(s)
    art = art3('n_aus_S', 'turnier', 'a1_gesucht', ['n_aus_S', 'halb', 'a1_gesucht', 'turnier', 'halb'])
    if art == 'n_aus_S': return _filter(g_geom, 3, 'Wie viele Glieder')
    if art == 'halb':
        for _ in range(80):
            t = g_geom(3)
            if t and ('128' in t['f']['text'] or '64' in t['f']['text'] or '32' in t['f']['text']) and 'Wie viele' not in t['f']['text'] and 'q = −' not in t['f']['text']: return t
        return None
    return geom3(art)


def g2_sach(s):
    if s == 1: return g_sach(1)
    if s == 2:  # Stufe 2: andere Einkleidung (Sparen über ein Jahr, Stapel bis 1) und geometrische Sachaufgabe (vorher Stufe 3)
        return R.choice([lambda: _filter(g_sach, 2, 'Lea'), lambda: _filter(g_sach, 2, 'Baumstämme'), lambda: _filter(g_sach, 3, 'Schachbrett')])()
    art = art3('sparen_rueck', 'kette', 'verdopplung', ['sparen_rueck', 'kette', 'verdopplung', 'turnier', 'sparen_rueck'])
    if art == 'sparen_rueck': return _filter(g_sach, 3, 'Nach wie vielen Monaten')
    if art == 'kette': return _filter(g_sach, 3, 'Nachricht')
    if art == 'turnier': return _filter(g_sach, 3, 'Turnier')
    return sach3(art)


def g2_verstehen(s):
    if s < 3: return g_verstehen(s)
    art = art3('qn', 'teil', 'an_sn_neu', ['qn', 'teil', 'an_sn_neu', 'teil', 'qn'])
    if art == 'an_sn_neu': return verstehen3(art)
    teil = {'qn': 'Tom', 'teil': 'S₆', 'halb_eva': 'Eva'}[art]
    for _ in range(120):
        t = g_verstehen(3)
        if t and (teil in t['f']['text'] or (art == 'teil' and 'Wie groß ist a' in t['f']['text'])): return t
    return None


GEN = schoen({'summenzeichen': g2_summenzeichen, 'arith': g2_arith, 'geom': g2_geom, 'sach': g2_sach, 'verstehen': g2_verstehen})

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import tab  # noqa: E402


def _s(werte, namen, einheit=''):
    return {'typ': 'saeulen', 'einheit': einheit, 'werte': [{'name': n, 'wert': w} for n, w in zip(namen, werte)], 'zahlen': True}


_KK = ['k', '1', '2', '3', '4']
_W = [5, 7, 9, 11, 13, 15, 17, 19]
UMBAU = {
    'summenzeichen': {
        'einstieg': 'Ein Muster hat in Bild 1 bis 4 nacheinander 2, 5, 8 und 11 Plättchen. Wie viele sind es zusammen? '
                    'Die Summe von Folgengliedern heißt ⟦Reihe⟧.',
        'woerter': [['Reihe', 'die Summe von Folgengliedern'],
                    ['∑', 'Summenzeichen: für k alle Zahlen von unten bis oben einsetzen und addieren']],
        'bild': tab(_KK, ['3k − 1', '?', '?', '?', '?']),
        'schritte': [
            {'text': '∑ₖ₌₁⁴ (3k − 1): k = 1, 2, 3, 4 einsetzen.'},
            {'text': 'Die Glieder sind 2; 5; 8; 11.', 'bild': tab(_KK, ['3k − 1', '2', '5', '8', '11'])},
            {'text': 'Alles addieren: 2 + 5 + 8 + 11 = ⟦26⟧.', 'bild': _s([2, 5, 8, 11, 26], ['k = 1', 'k = 2', 'k = 3', 'k = 4', 'Summe'])},
        ],
        'fehler': '3 · 4 − 1 = 11 ist nur das ⟦letzte Glied⟧. Das Summenzeichen verlangt, alle Glieder zu addieren.',
        'regel': '∑: für k ⟦alle Zahlen von unten bis oben⟧ einsetzen. Dann die Ergebnisse addieren.',
    },
    'arith': {
        'einstieg': 'Ein Lehrer lässt 1 + 2 + … + 100 rechnen. Ein Kind bildet Paare: 1 + 100 und 2 + 99 ergeben ⟦101⟧. '
                    'Das ist der Trick der arithmetischen Reihe.',
        'woerter': [['Sₙ', 'die Summe der ersten n Glieder'],
                    ['Paar', 'erstes und letztes Glied, zweites und vorletztes …']],
        'bild': tab(['Paar', '1 + 100'], ['Summe', '101']),
        'schritte': [
            {'text': 'Erstes und letztes Glied: 1 + 100 = 101.'},
            {'text': 'Jedes Paar ergibt 101. 100 Zahlen bilden 50 Paare.',
             'bild': tab(['Paar', '1 + 100', '2 + 99', '3 + 98', '…', '50 + 51'], ['Summe', '101', '101', '101', '…', '101'])},
            {'text': 'S₁₀₀ = 50 · 101 = ⟦5 050⟧.'},
            {'text': 'Als Formel: Sₙ = n · (a₁ + aₙ) : 2.'},
        ],
        'fehler': '100 · 101 = 10 100 ist falsch. So ist jedes Paar ⟦doppelt⟧ gezählt, man muss durch 2 teilen.',
        'regel': 'Arithmetische Reihe: ⟦Sₙ = n · (a₁ + aₙ) : 2⟧. Erstes plus letztes Glied, mal Anzahl, halbieren.',
    },
    'geom': {
        'einstieg': 'Ein Kettenbrief: Erst bekommen ihn 3 Leute, jede Runde doppelt so viele. Wie viele Briefe sind es nach 5 Runden zusammen? '
                    'Das zählt die ⟦geometrische Reihe⟧.',
        'woerter': [['geometrische Reihe', 'die Summe der Glieder einer geometrischen Folge']],
        'bild': _s([3, 6, 12, 24, 48], ['R1', 'R2', 'R3', 'R4', 'R5'], 'Briefe'),
        'schritte': [
            {'text': 'Die Briefe pro Runde: 3; 6; 12; 24; 48.'},
            {'text': 'Also a₁ = 3, q = 2 und n = 5 Glieder.'},
            {'text': 'S₅ = 3 · (2⁵ − 1) : 1 = ⟦93⟧.', 'bild': _s([3, 6, 12, 24, 48, 93], ['R1', 'R2', 'R3', 'R4', 'R5', 'Summe'], 'Briefe')},
            {'text': 'Probe: 3 + 6 + 12 + 24 + 48 = 93.'},
        ],
        'fehler': '3 · (2⁴ − 1) = 45 ist falsch. In der Summenformel steht ⟦qⁿ⟧ mit n = 5, der Anzahl der Glieder.',
        'regel': 'Geometrische Reihe: Die Summenformel hat ⟦qⁿ⟧, nicht qⁿ⁻¹. Sie lautet Sₙ = a₁ · (qⁿ − 1) : (q − 1).',
    },
    'sach': {
        'einstieg': 'Ein Läufer läuft in Woche 1 genau 5 km, jede Woche 2 km mehr. Wie viele km sind es in 8 Wochen zusammen? '
                    'Gefragt ist die ⟦Summe⟧.',
        'woerter': [['Gesamtstrecke', 'alle Wochen zusammengezählt']],
        'bild': _s(_W[:3], ['W1', 'W2', 'W3'], 'km'),
        'schritte': [
            {'text': 'Immer 2 km mehr: arithmetisch mit a₁ = 5 und d = 2.'},
            {'text': 'Woche 8: a₈ = 5 + 7 · 2 = 19.', 'bild': _s(_W, [f'W{i}' for i in range(1, 9)], 'km')},
            {'text': 'Gesamtstrecke: S₈ = 8 · (5 + 19) : 2 = ⟦96 km⟧.'},
        ],
        'fehler': '19 km ist nur die ⟦8. Woche⟧. Gefragt ist die Summe aller Wochen: 96 km.',
        'regel': 'Erst klären: ⟦gleich viel dazu⟧ oder gleicher Faktor? Dann a₁, d oder q und n bestimmen und die Summenformel nutzen.',
    },
    'verstehen': {
        'einstieg': 'Von Meter 3 bis Meter 10 steht an jedem Meter ein Zaunpfosten. Viele rechnen 10 − 3 = 7 und liegen daneben. '
                    'Du musst ⟦beide Enden⟧ mitzählen.',
        'woerter': [['Summand', 'eine Zahl, die in einer Summe addiert wird']],
        'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 12, 'abschnitte': 12, 'beschriftet': 'alle'},
        'schritte': [
            {'text': '∑ₖ₌₃¹⁰ k: Wie viele Summanden hat die Summe?'},
            {'text': 'k = 3, 4, 5, 6, 7, 8, 9, 10.', 'bild': {'punkte': [{'wert': k, 'name': ''} for k in range(3, 11)]}},
            {'text': 'Zählen: 10 − 3 + 1 = ⟦8 Summanden⟧.'},
        ],
        'fehler': '10 − 3 = 7 ist falsch. Von 3 bis 10 zählen ⟦beide Enden mit⟧: 10 − 3 + 1 = 8.',
        'regel': 'Beim Zählen beide Enden mitnehmen. Von u bis o sind es ⟦o − u + 1⟧ Glieder.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


d = bauen('funktionen.reihen',
      'Reihen mit dem Summenzeichen schreiben und berechnen, Summenformeln für arithmetische und geometrische Reihen anwenden und Sachaufgaben lösen.',
      ['Reihe (series) = Summe von Folgengliedern; ∑ₖ₌₁ⁿ: k von 1 bis n einsetzen und addieren.',
       'Arithmetisch: Sₙ = n · (a₁ + aₙ) : 2.',
       'Geometrisch: Sₙ = a₁ · (qⁿ − 1) : (q − 1), q ≠ 1.',
       'Anzahl der Glieder von k = u bis k = o: o − u + 1.'],
      [('Schreibweise', ['summenzeichen']), ('Summenformeln', ['arith', 'geom']), ('Anwenden', ['sach', 'verstehen'])],
      ETAPPEN, GEN,
      offen=['Unendliche geometrische Reihen (Grenzwert a₁ : (1 − q)) sind nicht enthalten: Das ist IB MYP 5 Extended bzw. DP-Stoff. Annahme: MYP 4 endet bei endlichen Reihen.',
             'Summenzeichen mit Unicode-Indizes (∑ₖ₌₁⁵). Die Grenzen stehen dadurch neben, nicht unter/über dem ∑ – bei Bedarf App-Wunsch für eine Formeldarstellung.'], plan=PLAN2)
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)


# ---- STUFEN (Zwanzigste Runde, Zusatz Realschule/IB, Zweig stufen-rsib-2) ----
from _stufen_rsib2 import Stufen, stufen  # noqa: E402

ST = Stufen('funktionen.reihen', 20_2_6)
Z, A, L = ST.Z, ST.A, ST.L
ST.vorbild += ['IB MYP eAssessment Mathematics (Extended): arithmetische und geometrische Reihen in Sachsituationen (mehrteilige Aufgabe)',
               'Känguru der Mathematik / Mathematik-Olympiade: Summen- und Zählaufgaben (Gaußsche Summe, Teleskopsumme) als Vorbild für die Knobel-Bordkarten (nur Art)']

# summenzeichen
ST.stufenleiter('summenzeichen', 'Glieder einer ∑-Summe aufschreiben und addieren.',
                'Längere Summen, Anzahl der Summanden, k und k², Summe in einer Sachsituation.',
                'Summe als ∑ schreiben, mit bekannter Summe rechnen, konstante Summanden, Fehler beim Einsetzen, n zu einer Summe.')
ST.typ('summenzeichen', '/^Schreibe die Glieder/', 'erkennen')
ST.typ('summenzeichen', '/^/', 'direkt', s=1)
ST.typ('summenzeichen', '/Wie viele Summanden/', 'umkehr')
ST.typ('summenzeichen', '/^/', 'mehrschritt', s=2)
ST.typ('summenzeichen', '/Welche Schreibweise/', 'rueckwaerts')
ST.typ('summenzeichen', '/^Es gilt/', 'verknuepfen')
ST.typ('summenzeichen', '/^Berechne ∑ₖ₌₁[⁰¹²³⁴⁵⁶⁷⁸⁹]+ \\d+\\.$/', 'transfer')
ST.typ('summenzeichen', '/^/', 'mehrschritt', s=3)
ST.neu('summenzeichen', 'einkleidung', Z('Eine Treppe aus Würfeln hat 6 Stufen; Stufe k besteht aus k Würfeln. Wie viele Würfel braucht man (∑ₖ₌₁⁶ k)?', 21, '1+2+3+4+5+6',
       '1 + 2 + 3 + 4 + 5 + 6 = 21.', 'Setze k = 1 bis 6 ein.'))
ST.neu('summenzeichen', 'fehler', A('Jemand schreibt: ∑ₖ₌₁³ (k + 1) = 1 + 2 + 3 + 1 = 7. Was stimmt?', 'Falsch: Jeder Summand ist k + 1: 2 + 3 + 4 = 9.',
       ['Richtig.', 'Falsch: 1 + 1 + 1 = 3.', 'Falsch: (1 + 2 + 3) · 1 = 6.'], 'Für jedes k wird der ganze Term k + 1 gebildet: k = 1 → 2, k = 2 → 3, k = 3 → 4.', 'Setze k = 1, 2, 3 jeweils in (k + 1) ein.'))
ST.neu('summenzeichen', 'parameter', Z('Für welches n gilt ∑ₖ₌₁ⁿ 4 = 36?', 9, '36/4', 'Jeder Summand ist 4, es sind n Summanden: 4n = 36 ⇒ n = 9.', 'Wie viele Vieren werden addiert?'))
ST.knobel('summenzeichen', Z('Berechne ∑ₖ₌₁¹⁰ (k + 1)² − ∑ₖ₌₁¹⁰ k².', 120, '2*55 + 10',
          '(k + 1)² − k² = 2k + 1. Also ∑ (2k + 1) = 2 · 55 + 10 = 120 – ohne ein einziges Quadrat auszurechnen.', 'Fasse die beiden Summen gliedweise zusammen.'))
ST.knobel('summenzeichen', L('Berechne ∑ₖ₌₁⁹⁹ 1/(k · (k + 1)).', '□/□', [99, 100], ['99', '100'],
          '1/(k(k + 1)) = 1/k − 1/(k + 1). Die Summe wird (1 − 1/2) + (1/2 − 1/3) + … + (1/99 − 1/100); alles in der Mitte hebt sich weg: 1 − 1/100 = 99/100.',
          'Schreibe 1/(1 · 2) und 1/(2 · 3) als Differenz zweier Brüche.', hinweis='Zähler und Nenner eintragen.'))

# arith
ST.stufenleiter('arith', 'Sₙ = n · (a₁ + aₙ) : 2 mit gegebenen Werten, 1 + 2 + … + n.',
                'Letztes Glied erst berechnen, Sachsituationen (Glockenschläge), letztes Glied aus der Summe, Summe der geraden Zahlen.',
                'Summen mit anderem Start, Anzahl der Glieder zu einer Summe, Vielfache in einem Bereich, Fehler „: 2 vergessen“, „doppelt so viele Glieder“.')
ST.typ('arith', '/^/', 'direkt', s=1)
ST.typ('arith', '/^/', 'mehrschritt', s=2)
ST.typ('arith', '/^Berechne \\d+ \\+/', 'verknuepfen')
ST.typ('arith', '/Wie viele Glieder/', 'rueckwaerts')
ST.typ('arith', '/^/', 'transfer', s=3)
ST.neu('arith', 'erkennen', A('Bei 1 + 2 + … + 10 fasst man Zahlen zu Paaren mit gleicher Summe zusammen. Welche Paare?', '1 und 10, 2 und 9, 3 und 8, … – jedes Paar ergibt 11',
       ['1 und 2, 3 und 4, … – jedes Paar ergibt 3', '1 und 10, 2 und 10, … – jedes Paar ergibt 11', '5 und 5 – das Paar ergibt 10'],
       'Erstes mit letztem, zweites mit vorletztem: Jedes Paar ergibt 11, es gibt 5 Paare: 55.', 'Wie im Beispiel 1 + 100.'))
ST.neu('arith', 'einkleidung', Z('Eine Uhr schlägt zu jeder vollen Stunde so oft, wie es Uhr ist (1-mal um 1 Uhr, …, 12-mal um 12 Uhr). Wie oft schlägt sie in 12 Stunden?', 78, '12*(1 + 12)/2',
       '1 + 2 + … + 12 = 12 · 13 : 2 = 78.', 'Welche Zahlen werden addiert?'))
ST.neu('arith', 'umkehr', Z('Eine arithmetische Reihe mit 10 Gliedern hat die Summe 155 und a₁ = 2. Wie groß ist a₁₀?', 29, '155*2/10 - 2',
       '155 = 10 · (2 + a₁₀) : 2 = 5 · (2 + a₁₀) ⇒ 2 + a₁₀ = 31 ⇒ a₁₀ = 29.', 'Setze in die Summenformel ein.'))
ST.neu('arith', 'mehrschritt', Z('Berechne die Summe aller geraden Zahlen von 2 bis 100.', 2550, '50*(2 + 100)/2',
       '50 Zahlen, erstes 2, letztes 100: 50 · 102 : 2 = 2 550.', 'Wie viele gerade Zahlen sind es?'))
ST.neu('arith', 'fehler', A('Jemand rechnet 1 + 2 + … + 50 = 50 · 51 = 2 550. Was stimmt?', 'Falsch: Es fehlt „: 2“, richtig ist 1 275.', ['Richtig.', 'Falsch: 50 · 50 = 2 500.', 'Falsch: 51 · 52 : 2 = 1 326.'],
       '50 Zahlen bilden 25 Paare mit Summe 51: 25 · 51 = 1 275. 50 · 51 zählt jede Zahl doppelt.', 'Wie viele Paare gibt es?'))
ST.neu('arith', 'begruenden', A('Stimmt: Verdoppelt man n in 1 + 2 + … + n, verdoppelt sich auch die Summe?', 'Nein, sie wird etwa viermal so groß.',
       ['Ja, genau doppelt so groß.', 'Ja, weil doppelt so viele Zahlen addiert werden.', 'Nein, sie bleibt gleich.'],
       'Beispiel: 1 + … + 10 = 55, 1 + … + 20 = 210. Es kommen mehr Zahlen dazu, und die neuen sind auch größer: n(n + 1) : 2 wächst etwa wie n².', 'Probiere n = 10 und n = 20.'))
ST.knobel('arith', Z('Die Summe von 10 aufeinanderfolgenden natürlichen Zahlen ist 155. Wie heißt die kleinste?', 11, '(155 - 45)/10',
          'Zahlen a, a + 1, …, a + 9. Summe 10a + (0 + 1 + … + 9) = 10a + 45 = 155 ⇒ a = 11. Probe: 11 + … + 20 = 155.', 'Nenne die kleinste Zahl a.'))
ST.knobel('arith', Z('Wie viele Zahlen 1 + 2 + 3 + … muss man mindestens addieren, damit die Summe größer als 1 000 ist?', 45, '45',
          'n(n + 1) : 2 > 1 000 ⇒ n(n + 1) > 2 000. 44 · 45 = 1 980 reicht nicht, 45 · 46 = 2 070 schon. Also 45 Zahlen (Summe 1 035).', 'Schätze: n² ≈ 2 000.'))

# geom
ST.stufenleiter('geom', 'Sₙ einer geometrischen Reihe mit a₁ und q bzw. durch Addieren.',
                'Negatives q, Reihen aus einer Folge, Sachsituation (Kettenmail), Anzahl der Glieder zu einer Endzahl.',
                'Anzahl der Glieder zu einer Summe, K.-o.-Turnier, a₁ aus der Summe, Brüche als Glieder, Fehler „Glied statt Summe“, Zweierpotenzen begründen.')
ST.typ('geom', '/^/', 'direkt', s=1)
ST.typ('geom', '/^/', 'mehrschritt', s=2)
ST.typ('geom', '/Wie viele Glieder|Wie groß ist a₁/', 'rueckwaerts')
ST.typ('geom', '/Turnier/', 'transfer')
ST.typ('geom', '/^/', 'verknuepfen', s=3)
ST.neu('geom', 'erkennen', L('Bei 3 + 6 + 12 + 24: Welche Werte haben a₁, q und n?', 'a₁ = □; q = □; n = □', [3, 2, 4], ['3', '6/3', '4'],
       'Erstes Glied 3, Faktor 6 : 3 = 2, vier Glieder.', 'Zähle die Summanden.'))
ST.neu('geom', 'einkleidung', Z('Eine Kettenmail: Am 1. Tag werden 2 Mails verschickt, jeden Tag dreimal so viele wie am Vortag. Wie viele Mails sind nach 4 Tagen insgesamt verschickt?', 80, '2 + 6 + 18 + 54',
       '2 + 6 + 18 + 54 = 80, oder 2 · (3⁴ − 1) : 2 = 80.', 'Schreibe die vier Tage auf.'))
ST.neu('geom', 'umkehr', Z('Wie viele Glieder hat die Summe 1 + 2 + 4 + … + 64?', 7, '7', '1, 2, 4, 8, 16, 32, 64: 64 = 2⁶, also 7 Glieder (2⁰ bis 2⁶).', 'Zähle die Zweierpotenzen.'))
ST.neu('geom', 'fehler', A('a₁ = 3, q = 2. Jemand berechnet S₄ = 3 · 2⁴ = 48. Was stimmt?', 'Falsch: Das ist (fast) ein Glied, keine Summe; S₄ = 3 + 6 + 12 + 24 = 45.',
       ['Richtig.', 'Falsch: S₄ = 3 · 2³ = 24.', 'Falsch: S₄ = 3 · 4 · 2 = 24.'], 'Die Summe braucht alle vier Glieder: 3 · (2⁴ − 1) : (2 − 1) = 45.', 'Addiere die Glieder zur Probe.'))
ST.neu('geom', 'begruenden', A('Stimmt: 1 + 2 + 4 + … + 2ⁿ⁻¹ ist immer um 1 kleiner als 2ⁿ?', 'Ja, die Summe ist 2ⁿ − 1.', ['Nein, sie ist gleich 2ⁿ.', 'Nein, sie ist doppelt so groß wie 2ⁿ.', 'Nur für gerade n.'],
       'Mit a₁ = 1 und q = 2: Sₙ = (2ⁿ − 1) : (2 − 1) = 2ⁿ − 1. Beispiel 1 + 2 + 4 = 7 = 8 − 1.', 'Probiere n = 3 und n = 4.'))
ST.knobel('geom', Z('Wie viele Glieder von 1 + 1/2 + 1/4 + 1/8 + … braucht man mindestens, damit die Summe größer als 1,99 ist?', 8, '8',
          'Nach n Gliedern fehlt bis 2 genau das letzte Glied: Sₙ = 2 − 1/2ⁿ⁻¹. Gefordert 1/2ⁿ⁻¹ < 0,01: 2⁶ = 64 reicht nicht, 2⁷ = 128 schon ⇒ n − 1 = 7, n = 8.',
          'Wie viel fehlt nach 1, 2, 3 Gliedern noch bis 2?'))
ST.knobel('geom', A('Auf ein Schachbrett legt man 1, 2, 4, 8, … Reiskörner. Wie verhält sich die Zahl der Körner auf Feld 64 zu allen Körnern auf den 63 Feldern davor?', 'Feld 64 hat genau 1 Korn mehr als alle 63 davor zusammen.',
          ['Feld 64 hat halb so viele.', 'Feld 64 hat genauso viele.', 'Feld 64 hat doppelt so viele.'],
          'Feld 64 hat 2⁶³ Körner, die Felder davor zusammen 1 + 2 + … + 2⁶² = 2⁶³ − 1. Also genau eins mehr.', 'Nutze 1 + 2 + … + 2ⁿ⁻¹ = 2ⁿ − 1.'))

# sach
ST.stufenleiter('sach', 'Arithmetische Reihe in einer vertrauten Sachsituation direkt ausrechnen.',
                'Stapel, Sparpläne, Schachbrett, Zahl der Reihen zu einer Gesamtzahl.',
                'Dauer bis zu einem Sparziel, Weiterleiten von Nachrichten, zwei Angebote vergleichen, Turnierspiele, Fehler „letzte Woche statt Summe“, mehrteilige Stapelaufgabe.')
ST.typ('sach', '/^/', 'direkt', s=1)
ST.typ('sach', '/Baumstämme|Schachbrett/', 'einkleidung')
ST.typ('sach', '/^/', 'mehrschritt', s=2)
ST.typ('sach', '/Nach wie vielen Monaten/', 'rueckwaerts')
ST.typ('sach', '/Angebot A/', 'transfer')
ST.typ('sach', '/^/', 'verknuepfen', s=3)
ST.neu('sach', 'erkennen', A('Ein Sparplan: 10 €, 15 €, 20 €, 25 €, … Welche Art von Reihe beschreibt das Gesparte insgesamt?', 'eine arithmetische Reihe (d = 5)', ['eine geometrische Reihe (q = 1,5)', 'keine Reihe', 'eine geometrische Reihe (q = 5)'],
       'Jeden Monat kommen 5 € mehr dazu: gleiche Differenz, also arithmetisch.', 'Gleiche Differenz oder gleicher Faktor?'))
ST.neu('sach', 'umkehr', Z('Ein Stapel Baumstämme hat oben 3 Stämme, jede Reihe darunter einen mehr; insgesamt sind es 25 Stämme. Wie viele Reihen hat der Stapel?', 5, '5',
       '3 + 4 + 5 + 6 + 7 = 25: fünf Reihen.', 'Addiere Reihe für Reihe, bis 25 erreicht sind.'))
ST.neu('sach', 'fehler', A('Ein Läufer läuft in Woche 1 genau 5 km und jede Woche 2 km mehr. Gefragt ist die Gesamtstrecke nach 8 Wochen. Jemand rechnet 5 + 7 · 2 = 19 km. Was stimmt?',
       'Falsch: 19 km ist nur Woche 8; insgesamt 8 · (5 + 19) : 2 = 96 km.', ['Richtig.', 'Falsch: 5 + 8 · 2 = 21 km.', 'Falsch: 8 · 5 = 40 km.'],
       'Gefragt ist die Summe aller Wochen, nicht das letzte Glied.', 'Glied oder Summe?'))
ST.neu('sach', 'pruefung', L('Ein Bauer stapelt Strohballen: unten 20, jede Reihe darüber 2 weniger, oben 2. a) Wie viele Reihen? b) Wie viele Ballen insgesamt?', 'a) □; b) □', [10, 110],
       ['(20 - 2)/2 + 1', '10*(20 + 2)/2'], 'a) 20, 18, …, 2: (20 − 2) : 2 + 1 = 10 Reihen. b) 10 · (20 + 2) : 2 = 110 Ballen.', 'Bestimme zuerst die Zahl der Reihen.'))
ST.knobel('sach', Z('Ein Frosch springt am 1. Tag 1 m, an jedem weiteren Tag halb so weit wie am Vortag. Welche Strecke (in m) kann er auf diese Weise höchstens zurücklegen?', 2, '2',
          '1 + 1/2 + 1/4 + … Nach jedem Tag fehlt bis 2 m genau so viel wie der letzte Sprung. Die Summe kommt 2 m beliebig nahe, erreicht sie aber nie: höchstens 2 m.',
          'Wie viel fehlt nach 1, 2, 3 Tagen noch bis 2 m?', einheit='m'))
ST.knobel('sach', Z('Bei einer Feier stößt jeder Gast mit jedem anderen genau einmal an. Es klirrt 45-mal. Wie viele Gäste sind es?', 10, '10',
          'Der erste stößt mit n − 1 an, der zweite noch mit n − 2, … Zusammen 1 + 2 + … + (n − 1) = n(n − 1) : 2 = 45 ⇒ n(n − 1) = 90 ⇒ n = 10.', 'Zähle, mit wie vielen der 1., 2., 3. Gast neu anstößt.'))

# verstehen
ST.stufenleiter('verstehen', 'Anzahl der Summanden zählen, „Glied statt Summe“ erkennen.',
                'Fehler „: 2 vergessen“, Summen ausschreiben, n zu einer Summe, Anzahl in einer Reihe mit Schrittweite.',
                'Falscher Exponent in der Formel, Teilsummen aus Sₙ, Glied aus der Summenformel, aₙ = Sₙ − Sₙ₋₁ begründen.')
ST.typ('verstehen', '/Ben antwortet/', 'erkennen')
ST.typ('verstehen', '/^/', 'direkt', s=1)
ST.typ('verstehen', '/Wie viele Summanden/', 'direkt')
ST.typ('verstehen', '/^/', 'mehrschritt', s=2)
ST.typ('verstehen', '/Tom rechnet/', 'fehler')
ST.typ('verstehen', '/Wie groß ist a₁₀ \\+|Wie groß ist a₁₁ \\+/', 'verknuepfen')
ST.typ('verstehen', '/^/', 'rueckwaerts', s=3)
ST.neu('verstehen', 'einkleidung', Z('Ein Turm aus Bechern hat oben 1 Becher, jede Reihe darunter einen mehr, unten 8. Wie viele Becher sind es?', 36, '8*9/2',
       '1 + 2 + … + 8 = 8 · 9 : 2 = 36.', 'Wie viele Reihen sind es?'))
ST.neu('verstehen', 'umkehr', Z('Es gilt ∑ₖ₌₁ⁿ k = 55. Wie groß ist n?', 10, '10', 'n(n + 1) : 2 = 55 ⇒ n(n + 1) = 110 = 10 · 11 ⇒ n = 10.', 'Welches Produkt zweier Nachbarzahlen ergibt 110?'))
ST.neu('verstehen', 'darstellung', A('Welche Summe gehört zu ∑ₖ₌₂⁵ k²?', '4 + 9 + 16 + 25', ['1 + 4 + 9 + 16 + 25', '2 + 3 + 4 + 5', '4 + 6 + 8 + 10'],
       'k läuft von 2 bis 5, jedes k wird quadriert.', 'Wo beginnt k?'))
ST.neu('verstehen', 'mehrschritt', Z('Wie viele Summanden hat 5 + 8 + 11 + … + 50?', 16, '(50 - 5)/3 + 1', 'Schrittweite 3: (50 − 5) : 3 = 15 Schritte, also 16 Summanden.', 'Zähle die Schritte und denk an den ersten Summanden.'))
ST.neu('verstehen', 'begruenden', A('Stimmt: Für jede Folge gilt aₙ = Sₙ − Sₙ₋₁?', 'Ja: Sₙ ist Sₙ₋₁ plus das Glied aₙ.', ['Nein, nur für arithmetische Folgen.', 'Nein, nur für geometrische Folgen.', 'Nein, es gilt aₙ = Sₙ + Sₙ₋₁.'],
       'Sₙ = a₁ + … + aₙ₋₁ + aₙ = Sₙ₋₁ + aₙ. Das gilt für jede Folge.', 'Schreibe S₄ und S₃ aus.'))
ST.knobel('verstehen', Z('Für eine Folge gilt Sₙ = n² für jedes n. Wie groß ist a₁₀₀?', 199, '100**2 - 99**2',
          'a₁₀₀ = S₁₀₀ − S₉₉ = 10 000 − 9 801 = 199. Allgemein aₙ = 2n − 1: die ungeraden Zahlen.', 'Nutze aₙ = Sₙ − Sₙ₋₁.'))
ST.knobel('verstehen', A('Jemand „beweist“: S = 1 + 2 + 4 + 8 + … (ohne Ende). Dann ist 2S = 2 + 4 + 8 + … = S − 1, also S = −1. Wo steckt der Fehler?',
          'Die Summe wächst ohne Grenze; mit ihr darf man nicht wie mit einer Zahl rechnen.', ['2S ist nicht S − 1, sondern S + 1.', 'Kein Fehler, S = −1.', 'Man hätte durch 2 teilen müssen.'],
          'Die Teilsummen 1, 3, 7, 15, … werden beliebig groß. Ein „S“ als Zahl gibt es nicht, also sind Umformungen wie 2S = S − 1 sinnlos. (Bei 1 + 1/2 + 1/4 + … geht es gut, weil die Summe gegen 2 strebt.)',
          'Gibt es überhaupt eine Zahl S?'))

if __name__ == '__main__':
    stufen('funktionen.reihen', ST)


# ---- AUFLOESEN (Vierundzwanzigste Runde, Zweig aufloesen, siehe _aufloesen.py und _af_plan.py) ----
if __name__ == '__main__':
    from _aufloesen import aufloesen_datei
    aufloesen_datei('funktionen.reihen')
# ---- AUFLOESEN ENDE ----
