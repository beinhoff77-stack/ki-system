"""Denkfigur (idee) je Aufgabe: Kategorie | Kurzbeschreibung. Wird von bauen.py als Feld idee in die JSON-Dateien geschrieben."""
I = """
001 was_waere_wenn|Kantenfaktoren 2, 3, 1/2 zusammen
002 immer_nie|Würfel, alle Kanten halbiert
003 umkehr|Volumen nach Veränderung zurückrechnen
004 fehler|Fehler-Detektiv: Summe statt Produkt
005 was_waere_wenn|welche Kantenänderung verdoppelt das Volumen
006 umkehr|Kantenverhältnisse und Volumen, Breite und Höhe gesucht
007 groessenvergleich|Würfel gegen Quader bei gleicher Kantensumme
008 bruecke|Volumen in cm³ in Liter und Zeit verbinden
009 begruenden|Würfel mit 1 m Kante fasst 100 l?
010 fehler|Fehler-Detektiv: cm³ in l falsch umgerechnet
011 umkehr|Fassungsvermögen in Liter, Kante gesucht
012 zwei_wege|Umrechnung vor oder nach dem Multiplizieren
013 darstellung|welche Angabe ist nicht dasselbe Volumen
014 transfer|Dusche, Wanne, Zeit
015 umkehr|Breite aus Volumen und Verhältnis von Höhe zu Breite
016 fehler|Fehler-Detektiv: Höhe aus Volumen
017 rechnung_waehlen|welche Rechnung liefert die Höhe
018 groessenvergleich|gleiches Volumen, Grundflächen vergleichen ohne Rechnen
019 umkehr|Zufluss aus Wasserstandsänderung
020 was_waere_wenn|Höhenzuwachs und Volumenzuwachs
021 transfer|Becken leeren, Zeit gesucht
022 was_waere_wenn|Raumhöhe und Luftmenge
023 immer_nie|Höhe um 2 cm größer, Volumenzuwachs
024 fehler|Fehler-Detektiv: Luft im Zimmer
025 transfer|Quader aus Würfeln
026 groessenvergleich|zwei Quader ohne Ausrechnen vergleichen
027 transfer|Päckchen im Karton
028 was_waere_wenn|Länge und Breite um 50 % vergrößert
029 groessenvergleich|Anteile zweier Klassen, Prozentpunkte
030 darstellung|Anteil als Bruch, Dezimalzahl, Prozent
031 fehler|Fehler-Detektiv: relative Häufigkeit beim Würfeln
032 umkehr|Anteil bekannt, Gesamtzahl gesucht
033 groessenvergleich|8 von 25 gegen 9 von 30
034 darstellung|gemischte Schreibweisen zusammenführen
035 was_waere_wenn|neue Kinder verändern den Anteil
036 darstellung|zwei Maßstäbe, Höhenunterschied
037 fehler|Fehler-Detektiv: Säulenhöhe in Stimmen
038 umkehr|Höhenunterschied und Kinderunterschied, Maßstab gesucht
039 begruenden|Säulenverhältnis und Werteverhältnis
040 darstellung|Werte in Säulenhöhen übersetzen
041 zwei_wege|Dreisatz oder Maßstab
042 transfer|Gesamtzahl und Anteil aus Säulen
043 darstellung|abgeschnittene Hochachse, wahre Änderung
044 darstellung|ungleiche Skala
045 begruenden|Prozente mit verschiedener Basis
046 fehler|Fehler-Detektiv: Diagramm mit Achsenbeginn
047 was_waere_wenn|Achsenbeginn verschieben
048 begruenden|Säulenbreite und Aussage
049 zwei_wege|dieselben Daten, zwei Diagramme
050 was_waere_wenn|ein weiterer Wert ändert den Mittelwert
051 immer_nie|ein Wert wächst, Wirkung auf den Mittelwert
052 fehler|Fehler-Detektiv: Notenmittel
053 was_waere_wenn|alle Werte malgenommen
054 begruenden|welche Änderung lässt den Mittelwert gleich
055 transfer|gewichteter Mittelwert zweier Klassen
056 groessenvergleich|Ausreißer und Mittelwert ohne genaues Rechnen
057 umkehr|fehlender Wert für Zielmittelwert
058 was_waere_wenn|eine Zahl ersetzt, Mittelwert ändert sich
059 fehler|Fehler-Detektiv: vierte Zahl
060 begruenden|dritte Zahl aus Mittelwert
061 umkehr|fehlender Wert aus Mittelwert
062 zwei_wege|Summe oder Abweichungen vom Mittelwert
063 transfer|Rundenzeiten, Mittelwert und Spannweite
064 begruenden|Geburtsmonat als Funktion
065 immer_nie|Aussagen über f(x) = 5 − x² auf ℚ
066 umkehr|Definitionsmenge aus Wertemenge
067 fehler|Fehler-Detektiv: Wertemenge und Elementezahl
068 transfer|Quersumme als Funktion
069 transfer|Definitionslücken eines Terms
070 mengen_deuten|Schnitt von D und W
071 umkehr|zwei Stellen für einen Funktionswert
072 groessenvergleich|Unterschied zweier Stellen über die Steigung
073 fehler|Fehler-Detektiv: Stelle zu f(x) = 15
074 rechnung_waehlen|Ansatz für Pflanzenwachstum
075 umkehr|Stellen zu gegebenen Werten bei f(x) = 20 : (x − 1)
076 begruenden|Gleichung ohne Lösung
077 transfer|Parkplatz mit Höchstpreis
078 darstellung|Gerade durch zwei Punkte, Term gesucht
079 darstellung|Wertetabelle in Term übersetzen
080 fehler|Fehler-Detektiv: Achsenabschnitt
081 begruenden|parallele Geraden
082 gegenbeispiel|Wertetabelle: ist der Graph eine Gerade
083 transfer|Steigung beschrieben, Wert gesucht
084 begruenden|Vorzeichen der Steigung
085 was_waere_wenn|Parameter b bestimmen, Wert an anderer Stelle
086 begruenden|Punktprobe mit Begründung
087 fehler|Fehler-Detektiv: Punktprobe
088 pruefen|drei Punkte auf dem Graphen
089 transfer|Gerade durch drei Punkte
090 immer_nie|Ursprung auf dem Graphen
091 transfer|Leihpreis und Tage
092 darstellung|Fass: Term und sinnvoller Bereich
093 darstellung|Tabelle in Term
094 fehler|Fehler-Detektiv: Handytarif
095 transfer|Streichholzmuster
096 transfer|Zug, Entfernung und Zeit
097 umkehr|vom Term zur Beschreibung der Situation
098 groessenvergleich|zwei Tarife vergleichen
099 immer_nie|ein Winkel ist 90°
100 umkehr|Nachbarwinkel im Verhältnis 1 : 2
101 fehler|Fehler-Detektiv: Scheitelwinkel
102 umkehr|vier Winkel aus Teilsumme
103 immer_nie|welche Aussage über Kreuzungswinkel gilt immer
104 transfer|drei Geraden durch einen Punkt
105 darstellung|Winkelfolgen um den Schnittpunkt
106 umkehr|andere Uhrzeit mit gleichem Winkel
107 zusammenhang|Drehung von Minuten- und Stundenzeiger
108 fehler|Fehler-Detektiv: Winkel um 4:30 Uhr
109 begruenden|gleicher Winkel um 9:00, 3:00 und 9:15 Uhr
110 transfer|wie oft stehen die Zeiger senkrecht
111 groessenvergleich|kleinster Zeigerwinkel
112 transfer|Uhr geht vor
113 fehler|Fehler-Detektiv: Teilwinkel im Rechteck
114 fehler|Fehler-Detektiv: Teile im Verhältnis 1 : 3
115 transfer|Torte, Schnitte und Winkel
116 begruenden|Diagonale im Rechteck
117 umkehr|Teilwinkel, die jeweils größer werden
118 immer_nie|Zerlegung eines rechten Winkels
119 umkehr|Teile eines rechten Winkels
120 immer_nie|spitzer und stumpfer Winkel nebeneinander
121 begruenden|Geodreieck und Augenmaß
122 was_waere_wenn|Winkel verdoppelt, Nebenwinkel schrumpft
123 fehler|Fehler-Detektiv: drei gleiche Winkel um einen Punkt
124 immer_nie|Nebenwinkel eines spitzen Winkels
125 begruenden|Schenkellänge und Winkelgröße
126 umkehr|zwei Winkel, Summe und Unterschied
"""
IDEE = {"VT3-" + z[:3]: z[4:] for z in I.strip().split("\n")}
assert len(IDEE) == 126
