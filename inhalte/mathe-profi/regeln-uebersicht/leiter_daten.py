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
  (7, "A", "bruch.prozent_grundwert", "0,15 ⟦· 100⟧ = 15, also 0,15 = 15 %", lambda: F(15, 100) * 100 == 15),
  (8, "A", "terme.potenzgesetze_ganzzahlig", "3 ⟦· 10⁻⁴⟧ = 0,0003", lambda: 3 * F(10) ** -4 == F(3, 10000)),
  (9, None, BENUTZT), (10, None, BENUTZT)]),
 "rr.plusminus": ("Die zwei Minuszeichen nebeneinander: Rechenzeichen und Vorzeichen.", [
  (5, "E", "zahlen.ganz", "3 ⟦−⟧ (⟦−⟧2) = 3 + 2 = 5", lambda: 3 - (-2) == 5),
  (6, "A", "bruch.rechnen", "½ ⟦−⟧ (⟦−⟧¼) = ½ + ¼ = ¾", lambda: F(1, 2) - (-F(1, 4)) == F(3, 4)),
  (7, "A", "terme.umformen", "3x ⟦−⟧ (⟦−⟧2x) = 3x + 2x = 5x", lambda: alle(lambda x: 3 * x - (-2 * x), lambda x: 5 * x)),
  (8, "A", "funktionen.linear", "f(x) = 3 − x an der Stelle −2: 3 ⟦−⟧ (⟦−⟧2) = 3 + 2 = 5", lambda: 3 - (-2) == 5),
  (9, "A", "zahlen.reell", "3√2 ⟦−⟧ (⟦−⟧2√2) = 3√2 + 2√2 = 5√2", lambda: nah(3 * 2 ** .5 - (-2 * 2 ** .5), 5 * 2 ** .5, 9)),
  (10, "A", "funktionen.ganzrational", "f(x) = 3 − 2x³ an der Stelle −1: 3 ⟦−⟧ (⟦−⟧2) = 3 + 2 = 5", lambda: 3 - 2 * (-1) ** 3 == 5)]),
 "rr.vorzeichen": ("Die Vorzeichen der beiden Zahlen und das Vorzeichen des Ergebnisses.", [
  (5, "E", "zahlen.rechengesetze", "(⟦−⟧3) · (⟦−⟧4) = ⟦+⟧12", lambda: (-3) * (-4) == 12),
  (6, "A", "bruch.rechnen", "(⟦−⟧⅔) · (⟦−⟧¾) = ⟦+⟧½", lambda: -F(2, 3) * -F(3, 4) == F(1, 2)),
  (7, "A", "terme.umformen", "(⟦−⟧3x) · (⟦−⟧4) = ⟦+⟧12x", lambda: alle(lambda x: (-3 * x) * (-4), lambda x: 12 * x)),
  (8, "A", "funktionen.linear", "Steigung aus zwei Punkten: (⟦−⟧6) : (⟦−⟧2) = ⟦+⟧3", lambda: F(-6, -2) == 3),
  (9, "A", "gleichungen.quadratisch", "(⟦−⟧5)² = (⟦−⟧5) · (⟦−⟧5) = ⟦+⟧25", lambda: (-5) ** 2 == 25),
  (10, "A", "funktionen.ganzrational", "(⟦−⟧2)³ = (⟦−⟧2) · (⟦−⟧2) · (⟦−⟧2) = ⟦−⟧8 – drei Minus: einmal umdrehen bleibt übrig", lambda: (-2) ** 3 == -8)]),
 "rr.reihenfolge": ("Der Teil, der zuerst gerechnet wird – in jeder Zeile der Punkt-Teil hinter dem Plus.", [
  (5, "E", "zahlen.rechengesetze", "2 + ⟦3 · 4⟧ = 2 + 12 = 14", lambda: 2 + 3 * 4 == 14),
  (6, "A", "bruch.rechnen", "½ + ⟦½ · ½⟧ = ½ + ¼ = ¾", lambda: F(1, 2) + F(1, 2) * F(1, 2) == F(3, 4)),
  (7, "A", "terme.umformen", "2 + ⟦3 · x⟧ bleibt 2 + 3x – nicht 5x", lambda: not alle(lambda x: 2 + 3 * x, lambda x: 5 * x)),
  (8, "A", "funktionen.linear", "f(x) = 2 + 3x an der Stelle 4: 2 + ⟦3 · 4⟧ = 2 + 12 = 14", lambda: 2 + 3 * 4 == 14),
  (9, "A", "funktionen.quadratisch", "f(x) = 2 + 3x² an der Stelle 2: 2 + ⟦3 · 2²⟧ = 2 + 3 · 4 = 14 – im Punkt-Teil zuerst das Hoch", lambda: 2 + 3 * 2 ** 2 == 14),
  (10, "A", "funktionen.exponential_log", "f(x) = 2 + 3 · 2ˣ an der Stelle 2: 2 + ⟦3 · 2²⟧ = 2 + 3 · 4 = 14", lambda: 2 + 3 * 2 ** 2 == 14)]),
 "rr.tauschen": ("Der Summand, der wandert – immer zusammen mit seinem Rechenzeichen.", [
  (5, "E", "zahlen.ganz", "12 − 30 ⟦+ 18⟧ = 12 ⟦+ 18⟧ − 30 = 0", lambda: 12 - 30 + 18 == 12 + 18 - 30 == 0),
  (6, "A", "bruch.rechnen", "¼ − ½ ⟦+ ¾⟧ = ¼ ⟦+ ¾⟧ − ½ = ½", lambda: F(1, 4) - F(1, 2) + F(3, 4) == F(1, 2)),
  (7, "E", "terme.umformen", "3a + 2b ⟦+ 4a⟧ = 3a ⟦+ 4a⟧ + 2b = 7a + 2b", lambda: all(3 * a + 2 * b + 4 * a == 7 * a + 2 * b for a in (2, 3) for b in (5, 7))),
  (8, "A", "gleichungen.lgs2", "Zwei Gleichungen addieren: 2x + 3y ⟦− 2x⟧ + y = 2x ⟦− 2x⟧ + 3y + y = 4y", lambda: all(2 * x + 3 * y - 2 * x + y == 4 * y for x in (2, 3) for y in (5, 7))),
  (9, "A", "zahlen.reell", "3√2 + 5 ⟦+ 2√2⟧ = 3√2 ⟦+ 2√2⟧ + 5 = 5√2 + 5", lambda: 3 + 2 == 5),
  (10, "A", "funktionen.ganzrational", "3x³ + 2x ⟦+ 4x³⟧ = 3x³ ⟦+ 4x³⟧ + 2x = 7x³ + 2x", lambda: alle(lambda x: 3 * x ** 3 + 2 * x + 4 * x ** 3, lambda x: 7 * x ** 3 + 2 * x))]),
 "rr.ausmultiplizieren": ("Der Faktor vor der Klammer – an allen drei Stellen, an denen er steht.", [
  (5, "E", "zahlen.rechengesetze", "⟦6⟧ · (20 + 2) = ⟦6⟧ · 20 + ⟦6⟧ · 2 = 132", lambda: 6 * 22 == 6 * 20 + 6 * 2 == 132),
  (6, "A", "bruch.rechnen", "⟦4⟧ · (2 + ½) = ⟦4⟧ · 2 + ⟦4⟧ · ½ = 10", lambda: 4 * (2 + F(1, 2)) == 10),
  (7, "E", "terme.umformen", "⟦3⟧ · (x + 2) = ⟦3⟧ · x + ⟦3⟧ · 2 = 3x + 6", lambda: alle(lambda x: 3 * (x + 2), lambda x: 3 * x + 6)),
  (8, "A", "gleichungen.bruch", "⟦x⟧ · (3/x + ½) = ⟦x⟧ · 3/x + ⟦x⟧ · ½ = 3 + x/2, für x ≠ 0", lambda: alle(lambda x: x * (3 / x + F(1, 2)), lambda x: 3 + x / 2)),
  (9, "A", "zahlen.reell", "⟦√2⟧ · (√2 + 3) = ⟦√2⟧ · √2 + ⟦√2⟧ · 3 = 2 + 3√2", lambda: nah(2 ** .5 * (2 ** .5 + 3), 2 + 3 * 2 ** .5, 9)),
  (10, "A", "gleichungen.polynom", "⟦x⟧ · (x² − 4) = ⟦x⟧ · x² − ⟦x⟧ · 4 = x³ − 4x", lambda: alle(lambda x: x * (x * x - 4), lambda x: x ** 3 - 4 * x))]),
 "rr.minusklammer": ("Das Minus vor der Klammer und das Zeichen in der Klammer, das wechselt.", [
  (5, "V", "zahlen.rechengesetze", "20 ⟦−⟧ (8 ⟦−⟧ 3) = 20 ⟦−⟧ 8 ⟦+⟧ 3 = 15", lambda: 20 - (8 - 3) == 20 - 8 + 3 == 15),
  (6, "V", "bruch.rechnen", "2 ⟦−⟧ (¾ ⟦−⟧ ¼) = 2 ⟦−⟧ ¾ ⟦+⟧ ¼ = 1½", lambda: 2 - (F(3, 4) - F(1, 4)) == 2 - F(3, 4) + F(1, 4) == F(3, 2)),
  (7, "E", "terme.umformen", "5x ⟦−⟧ (3x ⟦−⟧ 2) = 5x ⟦−⟧ 3x ⟦+⟧ 2 = 2x + 2", lambda: alle(lambda x: 5 * x - (3 * x - 2), lambda x: 2 * x + 2)),
  (8, "A", "gleichungen.ungleichungen", "7 ⟦−⟧ (2x ⟦−⟧ 6) = 7 ⟦−⟧ 2x ⟦+⟧ 6 = 13 − 2x", lambda: alle(lambda x: 7 - (2 * x - 6), lambda x: 13 - 2 * x)),
  (9, "A", "gleichungen.quadratisch", "(x + 1)² ⟦−⟧ (x² ⟦−⟧ 3) = x² + 2x + 1 ⟦−⟧ x² ⟦+⟧ 3 = 2x + 4", lambda: alle(lambda x: (x + 1) ** 2 - (x * x - 3), lambda x: 2 * x + 4)),
  (10, "A", "gleichungen.polynom", "x³ ⟦−⟧ (x³ ⟦−⟧ 4x) = x³ ⟦−⟧ x³ ⟦+⟧ 4x = 4x", lambda: alle(lambda x: x ** 3 - (x ** 3 - 4 * x), lambda x: 4 * x))]),
 "rr.potenz": ("Die Hochzahlen: Sie zählen die Faktoren und werden beim Malnehmen addiert.", [
  (5, "E", "zahlen.potenzen_basis", "2⟦³⟧ · 2⟦²⟧ = (2 · 2 · 2) · (2 · 2) = 2⟦⁵⟧ = 32", lambda: 2 ** 3 * 2 ** 2 == 2 ** 5 == 32),
  (6, "A", "zahlen.potenzen_zehner", "10⟦³⟧ · 10⟦²⟧ = 10⟦⁵⟧ = 100 000", lambda: 10 ** 3 * 10 ** 2 == 10 ** 5),
  (7, "E", "terme.potenzgesetze_natuerlich", "x⟦³⟧ · x⟦²⟧ = (x · x · x) · (x · x) = x⟦⁵⟧", lambda: alle(lambda x: x ** 3 * x ** 2, lambda x: x ** 5)),
  (8, "E", "terme.potenzgesetze_ganzzahlig", "x⟦³⟧ · x⟦⁻²⟧ = x⟦¹⟧ = x, für x ≠ 0", lambda: alle(lambda x: x ** 3 * x ** -2, lambda x: x)),
  (9, "E", "zahlen.rationale_exponenten", "x^⟦½⟧ · x^⟦½⟧ = x⟦¹⟧ = x, für x ≥ 0 – also ist x^½ die Wurzel aus x", lambda: nah(9 ** .5 * 9 ** .5, 9, 9)),
  (10, "A", "funktionen.exponential_log", "2⟦ˣ⟧ · 2⟦³⟧ = 2 hoch ⟦x + 3⟧", lambda: all(2 ** x * 2 ** 3 == 2 ** (x + 3) for x in range(1, 6)))]),
 "rr.kuerzen": ("Der gemeinsame Faktor – einmal im Zähler, einmal im Nenner.", [
  (5, None, NOCH_NICHT + " (Brüche ab Klasse 6)"),
  (6, "E", "bruch.brueche", "12/18 = (2 · ⟦6⟧) / (3 · ⟦6⟧) = 2/3", lambda: F(12, 18) == F(2, 3) and 2 * 6 == 12 and 3 * 6 == 18),
  (7, "A", "gleichungen.linear", "6x/9 = (2x · ⟦3⟧) / (3 · ⟦3⟧) = 2x/3", lambda: alle(lambda x: 6 * x / 9, lambda x: 2 * x / 3)),
  (8, "A", "terme.bruchterme", "(3x + 6) / (x + 2) = (3 · ⟦(x + 2)⟧) / (1 · ⟦(x + 2)⟧) = 3, für x ≠ −2", lambda: alle(lambda x: (3 * x + 6) / (x + 2), lambda x: F(3), aus=(-2,))),
  (9, "A", "abbildungen.aehnlichkeit", "Seitenverhältnis 6 cm : 9 cm = (2 · ⟦3⟧) : (3 · ⟦3⟧) = 2 : 3", lambda: F(6, 9) == F(2, 3)),
  (10, "A", "stochastik.mehrstufig", "Zweiter Zug aus der Urne: 2/4 = (1 · ⟦2⟧) / (2 · ⟦2⟧) = ½", lambda: F(2, 4) == F(1, 2))]),
 "rr.bruchrechnen": ("Der gemeinsame Nenner – in jedem der drei Brüche.", [
  (5, None, NOCH_NICHT + " (Brüche ab Klasse 6)"),
  (6, "E", "bruch.rechnen", "1/2 + 1/3 = 3/⟦6⟧ + 2/⟦6⟧ = 5/⟦6⟧", lambda: F(1, 2) + F(1, 3) == F(5, 6)),
  (7, "A", "gleichungen.linear", "x/2 + x/3 = 3x/⟦6⟧ + 2x/⟦6⟧ = 5x/⟦6⟧", lambda: alle(lambda x: x / 2 + x / 3, lambda x: 5 * x / 6)),
  (8, "A", "terme.bruchterme", "1/x + 1/(2x) = 2/⟦2x⟧ + 1/⟦2x⟧ = 3/⟦2x⟧, für x ≠ 0", lambda: alle(lambda x: 1 / x + 1 / (2 * x), lambda x: 3 / (2 * x))),
  (9, "A", "stochastik.verknuepft", "Additionssatz: 1/2 + 1/3 − 1/6 = 3/⟦6⟧ + 2/⟦6⟧ − 1/⟦6⟧ = 4/⟦6⟧ = ⅔", lambda: F(1, 2) + F(1, 3) - F(1, 6) == F(2, 3)),
  (10, "A", "stochastik.mehrstufig", "Zwei Pfade addieren: 1/6 + 1/3 = 1/⟦6⟧ + 2/⟦6⟧ = 3/⟦6⟧ = ½", lambda: F(1, 6) + F(1, 3) == F(1, 2))]),
 "rr.verhaeltnis": ("Die mittlere Zeile: der Wert für eins.", [
  (5, "E", "groessen.proportional", "3 kg kosten 7,50 € → ⟦1 kg kostet 2,50 €⟧ → 5 kg kosten 12,50 €", lambda: F(750, 3) == 250 and 250 * 5 == 1250),
  (6, "E", "bruch.prozent", "100 % sind 60 € → ⟦1 % sind 0,60 €⟧ → 25 % sind 15 €", lambda: F(60, 100) * 25 == 15),
  (7, "A", "bruch.prozent_grundwert", "80 % sind 48 € → ⟦1 % sind 0,60 €⟧ → 100 % sind 60 €", lambda: F(48, 80) * 100 == 60),
  (8, "A", "funktionen.linear", "2 nach rechts, 3 nach oben → ⟦1 nach rechts, 1,5 nach oben⟧ → 4 nach rechts, 6 nach oben (Steigung 1,5)", lambda: F(3, 2) * 4 == 6),
  (9, "A", "abbildungen.aehnlichkeit", "2 cm gehören zu 3 cm → ⟦1 cm gehört zu 1,5 cm⟧ → 4 cm gehören zu 6 cm (Strahlensatz)", lambda: F(3, 2) * 4 == 6),
  (10, "A", "funktionen.trig", "360° sind 2π → ⟦1° ist π/180⟧ → 90° sind π/2 (Bogenmaß)", lambda: nah(math.pi / 180 * 90, math.pi / 2, 9))]),
 "rr.gegenrechnung": ("Die Rechnung und ihre Gegenrechnung – als Paar.", [
  (5, "E", "gleichungen.einfach", "□ ⟦+ 7⟧ = 3, also □ = 3 ⟦− 7⟧ = −4", lambda: -4 + 7 == 3),
  (6, "A", "bruch.rechnen", "□ ⟦· ¾⟧ = 12, also □ = 12 ⟦: ¾⟧ = 16", lambda: 16 * F(3, 4) == 12),
  (7, "A", "bruch.prozent_grundwert", "G ⟦· 1,2⟧ = 60 €, also G = 60 € ⟦: 1,2⟧ = 50 €", lambda: 50 * F(12, 10) == 60),
  (8, "A", "gleichungen.formeln", "A = g ⟦· h⟧, also g = A ⟦: h⟧ – mit A = 42 und h = 7 ist g = 6", lambda: 6 * 7 == 42),
  (9, "E", "gleichungen.quadratisch", "x ⟦hoch 2⟧ = 49, also x = ⟦±√⟧49: x = 7 oder x = −7", lambda: 7 ** 2 == 49 == (-7) ** 2),
  (10, "E", "gleichungen.exponential", "2 ⟦hoch x⟧ = 8, also x = ⟦log₂⟧ 8 = 3", lambda: 2 ** 3 == 8)]),
 "rr.waage": ("Was auf beiden Seiten getan wird – der Befehl hinter dem Strich.", [
  (5, "V", "gleichungen.einfach", "□ + 7 = 3 | ⟦− 7⟧ → □ = −4", lambda: -4 + 7 == 3),
  (6, None, VORBEI + " (keine Gleichungen in Klasse 6)"),
  (7, "E", "gleichungen.linear", "2x + 2 = 12 | ⟦− 2⟧ → 2x = 10 | ⟦: 2⟧ → x = 5", lambda: 2 * 5 + 2 == 12),
  (8, "A", "gleichungen.ungleichungen", "2x + 2 < 12 | ⟦− 2⟧ → 2x < 10 | ⟦: 2⟧ → x < 5", lambda: all((2 * x + 2 < 12) == (x < 5) for x in range(-9, 12))),
  (9, "A", "gleichungen.quadratisch", "2x² + 2 = 20 | ⟦− 2⟧ → 2x² = 18 | ⟦: 2⟧ → x² = 9", lambda: 2 * 9 + 2 == 20),
  (10, "A", "gleichungen.exponential", "2 · 2ˣ + 2 = 18 | ⟦− 2⟧ → 2 · 2ˣ = 16 | ⟦: 2⟧ → 2ˣ = 8", lambda: 2 * 2 ** 3 + 2 == 18)]),
 "rr.nullprodukt": ("Die Null rechts und der Faktor, der null wird.", [
  (5, "V", "gleichungen.einfach", "⟦□⟧ · 7 = ⟦0⟧, also □ = 0", lambda: [x for x in range(-5, 6) if x * 7 == 0] == [0]),
  (6, None, VORBEI), (7, None, VORBEI + " (Gleichungen mit x² erst ab Klasse 9)"),
  (8, "V", "terme.bruchterme", "Der Nenner ⟦x⟧ · ⟦(x − 4)⟧ wird ⟦0⟧ für x = 0 oder x = 4 – diese Zahlen sind nicht erlaubt", lambda: [x for x in range(-5, 9) if x * (x - 4) == 0] == [0, 4]),
  (9, "E", "gleichungen.quadratisch", "⟦(x − 2)⟧ · ⟦(x + 3)⟧ = ⟦0⟧, also x = 2 oder x = −3", lambda: [x for x in range(-9, 9) if (x - 2) * (x + 3) == 0] == [-3, 2]),
  (10, "A", "gleichungen.polynom", "⟦x⟧ · ⟦(x − 2)⟧ · ⟦(x + 2)⟧ = ⟦0⟧, also x = 0, x = 2 oder x = −2", lambda: [x for x in range(-9, 9) if x * (x - 2) * (x + 2) == 0] == [-2, 0, 2])]),
}

# Tragende Ideen, Schlüssel = Kennung
LEITER_I = {
 "id.zahlen.zahlengerade": ("Das Kleiner-Zeichen: Links steht, was auf der Zahlengeraden weiter links liegt.", [
  (5, "E", "zahlen.ganz", "−3 ⟦<⟧ 2 – die −3 liegt links von der 2", lambda: -3 < 2),
  (6, "A", "bruch.rechnen", "−½ ⟦<⟧ ¼", lambda: -F(1, 2) < F(1, 4)),
  (7, None, VORBEI),
  (8, "A", "zahlen.intervalle", "Im Intervall ]−3; 2] liegen alle Zahlen mit −3 ⟦<⟧ x ⟦≤⟧ 2", lambda: [x for x in range(-5, 5) if -3 < x <= 2] == [-2, -1, 0, 1, 2]),
  (9, "A", "zahlen.reell", "1 ⟦<⟧ √2 ⟦<⟧ 2 – auch √2 ≈ 1,41 hat ihren Platz", lambda: 1 < 2 ** .5 < 2),
  (10, None, VORBEI)]),
 "id.zahlen.buendeln": ("Die Zehn, die getauscht wird.", [
  (5, "E", "zahlen.natuerlich", "⟦10⟧ Einer = 1 Zehner: 347 liegt zwischen 340 und 350", lambda: 340 < 347 < 350),
  (6, "E", "bruch.dezimal", "⟦10⟧ Zehntel = 1 Einer: 0,9 + 0,1 = 1,0", lambda: F(9, 10) + F(1, 10) == 1),
  (7, None, VORBEI),
  (8, "A", "terme.potenzgesetze_ganzzahlig", "⟦10⟧ Tausendstel = 1 Hundertstel: 10 · 10⁻³ = 10⁻²", lambda: 10 * F(10) ** -3 == F(10) ** -2),
  (9, None, VORBEI), (10, None, VORBEI)]),
 "id.zahlen.bausteine": ("Die Primfaktoren.", [
  (5, "E", "zahlen.teilbarkeit", "60 = ⟦2 · 2 · 3 · 5⟧", lambda: 2 * 2 * 3 * 5 == 60),
  (6, "A", "bruch.brueche", "12/18 = (⟦2 · 2 · 3⟧) / (⟦2 · 3 · 3⟧) = 2/3 – gemeinsame Bausteine 2 und 3 kürzen", lambda: F(12, 18) == F(2, 3)),
  (7, None, VORBEI), (8, None, VORBEI),
  (9, "A", "zahlen.wurzeln_basis", "√12 = √(⟦2 · 2 · 3⟧) = 2 · √3", lambda: nah(12 ** .5, 2 * 3 ** .5, 9)),
  (10, None, VORBEI)]),
 "id.zahlen.schreibweisen": ("Die Gleichheitszeichen zwischen den drei Schreibweisen.", [
  (5, None, NOCH_NICHT + " (Brüche ab Klasse 6)"),
  (6, "E", "bruch.prozent", "½ ⟦=⟧ 0,5 ⟦=⟧ 50 %", lambda: F(1, 2) == F(5, 10) == F(50, 100)),
  (7, "A", "bruch.prozent_grundwert", "⅕ ⟦=⟧ 0,2 ⟦=⟧ 20 %", lambda: F(1, 5) == F(2, 10) == F(20, 100)),
  (8, "A", "stochastik.grundbegriffe", "Wahrscheinlichkeit ¼ ⟦=⟧ 0,25 ⟦=⟧ 25 %", lambda: F(1, 4) == F(25, 100)),
  (9, "A", "zahlen.reell", "⅓ ⟦=⟧ 0,333… – eine Kommazahl, die nie endet, aber sich wiederholt", lambda: nah(1 / 3, 0.333, 3)),
  (10, None, BENUTZT)]),
 "id.zahlen.hoch_zurueck": ("Das Hoch – und ab Klasse 9 die Rechnung, die zurückfragt.", [
  (5, "E", "zahlen.potenzen_basis", "3 ⟦hoch 2⟧ = 9", lambda: 3 ** 2 == 9),
  (6, "A", "zahlen.potenzen_zehner", "10 ⟦hoch 3⟧ = 1 000", lambda: 10 ** 3 == 1000),
  (7, "A", "terme.potenzgesetze_natuerlich", "x ⟦hoch 2⟧ · x = x³", lambda: alle(lambda x: x ** 2 * x, lambda x: x ** 3)),
  (8, "A", "terme.potenzgesetze_ganzzahlig", "2 ⟦hoch −3⟧ = ⅛", lambda: F(2) ** -3 == F(1, 8)),
  (9, "E", "zahlen.wurzeln_basis", "3 ⟦hoch 2⟧ = 9 und zurück: ⟦√⟧9 = 3", lambda: 9 ** .5 == 3),
  (10, "E", "funktionen.exponential_log", "2 ⟦hoch 3⟧ = 8 und zurück: ⟦log₂⟧ 8 = 3", lambda: math.log2(8) == 3)]),
 "id.algebra.term": ("Die Zahl, die eingesetzt wird – in jeder Zeile die 5.", [
  (5, "V", "zahlen.rechengesetze", "2 · ⟦5⟧ + 3 = 13", lambda: 2 * 5 + 3 == 13),
  (6, None, VORBEI),
  (7, "E", "terme.aufstellen", "T(x) = 2 · x + 3; T(⟦5⟧) = 2 · ⟦5⟧ + 3 = 13", lambda: 2 * 5 + 3 == 13),
  (8, "A", "funktionen.grundbegriffe", "f(x) = 2 · x + 3; f(⟦5⟧) = 2 · ⟦5⟧ + 3 = 13", lambda: 2 * 5 + 3 == 13),
  (9, "A", "funktionen.quadratisch", "f(x) = 2 · x² + 3; f(⟦5⟧) = 2 · ⟦5⟧² + 3 = 53", lambda: 2 * 25 + 3 == 53),
  (10, "A", "funktionen.exponential_log", "f(x) = 2 · 3ˣ + 3; f(⟦2⟧) = 2 · 3² + 3 = 21 – hier die 2, weil 3⁵ unhandlich wird", lambda: 2 * 9 + 3 == 21)]),
 "id.algebra.erlaubte_zahlen": ("Die Zahl, die nicht eingesetzt werden darf.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT),
  (8, "E", "terme.bruchterme", "1 : (x − 2): nicht erlaubt ist ⟦x = 2⟧, denn der Nenner wäre 0", lambda: 2 - 2 == 0),
  (9, "A", "zahlen.wurzeln_basis", "√(x − 2): erlaubt ist nur ⟦x ≥ 2⟧, denn unter der Wurzel darf nichts Negatives stehen", lambda: all((x - 2 >= 0) == (x >= 2) for x in range(-5, 9))),
  (10, "A", "funktionen.exponential_log", "log₂(x − 2): erlaubt ist nur ⟦x > 2⟧", lambda: all((x - 2 > 0) == (x > 2) for x in range(-5, 9)))]),
 "id.algebra.gleichung_loesen": ("Die Lösung – jede Zahl, für die die Zeile stimmt.", [
  (5, "E", "gleichungen.einfach", "□ + 7 = 3 stimmt für ⟦□ = −4⟧", lambda: [x for x in range(-20, 20) if x + 7 == 3] == [-4]),
  (6, None, VORBEI),
  (7, "E", "gleichungen.linear", "2x + 2 = 12 stimmt für ⟦x = 5⟧", lambda: [x for x in range(-20, 20) if 2 * x + 2 == 12] == [5]),
  (8, "E", "gleichungen.ungleichungen", "x + 5 < 2 stimmt für ⟦alle x < −3⟧", lambda: all((x + 5 < 2) == (x < -3) for x in range(-20, 20))),
  (9, "E", "gleichungen.quadratisch", "x² = 9 stimmt für ⟦x = 3⟧ und für ⟦x = −3⟧", lambda: [x for x in range(-20, 20) if x * x == 9] == [-3, 3]),
  (10, "A", "gleichungen.exponential", "2ˣ = 8 stimmt für ⟦x = 3⟧", lambda: [x for x in range(0, 20) if 2 ** x == 8] == [3])]),
 "id.algebra.hoeherer_grad": ("Die Null auf der einen Seite und die Faktoren auf der anderen.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT), (8, None, NOCH_NICHT),
  (9, "E", "gleichungen.quadratisch", "x² + x = 6 → x² + x − 6 = ⟦0⟧ → ⟦(x − 2) · (x + 3)⟧ = ⟦0⟧ → x = 2 oder x = −3", lambda: [x for x in range(-9, 9) if x * x + x == 6] == [-3, 2]),
  (10, "A", "gleichungen.polynom", "x³ = 4x → x³ − 4x = ⟦0⟧ → ⟦x · (x − 2) · (x + 2)⟧ = ⟦0⟧ → x = 0, x = 2 oder x = −2", lambda: [x for x in range(-9, 9) if x ** 3 == 4 * x] == [-2, 0, 2])]),
 "id.verhaeltnisse.groesse": ("Die beiden Zahlen an derselben Größe.", [
  (5, "E", "groessen.einheiten", "⟦3⟧ m = ⟦30⟧ dm", lambda: 3 * 10 == 30),
  (5, "E", "messen.flaechen", "⟦3⟧ m² = ⟦300⟧ dm²", lambda: 3 * 100 == 300),
  (6, "E", "messen.volumen", "⟦3⟧ m³ = ⟦3 000⟧ dm³", lambda: 3 * 1000 == 3000),
  (7, None, BENUTZT), (8, None, BENUTZT), (9, None, BENUTZT),
  (10, "A", "funktionen.trig", "⟦180⟧° = ⟦π⟧ im Bogenmaß – andere Einheit, andere Zahl", lambda: nah(math.radians(180), math.pi, 9))]),
 "id.verhaeltnisse.wert_fuer_eins": ("Das „· 2“ auf beiden Seiten.", [
  (5, "E", "groessen.proportional", "3 kg kosten 7,50 €; ⟦doppelt so viel⟧: 6 kg kosten ⟦doppelt so viel⟧: 15 €", lambda: F(15, 2) * 2 == 15),
  (6, "A", "bruch.prozent", "25 % sind 15 €; ⟦doppelt so viel⟧: 50 % sind ⟦doppelt so viel⟧: 30 €", lambda: 15 * 2 == 30),
  (7, "A", "bruch.prozent_grundwert", "40 % sind 24 €; ⟦doppelt so viel⟧: 80 % sind ⟦doppelt so viel⟧: 48 €", lambda: 24 * 2 == 48),
  (8, "A", "funktionen.linear", "y = 2,5 · x: zu x = 3 gehört 7,5; zu ⟦doppeltem⟧ x = 6 gehört das ⟦Doppelte⟧: 15", lambda: F(5, 2) * 3 == F(15, 2) and F(5, 2) * 6 == 15),
  (9, "A", "abbildungen.aehnlichkeit", "Im Bild mit Faktor 2 ist jede Länge ⟦doppelt so lang⟧: aus 3 cm werden 6 cm, aus 4 cm werden 8 cm", lambda: (3 * 2, 4 * 2) == (6, 8)),
  (10, None, BENUTZT)]),
 "id.verhaeltnisse.prozent": ("Der Faktor, der aus dem Prozentsatz wird.", [
  (5, None, NOCH_NICHT + " (Prozent ab Klasse 6)"),
  (6, "E", "bruch.prozent", "25 % von 60 € = ⟦0,25⟧ · 60 € = 15 €", lambda: F(25, 100) * 60 == 15),
  (7, "E", "bruch.prozent_grundwert", "50 € plus 20 % = ⟦1,2⟧ · 50 € = 60 €", lambda: F(12, 10) * 50 == 60),
  (8, "A", "stochastik.grundbegriffe", "12 von 48 Würfen: 12 : 48 = ⟦0,25⟧ = 25 %", lambda: F(12, 48) == F(25, 100)),
  (9, None, BENUTZT),
  (10, "A", "funktionen.exponential_log", "1 000 € zwei Jahre lang plus 5 %: ⟦1,05⟧ · ⟦1,05⟧ · 1 000 € = 1 102,50 €", lambda: 1000 * F(105, 100) ** 2 == F(110250, 100))]),
 "id.geometrie.winkel": ("Die Winkel, die zusammen eine feste Summe ergeben.", [
  (5, "E", "geometrie.grundbegriffe", "Volle Drehung: ⟦90° + 90° + 90° + 90°⟧ = 360°", lambda: 4 * 90 == 360),
  (6, None, VORBEI),
  (7, "E", "geometrie.winkelsaetze", "Dreieck: ⟦50° + 60° + 70°⟧ = 180°", lambda: 50 + 60 + 70 == 180),
  (8, None, VORBEI),
  (9, "A", "trigo.rechtwinklig", "Rechtwinkliges Dreieck: ⟦90° + 30° + 60°⟧ = 180° – die zwei spitzen Winkel ergeben 90°", lambda: 90 + 30 + 60 == 180),
  (10, None, BENUTZT)]),
 "id.geometrie.abstand": ("Der gleiche Abstand.", [
  (5, "E", "geometrie.ortslinien", "Alle Punkte, die von M ⟦3 cm⟧ entfernt sind: Kreis um M mit Radius ⟦3 cm⟧", lambda: True),
  (6, None, VORBEI),
  (7, "E", "geometrie.konstruktion", "A(0 | 0), B(4 | 0): Der Punkt (2 | 3) ist von A und von B ⟦gleich weit⟧ entfernt – er liegt auf der Mittelsenkrechten", lambda: 2 ** 2 + 3 ** 2 == (2 - 4) ** 2 + 3 ** 2),
  (8, None, VORBEI),
  (9, "A", "trigo.pythagoras", "Der Punkt (3 | 4) ist vom Ursprung ⟦5⟧ entfernt, denn 3² + 4² = ⟦5⟧²", lambda: 3 ** 2 + 4 ** 2 == 5 ** 2),
  (10, None, VORBEI)]),
 "id.geometrie.deckungsgleich": ("Die Länge, die vorher und nachher gleich ist.", [
  (5, "V", "geometrie.grundbegriffe", "Im Rechteck sind gegenüberliegende Seiten ⟦gleich lang⟧", lambda: True),
  (6, None, VORBEI),
  (7, "E", "abbildungen.kongruenz", "Spiegeln an der y-Achse: A(2 | 1) → A′(−2 | 1), B(5 | 1) → B′(−5 | 1); die Strecke ist vorher ⟦3⟧ lang und nachher ⟦3⟧", lambda: 5 - 2 == -2 - (-5) == 3),
  (8, None, VORBEI), (9, None, VORBEI + " (dort beginnt „Ähnlich“)"), (10, None, VORBEI)]),
 "id.geometrie.aehnlich": ("Der Faktor, mit dem jede Länge malgenommen wird.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT), (8, None, NOCH_NICHT),
  (9, "E", "abbildungen.aehnlichkeit", "Dreieck 3 cm, 4 cm, 5 cm ⟦· 2⟧ → 6 cm, 8 cm, 10 cm; alle Winkel bleiben", lambda: (3 * 2, 4 * 2, 5 * 2) == (6, 8, 10)),
  (10, "A", "raum.pyramide_kegel_kugel", "Schneidet man eine Pyramide auf halber Höhe ab, ist die kleine Pyramide ähnlich: Kanten ⟦· ½⟧, Volumen · ⅛", lambda: F(1, 2) ** 3 == F(1, 8))]),
 "id.geometrie.rechtwinklig": ("Die Quadrate der drei Seiten.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT), (8, None, NOCH_NICHT),
  (9, "E", "trigo.pythagoras", "Katheten 3 cm und 4 cm: ⟦3² + 4² = 5²⟧, die Hypotenuse ist 5 cm lang", lambda: 3 ** 2 + 4 ** 2 == 5 ** 2),
  (10, "A", "raum.pyramide_kegel_kugel", "Kegel mit r = 3 cm und h = 4 cm: ⟦3² + 4² = 5²⟧, die Mantellinie ist 5 cm lang", lambda: 3 ** 2 + 4 ** 2 == 5 ** 2)]),
 "id.flaeche_raum.auslegen": ("Das Zählen in Reihen und Schichten.", [
  (5, "E", "messen.flaechen", "Rechteck 6 cm mal 4 cm: ⟦4 Reihen zu je 6⟧ = 24 cm²", lambda: 4 * 6 == 24),
  (6, "E", "messen.volumen", "Quader 5 cm, 4 cm, 3 cm: ⟦3 Schichten zu je 20⟧ = 60 cm³", lambda: 3 * 20 == 60),
  (7, "A", "terme.aufstellen", "Rechteck mit den Seiten x und 4: ⟦4 Reihen zu je x⟧ = 4x", lambda: True),
  (8, None, BENUTZT), (9, None, BENUTZT), (10, None, BENUTZT)]),
 "id.flaeche_raum.aus_dem_rechteck": ("Die Grundseite mal die Höhe – das Rechteck, das in jeder Formel steckt.", [
  (5, "E", "messen.flaechen", "Rechteck: ⟦6 cm · 4 cm⟧ = 24 cm²", lambda: 6 * 4 == 24),
  (6, "E", "messen.flaechen_vielecke", "Parallelogramm: ⟦6 cm · 4 cm⟧ = 24 cm². Dreieck: ⟦6 cm · 4 cm⟧ : 2 = 12 cm²", lambda: (6 * 4, 6 * 4 / 2) == (24, 12)),
  (7, None, VORBEI),
  (8, "E", "messen.kreisberechnung", "Kreis mit r = 3 cm, umgelegt zu einem Fast-Rechteck: ⟦π · 3 cm · 3 cm⟧ ≈ 28,3 cm²", lambda: nah(math.pi * 9, 28.3, 1)),
  (9, "A", "trigo.pythagoras", "Gleichseitiges Dreieck mit Seite 6 cm: Höhe √27 cm ≈ 5,2 cm, also ⟦6 cm · 5,2 cm⟧ : 2 ≈ 15,6 cm²", lambda: nah(27 ** .5, 5.2, 1) and nah(6 * 27 ** .5 / 2, 15.6, 1)),
  (10, "A", "raum.pyramide_kegel_kugel", "Mantel der Pyramide (Grundkante 6 cm, Seitenhöhe 5 cm): vier Dreiecke, je ⟦6 cm · 5 cm⟧ : 2 = 15 cm², zusammen 60 cm²", lambda: 4 * (6 * 5 / 2) == 60)]),
 "id.flaeche_raum.aus_dem_quader": ("Grundfläche mal Höhe.", [
  (5, None, NOCH_NICHT + " (Volumen ab Klasse 6)"),
  (6, "E", "messen.volumen", "Quader: ⟦20 cm² · 3 cm⟧ = 60 cm³", lambda: 20 * 3 == 60),
  (7, None, VORBEI),
  (8, "E", "messen.prisma_zylinder", "Prisma mit dreieckiger Grundfläche: ⟦6 cm² · 10 cm⟧ = 60 cm³", lambda: 6 * 10 == 60),
  (9, None, VORBEI),
  (10, "E", "raum.pyramide_kegel_kugel", "Pyramide: ⟦36 cm² · 4 cm⟧ : 3 = 48 cm³", lambda: F(36 * 4, 3) == 48)]),
 "id.flaeche_raum.haut": ("Die Flächen, die zusammengezählt werden.", [
  (5, "E", "messen.koerper_berechnung", "Quader 5 cm, 4 cm, 3 cm: ⟦2 · 20 + 2 · 15 + 2 · 12⟧ = 94 cm²", lambda: 2 * 20 + 2 * 15 + 2 * 12 == 94),
  (6, None, VORBEI), (7, None, VORBEI),
  (8, "E", "messen.prisma_zylinder", "Prisma (Dreieck 3 cm, 4 cm, 5 cm; Höhe 6 cm): ⟦2 · 6 + 18 + 24 + 30⟧ = 84 cm²", lambda: 2 * 6 + 3 * 6 + 4 * 6 + 5 * 6 == 84),
  (9, None, VORBEI),
  (10, "E", "raum.pyramide_kegel_kugel", "Pyramide (Grundkante 6 cm, Seitenhöhe 5 cm): ⟦36 + 4 · 15⟧ = 96 cm²", lambda: 36 + 4 * 15 == 96)]),
 "id.funktionen.zuordnung": ("Das Paar: zu diesem x genau dieses y.", [
  (5, "V", "groessen.proportional", "Zu ⟦3 kg⟧ gehört genau ein Preis: ⟦7,50 €⟧", lambda: True),
  (6, None, VORBEI),
  (7, "V", "terme.aufstellen", "T(x) = 2x + 1: zu ⟦x = 3⟧ gehört ⟦7⟧", lambda: 2 * 3 + 1 == 7),
  (8, "E", "funktionen.grundbegriffe", "y = 2x + 1: zu ⟦x = 3⟧ gehört ⟦y = 7⟧", lambda: 2 * 3 + 1 == 7),
  (9, "A", "funktionen.quadratisch", "y = x²: zu ⟦x = 3⟧ gehört ⟦y = 9⟧", lambda: 3 ** 2 == 9),
  (10, "A", "funktionen.exponential_log", "y = 2ˣ: zu ⟦x = 3⟧ gehört ⟦y = 8⟧", lambda: 2 ** 3 == 8)]),
 "id.funktionen.wachstum": ("Der Schritt von einem Wert zum nächsten.", [
  (5, "V", "groessen.proportional", "Je Kilogramm ⟦+ 2,50 €⟧: 2,50 €; 5 €; 7,50 €", lambda: [F(5, 2) * k for k in (1, 2, 3)] == [F(5, 2), 5, F(15, 2)]),
  (6, None, VORBEI), (7, None, VORBEI),
  (8, "E", "funktionen.linear", "y = 1 + 2x: von Schritt zu Schritt ⟦+ 2⟧: 1; 3; 5; 7; 9", lambda: [1 + 2 * x for x in range(5)] == [1, 3, 5, 7, 9]),
  (9, None, VORBEI + " (quadratisch wächst weder in gleichen Schritten noch mit gleichem Faktor)"),
  (10, "E", "funktionen.exponential_log", "y = 2ˣ: von Schritt zu Schritt ⟦· 2⟧: 1; 2; 4; 8; 16", lambda: [2 ** x for x in range(5)] == [1, 2, 4, 8, 16])]),
 "id.funktionen.gleichung_form": ("Die Stelle in der Gleichung, die die Form bestimmt.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT),
  (8, "E", "funktionen.linear", "y = 2 · ⟦x⟧ + 1: Gerade", lambda: True),
  (8, "E", "funktionen.gebrochen", "y = 1 : ⟦x⟧: Hyperbel", lambda: True),
  (9, "E", "funktionen.quadratisch", "y = ⟦x²⟧: Parabel. y = (x − 3)²: dieselbe Parabel, 3 nach rechts", lambda: (3 - 3) ** 2 == 0),
  (10, "E", "funktionen.ganzrational", "y = ⟦x³⟧ − 4x: Kurve mit drei Nullstellen −2, 0, 2", lambda: [x for x in range(-3, 4) if x ** 3 - 4 * x == 0] == [-2, 0, 2])]),
 "id.daten.kennzahl": ("Die eine Zahl, die für alle steht.", [
  (5, None, VORBEI),
  (6, "E", "daten.kennwerte", "4, 5, 5, 6: Mittelwert ⟦5⟧. Und 1, 2, 8, 9: Mittelwert auch ⟦5⟧", lambda: F(20, 4) == 5),
  (7, "E", "daten.boxplot", "2, 3, 3, 4, 18: Median ⟦3⟧, Mittelwert 6 – der Ausreißer zieht nur den Mittelwert mit", lambda: sorted([2, 3, 3, 4, 18])[2] == 3 and F(30, 5) == 6),
  (8, None, VORBEI), (9, None, VORBEI), (10, None, VORBEI)]),
 "id.daten.teil_ganzes": ("Der Anteil in der Stichprobe.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT),
  (8, "E", "stochastik.grundbegriffe", "Von 100 zufällig gezogenen Kugeln sind 30 rot: geschätzter Anteil ⟦30 %⟧", lambda: F(30, 100) == F(3, 10)),
  (9, None, VORBEI),
  (10, "A", "stochastik.simulation", "Ein Versuch wird sehr oft nachgespielt; der ⟦Anteil der Treffer⟧ schätzt die Wahrscheinlichkeit", lambda: True)]),
 "id.daten.anteil": ("Günstige durch mögliche.", [
  (5, "V", "stochastik.kombinatorik", "3 Hosen und 2 Hemden: 3 · 2 = ⟦6 Möglichkeiten⟧", lambda: 3 * 2 == 6),
  (6, None, VORBEI), (7, None, VORBEI),
  (8, "E", "stochastik.grundbegriffe", "Würfel, gerade Zahl: ⟦3 von 6⟧ = ½", lambda: F(3, 6) == F(1, 2)),
  (9, "A", "stochastik.verknuepft", "Würfel, „gerade oder größer als 4“: günstig sind 2, 4, 5, 6 – ⟦4 von 6⟧ = ⅔", lambda: len([x for x in range(1, 7) if x % 2 == 0 or x > 4]) == 4),
  (10, "A", "stochastik.mehrstufig", "Zwei Münzwürfe, zweimal Kopf: ⟦1 von 4⟧ = ¼", lambda: F(1, 4) == F(1, 2) ** 2)]),
 "id.daten.stufen": ("Das Mal entlang des Pfades.", [
  (5, None, NOCH_NICHT), (6, None, NOCH_NICHT), (7, None, NOCH_NICHT), (8, None, NOCH_NICHT),
  (9, None, NOCH_NICHT + " (Klasse 9 arbeitet mit der Vierfeldertafel, noch ohne Pfade)"),
  (10, "E", "stochastik.mehrstufig", "Zwei Münzwürfe, erst Kopf, dann Zahl: ½ ⟦·⟧ ½ = ¼. Genau einmal Kopf: ¼ ⟦+⟧ ¼ = ½", lambda: F(1, 2) * F(1, 2) == F(1, 4) and 2 * F(1, 4) == F(1, 2))]),
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
