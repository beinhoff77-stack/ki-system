# Korrektur nach der dritten Vorprüfung (Befund → geschlossen wie)

Stand: Zweig `helfer-vtest-r2`. Geprüft nach der Korrektur: `bauen.py` feste Prüfungen ok, `gegenrechnung.py` 0 Abweichungen, `vtest_pruefen.py --runde 2` ohne Fehler (zwei bekannte Hinweise 106 und 108: gerundet wird nur in der Voraussetzung). Vor jedem Ersatz wurde im Bestand der Etappe (`inhalte/themen`, alle `rollend-*`) nach dem Kern gesucht, siehe `bestandsvergleich.md` (Nachtrag).

## B-Befunde

- **B1 001 (Test)** → ersetzt: Aus den Nettozinsen (45 €) und dem Sparbuch (3 000 € zu 1 %) wird rückwärts auf die Kreditzinsen (75 €) und den Kredit (2 500 €) geschlossen. Kern anders: Bestand rechnet die Bilanz vorwärts.
- **B2 015 (Test)** → ersetzt: Zinsen gleich (120 €), Zinssatz steigt von 2 % auf 3 %: Kapital 6 000 € → 4 000 €, Einsparung 2 000 €. Kern: Kapital und Zinssatz sind umgekehrt proportional, drei Lücken. Die vorige Aufgabe war wieder die Differenz-Aufgabe aus dem Bestand.
- **B3 005** → ersetzt: Zinssatz aus Mias Sparbuch (50 € auf 2 000 € = 2,5 %) auf den Kredit des Bruders übertragen (90 € → 3 600 €). Der vermehrte Grundwert entfällt, damit auch der Lehrplanzweifel zu 005.
- **B4 044** → ersetzt: zwei Zählweisen eines Streichholzmusters als Terme (zwei von drei Termen richtig, Figur 10 hat 31).
- **B5 080** → die Lösung folgt keiner Textreihenfolge mehr: 079 zählt über fünf Dreiecke (Lösung 1, 2, 2), 080 verlangt erst γ aus α und β (90°) und dann die Lage (2). Die Zuordnung A, B, C mit Lösung 1, 2, 3 gibt es nicht mehr.
- **B6 055** → umgebaut: „Faktor 6x, k ganze Zahl zwischen 7 und 20“, Soll 12. Die gesuchte Zahl steht nicht im Text; 6 (aus 6x) und 18 sind Fehlbilder.
- **B7 057** → Fehlbild „Zeile 1 für falsch gehalten“ steht bei Lücke 1; Lücke 2 bekam „(2x)² als 2x²“. In `bauen.py` steht jetzt die feste Prüfung „jede Lücke braucht ein Fehlbild“. Sie fand außerdem 070 (Lücke 1: Winkel MCB 50° statt ACM) und 123 (Lücke 1: M gleich D oder C gelesen); beide ergänzt.
- **B8 017** → Fehlbild-Text berichtigt: „52 · 0,04 = 2,08 ist nicht das Kapital, sondern nur ein kleiner Teil der Zinsen“.
- **B9 Fehler-Detektive** → Fehlerzeilen verschoben: 018 und 052 jetzt Zeile 1, 081 Zeile 1, 008 Zeile 3, 120 Zeile 4. Verteilung der 18 Aufgaben: Zeile 1 dreimal, Zeile 2 siebenmal, Zeile 3 siebenmal, Zeile 4 einmal; die vier Tests haben die Zeilen 3, 2, 2, 4. Feste Prüfung: mindestens zwei Aufgaben mit Zeile 1, keine Zeile über 45 %, in den Tests mindestens drei verschiedene Zeilen (bei Auswahl-Detektiven trägt `bauen.py` die Zeile in einer Tabelle FD_AUSWAHL ein).
- **B10 079/081, 082/084** → 081 liegt jetzt im Pool sicherung und hat den Fehler schon in Zeile 1 (gleich weit von den Seiten), 079 ist ersetzt (Zählung über fünf Dreiecke), 082 ist im Pool korrektur und nennt als falsche Begründung die Höhen, nicht mehr die Mittelsenkrechten. Damit liegen 079, 080, 082 (korrektur) und 081, 083, 084 (sicherung); die Mittelsenkrechte/Winkelhalbierende-Verwechslung kommt nur noch in 081 (Fehlersuche) und 084 (gleichseitig) vor.
- **B11 Schema** → ersetzt: zeitanteil 025 (Zinssatzwechsel im Jahr), minusklammer 042 (lange Klammer mit fünf Gliedern), aequivalenz 046 (Zahlenrätsel) und 048 (Übereinstimmung an zwei Stellen), ausklammern 051 (negativer Faktor), runden_sinnvoll 116 (Rundungsbereich in Preisrechnung) und 118 (Rundungsbereich durch eine Zahl teilen). Danach Schema-nahe je Lernziel: zeitanteil 023, 026; minusklammer 037, 040 (042 Grenzfall); aequivalenz 043, 045; ausklammern 053, 056; runden_sinnvoll 113, 114. Alle anderen Lernziele unverändert bei höchstens zwei (Tabelle der Vorprüfung).
- **B12 Auswahl** → die richtige Möglichkeit war in 054, 059, 064, 094, 110, 111, 115 und 129 mindestens 25 % länger als die längste falsche; alle acht gekürzt (064 und 054 verlieren auch das „nämlich 5 cm“ und den Nebensatz mit Semikolon). Nebensatz-Marker (Semikolon, „aber“, „, nicht“, „, auch“): vorher richtig 37 %, falsch 12 %; in zehn Aufgaben aus den richtigen Möglichkeiten entfernt (011, 032, 039, 062, 077, 089, 094, 105, 111, 117), jetzt richtig 2 %, falsch 11 %. Fest in `bauen.py`: richtige ≥ 1,25 × längste falsche höchstens in 15 % der Aufgaben (jetzt 1 von 41, die 059), Nebensatz-Marker höchstens 12 Punkte Unterschied. Sammel-Möglichkeiten: 5, davon 2 richtig (`bauen.py`-Zählung nach Anfangswort „Beide/Alle/Keine/Gleich“); die Vorprüfung zählt 7 mit „Weder …“, siehe README.

## C-Befunde

- C1 006: `idee` heißt jetzt „Kapital für gleiche Zinsen“ (nicht „Zinssatz aus Differenz“), siehe `ideen.py`.
- C2 013: README-Angabe berichtigt (Lückenwerte 36 und 39).
- C3 030: Fehlbild für „1“ (Vorzeichen von −x² verloren) ergänzt.
- C4 033: Fehlbild-Text bleibt (nur lose passend, kein Fehler in der Lösung); ich habe ihn nicht geändert.
- C5 042 ersetzt (s. B11). C6 051 ersetzt (s. B11).
- C7 075: Fehlbild 4 bleibt als konstruierter Fall, ohne Folgen für die Lösung.
- C8 014, 100, 107: unverändert; `typ` begruenden ohne verlangte Begründung bleibt offen.
- C9 108: bleibt, die Einsicht liegt im Gegenfall (49).
- C10 Tests nicht klar die anspruchsvollsten (036, 064, 113, 001): 001 ist durch den Zwei-Schritt-Rückwärtsschluss deutlich schwerer als 002 und 007; 064 und 036 bleiben Auswahl mit Stufe 3; 113 ist Produktschätzung mit zwei Fehlern (Stufe 3). Nicht gemessen.
- C11 Lücke 1 ohne Fehlbild in 057, 070, 123 → ergänzt (s. B7).
- C12 README: Sammel-Möglichkeiten und Zeilenzuordnung berichtigt; `bestandsvergleich.md` ordnet 022 jetzt zeitanteil und 078 umkreis_inkreis zu (Tabellenzeilen unverändert, Nachtrag nennt es). Der Lehrplanabschnitt heißt „Kongruenz, besondere Dreiecke und Dreieckskonstruktionen“; das Etikett „M7 5 (Kreis)“ bleibt ein Repo-Etikett.
- C13 Platzfolge: Hinweis zur Kenntnis genommen; die Platzverteilung ist A 8, B 12, C 10, D 11.
- C14 Nahe am Bestand, behalten: siehe `bestandsvergleich.md`.

## Lehrplan-Zweifel (offen, nichts geraten)

- Lage Gerade/Kreis (VT2-071 bis 077): Ob der Stoff in Jahrgangsstufe 7 steht, ist nicht bestätigt (Vorprüfer etwa 50 %, Jahrgangsstufe 8 nicht abrufbar). Gegenprüfung bei der Schule bzw. im Schulbuch.
- Umkreis/Inkreis (VT2-078 bis 084): Im Lehrplan nur als Beispielliste im Lernbereich 5, die Lage des Umkreismittelpunkts nicht im Wortlaut (Vorprüfer etwa 65 %).
