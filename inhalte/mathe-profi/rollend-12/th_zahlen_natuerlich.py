T = "zahlen.natuerlich"
SW, ZG, BU = "rr.stellenwert", "id.zahlen.zahlengerade", "id.zahlen.buendeln"

# ───────── stellenwert ─────────
neu(T, "stellenwert", "zwei_wege", Z(
    "Weg A: Teile die Zahl durch 10. Weg B: Zähle zusammen, wie viele Zehner in den Tausendern, in den Hundertern und in den Zehnern stecken. Wie viele Zehner stecken insgesamt in der Zahl 4 560?",
    456, "4560 / 10", "400 + 50 + 6", "Ein Tausender besteht aus vielen Zehnern. Wie viele sind es?",
    "Weg A: 4 560 : 10 = 456. Weg B: 4 Tausender sind 400 Zehner, 5 Hunderter sind 50 Zehner, dazu 6 Zehner: 400 + 50 + 6 = 456. Beide Wege geben 456 Zehner.",
    [(45, None, "nur die 45 vollen Hunderter gezählt, den Rest 60 weggelassen", "4560 // 100"), (56, None, "nur die Zehner aus den Hundertern und den Zehnern gezählt: 50 + 6", "50 + 6"), (6, None, "nur die Ziffer an der Zehnerstelle genommen", "6")], "Zehner"), regel=SW)
neu(T, "stellenwert", "umkehren", Z(
    "Ein Zähler wurde um 4 Tausender und 5 Zehner erhöht. Jetzt zeigt er 12 078. Welche Zahl zeigte er vorher?",
    8028, "12078 - 4000 - 50", "12078 - 4050", "Gehe den Weg rückwärts: Was musst du von der neuen Zahl wieder wegnehmen?",
    "Erhöht wurde um 4 000 + 50 = 4 050. Rückwärts wird abgezogen: 12 078 − 4 050 = 8 028. Probe: 8 028 + 4 050 = 12 078.",
    [(16128, None, "addiert statt abgezogen: 12 078 + 4 050", "12078 + 4050"), (8078, None, "nur die 4 Tausender abgezogen, die Zehner vergessen", "12078 - 4000"), (7578, None, "die 5 Zehner als 5 Hunderter abgezogen", "12078 - 4000 - 500")]), g="rueckwaerts", regel=SW)

# ───────── zahlwort_zu_ziffern ─────────
neu(T, "zahlwort_zu_ziffern", "zwei_wege", Z(
    "Die Zahl lautet „dreihundertzwölf Millionen vierzigtausend“. Weg A: Schreibe die ganze Zahl mit Ziffern hin und lies die Stelle ab. Weg B: Suche im Zahlwort den Teil, der die Zehntausender enthält, und lies dort die Ziffer ab. Welche Ziffer steht an der Zehntausenderstelle?",
    4, "312040000 // 10000 % 10", "40000 // 10000", "Die Zehntausenderstelle ist die fünfte Stelle von rechts. Welcher Teil des Zahlworts liefert sie?",
    "Weg A: 312 040 000, von rechts gezählt: Einer 0, Zehner 0, Hunderter 0, Tausender 0, Zehntausender 4. Weg B: Die Millionen reichen nur bis zur Millionenstelle; „vierzigtausend“ ist 40 000 und hat 4 Zehntausender.",
    [(0, None, "die Hunderttausenderstelle abgelesen", "312040000 // 100000 % 10"), (2, None, "die Millionenstelle abgelesen", "312040000 // 1000000 % 10"), (3, None, "die erste Ziffer der Zahl genommen", "312040000 // 100000000")], "Ziffer"))
_NN = [2030000, 200000003, 20003000, 200030]
neu(T, "zahlwort_zu_ziffern", "bruecke", W(
    "Vier Zahlen sind als Zahlwort angegeben. Schreibe sie in Ziffern. Welches Zahlwort gehört zu der Zahl, die in Ziffern geschrieben die meisten Nullen hat?",
    "zweihundert Millionen drei",
    [("zwei Millionen dreißigtausend", "Das sind 2 030 000 mit fünf Nullen."), ("zwanzig Millionen dreitausend", "Das sind 20 003 000 mit sechs Nullen."), ("zweihunderttausenddreißig", "Das sind 200 030 mit vier Nullen.")],
    "Schreibe zuerst jede Zahl mit Ziffern. Zähle dann die Nullen.",
    "„zweihundert Millionen drei“ ist 200 000 003 mit sieben Nullen. 2 030 000 hat fünf, 20 003 000 hat sechs, 200 030 hat vier Nullen.",
    lambda: all(zahlwort(n) == s for n, s in zip(_NN, ["zwei Millionen dreißigtausend", "zweihundert Millionen drei", "zwanzig Millionen dreitausend", "zweihunderttausenddreißig"])) and [str(n).count("0") for n in _NN] == [5, 7, 6, 4]), g="verknuepfen")

# ───────── ziffern_zu_zahlwort ─────────
neu(T, "ziffern_zu_zahlwort", "anwenden", W(
    "Ein Verein erhält eine Spende von 40 306 Euro. Der Betrag soll auf der Quittung in Worten stehen. Welche Schreibweise ist richtig?",
    "vierzigtausenddreihundertsechs Euro",
    [("vierzigtausenddreihundertsechzig Euro", "Das ist 40 360 Euro."), ("viertausenddreihundertsechs Euro", "Das ist 4 306 Euro."), ("dreiundvierzigtausendsechs Euro", "Das ist 43 006 Euro.")],
    "Lies die Zahl in Gruppen: erst die Tausender, dann Hunderter, Zehner und Einer. Eine Null bleibt stumm.",
    "40 306 hat 40 Tausender und 306 Einer: „vierzigtausend“ und „dreihundertsechs“, zusammen „vierzigtausenddreihundertsechs“.",
    lambda: zahlwort(40306) == "vierzigtausenddreihundertsechs" and zahlwort(40360) == "vierzigtausenddreihundertsechzig" and zahlwort(4306) == "viertausenddreihundertsechs" and zahlwort(43006) == "dreiundvierzigtausendsechs"))
neu(T, "ziffern_zu_zahlwort", "fehler_detektiv", FD(
    "Tim schreibt die Zahl 70 305 in Worten.",
    [("70 305 hat 7 Zehntausender, 0 Tausender, 3 Hunderter, 0 Zehner und 5 Einer.", [70305 // 10000 % 10, 70305 // 1000 % 10, 70305 // 100 % 10, 70305 // 10 % 10, 70305 % 10] == [7, 0, 3, 0, 5], True, "Zeile 1 stimmt: Die Ziffern 7, 0, 3, 0, 5 gehören zu den genannten Stellen. Der Fehler steckt später."),
     ("7 Zehntausender sind siebzigtausend.", 7 * 10000 == 70000, True, "Zeile 2 stimmt: 7 · 10 000 = 70 000. Der Fehler steckt später."),
     ("3 Hunderter und 5 Einer sind dreihundertfünfzig.", 3 * 100 + 5 == 350, True),
     ("Zusammen heißt die Zahl siebzigtausenddreihundertfünfzig.", False, True, "Zeile 4 übernimmt nur das falsche Wort aus Zeile 3. Der Fehler liegt schon davor.")],
    "Prüfe jede Zeile für sich und schreibe die Zahl selbst in Worten auf. Welche Aussage stimmt zum ersten Mal nicht?",
    "3 Hunderter und 5 Einer sind 305, also „dreihundertfünf“ (die Zehnerstelle ist leer). Richtig: siebzigtausenddreihundertfünf. Der erste Fehler steht in Zeile 3."))

# ───────── strahl_ablesen ─────────
neu(T, "strahl_ablesen", "zwei_wege", Z(
    "Auf einem Zahlenstrahl sind die Marken 4 000 und 5 000 beschriftet. Zwischen ihnen liegen 10 gleich große Abschnitte. Ein Pfeil steht nach dem 7. Abschnitt, von 4 000 aus gezählt. Weg A: Bestimme die Länge eines Abschnitts und zähle von 4 000 aus vor. Weg B: Zähle von 5 000 aus zurück. Welche Zahl zeigt der Pfeil?",
    4700, "4000 + 7 * ((5000 - 4000) / 10)", "5000 - 3 * 100", "Wie viele Abschnitte liegen zwischen dem Pfeil und der Marke 5 000?",
    "Ein Abschnitt ist (5 000 − 4 000) : 10 = 100 lang. Weg A: 4 000 + 7 · 100 = 4 700. Weg B: Bis 5 000 sind es noch 3 Abschnitte: 5 000 − 3 · 100 = 4 700.",
    [(4007, None, "nur 7 addiert statt 7 Abschnitte mit je 100", "4000 + 7"), (4070, None, "den Abschnitt mit 10 statt mit 100 gerechnet", "4000 + 7 * 10"), (4300, None, "7 Abschnitte von 5 000 aus zurückgezählt", "5000 - 7 * 100")]), regel=ZG)
neu(T, "strahl_ablesen", "umkehren", Z(
    "Auf einem Zahlenstrahl ist die Marke 1 450 beschriftet. Ein Pfeil zeigt auf die Zahl 1 585. Er steht auf dem 3. Strich rechts von der Marke 1 450. Alle Striche haben gleichen Abstand. Welche Zahl gehört zum 4. Strich rechts von 1 450?",
    1630, "1585 + (1585 - 1450) / 3", "1450 + 4 * 45", "Was weißt du über den Abstand zweier Striche? Wie kannst du ihn aus den Angaben bestimmen?",
    "Von 1 450 bis 1 585 sind es 135 in 3 Abschnitten, ein Abschnitt ist also 135 : 3 = 45 lang. Der 4. Strich liegt einen Abschnitt hinter dem Pfeil: 1 585 + 45 = 1 630. Probe: 1 450 + 4 · 45 = 1 630.",
    [(45, None, "nur den Abstand zweier Striche angegeben", "(1585 - 1450) / 3"), (1495, None, "den 1. Strich statt des 4. Strichs genannt", "1450 + 45"), (1720, None, "den ganzen Abstand von 135 statt eines Abschnitts addiert", "1585 + (1585 - 1450)")]), g="rueckwaerts", regel=ZG)

# ───────── strahl_eintragen ─────────
neu(T, "strahl_eintragen", "bruecke", Z(
    "Ein Zahlenstrahl beginnt bei 0 und endet bei 600. Er ist in 12 gleich große Abschnitte geteilt. Die Zahl 350 soll eingetragen werden. Nach wie vielen Abschnitten, von 0 aus gezählt, liegt sie?",
    7, "350 / (600 / 12)", "350 / 50", "Wie lang ist ein Abschnitt in Zahlen?",
    "Ein Abschnitt ist 600 : 12 = 50 lang. 350 : 50 = 7. Die Zahl 350 liegt nach 7 Abschnitten.",
    [(3.5, None, "durch 100 statt durch die Länge eines Abschnitts geteilt", "350 / 100"), (5, None, "mit einem Abschnitt von 70 gerechnet", "350 / 70"), (12, None, "die Zahl der Abschnitte des ganzen Strahls angegeben", "600 / 50")], "Abschnitte"), regel=ZG)
neu(T, "strahl_eintragen", "fehler_detektiv", FD(
    "Ein Zahlenstrahl geht von 0 bis 400 und ist in 8 gleiche Abschnitte geteilt. Mia will die Zahl 250 eintragen.",
    [("Ein Abschnitt ist 400 : 8 = 40 lang.", 400 / 8 == 40, True),
     ("Es gilt 250 : 40 = 6 Rest 10.", 250 // 40 == 6 and 250 % 40 == 10, True, "Zeile 2 ist für sich richtig gerechnet (6 · 40 + 10 = 250). Sie benutzt aber schon die falsche Abschnittslänge aus Zeile 1."),
     ("Die Marke liegt also 6 Abschnitte und noch ein Stück rechts von der 0.", True, True, "Zeile 3 folgt richtig aus Zeile 2. Der Fehler liegt schon in Zeile 1.")],
    "Prüfe jede Zeile für sich und mache bei den Rechnungen die Gegenprobe. Welche Aussage stimmt zum ersten Mal nicht?",
    "400 : 8 = 50, nicht 40 (8 · 40 = 320). Richtig: ein Abschnitt ist 50 lang, 250 : 50 = 5, die Marke 250 liegt genau 5 Abschnitte von der 0 entfernt. Der erste Fehler steht in Zeile 1."), regel=ZG)

# ───────── vergleichen ─────────
neu(T, "vergleichen", "bruecke", Z(
    "Die Tabelle zeigt, wie viele Einwohner vier Orte haben. Wie viele Einwohner hat der Ort mit der drittgrößten Einwohnerzahl?",
    48305, "48305", "48000 + 305", "Ordne die vier Zahlen der Größe nach. Beginne mit der größten.",
    "Der Größe nach: 84 053 > 48 350 > 48 305 > 40 835. Die drittgrößte Zahl ist 48 305.",
    [(48350, None, "die zweitgrößte statt der drittgrößten Zahl genommen", "48350"), (40835, None, "die kleinste Zahl genommen", "40835")], "Einwohner",
    grafik=TAB(["Ort", "Einwohner"], ["Altbach", "48 305"], ["Bergau", "48 350"], ["Clausen", "40 835"], ["Dorfen", "84 053"])))
neu(T, "vergleichen", "anwenden", Z(
    "In der Schulbücherei stehen vier Regale. Sie enthalten 1 205, 1 250, 1 052 und 1 502 Bücher. Wie viele Bücher mehr stehen im vollsten Regal als im leersten?",
    450, "1502 - 1052", "1502 - 1000 - 52", "Finde zuerst das Regal mit den meisten und das mit den wenigsten Büchern. Dann vergleiche.",
    "Die meisten Bücher hat das Regal mit 1 502, die wenigsten das mit 1 052. 1 502 − 1 052 = 450.",
    [(297, None, "vom vollsten Regal das zweitkleinste abgezogen: 1 502 − 1 205", "1502 - 1205"), (2554, None, "addiert statt den Unterschied zu bilden", "1502 + 1052"), (252, None, "vom vollsten Regal das zweitvollste abgezogen: 1 502 − 1 250", "1502 - 1250")], "Bücher"), g="transfer")

# ───────── runden_regel ─────────
neu(T, "runden_regel", "zwei_wege", Z(
    "Weg A: Wende die Rundungsregel an und sieh dir die Ziffer rechts neben der Rundungsstelle an. Weg B: Schreibe die beiden benachbarten vollen Hunderter auf und prüfe, zu welchem 7 349 näher liegt. Runde 7 349 auf volle Hunderter.",
    7300, "(7349 + 50) // 100 * 100", "7300 if 7349 - 7300 < 7400 - 7349 else 7400", "Die Rundungsstelle ist die Hunderterstelle. Welche Ziffer rechts daneben entscheidet?",
    "Weg A: Rechts neben den Hundertern steht die 4 (Zehnerstelle). 4 ist kleiner als 5, also wird abgerundet: 7 300. Weg B: Die Nachbarn sind 7 300 und 7 400. Der Abstand zu 7 300 ist 49, zu 7 400 ist 51. 7 300 ist näher.",
    [(7400, None, "wegen der Einerziffer 9 aufgerundet: 7 349 + 51 = 7 400", "7349 + 51"), (7350, None, "auf Zehner gerundet", "(7349 + 5) // 10 * 10"), (7000, None, "auf Tausender gerundet", "(7349 + 500) // 1000 * 1000")]), regel=BU)
neu(T, "runden_regel", "fehler_detektiv", FD(
    "Mara rundet 38 428 auf volle Hunderter.",
    [("Die Hunderterstelle von 38 428 ist die 4.", 38428 // 100 % 10 == 4, True, "Zeile 1 stimmt: An der Hunderterstelle steht die 4. Der Fehler steckt später."),
     ("Die Ziffer links neben der 4 ist die 8. Weil 8 mindestens 5 ist, wird aufgerundet.", 38428 // 10 % 10 >= 5, True),
     ("Aus 4 Hundertern werden 5 Hunderter, rechts stehen Nullen: 38 500.", True, True, "Zeile 3 folgt richtig aus der Entscheidung „aufrunden“ in Zeile 2. Der Fehler liegt schon davor.")],
    "Prüfe jede Zeile für sich: Stimmt die Aussage, und folgt der Schritt aus der Rundungsregel? Welche Zeile enthält zuerst einen Fehler?",
    "Entscheidend ist die Ziffer rechts neben der Rundungsstelle, hier die 2 der Zehnerstelle. 2 ist kleiner als 5, also wird abgerundet: 38 400. Der erste Fehler steht in Zeile 2."), regel=BU)

# ───────── runden_uebertrag ─────────
_BES = [2949, 2950, 3049, 3050, 2987, 3012]
neu(T, "runden_uebertrag", "bruecke", Z(
    "Eine Zeitung meldet die Besucherzahlen eines Museums, jeweils auf volle Hunderter gerundet. In der Tabelle stehen die echten Zahlen von sechs Tagen. An wie vielen dieser Tage steht in der Zeitung 3 000?",
    4, "4", "[(x + 50) // 100 * 100 for x in [2949, 2950, 3049, 3050, 2987, 3012]].count(3000)", "Runde jede Zahl der Tabelle einzeln auf Hunderter. Achte auf die Zehnerziffer.",
    "Gerundet: 2 949 → 2 900; 2 950 → 3 000; 3 049 → 3 000; 3 050 → 3 100; 2 987 → 3 000; 3 012 → 3 000. An 4 Tagen steht 3 000.",
    [(3, "fb.buendeln.abgeschnitten_statt_gerundet", "abgeschnitten statt gerundet (Zehner und Einer weggelassen)", lambda: [x // 100 * 100 for x in _BES].count(3000) == 3), (5, None, "alle Werte von 2 950 bis 3 050 gezählt, auch 3 050", lambda: sum(2950 <= x <= 3050 for x in _BES) == 5)], "Tage",
    grafik=TAB(["Tag", "Besucher"], ["Mo", "2 949"], ["Di", "2 950"], ["Mi", "3 049"], ["Do", "3 050"], ["Fr", "2 987"], ["Sa", "3 012"])), regel=BU)
neu(T, "runden_uebertrag", "umkehren", Z(
    "Eine ganze Zahl wurde mit der üblichen Rundungsregel (ab 5 wird aufgerundet) auf volle Hunderter gerundet und ergibt 8 000. Welches ist die kleinste ganze Zahl, bei der das passiert?",
    7950, "8000 - 50", "7900 + 50", "Teste Zahlen knapp unter 8 000: Welche werden noch zu 8 000, welche schon zu 7 900?",
    "Aufgerundet wird ab einer Zehnerziffer 5. Der kleinere volle Hunderter ist 7 900. Die kleinste Zahl, die zu 8 000 aufgerundet wird, ist 7 950. 7 949 würde zu 7 900 abgerundet.",
    [(7900, None, "den kleineren vollen Hunderter genannt", "8000 - 100"), (7949, None, "eine Zahl zu klein: 7 949 wird abgerundet", "7950 - 1"), (7500, None, "mit der Grenze für Tausender gerechnet", "8000 - 500")]), g="rueckwaerts", regel=BU)

# ───────── runden_sinnvoll ─────────
neu(T, "runden_sinnvoll", "zwei_wege", Z(
    "Für 342 Personen sollen Busse bestellt werden. In jeden Bus passen 50 Personen. Weg A: Teile und runde sinnvoll. Weg B: Zähle die Plätze für 1, 2, 3 … Busse auf, bis es reicht. Wie viele Busse werden mindestens gebraucht?",
    7, "-(-342 // 50)", "342 // 50 + 1", "Passen 342 Personen in 6 Busse? Probiere es.",
    "Weg A: 342 : 50 = 6 Rest 42. Die 42 Personen brauchen noch einen Bus: 7 Busse. Weg B: 6 Busse haben 300 Plätze, das reicht nicht. 7 Busse haben 350 Plätze, das reicht.",
    [(6, None, "abgerundet: die übrigen 42 Personen bleiben ohne Platz", "342 // 50"), (8, None, "einen Bus zu viel bestellt", "342 // 50 + 2")], "Busse"))
neu(T, "runden_sinnvoll", "fehler_detektiv", FD(
    "Eine Klasse bestellt Pizza. 47 Personen essen je 2 Stücke. Eine Pizza hat 8 Stücke. Nico rechnet.",
    [("47 Personen essen zusammen 47 · 2 = 94 Stücke.", 47 * 2 == 94, True, "Zeile 1 stimmt: 47 · 2 = 94. Der Fehler steckt später."),
     ("94 geteilt durch 8 ergibt 11 Rest 6.", 94 // 8 == 11 and 94 % 8 == 6, True, "Zeile 2 stimmt: 11 · 8 = 88, dazu der Rest 6 ergibt 94. Der Fehler steckt später."),
     ("Es reichen 11 Pizzen, denn die übrigen 6 Stücke sind weniger als eine ganze Pizza.", 11 * 8 >= 94, True)],
    "Prüfe jede Zeile für sich: Rechnet sie richtig, und passt der Schluss zur Aufgabe? Welche Zeile enthält zuerst einen Fehler?",
    "11 Pizzen haben nur 11 · 8 = 88 Stücke, es fehlen 6. Man muss aufrunden: 12 Pizzen (96 Stücke). Der erste Fehler steht in Zeile 3."))

# ───────── unendlich ─────────
neu(T, "unendlich", "zwei_wege", Z(
    "Tim behauptet: „999 999 ist die größte natürliche Zahl.“ Du widerlegst das mit dem Nachfolger. Weg A: Addiere 1 zu 999 999. Weg B: Überlege, welche Zahl direkt nach 999 999 kommt, wenn du die Zahlen bis zur Million aufzählst. Wie heißt der Nachfolger von 999 999?",
    1000000, "999999 + 1", "10 ** 6", "Welche Zahl kommt unmittelbar nach 999 999? Was geschieht mit den Neunen?",
    "Weg A: 999 999 + 1 = 1 000 000. Weg B: Beim Zählen auf die Million kommt nach 999 999 die Zahl 1 000 000. Der Nachfolger ist größer, also ist Tims Zahl nicht die größte. Dasselbe gilt für jede Zahl, die jemand als größte nennt: Ihr Nachfolger ist größer. Darum gibt es keine größte natürliche Zahl.",
    [(999998, None, "den Vorgänger statt des Nachfolgers genommen: 999 999 − 1", "999999 - 1"), (1000001, None, "zwei Schritte statt einen weitergezählt: 999 999 + 2", "999999 + 2"), (100000, None, "nur eine 1 mit fünf Nullen geschrieben", "10 ** 5")]))
neu(T, "unendlich", "umkehren", Z(
    "Anna behauptet, ihre Zahl sei die größte natürliche Zahl. Ben widerlegt sie, indem er den Nachfolger ihrer Zahl nennt: 2 000 000. Welche Zahl hat Anna genannt?",
    1999999, "2000000 - 1", "1999999", "Ben hat zu Annas Zahl 1 addiert. Wie kommst du zu Annas Zahl zurück?",
    "Der Nachfolger von Annas Zahl ist 2 000 000, also ist Annas Zahl der Vorgänger: 2 000 000 − 1 = 1 999 999. Probe: 1 999 999 + 1 = 2 000 000. Zu jeder Zahl gibt es einen Nachfolger, der größer ist; darum kann Annas Zahl nicht die größte sein.",
    [(2000001, None, "den Nachfolger statt des Vorgängers genommen: 2 000 000 + 1", "2000000 + 1"), (1999998, None, "zwei Schritte statt einen zurückgegangen: 2 000 000 − 2", "2000000 - 2"), (1000000, None, "die Zahl halbiert: 2 000 000 : 2", "2000000 / 2")]), g="rueckwaerts")

# ───────── roemisch_schreiben ─────────
_RW = [("MCMLXXXIV", 1984), ("MCMLXXXVI", 1986), ("MDCLXXXIV", 1684), ("MCMLXXIV", 1974)]
neu(T, "roemisch_schreiben", "anwenden", W(
    "Über dem Eingang einer Schule soll das Baujahr 1984 in römischen Zahlzeichen stehen. Welche Schreibweise ist richtig?",
    "MCMLXXXIV",
    [("MCMLXXXVI", "Das ist 1986."), ("MDCLXXXIV", "Das ist 1684."), ("MCMLXXIV", "Das ist 1974.")],
    "Zerlege 1984 in Tausender, Hunderter, Zehner und Einer. Schreibe jeden Teil einzeln.",
    "1984 = 1000 + 900 + 80 + 4 = M + CM + LXXX + IV = MCMLXXXIV.",
    lambda: all(roem_wert(s) == v for s, v in _RW) and roem(1984) == "MCMLXXXIV"))
neu(T, "roemisch_schreiben", "fehler_detektiv", FD(
    "Lena schreibt die Zahl 49 in römischen Zahlzeichen.",
    [("49 ist 50 − 1.", 50 - 1 == 49, True, "Zeile 1 stimmt: 50 − 1 = 49. Der Fehler steckt später."),
     ("Das Zeichen für 50 ist L, das Zeichen für 1 ist I.", roem_wert("L") == 50 and roem_wert("I") == 1, True, "Zeile 2 stimmt: L ist 50 und I ist 1. Der Fehler steckt später."),
     ("Ein kleineres Zeichen vor einem größeren wird abgezogen, also darf die I direkt vor der L stehen.", False, True),
     ("Also schreibt man 49 als IL.", roem(49) == "IL", True, "Zeile 4 übernimmt nur die Schreibweise aus Zeile 3. Der Fehler liegt schon davor.")],
    "Prüfe jede Zeile für sich und denke an die Regeln für das Abziehen bei römischen Zahlen. Welche Zeile enthält zuerst einen Fehler?",
    "Das Abziehen ist eingeschränkt: Die I darf nur vor V und X stehen, die X nur vor L und C. 49 = 40 + 9 = XL + IX = XLIX. Der erste Fehler steht in Zeile 3."))

# ───────── roemisch_system ─────────
neu(T, "roemisch_system", "umkehren", W(
    "Das Doppelte einer Zahl ist MCM. Welche römische Zahl ist es?",
    "CML",
    [("ML", "Das ist 1 050: MCM wurde als 1 000 + 100 + 1 000 = 2 100 gelesen und halbiert, dabei wurde das C falsch addiert."), ("MMMDCCC", "Das ist 3 800: Es wurde verdoppelt statt halbiert.")],
    "Schreibe MCM zuerst mit Ziffern. Rechne dann rückwärts.",
    "MCM ist 1 900 (M = 1 000 und CM = 900). Die Zahl ist die Hälfte: 1 900 : 2 = 950. 950 = 900 + 50 = CM + L = CML. Probe: 2 · 950 = 1 900. Das Zeichen C hat immer den Grundwert 100; steht es vor M, wird es abgezogen: CM = 1 000 − 100 = 900. Das Zeichen behält seinen Wert, nur seine Stellung vor oder nach einem anderen Zeichen entscheidet, ob addiert oder abgezogen wird.",
    lambda: roem_wert("MCM") == 1900 and roem(950) == "CML" and roem_wert("ML") == 1050 == (roem_wert("M") + roem_wert("C") + roem_wert("M")) // 2 and roem_wert("MMMDCCC") == 2 * 1900))
neu(T, "roemisch_system", "anwenden", Z(
    "Römische Zahlen haben keinen Stellenwert und keine Null. Die Zahl 888 hat in Ziffern 3 Zeichen. Bei 888 benötigt jeder der drei Teile 800, 80 und 8 vier römische Zeichen. Wie viele Zeichen mehr braucht ihre römische Schreibweise (DCCCLXXXVIII)?",
    9, "(1 + 3) + (1 + 3) + (1 + 3) - 3", "12 - 3", "Zähle die Zeichen D, C, L, X, V und I in der römischen Zahl einzeln. Was gehört zu den Ziffern 8?",
    "888 = 800 + 80 + 8 = DCCC + LXXX + VIII. Jede 8 braucht 4 Zeichen (ein Fünfer-Zeichen und drei Einer-Zeichen), zusammen 12 Zeichen. In Ziffern sind es 3. Also 12 − 3 = 9 Zeichen mehr.",
    [(12, None, "alle römischen Zeichen gezählt, die 3 Ziffern nicht abgezogen", "4 + 4 + 4"), (6, None, "die Fünfer-Zeichen D, L und V nicht mitgezählt: 3 + 3 + 3 − 3", "3 + 3 + 3 - 3"), (3, None, "nur die Zahl der Ziffern genannt", "3")], "Zeichen"), g="transfer")

# ───────── dualsystem ─────────
neu(T, "dualsystem", "zwei_wege", Z(
    "Weg A: Addiere die Stellenwerte 1, 2, 4, 8, 16, 32 dort, wo eine 1 steht. Weg B: Gehe von links nach rechts: Verdopple die bisherige Zahl und addiere die nächste Ziffer. Welche Zahl im Zehnersystem steht hinter der Dualzahl 101101?",
    45, "32 + 8 + 4 + 1", "((((1 * 2 + 0) * 2 + 1) * 2 + 1) * 2 + 0) * 2 + 1", "Von rechts nach links verdoppeln sich die Stellenwerte: 1, 2, 4 …",
    "Weg A: 32 + 8 + 4 + 1 = 45. Weg B: 1, dann 1 · 2 + 0 = 2, 2 · 2 + 1 = 5, 5 · 2 + 1 = 11, 11 · 2 + 0 = 22, 22 · 2 + 1 = 45.",
    [(4, None, "nur die Einsen gezählt", "1 + 1 + 1 + 1"), (63, None, "alle Stellenwerte addiert, auch bei den Nullen", "32 + 16 + 8 + 4 + 2 + 1")]))
neu(T, "dualsystem", "fehler_detektiv", FD(
    "Ben schreibt die Zahl 13 als Dualzahl.",
    [("13 = 8 + 4 + 1.", 8 + 4 + 1 == 13, True, "Zeile 1 stimmt: 8 + 4 + 1 = 13. Der Fehler steckt später."),
     ("Die Stellenwerte sind 8, 4, 2, 1. Also steht bei 8 eine 1, bei 4 eine 0, bei 2 eine 1 und bei 1 eine 1.", 8 + 2 + 1 == 13, True),
     ("Die Dualzahl ist 1011.", int("1011", 2) == 13, True, "Zeile 3 schreibt die Ziffern aus Zeile 2 richtig hintereinander. Der Fehler liegt schon in Zeile 2.")],
    "Prüfe jede Zeile für sich und rechne die Dualzahl zur Probe zurück. Welche Zeile enthält zuerst einen Fehler?",
    "In 13 = 8 + 4 + 1 kommt die 2 nicht vor. Richtig: bei 8 eine 1, bei 4 eine 1, bei 2 eine 0, bei 1 eine 1: 1101. Der erste Fehler steht in Zeile 2."))
