T = "groessen.proportional"
WF, VH = "id.verhaeltnisse.wert_fuer_eins", "rr.verhaeltnis"

# ───────── einheit ─────────
neu(T, "einheit", "zwei_wege", Z(
    "5 Äpfel kosten 2 €. Was kosten 12 Äpfel? Weg A: Berechne zuerst den Preis für 1 Apfel und rechne dann mit 12. Weg B: Überlege, das Wievielfache von 5 die Zahl 12 ist, und nimm den Preis für 5 Äpfel mit diesem Faktor mal.",
    4.8, "2 / 5 * 12", "2 * 2.4", "Bei Weg B: Wie oft passt 5 in 12? Das Ergebnis ist keine ganze Zahl.",
    "Weg A: 1 Apfel kostet 2 € : 5 = 0,40 €. 12 Äpfel: 12 · 0,40 € = 4,80 €. Weg B: 12 : 5 = 2,4. 2,4 · 2 € = 4,80 €.",
    [(24, None, "2 € mit 12 malgenommen", "2 * 12"), (10, None, "2 € mit 5 malgenommen", "2 * 5"), (0.4, None, "nur den Preis für 1 Apfel genannt", "2 / 5")], "€"), regel=WF)
neu(T, "einheit", "anwenden", Z(
    "Eine Pumpe fördert in 8 Minuten 120 Liter Wasser. Wie viele Liter fördert sie in einer Stunde?",
    900, "120 / 8 * 60", "15 * 60", "Auf welche gemeinsame Zeiteinheit musst du die Angaben bringen? Was lässt sich zuerst ausrechnen?",
    "In 1 Minute: 120 : 8 = 15 Liter. Eine Stunde hat 60 Minuten: 15 · 60 = 900 Liter.",
    [(15, None, "nur die Liter je Minute genannt", "120 / 8"), (960, None, "120 mit 8 malgenommen", "120 * 8"), (7200, None, "120 mit 60 malgenommen", "120 * 60")], "Liter"), g="transfer", regel=WF)

# ───────── dreisatz ─────────
neu(T, "dreisatz", "anwenden", Z(
    "Ein Lastwagen fährt in 3 Stunden 240 km. Er fährt immer gleich schnell. Wie weit kommt er in 5 Stunden?",
    400, "240 / 3 * 5", "80 * 5", "Wie weit fährt er in einer Stunde?",
    "In 1 Stunde: 240 km : 3 = 80 km. In 5 Stunden: 5 · 80 km = 400 km.",
    [(160, None, "nur mit dem Zeitunterschied der beiden Fahrten gerechnet", "240 / 3 * 2"), (720, None, "240 mit 3 malgenommen", "240 * 3"), (1200, None, "240 mit 5 malgenommen", "240 * 5")], "km"), regel=VH)
neu(T, "dreisatz", "zwei_wege", Z(
    "Ein Kopierer druckt 90 Blätter in 6 Minuten. Wie lange braucht er für 330 Blätter? Weg A: Bestimme, wie viele Blätter er pro Minute druckt, und teile 330 durch diese Zahl. Weg B: Überlege, wie lange 270 Blätter dauern, und rechne die restlichen 60 Blätter dazu.",
    22, "330 / (90 / 6)", "3 * 6 + 60 / 15", "Bei Weg B: 270 Blätter sind das Dreifache von 90 Blättern. Wie lange dauern 60 Blätter?",
    "Weg A: 90 : 6 = 15 Blätter je Minute. 330 : 15 = 22 Minuten. Weg B: 270 Blätter brauchen 3 · 6 = 18 Minuten. 60 Blätter brauchen 60 : 15 = 4 Minuten. 18 + 4 = 22 Minuten.",
    [(55, None, "330 durch 6 geteilt", "330 / 6"), (18, None, "nur die ersten 270 Blätter gerechnet", "3 * 6"), (4, None, "nur die restlichen 60 Blätter gerechnet", "60 / 15")], "min"), g="verknuepfen", regel=VH)

# ───────── geschickt ─────────
neu(T, "geschickt", "umkehren", Z(
    "36 Eier kosten 9 €. Wie viele Eier bekommt man für 2,50 €?",
    10, "2.5 / (9 / 36)", "2.5 * 4", "Wie viel kostet ein Ei? Wie oft passt dieser Preis in 2,50 €?",
    "Ein Ei kostet 9 € : 36 = 0,25 €. 2,50 € : 0,25 € = 10. Man bekommt 10 Eier. Probe: 10 · 0,25 € = 2,50 €.",
    [(90, None, "2,50 mit 36 malgenommen", "2.5 * 36"), (0.25, None, "nur den Preis für ein Ei genannt", "9 / 36"), (4, None, "36 durch 9 geteilt", "36 / 9")], "Eier"), g="umkehr", regel=WF)
neu(T, "geschickt", "bruecke", Z(
    "Die Tabelle gehört zu einer proportionalen Zuordnung (Anzahl Hefte → Preis). Wie viel Euro kosten 14 Hefte?",
    21, "6 + 15", "14 * 1.5", "Aus welchen Heftzahlen der Tabelle kannst du 14 zusammensetzen? Was bedeutet das für die Preise?",
    "14 Hefte sind 4 Hefte und 10 Hefte. Preis: 6 € + 15 € = 21 €. Kontrolle: Ein Heft kostet 1,50 €, 14 · 1,50 € = 21 €.",
    [(28, None, "14 mit 2 malgenommen", "14 * 2"), (24, None, "den Preis für 6 Hefte statt 4 Hefte addiert: 9 + 15", "9 + 15"), (15, None, "nur den Preis für 10 Hefte genannt", "15")], "€",
    grafik=TAB(["Hefte", "Preis in €"], ["4", "6"], ["6", "9"], ["10", "15"])), g="verknuepfen", regel=WF)

# ───────── sach ─────────
neu(T, "sach", "bruecke", Z(
    "Die Tabelle zeigt ein Rezept für 4 Personen. Wie viel Gramm Butter braucht man für 10 Personen?",
    300, "120 / 4 * 10", "30 * 10", "Wie viel Butter braucht eine Person?",
    "Für 1 Person: 120 g : 4 = 30 g Butter. Für 10 Personen: 10 · 30 g = 300 g.",
    [(1200, None, "120 g mit 10 malgenommen", "120 * 10"), (480, None, "120 g mit 4 malgenommen", "120 * 4"), (30, None, "nur die Menge für eine Person genannt", "120 / 4")], "g",
    grafik=TAB(["Zutat", "Menge für 4 Personen"], ["Mehl", "200 g"], ["Zucker", "80 g"], ["Butter", "120 g"])), regel=WF)
neu(T, "sach", "umkehren", Z(
    "Mit einer Tankfüllung von 45 Litern kommt ein Auto 900 km weit. Wie viele Liter verbraucht es auf 100 km?",
    5, "45 / (900 / 100)", "45 / 9", "Wie viele Hunderter sind 900 km? Verteile die 45 Liter darauf.",
    "900 km sind 9 mal 100 km. 45 Liter : 9 = 5 Liter. Das Auto verbraucht 5 Liter auf 100 km.",
    [(20, None, "die Kilometer je Liter genannt: 900 : 45", "900 / 45"), (405, None, "45 mit 9 malgenommen", "45 * 9"), (0.05, None, "45 durch 900 geteilt (Verbrauch je km)", "45 / 900")], "Liter"), g="rueckwaerts", regel=WF)

# ───────── aenderung ─────────
neu(T, "aenderung", "bruecke", Z(
    "Die Tabelle zeigt die Temperatur an einem Morgen. Sie steigt gleichmäßig. Um wie viel Grad steigt sie pro Stunde?",
    3, "(24 - 12) / (12 - 8)", "(18 - 12) / 2", "Wie viele Grad kommen zwischen 8 Uhr und 12 Uhr dazu? Wie viele Stunden sind das?",
    "Von 8 Uhr bis 12 Uhr steigt die Temperatur um 24 − 12 = 12 Grad in 4 Stunden. Pro Stunde: 12 : 4 = 3 Grad.",
    [(6, None, "den Anstieg in 2 Stunden genannt", "18 - 12"), (12, None, "den gesamten Anstieg genannt", "24 - 12"), (4, None, "die Zahl der Stunden genannt", "12 - 8")], "°C",
    grafik=TAB(["Uhrzeit", "Temperatur in °C"], ["8 Uhr", "12"], ["10 Uhr", "18"], ["12 Uhr", "24"])))
neu(T, "aenderung", "anwenden", Z(
    "Ein Becken wird gleichmäßig gefüllt. Nach 2 Stunden sind 800 Liter im Becken, nach 5 Stunden 2 000 Liter. Wie viele Liter sind nach 8 Stunden im Becken?",
    3200, "800 + 6 * (2000 - 800) / 3", "2000 + 3 * 400", "Wie viele Liter kommen pro Stunde dazu? Wie viele Stunden sind es noch bis zur 8. Stunde?",
    "Von der 2. bis zur 5. Stunde kommen 1 200 Liter in 3 Stunden dazu, also 400 Liter je Stunde. Von der 5. bis zur 8. Stunde noch einmal 3 · 400 = 1 200 Liter. 2 000 + 1 200 = 3 200 Liter.",
    [(6400, None, "8 mit 800 malgenommen", "8 * 800"), (2800, None, "nur 800 Liter dazugerechnet", "2000 + 800"), (5600, None, "den Zuwachs von 1 200 Litern, der schon 3 Stunden umfasst, noch einmal mit 3 malgenommen", "2000 + 3 * 1200")], "Liter"), g="transfer", regel=WF)
