"""Mathe-Profi, Auftrag 6: Gegenprüfung der Auswahl (20 Aufgabentypen).

Aufruf: python3 -I inhalte/mathe-profi/gegenpruefung_probe.py
Teil 1  Bedingungs-Prüfung `pruefe2` (Erweiterung von `pruefe` aus massstab_probe.py) für die Typen 6, 7, 8, 9, 15,
        je Typ zwei Musteraufgaben Klasse 5 und zwei Klasse 8, mit guten und schlechten Antworten.
Teil 2  Typ 3 „Rechenweg zusammenbauen“: Prüfregel `pruefe_weg` und drei Musteraufgaben.
Teil 3  Nachweis zu Frage 2: Das Beispiel mit vier fertigen Karten lässt sich ohne Rechnen ordnen.
Nur Inhalte, keine Lerndaten.
"""
from fractions import Fraction as F
from itertools import combinations, product
from statistics import median


def zahl(s, ganz=False):
    try:
        t = str(s).replace("−", "-").replace(",", ".").replace(" ", "")
        w = F(t)
    except (ValueError, ZeroDivisionError):
        return None
    return None if ganz and w.denominator != 1 else w


def pruefe2(m, antwort):
    """Felder lesen, dann Bedingungen der Reihe nach. Neu gegenüber `pruefe`:
    Feldart 'wahl' (eine von mehreren Aussagen), 'menge' (Bausteine ankreuzen), Rückgabe eines Hinweises mit Zahl."""
    if not isinstance(antwort, list) or len(antwort) != len(m["felder"]):
        return {"format_ok": False}
    werte = []
    for a, f in zip(antwort, m["felder"]):
        if f in ("ganz", "rational"):
            w = zahl(a, ganz=f == "ganz")
        elif f.startswith("wahl:"):
            w = a if a in f[5:].split("|") else None
        elif f == "menge":
            w = frozenset(a) if isinstance(a, (list, set, frozenset)) and set(a) <= set(m["bausteine"]) else None
        else:
            raise ValueError(f)
        if w is None:
            return {"format_ok": False}
        werte.append(w)
    for name, bed in m["bedingungen"]:
        try:
            ok = bed(*werte)
        except ZeroDivisionError:
            ok = False
        if ok is not True:
            return {"format_ok": True, "richtig": False, "verletzt": name, **({"hinweis": ok} if isinstance(ok, str) else {})}
    return {"format_ok": True, "richtig": True}


def steckbrief(m):
    """Typ 9: Die angekreuzten Bausteine müssen auf das Ziel passen und auf nichts sonst in der Grundmenge."""
    def bed(gewaehlt):
        if not gewaehlt or len(gewaehlt) > m["hoechstens"]:
            return f"wähle 1 bis {m['hoechstens']} Bausteine"
        if not all(m["bausteine"][b](m["ziel"]) for b in gewaehlt):
            return "ein Baustein stimmt für die gesuchte Zahl nicht"
        auch = [g for g in m["grundmenge"] if g != m["ziel"] and all(m["bausteine"][b](g) for b in gewaehlt)]
        return True if not auch else f"passt auch auf {m['zeige'](auch[0])}"
    return bed


def immer_oder_zufall(links, rechts, wahr, n):
    """Typ 15: erst Urteil, dann – wenn 'nicht immer' – ein Gegenbeispiel, bei dem beide Seiten verschieden sind."""
    def bed(urteil, *z):
        if wahr:
            return True if urteil == "immer" else "Rechne deine Zahlen nach: Beide Seiten sind gleich. Findest du überhaupt ein Gegenbeispiel?"
        if urteil == "immer":
            return "Es gibt Zahlen, bei denen die Seiten verschieden sind."
        l, r = links(*z), rechts(*z)
        return True if l != r else f"Bei deinen Zahlen sind beide Seiten gleich ({l}). Das ist Zufall – nimm andere Zahlen."
    return bed


G = [(a, b, c) for a in range(-4, 5) for b in range(-4, 5) for c in range(-4, 5)]
sechs_gl = {  # Grundmenge für K8-Steckbrief: (a, b, c, d) steht für a·x + b = c·x + d
    "3x − 6 = x + 2": (3, -6, 1, 2), "2x + 5 = 2x − 1": (2, 5, 2, -1), "4x + 8 = 0": (4, 8, 0, 0),
    "5x = 2x": (5, 0, 2, 0), "x − 3 = 3 − x": (1, -3, -1, 3), "2(x + 1) = 2x + 2": (2, 2, 2, 2)}


def loesung(g):
    a, b, c, d = g
    if a == c:
        return "alle" if b == d else "keine"
    return F(d - b, a - c)


sechs_terme = {  # Grundmenge für K8-Steckbrief Bruchterme: (Zähler, Nenner)
    "(x − 1)/(x + 2)": (lambda x: x - 1, lambda x: x + 2), "(x + 2)/(x − 1)": (lambda x: x + 2, lambda x: x - 1),
    "(x − 1)/(x − 2)": (lambda x: x - 1, lambda x: x - 2), "(1 − x)/(x + 2)": (lambda x: 1 - x, lambda x: x + 2),
    "x/(x + 2)": (lambda x: x, lambda x: x + 2), "(x + 1)/(x + 2)": (lambda x: x + 1, lambda x: x + 2)}


def tw(t, x):
    z_, n_ = sechs_terme[t]
    return None if n_(F(x)) == 0 else z_(F(x)) / n_(F(x))


M = {
    # ── Typ 6 Bedingung erfüllen ──
    "6-K5-1": dict(text="Nenne drei verschiedene ganze Zahlen mit der Summe 0. Genau eine davon soll positiv sein.", felder=["ganz"] * 3,
                   bedingungen=[("verschieden", lambda a, b, c: len({a, b, c}) == 3), ("Summe ist 0", lambda a, b, c: a + b + c == 0 or f"deine Summe ist {a + b + c}"),
                                ("genau eine positiv", lambda a, b, c: sum(v > 0 for v in (a, b, c)) == 1)],
                   gut=[[5, -2, -3], [1, 0, -1]], schlecht=[([2, 3, -5], "genau eine positiv"), ([4, -1, -2], "Summe ist 0"), ([0, 0, 0], "verschieden")]),
    "6-K5-2": dict(text="Nenne zwei ganze Zahlen: Ihr Produkt ist −24, ihre Summe ist positiv.", felder=["ganz"] * 2,
                   bedingungen=[("Produkt ist −24", lambda a, b: a * b == -24 or f"dein Produkt ist {a * b}"), ("Summe ist positiv", lambda a, b: a + b > 0 or f"deine Summe ist {a + b}")],
                   gut=[[-3, 8], [12, -2], [24, -1]], schlecht=[([3, -8], "Summe ist positiv"), ([4, 6], "Produkt ist −24")]),
    "6-K8-1": dict(text="Setze a und b so ein, dass die Gleichung a · x + b = 3x − 6 keine Lösung hat.", felder=["rational"] * 2,
                   bedingungen=[("x fällt weg", lambda a, b: a == 3), ("es bleibt eine falsche Aussage", lambda a, b: b != -6 or "bei b = −6 ist jede Zahl Lösung")],
                   gut=[[3, 1], [3, "-6,5"]], schlecht=[([3, -6], "es bleibt eine falsche Aussage"), ([2, 1], "x fällt weg")]),
    "6-K8-2": dict(text="Nenne eine Zahl x, für die der Bruchterm (x + 1)/(x − 2) negativ ist.", felder=["rational"],
                   bedingungen=[("Term ist definiert", lambda x: x != 2), ("Termwert ist negativ", lambda x: (x + 1) / (x - 2) < 0 or f"dein Termwert ist {(x + 1) / (x - 2)}")],
                   gut=[[0], ["1,5"], ["-1/2"]], schlecht=[([2], "Term ist definiert"), ([3], "Termwert ist negativ"), ([-1], "Termwert ist negativ"), ([-4], "Termwert ist negativ")]),
    # ── Typ 7 Datensatz bauen ──
    "7-K5-1": dict(text="Baue eine Liste aus fünf verschiedenen ganzen Zahlen: Die kleinste ist −6, die größte ist 3, die Summe ist −5.", felder=["ganz"] * 5,
                   bedingungen=[("verschieden", lambda *v: len(set(v)) == 5), ("kleinste ist −6", lambda *v: min(v) == -6), ("größte ist 3", lambda *v: max(v) == 3),
                                ("Summe ist −5", lambda *v: sum(v) == -5 or f"deine Summe ist {sum(v)}")],
                   gut=[[-6, -3, -1, 2, 3], [3, 0, -6, 1, -3]], schlecht=[([-6, -2, 0, 1, 3], "Summe ist −5"), ([-6, -6, 1, 3, 3], "verschieden"), ([-7, -1, 0, 1, 2], "kleinste ist −6")]),
    "7-K5-2": dict(text="Baue eine Liste aus vier ganzen Zahlen: Die Summe ist 0, das Produkt ist positiv.", felder=["ganz"] * 4,
                   bedingungen=[("Summe ist 0", lambda *v: sum(v) == 0 or f"deine Summe ist {sum(v)}"),
                                ("Produkt ist positiv", lambda a, b, c, d: a * b * c * d > 0 or f"dein Produkt ist {a * b * c * d}")],
                   gut=[[-3, -1, 1, 3], [5, -5, 2, -2]], schlecht=[([-3, 1, 1, 1], "Produkt ist positiv"), ([0, 0, 0, 0], "Produkt ist positiv"), ([1, 2, 3, 4], "Summe ist 0")]),
    "7-K8-1": dict(text="Baue eine Liste aus fünf ganzen Zahlen: kleinste Zahl −2, Median 3, Mittelwert 5.", felder=["ganz"] * 5,
                   bedingungen=[("kleinste ist −2", lambda *v: min(v) == -2), ("Median ist 3", lambda *v: median(v) == 3 or f"dein Median ist {median(v)}"),
                                ("Mittelwert ist 5", lambda *v: F(sum(v), 5) == 5 or f"dein Mittelwert ist {F(sum(v), 5)}")],
                   gut=[[-2, 0, 3, 10, 14], [3, -2, 3, 3, 18]], schlecht=[([-2, 3, 5, 8, 11], "Median ist 3"), ([-2, 0, 3, 4, 5], "Mittelwert ist 5")]),
    "7-K8-2": dict(text="Baue eine Liste aus vier Zahlen: Mittelwert 0, Median 1, Abstand zwischen kleinster und größter Zahl 10.", felder=["rational"] * 4,
                   bedingungen=[("Mittelwert ist 0", lambda *v: sum(v) == 0 or f"deine Summe ist {sum(v)}"), ("Median ist 1", lambda *v: median(v) == 1 or f"dein Median ist {median(v)}"),
                                ("Abstand ist 10", lambda *v: max(v) - min(v) == 10)],
                   gut=[[-6, 1, 1, 4], [-6, 0, 2, 4]], schlecht=[([-5, 0, 0, 5], "Median ist 1"), ([-4, 1, 1, 2], "Abstand ist 10")]),
    # ── Typ 8 Aufgabe ergänzen ──
    "8-K5-1": dict(text="Ergänze zwei ganze Zahlen, sodass die Rechnung stimmt: (□ − 9) · □ = −20. Die erste Zahl soll positiv sein.", felder=["ganz"] * 2,
                   bedingungen=[("erste Zahl positiv", lambda a, b: a > 0), ("Rechnung stimmt", lambda a, b: (a - 9) * b == -20 or f"bei dir kommt {(a - 9) * b} heraus")],
                   gut=[[5, 5], [4, 4], [7, 10], [13, -5]], schlecht=[([9, 3], "Rechnung stimmt"), ([-1, 2], "erste Zahl positiv"), ([5, -5], "Rechnung stimmt")]),
    "8-K5-2": dict(text="Ergänze zwei ganze Zahlen: □ · 6 − □ = −15. Die erste Zahl soll negativ sein.", felder=["ganz"] * 2,
                   bedingungen=[("erste Zahl negativ", lambda a, b: a < 0), ("Rechnung stimmt", lambda a, b: a * 6 - b == -15 or f"bei dir kommt {a * 6 - b} heraus")],
                   gut=[[-1, 9], [-2, 3], [-3, -3]], schlecht=[([1, 21], "erste Zahl negativ"), ([-2, -3], "Rechnung stimmt")]),
    "8-K8-1": dict(text="Ergänze zwei Zahlen, sodass x = 3 die einzige Lösung ist: □ · (x − 4) = 2x + □", felder=["rational"] * 2,
                   bedingungen=[("x = 3 erfüllt die Gleichung", lambda a, b: a * (3 - 4) == 2 * 3 + b or f"links {a * (3 - 4)}, rechts {6 + b}"),
                                ("nur eine Lösung", lambda a, b: a != 2 or "mit 2 vor der Klammer ist jede Zahl Lösung")],
                   gut=[[1, -7], [-3, -3], ["0,5", "-6,5"]], schlecht=[([2, -8], "nur eine Lösung"), ([1, 7], "x = 3 erfüllt die Gleichung")]),
    "8-K8-2": dict(text="Ergänze zwei Zahlen: Der Bruchterm (x + □)/(x − □) ist für x = 5 nicht definiert und hat für x = 1 den Wert −2.", felder=["rational"] * 2,
                   bedingungen=[("für x = 5 nicht definiert", lambda a, b: b == 5), ("Wert −2 für x = 1", lambda a, b: (1 + a) / (1 - b) == -2 or f"dein Wert ist {(1 + a) / (1 - b)}")],
                   gut=[[7, 5]], schlecht=[([7, -5], "für x = 5 nicht definiert"), ([-9, 5], "Wert −2 für x = 1"), ([1, 5], "Wert −2 für x = 1")]),
    # ── Typ 15 Immer gleich oder Zufall? ──
    "15-K5-1": dict(text="Behauptung: „Tauscht man bei einer Minus-Aufgabe die beiden Zahlen, kommt dasselbe heraus.“ Stimmt das immer? Wenn nicht: Nenne zwei Zahlen, bei denen es nicht stimmt.",
                    felder=["wahl:immer|nicht immer", "ganz", "ganz"], ident=(lambda a, b: a - b, lambda a, b: b - a, False),
                    gut=[["nicht immer", 5, 3], ["nicht immer", -2, 0]], schlecht=[(["nicht immer", 4, 4], "Urteil und Gegenbeispiel"), (["immer", 4, 4], "Urteil und Gegenbeispiel")]),
    "15-K5-2": dict(text="Behauptung: „Statt eine Klammer (b − c) abzuziehen, kann man erst b abziehen und dann c dazuzählen.“ Stimmt das immer? Wenn nicht: Nenne drei Zahlen a, b, c als Gegenbeispiel.",
                    felder=["wahl:immer|nicht immer", "ganz", "ganz", "ganz"], ident=(lambda a, b, c: a - (b - c), lambda a, b, c: a - b + c, True),
                    gut=[["immer", 0, 0, 0]], schlecht=[(["nicht immer", 9, 5, 2], "Urteil und Gegenbeispiel")]),
    "15-K8-1": dict(text="Jemand kürzt (x + 3)/(x + 6) zu 1/2. Stimmt das für jede erlaubte Zahl? Wenn nicht: Nenne eine Zahl, bei der es nicht stimmt.",
                    felder=["wahl:immer|nicht immer", "rational"], ident=(lambda x: (x + 3) / (x + 6), lambda x: F(1, 2), False),
                    gut=[["nicht immer", 1], ["nicht immer", "-3"]], schlecht=[(["nicht immer", 0], "Urteil und Gegenbeispiel"), (["nicht immer", -6], "Urteil und Gegenbeispiel"), (["immer", 0], "Urteil und Gegenbeispiel")]),
    "15-K8-2": dict(text="Behauptung: a⁻² · a⁵ = a³ für jede Zahl a außer 0. Stimmt das immer? Wenn nicht: Nenne ein Gegenbeispiel.",
                    felder=["wahl:immer|nicht immer", "rational"], ident=(lambda a: a ** -2 * a ** 5, lambda a: a ** 3, True),
                    gut=[["immer", 1]], schlecht=[(["nicht immer", 2], "Urteil und Gegenbeispiel")]),
}
for name, m in M.items():
    if "ident" in m:
        l, r, wahr = m["ident"]
        n = len(m["felder"]) - 1
        pkt = [p for p in product([F(v) for v in (-3, -2, -1, 1, 2, 3, 5)], repeat=n)]
        def sicher(f, p):
            try:
                return f(*p)
            except ZeroDivisionError:
                return None
        gleich = [sicher(l, p) == sicher(r, p) for p in pkt]
        assert all(gleich) == wahr, name                      # Behauptung wirklich wahr / wirklich falsch
        if not wahr:
            assert any(gleich) or name == "15-K8-1", name     # es gibt Zufallstreffer – sonst wäre es keine Falle
        m["bedingungen"] = [("Urteil und Gegenbeispiel", immer_oder_zufall(l, r, wahr, n))]
assert (F(0) + 3) / (F(0) + 6) == F(1, 2)                     # der Zufallstreffer bei 15-K8-1 ist x = 0

# ── Typ 9 Steckbrief schreiben ──
quad = {n * n for n in range(1, 8)}
S = {
    "9-K5-1": dict(text="Schreibe einen Steckbrief für −6 aus höchstens drei Bausteinen. Er darf auf keine andere ganze Zahl von −10 bis 10 passen.",
                   grundmenge=list(range(-10, 11)), ziel=-6, hoechstens=3, zeige=lambda g: str(g).replace("-", "−"),
                   bausteine={"ist negativ": lambda n: n < 0, "ist gerade": lambda n: n % 2 == 0, "ist durch 3 teilbar": lambda n: n % 3 == 0,
                              "Betrag größer als 4": lambda n: abs(n) > 4, "liegt links von −3": lambda n: n < -3, "Gegenzahl ist größer als 5": lambda n: -n > 5, "ist kleiner als −7": lambda n: n < -7},
                   gut=[["ist negativ", "ist gerade", "ist durch 3 teilbar"]], schlecht=[(["ist negativ", "ist durch 3 teilbar", "Betrag größer als 4"], "passt auch auf −9")]),
    "9-K5-2": dict(text="Schreibe einen Steckbrief für 36 aus höchstens drei Bausteinen. Er darf auf keine andere Zahl von 1 bis 50 passen.",
                   grundmenge=list(range(1, 51)), ziel=36, hoechstens=3, zeige=str,
                   bausteine={"ist eine Quadratzahl": lambda n: n in quad, "ist gerade": lambda n: n % 2 == 0, "ist durch 3 teilbar": lambda n: n % 3 == 0,
                              "ist zweistellig": lambda n: n >= 10, "Quersumme ist 9": lambda n: sum(map(int, str(n))) == 9, "ist kleiner als 40": lambda n: n < 40, "ist durch 8 teilbar": lambda n: n % 8 == 0},
                   gut=[["ist eine Quadratzahl", "ist gerade", "ist durch 3 teilbar"]], schlecht=[(["ist eine Quadratzahl", "ist gerade"], "passt auch auf 4"), (["Quersumme ist 9", "ist gerade", "ist kleiner als 40"], "passt auch auf 18")]),
    "9-K8-1": dict(text="Sechs Gleichungen liegen aus. Schreibe einen Steckbrief aus höchstens zwei Bausteinen, der nur auf „x − 3 = 3 − x“ passt.",
                   grundmenge=list(sechs_gl), ziel="x − 3 = 3 − x", hoechstens=2, zeige=lambda g: g,
                   bausteine={"hat genau eine Lösung": lambda g: isinstance(loesung(sechs_gl[g]), F), "die Lösung ist positiv": lambda g: isinstance(loesung(sechs_gl[g]), F) and loesung(sechs_gl[g]) > 0,
                              "x = 0 ist eine Lösung": lambda g: loesung(sechs_gl[g]) in ("alle", 0), "die Lösung ist kleiner als 4": lambda g: isinstance(loesung(sechs_gl[g]), F) and loesung(sechs_gl[g]) < 4,
                              "auf beiden Seiten steht ein x": lambda g: sechs_gl[g][0] != 0 and sechs_gl[g][2] != 0},
                   gut=[["die Lösung ist positiv", "die Lösung ist kleiner als 4"]], schlecht=[(["die Lösung ist positiv"], "passt auch auf 3x − 6 = x + 2"), (["hat genau eine Lösung", "die Lösung ist kleiner als 4"], "passt auch auf 4x + 8 = 0")]),
    "9-K8-2": dict(text="Sechs Bruchterme liegen aus. Schreibe einen Steckbrief aus höchstens zwei Bausteinen, der nur auf (x − 1)/(x + 2) passt.",
                   grundmenge=list(sechs_terme), ziel="(x − 1)/(x + 2)", hoechstens=2, zeige=lambda g: g,
                   bausteine={"für x = −2 nicht definiert": lambda t: tw(t, -2) is None, "hat für x = 1 den Wert 0": lambda t: tw(t, 1) == 0,
                              "hat für x = 0 einen negativen Wert": lambda t: tw(t, 0) is not None and tw(t, 0) < 0, "hat für x = 3 einen Wert kleiner als 1": lambda t: tw(t, 3) is not None and tw(t, 3) < 1,
                              "hat für x = 4 einen positiven Wert": lambda t: tw(t, 4) is not None and tw(t, 4) > 0, "hat für x = 2 den Wert 1": lambda t: tw(t, 2) == 1},
                   gut=[["für x = −2 nicht definiert", "hat für x = 0 einen negativen Wert"]], schlecht=[(["für x = −2 nicht definiert", "hat für x = 1 den Wert 0"], "passt auch auf (1 − x)/(x + 2)")]),
}
print("Typ 9 – Steckbriefe: kleinste Zahl nötiger Bausteine, Zahl der gültigen Steckbriefe, Zahl aller Ankreuz-Möglichkeiten")
for name, m in S.items():
    m["felder"] = ["menge"]
    m["bedingungen"] = [("Steckbrief eindeutig", steckbrief(m))]
    wahr = [b for b, f in m["bausteine"].items() if f(m["ziel"])]
    falsch = [b for b in m["bausteine"] if b not in wahr]
    alle = [c for k in range(1, m["hoechstens"] + 1) for c in combinations(m["bausteine"], k)]
    gueltig = [c for c in alle if pruefe2(m, [list(c)]).get("richtig")]
    kleinste = min(len(c) for c in gueltig)
    assert gueltig and kleinste >= 2 and len(gueltig) / len(alle) <= 0.2 and falsch, (name, kleinste, len(gueltig), len(alle), falsch)
    print(f"  {name}: mindestens {kleinste} Bausteine, {len(gueltig)} von {len(alle)} Möglichkeiten gültig, {len(falsch)} Baustein(e) stimmen für das Ziel gar nicht")
    m["gut"] = [[g] for g in m["gut"]]
    m["schlecht"] = [([g], grund) for g, grund in m["schlecht"]]
    M[name] = m

for name, m in M.items():
    for a in m["gut"]:
        assert pruefe2(m, a) == {"format_ok": True, "richtig": True}, (name, a, pruefe2(m, a))
    for a, grund in m["schlecht"]:
        e = pruefe2(m, a)
        assert e["format_ok"] and e["richtig"] is False, (name, a, e)
        assert e["verletzt"] == grund or e.get("hinweis") == grund, (name, a, e)
    assert pruefe2(m, ["abc"] * len(m["felder"])) == {"format_ok": False}
assert len(M) == 20 and all(sum(k.startswith(f"{t}-K{kl}") for k in M) == 2 for t in (6, 7, 8, 9, 15) for kl in (5, 8))
# Wie viele gültige Antworten hat eine offene Aufgabe im Bereich −12 … 12? (Schutz gegen Auswendiglernen)
for name in ("6-K5-1", "6-K5-2", "8-K5-1", "8-K5-2"):
    m = M[name]
    n = sum(pruefe2(m, list(p)).get("richtig", False) for p in product(range(-12, 13), repeat=len(m["felder"])))
    print(f"  {name}: {n} gültige Antworten mit Zahlen von −12 bis 12")
    assert n >= 4
print("Teil 1 – 20 Musteraufgaben für die Typen 6, 7, 8, 9, 15: Prüfregel trägt (mit zwei neuen Feldarten)")


# ── Teil 2 ── Typ 3: Rechenweg zusammenbauen
def pruefe_weg(aufgabe, gelegt):
    """gelegt = [(karten_id, eingetragene Zahl), …] in der Reihenfolge des Kindes.
    Regel: (1) je Stufe genau eine Karte, Stufen aufsteigend und vollständig; (2) jede Karte ist – mit der eingetragenen Zahl –
    gleichwertig zur Aufgabe (gerechnet, nicht hinterlegt); (3) die erste nicht gleichwertige Karte wird gemeldet,
    mit dem Fehlbild, wenn die Zahl dazu passt."""
    k = aufgabe["karten"]
    stufen = [k[i]["stufe"] for i, _ in gelegt]
    if stufen != list(range(1, aufgabe["stufen"] + 1)):
        return {"richtig": False, "grund": "reihenfolge"}
    for pos, (i, roh) in enumerate(gelegt, 1):
        w = zahl(roh)
        if w is None:
            return {"format_ok": False}
        if not aufgabe["gleichwertig"](k[i]["zeile"], w):
            fb = k[i].get("fehlbild", {})
            return {"richtig": False, "grund": "zeile", "karte": pos, **({"fehlbild": fb[w]} if w in fb else {})}
    return {"richtig": True}


def wert_gleich(ziel):
    return lambda zeile, w: zeile(w) == ziel


def loesung_gleich(ziel):
    def f(zeile, w):
        g = lambda x: zeile(F(x), w)          # linke minus rechte Seite
        f0, f1, f2 = g(0), g(1), g(2)
        if f2 - f1 != f1 - f0 or f1 == f0:
            return False
        return -f0 / (f1 - f0) == ziel
    return f


W = {
    "3-K5": dict(text="25 − 4 · (3 − 8)", stufen=3, gleichwertig=wert_gleich(25 - 4 * (3 - 8)), karten={
        "a": dict(stufe=1, text="25 − 4 · (□)", zeile=lambda w: 25 - 4 * w, fehlbild={5: "Richtung: 3 − 8 ist −5"}),
        "b": dict(stufe=1, text="□ · (3 − 8)", zeile=lambda w: w * (3 - 8), fehlbild={21: "Rangfolge: erst die Klammer, dann Punkt vor Strich"}),
        "c": dict(stufe=2, text="25 + □", zeile=lambda w: 25 + w, fehlbild={-20: "Zeichen-Paar: minus mal minus ist plus"}),
        "d": dict(stufe=2, text="25 − □", zeile=lambda w: 25 - w, fehlbild={20: "Zeichen-Paar: 4 · (−5) ist −20"}),
        "e": dict(stufe=3, text="= □", zeile=lambda w: w, fehlbild={5: "Zeichen-Paar", -105: "Rangfolge"})},
        gut=[[("a", -5), ("c", 20), ("e", 45)], [("a", -5), ("d", -20), ("e", 45)], [("b", -9), ("c", 20), ("e", 45)]],
        schlecht=[([("b", 21), ("e", -105)], "reihenfolge", None), ([("b", 21), ("c", 20), ("e", 45)], 1, "Rangfolge: erst die Klammer, dann Punkt vor Strich"),
                  ([("a", -5), ("d", 20), ("e", 5)], 2, "Zeichen-Paar: 4 · (−5) ist −20"), ([("a", 5), ("c", 20), ("e", 45)], 1, "Richtung: 3 − 8 ist −5"),
                  ([("e", 45), ("c", 20), ("a", -5)], "reihenfolge", None)]),
    "3-K8-1": dict(text="4 − 3(x − 2) = 2x − 5", stufen=4, gleichwertig=loesung_gleich(3), karten={
        "a": dict(stufe=1, text="4 − 3x + □ = 2x − 5", zeile=lambda x, w: 4 - 3 * x + w - (2 * x - 5), fehlbild={2: "Verteilen: auch die 2 mal 3", -6: "Minusklammer"}),
        "b": dict(stufe=1, text="4 − 3x − □ = 2x − 5", zeile=lambda x, w: 4 - 3 * x - w - (2 * x - 5), fehlbild={6: "Minusklammer: −3 · (−2) ist + 6", 2: "Verteilen und Minusklammer"}),
        "c": dict(stufe=2, text="□ − 3x = 2x − 5", zeile=lambda x, w: w - 3 * x - (2 * x - 5), fehlbild={-2: "Minusklammer"}),
        "d": dict(stufe=3, text="□ = 5x", zeile=lambda x, w: w - 5 * x, fehlbild={5: "Waage: + 5 auf beiden Seiten"}),
        "e": dict(stufe=3, text="−5x = □", zeile=lambda x, w: -5 * x - w, fehlbild={15: "Waage: Vorzeichen beim Hinüberbringen"}),
        "f": dict(stufe=4, text="x = □", zeile=lambda x, w: x - w, fehlbild={-3: "Zeichen-Paar beim Teilen"})},
        gut=[[("a", 6), ("c", 10), ("d", 15), ("f", 3)], [("a", 6), ("c", 10), ("e", -15), ("f", 3)], [("b", -6), ("c", 10), ("d", 15), ("f", 3)]],
        schlecht=[([("b", 6), ("c", -2), ("d", 3), ("f", "3/5")], 1, "Minusklammer: −3 · (−2) ist + 6"), ([("a", 6), ("c", 10), ("e", 15), ("f", 3)], 3, "Waage: Vorzeichen beim Hinüberbringen"),
                  ([("a", 6), ("d", 15), ("f", 3)], "reihenfolge", None)]),
    "3-K8-2": dict(text="5/(x + 3) = 2/(x − 3)", stufen=4, gleichwertig=loesung_gleich(7), karten={
        "a": dict(stufe=1, text="5 · (x − □) = 2 · (x + 3)", zeile=lambda x, w: 5 * (x - w) - 2 * (x + 3), fehlbild={-3: "Verhältnis: über Kreuz heißt mit dem anderen Nenner"}),
        "b": dict(stufe=1, text="5 · (x + □) = 2 · (x − 3)", zeile=lambda x, w: 5 * (x + w) - 2 * (x - 3), fehlbild={3: "Verhältnis: nicht mit dem eigenen Nenner malnehmen"}),
        "c": dict(stufe=2, text="5x − □ = 2x + 6", zeile=lambda x, w: 5 * x - w - (2 * x + 6), fehlbild={3: "Verteilen: auch die 3 mal 5"}),
        "d": dict(stufe=2, text="5x − 15 = 2x + □", zeile=lambda x, w: 5 * x - 15 - (2 * x + w), fehlbild={3: "Verteilen: auch die 3 mal 2"}),
        "e": dict(stufe=3, text="3x = □", zeile=lambda x, w: 3 * x - w, fehlbild={-9: "Waage: + 15 auf beiden Seiten", 9: "Waage"}),
        "f": dict(stufe=4, text="x = □", zeile=lambda x, w: x - w)},
        gut=[[("a", 3), ("c", 15), ("e", 21), ("f", 7)], [("a", 3), ("d", 6), ("e", 21), ("f", 7)]],
        schlecht=[([("b", 3), ("c", 15), ("e", 21), ("f", 7)], 1, "Verhältnis: nicht mit dem eigenen Nenner malnehmen"), ([("a", 3), ("c", 3), ("e", 9), ("f", 3)], 2, "Verteilen: auch die 3 mal 5"),
                  ([("a", 3), ("d", 6), ("e", -9), ("f", -3)], 3, "Waage: + 15 auf beiden Seiten")]),
}
assert F(5, 7 + 3) == F(2, 7 - 3) and 4 - 3 * (3 - 2) == 2 * 3 - 5 and 25 - 4 * (3 - 8) == 45
for name, a in W.items():
    for g in a["gut"]:
        assert pruefe_weg(a, g) == {"richtig": True}, (name, g, pruefe_weg(a, g))
    for g, wo, fb in a["schlecht"]:
        e = pruefe_weg(a, g)
        assert e["richtig"] is False and (e["grund"] == wo if wo == "reihenfolge" else (e["karte"], e.get("fehlbild")) == (wo, fb)), (name, g, e)
    # Wiedererkennen: Wie viele Wege gibt es allein durch Auswahl der Karten (ohne Zahlen)? Und: jede Karte kann richtig ODER falsch werden.
    je_stufe = [sum(1 for k in a["karten"].values() if k["stufe"] == s) for s in range(1, a["stufen"] + 1)]
    wege = 1
    for n in je_stufe:
        wege *= n
    assert wege >= 4 and all("fehlbild" in k or k["stufe"] == a["stufen"] for k in a["karten"].values())
    print(f"  {name}: {len(a['karten'])} Karten, {wege} Karten-Wege, {len(a['gut'])} geprüfte richtige Lösungen, {len(a['schlecht'])} geprüfte falsche")
print("Teil 2 – Typ 3: Prüfregel und drei Musteraufgaben stimmen")

# ── Teil 3 ── fertige Karten ordnen ohne zu rechnen: „weniger Zeichen kommt später“ genügt
karten = ["2x + y = 11 und x − y = 1", "I + II", "3x = 12", "x = 4", "y = 3"]
falsch = ["I − II", "3x = 10"]
assert sorted(karten[2:4], key=len, reverse=True) == karten[2:4]
# Von den zwei falschen Karten widerspricht „3x = 10“ sichtbar der Karte „x = 4“ (4 · 3 = 12): Ausschluss durch Vergleich, nicht durch Lösen.
assert 3 * 4 == 12 != 10
print("Teil 3 – Beispiel mit fertigen Karten: Reihenfolge folgt aus der Form; eine falsche Karte fällt durch Vergleich mit „x = 4“ heraus")
print("OK")
