"""rollend-5 · zahlen.natuerlich (13 Lernkarten, 39 Aufgaben)."""
from k5basis import *      # noqa: F401,F403

TH = "zahlen.natuerlich"
SW, ZG, BU, SS = "rr.stellenwert", "id.zahlen.zahlengerade", "id.zahlen.buendeln", "id.zahlen.schreibweisen"
WERT = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roem_zu_zahl(s):
    t = 0
    for i, ch in enumerate(s):
        v = WERT[ch]
        t += -v if i + 1 < len(s) and WERT[s[i + 1]] > v else v
    return t


def zahl_zu_roem(n):
    r = ""
    for v, z in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
        while n >= v:
            r += z
            n -= v
    return r


# ── stellenwert ──
neu(TH, "stellenwert", "lueckenweg", "direkt", L(
    "In der Zahl 6 083 steht die 8 an der Zehnerstelle: 8 · 10 = ①. Die 6 steht an der Tausenderstelle: 6 · 1 000 = ②. Die Ziffer 0 an der Hunderterstelle trägt nichts bei. Die Zahl ohne die Einer ist deshalb ② + ① = ③.",
    ["8*10", "6*1000", "6*1000+8*10"], ["80", "6*10**3", "6080"], "Wert einer Ziffer = Ziffer mal Wert ihrer Stelle.", "8 · 10 = 80. 6 · 1 000 = 6 000. 6 000 + 80 = 6 080.",
    {0: [(8, None, "nur die Ziffer genommen")], 1: [(600, "fb.stellenwert.eine_stelle_daneben", "eine Stelle zu weit rechts gerechnet")], 2: [(680, None, "mit dem Wert 600 für die 6 weitergerechnet")]}), SW)
neu(TH, "stellenwert", "bruecke", "darstellung", Z(
    "Die Tafel zeigt die Ziffern einer Zahl. Schreibe die Zahl.",
    "3*1000+0*100+5*10+0*1", "3050", "Lies die Tafel von links nach rechts. Eine Null hält die Stelle frei.", "3 Tausender, 0 Hunderter, 5 Zehner, 0 Einer: 3 000 + 50 = 3 050.",
    [(350, None, "die Null an der Hunderterstelle weggelassen"), (3500, "fb.stellenwert.eine_stelle_daneben", "die 5 eine Stelle zu weit links gelesen (als Hunderter)")],
    grafik=TAB(["T", "H", "Z", "E"], ["3", "0", "5", "0"])), SW)
neu(TH, "stellenwert", "anwenden", "einkleidung", Z(
    "Eine Anzeige am Eingang eines Museums zeigt die Besucherzahl: 5 Tausender, 0 Hunderter, 7 Zehner, 3 Einer. Danach kommen noch 40 Besucher. Wie viele Besucher sind es dann?",
    "5*1000+0*100+7*10+3+40", "5073+40", "Schreibe zuerst die Zahl der Anzeige als Ziffern. Dann addiere.", "Anzeige: 5 000 + 70 + 3 = 5 073. Dazu 40: 5 113 Besucher.",
    [(5073, None, "die 40 vergessen"), (5473, None, "40 als 400 addiert")]), SW)

# ── zahlwort_zu_ziffern ──
neu(TH, "zahlwort_zu_ziffern", "fehler_detektiv", "fehler", FDZ(
    "Kim schreibt „drei Millionen vierzigtausend zwölf“ in Ziffern.",
    [("Drei Millionen sind 3 000 000.", True), ("Vierzigtausend sind 400 000.", 40000 == 400000), ("Zusammen: 3 000 000 + 400 000 + 12 = 3 400 012.", 3000000 + 400000 + 12 == 3400012)],
    "Wie viele Nullen hat „vierzigtausend“?", "Vierzigtausend sind 40 000 (4 Zehntausender). Richtig: 3 000 000 + 40 000 + 12 = 3 040 012."), SS)
neu(TH, "zahlwort_zu_ziffern", "umkehren", "umkehr", Z(
    "Ein Zahlwort heißt „fünfzig Millionen dreihundert“. Aus wie vielen Ziffern besteht die Zahl, wenn du sie aufschreibst?",
    "8", str(len(str(50000300))), "Schreibe die Zahl zuerst auf. Von rechts: Dreiergruppen.", "50 Millionen = 50 000 000, dazu 300: 50 000 300. Das sind 8 Ziffern.",
    [(5, None, "50 300 geschrieben und die leere Gruppe weggelassen")]), SS)
neu(TH, "zahlwort_zu_ziffern", "anwenden", "einkleidung", Z(
    "Ein Verein meldet: „Wir haben zwei Millionen dreihunderttausend vierzig Euro gespendet.“ Ein anderer Verein hat 2 299 940 € gespendet. Wie viel Euro hat der erste Verein mehr gespendet?",
    "2300040-2299940", "100", "Schreibe die Spende des ersten Vereins zuerst in Ziffern.", "„Zwei Millionen dreihunderttausend vierzig“ sind 2 300 040. 2 300 040 − 2 299 940 = 100.",
    [(460, None, "„vierzig“ als 400 gelesen")]), SS)

# ── ziffern_zu_zahlwort ──
neu(TH, "ziffern_zu_zahlwort", "lueckenweg", "direkt", L(
    "Die Zahl 48 000 120 soll in Worten geschrieben werden. Sie hat ① Ziffern. Von diesen ① Ziffern bilden 6 Ziffern von rechts zwei volle Dreiergruppen. Links bleiben ② Ziffern übrig. Diese ② Ziffern stehen vor dem Wort „Millionen“. Die mittlere Gruppe ist eine Zahl mit dem Wert ③.",
    ["8", "8-6", "0"], ["8", "2", "0"], "Zähle alle Ziffern. Schreibe die Zahl dann von rechts in Dreiergruppen.", "Die Zahl hat 8 Ziffern. Zwei volle Gruppen sind 6 Ziffern, links bleiben 2: 48 Millionen. Die mittlere Gruppe 000 hat den Wert 0 und wird nicht gelesen. Zahlwort: achtundvierzig Millionen einhundertzwanzig.",
    {0: [(7, None, "eine Ziffer übersehen")], 1: [(3, None, "die linke Gruppe als volle Dreiergruppe angenommen")], 2: [(48, None, "die linke Gruppe statt der mittleren genannt"), (120, None, "die rechte Gruppe statt der mittleren genannt")]}), SS)
neu(TH, "ziffern_zu_zahlwort", "zwei_wege", "mehrschritt", Z(
    "Zwei Wege für die Zahl 20 305 060: Weg A teilt von rechts in Dreiergruppen. Weg B rechnet: Zahl der Ziffern minus 3 minus 3. Wie viele Ziffern hat die Gruppe ganz links?",
    "8-3-3", "8%3", "Zähle zuerst alle Ziffern der Zahl.", "Die Zahl hat 8 Ziffern. Zwei volle Gruppen sind 6 Ziffern. Es bleiben 8 − 6 = 2 Ziffern ganz links: „zwanzig“.",
    [(3, None, "die linke Gruppe als voll angenommen"), (8, None, "alle Ziffern genannt")]), SS)
neu(TH, "ziffern_zu_zahlwort", "bruecke", "darstellung", W(
    "Die Tafel zeigt, wie viele Millionen, Tausender und Einer eine Zahl hat. Welches Zahlwort gehört zu der Zahl?",
    "sieben Millionen dreihundertfünftausend vierzig",
    [("sieben Millionen dreihundertfünf vierzig", "das Wort „tausend“ vergessen"), ("sieben Millionen dreihundertfünftausend vierhundert", "die Einer-Gruppe 40 als 400 gelesen"), ("siebenhundertdreißigtausend fünfhundertvierzig", "die Zahl 730 540 gelesen: Gruppen falsch zusammengesetzt")],
    "Lies die Gruppen von links nach rechts. Hinter jeder Gruppe steht ihr Wort.", "7 Millionen, 305 Tausender, 40 Einer: sieben Millionen dreihundertfünftausend vierzig. Die Zahl ist 7 305 040.",
    7 * 10**6 + 305 * 10**3 + 40 == 7305040,
    grafik=TAB(["Mio.", "Tsd.", "Einer"], ["7", "305", "40"])), SS)

# ── strahl_ablesen ──
neu(TH, "strahl_ablesen", "fehler_detektiv", "fehler", FDZ(
    "Ein Zahlenstrahl geht von 200 bis 600 und hat 8 Abschnitte. Der Pfeil steht 5 Abschnitte nach dem Anfang. Kim liest ihn ab.",
    [("Abschnittswert: 600 : 8 = 75.", 600 / 8 == (600 - 200) / 8), ("Der Pfeil liegt 5 Abschnitte weiter: 5 · 75 = 375.", 5 * 75 == 375), ("Die Zahl am Pfeil ist 200 + 375 = 575.", 200 + 375 == 575)],
    "Wie wird der Abschnittswert berechnet: Was gehört in die Klammer?", "Der Abschnittswert ist (Ende − Anfang) : Abschnitte = (600 − 200) : 8 = 50. Der Pfeil zeigt 200 + 5 · 50 = 450."), ZG)
neu(TH, "strahl_ablesen", "bruecke", "darstellung", W(
    "Der Zahlenstrahl hat gleich große Abschnitte. Welche Rechnung gibt die Zahl am Pfeil?",
    "300 + 3 · 50", [("3 · 50", "den Anfang vergessen"), ("300 + 3 · 8", "mit der Zahl der Abschnitte statt mit dem Abschnittswert gerechnet"), ("700 − 3 · 50", "vom Ende statt vom Anfang gezählt")],
    "Zuerst: Wie viel ist ein Abschnitt wert? Dann: Von welcher Zahl aus zählst du?", "Abschnittswert: (700 − 300) : 8 = 50. Der Pfeil steht 3 Abschnitte nach dem Anfang: 300 + 3 · 50 = 450.",
    300 + 3 * 50 == 450 and 3 * 50 != 450 and 300 + 3 * 8 != 450 and 700 - 3 * 50 != 450,
    grafik={"typ": "zahlenstrahl", "start": 300, "ende": 700, "abschnitte": 8, "beschriftet": "anfang_ende", "pfeil": 3}), ZG)
neu(TH, "strahl_ablesen", "anwenden", "einkleidung", Z(
    "Eine Laufstrecke ist als Zahlenstrahl von 1 000 m bis 2 000 m gezeichnet, mit 10 gleich großen Abschnitten. Eine Läuferin steht 7 Abschnitte nach dem Anfang. Dann läuft sie noch 150 m weiter. Bei welcher Meterzahl ist sie dann?",
    "1000+7*((2000-1000)//10)+150", "1850", "Wie viel Meter ist ein Abschnitt? Die Strecke beginnt nicht bei 0.", "Ein Abschnitt: 1 000 m : 10 = 100 m. 1 000 + 700 = 1 700. Dazu 150: 1 850 m.",
    [(850, None, "den Anfang vergessen"), (1700, None, "die 150 m vergessen")], einheit="m"), ZG)

# ── strahl_eintragen ──
neu(TH, "strahl_eintragen", "lueckenweg", "direkt", L(
    "Ein Strahl geht von 2 000 bis 3 000 und hat 5 Abschnitte. Ein Abschnitt ist (3 000 − 2 000) : 5 = ① wert. Die Zahl 2 600 liegt (2 600 − 2 000) : ① = ② Abschnitte nach dem Anfang.",
    ["(3000-2000)//5", "(2600-2000)//((3000-2000)//5)"], ["200", "600//200"], "Erst den Abschnittswert, dann die Strecke vom Anfang bis zur Zahl.", "1 000 : 5 = 200. 600 : 200 = 3 Abschnitte.",
    {0: [(500, None, "durch 2 statt durch 5 geteilt")], 1: [(4, None, "Striche statt Abschnitte gezählt"), (600, None, "die Strecke genannt, nicht durch den Abschnittswert geteilt")]}), ZG)
neu(TH, "strahl_eintragen", "umkehren", "umkehr", Z(
    "Auf einem Zahlenstrahl liegt die Zahl 4 500 genau 3 Abschnitte nach dem Anfang. Ein Abschnitt ist 500 wert. Bei welcher Zahl beginnt der Strahl?",
    "4500-3*500", "3000", "Gehe vom Pfeil rückwärts zum Anfang. Wie weit ist das in Zahlen?", "3 Abschnitte sind 3 · 500 = 1 500. 4 500 − 1 500 = 3 000. Der Strahl beginnt bei 3 000.",
    [(6000, None, "addiert statt abgezogen"), (4000, None, "nur einen Abschnitt abgezogen")]), ZG)
neu(TH, "strahl_eintragen", "verfahren_waehlen", "mehrschritt", W(
    "Du sollst 3 700 auf einem Zahlenstrahl von 3 000 bis 4 000 mit 10 gleich großen Abschnitten eintragen. Welcher Weg führt zum Ziel?",
    "Abschnittswert 100 bestimmen, dann (3 700 − 3 000) : 100 = 7 Abschnitte nach dem Anfang zählen",
    [("3 700 : 10 = 370 Abschnitte nach dem Anfang zählen", "Zahl durch die Zahl der Abschnitte geteilt"), ("3 700 − 10 = 3 690 Abschnitte nach dem Anfang zählen", "Zahl der Abschnitte abgezogen"), ("Vom Ende aus 3 000 Abschnitte zurückzählen", "Anfangswert als Zahl der Abschnitte genommen")],
    "Frage dich zuerst: Wie viel ist ein Abschnitt wert?", "Abschnittswert: 1 000 : 10 = 100. Der Abstand zum Anfang ist 700. 700 : 100 = 7 Abschnitte.",
    (3700 - 3000) / ((4000 - 3000) / 10) == 7 and 3700 / 10 > 10 and 3700 - 10 > 10), ZG)

# ── vergleichen ──
neu(TH, "vergleichen", "fehler_detektiv", "fehler", FDZ(
    "Kim vergleicht 89 999 und 101 000.",
    [("89 999 hat 5 Stellen.", len(str(89999)) == 5), ("101 000 hat 6 Stellen.", len(str(101000)) == 6), ("Die Zahl der Stellen ist egal. Ich vergleiche nur die erste Ziffer: 8 ist größer als 1.", len(str(89999)) == len(str(101000))), ("Also ist 89 999 die größere Zahl.", True)],
    "Wann darfst du direkt von links Ziffer für Ziffer vergleichen?", "Hat eine Zahl mehr Stellen, ist sie größer. Erst bei gleich vielen Stellen vergleichst du von links. 101 000 ist größer als 89 999."), BU)
neu(TH, "vergleichen", "zwei_wege", "mehrschritt", Z(
    "Drei Zahlen: 48 205, 48 250 und 48 025. Weg A vergleicht von links Ziffer für Ziffer. Weg B zieht von jeder Zahl 48 000 ab und vergleicht die Reste. Wie groß ist der Unterschied zwischen der größten und der kleinsten Zahl?",
    "max(48205,48250,48025)-min(48205,48250,48025)", "250-25", "Beide Wege geben dieselbe Reihenfolge der Zahlen.", "Reste: 205, 250 und 25. Größte: 48 250, kleinste: 48 025. 250 − 25 = 225.",
    [(45, None, "größte und mittlere Zahl verglichen"), (25, None, "nur den Rest der kleinsten Zahl genannt")]), BU)
neu(TH, "vergleichen", "anwenden", "einkleidung", Z(
    "Drei Städte haben diese Einwohnerzahlen: Stadt A 1 204 350, Stadt B 1 240 035, Stadt C 1 204 530. Wie viele Einwohner mehr hat die größte Stadt als die kleinste?",
    "1240035-1204350", "35685", "Ordne zuerst die drei Zahlen. Vergleiche von links.", "Größte: B mit 1 240 035. Kleinste: A mit 1 204 350. Unterschied: 1 240 035 − 1 204 350 = 35 685.",
    [(35505, None, "C statt A als kleinste genommen"), (180, None, "Stadt C und Stadt A verglichen")]), BU)

# ── runden_regel ──
neu(TH, "runden_regel", "lueckenweg", "direkt", L(
    "Die Zahl 48 372 wird auf Hunderter gerundet. Rechts neben der Hunderterstelle steht die Ziffer ①. Ist ① gleich 5 oder mehr, wird die Hunderterziffer 3 um 1 größer: Sie wird zur ②. Die gerundete Zahl hat vorn 48 dann die Hunderterziffer ② und dahinter zwei Nullen. Sie ist um ③ größer als 48 372.",
    ["48372//10%10", "48372//100%10+1", "(48372+50)//100*100-48372"], ["7", "4", "28"], "Welche Ziffer steht direkt rechts von der Hunderterstelle?", "Rechts der Hunderterstelle steht die 7. Also aufrunden: aus 3 wird 4. Dahinter Nullen: 48 400. 48 400 − 48 372 = 28.",
    {0: [(2, None, "die letzte Ziffer genommen")], 1: [(3, None, "nicht aufgerundet")], 2: [(-72, None, "mit 48 300 gerechnet (abgerundet)")]}), BU)
neu(TH, "runden_regel", "umkehren", "umkehr", Z(
    "Eine Zahl wurde auf Tausender gerundet und ergibt 65 000. Welche ist die kleinste Zahl, die beim Runden auf Tausender zu 65 000 wird?",
    "65000-500", "64500", "Ab welcher Ziffer rechts wird aufgerundet? Gehe von 65 000 aus nach unten.", "Aufgerundet wird ab 500. 65 000 − 500 = 64 500. Die Zahl 64 499 würde schon zu 64 000.",
    [(64000, None, "die glatte Zahl darunter genommen"), (65499, None, "die größte statt der kleinsten Zahl genannt")]), BU)
neu(TH, "runden_regel", "anwenden", "einkleidung", Z(
    "Ein Stadion fasst 52 487 Zuschauer. Die Zeitung rundet auf Hunderter. Ein Imbiss plant 300 Portionen weniger als die Zahl der Zeitung. Mit wie vielen Portionen plant er?",
    "(52487+50)//100*100-300", "52500-300", "Runde zuerst. Dann ziehe ab.", "Die Hunderter-Rundung von 52 487 ist 52 500. 52 500 − 300 = 52 200.",
    [(52187, None, "nicht gerundet"), (52100, None, "abgerundet statt aufgerundet")]), BU)

# ── runden_uebertrag ──
neu(TH, "runden_uebertrag", "fehler_detektiv", "fehler", FDZ(
    "Kim rundet 3 996 auf Zehner.",
    [("Die Einerziffer 6 ist 5 oder mehr: Es wird aufgerundet.", 6 >= 5), ("Aus 9 + 1 wird 10: Ich schreibe 0 an die Zehnerstelle und vergesse die 1.", (3996 + 5) // 10 * 10 == 3900), ("Die Hunderterziffer bleibt 9. Gerundet: 3 900.", True)],
    "Wohin gehört die 1 aus der 10?", "Die 1 muss an die Hunderterstelle weitergegeben werden: 9 + 1 = 10, wieder mit Übertrag. 3 996 wird zu 4 000."), BU)
neu(TH, "runden_uebertrag", "zwei_wege", "mehrschritt", Z(
    "Die Zahl 2 995 wird auf Hunderter gerundet. Weg A: Ziffer rechts der Hunderterstelle ansehen und aufrunden. Weg B: die zwei nächsten glatten Hunderterzahlen auf dem Zahlenstrahl suchen und die näher liegende nehmen. Um wie viel unterscheidet sich die gerundete Zahl von 2 995?",
    "3000-2995", "5", "Beide Wege geben dieselbe gerundete Zahl.", "Weg A: Rechts steht die 9, also aufrunden: 3 000. Weg B: 2 900 ist 95 entfernt, 3 000 nur 5. Unterschied: 3 000 − 2 995 = 5.",
    [(95, None, "zur falschen Hunderterzahl gerechnet"), (100, None, "beide Abstände addiert")]), BU)
neu(TH, "runden_uebertrag", "anwenden", "einkleidung", Z(
    "Der Tacho eines Autos zeigt 19 960 km. Der Händler schreibt in die Anzeige die Zahl auf Hunderter gerundet. Wie viele Kilometer ist die Zahl in der Anzeige größer als die Tacho-Anzeige?",
    "(19960+50)//100*100-19960", "20000-19960", "Runde zuerst. Vorsicht: Die 9 gibt die 1 weiter.", "19 960 auf Hunderter gerundet: 20 000. 20 000 − 19 960 = 40 km.",
    [(60, None, "abgerundet auf 19 900 gerechnet")], einheit="km"), BU)

# ── runden_sinnvoll ──
neu(TH, "runden_sinnvoll", "lueckenweg", "direkt", L(
    "Eine Zeitung schreibt über 4 987 Besucher. Auf Hunderter gerundet sind das ①. Der Veranstalter rechnet genau ab: Jeder Besucher zahlt 2 €. Das sind ② €. Mit der gerundeten Zahl wären es ① · 2 = ③ €, also 26 € zu viel.",
    ["(4987+50)//100*100", "4987*2", "(4987+50)//100*100*2"], ["5000", "9974", "10000"], "Runden darf man für eine Meldung. Für die Abrechnung nimmst du die genaue Zahl.", "4 987 ≈ 5 000. Genau: 4 987 · 2 = 9 974. Gerundet: 5 000 · 2 = 10 000. Unterschied: 26 €.",
    {0: [(4900, None, "abgerundet statt aufgerundet")], 2: [(9800, None, "mit 4 900 weitergerechnet")]}), BU)
neu(TH, "runden_sinnvoll", "verfahren_waehlen", "erkennen", W(
    "Du kennst die genaue Zahl 6 842. Für welchen Zweck darfst du sie runden?",
    "für eine Zeitungsmeldung: „etwa 6 800 Zuschauer“",
    [("für die Geheimzahl einer Karte: 6 800", "eine Geheimzahl muss genau stimmen"), ("für die Kasse: 6 800 € genau so buchen", "ein Betrag, der gebucht wird, muss genau stimmen"), ("für die Hausnummer: Haus 6 800", "eine Nummer rundet man nie")],
    "Frage: Reicht „ungefähr“ oder muss es genau stimmen?", "Runden ist erlaubt, wenn „ungefähr“ reicht, wie bei einer Meldung. Nummern, Geheimzahlen und ein Betrag, der gebucht wird, müssen genau stimmen.", 6842 != 6800), BU)
neu(TH, "runden_sinnvoll", "anwenden", "einkleidung", Z(
    "Für ein Fest kommen 238 Gäste. Jeder Gast bekommt einen Becher. Becher gibt es nur in Packungen zu je 50 Stück. Wie viele Packungen musst du mindestens kaufen?",
    "-(-238//50)", "(238+49)//50", "Eine Packung mehr ist besser als zu wenig Becher. Hier wird immer aufgerundet.", "238 : 50 = 4 Rest 38. Vier Packungen reichen nicht, es sind 5 Packungen.",
    [(4, None, "abgerundet: es fehlen Becher"), (6, None, "zu weit aufgerundet")]), BU)

# ── unendlich ──
neu(TH, "unendlich", "fehler_detektiv", "fehler", FDZ(
    "Kim sagt: „Es gibt eine größte natürliche Zahl.“ Er begründet.",
    [("Die größte Zahl mit 3 Ziffern ist 999.", True), ("Mit 4 Ziffern ist die größte Zahl 9 999. Sie ist größer.", 9999 > 999), ("Irgendwo kommt eine Zahl, die keinen Nachfolger mehr hat. Sie ist die größte.", not all(n + 1 > n for n in range(100000)))],
    "Kannst du zu jeder Zahl 1 dazuzählen?", "Zu jeder Zahl gibt es einen Nachfolger (+ 1). Darum gibt es keine größte natürliche Zahl."), SS)
neu(TH, "unendlich", "umkehren", "umkehr", Z(
    "Eine Zahl hat den Nachfolger 1 000 000. Wie heißt der Vorgänger dieser Zahl?",
    "1000000-2", "999998", "Gehe von 1 000 000 aus zwei Schritte zurück.", "Die Zahl selbst ist 999 999 (Vorgänger von 1 000 000). Ihr Vorgänger ist 999 998.",
    [(999999, None, "nur einen Schritt zurück"), (1000001, None, "in die falsche Richtung gerechnet")]), SS)
neu(TH, "unendlich", "anwenden", "einkleidung", Z(
    "Ein Zähler am Eingang eines Parks zählt jeden Besucher mit einer Ziffernanzeige. Er soll bis zur Zahl 1 000 000 zählen können. Wie viele Ziffernfelder braucht die Anzeige mindestens?",
    "6+1", str(len(str(1000000))), "Schreibe 1 000 000 auf und zähle die Ziffern.", "1 000 000 hat eine 1 und sechs Nullen: 7 Ziffern. Mit 6 Feldern würde nach 999 999 Schluss sein.",
    [(6, None, "nur die Nullen gezählt")]), SS)

# ── roemisch_schreiben ──
neu(TH, "roemisch_schreiben", "lueckenweg", "direkt", L(
    "MCMXLIV wird zerlegt. M = 1 000. CM = 1 000 − 100 = ①. XL = 50 − 10 = ②. IV = 5 − 1 = ③. Die Zahl ist die Summe 1 000 + ① + ② + ③ = ④.",
    ["1000-100", "50-10", "5-1", "1000+(1000-100)+(50-10)+(5-1)"], ["900", "40", "4", "1944"], "Ein kleineres Zeichen vor einem größeren wird abgezogen.", "CM = 900, XL = 40, IV = 4. Summe: 1 000 + 900 + 40 + 4 = 1 944.",
    {0: [(1100, None, "CM als M + C gelesen")], 3: [(2144, None, "mit 1 100 für CM weitergerechnet")]}, hinweis=GZ), SS)
_z1 = zahl_zu_roem(1493)
neu(TH, "roemisch_schreiben", "bruecke", "darstellung", T(
    "Die Tafel zeigt Tausender, Hunderter, Zehner und Einer einer Zahl. Schreibe die Zahl mit römischen Zeichen.",
    "MCDXCIII", _z1 == "MCDXCIII" and roem_zu_zahl("MCDXCIII") == 1493, "Schreibe jeden Teil einzeln: 1 000, 400, 90, 3. Dann hintereinander.", "1 000 = M, 400 = CD, 90 = XC, 3 = III. Zusammen: MCDXCIII.",
    [("MCCCCXCIII", "400 als CCCC statt CD"), ("MXDIII", "ein Paar, das es nicht gibt")],
    grafik=TAB(["T", "H", "Z", "E"], ["1", "4", "9", "3"])), SS)
neu(TH, "roemisch_schreiben", "umkehren", "umkehr", T(
    "Der Nachfolger einer Zahl ist XL. Schreibe die Zahl mit römischen Zeichen.",
    "XXXIX", zahl_zu_roem(roem_zu_zahl("XL") - 1) == "XXXIX", "Wie viel ist XL? Gehe einen Schritt zurück.", "XL ist 40. Der Vorgänger ist 39 = 30 + 9 = XXX + IX = XXXIX.",
    [("XXXX", "die 40 selbst nur mit Plus-Zeichen geschrieben statt den Vorgänger"), ("XIL", "40 − 1 als XIL geschrieben: I vor L gibt es nicht")]), SS)

# ── roemisch_system ──
neu(TH, "roemisch_system", "fehler_detektiv", "fehler", FDZ(
    "Kim vergleicht die römischen Zahlen IX und XI.",
    [("Bei IX steht das kleinere Zeichen I vor dem größeren X. Ich addiere trotzdem: 10 + 1 = 11.", roem_zu_zahl("IX") == 11), ("Bei XI steht das I hinter dem X: 10 + 1 = 11.", roem_zu_zahl("XI") == 11), ("Also haben IX und XI den gleichen Wert, nämlich 11.", True)],
    "Steht das I bei IX vor oder hinter dem X? Was bedeutet das?", "Steht ein kleineres Zeichen vor einem größeren, wird es abgezogen: IX = 10 − 1 = 9. XI = 10 + 1 = 11."), SS)
neu(TH, "roemisch_system", "zwei_wege", "mehrschritt", Z(
    "Wie viel ist MCMLXXXIV? Weg A: von links nach rechts lesen und jedes Zeichen zählen; ein kleineres Zeichen vor einem größeren wird abgezogen. Weg B: in eine Stellentafel eintragen: M zu den Tausendern, CM zu den Hundertern, LXXX zu den Zehnern, IV zu den Einern.",
    "1000+900+80+4", str(roem_zu_zahl("MCMLXXXIV")), "Beide Wege geben dieselbe Zahl.", "Weg A: 1 000 + 900 + 80 + 4 = 1 984. Weg B: Tausender 1, Hunderter 9, Zehner 8, Einer 4: 1 984.",
    [(1884, None, "CM als 800 gelesen"), (1964, None, "LXXX als 60 gelesen")]), SS)
neu(TH, "roemisch_system", "anwenden", "einkleidung", Z(
    "Über einer Haustür steht das Baujahr MDCCCLXXV. Wie viele Jahre ist das Haus im Jahr 2026 alt?",
    "2026-1875", "2026-" + str(roem_zu_zahl("MDCCCLXXV")), "Lies zuerst das Baujahr in normalen Ziffern.", "MDCCCLXXV = 1 000 + 500 + 300 + 70 + 5 = 1 875. 2 026 − 1 875 = 151 Jahre.",
    [(1875, None, "nur das Baujahr genannt")]), SS)

# ── dualsystem ──
neu(TH, "dualsystem", "lueckenweg", "direkt", L(
    "Die Zweierzahl 1101 hat die Stellenwerte 8, 4, 2 und 1. Gerechnet: 1 · 8 + 1 · 4 + 0 · 2 + 1 · 1 = ①. Die Zweierzahl 10010 hat die Stellenwerte 16, 8, 4, 2 und 1. Ebenso gerechnet ist sie ②. Die zweite Zahl ist um ② − ① = ③ größer.",
    ["1*8+1*4+0*2+1*1", "1*16+0*8+0*4+1*2+0*1", "1*16+0*8+0*4+1*2+0*1-(1*8+1*4+0*2+1*1)"], ["13", "18", "5"], "Nur die Stellenwerte mit einer 1 darunter werden addiert.", "1101: 8 + 4 + 1 = 13. 10010: 16 + 2 = 18. 18 − 13 = 5.",
    {0: [(1101, None, "die Zahl einfach wie bei uns gelesen")], 1: [(10010, None, "die Zahl einfach wie bei uns gelesen")], 2: [(8909, None, "mit den falsch gelesenen Zahlen gerechnet")]}), BU)
neu(TH, "dualsystem", "bruecke", "darstellung", Z(
    "Die Tafel zeigt die Stellenwerte einer Zweierzahl und ihre Ziffern. Welche normale Zahl ist das?",
    "1*16+0*8+1*4+1*2+0*1", "22", "Addiere nur die Stellenwerte, unter denen eine 1 steht.", "Unter 16, 4 und 2 steht eine 1: 16 + 4 + 2 = 22.",
    [(10110, None, "als normale Zahl gelesen"), (23, None, "den Stellenwert 1 zusätzlich mitgerechnet")],
    grafik=TAB(["16", "8", "4", "2", "1"], ["1", "0", "1", "1", "0"])), BU)
neu(TH, "dualsystem", "anwenden", "einkleidung", Z(
    "Ein Lichtband hat fünf Lampen für die Stellenwerte 16, 8, 4, 2 und 1. Die Lampen sind von links nach rechts so geordnet. Es leuchten die erste, die dritte und die fünfte Lampe. So zeigt das Band, wie viele Gäste im Saal sind. Dann kommen noch 9 Gäste. Wie viele Gäste sind es dann?",
    "16+4+1+9", "21+9", "Die leuchtenden Lampen sind die Einsen. Erst die Zahl auf dem Band, dann addieren.", "Es leuchten die Lampen für 16, 4 und 1: 21 Gäste. 21 + 9 = 30.",
    [(21, None, "die 9 vergessen"), (10110, None, "die Zweierzahl 10101 als normale Zahl gelesen und 9 addiert")]), BU)
