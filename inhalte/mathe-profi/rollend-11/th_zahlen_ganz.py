T = "zahlen.ganz"

# ───────── deuten: Zwei Wege ─────────
Z(T, "deuten", "zwei_wege",
  "Eine Möwe fliegt 85 m über dem Meeresspiegel. Ein Fisch schwimmt bei −42 m. Dann steigt die Möwe noch 15 m auf und der Fisch taucht noch 30 m tiefer. "
  "Weg A: Rechne den neuen Abstand in zwei Teilen: von der Möwe bis zum Meeresspiegel und von dort bis zum Fisch. Weg B: Rechne die beiden neuen Höhen mit einer Subtraktion. "
  "Wie viele Meter sind Möwe und Fisch dann voneinander entfernt?",
  172, "(85 + 15) - (-42 - 30)", "(85 + 15) + (42 + 30)",
  "Bestimme zuerst, in welcher Höhe sich Möwe und Fisch nach den Bewegungen befinden.",
  "Möwe: 85 + 15 = 100 m. Fisch: −42 − 30 = −72 m. Weg A: 100 m bis zum Meeresspiegel und 72 m weiter bis zum Fisch: 100 + 72 = 172 m. "
  "Weg B: 100 − (−72) = 100 + 72 = 172 m. Beide Wege ergeben 172 m.",
  [(28, "100 - 72", "die Beträge voneinander abgezogen, als lägen beide auf derselben Seite des Meeresspiegels: 100 − 72"),
   (127, "85 + 42", "die Bewegungen vergessen und nur die Anfangshöhen genommen: 85 + 42"),
   (142, "100 + 42", "das Tieferschwimmen des Fisches vergessen: 100 + 42")],
  "id.zahlen.zahlengerade", einheit="m")

# ───────── ordnen: Brücke ─────────
Z(T, "ordnen", "bruecke",
  "Die Tabelle zeigt die Kontostände von fünf Personen. Ordne die Stände gedanklich auf einer Zahlengerade von links nach rechts. "
  "Wie viele Euro liegen zwischen dem zweitniedrigsten und dem zweithöchsten Stand?",
  40, "5 - (-35)", "35 + 5",
  "Welche Zahl liegt auf der Zahlengerade am weitesten links, welche als Nächstes? Mit negativen Zahlen kommt es nicht auf die Größe der Ziffer an.",
  "Von links nach rechts: −80, −35, −12, 5, 20. Der zweitniedrigste Stand ist −35 €, der zweithöchste ist 5 €. Zwischen ihnen liegen 5 − (−35) = 40 €.",
  [(23, "35 - 12", "nach dem Betrag statt nach der Lage geordnet: 12, 35 statt −35, 5 → 35 − 12"),
   (100, "20 - (-80)", "höchsten und niedrigsten Stand genommen statt des zweithöchsten und des zweitniedrigsten"),
   (17, "5 - (-12)", "den drittniedrigsten Stand (−12) statt des zweitniedrigsten (−35) genommen")],
  "id.zahlen.zahlengerade", einheit="€",
  grafik={"typ": "tabelle", "kopf": ["Person", "Ali", "Bea", "Cem", "Dora", "Emil"], "zeilen": [["Stand in €", "−35", "20", "−80", "5", "−12"]]})


# ───────── schriftlich_plus_minus: Fehler-Detektiv ─────────
def add_zeile(name, summanden, uebertrag, summe, schreibe, merke):
    teile = " + ".join(str(s) for s in summanden) + (f" + {uebertrag}" if uebertrag else "")
    ok = sum(summanden) + uebertrag == summe and summe % 10 == schreibe and summe // 10 == merke
    mer = f" und merke {merke}" if merke else ""
    return f"{name}: {teile} = {summe}. Ich schreibe {schreibe} hin{mer}.", ok


FD(T, "schriftlich_plus_minus",
   "Kim addiert schriftlich 3 748 + 2 659 + 1 875 und rechnet von rechts nach links.",
   [add_zeile("Einer", [8, 9, 5], 0, 22, 2, 1), add_zeile("Zehner", [4, 5, 7], 1, 17, 7, 1),
    add_zeile("Hunderter", [7, 6, 8], 1, 22, 2, 2), add_zeile("Tausender", [3, 2, 1], 2, 8, 8, 0)],
   "Prüfe jede Zeile: Passen Summe, hingeschriebene Ziffer und gemerkter Übertrag zusammen?",
   "Die Summe in Zeile 1 stimmt: 8 + 9 + 5 = 22. Aber bei 22 muss man 2 merken (zwei Zehner), nicht 1. Alle weiteren Zeilen rechnen mit dem falschen Übertrag richtig weiter. "
   "Richtig wäre: Zehner 4 + 5 + 7 + 2 = 18 (schreibe 8, merke 1), Hunderter 7 + 6 + 8 + 1 = 22 (schreibe 2, merke 2), Tausender 3 + 2 + 1 + 2 = 8. Ergebnis: 8 282, Kim erhält 8 272.",
   "rr.plusminus", "bei der Summe 22 nur 1 statt 2 Zehner gemerkt")

# ───────── subtrahieren: Umkehren ─────────
Z(T, "subtrahieren", "umkehren",
  "Ich denke mir eine ganze Zahl. Davon ziehe ich −9 ab, dann ziehe ich 14 ab, und dann addiere ich −5. Ich erhalte −21. Wie heißt meine Zahl?",
  -11, "-21 - (-5) + 14 + (-9)", "-21 + 10",
  "Mache jeden Schritt in umgekehrter Reihenfolge rückgängig. Was hebt „minus −9“ auf?",
  "Rückwärts, mit dem letzten Schritt zuerst: −21 − (−5) = −16. Dann −16 + 14 = −2. Dann −2 + (−9) = −11. Probe: −11 − (−9) = −2; −2 − 14 = −16; −16 + (−5) = −21. Die Zahl ist −11.",
  [(7, "-21 - (-5) + 14 - (-9)", "den ersten Schritt falsch rückgängig gemacht: −9 statt abgezogen noch einmal abgezogen"),
   (-16, "-21 + 14 + (-9)", "den dritten Schritt (+ (−5)) nicht rückgängig gemacht"),
   (-31, "-21 + (-10)", "die Gesamtänderung −10 zum Ergebnis addiert statt von ihm abgezogen")],
  "rr.plusminus")


# ───────── ketten: Fehler-Detektiv ─────────
FD(T, "ketten",
   "Kim berechnet −14 − (−9) + (−6) − (8 − 21) in Schritten.",
   [("Die innere Klammer: 8 − 21 = −13", 8 - 21 == -13),
    ("Der Term lautet jetzt −14 − (−9) + (−6) − (−13) = −14 + 9 − 6 − 13", -14 - (-9) + (-6) - (-13) == -14 + 9 - 6 - 13),
    ("Von links nach rechts: −14 + 9 − 6 − 13 = −24", -14 + 9 - 6 - 13 == -24)],
   "Wie lässt sich „minus eine negative Zahl“ ersetzen? Rechne jede Zeile einzeln nach.",
   "Zeile 1 stimmt. In Zeile 2 steht vor der letzten Klammer „− (−13)“. Das heißt „plus 13“, nicht „minus 13“. Richtig: −14 + 9 − 6 + 13 = 2. "
   "Zeile 3 rechnet mit der falschen Zeile 2 richtig weiter (−24).",
   "rr.plusminus", "„− (−13)“ als „− 13“ aufgelöst")

# ───────── sach: Zwei Wege ─────────
Z(T, "sach", "zwei_wege",
  "Der Pegel eines Baches steht am Montagmorgen bei −35 cm (Nullmarke ist 0). Montag steigt er um 60 cm, Dienstag fällt er um 45 cm, Mittwoch steigt er um 25 cm, "
  "Donnerstag fällt er um 80 cm, Freitag steigt er um 38 cm. Weg A: Verfolge den Pegel Tag für Tag. Weg B: Zähle alle Anstiege zusammen und alle Rückgänge zusammen und "
  "vergleiche beides mit dem Start. Welchen Pegel zeigt die Messlatte am Freitagabend in cm?",
  -37, "-35 + 60 - 45 + 25 - 80 + 38", "-35 + (60 + 25 + 38) - (45 + 80)",
  "Beide Wege müssen dasselbe ergeben. Vergiss nicht, wo der Pegel am Montagmorgen steht.",
  "Weg A: −35 + 60 = 25; 25 − 45 = −20; −20 + 25 = 5; 5 − 80 = −75; −75 + 38 = −37. Weg B: Anstiege 60 + 25 + 38 = 123 cm, Rückgänge 45 + 80 = 125 cm, Bilanz −2 cm. −35 + (−2) = −37. Der Pegel steht bei −37 cm.",
  [(-2, "(60 + 25 + 38) - (45 + 80)", "den Startpegel −35 cm vergessen und nur die Bilanz −2 genommen"),
   (-33, "-35 - (-2)", "die Bilanz −2 mit dem falschen Vorzeichen zum Start gerechnet: −35 − (−2)"),
   (37, "35 + 2", "Vorzeichen des Ergebnisses vergessen")],
  "rr.plusminus", einheit="cm")
