#!/usr/bin/env python3
"""Thema terme.umformen – Terme umformen (Gymnasium Bayern, Klasse 7). Runde 9: Aufgaben auffüllen.

Lernkarten unverändert aus inhalte/klar/terme.umformen.json; neu sind nur die Aufgaben.
Term-Antworten als luecken mit Term-Vorlage (das Kind tippt den ganzen Term), z. B. „□x + □y“, „□x² + □x + □“, „□x(□x + □)“.
"""
import math
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _auffuellen import A, L, Z, baue, etappen_aus_klar, faktor, term, zt, kl  # noqa: E402

META = {'thema_schluessel': 'terme.umformen', 'thema_id': 29, 'block_id': 62, 'klasse': {'gym_by': 7}}
TITEL = [('zusammenfassen', 'Gleichartige Glieder zusammenfassen'), ('produkte', 'Produkte vereinfachen'),
         ('minusklammer', 'Minus vor der Klammer'), ('ausmultiplizieren', 'Ausmultiplizieren'),
         ('summe_mal_summe', 'Summe mal Summe'), ('ausklammern', 'Gemeinsamen Faktor ausklammern'),
         ('aequivalenz', 'Äquivalente Terme'), ('binomisch', 'Binomische Formeln')]
ETAPPEN = etappen_aus_klar(META['thema_schluessel'], TITEL)
HW = 'Tippe den ganzen Term ein, z. B. 3x − 2y.'


def nz(R, a, b):
    """Zufallszahl aus [a, b] ohne 0."""
    while True:
        x = R.randint(a, b)
        if x: return x


def vz(R, a, b):
    return R.choice([-1, 1]) * R.randint(a, b)


# ---------------- Gleichartige Glieder zusammenfassen ----------------
def g_zusammenfassen(R, s):
    if s == 1:
        a, c = R.randint(2, 9), nz(R, -6, 6)
        b, d = R.randint(2, 9), nz(R, -6, 6)
        if a + c == 0 or b + d == 0: return g_zusammenfassen(R, s)
        t = term([(a, 'x'), (b, 'y'), (c, 'x'), (d, 'y')])
        return L(f'Fasse zusammen: {t}', '□x + □y', [a + c, b + d], [f'{a} + ({c})', f'{b} + ({d})'],
                 f'x-Glieder: {term([(a, "x"), (c, "x")])} = {term([(a + c, "x")])}. y-Glieder: {term([(b, "y"), (d, "y")])} = {term([(b + d, "y")])}. '
                 f'Ergebnis: {term([(a + c, "x"), (b + d, "y")])}.', 'Sortiere zuerst: alle x-Glieder zusammen, alle y-Glieder zusammen. Das Vorzeichen gehört zum Glied.', HW)
    if s == 2:
        art = R.choice(['quadrat', 'zahl'])
        if art == 'quadrat':
            p, q, r, u, w = nz(R, -5, 6), nz(R, -7, 7), nz(R, -6, 6), nz(R, -7, 7), nz(R, -9, 9)
            if p + r == 0 or q + u == 0: return g_zusammenfassen(R, s)
            t = term([(p, 'x²'), (q, 'x'), (r, 'x²'), (w, ''), (u, 'x')])
            return L(f'Fasse zusammen: {t}', '□x² + □x + □', [p + r, q + u, w], [f'{p} + ({r})', f'{q} + ({u})', str(w)],
                     f'x² und x sind verschieden. x²-Glieder: {term([(p + r, "x²")])}, x-Glieder: {term([(q + u, "x")])}, Zahl: {zt(w)}. '
                     f'Ergebnis: {term([(p + r, "x²"), (q + u, "x"), (w, "")])}.', 'x² und x sind nicht gleichartig. Ordne nach x², x und Zahlen.', HW)
        a, b, c, d = R.randint(2, 12), vz(R, 2, 15), nz(R, -9, 9), vz(R, 2, 15)
        if a + c == 0 or b + d == 0: return g_zusammenfassen(R, s)
        t = term([(a, 'a'), (b, ''), (c, 'a'), (d, '')])
        return L(f'Fasse zusammen: {t}', '□a + □', [a + c, b + d], [f'{a} + ({c})', f'{b} + ({d})'],
                 f'a-Glieder: {term([(a + c, "a")])}. Zahlen: {zt(b)} {"+" if d > 0 else "−"} {zt(abs(d))} = {zt(b + d)}. Ergebnis: {term([(a + c, "a"), (b + d, "")])}.',
                 'Zahlen ohne Buchstaben sind untereinander gleichartig. Fasse sie extra zusammen.', 'Tippe den ganzen Term ein, z. B. 3a − 2.')
    art = R.choice(['fehler', 'umfang', 'fehler2'])
    if art == 'umfang':
        a, b = R.randint(2, 9), R.randint(2, 9)
        if a == b: return g_zusammenfassen(R, s)
        return L(f'Ein Rechteck ist {term([(a, "x")])} lang und {term([(b, "y")])} breit. Gib den Umfang als Term an.', '□x + □y', [2 * a, 2 * b], [f'2 * {a}', f'2 * {b}'],
                 f'Umfang = {a}x + {b}y + {a}x + {b}y = {2 * a}x + {2 * b}y. x und y bleiben getrennt.', 'Der Umfang ist die Länge rundherum: jede Seite zweimal.', HW)
    a, b, c = R.randint(2, 9), R.randint(2, 9), R.randint(2, 9)
    if art == 'fehler':
        return A(R, f'Jemand rechnet: {a}x + {b}y = {a + b}xy. Was stimmt?', f'Falsch: x und y sind verschieden, {a}x + {b}y bleibt stehen.',
                 [f'Richtig: {a} + {b} = {a + b}.', f'Falsch: Es muss {a * b}xy heißen.', f'Falsch: Es muss {a + b}x heißen.'],
                 f'Nur gleichartige Glieder darf man zusammenfassen. {a}x und {b}y haben verschiedene Buchstaben. Probe mit x = 1, y = 1: {a + b} gegen {a + b}, aber x = 2, y = 1: {2 * a + b} gegen {2 * (a + b)}.',
                 'Haben beide Glieder denselben Buchstabenteil?')
    if a == c: return g_zusammenfassen(R, s)
    return A(R, f'Welcher Term ist gleichwertig zu {a}x − {c}x + {b}?', term([(a - c, 'x'), (b, '')]),
             [term([(a + c, 'x'), (b, '')]), term([(a - c + b, 'x')]), term([(a - c, 'x'), (-b, '')])],
             f'Das Minus gehört zu {c}x: {a}x − {c}x = {term([(a - c, "x")])}. Die Zahl {b} bleibt einzeln stehen: {term([(a - c, "x"), (b, "")])}.',
             'Das Vorzeichen vor einem Glied wandert mit ihm.')


# ---------------- Produkte vereinfachen ----------------
def g_produkte(R, s):
    if s == 1:
        a, b = R.randint(2, 9), R.randint(2, 9)
        if R.random() < .5:
            return L(f'Vereinfache: {a}x · {b}y', '□xy', [a * b], [f'{a} * {b}'],
                     f'Zahlen malnehmen: {a} · {b} = {a * b}. Buchstaben dahinter: xy. Ergebnis: {a * b}xy.', 'Erst die Zahlen malnehmen, dann die Buchstaben dahinterschreiben.', 'Tippe den ganzen Term ein, z. B. 12xy.')
        return L(f'Vereinfache: {a}a · {b}a', '□a²', [a * b], [f'{a} * {b}'],
                 f'{a} · {b} = {a * b} und a · a = a². Ergebnis: {a * b}a².', 'Gleiche Buchstaben werden zur Potenz: a · a = a².', 'Tippe den ganzen Term ein, z. B. 6a².')
    if s == 2:
        a, b = vz(R, 2, 9), vz(R, 2, 9)
        if a > 0 and b > 0: a = -a
        art = R.choice(['quadrat', 'drei'])
        if art == 'quadrat':
            return L(f'Vereinfache: {faktor(a, "x")} · {faktor(b, "x")}', '□x²', [a * b], [f'({a}) * ({b})'],
                     f'{kl(a)} · {kl(b)} = {zt(a * b)}, x · x = x². {"Minus mal minus ergibt plus" if a < 0 and b < 0 else "Plus mal minus ergibt minus"}. Ergebnis: {term([(a * b, "x²")])}.',
                     'Bestimme zuerst das Vorzeichen, dann die Zahl, dann den Buchstabenteil.', 'Tippe den ganzen Term ein, z. B. −6x².')
        c = vz(R, 2, 5)
        return L(f'Vereinfache: {faktor(a, "a")} · {faktor(c, "")} · {faktor(b, "b")}', '□ab', [a * b * c], [f'({a}) * ({c}) * ({b})'],
                 f'Zahlen: {kl(a)} · {kl(c)} · {kl(b)} = {zt(a * b * c)}. Buchstaben: ab. Ergebnis: {term([(a * b * c, "ab")])}.',
                 'Zähle die Minuszeichen: gerade Anzahl ergibt plus, ungerade minus.', 'Tippe den ganzen Term ein, z. B. −24ab.')
    art = R.choice(['flaeche', 'fehler', 'fehler'])
    a, b = R.randint(2, 9), R.randint(2, 9)
    if art == 'flaeche':
        return L(f'Ein Rechteck ist {a}a lang und {b}a breit. Gib den Flächeninhalt als Term an.', '□a²', [a * b], [f'{a} * {b}'],
                 f'Fläche = Länge · Breite = {a}a · {b}a = {a * b}a². Eine Fläche hat zwei Längen als Faktoren.', 'Fläche ist Länge mal Breite. Wie oft steckt a darin?', 'Tippe den ganzen Term ein, z. B. 6a².')
    return A(R, f'Jemand rechnet: {a}x · {b}x = {a * b}x. Was stimmt?', f'Falsch: Es muss {a * b}x² heißen.',
             [f'Richtig: {a} · {b} = {a * b}.', f'Falsch: Es muss {a + b}x heißen.', f'Falsch: Es muss {a + b}x² heißen.'],
             f'x kommt zweimal als Faktor vor: x · x = x². Also {a}x · {b}x = {a * b}x². Probe mit x = 2: {2 * a} · {2 * b} = {4 * a * b}, und {a * b} · 4 = {4 * a * b} ✓',
             'Wie oft steht x als Faktor da?')


# ---------------- Minus vor der Klammer ----------------
def g_minusklammer(R, s):
    if s == 1:
        a, b, c = R.randint(5, 12), R.randint(1, 4), R.randint(1, 9)
        op = R.choice(['+', '−'])
        cc = c if op == '−' else -c
        return L(f'Löse die Klammer auf und fasse zusammen: {a}x − ({term([(b, "x")])} {op} {c})', '□x + □', [a - b, cc],
                 [f'{a} - {b}', f'-({-cc})' if cc < 0 else str(cc)],
                 f'Minus vor der Klammer: Jedes Vorzeichen wechselt: {a}x − {term([(b, "x")])} {"+" if op == "−" else "−"} {c}. Ergebnis: {term([(a - b, "x"), (cc, "")])}.',
                 'Lass die Klammer weg und dreh jedes Vorzeichen darin um.', 'Tippe den ganzen Term ein, z. B. 3x + 3.')
    if s == 2:
        a, b, c, d = R.randint(2, 9), vz(R, 1, 9), R.randint(2, 9), vz(R, 1, 9)
        if a == c or b == d: return g_minusklammer(R, s)
        t = f'({term([(a, "x"), (b, "")])}) − ({term([(c, "x"), (d, "")])})'
        return L(f'Löse die Klammern auf und fasse zusammen: {t}', '□x + □', [a - c, b - d], [f'{a} - {c}', f'({b}) - ({d})'],
                 f'Die erste Klammer fällt weg. Bei der zweiten wechseln die Vorzeichen: {term([(a, "x"), (b, ""), (-c, "x"), (-d, "")])} = {term([(a - c, "x"), (b - d, "")])}.',
                 'Nur vor der zweiten Klammer steht ein Minus. Dort wechselt jedes Vorzeichen.', 'Tippe den ganzen Term ein, z. B. 3x − 4.')
    art = R.choice(['fehler', 'einkauf', 'zahl'])
    if art == 'zahl':
        a, b, c = R.randint(2, 6), R.randint(2, 9), R.randint(1, 9)
        return L(f'Löse die Klammer auf: −{a}({term([(b, "x"), (c, "")])})', '□x + □', [-a * b, -a * c], [f'-{a} * {b}', f'-{a} * {c}'],
                 f'Hier steht noch eine Zahl vor der Klammer: (−{a}) · {b}x = {term([(-a * b, 'x')])} und (−{a}) · {c} = {zt(-a * c)}. Ergebnis: {term([(-a * b, "x"), (-a * c, "")])}.',
                 'Minus und Zahl vor der Klammer: jedes Glied mit der ganzen Zahl samt Minus malnehmen.', 'Tippe den ganzen Term ein, z. B. −2x − 6.')
    if art == 'einkauf':
        g, p, r = R.randint(20, 50), R.randint(8, 19), R.randint(2, 5)
        return Z(f'Du hast {g} €. Ein T-Shirt kostet {p} €, an der Kasse gibt es {r} € Rabatt. Rechne {g} − ({p} − {r}). Wie viel Geld bleibt dir?',
                 g - p + r, f'{g} - ({p} - {r})', f'{g} − ({p} − {r}) = {g} − {p} + {r} = {g - p + r}. Der Rabatt bleibt dir, darum kommt er dazu.',
                 f'Löse die Klammer auf: Aus − {r} in der Klammer wird + {r}.', einheit='€')
    a, b, c = R.randint(5, 12), R.randint(1, 4), R.randint(2, 9)
    return A(R, f'Welche Umformung von {a}x − ({b}x − {c}) ist richtig?', f'{a}x − {b}x + {c}',
             [f'{a}x − {b}x − {c}', f'{a}x + {b}x − {c}', f'{a}x − {b}x'],
             f'Vor der Klammer steht ein Minus, also wechselt jedes Vorzeichen darin: −{b}x bleibt −{b}x, −{c} wird +{c}. Ergebnis: {term([(a - b, "x"), (c, "")])}.',
             'Jedes Vorzeichen in der Klammer wechselt, nicht nur das erste.')


# ---------------- Ausmultiplizieren ----------------
def g_ausmultiplizieren(R, s):
    if s == 1:
        a, b, c = R.randint(2, 9), R.randint(1, 9), R.randint(1, 12)
        op = R.choice([1, -1])
        return L(f'Multipliziere aus: {a}({term([(b, "x"), (op * c, "")])})', '□x + □', [a * b, a * op * c], [f'{a} * {b}', f'{a} * ({op * c})'],
                 f'{a} · {term([(b, "x")])} = {a * b}x und {a} · {kl(op * c)} = {zt(a * op * c)}. Ergebnis: {term([(a * b, "x"), (a * op * c, "")])}.',
                 'Der Faktor vor der Klammer wird mit jedem Glied malgenommen.', 'Tippe den ganzen Term ein, z. B. 3x + 6.')
    if s == 2:
        art = R.choice(['negativ', 'x'])
        if art == 'negativ':
            a, b, c = -R.randint(2, 9), vz(R, 1, 9), vz(R, 1, 12)
            return L(f'Multipliziere aus: {zt(a)}({term([(b, "x"), (c, "")])})', '□x + □', [a * b, a * c], [f'({a}) * ({b})', f'({a}) * ({c})'],
                     f'{kl(a)} · {faktor(b, "x")} = {term([(a * b, "x")])} und {kl(a)} · {kl(c)} = {zt(a * c)}. Ergebnis: {term([(a * b, "x"), (a * c, "")])}.',
                     'Achte auf die Vorzeichen: Minus mal Minus ergibt Plus.', 'Tippe den ganzen Term ein, z. B. −6x + 8.')
        a, b, c = vz(R, 2, 6), R.randint(1, 9), vz(R, 1, 12)
        return L(f'Multipliziere aus: {term([(a, "x")])}({term([(b, "x"), (c, "")])})', '□x² + □x', [a * b, a * c], [f'({a}) * {b}', f'({a}) * ({c})'],
                 f'{faktor(a, "x")} · {term([(b, "x")])} = {term([(a * b, "x²")])} und {faktor(a, "x")} · {kl(c)} = {term([(a * c, "x")])}. Ergebnis: {term([(a * b, "x²"), (a * c, "x")])}.',
                 'x · x = x². Jedes Glied in der Klammer bekommt den Faktor.', 'Tippe den ganzen Term ein, z. B. 2x² − 6x.')
    art = R.choice(['zwei', 'fehler', 'geschenk'])
    if art == 'zwei':
        a, b, c, d = R.randint(2, 6), vz(R, 1, 9), R.randint(2, 6), vz(R, 1, 9)
        if a == c: return g_ausmultiplizieren(R, s)
        return L(f'Vereinfache: {a}(x {"+" if b > 0 else "−"} {abs(b)}) − {c}(x {"+" if d > 0 else "−"} {abs(d)})', '□x + □', [a - c, a * b - c * d],
                 [f'{a} - {c}', f'{a} * ({b}) - {c} * ({d})'],
                 f'Erst ausmultiplizieren: {term([(a, "x"), (a * b, ""), (-c, "x"), (-c * d, "")])}. '
                 f'Dann zusammenfassen: {term([(a - c, "x"), (a * b - c * d, "")])}.',
                 'Vor der zweiten Klammer steht −' + str(c) + '. Nimm jedes Glied mit −' + str(c) + ' mal.', 'Tippe den ganzen Term ein, z. B. 2x + 5.')
    if art == 'geschenk':
        n, p, q = R.randint(3, 9), R.randint(2, 9), R.randint(1, 5)
        return L(f'Für {n} Geschenke kauft jemand je ein Buch für x € und eine Karte für {q} €. Die Kosten sind {n}(x + {q}). Multipliziere aus.', '□x + □',
                 [n, n * q], [str(n), f'{n} * {q}'],
                 f'{n} Bücher kosten {n}x, {n} Karten kosten {n} · {q} = {n * q} €. Ergebnis: {n}x + {n * q}.',
                 'Jedes Geschenk hat ein Buch und eine Karte. Wie viele Karten sind es?', 'Tippe den ganzen Term ein, z. B. 4x + 8.')
    a, b = R.randint(2, 9), R.randint(2, 9)
    return A(R, f'Jemand rechnet: {a}(x + {b}) = {a}x + {b}. Was stimmt?', f'Falsch: Es muss {a}x + {a * b} heißen.',
             [f'Richtig: Die {a} gehört nur zum x.', f'Falsch: Es muss {a + b}x heißen.', f'Falsch: Es muss {a}x + {a + b} heißen.'],
             f'Der Faktor {a} wird mit jedem Glied malgenommen, auch mit {b}: {a} · {b} = {a * b}. Probe mit x = 1: {a} · {1 + b} = {a * (1 + b)}, und {a} + {a * b} = {a + a * b} ✓',
             'Wird jedes Glied in der Klammer mit dem Faktor malgenommen?')


# ---------------- Summe mal Summe ----------------
def g_summe_mal_summe(R, s):
    def kl2(m, t): return f'({term([(m, "x"), (t, "")])})'
    if s == 1:
        a, b = R.randint(1, 9), R.randint(1, 9)
        return L(f'Multipliziere aus: {kl2(1, a)}{kl2(1, b)}', '□x² + □x + □', [1, a + b, a * b], ['1', f'{a} + {b}', f'{a} * {b}'],
                 f'x · x = x², x · {b} = {b}x, {a} · x = {a}x, {a} · {b} = {a * b}. Zusammen: x² + {a + b}x + {a * b}.',
                 'Vier Produkte: jedes Glied der ersten Klammer mal jedes der zweiten.', 'Tippe den ganzen Term ein, z. B. x² + 5x + 6.')
    if s == 2:
        a, b = vz(R, 1, 9), vz(R, 1, 9)
        m = R.choice([1, 1, 2, 3])
        if (a > 0 and b > 0) or m * b + a == 0: return g_summe_mal_summe(R, s)
        return L(f'Multipliziere aus: {kl2(m, a)}{kl2(1, b)}', '□x² + □x + □', [m, m * b + a, a * b], [str(m), f'{m} * ({b}) + ({a})', f'({a}) * ({b})'],
                 f'{term([(m, "x")])} · x = {term([(m, "x²")])}, {term([(m, "x")])} · {kl(b)} = {term([(m * b, "x")])}, {kl(a)} · x = {term([(a, "x")])}, {kl(a)} · {kl(b)} = {zt(a * b)}. '
                 f'Zusammen: {term([(m, "x²"), (m * b + a, "x"), (a * b, "")])}.',
                 'Schreib alle vier Produkte mit Vorzeichen auf und fasse dann die x-Glieder zusammen.', 'Tippe den ganzen Term ein, z. B. x² + x − 6.')
    art = R.choice(['garten', 'fehler', 'zwei'])
    if art == 'garten':
        a, b = R.randint(2, 6), R.randint(1, 5)
        return L(f'Ein quadratischer Garten mit Seite x m wird {a} m länger und {b} m breiter. Gib die neue Fläche (x + {a})(x + {b}) ohne Klammern an.', '□x² + □x + □',
                 [1, a + b, a * b], ['1', f'{a} + {b}', f'{a} * {b}'],
                 f'(x + {a})(x + {b}) = x² + {term([(b, "x")])} + {term([(a, "x")])} + {a * b} = x² + {a + b}x + {a * b}. Die Fläche wächst um {a + b}x + {a * b} m².',
                 'Die neue Fläche ist neue Länge mal neue Breite.', 'Tippe den ganzen Term ein, z. B. x² + 5x + 6.')
    if art == 'zwei':
        a, b, c, d = R.randint(2, 4), vz(R, 1, 7), R.randint(2, 4), vz(R, 1, 7)
        if a * d + b * c == 0: return g_summe_mal_summe(R, s)
        return L(f'Multipliziere aus: {kl2(a, b)}{kl2(c, d)}', '□x² + □x + □', [a * c, a * d + b * c, b * d], [f'{a} * {c}', f'{a} * ({d}) + ({b}) * {c}', f'({b}) * ({d})'],
                 f'{a}x · {c}x = {a * c}x², {a}x · {kl(d)} = {term([(a * d, "x")])}, {kl(b)} · {c}x = {term([(b * c, "x")])}, {kl(b)} · {kl(d)} = {zt(b * d)}. '
                 f'Zusammen: {term([(a * c, "x²"), (a * d + b * c, "x"), (b * d, "")])}.',
                 'Vier Produkte bilden, dann die beiden x-Glieder zusammenfassen.', 'Tippe den ganzen Term ein, z. B. 6x² + 5x − 4.')
    a, b = R.randint(2, 9), R.randint(2, 9)
    return A(R, f'Jemand rechnet: (x + {a})(x + {b}) = x² + {a * b}. Was fehlt?', f'Die Glieder {b}x und {a}x, zusammen {a + b}x.',
             ['Nichts, das Ergebnis stimmt.', f'Nur das Glied {a + b}.', f'Das Glied {a * b}x².'],
             f'Zwei Glieder mal zwei Glieder ergibt vier Produkte: x², {b}x, {a}x und {a * b}. Richtig: x² + {a + b}x + {a * b}. Probe mit x = 1: {(1 + a) * (1 + b)} gegen {1 + a * b}.',
             'Zähle die Produkte: Wie viele müssen es sein?')


# ---------------- Gemeinsamen Faktor ausklammern ----------------
def g_ausklammern(R, s):
    if s == 1:
        g, p, q = R.randint(2, 9), R.randint(1, 9), R.randint(1, 9)
        if math.gcd(p, q) != 1: return g_ausklammern(R, s)
        return L(f'Klammere den größten gemeinsamen Faktor aus: {term([(g * p, "x"), (g * q, "")])}', '□(□x + □)', [g, p, q],
                 [str(g), f'{g * p} // {g}', f'{g * q} // {g}'],
                 f'{g * p} und {g * q} haben den größten gemeinsamen Teiler {g}. {g * p}x = {g} · {term([(p, "x")])}, {g * q} = {g} · {q}. Ergebnis: {g}({term([(p, "x"), (q, "")])}).',
                 'Welche größte Zahl steckt in beiden Gliedern?', 'Tippe den ganzen Term mit Klammer ein, z. B. 4(3x + 1).')
    if s == 2:
        g, p, q = R.randint(1, 6), R.randint(1, 6), vz(R, 1, 9)
        if math.gcd(p, abs(q)) != 1: return g_ausklammern(R, s)
        return L(f'Klammere den größten gemeinsamen Faktor aus: {term([(g * p, "x²"), (g * q, "x")])}', '□x(□x + □)', [g, p, q],
                 [str(g), f'{g * p} // {g}', f'({g * q}) // {g}'],
                 f'In beiden Gliedern steckt {term([(g, "x")])}. {term([(g * p, "x²")])} = {term([(g, "x")])} · {term([(p, "x")])}, {term([(g * q, "x")])} = {term([(g, "x")])} · {kl(q)}. '
                 f'Ergebnis: {term([(g, "x")])}({term([(p, "x"), (q, "")])}).',
                 'Suche die größte Zahl und das x, die in beiden Gliedern stecken.', 'Tippe den ganzen Term mit Klammer ein, z. B. 4x(3x + 1).')
    art = R.choice(['eins', 'fehler', 'pruefen'])
    g = R.randint(2, 7)
    if art == 'eins':
        p = R.randint(2, 6)
        return L(f'Klammere den größten gemeinsamen Faktor aus: {term([(g * p, "x²"), (g, "x")])}', '□x(□x + □)', [g, p, 1], [str(g), f'{g * p} // {g}', f'{g} // {g}'],
                 f'Das zweite Glied {term([(g, "x")])} ist genau der Faktor {term([(g, "x")])}. In der Klammer bleibt 1, denn {g}x · 1 = {g}x. Ergebnis: {g}x({p}x + 1).',
                 'Was bleibt in der Klammer, wenn ein Glied genau der Faktor ist?', 'Tippe den ganzen Term mit Klammer ein, z. B. 4x(3x + 1).')
    p, q = R.randint(2, 6), R.randint(1, 5)
    if math.gcd(p, q) != 1: return g_ausklammern(R, s)
    if art == 'fehler':
        return A(R, f'Jemand klammert aus: {term([(2 * g * p, "x"), (2 * g * q, "")])} = 2({term([(g * p, "x"), (g * q, "")])}). Was stimmt?',
                 f'Gleichwertig, aber nicht vollständig: Der größte Faktor ist {2 * g}.',
                 ['Richtig und vollständig ausgeklammert.', 'Falsch: Die Terme haben verschiedene Werte.', f'Vollständig wäre {2 * g * p}(x + {q}).'],
                 f'In {g * p} und {g * q} steckt noch der Faktor {g}. Vollständig: {2 * g}({term([(p, "x"), (q, "")])}). Ausmultipliziert ergibt beides {term([(2 * g * p, "x"), (2 * g * q, "")])}.',
                 'Haben die Zahlen in der Klammer noch einen gemeinsamen Teiler?')
    return A(R, f'Welche Ausklammerung von {term([(g * p, "x²"), (g * q, "x")])} ist richtig und vollständig?', f'{g}x({term([(p, "x"), (q, "")])})',
             [f'{g}({term([(p, "x²"), (q, "x")])})', f'{g}x({term([(p, "x"), (g * q, "")])})', f'x({term([(g * p, "x"), (q, "")])})'],
             f'Größter gemeinsamer Faktor: {g}x. Probe: {g}x · {p}x = {term([(g * p, "x²")])} und {g}x · {q} = {term([(g * q, "x")])} ✓',
             'Mach bei jeder Antwort die Probe durch Ausmultiplizieren.')


# ---------------- Äquivalente Terme ----------------
def g_aequivalenz(R, s):
    if s == 1:
        a, b, x = R.randint(2, 6), R.randint(1, 9), R.randint(1, 6)
        if R.random() < .5:
            return Z(f'Berechne den Wert des Terms {a}(x + {b}) für x = {x}.', a * (x + b), f'{a} * ({x} + {b})',
                     f'Einsetzen: {a} · ({x} + {b}) = {a} · {x + b} = {a * (x + b)}.', 'Setze die Zahl für x ein. Klammer zuerst.')
        return Z(f'Berechne den Wert des Terms {a}x + {b} für x = {x}.', a * x + b, f'{a} * {x} + {b}',
                 f'Einsetzen: {a} · {x} + {b} = {a * x} + {b} = {a * x + b}.', 'Setze die Zahl für x ein. Punkt vor Strich.')
    if s == 2:
        a, b = R.randint(2, 7), R.randint(2, 9)
        return A(R, f'Welcher Term ist äquivalent zu {a}(x + {b})?', f'{a}x + {a * b}', [f'{a}x + {b}', f'x + {a * b}', f'{a}x + {a + b}'],
                 f'Ausmultiplizieren: {a} · x + {a} · {b} = {a}x + {a * b}. Für jede Zahl x haben beide Terme denselben Wert.',
                 'Multipliziere die Klammer aus und vergleiche.')
    art = R.choice(['gegenbeispiel', 'quadrat', 'pruefen'])
    if art == 'gegenbeispiel':
        return A(R, 'x + x und x · x sind nicht äquivalent. Welche Zahl ist ein Gegenbeispiel?', str(R.choice([1, 3, 4, 5])), ['0', '2'],
                 'Bei x = 0 ergeben beide 0, bei x = 2 beide 4 – das sind keine Gegenbeispiele. Bei jeder anderen Zahl unterscheiden sich die Werte, z. B. x = 3: 6 und 9.',
                 'Setze jede Antwort in beide Terme ein. Ein Gegenbeispiel liefert verschiedene Werte.')
    if art == 'quadrat':
        a = R.randint(2, 6)
        return A(R, f'Sind (x + {a})² und x² + {a * a} äquivalent?', f'Nein, für x = 1 ergibt sich {(1 + a) ** 2} und {1 + a * a}.',
                 [f'Ja, man quadriert einfach beide Glieder.', f'Ja, für x = 0 ergibt sich bei beiden {a * a}.', 'Das kann man nicht entscheiden.'],
                 f'x = 0 passt zufällig ({a * a} und {a * a}), beweist aber nichts. x = 1 ist ein Gegenbeispiel: (1 + {a})² = {(1 + a) ** 2}, aber 1 + {a * a} = {1 + a * a}.',
                 'Eine passende Zahl beweist nichts. Suche ein Gegenbeispiel.')
    a, b, x = R.randint(2, 6), R.randint(2, 9), R.randint(1, 5)
    return Z(f'Setze x = {x} in {a}(x + {b}) und in {a}x + {b} ein. Um wie viel ist der erste Wert größer?', a * (x + b) - (a * x + b),
             f'{a} * ({x} + {b}) - ({a} * {x} + {b})', f'{a}(x + {b}) = {a * (x + b)}, {a}x + {b} = {a * x + b}. Unterschied: {a * (x + b) - (a * x + b)}. Die Terme sind nicht äquivalent.',
             'Berechne beide Werte und ziehe sie voneinander ab.')


# ---------------- Binomische Formeln ----------------
def g_binomisch(R, s):
    if s == 1:
        a = R.randint(1, 10)
        if R.random() < .5:
            return L(f'Wende die 1. binomische Formel an: (x + {a})²', '□x² + □x + □', [1, 2 * a, a * a], ['1', f'2 * {a}', f'{a} * {a}'],
                     f'(x + {a})² = x² + 2 · x · {a} + {a}² = x² + {2 * a}x + {a * a}.', 'a² + 2ab + b²: Das Mittelglied ist 2 · x · ' + str(a) + '.', 'Tippe den ganzen Term ein, z. B. x² + 8x + 16.')
        return L(f'Wende die 2. binomische Formel an: (x − {a})²', '□x² + □x + □', [1, -2 * a, a * a], ['1', f'-2 * {a}', f'{a} * {a}'],
                 f'(x − {a})² = x² − 2 · x · {a} + {a}² = x² − {2 * a}x + {a * a}.', 'a² − 2ab + b²: Das Mittelglied hat ein Minus, das letzte Glied nicht.', 'Tippe den ganzen Term ein, z. B. x² − 6x + 9.')
    if s == 2:
        art = R.choice(['dritte', 'faktor'])
        if art == 'dritte':
            a = R.randint(2, 12)
            return L(f'Wende die 3. binomische Formel an: (x + {a})(x − {a})', '□x² + □', [1, -a * a], ['1', f'-{a} * {a}'],
                     f'(x + {a})(x − {a}) = x² − {a}² = x² − {a * a}. Die Glieder +{a}x und −{a}x heben sich auf.', 'Bei (a + b)(a − b) fällt das Mittelglied weg.', 'Tippe den ganzen Term ein, z. B. x² − 36.')
        m, a = R.randint(2, 5), vz(R, 1, 6)
        return L(f'Multipliziere mit einer binomischen Formel aus: ({term([(m, "x"), (a, "")])})²', '□x² + □x + □', [m * m, 2 * m * a, a * a], [f'{m} * {m}', f'2 * {m} * ({a})', f'({a}) * ({a})'],
                 f'({m}x)² = {m * m}x², 2 · {m}x · {kl(a)} = {term([(2 * m * a, "x")])}, {kl(a)}² = {a * a}. Ergebnis: {term([(m * m, "x²"), (2 * m * a, "x"), (a * a, "")])}.',
                 'Auch die Zahl vor dem x wird quadriert: (3x)² = 9x².', 'Tippe den ganzen Term ein, z. B. 9x² + 12x + 4.')
    art = R.choice(['rueckwaerts', 'fehler', 'kopf'])
    a = R.randint(2, 9)
    if art == 'rueckwaerts':
        return L(f'Ergänze so, dass eine binomische Formel entsteht: x² + {2 * a}x + □ = (x + □)²', 'x² + ' + str(2 * a) + 'x + □ = (x + □)²', [a * a, a],
                 [f'({2 * a} // 2) ** 2', f'{2 * a} // 2'], f'Das Mittelglied {2 * a}x ist 2 · x · {a}. Also ist b = {a} und b² = {a * a}: x² + {2 * a}x + {a * a} = (x + {a})².',
                 'Das Mittelglied ist 2 · x · b. Wie groß ist b?', 'Trage in jedes Feld eine Zahl ein.')
    if art == 'kopf':
        n = R.choice([21, 31, 41, 51, 19, 29, 39, 49])
        b = n % 10 if n % 10 == 1 else 10 - n % 10
        t = n - n % 10 if n % 10 == 1 else n + b
        z = '+' if n % 10 == 1 else '−'
        return Z(f'Rechne geschickt mit einer binomischen Formel: {n}² = ({t} {z} 1)²', n * n, f'{n} ** 2',
                 f'({t} {z} 1)² = {t}² {z} 2 · {t} · 1 + 1 = {t * t} {z} {2 * t} + 1 = {n * n}.', 'Nutze (a + b)² oder (a − b)² mit einer glatten Zehnerzahl.')
    return A(R, f'Jemand rechnet: (x + {a})² = x² + {a * a}. Was stimmt?', f'Falsch: Das Mittelglied {2 * a}x fehlt.',
             ['Richtig: Man quadriert beide Glieder.', f'Falsch: Es muss x² + {2 * a} heißen.', f'Falsch: Es muss x² + {a * a}x heißen.'],
             f'(x + {a})² = (x + {a})(x + {a}) = x² + {a}x + {a}x + {a * a} = x² + {2 * a}x + {a * a}. Probe mit x = 1: {(1 + a) ** 2} gegen {1 + a * a}.',
             'Schreib das Quadrat als Summe mal Summe.')


GEN = {'zusammenfassen': g_zusammenfassen, 'produkte': g_produkte, 'minusklammer': g_minusklammer, 'ausmultiplizieren': g_ausmultiplizieren,
       'summe_mal_summe': g_summe_mal_summe, 'ausklammern': g_ausklammern, 'aequivalenz': g_aequivalenz, 'binomisch': g_binomisch}
# Beispielzahlen der Lernkarten nicht als Aufgabe verwenden
VERBOT = {'zusammenfassen': ['3x + 5y − x + 2y'], 'produkte': ['3a · (−2a)', '3a · 2a'], 'minusklammer': ['5x − (2x − 3)'],
          'ausmultiplizieren': ['−2(3x − 4)'], 'summe_mal_summe': ['(x + 3)(x − 2)'], 'ausklammern': ['12x² + 4x'],
          'aequivalenz': ['2(x + 3)'], 'binomisch': ['(x + 4)²', '(x − 3)²', '(x + 6)(x − 6)']}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Zusammenfassen und multiplizieren', ['zusammenfassen', 'produkte']),
          ('Klammern auflösen', ['minusklammer', 'ausmultiplizieren', 'summe_mal_summe']),
          ('Ausklammern und vergleichen', ['ausklammern', 'aequivalenz', 'binomisch'])],
         'Terme vereinfachen: gleichartige Glieder zusammenfassen, Produkte vereinfachen, Klammern auflösen und ausmultiplizieren, ausklammern, Äquivalenz prüfen und die binomischen Formeln anwenden.',
         ['Nur gleichartige Glieder zusammenfassen.', 'Minus vor der Klammer: jedes Vorzeichen darin wechselt.',
          'Ausmultiplizieren: Der Faktor kommt zu jedem Glied.', 'Summe mal Summe: jedes Glied mal jedes Glied.',
          '(a + b)² = a² + 2ab + b², (a − b)² = a² − 2ab + b², (a + b)(a − b) = a² − b².'],
         verbot=VERBOT,
         offen=['Runde 9: Thema stammt aus der Zeit vor dem Bausatz; die bisherigen Aufgaben liegen nur in der Datenbank. Dieser Generator erzeugt neue Aufgaben, '
                'die beim Einspielen mit einheit_abgleichen(…, \'lassen\') dazukommen. Dubletten zu den alten Aufgaben ließen sich hier nicht prüfen, weil diese nicht im Repository liegen.'])
