from kern import Bau

B = Bau("daten.kennwerte", "M6 3", {
    "mittelwert": "Die Übungen berechnen den Mittelwert aus einer gegebenen Liste.",
    "mittel_rueckwaerts": "Die Übungen suchen einen fehlenden Wert mit einfachen Standardzahlen.",
})
ZF = "In welcher Zeile steckt der erste Fehler, und "

# ---------------- mittelwert ----------------
B.zahl("mittelwert", "test", 3, "parameter", None,
       "Sieben Kinder sparen im Mittel 18 € pro Monat. Ein achtes Kind kommt dazu und spart 42 € pro Monat. Wie groß ist jetzt der Mittelwert aller acht Kinder?",
       21, "(7 · 18 + 42) : 8",
       [(30, "(18 + 42) : 2", "den Mittelwert der beiden Zahlen 18 und 42 gebildet"),
        (24, "18 + 42 : 7", "nur 42 durch 7 geteilt und zu 18 addiert")],
       "Die Summe der sieben Kinder ist 7 · 18 = 126 €. Mit dem achten Kind: 126 + 42 = 168 €. Mittelwert: 168 : 8 = 21 €.", einheit="€")
B.auswahl("mittelwert", "korrektur", 2, "begruenden", None,
          "Der Mittelwert von vier Zahlen ist 10. Eine der Zahlen wird um 8 vergrößert, die anderen bleiben gleich. Was passiert mit dem Mittelwert?",
          ["Er steigt um 8, denn eine Zahl wächst um 8.",
           "Er steigt um 2, denn die Summe wächst um 8 und wird durch 4 geteilt.",
           "Er bleibt gleich, denn die Anzahl der Zahlen ändert sich nicht.",
           "Er steigt um 4, denn man teilt 8 durch 2."],
          1,
          {0: "den Zuwachs einer Zahl auf den Mittelwert übertragen",
           2: "nur auf die Anzahl geschaut, die Summe vergessen",
           3: "den Zuwachs durch 2 statt durch die Anzahl 4 geteilt"},
          "Die Summe wächst um 8. Der Mittelwert ist die Summe geteilt durch 4, also wächst er um 8 : 4 = 2.")
B.luecken("mittelwert", "korrektur", 2, "fehler", "fehler_detektiv",
          "Mia hat die Noten 2, 3, 2 und 5. Zeile 1: Die Summe der Noten ist 2 + 3 + 2 + 5 = 12. Zeile 2: Es sind vier Noten. Zeile 3: Der Mittelwert ist 12 : 3 = 4. Zeile 4: Mias Durchschnitt ist also 4. " + ZF + "wie groß ist der Mittelwert richtig?",
          "Fehler in Zeile □, Mittelwert richtig: □", [3, 3], ["3", "12 : 4"],
          [(2, 4, "12 : 3", "durch 3 statt durch die Zahl der Noten 4 geteilt"),
           (2, 12, "2 + 3 + 2 + 5", "die Summe als Mittelwert angegeben")],
          "Zeile 3 ist falsch: Man teilt durch die Anzahl der Noten, also durch 4. 12 : 4 = 3.")
B.zahl("mittelwert", "korrektur", 2, "parameter", None,
       "Der Mittelwert einer Messreihe ist 7,5. Alle Messwerte werden mit 3 malgenommen. Wie groß ist dann der Mittelwert der neuen Reihe?",
       22.5, "7,5 · 3",
       [(10.5, "7,5 + 3", "3 zum Mittelwert addiert"),
        (2.5, "7,5 : 3", "durch 3 geteilt statt mit 3 malgenommen")],
       "Wird jeder Wert mit 3 malgenommen, so auch die Summe und damit der Mittelwert: 7,5 · 3 = 22,5.")
B.auswahl("mittelwert", "sicherung", 2, "begruenden", None,
          "Der Mittelwert der Zahlen 3, 5, 7 und 9 ist 6. Welche Veränderung lässt den Mittelwert unverändert bei 6?",
          ["Man streicht die 3.",
           "Man ersetzt die 3 durch 4 und die 9 durch 7.",
           "Man fügt eine weitere 6 hinzu.",
           "Man fügt die Zahlen 5 und 8 hinzu."],
          2,
          {0: ("die kleinste Zahl gestrichen: (5 + 7 + 9) : 3 = 7", "(5 + 7 + 9) : 3"),
           1: ("die Summe sinkt um 1: (4 + 5 + 7 + 7) : 4 = 5,75", "(4 + 5 + 7 + 7) : 4"),
           3: "die beiden neuen Zahlen liegen im Mittel bei 6,5, das hebt den Mittelwert an: 37 : 6 ≈ 6,17"},
          "Eine Zahl, die genau dem Mittelwert gleicht, ändert den Mittelwert nicht: (24 + 6) : 5 = 6. Bei den anderen Möglichkeiten ergibt sich 7, 5,75 und etwa 6,17.")
B.zahl("mittelwert", "sicherung", 3, "parameter", None,
       "In einer Gruppe von 9 Kindern ist die mittlere Körpergröße 150 cm. Ein zehntes Kind mit 160 cm kommt dazu. Um wie viele Zentimeter steigt der Mittelwert?",
       1, "(9 · 150 + 160) : 10 − 150",
       [(10, "160 − 150", "den Unterschied des neuen Kindes zum alten Mittelwert genommen"),
        (5, "(160 − 150) : 2", "den Unterschied durch 2 statt durch 10 geteilt")],
       "Neue Summe: 9 · 150 + 160 = 1 510 cm. Neuer Mittelwert: 1 510 : 10 = 151 cm. Er steigt um 1 cm (der Unterschied 10 cm verteilt sich auf 10 Kinder).", einheit="cm")
B.auswahl("mittelwert", "sicherung", 3, "begruenden", None,
          "Fünf Hunde wiegen 8 kg, 9 kg, 10 kg, 11 kg und 12 kg, im Mittel also 10 kg. Ein sechster Hund mit 60 kg kommt dazu. Welche Aussage über den neuen Mittelwert stimmt?",
          ["Er bleibt 10 kg, denn nur ein Wert kommt dazu.",
           "Er beträgt 35 kg, denn man bildet den Mittelwert aus 10 kg und 60 kg.",
           "Er sinkt unter 10 kg, weil jetzt mehr Werte vorhanden sind.",
           "Er beträgt etwa 18 kg und ist damit größer als das Gewicht von fünf der sechs Hunde."],
          3,
          {0: "nicht beachtet, dass die Summe stark wächst",
           1: "den alten Mittelwert wie einen einzelnen Wert behandelt",
           2: "mehr Werte mit sinkendem Mittelwert verwechselt"},
          "Neue Summe: 50 + 60 = 110 kg. 110 : 6 ≈ 18,3 kg. Das ist mehr als jeder der fünf ersten Hunde wiegt. Ein einzelner sehr großer Wert zieht den Mittelwert stark nach oben.")

# ---------------- mittel_rueckwaerts ----------------
B.zahl("mittel_rueckwaerts", "test", 3, "umkehr", "umkehren",
       "Nach vier Wertungen hat eine Turnerin im Mittel 8,5 Punkte. Mit der fünften Wertung soll ihr Mittelwert genau 9 Punkte betragen. Wie viele Punkte braucht sie in der fünften Wertung?",
       11, "9 · 5 − 8,5 · 4",
       [(17.5, "9 + 8,5", "die beiden Mittelwerte addiert"),
        (9.5, "9 + 0,5", "den Zuwachs 0,5 des Mittelwerts zum Zielwert 9 addiert")],
       "Gesamtsumme nach fünf Wertungen: 9 · 5 = 45. Bisher: 8,5 · 4 = 34. Fehlend: 45 − 34 = 11 Punkte.", einheit="Punkte")
B.zahl("mittel_rueckwaerts", "korrektur", 2, "umkehr", "umkehren",
       "Der Mittelwert von sechs Zahlen ist 14. Fünf davon sind 10, 12, 15, 18 und 13. Wie heißt die sechste Zahl?",
       16, "14 · 6 − (10 + 12 + 15 + 18 + 13)",
       [(84, "14 · 6", "nur die Gesamtsumme berechnet"),
        (2, "14 · 5 − (10 + 12 + 15 + 18 + 13)", "mit fünf statt sechs Zahlen gerechnet")],
       "Die Summe aller sechs Zahlen ist 6 · 14 = 84. Die fünf bekannten haben die Summe 68. Die sechste Zahl ist 84 − 68 = 16.")
B.luecken("mittel_rueckwaerts", "korrektur", 2, "fehler", "fehler_detektiv",
          "Der Mittelwert von vier Zahlen ist 9. Drei der Zahlen sind 7, 11 und 8. Zeile 1: Die Summe aller vier Zahlen ist 9 · 4 = 36. Zeile 2: Die drei bekannten Zahlen haben die Summe 7 + 11 + 8 = 26. Zeile 3: Die vierte Zahl ist 36 + 26 = 62. Zeile 4: Die vierte Zahl ist also 62. " + ZF + "wie heißt die vierte Zahl richtig?",
          "Fehler in Zeile □, richtig: □", [3, 10], ["3", "36 − 26"],
          [(2, 62, "36 + 26", "die beiden Summen addiert statt subtrahiert"),
           (2, -10, "26 − 36", "in der falschen Reihenfolge subtrahiert")],
          "Zeile 3 ist falsch: Die fehlende Zahl ist die Gesamtsumme minus die bekannte Summe, also 36 − 26 = 10.")
B.auswahl("mittel_rueckwaerts", "korrektur", 2, "begruenden", None,
          "Der Mittelwert von drei Zahlen ist 20. Zwei der Zahlen sind 15 und 18. Mia sagt: „Die dritte Zahl ist 20, denn der Mittelwert ist 20.“ Welche Aussage stimmt?",
          ["Mia hat recht, denn der Mittelwert ist die Zahl in der Mitte.",
           "Mia hat nicht recht: Die dritte Zahl ist 20 − 33 = −13.",
           "Mia hat nicht recht: Die Summe ist 3 · 20 = 60, die dritte Zahl ist also 60 − 33 = 27.",
           "Mia hat nicht recht: Die dritte Zahl ist 33 : 2 = 16,5."],
          2,
          {0: "den Mittelwert mit der Zahl in der Mitte verwechselt",
           1: "den Mittelwert statt der Gesamtsumme abgezogen",
           3: "die beiden bekannten Zahlen gemittelt"},
          "Die Summe der drei Zahlen ist 3 · 20 = 60. 15 + 18 = 33. Die dritte Zahl ist 60 − 33 = 27 (Kontrolle: (15 + 18 + 27) : 3 = 20).")
B.zahl("mittel_rueckwaerts", "sicherung", 3, "umkehr", "umkehren",
       "Drei Geschwister haben im Mittel 15 € Taschengeld. Das älteste bekommt 6 € mehr als das mittlere, das jüngste 3 € weniger als das mittlere. Wie viel Taschengeld bekommt das mittlere Kind?",
       14, "(45 − 6 + 3) : 3",
       [(12, "(45 − 6 − 3) : 3", "beide Unterschiede abgezogen"),
        (15, "45 : 3", "den Mittelwert als Wert des mittleren Kindes angegeben")],
       "Gesamt: 3 · 15 = 45 €. Mit m für das mittlere Kind: (m + 6) + m + (m − 3) = 45, also 3m + 3 = 45, 3m = 42, m = 14 €. Kontrolle: 20 + 14 + 11 = 45.", einheit="€")
B.zahl("mittel_rueckwaerts", "sicherung", 2, "umkehr", "zwei_wege",
       "Der Mittelwert der Zahlen 12, 15, 9, x und 14 ist 13. Mia löst es über die Summe, Jonas über die Abweichungen der Zahlen vom Mittelwert 13. Wie groß ist x?",
       15, "13 · 5 − (12 + 15 + 9 + 14)",
       [(65, "13 · 5", "nur die Gesamtsumme angegeben"),
        (2, "13 · 4 − (12 + 15 + 9 + 14)", "mit vier statt fünf Zahlen gerechnet")],
       "Mia: 5 · 13 = 65, 65 − (12 + 15 + 9 + 14) = 65 − 50 = 15. Jonas: Abweichungen −1, +2, −4, +1 ergeben −2, also muss x um +2 über 13 liegen: x = 15.")
B.luecken("mittel_rueckwaerts", "sicherung", 3, "transfer", "anwenden",
          "Eine Läuferin hat bei 5 Runden im Mittel 70 Sekunden gebraucht. Die schnellste Runde dauerte 65 s, die langsamste 78 s, die drei übrigen Runden waren gleich lang. Wie lang war jede der drei übrigen Runden, und wie viele Sekunden brauchte sie insgesamt?",
          "Jede der drei Runden: □ s, insgesamt: □ s", [69, 350], ["(70 · 5 − 65 − 78) : 3", "70 · 5"],
          [(1, 207, "70 · 5 − 65 − 78", "die Summe der drei Runden als Länge einer Runde angegeben"),
           (1, 70, "70", "den Mittelwert als Länge der drei Runden angenommen"),
           (2, 280, "70 · 4", "mit 4 statt 5 Runden gerechnet"),
           (2, 75, "70 + 5", "5 zum Mittelwert addiert")],
          "Gesamtzeit: 5 · 70 = 350 s. Schnellste und langsamste Runde: 65 + 78 = 143 s. Die drei übrigen Runden: 350 − 143 = 207 s, jede 207 : 3 = 69 s.")
