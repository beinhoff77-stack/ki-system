"""Mathe-Profi, Auftrag 13: Zeichen-Vorgaben für die tragenden Ideen der übrigen fünf Planeten.

Aufruf: python3 -I inhalte/mathe-profi/regeln-uebersicht/ideen_zeichnung.py
Je Idee: warum sie trägt, eine Zeichen-Vorgabe (sechs Zeilen), Rechenproben für alle Zahlen der Vorgabe.
Schreibt zeichen-vorgaben-fuenf-planeten.md. Höchstens vier Felder je Reihe (Wunsch des Designers).
"""
import importlib.util
import io
import contextlib
import os
import sys
from fractions import Fraction as F

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("gesetzbuch", os.path.join(HIER, "gesetzbuch.py"))
gb = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(gb)
Z, zeichnung_text = gb.sonne.Z, gb.sonne.zeichnung_text

# Kurzname der Idee → (warum, Zeichen-Vorgabe, [Proben])
V = {
 # ───── Zahlen ─────
 "Zahlengerade": ("Auf der Zahlengeraden hat jede Zahl genau einen Platz – ganze Zahlen, Brüche, Kommazahlen, negative Zahlen und später Wurzeln. Größer und kleiner heißt dann einfach: weiter rechts oder weiter links.",
  Z("Eine Zahlengerade von −3 bis 3. Vier Zahlen sind als Punkte eingetragen: −2,5 und −1 links der Null, ½ und 2 rechts. Unter der Geraden ein langer Pfeil nach rechts.",
    "Gleiche Abstände, Teilstriche an jeder ganzen und jeder halben Zahl. Die Null ist kräftiger gezeichnet.",
    "An den Punkten „−2,5“, „−1“, „½“, „2“. Am Pfeil: „nach rechts wird es größer“. Darunter: „−2,5 < −1 < ½ < 2“.",
    "Die Punkte −2,5 und −1: Die −2,5 liegt weiter links, ist also kleiner – obwohl 2,5 mehr ist als 1.",
    "−2,5 muss genau in der Mitte zwischen −3 und −2 liegen, ½ genau zwischen 0 und 1. Die Null muss sichtbar sein. Der Pfeil zeigt nach rechts.",
    "Dieselbe Gerade mit zwei gleich langen Bögen von 0 nach −2 und von 0 nach 2: Betrag und Gegenzahl. Dieselbe Gerade mit √2 ≈ 1,41 zwischen 1 und 2: irrationale Zahlen. Mit Teilstrichen in Sechsteln: ½ = 3/6 und ⅔ = 4/6 vergleichen."),
  [lambda: F(-5, 2) < -1 < F(1, 2) < 2, lambda: abs(2 ** 0.5 - 1.41) < 0.005, lambda: F(1, 2) == F(3, 6) and F(2, 3) == F(4, 6)]),
 "Bündeln in Zehnern": ("Unser Zahlensystem tauscht immer zehn gleiche Teile gegen ein größeres. Das gilt in beide Richtungen: nach links zu Zehnern und Hundertern, nach rechts zu Zehnteln und Hundertsteln. Jedes Rechnen mit Übertrag, jedes Runden und jedes Komma-Verschieben beruht darauf.",
  Z("Zwei Felder. Feld 1: zehn einzelne Einerwürfel, ein Pfeil, eine Zehnerstange aus zehn Würfeln. Feld 2: ein Einerwürfel als Streifen gezeichnet, ein Pfeil, derselbe Streifen in zehn gleiche Zehntel geschnitten.",
    "Genau zehn Würfel, genau zehn Zehntel; Stange und Würfelreihe gleich lang.",
    "Feld 1: „10 Einer = 1 Zehner“. Feld 2: „1 Einer = 10 Zehntel“.",
    "Die beiden Tausch-Pfeile mit der Zahl 10.",
    "Es müssen genau zehn sein und man muss sie zählen können. Die Zehntel sind gleich groß.",
    "Die Stellenwerttafel von Rechenregel 1 ist dieselbe Idee als Tabelle. Zweiersystem: je zwei Würfel werden gebündelt (1, 2, 4, 8). Runden: Zahlengerade von 340 bis 350 mit 347 – näher an 350."),
  [lambda: 10 * 1 == 10, lambda: F(1) == 10 * F(1, 10), lambda: abs(347 - 350) < abs(347 - 340)]),
 "Bausteine": ("Jede natürliche Zahl ab 2 lässt sich so lange in Faktoren zerlegen, bis nur noch Primzahlen übrig sind – und es kommen immer dieselben heraus, gleich wie man anfängt. Teiler, Vielfache, ggT, kgV und das Kürzen lassen sich an diesen Bausteinen ablesen.",
  Z("Zwei Zerlegungsbäume nebeneinander für die Zahl 60. Links: 60 → 6 und 10 → 2, 3 und 2, 5. Rechts: 60 → 4 und 15 → 2, 2 und 3, 5. Die Primzahlen am Ende stehen in Kreisen.",
    "Beide Bäume gleich hoch; die Endkreise gleich groß.",
    "Unter beiden Bäumen dieselbe Zeile: „60 = 2 · 2 · 3 · 5“.",
    "Die Primzahlen in den Kreisen – in beiden Bäumen dieselben vier.",
    "In den Kreisen stehen nur Primzahlen. Jedes Paar von Ästen ergibt malgenommen die Zahl darüber. Beide Bäume enden mit denselben Bausteinen.",
    "Zwei Reihen von Bausteinen untereinander: 12 = 2 · 2 · 3 und 18 = 2 · 3 · 3; die gemeinsamen Bausteine 2 und 3 sind umrahmt (ggT 6), alle zusammen ergeben das kgV 36."),
  [lambda: 6 * 10 == 4 * 15 == 2 * 2 * 3 * 5 == 60, lambda: 2 * 2 * 3 == 12 and 2 * 3 * 3 == 18, lambda: __import__("math").gcd(12, 18) == 6 and 12 * 18 // 6 == 36]),
 "Schreibweisen": ("Ein Bruch, eine Kommazahl und eine Prozentangabe können genau dieselbe Zahl meinen. Wer zwischen den drei Schreibweisen wechseln kann, wählt jeweils die, mit der sich am leichtesten rechnet.",
  Z("Drei Felder für dieselbe Zahl. Feld 1: ein Streifen, in zwei Teile geteilt, eines gefärbt. Feld 2: eine Zahlengerade von 0 bis 1 in Zehnteln, ein Punkt bei 0,5. Feld 3: ein Hunderterfeld (10 mal 10), 50 Felder gefärbt.",
    "Streifen und Zahlengerade gleich lang und genau untereinander; die Färbung des Streifens endet über dem Punkt 0,5. Im Hunderterfeld fünf volle Spalten.",
    "Feld 1: „½“. Feld 2: „0,5“. Feld 3: „50 %“. Darunter: „½ = 0,5 = 50 %“.",
    "Die gemeinsame Stelle: das Ende der Färbung und der Punkt auf der Geraden.",
    "Die drei Darstellungen müssen sichtbar gleich viel zeigen: genau die Hälfte. Im Hunderterfeld genau 50 Felder.",
    "Dieselben drei Felder für ¼ = 0,25 = 25 %. Für ⅓ = 0,333… ≈ 33,3 %: Hier geht die Kommazahl nie zu Ende (Periode)."),
  [lambda: F(1, 2) == F(5, 10) == F(50, 100), lambda: F(1, 4) == F(25, 100), lambda: abs(1 / 3 - 0.333) < 0.001]),
 "Hoch und zurück": ("Potenzieren fragt: Was kommt heraus? Die Wurzel fragt zurück: Welche Zahl wurde potenziert? Der Logarithmus fragt: Mit welcher Hochzahl? Alle drei gehören zu einer einzigen Gleichung.",
  Z("Ein Quadrat aus Einheitsquadraten. An der Seite steht die Seitenlänge, im Quadrat die Fläche. Ein Pfeil führt von der Seite zur Fläche, ein zweiter zurück.",
    "Quadrat 3 mal 3 Karos, 9 Einheitsquadrate.",
    "An der Seite „3“, in der Fläche „9“. Am Hin-Pfeil „hoch 2“, am Rück-Pfeil „Wurzel“. Darunter zwei Zeilen: „3² = 9“ und „√9 = 3“.",
    "Die beiden Pfeile als Paar.",
    "Genau 9 abzählbare Quadrate. Die Pfeile zeigen in entgegengesetzte Richtungen.",
    "Würfel aus 2 mal 2 mal 2 Einheitswürfeln: „2³ = 8“ und „dritte Wurzel aus 8 ist 2“. Klasse 10, ohne Bild als drei Zeilen zu einer Gleichung: 2³ = 8 (Potenz: Was kommt heraus?), ∛8 = 2 (Wurzel: welche Basis?), log₂ 8 = 3 (Logarithmus: welche Hochzahl?)."),
  [lambda: 3 ** 2 == 9, lambda: 2 ** 3 == 8, lambda: __import__("math").log2(8) == 3]),
 # ───── Algebra ─────
 "Term": ("Ein Term schreibt eine Rechnung auf, bevor man die Zahl kennt. Zwei Terme, die ganz verschieden aussehen, können für jede Zahl dasselbe liefern – dann darf man den einen durch den anderen ersetzen. Das ist der Sinn jeder Termumformung.",
  Z("Zwei Rechenketten untereinander, jede von links nach rechts: Eingabe-Kästchen, Pfeile mit Rechenschritten, Ausgabe-Kästchen. Kette 1: x → „· 2“ → „+ 3“. Kette 2: x → „+ 1“ → „· 2“ → „+ 1“. Rechts daneben eine Tabelle mit drei Eingaben und den Ausgaben beider Ketten.",
    "Tabelle: x = 1, 2, 5. Ausgaben beider Ketten: 5, 7, 13.",
    "Über Kette 1 „2 · x + 3“, über Kette 2 „2 · (x + 1) + 1“. Tabellenköpfe: „x“, „2 · x + 3“, „2 · (x + 1) + 1“.",
    "Die zwei Ausgabe-Spalten der Tabelle: Zeile für Zeile dieselbe Zahl.",
    "Die Ausgaben müssen stimmen. Die Ketten laufen in Leserichtung. Die Reihenfolge der Schritte entspricht dem Term (Klammer zuerst).",
    "Das Rechteck von Rechenregel 6 als Quadrat mit der Seite a + b, in vier Felder a², a · b, a · b, b² geteilt: binomische Formel. Parabel mit tiefstem Punkt für „Kleinster und größter Wert“."),
  [lambda: all(2 * x + 3 == 2 * (x + 1) + 1 for x in range(-9, 10)), lambda: [2 * x + 3 for x in (1, 2, 5)] == [5, 7, 13]]),
 "Erlaubte Zahlen": ("Nicht jede Zahl darf in jeden Term: Durch null kann man nicht teilen, und aus einer negativen Zahl gibt es keine Quadratwurzel. Wer das vor dem Rechnen klärt, erkennt Scheinlösungen.",
  Z("Eine Zahlengerade von −1 bis 5, durchgehend kräftig gezeichnet – nur bei 2 sitzt ein offener Ring (ein Loch). Darüber der Term. Darunter eine kleine Tabelle mit drei Einsetzungen.",
    "Ring genau bei 2. Tabelle: x = 1 ergibt −1; x = 2 „geht nicht“; x = 3 ergibt 1.",
    "Über der Geraden: „1 : (x − 2)“. Am Ring: „x = 2 ist nicht erlaubt: Der Nenner wäre 0“.",
    "Der offene Ring bei 2.",
    "Der Ring ist offen, nicht gefüllt. Überall sonst ist die Gerade durchgezogen. In der Tabelle steht bei x = 2 kein Zahlenwert.",
    "Dieselbe Gerade für √(x − 2): kräftig erst ab 2 nach rechts, bei 2 ein gefüllter Punkt, links davon dünn und grau („nicht erlaubt“)."),
  [lambda: F(1, 1 - 2) == -1 and F(1, 3 - 2) == 1, lambda: 2 - 2 == 0]),
 "Gleichung lösen": ("Eine Gleichung ist eine Frage: Für welche Zahlen stimmt sie? Die Antwort kann eine Zahl sein, mehrere, keine oder ein ganzer Bereich. Umformen ist nur der schnelle Weg dorthin; Einsetzen zeigt, ob die Antwort stimmt.",
  Z("Eine Zahlengerade von 2 bis 7. Unter den Zahlen 3, 4, 5 und 6 steht jeweils, was beim Einsetzen links herauskommt, und ein Haken oder ein Kreuz.",
    "Eingesetzt in 2 · x + 2: bei 3 ergibt sich 8, bei 4 ergibt sich 10, bei 5 ergibt sich 12, bei 6 ergibt sich 14.",
    "Oben: „2 · x + 2 = 12“. Unter 3: „8 ✗“. Unter 4: „10 ✗“. Unter 5: „12 ✓“. Unter 6: „14 ✗“. Darunter: „Lösung: x = 5“.",
    "Der Haken bei 5 und der Punkt 5 auf der Geraden.",
    "Die eingesetzten Werte müssen stimmen. Genau ein Haken.",
    "Dieselbe Gerade von −4 bis 4 für x² = 9: Haken bei −3 und bei 3. Für die Ungleichung x + 5 < 2: offener Ring bei −3 und ein kräftiger Strahl nach links (alle Zahlen kleiner als −3)."),
  [lambda: [2 * x + 2 for x in (3, 4, 5, 6)] == [8, 10, 12, 14], lambda: [x for x in range(-4, 5) if x * x == 9] == [-3, 3], lambda: all((x + 5 < 2) == (x < -3) for x in range(-9, 9))]),
 "Höherer Grad": ("Bei Gleichungen mit x² hilft das Hin- und Herschieben einzelner Summanden nicht weiter. Bringt man alles auf eine Seite und zerlegt in Faktoren, greift das Nullprodukt: Jeder Faktor liefert eine Lösung. Wo die Gegenrechnung reicht (x² = 49), ist sie der kürzere Weg.",
  Z("Zwei Felder. Feld 1: drei Rechenzeilen untereinander mit Pfeilen dazwischen, darunter die zwei Kästen von Rechenregel 14. Feld 2: eine Parabel im Koordinatensystem, die die x-Achse an zwei Stellen schneidet.",
    "Feld 2: Parabel durch (−3 | 0), (2 | 0) und (0 | −6), tiefster Punkt bei (−0,5 | −6,25). Achsen von −4 bis 3 und von −7 bis 4.",
    "Feld 1: „x² + x = 6“, Pfeil „− 6 auf beiden Seiten“, „x² + x − 6 = 0“, Pfeil „zerlegen“, „(x − 2) · (x + 3) = 0“, darunter „x = 2 oder x = −3“. Feld 2: „y = x² + x − 6“, an den Schnittpunkten „−3“ und „2“.",
    "Die Null auf der rechten Seite – und in Feld 2 die beiden Schnittpunkte mit der x-Achse.",
    "Rechts muss genau 0 stehen. Die Parabel schneidet die x-Achse genau bei −3 und 2. Zwischen den Lösungen steht „oder“.",
    "Feld 1 für x² = 49 mit dem Rückweg von Rechenregel 12: zwei Pfeile zu 7 und −7. Feld 2 mit einer Parabel, die die Achse nur berührt (eine Lösung) oder gar nicht trifft (keine)."),
  [lambda: all((x - 2) * (x + 3) == x * x + x - 6 for x in range(-9, 10)), lambda: 2 * 2 + 2 == 6 and (-3) ** 2 + (-3) == 6, lambda: F(-1, 2) ** 2 + F(-1, 2) - 6 == F(-25, 4)]),
 # ───── Geld und Verhältnisse ─────
 "Größe": ("Eine Größe besteht aus Zahl und Einheit. Dieselbe Länge kann 3 m oder 300 cm heißen: Je kleiner die Einheit, desto mehr davon braucht man. Wer das im Kopf hat, weiß bei jeder Umrechnung, ob die Zahl größer oder kleiner werden muss.",
  Z("Ein Balken, darüber und darunter je ein Maßband. Das obere Maßband ist in Meter geteilt, das untere in Dezimeter.",
    "Balken 3 m lang. Oben 3 Abschnitte, unten 30 Abschnitte; je 10 untere Abschnitte passen genau unter einen oberen.",
    "Oben „3 m“, unten „30 dm“. Darunter: „3 m = 30 dm = 300 cm“.",
    "Die beiden Zahlen 3 und 30 an derselben Länge.",
    "Beide Maßbänder beginnen und enden genau am Balken. Die Dezimeter sind gleich lang.",
    "Dieselbe Zeichnung für 2 h = 120 min (Umrechnungszahl 60) und 1,5 kg = 1 500 g. Maßstab 1 : 100: ein Plan-Balken von 3 cm über dem „echten“ von 3 m."),
  [lambda: 3 * 10 == 30 and 3 * 100 == 300, lambda: 2 * 60 == 120, lambda: F(3, 2) * 1000 == 1500]),
 "Wert für eins": ("Bei proportionalen Größen gehört zu jeder Einheit derselbe Wert. Darum gilt: doppelte Menge, doppelter Preis – und die Hälfte kostet die Hälfte. Dreisatz, Maßstab und Steigung sind Anwendungen davon.",
  Z("Eine doppelte Zahlengerade: oben die Menge, unten der Preis, beide beginnen bei 0 genau übereinander. Senkrechte dünne Linien verbinden zusammengehörige Werte.",
    "Oben 0, 1, 2, 3, 4, 5, 6 kg in gleichen Abständen. Unten 0 €; 2,50 €; 5 €; 7,50 €; 10 €; 12,50 €; 15 €.",
    "Oben „kg“, unten „€“. Ein Bogenpfeil oben von 3 nach 6 mit „· 2“, ein Bogenpfeil unten von 7,50 nach 15 mit „· 2“.",
    "Das Paar 1 kg und 2,50 € (der Wert für eins) und die beiden gleichen Bogenpfeile.",
    "Beide Geraden beginnen bei 0 an derselben Stelle. Gleiche Abstände. Die beiden Bogenpfeile sind gleich lang und tragen dieselbe Beschriftung.",
    "Dieselben Zahlen als Dreisatz-Tabelle (Rechenregel 11) und als Gerade durch den Ursprung und (1 | 2,5). Gegenstück, eigenes Feld: drei Rechtecke mit gleicher Fläche 12 (2 mal 6, 3 mal 4, 4 mal 3) für die indirekte Proportionalität."),
  [lambda: [F(5, 2) * k for k in range(7)] == [0, F(5, 2), 5, F(15, 2), 10, F(25, 2), 15], lambda: 2 * 6 == 3 * 4 == 4 * 3 == 12]),
 "Prozent als Faktor": ("Prozent ist nur ein anderes Wort für Hundertstel. Ein Anteil in Prozent sagt, wie viele von hundert gleichen Teilen gemeint sind. Wächst etwas um 20 %, hat man danach 120 Hundertstel – also das 1,2-fache.",
  Z("Zwei Felder. Feld 1: ein Hunderterfeld (10 mal 10), 25 Felder gefärbt. Feld 2: ein Streifen mit zwei Skalen – oben Prozent, unten Euro.",
    "Feld 1: zweieinhalb Spalten, also 25 von 100 Feldern. Feld 2: oben 0 % bis 100 % in Zehnerschritten, unten 0 € bis 60 €; markiert sind 1 % mit 0,60 € und 80 % mit 48 €.",
    "Feld 1: „25 von 100 = 25 %“. Feld 2: „80 % von 60 € sind 48 €“.",
    "Feld 1: die 25 gefärbten Felder. Feld 2: die Markierung bei 80 % und 48 €.",
    "Genau 100 Felder, genau 25 gefärbt. In Feld 2 beginnen beide Skalen bei 0, und 100 % steht genau über 60 €.",
    "Feld 2 verlängert: Streifen bis 120 %, das Stück von 100 % bis 120 % anders markiert – „plus 20 % heißt mal 1,2: aus 50 € werden 60 €“. Zinseszins als Treppe: 1 000 €, mal 1,05 gleich 1 050 €, mal 1,05 gleich 1 102,50 €."),
  [lambda: F(80, 100) * 60 == 48 and F(1, 100) * 60 == F(6, 10), lambda: 50 * F(12, 10) == 60, lambda: 1000 * F(105, 100) ** 2 == F(110250, 100)]),
 # ───── Funktionen ─────
 "Zuordnung": ("Eine Funktion ist eine Zuordnung, bei der zu jedem x genau ein y gehört. Man kann sie als Tabelle, als Graph oder als Gleichung zeigen; jede Darstellung lässt sich in die anderen übersetzen.",
  Z("Drei Felder für dieselbe Funktion. Feld 1: Tabelle mit vier Wertepaaren. Feld 2: Koordinatensystem mit den vier Punkten und der Geraden durch sie. Feld 3: die Gleichung.",
    "Wertepaare: (0 | 1), (1 | 3), (2 | 5), (3 | 7). Achsen von −1 bis 4 und von −1 bis 8, gleiche Einheiten.",
    "Feld 1: Köpfe „x“ und „y“. Feld 3: „y = 2 · x + 1“. In Feld 2 eine gestrichelte senkrechte Linie bei x = 2, die den Graphen genau einmal trifft.",
    "Das Wertepaar (2 | 5): in der Tabelle umrahmt, im Graphen als kräftiger Punkt, in der Gleichung als Zeile „2 · 2 + 1 = 5“.",
    "Alle vier Punkte liegen genau auf der Geraden. Die senkrechte Linie trifft den Graphen nur einmal.",
    "Feld 2 mit einem Kreis statt der Geraden: Die senkrechte Linie trifft zweimal – keine Funktion. Feld 2 mit markierten Punkten (0 | 1) und (−0,5 | 0): Achsenabschnitt und Nullstelle."),
  [lambda: [2 * x + 1 for x in range(4)] == [1, 3, 5, 7], lambda: 2 * F(-1, 2) + 1 == 0]),
 "Wachstum": ("Es gibt zwei Grundarten zu wachsen. Kommt in jedem Schritt gleich viel dazu, liegen die Punkte auf einer Geraden. Wird in jedem Schritt mit derselben Zahl malgenommen, wird die Kurve immer steiler und überholt jede Gerade.",
  Z("Ein Koordinatensystem mit zwei Graphen, die im selben Punkt beginnen: eine Gerade und eine Kurve. An beiden sind die Punkte für x = 0 bis 4 markiert; zwischen den Punkten kleine Treppenstufen.",
    "Gerade: (0 | 1), (1 | 3), (2 | 5), (3 | 7), (4 | 9). Kurve: (0 | 1), (1 | 2), (2 | 4), (3 | 8), (4 | 16). x-Achse 0 bis 4, y-Achse 0 bis 16.",
    "An den Stufen der Geraden jeweils „+ 2“, an den Stufen der Kurve jeweils „· 2“. Graphen beschriftet mit „immer plus 2“ und „immer mal 2“.",
    "Die Stufenbeschriftungen „+ 2“ und „· 2“.",
    "Beide Graphen beginnen in (0 | 1). Bis x = 2 liegt die Gerade höher, ab x = 3 die Kurve. Die Punkte liegen genau.",
    "Dieselben Zahlen als zwei Zahlenfolgen (1, 3, 5, 7, 9 und 1, 2, 4, 8, 16). Zinsen ohne und mit Zinseszins."),
  [lambda: [1 + 2 * x for x in range(5)] == [1, 3, 5, 7, 9] and [2 ** x for x in range(5)] == [1, 2, 4, 8, 16], lambda: 1 + 2 * 2 > 2 ** 2 and 1 + 2 * 3 < 2 ** 3]),
 "Gleichung und Form": ("An der Gleichung erkennt man, wie der Graph aussieht, bevor man einen einzigen Punkt berechnet: x allein gibt eine Gerade, x² eine Parabel, x im Nenner eine Hyperbel. Ändert man die Gleichung an einer Stelle, bewegt sich der Graph auf eine vorhersagbare Weise.",
  Z("Vier kleine Koordinatensysteme in einer Reihe, jedes mit einem Graphen und seiner Gleichung: Gerade, Parabel, Hyperbel, Knick.",
    "Alle vier mit Achsen von −3 bis 3. Parabel durch (−2 | 4), (−1 | 1), (0 | 0), (1 | 1), (2 | 4) – dafür y-Achse bis 4. Hyperbel durch (1 | 1), (2 | 0,5), (0,5 | 2) und gespiegelt im dritten Viertel.",
    "„y = x“, „y = x²“, „y = 1 : x“, „y = |x|“.",
    "In jeder Gleichung die Stelle, die die Form bestimmt: x, x², das x unter dem Bruchstrich, die Betragsstriche.",
    "Die Parabel ist symmetrisch zur y-Achse. Die Hyperbel berührt keine Achse. Der Knick liegt genau im Ursprung.",
    "**Zweite Reihe, drei Felder (Verschieben):** y = x², y = x² + 2 (2 nach oben), y = (x − 3)² (3 nach rechts – nicht nach links). Ganzrationale Funktion y = x · (x − 2) · (x + 2) mit den Nullstellen −2, 0, 2."),
  [lambda: [x * x for x in (-2, -1, 0, 1, 2)] == [4, 1, 0, 1, 4], lambda: (3 - 3) ** 2 == 0, lambda: [x for x in range(-3, 4) if x * (x - 2) * (x + 2) == 0] == [-2, 0, 2]]),
 # ───── Daten und Zufall ─────
 "Kennzahl": ("Mittelwert, Median und Spannweite fassen viele Werte in einer Zahl zusammen. Das macht Daten vergleichbar – aber zwei ganz verschiedene Datenreihen können denselben Mittelwert haben. Deshalb braucht man meist zwei Kennzahlen: eine für die Mitte und eine für die Streuung.",
  Z("Zwei Punktreihen untereinander über derselben Zahlengeraden von 0 bis 10. Jede Reihe hat vier Punkte. In beiden steht an derselben Stelle ein Dreieck als Zeichen für den Mittelwert.",
    "Reihe A: Punkte bei 4, 5, 5, 6 (die zwei Fünfen übereinander). Reihe B: Punkte bei 1, 2, 8, 9. Mittelwert in beiden: 5.",
    "„A: 4, 5, 5, 6 – Mittelwert 5“. „B: 1, 2, 8, 9 – Mittelwert 5“.",
    "Die beiden Dreiecke bei 5, genau untereinander.",
    "Die Punkte stehen genau an ihren Werten. Beide Dreiecke stehen genau bei 5.",
    "Eine dritte Reihe mit Ausreißer: 2, 3, 3, 4, 18 – Mittelwert 6 (Dreieck), Median 3 (Strich). Dieselbe Gerade mit einem Boxplot."),
  [lambda: F(4 + 5 + 5 + 6, 4) == 5 == F(1 + 2 + 8 + 9, 4), lambda: F(2 + 3 + 3 + 4 + 18, 5) == 6 and sorted([2, 3, 3, 4, 18])[2] == 3]),
 "Vom Teil aufs Ganze": ("Man kann selten alle fragen oder alles messen. Eine Stichprobe verrät nur dann etwas über das Ganze, wenn der Zufall sie ausgewählt hat und wenn sie groß genug ist. Das gilt für Umfragen genauso wie für das Schätzen von Wahrscheinlichkeiten durch viele Versuche.",
  Z("Ein Feld mit 100 Punkten (10 mal 10), ein Teil davon gefärbt; die gefärbten häufen sich in der linken unteren Ecke. Zwei Rahmen greifen je 10 Punkte heraus: Rahmen 1 verstreut über das ganze Feld (durch dünne Linien zu einer Gruppe verbunden), Rahmen 2 ein Block in der linken unteren Ecke.",
    "Genau 30 der 100 Punkte gefärbt. Rahmen 1 enthält 3 gefärbte von 10, Rahmen 2 enthält 8 gefärbte von 10.",
    "Am Feld: „30 von 100 = 30 %“. Rahmen 1: „zufällig gezogen: 3 von 10 = 30 %“. Rahmen 2: „aus einer Ecke: 8 von 10 = 80 %“.",
    "Die beiden Rahmen und ihre Ergebnisse.",
    "Die Zahlen müssen abzählbar stimmen (30, 3, 8). Rahmen 2 muss erkennbar dort liegen, wo sich die gefärbten Punkte häufen.",
    "Ein Verlauf für das Gesetz der großen Zahlen: Anteil „Kopf“ nach 10, 100 und 1 000 Würfen, der sich 0,5 nähert – die Werte dafür müssen aus einer echten oder simulierten Wurfreihe stammen, nicht erfunden sein."),
  [lambda: F(30, 100) == F(3, 10), lambda: F(8, 10) != F(30, 100)]),
 "Anteil": ("Kann ein Versuch auf mehrere Arten ausgehen und ist keine davon bevorzugt, dann ist die Wahrscheinlichkeit eines Ereignisses sein Anteil an allen Möglichkeiten. Dafür muss man nur richtig zählen.",
  Z("Sechs Würfelflächen in einer Reihe, mit 1 bis 6 Augen. Die Flächen mit 2, 4 und 6 Augen sind hervorgehoben.",
    "Alle sechs Flächen gleich groß und in gleichen Abständen.",
    "Darunter: „gerade Zahl: 3 von 6 = ½“.",
    "Die drei Flächen 2, 4 und 6.",
    "Alle sechs Flächen sind gleich groß (gleich wahrscheinlich). Genau drei sind hervorgehoben. Die Augenzahlen stimmen.",
    "Dieselbe Reihe mit den übrigen drei Flächen markiert: Gegenereignis, ½ + ½ = 1. Gegenbeispiel als eigenes Feld: ein Glücksrad mit drei Feldern, die die Hälfte, ein Viertel und ein Viertel einnehmen – „3 Felder, aber nicht jedes hat ⅓“. Zählprinzip: 3 Hosen und 2 Hemden als Gitter mit 6 Kombinationen."),
  [lambda: F(3, 6) == F(1, 2), lambda: F(1, 2) + F(1, 4) + F(1, 4) == 1, lambda: 3 * 2 == 6]),
 "Stufen": ("Besteht ein Versuch aus mehreren Schritten, zeichnet man einen Baum. Ein Pfad ist ein Ausgang des ganzen Versuchs; seine Wahrscheinlichkeit ist das Produkt entlang des Pfades. Gehören mehrere Pfade zum Ereignis, addiert man sie.",
  Z("Ein Baumdiagramm für zwei Münzwürfe: von der Wurzel zwei Äste (Kopf, Zahl), von jedem wieder zwei. Vier Enden.",
    "An jedem Ast „½“. An den Enden: KK, KZ, ZK, ZZ, jeweils mit „¼“.",
    "Unter dem Baum zwei Zeilen: „Pfad Kopf–Zahl: ½ · ½ = ¼“ und „genau einmal Kopf: ¼ + ¼ = ½“.",
    "Zwei verschiedene Markierungen: ein Pfad entlang (mal) – und die zwei Enden KZ und ZK zusammen (plus).",
    "Die Wahrscheinlichkeiten an den Ästen eines Knotens ergeben zusammen 1. Vier Enden, zusammen 1.",
    "Derselbe Baum für eine Urne mit 3 roten und 2 blauen Kugeln ohne Zurücklegen: erster Zug 3/5 und 2/5; nach Rot: 2/4 und 2/4; nach Blau: 3/4 und 1/4; „rot, rot: 3/5 · 2/4 = 3/10“. Dieselben Zahlen als Vierfeldertafel."),
  [lambda: F(1, 2) * F(1, 2) == F(1, 4) and 2 * F(1, 4) == F(1, 2), lambda: F(3, 5) * F(2, 4) == F(3, 10), lambda: F(3, 5) * F(2, 4) + F(3, 5) * F(2, 4) + F(2, 5) * F(3, 4) + F(2, 5) * F(1, 4) == 1]),
}
PLANETEN = ["Zahlen", "Algebra", "Geld und Verhältnisse", "Funktionen", "Daten und Zufall"]
soll = [k for p in PLANETEN for k, _, _ in gb.IDEEN[p]]
assert sorted(V) == sorted(soll), set(V) ^ set(soll)
n_proben = 0
for k, (warum, z, proben) in V.items():
    assert warum and all(z[f] for f in z), k
    for pr in proben:
        assert pr() is True, k
        n_proben += 1
teile = []
for p in PLANETEN:
    teile.append(f"# Planet „{p}“\n")
    for nr, (kurz, genau, ns) in enumerate(gb.IDEEN[p], 1):
        warum, z, _ = V[kurz]
        teile += [f"## {p}, Idee {nr}: {kurz}", "", f"> **{gb.IDEE_SPRUCH[kurz][0]}**", "", f"**Genau gesagt:** {genau}", "", f"**Warum diese Idee trägt:** {warum}", "",
                  f"**Trägt {len(ns)} Gesetze:** {', '.join(gb.NR[n] + ' ' + n for n in ns)}", "", "**Zeichen-Vorgabe**", zeichnung_text(z), ""]
open(os.path.join(HIER, "zeichen-vorgaben-fuenf-planeten.md"), "w", encoding="utf-8").write(f"""# Gesetzbuch · Zeichen-Vorgaben für die tragenden Ideen der übrigen fünf Planeten

Mathe-Profi, 26.11.2026 (Auftrag 13). Erzeugt von `ideen_zeichnung.py`. {len(V)} Vorgaben; {n_proben} Rechenproben zu den Zahlen der Vorgaben, alle bestanden (Lauf „OK“).
Die Vorgaben für Fläche und Raum und für Geometrie stehen in den beiden Planeten-Dateien, die für die 14 Rechenregeln in `sonne.md`. Damit hat jeder der 42 Sätze der Ebene 1 genau eine Hauptzeichnung.

**Für alle Vorgaben gilt** (mit dem Designer abgestimmt): maßstäblich · ein Karo ist eine Einheit · Hervorhebung nie durch Farbe allein · „·“ ist nur Malzeichen · höchstens vier Felder je Reihe, Nebenzeichnungen als eigene Reihe · keine anderen Zahlen als die genannten.
Die Zeile „Gleiche Zeichnung, andere Beschriftung“ nennt Nebenzeichnungen; sie sind kein Muss für die Übersicht.

{chr(10).join(teile)}
## Nicht geprüft

- Geprüft sind die Zahlen (Rechenproben). Ob eine Vorgabe am Handy lesbar zu zeichnen ist, kann nur der Designer sagen.
- Keine Vorgabe ist gezeichnet oder mit einem Kind erprobt.
- Der Verlauf zum Gesetz der großen Zahlen hat bewusst keine Zahlen: Sie müssen aus einer echten oder simulierten Wurfreihe kommen.
""")
print(f"{len(V)} Zeichen-Vorgaben, {n_proben} Rechenproben")
print("OK")
