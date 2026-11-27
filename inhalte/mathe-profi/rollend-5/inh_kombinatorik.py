"""rollend-5 · stochastik.kombinatorik (7 Lernkarten, 21 Aufgaben)."""
import math
from k5basis import *      # noqa: F401,F403

TH = "stochastik.kombinatorik"
ST = "id.daten.stufen"

# ── systematisch ──
neu(TH, "systematisch", "lueckenweg", "direkt", L(
    "Ein Eisbecher hat eine Sorte (Vanille, Schoko, Erdbeere) und eine Soße (Karamell, Himbeer). Die Sorte Vanille lässt sich mit ① Soßen kombinieren. Das gilt für jede Sorte. Alle Becher zusammen: Zahl der Sorten mal ① = ②.",
    ["2", "3*2"], ["2", "6"], "Zähle die Soßen, die zu einer einzigen Sorte passen.", "Zu Vanille passen 2 Soßen, genauso zu Schoko und Erdbeere. 3 · 2 = 6 Becher.",
    {1: [(5, None, "3 + 2 gerechnet")]}), ST)
neu(TH, "systematisch", "bruecke", "darstellung", Z(
    "Die Tabelle zeigt die Eisbecher mit Vanille und mit Schoko. Jedes Feld steht für einen Becher. Die Zeile für Erdbeere fehlt noch. Sie hätte dieselben Soßen wie die anderen Zeilen. Wie viele Becher-Felder hätte die Tabelle insgesamt, wenn die Zeile für Erdbeere dazukäme?",
    "3*2", "2*2+2", "Wie viele Becher stünden in der Zeile für Erdbeere? Wie viele Zeilen hätte die Tabelle dann?", "Jede Zeile hat 2 Felder (2 Soßen). Mit Erdbeere sind es 3 Zeilen: 3 · 2 = 6 Becher.",
    [(4, None, "nur die gezeichneten Zeilen gezählt"), (5, None, "3 + 2 gerechnet")],
    grafik=TAB(["", "Karamell", "Himbeer"], ["Vanille", "Becher 1", "Becher 2"], ["Schoko", "Becher 3", "Becher 4"])), ST)
neu(TH, "systematisch", "anwenden", "einkleidung", Z(
    "Eine Pizzeria bietet 3 Teigarten und 4 Beläge an. Jede Pizza hat genau eine Teigart und genau einen Belag. Kim will jede mögliche Kombination genau einmal probieren, eine Pizza pro Tag. Wie viele Tage braucht sie?",
    "3*4", "4+4+4", "Halte eine Teigart fest und zähle die Beläge. Dann die nächste Teigart.", "Zu jeder der 3 Teigarten gibt es 4 Beläge: 3 · 4 = 12 Tage.",
    [(7, None, "3 + 4 gerechnet"), (4, None, "nur eine Teigart gezählt")]), ST)

# ── zaehlprinzip ──
neu(TH, "zaehlprinzip", "fehler_detektiv", "fehler", FDZ(
    "Eine Schule bietet Menüs an: 3 Vorspeisen, 4 Hauptgerichte und 2 Nachspeisen. Jedes Menü hat von jeder Sorte genau eines. Kim zählt die Menüs.",
    [("Es gibt 3 Vorspeisen.", True), ("Zu jeder Vorspeise passen 4 Hauptgerichte: 3 · 4 = 12 Paare.", 3 * 4 == 12), ("Zu jedem der 12 Paare gibt es 2 Nachspeisen.", True), ("Also gibt es 12 + 2 = 14 Menüs.", 12 + 2 == 3 * 4 * 2)],
    "Wie werden Anzahlen verbunden, wenn man nacheinander wählt?", "Wahlen nacheinander werden malgenommen: 12 · 2 = 24 Menüs."), ST)
neu(TH, "zaehlprinzip", "zwei_wege", "mehrschritt", Z(
    "Ein Fahrrad gibt es in 4 Farben, 3 Größen und 2 Lenkerformen. Jedes Rad hat von jedem eines. Weg A multipliziert die drei Anzahlen. Weg B zählt alle Räder einer Farbe auf und addiert diese Anzahl dann für jede Farbe. Wie viele verschiedene Räder gibt es?",
    "4*3*2", "(3*2)+(3*2)+(3*2)+(3*2)", "Beide Wege führen zur selben Zahl.", "Weg A: 4 · 3 · 2 = 24. Weg B: Je Farbe gibt es 3 · 2 = 6 Räder. Für 4 Farben: 6 + 6 + 6 + 6 = 24.",
    [(9, None, "alle Anzahlen addiert"), (12, None, "den Lenker vergessen")]), ST)
neu(TH, "zaehlprinzip", "anwenden", "einkleidung", Z(
    "Ein Nummernschloss hat 3 Rädchen. Auf jedem Rädchen kann man eine Ziffer von 0 bis 9 einstellen, auch dieselbe Ziffer mehrmals. Wie viele Einstellungen gibt es?",
    "10*10*10", "10**3", "Wie viele Ziffern gibt es von 0 bis 9? Ein Rädchen nach dem anderen.", "Jedes Rädchen hat 10 Möglichkeiten: 10 · 10 · 10 = 1 000 Einstellungen.",
    [(30, None, "10 + 10 + 10 gerechnet"), (720, None, "ohne Wiederholung gerechnet")]), ST)

# ── reihenfolgen ──
neu(TH, "reihenfolgen", "lueckenweg", "direkt", L(
    "Vier Kinder setzen sich auf vier Plätze nebeneinander, jedes auf einen anderen. Auf den ersten Platz kann jedes der 4 Kinder. Für den zweiten Platz bleiben ① Kinder. Für den dritten Platz bleibt eins weniger als beim zweiten: ②. Zusammen: 4 · ① · ② · 1 = ③ Reihenfolgen.",
    ["4-1", "4-1-1", "4*3*2*1"], ["3", "2", "24"], "Jedes Kind sitzt nur auf einem Platz. Die Auswahl wird jedes Mal um eins kleiner.", "Platz 2: 3 Kinder, Platz 3: 2 Kinder, Platz 4: 1 Kind. 4 · 3 · 2 · 1 = 24.",
    {0: [(4, None, "ein Kind sitzt schon, das vergessen")], 2: [(64, None, "mit 4 · 4 · 4 · 1 gerechnet"), (10, None, "4 + 3 + 2 + 1 gerechnet")]}), ST)
assert math.factorial(5) == 120
neu(TH, "reihenfolgen", "umkehren", "umkehr", Z(
    "Mehrere Kinder stellen sich in einer Reihe auf, alle verschieden. Dafür gibt es 120 mögliche Reihenfolgen. Wie viele Kinder sind es?",
    "5", str(next(n for n in range(1, 10) if math.factorial(n) == 120)), "Probiere nacheinander 3 · 2 · 1, dann 4 · 3 · 2 · 1 und so weiter.", "5 · 4 · 3 · 2 · 1 = 120. Es sind 5 Kinder. Bei 4 Kindern wären es nur 24 Reihenfolgen.",
    [(4, None, "bei 24 Reihenfolgen aufgehört"), (6, None, "eins zu weit: 720 Reihenfolgen")]), ST)
neu(TH, "reihenfolgen", "anwenden", "einkleidung", Z(
    "Bei einer Staffel laufen 4 Kinder nacheinander. Jedes Kind läuft genau einmal. Die Trainerin legt fest, in welcher Reihenfolge sie laufen. Wie viele Möglichkeiten hat sie?",
    "4*3*2*1", "24", "Für den ersten Läufer hat sie 4 Kinder zur Wahl. Dann wird die Auswahl kleiner.", "4 · 3 · 2 · 1 = 24 Reihenfolgen.",
    [(10, None, "4 + 3 + 2 + 1 gerechnet"), (256, None, "mit Wiederholung gerechnet: 4 · 4 · 4 · 4")]), ST)

# ── baumdiagramm ──
neu(TH, "baumdiagramm", "bruecke", "darstellung", Z(
    "Das Baumdiagramm zeigt zwei Münzwürfe nacheinander (K = Kopf, Z = Zahl). Bei wie vielen Pfaden kommt mindestens einmal Z vor?",
    "4-1", "3", "Zähle alle Pfade und streiche den, bei dem kein Z vorkommt.", "Es gibt 4 Pfade: KK, KZ, ZK, ZZ. Nur KK hat kein Z. Es bleiben 3 Pfade.",
    [(2, None, "nur KZ und ZK gezählt"), (1, None, "nur ZZ gezählt")],
    grafik={"typ": "baum", "aeste": [{"text": "K", "aeste": [{"text": "K"}, {"text": "Z"}]}, {"text": "Z", "aeste": [{"text": "K"}, {"text": "Z"}]}]}), ST)
neu(TH, "baumdiagramm", "verfahren_waehlen", "erkennen", W(
    "Du willst alle Ergebnisse von drei Münzwürfen nacheinander zählen. Welcher Weg ist sicher?",
    "Ein Baumdiagramm mit drei Stufen zeichnen und die Pfade zählen: 2 · 2 · 2 = 8",
    [("Die Äste einer Stufe zählen und mit 3 malnehmen: 2 · 3 = 6", "Zahl der Würfe als Faktor genommen"), ("Die Äste addieren: 2 + 2 + 2 = 6", "Anzahlen addiert statt malgenommen"), ("Nur Kopf-Kopf-Kopf und Zahl-Zahl-Zahl zählen: 2", "nur zwei Pfade betrachtet")],
    "Jeder Pfad von der Wurzel bis zum Ende ist ein Ergebnis.", "Jeder Wurf hat 2 Äste, jeder Ast teilt sich wieder in 2: 2 · 2 · 2 = 8 Pfade.",
    2 ** 3 == 8 and 2 * 3 != 8 and 2 + 2 + 2 != 8), ST)
neu(TH, "baumdiagramm", "umkehren", "umkehr", Z(
    "In einem Baumdiagramm teilt sich die Wurzel in 3 Äste. Jeder dieser Äste teilt sich in gleich viele weitere Äste. Es gibt am Ende 12 Pfade. In wie viele Äste teilt sich jeder der ersten Äste?",
    "12//3", "4", "Die Zahl der Pfade ist das Produkt der Astzahlen. Welche Zahl mal 3 gibt 12?", "3 · ? = 12, also ? = 12 : 3 = 4 Äste.",
    [(36, None, "malgenommen statt geteilt"), (9, None, "12 − 3 gerechnet")]), ST)

# ── bedingungen ──
neu(TH, "bedingungen", "lueckenweg", "direkt", L(
    "Gesucht sind dreistellige Zahlen mit lauter verschiedenen Ziffern, deren erste Ziffer ungerade ist. Es gibt 10 Ziffern von null bis neun. Für die erste Ziffer gibt es ① Möglichkeiten. Für die zweite Ziffer darf jede Ziffer außer der ersten stehen, auch die 0: Das sind ② Möglichkeiten. Für die dritte Ziffer bleibt eine weniger als bei der zweiten: ③. Zusammen ① · ② · ③ = ④.",
    ["10//2", "10-1", "10-2", "5*9*8"], ["5", "9", "8", "360"], "Beginne mit der Stelle, für die eine Bedingung gilt. Welche Ziffern von 0 bis 9 sind ungerade?", "Ungerade Ziffern: 1, 3, 5, 7, 9. Das sind 5 Möglichkeiten. Zweite Ziffer: 10 minus die erste, also 9. Dritte Ziffer: 8. Zusammen 5 · 9 · 8 = 360.",
    {0: [(9, None, "nur „nicht 0“ beachtet statt „ungerade“"), (4, None, "eine ungerade Ziffer vergessen")], 1: [(10, None, "die erste Ziffer nicht abgezogen")], 3: [(648, None, "mit 9 · 9 · 8 gerechnet: nur die 0 vorn verboten"), (720, None, "mit 10 · 9 · 8 gerechnet: vorn keine Einschränkung")]}), ST)
neu(TH, "bedingungen", "zwei_wege", "mehrschritt", Z(
    "Eine PIN hat 4 Ziffern. Die erste Ziffer darf nicht 0 sein, die anderen dürfen beliebig sein, auch gleich. Weg A rechnet 9 · 10 · 10 · 10. Weg B nimmt alle 10 000 Ziffernfolgen und zieht die 1 000 Folgen mit 0 vorn ab. Wie viele PINs gibt es?",
    "9*10*10*10", "10000-1000", "Beide Wege geben dieselbe Zahl.", "Weg A: 9 · 1 000 = 9 000. Weg B: 10 000 − 1 000 = 9 000.",
    [(10000, None, "führende Null erlaubt"), (4536, None, "ohne Wiederholung gerechnet: 9 · 9 · 8 · 7")]), ST)
neu(TH, "bedingungen", "anwenden", "einkleidung", Z(
    "Ein Team hat 6 Kinder. Es wird ein Kapitän und eine Stellvertretung gewählt. Dasselbe Kind kann nicht beides sein. Wie viele Möglichkeiten gibt es?",
    "6*5", "30", "Beginne mit dem Kapitän. Wie viele Kinder bleiben für die Stellvertretung?", "Kapitän: 6 Möglichkeiten. Stellvertretung: 5 Kinder bleiben. 6 · 5 = 30.",
    [(36, None, "dasselbe Kind erlaubt"), (11, None, "6 + 5 gerechnet")]), ST)

# ── grenzen ──
neu(TH, "grenzen", "fehler_detektiv", "fehler", FDZ(
    "Beim Fest begrüßen sich 6 Kinder, indem jedes Paar einmal die Hand gibt. Kim zählt die Handschläge.",
    [("Jedes Kind gibt 5 anderen die Hand.", 6 - 1 == 5), ("6 · 5 = 30, wenn man jedes Kind einzeln mitzählt.", 6 * 5 == 30), ("Ich teile nicht durch 2, denn jeder Handschlag zählt nur einmal.", 6 * 5 == 15), ("Es gibt 30 Handschläge.", True)],
    "Wie oft ist ein Handschlag zwischen A und B in deiner Rechnung gezählt?", "Jeder Handschlag wird zweimal gezählt (A mit B und B mit A). Darum teilt man durch 2: 30 : 2 = 15 Handschläge."), ST)
assert 7 * 6 // 2 == 21
neu(TH, "grenzen", "umkehren", "umkehr", Z(
    "Bei einem Turnier spielt jede Mannschaft genau einmal gegen jede andere. Es gibt 21 Spiele. Wie viele Mannschaften nehmen teil?",
    "7", str(next(n for n in range(2, 20) if n * (n - 1) // 2 == 21)), "Probiere: n Mannschaften geben n · (n − 1) : 2 Spiele.", "Bei 7 Mannschaften: 7 · 6 : 2 = 21 Spiele. Bei 6 wären es nur 15.",
    [(6, None, "bei 15 Spielen aufgehört"), (11, None, "21 : 2 gerundet")]), ST)
neu(TH, "grenzen", "anwenden", "einkleidung", Z(
    "Ein Verein hat 8 Mitglieder. Zwei von ihnen fahren gemeinsam zu einem Treffen. Es kommt nicht darauf an, wer zuerst genannt wird. Wie viele verschiedene Paare sind möglich?",
    "8*7//2", "28", "Zähle erst alle geordneten Paare und teile dann, weil die Reihenfolge egal ist.", "8 · 7 = 56 geordnete Paare. Jedes Paar ist doppelt gezählt: 56 : 2 = 28.",
    [(56, None, "nicht durch 2 geteilt"), (15, None, "8 + 7 gerechnet")]), ST)

# ── verstehen ──
neu(TH, "verstehen", "fehler_detektiv", "fehler", FDZ(
    "Kim zählt Buchstabenfolgen aus den vier Buchstaben A, B, C und D. Die Folgen müssen keine Bedeutung haben. Jeder Buchstabe darf in einer Folge genau einmal vorkommen, jede Folge hat vier Buchstaben.",
    [("Für den ersten Buchstaben gibt es 4 Möglichkeiten.", True), ("Für den zweiten bleiben 3, für den dritten 2, für den vierten 1.", True), ("Die Buchstaben werden nacheinander gewählt.", True), ("Also gibt es 4 + 3 + 2 + 1 = 10 Folgen.", 4 + 3 + 2 + 1 == 4 * 3 * 2 * 1)],
    "Wie verbindet man Anzahlen bei Wahlen nacheinander?", "Nacheinander heißt malnehmen: 4 · 3 · 2 · 1 = 24 Folgen."), ST)
neu(TH, "verstehen", "verfahren_waehlen", "erkennen", W(
    "Drei Freunde bestellen jeweils ein Getränk aus 4 Sorten. Dieselbe Sorte darf mehrfach bestellt werden. Es zählt, wer was bestellt: Nimmt Freund 1 Cola und Freund 2 Tee, ist das etwas anderes, als wenn es umgekehrt ist. Welche Rechnung zählt die möglichen Bestellungen?",
    "4 · 4 · 4", [("4 · 3 · 2", "als dürfte sich nichts wiederholen"), ("4 + 4 + 4", "Anzahlen addiert"), ("4 · 3", "Zahl der Sorten mal Zahl der Freunde gerechnet statt 4 · 4 · 4")],
    "Darf sich etwas wiederholen? Dann bleibt die Auswahl bei jeder Wahl gleich groß.", "Jeder der 3 Freunde hat 4 Sorten zur Wahl. 4 · 4 · 4 = 64 Bestellungen.",
    4 ** 3 == 64 and 4 * 3 * 2 != 64 and 4 + 4 + 4 != 64 and 4 * 3 != 64), ST)
assert 5 ** 3 == 125
neu(TH, "verstehen", "umkehren", "umkehr", Z(
    "Bei 3 Wahlen nacheinander gibt es jedes Mal gleich viele Möglichkeiten, und dieselbe Möglichkeit darf wiederholt werden. Insgesamt gibt es 125 Fälle. Wie viele Möglichkeiten hat jede einzelne Wahl?",
    "5", str(next(n for n in range(1, 20) if n ** 3 == 125)), "Welche Zahl ergibt als Produkt aus drei gleichen Faktoren 125?", "5 · 5 · 5 = 125. Jede Wahl hat 5 Möglichkeiten.",
    [(42, None, "125 : 3 gerundet"), (25, None, "die Fälle nach zwei Wahlen genannt (5 · 5)")]), ST)
