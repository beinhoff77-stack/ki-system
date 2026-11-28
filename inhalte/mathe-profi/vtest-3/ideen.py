"""Denkfigur (idee) je Aufgabe: Kategorie|Kurzbeschreibung. Wird von bauen.py als Feld idee in die JSON-Dateien geschrieben.
Die Kategorie beschreibt, was beim Lösen wirklich gedacht werden muss (nicht das Aufgabenformat)."""
I = """
001 was_waere_wenn|Kantenänderungen in Prozent, Faktoren statt Prozentzahlen
002 zusammenhang|drei Kanten im Verhältnis 1 : 2 : 3, kürzeste Kante aus dem Volumen
003 transfer|Papierstapel: Höhe und Blattzahl proportional
004 fehler|Fehler-Detektiv: Summe statt Produkt
005 rechnung_waehlen|gemischte Einheiten, Rechnung in dm³ auswählen
006 transfer|kleinster Würfel aus gleichen Quadern
007 groessenvergleich|Würfel und Quader, gleiche Kantensumme oder Volumen
008 bruecke|Würfelbehälter, Liter und Anzahl über Kantenverhältnis
009 begruenden|Würfel mit 1 m Kante, Liter
010 fehler|Fehler-Detektiv: cm³ in l falsch umgerechnet
011 pruefen|welcher Quader fasst nicht genau 2 Liter
012 immer_nie|Gefäß mit 1 Liter, Form nicht festgelegt
013 zusammenhang|Würfelreihe von 10 m, wie viele Liter
014 transfer|Wanne, Zufluss und Zeit
015 umkehr|Höhe aus Volumen und Verhältnis zur Länge
016 fehler|Fehler-Detektiv: Höhe aus Volumen
017 rechnung_waehlen|welche Rechnung liefert die Höhe
018 groessenvergleich|gleiches Volumen, Grundflächen vergleichen ohne Rechnen
019 gegenbeispiel|welche Kantenlänge ist bei 36 cm³ unmöglich
020 was_waere_wenn|größere Höhe bei gleicher Grundfläche
021 zusammenhang|Volumen geviertelt, Seite der quadratischen Grundfläche
022 transfer|Päckchen im Karton, Randverlust beim Stapeln
023 begruenden|Höhe plus 2 cm, Volumenzuwachs unabhängig von der Höhe
024 fehler|Fehler-Detektiv: Luft im Zimmer
025 umkehr|Gleiche Höhe, Volumenunterschied zweier Quader, Höhe gesucht
026 groessenvergleich|zwei Quader ohne Ausrechnen vergleichen
027 zusammenhang|Wasserhöhe im Becken wächst mit der Zeit gleichmäßig
028 was_waere_wenn|Länge verdoppelt, Breite halbiert
029 umkehr|nötige weitere Treffer für Zielhäufigkeit
030 darstellung|Anteil als Bruch, Dezimalzahl, Prozent
031 fehler|Fehler-Detektiv: relative Häufigkeit beim Würfeln
032 pruefen|ist 30 % bei 8 Würfen überhaupt möglich
033 groessenvergleich|8 von 25 gegen 9 von 30
034 immer_nie|Aussage über jede Versuchsreihe (Vielfaches von 1/120)
035 zusammenhang|zwei Versuchsreihen zusammen, Prozentsätze nicht mitteln
036 was_waere_wenn|anderer Maßstab: alte Höhe aus den Höhenunterschieden
037 fehler|Fehler-Detektiv: Säulenhöhe in Kindern
038 rechnung_waehlen|Maßstab für höchstens 12 cm Höhe wählen
039 begruenden|Säulenverhältnis und Werteverhältnis
040 gegenbeispiel|Säulenbreite sagt nichts über die Anzahl, nur die Höhe
041 pruefen|welche Säulenhöhe passt nicht zu ganzen Kinderzahlen
042 mengen_deuten|Teilstück einer gestapelten Säule in Kinder umrechnen
043 darstellung|abgeschnittene Achse, Höhen in Besucher übersetzen, wahre Änderung
044 pruefen|Nummer der Marke gegen Wert der Marke
045 begruenden|Prozente mit verschiedener Basis
046 fehler|Fehler-Detektiv: Prozentpunkte und Prozent
047 groessenvergleich|Ausschnitt des Jahres täuscht: Anstieg im Ausschnitt gegen ganzes Jahr
048 darstellung|Säulenbreite und Aussage
049 zwei_wege|dieselben Daten, zwei Maßstäbe, Anstieg und Verkaufsänderung
050 umkehr|Werte verdreifacht und verkleinert, alter Mittelwert gesucht
051 mengen_deuten|Kinder ohne Erspartes zählen beim Mittelwert mit
052 fehler|Fehler-Detektiv: Notenmittel
053 zusammenhang|Gesamtmittelwert liegt näher bei der größeren Gruppe
054 begruenden|welche Änderung lässt den Mittelwert gleich
055 zusammenhang|gleichmäßiger Zuwachs, Mittelwert ist die Mitte von Anfang und Ende
056 groessenvergleich|Ausreißer und Mittelwert ohne genaues Rechnen
057 umkehr|Zahl der Mädchen aus den Mittelwerten von Gruppe und Klasse
058 zusammenhang|Abstände über und unter dem Mittelwert gleichen sich aus
059 fehler|Fehler-Detektiv: Zielmittelwert beim fünften Lauf
060 begruenden|Aussage über vier Zahlen mit Mittelwert 10
061 darstellung|Mittelwert über Abweichungen von 100
062 was_waere_wenn|Summe ändert sich um Plus und Minus, wie ändert sich der Mittelwert
063 gegenbeispiel|größte Zahl streichen, Sonderfall alle Zahlen gleich
064 begruenden|Geburtsmonat als Funktion, Wertemenge
065 immer_nie|höchstens so viele Funktionswerte wie Elemente der Definitionsmenge
066 umkehr|Definitionsmenge zu x² und gegebener Wertemenge, mehrere Stellen möglich
067 fehler|Fehler-Detektiv: Wertemenge von x² − 4
068 gegenbeispiel|welche Zuordnung ist keine Funktion
069 mengen_deuten|Definitionslücken eines Terms
070 mengen_deuten|Schnitt von D und W
071 umkehr|zweite Stelle zu einem Funktionswert
072 zusammenhang|Unterschied zweier Stellen über die Steigung
073 fehler|Fehler-Detektiv: doppelter Funktionswert heißt nicht doppelte Stelle
074 immer_nie|fallende Funktion, a < b
075 umkehr|Stellen zu gegebenen Werten bei 20 : (x − 1)
076 begruenden|Gleichung ohne Lösung
077 transfer|Funktionswert in der Mitte zweier Stellen
078 zusammenhang|welche Angabe legt eine Gerade nicht fest
079 darstellung|Wertetabelle in Term übersetzen
080 fehler|Fehler-Detektiv: Achsenabschnitt
081 begruenden|parallele Geraden
082 gegenbeispiel|Wertetabelle: ist der Graph eine Gerade
083 pruefen|Schnittpunkte mit den Achsen
084 begruenden|Vorzeichen der Steigung
085 umkehr|Parameter b aus einem Punkt, Wert an anderer Stelle
086 zusammenhang|Mittelpunkt zweier Graphpunkte liegt auf dem Graphen
087 fehler|Fehler-Detektiv: Punktprobe
088 pruefen|Punkt P(a | b) auf dem Graphen, was gilt immer
089 bruecke|gemeinsamer Punkt zweier Graphen
090 immer_nie|Ursprung auf dem Graphen
091 darstellung|Punkt auf dem Graphen im Sachzusammenhang deuten
092 transfer|Jahreskarte: ab wann günstiger
093 was_waere_wenn|doppelte Strecke, doppelter Preis?
094 fehler|Fehler-Detektiv: Handytarif
095 pruefen|Streichholzmuster, Behauptung prüfen
096 transfer|Zeiteinheit im Term wechseln
097 gegenbeispiel|welcher Zusammenhang ist linear
098 darstellung|Fass: Term und sinnvoller Bereich
099 zusammenhang|sechs Winkel an drei Geraden, wie viele sind spitz
100 begruenden|ein Winkel ist 90°, alle vier Winkel
101 fehler|Fehler-Detektiv: Scheitelwinkel, falsche Gegenüberstellung
102 umkehr|vier Winkel aus Summe dreier Winkel
103 immer_nie|welche Aussage über Kreuzungswinkel gilt immer
104 transfer|zwei senkrechte und eine dritte Gerade
105 darstellung|Winkelfolgen um den Schnittpunkt
106 transfer|Digitalanzeige 15:30 auf das 12-Stunden-Zifferblatt übertragen, Winkel zwischen den Zeigern
107 zusammenhang|Drehung von Minuten- und Stundenzeiger
108 fehler|Fehler-Detektiv: kleinerer Winkel um 8:00 Uhr, überstumpfen Winkel genommen
109 pruefen|gleicher Winkel um 9:00, 3:00 und 9:15 Uhr
110 immer_nie|Winkel zu den vollen Stunden
111 groessenvergleich|kleinster Zeigerwinkel
112 umkehr|andere Uhrzeit mit gleichem Winkel
113 fehler|Fehler-Detektiv: vier Teilwinkel als gleich große Stücke gezählt, ein Teil vergessen
114 fehler|Fehler-Detektiv: Teile im Verhältnis 1 : 3
115 umkehr|Torte, Schnitte durch den Mittelpunkt
116 groessenvergleich|Bruchteile verschiedener Winkel
117 begruenden|Quadrat auf einer Geraden, Winkel neben der Ecke
118 immer_nie|Zerlegung eines rechten Winkels
119 transfer|zwei gegeneinander gedrehte Quadrate, gemeinsamer und überdeckter Winkel
120 was_waere_wenn|Winkel verdreifacht, Nebenwinkel schrumpft
121 begruenden|Geodreieck und Augenmaß
122 immer_nie|spitzer Winkel verdoppelt, was gilt immer
123 fehler|Fehler-Detektiv: gestreckter Winkel gehört nicht zu den stumpfen Winkeln
124 transfer|volle Umdrehungen und Rest
125 begruenden|Schenkellänge und Winkelgröße
126 umkehr|zwei Winkel, Summe und Unterschied
"""
IDEE = {"VT3-" + z[:3]: z[4:] for z in I.strip().split("\n")}
assert len(IDEE) == 126
