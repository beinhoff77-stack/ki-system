T = "terme.potenzgesetze_natuerlich"

# ───────── gleicher_exponent: Zwei Wege ─────────
assert 2 ** 7 * 5 ** 7 - 2 ** 6 * 5 ** 6 == 9000000
Z(T, "gleicher_exponent", "zwei_wege",
  "Berechne 2⁷ · 5⁷ − 2⁶ · 5⁶. Weg A: Rechne alle vier Potenzen einzeln aus und dann weiter. Weg B: Nimm in jedem Produkt zuerst die Basen mal, weil die Hochzahlen gleich sind.",
  9000000, "10 ** 7 - 10 ** 6", "128 * 78125 - 64 * 15625",
  "Beide Wege müssen denselben Wert ergeben. Welche Basis entsteht, wenn man 2 und 5 malnimmt?",
  "Weg B: 2⁷ · 5⁷ = (2 · 5)⁷ = 10⁷ = 10 000 000 und 2⁶ · 5⁶ = 10⁶ = 1 000 000. Differenz: 9 000 000. Weg A: 2⁷ = 128, 5⁷ = 78 125, 128 · 78 125 = 10 000 000; 2⁶ = 64, 5⁶ = 15 625, 64 · 15 625 = 1 000 000. Gleiches Ergebnis.",
  [(10000000, "10 ** 7", "nur das erste Produkt gerechnet und das zweite vergessen"),
   (1000000, "10 ** 6", "nur das zweite Produkt genannt"),
   (10, "10 ** 7 / 10 ** 6", "die beiden Produkte geteilt statt voneinander abgezogen")],
  "rr.potenz")

# ───────── potenz_von_potenz: Fehler-Detektiv ─────────
b = F(3)
FD(T, "potenz_von_potenz",
   "Kim vereinfacht (a²)³ · a⁴ für eine Zahl a ≠ 0.",
   [("(a²)³ = a²·³ = a⁶", (b ** 2) ** 3 == b ** 6),
    ("a⁶ · a⁴ = a⁶·⁴ = a²⁴", b ** 6 * b ** 4 == b ** 24),
    ("Also ist (a²)³ · a⁴ = a²⁴", b ** 24 == b ** 24)],
   "Prüfe jede Zeile mit a = 2.",
   "Zeile 1 stimmt: Bei einer Potenz von einer Potenz werden die Hochzahlen malgenommen. In Zeile 2 steht aber ein Produkt gleicher Basen: Dort werden die Hochzahlen addiert, also a⁶ · a⁴ = a¹⁰. "
   "Zeile 3 folgt aus der falschen Zeile 2.",
   "rr.potenz", "bei einem Produkt gleicher Basen die Hochzahlen malgenommen statt addiert")
