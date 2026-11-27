T = "groessen.indirekt"
# ───────── erkennen ─────────
neu(T, "erkennen", "lueckenweg", L(
    "Alle Helfer arbeiten gleich schnell. 3 Helfer brauchen 24 Stunden, 6 Helfer brauchen 12 Stunden. Bei einer indirekten Proportionalität ist das Produkt aus Helfern und Stunden immer gleich. Dieses Produkt ist ①. Dann brauchen 4 Helfer ② Stunden und 9 Helfer ③ Stunden.",
    KOMM(3), [72, 18, 8], ["3 * 24", "{1} // 4", "{1} // 9"], ["72", "72 // 4", "72 // 9"], "Rechne Helfer mal Stunden. Teile dieses Produkt durch die neue Zahl der Helfer.",
    "3 · 24 = 72 und 6 · 12 = 72. 72 : 4 = 18 und 72 : 9 = 8.",
    {0: [(27, "fb.verhaeltnis.addiert_statt_malgenommen", "3 + 24 gerechnet", "3 + 24")], 1: [(24, None, "die Stunden von 3 Helfern übernommen", "24")], 2: [(216, "fb.verhaeltnis.falsche_richtung", "mit der Helferzahl malgenommen: 24 · 9", "24 * 9")]}), regel="rr.verhaeltnis")
neu(T, "erkennen", "fehler_detektiv", FD(
    "Kim prüft, ob die Zuordnung Arbeiter → Tage indirekt proportional ist: 2 Arbeiter brauchen 30 Tage, 5 Arbeiter brauchen 12 Tage, 10 Arbeiter brauchen 7 Tage.",
    [("Ich prüfe, ob das Produkt aus Arbeitern und Tagen immer gleich ist.", True), ("Die Produkte sind 2 · 30 = 60, 5 · 12 = 60 und 10 · 7 = 70.", 2 * 30 == 60 and 5 * 12 == 60 and 10 * 7 == 70),
     ("60, 60 und 70 sind fast gleich, also ist die Zuordnung indirekt proportional.", 60 == 70)],
    "Muss das Produkt genau gleich sein oder reicht „fast“?",
    "Bei einer indirekten Proportionalität muss das Produkt immer genau gleich sein. 70 ist nicht 60. Die Zuordnung ist nicht indirekt proportional."), regel="id.funktionen.zuordnung")
neu(T, "erkennen", "bruecke", W(
    "Die Tabelle zeigt, wie lange verschiedene Zahlen von Helfern für eine Arbeit brauchen. Alle Helfer arbeiten gleich schnell. Welche Aussage passt?",
    "Indirekt proportional: Das Produkt ist immer 24.", [("Direkt proportional: Der Quotient ist immer gleich.", "die Art vertauscht, die Zeit wird kleiner"), ("Indirekt proportional: Die Differenz ist immer gleich.", "Differenz statt Produkt geprüft"), ("Weder noch: Die Zeiten werden kleiner.", "„wird kleiner“ als Ausschluss gelesen")],
    "Bilde für jede Spalte das Produkt aus Helfern und Stunden.",
    "2 · 12 = 24, 4 · 6 = 24, 8 · 3 = 24. Das Produkt ist immer gleich. Die Zuordnung ist indirekt proportional.",
    lambda: 2 * 12 == 4 * 6 == 8 * 3 == 24 and 12 / 2 != 6 / 4,
    grafik=TAB(["Helfer", "2", "4", "8"], ["Stunden", "12", "6", "3"])), regel="id.funktionen.zuordnung")

# ───────── vervielfachen ─────────
neu(T, "vervielfachen", "lueckenweg", L(
    "Die Zuordnung Pumpen → Stunden ist indirekt proportional (alle Pumpen leisten gleich viel). 4 Pumpen brauchen 24 Stunden. Doppelt so viele Pumpen brauchen nur die Hälfte der Zeit: 8 Pumpen brauchen ① Stunden. Verdoppelst du die Pumpenzahl noch einmal auf 16, halbiert sich die Zeit aus ① noch einmal: 16 Pumpen brauchen ② Stunden. Zur Probe rechnest du 16 mal ②. Das Ergebnis ist ③.",
    KOMM(3), [12, 6, 96], ["24 // 2", "{1} // 2", "16 * {2}"], ["12", "6", "4 * 24"], "Mehr Pumpen: Die Zeit wird durch denselben Faktor geteilt. Das Produkt aus Pumpen und Stunden bleibt gleich.",
    "8 Pumpen: 24 : 2 = 12 Stunden. 16 Pumpen: 12 : 2 = 6 Stunden. Probe: 16 · 6 = 96 und 4 · 24 = 96. Das Produkt bleibt gleich.",
    {0: [(48, "fb.verhaeltnis.falsche_richtung", "mit 2 malgenommen statt geteilt", "24 * 2")], 1: [(24, "fb.verhaeltnis.falsche_richtung", "vom richtigen Wert 12 ausgegangen, aber mit 2 malgenommen statt durch 2 geteilt", "{1} * 2")]}), regel="rr.verhaeltnis")
neu(T, "vervielfachen", "zwei_wege", Z(
    "6 Maler streichen ein Haus in 20 Tagen. Alle Maler arbeiten gleich schnell, und die Arbeit lässt sich beliebig aufteilen. Wie viele Tage brauchen 8 Maler? Rechne auf zwei Wegen. Weg A: erst ausrechnen, wie lange ein Maler braucht. Weg B: Die Zahl der Maler wächst um den Faktor 8/6, deshalb ändert sich die Zeit um den Faktor 6/8.",
    15, "6 * 20 / 8", "20 * 6 / 8", "Beide Wege müssen dasselbe ergeben. Mehr Maler: Die Zeit wird kürzer.",
    "Weg A: 1 Maler braucht 6 · 20 = 120 Tage, 8 Maler brauchen 120 : 8 = 15 Tage. Weg B: Die Malerzahl wächst um den Faktor 8/6, die Zeit ändert sich um den Faktor 6/8: 20 · 6/8 = 15 Tage.",
    [(26.67, "fb.verhaeltnis.falsche_richtung", "direkt proportional gerechnet: 20 · 8 : 6 (gerundet)", "20 * 8 / 6"), (18, "fb.verhaeltnis.addiert_statt_malgenommen", "20 − 2 gerechnet, weil 2 Maler mehr kommen", "20 - 2")], "Tage"), regel="rr.verhaeltnis")
neu(T, "vervielfachen", "umkehren", Z(
    "10 gleich starke Pumpen leeren ein Becken in 12 Stunden. Jede Pumpe fördert gleichmäßig. Es soll in nur 8 Stunden leer sein. Wie viele solche Pumpen braucht man mindestens?",
    15, "10 * 12 / 8", 15, "Das Produkt aus Pumpen und Stunden bleibt gleich. Rechne zurück von der Zeit zur Zahl der Pumpen.",
    "10 · 12 = 120 Pumpenstunden. 120 : 8 = 15. Man braucht 15 Pumpen.",
    [(6.67, "fb.verhaeltnis.falsche_richtung", "10 · 8 : 12 gerechnet (gerundet)", "10 * 8 / 12"), (14, "fb.verhaeltnis.addiert_statt_malgenommen", "12 − 8 = 4 zu 10 dazugezählt", "10 + (12 - 8)")], "Pumpen"), g="rueckwaerts", regel="rr.verhaeltnis")

# ───────── produkt ─────────
neu(T, "produkt", "lueckenweg", L(
    "Eine Tabelle gehört zu einer indirekten Proportionalität. Für x = 5 ist y = 12. Das Produkt x · y ist ①. Für x = 4 ist dann y = ②. Für x = 20 ist y = ③.",
    KOMM(3), [60, 15, 3], ["5 * 12", "{1} // 4", "{1} // 20"], ["60", "15", "3"], "Das Produkt aus x und y bleibt immer gleich. Teile es durch das neue x.",
    "5 · 12 = 60. 60 : 4 = 15. 60 : 20 = 3.",
    {0: [(17, "fb.verhaeltnis.addiert_statt_malgenommen", "5 + 12 gerechnet", "5 + 12")], 1: [(48, "fb.verhaeltnis.falsche_richtung", "12 · 4 gerechnet", "12 * 4")]}), regel="id.funktionen.zuordnung")
neu(T, "produkt", "umkehren", Z(
    "Bei einer indirekten Proportionalität ist y = 7,5, wenn x = 8 ist. Für welches x ist y = 12?",
    5, "7.5 * 8 / 12", 5, "Berechne zuerst das Produkt aus x und y.",
    "x · y = 8 · 7,5 = 60. Für y = 12 gilt x = 60 : 12 = 5. Probe: 5 · 12 = 60.",
    [(11.25, "fb.verhaeltnis.falsche_richtung", "direkt proportional gerechnet: 7,5 · 12 : 8", "7.5 * 12 / 8"), (12.8, "fb.verhaeltnis.falsche_richtung", "8 · 12 : 7,5 gerechnet", "8 * 12 / 7.5")]), g="rueckwaerts", regel="id.funktionen.zuordnung")
neu(T, "produkt", "anwenden", Z(
    "Ein Rechteck soll immer die Fläche 36 cm² haben. Die Zuordnung Breite → Länge ist dann indirekt proportional. Wie lang ist das Rechteck, wenn es 4 cm breit ist?",
    9, "36 / 4", 9, "Die Fläche ist Breite mal Länge. Sie bleibt gleich.",
    "Breite · Länge = 36. Bei 4 cm Breite: Länge = 36 : 4 = 9 cm.",
    [(32, "fb.verhaeltnis.addiert_statt_malgenommen", "36 − 4 gerechnet", "36 - 4"), (144, "fb.verhaeltnis.falsche_richtung", "36 · 4 gerechnet", "36 * 4")], "cm"), g="einkleidung", regel="id.funktionen.zuordnung")

# ───────── dreisatz ─────────
neu(T, "dreisatz", "zwei_wege", Z(
    "5 gleiche Rohre füllen einen Tank in 36 Minuten. Jedes Rohr liefert gleich viel Wasser. Wie viele Minuten brauchen 9 solche Rohre? Rechne auf zwei Wegen. Weg A: erst ausrechnen, wie lange 1 Rohr braucht. Weg B: Das Produkt aus Rohren und Minuten bleibt gleich.",
    20, "5 * 36 / 9", "180 / 9", "Beide Wege müssen dasselbe ergeben. Mehr Rohre: kürzere Zeit.",
    "Weg A: 1 Rohr braucht 5 · 36 = 180 Minuten, 9 Rohre brauchen 180 : 9 = 20 Minuten. Weg B: 5 · 36 = 180 = 9 · 20.",
    [(64.8, "fb.verhaeltnis.falsche_richtung", "direkt proportional gerechnet: 36 · 9 : 5", "36 * 9 / 5"), (40, "fb.verhaeltnis.addiert_statt_malgenommen", "36 + 4 gerechnet", "36 + 4")], "min"), regel="rr.verhaeltnis")
neu(T, "dreisatz", "anwenden", Z(
    "Ein Vorrat Hundefutter reicht für 4 Hunde genau 15 Tage. Jeder Hund bekommt jeden Tag dieselbe Menge. Nach 3 Tagen kommen 2 Hunde dazu, es sind jetzt 6 Hunde. Wie viele Tage reicht der Rest des Futters noch?",
    8, "4 * (15 - 3) / 6", 8, "Wie viel Futter ist nach 3 Tagen noch da? Rechne in „Hundetagen“.",
    "Noch da: 12 Tage für 4 Hunde, das sind 4 · 12 = 48 Hundetage. 48 : 6 = 8. Der Rest reicht noch 8 Tage.",
    [(10, None, "die 3 Tage nicht abgezogen: 60 : 6", "4 * 15 / 6"), (12, None, "die restlichen Tage ohne die neuen Hunde übernommen", "15 - 3"), (5, None, "15 : 3 gerechnet", "15 / 3")], "Tage"), g="transfer", regel="rr.verhaeltnis")
neu(T, "dreisatz", "verfahren_waehlen", W(
    "12 Arbeiter brauchen für eine Arbeit 10 Tage. Alle Arbeiter sind gleich leistungsfähig, und die Arbeit lässt sich beliebig aufteilen. Es sind aber nur 8 Arbeiter da. Welcher Weg führt zur richtigen Zahl der Tage?",
    "12 · 10 = 120 Arbeitertage, dann 120 : 8 = 15 Tage.", [("10 : 12 · 8 ≈ 6,7 Tage.", "direkt proportional gerechnet"), ("12 − 8 = 4 Arbeiter weniger, also 10 + 4 = 14 Tage.", "die Differenz statt des Produkts benutzt"), ("10 · 8 = 80 Tage.", "mit der neuen Arbeiterzahl malgenommen")],
    "Weniger Arbeiter: Die Arbeit dauert länger. Was bleibt gleich?",
    "Die gesamte Arbeit ist 12 · 10 = 120 Arbeitertage. Mit 8 Arbeitern: 120 : 8 = 15 Tage.",
    lambda: 12 * 10 / 8 == 15 and abs(10 / 12 * 8 - 6.667) < 0.01 and 14 != 15 and 80 != 15), regel="rr.verhaeltnis")

# ───────── graph ─────────
neu(T, "graph", "lueckenweg", L(
    "Im Koordinatensystem ist der Punkt P(3 | 8) eingezeichnet. Er liegt auf dem Graphen einer indirekten Proportionalität (für x > 0). Das Produkt x · y ist für jeden Punkt dieses Graphen gleich: ①. Der Graph geht durch den Punkt Q(4 | ②). Er geht auch durch den Punkt R(12 | ③).",
    KOMM(3), [24, 6, 2], ["3 * 8", "{1} // 4", "{1} // 12"], ["24", "24 // 4", "24 // 12"], "Das Produkt der Koordinaten von P gilt für alle Punkte des Graphen. Teile es durch die x-Koordinate.",
    "x · y = 3 · 8 = 24. Für Q: 24 : 4 = 6. Für R: 24 : 12 = 2. Je größer x, desto kleiner y.",
    {0: [(11, "fb.verhaeltnis.addiert_statt_malgenommen", "3 + 8 gerechnet", "3 + 8")], 1: [(32, "fb.verhaeltnis.falsche_richtung", "8 · 4 gerechnet", "8 * 4")], 2: [(96, "fb.verhaeltnis.falsche_richtung", "8 · 12 gerechnet", "8 * 12")]},
    grafik=KO([0, 13], [0, 13], punkte=[{"x": 3, "y": 8, "name": "P"}])), regel="id.funktionen.zuordnung")
neu(T, "graph", "bruecke", W(
    "Der Graph zeigt eine indirekt proportionale Zuordnung und den Punkt P(3 | 4). Welche Gleichung gehört zum Graphen?",
    "y = 12 : x", [("y = x : 12", "x und 12 vertauscht"), ("y = 12 · x", "direkt proportional gerechnet"), ("y = x + 1", "eine Gerade statt einer Hyperbel")],
    "Setze die Koordinaten von P in die Gleichungen ein. Passt mehr als eine Gleichung? Dann lies einen zweiten Punkt des Graphen ab und prüfe, ob x · y gleich bleibt.",
    "Für P(3 | 4) gilt x · y = 12. Also y = 12 : x. Probe: 12 : 3 = 4. Auch y = x + 1 geht durch P, aber der Graph geht durch den Punkt (6 | 2), und dort ist x + 1 = 7. Nur bei y = 12 : x bleibt x · y immer gleich.",
    lambda: 12 / 3 == 4 and 3 / 12 != 4 and 12 * 3 != 4 and 3 + 1 == 4 and wert_an("12/x", 6) == 2 and wert_an("x+1", 6) == 7 and wert_an("12/x", 6) != wert_an("x+1", 6),
    grafik=KO([0, 13], [0, 13], graphen=[{"art": "hyperbel", "a": 12, "b": 0, "c": 0, "name": "f"}], punkte=[{"x": 3, "y": 4, "name": "P"}])), regel="id.funktionen.zuordnung")
neu(T, "graph", "umkehren", Z(
    "Der Punkt P(4 | 6) liegt auf dem Graphen einer indirekten Proportionalität. Der Punkt Q(x | 2) liegt auf demselben Graphen. Welche x-Koordinate hat Q?",
    12, "4 * 6 / 2", 12, "Berechne das Produkt der Koordinaten von P. Es ist für jeden Punkt des Graphen gleich.",
    "x · y = 4 · 6 = 24. Für Q: x · 2 = 24, also x = 12. Probe: 12 · 2 = 24.",
    [(8, "fb.verhaeltnis.falsche_richtung", "4 · 2 gerechnet", "4 * 2"), (24, None, "das Produkt 24 nicht durch 2 geteilt", "4 * 6"), (48, "fb.verhaeltnis.falsche_richtung", "24 · 2 gerechnet", "4 * 6 * 2")]), g="umkehr", regel="id.funktionen.zuordnung")

# ───────── unterscheiden ─────────
neu(T, "unterscheiden", "fehler_detektiv", FD(
    "Kim ordnet eine Taxifahrt ein. Der Preis besteht aus 3 € Grundgebühr und 2 € je Kilometer. 2 km kosten 7 €, 4 km kosten 11 €.",
    [("Wenn die Strecke größer wird, wird auch der Preis größer. Also ist die Zuordnung direkt proportional.", 11 == 2 * 7), ("Dann kosten 8 km das Vierfache von 2 km: 4 · 7 = 28 €.", 4 * 7 == 28), ("Die Fahrt von 8 km kostet 28 €.", True)],
    "Reicht „mehr gibt mehr“ für direkte Proportionalität? Prüfe: Kosten 4 km doppelt so viel wie 2 km?",
    "Direkt proportional heißt: doppelte Strecke, doppelter Preis. Hier ist 11 € nicht 14 €. Die Zuordnung ist nicht proportional. 8 km kosten 3 + 16 = 19 €."), regel="id.funktionen.zuordnung")
neu(T, "unterscheiden", "verfahren_waehlen", W(
    "Wie prüfst du sicher, ob eine Wertetabelle zu einer indirekten Proportionalität gehört?",
    "Alle Produkte x · y müssen gleich sein.", [("Es reicht, dass y kleiner wird, wenn x größer wird.", "„wird kleiner“ reicht nicht"), ("Alle Quotienten y : x müssen gleich sein.", "die Prüfung für direkte Proportionalität benutzt"), ("Alle Summen x + y müssen gleich sein.", "die Summe statt des Produkts geprüft")],
    "Denke an die Helfer-Aufgabe: Doppelt so viele Helfer, halb so lange. Was bleibt gleich?",
    "Bei einer indirekten Proportionalität ist x · y immer derselbe Wert. „Wird kleiner“ gilt auch für andere Zuordnungen, zum Beispiel y = 20 − x.",
    lambda: 2 * 12 == 4 * 6 and (10 - 2) + 0 == 8 and (20 - 2) + 2 == (20 - 4) + 4 and 2 * (20 - 2) != 4 * (20 - 4)), g="erkennen", regel="id.funktionen.zuordnung")
neu(T, "unterscheiden", "bruecke", W(
    "Die Tabelle zeigt, wie viel verschiedene Mengen Äpfel kosten. Welche Zuordnung passt?",
    "Direkt proportional: Der Quotient Preis : Menge ist immer 2,5.", [("Indirekt proportional: Der Preis wird größer.", "„wird größer“ mit „indirekt“ verwechselt"), ("Indirekt proportional: Das Produkt ist immer gleich.", "Produkt statt Quotient geprüft"), ("Weder noch, weil die Zahlen verschieden sind.", "Verschiedenheit der Zahlen als Ausschluss gelesen")],
    "Prüfe Quotient und Produkt in jeder Spalte.",
    "5 : 2 = 2,5; 10 : 4 = 2,5; 15 : 6 = 2,5. Der Quotient ist immer gleich, also direkt proportional. Die Produkte 10, 40, 90 sind verschieden.",
    lambda: F(5, 2) == F(10, 4) == F(15, 6) == F(5, 2) and len({2 * 5, 4 * 10, 6 * 15}) == 3,
    grafik=TAB(["Menge in kg", "2", "4", "6"], ["Preis in €", "5", "10", "15"])), regel="id.funktionen.zuordnung")

# ───────── sach ─────────
neu(T, "sach", "anwenden", Z(
    "Die Miete für eine Hütte wird gleichmäßig auf alle Personen verteilt, die Gesamtmiete bleibt gleich. Bei 8 Personen zahlt jede Person 45 €. Zwei Personen sagen ab. Wie viel Euro muss jede der übrigen Personen zahlen?",
    60, "8 * 45 / 6", 60, "Wie hoch ist die gesamte Miete? Sie ändert sich nicht.",
    "Gesamtmiete: 8 · 45 = 360 €. Jetzt 6 Personen: 360 : 6 = 60 €.",
    [(47, "fb.verhaeltnis.addiert_statt_malgenommen", "45 + 2 gerechnet", "45 + 2"), (33.75, "fb.verhaeltnis.falsche_richtung", "45 · 6 : 8 gerechnet", "45 * 6 / 8")], "€"), g="einkleidung", regel="rr.verhaeltnis")
neu(T, "sach", "anwenden", Z(
    "Zwei gleiche Pumpen füllen ein Becken in 9 Stunden. Jede Pumpe fördert gleichmäßig. Nach 3 Stunden fällt eine Pumpe aus. Die andere pumpt allein weiter. Wie viele Stunden dauert das Füllen insgesamt?",
    15, "3 + (2 * 9 - 2 * 3) / 1", 15, "Rechne in Pumpenstunden: Wie viel ist insgesamt nötig, wie viel ist nach 3 Stunden getan?",
    "Insgesamt nötig: 2 · 9 = 18 Pumpenstunden. Nach 3 Stunden: 2 · 3 = 6 getan. Rest: 12 Pumpenstunden mit einer Pumpe: 12 Stunden. Insgesamt 3 + 12 = 15 Stunden.",
    [(12, None, "nur die restliche Zeit angegeben", "(2 * 9 - 2 * 3) / 1"), (18, None, "doppelte Zeit für eine Pumpe, ohne die ersten 3 Stunden zu berücksichtigen", "2 * 9"), (13.5, None, "9 + 4,5 gerechnet", "9 + 9 / 2")], "Stunden"), g="transfer", regel="rr.verhaeltnis")
neu(T, "sach", "zwei_wege", Z(
    "Ein Futtervorrat reicht für 15 Schafe 24 Tage. Jedes Schaf frisst jeden Tag dieselbe Menge. Wie viele Tage reicht er für 20 Schafe? Rechne auf zwei Wegen. Weg A: Der Vorrat ist 15 · 24 „Schaftage“; teile durch 20. Weg B: Die Schafzahl wird mit 20/15 malgenommen, die Tage mit 15/20.",
    18, "15 * 24 / 20", "24 * 15 / 20", "Beide Wege müssen dasselbe ergeben. Mehr Schafe: weniger Tage.",
    "Weg A: 15 · 24 = 360 Schaftage, 360 : 20 = 18 Tage. Weg B: 24 · 3/4 = 18 Tage.",
    [(32, "fb.verhaeltnis.falsche_richtung", "direkt proportional gerechnet: 24 · 20 : 15", "24 * 20 / 15"), (19, "fb.verhaeltnis.addiert_statt_malgenommen", "24 − 5 gerechnet", "24 - 5")], "Tage"), regel="rr.verhaeltnis")
