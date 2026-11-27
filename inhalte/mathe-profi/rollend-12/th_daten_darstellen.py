T = "daten.darstellen"

# ───────── absolute_haeufigkeit ─────────
neu(T, "absolute_haeufigkeit", "umkehren", Z(
    "Bei einer Umfrage unter 30 Kindern nannten 12 Kinder Fußball und 8 Kinder Schwimmen als Lieblingssport. Alle übrigen Kinder nannten Tanzen. Wie oft wurde Tanzen genannt?",
    10, "30 - 12 - 8", "30 - (12 + 8)", "Wie viele Kinder haben schon etwas anderes genannt? Was bleibt von allen Befragten übrig?",
    "Fußball und Schwimmen zusammen: 12 + 8 = 20 Nennungen. Von 30 Kindern bleiben 30 − 20 = 10 für Tanzen. Probe: 12 + 8 + 10 = 30.",
    [(20, None, "nur Fußball und Schwimmen zusammengezählt", "12 + 8"), (18, None, "nur die Nennungen für Fußball von 30 abgezogen", "30 - 12"), (50, None, "alle Zahlen addiert", "30 + 12 + 8")], "Nennungen"), g="umkehr")
neu(T, "absolute_haeufigkeit", "anwenden", Z(
    "Ein Kiosk zählt, wie viele Eis er von Montag bis Freitag verkauft: Montag 12, Dienstag 15, Mittwoch 9, Donnerstag 18, Freitag 21. Am Wochenende (Samstag und Sonntag zusammen) verkauft er ein Drittel so viele Eis wie von Montag bis Freitag zusammen. Wie viele Eis verkauft er in der ganzen Woche?",
    100, "(12 + 15 + 9 + 18 + 21) + (12 + 15 + 9 + 18 + 21) / 3", "75 + 25", "Wie viele Eis wurden von Montag bis Freitag verkauft? Worauf bezieht sich das Drittel?",
    "Montag bis Freitag: 12 + 15 + 9 + 18 + 21 = 75 Eis. Ein Drittel davon: 75 : 3 = 25 Eis am Wochenende. Insgesamt 75 + 25 = 100 Eis.",
    [(75, None, "das Wochenende vergessen", "12 + 15 + 9 + 18 + 21"), (25, None, "nur das Wochenende genannt", "75 / 3"), (300, None, "das Wochenende dreimal so groß statt ein Drittel gerechnet: 75 + 3 · 75", "75 + 75 * 3")], "Eis"), g="transfer")

# ───────── relative_haeufigkeit ─────────
neu(T, "relative_haeufigkeit", "zwei_wege", Z(
    "Weg A: Erweitere den Bruch 18/25 auf den Nenner 100. Weg B: Rechne 18 : 25 und schreibe das Ergebnis in Prozent. Gib 18 von 25 als Prozentzahl an.",
    72, "18 * 4", "18 / 25 * 100", "Mit welcher Zahl musst du 25 malnehmen, um 100 zu erhalten?",
    "Weg A: 25 · 4 = 100, also 18 · 4 = 72 und 18/25 = 72/100 = 72 %. Weg B: 18 : 25 = 0,72 und 0,72 = 72 %.",
    [(18, None, "den Zähler als Prozentzahl genommen", "18"), (0.72, None, "das Ergebnis der Division nicht in Prozent umgerechnet", "18 / 25"), (43, None, "Zähler und Nenner addiert", "18 + 25")], "%"))
neu(T, "relative_haeufigkeit", "anwenden", Z(
    "An einer Schule lernen 400 Kinder. 30 % davon sind Fahrschüler. Die Hälfte der Fahrschüler kommt mit dem Bus. Wie viele Kinder kommen mit dem Bus?",
    60, "400 * 30 / 100 / 2", "400 * 15 / 100", "Berechne zuerst, wie viele Kinder Fahrschüler sind.",
    "30 % von 400 sind 400 : 100 · 30 = 120 Fahrschüler. Die Hälfte davon: 120 : 2 = 60 Kinder.",
    [(120, None, "alle Fahrschüler genannt", "400 * 30 / 100"), (200, None, "die Hälfte aller Kinder genommen", "400 / 2"), (15, None, "die Prozentzahl halbiert", "30 / 2")], "Kinder"), g="transfer")

# ───────── tabelle_auswerten ─────────
neu(T, "tabelle_auswerten", "zwei_wege", Z(
    "Die Tabelle zeigt eine Umfrage zum Lieblingssport. Weg A: Addiere die Anzahlen aller anderen Sportarten. Weg B: Berechne zuerst, wie viele Kinder insgesamt befragt wurden, und ziehe dann die Anzahl für Fußball ab. Wie viele Kinder haben nicht „Fußball“ gewählt?",
    17, "6 + 4 + 7", "(11 + 6 + 4 + 7) - 11", "Welche Zeilen der Tabelle zählen zu „nicht Fußball“?",
    "Weg A: Schwimmen 6 + Tennis 4 + Tanzen 7 = 17. Weg B: Insgesamt 11 + 6 + 4 + 7 = 28 Kinder. 28 − 11 = 17.",
    [(11, None, "nur die Fußball-Kinder genannt", "11"), (28, None, "alle befragten Kinder genannt", "11 + 6 + 4 + 7"), (10, None, "nur Schwimmen und Tennis addiert", "6 + 4")], "Kinder",
    grafik=TAB(["Sportart", "Anzahl Kinder"], ["Fußball", "11"], ["Schwimmen", "6"], ["Tennis", "4"], ["Tanzen", "7"])))
neu(T, "tabelle_auswerten", "anwenden", Z(
    "Die Tabelle zeigt, wie viele Eis ein Kiosk an vier Tagen verkauft hat. Ein Eis kostet 2 €. Wie viel Euro hat der Kiosk an den zwei Tagen mit den meisten verkauften Eis zusammen eingenommen?",
    152, "(41 + 35) * 2", "41 * 2 + 35 * 2", "Finde die beiden Tage mit den meisten Eis. Wie viele Eis sind das zusammen?",
    "Die meisten Eis gab es am Mittwoch (41) und am Montag (35). Zusammen 41 + 35 = 76 Eis. 76 · 2 € = 152 €.",
    [(82, None, "nur den besten Tag gerechnet", "41 * 2"), (76, None, "die Zahl der Eis genannt, nicht den Preis", "41 + 35"), (148, None, "Mittwoch und Donnerstag genommen", "(41 + 33) * 2")], "€",
    grafik=TAB(["Tag", "Verkaufte Eis"], ["Montag", "35"], ["Dienstag", "28"], ["Mittwoch", "41"], ["Donnerstag", "33"])), g="transfer")

# ───────── saeulendiagramm ─────────
neu(T, "saeulendiagramm", "bruecke", Z(
    "Das Säulendiagramm zeigt, wie viele Kinder in vier Klassen eine Brezel bestellt haben. Eine Brezel kostet 70 Cent. Wie viel Euro kosten alle bestellten Brezeln?",
    35, "(14 + 11 + 9 + 16) * 70 / 100", "50 * 0.7", "Lies die vier Säulen ab und zähle sie zusammen. Wie viele Brezeln sind das?",
    "Bestellt wurden 14 + 11 + 9 + 16 = 50 Brezeln. 50 · 70 Cent = 3 500 Cent = 35 €.",
    [(50, None, "die Zahl der Brezeln als Preis genannt", "14 + 11 + 9 + 16"), (3500, None, "in Cent statt in Euro angegeben", "50 * 70"), (3.5, None, "durch 1 000 statt durch 100 geteilt", "50 * 70 / 1000")], "€",
    grafik={"typ": "saeulen", "werte": [{"name": "5a", "wert": 14}, {"name": "5b", "wert": 11}, {"name": "5c", "wert": 9}, {"name": "5d", "wert": 16}]}))
neu(T, "saeulendiagramm", "umkehren", Z(
    "Ein Säulendiagramm zeigt vier Klassen. Die ersten drei Säulen sind 12, 7 und 15 Kinder hoch, die vierte Säule ist verdeckt. Insgesamt wurden 50 Kinder befragt. Wie hoch ist die verdeckte Säule?",
    16, "50 - (12 + 7 + 15)", "50 - 12 - 7 - 15", "Wie viele Kinder zeigen die drei sichtbaren Säulen zusammen? Wie viele fehlen bis 50?",
    "Die drei sichtbaren Säulen zeigen 12 + 7 + 15 = 34 Kinder. Es fehlen 50 − 34 = 16 Kinder. Die verdeckte Säule ist 16 hoch.",
    [(34, None, "die Summe der sichtbaren Säulen genannt", "12 + 7 + 15"), (84, None, "alle Zahlen addiert", "50 + 12 + 7 + 15")], "Kinder"), g="rueckwaerts")

# ───────── kreisdiagramm ─────────
neu(T, "kreisdiagramm", "bruecke", Z(
    "Die Tabelle zeigt, welchen Anteil vier Sportarten bei einer Umfrage haben. Daraus wird ein Kreisdiagramm gezeichnet. Wie groß ist der Winkel des Sektors „Schwimmen“?",
    36, "360 / 100 * 10", "360 * 10 / 100", "Ein ganzer Kreis hat 360°. Wie viel Grad entsprechen 1 %?",
    "1 % entspricht 360° : 100 = 3,6°. Für 10 % ist der Winkel 10 · 3,6° = 36°.",
    [(10, None, "die Prozentzahl als Winkel genommen", "10"), (3.6, None, "nur 1 % berechnet", "360 / 100"), (90, None, "den Winkel für Fußball (25 %) genannt", "360 / 100 * 25")], "°",
    grafik=TAB(["Sportart", "Anteil"], ["Fußball", "25 %"], ["Schwimmen", "10 %"], ["Tanzen", "40 %"], ["Sonstige", "25 %"])))
neu(T, "kreisdiagramm", "umkehren", Z(
    "Im Kreisdiagramm einer Umfrage hat ein Sektor den Winkel 72°. Insgesamt wurden 60 Personen befragt. Wie viele Personen gehören zu diesem Sektor?",
    12, "72 / 360 * 60", "60 / 5", "Welcher Bruchteil des ganzen Kreises sind 72°?",
    "72° von 360° sind 72/360 = 1/5 des Kreises. Ein Fünftel von 60 Personen sind 60 : 5 = 12 Personen.",
    [(20, None, "den Anteil in Prozent angegeben (20 %)", "72 / 360 * 100"), (72, None, "den Winkel als Personenzahl genommen", "72"), (300, None, "60 · 5 gerechnet", "60 * 5")], "Personen"), g="rueckwaerts")

# ───────── irrefuehrend ─────────
neu(T, "irrefuehrend", "umkehren", Z(
    "Die Hochachse eines Säulendiagramms beginnt bei 500. Die erste Säule steht für 520 und ist 2 cm hoch gezeichnet. Die zweite Säule wirkt 3-mal so hoch wie die erste. Für welchen Wert steht die zweite Säule?",
    560, "500 + 3 * (520 - 500)", "500 + 60", "Welcher Zuwachs über 500 gehört zu 2 cm? Was bedeutet 3-mal so hoch?",
    "2 cm stehen für 520 − 500 = 20. Die zweite Säule ist 3 · 2 cm = 6 cm hoch, das sind 3 · 20 = 60 über 500. Wert: 500 + 60 = 560.",
    [(1560, None, "den Wert der ersten Säule mit 3 malgenommen", "520 * 3"), (580, None, "60 zum Wert der ersten Säule addiert", "520 + 60"), (60, None, "nur den Zuwachs über der Achse genannt", "3 * 20")]), g="umkehr")
neu(T, "irrefuehrend", "anwenden", Z(
    "Eine Firma zeigt ein Säulendiagramm, dessen Hochachse bei 8 000 € beginnt. Der Umsatz 2024 war 8 400 €, der Umsatz 2025 war 9 200 €. Wie oft so hoch wie die Säule für 2024 wirkt die Säule für 2025?",
    3, "(9200 - 8000) / (8400 - 8000)", "1200 / 400", "Die Achse beginnt nicht bei null. Wie hoch sind die Säulen über 8 000 gezeichnet?",
    "Über der Achsenmarke 8 000 ragen die Säulen 400 und 1 200 hinaus. 1 200 : 400 = 3. Die zweite Säule wirkt 3-mal so hoch, obwohl der Umsatz nur um etwa 10 % gestiegen ist.",
    [(1.1, None, "das echte Verhältnis der Umsätze genannt, gerundet auf eine Stelle", "9200 / 8400"), (800, None, "den Unterschied der Umsätze in € genannt", "9200 - 8400"), (2, None, "800 : 400 gerechnet", "(9200 - 8400) / 400")]), g="transfer")
