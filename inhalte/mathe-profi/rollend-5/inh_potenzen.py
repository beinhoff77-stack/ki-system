"""rollend-5 · zahlen.potenzen_basis (7 Lernkarten, 21 Aufgaben)."""
from k5basis import *      # noqa: F401,F403

TH = "zahlen.potenzen_basis"
PO, HZ, VZ = "rr.potenz", "id.zahlen.hoch_zurueck", "rr.vorzeichen"

# ── schreibweise ──
neu(TH, "schreibweise", "fehler_detektiv", "fehler", FDZ(
    "Kim schreibt 5 · 5 · 5 · 5 als Potenz und rechnet sie aus.",
    [("Die Basis ist 5. Sie kommt 4-mal als Faktor vor.", True), ("Als Potenz: 5⁴.", 5 ** 4 == 5 * 5 * 5 * 5), ("Ausgerechnet: 5⁴ = 5 · 4 = 20.", 5 ** 4 == 5 * 4)],
    "Was sagt der Exponent: Wie oft kommt die Basis als Faktor vor?", "5⁴ = 5 · 5 · 5 · 5 = 625. Der Exponent zählt die Faktoren, er wird nicht mit der Basis malgenommen."), PO)
neu(TH, "schreibweise", "bruecke", "darstellung", W(
    "Die Zahl 3 kommt sechsmal als Faktor vor. Welche Schreibweise gehört dazu?",
    "3⁶", [("6³", "Basis und Exponent vertauscht"), ("3 · 6", "als Malaufgabe mit nur zwei Faktoren"), ("3 + 6", "Plus statt Mal")],
    "Die Basis ist die Zahl, die malgenommen wird. Der Exponent sagt, wie oft.", "Sechs Faktoren 3: 3 · 3 · 3 · 3 · 3 · 3 = 3⁶ = 729. Die Potenz 6³ wäre 216.",
    3 ** 6 == 3 * 3 * 3 * 3 * 3 * 3 and 6 ** 3 != 3 ** 6 and 3 * 6 != 3 ** 6 and 3 + 6 != 3 ** 6), PO)
neu(TH, "schreibweise", "umkehren", "umkehr", Z(
    "Eine Potenz hat die Basis 2 und den Wert 64. Welcher Exponent steht dort?",
    "6", str(next(e for e in range(1, 20) if 2 ** e == 64)), "Multipliziere 2 · 2 · … so lange, bis du bei 64 bist, und zähle die Zweier.", "2 · 2 = 4, · 2 = 8, 16, 32, 64: sechs Faktoren. Also 2⁶ = 64.",
    [(32, None, "die Hälfte statt des Exponenten genannt"), (5, None, "einen Faktor zu wenig gezählt")]), PO)

# ── berechnen ──
neu(TH, "berechnen", "lueckenweg", "direkt", L(
    "Du rechnest 3⁴ = 3 · 3 · 3 · 3 Schritt für Schritt. Erst 3 · 3 = ①. Dann ① · 3 = ②. Dann ② · 3 = ③.",
    ["3*3", "3*3*3", "3*3*3*3"], ["9", "27", "81"], "Immer das letzte Ergebnis noch einmal mit 3 malnehmen.", "3 · 3 = 9, 9 · 3 = 27, 27 · 3 = 81.",
    {2: [(12, "fb.potenz.basis_mal_hochzahl", "3 · 4 gerechnet")]}), PO)
neu(TH, "berechnen", "zwei_wege", "mehrschritt", Z(
    "Berechne 4³. Weg A: 4 · 4 · 4 in einem Zug. Weg B: erst 4 · 4 = 16, dann 16 · 4. Wie groß ist das Ergebnis?",
    "4**3", "4*4*4", "Beide Wege geben dieselbe Zahl. 4³ ist nicht 4 · 3.", "Weg A: 4 · 4 · 4 = 64. Weg B: 16 · 4 = 64.",
    [(12, "fb.potenz.basis_mal_hochzahl", "4 · 3 gerechnet"), (16, None, "nach dem ersten Schritt aufgehört")]), PO)
neu(TH, "berechnen", "anwenden", "einkleidung", Z(
    "Eine Bakterienkultur verdoppelt sich jede Stunde. Am Anfang sind es 5 Bakterien. Wie viele Bakterien sind es nach 4 Stunden?",
    "5*2**4", "5*2*2*2*2", "Nach jeder Stunde mal 2. Das sind 4 Verdopplungen.", "2⁴ = 16. 5 · 16 = 80 Bakterien.",
    [(40, None, "nur dreimal verdoppelt"), (160, None, "fünfmal verdoppelt")]), PO)

# ── quadrat ──
neu(TH, "quadrat", "fehler_detektiv", "fehler", FDZ(
    "Kim berechnet 13² und die Fläche eines Quadrats.",
    [("13² heißt 13 · 2.", 13 ** 2 == 13 * 2), ("13 · 2 = 26.", 13 * 2 == 26), ("Ein Quadrat mit 13 cm Seitenlänge hat also 26 cm² Fläche.", True)],
    "Wie oft steht die 13 als Faktor da?", "13² heißt 13 · 13 = 169. Ein Quadrat mit 13 cm Seite hat 169 cm² Fläche."), HZ)
assert 14 * 14 == 196
neu(TH, "quadrat", "umkehren", "umkehr", Z(
    "Ein Quadrat hat die Fläche 196 cm². Wie lang ist eine Seite in cm?",
    "14", "14", "Welche Zahl mal sich selbst gibt 196? Probiere bei 10 und 15.", "14 · 14 = 196. Die Seite ist 14 cm lang.",
    [(98, None, "durch 2 geteilt"), (49, None, "durch 4 geteilt")], einheit="cm"), HZ)
neu(TH, "quadrat", "anwenden", "einkleidung", Z(
    "Ein quadratischer Spielplatz ist 18 m lang und 18 m breit. Er wird mit Platten zu je 1 m² ausgelegt. Wie viele Platten braucht man?",
    "18**2", "18*18", "Fläche eines Quadrats: Seite mal Seite.", "18² = 18 · 18 = 324. Es sind 324 Platten.",
    [(36, "fb.potenz.basis_mal_hochzahl", "18 · 2 gerechnet"), (72, None, "den Umfang genommen")]), PO)

# ── vertauschen ──
neu(TH, "vertauschen", "lueckenweg", "direkt", L(
    "Beachte: 5³ ist nicht 3⁵. Es ist 5³ = 5 · 5 · 5 = ①. Es ist 3⁵ = 3 · 3 · 3 · 3 · 3 = ②. Der Unterschied ist ② − ① = ③.",
    ["5**3", "3**5", "3**5-5**3"], ["125", "243", "118"], "Zähle die Faktoren: Der Exponent sagt, wie oft die Basis dasteht.", "5³ = 125. 3⁵ = 243. 243 − 125 = 118.",
    {0: [(15, "fb.potenz.basis_mal_hochzahl", "5 · 3 gerechnet")]}), PO)
neu(TH, "vertauschen", "zwei_wege", "mehrschritt", Z(
    "Vergleiche 4³ und 3⁴. Weg A: beide Potenzen einzeln ausrechnen. Weg B: beide als Mal-Kette schreiben und rechnen. Um wie viel ist 3⁴ größer als 4³?",
    "3**4-4**3", "81-64", "Die Zahlen sind dieselben, aber die Rollen sind vertauscht.", "4³ = 64. 3⁴ = 81. 81 − 64 = 17.",
    [(-17, None, "falsch herum abgezogen")]), PO)
neu(TH, "vertauschen", "anwenden", "einkleidung", Z(
    "Schloss A hat 5 Rädchen mit je 2 Symbolen. Seine Einstellungen zählt man mit 2⁵. Schloss B hat 2 Rädchen mit je 5 Symbolen. Seine Einstellungen zählt man mit 5². Wie viele Einstellungen hat Schloss A mehr als Schloss B?",
    "2**5-5**2", "32-25", "Rechne beide Potenzen getrennt aus.", "2⁵ = 32. 5² = 25. 32 − 25 = 7.",
    [(-7, None, "falsch herum abgezogen")]), PO)

# ── zehner ──
neu(TH, "zehner", "fehler_detektiv", "fehler", FDZ(
    "Kim schreibt 7 · 10⁴ als Zahl.",
    [("10⁴ ist eine 1 mit vier Nullen: 10 000.", 10 ** 4 == 10000), ("7 · 10⁴ heißt: 7 mal 10 000.", True), ("Das ist die 7 mit vier Nullen dahinter.", 7 * 10 ** 4 == int("7" + "0" * 4)), ("Also ist 7 · 10⁴ = 700 000.", 7 * 10 ** 4 == 700000)],
    "Zähle die Nullen in deiner Zahl und vergleiche mit dem Exponenten.", "7 und vier Nullen sind 70 000, nicht 700 000."), PO)
neu(TH, "zehner", "bruecke", "darstellung", W(
    "Welche Schreibweise ist gleich der Zahl 3 400 000?",
    "34 · 10⁵", [("34 · 10⁶", "eine Null zu viel"), ("34 · 10⁴", "eine Null zu wenig"), ("340 · 10⁵", "eine Stelle zu viel")],
    "Wie viele Nullen stehen hinter der 34?", "3 400 000 = 34 und fünf Nullen = 34 · 10⁵.",
    34 * 10 ** 5 == 3400000 and 34 * 10 ** 6 != 3400000 and 34 * 10 ** 4 != 3400000 and 340 * 10 ** 5 != 3400000), PO)
neu(TH, "zehner", "umkehren", "umkehr", Z(
    "Die Zahl 25 000 000 000 soll als 25 · 10ⁿ geschrieben werden. Welche Zahl ist n?",
    "9", str(len(str(25000000000)) - 2), "Zähle die Nullen hinter der 25.", "25 000 000 000 hat hinter der 25 genau 9 Nullen. n = 9.",
    [(11, None, "alle Ziffern der Zahl gezählt"), (2, None, "die Ziffern der 25 gezählt")]), PO)

# ── negativ ──
neu(TH, "negativ", "lueckenweg", "direkt", L(
    "Du rechnest (−2)⁴ = (−2) · (−2) · (−2) · (−2). Erst (−2) · (−2) = ①. Dann ① · (−2) = ②. Dann ② · (−2) = ③.",
    ["(-2)*(-2)", "(-2)*(-2)*(-2)", "(-2)**4"], ["4", "-8", "16"], "Gleiche Vorzeichen ergeben plus, verschiedene minus.", "(−2) · (−2) = 4; 4 · (−2) = −8; (−8) · (−2) = 16. Gerader Exponent: Ergebnis positiv.",
    {1: [(8, "fb.vorzeichen.falsches_zeichen", "Vorzeichen vergessen")]}), VZ)
neu(TH, "negativ", "verfahren_waehlen", "mehrschritt", W(
    "Du sollst −3² berechnen (ohne Klammer um die −3). Welcher Weg ist richtig?",
    "Erst 3² = 9, das Minus steht davor: −9", [("(−3) · (−3) = 9", "das Minus als Teil der Basis gelesen"), ("−3 · 2 = −6", "Basis mal Exponent gerechnet"), ("−3 + 2 = −1", "Plus statt Hoch")],
    "Zu welcher Zahl gehört der Exponent 2?", "Der Exponent gehört nur zur 3. Erst 3² = 9, dann das Minus: −9. Mit Klammern wäre (−3)² = 9.",
    -3 ** 2 == -9 and (-3) ** 2 == 9), PO)
assert (-5) ** 3 == -125
neu(TH, "negativ", "umkehren", "umkehr", Z(
    "Eine negative Zahl hoch 3 ergibt −125. Wie heißt die Basis?",
    "-5", "-5", "Welche Zahl dreimal mit sich malgenommen gibt 125? Dann das Vorzeichen.", "(−5) · (−5) · (−5) = 25 · (−5) = −125. Bei ungeradem Exponent bleibt das Minus.",
    [(5, "fb.vorzeichen.falsches_zeichen", "Vorzeichen vergessen")]), VZ)

# ── sach ──
neu(TH, "sach", "fehler_detektiv", "fehler", FDZ(
    "Kim faltet ein Blatt Papier 5-mal. Er will wissen, wie viele Lagen es dann sind.",
    [("Nach dem 1. Falten sind es 2 Lagen.", 2 ** 1 == 2), ("Bei jedem weiteren Falten kommen 2 Lagen dazu.", 2 + 2 * 4 == 2 ** 5), ("Nach dem 5. Falten sind es 2 + 2 · 4 = 10 Lagen.", 2 + 2 * 4 == 10)],
    "Wie viele Lagen sind es nach dem 2. Falten? Nimm ein Blatt und falte.", "Beim Falten verdoppelt sich die Zahl der Lagen: 2, 4, 8, 16, 32. Nach 5-mal sind es 2⁵ = 32 Lagen."), PO)
neu(TH, "sach", "anwenden", "einkleidung", Z(
    "Eine Kettennachricht: In Runde 1 schickt eine Person sie an 3 Personen. In jeder weiteren Runde schickt jede neue Person sie an 3 weitere Personen. Wie viele Personen bekommen die Nachricht in Runde 4 neu?",
    "3**4", "3*3*3*3", "Runde 1: 3, Runde 2: 9. Jede Runde mal 3.", "Runde 1: 3, Runde 2: 9, Runde 3: 27, Runde 4: 81. Das ist 3⁴.",
    [(12, "fb.potenz.basis_mal_hochzahl", "3 · 4 gerechnet"), (64, None, "Basis und Exponent vertauscht")]), PO)
neu(TH, "sach", "bruecke", "darstellung", Z(
    "Die Tabelle zeigt, wie viele Lagen ein gefaltetes Papier nach dem Falten hat. Wie viele Lagen sind es nach dem 7. Falten?",
    "2**7", "2*2*2*2*2*2*2", "Wie wächst die untere Zeile von Spalte zu Spalte?", "Die Lagen verdoppeln sich jedes Mal: 2, 4, 8, 16, 32, 64, 128. Das ist 2⁷ = 128.",
    [(14, None, "2 · 7 gerechnet"), (64, None, "nur sechs Verdopplungen")],
    grafik=TAB(["Falten", "1", "2", "3", "4"], ["Lagen", "2", "4", "8", "16"])), PO)
