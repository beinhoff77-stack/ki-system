T = "terme.bruchterme"

# ───────── definitionsmenge: Brücke ─────────
# c steht nicht im Text, nur in der Tabelle: aus dem Wert bei x = 0 folgt c = 5, die dritte Nullstelle liegt außerhalb der Tabelle
nenner = lambda x, c=5: (x - 2) * (x + 1) * (x - c)
assert [nenner(x) for x in (-2, -1, 0, 1, 2, 3)] == [-28, 0, 10, 8, 0, -8]
assert [c for c in range(-30, 31) if [nenner(x, c) for x in (-2, -1, 0, 1, 2, 3)] == [-28, 0, 10, 8, 0, -8]] == [5]
assert [x for x in range(-9, 10) if nenner(x) == 0] == [-1, 2, 5]
Z(T, "definitionsmenge", "bruecke",
  "Die Tabelle zeigt einige Werte des Nenners N(x) = (x − 2)(x + 1)(x − c) für eine feste Zahl c. Der Term T(x) = 7/N(x) hat diesen Nenner. "
  "Wie viele Zahlen muss man aus ℚ ausschließen, damit T(x) definiert ist?",
  3, "3", "1 + 1 + 1",
  "Mit einem Wert aus der Tabelle kannst du c bestimmen. Wann ist ein Produkt aus drei Faktoren gleich null?",
  "Für x = 0 ist N(0) = (−2) · 1 · (−c) = 2c. Laut Tabelle ist N(0) = 10, also c = 5. Probe mit x = 1: (−1) · 2 · (1 − 5) = 8, das passt zur Tabelle. "
  "Der Nenner ist 0, wenn einer der Faktoren 0 ist: x = 2, x = −1 oder x = 5. Man muss 3 Zahlen ausschließen: D = ℚ \\ {−1; 2; 5}.",
  [(2, "3 - 1", "nur die in der Tabelle sichtbaren Nullstellen −1 und 2 gezählt (die dritte, x = 5, liegt außerhalb der Tabelle)"),
   (6, "6", "die Zahl der Spalten der Tabelle genannt"),
   (1, "1", "nur eine Nullstelle des Nenners gezählt")],
  "id.algebra.erlaubte_zahlen", einheit="Zahlen",
  grafik={"typ": "tabelle", "kopf": ["x", "−2", "−1", "0", "1", "2", "3"], "zeilen": [["N(x)", "−28", "0", "10", "8", "0", "−8"]]})

# ───────── termwert: Fehler-Detektiv ─────────
FD(T, "termwert",
   "Kim berechnet T(−2) für T(x) = (3 − x²)/(x + 4).",
   [("Zähler: (−2)² = −4, also 3 − (−4) = 7", (-2) ** 2 == -4 and 3 - (-4) == 7),
    ("Nenner: −2 + 4 = 2", -2 + 4 == 2),
    ("T(−2) = 7 : 2 = 3,5", 7 / 2 == 3.5)],
   "Rechne T(−2) selbst mit dem Taschenrechner nach.",
   "Zeile 1 enthält den Fehler: (−2)² = (−2) · (−2) = 4, nicht −4. Der Zähler ist also 3 − 4 = −1. Zeile 2 stimmt. Zeile 3 rechnet mit dem falschen Zähler 7 richtig weiter. Richtig ist T(−2) = −1 : 2 = −0,5.",
   "rr.reihenfolge", "(−2)² als −4 gerechnet (das Quadrat einer negativen Zahl)",
   rueck={1: "Diese Zeile ist richtig: Der Nenner wird unabhängig vom Zähler berechnet, −2 + 4 = 2. Der erste Fehler steckt beim Quadrieren im Zähler (Zeile 1)."})

# ───────── erweitern: Zwei Wege ─────────
assert gl("(x-2)*(x+2)", "x**2-4")
Z(T, "erweitern", "zwei_wege",
  "Der Bruch 5/(x − 2) (x ≠ 2 und x ≠ −2) wird so erweitert, dass der Nenner x² − 4 lautet. "
  "Weg A: Setze x = 5 in den alten und in den neuen Nenner ein und vergleiche die beiden Zahlen. Weg B: Zerlege x² − 4 mit der dritten binomischen Formel in Faktoren und vergleiche mit dem alten Nenner. "
  "Welchen Wert hat der neue Zähler für x = 5?",
  35, "5 * (5 + 2)", "5 * (5 ** 2 - 4) / (5 - 2)",
  "Beide Wege müssen denselben Wert ergeben. Der Zähler wird mit demselben Faktor malgenommen wie der Nenner.",
  "Weg A: Für x = 5 ist der alte Nenner 5 − 2 = 3 und der neue Nenner 25 − 4 = 21. Der Nenner wurde mit 21 : 3 = 7 malgenommen, also auch der Zähler: 5 · 7 = 35. Weg B: x² − 4 = (x − 2)(x + 2), der alte Nenner ist ein Faktor davon, der Erweiterungsfaktor ist x + 2, für x = 5 also 7. Neuer Zähler: 5(x + 2) = 5 · 7 = 35. Beide Wege geben 35.",
  [(5, "5", "den Zähler nicht mit erweitert"),
   (15, "5 * (5 - 2)", "mit x − 2 statt mit x + 2 erweitert"),
   (25, "5 * 5", "mit x statt mit x + 2 erweitert")],
  "rr.kuerzen")

# ───────── addieren: Brücke ─────────
wertetabelle = {2: F(5, 2), 3: F(26, 15), 4: F(4, 3)}
terme = [lambda x: F(6, 2 * x + 2), lambda x: F(4 * x + 10, x * (x + 2)), lambda x: F(6 * x + 8, x * (x + 2)), lambda x: F(6, x * (x + 2))]
assert all(F(4, x) + F(2, x + 2) == wertetabelle[x] for x in wertetabelle)
W(T, "addieren", "bruecke",
  "Die Tabelle zeigt einige Werte des Terms T(x) = 4/x + 2/(x + 2). Welcher zu einem Bruch zusammengefasste Term gehört zu allen Werten der Tabelle?",
  ["6/(2x + 2)", "(4x + 10)/(x(x + 2))", "(6x + 8)/(x(x + 2))", "6/(x(x + 2))"], 2,
  [all(t(x) == wertetabelle[x] for x in wertetabelle) for t in terme],
  "Setze einen Wert aus der Tabelle in die Terme ein, zum Beispiel x = 2. Du kannst auch selbst mit dem Hauptnenner x(x + 2) zusammenfassen.",
  "Hauptnenner x(x + 2): 4/x = 4(x + 2)/(x(x + 2)) und 2/(x + 2) = 2x/(x(x + 2)). Summe: (4x + 8 + 2x)/(x(x + 2)) = (6x + 8)/(x(x + 2)). Probe x = 2: 20/8 = 5/2, das passt zur Tabelle.",
  {0: ("Zähler und Nenner getrennt addiert: (4 + 2)/(x + x + 2)", lambda: gl("(4+2)/(x+x+2)", "6/(2*x+2)")),
   1: ("nur den ersten Bruch auf den Hauptnenner erweitert: 4(x + 2) + 2 im Zähler", lambda: gl("(4*(x+2)+2)/(x*(x+2))", "(4*x+10)/(x*(x+2))")),
   3: ("die Zähler addiert, aber nicht erweitert: 4 + 2 über dem Hauptnenner", lambda: gl("(4+2)/(x*(x+2))", "6/(x*(x+2))"))},
  "rr.bruchrechnen",
  grafik={"typ": "tabelle", "kopf": ["x", "2", "3", "4"], "zeilen": [["T(x)", "5/2", "26/15", "4/3"]]})
