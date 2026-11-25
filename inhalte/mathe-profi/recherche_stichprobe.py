"""Mathe-Profi, Nachtrag zu den Denkpapieren Maßstab und Methoden (nach Lektüre von inhalte/recherche/).

Aufruf: python3 -I inhalte/mathe-profi/recherche_stichprobe.py

Teil 1  Erfolgsquoten 2023–2025 je Teilaufgabe aus tief-5 (Angabe des Helfers), gegengeprüft über die Gesamtquoten
        der Ergebnisberichte, ausgewertet nach MEINER Zuordnung aus massstab_probe.py.
Teil 2  Stichprobe: zwölf Beispiele der Helfer nachgerechnet (deren Prüfskripte liegen nicht im Repo).
Teil 3  Kästchengröße im Gitter (Aussage in tief-10 gegen die Rechnung aus auftrag2.md).
Nur Inhalte, keine Lerndaten.
"""
from fractions import Fraction as F
from itertools import permutations

# ── Teil 1 ── (Jahr, Nr, BE, Tätigkeit nach massstab_probe.py, Formel?, Quote laut tief-5)
D = """2025 1a 1 R - 75.9|2025 1b 1 R - 27.9|2025 2a 2 R f 47.4|2025 2b 1 U - 12.6|2025 3 2 R - 52.8|2025 4 2 R - 48.7|2025 5 1 B - 41.8
2025 6a 1 B - 63.1|2025 6b 2 U - 18.2|2025 6c 1 B - 50.7|2025 6d 1 B - 69.4|2025 7a 1 Z - 73.6|2025 7b 1 R f 36.5|2025 7c 1 U - 16.0
2025 8a 1 B - 36.1|2025 8b 2 B - 16.6
2024 1a 2 R - 61.6|2024 1b 1 U - 56.7|2024 2 2 R - 36.6|2024 3a 1 A - 86.9|2024 3b 2 A - 81.5|2024 3c 2 R - 70.1|2024 4a 1 R - 34.2
2024 4b 1 Z - 36.3|2024 5a 2 B - 55.1|2024 5b 1 B - 17.1|2024 6a 1 R - 73.3|2024 6b 1 U - 22.6|2024 6c 1 U - 33.5|2024 7a 1 U - 37.2
2024 7b 2 B - 15.3
2023 1a 1 R - 57.0|2023 1b 1 R - 48.8|2023 1c 1 R - 31.6|2023 2a 1 S - 63.9|2023 2b 2 R - 59.2|2023 3a 1 Z - 74.4|2023 3b 1 B - 75.0
2023 4a 1 S - 35.8|2023 4b 1 U - 49.8|2023 4c 2 R f 38.7|2023 5a 1 R - 75.9|2023 5b 1 A - 33.2|2023 5c 1 U - 42.4|2023 6 2 U - 46.5
2023 7a 1 R f 51.3|2023 7b 1 Z - 27.6|2023 7c 2 B - 16.7"""
T = [dict(zip("jahr nr be tat merk quote".split(), z.split())) for block in D.splitlines() for z in block.split("|")]
for t in T:
    t["be"], t["quote"] = int(t["be"]), float(t["quote"])
assert len(T) == 48 and sum(t["be"] for t in T) == 63
gesamt = {j: sum(t["be"] * t["quote"] for t in T if t["jahr"] == j) / 21 for j in ("2023", "2024", "2025")}
# Ergebnisberichte laut tief-5: 47,1 % · 49,4 % · 41,5 % – die abgelesenen Einzelquoten passen dazu
assert abs(gesamt["2023"] - 47.1) < 0.3 and abs(gesamt["2024"] - 49.4) < 0.3 and abs(gesamt["2025"] - 41.5) < 0.1, gesamt


def quote(bed):
    sel = [t for t in T if bed(t)]
    return sum(t["be"] * t["quote"] for t in sel) / sum(t["be"] for t in sel), sum(t["be"] for t in sel)


gruppen = [("Rechnen, nur die 15 Regeln", lambda t: t["tat"] == "R" and t["merk"] != "f"),
           ("Rechnen mit Geometrie-Formel", lambda t: t["tat"] == "R" and t["merk"] == "f"),
           ("Übertragen, Umkehren, Term aufstellen", lambda t: t["tat"] == "U"),
           ("Begründen", lambda t: t["tat"] == "B"),
           ("Zeichnen, Sehen", lambda t: t["tat"] == "Z"), ("Ablesen, Datenbegriff", lambda t: t["tat"] == "A"), ("Deuten, Schätzen", lambda t: t["tat"] == "S")]
print("Teil 1 – landesweite Erfolgsquote 2023–2025 nach meiner Zuordnung (Quoten laut tief-5)")
erg = {}
for name, bed in gruppen:
    q, n = quote(bed)
    erg[name] = round(q)
    print(f"  {name:40} {n:2d} BE  {q:5.1f} %")
assert erg == {"Rechnen, nur die 15 Regeln": 54, "Rechnen mit Geometrie-Formel": 43, "Übertragen, Umkehren, Term aufstellen": 33,
               "Begründen": 37, "Zeichnen, Sehen": 53, "Ablesen, Datenbegriff": 71, "Deuten, Schätzen": 50}, erg
b_geo = quote(lambda t: t["tat"] == "B" and (t["jahr"], t["nr"]) in {("2025", "8a"), ("2025", "8b"), ("2024", "5a"), ("2024", "5b"), ("2023", "3b"), ("2023", "7c")})
print(f"  davon Begründen in Geometrie (ohne die Formel an der Figur 2024) {b_geo[1]} BE  {b_geo[0]:.1f} %")

# ── Teil 2 ── Beispiele der Helfer
assert max(int(f"{a}{b}") * int(f"{c}{d}") for a, b, c, d in permutations(range(1, 7), 4)) == 3402 == 63 * 54            # tief-12 B7
assert sum(1 for a in range(1, 7) for b in range(1, 7) if (a * b) % 2 == 0) == 27                                          # tief-12 B9
assert sum(1 for a in range(1, 7) for b in range(1, 7) if (a + b) % 2 == 0) == 18
assert sorted(n for n in range(10, 100) if n % 3 == 0 and n % 4 == 0 and sum(map(int, str(n))) == 12) == [48, 84]          # tief-12 B5
assert (-2) ** 2 * 3 == 12 and F(1 + 2 + 3 + 10, 4) == 4 and F(2 + 3, 2) == F(5, 2)                                        # tief-12 B1, B4
assert 5 * 12 - (10 + 14 + 9 + 13) == 14                                                                                    # tief-10 Form 4
assert all(((a + b) ** 2 != a * a + b * b) == (a * b != 0) for a in range(-4, 5) for b in range(-4, 5))                    # tief-10 Form 1
assert sorted([3, 5, 5, 6, 8, 9, 13])[3] == 6 and sum([3, 5, 5, 6, 8, 9, 13]) == 49                                        # tief-10 Form 3
assert 3 + 6 + F(9, 3) == 12 and F(3 + 6 + 9, 3) == 6                                                                       # tief-10 Form 5
assert 3 * (13 - 2) - 2 * (13 + 1) == 5 == 13 - 8 and 12 * 7 - 3 * 3 == 75                                                 # tief-8 B6, B1
assert F(620, 4) == 155 and 155 * 7 == 1085 and 3 * 8 // 4 == 6                                                            # tief-8 B3, B5
assert 6 * 98 == 6 * 100 - 6 * 2 == 588 and F(9 - 3, 4 - 1) == 2                                                           # tief-8 B8
print("Teil 2 – zwölf Helfer-Beispiele nachgerechnet: alle stimmen")

# ── Teil 3 ── Gitter 10 × 10 im Bild mit 340 Einheiten Breite und 38 Rand je Seite (lernKoordinaten)
einheiten = F(340 - 2 * 38, 10)
assert einheiten == F(132, 5) and float(einheiten) == 26.4            # nicht 34
assert round(float(einheiten) * 298 / 340, 1) == 23.1                  # gemessen im Entwurf bei 360 px Gerätebreite
print("Teil 3 – 10 Kästchen: 26,4 Einheiten, am Handy etwa 23 px (tief-10 nennt 34 px)")
print("OK")
