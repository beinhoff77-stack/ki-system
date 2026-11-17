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
- Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

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
- Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

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
- Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

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
- Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

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
- Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

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
- Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

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
- Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
Arbeite ohne Rückfragen durch. Triff bei Unklarheit die fachlich naheliegende Entscheidung und notiere sie unter "offen".

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
Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
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
Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
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
Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
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
Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
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
Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
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
Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/<zweig>.md ablegen und pushen.
Arbeite ohne Rückfragen durch. Am Ende: je Thema umgesetzte/abgelehnte Punkte, neue Lernkarten, Zahl der Bilder, verbleibende offen-Punkte.
```



---

# Vierte Runde: Themen nur für Realschule und IB

Alle Gymnasium-Themen (Klasse 5–10) sind gebaut. Diese 24 Themen kommen nur in der bayerischen Realschule, im IB MYP oder in keinem der drei Lehrpläne vor.

## Paket Realschule (10 Themen)

```text
Du baust Mathe-Lerninhalte für eine Lern-App. Diese Themen stehen nicht im Lehrplan des bayerischen Gymnasiums, sondern im LehrplanPLUS der bayerischen Realschule (Wahlpflichtfächergruppe I).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig inhalte-rs an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (Format, Regeln, „Erfahrungen“, „Zeichnungen“), inhalte/postfach/README.md (Meldungen),
inhalte/vorlage_generator.py und die Einträge der unten genannten Themen in inhalte/themenliste.json (Felder klasse, umfang, lehrplan_andere).
Als Beispiel für ein fertig geprüftes Thema: inhalte/generatoren/zahlen_ganz.py mit inhalte/themen/zahlen.ganz.json.

Aufgabe: Baue diese Themen nacheinander. Je Thema ein Generator (inhalte/generatoren/<thema_schluessel>.py), der inhalte/themen/<thema_schluessel>.json schreibt.
Niveau und Sprache: Realschule der angegebenen Klasse – anschaulich, kleinschrittig, viele Rechenbeispiele. In das Feld klasse der Datei genau die Angabe aus themenliste.json übernehmen (kein gym_by).

 1. abbildungen.determinanten2 – Zweireihige Determinanten (thema_id 74, block_id 75, rs_by 7)
 2. abbildungen.vektoren – Vektoren und Determinanten (thema_id 48, block_id 75, rs_by 7)
 3. daten.stichproben – Stichproben und Aussagekraft (thema_id 81, block_id 93, rs_by 7)
 4. funktionen.scharen – Parameter und Funktionenscharen (thema_id 78, block_id 72, rs_by 8)
 5. terme.quadratische_extreme – Quadratische Terme und Extremwerte (thema_id 97, block_id 112, rs_by 8)
 6. funktionen.transformation – Graphentransformation (thema_id 40, block_id 70, rs_by 9)
 7. gleichungen.reinquadratisch – Reinquadratische Gleichungen (thema_id 12, block_id 58, rs_by 9)
 8. gleichungen.wurzel – Wurzelgleichungen (thema_id 13, block_id 57, rs_by 9)
 9. abbildungen.matrizen – Matrizen und Abbildungen mit Matrizen (thema_id 49, block_id 74, rs_by 10, ib_myp 4)
10. funktionen.umkehr – Umkehrfunktionen (thema_id 77, block_id 68, rs_by 10, ib_myp 4)

Regeln:
- Gleich die Qualität der geprüften Themen liefern: Anschauungsmodell und Alltagsbeispiel in jeder Erklärung, typischer Fehler mit Zahlen,
  Stufe 3 als anderer Gedanke (Fehler finden, Umkehraufgabe, Sachaufgabe), falsche Antworten aus typischen Denkfehlern, Bilder wo sie helfen.
- Ein Thema ist erst fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet und jede Zahl-Aufgabe nachgerechnet ist.
  Mindestens 10 Aufgaben je Lernkarte selbst lesen. Dann Commit + Push auf inhalte-rs (ein Thema = ein Commit).
- Eigene Hilfsdatei nur als inhalte/generatoren/_rs.py. Bestehende Dateien anderer Pakete nicht ändern.
- Keine Datenbank, keine Serverfunktionen, kein App-Code, kein Merge nach main. Keine Schulbuchaufgaben abschreiben.
- Ist der Umfang eines Themas unklar (leeres Lehrplan-Feld): den üblichen Schulstoff dieser Stufe bauen und die Annahme unter "offen" notieren.
- Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/inhalte-rs.md ablegen und pushen.
Arbeite ohne Rückfragen durch.
```

## Paket IB (14 Themen)

```text
Du baust Mathe-Lerninhalte für eine Lern-App. Diese Themen stehen nicht im Lehrplan des bayerischen Gymnasiums, sondern im IB Middle Years Programme (MYP) bzw. in keinem der drei Lehrpläne (Zusatzstoff).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig inhalte-ib an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (Format, Regeln, „Erfahrungen“, „Zeichnungen“), inhalte/postfach/README.md (Meldungen),
inhalte/vorlage_generator.py und die Einträge der unten genannten Themen in inhalte/themenliste.json (Felder klasse, umfang, lehrplan_andere).
Als Beispiel für ein fertig geprüftes Thema: inhalte/generatoren/zahlen_ganz.py mit inhalte/themen/zahlen.ganz.json.

Aufgabe: Baue diese Themen nacheinander. Je Thema ein Generator (inhalte/generatoren/<thema_schluessel>.py), der inhalte/themen/<thema_schluessel>.json schreibt.
Niveau und Sprache: IB MYP des angegebenen Jahres (MYP 1 ≈ Klasse 6, MYP 4 ≈ Klasse 9); Themen ohne Zuordnung auf dem Niveau Klasse 9/10. Deutsch, Fachbegriffe beim ersten Auftreten zusätzlich auf Englisch in Klammern. In das Feld klasse der Datei genau die Angabe aus themenliste.json übernehmen (kein gym_by).

 1. mengen.grundbegriffe – Mengen und Venn-Diagramme (thema_id 83, block_id 99, ib_myp 1)
 2. groessen.verhaeltnisse – Verhältnisse und Raten (thema_id 27, block_id 51, ib_myp 2)
 3. daten.zweidimensional – Zweidimensionale Daten (thema_id 59, block_id 89, ib_myp 3)
 4. daten.standardabweichung – Standardabweichung (thema_id 79, block_id 88, ib_myp 4)
 5. stochastik.bedingt – Bedingte Wahrscheinlichkeit (thema_id 82, block_id 88, ib_myp 4)
 6. funktionen.betrag – Betragsfunktion (thema_id 75, block_id 65, ib_myp 4)
 7. funktionen.folgen – Folgen (thema_id 41, block_id 65, ib_myp 4)
 8. funktionen.reihen – Reihen (thema_id 76, block_id 65, ib_myp 4)
 9. sonder.graphentheorie – Graphentheorie (thema_id 65, block_id 98, ib_myp 4)
10. sonder.optimierung – Lineare Optimierung (thema_id 66, block_id 98, ib_myp 4)
11. daten.normalverteilung – Normalverteilung (thema_id 80, block_id 88, ohne Lehrplan-Zuordnung)
12. finanzen.zinseszins – Zinseszins (thema_id 72, block_id 50, ohne Lehrplan-Zuordnung)
13. sonder.logik – Aussagenlogik (thema_id 84, block_id 97, ohne Lehrplan-Zuordnung)
14. zahlen.schranken – Schranken und Genauigkeit (thema_id 70, block_id 97, ohne Lehrplan-Zuordnung)

Regeln:
- Gleich die Qualität der geprüften Themen liefern: Anschauungsmodell und Alltagsbeispiel in jeder Erklärung, typischer Fehler mit Zahlen,
  Stufe 3 als anderer Gedanke (Fehler finden, Umkehraufgabe, Sachaufgabe), falsche Antworten aus typischen Denkfehlern, Bilder wo sie helfen.
- Ein Thema ist erst fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet und jede Zahl-Aufgabe nachgerechnet ist.
  Mindestens 10 Aufgaben je Lernkarte selbst lesen. Dann Commit + Push auf inhalte-ib (ein Thema = ein Commit).
- Eigene Hilfsdatei nur als inhalte/generatoren/_ib.py. Bestehende Dateien anderer Pakete nicht ändern.
- Keine Datenbank, keine Serverfunktionen, kein App-Code, kein Merge nach main. Keine Schulbuchaufgaben abschreiben.
- Ist der Umfang eines Themas unklar (leeres Lehrplan-Feld): den üblichen Schulstoff dieser Stufe bauen und die Annahme unter "offen" notieren.
- Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/inhalte-ib.md ablegen und pushen.
Arbeite ohne Rückfragen durch.
```


---

# Fünfte Runde: Nachbau der drei alten Entwürfe (3 Themen)

Diese drei Themen entstanden vor dem Bausatz (nur in der Datenbank, 12 Aufgaben je Lernkarte, kaum typische Fehler, keine Bilder). Sie werden nach dem Bausatz neu gebaut.

```text
Du baust Mathe-Lerninhalte für eine Lern-App (bayerisches Gymnasium).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig inhalte-nachbau an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (Format, Regeln, „Erfahrungen“, „Zeichnungen“), inhalte/postfach/README.md (Meldungen),
inhalte/vorlage_generator.py, inhalte/pruefung/README.md (worauf die Prüfer achten) und die Einträge der drei Themen in inhalte/themenliste.json.
Als Beispiele für fertig geprüfte und eingearbeitete Themen: inhalte/generatoren/zahlen_ganz.py mit inhalte/themen/zahlen.ganz.json
sowie ein Thema der passenden Klasse aus inhalte/themen/ (z. B. terme.umformen.json, gleichungen.ungleichungen.json).

Aufgabe: Baue diese drei Themen nacheinander neu. Je Thema ein Generator (inhalte/generatoren/<thema_schluessel mit _ statt .>.py), der inhalte/themen/<thema_schluessel>.json schreibt.
 1. gleichungen.einfach – Einfache Gleichungen (thema_id 1, block_id 64, Gymnasium Klasse 5): Waage-Modell, Umkehraufgabe, Probe, Textaufgaben als Gleichung, Gleichungen ohne Lösung in ℕ als Vertiefung.
 2. groessen.indirekt – Indirekte Proportionalität (thema_id 93, block_id 107, Gymnasium Klasse 8): erkennen, Produktgleichheit, Dreisatz, Hyperbel-Graph, Abgrenzung zu direkt proportional und zu „weder noch“.
 3. gleichungen.linear – Lineare Gleichungen (thema_id 2, block_id 61, Gymnasium Klasse 7): Äquivalenzumformungen mit Waage, Klammern, Variable auf beiden Seiten, Probe, Sonderfälle (keine/unendlich viele Lösungen), Sachaufgaben.

Regeln:
- Gleich die Qualität der eingearbeiteten Themen liefern: Anschauungsmodell und Alltagsbeispiel in jeder Erklärung, typischer Fehler mit Zahlen,
  Stufe 3 als anderer Gedanke (Fehler finden, Umkehraufgabe, Sachaufgabe), falsche Antworten aus typischen Denkfehlern, Bilder wo sie helfen.
- Ein Thema ist erst fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet und jede Zahl-Aufgabe nachgerechnet ist.
  Mindestens 10 Aufgaben je Lernkarte selbst lesen. Dann Commit + Push auf inhalte-nachbau (ein Thema = ein Commit).
- Eigene Hilfsdatei nur als inhalte/generatoren/_nachbau.py. Bestehende Dateien anderer Pakete nicht ändern.
- Keine Datenbank, keine Serverfunktionen, kein App-Code, kein Merge nach main. Keine Schulbuchaufgaben abschreiben.
- Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht) nach inhalte/postfach/README.md in inhalte/postfach/inhalte-nachbau.md ablegen und pushen.
Arbeite ohne Rückfragen durch.
```


---

# Sechste Runde: Lücken laut Lehrplan schließen (Aufbau-Prüfung)

Der Prüfer „Aufbau“ hat je Klasse den Stoff mit dem LehrplanPLUS (Gymnasium Bayern) abgeglichen: inhalte/pruefung/aufbau/klasse<N>.json
(Felder: luecken mit was_fehlt/wohin/dringlichkeit, zu_viel, themen[].hinweise, reihenfolge). Ein Chat je Klasse; N durch 5, 6, 7, 8, 9 oder 10 ersetzen.

Nicht Teil dieser Runde (macht der Haupt-Chat bzw. eine eigene Runde): neue Themen messen.flaechen_vielecke, messen.volumen, geometrie.winkelsaetze,
messen.prisma_zylinder; die Themen gleichungen.einfach, gleichungen.linear, groessen.indirekt (Runde 5). Schon vorhanden und nicht mehr „fehlend“:
zahlen.natuerlich, zahlen.teilbarkeit, terme.umformen.

```text
Du ergänzt Mathe-Lerninhalte einer Lern-App (Gymnasium Bayern, Klasse N) um fehlenden Lehrplan-Stoff.
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig luecken-klN an und arbeite nur dort.

Lies vollständig: inhalte/README.md (Format, „Erfahrungen“, „Zeichnungen“), inhalte/postfach/README.md (Meldungen) und inhalte/pruefung/aufbau/klasseN.json.

Aufgabe: Arbeite die Einträge unter luecken mit dringlichkeit hoch und mittel ab, soweit sie eine neue Lernkarte oder eine Ergänzung in einem
BESTEHENDEN Thema dieser Klasse verlangen (Feld wohin nennt Thema und Stelle). Prüfe zuerst im Generator, ob der Punkt inzwischen erledigt ist.
- Neue Lernkarte = vollständige Lernkarte (lernziel, titel, regel, schritte, probe, fehler, wenn sinnvoll bild) mit eigenem Aufgaben-Generator und
  allen Pools wie jede andere Karte (12 Übung, 1 Test, 3 Korrektur, 6 Sicherung; je Stufe mindestens 3 Übungen), eingehängt in abschnitte,
  teilfaehigkeiten und bewertung (Pflicht oder Vertiefung – begründet entscheiden).
- Ergänzung einer bestehenden Karte: Erklärung erweitern und passende Aufgaben in die Stufen einbauen, ohne bestehende Aufgabentexte zu ändern,
  wenn es nicht nötig ist (bestehende Aufgaben können schon von Kindern bearbeitet sein).
- Hinweise unter themen[].hinweise mit umsetzen, wenn sie eine Lücke betreffen (z. B. Zeichnungen, die die App inzwischen kann: boxplot, baum, figur, koordinaten).
- zu_viel: nichts löschen. Betroffene Lernkarten höchstens von Pflicht auf Vertiefung setzen und das im Postfach melden.
- Einträge, die ein NEUES Thema verlangen oder ein Thema einer anderen Klasse betreffen: nicht bauen, im Abschlussbericht auflisten.
- Niedrige Dringlichkeit nur, wenn sie in einer ohnehin geänderten Karte mit einem Satz oder einer Aufgabengruppe erledigt ist.

Je geändertem Thema: Generator laufen lassen, `python3 -I tools/inhalt_pruefen.py inhalte/themen/<thema>.json` muss OK melden, jede Zahl-Aufgabe nachgerechnet,
mindestens 10 Aufgaben je neuer Lernkarte selbst lesen. Ein Thema = ein Commit, Push auf luecken-klN.
Verboten: Dateien unter inhalte/pruefung/ ändern, Datenbank, Serverfunktionen, App-Code, Tests, Merge nach main. Keine Schulbuchaufgaben abschreiben.
Meldungen (Status nach jedem Thema, Fragen, Blocker, Abschlussbericht mit umgesetzten/nicht umgesetzten Lücken) in inhalte/postfach/luecken-klN.md ablegen und pushen.
Arbeite ohne Rückfragen durch.
```


---

# Siebte Runde: Erklärungen verständlich machen (alle Themen)

Anlass und Maßstab: inhalte/README.md, Abschnitt „Verständliche Erklärungen (Pflicht seit 15.11.)“. Muster: funktionen.grundbegriffe (schon erledigt).
Ein Chat je Klasse; N durch 5, 6, 7, 8, 9 oder 10 ersetzen. Reihenfolge der Dringlichkeit: 8 und 5 zuerst, dann 7 und 6, dann 9 und 10.

```text
Du machst die Erklärungen einer Mathe-Lern-App verständlich (Gymnasium Bayern, Klasse N).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig klar-klN an und arbeite nur dort.

Lies vollständig: inhalte/README.md – vor allem den Abschnitt „Verständliche Erklärungen (Pflicht seit 15.11.)“ – und inhalte/postfach/README.md.
Sieh dir das Muster genau an: inhalte/generatoren/funktionen.grundbegriffe.py (Abschnitt KLAR) und das Ergebnis in inhalte/themen/funktionen.grundbegriffe.json.

Aufgabe: Überarbeite die Lernkarten ALLER Themen der Klasse N (Feld klasse.gym_by in inhalte/themenliste.json; funktionen.grundbegriffe ist fertig).
Je Lernkarte: einstieg und woerter neu schreiben; schritte, regel, fehler und Bildbeschriftung nach dem Maßstab überarbeiten. Technisch wie im Muster:
ein Abschnitt KLAR im Generator des Themas, der die Felder der Lernkarten überschreibt.
- Stell dir beim Schreiben ein Kind vor, das das Thema noch nie gesehen hat, und ein Elternteil ohne Mathe-Erinnerung. Lies jede Karte am Ende laut gedacht durch:
  Kommt ein Wort oder Zeichen vor, das nicht erklärt ist? Dann in woerter aufnehmen oder ersetzen.
- Die Alltagssituation muss wirklich passen und rechnerisch stimmen (Zahlen nachrechnen). Keine erfundenen Sachverhalte, die fachlich schief sind.
- Fachlich darf nichts falsch oder verkürzt-falsch werden. Fachwörter bleiben – sie werden erklärt, nicht weggelassen.
- Aufgaben NICHT ändern: Nach dem Generatorlauf müssen alle Aufgaben wörtlich gleich sein wie vorher (mit einem kleinen Vergleichsskript gegen
  `git show HEAD:inhalte/themen/<thema>.json` prüfen und das Ergebnis im Postfach nennen). Verwendet der Generator Beispieltexte der Karte zum Vermeiden von Dopplungen
  und ändern sich dadurch Aufgaben, dann die alten Beispieltexte für diese Prüfung beibehalten (wie _verbot im Muster).
- `python3 -I tools/inhalt_pruefen.py inhalte/themen/<thema>.json` muss OK melden. Ein Thema = ein Commit, Push auf klar-klN.

Verboten: Datenbank, Serverfunktionen, App-Code, Tests, Dateien unter inhalte/pruefung/, Merge nach main.
Meldungen (Status nach jedem Thema, Fragen, Abschlussbericht) in inhalte/postfach/klar-klN.md ablegen und pushen. Arbeite ohne Rückfragen durch.
```


---

# Runde 7b: Erklärungen verständlich machen – die letzten sechs Themen

Vier Themen liegen nur in der Datenbank (kein Generator): zahlen.natuerlich, zahlen.teilbarkeit, terme.umformen, finanzen.zinsen. Zwei sind nachgebaut, aber noch ohne
einstieg/woerter: gleichungen.einfach, groessen.indirekt. Ein Chat für alle sechs.

```text
Du machst die Erklärungen einer Mathe-Lern-App verständlich (Gymnasium Bayern).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig klar-rest an und arbeite nur dort.

Lies vollständig: inhalte/README.md – vor allem den Abschnitt „Verständliche Erklärungen (Pflicht seit 15.11.)“ –, inhalte/postfach/README.md und inhalte/klar/quelle.md.
Muster für Ton und Tiefe: inhalte/themen/funktionen.grundbegriffe.json, inhalte/themen/zahlen.ganz.json, inhalte/themen/bruch.brueche.json (Felder einstieg, woerter, schritte, regel, fehler).

Teil A – vier Themen ohne Generator (zahlen.natuerlich zuerst, dann terme.umformen, zahlen.teilbarkeit, finanzen.zinsen):
Schreibe je Thema eine Überlagerungs-Datei inhalte/klar/<thema_schluessel>.json in dieser Form:
  {"thema_schluessel": "zahlen.natuerlich", "karten": {"<lernziel>": {"einstieg": "…", "woerter": [["Wort", "Erklärung"], …], "schritte": ["…", …], "regel": "…", "fehler": "…", "probe": "…"}}}
- Für JEDES Lernziel aus inhalte/klar/quelle.md ein Eintrag mit einstieg, woerter, schritte (3–5 ganze Sätze, Ergebnis in ⟦…⟧) und regel. fehler immer (auch wo bisher keiner stand:
  dann einen typischen Fehler mit Zahlen ergänzen). probe nur, wo sie passt. Kein Feld bild (die Bilder bleiben, wie sie sind – Beispielzahlen der Karten mit Bild deshalb beibehalten).
- Zeichen ⟦…⟧ für Hervorhebungen wie in den Mustern. Zahlen deutsch schreiben (Komma, Tausender mit Leerzeichen, Minus als −).
- Prüfe jede Datei mit einem kleinen Skript: gültiges JSON, alle Lernziele aus quelle.md vorhanden und keine zusätzlichen, woerter als Liste aus [Wort, Erklärung],
  3–5 Schritte, einstieg mindestens 60 Zeichen, keine Wörter „einfach/offensichtlich/trivial“ in einstieg und schritte. Alle Zahlen nachrechnen.

Teil B – zwei Themen mit Generator (gleichungen.einfach: inhalte/generatoren/gleichungen_einfach.py; groessen.indirekt: inhalte/generatoren/groessen_indirekt.py):
Wie in „Siebte Runde“: Abschnitt KLAR im Generator, Aufgaben müssen wörtlich gleich bleiben (Vergleich gegen git show HEAD:…), `python3 -I tools/inhalt_pruefen.py` muss OK melden.

Ein Thema = ein Commit, Push auf klar-rest. Verboten: Datenbank, Serverfunktionen, App-Code, Tests, Dateien unter inhalte/pruefung/, Merge nach main.
Meldungen (Status nach jedem Thema, Fragen, Abschlussbericht) in inhalte/postfach/klar-rest.md ablegen und pushen. Arbeite ohne Rückfragen durch.
```


---

# Achte Runde: Umbau der Lernkarten auf das neue Muster (Vorgabe 16.11.)

Grundlage: inhalte/pruefung/erklaerungen/darstellung/umsetzung.md (Sebastians Auswahl). Die App kann das neue Format seit Version 0.73.0
(Übersicht → eine Karte, Bildergeschichte, „Pass auf!“, antippbare Wörter, gestapelte Brüche, neue Zeichnungsarten, Prüfregeln).
Aufgaben bleiben unverändert.

| Paket | Zweig | Klasse | Themen | Hinweis |
|---|---|---|---|---|
| U5 | `umbau-kl5` | 5 | 14 | zuerst (Kind A); Thermometer, Zahlenstrahl mit Bögen, Bruchstreifen |
| U8 | `umbau-kl8` | 8 | 15 | Kind B; meist Koordinatensystem mit Schritt-Zuständen |
| U6 | `umbau-kl6` | 6 | 9 | erst nach dem Test mit den Kindern starten |
| U7 | `umbau-kl7` | 7 | 8 | erst nach dem Test mit den Kindern starten |
| U9 | `umbau-kl9` | 9 | 14 | erst nach dem Test mit den Kindern starten |
| U10 | `umbau-kl10` | 10 | 7 | erst nach dem Test mit den Kindern starten |
| UR | `umbau-rest` | ohne gym_by | 24 | Realschule/IB; zuletzt |

Reihenfolge: U5 → U8 → (Test je einer umgebauten Karte mit beiden Kindern, Sebastian gibt frei) → U6 → U7 → U9 → U10 → UR.

Auftragstext je Paket (`<zweig>` und `<klasse>` ersetzen; bei UR statt „mit "gym_by": <klasse>“: „ohne gym_by“):

```text
Du baust die Lernkarten (Erklärungen) eines Pakets der Lern-App auf das neue Muster um.
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin), Ausgangszweig lernen-app. Lege den Zweig <zweig> an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (besonders „Verständliche Erklärungen“ mit der Vorgabe seit 16.11. und den Längenregeln, sowie „Zeichnungen“),
inhalte/pruefung/erklaerungen/darstellung/umsetzung.md (Abschnitte 1, 3, 4, 5), inhalte/postfach/README.md und als Muster die Karte
zahlen.ganz/betrag in inhalte/pruefung/erklaerungen/darstellung/entwurf.html.

Aufgabe: Für jedes Thema mit "gym_by": <klasse> in inhalte/themenliste.json – dazu die Themen ohne Generator, die zu dieser Klasse gehören
(Klasse 5: zahlen.natuerlich, zahlen.teilbarkeit · Klasse 6: finanzen.zinsen · Klasse 7: terme.umformen) – die Lernkarten so umbauen, dass jede dem Muster entspricht:
einstieg (≤ 35 Wörter), woerter (≤ 3), Kartenbild, schritte als Objekte {text, bild} mit Bild je Bildänderung, fehler + fehler_bild, regel (erster Satz = Kurz gesagt, ≤ 12 Wörter).
- Themen mit Generator: im Generator inhalte/generatoren/<thema>.py ändern (dort gibt es schon einen Abschnitt KLAR bzw. eine Hilfsdatei _klar_*.py, die die Erklärfelder
  nach dem Erzeugen der Aufgaben überlagert – dort weiterarbeiten), nicht von Hand in der JSON-Datei.
- Themen ohne Generator (zahlen.natuerlich, zahlen.teilbarkeit, terme.umformen, finanzen.zinsen): die Überlagerung inhalte/klar/<thema>.json umbauen.
  Dort sind jetzt zusätzlich die Felder bild (ersetzt das Kartenbild), schritte als Objekte und fehler_bild erlaubt. Die bisherigen Kartenbilder stehen in inhalte/klar/quelle.md.

Regeln:
- Aufgaben nicht ändern (Texte wörtlich gleich; Vergleich gegen `git show HEAD:inhalte/themen/<thema>.json` und Ergebnis im Postfach nennen). titel und lernziel nicht ändern.
- Nur Zeichnungsarten aus inhalte/README.md benutzen (neu: zahlenstrahl mit punkte/boegen/bereich, thermometer, bruchstreifen). Fehlt eine: im Feld "offen" notieren, nicht erfinden.
- Ein Thema ist fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` ohne Fehler durchläuft, die Hinweise zu Längen abgearbeitet sind
  (bewusst stehen gelassene Hinweise im Postfach begründen) und du jede Karte einmal laut gelesen hast: Versteht ein Kind der Klasse sie beim ersten Lesen?
- Fachlich darf nichts falsch werden. Alle Zahlen der Situationen nachrechnen. Bild, einstieg und Beispiel erzählen dieselbe Situation.
- Ein Thema = ein Commit + Push auf <zweig>. Status nach jedem Thema in inhalte/postfach/<zweig>.md, am Ende ein Abschlussbericht.
- Keine Datenbank, keine Serverfunktionen, kein App-Code, keine Tests, kein Merge nach main.
Arbeite ohne Rückfragen durch; Unklares unter "offen" notieren.
```

Abnahme je Paket: Der Haupt-Chat prüft (Prüfskript, Aufgaben gleich, Zeichnungen rendern, drei Karten lesen) und spielt die Erklärungen ein.
Danach liest das Kind eine Karte und löst die erste Aufgabe ohne Hilfe.


---

# Neunte Runde: Aufgaben auffüllen – drei Themen mit nur 2 Übungen je Lernkarte

Befund aus dem echten Einsatz (16.11.): In zahlen.teilbarkeit (Athen), terme.umformen (Samarkand) und finanzen.zinsen (New York) gibt es je Lernkarte nur
2 Übungsaufgaben (dazu 1 Test, 3 Korrektur, 6 Sicherung). Eine Karte „sitzt“ erst nach 2 richtigen Antworten hintereinander, und eine richtige Antwort im zweiten
Versuch zählt dafür nicht. Folge: Das Kind bekommt dieselbe Aufgabe sofort noch einmal. Diese drei Themen stammen aus der Zeit vor dem Bausatz und haben keinen Generator.

```text
Du baust Übungsaufgaben für drei bestehende Themen einer Mathe-Lern-App nach (bayerisches Gymnasium).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig aufgaben-auffuellen an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (Format, Regeln, „Erfahrungen“, „Zeichnungen“, „Verständliche Erklärungen“), inhalte/postfach/README.md, inhalte/vorlage_generator.py,
inhalte/klar/quelle.md (dort stehen für die drei Themen alle Lernziele, Titel, bisherigen Beispiele) und die Überlagerungen inhalte/klar/zahlen.teilbarkeit.json,
inhalte/klar/terme.umformen.json, inhalte/klar/finanzen.zinsen.json (das sind die aktuellen, bereits umgebauten Lernkarten dieser Themen).
Als Muster für Generatoren: inhalte/generatoren/gleichungen_einfach.py mit _nachbau.py und inhalte/generatoren/zahlen.ganz.py.

Aufgabe: Je Thema ein Generator inhalte/generatoren/<thema mit _ statt .>.py, der inhalte/themen/<thema_schluessel>.json schreibt:
 1. terme.umformen – Terme umformen (thema_id 29, block_id 62, klasse {"gym_by": 7}) – zuerst, ein Kind arbeitet gerade daran
 2. zahlen.teilbarkeit – Teilbarkeit und Primzahlen (thema_id 17, block_id 48, klasse {"gym_by": 5})
 3. finanzen.zinsen – Einfache Zinsen (thema_id 71, block_id 52, klasse {"gym_by": 6})
- Lernziele (Schlüssel), Reihenfolge und Titel der Lernkarten GENAU wie in inhalte/klar/quelle.md. Die Erklärfelder jeder Lernkarte (einstieg, woerter, bild, schritte, fehler,
  fehler_bild, regel, probe) unverändert aus inhalte/klar/<thema>.json übernehmen (der Generator liest die Datei ein); fehlt dort ein Bild, das Kartenbild aus quelle.md nachbauen.
- Je Lernkarte NEUE Aufgaben mit allen Pools wie im Bausatz: 12 Übungen (je Stufe mindestens 3), 1 Test, 3 Korrektur, 6 Sicherung. Die Aufgaben vom Programm erzeugen,
  jede Lösung berechnen, Zahl-Aufgaben mit Rechenausdruck „c“. Stufe 3 als anderer Gedanke (Fehler finden, Umkehraufgabe, Sachaufgabe). Falsche Antworten aus typischen Denkfehlern.
  Aufgaben zu Termen: Antworttyp luecken mit Term-Vorlage wie in den vorhandenen Themen (z. B. „□x + □“, „□x² + □x + □“) – siehe README und terme.bruchterme/gleichungen.linear als Muster.
- abschnitte, teilfaehigkeiten und bewertung vollständig anlegen (alle Lernkarten Pflicht, außer du begründest eine Vertiefung unter "offen").
- Ein Thema ist fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet, jede Zahl-Aufgabe nachgerechnet ist und du je Lernkarte mindestens 10 Aufgaben gelesen hast.
  Ein Thema = ein Commit + Push auf aufgaben-auffuellen.
- Keine Datenbank, keine Serverfunktionen, kein App-Code, keine Tests, kein Merge nach main. Keine Schulbuchaufgaben abschreiben.
Meldungen (Status nach jedem Thema, Fragen, Abschlussbericht) in inhalte/postfach/aufgaben-auffuellen.md ablegen und pushen. Arbeite ohne Rückfragen durch.
```

Einspielen (Haupt-Chat): mit einheit_abgleichen(…, 'lassen') – die vorhandenen Aufgaben und Lernstände bleiben, die neuen kommen dazu.

# Zehnte Runde: Durchsicht je Jahrgang + schwerere Aufgaben nach Prüfungsvorbild

Befund (16.11.): Rund ein Drittel der Übungen ist Stufe 3, aber 18 Lernkarten haben keine einzige und 7 nur 1–2 Stufe-3-Übungen. Stufe 3 ist bisher gehobenes Schulniveau;
Aufgaben auf dem Niveau echter Prüfungen (Jahrgangsstufentest, Abschlussprüfung, Wettbewerb) fehlen. Ein Chat je Jahrgang, Zweige `schwer-kl5` … `schwer-kl10`.
Im Text unten `<N>` durch die Klasse ersetzen (5, 6, 7, 8, 9 oder 10).

```text
Du prüfst und erweiterst die Aufgaben einer Mathe-Lern-App für Klasse <N> (bayerisches Gymnasium, LehrplanPLUS).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig schwer-kl<N> an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md (Format, Regeln, „Erfahrungen“, „Zeichnungen“, „Verständliche Erklärungen“), inhalte/postfach/README.md, inhalte/vorlage_generator.py.
Deine Themen: alle Einträge in inhalte/themenliste.json mit klasse {"gym_by": <N>}. Zu jedem Thema gibt es inhalte/themen/<thema_schluessel>.json und einen Generator
unter inhalte/generatoren/ (teils mit Hilfsdateien _klar_*.py, _nachbau.py). Themen ohne Generator auslassen und im Postfach nennen.

Teil 1 – Durchsicht (je Thema, vor dem Erweitern):
- Jede Lernkarte und je Lernkarte mindestens 10 vorhandene Aufgaben lesen. Prüfen: Lösung richtig? Aufgabe eindeutig? Passt die Stufe (1 leicht, 2 mittel, 3 schwer)?
  Passen Aufgaben und Erklärung zusammen? Fehlt laut LehrplanPLUS Klasse <N> ein Aufgabentyp, der in Schulaufgaben üblich ist?
- Vorhandene Aufgaben NICHT ändern oder löschen (Lernstände hängen daran). Fehler, falsch eingestufte Aufgaben und Lücken nur als Liste melden (Thema, Lernkarte, Aufgabe, Befund).

Teil 2 – Recherche echter Prüfungsaufgaben (je Thema, mit Websuche):
- Suche frei zugängliche, echte Prüfungs- und Testaufgaben zu genau diesem Thema und dieser Klasse, z. B. bayerische Jahrgangsstufentests / Bayerischer Mathematik-Test (ISB),
  VERA-Vergleichsarbeiten (IQB), Abschlussprüfungen Realschule/Mittlerer Schulabschluss Bayern (für Klasse 9/10), ab Klasse 10 auch einfache Abitur-Grundaufgaben ohne Hilfsmittel,
  Musterschulaufgaben bayerischer Gymnasien, Wettbewerbe (Känguru, Mathematik-Olympiade Schulrunde, Pangea) für Knobelaufgaben.
- Halte je Thema fest: welche Aufgabentypen kommen in Prüfungen wirklich vor, welches Niveau, welche typischen Einkleidungen und Fallen. Quelle mit Adresse notieren.
- WICHTIG (Urheberrecht): Prüfungsaufgaben nie wörtlich oder mit denselben Zahlen übernehmen. Sie sind das Vorbild für Typ, Aufbau und Niveau; Wortlaut, Einkleidung und Zahlen
  sind eigene. Keine Schulbuchaufgaben abschreiben. Findest du zu einem Thema nichts Belastbares, das ehrlich melden statt etwas zu erfinden.

Teil 3 – Neue Aufgaben (je Lernkarte, Pool uebung):
- Mindestens 6 neue Übungen je Lernkarte: 4 der Stufe 3 und 2 der Stufe 2. Danach hat jede Lernkarte mindestens 6 Stufe-3-Übungen.
- Von den neuen Stufe-3-Aufgaben mindestens 2 nach Prüfungsvorbild aus Teil 2 (Typ und Niveau wie dort) und mindestens 1 echte Knobelaufgabe, sofern das Thema es hergibt:
  mehrschrittig, Verknüpfung mit früherem Stoff, Rückwärtsdenken, Begründen/Fehler finden, ungewohnte Einkleidung, Parameter statt Zahl. „Schwer“ heißt anderer Gedanke,
  nicht größere Zahlen oder längere Rechnung.
- Mehrteilige Prüfungsaufgaben in einzelne, je für sich prüfbare Aufgaben zerlegen (gleiche Einkleidung, Teil a/b/c als eigene Aufgaben). Nur die Antworttypen der App verwenden.
- Jede Aufgabe mit Tipp und Lösungsweg wie im Bausatz; Zahl-Aufgaben mit Rechenausdruck „c“; falsche Antworten aus typischen Denkfehlern. Lösungen vom Programm berechnen
  und zusätzlich von Hand nachrechnen.
- Technik: Die neuen Aufgaben im Generator in einem eigenen Abschnitt mit eigenem festen Zufallsstart ergänzen, sodass alle bisherigen Aufgaben unverändert bleiben.
  Per Skript nachweisen: jede Aufgabe der alten Datei (Stand lernen-app) steht unverändert in der neuen Datei. Lernkarten-Texte und Zeichnungen nicht ändern.
- Ein Thema ist fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet, der Unverändert-Nachweis stimmt und du jede neue Aufgabe gelesen hast.
  Ein Thema = ein Commit + Push auf schwer-kl<N>.

Grenzen: Keine Datenbank, keine Serverfunktionen, kein App-Code, keine Tests, kein Merge nach main oder lernen-app. Keine Namen oder Daten von Kindern.
Meldungen in inhalte/postfach/schwer-kl<N>.md ablegen und pushen: Status nach jedem Thema; am Ende ein Abschlussbericht mit (1) Befundliste aus Teil 1,
(2) je Thema den genutzten Prüfungsquellen mit Adresse und den daraus abgeleiteten Aufgabentypen, (3) Zahl der neuen Aufgaben je Lernkarte und Stufe, (4) Themen, zu denen
keine Prüfungsaufgaben zu finden waren. Arbeite ohne Rückfragen durch.
```

Einspielen (Haupt-Chat): Zweige zusammenführen, prüfen, mit einheit_abgleichen(…, 'lassen') einspielen – vorhandene Aufgaben und Lernstände bleiben, neue kommen dazu.
Reihenfolge: Klasse 8 und 5 zuerst (dort arbeiten die Kinder), dann 7, 6, 9, 10.

# Elfte Runde (D1 im Gesamtauftrag Umbau): Klassen-Zuordnung prüfen

Grundlage: `inhalte/pruefung/UMBAU-AUFTRAG.md` im Zweig pruefung-kinderansicht (Phase 1, Spalte Daten) und Befund B8 im Bericht Kinderansicht.
Ergebnis ist nur ein Vorschlag an Sebastian. Geändert wird erst nach seiner Freigabe (D2).

```text
Du prüfst die Klassen-Zuordnung der Themen einer Mathe-Lern-App gegen den bayerischen LehrplanPLUS (Gymnasium, Mathematik).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig daten-klassen an und arbeite nur dort.

Lies zuerst: inhalte/README.md, inhalte/postfach/README.md, inhalte/themenliste.json. Nur lesen (nicht mergen), mit git show:
origin/pruefung-kinderansicht:inhalte/pruefung/UMBAU-AUFTRAG.md, origin/pruefung-kinderansicht:inhalte/pruefung/kinderansicht/bericht.md (Befund B8, Abschnitt 7),
origin/pruefung-kinderansicht:inhalte/pruefung/kinderansicht/orte.json (Orte mit Klasse und ihren Themen).

Teil 1 – 16 Themen ohne Lehrplan-Beleg: In inhalte/themenliste.json haben 16 Einträge eine Klasse gym_by, aber kein Feld lehrplan_gym:
geometrie.winkel, geometrie.ortslinien, zahlen.potenzen_zehner, bruch.dezimal, zahlen.intervalle, funktionen.grundbegriffe, raum.schraegbilder, stochastik.simulation,
zahlen.wurzeln_basis, zahlen.reell, trigo.pythagoras, trigo.rechtwinklig, abbildungen.kongruenz, gleichungen.einfach, gleichungen.linear, groessen.indirekt.
Suche für jedes Thema im LehrplanPLUS Gymnasium Mathematik (lehrplanplus.bayern.de, mit Websuche) den Lernbereich, in dem der Stoff steht, und die Jahrgangsstufe.
Beginne mit geometrie.winkel (Winkelsätze) und geometrie.ortslinien. Wo der Stoff über zwei Jahrgangsstufen verteilt ist, beides nennen und eine Hauptklasse vorschlagen.
Nichts raten: Findest du keinen Beleg, schreibe „kein Beleg gefunden“.

Teil 2 – 13 Orte mit widersprüchlicher Klasse: Laut orte.json weicht bei 13 von 65 Orten die Klasse des Ortes von der Klasse mindestens eines Themas ab
(Beispiele: Cusco Klasse 5 mit „Körper und Netze“ Klasse 8; Timbuktu Klasse 7 mit „Winkel“ Klasse 5; Rom Klasse 5 mit einem Thema der Klasse 6).
Ziel ist „ein Ort = eine Klasse“. Mache je Ort einen Vorschlag: Welche Klasse bekommt der Ort, welche Themen ziehen an welchen anderen (vorhandenen) Ort derselben Klasse
und desselben Gebiets um, und in welcher Reihenfolge laut Lehrplan stehen die Themen im Ort. Neue Orte nur vorschlagen, wenn kein vorhandener passt.

Ergebnis: eine Datei inhalte/pruefung/klassen/vorschlag.md mit zwei Tabellen
 (1) Thema · Klasse heute · Klasse laut LehrplanPLUS · Lernbereich (Kürzel und Titel) · Quelle (Adresse) · Vorschlag (bleibt / ändern auf …)
 (2) Ort · Klasse heute · Themen mit Klasse · Vorschlag (Klasse des Ortes, Umzüge, Reihenfolge)
und einer kurzen Liste der Punkte, die Sebastian entscheiden muss. Einfache Sprache, keine Fachkürzel ohne Erklärung.

Grenzen: In dieser Runde KEINE Änderung an inhalte/themenliste.json, Generatoren, Datenbank, App-Code oder Tests – nur der Vorschlag. Kein Merge.
Meldungen in inhalte/postfach/daten-klassen.md ablegen und pushen. Arbeite ohne Rückfragen durch.
```

# Zwölfte Runde: zahlen.natuerlich (Rom, erster Flug) auffüllen und schwerer machen

Nach Runde 9 und 10 ist „Natürliche Zahlen und Stellenwertsysteme“ (thema_id 15, block_id 49, Klasse 5) das einzige Gymnasium-Thema ohne Generator:
je Lernkarte nur 9–11 Übungen und 2–5 der Stufe 3. Ein Kind arbeitet gerade daran.

```text
Du baust zusätzliche Übungsaufgaben für ein bestehendes Thema einer Mathe-Lern-App (bayerisches Gymnasium, Klasse 5).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig schwer-natuerlich an und arbeite nur dort.

Lies zuerst vollständig: inhalte/README.md, inhalte/postfach/README.md, inhalte/vorlage_generator.py, inhalte/klar/quelle.md (dort stehen für zahlen.natuerlich alle Lernziele,
Titel und bisherigen Beispiele) und inhalte/klar/zahlen.natuerlich.json (die aktuellen Lernkarten). Als Muster: inhalte/generatoren/zahlen_teilbarkeit.py (Runde 9, gleicher Fall)
und inhalte/generatoren/_schwer_kl5.py mit einem Abschnitt „SCHWER (Zehnte Runde)“ aus einem Klasse-5-Generator. Lies außerdem in inhalte/AUFTRAEGE.md die Abschnitte
„Neunte Runde“ und „Zehnte Runde“ – deren Regeln gelten hier beide.

Aufgabe: Ein Generator inhalte/generatoren/zahlen_natuerlich.py, der inhalte/themen/zahlen.natuerlich.json schreibt (thema_id 15, block_id 49, klasse {"gym_by": 5}).
- Lernziele (Schlüssel), Reihenfolge und Titel GENAU wie in inhalte/klar/quelle.md; die Erklärfelder jeder Lernkarte unverändert aus inhalte/klar/zahlen.natuerlich.json.
- Je Lernkarte NEUE Aufgaben: 18 Übungen (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8), 1 Test, 3 Korrektur, 6 Sicherung. Die vorhandenen Aufgaben in der Datenbank bleiben, deine kommen dazu –
  also andere Zahlen und Einkleidungen als die Beispiele in quelle.md.
- Von den Stufe-3-Aufgaben je Lernkarte mindestens 2 nach Prüfungsvorbild und mindestens 1 Knobelaufgabe. Recherchiere dafür mit Websuche echte Aufgaben zu natürlichen Zahlen,
  Stellenwert, Runden, Zahlenstrahl, römischen Zahlen (z. B. bayerische Jahrgangsstufentests Klasse 6 des ISB, VERA, Känguru Klasse 5/6, Musterschulaufgaben Klasse 5).
  Urheberrecht: nie wörtlich oder mit denselben Zahlen übernehmen; Typ und Niveau sind das Vorbild. Quellen mit Adresse im Abschlussbericht nennen.
- Lösungen vom Programm berechnen und von Hand nachrechnen; Zahl-Aufgaben mit Rechenausdruck „c“; falsche Antworten aus typischen Denkfehlern; jede Aufgabe mit Tipp und Lösungsweg.
- Fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/zahlen.natuerlich.json` OK meldet und du jede Aufgabe gelesen hast. Commit + Push auf schwer-natuerlich.
Grenzen: Keine Datenbank, kein App-Code, keine Tests, kein Merge. Meldungen in inhalte/postfach/schwer-natuerlich.md. Arbeite ohne Rückfragen durch.
```

# Dreizehnte Runde: Befundlisten aus Runde 10 abarbeiten (Stufen und Fehler in alten Aufgaben)

Die sechs Klassen-Chats der Zehnten Runde haben alte Aufgaben nur gemeldet, nicht geändert. Die Listen stehen in inhalte/postfach/schwer-kl5.md … schwer-kl10.md
(jeweils Abschlussbericht, Teil „Befundliste aus Teil 1“). Ein Chat arbeitet sie ab, Zweig `befunde`.

```text
Du korrigierst gemeldete Mängel in vorhandenen Aufgaben einer Mathe-Lern-App (bayerisches Gymnasium, Klassen 5–10).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig befunde an und arbeite nur dort.
Gibt es den Zweig befunde schon, arbeite dort weiter: Lies zuerst inhalte/postfach/befunde.md und mache beim ersten Thema weiter, das dort noch nicht als fertig steht.

Lies zuerst vollständig: inhalte/README.md, inhalte/postfach/README.md und die sechs Befundlisten in inhalte/postfach/schwer-kl5.md, schwer-kl6.md, schwer-kl7.md, schwer-kl8.md,
schwer-kl9.md, schwer-kl10.md (jeweils im Abschlussbericht der Teil „Befundliste aus Teil 1“). Reihenfolge der Arbeit: Klasse 8, 5, 7, 6, 9, 10.

Aufgabe je Thema: Jeden Befund prüfen (selbst nachrechnen, nicht blind übernehmen) und im Generator des Themas (inhalte/generatoren/, teils mit Hilfsdateien) beheben:
 a) Falsch eingestufte Aufgabe: nur die Stufe ändern (Feld s). „Schwer“ heißt anderer Gedanke, nicht größere Zahlen. Frage und Antworten bleiben Zeichen für Zeichen gleich.
 b) Falsche oder unklare Lösung, Tipp oder Lösungsweg bei gleicher Frage: Lösung (o), Tipp (h), Lösungsweg (w) berichtigen. Frage und Antworten bleiben gleich.
 c) Fehler in der Frage selbst oder in den Antwortmöglichkeiten, Beinahe-Dubletten, mehrdeutige Aufgaben: die Aufgabe durch eine berichtigte ersetzen (neue Frage).
    Führe dazu in inhalte/postfach/befunde.md je Thema eine Liste „ersetzt“ mit dem genauen alten Fragetext – der Haupt-Chat sperrt die alten Fassungen in der Datenbank.
 d) Erklärung und Aufgabe passen nicht zusammen: die Aufgabe anpassen oder ersetzen (wie c), die Lernkarten-Texte NICHT ändern; solche Fälle zusätzlich unter „für Sebastian“ notieren.
Regeln:
- Alle nicht betroffenen Aufgaben bleiben Zeichen für Zeichen unverändert (per Skript gegen den Stand von lernen-app nachweisen: geändert sind nur die gemeldeten Aufgaben).
- Nach dem Umstufen muss jede Lernkarte weiter mindestens 3 Übungen je Stufe haben; fehlt dadurch etwas, passende neue Übungen ergänzen (Regeln der Zehnten Runde in inhalte/AUFTRAEGE.md).
- Befunde, die du nach eigener Prüfung für unbegründet hältst, nicht umsetzen, sondern mit kurzer Begründung unter „nicht umgesetzt“ notieren.
- Ein Thema ist fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet und der Nachweis stimmt. Ein Thema = ein Commit + Push auf befunde.
Grenzen: Keine Datenbank, kein App-Code, keine Tests, kein Merge. Keine Namen oder Daten von Kindern.
Meldungen in inhalte/postfach/befunde.md ablegen und pushen: nach jedem Thema eine Zeile (Thema fertig, Zahl umgestuft / berichtigt / ersetzt / nicht umgesetzt), am Ende ein
Abschlussbericht mit den Listen „ersetzt“ (alte Fragetexte je Thema), „nicht umgesetzt“ und „für Sebastian“. Arbeite ohne Rückfragen durch.
```

Einspielen (Haupt-Chat): einheit_abgleichen(…, 'lassen') übernimmt geänderte Stufen, Lösungen, Tipps und Lösungswege und fügt Ersatz-Aufgaben ein; die alten Fassungen aus „ersetzt“ danach sperren (freigegeben = false).

# Bau-Auftrag E-1 (App): Eltern-/Lehrerseite – Sofort-Speichern, Info-Seite, Reisewörter

Erster Auftrag an einen eigenen Bau-Chat für App-Code. Regel: Es baut immer nur EIN Chat am App-Code. Solange der Bau-Chat arbeitet, ändert der Haupt-Chat
lernen.js, style.css und tests/ nicht; er führt den Zweig danach zusammen und spielt Datenbank-Änderungen ein.

```text
Du baust an der Lern-App „Lernen Schule“ (Mathe, Kinder und Eltern/Lehrer). Du bist der Bau-Chat für App-Code.
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig bau-eltern an und arbeite nur dort.

Lies zuerst: AGENTS.md, inhalte/postfach/README.md und in inhalte/postfach/antworten.md die Einträge vom 16.11. (aktueller Stand der App und der Lernregeln).
Nur lesen, nicht mergen (mit git show):
- origin/pruefung-kinderansicht:inhalte/pruefung/UMBAU-AUFTRAG.md (Gesamtauftrag, Phasen, Wörter)
- origin/pruefung-eltern:inhalte/pruefung/eltern/umsetzung.md (Pakete E-1 bis E-4 mit Prüfpunkten)
- origin/pruefung-eltern:inhalte/pruefung/eltern/info-seite.md (Text der Info-Seite)
- origin/pruefung-eltern:inhalte/pruefung/eltern/bericht.md und rundgang.test.cjs (Befunde und Nachprüf-Skript)
Der App-Code der Lern-App steht in lernen.js (alle Ansichten), style.css, lernen/index.html, lernen/schule.js; Tests in tests/lernen.test.cjs.
Eltern-/Lehrer-Ansichten in lernen.js: viewLernen (Startseite), lernElternBereich, viewPlan (Themenplan), viewLernstand, viewInhalte, viewLehrplan, viewRueckmeldungen, viewZugaenge.

Auftrag jetzt (Paket E-1, Phase 1):
1. Themenplan (viewPlan): Jede Änderung (verschieben, hinzufügen, entfernen, „kann schon“) wird sofort gespeichert (Aktion schule_plan_setzen mit revision). Der Knopf „Plan speichern“
   entfällt. Nach jeder Änderung erscheint kurz „Gespeichert · Rückgängig“; „Rückgängig“ stellt den Zustand vor der letzten Änderung wieder her. Bei Versionskonflikt
   (jemand anderes hat den Plan geändert) eine klare Meldung mit Knopf „Neu laden“; nichts überschreiben.
2. Info-Seite „So funktioniert’s“ mit den Teilen „Erste Schritte“ und „Fragen“. Text aus info-seite.md, in Reisewörtern. Erreichbar mit einem Tipp oben rechts auf der Startseite
   der Eltern/Lehrer und im Themenplan. Prüfe jeden Satz der Info-Seite gegen den Code und die Einträge vom 16.11. in antworten.md; gilt eine Regel inzwischen anders, schreibe den
   aktuellen Stand. Aktuell gilt u. a.: Eine neue Etappe zeigt zuerst die Erklärung. Eine Etappe sitzt nach 6 Punkten (richtig im ersten Versuch ohne Hilfe +1, Fehler −2) und mindestens
   einer schweren Bordkarte im ersten Versuch. Bei einem Fehler gibt es zuerst einen zweiten Versuch. Wiederholungen kommen nach 1, 3, 7, 14, 30 Lerntagen, höchstens 6 vor einem Flug.
3. Reisewörter jetzt auch in ALLEN Texten für Eltern und Lehrer: Thema → Flug, Lernkarte → Etappe, Aufgabe → Bordkarte, Gebiet → Kontinent, Stadt → Ort
   (auch „Themenplan“ → „Flugplan“, „Lernziel“ → „Etappe“). Auf Geschlecht und Fall achten („dieses Thema“ → „dieser Flug“). Intern (Code, Datenbank, inhalte/README.md)
   bleiben die bisherigen Namen. In den Kinderansichten ist das schon umgesetzt – dort nichts zurückändern.

Arbeitsweise:
- Tests: cd in das Repository, dann `node --test tests/lernen.test.cjs` (Playwright mit Chromium; ist kein Browser vorinstalliert, den Pfad über PW_TEST_EXECUTABLE setzen).
  Danach `git checkout -q -- docs/previews`. Alle Tests müssen durchlaufen; passe Erwartungen an neue Texte an und ergänze Tests für Sofort-Speichern, Rückgängig, Versionskonflikt
  und Info-Seite. tests/search.test.cjs hat 10 bekannte alte Fehler, die nicht zu diesem Auftrag gehören.
- Stelle zusätzlich das Nachprüf-Skript der Eltern-Runde nach (rundgang.test.cjs aus origin/pruefung-eltern vorübergehend an seinen Ort kopieren, laufen lassen, danach wieder entfernen –
  nicht committen).
- Version: aktuelle Nummer in sw.js suchen und überall erhöhen (sw.js, app.js, index.html, lernen/schule.js, lernen/index.html, tests/search.test.cjs), dazu den Cache-Namen 'vNNN'
  in sw.js und tests/search.test.cjs um 1 erhöhen.
- Datenbank und Serverfunktionen rührst du nicht an. Braucht ein Punkt eine Datenbank-Änderung, lege sie als Datei unter supabase/migrations/ ab (nicht ausführen) und melde es;
  der Haupt-Chat spielt sie nach den Werkstatt-Regeln ein. E-1 sollte ohne Datenbank-Änderung auskommen.
- Keine Schlüssel, Tokens, Zugangscodes oder Daten echter Kinder in Code, Commits oder Nachrichten. Kein Merge nach main und nicht nach lernen-app. Kleine, klare Commits; pushen auf bau-eltern.
Meldung: inhalte/postfach/bau-eltern.md – am Ende ein Bericht: was gebaut ist, je Prüfpunkt aus umsetzung.md „erfüllt/nicht erfüllt“, was nicht geprüft werden konnte, offene Fragen.
Arbeite ohne Rückfragen durch. Die Pakete E-2 bis E-4 NICHT beginnen – dafür kommt ein eigener Auftrag.
```

Danach (Haupt-Chat): Zweig bau-eltern prüfen, nach lernen-app zusammenführen, Meldung „Phase 1 (E-1)“ ins Postfach.

# Bau-Auftrag Phase 2 und 3 (App): Kinderansicht K2–K4, Eltern E-2–E-4, Befunde N1–N5

Entscheidung Sebastian 16.11.: Der Bau-Chat übernimmt den ganzen App-Umbau der Phasen 2 und 3. Voraussetzung: Bau-Auftrag E-1 ist fertig und nach lernen-app zusammengeführt.
Es baut immer nur EIN Chat am App-Code.

```text
Du bist der Bau-Chat für den App-Code der Lern-App „Lernen Schule“ und setzt den Umbau fort.
Repository: beinhoff77-stack/ki-system. Hole den aktuellen Stand des Zweigs lernen-app und lege davon den Zweig bau-phase2 an (gibt es ihn schon: dort weiterarbeiten, vorher lernen-app hineinführen).
Lies zuerst: AGENTS.md, in inhalte/AUFTRAEGE.md den Abschnitt „Bau-Auftrag E-1“ (dort stehen Arbeitsweise, Tests, Version, Grenzen – sie gelten unverändert) und in
inhalte/postfach/antworten.md die Einträge vom 16.11. Nur lesen, nicht mergen (git show):
- origin/pruefung-kinderansicht:inhalte/pruefung/UMBAU-AUFTRAG.md (Gesamtauftrag) und inhalte/pruefung/NACHPRUEFUNG-2026-11-16.md (neue Befunde N1–N5)
- origin/pruefung-kinderansicht:inhalte/pruefung/kinderansicht/umsetzung.md und bericht.md (K2–K4, Rechenregel „Stand“, Entwürfe)
- origin/pruefung-eltern:inhalte/pruefung/eltern/umsetzung.md, bericht.md, info-seite.md (E-2 bis E-4)

Reihenfolge – nach jedem Schritt Tests grün, Version erhöhen, Commit + Push, Meldung in inhalte/postfach/bau-phase2.md:
Schritt A (zuerst): Befunde N1–N8 aus der Nachprüfung (NACHPRUEFUNG-2026-11-16.md, Bilder unter inhalte/pruefung/nach/bilder/ im Zweig pruefung-kinderansicht).
  N1 Bildergeschichte: Ein Schrittbild nur zeigen, wenn es sich gegenüber dem zuletzt gezeigten Bild (auch dem Einstiegsbild) ändert, sonst nur den Text. Was in einem Schritt neu ins
     Bild kommt, in der Akzentfarbe und kräftig zeichnen (Punkte, Bögen, Steigungsdreieck mindestens 2 Einheiten breit). Ursache: lernErklaerung zeichnet den Bildzustand bei jedem Schritt;
     betroffen sind 413 von 443 Etappen. Ziel: keine zwei gleichen Bilder hintereinander; Etappe „Was bedeutet eine negative Zahl?“ auf dem Handy deutlich unter 3 000 px.
  N8 Bildergeschichte auf Tablet und Rechner: je Schritt Bild links und Text rechts daneben (oder Bild links mitlaufend, Schritte rechts). Heute stehen Nummer, Bild und Text auseinander.
  N2 Übersicht der Etappen: „Kurz gesagt“ ganz zeigen (höchstens zwei Zeilen, kein „…“).
  N3 Kurs-Grafik: Komma nur zeigen, wenn eine der beiden Zahlen Nachkommastellen hat (heute „2 4 ,“ bei 24 %).
  N4 Startknopf auf der Abflugtafel: „Erst 1 Wiederholung ›“ statt „Erst wiederholen · ROM ›“; nach der Wiederholung „Weiter nach Rom ›“.
  N5 Fehler-Detektiv: bis zu den Fehlbildern (R4) nur zeigen, wenn kein Fehlermuster erkannt wurde.
  N6 Test-Seiten: im Kopf „Ort · Flugname“ wie im Erklären-Reiter statt des Ortstitels (ctx.titel in viewLernEinheit nimmt ort_titel).
  N7 Testergebnis: Knöpfe im Abflug-Stil statt der ungestalteten Links „Zum Flug“/„Zur Reise“; bei „noch üben“ ein Hauptknopf „Erst üben: <Etappe> ›“ und danach „Verbessern ›“;
     beim Zahlenstrahl die richtige Markierung grün einzeichnen.
  Nach Schritt A eine eigene Meldung im Postfach („Schritt A fertig“), damit die Nachprüfung laufen kann.
Schritt B (Phase 2, Kinder): K2 – Mein Weg mit den Reitern Stand · Kontinente · Karte; Weltkarte aus dem Menü in „Mein Weg“ (Menü: Abflugtafel · Mein Weg · Merkheft · Reisepass);
  Karte nur mit Orten der eigenen Klasse, Antarktis als Polarkarte von oben; Merkheft nur Geschafftes, gegliedert Kontinent → Flug → Etappe, Suche oben.
  Dazu: Die Flüge innerhalb eines Ortes nach dem Feld „reihenfolge“ der Übersicht ordnen, sobald es geliefert wird (sonst wie bisher).
Schritt C (Phase 2, Eltern): E-2 – Startseite je Kind ein Bereich; Flugplan in zwei Spalten mit Ziehen (Maus und Finger) und ↑ ↓; Flüge innerhalb eines Ortes abwählbar.
  E-3 – ein Knopf „Ändern lassen“ an Erklärung, Etappe, Bordkarte, Flug und Plan; „Meine Aufträge“ mit Status und Antwort (ersetzt Rückmeldungen, Anmerkung, „Bauen lassen“).
Schritt D (Phase 3): K3 – Mini-Linien GYM · RS · IB auf der Abflugtafel, „Stand“ mit 3 Ebenen, Feld stufen je Kind. K4 – Eltern-Ansicht mit 3 Ebenen und Einstiegs-Check
  (Hinweis „Orientierung, keine Einstufung durch eine Schule“). In K4 je Etappe anzeigen, wie viele Bordkarten bis „sitzt“ gebraucht wurden
  (damit sichtbar wird, ob die Regel „6 Punkte und eine schwere Bordkarte“ für Klasse 5 zu lang ist; fehlt dafür ein Feld, als Migration vorschlagen). E-4 – neuer Plan aus Lehrplan-Vorlage (Schulart, Klasse, Stufen).
Jeder Schritt richtet sich nach den Prüfpunkten („fertig, wenn …“) in den umsetzung.md-Dateien.

Datenbank: Du führst nichts aus. Für abwählbare Flüge (E-2), neue Auftragsarten (E-3) und das Feld stufen (K3/E-4) schreibst du je eine Migration als Datei unter supabase/migrations/
(Namensmuster wie die vorhandenen 20261116_w150_*.sql; bestehende Funktionen nur mit create or replace bzw. per gezieltem Ersetzen wie in 20261116_w150_r3_*.sql; kein DROP, kein DELETE)
und beschreibst im Postfach, welche neuen Felder die App-Aktionen liefern oder annehmen müssen. Baue die App so, dass sie ohne die Migration weiterläuft (Feld fehlt → bisheriges Verhalten).
Der Haupt-Chat spielt die Migration ein; danach prüfst du den Schritt gegen die echte Antwortform. Mache nach Schritt C und nach Schritt D eine Pause mit der Meldung
„wartet auf Migration“, wenn eine nötig ist.
Wörter: In ALLEN Texten (Kinder, Eltern, Lehrer) Flug, Etappe, Bordkarte, Kontinent, Ort. Ändert sich eine Lernregel, die Info-Seite im selben Schritt anpassen.
Grenzen wie im Bau-Auftrag E-1: keine Schlüssel oder Kinderdaten, kein Merge nach main oder lernen-app. Arbeite ohne Rückfragen durch.
```

# Vierzehnte Runde (D2-Folge, Inhalte): neuer Flug „Winkelsätze“ (Klasse 7), Vertiefungen kennzeichnen, Lehrplan-Reihenfolge

Entscheidungen Sebastian 16.11. zum Vorschlag inhalte/pruefung/klassen/vorschlag.md (Zweig daten-klassen): alles wie empfohlen. In der Datenbank schon umgesetzt:
Ortsklassen, Umzüge Zehnerpotenzen → Paris und Ortslinien → Kairo, Schrägbilder und Simulation am Gymnasium Klasse 10, Titel „Mit Winkeln rechnen“.

```text
Du ergänzt Inhalte einer Mathe-Lern-App (bayerisches Gymnasium).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig daten-klassen-2 an und arbeite nur dort.
Lies zuerst vollständig: inhalte/README.md (Format, Regeln, „Verständliche Erklärungen“ mit „Vorgabe seit 16.11.“, „Zeichnungen“), inhalte/postfach/README.md, inhalte/vorlage_generator.py,
in inhalte/AUFTRAEGE.md die Abschnitte „Zehnte Runde“ und „Elfte Runde“, und mit git show origin/daten-klassen:inhalte/pruefung/klassen/vorschlag.md den Vorschlag samt Quellen.

Teil 1 – Neuer Flug „Winkelsätze“ (thema_schluessel geometrie.winkelsaetze, thema_id 98, block_id 80 = Addis Abeba, klasse {"gym_by": 7}):
LehrplanPLUS Gymnasium M7 2.2 „Winkelbetrachtungen an Figuren“: Scheitel- und Nebenwinkel, Stufen- und Wechselwinkel an Parallelen, Innenwinkelsumme im Dreieck, Winkelsumme im Viereck
und Vieleck, Außenwinkel, Winkel berechnen und begründen in Figuren. Lies den Lehrplantext selbst nach (Websuche, lehrplanplus.bayern.de) und lege 6–8 Lernkarten fest.
Als Muster: inhalte/generatoren/geometrie.winkel.py (Klasse 5, Zeichnungsart figur) – dessen Inhalte nicht wiederholen, sondern darauf aufbauen.
Generator inhalte/generatoren/geometrie.winkelsaetze.py schreibt inhalte/themen/geometrie.winkelsaetze.json. Lernkarten im neuen Muster (einstieg, woerter, Schritte als Bildergeschichte mit
Zeichnungen, fehler mit fehler_bild, regel, probe). Je Lernkarte 18 Übungen (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8; davon mindestens 2 nach Prüfungsvorbild und 1 Knobelaufgabe –
Regeln der Zehnten Runde, Urheberrecht beachten), 1 Test, 3 Korrektur, 6 Sicherung. Eintrag in inhalte/themenliste.json ergänzen (mit lehrplan_gym „M7 2.2“).
Teil 2 – Vertiefungen kennzeichnen (nicht Pflicht, also nicht testrelevant): in den Generatoren
 geometrie.winkel („Winkel an einer Geradenkreuzung“), abbildungen.kongruenz (Verschiebung, Drehung, Parkett), raum.schraegbilder (windschief, Punkte im Raum mit Koordinaten)
 die betroffenen Lernkarten aus bewertung.lernziele_pflicht nehmen (siehe README, „Vertiefung“). Bei geometrie.winkel außerdem Titel „Mit Winkeln rechnen“ und umfang auf Klasse-5-Stoff kürzen.
 Sonst nichts an diesen Themen ändern (Nachweis per Skript: Aufgaben und Lernkarten-Texte unverändert).
Teil 3 – inhalte/themenliste.json: (a) die vier fehlenden Themen aufnehmen (zahlen.natuerlich, zahlen.teilbarkeit, terme.umformen, finanzen.zinsen; Angaben aus inhalte/klar/quelle.md und den
 Generatoren), (b) für JEDES Thema mit gym_by das Feld lehrplan_gym füllen, soweit im Vorschlag belegt, (c) neues Feld reihenfolge je Thema, z. B. {"gym_by": 3}: laufende Nummer in
 Lehrplan-Reihenfolge innerhalb der Klasse und Schulart. Gymnasium nach den Lernbereichs-Nummern des LehrplanPLUS; für rs_by und ib_myp nur setzen, wenn du die Reihenfolge belegen kannst,
 sonst weglassen und im Postfach nennen.
Fertig, wenn `python3 -I tools/inhalt_pruefen.py` für alle geänderten Themendateien OK meldet. Je Teil ein Commit + Push auf daten-klassen-2.
Grenzen: Keine Datenbank, kein App-Code, keine Tests, kein Merge. Meldungen in inhalte/postfach/daten-klassen-2.md. Arbeite ohne Rückfragen durch.
```

# Fünfzehnte Runde: offene Punkte aus der Liste „für Sebastian“ (Befund-Chat) umsetzen

Entscheidung Sebastian 17.11.: wie vom Haupt-Chat vorgeschlagen. Grundlage: inhalte/postfach/befunde.md, Abschnitt „Liste „für Sebastian““.

```text
Du überarbeitest einzelne Lernkarten und Aufgaben einer Mathe-Lern-App (bayerisches Gymnasium).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig nacharbeit an und arbeite nur dort.
Lies zuerst vollständig: inhalte/README.md (Format, „Verständliche Erklärungen“ mit „Vorgabe seit 16.11.“, „Zeichnungen“), inhalte/postfach/README.md,
inhalte/postfach/befunde.md (Abschnitt „Liste „für Sebastian““ und die Arbeitsweise im Abschlussbericht) sowie in inhalte/AUFTRAEGE.md die Abschnitte „Zehnte Runde“ und „Dreizehnte Runde“.
Die Themen sind für Kinder freigegeben: Was du nicht ausdrücklich ändern sollst, bleibt Zeichen für Zeichen gleich (Nachweis per Skript wie in der Dreizehnten Runde,
Werkzeug inhalte/generatoren/_befunde_nachweis.py bzw. ein eigenes Vergleichsskript gegen origin/lernen-app).

Aufträge (je Thema ein Commit + Push):
1. funktionen.trig (Klasse 10) – Bogenmaß: LehrplanPLUS M10 3 und das Abitur arbeiten im Bogenmaß; die App kann die x-Achse in Vielfachen von π beschriften (README, Zeichnungen).
   Lernkarten so ergänzen, dass Bogenmaß erklärt und danach durchgehend mitgeführt wird (Gradmaß bleibt als Einstieg). Je Lernkarte mindestens 8 neue Übungen im Bogenmaß
   (Stufe 1: 2, Stufe 2: 3, Stufe 3: 3). Die alten Gradmaß-Aufgaben bleiben. Den veralteten Eintrag unter „offen“ (keine π-Beschriftung) entfernen.
2. daten.kennwerte (Klasse 6): die Lernkarten modal_spannweite und median als Vertiefung führen (aus bewertung.lernziele_pflicht nehmen, in bewertung.lernziele_vertiefung eintragen –
   Muster: geometrie.winkel nach der Vierzehnten Runde). Sonst nichts ändern.
3. Erklärung ergänzen, damit sie zu den vorhandenen Aufgaben passt (je ein zusätzlicher Schritt der Bildergeschichte mit Zeichnung, höchstens zwei; Längenregeln der README einhalten):
   a) geometrie.grundbegriffe / kreis_lage: zwei Kreise – von außen berühren und getrennt liegen (Abstand der Mittelpunkte im Vergleich zu r₁ + r₂).
   b) geometrie.ortslinien / zwei_kreise: „Kreis im Kreis“ (Abstand kleiner als r₁ − r₂) kurz zeigen.
   c) trigo.allgemein / kosinussatz_seite: bei Kurs- und Schiff-Aufgaben ist der Dreieckswinkel 180° minus Drehwinkel – mit Zeichnung.
   d) gleichungen.lgs3 / loesen: ein Schritt „Was, wenn am Ende 0 = 5 oder 0 = 0 steht?“ (keine bzw. unendlich viele Lösungen).
4. geometrie.konstruktion / kongruenzsatz: Die Stufe-3-Aufgaben zum Fall SsW sind ohne Zeichnung kaum zu entscheiden. Jede dieser Aufgaben bekommt eine Zeichnung (Zeichnungsart figur),
   aus der die Lage der gegebenen Stücke ablesbar ist; ist das nicht sauber möglich, die Aufgabe durch eine entscheidbare ersetzen und den alten Fragetext unter „ersetzt“ melden.
5. Aufräumen: veraltete Einträge unter „offen“ entfernen oder berichtigen – funktionen.grundbegriffe („Kreis kann die App nicht zeichnen“ stimmt nicht mehr) und geometrie.winkel
   (nennt noch die alte Lage „Winkelsätze Kl. 5“; das Thema heißt jetzt „Mit Winkeln rechnen“, Winkelsätze sind ein eigener Flug in Klasse 7).
6. inhalte/README.md: einen kurzen Abschnitt „Vertiefung“ ergänzen (Felder bewertung.lernziele_pflicht und bewertung.lernziele_vertiefung, Bedeutung: nicht testrelevant, zählt nicht für den Stempel).
Nicht ändern (so entschieden): gleichungen.potenz – Zinseszins-Sachaufgaben bleiben in Klasse 9; zahlen.intervalle und gleichungen.ungleichungen bleiben vorläufig Klasse 8;
Schrägbilder, Simulation und Ortslinien sind durch D2 schon geklärt.

Fertig je Thema, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet und der Nachweis „nur das Beauftragte geändert“ stimmt.
Grenzen: Keine Datenbank, kein App-Code, keine Tests, kein Merge. Keine Schulbuch- oder Prüfungsaufgaben wörtlich übernehmen.
Meldungen in inhalte/postfach/nacharbeit.md: nach jedem Thema eine Zeile, am Ende ein Abschlussbericht mit den Listen „geänderte Lernkarten“ (Thema, Lernkarte, was ergänzt wurde),
„ersetzt“ (alte Fragetexte) und „offen geblieben“. Arbeite ohne Rückfragen durch.
```

Einspielen (Haupt-Chat): einheit_abgleichen(…, 'sperren') je Thema (Weg A); geänderte Erklärungen dabei mit übernehmen.

# Sechzehnte Runde: Flug „Winkelsätze“ nach zwei Prüfungen nachbessern

Zwei Prüf-Chats haben geometrie.winkelsaetze (Entwurf, Einheit 92) geprüft: „freigabereif: nein“. Befunde:
origin/pruefung-winkelsaetze:inhalte/postfach/pruefung-winkelsaetze.md (Teile A, B, C) und origin/pruefung-eltern:inhalte/postfach/pruefung-eltern.md (Abschnitt „Flug Winkelsätze“).

```text
Du besserst einen neuen, noch nicht freigegebenen Flug einer Mathe-Lern-App nach (bayerisches Gymnasium, Klasse 7): geometrie.winkelsaetze.
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig winkelsaetze-2 an und arbeite nur dort.
Lies zuerst vollständig: inhalte/README.md, inhalte/postfach/README.md, den Generator inhalte/generatoren/geometrie.winkelsaetze.py und die beiden Prüfberichte (nur lesen, git show):
origin/pruefung-winkelsaetze:inhalte/postfach/pruefung-winkelsaetze.md und origin/pruefung-eltern:inhalte/postfach/pruefung-eltern.md (Abschnitt „Flug Winkelsätze“).
Das Thema ist ein Entwurf ohne Lernstände: Aufgaben dürfen geändert, ersetzt und umsortiert werden.

Setze ALLE Befunde beider Berichte um (Teil A, B und C sowie die drei „Vor der Freigabe beheben“ und die Kleinigkeiten des zweiten Berichts). Entscheidungen dazu:
- Außenwinkel: Die Etappe aussenwinkel wird Vertiefung (bewertung.lernziele_vertiefung, nicht Pflicht), weil sie nicht im LehrplanPLUS M7 2.2 steht.
  Aufgaben anderer Etappen, die den Außenwinkelsatz brauchen (z. B. parallel_pruefen #67, #69, #71, #73), über Stufenwinkel bzw. Winkelsumme begründen oder in die Etappe aussenwinkel verschieben.
- Gleichschenklige Dreiecke / Basiswinkel (Stoff von M7 5) kommen in Pflicht-Etappen nicht vor; solche Aufgaben ersetzen. In der Vertiefungs-Etappe aussenwinkel höchstens 2 davon, mit dem Satz
  „Im gleichschenkligen Dreieck sind die beiden Basiswinkel gleich groß“ im Aufgabentext.
- Lineare Gleichungen (M7 3) kommen nach diesem Flug: Aufgaben, die nur mit x-Ansatz lösbar sind, ohne Variable stellen („Teile“-Überlegung) oder ersetzen; „Wie groß ist x?“ nicht mit Einheit Grad.
- Wechselwinkel: nur eindeutige Paare abfragen; „weder noch“ nur für Paare, die an Parallelen nie gleich groß sind. In der Lernkarte einen Satz ergänzen, dass manche Bücher auch die
  äußeren Paare Wechselwinkel nennen.
- Zeichnungen: „nicht parallel“ sichtbar nicht parallel zeichnen; Winkelbögen an der richtigen Geraden; angeschriebene und gezeichnete Winkel höchstens 3° auseinander;
  Etappe figuren: jede Bordkarte mit Zeichnung (Zeichnungsart figur); Etappe vieleck: Stufe 1 und 2 mit Zeichnung.
- Etappe beweisen: Test, Korrektur und Sicherung prüfen das Lernziel der Etappe (Fundamentalsatz/abgeleiteter Satz, Zirkelschluss, Reihenfolge einer Beweiskette); die Lückenaufgabe eindeutig machen.
- Bildergeschichte innenwinkelsumme: jeder Schritt mit eigenem Bild, die Wechselwinkel an C eingezeichnet.
- Mehr Abwechslung, wo die Berichte Wiederholungen nennen; Schreibweise ∢BAC einheitlich und einmal erklärt; große Zahlen mit Leerzeichen; fehlende Wörter in woerter.
- Überschneidung mit geometrie.konstruktion (gleicher Ort): nichts an geometrie.konstruktion ändern, nur im Postfach auflisten, welche Karten sich überschneiden.
Mengen je Etappe bleiben: 18 Übungen (4/6/8), 1 Test, 3 Korrektur, 6 Sicherung. Lösungen berechnen und von Hand nachrechnen; jede Zeichnung ansehen (gezeichnete gegen angeschriebene Winkel per Skript).
Fertig, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/geometrie.winkelsaetze.json` OK meldet. Commit + Push auf winkelsaetze-2.
Grenzen: Keine Datenbank, kein App-Code, keine Tests, kein Merge, keine anderen Themen. Meldung in inhalte/postfach/winkelsaetze-2.md: je Befund „behoben / anders gelöst / nicht umgesetzt (Grund)“.
Arbeite ohne Rückfragen durch.
```

Einspielen (Haupt-Chat): Entwurf → einheit_abgleichen(…, 'loeschen'); danach kurze Nachprüfung und Freigabe durch Sebastian.

# Zusatz zum Bau-Auftrag Phase 2 (17.11.): Befunde aus der Nachprüfung E-1

Quelle: origin/pruefung-eltern:inhalte/postfach/pruefung-eltern.md (Befunde 1–6). Schritt A (N1–N8) ist nach lernen-app zusammengeführt (0.74.2).

```text
Zusatz zum laufenden Bau-Auftrag Phase 2 und 3 (Zweig bau-phase2). Schritt A ist nach lernen-app zusammengeführt (0.74.2, 24 von 24 Tests); führe lernen-app in bau-phase2, bevor du weitermachst.
Die Nachprüfung von E-1 (git show origin/pruefung-eltern:inhalte/postfach/pruefung-eltern.md) hat sechs Befunde. Bitte in Schritt C (E-2) mit erledigen:
1. Info-Seite: keine feste Zahl der Flüge („derzeit 87“) – zählen oder „über 90“; den überholten Satz zu „16 Flügen, Klassen-Zuordnung noch geprüft“ streichen;
   „100 Sterne für einen geschafften Ort“ ergänzen.
2. Rückgängig nach „Entfernen“ eines geschafften Ortes: Der Ort darf „geschafft“ nicht verlieren. Datenbank-Seite (schule_plan_setzen) als Migration-Datei vorschlagen
   (alten Status beim Entfernen merken bzw. fertig nicht überschreiben) – zusammen mit der Migration für abwählbare Flüge.
3. Positionen entfernter Orte wachsen bei jedem Speichern um 200 000 (Zahlenüberlauf nach etwa 10 000 Speichervorgängen): in derselben Migration beheben.
4. „Rückgängig“ dauerhaft in der Kopfzeile des Flugplans, nicht nur 8 Sekunden.
5. Reisewörter-Test: Muster auf \bThema\b|\bThemen\b ändern (die gewollte Erklärung „Flug = ein Mathe-Thema“ ausnehmen).
6. Flugplan-Zeilen flacher und Ziehen statt vieler Tipps – ist ohnehin E-2.
Außerdem aus deinem eigenen Bericht zu N2: Die App zeigt „Kurz gesagt“ jetzt ganz; die 116 zu langen Merksätze sind Inhalt und gehen an einen Inhalts-Chat, nicht an dich.
```

# Zusatz 2 zum Bau-Auftrag Phase 2 (17.11.): Schritt A2 aus der Nachprüfung N1–N8

Quelle: origin/pruefung-kinderansicht:inhalte/pruefung/NACHPRUEFUNG-2026-11-17-N1-N8.md. Schritt B (K2, App 0.74.3) ist nach lernen-app zusammengeführt (26 von 26 Tests).

```text
Zusatz 2 zum laufenden Bau-Auftrag Phase 2 und 3 (Zweig bau-phase2). Schritt B (K2, 0.74.3) ist nach lernen-app zusammengeführt (26 von 26 Tests); führe lernen-app in bau-phase2, bevor du weitermachst.
Die Nachprüfung von Schritt A (git show origin/pruefung-kinderansicht:inhalte/pruefung/NACHPRUEFUNG-2026-11-17-N1-N8.md, Abschnitt „Nacharbeit“) meldet: N3–N8 erfüllt, N2 nicht erfüllt, N1 teilweise.
Bitte als Schritt A2 VOR Schritt C erledigen, eigene Meldung „Schritt A2 fertig“ im Postfach:
1. N2 (Fehler): Das Satzende für „Kurz gesagt“ wie früher an jedem . ! ? vor einem Leerzeichen oder dem Textende erkennen, aber nicht nach Abkürzungen (z. B., d. h., u. a., bzw., ca., usw., vgl.).
   Heute enthalten 87 von 593 „Kurz gesagt“ zwei Sätze. Test: alle Merksätze aus inhalte/themen durchlaufen – „Kurz gesagt“ ist höchstens ein Satz.
2. N1 Abblenden: Den Rest des Bildes nicht über die Deckkraft zurücknehmen (in der hellen Gestaltung verschwindet der gelbe Graph fast). Stattdessen Graphen und Linien grau mit mindestens 3:1 Kontrast
   zum Hintergrund zeichnen oder nur Gitter und Hilfslinien zurücknehmen; abblenden nur, wenn wirklich ein Element neu ist.
3. N1 Steigungsdreieck: NICHT mehr in der App vergrößern (Text und Bild stimmen sonst nicht überein). Das Dreieck so zeichnen, wie es im Inhalt steht, neu = kräftig in Akzentfarbe.
   Die Inhalte dazu ändert ein Inhalts-Chat.
4. N1 Tabellen und Stellentafel: die geänderte Zelle hervorheben (markiert oder neuer Wert), wenn ein Schritt nur eine Zelle ändert.
5. N7: für die richtige Markierung am Zahlenstrahl ein festes Grün, das in allen Gestaltungen grün ist.
```

# Siebzehnte Runde (Inhalte): „Kurz gesagt“ kürzen, Steigungsdreieck, überdeckte Beschriftung

Befunde aus dem Bericht des Bau-Chats (N2) und der Nachprüfung N1–N8. Entscheidung zum Steigungsdreieck: im Inhalt 2 Einheiten breit zeichnen und den Text anpassen.

```text
Du überarbeitest einzelne Stellen in den Lernkarten einer Mathe-Lern-App (bayerisches Gymnasium, Klassen 5–10). Die Themen sind für Kinder freigegeben.
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig merksaetze an und arbeite nur dort.
Lies zuerst vollständig: inhalte/README.md („Verständliche Erklärungen“ mit „Vorgabe seit 16.11.“, „Zeichnungen“), inhalte/postfach/README.md, in inhalte/AUFTRAEGE.md die Abschnitte
„Dreizehnte Runde“ und „Fünfzehnte Runde“ (Arbeitsweise und Nachweis) und mit git show origin/pruefung-kinderansicht:inhalte/pruefung/NACHPRUEFUNG-2026-11-17-N1-N8.md den Prüfbericht.

1. „Kurz gesagt“: Der erste Satz des Feldes regel jeder Lernkarte ist das „Kurz gesagt“ (Regel: ein Satz, höchstens 12 Wörter). Finde per Skript in allen Dateien unter inhalte/themen
   mit gym_by-Klasse die Lernkarten, deren erster Satz länger als 12 Wörter oder länger als 90 Zeichen ist (Satzende: . ! ? vor Leerzeichen oder Textende, nicht nach z. B., d. h., u. a., bzw.,
   ca., usw., vgl.; laut Prüfung etwa 75). Schreibe für jede einen neuen ersten Satz mit höchstens 12 Wörtern, der den Kern der Regel in Kindersprache trifft; der Rest der Regel bleibt
   inhaltlich gleich (er darf den bisherigen ersten Satz als zweiten Satz behalten). Mathematisch nichts verändern oder verkürzen, was dann falsch wäre.
2. Steigungsdreieck (funktionen.linear, 4 Schritte laut Prüfbericht): Das Dreieck im Inhalt 2 Einheiten breit zeichnen und den Schritt-Text passend machen
   (z. B. „In 2 Stunden wird sie 3 cm kürzer – das sind 1,5 cm je Stunde“). Die App vergrößert das Dreieck künftig nicht mehr selbst.
3. Überdeckte Beschriftung: In der Kerze-Etappe überdeckt der Punktname „leer“ den Graphennamen „Kerze“ (beide bei x ≈ 13) – Beschriftung versetzen. Prüfe per Skript alle Karten- und
   Schrittbilder der Art koordinaten auf Namen, die näher als 1 Einheit beieinander liegen, und versetze sie.
Regeln: Nur die genannten Felder ändern (regel, einzelne schritte bzw. bild). Aufgaben und alles Übrige bleiben Zeichen für Zeichen gleich – Nachweis per Skript gegen origin/lernen-app.
Änderungen im Generator des Themas (Abschnitt wie in der Fünfzehnten Runde), nicht nur in der JSON-Datei. Je Thema ein Commit + Push auf merksaetze.
Fertig je Thema, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet und der Nachweis stimmt.
Grenzen: Keine Datenbank, kein App-Code, keine Tests, kein Merge. Meldungen in inhalte/postfach/merksaetze.md; am Ende eine Liste alt → neu für jeden geänderten Merksatz. Arbeite ohne Rückfragen durch.
```

# Zusatz 3 zum Bau-Auftrag (17.11.): Schritt E – Befunde M1–M9 aus der Nachprüfung 0.74.5

Quelle: origin/pruefung-kinderansicht:inhalte/pruefung/NACHPRUEFUNG-2026-11-17.md (Bilder unter inhalte/pruefung/nach-0745/bilder/). Schritt D ist zusammengeführt (0.74.6), Migration D eingespielt.

```text
Zusatz 3 zum Bau-Auftrag (Zweig bau-phase2). Schritt D (K3, K4, E-4; App 0.74.6) ist nach lernen-app zusammengeführt, 38 von 38 Tests. Die Migration 20261117_w150_d_stufen_stand.sql ist
unverändert eingespielt. Ein Test wurde stabilisiert (K4 wartete nicht auf die fertig gezeichnete Seite und las gelegentlich „Lade …“). Führe lernen-app in bau-phase2.
1. Prüfe Schritt D gegen die echte Antwortform (schule_uebersicht.themen und lernende[].stufen, schule_plan_lesen.kind.stufen und lehrplan_reihenfolge, schule_lernstand.bis_sitzt/sitzt_am,
   schule_kind_setzen mit stufen) und melde das Ergebnis.
2. Schritt E – Befunde der Nachprüfung 0.74.5 (git show origin/pruefung-kinderansicht:inhalte/pruefung/NACHPRUEFUNG-2026-11-17.md, Abschnitt „Neue Befunde“):
   M1 „Gerade dran“ in Mein Weg · Stand widerspricht den Zahlen darüber: „Gerade dran“ = nur der aktuelle Ort (höchstens dazu der nächste); alles Übrige im Plan unter „Kommt noch“.
      Kacheln passend, z. B. „1 kann ich · 1 gerade dran · 12 kommen noch“.
   M2 Flugplan: Das Feld „Klasse“ (und die Stufen je Schulart) speichert sofort wie der Plan – kein eigener Knopf „Speichern“.
   M3 Aufgeklappter Ort im Flugplan: Häkchen links in derselben Zeile wie der Flugname, eine Zeile je Flug.
   M4 Orte, deren Flüge alle über der Klasse des Kindes liegen: im Flugplan sichtbar markieren („Klasse 8 – über der Klasse des Kindes“) und beim Kind unter „Später“ einsortieren,
      solange Eltern sie nicht bewusst vorgezogen haben (Vorziehen = im Plan vor einem Ort der eigenen Klasse eingeordnet).
   M5 Abflugtafel: als Ziel das nächste Zwischenziel zeigen („Noch 3 Etappen bis ›Ganze Zahlen‹ gelandet“); der Stempel des Ortes mit allen Flügen steht im Reisepass und klein darunter.
   M6 Detektiv bei Auswahl-Bordkarten ohne hinterlegtes Fehlermuster: neutraler Satz („Schau dir deine Wahl und die Frage noch einmal an“) statt eines Musters, das nicht zur Antwort passt.
   M7 Erklärung: bei „Worum geht’s“ kein Bild zeigen, wenn Schritt 1 dasselbe Bild (nur mit Ergänzung) zeigt.
   M8 Schwebender Menüknopf ≡ verdeckt Inhalt: prüfen (Handy 390 px, Tablet 820 px, beim Rollen) und so setzen, dass er keinen Text und keinen Knopf überdeckt.
   M9 Text „Für deine Klasse ist alles verteilt.“ → „Alles aus Klasse 5 steht schon in deinem Plan.“ (mit der Klasse des Kindes).
   Außerdem aus dem Prüfbericht „nicht nachgestellt“: Ziehen im Flugplan auf Handy (390 px) und Rechner (Maus) mit einem eigenen Test absichern; Startseite: GYM/RS/IB-Balken dürfen nicht „–“ zeigen,
   wenn Flüge mit Klasse da sind.
Tests grün, Version erhöhen, Commit + Push, Meldung „Schritt E fertig“ im Postfach. Braucht ein Punkt die Datenbank: Migration als Datei, nicht ausführen.
```

# Zusatz 4 zum Bau-Auftrag (17.11.): drei Befunde der Nachprüfung Phase 2 – gehören zu Schritt E

Quelle: Meldung des Prüf-Chats (pruefung-phase2), wiedergegeben in inhalte/postfach/antworten.md, Abschnitt „Nachprüfung Phase 2“.

```text
Zusatz 4 zum Bau-Auftrag (Zweig bau-phase2), bitte zusammen mit Schritt E (M1–M9) erledigen. Die Nachprüfung von A2, K2, E-2 und E-3 meldet „erfüllt“ mit drei Befunden
(Wortlaut in inhalte/postfach/antworten.md, Abschnitt „Nachprüfung Phase 2 (A2, K2, E-2, E-3) und Winkelsätze“):
P1 „Kurz gesagt“: Bei funktionen.reihen hält die App „: 2.“ für eine Aufzählung und zeigt deshalb zwei Sätze. Die Aufzählungs-Ausnahme enger fassen (nur „1. …, 2. …“ am Satzanfang bzw.
   nach Komma/Strichpunkt, nicht nach Doppelpunkt mit einer einzelnen Zahl); der Test über alle Merksätze muss das abdecken.
P2 Mein Weg · Karte wählt die Orte nach block.ziel_klasse und beachtet die Schulart nicht; der Reiter „Stand“ rechnet mit jahrgang[schulart]. Bei RS- und IB-Kindern zeigen Karte und Stand
   deshalb unterschiedliche Orte. Die Karte nach derselben Regel wie „Stand“ auswählen (ein Ort gehört zur Klasse, wenn ein geplanter Flug dort jahrgang[schulart] = Stufe des Kindes hat).
P3 Flugplan: Wählt man den letzten offenen Flug eines Ortes ab, zählt der Stempel sofort (schule.ort_stand), der Ort wird aber nie „fertig“, weil das nur beim Abschluss eines Tests gesetzt wird –
   er bleibt „dran“, und die Sterne für den Ort fehlen. Lösung als Migration-Datei vorschlagen (nicht ausführen): api.schule_plan_setzen setzt nach dem Speichern jeden Ort des Plans auf „fertig“,
   dessen ort_stand „abgeschlossen“ meldet (der Trigger route_sterne bucht die Sterne dann einmal); umgekehrt wird ein Ort, der nur wegen abgewählter Flüge „fertig“ war, wieder „offen“,
   wenn ein nicht geschaffter Flug zurück in den Plan kommt.
```

# Achtzehnte Runde: Lücken laut Lehrplan schließen (Gymnasium)

Grundlage: Aufbau-Prüfung vom 14.11. (inhalte/pruefung/aufbau/klasse5.json … klasse10.json, Feld „luecken“). Ein Teil ist inzwischen erledigt (zahlen.natuerlich, zahlen.teilbarkeit, terme.umformen,
gleichungen.linear, geometrie.winkelsaetze, Bogenmaß in funktionen.trig, ergänzte Erklärschritte der Fünfzehnten Runde). Entscheidung Sebastian 17.11.: Lücken schließen.
Teil A: drei neue Flüge (ein Chat, Zweig luecken-neu). Teil B: fehlende Etappen in vorhandenen Flügen (ein Chat je Klasse, Zweige luecken-kl5 … luecken-kl10).

## Teil A – drei neue Flüge

```text
Du baust drei neue Themen („Flüge“) für eine Mathe-Lern-App (bayerisches Gymnasium, LehrplanPLUS).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig luecken-neu an und arbeite nur dort.
Lies zuerst vollständig: inhalte/README.md (Format, Regeln, „Verständliche Erklärungen“ mit „Vorgabe seit 16.11.“, „Zeichnungen“, „Vertiefung“), inhalte/postfach/README.md,
inhalte/vorlage_generator.py, in inhalte/AUFTRAEGE.md den Abschnitt „Zehnte Runde“ (Regeln für schwere Aufgaben und Prüfungsvorbilder, Urheberrecht) und in
inhalte/pruefung/aufbau/klasse6.json und klasse8.json die Einträge unter „luecken“ zu diesen drei Themen. Als Muster für Aufbau und Zeichnungen: inhalte/generatoren/geometrie.winkelsaetze.py
(neuester Flug, zweimal geprüft) und für Flächen/Körper inhalte/generatoren/messen.flaechen.py sowie messen.koerper_berechnung.py – deren Inhalte nicht wiederholen, sondern darauf aufbauen.

Die drei Themen (Nummern sind in der Datenbank schon angelegt – genau so verwenden):
1. messen.flaechen_vielecke – thema_id 99, block_id 114 (Quito), klasse {"gym_by": 6}, Titel „Flächen von Parallelogramm, Dreieck und Trapez“. LehrplanPLUS M6 2.1:
   Flächeninhalt von Parallelogramm, Dreieck und Trapez durch Zerlegen und Ergänzen herleiten und berechnen, zusammengesetzte Figuren, Oberfläche einfacher Körper. Ohne Zeichnung nicht sinnvoll (figur).
2. messen.volumen – thema_id 100, block_id 114 (Quito), klasse {"gym_by": 6}, Titel „Volumen“. LehrplanPLUS M6 2.2: Einheitswürfel, Quaderformel, Volumeneinheiten umrechnen
   (mm³ bis m³, Liter und Milliliter), zusammengesetzte Körper, Sachaufgaben.
3. messen.prisma_zylinder – thema_id 101, block_id 86 (Cusco), klasse {"gym_by": 8}, Titel „Prismen und Zylinder“. LehrplanPLUS M8 7: Volumen gerader Prismen (V = G · h) mit Begründung,
   Oberfläche, Zylinder-Volumen und -Oberfläche, Sachaufgaben. In messen.kreisberechnung gibt es schon eine Karte „zylinder“ – nicht verschieben, nicht wiederholen, sondern darauf verweisen und vertiefen.
Lies den Lehrplantext jeweils selbst nach (Websuche, lehrplanplus.bayern.de; Klasse 8 notfalls ISB-Material) und lege je Thema 6–8 Lernkarten fest, die letzte „verstehen/anwenden“.

Je Thema: Generator inhalte/generatoren/<thema_schluessel>.py schreibt inhalte/themen/<thema_schluessel>.json. Lernkarten im neuen Muster (einstieg, woerter, Bildergeschichte mit Zeichnung je Schritt,
fehler mit fehler_bild, regel mit erstem Satz ≤ 12 Wörter, probe). Je Lernkarte 18 Übungen (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8; davon mindestens 2 nach Prüfungsvorbild und 1 Knobelaufgabe),
1 Test, 3 Korrektur, 6 Sicherung. Lehren aus der Prüfung der Winkelsätze beachten: nichts verlangen, was im Lehrplan erst später kommt (in Klasse 6 keine Gleichungen mit x, in Klasse 8 kein Pythagoras);
bei Auswahl-Aufgaben darf keine „falsche“ Antwort ebenfalls richtig sein; Zeichnungen maßstäblich (angeschriebene und gezeichnete Maße stimmen, per Skript prüfen); jede Figur-Aufgabe mit Bild.
Eintrag je Thema in inhalte/themenliste.json (mit lehrplan_gym und reihenfolge innerhalb der Klasse).
Fertig je Thema, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet und du jede Aufgabe gelesen und nachgerechnet hast. Ein Thema = ein Commit + Push auf luecken-neu.
Grenzen: Keine Datenbank, kein App-Code, keine Tests, kein Merge, keine anderen Themen. Meldungen in inhalte/postfach/luecken-neu.md (Status je Thema, am Ende Abschlussbericht mit Quellen).
Arbeite ohne Rückfragen durch.
```

## Teil B – fehlende Etappen je Klasse (im Text `<N>` durch die Klasse ersetzen)

```text
Du schließt Lehrplan-Lücken in vorhandenen Themen einer Mathe-Lern-App (bayerisches Gymnasium, Klasse <N>). Die Themen sind für Kinder freigegeben.
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig luecken-kl<N> an und arbeite nur dort.
Lies zuerst vollständig: inhalte/README.md (Format, Regeln, „Verständliche Erklärungen“ mit „Vorgabe seit 16.11.“, „Zeichnungen“, „Vertiefung“), inhalte/postfach/README.md,
in inhalte/AUFTRAEGE.md die Abschnitte „Zehnte Runde“ (schwere Aufgaben, Prüfungsvorbilder, Urheberrecht) und „Fünfzehnte Runde“ (Arbeitsweise und Nachweis bei freigegebenen Themen),
und inhalte/pruefung/aufbau/klasse<N>.json – dort das Feld „luecken“ (was fehlt, Lehrplan-Bezug, wohin, Dringlichkeit).

Schritt 1 – Bestandsaufnahme: Die Liste ist vom 14.11.; seitdem ist vieles gebaut. Prüfe jeden Eintrag gegen den heutigen Stand (inhalte/themen, inhalte/themenliste.json) und schreibe ins Postfach
je Eintrag „erledigt (wo)“, „offen“ oder „nicht Teil dieses Auftrags“. Nicht Teil dieses Auftrags: neue Themen (messen.flaechen_vielecke, messen.volumen, messen.prisma_zylinder baut ein anderer Chat;
zahlen.natuerlich, zahlen.teilbarkeit, terme.umformen, gleichungen.linear, geometrie.winkelsaetze gibt es schon) und das Verschieben von Lernkarten zwischen Themen (nur melden).
Schritt 2 – jede offene Lücke schließen, Dringlichkeit „hoch“ zuerst: im Generator des genannten Themas eine neue Lernkarte an der unter „wohin“ genannten Stelle ergänzen (oder, wo „wohin“ das sagt,
eine vorhandene Karte um einen Schritt und Aufgaben erweitern). Prüfe den Lehrplan-Bezug selbst nach (Websuche, lehrplanplus.bayern.de). Neue Lernkarte im neuen Muster (einstieg, woerter,
Bildergeschichte mit Zeichnung je Schritt, fehler mit fehler_bild, regel mit erstem Satz ≤ 12 Wörter, probe) mit 18 Übungen (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8; mindestens 2 nach Prüfungsvorbild,
1 Knobelaufgabe), 1 Test, 3 Korrektur, 6 Sicherung. Steht der Stoff im Lehrplan der Klasse: Pflicht (bewertung.lernziele_pflicht); geht er darüber hinaus: Vertiefung.
Nichts verlangen, was im Lehrplan erst später kommt; bei Auswahl-Aufgaben darf keine „falsche“ Antwort ebenfalls richtig sein; Zeichnungen maßstäblich.
Regeln: Alle vorhandenen Lernkarten und Aufgaben bleiben Zeichen für Zeichen unverändert (Nachweis per Skript gegen origin/lernen-app: nur Neues kam dazu; wo eine vorhandene Karte erweitert wird,
ist genau diese Karte geändert). Neue Aufgaben in einem eigenen Abschnitt des Generators mit eigenem festen Zufallsstart. Ein Thema = ein Commit + Push auf luecken-kl<N>.
Fertig je Thema, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet, der Nachweis stimmt und du jede neue Aufgabe gelesen und nachgerechnet hast.
Grenzen: Keine Datenbank, kein App-Code, keine Tests, kein Merge. Meldungen in inhalte/postfach/luecken-kl<N>.md: zuerst die Bestandsaufnahme, dann je Thema eine Zeile,
am Ende ein Abschlussbericht (neue Lernkarten mit Lehrplan-Bezug und Quelle, erweiterte Karten, was offen blieb und warum). Arbeite ohne Rückfragen durch.
```

Einspielen (Haupt-Chat): Teil A als Entwurf importieren (einheit_importieren), prüfen lassen, Freigabe durch Sebastian; Quito danach in den Plan der Klasse 6 aufnehmen.
Teil B mit einheit_abgleichen(…, 'sperren') (Weg A); neue Etappen sind sofort sichtbar.

# Neunzehnte Runde: Gesamtdurchsicht der Stoffsammlung – je Klasse, dazu Realschule und IB

Auftrag Sebastian 17.11.: Jede Klasse geht ihre gesamte Stoffsammlung noch einmal durch – passen die Themen, sind die Erklärungen gut, einfach, schlüssig und mit Beispielen,
unterscheiden sich die Stufen der Bordkarten wirklich im Gedanken und nicht nur in der Größe der Zahlen. Mängel werden gleich behoben (in Grenzen), alles Übrige gemeldet.
Teil A: Gymnasium, ein Chat je Klasse (Zweige durchsicht-kl5 … durchsicht-kl10). Teil B: die 24 Realschul-/IB-Themen in zwei Chats (durchsicht-rsib-1, durchsicht-rsib-2).
Teil C: Abgleich aller Themen mit dem Realschul-Lehrplan und dem IB MYP (ein Chat, Zweig lehrplan-rsib, nur Vorschlag).

## Teil A – Gymnasium (im Text `<N>` durch die Klasse ersetzen)

```text
Du gehst die gesamte Stoffsammlung einer Mathe-Lern-App für Klasse <N> (bayerisches Gymnasium, LehrplanPLUS) kritisch durch und besserst nach. Die Themen sind für Kinder freigegeben.
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig durchsicht-kl<N> an und arbeite nur dort.
Lies zuerst vollständig: inhalte/README.md (Format, Regeln, „Verständliche Erklärungen“ mit „Vorgabe seit 16.11.“, „Zeichnungen“, „Vertiefung“), inhalte/postfach/README.md,
in inhalte/AUFTRAEGE.md die Abschnitte „Zehnte Runde“ (schwere Aufgaben, Prüfungsvorbilder, Urheberrecht), „Dreizehnte Runde“ und „Fünfzehnte Runde“ (Arbeitsweise und Nachweis bei freigegebenen
Themen) und die Berichte zu deiner Klasse in inhalte/postfach/ (schwer-kl<N>.md, befunde.md, luecken-kl<N>.md), damit du weißt, was schon geprüft und bewusst entschieden ist.
Deine Themen: alle Einträge in inhalte/themenliste.json mit klasse {"gym_by": <N>} (Datei inhalte/themen/<thema_schluessel>.json, Generator unter inhalte/generatoren/).
Lies den LehrplanPLUS Gymnasium Mathematik <N> selbst nach (Websuche, lehrplanplus.bayern.de). Sprache der App: „Flug“ = Thema, „Etappe“ = Lernkarte, „Bordkarte“ = Aufgabe.

Prüfe JEDES Thema vollständig – jede Lernkarte ganz, jede Aufgabe gelesen und nachgerechnet – in dieser Reihenfolge:
1. Passt das Thema? Stoff und Umfang gegen den Lehrplan der Klasse <N>: fehlt etwas, ist etwas zu viel oder gehört in eine andere Klasse? Stimmt die Reihenfolge der Lernkarten
   (jede baut nur auf vorher Erklärtem auf – auch über Themen hinweg, siehe Feld reihenfolge in der Themenliste)? Überschneidet es sich mit einem anderen Thema?
2. Erklärungen: Versteht ein Kind der Klasse <N> die Lernkarte allein, ohne Erwachsenen? Einfache Wörter, kurze Sätze, jedes Fachwort einmal erklärt. Ist sie schlüssig (kein Sprung, jeder Schritt
   folgt aus dem vorigen)? Hat sie ein vollständig vorgerechnetes Beispiel mit Zeichnung, das genau den Aufgabentyp der Karte zeigt, und eine typische Falle? Passt der Merksatz
   (erster Satz höchstens 12 Wörter)? Kommt in den Aufgaben etwas vor, das die Erklärung nicht zeigt?
3. Aufgaben: Lösung richtig, Frage eindeutig, bei Auswahl keine zweite richtige Antwort, Zeichnung stimmt mit den Zahlen, Tipp hilft ohne zu verraten, Lösungsweg nachvollziehbar.
4. Schwierigkeit – der wichtigste Punkt: Die drei Stufen müssen sich im GEDANKEN unterscheiden, nicht in der Größe der Zahlen.
   Stufe 1 = das vorgerechnete Beispiel mit anderen Zahlen (ein Schritt, direkt anwenden). Stufe 2 = mehrere Schritte, eine Einkleidung, eine kleine Abwandlung oder Umkehrung.
   Stufe 3 = ein anderer Gedanke: rückwärts denken, verknüpfen mit früherem Stoff, begründen oder Fehler finden, ungewohnte Einkleidung, Parameter statt Zahl, Prüfungsniveau.
   Schreibe je Lernkarte in einem Satz auf, worin sich ihre Stufen heute unterscheiden. Wo die Antwort „nur größere Zahlen“ oder „längere Rechnung“ lautet, ist das ein Mangel.
   Prüfe auch die Abwechslung: nicht dieselbe Aufgabe mit getauschten Zahlen in Reihe.

Nachbessern (im Generator des Themas, eigener Abschnitt; alles andere bleibt Zeichen für Zeichen gleich – Nachweis per Skript gegen origin/lernen-app):
 a) Falsche Stufe: nur das Feld s ändern. b) Fehler in Lösung, Tipp oder Lösungsweg bei gleicher Frage: berichtigen.
 c) Fehlerhafte, mehrdeutige oder bloß wiederholende Aufgabe: durch eine bessere ersetzen und den alten Fragetext unter „ersetzt“ melden (der Haupt-Chat sperrt die alte Fassung).
 d) Stufen ohne echten Unterschied: neue Aufgaben der fehlenden Art ergänzen, bis jede Lernkarte mindestens 4 Übungen je Stufe hat, die der Beschreibung oben entsprechen
    (für Stufe 3 gelten die Regeln der Zehnten Runde; Prüfungsvorbilder recherchieren, nie wörtlich übernehmen).
 e) Erklärung unklar, lückenhaft oder ohne passendes Beispiel: die Lernkarte verbessern (einstieg, woerter, schritte mit Zeichnung, fehler, regel, probe) – Längenregeln der README einhalten,
    Lernziel-Schlüssel, Titel und Reihenfolge der Lernkarten nicht ändern. Jede geänderte Lernkarte mit „vorher/nachher“ in einem Satz melden.
 Nicht selbst ändern, nur melden: Themen in eine andere Klasse schieben, Lernkarten löschen, teilen oder zwischen Themen verschieben, neue Themen, App-Wünsche.
Fertig je Thema, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet, der Nachweis stimmt und jede Lernkarte weiter mindestens 3 Übungen je Stufe hat.
Ein Thema = ein Commit + Push auf durchsicht-kl<N>.
Grenzen: Keine Datenbank, kein App-Code, keine Tests, kein Merge. Keine Namen oder Daten von Kindern. Keine Schulbuch- oder Prüfungsaufgaben wörtlich übernehmen.
Meldungen in inhalte/postfach/durchsicht-kl<N>.md: je Thema eine Zeile nach Abschluss; am Ende ein Abschlussbericht in einfacher Sprache mit
 (1) Urteil je Thema: Thema passt? Erklärungen? Stufen? – je mit einer Note von 1 bis 5 und einem Satz Begründung,
 (2) Tabelle je Lernkarte: worin sich die Stufen unterscheiden (vorher → nachher),
 (3) Zahlen: umgestuft, berichtigt, ersetzt, neu, Lernkarten verbessert,
 (4) Liste „ersetzt“ (alte Fragetexte je Thema),
 (5) Liste „für Sebastian“: was nicht passt und eine Entscheidung braucht (Thema in anderer Klasse, fehlender Stoff, Überschneidungen, App-Wünsche),
 (6) was du nicht prüfen konntest. Trenne Tatsachen, Annahmen und Meinung. Arbeite ohne Rückfragen durch.
```

## Teil B – Realschule und IB (24 Themen ohne Gymnasium-Klasse, bisher Entwurf)

Chat 1 (Zweig durchsicht-rsib-1): abbildungen.determinanten2, abbildungen.vektoren, daten.stichproben, funktionen.scharen, terme.quadratische_extreme, funktionen.transformation,
gleichungen.reinquadratisch, gleichungen.wurzel, abbildungen.matrizen, funktionen.umkehr, mengen.grundbegriffe, groessen.verhaeltnisse.
Chat 2 (Zweig durchsicht-rsib-2): daten.zweidimensional, daten.standardabweichung, stochastik.bedingt, funktionen.betrag, funktionen.folgen, funktionen.reihen, sonder.graphentheorie,
sonder.optimierung, daten.normalverteilung, finanzen.zinseszins, sonder.logik, zahlen.schranken.

```text
Du machst Themen einer Mathe-Lern-App für Realschule (Bayern) und IB MYP freigabereif. Die Themen sind Entwürfe: Kinder sehen sie noch nicht, es hängen keine Lernstände daran –
Lernkarten und Aufgaben dürfen deshalb geändert, ersetzt und ergänzt werden (Lernziel-Schlüssel, thema_id und block_id bleiben).
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig <ZWEIG> an und arbeite nur dort.
Deine Themen: <THEMEN>.
Lies zuerst vollständig: inhalte/README.md (Format, Regeln, „Verständliche Erklärungen“ mit „Vorgabe seit 16.11.“, „Zeichnungen“, „Vertiefung“), inhalte/postfach/README.md,
inhalte/postfach/umbau-rest.md (letzter Umbau dieser Themen), in inhalte/AUFTRAEGE.md die Abschnitte „Zehnte Runde“ (schwere Aufgaben, Prüfungsvorbilder, Urheberrecht) und
„Neunzehnte Runde, Teil A“ – die vier Prüfpunkte dort (Thema passt, Erklärungen, Aufgaben, Schwierigkeit im Gedanken statt in der Zahlengröße) gelten hier genauso.
Welche Klasse ein Thema in welcher Schulart hat, steht in inhalte/themenliste.json (rs_by = Realschule Bayern, ib_myp = IB MYP Jahr 1–5; MYP 1 entspricht etwa Klasse 6).
Lies zum Stoff den LehrplanPLUS Realschule Mathematik der genannten Klasse (lehrplanplus.bayern.de, Wahlpflichtfächergruppe I, wo unterschieden wird) bzw. für IB das MYP Mathematics Framework
(vier Bereiche: Zahl, Algebra, Geometrie und Trigonometrie, Statistik und Wahrscheinlichkeit; Standard und Extended) selbst nach. Das MYP legt den Stoff nicht je Jahr fest – schreibe dazu, wie sicher die Zuordnung ist.

Je Thema, vollständig (jede Lernkarte ganz, jede Aufgabe gelesen und nachgerechnet):
1. Die vier Prüfpunkte aus Teil A. Zusätzlich: Baut das Thema nur auf Stoff auf, der in dieser Schulart vorher dran war?
2. „Kurz gesagt“: erster Satz jedes Merksatzes höchstens 12 Wörter und 90 Zeichen (in diesen Themen sind laut Prüfung rund 100 zu lang) – kürzen, Rest der Regel bleibt inhaltlich.
3. Erklärungen nach dem Muster der Gymnasium-Themen nachziehen, wo sie dünner sind (vorgerechnetes Beispiel mit Zeichnung je Schritt, fehler mit fehler_bild).
4. Aufgaben: Mängel beheben; je Lernkarte am Ende mindestens 18 Übungen (Stufe 1: mindestens 4, Stufe 2: mindestens 6, Stufe 3: mindestens 8, davon 2 nach Prüfungsvorbild – z. B. Abschlussprüfung
   Realschule Bayern, Jahrgangsstufentests, IB-Aufgabenformate – und 1 Knobelaufgabe), dazu 1 Test, 3 Korrektur, 6 Sicherung. Vorhandene gute Aufgaben bleiben.
Fertig je Thema, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK ohne Hinweise meldet. Ein Thema = ein Commit + Push.
Grenzen: Keine Datenbank, kein App-Code, keine Tests, kein Merge, keine anderen Themen. Keine Schulbuch- oder Prüfungsaufgaben wörtlich übernehmen.
Meldungen in inhalte/postfach/<ZWEIG>.md: je Thema eine Zeile; am Ende Abschlussbericht wie in Teil A (Urteil je Thema mit Noten, Stufen-Tabelle, Zahlen, „für Sebastian“, nicht Geprüftes)
und je Thema „freigabereif: ja/nein“. Arbeite ohne Rückfragen durch.
```

## Teil C – Abgleich mit Realschul-Lehrplan und IB MYP (nur Vorschlag)

```text
Du prüfst für eine Mathe-Lern-App, ob alle Themen richtig den Klassen der Realschule Bayern und den Jahren des IB MYP zugeordnet sind, und was für diese Schularten noch fehlt.
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig lehrplan-rsib an und arbeite nur dort.
Lies zuerst: inhalte/README.md, inhalte/postfach/README.md, inhalte/themenliste.json (Felder klasse.rs_by, klasse.ib_myp, lehrplan_gym, reihenfolge), in inhalte/AUFTRAEGE.md den Abschnitt
„Elfte Runde“ und mit git show origin/daten-klassen:inhalte/pruefung/klassen/vorschlag.md den Vorschlag fürs Gymnasium – dein Ergebnis soll genauso aufgebaut sein.
Teil 1 – Realschule Bayern: Für JEDES Thema mit rs_by den Lernbereich und die Jahrgangsstufe im LehrplanPLUS Realschule Mathematik suchen (lehrplanplus.bayern.de, mit Websuche; wo die
 Wahlpflichtfächergruppen I und II/III sich unterscheiden, beide nennen und Gruppe I als Hauptfall nehmen). Tabelle: Thema · Klasse heute · Klasse laut Lehrplan · Lernbereich · Quelle (Adresse) ·
 Vorschlag (bleibt / ändern auf …). Dazu eine laufende Nummer in Lehrplan-Reihenfolge je Klasse (für das Feld reihenfolge.rs_by).
Teil 2 – Was fehlt der Realschule? Gehe den LehrplanPLUS Realschule Mathematik Klasse 5 bis 10 Lernbereich für Lernbereich durch und liste, was kein Thema der App abdeckt
 (was fehlt · Lehrplan-Bezug · wohin: vorhandenes Thema erweitern oder neues Thema · Dringlichkeit).
Teil 3 – IB MYP: Für jedes Thema mit ib_myp die Zuordnung zu MYP-Jahr und Bereich des Mathematics Framework prüfen (Standard oder Extended). Das MYP gibt keinen festen Stoff je Jahr vor –
 nenne deshalb je Thema, worauf sich das Jahr stützt (Framework, typische Schulcurricula, Lehrwerke mit Quelle) und wie sicher es ist (sicher / üblich / Annahme). Liste, was aus dem Framework
 (Standard, dazu Extended getrennt) fehlt. Vorschlag für reihenfolge.ib_myp nur, wo belegbar.
Nichts raten: ohne Beleg „kein Beleg gefunden“ schreiben. Ergebnis: inhalte/pruefung/klassen/vorschlag-rsib.md mit den Tabellen und einer kurzen Liste der Punkte, die Sebastian entscheiden muss.
Grenzen: KEINE Änderung an inhalte/themenliste.json, Generatoren, Datenbank, App-Code oder Tests – nur der Vorschlag. Kein Merge. Meldungen in inhalte/postfach/lehrplan-rsib.md.
Arbeite ohne Rückfragen durch.
```

Einspielen (Haupt-Chat): Teil A mit einheit_abgleichen(…, 'sperren') (Weg A) und Sperren der „ersetzt“-Fassungen; Teil B als Entwurf abgleichen ('loeschen'), Freigabe durch Sebastian;
Teil C ist Entscheidungsgrundlage (Klassen, Reihenfolge, neue Themen).
