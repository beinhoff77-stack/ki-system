"""Mathe-Profi, Denkpapier Maßstab: eigene Zuordnung der drei Tests, Prüfregel für offene Umkehraufgaben, Stichprobe.

Aufruf: python3 -I inhalte/mathe-profi/massstab_probe.py

Teil A  Bayerischer Mathematik-Test Gymnasium Jahrgangsstufe 8, Gruppe A, 2023–2025 (63 Bewertungseinheiten).
        Jede Teilaufgabe nur der Art nach (Nummer, BE, Inhalt, Tätigkeit) – keine Aufgabentexte.
        Quelle der Arten: die Aufgabenblätter des Staatsinstituts (am 25.11.2026 gelesen) und der Katalog im Repo
        (inhalte/pruefmaterial/gym/katalog.json), beide stimmen in Nummern und BE überein.
        Erfolgsquoten 2025: Ergebnisbericht des Staatsinstituts; die Zuordnung zu den Teilaufgaben ist aus dem
        Diagramm gelesen und über die Gesamtquote gegengeprüft (siehe assert).
Teil B  Zehn Muster „offene Umkehraufgabe“ mit Referenz der Prüfregel (Bedingung statt fester Lösung).
Teil C  Stichprobe: je 20 Übungen aus drei Flügen (fester Zufallsstart), einfache Kennzahlen.
Teil D  Zahlen aus dem Papier (umgeschriebene Erklärungen, Beispiele).
Liest nur Inhalte, keine Lerndaten.
"""
import json
import os
import random
import re
from collections import Counter, defaultdict
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))

# ───────────── Teil A ─────────────
# Tätigkeit: R rechnen nach Regel/Formel · U übertragen, umkehren, Term aufstellen · B begründen, erläutern, Gegenbeispiel
#            Z zeichnen, konstruieren, im Bild sehen · A ablesen, Datenbegriff · S deuten, schätzen
# Inhalt:    Alg Zahlen/Algebra · Geo Geometrie/Raum · Geld Prozent, Verhältnis, Größen · Dat Daten
# f = braucht eine Formel aus Geometrie/Raum; t = Tabellenkalkulation; letzte Spalte = Erfolgsquote 2025 in %
TEST = """
2023 1a 1 Alg R - - | 2023 1b 1 Alg R - - | 2023 1c 1 Alg R - - | 2023 2a 1 Alg S - - | 2023 2b 2 Alg R - -
2023 3a 1 Geo Z - - | 2023 3b 1 Geo B - - | 2023 4a 1 Geld S - - | 2023 4b 1 Geld U - - | 2023 4c 2 Geo R f -
2023 5a 1 Geld R - - | 2023 5b 1 Dat A - - | 2023 5c 1 Dat U - - | 2023 6 2 Geld U - - | 2023 7a 1 Geo R f -
2023 7b 1 Geo Z - - | 2023 7c 2 Geo B - -
2024 1a 2 Alg R - - | 2024 1b 1 Alg U - - | 2024 2 2 Alg R - - | 2024 3a 1 Dat A - - | 2024 3b 2 Dat A - -
2024 3c 2 Geld R - - | 2024 4a 1 Geld R - - | 2024 4b 1 Geo Z - - | 2024 5a 2 Geo B - - | 2024 5b 1 Geo B - -
2024 6a 1 Alg R - - | 2024 6b 1 Alg U - - | 2024 6c 1 Alg U t - | 2024 7a 1 Alg U - - | 2024 7b 2 Alg B - -
2025 1a 1 Alg R - 75.9 | 2025 1b 1 Alg R - 27.9 | 2025 2a 2 Geo R f 47.4 | 2025 2b 1 Geo U - 12.6 | 2025 3 2 Alg R - 52.8
2025 4 2 Alg R - 48.7 | 2025 5 1 Dat B t 41.8 | 2025 6a 1 Dat B - 63.1 | 2025 6b 2 Geld U - 18.2 | 2025 6c 1 Dat B - 50.7
2025 6d 1 Geld B - 69.4 | 2025 7a 1 Geo Z - 73.6 | 2025 7b 1 Geo R f 36.5 | 2025 7c 1 Geo U - 16.0 | 2025 8a 1 Geo B - 36.1
2025 8b 2 Geo B - 16.6
"""
zeilen = [z.split() for block in TEST.strip().splitlines() for z in block.split("|")]
T = [{"jahr": int(z[0]), "nr": z[1], "be": int(z[2]), "inhalt": z[3], "tat": z[4], "merk": z[5],
      "quote": None if z[6] == "-" else float(z[6])} for z in zeilen]
assert len(T) == 48 and sum(t["be"] for t in T) == 63
for j in (2023, 2024, 2025):
    assert sum(t["be"] for t in T if t["jahr"] == j) == 21, j

be = lambda bed: sum(t["be"] for t in T if bed(t))
tat = {k: be(lambda t, k=k: t["tat"] == k) for k in "RUBZAS"}
inh = {k: be(lambda t, k=k: t["inhalt"] == k) for k in ("Alg", "Geo", "Geld", "Dat")}
r_formel = be(lambda t: t["tat"] == "R" and t["merk"] == "f")
r_rein = tat["R"] - r_formel
assert tat == {"R": 26, "U": 12, "B": 15, "Z": 4, "A": 4, "S": 2} and (r_rein, r_formel) == (20, 6)
assert inh == {"Alg": 23, "Geo": 21, "Geld": 11, "Dat": 8}
b_geo = be(lambda t: t["tat"] == "B" and t["inhalt"] == "Geo")
assert b_geo == 9
pz = lambda n: round(100 * n / 63)
print("Teil A – 63 Bewertungseinheiten, eigene Zuordnung")
print("  Tätigkeit:", {k: f"{v} ({pz(v)} %)" for k, v in tat.items()})
print(f"  Rechnen nach Regel: {r_rein} ({pz(r_rein)} %) nur mit den 15 Regeln, {r_formel} ({pz(r_formel)} %) Regel plus Geometrie-Formel")
print("  Inhalt:", {k: f"{v} ({pz(v)} %)" for k, v in inh.items()})
print(f"  Begründen: {tat['B']} BE, davon {b_geo} in Geometrie")
print("  Tabellenkalkulation in den Jahren:", sorted({t["jahr"] for t in T if t["merk"] == "t"}))

NOTE = lambda p: 1 if p >= 16 else 2 if p >= 13 else 3 if p >= 10 else 4 if p >= 7 else 5 if p >= 4 else 6
stufen = [("nur die 15 Regeln", lambda t: t["tat"] == "R" and t["merk"] != "f"),
          ("+ Geometrie-Formeln", lambda t: t["tat"] == "R"),
          ("+ Übertragen/Umkehren", lambda t: t["tat"] in "RU"),
          ("+ Ablesen, Zeichnen, Deuten", lambda t: t["tat"] in "RUAZS"),
          ("+ Begründen (alles)", lambda t: True)]
print("  Wer genau das kann und sonst nichts – BE und Note je Jahrgang:")
erg = {}
for name, bed in stufen:
    p = [sum(t["be"] for t in T if t["jahr"] == j and bed(t)) for j in (2023, 2024, 2025)]
    erg[name] = (p, [NOTE(x) for x in p])
    print(f"    {name:30} BE {p}  Note {[NOTE(x) for x in p]}")
assert erg["nur die 15 Regeln"] == ([6, 8, 6], [5, 4, 5])
assert erg["+ Geometrie-Formeln"] == ([9, 8, 9], [4, 4, 4])
assert erg["+ Übertragen/Umkehren"] == ([13, 12, 13], [2, 3, 2])
assert erg["+ Ablesen, Zeichnen, Deuten"] == ([18, 16, 14], [1, 1, 2])

# Erfolgsquoten 2025 je Tätigkeit (gewichtet mit BE) und Gegenprobe über die Gesamtquote
t25 = [t for t in T if t["jahr"] == 2025]
gesamt = sum(t["be"] * t["quote"] for t in t25) / 21
assert abs(gesamt - 41.5) < 0.1 and abs(gesamt * 21 / 100 - 8.71) < 0.01           # Bericht: 41,5 % und 8,71 BE
q = {}
for k in "RUBZ":
    sel = [t for t in t25 if t["tat"] == k]
    q[k] = sum(t["be"] * t["quote"] for t in sel) / sum(t["be"] for t in sel)
print("  Erfolgsquote 2025 je Tätigkeit:", {k: f"{v:.0f} %" for k, v in q.items()}, f"| gesamt {gesamt:.1f} % = {gesamt * 21 / 100:.2f} BE")
assert round(q["R"]) == 49 and round(q["U"]) == 16 and round(q["B"]) == 42

# ───────────── Teil B ─────────────
def zahl(v, ganz=False, stellen=3, grenze=10 ** 6):
    """Antwort als exakte Zahl lesen; None = Unsinn (zählt nie als Fehler)."""
    if isinstance(v, bool) or not isinstance(v, (int, float, str)):
        return None
    s = str(v).strip().replace("−", "-").replace(",", ".")
    if not re.fullmatch(r"-?\d+(\.\d{1,%d})?" % stellen, s):
        return None
    x = F(s)
    if abs(x) > grenze or (ganz and x.denominator != 1):
        return None
    return x


def pruefe(muster, antwort):
    """Referenz: alle Werte lesen, dann die Bedingungen der Reihe nach prüfen. Die erste verletzte Bedingung gibt den Hinweis."""
    if not isinstance(antwort, list) or len(antwort) != len(muster["felder"]):
        return {"format_ok": False}
    werte = [zahl(a, ganz=f == "ganz") for a, f in zip(antwort, muster["felder"])]
    if any(w is None for w in werte):
        return {"format_ok": False}
    for name, bed in muster["bedingungen"]:
        try:
            ok = bed(*werte)
        except ZeroDivisionError:
            ok = False
        if not ok:
            return {"format_ok": True, "richtig": False, "verletzt": name}
    return {"format_ok": True, "richtig": True}


M = {
    "K5-1": {"text": "Nenne eine ganze Zahl, die man von 7 abziehen kann, sodass mehr als 7 herauskommt.",
             "felder": ["ganz"], "bedingungen": [("Ergebnis größer als 7", lambda x: 7 - x > 7)],
             "gut": [[-1], [-250]], "schlecht": [([3], "Ergebnis größer als 7"), ([0], "Ergebnis größer als 7")]},
    "K5-2": {"text": "Nenne zwei verschiedene ganze Zahlen mit der Summe −5, von denen eine positiv ist.",
             "felder": ["ganz", "ganz"],
             "bedingungen": [("Summe ist −5", lambda a, b: a + b == -5), ("eine ist positiv", lambda a, b: max(a, b) > 0),
                             ("verschieden", lambda a, b: a != b)],
             "gut": [[3, -8], [-6, 1]], "schlecht": [([-2, -3], "eine ist positiv"), ([2, -8], "Summe ist −5")]},
    "K5-3": {"text": "Setze für □ eine Zahl ein, sodass 3 · (□ − 4) kleiner als −6 ist.",
             "felder": ["ganz"], "bedingungen": [("Termwert kleiner als −6", lambda x: 3 * (x - 4) < -6)],
             "gut": [[1], [-10]], "schlecht": [([2], "Termwert kleiner als −6"), ([5], "Termwert kleiner als −6")]},
    "K5-4": {"text": "Nenne Länge und Breite (ganze cm) eines Rechtecks mit Umfang 20 cm und mehr als 20 cm² Flächeninhalt.",
             "felder": ["ganz", "ganz"],
             "bedingungen": [("Seiten sind positiv", lambda l, b: l > 0 and b > 0), ("Umfang ist 20", lambda l, b: 2 * (l + b) == 20),
                             ("Fläche größer als 20", lambda l, b: l * b > 20)],
             "gut": [[5, 5], [7, 3], [4, 6]], "schlecht": [([8, 2], "Fläche größer als 20"), ([10, 10], "Umfang ist 20"), ([12, -2], "Seiten sind positiv")]},
    "K5-5": {"text": "Nenne eine Zahl, die durch 2 und durch 3 teilbar ist, aber nicht durch 12.",
             "felder": ["ganz"],
             "bedingungen": [("positiv", lambda n: n > 0), ("durch 2 und durch 3 teilbar", lambda n: n % 6 == 0), ("nicht durch 12 teilbar", lambda n: n % 12 != 0)],
             "gut": [[6], [18], [30]], "schlecht": [([12], "nicht durch 12 teilbar"), ([8], "durch 2 und durch 3 teilbar")]},
    "K8-1": {"text": "Durch welche Zahl muss man die 12 in 5x − (3x − 2) = 12 ersetzen, damit x = 4 die Lösung ist?",
             "felder": ["rational"], "bedingungen": [("x = 4 erfüllt die Gleichung", lambda c: 5 * 4 - (3 * 4 - 2) == c)],
             "gut": [[10]], "schlecht": [([6], "x = 4 erfüllt die Gleichung"), ([12], "x = 4 erfüllt die Gleichung")]},
    "K8-2": {"text": "Gib m und t so an, dass der Graph von y = m · x + t fällt und durch P(2 | 3) geht.",
             "felder": ["rational", "rational"],
             "bedingungen": [("geht durch P", lambda m, t: 2 * m + t == 3), ("Graph fällt", lambda m, t: m < 0)],
             "gut": [[-1, 5], ["-0,5", 4]], "schlecht": [([1, 1], "Graph fällt"), ([-1, 3], "geht durch P")]},
    "K8-3": {"text": "Gib eine Zahl a an, für die die Lösung von a · x + 3 = 2x + 5 negativ ist.",
             "felder": ["rational"],
             "bedingungen": [("Gleichung hat genau eine Lösung", lambda a: a != 2), ("Lösung ist negativ", lambda a: F(2) / (a - 2) < 0)],
             "gut": [[1], [0], [-3]], "schlecht": [([2], "Gleichung hat genau eine Lösung"), ([4], "Lösung ist negativ")]},
    "K8-4": {"text": "Nenne eine Zahl x, für die der Bruchterm 1 : (x − 3) größer als 1 ist.",
             "felder": ["rational"],
             "bedingungen": [("Term ist definiert", lambda x: x != 3), ("Termwert größer als 1", lambda x: F(1) / (x - 3) > 1)],
             "gut": [["3,5"], ["3,1"]], "schlecht": [([3], "Term ist definiert"), ([5], "Termwert größer als 1"), ([2], "Termwert größer als 1")]},
    "K8-5": {"text": "A(0 | 0) und B(4 | 0). Nenne einen Gitterpunkt C, sodass das Dreieck ABC den Flächeninhalt 6 hat.",
             "felder": ["ganz", "ganz"], "bedingungen": [("Flächeninhalt ist 6", lambda x, y: F(1, 2) * 4 * abs(y) == 6)],
             "gut": [[0, 3], [7, -3], [-2, 3]], "schlecht": [([2, 6], "Flächeninhalt ist 6"), ([3, 0], "Flächeninhalt ist 6")]},
}
for name, m in M.items():
    for a in m["gut"]:
        assert pruefe(m, a) == {"format_ok": True, "richtig": True}, (name, a)
    assert len(m["gut"]) >= 1
    for a, verletzt in m["schlecht"]:
        assert pruefe(m, a) == {"format_ok": True, "richtig": False, "verletzt": verletzt}, (name, a, pruefe(m, a))
    for unsinn in (None, [], ["abc"] * len(m["felder"]), [True] * len(m["felder"]), ["1e9"] * len(m["felder"]),
                   [10 ** 7] * len(m["felder"]), ["1,23456"] * len(m["felder"]), [1] * (len(m["felder"]) + 1)):
        assert pruefe(m, unsinn) == {"format_ok": False}, (name, unsinn)
    # offen heißt: mehr als eine richtige Antwort (außer K8-1, dort ist die Umkehrung eindeutig)
    assert (len(m["gut"]) > 1) or name == "K8-1"
# K5-4 vollständig durchsucht: genau die Paare mit Summe 10 und Produkt > 20
assert {(l, b) for l in range(1, 20) for b in range(1, 20) if pruefe(M["K5-4"], [l, b]).get("richtig")} == {(3, 7), (4, 6), (5, 5), (6, 4), (7, 3)}
assert 5 * 4 - (3 * 4 - 2) == 10
print(f"Teil B – {len(M)} Muster, Prüfregel gegen {sum(len(m['gut']) + len(m['schlecht']) for m in M.values())} Antworten und je 8 Unsinn-Eingaben getestet")

# ───────────── Teil C ─────────────
random.seed(20261125)
print("Teil C – Stichprobe je 20 Übungen")
for s in ("geometrie.winkel", "daten.kennwerte", "funktionen.grundbegriffe"):
    d = json.load(open(os.path.join(HIER, "..", "themen", s + ".json"), encoding="utf-8"))
    alle = [a for a in d["aufgaben"] if a["p"] == "uebung"]
    st = random.sample(alle, 20)
    form = Counter(a["y"] for a in alle)
    print(f"  {s}: {len(alle)} Übungen, Zahl oder Auswahl {round(100 * (form['zahl'] + form['auswahl']) / len(alle))} %, mit Bild "
          f"{round(100 * sum(1 for a in alle if a['f'].get('grafik')) / len(alle))} % | Stichprobe: Stufen {dict(sorted(Counter(a['s'] for a in st).items()))}, "
          f"ohne Typ {sum(1 for a in st if not a.get('g'))}, Typen {len({a.get('g') for a in st if a.get('g')})}, "
          f"Tipp nennt die Formel {sum(1 for a in st if re.search(r'=|mal Anzahl|durch die Anzahl|Summe durch', a.get('h') or ''))}")

# ───────────── Teil D ─────────────
assert 12 * 100 == 1200 and F(350, 100) == F(7, 2) and 2 * 100 * 100 == 20000 and 5 * 100 == 500 and 3 * 10 == 30 and 3 * 100 == 300
assert F(3, 10) + F(5, 10) + F(2, 10) == 1 and F(3 + 2, 10) == 1 - F(5, 10) == F(1, 2) and F(3, 10) != F(1, 3) and F(3, 10) != F(3, 7)
assert F(600, 4) == 150 and 3 * 150 == 450 and F(60, 4) * 5 == 75 and 75 * F(80, 100) == 60          # Balken Klasse 5 und 8
assert 6 * 20 - 6 * 2 == 6 * 10 + 6 * 8 == 108 and (12 // 3) - 2 == 2 == F(12 - 6, 3)                # zwei Wege
assert (52 + 60) / 2 == 56 and 52 + 60 / 2 == 82
print("OK")
