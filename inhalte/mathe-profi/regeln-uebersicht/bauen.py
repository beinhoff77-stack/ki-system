"""Mathe-Profi, Aufträge 10 und 11: Gesetzbuch – die Sonne (14 Rechenregeln), zweite Fassung nach der Gegenprüfung.

Aufruf: python3 -I inhalte/mathe-profi/regeln-uebersicht/bauen.py
Hält die Regeln als Daten, rechnet jedes Beispiel nach, prüft die Klasse jedes Beispiels gegen inhalte/themenliste.json
(Gymnasium, Zuordnung der App) und schreibt sonne.md. Das Gesamtverzeichnis und die Planeten erzeugt gesetzbuch.py.
Nur Inhalte.
"""
import json
import os
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
LISTE = {t["thema_schluessel"]: t for t in json.load(open(os.path.join(WURZEL, "inhalte", "themenliste.json"), encoding="utf-8"))}
ART = {"V": "Vorwissen", "E": "Einführung", "A": "Anwendung"}


def gleich(f, g, aus=()):
    pkt = [F(p) for p in (-5, -3, -2, 2, 3, 5, 7, F(1, 2)) if p not in aus]
    return all(f(p) == g(p) for p in pkt)


def Z(sehen, masse, schrift, betont, falsch, varianten):
    return dict(sehen=sehen, masse=masse, schrift=schrift, betont=betont, falsch=falsch, varianten=varianten)


# Beispiel: (Klasse, Art V/E/A, Thema der App, Text – eine Aussage je Zeile, Probe)
R = [
 dict(nr=13, name="Stellenwert", schicht=1,
      merk="Mal 10 rückt jede Ziffer in die nächsthöhere Stelle, geteilt durch 10 in die nächstniedrigere.",
      warum="Unser Zahlensystem bündelt in Zehnern: Jede Stelle ist zehnmal so viel wert wie die Stelle rechts von ihr. Beim Malnehmen mit 10 wird deshalb aus jedem Einer ein Zehner, aus jedem Zehntel ein Einer. Die Ziffern bleiben, nur ihre Plätze ändern sich. Das Komma markiert die Grenze zwischen Einern und Zehnteln.",
      gilt="Gilt für jede Zahl im Zehnersystem, auch hinter dem Komma.",
      fehler="„Eine Null anhängen“: 2,5 · 10 ist 25, nicht 2,50.",
      verwandt="Runden ist eine eigene Vereinbarung (Planet Zahlen). Prozent heißt Hundertstel (Planet Geld und Verhältnisse). Flächen- und Raumeinheiten: Umrechnungszahl 100 und 1 000 (Planet Fläche und Raum).",
      weg=[],
      z=Z("Eine Stellenwerttafel mit den Spalten H, Z, E, Komma-Strich, z, h. Zwei Zeilen: oben die Zahl 2,5 (2 in E, 5 in z), unten 25 (2 in Z, 5 in E). Von jeder Ziffer der oberen Zeile führt ein schräger Pfeil zu derselben Ziffer eine Spalte weiter links.",
          "Fünf gleich breite Spalten; der Komma-Strich steht fest zwischen E und z und ist in beiden Zeilen an derselben Stelle.",
          "Spaltenköpfe H, Z, E, z, h; rechts neben den Zeilen „2,5“ und „· 10 = 25“.",
          "Die beiden Pfeile (gleiche Farbe, gleiche Länge, gleiche Richtung).",
          "Das Komma darf nicht wandern. Es darf keine Null erscheinen. Beide Ziffern müssen gleich weit rücken.",
          "Dieselbe Tafel für 3 400 m = 3,4 km (geteilt durch 1 000: drei Spalten nach rechts) und für 0,0003 = 3 · 10⁻⁴."),
      bsp=[(5, "E", "zahlen.natuerlich", "340 · 10 = 3 400", lambda: 340 * 10 == 3400),
           (5, "A", "groessen.einheiten", "3 400 m = 3,4 km", lambda: F(3400, 1000) == F(34, 10)),
           (6, "E", "bruch.dezimal", "2,5 · 10 = 25", lambda: F(5, 2) * 10 == 25),
           (6, "A", "bruch.prozent", "15 % = 15 Hundertstel = 0,15", lambda: F(15, 100) == F(3, 20)),
           (8, "A", "terme.potenzgesetze_ganzzahlig", "3 · 10⁻⁴ = 0,0003", lambda: 3 * F(10) ** -4 == F(3, 10000))]),
 dict(nr=1, name="Plus und Minus mit negativen Zahlen", schicht=1,
      merk="Beim Addieren zeigt das Vorzeichen der zweiten Zahl die Richtung. Beim Subtrahieren gehst du genau andersherum.",
      warum="Auf der Zahlengeraden heißt „plus eine positive Zahl“ nach rechts gehen und „plus eine negative Zahl“ nach links. Subtrahieren ist das Gegenteil des Addierens, also läuft man jeweils in die andere Richtung. Deshalb ist 3 − (−2) dasselbe wie 3 + 2.",
      gilt="Gilt für alle Zahlen: ganze Zahlen, Brüche, Dezimalzahlen und später Terme.",
      fehler="3 − (−2) = 1 statt 5: das zweite Minus übersehen. Und: −30 für größer halten als −10.",
      verwandt="Betrag und Gegenzahl (Planet Zahlen). Bei Mal und Geteilt gilt eine andere Regel: die Vorzeichenregel.",
      weg=[],
      z=Z("Zwei Zahlengeraden untereinander von −1 bis 6. Oben: Startpunkt bei 3, ein Bogenpfeil zwei Einheiten nach links, Landung bei 1. Unten: Startpunkt bei 3, ein Bogenpfeil zwei Einheiten nach rechts, Landung bei 5.",
          "Gleicher Maßstab auf beiden Geraden, Teilstriche an jeder ganzen Zahl; beide Starts genau übereinander bei 3.",
          "Über der oberen Geraden „3 + (−2) = 1“ und „einmal umdrehen“, über der unteren „3 − (−2) = 5“ und „zweimal umdrehen“. Start mit vollem Punkt, Ziel mit Ring. Am Start steht eine kleine Figur mit Blick nach rechts; je Minuszeichen zeigt ein kleiner Bogenpfeil eine Kehrtwende.",
          "Jedes Minuszeichen und die zugehörige Kehrtwende in derselben Farbe: oben eine, unten zwei.",
          "Beide Pfeile müssen genau zwei Einheiten lang sein. Der Start darf nicht bei 0 liegen. Die Null muss sichtbar sein.",
          "Dieselben zwei Geraden für −½ − ¾ (Teilstriche in Vierteln) und für 3x − 5x (Einheit „x“)."),
      bsp=[(5, "E", "zahlen.ganz", "3 + (−2) = 1", lambda: 3 + (-2) == 1),
           (5, "E", "zahlen.ganz", "3 − (−2) = 5", lambda: 3 - (-2) == 5),
           (6, "A", "bruch.rechnen", "−½ − ¾ = −1¼", lambda: -F(1, 2) - F(3, 4) == -F(5, 4)),
           (7, "A", "terme.umformen", "3x − 5x = −2x", lambda: gleich(lambda x: 3 * x - 5 * x, lambda x: -2 * x)),
           (8, "A", "gleichungen.ungleichungen", "x + 5 < 2, also x < −3", lambda: all((x + 5 < 2) == (x < -3) for x in range(-9, 9)))]),
 dict(nr=2, name="Vorzeichen bei Mal und Geteilt", schicht=1,
      merk="Bei Mal und Geteilt mit zwei Zahlen ungleich null: Gleiche Vorzeichen ergeben Plus, verschiedene Minus.",
      warum="In der Reihe 3 · (−2) = −6, 2 · (−2) = −4, 1 · (−2) = −2, 0 · (−2) = 0 wird das Ergebnis jedes Mal um 2 größer. Setzt man sie fort, muss (−1) · (−2) = 2 sein. Nur so bleiben die übrigen Rechengesetze gültig. Für Geteilt gilt dasselbe, weil Teilen die Gegenrechnung zum Malnehmen ist.",
      gilt="Gilt für zwei Zahlen, die beide nicht null sind. Ist ein Faktor null, ist das Produkt null und hat kein Vorzeichen.",
      fehler="Die Regel auf Plus übertragen: (−3) + (−4) ist −7, nicht +7.",
      verwandt="Ungleichungen: Mal oder geteilt durch eine negative Zahl dreht das Ungleichheitszeichen um (Planet Algebra). Potenzen mit negativer Basis (Planet Zahlen).",
      weg=["Plus und Minus mit negativen Zahlen"],
      z=Z("Eine Treppe aus fünf Stufen, die von links nach rechts ansteigt. Auf den Stufen stehen die Ergebnisse −6, −4, −2, 0, +2; unter jeder Stufe die Rechnung 3 · (−2), 2 · (−2), 1 · (−2), 0 · (−2), (−1) · (−2).",
          "Alle Stufen gleich hoch (eine Stufe = 2). Die Stufe mit 0 liegt auf einer durchgezogenen Null-Linie.",
          "Zwischen den Stufen jeweils „+ 2“. Der erste Faktor zählt sichtbar herunter: 3, 2, 1, 0, −1.",
          "Die letzte Stufe (−1) · (−2) = +2, über der Null-Linie.",
          "Die Treppe muss steigen, nicht fallen. Die Stufen müssen gleich hoch sein. Die +2 muss oberhalb der Null-Linie liegen.",
          "Keine – diese Zeichnung bleibt bei Zahlen. Für (−2x) · (−3) = 6x wird nur das Ergebnis darunter geschrieben."),
      bsp=[(5, "E", "zahlen.rechengesetze", "(−3) · (−4) = 12", lambda: (-3) * (-4) == 12),
           (5, "E", "zahlen.rechengesetze", "(−12) : 4 = −3", lambda: F(-12, 4) == -3),
           (6, "A", "bruch.rechnen", "(−⅔) · ¾ = −½", lambda: -F(2, 3) * F(3, 4) == -F(1, 2)),
           (7, "A", "terme.umformen", "(−2x) · (−3) = 6x", lambda: gleich(lambda x: (-2 * x) * (-3), lambda x: 6 * x)),
           (8, "A", "gleichungen.ungleichungen", "−2x < 6, also x > −3", lambda: all((-2 * x < 6) == (x > -3) for x in range(-9, 9))),
           (9, "A", "gleichungen.quadratisch", "x² = 25 hat die Lösungen 5 und −5", lambda: 5 ** 2 == 25 == (-5) ** 2)]),
 dict(nr=3, name="Reihenfolge beim Rechnen", schicht=1,
      merk="Klammer zuerst, dann Hoch, dann Punkt, dann Strich – Gleichrangiges von links nach rechts.",
      warum="Die Reihenfolge ist eine Vereinbarung, damit jeder dieselbe Rechnung gleich liest. Sie folgt dem Aufbau der Rechenarten: Hoch ist wiederholtes Malnehmen, Mal ist wiederholtes Addieren – die „stärkere“ Rechnung bindet enger. Klammern sind das Mittel, die Reihenfolge zu ändern.",
      gilt="Gilt für jeden Term. Mal und Geteilt sind gleichrangig, ebenso Plus und Minus: Dann wird von links nach rechts gerechnet, zum Beispiel 12 : 3 · 2 = 8.",
      fehler="Von links nach rechts durchrechnen: 2 + 3 · 4 = 20. Und: 2 + 3x zu 5x zusammenziehen.",
      verwandt="Die zuletzt ausgeführte Rechnung gibt dem Term seinen Namen: 2 + 3x ist eine Summe (Planet Algebra).",
      weg=[],
      z=Z("Vier Treppenstufen von oben nach unten, beschriftet „Klammer“, „Hoch“, „Punkt · :“, „Strich + −“. Rechts daneben die Rechnung 2 + 3 · 4 in drei Zeilen: erst mit einem Rahmen um 3 · 4, dann 2 + 12, dann 14.",
          "Stufen gleich breit und gleich hoch. Der Rahmen umschließt genau „3 · 4“.",
          "Auf der dritten Stufe die Zeichen · und :, auf der vierten + und −. Kleiner Zusatz an Stufe 3 und 4: „von links nach rechts“.",
          "Der Rahmen um 3 · 4 in der Farbe der Stufe „Punkt“.",
          "Die oberste Stufe muss die erste sein (Klammer). Punkt und Strich dürfen nicht auf einer Höhe stehen. · und : stehen zusammen auf einer Stufe.",
          "Dieselbe Treppe mit ½ + ½ · ½, mit 2 + 3x und mit 2 · 3² – immer wird der Teil eingerahmt, der zuerst kommt."),
      bsp=[(5, "E", "zahlen.rechengesetze", "2 + 3 · 4 = 14", lambda: 2 + 3 * 4 == 14),
           (5, "E", "zahlen.rechengesetze", "12 : 3 · 2 = 8", lambda: F(12, 3) * 2 == 8),
           (6, "A", "bruch.rechnen", "½ + ½ · ½ = ¾", lambda: F(1, 2) + F(1, 2) * F(1, 2) == F(3, 4)),
           (7, "A", "terme.umformen", "2 + 3x bleibt 2 + 3x", lambda: not gleich(lambda x: 2 + 3 * x, lambda x: 5 * x)),
           (8, "A", "terme.potenzgesetze_ganzzahlig", "3 · 2⁻² = ¾", lambda: 3 * F(2) ** -2 == F(3, 4)),
           (9, "A", "gleichungen.quadratisch", "−3² = −9", lambda: -(3 ** 2) == -9),
           (10, "A", "gleichungen.exponential", "2 · 3ˣ = 18: erst durch 2, dann 3ˣ = 9, also x = 2", lambda: 2 * 3 ** 2 == 18)]),
 dict(nr=6, name="Tauschen, Klammern, Zusammenfassen", schicht=2,
      merk="In einer Summe darfst du die Summanden tauschen und neu klammern, in einem Produkt die Faktoren. Zusammenfassen: gleicher Buchstabenteil – Vorzahlen addieren.",
      warum="Bei einer Summe und bei einem Produkt kommt es nicht auf die Reihenfolge und nicht auf die Klammerung an (Vertauschungs- und Verbindungsgesetz). Zusammenfassen heißt zählen: 3 Stück a und 4 Stück a sind 7 Stück a.",
      gilt="Gilt für reine Summen und reine Produkte. Eine Differenz schreibt man vorher als Summe (5 − 3 = 5 + (−3)), dann wandert das Minus mit seiner Zahl mit.",
      fehler="Bei Minus oder Geteilt einfach tauschen: 5 − 3 ist nicht 3 − 5. Und: 3a + 4b zu 7ab zusammenfassen.",
      verwandt="Vertauschungsgesetz (Kommutativgesetz) und Verbindungsgesetz (Assoziativgesetz) sind die Fachnamen. 0 ändert beim Addieren nichts, 1 ändert beim Malnehmen nichts.",
      weg=[],
      z=Z("Oben: drei Kärtchen in einer Reihe „25“, „· 37“, „· 4“; darunter dieselben Kärtchen umgestellt „25“, „· 4“, „· 37“, die ersten beiden mit einer Klammer zusammengefasst und „100“ darunter. Unten: zwei Körbe; in den linken fallen die Kärtchen „+3a“ und „+4a“ (darunter „7a“), in den rechten „+2b“.",
          "Jedes Kärtchen trägt sein Rechenzeichen fest vorn. Kärtchen gleich groß.",
          "Oben „25 · 37 · 4 = 25 · 4 · 37 = 3 700“. Unten „3a + 2b + 4a = 7a + 2b“.",
          "Das Zeichen auf jedem Kärtchen (es wandert mit).",
          "Kein Kärtchen ohne Zeichen außer dem ersten. Im linken Korb dürfen nur a-Kärtchen liegen. a und b dürfen nicht in einem Korb landen.",
          "Dieselben Kärtchen für 12 − 30 + 18 − 5 (Kärtchen „+12“, „−30“, „+18“, „−5“)."),
      bsp=[(5, "E", "zahlen.rechengesetze", "25 · 37 · 4 = 25 · 4 · 37 = 3 700", lambda: 25 * 37 * 4 == 3700),
           (5, "E", "zahlen.ganz", "12 − 30 + 18 = 12 + 18 − 30 = 0", lambda: 12 - 30 + 18 == 0),
           (6, "A", "bruch.rechnen", "0,5 · 7 · 2 = 0,5 · 2 · 7 = 7", lambda: F(1, 2) * 7 * 2 == 7),
           (7, "E", "terme.umformen", "3a + 2b + 4a = 7a + 2b", lambda: all(3 * a + 2 * b + 4 * a == 7 * a + 2 * b for a in (2, 3) for b in (5, 7))),
           (9, "A", "zahlen.reell", "3 · √2 + 2 · √2 = 5 · √2", lambda: 3 + 2 == 5)]),
 dict(nr=4, name="Ausmultiplizieren und Ausklammern", schicht=2,
      merk="Der Faktor vor der Klammer multipliziert jeden Summanden – vorwärts ausmultiplizieren, rückwärts ausklammern.",
      warum="Ein Rechteck mit den Seiten a und (b + c) hat dieselbe Fläche wie die zwei Teilrechtecke a · b und a · c zusammen. Rückwärts gelesen ist es das Ausklammern: Steckt in jedem Summanden derselbe Faktor, darf man ihn vor eine Klammer ziehen.",
      gilt="Gilt für einen Faktor vor einer Summe oder Differenz – für Zahlen, Brüche und Terme.",
      fehler="Nur den ersten Summanden malnehmen: 3 · (x + 2) = 3x + 2. Und: die Regel auf Hoch übertragen – (a + b)² ist nicht a² + b².",
      verwandt="Summe mal Summe und binomische Formeln (Planet Algebra). Kürzen von Bruchtermen braucht vorher das Ausklammern.",
      weg=["Reihenfolge beim Rechnen"],
      z=Z("Ein Rechteck, durch einen senkrechten Strich in zwei Teilrechtecke geteilt. Linke Seite: Höhe 6. Obere Seite: zwei Abschnitte 20 und 2 (zusammen 22 – für das Minus-Beispiel siehe Varianten). In jedem Teilrechteck steht seine Fläche: 120 und 12.",
          "Maßstäblich: Höhe 6 Einheiten, Breite 20 + 2 Einheiten; der Trennstrich steht bei 20. Für die Buchstaben-Fassung dasselbe Rechteck mit den Abschnitten x und 2 (x deutlich länger als 2, ohne Kästchen).",
          "Links außen der Faktor, oben über jedem Abschnitt der Summand, in jedem Feld das Teilprodukt. Darunter die Zeile „6 · (20 + 2) = 6 · 20 + 6 · 2“.",
          "Der Faktor links und die zwei Teilflächen – der Faktor in derselben Farbe wie die beiden Malzeichen in der Zeile darunter.",
          "Beide Teilrechtecke müssen dieselbe Höhe haben. Es dürfen nicht zwei getrennte Rechtecke sein. Der Trennstrich darf nicht in der Mitte stehen, wenn die Summanden verschieden sind.",
          "**Dieselbe Zeichnung, vier Beschriftungen:** (1) 6 · (20 + 2), (2) 6 · (20 − 2): großes Rechteck Breite 20, rechts ein gestrichelt abgetrenntes Stück Breite 2, (3) 3 · (x + 2), (4) 3/2 · (4 + ½) = 6 + ¾ – Höhe 1,5 und Breite 4,5, damit das Rechteck maßstäblich bleibt und trotzdem dieselbe Gestalt hat wie die anderen drei. Reihenfolge der Felder: Zahlen mit Plus, mit x, mit Brüchen, zuletzt Zahlen mit Minus. Im Minus-Feld stehen in den Flächen die Werte „108“ und „12“. Rückwärts gelesen (Ausklammern): 3x + 6 = 3 · (x + 2). Zusatzbild für den häufigen Fehler: Quadrat mit Seite a + b, in vier Felder a², ab, ab, b² geteilt."),
      bsp=[(5, "E", "zahlen.rechengesetze", "6 · 98 = 6 · 100 − 6 · 2 = 588", lambda: 6 * 98 == 6 * 100 - 6 * 2 == 588),
           (6, "A", "bruch.rechnen", "4 · 2,5 = 4 · 2 + 4 · 0,5 = 10", lambda: 4 * F(5, 2) == 4 * 2 + 4 * F(1, 2) == 10),
           (7, "E", "terme.umformen", "3 · (x + 2) = 3x + 6", lambda: gleich(lambda x: 3 * (x + 2), lambda x: 3 * x + 6)),
           (7, "E", "terme.umformen", "3x + 6 = 3 · (x + 2)", lambda: gleich(lambda x: 3 * x + 6, lambda x: 3 * (x + 2))),
           (8, "A", "terme.bruchterme", "(3x + 6) : (x + 2) = 3 für x ≠ −2", lambda: gleich(lambda x: (3 * x + 6) / (x + 2), lambda x: F(3), aus=(-2,))),
           (9, "A", "gleichungen.quadratisch", "x² + 5x = x · (x + 5)", lambda: gleich(lambda x: x * x + 5 * x, lambda x: x * (x + 5))),
           (10, "A", "gleichungen.polynom", "x³ − 4x = x · (x² − 4)", lambda: gleich(lambda x: x ** 3 - 4 * x, lambda x: x * (x * x - 4)))]),
 dict(nr=5, name="Minus vor der Klammer", schicht=2,
      merk="Löst du eine Minusklammer auf, wechselt jeder Summand in der Klammer sein Vorzeichen.",
      warum="Ein Minus vor der Klammer heißt „mal (−1)“. Der Faktor −1 multipliziert jeden Summanden, also wechselt jedes Vorzeichen. Im Alltag: Wer 20 € hat und einen Einkauf von 8 € mit 3 € Rabatt bezahlt, behält 20 − 8 + 3 €.",
      gilt="Gilt für jede Klammer, vor der ein Minus steht. Malzeichen in der Klammer bleiben: −(2 · x − 3) = −2 · x + 3.",
      fehler="Nur das erste Vorzeichen wechseln: 5x − (3x − 2) = 5x − 3x − 2.",
      verwandt="Folgt aus dem Ausmultiplizieren und der Vorzeichenregel; steht eigens da, weil hier besonders viele Fehler entstehen. Ein Plus vor der Klammer ändert nichts.",
      weg=["Ausmultiplizieren und Ausklammern", "Vorzeichen bei Mal und Geteilt"],
      z=Z("Ein Kassenzettel mit drei Zeilen: „Guthaben 20 €“, darunter eingerückt und mit einer Klammer zusammengefasst „Einkauf 8 €“ und „Rabatt −3 €“, darunter „bleibt 15 €“. Rechts daneben die Rechnung in zwei Zeilen: 20 − (8 − 3) und 20 − 8 + 3.",
          "Die Klammer am Zettel umfasst genau die zwei mittleren Zeilen.",
          "In der zweiten Rechenzeile stehen „− 8“ und „+ 3“ genau unter „8“ und „− 3“ der ersten Zeile.",
          "Die beiden Summanden in der Klammer und ihre neuen Vorzeichen, paarweise in derselben Farbe; das „20“ bleibt neutral.",
          "Beide Vorzeichen müssen als gewechselt erkennbar sein (aus „8“ wird „− 8“, aus „− 3“ wird „+ 3“). Das Ergebnis 15 muss stimmen.",
          "Dieselbe Paar-Markierung für 5x − (3x − 2) = 5x − 3x + 2 (ohne Zettel, nur die zwei Rechenzeilen)."),
      bsp=[(5, "V", "zahlen.rechengesetze", "20 − (8 − 3) = 20 − 8 + 3 = 15", lambda: 20 - (8 - 3) == 20 - 8 + 3 == 15),
           (7, "E", "terme.umformen", "5x − (3x − 2) = 5x − 3x + 2", lambda: gleich(lambda x: 5 * x - (3 * x - 2), lambda x: 5 * x - 3 * x + 2)),
           (8, "A", "gleichungen.bruch", "7 − 2 · (x − 3) = 7 − 2x + 6", lambda: gleich(lambda x: 7 - 2 * (x - 3), lambda x: 7 - 2 * x + 6)),
           (9, "A", "gleichungen.quadratisch", "(x + 1)² − (x² − 3) = 2x + 4", lambda: gleich(lambda x: (x + 1) ** 2 - (x * x - 3), lambda x: 2 * x + 4))]),
 dict(nr=12, name="Potenzen", schicht=2,
      merk="Hoch n heißt: n gleiche Faktoren. Bei gleicher Basis gilt: Mal – Hochzahlen addieren.",
      warum="2³ · 2² ist (2 · 2 · 2) · (2 · 2) – zusammen fünf Zweien, also 2⁵. Teilt man, fallen Faktoren weg; deshalb werden die Hochzahlen abgezogen. Setzt man die Reihe 8, 4, 2 fort, ergibt sich 2⁰ = 1 und 2⁻¹ = ½: Eine negative Hochzahl heißt Kehrwert.",
      gilt="„n gleiche Faktoren“ gilt für n = 1, 2, 3 … Hoch 0 und negative Hochzahlen sind eigens festgelegt und verlangen eine Basis, die nicht null ist. Das Additionsgesetz verlangt dieselbe Basis.",
      fehler="Basis mal Hochzahl rechnen: 2³ = 6. Und: 2³ + 2² zu 2⁵ machen – das Gesetz gilt nur bei Mal.",
      verwandt="Die weiteren Potenzgesetze, Wurzeln und Logarithmen (Planet Zahlen). a · a ist a², aber a + a ist 2a.",
      weg=["Reihenfolge beim Rechnen"],
      z=Z("Eine Zeile mit drei Zweien in einer Klammer und zwei Zweien in einer zweiten Klammer, dazwischen ein Malpunkt: (2 · 2 · 2) · (2 · 2). Unter der ersten Klammer „2³“, unter der zweiten „2²“, unter allen fünf zusammen eine lange Klammer mit „2⁵“. Darunter eine Zahlenreihe 8, 4, 2, 1, ½, ¼ mit den Hochzahlen 3, 2, 1, 0, −1, −2 darüber und „: 2“ zwischen den Gliedern.",
          "Die fünf Zweien stehen in gleichen Abständen; die untere Reihe hat sechs gleich breite Felder.",
          "„2³ · 2² = 2⁵“ und „3 + 2 = 5“. In der Reihe: Hochzahl über jedem Wert.",
          "Die erste Klammer: drei Zweien, hingeschrieben und malgenommen – dazu die Hochzahl 3 in derselben Farbe. Zweitrangig: die Hochzahlen 2 und 5; in der Reihe das Feld 2⁰ = 1.",
          "Es müssen genau fünf Zweien sein. In der Reihe darf 2⁰ nicht 0 sein und 2⁻¹ nicht negativ.",
          "Dieselbe Zeile mit x statt 2: (x · x · x) · (x · x) = x⁵. Dieselbe Reihe mit 10: 1 000, 100, 10, 1, 0,1, 0,01."),
      bsp=[(5, "E", "zahlen.potenzen_basis", "2⁵ = 2 · 2 · 2 · 2 · 2 = 32", lambda: 2 ** 5 == 32),
           (6, "A", "zahlen.potenzen_zehner", "10³ · 10² = 10⁵", lambda: 10 ** 3 * 10 ** 2 == 10 ** 5),
           (7, "E", "terme.potenzgesetze_natuerlich", "x² · x³ = x⁵", lambda: gleich(lambda x: x ** 2 * x ** 3, lambda x: x ** 5)),
           (8, "E", "terme.potenzgesetze_ganzzahlig", "a⁻² = 1 : a² für a ≠ 0", lambda: gleich(lambda a: a ** -2, lambda a: 1 / (a * a))),
           (10, "A", "funktionen.exponential_log", "2ˣ · 2³ = 2 hoch (x + 3)", lambda: all(2 ** x * 2 ** 3 == 2 ** (x + 3) for x in range(1, 6)))]),
 dict(nr=10, name="Erweitern und Kürzen", schicht=3,
      merk="Ein gemeinsamer Faktor ungleich null darf in Zähler und Nenner dazukommen oder wegfallen – der Wert des Bruchs bleibt.",
      warum="Der Nenner sagt, in wie viele gleiche Teile das Ganze geteilt ist, der Zähler, wie viele davon gemeint sind. Teilt man jedes Teil noch einmal, gibt es doppelt so viele Teile und man nimmt doppelt so viele: Die Menge bleibt gleich, nur die Einteilung wird feiner.",
      gilt="Der Faktor darf nicht null sein. Er muss den ganzen Zähler und den ganzen Nenner betreffen.",
      fehler="Aus Summen kürzen: (x + 6) : (x + 2) zu 3 machen. Erst ausklammern, dann kürzen.",
      verwandt="ggT zum vollständigen Kürzen, kgV als Hauptnenner (Planet Zahlen). Dasselbe bei Verhältnissen und Bruchtermen.",
      weg=[],
      z=Z("Zwei gleich lange Streifen genau untereinander. Der obere ist in 2 gleiche Teile geteilt, 1 Teil gefärbt. Der untere ist in 4 gleiche Teile geteilt, 2 Teile gefärbt. Die gefärbten Flächen enden an derselben senkrechten Linie.",
          "Beide Streifen exakt gleich lang und gleich hoch; die Teilung des unteren halbiert jedes Teil des oberen.",
          "Links neben den Streifen „½“ und „2/4“; dazwischen ein Pfeil „Zähler und Nenner · 2“ (abwärts) und „: 2“ (aufwärts).",
          "Die gemeinsame Endlinie der gefärbten Flächen.",
          "Die gefärbten Längen müssen genau gleich sein. Die Teile eines Streifens müssen gleich groß sein.",
          "Dieselben zwei Streifen für 12/18 = 2/3 (18 und 3 Teile) und – ohne Streifen, nur als Rechenzeile mit gleich gefärbtem Faktor – für (3 · (x + 2)) : (1 · (x + 2)) = 3."),
      bsp=[(6, "E", "bruch.brueche", "½ = 2/4", lambda: F(1, 2) == F(2, 4)),
           (6, "E", "bruch.brueche", "12/18 = 2/3", lambda: F(12, 18) == F(2, 3)),
           (7, "A", "terme.umformen", "6x : 9 = 2x : 3", lambda: gleich(lambda x: 6 * x / 9, lambda x: 2 * x / 3)),
           (8, "A", "terme.bruchterme", "(3x + 6) : (x + 2) = 3 · (x + 2) : (x + 2) = 3 für x ≠ −2", lambda: gleich(lambda x: (3 * x + 6) / (x + 2), lambda x: F(3), aus=(-2,))),
           (9, "A", "abbildungen.aehnlichkeit", "Das Seitenverhältnis 6 : 9 ist dasselbe wie 2 : 3", lambda: F(6, 9) == F(2, 3))]),
 dict(nr=11, name="Rechnen mit Brüchen", schicht=3,
      merk="Gleichnamige Brüche: Zähler addieren oder subtrahieren, Nenner behalten. Mal: Zähler mal Zähler, Nenner mal Nenner. Geteilt: mit dem Kehrwert malnehmen.",
      warum="Addieren kann man nur gleich große Teile – Halbe und Drittel müssen erst in Sechstel umgerechnet werden. „Mal ½“ heißt „die Hälfte von“; deshalb werden beim Malnehmen die Teile feiner. Teilen fragt „wie oft passt es hinein“: In 6 passt ½ zwölfmal – das ist dasselbe wie 6 mal 2.",
      gilt="Nenner sind nie null; beim Teilen darf auch der Bruch, durch den geteilt wird, nicht null sein. Ungleichnamige Brüche erst gleichnamig machen.",
      fehler="Zähler plus Zähler und Nenner plus Nenner: ½ + ⅓ = 2/5.",
      verwandt="Bruchterme und Bruchgleichungen (Planet Algebra). Pfadregeln bei Wahrscheinlichkeiten (Planet Daten und Zufall).",
      weg=["Erweitern und Kürzen"],
      z=Z("Drei gleich lange Streifen untereinander. Der erste ist halbiert, eine Hälfte gefärbt. Der zweite ist gedrittelt, ein Drittel gefärbt (andere Farbe). Der dritte ist in sechs Teile geteilt: drei Teile in der ersten Farbe, direkt daneben zwei Teile in der zweiten Farbe.",
          "Alle Streifen exakt gleich lang; die Sechstel-Teilung passt zu beiden oberen Teilungen (Hilfslinien dünn nach unten gezogen).",
          "Neben den Streifen „½“, „⅓“ und „3/6 + 2/6 = 5/6“.",
          "Die fünf gefärbten Sechstel im dritten Streifen.",
          "Im dritten Streifen dürfen nicht 2 von 5 Feldern gefärbt sein. Die Farbfelder müssen lückenlos aneinanderliegen. Das sechste Feld bleibt leer.",
          "Dieselben Streifen für x/2 + x/3 = 5x/6 (ganzer Streifen = x). **Zwei Nebenfelder für die Sprüche zwei und drei:** Mal – ein Einheitsquadrat, waagerecht in Viertel und senkrecht in Drittel geteilt (12 Felder); drei Viertel sind hell gefärbt, davon zwei Drittel kräftig: 6 von 12 Feldern, „⅔ · ¾ = 6/12 = ½“. Geteilt – sechs ganze Streifen, jeder halbiert: 12 Hälften, „6 : ½ = 6 · 2 = 12“."),
      bsp=[(6, "E", "bruch.rechnen", "½ + ⅓ = 3/6 + 2/6 = 5/6", lambda: F(1, 2) + F(1, 3) == F(5, 6)),
           (6, "E", "bruch.rechnen", "⅔ · ¾ = 6/12 = ½", lambda: F(2, 3) * F(3, 4) == F(1, 2)),
           (6, "E", "bruch.rechnen", "6 : ½ = 6 · 2 = 12", lambda: 6 / F(1, 2) == 12),
           (7, "A", "gleichungen.linear", "x/2 + x/3 = 5x/6", lambda: gleich(lambda x: x / 2 + x / 3, lambda x: 5 * x / 6)),
           (8, "A", "terme.bruchterme", "2/x + 3/(x + 1) = (5x + 2) : (x · (x + 1)) für x ≠ 0 und x ≠ −1", lambda: gleich(lambda x: 2 / x + 3 / (x + 1), lambda x: (5 * x + 2) / (x * (x + 1)), aus=(0, -1))),
           (10, "A", "stochastik.mehrstufig", "Zwei unabhängige Würfe einer fairen Münze, zweimal Kopf: ½ · ½ = ¼", lambda: F(1, 2) * F(1, 2) == F(1, 4))]),
 dict(nr=14, name="Verhältnis (Dreisatz)", schicht=3,
      merk="Bei gleichem Preis je Einheit: erst auf eins, dann auf die gewünschte Menge.",
      warum="Wenn zwei Größen im selben Verhältnis wachsen, gehört zu jeder Einheit derselbe Wert. Wer den Wert für eine Einheit kennt, kennt jeden anderen: 3 kg kosten 7,50 €, also 1 kg 2,50 €, also 5 kg 12,50 €. Allgemein: y = k · x, und k ist der Wert für eine Einheit.",
      gilt="Gilt nur bei direkter Proportionalität: doppelte Menge, doppelter Wert; zur Menge null gehört der Wert null.",
      fehler="Den Dreisatz anwenden, obwohl ein fester Betrag dazukommt (Grundgebühr) oder obwohl mehr von dem einen weniger von dem anderen bedeutet.",
      verwandt="Umgekehrte Proportionalität: Das Produkt bleibt gleich (x · y = k). Prozent, Maßstab, Steigung einer Geraden, Strahlensatz und Sinus sind dieselbe Idee.",
      weg=["Erweitern und Kürzen"],
      z=Z("Eine Tabelle mit zwei Spalten („kg“ und „€“) und drei Zeilen: 3 | 7,50, dann 1 | 2,50, dann 5 | 12,50. Links und rechts der Tabelle Bogenpfeile von Zeile 1 zu Zeile 2 mit „: 3“ und von Zeile 2 zu Zeile 3 mit „· 5“.",
          "Die Pfeile links und rechts stehen auf gleicher Höhe und tragen dieselbe Beschriftung.",
          "Spaltenköpfe mit Einheit. Die mittlere Zeile ist mit „für eins“ gekennzeichnet.",
          "Die mittlere Zeile (1 kg – 2,50 €) und die vier Pfeilbeschriftungen, links und rechts gleichfarbig.",
          "Links und rechts muss dieselbe Rechnung stehen. Die mittlere Zeile muss die Einheit 1 zeigen. Kein Kreuz-Schema.",
          "Dieselbe Tabelle für Prozent (80 % | 48 €, 1 % | 0,60 €, 100 % | 60 €) und für die Steigung (2 nach rechts | 3 nach oben, 1 nach rechts | 1,5 nach oben) – dort zusätzlich ein Steigungsdreieck."),
      bsp=[(5, "E", "groessen.proportional", "3 kg kosten 7,50 €, also kostet 1 kg 2,50 € und 5 kg kosten 12,50 €", lambda: F(750, 3) == 250 and 250 * 5 == 1250),
           (6, "A", "bruch.prozent", "15 von 60 sind 25 %", lambda: F(15, 60) == F(25, 100)),
           (7, "A", "bruch.prozent_grundwert", "80 % sind 48 €, also ist 1 % 0,60 € und 100 % sind 60 €", lambda: F(48, 80) == F(6, 10) and F(6, 10) * 100 == 60),
           (8, "A", "funktionen.linear", "Steigung 1,5: je 2 nach rechts geht es 3 nach oben", lambda: F(3, 2) * 2 == 3),
           (9, "A", "abbildungen.aehnlichkeit", "Strahlensatz: 2 : 3 = 4 : x, also x = 6", lambda: F(2, 3) == F(4, 6))]),
 dict(nr=8, name="Gegenrechnung", schicht=4,
      merk="Rechne den Weg rückwärts: Was zuletzt gerechnet wurde, machst du zuerst rückgängig.",
      warum="Zu jeder umkehrbaren Rechnung gibt es eine Gegenrechnung: Plus und Minus, Mal und Geteilt, Quadrat und Wurzel, später Hoch und Logarithmus. Wer weiß, was mit einer Zahl nacheinander gemacht wurde, findet sie, indem er den Weg rückwärts geht – wie beim Anziehen und Ausziehen: Der Schuh kam zuletzt, also kommt er zuerst weg.",
      gilt="Die Rechnung muss umkehrbar sein. „Mal null“ löscht die Zahl, das lässt sich nicht rückgängig machen; durch null kann man nicht teilen.",
      fehler="In derselben Reihenfolge zurückrechnen statt in umgekehrter. Und beim Quadrat nur eine Lösung nennen: x² = 49 hat die Lösungen 7 und −7.",
      verwandt="Die Wurzel aus x² ist der Betrag von x. Formeln umstellen (Planet Algebra). Umkehrfunktion (Planet Funktionen).",
      weg=["Reihenfolge beim Rechnen"],
      z=Z("Zwei Reihen untereinander. Oben von links nach rechts: ein leeres Kästchen □, ein Pfeil mit „− 12“, ein Zwischenkästchen, ein Pfeil mit „· 4“, das Kästchen −20. Unten von rechts nach links: −20, ein Pfeil mit „: 4“, das Zwischenkästchen −5, ein Pfeil mit „+ 12“, das Kästchen 7.",
          "Die Kästchen der beiden Reihen stehen genau untereinander; die unteren Pfeile zeigen nach links.",
          "Über der oberen Reihe „4 · (□ − 12) = −20“. Unter der unteren Reihe „□ = 7“.",
          "Die Pfeilpaare: „· 4“ und „: 4“ in einer Farbe, „− 12“ und „+ 12“ in einer zweiten.",
          "Die untere Reihe muss rechts beginnen. „: 4“ muss unter „· 4“ stehen, nicht unter „− 12“. Zwischenwert −5 muss stimmen.",
          "Dieselben zwei Reihen für das Formel-Umstellen (h → „· g“ → „: 2“ → A und zurück) und für x → „hoch 2“ → 49 (zurück: zwei Pfeile zu 7 und −7)."),
      bsp=[(5, "E", "gleichungen.einfach", "4 · (□ − 12) = −20: erst : 4, dann + 12, also □ = 7", lambda: 4 * (7 - 12) == -20 and F(-20, 4) + 12 == 7),
           (6, "A", "bruch.rechnen", "¾ von einer Zahl sind 12, also ist die Zahl 12 : ¾ = 16", lambda: F(3, 4) * 16 == 12),
           (7, "A", "bruch.prozent_grundwert", "Nach 20 % Aufschlag kostet es 60 €, vorher also 60 : 1,2 = 50 €", lambda: 60 / F(12, 10) == 50),
           (8, "A", "gleichungen.formeln", "A = g · h : 2 nach h: erst mal 2, dann durch g", lambda: F(12 * 7, 2) == 42 and F(2 * 42, 12) == 7),
           (9, "E", "gleichungen.quadratisch", "x² = 49, also x = 7 oder x = −7", lambda: 7 ** 2 == 49 == (-7) ** 2),
           (10, "E", "gleichungen.exponential", "2ˣ = 8, also x = 3", lambda: 2 ** 3 == 8)]),
 dict(nr=7, name="Gleichung als Waage", schicht=4,
      merk="Dieselbe umkehrbare Rechnung auf beiden Seiten ändert die Lösungen nicht.",
      warum="Das Gleichheitszeichen sagt: Links und rechts steht gleich viel. Nimmt man auf beiden Seiten einer Waage dasselbe weg oder halbiert beide Seiten, bleibt sie im Gleichgewicht. Weil man jede solche Rechnung zurücknehmen kann, geht keine Lösung verloren und keine kommt dazu.",
      gilt="Erlaubt: auf beiden Seiten dieselbe Zahl addieren oder subtrahieren; mit derselben Zahl ungleich null malnehmen oder durch sie teilen. Beim Malnehmen oder Teilen mit einem Term vorher klären, wo dieser Term null wird.",
      fehler="Nur einen Summanden malnehmen statt der ganzen Seite. Und: quadrieren und die neu entstandene Lösung nicht prüfen (aus x = 2 wird x² = 4 mit der zusätzlichen Lösung −2).",
      verwandt="Äquivalenzumformung ist der Fachname (Planet Algebra). Bei Ungleichungen dreht mal oder geteilt durch eine negative Zahl das Zeichen um.",
      weg=["Gegenrechnung"],
      z=Z("Eine Balkenwaage im Gleichgewicht, dreimal nebeneinander. Bild 1: links zwei Säckchen (jedes mit „x“) und zwei Kugeln, rechts zwölf Kugeln. Bild 2: links zwei Säckchen, rechts zehn Kugeln (auf beiden Seiten sind zwei Kugeln durchgestrichen oder entfernt). Bild 3: links ein Säckchen, rechts fünf Kugeln.",
          "Der Balken ist in allen drei Bildern waagerecht. Kugeln gleich groß und zählbar angeordnet (Zweierreihen).",
          "Unter den Bildern: „2x + 2 = 12“, „2x = 10“, „x = 5“. Zwischen den Bildern: „− 2 auf beiden Seiten“, „: 2 auf beiden Seiten“.",
          "Was auf beiden Seiten weggenommen wird (in Bild 1 die je zwei Kugeln, gleich markiert).",
          "Der Balken darf nie schief stehen. Die Kugelzahlen müssen stimmen (12, 10, 5). Links und rechts muss sichtbar dasselbe geschehen.",
          "Dieselbe Waage mit Zahlen statt Säckchen für Klasse 5 (□ + 7 = 3 geht mit Kugeln nicht – dort nur die Rechenzeilen mit gleicher Markierung)."),
      bsp=[(5, "E", "gleichungen.einfach", "□ + 7 = 3: auf beiden Seiten 7 abziehen, also □ = −4", lambda: -4 + 7 == 3),
           (7, "E", "gleichungen.linear", "2x + 2 = 12, also 2x = 10, also x = 5", lambda: 2 * 5 + 2 == 12),
           (8, "A", "gleichungen.bruch", "3/x + ½ = 5/x mit x ≠ 0: beide Seiten mal 2x, dann 6 + x = 10, also x = 4", lambda: F(3, 4) + F(1, 2) == F(5, 4)),
           (9, "A", "gleichungen.quadratisch", "2x² = 18, also x² = 9", lambda: 2 * 3 ** 2 == 18),
           (10, "A", "gleichungen.exponential", "3 · 2ˣ = 24, also 2ˣ = 8", lambda: 3 * 2 ** 3 == 24)]),
 dict(nr=15, name="Nullprodukt", schicht=4,
      merk="Ein Produkt ist genau dann null, wenn mindestens ein Faktor null ist.",
      warum="Null mal irgendetwas ist null. Umgekehrt kann aus zwei Zahlen, die beide nicht null sind, beim Malnehmen nie null werden. Deshalb darf man eine Gleichung „Produkt = 0“ in mehrere einfache Gleichungen zerlegen: Jeder Faktor für sich kann null sein.",
      gilt="Auf der einen Seite muss ein Produkt stehen, auf der anderen genau null.",
      fehler="Die Regel bei einer anderen Zahl anwenden: Aus (x − 2) · (x + 3) = 6 folgt nicht x − 2 = 6.",
      verwandt="Faktorisieren – durch Ausklammern oder mit einer binomischen Formel – bringt eine Gleichung in diese Form (Planet Algebra). Ein Nenner darf nicht null sein (Definitionsmenge).",
      weg=[],
      z=Z("Zwei Kästen nebeneinander, dazwischen ein Malpunkt, rechts „= 0“. Im ersten Kasten „x − 2“, im zweiten „x + 3“. Von jedem Kasten führt ein Pfeil nach unten zu einer eigenen kleinen Gleichung: „x − 2 = 0“ und „x + 3 = 0“, darunter „x = 2“ und „x = −3“. Zwischen den beiden unteren Spalten das Wort „oder“.",
          "Beide Kästen gleich groß, die zwei Spalten darunter genau unter den Kästen.",
          "Oben „(x − 2) · (x + 3) = 0“. Unten „x = 2 oder x = −3“.",
          "Die Null rechts und die beiden Kästen.",
          "Rechts muss 0 stehen, keine andere Zahl. Zwischen den Lösungen muss „oder“ stehen, nicht „und“.",
          "Dieselben Kästen mit „□“ und „7“ für Klasse 5 (□ · 7 = 0, also □ = 0) und mit drei Kästen x, x − 2, x + 2 für Klasse 10."),
      bsp=[(5, "V", "zahlen.rechengesetze", "0 · 7 = 0", lambda: 0 * 7 == 0),
           (5, "V", "gleichungen.einfach", "□ · 7 = 0, also □ = 0", lambda: [x for x in range(-5, 6) if x * 7 == 0] == [0]),
           (8, "A", "terme.bruchterme", "Der Nenner x · (x − 4) ist null für x = 0 oder x = 4", lambda: [x for x in range(-5, 9) if x * (x - 4) == 0] == [0, 4]),
           (9, "E", "gleichungen.quadratisch", "(x − 2) · (x + 3) = 0, also x = 2 oder x = −3", lambda: [x for x in range(-9, 9) if (x - 2) * (x + 3) == 0] == [-3, 2]),
           (10, "A", "gleichungen.polynom", "x · (x − 2) · (x + 2) = 0, also x = 0, x = 2 oder x = −2", lambda: [x for x in range(-9, 9) if x * (x - 2) * (x + 2) == 0] == [-2, 0, 2])]),
]
# Auftrag 12: je Regel ein einprägsamer Merksatz (höchstens etwa zwölf Wörter); der genaue Satz steht in "merk" („Genau gesagt“).
# nr → (Merksatz, Herkunft, [(verworfener Kandidat, Grund)])
SPRUCH = {
 13: ("Mal zehn: Jede Ziffer rückt eins nach links.", "eigen",
      [("Mal zehn: Null dran.", "falsch bei Kommazahlen"), ("Mal zehn: Komma eins nach rechts.", "unsichtbar bei 340; in der Zeichnung steht das Komma fest")]),
 1: ("Minus heißt umdrehen – zweimal umdrehen ist wieder geradeaus.", "eigen",
     [("Minus minus gibt plus.", "wird auf (−3) + (−4) übertragen"), ("Schulden abziehen heißt Geld bekommen.", "trägt nur einen der Fälle")]),
 2: ("Minus mal Minus gibt Plus, Minus mal Plus gibt Minus.", "überliefert",
     [("Gleiche Zeichen plus, verschiedene minus.", "ohne „mal“ – wird aufs Addieren übertragen"), ("Der Feind meines Feindes ist mein Freund.", "Bild ohne Rechnung")]),
 3: ("Klammer zuerst, dann Hoch, dann Punkt vor Strich.", "überliefert, ergänzt",
     [("Punkt vor Strich.", "allein unvollständig: Klammer und Hoch fehlen"), ("KlaPoPuStri.", "Kunstwort")]),
 6: ("Tauschen bei Plus und Mal. Zusammenfassen: nur Gleiches zu Gleichem.", "eigen",
     [("Äpfel und Birnen kann man nicht addieren.", "macht aus a einen Gegenstand statt einer Zahl"), ("Die Reihenfolge ist egal.", "falsch bei Minus und Geteilt")]),
 4: ("Was vor der Klammer steht, nimmt jeden in der Klammer mal.", "eigen",
     [("Jeder mit jedem.", "gehört zu Summe mal Summe"), ("Jeder kommt dran.", "ohne „mal“ unklar")]),
 5: ("Minus vor der Klammer dreht alle Zeichen um.", "überliefert",
     [("Minus vor der Klammer: aus Plus wird Minus.", "nennt nur eine Richtung"), ("Minusklammer heißt Vorzeichenwechsel.", "Fachwörter")]),
 12: ("Hoch drei heißt: die Zahl dreimal hinschreiben und malnehmen.", "eigen",
      [("Hoch ist Mal mit sich selbst.", "wie oft, bleibt offen"), ("Gleiche Basis: Hochzahlen plus.", "Fachwort; erst ab Klasse 7")]),
 10: ("Oben und unten dasselbe mal oder geteilt – der Bruch bleibt gleich.", "eigen",
      [("Aus Summen kürzen nur die Dummen.", "überliefert, aber beschämend; nennt nur den Fehler"), ("Zähler und Nenner gleich behandeln.", "falsch bei Plus und Minus")]),
 11: ("Plus und Minus: erst gleiche Nenner.<br>Mal: oben mal oben, unten mal unten.<br>Geteilt: mit dem Kehrwert malnehmen.", "überliefert; drei Sprüche für drei Regeln (Entscheidung des Projektleiters)",
      [("Plus: erst gleiche Nenner. Mal: oben mal oben, unten mal unten. Geteilt: Kehrwert.", "ein Spruch für drei Regeln – zu lang"), ("Nur Gleiches lässt sich zusammenzählen.", "deckt Mal und Geteilt nicht"), ("Bruch durch Bruch: umdrehen und malnehmen.", "welchen umdrehen, bleibt offen")]),
 14: ("Erst auf eins, dann auf viele.", "überliefert",
      [("Je mehr, desto mehr.", "gilt auch, wo kein Dreisatz gilt"), ("Über Kreuz malnehmen.", "Rezept ohne Sinn")]),
 8: ("Rückwärts rechnen: Was zuletzt kam, geht zuerst.", "eigen",
     [("Plus und Minus heben sich auf.", "nur ein Paar"), ("Schuhe vor Socken ausziehen.", "Bild ohne Rechnung – bleibt in der Erklärung")]),
 7: ("Eine Gleichung ist eine Waage: Was du links tust, musst du auch rechts tun.", "überliefert; Wortlaut des Nutzers",
     [("Auf beiden Seiten dasselbe.", "ohne Bild"), ("Rüberbringen und Zeichen wechseln.", "überliefert, erzeugt Fehler bei Mal und Geteilt")]),
 15: ("Mal ergibt nur null, wenn eine der Zahlen null ist.", "eigen",
      [("Null mal irgendwas ist null.", "nur eine Richtung"), ("Ein Produkt ist genau dann null, wenn mindestens ein Faktor null ist.", "richtig, aber nicht aufsagbar – steht unter „Genau gesagt“")]),
}


def woerter(text):
    return max(_woerter(z) for z in text.split("<br>"))


def _woerter(text):
    return len([w for w in text.replace("–", " ").split() if any(c.isalnum() for c in w)])


WIRK = {13: 'Die Ziffern, die rücken (in der Zeichnung jede Ziffer mit ihrem Pfeil); in der Rechenzeile „· 10“ oder „: 10“.', 1: 'Jedes Minuszeichen – Rechenzeichen wie Vorzeichen. Ein Plus wird nicht markiert.', 2: 'Die Vorzeichen der beiden Zahlen und das Vorzeichen des Ergebnisses.', 3: 'Der Teil, der zuerst gerechnet wird (Rahmen).', 6: 'Beim Tauschen: das Rechenzeichen zusammen mit seiner Zahl. Beim Zusammenfassen: der gleiche Buchstabenteil.', 4: 'Der Faktor vor der Klammer – an jeder Stelle, an der er auftritt.', 5: 'Das Minus vor der Klammer und jedes Vorzeichen, das wechselt (vorher und nachher als Paar).', 12: 'Die Hochzahl und die gleich vielen Faktoren.', 10: 'Der gemeinsame Faktor in Zähler und Nenner.', 11: 'Bei Plus und Minus: der gemeinsame Nenner. Bei Mal: Zähler mit Zähler. Bei Geteilt: der Kehrwert.', 14: 'Der Wert für eins.', 8: 'Jede Rechnung zusammen mit ihrer Gegenrechnung (als Paar).', 7: 'Was auf beiden Seiten getan wird.', 15: 'Die Null und der Faktor, der null wird.'}
for r in R:
    r["wirk"] = WIRK[r["nr"]]
    r["spruch"], r["herkunft"], r["verworfen"] = SPRUCH[r["nr"]]
    assert woerter(r["spruch"]) <= 14 and 2 <= len(r["verworfen"]) <= 3, (r["name"], woerter(r["spruch"]))
assert sorted(SPRUCH) == sorted(r["nr"] for r in R)

SCHICHT = {1: "Grundrechnen", 2: "Klammern und Potenzen", 3: "Brüche und Verhältnis", 4: "Gleichungen"}

# ── Prüfen ──
NAME = {r["nr"]: r["name"] for r in R}
NAMEN = [r["name"] for r in R]
assert len(R) == 14 and sorted(NAME) == [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]
for r in R:
    assert all(w in NAMEN for w in r["weg"]), r["name"]
    assert all(r[k] for k in ("merk", "warum", "gilt", "fehler", "verwandt")) and all(r["z"][k] for k in r["z"]), r["name"]
    assert len(r["merk"]) <= 200, (r["name"], len(r["merk"]))
    folge = [(k, "VEA".index(a)) for k, a, *_ in r["bsp"]]
    assert [k for k, _ in folge] == sorted(k for k, _ in folge), r["name"]
    assert any(a == "E" for _, a, *_ in r["bsp"]), r["name"]
    for k, art, thema, text, probe in r["bsp"]:
        assert probe() is True, (r["name"], k, text)
        assert art in ART and thema in LISTE, (r["name"], thema)
        assert LISTE[thema]["klasse"].get("gym_by") == k, (r["name"], k, thema, LISTE[thema]["klasse"].get("gym_by"))
        assert " · " not in text or "=" not in text.split(" · ")[0] or text.count("=") <= 3, text   # eine Aussage je Zeile
n_bsp = sum(len(r["bsp"]) for r in R)
KL = (5, 6, 7, 8, 9, 10)


def zelle(r, k):
    arten = [a for kk, a, *_ in r["bsp"] if kk == k]
    return "" if not arten else ("E" if "E" in arten else "A" if "A" in arten else "V")


def zeichnung_text(z):
    return "\n".join([f"- **Zu sehen:** {z['sehen']}", f"- **Maße:** {z['masse']}", f"- **Beschriftung:** {z['schrift']}", f"- **Hervorgehoben:** {z['betont']}",
                      f"- **Darf nicht falsch aussehen:** {z['falsch']}", f"- **Gleiche Zeichnung, andere Beschriftung:** {z['varianten']}"])


def regel_text(i, r):
    z = [f"### {i}. {r['name']}", "", "> **" + r['spruch'].replace("<br>", "**  \n> **") + "**", "", f"**Genau gesagt:** {r['merk']}", "", f"**Warum das gilt:** {r['warum']}", "", f"**Voraussetzung:** {r['gilt']}", "", f"**Häufiger Fehler:** {r['fehler']}", "",
         f"**Verwandt:** {r['verwandt']}", "", "| Klasse | Art | Dieselbe Regel in diesem Jahr | Thema in der App |", "|---|---|---|---|"]
    z += [f"| {k} | {ART[a]} | {text} | `{thema}` |" for k, a, thema, text, _ in r["bsp"]]
    z += ["", f"**Möglicher Erklärweg über:** {', '.join(r['weg']) or '–'} (zum Erklären hilfreich, keine Lernvoraussetzung)", "", f"**Wirkstelle** (in jedem Beispiel und in der Zeichnung gleich markiert): {r['wirk']}", "", "**Zeichen-Vorgabe**", zeichnung_text(r["z"])]
    return "\n".join(z)


if __name__ == "__main__" or True:
    matrix = ["| Regel | " + " | ".join(f"Kl. {k}" for k in KL) + " |", "|---|" + "---|" * len(KL)]
    for i, r in enumerate(R, 1):
        matrix.append(f"| {i} {r['name']} | " + " | ".join(zelle(r, k) for k in KL) + " |")
    schichten = "\n".join(f"| **{s} {SCHICHT[s]}** | " + ", ".join(f"{NAMEN.index(r['name']) + 1} {r['name']}" for r in R if r["schicht"] == s) + " |" for s in sorted(SCHICHT))
    merkliste = "\n".join(f"{i}. **{r['spruch']}**  \n   *{r['name']} – genau gesagt:* {r['merk']}" for i, r in enumerate(R, 1))
    nummern = ", ".join(f"{i} = Etikett {r['nr']}" for i, r in enumerate(R, 1))
    open(os.path.join(HIER, "sonne.md"), "w", encoding="utf-8").write(f"""# Gesetzbuch · Die Sonne: die {len(R)} Rechenregeln (vierte Fassung: Merksatz, „Genau gesagt“, Wirkstelle)

Mathe-Profi, 26.11.2026. Erzeugt von `bauen.py`; {n_bsp} Beispiele, jedes nachgerechnet (Lauf „OK“).
Die Sonne ist die Mitte des Gesetzbuchs: Diese Regeln bleiben von Klasse 5 bis 10 dieselben, nur das Gewand wechselt (Zahl, Bruch, Buchstabe, Bruchterm, Wurzel).
**[G]** gesichert · **[A]** Annahme · **[M]** Meinung.

## Die {len(R)} Merksätze

Je Regel zwei Zeilen: oben der Merksatz zum Aufsagen, darunter der genaue Satz mit seiner Bedingung. Der Merksatz darf vereinfachen, behauptet aber nichts Falsches. Verworfene Kandidaten: Anhang von `ebene1.md`.

{merkliste}

## Dieselbe Regel in vielen Klassen

**V** = Vorwissen (kommt vor, wird aber noch nicht als Regel gelehrt) · **E** = Einführung · **A** = spätere Anwendung · leer = kein Beispiel hinterlegt (heißt nicht: kommt nicht vor).

{chr(10).join(matrix)}

Die Einordnung V / E / A habe ich nach den Themen der App eingeschätzt; sie ist **nicht** Etappe für Etappe belegt und **nicht** an LehrplanPLUS geprüft. [A]

## Die vier Schichten der Sonne

Von innen nach außen. Das ist eine Ordnung zum Überblicken, **keine Sperre**: Keine Regel muss „abgeschlossen“ sein, bevor die nächste kommt.

| Schicht | Regeln |
|---|---|
{schichten}

## Die Regeln einzeln

{(chr(10) + chr(10)).join(regel_text(i, r) for i, r in enumerate(R, 1))}

## Was keine eigene Rechenregel ist – und wo es steht

| Was | Wo es steht |
|---|---|
| Runden | Planet Zahlen, eigener Eintrag (eine Vereinbarung) |
| Prozent | Planet Geld und Verhältnisse |
| Betrag | Planet Zahlen |
| Ungleichung umdrehen | Planet Algebra; verwandt mit Regel 3 und Regel 13 |
| Wurzel und Logarithmus | Gegenrechnungen (Regel 12); ihre Gesetze: Planet Zahlen |
| Vertauschungs- und Verbindungsgesetz, 0 und 1 als neutrale Zahlen | Fachnamen zu Regel 5; im Nachschlagen eigens auffindbar |
| Probe | Arbeitsweise, keine Rechenregel |
| Überschlag | Arbeitsweise |

## Für die Technik

Nummern der Übersicht und Nummern in den Aufgaben-Etiketten (`schritt1/etiketten.json`): {nummern}. Etikett 9 „Einsetzen und Probe“ ist die Arbeitsweise „Probe“.

## Nicht geprüft

- **Lehrplan an der Quelle:** Der Abruf von LehrplanPLUS war in dieser Sitzung nicht möglich (keine Freigabe). Die Klasse jedes Beispiels ist gegen `inhalte/themenliste.json` geprüft; die Art (V / E / A) ist meine Einschätzung.
- Ob ein Kind der Klasse 5 die Merksätze versteht und behält – nicht erprobt.
- Die Zeichnungen sind Vorgaben in Worten; gezeichnet und nachgemessen ist nichts.

## Annahmen

- Realschule und IB folgen bei den Rechenregeln denselben Schritten, zum Teil ein Jahr versetzt; die Tabelle zeigt nur das Gymnasium.
- „Einführung“ heißt: In dieser Klasse wird die Regel nach meiner Einschätzung erstmals als Regel gelehrt.
""")
    print(f"{len(R)} Regeln, {n_bsp} Beispiele")
    print("OK")
