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


# ---- STUFEN (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, siehe _stufen_kl7.py) ----
# Vorbilder (Typ und Niveau, eigene Zahlen): BMT8 (ISB) 2019 B1b, 2024 A2, 2025 A4 („Vereinfache so weit wie möglich“), 2014 B7 (ausklammern ergänzen),
# 2023 A1 (äquivalente Terme ankreuzen); Knobel nach der Art von Känguru 7/8 und Mathematik-Olympiade (geschickt rechnen, Zauberquadrat, Vorzeichen).
from _stufen_kl7 import Stufen, stufen_datei  # noqa: E402

ST = Stufen('terme.umformen', 20_7_2)
_HT = 'Tippe den ganzen Term ein, z. B. 3x − 2y.'
_HZ = 'Trage in jedes Feld eine Zahl ein.'
# zusammenfassen
ST.leiter('zusammenfassen', 'Gleichartige Glieder mit x und y zusammenfassen.',
          'Terme mit x², Zahlen und mehreren Gliedern; Umfang als Term; fehlenden Summanden bestimmen.',
          'Fehler beim Zusammenfassen deuten, rückwärts den Term T finden, Seite aus dem Umfang, Potenzen unterscheiden, Parameter, Prüfungsaufgabe mit Produkten.')
ST.regel('zusammenfassen', 1, 'Fasse zusammen', 'direkt')
ST.regel('zusammenfassen', 1, 'gleichwertig', 'erkennen')
ST.regel('zusammenfassen', 2, 'Fasse zusammen', 'mehrschritt')
ST.regel('zusammenfassen', 2, 'Rechteck', 'einkleidung')
ST.regel('zusammenfassen', 3, 'Jemand rechnet', 'fehler')
ST.regel('zusammenfassen', 3, 'Wie heißt der Term T', 'rueckwaerts')
ST.regel('zusammenfassen', 3, 'Dreiecks', 'transfer')
ST.regel('zusammenfassen', 3, 'gleichartig', 'verknuepfen')
ST.regel('zusammenfassen', 3, 'genau', 'begruenden')
ST.neu('zusammenfassen', 2, 'umkehr', ST.L('Welcher Term ergibt zusammen mit 3x + 2y den Term 7x − y?', '□x + □y', [4, -3], ['7 - 3', '-1 - 2'],
                                           '7x − 3x = 4x und −y − 2y = −3y. Der Term ist 4x − 3y. Probe: 3x + 2y + 4x − 3y = 7x − y ✓.',
                                           'Was fehlt bei den x-Gliedern, was bei den y-Gliedern?', _HT))
ST.neu('zusammenfassen', 3, 'parameter', ST.Z('Für welche Zahl k ergibt kx + 3y − 2x + y zusammengefasst 5x + 4y?', 7, '5 + 2',
                                              'kx − 2x soll 5x sein, also k − 2 = 5 und k = 7. Die y-Glieder: 3y + y = 4y ✓.', 'Fasse die x-Glieder mit k zusammen.'))
ST.neu('zusammenfassen', 3, 'pruefung', ST.L('Vereinfache so weit wie möglich: 2a² + 3a − a · a + 4a', '□a² + □a', [1, 7], ['2 - 1', '3 + 4'],
                                             'a · a = a². Dann 2a² − a² = a² und 3a + 4a = 7a. Ergebnis: a² + 7a.', 'Rechne zuerst das Produkt a · a aus.', _HT))
ST.neu('zusammenfassen', 3, 'fehler', ST.A('Jemand fasst 5x² + 3x zu 8x³ zusammen. Was stimmt?', 'Falsch: x² und x sind nicht gleichartig, 5x² + 3x bleibt stehen.',
                                           ['Richtig: 5 + 3 = 8 und 2 + 1 = 3.', 'Falsch: Richtig ist 8x².', 'Falsch: Richtig ist 15x³.'],
                                           'Zusammenfassen darf man nur Glieder mit genau demselben Buchstabenteil. x² und x sind verschieden – der Term lässt sich nicht kürzer schreiben.',
                                           'Sind x² und x gleichartig?'))
ST.knobel('zusammenfassen', ST.L('Zehn Terme: a, a + 3, a + 6, a + 9, …, a + 27 (jeder 3 mehr als der vorige). Fasse die Summe aller zehn Terme zusammen.', '□a + □', [10, 135],
                                 ['10', '3 * (0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)'],
                                 'Zehnmal a ergibt 10a. Die Zahlen sind 0, 3, 6, 9, 12, 15, 18, 21, 24 und 27. '
                                 'Paare von vorne und hinten: 0 + 27, 3 + 24, 6 + 21, 9 + 18, 12 + 15 – fünf Paare mit je 27, zusammen 5 · 27 = 135. Ergebnis 10a + 135.',
                                 'Zähle die a getrennt. Für die Zahlen: Bilde Paare von vorne und hinten.', _HT))
ST.knobel('zusammenfassen', ST.L('In einem Zauberquadrat aus 3 × 3 Feldern ergeben alle Zeilen, Spalten und beide Diagonalen dieselbe Summe. Im mittleren Feld steht x + 2. Wie groß ist diese Summe?',
                                 '□x + □', [3, 6], ['3', '3 * 2'],
                                 'Nenne die gesuchte Summe S. Die mittlere Zeile, die mittlere Spalte und die beiden Diagonalen gehen durch die Mitte; zusammen ergeben sie 4S. '
                                 'In diesen vier Linien kommt jedes Feld genau einmal vor, nur das Mittelfeld viermal, also dreimal zu viel. Alle neun Felder zusammen sind die drei Zeilen, also 3S. '
                                 'Damit 4S = 3S + 3 · Mitte, und es bleibt S = 3 · Mitte = 3 · (x + 2) = 3x + 6.',
                                 'Addiere die vier Linien durch die Mitte. Wie oft kommt jedes Feld darin vor?', _HT))
# produkte
ST.leiter('produkte', 'Zwei Faktoren mit Zahl und Variable malnehmen (2x · 5y).',
          'Vorzeichen bei mehreren Faktoren, gleiche Variablen werden zum Quadrat, Fläche als Term, fehlende Seite.',
          'Fehler x statt x², Volumen mit a³, fehlenden Faktor rückwärts, Vorzeichen bei drei Minus, Verdopplung der Seiten, Parameter, Prüfungsaufgabe.')
ST.regel('produkte', 1, 'Vereinfache', 'direkt')
ST.regel('produkte', 2, 'Vereinfache', 'mehrschritt')
ST.regel('produkte', 2, 'Rechteck', 'einkleidung')
ST.regel('produkte', 3, 'Jemand rechnet', 'fehler')
ST.regel('produkte', 3, 'Quader', 'verknuepfen')
ST.regel('produkte', 3, 'Welcher Faktor fehlt', 'rueckwaerts')
ST.regel('produkte', 3, '(−c)', 'begruenden')
ST.regel('produkte', 3, 'verdoppelt', 'begruenden')
ST.neu('produkte', 1, 'erkennen', ST.A('Welcher Term ist gleich 4 · a · a?', '4a²', ['8a', '4a', '(4a)²'],
                                       'a · a = a², also 4 · a · a = 4a². (4a)² wäre 4a · 4a = 16a².', 'Wie schreibt man a · a kürzer?'))
ST.neu('produkte', 2, 'umkehr', ST.L('Ein Rechteck hat den Flächeninhalt 12x² und die Länge 4x. Wie breit ist es?', '□x', [3], ['12 / 4'],
                                     '4x · 3x = 12x². Die Breite ist 3x.', 'Welcher Term mal 4x ergibt 12x²?', 'Tippe den Term ein, z. B. 5x.'))
ST.neu('produkte', 3, 'transfer', ST.Z('Bei einem Quadrat mit der Seite s wird eine Seite verdreifacht und die andere halbiert. Mit welcher Zahl wird der Flächeninhalt malgenommen?', 1.5, '3 * 0.5',
                                       'Neue Fläche: 3s · 0,5s = 1,5s². Vorher s². Die Fläche wird mit 1,5 malgenommen.', 'Schreibe die neue Fläche als Produkt und vergleiche mit s².'))
ST.neu('produkte', 3, 'pruefung', ST.L('Vereinfache so weit wie möglich: (3x)² − 2x · 4x', '□x²', [1], ['9 - 8'],
                                       '(3x)² = 3x · 3x = 9x². 2x · 4x = 8x². 9x² − 8x² = x².', 'Rechne beide Produkte einzeln aus.', 'Tippe den Term ein, z. B. 5x².'))
ST.neu('produkte', 3, 'parameter', ST.Z('Für welche Zahl n gilt 2a · na = 10a²?', 5, '10 / 2', '2a · na = 2n · a². Das soll 10a² sein: 2n = 10, n = 5.', 'Multipliziere die Zahlen und die Variablen getrennt.'))
ST.knobel('produkte', ST.Z('Ein großer Würfel hat die Kantenlänge 3a, kleine Würfel haben die Kantenlänge a. Wie viele kleine Würfel passen genau in den großen?', 27, '3 * 3 * 3',
                           'Volumen groß: (3a)³ = 3a · 3a · 3a = 27a³. Volumen klein: a³. In jede Richtung passen 3 kleine Würfel: 3 · 3 · 3 = 27.',
                           'Wie viele kleine Würfel passen entlang einer Kante?'))
ST.knobel('produkte', ST.A('Welches Vorzeichen hat (−a) · (−a)² · (−a)³ für eine positive Zahl a?', 'plus', ['minus', 'Das hängt davon ab, wie groß a ist.'],
                           '(−a)² = a² ist positiv, (−a)³ = −a³ ist negativ. (−a) · a² · (−a³) = (−1) · (−1) · a⁶ = a⁶: zwei Minuszeichen, also plus. '
                           'Kurz: Insgesamt wird −a sechsmal mit sich malgenommen – eine gerade Anzahl.',
                           'Zähle, wie oft der Faktor (−a) insgesamt vorkommt.'))
# minusklammer
ST.leiter('minusklammer', 'Eine Minusklammer auflösen und zusammenfassen; richtige Umformung erkennen.',
          'Zwei Klammern, Minus vor einem Faktor, Sachsituation Konto, fehlenden Term in der Klammer finden.',
          'Fehler deuten, verschachtelte Klammern, Ausgaben einer Kasse, Lücke rückwärts, Gegenbeispiel zu a − (b − c), Seite aus dem Umfang, Prüfungsaufgabe.')
ST.regel('minusklammer', 1, 'Löse die Klammer auf und fasse zusammen', 'direkt')
ST.regel('minusklammer', 1, 'Welche Umformung', 'erkennen')
ST.regel('minusklammer', 2, 'Löse die Klammer', 'mehrschritt')
ST.regel('minusklammer', 3, 'Jemand rechnet', 'fehler')
ST.regel('minusklammer', 3, '(2x − (x', 'transfer')
ST.regel('minusklammer', 3, 'Klassenkasse', 'transfer')
ST.regel('minusklammer', 3, 'Lücke', 'parameter')
ST.neu('minusklammer', 2, 'einkleidung', ST.L('Auf einem Konto sind 8x €. Abgebucht werden (3x − 5) €. Wie viel bleibt auf dem Konto?', '□x + □', [5, 5], ['8 - 3', '5'],
                                              '8x − (3x − 5) = 8x − 3x + 5 = 5x + 5 (in €).', 'Die ganze Abbuchung wird abgezogen.', _HT))
ST.neu('minusklammer', 2, 'umkehr', ST.L('Welcher Term gehört in die Klammer? 7x − ( ? ) = 4x + 2', '□x + □', [3, -2], ['7 - 4', '-2'],
                                         '7x − (3x − 2) = 7x − 3x + 2 = 4x + 2 ✓.', 'Was muss abgezogen werden, damit aus 7x der Term 4x wird? Achte auf das Vorzeichen der Zahl.', _HT))
ST.neu('minusklammer', 3, 'begruenden', ST.A('Stimmt für alle Zahlen: a − (b − c) = a − b − c?', 'Nein: Für a = 5, b = 3, c = 1 ergibt links 3, rechts 1.',
                                             ['Ja: Man lässt die Klammer einfach weg.', 'Ja, aber nur für positive Zahlen.', 'Nein: Richtig ist a − b − c = a + b − c.'],
                                             'Minus vor der Klammer dreht jedes Vorzeichen: a − (b − c) = a − b + c. Das Gegenbeispiel zeigt es: 5 − (3 − 1) = 3, aber 5 − 3 − 1 = 1.',
                                             'Probiere es mit kleinen Zahlen aus.'))
ST.neu('minusklammer', 3, 'rueckwaerts', ST.Z('Aus 9x − (□x + 4) entsteht nach dem Auflösen und Zusammenfassen 2x − 4. Welche Zahl steht im Kästchen?', 7, '9 - 2',
                                              '9x − □x − 4 = 2x − 4. Also 9 − □ = 2 und □ = 7.', 'Löse die Klammer mit dem Kästchen auf und vergleiche die x-Glieder.'))
ST.neu('minusklammer', 3, 'pruefung', ST.L('Vereinfache so weit wie möglich: (5x − 3) − (2x − 7) − x', '□x + □', [2, 4], ['5 - 2 - 1', '-3 + 7'],
                                           '5x − 3 − 2x + 7 − x = 2x + 4.', 'Löse beide Klammern auf, dann zusammenfassen.', _HT))
ST.neu('minusklammer', 3, 'verknuepfen', ST.L('Ein Dreieck hat den Umfang 10x + 4. Zwei Seiten sind (3x + 1) und (2x − 2) lang. Wie lang ist die dritte Seite?', '□x + □', [5, 5],
                                              ['10 - 3 - 2', '4 - 1 + 2'], '10x + 4 − (3x + 1) − (2x − 2) = 10x + 4 − 3x − 1 − 2x + 2 = 5x + 5.',
                                              'Umfang minus die beiden bekannten Seiten – jede als ganze Klammer.', _HT))
ST.knobel('minusklammer', ST.Z('Berechne geschickt: 1 − 2 + 3 − 4 + 5 − 6 + … + 99 − 100', -50, '50 * (-1)',
                               'Fasse je zwei Nachbarzahlen zusammen: 1 − 2 = −1, 3 − 4 = −1, 5 − 6 = −1 und so weiter bis 99 − 100 = −1. Die 100 Zahlen bilden 50 solche Paare, jedes ergibt −1. Ergebnis 50 · (−1) = −50.',
                               'Bilde Paare aus Nachbarzahlen.'))
ST.knobel('minusklammer', ST.Z('Setze in 10 − 9 − 8 − 7 genau ein Klammerpaar so, dass das Ergebnis möglichst groß wird. Wie groß ist es?', 16, '10 - (9 - 8 - 7)',
                               'Ohne Klammer: −14. Eine Klammer hinter dem ersten Minus dreht alle Vorzeichen darin: 10 − (9 − 8 − 7) = 10 − 9 + 8 + 7 = 16. '
                               'Andere Möglichkeiten: 10 − (9 − 8) − 7 = 2, 10 − 9 − (8 − 7) = 0. Am größten: 16.',
                               'Ein Minus vor der Klammer dreht die Vorzeichen in der Klammer. Welche Zahlen sollen plus werden?'))
# ausmultiplizieren
ST.leiter('ausmultiplizieren', 'Eine Zahl vor der Klammer mit jedem Glied malnehmen.',
          'x vor der Klammer, negative Faktoren, zwei Klammern vereinfachen, Fläche als Term, Faktoren ergänzen.',
          'Zuwachs unabhängig von x, Faktor rückwärts, Fehler mit Vorzeichen und x · 4, Parameter a, Gegenbeispiel zu 2(ab), geschickt rechnen, Prüfungsaufgabe.')
ST.regel('ausmultiplizieren', 1, 'Multipliziere aus', 'direkt')
ST.regel('ausmultiplizieren', 2, 'Multipliziere aus', 'mehrschritt')
ST.regel('ausmultiplizieren', 2, 'Vereinfache', 'mehrschritt')
ST.regel('ausmultiplizieren', 3, 'Rechteck', 'transfer')
ST.regel('ausmultiplizieren', 3, 'Welche Zahl steht vor der Klammer', 'rueckwaerts')
ST.regel('ausmultiplizieren', 3, 'Jemand rechnet', 'fehler')
ST.regel('ausmultiplizieren', 3, 'Für welche Zahl a', 'parameter')
ST.neu('ausmultiplizieren', 1, 'erkennen', ST.A('Welcher Term entsteht, wenn man 5(x + 3) ausmultipliziert?', '5x + 15', ['5x + 3', 'x + 15', '5x + 8'],
                                                '5 · x = 5x und 5 · 3 = 15. Die 5 kommt zu jedem Glied.', 'Wird die 3 auch malgenommen?'))
ST.neu('ausmultiplizieren', 2, 'einkleidung', ST.L('Ein Rechteck ist x cm breit und 3 cm länger als breit. Gib seinen Flächeninhalt ohne Klammer an.', '□x² + □x', [1, 3], ['1', '3'],
                                                   'Länge x + 3, Fläche x · (x + 3) = x² + 3x.', 'Schreibe zuerst die Länge als Term.', 'Tippe den Term ein, z. B. 2x² + 5x.'))
ST.neu('ausmultiplizieren', 2, 'umkehr', ST.L('Ergänze: 4(□x + □) = 12x + 8', '4(□x + □)', [3, 2], ['12 / 4', '8 / 4'],
                                              '4 · 3x = 12x und 4 · 2 = 8.', 'Welche Zahlen ergeben mal 4 genau 12 und 8?', _HZ))
ST.neu('ausmultiplizieren', 3, 'begruenden', ST.A('Stimmt für alle Zahlen: 2 · (a · b) = 2a · 2b?', 'Nein: Für a = b = 1 ist links 2, rechts 4.',
                                                  ['Ja: Die 2 kommt zu jedem Faktor.', 'Ja, das ist das Ausmultiplizieren.', 'Nein: Richtig ist 2 · (a · b) = 2a + 2b.'],
                                                  'Ausmultiplizieren gilt nur bei Summen. Bei einem Produkt verdoppelt man nur einen Faktor: 2 · (a · b) = 2ab. Gegenbeispiel a = b = 1: 2 ≠ 4.',
                                                  'Setze kleine Zahlen ein.'))
ST.neu('ausmultiplizieren', 3, 'verknuepfen', ST.Z('Berechne geschickt mit Ausmultiplizieren: 7 · 103', 721, '7 * 100 + 7 * 3',
                                                   '7 · 103 = 7 · (100 + 3) = 700 + 21 = 721.', 'Schreibe 103 als Summe.'))
ST.neu('ausmultiplizieren', 3, 'pruefung', ST.L('Multipliziere aus und vereinfache so weit wie möglich: 3(2x − 1) − 2(x − 4)', '□x + □', [4, 5], ['6 - 2', '-3 + 8'],
                                                '6x − 3 − 2x + 8 = 4x + 5.', 'Achte beim zweiten Teil auf −2 · (−4).', _HT))
ST.neu('ausmultiplizieren', 3, 'fehler', ST.A('Jemand rechnet: x(x + 4) = x² + 4. Was stimmt?', 'Falsch: x · 4 = 4x fehlt, richtig ist x² + 4x.',
                                              ['Richtig gerechnet.', 'Falsch: Richtig ist 2x + 4.', 'Falsch: Richtig ist x² + 4x².'],
                                              'Das x vor der Klammer kommt zu jedem Glied: x · x = x² und x · 4 = 4x.', 'Wurde das zweite Glied auch mit x malgenommen?'))
ST.knobel('ausmultiplizieren', ST.Z('Wie viele Glieder hat 2(a + b + c) + 3(b + c + d) − 5(c + d + e) nach dem Ausmultiplizieren und Zusammenfassen?', 4, '4',
                                    'Ausmultipliziert: 2a + 2b + 2c + 3b + 3c + 3d − 5c − 5d − 5e. Zusammengefasst: 2a + 5b + 0c − 2d − 5e. '
                                    'Das c fällt weg (2 + 3 − 5 = 0). Es bleiben 4 Glieder: 2a + 5b − 2d − 5e.',
                                    'Zähle für jeden Buchstaben, wie oft er insgesamt vorkommt – mit Vorzeichen.'))
ST.knobel('ausmultiplizieren', ST.Z('Rechnet man 3(x + 4) − 2(x + 5) − x aus, kommt für jedes x dieselbe Zahl heraus. Welche?', 2, '12 - 10',
                                    '3x + 12 − 2x − 10 − x = (3 − 2 − 1)x + 2 = 2. Das x fällt ganz weg – für jede Zahl x ergibt sich 2.',
                                    'Multipliziere aus und sammle die x-Glieder.'))
# summe_mal_summe
ST.leiter('summe_mal_summe', '(x + a)(x + b) ausmultiplizieren; die Anzahl der Produkte kennen.',
          'Minuszeichen und Faktoren vor x, Garten als Sachsituation, Rechteck aus vier Teilflächen als Produkt schreiben.',
          'Fehlende Glieder deuten, Flächenänderung, Zahl rückwärts, Parameter k, geschickt rechnen 21 · 19, Prüfungsaufgabe, Rechnung beurteilen.')
ST.regel('summe_mal_summe', 1, 'Multipliziere aus', 'direkt')
ST.regel('summe_mal_summe', 2, 'Multipliziere aus', 'mehrschritt')
ST.regel('summe_mal_summe', 2, 'Garten', 'einkleidung')
ST.regel('summe_mal_summe', 3, 'Jemand rechnet', 'fehler')
ST.regel('summe_mal_summe', 3, 'Garten', 'transfer')
ST.regel('summe_mal_summe', 3, 'Welche Zahl fehlt', 'rueckwaerts')
ST.regel('summe_mal_summe', 3, 'Wie viele Produkte', 'begruenden')
ST.neu('summe_mal_summe', 1, 'erkennen', ST.Z('Wie viele Produkte bildet man beim Ausmultiplizieren von (x + 2)(x + 5), bevor man zusammenfasst?', 4, '2 * 2',
                                              'Jedes der 2 Glieder der ersten Klammer mal jedes der 2 Glieder der zweiten: 2 · 2 = 4 Produkte.', 'Jedes Glied mal jedes Glied.'))
ST.neu('summe_mal_summe', 1, 'direkt', ST.L('Multipliziere aus: (a + 2)(b + 3)', '□ab + □a + □b + □', [1, 3, 2, 6], ['1', '3', '2', '2 * 3'],
                                            'a · b + a · 3 + 2 · b + 2 · 3 = ab + 3a + 2b + 6. Hier lässt sich nichts zusammenfassen.', 'Jedes Glied der ersten Klammer mal jedes der zweiten.',
                                            'Tippe den ganzen Term ein, z. B. ab + 2a + 3b + 6.'))
ST.neu('summe_mal_summe', 2, 'darstellung', ST.A('Ein Rechteck ist in vier Teile zerlegt: x², 5x, 2x und 10. Welches Produkt beschreibt die ganze Fläche?', '(x + 2)(x + 5)',
                                                 ['(x + 5)(x + 10)', '(x + 2)(x + 10)', '(x + 7)(x + 10)'],
                                                 'Die Teile x · x, x · 5, 2 · x und 2 · 5 ergeben die Seiten x + 2 und x + 5. Probe: (x + 2)(x + 5) = x² + 5x + 2x + 10 ✓.',
                                                 'Welche Seitenlängen ergeben die Teilflächen 5x und 10?'))
ST.neu('summe_mal_summe', 3, 'parameter', ST.Z('Für welche Zahl k gilt (x + k)(x + 2) = x² + 7x + 10 für jedes x?', 5, '10 / 2',
                                               '(x + k)(x + 2) = x² + (k + 2)x + 2k. Also k + 2 = 7 und 2k = 10: k = 5.', 'Multipliziere mit k aus und vergleiche die Glieder.'))
ST.neu('summe_mal_summe', 3, 'pruefung', ST.Z('Vereinfache so weit wie möglich: (x + 4)(x − 2) − x(x + 2)', -8, '4 * (-2)',
                                              '(x + 4)(x − 2) = x² + 2x − 8. x(x + 2) = x² + 2x. Differenz: −8.', 'Multipliziere beide Teile aus; Minus vor dem zweiten.'))
ST.neu('summe_mal_summe', 3, 'verknuepfen', ST.Z('Berechne geschickt: 21 · 19 = (20 + 1)(20 − 1)', 399, '20 * 20 - 1',
                                                 '(20 + 1)(20 − 1) = 400 − 20 + 20 − 1 = 399.', 'Multipliziere die Klammern aus. Zwei Glieder heben sich weg.'))
ST.neu('summe_mal_summe', 3, 'begruenden', ST.A('Jemand rechnet: (2x + 1)(x + 3) = 2x² + 6x + x + 3 = 2x² + 7x + 3. Was stimmt?', 'Die Rechnung ist richtig.',
                                                ['Falsch: Es fehlt das Glied 3x.', 'Falsch: Richtig ist 2x² + 3.', 'Falsch: Richtig ist 3x² + 7x + 3.'],
                                                'Vier Produkte: 2x · x = 2x², 2x · 3 = 6x, 1 · x = x, 1 · 3 = 3. Zusammengefasst 2x² + 7x + 3 – alles richtig.',
                                                'Prüfe jedes der vier Produkte einzeln.'))
ST.knobel('summe_mal_summe', ST.Z('Berechne ohne Taschenrechner: 47 · 49 + 1', 2304, '48 * 48',
                                  'Mit n = 48: (n − 1)(n + 1) + 1 = n² − 1 + 1 = n². Also 47 · 49 + 1 = 48² = 2 304.',
                                  'Beide Zahlen liegen gleich weit neben einer runden Mitte. Schreibe sie mit dieser Mitte.'))
ST.knobel('summe_mal_summe', ST.Z('Ein Rechteck hat die Seiten (x + 3) und (x + 7), ein Quadrat die Seite (x + 5). Um wie viel ist die Fläche des Quadrats größer – für jedes x?', 4, '25 - 21',
                                  'Quadrat: (x + 5)(x + 5) = x² + 10x + 25. Rechteck: (x + 3)(x + 7) = x² + 10x + 21. Unterschied: 4 – egal wie groß x ist.',
                                  'Multipliziere beide aus und vergleiche Glied für Glied.'))
# ausklammern
ST.leiter('ausklammern', 'Den größten gemeinsamen Zahlfaktor ausklammern.',
          'Zahl und x ausklammern, fehlenden Faktor ergänzen, Länge aus Fläche und Breite.',
          'Unvollständiges Ausklammern beurteilen, zwei Variablen, negative Faktoren, Länge rückwärts, Parameter, geschickt rechnen, Prüfungsaufgabe (Lücken).')
ST.regel('ausklammern', 1, 'Klammere den größten gemeinsamen Faktor aus', 'direkt')
ST.regel('ausklammern', 2, 'Klammere den größten gemeinsamen Faktor aus', 'mehrschritt')
ST.regel('ausklammern', 3, 'Jemand klammert aus', 'fehler')
ST.regel('ausklammern', 3, 'ab −', 'verknuepfen')
ST.regel('ausklammern', 3, 'Klammere −4', 'transfer')
ST.regel('ausklammern', 3, 'Rechteck', 'rueckwaerts')
ST.neu('ausklammern', 1, 'erkennen', ST.Z('Welches ist die größte Zahl, die sowohl in 6x als auch in 15 als Faktor steckt?', 3, '3', '6 = 3 · 2 und 15 = 3 · 5. Der größte gemeinsame Faktor ist 3.',
                                         'Suche die größte Zahl, die 6 und 15 teilt.'))
ST.neu('ausklammern', 1, 'direkt', ST.L('Klammere x aus: x² + 7x', 'x(□x + □)', [1, 7], ['1', '7'], 'x² = x · x und 7x = x · 7. Also x(x + 7).', 'In beiden Gliedern steckt x.',
                                        'Tippe den ganzen Term mit Klammer ein, z. B. x(x + 2).'))
ST.neu('ausklammern', 2, 'umkehr', ST.Z('Ergänze: □ · (2x + 5) = 6x + 15', 3, '6 / 2', '3 · 2x = 6x und 3 · 5 = 15.', 'Welche Zahl mal 2x ergibt 6x?'))
ST.neu('ausklammern', 2, 'einkleidung', ST.L('Ein Garten hat den Flächeninhalt (8x + 12) m² und ist 4 m breit. Wie lang ist er?', '□x + □', [2, 3], ['8 / 4', '12 / 4'],
                                             '8x + 12 = 4(2x + 3). Breite 4 m, also Länge (2x + 3) m.', 'Klammere die Breite 4 aus.', _HT))
ST.neu('ausklammern', 3, 'begruenden', ST.A('Ist 6x + 9 = 3(2x + 3) vollständig ausgeklammert?', 'Ja: 2x und 3 haben keinen gemeinsamen Faktor mehr.',
                                            ['Nein: Man kann noch 2 ausklammern.', 'Nein: Man muss 9 ausklammern.', 'Ja, aber nur, wenn x gerade ist.'],
                                            'Vollständig heißt: In der Klammer steckt kein gemeinsamer Faktor mehr. Die Zahlen 2 und 3 haben keinen gemeinsamen Faktor außer 1, und x kommt in 3 nicht vor. Also ist nichts mehr auszuklammern.',
                                            'Prüfe, ob die Glieder in der Klammer noch einen gemeinsamen Faktor haben.'))
ST.neu('ausklammern', 3, 'parameter', ST.Z('Für welche Zahl k gilt kx + 20 = 4(3x + 5)?', 12, '4 * 3', '4(3x + 5) = 12x + 20. Also k = 12.', 'Multipliziere die rechte Seite aus.'))
ST.neu('ausklammern', 3, 'pruefung', ST.L('Ergänze: 12a²b + 8ab² = □ab(3a + □b)', '□ab(3a + □b)', [4, 2], ['12 / 3', '8 / 4'],
                                          'In beiden Gliedern stecken 4, a und b: 12a²b = 4ab · 3a und 8ab² = 4ab · 2b.', 'Welche Zahl mal 3a ergibt 12a²b, wenn ab schon dasteht?', _HZ))
ST.neu('ausklammern', 3, 'verknuepfen', ST.Z('Berechne geschickt: 37 · 13 + 37 · 87', 3700, '37 * (13 + 87)', '37 · 13 + 37 · 87 = 37 · (13 + 87) = 37 · 100 = 3 700.',
                                             'Welcher Faktor kommt in beiden Produkten vor?'))
ST.knobel('ausklammern', ST.Z('Berechne ohne Taschenrechner: 2 024 · 2 023 − 2 023 · 2 022', 4046, '2023 * 2',
                              'Klammere 2 023 aus: 2 023 · (2 024 − 2 022) = 2 023 · 2 = 4 046.', 'Welcher Faktor steckt in beiden Produkten?'))
ST.knobel('ausklammern', ST.Z('Für welche natürliche Zahl n ergibt (n² + 5n) : (n + 5) genau 12?', 12, '12',
                              'n² + 5n = n(n + 5). Geteilt durch n + 5 bleibt n. Also n = 12. (Probe: 144 + 60 = 204, 204 : 17 = 12 ✓.)',
                              'Klammere in n² + 5n einen Faktor aus. Was bleibt nach dem Teilen durch n + 5 übrig?'))
# aequivalenz
ST.leiter('aequivalenz', 'Termwerte berechnen und einsetzen, um zu vergleichen; ausmultiplizierte Form erkennen.',
          'Zwei Terme mit einer Zahl vergleichen, äquivalente Paare finden, Gegenbeispiel wählen, Wertetabelle → Term, Sachsituation zweier Kassen.',
          'Fehlschluss aus einem Beispiel, Parameter, Term rückwärts, Zählweisen vergleichen, (−x)² und −x², Prüfungsaufgabe „nicht äquivalent“.')
ST.regel('aequivalenz', 1, 'Berechne den Wert', 'direkt')
ST.regel('aequivalenz', 1, 'Welcher Term ist äquivalent', 'erkennen')
ST.regel('aequivalenz', 1, 'Setze x', 'direkt')
ST.regel('aequivalenz', 2, 'Welcher Term ist äquivalent', 'erkennen', neu_s=1)
ST.regel('aequivalenz', 2, 'Um wie viel', 'mehrschritt')
ST.regel('aequivalenz', 2, 'Welche beiden Terme', 'mehrschritt')
ST.regel('aequivalenz', 2, 'Gegenbeispiel', 'umkehr')
ST.regel('aequivalenz', 3, 'Sind (x + ', 'begruenden')
ST.regel('aequivalenz', 3, 'Lisa', 'fehler')
ST.regel('aequivalenz', 3, 'x + x und x · x', 'begruenden')
ST.regel('aequivalenz', 3, 'Für welche Zahl a', 'parameter')
ST.neu('aequivalenz', 2, 'einkleidung', ST.A('Ein Heft kostet 2 €, ein Block 3 €. Für x Hefte und einen Block tippt Kasse A 2x + 3, Kasse B 2(x + 3) − 3. Rechnen beide Kassen immer gleich?',
                                             'Ja: 2(x + 3) − 3 = 2x + 6 − 3 = 2x + 3.',
                                             ['Nein: Kasse B rechnet 3 € zu viel.', 'Nein, nur bei x = 0.', 'Ja, aber nur, wenn x gerade ist.'],
                                             '2(x + 3) − 3 = 2x + 6 − 3 = 2x + 3. Die Terme sind äquivalent – beide Kassen rechnen immer gleich.',
                                             'Forme den Term von Kasse B um.'))
ST.neu('aequivalenz', 2, 'darstellung', ST.A('Ein Term hat die Werte: x = 0 → 3, x = 1 → 5, x = 2 → 7. Welcher Term passt dazu?', '2(x + 1) + 1',
                                             ['3x + 2', 'x + 3', '2x + 1'],
                                             '2(x + 1) + 1 = 2x + 3: für 0, 1, 2 ergibt das 3, 5, 7 ✓. 3x + 2 ergibt bei x = 0 nur 2, x + 3 bei x = 1 nur 4, 2x + 1 bei x = 0 nur 1.',
                                             'Setze die Werte aus der Tabelle in jeden Term ein.',
                                             grafik={'typ': 'tabelle', 'kopf': ['x', '0', '1', '2'], 'zeilen': [['Wert', '3', '5', '7']]}))
ST.neu('aequivalenz', 2, 'umkehr', ST.Z('2x + 1 und x + 2 sind nicht äquivalent. Für genau eine Zahl x haben sie trotzdem denselben Wert. Für welche?', 1, '2 - 1',
                                        'Für x = 1: 2 · 1 + 1 = 3 und 1 + 2 = 3. Für jede andere Zahl unterscheiden sie sich (der Unterschied ist x − 1).', 'Probiere kleine Zahlen.'))
ST.neu('aequivalenz', 3, 'rueckwaerts', ST.L('Ein Term T erfüllt T + (2x − 5) = 5x + 1 für jedes x. Wie heißt T?', '□x + □', [3, 6], ['5 - 2', '1 + 5'],
                                             'T = 5x + 1 − (2x − 5) = 5x + 1 − 2x + 5 = 3x + 6.', 'Ziehe (2x − 5) von 5x + 1 ab.', _HT))
ST.neu('aequivalenz', 3, 'transfer', ST.A('Um ein Quadrat aus n × n Plättchen liegt ein Rahmen. Anna zählt die Rahmen-Plättchen mit 4n + 4, Ben mit 4(n + 2) − 4. Was stimmt?',
                                          'Beide Terme sind äquivalent: 4(n + 2) − 4 = 4n + 4.',
                                          ['Nur Annas Term stimmt.', 'Nur Bens Term stimmt.', 'Die Terme sind verschieden, sie unterscheiden sich um 4.'],
                                          '4(n + 2) − 4 = 4n + 8 − 4 = 4n + 4. Ben zählt vier Seiten mit je n + 2 Plättchen und zieht die doppelt gezählten Ecken ab.',
                                          'Forme Bens Term um.'))
ST.neu('aequivalenz', 3, 'pruefung', ST.A('Welcher Term ist NICHT äquivalent zu 6x − 9?', '3(2x − 9)', ['3(2x − 3)', '−3(3 − 2x)', '6(x − 1,5)'],
                                          '3(2x − 9) = 6x − 27. Die anderen: 3(2x − 3) = 6x − 9, −3(3 − 2x) = −9 + 6x, 6(x − 1,5) = 6x − 9.',
                                          'Multipliziere jeden Term aus.'))
ST.neu('aequivalenz', 3, 'verknuepfen', ST.A('Sind (−x)² und −x² äquivalent?', 'Nein: Für x = 1 ist (−1)² = 1, aber −1² = −1.',
                                             ['Ja: Beide haben ein Minus und ein Quadrat.', 'Ja, für alle Zahlen außer 0.', 'Nein: (−x)² ist immer negativ.'],
                                             '(−x)² = (−x) · (−x) = x² ist nie negativ. −x² = −(x²) ist nie positiv. Nur für x = 0 sind beide gleich.',
                                             'Setze x = 1 ein. Wo steht das Minus beim Quadrieren?'))
ST.knobel('aequivalenz', ST.Z('Für wie viele ganze Zahlen x zwischen −10 und 10 haben x² und 3x denselben Wert?', 2, '2',
                              'x² = 3x heißt x · x = 3 · x. Das gilt für x = 0 (0 = 0) und für x = 3 (9 = 9). Für jede andere Zahl darf man durch x teilen und bekommt x = 3 – also gibt es nur diese zwei.',
                              'Vergleiche x · x mit 3 · x. Was passiert bei x = 0?'))
ST.knobel('aequivalenz', ST.L('Der Term (x + 1)² − (x − 1)² ist äquivalent zu einem ganz einfachen Term. Zu welchem?', '□x', [4], ['4'],
                              '(x + 1)² = x² + 2x + 1 und (x − 1)² = x² − 2x + 1. Differenz: 4x. Probe x = 2: 9 − 1 = 8 = 4 · 2 ✓.',
                              'Multipliziere beide Quadrate als Summe mal Summe aus.', 'Tippe den Term ein, z. B. 3x.'))
# binomisch
ST.leiter('binomisch', '(x + a)² und (x − a)² mit der passenden Formel ausmultiplizieren; Formel erkennen.',
          'Faktoren vor x, quadratischer Platz als Sachsituation, Quadrat erkennen und zurückschreiben, Flächenbild deuten.',
          'Geschickt rechnen (51², 49 · 51), Fehler „Mittelglied vergessen“, ergänzen rückwärts, (a − b)² = (b − a)² begründen, Parameter, Prüfungsaufgabe.')
ST.regel('binomisch', 1, 'Wende die', 'direkt')
ST.regel('binomisch', 2, 'Wende die', 'direkt', neu_s=1)
ST.regel('binomisch', 2, 'Multipliziere mit einer binomischen Formel aus', 'mehrschritt')
ST.regel('binomisch', 3, 'Rechne geschickt', 'verknuepfen')
ST.regel('binomisch', 3, 'Jemand rechnet', 'fehler')
ST.regel('binomisch', 3, 'Ergänze', 'rueckwaerts')
ST.neu('binomisch', 1, 'erkennen', ST.A('Welche binomische Formel passt zu (x − 5)(x + 5)?', 'die 3. binomische Formel', ['die 1. binomische Formel', 'die 2. binomische Formel'],
                                        '(a + b)(a − b) = a² − b² ist die 3. Formel: eine Klammer mit plus, eine mit minus.', 'Wie sehen die beiden Klammern aus?'))
ST.neu('binomisch', 2, 'einkleidung', ST.L('Ein quadratischer Platz hat die Seitenlänge x m. Jede Seite wird um 3 m länger, der Platz bleibt quadratisch. Gib die neue Fläche ohne Klammer an.', 'x² + □x + □', [6, 9],
                                           ['2 * 3', '3 * 3'], 'Neue Seite x + 3. (x + 3)² = x² + 6x + 9.', 'Schreibe die neue Seite als Term und quadriere.', 'Tippe den Term ein, z. B. x² + 4x + 4.'))
ST.neu('binomisch', 2, 'umkehr', ST.Z('Schreibe als Quadrat: x² + 10x + 25 = (x + □)²', 5, '10 / 2', '25 = 5² und 10x = 2 · x · 5. Also (x + 5)².', 'Welche Zahl ergibt quadriert 25?'))
ST.neu('binomisch', 2, 'darstellung', ST.A('Ein Quadrat mit der Seite a + b wird in ein Quadrat a², ein Quadrat b² und zwei gleiche Rechtecke zerlegt. Welchen Flächeninhalt hat eines der Rechtecke?',
                                           'ab', ['2ab', 'a + b', 'a²b²'],
                                           'Jedes Rechteck hat die Seiten a und b, also die Fläche ab. Zusammen 2ab – das Mittelglied der 1. Formel.', 'Welche Seitenlängen hat ein Rechteck?'))
ST.neu('binomisch', 3, 'begruenden', ST.A('Stimmt für alle Zahlen: (a − b)² = (b − a)²?', 'Ja: Beide ergeben a² − 2ab + b².',
                                          ['Nein: Das Vorzeichen ändert sich.', 'Nein, nur wenn a = b ist.', 'Ja, aber nur für positive Zahlen.'],
                                          '(a − b)² = a² − 2ab + b² und (b − a)² = b² − 2ab + a² – dasselbe. Auch anschaulich: a − b und b − a unterscheiden sich nur im Vorzeichen, Quadrieren macht beides gleich.',
                                          'Multipliziere beide aus.'))
ST.neu('binomisch', 3, 'parameter', ST.Z('Für welche positive Zahl k lässt sich x² + kx + 16 als Quadrat (x + □)² schreiben?', 8, '2 * 4', '16 = 4². (x + 4)² = x² + 8x + 16, also k = 8.', 'Welche Zahl ergibt quadriert 16?'))
ST.neu('binomisch', 3, 'pruefung', ST.L('Vereinfache so weit wie möglich: (x + 3)² − (x − 3)²', '□x', [12], ['4 * 3'],
                                        '(x + 3)² = x² + 6x + 9, (x − 3)² = x² − 6x + 9. Differenz: 12x.', 'Wende auf beide Quadrate eine binomische Formel an.',
                                        'Tippe den Term ein, z. B. 5x.'))
ST.knobel('binomisch', ST.Z('Berechne ohne Taschenrechner: 1 000 001² − 999 999²', 4000000, '(1000001 + 999999) * (1000001 - 999999)',
                            'Mit der 3. Formel: a² − b² = (a + b)(a − b) = 2 000 000 · 2 = 4 000 000.', 'Die Zahlen liegen nahe beieinander. Welche Formel passt zu a² − b²?'))
ST.knobel('binomisch', ST.Z('35² = 1 225 und 45² = 2 025. Es gibt einen Trick für Zahlen, die auf 5 enden. Wie groß ist 85²?', 7225, '85 * 85',
                            'Eine Zahl mit Zehnerziffer a und Einer 5 ist 10a + 5. (10a + 5)² = 100a² + 100a + 25 = 100 · a · (a + 1) + 25. '
                            'Für 85: a = 8, 8 · 9 = 72, dahinter 25: 7 225.',
                            'Schreibe die Zahl als 10a + 5 und quadriere mit der 1. Formel.'))
# ---- STUFEN ENDE ----


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
    stufen_datei(META['thema_schluessel'], ST)  # Zwanzigste Runde: zuletzt


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('terme.umformen')
# ---- BEREINIGEN ENDE ----


# ---- POTENZ-TEILEN (Sechsundzwanzigste Runde): die vier Potenz-Lernkarten ziehen in den Flug terme.potenzgesetze_natuerlich ----
if __name__ == '__main__':
    from _potenz_teilen import umformen_datei
    umformen_datei()
# ---- POTENZ-TEILEN ENDE ----
