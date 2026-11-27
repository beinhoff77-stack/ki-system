T = "terme.potenzgesetze_ganzzahlig"

# ───────── warum_gilt: Fehler-Detektiv ─────────
FD(T, "warum_gilt",
   "Kim setzt das Muster der Zweierpotenzen nach rechts fort. Bei jedem Schritt nach rechts wird durch 2 geteilt.",
   [("2⁴ = 16, 2³ = 8, 2² = 4, 2¹ = 2", [F(16) / 2, F(8) / 2, F(4) / 2] == [8, 4, 2]),
    ("2⁰ = 2 : 2 = 1", F(2) / 2 == 1),
    ("2⁻¹ = 1 : 2 = 1/2", F(1) / 2 == F(1, 2)),
    ("2⁻² = 1/2 − 2 = −3/2", F(1, 2) / 2 == F(1, 2) - 2)],
   "Welche Rechenart steht bei jedem Schritt nach rechts? Rechne jede Zeile nach.",
   "Zeile 1 bis 3 stimmen. In Zeile 4 wird 2 abgezogen statt geteilt. Das Muster verlangt aber: 1/2 : 2 = 1/4. Also ist 2⁻² = 1/4, und eine negative Hochzahl macht die Potenz nicht negativ.",
   None, "bei der negativen Hochzahl 2 abgezogen statt durch 2 geteilt")

# ───────── gleiche_basis_ganz: Fehler-Detektiv ─────────
a = F(3)
FD(T, "gleiche_basis_ganz",
   "Kim vereinfacht (a ≠ 0) den Term a⁻⁴ · a⁷ : a⁻² · a⁻⁵.",
   [("a⁻⁴ · a⁷: Die Hochzahlen werden addiert, (−4) + 7 = 3. Also ist a⁻⁴ · a⁷ = a³.", a ** -4 * a ** 7 == a ** 3),
    ("a³ : a⁻²: Die Hochzahlen werden subtrahiert, 3 − (−2) = 5. Also ist a³ : a⁻² = a⁵.", a ** 3 / a ** -2 == a ** 5),
    ("a⁵ · a⁻⁵: Die Hochzahlen werden addiert, 5 + (−5) = 0. Also ist a⁵ · a⁻⁵ = a⁰ = 0.", a ** 5 * a ** -5 == 0)],
   "Rechne jede Zeile mit einer Zahl nach, zum Beispiel a = 2.",
   "Zeile 1 und 2 stimmen. In Zeile 3 ist die Hochzahl 5 + (−5) = 0 richtig, aber a⁰ ist 1 (für a ≠ 0), nicht 0. Man kann auch sehen: a⁵ · a⁻⁵ = a⁵ · 1/a⁵ = 1. Richtig ist das Ergebnis 1.",
   "rr.potenz", "a⁰ = 0 statt a⁰ = 1")

# ───────── exponent_und_potenz: Zwei Wege ─────────
assert (F(2) ** -2) ** -3 * F(2) ** -4 == 4
Z(T, "exponent_und_potenz", "zwei_wege",
  "Berechne (2⁻²)⁻³ · 2⁻⁴. Weg A: Verrechne die Hochzahlen mit den Potenzgesetzen und rechne dann die eine Potenz aus. "
  "Weg B: Schreibe die Potenzen mit negativer Hochzahl als Brüche und rechne mit den Brüchen. Welchen Wert hat der Term?",
  4, "2 ** ((-2) * (-3) + (-4))", "(1 / 4) ** (-3) * (1 / 16)",
  "Beide Wege müssen denselben Wert ergeben. Bei einer Potenz von einer Potenz werden die Hochzahlen malgenommen, bei einem Produkt gleicher Basen addiert.",
  "Weg A: Die Hochzahlen werden multipliziert: (−2) · (−3) = 6. Also ist (2⁻²)⁻³ = 2⁶. Dann werden bei 2⁶ · 2⁻⁴ die Hochzahlen addiert: 6 + (−4) = 2, also 2² = 4. Weg B: 2⁻² = 1/4. (1/4)⁻³ = 4³ = 64. 2⁻⁴ = 1/16. 64 · 1/16 = 4. Beide Wege: 4.",
  [(0.001953125, "2 ** (-9)", "alle Hochzahlen addiert, also 2⁻⁹ = 1 : 512"),
   (1024, "2 ** 10", "das Vorzeichen von −4 falsch verrechnet: 6 + 4 = 10"),
   (64, "(1 / 4) ** (-3)", "nur (2⁻²)⁻³ berechnet und den Faktor 2⁻⁴ vergessen")],
  "rr.potenz")
