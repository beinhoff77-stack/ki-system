"""Mathe-Profi, Auftrag 10: Übersicht der Grundregeln – Inhalt (Schritt 1 von 5).

Aufruf: python3 -I inhalte/mathe-profi/regeln-uebersicht/bauen.py
Hält Regeln, Merksätze, Beispiele je Klasse, Sätze der Gebiete und Arbeitsweisen als Daten,
rechnet jedes Beispiel nach, prüft die Klasse jedes Beispiels gegen inhalte/themenliste.json (Gymnasium) und schreibt inhalt.md.
Nur Inhalte.
"""
import json
import os
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
LISTE = {t["thema_schluessel"]: t for t in json.load(open(os.path.join(WURZEL, "inhalte", "themenliste.json"), encoding="utf-8"))}


def gleich(f, g, aus=()):
    pkt = [F(p) for p in (-5, -3, -2, 2, 3, 5, 7, F(1, 2)) if p not in aus]
    return all(f(p) == g(p) for p in pkt)


# Regel: nr (wie in den Etiketten der Aufgaben), name, etage, merksatz, warum, grenze, baut_auf, bild, verworfen, beispiele[(klasse, thema, text, probe)]
R = [
 dict(nr=13, name="Stellenwert und Prozent", etage=1,
      merk="Mal 10 schiebt jede Ziffer eine Stelle nach links, geteilt durch 10 eine nach rechts. Prozent heißt Hundertstel.",
      warum="Unser Zahlensystem zählt in Zehnerbündeln: Jede Stelle ist zehnmal so viel wert wie die Stelle rechts von ihr. Deshalb verschiebt Malnehmen mit 10 alle Ziffern, ohne sie zu ändern. Das Komma trennt nur Ganze von Zehnteln; „Prozent“ ist ein anderes Wort für Hundertstel.",
      grenze="Es wird nicht „eine Null angehängt“: 2,5 · 10 ist 25, nicht 2,50. Beim Runden entscheidet die Ziffer rechts von der Rundungsstelle (ab 5 aufrunden).",
      baut=[], bild="Stellenwerttafel, in der die Ziffern 2 und 5 beim Malnehmen mit 10 gemeinsam ein Fach nach links rutschen – das Komma bleibt stehen.",
      verworfen="„Null anhängen“ (falsch bei Kommazahlen); wanderndes Komma (zeigt die Wirkung, nicht den Grund).",
      bsp=[(5, "groessen.einheiten", "3 400 m = 3,4 km", lambda: F(3400, 1000) == F(34, 10)),
           (6, "bruch.prozent", "15 % von 240 = 0,15 · 240 = 36", lambda: F(15, 100) * 240 == 36),
           (7, "bruch.prozent_grundwert", "20 % mehr heißt mal 1,2: aus 50 € werden 60 €", lambda: 50 * F(12, 10) == 60),
           (8, "terme.potenzgesetze_ganzzahlig", "3 · 10⁻⁴ = 0,0003", lambda: 3 * F(10) ** -4 == F(3, 10000)),
           (10, "funktionen.exponential_log", "Jedes Jahr 5 % mehr heißt jedes Jahr mal 1,05", lambda: 200 * F(105, 100) == 210)]),
 dict(nr=1, name="Plus und Minus mit negativen Zahlen", etage=1,
      merk="Plus geht nach rechts, Minus nach links. Ein Minus in der Klammer dreht die Richtung um.",
      warum="Auf der Zahlengeraden ist Addieren ein Schritt nach rechts und Subtrahieren ein Schritt nach links. Eine negative Zahl ist ein Schritt in die Gegenrichtung. Wer eine negative Zahl abzieht, dreht also zweimal um und geht nach rechts: 9 − (−5) = 9 + 5.",
      grenze="Die Regel sagt nichts über die Größe: −30 ist kleiner als −10, obwohl 30 größer ist als 10. Der Betrag ist der Abstand zur Null und nie negativ.",
      baut=[], bild="Zahlengerade mit einer Figur: Sie steht auf der 9, schaut nach links (Minus), dreht sich wegen der (−5) um und geht fünf Schritte nach rechts.",
      verworfen="Schulden und Guthaben (trägt beim Abziehen von Schulden schlecht); Thermometer (gut für das Vergleichen, schwach für „minus minus“).",
      bsp=[(5, "zahlen.ganz", "(−7) + 4 = −3 · 9 − (−5) = 14", lambda: -7 + 4 == -3 and 9 - (-5) == 14),
           (6, "bruch.rechnen", "−½ − ¾ = −1¼", lambda: -F(1, 2) - F(3, 4) == -F(5, 4)),
           (7, "terme.umformen", "3x − 5x = −2x", lambda: gleich(lambda x: 3 * x - 5 * x, lambda x: -2 * x)),
           (8, "gleichungen.ungleichungen", "x + 5 < 2, also x < −3", lambda: all((x + 5 < 2) == (x < -3) for x in range(-9, 9))),
           (9, "zahlen.reell", "Die Wurzel aus x² ist der Betrag von x: aus (−3)² wird 3", lambda: abs(-3) == 3 and (-3) ** 2 == 9)]),
 dict(nr=2, name="Vorzeichen bei Mal und Geteilt", etage=1,
      merk="Minus mal Minus gibt Plus. Plus mal Minus gibt Minus.",
      warum="Setzt man die Reihe 3 · (−2) = −6, 2 · (−2) = −4, 1 · (−2) = −2, 0 · (−2) = 0 fort, wächst das Ergebnis jedes Mal um 2. Also muss (−1) · (−2) = 2 sein. Nur so bleiben alle anderen Rechengesetze gültig. Für Geteilt gilt dasselbe, weil Teilen die Gegenrechnung zum Malnehmen ist.",
      grenze="Gilt nur bei Mal und Geteilt, nicht bei Plus: (−3) + (−4) ist −7, nicht +7. Bei Ungleichungen dreht Malnehmen mit einer negativen Zahl das Ungleichheitszeichen um.",
      baut=[1], bild="Die Musterreihe als Treppe: vier Stufen abwärts von −6 bis 0 – und die nächste Stufe landet zwingend bei +2.",
      verworfen="Vierfeldertafel der Zeichen (richtig, aber erklärt nichts); „Feind meines Feindes“ (merkbar, aber kein Grund).",
      bsp=[(5, "zahlen.rechengesetze", "(−3) · (−4) = 12", lambda: (-3) * (-4) == 12),
           (6, "bruch.rechnen", "(−⅔) · ¾ = −½", lambda: -F(2, 3) * F(3, 4) == -F(1, 2)),
           (7, "terme.umformen", "(−2x) · (−3) = 6x", lambda: gleich(lambda x: (-2 * x) * (-3), lambda x: 6 * x)),
           (8, "gleichungen.ungleichungen", "−2x < 6, also x > −3", lambda: all((-2 * x < 6) == (x > -3) for x in range(-9, 9))),
           (9, "gleichungen.quadratisch", "x² = 25 hat zwei Lösungen: 5 und −5", lambda: 5 ** 2 == 25 == (-5) ** 2),
           (10, "funktionen.ganzrational", "(−2)³ = −8: Eine ungerade Hochzahl behält das Minus", lambda: (-2) ** 3 == -8)]),
 dict(nr=3, name="Reihenfolge beim Rechnen", etage=1,
      merk="Klammer zuerst, dann Hoch, dann Punkt, dann Strich.",
      warum="Die Reihenfolge ist eine Vereinbarung, damit jeder dieselbe Rechnung gleich liest. Sie folgt dem Aufbau: Hoch ist wiederholtes Malnehmen, Mal ist wiederholtes Addieren – die „stärkere“ Rechnung bindet enger. Klammern sind das Mittel, die Reihenfolge zu ändern.",
      grenze="Die zuletzt ausgeführte Rechnung gibt dem Term seinen Namen: 2 + 3x ist eine Summe. Deshalb darf man 2 + 3x nicht zu 5x zusammenziehen.",
      baut=[], bild="Vier Treppenstufen von oben nach unten: Klammer, Hoch, Punkt, Strich. Daneben 2 + 3 · 4 mit einem Rahmen um 3 · 4.",
      verworfen="Kunstwort aus Anfangsbuchstaben (merkt sich, erklärt nichts); Ampel (keine Rangfolge erkennbar).",
      bsp=[(5, "zahlen.rechengesetze", "2 + 3 · 4 = 14, nicht 20", lambda: 2 + 3 * 4 == 14),
           (6, "bruch.rechnen", "½ + ½ · ½ = ¾", lambda: F(1, 2) + F(1, 2) * F(1, 2) == F(3, 4)),
           (7, "terme.umformen", "2 + 3x ist eine Summe, nicht 5x", lambda: not gleich(lambda x: 2 + 3 * x, lambda x: 5 * x)),
           (8, "terme.potenzgesetze_ganzzahlig", "3 · 2⁻² = ¾, nicht 6⁻²", lambda: 3 * F(2) ** -2 == F(3, 4) != F(6) ** -2),
           (9, "gleichungen.quadratisch", "−3² = −9, aber (−3)² = 9", lambda: -(3 ** 2) == -9 and (-3) ** 2 == 9),
           (10, "gleichungen.exponential", "2 · 3² = 18, nicht 6² = 36: Hoch kommt vor Mal", lambda: 2 * 3 ** 2 == 18 != 6 ** 2)]),
 dict(nr=6, name="Tauschen und Zusammenfassen", etage=2,
      merk="Bei Plus und Mal darfst du tauschen, bei Minus und Geteilt nicht. Zusammenfassen darfst du nur Gleiches.",
      warum="Bei einer Summe und bei einem Produkt kommt es nicht auf die Reihenfolge an: 3 + 5 und 5 + 3 sind dieselbe Menge. Beim Abziehen und Teilen schon: 5 − 3 ist nicht 3 − 5. Wer jede Zahl mit ihrem Rechenzeichen zusammen verschiebt, darf trotzdem umstellen. Zusammenfassen heißt zählen: 3 Äpfel und 4 Äpfel sind 7 Äpfel – 3 Äpfel und 4 Birnen bleiben getrennt.",
      grenze="3a + 4b lässt sich nicht zusammenfassen, 3a · 4b schon (12ab). a und a² sind nicht „Gleiches“.",
      baut=[1], bild="Zwei Körbe: In einen wandern alle x, in den anderen alle Zahlen. Jedes Teil trägt sein Rechenzeichen wie ein Etikett mit.",
      verworfen="Äpfel und Birnen allein (zeigt das Zusammenfassen, nicht das Tauschen).",
      bsp=[(5, "zahlen.rechengesetze", "25 · 37 · 4 = 25 · 4 · 37 = 3 700", lambda: 25 * 37 * 4 == 3700),
           (6, "bruch.dezimal", "0,5 · 7 · 2 = 0,5 · 2 · 7 = 7", lambda: F(1, 2) * 7 * 2 == 7),
           (7, "terme.umformen", "3a + 2b + 4a = 7a + 2b", lambda: all(3 * a + 2 * b + 4 * a == 7 * a + 2 * b for a in (2, 3) for b in (5, 7))),
           (8, "terme.potenzgesetze_ganzzahlig", "a³ · b · a⁻¹ = a² · b", lambda: all(F(a) ** 3 * b * F(a) ** -1 == a * a * b for a in (2, 3) for b in (5, 7))),
           (9, "zahlen.reell", "3 · √2 + 2 · √2 = 5 · √2 (nur gleiche Wurzeln)", lambda: 3 + 2 == 5)]),
 dict(nr=4, name="Ausmultiplizieren und Ausklammern", etage=2,
      merk="Der Faktor vor der Klammer trifft jeden in der Klammer.",
      warum="Ein Rechteck mit den Seiten a und (b + c) hat dieselbe Fläche wie die zwei Teilrechtecke a · b und a · c zusammen. Rückwärts gelesen ist es das Ausklammern: Steckt in jedem Summanden derselbe Faktor, darf man ihn vor eine Klammer ziehen.",
      grenze="Gilt für Mal vor einer Summe, nicht für Hoch: (a + b)² ist nicht a² + b². Das Rechteckbild zeigt warum – es fehlen zwei Rechtecke a · b.",
      baut=[3], bild="Ein Rechteck, durch einen Strich in zwei Teile geteilt: Breite a, Längen b und c. Darunter dasselbe Bild für (a + b)² mit vier Feldern.",
      verworfen="Pfeile vom Faktor zu jedem Summanden (gut als Rechenhilfe, aber ohne Grund); Verteilen von Bonbons (trägt nicht bis zu Buchstaben).",
      bsp=[(5, "zahlen.rechengesetze", "6 · 98 = 6 · 100 − 6 · 2 = 588", lambda: 6 * 98 == 6 * 100 - 6 * 2 == 588),
           (6, "bruch.dezimal", "4 · 2,5 = 4 · 2 + 4 · 0,5 = 10", lambda: 4 * F(5, 2) == 4 * 2 + 4 * F(1, 2) == 10),
           (7, "terme.umformen", "3 · (x + 2) = 3x + 6 · (a + b)² = a² + 2ab + b²", lambda: gleich(lambda x: 3 * (x + 2), lambda x: 3 * x + 6) and all((a + b) ** 2 == a * a + 2 * a * b + b * b for a in (2, -3) for b in (5, 7))),
           (8, "terme.bruchterme", "(3x + 6) : (x + 2) = 3 · (x + 2) : (x + 2) = 3", lambda: gleich(lambda x: (3 * x + 6) / (x + 2), lambda x: F(3), aus=(-2,))),
           (9, "gleichungen.quadratisch", "x² + 5x = x · (x + 5)", lambda: gleich(lambda x: x * x + 5 * x, lambda x: x * (x + 5))),
           (10, "gleichungen.polynom", "x³ − 4x = x · (x² − 4)", lambda: gleich(lambda x: x ** 3 - 4 * x, lambda x: x * (x * x - 4)))]),
 dict(nr=5, name="Minus vor der Klammer", etage=2,
      merk="Minus vor der Klammer dreht jedes Zeichen in der Klammer um.",
      warum="Ein Minus vor der Klammer heißt „mal (−1)“. Nach der Regel „der Faktor trifft jeden“ wird jeder Summand mit −1 malgenommen, also wechselt jedes Vorzeichen. Im Alltag: Wer 20 € hat und einen Einkauf von 8 € mit 3 € Rabatt bezahlt, hat 20 − 8 + 3 € übrig.",
      grenze="Ein Plus vor der Klammer ändert nichts. Die Regel ist keine neue Regel, sondern folgt aus den beiden Regeln davor – sie steht eigens da, weil hier die meisten Fehler entstehen.",
      baut=[4, 2], bild="Kassenzettel: 20 € − (8 € − 3 € Rabatt). Der Rabatt in der Klammer wird beim Auflösen zu + 3 €.",
      verworfen="Vorzeichen-Wechsel als Schalter (zeigt nur das Was); Spiegel (führt in die Irre).",
      bsp=[(5, "zahlen.rechengesetze", "20 − (8 − 3) = 20 − 8 + 3 = 15 (in Klasse 5 nur zum Nachrechnen)", lambda: 20 - (8 - 3) == 20 - 8 + 3 == 15),
           (7, "terme.umformen", "5x − (3x − 2) = 2x + 2", lambda: gleich(lambda x: 5 * x - (3 * x - 2), lambda x: 2 * x + 2)),
           (8, "gleichungen.bruch", "7 − 2 · (x − 3) = 7 − 2x + 6", lambda: gleich(lambda x: 7 - 2 * (x - 3), lambda x: 7 - 2 * x + 6)),
           (9, "gleichungen.quadratisch", "(x + 1)² − (x² − 3) = 2x + 4", lambda: gleich(lambda x: (x + 1) ** 2 - (x * x - 3), lambda x: 2 * x + 4))]),
 dict(nr=12, name="Potenzen", etage=2,
      merk="Hoch heißt: so oft mit sich selbst malnehmen. Gleiche Basis mal gleiche Basis: Hochzahlen addieren.",
      warum="2³ · 2² ist (2 · 2 · 2) · (2 · 2) – zusammen fünf Zweien, also 2⁵. Teilt man, fallen Faktoren weg; deshalb werden die Hochzahlen abgezogen. Setzt man das fort, ergibt sich 2⁰ = 1 und 2⁻¹ = ½: Eine negative Hochzahl heißt Kehrwert.",
      grenze="Gilt nur bei gleicher Basis und nur bei Mal: 2³ + 2² ist nicht 2⁵. Und a · a ist a², nicht 2a. Eine negative Hochzahl macht die Zahl nicht negativ.",
      baut=[3, 2], bild="Faltblatt: einmal falten 2 Lagen, zweimal 4, dreimal 8. Darunter die Reihe 8, 4, 2, 1, ½, ¼ mit den Hochzahlen 3, 2, 1, 0, −1, −2.",
      verworfen="Turm aus Würfeln (zeigt Wachstum, nicht das Gesetz); Schachbrett mit Reiskörnern (schön, aber nur die Größe).",
      bsp=[(5, "zahlen.potenzen_basis", "2⁵ = 2 · 2 · 2 · 2 · 2 = 32", lambda: 2 ** 5 == 32),
           (6, "terme.potenzgesetze", "10³ · 10² = 10⁵", lambda: 10 ** 3 * 10 ** 2 == 10 ** 5),
           (7, "terme.potenzgesetze_natuerlich", "x² · x³ = x⁵", lambda: gleich(lambda x: x ** 2 * x ** 3, lambda x: x ** 5)),
           (8, "terme.potenzgesetze_ganzzahlig", "a⁻² = 1 : a²", lambda: gleich(lambda a: a ** -2, lambda a: 1 / (a * a))),
           (9, "zahlen.rationale_exponenten", "9 hoch ½ ist die Wurzel aus 9, also 3", lambda: 3 * 3 == 9),
           (10, "funktionen.exponential_log", "2ˣ · 2³ = 2 hoch (x + 3)", lambda: all(2 ** x * 2 ** 3 == 2 ** (x + 3) for x in range(1, 6)))]),
 dict(nr=10, name="Erweitern und Kürzen", etage=3,
      merk="Zähler und Nenner mit derselben Zahl malnehmen oder durch dieselbe Zahl teilen: Der Bruch behält seinen Wert.",
      warum="Der Nenner sagt, in wie viele gleiche Teile das Ganze geschnitten ist, der Zähler, wie viele davon gemeint sind. Schneidet man jedes Teil noch einmal durch, gibt es doppelt so viele Teile und man nimmt doppelt so viele – die Menge bleibt gleich: ½ = 2/4.",
      grenze="Kürzen darf man nur Faktoren, nie aus Summen: (x + 6) : (x + 2) ist nicht 3. Und Plus oder Minus in Zähler und Nenner ändert den Wert: 2/3 ist nicht 3/4.",
      baut=[13], bild="Dieselbe Pizza dreimal: in 2, in 4 und in 8 Stücke geschnitten – jedes Mal ist dieselbe Hälfte gefärbt.",
      verworfen="Bruchstreifen (genauso gut, aber weniger einprägsam); Formel a/b = ac/bc (richtig, aber kein Bild).",
      bsp=[(6, "bruch.brueche", "12/18 = 2/3", lambda: F(12, 18) == F(2, 3)),
           (7, "terme.umformen", "6x : 9 = 2x : 3", lambda: gleich(lambda x: 6 * x / 9, lambda x: 2 * x / 3)),
           (8, "terme.bruchterme", "(3x + 6) : (x + 2) = 3, aber (x + 6) : (x + 2) lässt sich nicht kürzen", lambda: gleich(lambda x: (3 * x + 6) / (x + 2), lambda x: F(3), aus=(-2,)) and not gleich(lambda x: (x + 6) / (x + 2), lambda x: F(3), aus=(-2,))),
           (9, "abbildungen.aehnlichkeit", "Seitenverhältnis 6 : 9 ist dasselbe wie 2 : 3", lambda: F(6, 9) == F(2, 3))]),
 dict(nr=11, name="Rechnen mit Brüchen", etage=3,
      merk="Plus und Minus: erst gleicher Nenner. Mal: Zähler mal Zähler, Nenner mal Nenner. Geteilt: mal den Kehrbruch.",
      warum="Addieren kann man nur gleich große Teile – Drittel und Halbe müssen erst in Sechstel umgerechnet werden. „Mal ½“ heißt „die Hälfte von“; deshalb werden beim Malnehmen die Teile feiner (Nenner mal Nenner). Teilen fragt „wie oft passt es hinein“: In 6 passt ½ zwölfmal – das ist dasselbe wie 6 mal 2.",
      grenze="Nie Zähler plus Zähler und Nenner plus Nenner: ½ + ⅓ ist nicht 2/5. Beim Malnehmen braucht man keinen gemeinsamen Nenner.",
      baut=[10], bild="Zwei gleich lange Streifen: einer halbiert, einer gedrittelt. Darunter beide in Sechstel geteilt – drei Sechstel und zwei Sechstel liegen nebeneinander.",
      verworfen="Zwei Pizzen (unterschiedliche Stückgrößen sind schlecht zu sehen); Rechenregel als Kasten (kein Grund sichtbar).",
      bsp=[(6, "bruch.rechnen", "½ + ⅓ = 3/6 + 2/6 = 5/6 · 6 : ½ = 12", lambda: F(1, 2) + F(1, 3) == F(5, 6) and 6 / F(1, 2) == 12),
           (7, "gleichungen.linear", "x/2 + x/3 = 5x/6", lambda: gleich(lambda x: x / 2 + x / 3, lambda x: 5 * x / 6)),
           (8, "terme.bruchterme", "2/x + 3/(x + 1) = (5x + 2) : (x · (x + 1))", lambda: gleich(lambda x: 2 / x + 3 / (x + 1), lambda x: (5 * x + 2) / (x * (x + 1)), aus=(0, -1))),
           (10, "stochastik.mehrstufig", "Zweimal Kopf: ½ · ½ = ¼", lambda: F(1, 2) * F(1, 2) == F(1, 4))]),
 dict(nr=14, name="Verhältnis (Dreisatz)", etage=3,
      merk="Erst auf eins, dann auf viele.",
      warum="Wenn zwei Größen im selben Verhältnis wachsen, kostet jede Einheit gleich viel. Wer den Wert für eine Einheit kennt, kennt jeden anderen: 3 kg kosten 7,50 €, also 1 kg 2,50 €, also 5 kg 12,50 €. Dieselbe Idee steckt in Prozent (Wert je Hundertstel), in der Steigung einer Geraden (Höhe je Schritt nach rechts) und im Maßstab.",
      grenze="Gilt nur, wenn nichts Festes dazukommt: Mit Grundgebühr stimmt es nicht mehr. Und es gibt das Gegenstück: Bei „je mehr, desto weniger“ (doppelt so viele Helfer, halbe Zeit) bleibt das Produkt gleich, nicht das Verhältnis.",
      baut=[10, 13], bild="Drei Zeilen untereinander: 3 kg – 7,50 €, 1 kg – 2,50 €, 5 kg – 12,50 €, mit Pfeilen „geteilt durch 3“ und „mal 5“ auf beiden Seiten. Daneben ein Steigungsdreieck: 1 nach rechts, 2,5 nach oben.",
      verworfen="Kreuz-Schema „über Kreuz malnehmen“ (schnell, aber blind); Waage (schon vergeben).",
      bsp=[(5, "groessen.proportional", "3 kg kosten 7,50 €, 1 kg kostet 2,50 €, 5 kg kosten 12,50 €", lambda: F(750, 3) == 250 and 250 * 5 == 1250),
           (6, "bruch.prozent", "15 von 60 sind 25 %", lambda: F(15, 60) == F(25, 100)),
           (7, "bruch.prozent_grundwert", "80 % sind 48 €, 1 % sind 0,60 €, 100 % sind 60 €", lambda: F(48, 80) == F(6, 10) and F(6, 10) * 100 == 60),
           (8, "funktionen.linear", "Steigung 1,5: je 2 nach rechts geht es 3 nach oben", lambda: F(3, 2) * 2 == 3),
           (9, "abbildungen.aehnlichkeit", "Strahlensatz: 2 : 3 = 4 : x, also x = 6", lambda: F(2, 3) == F(4, 6))]),
 dict(nr=8, name="Gegenrechnung", etage=4,
      merk="Jede Rechnung hat eine Gegenrechnung: Plus und Minus, Mal und Geteilt, Quadrat und Wurzel.",
      warum="Die Gegenrechnung macht eine Rechnung rückgängig. Wer weiß, was mit einer Zahl gemacht wurde, findet sie, indem er rückwärts geht und jede Rechnung umkehrt – die letzte zuerst. In Klasse 10 kommt ein viertes Paar dazu: Hoch und Logarithmus.",
      grenze="Rückwärts in umgekehrter Reihenfolge: Was zuletzt gerechnet wurde, kommt zuerst weg. Beim Quadrat gibt es zwei Wege zurück: x² = 49 hat die Lösungen 7 und −7. Durch null teilen hat keine Gegenrechnung.",
      baut=[3], bild="Eine Zahl geht durch zwei Maschinen („− 12“, dann „· 4“) und kommt als −20 heraus. Darunter derselbe Weg rückwärts: „: 4“, dann „+ 12“.",
      verworfen="Hin- und Rückweg auf einer Straße (gleichwertig, weniger genau bei der Reihenfolge); Reißverschluss.",
      bsp=[(5, "gleichungen.einfach", "4 · (□ − 12) = −20: erst : 4, dann + 12, also □ = 7", lambda: 4 * (7 - 12) == -20 and F(-20, 4) + 12 == 7),
           (6, "bruch.rechnen", "¾ von einer Zahl sind 12: Die Zahl ist 12 : ¾ = 16", lambda: F(3, 4) * 16 == 12),
           (7, "bruch.prozent_grundwert", "Nach 20 % Aufschlag kostet es 60 €: vorher 60 : 1,2 = 50 €", lambda: 60 / F(12, 10) == 50),
           (8, "gleichungen.formeln", "A = g · h : 2 nach h: erst mal 2, dann durch g", lambda: F(12 * 7, 2) == 42 and F(2 * 42, 12) == 7),
           (9, "gleichungen.quadratisch", "x² = 49, also x = 7 oder x = −7", lambda: 7 ** 2 == 49 == (-7) ** 2),
           (10, "gleichungen.exponential", "2ˣ = 8, also x = 3 (Logarithmus)", lambda: 2 ** 3 == 8)]),
 dict(nr=7, name="Gleichung als Waage", etage=4,
      merk="Eine Gleichung ist eine Waage: Was du links tust, musst du auch rechts tun.",
      warum="Das Gleichheitszeichen sagt: Links und rechts steht gleich viel. Nimmt man auf beiden Seiten dasselbe weg oder verdoppelt beide Seiten, bleibt die Waage im Gleichgewicht – die Gleichung hat danach dieselbe Lösung. Welche Rechnung man wählt, sagt die Gegenrechnung.",
      grenze="„Auf beiden Seiten“ heißt: die ganze Seite. Beim Malnehmen und Teilen trifft es jeden Summanden. Mit null malnehmen oder durch einen Term teilen, der null sein kann, zerstört die Gleichung. Bei Ungleichungen dreht mal oder geteilt durch eine negative Zahl das Zeichen um.",
      baut=[8, 4], bild="Balkenwaage: links zwei Säckchen x und zwei Kugeln, rechts zwölf Kugeln. Auf beiden Seiten werden zwei Kugeln weggenommen, dann beide Seiten halbiert.",
      verworfen="„Rüberbringen und Zeichen wechseln“ (führt zu Fehlern bei Mal und Geteilt); Wippe.",
      bsp=[(5, "gleichungen.einfach", "□ + 7 = 3: auf beiden Seiten 7 abziehen, □ = −4", lambda: -4 + 7 == 3),
           (7, "gleichungen.linear", "2x + 2 = 12, also 2x = 10, also x = 5", lambda: 2 * 5 + 2 == 12),
           (8, "gleichungen.bruch", "3/x + ½ = 5/x: beide Seiten mal 2x, dann 6 + x = 10, x = 4", lambda: F(3, 4) + F(1, 2) == F(5, 4)),
           (9, "gleichungen.quadratisch", "2x² = 18, also x² = 9", lambda: 2 * 3 ** 2 == 18),
           (10, "gleichungen.exponential", "3 · 2ˣ = 24, also 2ˣ = 8", lambda: 3 * 2 ** 3 == 24)]),
 dict(nr=15, name="Nullprodukt", etage=4,
      merk="Ein Produkt ist null, wenn ein Faktor null ist – und nur dann.",
      warum="Null mal irgendetwas ist null. Umgekehrt kann aus zwei Zahlen, die beide nicht null sind, beim Malnehmen nie null werden. Deshalb darf man eine Gleichung „Produkt = 0“ in mehrere einfache Gleichungen zerlegen: Jeder Faktor für sich kann null sein.",
      grenze="Gilt nur für null: Aus (x − 2) · (x + 3) = 6 folgt nicht x − 2 = 6. Erst alles auf eine Seite bringen, dann ausklammern.",
      baut=[4, 7], bild="Eine Kette aus zwei Gliedern, die an der Null hängt: Reißt ein Glied (ist es null), fällt alles auf null.",
      verworfen="Lichtschalter in Reihe (passt, aber fremd für Klasse 5); Dominosteine.",
      bsp=[(5, "zahlen.rechengesetze", "0 · 7 = 0 · und: durch 0 kann man nicht teilen", lambda: 0 * 7 == 0),
           (8, "terme.bruchterme", "Der Nenner x · (x − 4) ist null für x = 0 oder x = 4", lambda: [x for x in range(-5, 9) if x * (x - 4) == 0] == [0, 4]),
           (9, "gleichungen.quadratisch", "(x − 2) · (x + 3) = 0, also x = 2 oder x = −3", lambda: [x for x in range(-9, 9) if (x - 2) * (x + 3) == 0] == [-3, 2]),
           (10, "gleichungen.polynom", "x³ − 4x = x · (x − 2) · (x + 2) = 0, also x = 0, 2 oder −2", lambda: [x for x in range(-9, 9) if x ** 3 - 4 * x == 0] == [-2, 0, 2])]),
]
ETAGE = {1: "Zahlen", 2: "Klammern und Potenzen", 3: "Brüche und Verhältnis", 4: "Gleichungen"}

# Sätze und Formeln der Gebiete: (Gebiet, Klasse laut App, Thema, Satz)
S = [
 ("Rechnen: Formeln, die aus den Regeln folgen", 7, "terme.umformen", "Binomische Formeln: (a + b)² = a² + 2ab + b² · (a − b)² = a² − 2ab + b² · (a + b)(a − b) = a² − b²"),
 ("Rechnen: Formeln, die aus den Regeln folgen", 6, "bruch.prozent", "Prozentwert = Prozentsatz mal Grundwert"),
 ("Rechnen: Formeln, die aus den Regeln folgen", 6, "finanzen.zinsen", "Jahreszinsen = Kapital mal Zinssatz"),
 ("Rechnen: Formeln, die aus den Regeln folgen", 8, "terme.potenzgesetze_ganzzahlig", "Potenzgesetze: gleiche Basis – Hochzahlen addieren; gleiche Hochzahl – Basen malnehmen; Potenz der Potenz – Hochzahlen malnehmen"),
 ("Rechnen: Formeln, die aus den Regeln folgen", 9, "zahlen.reell", "Wurzelgesetze: Wurzel aus a mal Wurzel aus b ist Wurzel aus a · b (nicht bei Plus)"),
 ("Rechnen: Formeln, die aus den Regeln folgen", 9, "gleichungen.quadratisch", "Lösungsformel der quadratischen Gleichung"),
 ("Rechnen: Formeln, die aus den Regeln folgen", 10, "funktionen.exponential_log", "Logarithmusgesetze: Aus Mal wird Plus, aus Hoch wird Mal"),
 ("Geometrie: Winkel und Figuren", 5, "geometrie.winkel", "Scheitelwinkel sind gleich groß, Nebenwinkel ergänzen sich zu 180°"),
 ("Geometrie: Winkel und Figuren", 7, "geometrie.winkelsaetze", "Stufen- und Wechselwinkel an Parallelen sind gleich groß"),
 ("Geometrie: Winkel und Figuren", 7, "geometrie.winkelsaetze", "Winkelsumme: im Dreieck 180°, im Viereck 360°"),
 ("Geometrie: Winkel und Figuren", 7, "geometrie.winkelsaetze", "Im gleichschenkligen Dreieck sind die Basiswinkel gleich groß"),
 ("Geometrie: Winkel und Figuren", 7, "geometrie.kreis", "Satz des Thales: Jeder Winkel im Halbkreis ist ein rechter Winkel"),
 ("Geometrie: Winkel und Figuren", 7, "geometrie.konstruktion", "Kongruenzsätze: Drei passende Angaben legen ein Dreieck fest (SSS, SWS, WSW, SsW)"),
 ("Geometrie: Winkel und Figuren", 9, "abbildungen.aehnlichkeit", "Ähnlichkeit und Strahlensatz: Gleiche Winkel – gleiche Seitenverhältnisse"),
 ("Geometrie: Winkel und Figuren", 9, "trigo.pythagoras", "Satz des Pythagoras: Im rechtwinkligen Dreieck gilt a² + b² = c²"),
 ("Geometrie: Winkel und Figuren", 9, "trigo.rechtwinklig", "Sinus, Kosinus, Tangens: Seitenverhältnisse im rechtwinkligen Dreieck"),
 ("Geometrie: Winkel und Figuren", 9, "trigo.allgemein", "Sinussatz und Kosinussatz für beliebige Dreiecke"),
 ("Geometrie: Messen", 5, "messen.flaechen", "Rechteck: Fläche = Länge mal Breite, Umfang = zweimal (Länge plus Breite)"),
 ("Geometrie: Messen", 6, "messen.flaechen_vielecke", "Parallelogramm: Grundseite mal Höhe · Dreieck: die Hälfte davon · Trapez: Mittel der parallelen Seiten mal Höhe"),
 ("Geometrie: Messen", 8, "messen.kreisberechnung", "Kreis: Umfang = 2 · π · r, Fläche = π · r²"),
 ("Geometrie: Messen", 5, "messen.koerper_berechnung", "Quader: Volumen = Länge mal Breite mal Höhe"),
 ("Geometrie: Messen", 8, "messen.prisma_zylinder", "Prisma und Zylinder: Volumen = Grundfläche mal Höhe"),
 ("Geometrie: Messen", 10, "raum.pyramide_kegel_kugel", "Pyramide und Kegel: ein Drittel von Grundfläche mal Höhe · Kugel: Volumen = 4/3 · π · r³"),
 ("Geometrie: Messen", 9, "abbildungen.aehnlichkeit", "Vergrößern mit Faktor k: Längen mal k, Flächen mal k², Volumen mal k³"),
 ("Funktionen", 8, "funktionen.linear", "Gerade y = m · x + t: m ist die Steigung, t der Abschnitt auf der y-Achse"),
 ("Funktionen", 8, "funktionen.linear", "Nullstelle: dort ist y = 0 · Schnittpunkt: dort sind beide Funktionswerte gleich"),
 ("Funktionen", 8, "funktionen.gebrochen", "Hyperbel y = a : x: doppeltes x, halbes y"),
 ("Funktionen", 9, "funktionen.quadratisch", "Parabel y = a · (x − d)² + e: Scheitel bei (d | e)"),
 ("Funktionen", 10, "funktionen.exponential_log", "Exponentielles Wachstum y = a · bˣ: In gleichen Schritten wird mit derselben Zahl malgenommen"),
 ("Funktionen", 10, "funktionen.trig", "Sinus und Kosinus als Funktionen: Sie wiederholen sich nach 360°"),
 ("Daten und Zufall", 6, "daten.kennwerte", "Mittelwert: alle Werte addieren, durch die Anzahl teilen"),
 ("Daten und Zufall", 7, "daten.boxplot", "Median: der Wert in der Mitte der geordneten Liste"),
 ("Daten und Zufall", 6, "daten.darstellen", "Relative Häufigkeit: Anteil = Anzahl durch Gesamtzahl"),
 ("Daten und Zufall", 5, "stochastik.kombinatorik", "Zählprinzip: Möglichkeiten der Stufen malnehmen"),
 ("Daten und Zufall", 8, "stochastik.grundbegriffe", "Laplace: Wahrscheinlichkeit = günstige durch mögliche Ergebnisse (nur wenn alle gleich wahrscheinlich sind)"),
 ("Daten und Zufall", 8, "stochastik.grundbegriffe", "Gegenereignis: 1 minus die Wahrscheinlichkeit"),
 ("Daten und Zufall", 10, "stochastik.mehrstufig", "Pfadregeln: entlang eines Pfades malnehmen, mehrere Pfade addieren"),
]
# Arbeitsweisen: (Name, Merksatz, wozu)
A = [
 ("Probe", "Setz ein und rechne nach.", "Prüft jede Lösung und jede Umformung. Eine Probe kann einen Fehler zeigen, aber nichts beweisen. (In den Aufgaben-Etiketten bisher als Regel 9 geführt.)"),
 ("Überschlag", "Erst grob, dann genau.", "Mit gerundeten Zahlen die Größenordnung schätzen; fängt Komma- und Stellenfehler ab."),
 ("Skizze", "Zeichne, was du weißt.", "Geometrie und Sachaufgaben: Gegebenes eintragen, Gesuchtes markieren."),
 ("Ansatz", "Gegeben, gesucht, Rechnung, Antwort.", "Sachaufgaben: Text in eine Rechnung oder Gleichung übersetzen, am Ende ein Antwortsatz mit Einheit."),
 ("Begründen", "Nenne den Satz, dann wende ihn an.", "Geometrie und Daten: nicht nur die Zahl, sondern der Grund – und für „stimmt nicht“ genügt ein Gegenbeispiel."),
 ("Ablesen und Darstellen", "Erst Achsen und Einheiten lesen, dann die Werte.", "Diagramme, Tabellen, Graphen: lesen, ergänzen, auf Täuschungen prüfen."),
 ("Formel umstellen", "Formel hinschreiben, einsetzen, auflösen.", "Verbindet die Sätze der Gebiete mit den Rechenregeln (Gegenrechnung, Waage)."),
]

# ── Prüfen ──
NAME = {r["nr"]: r["name"] for r in R}
assert len(R) == 14 and sorted(NAME) == [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]
reihe = [r["nr"] for r in R]
zweifel = []
for r in R:
    assert all(b in reihe[:reihe.index(r["nr"])] for b in r["baut"]), (r["name"], "baut auf etwas, das später kommt")
    assert all(R[reihe.index(b)]["etage"] <= r["etage"] for b in r["baut"])
    klassen = [k for k, *_ in r["bsp"]]
    assert klassen == sorted(set(klassen)) and len(klassen) >= 4, r["name"]
    for k, thema, text, probe in r["bsp"]:
        assert probe() is True, (r["name"], k, text)
        assert thema in LISTE, thema
        gym = LISTE[thema]["klasse"].get("gym_by")
        if gym != k:
            zweifel.append((r["name"], k, thema, gym))
for g, k, thema, satz in S:
    assert thema in LISTE, thema
assert zweifel == [], zweifel          # jedes Beispiel steht in der Gymnasium-Klasse seines Themas laut themenliste.json
start = [min(k for k, *_ in r["bsp"]) for r in R]
ende = [max(k for k, *_ in r["bsp"]) for r in R]
ab5, ab6 = start.count(5), start.count(6)
assert ab5 + ab6 == len(R) and min(ende) >= 9

# ── Schreiben ──
KL = (5, 6, 7, 8, 9, 10)


def regel_text(i, r):
    z = [f"### {i}. {r['name']}", "", f"> **{r['merk']}**", "", f"**Warum das gilt:** {r['warum']}", "", f"**Wo es nicht gilt:** {r['grenze']}", ""]
    z.append("| Klasse | Dieselbe Regel in diesem Jahr | Thema in der App |")
    z.append("|---|---|---|")
    for k, thema, text, _ in r["bsp"]:
        z.append(f"| {k} | {text} | `{thema}` |")
    z.append("")
    z.append(f"**Baut auf:** {', '.join(NAME[b] for b in r['baut']) or 'nichts – Fundament'}")
    z.append(f"**Bild (gewählt):** {r['bild']}")
    z.append(f"**Verworfen:** {r['verworfen']}")
    return "\n".join(z)


matrix = ["| Regel | " + " | ".join(f"Kl. {k}" for k in KL) + " |", "|---|" + "---|" * len(KL)]
for i, r in enumerate(R, 1):
    da = {k for k, *_ in r["bsp"]}
    matrix.append(f"| {i} {r['name']} | " + " | ".join("●" if k in da else "" for k in KL) + " |")
aufbau = []
for e in sorted(ETAGE, reverse=True):
    aufbau.append(f"| **{e} · {ETAGE[e]}** | " + " · ".join(f"{reihe.index(r['nr']) + 1} {r['name']}" for r in R if r["etage"] == e) + " |")
kanten = "\n".join(f"- **{reihe.index(r['nr']) + 1} {r['name']}** braucht: {', '.join(str(reihe.index(b) + 1) + ' ' + NAME[b] for b in r['baut'])}" for r in R if r["baut"])
gebiete = {}
for g, k, thema, satz in S:
    gebiete.setdefault(g, []).append((k, satz, thema))
saetze = []
for g, liste in gebiete.items():
    saetze.append(f"\n**{g}** ({len(liste)})\n\n| Klasse | Satz oder Formel | Thema in der App |\n|---|---|---|")
    for k, satz, thema in sorted(liste, key=lambda x: x[0]):
        saetze.append(f"| {k} | {satz} | `{thema}` |")
merkliste = "\n".join(f"{i}. **{r['name']}:** {r['merk']}" for i, r in enumerate(R, 1))
nummern = " · ".join(f"{i} = Etikett {r['nr']}" for i, r in enumerate(R, 1))
n_bsp = sum(len(r["bsp"]) for r in R)

open(os.path.join(HIER, "inhalt.md"), "w", encoding="utf-8").write(f"""# Übersicht der Grundregeln – Inhalt (Schritt 1 von 5)

Mathe-Profi, 26.11.2026. Erzeugt von `bauen.py`; jedes Beispiel ist nachgerechnet ({n_bsp} Beispiele, Lauf „OK“).
Für ChatGPT zum Angreifen und für den Designer als Stoff. Noch keine Darstellung.
**[G]** gesichert · **[A]** Annahme · **[M]** Meinung.

## Die Antwort in einer Minute

- **Nein, es gibt nicht nur 15 Regeln.** Die 15 waren nur die Regeln fürs Rechnen mit Zahlen und Buchstaben. Ehrlich gezählt sind es drei Schichten:
  - **{len(R)} Rechenregeln** – sie gelten von Klasse 5 bis 10 unverändert, nur das Gewand wechselt (Zahl, Bruch, Buchstabe, Bruchterm, Wurzel).
  - **{len(S)} Sätze und Formeln der Gebiete** – Geometrie, Funktionen, Daten und Zufall, dazu die Formeln, die aus den Rechenregeln folgen. Sie kommen Jahr für Jahr dazu.
  - **{len(A)} Arbeitsweisen** – wie man vorgeht: Probe, Überschlag, Skizze, Ansatz, Begründen, Ablesen, Formel umstellen.
- Zusammen **{len(R) + len(S) + len(A)} Dinge**, nicht 15. Aber: Die {len(R)} Rechenregeln sind der Teil, der sich nie ändert – wer sie sicher hat, muss in jedem neuen Jahr nur das neue Gewand lernen.
- **Aus 15 werden {len(R)}:** „Einsetzen und Probe“ ist keine Rechenregel, sondern eine Arbeitsweise, und steht jetzt dort. [M]

## Die {len(R)} Merksätze

{merkliste}

Namen sind die üblichen Schulwörter. „Zeichen-Paar“, „Wert bleibt“, „Richtung“ und „Verteilen“ aus den früheren Papieren kommen nicht mehr vor.

## Dieselbe Regel in vielen Klassen

Jeder Punkt ist ein nachgerechnetes Beispiel aus einem Thema dieser Klasse (Abschnitt „Die Regeln einzeln“).

{chr(10).join(matrix)}

{ab5} der {len(R)} Regeln beginnen in Klasse 5, die übrigen {ab6} in Klasse 6 mit den Brüchen. Jede reicht mindestens bis Klasse 9. [G, gezählt aus den Beispielen]

## Der Aufbau: Was setzt was voraus

Vier Etagen, von unten nach oben zu lesen. Eine Regel steht nie unter einer Regel, die sie braucht ([G], `bauen.py` prüft es).

| Etage | Regeln |
|---|---|
{chr(10).join(aufbau)}

Die einzelnen Abhängigkeiten:

{kanten}

Vorschlag für die Darstellung [M]: **ein Haus mit vier Etagen** für den Aufbau und daneben **ein Band je Regel von Klasse 5 bis 10**, auf dem in jedem Jahr das Beispiel steht. Das Haus zeigt „aufeinander aufbauend“, die Bänder zeigen „für viele Klassen dasselbe“. Auf dem Dach stehen die Sätze der Gebiete, neben dem Haus der Werkzeugkasten mit den Arbeitsweisen.
Verworfen: Baum (Äste suggerieren Trennung, die Regeln greifen aber ineinander) · Sonnensystem (kein Unten und Oben, also kein Aufbau) · reine Tabelle (zeigt die Jahre, nicht den Aufbau).

## Die Regeln einzeln

{(chr(10) + chr(10)).join(regel_text(i, r) for i, r in enumerate(R, 1))}

## Gibt es wirklich nur diese Regeln? – die ehrliche Liste

**1. Fehlt beim Rechnen etwas?** Keine eigene Regel, aber fünf Dinge, die bisher nicht ausdrücklich dastanden. Sie sind jetzt eingeordnet:

| Was | Wo es jetzt steht | Warum keine eigene Regel |
|---|---|---|
| Runden | Regel 1 Stellenwert (unter „Wo es nicht gilt“) | eine Vereinbarung über die Ziffer rechts daneben |
| Überschlag | Arbeitsweise | ein Vorgehen, kein Gesetz |
| Betrag | Regel 2 Plus und Minus | Abstand zur Null auf der Zahlengeraden |
| Ungleichung umdrehen | Regel 3 Vorzeichen und Regel 13 Waage | Folge aus „mal Minus“ |
| Wurzel und Logarithmus | Regel 12 Gegenrechnung (als Paare), ihre Gesetze unter „Sätze und Formeln“ | Gegenrechnungen zu Quadrat und Hoch; die Gesetze folgen aus den Potenzen |

**2. Die Sätze und Formeln der Gebiete** – das ist die zweite Schicht. Sie sind keine Rechenregeln: Man muss sie wissen, und man wendet sie mit den Rechenregeln an.
{chr(10).join(saetze)}

Die Liste nennt die tragenden Sätze, nicht jede Formel des Lehrplans (zum Beispiel fehlen Kreisbogen, Mantelflächen, Vierfeldertafel). Die Zahl {len(S)} ist deshalb eine Untergrenze. [M]

**3. Die Arbeitsweisen** – die dritte Schicht, für alles, was nicht Rechnen ist:

| Arbeitsweise | Merksatz | Wozu |
|---|---|---|
{chr(10).join(f"| {n} | **{m}** | {w} |" for n, m, w in A)}

**4. Die ganze Landkarte**

| Schicht | Zahl | ändert sich über die Jahre? | Was ein Kind damit tut |
|---|---|---|---|
| Rechenregeln | {len(R)} | nein – nur das Gewand | sicher können, im neuen Stoff wiedererkennen |
| Sätze und Formeln der Gebiete | mindestens {len(S)} | ja – jedes Jahr kommen neue dazu | wissen (Formel-Koffer) und richtig auswählen |
| Arbeitsweisen | {len(A)} | nein | bei jeder Aufgabe anwenden |

Für Geometrie, Daten und Sachaufgaben heißt das: Dort trägt nicht eine Rechenregel, sondern **Satz plus Arbeitsweise** – „Winkelsumme im Dreieck“ und „Nenne den Satz, dann wende ihn an“. Auf der Übersicht gehören sie deshalb sichtbar dazu: die Sätze als Dach nach Gebieten und Klassen, die Arbeitsweisen als Werkzeugkasten daneben. [M]

## Für die Technik

Nummern der Übersicht und Nummern in den Aufgaben-Etiketten (`schritt1/etiketten.json`): {nummern}. Etikett 9 „Einsetzen und Probe“ ist jetzt die Arbeitsweise „Probe“; die Etiketten bleiben gültig.

## Nicht geprüft

- **Lehrplan:** Die Klasse jedes Beispiels ist gegen `inhalte/themenliste.json` geprüft (Gymnasium Bayern, Zuordnung der App), **nicht gegen den Lehrplan an der Quelle**. Die vier Widersprüche zwischen Themenliste und App aus dem Lehrplan-Auftrag betreffen keines der Beispiele.
- „Minus vor der Klammer“ in Klasse 5: Das Thema gehört zur Klasse, erklärt die Regel aber nicht; das Beispiel ist dort nur zum Nachrechnen gedacht.
- Realschule und IB: Die Beispiele folgen den Gymnasium-Klassen. Bei der Realschule liegen einige Themen ein Jahr früher oder später.
- Ob ein Kind der Klasse 5 die Merksätze versteht und behält – nicht erprobt.
- Die Bilder sind beschrieben, nicht gezeichnet.
- Die Liste der Sätze und Formeln ist aus meiner Kenntnis und den Themen der App zusammengestellt, nicht aus dem Lehrplan abgeschrieben.

## Annahmen

- Die Übersicht soll alle Klassen 5 bis 10 zeigen, auch wenn die Kinder erst in 5 und 8 sind.
- „Professionell“ heißt: fachlich richtig, mit Grund und Grenze, in üblichen Schulwörtern.
- {len(R)} statt 15 ist ein Vorschlag; die alte Zählung lässt sich ohne Verlust wiederherstellen.
""")
print(f"{len(R)} Regeln, {n_bsp} Beispiele, {len(S)} Sätze und Formeln, {len(A)} Arbeitsweisen")
print("OK")
