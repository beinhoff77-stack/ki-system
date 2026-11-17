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

# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Klasse 7, siehe _durchsicht_kl7.py) ----
# Thema ohne Zehnte Runde: Stufe 3 war oft nur das Beispiel in Einkleidung oder dreimal derselbe Fehler-Typ. Falsch eingestufte Aufgaben umgestuft,
# Wiederholungen ersetzt, je Lernkarte Stufe-3-Aufgaben mit anderem Gedanken ergänzt (rückwärts, Fehler finden, Parameter, verschachtelt, Einkleidung).
# Vorbilder (Typ und Niveau, eigene Zahlen): BMT8 (ISB) 2019 B1b, 2024 A2, 2025 A4 (vereinfachen), 2014 B7 (ausklammern ergänzen); LehrplanPLUS M7 1.2 (Verdopplung der Seiten).
from _durchsicht_kl7 import Durchsicht, durchsicht_datei  # noqa: E402

DS = Durchsicht('terme.umformen', 19_7_2)
_HT = 'Tippe den ganzen Term ein, z. B. 3x − 2y.'
_HK = 'Tippe den ganzen Term mit Klammer ein, z. B. 4x(3x + 1).'
_HZ = 'Trage in jedes Feld eine Zahl ein.'
# zusammenfassen
DS.stufe('zusammenfassen', 'Welcher Term ist gleichwertig zu 7x − 5x + 8?', 1)
DS.stufe('zusammenfassen', 'Ein Rechteck ist 3x lang und 9y breit. Gib den Umfang als Term an.', 2)
DS.ersetze('zusammenfassen', 'Jemand rechnet: 6x + 9y = 15xy. Was stimmt?',
           DS.L('5x + 4y − T soll zusammengefasst 2x + 7y ergeben. Wie heißt der Term T?', '□x + □y', [3, -3], ['5 - 2', '4 - 7'],
                'Von 5x bis 2x fehlen 3x, also zieht T 3x ab. Von 4y bis 7y kommen 3y dazu, also zieht T −3y ab. T = 3x − 3y.',
                'Rückwärts denken: Was muss T bei den x-Gliedern abziehen, was bei den y-Gliedern?', _HT))
DS.neu('zusammenfassen', 3, DS.L('Der Umfang eines Dreiecks ist 9x + 5y. Zwei Seiten sind 2x + y und 4x − y lang. Wie lang ist die dritte Seite?', '□x + □y', [3, 5],
                                 ['9 - 2 - 4', '5 - 1 + 1'], 'Die zwei Seiten zusammen: 2x + y + 4x − y = 6x. Dritte Seite: 9x + 5y − 6x = 3x + 5y.',
                                 'Fasse die beiden bekannten Seiten zusammen und zieh sie vom Umfang ab.', _HT))
DS.neu('zusammenfassen', 3, DS.A('Im Term 4ab + 3a² − ab + 2a: Welche beiden Glieder sind gleichartig?', '4ab und −ab',
                                 ['3a² und 2a', '4ab und 3a²', '3a² und −ab'],
                                 'Gleichartig heißt: gleicher Buchstabenteil. 4ab und −ab haben beide ab. a² und a sind verschieden.',
                                 'Vergleiche nur den Buchstabenteil – auch die Hochzahl zählt.'))
DS.neu('zusammenfassen', 3, DS.A('Welcher Term ergibt zusammengefasst genau 5x?', '3x + 4x − 2x', ['3x − 4x + 2x', '3x + 4 − 2x', '6x − x − x'],
                                 '3x + 4x − 2x = 5x. Die anderen: 3x − 4x + 2x = x; 3x + 4 − 2x = x + 4; 6x − x − x = 4x.',
                                 'Fasse jeden Term zusammen. Achtung: 4 ohne x ist nicht gleichartig.'))
# produkte
DS.stufe('produkte', 'Ein Rechteck ist 6a lang und 5a breit. Gib den Flächeninhalt als Term an.', 2)
DS.ersetze('produkte', 'Jemand rechnet: 5x · 4x = 20x. Was stimmt?',
           DS.L('Ein Quader ist 2a lang, 3a breit und a hoch. Gib sein Volumen als Term an.', '□a³', [6], ['2 * 3 * 1'],
                'V = 2a · 3a · a = (2 · 3 · 1) · a · a · a = 6a³.', 'Volumen ist Länge · Breite · Höhe. Wie oft kommt a als Faktor vor?',
                'Tippe den ganzen Term ein, z. B. 5a³.'))
DS.ersetze('produkte', 'Jemand rechnet: 8x · 8x = 64x. Was stimmt?',
           DS.L('Welcher Faktor fehlt? 4x · (?) = −20x²', '□x', [-5], ['-20 / 4'],
                '4 · (−5) = −20 und x · x = x². Der Faktor ist −5x.', 'Rückwärts: Welche Zahl mal 4 ergibt −20? Und ein x fehlt noch.', 'Tippe den Faktor ein, z. B. −3x.'))
DS.neu('produkte', 3, DS.A('Vereinfache (−2a) · (−3b) · (−c). Was kommt heraus?', '−6abc', ['6abc', '−5abc', '5abc'],
                           'Zahlen: (−2) · (−3) · (−1) = −6, drei Minuszeichen ergeben minus. Buchstaben: a · b · c = abc. Also −6abc.',
                           'Zähle die Minuszeichen: Gerade Anzahl ergibt plus, ungerade minus. Vor c steht die Zahl −1.'))
DS.neu('produkte', 3, DS.A('Ein Quadrat hat die Seitenlänge 3x. Jede Seite wird verdoppelt. Was passiert mit dem Flächeninhalt?',
                           'Er wird vervierfacht: aus 9x² wird 36x².',
                           ['Er wird verdoppelt: aus 9x² wird 18x².', 'Er wird verdoppelt: aus 9x wird 18x.', 'Er bleibt gleich, nur die Form ändert sich.'],
                           'Vorher 3x · 3x = 9x². Nachher 6x · 6x = 36x², das ist 4 · 9x². Beide Seiten verdoppeln heißt Fläche mal 4.',
                           'Rechne die Fläche vorher und nachher als Term aus und vergleiche.'))
# minusklammer
DS.stufe('minusklammer', 'Welche Umformung von 12x − (2x − 4) ist richtig?', 1)
DS.stufe('minusklammer', 'Welche Umformung von 10x − (1x − 6) ist richtig?', 1)
DS.stufe('minusklammer', 'Löse die Klammer auf: −4(7x + 1)', 2)
DS.stufe('minusklammer', 'Löse die Klammer auf: −5(4x + 2)', 2)
DS.neu('minusklammer', 3, DS.A('Jemand rechnet: 7x − (3x − 5) = 4x − 5. Was stimmt?', 'Falsch: Auch −5 wechselt das Vorzeichen, richtig ist 4x + 5.',
                               ['Richtig: 7x − 3x = 4x.', 'Falsch: Richtig ist 10x − 5.', 'Falsch: Richtig ist 4x − 5x.'],
                               '7x − (3x − 5) = 7x − 3x + 5 = 4x + 5. Der Fehler: Nur das erste Vorzeichen wurde gewechselt.',
                               'Wechselt jedes Vorzeichen in der Klammer?'))
DS.neu('minusklammer', 3, DS.L('Vereinfache: 3x − (2x − (x − 4))', '□x + □', [2, -4], ['3 - 1', '-4'],
                               'Innen zuerst: 2x − (x − 4) = 2x − x + 4 = x + 4. Dann 3x − (x + 4) = 3x − x − 4 = 2x − 4.',
                               'Löse zuerst die innere Klammer auf.', 'Tippe den ganzen Term ein, z. B. 3x − 4.'))
DS.neu('minusklammer', 3, DS.L('In der Klassenkasse sind 5x €. Ausgegeben werden (x + 12) € für Bastelzeug und (2x − 3) € für Getränke. Wie viel bleibt übrig?', '□x + □', [2, -9],
                               ['5 - 1 - 2', '-12 + 3'], '5x − (x + 12) − (2x − 3) = 5x − x − 12 − 2x + 3 = 2x − 9 (in €).',
                               'Beide Ausgaben werden abgezogen – jede als ganze Klammer.', 'Tippe den ganzen Term ein, z. B. 3x − 4.'))
DS.neu('minusklammer', 3, DS.Z('Welche Zahl muss in die Lücke, damit 6x − (2x − □) für jedes x denselben Wert hat wie 4x + 7?', 7, '7',
                               '6x − (2x − □) = 6x − 2x + □ = 4x + □. Damit das 4x + 7 ist, muss □ = 7 sein.',
                               'Löse die Klammer auf: Welches Vorzeichen bekommt die Zahl in der Lücke?'))
# ausmultiplizieren
DS.stufe('ausmultiplizieren', 'Für 9 Geschenke kauft jemand je ein Buch für x € und eine Karte für 1 €. Die Kosten sind 9(x + 1). Multipliziere aus.', 1)
for _t in ['Vereinfache: 2(x + 6) − 4(x + 5)', 'Vereinfache: 5(x − 2) − 6(x − 3)', 'Vereinfache: 2(x + 2) − 6(x − 3)']:
    DS.stufe('ausmultiplizieren', _t, 2)
DS.neu('ausmultiplizieren', 3, DS.Z('Ein Rechteck ist x cm lang und 4 cm breit. Die Länge wird um 3 cm vergrößert. Um wie viel cm² wächst die Fläche – egal wie groß x ist?', 12, '4 * 3',
                                    'Neue Fläche 4(x + 3) = 4x + 12, alte Fläche 4x. Unterschied: 12 cm², für jedes x.',
                                    'Stelle die neue Fläche als Term auf, multipliziere aus und vergleiche mit 4x.', einheit='cm²'))
DS.neu('ausmultiplizieren', 3, DS.Z('Welche Zahl steht vor der Klammer? □ · (2x − 5) = −6x + 15', -3, '-6 / 2',
                                    '□ · 2x = −6x, also □ = −3. Probe: (−3) · (−5) = +15 ✓.', 'Rückwärts: Welche Zahl mal 2 ergibt −6? Prüfe mit dem zweiten Glied.'))
DS.neu('ausmultiplizieren', 3, DS.A('Jemand rechnet: −3(2x − 4) = −6x − 12. Was stimmt?', 'Falsch: (−3) · (−4) = +12, richtig ist −6x + 12.',
                                    ['Richtig.', 'Falsch: Richtig ist −6x − 4.', 'Falsch: Richtig ist 6x + 12.'],
                                    '(−3) · 2x = −6x und (−3) · (−4) = +12. Minus mal minus ergibt plus.', 'Prüfe das Vorzeichen beim zweiten Glied.'))
DS.neu('ausmultiplizieren', 3, DS.Z('Für welche Zahl a hat der Term a(x + 2) − 3x für jedes x den Wert 6?', 3, '6 / 2',
                                    'a(x + 2) − 3x = ax + 2a − 3x. Das x muss wegfallen: a = 3. Dann bleibt 2 · 3 = 6 ✓.',
                                    'Multipliziere aus. Wann fällt x ganz weg?'))
# summe_mal_summe
for _t in ['Ein quadratischer Garten mit Seite x m wird 2 m länger und 5 m breiter. Gib die neue Fläche (x + 2)(x + 5) ohne Klammern an.',
           'Ein quadratischer Garten mit Seite x m wird 6 m länger und 1 m breiter. Gib die neue Fläche (x + 6)(x + 1) ohne Klammern an.',
           'Ein quadratischer Garten mit Seite x m wird 2 m länger und 2 m breiter. Gib die neue Fläche (x + 2)(x + 2) ohne Klammern an.']:
    DS.stufe('summe_mal_summe', _t, 2)
DS.neu('summe_mal_summe', 3, DS.L('Ein quadratischer Garten mit Seite x m wird 4 m länger und 3 m schmaler. Gib die Änderung der Fläche (x + 4)(x − 3) − x² als Term an.',
                                  '□x + □', [1, -12], ['4 - 3', '4 * (-3)'],
                                  '(x + 4)(x − 3) = x² − 3x + 4x − 12 = x² + x − 12. Minus x²: x − 12. Die Fläche wächst nur, wenn x größer als 12 ist.',
                                  'Erst ausmultiplizieren, dann x² abziehen.', 'Tippe den ganzen Term ein, z. B. 3x − 4.'))
DS.neu('summe_mal_summe', 3, DS.Z('Welche Zahl fehlt? (x + □)(x + 3) = x² + 8x + 15', 5, '15 / 3',
                                  '□ · 3 = 15, also □ = 5. Probe Mittelglied: 3x + 5x = 8x ✓.', 'Rückwärts: Das letzte Glied entsteht aus □ · 3.'))
DS.neu('summe_mal_summe', 3, DS.Z('Wie viele Produkte entstehen beim Ausmultiplizieren von (a + b + 2)(a − 3), bevor man zusammenfasst?', 6, '3 * 2',
                                  'Jedes der 3 Glieder der ersten Klammer mal jedes der 2 Glieder der zweiten: 3 · 2 = 6 Produkte.',
                                  'Jedes Glied mal jedes Glied – zähle die Glieder in beiden Klammern.'))
# ausklammern
DS.stufe('ausklammern', 'Klammere den größten gemeinsamen Faktor aus: 4x² + 2x', 2)
DS.ersetze('ausklammern', 'Jemand klammert aus: 12x + 20 = 2(6x + 10). Was stimmt?',
           DS.L('Klammere den größten gemeinsamen Faktor aus: 6ab − 9b', '□b(□a + □)', [3, 2, -3], ['3', '6 / 3', '-9 / 3'],
                'In beiden Gliedern stecken 3 und b: 6ab − 9b = 3b(2a − 3).', 'Welche Zahl und welcher Buchstabe stecken in beiden Gliedern?', _HK))
DS.ersetze('ausklammern', 'Jemand klammert aus: 30x + 10 = 2(15x + 5). Was stimmt?',
           DS.L('Klammere −4 aus: −8x + 12', '−4(□x + □)', [2, -3], ['-8 / (-4)', '12 / (-4)'],
                '−8x : (−4) = 2x und 12 : (−4) = −3. Also −4(2x − 3). Probe: −4 · 2x = −8x, −4 · (−3) = +12 ✓.',
                'Teile jedes Glied durch −4. Achte auf die Vorzeichen.', 'Tippe den ganzen Term mit Klammer ein, z. B. −4(3x + 1).'))
DS.neu('ausklammern', 3, DS.L('Ein Rechteck hat den Flächeninhalt 6x² + 15x und die Breite 3x. Wie lang ist es?', '□x + □', [2, 5], ['6 / 3', '15 / 3'],
                              '6x² + 15x = 3x(2x + 5). Breite 3x, also Länge 2x + 5.', 'Klammere die Breite 3x aus. Was bleibt in der Klammer?',
                              'Tippe den ganzen Term ein, z. B. 3x − 4.'))
# aequivalenz
DS.stufe('aequivalenz', 'Welcher Term ist äquivalent zu 4(x + 9)?', 1)
DS.stufe('aequivalenz', 'Welcher Term ist äquivalent zu 7(x + 4)?', 1)
DS.stufe('aequivalenz', 'Setze x = 4 in 3(x + 2) und in 3x + 2 ein. Um wie viel ist der erste Wert größer?', 2)
DS.neu('aequivalenz', 1, DS.L('Setze x = 0 in 3(x + 4) und in 3x + 4 ein. Welche Werte ergeben sich?', '3(x + 4): □; 3x + 4: □', [12, 4], ['3 * 4', '4'],
                              '3 · (0 + 4) = 12 und 3 · 0 + 4 = 4. Verschiedene Werte: x = 0 ist ein Gegenbeispiel, die Terme sind nicht äquivalent.',
                              'Erst die Klammer ausrechnen, dann malnehmen.', _HZ))
DS.neu('aequivalenz', 2, DS.A('Welche beiden Terme sind äquivalent? A: 2(x − 3) + x   B: 3x − 6   C: 3(x − 3)', 'A und B', ['A und C', 'B und C', 'alle drei'],
                              'A: 2x − 6 + x = 3x − 6, das ist B. C: 3x − 9 ist anders (für x = 0: −6 gegen −9).', 'Forme A und C um und vergleiche mit B.'))
DS.neu('aequivalenz', 2, DS.A('x² und 2x sind nicht äquivalent. Welche Zahl ist ein Gegenbeispiel?', '3', ['0', '2'],
                              'Für 3: 3² = 9, aber 2 · 3 = 6 – verschieden. Für 0 (0 und 0) und 2 (4 und 4) passen beide zufällig.',
                              'Setze jede Zahl in beide Terme ein. Ein Gegenbeispiel liefert verschiedene Werte.'))
DS.ersetze('aequivalenz', 'Sind (x + 3)² und x² + 9 äquivalent?',
           DS.A('Lisa sagt: „x + x + x und x · x · x sind äquivalent, denn für x = 0 ergeben beide 0.“ Was stimmt?', 'Falsch: Für x = 2 ergibt sich 6 und 8.',
                ['Richtig: Ein passendes Beispiel genügt.', 'Richtig: Beide haben dreimal x.', 'Falsch: Für x = 0 ergibt sich 0 und 3.'],
                'Ein passendes Beispiel beweist nichts. Für x = 2: 2 + 2 + 2 = 6, aber 2 · 2 · 2 = 8. Das Gegenbeispiel zeigt: nicht äquivalent.',
                'Ein Beispiel reicht für „nicht äquivalent“, aber nie für „äquivalent“. Probiere eine andere Zahl.'))
DS.neu('aequivalenz', 3, DS.Z('Für welche Zahl a ist der Term 3(x + a) äquivalent zu 3x + 12?', 4, '12 / 3',
                              '3(x + a) = 3x + 3a. Äquivalent zu 3x + 12 heißt 3a = 12, also a = 4.', 'Multipliziere 3(x + a) aus und vergleiche Glied für Glied.'))
# binomisch
DS.ersetze('binomisch', 'Ergänze so, dass eine binomische Formel entsteht: x² + 14x + □ = (x + □)²',
           DS.L('Ergänze so, dass eine binomische Formel entsteht: (□x − 3)² = 4x² − □x + 9', '(□x − 3)² = 4x² − □x + 9', [2, 12], ['2', '2 * 2 * 3'],
                '4x² = (2x)², also steht 2 vorne. Mittelglied: 2 · 2x · 3 = 12x. (2x − 3)² = 4x² − 12x + 9.',
                'Welcher Term ergibt quadriert 4x²? Das Mittelglied ist 2 · a · b.', _HZ))
DS.neu('binomisch', 3, DS.Z('Rechne geschickt mit einer binomischen Formel: 49 · 51', 2499, '50 * 50 - 1',
                            '49 · 51 = (50 − 1)(50 + 1) = 50² − 1² = 2500 − 1 = 2499 (3. binomische Formel).',
                            'Schreibe 49 und 51 als 50 − 1 und 50 + 1.'))
# ---- DURCHSICHT ENDE ----


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
    durchsicht_datei(META['thema_schluessel'], DS)  # Neunzehnte Runde: zuletzt
