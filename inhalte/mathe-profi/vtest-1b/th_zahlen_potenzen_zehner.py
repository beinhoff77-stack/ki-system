T = "zahlen.potenzen_zehner"
LP = "M6 1 Rationale Zahlen (Zehnerpotenzen, wissenschaftliche Schreibweise, Vorsilben)"
REGEL[(T, "gross_wissenschaftlich")] = "rr.stellenwert"
REGEL[(T, "negativer_exponent")] = "rr.potenz"
REGEL[(T, "vorsilben_klein")] = "id.verhaeltnisse.groesse"
REGEL[(T, "vergleichen_pruefen")] = "id.zahlen.schreibweisen"
ABG[(T, "gross_wissenschaftlich")] = "Die Übungen schreiben eine große Zahl als a · 10ⁿ; hier wird die Bedingung 1 ≤ a < 10 begründet, ein Verschiebefehler gefunden und das Ergebnis einer Rechnung in die Form gebracht."
ABG[(T, "negativer_exponent")] = "Die Übungen schreiben 10⁻ⁿ als Dezimalzahl; hier werden Vorfaktor und Exponent zusammen betrachtet, Zehnerpotenzen verglichen und gedeutet."
ABG[(T, "vorsilben_klein")] = "Die Übungen wandeln eine Einheit um; hier werden Längen mit verschiedenen Vorsilben verglichen, geordnet und eine fehlerhafte Umrechnungskette berichtigt."
ABG[(T, "vergleichen_pruefen")] = "Die Übungen vergleichen zwei einfache Zehnerpotenzen; hier wird mit Vorfaktoren und Exponenten zugleich verglichen, ein Vergleichsfehler gefunden und ein Exponentenbereich bestimmt."
# ───────── gross_wissenschaftlich ─────────
neu(T, "gross_wissenschaftlich", "test", "fehler", L(
    "Ein Kind soll 23,1 · 10⁴ in wissenschaftliche Schreibweise bringen und rechnet: Zeile 1: Der Vorfaktor muss mindestens 1 und kleiner als 10 sein. Zeile 2: 23,1 = 2,31 · 10. Zeile 3: Also ist 23,1 · 10⁴ = 2,31 · 10⁴. In welcher Zeile steckt der erste Fehler? Welcher Exponent gehört richtig an die 10?",
    "Fehler in Zeile □, richtig: 23,1 · 10⁴ = 2,31 · 10^□", [3, 5], ["3", "4 + 1"], ["2 + 1", "5"],
    "Zeile 1 stimmt, Zeile 2 stimmt (2,31 · 10 = 23,1). In Zeile 3 wird die Zehn aus Zeile 2 vergessen: 23,1 · 10⁴ = 2,31 · 10 · 10⁴ = 2,31 · 10⁵. Der Exponent wird um 1 größer, wenn man das Komma um eine Stelle nach links schiebt.",
    {0: [(2, "Zeile 2 genannt, weil dort das Komma verschoben wird, obwohl diese Zeile stimmt", "2")], 1: [(4, "den Exponenten 4 unverändert übernommen", "4"), (3, "den Exponenten beim Verschieben des Kommas um 1 verkleinert", "4 - 1"), (14, "die 10 zum Exponenten addiert", "4 + 10")]}), form="fehler_detektiv", lp=LP, idee="bedingung_fehler")
neu(T, "gross_wissenschaftlich", "korrektur", "darstellung", W(
    "Welche Angabe beschreibt die Zahl 3,85 · 10⁷?",
    "38,5 Millionen",
    [("3,85 Millionen", "die Million mit 10⁶ gleichgesetzt, aber 10⁷ ist das Zehnfache davon: der Exponent wurde nicht beachtet"),
     ("385 Millionen", "das Komma beim Vorfaktor nach rechts verschoben, aber den Exponenten dabei nicht verkleinert"),
     ("3,85 Milliarden", "die Milliarde mit 10⁷ verwechselt; 10⁹ ist eine Milliarde")],
    "10⁷ sind zehn Millionen. 3,85 · 10⁷ = 3,85 · 10 Millionen = 38,5 Millionen = 38 500 000. Eine Million ist 10⁶, eine Milliarde 10⁹.",
    lambda: 3.85e7 == 38.5e6 and 3.85e7 != 3.85e6 and 3.85e7 != 385e6 and 3.85e7 != 3.85e9),
    form="bruecke", lp=LP, idee="zehnerpotenz_in_worten")
neu(T, "gross_wissenschaftlich", "korrektur", "umkehr", Z(
    "Eine Zahl wird in wissenschaftlicher Schreibweise als a · 10ⁿ geschrieben (a von 1 bis unter 10). Ausgeschrieben hat die Zahl 12 Ziffern. Wie groß ist n?",
    11, "12 - 1", "11",
    "Der Vorfaktor a hat eine Ziffer vor dem Komma. Der Exponent n gibt an, um wie viele Stellen das Komma nach rechts geschoben wird. Die ausgeschriebene Zahl hat also n + 1 Ziffern: n + 1 = 12, daher n = 11. Beispiel: 3,2 · 10² = 320 hat 3 Ziffern.",
    [B("12", "die Zahl der Ziffern als Exponenten genommen"),
     B("12 + 1", "eine Ziffer zu viel gezählt: Exponent um eins zu groß"),
     B("12 - 2", "zwei Ziffern abgezogen statt einer")]), form="umkehren", lp=LP, idee="ziffernzahl")
neu(T, "gross_wissenschaftlich", "korrektur", "mehrschritt", W(
    "Mia und Tom schreiben 24 000 000 in wissenschaftlicher Schreibweise. Mia schreibt 2,4 · 10⁷, Tom schreibt 24 · 10⁶. Wer hat die wissenschaftliche Schreibweise richtig angegeben?",
    "Nur Mia, denn der Vorfaktor muss kleiner als 10 sein.",
    [("Nur Tom, denn der Exponent muss die Anzahl der Nullen sein, also 6.", "den Exponenten als Anzahl der Nullen gedeutet; die Bedingung für den Vorfaktor wurde nicht geprüft"),
     ("Beide, denn beide Schreibweisen haben denselben Wert.", "nur den Wert verglichen; wissenschaftlich heißt auch, dass der Vorfaktor zwischen 1 und 10 liegt"),
     ("Keiner von beiden, denn der Exponent muss die Anzahl der Ziffern sein, also 8.", "den Exponenten als Anzahl der Ziffern gedeutet; er ist um eins kleiner")],
    "24 000 000 hat 8 Ziffern. Mias Schreibweise 2,4 · 10⁷ hat den Vorfaktor 2,4 (zwischen 1 und 10) und den Wert 24 000 000. Toms 24 · 10⁶ hat denselben Wert, aber der Vorfaktor 24 ist nicht kleiner als 10. Also ist nur Mias Schreibweise wissenschaftlich.",
    lambda: 2.4e7 == 24e6 == 24000000 and 1 <= 2.4 < 10 and not 1 <= 24 < 10), form="zwei_wege", lp=LP, idee="zwei_wege_pruefen")
neu(T, "gross_wissenschaftlich", "sicherung", "umkehr", Z(
    "Welche ganze Zahl muss man für n einsetzen, damit 5,3 · 10ⁿ = 530 000 gilt?",
    5, "6 - 1", "5",
    "5,3 · 10ⁿ = 530 000. 530 000 = 5,3 · 100 000 = 5,3 · 10⁵. Das Komma in 5,3 muss um 5 Stellen nach rechts. Probe: 5,3 · 100 000 = 530 000.",
    [B("6", "die Anzahl der Ziffern von 530 000 als Exponenten genommen"),
     B("3", "nur die Nullen am Ende abzüglich 1 gezählt"),
     B("4", "nur die Nullen am Ende der Zahl gezählt")]), lp=LP, idee="exponent_suchen")
neu(T, "gross_wissenschaftlich", "sicherung", "begruenden", W(
    "Warum ist 0,5 · 10⁸ keine wissenschaftliche Schreibweise der Zahl 50 000 000?",
    "Der Vorfaktor 0,5 ist kleiner als 1, wissenschaftlich wäre 5 · 10⁷.",
    [("Der Exponent 8 ist zu groß; man darf höchstens 10⁷ verwenden.", "eine Höchstgrenze für den Exponenten erfunden; Exponenten dürfen beliebig groß sein"),
     ("0,5 · 10⁸ ist eine andere Zahl als 50 000 000; richtig wäre 0,05 · 10⁸.", "den Wert falsch gerechnet: 0,5 · 10⁸ ist bereits 50 000 000, nur der Vorfaktor passt nicht"),
     ("Der Vorfaktor muss eine ganze Zahl sein; 0,5 ist keine ganze Zahl.", "verlangt, dass der Vorfaktor ganzzahlig ist; auch Dezimalzahlen zwischen 1 und 10 sind erlaubt")],
    "0,5 · 10⁸ = 50 000 000 ist richtig als Wert. Es fehlt nur die Bedingung 1 ≤ a < 10: 0,5 ist kleiner als 1. Man verschiebt das Komma um eine Stelle nach rechts und verkleinert den Exponenten: 5 · 10⁷ = 50 000 000.",
    lambda: 0.5 * 10 ** 8 == 5 * 10 ** 7 == 50000000 and not 1 <= 0.5 < 10 and 1 <= 5 < 10 and 1 <= 2.5 < 10), lp=LP, idee="bedingung_begruenden")
neu(T, "gross_wissenschaftlich", "sicherung", "transfer", Z(
    "Die Zahl 7,5 · 10⁷ wird mit 4 malgenommen. Das Ergebnis wird wieder in wissenschaftlicher Schreibweise a · 10ⁿ geschrieben (a von 1 bis unter 10). Wie groß ist n?",
    8, "7 + 1", "8",
    "7,5 · 4 = 30. Also ist das Ergebnis 30 · 10⁷. Der Vorfaktor 30 ist nicht kleiner als 10: 30 · 10⁷ = 3 · 10 · 10⁷ = 3 · 10⁸. Der Exponent wird um 1 größer, also n = 8.",
    [B("7", "den Exponenten unverändert gelassen, obwohl der Vorfaktor 30 nicht kleiner als 10 ist"),
     B("7 + 4", "den Faktor 4 zum Exponenten addiert"),
     B("7 * 4", "den Exponenten mit dem Faktor 4 malgenommen")]), lp=LP, idee="mal_rechnen_uebertrag")
# ───────── negativer_exponent ─────────
neu(T, "negativer_exponent", "test", "transfer", L(
    "Die Zahl 0,000 04 wird auf zwei Arten mit einer Zehnerpotenz geschrieben. Ergänze die Exponenten: 0,000 04 = 4 · 10^□ und 0,000 04 = 40 · 10^□.",
    "4 · 10^□ und 40 · 10^□", [-5, -6], ["0 - 5", "0 - 6"], ["-5", "0 - 5 - 1"],
    "Die 4 steht an der 5. Stelle hinter dem Komma, also ist 0,000 04 = 4 · 10⁻⁵. Wird der Vorfaktor zehnmal so groß (40 statt 4), muss die Zehnerpotenz zehnmal so klein werden, der Exponent also um 1 kleiner: 40 · 10⁻⁶. Probe: 40 · 0,000 001 = 0,000 04.",
    {0: [(5, "das Minus im Exponenten vergessen", "5"), (-4, "nur die Nullen hinter dem Komma gezählt", "0 - 4")],
     1: [(-4, "wie beim ersten Vorfaktor gezählt, obwohl der Vorfaktor jetzt größer ist", "0 - 4"), (-7, "den Exponenten beim größeren Vorfaktor um eins vergrößert statt verkleinert", "0 - 7")]}), lp=LP, idee="vorfaktor_und_exponent")
neu(T, "negativer_exponent", "korrektur", "umkehr", Z(
    "Eine Zehnerpotenz hat den Wert 0,000 000 1. Wie lautet ihr Exponent n?",
    -7, "0 - 7", "3 - 10",
    "0,000 000 1 = 1/10 000 000 = 1/10⁷ = 10⁻⁷. Die 1 steht an der siebten Stelle nach dem Komma, also ist n = −7.",
    [B("7", "das Minus im Exponenten vergessen"),
     B("0 - 6", "die Nullen hinter dem Komma (6) gezählt statt der Stelle der 1"),
     B("6", "die sechs Nullen gezählt und das Minus vergessen")]), form="umkehren", lp=LP, idee="stellen_zaehlen")
neu(T, "negativer_exponent", "korrektur", "darstellung", Z(
    "Wie viele der Zahlen 10⁻⁹, 10⁻⁴, 10⁻⁷ und 10⁻⁵ sind kleiner als 0,0001?",
    3, "1 + 1 + 1", "3",
    "0,0001 = 10⁻⁴. Eine Zehnerpotenz mit kleinerem Exponenten ist kleiner. Kleiner als 10⁻⁴ sind 10⁻⁹, 10⁻⁷ und 10⁻⁵ (drei Zahlen). 10⁻⁴ ist gleich 0,0001, nicht kleiner.",
    [B("1 + 1 + 1 + 1", "auch 10⁻⁴ mitgezählt, obwohl es gleich 0,0001 ist"),
     B("1", "nur die kleinste Zahl 10⁻⁹ gezählt"),
     B("1 + 1", "nur die zwei Zahlen mit dem größten Betrag des Exponenten gezählt")], einheit="Zahlen"), lp=LP, idee="vergleich_mit_grenze")
neu(T, "negativer_exponent", "korrektur", "darstellung", Z(
    "Wie viele Millionstel sind 10⁻¹?",
    100000, "10 ** 5", "100000",
    "Ein Millionstel ist 10⁻⁶. Es gilt 10⁻¹ = 1/10 = 100 000/1 000 000, also 100 000 Millionstel. Mit Potenzen: 10⁻¹ = 100 000 · 10⁻⁶, denn 10⁻⁶ · 10⁵ = 10⁻¹ (jeder Schritt im Exponenten um 1 nach rechts macht die Zahl zehnmal so groß).",
    [B("1", "den Exponenten 1 ohne Vorzeichen als Anzahl genommen"),
     B("10 ** 6", "die Million selbst als Anzahl genommen"),
     B("10 ** 4", "mit einem Schritt zu wenig zwischen den Exponenten gerechnet")], einheit="Millionstel"), form="bruecke", lp=LP, idee="millionstel")
neu(T, "negativer_exponent", "sicherung", "parameter", Z(
    "Die Zehnerpotenz 10⁻² wird durch 10 geteilt. Sie hat dann die Form 10ⁿ. Welche Zahl ist n?",
    -3, "0 - 3", "0 - 2 - 1",
    "10⁻² = 1/100. Zehnmal so klein ist 1/1000 = 10⁻³. Jedes Teilen durch 10 senkt den Exponenten um 1: aus −2 wird −3.",
    [B("0 - 1", "gedacht, dass Teilen durch 10 den Exponenten um 1 erhöht und dann −1 gerechnet"),
     B("0 - 2 * 10", "den Exponenten mit 10 malgenommen"),
     B("0 - 2", "den Exponenten unverändert gelassen")]), lp=LP, idee="durch_zehn_teilen")
neu(T, "negativer_exponent", "sicherung", "darstellung", W(
    "Welche Gleichung ist wahr?",
    "0,0004 = 4 · 10⁻⁴",
    [("0,0004 = 4 · 10⁻³", "den Exponenten um eins zu klein gezählt: die Stelle der 4 hinter dem Komma falsch bestimmt"),
     ("0,0004 = 4 · 10⁻⁵", "den Exponenten um eins zu groß gezählt: ein Nullen-Platz zu viel"),
     ("0,0004 = 0,4 · 10⁻⁴", "den Vorfaktor verkleinert, ohne den Exponenten anzupassen")],
    "Die 4 steht an der 4. Stelle hinter dem Komma: 0,0004 = 4 · 10⁻⁴. Mit dem Vorfaktor 0,4 müsste der Exponent −3 sein (0,4 · 10⁻³ = 0,0004); 0,4 · 10⁻⁴ ist nur 0,00004.",
    lambda: abs(4e-4 - 0.0004) < 1e-15 and abs(4e-3 - 0.0004) > 1e-9 and abs(4e-5 - 0.0004) > 1e-9 and abs(0.4e-4 - 0.0004) > 1e-9), lp=LP, idee="gleichung_wahr")
neu(T, "negativer_exponent", "sicherung", "begruenden", W(
    "Ein Datenblatt nennt den Wert 10⁻³. Welche Deutung dieser Zehnerpotenz stimmt?",
    "Ein Tausendstel, geschrieben als 0,001.",
    [("Ein Zehntausendstel, geschrieben als 0,0001.", "eine Stelle zu viel gezählt: der Exponent 3 bedeutet drei Stellen, die 1 steht an der dritten Stelle"),
     ("Minus Tausend, geschrieben als −1000.", "das Minus im Exponenten als Vorzeichen der Zahl gedeutet"),
     ("Dreimal ein Zehntel, geschrieben als 0,3.", "den Exponenten als Anzahl der Zehntel genommen statt als Anzahl der Faktoren")],
    "10⁻³ = 1/10³ = 1/1000 = 0,001. Das ist ein Tausendstel: Die 1 steht an der dritten Stelle hinter dem Komma. Das Minus im Exponenten macht die Zahl nicht negativ, sondern klein.",
    lambda: F(10) ** -3 == F(1, 1000) == F("0.001") != F("0.0001") and F(10) ** -3 > 0), lp=LP, idee="deutung")
# ───────── vorsilben_klein ─────────
neu(T, "vorsilben_klein", "test", "transfer", Z(
    "Wie viele der Längen 3 000 nm, 0,004 mm, 5 µm, 0,0025 mm und 0,000 002 m sind kürzer als 4 µm? (1 nm = 10⁻⁹ m, 1 µm = 10⁻⁶ m, 1 mm = 10⁻³ m)",
    3, "1 + 1 + 1", sum(1 for x in (F(3000) * F(10) ** -9, F("0.004") * F(10) ** -3, 5 * F(10) ** -6, F("0.0025") * F(10) ** -3, F("0.000002")) if x < 4 * F(10) ** -6),
    "Alle Längen in µm: 3 000 nm = 3 µm (kürzer). 0,004 mm = 4 µm (gleich lang, nicht kürzer). 5 µm (länger). 0,0025 mm = 2,5 µm (kürzer). 0,000 002 m = 2 µm (kürzer). Kürzer als 4 µm sind also 3 Längen.",
    [B("1 + 1 + 1 + 1", "die gleich lange Länge 0,004 mm mitgezählt"),
     B("1 + 1", "nur zwei der drei kürzeren Längen erkannt, weil die Maßzahlen verschiedener Einheiten verglichen wurden"),
     B("1 + 1 + 1 + 1 + 1", "alle Längen mitgezählt, weil die Zahlen vor den Einheiten alle klein sind")], einheit="Längen"), lp=LP, idee="einheiten_vergleichen")
neu(T, "vorsilben_klein", "korrektur", "darstellung", W(
    "Welche Gleichung ist richtig?",
    "1 µm = 10⁻⁶ m",
    [("1 µm = 10⁻³ m", "Mikro und Milli verwechselt: 10⁻³ m ist ein Millimeter"),
     ("1 nm = 10⁻⁶ m", "Nano und Mikro verwechselt: 10⁻⁶ m ist ein Mikrometer"),
     ("1 mm = 10⁻⁶ m", "Milli und Mikro verwechselt: ein Millimeter ist tausendmal so groß wie ein Mikrometer")],
    "Milli (m) bedeutet 10⁻³, Mikro (µ) bedeutet 10⁻⁶, Nano (n) bedeutet 10⁻⁹. Also gilt 1 mm = 10⁻³ m, 1 µm = 10⁻⁶ m und 1 nm = 10⁻⁹ m. Nur die erste Gleichung stimmt.",
    lambda: F(10) ** -6 != F(10) ** -3 and F(10) ** -6 != F(10) ** -9), form="bruecke", lp=LP, idee="beziehung_potenz")
neu(T, "vorsilben_klein", "korrektur", "einkleidung", Z(
    "Ein Haar ist 80 µm dick. Wie viele solche Haare liegen nebeneinander auf einer Strecke von 1 cm? (1 cm = 10 000 µm)",
    125, "10000 / 80", "1000000 / 8000",
    "1 cm sind 10 000 µm. Jedes Haar braucht 80 µm. Es passen 10 000 : 80 = 125 Haare nebeneinander. Probe: 125 · 80 µm = 10 000 µm = 1 cm.",
    [B("1000 / 80", "1 cm als 1000 µm gerechnet statt 10 000 µm"),
     B("10000 * 80", "malgenommen statt geteilt"),
     B("80 / 10000", "die Maßzahlen in der falschen Reihenfolge geteilt")], einheit="Haare"), form="bruecke", lp=LP, idee="stueckzahl")
neu(T, "vorsilben_klein", "korrektur", "darstellung", L(
    "Ergänze: 3 000 nm = □ µm und 0,25 mm = □ µm.",
    "3 000 nm = □ µm; 0,25 mm = □ µm", [3, 250], ["3000 / 1000", "0.25 * 1000"], ["3", "250"],
    "1 µm = 1000 nm, also 3 000 nm = 3 µm. 1 mm = 1000 µm, also 0,25 mm = 0,25 · 1000 µm = 250 µm.",
    {0: [(3000, "die Zahl 3 000 unverändert übernommen", "3000"), (3000000, "mit 1000 malgenommen statt geteilt", "3000 * 1000")], 1: [(25, "das Komma um eine Stelle zu wenig verschoben", "0.25 * 100"), (2500, "um eine Zehnerpotenz zu viel verschoben", "0.25 * 10000")]}), form="bruecke", lp=LP, idee="maszahl_umrechnen")
neu(T, "vorsilben_klein", "sicherung", "fehler", L(
    "Ein Kind rechnet: Zeile 1: 1 nm = 10⁻⁹ m. Zeile 2: 1 µm = 10⁻⁶ m. Zeile 3: Also ist 10⁻⁶ : 10⁻⁹ = 10⁻³. Zeile 4: Also sind 1 µm gleich 10⁻³ nm. In welcher Zeile steckt der erste Fehler? Wie viele Nanometer sind 1 µm richtig?",
    "Fehler in Zeile □, richtig: 1 µm = □ nm", [3, 1000], ["3", "10 ** 3"], ["2 + 1", "1000"],
    "Zeile 1 und Zeile 2 sind richtig. In Zeile 3 ist die Rechnung falsch: 10⁻⁶ : 10⁻⁹ = 10⁻⁶ · 10⁹ = 10³, nicht 10⁻³. Also sind 1 µm gleich 10³ nm = 1000 nm. Zeile 4 folgt aus dem Fehler in Zeile 3.",
    {0: [(4, "die Schlusszeile genannt, weil dort der falsche Wert 10⁻³ steht", "4")], 1: [(-3, "das falsche Ergebnis 10⁻³ als Zahl −3 genommen", "0 - 3"), (1, "die Vorsilben als Faktor 1 gelesen", "1"), (1000000, "mit 10⁶ gerechnet statt 10³", "10 ** 6")]}), form="fehler_detektiv", lp=LP, idee="fehler_kette")
neu(T, "vorsilben_klein", "sicherung", "darstellung", W(
    "Welche Zeile ordnet die Längen 0,001 mm, 5 µm, 800 nm und 0,002 mm von kurz nach lang?",
    "800 nm, 0,001 mm, 0,002 mm, 5 µm",
    [("0,001 mm, 0,002 mm, 5 µm, 800 nm", "nur auf die Zahlen vor der Einheit geachtet: 0,001 kleiner als 0,002 kleiner als 5 kleiner als 800"),
     ("800 nm, 5 µm, 0,001 mm, 0,002 mm", "nach der Reihenfolge der Einheiten geordnet (nm vor µm vor mm), ohne die Maßzahlen umzurechnen"),
     ("5 µm, 0,002 mm, 0,001 mm, 800 nm", "die Reihenfolge von lang nach kurz statt von kurz nach lang angegeben")],
    "Alle Längen in µm: 800 nm = 0,8 µm; 0,001 mm = 1 µm; 0,002 mm = 2 µm; 5 µm. Von kurz nach lang: 0,8 µm, 1 µm, 2 µm, 5 µm, also 800 nm, 0,001 mm, 0,002 mm, 5 µm.",
    lambda: F(800) * F(10) ** -9 < F("0.001") * F(10) ** -3 < F("0.002") * F(10) ** -3 < 5 * F(10) ** -6), lp=LP, idee="ordnen_gemischt")
neu(T, "vorsilben_klein", "sicherung", "begruenden", W(
    "Ein Kind sagt: „Ein Mikrometer ist tausendmal kleiner als ein Millimeter, also muss die Maßzahl in Mikrometern tausendmal kleiner sein als in Millimetern.“ Welche Aussage stimmt?",
    "Das stimmt nicht: Die Maßzahl in Mikrometern ist tausendmal größer, denn man braucht tausendmal so viele der kleineren Einheiten.",
    [("Das stimmt: Die Maßzahl in Mikrometern ist tausendmal kleiner, denn kleinere Einheiten haben kleinere Maßzahlen.", "Größe der Einheit und Maßzahl gleichgesetzt; mit einer kleineren Einheit braucht man mehr davon"),
     ("Das stimmt nicht: Die Maßzahl bleibt gleich, denn die Länge ändert sich beim Umrechnen nicht.", "Länge und Maßzahl verwechselt; die Länge bleibt gleich, die Maßzahl ändert sich"),
     ("Das stimmt nicht: Die Maßzahl in Mikrometern ist hundertmal größer, denn ein Mikrometer ist hundertmal kleiner als ein Millimeter.", "den Faktor zwischen Milli und Mikro falsch angegeben; es ist ein Faktor tausend")],
    "1 mm = 1000 µm. Dieselbe Länge wird in der kleineren Einheit durch eine größere Maßzahl angegeben: 2 mm sind 2000 µm. Die Maßzahl wird tausendmal größer, nicht kleiner. Die Länge selbst bleibt gleich.",
    lambda: 2 * 1000 == 2000 and F(10) ** -3 / F(10) ** -6 == 1000), lp=LP, idee="maszahl_gegenlaeufig")
# ───────── vergleichen_pruefen ─────────
neu(T, "vergleichen_pruefen", "test", "parameter", Z(
    "Für wie viele ganze Zahlen n von −5 bis 2 (einschließlich) ist der Wert von 5 · 10ⁿ größer als 0,003 und kleiner als 40?",
    4, "1 + 1 + 1 + 1", sum(1 for n in range(-5, 3) if F(3, 1000) < 5 * F(10) ** n < 40),
    "Die Werte 5 · 10ⁿ sind für n = −5 bis 2: 0,000 05; 0,0005; 0,005; 0,05; 0,5; 5; 50; 500. Größer als 0,003 und kleiner als 40 sind 0,005; 0,05; 0,5 und 5, also die Exponenten −3, −2, −1 und 0: 4 Zahlen. 0,0005 liegt unter 0,003, und 50 liegt über 40.",
    [B("1 + 1 + 1", "den Wert 0,005 vergessen, der knapp über der unteren Grenze liegt"),
     B("1 + 1 + 1 + 1 + 1", "auch den Wert 50 mitgezählt, der über der oberen Grenze liegt"),
     B("1 + 1 + 1 + 1 + 1 + 1 + 1 + 1", "alle Exponenten gezählt, ohne die Werte mit den Grenzen zu vergleichen")], einheit="Zahlen"), lp=LP, idee="bereich_exponent")
neu(T, "vergleichen_pruefen", "korrektur", "darstellung", Z(
    "Wie viele der Zahlen 5 · 10⁵, 50 · 10⁴, 0,5 · 10⁶ und 5 000 000 · 10⁻² sind gleich 500 000?",
    3, "1 + 1 + 1", "3",
    "5 · 10⁵ = 500 000. 50 · 10⁴ = 500 000. 0,5 · 10⁶ = 500 000. Aber 5 000 000 · 10⁻² = 50 000, denn 10⁻² teilt durch 100. Es sind 3 Zahlen gleich 500 000.",
    [B("1 + 1 + 1 + 1", "auch die vierte Zahl mitgezählt, ohne durch 100 zu teilen"),
     B("1", "nur die wissenschaftliche Schreibweise gezählt"),
     B("1 + 1", "die Zahl mit dem Vorfaktor kleiner als 1 und die mit dem großen Vorfaktor nicht mitgezählt")], einheit="Zahlen"), lp=LP, idee="gleiche_zahl")
neu(T, "vergleichen_pruefen", "korrektur", "darstellung", W(
    "Welche der folgenden Zahlen liegt zwischen 3 · 10⁻³ und 4 · 10⁻³?",
    "35 · 10⁻⁴",
    [("3,5 · 10⁻⁴", "den Vorfaktor 3,5 zwischen 3 und 4 gesehen, aber der Exponent −4 macht die Zahl zehnmal kleiner als 10⁻³"),
     ("3,5 · 10⁻²", "den Vorfaktor 3,5 zwischen 3 und 4 gesehen, aber der Exponent −2 macht die Zahl zehnmal größer als 10⁻³"),
     ("0,35 · 10⁻³", "den Exponenten −3 übernommen, aber der Vorfaktor 0,35 liegt nicht zwischen 3 und 4")],
    "3 · 10⁻³ = 0,003 und 4 · 10⁻³ = 0,004. 35 · 10⁻⁴ = 0,0035 liegt dazwischen. 3,5 · 10⁻⁴ = 0,00035 ist zu klein, 3,5 · 10⁻² = 0,035 ist zu groß, 0,35 · 10⁻³ = 0,00035 ist zu klein.",
    lambda: F(3, 1000) < 35 * F(10) ** -4 < F(4, 1000) and not (F(3, 1000) < F("3.5") * F(10) ** -4 < F(4, 1000)) and not (F(3, 1000) < F("3.5") * F(10) ** -2 < F(4, 1000)) and not (F(3, 1000) < F("0.35") * F(10) ** -3 < F(4, 1000))), lp=LP, idee="zwischen_darstellung")
neu(T, "vergleichen_pruefen", "korrektur", "umkehr", Z(
    "Welches ist die kleinste ganze Zahl n, für die 4 · 10ⁿ größer als 0,005 ist?",
    -2, "0 - 2", "2 - 4",
    "0,005 = 5 · 10⁻³. Für n = −2 ist 4 · 10⁻² = 0,04 > 0,005. Für n = −3 ist 4 · 10⁻³ = 0,004 und das ist kleiner als 0,005. Also ist n = −2 die kleinste Zahl.",
    [B("0 - 3", "die Zahl mit dem Exponenten −3 schon für größer als 0,005 gehalten, ohne die Vorfaktoren zu vergleichen"),
     B("2", "das Minus im Exponenten vergessen"),
     B("0 - 1", "die Zahl n = −1 gewählt, aber −2 ist noch kleiner und erfüllt die Bedingung auch")]), form="umkehren", lp=LP, idee="kleinstes_n")
neu(T, "vergleichen_pruefen", "sicherung", "fehler", L(
    "Ein Kind vergleicht 5 · 10⁻⁵ und 2 · 10⁻⁴ und rechnet: Zeile 1: Ich vergleiche die beiden Zahlen. Zeile 2: Die Exponenten spielen für den Vergleich keine Rolle, es zählt nur 5 > 2. Zeile 3: Also ist 5 · 10⁻⁵ größer als 2 · 10⁻⁴. In welcher Zeile steckt der erste Fehler? Wie oft passt die kleinere Zahl in die größere?",
    "Fehler in Zeile □, die größere Zahl ist □-mal so groß wie die kleinere", [2, 4], ["2", "20 / 5"], ["3 - 1", "4"],
    "Zeile 1 sagt nur, was getan wird. In Zeile 2 steckt der Fehler: Der Exponent gehört zur Zahl und entscheidet mit; 10⁻⁵ ist zehnmal kleiner als 10⁻⁴. Es gilt 2 · 10⁻⁴ = 20 · 10⁻⁵, und 20 · 10⁻⁵ ist 4-mal so groß wie 5 · 10⁻⁵. Zeile 3 folgt aus dem Fehler in Zeile 2. Richtig ist: 2 · 10⁻⁴ ist größer.",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3")], 1: [(20, "den Vorfaktor 20 aus der Umschreibung als Vergleichszahl genommen", "20"), (5, "den kleineren Vorfaktor 5 als Zahl der Passungen genommen", "5")]}), form="fehler_detektiv", lp=LP, idee="fehler_vorfaktor")
neu(T, "vergleichen_pruefen", "sicherung", "umkehr", Z(
    "Eine Zahl wird mit 10⁻⁴ malgenommen und ergibt 0,006. Welche Zahl war es?",
    60, "0.006 * 10000", "6 * 10000 / 1000",
    "Malnehmen mit 10⁻⁴ heißt durch 10 000 teilen. Rückwärts muss man mit 10 000 malnehmen: 0,006 · 10 000 = 60. Probe: 60 · 10⁻⁴ = 60 : 10 000 = 0,006.",
    [B("0.006 * 100", "mit 100 statt mit 10 000 malgenommen"),
     B("0.006 / 10000", "noch einmal durch 10 000 geteilt statt zurückgerechnet"),
     B("6 * 100", "die Ziffer 6 mit 100 malgenommen")]), lp=LP, idee="faktor_rueckwaerts")
neu(T, "vergleichen_pruefen", "sicherung", "begruenden", W(
    "Welche der Zahlen 7 · 10⁻⁶ und 3 · 10⁻⁵ ist größer, und warum?",
    "3 · 10⁻⁵ ist größer, denn 7 · 10⁻⁶ = 0,7 · 10⁻⁵ und 0,7 ist kleiner als 3.",
    [("7 · 10⁻⁶ ist größer, denn 7 ist größer als 3.", "nur die Vorfaktoren verglichen und die Exponenten nicht beachtet"),
     ("7 · 10⁻⁶ ist größer, denn bei negativen Exponenten ist die Zahl mit der größeren Hochzahl auch die größere Zahl.", "den Betrag des negativen Exponenten für die Größe gehalten; 10⁻⁶ ist kleiner als 10⁻⁵"),
     ("Beide sind gleich groß, denn beide haben hinter dem Komma nur eine von null verschiedene Ziffer.", "nur die Anzahl der von null verschiedenen Ziffern verglichen")],
    "Man bringt beide auf denselben Exponenten: 7 · 10⁻⁶ = 0,7 · 10⁻⁵. Jetzt vergleicht man die Vorfaktoren: 0,7 ist kleiner als 3. Also ist 3 · 10⁻⁵ größer. Ausgeschrieben: 0,000 03 gegen 0,000 007.",
    lambda: F(3) * F(10) ** -5 > 7 * F(10) ** -6 and 7 * F(10) ** -6 == F("0.7") * F(10) ** -5), lp=LP, idee="begruenden_vergleich")
