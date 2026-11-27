"""Mathe-Profi, Auftrag 15 Teil A und B: Klassenleitern – dieselbe Regel, dieselbe Idee in Klasse 5 bis 10 (Gymnasium Bayern).

Nur Daten. Je Klasse entweder ein Beispiel oder ausdrücklich „kommt nicht vor“.
Beispiel: (Klasse, Art, Thema der App, Text, Probe).  Art: V = Vorwissen, E = Einführung, A = Anwendung.
Im Text ist die wirkende Stelle mit ⟦…⟧ umschlossen – genau diese Zeichen markiert der Designer.
Nicht vorhanden: (Klasse, None, Grund).
Die Beispiele einer Leiter sind gleich gebaut: gleiche Stelle, gleiche Handlung; nur die Zahlen werden zu Brüchen und Buchstaben.
"""
import math
from fractions import Fraction as F

KEIN = "kommt nicht vor"
BENUTZT = "kommt nicht vor – kein Thema der App in dieser Klasse; die Regel wird als bekannt benutzt"
NOCH_NICHT = "kommt nicht vor – der Stoff dafür beginnt später"
VORBEI = "kommt nicht vor – kein Thema der App in dieser Klasse"


def alle(f, g, aus=()):
    return all(f(F(p)) == g(F(p)) for p in (-5, -3, -2, 2, 3, 5, 7, F(1, 2)) if p not in aus)


def nah(a, b, st=2):
    return round(a, st) == round(b, st)


# Rechenregeln, Schlüssel = Kennung. Dazu: „gleich“ = was in jeder Zeile gleich bleibt (für den Designer).
LEITER_R = {
 "rr.stellenwert": ("Das „· 10“ (oder „· 100“, „· 10⁻⁴“) – die Ziffern bleiben, sie rücken nur.", [
  (5, "E", "zahlen.natuerlich", "34 ⟦· 10⟧ = 340", lambda: 34 * 10 == 340),
  (6, "E", "bruch.dezimal", "2,5 ⟦· 10⟧ = 25", lambda: F(5, 2) * 10 == 25),
  (7, "A", "bruch.prozent_grundwert", "0,15 ⟦· 100⟧ = 15, also 15 %", lambda: F(15, 100) * 100 == 15),
  (8, "A", "terme.potenzgesetze_ganzzahlig", "3 ⟦· 10⁻⁴⟧ = 0,0003", lambda: 3 * F(10) ** -4 == F(3, 10000)),
  (9, None, BENUTZT), (10, None, BENUTZT)]),
 "rr.plusminus": ("Die zwei Minuszeichen nebeneinander: Rechenzeichen und Vorzeichen.", [
  (5, "E", "zahlen.ganz", "3 ⟦−⟧ (⟦−⟧2) = 3 + 2 = 5", lambda: 3 - (-2) == 5),
  (6, "A", "bruch.rechnen", "½ ⟦−⟧ (⟦−⟧¼) = ½ + ¼ = ¾", lambda: F(1, 2) - (-F(1, 4)) == F(3, 4)),
  (7, "A", "terme.umformen", "3x ⟦−⟧ (⟦−⟧2x) = 3x + 2x = 5x", lambda: alle(lambda x: 3 * x - (-2 * x), lambda x: 5 * x)),
  (8, "A", "funktionen.linear", "f(x) = 3 − x, x = −2: 3 ⟦−⟧ (⟦−⟧2) = 3 + 2 = 5", lambda: 3 - (-2) == 5),
  (9, "A", "zahlen.reell", "3√2 ⟦−⟧ (⟦−⟧2√2) = 3√2 + 2√2 = 5√2", lambda: nah(3 * 2 ** .5 - (-2 * 2 ** .5), 5 * 2 ** .5, 9)),
  (10, "A", "funktionen.ganzrational", "f(x) = 3 − 2x³, x = −1: 3 ⟦−⟧ (⟦−⟧2) = 3 + 2 = 5", lambda: 3 - 2 * (-1) ** 3 == 5)]),
 "rr.vorzeichen": ("Die Vorzeichen der Zahlen und das Vorzeichen des Ergebnisses. In Klasse 10 sind es drei Minus: Ein Umdrehen bleibt übrig.", [
  (5, "E", "zahlen.rechengesetze", "(⟦−⟧3) · (⟦−⟧4) = ⟦+⟧12", lambda: (-3) * (-4) == 12),
  (6, "A", "bruch.rechnen", "(⟦−⟧⅔) · (⟦−⟧¾) = ⟦+⟧½", lambda: -F(2, 3) * -F(3, 4) == F(1, 2)),
  (7, "A", "terme.umformen", "(⟦−⟧3x) · (⟦−⟧4) = ⟦+⟧12x", lambda: alle(lambda x: (-3 * x) * (-4), lambda x: 12 * x)),
  (8, "A", "funktionen.linear", "Steigung: (⟦−⟧6) : (⟦−⟧2) = ⟦+⟧3", lambda: F(-6, -2) == 3),
  (9, "A", "gleichungen.quadratisch", "(⟦−⟧5)² = (⟦−⟧5) · (⟦−⟧5) = ⟦+⟧25", lambda: (-5) ** 2 == 25),
  (10, "A", "funktionen.ganzrational", "(⟦−⟧2)³ = (⟦−⟧2) · (⟦−⟧2) · (⟦−⟧2) = ⟦−⟧8", lambda: (-2) ** 3 == -8)]),
 "rr.reihenfolge": ("Der Teil, der zuerst gerechnet wird – in jeder Zeile der Punkt-Teil hinter dem Plus. Steht darin ein Hoch (Klasse 9 und 10), kommt es noch davor.", [
  (5, "E", "zahlen.rechengesetze", "2 + ⟦3 · 4⟧ = 2 + 12 = 14", lambda: 2 + 3 * 4 == 14),
  (6, "A", "bruch.rechnen", "½ + ⟦½ · ½⟧ = ½ + ¼ = ¾", lambda: F(1, 2) + F(1, 2) * F(1, 2) == F(3, 4)),
  (7, "A", "terme.umformen", "2 + ⟦3 · x⟧ bleibt 2 + 3x – nicht 5x", lambda: not alle(lambda x: 2 + 3 * x, lambda x: 5 * x)),
  (8, "A", "funktionen.linear", "f(x) = 2 + 3x, x = 4: 2 + ⟦3 · 4⟧ = 14", lambda: 2 + 3 * 4 == 14),
  (9, "A", "funktionen.quadratisch", "f(x) = 2 + 3x², x = 2: 2 + ⟦3 · 2²⟧ = 14", lambda: 2 + 3 * 2 ** 2 == 14),
  (10, "A", "funktionen.exponential_log", "f(x) = 2 + 3 · 2ˣ, x = 2: 2 + ⟦3 · 2²⟧ = 14", lambda: 2 + 3 * 2 ** 2 == 14)]),
 "rr.tauschen": ("Der Summand, der wandert – immer zusammen mit seinem Rechenzeichen.", [
  (5, "E", "zahlen.ganz", "12 − 30 ⟦+ 18⟧ = 12 ⟦+ 18⟧ − 30 = 0", lambda: 12 - 30 + 18 == 12 + 18 - 30 == 0),
  (6, "A", "bruch.rechnen", "¼ − ½ ⟦+ ¾⟧ = ¼ ⟦+ ¾⟧ − ½ = ½", lambda: F(1, 4) - F(1, 2) + F(3, 4) == F(1, 2)),
  (7, "E", "terme.umformen", "3a + 2b ⟦+ 4a⟧ = 3a ⟦+ 4a⟧ + 2b = 7a + 2b", lambda: all(3 * a + 2 * b + 4 * a == 7 * a + 2 * b for a in (2, 3) for b in (5, 7))),
  (8, "A", "gleichungen.lgs2", "2x + 3y ⟦− 2x⟧ + y = 2x ⟦− 2x⟧ + 4y = 4y", lambda: all(2 * x + 3 * y - 2 * x + y == 4 * y for x in (2, 3) for y in (5, 7))),
  (9, "A", "zahlen.reell", "3√2 + 5 ⟦+ 2√2⟧ = 3√2 ⟦+ 2√2⟧ + 5 = 5√2 + 5", lambda: 3 + 2 == 5),
  (10, "A", "funktionen.ganzrational", "3x³ + 2x ⟦+ 4x³⟧ = 3x³ ⟦+ 4x³⟧ + 2x = 7x³ + 2x", lambda: alle(lambda x: 3 * x ** 3 + 2 * x + 4 * x ** 3, lambda x: 7 * x ** 3 + 2 * x))]),
 "rr.ausmultiplizieren": ("Der Faktor vor der Klammer – an allen drei Stellen, an denen er steht.", [
  (5, "E", "zahlen.rechengesetze", "⟦6⟧ · (20 + 2) = ⟦6⟧ · 20 + ⟦6⟧ · 2 = 132", lambda: 6 * 22 == 6 * 20 + 6 * 2 == 132),
  (6, "A", "bruch.rechnen", "⟦4⟧ · (2 + ½) = ⟦4⟧ · 2 + ⟦4⟧ · ½ = 10", lambda: 4 * (2 + F(1, 2)) == 10),
  (7, "E", "terme.umformen", "⟦3⟧ · (x + 2) = ⟦3⟧ · x + ⟦3⟧ · 2 = 3x + 6", lambda: alle(lambda x: 3 * (x + 2), lambda x: 3 * x + 6)),
  (8, "A", "gleichungen.bruch", "⟦x⟧ · (3/x + ½) = ⟦x⟧ · (3/x) + ⟦x⟧ · ½, für x ≠ 0", lambda: alle(lambda x: x * (3 / x + F(1, 2)), lambda x: 3 + x / 2)),
  (9, "A", "zahlen.reell", "⟦√2⟧ · (√2 + 3) = ⟦√2⟧ · √2 + ⟦√2⟧ · 3 = 2 + 3√2", lambda: nah(2 ** .5 * (2 ** .5 + 3), 2 + 3 * 2 ** .5, 9)),
  (10, "A", "gleichungen.polynom", "⟦x⟧ · (x² − 4) = ⟦x⟧ · x² − ⟦x⟧ · 4 = x³ − 4x", lambda: alle(lambda x: x * (x * x - 4), lambda x: x ** 3 - 4 * x))]),
 "rr.minusklammer": ("Das Minus vor der Klammer und das Zeichen in der Klammer, das wechselt.", [
  (5, "V", "zahlen.rechengesetze", "20 ⟦−⟧ (8 ⟦−⟧ 3) = 20 ⟦−⟧ 8 ⟦+⟧ 3 = 15", lambda: 20 - (8 - 3) == 20 - 8 + 3 == 15),
  (6, "V", "bruch.rechnen", "2 ⟦−⟧ (¾ ⟦−⟧ ¼) = 2 ⟦−⟧ ¾ ⟦+⟧ ¼ = 1½", lambda: 2 - (F(3, 4) - F(1, 4)) == 2 - F(3, 4) + F(1, 4) == F(3, 2)),
  (7, "E", "terme.umformen", "5x ⟦−⟧ (3x ⟦−⟧ 2) = 5x ⟦−⟧ 3x ⟦+⟧ 2 = 2x + 2", lambda: alle(lambda x: 5 * x - (3 * x - 2), lambda x: 2 * x + 2)),
  (8, "A", "gleichungen.ungleichungen", "7 ⟦−⟧ (2x ⟦−⟧ 6) = 7 ⟦−⟧ 2x ⟦+⟧ 6 = 13 − 2x", lambda: alle(lambda x: 7 - (2 * x - 6), lambda x: 13 - 2 * x)),
  (9, "A", "gleichungen.quadratisch", "x² ⟦−⟧ (x² ⟦−⟧ 3x) = x² ⟦−⟧ x² ⟦+⟧ 3x = 3x", lambda: alle(lambda x: x * x - (x * x - 3 * x), lambda x: 3 * x)),
  (10, "A", "gleichungen.polynom", "x³ ⟦−⟧ (x³ ⟦−⟧ 4x) = x³ ⟦−⟧ x³ ⟦+⟧ 4x = 4x", lambda: alle(lambda x: x ** 3 - (x ** 3 - 4 * x), lambda x: 4 * x))]),
 "rr.potenz": ("Die Hochzahlen: Sie zählen die Faktoren und werden beim Malnehmen addiert.", [
  (5, "E", "zahlen.potenzen_basis", "2⟦³⟧ · 2⟦²⟧ = (2 · 2 · 2) · (2 · 2) = 2⟦⁵⟧ = 32", lambda: 2 ** 3 * 2 ** 2 == 2 ** 5 == 32),
  (6, "A", "zahlen.potenzen_zehner", "10⟦³⟧ · 10⟦²⟧ = 10⟦⁵⟧ = 100 000", lambda: 10 ** 3 * 10 ** 2 == 10 ** 5),
  (7, "E", "terme.potenzgesetze_natuerlich", "x⟦³⟧ · x⟦²⟧ = (x · x · x) · (x · x) = x⟦⁵⟧", lambda: alle(lambda x: x ** 3 * x ** 2, lambda x: x ** 5)),
  (8, "E", "terme.potenzgesetze_ganzzahlig", "x⟦³⟧ · x⟦⁻²⟧ = x⟦¹⟧ = x, für x ≠ 0", lambda: alle(lambda x: x ** 3 * x ** -2, lambda x: x)),
  (9, "E", "zahlen.rationale_exponenten", "x^⟦½⟧ · x^⟦½⟧ = x⟦¹⟧ = x, für x ≥ 0", lambda: nah(9 ** .5 * 9 ** .5, 9, 9)),
  (10, "A", "funktionen.exponential_log", "2⟦ˣ⟧ · 2⟦³⟧ = 2⁽⟦ˣ⁺³⟧⁾", lambda: all(2 ** x * 2 ** 3 == 2 ** (x + 3) for x in range(1, 6)))]),
 "rr.kuerzen": ("Der gemeinsame Faktor – einmal im Zähler, einmal im Nenner.", [
  (5, None, NOCH_NICHT + " (Brüche ab Klasse 6)"),
  (6, "E", "bruch.brueche", "12/18 = (2 · ⟦6⟧) / (3 · ⟦6⟧) = 2/3", lambda: F(12, 18) == F(2, 3) and 2 * 6 == 12 and 3 * 6 == 18),
  (7, "A", "gleichungen.linear", "6x/9 = (2x · ⟦3⟧) / (3 · ⟦3⟧) = 2x/3", lambda: alle(lambda x: 6 * x / 9, lambda x: 2 * x / 3)),
  (8, "A", "terme.bruchterme", "(3 · ⟦(x + 2)⟧) / (1 · ⟦(x + 2)⟧) = 3, für x ≠ −2", lambda: alle(lambda x: (3 * x + 6) / (x + 2), lambda x: F(3), aus=(-2,))),
  (9, "A", "abbildungen.aehnlichkeit", "6 cm : 9 cm = (2 · ⟦3⟧) : (3 · ⟦3⟧) = 2 : 3", lambda: F(6, 9) == F(2, 3)),
  (10, "A", "stochastik.mehrstufig", "2/4 = (1 · ⟦2⟧) / (2 · ⟦2⟧) = ½", lambda: F(2, 4) == F(1, 2))]),
 "rr.bruchrechnen": ("Der gemeinsame Nenner – in jedem der drei Brüche.", [
  (5, None, NOCH_NICHT + " (Brüche ab Klasse 6)"),
  (6, "E", "bruch.rechnen", "1/2 + 1/3 = 3/⟦6⟧ + 2/⟦6⟧ = 5/⟦6⟧", lambda: F(1, 2) + F(1, 3) == F(5, 6)),
  (7, "A", "gleichungen.linear", "x/2 + x/3 = 3x/⟦6⟧ + 2x/⟦6⟧ = 5x/⟦6⟧", lambda: alle(lambda x: x / 2 + x / 3, lambda x: 5 * x / 6)),
  (8, "A", "terme.bruchterme", "1/x + 1/(2x) = 2/⟦(2x)⟧ + 1/⟦(2x)⟧ = 3/⟦(2x)⟧, für x ≠ 0", lambda: alle(lambda x: 1 / x + 1 / (2 * x), lambda x: 3 / (2 * x))),
  (9, "A", "stochastik.verknuepft", "1/2 + 1/3 − 1/6 = 3/⟦6⟧ + 2/⟦6⟧ − 1/⟦6⟧ = 4/⟦6⟧", lambda: F(1, 2) + F(1, 3) - F(1, 6) == F(2, 3)),
  (10, "A", "stochastik.mehrstufig", "1/6 + 1/3 = 1/⟦6⟧ + 2/⟦6⟧ = 3/⟦6⟧", lambda: F(1, 6) + F(1, 3) == F(1, 2))]),
 "rr.verhaeltnis": ("Die Eins in der Mitte: erst auf eins, dann auf viele.", [
  (5, "E", "groessen.proportional", "3 kg: 7,50 € → ⟦1 kg⟧: 2,50 € → 5 kg: 12,50 €", lambda: F(750, 3) == 250 and 250 * 5 == 1250),
  (6, "E", "bruch.prozent", "100 %: 60 € → ⟦1 %⟧: 0,60 € → 25 %: 15 €", lambda: F(60, 100) * 25 == 15),
  (7, "A", "bruch.prozent_grundwert", "80 %: 48 € → ⟦1 %⟧: 0,60 € → 100 %: 60 €", lambda: F(48, 80) * 100 == 60),
  (8, "A", "funktionen.linear", "x = 2: y = 3 → ⟦x = 1⟧: y = 1,5 → x = 4: y = 6", lambda: F(3, 2) * 4 == 6),
  (9, "A", "abbildungen.aehnlichkeit", "2 cm: 3 cm → ⟦1 cm⟧: 1,5 cm → 4 cm: 6 cm", lambda: F(3, 2) * 4 == 6),
  (10, "A", "funktionen.trig", "360°: 2π → ⟦1°⟧: π/180 → 90°: π/2", lambda: nah(math.pi / 180 * 90, math.pi / 2, 9))]),
 "rr.gegenrechnung": ("Die Rechnung und ihre Gegenrechnung – als Paar.", [
  (5, "E", "gleichungen.einfach", "□ ⟦+ 7⟧ = 3, also □ = 3 ⟦− 7⟧ = −4", lambda: -4 + 7 == 3),
  (6, "A", "bruch.rechnen", "□ ⟦· ¾⟧ = 12, also □ = 12 ⟦: ¾⟧ = 16", lambda: 16 * F(3, 4) == 12),
  (7, "A", "bruch.prozent_grundwert", "G ⟦· 1,2⟧ = 60 €, also G = 60 € ⟦: 1,2⟧ = 50 €", lambda: 50 * F(12, 10) == 60),
  (8, "A", "gleichungen.formeln", "A = g ⟦· h⟧, also g = A ⟦: h⟧ (für h ≠ 0)", lambda: 6 * 7 == 42),
  (9, "E", "gleichungen.quadratisch", "x ⟦hoch 2⟧ = 49, also x = ⟦±√⟧49 = ±7", lambda: 7 ** 2 == 49 == (-7) ** 2),
  (10, "E", "gleichungen.exponential", "2 ⟦hoch x⟧ = 8, also x = ⟦log₂⟧ 8 = 3", lambda: 2 ** 3 == 8)]),
 "rr.waage": ("Was auf beiden Seiten getan wird – der Befehl hinter dem Strich.", [
  (5, "V", "gleichungen.einfach", "□ + 7 = 3 | ⟦− 7⟧ → □ = −4", lambda: -4 + 7 == 3),
  (6, None, VORBEI + " (keine Gleichungen in Klasse 6)"),
  (7, "E", "gleichungen.linear", "2x + 2 = 12 | ⟦− 2⟧ → 2x = 10 | ⟦: 2⟧ → x = 5", lambda: 2 * 5 + 2 == 12),
  (8, "A", "gleichungen.ungleichungen", "2x + 2 < 12 | ⟦− 2⟧ → 2x < 10 | ⟦: 2⟧ → x < 5", lambda: all((2 * x + 2 < 12) == (x < 5) for x in range(-9, 12))),
  (9, "A", "gleichungen.quadratisch", "2x² + 2 = 20 | ⟦− 2⟧ → 2x² = 18 | ⟦: 2⟧ → x² = 9", lambda: 2 * 9 + 2 == 20),
  (10, "A", "gleichungen.exponential", "2 · 2ˣ + 2 = 18 | ⟦− 2⟧ → 2 · 2ˣ = 16 | ⟦: 2⟧ → 2ˣ = 8", lambda: 2 * 2 ** 3 + 2 == 18)]),
 "rr.nullprodukt": ("Die Null rechts und der Faktor, der null wird.", [
  (5, "V", "gleichungen.einfach", "⟦□⟧ · 7 = ⟦0⟧: □ = 0", lambda: [x for x in range(-5, 6) if x * 7 == 0] == [0]),
  (6, None, VORBEI), (7, None, VORBEI + " (Gleichungen mit x² erst ab Klasse 9)"),
  (8, "V", "terme.bruchterme", "Nenner ⟦x⟧ · ⟦(x − 4)⟧ ist ⟦null⟧ für x = 0 oder x = 4: beide Werte sind ausgeschlossen", lambda: [x for x in range(-5, 9) if x * (x - 4) == 0] == [0, 4]),
  (9, "E", "gleichungen.quadratisch", "⟦(x − 2)⟧ · ⟦(x + 3)⟧ = ⟦0⟧: x = 2 oder −3", lambda: [x for x in range(-9, 9) if (x - 2) * (x + 3) == 0] == [-3, 2]),
  (10, "A", "gleichungen.polynom", "⟦x⟧ · ⟦(x − 2)⟧ · ⟦(x + 2)⟧ = ⟦0⟧: x = 0, 2 oder −2", lambda: [x for x in range(-9, 9) if x * (x - 2) * (x + 2) == 0] == [-2, 0, 2])]),
}

# Tragende Ideen, Schlüssel = Kennung
LEITER_I = {
 "id.zahlen.zahlengerade": ("Das Kleiner-Zeichen: Links steht, was auf der Zahlengeraden weiter links liegt.", [
  (5, "E", "zahlen.ganz", "−3 ⟦<⟧ 2", lambda: -3 < 2),
  (6, "A", "bruch.rechnen", "−½ ⟦<⟧ ¼", lambda: -F(1, 2) < F(1, 4)),
  (7, None, VORBEI),
  (8, "A", "zahlen.intervalle", "Intervall ]−3; 2]: −3 ⟦<⟧ x ⟦≤⟧ 2", lambda: [x for x in range(-5, 5) if -3 < x <= 2] == [-2, -1, 0, 1, 2]),
  (9, "A", "zahlen.reell", "1 ⟦<⟧ √2 ⟦<⟧ 2", lambda: 1 < 2 ** .5 < 2),
  (10, None, VORBEI)]),
 "id.zahlen.buendeln": ("Die Zehn, die getauscht wird.", [
  (5, "E", "zahlen.natuerlich", "⟦10⟧ Einer = 1 Zehner", lambda: 10 * 1 == 10),
  (6, "E", "bruch.dezimal", "⟦10⟧ Zehntel = 1 Einer", lambda: F(9, 10) + F(1, 10) == 1),
  (7, None, VORBEI),
  (8, "A", "terme.potenzgesetze_ganzzahlig", "⟦10⟧ Tausendstel = 1 Hundertstel", lambda: 10 * F(10) ** -3 == F(10) ** -2),
  (9, None, VORBEI), (10, None, VORBEI)]),
 "id.zahlen.bausteine": ("Die Primfaktoren.", [
  (5, "E", "zahlen.teilbarkeit", "60 = ⟦2 · 2 · 3 · 5⟧", lambda: 2 * 2 * 3 * 5 == 60),
  (6, "A", "bruch.brueche", "12/18 = (⟦2 · 2 · 3⟧) / (⟦2 · 3 · 3⟧) = 2/3", lambda: F(12, 18) == F(2, 3)),
  (7, None, VORBEI), (8, None, VORBEI),
  (9, "A", "zahlen.wurzeln_basis", "√12 = √(⟦2 · 2 · 3⟧) = 2 · √3", lambda: nah(12 ** .5, 2 * 3 ** .5, 9)),
  (10, None, VORBEI)]),
 "id.zahlen.schreibweisen": ("Die Gleichheitszeichen zwischen den drei Schreibweisen.", [
  (5, None, NOCH_NICHT + " (Brüche ab Klasse 6)"),
  (6, "E", "bruch.prozent", "½ ⟦=⟧ 0,5 ⟦=⟧ 50 %", lambda: F(1, 2) == F(5, 10) == F(50, 100)),
  (7, "A", "bruch.prozent_grundwert", "⅕ ⟦=⟧ 0,2 ⟦=⟧ 20 %", lambda: F(1, 5) == F(2, 10) == F(20, 100)),
  (8, "A", "stochastik.grundbegriffe", "¼ ⟦=⟧ 0,25 ⟦=⟧ 25 %", lambda: F(1, 4) == F(25, 100)),
  (9, "A", "zahlen.reell", "⅓ ⟦=⟧ 0,333… ⟦≈⟧ 33,3 %", lambda: nah(1 / 3, 0.333, 3)),
  (10, None, BENUTZT)]),
 "id.zahlen.hoch_zurueck": ("Das Hoch – und ab Klasse 9 die Rechnung, die zurückfragt.", [
  (5, "E", "zahlen.potenzen_basis", "3 ⟦hoch 2⟧ = 9", lambda: 3 ** 2 == 9),
  (6, "A", "zahlen.potenzen_zehner", "10 ⟦hoch 3⟧ = 1 000", lambda: 10 ** 3 == 1000),
  (7, "A", "terme.potenzgesetze_natuerlich", "x ⟦hoch 2⟧ · x = x³", lambda: alle(lambda x: x ** 2 * x, lambda x: x ** 3)),
  (8, "A", "terme.potenzgesetze_ganzzahlig", "2 ⟦hoch −3⟧ = ⅛", lambda: F(2) ** -3 == F(1, 8)),
  (9, "E", "zahlen.wurzeln_basis", "3 ⟦hoch 2⟧ = 9 und zurück: ⟦√⟧9 = 3", lambda: 9 ** .5 == 3),
  (10, "E", "funktionen.exponential_log", "2 ⟦hoch 3⟧ = 8 und zurück: ⟦log₂⟧ 8 = 3", lambda: math.log2(8) == 3)]),
 "id.algebra.term": ("Die Zahl, die eingesetzt wird – die 5, in Klasse 10 die 2 (3⁵ wäre unhandlich).", [
  (5, "V", "zahlen.rechengesetze", "2 · ⟦5⟧ + 3 = 13", lambda: 2 * 5 + 3 == 13),
  (6, None, VORBEI),
  (7, "E", "terme.aufstellen", "T(⟦5⟧) = 2 · ⟦5⟧ + 3 = 13", lambda: 2 * 5 + 3 == 13),
  (8, "A", "funktionen.grundbegriffe", "f(⟦5⟧) = 2 · ⟦5⟧ + 3 = 13", lambda: 2 * 5 + 3 == 13),
  (9, "A", "funktionen.quadratisch", "f(⟦5⟧) = 2 · ⟦5⟧² + 3 = 53", lambda: 2 * 25 + 3 == 53),
  (10, "A", "funktionen.exponential_log", "f(x) = 2 · 3ˣ + 3; f(⟦2⟧) = 2 · 3⟦²⟧ + 3 = 21", lambda: 2 * 9 + 3 == 21)]),
 "id.algebra.erlaubte_zahlen": ("Die Bedingung für x: Kein Nenner wird 0, unter keiner Quadratwurzel steht etwas Negatives.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT),
  (8, "E", "terme.bruchterme", "1 : (x − 2): nicht erlaubt ⟦x = 2⟧", lambda: 2 - 2 == 0),
  (9, "A", "zahlen.wurzeln_basis", "√(x − 2): erlaubt nur ⟦x ≥ 2⟧", lambda: all((x - 2 >= 0) == (x >= 2) for x in range(-5, 9))),
  (10, "A", "funktionen.exponential_log", "log₂(x − 2): erlaubt nur ⟦x > 2⟧", lambda: all((x - 2 > 0) == (x > 2) for x in range(-5, 9)))]),
 "id.algebra.gleichung_loesen": ("Die Lösung – jede Zahl, für die die Zeile stimmt.", [
  (5, "E", "gleichungen.einfach", "□ + 7 = 3 stimmt für ⟦□ = −4⟧", lambda: [x for x in range(-20, 20) if x + 7 == 3] == [-4]),
  (6, None, VORBEI),
  (7, "E", "gleichungen.linear", "2x + 2 = 12 stimmt für ⟦x = 5⟧", lambda: [x for x in range(-20, 20) if 2 * x + 2 == 12] == [5]),
  (8, "E", "gleichungen.ungleichungen", "x + 5 < 2 stimmt für ⟦alle x < −3⟧", lambda: all((x + 5 < 2) == (x < -3) for x in range(-20, 20))),
  (9, "E", "gleichungen.quadratisch", "x² = 9 stimmt für ⟦x = 3⟧ und für ⟦x = −3⟧", lambda: [x for x in range(-20, 20) if x * x == 9] == [-3, 3]),
  (10, "A", "gleichungen.exponential", "2ˣ = 8 stimmt für ⟦x = 3⟧", lambda: [x for x in range(0, 20) if 2 ** x == 8] == [3])]),
 "id.algebra.hoeherer_grad": ("Die Null auf der rechten Seite – erst dann wird zerlegt.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT), (8, None, NOCH_NICHT),
  (9, "E", "gleichungen.quadratisch", "x² + x − 6 = ⟦0⟧ → (x − 2) · (x + 3) = ⟦0⟧", lambda: [x for x in range(-9, 9) if x * x + x - 6 == 0] == [-3, 2] and alle(lambda x: x * x + x - 6, lambda x: (x - 2) * (x + 3))),
  (10, "A", "gleichungen.polynom", "x³ − 4x = ⟦0⟧ → x · (x − 2) · (x + 2) = ⟦0⟧", lambda: alle(lambda x: x ** 3 - 4 * x, lambda x: x * (x - 2) * (x + 2)))]),
 "id.verhaeltnisse.groesse": ("Die beiden Zahlen an derselben Größe.", [
  (5, "E", "groessen.einheiten", "⟦3⟧ m = ⟦30⟧ dm", lambda: 3 * 10 == 30),
  (5, "E", "messen.flaechen", "⟦3⟧ m² = ⟦300⟧ dm²", lambda: 3 * 100 == 300),
  (6, "E", "messen.volumen", "⟦3⟧ m³ = ⟦3 000⟧ dm³", lambda: 3 * 1000 == 3000),
  (7, None, BENUTZT), (8, None, BENUTZT), (9, None, BENUTZT),
  (10, "A", "funktionen.trig", "⟦180⟧° = ⟦π⟧ im Bogenmaß", lambda: nah(math.radians(180), math.pi, 9))]),
 "id.verhaeltnisse.wert_fuer_eins": ("Das „· 2“ – es gilt für beide Größen zugleich.", [
  (5, "E", "groessen.proportional", "3 kg: 7,50 € ⟦· 2⟧ → 6 kg: 15 €", lambda: (3 * 2, F(15, 2) * 2) == (6, 15)),
  (6, "A", "bruch.prozent", "25 %: 15 € ⟦· 2⟧ → 50 %: 30 €", lambda: (25 * 2, 15 * 2) == (50, 30)),
  (7, "A", "bruch.prozent_grundwert", "40 %: 24 € ⟦· 2⟧ → 80 %: 48 €", lambda: (40 * 2, 24 * 2) == (80, 48)),
  (8, "A", "funktionen.linear", "x = 3: y = 7,5 ⟦· 2⟧ → x = 6: y = 15", lambda: F(5, 2) * 3 == F(15, 2) and F(5, 2) * 6 == 15),
  (9, "A", "abbildungen.aehnlichkeit", "3 cm: 4,5 cm ⟦· 2⟧ → 6 cm: 9 cm", lambda: F(9, 2) / 3 == F(9, 6) == F(3, 2)),
  (10, None, BENUTZT)]),
 "id.verhaeltnisse.prozent": ("Der Faktor, der aus dem Prozentsatz wird.", [
  (5, None, NOCH_NICHT + " (Prozent ab Klasse 6)"),
  (6, "E", "bruch.prozent", "25 % von 60 € = ⟦0,25⟧ · 60 € = 15 €", lambda: F(25, 100) * 60 == 15),
  (7, "E", "bruch.prozent_grundwert", "50 € plus 20 % = ⟦1,2⟧ · 50 € = 60 €", lambda: F(12, 10) * 50 == 60),
  (8, "A", "stochastik.grundbegriffe", "12 von 48: 12 : 48 = ⟦0,25⟧ = 25 %", lambda: F(12, 48) == F(25, 100)),
  (9, None, BENUTZT),
  (10, "A", "funktionen.exponential_log", "Zweimal plus 5 %: ⟦1,05⟧ · ⟦1,05⟧ · 1 000 € = 1 102,50 €", lambda: 1000 * F(105, 100) ** 2 == F(110250, 100))]),
 "id.geometrie.winkel": ("Die Summe 180° – die gerade Linie.", [
  (5, "E", "geometrie.grundbegriffe", "Gestreckter Winkel: 90° + 90° = ⟦180°⟧", lambda: 90 + 90 == 180),
  (6, None, VORBEI),
  (7, "E", "geometrie.winkelsaetze", "Dreieck: 50° + 60° + 70° = ⟦180°⟧", lambda: 50 + 60 + 70 == 180),
  (8, None, VORBEI),
  (9, "A", "trigo.rechtwinklig", "Rechtwinklig: 90° + 30° + 60° = ⟦180°⟧", lambda: 90 + 30 + 60 == 180),
  (10, None, BENUTZT)]),
 "id.geometrie.abstand": ("Der gleiche Abstand.", [
  (5, "E", "geometrie.ortslinien", "Kreis um M: alle Punkte ⟦3 cm⟧ von M", lambda: True),
  (6, None, VORBEI),
  (7, "E", "geometrie.konstruktion", "Mittelsenkrechte: von A und B ⟦gleich weit⟧", lambda: 2 ** 2 + 3 ** 2 == (2 - 4) ** 2 + 3 ** 2),
  (8, None, VORBEI),
  (9, "A", "trigo.pythagoras", "(3 | 4) ist vom Ursprung ⟦5⟧ entfernt", lambda: 3 ** 2 + 4 ** 2 == 5 ** 2),
  (10, None, VORBEI)]),
 "id.geometrie.deckungsgleich": ("Die Länge, die vorher und nachher gleich ist.", [
  (5, "V", "geometrie.grundbegriffe", "Rechteck: Gegenseiten ⟦gleich lang⟧", lambda: True),
  (6, None, VORBEI),
  (7, "E", "abbildungen.kongruenz", "Spiegeln: |AB| = ⟦3⟧, danach |A′B′| = ⟦3⟧", lambda: 5 - 2 == -2 - (-5) == 3),
  (8, None, VORBEI), (9, None, VORBEI + " (dort beginnt „Ähnlich“)"), (10, None, VORBEI)]),
 "id.geometrie.aehnlich": ("Der Faktor, mit dem jede Länge malgenommen wird.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT), (8, None, NOCH_NICHT),
  (9, "E", "abbildungen.aehnlichkeit", "3, 4, 5 cm ⟦· 2⟧ → 6, 8, 10 cm", lambda: (3 * 2, 4 * 2, 5 * 2) == (6, 8, 10)),
  (10, "A", "raum.pyramide_kegel_kugel", "Pyramide, Schnitt parallel zur Grundfläche auf halber Höhe: Die abgeschnittene Spitze hat halbe Kantenlängen (⟦· ½⟧) und ⅛ des ursprünglichen Volumens, der Stumpf ⅞", lambda: F(1, 2) ** 3 == F(1, 8) and 1 - F(1, 8) == F(7, 8))]),
 "id.geometrie.rechtwinklig": ("Die Quadrate der drei Seiten.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT), (8, None, NOCH_NICHT),
  (9, "E", "trigo.pythagoras", "Dreieck 3, 4, 5 cm: ⟦3² + 4² = 5²⟧", lambda: 3 ** 2 + 4 ** 2 == 5 ** 2),
  (10, "A", "raum.pyramide_kegel_kugel", "Kegel r = 3, h = 4, s = 5: ⟦3² + 4² = 5²⟧", lambda: 3 ** 2 + 4 ** 2 == 5 ** 2)]),
 "id.flaeche_raum.auslegen": ("Das, was gezählt wird: Reihen und Schichten.", [
  (5, "E", "messen.flaechen", "Rechteck: ⟦4 Reihen⟧ zu je 6 = 24 cm²", lambda: 4 * 6 == 24),
  (6, "E", "messen.volumen", "Quader: ⟦3 Schichten⟧ zu je 20 = 60 cm³", lambda: 3 * 20 == 60),
  (7, "A", "terme.aufstellen", "Rechteck: ⟦4 Reihen⟧ zu je x = 4x", lambda: True),
  (8, None, BENUTZT), (9, None, BENUTZT), (10, None, BENUTZT)]),
 "id.flaeche_raum.aus_dem_rechteck": ("Grundseite mal Höhe – das Rechteck, das in jeder Formel steckt. Längen in cm.", [
  (5, "E", "messen.flaechen", "Rechteck: ⟦6 · 4⟧ = 24 cm²", lambda: 6 * 4 == 24),
  (6, "E", "messen.flaechen_vielecke", "Parallelogramm: ⟦6 · 4⟧ = 24 cm²", lambda: 6 * 4 == 24),
  (6, "E", "messen.flaechen_vielecke", "Dreieck: ⟦6 · 4⟧ : 2 = 12 cm²", lambda: F(6 * 4, 2) == 12),
  (7, None, VORBEI),
  (8, "E", "messen.kreisberechnung", "Kreis, r = 3: ⟦π · 3 · 3⟧ ≈ 28,3 cm²", lambda: nah(math.pi * 9, 28.3, 1)),
  (9, "A", "trigo.pythagoras", "Gleichseitig, a = 6: ⟦6 · 5,2⟧ : 2 ≈ 15,6 cm²", lambda: nah(27 ** .5, 5.2, 1) and nah(6 * 27 ** .5 / 2, 15.6, 1)),
  (10, "A", "raum.pyramide_kegel_kugel", "Pyramidenmantel: 4 mal ⟦6 · 5⟧ : 2 = 60 cm²", lambda: 4 * (6 * 5 / 2) == 60)]),
 "id.flaeche_raum.aus_dem_quader": ("Grundfläche mal Höhe. Grundfläche in cm², Höhe in cm.", [
  (5, None, NOCH_NICHT + " (Volumen ab Klasse 6)"),
  (6, "E", "messen.volumen", "Quader: ⟦20 · 3⟧ = 60 cm³", lambda: 20 * 3 == 60),
  (7, None, VORBEI),
  (8, "E", "messen.prisma_zylinder", "Prisma: ⟦6 · 10⟧ = 60 cm³", lambda: 6 * 10 == 60),
  (9, None, VORBEI),
  (10, "E", "raum.pyramide_kegel_kugel", "Pyramide: ⟦36 · 4⟧ : 3 = 48 cm³", lambda: F(36 * 4, 3) == 48)]),
 "id.flaeche_raum.haut": ("Das Plus: Die Flächen der Haut werden zusammengezählt.", [
  (5, "E", "messen.koerper_berechnung", "Quader 5 · 4 · 3 cm: 2 · 20 ⟦+⟧ 2 · 15 ⟦+⟧ 2 · 12 = 94 cm²", lambda: 2 * 20 + 2 * 15 + 2 * 12 == 40 + 30 + 24 == 94),
  (6, None, VORBEI), (7, None, VORBEI),
  (8, "E", "messen.prisma_zylinder", "Gerades Prisma (Dreiecksseiten 3, 4, 5 cm, Höhe 6 cm): 2 · 6 ⟦+⟧ 18 ⟦+⟧ 24 ⟦+⟧ 30 = 84 cm²", lambda: 2 * 6 + 3 * 6 + 4 * 6 + 5 * 6 == 12 + 18 + 24 + 30 == 84),
  (9, None, VORBEI),
  (10, "E", "raum.pyramide_kegel_kugel", "Pyramide: 36 ⟦+⟧ 60 = 96 cm²", lambda: 36 + 4 * 15 == 36 + 60 == 96)]),
 "id.funktionen.zuordnung": ("Das Paar: zu diesem x genau dieses y.", [
  (5, "V", "groessen.proportional", "zu ⟦3 kg⟧ gehört ⟦7,50 €⟧", lambda: True),
  (6, None, VORBEI),
  (7, "V", "terme.aufstellen", "T(x) = 2x + 1: zu ⟦x = 3⟧ gehört ⟦7⟧", lambda: 2 * 3 + 1 == 7),
  (8, "E", "funktionen.grundbegriffe", "y = 2x + 1: zu ⟦x = 3⟧ gehört ⟦y = 7⟧", lambda: 2 * 3 + 1 == 7),
  (9, "A", "funktionen.quadratisch", "y = x²: zu ⟦x = 3⟧ gehört ⟦y = 9⟧", lambda: 3 ** 2 == 9),
  (10, "A", "funktionen.exponential_log", "y = 2ˣ: zu ⟦x = 3⟧ gehört ⟦y = 8⟧", lambda: 2 ** 3 == 8)]),
 "id.funktionen.wachstum": ("Der Schritt von einem Wert zum nächsten.", [
  (5, "V", "groessen.proportional", "Preis für 1, 2, 3 kg: 2,50 €; 5 €; 7,50 € – immer ⟦+ 2,50 €⟧", lambda: [F(5, 2) * k for k in (1, 2, 3)] == [F(5, 2), 5, F(15, 2)]),
  (6, None, VORBEI), (7, None, VORBEI),
  (8, "E", "funktionen.linear", "y = 1 + 2x: 1; 3; 5; 7 – immer ⟦+ 2⟧", lambda: [1 + 2 * x for x in range(4)] == [1, 3, 5, 7]),
  (9, None, VORBEI + " (quadratisch wächst weder in gleichen Schritten noch mit gleichem Faktor)"),
  (10, "E", "funktionen.exponential_log", "y = 2ˣ: 1; 2; 4; 8 – immer ⟦· 2⟧", lambda: [2 ** x for x in range(4)] == [1, 2, 4, 8])]),
 "id.funktionen.gleichung_form": ("Die Stelle in der Gleichung, die die Form bestimmt.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT),
  (8, "E", "funktionen.linear", "y = 2 · ⟦x⟧ + 1: Gerade", lambda: True),
  (8, "E", "funktionen.gebrochen", "y = 1 : ⟦x⟧: Hyperbel", lambda: True),
  (9, "E", "funktionen.quadratisch", "y = ⟦x²⟧: Parabel", lambda: (3 - 3) ** 2 == 0),
  (10, "E", "funktionen.ganzrational", "y = ⟦x³⟧ − 4x: drei Nullstellen", lambda: [x for x in range(-3, 4) if x ** 3 - 4 * x == 0] == [-2, 0, 2])]),
 "id.daten.kennzahl": ("Die eine Zahl, die für alle steht.", [
  (5, None, VORBEI),
  (6, "E", "daten.kennwerte", "4, 5, 5, 6: Mittelwert ⟦5⟧", lambda: F(20, 4) == 5),
  (7, "E", "daten.boxplot", "2, 3, 3, 4, 18: Median ⟦3⟧, Mittelwert 6", lambda: sorted([2, 3, 3, 4, 18])[2] == 3 and F(30, 5) == 6),
  (8, None, VORBEI), (9, None, VORBEI), (10, None, VORBEI)]),
 "id.daten.teil_ganzes": ("Der Anteil in der Stichprobe – er schätzt den Anteil im Ganzen.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT),
  (8, "E", "stochastik.grundbegriffe", "30 von 100 gezogenen Kugeln rot: ⟦30 %⟧", lambda: F(30, 100) == F(3, 10)),
  (9, None, VORBEI),
  (10, "A", "stochastik.simulation", "493 Treffer in 1 000 Versuchen: ⟦49,3 %⟧", lambda: F(493, 1000) == F(493, 10) / 100)]),
 "id.daten.anteil": ("Die Zahl der Möglichkeiten – ab Klasse 8 mit den günstigen davor.", [
  (5, "V", "stochastik.kombinatorik", "3 Hosen, 2 Hemden: 3 · 2 = ⟦6⟧ Möglichkeiten", lambda: 3 * 2 == 6),
  (6, None, VORBEI), (7, None, VORBEI),
  (8, "E", "stochastik.grundbegriffe", "Würfel, gerade Zahl: ⟦3 von 6⟧ = ½", lambda: F(3, 6) == F(1, 2)),
  (9, "A", "stochastik.verknuepft", "Würfel, gerade oder über 4: ⟦4 von 6⟧ = ⅔", lambda: len([x for x in range(1, 7) if x % 2 == 0 or x > 4]) == 4),
  (10, "A", "stochastik.mehrstufig", "Zweimal Kopf: ⟦1 von 4⟧ = ¼", lambda: F(1, 4) == F(1, 2) ** 2)]),
 "id.daten.stufen": ("Das Mal entlang des Pfades.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT), (8, None, NOCH_NICHT),
  (9, None, NOCH_NICHT + " (Klasse 9 arbeitet mit der Vierfeldertafel, noch ohne Pfade)"),
  (10, "E", "stochastik.mehrstufig", "Kopf, dann Zahl: ½ ⟦·⟧ ½ = ¼", lambda: F(1, 2) * F(1, 2) == F(1, 4)),
  (10, "E", "stochastik.mehrstufig", "Genau einmal Kopf: ¼ ⟦+⟧ ¼ = ½", lambda: 2 * F(1, 4) == F(1, 2))]),
}

# alte Etikett-Nummer → Kennung (dieselbe Zuordnung wie in kennungen.py; dort wird sie geprüft)
ETIKETT = {13: "rr.stellenwert", 1: "rr.plusminus", 2: "rr.vorzeichen", 3: "rr.reihenfolge", 6: "rr.tauschen", 4: "rr.ausmultiplizieren", 5: "rr.minusklammer",
           12: "rr.potenz", 10: "rr.kuerzen", 11: "rr.bruchrechnen", 14: "rr.verhaeltnis", 8: "rr.gegenrechnung", 7: "rr.waage", 15: "rr.nullprodukt"}
ARTNAME = {"V": "Vorwissen", "E": "Einführung", "A": "Anwendung"}


def leiter_tabelle(zeilen):
    """Markdown-Tabelle einer Leiter; die wirkende Stelle bleibt mit ⟦…⟧ markiert."""
    t = ["| Klasse | Beispiel (wirkende Stelle in ⟦ ⟧) | Art | Thema der App |", "|---|---|---|---|"]
    for z in zeilen:
        if z[1] is None:
            t.append(f"| {z[0]} | *{z[2]}* | – | – |")
        else:
            t.append(f"| {z[0]} | {z[3].replace('|', '&#124;')} | {ARTNAME[z[1]]} | `{z[2]}` |")
    return "\n".join(t)
