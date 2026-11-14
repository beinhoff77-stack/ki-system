#!/usr/bin/env python3
"""Thema funktionen.reihen – Reihen (IB MYP 4, etwa Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403

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
    art = R.choice({1: ['gauss', 'formel'], 2: ['formel', 'ohne_an', 'folge'], 3: ['folge_lang', 'bereich', 'gerade']}[s])
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
    art = R.choice({1: ['formel', 'klein'], 2: ['formel', 'folge', 'q_neg'], 3: ['folge', 'halb', 'n_aus_S', 'q_neg']}[s])
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


GEN = schoen({'summenzeichen': g_summenzeichen, 'arith': g_arith, 'geom': g_geom, 'sach': g_sach, 'verstehen': g_verstehen})

bauen('funktionen.reihen',
      'Reihen mit dem Summenzeichen schreiben und berechnen, Summenformeln für arithmetische und geometrische Reihen anwenden und Sachaufgaben lösen.',
      ['Reihe (series) = Summe von Folgengliedern; ∑ₖ₌₁ⁿ: k von 1 bis n einsetzen und addieren.',
       'Arithmetisch: Sₙ = n · (a₁ + aₙ) : 2.',
       'Geometrisch: Sₙ = a₁ · (qⁿ − 1) : (q − 1), q ≠ 1.',
       'Anzahl der Glieder von k = u bis k = o: o − u + 1.'],
      [('Schreibweise', ['summenzeichen']), ('Summenformeln', ['arith', 'geom']), ('Anwenden', ['sach', 'verstehen'])],
      ETAPPEN, GEN,
      offen=['Unendliche geometrische Reihen (Grenzwert a₁ : (1 − q)) sind nicht enthalten: Das ist IB MYP 5 Extended bzw. DP-Stoff. Annahme: MYP 4 endet bei endlichen Reihen.',
             'Summenzeichen mit Unicode-Indizes (∑ₖ₌₁⁵). Die Grenzen stehen dadurch neben, nicht unter/über dem ∑ – bei Bedarf App-Wunsch für eine Formeldarstellung.'])
