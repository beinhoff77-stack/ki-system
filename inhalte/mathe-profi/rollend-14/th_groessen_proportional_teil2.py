T = "groessen.proportional_teil2"
# ───────── erkennen ─────────
a1(T, "erkennen", Z(
    "Ein Aufzug fährt gleichmäßig schnell. In 4 Sekunden fährt er 10 m. Wie viele Meter fährt er in 10 Sekunden?",
    25, "10 / 4 * 10", "10 * 2.5", "Proportional heißt: Zur doppelten Zeit gehört die doppelte Strecke. Wie weit fährt der Aufzug in 1 Sekunde?",
    "In 1 Sekunde fährt er 10 : 4 = 2,5 m. In 10 Sekunden fährt er 10 · 2,5 = 25 m. Probe: In 8 Sekunden wären es 20 m, dazu noch 2 Sekunden mit 5 m.",
    [B("10 + (10 - 4)", "die Sekunden dazugezählt: 6 Sekunden mehr, also 6 Meter mehr"), B("10 / 4", "nur die Strecke in einer Sekunde angegeben"), B("10 * 10", "die Strecke mit der Zeit malgenommen")], "m"))
a2(T, "erkennen", Z(
    "Bäckerei A: 6 Brötchen kosten 2,40 €, jedes Brötchen kostet gleich viel. Bäckerei B: 1 € Tütengebühr und dazu 0,30 € für jedes Brötchen. Bei einer der beiden Bäckereien ist die Zuordnung Anzahl → Preis proportional. Wie viel Euro kosten dort 12 Brötchen?",
    4.8, "2.4 / 6 * 12", "2.4 * 2", "Bei einer proportionalen Zuordnung gehört zu 0 Brötchen der Preis 0. Bei welcher Bäckerei ist das so?",
    "Bei Bäckerei B kostet schon die Tüte 1 €, auch bei 0 Brötchen: Das ist nicht proportional. Bei Bäckerei A kostet ein Brötchen 2,40 : 6 = 0,40 €. 12 Brötchen kosten 12 · 0,40 = 4,80 €. Das ist das Doppelte von 2,40 €.",
    [B("1 + 0.3 * 12", "den Preis der Bäckerei B berechnet, die nicht proportional ist"), B("2.4 + 6", "6 Brötchen dazugezählt und 6 € addiert"), B("2.4 / 6", "nur den Preis eines Brötchens angegeben")], "€"))
a3(T, "erkennen", Z(
    "Sam behauptet: „Die Zuordnung Alter → Körpergröße ist proportional.“ Mit 8 Jahren war Sam 128 cm groß, mit 12 Jahren ist Sam 152 cm groß. Sam rechnet vom Wert bei 8 Jahren proportional weiter und sagt voraus, wie groß er mit 20 Jahren wäre. Um wie viele Zentimeter ist diese Vorhersage größer als eine realistische Größe von 180 cm?",
    140, "128 / 8 * 20 - 180", "320 - 180", "Berechne zuerst, wie viele Zentimeter Sam bei 8 Jahren je Lebensjahr hat. Dann rechnest du auf 20 Jahre hoch und vergleichst.",
    "Bei Proportionalität: 128 : 8 = 16 cm je Jahr. Mit 20 Jahren wären es 16 · 20 = 320 cm. Das sind 320 − 180 = 140 cm mehr als realistisch. Die Annahme stimmt nicht: Schon bei 12 Jahren wären es 192 cm statt 152 cm.",
    [B("128 / 8 * 20", "die proportionale Größe als Unterschied angegeben"), B("180 - 128", "den Unterschied zu 128 cm statt zur Vorhersage berechnet"), B("152 - 128", "das tatsächliche Wachstum bis 12 Jahre angegeben")], "cm"), g="pruefung")
# ───────── vervielfachen ─────────
a1(T, "vervielfachen", Z(
    "Bei einem Bäcker kosten 4 Brezeln zusammen 5 €. Wie viele Brezeln bekommt man für 35 €?",
    28, "35 * 4 / 5", "(35 / 5) * 4", "Wie oft passen 5 € in 35 €? So oft bekommst du 4 Brezeln.",
    "5 € ergeben 4 Brezeln. 35 € sind 7 mal 5 €, also bekommt man 7 · 4 = 28 Brezeln.",
    [B("35 * 5 / 4", "mit dem Kehrwert des richtigen Faktors gerechnet"), B("35 * 4", "die Euro mit 4 malgenommen"), B("35 - 1", "den Unterschied 1 zwischen 5 und 4 abgezogen")], "Brezeln"))
a2(T, "vervielfachen", Z(
    "Ein Wanderer legt gleichmäßig 12 km in 3 Stunden zurück. Wie viele Minuten braucht er für 5 km?",
    75, "5 * 3 * 60 / 12", "75", "Wie viele Kilometer schafft er in 1 Stunde? Wie viele Minuten braucht er dann für 1 km?",
    "In 3 Stunden sind es 12 km, also 4 km in einer Stunde (60 Minuten). Für 1 km braucht er 60 : 4 = 15 Minuten, für 5 km also 5 · 15 = 75 Minuten.",
    [B("5 * 3 / 12", "das Ergebnis in Stunden statt in Minuten angegeben"), B("5 * 12 / 3", "5 mit den 4 km je Stunde malgenommen"), B("5 * 3 * 60", "nicht durch 12 geteilt")], "Minuten"))
a3(T, "vervielfachen", Z(
    "Ein Rezept für 8 Personen braucht 600 g Mehl und 300 ml Milch. Zu Hause sind 1,5 kg Mehl und 600 ml Milch da. Für wie viele Personen reichen die Zutaten höchstens, wenn man nach dem Rezept kocht?",
    16, "600 / 300 * 8", "min(1500 / 600 * 8, 600 / 300 * 8)", "Berechne getrennt, für wie viele Personen das Mehl und für wie viele die Milch reicht. Was begrenzt?",
    "Mehl: 1 500 g : 600 g = 2,5 Rezepte, also 2,5 · 8 = 20 Personen. Milch: 600 ml : 300 ml = 2 Rezepte, also 2 · 8 = 16 Personen. Die Milch reicht nur für 16 Personen, sie begrenzt.",
    [B("1500 / 600 * 8", "nur das Mehl berücksichtigt"), B("20 + 16", "die beiden Personenzahlen addiert"), B("600 / 300", "nur die Zahl der Rezepte für die Milch angegeben")], "Personen"), g="verknuepfen")
# ───────── pruefen ─────────
a1(T, "pruefen", Z(
    "Kim zahlt für 2 kg Birnen 5 €, für 3 kg Birnen 7,50 € und für 5 kg Birnen 12,50 €. Kim möchte wissen, was 8 kg Birnen kosten, wenn sich der Preis weiter in dieser Weise ändert. Wie viel Euro kosten 8 kg Birnen?",
    20, "5 / 2 * 8", "7.5 + 12.5", "Prüfe mit Preis : Gewicht in jeder Spalte, ob immer dieselbe Zahl herauskommt. Dann rechnest du weiter.",
    "5 : 2 = 2,5; 7,5 : 3 = 2,5; 12,5 : 5 = 2,5. Immer 2,50 € je kg, die Tabelle ist proportional. 8 kg kosten 8 · 2,5 = 20 €. Probe: 3 kg + 5 kg: 7,50 + 12,50 = 20.",
    [B("12.5 + 8", "8 € zum Preis von 5 kg addiert"), B("5 * 8", "die 5 € mit 8 malgenommen"), B("2.5 * 8 + 5", "5 € Grundpreis dazugezählt")], "€"))
a2(T, "pruefen", Z(
    "Alle Paare einer Tabelle gehören zu einer proportionalen Zuordnung, nur ein Wert wurde falsch eingetragen: (4 | 18), (6 | 27), (10 | 46). Welche Zahl müsste statt 46 stehen?",
    45, "18 / 4 * 10", "27 / 6 * 10", "Rechne in jeder Spalte zweite Zahl : erste Zahl. Welche Zahl kommt zweimal heraus?",
    "18 : 4 = 4,5 und 27 : 6 = 4,5. Der Faktor ist 4,5. Bei 10 müsste 4,5 · 10 = 45 stehen, nicht 46. Probe: 46 : 10 = 4,6, das passt nicht zu 4,5.",
    [B("27 + 10", "10 zum Wert 27 addiert"), B("10 * 4", "mit 4 statt mit 4,5 malgenommen"), B("10 * 6", "10 mit 6 malgenommen")]))
a3(T, "pruefen", Z(
    "Eine Tabelle zeigt, wie viel Benzin ein Motorroller auf verschiedenen Strecken verbraucht: 40 km → 1 l; 60 km → 1,5 l; 100 km → 2,5 l. Wie viele Kilometer kommt der Roller mit 7,5 Litern, wenn der Verbrauch weiter in dieser Weise zunimmt?",
    300, "7.5 / (1.5 / 60)", "7.5 * 40", "Prüfe, ob in jeder Spalte Liter : Kilometer dieselbe Zahl ergibt. Wie viele Kilometer fährt der Roller mit einem Liter? Dann rechnest du mit 7,5 Litern.",
    "1 : 40 = 0,025; 1,5 : 60 = 0,025; 2,5 : 100 = 0,025. Es sind immer 0,025 l je km, die Zuordnung ist proportional. Mit 1 l kommt der Roller 40 km weit, mit 7,5 l also 7,5 · 40 = 300 km.",
    [B("7.5 * 1.5", "mit 1,5 malgenommen statt mit der Strecke je Liter"), B("7.5 * 100", "die Strecke für einen Liter als 100 km angenommen"), B("7.5 + 40", "40 km zu den Litern addiert")], "km"), g="pruefung")