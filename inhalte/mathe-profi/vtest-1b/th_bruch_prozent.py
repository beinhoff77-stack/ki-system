T = "bruch.prozent"
LP = "M6 3 Prozentrechnung (Prozentwert, Grundwert und Prozentsatz; Prozente verstehen)"
REGEL[(T, "prozentwert")] = REGEL[(T, "grundwert")] = REGEL[(T, "verstehen")] = "id.verhaeltnisse.prozent"
ABG[(T, "prozentwert")] = "Die Übungen berechnen einen Prozentwert mit einem Satz; hier müssen mehrere Prozentsätze auf verschiedene Ganze bezogen, Größenordnungen abgeschätzt oder eine Prozentangabe in eine andere Darstellung gebracht werden."
ABG[(T, "grundwert")] = "Die Übungen berechnen den Grundwert aus Prozentwert und Prozentsatz; hier wird der Grundwert für weitere Aussagen über dasselbe Ganze gebraucht, in Darstellungen gelesen oder mit anderen Grundwerten verglichen."
ABG[(T, "verstehen")] = "Die Übungen rechnen mit Prozenten; hier wird begründet, warum sich Prozentzahlen immer auf ein bestimmtes Ganzes beziehen und was sich ändert, wenn das Ganze wechselt."
# ───────── prozentwert ─────────
# ───────── prozentwert ─────────
neu(T, "prozentwert", "test", "transfer", Z(
    "In einer Schüssel sind 800 g Salzlösung mit 5 % Salz. Man gießt reines Wasser dazu, bis die Lösung nur noch 2 % Salz enthält. Wie viel Gramm Wasser muss man dazugießen?",
    1200, "800 * 5 / 2 - 800", "800 * 0.05 / 0.02 - 800",
    "Das Salz bleibt beim Verdünnen gleich: 5 % von 800 g sind 40 g. Diese 40 g sollen nur noch 2 % der neuen Lösung sein, also ist die neue Lösung 40 g : 0,02 = 2 000 g schwer. Dazugegossen werden 2 000 g − 800 g = 1 200 g Wasser. Probe: 2 % von 2 000 g sind 40 g.",
    [B("800 * 0.05 / 0.02", "die neue Gesamtmasse der Lösung als zugegossene Wassermenge angegeben"),
     B("800 * 0.03", "den Unterschied der beiden Prozentsätze auf die alte Lösung angewendet"),
     B("800 * 0.05", "die Salzmenge statt der Wassermenge angegeben")], einheit="g"),
    lp=LP, idee="verduennen")

neu(T, "prozentwert", "korrektur", "umkehr", Z(
    "Aus einer Gruppe soll genau 35 % der Kinder ausgewählt werden, und die Zahl der Ausgewählten muss eine ganze Zahl sein. Für wie viele Gruppengrößen n von 1 bis 100 ist das möglich?",
    5, "100 / 20", "10 / 2",
    "35 % sind 35/100 = 7/20. Damit 7/20 von n eine ganze Zahl ist, muss n durch 20 teilbar sein, denn 7 und 20 haben keinen gemeinsamen Teiler. Die Gruppengrößen sind 20, 40, 60, 80 und 100, das sind 5. Probe: 35 % von 60 sind 21.",
    [B("35", "die Prozentzahl selbst als Anzahl der Gruppengrößen angegeben"),
     B("100 / 5", "die Gruppengrößen gezählt, die durch die Kürzungszahl von 35 teilbar sind"),
     B("100 / 10", "nur die vollen Zehner gezählt")], einheit="Gruppengrößen"),
    form="umkehren", lp=LP, idee="ganzzahl_prozent")

neu(T, "prozentwert", "korrektur", "einkleidung", Z(
    "Ein Behälter mit 500 l Wasser verliert jeden Tag 8 % seines ursprünglichen Inhalts durch Verdunstung. Nach wie vielen Tagen ist der Behälter zum ersten Mal leer?",
    13, "12 + 1", "100 / 8 + 0.5",
    "Jeden Tag verdunsten 8 % von 500 l, das sind 40 l. Weil es immer dieselben 8 % des ursprünglichen Inhalts sind, nimmt der Inhalt gleichmäßig ab. Nach 12 Tagen sind 96 % verdunstet, es bleiben 20 l, und am 13. Tag ist der Behälter leer. Nach 12 Tagen ist er noch nicht leer, 100 : 8 = 12,5 wird aufgerundet.",
    [B("100 / 8", "auf 12,5 Tage gerundet statt auf den ersten ganzen Tag, an dem der Behälter leer ist"),
     B("100 / 8 - 0.5", "abgerundet: nach 12 Tagen sei der Behälter leer"),
     B("500 * 0.08", "die täglich verdunstete Menge in Litern als Anzahl der Tage angegeben")], einheit="Tage"),
    form="bruecke", lp=LP, idee="behaelter_taeglich")

neu(T, "prozentwert", "sicherung", "begruenden", W(
    "Ein Laden verkauft Hefte für h Euro und Stifte für s Euro. Auf beides gibt es denselben Rabatt von 12 %. Jemand berechnet den Rabatt nicht einzeln, sondern als 12 % vom gesamten Preis h + s. Welche Aussage stimmt?",
    "Das stimmt, denn 0,12 · h + 0,12 · s ist dasselbe wie 0,12 · (h + s).",
    [("Das stimmt nicht, denn der Rabatt bezieht sich auf zwei verschiedene Beträge, und die darf man bei der Rechnung nicht zusammenfassen.", "gedacht, bei verschiedenen Beträgen müsse man den Prozentsatz einzeln anwenden"),
     ("Das stimmt nicht, denn 12 % vom gesamten Preis sind mehr als die beiden einzelnen Rabatte zusammen.", "geglaubt, beim Zusammenfassen der Beträge werde der Rabatt größer"),
     ("Das stimmt nicht, denn nur bei gleich großen Beträgen darf man zuerst addieren und dann den Rabatt berechnen.", "geglaubt, das Zusammenfassen gehe nur bei gleichen Beträgen")],
    "Beide Rabatte sind 12 % des jeweiligen Betrags: 0,12 · h und 0,12 · s. Der Faktor 0,12 steht in beiden Summanden und darf ausgeklammert werden (Verteilungsgesetz): 0,12 · h + 0,12 · s = 0,12 · (h + s). Die Beträge müssen dafür nicht gleich groß sein. Zahlenprobe: h = 350 und s = 150 geben 42 + 18 = 60, und 12 % von 500 sind ebenfalls 60.",
    lambda: all(F(12, 100) * a + F(12, 100) * b == F(12, 100) * (a + b) for a in (350, 7, 99, 1) for b in (150, 40, 1, 12)) and F(12, 100) * 350 + F(12, 100) * 150 == 60 == F(12, 100) * 500), lp=LP, idee="distributiv")

neu(T, "prozentwert", "sicherung", "einkleidung", L(
    "Bei einer Qualitätskontrolle sind 0,15 % von 40 000 Bauteilen fehlerhaft. Es sind □ Bauteile fehlerhaft und □ Bauteile fehlerfrei.",
    "□ fehlerhaft, □ fehlerfrei", [60, 39940], ["0.0015 * 40000", "40000 - 0.0015 * 40000"], ["40000 * 15 / 10000", "40000 * 99.85 / 100"],
    "0,15 % sind 0,15 : 100 = 0,0015. 0,0015 · 40 000 = 60 Bauteile sind fehlerhaft. Fehlerfrei sind die übrigen 40 000 − 60 = 39 940 Bauteile. Zur Probe: 1 % wären 400 Bauteile, 0,15 % sind also deutlich weniger als ein halbes Prozent.",
    {0: [(6000, "das Komma im Prozentsatz überlesen und mit der ganzen Prozentzahl gerechnet", "0.15 * 40000"), (600, "das Komma beim Umrechnen in einen Dezimalbruch um eine Stelle falsch gesetzt", "0.015 * 40000"), (6, "das Komma beim Umrechnen um eine Stelle zu weit nach links gesetzt", "0.00015 * 40000")],
     1: [(34000, "den Prozentsatz zu groß angesetzt und davon abgezogen", "40000 - 6000"), (40000, "gedacht, bei so kleinem Prozentsatz seien alle Teile fehlerfrei", "40000"), (39994, "von den 40 000 Bauteilen den falschen Wert 6 abgezogen", "40000 - 6")]}),
    form="bruecke", lp=LP, idee="bauteile")

# ───────── grundwert ─────────
neu(T, "grundwert", "test", "transfer", Z(
    "Frische Gurken bestehen zu 99 % aus Wasser. 100 kg frische Gurken werden getrocknet, bis sie nur noch zu 98 % aus Wasser bestehen. Wie viel Kilogramm wiegen sie dann?",
    50, "100 * 0.01 / 0.02", "100 / 2",
    "Die Trockenmasse ändert sich nicht: 1 % von 100 kg sind 1 kg. Nach dem Trocknen sind diese 1 kg nicht mehr 1 %, sondern 2 % der Masse. 2 % sind 1 kg, also sind 100 % genau 50 kg. Die Masse halbiert sich, obwohl der Wassergehalt nur um einen Prozentpunkt sinkt.",
    [B("100 * 0.98", "98 % der ursprünglichen Masse berechnet"),
     B("100 * 0.01", "nur die Trockenmasse angegeben"),
     B("100 * 0.99", "99 % der ursprünglichen Masse als Ergebnis genommen")], einheit="kg"),
    lp=LP, idee="gurken")

neu(T, "grundwert", "korrektur", "umkehr", Z(
    "Von einem Betrag sind 30 % um 12 € größer als 20 % desselben Betrags. Wie groß ist der Betrag?",
    120, "12 / (0.3 - 0.2)", "12 * 10",
    "Der Unterschied der beiden Anteile ist 30 % − 20 % = 10 % des Betrags, und das sind 12 €. Also sind 1 % genau 1,20 € und 100 % genau 120 €. Probe: 30 % von 120 € sind 36 €, 20 % von 120 € sind 24 €, und 36 € − 24 € = 12 €.",
    [B("12 / 0.3", "die 12 € als 30 % genommen, obwohl sie nur der Unterschied der beiden Anteile sind"),
     B("12 / 0.5", "die beiden Prozentsätze addiert statt voneinander abgezogen"),
     B("12 / 0.2", "die 12 € als 20 % genommen")], einheit="€"), lp=LP, idee="differenz_prozentsaetze")

neu(T, "grundwert", "korrektur", "darstellung", Z(
    "In einem Kreisdiagramm gehört zum Sektor „Fußweg“ der Mittelpunktswinkel 54°. Diesem Sektor entsprechen 63 Kinder. Wie viele Kinder wurden insgesamt befragt?",
    420, "63 / (54 / 360)", "63 * 360 / 54",
    "Der volle Kreis hat 360°, der Sektor 54° ist 54 : 360 = 0,15 = 15 % des Kreises. 63 Kinder sind also 15 % aller Kinder. 1 % sind 4,2 Kinder, 100 % sind 420 Kinder.",
    [B("63 * 54 / 360", "15 % von 63 berechnet, obwohl 63 schon der Teil ist"),
     B("63 * 54", "die Kinderzahl mit dem Winkel malgenommen"),
     B("63 + 360 - 54", "die Zahlen aus dem Text gemischt addiert und subtrahiert")], einheit="Kinder"), lp=LP, idee="winkel_zurueck")

neu(T, "grundwert", "sicherung", "begruenden", W(
    "Anna und Ben haben beide denselben Betrag gespart. Bei Anna sind das 30 % ihres Sparziels, bei Ben 60 % seines Sparziels. Welche Aussage über die Sparziele stimmt?",
    "Bens Sparziel ist halb so groß wie Annas, denn derselbe Betrag sind bei Ben doppelt so viele Prozent.",
    [("Bens Sparziel ist doppelt so groß wie Annas, denn Ben hat doppelt so viele Prozent seines Ziels gespart.", "aus dem doppelten Prozentsatz auf das doppelte Ziel geschlossen"),
     ("Die Sparziele sind gleich groß, denn beide haben denselben Betrag gespart und das Ziel steht für das Ganze.", "gedacht, gleiche gesparte Beträge bedeuten gleiche Ziele"),
     ("Bens Sparziel ist um 30 niedriger als Annas, denn der Unterschied der Prozentzahlen ist 30.", "den Unterschied der Prozentzahlen als Unterschied der Ziele gelesen")],
    "Der gesparte Betrag ist der Prozentwert und bei beiden gleich, etwa 18 €. Annas Ziel: 18 € : 0,3 = 60 €. Bens Ziel: 18 € : 0,6 = 30 €. Je mehr Prozent derselbe Betrag ist, desto kleiner ist das Ganze: Bei doppelt so vielen Prozent ist das Ziel nur halb so groß. Das gilt für jeden Betrag.",
    lambda: all(F(b) / F(3, 10) == 2 * (F(b) / F(6, 10)) for b in (6, 18, 45, 90)) and F(18) / F(3, 10) != F(18) / F(6, 10)), lp=LP, idee="antiproportional")

neu(T, "grundwert", "sicherung", "einkleidung", Z(
    "Ein Müsli besteht zu 25 % aus Nüssen. Man gibt 150 g Nüsse dazu, danach machen die Nüsse 50 % des Müslis aus. Wie viel Gramm Müsli waren es vorher?",
    300, "150 * 0.5 / (0.75 - 0.5)", "300",
    "Alles außer den Nüssen bleibt gleich: Das sind vorher 75 % des alten Müslis, nachher 50 % des neuen. Das neue Müsli ist um 150 g schwerer als das alte. Es gilt: 75 % vom alten = 50 % vom alten + 50 % von 150 g, also 25 % vom alten = 75 g und das alte Müsli wiegt 75 g : 0,25 = 300 g. Probe: 25 % von 300 g sind 75 g Nüsse, dazu 150 g gibt 225 g von insgesamt 450 g, das sind 50 %.",
    [B("150 / 0.25", "die zugegebenen Gramm als Unterschied der beiden Nussanteile gedeutet"),
     B("150", "die zugegebene Menge als Anfangsmasse genommen"),
     B("150 * 0.5 / (0.75 - 0.5) + 150", "das Gewicht nach der Zugabe statt vorher angegeben")], einheit="g"), form="bruecke", lp=LP, idee="muesli_nuesse")

# ───────── verstehen ─────────
neu(T, "verstehen", "test", "begruenden", W(
    "Bei Verein A sind 20 % der Mitglieder mehr Personen als 30 % der Mitglieder von Verein B. Welche Aussage über die Mitgliederzahlen folgt sicher?",
    "A hat mehr als anderthalbmal so viele Mitglieder wie B, denn 20 % von A sind mehr als 30 % von B.",
    [("Verein A hat weniger Mitglieder als Verein B, denn 20 % sind weniger als 30 %.", "die Prozentzahlen verglichen und vergessen, dass sie sich auf verschiedene Ganze beziehen"),
     ("Verein A hat genau doppelt so viele Mitglieder wie Verein B, denn 20 % von A sind mehr als 30 % von B.", "aus der Ungleichung einen genauen Wert gemacht; es folgt nur, dass A mehr als anderthalbmal so groß ist"),
     ("Verein A hat genau anderthalbmal so viele Mitglieder wie Verein B, denn 20 % von A sind mehr als 30 % von B.", "das Verhältnis 30 : 20 als genauen Wert genommen, obwohl der Vergleich nur mehr als sagt")],
    "Es gilt 0,2 · A > 0,3 · B. Teilt man durch 0,2, folgt A > 1,5 · B. A ist also mehr als anderthalbmal so groß wie B; ein genauer Wert folgt nicht. Beispiel: B = 100 Mitglieder, dann muss A größer als 150 sein.",
    lambda: F(3, 10) / F(2, 10) == F(3, 2) and all(F(2, 10) * a > F(3, 10) * 100 for a in (151, 200, 400)) and not (F(2, 10) * 150 > F(3, 10) * 100)), lp=LP, idee="ganze_verschieden")

neu(T, "verstehen", "korrektur", "umkehr", Z(
    "In einer Klasse mit 24 Kindern sind 6 Linkshänder. Einige Rechtshänder ziehen weg, die Linkshänder bleiben. Mindestens wie viele Rechtshänder müssen wegziehen, damit die Linkshänder mindestens 40 % der Klasse ausmachen?",
    9, "24 - 6 / 0.4", "24 - 15",
    "Die 6 Linkshänder sollen mindestens 40 % der Klasse sein, also darf die Klasse höchstens 6 : 0,4 = 15 Kinder haben. Von den 24 Kindern müssen deshalb mindestens 24 − 15 = 9 wegziehen. Probe: 6 von 15 Kindern sind genau 40 %. Das Ganze wird kleiner, der Prozentsatz der unveränderten Gruppe steigt.",
    [B("24 - 6", "alle Rechtshänder wegziehen lassen"),
     B("6 / 0.4", "die höchstens noch erlaubte Klassengröße als Zahl der Wegziehenden angegeben"),
     B("24 - 6 / 0.5", "für einen größeren Anteil gerechnet, als verlangt ist")], einheit="Kinder"),
    lp=LP, idee="wegzug")

neu(T, "verstehen", "korrektur", "einkleidung", Z(
    "In einem Jahrgang spielen 40 Kinder Fußball. 30 % dieser Fußballer sind Mädchen. Im ganzen Jahrgang gibt es 48 Mädchen. Wie viel Prozent aller Mädchen des Jahrgangs spielen Fußball?",
    25, "0.3 * 40 / 48 * 100", "12 / 48 * 100",
    "Die 30 % beziehen sich auf die Fußballer. 30 % von 40 sind 12 Mädchen, die Fußball spielen. Gefragt ist aber der Anteil an allen 48 Mädchen: 12 : 48 = 0,25 = 25 %. Die Zahl 30 % und die gesuchten 25 % haben verschiedene Ganze.",
    [B("30", "die 30 % als Antwort genommen, obwohl sie sich auf die Fußballer beziehen"),
     B("0.3 * 40", "die Anzahl der Mädchen unter den Fußballern als Prozentzahl angegeben"),
     B("48 / 12 * 100", "die Teile verkehrt herum geteilt: alle Mädchen durch die Fußballerinnen")], einheit="%"),
    form="bruecke", lp=LP, idee="bezug_wechsel")

neu(T, "verstehen", "sicherung", "parameter", Z(
    "Eine Gruppe hat 20 Kinder, davon 12 Mädchen. Es kommen 10 Kinder dazu, darunter m Mädchen. Danach sollen die Mädchen höchstens 50 % der Gruppe sein, ihre Zahl soll aber größer sein als vorher. Wie viele ganze Zahlen m sind möglich?",
    3, "15 - 12", "30 / 2 - 12",
    "Die Gruppe hat danach 30 Kinder, davon höchstens die Hälfte, also höchstens 15 Mädchen. Vorher waren es 12, also muss 12 + m ≤ 15 gelten, das heißt m ≤ 3. Die Zahl der Mädchen soll größer werden, also m ≥ 1. Möglich sind m = 1, 2 und 3.",
    [B("15 - 12 + 1", "m = 0 mitgezählt, obwohl die Zahl der Mädchen steigen soll"),
     B("30 / 2", "die höchste erlaubte Mädchenzahl als Anzahl der möglichen Werte angegeben"),
     B("20 / 2", "nur die Hälfte der ursprünglichen Gruppe betrachtet")], einheit="Werte"),
    lp=LP, idee="maedchen_dazu")

neu(T, "verstehen", "sicherung", "darstellung", Z(
    "Der Eintritt für ein Schwimmbad kostete 30 €. Nach dem Umbau steigt der Preis um 200 %. Wie viel Euro kostet der Eintritt danach?",
    90, "30 + 30 * 200 / 100", "30 * 3",
    "200 % von 30 € sind 2 · 30 € = 60 €. Der Preis steigt um 60 €, also kostet der Eintritt danach 30 € + 60 € = 90 €. Das ist das Dreifache (300 % des alten Preises). „Um 200 % steigen“ heißt nicht „auf 200 % steigen“.",
    [B("2 * 30", "„um 200 % steigen“ als „auf 200 % steigen“ gelesen: nur 2 · 30"),
     B("30 + 200", "die 200 % als 200 € gelesen und zum alten Preis addiert"),
     B("30 * 200", "mit der Prozentzahl 200 malgenommen, ohne sie in einen Anteil umzuwandeln")], einheit="€"), form="bruecke", lp=LP, idee="um_oder_auf")

# ───────── vorrat ─────────
neu(T, "prozentwert", "sicherung", "fehler", L(
    "Max soll 8 % von 450 € berechnen und schreibt: Zeile 1: 8 % = 8/100 = 0,8. Zeile 2: 0,8 · 450 = 360. Zeile 3: Also sind 8 % von 450 € genau 360 €. In welcher Zeile steckt der erste Fehler, und wie viele Euro sind 8 % von 450 € richtig?",
    "Fehler in Zeile □, richtig: □ €", [1, 36], ["1", "0.08 * 450"], ["2 - 1", "450 * 8 / 100"],
    "Zeile 1 ist falsch: 8/100 ist 0,08 und nicht 0,8 (0,8 wären 80 %). Zeile 2 ist als Rechnung richtig (0,8 · 450 = 360), übernimmt aber den Fehler. Richtig: 0,08 · 450 € = 36 €. Probe: 10 % von 450 € sind 45 €, 8 % müssen etwas weniger sein.",
    {0: [(2, "die Rechnung in Zeile 2 für falsch gehalten, obwohl dort nur der Fehler aus Zeile 1 fortgeführt wird", "2 * 1")], 1: [(360, "mit 0,8 statt 0,08 gerechnet, wie in Zeile 1", "0.8 * 450"), (3600, "mit der Prozentzahl 8 malgenommen", "8 * 450"), (442, "die Prozentzahl 8 vom Preis abgezogen", "450 - 8")]}),
    form="fehler_detektiv", lp=LP, idee="fehler_komma")

neu(T, "grundwert", "sicherung", "begruenden", W(
    "Anna hat 30 € gespart, das sind 20 % ihres Sparziels. Ben hat 40 € gespart, das sind 25 % seines Sparziels. Welche Aussage über die Sparziele stimmt?",
    "Ben, denn sein Sparziel ist 160 € und Annas Sparziel ist 150 €.",
    [("Anna, denn ihr Sparziel ist 600 € und Bens Sparziel ist 160 €.", "20 % als Faktor 20 gelesen und mit den gesparten 30 € malgenommen"),
     ("Die Sparziele sind gleich groß, denn beide haben ungefähr gleich viel Prozent gespart.", "die beiden Prozentsätze für fast gleich gehalten und die verschiedenen gesparten Beträge nicht beachtet"),
     ("Anna, denn 20 % sind weniger als 25 %, und weniger Prozent bedeuten ein größeres Sparziel.", "die Prozentsätze verglichen, aber nicht bedacht, dass die gesparten Beträge verschieden sind")],
    "Annas Sparziel ist der Grundwert: 30 € sind 20 %, also 1 % = 1,50 € und 100 % = 150 €. Bens Sparziel: 40 € sind 25 %, also ist das Ziel 40 € : 0,25 = 160 €. Bens Ziel ist höher. Aus den Prozentsätzen allein lässt sich nichts schließen, weil auch die Beträge verschieden sind.",
    lambda: F(30) / F(1, 5) == 150 and F(40) / F(1, 4) == 160 and 160 > 150 and 30 * 20 == 600), lp=LP, idee="grundwerte_vergleichen")

neu(T, "grundwert", "sicherung", "darstellung", L(
    "7 % der Murmeln in einem Beutel sind 42 Murmeln. Dann sind 1 % genau □ Murmeln, und alle Murmeln im Beutel (100 %) sind □ Murmeln.",
    "1 % sind □ Murmeln, 100 % sind □ Murmeln", [6, 600], ["42 / 7", "42 / 7 * 100"], ["6", "42 * 100 / 7"],
    "Aus 7 % = 42 Murmeln folgt durch Teilen durch 7: 1 % = 6 Murmeln. Mit 100 malgenommen: 100 % = 600 Murmeln. Probe: 7 % von 600 sind 42.",
    {0: [(294, "mit 7 malgenommen statt durch 7 geteilt", "7 * 42"), (35, "7 von 42 abgezogen", "42 - 7")],
     1: [(4200, "42 mit 100 malgenommen, ohne vorher durch 7 zu teilen", "42 * 100"), (49, "die beiden Zahlen im Text addiert", "42 + 7")]}),
    form=None, lp=LP, idee="eins_prozent")


neu(T, "grundwert", "sicherung", "fehler", L(
    "Lena bestimmt, wie viele Mitglieder ein Verein hat, wenn 20 Mitglieder 25 % aller Mitglieder sind. Zeile 1: 20 Mitglieder sind 25 % aller Mitglieder. Zeile 2: Alle Mitglieder = 20 · 25 % = 20 · 0,25 = 5. Zeile 3: Der Verein hat also 5 Mitglieder. In welcher Zeile steckt der erste Fehler, und wie viele Mitglieder hat der Verein richtig?",
    "Fehler in Zeile □, richtig: □ Mitglieder", [2, 80], ["2", "20 / 0.25"], ["3 - 1", "20 * 4"],
    "Der Grundwert ist Prozentwert durch Prozentsatz, nicht mal: 20 : 0,25 = 80. Zeile 1 ist richtig. Zeile 2 multipliziert statt zu teilen. Zeile 3 übernimmt den Fehler; das Ergebnis 5 ist ein Warnzeichen, denn 20 Mitglieder können nicht Teil von nur 5 sein.",
    {0: [(3, "die Schlusszeile genannt, weil dort das unsinnige Ergebnis 5 steht", "3")], 1: [(5, "den Prozentwert mit dem Prozentsatz malgenommen, wie in Zeile 2", "20 * 0.25"), (500, "mit der Prozentzahl 25 malgenommen", "20 * 25"), (45, "die beiden Zahlen im Text addiert", "20 + 25")]}),
    form="fehler_detektiv", lp=LP, idee="fehler_multiplizieren")
