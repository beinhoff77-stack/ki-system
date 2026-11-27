"""Mathe-Profi, Auftrag 5 (Fassung 2): zugeschnittener Papier-Test, 40 Minuten, je Kind Blatt A und Zwilling B.

Aufruf: python3 -I inhalte/mathe-profi/papier-test-1/bauen.py
Rechnet jede Aufgabe auf zwei Wegen nach und schreibt k5-blatt-a.html, k5-blatt-b.html, k8-blatt-a.html, k8-blatt-b.html.
Jede Datei: Blatt (Seiten 1–2), Bewertungsschema, Erfassungsbogen – je auf eigenen Seiten.
Nur Inhalte. Keine Namen, keine Lerndaten, keine Ergebnisse.
"""
import os
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))
M = "−"


def z(n):
    """Zahl mit echtem Minuszeichen."""
    return (M + str(-n)) if n < 0 else str(n)


def k(n):
    """negative Zahl in Klammern"""
    return f"({z(n)})" if n < 0 else str(n)


def fr(a, b):
    return f'<span class="fr"><span>{a}</span><span>{b}</span></span>'


def gleich(f, g, stellen=(-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7), aus=()):
    """Zwei Terme stimmen an mindestens 8 Stellen überein (für die vorkommenden Grade ein Beweis)."""
    pkt = [F(s) for s in stellen if s not in aus]
    assert len(pkt) >= 8
    return all(f(p) == g(p) for p in pkt)


def linear(f):
    """Löst f(x) = 0 für lineares f: zweiter Weg zur Handrechnung."""
    f0, f1, f2 = f(F(0)), f(F(1)), f(F(2))
    assert f2 - f1 == f1 - f0 != 0
    return -f0 / (f1 - f0)


# ───────────────────────────── Klasse 5 ─────────────────────────────
def klasse5(p):
    A = []

    def auf(nr, teil, pkt, gruppe, text, loesung, vergabe, regel, platz):
        A.append(dict(nr=nr, teil=teil, pkt=pkt, gruppe=gruppe, text=text, loesung=loesung, vergabe=vergabe, regel=regel, platz=platz))

    a, b, c = p["a1"]
    e = a + b - c
    assert e == sum([a, b, -c]) and a < 0 and c < 0
    auf("1a", 1, 1, "Rechnen", f"{k(a)} + {b} {M} {k(c)}", f"= {z(a)} + {b} + {-c} = <b>{z(e)}</b>", "1 P für das Ergebnis.",
        f"Zeichen-Paar (minus minus wird plus). Bei {z(a + b + c)}: „{M} ({z(c)})“ als Minus gerechnet.", 2.2)
    assert a + b + c != e

    a, b, c, d = p["b1"]
    e = a - b - c + d
    plus, minus = a - c, b - d
    assert e == plus - minus and c < 0 and d < 0
    auf("1b", 1, 2, "Rechnen", f"{a} {M} {b} {M} {k(c)} + {k(d)}", f"= {a} {M} {b} + {-c} {M} {-d} = {plus} {M} {minus} = <b>{z(e)}</b>",
        "1 P: beide Klammern richtig aufgelöst. 1 P: Ergebnis.", "Zeichen-Paar (Klammern auflösen) oder Richtung (über die Null rechnen).", 2.8)

    a, b, c, d = p["a2"]
    e = a - b * (c - d)
    assert e == a - (b * c - b * d) and e != (a - b) * (c - d)
    auf("2a", 1, 2, "Rechnen", f"{a} {M} {b} · ({c} {M} {d})", f"= {a} {M} {b} · {c - d} = {a} {M} {b * (c - d)} = <b>{z(e)}</b>",
        "1 P: Klammer zuerst, dann Punkt vor Strich (Zwischenschritt sichtbar). 1 P: Ergebnis.",
        f"Rangfolge. Bei {(a - b) * (c - d)}: zuerst {a} {M} {b} gerechnet.", 2.8)

    a, b, c, d = p["b2"]
    e = a * b + c // d
    assert c % d == 0 and e == (a * b) + F(c, d) and a < 0 and c < 0 and d < 0
    auf("2b", 1, 2, "Rechnen", f"{k(a)} · {b} + {k(c)} : {k(d)}", f"= {z(a * b)} + {c // d} = <b>{z(e)}</b>",
        f"1 P: beide Teilergebnisse ({z(a * b)} und {c // d}) mit richtigem Vorzeichen. 1 P: Ergebnis.",
        f"Zeichen-Paar bei mal und geteilt. Bei {z(a * b - c // d)}: minus durch minus als minus gerechnet.", 2.8)

    a, b, rund = p["g"]
    e = a * b
    assert e == a * rund - a * (rund - b) and 0 < rund - b <= 5
    auf("3", 1, 1, "Rechnen", f"Rechne geschickt und schreibe deinen Weg auf: {a} · {b}",
        f"= {a} · {rund} {M} {a} · {rund - b} = {a * rund} {M} {a * (rund - b)} = <b>{e}</b>",
        "1 P nur, wenn der geschickte Weg dasteht <i>und</i> das Ergebnis stimmt. Schriftliches Malnehmen mit richtigem Ergebnis: 0 P (Weg war verlangt).",
        "Verteilen (Zahl mal Klammer: mit jedem Teil malnehmen).", 2.4)

    a, b = p["e1"]
    x = b + a
    assert x - a == b
    auf("4a", 1, 1, "Rechnen", f"Löse die Gleichung und mach die Probe: x {M} {a} = {z(b)}", f"x = {z(b)} + {a} = <b>{x}</b>; Probe: {x} {M} {a} = {z(b)} ✓",
        "1 P für x. Die Probe gibt keinen eigenen Punkt; im Bogen vermerken, ob sie dasteht.",
        f"Umkehren. Bei {z(b - a)}: mit Minus statt mit Plus zurückgerechnet.", 2.2)
    a, b = p["e2"]
    x = b // a
    assert a * x == b and a < 0
    auf("4b", 1, 1, "Rechnen", f"Löse die Gleichung: {k(a)} · x = {b}", f"x = {b} : {k(a)} = <b>{z(x)}</b>", "1 P für x.",
        f"Umkehren; bei {-x}: Zeichen-Paar (plus durch minus ist minus).", 2.0)

    wort, s, ziel = p["r"]
    passend = [n for n in range(ziel - 2 * s, ziel + 2 * s) if (n + s // 2) // s * s == ziel]
    lo, hi = min(passend), max(passend)
    assert (lo, hi) == (ziel - s // 2, ziel + s // 2 - 1) and len(passend) == s
    t = f"{ziel:,}".replace(",", " ")
    auf("5", 2, 2, "Umkehren", f"Eine ganze Zahl wurde auf {wort} gerundet. Das Ergebnis ist {t}.<br>Gib die kleinste und die größte Zahl an, die es gewesen sein kann.",
        f"kleinste: <b>{lo:,}</b>; größte: <b>{hi:,}</b>".replace(",", " "), "Je 1 P.",
        f"Stellenwert (Runden: ab 5 aufrunden). Typisch: {hi + 1:,} oder {ziel + s - 1:,} als größte Zahl.".replace(",", " "), 2.2)

    a, b, c = p["f"]
    richtig, falsch = a + b - c, a - b - c
    assert richtig == a - (-b) - c and richtig != falsch
    auf("6", 2, 2, "Fehler finden", "Ein Kind hat so gerechnet. Kreise die Zeile ein, in der der Fehler steckt, und rechne daneben richtig."
        f'<div class="rech">{a} {M} ({z(-b)}) {M} {c}<br>= {a} {M} {b} {M} {c}<br>= {z(falsch)}</div>',
        f"Falsch ist die <b>zweite Zeile</b> (aus „{M} ({z(-b)})“ muss „+ {b}“ werden). Richtig: {a} + {b} {M} {c} = <b>{z(richtig)}</b>",
        "1 P: zweite Zeile markiert. 1 P: richtiges Ergebnis.", "Zeichen-Paar (minus minus wird plus).", 2.8)

    s = p["aussage"]
    assert s["test"]()
    auf("7", 2, 2, "Begründen", f"Jemand behauptet: „{s['text']}“<br>Stimmt das immer? Entscheide und begründe mit einer Rechnung.",
        f"<b>Nein.</b> Gegenbeispiel, zum Beispiel {s['bsp']}. {s['wann']}",
        "1 P: „stimmt nicht“. 1 P: ein Gegenbeispiel mit ausgerechneter Zahl. Nur Beispiele, bei denen es stimmt: 0 P.",
        "Richtung (Rechnen mit negativen Zahlen) – und: Ein Gegenbeispiel genügt.", 3.0)

    t = p["sach"]
    start, n, je, ab = t["zahlen"]
    e = start + n * je - ab
    schritt = start
    for _ in range(n):
        schritt += je
    assert e == schritt - ab and start < 0
    auf("8", 2, 2, "Ansatz aus Text", t["text"] + "<br>Schreibe <u>einen</u> Term für das Ganze und rechne ihn aus.",
        f"{z(start)} + {n} · {je} {M} {ab} = {z(start)} + {n * je} {M} {ab} = <b>{z(e)}{t['einheit']}</b>",
        "1 P: ein Term, der die Rechnung richtig beschreibt (auch mit Klammer um das Produkt). 1 P: Ergebnis mit Einheit. Schritt für Schritt richtig gerechnet, aber kein Term: nur 1 P.",
        f"Rangfolge (Punkt vor Strich) und Richtung. Bei {z((start + n) * je - ab)}: von links nach rechts gerechnet. Mischt die Themen zahlen.ganz und zahlen.rechengesetze.", 3.2)

    a, b, c, d, ziel = p["klammer"]
    wege = {"keine": a * b - c + d, f"{a} · ({b} {M} {c}) + {d}": a * (b - c) + d, f"{a} · {b} {M} ({c} + {d})": a * b - (c + d), f"{a} · ({b} {M} {c} + {d})": a * (b - c + d)}
    treffer = [w for w, v in wege.items() if v == ziel]
    assert treffer == [f"{a} · ({b} {M} {c}) + {d}"] and len(set(wege.values())) == 4
    auf("9", 2, 1, "Umkehren", f"Setze ein Klammerpaar so, dass die Rechnung stimmt:<br><span class='gross'>{a} · {b} {M} {c} + {d} = {z(ziel)}</span>",
        f"<b>{treffer[0]}</b> = {a} · {k(b - c)} + {d} = {z(ziel)}", "1 P für die richtige Klammer. (Die drei anderen Möglichkeiten ergeben "
        + ", ".join(z(v) for w, v in wege.items() if v != ziel) + ".)", "Rangfolge (Klammer zuerst).", 2.0)

    a, b, c, d = p["term"]
    e = (a - b) * (c + d)
    assert e == a * c + a * d - b * c - b * d and c < 0
    auf("10", 2, 1, "Ansatz aus Text", f"Schreibe als Term und rechne aus:<br>Multipliziere die Differenz aus {a} und {b} mit der Summe aus {z(c)} und {d}.",
        f"({a} {M} {b}) · ({z(c)} + {d}) = {k(a - b)} · {k(c + d)} = <b>{e}</b>", "1 P nur für Term mit beiden Klammern <i>und</i> Ergebnis.",
        f"Rangfolge (Klammern fehlen) oder Zeichen-Paar (minus mal minus). Ohne Klammern käme {z(a - b * c + d)} heraus.", 2.4)
    return A


def aussage_plus():
    assert all(a + b > max(a, b) for a in range(1, 9) for b in range(1, 9)) and not (5 + (-3) > 5) and 5 + (-3) == 2
    return True


def aussage_minus():
    assert all(a - b < a for a in range(-5, 9) for b in range(1, 9)) and not (5 - (-2) < 5) and 5 - (-2) == 7
    return True


K5 = {
    "A": dict(a1=(-17, 9, -14), b1=(23, 41, -6, -12), a2=(50, 6, 13, 5), b2=(-4, 7, -36, -9), g=(6, 197, 200), e1=(38, -15), e2=(-6, 84),
              r=("Hunderter", 100, 4700), f=(12, 5, 20),
              aussage=dict(text="Wenn man zwei Zahlen addiert, ist das Ergebnis immer größer als jede der beiden Zahlen.", bsp=f"5 + ({M}3) = 2, und 2 ist kleiner als 5",
                           wann="Es stimmt nur, wenn beide Zahlen positiv sind. Auch ein Beispiel mit 0 zählt (5 + 0 = 5 ist nicht größer).", test=aussage_plus),
              sach=dict(zahlen=(-7, 5, 3, 11), einheit=" °C", text=f"Um 6 Uhr sind es {M}7 °C. Danach steigt die Temperatur 5 Stunden lang jede Stunde um 3 Grad. Am Abend fällt sie um 11 Grad."),
              klammer=(4, 6, 9, 2, -10), term=(4, 10, -8, 3)),
    "B": dict(a1=(-23, 8, -19), b1=(31, 52, -7, -15), a2=(60, 7, 12, 4), b2=(-6, 8, -45, -5), g=(8, 296, 300), e1=(47, -18), e2=(-7, 91),
              r=("Tausender", 1000, 38000), f=(9, 8, 25),
              aussage=dict(text="Wenn man von einer Zahl eine andere Zahl abzieht, ist das Ergebnis immer kleiner als die erste Zahl.", bsp=f"5 {M} ({M}2) = 7, und 7 ist größer als 5",
                           wann="Es stimmt nur, wenn die abgezogene Zahl positiv ist. Auch ein Beispiel mit 0 zählt (5 − 0 = 5 ist nicht kleiner).", test=aussage_minus),
              sach=dict(zahlen=(-12, 4, 6, 17), einheit=" €", text=f"Auf einem Konto sind {M}12 €. Danach kommen 4 Wochen lang jede Woche 6 € dazu. Am Ende werden 17 € abgebucht."),
              klammer=(5, 3, 8, 4, -21), term=(2, 9, -6, 2)),
}


# ───────────────────────────── Klasse 8 ─────────────────────────────
def klasse8(p):
    A = []

    def auf(nr, teil, pkt, gruppe, text, loesung, vergabe, regel, platz):
        A.append(dict(nr=nr, teil=teil, pkt=pkt, gruppe=gruppe, text=text, loesung=loesung, vergabe=vergabe, regel=regel, platz=platz))

    def lin(a, b, v="x"):
        """a·x + b als Text"""
        ax = "" if a == 0 else (v if a == 1 else M + v if a == -1 else f"{z(a)}{v}")
        if b == 0:
            return ax
        return f"{ax} {'+' if b > 0 else M} {abs(b)}" if ax else z(b)

    a, b, c, d, e, g = p["t1"]          # a x − b(c x − d) − (e − g x)
    A1, B1 = a - b * c + g, b * d - e
    assert gleich(lambda x: a * x - b * (c * x - d) - (e - g * x), lambda x: A1 * x + B1)
    gx = "x" if g == 1 else f"{g}x"
    auf("1", 1, 2, "Rechnen", f"Vereinfache so weit wie möglich: {a}x {M} {b}({c}x {M} {d}) {M} ({e} {M} {gx})",
        f"= {a}x {M} {b * c}x + {b * d} {M} {e} + {gx} = <b>{lin(A1, B1)}</b>",
        "1 P: beide Klammern richtig aufgelöst (alle vier Vorzeichen). 1 P: richtig zusammengefasst. Folgefehler: Ist nur ein Vorzeichen falsch und danach richtig zusammengefasst, 1 P.",
        f"Minusklammer oder Verteilen. Typisch: {M} {b * d} statt + {b * d}, oder {M} {gx} statt + {gx}.", 3.0)

    a, b, c, d, e, g = p["g2"]          # a(x − b) − c = d(x + e) + g
    x = linear(lambda t: a * (t - b) - c - (d * (t + e) + g))
    assert x == F(d * e + g + a * b + c, a - d) and x.denominator == 1 and a * (x - b) - c == d * (x + e) + g
    L, R = -a * b - c, d * e + g
    auf("2", 1, 2, "Rechnen", f"Löse die Gleichung: {a}(x {M} {b}) {M} {c} = {d}(x + {e}) + {g}",
        f"{lin(a, L)} = {lin(d, R)} &nbsp;→&nbsp; {a - d}x = {R - L} &nbsp;→&nbsp; <b>x = {x}</b> (Probe: beide Seiten {a * (x - b) - c})",
        "1 P: Klammern aufgelöst und zusammengefasst (Zeile ohne Klammern stimmt). 1 P: x. Folgefehler: Aus einer falschen Zeile richtig weitergerechnet gibt den zweiten Punkt.",
        "Verteilen (Klammer) oder Waage (auf beiden Seiten dasselbe).", 3.6)

    m, n = p["k3"]                      # (m x + m n)/(x² + n x) = m/x
    assert gleich(lambda x: (m * x + m * n) / (x * x + n * x), lambda x: F(m) / x, aus=(0, -n))
    vz = "+" if n > 0 else M
    auf("3a", 1, 1, "Rechnen", f"Kürze so weit wie möglich: {fr(f'{m}x {vz} {m * abs(n)}', f'x² {vz} {abs(n)}x')}",
        f"= {fr(f'{m}(x {vz} {abs(n)})', f'x(x {vz} {abs(n)})')} = <b>{fr(m, 'x')}</b>",
        "1 P für das Ergebnis; das Ausklammern muss zu sehen sein.", "Bruchrechnen (nur Faktoren kürzen) – vorher Verteilen rückwärts (ausklammern). Typisch: einzelne Summanden „weggekürzt“.", 3.0)

    a, b, n = p["a3"]                   # a/x + b/(x + n)
    Z1, Z0 = a + b, a * n
    assert gleich(lambda x: F(a) / x + F(b) / (x + n), lambda x: (Z1 * x + Z0) / (x * (x + n)), aus=(0, -n))
    xn = f"x {'+' if n > 0 else M} {abs(n)}"
    auf("3b", 1, 2, "Rechnen", f"Schreibe als einen Bruch: {fr(a, 'x')} + {fr(b, xn)}",
        f"= {fr(f'{a}({xn}) + {b}x', f'x({xn})')} = <b>{fr(lin(Z1, Z0), f'x({xn})')}</b> &nbsp;(Nenner auch ausmultipliziert richtig: x² {'+' if n > 0 else M} {abs(n)}x)",
        "1 P: gemeinsamer Nenner und beide Zähler richtig erweitert. 1 P: Zähler zusammengefasst.",
        f"Bruchrechnen (Hauptnenner). Typisch: {fr(a + b, f'2x {chr(43) if n > 0 else M} {abs(n)}')} – Zähler und Nenner einfach addiert.", 3.4)

    c, ea, vb, eb, zus_v, zus_e = p["p4"]   # (c a^ea b^eb)² · v^e
    exp = {"a": 2 * ea, "b": 2 * eb}
    exp[zus_v] += zus_e
    assert exp == p["p4_erg"]

    def wert(a_, b_):
        return (c * F(a_) ** ea * F(b_) ** eb) ** 2 * {"a": F(a_), "b": F(b_)}[zus_v] ** zus_e

    assert all(wert(a_, b_) == c * c * F(a_) ** exp["a"] * F(b_) ** exp["b"] for a_ in (2, 3, -2) for b_ in (2, 5, -3))
    hoch = {2: "²", 3: "³", 4: "⁴", 5: "⁵", 6: "⁶", -2: "⁻²", -3: "⁻³", -4: "⁻⁴", -6: "⁻⁶", 1: ""}
    zae = "".join(f"{v}{hoch[x]}" for v, x in exp.items() if x > 0)
    nen = "".join(f"{v}{hoch[-x]}" for v, x in exp.items() if x < 0)
    auf("4", 1, 1, "Rechnen", f"Vereinfache. Im Ergebnis darf kein negativer Exponent stehen: ({c}{'a' + hoch[ea]}{'b' + hoch[eb]})² · {zus_v}{hoch[zus_e]}",
        f"= {c * c}{'a' + hoch[2 * ea]}{'b' + hoch[2 * eb]} · {zus_v}{hoch[zus_e]} = <b>{fr(f'{c * c}{zae}', nen)}</b>",
        "1 P für das Ergebnis als Bruch.", f"Potenz. Typisch: {c * 2} statt {c * c} (Zahl nicht mitquadriert) oder Exponenten addiert statt malgenommen.", 2.6)

    a, m, b, n = p["b5"]                # a/(x − m) = b/(x + n)
    x = linear(lambda t: a * (t + n) - b * (t - m))
    assert x.denominator == 1 and x not in (m, -n) and F(a) / (x - m) == F(b) / (x + n)
    auf("5", 1, 2, "Rechnen", f"Gib die Definitionsmenge an und löse: {fr(a, f'x {M} {m}')} = {fr(b, f'x + {n}')}",
        f"D = ℚ ohne {{{z(-n)}; {m}}}. Über Kreuz: {a}(x + {n}) = {b}(x {M} {m}) → {a}x + {a * n} = {b}x {M} {b * m} → {a - b}x = {z(-b * m - a * n)} → <b>x = {z(int(x))}</b> (liegt in D)",
        "1 P: Definitionsmenge (beide ausgeschlossenen Zahlen). 1 P: x. Folgefehler wie bei Aufgabe 2.",
        "Verhältnis (über Kreuz) und Verteilen. Fehlt die Definitionsmenge: Bruchrechnen (Nenner darf nicht 0 sein).", 3.8)

    a, b, c, d, e = p["f6"]             # a − b(x − c) = d x − e
    xr = linear(lambda t: a - b * (t - c) - (d * t - e))
    xf = F(e + a - b * c, b + d)
    assert xr.denominator == 1 and xf != xr and xr == F(a + b * c + e, b + d)
    auf("6", 2, 2, "Fehler finden", "In dieser Lösung steckt ein Fehler. Kreise die <u>erste</u> falsche Zeile ein und löse die Gleichung daneben richtig."
        f'<div class="rech">{a} {M} {b}(x {M} {c}) = {d}x {M} {e}<br>{a} {M} {b}x {M} {b * c} = {d}x {M} {e}<br>{a - b * c} {M} {b}x = {d}x {M} {e}<br>{a - b * c + e} = {b + d}x<br>x = {fr(xf.numerator, xf.denominator)}</div>',
        f"Falsch ist die <b>zweite Zeile</b>: {M} {b} · ({M}{c}) ist + {b * c}. Richtig: {a + b * c} {M} {b}x = {d}x {M} {e} → {a + b * c + e} = {b + d}x → <b>x = {xr}</b>",
        "1 P: zweite Zeile markiert. 1 P: richtige Lösung.", "Minusklammer (Minus mal Minus beim Auflösen).", 3.6)

    u, v, w = p["u7"]                   # nicht definiert bei u und v, Wert w bei 0
    zaehler = w * u * v
    assert pruefe7(lambda x: F(zaehler), lambda x: (x - u) * (x - v), u, v, w)
    assert not pruefe7(lambda x: F(w), lambda x: (x - u) * (x - v), u, v, w) and not pruefe7(lambda x: F(zaehler), lambda x: (x - u), u, v, w)
    auf("7", 2, 2, "Umkehren", f"Gib einen Bruchterm an, der für x = {z(u)} und für x = {z(v)} nicht definiert ist und für x = 0 den Wert {w} hat.",
        f"Zum Beispiel <b>{fr(z(zaehler), f'(x {M} {u})(x + {-v})')}</b>: für x = 0 ist der Nenner {z(u * v)}, also {z(zaehler)} : ({z(u * v)}) = {w}. Viele andere Lösungen sind möglich.",
        f"So prüfen: (1) {z(u)} in den Nenner einsetzen → 0? (2) {z(v)} einsetzen → 0? (3) 0 in den ganzen Term einsetzen → {w}? 1 P für (1) und (2) zusammen, 1 P für (3).",
        "Nullprodukt (Nenner aus zwei Faktoren bauen) und Einsetzen. Bleibt die Aufgabe leer: Sie verlangt Rückwärtsdenken, nicht Rechnen.", 3.2)

    a, b = p["b8"]                      # (x + a)/(x + b) angeblich = a/b
    q = F(a, b)
    assert q.denominator == 1 and F(0 + a, 0 + b) == q and all(F(t + a, t + b) != q for t in (1, 2, 3, -1, 5))
    auf("8", 2, 2, "Begründen", f"Jemand kürzt {fr(f'x + {a}', f'x + {b}')} zu {q}.<br>Zeige mit einer Zahl, dass das falsch ist. Erkläre in einem Satz, warum man hier nicht kürzen darf.",
        f"Zum Beispiel x = 1: {fr(1 + a, 1 + b)} ist nicht {q}. Kürzen darf man nur gemeinsame <b>Faktoren</b>; hier stehen Summen, {a} und {b} sind Summanden.",
        f"1 P: eine Zahl, bei der es nicht {q} ergibt, ausgerechnet. 1 P: Satz mit „Summe“/„kein Faktor“/„nicht aus Summen kürzen“. <b>Achtung:</b> x = 0 ergibt zufällig {q} – das ist kein Gegenbeispiel (0 P für diesen Teil).",
        "Bruchrechnen (aus Summen kürzen) und Einsetzen und Probe.", 3.4)

    d, s, zu = p["r9"]                  # Länge = Breite + d; beide + s; Fläche wächst um zu
    x = linear(lambda t: (t + s) * (t + d + s) - t * (t + d) - zu)
    assert x.denominator == 1 and x > 0 and (x + s) * (x + d + s) - x * (x + d) == zu and x == F(zu - s * (d + s), 2 * s)
    auf("9", 2, 3, "Ansatz aus Text", f"Ein Rechteck ist {d} cm länger als breit. Verlängert man beide Seiten um {s} cm, so wächst der Flächeninhalt um {zu} cm².<br>Wie breit ist das Rechteck? Stelle eine Gleichung auf und löse sie.",
        f"Breite x, Länge x + {d}. (x + {s})(x + {d + s}) {M} x(x + {d}) = {zu} → x² + {d + 2 * s}x + {s * (d + s)} {M} x² {M} {d}x = {zu} → {2 * s}x + {s * (d + s)} = {zu} → <b>x = {x} cm</b>. Probe: {x}·{x + d} = {x * (x + d)}, {x + s}·{x + d + s} = {(x + s) * (x + d + s)}, Unterschied {zu} ✓",
        "1 P: Gleichung richtig aufgestellt (auch als „neu = alt + " + str(zu) + "“). 1 P: ausmultipliziert, x² fällt weg. 1 P: x mit Einheit. Durch Probieren gefunden und mit Probe belegt: 2 P.",
        "Verteilen (Summe mal Summe) und Waage. Steht keine Gleichung da: der Ansatz fehlt, nicht das Rechnen. Mischt terme.umformen und gleichungen.linear.", 5.0)

    liste = p["o10"]
    werte = sorted(liste, key=lambda t: t[1])
    assert len({t[1] for t in liste}) == 4 and [t[1] for t in werte] == sorted(t[1] for t in liste) and werte != liste
    for _txt, w, (ba, ex) in liste:
        assert F(ba) ** ex == w          # zweiter Weg: Potenz ausgerechnet

    def bruchtext(w):
        return str(w.numerator) if w.denominator == 1 else f"{w.numerator}/{w.denominator}"

    auf("10", 2, 1, "Verfahren wählen", "Ordne der Größe nach, beginne mit der kleinsten Zahl: &nbsp; " + " &nbsp;;&nbsp; ".join(t[0] for t in liste),
        " &lt; ".join(f"{t[0]} = {bruchtext(F(t[1]))}" for t in werte), "1 P nur für die ganz richtige Reihenfolge.",
        "Potenz (negativer Exponent heißt Kehrwert, nicht negative Zahl; hoch 0 ist 1).", 2.4)
    return A


def pruefe7(zaehler, nenner, u, v, w):
    """Bedingungs-Prüfung der offenen Umkehraufgabe: Nenner 0 bei u und v, Termwert w bei 0."""
    if nenner(F(u)) != 0 or nenner(F(v)) != 0 or nenner(F(0)) == 0:
        return False
    return zaehler(F(0)) / nenner(F(0)) == w


K8 = {
    "A": dict(t1=(4, 3, 2, 5, 7, 1), g2=(5, 2, 3, 2, 4, 6), k3=(3, -4), a3=(2, 3, 1), p4=(2, -3, "b", 2, "a", 4), p4_erg={"a": -2, "b": 4},
              b5=(6, 2, 4, 1), f6=(7, 2, 3, 3, 12), u7=(3, -1, 2), b8=(6, 2), r9=(4, 3, 51),
              o10=[("2⁻³", F(1, 8), (2, -3)), ("(½)⁻²", F(4), (F(1, 2), -2)), (f"({M}2)⁻²", F(1, 4), (-2, -2)), ("4⁰", F(1), (4, 0))]),
    "B": dict(t1=(5, 2, 3, 4, 9, 2), g2=(4, 3, 5, 2, 1, 3), k3=(5, 2), a3=(3, 2, -1), p4=(3, -2, "b", 1, "a", 1), p4_erg={"a": -3, "b": 2},
              b5=(8, 3, 6, 2), f6=(9, 3, 2, 2, 15), u7=(2, -3, 1), b8=(8, 4), r9=(5, 2, 38),
              o10=[("5⁻¹", F(1, 5), (5, -1)), ("(⅕)⁻²", F(25), (F(1, 5), -2)), (f"({M}5)⁻²", F(1, 25), (-5, -2)), ("5⁰", F(1), (5, 0))]),
}

# ───────────────────────────── Ausgabe ─────────────────────────────
PLATZ = {5: 0.80, 8: 0.68}   # Faktor für den Rechenplatz, damit das Blatt auf zwei Seiten passt

CSS = """@page{size:A4;margin:16mm 15mm}
body{font:12pt/1.4 Georgia,'Times New Roman',serif;color:#000;margin:0}
h1{font-size:15pt;margin:0 0 2mm} h2{font-size:12.5pt;margin:5mm 0 2mm;border-bottom:1px solid #000}
.seite{page-break-after:always} .seite:last-child{page-break-after:auto}
.kopf{display:flex;justify-content:space-between;font-size:10.5pt;border:1px solid #000;padding:2mm 3mm;margin-bottom:3mm}
.regeln{font-size:10.5pt;margin:0 0 3mm}
.auf{display:flex;gap:3mm;page-break-inside:avoid;border-top:1px dotted #777;padding-top:1.5mm}
.auf .nr{width:9mm;font-weight:bold} .auf .tx{flex:1} .auf .p{width:11mm;text-align:right;font-size:10pt;white-space:nowrap}
.fr{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;margin:0 .15em;font-size:.95em}
.fr span:first-child{border-bottom:1px solid #000;padding:0 .25em} .fr span:last-child{padding:0 .25em}
.rech{margin:2mm 0 0 6mm;padding:1.5mm 4mm;border-left:2px solid #000;line-height:1.9;display:table}
.gross{font-size:13.5pt;letter-spacing:.5px}
table{border-collapse:collapse;width:100%;font-size:9.5pt;line-height:1.3} td,th{border:1px solid #000;padding:1.2mm 1.6mm;vertical-align:top;text-align:left}
th{background:#eee} .schema td .fr{font-size:.9em} .klein{font-size:9.5pt} .bogen td{height:8.5mm}
ul{margin:1mm 0 2mm 5mm;padding-left:4mm}"""


def html(klasse, blatt, A, themen):
    kurz = f"K{klasse}-{blatt}"
    t1 = sum(a["pkt"] for a in A if a["teil"] == 1)
    t2 = sum(a["pkt"] for a in A if a["teil"] == 2)
    assert t1 == t2 == 10, (kurz, t1, t2)

    def teil(n, titel):
        out = [f"<h2>Teil {n}: {titel}</h2>"]
        for a in A:
            if a["teil"] == n:
                out.append(f'<div class="auf"><div class="nr">{a["nr"]}</div><div class="tx">{a["text"]}<div style="height:{a["platz"] * PLATZ[klasse]:.2f}cm"></div></div><div class="p">/ {a["pkt"]} P</div></div>')
        return "\n".join(out)

    kopf = f'<div class="kopf"><span>Mathematik · Papier-Test 1 · Blatt {kurz}</span><span>Datum: __________</span><span>Punkte: ____ / 20</span></div>'
    blatt_html = f"""<div class="seite"><h1>Papier-Test Klasse {klasse}</h1>{kopf}
<p class="regeln"><b>40 Minuten.</b> Ohne Taschenrechner, ohne Formelsammlung, ohne Hilfe. Geodreieck und Zirkel sind erlaubt.
<b>Schreibe deinen Rechenweg auf</b> – er wird mitbewertet. Fang mit den Aufgaben an, die dir leichtfallen. Streiche Falsches durch, radiere nicht. Reicht der Platz nicht, rechne auf einem Extrablatt weiter und schreib die Aufgabennummer dazu.</p>
{teil(1, "Rechnen mit Rechenweg")}
{teil(2, "Umdrehen, begründen, selbst ansetzen")}
<p class="klein">Fertig? Schreib oben rechts auf, wie viele Minuten du gebraucht hast.</p></div>"""

    zeilen = "".join(f'<tr><td><b>{a["nr"]}</b></td><td>{a["pkt"]}</td><td>{a["loesung"]}</td><td>{a["vergabe"]}</td><td>{a["regel"]}</td></tr>' for a in A)
    schema = f"""<div class="seite"><h1>Bewertungsschema – Blatt {kurz}</h1>
<p class="klein"><b>Für Erwachsene, auch ohne Mathe-Ausbildung. Aufwand etwa 15–20 Minuten.</b> Stoff (Themen der App): {themen}.</p>
<ul class="klein"><li>Nur ganze Punkte. Jede Spalte „Lösung“ zeigt einen Weg; andere richtige Wege zählen genauso.</li>
<li><b>Rechenweg:</b> Bei Aufgaben mit 2 oder 3 Punkten gibt ein richtiges Ergebnis ganz ohne Weg nur 1 Punkt.</li>
<li><b>Folgefehler:</b> Jeder Fehler kostet nur einmal. Wer nach einem Fehler mit der falschen Zahl richtig weiterrechnet, bekommt die späteren Punkte.</li>
<li>Vorzeichen, Einheit oder Klammer vergessen und dadurch falsch: Punkt für das Ergebnis weg. Reine Schreibweise (z. B. „·“ fehlt) kostet nichts.</li>
<li>Im Zweifel: Punkt nicht geben und die Aufgabe im Bogen mit „?“ kennzeichnen.</li>
<li>Letzte Spalte: welche Grundregel vermutlich fehlt, wenn die Aufgabe falsch ist. Das ist eine Vermutung, kein Urteil.</li></ul>
<table class="schema"><tr><th>Nr.</th><th>P</th><th style="width:36%">Lösung</th><th style="width:27%">Punkte gibt es für</th><th>Wenn falsch, dann vermutlich Regel …</th></tr>{zeilen}</table></div>"""

    bz = "".join(f'<tr><td><b>{a["nr"]}</b></td><td>{a["teil"]}</td><td>{a["gruppe"]}</td><td>{a["pkt"]}</td><td></td><td>ja / nein</td><td></td></tr>' for a in A)
    bogen = f"""<div class="seite"><h1>Erfassungsbogen – Blatt {kurz}</h1>
<p class="klein">Datum: __________ &nbsp; Gebrauchte Zeit: ____ Min. &nbsp; Bewertet von: __________ &nbsp; Bis zu welcher Aufgabe gekommen: ____<br>
Dieser Bogen wird ausgefüllt <b>nicht</b> ins Repo gelegt. Ergebnisse gehen nur an den Nutzer.</p>
<table class="bogen"><tr><th>Teilaufgabe</th><th>Teil</th><th>Tätigkeit</th><th>max.</th><th>erreicht</th><th>Rechenweg sichtbar</th><th style="width:34%">vermutete Regel (aus dem Schema, nur wenn Punkte fehlen)</th></tr>{bz}
<tr><td colspan="3"><b>Teil 1 „wie in der App“</b></td><td>10</td><td></td><td colspan="2"></td></tr>
<tr><td colspan="3"><b>Teil 2 „weiter“</b></td><td>10</td><td></td><td colspan="2"></td></tr>
<tr><td colspan="3"><b>Gesamt</b></td><td>20</td><td></td><td colspan="2"></td></tr></table>
<p class="klein"><b>Lesen:</b> Teil 1 klar über Teil 2 → Das Kind kann die Verfahren, aber noch nicht umdrehen, begründen und selbst ansetzen. Beide niedrig → Die App-Quote misst zu großzügig (Tipps, zweiter Versuch, Auswahl).
Beide hoch → Stoff sitzt auch auf Papier. Nicht fertig geworden → zuerst das Tempo ansehen, nicht den Stoff.<br>
Zwilling: Blatt {'B' if blatt == 'A' else 'A'} hat dieselben Muster mit anderen Zahlen. Abstand vier bis sechs Wochen; bis dahin nicht zeigen.</p></div>"""
    return f'<!doctype html><html lang="de"><meta charset="utf-8"><title>Papier-Test 1 · {kurz}</title><style>{CSS}</style><body>{blatt_html}{schema}{bogen}</body></html>'


THEMEN = {5: "<code>zahlen.ganz</code>, <code>zahlen.rechengesetze</code>, <code>zahlen.natuerlich</code> (nur Runden)",
          8: "<code>terme.umformen</code>, <code>gleichungen.linear</code>, <code>terme.bruchterme</code>, <code>gleichungen.bruch</code>, <code>terme.potenzgesetze_ganzzahlig</code>"}

if __name__ == "__main__":
    for klasse, daten, bau in ((5, K5, klasse5), (8, K8, klasse8)):
        blaetter = {b: bau(p) for b, p in daten.items()}
        # Zwilling: gleiche Muster, gleiche Punkte, andere Zahlen
        assert [(a["nr"], a["teil"], a["pkt"], a["gruppe"]) for a in blaetter["A"]] == [(a["nr"], a["teil"], a["pkt"], a["gruppe"]) for a in blaetter["B"]]
        assert all(x["text"] != y["text"] and x["loesung"] != y["loesung"] for x, y in zip(blaetter["A"], blaetter["B"]))
        for b, A in blaetter.items():
            with open(os.path.join(HIER, f"k{klasse}-blatt-{b.lower()}.html"), "w", encoding="utf-8") as f:
                f.write(html(klasse, b, A, THEMEN[klasse]))
            print(f"K{klasse}-{b}: {len(A)} Teilaufgaben, {sum(a['pkt'] for a in A)} Punkte")
    print("OK")
