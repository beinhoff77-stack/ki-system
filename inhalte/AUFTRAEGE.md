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
Zusätzlich abarbeiten: die Befunde zu deiner Klasse aus der Prüfung der Achtzehnten Runde – inhalte/postfach/antworten.md, Abschnitt „Prüfung der Achtzehnten Runde Teil B“
(Klasse 5: zahlen.rechengesetze; Klasse 7: Geradengleichungen in abbildungen.kongruenz und geometrie.konstruktion, vierecke_ordnen; Klasse 9: Scheinlösung in gleichungen.quadratisch).
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

# Bau-Auftrag F (App, Prüfskript, Datenbank): echte Stufen sichtbar und erzwungen, Bonus-Bordkarten

Anlass (Sebastian 17.11.): Alle Durchsichten melden dasselbe – Stufe 2 oft dieselbe Rechnung wie Stufe 1, Stufe 3 mit Aufgaben der Stufe 2, dazu 3 bis 6 gleich gebaute Aufgaben hintereinander.
Bisher prüft nichts mechanisch, ob sich Stufen im Gedanken unterscheiden. Das wird jetzt Regel, Prüfung und Anzeige. Danach folgt die Inhalts-Runde „Zwanzigste Runde“.

```text
Du bist der Bau-Chat für die Lern-App „Lernen Schule“. Neuer Auftrag F.
Repository: beinhoff77-stack/ki-system. Hole den aktuellen Stand des Zweigs lernen-app und lege davon den Zweig bau-stufen an.
Lies zuerst: AGENTS.md, in inhalte/AUFTRAEGE.md die Abschnitte „Bau-Auftrag E-1“ (Arbeitsweise, Tests, Version, Grenzen – gelten unverändert) und „Bau-Auftrag F“, inhalte/README.md,
tools/inhalt_pruefen.py, und in inhalte/postfach/ zwei Abschlussberichte der Durchsicht (durchsicht-kl6.md, durchsicht-kl9.md auf den Zweigen origin/durchsicht-kl6 und origin/durchsicht-kl9),
damit du das Problem kennst.

1. Aufgabentyp je Bordkarte (Inhalt + Prüfskript + Datenbank)
 - Neues Feld „g“ je Aufgabe = Aufgabentyp („Gedanke“), ein kurzer Schlüssel aus fester Liste:
   Stufe 1: direkt (wie das Beispiel der Lernkarte, andere Zahlen) · erkennen (zuordnen, ablesen, benennen)
   Stufe 2: mehrschritt (zwei bis drei Rechenschritte) · einkleidung (Sachsituation, die direkt auf die Rechnung führt) · umkehr (gesuchte Größe ist eine andere als im Beispiel) · darstellung (Wechsel Tabelle/Bild/Term)
   Stufe 3: rueckwaerts (vom Ergebnis zur Ausgangsgröße über mehrere Schritte) · verknuepfen (braucht früheren Stoff dazu) · begruenden (Aussage prüfen, Gegenbeispiel) · fehler (Fehler in einer Rechnung finden und deuten)
            · transfer (ungewohnte Einkleidung, Modell selbst aufstellen) · parameter (Variable statt Zahl, „für welche a …“) · pruefung (Aufbau wie eine echte Prüfungsaufgabe)
   Bonus:   knobel (Wettbewerbsniveau, mehrere Ideen nötig)
 - inhalte/README.md: Abschnitt „Stufen und Aufgabentypen“ mit dieser Liste, je Typ ein Satz und ein Beispiel; Regel: Die Stufe folgt aus dem Typ, nicht aus der Größe der Zahlen.
 - tools/inhalt_pruefen.py: „g“ ist freiwillig (alte Aufgaben haben es nicht). Für Aufgaben MIT „g“ gilt als Fehler: unbekannter Typ; Typ passt nicht zur Stufe.
   Für Lernkarten, deren Übungen ALLE ein „g“ haben, zusätzlich als Fehler: weniger als 2 verschiedene Typen in Stufe 1, weniger als 3 in Stufe 2, weniger als 4 in Stufe 3;
   mehr als 2 Aufgaben desselben Typs je Stufe mit gleichem Satzbau (Fragetext nach Ersetzen aller Zahlen identisch). Als Hinweis für alle Lernkarten: Zahl der Übungen je Stufe mit „g“ / ohne „g“,
   und „gleich gebaut hintereinander“ (3 oder mehr Übungen derselben Lernkarte in Folge mit identischem Fragetext nach Ersetzen der Zahlen). Die Ausgabe nennt am Ende je Datei die Zahl solcher Gruppen.
 - Neuer Pool „bonus“ (Feld p): freiwillige Knobel-Bordkarte, zählt weder für „sitzt“ noch für Test; je Lernkarte höchstens 3; nur Typ knobel; Stufe 3. Prüfskript und README anpassen
   (Mengenregeln der anderen Pools bleiben).
 - Datenbank (Migration als Datei, nicht ausführen; Namensmuster 20261118_w150_f_*.sql; kein DROP, kein DELETE): Spalte schule.aufgabe.typ text; schule.aufgaben_einfuegen und
   schule.einheit_abgleichen übernehmen a->>'g' nach typ (beim Abgleich auch für vorhandene Aufgaben mit gleicher Frage); Pool „bonus“ zulassen (Prüfbedingungen, art); die Antworten an die App
   (Aufgabenliste der Einheit, Übung prüfen) liefern typ und bei Bonus-Bordkarten ein Kennzeichen; schule.karte_buchen zählt Bonus nicht (prüfen: tut es wegen pool <> 'uebung' schon nicht).
   Belohnung: richtige Bonus-Bordkarte im ersten Versuch = 30 Sterne (schule.sterne, Grund „bonus“, je Aufgabe einmal) und ein Zähler „Knobel-Sterne“ im Konto.

2. App – Kinderansicht
 - Stufe auf jeder Bordkarte zeigen: kleines Zeichen im Kopf der Bordkarte (● leicht · ●● mittel · ●●● schwer, mit Text für Vorleser). Kein Druck: keine rote Farbe, kein „zu schwer“.
 - Abwechslung: Die Auswahl der nächsten Bordkarte (waehleStufe in lernen.js) nimmt innerhalb der Ziel-Stufe nie zweimal hintereinander denselben Typ (Feld typ; fehlt es: nie zweimal
   hintereinander denselben Fragetext nach Ersetzen der Zahlen) und bevorzugt Typen, die das Kind in dieser Etappe noch nicht hatte. Die „schwere Bordkarte im ersten Versuch“ für „sitzt“
   bleibt Pflicht – wenn Typen vorhanden sind, zählt dafür nur eine Aufgabe mit Stufe-3-Typ (nicht eine umetikettierte leichte).
 - Bonus-Bordkarte: Wenn eine Etappe sitzt und es für sie Bonus-Bordkarten gibt, bietet die Landung „★ Knobel-Bordkarte (freiwillig)“ an; außerdem höchstens einmal je Lerntag auf der Abflugtafel
   („Knobeln des Tages“ aus einer sitzenden Etappe). Falsch kostet nichts und zeigt die Lösung mit Weg; richtig im ersten Versuch: 30 Sterne und ein Knobel-Stern, sichtbar im Reisepass
   („Knobel-Sterne: n“). Kein zweiter Versuch mit Punktabzug, kein Einfluss auf „sitzt“, Wiederholung oder Test. Ohne Migration/ohne Bonus-Aufgaben erscheint nichts davon.
 - Eltern/Lehrer: unter „Inhalte ansehen“ je Bordkarte Stufe und Typ; im Lernstand je Etappe „Knobel: x von y“.
 - Info-Seite „So funktioniert’s“ im selben Schritt anpassen (drei Stufen = drei Arten zu denken; Knobel-Bordkarten freiwillig).
Tests ergänzen (Stufenzeichen, keine zwei gleichen Typen hintereinander, Bonus-Angebot, Bonus zählt nicht für „sitzt“, Sterne). Version erhöhen, Commit + Push auf bau-stufen.
Meldung in inhalte/postfach/bau-stufen.md: zuerst „Teil 1 fertig“ (README, Prüfskript, Migration als Datei) – darauf warten die Inhalts-Chats –, dann „Teil 2 fertig“ (App).
Grenzen wie im Bau-Auftrag E-1: Datenbank nicht ausführen, kein Merge nach main oder lernen-app, keine Inhalte in inhalte/themen ändern. Arbeite ohne Rückfragen durch.
```

## Zusatz 1 zu Bau-Auftrag F (17.11., Wunsch von Sebastian): „Lernstand“ öffnet die Klassen-Übersicht

**Befund (Sebastian, mit Bildschirmfoto):** Die Seite „Stand über Schularten“ in der Kind-Ebene (Tabelle Kontinente × Klassen, z. B. „Kind A · Gymnasium“) ist für ihn *der* Lernstand. Man kommt aber nur über die kleine Karte „Stand über Schularten“ und dann über das Kind dorthin. Der Knopf „Lernstand“ an der Kinderkarte öffnet stattdessen „Was wackelt?“ – das erwartet er dort nicht.

**Auftrag (in Teil 2 mit erledigen, kein eigener Zweig):**
1. Der Knopf „Lernstand“ an jeder Kinderkarte (Eltern/Lehrer-Startseite) öffnet direkt die Kind-Ebene von „Stand über Schularten“ für dieses Kind, in seiner Schulart (Tabelle Kontinente × Klassen). Ein Klick, kein Umweg.
2. Diese Seite heißt in Titel und Kopfzeile „Lernstand <Name>“. Schulart-Umschalter, „Einstieg prüfen“ und der Weg in die Zelle (Flüge und Etappen) bleiben, wie sie sind.
3. Die bisherige Lernstand-Seite heißt überall „Was wackelt?“ und bekommt an der Kinderkarte einen eigenen Knopf „Was wackelt?“ neben „Lernstand“. Der Verweis von der Tabelle dorthin bleibt. Die Adresse `#/lernstand/<id>` zeigt künftig auf die Tabelle; „Was wackelt?“ bekommt eine eigene Adresse; alte Verweise in der App anpassen.
4. Die Vergleichsseite aller Kinder (Ebene 1) bleibt über die Karte erreichbar, heißt dort „Alle Kinder im Vergleich“.
5. Info-Seite („So funktioniert’s“) und der Satz „Frag Mama oder Papa – sie sehen im Lernstand, wo es hakt.“ im selben Schritt an die neuen Namen anpassen. Tests anpassen bzw. ergänzen (Klick auf „Lernstand“ zeigt die Tabelle des Kindes).
6. Keine Datenbank-Änderung nötig. Meldung wie gehabt in `inhalte/postfach/bau-stufen.md`.

# Zwanzigste Runde (Inhalte): echte Stufe 3 und Knobel-Bordkarten – je Klasse neu bauen

Voraussetzung: Bau-Auftrag F Teil 1 ist nach lernen-app zusammengeführt (Prüfskript kennt „g“ und Pool „bonus“) und die Neunzehnte Runde (Durchsicht) ist eingespielt.
Ein Chat je Klasse (Zweige stufen-kl5 … stufen-kl10). Im Text `<N>` durch die Klasse ersetzen.

```text
Du baust für eine Mathe-Lern-App (bayerisches Gymnasium, Klasse <N>) Bordkarten mit ECHTEN Unterschieden in der Schwierigkeit. Die Themen sind für Kinder freigegeben.
Repository: beinhoff77-stack/ki-system (lernen-app ist ein Zweig darin). Hole den aktuellen Stand des Zweigs lernen-app, lege davon den Zweig stufen-kl<N> an und arbeite nur dort.
Lies zuerst vollständig: inhalte/README.md – besonders „Stufen und Aufgabentypen“ (Feld g, Pool bonus) –, inhalte/postfach/README.md, in inhalte/AUFTRAEGE.md die Abschnitte „Zehnte Runde“
(Prüfungsvorbilder, Urheberrecht), „Fünfzehnte Runde“ (Arbeitsweise bei freigegebenen Themen) und „Bau-Auftrag F“ (Liste der Typen), und inhalte/postfach/durchsicht-kl<N>.md
(dort steht je Lernkarte, worin sich die Stufen heute unterscheiden und was gefehlt hat).
Deine Themen: alle Einträge in inhalte/themenliste.json mit klasse {"gym_by": <N>}.

Das Problem, das du löst: Die Aufgaben stammen aus Vorlagen mit Zufallszahlen. Dadurch war Stufe 2 oft die Rechnung von Stufe 1 mit anderen Zahlen, Stufe 3 enthielt Stufe-2-Aufgaben, und es kamen
3 bis 6 gleich gebaute Aufgaben hintereinander. „Schwer“ heißt ab jetzt: ein anderer Gedanke.

Je Lernkarte (jede Lernkarte jedes Themas):
1. Schreibe zuerst eine Stufen-Leiter in drei Zeilen: Was kann ein Kind auf Stufe 1, was muss es auf Stufe 2 zusätzlich können, welche neuen Gedanken verlangt Stufe 3? (kommt in den Bericht)
2. Gib JEDER vorhandenen Übung der Lernkarte ihren Typ (Feld g) nach der Liste in der README. Passt eine Aufgabe zu keinem Typ ihrer Stufe, stufe sie um (Feld s) – Frage und Antworten bleiben gleich.
3. Baue neue Übungen, bis die Lernkarte hat: Stufe 1 mindestens 4 (mindestens 2 Typen), Stufe 2 mindestens 6 (mindestens 3 Typen), Stufe 3 mindestens 8 mit mindestens 4 verschiedenen Typen
   aus rueckwaerts, verknuepfen, begruenden, fehler, transfer, parameter, pruefung – je Typ höchstens 3. Jede neue Aufgabe ist einzeln entworfen: eigener Satzbau, eigene Situation, eigener Gedanke.
   Zufallszahlen sind erlaubt, aber nicht mehrere Aufgaben aus derselben Vorlage. Für „pruefung“ echte Prüfungs- und Testaufgaben recherchieren (Websuche) und Typ und Niveau nachbauen, nie Wortlaut oder Zahlen.
4. Baue je Lernkarte 2 Knobel-Bordkarten (Pool bonus, Typ knobel): Wettbewerbsniveau (Känguru, Mathematik-Olympiade Schulrunde, Pangea als Vorbild für die ART der Aufgabe), mit dem Stoff der Lernkarte
   lösbar, aber erst mit einer eigenen Idee. Mit Tipp, der die Idee nicht verrät, und ausführlichem Lösungsweg. Wo eine Lernkarte dafür nichts hergibt, eine statt zwei und das begründen.
5. Übungen der Lernkarte, die danach überflüssig sind (dieselbe Vorlage zum vierten Mal), meldest du unter „überzählig“ mit Fragetext – nicht löschen; der Haupt-Chat sperrt sie.
6. Reihenfolge in der Datei: innerhalb einer Lernkarte nie zwei Aufgaben desselben Typs direkt hintereinander.
Regeln: Lösungen vom Programm berechnen und von Hand nachrechnen; Rechenausdruck „c“ muss die Aufgabe wirklich nachrechnen. Bei Auswahl darf keine zweite Antwort richtig sein.
Nichts verlangen, was im Lehrplan erst später kommt (Reihenfolge der Themenliste beachten). Zeichnungen maßstäblich. Lernkarten-Texte nicht ändern.
Alles, was du nicht ausdrücklich änderst, bleibt Zeichen für Zeichen gleich (Nachweis per Skript gegen origin/lernen-app: bei alten Aufgaben ändern sich nur g und gegebenenfalls s).
Fertig je Thema, wenn `python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json` OK meldet – ohne Fehler zu Typen und mit 0 Gruppen „gleich gebaut hintereinander“ – und du jede neue Aufgabe
gelesen und nachgerechnet hast. Ein Thema = ein Commit + Push auf stufen-kl<N>.
Grenzen: Keine Datenbank, kein App-Code, keine Tests, kein Merge. Keine Namen oder Daten von Kindern. Keine Schulbuch-, Prüfungs- oder Wettbewerbsaufgaben wörtlich übernehmen.
Meldungen in inhalte/postfach/stufen-kl<N>.md: je Thema eine Zeile; am Ende Abschlussbericht mit (1) Stufen-Leiter je Lernkarte, (2) Tabelle je Lernkarte: Übungen je Stufe und Typ vorher → nachher,
(3) Zahl neuer Übungen und Knobel-Bordkarten, (4) Liste „überzählig“, (5) Quellen der Prüfungsvorbilder, (6) drei Beispiel-Bordkarten je Stufe aus einer Lernkarte deiner Wahl im Wortlaut,
damit Sebastian den Unterschied sieht. Arbeite ohne Rückfragen durch.
```

Einspielen (Haupt-Chat): Migration F einspielen, dann einheit_abgleichen(…, 'lassen') je Thema (übernimmt typ und Stufe, fügt Neues ein); „überzählig“ sperren.

# Zwanzigste Runde – Zusatz Realschule und IB (17.11.): Typen, echte Stufe 3 und Knobel-Bordkarten für die 24 Themen ohne Gymnasium-Klasse

Entscheidung von Sebastian (17.11.): Die Realschul- und IB-Themen werden **nicht** zurückgestellt. Sie kommen in den Plan der Kinder (Ziel: nach Klasse 8 der Stand von Gymnasium, Realschule und IB). Dafür brauchen sie dieselbe Qualität wie die Gymnasium-Themen.

Es gelten **alle Regeln des Abschnitts „Zwanzigste Runde (Inhalte): echte Stufe 3 und Knobel-Bordkarten“** (Stufen-Leiter je Lernkarte, Feld `g` für jede Übung, Stufe 1 mindestens 4 Übungen aus 2 Typen, Stufe 2 mindestens 6 aus 3 Typen, Stufe 3 mindestens 8 aus 4 Typen, 2 Knobel-Bordkarten je Lernkarte, überzählige Übungen ohne `g` und im Bericht gelistet, drei Beispiel-Bordkarten je Stufe im Bericht). Statt „Klasse `<N>`“ gilt die Themenliste unten. Vorher `inhalte/README.md`, Abschnitt „Stufen und Aufgabentypen“, lesen.

Zwei Chats, je 12 Themen:

- **Chat 1 – Zweig `stufen-rsib-1`, Meldungen in `inhalte/postfach/stufen-rsib-1.md`:** abbildungen.determinanten2, abbildungen.vektoren, daten.stichproben, funktionen.scharen, terme.quadratische_extreme, funktionen.transformation, gleichungen.reinquadratisch, gleichungen.wurzel, abbildungen.matrizen, funktionen.umkehr, mengen.grundbegriffe, groessen.verhaeltnisse
- **Chat 2 – Zweig `stufen-rsib-2`, Meldungen in `inhalte/postfach/stufen-rsib-2.md`:** daten.zweidimensional, daten.standardabweichung, stochastik.bedingt, funktionen.betrag, funktionen.folgen, funktionen.reihen, sonder.graphentheorie, sonder.optimierung, daten.normalverteilung, finanzen.zinseszins, sonder.logik, zahlen.schranken

Zusätzlich je Thema im Bericht: (a) Welches Vorwissen aus anderen Flügen setzt das Thema voraus (Themenschlüssel nennen)? (b) Ab welcher Klasse kann ein Gymnasium-Kind das Thema frühestens lösen? Das brauche ich für die Einordnung in den Plan.

Ein Thema = ein Commit + Push. Kein Merge, keine Datenbank, kein App-Code, keine Tests.

# Einundzwanzigste Runde (17.11.): Bereinigen und Mindeststand je Jahrgang

Entscheidungen von Sebastian (17.11.): Reihenfolge-Fehler beheben · Überschneidungen **zusammenlegen** · Stoff über dem Lehrplan **verschieben** · Realschule gehört in den Plan: **Mindeststand je Jahrgang** (Gymnasium ist die Basis; hat die Realschule ein Thema früher, gilt die frühere Klasse).

Schon erledigt (Haupt-Chat): Lehrplan-Reihenfolge Klasse 9 (rationale Exponenten vor Potenzfunktionen; `trigo.allgemein` vor `gleichungen.trig`); drei neue Flüge freigegeben; Überzählige gesperrt.

## Teil A – Bereinigen (EIN Chat, Zweig `bereinigen`, Meldungen in `inhalte/postfach/bereinigen.md`)

Nur die Gymnasium-Themen (Klasse 5–10). Grundlage sind die Listen „Für Sebastian“ in `inhalte/postfach/durchsicht-kl5.md` … `durchsicht-kl10.md`. Regeln der Zwanzigsten Runde gelten weiter (jede Übung mit `g`, Mindestmengen 4 / 6 / 8, 2 Knobel-Bordkarten je Lernkarte, Prüfskript OK).

**A1 Zusammenlegen (derselbe Stoff steht in zwei Flügen):** Je Paar bleibt der Stoff an **einer** Stelle – dort, wo er laut Lehrplan zuerst gebraucht wird. An der anderen Stelle entfällt die Lernkarte oder wird zu einer kurzen Wiederholung mit Verweis. Die besten Aufgaben beider Stellen bleiben erhalten (keine doppelten Fragetexte). Paare:
- Kl. 5: `gleichungen.einfach` (umkehr_plus, umkehr_mal) ↔ `zahlen.ganz`/umkehraufgabe ↔ `zahlen.rechengesetze`/umkehraufgabe_mal · `messen.koerper_berechnung`/volumen (und die 7 Volumen-Aussagen in „verstehen“) ↔ `messen.volumen` (Kl. 6)
- Kl. 6: `zahlen.potenzen_zehner`/negativer_exponent ↔ `terme.potenzgesetze`/negativer_exponent · `finanzen.zinsen` ↔ `bruch.prozent`/zinsen
- Kl. 7: `geometrie.konstruktion` (parallelen, winkelsumme) ↔ `geometrie.winkelsaetze` (stufen_wechsel, innenwinkelsumme) · `daten.boxplot` ↔ `daten.kennwerte`
- Kl. 8: `groessen.indirekt` ↔ `funktionen.gebrochen` (indirekt, indirekt_sach) · `messen.koerper_darstellung` ↔ `raum.schraegbilder` (Schrägbild q = 1/2, Ecken/Kanten/Flächen) · `messen.kreisberechnung`/zylinder ↔ `messen.prisma_zylinder`
- Kl. 9: `funktionen.quadratisch`/nullstellen (Parabel–Gerade) ↔ Karte schnittpunkte
- Kl. 10: `funktionen.exponential_log`/zeitpunkt ↔ `gleichungen.exponential` (wachstum, mit_log_loesen) · π-Schätzung in `stochastik.mehrstufig`/simulation, `stochastik.mehrstufig`/pi_schaetzen, `stochastik.simulation`/monte_carlo · Schrägbild der Pyramide in `raum.schraegbilder`/pyramide ↔ `raum.pyramide_kegel_kugel`/pyr_volumen

**A2 Verschieben (Stoff steht früher als im Lehrplan oder wird vor seiner Erklärung geübt):** Die Lernkarte samt Aufgaben wandert in das passende Thema der richtigen Klasse. Gibt es dort keines, wird sie im alten Thema als Vertiefung geführt (`vertiefung`) – das dann im Bericht begründen.
- Kl. 5: `zahlen.teilbarkeit` – Neunerregel, ggT/kgV (M5 nennt nur 2, 3, 5, 10 und Primfaktoren) · `geometrie.ortslinien` – Schreibweise „y = 2“ · `geometrie.winkel`/uhr – 0,5° je Minute · `groessen.proportional`/erkennen – Begriff „proportional“
- Kl. 6: `terme.potenzgesetze` – Potenzgesetze und Variablen (M6 1.4 nennt sie nicht; M7 1.2 verlangt „Produkte und Potenzen von Potenzen“ → nach `terme.umformen`, Kl. 7) · `daten.kennwerte` – Modalwert, Spannweite, Median
- Kl. 7: `abbildungen.kongruenz`/achsenspiegelung – 21 Aufgaben und die Karte mit Geradengleichungen (x = 3, y = x): durch Fassungen ohne Geradengleichung ersetzen (Achse als Gitterlinie oder durch zwei Punkte) · `geometrie.konstruktion`/satz_kehrsatz – Satz des Thales vor `geometrie.kreis` · `abbildungen.kongruenz`/parkett – Innenwinkel vor `geometrie.winkelsaetze`
- Kl. 8: `gleichungen.formeln` – Körperformeln (Pyramide), die noch nicht dran waren
- Kl. 9: `stochastik.verknuepft`/bedingt – bedingte Wahrscheinlichkeit (Oberstufe) · `gleichungen.lgs3` – pruefen, stufenform, eliminieren (M9 2.2 verlangt nur einfache Beispiele) · `gleichungen.trig` – Aufgaben, die Stoff aus `trigo.allgemein` brauchen, sind jetzt richtig gereiht; prüfen, ob noch etwas vorgreift
- Kl. 10: `funktionen.ganzrational`/nullstellen – zwei Stufe-3-Übungen mit Substitution → nach `gleichungen.polynom`/substitution

**Pflicht im Bericht – Umzugstabelle:** je verschobener oder entfallener Lernkarte eine Zeile `altes Thema / alte Lernkarte → neues Thema / neue Lernkarte (oder „entfällt“, „Vertiefung“)`. Die brauche ich, um die Lernstände der Kinder in der Datenbank mitzunehmen. Lernkarten-Schlüssel (`l`) beim Umzug möglichst behalten. Themenschlüssel und `thema_id` nicht ändern, keine neuen Themen anlegen (falls eines nötig wäre: nur vorschlagen).
Ein Thema = ein Commit + Push. Kein Merge, keine Datenbank, kein App-Code, keine Tests. Bei Unklarheit: sinnvollste Lesart nehmen und im Bericht nennen.

## Teil B – Mindeststand je Jahrgang: Vorschlag für den Plan (EIN Chat, Zweig `plan-mindeststand`, nur Vorschlag)

Ziel: Ein Kind soll am Ende jeder Klasse mindestens den Stand von Gymnasium **und** Realschule Bayern haben; IB MYP läuft nebenbei mit (siehe Punkt 2). Ergebnis ist die Datei `inhalte/pruefung/klassen/vorschlag-mindeststand.md` – keine Änderung an Themenliste, Datenbank, App.

Grundlagen: `inhalte/themenliste.json` (Felder `klasse`, `reihenfolge`, `block_id`, `ort`), `inhalte/pruefung/klassen/vorschlag-rsib.md` (Lehrplan-Abgleich Realschule/IB mit Korrekturen), `inhalte/pruefung/klassen/vorschlag.md` (Klassenzuordnung der Orte, D1/D2).

1. **Plan-Klasse je Thema** (alle 95): Gymnasium-Klasse; ist die (nach `vorschlag-rsib.md` korrigierte) Realschul-Klasse kleiner, gilt sie; Themen ohne Gymnasium-Klasse: Realschul-Klasse; reine IB-Themen nach Punkt 2. Spalten: Thema · Gym · RS (alt → korrigiert) · IB · Plan-Klasse · Grund. Die sieben Klassen-Korrekturen und fünf Nachträge für `rs_by` aus `vorschlag-rsib.md` sind beschlossen.
2. **IB läuft nebenbei (Entscheidung Sebastian, 17.11.):** IB zieht **keinen** Gymnasium-Stoff nach vorn. Die Themen, die nur IB hat (keine Gymnasium- und keine Realschul-Klasse), werden sinnvoll auf die Jahrgangsstufen verteilt: nach Vorwissen und so, dass keine Klasse überladen wird (höchstens 2–3 zusätzliche IB-Flüge je Klasse). Die IB-Jahresangabe ist dabei nur ein Anhaltspunkt. Je Thema: vorgeschlagene Plan-Klasse, Vorwissen, Grund. Die vier Themen ohne Klasse (`daten.normalverteilung`, `finanzen.zinseszins`, `sonder.logik`, `zahlen.schranken`) ebenfalls einordnen. Zur Kenntnis (ohne Folge für den Plan): Liste der Gymnasium-Themen, die IB früher hat.
3. **Vorwissen prüfen:** Für jedes Thema, dessen Plan-Klasse kleiner ist als die Gymnasium-Klasse: Welche Themen setzt es voraus, und liegen die dann davor? Wo nicht: Thema lassen oder Voraussetzung mitziehen.
4. **Orte:** Für jedes Thema, dessen Ort (`ziel_klasse`) nicht zur Plan-Klasse passt, und für die 24 Themen ohne Gymnasium-Klasse (ihre Orte haben teils keine Klasse): Zielort vorschlagen (bestehender Ort derselben Klasse auf demselben Kontinent oder neuer Ort mit Stadt, Titel, Kontinent, Koordinaten). Kein Ort mit mehr als 4 Flügen.
5. **Reihenfolge je Klasse** über alle Themen der Plan-Klasse (Vorwissen zuerst), als Zahlenliste.
6. **Fehlender Realschul-Stoff** (aus `vorschlag-rsib.md`): je neuem Thema Titel, Plan-Klasse, Ort, 5–8 Lernkarten als Stichworte (Zentrische Streckung im Koordinatensystem, Vierecke und Drehung, Trigonometrie-Ergänzung Klasse 10, weitere).
7. **Folgen für zwei Kinder** (nur als Kind A, Klasse 5, und Kind B, Klasse 8): Wie viele Flüge kommen je Klasse dazu, wie viele liegen bei Kind B dann in schon abgeschlossenen Klassen?
Tatsachen, Annahmen und Meinungen trennen; Quellen nennen. Meldung in `inhalte/postfach/plan-mindeststand.md`.

# Bau-Auftrag G (Werkstatt-Wunsch 176): Motivation & Lernerfolg – P1 Punkteregel ohne Minuspunkte, P2 Mischkarten, P3 Expeditionen (Technik)

Von Sebastian freigegeben (17.11.2026). **Nicht neu verhandeln:** (1) Minuspunkte raus – Regel und Text. (2) 6 Aufgaben allein reichen nicht als Nachweis; die Regel unten gilt und wird nach dem Start an echten Daten überprüft. (3) Gemischte Aufgaben: vor allem Expeditionen, zusätzlich gemischte Reihenfolge. (4) P4–P7 kommen danach (nicht Teil dieses Auftrags).

**Rahmen:** Repository beinhoff77-stack/ki-system, Zweig `bau-motivation` (von aktuellem `lernen-app`). Es baut nur dieser eine Chat am App-Code. Die Datenbank ändert nur der Haupt-Chat: Migrationen als Datei nach `supabase/migrations/20261118_w176_<teil>_<name>.sql`, nicht ausführen; kein DROP von Tabellen, Spalten, Funktionen, kein DELETE; Lernstände dürfen nie verloren gehen. Lesen der Datenbank ist erlaubt. Keine Kindernamen, Schlüssel oder Zugangscodes in Code, Commits, Meldungen. Reisewörter gelten überall (Flug, Etappe, Bordkarte, Kontinent). Ändert sich eine Lernregel, wird die Info-Seite „So funktioniert’s“ und `inhalte/README.md` im selben Schritt angepasst. Tests: `tests/lernen.test.cjs` erweitern, alle grün. Kein Merge nach `lernen-app` oder `main`. Meldungen in `inhalte/postfach/bau-motivation.md` (neueste oben), nach jedem Teil „FERTIG: Teil n“ mit: was gebaut, welche Migration, welche neuen Felder für die App, was nicht geprüft werden konnte.

**Stand heute (wichtig, weicht von der ersten Spezifikation ab):** App 0.75.1 live. Migration F ist eingespielt: `schule.aufgabe.typ` ist für alle Übungen der 71 freigegebenen Flüge gesetzt (Typen: Stufe 1 direkt, erkennen · Stufe 2 mehrschritt, einkleidung, umkehr, darstellung · Stufe 3 rueckwaerts, verknuepfen, begruenden, fehler, transfer, parameter, pruefung · Bonus knobel); jede Etappe hat mindestens 4 / 6 / 8 freie Übungen auf Stufe 1 / 2 / 3 und Knobel-Bordkarten (Pool `bonus`, zählen nicht für „sitzt“). `schule.karte_buchen` (zuletzt geändert durch `20261118_w150_f_stufen_typ_bonus.sql`, davor `20261116_w150_sitzt_regel_6_mit_schwer.sql`): richtig im 1. Versuch ohne Tipp +1, Fehler −2 (mindestens 0), Tipp oder 2. Versuch 0; „sitzt“ bei `serie ≥ karte_ziel` (6; bei wenigen Aufgaben mindestens 2) und `schwer_ok`. Die App wählt die Bordkarte mit `lernWaehleBordkarte` (Stufe nach Punktestand, nie zwei gleiche Typen hintereinander).

Reihenfolge: **Teil 1 (P1) → Teil 2 (Format für P3) → Teil 3 (P2) → Teil 4 (P3 Technik).** Nach jedem Teil melden und auf den Haupt-Chat warten (Zusammenführen, Migration, Prüfung durch ChatGPT, „Live“ von Sebastian).

## Teil 1 – P1: Neue Punkteregel „gelandet“ / „sicher“ ohne Minuspunkte

**Regel „gelandet“** (intern bleibt `sitzt = true`). Alle Bedingungen müssen erfüllt sein:
1. `eigene_loesungen ≥ ziel` (6; bei wenigen freien Übungen wie bisher mindestens 2). Es zählt nur „richtig im 1. Versuch ohne Tipp“.
2. Darunter mindestens 2 verschiedene Aufgabentypen (`aufgabe.typ`), sofern die Etappe mindestens 2 Typen hat.
3. Darunter mindestens 1 Stufe-3-Aufgabe mit Stufe-3-Typ (wie `schwer_ok` heute), sofern vorhanden.
4. Die letzten 3 gewerteten Bordkarten in Folge richtig: `folge ≥ min(3, ziel)`.

**Fehler:** keine Abzüge. Endgültig falsch → `folge = 0`. Tipp oder 2. Versuch richtig → zählt nicht, `folge` bleibt unverändert.
**Stufensteuerung:** Die Stufe steigt mit den eigenen Lösungen (anteilig wie bisher) und fällt erst nach 2 endgültigen Fehlern in Folge um 1 – nicht nach jedem Fehler.
**Neue Felder in `schule.karte_stand` (Vorschlag):** `eigene_loesungen int`, `typen text[]`, `folge int`, `fehler_folge int`. `serie` bleibt für alte App-Fassungen lesbar oder wird ersetzt – entscheide und dokumentiere es. Die alte App (0.75.1) darf nach dem Einspielen der Migration nicht brechen, bis die neue live ist.
**Bestandsübernahme (in der Migration):** `eigene_loesungen = serie`; `folge = least(serie, 3)`; `typen` aus `schule.versuch` nachrechnen, wo möglich; **bereits sitzende Etappen bleiben sitzend**. Kein Lernstand geht verloren. In der Meldung: Zahlen vorher/nachher (Etappen sitzend, Summe der Punkte) – ohne Namen.

**„sicher“** (nur Anzeige, kein neuer Lernweg): gelandet + Wiederholungen bis zur Stufe „14 Lerntage“ bestanden + (sobald P2 live ist) mindestens 1 richtige Mischkarte + Nachtest des Flugs bestanden. Einen vorhandenen Status gesichert/„sicher“ nutzen; sichtbar machen für Kind und Eltern.

**App:**
- Den Satz „Ein Fehler kostet 2 Punkte“ ersatzlos streichen. Nach einem Fehler: Lösungsweg/Fehler-Detektiv wie bisher, Abschluss „Die nächste zählt wieder voll.“
- Fortschritt ehrlich und ohne Strafbild: Checkliste je Etappe, z. B. „Eigene Lösungen 4/6 · 2 Aufgabentypen ✓ · schwere ✓ · 3 in Folge: 1/3“. Nichts fällt sichtbar zurück außer „in Folge“.
- Getrennter Aktivitätszähler: „heute X Aufgaben selbst gelöst“ (ohne Bezug zur Schwelle).
- Kindertexte: „GELANDET“ bleibt; Zusatz „Sicher wird die Etappe, wenn du sie in ein paar Tagen wieder kannst.“
- Info-Seite („Wie wird gelernt?“), Eltern-Ansichten („Bordkarten bis sitzt“, „Was wackelt?“, Lernstand) und README anpassen. Nirgends mehr „−2“ oder „Punkte verlieren“.

**Tests:** Regel-Fälle als Rauchtest mit dem Testkind (in einer Transaktion, zurückgerollt; Skript in die Meldung): 6 richtige ohne Typvielfalt → nicht gelandet · 6 richtige, letzte falsch → nicht gelandet · Tipp-Treffer zählt nicht und bricht die Folge nicht · 2 Fehler in Folge senken die Stufe um 1, einer nicht · Etappe mit wenigen Aufgaben · Bestandsübernahme · Knobel-Bordkarte zählt weiter nicht. App-Tests erweitern.

## Teil 2 – Format für Expeditionen (nur README und Prüfskript, kein App-Code)

Damit die Inhalte-Chats früh anfangen können: lege das Dateiformat fest und beschreibe es in `inhalte/README.md` (Abschnitt „Expeditionen“) mit einem vollständigen Beispiel; erweitere `tools/inhalt_pruefen.py`.
- Datei je Expedition: `inhalte/expeditionen/<klasse>-<name>.json`, erzeugt von `inhalte/generatoren/expedition_<name>.py` (alle Lösungen vom Programm berechnet).
- Inhalt: Klasse, Titel, Einleitung/Kontext, optionale Grafik (die Zeichenarten der App: Koordinatensystem, Figur, Diagramme, Tabelle …), `voraussetzungen` = Liste `{thema_schluessel, lernziel}`, `teile` = 3–5 Teile mit Frage, Antworttyp (Zahl, Auswahl, Lücken, Markierung, Text – nur Formen, die die App schon prüft), Lösung, Rechenausdruck `c`, Lösungsweg, Bezug `{thema_schluessel, lernziel}`, optional Tipp. Folgeteile müssen mit der **richtigen** Lösung des Vorteils weiterrechnen können (kein Folgefehler-Domino): Der Text jedes Teils nennt die nötigen Werte.
- Prüfskript: Voraussetzungen existieren (Thema und Lernkarte in `inhalte/themen/`); jeder Teil nachgerechnet; Bezug jedes Teils steht in den Voraussetzungen; Klasse passt zu allen Voraussetzungen (Plan-Klasse des Themas ≤ Klasse der Expedition); keine doppelten Fragetexte; 3–5 Teile.
- Beispiel-Expedition „Handytarif“ (Klasse 8) als Datei mitliefern: a) Tarif A: 5 € + 0,10 €/min – Term aufstellen · b) Welcher Graph gehört zu A? (Auswahl aus 3 Graphen) · c) Ab wie vielen Minuten ist Tarif B (12 € Flat) günstiger? · d) B wird 15 % teurer – neue Antwort?
Melde „FERTIG: Teil 2“ – darauf setzen zwei Inhalte-Chats auf.

## Teil 3 – P2: Gemischte Reihenfolge (Mischkarten)

Ziel: Das Kind muss selbst erkennen, welches Verfahren passt. Keine Zusatzkarten, kein Pflicht-Tor – nur Umordnung der ohnehin anstehenden Übung. Dynamisch je Kind, unabhängig von der Plan-Reihenfolge: Quelle sind **nur Etappen, die bei diesem Kind sitzen** (gleiches Muster wie `api.schule_wiederholung`).

**Server** (neu, z. B. `api.schule_mischkarte` oder als Feld in einer bestehenden Aktion – keine neue Aktion in `lernen-api`, wenn es ohne geht; sonst melden):
- Kandidaten: sitzende Etappen des Kindes, außer der gerade geübten.
- Gewichtung: (1) gleicher Flug, (2) gleicher Kontinent bzw. verwechselbare Verfahren, (3) gelegentlich ein älterer Flug (z. B. jede 3. Mischkarte).
- Aufgabe: Pool `uebung`, Stufe 2–3, freigegeben, am seltensten gesehen (wie Wiederholung), **ohne** Etappen-Titel in der Anzeige. Entwürfe nur für das Testkind.

**Einsatz in der App:**
- Start erst, wenn im aktuellen Flug mindestens 3 Etappen sitzen.
- Jede 4. Bordkarte im normalen Üben ist eine Mischkarte; bei `lernender.klasse ≤ 6` jede 6. (Startwerte als Regel in `schule.regel`, später an Daten justieren).
- Kennzeichnung neutral: „Aus deiner Reise – erkennst du, was gefragt ist?“; nach der Lösung die Etappe nennen („Das war: Grundwert gesucht – Rom“).

**Wirkung:**
- Die Mischkarte zählt **nicht** für „gelandet“ der aktuellen Etappe.
- Richtig: Beleg „in Mischung erkannt“ für die Herkunftsetappe (neues Feld, z. B. `karte_stand.misch_ok_am`) → Bedingung für „sicher“ (Teil 1).
- Falsch: keine Abzüge; die Herkunftsetappe ist am nächsten Lerntag fällig (wie ein Fehler in der Wiederholung). Die Grenze „höchstens 6 Wiederholungen vor einem Flug“ bleibt.

**Tests:** keine Mischkarte bei weniger als 3 sitzenden Etappen · nur sitzende Etappen · Fehler → fällig · zählt nicht für die aktuelle Etappe · Dosis für Klasse ≤ 6 · Knobel-Bordkarten und gesperrte Aufgaben kommen nie als Mischkarte.

## Teil 4 – P3: Expeditionen (Technik)

- **Datenmodell** (du entscheidest und begründest): neue Tabelle `schule.expedition` (id, klasse, titel, einleitung, grafik, teile jsonb, voraussetzungen jsonb, status entwurf/geprueft/freigegeben, version) **oder** eigener Pool in `schule.aufgabe` mit Teil-Gruppe. Versuche je Teil in `schule.versuch` (Bezug auf den Teil). Import-Funktion für die Dateien aus Teil 2 (wie `einheit_importieren`/`einheit_abgleichen`: neu anlegen, abgleichen, nichts löschen).
- **Auswahl dynamisch je Kind:** Eine Expedition wird nur angeboten, wenn **alle** Voraussetzungs-Etappen beim Kind sitzen. Plan-Reihenfolge egal. Entwürfe sieht nur das Testkind.
- **Ablauf:** Jeder Teil wird einzeln geprüft; bei Fehler ein 2. Versuch, dann Lösung zeigen und mit dem nächsten Teil auf Basis der richtigen Lösung weitermachen. Keine Minuspunkte. Teil richtig im 1. Versuch → Beleg „in neuer Aufgabe angewandt“ für die betroffene Etappe (Feld vorsehen, Anzeige kommt mit P5). Teil falsch → betroffene Etappe am nächsten Lerntag fällig (wie Teil 3).
- **Platz in der Reise:** am Ende eines Flugs bzw. nach 2–3 Flügen als „Expedition“ mit eigenem Stempel; angeboten, nie erzwungen; zählt nicht für „gelandet“. Sterne: Vorschlag machen (Regel in `schule.regel`), nicht höher als ein Ort.
- **Grafik:** Die App zeichnet (vorhanden). Das Kind kann ablesen, einen Graphen auswählen, einen Punkt bestimmen – selbst zeichnen geht nicht.
- **Eltern/Lehrer:** Expeditionen in „Inhalte ansehen“ lesbar; im Lernstand je Kind: angeboten / begonnen / geschafft.
- **Tests:** keine Expedition ohne alle Voraussetzungen · Folgeteil nach Fehler nutzbar · Belege und Fälligkeit richtig · Entwurf nur Testkind · Abbruch mitten in der Expedition verliert nichts.

# Zweiundzwanzigste Runde (18.11., Auftrag des Lehrers): mehr Textaufgaben in Klasse 8

**Befund des Lehrers (von Sebastian weitergegeben):** In Klasse 8 sind zu wenig Textaufgaben. Zählung heute: Von 1 907 freien Übungen der 14 Themen mit Gymnasium-Klasse 8 sind 286 vom Typ `einkleidung` oder `transfer` (15 %; je Thema 10–20 %). Weitere Sachaufgaben stecken in anderen Typen, sind aber nicht gezählt.

**Ein Chat, Zweig `text-kl8` (von aktuellem `lernen-app`), Meldungen in `inhalte/postfach/text-kl8.md`.** Themen: alle mit `klasse.gym_by = 8` in `inhalte/themenliste.json` (funktionen.grundbegriffe, funktionen.linear, zahlen.intervalle, gleichungen.ungleichungen, groessen.indirekt, funktionen.gebrochen, terme.bruchterme, gleichungen.bruch, gleichungen.formeln, stochastik.grundbegriffe, gleichungen.lgs2, messen.kreisberechnung, messen.koerper_darstellung, messen.prisma_zylinder). Vorher `inhalte/README.md` lesen (Themen-Bausatz, „Stufen und Aufgabentypen“).

**Was eine Textaufgabe hier ist:** eine Sachsituation in ganzen Sätzen, aus der das Kind selbst herauslesen muss, was gegeben und was gesucht ist, und die es in Mathematik übersetzt (Term, Gleichung, Funktion, Skizze), löst und im Sachzusammenhang beantwortet. Nicht: eine Rechenaufgabe mit einem Einleitungssatz davor.

**Ziel je Lernkarte (freie Übungen, Pool `uebung`):**
- Mindestens **8 Textaufgaben**: Stufe 1 mindestens 1 (kurze Situation, ein Schritt), Stufe 2 mindestens 3, Stufe 3 mindestens 4.
- Über das ganze Thema mindestens **40 %** der Übungen mit `g` sind Textaufgaben.
- Ausnahme: Lernkarten, bei denen eine Sachsituation fachlich unsinnig wäre (reine Schreibweisen, Begriffe). Dann so viele wie sinnvoll und im Bericht begründen.
- Pool `sicherung`: mindestens 2 der 6 Aufgaben je Lernkarte sind Textaufgaben. Pool `korrektur`: mindestens 1 von 3. Test unverändert, außer die Testaufgabe ist fachlich schwächer als eine neue Textaufgabe.

**Qualität:**
- Lebenswelt von 13- bis 14-Jährigen und Reise-/Alltagsbezug (Tarife, Fahrpläne, Rezepte, Sport, Taschengeld, Baupläne, Messwerte, Karten und Maßstab). Realistische Zahlen und Einheiten. Keine Namen realer Personen, keine Marken.
- Abwechslung im Satzbau und in der Situation: je Lernkarte keine zwei Textaufgaben mit derselben Geschichte.
- Auf Stufe 2 und 3 mehrschrittig; auf Stufe 3 mindestens zwei je Lernkarte mit **einer** dieser Hürden: überflüssige Angabe · fehlende Angabe, die aus dem Text erschlossen werden muss · Ergebnis muss gedeutet oder gerundet werden (z. B. „wie viele Busse“) · zwei Bedingungen · Antwort ist eine Entscheidung mit Begründung (als Auswahl).
- Typen: Stufe 1 `direkt`/`erkennen` in kurzer Situation · Stufe 2 `einkleidung` (auch `umkehr`, `darstellung` mit Tabelle/Diagramm im Sachzusammenhang) · Stufe 3 `transfer`, `pruefung`, `verknuepfen`, `rueckwaerts`, `fehler`, `begruenden` im Sachzusammenhang.
- Vorbild für Niveau und Form: Bayerischer Mathematik-Test 8 und Jahrgangsstufenarbeiten (ISB) – nur Typ und Niveau, eigene Zahlen und Einkleidung, nichts wörtlich übernehmen.
- Lösungsweg `w` in Schritten: gegeben · gesucht · Ansatz · Rechnung · Antwortsatz. Tipp `h` hilft beim Übersetzen („Was kostet eine Minute? Was kommt einmalig dazu?“), verrät nicht die Rechnung.
- Alle Lösungen rechnet der Generator; Rechenausdruck `c` Pflicht bei Zahl und Lücken.

**Regeln der Zwanzigsten Runde gelten weiter:** jede freie Übung hat `g`; Mindestmengen 4 / 6 / 8; mindestens 2 / 3 / 4 Typen je Stufe; auf Stufe 3 je Typ höchstens 3 mit gleichem Satzbau; 2 Knobel-Bordkarten je Lernkarte bleiben. Werden durch die neuen Textaufgaben alte reine Rechenaufgaben überzählig, verlieren sie ihr `g` (sie werden beim Einspielen gesperrt, nicht gelöscht) – im Bericht je Lernkarte zählen. Alte Aufgaben sonst nicht ändern (Fragetext und Antworten Zeichen für Zeichen gleich, damit Lernstände erhalten bleiben).

**Bericht:** Tabelle je Lernkarte: Textaufgaben vorher → nachher je Stufe, neue Aufgaben, überzählig; Anteil je Thema; je Thema drei Beispiel-Textaufgaben (je Stufe eine) im Wortlaut; Lernkarten mit Ausnahme und Grund; was nicht geprüft wurde. Ein Thema = ein Commit + Push. Kein Merge, keine Datenbank, kein App-Code, keine Tests.

# Expeditionen (Werkstatt-Wunsch 176, P3) – Inhalte für Klasse 5 und Klasse 8

Voraussetzung erfüllt: Das Format steht in `inhalte/README.md`, Abschnitt „Expeditionen“ (mit vollständigem Beispiel `inhalte/expeditionen/8-handytarif.json`, Generator `inhalte/generatoren/expedition_handytarif.py`); `tools/inhalt_pruefen.py` prüft Expeditionen.

**Idee:** Eine Aufgabe wie in einer Schulaufgabe mit a), b), c), d): eine Situation, 3–5 Teile, jeder Teil aus einem **anderen** Thema (z. B. Term aufstellen · Graph zuordnen · Gleichung lösen · Prozent rechnen). Das Kind bekommt eine Expedition nur angeboten, wenn alle Voraussetzungs-Etappen bei ihm sitzen.

**Zwei Chats:** Klasse 5 → Zweig `expedition-kl5`, Meldungen `inhalte/postfach/expedition-kl5.md` · Klasse 8 → Zweig `expedition-kl8`, Meldungen `inhalte/postfach/expedition-kl8.md`. Je etwa **10 Expeditionen**.

**Regeln:**
- Je Expedition ein Generator `inhalte/generatoren/expedition_<name>.py`, der `inhalte/expeditionen/<klasse>-<name>.json` schreibt. Alle Lösungen berechnet das Programm, nichts wird abgeschrieben. Realistische Zahlen, keine Namen realer Personen, keine Marken. Keine Schulbuch- oder Prüfungsaufgaben wörtlich übernehmen.
- `voraussetzungen` = Liste `{thema_schluessel, lernziel}`; nur Lernkarten, die es in `inhalte/themen/` gibt; Plan-Klasse jedes Themas ≤ Klasse der Expedition. Jeder Teil hat einen `bezug` aus dieser Liste.
- Mindestens **3 verschiedene Themen** je Expedition, möglichst aus verschiedenen Gebieten (Zahlen, Größen, Geometrie, Daten, Funktionen, Gleichungen …). Die ersten fünf Expeditionen je Klasse nutzen nur Themen, die im Plan früh kommen (Klasse 5: Flüge der Orte Rom, Kairo, Timbuktu, Athen, Toronto; Klasse 8: funktionen.grundbegriffe, funktionen.linear, gleichungen.ungleichungen, groessen.indirekt und Stoff aus Klasse 5–7); die übrigen dürfen den ganzen Stoff bis zur Klasse nutzen.
- **Kein Folgefehler-Domino:** Jeder Teil nennt die Werte, die er braucht – auch wenn sie das Ergebnis eines Vorteils sind.
- Antwortformen nur, die die App prüft (Zahl, Auswahl, Lücken, Markierung …, siehe README). Wo es passt, eine Grafik (Koordinatensystem, Diagramm, Tabelle, Figur): ablesen, zuordnen, Punkt bestimmen – nichts, was das Kind zeichnen müsste.
- Schwierigkeit steigt von a) nach d); der letzte Teil verlangt eine Deutung oder Entscheidung im Sachzusammenhang. Lösungsweg je Teil in Schritten, Tipp je Teil.
- Themenmischung über die 10 Expeditionen: Jedes früh liegende Thema kommt mindestens zweimal vor; keine zwei Expeditionen mit derselben Geschichte.
- Prüfwerkzeug muss für jede Datei OK melden. Eine Expedition = ein Commit + Push. Kein Merge, keine Datenbank-, App- oder Server-Änderung.
- Bericht: Tabelle Expedition · Situation · Teile mit Thema/Lernkarte · Antwortformen · Grafik; je Expedition der Wortlaut eines Teils; was nicht geprüft wurde (z. B. wie die App die Grafik zeichnet).

# Dreiundzwanzigste Runde (18.11.): Was an den 24 Realschul-/IB-Themen ist wirklich neu? (nur Prüfung und Vorschlag)

**Anlass (Sebastian):** „Die lernen doch grundsätzlich dasselbe Mathe – warum so viele neue Themen?“ Der Vorschlag `inhalte/pruefung/klassen/vorschlag-mindeststand.md` plant alle 24 Themen ohne Gymnasium-Klasse als zusätzliche Flüge ein. Vermutung: Ein großer Teil davon steckt schon in Gymnasium-Flügen und wäre doppelt.

**Ein Chat, Zweig `doppelt-pruefen`, Ergebnis `inhalte/pruefung/klassen/doppelt-rsib.md`, Meldung in `inhalte/postfach/doppelt-pruefen.md`.** Nur lesen und vorschlagen: keine Änderung an Themendateien, Themenliste, Datenbank oder App. Kein Merge.

**Die 24 Themen** (alle in `inhalte/themenliste.json` ohne `klasse.gym_by`): abbildungen.determinanten2, abbildungen.vektoren, abbildungen.matrizen, daten.stichproben, funktionen.scharen, terme.quadratische_extreme, funktionen.transformation, gleichungen.reinquadratisch, gleichungen.wurzel, funktionen.umkehr, mengen.grundbegriffe, groessen.verhaeltnisse, daten.zweidimensional, daten.standardabweichung, stochastik.bedingt, funktionen.betrag, funktionen.folgen, funktionen.reihen, sonder.graphentheorie, sonder.optimierung, daten.normalverteilung, finanzen.zinseszins, sonder.logik, zahlen.schranken.

**Arbeit je Thema – Lernkarte für Lernkarte** (Feld `l`, Titel und Merksatz in `lernkarten`, dazu Stichproben der Aufgaben), verglichen mit **allen 71 Gymnasium-Themen** in `inhalte/themen/`:
1. Steht derselbe Stoff schon in einem Gymnasium-Flug? Dann: Thema/Lernkarte nennen und belegen (Titel, zwei Beispielaufgaben beider Seiten im Wortlaut).
2. Einordnung jeder Lernkarte in genau eine Gruppe:
   - **A – schon da:** Gymnasium-Flug deckt es ab → entfällt als eigener Stoff.
   - **B – kleiner Zusatz:** passt als eine Lernkarte (oder ein paar Aufgaben) in einen bestehenden Gymnasium-Flug → Zielthema, Stelle in der Reihenfolge, Klasse nennen; als Vertiefung oder Pflicht?
   - **C – wirklich neu:** kein Gymnasium-Flug enthält es → bleibt eigener Stoff.
3. Urteil je Thema: **auflösen** (alles A/B) · **verkleinern** (Rest-Flug nur aus C-Karten, mindestens 3 Lernkarten, sonst in ein anderes Thema) · **bleibt** (überwiegend C).
4. Für jedes Thema, das bleibt oder verkleinert wird: für wen ist es Pflicht? Realschule alle Zweige · nur Realschule Wahlpflichtgruppe I (mathematischer Zweig) · nur IB (Standard oder Extended) · keines (Zusatz). Mit Lehrplanstelle (LehrplanPLUS Realschule Bayern, Jahrgangsstufe und Lernbereich; IB Mathematics guide/Lehrwerk wie in `vorschlag-rsib.md`). Vorschlag für Plan-Klasse und Ort.
5. Gegenprobe in die andere Richtung: Gibt es Stoff, den Realschule (alle Zweige) oder IB bis Jahr 4 verlangen und der in **keinem** Flug steht? (Abgleich mit `vorschlag-rsib.md`, Teil 2 und „Was aus dem Framework fehlt“.) Die vier dort vorgeschlagenen neuen Themen ebenso einordnen: wirklich nötig oder als Lernkarten in bestehende Flüge?

**Ergebnisdatei:** Kurzfassung oben (Zahl der Themen je Urteil; Zahl der Flüge, die Kind A und Kind B danach zusätzlich hätten – nur als Kind A, Klasse 5, und Kind B, Klasse 8); Tabelle aller 24 Themen (Urteil, Pflicht für wen, Plan-Klasse); je Thema die Lernkarten-Tabelle mit Gruppe A/B/C und Beleg; Liste „Für Sebastian zu entscheiden“ (z. B. ob der mathematische Realschul-Zweig abgedeckt werden soll). Tatsachen, Annahmen und Meinungen trennen; sagen, was nicht geprüft wurde. Keine Schulbuch- oder Prüfungsaufgaben wörtlich übernehmen.

# Bau-Auftrag H (Werkstatt-Wunsch 176): Befunde aus der Prüfung von ChatGPT zu Teil 1 (Punkteregel) – vier „muss“, drei „sollte“

Quelle: Werkstatt-Nachricht 843 (Prüfergebnis ChatGPT zur Prüfbitte 841, Stand Commit 09fb5cd, mit lesender Prüfung der Live-Funktionen). Urteil dort: Grundidee und zentrale Mechanik stimmen, die Abnahme ist wegen vier Punkten **nicht** erteilt. Der Haupt-Chat hält alle vier für berechtigt.

**Rahmen wie Bau-Auftrag G:** Zweig `bau-motivation` (vorher aktuellen Stand von `lernen-app` holen); Migrationen nur als Datei nach `supabase/migrations/20261119_w176_h_<name>.sql`, nicht ausführen; kein DROP, kein DELETE; Lernstände dürfen nicht verloren gehen; bereits gelandete Etappen bleiben gelandet; Info-Seite und `inhalte/README.md` im selben Schritt; Tests erweitern; kein Merge. Meldung „FERTIG: Auftrag H“ in `inhalte/postfach/bau-motivation.md` mit Zahlen vorher/nachher (ohne Namen) und einer Antwort je Punkt, die der Haupt-Chat an ChatGPT weitergeben kann.

## Muss

**H1 – Wieder geöffnete Etappe wird weiter als „gelandet/fertig“ behandelt.** Setzt `karte_buchen` nach zwei endgültig falschen Wiederholungen `sitzt = false`, bleibt `schule.etappen_stand.fertig` trotzdem `true`, sobald `schule.lernziel_stand.status` vorher `nachgewiesen/korrigiert/gesichert` war (`fertig = k.sitzt OR s.status IN (…)`); `karte_buchen` korrigiert `lernziel_stand` nicht. In `lernen.js` zusätzlich `e.fertig = e.fertig || r.karte.sitzt` (bleibt nach `sitzt = false` stehen). Folge: Abflugtafel, Etappe, Elternblick und Testsperre können ein falsches „gelandet“ zeigen.
→ Wiederöffnen in allen Statusfeldern einheitlich wirksam machen; einen früher bestandenen Test getrennt führen bzw. kennzeichnen statt ihn „fertig“ erzwingen zu lassen; die App berechnet den Status aus der aktuellen Serverantwort neu (kein „oder“ mit dem alten Wert). Durchgehender Test mit dem Testkind: gelandet → Flugtest → 2 fällige Wiederholungen falsch → nicht gelandet in Abflugtafel, Etappe, Elternblick und Testsperre → 3 neue eigene Lösungen in Folge → wieder gelandet.

**H2 – Die Bestandsübernahme hat „drei in Folge“ aus der alten Netto-Punktzahl erfunden** (`folge = least(serie, 3)`). `serie` war vor Teil 1 eine Netto-Zahl mit Abzügen und sagt nichts über die letzten drei Bordkarten.
→ Für **noch offene** Etappen die Folge aus den zeitlich geordneten endgültigen Versuchen (`schule.versuch`) nachrechnen; wo das nicht eindeutig geht, mit 0 beginnen. `eigene_loesungen` bleibt, `sitzt = true` bleibt unberührt. Die Korrektur betrifft nur Zeilen aus der Übernahme vom 17.11., deren `folge` seither nicht durch neue Versuche überschrieben wurde – sauber abgrenzen und in der Meldung zählen. Test: letzter alter Versuch falsch; alte Tipp-/Zweitversuch-Treffer; danach normales Landen.

**H3 – Dieselbe Aufgabe zählt beliebig oft als „eigene Lösung“.** `karte_buchen` prüft nicht, ob die `aufgabe_id` schon für den Nachweis gezählt wurde; der Rauchtest wiederholt sogar sechsmal dieselbe schwere Aufgabe.
→ Für den Nachweis zählen nur **verschiedene** Aufgaben: Eine Aufgabe, die für diese Etappe schon als eigene Lösung gezählt hat, zählt beim nächsten Mal nicht noch einmal für `eigene_loesungen`, Typen und „schwere“ (für „in Folge“ darf sie zählen – Vorschlag; entscheide und begründe). Wiederholtes Üben bleibt erlaubt und wird freundlich benannt („Die kennst du schon – gut wiederholt.“), ohne Strafbild. Regel für die Zeit nach einem Wiederöffnen (H1) festlegen: Vorschlag – Aufgaben zählen wieder, wenn seit ihrer letzten Zählung mindestens ein Lerntag vergangen ist. Die App wählt ohnehin die am seltensten gesehenen Aufgaben; sicherstellen, dass sie innerhalb einer Etappe keine schon gezählte Aufgabe zeigt, solange es ungezählte gibt (jede Etappe hat mindestens 18 freie Übungen). Rauchtest entsprechend umbauen.

**H4 – „Sicher“ ist kein verlässlicher Nachweis für die einzelne Etappe.** `karte_sicher` verlangt irgendeinen bestandenen Flug-Nachtest derselben Einheit – nicht, dass die Aufgabe dieser Etappe im Nachtest richtig war, und nicht, dass der Nachtest **nach** der letzten (Neu-)Landung lag.
→ „Sicher“ nur, wenn die Bordkarte dieser Etappe im Nachtest richtig war und der Nachtest nach der letzten Landung der Etappe stattfand; sonst ehrlich als „Flug-Nachtest bestanden“ anzeigen. Tests: Nachtest mit 80 % bestanden, aber diese Etappe falsch → nicht sicher; alter bestandener Nachtest, danach Rückfall und Neu-Landung → nicht sicher.

## Sollte

**H5 – Rauchtest-Lücken:** Der Test ruft `karte_buchen` direkt auf und setzt `sitzt` künstlich. Ergänzen als zurückgerollte Durchläufe über die echten Wege (`uebung_pruefen_intern`, Trigger `versuch_karte`): erster Fehler → zweiter Versuch; 2 falsche Wiederholungen → offen → wieder gelandet; „sicher“; Bestandsübernahme der Folge; doppelte Aufgabe; Etappe mit wenigen Übungen als echter Fall statt Hinweis.
**H6 – „heute X Aufgaben selbst gelöst“:** Der Tageswechsel liegt in UTC (`new Date().toISOString().slice(0, 10)`), in Adelaide also am Vormittag. Auf den lokalen Tag des Kindes umstellen (Zeitzone des Kindes aus `lernender.zeitzone`) oder aus den bestätigten Versuchen des Lerntags zählen (dann geräteunabhängig – bevorzugt).
**H7 – Texte:** Tipp-Hinweis sagt noch „zählt nicht für die Serie“ → „zählt nicht als eigene Lösung; unterbricht deine Folge nicht“. Überall prüfen, dass „Serie“ und „Punkte“ aus den Kinder- und Elterntexten verschwunden sind.

## Bau-Auftrag H, Teil 2: Befunde aus der Prüfung von ChatGPT zu Teil 3 (Mischkarten) und Teil 4 (Expeditionen) – Werkstatt-Nachricht 848

Stand der Prüfung: `main`, App 0.78.1, Live-Funktionen lesend geprüft. Urteil: technisch vorhanden, noch nicht vorbehaltlos freigabereif. Der Haupt-Chat nimmt alle Punkte an. **Reihenfolge: H8 zuerst** (wirkt schon heute bei den Kindern, weil Mischkarten live sind), dann H1–H4, dann der Rest. Expeditionen werden erst freigegeben, wenn H8–H11 erledigt sind.

### Muss
**H8 – Ein zweiter Fehler in Mischkarte oder Expedition öffnet eine gelandete Etappe wieder.** `schule.misch_buchen` und `schule.expedition_buchen` geben einen endgültigen Fehler an `schule.karte_buchen(…, false, …)` weiter; diese setzt bei `wdh_fehler >= 1` `sitzt = false`. Das widerspricht der Regel „falsch → am nächsten Lerntag fällig, keine Abzüge“ und kann Voraussetzungen anderer Expeditionen entziehen.
→ Eigener Fehlerweg für Mischkarten und Expeditionen: Etappe am nächsten Lerntag fällig, `sitzt` und alle Belege unverändert – auch beim zweiten und dritten Fehler und auch, wenn `wdh_fehler` schon 1 ist. Das Wiederöffnen bleibt allein der fälligen Wiederholung vorbehalten. Test mit zwei endgültigen Fehlern hintereinander (Mischkarte, Expedition, gemischt).
**H9 – Voraussetzungen und Klasse einer Expedition werden beim Prüfen nicht serverseitig durchgesetzt.** Das Angebot prüft sie, `uebung_pruefen_intern` bei Pool `expedition` aber nur die Sichtbarkeit; `expedition.klasse` wird nirgends geprüft.
→ Vor jeder neuen Wertung eines Teils alle Voraussetzungen prüfen (begonnene Expeditionen dürfen nach einem späteren Rückfall zu Ende geführt werden, ohne Nachteil). `klasse`: festlegen und dokumentieren, was sie bewirkt – Vorschlag: reine Einordnung für Eltern, kein Ausschluss, weil das Angebot allein an den gelandeten Voraussetzungen hängt; dann das auch so benennen. Test über den äußeren Weg (`api.schule_uebung_pruefen`).
**H10 – Der Misch-Beleg lässt sich ohne echte Mischung erzeugen.** Der Server vertraut `misch: true` aus dem Browser.
→ Serverseitig prüfen: Die Aufgabe gehört zu einer gelandeten Etappe des Kindes, sie ist nicht die gerade geübte Etappe (Einheit und Lernkarte der laufenden Übung mitsenden und prüfen) und sie stand in der zuletzt ausgelieferten Mischkarten-Liste bzw. erfüllt deren Regeln (Stufe 2–3, Pool `uebung`). Sonst wird normal gebucht, ohne Misch-Beleg. Negativtest.
**H11 – Bei mehreren Versionen eines Themas kann die Expedition die falsche Etappe buchen.** Der Import bindet jeden Teil an eine `einheit_id`; die Voraussetzungen gelten für jede Version des Themas.
→ Beim Buchen die Etappe je Kind über `thema_id` + Lernkarte auf die tatsächlich gelandete Version auflösen. Test mit zwei Versionen. (Heute gibt es je Thema eine Einheit – trotzdem vor der ersten Freigabe.)

### Sollte
**H12 – Import härten:** `expedition_importieren` erzwingt 3–5 Teile, mindestens 3 Themen, gültige Lernkarten, Bezug jedes Teils in den Voraussetzungen und beim Status „freigegeben“ freigegebene Bezugs-Flüge; sonst Abbruch mit klarer Meldung.
**H13 – Dosis der Mischkarten als Test:** Klasse 5 und 8; nur zwei gelandete Etappen; Wechsel der Lernkarte und Neustart des Browsers; manuelle Stufenwahl; alle acht Kandidaten verbraucht; Abbruch nach einem Mischfehler.
**H14 – Rauchtests über die echte Antwortstrecke** (Teil 4 und „gesperrte Bordkarte“): äußerer API-Weg, 1./2. Versuch, Tipp, Fortsetzung nach Abbruch, „geladen, danach gesperrt“.
**H15 – Botschaft der Expedition:** „Expedition abgeschlossen“ (Durchhalten, Stempel) klar trennen von „selbst gelöst/angewandt“ (Beleg je Teil); kein Straftext. Prüfen, ob ein alter Misch-Beleg nach späteren Fehlern noch als aktuell gelten soll (Vorschlag: Beleg muss nach der letzten Landung liegen – passt zu H4).

# Bau-Auftrag LA (18.11.): Lehrer-Aufbau – Pakete LA-1 bis LA-7

**Auswahl Sebastian:** 1A · 2B · 3B · 4A · 5A · 6B · 7A. **Der vollständige Bauauftrag steht in `inhalte/pruefung/lehrer/umsetzung.md`**, die Befunde dazu (L1–L9, App 0.78.1) in `inhalte/pruefung/lehrer/bericht.md`, Bilder des heutigen Stands in `inhalte/pruefung/lehrer/bilder/` (alle drei aus dem Zweig `pruefung-kinderansicht` nach `lernen-app` übernommen). Dieser Abschnitt legt nur fest, was dort offen ist oder von unseren Regeln abweicht.

**Wer baut:** der Bau-Chat (nicht der Haupt-Chat, anders als in der Tabelle „Wer macht was“). Zweig `bau-lehrer` von aktuellem `lernen-app`, **erst nachdem H8 und H1–H4 aus Bau-Auftrag H gemeldet sind** – es baut immer nur ein Chat am App-Code. Datenbank: Migrationen als Datei nach `supabase/migrations/20261119_la_<paket>_<name>.sql`, nicht ausführen; kein DROP, kein DELETE; Lernstände und Pläne bleiben erhalten. Meldungen in `inhalte/postfach/bau-lehrer.md`, je Paket „FERTIG: LA-n“. Kein Merge nach `lernen-app` oder `main`. Reisewörter überall; Info-Seite „So funktioniert’s“ im selben Schritt; Tests in `tests/lernen.test.cjs` je Paket.

**Reihenfolge und Lieferung:** LA-1 → LA-2 → LA-6 → LA-3 → LA-5 → LA-4 → LA-7. Nach LA-2 und nach LA-4 je eine Zwischenmeldung mit Bildern (Tablet 820 px, Handy 400 px, Rechner), damit der Prüf-Chat nachprüfen kann.

**Abweichungen und Klarstellungen:**
1. **„Lernen starten“ bleibt für Eltern.** Die Kinder haben derzeit keinen eigenen Zugang; sie kommen über den Eltern-Zugang und den Knopf „Lernen starten“ auf ihre Abflugtafel. Deshalb: Bei der Rolle **Eltern** steht „Lernen starten“ in jeder Tabellenzeile bzw. Kind-Karte (LA-2) und im Kopf der Kind-Seite als deutlicher Knopf. Bei der Rolle **Lehrer** entfällt er wie in LA-2 beschrieben; dort bleibt „Lernreise ansehen“ klein im Kopf der Kind-Seite.
2. **„Besprochen ✓“ (LA-3):** neue Tabelle (Kind, Einheit, Lernkarte, wer, wann); Lehrer und Eltern dürfen setzen; neue endgültig falsche Antworten nach dem Zeitpunkt holen die Etappe zurück nach „Zu tun“. Keine neue Aktion in `lernen-api`, wenn es über eine bestehende geht – sonst melden.
3. **„Kann schon“ je Flug (LA-4):** neues Feld am Plan (z. B. `route.kann_schon_themen bigint[]`, entsprechend `ausgelassen`); zählt in `thema_stand`, Lernstand-Tabelle, Abflugtafel und Ort-Abschluss wie gelandet, aber als eigener Zustand („kann schon“), nicht als `karte_stand.sitzt` – Mischkarten, Wiederholungen und Expeditionen entstehen daraus **nicht**. Das bisherige „kann schon“ für den ganzen Ort bleibt und setzt alle Flüge. Rückgängig ohne Verlust.
4. **„Zu tun“ rot (LA-2):** „eingetragene Pausen/Reisetage“ gibt es noch nicht. Bis dahin ohne diese Ausnahme bauen; nichts Neues dafür anlegen, nur im Bericht nennen.
5. **„Häufigster Fehler“ (LA-3):** nur zeigen, wo `grund` bei mindestens zwei falschen Antworten vorkommt; sonst „–“. Keine Aussage erfinden, wie das Kind gerechnet hat.
6. **IB:** einheitlich MYP-Jahr = Klasse − 5 (seit 0.78.0); unter Klasse 6 „noch kein MYP-Jahr“.
7. **Entwurf:** Der Auswahl-Entwurf „Lehrer-Ansicht: neuer Aufbau“ liegt nicht im Repository. Maßgeblich ist der Text in `umsetzung.md`. Wo er eine Frage offenlässt, die schlichteste Lösung nehmen und in der Meldung nennen.

# Vierundzwanzigste Runde (18.11.): Realschul-/IB-Themen auflösen, wo der Stoff schon da ist

**Entscheidungen von Sebastian (18.11.) zu `inhalte/pruefung/klassen/doppelt-rsib.md`:**
1. Grundsatz angenommen: **11 Themen auflösen, 13 bleiben, keine neuen Themen.**
2. Von den 13 bleibenden sind im Plan der Kinder **Pflicht** nur die zwei für alle Realschul-Zweige (`abbildungen.determinanten2`, `daten.stichproben`). Alle anderen (IB Standard, IB Extended, Zusatz, mathematischer Realschul-Zweig) werden **freiwillig angeboten**. (Das stellt der Haupt-Chat im Plan ein – nicht Teil dieses Auftrags.)
3. `terme.quadratische_extreme` bleibt als eigener Flug in Klasse 8 (Realschule verlangt es dort); die entsprechenden Gymnasium-Lernkarten in Klasse 9 werden zur kurzen Wiederholung mit Verweis.
4. Das Dualsystem wird ergänzt (Realschule M5 1.2).

**Ein Chat, Zweig `aufloesen` (von aktuellem `lernen-app`), Meldungen in `inhalte/postfach/aufloesen.md`.** Grundlage ist `doppelt-rsib.md`: Teil 2 (je Thema Lernkarte für Lernkarte mit Gruppe A/B/C und Zielthema) und Teil 3a (fünf neue Lernkarten statt vier neuer Themen). Vorher lesen: `inhalte/README.md` (Themen-Bausatz, „Stufen und Aufgabentypen“, Vertiefung), `inhalte/postfach/stufen-kl5.md` (oberste Meldung: Fehlerarten bei neuen Aufgaben).

**Teil A – die 11 Themen auflösen** (`abbildungen.vektoren`, `funktionen.scharen`, `funktionen.transformation`, `gleichungen.reinquadratisch`, `funktionen.umkehr`, `mengen.grundbegriffe`, `groessen.verhaeltnisse`, `stochastik.bedingt`, `funktionen.folgen`, `finanzen.zinseszins`; Sonderfall `terme.quadratische_extreme` siehe Teil C):
- **A-Lernkarten** (Stoff steht schon im Gymnasium-Flug): entfallen. Aufgaben, die dort einen fehlenden Typ oder eine fehlende Stufe ergänzen, dürfen in die Gymnasium-Lernkarte umziehen (keine doppelten Fragetexte).
- **B- und C-Lernkarten:** ziehen als Lernkarte in das in `doppelt-rsib.md` genannte Zielthema, an die dort genannte Stelle, mit Erklärung, „Kurz gesagt“, Beispiel und allen Pools. **Pflicht**, wenn der Stoff für alle Realschul-Zweige verlangt ist (so in `doppelt-rsib.md` vermerkt); sonst **Vertiefung** (IB, mathematischer Realschul-Zweig, Zusatz). Der Lernkarten-Schlüssel `l` bleibt, wenn er im Zielthema frei ist.
- Die Themendatei des aufgelösten Themas bleibt unverändert liegen (sie ist in der Datenbank ein Entwurf ohne Lernstände; der Haupt-Chat legt sie still). Nicht löschen, nicht aus der Themenliste nehmen.
- Vorwissen: Eine umgezogene Lernkarte darf nichts voraussetzen, was im Zielthema und in der Reihenfolge von `inhalte/themenliste.json` erst später kommt. Sonst an die spätere passende Stelle oder als Vertiefung ans Ende – im Bericht begründen.

**Teil B – fünf neue Lernkarten in bestehenden Flügen** (aus `doppelt-rsib.md` Teil 3a, die „C“-Karten der vier nicht mehr geplanten Themen) **und das Dualsystem** (eine Lernkarte in Klasse 5 im passenden Flug zu Stellenwertsystemen, vermutlich `zahlen.natuerlich`; prüfen, was dort schon steht – nur ergänzen, was fehlt; Pflicht für die Realschule, für das Gymnasium Vertiefung, falls der Lehrplan M5 es nicht nennt).

**Teil C – `terme.quadratische_extreme`:** Der Flug bleibt (Klasse 8). In den Gymnasium-Themen der Klasse 9, die denselben Stoff enthalten, wird die Lernkarte gekürzt zu einer Wiederholung (Erklärung verweist auf den Flug in Klasse 8, die besten Aufgaben bleiben, Mindestmengen halten). Nichts doppelt.

**Für alle neuen oder umgezogenen Lernkarten gelten die Regeln der Zwanzigsten Runde:** jede freie Übung mit `g`; Stufe 1 mindestens 4 aus 2 Typen, Stufe 2 mindestens 6 aus 3 Typen, Stufe 3 mindestens 8 aus 4 Typen; 2 Knobel-Bordkarten; Lösungen rechnet der Generator. **Und die Prüfkriterien für neue Aufgaben:** jede Lösung nachrechnen (bei „höchstens/mindestens/wie viele/immer“ alle Fälle); keine mehrdeutige Zählweise („k. Strich“); keine Begriffe aus späterem Stoff, auch nicht in Tipp und Lösungsweg; keine Buchstaben als Unbekannte vor dem Stoff, der sie einführt; keine falschen Rechnungen in Antwortoptionen; Lösungswege ohne Sprünge. Alte Aufgaben der Zielthemen bleiben Zeichen für Zeichen gleich.

**Bericht (Pflicht):** Umzugstabelle `altes Thema / Lernkarte → Zielthema / Lernkarte · Pflicht oder Vertiefung · Klasse · Zahl der Aufgaben`; Liste der entfallenen A-Lernkarten mit dem Gymnasium-Gegenstück; neue Lernkarten aus Teil B; was sich für ein Kind ändert, das den Zielflug schon abgeschlossen hat (neue Pflicht-Lernkarte = Flug wieder offen – je Zielthema nennen); was nicht geprüft wurde. Ein Zielthema = ein Commit + Push. Prüfskript OK je Thema. Kein Merge, keine Datenbank, kein App-Code, keine Tests. Ohne Rückfragen durcharbeiten; bei Unklarheit die sinnvollste Lesart nehmen und nennen.

# Ortsprüfung (18.11., Wunsch von Sebastian): ein ausführlicher Test je Ort – gibt Punkte und Geld

**Entscheidungen von Sebastian:** Nach jedem Ort ein ausführlicher Test („Ortsprüfung“). **Keine Noten** – nur eine Punkte-Übersicht; ab einer Schwelle gibt es Punkte und Geld. **Keine Zeitbegrenzung**; die Zeit wird gemessen, eine gute Zeit kann einen Bonus bringen (ein Abzug für „zu lange“ ist möglich, aber standardmäßig aus). **Wiederholen:** Das Kind kann sagen „die will ich in ein paar Tagen noch einmal schreiben“; es zählt das bessere Ergebnis, bei der Wiederholung mit etwas Abzug. **Der Rechenweg zählt:** Das Kind rechnet auf Papier. Die Kinder wollen lieber mehrere kleinere Prüfungen als wenige große. Die bisherigen Sterne werden **Fleißsterne** (kleiner Betrag, gedeckelt).

## Teil 1 – Dateiformat (gilt für Bau- und Inhalte-Chats)

Datei `inhalte/pruefungen/<klasse>-<ort>-<fassung>.json` (`fassung` = `a` oder `b`; `ort` = Stadt klein, ohne Sonderzeichen), erzeugt von `inhalte/generatoren/pruefung_<klasse>_<ort>.py` (ein Generator schreibt beide Fassungen; alle Lösungen rechnet das Programm, exakt).
Felder: `schluessel` (= Dateiname ohne Endung), `klasse` (`{"gym_by": n}`), `block_id`, `ort`, `fassung`, `titel`, `richtzeit_min` (ehrliche Schätzung für ein durchschnittliches Kind, auf 5 gerundet), `hilfsmittel` (z. B. „Geodreieck, kein Taschenrechner“), `stoff` = Liste `{thema_schluessel, lernziel}` (nur Lernkarten der Flüge dieses Ortes, dazu höchstens zwei ältere Lernkarten zur Verknüpfung, als `"alt": true` markiert), `aufgaben` = Liste; je Aufgabe: `nr`, `titel`, `einleitung` (Sachsituation), optional `grafik`, `teile` = 2–4 Teile.
Je Teil die Felder einer Bordkarte wie bei Expeditionen (`k, y, f, a, o, c, w`, kein Tipp) und `bezug {thema_schluessel, lernziel}`, dazu: `punkte_ergebnis` (1–2), `punkte_weg` (0–3) und `weg_schritte` = Liste `{text, punkte}` – die Schritte der Musterlösung, an denen Eltern oder Lehrer den Rechenweg abhaken (Summe = `punkte_weg`). Teile ohne Rechenweg (Ablesen, Auswahl) haben `punkte_weg` 0.

## Teil 2 – Inhalte (zwei Chats, zuerst die Orte, die bei den Kindern als nächste kommen)

**Chat Klasse 5 → Zweig `pruefung-kl5`, Meldungen `inhalte/postfach/pruefung-kl5.md`:** Orte Rom, Kairo, Timbuktu, Athen, Toronto. **Chat Klasse 8 → Zweig `pruefung-kl8`, Meldungen `inhalte/postfach/pruefung-kl8.md`:** Orte Samarkand, Mumbai, Delhi, McMurdo-Station, Neumayer-Station III. Welche Flüge zu einem Ort gehören: `inhalte/themenliste.json` (Felder `ort`/`block_id`); Lernkarten und Niveau: `inhalte/themen/<thema>.json`. Je Ort **zwei Fassungen** (a, b) – gleicher Aufbau und gleiche Schwierigkeit, andere Situationen und Zahlen.

Regeln:
- **Umfang:** je Flug des Ortes etwa eine mehrteilige Aufgabe, mindestens 3 und höchstens 6 Aufgaben; zusammen 20–35 Punkte; `richtzeit_min` 20–45. Jede Pflicht-Lernkarte des Ortes kommt in mindestens einem Teil vor; Vertiefungs-Lernkarten nicht.
- **Niveau wie eine Schulaufgabe am bayerischen Gymnasium:** etwa 40 % Grundfertigkeiten, 40 % mehrschrittig/Sachaufgabe, 20 % anspruchsvoll (begründen, rückwärts, verknüpfen). Vorbild sind Schulaufgaben und Jahrgangsstufenarbeiten – nur Typ und Niveau, nichts wörtlich übernehmen.
- **Unbekannte Aufgaben:** kein Fragetext, der in `inhalte/themen/` oder `inhalte/expeditionen/` vorkommt, und keine bloße Zahlenvariante einer dortigen Aufgabe mit demselben Satzbau.
- **Kein Folgefehler-Domino:** Jeder Teil nennt die Werte, die er braucht.
- **Rechenweg:** `weg_schritte` so schreiben, dass ein Erwachsener ohne Mathe-Studium sie auf dem Blatt wiederfindet („Gleichung aufgestellt: 5 + 0,1x = 12“ · „nach x aufgelöst“ · „Antwortsatz mit Einheit“). Andere richtige Wege zählen gleich – im Text der Aufgabe `w` darauf hinweisen, wenn es einen üblichen zweiten Weg gibt.
- Die Prüfkriterien für neue Aufgaben gelten (jede Lösung nachrechnen, bei „höchstens/mindestens/wie viele“ alle Fälle; eindeutige Fragen; kein späterer Stoff nach der Reihenfolge in `themenliste.json`, auch nicht in der Musterlösung; in Klasse 5 keine Buchstaben als Unbekannte außerhalb von Stoff, der sie einführt; keine Zählweise „k. Strich“; realistische Zahlen und Einheiten; keine Namen realer Personen).
- Der Generator prüft sich selbst (Abbruch, wenn Punktesummen nicht stimmen, ein Bezug nicht in `stoff` steht, eine Pflicht-Lernkarte fehlt oder ein Fragetext schon in den Themen vorkommt). Das Prüfskript `tools/inhalt_pruefen.py` kennt Prüfungen noch nicht – das ergänzt der Bau-Chat.
- Eine Prüfung (beide Fassungen) = ein Commit + Push. Bericht: Tabelle Ort · Flüge · Aufgaben · Punkte (Ergebnis/Weg) · Richtzeit; je Prüfung eine Aufgabe im Wortlaut mit Musterlösung; was nicht geprüft wurde. Kein Merge, keine Datenbank, kein App-Code.

## Teil 3 – Bau (Bau-Chat, nach Auftrag H und nach dem Lehrer-Aufbau LA; Zweig `bau-pruefung`, Meldungen `inhalte/postfach/bau-pruefung.md`)

Rahmen wie Bau-Auftrag G (Migrationen nur als Datei, kein DROP/DELETE, Lernstände bleiben, Info-Seite und README im selben Schritt, Tests, kein Merge).
1. **Daten und Import:** Tabelle für Prüfungen (Kopf wie `schule.expedition`, dazu Ort, Fassung, Richtzeit), Teile als Zeilen in `schule.aufgabe` (eigener Pool `pruefung`, nie in Übung, Wiederholung, Mischkarten, Tests, Expeditionen); Import-Funktion mit denselben harten Prüfungen wie `expedition_importieren`. `tools/inhalt_pruefen.py` um Prüfungen erweitern (Format, Punktesummen, Bezug in `stoff`, jede Pflicht-Lernkarte des Ortes, Lösung nachgerechnet, kein Fragetext aus Themen/Expeditionen).
2. **Freischalten:** Eine Ortsprüfung wird möglich, wenn alle Flüge des Ortes (die im Plan sind) gelandet und ihre Flug-Tests bestanden sind. Eltern oder Lehrer schalten sie frei („Prüfung jetzt schreiben lassen“) – das Kind kann sie nicht allein starten. Entwürfe nur für das Testkind.
3. **Schreiben (Kind):** ruhige Ansicht ohne Tipps, ohne zweiten Versuch, ohne sofortige Rückmeldung; alle Aufgaben sichtbar, Reihenfolge frei, Antworten bis zur Abgabe änderbar; Hinweis „Rechne auf deinem Blatt – der Rechenweg zählt“; Zeit läuft sichtbar mit (klein, ohne Countdown, ohne Farbe), Pausieren möglich; Abgabe mit Rückfrage; Abbruch verliert nichts.
4. **Auswerten:** Ergebnispunkte sofort durch die App. Danach zeigt die App Eltern/Lehrern je Teil die Musterlösung mit `weg_schritte` zum Abhaken (Standard: nichts angehakt; „alles richtig“ als Abkürzung je Aufgabe). Erst nach diesem Schritt steht das Ergebnis fest. Punkte-Übersicht für Kind und Eltern: je Aufgabe Ergebnis- und Wegpunkte, Summe, Anteil, Schwelle – **keine Note**, kein Rot. Besprechung: Musterlösung je Teil für das Kind sichtbar.
5. **Schwelle, Zeit, Geld (alles einstellbar je Kind, Vorgaben in `schule.regel`):** Schwelle bestanden (Vorgabe 80 %), zweite Stufe „sehr gut“ (Vorgabe 95 %, kann aus sein); Zeitbonus, wenn höchstens Richtzeit × Faktor (Vorgabe 1,0; kann aus sein); Zeitabzug ab Richtzeit × Faktor (Vorgabe aus); Betrag je bestandener Ortsprüfung, Zuschlag „sehr gut“, Zeitbonus; Wiederholung zählt mit Faktor (Vorgabe 0,8). Beträge sind je Kind gleich voreingestellt und nur von Eltern änderbar. Sterne für die Prüfung: Vorschlag machen, getrennt von den Fleißsternen ausweisen.
6. **Wiederholen:** Das Kind (oder Eltern) kann nach dem Ergebnis „In ein paar Tagen noch einmal“ wählen; frühestens nach 3 Lerntagen, dann mit der **anderen Fassung**; es zählt das bessere Ergebnis, das Geld der Wiederholung mit Faktor. Höchstens eine Wiederholung je Ort (einstellbar).
7. **Abrechnung „Verdient“ (nur Eltern):** je Kind eine Liste – bestandene Ortsprüfungen mit Betrag, Fleißsterne des Monats mit Kurs und Obergrenze (beides einstellbar, Vorgabe gleich für alle Kinder), Summe offen, „ausgezahlt“ zum Abhaken mit Datum. Keine Zahlungsfunktion – nur Buchführung. Fleißsterne = die bisherigen Sterne; ihr Name in Kinder- und Elterntexten bleibt „Sterne“, in der Abrechnung „Fleißsterne“.
8. **Foto des Rechenwegs:** nicht in der App speichern. Hinweis für Eltern: „Unsicher beim Rechenweg? Blatt fotografieren und im Chat mit Claude prüfen lassen.“
9. **Reise:** Der Stempel für den Ort bleibt, wie er ist (alle Flüge geschafft). Die bestandene Ortsprüfung gibt ein eigenes Zeichen am Ort (Vorschlag: Siegel im Reisepass). Eine nicht bestandene Prüfung nimmt nichts weg.
10. **Tests:** Freischalten nur durch Eltern/Lehrer; Abgabe und Auswertung; Weg-Haken ändern das Ergebnis; Schwelle/Zeitbonus/Wiederholung mit anderer Fassung und Faktor; Abrechnung; Entwurf nur Testkind; kein Prüfungs-Teil taucht je im Üben auf.

---

# Expeditionen – Korrekturen nach der fachlichen Prüfung (18.11., Werkstatt-Nachricht 853)

Ergebnis der Prüfung durch ChatGPT: 17 von 21 Expeditionen freigabereif, 4 mit Auflagen, 0 nicht freigabefähig. Alle 64 Zahl-/Lückenlösungen wurden nachgerechnet und stimmen. Es geht nur um Texte, keine Rechnung ändert sich.

Regeln wie im Abschnitt „Expeditionen – Inhalte für Klasse 5 und Klasse 8“. Nur die genannten Dateien und ihre Generatoren ändern. Danach `python3 -I tools/inhalt_pruefen.py --alle`. Nichts in die Datenbank schreiben; kein Merge nach `main`.

## Chat `expedition-kl5` (Zweig `expedition-kl5`, Meldung in `inhalte/postfach/expedition-kl5.md`)

1. **`5-flug_toronto` (Muss):** Die vier Teile (Flugzeiten, Outfits, Wäscherei, Gepäck) sind bisher einzelne Reise-Aufgaben. Baue einen durchgehenden Zusammenhang ein: Ein Teil muss ein Ergebnis oder eine Entscheidung aus der Geschichte brauchen (jeder Teil nennt weiter alle nötigen Zahlen selbst – kein Folgefehler). Zusätzlich: „Toronto = Berlin − 6 Stunden“ als Annahme für diesen Reisetag kennzeichnen.
2. **`5-schatzsuche` (Muss):** Teil d nutzt die Quersummenregel für 9. Der Lehrplan Klasse 5 nennt nur die Regeln für 2, 3, 5 und 10. Gib die 9er-Regel im Aufgabentext oder im Tipp ausdrücklich an („Eine Zahl ist durch 9 teilbar, wenn ihre Quersumme durch 9 teilbar ist.“).
3. **`5-roemerstrasse` (Sollte):** Die 144 Meilen als Strecke ab Meile 0 kennzeichnen – das Kind wandert nicht 213 km.
4. **`5-pyramide` (Sollte):** Den Wechsel vom kleinen Würfelmodell zur großen Pyramide mit einem Satz verbinden.

## Chat `expedition-kl8` (Zweig `expedition-kl8`, Meldung in `inhalte/postfach/expedition-kl8.md`)

1. **`8-radtour` (Muss):** In Teil c und d klarstellen, dass Kilometer 36 im Graph ein Zwischenpunkt ist und der See bei Kilometer 42 liegt (die Route ist 36 km lang und beginnt bei Kilometer 6). Sonst wirken 30 km aus dem Graph wie ein Widerspruch.
2. **`8-pool` (Muss):** Teil d „wenn es ganz über dem Wasser hängt“ umformulieren – ein Dreieckssegel mit 4 m Seitenlänge passt nicht in einen Kreis mit 3,6 m Durchmesser. Vorschlag: „Selbst wenn die gesamte Segelfläche Schatten auf das Wasser wirft …“. Rechnung und Antwort bleiben.

Fertig, wenn: Dateien und Generatoren stimmen überein, Prüfskript ohne Fehler, Meldung „FERTIG: Korrekturen 853“ im Postfach mit dem alten und neuen Wortlaut jeder geänderten Stelle.

---

# Bau-Auftrag I (20.11.): Mängel aus drei Nachprüfungen

Grundlagen: Nachprüfung Lehrer-Aufbau `inhalte/pruefung/lehrer/nachpruefung.md` (Prüf-Chat, mit Bildern), Prüfergebnisse von ChatGPT in der Werkstatt – Nachricht 872 (Auftrag H) und 873 (Nachtragstest W177). Die Texte der beiden Nachrichten stehen sinngemäß unten; die Nachprüfung liegt im Arbeitszweig.

**Es baut immer nur EIN Chat am App-Code.** Reihenfolge: zuerst Teil 1 (Chat `bau-lehrer`), danach Teil 2 (Chat `bau-motivation`). Teil 2 beginnt erst, wenn Teil 1 in `lernen-app` zusammengeführt ist (Meldung des Haupt-Chats in `inhalte/postfach/antworten.md`).

Für beide Teile: Zweig vom aktuellen `lernen-app`; Datenbank nur lesen; Migrationen als Datei mit Rauchtest (Rollback, nur Testkind, eigene Namen für Variablen – keine Tabellen-Aliase doppelt belegen, keine Kommentare mitten in `declare`-Zeilen; Tests dürfen nicht von Daten abhängen, die schon in der Datenbank liegen); App-Tests vollständig laufen lassen; kein Merge nach `main`. Keine Kinderdaten, keine Schlüssel. Meldung „FERTIG: Auftrag I, Teil n“ im eigenen Postfach, getrennt nach „gesehen/getestet“ und „nicht geprüft“.

## Teil 1 – Lehrer-Aufbau (Chat `bau-lehrer`, Zweig `bau-lehrer`, App 0.81.0)

**Muss**
1. **„Was wackelt“ auf dem Handy (400 px):** Wörter brechen mitten im Wort, die Spalte „seit“ und der Reiter „Plan“ sind abgeschnitten. Unter 560 px je Etappe eine Karte (wie die Kinder-Karten der Startseite) statt Tabelle; Reiterband ohne Abschneiden.

**Sollte**
2. **Eltern-Startseite:** „Wartet auf dich“ (Belohnung einlösen) als blauer Eintrag in „Zu tun“ statt als Kasten darüber. Danach passt die Kinder-Tabelle auf dem Rechner (1280 × 800) ohne Rollen – per Test messen.
3. **Lehrplan-Übersicht auf dem Handy:** als Liste oder mit fester erster Spalte, ohne abgeschnittene Inhalte.
4. **Reisewörter beim ersten Vorkommen erklären** (klein, in Klammern oder als Hinweis): Rückreise = Wiederholung nach nicht bestandenem Nachtest; Etappe = Lernschritt; Flug = Thema; Bordkarte = Aufgabe.
5. **Nachtragstest-Link (W177, Befund 7):** Der Link auf der Flugseite hängt an `!offen` und heißt „Alle Etappen sitzen – Test zu den neuen Etappen“. Den Link nur an „Flug-Test abgeschlossen und neue offene Pflicht-Etappen“ binden, Text neutral „Test zu den neuen Etappen“.

**Kann** (mitnehmen, wenn es ohne Umbau geht)
6. Überblick: nicht „Nichts wackelt.“ direkt über „Rückreise … offen“ – z. B. „Keine Etappe wackelt · Rückreise Pisa offen“.
7. Geschafft: Flug ohne Inhalt als „noch kein Inhalt“ statt dreimal „–“.
8. Tablet: Rahmen der ⚙-Zelle ausrichten; „noch kein MYP-Jahr“ kürzer („– (ab Kl. 6)“); Spaltenkopf „AKTIONEN“ weglassen; Hinweis „über der Klasse des Kindes“ nicht abschneiden.
9. Hinweise mit dem Wort „Datenbank“ durch neutrale Sätze ersetzen.

**Zusatz (Sebastians Entscheidung 20.11.)**
10. **Reisetage und Pausen eintragen.** Eltern und Lehrer können je Kind Zeiträume ohne Lernen eintragen (von–bis, optional ein Wort wie „Reisetag“, „krank“, „Ferien“; auch für alle Kinder zugleich). Ort: „⚙ Einstellen“ des Kindes und ein kurzer Weg von der Startseite („Reisetag eintragen“). Wirkung: Eingetragene Tage zählen nicht für „rot/gelb“ bei „Lernt“ und nicht für „kein Lerntag seit …“ in „Zu tun“; in der Zeile steht dann z. B. „Pause bis 24.11.“. An Lernregeln, Wiederholungen und Nachtests ändert sich nichts (die zählen ohnehin in Lerntagen). Eintragen, ändern und löschen muss gehen; vergangene Einträge bleiben sichtbar. Datenbank: Migration als Datei (Tabelle z. B. `schule.pause`: Kind oder alle, von, bis, grund, wer, wann) mit Rauchtest; Zugriff nur für Eltern/Lehrer. Info-Seite um einen Satz ergänzen.

**Entschieden, nicht bauen:** Die Stand-Zellen (GYM, RS, IB) bleiben ohne Ampelfarbe.

## Teil 1b – LA-8 „Lehrplan nach Themengebiet“ (Chat `bau-lehrer`, gleicher Zweig, nach Teil 1; von Sebastian am 20.11. freigegeben)

Vorgabe des Gestalters: `inhalte/pruefung/lehrer/umsetzung.md`, Abschnitt **LA-8** (vollständig, mit „Fertig, wenn“). Entwurf zum Ansehen: `inhalte/pruefung/lehrer/entwurf/lehrplan-spalte.html` (im Browser öffnen, enthält die echte Themenliste). Bild: `inhalte/pruefung/lehrer/bilder/lehrplan-spalte-entwurf.png`. LA-8 ergänzt LA-4 (Flugplan, rechte Spalte) und LA-7 (Lehrplan-Übersicht). Es gilt für Lehrer und Eltern; **die Kinderansicht behält die Orte**.

Kurz, maßgeblich ist der Abschnitt LA-8:
1. Überschrift jeder Zeile „Themengebiet – Thema“ statt „Ort – Thema“ (mehrere Flüge mit „und“, ab 3 die ersten zwei und „…“); darunter klein „Gym 7 · RS 7 · MYP 3 · 2 Flüge“. Links im Plan steht der Ort nur noch klein am Ende („Ort in der Reise: Samarkand“).
2. Rechte Spalte mit Umschalter „Nach Themengebiet“ (Standard) | „Nach Klasse (Lehrplan)“.
3. „Nach Themengebiet“: Knöpfe für die acht Gebiete (vorbelegt mit dem Gebiet des aktuellen Ortes), „Sortiert nach Klasse in: Gymnasium | Realschule | IB MYP“ (vorbelegt mit der Schulart des Kindes), alle Orte des Gebiets aus allen Klassen von leicht nach schwer, gestrichelte Linie „ab hier über Klasse X des Kindes“, Kopf „Zahlen: 4 von 8 Orten im Plan · von leicht nach schwer“ mit Balken, jeder Ort mit „+“ oder Ziehen einplanbar, eingeplante grau mit „✓ im Plan“.
4. „Nach Klasse (Lehrplan)“ wie LA-4, mit den neuen Überschriften.
5. Farbe je Klasse nach der Gymnasium-Klasse (Kästchen mit Klassenzahl, farbiger linker Rand mit hellem Verlauf, links und rechts gleich): 5 #2E7D32 · 6 #0277BD · 7 #6A1B9A · 8 #C62828 · 9 #EF6C00 · 10 #455A64; ohne Gymnasium-Klasse graues „–“; Legende unten.

Hinweise des Haupt-Chats: Themengebiet = `schule.kontinent.titel` des Ortes (Zahlen, Geld und Verhältnisse, Algebra, Funktionen, Geometrie, Fläche und Raum, Daten und Zufall, Entdecker-Inseln). Klassen je Schulart kommen aus `schule.thema_jahrgang` (Realschule und IB sind seit dem 18.11. fest eingetragen; IB als MYP-Jahr = Klasse − 5). Orte, die nur Entwurfs-Flüge haben (10 aufgelöste Themen), erscheinen nicht. Seit dem 18.11. gibt es Orte ohne Gymnasium-Klasse (Zusatz-Orte) – die bekommen das graue „–“ und sortieren bei „Gymnasium“ ans Ende. Braucht die App dafür neue Felder vom Server: Migration als Datei mit Rauchtest. Farben auch in der dunklen Gestaltung lesbar halten (Kontrast messen). Tests für alle vier „Fertig, wenn“-Punkte. Version 0.81.0 zusammen mit Teil 1. Meldung „FERTIG: Auftrag I, Teil 1b (LA-8)“ – der Gestalter prüft nach.

## Teil 2 – Lernregeln (Chat `bau-motivation`, Zweig `bau-motivation`, App 0.81.1)

**Muss**
1. **H10 – Mischkarte serverseitig binden.** Heute glaubt der Server dem Gerät, welche Etappe „die aktuelle“ ist (`aktuell_einheit`, `aktuell_lernziel`); damit lässt sich jede Übung einer gelandeten Etappe als Mischkarte melden und erzeugt einen Beleg (`misch_ok_am`) – und darüber „sicher“. Lösung: Der Server merkt sich, welche Mischkarten er einem Kind ausgegeben hat (z. B. Tabelle `schule.misch_ausgabe`: Kind, Aufgabe, ausgegeben am, eingelöst am; Eintrag beim Ausliefern durch `schule.mischkarten`), und `misch_buchen` zählt nur eine ausgegebene, noch nicht eingelöste Karte der letzten 24 Stunden. Ohne passende Ausgabe: normale Buchung als Übung, kein Misch-Beleg. Die alte App (0.80.0) darf dabei nicht brechen – sie bekommt dann schlicht keinen Misch-Beleg. Rauchtest mit gefälschtem Kontext (Negativfall) und echtem Ablauf (Positivfall).
2. **H2 – Folge richtig nachrechnen.** Die Nachrechnung in `h_muss` blendet jede falsche Antwort mit `anlauf = 1` aus – auch einen endgültigen Fehler bei einer Auswahl ohne zweite Chance. Regel sauber fassen (endgültig falsch = letzter Versuch dieser Bordkarte in dieser Runde ist falsch, gleich welcher Anlauf) und als Funktion liefern, die die laufende Buchung und eine Nachrechnung gemeinsam benutzen. Bestand: Der Haupt-Chat hat am 20.11. gelesen – bei den echten Kindern gibt es 3 offene Etappen mit Folge > 0, keine davon ist betroffen. Deshalb **keine** Bestandsänderung, nur die Funktion und ein Negativtest.

**Sollte**
3. **H4/H11/H14 – fehlende Tests:** Nachtest mit 80 % bestanden, aber diese Etappe falsch → nicht „sicher“ (Negativtest); Expedition bei zwei Versionen eines Themas über die ganze Buchung (nicht nur die Hilfsfunktion); Expedition unterbrochen und fortgesetzt.
4. **H12 – Import:** zusätzlich angegebene Voraussetzungen auch auf vorhandene Lernkarte (Lernziel) prüfen, nicht nur auf das Thema.
5. **H6 – Tageszähler:** Die App nimmt für „heute selbst gelöst“ den Tag, den der Server liefert, nicht den Kalendertag des Geräts.
6. **W177 – Nachtragstest:** Rauchtest um Sterne (vorher/nachher, keine Doppelbuchung bei Abbruch und Wiederaufnahme) und um den Fall „offene und fehlerhafte Pflicht-Etappen zugleich“ ergänzen. Frist des nächsten Nachtests nach einem Nachtragstest: im Bericht beschreiben, was heute geschieht (beginnt die 10-Lerntage-Frist neu?) – nichts ändern, Sebastian entscheidet.
7. **H5/H13:** im Bericht ehrlich festhalten, was nur über die innere Funktion und was über den äußeren Zugang getestet ist. Ein Test über den äußeren Zugang braucht einen Schlüssel und entfällt.

---

# Fünfundzwanzigste Runde (20.11.): unabhängige Prüfung der 14 neu freigegebenen Flüge

Sebastian hat am 18.11. 14 Flüge freigegeben, die bisher nur von ihren Autoren-Chats und vom Prüfskript geprüft sind. Diese Runde holt die unabhängige inhaltliche Prüfung nach. **Wer hier prüft, darf keines dieser Themen selbst geschrieben haben** – deshalb zwei neue Chats.

- **Chat `pruefung-neu-1`** (Zweig `pruefung-neu-1`, Meldungen `inhalte/postfach/pruefung-neu-1.md`) – zuerst die Flüge, die im Plan eines Kindes stehen: `abbildungen.determinanten2`, `daten.stichproben`, `terme.quadratische_extreme`, dann `gleichungen.wurzel`, `abbildungen.matrizen`, `funktionen.reihen`, `funktionen.betrag`.
- **Chat `pruefung-neu-2`** (Zweig `pruefung-neu-2`, Meldungen `inhalte/postfach/pruefung-neu-2.md`): `daten.zweidimensional`, `daten.standardabweichung`, `daten.normalverteilung`, `sonder.graphentheorie`, `sonder.logik`, `sonder.optimierung`, `zahlen.schranken`.

Beide Zweige vom aktuellen `lernen-app`. Vorher lesen: `inhalte/README.md` (Themen-Bausatz, „Stufen und Aufgabentypen“, Vertiefung) und `inhalte/postfach/stufen-kl5.md` (oberste Meldung: Beispiele für die Fehlerarten).

**Was zu prüfen ist – je Thema jede Lernkarte und jede Aufgabe in allen Pools** (Übung, Knobel, Test, Korrektur, Sicherung) aus `inhalte/themen/<thema>.json`:

a) **Lösung falsch oder nicht eindeutig.** Jede Lösung selbst nachrechnen, unabhängig vom Generator. Bei „höchstens / mindestens / wie viele / immer / nie“ alle Fälle durchgehen. Bei Auswahl-Aufgaben: genau eine Option richtig, keine zweite vertretbar.
b) **Mehrdeutige Frage oder Zählweise** („der k. Strich“, „zwischen“, „bis“), fehlende Angabe, unklare Einheit, unklare Rundung.
c) **Späterer Stoff.** Nichts voraussetzen, was nach der Reihenfolge in `inhalte/themenliste.json` erst später kommt – auch nicht in Tipp, Lösungsweg, Antwortoptionen oder Erklärung. Maßgeblich ist die Klasse des Themas (Feld `klasse`, bei Realschul-Themen `rs_by`, bei IB `ib_myp` + 5).
d) **Erklärung der Lernkarte** (Einstieg, Wörter, Bild, Schritte, typischer Fehler, „Kurz gesagt“): fachlich richtig, vollständig genug für die Aufgaben der Karte, Beispielrechnung stimmt, kein Sprung.
e) **Lösungsweg und Tipp:** führt wirklich zur Lösung, keine Sprünge, Tipp verrät nicht das Ergebnis; falsche Antwortoptionen beruhen auf echten Denkfehlern und enthalten keine falschen Rechnungen als „Begründung“, die ein Kind für richtig halten könnte.
f) **Stufe und Typ:** Stufe 1/2/3 und Aufgabentyp (`g`) passen zum Anspruch; Stufe 3 ist wirklich schwerer als Stufe 2 und nicht nur „größere Zahlen“. Realistische Zahlen, Einheiten und Sachsituationen; keine Namen realer Personen; nichts wörtlich aus Schulbüchern oder Prüfungen.

Zusätzlich je Thema ein Satz: **Passt der Flug zur angegebenen Klasse und zum Lehrplan** (Realschule Bayern bzw. IB MYP), und fehlt etwas Wesentliches? Quelle nennen (lehrplanplus.bayern.de mit Abrufdatum bzw. das IB-Dokument); was nicht belegbar ist, als Annahme kennzeichnen.

**Fehler beheben, nicht nur melden:** im Generator des Themas ändern (`inhalte/generatoren/…`), Themendatei neu erzeugen, `python3 -I tools/inhalt_pruefen.py inhalte/themen/<thema>.json` muss OK melden. Mindestmengen halten (Stufe 1/2/3 mindestens 4/6/8 freie Übungen mit 2/3/4 Typen, 2 Knobel, Test 1, Korrektur 3, Sicherung 6). Geänderte Aufgaben behalten Typ und Stufe, sofern nicht gerade die falsch waren. Ein Thema = ein Commit + Push.

**Bericht je Thema im Postfach:** Zahl der gelesenen und nachgerechneten Aufgaben; Zahl der Änderungen je Fehlerart a–f; jede Änderung der Art a (falsche Lösung) mit altem und neuem Wortlaut; Urteil „in Ordnung / mit Korrekturen in Ordnung / nicht freigabefähig“ – bei „nicht freigabefähig“ sofort melden, nicht erst am Ende. Tatsachen (nachgerechnet, gelesen) von Annahmen trennen; nennen, was nicht geprüft wurde.

Kein Merge nach `main`, nichts in die Datenbank schreiben, kein App-Code, keine Kinderdaten. Ohne Rückfragen durcharbeiten; bei Unklarheit die sinnvollste Lesart nehmen und im Bericht nennen. Am Ende „FERTIG: Prüfung neu, Chat n“.

## Teil 3 – Nachprüfung von ChatGPT zu Teil 2 (Werkstatt-Nachricht 878; Chat `bau-motivation`, App 0.81.2)

Teil 2 ist live (0.81.1). ChatGPT hat gelesen (nicht ausgeführt): H10 auf dem normalen Weg geschlossen; bei H2 zwei Muss. Beides sind Randfälle – bei den echten Kindern ist nichts beschädigt; **keine Bestandsänderung**.

**Muss**
1. **H2 – endgültige Wertung festhalten.** Fall: zwei richtige; Bordkarte X im 1. Anlauf falsch; dann Y richtig (X wird endgültig falsch gebucht, Folge 0, Y → 1); danach doch noch X im 2. Anlauf richtig, innerhalb von 30 Minuten. Die laufende Buchung bleibt bei Folge 1, `folge_nachrechnen` wertet X rückwirkend als „ersetzt“ und kommt auf 3. Lösung: die getroffene Entscheidung am Versuch speichern (z. B. Spalte `wertung_fest`: `falsch`/`ersetzt`/`eigen`/`neutral`), `versuch_wertung` und `folge_nachrechnen` lesen zuerst diesen Wert; ein späterer 2. Anlauf ändert eine schon endgültig gebuchte Wertung nicht mehr (er zählt dann als normaler neutraler Versuch). Negativtest genau dieses Falls: Buchung = Nachrechnung.
2. **H2 – Nachbuchen genau einmal.** Das Nachbuchen offener erster Anläufe (`wertung_offen`) läuft ohne Sperre: Zwei gleichzeitige Antworten desselben Kindes (zwei Tabs) könnten denselben offenen Fehler doppelt buchen. Lösung: offene Zeilen in einem Schritt beanspruchen (`update … set wertung_offen = false … returning` bzw. `for update skip locked`) und nur die beanspruchten buchen. Test, so weit ohne echte Gleichzeitigkeit möglich: zweimaliges Nachbuchen derselben Zeile bucht einmal.

**Sollte**
3. **H10 – Einlösen atomar:** `misch_buchen` bucht den Beleg nur, wenn das Einlösen tatsächlich eine Ausgabe getroffen hat (`update … returning`); eindeutiger Index auf offene Ausgaben je Kind und Bordkarte (nur, wenn im Bestand keine Dopplung liegt – vorher lesend prüfen und berichten); `schule.mischkarten` legt Ausgaben konfliktfest an.
4. **H10 – Ausgabe an die Lage binden:** In `misch_ausgabe` die Etappe mitschreiben, für die die Karten ausgeliefert wurden (Einheit, Lernziel); `misch_gueltig` vergleicht mit dieser gespeicherten Etappe statt mit den Angaben des Geräts.
5. **H2 – 30-Minuten-Grenze:** Offene erste Anläufe, die älter als 30 Minuten sind, auch beim Lesen des Flugs (`einheit_lesen_intern`) und beim Start eines Tests entscheiden – nicht erst bei der nächsten Übungsantwort. Test mit abgelaufener Zeit.
6. **H6 – Tageswechsel:** Der Zähler „heute selbst gelöst“ verwirft einen gespeicherten Stand, wenn der Server-Tag gewechselt hat (auch bei über Nacht offener Seite: beim nächsten Laden oder Antworten).

Migration als Datei mit Rauchtest (Rollback, nur Testkind); alle bisherigen Rauchtests müssen weiter laufen – nenne im Bericht, welche du angepasst hast. Die alte App (0.81.1) darf nicht brechen. Meldung „FERTIG: Auftrag I, Teil 3“.

## Teil 4 – Restpunkte des Gestalters aus Nachprüfung 2 (Chat `bau-lehrer`, **nach** Teil 3; App 0.81.3)

Grundlage: `inhalte/pruefung/lehrer/nachpruefung-2.md` (mit Bildern).
1. Umschalter „Nach Themengebiet | Nach Klasse (Lehrplan)“ auf dem Tablet ohne Trennung im Wort (kürzere Beschriftung „Themengebiet | Klasse“ unter 1100 px ist in Ordnung).
2. Plan links auf dem Handy: lange Überschriften nicht mitten im Wort trennen (kleinere Schrift, Pfeile unter den Text oder Kürzen mit „…“ wie auf dem Tablet).
3. Kann, wenn ohne Umbau: heller Verlauf auch links im Plan; gestrichelte Linie bei IB auch für ein Kind ohne MYP-Jahr (dann ganz oben); Legende auf Tablet und Rechner ohne inneres Rollen sichtbar; Vorlese-Namen der Knöpfe an die sichtbare Überschrift angleichen; doppeltes „–“ in der IB-Zelle für Klasse 5 weglassen; im Info-Text ein Satz, dass ein Pausentag nach dem Kalendertag am Aufenthaltsort des Kindes zählt.
4. **„Inhalte ansehen“: gesperrte Bordkarten heißen fälschlich „in Prüfung“** (Sebastian, 20.11., Bild: „54 Bordkarten (5 in Prüfung)“). In freigegebenen Flügen sind Bordkarten mit `freigegeben = false` nicht „in Prüfung“, sondern aussortiert: überzählige alte Übungen ohne Typ und alte Fassungen, die durch eine Korrektur ersetzt wurden. Sie werden nie wieder ausgegeben. Änderung: In der Zeile der Etappe nur die aktiven Bordkarten zählen („49 Bordkarten“); aussortierte nicht in der Liste zeigen, sondern am Ende der Etappe zugeklappt „5 aussortierte Bordkarten (ersetzt oder überzählig) anzeigen“; dort statt „in Prüfung“ das Wort „aussortiert“. „In Prüfung“ bleibt nur für Flüge, die als Ganzes noch Entwurf sind. Die Zahl der Bordkarten in der Lehrplan-Übersicht („Fertig · n Etappen · m Bordkarten“) zählt ebenfalls nur aktive. Info-Seite anpassen.
5. **Kinderansicht – nach der Landung nicht zurück in die Übungen** (Sebastian, 20.11.; Fehler aus dem Betrieb: Ein Kind landete die letzte Etappe eines Flugs, löste die Knobel-Bordkarte und wurde danach in die Übungen derselben Etappe zurückgeschickt – es übte 12 Bordkarten weiter, ohne zu merken, dass es fertig war).
   a) Nach einer Knobel-Bordkarte, die vom Landebildschirm aus gestartet wurde (richtig, falsch oder abgebrochen), geht es **zurück zum Landebildschirm** dieser Etappe – nicht in `zeichneUeben()`. Gleiches gilt für jeden anderen Rückweg vom Landebildschirm.
   b) Öffnet das Kind eine **schon gelandete Etappe** zum Üben, steht oben deutlich „Hier bist du fertig ✓“ mit **einem großen Knopf zum nächsten Schritt** (nächste offene Etappe · „Zum Test“, wenn alle Pflicht-Etappen gelandet sind · nächster Flug bzw. Abflugtafel, wenn der Flug geschafft ist). Weiterüben bleibt möglich, aber als zweiter, kleiner Knopf („Trotzdem weiterüben“). Nach jeder weiteren Bordkarte in einer gelandeten Etappe bleibt der Knopf zum nächsten Schritt sichtbar.
   c) Die Abflugtafel und „Weiter geht’s“ führen nie in eine gelandete Etappe, solange es einen nächsten Schritt gibt (prüfen und, falls nötig, berichtigen).
   d) **Reihenfolge am Ende einer Etappe (Sebastian, 20.11., ersetzt die frühere Fassung von d):** Die **Knobel-Bordkarte kommt immer von selbst hinten dran** – nicht als Angebot zur Auswahl. Ablauf: letzte Übung → „gelandet“ wird gebucht → sofort die Knobel-Bordkarte dieser Etappe (eine, die das Kind noch nicht gelöst hat; gibt es keine, entfällt der Schritt), mit einer Zeile darüber „Zum Schluss eine harte Nuss – falsch kostet nichts.“ → danach der Landebildschirm. Die Regeln der Knobel-Bordkarte bleiben (ein Versuch, falsch kostet nichts und zeigt den Weg, richtig = 30 Sterne, zählt nicht für „gelandet“). Ein kleiner Textlink „Heute keine Knobel-Bordkarte“ darf bleiben.
   e) **Nach der letzten Pflicht-Etappe kommt der Test von selbst** („Warum landet er zum Schluss nicht automatisch beim Test?“): Sind mit dieser Landung alle Pflicht-Etappen des Flugs gelandet, folgt nach der Knobel-Bordkarte und dem Landebildschirm **ohne Umweg die Startseite des Flug-Tests** – der Landebildschirm hat dann nur den einen großen Knopf „Jetzt zum Test“ („6 Bordkarten, ohne Tipps. Bestehst du ihn, ist der Flug geschafft.“; bei einem Nachtragstest „Test zu den neuen Etappen“; dazu, was für den Stempel des Ortes noch fehlt) und klein „Pause – zur Abflugtafel“. Öffnet das Kind einen Flug, in dem alle Pflicht-Etappen gelandet sind und nur der Test fehlt, kommt zuerst diese Aufforderung, nicht die Übungen; „Weiter geht’s“ auf der Abflugtafel führt dann direkt zur Testseite. Für gesetzte Flüge ohne Test (LB-3) entfällt das.
   f) **Test-Ergebnis: richtige Antworten deutlicher** (Rückmeldung eines Kindes: „nur ein ganz dünner grüner Rahmen“). In der Antwortliste nach dem Test jede Zeile klar als richtig oder falsch kennzeichnen: kräftige Fläche oder breiter linker Balken in Grün bzw. Rot, großes ✓ bzw. ✗ und das Wort „richtig“/„falsch“ – nicht nur Farbe (auch für Farbenblinde lesbar), in beiden Gestaltungen (hell und „nacht“), Kontrast gemessen. Oben die Summe groß („5 von 6 richtig“).
   g) **„Verbessern ›“ nach dem Test tut nichts** (Fehler aus dem Betrieb, 20.11.: Ein Kind hatte 4 von 6 im Flug-Test und konnte „Verbessern“ nicht antippen). Ursache (gelesen): `lernTestKnoepfe` verlinkt „Verbessern ›“ auf `…-test` – das ist die Adresse, auf der das Kind schon steht, also passiert nichts. Der Server würde die Korrektur starten (geprüft: `test_starten_intern` mit `art: korrektur` liefert für diesen Fall 2 Bordkarten). Änderung: Der Knopf startet die Korrektur direkt (wie „Verbessern starten“ auf der Testseite) bzw. zeichnet die Testseite neu. Nach dem Ergebnis mit Fehlern gibt es genau zwei klare Wege: groß „Erst üben: <Etappe> ›“ und daneben „Gleich verbessern ›“; beide müssen in beiden Gestaltungen funktionieren. Test dazu (Ergebnis mit Fehler → „Verbessern“ → Korrektur läuft). Prüfe bei der Gelegenheit alle Knöpfe und Links der Test- und Ergebnisseiten darauf, ob sie auf die eigene Adresse zeigen.
   h) **Nach bestandenem „Verbessern“ zeigt die App wieder „Verbessern“** (Fehler aus dem Betrieb, 20.11.): Das Kind hat beide Korrektur-Bordkarten richtig gelöst; in der Datenbank sind beide Etappen „korrigiert“ und der Flug „erledigt“ – die App bot danach trotzdem wieder „Verbessern“ an (vermutlich alter Stand der Seite: die Testseite rechnet mit den Daten von vor der Korrektur). Änderung: Nach jedem abgeschlossenen Test (Flug-Test, Verbessern, Nachtragstest, Nachtest) den Stand des Flugs neu vom Server laden, bevor Knöpfe gezeichnet werden; ist der Flug damit geschafft, erscheint „Flug geschafft“ mit dem nächsten Schritt und **kein** „Verbessern“. Test dazu (Korrektur vollständig richtig → kein Knopf „Verbessern“, stattdessen Flug geschafft).
   Nur diese Punkte a) bis h) – die neue Gestaltung des Landebildschirms und des Flug-Abschlusses folgt als eigener Bau-Auftrag AB (Entwurf des Gestalters, freigegeben).
Tests für 1, 2, 4 und 5 (Messung: kein Wort wird getrennt; Zählung ohne aussortierte; nach Knobel zurück zum Landebildschirm; gelandete Etappe zeigt den Knopf zum nächsten Schritt). Meldung „FERTIG: Auftrag I, Teil 4“.

---

# Bau-Auftrag LB (20.11.): Plan als Cockpit, Lehrplan nach Klasse je Thema, 4 Stufen, „Kann er – aber wiederholen“, Lehrpläne Realschule/IB

Von Sebastian freigegeben. **Maßgeblich ist die Vorgabe des Gestalters:** `inhalte/pruefung/lehrer/umsetzung-lb.md` (Befund, die 4 Stufen, Pakete LB-1 bis LB-5, „Fertig, wenn“; Fassung vom 20.11. 04:43 mit LB-5). **Leitidee:** Der Reiter „Plan“ ist das Cockpit des Lehrers – dort bearbeitet er den individuellen Lehrplan mit allen Funktionen. Entwurf zum Ansehen: `inhalte/pruefung/lehrer/entwurf/lehrplan-klasse-4-stufen.html` (echte Themen, Lernstand nur Beispiel). Bilder: `inhalte/pruefung/lehrer/bilder/lehrplan-klasse-gym8.png`, `lehrplan-klasse-rs7.png`. Gilt für Lehrer und Eltern; **die Kinderansicht bleibt bei Orten.**

Reihenfolge (es baut immer nur EIN Chat am App-Code): Bau-Auftrag I Teil 3 (`bau-motivation`) → **LB-3 Serverteil** (`bau-motivation`; von Sebastian am 20.11. bestätigt, ohne Vortest) → **Teil 4 + LB-1 + LB-2 + LB-5** (`bau-lehrer`). **LB-4** ist reine Inhaltsarbeit und läuft sofort nebenher.

## LB-4 – Lehrpläne Realschule und IB MYP, Lernbereiche (neuer Inhalts-Chat `lehrplan-lb`, Zweig `lehrplan-lb`, Meldungen `inhalte/postfach/lehrplan-lb.md`) – sofort

Je Thema in `inhalte/themenliste.json` ergänzen (alle 95 Themen):
- `reihenfolge.rs_by` und `reihenfolge.ib_myp`: Platz in der Lehrplan-Reihenfolge **innerhalb der Klasse** dieser Schulart (1, 2, 3 …; `reihenfolge.gym_by` gibt es schon – nicht ändern). Realschule: LehrplanPLUS Bayern, Mathematik, Wahlpflichtfächergruppe I (Abweichungen von II/III im Bericht nennen). IB: MYP Mathematics, Jahr 1–5 (MYP-Jahr = Klasse − 5).
- `lernbereich: { "gym_by": "…", "rs_by": "…", "ib_myp": "…" }`: Lernbereich bzw. Kapitel als Überschrift, so wie er im Lehrplan heißt (z. B. „M8 1 Funktion und Term“). Für das Gymnasium aus `lehrplan_gym` ableiten und gegen den Lehrplan prüfen. Hat ein Thema in einer Schulart keine Klasse, bleibt der Eintrag dort weg.
- `lehrplan_rs` und `lehrplan_ib`: Kompetenzerwartungen in derselben Form wie `lehrplan_gym` (kurz, in eigenen Worten, nichts wörtlich in Länge abschreiben). `lehrplan_andere` bleibt stehen, bis der Haupt-Chat es entfernt.
- **Klassen nicht ändern.** Das Feld `klasse` hat Sebastian am 18.11. festgelegt (und die Generatoren lesen es). Hältst du eine Klasse für falsch: als Liste im Bericht (Thema, heute, Vorschlag, Quelle) – nicht in der Datei ändern.
- Quelle zu jeder Angabe: Lehrplan-Seite mit Abschnitt und Abrufdatum im Bericht (je Klasse und Schulart eine Tabelle). Was sich nicht belegen lässt, als Annahme kennzeichnen; lässt sich eine Lehrplan-Seite nicht abrufen, das ausdrücklich sagen und nicht aus dem Gedächtnis füllen.
- **Dateiformat erhalten:** `themenliste.json` nicht neu formatieren (kein `json.dump` über die ganze Datei) – nur gezielt Felder einfügen, damit der Unterschied lesbar bleibt. Danach `python3 -I tools/inhalt_pruefen.py --alle` (muss OK bleiben).
- Selbstprüfung per Skript im Bericht: je Schulart und Klasse sind die Reihenfolge-Nummern lückenlos und eindeutig; jedes Thema mit Klasse hat einen Lernbereich; „Realschule Klasse 7“ hat 18 Themen (Stand Datenbank).
Kein App-Code, keine Datenbank, kein Merge nach `main`. Ein Commit je Schulart. Meldung „FERTIG: LB-4“. Der Haupt-Chat übernimmt die Felder in die Datenbank.

## LB-3 – „Kann er – aber wiederholen“, Serverteil (Chat `bau-motivation`, nach Teil 3; **von Sebastian bestätigt, ohne Vortest**)

Regel laut `umsetzung-lb.md`, Abschnitt LB-3: Der Lehrer setzt einen Flug auf „kann er – aber wiederholen“. Dann gelten alle Etappen des Flugs als gelandet, die Wiederholung beginnt bei Stufe 1 (fällig nach 1 Lerntag, dann 3, 7, 14, 30); es gelten die bestehenden Regeln (höchstens 6 Wiederholungen vor einem Flug; ein Fehler → am nächsten Lerntag wieder; zwei Fehler hintereinander → wieder offen). Kein Flug-Test und keine Flug-Nachtests für diese Flüge; „sicher“ = Wiederholung nach 14 Lerntagen bestanden (und eine Mischkarte richtig, falls eine kam). Mischkarten und Expeditionen dürfen daraus entstehen.
- Neues Feld je Kind und Ort analog `route.kann_schon_themen` (z. B. `kann_wdh_themen bigint[]`), setzbar über `api.schule_plan_setzen` (gleiches Muster wie `kann_schon_themen`, gleiche Prüfungen), lesbar über `schule_plan_lesen`.
- Buchung in `schule.karte_stand` mit erkennbarer Herkunft „gesetzt“ (z. B. Spalte `gesetzt_am`/`gesetzt_von`): für jede Pflicht- und Vertiefungs-Etappe des Flugs, die noch nicht gelandet ist, `sitzt = true`, Wiederholungsstufe 1, fällig am nächsten Lerntag. Schon vorhandene eigene Lösungen und schon gelandete Etappen bleiben unberührt.
- **Rücknahme:** Nimmt der Lehrer die Einstellung zurück, werden nur die „gesetzten“ Landungen wieder aufgehoben, bei denen das Kind seitdem nichts selbst gezeigt hat; eigene Lösungen, bestandene Wiederholungen und Sterne bleiben. Kein DELETE von Versuchen.
- `thema_stand`, `ort_stand`, `flug_nachtest`, `karte_sicher` und die Abflugtafel an die Regel anpassen (kein Flug-Test, kein Nachtest, „sicher“ ohne Nachtest); Sterne für den Ort wie bei „kann schon“ (keine Geschenk-Sterne für gesetzte Landungen – im Bericht nennen, wie du es löst).
- `schule_lernstand` bzw. `schule_plan_lesen` liefern je Flug, was die App für die 4 Stufen braucht: gesetzt (komplett/wiederholen), Etappen gesamt/begonnen/gelandet/sicher, kleinste Wiederholungsstufe, Lerntage bis zur nächsten Wiederholung, wieder offen, Rückreise/Test offen. Lieber der Server rechnet die Stufe (◉ ↻ ▶ ○) nach den Regeln der Tabelle „Die 4 Stufen“, die App zeigt sie nur.
- **„Wieder in die Wiederholung“ für ◉-Themen** (selbst geschafft oder „Kann er komplett“ gesetzt): eigene Aktion je Kind und Flug. Alle Etappen des Flugs starten erneut bei Wiederholungsstufe 1 (fällig am nächsten Lerntag); die bisherigen Belege bleiben als Verlauf erhalten (nichts löschen, „gelandet“ bleibt); Stufe ↻, nach bestandener Wiederholung am 14. Lerntag wieder ◉. Bei „Kann er komplett“ gesetzten Flügen ohne Karten-Stand entspricht das „Kann er – aber wiederholen“. Ein bestandener Flug-Test bleibt bestehen; ob für selbst geschaffte Flüge die Flug-Nachtests weiterlaufen, im Bericht festlegen und begründen (Vorschlag: sie laufen unverändert weiter).
- **Sammelaktionen:** Die vier Einstellungen (Lernen · Kann er – aber wiederholen · Kann er komplett · Aus dem Plan nehmen) und „Wieder in die Wiederholung“ müssen für mehrere Flüge in **einem** Aufruf gesetzt werden können (auch Flüge aus verschiedenen Orten und Orte, die noch nicht im Plan stehen), als ein Schritt mit **einer** Rücknahme („Rückgängig“ stellt den Zustand davor für alle betroffenen Flüge wieder her). Die vier Einstellungen schließen einander je Flug aus.
- Migration als Datei mit Rauchtest (Rollback, nur Testkind): 6 Flüge einer Klasse in einem Aufruf auf „wiederholen“ → am nächsten Lerntag fällig; ◉-Flug „wieder in die Wiederholung“; Rücknahme eines Sammelschritts; setzen → alle Etappen gelandet, am nächsten Lerntag fällig; zwei Fehler in der Wiederholung → wieder offen; Rücknahme; kein Flug-Test; Mischkarte möglich. Die alte App darf nicht brechen. Version 0.81.2 zusammen mit Teil 3 oder 0.81.3 – eine Meldung „FERTIG: LB-3 Serverteil“ mit der genauen Beschreibung der neuen Felder für `bau-lehrer`.

## Teil 4 + LB-1 + LB-2 + LB-5 – App (Chat `bau-lehrer`, nach `bau-motivation`; App 0.82.0)

- **Teil 4** des Bau-Auftrags I (Restpunkte des Gestalters) – soweit sie nach LB-1/LB-2 noch zutreffen.
- **LB-1 Lehrplan „Nach Klasse“ neu** – genau nach `umsetzung-lb.md`: eine Zeile = ein Thema; strenger Filter (nur Themen mit genau dieser Klasse in der gewählten Schulart); Reihenfolge = Lehrplan der gewählten Schulart mit Zwischenüberschrift je Lernbereich; Eingeplantes bleibt an seinem Platz; Stufe je Zeile; Aufklappen mit Lehrplan-Bezug, Kurzbeschreibung, Etappen mit Stand, „Inhalte ansehen“ und den 4 Knöpfen (Lernen bzw. „+ In den Plan“ · Kann er – aber wiederholen · Kann er komplett · Aus dem Plan nehmen); „+ In den Plan“ nimmt den Ort nur mit diesem Flug auf, die anderen Flüge des Ortes werden abgewählt; alles speichert sofort, mit „Rückgängig“. Oben nur „Gym 8: X von Y Themen im Plan oder schon gekonnt“ mit Balken – keine Zählung und kein Filter je Stufe.
- **LB-2 Die 4 Stufen überall** – gleiche Zeichen, Farben und Wörter in „Nach Themengebiet“, im Plan links (je Ort; aufgeklappt je Flug mit den 4 Knöpfen statt der Häkchen), in der Lehrplan-Übersicht (Stufe je Kind, Zeile wie LB-1, ohne Spalte „Ort“) und im Überblick bei „Zuletzt geschafft“.
- **LB-5 Plan = Cockpit** – nach `umsetzung-lb.md`, Abschnitt LB-5: links „Unser Lehrplan“, gegliedert nach Stufen (▶ Gerade dran · ○ Kommt noch, Reihenfolge ziehen oder ↑↓ wie heute · ↻ In Wiederholung mit „Wdh x von 5 · nächste in n Lerntagen“ · ◉ Kann er komplett, zugeklappt, mit Datum) – das ersetzt den Block „Geschafft“. Jede Zeile (Ort und aufgeklappt jeder Flug) zeigt die Stufe und dieselben Knöpfe wie LB-1, bei ◉ zusätzlich „Wieder in die Wiederholung“. **Auswahlmodus** (Häkchen je Thema) mit den Sammelaktionen links und rechts. Rechts der Lehrplan (Nach Themengebiet | Nach Klasse) mit Stufen und denselben Knöpfen – Themen lassen sich dort direkt setzen. Kopf in einer Zeile: „Gymnasium Kl. 8 · 3 ▶ · 9 ○ · 6 ↻ · 14 ◉ · Gespeichert · ↶ Rückgängig“ (kein Filter). Die Reihenfolge, in der das Kind lernt, bleibt die Reihenfolge der Orte unter „Kommt noch“/„Gerade dran“; an den Lernregeln und an der Kinderansicht ändert LB-5 nichts.
- Hinweise des Haupt-Chats: Lernbereich und Reihenfolge für Realschule/IB kommen aus LB-4; bis sie in der Datenbank sind, zeigt die App bei RS/IB „Reihenfolge vorläufig wie Gymnasium“ und keine Zwischenüberschriften (die App muss mit und ohne diese Felder laufen). Den Knopf „Kann er – aber wiederholen“ nur zeigen, wenn der Server das Feld kennt (LB-3 eingespielt). Themen ohne Klasse in der gewählten Schulart erscheinen in „Nach Klasse“ nicht. Die 10 aufgelösten Themen (Entwurf) erscheinen nirgends. Braucht die App neue Felder vom Server (Lernbereich, Lehrplan-Bezug, Kurzbeschreibung je Thema): Migration als Datei mit Rauchtest; die Felder für LB-4 legt diese Migration an (`schule.thema`: Lernbereich je Schulart, Lehrplan-Text je Schulart; die Reihenfolge je Schulart liegt in `schule.thema.lehrplan_reihenfolge`), befüllt werden sie vom Haupt-Chat.
- Tests für alle „Fertig, wenn“-Punkte aus `umsetzung-lb.md` (neun), soweit sie die App betreffen – darunter: 6 Themen aus Gym 7 in einem Schritt auf „Kann er – aber wiederholen“, ein ◉-Thema mit „Wieder in die Wiederholung“ zurückholen, alle Knöpfe im Plan erreichbar; Messung auf 400, 820 und 1280 px (kein Querrollen, kein Wort getrennt). Meldung „FERTIG: LB-1/LB-2/LB-5“ – der Gestalter prüft nach.


---

# Kinderansicht: Abschluss nach Etappe und Flug (20.11., Wunsch von Sebastian) – zuerst Entwurf des Gestalters

**Anlass:** Die Kinder merken nicht deutlich genug, wann sie fertig sind und dass jetzt etwas Neues kommt. Ein Kind hat nach der Landung endlos weitergeübt. Sebastian will: nach jeder Etappe eine **kleine Motivations-Ansicht, je nachdem wie das Kind es geschafft hat**; nach einem Flug eine **spektakulärere Ansicht** – und **unübersehbar, dass es jetzt zu einem neuen Thema geht**.

**Chat `pruefung-kinderansicht` (Gestalter), Zweig `pruefung-kinderansicht`: nur Entwurf und Beschreibung, kein App-Code.** Sebastian gibt den Entwurf frei, danach baut ein Bau-Chat.

**Was es heute gibt (lesen, nicht raten):** `lernen.js` – Landebildschirm im Übungsablauf (`lr-gelandet`: „ETAPPE n VON m“, Stempel „GELANDET“, Titel, „x Bordkarten selbst gelöst …“, Sterne, Knobel-Angebot, Knopf zur nächsten Etappe bzw. Test, „Zur Abflugtafel“), Abschluss des Flug-Tests („Flug geschafft! 🎉“ als eine Zeile), Abflugtafel. Beide Gestaltungen der Kinderansicht (hell und „nacht“) beachten. Regeln: `inhalte/README.md`, Abschnitt „Lernregel ‚gelandet‘ und ‚sicher‘“.

**Zu entwerfen**
1. **Abschluss einer Etappe** in drei Fassungen nach dem Verlauf – Zahlen, die der Server schon kennt (eigene Lösungen, Fehler, Tipps, Anläufe, Folge):
   - **auf Anhieb** (schnellster Weg: 6 Bordkarten, alle beim ersten Versuch) – z. B. „Direktflug“;
   - **sauber gelandet** (wenige Fehler);
   - **durchgekämpft** (viele Anläufe, Tipps, Stufe zwischendurch gesenkt) – ausdrücklich Anerkennung fürs Dranbleiben, nichts Abwertendes, kein Vergleich mit anderen Kindern.
   Dazu immer: was das Kind jetzt kann (ein Satz aus der Etappe), die Sterne, das Knobel-Angebot, und **ein** großer Knopf zum nächsten Schritt. Kurz – höchstens ein Bildschirm auf dem Handy, in wenigen Sekunden erfasst.
2. **Abschluss eines Flugs** (nach bestandenem Flug-Test): deutlich größer. Inhalt: „Flug geschafft“, die Etappen als Liste dessen, was das Kind jetzt kann; Ergebnis des Tests; Sterne; ein Hinweis, dass die Etappen in ein paar Tagen zur Wiederholung kommen (und warum). Dann als eigener, unübersehbarer Schritt: **„Neues Thema: <Titel des nächsten Flugs>“** – mit einem Satz, worum es geht, und dem Ort; wechselt dabei der Ort, gehört das dazu (Abschied vom Ort, Orts-Sterne, neuer Ort).
3. **Abschluss eines Orts** (alle Flüge des Orts geschafft): prüfen, was heute erscheint, und Vorschlag, wie es sich vom Flug-Abschluss abhebt.
4. **Bewegung und Ton:** Vorschlag für eine kurze Animation (ohne fremde Bibliothek, mit `prefers-reduced-motion` abschaltbar, höchstens 2 Sekunden, überspringbar); kein Ton ohne Einwilligung. Die Kinder sind 11 und 14 – nicht kindisch.
5. **Der Weg zum Test und zum Stempel:** Den Kindern war nicht klar, dass nach den Etappen der Flug-Test kommt und erst alle Flüge eines Ortes den Stempel bringen (ein Kind hatte alle Etappen beider Flüge gelandet, aber keinen Test gemacht und fragte nach dem Stempel). Zeige im Entwurf: nach der letzten Etappe die Aufforderung zum Test; auf dem Flug-Abschluss, was für den Stempel des Ortes noch fehlt; und eine kleine dauerhafte Anzeige des Wegs (Etappen → Test → Flug geschafft → Stempel).
6. **Was nach dem Abschluss nicht mehr passieren darf:** kein Weg zurück in die Übungen der fertigen Etappe ohne bewusste Wahl (der technische Fehler dazu wird schon in Bau-Auftrag I, Teil 4, Punkt 5 behoben – deine Entwürfe bauen darauf auf).

**Abgabe:** `inhalte/pruefung/kind/abschluss/umsetzung.md` (je Ansicht: Texte wörtlich, Aufbau, Regeln für die drei Fassungen mit Schwellen, welche Daten gebraucht werden und ob der Server sie schon liefert, „Fertig, wenn“), klickbarer Entwurf `inhalte/pruefung/kind/abschluss/entwurf/abschluss.html` (Handy 400 px und Tablet 820 px, hell und „nacht“, alle drei Etappen-Fassungen, Flug- und Orts-Abschluss) und Bilder davon. Wo es zwei gute Wege gibt: beide zeigen und einen empfehlen. Keine Kinderdaten, keine Namen; Beispiele mit „Kind A“. Meldung „FERTIG: Entwurf Abschluss“ in `inhalte/postfach/pruefung-kinderansicht.md`. Kein Merge.


---

# Bau-Auftrag AB (20.11.): Abschluss nach Etappe, Flug und Ort (Kinderansicht) – Entwurf 2 des Gestalters, von Sebastian freigegeben

**Maßgeblich:** `inhalte/pruefung/kind/abschluss/umsetzung.md` (Abschnitte 1–5 mit „Fertig, wenn“ je Ansicht; Abschnitt 7 Freigabe: Schwellen wie vorgeschlagen, Abzeichen werden im Reisepass gezählt). Klickbarer Entwurf: `inhalte/pruefung/kind/abschluss/entwurf/abschluss.html` (Handy/Tablet, hell/nacht, Bewegung umschaltbar). Bilder: `inhalte/pruefung/kind/abschluss/bilder/` (`uebersicht-etappe.png`, `uebersicht-flug-ort.png`, `uebersicht-tablet.png`).

**Zusätze von Sebastian (20.11.), gehen der Vorgabe vor:**
- **Ablauf:** Übungen → Knobel-Bordkarte (immer hinten dran, nicht zur Auswahl) → Abschluss-Ansicht der Etappe. Nach der letzten Pflicht-Etappe: Knobel-Bordkarte → Abschluss-Ansicht → **Flug-Test** → Abschluss-Ansicht des Flugs (und des Orts). Das Knobel-Angebot auf dem Blatt der Abschluss-Ansicht entfällt damit; die Vorgabe „beim Sturmflug kein Knobel-Angebot“ gilt so: Beim Sturmflug kommt die Knobel-Bordkarte nicht von selbst (das Kind hat sich gerade durchgekämpft) – sie steht dort nur als kleiner Textlink.
- **Test-Ergebnis:** richtige und falsche Antworten deutlich kennzeichnen (Teil 4, Punkt 5 f) – gilt auch für „Test ansehen“.

**Kurzfassung (die Vorgabe gilt):** 1. Etappe gelandet in drei Fassungen mit eigener Szene, Farbe, Abzeichen und Bewegung – *Direktflug* (alle Bordkarten im ersten Versuch richtig, ohne Tipp, genau so viele wie nötig; „6/6 AUF ANHIEB“, goldenes Abzeichen „Direkt“), *Saubere Landung* (höchstens 2 endgültige Fehler, Stufe nie gesenkt, höchstens 4 Bordkarten mehr als nötig; grünes Abzeichen „Sauber“; nach „wieder offen“ Titel „WIEDER GELANDET“), *Sturmflug gemeistert* (alles darüber; Ausdauer-Abzeichen, keine Fehlerzahl). Darunter immer ein Blatt: „Du kannst jetzt …“, Sterne, ein Satz zur Wiederholung, **genau ein** großer Knopf zum nächsten Schritt, Textlink „Pause – zur Abflugtafel“. Kein Weg zurück in die Übungen derselben Etappe. 2. Flug geschafft in zwei Bildschirmen: Gold-Szene mit Konfetti, je Etappe ein Licht, Sterne-Zähler, Liste „Das kannst du jetzt“, Hinweis zur Wiederholung, Knopf „Weiter zum nächsten Thema“ (Antwortliste nur über „Test ansehen“) → Bordkarte zum nächsten Flug, Knopf „Boarding: {Titel}“ öffnet die Erklärung der ersten Etappe. 3. Ort geschafft: Flug-Bildschirm 1 → Reisepass-Stempel mit „+100 Ort-Sterne“ → Bordkarte „VON {alter Ort} → NACH {neuer Ort}“, Knopf „Abflug nach {Ort}“. 4. Bewegung nur CSS, höchstens 1,8 Sekunden, überspringbar, bei „weniger Bewegung“ am Gerät aus, kein Ton.

## AB-S – Server (Chat `bau-motivation`, nach „Misch-Ausgaben wiederverwenden“; nur Migration und Rauchtest, kein `lernen.js`)
- Beim Landen liefert die Antwort auf eine Übung das Feld **`landung`**: Zahl der Bordkarten bis zur Landung, nötige Zahl (`ziel`), endgültige Fehler, Antworten mit Tipp, zweite Versuche, wie oft die Stufe gesenkt wurde, Lerntage, „wieder gelandet“ ja/nein – und die daraus berechnete **`landung_art`** (`direkt` | `sauber` | `sturm`) nach den Schwellen aus `umsetzung.md` Abschnitt 1 (die Schwellen als Einträge in `schule.regel`, nicht fest im Code). Gezählt wird seit dem Beginn bzw. seit dem letzten „wieder offen“ dieser Etappe; Mischkarten und Knobel zählen nicht.
- `landung_art` je Kind und Etappe **speichern** (z. B. `karte_stand.landung_art`, bei „wieder gelandet“ überschrieben; gesetzte Landungen aus LB-3 bekommen keine) und im Reisepass zählen: `schule_konto` (bzw. die Aktion, die den Reisepass speist) liefert `abzeichen: {direkt: n, sauber: n, sturm: n}`. Bestand: schon gelandete Etappen bekommen keine nachträgliche Art (nichts erfinden) – im Bericht nennen.
- **`sterne_flug`** im Ergebnis des Flug-Tests (Sterne dieses Tests und Summe der Sterne des Flugs), dazu was die App für Bildschirm 2 und den Orts-Abschluss braucht: nächster Flug bzw. nächster Ort des Kindes laut Plan (Titel, Ort, Themengebiet, erste Etappe), „Ort damit geschafft“ ja/nein, Orts-Sterne.
- Texte: je Etappe `kann` und je Thema `kurz` kommen aus AB-I; lege dafür die Ablage an (z. B. `schule.thema.kurz` und Tabelle `schule.etappe_text(thema_id, lernziel, kann)` – nicht in `einheit.inhalt`, weil freigegebene Flüge unveränderlich sind) und liefere sie in `schule_einheit_lesen` und im Test-Ergebnis mit; fehlt ein Text, liefert der Server `null` (die App nimmt dann „Kurz gesagt“ bzw. `umfang`).
- Rauchtest: je eine Landung `direkt`, `sauber`, `sturm` (auch „wieder gelandet“); Zählung im Reisepass; Test-Ergebnis mit `sterne_flug`, nächstem Flug und „Ort geschafft“. Die alte App darf nicht brechen. Meldung „FERTIG: AB-S“ mit genauer Feldbeschreibung für den App-Teil.

## AB-A – App (Chat `bau-motivation`, **erst wenn `bau-lehrer` mit App 0.82.0 fertig und zusammengeführt ist**; App 0.83.0)
Ansichten 1–3, Bewegung, Wege nach dem Abschluss, Abzeichen-Zeile im Reisepass („⚡ Direkt · ✓ Sauber · ⚡ Ausdauer“ mit Anzahl) – genau nach `umsetzung.md` und dem klickbaren Entwurf, mit den Zusätzen von Sebastian oben. Baut auf Teil 4, Punkt 5 (a–f) auf, der mit 0.82.0 kommt. Beide Gestaltungen (hell, „nacht“), Handy 400 px und Tablet 820 px; Tests für jedes „Fertig, wenn“ aus `umsetzung.md`; Bilder der fertigen Ansichten nach `docs/previews/ab/`. Meldung „FERTIG: AB-A“ – der Gestalter prüft nach.

## AB-I – Texte „kann“ und „kurz“ (drei neue Inhalts-Chats, sofort; reine Inhaltsarbeit)
Je freigegebenem Flug eine Datei **`inhalte/kann/<thema_schluessel>.json`**: `{"thema_schluessel": "…", "kurz": "…", "etappen": {"<lernziel>": "…", …}}`.
- **`kurz`** (je Thema): ein Satz, worum es in diesem Flug geht, in der Sprache der Kinder, höchstens 110 Zeichen, ohne Fachwort, das erst im Flug erklärt wird. Beispiel: „Du lernst, wie man Gleichungen Schritt für Schritt nach x auflöst.“
- **`kann`** (je Etappe, Schlüssel = `lernziel` aus `inhalt.etappen` der Themendatei, alle Etappen): setzt den Satz „Du kannst jetzt …“ fort, klein begonnen, ohne Punkt am Ende, höchstens 90 Zeichen, konkret und prüfbar. Beispiel: „gleichartige Glieder zusammenfassen, auch mit Minuszeichen“. Kein Lob, keine Wiederholung des Etappen-Titels Wort für Wort, nichts versprechen, was die Etappe nicht übt (Erklärung und Aufgaben der Etappe lesen).
- Aufteilung nach `klasse.gym_by` in `inhalte/themenliste.json`: **Chat `kann-1`** Klasse 5 und 6 · **Chat `kann-2`** Klasse 7 und 8 · **Chat `kann-3`** Klasse 9 und 10 und alle Themen ohne Gymnasium-Klasse. Die 10 aufgelösten Themen (in der Datenbank Entwurf: `groessen.verhaeltnisse`, `mengen.grundbegriffe`, `abbildungen.vektoren`, `funktionen.scharen`, `funktionen.folgen`, `finanzen.zinseszins`, `gleichungen.reinquadratisch`, `funktionen.transformation`, `funktionen.umkehr`, `stochastik.bedingt`) auslassen.
- Je Chat eigener Zweig (`kann-1`, `kann-2`, `kann-3`) vom aktuellen `lernen-app`, Meldungen in `inhalte/postfach/kann-<n>.md`. Selbstprüfung per Skript im Bericht: jede Etappe der Themendatei hat genau einen Eintrag, keine überzähligen Schlüssel, Längen eingehalten, gültiges JSON. Nur Dateien unter `inhalte/kann/` anlegen – keine Themendateien, keine Generatoren, kein App-Code, keine Datenbank, kein Merge. Ein Commit je Klasse. Am Ende „FERTIG: AB-I, Chat n“. Der Haupt-Chat bringt die Texte in die Datenbank.

---

# Bau-Auftrag LB, Teil 5 (20.11.): Mängel aus der Nachprüfung 3 des Gestalters (Chat `bau-lehrer`, App 0.82.2)

Grundlage: `inhalte/pruefung/lehrer/nachpruefung-3.md` (mit Bildern unter `inhalte/pruefung/lehrer/n3/`). Ergebnis der Nachprüfung: 5 von 8 „Fertig, wenn“ erfüllt, 2 teilweise geprüft, 1 nicht prüfbar (Server-Regel, durch Rauchtest `lb3` belegt). Zweig vom aktuellen `lernen-app` (App 0.82.1). Datenbank nur lesen; alle App-Tests; kein Merge nach `main`.

**Muss**
- **M1 Tablet 820 px: Lehrplan-Spalte zu schmal.** In „Nach Klasse“ bricht die Unterzeile in Silben („Fun / ktio / nen“, „Alge / bra“), lange Titel laufen in das Stufenwort. Unter 1100 px steht das Stufenwort **unter** dem Titel (wie auf dem Handy), Unterzeile ohne Silbentrennung; alternativ Spaltenbreite 55 % / 45 %. **Mit echten Thementiteln messen**, nicht mit Testdaten: Die Tests laden dafür die Titel aus `inhalte/themenliste.json` (längster Titel je Klasse) – kein Wort getrennt, keine Überlappung, bei 400, 820 und 1280 px.

**Sollte**
- **S1 Auswahlmodus kompakt:** Orte bleiben zugeklappt; je Ort ein Häkchen (wählt alle seine Flüge), daneben „▸ einzeln“ zum Aufklappen; je Abschnitt ein Häkchen „alle auswählen“. Die vier Knöpfe je Flug und „alle Flüge: kann er komplett“ sind ausgeblendet, solange ausgewählt wird. Die Sammelleiste bleibt oben stehen.
- **S2 Gleiche Einheit in Kopf und Abschnitten:** z. B. „○ KOMMT NOCH · 5 Orte, 8 Flüge“ – oder überall Flüge.
- **S3 Lehrplan-Übersicht wie „Nach Klasse“ gliedern:** nach Lernbereich und in Lehrplan-Reihenfolge der gewählten Schulart (heute nach Gebiet, darin nicht in Lehrplan-Reihenfolge).
- **S4 Etappen beim Aufklappen mit Titel** (nicht „Etappe 1 … 7“ mit Titel nur im Tooltip) und mit Stand (offen · begonnen · gelandet · sicher) – auf Tablet und Handy gibt es kein Überfahren mit der Maus.

**Kann**
- K1 Legende oben in der Lehrplan-Spalte zuklappbar oder einzeilig. K2 „Nach Themengebiet“: keine innere Bildlaufleiste, die Seite rollt. K3 IB-Lernbereiche: deutsche Bezeichnung zuerst, die englische in Klammern (nur Anzeige; die Daten bleiben). K4 Fehlt bei einem Thema der Lehrplan-Bezug für die gewählte Schulart (heute Gymnasium bei „Teilbarkeit und Primzahlen“ und „Intervalle“), zeigt die Zeile „Lehrplan:“ den Lernbereich statt leer zu bleiben.

Meldung „FERTIG: LB, Teil 5“ in `inhalte/postfach/bau-lehrer.md` – der Gestalter prüft nach. **Danach** beginnt `bau-motivation` mit AB-A.

---

# Bau-Auftrag LB-3, Nachbesserung (20.11.): drei Muss aus der Prüfung von ChatGPT (Werkstatt 881, 882) – Chat `bau-motivation`, nur Migration und Rauchtest, **vor** AB-A

LB-3 ist live (seit App 0.81.3; die Knöpfe seit 0.82.0). ChatGPT hat den Code gelesen (nicht ausgeführt) und drei Muss gefunden. Keine Bestandsänderung nötig – vorher lesend prüfen, ob es schon gesetzte Flüge gibt (`route.kann_wdh_themen`, `karte_stand.gesetzt_am`), und im Bericht nennen.

**Muss**
1. **Setzen startet die Wiederholung für ALLE Etappen des Flugs neu** (bestätigte Regel: „alle Etappen gelten als gelandet, Wiederholung ab Stufe 1“). Heute werden schon gelandete Etappen übersprungen und behalten ihre alte Wiederholungsstufe – ist alles schon sicher, steht der Flug sofort auf ◉ statt ↻. Neu: Beim Setzen gehen auch schon gelandete Etappen auf Wiederholungsstufe 1 (fällig am nächsten Lerntag) – **ohne** eigene Lösungen, ursprüngliche Landung (`sitzt_am`) oder Belege zu verlieren; ihre Herkunft bleibt „selbst gelandet“ (kein `gesetzt_am`). Der Stand vor dem Setzen wird im Schritt gemerkt, damit „Rückgängig“ ihn wiederherstellt. Test: ganzer Flug vorher sicher → nach dem Setzen ↻, Wiederholung am nächsten Lerntag.
2. **Rücknahme lässt keine unbelegte Landung stehen.** Heute genügt ein einziger Versuch nach dem Setzen (auch ein falscher oder offener), damit die gesetzte Landung bei der Rücknahme bleibt – nur die Herkunft fällt weg. Neu: Bei Rücknahme (und bei „Rückgängig“) bleibt eine gesetzte Etappe nur dann gelandet, wenn das Kind sie seit dem Setzen **nach der normalen Regel selbst gelandet** hätte (eigene Lösungen ≥ Ziel, Typen, schwere, Folge – dieselbe Prüfung wie in `karte_buchen`, als gemeinsame Funktion); sonst wird sie wieder offen. Alle Versuche, eigenen Lösungen und Sterne bleiben; die eigenen Lösungen seit dem Setzen zählen für die offene Etappe weiter. Tests: Setzen → ein Fehler → Rücknahme → offen; Setzen → offener erster Anlauf → Rücknahme → offen; Setzen → eine richtige Wiederholung → Rücknahme → offen (mit 1 eigener Lösung); echte eigene Landung seit dem Setzen → bleibt gelandet. Eine begonnene Expedition bleibt fortsetzbar (wie heute bei Rückfall).
3. **„sicher“ richtet sich nach dem Flug, nicht nach der Herkunft der Etappe.** Heute braucht eine selbst gelandete Etappe in einem gesetzten Flug weiter den Flug-Nachtest, den es für gesetzte Flüge nicht mehr gibt – sie kann nie „sicher“ werden, der Flug nie ◉. Neu: Solange der Flug auf „Kann er – aber wiederholen“ steht, gilt für **alle** seine Etappen: sicher = gelandet + Wiederholung nach 14 Lerntagen bestanden (+ Mischkarte richtig, falls seit dem Setzen eine **eingelöst oder gezeigt** wurde – nicht schon, wenn nur eine vorgeladen wurde). Test: eine selbst gelandete Etappe ohne Nachtest + eine gesetzte, Wiederholungen bestanden → beide sicher, Flug ◉.

**Sollte**
4. **Rückgängig nur für den jüngsten Schritt:** `rueckgaengig` nimmt nur die letzte `schritt_id` des Kindes an (sonst Meldung „Inzwischen wurde etwas anderes geändert.“). Test: A setzen → B ändern → A rückgängig wird abgelehnt.
5. **Stufe bei „Kann er komplett“ mit Rückfall:** Ist ein Flug „komplett“ gesetzt, aber eine früher gelandete Etappe wieder offen, liefert `thema_stufe` zusätzlich `wieder_offen` > 0 und ein Feld `hinweis: 'rueckfall'` – die Stufe bleibt ◉ (Entscheidung des Lehrers), die App kann es anzeigen.
6. **H6 Tageswechsel:** Server liefert zu `heute_tag` ein `heute_bis` (nächster Tagesbeginn in der Zeitzone des Kindes); die App-Seite dazu gehört zu AB-A.
7. Den wackeligen `i3_lernregeln_rauchtest.sql` vom Zufall der Kartenauswahl lösen (Eintrag im Postfach 07:10) – danach laufen auch die Kontext-Tests S4 dieses Blocks.

Migration `…_lb3_nachbesserung.sql` mit Rauchtest (Rollback, nur Testkind); alle bisherigen Rauchtests müssen weiter laufen (nenne, welche du anpasst – `lb3_rauchtest.sql` erwartet heute den alten Zustand von Punkt 1). Kein `lernen.js` in diesem Schritt. Meldung „FERTIG: LB-3 Nachbesserung“. **Danach** AB-A (App 0.83.0) auf dem Stand `lernen-app` mit App 0.82.2.

---

# Sechsundzwanzigste Runde (20.11.): Potenzgesetze in zwei eigene Flüge teilen – Entscheidung von Sebastian

Grundlage: `inhalte/postfach/lehrplan-lb.md`, Einträge „AUFTRAGSENTWURF: Potenzgesetze in zwei eigene Flüge teilen“ und „ENTSCHEIDUNG SEBASTIAN“ (beide lesen – sie gelten, soweit hier nichts anderes steht). Neuer Inhalts-Chat **`potenz-teilen`**, Zweig `potenz-teilen` vom aktuellen `lernen-app`, Meldungen `inhalte/postfach/potenz-teilen.md`. Vorher lesen: `inhalte/README.md` (Themen-Bausatz, Stufen und Aufgabentypen, Vertiefung), `inhalte/generatoren/_aufloesen.py` und `_af_plan.py` (Werkzeug zum Umziehen von Lernkarten aus der Vierundzwanzigsten Runde).

**Vom Haupt-Chat vergeben (nicht ändern):**

| | Flug A | Flug B |
|---|---|---|
| Titel | Potenzgesetze | Potenzgesetze mit ganzzahligen Exponenten |
| `thema_schluessel` | `terme.potenzgesetze_natuerlich` | `terme.potenzgesetze_ganzzahlig` |
| `thema_id` | 102 | 103 |
| Ort (`block_id`) | Samarkand (62) – wie `terme.umformen` | Mumbai (60) – wie `terme.bruchterme` |
| Themengebiet | Algebra | Algebra |
| `klasse` | `gym_by` 7 · `rs_by` 7 · `ib_myp` 4 | `gym_by` 8 · `rs_by` 7 · `ib_myp` 4 |
| `reihenfolge.gym_by` | 2 (hinter `terme.aufstellen`, vor `terme.umformen`) | 8 (hinter `terme.bruchterme`, vor `gleichungen.bruch`) |
| Lernbereich Gymnasium | „M7 1 Terme mit Variablen“ | „M8 4 Bruchterme und Bruchgleichungen“ |

**Flug A – aus `terme.umformen` herauslösen**
- Die vier Lernkarten ziehen um und **behalten ihre Lernziel-Schlüssel**: `mal_gleiche_basis`, `gleicher_exponent` (Pflicht), `geteilt_gleiche_basis`, `anwenden` (Vertiefung). Das ist zwingend – der Haupt-Chat hängt damit den Lernstand eines Kindes um, das alle vier schon gelandet hat.
- Die 22 Aufgaben mit negativen Exponenten gehen nach Flug B; in Flug A durch gleichwertige Aufgaben mit natürlichen Exponenten ersetzen (gleiche Stufe, gleicher Typ; auch die Testaufgabe von „Gleiche Basis: teilen“). Dazu kommen die Aufgaben aus „Fehler finden“ von `terme.potenzgesetze` (Gym 6), die ein Potenzgesetz voraussetzen (19 laut Zählung; die mit negativen Exponenten darunter gehen nach Flug B) – als Übungen vom Typ `fehler` in die passende Karte.
- Mindestmengen je Lernkarte wie überall (Stufe 1/2/3: 4/6/8 freie Übungen mit 2/3/4 Typen, 2 Knobel, Test 1, Korrektur 3, Sicherung 6). Einstieg des Flugs neu schreiben (Ziel, Vorwissen: Potenzbegriff aus Klasse 6).
- **`terme.umformen`:** die vier Lernziele aus den Lernkarten und aus `bewertung` streichen; es bleiben 8 Lernkarten. Einstieg/Ziel anpassen („Die Potenzgesetze stehen im Flug ‚Potenzgesetze‘“). Die übrigen 8 Karten nicht anfassen.
- **`terme.potenzgesetze` (Gym 6):** Titel „Potenzen und negative Exponenten“, `umfang` und der dritte Eintrag von `lehrplan_gym` an den echten Inhalt anpassen (kein Versprechen von Potenzgesetzen). In „Fehler finden“ bleiben nur Aufgaben zu Potenzbegriff, Hoch 0 und negativem Exponenten; reichen sie nicht mehr für die Mindestmengen, nachbauen.

**Flug B – neu bauen** (Lehrplan M8 4: Rechengesetze für Potenzen mit ganzzahligen Exponenten plausibel machen und in einfachen Fällen anwenden)
- Lernkarten wie im Auftragsentwurf (1 Warum die Gesetze auch für negative Exponenten gelten · 2 Gleiche Basis malnehmen und teilen · 3 Gleicher Exponent und Potenz einer Potenz · 4 Terme mit Variablen vereinfachen, auch als Bruchterm · 5 Fehler finden, Vertiefung). Eigene, sprechende Lernziel-Schlüssel (nicht die vier von Flug A). Die 22 Aufgaben aus Flug A und die betroffenen aus Gym 6 sind Startbestand. Vollständig nach dem Themen-Bausatz: Erklärung je Karte (Einstieg, Wörter, Bild, Schritte, typischer Fehler, „Kurz gesagt“), alle Pools, Typen, Stufen.
- Nichts voraussetzen, was in Gym 8 nach `terme.bruchterme` kommt.

**Themenliste** (`inhalte/themenliste.json`, Format erhalten, nur gezielt ändern): zwei neue Einträge mit allen Feldern, die die anderen Themen haben (`thema_id`, `thema_schluessel`, `datei`, Titel, Gebiet, `umfang`, `klasse`, `reihenfolge` für alle drei Schularten, `lernbereich`, `lehrplan_gym`, `lehrplan_rs`, `lehrplan_ib`). `reihenfolge.gym_by` der übrigen Themen nachziehen: **Klasse 7** – ab `terme.umformen` alles +1 (Flug A = 2); **Klasse 8** – ab `gleichungen.bruch` alles +1 (Flug B = 8). Für `rs_by` (Klasse 7) und `ib_myp` (MYP 4) beide Flüge wie im Auftragsentwurf einordnen und die folgenden Nummern nachziehen; Lernbereiche und Lehrplan-Bezüge mit Quelle (Abschnitt, Abrufdatum) – was nicht belegbar ist, als Annahme kennzeichnen. Selbstprüfung per Skript: Reihenfolge je Schulart und Klasse lückenlos und eindeutig.

**Texte für die Abschluss-Ansichten:** `inhalte/kann/terme.potenzgesetze_natuerlich.json` und `…_ganzzahlig.json` (Format wie die anderen Dateien dort: `kurz` ≤ 110 Zeichen, je Etappe `kann` ≤ 90 Zeichen, setzt „Du kannst jetzt …“ fort); `inhalte/kann/terme.umformen.json` und `terme.potenzgesetze.json` anpassen (die vier Lernziele dort streichen bzw. Texte an den neuen Inhalt angleichen).

**Prüfen und melden:** Generatoren für beide neuen Flüge und die zwei geänderten; `python3 -I tools/inhalt_pruefen.py --alle` muss OK melden; jede Lösung selbst nachrechnen. Bericht: Zahl der Aufgaben je Flug, Karte, Pool und Stufe; welche Aufgaben wohin umgezogen sind (alte → neue Stelle); Lehrplan-Quellen; was nicht geprüft wurde. Ein Commit je Flug + einer für Themenliste und Texte. **Nichts in die Datenbank schreiben, kein App-Code, kein Merge nach `main`, keine Kinderdaten.** Am Ende „FERTIG: Potenzgesetze geteilt“.

**Danach der Haupt-Chat:** Themen 102 und 103 in der Datenbank anlegen und den Orten zuordnen, Flüge einspielen (Entwurf), unabhängig prüfen lassen, den Lernstand des betroffenen Kindes von `terme.umformen` auf Flug A umhängen (Landungen, Wiederholungen, Nachweise – ohne Verlust; der abgeschlossene Ort bleibt abgeschlossen), Lehrplan-Felder nachziehen; Freigabe und Plan entscheidet Sebastian.

---

# Bau-Auftrag LB, Teil 6 (20.11.): Nachprüfung 4 des Gestalters – Lehrer-Ansicht

Grundlage: `inhalte/pruefung/lehrer/nachpruefung-4.md` (Bilder und Messwerte in `inhalte/pruefung/lehrer/n4/`). Teil 5 ist vollständig erledigt; neu aufgefallen sind fünf Punkte. Nur App (`lernen.js`/Stile), kein Server. Wird **zusammen mit AB-A** vom selben Bau-Chat gebaut (eine Version, 0.83.0).

1. **N1 – Muss:** Ansicht „Nach Themengebiet“ (Standard) bricht auf Tablet (820) 16 und auf dem Handy (400) 2 Wörter. Wie in „Nach Klasse“: unter 1100 px steht das Stufenwort unter dem Titel. Abnahme: maschinell gezählt 0 gebrochene Wörter bei 400, 820, 1280 in allen 8 Gebieten.
2. **N2 – Sollte:** Plan-Zeilen links auf Handy und Tablet: Titel bis zu zwei Zeilen, erst danach „…“.
3. **N3 – Sollte:** Abschnittszähler zählt nur die Flüge der eigenen Stufe („16 Orte · 20 Flüge in Wiederholung“), sodass Kopf und Abschnitt dieselbe Zahl zeigen.
4. **N4 – Kann:** „Nach Themengebiet“: eingeplante Zeilen nicht abblassen (wie „Nach Klasse“).
5. **N5 – Kann:** Etappen-Liste auf dem Handy: Stand rechtsbündig in derselben Zeile wie der Titel.
6. **Aus LB-3 Nachbesserung (Sollte 4):** Die App bietet „↶ Rückgängig“ nur noch für den jüngsten Schritt an; die Ablehnung des Servers („Inzwischen wurde etwas anderes geändert.“) verständlich anzeigen. Rückfall-Hinweis (`hinweis: 'rueckfall'`, `wieder_offen`) in der Lehrer-Ansicht zeigen; `heute_bis` statt eigener Tagesrechnung verwenden, wo die App „heute“ bestimmt.

Tests ergänzen (mindestens N1 als Messung, N3, Punkt 6), alle Tests laufen lassen. Meldung im Postfach, am Ende „FERTIG: LB Teil 6“.

---

# Bau-Auftrag LB, Teil 7 (20.11.): Info-Seite „So funktioniert’s“ auf den Stand 0.82.2 bringen

Vorgabe des Gestalters mit allen neuen Texten **wörtlich**: `inhalte/pruefung/lehrer/info-seite-update.md` (Punkte 1–7). Nur Texte in `lernen.js` (`viewInfo` und `LERN_INFO_FRAGEN`), keine Datenbank. Wird vom selben Bau-Chat zusammen mit AB-A und Teil 6 gebaut (0.83.0).

- Punkte 1–7 genau nach Vorgabe übernehmen; die doppelten alten Einträge „Lernstand:“ und „Was wackelt?:“ löschen.
- Abschluss-Ansichten und Abzeichen (AB-A) kommen in derselben Version: dafür einen kurzen Eintrag ergänzen, der genau das beschreibt, was AB-A zeigt (Text im Bericht nennen, der Gestalter prüft ihn).
- Punkt 3 („Kann er – aber wiederholen“) beschreibt den Stand **nach** der LB-3-Nachbesserung am Server; steht die beim Live noch aus, meldet der Haupt-Chat das.
- Tests: vorhandene Info-Seiten-Tests anpassen. Im Bericht „FERTIG: LB Teil 7“; der Gestalter prüft den Text gegen die App.

---

# Siebenundzwanzigste Runde (20.11.): Unabhängige Prüfung der geteilten Potenzgesetz-Flüge

Prüf-Chat **`pruefung-potenz`**, Zweig `pruefung-potenz` vom aktuellen `lernen-app`, Bericht `inhalte/pruefung/potenz/bericht.md`, Meldung `inhalte/postfach/pruefung-potenz.md`. Grundlage: Sechsundzwanzigste Runde und der Bericht in `inhalte/postfach/potenz-teilen.md` (auch „Abweichungen vom Auftrag“ 1–6). Nur prüfen, nichts an den Inhalten ändern.

Geprüft werden `inhalte/themen/terme.potenzgesetze_natuerlich.json` (Flug A, 191 Aufgaben), `terme.potenzgesetze_ganzzahlig.json` (Flug B, 175), `terme.potenzgesetze.json` (Karte „Fehler finden“, alle 32) und `terme.umformen.json` (nur: fehlen genau die vier Karten, ist der Rest unverändert, stimmen Einstieg/Ziel).

1. **Jede Aufgabe selbst nachrechnen** (Lösung, alle falschen Antworten samt Begründung, Lösungsweg, Tipp) – unabhängig vom Generator, mit eigenem Skript oder von Hand; Ergebnis je Aufgabe.
2. **Trennung:** Flug A enthält nirgends negative Exponenten (Text, Antworten, Lösungsweg, Ergebnis); Gym 6 setzt kein Potenzgesetz voraus; Flug B setzt nichts voraus, was in Gym 8 nach Bruchtermen kommt.
3. **Lehrplan:** passt Flug B zu M8 4 („plausibel machen und in einfachen Fällen anwenden“) – nicht zu schwer, nicht zu leicht? Passen Stufe und Typ je Aufgabe (insbesondere die 23 nach Flug A umgezogenen Aufgaben, jetzt alle Stufe 3 „fehler“, und die in Flug B umgestuften 29)?
4. **Erklärungen von Flug B** (5 Karten): fachlich richtig, für Klasse 8 verständlich, typischer Fehler treffend.
5. **Themenliste und kann-Texte** der vier Flüge: Titel, `umfang`, Lehrplan-Bezüge, Reihenfolgen plausibel; kann-Texte treffen den Inhalt.

Bericht: Muss / Sollte / Kann mit Fundstelle (Flug, Karte, Fragetext), dazu was nicht geprüft wurde. Keine Kinderdaten, nichts in die Datenbank, kein App-Code. Am Ende „FERTIG: Prüfung Potenz“.

**Nachtrag zur Sechsundzwanzigsten Runde – Entscheidung Sebastian (20.11.):** In Flug A werden die vier leichten „Stimmt die Rechnung? …“-Aufgaben (aus Gym 6 umgezogen, derzeit Stufe 3 „fehler“ in `mal_gleiche_basis`) zu **Stufe 1, Typ „erkennen“**. Grund: Eine Landung verlangt eine gelöste Stufe-3-Aufgabe; leichte Aufgaben dort entwerten die Hürde. `potenz-teilen` setzt das zusammen mit den Ergebnissen der Siebenundzwanzigsten Runde um (eine Nachbesserung, nicht zwei); der Prüf-Chat nennt weitere Stufe-3-Aufgaben, die zu leicht sind.

---

# Achtundzwanzigste Runde (20.11.): Potenzgesetz-Flüge nachbessern – nach der unabhängigen Prüfung

Chat **`potenz-teilen`** (weiter auf seinem Zweig, vorher `lernen-app` holen). Grundlage: `inhalte/pruefung/potenz/bericht.md` – jede Fundstelle dort genau lesen. Kein Rechenfehler gefunden; es geht um Trennung, Ablenker, Stufe/Typ, Einordnung.

**Muss**
1. Gym 6, `negativer_exponent`, Aufgabe 35: Tipp ohne Potenzgesetz („Rechne beide Potenzen aus und teile.“).
2. Flug A, `mal_gleiche_basis`, Aufgabe 11: Tipp ohne negative Exponenten.

**Sollte (alle umsetzen)**
1. Gym 6: Tipps zu Hoch 0 (Aufgaben 31, 37) ohne Quotientengesetz, über das Muster der Lernkarte.
2. Flug A, `geteilt_gleiche_basis`, Aufgaben 131 und 135: nach Flug B verlegen und in Flug A gleichwertig ersetzen (erster Exponent nie kleiner).
3. Flug A: die sechs unpassenden Ablenker (Aufgaben 14, 16, 18, 68, 88, 136) durch typische Fehler ersetzen, die zur jeweiligen Rechnung passen.
4. **Stufe und Typ der 23 umgezogenen Aufgaben** (Entscheidung Sebastian + Prüfbericht; ersetzt „alle Stufe 3 fehler“ aus der Sechsundzwanzigsten Runde): die **sechs** „Stimmt die Rechnung?“ mit richtiger Rechnung (2, 4, 6, 112, 116, 122) → Stufe 1 `erkennen`; 26 → `parameter`; 31 → `rueckwaerts`; 178 → `begruenden`; 43 zurück in den Knobel-Pool oder ersetzen (zu nah an 44). Stufe folgt dem Typ laut README. Danach Mindestmengen und Typ-Mischung je Karte neu prüfen (Stufe 3 von `mal_gleiche_basis` nicht mehr von „fehler“ beherrscht).
5. **IB:** Flug A nach MYP 3, vor `terme.umformen` (wie im Gymnasium); Reihenfolgen MYP 3 und MYP 4 nachziehen, weiter als Annahme gekennzeichnet.
6. Flug A: Aufgaben 75, 76 bekommen einen Typ; 30, 154, 156 einheitlich einstufen.

**Kann (umsetzen):** 1 („Bruch“ statt „Bruchterm“, wo der Begriff in RS/IB noch fehlt) · 2 (Hinweis-Satz in „Gleiche Basis: teilen“) · 3 (`offen` in Gym 6 bereinigen) · 4 (`lehrplan_rs` von `terme.umformen`) · 5 (kann-Text `kurz` Gym 6) · 7 (Einstieg `terme_vereinfachen`). Kann 8 bleibt.

**Kann 6 („Potenzen von Potenzen“ als Karte in Flug A, M7 1.2): nur bauen, wenn der Haupt-Chat Sebastians Ja im Postfach meldet.** Dann als **Pflichtkarte** mit eigenem Lernziel-Schlüssel `potenz_von_potenz`, vollständig nach Bausatz; die vier bestehenden Schlüssel bleiben unverändert.

Prüfskript `--alle` OK, Selbstprüfung der Reihenfolgen, Bericht mit alt → neu je geänderter Aufgabe. Nichts in die Datenbank, kein App-Code. Am Ende „FERTIG: Potenz nachgebessert“.

---

# Nachträge aus ChatGPTs Prüfergebnis 885 (20.11.)

Ergebnis: Die drei Muss aus 881/882 sind geschlossen; kein neues Muss in i4, i5, AB-S. Offen sind nur Sollte.

**An `bau-lehrer` (nur Server-Tests, kein App-Code) – „LB-3 Tests ergänzen“:**
1. `lb3_nachbesserung_rauchtest.sql`: zusätzlicher Fall **ohne direktes Setzen der Nachweisfelder** – ein gesetzter Flug, das Testkind erarbeitet eine Etappe wirklich über `uebung_pruefen_intern` (Ziel-Anzahl verschiedener richtiger Bordkarten, nötige Typen, eine schwere, Folge), danach Rücknahme → diese Etappe bleibt gelandet, die anderen werden offen.
2. `i4_misch_ausgabe_rauchtest.sql`: Fall „zweimal derselbe Flug → dieselben gültigen Karten; Flugwechsel → bisherige verfallen; zurückwechseln → neu ausgegeben; älter als 24 h → verfallen“.
3. `ab_s_abschluss_rauchtest.sql`: `test_abschliessen_intern` bei nicht bestandenem Test, bei Verbessern/Nachtragstest und beim erneuten Aufruf – was liefern `flug`, `naechster_flug`, `sterne_flug`? Ergebnis melden; liefert der Server die Felder auch dort, per Migration auf den erstmaligen Flug-Abschluss beschränken (Datei, nicht ausführen).
Am Ende „FERTIG: LB-3 Tests ergänzt“.

**Für AB-A / Teil 6 / Teil 7 (`bau-motivation`, in 0.83.0 mit beachten):**
- Abschluss-Ansicht des Flugs **nur beim erstmaligen Abschluss** zeigen (`einheit_abgeschlossen` und Flug-Test, nicht Verbessern/Nachtragstest, nicht beim erneuten Öffnen).
- Wiederlandung: Text „WIEDER GELANDET“, nicht „fehlerfreie Landung“ – auch wenn der Server `sauber` meldet.
- Abzeichen: zeigt die Art der **letzten** Landung; so beschriften („Abzeichen der letzten Landung“), kein Eindruck, ein früheres Abzeichen sei verloren.
- Rückfall-Hinweis (`hinweis: 'rueckfall'`) in der Lehrer-Ansicht sichtbar – ◉ allein wäre irreführend (steht schon in Teil 6, Punkt 6).
- `heute_bis`: Die Kinder-Ansicht aktualisiert „heute“ beim Tageswechsel von selbst (Test dazu).
- Info-Seite (Teil 7): ein Satz, dass „Rückgängig“ den Stand einer selbst gelandeten Etappe nicht zurückdreht, wenn das Kind inzwischen weitergeübt hat.

---

# Nachträge 20.11. nachmittags

**A – `bau-lehrer`: „Flug geschafft“ auch nach Verbessern (Entscheidung Haupt-Chat, im Sinne von Sebastians Vorgabe „nach einem Flug eine spektakulärere Ansicht“).** `supabase/migrations/20261120_ab_s_flug_abschluss_einmal.sql` ist **nicht eingespielt** und wird so geändert: `flug_geschafft` = dieser Aufruf schließt die Sitzung ab **und der Flug wird dadurch zum ersten Mal fertig** – egal ob über den Flug-Test (`blocktest`) oder über Verbessern (`korrektur`). Weiter false: nicht bestandener Test, Nachtragstest, Nachtest, erneuter Aufruf einer anderen Sitzung, alles nach dem ersten Fertigwerden. Erneuter Aufruf derselben Sitzung liefert dasselbe wie beim ersten Mal. Rauchtest 9c entsprechend (Verbessern, das den Flug erstmals fertig macht → `flug_geschafft` true mit Feldern; zweites Verbessern/Nachtest → false). Nur Datei, nicht ausführen. „FERTIG: flug_geschafft“.

**B – `bau-motivation` (erst nach A und nach dem Live von 0.83.0): App 0.83.1** – Abschluss-Ansicht des Flugs an `flug_geschafft` (oder `ort_geschafft`) hängen statt an `einheit_abgeschlossen`; fehlt das Feld (alter Server), Verhalten wie 0.83.0. Tests. „FERTIG: 0.83.1“.

**C – `pruefung-potenz`: Nachprüfung der Nachbesserung.** Grundlage: Bericht „FERTIG: Potenz nachgebessert“ in `inhalte/postfach/potenz-teilen.md` (Entscheidungen 1–7 dort). Prüfen: (1) die neue Pflichtkarte `potenz_von_potenz` in Flug A vollständig – alle 35 Aufgaben nachrechnen, Erklärung, keine negativen Exponenten, passt zu M7 1.2; (2) jede in der Nachbesserung geänderte oder ersetzte Aufgabe (Liste alt → neu im Bericht); (3) sind Muss 1–2 und Sollte 1–6 wirklich erledigt; (4) die Umstufungen aus Entscheidung 1 (8 Aufgaben auf Stufe 1 „erkennen“) und die zwei Aufgaben ohne Typ (Entscheidung 3) vertretbar? Bericht `inhalte/pruefung/potenz/nachpruefung.md`, Muss/Sollte/Kann. „FERTIG: Nachprüfung Potenz“.

---

# Bau-Auftrag LB, Teil 8 (20.11.): Aufgeklappte Themen-Karte im Lehrplan kompakter – Variante A (von Sebastian gewählt)

Betrifft die aufgeklappte Themen-Karte im Lehrplan des Plans, Ansichten „Nach Klasse“ und „Nach Themengebiet“ (LB-2). Vorlage: Entwurf des Gestalters im Chat mit Sebastian („Variante A“); es gibt keine Entwurfsdatei – die folgende Beschreibung ist die Vorgabe. Nur App, kein Server. Wird von `bau-motivation` zusammen mit Nachtrag B (`flug_geschafft`) als **0.83.1** gebaut.

Heute: vier große Felder für die Stufen (je zwei Zeilen Erklärung) nehmen die halbe Karte ein, „Inhalte ansehen ›“ ist nur ein kleiner Link neben dem Ort, darüber neun Etappen-Kästchen.

Neu, von oben nach unten:
1. Kopf unverändert: Zeichen + Thema, darunter Themengebiet · Klassen; rechts Stufe und „im Plan“.
2. „Lehrplan: …“ und der Beschreibungstext unverändert.
3. Eine Zeile: Knopf „Inhalte ansehen (n Etappen)“ mit Rahmen in Akzentfarbe (öffnet wie bisher die Inhalte des Themas), daneben klein und grau „Ort: <Ort>“. Die Etappen-Kästchen entfallen.
4. Trennlinie, darunter eine Zeile: „Stufe ⓘ“ (ⓘ führt zu „So funktioniert’s“, Abschnitt zu den Stufen), dann drei schmale Knöpfe nebeneinander: „Lernen“, „Kann er – wiederholen“, „Kann er komplett“. Der aktive Knopf grün hinterlegt mit ✓. Keine Erklärungszeilen unter den Knöpfen.
5. In derselben Zeile ganz rechts als roter Textlink (kein Kasten): „Aus dem Plan nehmen“. Für Themen außerhalb des Plans steht dort stattdessen „In den Plan nehmen“.

Wirkung und Speichern der Stufen bleiben unverändert (LB-3, LB-5), nur die Darstellung ändert sich. Der Rückfall-Hinweis aus Teil 6 bleibt sichtbar.
Handy (400 px): Die Knöpfe dürfen umbrechen; „Aus dem Plan nehmen“ dann in eigener Zeile darunter, rechtsbündig.
Abnahme bei 400, 820 und 1280 px: kein Wort mitten im Wort umbrochen, die Karte zugeklappt unverändert. Tests ergänzen. Offene Punkte (z. B. Etappen-Liste mit Stand aus Teil 5 S4 – bleibt sie hinter „Inhalte ansehen“ erreichbar?) im Bericht nennen. „FERTIG: LB Teil 8“.

---

# Bau-Auftrag LB, Teil 9 (20.11.): Nachprüfung 5 (Lehrer) und Nachprüfung Abschluss (Kind) – App 0.83.2

Grundlage: `inhalte/pruefung/lehrer/nachpruefung-5.md` (N6–N8, Info-Seite) und `inhalte/pruefung/kind/abschluss/nachpruefung.md` (N1–N5); Fundstellen und Bilder dort. Teil 6 und Teil 7 sind bestätigt. Nur App. `bau-motivation`, Version 0.83.2.

**Lehrer-Ansicht**
1. **N6 (Sollte):** Gewählter Themengebiet-Knopf (`aria-pressed="true"`) bleibt beim Hover dunkel mit weißer Schrift.
2. **N7 (Sollte):** Plan links auf dem Handy: Titel nur das Thema, Themengebiet klein und grau in der Zeile darunter; ↑ ↓ kleiner (32 px) oder untereinander. Ziel bei 400 px: höchstens wenige Titel mit „…“, nie Trennstrich und „…“ hintereinander.
3. **N8 (Kann):** bleibt wie es ist, bis Sebastian entscheidet (Wort „Themen“ in der Lehrer-Ansicht).
4. **Info-Seite (Kann):** Schritt 1 „Rechts (auf dem Handy darunter) der Lehrplan“.

**Abschluss-Ansichten (Kind)**
5. **N1 (Sollte):** Datum im Ort-Stempel ohne doppelten Punkt („20.11.“).
6. **N2–N5 (Kann):** wie im Bericht (Abstand unter „2/2“, Blitz beim Sturmflug hinter dem Text bei 360 × 640, N4 laut Bericht, „Überspringen ›“ lesbar).

Tests ergänzen (N6, N7 als Messung, N1), alle laufen lassen. „FERTIG: 0.83.2“.

---

# Entscheidungen Sebastian (21.11.) – „alles wie empfohlen“

1. **Neue Pflicht-Etappe „Potenzen von Potenzen“ (Flug A):** Das betroffene Kind übt sie normal (Landung, dann Nachtragstest); sie wird nicht gesetzt. Der Ort zeigt bis dahin wieder einen offenen Flug; Stempel und Orts-Sterne bleiben.
2. **Flug A, sieben Aufgaben „Ein Kind rechnet … Was ist falsch?“ / „Welcher Satz beschreibt den Fehler richtig?“** (6 in `mal_gleiche_basis`, 1 in `gleicher_exponent`, derzeit Stufe 1 `erkennen`): bekommen **keinen Typ** (überzählig, werden beim Einspielen gesperrt, nicht gelöscht). → **`potenz-teilen`, Neunundzwanzigste Runde:** genau das umsetzen, dazu aus der Nachprüfung Kann 2 (zwei Ablenker, die eine Basis verlieren), Kann 4 („2¹⁰ : 2ⁿ = 16“ → Stufe 2 `umkehr`), Kann 6 (Wort „potenziert“ einfacher), Kann 7 (Flug B `exponent_und_potenz` verweist auf Klasse 7). Mindestmengen und Typ-Mischung danach prüfen, Prüfskript `--alle` OK. „FERTIG: Potenz Runde 29“.
3. **Etappen-Liste mit Stand im Plan kommt zurück** → Ergänzung zu **Bau-Auftrag LB, Teil 9 (0.83.2):** in der kompakten Themen-Karte ein zugeklappter Textlink „Etappen ▸“ in der Inhalte-Zeile; aufgeklappt die Liste wie in 0.83.0 (Nummer, Titel, Stand rechtsbündig).
4. **Wort „Themen“ in der Lehrer-Ansicht ist erlaubt** → Ergänzung zu Teil 9, Punkt 3: Der Test „Reisewörter“ gilt nur noch für Kinderseiten; auf Eltern-/Lehrerseiten sind „Thema/Themen“ und „Themengebiet“ zulässig. Bestehende Texte der Info-Seite bleiben, wie sie sind.

---

# Nachträge aus ChatGPTs Prüfergebnis 888 (21.11.) – `flug_geschafft`

- **MUSS 1 (alte Sitzungen mit `flug_geschafft` NULL sperren einen späteren ersten Abschluss):** im Code zutreffend. Bestand geprüft (21.11.): Es gibt 7 alte abgeschlossene Flug-Test-/Verbessern-Sitzungen, alle gehören zu Flügen, die schon fertig sind – der Fall „alter nicht bestandener Test, Flug noch offen“ existiert nicht und kann nicht mehr entstehen (neue Sitzungen bekommen den Wert beim Abschließen). Keine Änderung nötig; `bau-lehrer` ergänzt trotzdem den Regressionstest (alte Sitzung NULL + Flug offen → späteres Verbessern liefert true) und macht die Bedingung robust (alte NULL-Sitzung zählt nur als früherer Abschluss, wenn der Flug vor diesem Aufruf schon einmal fertig war). Datei, nicht ausführen.
- **`bau-lehrer`, Tests:** Fälle 9c/9d dürfen nicht mehr mit „Info“ übersprungen werden (feste Testvorbereitung, harte Prüfung); eigener Negativfall „Nachtest“.
- **`bau-motivation`, in 0.83.3:** Meldet der Server nur `ort_geschafft` (ohne `flug_geschafft`), zeigt die App direkt Ort-Stempel und Bordkarte, nicht noch einmal „Flug geschafft“. Test dazu.
- Nicht übernommen (bekannte Grenze): Abschluss-Daten beim Wiederöffnen werden neu berechnet (kein Schnappschuss); Sperre gegen zwei gleichzeitig laufende Tests desselben Flugs.

---

# Dreißigste Runde (21.11.): Lehrplan-Prüfung – Zuordnungen und Voraussetzungen der Themenliste

Chat **`lehrplan-lb`** (Inhalte, kein App-Code), Zweig `lehrplan-lb` auf den Stand von `lernen-app` bringen, Meldung `inhalte/postfach/lehrplan-lb.md`. Anlass: Sebastians Übersichtsblatt „Mathe 5–10 – was gelernt wird“ (Matrix Klasse × Themengebiet aus `inhalte/themenliste.json` und `schule.voraussetzung`) zeigt Lücken. Auftrag des Gestalters, vom Haupt-Chat übernommen.

**1. Themen ohne Klasse prüfen (Gymnasium Bayern)**
- **Reinquadratische Gleichungen:** `gym_by` fehlt, ist aber harte Voraussetzung für „Quadratische Gleichungen (allgemein)“ (Gym Kl. 9). Entweder Gym Kl. 9 zuordnen oder die Voraussetzung für Gym anders lösen. Danach prüfen, ob ein Gymnasiast das Thema im Plan bekommt.
- **Graphentransformation, Umkehrfunktionen, Wurzelgleichungen:** im LehrplanPLUS Gymnasium enthalten? Wenn ja, Klasse und Lernbereich eintragen, sonst kurz begründen, in welchem Thema es steckt.
- **Realschule:** Formeln umstellen (steckt laut Umfang in „Prismen und Zylinder“, Kl. 9) – bestätigen oder zuordnen.
- Die übrigen Themen ohne Klasse (IB-Themen, Entdecker-Inseln, reiner Realschul- bzw. Gymnasialstoff) sind plausibel; nur stichprobenartig bestätigen.

**2. Realschule:** Klasse 7 hat 20 Themen, Klasse 8 nur 7 – Zuordnung gegen LehrplanPLUS RS prüfen.

**3. Voraussetzungen (`schule.voraussetzung`) vervollständigen:** 70 Verbindungen, aber 18 Gym- und 19 RS-Themen haben keine einzige, darunter Dezimalzahlen, Volumen, Potenzgesetze, Winkelsätze, Prismen und Zylinder, Kreis und Tangenten. Für jedes Thema mit Klasse: mindestens die direkten Voraussetzungen („hart“ oder „empfohlen“, mit Begründung) eintragen oder ausdrücklich als „eigenständig“ kennzeichnen. Ziel: Man kann eigenständige Themen von Datenlücken unterscheiden.

**Rahmen (Haupt-Chat):**
- **Die Datenbank bleibt beim Haupt-Chat.** Du liest nur (Tabellen `schule.thema`, `schule.voraussetzung`, `schule.thema_jahrgang`, `schule.block_thema`) und lieferst: (a) Änderungen an `inhalte/themenliste.json` im Zweig, (b) eine Migrationsdatei `supabase/migrations/20261121_lehrplan_zuordnung_voraussetzungen.sql` (wiederholt ausführbar, kein DROP/DELETE, nicht ausführen) samt kurzem Rauchtest, (c) die Liste der Änderungen mit Quelle (LehrplanPLUS-Abschnitt, Abrufdatum) je Änderung; Unbelegtes als Annahme kennzeichnen. Fehlt in `schule.voraussetzung` eine Möglichkeit, „eigenständig“ festzuhalten, schlage die kleinste Ergänzung vor (z. B. Kennzeichen am Thema) – als Teil der Migrationsdatei.
- **Stand beachten:** Die Themenliste enthält schon die zwei neuen Flüge `terme.potenzgesetze_natuerlich` (102) und `terme.potenzgesetze_ganzzahlig` (103) und den geänderten Titel von `terme.potenzgesetze`; in der Datenbank sind sie noch nicht angelegt (kommt vom Haupt-Chat). Voraussetzungen für 102/103 mitliefern (u. a. 30 → 102 → 29 `terme.umformen`; 102 → 103); die Migration darf nicht scheitern, wenn 102/103 noch fehlen.
- **Folgen nennen:** Jede neue Klassen-Zuordnung oder harte Voraussetzung, die den Plan eines Kindes ändern würde (neuer Flug im Plan, andere Reihenfolge), ausdrücklich auflisten – ohne Namen. Reihenfolgen je Schulart und Klasse bleiben lückenlos und eindeutig (Selbstprüfung per Skript).
- Keine Inhalte (Aufgaben, Karten) ändern, keine Kinderdaten, kein Merge nach `main`. Am Ende „FERTIG: Lehrplan Runde 30“. Danach meldet der Haupt-Chat dem Gestalter, der das Übersichtsblatt aktualisiert und gegenprüft.

---

# Bau-Auftrag LM (21.11.): Lehrplan-Matrix „Mathe 5–10“ – bei Lehrer/Eltern und auf der Kinderseite

Von Sebastian gewünscht. Vorgabe des Gestalters (maßgeblich, vollständig lesen): `inhalte/pruefung/lehrer/matrix/umsetzung.md` (LM-1 bis LM-6), Vorlage `inhalte/pruefung/lehrer/matrix/entwurf/lehrplan-matrix.html` (läuft ohne Server, erfundener Lernstand „Kind A“/„Kind B“).

**Schritt 1 – LM-S, Server (`bau-lehrer`, nur Dateien, parallel möglich):** Prüfen, was die Matrix an Daten braucht und was `api.schule_lehrplan_uebersicht` heute liefert. Fehlendes als Migrationsdatei mit Rauchtest (nicht ausführen): je Thema Titel, Themengebiet, Klasse/Reihenfolge/Lernbereich je Schulart, „Was gefordert ist“ (`thema.beschreibung`), Lehrplan-Wortlaut, „Das muss sitzen“ (`merke` der freigegebenen Einheit), Etappen (Titel, Pflicht); die Verbindungen aus `schule.voraussetzung` (Art, Begründung); je sichtbarem Kind Stufe, Etappen gesamt/gelandet („Etappe x von y“), im Plan ja/nein – für alle Kinder in einem Aufruf. Zugriff: Eltern/Lehrer sehen ihre Kinder; ein Kind sieht nur sich selbst und bekommt weder Lehrplan-Wortlaut noch Daten anderer Kinder. Die Ansicht muss mit dem heutigen Stand von `schule.voraussetzung` funktionieren (die Vervollständigung läuft getrennt, Dreißigste Runde). Bericht: Feldliste für den App-Bau. „FERTIG: LM-S“.

**Schritt 2 – LM-1 bis LM-5, App Lehrer/Eltern (`bau-motivation`, nach LM-S, Version 0.84.0):**
- Nachschlagen → „Lehrplan“ = Matrix (LM-1 bis LM-4) mit allen Kindern und „Beide vergleichen“.
- Seite des Kindes, Reiter „Plan“: Link „Als Matrix ansehen ›“ → Matrix mit diesem Kind vorgewählt und dessen Schulart. Kein fünfter Reiter.
- Detail eines Themas (genau ein Kind gewählt): Stufen-Knöpfe wie LB Teil 8 Variante A („Lernen · Kann er – wiederholen · Kann er komplett“, rechts „Aus dem Plan nehmen“/„In den Plan nehmen“), gleiche Server-Aufrufe und Rückgängig wie im Plan. „Im Plan öffnen ›“ springt in den Plan mit dem Thema aufgeklappt.
- Die bisherige Lehrplan-Übersicht (LB-1) geht in der Matrix auf; nichts davon darf verloren gehen, was die Matrix nicht ersetzt – im Bericht nennen.

**Schritt 3 – LM-6, Kinderseite „Meine Route 5–10“ (`bau-motivation`, eigener Schritt nach Schritt 2, Version 0.85.0):**
- Textlink „Meine Route 5–10 ›“ auf der Abflugtafel.
- Nur das eigene Kind, Lernstand immer an; kein Geschwister-Vergleich, keine Schulart-Kennzeichen, kein Lehrplan-Wortlaut.
- Reisewörter (Flug, Kontinent, Etappe; der Test der Reisewörter gilt). Stufen: „kannst du“, „kommt zur Wiederholung“, „hier bist du – Etappe x von y“, „kommt noch“; nicht im Plan blass.
- Kopf je Klasse: „Du kannst schon n von m Flügen“ mit Balken.
- Detail: Was du hier lernst, Das muss sitzen, Das brauchst du vorher (mit eigener Stufe), Danach geht’s weiter mit, Etappen mit ✓. Plan nicht änderbar; nur beim ▶-Flug großer Knopf „Weiter lernen ›“.
- Handy/Tablet zuerst.

**Für alle Schritte:** Tests nur mit Testkind und erfundenen Daten, keine Kinderdaten in Dateien. Abnahme bei 400, 820, 1280 px (kein Wort mitten im Wort umbrochen, Trennstrich erlaubt; Linien hinter den Karten). Nach jedem Schritt im Postfach melden – der Gestalter prüft nach. Merge nach `main` erst nach Sebastians „Live“.

**Nachtrag zur Dreißigsten Runde (21.11., vom Gestalter):** Im Bericht ausdrücklich angeben, **wo und wie „eigenständig“ abgelegt wird** (Spalte oder Eintrag, mit Namen) – nur dann kann das Übersichtsblatt es anzeigen. Der Gestalter prüft danach: kein Thema mit Klasse ohne Verbindung, außer ausdrücklich eigenständig; keine Voraussetzung liegt in einer späteren Klasse als das Thema (je Schulart); die Themen 100–103 sind verknüpft. Diese drei Regeln als Selbstprüfung in den Rauchtest aufnehmen. Stand: 102/103 sind seit 21.11. in der Datenbank und freigegeben.

---

# Nachbesserung Dreißigste Runde und LM-S (21.11.) – nach dem Probelauf des Haupt-Chats

Probelauf (echte Datenbank, zurückgerollt): alle drei Migrationen laufen (`lehrplan_zuordnung_voraussetzungen` mit eigenem Rauchtest, `ab_s_flug_geschafft_robust`, `lm_s_lehrplan_matrix`); `ab_s`-Rauchtest bestanden; Stufen und Plan aller Kinder vorher/nachher gleich. **Nichts davon ist eingespielt.**

**A – `lehrplan-lb`: Thema 12 „Reinquadratische Gleichungen“ nicht dem Gymnasium zuordnen.** Das Thema ist seit der Vierundzwanzigsten Runde für das Gymnasium **aufgelöst**: Der Stoff steht als Etappe `reinquadratisch` im Flug `gleichungen.quadratisch` (Gym 9); in der Datenbank ist Thema 12 ein stillgelegter Entwurf ohne freigegebenen Inhalt. Mit `gym_by 9` stünde ein Flug ohne Inhalt im Lehrplan des Gymnasiums. Also: `gym_by` für 12 wieder entfernen (Reihenfolge Gym 9 zurück), stattdessen die **veraltete Verbindung** „Quadratische Gleichungen braucht 12“ auflösen. Dasselbe für **alle zehn aufgelösten Themen** prüfen (`groessen.verhaeltnisse`, `mengen.grundbegriffe`, `abbildungen.vektoren`, `funktionen.scharen`, `funktionen.transformation`, `gleichungen.reinquadratisch`, `funktionen.umkehr`, `stochastik.bedingt`, `funktionen.folgen`, `finanzen.zinseszins` – Liste gegen `schule.einheit` mit Status `entwurf` abgleichen): Kein Thema mit freigegebenem Flug darf ein aufgelöstes Thema brauchen; die Verbindung zeigt stattdessen auf den Flug, in dem der Stoff jetzt steht, oder entfällt (dann mit Begründung im Bericht). Veraltete Zeilen in `schule.voraussetzung` dürfen dafür **gezielt gelöscht** werden (einzeln aufgezählt, mit Kommentar) – einzige Ausnahme vom Lösch-Verbot. Im Bericht je aufgelöstem Thema: wo steht der Stoff heute (Flug, Etappe). Neue Regel für den Rauchtest: keine Verbindung von oder zu einem Thema ohne freigegebene Einheit, außer ausdrücklich begründet. Die übrigen Ergebnisse der Runde (4 Lernbereich, 32 nach MYP 3, 73 Verbindungen, 7 eigenständig, Spalte `eigenstaendig` als Text) sind angenommen. „FERTIG: Lehrplan Runde 30 b“.

**B – `bau-lehrer`: LM-S an die Ablage von „eigenständig“ anpassen.** `schule.thema.eigenstaendig` ist **Text** (Begründung; `null` = nicht gekennzeichnet), nicht boolean – so liefert es `lehrplan-lb`. Der LM-S-Rauchtest bricht nach dessen Migration ab („invalid input syntax for type boolean …“). Funktion und Test anpassen: `eigenstaendig` = Begründungstext (gesetzt ⇒ eigenständig); Feldliste nachziehen. Außerdem: Themen ohne freigegebene Einheit (aufgelöste Entwürfe) in der Matrix kennzeichnen (`ohne_flug: true`), damit die App sie blass oder gar nicht zeigt. Größe: Lehrer-Antwort im Probelauf 249 KB, Kindsicht 161 KB – Lehrplan-Wortlaut, `beispiel` und `merke` erst im Detail nachladen (zweite Aktion `thema_id`), Ziel deutlich unter 100 KB je Aufruf. „FERTIG: LM-S 2“.

---

# Rückläufer 21.11. morgens (Probelauf des Haupt-Chats, ChatGPT 896) – nichts davon ist eingespielt

**A – `lehrplan-lb`, Runde 30 c: harte Voraussetzungen ändern die Visum-Regeln der Kinder.** Die Migration läuft und ihr Rauchtest besteht; Stufen und Lernstand bleiben gleich. **Aber:** `schule.v_ort_visum` wächst von 49 auf 81 Zeilen, und `schule.reiseoptionen` liefert für die Kinder andere Ergebnisse (neue „Visum fehlt“-Sperren, z. B. braucht ein Ort der Klasse 5 jetzt das Visum eines anderen Orts). „Plan-Folgen: keine“ stimmt also nicht – harte Verbindungen steuern, in welchen Ort ein Kind reisen darf. Bitte: (1) `v_ort_visum` und `reiseoptionen` lesen und verstehen; (2) für jede neue oder geänderte **harte** Verbindung prüfen, ob sie wirklich eine Reise-Sperre sein soll – sonst `empfohlen`; (3) im Bericht je Kind (ohne Namen, „Kind Klasse 5“, „Kind Klasse 8“) vorher/nachher: welche Orte sind wählbar, welche gesperrt und wodurch; Ziel: Für die heutigen Pläne ändert sich nichts, außer es ist fachlich zwingend und einzeln begründet (das entscheidet dann Sebastian); (4) Rauchtest-Regel: `reiseoptionen` der vorhandenen Kinder vor und nach der Migration vergleichen und Unterschiede ausgeben. „FERTIG: Lehrplan Runde 30 c“.

**B – `bau-lehrer`, LM-S 3: Migration bricht ab.** `20261121_lm_s_lehrplan_matrix.sql` (md5 544f48ff…) scheitert beim Ausführen auf der echten Datenbank mit „mismatched parentheses at or near ")"“; danach fehlt die Funktion, der Rauchtest läuft nicht. Bitte beheben und die Datei wirklich ausführbar prüfen (z. B. mit `plpgsql_check` oder lokal gegen Postgres; pglast prüft den Funktionsrumpf nicht). „FERTIG: LM-S 3“.

**C – `bau-lehrer`, „Flug geschafft“ als einmaliges Ereignis (ChatGPT 896: zwei neue Muss).** Die Rekonstruktion aus alten Sitzungen (`flug_fertig_nach`) ist nicht verlässlich (heutige Pflichtliste; Lesen einer alten Sitzung schreibt `false` fest). Neuer Weg statt Rekonstruktion: Tabelle `schule.flug_erstabschluss (lernender_id, einheit_id, sitzung_id, am, primary key (lernender_id, einheit_id))`. Die Migration trägt einmalig alle Flüge ein, die **jetzt** fertig sind (alle Pflicht-Etappen nachgewiesen/korrigiert/gesichert) oder zu denen es eine abgeschlossene Flug-Test-/Verbessern-Sitzung mit `flug_geschafft = true` gibt (`sitzung_id` null, wenn unbekannt). `flug_geschafft` einer Sitzung = dieser Aufruf schließt sie ab, der Flug ist danach fertig **und** der Eintrag in `flug_erstabschluss` konnte neu angelegt werden (`insert … on conflict do nothing`, `found`). Damit gibt es je Kind und Flug höchstens ein „Flug geschafft“, unabhängig von später hinzugefügten Pflicht-Etappen, vom erneuten Lesen und von gleichzeitig laufenden Sitzungen. `flug_fertig_nach` entfällt (nicht mehr benutzen; kein DROP nötig, weil nie eingespielt – Datei `20261121_ab_s_flug_geschafft_robust.sql` ersetzen). Tests: alter bestandener Flug + neue Pflicht-Etappe + Nachtragstest → false; alte Sitzung vorher erneut gelesen → false; alter nicht bestandener Test + Verbessern → true; zweimal abschließen → einmal true. „FERTIG: flug_erstabschluss“.

**D – `bau-motivation`, 0.84.0 an LM-S 2/3 anpassen (noch nicht live):** Detail kommt über die eigene Aktion `schule_lehrplan_thema {thema_id}` (nicht `schule_lehrplan_matrix {thema_id}`); `verbindungen[]` sind Tripel `[thema_id, braucht_id, "h"|"e"]`; `titel` des Gebiets nur in `gebiete[]`; `etappen_anzahl` im Raster; `kurz, ort, was_gefordert, merke, etappen, beispiel, braucht, baut_darauf, lehrplan, eigenstaendig` (Text) im Detail – Feldliste in `inhalte/postfach/bau-motivation.md`, „FERTIG: LM-S 2“. Info-Seite: Texte zur alten Lehrplan-Übersicht an die Matrix anpassen (Vorschlag im Bericht, der Gestalter prüft). Den weggefallenen Sammelblick „was fehlt noch?“ (Filter nach Inhaltsstand) als Filter in der Matrix erhalten. Weiter Version 0.84.0. „FERTIG: 0.84.0 b“.

---

# Nacharbeit aus ChatGPTs Prüfergebnis 907 (22.11.) – blockiert das Einspielen nicht

Die zwei Muss aus 907 sind erledigt: Der Altzustand (früher fertiger Flug mit nachträglich erweiterter Pflichtliste) kommt im Bestand nicht vor (4 von 4 Flügen mit Test sind fertig, Pflichtlisten vollständig); der Haupt-Chat spielt jede Datei in einer Transaktion ein und vergleicht Reiseoptionen und Stufen selbst.

**`bau-lehrer` (nur Dateien):**
1. `ab_s_abschluss_rauchtest.sql`: Fall „alter bestandener Flug (Sitzung NULL bzw. vorher gelesen und dadurch false) → neue Pflicht-Etappe offen → **erst dann** Nachtrag → Nachtragstest“; erwartetes Ergebnis festlegen und im Kopf der Migration dokumentieren, dass dieser Altzustand beim Einspielen ausgeschlossen wurde. Im Kommentar festhalten: erneutes Lesen derselben erfolgreichen Sitzung zeigt wieder `flug_geschafft = true` (gewollt).
2. Nachtrag: `sitzung_id` und `am` aus derselben (zeitlich ersten) Zeile.
3. LM-S: negative Tests über `api.schule_lehrplan_matrix` / `api.schule_lehrplan_thema` mit einem Lern-Zugang des Testkinds (fremde `lernender_id`, `mit_testkind: true`, Detail, gesperrter Zugang) – keine echten Schlüssel in Dateien; `etappe_jetzt` = Nummer der ersten offenen Etappe in Reihenfolge statt „gelandet + 1“; Größenprüfung mit `octet_length`.

**`lehrplan-lb` (nur Dateien):** Rauchtest j: fehlender Vorherstand → EXCEPTION; Kopfkommentar „kein DELETE“ berichtigen; vor jeder gezielten Löschung prüfen, dass das Thema weiter keinen freigegebenen Flug hat; Testfall „Zielort offen, Voraussetzungs-Ort fehlt“ für die Kante 102 ← 30. Restlücke „Vektorkoordinaten für Determinanten (RS 7)“ als offenen Inhaltspunkt im Bericht führen.

---

# Bau-Auftrag WD (22.11.): Wiederholungen dynamisch – Stau vermeiden, Belohnung fürs Ablegen

Anlass: Sebastian und die Kinder. Jede gelandete Etappe erzeugt 5 Wiederholungen (1, 3, 7, 14, 30 Lerntage); die Runde am Anfang hat fest 6 Aufgaben. Bei mehr als etwa 1,2 Landungen pro Lerntag staut es sich; ein Kind hat nach dem Setzen mehrerer Flüge 41 fällige Etappen. **Entscheidungen Sebastians (22.11.):** Die Wiederholungs-Runde am Anfang bleibt (einmal pro Tag); ihre Größe wird errechnet; Mischkarten bleiben und bauen mit ab; **kein Bündeln je Flug – jede Etappe für sich**; Sterne 5 / 30 / 100; kein neues Abzeichen, sondern der vorhandene Stempel wird golden. **Gebaut wird erst nach ChatGPTs Prüfung des Konzepts und der Vorgabe des Gestalters.**

**WD-1 Größe der Runde (Server liefert, App zeigt) – geändert 22.11., Sebastian: lockerer, ein Stau darf sich über 5 Lerntage auflösen:** fällige Etappen bis 6 → alle; darüber **ein Fünftel der fälligen, aufgerundet, mindestens 6, höchstens 12** (bis Klasse 6 höchstens 10). Beispiele: 20 fällig → 6; 41 → 9; 60 → 12. Werte in `schule.regel` (änderbar ohne Bau). Reihenfolge: zuerst Etappen mit einem Wiederholungs-Fehler, dann die am längsten fälligen, dann niedrigste Stufe. Weitere fällige bleiben freiwillig angeboten wie heute.

**WD-2 „Runde heute gemacht“ merkt sich der Server** (heute nur das Gerät, `localStorage`): je Kind und Lerntag (`heute_bis`), damit ein Gerätewechsel keine zweite Pflicht-Runde auslöst.

**WD-3 Mischkarten bauen mit ab:** Die Auswahl der Mischkarten bevorzugt fällige Etappen (sonst wie bisher). Eine Mischkarte aus einer fälligen Etappe, richtig im ersten Versuch ohne Tipp, gilt als bestandene Wiederholung: Die Etappe rückt im Takt weiter wie nach einer richtigen Wiederholung, zusätzlich zum bisherigen Beleg für „sicher“. Falsch bleibt wie heute (am nächsten Lerntag fällig, öffnet nie). Häufigkeit unverändert (jede 4., bis Klasse 6 jede 6., ab 3 gelandeten Etappen im Flug).

**WD-4 Gesetzte Flüge gestaffelt:** „Kann er – aber wiederholen“ bringt je Kind höchstens 6 Etappen pro Lerntag neu in den Takt (ein Flug nach dem anderen, in Plan-Reihenfolge); die übrigen warten sichtbar („kommt ab …“). Für den vorhandenen Stau eine einmalige, verlustfreie Umverteilung vorschlagen (nur Fälligkeiten strecken; keine Landung, kein Stand geht verloren) – als eigene, gut lesbare Migration, die der Haupt-Chat erst nach Probelauf und Sebastians Okay einspielt.

**WD-5 Sterne:** 5 Sterne je richtiger Wiederholung (Runde am Anfang, freiwillige Wiederholung oder Mischkarte nach WD-3; je Etappe und Fälligkeit einmal). Vorher feststellen und melden, was Wiederholungen und Mischkarten heute geben (Mischkarte in der App: 10) – nichts doppelt buchen, nichts stillschweigend kürzen.

**WD-6 „Endgültig abgelegt“:** Besteht eine Etappe die letzte Wiederholung (30 Lerntage), ist sie abgelegt: raus aus dem Takt, **30 Sterne**, Einblendung (einmal je Kind und Etappe, serverseitig festgehalten wie `flug_erstabschluss`). Sind alle Etappen eines Flugs abgelegt: **100 Sterne**, größere Einblendung; im Reisepass wird der vorhandene Eintrag des Flugs **golden** (kein neues Abzeichen). Sind alle Flüge eines Orts abgelegt, wird der **Orts-Stempel golden**. Verhältnis zu „sicher“ (◉) klären und im Bericht vorschlagen: zwei ähnliche Zustände nebeneinander vermeiden. Eine abgelegte Etappe kann durch den Nachtest des Flugs weiter auffallen – Regel dafür vorschlagen (Vorschlag: sie kommt einmalig mit 7 Lerntagen zurück in den Takt, das Gold bleibt).

**Aufteilung:** Server (`bau-lehrer`, Migrationen als Datei mit Rauchtests: Rundengröße, Server-Merker, Mischkarte als Wiederholung, Staffelung, Sterne, Ablegen einmalig; Lernstände bleiben unverändert – Vergleich vorher/nachher im Test). App (`bau-motivation`, nach LM-6): Runde in errechneter Größe, Einblendungen nach Vorgabe des Gestalters, goldener Flug-Eintrag und Stempel, Info-Seite. Gestalter: zwei Einblendungen („Etappe abgelegt“, „Flug abgelegt“) und das Gold im Reisepass, Vorgabe unter `inhalte/pruefung/kind/abgelegt/`.

**Nachtrag zum Bau-Auftrag WD (22.11., Sebastian: „Wiederholungen zuerst“) – Reihenfolge und Schnittstelle.** WD hat Vorrang vor LM-6. Server und App werden **gleichzeitig** gebaut; dafür gilt diese Schnittstelle verbindlich (Abweichungen nur mit Meldung im Postfach, bevor gebaut wird). ChatGPTs Prüfung des Konzepts (Werkstatt 909/910) läuft parallel; ihre Ergebnisse werden eingearbeitet, eingespielt wird erst danach.

- `schule_wiederholung` (bestehende Aktion) liefert zusätzlich: `runde` (Zahl der Pflicht-Aufgaben heute nach WD-1), `faellig` (alle fälligen Etappen), `runde_gemacht` (true, wenn die Pflicht-Runde dieses Lerntags erledigt ist – WD-2), `aufgaben[]` in der Reihenfolge nach WD-1 (die ersten `runde` sind Pflicht, weitere freiwillig), `gestaffelt` (Zahl gesetzter Etappen, die noch warten – WD-4). Neue Aktion `schule_wiederholung_runde_fertig {lernender_id}` setzt den Merker.
- `schule_uebung_pruefen` liefert bei einer Wiederholung oder einer Mischkarte nach WD-3 zusätzlich `wiederholung: { bestanden, sterne, stufe_neu, naechste_in }` und, wenn dadurch etwas abgelegt wird, `abgelegt: { etappe: { titel, sterne }, flug?: { titel, sterne }, ort_gold?: true }` – höchstens einmal je Kind und Etappe/Flug/Ort.
- Konto/Reisepass (`schule_konto`): je Flug `abgelegt: true|false` und `etappen_abgelegt`/`etappen`; je Ort `gold: true|false`.
- Regeln in `schule.regel`: `wdh_runde_min` 6, `wdh_runde_max` 12, `wdh_runde_max_bis_kl6` 10, `wdh_runde_teiler` 5, `wdh_gesetzt_je_lerntag` 6, `sterne_wdh_richtig` 5, `sterne_etappe_abgelegt` 30, `sterne_flug_abgelegt` 100.
- **Sterne heute:** `sterne_uebung_richtig` = 10. `bau-lehrer` stellt fest, ob eine richtige Wiederholung heute schon 10 Sterne gibt. Wenn ja: **nicht kürzen**, sondern melden – Sebastian entscheidet dann zwischen 5 und 10.
- App ohne neue Server-Felder (alter Server): Verhalten wie 0.84.0.
- Einblendungen: `bau-motivation` baut sie im Stil der vorhandenen Abschluss-Ansichten („Etappe abgelegt“ klein, „Flug abgelegt“ groß, Gold im Reisepass); der Gestalter liefert parallel die Vorgabe und prüft nach – Abweichungen werden danach angeglichen.

---

# Vorarbeit „Reise-Aufbau“ (22.11.): Kontinent → Land → Stadt – Festlegungen des Haupt-Chats

Richtung von Sebastian (22.11.): Kontinent = Themengebiet (bleibt); **Flug = ein Thema = ein Land** auf diesem Kontinent; **Etappe = eine Stadt** in diesem Land; Aufgaben = Highlights der Stadt, ohne Namen; sinnvoll gegliedert. Die Ebene „Ort“ entfällt. **Reihenfolge: erst der Bau-Auftrag WD, dann dieser Umbau.** Bis dahin nur Vorarbeit (Vorschlagsliste, kein Bau). Sebastian hat die Sonderfälle dem Haupt-Chat überlassen; festgelegt (er kann widersprechen):

1. **Antarktis ist kein Lern-Kontinent mehr.** Dort gibt es keine Länder und Städte. Die Antarktis wird Heimat der **Expeditionen** (Forschungsstationen statt Städte) – das passt zum Wort und braucht keine Länder.
2. **„Funktionen“ zieht in den Orient** (Naher Osten und Kaukasus, als eigener Reise-Kontinent neben Asien): 10 Länder, z. B. Türkei, Georgien, Armenien, Aserbaidschan, Iran, Irak, Jordanien, Saudi-Arabien, Vereinigte Arabische Emirate, Oman. Bisher hat dort kein Kind etwas gelernt – es geht nichts verloren.
3. **„Algebra“ bleibt Asien** ohne den Orient: Zentral-, Süd-, Ost- und Südostasien (19 Länder). Die heutigen Orte Bagdad und Teheran wechseln in asiatische Länder; **Usbekistan (Samarkand) und Indien (Mumbai) bleiben**, weil dort schon gelernt wurde.
4. **„Daten und Zufall“ = Australien und Ozeanien:** Australien zählt nach **Bundesstaaten** (New South Wales, Victoria, Queensland, South Australia, Western Australia, Tasmanien, Northern Territory), dazu Neuseeland (Nord- und Südinsel getrennt), Papua-Neuguinea und Fidschi – zusammen 12. Einzige Ausnahme von „ein Land“, weil Ozeaniens Inselstaaten zu wenige Städte haben.
5. **„Entdecker-Inseln“ = Pazifik:** Hawaii, Französisch-Polynesien, Samoa, Tonga – keine Überschneidung mit Punkt 4.
6. **Wo schon gelernt wurde, bleibt die Stadt erhalten:** Die heutige Stadt eines Orts wird eine der Städte des neuen Landes; Stempel und Sterne der Kinder bleiben (aus Stadt-Stempeln werden Länder-Stempel). Hat ein Ort heute mehrere Flüge, behält der Flug, den das Kind zuerst abgeschlossen hat, das Land der Stadt; die anderen bekommen Nachbarländer.
7. **Länder nach Größe:** ein Flug hat 3 bis 12 Etappen – nur Länder mit genug bekannten Städten; Reihenfolge der Länder je Kontinent = Reihenfolge der Klassen als Route, Städte je Land als fahrbare Rundreise.
8. Eltern/Lehrer sehen weiter „Themengebiet · Thema · Etappe“; die Reise-Namen sind nur die Kinderseite.

**Nachtrag „Reise-Aufbau“ (22.11., zweite Durchsicht des Haupt-Chats; Sebastian: es können Themen dazukommen):**

9. **Wachstum eingeplant.** „Land“ heißt überall **Land oder großer Landesteil** (Bundesstaat, Provinz, Region) – nicht nur in Australien. Große Länder dürfen also geteilt werden (z. B. USA, Kanada, Brasilien, Indien, China), wenn ein Kontinent sonst keine Länder mehr frei hat. Je Kontinent bleibt mindestens ein Drittel der möglichen Länder/Landesteile **unbenutzt als Reserve** (im Vorschlag auflisten); je Land mindestens **drei Reserve-Städte** für spätere Etappen. Neuer Flug = nächstes freies Land auf der Route; neue Etappe = Reserve-Stadt; geteilter Flug (wie bei den Potenzgesetzen) = Nachbarland. Wird ein Flug stillgelegt, bleibt sein Land für immer vergeben (kein Wiederverwenden – Stempel der Kinder).
10. **Jedes Fach hat seine eigene Reise-Welt.** Die Zuordnung gilt nur für Mathematik (`fach`); ein späteres Fach darf dieselben Länder mit eigenem Reisepass neu belegen.
11. **Der Mathe-Titel bleibt immer sichtbar.** Stadt und Land sind die Verpackung, nie der einzige Name: „Samarkand · Minus vor der Klammer“, „Usbekistan · Terme umformen“. Das gilt auch für Wiederholungen, Mischkarten („Das war: …“) und Tests.
12. **Technischer Weg (für die spätere Schätzung von `bau-lehrer`): die Ebene Ort nicht ausbauen, sondern jeden Ort auf genau einen Flug bringen.** Die 18 Orte mit mehreren Flügen werden in Ein-Flug-Orte aufgeteilt (Daten-Migration: `block`, `block_thema`, `route` der Kinder mit richtigem Status je neuem Ort, Voraussetzungen/Visum, Sterne „ort“), der Ort bekommt das Land, die Etappe die Stadt. Plan, Reise-Sperren und Stempel arbeiten dann unverändert weiter – Stempel je Flug und „Visum für ein Land“ ergeben sich von selbst. Vorher/nachher-Vergleich je Kind: Stufen, Plan-Reihenfolge, Reiseoptionen, Sterne.
13. **Bestehende Erfolge:** Hat ein Kind in einem bisherigen Mehr-Flug-Ort Flüge abgeschlossen, bekommt es für jeden dieser Flüge den Länder-Stempel und die Orts-Sterne nachträglich (einmalig); nichts wird abgezogen.
14. Vorrang bei Widerspruch: Regel 6 (begonnene Städte bleiben) geht vor Regel 2/3 (Orient/Asien) – liegt eine begonnene Stadt im Orient, bleibt ihr Land beim bisherigen Themengebiet und wird im Orient nicht verwendet.

---

# Rückläufer 22.11. abends – Probelauf des Haupt-Chats und ChatGPT 911/912 (nichts eingespielt, nichts live)

Übernommen (e1900e5): WD-S und Nacharbeit 907 (`bau-lehrer`), App 0.85.0 (WD) und 0.86.0 (LM-6) (`bau-motivation`), Lehrplan-Nacharbeit 907 (`lehrplan-lb`), Vorschlag Reise-Aufbau, Vorgabe „abgelegt“ und Nachprüfung Matrix (Gestalter). Probelauf auf der echten Datenbank, zurückgerollt: `nacharbeit_907` läuft, beide Rauchtests bestanden; `wd_s_wiederholungen` läuft; `wd_4b_stau_strecken` läuft (ein Kind: 42 fällige → 14); Stufen, Plan, Reiseoptionen, Lernstand und Sterne aller Kinder gleich.

**A – `bau-lehrer`, WD-S 2**
1. **Fehler:** `wd_s_rauchtest.sql` bricht auf der echten Datenbank ab: „new row for relation "sterne" violates check constraint "sterne_grund_check"“. Die neuen Sterne-Gründe fehlen in der Prüfregel der Tabelle `schule.sterne` – in der Migration ergänzen (ohne DROP der Spalte; Constraint ersetzen ist erlaubt), lokal mit der echten Tabellendefinition prüfen.
2. **ChatGPT 912, MUSS 5:** `schule_wiederholung_runde_fertig` darf kein bloßer Schalter sein. Beim ersten Abruf des Lerntags die Runde festhalten (Tagesziel und zugeordnete Etappen in `schule.wdh_runde`); „gemacht“ setzt der Server selbst, sobald alle Pflicht-Aufgaben der Runde beantwortet sind (richtig oder falsch – falsch zählt als bearbeitet, nicht als bestanden); die Aktion bestätigt nur noch und lehnt ab, wenn Aufgaben fehlen (Ausnahme: 0 fällige, oder Aufgabe inzwischen gesperrt → zählt als bearbeitet). Zweites Gerät setzt dieselbe Runde fort; neue Fälligkeiten am selben Tag erzeugen keine zweite Pflicht-Runde.
3. **ChatGPT 911, MUSS 3:** je Fälligkeit genau ein Stufenfortschritt und eine Vergütung – auch bei zwei Geräten oder doppelt gesendeter Antwort (Test dazu); eine nicht fällige Mischkarte gibt nur den Misch-Beleg, keinen Fortschritt (Test). Falsche Mischkarte als Wiederholungs-Fehler für die Reihenfolge der nächsten Runde zählen.
4. **Reihenfolge der Runde:** mindestens ein Drittel der Pflicht-Plätze für die am längsten fälligen Etappen, damit Fehler-Etappen die übrigen nicht verdrängen.
5. **Nachtest nach dem Ablegen (ChatGPT MUSS 4, statt „7 Lerntage“):** Fällt eine abgelegte Etappe im Nachtest oder beim Üben durch, kommt sie am **nächsten Lerntag** zurück in den Takt (Stufe 2); Gold, Sterne und Einblendung bleiben, ein zweites Ablegen gibt nichts. Als Teil dieser Lieferung bauen. Ablegen bleibt an der bestandenen fünften Wiederholung (30 Lerntage nach der vierten) – nicht zusätzlich an „sicher“ gebunden (Wunsch der Kinder); im Kopf der Migration festhalten: frühestens 55 Lerntage nach der Landung; `abgelegt` ist ein eigenes Ereignis, nie aus `wdh_stufe` abgeleitet.
6. **Sterne:** `sterne_wdh_richtig` bleibt bis zu Sebastians Entscheidung auf 10. Letzte Wiederholung: Wiederholungs-Sterne + 30 + ggf. 100 kommen zusammen, je einmal.
7. Im Kopf von `wd_s`: Ziel ist „Stau schrittweise abbauen, etwa fünf Lerntage bei ausreichender Kapazität“ – keine Garantie (ChatGPT MUSS 1); bekannte Grenze: ohne Bündeln trägt die Kapazität dauerhaft etwa 3 Landungen je Lerntag (MUSS 2).
8. Tests zusätzlich: 20/41/60/100 fällige, keine Mischkarten, zwei Geräte, Abbruch mitten in der Runde, Tageswechsel, letzte Stufe, Rückfall nach dem Ablegen. „FERTIG: WD-S 2“.

**B – `lehrplan-lb`:** `20261122_lehrplan_nacharbeit_907.sql` bricht ab: „cannot insert a non-DEFAULT value into column "id"“ (`schule.thema.id` ist GENERATED ALWAYS – Testthemen ohne feste id anlegen oder `overriding system value`). Dazu aus der Nachprüfung des Gestalters: N2 – fünf aufgelöste Themen tragen noch eine Realschul-Klasse (48, 78, …): Klasse/Reihenfolge RS und IB der zehn aufgelösten Themen leeren, Reihenfolgen nachziehen; N3 – Thema 83 ist aufgelöst und trägt `eigenstaendig`: Kennzeichnung entfernen. „FERTIG: Lehrplan Nacharbeit 907 b“.

**C – `bau-motivation`, 0.86.1:**
1. **Test schlägt fehl (zweimal, auch einzeln):** „LM-S 2: Raster … Detail …“ wartet vergeblich auf „Eigenständig: braucht keine Voraussetzung – Einstieg in die Geometrie“ im Detail (`tests/lernen.test.cjs:3778`). Ursache finden (App oder Test) und beheben – das betrifft die Lehrer-Matrix, die live ist.
2. Einblendungen, Gold und Runde an die Vorgabe des Gestalters angleichen: `inhalte/pruefung/kind/abgelegt/umsetzung.md`, `entwurf/abgelegt.html`.
3. An WD-S 2 anpassen: kein eigenes Setzen von „Runde gemacht“ mehr – der Server setzt es; die Aktion nur noch zum Bestätigen; Aufgaben mit `pflicht`; `anzahl` weglassen. Text: nie „Schulden“/große Rückstandszahl zeigen; Runde sichtbar endlich („3 von 9“), unterbrechen und fortsetzen möglich.
4. Matrix-Nachprüfung N1: am Rechner (1280) sind die Spalten zu schmal, Titel zerstückelt – Lösung nach `inhalte/pruefung/lehrer/matrix/nachpruefung.md`.
„FERTIG: 0.86.1“.

---

# Fehler Mischkarten (22.11., gemeldet von einem Kind): dieselbe Aufgabe dreimal am Tag, in drei Etappen

**Befund aus den Daten (ohne Namen):** Eine Aufgabe (Stufe 2, Etappe „Werte von Bruchtermen berechnen“) wurde am selben Tag dreimal beantwortet: 14:23 im normalen Üben ihrer eigenen Etappe, 18:39 als Mischkarte (Ausgabe von 13:10 eingelöst), 20:04 noch einmal als Mischkarte angezeigt – vom Server aber als normale Antwort gebucht, weil keine gültige Ausgabe mehr bestand. Im Pool dieser Etappe liegen 16 passende Aufgaben (Stufe 2–3).

**Ursachen**
1. **App:** Die Mischkarten-Liste (`ctx.daten.mischkarten`) wird je Flug einmal geladen und **für jede Etappe neu von vorn benutzt** (`mischRest` in `lernen.js`, „keine Wiederholung in der Sitzung“ gilt nur innerhalb einer Etappe). In der nächsten Etappe kommt dieselbe Karte wieder.
2. **Server:** Eine vorab ausgegebene Mischkarte bleibt bis zu 24 Stunden offen und wird wieder ausgegeben, auch wenn das Kind **dieselbe Aufgabe inzwischen im normalen Üben gelöst** hat. Die Auswahl (`schule.mischkarten_waehlen`) schließt schon bearbeitete Aufgaben nicht aus.
3. **Anzeige:** Beim dritten Mal zeigt die App „+10 Sterne“, obwohl der Server je Aufgabe nur einmal Sterne bucht.

**Aufträge – Teil des WD-Pakets, vor dem Einspielen (mit WD zählt eine Mischkarte als Wiederholung; eine bekannte Aufgabe wäre dann kein Abruf, vgl. ChatGPT 911 MUSS 3):**
- **`bau-lehrer`, WD-S 3 (Dateien):** (a) Auswahl der Mischkarten: zuerst Aufgaben, die das Kind **noch nie** beantwortet hat, dann die am längsten zurückliegenden; **nie** eine Aufgabe, die es in den letzten 3 Lerntagen beantwortet hat (egal ob Üben, Wiederholung, Mischkarte, Test); unter gleichwertigen zufällig. (b) Offene Ausgabe verfällt sofort, wenn dieselbe Aufgabe anders beantwortet wird. (c) Dieselbe Regel für die Aufgaben der Wiederholungs-Runde (`schule_wiederholung`): keine Aufgabe von heute oder gestern, wenn die Etappe andere hat. (d) Kommt eine Mischkarte ohne gültige Ausgabe an, antwortet der Server mit `misch: { gueltig: false }`, bucht sie nicht als Wiederholung und liefert die tatsächlich gebuchten Sterne (`sterne`) mit. Tests: gleiche Aufgabe nicht zweimal am Tag; Pool mit nur einer Aufgabe; nach normalem Üben keine Mischkarte derselben Aufgabe. „FERTIG: WD-S 3“.
- **`bau-motivation`, 0.86.2:** (a) Eine gezeigte Mischkarte wird für die ganze Sitzung des Flugs aus der Liste genommen (nicht je Etappe neu); ist die Liste leer, einmal neu vom Server holen, sonst ohne Mischkarte weiter. (b) Sterne-Anzeige nur aus der Antwort des Servers (keine eigenen „+10“). (c) Bei `misch.gueltig === false` kein „Das war …“-Lob als Wiederholung. Test: drei Etappen nacheinander, keine Mischkarte doppelt. „FERTIG: 0.86.2“.

**Nachtrag „WD-S 3 – frische Aufgaben“ (22.11., Entscheidung Sebastian):**
- Wiederholungen nach **1, 3 und 7 Lerntagen** (Stufe 0–2) und **jede Mischkarte**: nur Aufgaben, die das Kind **noch nie** beantwortet hat (egal in welcher Rolle: Üben, Wiederholung, Mischkarte, Test, Knobeln).
- Wiederholungen nach **14 und 30 Lerntagen** (Stufe 3–4): beliebige Aufgabe der Etappe, bevorzugt die am längsten zurückliegende.
- Ist keine frische Aufgabe mehr da: die am längsten zurückliegende, **nie** eine aus den letzten 3 Lerntagen; gibt es auch die nicht, an diesem Tag keine Aufgabe dieser Etappe (Wiederholung bleibt fällig).
- **Keine Mischkarte aus einer Etappe, in der das Kind am selben Lerntag schon eine Aufgabe beantwortet hat** (auch nicht, wenn sie fällig ist – dann kommt sie in der Runde am nächsten Lerntag).
- Lesende Funktion für den Haupt-Chat: je Kind die gelandeten Etappen mit weniger als 3 frischen Aufgaben der Stufen 2–3 (Stand 22.11.: Bestand je Etappe mindestens 14 solche Aufgaben, typisch 16; 3 von 51 selbst gelandeten Etappen liegen unter 3). Dort lässt der Haupt-Chat Aufgaben nachliefern.

---

# ChatGPT 919 zu WD-S 2 / WD-4b / Nacharbeit 907 (22.11.) – vier Muss, alles vor dem Einspielen

(ChatGPT 918 betrifft die alte Fassung von `flug_geschafft` und ist durch `flug_erstabschluss` überholt.)

**`bau-lehrer` – in WD-S 3 mit erledigen (zusätzlich zu „Fehler Mischkarten“ und „WD-S 3 – frische Aufgaben“):**
1. **MUSS 1 – bestandene Wiederholung.** Heute rückt eine fällige Wiederholung auch mit Tipp oder im zweiten Versuch weiter; damit könnte eine Etappe mit Hilfe „abgelegt“ werden. Neu (vorbehaltlich Sebastians Entscheidung, Standard so bauen, per Regel `wdh_nur_selbst` = true umschaltbar): **Stufenfortschritt, Wiederholungs-Sterne und Ablegen nur bei richtig im ersten Versuch ohne Tipp** – für Runde, freiwillige Wiederholung und Mischkarte gleich. Richtig mit Tipp oder im zweiten Versuch: kein Fortschritt, kein Fehler; die Etappe kommt am nächsten Lerntag wieder. Endgültig falsch: wie bisher. Test über den echten Antwortweg (Stufe 4, Tipp bzw. zweiter Versuch → nicht abgelegt).
2. **MUSS 2 – WD-4b und die festgehaltene Tagesrunde.** WD-4b nimmt Etappen aus, die in einer offenen Runde von heute stehen (oder aktualisiert die Runde mit). Test „Runde begonnen → WD-4b → offene Pflichtaufgabe zählt“.
3. **MUSS 3 – WD-4b zählt belegte Folgetage mit:** höchstens `wdh_gesetzt_je_lerntag` erste Wiederholungen je Kind und Lerntag einschließlich der schon von WD-4 geplanten. Test mit vorbelegtem Folgetag.
4. **Sollte:** Misch-Fehler für die Reihenfolge erst nach endgültiger Wertung (`schule.versuch_wertung`); echter Test mit zwei gleichzeitigen Transaktionen (ein Fortschritt, einmal Sterne) und über die API-Antwort; Rückweg von WD-4b nur ohne Zwischenübung (prüfen und sonst ablehnen), kein zweiter Lauf; Lerntage statt Kalendertage belegen (Test mit eingetragenen Reisetagen); vorhandene Einträge in `flug_erstabschluss` gegenprüfen.

**`lehrplan-lb` – Nacharbeit 907 c:** MUSS 4 – der Löschschutz gilt auch für Einheiten im Status `geprueft` (für Kinder sichtbar), Test dazu; Rauchtest l nur für die zehn stillgelegten Themen, nicht für alle nicht freigegebenen.

**`bau-motivation` – in 0.86.2 mit erledigen:** Text nach dem Ablegen nicht „kommt nicht mehr wieder“, sondern sinngemäß „aus der regelmäßigen Wiederholung – wird nur noch bei Bedarf aufgefrischt“; Antwort `wiederholung.bestanden === false` bei richtig mit Tipp/zweitem Versuch freundlich zeigen („Richtig – morgen noch einmal ohne Hilfe“).

**Entscheidungen Sebastian (22.11., 11:00 Berlin) zum WD-Paket und zum Reise-Aufbau:**
1. **Wiederholung zählt nur selbstständig:** Fortschritt im Takt, Wiederholungs-Sterne und Ablegen nur bei richtig im ersten Versuch ohne Tipp (`wdh_nur_selbst` = true bleibt). Mit Tipp oder im zweiten Versuch richtig: kein Fehler, die Etappe kommt am nächsten Lerntag wieder.
2. **10 Sterne je richtiger Wiederholung** (`sterne_wdh_richtig` = 10, keine Kürzung); dazu 30 je abgelegter Etappe und 100 je abgelegtem Flug.
3. **Stau strecken (WD-4b): ja** – nach WD-S 3, Probelauf und ChatGPT, zusammen mit dem Paket.
4. **Reise-Aufbau:** nach dem WD-Paket weitermachen (Entwurf des Gestalters, Aufwandsschätzung); für schon abgeschlossene Flüge gibt es Länder-Stempel **und** die 100 Sterne nachträglich.
5. Kinder-Zugänge sind angelegt (je Kind ein Lern-Zugang) – erledigt.

### Nachtrag WD-S 3 – Rauchtest stabil machen (22.11., 11:15 Berlin) · an `bau-lehrer`

Probelauf des Haupt-Chats gegen die echte Datenbank (Rollback, Commit 7675d32): alle fünf Migrationen laufen, Stufen/Reise/Lernstand/Sterne unverändert, drei Tests grün. `supabase/tests/wd_s3_rauchtest.sql` bricht in Schritt 2 ab („keine frische: nicht die am längsten zurückliegende“).

Ursache liegt im Test, nicht in der Funktion: Der Test rechnet nur mit den Auswahl-Aufgaben der Stufen 2–3 (`v_ids`), `schule.wdh_aufgabe_waehlen` wählt aber richtig aus **allen** freigegebenen Übungsaufgaben der Etappe. In der echten Etappe (Einheit 1, `roemisch_system`: 19 Aufgaben, davon 8 Auswahl Stufe 2–3) gibt es weitere nie beantwortete Aufgaben – die werden zu Recht vor einer alten gewählt. Schritt 2, erste Prüfung, besteht dort nur zufällig.

Bitte nur die Testdatei ändern (keine Migration): Vor Schritt 1 alle übrigen Übungsaufgaben beider Test-Etappen als „innerhalb der Sperre beantwortet“ markieren (z. B. `w3_gesehen` am Vortag, nicht heute) – mit genau dieser Änderung läuft der ganze Test bei mir grün. Meldung im Postfach: „FERTIG: WD-S 3 Test“.

## Bau-Auftrag FP – faire Punkte (22.11., 11:30 Berlin) · Entscheidung Sebastian: „Ja“

**Anlass:** Die Kinder haben bemerkt, dass eine Etappe mit Fehlern mehr Sterne bringt (Daten: 0 Fehler ≈ 5 Aufgaben ≈ 50 Sterne, 3+ Fehler ≈ 15 Aufgaben ≈ 145 Sterne). Je Aufgabe ist es gleich, je Etappe nicht. Sauberes Arbeiten soll sich lohnen, ohne das Kind zu bestrafen, das mehr üben muss.

**Regeln (entschieden):**
1. Übungsaufgabe richtig **im ersten Versuch ohne Tipp**: 10 Sterne (wie bisher, je Aufgabe einmal). Richtig erst im zweiten Versuch oder mit Tipp: **5** Sterne. Neue Regel `sterne_uebung_mit_hilfe` = 5.
2. **Landungs-Bonus** je Kind und Etappe genau einmal, im Moment der Landung: ohne Fehler **80**, mit 1–2 Fehlern **40**, sonst **10**. Regeln `sterne_landung_ohne_fehler` 80, `sterne_landung_wenig_fehler` 40, `sterne_landung_sonst` 10, `landung_wenig_fehler_max` 2.
3. „Fehler“ = falsche Antwort auf eine Übungsaufgabe dieser Etappe bis zur Landung (keine Tests, keine Wiederholungen, keine Mischkarten). Ein genommener Tipp ist kein Fehler (er kostet nur über Regel 1).
4. **Nachträglich** für alle schon gelandeten Etappen (echte Landung, nicht über „Kann er“ gesetzt): Bonus nach derselben Regel gutschreiben. Schon gebuchte Sterne werden nie gekürzt; Regel 1 gilt erst ab Einspielen.
5. Wiederholungen bleiben wie in WD entschieden (10, nur selbst gelöst).

### FP-S · an `bau-lehrer` (Datei, nicht einspielen)
- Neue Migration `supabase/migrations/20261122_fp_s_faire_punkte.sql`, baut auf WD-S 2/3 auf (wird danach eingespielt). Kein DROP, kein DELETE.
- Neuer Sterne-Grund für den Bonus (Constraint `sterne_grund_check` erweitern), Buchung einmalig je Kind+Etappe (doppelter Aufruf, gleichzeitige Antworten: genau eine Buchung).
- `schule_uebung_pruefen` liefert bei der Landung zusätzlich `landung {bonus, fehler, stufe: 'ohne'|'wenig'|'sonst'}` und bei jeder Antwort die tatsächlich gebuchten Sterne (`sterne`), damit die App nichts selbst rechnet (Wunsch von bau-motivation). Regeln über `schule_konto`/Regel-Auslieferung mitgeben.
- Nachbuchung als Funktion `schule.landung_bonus_nachbuchen()` (liefert je Kind Anzahl Etappen und Summe, nur Nummern), einmalig, zweiter Lauf tut nichts. Der Haupt-Chat führt sie nach Probelauf aus.
- Rauchtest `supabase/tests/fp_s_rauchtest.sql` (begin … rollback, Testkind): 10/5, Bonus 80/40/10, genau einmal, gesetzte Etappe ohne Bonus, Nachbuchung zweimal = einmal, Lernstand/Stufen unverändert. Der Test darf nicht von der Zusammensetzung einer echten Etappe abhängen (siehe Nachtrag WD-S 3).
- Meldung im Postfach: „FERTIG: FP-S“ mit Vorher/Nachher-Zahlen der Nachbuchung aus einem lesenden Lauf.

### FP-App · an `bau-motivation` (nach FP-S-Schnittstelle, App 0.87.0)
- Anzeige nach der Antwort aus dem Serverwert `sterne` (10 bzw. 5; bei 5 kurzer Hinweis „selbst gelöst gibt 10“ – ohne Tadel).
- Landungs-Einblendung zeigt den Bonus: „Direktflug – ohne Fehler +80“, „Fast direkt +40“, „Gelandet +10“ (Wortlaut darf der Gestalter ändern). Fehlt `landung`, bleibt alles wie bisher.
- Einmaliger Hinweis nach der Nachbuchung („Für deine bisherigen Landungen gab es … Sterne“), wenn der Server ihn liefert; sonst nichts.
- Info-Seite der Regeln anpassen. Tests ergänzen. Meldung: „FERTIG: 0.87.0“.

### Aufgaben nachliefern · an `lehrplan-lb`
Etappen mit weniger als 3 nie beantworteten Aufgaben der Stufen 2–3 (aus `schule.etappen_wenig_frisch()`): Einheit 39 „ordnen“ und „zahlengerade“, Einheit 5 „waage“. Je Etappe 8 neue Übungsaufgaben (Stufe 2–3, mindestens zwei Aufgabentypen, eigene Formulierungen, keine Schulbuch-Aufgaben wörtlich), im üblichen Einheiten-Format, Prüfskript grün. Meldung: „FERTIG: Aufgaben frisch“.

### Nachtrag WD-S 4 – Rückläufer ChatGPT 921 (22.11., 11:55 Berlin)

ChatGPT hat WD-S 3 / WD-4b / 907 c bei Commit 7675d32 gelesen: die vier Muss aus 919 sind zu, fünf neue Muss. Bewertung des Haupt-Chats: alle berechtigt, im Alltag selten, aber billig zu schließen – vor dem Einspielen erledigen. **Vor FP-S bearbeiten.**

**An `bau-lehrer`** – neue Datei `supabase/migrations/20261122_wd_s4_nacharbeit_921.sql` (nach WD-S 3 und WD-4b einzuspielen; schon gelieferte Dateien nicht ändern, außer den Tests). Kein DROP, kein DELETE.
1. **Mischkarte beim Einlösen prüfen (Muss 1):** Eine ausgegebene Mischkarte zählt nicht mehr als Misch-Nachweis/Wiederholung, wenn seit der Ausgabe eine *andere* Aufgabe derselben Etappe beantwortet wurde (Prüfung im Server beim Einlösen). Zweiter Versuch einer schon begonnenen Mischkarte bleibt möglich. Test: A ausgeben → B derselben Etappe beantworten → A ohne Neuladen einlösen → `misch.gueltig` false, keine Wiederholung.
2. **Wiederholung mit Hilfe: keine Sterne (Muss 2, Festlegung Haupt-Chat):** Jede richtig gelöste *fällige Wiederholung oder Mischkarte* mit Tipp oder im zweiten Versuch bucht 0 Sterne – auch keine Übungssterne. Antwort und Konto stimmen überein. (FP ändert daran nichts: 5 Sterne mit Hilfe gelten nur beim normalen Üben einer Etappe.) Test: Sternsumme und Gründe vorher/nachher.
3. **Runde fertig bei gleichzeitigen Antworten (Muss 3):** Abschluss der Tagesrunde je Kind und Tag serialisieren (Sperre auf der Runden-Zeile vor dem Zählen). Zwei-Sitzungen-Test an zwei verschiedenen letzten Pflicht-Etappen, Zustand danach direkt per SELECT.
4. **`wdh_staffel_zurueck`/`_strecken` unter Sperre (Muss 4):** Karten in fester Reihenfolge `for update` sperren, unter der Sperre prüfen und schreiben.
5. **Tests (Muss 5, Sollte 1, 3):** `wd_s3_rauchtest.sql` wie im Nachtrag „Rauchtest stabil machen“; Teil 7 darf fehlende WD-4b-Funktionen nicht überspringen; `wd_s3_gleichzeitig.sh` bricht bei „FEHLER“ mit Exit ≠ 0 ab; `wdh_aufgabe_da` als deterministisches EXISTS (ohne Zufallswahl); Fälle 0/1 freie Aufgabe und Lerntage mit Pausen.
6. **Rechte (Sollte 4):** für alle neuen `schule.*`-Helfer aus WD-S 2/3/4 `revoke all … from public, anon, authenticated`, soweit noch nicht geschehen.
Meldung im Postfach: „FERTIG: WD-S 4“ (ersetzt „FERTIG: WD-S 3 Test“).

**An `bau-motivation`** – App 0.86.3 (vor 0.87.0):
- Runde gemacht, noch fällige Etappen, aber keine wählbare Aufgabe: kein Angebot „freiwillige Extras“, sondern „Heute keine passende frische Aufgabe – bleibt für später offen.“ (Sollte 2)
- Siegel-Text „FÜR IMMER GELERNT“ ersetzen (Etappe kann nach einem Fehler zurück in den Takt), z. B. „ABGELEGT“; Wortlaut nach Gestalter-Vorgabe `inhalte/pruefung/kind/abgelegt/`, falls dort anders. (Sollte 4)
- Anzeige bei Wiederholung/Mischkarte mit Hilfe: 0 Sterne, aus dem Serverwert.
Meldung: „FERTIG: 0.86.3“.

### Nachtrag FP-S 2 – Rückläufer ChatGPT 924 (22.11., 12:50 Berlin) · an `bau-lehrer`

ChatGPT 924: die fünf Muss aus 921 sind zu (WD-S 4). Ein neues Muss zu FP-S, dazu Sollte. Neue Datei `supabase/migrations/20261122_fp_s2_nacharbeit_924.sql` (nach FP-S einzuspielen; gelieferte Migrationen nicht ändern). Kein DROP, kein DELETE.
1. **`sterne` in der Antwort (Muss):** nicht mehr als Differenz der ganzen Kind-Sternsumme vor/nach dem Aufruf berechnen (zwei gleichzeitige Antworten desselben Kindes melden sonst fremde Sterne mit), sondern nur die in diesem Aufruf eingefügten Buchungen zählen (RETURNING bzw. aufruf-lokaler Zähler). Gilt auch für `misch.sterne`. Zwei-Sitzungen-Test: zwei Etappen gleichzeitig; Landung gleichzeitig mit Nachbuchung – jede Antwort meldet genau ihre Sterne, Summe stimmt.
2. **Misch-Gültigkeit einmal entscheiden (Sollte 2):** Ergebnis der einen Prüfung an Antwort und Wertung durchreichen.
3. **Nachbuchungs-Hinweis (Sollte 3):** „gesehen“ im Server merken (Zeitpunkt je Kind, kleine Aktion mit Zugriffsprüfung) statt nur im Gerät; an `bau-motivation` die Schnittstelle melden.
4. **Tests (Sollte 1, 4):** `wd_s3_gleichzeitig.sh` wartet auf beide Prozesse einzeln und bricht bei Fehler ab; `fp_s_rauchtest.sql` ergänzt um 1 Fehler, Tipp, zweiter Versuch, Mischkarte, Fehler nach der Landung, Wiederlandung.
Meldung im Postfach: „FERTIG: FP-S 2“.

## Prüf-Auftrag LP-RS – Realschul-Lehrplan Punkt für Punkt (22.11., 13:00 Berlin) · an `lehrplan-lb`

**Anlass (Sebastian):** „Ich glaube euch irgendwie noch nicht.“ In der Matrix hat RS 7 rund 20 Themen, RS 8 nur 7–10. Stichprobe des Haupt-Chats gegen LehrplanPLUS (Gruppe I, 7 und 8):
- Lernbereiche und Stunden stimmen (7: 8 Lernbereiche, 8: 7 Lernbereiche, je ca. 112 Std.).
- RS 8: Lernbereich 1 Vierecke (12 Std.), 2 Drehung (6 Std.), 7 Daten und Zufall (8 Std.) haben kein Thema in Klasse 8; Lernbereich 4 (40 Std.) nur eines – Terme/Gleichungen stehen in Klasse 7, weil ein Thema nur an einer Klasse hängt.
- Zuordnungen fehlen ganz: RS 7 „Dreiecke“ (5 Punkte), „Ortslinien“ (6 Punkte) – obwohl Themen 44, 45, 73 diesen Lernbereich als Beschriftung tragen; RS 8 „Daten und Zufall“ 2 von 3; RS 9 „Kreis“ 2 von 2. Zuordnungstabelle und `thema.lernbereich` widersprechen sich.
- Die Kompetenz-Texte ab Klasse 7 sind Kurzfassungen (Quelle-Hinweis „nicht gegen Original geprüft“).

**Aufgabe (nur prüfen und Dateien liefern, nichts einspielen):**
1. **Original abgleichen:** Realschule Bayern Mathematik 5–10, ab Klasse 7 **beide** Wahlpflichtfächergruppen (I und II/III), jede Seite von lehrplanplus.bayern.de neu abrufen. Je Lernbereich: Nummer, Titel, Stunden, Zahl der Kompetenz- und Inhaltspunkte – gegen `schule.eintrag` (Quellen 7, 8, 24, 25, 12, 26, 13, 14, 15, 16). Abweichungen und fehlende Punkte auflisten. Keine Lehrplantexte wörtlich übernehmen (eigene Kurzfassung bleibt), aber jede Kurzfassung auf Sinn gegen das Original prüfen.
2. **Zweite Quelle je Klasse und Gruppe:** mindestens ein Stoffverteilungsplan oder Inhaltsverzeichnis eines zugelassenen bayerischen Realschulbuchs (z. B. C.C. Buchner Mathe.Logo, Westermann Mathematik Realschule Bayern, Cornelsen) und, für 9/10, die Themen der Abschlussprüfung (ISB/Kultusministerium). Zweck: Gegenprobe, ob ein Thema in der Praxis in dieser Klasse unterrichtet wird. Quelle mit Link und Abrufdatum nennen; Widersprüche zum amtlichen Plan ausweisen (amtlich gilt).
3. **Jeder Punkt braucht ein Zuhause:** Für jeden Kompetenz-/Inhaltspunkt entweder Thema (mit Bezug „neu“ oder „weitergeführt“) oder ausdrücklich „Lücke – kein Thema vorhanden“. Tabelle je Klasse/Gruppe: Lernbereich · Stunden · Punkte · zugeordnet · Lücken · Themen.
4. **Klasse je Thema prüfen:** Für jedes Thema mit `klasse_fest.rs_by`: In welchen Klassen kommt es laut Original vor (erstmals / weitergeführt)? Liste der falsch eingeordneten Themen mit Beleg (Lernbereich-Nummer).
5. **Gymnasium als Stichprobe:** Klasse 7 und 8 nach demselben Verfahren (Leo). Nur Bericht.
6. **Vorschlag Datenmodell** (kurz, für `bau-lehrer`): wie ein Thema in mehreren Klassen geführt wird („neu“/„weitergeführt“) und wie die Matrix je Klasse die Abdeckung der Lernbereiche nach Stunden zeigt statt einer Themenzahl.

**Lieferung:** `inhalte/pruefung/lehrplan/rs_pruefung_2211.md` (Bericht mit Tabellen und Quellenliste), `rs_pruefung_2211.json` (maschinenlesbar: Quelle, Lernbereich, Punkt, Thema, Bezug, Befund) und – getrennt – ein Korrektur-SQL als Datei (nur INSERT/UPDATE auf `schule.zuordnung`, `schule.eintrag`, `schule.thema`; kein DROP, kein DELETE), das der Haupt-Chat nach Probelauf einspielt. Trennen: gesichert (am Original belegt) / Annahme / offen. Meldung im Postfach: „FERTIG: LP-RS“.

### Nachtrag FP-S 3 – Rückläufer ChatGPT 929 (22.11., 13:30 Berlin) · an `bau-lehrer`

ChatGPT 929: Muss aus 924 (Sterne aus Summendifferenz) ist zu. Ein Muss bleibt: **Mischkarte atomar einlösen.** FP-S 2 prüft die Gültigkeit ohne Sperre vor und reicht das Ergebnis durch; entschieden wird aber erst in `schule.misch_buchen` (UPDATE … FOR UPDATE SKIP LOCKED). Findet dieser Schritt keine freie Ausgabe (zweite gleichzeitige Antwort auf dieselbe Karte, oder inzwischen andere Aufgabe der Etappe beantwortet), wird normal gebucht – die Antwort meldet trotzdem `misch.gueltig = true`.
Neue Datei `supabase/migrations/20261122_fp_s3_nacharbeit_929.sql` (nach FP-S 2): Gültigkeit und Beanspruchen der Ausgabe unter einer gemeinsamen Sperre entscheiden; der **tatsächliche** Ausgang geht an Versuch, Wiederholungswertung und Antwort (`misch.gueltig`, `kein_wdh`). Tests: zwei verschiedene `client_id` auf dieselbe ausgegebene Mischkarte; A vorprüfen → B derselben Etappe beantworten → A einlösen; in beiden Fällen keine falsche Misch-Bestätigung, kein Wiederholungsfortschritt im Rückfall. Paralleltest D zusätzlich für gleichzeitiges Beanspruchen desselben Landungs-Bonus. Kein DROP, kein DELETE. Meldung: „FERTIG: FP-S 3“.

**An `bau-motivation`** (App 0.87.1): Nachbuchungs-Hinweis über die neue Aktion `schule_landung_nachbuchung_gesehen` quittieren (Feld `gesehen_am` aus `schule_konto`), localStorage nur noch als Rückfall. Meldung: „FERTIG: 0.87.1“.

### Nachtrag LP-RS – Gegenprobe ChatGPT 927/928/930 (22.11., 13:30 Berlin) · an `lehrplan-lb`

ChatGPT hat alle acht amtlichen Pläne (7–10 × Gruppe I, II/III) unabhängig gelesen. Bitte in die Prüfung einarbeiten und selbst nachprüfen:
- Stichprobe 7 I / 8 I bestätigt. Stunden laut amtlichem Plan: 7 I 112 / II–III 84; 8 I 112 / 84; 9 I 140 / 84; 10 I 120 / 96.
- **Die Gruppen unterscheiden sich in der Klassenlage:** Dreiecke I 7 ↔ II/III 8; lineare Funktionen I 8 ↔ II/III 8 (y = mx) und 9 (y = mx + t); quadratische Funktionen/Gleichungen I 9 ↔ II/III 10; Körperberechnungen I 9 ↔ II/III 10; Matrizen-Abbildungen und Potenzfunktionen nur 10 I. Ein einziges `klasse_fest.rs_by` je Thema kann das nicht abbilden.
- Nicht pauschal verschieben: Extremwerte quadratischer Terme stehen in beiden Gruppen in 8; Schrägbilder 7 I und 8 II/III; Determinanten auch 7 II/III; Baumdiagramme/Vierfeldertafel schon in 8, Laplace 9, Pfadregeln 10.
- Im Repo auffällig: Themen 48 und 78 ohne RS-Klasse trotz RS-Lernbereich; 91 steht bei RS 8, beschreibt aber auch 7 I; 46 (RS 6) enthält Drehung (8 I); 33 mischt y = mx und y = mx + t.
- Zweitquellen, die ChatGPT lesen konnte: Inhaltsverzeichnis Westermann 7 I (kapiert.de), Kapitelübersicht 8 II/III (braille.bildung.hessen.de), ISB-Leistungsaufgaben 9, Abschlussprüfung 2026 I und II/III (isb.bayern.de). Die Jahrgangsstufenprofil-Adressen für 8–10 führten auf die Startseite – nicht als Beleg verwenden.
- **Vorschlag Datenmodell (Punkt 6 des Auftrags) deshalb verbindlich so anlegen:** Zuordnung je `Gruppe × Klasse × Lernbereich × Punkt → Thema/Etappe` mit Bezug „neu/weitergeführt“; Lernstand und Sterne werden nie doppelt geführt. Welche Gruppe die App zeigt, entscheidet Sebastian (offen).
