T = "zahlen.potenzen_zehner"
LP = "M6 1 Rationale Zahlen (Zehnerpotenzen, wissenschaftliche Schreibweise, Vorsilben)"
ABG[(T, "gross_wissenschaftlich")] = "Die Übungen schreiben eine große Zahl als a · 10ⁿ; hier wird die Bedingung 1 ≤ a < 10 begründet, ein Verschiebefehler gefunden und mit Größenordnungen gerechnet."
ABG[(T, "negativer_exponent")] = "Die Übungen schreiben 10⁻ⁿ als Dezimalzahl; hier werden Stellen (nicht Nullen) gezählt, Zehnerpotenzen verglichen und der Exponent aus der Dezimalzahl umgekehrt bestimmt."
ABG[(T, "vorsilben_klein")] = "Die Übungen wandeln eine Einheit um; hier werden die Vorsilben begründet, Längen verschiedener Vorsilben geordnet und eine fehlerhafte Umrechnungskette berichtigt."
ABG[(T, "vergleichen_pruefen")] = "Die Übungen vergleichen zwei einfache Zehnerpotenzen; hier wird mit Vorfaktoren und Exponenten zugleich verglichen und begründet, welche Darstellungen dieselbe Zahl sind."
IDEEN[(T, "gross_wissenschaftlich")] = ['fehler_finden_richtigstellen', 'umkehr', 'darstellung_wechseln', 'groessenvergleich', 'groessenordnung_abschaetzen', 'begruenden_ablenker', 'umkehr']
IDEEN[(T, "negativer_exponent")] = ['begruenden_ablenker', 'umkehr', 'darstellung_wechseln', 'groessenvergleich', 'modell_aufstellen', 'was_waere_wenn', 'darstellung_wechseln']
IDEEN[(T, "vorsilben_klein")] = ['begruenden_ablenker', 'darstellung_wechseln', 'darstellung_wechseln', 'umkehr', 'modell_aufstellen', 'fehler_finden_richtigstellen', 'groessenvergleich']
IDEEN[(T, "vergleichen_pruefen")] = ['begruenden_ablenker', 'groessenvergleich', 'umkehr', 'darstellung_wechseln', 'modell_aufstellen', 'fehler_finden_richtigstellen', 'groessenvergleich']
# ───────── gross_wissenschaftlich ─────────
neu(T, "gross_wissenschaftlich", "test", "fehler", L(
    "Ein Kind soll 23,1 · 10⁴ in wissenschaftliche Schreibweise bringen und rechnet: Zeile 1: Der Vorfaktor muss mindestens 1 und kleiner als 10 sein. Zeile 2: 23,1 = 2,31 · 10. Zeile 3: Also ist 23,1 · 10⁴ = 2,31 · 10⁴. In welcher Zeile steckt der erste Fehler? Welcher Exponent gehört richtig an die 10?",
    "Fehler in Zeile □, richtig: 23,1 · 10⁴ = 2,31 · 10^□", [3, 5], ["3", "4 + 1"], ["2 + 1", "5"],
    "Zeile 1 stimmt, Zeile 2 stimmt (2,31 · 10 = 23,1). In Zeile 3 wird die Zehn aus Zeile 2 vergessen: 23,1 · 10⁴ = 2,31 · 10 · 10⁴ = 2,31 · 10⁵. Der Exponent wird um 1 größer, wenn man das Komma um eine Stelle nach links schiebt.",
    {0: [(2, "Zeile 2 genannt, weil dort das Komma verschoben wird, obwohl diese Zeile stimmt", "2")], 1: [(4, "den Exponenten 4 unverändert übernommen", "4"), (3, "den Exponenten beim Verschieben des Kommas um 1 verkleinert", "4 - 1"), (14, "die 10 zum Exponenten addiert", "4 + 10")]}), form="fehler_detektiv", lp=LP)
neu(T, "gross_wissenschaftlich", "korrektur", "umkehr", L(
    "Eine Zahl hat in wissenschaftlicher Schreibweise den Vorfaktor 6,2 und ausgeschrieben lautet sie 62 000 000. Ergänze: Der Exponent der 10 ist □. Die ausgeschriebene Zahl hat □ Ziffern.",
    "Exponent n = □, Ziffern: □", [7, 8], ["8 - 1", "7 + 1"], ["7", "2 + 6"],
    "62 000 000 hat 8 Ziffern. Der Vorfaktor 6,2 hat die erste Ziffer 6 vor dem Komma, danach folgen 7 Stellen: 62 000 000 = 6,2 · 10⁷. Probe: 6,2 · 10 000 000 = 62 000 000.",
    {0: [(8, "die Anzahl der Ziffern als Exponenten genommen", "8"), (6, "nur die Nullen am Ende gezählt", "6")], 1: [(7, "den Exponenten als Anzahl der Ziffern genommen", "7"), (6, "die Nullen als Ziffern gezählt", "6")]}), form="umkehren", lp=LP)
neu(T, "gross_wissenschaftlich", "korrektur", "darstellung", W(
    "Welche der folgenden Schreibweisen ist die wissenschaftliche Schreibweise der Zahl 38 500 000?",
    "3,85 · 10⁷",
    [("38,5 · 10⁶", "den Vorfaktor nicht kleiner als 10 gemacht: 38,5 ist zu groß"),
     ("385 · 10⁵", "nur eine Potenz von 10 abgespalten; der Vorfaktor 385 ist viel zu groß"),
     ("0,385 · 10⁸", "den Vorfaktor kleiner als 1 gewählt; 0,385 ist zu klein")],
    "Der Vorfaktor muss mindestens 1 und kleiner als 10 sein. 38 500 000 = 3,85 · 10 000 000 = 3,85 · 10⁷. Die anderen Schreibweisen haben denselben Wert, aber der Vorfaktor 38,5 (zu groß), 385 (zu groß) oder 0,385 (zu klein) passt nicht.",
    lambda: all(abs(x - 38500000) < 1e-6 for x in (3.85e7, 38.5e6, 385e5, 0.385e8)) and 1 <= 3.85 < 10 and not 1 <= 38.5 < 10 and not 1 <= 385 < 10 and not 1 <= 0.385 < 10), form="bruecke", lp=LP)
neu(T, "gross_wissenschaftlich", "sicherung", "transfer", Z(
    "Licht legt in einer Sekunde etwa 3 · 10⁵ km zurück. Ein Jahr hat rund 3,2 · 10⁷ Sekunden. Die Strecke, die Licht in einem Jahr zurücklegt, ist eine ganze Zahl von Kilometern. Wie viele Ziffern hat diese Zahl, wenn man sie ausschreibt?",
    13, "12 + 1", "13",
    "3 · 10⁵ · 3,2 · 10⁷ = 9,6 · 10¹². Das sind 9 600 000 000 000 km. Bei wissenschaftlicher Schreibweise a · 10ⁿ hat die Zahl n + 1 = 13 Ziffern.",
    [B("12", "den Exponenten 12 der wissenschaftlichen Schreibweise als Anzahl der Ziffern genommen"),
     B("5 * 7", "die Exponenten 5 und 7 malgenommen und das Ergebnis als Ziffernzahl genommen"),
     B("14", "eine Ziffer zu viel gezählt")], einheit="Ziffern"), form="anwenden", lp=LP)
neu(T, "gross_wissenschaftlich", "sicherung", "begruenden", W(
    "Warum ist 0,5 · 10⁸ keine wissenschaftliche Schreibweise der Zahl 50 000 000?",
    "Der Vorfaktor 0,5 ist kleiner als 1, wissenschaftlich wäre 5 · 10⁷.",
    [("Der Exponent 8 ist zu groß; man darf höchstens 10⁷ verwenden.", "eine Höchstgrenze für den Exponenten erfunden; Exponenten dürfen beliebig groß sein"),
     ("0,5 · 10⁸ ist eine andere Zahl als 50 000 000; richtig wäre 0,05 · 10⁸.", "den Wert falsch gerechnet: 0,5 · 10⁸ ist bereits 50 000 000, nur der Vorfaktor passt nicht"),
     ("Der Vorfaktor muss eine ganze Zahl sein; 0,5 ist keine ganze Zahl.", "verlangt, dass der Vorfaktor ganzzahlig ist; auch Dezimalzahlen zwischen 1 und 10 sind erlaubt")],
    "0,5 · 10⁸ = 50 000 000 ist richtig als Wert. Es fehlt nur die Bedingung 1 ≤ a < 10: 0,5 ist kleiner als 1. Man verschiebt das Komma um eine Stelle nach rechts und verkleinert den Exponenten: 5 · 10⁷ = 50 000 000.",
    lambda: 0.5 * 10 ** 8 == 5 * 10 ** 7 == 50000000 and not 1 <= 0.5 < 10 and 1 <= 5 < 10 and 1 <= 2.5 < 10), lp=LP)
neu(T, "gross_wissenschaftlich", "sicherung", "umkehr", Z(
    "Welche ganze Zahl muss man für n einsetzen, damit 5,3 · 10ⁿ = 530 000 gilt?",
    5, "6 - 1", "5",
    "5,3 · 10ⁿ = 530 000. 530 000 = 5,3 · 100 000 = 5,3 · 10⁵. Das Komma in 5,3 muss um 5 Stellen nach rechts. Probe: 5,3 · 100 000 = 530 000.",
    [B("6", "die Anzahl der Ziffern von 530 000 als Exponenten genommen"),
     B("4", "nur die Nullen am Ende abzüglich 1 gezählt"),
     B("3", "nur die Nullen am Ende der Zahl gezählt")]), lp=LP)
neu(T, "gross_wissenschaftlich", "korrektur", "darstellung", Z(
    "Eine Zahl wird als 7,4 · 10⁸ angegeben. Aus wie vielen Ziffern besteht die ausgeschriebene Zahl?",
    9, "8 + 1", "9",
    "7,4 · 10⁸ = 740 000 000. Vor dem Komma steht eine Ziffer, der Exponent 8 schiebt das Komma um 8 Stellen nach rechts: Es sind 1 + 8 = 9 Ziffern.",
    [B("8", "den Exponenten als Anzahl der Ziffern genommen"),
     B("8 + 2", "die beiden Ziffern des Vorfaktors zusätzlich zum Exponenten gezählt"),
     B("8 - 1", "eine Ziffer zu wenig gezählt")], einheit="Ziffern"), lp=LP)
# ───────── negativer_exponent ─────────
neu(T, "negativer_exponent", "test", "begruenden", W(
    "Ein Datenblatt nennt den Wert 10⁻³. Welche Deutung dieser Zehnerpotenz stimmt?",
    "10⁻³ = 0,001: Die 1 steht an der dritten Stelle nach dem Komma.",
    [("10⁻³ = −1000, denn das Minus im Exponenten macht die Zahl negativ.", "das Minus im Exponenten auf den Wert übertragen"),
     ("10⁻³ = 0,0001, denn hinter dem Komma stehen drei Nullen.", "die Nullen statt der Stelle der 1 gezählt; es sind zwei Nullen vor der 1"),
     ("10⁻³ = 0,03, denn man teilt 10 durch die Hochzahl 3 mal 10.", "10 mit dem Exponenten 3 zu 0,03 verrechnet statt dreimal durch 10 zu teilen")],
    "10⁻³ = 1/10³ = 1/1000 = 0,001. Die 1 steht an der dritten Stelle nach dem Komma, vor ihr stehen zwei Nullen. Das Minus im Exponenten macht die Zahl nicht negativ, sondern klein.",
    lambda: F(10) ** -3 == F(1, 1000) == F("0.001") and F(10) ** -3 > 0 and F("0.0001") != F(10) ** -3 and F("0.03") != F(10) ** -3), lp=LP)
neu(T, "negativer_exponent", "korrektur", "umkehr", Z(
    "Eine Zehnerpotenz hat den Wert 0,000 000 1. Wie lautet ihr Exponent n?",
    -7, "0 - 7", "3 - 10",
    "0,000 000 1 = 1/10 000 000 = 1/10⁷ = 10⁻⁷. Die 1 steht an der siebten Stelle nach dem Komma, also ist n = −7.",
    [B("7", "das Minus im Exponenten vergessen"),
     B("0 - 6", "die Nullen hinter dem Komma (6) gezählt statt der Stelle der 1"),
     B("6", "die sechs Nullen gezählt und das Minus vergessen")]), form="umkehren", lp=LP)
neu(T, "negativer_exponent", "korrektur", "darstellung", L(
    "Ergänze für 10⁻⁵: 10⁻⁵ = 1/□ und als Dezimalzahl stehen □ Nullen direkt hinter dem Komma (vor der 1).",
    "10⁻⁵ = 1/□; Nullen nach dem Komma: □", [100000, 4], ["10 ** 5", "5 - 1"], ["10 * 10 * 10 * 10 * 10", "4"],
    "10⁻⁵ = 1/10⁵ = 1/100 000 = 0,000 01. Die 1 steht an der fünften Stelle nach dem Komma, davor stehen 4 Nullen.",
    {0: [(10000, "nur vier Zehnerfaktoren genommen", "10 ** 4"), (50, "10 mal 5 gerechnet", "10 * 5")], 1: [(5, "die Stelle der 1 als Anzahl der Nullen genommen", "5"), (6, "eine Null zu viel gezählt", "5 + 1")]}), form="bruecke", lp=LP)
neu(T, "negativer_exponent", "korrektur", "darstellung", Z(
    "Wie viele der Zahlen 10⁻⁹, 10⁻⁴, 10⁻⁷ und 10⁻⁵ sind kleiner als 0,0001?",
    3, "1 + 1 + 1", "3",
    "0,0001 = 10⁻⁴. Eine Zehnerpotenz mit kleinerem Exponenten ist kleiner. Kleiner als 10⁻⁴ sind 10⁻⁹, 10⁻⁷ und 10⁻⁵ (drei Zahlen). 10⁻⁴ ist gleich 0,0001, nicht kleiner.",
    [B("1 + 1 + 1 + 1", "auch 10⁻⁴ mitgezählt, obwohl es gleich 0,0001 ist"),
     B("1", "nur die kleinste Zahl 10⁻⁹ gezählt"),
     B("1 + 1", "nur die zwei Zahlen mit dem größten Betrag des Exponenten gezählt")], einheit="Zahlen"), lp=LP)
neu(T, "negativer_exponent", "sicherung", "transfer", Z(
    "Ein Virus ist etwa 10⁻⁹ m lang. Eine Bakterie ist 10⁻⁶ m lang. Wie viele Viren passen der Länge nach nebeneinander auf die Länge einer Bakterie?",
    1000, "10 ** 3", "10 ** 9 / 10 ** 6",
    "Gesucht ist der Quotient der Längen: 10⁻⁶ : 10⁻⁹ = 10³ = 1000. Probe: 1000 Viren zu je 10⁻⁹ m sind 1000 · 10⁻⁹ m = 10⁻⁶ m.",
    [B("1000000000000000", "die Beträge der Exponenten addiert statt subtrahiert"),
     B("9 - 6", "die Exponenten subtrahiert und das Ergebnis 3 nicht als Zehnerpotenz gelesen"),
     B("1000000000", "den Exponenten der Virenlänge als Anzahl genommen")], einheit="Viren"), form="anwenden", lp=LP)
neu(T, "negativer_exponent", "sicherung", "parameter", Z(
    "Die Zehnerpotenz 10⁻² wird zehnmal so klein gemacht. Sie hat dann die Form 10ⁿ. Welche Zahl ist n?",
    -3, "0 - 3", "0 - 2 - 1",
    "10⁻² = 1/100. Zehnmal so klein ist 1/1000 = 10⁻³. Jedes Teilen durch 10 senkt den Exponenten um 1: aus −2 wird −3.",
    [B("0 - 1", "gedacht, dass Teilen durch 10 den Exponenten um 1 erhöht und dann −1 gerechnet"),
     B("0 - 2 * 10", "den Exponenten mit 10 malgenommen"),
     B("0 - 2", "den Exponenten unverändert gelassen")]), lp=LP)
neu(T, "negativer_exponent", "sicherung", "darstellung", W(
    "Welche der folgenden Zahlen ist gleich 0,0004?",
    "4 · 10⁻⁴",
    [("4 · 10⁻³", "den Exponenten um 1 zu klein im Betrag gewählt: die Zahl wird zehnmal so groß"),
     ("4 · 10⁻⁵", "den Exponenten um 1 zu groß im Betrag gewählt: die Zahl wird zehnmal so klein"),
     ("4 · 10⁴", "das Minus im Exponenten weggelassen: die Zahl wird sehr groß")],
    "4 · 10⁻⁴ = 4 · 0,0001 = 0,0004. Die 4 steht an der vierten Stelle nach dem Komma, deshalb ist der Exponent −4.",
    lambda: F(4) * F(10) ** -4 == F("0.0004") and F(4) * F(10) ** -3 != F("0.0004") and F(4) * F(10) ** -5 != F("0.0004") and 4 * 10 ** 4 != F("0.0004")), form="bruecke", lp=LP)
# ───────── vorsilben_klein ─────────
neu(T, "vorsilben_klein", "test", "begruenden", W(
    "Wie verhalten sich ein Millimeter (mm) und ein Mikrometer (µm) zueinander?",
    "1 mm = 1000 µm, denn 10⁻³ ist 1000-mal so groß wie 10⁻⁶.",
    [("1 µm = 1000 mm, denn Mikro ist die größere Vorsilbe von beiden.", "Mikro für größer gehalten; Mikro (10⁻⁶) ist kleiner als Milli (10⁻³)"),
     ("1 mm = 100 µm, denn zwischen beiden liegen zwei Stellen.", "die Vorsilben nicht als 10⁻³ und 10⁻⁶ gelesen; der Abstand der Exponenten ist 3, nicht 2"),
     ("1 mm = 10⁶ µm, denn Mikro steht für Millionen von Millimetern.", "Mikro mit Mega verwechselt; Mikro (µ) steht für den Millionstel Teil")],
    "Milli bedeutet 10⁻³ (ein Tausendstel), Mikro bedeutet 10⁻⁶ (ein Millionstel). Es gilt 10⁻³ : 10⁻⁶ = 10³ = 1000. Also sind 1 mm = 1000 µm.",
    lambda: F(10) ** -3 / F(10) ** -6 == 1000 and F(10) ** -6 < F(10) ** -3 and F(10) ** -3 / F(10) ** -6 != 100 and F(10) ** -3 / F(10) ** -6 != 10 ** 6), lp=LP)
neu(T, "vorsilben_klein", "korrektur", "darstellung", Z(
    "Ein Bauteil ist 0,000 000 05 m breit. Wie viele Nanometer (1 nm = 10⁻⁹ m) sind das?",
    50, "5 * 10", "50",
    "0,000 000 05 m = 5 · 10⁻⁸ m. Ein Nanometer ist 10⁻⁹ m, also ist 5 · 10⁻⁸ m = 50 · 10⁻⁹ m = 50 nm.",
    [B("5", "die Ziffer vor den Nullen als Zahl der Nanometer genommen"),
     B("0.00000005 * 10 ** 6", "in Mikrometer statt in Nanometer umgerechnet"),
     B("50 * 10", "eine Zehnerpotenz zu viel: 500 nm statt 50 nm")], einheit="nm"), lp=LP)
neu(T, "vorsilben_klein", "korrektur", "darstellung", L(
    "Ergänze: 3 000 nm = □ µm und 0,25 mm = □ µm.",
    "3 000 nm = □ µm; 0,25 mm = □ µm", [3, 250], ["3000 / 1000", "0.25 * 1000"], ["3", "250"],
    "1 µm = 1000 nm, also 3 000 nm = 3 µm. 1 mm = 1000 µm, also 0,25 mm = 0,25 · 1000 µm = 250 µm.",
    {0: [(3000, "die Zahl 3 000 unverändert übernommen", "3000"), (3000000, "mit 1000 malgenommen statt geteilt", "3000 * 1000")], 1: [(25, "das Komma nur um eine Stelle verschoben", "0.25 * 100"), (2500, "um eine Zehnerpotenz zu viel verschoben", "0.25 * 10000")]}), form="bruecke", lp=LP)
neu(T, "vorsilben_klein", "korrektur", "umkehr", Z(
    "Eine Länge ist 0,000 06 m lang und wird als a µm geschrieben (1 µm = 10⁻⁶ m). Welche Zahl ist a?",
    60, "6 * 10", "60",
    "0,000 06 m = 6 · 10⁻⁵ m. Ein Mikrometer ist 10⁻⁶ m, also ist 6 · 10⁻⁵ m = 60 · 10⁻⁶ m = 60 µm. Probe: 60 · 0,000 001 m = 0,000 06 m.",
    [B("6", "die Ziffer 6 als Zahl der Mikrometer genommen"),
     B("600", "eine Zehnerpotenz zu viel"),
     B("0.6", "das Komma in die falsche Richtung geschoben")]), form="umkehren", lp=LP)
neu(T, "vorsilben_klein", "sicherung", "transfer", Z(
    "Eine Zelle ist 5 µm lang. Wie viele Zellen passen hintereinander auf eine Strecke von 3 mm?",
    600, "3000 / 5", "600",
    "3 mm = 3000 µm. Es passen 3000 µm : 5 µm = 600 Zellen. Probe: 600 · 5 µm = 3000 µm = 3 mm.",
    [B("3000 * 5", "mit 5 malgenommen statt geteilt"),
     B("3000", "die Länge der Zelle ignoriert"),
     B("300 / 5", "3 mm als 300 µm statt als 3000 µm gerechnet")], einheit="Zellen"), form="anwenden", lp=LP)
neu(T, "vorsilben_klein", "sicherung", "fehler", L(
    "Ein Kind rechnet: Zeile 1: 1 nm = 10⁻⁹ m. Zeile 2: 1 µm = 10⁻⁶ m. Zeile 3: Also ist 10⁻⁶ : 10⁻⁹ = 10⁻³. Zeile 4: Also sind 1 µm gleich 10⁻³ nm. In welcher Zeile steckt der erste Fehler? Wie viele Nanometer sind 1 µm richtig?",
    "Fehler in Zeile □, richtig: 1 µm = □ nm", [3, 1000], ["3", "10 ** 3"], ["2 + 1", "1000"],
    "Zeile 1 und Zeile 2 sind richtig. In Zeile 3 ist die Rechnung falsch: 10⁻⁶ : 10⁻⁹ = 10⁻⁶ · 10⁹ = 10³, nicht 10⁻³. Also sind 1 µm gleich 10³ nm = 1000 nm. Zeile 4 folgt aus dem Fehler in Zeile 3.",
    {0: [(4, "die Schlusszeile genannt, weil dort der falsche Wert 10⁻³ steht", "4")], 1: [(-3, "das falsche Ergebnis 10⁻³ als Zahl −3 genommen", "0 - 3"), (1, "die Vorsilben als Faktor 1 gelesen", "1"), (1000000, "mit 10⁶ gerechnet statt 10³", "10 ** 6")]}), form="fehler_detektiv", lp=LP)
neu(T, "vorsilben_klein", "sicherung", "darstellung", W(
    "Welche Zeile ordnet die Längen 5 µm, 2 mm, 800 nm und 0,01 mm von kurz nach lang?",
    "800 nm, 5 µm, 0,01 mm, 2 mm",
    [("5 µm, 800 nm, 0,01 mm, 2 mm", "nur auf die Zahlen vor der Einheit geachtet: 5 kleiner als 800"),
     ("800 nm, 5 µm, 2 mm, 0,01 mm", "0,01 mm = 10 µm zu 0,01 geschrieben und deshalb vor 2 mm eingeordnet"),
     ("2 mm, 0,01 mm, 5 µm, 800 nm", "von lang nach kurz geordnet")],
    "Alles in Mikrometer: 800 nm = 0,8 µm, 5 µm, 0,01 mm = 10 µm, 2 mm = 2000 µm. Von kurz nach lang: 0,8 µm < 5 µm < 10 µm < 2000 µm, also 800 nm, 5 µm, 0,01 mm, 2 mm.",
    lambda: 0.8 < 5 < 10 < 2000 and 800 / 1000 == 0.8 and 0.01 * 1000 == 10 and 2 * 1000 == 2000), form="bruecke", lp=LP)
# ───────── vergleichen_pruefen ─────────
neu(T, "vergleichen_pruefen", "test", "begruenden", W(
    "Welche der Zahlen 8 · 10⁻⁴ und 2 · 10⁻³ ist größer, und warum?",
    "2 · 10⁻³ ist größer, denn 2 · 10⁻³ = 20 · 10⁻⁴ und 20 ist größer als 8.",
    [("8 · 10⁻⁴ ist größer, denn 8 ist größer als 2.", "nur die Vorfaktoren verglichen und die Exponenten nicht beachtet"),
     ("8 · 10⁻⁴ ist größer, denn −4 ist kleiner als −3 und kleiner heißt kleiner Nenner.", "die Exponenten vertauscht: ein kleinerer Exponent gibt eine kleinere Zehnerpotenz"),
     ("Beide sind gleich groß, denn 8 · 4 = 2 · 3.", "die Vorfaktoren mit den Exponenten verrechnet und dabei 8 · 4 gleich 2 · 3 angenommen")],
    "Man bringt beide Zahlen auf denselben Exponenten: 2 · 10⁻³ = 2 · 10 · 10⁻⁴ = 20 · 10⁻⁴. Dann vergleicht man 20 · 10⁻⁴ mit 8 · 10⁻⁴: 20 > 8. Dezimal: 0,002 ist größer als 0,0008.",
    lambda: F(2) * F(10) ** -3 > F(8) * F(10) ** -4 and F(2) * F(10) ** -3 == F(20) * F(10) ** -4 and F(8) * F(10) ** -4 != F(2) * F(10) ** -3 and 8 * 4 != 2 * 3), lp=LP)
neu(T, "vergleichen_pruefen", "korrektur", "darstellung", Z(
    "Der Quotient (6 · 10⁷) : (3 · 10⁴) wird ausgerechnet. Wie lautet das Ergebnis als gewöhnliche Zahl?",
    2000, "2 * 10 ** 3", "6 * 10 ** 7 / (3 * 10 ** 4)",
    "Der Quotient ist (6 · 10⁷) : (3 · 10⁴) = (6 : 3) · 10⁷⁻⁴ = 2 · 10³ = 2000. Probe: 3 · 10⁴ · 2000 = 6 · 10⁷.",
    [B("6 / 3", "nur die Vorfaktoren geteilt"),
     B("2 * 10 ** 4", "die Exponentendifferenz 4 statt 3 genommen"),
     B("7 - 4", "nur die Exponenten subtrahiert")]), form="bruecke", lp=LP)
neu(T, "vergleichen_pruefen", "korrektur", "umkehr", Z(
    "Welches ist die kleinste ganze Zahl n, für die 4 · 10ⁿ größer als 0,005 ist?",
    -2, "0 - 2", "2 - 4",
    "0,005 = 5 · 10⁻³. Für n = −2 ist 4 · 10⁻² = 0,04 > 0,005. Für n = −3 ist 4 · 10⁻³ = 0,004 und das ist kleiner als 0,005. Also ist n = −2 die kleinste Zahl.",
    [B("0 - 3", "die Zahl mit dem Exponenten −3 schon für größer als 0,005 gehalten, ohne die Vorfaktoren zu vergleichen"),
     B("2", "das Minus im Exponenten vergessen"),
     B("0 - 1", "die Zahl n = −1 gewählt, aber −2 ist noch kleiner und erfüllt die Bedingung auch")]), form="umkehren", lp=LP)
neu(T, "vergleichen_pruefen", "korrektur", "darstellung", Z(
    "Wie viele der Zahlen 5 · 10⁵, 50 · 10⁴, 0,5 · 10⁶ und 5 000 000 · 10⁻² sind gleich 500 000?",
    3, "1 + 1 + 1", "3",
    "5 · 10⁵ = 500 000. 50 · 10⁴ = 500 000. 0,5 · 10⁶ = 500 000. Aber 5 000 000 · 10⁻² = 50 000, denn 10⁻² teilt durch 100. Es sind 3 Zahlen gleich 500 000.",
    [B("1 + 1 + 1 + 1", "auch die vierte Zahl mitgezählt, ohne durch 100 zu teilen"),
     B("1", "nur die wissenschaftliche Schreibweise gezählt"),
     B("1 + 1", "die Zahl mit dem Vorfaktor kleiner als 1 und die mit dem großen Vorfaktor nicht mitgezählt")], einheit="Zahlen"), lp=LP)
neu(T, "vergleichen_pruefen", "sicherung", "transfer", Z(
    "Die Sonne hat die Masse 4 · 10³⁰ kg, die Erde 8 · 10²⁴ kg. Wievielmal so schwer wie die Erde ist die Sonne?",
    500000, "5 * 10 ** 5", "4 * 10 ** 30 / (8 * 10 ** 24)",
    "Der Quotient ist (4 · 10³⁰) : (8 · 10²⁴) = (4 : 8) · 10⁶ = 0,5 · 10⁶ = 5 · 10⁵ = 500 000. Die Sonne ist etwa 500 000-mal so schwer wie die Erde.",
    [B("30 - 24", "nur die Exponenten subtrahiert"),
     B("10 ** 6", "die Vorfaktoren ignoriert"),
     B("2 * 10 ** 6", "die Vorfaktoren verkehrt herum geteilt")]), form="anwenden", lp=LP)
neu(T, "vergleichen_pruefen", "sicherung", "fehler", L(
    "Ein Kind vergleicht 3 · 10⁻⁵ und 2 · 10⁻⁴ und rechnet: Zeile 1: Ich vergleiche die beiden Zahlen. Zeile 2: Es gilt 3 > 2. Zeile 3: Also ist 3 · 10⁻⁵ größer als 2 · 10⁻⁴. In welcher Zeile steckt der erste Fehler? Ergänze: 2 · 10⁻⁴ = □ · 10⁻⁵.",
    "Fehler in Zeile □, richtig: 2 · 10⁻⁴ = □ · 10⁻⁵", [2, 20], ["2", "2 * 10"], ["3 - 1", "20"],
    "Zeile 1 ist in Ordnung. Zeile 2 vergleicht nur die Vorfaktoren und lässt die Exponenten außer Acht. Auf gleichen Exponenten gebracht: 2 · 10⁻⁴ = 20 · 10⁻⁵. Dann gilt 3 · 10⁻⁵ < 20 · 10⁻⁵. Zeile 3 folgt aus dem Fehler in Zeile 2.",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3")], 1: [(2, "den Vorfaktor 2 unverändert übernommen", "2"), (1, "den Unterschied 1 der Exponenten als Faktor genommen", "1"), (200, "um zwei Zehnerpotenzen zu viel verschoben", "2 * 100")]}), form="fehler_detektiv", lp=LP)
neu(T, "vergleichen_pruefen", "sicherung", "darstellung", W(
    "Welche der folgenden Zahlen liegt zwischen 3 · 10⁻³ und 4 · 10⁻³?",
    "3,5 · 10⁻³",
    [("3,5 · 10⁻⁴", "nur auf den Vorfaktor 3,5 geachtet; mit dem Exponenten −4 ist die Zahl zu klein"),
     ("3,5 · 10⁻²", "den Exponenten um 1 zu groß gewählt: die Zahl ist zehnmal so groß"),
     ("3,5 · 10³", "das Minus im Exponenten weggelassen")],
    "Zwischen 3 · 10⁻³ und 4 · 10⁻³ liegt jede Zahl mit demselben Exponenten −3 und einem Vorfaktor zwischen 3 und 4, zum Beispiel 3,5 · 10⁻³ = 0,0035. Die anderen haben einen anderen Exponenten.",
    lambda: F(3) * F(10) ** -3 < F("3.5") * F(10) ** -3 < F(4) * F(10) ** -3 and not (F(3) * F(10) ** -3 < F("3.5") * F(10) ** -4 < F(4) * F(10) ** -3) and not (F("3.5") * F(10) ** -2 < F(4) * F(10) ** -3) and not (F("3.5") * F(10) ** 3 < F(4) * F(10) ** -3)), form="bruecke", lp=LP)
