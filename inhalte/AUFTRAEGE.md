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
