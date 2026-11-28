T = "zahlen.potenzen_zehner"
LP = "M6 1 Rationale Zahlen (Zehnerpotenzen, wissenschaftliche Schreibweise, Vorsilben)"
REGEL[(T, "gross_wissenschaftlich")] = "rr.stellenwert"
REGEL[(T, "negativer_exponent")] = "rr.potenz"
REGEL[(T, "vorsilben_klein")] = "id.verhaeltnisse.groesse"
REGEL[(T, "vergleichen_pruefen")] = "id.zahlen.schreibweisen"
ABG[(T, "gross_wissenschaftlich")] = "Die Übungen schreiben eine große Zahl als a · 10ⁿ; hier wird der Exponentenbereich zu Ungleichungen bestimmt, nach einem Produkt neu normiert, die Ganzzahligkeit untersucht, rückwärts geschlossen und die Bedingung für den Vorfaktor begründet."
ABG[(T, "negativer_exponent")] = "Die Übungen schreiben 10⁻ⁿ als Dezimalzahl; hier werden Zehnerpotenzen verkettet, in Teilungen gedacht, rückwärts skaliert, Kehrwerte gebildet und die Mitte einer Folge von Zehnerpotenzen bestimmt."
ABG[(T, "vorsilben_klein")] = "Die Übungen wandeln eine Einheit um; hier werden Flächen und Geschwindigkeiten mit Vorsilben gerechnet, eine Länge mit Faktor über Einheiten bestimmt und Vorsilben aus Zahlenwerten erschlossen."
ABG[(T, "vergleichen_pruefen")] = "Die Übungen vergleichen zwei einfache Zehnerpotenzen; hier werden Zehnerpotenzen zwischen Grenzen gezählt, Zahlen rückwärts bestimmt, Skalenfaktoren gewählt und Bedingungen für Vorfaktoren gezählt."
# ───────── gross_wissenschaftlich ─────────
# ───────── gross_wissenschaftlich ─────────
# ───────── gross_wissenschaftlich ─────────
neu(T, "gross_wissenschaftlich", "test", "transfer", L(
    "Eine Zahl a · 10ⁿ ist in wissenschaftlicher Schreibweise geschrieben (a zwischen 1 und 10, n eine ganze Zahl). Sie ist größer als 5 000 und kleiner als 80 000. Dann ist der kleinste mögliche Exponent n = □ und der größte mögliche Exponent n = □.",
    "kleinstes n = □, größtes n = □", [3, 4], ["4 - 1", "5 - 1"], ["2 + 1", "8 / 2"],
    "Für n = 3 steht a · 1 000 da, und für a zwischen 5 und 10 liegt das zwischen 5 000 und 10 000: möglich. Für n = 2 wäre die Zahl kleiner als 1 000, also zu klein. Für n = 4 steht a · 10 000 da; mit a unter 8 liegt das unter 80 000: möglich. Für n = 5 wäre die Zahl mindestens 100 000 und damit zu groß. Also gilt n = 3 oder n = 4.",
    {0: [(4, "den Exponenten der oberen Grenze als kleinsten genommen", "4"), (2, "den Exponenten um eins zu klein bestimmt", "3 - 1")],
     1: [(5, "die Zahl der Ziffern von 80 000 als Exponenten genommen", "5"), (3, "den größten Exponenten gleich dem kleinsten gesetzt", "3")]}),
    form="bruecke", lp=LP, idee="bereich_exponent")

neu(T, "gross_wissenschaftlich", "korrektur", "einkleidung", Z(
    "Licht legt in einer Sekunde 3 · 10⁸ m zurück. Wie weit kommt es in 5 · 10³ Sekunden? Das Ergebnis wird in wissenschaftlicher Schreibweise a · 10ⁿ m geschrieben (a zwischen 1 und 10). Wie groß ist n?",
    12, "8 + 3 + 1", "11 + 1",
    "3 · 10⁸ · 5 · 10³ = 15 · 10¹¹. Die Zehnerpotenzen werden malgenommen, die Hochzahlen addiert: 8 + 3 = 11. Der Vorfaktor 15 ist aber nicht kleiner als 10; 15 · 10¹¹ = 1,5 · 10¹². Also ist n = 12. Probe: 1,5 · 10¹² = 1 500 000 000 000 m.",
    [B("8 + 3", "den Vorfaktor 15 nicht auf eine Stelle vor dem Komma gebracht"),
     B("8 * 3", "die Hochzahlen malgenommen statt addiert"),
     B("8 - 3", "die Hochzahlen subtrahiert")], einheit=""), form="bruecke", lp=LP, idee="produkt_normieren")

neu(T, "gross_wissenschaftlich", "korrektur", "umkehr", Z(
    "Für wie viele ganze Zahlen n von −5 bis 5 ist 2,5 · 10ⁿ eine ganze Zahl?",
    5, "5 - 1 + 1", "5",
    "Für n = 0 ist 2,5 · 10⁰ = 2,5, keine ganze Zahl. Für n = 1 ist es 25, und für jedes größere n kommen Nullen hinzu: 25, 250, 2 500, 25 000, 250 000. Für negative n wird die Zahl noch kleiner als 2,5 und ist nie ganz. Es sind die Werte n = 1, 2, 3, 4, 5, also 5.",
    [B("5 + 1", "n = 0 mitgezählt, obwohl 2,5 nicht ganz ist"),
     B("5 + 5 + 1", "alle ganzen Zahlen von −5 bis 5 gezählt"),
     B("5 - 1", "n = 1 nicht mitgezählt, weil dort das Komma noch eine Stelle verschoben wird")], einheit="Werte"), lp=LP, idee="ganzzahl_n")

neu(T, "gross_wissenschaftlich", "sicherung", "umkehr", Z(
    "Eine Zahl a · 10ⁿ ist in wissenschaftlicher Schreibweise geschrieben. Verdoppelt man sie, erhält man 1,6 · 10¹⁰. Wie groß ist n bei der ursprünglichen Zahl?",
    9, "10 - 1", "9",
    "Die ursprüngliche Zahl ist die Hälfte von 1,6 · 10¹⁰, also 0,8 · 10¹⁰. Der Vorfaktor 0,8 ist kleiner als 1: 0,8 · 10¹⁰ = 8 · 10⁹. Die ursprüngliche Zahl ist also 8 · 10⁹ und n = 9. Probe: 2 · 8 · 10⁹ = 16 · 10⁹ = 1,6 · 10¹⁰.",
    [B("10", "nur den Vorfaktor halbiert und den Exponenten unverändert gelassen"),
     B("11", "den Exponenten beim Halbieren vergrößert statt verkleinert"),
     B("8", "den Exponenten um eins zu klein gesetzt")]), form="umkehren", lp=LP, idee="rueckwaerts_halbieren")

neu(T, "gross_wissenschaftlich", "sicherung", "parameter", Z(
    "Eine Zahl a · 10ⁿ ist in wissenschaftlicher Schreibweise geschrieben (a zwischen 1 und 10). Multipliziert man sie mit 4, so ist das Ergebnis in wissenschaftlicher Schreibweise b · 10ⁿ⁺¹ mit dem um eins größeren Exponenten. Wie viele ganze Zahlen a sind dafür möglich?",
    7, "9 - 3 + 1", "7",
    "Das Ergebnis 4a · 10ⁿ hat den Exponenten n + 1 genau dann, wenn 4a mindestens 10 ist, also a ≥ 2,5. Außerdem ist a kleiner als 10. Die ganzen Zahlen von 3 bis 9 erfüllen das: 3, 4, 5, 6, 7, 8, 9, das sind 7. Bei a = 2 ist 4 · 2 = 8 noch kleiner als 10, der Exponent bleibt n.",
    [B("9 - 2 + 1", "a = 2 mitgezählt, obwohl 4 · 2 = 8 den Exponenten nicht ändert"),
     B("9 - 1 + 1", "alle ganzen Zahlen von 1 bis 9 gezählt"),
     B("9 - 3", "die Zahl 3 nicht mitgezählt, weil die Grenze 2,5 nicht ganz ist")], einheit="Zahlen"), lp=LP, idee="a_mal_vier")

# ───────── negativer_exponent ─────────
neu(T, "negativer_exponent", "test", "parameter", Z(
    "Man nimmt ein Hundertstel von einem Millionstel und davon noch ein Tausendstel. Wie viele Nullen stehen zwischen dem Komma und der 1, wenn man das Ergebnis als Dezimalzahl schreibt?",
    10, "2 + 6 + 3 - 1", "11 - 1",
    "Ein Hundertstel ist 10⁻², ein Millionstel ist 10⁻⁶, ein Tausendstel ist 10⁻³. Hintereinander ausgeführt: 10⁻² · 10⁻⁶ · 10⁻³ = 10⁻¹¹ = 0,000 000 000 01. Die 1 steht an der elften Stelle, davor stehen 10 Nullen.",
    [B("11", "den Exponenten als Zahl der Nullen genommen"),
     B("1 + 5 + 2", "die Nullen der drei Dezimalzahlen zusammengezählt"),
     B("2 * 6 * 3", "die Hochzahlen malgenommen statt addiert")], einheit="Nullen"), lp=LP, idee="zehnerpotenzen_verketten")

neu(T, "negativer_exponent", "korrektur", "umkehr", Z(
    "Man startet bei 4 000 und teilt immer wieder durch zehn. Nach wie vielen Teilungen ist das Ergebnis zum ersten Mal kleiner als 0,000 000 1?",
    11, "3 + 8", "11",
    "4 000 = 4 · 10³ und 0,000 000 1 = 10⁻⁷. Jede Teilung durch zehn senkt den Exponenten um 1. Nach 10 Teilungen ist das Ergebnis 4 · 10⁻⁷ = 0,000 000 4 und noch größer als 10⁻⁷. Nach 11 Teilungen ist es 4 · 10⁻⁸ = 0,000 000 04 und damit zum ersten Mal kleiner.",
    [B("3 + 7", "schon gestoppt, als die Zehnerpotenz erreicht war, obwohl der Wert dann noch größer als die Grenze ist"),
     B("7", "nur die Stellen der kleinen Zahl gezählt"),
     B("7 - 3", "die Exponenten der beiden Zahlen voneinander abgezogen")], einheit="Teilungen"), form="umkehren", lp=LP, idee="teilungen_zaehlen")

neu(T, "negativer_exponent", "korrektur", "darstellung", Z(
    "Eine Zehnerpotenz 10ⁿ ist 1 000-mal so klein wie 0,000 01. Wie groß ist n?",
    -8, "0 - 8", "0 - 5 - 3",
    "0,000 01 = 10⁻⁵. 1 000-mal so klein heißt durch 1 000 = 10³ teilen: 10⁻⁵ : 10³ = 10⁻⁸. Probe: 0,000 01 : 1 000 = 0,000 000 01, die 1 steht an der achten Stelle.",
    [B("8", "das Minus im Exponenten vergessen"),
     B("0 - 2", "den Exponenten von 1 000 addiert statt abgezogen"),
     B("0 - 15", "die Hochzahlen malgenommen statt abgezogen")]), form="bruecke", lp=LP, idee="skalierung_rueckwaerts")

neu(T, "negativer_exponent", "sicherung", "darstellung", Z(
    "Man startet bei 10⁻⁷ und multipliziert immer wieder mit 10, bis man bei 10¹ ankommt. Nach der Hälfte dieser Schritte steht die Zehnerpotenz 10ⁿ da. Wie groß ist n?",
    -3, "0 - 7 + 8 / 2", "(0 - 7 + 1) / 2",
    "Von 10⁻⁷ bis 10¹ steigt der Exponent von −7 auf 1, das sind 8 Schritte. Nach der Hälfte, also nach 4 Schritten, ist der Exponent −7 + 4 = −3. Die Zehnerpotenz in der Mitte ist 10⁻³, nicht die Zahl in der Mitte zwischen den Werten. Probe: Von 10⁻⁷ bis 10⁻³ sind es 4 Schritte, von 10⁻³ bis 10¹ auch.",
    [B("3", "das Minus im Exponenten vergessen"),
     B("0 - 8 / 2", "die Hälfte der Schrittzahl selbst als Exponenten genommen"),
     B("0 - 7 + 1", "die beiden Exponenten addiert statt die Mitte zu bilden")]), form=None, lp=LP, idee="mitte_der_potenzen")

neu(T, "negativer_exponent", "sicherung", "transfer", Z(
    "Ein Filter lässt nur den Anteil 10⁻⁹ des Lichts durch. Mit welcher Zehnerpotenz 10ⁿ müsste man die Lichtstärke hinter dem Filter malnehmen, um wieder die ursprüngliche Lichtstärke zu erhalten? Wie groß ist n?",
    9, "0 - (0 - 9)", "9",
    "Hinter dem Filter bleibt der Anteil 10⁻⁹ = 1/1 000 000 000. Um wieder auf das Ganze zu kommen, muss man mit 1 000 000 000 = 10⁹ malnehmen: 10⁻⁹ · 10⁹ = 10⁰ = 1. Also ist n = 9. Allgemein: Der Kehrwert von 10⁻⁹ ist 10⁹.",
    [B("0 - 9", "den Exponenten des Filters ohne Änderung übernommen"),
     B("9 + 1", "eine Zehnerpotenz zu viel"),
     B("9 - 1", "eine Zehnerpotenz zu wenig")], einheit=""), lp=LP, idee="kehrwert_filter")


# ───────── vorsilben_klein ─────────
neu(T, "vorsilben_klein", "test", "transfer", L(
    "Ein Filter lässt nur Teilchen durch, die kürzer als 0,2 µm sind. Vier Teilchen werden geprüft: A ist 90 nm lang, B ist 0,15 µm lang, C ist 0,0002 mm lang, D ist 20 nm lang. (1 nm = 10⁻⁹ m, 1 µm = 10⁻⁶ m, 1 mm = 10⁻³ m.) Es kommen □ Teilchen durch den Filter, und das längste davon ist □ nm lang.",
    "□ Teilchen kommen durch, das längste ist □ nm lang", [3, 150], ["4 - 1", "0.15 * 1000"], ["1 + 2", "15 * 10"],
    "Die Grenze ist 0,2 µm = 200 nm. A mit 90 nm ist kürzer, B mit 0,15 µm = 150 nm ist kürzer, C mit 0,0002 mm = 0,2 µm = 200 nm ist genau so lang wie die Grenze und kommt nicht durch, D mit 20 nm ist kürzer. Es kommen also A, B und D durch, das sind 3 Teilchen. Das längste davon ist B mit 150 nm.",
    {0: [(4, "auch das Teilchen mitgezählt, das genau so lang wie die Grenze ist", "4"), (2, "nur die Maßzahlen mit der Grenze verglichen, ohne die Einheiten anzugleichen", "2")],
     1: [(200, "die Länge des Teilchens genommen, das genau auf der Grenze liegt", "200"), (90, "das Teilchen mit der größten Maßzahl in Nanometern genommen, ohne umzurechnen", "90")]}),
    lp=LP, idee="filter_entscheiden")

neu(T, "vorsilben_klein", "korrektur", "darstellung", Z(
    "Ein Quadrat hat die Seitenlänge 1 mm = 10⁻³ m. Seine Fläche ist 10ᵏ m². Wie groß ist k?",
    -6, "(0 - 3) * 2", "(0 - 3) + (0 - 3)",
    "Die Fläche ist Seitenlänge mal Seitenlänge: 10⁻³ m · 10⁻³ m = 10⁻⁶ m². Beim Malnehmen von Zehnerpotenzen werden die Hochzahlen addiert: −3 + (−3) = −6. Probe: 1 mm² ist ein Millionstel von 1 m².",
    [B("0 - 3", "die Hochzahl der Seitenlänge für die Fläche übernommen"),
     B("6", "das Minus im Exponenten vergessen"),
     B("0 - 9", "die Hochzahl mit 3 malgenommen, wie bei einem Würfel")], einheit=""), form="bruecke", lp=LP, idee="flaeche_exponent")

neu(T, "vorsilben_klein", "korrektur", "einkleidung", Z(
    "Licht legt in einer Sekunde 3 · 10⁸ m zurück. Wie viele Zentimeter legt es in einer Nanosekunde zurück? (1 ns = 10⁻⁹ s, 1 m = 100 cm)",
    30, "3 * 100000000 * 100 / 1000000000", "0.3 * 100",
    "In einer Nanosekunde legt das Licht 3 · 10⁸ m · 10⁻⁹ = 3 · 10⁻¹ m = 0,3 m zurück. In Zentimetern sind das 0,3 · 100 = 30 cm. Probe: In 10⁹ Nanosekunden, also einer Sekunde, sind es 30 cm · 10⁹ = 3 · 10⁸ m.",
    [B("3", "die 0,3 m nicht in Zentimeter umgerechnet und das Komma übersehen"),
     B("300", "eine Zehnerpotenz zu viel beim Umrechnen"),
     B("3 * 100000000 * 100", "die Sekunde nicht in eine Nanosekunde umgerechnet")], einheit="cm"), form="bruecke", lp=LP, idee="licht_ns")

neu(T, "vorsilben_klein", "sicherung", "rueckwaerts", W(
    "Ein Staubkorn ist 0,03 mm lang. Dieselbe Länge soll als 30 □m geschrieben werden (Milli = 10⁻³, Mikro = 10⁻⁶, Nano = 10⁻⁹; die Maßzahl soll zwischen 1 und 1 000 liegen). Welche Vorsilbe gehört in die Lücke?",
    "Mikro (µm), denn 0,03 mm sind 30 µm, und die Einheit µm ist tausendmal kleiner als mm.",
    [("Nano (nm), denn die Einheit muss kleiner werden, und Nano ist die kleinste Vorsilbe.", "nur auf „kleiner“ geachtet und den Faktor zwischen den Einheiten nicht geprüft"),
     ("Milli (mm), denn aus 0,03 wird 30, wenn man das Komma verschiebt, und die Einheit bleibt dabei dieselbe.", "die Maßzahl umgeschrieben und die Einheit nicht gewechselt"),
     ("Zenti (cm), denn eine größere Maßzahl gehört zu einer größeren Einheit.", "Größe der Einheit und Maßzahl gleichgesetzt; zu einer größeren Maßzahl gehört eine kleinere Einheit")],
    "Aus 0,03 mm wird 30 mal etwas: Die Maßzahl wird 1 000-mal größer, also muss die Einheit 1 000-mal kleiner sein. Ein Millimeter ist 1 000 Mikrometer, also 0,03 mm = 30 µm. Nanometer wären eine Million Mal kleiner als Millimeter, Zentimeter sind größer.",
    lambda: F(3, 100) * 1000 == 30 and F(3, 100) * 10 ** 6 != 30), lp=LP, idee="vorsilbe_gesucht")

neu(T, "vorsilben_klein", "sicherung", "mehrschritt", Z(
    "Eine Länge ist 4 000-mal so groß wie 2 nm. Wie viele Mikrometer sind das? (1 µm = 1 000 nm)",
    8, "2 * 4000 / 1000", "8000 / 1000",
    "4 000-mal 2 nm sind 8 000 nm. Weil 1 µm = 1 000 nm ist, sind 8 000 nm genau 8 µm. Probe: 8 µm = 8 · 10⁻⁶ m und 4 000 · 2 · 10⁻⁹ m = 8 · 10⁻⁶ m.",
    [B("2 * 4000", "das Ergebnis in Nanometern nicht in Mikrometer umgerechnet"),
     B("2 * 4000 / 100", "durch 100 statt durch 1 000 geteilt"),
     B("2 * 4000 * 1000", "mit 1 000 malgenommen statt geteilt")], einheit="µm"), form="bruecke", lp=LP, idee="ratio_mikro")


# ───────── vergleichen_pruefen ─────────
neu(T, "vergleichen_pruefen", "test", "transfer", Z(
    "Wie viele Zehnerpotenzen 10ⁿ (n eine ganze Zahl, auch negativ oder null) liegen zwischen 0,000 000 3 und 40 000? Die beiden Grenzen selbst zählen nicht mit.",
    11, "4 + 6 + 1", "5 + 6",
    "0,000 000 3 = 3 · 10⁻⁷ und 40 000 = 4 · 10⁴. Die Zehnerpotenz 10⁻⁷ ist kleiner als 3 · 10⁻⁷ und gehört nicht dazu, 10⁻⁶ ist größer und gehört dazu. Oben ist 10⁴ = 10 000 kleiner als 40 000 und gehört dazu, 10⁵ ist größer. Die Exponenten −6 bis 4 sind 4 + 6 + 1 = 11 Zahlen (die 0 gehört dazu).",
    [B("4 + 6", "die Zehnerpotenz 10⁰ nicht mitgezählt"),
     B("4 + 7 + 1", "auch die Zehnerpotenz mitgezählt, die knapp unter der unteren Grenze liegt"),
     B("4 * 6", "die beiden Exponenten malgenommen")], einheit="Zehnerpotenzen"), form=None, lp=LP, idee="raster_grenzen")

neu(T, "vergleichen_pruefen", "korrektur", "umkehr", Z(
    "Eine Zahl wird mit 10⁻⁴ malgenommen und ergibt 0,006. Welche Zahl war es?",
    60, "0.006 * 10000", "6 * 10000 / 1000",
    "Malnehmen mit 10⁻⁴ heißt durch 10 000 teilen. Rückwärts muss man mit 10 000 malnehmen: 0,006 · 10 000 = 60. Probe: 60 · 10⁻⁴ = 60 : 10 000 = 0,006.",
    [B("0.006 * 100", "mit 100 statt mit 10 000 malgenommen"),
     B("0.006 * 1000", "mit 1 000 statt mit 10 000 malgenommen"),
     B("6 * 100", "die Ziffer 6 mit 100 malgenommen")]), lp=LP, idee="faktor_rueckwaerts")

neu(T, "vergleichen_pruefen", "korrektur", "umkehr", W(
    "Ohne genau zu rechnen: Etwa wie oft passt die Länge 4,8 · 10⁻⁷ m in die Länge 2,1 · 10⁻⁴ m?",
    "etwa 400-mal, denn der Quotient der Vorfaktoren ist ungefähr 0,4 und die Zehnerpotenzen ergeben 10³.",
    [("etwa 40-mal, denn der Quotient der Vorfaktoren ist ungefähr 0,4 und die Zehnerpotenzen ergeben 10².", "den Unterschied der Exponenten um eins zu klein bestimmt"),
     ("etwa 4 000-mal, denn der Quotient der Vorfaktoren ist ungefähr 4 und die Zehnerpotenzen ergeben 10³.", "die Vorfaktoren falsch herum geteilt"),
     ("etwa 0,4-mal, denn der Quotient der Vorfaktoren ist ungefähr 0,4 und die Zehnerpotenzen fallen weg.", "die Exponenten beim Teilen nicht beachtet")],
    "Es geht um 2,1 · 10⁻⁴ : (4,8 · 10⁻⁷). Die Vorfaktoren: 2,1 : 4,8 ist etwa 0,4. Die Zehnerpotenzen: 10⁻⁴ : 10⁻⁷ = 10³. Zusammen etwa 0,4 · 10³ = 400. Genau sind es etwa 437,5.",
    lambda: 300 < F("2.1") * F(10) ** -4 / (F("4.8") * F(10) ** -7) < 500), lp=LP, idee="groessenordnung_quotient")

neu(T, "vergleichen_pruefen", "sicherung", "parameter", Z(
    "Ein Zähler zeigt Vielfache von 0,001 an: k · 10⁻³ mit ganzem k. Wie viele solcher Anzeigen liegen echt zwischen 2 · 10⁻³ und 7 · 10⁻²?",
    67, "69 - 3 + 1", "70 - 2 - 1",
    "Man schreibt 7 · 10⁻² = 70 · 10⁻³ und 2 · 10⁻³ unverändert. Dann sind nur die Vorfaktoren zu vergleichen: 2 < k < 70. Die ganzen Zahlen von 3 bis 69 erfüllen das, das sind 69 − 3 + 1 = 67 Zahlen. Die Grenzen 2 und 70 gehören nicht dazu.",
    [B("69 - 2 + 1", "eine Grenze mitgezählt"),
     B("70 - 2 + 1", "beide Grenzen mitgezählt"),
     B("70", "von 1 bis zur oberen Grenze gezählt")], einheit="Zahlen"), lp=LP, idee="parameter_k")

neu(T, "vergleichen_pruefen", "sicherung", "einkleidung", Z(
    "Ein Messgerät liefert Werte zwischen 2 · 10⁻⁸ und 5 · 10⁻⁵. Für die Anzeige wird jeder Wert mit 10ⁿ malgenommen (n eine ganze Zahl). Der kleinste Wert soll danach größer als 1 sein. Welches ist das kleinste n, für das das gilt?",
    8, "7 + 1", "10 - 2",
    "Der kleinste Wert ist 2 · 10⁻⁸. Mit 10ⁿ malgenommen gibt das 2 · 10ⁿ⁻⁸. Für n = 7 ist das 2 · 10⁻¹ = 0,2, noch kleiner als 1. Für n = 8 ist es 2 · 10⁰ = 2, größer als 1. Also ist das kleinste n gleich 8. Der größte Wert wird dann 5 · 10³ = 5 000.",
    [B("9", "den Vorfaktor 2 übersehen und so gewählt, dass der Wert mindestens zehn ist"),
     B("7", "den Wert 0,2 als größer als 1 gewertet"),
     B("5", "den Exponenten des größten Werts genommen")], einheit=""), form="bruecke", lp=LP, idee="skala_faktor")


# ───────── vorrat ─────────
neu(T, "gross_wissenschaftlich", "sicherung", "begruenden", W(
    "Warum ist 0,5 · 10⁸ keine wissenschaftliche Schreibweise der Zahl 50 000 000?",
    "Der Vorfaktor 0,5 ist kleiner als 1, wissenschaftlich wäre 5 · 10⁷.",
    [("Der Exponent 8 ist zu groß; man darf höchstens 10⁷ verwenden.", "eine Höchstgrenze für den Exponenten erfunden; Exponenten dürfen beliebig groß sein"),
     ("0,5 · 10⁸ ist eine andere Zahl als 50 000 000; richtig wäre 0,05 · 10⁸.", "den Wert falsch gerechnet: 0,5 · 10⁸ ist bereits 50 000 000, nur der Vorfaktor passt nicht"),
     ("Der Vorfaktor muss eine ganze Zahl sein; 0,5 ist keine ganze Zahl.", "verlangt, dass der Vorfaktor ganzzahlig ist; auch Dezimalzahlen zwischen 1 und 10 sind erlaubt")],
    "0,5 · 10⁸ = 50 000 000 ist richtig als Wert. Es fehlt nur die Bedingung 1 ≤ a < 10: 0,5 ist kleiner als 1. Man verschiebt das Komma um eine Stelle nach rechts und verkleinert den Exponenten: 5 · 10⁷ = 50 000 000.",
    lambda: 0.5 * 10 ** 8 == 5 * 10 ** 7 == 50000000 and not 1 <= 0.5 < 10 and 1 <= 5 < 10 and 1 <= 2.5 < 10), lp=LP, idee="bedingung_begruenden")


neu(T, "gross_wissenschaftlich", "test", "fehler", L(
    "Ein Kind soll 23,1 · 10⁴ in wissenschaftliche Schreibweise bringen und rechnet: Zeile 1: Ich muss das Komma verschieben. Zeile 2: 23,1 = 2,31 · 10. Zeile 3: Die Zahl bleibt dieselbe, also bleibt der Exponent 4: 23,1 · 10⁴ = 2,31 · 10⁴. In welcher Zeile steckt der erste Fehler? Welcher Exponent gehört richtig an die 10?",
    "Fehler in Zeile □, richtig: 23,1 · 10⁴ = 2,31 · 10^□", [3, 5], ["3", "4 + 1"], ["2 + 1", "5"],
    "Zeile 1 sagt nur, was getan wird. Zeile 2 stimmt (2,31 · 10 = 23,1). In Zeile 3 wird die Zehn aus Zeile 2 vergessen: 23,1 · 10⁴ = 2,31 · 10 · 10⁴ = 2,31 · 10⁵. Wird das Komma um eine Stelle nach links geschoben, muss der Exponent um 1 größer werden, sonst ändert sich der Wert der Zahl.",
    {0: [(2, "Zeile 2 genannt, weil dort das Komma verschoben wird, obwohl diese Zeile stimmt", "2"), (1, "Zeile 1 genannt, obwohl dort nur das Vorgehen steht", "1")], 1: [(4, "den Exponenten unverändert übernommen", "4"), (3, "den Exponenten beim Verschieben des Kommas verkleinert", "4 - 1"), (14, "die Zehn zum Exponenten addiert", "4 + 10")]}), form="fehler_detektiv", lp=LP, idee="komma_ausgleich")

neu(T, "gross_wissenschaftlich", "sicherung", "umkehr", Z(
    "Ein Buch hat etwa 4 · 10⁵ Zeichen. Ein Speicher fasst 2 · 10⁹ Zeichen. Wie viele solcher Bücher passen höchstens in den Speicher?",
    5000, "2000000000 / 400000", "2000000000 / 400000",
    "2 · 10⁹ = 2 000 000 000 und 4 · 10⁵ = 400 000. Es passen 2 000 000 000 : 400 000 = 5 000 Bücher. Mit Potenzen: 2 : 4 = 0,5 und 10⁹ : 10⁵ = 10⁴, also 0,5 · 10⁴ = 5 000.",
    [B("500", "den Exponenten um eins zu klein gerechnet"),
     B("50000", "den Exponenten um eins zu groß gerechnet"),
     B("20000", "die Vorfaktoren falsch herum geteilt")], einheit="Bücher"), lp=LP, idee="passt_wie_oft")

neu(T, "negativer_exponent", "sicherung", "fehler", L(
    "Ein Kind rechnet: Zeile 1: 10⁻³ bedeutet 1 : 10³, also 1 : 1 000. Zeile 2: Der Exponent ist negativ, also ist auch die Zahl 10⁻³ negativ, nämlich −0,001. Zeile 3: Also ist 10⁻³ · 1 000 = −0,001 · 1 000 = −1. In welcher Zeile steckt der erste Fehler? Wie viel ist 10⁻³ · 1 000 richtig?",
    "Fehler in Zeile □, richtig: 10⁻³ · 1 000 = □", [2, 1], ["2", "1 + 0"], ["1 + 1", "1000 / 1000"],
    "Zeile 1 stimmt: 10⁻³ = 1 : 1 000 = 0,001. In Zeile 2 steckt der Fehler: Das Minus im Exponenten macht die Zahl nicht negativ, sondern klein. 10⁻³ = 0,001 ist positiv. Zeile 3 folgt aus dem Fehler. Richtig: 10⁻³ · 1 000 = 0,001 · 1 000 = 1.",
    {0: [(1, "Zeile 1 genannt, obwohl dort die Bedeutung richtig angegeben ist", "1"), (3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3")], 1: [(-1, "das Minus aus dem Exponenten mit in die Zahl genommen", "0 - 1"), (0, "die kleine Zahl mit dem Tausendfachen als null gerechnet", "0"), (-3, "den Exponenten als Ergebnis genommen", "0 - 3")]}), form="fehler_detektiv", lp=LP, idee="minus_macht_negativ")

neu(T, "vorsilben_klein", "korrektur", "umkehr", Z(
    "Ein Virus ist 4 500 nm lang. In Millimetern schreibt man die Länge als 4,5 · 10ⁿ mm. Wie groß ist n? (1 nm = 10⁻⁹ m, 1 mm = 10⁻³ m)",
    -3, "0 - 3", "3 - 6",
    "1 mm = 10⁶ nm. 4 500 nm = 4 500 : 1 000 000 mm = 0,0045 mm. Das Komma steht dann hinter der ersten Ziffer, es ist drei Stellen nach rechts gewandert: 0,0045 = 4,5 · 10⁻³. Also ist n = −3.",
    [B("3", "das Minus im Exponenten vergessen"),
     B("0 - 6", "nur den Faktor zwischen Nanometer und Millimeter als Exponenten genommen"),
     B("0 - 9", "die Hochzahl der Vorsilbe Nano als Exponenten genommen")]), form="umkehren", lp=LP, idee="umrechnen_wissenschaftlich")

neu(T, "vorsilben_klein", "sicherung", "fehler", L(
    "Ein Kind rechnet: Zeile 1: 1 nm = 10⁻⁹ m. Zeile 2: 1 µm = 10⁻⁶ m. Zeile 3: Also ist 10⁻⁶ : 10⁻⁹ = 10⁻³. Zeile 4: Also sind 1 µm gleich 10⁻³ nm. In welcher Zeile steckt der erste Fehler? Wie viele Nanometer sind 1 µm richtig?",
    "Fehler in Zeile □, richtig: 1 µm = □ nm", [3, 1000], ["3", "10 ** 3"], ["2 + 1", "1000"],
    "Zeile 1 und Zeile 2 sind richtig. In Zeile 3 ist die Rechnung falsch: 10⁻⁶ : 10⁻⁹ = 10⁻⁶ · 10⁹ = 10³, nicht 10⁻³. Also sind 1 µm gleich 10³ nm = 1000 nm. Zeile 4 folgt aus dem Fehler in Zeile 3.",
    {0: [(4, "die Schlusszeile genannt, weil dort der falsche Wert 10⁻³ steht", "4"), (1, "Zeile 1 genannt, obwohl dort die Vorsilbe richtig steht", "1")], 1: [(-3, "das falsche Ergebnis 10⁻³ als Zahl −3 genommen", "0 - 3"), (1, "die Vorsilben als Faktor 1 gelesen", "1"), (1000000, "mit 10⁶ gerechnet statt 10³", "10 ** 6")]}), form="fehler_detektiv", lp=LP, idee="fehler_kette")

neu(T, "vergleichen_pruefen", "test", "transfer", L(
    "Gegeben sind drei Zahlen: A = 5 · 10⁻⁶, B = 0,2 · 10⁻⁴ und C = 30 · 10⁻⁷. Welche Zahl ist die kleinste, welche die größte? Trage jeweils die Nummer ein (1 = A, 2 = B, 3 = C).",
    "kleinste Zahl: □, größte Zahl: □", [3, 2], ["3", "1 + 1"], ["1 + 2", "2"],
    "Alle drei Zahlen mit dem Exponenten −7: A = 50 · 10⁻⁷, B = 0,2 · 10⁻⁴ = 200 · 10⁻⁷, C = 30 · 10⁻⁷. Die kleinste ist C (30), die größte ist B (200). Ausgeschrieben: A = 0,000 005, B = 0,000 02, C = 0,000 003.",
    {0: [(2, "nur die Vorfaktoren verglichen: 0,2 ist der kleinste Vorfaktor", "2"), (1, "die mittlere Zahl A genannt, ohne alle Zahlen auf einen gemeinsamen Exponenten zu bringen", "1")],
     1: [(3, "nur die Vorfaktoren verglichen: 30 ist der größte Vorfaktor", "3"), (1, "die mittlere Zahl A genannt, ohne alle Zahlen auf einen gemeinsamen Exponenten zu bringen", "1")]}), lp=LP, idee="normalisieren_ordnen")

neu(T, "vergleichen_pruefen", "sicherung", "fehler", L(
    "Ein Kind vergleicht 6 · 10⁻⁷ und 4 · 10⁻⁶ und rechnet: Zeile 1: Ich schreibe beide Zahlen mit dem Exponenten −7. Zeile 2: Dann ist 4 · 10⁻⁶ = 0,4 · 10⁻⁷, denn das Komma geht eine Stelle nach links. Zeile 3: Also ist 6 · 10⁻⁷ größer als 4 · 10⁻⁶. In welcher Zeile steckt der erste Fehler? Welcher Vorfaktor gehört richtig vor 10⁻⁷?",
    "Fehler in Zeile □, richtig: 4 · 10⁻⁶ = □ · 10⁻⁷", [2, 40], ["2", "4 * 10"], ["1 + 1", "400 / 10"],
    "Zeile 1 sagt nur, was getan wird. In Zeile 2 steckt der Fehler: 10⁻⁷ ist zehnmal kleiner als 10⁻⁶, deshalb muss der Vorfaktor zehnmal größer werden: 4 · 10⁻⁶ = 40 · 10⁻⁷. Zeile 3 folgt aus dem Fehler. Richtig ist: 4 · 10⁻⁶ ist größer als 6 · 10⁻⁷.",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3"), (1, "Zeile 1 genannt, obwohl dort nur das Vorgehen steht", "1")], 1: [(4, "den Vorfaktor unverändert übernommen", "4"), (400, "den Vorfaktor um zwei Stellen verschoben statt um eine", "4 * 100")]}), form="fehler_detektiv", lp=LP, idee="angleichen_richtung")

# Regel je Aufgabe nach Lernziel und Denkleistung differenziert (Urteil 1222)
for _a in A:
    if _a["thema"] == T and _a["lk"] == "vergleichen_pruefen":
        _a["regel"] = "rr.potenz" if _a["idee"] in ("faktor_rueckwaerts", "raster_grenzen", "groessenordnung_quotient") else "id.zahlen.schreibweisen"
