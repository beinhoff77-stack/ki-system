# Sonderfall-Durchsicht aller 63 Auswahl-Aufgaben (Runde VT3, Stand nach Urteil 1222)

Geprüft: (a) versagt die richtige Option in einem Sonderfall (Null, leere Menge, Gleichheit am Rand, zusammenfallende Geraden, negative Werte, mehrere Uhrzeiten mit gleichem Winkel, rechter Winkel)? (b) behauptet ein Fehlbild mehr, als folgt? (c) liefert eine falsche Option zufällig dasselbe Ergebnis wie die richtige (neu aufgenommen, siehe VT3-005)? Wo Zahlen im Spiel sind, rechnet `gegenrechnung.py` die richtige Option neu nach und sucht sie über ihren Text (`kern.py` legt die Reihenfolge fest und mischt Optionen und Fehlbilder gemeinsam). „i. O.“ = kein Sonderfall offen. Neu nach Urteil 1222: (d) Hat eine falsche Option ein richtiges Urteil oder eine richtige Folgerung mit nur falscher Begründung? Alle 63 Auswahl-Aufgaben wurden daraufhin gelesen; gefunden und umgebaut wurden VT3-084 (Option „nicht recht“ mit falscher Begründung), VT3-086 und VT3-100 (Option „recht“ mit falscher Begründung), VT3-121 (Option „falsche Skala“ mit falscher Rechnung). Bei VT3-095 urteilen drei Optionen „nicht recht“, nennen aber unterschiedliche Folgerungen (falscher Term 3n, 4 + 3n, 7 Hölzer); die falschen Optionen enthalten also einen falschen Term.

## messen.volumen
- VT3-005 (quader): 2 m = 20 dm, 30 cm = 3 dm, 50 cm = 5 dm: 20 · 3 · 5 = 300 dm³. Die Rechnung „2 · 30 · 50“ ergibt 3 000 und damit eine andere Zahl; frühere Zahlen (2 m, 30 cm, 5 dm) hätten bei „2 · 30 · 5“ zufällig dieselbe Zahl 300 geliefert, deshalb sind sie ersetzt. i. O.
- VT3-007 (quader): 4 · 4 · 4 = 64 gegen 3 · 4 · 5 = 60 cm³; beide Körper haben Kantensumme 48 cm, Gleichheit und „nicht entscheidbar“ sind widerlegt, die Aussage gilt nur für diese zwei Körper. i. O.
- VT3-009 (liter): 1 m³ = 1 000 Liter; Mia hat nur die Kante umgerechnet. Die Option „1 · 1 · 1 = 1 und 1 m³ ist genau 1 Liter“ ist falsch (1 m³ sind 1 000 l). i. O.
- VT3-011 (liter): 10 · 10 · 20 = 2 000 cm³, 25 · 8 · 10 = 2 000 cm³, 1 · 2 · 1 dm³ = 2 dm³ = 2 000 cm³ und 15 · 15 · 10 = 2 250 cm³ (2,25 l). Alle Optionen nennen nur die Maße und sind gleich gebaut; die richtige Option sticht nicht mehr durch ein anderes Ergebnis hervor. „NICHT“ steht im Text groß. i. O.
- VT3-012 (liter): 1 Liter = 1 dm³ = 1 000 cm³ gilt für jede Form; die Optionen „nur Würfel“ und „jede Kante mindestens 10 cm“ scheitern an Quader 20 · 10 · 5 und 50 · 40 · 0,5 (beide 1 000 cm³). Keine falsche Option stimmt im Urteil. i. O.
- VT3-017 (rueckwaerts): Nur „1 200 : (20 · 5)“ ergibt 12; „1 200 : 20 · 5“ ergibt von links 300, die beiden anderen 1 100 und 48. Keine zweite Rechnung liefert 12. i. O.
- VT3-018 (rueckwaerts): 120 : 24 = 5 cm gegen 120 : 40 = 3 cm; kein Gleichstand, die Höhe folgt aus Volumen und Grundfläche. i. O.
- VT3-019 (rueckwaerts): 36 : 5 ist nicht ganz, also teilt 5 das Volumen nicht; 36 : 4 = 9, 36 : 6 = 6 und 36 : 9 = 4 sind ganz. Alle vier Optionen haben dieselbe Bauart („denn 36 : … ist/ist keine ganze Zahl und … teilt das Volumen“), die Quader 4 · 3 · 3, 6 · 2 · 3 und 9 · 2 · 2 stehen nur in den Fehlbildern. i. O.
- VT3-023 (verstehen): Zuwachs = 2 cm · Länge · Breite für jeden Quader; „um 2 cm³“ gilt nur für Länge · Breite = 1 cm² und ist als Fehlbild benannt. i. O.
- VT3-026 (verstehen): 10 · 4 · 6 = 10 · 6 · 4 = 240 cm³; „nicht sagen“ falsch, weil das Produkt von der Reihenfolge nicht abhängt. i. O.
- VT3-027 (verstehen): Das Becken ist anfangs leer: 30 cm in 2 Stunden, also 90 cm in 6 Stunden. Bei Anfangshöhe 15 cm wären es 10 Stunden (steht in der Erklärung als Gegenbeispiel). 4 Stunden (Differenzdenken), 8 Stunden (angeblich langsamer) und „nicht bestimmbar“ (Grundfläche nicht nötig) scheitern. i. O.
- VT3-028 (verstehen): 2 · l · (b : 2) · h = l · b · h, das Volumen bleibt gleich; „doppelt“ und „halb“ vergessen jeweils eine Kante, „kleiner“ unterstellt, Halbieren wirke stärker. i. O.

## daten.darstellen
- VT3-030 (relative_haeufigkeit): 18 : 24 = 0,75; 0,18 und 0,24 sind abgelesene Zahlen, 4/3 der Kehrwert. i. O.
- VT3-032 (relative_haeufigkeit): 30 % von 8 = 2,4, keine ganze Zahl; höchster Wert „höchstens 25 %“ ist falsch (8 Sechsen wären 100 %). i. O.
- VT3-033 (relative_haeufigkeit): 8 : 25 = 32 %, 9 : 30 = 30 %; kein Gleichstand; die Anteile sind vergleichbar. i. O.
- VT3-034 (relative_haeufigkeit): Jede Sechs erhöht die Trefferzahl um 1, also Vielfaches von 1/120; „genau 1/6“, „größer als 0“ (keine Sechs möglich) und „kleiner als die Eins“ scheitern an Gegenbeispielen. i. O.
- VT3-038 (saeulendiagramm): Höchste Säule 90 Kinder: bei 1 cm für 5 Kinder 18 cm (zu hoch), bei 10 cm 9 cm, bei 20 4,5 cm (passt, aber nicht „möglichst hoch“), bei 100 0,9 cm. Nur 10 erfüllt beides. i. O.
- VT3-039 (saeulendiagramm): 6 : 3 = 2, unabhängig vom Maßstab (Achse ab 0, steht im Text); „nichts sagen“ und „3 Kinder mehr“ scheitern. i. O.
- VT3-040 (saeulendiagramm): Beide Säulen 3 cm hoch, also je 12 Kinder; Breite ohne Bedeutung. Die Option mit 6 und 12 Kindern misst die Fläche und liefert ein falsches Urteil. i. O.
- VT3-041 (saeulendiagramm): 1 cm = 4 Kinder; 0,5 cm = 2, 1,75 cm = 7, 2,5 cm = 10 Kinder sind ganz, 3,2 cm = 12,8 Kinder nicht. Genau eine Option scheitert. i. O.
- VT3-042 (saeulendiagramm): Gestapelte Säule 9 cm, unterer Teil 5 cm, 1 cm für 3 Kinder: obere 4 cm sind 12 Jungen; 27 wäre die ganze Klasse, 15 die Mädchen, 4 die Höhe ohne Maßstab. i. O.
- VT3-045 (irrefuehrend): 20 neue Mitglieder gegen 2, Prozentzahlen mit verschiedener Basis; „fünfmal so erfolgreich“ vergleicht die Prozentzahlen. i. O.
- VT3-048 (irrefuehrend): Achse ab 0 genannt, nur die Höhe zählt; „nichts sagen“ falsch. i. O.
- VT3-049 (irrefuehrend): Beide Linienzüge steigen von 40 auf 60 (um 20); A steigt um 2 cm, B um 0,4 cm bei gleichem waagerechten Abstand, also ist A steiler und der Verkauf gleich gestiegen. Die Optionen „B steiler“, „A stärker gestiegen“ und „gleich steil“ sind im Urteil falsch. i. O.

## daten.kennwerte
- VT3-051 (mittelwert): 16 · 10 = 160 €, geteilt durch alle 20 Kinder = 8 €; „10 €“ lässt die Kinder mit 0 € weg, „6 €“ und „5 €“ sind Fehlbilder ohne Rechnung. i. O.
- VT3-053 (mittelwert): (10 · 8 + 20 · 11) : 30 = 10 (genau 10,0), also näher bei 11 als bei 8 und unter 11; „9,5“, „über 11“ scheitern. i. O.
- VT3-054 (mittelwert): „Eine weitere 6“ behält den Mittelwert; die anderen drei Veränderungen einzeln nachgerechnet (7; 23 : 4 = 5,75; 37 : 6 ≈ 6,17). i. O.
- VT3-056 (mittelwert): 110 : 6 ≈ 18,3; „über fünf der sechs Gewichte“ stimmt, es liegt über 12. i. O.
- VT3-060 (mittel_rueckwaerts): Die größte der vier Zahlen ist mindestens so groß wie der Mittelwert, Gleichheit erlaubt (10, 10, 10, 10); „größer als 10“ scheitert daran, „genau 10 kommt vor“ an 9, 9, 11, 11. i. O.
- VT3-063 (mittel_rueckwaerts): Die größte Zahl ist mindestens 12; nach dem Streichen ist der Rest im Mittel höchstens 12, bei lauter Zwölfen genau 12. „Mindestens 1 unter 12“ ist deshalb falsch (Sonderfall alle gleich), „bleibt 12“ und „steigt“ scheitern an 10, 11, 12, 13, 14 (Mittelwert danach 11,5). i. O.

## funktionen.grundbegriffe
- VT3-064 (mengen): „Höchstens 12“ gilt auch bei fehlenden Monaten; „genau 28“, „genau 12“ und „mindestens 12“ scheitern an Klassen mit vielen gleichen Geburtsmonaten. i. O.
- VT3-065 (mengen): Jeder der 5 Werte von D liefert genau einen Funktionswert, also höchstens 5 verschiedene Werte; f(x) = x gibt 5, f(x) = 7 gibt 1. „Genau 5“, „mindestens 6“ und „höchstens 3“ scheitern an diesen Beispielen. i. O.
- VT3-066 (mengen): f(−1) = 1, f(2) = 4 gibt W = {1; 4}. D = {1; 4} gibt {1; 16}, D = {1; 2; 3} gibt {1; 4; 9}, D = {2; 3} gibt {4; 9}. Genau eine Menge erfüllt es. i. O.
- VT3-068 (mengen): Mia und Ben sind Geschwister, Zoe hat keines in der Gruppe: „eines seiner Geschwister aus der Gruppe“ gibt Zoe keinen Wert (keine Funktion); Geburtstag, Sitzplatz und Buchstabenzahl sind eindeutig. i. O.
- VT3-074 (stelle): fallend und a < b gibt f(a) > f(b); Beispiel f(x) = 10 − 2x mit a = 1, b = 3: 8 > 4. Die Optionen „f(a) < f(b)“, „f(a) = f(b)“ und „nicht sagbar“ sind im Urteil falsch. i. O.
- VT3-076 (stelle): −2x² ist nie positiv, also keine Lösung; ±2 ergibt −8. i. O.
- VT3-078 (graph_lesen): Zwei Punkte mit verschiedenen x-Koordinaten (Ursprung, y-Achsenabschnitt) und Punkt mit Steigung legen die Gerade fest; P(2 | 5) und Q(2 | 9) liegen senkrecht übereinander, das ist keine Funktion, der Term wäre nicht festgelegt. i. O.
- VT3-081 (graph_lesen): Achsenabschnitte 1 und −3 verschieden, also parallel und verschieden. i. O.
- VT3-082 (graph_lesen): Zuwächse 2, 6, 18, keine Gerade; „y = 2x + 1“ passt nur für zwei Punkte (bei x = 2 ergäbe sich 5). i. O.
- VT3-083 (graph_lesen): f(0) = −4, 2x − 4 = 0 ergibt x = 2; die drei anderen Paare sind falsch zugeordnet oder mit falschem Vorzeichen. i. O.
- VT3-084 (graph_lesen): Steigung −3, der Graph fällt. Alle drei falschen Optionen urteilen „Jonas hat recht“ (früher gab es eine falsche Option mit richtigem Urteil, sie ist ersetzt). i. O.
- VT3-086 (punkt_graph): Der Graph einer linearen Funktion ist eine Gerade, die Strecke [AB] liegt auf ihr, M(3 | 7) liegt auf f(x) = 2x + 1 (f(3) = 7). Die drei falschen Optionen sind im Urteil falsch („nein“, „nicht sagbar“, „nur mit Ursprung“). i. O.
- VT3-088 (punkt_graph): a ganz ⇒ b = 2a + 1 ganz; Umkehrung scheitert an a = 0,5; „a negativ ⇒ b negativ“ scheitert an a = −0,25. i. O.
- VT3-090 (punkt_graph): a · 0 = 0 für jedes a, auch a = 0 und negative a. i. O.
- VT3-091 (punkt_graph): Erste Koordinate Tage, zweite Preis: K(7) = 12 + 35 = 47. Die Optionen mit vertauschten Koordinaten und mit „Grundgebühr 47“ sind falsch. i. O.
- VT3-093 (sachzusammenhang): K(8) = 19, K(4) = 11, 19 < 22; Differenz 8 €, nicht 4 €. i. O.
- VT3-095 (sachzusammenhang): 2 Quadrate = 7 Hölzer, n Quadrate = 3n + 1; „4 + 3n“ ergäbe für n = 1 sieben statt vier. i. O.
- VT3-096 (sachzusammenhang): Je Minute 90 : 60 = 1,5 km. i. O.
- VT3-097 (sachzusammenhang): Nur der Apfelpreis ist proportional; Quadratfläche, Wurfhöhe und Körpergröße sind nicht linear. i. O.
- VT3-098 (sachzusammenhang): 120 : 15 = 8 h; die Optionen unterscheiden Term und Bereich einzeln, genau eine Option trifft beides. i. O.

## geometrie.winkel
- VT3-100 (kreuzung): Begründung über Nebenwinkel und Scheitelwinkel; die Option „nur zwei der vier Winkel sind 90°“ scheitert an den Nachbarwinkeln, „nicht folgern“ und „Nachbarwinkel immer verschieden“ am 90°-Fall. Keine falsche Option stimmt im Urteil. i. O.
- VT3-103 (kreuzung): Scheitelwinkel gleich groß; Sonderfall 90° widerlegt „mindestens einer spitz“ und „Nachbarwinkel verschieden“. i. O.
- VT3-105 (kreuzung): Nur 72, 108, 72, 108 erfüllt Scheitel- und Nebenwinkelregel (Summe 360°). i. O.
- VT3-109 (uhr): 9:00 und 3:00 je 90° (kleinerer Winkel); 9:15 Uhr 172,5°. i. O.
- VT3-110 (uhr): Vielfaches von 30° und höchstens 180°; Gegenbeispiele für die anderen drei (3:00 Uhr 90°, 6:00 Uhr 180° ohne zweite Stunde, 12:00 Uhr 0°). i. O.
- VT3-111 (uhr): 1:05 Uhr 2,5°; 12:15 Uhr 82,5°, 3:00 Uhr 90°, 6:00 Uhr 180°. i. O.
- VT3-114 (figuren): Zeile 2 ist die erste falsche (1 + 3 = 4 Stücke, 90° : 4 = 22,5°); Zeile 3 und 4 sind Folgen. i. O.
- VT3-116 (figuren): 90° : 3 = 30° gegen 180° : 4 = 45°. i. O.
- VT3-117 (figuren): α + 90° + β = 180°, also α + β = 90° für jede Lage des Quadrats; α = β gilt nur für 45°, „α größer als β“ nicht immer (30° und 60° vertauschbar). i. O.
- VT3-118 (figuren): Bei 30 + 30 + 30 gilt „höchstens 30°“ mit Gleichheit; „mindestens 20°“ scheitert an 10, „größer als 30°“ an 30, 30, 30, „paarweise verschieden“ an gleichen Teilen. i. O.
- VT3-121 (verstehen): 116° ist stumpf; 64° ist spitz, also falsche Skala. Die falsche Option „26°“ urteilt falsch (ein stumpfer Winkel kann nicht 26° sein). i. O.
- VT3-122 (verstehen): Spitz verdoppelt ist immer kleiner als 180°; 2 · 30° = 60° (spitz), 2 · 45° = 90°, 2 · 70° = 140° (stumpf) widerlegen „stumpf“, „spitz“ und „genau 180°“. i. O.
- VT3-125 (verstehen): 60° ist größer als 40°; die Schenkellänge ist beliebig verlängerbar. i. O.
