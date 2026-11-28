T = "bruch.prozent"
LP = "M6 3 Prozentrechnung (Prozentwert, Grundwert und Prozentsatz; Prozente verstehen)"
REGEL[(T, "prozentwert")] = REGEL[(T, "grundwert")] = REGEL[(T, "verstehen")] = "id.verhaeltnisse.prozent"
ABG[(T, "prozentwert")] = "Die Übungen berechnen einen Prozentwert mit einem Satz; hier müssen mehrere Prozentsätze auf verschiedene Ganze bezogen, Größenordnungen abgeschätzt oder eine Prozentangabe in eine andere Darstellung gebracht werden."
ABG[(T, "grundwert")] = "Die Übungen berechnen den Grundwert aus Prozentwert und Prozentsatz; hier wird der Grundwert für weitere Aussagen über dasselbe Ganze gebraucht, in Darstellungen gelesen oder mit anderen Grundwerten verglichen."
ABG[(T, "verstehen")] = "Die Übungen rechnen mit Prozenten; hier wird begründet, warum sich Prozentzahlen immer auf ein bestimmtes Ganzes beziehen und was sich ändert, wenn das Ganze wechselt."
# ───────── prozentwert ─────────
neu(T, "prozentwert", "test", "transfer", L(
    "In einer Schule sind 40 % der Kinder Jungen. 50 % der Jungen und 25 % der Mädchen fahren mit dem Rad, das sind zusammen 490 Kinder. Wie viele Kinder hat die Schule, und wie viele davon sind Mädchen?",
    "□ Kinder an der Schule, davon □ Mädchen", [1400, 840], ["490 / (0.4 * 0.5 + 0.6 * 0.25)", "490 / (0.4 * 0.5 + 0.6 * 0.25) * 0.6"], ["1400", "840"],
    "Man schätzt den Anteil der Radfahrer an allen Kindern: 50 % von 40 % sind 20 %, 25 % von 60 % sind 15 %, zusammen 35 % aller Kinder. 490 Kinder sind 35 %, also 1 % = 14 Kinder und 100 % = 1 400 Kinder. Mädchen sind 60 % von 1 400, das sind 840. Probe: 560 Jungen, davon 280 mit Rad, 840 Mädchen, davon 210 mit Rad, zusammen 490.",
    {0: [(980, "nur den Satz der Jungen (50 %) genommen: 490 : 0,5", "490 / 0.5"), (1960, "nur den Satz der Mädchen (25 %) genommen: 490 : 0,25", "490 / 0.25"), (700, "die beiden Sätze 50 % und 25 % nicht gewichtet, sondern den Gesamtanteil grob mit 0,7 geschätzt", "490 / 0.7")],
     1: [(560, "die Zahl der Jungen statt der Mädchen angegeben", "1400 * 0.4"), (350, "25 % von allen 1 400 Kindern als Mädchen genommen", "1400 * 0.25"), (980, "1 400 mit 0,7 malgenommen und den Anteil der Mädchen falsch bestimmt", "1400 * 0.7")]}),
    lp=LP, idee="mehrere_ganze")
neu(T, "prozentwert", "korrektur", "einkleidung", W(
    "Du sollst 16 % von 25 € berechnen. Kim rechnet 0,16 · 25 €. Ben rechnet stattdessen 25 % von 16 €. Welche Aussage über die beiden Rechenwege stimmt?",
    "Beide Wege geben denselben Betrag, denn in beiden Fällen wird 16 mit 25 malgenommen und durch 100 geteilt.",
    [("Die Wege geben verschiedene Beträge, denn Prozentsatz und Grundwert dürfen nicht vertauscht werden.", "geglaubt, Prozentsatz und Grundwert seien nicht vertauschbar, obwohl beim Malnehmen die Reihenfolge keine Rolle spielt"),
     ("Nur Kims Weg ist richtig, denn die 25 € sind der Grundwert und müssen dort stehen, wo der Prozentsatz steht.", "den Grundwert für unantastbar gehalten und nicht gesehen, dass das Produkt gleich bleibt"),
     ("Bens Weg gibt einen größeren Betrag, denn 25 % sind mehr als 16 %.", "nur die beiden Prozentsätze verglichen und die verschiedenen Grundwerte nicht beachtet")],
    "16 % von 25 € sind 0,16 · 25 € = 4 €. 25 % von 16 € sind ein Viertel von 16 €, das sind ebenfalls 4 €. Beide Rechnungen sind 16 · 25 : 100, nur in anderer Reihenfolge: Beim Malnehmen darf man die Faktoren vertauschen. Bens Weg ist im Kopf bequemer, weil ein Viertel leicht zu bilden ist.",
    lambda: F(16, 100) * 25 == F(25, 100) * 16 == 4 and F(25, 100) > F(16, 100)), form="zwei_wege", lp=LP, idee="kopfrechnen_zwei_wege")
neu(T, "prozentwert", "korrektur", "darstellung", Z(
    "Von 600 Kindern kommen 35 % mit dem Fahrrad zur Schule. Im Kreisdiagramm wird diese Gruppe als Sektor gezeichnet. Welchen Mittelpunktswinkel hat dieser Sektor (in Grad)?",
    126, "0.35 * 360", "35 * 360 / 100",
    "Der ganze Kreis hat 360° und steht für 100 % der Kinder. Der Sektor für 35 % hat also 35 % von 360° = 126°. Die Zahl 600 der Kinder wird für den Winkel nicht gebraucht, nur der Prozentsatz.",
    [B("0.35 * 600", "den Prozentwert in Kindern (210) als Winkel genommen"),
     B("35", "die Prozentzahl selbst als Winkel in Grad hingeschrieben"),
     B("360 / 100", "nur ein Prozent des Kreises berechnet und nicht mit der Prozentzahl malgenommen")], einheit="Grad"), lp=LP, idee="winkel_im_kreisdiagramm")
neu(T, "prozentwert", "korrektur", "umkehr", Z(
    "Ein Buch hat 280 Seiten. Lia liest am ersten Tag 15 % des ganzen Buchs. Am zweiten Tag liest sie weitere Seiten, danach hat sie noch 168 Seiten vor sich. Wie viel Prozent des ganzen Buchs liest sie am zweiten Tag?",
    25, "100 - 15 - 168 / 280 * 100", "(280 - 168) / 280 * 100 - 15",
    "Die 168 übrigen Seiten sind 168 : 280 = 0,6 = 60 % des Buchs. Gelesen sind also 100 % − 60 % = 40 %. Davon gehören 15 % zum ersten Tag, also bleiben 40 % − 15 % = 25 % für den zweiten Tag. Probe: 25 % von 280 sind 70 Seiten, 42 + 70 + 168 = 280.",
    [B("168 / 280 * 100", "den Anteil der noch ungelesenen Seiten als Antwort angegeben"),
     B("100 - 15", "nur den ersten Tag vom ganzen Buch abgezogen"),
     B("100 - 168 / 280 * 100", "den gesamten gelesenen Anteil angegeben statt nur den zweiten Tag")], einheit="%"), lp=LP, idee="rest_ueber_prozente")
neu(T, "prozentwert", "sicherung", "transfer", W(
    "Ohne genau zu rechnen: Welche Zahl ist ungefähr 51 % von 3 980?",
    "etwa 2 000",
    [("etwa 200", "das Komma um eine Stelle falsch gesetzt: etwa ein Zehntel des richtigen Werts"),
     ("etwa 20", "um zwei Stellen verrutscht: aus 51 % wurde 0,51 % gemacht"),
     ("etwa 20 000", "Komma um eine Stelle falsch: zehnmal so groß wie der richtige Wert")],
    "51 % sind etwas mehr als die Hälfte, und 3 980 ist ungefähr 4 000. Die Hälfte von 4 000 ist 2 000. Genau: 0,51 · 3 980 = 2 029,8. Die anderen Zahlen sind um Zehnerpotenzen daneben.",
    lambda: 1500 < F(51, 100) * 3980 < 2500 and all(not (1500 < x < 2500) for x in (200, 20, 20000))), lp=LP, idee="groessenordnung")
neu(T, "prozentwert", "sicherung", "fehler", L(
    "Max soll 8 % von 450 € berechnen und schreibt: Zeile 1: 8 % = 8/100 = 0,8. Zeile 2: 0,8 · 450 = 360. Zeile 3: Also sind 8 % von 450 € genau 360 €. In welcher Zeile steckt der erste Fehler, und wie viele Euro sind 8 % von 450 € richtig?",
    "Fehler in Zeile □, richtig: □ €", [1, 36], ["1", "0.08 * 450"], ["2 - 1", "450 * 8 / 100"],
    "Zeile 1 ist falsch: 8/100 ist 0,08 und nicht 0,8 (0,8 wären 80 %). Zeile 2 ist als Rechnung richtig (0,8 · 450 = 360), übernimmt aber den Fehler. Richtig: 0,08 · 450 € = 36 €. Probe: 10 % von 450 € sind 45 €, 8 % müssen etwas weniger sein.",
    {0: [(2, "die Rechnung in Zeile 2 für falsch gehalten, obwohl dort nur der Fehler aus Zeile 1 fortgeführt wird", "2 * 1")], 1: [(360, "mit 0,8 statt 0,08 gerechnet, wie in Zeile 1", "0.8 * 450"), (3600, "mit der Prozentzahl 8 malgenommen", "8 * 450"), (442, "die Prozentzahl 8 vom Preis abgezogen", "450 - 8")]}),
    form="fehler_detektiv", lp=LP, idee="fehler_komma")
neu(T, "prozentwert", "sicherung", "mehrschritt", W(
    "In einer Gruppe von 240 Kindern lesen 3/5 gern. In einer anderen Gruppe von 300 Kindern lesen 65 % gern. Welche Aussage über die Anteile stimmt?",
    "In der zweiten Gruppe lesen anteilig mehr Kinder gern, denn 3/5 sind 60 % und 65 % ist mehr.",
    [("In der ersten Gruppe lesen anteilig mehr Kinder gern, denn 3/5 sind 75 %.", "den Bruch 3/5 falsch in Prozent umgewandelt"),
     ("Die Anteile lassen sich nicht vergleichen, denn die beiden Gruppen sind verschieden groß.", "geglaubt, Anteile könne man nur bei gleich großen Gruppen vergleichen"),
     ("Die Anteile sind gleich, denn 3/5 und 65 % sind beides Angaben für „etwas mehr als die Hälfte“.", "zwei verschiedene Anteile für gleich gehalten, weil sie ungefähr zusammenpassen")],
    "3/5 = 0,6 = 60 %. In der zweiten Gruppe sind es 65 %, also ein größerer Anteil. Anteile in Bruch- und Prozentschreibweise vergleicht man, indem man beide in dieselbe Schreibweise bringt; die Größe der Gruppen spielt dafür keine Rolle. Zur Probe: 60 % von 240 sind 144 Kinder, 65 % von 300 sind 195 Kinder.",
    lambda: F(3, 5) == F(60, 100) and F(65, 100) > F(3, 5) and F(3, 5) != F(75, 100)), form="bruecke", lp=LP, idee="bruch_prozent_wert")
# ───────── grundwert ─────────
neu(T, "grundwert", "test", "transfer", Z(
    "Im Schulbus fahren 18 Kinder, das sind 45 % aller Kinder einer Jahrgangsstufe. 30 % aller Kinder dieser Jahrgangsstufe kommen zu Fuß, alle anderen fahren mit dem Rad. Wie viele Kinder fahren mit dem Rad?",
    10, "18 / 0.45 * (1 - 0.45 - 0.3)", "18 / 0.45 * 0.25",
    "Alle Angaben beziehen sich auf dasselbe Ganze, die ganze Jahrgangsstufe. Aus 18 = 45 % folgt: 1 % sind 0,4 Kinder, also sind es 40 Kinder. Mit dem Rad fahren 100 % − 45 % − 30 % = 25 % von 40 Kindern, das sind 10 Kinder. Probe: 18 + 12 + 10 = 40.",
    [B("18 / 0.45 * 0.3", "nur die Kinder gezählt, die zu Fuß kommen (30 % von allen)"),
     B("18 / 0.45 - 18", "die Jahrgangsstufe minus die Busfahrer gerechnet, also alle Kinder, die nicht mit dem Bus fahren"),
     B("0.25 * 18", "25 % von den 18 Kindern im Bus genommen, obwohl sich die Prozente auf alle Kinder beziehen")], einheit="Kinder"),
    lp=LP, idee="gemeinsames_ganzes")
neu(T, "grundwert", "korrektur", "umkehr", W(
    "Kim sagt: „Der Grundwert ist immer die größte Zahl in einer Prozentaufgabe.“ Welches Beispiel zeigt, dass Kim irrt?",
    "Ein Preis steigt um 25 % auf 15 €: Der Grundwert ist der alte Preis mit 12 € und damit kleiner als der neue Preis.",
    [("Von 80 Kindern fahren 20 % mit dem Bus: Der Grundwert ist 80 und damit größer als die 16 Busfahrer.", "ein Beispiel gewählt, in dem der Grundwert tatsächlich der größte Wert ist"),
     ("Ein Pullover kostet nach 10 % Rabatt noch 45 €: Der Grundwert ist 50 € und damit größer als 45 €.", "ein Beispiel mit Rabatt gewählt, bei dem der Grundwert wirklich größer ist als der Prozentwert"),
     ("Bei 30 % von 200 € ist der Grundwert 200 € und damit größer als der Prozentwert 60 €.", "ein Beispiel mit Prozentsatz unter 100 % gewählt, das Kim bestätigt statt widerlegt")],
    "Der Grundwert ist die Größe, auf die sich der Prozentsatz bezieht. Bei einer Erhöhung steht der alte Preis für 100 %, der neue für 125 %. Hier ist 15 € = 125 % von 12 €: Der Grundwert 12 € ist kleiner als der neue Preis 15 €. In den anderen Beispielen ist der Grundwert zufällig der größte Wert, das widerlegt Kim nicht.",
    lambda: F(12) * F(125, 100) == 15 and 12 < 15 and F(80) * F(20, 100) == 16 and F(50) * F(90, 100) == 45 and F(200) * F(30, 100) == 60), lp=LP, idee="grundwert_direkt")
neu(T, "grundwert", "korrektur", "darstellung", Z(
    "In einem Kreisdiagramm gehört zum Sektor „Fußweg“ der Mittelpunktswinkel 54°. Diesem Sektor entsprechen 63 Kinder. Wie viele Kinder wurden insgesamt befragt?",
    420, "63 / (54 / 360)", "63 * 360 / 54",
    "Der volle Kreis hat 360°, der Sektor 54° ist 54 : 360 = 0,15 = 15 % des Kreises. 63 Kinder sind also 15 % aller Kinder. 1 % sind 4,2 Kinder, 100 % sind 420 Kinder.",
    [B("63 * 54 / 360", "15 % von 63 berechnet, obwohl 63 schon der Teil ist"),
     B("63 * 54", "die Kinderzahl mit dem Winkel malgenommen"),
     B("63 + 360 - 54", "die Zahlen aus dem Text gemischt addiert und subtrahiert")], einheit="Kinder"), lp=LP, idee="winkel_zurueck")
neu(T, "grundwert", "korrektur", "umkehr", Z(
    "Ben spart für ein Fahrrad. Ihm fehlen noch 105 €, das sind 70 % des Preises. Wie viel Euro hat er schon gespart?",
    45, "105 / 0.7 - 105", "105 / 70 * 30",
    "Die fehlenden 105 € sind 70 % des Preises, also ist der Preis 105 € : 0,7 = 150 €. Gespart hat Ben 150 € − 105 € = 45 €. Probe: 45 € sind 30 % von 150 €.",
    [B("105 / 0.7", "den Preis (150 €) als gesparten Betrag angegeben"),
     B("105 * 0.3", "30 % von den fehlenden 105 € genommen statt vom Preis"),
     B("105 / 0.7 - 70", "von dem Preis die Prozentzahl 70 abgezogen statt die fehlenden 105 €")], einheit="€"), lp=LP, idee="fehlbetrag")
neu(T, "grundwert", "sicherung", "begruenden", W(
    "Anna hat 30 € gespart, das sind 20 % ihres Sparziels. Ben hat 40 € gespart, das sind 25 % seines Sparziels. Welche Aussage über die Sparziele stimmt?",
    "Ben, denn sein Sparziel ist 160 € und Annas Sparziel ist 150 €.",
    [("Anna, denn ihr Sparziel ist 600 € und Bens Sparziel ist 160 €.", "20 % als Faktor 20 gelesen und mit den gesparten 30 € malgenommen"),
     ("Die Sparziele sind gleich groß, denn beide haben ungefähr gleich viel Prozent gespart.", "die beiden Prozentsätze für fast gleich gehalten und die verschiedenen gesparten Beträge nicht beachtet"),
     ("Anna, denn 20 % sind weniger als 25 %, und weniger Prozent bedeuten ein größeres Sparziel.", "die Prozentsätze verglichen, aber nicht bedacht, dass die gesparten Beträge verschieden sind")],
    "Annas Sparziel ist der Grundwert: 30 € sind 20 %, also 1 % = 1,50 € und 100 % = 150 €. Bens Sparziel: 40 € sind 25 %, also ist das Ziel 40 € : 0,25 = 160 €. Bens Ziel ist höher. Aus den Prozentsätzen allein lässt sich nichts schließen, weil auch die Beträge verschieden sind.",
    lambda: F(30) / F(1, 5) == 150 and F(40) / F(1, 4) == 160 and 160 > 150 and 30 * 20 == 600), lp=LP, idee="grundwerte_vergleichen")
neu(T, "grundwert", "sicherung", "fehler", L(
    "Lena bestimmt, wie viele Mitglieder ein Verein hat, wenn 20 Mitglieder 25 % aller Mitglieder sind. Zeile 1: 20 Mitglieder sind 25 % aller Mitglieder. Zeile 2: Alle Mitglieder = 20 · 25 % = 20 · 0,25 = 5. Zeile 3: Der Verein hat also 5 Mitglieder. In welcher Zeile steckt der erste Fehler, und wie viele Mitglieder hat der Verein richtig?",
    "Fehler in Zeile □, richtig: □ Mitglieder", [2, 80], ["2", "20 / 0.25"], ["3 - 1", "20 * 4"],
    "Der Grundwert ist Prozentwert durch Prozentsatz, nicht mal: 20 : 0,25 = 80. Zeile 1 ist richtig. Zeile 2 multipliziert statt zu teilen. Zeile 3 übernimmt den Fehler; das Ergebnis 5 ist ein Warnzeichen, denn 20 Mitglieder können nicht Teil von nur 5 sein.",
    {0: [(3, "die Schlusszeile genannt, weil dort das unsinnige Ergebnis 5 steht", "3")], 1: [(5, "den Prozentwert mit dem Prozentsatz malgenommen, wie in Zeile 2", "20 * 0.25"), (500, "mit der Prozentzahl 25 malgenommen", "20 * 25"), (45, "die beiden Zahlen im Text addiert", "20 + 25")]}),
    form="fehler_detektiv", lp=LP, idee="fehler_multiplizieren")
neu(T, "grundwert", "sicherung", "darstellung", L(
    "7 % der Murmeln in einem Beutel sind 42 Murmeln. Dann sind 1 % genau □ Murmeln, und alle Murmeln im Beutel (100 %) sind □ Murmeln.",
    "1 % sind □ Murmeln, 100 % sind □ Murmeln", [6, 600], ["42 / 7", "42 / 7 * 100"], ["6", "42 * 100 / 7"],
    "Aus 7 % = 42 Murmeln folgt durch Teilen durch 7: 1 % = 6 Murmeln. Mit 100 malgenommen: 100 % = 600 Murmeln. Probe: 7 % von 600 sind 42.",
    {0: [(294, "mit 7 malgenommen statt durch 7 geteilt", "7 * 42"), (35, "7 von 42 abgezogen", "42 - 7")],
     1: [(4200, "42 mit 100 malgenommen, ohne vorher durch 7 zu teilen", "42 * 100"), (49, "die beiden Zahlen im Text addiert", "42 + 7")]}),
    form=None, lp=LP, idee="eins_prozent")
# ───────── verstehen ─────────
neu(T, "verstehen", "test", "transfer", L(
    "In einem Dorf sind 40 % der Einwohner Kinder. Von den Kindern sind 30 % im Sportverein. Im Sportverein sind 60 Kinder. Wie viele Einwohner hat das Dorf, und wie viele Kinder wohnen dort?",
    "□ Einwohner im Dorf, davon □ Kinder", [500, 200], ["60 / (0.4 * 0.3)", "60 / 0.3"], ["500", "200"],
    "Die 30 % beziehen sich nur auf die Kinder. 60 Kinder im Verein sind 30 % aller Kinder, also gibt es 60 : 0,3 = 200 Kinder. Diese 200 Kinder sind 40 % aller Einwohner, also hat das Dorf 200 : 0,4 = 500 Einwohner. Kürzer: 30 % von 40 % sind 12 %, und 60 : 0,12 = 500.",
    {0: [(150, "die 60 Kinder als 40 % gedeutet: 60 : 0,4", "60 / 0.4"), (200, "nur die Kinderzahl bestimmt und als Einwohnerzahl angegeben", "60 / 0.3"), (1500, "die 60 Kinder als einen viel zu kleinen Prozentsatz der Einwohner gedeutet, das Komma verrutscht", "60 / 0.04")],
     1: [(60, "die Zahl der Kinder im Verein als Zahl aller Kinder angegeben", "60"), (150, "40 % von 375 genommen, den Grundwert falsch bestimmt", "0.4 * 375"), (300, "60 : 0,2 gerechnet, die beiden Prozentzahlen 40 und 30 verwechselt", "60 / 0.2")]}),
    lp=LP, idee="anteil_von_anteil")
neu(T, "verstehen", "korrektur", "einkleidung", Z(
    "Der Eintritt für ein Schwimmbad kostete 30 €. Nach dem Umbau steigt der Preis um 200 %. Wie viel Euro kostet der Eintritt danach?",
    90, "30 + 30 * 200 / 100", "30 * 3",
    "200 % von 30 € sind 2 · 30 € = 60 €. Der Preis steigt um 60 €, also kostet der Eintritt danach 30 € + 60 € = 90 €. Das ist das Dreifache (300 % des alten Preises). „Um 200 % steigen“ heißt nicht „auf 200 % steigen“.",
    [B("2 * 30", "„um 200 % steigen“ als „auf 200 % steigen“ gelesen: nur 2 · 30"),
     B("30 + 200", "die 200 % als 200 € gelesen und zum alten Preis addiert"),
     B("30 * 200", "mit der Prozentzahl 200 malgenommen, ohne sie in einen Anteil umzuwandeln")], einheit="€"), form="bruecke", lp=LP, idee="um_oder_auf")
neu(T, "verstehen", "korrektur", "darstellung", W(
    "Welche dieser vier Angaben beschreibt den größten Anteil?",
    "3/8 der Kinder",
    [("0,36 der Kinder", "als Prozentzahl 36 % gelesen und für größer gehalten als 37,5 %: Der Bruch 3/8 wurde nicht umgewandelt"),
     ("37 % der Kinder", "die Prozentzahl 37 für die größte gehalten, ohne 3/8 als 37,5 % zu erkennen"),
     ("7/20 der Kinder", "den Bruch mit der größeren Zahl 20 im Nenner für den größten gehalten")],
    "Alle Angaben als Prozent: 3/8 = 0,375 = 37,5 %; 0,36 = 36 %; 37 %; 7/20 = 35 %. Der größte Anteil ist 37,5 %, also 3/8. Schon 3/8 und 37 % liegen nur 0,5 Prozentpunkte auseinander.",
    lambda: F(3, 8) > F(37, 100) > F("0.36") > F(7, 20)), lp=LP, idee="darstellungen_vergleichen")
neu(T, "verstehen", "korrektur", "umkehr", Z(
    "Eine Sonnenblume ist heute 150 % so hoch wie vor einem Monat und misst 54 cm. Wie hoch war sie vor einem Monat?",
    36, "54 / 1.5", "54 * 100 / 150",
    "Vor einem Monat war die Sonnenblume das Ganze, also 100 %. Heute sind es 150 %, das ist das Eineinhalbfache. 150 % sind 54 cm, also 50 % sind 18 cm und 100 % sind 36 cm. Probe: 150 % von 36 cm sind 54 cm.",
    [B("54 / 1.5 / 2", "nach dem Teilen noch durch 2 geteilt, weil 150 % als anderthalbfach und zugleich als Hälfte gelesen wurde"),
     B("54 - 54 * 0.5", "50 % von der heutigen Höhe abgezogen statt vom alten Wert"),
     B("54 * 1.5", "die heutige Höhe mit 1,5 malgenommen, statt durch 1,5 zu teilen")], einheit="cm"), form="umkehren", lp=LP, idee="ganzes_aendert_sich")
neu(T, "verstehen", "sicherung", "fehler", L(
    "Zwei Klassen vergleichen die Hausaufgaben. Zeile 1: Klasse A hat 8 Kinder, Klasse B hat 30 Kinder. In A haben 75 % der Kinder die Hausaufgabe gemacht, in B nur 40 %. Zeile 2: 75 % sind mehr als 40 %, also ist der Anteil in A größer. Zeile 3: Also haben in A mehr Kinder die Hausaufgabe gemacht als in B. In welcher Zeile steckt der erste Fehler, und wie viele Kinder haben in B mehr die Hausaufgabe gemacht als in A?",
    "Fehler in Zeile □, Unterschied: □ Kinder", [3, 6], ["3", "0.4 * 30 - 0.75 * 8"], ["4 - 1", "12 - 6"],
    "Prozentzahlen vergleichen Anteile, nicht Anzahlen. Zeile 1 und 2 sind richtig. Zeile 3 ist falsch: In A haben 75 % von 8 = 6 Kinder die Hausaufgabe gemacht, in B 40 % von 30 = 12 Kinder. In B sind es also 12 − 6 = 6 Kinder mehr, obwohl der Anteil dort kleiner ist.",
    {0: [(2, "den Vergleich der Prozentzahlen in Zeile 2 für falsch gehalten", "1 + 1")], 1: [(-6, "die Differenz andersherum gebildet: A minus B", "0.75 * 8 - 0.4 * 30"), (12, "nur die Kinder aus Klasse B gezählt", "0.4 * 30"), (35, "den Unterschied der Prozentzahlen als Kinderzahl gelesen", "75 - 40")]}),
    form="fehler_detektiv", lp=LP, idee="anzahl_oder_anteil")
neu(T, "verstehen", "sicherung", "begruenden", W(
    "Bei Verein A sind 20 % der Mitglieder mehr Personen als 30 % der Mitglieder von Verein B. Welche Aussage über die Mitgliederzahlen folgt sicher?",
    "Verein A hat mehr als anderthalbmal so viele Mitglieder wie Verein B, denn 20 % von A sind mehr als 30 % von B.",
    [("Verein A hat weniger Mitglieder als Verein B, denn 20 % sind weniger als 30 %.", "die Prozentzahlen verglichen und vergessen, dass sie sich auf verschiedene Ganze beziehen"),
     ("Verein A hat genau doppelt so viele Mitglieder wie Verein B, denn 20 % von A sind mehr als 30 % von B.", "aus der Ungleichung einen genauen Wert gemacht; es folgt nur, dass A mehr als anderthalbmal so groß ist"),
     ("Verein A hat genau anderthalbmal so viele Mitglieder wie Verein B, denn 20 % von A sind mehr als 30 % von B.", "das Verhältnis 30 : 20 als genauen Wert genommen, obwohl der Vergleich nur mehr als sagt")],
    "Es gilt 0,2 · A > 0,3 · B. Teilt man durch 0,2, folgt A > 1,5 · B. A ist also mehr als anderthalbmal so groß wie B; ein genauer Wert folgt nicht. Beispiel: B = 100 Mitglieder, dann muss A größer als 150 sein.",
    lambda: F(3, 10) / F(2, 10) == F(3, 2) and all(F(2, 10) * a > F(3, 10) * 100 for a in (151, 200, 400)) and not (F(2, 10) * 150 > F(3, 10) * 100)), lp=LP, idee="ganze_verschieden")
neu(T, "verstehen", "sicherung", "umkehr", Z(
    "Ben isst 20 % eines Kuchens. Ida isst ein Viertel des Rests. Danach bleiben 18 Stücke übrig. Aus wie vielen Stücken bestand der ganze Kuchen?",
    30, "18 / (1 - 0.2 - (1 - 0.2) / 4)", "18 / 0.6",
    "Ben isst 20 %, es bleiben 80 %. Ida isst ein Viertel von diesen 80 %, das sind 20 % des ganzen Kuchens. Es bleiben 80 % − 20 % = 60 %. Diese 60 % sind 18 Stücke, also 100 % = 18 : 0,6 = 30 Stücke. Das Viertel gehört zum Rest und nicht zum ganzen Kuchen.",
    [B("18 / 0.4", "Bens und Idas Stücke zusammen als die verbleibenden Stücke gedeutet"),
     B("18 / 0.8", "Idas Stück vergessen und nur Bens Stück berücksichtigt"),
     B("18 / 0.2", "nur Bens Anteil als die gegebenen 18 Stücke gedeutet")], einheit="Stücke"), lp=LP, idee="anteil_vom_rest")
