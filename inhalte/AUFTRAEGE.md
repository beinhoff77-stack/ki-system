# Aufträge für die parallelen Chats

Je Paket einen neuen Claude-Chat (Claude Code mit Zugriff auf das Repository `beinhoff77-stack/ki-system`) öffnen und den Text im Kasten einfügen. Die Chats arbeiten unabhängig; jeder hat seinen eigenen Zweig.

Reihenfolge, falls nicht alle vier gleichzeitig laufen: **Klasse 5 → Klasse 8 → Klasse 6 → Klasse 9**.


## Paket Klasse 5 (11 Themen) – Kind A, Klasse 5 – läuft gerade, höchste Priorität

```text
Du baust Mathe-Lerninhalte für eine Lern-App (Gymnasium Bayern, Klasse 5).
Repository: beinhoff77-stack/ki-system, Ausgangszweig lernen-app. Lege den Zweig inhalte-kl5 an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (Format, Regeln, Verbote), inhalte/vorlage_generator.py (Muster)
und die Einträge mit "gym_by": 5 in inhalte/themenliste.json (Umfang und Lehrplan-Wortlaut je Thema).

Aufgabe: Baue diese Themen nacheinander in dieser Reihenfolge. Je Thema ein Generator
(inhalte/generatoren/<thema_schluessel>.py), der inhalte/themen/<thema_schluessel>.json schreibt.

 1. zahlen.ganz – Ganze Zahlen (thema_id 16, block_id 49)
 2. zahlen.rechengesetze – Grundrechenarten und Rechengesetze (thema_id 18, block_id 49)
 3. zahlen.potenzen_basis – Potenzen als Schreibweise (thema_id 67, block_id 49)
 4. groessen.einheiten – Größen und Einheiten (thema_id 25, block_id 55)
 5. groessen.proportional – Direkte Proportionalität und Dreisatz (thema_id 26, block_id 54)
 6. geometrie.grundbegriffe – Grundbegriffe und Figuren (thema_id 42, block_id 83)
 7. geometrie.winkel – Winkelsätze (thema_id 43, block_id 81)
 8. geometrie.ortslinien – Ortslinien und Ortsbereiche (thema_id 73, block_id 79)
 9. messen.flaechen – Umfang und Flächeninhalt (thema_id 50, block_id 87)
10. messen.koerper_berechnung – Volumen und Oberfläche (thema_id 53, block_id 85)
11. stochastik.kombinatorik – Zählen und Kombinatorik (thema_id 60, block_id 95)

Regeln:
- Ein Thema ist erst fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet
  und jede Zahl-Aufgabe nachgerechnet ist. Dann Commit + Push auf inhalte-kl5 (ein Thema = ein Commit).
- Keine Datenbank, keine Serverfunktionen, kein App-Code, kein Merge nach main. Nur Dateien unter inhalte/.
- Keine Schulbuchaufgaben abschreiben. Lösungen immer vom Programm berechnen lassen.
- Braucht eine Lernkarte eine Zeichnung, die die App nicht kann: nicht erfinden, sondern im Feld "offen" der Datei notieren.
- Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

Am Ende: kurze Liste der fertigen Dateien mit Anzahl Lernkarten/Aufgaben und alle "offen"-Punkte.
```

## Paket Klasse 8 (14 Themen) – Kind B, Klasse 8 – höchste Priorität

```text
Du baust Mathe-Lerninhalte für eine Lern-App (Gymnasium Bayern, Klasse 8).
Repository: beinhoff77-stack/ki-system, Ausgangszweig lernen-app. Lege den Zweig inhalte-kl8 an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (Format, Regeln, Verbote), inhalte/vorlage_generator.py (Muster)
und die Einträge mit "gym_by": 8 in inhalte/themenliste.json (Umfang und Lehrplan-Wortlaut je Thema).

Aufgabe: Baue diese Themen nacheinander in dieser Reihenfolge. Je Thema ein Generator
(inhalte/generatoren/<thema_schluessel>.py), der inhalte/themen/<thema_schluessel>.json schreibt.

 1. gleichungen.ungleichungen – Lineare Ungleichungen (thema_id 3, block_id 61)
 2. zahlen.intervalle – Intervalle (thema_id 69, block_id 61)
 3. terme.bruchterme – Bruchterme (thema_id 31, block_id 60)
 4. gleichungen.formeln – Formeln umstellen (thema_id 4, block_id 60)
 5. gleichungen.bruch – Bruch- und Verhältnisgleichungen (thema_id 5, block_id 60)
 6. gleichungen.lgs2 – Gleichungssysteme mit 2 Unbekannten (thema_id 6, block_id 59)
 7. funktionen.grundbegriffe – Zuordnung und Funktion (thema_id 32, block_id 73)
 8. funktionen.linear – Lineare Funktionen (thema_id 33, block_id 72)
 9. funktionen.gebrochen – Gebrochen-rationale Funktionen (thema_id 34, block_id 71)
10. messen.koerper_darstellung – Körper darstellen (thema_id 52, block_id 86)
11. raum.schraegbilder – Schrägbilder und Raumdarstellung (thema_id 91, block_id 109)
12. messen.kreisberechnung – Kreisberechnungen (thema_id 51, block_id 84)
13. stochastik.grundbegriffe – Zufall und Laplace (thema_id 61, block_id 92)
14. stochastik.simulation – Simulation (thema_id 64, block_id 90)

Regeln:
- Ein Thema ist erst fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet
  und jede Zahl-Aufgabe nachgerechnet ist. Dann Commit + Push auf inhalte-kl8 (ein Thema = ein Commit).
- Keine Datenbank, keine Serverfunktionen, kein App-Code, kein Merge nach main. Nur Dateien unter inhalte/.
- Keine Schulbuchaufgaben abschreiben. Lösungen immer vom Programm berechnen lassen.
- Braucht eine Lernkarte eine Zeichnung, die die App nicht kann: nicht erfinden, sondern im Feld "offen" der Datei notieren.
- Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

Am Ende: kurze Liste der fertigen Dateien mit Anzahl Lernkarten/Aufgaben und alle "offen"-Punkte.
```

## Paket Klasse 6 (8 Themen) – Kind A, Klasse 6

```text
Du baust Mathe-Lerninhalte für eine Lern-App (Gymnasium Bayern, Klasse 6).
Repository: beinhoff77-stack/ki-system, Ausgangszweig lernen-app. Lege den Zweig inhalte-kl6 an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (Format, Regeln, Verbote), inhalte/vorlage_generator.py (Muster)
und die Einträge mit "gym_by": 6 in inhalte/themenliste.json (Umfang und Lehrplan-Wortlaut je Thema).

Aufgabe: Baue diese Themen nacheinander in dieser Reihenfolge. Je Thema ein Generator
(inhalte/generatoren/<thema_schluessel>.py), der inhalte/themen/<thema_schluessel>.json schreibt.

 1. zahlen.potenzen_zehner – Zehnerpotenzen und wissenschaftliche Schreibweise (thema_id 19, block_id 49)
 2. bruch.brueche – Brüche und Anteile (thema_id 21, block_id 47)
 3. bruch.dezimal – Dezimalzahlen (thema_id 22, block_id 46)
 4. bruch.rechnen – Rechnen mit rationalen Zahlen (thema_id 23, block_id 45)
 5. terme.potenzgesetze – Potenzen und Potenzgesetze (thema_id 30, block_id 44)
 6. bruch.prozent – Prozent- und Zinsrechnung (thema_id 24, block_id 53)
 7. daten.darstellen – Daten erfassen und darstellen (thema_id 57, block_id 96)
 8. daten.kennwerte – Mittelwert und Häufigkeiten (thema_id 58, block_id 94)

Regeln:
- Ein Thema ist erst fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet
  und jede Zahl-Aufgabe nachgerechnet ist. Dann Commit + Push auf inhalte-kl6 (ein Thema = ein Commit).
- Keine Datenbank, keine Serverfunktionen, kein App-Code, kein Merge nach main. Nur Dateien unter inhalte/.
- Keine Schulbuchaufgaben abschreiben. Lösungen immer vom Programm berechnen lassen.
- Braucht eine Lernkarte eine Zeichnung, die die App nicht kann: nicht erfinden, sondern im Feld "offen" der Datei notieren.
- Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

Am Ende: kurze Liste der fertigen Dateien mit Anzahl Lernkarten/Aufgaben und alle "offen"-Punkte.
```

## Paket Klasse 9 (14 Themen) – Kind B, Klasse 9

```text
Du baust Mathe-Lerninhalte für eine Lern-App (Gymnasium Bayern, Klasse 9).
Repository: beinhoff77-stack/ki-system, Ausgangszweig lernen-app. Lege den Zweig inhalte-kl9 an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (Format, Regeln, Verbote), inhalte/vorlage_generator.py (Muster)
und die Einträge mit "gym_by": 9 in inhalte/themenliste.json (Umfang und Lehrplan-Wortlaut je Thema).

Aufgabe: Baue diese Themen nacheinander in dieser Reihenfolge. Je Thema ein Generator
(inhalte/generatoren/<thema_schluessel>.py), der inhalte/themen/<thema_schluessel>.json schreibt.

 1. zahlen.wurzeln_basis – Elementare Wurzeln (thema_id 68, block_id 43)
 2. zahlen.reell – Wurzeln und reelle Zahlen (thema_id 20, block_id 43)
 3. zahlen.rationale_exponenten – Rationale Exponenten und n-te Wurzel (thema_id 96, block_id 106)
 4. gleichungen.quadratisch – Quadratische Gleichungen (allgemein) (thema_id 8, block_id 58)
 5. gleichungen.potenz – Potenzgleichungen (thema_id 9, block_id 57)
 6. gleichungen.lgs3 – Gleichungssysteme mit 3 Unbekannten (thema_id 7, block_id 113)
 7. funktionen.quadratisch – Quadratische Funktionen (thema_id 35, block_id 70)
 8. funktionen.potenz – Potenzfunktionen (thema_id 36, block_id 69)
 9. abbildungen.aehnlichkeit – Ähnlichkeit und Strahlensätze (thema_id 47, block_id 78)
10. trigo.pythagoras – Satz des Pythagoras (thema_id 54, block_id 77)
11. trigo.rechtwinklig – Trigonometrie im rechtwinkligen Dreieck (thema_id 55, block_id 76)
12. trigo.allgemein – Allgemeine Trigonometrie (thema_id 56, block_id 76)
13. gleichungen.trig – Trigonometrische Gleichungen (thema_id 14, block_id 76)
14. stochastik.verknuepft – Verknüpfte Ereignisse (thema_id 63, block_id 91)

Regeln:
- Ein Thema ist erst fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet
  und jede Zahl-Aufgabe nachgerechnet ist. Dann Commit + Push auf inhalte-kl9 (ein Thema = ein Commit).
- Keine Datenbank, keine Serverfunktionen, kein App-Code, kein Merge nach main. Nur Dateien unter inhalte/.
- Keine Schulbuchaufgaben abschreiben. Lösungen immer vom Programm berechnen lassen.
- Braucht eine Lernkarte eine Zeichnung, die die App nicht kann: nicht erfinden, sondern im Feld "offen" der Datei notieren.
- Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

Am Ende: kurze Liste der fertigen Dateien mit Anzahl Lernkarten/Aufgaben und alle "offen"-Punkte.
```


---

# Zweite Runde (14.11.): Rest Klasse 5, Klasse 7, Klasse 10

Die Pakete Klasse 6, 8 und 9 sind erledigt und eingespielt. Für die neuen Pakete gilt dieselbe Vorgehensweise.

## Paket Klasse 5 Rest (7 Themen) – Kind A, höchste Priorität

```text
Du baust Mathe-Lerninhalte für eine Lern-App (Gymnasium Bayern, Klasse 5).
Repository: beinhoff77-stack/ki-system, Ausgangszweig lernen-app. Lege den Zweig inhalte-kl5-rest an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (Format, Regeln, Verbote, Erfahrungen aus der ersten Runde),
inhalte/vorlage_generator.py (Muster) und die Einträge der unten genannten Themen in inhalte/themenliste.json.
Als Beispiel für ein fertiges Thema: inhalte/generatoren/zahlen_ganz.py mit inhalte/themen/zahlen.ganz.json.

Aufgabe: Baue diese Themen nacheinander in dieser Reihenfolge. Je Thema ein Generator
(inhalte/generatoren/<thema_schluessel>.py), der inhalte/themen/<thema_schluessel>.json schreibt.

 1. groessen.einheiten – Größen und Einheiten (thema_id 25, block_id 55)
 2. geometrie.grundbegriffe – Grundbegriffe und Figuren (thema_id 42, block_id 83)
 3. geometrie.winkel – Winkelsätze (thema_id 43, block_id 81)
 4. geometrie.ortslinien – Ortslinien und Ortsbereiche (thema_id 73, block_id 79)
 5. messen.flaechen – Umfang und Flächeninhalt (thema_id 50, block_id 87)
 6. messen.koerper_berechnung – Volumen und Oberfläche (thema_id 53, block_id 85)
 7. stochastik.kombinatorik – Zählen und Kombinatorik (thema_id 60, block_id 95)

Regeln:
- Ein Thema ist erst fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet
  und jede Zahl-Aufgabe nachgerechnet ist. Dann Commit + Push auf inhalte-kl5-rest (ein Thema = ein Commit).
- Eigene Hilfsdatei nur unter dem Namen inhalte/generatoren/_kl5_rest.py. Bestehende Dateien anderer Pakete nicht ändern.
- Keine Datenbank, keine Serverfunktionen, kein App-Code, kein Merge nach main. Nur Dateien unter inhalte/.
- Keine Schulbuchaufgaben abschreiben. Lösungen immer vom Programm berechnen lassen.
- Braucht eine Lernkarte eine Zeichnung, die die App nicht kann: nicht erfinden, sondern im Feld "offen" der Datei notieren.
- Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

Am Ende: kurze Liste der fertigen Dateien mit Anzahl Lernkarten/Aufgaben und alle "offen"-Punkte.
```

## Paket Klasse 7 (6 Themen) – Lücken aus dem Vorjahr von Kind B

```text
Du baust Mathe-Lerninhalte für eine Lern-App (Gymnasium Bayern, Klasse 7).
Repository: beinhoff77-stack/ki-system, Ausgangszweig lernen-app. Lege den Zweig inhalte-kl7 an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (Format, Regeln, Verbote, Erfahrungen aus der ersten Runde),
inhalte/vorlage_generator.py (Muster) und die Einträge der unten genannten Themen in inhalte/themenliste.json.
Als Beispiel für ein fertiges Thema: inhalte/generatoren/zahlen_ganz.py mit inhalte/themen/zahlen.ganz.json.

Aufgabe: Baue diese Themen nacheinander in dieser Reihenfolge. Je Thema ein Generator
(inhalte/generatoren/<thema_schluessel>.py), der inhalte/themen/<thema_schluessel>.json schreibt.

 1. bruch.prozent_grundwert – Vermehrter und verminderter Grundwert (thema_id 94, block_id 108)
 2. terme.aufstellen – Terme aufstellen und deuten (thema_id 28, block_id 63)
 3. abbildungen.kongruenz – Kongruenzabbildungen (thema_id 46, block_id 82)
 4. geometrie.konstruktion – Konstruktionen, Kongruenz und Beweise (thema_id 44, block_id 80)
 5. geometrie.kreis – Kreis und Tangenten (thema_id 45, block_id 79)
 6. daten.boxplot – Median, Quartile, Boxplot (thema_id 95, block_id 111)

Regeln:
- Ein Thema ist erst fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet
  und jede Zahl-Aufgabe nachgerechnet ist. Dann Commit + Push auf inhalte-kl7 (ein Thema = ein Commit).
- Eigene Hilfsdatei nur unter dem Namen inhalte/generatoren/_kl7.py. Bestehende Dateien anderer Pakete nicht ändern.
- Keine Datenbank, keine Serverfunktionen, kein App-Code, kein Merge nach main. Nur Dateien unter inhalte/.
- Keine Schulbuchaufgaben abschreiben. Lösungen immer vom Programm berechnen lassen.
- Braucht eine Lernkarte eine Zeichnung, die die App nicht kann: nicht erfinden, sondern im Feld "offen" der Datei notieren.
- Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

Am Ende: kurze Liste der fertigen Dateien mit Anzahl Lernkarten/Aufgaben und alle "offen"-Punkte.
```

## Paket Klasse 10 (7 Themen) – Vorrat

```text
Du baust Mathe-Lerninhalte für eine Lern-App (Gymnasium Bayern, Klasse 10).
Repository: beinhoff77-stack/ki-system, Ausgangszweig lernen-app. Lege den Zweig inhalte-kl10 an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (Format, Regeln, Verbote, Erfahrungen aus der ersten Runde),
inhalte/vorlage_generator.py (Muster) und die Einträge der unten genannten Themen in inhalte/themenliste.json.
Als Beispiel für ein fertiges Thema: inhalte/generatoren/zahlen_ganz.py mit inhalte/themen/zahlen.ganz.json.

Aufgabe: Baue diese Themen nacheinander in dieser Reihenfolge. Je Thema ein Generator
(inhalte/generatoren/<thema_schluessel>.py), der inhalte/themen/<thema_schluessel>.json schreibt.

 1. gleichungen.exponential – Exponentialgleichungen (thema_id 10, block_id 56)
 2. gleichungen.polynom – Polynomgleichungen (thema_id 11, block_id 56)
 3. funktionen.exponential_log – Exponential- und Logarithmusfunktionen (thema_id 37, block_id 68)
 4. funktionen.trig – Sinus- und Kosinusfunktion (thema_id 38, block_id 67)
 5. funktionen.ganzrational – Ganzrationale Funktionen (thema_id 39, block_id 66)
 6. raum.pyramide_kegel_kugel – Pyramide, Kegel, Kugel (thema_id 92, block_id 110)
 7. stochastik.mehrstufig – Mehrstufige Zufallsexperimente (thema_id 62, block_id 90)

Regeln:
- Ein Thema ist erst fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet
  und jede Zahl-Aufgabe nachgerechnet ist. Dann Commit + Push auf inhalte-kl10 (ein Thema = ein Commit).
- Eigene Hilfsdatei nur unter dem Namen inhalte/generatoren/_kl10.py. Bestehende Dateien anderer Pakete nicht ändern.
- Keine Datenbank, keine Serverfunktionen, kein App-Code, kein Merge nach main. Nur Dateien unter inhalte/.
- Keine Schulbuchaufgaben abschreiben. Lösungen immer vom Programm berechnen lassen.
- Braucht eine Lernkarte eine Zeichnung, die die App nicht kann: nicht erfinden, sondern im Feld "offen" der Datei notieren.
- Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

Am Ende: kurze Liste der fertigen Dateien mit Anzahl Lernkarten/Aufgaben und alle "offen"-Punkte.
```


---

# Dritte Runde: Prüfergebnisse einarbeiten und Zeichnungen nachrüsten

Erst starten, wenn die Prüfer-Chats für die Themen des Pakets fertig sind (Dateien unter `inhalte/pruefung/erklaerungen/` und `inhalte/pruefung/aufgaben/` auf den Zweigen `pruefung-erklaerungen` und `pruefung-aufgaben`).

Grundsatz: Der **Generator** bleibt die einzige Quelle. Nie die Datei unter `inhalte/themen/` von Hand ändern – immer den Generator ändern und neu laufen lassen.

## Einarbeiten Klasse 5 (11 Themen)

```text
Du überarbeitest Mathe-Lerninhalte einer Lern-App (Gymnasium Bayern, Klasse 5) nach einer Prüfung.
Repository: beinhoff77-stack/ki-system. Hole den aktuellen Stand von lernen-app, lege davon den Zweig einarbeiten-kl5 an und führe die Zweige
origin/pruefung-erklaerungen und origin/pruefung-aufgaben hinein (sie enthalten nur Dateien unter inhalte/pruefung/).

Lies vollständig: inhalte/README.md (besonders „Erfahrungen“ und „Zeichnungen“) und inhalte/pruefung/README.md (Format der Prüfergebnisse).

Themen dieses Pakets: geometrie.grundbegriffe, geometrie.ortslinien, geometrie.winkel, groessen.einheiten, groessen.proportional, messen.flaechen, messen.koerper_berechnung, stochastik.kombinatorik, zahlen.ganz, zahlen.potenzen_basis, zahlen.rechengesetze

Für jedes Thema, zu dem Prüfdateien vorliegen (inhalte/pruefung/erklaerungen/<thema>.json und inhalte/pruefung/aufgaben/<thema>.json):
1. Erklärungen: Jedes Feld unter karten[].neu wörtlich in die Lernkarte des Generators übernehmen (es ersetzt das alte Feld vollständig).
   neue_karten als vollständige Lernkarte einbauen – mit eigenem Aufgaben-Generator und allen Pools wie bei jeder Karte.
2. Aufgaben: Jeden Eintrag unter fehler beheben (im Generator, sodass der Fehler in keiner Variante mehr vorkommt).
   Jede generator_regel umsetzen. Jeden fehlenden Aufgabentyp aus fehlende_aufgabentypen einbauen und auf die Stufen verteilen;
   Stufe 3 soll ein anderer Gedanke sein, nicht nur größere Zahlen.
3. Zeichnungen nachrüsten: Wo die Prüfung ein bild vorschlägt oder das Feld offen der Themen-Datei eine fehlende Zeichnung nennt,
   die die App inzwischen kann (Koordinatensystem mit Graphen, Figur, Säulen-/Kreisdiagramm, Tabelle, Boxplot, Baumdiagramm),
   Bilder in Lernkarten (bild) und Aufgaben (f.grafik) einbauen. Erledigte Punkte aus offen streichen.
4. Brüche, Zahlenpaare, Punkte als Antwort: als luecken (□/□, x = □; y = □, S(□ | □)) statt Auswahl, wo das die bessere Aufgabe ist.
5. Gerundete Ergebnisse: toleranz in o setzen (eine Einheit der letzten verlangten Stelle).
6. Bist du mit einem Prüfpunkt fachlich nicht einverstanden: nicht umsetzen, sondern unter offen begründen.
7. Generator laufen lassen, `python3 -I tools/inhalt_pruefen.py inhalte/themen/<thema>.json` muss OK melden. Mindestens 10 Aufgaben je Lernkarte selbst lesen.
   Ein Thema = ein Commit, Push auf einarbeiten-kl5. In die Commit-Nachricht: wie viele Prüfpunkte umgesetzt, wie viele abgelehnt.

Themen ohne Prüfdateien überspringen und am Ende nennen.

Verboten: Dateien unter inhalte/pruefung/ ändern, Datenbank, Serverfunktionen, App-Code, Tests, Merge nach main.
Arbeite ohne Rückfragen durch. Am Ende: je Thema umgesetzte/abgelehnte Punkte, neue Lernkarten, Zahl der Bilder, verbleibende offen-Punkte.
```

## Einarbeiten Klasse 8 (14 Themen)

```text
Du überarbeitest Mathe-Lerninhalte einer Lern-App (Gymnasium Bayern, Klasse 8) nach einer Prüfung.
Repository: beinhoff77-stack/ki-system. Hole den aktuellen Stand von lernen-app, lege davon den Zweig einarbeiten-kl8 an und führe die Zweige
origin/pruefung-erklaerungen und origin/pruefung-aufgaben hinein (sie enthalten nur Dateien unter inhalte/pruefung/).

Lies vollständig: inhalte/README.md (besonders „Erfahrungen“ und „Zeichnungen“) und inhalte/pruefung/README.md (Format der Prüfergebnisse).

Themen dieses Pakets: funktionen.gebrochen, funktionen.grundbegriffe, funktionen.linear, gleichungen.bruch, gleichungen.formeln, gleichungen.lgs2, gleichungen.ungleichungen, messen.koerper_darstellung, messen.kreisberechnung, raum.schraegbilder, stochastik.grundbegriffe, stochastik.simulation, terme.bruchterme, zahlen.intervalle

Für jedes Thema, zu dem Prüfdateien vorliegen (inhalte/pruefung/erklaerungen/<thema>.json und inhalte/pruefung/aufgaben/<thema>.json):
1. Erklärungen: Jedes Feld unter karten[].neu wörtlich in die Lernkarte des Generators übernehmen (es ersetzt das alte Feld vollständig).
   neue_karten als vollständige Lernkarte einbauen – mit eigenem Aufgaben-Generator und allen Pools wie bei jeder Karte.
2. Aufgaben: Jeden Eintrag unter fehler beheben (im Generator, sodass der Fehler in keiner Variante mehr vorkommt).
   Jede generator_regel umsetzen. Jeden fehlenden Aufgabentyp aus fehlende_aufgabentypen einbauen und auf die Stufen verteilen;
   Stufe 3 soll ein anderer Gedanke sein, nicht nur größere Zahlen.
3. Zeichnungen nachrüsten: Wo die Prüfung ein bild vorschlägt oder das Feld offen der Themen-Datei eine fehlende Zeichnung nennt,
   die die App inzwischen kann (Koordinatensystem mit Graphen, Figur, Säulen-/Kreisdiagramm, Tabelle, Boxplot, Baumdiagramm),
   Bilder in Lernkarten (bild) und Aufgaben (f.grafik) einbauen. Erledigte Punkte aus offen streichen.
4. Brüche, Zahlenpaare, Punkte als Antwort: als luecken (□/□, x = □; y = □, S(□ | □)) statt Auswahl, wo das die bessere Aufgabe ist.
5. Gerundete Ergebnisse: toleranz in o setzen (eine Einheit der letzten verlangten Stelle).
6. Bist du mit einem Prüfpunkt fachlich nicht einverstanden: nicht umsetzen, sondern unter offen begründen.
7. Generator laufen lassen, `python3 -I tools/inhalt_pruefen.py inhalte/themen/<thema>.json` muss OK melden. Mindestens 10 Aufgaben je Lernkarte selbst lesen.
   Ein Thema = ein Commit, Push auf einarbeiten-kl8. In die Commit-Nachricht: wie viele Prüfpunkte umgesetzt, wie viele abgelehnt.

Themen ohne Prüfdateien überspringen und am Ende nennen.

Verboten: Dateien unter inhalte/pruefung/ ändern, Datenbank, Serverfunktionen, App-Code, Tests, Merge nach main.
Arbeite ohne Rückfragen durch. Am Ende: je Thema umgesetzte/abgelehnte Punkte, neue Lernkarten, Zahl der Bilder, verbleibende offen-Punkte.
```

## Einarbeiten Klasse 6 (8 Themen)

```text
Du überarbeitest Mathe-Lerninhalte einer Lern-App (Gymnasium Bayern, Klasse 6) nach einer Prüfung.
Repository: beinhoff77-stack/ki-system. Hole den aktuellen Stand von lernen-app, lege davon den Zweig einarbeiten-kl6 an und führe die Zweige
origin/pruefung-erklaerungen und origin/pruefung-aufgaben hinein (sie enthalten nur Dateien unter inhalte/pruefung/).

Lies vollständig: inhalte/README.md (besonders „Erfahrungen“ und „Zeichnungen“) und inhalte/pruefung/README.md (Format der Prüfergebnisse).

Themen dieses Pakets: bruch.brueche, bruch.dezimal, bruch.prozent, bruch.rechnen, daten.darstellen, daten.kennwerte, terme.potenzgesetze, zahlen.potenzen_zehner

Für jedes Thema, zu dem Prüfdateien vorliegen (inhalte/pruefung/erklaerungen/<thema>.json und inhalte/pruefung/aufgaben/<thema>.json):
1. Erklärungen: Jedes Feld unter karten[].neu wörtlich in die Lernkarte des Generators übernehmen (es ersetzt das alte Feld vollständig).
   neue_karten als vollständige Lernkarte einbauen – mit eigenem Aufgaben-Generator und allen Pools wie bei jeder Karte.
2. Aufgaben: Jeden Eintrag unter fehler beheben (im Generator, sodass der Fehler in keiner Variante mehr vorkommt).
   Jede generator_regel umsetzen. Jeden fehlenden Aufgabentyp aus fehlende_aufgabentypen einbauen und auf die Stufen verteilen;
   Stufe 3 soll ein anderer Gedanke sein, nicht nur größere Zahlen.
3. Zeichnungen nachrüsten: Wo die Prüfung ein bild vorschlägt oder das Feld offen der Themen-Datei eine fehlende Zeichnung nennt,
   die die App inzwischen kann (Koordinatensystem mit Graphen, Figur, Säulen-/Kreisdiagramm, Tabelle, Boxplot, Baumdiagramm),
   Bilder in Lernkarten (bild) und Aufgaben (f.grafik) einbauen. Erledigte Punkte aus offen streichen.
4. Brüche, Zahlenpaare, Punkte als Antwort: als luecken (□/□, x = □; y = □, S(□ | □)) statt Auswahl, wo das die bessere Aufgabe ist.
5. Gerundete Ergebnisse: toleranz in o setzen (eine Einheit der letzten verlangten Stelle).
6. Bist du mit einem Prüfpunkt fachlich nicht einverstanden: nicht umsetzen, sondern unter offen begründen.
7. Generator laufen lassen, `python3 -I tools/inhalt_pruefen.py inhalte/themen/<thema>.json` muss OK melden. Mindestens 10 Aufgaben je Lernkarte selbst lesen.
   Ein Thema = ein Commit, Push auf einarbeiten-kl6. In die Commit-Nachricht: wie viele Prüfpunkte umgesetzt, wie viele abgelehnt.

Themen ohne Prüfdateien überspringen und am Ende nennen.

Verboten: Dateien unter inhalte/pruefung/ ändern, Datenbank, Serverfunktionen, App-Code, Tests, Merge nach main.
Arbeite ohne Rückfragen durch. Am Ende: je Thema umgesetzte/abgelehnte Punkte, neue Lernkarten, Zahl der Bilder, verbleibende offen-Punkte.
```

## Einarbeiten Klasse 9 (14 Themen)

```text
Du überarbeitest Mathe-Lerninhalte einer Lern-App (Gymnasium Bayern, Klasse 9) nach einer Prüfung.
Repository: beinhoff77-stack/ki-system. Hole den aktuellen Stand von lernen-app, lege davon den Zweig einarbeiten-kl9 an und führe die Zweige
origin/pruefung-erklaerungen und origin/pruefung-aufgaben hinein (sie enthalten nur Dateien unter inhalte/pruefung/).

Lies vollständig: inhalte/README.md (besonders „Erfahrungen“ und „Zeichnungen“) und inhalte/pruefung/README.md (Format der Prüfergebnisse).

Themen dieses Pakets: abbildungen.aehnlichkeit, funktionen.potenz, funktionen.quadratisch, gleichungen.lgs3, gleichungen.potenz, gleichungen.quadratisch, gleichungen.trig, stochastik.verknuepft, trigo.allgemein, trigo.pythagoras, trigo.rechtwinklig, zahlen.rationale_exponenten, zahlen.reell, zahlen.wurzeln_basis

Für jedes Thema, zu dem Prüfdateien vorliegen (inhalte/pruefung/erklaerungen/<thema>.json und inhalte/pruefung/aufgaben/<thema>.json):
1. Erklärungen: Jedes Feld unter karten[].neu wörtlich in die Lernkarte des Generators übernehmen (es ersetzt das alte Feld vollständig).
   neue_karten als vollständige Lernkarte einbauen – mit eigenem Aufgaben-Generator und allen Pools wie bei jeder Karte.
2. Aufgaben: Jeden Eintrag unter fehler beheben (im Generator, sodass der Fehler in keiner Variante mehr vorkommt).
   Jede generator_regel umsetzen. Jeden fehlenden Aufgabentyp aus fehlende_aufgabentypen einbauen und auf die Stufen verteilen;
   Stufe 3 soll ein anderer Gedanke sein, nicht nur größere Zahlen.
3. Zeichnungen nachrüsten: Wo die Prüfung ein bild vorschlägt oder das Feld offen der Themen-Datei eine fehlende Zeichnung nennt,
   die die App inzwischen kann (Koordinatensystem mit Graphen, Figur, Säulen-/Kreisdiagramm, Tabelle, Boxplot, Baumdiagramm),
   Bilder in Lernkarten (bild) und Aufgaben (f.grafik) einbauen. Erledigte Punkte aus offen streichen.
4. Brüche, Zahlenpaare, Punkte als Antwort: als luecken (□/□, x = □; y = □, S(□ | □)) statt Auswahl, wo das die bessere Aufgabe ist.
5. Gerundete Ergebnisse: toleranz in o setzen (eine Einheit der letzten verlangten Stelle).
6. Bist du mit einem Prüfpunkt fachlich nicht einverstanden: nicht umsetzen, sondern unter offen begründen.
7. Generator laufen lassen, `python3 -I tools/inhalt_pruefen.py inhalte/themen/<thema>.json` muss OK melden. Mindestens 10 Aufgaben je Lernkarte selbst lesen.
   Ein Thema = ein Commit, Push auf einarbeiten-kl9. In die Commit-Nachricht: wie viele Prüfpunkte umgesetzt, wie viele abgelehnt.

Themen ohne Prüfdateien überspringen und am Ende nennen.

Verboten: Dateien unter inhalte/pruefung/ ändern, Datenbank, Serverfunktionen, App-Code, Tests, Merge nach main.
Arbeite ohne Rückfragen durch. Am Ende: je Thema umgesetzte/abgelehnte Punkte, neue Lernkarten, Zahl der Bilder, verbleibende offen-Punkte.
```

## Einarbeiten Klasse 7 (6 Themen)

```text
Du überarbeitest Mathe-Lerninhalte einer Lern-App (Gymnasium Bayern, Klasse 7) nach einer Prüfung.
Repository: beinhoff77-stack/ki-system. Hole den aktuellen Stand von lernen-app, lege davon den Zweig einarbeiten-kl7 an und führe die Zweige
origin/pruefung-erklaerungen und origin/pruefung-aufgaben hinein (sie enthalten nur Dateien unter inhalte/pruefung/).

Lies vollständig: inhalte/README.md (besonders „Erfahrungen“ und „Zeichnungen“) und inhalte/pruefung/README.md (Format der Prüfergebnisse).

Themen dieses Pakets: abbildungen.kongruenz, bruch.prozent_grundwert, daten.boxplot, geometrie.konstruktion, geometrie.kreis, terme.aufstellen

Für jedes Thema, zu dem Prüfdateien vorliegen (inhalte/pruefung/erklaerungen/<thema>.json und inhalte/pruefung/aufgaben/<thema>.json):
1. Erklärungen: Jedes Feld unter karten[].neu wörtlich in die Lernkarte des Generators übernehmen (es ersetzt das alte Feld vollständig).
   neue_karten als vollständige Lernkarte einbauen – mit eigenem Aufgaben-Generator und allen Pools wie bei jeder Karte.
2. Aufgaben: Jeden Eintrag unter fehler beheben (im Generator, sodass der Fehler in keiner Variante mehr vorkommt).
   Jede generator_regel umsetzen. Jeden fehlenden Aufgabentyp aus fehlende_aufgabentypen einbauen und auf die Stufen verteilen;
   Stufe 3 soll ein anderer Gedanke sein, nicht nur größere Zahlen.
3. Zeichnungen nachrüsten: Wo die Prüfung ein bild vorschlägt oder das Feld offen der Themen-Datei eine fehlende Zeichnung nennt,
   die die App inzwischen kann (Koordinatensystem mit Graphen, Figur, Säulen-/Kreisdiagramm, Tabelle, Boxplot, Baumdiagramm),
   Bilder in Lernkarten (bild) und Aufgaben (f.grafik) einbauen. Erledigte Punkte aus offen streichen.
4. Brüche, Zahlenpaare, Punkte als Antwort: als luecken (□/□, x = □; y = □, S(□ | □)) statt Auswahl, wo das die bessere Aufgabe ist.
5. Gerundete Ergebnisse: toleranz in o setzen (eine Einheit der letzten verlangten Stelle).
6. Bist du mit einem Prüfpunkt fachlich nicht einverstanden: nicht umsetzen, sondern unter offen begründen.
7. Generator laufen lassen, `python3 -I tools/inhalt_pruefen.py inhalte/themen/<thema>.json` muss OK melden. Mindestens 10 Aufgaben je Lernkarte selbst lesen.
   Ein Thema = ein Commit, Push auf einarbeiten-kl7. In die Commit-Nachricht: wie viele Prüfpunkte umgesetzt, wie viele abgelehnt.

Themen ohne Prüfdateien überspringen und am Ende nennen.

Verboten: Dateien unter inhalte/pruefung/ ändern, Datenbank, Serverfunktionen, App-Code, Tests, Merge nach main.
Arbeite ohne Rückfragen durch. Am Ende: je Thema umgesetzte/abgelehnte Punkte, neue Lernkarten, Zahl der Bilder, verbleibende offen-Punkte.
```

## Einarbeiten Klasse 10 (7 Themen)

```text
Du überarbeitest Mathe-Lerninhalte einer Lern-App (Gymnasium Bayern, Klasse 10) nach einer Prüfung.
Repository: beinhoff77-stack/ki-system. Hole den aktuellen Stand von lernen-app, lege davon den Zweig einarbeiten-kl10 an und führe die Zweige
origin/pruefung-erklaerungen und origin/pruefung-aufgaben hinein (sie enthalten nur Dateien unter inhalte/pruefung/).

Lies vollständig: inhalte/README.md (besonders „Erfahrungen“ und „Zeichnungen“) und inhalte/pruefung/README.md (Format der Prüfergebnisse).

Themen dieses Pakets: funktionen.exponential_log, funktionen.ganzrational, funktionen.trig, gleichungen.exponential, gleichungen.polynom, raum.pyramide_kegel_kugel, stochastik.mehrstufig

Für jedes Thema, zu dem Prüfdateien vorliegen (inhalte/pruefung/erklaerungen/<thema>.json und inhalte/pruefung/aufgaben/<thema>.json):
1. Erklärungen: Jedes Feld unter karten[].neu wörtlich in die Lernkarte des Generators übernehmen (es ersetzt das alte Feld vollständig).
   neue_karten als vollständige Lernkarte einbauen – mit eigenem Aufgaben-Generator und allen Pools wie bei jeder Karte.
2. Aufgaben: Jeden Eintrag unter fehler beheben (im Generator, sodass der Fehler in keiner Variante mehr vorkommt).
   Jede generator_regel umsetzen. Jeden fehlenden Aufgabentyp aus fehlende_aufgabentypen einbauen und auf die Stufen verteilen;
   Stufe 3 soll ein anderer Gedanke sein, nicht nur größere Zahlen.
3. Zeichnungen nachrüsten: Wo die Prüfung ein bild vorschlägt oder das Feld offen der Themen-Datei eine fehlende Zeichnung nennt,
   die die App inzwischen kann (Koordinatensystem mit Graphen, Figur, Säulen-/Kreisdiagramm, Tabelle, Boxplot, Baumdiagramm),
   Bilder in Lernkarten (bild) und Aufgaben (f.grafik) einbauen. Erledigte Punkte aus offen streichen.
4. Brüche, Zahlenpaare, Punkte als Antwort: als luecken (□/□, x = □; y = □, S(□ | □)) statt Auswahl, wo das die bessere Aufgabe ist.
5. Gerundete Ergebnisse: toleranz in o setzen (eine Einheit der letzten verlangten Stelle).
6. Bist du mit einem Prüfpunkt fachlich nicht einverstanden: nicht umsetzen, sondern unter offen begründen.
7. Generator laufen lassen, `python3 -I tools/inhalt_pruefen.py inhalte/themen/<thema>.json` muss OK melden. Mindestens 10 Aufgaben je Lernkarte selbst lesen.
   Ein Thema = ein Commit, Push auf einarbeiten-kl10. In die Commit-Nachricht: wie viele Prüfpunkte umgesetzt, wie viele abgelehnt.

Themen ohne Prüfdateien überspringen und am Ende nennen.

Verboten: Dateien unter inhalte/pruefung/ ändern, Datenbank, Serverfunktionen, App-Code, Tests, Merge nach main.
Arbeite ohne Rückfragen durch. Am Ende: je Thema umgesetzte/abgelehnte Punkte, neue Lernkarten, Zahl der Bilder, verbleibende offen-Punkte.
```

