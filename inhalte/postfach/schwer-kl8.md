# Postfach schwer-kl8 (Zehnte Runde, Klasse 8)

Neueste Meldung oben.

## 2026-11-16 11:20 – FERTIG
Zehnte Runde Klasse 8 abgeschlossen: alle 15 Themen mit gym_by 8 bearbeitet (alle haben einen Generator; groessen.indirekt heißt groessen_indirekt.py). 15 Commits auf schwer-kl8, 582 neue Übungen.

Technik
- Neue Übungen stehen je Generator im Abschnitt SCHWER (eigener Zufallsstart, eigene Positionsverteilung); sie werden erst nach dem vollständigen Bau angehängt, direkt hinter der letzten Aufgabe ihrer Lernkarte. Helfer: inhalte/generatoren/_schwer_kl8.py.
- Unverändert-Nachweis: `python3 -I inhalte/generatoren/_unveraendert_kl8.py <thema>` vergleicht mit origin/lernen-app: alle alten Aufgaben Zeichen für Zeichen gleich und in gleicher Reihenfolge, alles außer „aufgaben“ gleich (Lernkarten, Zeichnungen, offen), neu nur Pool uebung. Ergebnis für alle 15 Themen: JA. Prüfskript: alle 15 OK.
- Teilfähigkeit „t“ der neuen Aufgaben = die der Lernkarte laut inhalt.teilfaehigkeiten (wichtig bei groessen.indirekt).
- Lösungen: Zahl-Aufgaben und Lücken werden beim Bauen gegen „c“ nachgerechnet; gerundete Ergebnisse mit round(…) in „c“ und Toleranz; Auswahl-Aufgaben mit kritischen Werten zusätzlich per assert geprüft (Würfelnetze mit falten(), Lagebeziehungen mit lage_von(), Zählungen von Zufallsziffern). Jede neue Aufgabe von Hand nachgerechnet und gelesen.
- Keine Änderung an Lernkarten, Zeichnungen, App, Datenbank, Tests. Kein Merge.

(1) Befundliste aus Teil 1 (vorhandene Aufgaben nicht geändert; je Lernkarte alle Übungen gelesen, mindestens 14)
Wichtigste Funde: **Fehler** in gleichungen.ungleichungen/grafisch (zwei S1: „oberhalb/unterhalb“ mit ≥/≤ beantwortet), **Toleranz fehlt** in messen.kreisberechnung/sektor (S1 „30° in Prozent, runden“), **Text und Antwort passen nicht** in gleichungen.formeln/ein_schritt (10 · 0,04 „≈ 0,43“). Sonst vor allem zu hoch eingestufte Stufe-3-Aufgaben (gleicher Typ wie Stufe 1/2) und Wiederholungen.

### funktionen.grundbegriffe
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| eindeutig | S3 „Welche Zuordnung ist KEINE Funktion?“ (Paarlisten, 2×) | gleicher Gedanke wie S1/S2 – eher Stufe 2 |
| funktionswert | S3 „Berechne f(6) für f(x) = 2/(x − 5)“ | einschrittig – eher Stufe 1–2 |
| stelle | S1/S2 „… wenn f(x) = −1(x + 1)“ bzw. „−1(x + 4)“ | Schreibweise unüblich, besser „f(x) = −(x + 1)“ (Lösungen richtig) |
| punkt_graph | S2 „Lies am Graphen ab: f(4) = ?“ | passt zur Karte graph_lesen, nicht zu „Liegt der Punkt auf dem Graphen?“ |
| (offen) | Eintrag „Kreis kann die App nicht zeichnen“ | veraltet: Koordinatensystem kann `kreise` (seit 15.11.); neue Aufgabe nutzt das |
| Lücke | – | fehlten: D/W im Sachzusammenhang, Tabellenkalkulations-Formel, Punkt ober-/unterhalb, Achsenschnittpunkte → ergänzt |
Alle gelesenen Lösungen (je Karte alle 14 Übungen) stimmen.

### funktionen.linear
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| zwei_punkte | S2/S3 „Liegen A, B, C auf einer Geraden?“ | Ablenker „Nein, AB hat Steigung 1, BC hat 1“ widerspricht sich selbst (sinnlos statt typischer Fehler) |
| proportional | S1 „6 m Stoff kosten 48 €. Wie viel kosten 1 m?“, „2 l … Wie viel kosten 1 l?“ | Grammatik: „Wie viel kostet 1 m?“ |
| proportional | S3 „Ist die Zuordnung … proportional?“ (4×) | Standardprüfung y : x – eher Stufe 2 |
| schnittpunkte | S3 Schnittpunkt zweier Geraden (4×) | gleicher Typ wie Stufe 2, nur andere Zahlen – eher Stufe 2 |
| lage | S3 „Wie liegen y = x − 5 und y = 2x − 6?“, „Steigung parallel zu y = 4x + 6“ | Stufe-1-Niveau |
| deuten | S3 Taxi 31,50 € / Planschbecken 30 cm | gleicher Typ wie Stufe 2 – eher Stufe 2 |
| Lücke | – | fehlten: Steigung in % (Straße/Rampe), Gerade aus Sachdaten (zwei Messwerte), Tarif-Schnittpunkt mit „ab wann billiger“, Fehler finden → ergänzt |
Alle gelesenen Lösungen stimmen.

### funktionen.gebrochen
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| asymptoten | S3 „Gib die waagrechte Asymptote von f(x) = −9/(x − 8) + 2 an“, „… 1/(x + 5) − 3“ | Stufe-1-Typ (direkt ablesen) als Stufe 3 |
| achsenpunkte | S3 „Welche Nullstelle hat f(x) = 3/(x − 4)?“, „… −7/(x + 3)?“ | gleicher Typ wie Stufe 2 – eher Stufe 2 |
| parameter | S3 „Wie unterscheidet sich −3/x von 3/x?“ | gleicher Typ wie Stufe 2 |
| indirekt | – | Karte überschneidet sich mit Thema groessen.indirekt (kein Fehler, nur Hinweis für die Reihenfolge) |
| Lücke | – | fehlten: Wippe/Hebelgesetz, Rechtecke unter der Hyperbel (BMT10), Term aus Graph mit Punkt, Schnitt Hyperbel–Gerade → ergänzt |
Alle gelesenen Lösungen (inkl. aller „Welche Aussage ist FALSCH“-Optionen nachgerechnet) stimmen.

### terme.bruchterme
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| erweitern | S3 „Mit welchem Term wurde 2/(4x) erweitert, wenn der neue Nenner 8x³ ist?“ | gleicher Typ wie Stufe 2 – eher Stufe 2 |
| addieren | S3 „(5x − 7)/x − (2x + 1)/x“, „(5x + 5)/(x + 1) − (4x − 1)/(x + 1)“ | gleicher Nenner, nur Minusklammer – eher Stufe 2 |
| fehler_finden | S3 „Warum ist 5/x + 2/x nicht 7/(2x)?“ | gleicher Typ wie Stufe 2 |
| kuerzen | S3 (x² − 49)/(x − 7) usw. | setzt die 3. binomische Formel voraus; prüfen, ob sie vor diesem Thema eingeführt ist (Reihenfolge) |
| Lücke | – | fehlten: Ausklammern im Nenner für D, „zu einem Bruch zusammenfassen“ mit ganzzahligem Summanden (z. B. 3x/(x − 2) − 1), Hauptnenner bestimmen, (x − 4)/(4 − x), Division mit D-Einschränkung → ergänzt |
Alle gelesenen Lösungen (alle Übungen je Karte) stimmen.

### gleichungen.bruch
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| verhaeltnis | S2 „6 : x = 6 : 6“, „12 : x = 3 : 3“ | trivial (Verhältnis 1 : 1) – Zufallszahlen unglücklich, eher Stufe 1 |
| verhaeltnis | S3 „Für 6 Personen 200 g Mehl … 9 Personen?“ | einfacher Dreisatz – eher Stufe 2 |
| ein_bruch | S1 „Löse 3/x = 3.“ | sehr leicht, in Ordnung für Stufe 1 |
| Lücke | – | fehlten: Sachaufgaben, die auf eine Bruchgleichung führen (Kosten pro Kopf, Rohre), Gleichung ohne Lösung / mit L = D, Begründung „über Kreuz“, Platzhalter-Aufgabe wie im Känguru, Maßstab bei Flächen → ergänzt |
Alle gelesenen Lösungen (alle Übungen je Karte, Stufe 3 vollständig nachgerechnet) stimmen.

### gleichungen.lgs2
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| sachaufgabe | S3 „Ein Händler mischt Erdnüsse … mit Cashewkerne …“ | Grammatik: „mit Cashewkernen“ (Lösung 5 kg stimmt) |
| sachaufgabe | S3 Eintrittskarten (2×) | gleicher Typ wie Stufe 2 – eher Stufe 2 |
| grafisch | S3 „Lies die Lösung … am Schnittpunkt ab“ (2×) | gleicher Typ wie Stufe 1/2 |
| addition | S1 Aufgaben mit fertigen Gegenzahlen | in Ordnung; Stufe 3 enthält keine Aufgabe, bei der beide Gleichungen multipliziert werden müssen → ergänzt |
| Lücke | – | fehlten: Gleichungssystem zu einem Text auswählen, Rückwärts-Parameter, Altersrätsel, Preisaufgabe mit zwei Einkäufen, Bewegungsaufgabe, Ziffernrätsel, Entscheidung ohne Rechnen → ergänzt |
Alle gelesenen Lösungen (alle Übungen je Karte, Stufe 3 vollständig nachgerechnet) stimmen.

### gleichungen.ungleichungen
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| grafisch | S1 „Für welche x liegt der Graph von y = x + 4 oberhalb der x-Achse?“ → „x ≥ −4“ | **Fehler**: „oberhalb“ schließt den Schnittpunkt aus, richtig x > −4 (Lösungsweg begründet mit „bei ≥ gehört er dazu“, im Text steht aber kein ≥) |
| grafisch | S1 „… y = 2x − 4 unterhalb der x-Achse?“ → „x ≤ 2“ | **Fehler** wie oben, richtig x < 2 |
| umformen | S3 „4x + 10 ≤ 4x + 3“, Antwort „L = ℝ (jede Zahl)“ als Ablenker | Zahlbereich in Kl. 8 ist ℚ; ℝ erst in Kl. 9 – besser „L = ℚ“ |
| umformen | S3 „8x + 1 > 4x + 13“, „7x − 3 ≤ 4x + 9“ | x auf beiden Seiten mit positivem Faktor – eher Stufe 2 |
| sachaufgabe | S1/S2 Aufzug/Handytarif in drei Stufen | Stufen 1 und 2 inhaltlich gleich |
| Lücke | – | fehlten: Sonderfälle L = ℚ / L = { }, Schnitt zweier Lösungsmengen (BMT10), Doppelungleichung mit Umdrehen, Kosten pro Person (Bruch-Ungleichung), Mittelwert, Parameter → ergänzt |
Alle übrigen gelesenen Lösungen stimmen.

### zahlen.intervalle
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| lesen | S3 Aquarium 23–27 °C und 24–28 °C | fast gleiche Aufgabe zweimal (nur Zahlen anders) |
| schreiben | S3 „alle Zahlen zwischen −5 und −3, beide Grenzen eingeschlossen“ (3×) | Stufe-1/2-Niveau |
| enthalten | S1 „Welche Zahl liegt im Intervall [1; 7]?“ | nur 3 Antworten – zulässig, aber uneinheitlich |
| (Karte) | lehrplan_gym ist leer | Thema hat keine eigene LehrplanPLUS-Zeile; Inhalt gehört zu Ungleichungen (Kl. 8) |
| Lücke | – | fehlten: Schnitt/Vereinigung, „über/unter/ab/bis einschließlich“ im Sachtext, Abstand („höchstens 3 von 2 entfernt“), „nicht negativ“, Sonderfall [5; 5] → ergänzt |
Alle gelesenen Lösungen (inkl. aller „genau n ganze Zahlen“-Ablenker) stimmen.

### gleichungen.formeln
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| ein_schritt | S3 „R = 10 Ω, U = 230 V. Jemand rechnet I = R : U = 0,04 A …“, Antwort „10 · 0,04 ergibt etwa 0,43“ | **Ungenau**: 10 · 0,04 = 0,4; die 0,43 entsteht nur mit dem ungerundeten 0,0435. Text und Antwort passen nicht zusammen (Kernaussage „nicht 230“ stimmt) |
| geometrie | S3 „Eine Pyramide hat das Volumen 45 cm³ … (V = G · h : 3)“ | Pyramidenvolumen ist Stoff einer höheren Jahrgangsstufe; als reine Formelanwendung vertretbar, aber prüfen |
| geometrie | S3 Quaderhöhe aus Volumen, Länge, Breite (2×) | gleicher Typ wie Stufe 2 |
| einsetzen | S3 Dichte mit dm³ → kg (3× fast gleich: Aluminium, Glas, Eis) | drei sehr ähnliche Aufgaben |
| Lücke | – | fehlten: Linsenformel (Kehrwerte), Parameter aus Messwert (BMT10), Formel mit x auf beiden Seiten, Liter ↔ dm³, Fahrenheit = Celsius, Wirkung von Verdoppeln/Halbieren → ergänzt |
Alle übrigen gelesenen Lösungen stimmen.

### messen.kreisberechnung
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| sektor | S1 „Mittelpunktswinkel 30°. Wie viel Prozent des Kreises sind das? (Runde auf eine Nachkommastelle.)“ | **Toleranz fehlt** bei gerundetem Ergebnis (8,3; Regel README) und Einheit „%“ fehlt; Eingabe 8,33 würde als falsch gewertet |
| umfang | S3 „Ein Kreis hat den Durchmesser 43,2 cm. Berechne den Umfang.“ | Stufe-1-Typ als Stufe 3 |
| flaeche | S3 Pizzavergleich (3×) | dreimal derselbe Typ; Ablenker gut |
| verstehen | S2 „Jemand rechnet A = 2 · π · r …“ (3×) | dreimal fast gleich |
| zylinder | S3 Oberfläche mit Kommazahlen (3×) | gleicher Typ wie Stufe 2, nur krummere Zahlen |
| Lücke | – | fehlten: Preis pro Fläche, Maßstab/Karte (VERA), Kreis vs. Quadrat bei gleichem Umfang, Steigen des Wasserspiegels, Volumenterm auswählen (BMT10), Seil um den Ball, zusammengesetzte Figuren mit exaktem π → ergänzt |
Alle übrigen gelesenen Lösungen (Pizza-, Rad-, Laufbahn-, Scheibenwischer-Aufgaben nachgerechnet) stimmen.

### messen.koerper_darstellung
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| beurteilen | S2/S3 „Ein Zylinder hat genau zwei Kanten.“ (als richtig gewertet) | fachlich umstritten: Manche Schulbücher sprechen beim Zylinder von zwei (gekrümmten) Kanten, andere von keiner Kante. Besser vermeiden oder in der Lernkarte festlegen |
| zylinder | S2 Mantelfläche aus Umfang · Höhe (6×) | sechsmal derselbe Typ |
| netz | S3 „Netz 442 cm², Grundfläche 7 × 8 cm, Höhe?“ (3×) | dreimal derselbe Typ |
| prisma | S3 „Kann ein Prisma 23 / 37 Kanten haben?“ | gut (Begründen) |
| (offen) | Überschneidung mit raum.schraegbilder | Karten „schraegbild“ beider Themen fast gleich – Doppelung im Plan prüfen |
| Lücke | – | fehlten: Würfelnetz ergänzen (VERA 2025), Spielwürfel-Netz, Volumen aus Schrägbild (BMT8 2025), Maßstab bei Volumen, Würfelgebäude, angemalte Würfel → ergänzt |
Alle übrigen gelesenen Lösungen stimmen (Netzflächen, Etiketten, Kantenlängen nachgerechnet).

### raum.schraegbilder
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| (Thema) | lehrplan_gym leer; Raumkoordinaten und windschiefe Geraden | gehören im LehrplanPLUS Gymnasium nicht zu Jgst. 8 (Raumkoordinaten erst in der Oberstufe). Das Thema ist eher Realschul-/Vertiefungsstoff – im Plan als Vertiefung markieren |
| laengen | S3 „Eine Kante führt 2 cm (8 cm) nach hinten. Wie lang mit q = 1/2?“ | Stufe-1-Typ als Stufe 3 |
| lage | S1 „BF und GH“, „BF und DA“ (windschief) | windschief als Stufe 1 – eher Stufe 2 |
| koordinaten | S2 „Gib die z-Koordinate von C an“ (= 0) | in Ordnung, aber dreimal derselbe Typ |
| (Doppelung) | Karte „laengen“ ≈ messen.koerper_darstellung/„schraegbild“ | fast gleiche Aufgaben in zwei Themen |
| Lücke | – | fehlten: Volumen aus Schrägbild (BMT8), Restkörper (BMT8 2008), zusammengesetzte Rotationskörper/Axialschnitt (RS-Prüfungen), Rohr/Doppelkegel, Kantenmodell → ergänzt |
Alle gelesenen Lösungen stimmen (Lagebeziehungen per Programm nachgeprüft).

### stochastik.grundbegriffe
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| laplace | S1 „… 9 rote, 3 blaue und 1 grüne Kugeln …“ | Grammatik: „1 grüne Kugel“ |
| laplace_pruefen | S3 Glücksräder mit verschieden großen Feldern (4×) | gleicher Typ wie Stufe 2 |
| grosse_zahlen | S2 Kronkorken 224/500 und S3 Kronkorken 225/500 | praktisch dieselbe Aufgabe auf zwei Stufen |
| gegenereignis | S3 „KEINE Zahl kleiner oder gleich 1/3 zu werfen“ | umständlich formuliert („eine Zahl größer als 3“) |
| gegenereignis | S3 „3 Würfe, P(mindestens eine Sechs) = 91/216“ | setzt Zählen von 216 Tripeln voraus (Produktregel) – prüfen, ob in Kl. 8 eingeführt |
| Lücke | – | fehlten: Schnittmenge zweier Ereignisse, Ziffer-7-Zählung, Kugeln zusammenschütten, „Würfelgedächtnis“, Glücksrad gestalten, Ergebnisraum hängt vom Notierten ab → ergänzt |
Alle übrigen gelesenen Lösungen stimmen (Augensummen, Gesamt-Häufigkeiten nachgerechnet).

### stochastik.simulation
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| (Thema) | lehrplan_gym leer | Simulation steht im LehrplanPLUS Gym Kl. 8 nicht als eigener Inhalt; als Vertiefung zu „Laplace/relative Häufigkeit“ behandeln |
| auswerten | S2 „400 Durchgänge, 57 Treffer … bei 5 000 echten Durchgängen etwa?“ → 712,5 | „etwa zu erwarten“ mit Kommazahl als exakte Lösung – besser ganze Zahl (713) mit Toleranz oder andere Zahlen |
| auswerten | S3 „Gruppe A 100 / B 50 Durchgänge – wessen Schätzwert …“ (3×) | dreimal derselbe Typ |
| beurteilen | S3 „p = 5/6, Urne 7 von 10“ (2×) | zweimal fast gleich |
| zufallsgeraet | S3 Glücksrad-Winkel aus p (4×) | einschrittig (p · 360°) – eher Stufe 2 |
| Lücke | – | fehlten: Tabellenkalkulation (Formel/Bedingung), Ziehen ohne Zurücklegen, Mehrstufigkeit (Durchgang mit mehreren Ziffern), Warten auf Erfolg, Zusammenfassen von Simulationen, Monte-Carlo mit Kreis/Karte → ergänzt |
Alle gelesenen Lösungen (Ziffern-Zählungen und π-Schätzwerte nachgezählt) stimmen.

### groessen.indirekt (Generator groessen_indirekt.py)
| Lernkarte | Aufgabe | Befund |
|---|---|---|
| erkennen | S3 „… Je mehr, desto weniger, also indirekt proportional.“ (4×) | viermal derselbe Typ |
| unterscheiden | S1/S2 „Welche Art von Zuordnung zeigt die Tabelle?“ (11×) | gleicher Typ auf zwei Stufen; S2 nur mit 4. Ablenker „nicht zu entscheiden“ |
| sach | S3 Freizeitpark (3×, nur Zahlen anders) | dreimal fast gleich |
| sach | S2 „Taxi … Was kosten 6 km?“ | gehört zu „weder noch“ – gut als Abgrenzung, aber in der Karte „Sachaufgaben (indirekt)“ überraschend |
| (Thema) | lehrplan_gym leer; Überschneidung mit funktionen.gebrochen/„indirekt“ | Reihenfolge im Plan klären |
| Lücke | – | fehlten: Summe statt Produkt konstant (fester Umfang), Messreihe mit Ausreißer, Prozent-Änderung, Arbeitsauftrag mit Ausfall, Zahnräder, Tabellenkalkulation, gemischte Proportionalität → ergänzt |
Alle gelesenen Lösungen stimmen.

(2) Prüfungsquellen je Thema und abgeleitete Aufgabentypen

Allgemeine Quellen (Adressen):
- [BMT8 2025 A] https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/BMT8_2025_Aufgaben_Gruppe_A.pdf
- [BMT8 2024 A] https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/BMT8_2024_Aufgaben_Gruppe_A.pdf
- [BMT8 2023 A] https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2023/BMT8_2023_Aufgaben_Gruppe_A.pdf
- [BMT8 2022 A] https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2022/bmt8_2022_aufgaben_gruppe_a.pdf
- [BMT8 2015 B] https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2015/bmt8_2015_aufgaben_gruppe_b.pdf
- [BMT8 2008 B] https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2008/bmt8_2008_aufgaben_gruppe_b.pdf
- [BMT10 2024 A/B] https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/BMT10_2024_Aufgaben_Gruppe_A.pdf und …_Gruppe_B.pdf
- [BMT10 2023 B] https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2023/BMT10_2023_Aufgaben_Gruppe_B.pdf
- [BMT10 2022 A] https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2022/bmt10_2022_aufgaben_gruppe_a.pdf
- [BMT10 2021 A] https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2021/bmt10_2021_aufgaben_gruppe_a.pdf
- [BMT10 2017 A] https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2017/bmt10_2017_aufgaben_gruppe_a.pdf
- [BMT10 2011 A] https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2011/bmt10_aufgabe_a.pdf
- [RS-JT8 2023] https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2023/2023_JT_Mathe_8_I_Angabe.pdf
- [RS-JT8 2014] https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2014/jahrgangsstufe_8_i_loesung_mit_deckblatt.pdf
- [RS-LA8] https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Mathematik/Weiterentwicklung_Abschlusspruefung/Exemplarische_Leistungsaufgaben/rs_m_08_leistungsaufgaben_8i.pdf
- [RS-LA9] https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Mathematik/Weiterentwicklung_Abschlusspruefung/Exemplarische_Leistungsaufgaben/rs_m_09_leistungsaufgaben_9ii.pdf
- [RS-AP 2022/2024] https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2022/2022_mii_ht.pdf und https://isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2024/2024_mii_ht.pdf
- [VERA 2026] https://www.iqb.hu-berlin.de/media/exercise_group_files/VERA-8_Mathematik/V8_2026_MA_ModulB_lMRNeBJ.pdf (Ebene Figuren, Zufall)
- [VERA 2025] https://www.iqb.hu-berlin.de/media/exercise_group_files/VERA-8_Mathematik/V8_2025_MA_ModulB_LjTPG3v.pdf (Raum und Form)
- [VERA 2012] https://www.nibis.de/nli1/allgemein/gosin/vergleich/v8-2012/MatheDidaktHinw2012/V8-2012_MA-Modul-C_TH-III_2012_01_16.pdf („Ungleichung erfüllen“)
- [GW-Kempten] https://hildegardis-gymnasium.de/wp-content/uploads/2026/07/8.-Klasse-Grundwissen-Mathe.pdf (Grundwissen 8, Standardaufgaben)
- [GW-Stein] https://unterrichten.zum.de/images/5/5a/Whaufgaben8.pdf
- [Stark-SA8] Leseprobe „Schulaufgaben Gymnasium Mathematik 8. Klasse Bayern“: https://buch-ka.de/media/44/d1/35/1648766582/9kkzw5kc3ryzwftcmvuzg9iagp4cmvmcjagmzk3iaowmdawmdawmdawidy1ntm1igygcjawmdawmdawmtugmdawmdagbiakmdawmdawmda5msawmdawmcbuiaowmdawmdawmji4idawmdawig4gcjawmdawmde2mjigmdawmdagbiakmdawmtgvtvt6qf7zeb.pdf
- [ISB-G8 M8.3] https://www.gym8-lehrplan.bayern.de/contentserv/3.1.neu/g8.de/data/media/26765/M_8.3_Elementare_gebrochen-rationale_Funktionen.pdf
- [UBT-Bruchgl] https://btmdx1.mat.uni-bayreuth.de/kcm/data/Materials/FertigeLernumgebungen/Bruchgleichungen.docx
- [Känguru] https://ksreussbuehl.lu.ch/-/media/KSReussbuehl/Dokumente/Ausbildung/Fachschaften/Mathematik/Kaenguru/14_78.pdf, …/testfragen_2010_stufen_7_und_8.pdf, https://didaktik.mathematik.hu-berlin.de/user/beierarx/kaenguru2024_78.pdf
- [NRW-Sim] https://schulentwicklung.nrw.de/materialdatenbank/material/download/7005 (Materialaufgabe Simulation mit Tabellenkalkulation)

Hinweis zum Niveau: Der BMT8 wird in Jgst. 8 geschrieben, prüft aber vor allem Stoff bis Jgst. 7. Für den Stoff der Jgst. 8 (Bruchterme, Hyperbeln, LGS, Kreis, Laplace) waren BMT10 (prüft Grundwissen aus 8/9), VERA-8, Grundwissen-/Schulaufgabensammlungen bayerischer Gymnasien und Realschul-Prüfungen die passenderen Vorbilder.

| Thema | Quellen | daraus abgeleitete Aufgabentypen (Wortlaut, Einkleidung und Zahlen eigen) |
|---|---|---|
| funktionen.grundbegriffe | BMT8 2022/2025, BMT8 2024, Stark-SA8, GW-Kempten | Tabellenkalkulations-Formel auswerten/auswählen (Punkt vor Strich), Rückwärts „Zahl ersetzen“, Zuordnung im Sachkontext begründen (Rennstrecke), D und W im Sachzusammenhang, Achsenschnittpunkte, Punkt ober-/unterhalb, Term aus Wertetabelle |
| funktionen.linear | BMT10 2017, Stark-SA8, GW-Kempten, BMT10 2024, RS-JT8 2023 | Steigung in % (Straße, Rampe), Gerade aus zwei Messwerten (Kostenfunktion), Achsenabschnitt deuten, Tarifschnittpunkt und „ab wann billiger“, Rechenfehler finden |
| funktionen.gebrochen | BMT10 2024 B, GW-Kempten, Stark-SA8, BMT8 2025 | Rechtecke unter der Hyperbel (konstante Fläche), Wippe, Term aus Graph mit Punkt, Schnitt mit Gerade, Graph–Term zuordnen, Aussage widerlegen |
| terme.bruchterme | BMT10 2024 B, GW-Kempten, GW-Stein, Stark-SA8, BMT8 2022/2025, RS-JT8 2023 | Ausklammern vor Kürzen und für D, „zu einem Bruch zusammenfassen“ mit ganzem Summanden, Hauptnenner, Tabellenkalkulation, Fehler finden |
| gleichungen.bruch | Känguru 2014, ISB-G8 M8.3, UBT-Bruchgl, BMT8 2024, BMT8 2025, BMT10 2024, GW-Kempten | Platzhalter in zwei Brüchen, „über Kreuz“ begründen, Textaufgaben (Kosten pro Kopf, Rohre), Rückwärts-Parameter, Maßstab bei Flächen, grafische Lösung |
| gleichungen.lgs2 | GW-Kempten, Stark-SA8, BMT8 2024, Känguru | Text → LGS auswählen, Altersrätsel, zwei Einkäufe, Bewegungsaufgabe, Tarife, beide Gleichungen multiplizieren, Lösbarkeit mit Parameter, Ziffernrätsel |
| gleichungen.ungleichungen | VERA 2012, BMT10 2022, Stark-SA8, BMT8 2025 | Zahlen auf Erfüllung prüfen (Grenze!), Schnitt zweier Lösungsmengen, Sonderfälle L = ℚ / L = { }, Fehler beim Umdrehen, Kosten pro Person, Mittelwert, Tarif „ab wann“ |
| zahlen.intervalle | BMT10 2022 (Mengen) – **keine eigenen Prüfungsaufgaben zu Intervallen gefunden** | Schnitt/Vereinigung, Sachbedingungen „über/unter/ab/bis einschließlich“, Lösungsmenge als Intervall |
| gleichungen.formeln | GW-Kempten (Linsen-, Trapezformel), BMT10 2024 A, BMT8 2023, RS-JT8 2023 | Formel umstellen und einsetzen (Kehrwerte), Parameter aus Messwert, Liter ↔ dm³, Umstellung mit Zahlen prüfen |
| messen.kreisberechnung | RS-JT8 2014, VERA 2026, BMT10 2024 B, BMT10 2021, BMT8 2025, Känguru | Preis pro Fläche (Pizza), Karte mit Maßstab (See), gleicher Zaun – größte Fläche, Volumenterm auswählen, Wasserspiegel, zusammengesetzte Figuren |
| messen.koerper_darstellung | VERA 2025, BMT8 2025, BMT8 2015, BMT8 2008, Känguru | Würfelnetz ergänzen, Spielwürfel-Netz, Ecken/Kanten-Tabelle, Volumen aus Schrägbild, Maßstab 1 : 10 beim Volumen, angemalte Würfel |
| raum.schraegbilder | RS-LA8, RS-LA9, RS-AP 2022/2024, BMT8 2025/2008, RS-JT8 2023, VERA 2025 – **für Raumkoordinaten und windschiefe Geraden keine Aufgaben auf Kl.-8-Niveau** (Typen übertragen) | Axialschnitt/Teilkörper, Kantenmodell aus Draht, Restkörper, Mittelpunkt-Fehler (auf 3D übertragen) |
| stochastik.grundbegriffe | VERA 2026, BMT10 2024 B, BMT10 2011, BMT10 2023 B, BMT8 2023, GW-Kempten | Ziffer 7 in 1–100, Schnittmenge von Ereignissen, Augensumme, Säckchen zusammenschütten, Würfelgedächtnis, Glücksrad gestalten, „keiner der beiden“ |
| stochastik.simulation | NRW-Sim, BMT8 2022/2025, VERA 2026 – **keine bayerischen Prüfungsaufgaben zur Simulation gefunden** | Tabellenkalkulation (ZUFALLSBEREICH, Bedingung), Durchgänge mit mehreren Ziffern, Ziehen ohne Zurücklegen, Monte-Carlo mit Kreis/Karte |
| groessen.indirekt | GW-Kempten, Stark-SA8, BMT10 2024 B, BMT8 2022/2025, Känguru | Begründung „doppelt → halb“, Messreihe mit Ausreißer, Wippe, Zahnräder, Arbeitsauftrag mit Ausfall, Tabellenkalkulation, gemischte Proportionalität |

(3) Neue Aufgaben je Lernkarte und Stufe (alle im Pool uebung)

| Thema | Lernkarte | neu Stufe 3 | neu Stufe 2 | Stufe-3-Übungen danach |
|---|---|---|---|---|
| funktionen.grundbegriffe | eindeutig | 4 | 2 | 8 |
| funktionen.grundbegriffe | mengen | 4 | 2 | 8 |
| funktionen.grundbegriffe | funktionswert | 4 | 2 | 8 |
| funktionen.grundbegriffe | stelle | 4 | 2 | 8 |
| funktionen.grundbegriffe | wertetabelle | 4 | 2 | 8 |
| funktionen.grundbegriffe | graph_lesen | 4 | 2 | 8 |
| funktionen.grundbegriffe | nullstellen | 4 | 2 | 8 |
| funktionen.grundbegriffe | punkt_graph | 4 | 2 | 8 |
| funktionen.linear | ablesen | 4 | 2 | 8 |
| funktionen.linear | zwei_punkte | 4 | 2 | 8 |
| funktionen.linear | proportional | 4 | 2 | 8 |
| funktionen.linear | aufstellen | 4 | 2 | 8 |
| funktionen.linear | schnittpunkte | 4 | 2 | 8 |
| funktionen.linear | lage | 4 | 2 | 8 |
| funktionen.linear | deuten | 4 | 2 | 8 |
| funktionen.gebrochen | indirekt | 4 | 2 | 8 |
| funktionen.gebrochen | definitionsmenge | 4 | 2 | 8 |
| funktionen.gebrochen | asymptoten | 4 | 2 | 8 |
| funktionen.gebrochen | achsenpunkte | 4 | 2 | 8 |
| funktionen.gebrochen | parameter | 4 | 2 | 8 |
| funktionen.gebrochen | beurteilen | 4 | 2 | 8 |
| terme.bruchterme | definitionsmenge | 4 | 2 | 8 |
| terme.bruchterme | termwert | 4 | 2 | 8 |
| terme.bruchterme | kuerzen | 4 | 2 | 8 |
| terme.bruchterme | erweitern | 4 | 2 | 8 |
| terme.bruchterme | addieren | 4 | 2 | 8 |
| terme.bruchterme | multiplizieren | 4 | 2 | 8 |
| terme.bruchterme | fehler_finden | 4 | 2 | 8 |
| gleichungen.bruch | definitionsmenge | 4 | 2 | 8 |
| gleichungen.bruch | ein_bruch | 4 | 2 | 8 |
| gleichungen.bruch | ueber_kreuz | 4 | 2 | 8 |
| gleichungen.bruch | hauptnenner | 4 | 2 | 8 |
| gleichungen.bruch | scheinloesung | 4 | 2 | 8 |
| gleichungen.bruch | verhaeltnis | 4 | 2 | 8 |
| gleichungen.bruch | graphisch | 4 | 2 | 8 |
| gleichungen.lgs2 | pruefen | 4 | 2 | 8 |
| gleichungen.lgs2 | grafisch | 4 | 2 | 8 |
| gleichungen.lgs2 | einsetzen | 4 | 2 | 8 |
| gleichungen.lgs2 | gleichsetzen | 4 | 2 | 8 |
| gleichungen.lgs2 | addition | 4 | 2 | 8 |
| gleichungen.lgs2 | verfahren | 4 | 2 | 8 |
| gleichungen.lgs2 | loesbarkeit | 4 | 2 | 8 |
| gleichungen.lgs2 | sachaufgabe | 4 | 2 | 8 |
| gleichungen.ungleichungen | umformen | 4 | 2 | 8 |
| gleichungen.ungleichungen | umdrehen | 4 | 2 | 8 |
| gleichungen.ungleichungen | klammern | 4 | 2 | 8 |
| gleichungen.ungleichungen | intervall | 4 | 2 | 8 |
| gleichungen.ungleichungen | pruefen | 4 | 2 | 8 |
| gleichungen.ungleichungen | grafisch | 4 | 2 | 8 |
| gleichungen.ungleichungen | sachaufgabe | 4 | 2 | 8 |
| zahlen.intervalle | lesen | 4 | 2 | 8 |
| zahlen.intervalle | schreiben | 4 | 2 | 8 |
| zahlen.intervalle | enthalten | 4 | 2 | 8 |
| zahlen.intervalle | beurteilen | 4 | 2 | 8 |
| gleichungen.formeln | ein_schritt | 4 | 2 | 8 |
| gleichungen.formeln | zwei_schritte | 4 | 2 | 8 |
| gleichungen.formeln | pruefen | 4 | 2 | 8 |
| gleichungen.formeln | einsetzen | 4 | 2 | 8 |
| gleichungen.formeln | geometrie | 4 | 2 | 8 |
| messen.kreisberechnung | umfang | 4 | 2 | 8 |
| messen.kreisberechnung | flaeche | 4 | 2 | 8 |
| messen.kreisberechnung | exakt | 4 | 2 | 8 |
| messen.kreisberechnung | verstehen | 4 | 2 | 8 |
| messen.kreisberechnung | sektor | 4 | 2 | 8 |
| messen.kreisberechnung | zusammengesetzt | 4 | 2 | 8 |
| messen.kreisberechnung | zylinder | 4 | 2 | 8 |
| messen.koerper_darstellung | prisma | 4 | 2 | 8 |
| messen.koerper_darstellung | netz | 4 | 2 | 8 |
| messen.koerper_darstellung | zylinder | 4 | 2 | 8 |
| messen.koerper_darstellung | schraegbild | 4 | 2 | 8 |
| messen.koerper_darstellung | ansichten | 4 | 2 | 8 |
| messen.koerper_darstellung | beurteilen | 4 | 2 | 8 |
| raum.schraegbilder | pyramide | 4 | 2 | 8 |
| raum.schraegbilder | laengen | 4 | 2 | 8 |
| raum.schraegbilder | lage | 4 | 2 | 8 |
| raum.schraegbilder | koordinaten | 4 | 2 | 8 |
| raum.schraegbilder | rotation | 4 | 2 | 8 |
| raum.schraegbilder | axialschnitt | 4 | 2 | 8 |
| stochastik.grundbegriffe | begriffe | 4 | 2 | 8 |
| stochastik.grundbegriffe | rel_haeufigkeit | 4 | 2 | 8 |
| stochastik.grundbegriffe | laplace | 4 | 2 | 8 |
| stochastik.grundbegriffe | laplace_pruefen | 4 | 2 | 8 |
| stochastik.grundbegriffe | gegenereignis | 4 | 2 | 8 |
| stochastik.grundbegriffe | grosse_zahlen | 4 | 2 | 8 |
| stochastik.simulation | zufallsgeraet | 4 | 2 | 8 |
| stochastik.simulation | regel | 4 | 2 | 8 |
| stochastik.simulation | zufallsziffern | 4 | 2 | 8 |
| stochastik.simulation | auswerten | 4 | 2 | 8 |
| stochastik.simulation | monte_carlo | 4 | 2 | 8 |
| stochastik.simulation | beurteilen | 4 | 2 | 8 |
| groessen.indirekt | erkennen | 4 | 2 | 9 |
| groessen.indirekt | vervielfachen | 4 | 2 | 9 |
| groessen.indirekt | produkt | 4 | 2 | 9 |
| groessen.indirekt | dreisatz | 4 | 2 | 9 |
| groessen.indirekt | graph | 4 | 2 | 9 |
| groessen.indirekt | unterscheiden | 4 | 2 | 9 |
| groessen.indirekt | sach | 4 | 2 | 9 |

Summe: 582 neue Übungen in 15 Themen, 97 Lernkarten – je Karte 4 × Stufe 3 und 2 × Stufe 2, davon je Karte mindestens 2 nach Prüfungsvorbild (P) und 1–2 Knobelaufgaben (K).

(4) Themen ohne passende Prüfungsaufgaben
- zahlen.intervalle: Intervalle werden in Prüfungen nicht eigenständig abgefragt; Vorbild nur Mengen-/Ungleichungsaufgaben (BMT10 2022).
- stochastik.simulation: keine bayerischen Prüfungsaufgaben; Vorbilder sind eine NRW-Materialaufgabe, BMT-Tabellenkalkulation und VERA-Zufallsaufgaben.
- raum.schraegbilder, Karten „koordinaten“ und „lage“: Raumkoordinaten/windschief liegen über dem Gym-Lehrplan Kl. 8; die P-Aufgaben dort sind übertragene Typen (Mittelpunkt-Fehler aus RS-JT8 2023, Volumen aus Koordinaten).

Offene Punkte für den Haupt-Chat
- funktionen.grundbegriffe „offen“: Der Eintrag „Kreis kann die App nicht zeichnen“ ist veraltet (koordinaten.kreise); eine neue Aufgabe nutzt den Kreis.
- Die Fehler aus der Befundliste brauchen eine Entscheidung. Ändern hieße Lernstände verlieren; Vorschlag: beim nächsten Umbau neue, korrigierte Aufgabe dazu und die alte ausblenden.
- Doppelungen zwischen Themen: messen.koerper_darstellung/„schraegbild“ ≈ raum.schraegbilder/„laengen“; funktionen.gebrochen/„indirekt“ ≈ groessen.indirekt.

## 2026-11-16 11:00 – STATUS
groessen.indirekt fertig: 42 neue Übungen. Prüfskript OK, Unverändert-Nachweis JA. Helfer übernimmt jetzt die Teilfähigkeit aus der Datei (hier fasst ein k mehrere Lernziele zusammen); alle anderen Themen bauen unverändert.

## 2026-11-16 10:35 – STATUS
stochastik.simulation fertig: 36 neue Übungen. Prüfskript OK, Unverändert-Nachweis JA. Echte Prüfungsaufgaben zur Simulation nicht gefunden – Vorbilder übertragen (siehe Abschlussbericht).

## 2026-11-16 10:05 – STATUS
stochastik.grundbegriffe fertig: 36 neue Übungen. Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 09:40 – STATUS
raum.schraegbilder fertig: 36 neue Übungen. Prüfskript OK, Unverändert-Nachweis JA. Hinweis: Raumkoordinaten/windschief liegen über dem Gym-Lehrplan Kl. 8 (siehe Befundliste).

## 2026-11-16 09:15 – STATUS
messen.koerper_darstellung fertig: 36 neue Übungen. Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 08:50 – STATUS
messen.kreisberechnung fertig: 42 neue Übungen. Prüfskript OK, Unverändert-Nachweis JA. Gerundete Ergebnisse haben Toleranz und einen Rechenausdruck mit round(…).

## 2026-11-16 08:25 – STATUS
gleichungen.formeln fertig: 30 neue Übungen. Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 08:10 – STATUS
zahlen.intervalle fertig: 24 neue Übungen. Prüfskript OK, Unverändert-Nachweis JA. Echte Prüfungsaufgaben nur zu Intervallen gibt es kaum; Vorbild sind Mengen-/Ungleichungsaufgaben (siehe Abschlussbericht).

## 2026-11-16 07:55 – STATUS
gleichungen.ungleichungen fertig: 42 neue Übungen. Prüfskript OK, Unverändert-Nachweis JA. Fund: zwei S1-Aufgaben der Karte „grafisch“ antworten „x ≥ −4“ bzw. „x ≤ 2“ auf „oberhalb/unterhalb“ (richtig wären > bzw. <) – nicht geändert, steht in der Befundliste.

## 2026-11-16 07:30 – STATUS
gleichungen.lgs2 fertig: 48 neue Übungen (8 Karten × 4 S3 + 2 S2). Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 07:05 – STATUS
gleichungen.bruch fertig: 42 neue Übungen (7 Karten × 4 S3 + 2 S2). Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 06:45 – STATUS
terme.bruchterme fertig: 42 neue Übungen (7 Karten × 4 S3 + 2 S2). Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 06:25 – STATUS
funktionen.gebrochen fertig: 36 neue Übungen (6 Karten × 4 S3 + 2 S2). Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 06:05 – STATUS
funktionen.linear fertig: 42 neue Übungen (7 Karten × 4 S3 + 2 S2). Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 05:40 – STATUS
funktionen.grundbegriffe fertig: 48 neue Übungen (je Lernkarte 4 × Stufe 3, 2 × Stufe 2; je Karte ≥ 2 nach Prüfungsvorbild, ≥ 1 Knobel).
Prüfskript OK, Unverändert-Nachweis JA (`python3 -I inhalte/generatoren/_unveraendert_kl8.py funktionen.grundbegriffe`).
Technik: Abschnitt SCHWER am Ende des Generators, Helfer `inhalte/generatoren/_schwer_kl8.py` (eigener Zufallsstart, Anhängen erst nach dem fertigen Bau).
