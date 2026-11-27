T = "stochastik.grundbegriffe"
# ───────── begriffe ─────────
neu(T, "begriffe", "lueckenweg", L(
    "In einer Urne liegen 6 rote, 2 blaue, 3 grüne und 2 gelbe Kugeln. Man zieht eine Kugel und notiert die Farbe. Der Ergebnisraum hat ① Ergebnisse. Zum Ereignis „rot oder blau“ gehören ② Kugeln. In der Urne liegen insgesamt ③ Kugeln. Zum Gegenereignis „weder rot noch blau“ gehören ④ Kugeln.",
    KOMM(4), [4, 8, 13, 5], ["4", "6 + 2", "6 + 2 + 3 + 2", "{3} - {2}"], ["4", "8", "13", "3 + 2"], "Die Ergebnisse sind die Farben. Das Ereignis fasst Ergebnisse zusammen, gezählt werden aber die Kugeln. Das Gegenereignis besteht aus allen übrigen Kugeln.",
    "Vier Farben, also vier Ergebnisse. Rot oder blau: 6 + 2 = 8 Kugeln. Insgesamt 6 + 2 + 3 + 2 = 13 Kugeln. Gegenereignis: 13 − 8 = 5 Kugeln (3 grüne und 2 gelbe).",
    {0: [(13, None, "die Kugeln statt der Farben gezählt", "6 + 2 + 3 + 2")], 1: [(2, None, "nur die Farbe blau betrachtet", "2"), (9, None, "rot und grün genommen", "6 + 3")], 3: [(8, None, "das Ereignis selbst statt des Gegenereignisses genannt", "{2}")]}), regel="id.daten.anteil")
neu(T, "begriffe", "umkehren", Z(
    "Ein Würfel hat die Zahlen 1 bis 12. Das Ereignis „Die Zahl ist ein Vielfaches von k“ hat genau 4 Ergebnisse. Dabei ist k eine natürliche Zahl größer als 1. Welche Zahl ist k?",
    3, 3, 3, "Zähle für k = 2, 3, 4 … wie viele Vielfache es zwischen 1 und 12 gibt.",
    "Vielfache von 3: 3, 6, 9, 12. Das sind genau 4. Bei k = 2 sind es 6, bei k = 4 nur 3 Vielfache.",
    [(4, None, "die Anzahl der Ergebnisse statt k genannt", False), (2, None, "bei k = 2 gibt es 6 Vielfache", lambda: len([m for m in range(1, 13) if m % 2 == 0]) == 6), (6, None, "bei k = 6 gibt es nur 2 Vielfache", lambda: len([m for m in range(1, 13) if m % 6 == 0]) == 2)]), g="umkehr", regel="id.daten.anteil")
assert [m for m in range(1, 13) if m % 3 == 0] == [3, 6, 9, 12] and all(len([m for m in range(1, 13) if m % k == 0]) != 4 for k in range(2, 13) if k != 3)
neu(T, "begriffe", "anwenden", Z(
    "Ein Glücksrad hat 8 gleich große Felder mit den Zahlen 1 bis 8. Wie viele Ergebnisse gehören zum Ereignis „Die Zahl ist durch 2 oder durch 3 teilbar“?",
    5, "4 + 2 - 1", 5, "Gehe die Zahlen 1 bis 8 der Reihe nach durch. Eine Zahl zählt nur einmal, auch wenn sie in beiden Reihen vorkommt.",
    "Durch 2 teilbar: 2, 4, 6, 8. Durch 3 teilbar: 3 und 6. Die 6 gehört zu beiden. Zusammen 5 Ergebnisse: {2; 3; 4; 6; 8}.",
    [(4, None, "nur die durch 2 teilbaren Zahlen gezählt", lambda: len([m for m in range(1, 9) if m % 2 == 0]) == 4), (6, None, "die 6 doppelt gezählt: 4 + 2", "4 + 2"), (8, None, "alle Felder gezählt", "8")], "Ergebnisse"), g="einkleidung", regel="id.daten.anteil")
assert [m for m in range(1, 9) if m % 2 == 0 or m % 3 == 0] == [2, 3, 4, 6, 8]

# ───────── rel_haeufigkeit ─────────
neu(T, "rel_haeufigkeit", "zwei_wege", Z(
    "Eine Münze wird 40-mal geworfen. Wappen fällt 18-mal. Wie groß ist die relative Häufigkeit von Wappen in Prozent? Rechne auf zwei Wegen. Weg A: 18 : 40 als Dezimalzahl und dann mal 100. Weg B: den Bruch 18/40 zuerst kürzen und dann auf den Nenner 100 erweitern.",
    45, "18 / 40 * 100", "9 / 20 * 100", "Beide Wege müssen dasselbe Ergebnis ergeben.",
    "Weg A: 18 : 40 = 0,45 und 0,45 · 100 = 45. Weg B: 18/40 = 9/20 = 45/100 = 45 %.",
    [(18, None, "die absolute Häufigkeit als Prozent genommen", "18"), (22, None, "40 − 18 gerechnet", "40 - 18"), (4.5, "fb.stellenwert.eine_stelle_daneben", "eine Stelle verrutscht: 18 : 40 · 10", "18 / 40 * 10")], "%"), regel="id.daten.anteil")
neu(T, "rel_haeufigkeit", "bruecke", W(
    "Die Tabelle zeigt 50 Würfe mit einem Würfel. Wie groß ist die relative Häufigkeit der Sechs?",
    "0,16", [("8", "die absolute Häufigkeit statt der relativen genommen"), ("0,08", "durch 100 statt durch 50 geteilt"), ("0,125", "1 durch 8 geteilt statt 8 durch 50")],
    "Relative Häufigkeit = Anzahl der Sechsen : Anzahl aller Würfe.",
    "In der Spalte „6“ steht 8. Es gab 50 Würfe. 8 : 50 = 0,16.",
    lambda: 9 + 7 + 8 + 12 + 6 + 8 == 50 and F(8, 50) == F("0.16") and F(8, 100) == F("0.08") and F(1, 8) == F("0.125"),
    grafik=TAB(["Zahl", "1", "2", "3", "4", "5", "6"], ["Anzahl", "9", "7", "8", "12", "6", "8"])), regel="id.daten.anteil")
neu(T, "rel_haeufigkeit", "anwenden", Z(
    "Eine Qualitätskontrolle prüft 250 Schrauben. 15 davon sind fehlerhaft. Es werden 2000 Schrauben hergestellt. Wie viele davon sind nach dieser Kontrolle ungefähr fehlerhaft?",
    120, "15 / 250 * 2000", "2000 * 6 / 100", "Berechne zuerst die relative Häufigkeit der fehlerhaften Schrauben. Übertrage sie auf 2000.",
    "15 : 250 = 0,06 = 6 %. 6 % von 2000 sind 120. Es sind ungefähr 120 fehlerhafte Schrauben.",
    [(15, None, "die Zahl aus der Prüfung übernommen", "15"), (1880, None, "die nicht fehlerhaften Schrauben berechnet", "2000 - 120"), (12, "fb.stellenwert.eine_stelle_daneben", "eine Stelle verrutscht: 0,6 % statt 6 %", "0.006 * 2000")], "Schrauben"), g="einkleidung", regel="id.daten.anteil")

# ───────── darstellen ─────────
neu(T, "darstellen", "umkehren", Z(
    "Eine Urne enthält Kugeln mit den Nummern 1 bis n. Man zieht zweimal nacheinander eine Kugel und legt sie nach jedem Zug zurück. Das Baumdiagramm hat insgesamt 36 Wege. Wie viele Kugeln liegen in der Urne?",
    6, 6, 6, "Jede Stufe hat n Äste. Wie viele Wege gibt es bei zwei Stufen?",
    "Es gibt n · n Wege, weil jeder der n Äste der ersten Stufe wieder n Zweige hat. n · n = 36, also n = 6.",
    [(18, "fb.stufen.addiert_statt_malgenommen", "Wege als n + n angenommen: n + n = 36, also n = 18", "36 / 2"), (72, None, "36 mit 2 malgenommen statt die Wurzel zu suchen", "36 * 2"), (36, None, "die Zahl der Wege genannt", "36")]), g="umkehr", regel="id.daten.stufen")
neu(T, "darstellen", "zwei_wege", Z(
    "Ein normaler Würfel wird zweimal geworfen. Ein Ergebnis ist ein Zahlenpaar (erster Wurf | zweiter Wurf). Wie viele Ergebnisse gehören zum Ereignis „Die Augensumme ist 5 oder 9“? Rechne auf zwei Wegen. Weg A: mit einem Baumdiagramm. Weg B: mit einer Tabelle mit 6 Zeilen und 6 Spalten.",
    8, "4 + 4", "2 * 4", "Zähle die Paare getrennt für Summe 5 und für Summe 9.",
    "Summe 5: (1|4), (2|3), (3|2), (4|1). Summe 9: (3|6), (4|5), (5|4), (6|3). Zusammen 4 + 4 = 8 Ergebnisse.",
    [(4, None, "nur eine der beiden Summen gezählt", lambda: sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == 5) == 4), (9, None, "die Zahl 9 aus der Summe als Anzahl genommen", False), (14, None, "5 + 9 gerechnet", "5 + 9")], "Ergebnisse"), regel="id.daten.stufen")
assert sum(1 for a in range(1, 7) for b in range(1, 7) if a + b in (5, 9)) == 8
neu(T, "darstellen", "bruecke", W(
    "Ein Glücksrad mit den Zahlen 1, 2 und 3 wird zweimal gedreht. Die Tabelle zeigt alle neun Augensummen. Wie viele Ergebnisse gehören zum Ereignis „Die Summe ist größer als 4“?",
    "3", [("6", "„größer oder gleich 4“ gelesen: auch die drei Felder mit Summe 4 mitgezählt"), ("2", "nur die Summe 5 gezählt, die Summe 6 vergessen"), ("9", "alle Felder der Tabelle gezählt")],
    "Zähle die Felder der Tabelle, in denen die Summe 5 oder 6 steht.",
    "Summe 5 steht zweimal, Summe 6 einmal. Zusammen 3 Ergebnisse.",
    lambda: sum(1 for a in (1, 2, 3) for b in (1, 2, 3) if a + b > 4) == 3 and sum(1 for a in (1, 2, 3) for b in (1, 2, 3) if a + b >= 4) == 6 and sum(1 for a in (1, 2, 3) for b in (1, 2, 3) if a + b == 5) == 2 and len([1 for a in (1, 2, 3) for b in (1, 2, 3)]) == 9,
    grafik=TAB(["+", "1", "2", "3"], ["1", "2", "3", "4"], ["2", "3", "4", "5"], ["3", "4", "5", "6"])), regel="id.daten.stufen")
