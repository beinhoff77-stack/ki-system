T = "groessen.proportional_teil2"
# ───────── erkennen ─────────
a1(T, "erkennen", Z(
    "Ein Aufzug fährt gleichmäßig schnell. In 4 Sekunden fährt er 10 m. Die Zuordnung Zeit → Strecke ist proportional. Wie viele Meter fährt er in 10 Sekunden?",
    25, "10 / 4 * 10", "10 * 2.5", "Proportional heißt: Zur doppelten Zeit gehört die doppelte Strecke. Wie weit fährt der Aufzug in 1 Sekunde?",
    "In 1 Sekunde fährt er 10 : 4 = 2,5 m. In 10 Sekunden fährt er 10 · 2,5 = 25 m. Probe: In 8 Sekunden wären es 20 m, dazu noch 2 Sekunden mit 5 m.",
    [B("10 + (10 - 4)", "die Sekunden dazugezählt: 6 Sekunden mehr, also 6 Meter mehr"), B("10 / 4", "nur die Strecke in einer Sekunde angegeben"), B("10 * 10", "die Strecke mit der Zeit malgenommen")], "m"))
a2(T, "erkennen", Z(
    "Bäckerei A: 6 Brötchen kosten 2,40 €, jedes Brötchen kostet gleich viel. Bäckerei B: 1 € Tütengebühr und dazu 0,30 € für jedes Brötchen. Bei einer der beiden Bäckereien ist die Zuordnung Anzahl → Preis proportional. Wie viel Euro kosten dort 12 Brötchen?",
    4.8, "2.4 / 6 * 12", "2.4 * 2", "Bei einer proportionalen Zuordnung gehört zu 0 Brötchen der Preis 0. Bei welcher Bäckerei ist das so?",
    "Bei Bäckerei B kostet schon die Tüte 1 €, auch bei 0 Brötchen: Das ist nicht proportional. Bei Bäckerei A kostet ein Brötchen 2,40 : 6 = 0,40 €. 12 Brötchen kosten 12 · 0,40 = 4,80 €. Das ist das Doppelte von 2,40 €.",
    [B("1 + 0.3 * 12", "den Preis der Bäckerei B berechnet, die nicht proportional ist"), B("2.4 + 6", "6 Brötchen dazugezählt und 6 € addiert"), B("2.4 / 6", "nur den Preis eines Brötchens angegeben")], "€"))
a3(T, "erkennen", Z(
    "Sam behauptet: „Die Zuordnung Alter → Körpergröße ist proportional. Mit 8 Jahren war ich 128 cm groß, mit 12 Jahren bin ich also 192 cm groß.“ Mit 12 Jahren ist Sam aber 152 cm groß. Um wie viele Zentimeter weicht der Wert, den die Proportionalität liefert, vom wirklichen Wert ab?",
    40, "128 / 8 * 12 - 152", "192 - 152", "Berechne zuerst, welche Größe bei Proportionalität für 12 Jahre herauskäme. Vergleiche mit 152 cm.",
    "Bei Proportionalität wären es 128 : 8 = 16 cm je Jahr und mit 12 Jahren 16 · 12 = 192 cm. Wirklich sind es 152 cm. Abweichung: 192 − 152 = 40 cm. Das Wachstum ist nicht proportional (zu 0 Jahren gehört nicht 0 cm).",
    [B("152 - 128", "das tatsächliche Wachstum angegeben"), B("128 / 8 * 12", "die proportionale Größe als Abweichung angegeben"), B("192 - 128", "das Wachstum nach Sams Rechnung angegeben")], "cm"), g="pruefung")
# ───────── vervielfachen ─────────
a1(T, "vervielfachen", Z(
    "Ein Auto verbraucht auf 100 km genau 6 Liter Benzin. Der Verbrauch ist auf jedem Kilometer gleich. Wie viele Liter Benzin verbraucht es auf 350 km?",
    21, "6 * 350 / 100", "6 * 3 + 3", "Wie viele Liter sind es auf 50 km? Zerlege 350 km in 300 km und 50 km.",
    "300 km sind 3 · 100 km: 3 · 6 = 18 Liter. 50 km sind die Hälfte von 100 km: 3 Liter. Zusammen 18 + 3 = 21 Liter.",
    [B("6 * 3", "nur 300 km gerechnet"), B("6 * 350", "den Verbrauch mit 350 malgenommen"), B("6 + 250", "250 km dazugezählt und 250 Liter addiert")], "l"))
a2(T, "vervielfachen", Z(
    "Ein Wasserhahn füllt gleichmäßig 18 Liter in 4 Minuten. Wie viele Minuten braucht er, um 63 Liter einzufüllen?",
    14, "63 / 18 * 4", "63 / 4.5", "Wie viele Liter fließen in 1 Minute? Wie oft passt das in 63 Liter? Oder: Wie viele Liter sind es in 2 Minuten?",
    "In 4 Minuten fließen 18 Liter, in 1 Minute 18 : 4 = 4,5 Liter. 63 : 4,5 = 14 Minuten. Probe: 14 · 4,5 = 63.",
    [B("63 / 18", "die Zahl 63 : 18 als Minuten angegeben"), B("63 - 18 + 4", "die Liter-Differenz zur Zeit addiert"), B("18 / 4 * 63", "mit 63 malgenommen statt geteilt")], "Minuten"))
a3(T, "vervielfachen", Z(
    "Ein Rezept für 8 Personen braucht 600 g Mehl und 300 ml Milch. Zu Hause sind 1,5 kg Mehl und 600 ml Milch da. Für wie viele Personen reichen die Zutaten höchstens, wenn man nach dem Rezept kocht?",
    16, "600 / 300 * 8", "min(1500 / 600 * 8, 600 / 300 * 8)", "Berechne getrennt, für wie viele Personen das Mehl und für wie viele die Milch reicht. Was begrenzt?",
    "Mehl: 1 500 g : 600 g = 2,5 Rezepte, also 2,5 · 8 = 20 Personen. Milch: 600 ml : 300 ml = 2 Rezepte, also 2 · 8 = 16 Personen. Die Milch reicht nur für 16 Personen, sie begrenzt.",
    [B("1500 / 600 * 8", "nur das Mehl berücksichtigt"), B("20 + 16", "die beiden Personenzahlen addiert"), B("600 / 300", "nur die Zahl der Rezepte für die Milch angegeben")], "Personen"), g="verknuepfen")
# ───────── pruefen ─────────
a1(T, "pruefen", Z(
    "Kim zahlt für 2 kg Birnen 5 €, für 3 kg Birnen 7,50 € und für 5 kg Birnen 12,50 €. Die Zuordnung Gewicht → Preis ist proportional. Wie viel Euro kosten 8 kg Birnen?",
    20, "5 / 2 * 8", "7.5 + 12.5", "Prüfe mit Preis : Gewicht in jeder Spalte, ob immer dieselbe Zahl herauskommt. Dann rechnest du weiter.",
    "5 : 2 = 2,5; 7,5 : 3 = 2,5; 12,5 : 5 = 2,5. Immer 2,50 € je kg, die Tabelle ist proportional. 8 kg kosten 8 · 2,5 = 20 €. Probe: 3 kg + 5 kg: 7,50 + 12,50 = 20.",
    [B("12.5 + 8", "8 € zum Preis von 5 kg addiert"), B("5 * 8", "die 5 € mit 8 malgenommen"), B("2.5 * 8 + 5", "5 € Grundpreis dazugezählt")], "€"))
a2(T, "pruefen", Z(
    "Alle Paare einer Tabelle gehören zu einer proportionalen Zuordnung, nur ein Wert wurde falsch eingetragen: (3 | 12), (5 | 20), (8 | 34). Welche Zahl müsste statt 34 stehen?",
    32, "12 / 3 * 8", "20 / 5 * 8", "Rechne in jeder Spalte zweite Zahl : erste Zahl. Welche Zahl kommt zweimal heraus?",
    "12 : 3 = 4 und 20 : 5 = 4. Der Faktor ist 4. Bei 8 müsste 4 · 8 = 32 stehen, nicht 34. Probe: 34 : 8 = 4,25, das passt nicht zu 4.",
    [B("20 + 8", "8 zum Wert 20 addiert"), B("12 * 2", "den Wert 12 verdoppelt"), B("8 * 5", "8 mit 5 malgenommen")]))
a3(T, "pruefen", Z(
    "Eine Tabelle zeigt, wie viel Benzin ein Moped auf verschiedenen Strecken verbraucht: 15 km → 1,2 l; 24 km → 1,92 l; 33 km → 2,64 l. Die Zuordnung ist proportional. Wie viel Liter verbraucht das Moped auf 250 km?",
    20, "250 * 1.2 / 15", "250 * 0.08", "Prüfe, ob in jeder Spalte Liter : Kilometer dieselbe Zahl ergibt. Dann rechnest du den Verbrauch für 250 km.",
    "1,2 : 15 = 0,08; 1,92 : 24 = 0,08; 2,64 : 33 = 0,08. Es sind immer 0,08 l je km, die Zuordnung ist proportional. 250 km: 250 · 0,08 = 20 l.",
    [B("1.2 * 250", "den Verbrauch für 15 km mit 250 malgenommen"), B("250 * 8", "den Verbrauch je km mit 8 statt 0,08 gerechnet"), B("250 / 15", "die Strecke durch 15 geteilt")], "l"), g="pruefung")
