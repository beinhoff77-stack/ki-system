T = "stochastik.grundbegriffe"
# ───────── begriffe ─────────
neu(T, "begriffe", "lueckenweg", L(
    "In einer Urne liegen 6 rote, 2 blaue, 5 grüne und 1 gelbe Kugel. Man zieht eine Kugel und notiert die Farbe. Der Ergebnisraum hat ① Ergebnisse. Zum Ereignis „rot oder blau“ gehören ② Kugeln. In der Urne liegen insgesamt ③ Kugeln.",
    KOMM(3), [4, 8, 14], ["4", "6 + 2", "6 + 2 + 5 + 1"], ["4", "8", "14"], "Die Ergebnisse sind die Farben. Das Ereignis fasst Ergebnisse zusammen, gezählt werden aber die Kugeln.",
    "Vier Farben, also vier Ergebnisse. Rot oder blau: 6 + 2 = 8 Kugeln. Insgesamt 6 + 2 + 5 + 1 = 14 Kugeln.",
    {0: [(14, None, "die Kugeln statt der Farben gezählt")], 1: [(2, None, "nur die Farbe blau betrachtet"), (11, None, "rot und grün genommen")]}), regel="id.daten.anteil")
neu(T, "begriffe", "umkehren", Z(
    "Ein Würfel hat die Zahlen 1 bis 12. Das Ereignis „Die Zahl ist ein Vielfaches von k“ hat genau 4 Ergebnisse. Dabei ist k eine Zahl größer als 1. Welche Zahl ist k?",
    3, 3, 3, "Zähle für k = 2, 3, 4 … wie viele Vielfache es zwischen 1 und 12 gibt.",
    "Vielfache von 3: 3, 6, 9, 12. Das sind genau 4. Bei k = 2 sind es 6, bei k = 4 nur 3 Vielfache.",
    [(4, None, "die Anzahl der Ergebnisse statt k genannt"), (2, None, "bei k = 2 gibt es 6 Vielfache"), (6, None, "bei k = 6 gibt es nur 2 Vielfache")]), g="umkehr", regel="id.daten.anteil")
assert [m for m in range(1, 13) if m % 3 == 0] == [3, 6, 9, 12] and all(len([m for m in range(1, 13) if m % k == 0]) != 4 for k in range(2, 13) if k != 3)
neu(T, "begriffe", "anwenden", Z(
    "Ein Glücksrad hat 8 gleich große Felder mit den Zahlen 1 bis 8. Wie viele Ergebnisse gehören zum Ereignis „Die Zahl ist durch 3 oder durch 4 teilbar“?",
    4, "2 + 2", 4, "Gehe die Zahlen 1 bis 8 der Reihe nach durch. Eine Zahl zählt nur einmal.",
    "Durch 3 teilbar: 3 und 6. Durch 4 teilbar: 4 und 8. Zusammen 4 Ergebnisse: {3; 4; 6; 8}.",
    [(2, None, "nur die durch 3 teilbaren Zahlen gezählt"), (8, None, "alle Felder gezählt"), (5, None, "die Zahl 12 oder 1 mitgezählt")], "Ergebnisse"), g="einkleidung", regel="id.daten.anteil")
assert [m for m in range(1, 9) if m % 3 == 0 or m % 4 == 0] == [3, 4, 6, 8]

# ───────── rel_haeufigkeit ─────────
neu(T, "rel_haeufigkeit", "zwei_wege", Z(
    "Eine Münze wird 40-mal geworfen. Wappen fällt 18-mal. Wie groß ist die relative Häufigkeit von Wappen in Prozent? Rechne auf zwei Wegen. Weg A: 18 : 40 als Dezimalzahl und dann mal 100. Weg B: den Bruch 18/40 auf den Nenner 100 erweitern.",
    45, "18 / 40 * 100", "(18 * 5 / 2) / (40 * 5 / 2) * 100", "Beide Wege müssen dasselbe Ergebnis ergeben.",
    "Weg A: 18 : 40 = 0,45 und 0,45 · 100 = 45. Weg B: 18/40 = 9/20 = 45/100 = 45 %.",
    [(18, None, "die absolute Häufigkeit als Prozent genommen"), (22, None, "40 − 18 gerechnet"), (4.5, "fb.stellenwert.eine_stelle_daneben", "eine Stelle verrutscht")], "%"), regel="id.daten.anteil")
neu(T, "rel_haeufigkeit", "bruecke", W(
    "Die Tabelle zeigt 50 Würfe mit einem Würfel. Wie groß ist die relative Häufigkeit der Sechs?",
    "0,16", [("8", "die absolute Häufigkeit statt der relativen genommen"), ("0,08", "durch 100 statt durch 50 geteilt"), ("0,125", "8 durch 64 geteilt")],
    "Relative Häufigkeit = Anzahl der Sechsen : Anzahl aller Würfe.",
    "In der Spalte „6“ steht 8. Es gab 50 Würfe. 8 : 50 = 0,16.",
    lambda: 9 + 7 + 8 + 12 + 6 + 8 == 50 and F(8, 50) == F("0.16") and F(8, 100) != F("0.16") and F(1, 8) != F("0.16"),
    grafik=TAB(["Zahl", "1", "2", "3", "4", "5", "6"], ["Anzahl", "9", "7", "8", "12", "6", "8"])), regel="id.daten.anteil")
neu(T, "rel_haeufigkeit", "anwenden", Z(
    "Eine Qualitätskontrolle prüft 250 Schrauben. 15 davon sind fehlerhaft. Es werden 2000 Schrauben hergestellt. Wie viele davon sind nach dieser Kontrolle ungefähr fehlerhaft?",
    120, "15 / 250 * 2000", "2000 * 6 / 100", "Berechne zuerst die relative Häufigkeit der fehlerhaften Schrauben. Übertrage sie auf 2000.",
    "15 : 250 = 0,06 = 6 %. 6 % von 2000 sind 120. Es sind ungefähr 120 fehlerhafte Schrauben.",
    [(15, None, "die Zahl aus der Prüfung übernommen"), (1880, None, "die nicht fehlerhaften Schrauben berechnet"), (12, "fb.stellenwert.eine_stelle_daneben", "eine Stelle verrutscht")], "Schrauben"), g="einkleidung", regel="id.daten.anteil")

# ───────── darstellen ─────────
neu(T, "darstellen", "umkehren", Z(
    "Eine Urne enthält Kugeln mit den Nummern 1 bis n. Man zieht zweimal nacheinander eine Kugel und legt sie nach jedem Zug zurück. Das Baumdiagramm hat insgesamt 36 Wege. Wie viele Kugeln liegen in der Urne?",
    6, 6, 6, "Jede Stufe hat n Äste. Wie viele Wege gibt es bei zwei Stufen?",
    "Es gibt n · n Wege, weil jeder der n Äste der ersten Stufe wieder n Zweige hat. n · n = 36, also n = 6.",
    [(18, "fb.stufen.addiert_statt_malgenommen", "36 : 2 gerechnet"), (12, "fb.stufen.addiert_statt_malgenommen", "n + n = 12 angenommen"), (36, None, "die Zahl der Wege genannt")]), g="umkehr", regel="id.daten.stufen")
neu(T, "darstellen", "zwei_wege", Z(
    "Ein Würfel wird zweimal geworfen. Wie viele Ergebnisse gehören zum Ereignis „Die Augensumme ist 5 oder 9“? Rechne auf zwei Wegen. Weg A: mit einem Baumdiagramm. Weg B: mit einer Tabelle mit 6 Zeilen und 6 Spalten.",
    8, "4 + 4", "2 * 4", "Zähle die Paare getrennt für Summe 5 und für Summe 9.",
    "Summe 5: (1|4), (2|3), (3|2), (4|1). Summe 9: (3|6), (4|5), (5|4), (6|3). Zusammen 4 + 4 = 8 Ergebnisse.",
    [(4, None, "nur eine der beiden Summen gezählt"), (9, None, "9 Ergebnisse angenommen, weil die Summe 9 heißt"), (14, None, "5 + 9 gerechnet")], "Ergebnisse"), regel="id.daten.stufen")
assert sum(1 for a in range(1, 7) for b in range(1, 7) if a + b in (5, 9)) == 8
neu(T, "darstellen", "bruecke", W(
    "Ein Glücksrad mit den Zahlen 1, 2 und 3 wird zweimal gedreht. Die Tabelle zeigt alle neun Augensummen. Wie viele Ergebnisse gehören zum Ereignis „Die Summe ist größer als 4“?",
    "3", [("6", "„größer oder gleich 4“ gelesen"), ("4", "die Summe 4 mitgezählt"), ("5", "falsch abgezählt")],
    "Zähle die Felder der Tabelle, in denen die Summe 5 oder 6 steht.",
    "Summe 5 steht zweimal, Summe 6 einmal. Zusammen 3 Ergebnisse.",
    lambda: sum(1 for a in (1, 2, 3) for b in (1, 2, 3) if a + b > 4) == 3 and sum(1 for a in (1, 2, 3) for b in (1, 2, 3) if a + b >= 4) == 6,
    grafik=TAB(["+", "1", "2", "3"], ["1", "2", "3", "4"], ["2", "3", "4", "5"], ["3", "4", "5", "6"])), regel="id.daten.stufen")
