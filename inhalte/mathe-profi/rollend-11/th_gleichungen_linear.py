T = "gleichungen.linear"

# ───────── waage: Fehler-Detektiv ─────────
FD(T, "waage",
   "Kim löst 7x − 4 = 3x + 20 und denkt dabei an eine Waage, die im Gleichgewicht bleiben muss.",
   [("Auf beiden Seiten 3x wegnehmen: 4x − 4 = 20", aequi("7*x-4", "3*x+20", "4*x-4", "20")),
    ("Auf der linken Seite 4 dazulegen: 4x − 4 + 4 = 20, also 4x = 20", aequi("4*x-4", "20", "4*x", "20")),
    ("Beide Seiten durch 4 teilen: x = 5", aequi("4*x", "20", "x", "5"))],
   "Setze das Ergebnis in die Gleichung am Anfang ein. Was muss mit einer Waage immer auf beiden Seiten geschehen?",
   "Zeile 1 stimmt. In Zeile 2 wird nur links 4 dazugelegt. Die Waage kippt: Auch rechts muss 4 dazukommen, also 4x = 24. Zeile 3 rechnet mit der falschen Zeile 2 richtig weiter. "
   "Richtig ist x = 6. Probe: 7 · 6 − 4 = 38 und 3 · 6 + 20 = 38.",
   "rr.waage", "die 4 nur auf einer Seite der Gleichung addiert")

# ───────── probe: Anwenden ─────────
assert 12 + 3 * 12 == 30 + 1.5 * 12 == 48
Z(T, "probe", "anwenden",
  "Eine Pflanze A ist 12 cm hoch und wächst gleichmäßig 3 cm pro Woche. Eine Pflanze B ist 30 cm hoch und wächst gleichmäßig 1,5 cm pro Woche. Nach einiger Zeit sind beide gleich hoch. "
  "Löse die Gleichung und mache die Probe in der Aufgabe: Wie viele Zentimeter sind beide Pflanzen dann hoch?",
  48, "12 + 3 * ((30 - 12) / (3 - 1.5))", "30 + 1.5 * 12",
  "Stelle für w Wochen eine Gleichung auf: Höhe von A = Höhe von B. Die Probe: Setze w in beide Höhen ein, beide Werte müssen gleich sein.",
  "Nach w Wochen: 12 + 3w = 30 + 1,5w. Daraus 1,5w = 18, also w = 12 Wochen. Probe: Pflanze A: 12 + 3 · 12 = 48 cm. Pflanze B: 30 + 1,5 · 12 = 48 cm. Beide sind 48 cm hoch.",
  [(12, "(30 - 12) / (3 - 1.5)", "die Zahl der Wochen genannt statt der Höhe"),
   (30, "12 + 3 * ((30 - 12) / 3)", "durch 3 statt durch 1,5 geteilt (6 Wochen) und die Höhe von A genannt"),
   (18, "30 - 12", "den Unterschied der Anfangshöhen genannt")],
  "rr.waage", einheit="cm")

# ───────── beide_seiten: Brücke ─────────
assert 12 + 8 * 5 == 82 - 6 * 5 == 52
Z(T, "beide_seiten", "bruecke",
  "Becken A wird gleichmäßig gefüllt, Becken B wird gleichmäßig leergepumpt. Die Tabelle zeigt den Wasserstand beider Becken in Litern. Nach wie vielen Minuten (nach Minute 0) enthalten beide Becken gleich viele Liter?",
  5, "(82 - 12) / (8 + 6)", "(82 - 12) / 14",
  "Wie viele Liter kommen bei A pro Minute dazu, wie viele gehen bei B pro Minute weg? Schreibe beide Wasserstände nach t Minuten als Term.",
  "Aus der Tabelle: A wächst um 8 Liter pro Minute, B nimmt um 6 Liter pro Minute ab. Nach t Minuten: A = 12 + 8t, B = 82 − 6t. Gleichsetzen: 12 + 8t = 82 − 6t, also 14t = 70 und t = 5. "
  "Probe: 12 + 40 = 52 und 82 − 30 = 52.",
  [(35, "(82 - 12) / (8 - 6)", "die beiden Raten voneinander abgezogen statt addiert"),
   (70, "82 - 12", "nur den Unterschied der Anfangswerte genannt"),
   (14, "8 + 6", "die Summe der beiden Raten genannt statt der Zeit")],
  "rr.waage", einheit="min",
  grafik={"typ": "tabelle", "kopf": ["Minute", "0", "1", "2", "3"], "zeilen": [["Becken A in Litern", "12", "20", "28", "36"], ["Becken B in Litern", "82", "76", "70", "64"]]})

# ───────── sach: Umkehren ─────────
assert 40 + 7 * 8 == 24 + 9 * 8 == 96
Z(T, "sach", "umkehren",
  "Anna hat anfangs 40 € und spart jede Woche 7 €. Ben spart jede Woche 9 €. Nach 8 Wochen haben beide gleich viel Geld. Wie viel Euro hatte Ben am Anfang?",
  24, "40 + 7 * 8 - 9 * 8", "40 - (9 - 7) * 8",
  "Wie viel Geld hat Anna nach 8 Wochen? Wie viel hat Ben in dieser Zeit gespart? Gehe von dem Endstand rückwärts zum Anfang.",
  "Anna hat nach 8 Wochen 40 + 7 · 8 = 96 €. Ben hat dann auch 96 €. Er hat in den 8 Wochen 9 · 8 = 72 € gespart. Am Anfang hatte er also 96 − 72 = 24 €. "
  "Probe: 24 + 72 = 96.",
  [(96, "40 + 7 * 8", "den gemeinsamen Endstand genannt"),
   (16, "(9 - 7) * 8", "den Unterschied der Sparbeträge pro Woche mal 8 genannt"),
   (112, "40 + 9 * 8", "Annas Anfangsbetrag plus Bens Gespartes gerechnet")],
  "rr.waage", einheit="€")
