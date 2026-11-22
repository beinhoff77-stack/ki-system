"""Aufgabenfamilien: Terme, lineare Gleichungen/Ungleichungen, Bruchterme/-gleichungen, quadratische Terme, Funktionen."""
from fractions import Fraction as Fr
import math

import sympy as sp

from _nachbau_kern import Kern, check, wissen, z, zk, term, euro, NAMEN, X

sx = X


def nz(rng, lo=1, hi=9):
    n = 0
    while n == 0:
        n = rng.randint(-hi, hi)
        if abs(n) < lo:
            n = 0
    return n


def lin(rng, hi=9):
    return nz(rng, 1, hi) * sx + nz(rng, 1, hi)


def gleich(e1, e2):
    return sp.expand(e1 - e2) == 0


# ---------- Terme umformen ----------
def f_umformen(rng, niv, info, et):
    v = rng.choice([sx, sp.Symbol('a'), sp.Symbol('b'), sp.Symbol('y')])
    w = rng.choice([s for s in [sp.Symbol('a'), sp.Symbol('b'), sp.Symbol('c'), sp.Symbol('y')] if s != v])
    falsch = []
    if et == 'zusammenfassen':
        terme = [sp.Integer(nz(rng, 1, 12)) * rng.choice([v, w, v ** 2 if niv != 'I' else v, sp.Integer(1)]) for _ in range(5 if niv != 'I' else 4)]
        s = ' '.join(('− ' + term(-t_)) if t_.could_extract_minus_sign() else ('+ ' + term(t_)) for t_ in terme)
        s = s[2:] if s.startswith('+ ') else '−' + s[2:]
        e = sum(terme)
        falsch.append((term(sum((-t_ if t_.could_extract_minus_sign() else t_) for t_ in terme)), 'Vorzeichen der Glieder nicht beachtet'))
        aufg = f'Fasse zusammen: {s}'
        weg = ['Gleichartige Glieder (gleiche Variablen und Exponenten) zusammenfassen.', f'= {term(e)}']
    elif et == 'produkte':
        c1, c2 = nz(rng, 2, 9), nz(rng, 2, 9)
        e1, e2 = rng.randint(1, 2), rng.randint(1, 2)
        e = c1 * v ** e1 * w * c2 * v ** e2
        s = f'{term(c1 * v ** e1 * w)} · ({term(c2 * v ** e2)})'
        falsch.append((term(c1 * c2 * v ** (e1 * e2) * w), 'Exponenten multipliziert'))
        aufg = f'Vereinfache: {s}'
        weg = ['Zahlen multiplizieren, gleiche Variablen zusammenfassen (Exponenten addieren).', f'= {term(e)}']
    elif et == 'minusklammer':
        p, q, r = lin(rng), lin(rng), nz(rng, 1, 9) * v
        p, q = p.subs(sx, v), q.subs(sx, v)
        e = p - (q - r) if niv != 'I' else p - q
        s = f'({term(p)}) − [({term(q)}) − {term(r)}]'.replace('(', '(').replace('[', '[') if niv != 'I' else f'{term(p)} − ({term(q)})'
        qt = sp.Add.make_args(sp.expand(q))
        falsch.append((term(p - q - r) if niv != 'I' else term(p - qt[0] + sum(qt[1:])), 'Vorzeichen in der Minusklammer nicht umgekehrt'))
        aufg = f'Löse die Klammern auf und fasse zusammen: {s}'
        weg = ['Steht ein Minus vor der Klammer, kehren sich beim Auflösen alle Vorzeichen um.', 'Innere Klammer zuerst.', f'= {term(e)}']
    elif et == 'ausmultiplizieren':
        k = nz(rng, 2, 9) * (v if niv != 'I' else 1)
        p = (nz(rng, 1, 9) * v + nz(rng, 1, 9) * w)
        e = k * p
        s = f'{term(k)} · ({term(p)})'
        falsch.append((term(k * p.as_ordered_terms()[0] + p.as_ordered_terms()[1]), 'nur den ersten Summanden multipliziert'))
        aufg = f'Multipliziere aus: {s}'
        weg = ['Jeden Summanden der Klammer mit dem Faktor multiplizieren.', f'= {term(e)}']
    elif et == 'summe_mal_summe':
        p, q = lin(rng).subs(sx, v), lin(rng).subs(sx, v)
        e = sp.expand(p * q)
        s = f'({term(p)}) · ({term(q)})'
        a1, b1 = sp.Poly(p, v).all_coeffs()
        a2, b2 = sp.Poly(q, v).all_coeffs()
        falsch.append((term(a1 * a2 * v ** 2 + b1 * b2), 'nur erste mal erste und letzte mal letzte Glieder multipliziert'))
        aufg = f'Multipliziere aus und fasse zusammen: {s}'
        weg = ['Jedes Glied der ersten Klammer mit jedem Glied der zweiten multiplizieren.', f'= {term(e)}']
    elif et == 'ausklammern':
        g = sp.Integer(nz(rng, 2, 6)) * (v if niv != 'I' else 1)
        inn = nz(rng, 1, 7) * v + nz(rng, 1, 7) * (w if niv == 'I' else 1)
        if niv == 'III':
            inn = inn + nz(rng, 1, 5) * v ** 2
        inn_c = sp.Poly(inn, v, w).terms()
        gcdk = math.gcd(*[int(c) for _, c in inn_c])
        inn = sp.expand(inn / gcdk)
        g = g * gcdk
        e_ausmult = sp.expand(g * inn)
        e = sp.factor(e_ausmult)
        s = term(e_ausmult)
        aufg = f'Klammere den größtmöglichen gemeinsamen Faktor aus: {s}'
        ant = f'{term(g)} · ({term(inn)})'
        weg = [f'Größter gemeinsamer Faktor: {term(g)}', f'= {ant}', f'Probe: ausmultiplizieren ergibt wieder {s}']
        g = sp.sympify(g)
        teil = g / 2 if g.as_coeff_Mul()[0] % 2 == 0 else (g / v if g.has(v) else None)
        if teil is not None:
            falsch.append((f'{term(teil)} · ({term(sp.expand(e_ausmult / teil))})', 'nicht den größten gemeinsamen Faktor ausgeklammert'))
        falsch.append((f'{term(g)} · ({term(sp.expand(inn - 2 * sp.Add.make_args(inn)[-1]))})', 'Vorzeichen in der Klammer falsch'))
        return Kern('', aufg, ant, weg, falsch, [check('Probe ausmultiplizieren', gleich(g * inn, e_ausmult))], luecke=f'Ergänze: {s} = {term(g)} · ( ___ )')
    elif et == 'binomisch':
        a, b = rng.randint(1, 6), rng.randint(1, 9)
        if niv != 'I':
            a = rng.randint(2, 7)
        art = rng.choice(['plus', 'minus', 'dritte'])
        if art == 'plus':
            p = (a * v + b) ** 2
            s = f'({term(a * v)} + {b})²'
            falsch.append((term(a ** 2 * v ** 2 + b ** 2), 'gemischtes Glied 2ab vergessen'))
        elif art == 'minus':
            p = (a * v - b) ** 2
            s = f'({term(a * v)} − {b})²'
            falsch.append((term(a ** 2 * v ** 2 - b ** 2), 'gemischtes Glied vergessen und Vorzeichen falsch'))
        else:
            p = (a * v + b) * (a * v - b)
            s = f'({term(a * v)} + {b}) · ({term(a * v)} − {b})'
            falsch.append((term(a ** 2 * v ** 2 + b ** 2), 'Vorzeichen bei der 3. binomischen Formel falsch'))
        e = sp.expand(p)
        if niv == 'III' or info.get('besonderheit', '').find('rückwärts') >= 0:
            ant = s
            weg = [f'Quadratzahlen erkennen: {term(e.coeff(v, 2) * v ** 2)} = ({term(a * v)})², {b * b} = {b}²', 'Mittleres Glied prüfen: 2 · a · b', f'{term(e)} = {s}']
            return Kern('', f'Schreibe als Produkt (binomische Formel rückwärts): {term(e)}', ant, weg,
                        [(f'({term(a * v)} + {b * b})²', 'Wurzel aus der Zahl nicht gezogen')], [check('Probe', gleich(p, e))],
                        luecke=f'Ergänze die Lücken: {term(a * a * v ** 2)} ___ {b * b} = ({term(a * v)} ___ {b})²' if art != 'dritte' else None)
        aufg = f'Wende eine binomische Formel an: {s}'
        weg = ['Passende binomische Formel wählen: (a ± b)² = a² ± 2ab + b² bzw. (a + b)(a − b) = a² − b².', f'= {term(e)}']
        k = Kern('', aufg, term(e), weg, falsch, [check('ausmultipliziert', gleich(p, e))],
                 luecke=f'Ergänze: {s} = {term(e.coeff(v, 2) * v ** 2)} ___ {term(e.subs(v, 0))}' if art != 'dritte' else None)
        return k
    else:  # aequivalenz
        a, b, c = nz(rng, 2, 6), nz(rng, 1, 9), nz(rng, 2, 5)
        links = c * (a * v + b)
        e = sp.expand(links)
        aufg = f'Ergänze die Lücken so, dass gleichwertige Terme entstehen: {c}·( ___ + {zk(b)}) = {term(e)}'
        return Kern('', aufg, f'{term(a * v)}', [f'{term(e)} : {c} = {term(a * v + b)}', f'Lücke: {term(a * v)}'],
                    [(term(e.coeff(v) * v), 'Faktor vor der Klammer nicht berücksichtigt')], [check('gleichwertig', gleich(c * (a * v + b), e))], luecke=aufg)
    return Kern('', aufg, term(e), weg, falsch, [check('mit sympy ausmultipliziert', gleich(e, sp.expand(e)))])


# ---------- Terme aufstellen ----------
UEBERS = [('Multipliziere die Summe aus x und {a} mit {b}.', lambda a, b: b * (sx + a), lambda a, b: b * sx + a),
          ('Subtrahiere vom {b}-Fachen einer Zahl x die Zahl {a}.', lambda a, b: b * sx - a, lambda a, b: a - b * sx),
          ('Dividiere die Differenz aus x und {a} durch {b}.', lambda a, b: (sx - a) / b, lambda a, b: sx - sp.Rational(a, b)),
          ('Addiere zum Quadrat einer Zahl x das {b}-Fache der Zahl.', lambda a, b: sx ** 2 + b * sx, lambda a, b: (sx + b * sx) ** 2),
          ('Das Produkt aus {b} und der um {a} verminderten Zahl x.', lambda a, b: b * (sx - a), lambda a, b: b * sx - a)]


def f_aufstellen(rng, niv, info, et):
    if et in ('termwert',):
        a, b = nz(rng, 1, 6), nz(rng, 1, 9)
        t = a * sx ** 2 + b if niv != 'I' else a * sx + b
        xs = sorted(rng.sample(range(-4, 5), 4))
        werte = [t.subs(sx, xx) for xx in xs]
        tab = '| x | ' + ' | '.join(z(xx) for xx in xs) + ' |\n|---|' + '---|' * 4 + '\n| T(x) | ' + ' | '.join('___' for _ in xs) + ' |'
        return Kern(f'Gegeben ist der Term T(x) = {term(t)}.\n\n{tab}\n', 'Vervollständige die Wertetabelle.', '; '.join(f'T({z(xx)}) = {z(int(w))}' for xx, w in zip(xs, werte)),
                    ['Für x jeweils den Wert einsetzen (negative Zahlen in Klammern).'] + [f'T({z(xx)}) = {z(int(w))}' for xx, w in zip(xs[:2], werte[:2])],
                    [('; '.join(f'T({z(xx)}) = {z(int(a * abs(xx) ** (2 if niv != "I" else 1) * (1 if niv != "I" else -1) + b))}' for xx in xs[:2]), 'Vorzeichen beim Einsetzen negativer Zahlen')],
                    [check('eingesetzt', all(w == t.subs(sx, xx) for xx, w in zip(xs, werte)))])
    if et in ('uebersetzen', 'deuten', 'struktur'):
        txt, f, fehl = rng.choice(UEBERS)
        a, b = rng.randint(2, 9), rng.randint(2, 7)
        t = f(a, b)
        tx = txt.format(a=a, b=b)
        rich = term_struktur(t, txt, a, b)
        fal = term_struktur(fehl(a, b), None, a, b)
        if et == 'deuten':
            return Kern(f'Gegeben ist der Term {rich}.', 'Welche Beschreibung passt?', tx, ['Rechenart der äußersten Verknüpfung bestimmt die Beschreibung (Summe, Differenz, Produkt, Quotient).'],
                        [(txt.format(a=b, b=a), 'Zahlen vertauscht'), ('Addiere ' + str(a) + ' zum ' + str(b) + '-Fachen von x.', 'Klammer nicht beachtet')], [wissen('Term')])
        return Kern('', f'Schreibe als Term: {tx}', rich, [f'Gliederung des Satzes: {tx}', f'Term: {rich}'], [(fal, 'Klammer vergessen bzw. Reihenfolge vertauscht')],
                    [check('Struktur', not gleich(f(a, b), fehl(a, b)))])
    if et == 'muster':
        a, b = rng.randint(2, 6), rng.randint(1, 5)
        k = rng.randint(6, 12)
        return Kern(f'Mit Hölzchen werden Figuren gelegt. Figur 1 besteht aus {a + b} Hölzchen, jede weitere Figur hat {a} Hölzchen mehr als die vorherige.',
                    f'Wie viele Hölzchen braucht Figur {k}? Gib einen Term für Figur n an.', f'{a * k + b} Hölzchen; Term {a}n + {b}',
                    [f'Zuwachs je Figur: {a} → {a}n', f'Figur 1: {a} · 1 + {b} = {a + b} ✓', f'Figur {k}: {a} · {k} + {b} = {a * k + b}'],
                    [(f'{(a + b) * k} Hölzchen; Term {a + b}n', 'Startwert mitvervielfacht')], [check('Figur 1', a + b == a * 1 + b)])
    # sachsituation: Umfang/Fläche einer Figur mit Variablen
    a, b, c = rng.randint(2, 5), rng.randint(1, 6), rng.randint(1, 4)
    lang = a * sx + b
    breit = sx + c
    if niv == 'I' or rng.random() < .5:
        u = 2 * (lang + breit)
        return Kern(f'Ein Rechteck ist ({term(lang)}) cm lang und ({term(breit)}) cm breit.', 'Stelle einen Term für den Umfang auf und vereinfache ihn.', f'U(x) = {term(u)} (in cm)',
                    ['U = 2 · (Länge + Breite)', f'= 2 · ({term(lang)} + {term(breit)}) = {term(u)}'], [(term(lang + breit), 'nur eine Länge und eine Breite addiert'), (term(lang * breit), 'Fläche statt Umfang')],
                    [check('vereinfacht', gleich(u, 2 * lang + 2 * breit))], luecke=f'Ergänze: U(x) = 2 · ({term(lang)} + ___) = ___')
    f = sp.expand(lang * breit - sx * sx)
    return Kern(f'Aus einem Rechteck mit den Seiten ({term(lang)}) cm und ({term(breit)}) cm wird ein Quadrat mit der Seitenlänge x cm ausgeschnitten.',
                'Stelle einen Term für den Flächeninhalt der Restfläche auf und vereinfache.', f'A(x) = {term(f)} (in cm²)',
                ['A = Rechteck − Quadrat', f'= ({term(lang)})({term(breit)}) − x²', f'= {term(f)}'], [(term(sp.expand(lang * breit)), 'Quadrat nicht abgezogen')],
                [check('ausmultipliziert', gleich(f, lang * breit - sx ** 2))])


def term_struktur(t, txt, a, b):
    if txt and 'Summe aus x' in txt:
        return f'{b} · (x + {a})'
    if txt and 'Differenz aus x' in txt:
        return f'(x − {a}) : {b}'
    if txt and 'verminderten' in txt:
        return f'{b} · (x − {a})'
    return term(t)


# ---------- Gleichungen ----------
GL_SACH = ['zahl', 'alter', 'preis', 'umfang', 'geschenk']


def f_gleichung(rng, niv, info, et):
    loes = Fr(nz(rng, 1, 12)) if niv == 'I' else Fr(rng.choice([nz(rng, 1, 12), Fr(nz(rng, 1, 9), 2)]))
    L = sp.Rational(loes.numerator, loes.denominator)
    if et == 'sach' or info.get('typ') == 'Sachaufgabe':
        return f_gl_sach(rng, niv, info)
    if et == 'sonderfaelle':
        a, b = nz(rng, 2, 7), nz(rng, 1, 9)
        art = rng.choice(['leer', 'alle'])
        lhs = a * (sx + b)
        rhs = a * sx + a * b + (nz(rng, 1, 5) if art == 'leer' else 0)
        return Kern('', f'Bestimme die Lösungsmenge über ℚ: {term_fakt(a, b)} = {term(rhs)}', 'L = { }' if art == 'leer' else 'L = ℚ',
                    ['Klammer auflösen: ' + term(sp.expand(lhs)) + ' = ' + term(rhs), 'x fällt weg: ' + ('falsche Aussage → keine Lösung' if art == 'leer' else 'wahre Aussage → alle Zahlen')],
                    [('L = {0}', 'x = 0 als Lösung angegeben, obwohl x weggefallen ist')], [check('Sonderfall', (sp.solve(sp.Eq(lhs, rhs), sx) == []) )])
    if et == 'waage':
        a = rng.randint(2, 6)
        b = rng.randint(1, 15)
        L = sp.Integer(rng.randint(1, 12))
        lhs, rhs = a * sx + b, a * L + b
    elif et == 'beide_seiten':
        a, c = nz(rng, 1, 9), nz(rng, 1, 9)
        while a == c:
            c = nz(rng, 1, 9)
        b = nz(rng, 1, 15)
        d = (a - c) * L + b
        lhs, rhs = a * sx + b, c * sx + d
    else:  # klammern, probe
        a, b, c, d = nz(rng, 2, 6), nz(rng, 1, 8), nz(rng, 2, 5), nz(rng, 1, 8)
        if niv == 'III' or 'binomisch' in info.get('besonderheit', ''):
            p = rng.randint(1, 6)
            lhs = (sx + p) ** 2 - sx * (sx + c)
            rhs_k = sp.expand(lhs).subs(sx, L)
            lhs_s = f'(x + {p})² − x(x + {c})' if c > 0 else f'(x + {p})² − x(x − {-c})'
            rhs = rhs_k
            if sp.expand(lhs).coeff(sx) == 0:
                return f_gleichung(rng, 'II', info, et)
        else:
            lhs = a * (sx + b) - c * (sx - d)
            lhs_s = f'{a}(x {"+" if b > 0 else "−"} {abs(b)}) {"−" if c > 0 else "+"} {abs(c)}(x {"−" if d > 0 else "+"} {abs(d)})'
            if sp.expand(lhs).coeff(sx) == 0:
                return f_gleichung(rng, niv, info, et)
            rhs = sp.expand(lhs).subs(sx, L)
        if et == 'probe':
            kand = L if rng.random() < .5 else L + 1
            ist = sp.simplify(lhs.subs(sx, kand) - rhs) == 0
            return Kern(f'{rng.choice(NAMEN)} hat für die Gleichung {lhs_s} = {z(rhs)} die Lösung x = {z(kand)} angegeben.', 'Prüfe durch eine Probe, ob das stimmt.',
                        ('Ja, ' if ist else 'Nein, ') + f'linke Seite für x = {z(kand)}: {z(lhs.subs(sx, kand))}, rechte Seite: {z(rhs)}' + ('' if ist else f'; richtig ist x = {z(L)}'),
                        [f'x = {z(kand)} einsetzen: {z(lhs.subs(sx, kand))}', f'Vergleich mit {z(rhs)}'], [('falsch' if ist else 'richtig', 'Probe nicht gerechnet')], [check('Probe', (lhs.subs(sx, L) == rhs))],
                        antwort_kurz='richtig' if ist else 'falsch')
        sol = sp.solve(sp.Eq(lhs, rhs), sx)
        return Kern('', f'Bestimme die Lösungsmenge (G = ℚ): {lhs_s} = {z(rhs)}', f'L = {{{z(L)}}}',
                    ['Klammern auflösen: ' + term(sp.expand(lhs)) + f' = {z(rhs)}', 'Glieder mit x auf eine Seite, Zahlen auf die andere.', f'x = {z(L)}', f'Probe: linke Seite = {z(lhs.subs(sx, L))} ✓'],
                    [(f'L = {{{z(-L)}}}', 'Vorzeichenfehler beim Auflösen der Minusklammer'), (f'L = {{{z(L + 1)}}}', 'Rechenfehler beim Zusammenfassen')],
                    [check('Probe durch Einsetzen', sp.simplify(lhs.subs(sx, L) - rhs) == 0), check('sympy-Lösung', sol == [L])])
    sol = sp.solve(sp.Eq(lhs, rhs), sx)
    return Kern('', f'Löse die Gleichung (G = ℚ): {term(lhs)} = {term(rhs)}', f'L = {{{z(L)}}}',
                ['Äquivalenzumformungen: auf beiden Seiten dasselbe addieren/subtrahieren, dann durch den Faktor vor x dividieren.', f'x = {z(L)}', f'Probe: {z(lhs.subs(sx, L))} = {z(rhs.subs(sx, L) if hasattr(rhs, "subs") else rhs)} ✓'],
                [(f'L = {{{z(-L)}}}', 'beim Umformen das Vorzeichen falsch übernommen')], [check('Probe', sp.simplify(lhs.subs(sx, L) - (rhs.subs(sx, L) if hasattr(rhs, 'subs') else rhs)) == 0), check('sympy', sol == [L])])


def term_fakt(a, b):
    return f'{a}(x {"+" if b > 0 else "−"} {abs(b)})'


def f_gl_sach(rng, niv, info):
    art = rng.choice(GL_SACH)
    n = rng.choice(NAMEN)
    if art == 'zahl':
        x0 = rng.randint(3, 25)
        a, b = rng.randint(2, 6), rng.randint(2, 20)
        c = rng.randint(2, 5)
        while c == a:
            c = rng.randint(2, 7)
        rechts = c * x0 + (a - c) * x0 - (a * x0 - b) + 0
        rhs = a * x0 - b
        txt = f'Nimmt man eine Zahl {a}-mal und subtrahiert {b}, erhält man {rhs}.'
        gl, L = f'{a}x − {b} = {rhs}', x0
        if niv != 'I':
            d = a * x0 - b - c * x0
            txt = (f'Verkleinert man das {a}-Fache einer gesuchten Zahl um {b}, ist das Ergebnis genauso groß wie das {c}-Fache der Zahl, '
                   + (f'vergrößert um {d}.' if d >= 0 else f'verkleinert um {-d}.'))
            gl = f'{a}x − {b} = {c}x ' + (f'+ {d}' if d >= 0 else f'− {-d}')
        return Kern(txt, 'Stelle eine Gleichung auf und bestimme die Zahl.', f'{gl}; x = {L}', [f'Gleichung: {gl}', f'x = {L}', f'Probe: {a} · {L} − {b} = {a * L - b}'],
                    [(f'x = {L + 1}', 'Rechenfehler')], [check('Probe', a * L - b == (rhs if niv == 'I' else c * L + a * x0 - b - c * x0))])
    if art == 'alter':
        m = rng.randint(9, 14)
        d1, d2 = rng.randint(2, 5), rng.randint(1, 4)
        s = (m + d1) + m + (m - d2)
        return Kern(f'Drei Geschwister sind zusammen {s} Jahre alt. Die Älteste ist {d1} Jahre älter als der Mittlere, der Jüngste ist {d2} Jahre jünger als der Mittlere.',
                    'Wie alt sind die drei? Stelle eine Gleichung auf.', f'(x + {d1}) + x + (x − {d2}) = {s}; {m + d1}, {m} und {m - d2} Jahre',
                    [f'x: Alter des Mittleren', f'3x + {d1 - d2} = {s}' if d1 >= d2 else f'3x − {d2 - d1} = {s}', f'x = {m}'],
                    [(f'{z(Fr(s, 3))} Jahre für alle', 'Altersunterschiede nicht berücksichtigt')], [check('Probe', (m + d1) + m + (m - d2) == s)])
    if art == 'preis':
        k = rng.randint(4, 9)
        e = 2 * k if rng.random() < .5 else k + rng.randint(2, 6)
        ne, nk = rng.randint(1, 3), rng.randint(2, 5)
        ges = ne * e + nk * k
        faktor = e == 2 * k
        rel = 'doppelt so viel wie eine Kinderkarte' if faktor else f'{e - k} € mehr als eine Kinderkarte'
        gl = f'{ne} · 2x + {nk}x = {ges}' if faktor else f'{ne}(x + {e - k}) + {nk}x = {ges}'
        return Kern(f'Im Freizeitbad kostet eine Erwachsenenkarte {rel}. Eine Familie mit {ne} Erwachsenen und {nk} Kindern zahlt {euro(ges)}.',
                    'Berechne die Preise für beide Karten mit einer Gleichung.', f'{gl}; Kind {euro(k)}, Erwachsene {euro(e)}',
                    [f'x: Preis der Kinderkarte', gl, f'x = {k}'], [(f'Kind {euro(Fr(ges, ne + nk))}', 'alle Karten gleich teuer angenommen')], [check('Probe', ne * e + nk * k == ges)])
    if art == 'umfang':
        b0 = rng.randint(3, 12)
        d = rng.randint(2, 7)
        u = 2 * (b0 + b0 + d)
        return Kern(f'Ein rechteckiges Beet ist {d} m länger als breit. Für die Einfassung braucht man {u} m Kantensteine.',
                    'Wie lang und wie breit ist das Beet?', f'Breite {b0} m, Länge {b0 + d} m', [f'2 · (x + x + {d}) = {u}', f'4x + {2 * d} = {u}', f'x = {b0}'],
                    [(f'Breite {z(Fr(u, 4))} m', 'Längenunterschied nicht berücksichtigt')], [check('Probe', 2 * (2 * b0 + d) == u)])
    k = rng.randint(3, 6)
    each = rng.randint(4, 12)
    rest = rng.randint(1, 9)
    tot = k * each + rest
    return Kern(f'{n} verteilt {tot} Sticker gleichmäßig an {k} Freunde und behält {rest} übrig.', 'Wie viele Sticker bekommt jedes Kind? Stelle eine Gleichung auf.',
                f'{k}x + {rest} = {tot}; x = {each}', [f'{k}x = {tot - rest}', f'x = {each}'], [(f'{z(Fr(tot, k))}', 'Rest nicht abgezogen')], [check('Probe', k * each + rest == tot)])


# ---------- Ungleichungen ----------
def f_ungl(rng, niv, info, et):
    if et == 'sachaufgabe' or info.get('typ') == 'Sachaufgabe':
        fix = rng.randint(10, 60)
        p = rng.choice([3, 4, 5, Fr(5, 2), Fr(7, 2), 6, 8])
        budget = fix + p * rng.randint(4, 20) + rng.randint(0, 2)
        nmax = math.floor((budget - fix) / Fr(p))
        return Kern(f'Ein Kletterpark verlangt {euro(fix)} Grundgebühr pro Gruppe und {euro(p)} pro Person. Die Klasse hat höchstens {euro(budget)} zur Verfügung.',
                    'Wie viele Personen können höchstens mitkommen? Stelle eine Ungleichung auf.', f'{z(fix)} + {z(p)}x ≤ {z(budget)}; höchstens {nmax} Personen',
                    [f'{z(fix)} + {z(p)}x ≤ {z(budget)}', f'{z(p)}x ≤ {z(budget - fix)}', f'x ≤ {z((budget - fix) / Fr(p))} → höchstens {nmax} (ganze Personen)'],
                    [(f'{nmax + 1} Personen', 'aufgerundet statt abgerundet'), (f'{math.floor(budget / Fr(p))} Personen', 'Grundgebühr vergessen')],
                    [check('Grenzfall', fix + p * nmax <= budget < fix + p * (nmax + 1))])
    a = nz(rng, 2, 6) * (-1 if et == 'umdrehen' or niv != 'I' else 1)
    b = nz(rng, 1, 12)
    g = Fr(nz(rng, 1, 9))
    c = a * g + b
    zei = rng.choice(['<', '≤', '>', '≥'])
    rel = {'<': sp.Lt, '≤': sp.Le, '>': sp.Gt, '≥': sp.Ge}[zei]
    neu = {'<': '>', '>': '<', '≤': '≥', '≥': '≤'}[zei] if a < 0 else zei
    if et == 'klammern':
        k = nz(rng, 2, 4)
        lhs_s = f'{k}(x {"+" if b > 0 else "−"} {abs(b)}) − {abs(a) + k}x' if a < 0 else f'{k}(x + {abs(b)})'
        lhs = k * (sx + b) - (abs(a) + k) * sx if a < 0 else k * (sx + abs(b))
        aa = sp.expand(lhs).coeff(sx)
        bb = sp.expand(lhs).subs(sx, 0)
        c = aa * g + bb
        a = aa
        neu = {'<': '>', '>': '<', '≤': '≥', '≥': '≤'}[zei] if a < 0 else zei
    else:
        lhs = a * sx + b
        lhs_s = term(lhs)
    loes = sp.solve_univariate_inequality(rel(lhs, c), sx, relational=False)
    ant = f'x {neu} {z(g)}'
    intervall = {'<': f']−∞; {z(g)}[', '≤': f']−∞; {z(g)}]', '>': f']{z(g)}; ∞[', '≥': f'[{z(g)}; ∞['}[neu]
    if et == 'pruefen':
        test = int(g) + rng.choice([-2, -1, 0, 1, 2])
        erfuellt = bool(rel(lhs.subs(sx, test), c))
        return Kern(f'Gegeben ist die Ungleichung {lhs_s} {zei} {z(c)} (G = ℚ).', f'Ist x = {z(test)} eine Lösung? Begründe durch Einsetzen.',
                    ('Ja' if erfuellt else 'Nein') + f': {z(lhs.subs(sx, test))} {zei} {z(c)} ist {"wahr" if erfuellt else "falsch"}', [f'x = {z(test)} einsetzen: {z(lhs.subs(sx, test))}', f'Vergleich mit {z(c)}'],
                    [('Nein' if erfuellt else 'Ja', 'Relationszeichen falsch gelesen')], [check('Einsetzen', erfuellt == (test in loes))], antwort_kurz='Ja' if erfuellt else 'Nein')
    fehl = {'<': '<', '>': '>', '≤': '≤', '≥': '≥'}[zei]
    k = Kern('', f'Bestimme die Lösungsmenge (G = ℚ): {lhs_s} {zei} {z(c)}' + (' Gib sie auch als Intervall an.' if et == 'intervall' else ''),
             f'L = {{x | {ant}}}' + (f' = {intervall}' if et == 'intervall' else ''),
             [f'{term(lhs) if lhs_s != term(lhs) else lhs_s} {zei} {z(c)}', f'{term(a * sx)} {zei} {z(c - (sp.expand(lhs).subs(sx, 0)))}', f'Division durch {z(a)}' + (' (negativ → Relationszeichen umdrehen)' if a < 0 else ''), f'x {neu} {z(g)}'],
             [(f'L = {{x | x {fehl} {z(g)}}}', 'Relationszeichen beim Dividieren durch eine negative Zahl nicht umgedreht')] if a < 0 else [(f'L = {{x | x {neu} {z(-g)}}}', 'Vorzeichenfehler')],
             [check('Grenze', sp.simplify(lhs.subs(sx, g) - c) == 0), check('Testpunkt', (g + 1 in loes) == (neu in ('>', '≥')))])
    return k


# ---------- Bruchterme / Bruchgleichungen ----------
def f_bruch_alg(rng, niv, info, et, thema):
    n1, n2 = nz(rng, 1, 7), nz(rng, 1, 7)
    while n1 == n2:
        n2 = nz(rng, 1, 7)
    if et == 'definitionsmenge' and thema == 'terme.bruchterme':
        k = rng.choice([2, 3, 4])
        nenner = (sx - n1) * (k * sx + n2) if niv != 'I' else (sx - n1)
        aus = sorted({sp.Rational(n1), sp.Rational(-n2, k)} if niv != 'I' else {sp.Rational(n1)})
        zt = term(sx + nz(rng, 1, 9))
        nt = f'(x {"−" if n1 > 0 else "+"} {abs(n1)})({k}x {"+" if n2 > 0 else "−"} {abs(n2)})' if niv != 'I' else f'x {"−" if n1 > 0 else "+"} {abs(n1)}'
        ant = 'D = ℚ \\ {' + '; '.join(z(a) for a in aus) + '}'
        return Kern('', f'Gib die Definitionsmenge des Bruchterms ({zt}) / ({nt}) an (G = ℚ).', ant,
                    ['Der Nenner darf nicht 0 werden.', 'Nullstellen des Nenners: ' + '; '.join(z(a) for a in aus)],
                    [('D = ℚ \\ {' + '; '.join(z(-a) for a in aus) + '}', 'Vorzeichen der Nullstellen vertauscht')], [check('Nennernullstellen', set(sp.solve(nenner, sx)) == set(aus))])
    if et in ('kuerzen', 'termwert', 'erweitern'):
        f = rng.randint(2, 6)
        zt, nt = f * (sx + n1), f * f * (sx + n1) * (sx - n2) if niv != 'I' else f * f * (sx + n1)
        erg = sp.cancel(zt / nt)
        return Kern('', f'Kürze so weit wie möglich: ({term(sp.expand(zt))}) / ({term(sp.expand(nt))})', f'{term(erg)} (für x ≠ {z(-n1)}' + (f', x ≠ {z(n2)})' if niv != 'I' else ')'),
                    ['Zähler und Nenner faktorisieren.', f'Gemeinsamen Faktor {f}(x {"+" if n1 > 0 else "−"} {abs(n1)}) kürzen.', f'= {term(erg)}'],
                    [('x/' + str(f * f), 'aus Summen gekürzt')], [check('gleichwertig', sp.simplify(zt / nt - erg) == 0)])
    if et in ('addieren', 'multiplizieren', 'fehler_finden'):
        a, b = rng.randint(1, 6), rng.randint(1, 6)
        e = sp.Rational(a) / sx + sp.Rational(b) / (2 * sx)
        erg = sp.together(e)
        return Kern('', f'Fasse zusammen (x ≠ 0): {a}/x + {b}/(2x)', f'{2 * a + b}/(2x)', ['Hauptnenner 2x', f'{2 * a}/(2x) + {b}/(2x) = {2 * a + b}/(2x)'],
                    [(f'{a + b}/(3x)', 'Zähler und Nenner einzeln addiert')], [check('sympy', sp.simplify(erg - sp.Rational(2 * a + b) / (2 * sx)) == 0)])
    # Bruchgleichungen
    L = sp.Integer(nz(rng, 1, 9))
    if et in ('ueber_kreuz', 'ein_bruch', 'definitionsmenge', 'verhaeltnis', 'scheinloesung'):
        p, q = rng.randint(2, 7), rng.randint(1, 7)
        while p == q:
            q = rng.randint(1, 7)
        # p/(x + n1) = q/(x + n2) mit Lösung L
        n2_ = sp.Rational(p * (L + n2) - q * L, q) if False else None
        n1_ = nz(rng, 1, 6)
        n2_ = sp.Rational(q, p) * (L + n1_) - L
        if n2_.q != 1 or L + n1_ == 0 or L + n2_ == 0 or n1_ == n2_:
            return f_bruch_alg(rng, niv, info, et, thema)
        lhs, rhs = p / (sx + n1_), q / (sx + n2_)
        sol = sp.solve(sp.Eq(lhs, rhs), sx)
        D = f'D = ℚ \\ {{{z(-n1_)}; {z(-n2_)}}}'
        gl = f'{p}/(x {"+" if n1_ > 0 else "−"} {abs(n1_)}) = {q}/(x {"+" if n2_ > 0 else "−"} {abs(n2_)})'
        if et == 'definitionsmenge':
            return Kern('', f'Gib die Definitionsmenge der Bruchgleichung {gl} an (G = ℚ).', D, ['Nenner dürfen nicht 0 werden.', D],
                        [(f'D = ℚ \\ {{{z(n1_)}; {z(n2_)}}}', 'Vorzeichen vertauscht')], [wissen('Nenner')])
        return Kern('', f'Bestimme Definitionsmenge und Lösungsmenge (G = ℚ): {gl}', f'{D}; L = {{{z(L)}}}',
                    [D, f'Über Kreuz multiplizieren: {p}(x {"+" if n2_ > 0 else "−"} {abs(n2_)}) = {q}(x {"+" if n1_ > 0 else "−"} {abs(n1_)})', f'x = {z(L)} ∈ D', f'Probe: beide Seiten = {z(lhs.subs(sx, L))}'],
                    [(f'L = {{{z(-L)}}}', 'Vorzeichenfehler')], [check('sympy', sol == [L]), check('Probe', lhs.subs(sx, L) == rhs.subs(sx, L))])
    # hauptnenner
    a, b = rng.randint(1, 6), rng.randint(2, 5)
    c = sp.Rational(a, L) + sp.Rational(b, 2 * L)
    gl = f'{a}/x + {b}/(2x) = {z(Fr(int(c.p), int(c.q)))}'
    sol = sp.solve(sp.Eq(a / sx + b / (2 * sx), c), sx)
    return Kern('', f'Löse die Bruchgleichung (G = ℚ): {gl}', f'D = ℚ \\ {{0}}; L = {{{z(L)}}}',
                ['D = ℚ \\ {0}', 'Mit dem Hauptnenner 2x multiplizieren.', f'{2 * a} + {b} = {z(Fr(int(c.p), int(c.q)))} · 2x', f'x = {z(L)}'],
                [(f'L = {{{z(1 / L) if L != 0 else 1}}}', 'Kehrwert genommen')], [check('sympy', sol == [L])])


# ---------- quadratische Terme ----------
def f_quad(rng, niv, info, et):
    a = 1 if niv == 'I' else rng.choice([1, -1, 2, -2])
    h = nz(rng, 1, 6)
    k = nz(rng, 0, 9) if True else 0
    t = sp.expand(a * (sx - h) ** 2 + k)
    art = 'Minimum' if a > 0 else 'Maximum'
    sf = f'{"" if a == 1 else "−" if a == -1 else z(a)}(x {"−" if h > 0 else "+"} {abs(h)})² {"+" if k >= 0 else "−"} {abs(k)}'
    if et == 'ergaenzen':
        b = sp.expand(t).coeff(sx)
        return Kern('', f'Ergänze quadratisch: x² {"+" if -2 * h > 0 else "−"} {abs(2 * h)}x + ___ = (x {"−" if h > 0 else "+"} {abs(h)})²', f'{h * h}',
                    [f'(x − h)² = x² − 2hx + h², h = {h} → h² = {h * h}'], [(f'{2 * h}', 'nicht quadriert'), (f'{abs(h)}', 'Hälfte statt Quadrat der Hälfte')],
                    [check('binomisch', gleich((sx - h) ** 2, sx ** 2 - 2 * h * sx + h * h))])
    if et == 'scheitelform':
        return Kern('', f'Gib einen quadratischen Term an, dessen {art} {z(k)} an der Stelle x = {z(h)} liegt' + (' und der in der Form a(x − d)² + e mit a = ' + z(a) + ' steht.' if a != 1 else '.'),
                    f'T(x) = {sf}', [f'Scheitelform a(x − d)² + e mit d = {z(h)}, e = {z(k)}'], [(f'T(x) = {"" if a == 1 else z(a)}(x {"+" if h > 0 else "−"} {abs(h)})² {"+" if k >= 0 else "−"} {abs(k)}', 'Vorzeichen in der Klammer falsch')],
                    [check('Extremum', sp.solve(sp.diff(t, sx), sx) == [h] and t.subs(sx, h) == k)])
    xs = sp.solve(sp.diff(t, sx), sx)
    return Kern(f'Gegeben ist T(x) = {term(t)} (G = ℚ).', f'Bestimme durch quadratische Ergänzung das {art} des Terms und für welches x es angenommen wird.',
                f'T_{"min" if a > 0 else "max"} = {z(k)} für x = {z(h)}', [f'T(x) = {sf}', f'Das Quadrat ist ≥ 0, also ist {z(k)} der {"kleinste" if a > 0 else "größte"} Wert, er wird für x = {z(h)} angenommen.'],
                [(f'T_{"min" if a > 0 else "max"} = {z(k)} für x = {z(-h)}', 'Vorzeichen in der Klammer falsch gedeutet'), (f'T_{"min" if a > 0 else "max"} = {z(t.subs(sx, 0))} für x = 0', 'Wert bei x = 0 statt Extremum')],
                [check('Ableitung 0 bei x = h', xs == [h]), check('Funktionswert', t.subs(sx, h) == k)])


# ---------- Funktionen ----------
def f_funktion(rng, niv, info, et, thema):
    m = sp.Rational(nz(rng, 1, 4), rng.choice([1, 1, 2])) if niv != 'I' else sp.Integer(nz(rng, 1, 4))
    t = sp.Integer(nz(rng, 0, 6))
    f = m * sx + t
    fs = f'y = {term(f)}'
    if et == 'eindeutig':
        xs = [1, 2, 3, 4]
        ys = [rng.randint(1, 9) for _ in xs]
        ist = rng.random() < .5
        if not ist:
            xs[3] = xs[1]
        tab = '| x | ' + ' | '.join(map(str, xs)) + ' |\n|---|---|---|---|---|\n| y | ' + ' | '.join(map(str, ys)) + ' |'
        return Kern(f'Eine Zuordnung ist durch die Tabelle gegeben.\n\n{tab}\n', 'Ist die Zuordnung eine Funktion? Begründe.',
                    'Ja, jedem x-Wert ist genau ein y-Wert zugeordnet.' if ist else f'Nein, dem x-Wert {xs[1]} sind zwei y-Werte zugeordnet.',
                    ['Funktion: jedem x genau ein y.'], [('Nein' if ist else 'Ja', 'Definition verwechselt (ein y darf mehrfach vorkommen)')],
                    [check('Eindeutigkeit', ist == (len(set(xs)) == len(xs)))], antwort_kurz='Ja' if ist else 'Nein')
    if et in ('funktionswert', 'einsetzen', 'punkt_graph'):
        x0 = nz(rng, 1, 6)
        y0 = f.subs(sx, x0)
        if et == 'punkt_graph':
            yp = y0 if rng.random() < .5 else y0 + 1
            liegt = yp == y0
            return Kern(f'Gegeben ist die Gerade g: {fs}.', f'Liegt der Punkt P({z(x0)} | {z(yp)}) auf g? Begründe durch Rechnung.',
                        ('Ja' if liegt else 'Nein') + f', denn für x = {z(x0)} ist y = {z(y0)}.', [f'x = {z(x0)} einsetzen: y = {term(m)}·{zk(x0)} {"+" if t >= 0 else "−"} {abs(t)} = {z(y0)}'],
                        [('Nein' if liegt else 'Ja', 'Koordinaten vertauscht eingesetzt')], [check('Einsetzen', f.subs(sx, x0) == y0)], antwort_kurz='Ja' if liegt else 'Nein')
        return Kern(f'Gegeben ist f: {fs}.', f'Berechne f({z(x0)}).', z(y0), [f'x = {z(x0)} einsetzen', f'f({z(x0)}) = {z(y0)}'], [(z(m * x0 - t), 'Vorzeichen von t falsch')],
                    [check('Einsetzen', f.subs(sx, x0) == y0)])
    if et in ('stelle', 'nullstellen'):
        y0 = 0 if et == 'nullstellen' else nz(rng, 1, 9)
        sol = sp.solve(sp.Eq(f, y0), sx)
        return Kern(f'Gegeben ist f: {fs}.', ('Berechne die Nullstelle von f.' if et == 'nullstellen' else f'Für welches x gilt f(x) = {z(y0)}?'), f'x = {z(sol[0])}',
                    [f'{term(f)} = {z(y0)}', f'x = {z(sol[0])}'], [(f'x = {z(-sol[0])}', 'Vorzeichenfehler'), (f'x = {z(t)}', 'y-Achsenabschnitt statt Nullstelle')], [check('Einsetzen', f.subs(sx, sol[0]) == y0)])
    if et in ('wertetabelle', 'graph_lesen', 'ablesen', 'graph_ablesen'):
        xs = [-2, 0, 2, 4]
        ys = [f.subs(sx, x) for x in xs]
        if et == 'wertetabelle':
            return Kern(f'Gegeben ist f: {fs}.', 'Lege eine Wertetabelle für x ∈ {−2; 0; 2; 4} an und zeichne den Graphen.', '; '.join(f'({x} | {z(y)})' for x, y in zip(xs, ys)),
                        ['x einsetzen, Punkte eintragen, mit dem Lineal verbinden.'], [], [check('Werte', all(f.subs(sx, x) == y for x, y in zip(xs, ys)))])
        return Kern('', f'Der Graph einer Geraden g verläuft durch die Punkte ({z(xs[1])} | {z(ys[1])}) und ({z(xs[2])} | {z(ys[2])}) (im Koordinatensystem eingezeichnet). Lies Steigung und y-Achsenabschnitt ab und gib die Gleichung an.',
                    f'm = {z(m)}, t = {z(t)}, {fs}', [f'y-Achsenabschnitt: Schnitt mit der y-Achse bei {z(t)}', f'Steigungsdreieck: {z(ys[2] - ys[1])} nach oben bei 2 nach rechts → m = {z(m)}'],
                    [(f'y = {term(t * sx + m)}', 'm und t vertauscht')], abb=f'Koordinatensystem mit der Geraden durch ({z(xs[1])} | {z(ys[1])}) und ({z(xs[2])} | {z(ys[2])}).',
                    pruef=[check('Punkte auf g', f.subs(sx, xs[2]) == ys[2])])
    if et in ('zwei_punkte', 'aufstellen'):
        x1, x2 = rng.sample(range(-4, 6), 2)
        y1, y2 = f.subs(sx, x1), f.subs(sx, x2)
        mm = (y2 - y1) / (x2 - x1)
        return Kern('', f'Bestimme die Gleichung der Geraden durch A({z(x1)} | {z(y1)}) und B({z(x2)} | {z(y2)}).', fs,
                    [f'm = ({z(y2)} − {zk(y1)}) : ({z(x2)} − {zk(x1)}) = {z(mm)}', f't aus A: {z(y1)} = {z(mm)} · {zk(x1)} + t → t = {z(t)}'],
                    [(f'y = {term(sp.Rational(1) / m * sx + t) if m != 0 else "1"}', 'Steigung als Δx : Δy berechnet')], [check('beide Punkte', f.subs(sx, x1) == y1 and f.subs(sx, x2) == y2 and mm == m)])
    if et == 'lage':
        art = rng.choice(['parallel', 'gleicher_t', 'senkrecht_y'])
        if art == 'parallel':
            t2 = t + nz(rng, 1, 5)
            return Kern(f'Gegeben ist g: {fs}.', 'Gib die Gleichung einer Geraden h an, die parallel zu g ist und durch P(0 | ' + z(t2) + ') geht.', f'h: y = {term(m * sx + t2)}',
                        ['Parallele Geraden haben die gleiche Steigung.', f'y-Achsenabschnitt {z(t2)}'], [(f'y = {term(-m * sx + t2)}', 'Steigung mit Gegenzahl verwechselt')], [wissen('parallel')])
        if art == 'gleicher_t':
            m2 = m + nz(rng, 1, 3)
            return Kern(f'Gegeben ist g: {fs}.', f'Gib die Gleichung einer Geraden h mit der Steigung {z(m2)} an, die die y-Achse im selben Punkt schneidet wie g.', f'h: y = {term(m2 * sx + t)}',
                        [f'Gleicher y-Achsenabschnitt t = {z(t)}'], [(f'y = {term(m2 * sx + m)}', 'Steigung statt y-Achsenabschnitt übernommen')], [wissen('t gleich')])
        xa = nz(rng, 1, 7)
        return Kern('', f'Gib die Gleichung der Geraden an, die durch A({xa} | {nz(rng, 1, 9)}) geht und parallel zur y-Achse verläuft.', f'x = {xa}',
                    ['Parallelen zur y-Achse haben die Form x = konstant.'], [(f'y = {xa}', 'mit Parallele zur x-Achse verwechselt'), (f'y = {xa}x', 'Ursprungsgerade')], [wissen('senkrecht')])
    if et == 'proportional':
        xp, yp = nz(rng, 1, 5), nz(rng, 1, 9)
        mm = sp.Rational(yp, xp)
        return Kern('', f'Eine Ursprungsgerade verläuft durch P({z(xp)} | {z(yp)}). Gib ihre Gleichung an und zeichne sie mit einem Steigungsdreieck.', f'y = {term(mm * sx)}',
                    [f'm = y : x = {z(yp)} : {zk(xp)} = {z(mm)}'], [(f'y = {term(sp.Rational(xp, yp) * sx)}', 'x : y statt y : x')], [check('P auf Gerade', mm * xp == yp)])
    if et in ('deuten', 'sachzusammenhang', 'wirkung', 'mengen'):
        grund = rng.choice([3, 4, Fr(7, 2), Fr(9, 2)])
        km = rng.choice([Fr(3, 2), 2, Fr(5, 2), Fr(9, 5)])
        strecke = rng.randint(4, 25)
        kosten = Fr(grund) + Fr(km) * strecke
        return Kern(f'Eine Taxifahrt kostet {euro(grund)} Grundgebühr und {euro(km)} pro km. Die Kosten werden durch y = {z(km)}x + {z(grund)} beschrieben (x: Strecke in km, y: Preis in €).',
                    f'Was bedeuten {z(km)} und {z(grund)} im Sachzusammenhang? Was kostet eine Fahrt über {strecke} km?', f'{z(km)}: Preis pro km (Steigung); {z(grund)}: Grundgebühr (y-Achsenabschnitt); {euro(kosten)}',
                    ['Steigung = Änderung des Preises je km', 'y-Achsenabschnitt = Preis bei 0 km', f'{z(km)} · {strecke} + {z(grund)} = {z(kosten)}'],
                    [(euro(Fr(km) * strecke), 'Grundgebühr vergessen'), (euro((Fr(grund) + Fr(km)) * strecke), 'Grundgebühr pro km gerechnet')], [check('Kosten', kosten == Fr(grund) + Fr(km) * strecke)])
    return f_funktion(rng, niv, info, 'funktionswert', thema)
