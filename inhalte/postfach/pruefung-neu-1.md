# Postfach pruefung-neu-1 (Fünfundzwanzigste Runde, unabhängige Prüfung)

Neueste Meldung oben. Prüfer: Chat `pruefung-neu-1`, hat keines der geprüften Themen geschrieben.

Allgemein gilt für alle Berichte:
- „Nachgerechnet“ heißt: Lösung unabhängig vom Generator bestimmt – entweder mit einem eigenen Prüfskript, das die Zahlen aus dem **Fragetext** liest und neu rechnet (nicht aus `c`), oder von Hand.
- Übungen ohne `g` sind laut Zwanzigster Runde „überzählig“ und werden beim Einspielen gesperrt. Sie wurden auf richtige Lösung (a) geprüft, nicht auf Stufe/Typ (f).
- Lehrplan: Die Seiten von lehrplanplus.bayern.de konnte ich in dieser Sitzung nicht direkt abrufen (Abruf brauchte eine Freigabe, die nicht beantwortet wurde). Lehrplanaussagen stützen sich daher auf `lehrplan_andere` in `themenliste.json` und auf ISB-Dokumente aus der Websuche (Abruf 20.11.2026); was nicht belegt ist, steht als Annahme da.

## 2026-11-20 – FERTIG: Prüfung neu, Chat 1 (Übersicht)

| Thema | Aufgaben gelesen / nachgerechnet | a | b | c | d | e | f | Urteil |
|---|---|---|---|---|---|---|---|---|
| abbildungen.determinanten2 | 240 / 240 | 0 | 2 | 1 | 0 | 0 | 0 | mit Korrekturen in Ordnung |
| daten.stichproben | 188 / 188 | 10 | 3 | 0 | 2 | 7 | 2 | mit Korrekturen in Ordnung |
| terme.quadratische_extreme | 196 / 196 | 0 | 0 | 2 | 0 | 0 | 0 | mit Korrekturen in Ordnung |
| gleichungen.wurzel | 227 / 227 | 0 | 1 | 0 | 0 | 0 | 0 | in Ordnung (eine Klarstellung) |
| abbildungen.matrizen | 263 / 263 | 0 | 0 | 0 | 0 | 0 | 0 | in Ordnung |
| funktionen.reihen | 287 / 287 | 0 | 1 | 1 | 0 | 0 | 0 | mit Korrekturen in Ordnung |
| funktionen.betrag | 174 / 174 | 0 | 0 | 0 | 0 | 3 | 0 | in Ordnung (Lösungswege geglättet) |

Kein Flug „nicht freigabefähig“. Einzige echte Mehrdeutigkeiten (Art a) in `daten.stichproben`, darunter eine **Testaufgabe** mit zwei richtigen Antworten – bitte beim Einspielen beachten.

**Zum Einspielen (Fakt):** Beim Neuerzeugen übernehmen die Generatoren das Feld `klasse` aus `themenliste.json`. Die eingecheckten Dateien waren hier veraltet: `daten.stichproben` hatte nur `{"rs_by": 7}` (jetzt `{"rs_by": 7, "ib_myp": 2}`), `funktionen.betrag` hatte `{"ib_myp": 4}` (jetzt `{"ib_myp": 5}`, wie in der Themenliste). Ich habe das so gelassen, weil die Themenliste maßgeblich ist; der Haupt-Chat sollte prüfen, ob die Datenbank noch die alte Klasse führt.

Alle Änderungen nur in Generatoren und Themendateien; nach jeder Änderung habe ich die alte und neue Themendatei Aufgabe für Aufgabe verglichen – geändert haben sich nur die im jeweiligen Bericht genannten Aufgaben (die Zufallsfolge der Generatoren ist erhalten). Kein Merge, keine Datenbank, kein App-Code, keine Kinderdaten.

## 2026-11-20 – funktionen.betrag (IB MYP 5): in Ordnung (Lösungswege geglättet)

**Gelesen und nachgerechnet (Fakt):** 5 Lernkarten und alle 174 Aufgaben (114 Übungen, 10 Knobel, 5 Test, 15 Korrektur, 30 Sicherung). 62 Aufgaben mit eigenem Skript aus dem Fragetext nachgerechnet (Funktionswerte, Knickpunkt, Grenze und Terme der Stücke, Betragsgleichungen und Lösungsanzahl über eine Gleichungslösung) – 0 Abweichungen. Die übrigen 112 (Auswahl, Graphen aus den Grafikdaten, Ungleichungen, Toleranzen, Gegenbeispiele, Knobel) von Hand nachgerechnet – alle richtig. Beispielrechnungen aller 5 Karten stimmen.

**Änderungen je Fehlerart:** a) 0 · b) 0 · c) 0 · d) 0 · e) 3 · f) 0

- e) Drei Lösungswege enthielten Generator-Reste mit „+ 0“: „Für x ≥ 0 ist x + 0 ≥ 0, der Betrag fällt weg“ (2 Sicherungen) und „|−8 + 0| = 8“ (1 Übung). Jetzt „Für x ≥ 0 ist x ≥ 0 …“ bzw. „|−8| = 8“. Fragen und Lösungen unverändert.

**Meinung, nicht geändert:** In „Ali löst |x + 4| = 4 und schreibt: „x = 0““ lautet eine Falschoption „Es fehlt x = 0“ – unsinnig, aber nicht richtig. Bei d = 0 fällt eine der Falschoptionen weg (nur 3 Antworten).

**Lehrplan:** IB MYP 5: Betrag, Betragsfunktion, stückweise Darstellung, einfache Betragsgleichungen und -ungleichungen – passt (Annahme, nicht gegen das IB-Dokument geprüft; Lehrplanfeld in der Themenliste leer). Klasse siehe Übersicht oben.

**Nicht geprüft:** Graphen nur über die Grafikdaten (a, b, c), nicht in der App angesehen. Übungen ohne `g` (9, gesperrt) nur auf Lösung.

Prüfskript: OK, 0 Gruppen „gleich gebaut hintereinander“.

## 2026-11-20 – funktionen.reihen (IB MYP 5): mit Korrekturen in Ordnung

**Gelesen und nachgerechnet (Fakt):** 8 Lernkarten und alle 287 Aufgaben (191 Übungen, 16 Knobel, 8 Test, 24 Korrektur, 48 Sicherung). 114 Aufgaben mit eigenem Skript aus dem Fragetext nachgerechnet (Folge erkennen und Glieder direkt aufsummieren statt Formel, Rekursion Schritt für Schritt, explizite Formel, aₙ, q, „wie viele Glieder bis Summe …“, Läufer/Stämme/Sparen/Schachbrett) – 0 Abweichungen. Die übrigen 173 (Summenzeichen, Auswahl, Fehler-Aufgaben, Sachaufgaben, Knobel) von Hand nachgerechnet – alle richtig, u. a. Angebot A/B (Tag 18 bzw. 19), Teleskopsumme 99/100, a₁₀₀ = 199. Beispielrechnungen aller 8 Karten stimmen.

**Änderungen je Fehlerart:** a) 0 · b) 1 · c) 1 (dieselbe Aufgabe) · d) 0 · e) 0 · f) 0

- c) und b) Knobel `sach`: „Ein Frosch springt am 1. Tag 1 m, an jedem weiteren Tag halb so weit wie am Vortag. Welche Strecke (in m) kann er auf diese Weise höchstens zurücklegen?“ – Lösung 2 m ist ein Grenzwert, der nie erreicht wird („höchstens“ stimmt so nicht), und unendliche geometrische Reihen sind laut `offen` bewusst nicht Stoff dieses Flugs. Neu: „… Nach wie vielen Tagen ist er zum ersten Mal insgesamt mehr als 1,9 m weit gekommen?“ → 5 (Summen 1; 1,5; 1,75; 1,875; 1,9375), Einheit entfernt.

**Meinung, nicht geändert:** Die Knobel-Karte „S = 1 + 2 + 4 + … ⇒ S = −1, wo ist der Fehler?“ streift unendliche Reihen und erwähnt im Lösungsweg „strebt gegen 2“. Die Frage selbst verlangt nur „mit einer unbeschränkt wachsenden Summe darf man nicht wie mit einer Zahl rechnen“ – als freiwillige Knobel-Karte vertretbar.

**Lehrplan:** IB MYP 5 (Klasse 10): endliche arithmetische und geometrische Reihen, Summenzeichen – passt (Annahme, nicht gegen das IB-Dokument geprüft). Die drei Folgen-Karten (rekursiv, arithmetisch, geometrisch) stammen laut Generator aus `funktionen.folgen` („Auflösen“); doppelte Inhalte zwischen beiden Flügen habe ich nicht geprüft.

**Nicht geprüft:** Säulenbilder nur im JSON. Übungen ohne `g` (gesperrt) nur auf Lösung.

Prüfskript: OK, 0 Gruppen „gleich gebaut hintereinander“. Vergleich alt/neu: nur die genannte Knobel-Karte geändert.

## 2026-11-20 – abbildungen.matrizen (RS 10, IB MYP 5): in Ordnung

**Gelesen und nachgerechnet (Fakt):** 7 Lernkarten und alle 263 Aufgaben (179 Übungen, 14 Knobel, 7 Test, 21 Korrektur, 42 Sicherung). 136 Aufgaben mit eigenem Skript aus dem Fragetext nachgerechnet (Bildpunkt, Urbild mit Inverser, Drehung x′/y′ mit cos/sin auf zwei Dezimalen, A · B, A + B, Inverse, Determinante, Skalarprodukt, „senkrecht?“, Parameter t und x, Abstand Punkt–Gerade über die Kreuzformel) – keine Abweichung (zwei Meldungen des Skripts waren eigene Lesefehler: zweimal abbilden, „Determinante 1“ statt „keine Inverse“; beide Lösungen von Hand bestätigt). Die übrigen 127 (Auswahl, Verkettungen, Fehler-/Begründungsaufgaben, Lotfußpunkt rückwärts, Knobel) von Hand nachgerechnet – alle richtig, z. B. A · B ≠ B · A in beiden Gegenbeispielen, Gitterpunkte mit Abstand 1 (5 Stück), „für kein a ganzzahlige Inverse“. Beispielrechnungen aller 7 Karten stimmen.

**Änderungen je Fehlerart:** a) 0 · b) 0 · c) 0 · d) 0 · e) 0 · f) 0

**Meinung, nicht geändert:** In der Karte `inverse` nennt Schritt 1 „Determinante von M“, ohne M im Text zu nennen; M steht nur im Bild darüber. Reicht, weil das Bild zuerst gezeigt wird. „Berechne den Betrag (die Länge) von a = (6 | 8)“ ist als Stufe 2 / mehrschritt eher leicht.

**Lehrplan:** Passt zu RS 10 (Koordinatenabbildungen mit Matrizen, Skalarprodukt/Orthogonalität/Winkel, `lehrplan_andere`) und zu IB MYP (Matrizenrechnung, Inverse); nicht gegen lehrplanplus.bayern.de bzw. das IB-Dokument geprüft (Annahme). Bewusst weggelassen laut `offen`: Spiegelung an beliebigen Ursprungsgeraden, Parkettierungen, LGS mit Inverser nur als Urpunkt-Aufgabe – für RS 10 vertretbar, für IB MYP 4/5 fehlt das Lösen von Gleichungssystemen mit der Inversen als eigene Fähigkeit (Annahme, Lehrplanabgleich offen).

**Nicht geprüft:** Koordinatenbilder nur im JSON. Übungen ohne `g` (überzählig, gesperrt) nur auf Lösung.

Prüfskript: unverändert OK (keine Datei geändert).

## 2026-11-20 – gleichungen.wurzel (RS 9): in Ordnung (eine kleine Klarstellung)

**Gelesen und nachgerechnet (Fakt):** 6 Lernkarten und alle 227 Aufgaben (155 Übungen, 12 Knobel, 6 Test, 18 Korrektur, 36 Sicherung). 112 Aufgaben („Löse …“, „Welche Lösungsmenge hat …“, „Gib die Definitionsmenge … an“) mit eigenem Skript aus dem Fragetext gelöst – reelle Lösungen der Gleichung, jede mit Probe in der Ausgangsgleichung, Scheinlösungen verworfen – 0 Abweichungen. Die übrigen 115 (Auswahl, Fehler-/Begründungsaufgaben, Sachaufgaben Fallzeit/Aufprall/Pendel/Horizont, Knobel) von Hand nachgerechnet – alle richtig. Beispielrechnungen der 6 Karten stimmen (z. B. x² + x − 6 = 0 → −3 und 2, L = {2}).

**Änderungen je Fehlerart:** a) 0 · b) 1 · c) 0 · d) 0 · e) 0 · f) 0

- b) `sachaufgabe`, Stufe 3, rueckwaerts: „Ein quadratisches Beet wird an jeder Seite um 3 m verlängert. Dabei wird seine Fläche viermal so groß.“ – „an jeder Seite um 3 m verlängert“ lässt auch „an beiden Enden je 3 m“ (Seite + 6 m) zu; dann wäre die Lösung eine andere. Jetzt: „Jede Seite eines quadratischen Beets wird um 3 m länger. …“ (Lösung 9 m² unverändert). Bei den 12 Aufgaben mit derselben Einleitung steht die Gleichung √A + d = … dabei, dort ist es eindeutig – gelassen.

**Meinung, nicht geändert:** Die Falschoptionen „Ja, aber nur, wenn man die Wurzel auf 8 rundet“ / „Nein, aber nur weil die Probe eine Dezimalzahl ergibt“ (Probe-Aufgaben) sind schwache Ablenker, aber nicht vertretbar richtig.

**Lehrplan:** Passt zu RS 9 („Wurzelgleichungen unter Berücksichtigung ihres Definitionsbereichs lösen“, `lehrplan_andere`; nicht gegen lehrplanplus.bayern.de geprüft). Quadratische Gleichungen (Karte `zwei_seiten`) kommen in der Themenliste vorher (`gleichungen.quadratisch`, RS 9). Nichts Wesentliches fehlt.

**Nicht geprüft:** Zahlenstrahl- und Tabellenbilder nur im JSON. Übungen ohne `g` (22, gesperrt) nur auf Lösung.

Prüfskript: OK, 0 Gruppen „gleich gebaut hintereinander“. Vergleich alt/neu: nur die genannte Aufgabe geändert.

## 2026-11-20 – terme.quadratische_extreme (RS 8): mit Korrekturen in Ordnung

**Gelesen und nachgerechnet (Fakt):** 5 Lernkarten und alle 196 Aufgaben (136 Übungen, 10 Knobel, 5 Test, 15 Korrektur, 30 Sicherung). 87 Lücken-Aufgaben (Ergänzen, Scheitelform, Ausmultiplizieren, Stelle und Wert des Extremums) mit eigenem Skript aus dem Fragetext nachgerechnet (Term einlesen, Koeffizienten, x = −b : (2a)) – 0 Abweichungen. Die übrigen 109 (Auswahl, Sachaufgaben Zaun/Mauer/Kiosk/Kino, Knobel) von Hand nachgerechnet, u. a. alle Kiosk-Einnahmen (337,50 €, 225 €, 270 €, 433,50 €, 726 €) und Beispielrechnungen und Wertetabelle der Karten – alles richtig.

**Änderungen je Fehlerart:** a) 0 · b) 0 · c) 2 · d) 0 · e) 0 · f) 0

- c) `scheitelform`, Stufe 3, transfer: „Ein Wasserstrahl hat die Höhe h(x) = −x² + 6x + 1 … Wie hoch steigt der Strahl höchstens?“ verlangte Maximum und Ausklammern von −1 – beides kommt erst in den späteren Karten `extremwert` und `mit_faktor` (der Tipp sagte sogar „Klammere das Minus vor x² aus“). Ersetzt durch eine Aufgabe mit dem Stoff der Karte: „Eine Hängebrücke für Kinder hängt durch. Die Höhe über dem Bach ist h(x) = x² − 6x + 13 (alles in dm …). Wie hoch ist die Brücke an ihrer tiefsten Stelle?“ → (x − 3)² + 4, 4 dm. Typ und Stufe gleich.
- c) `mit_faktor`, Lösungsweg einer Fehler-Aufgabe: „Der Faktor −2 öffnet nach unten“ spricht von Parabeln (RS 9, laut `offen` bewusst ausgespart). Jetzt: „Der Faktor −2 vor der Klammer heißt: Von 9 wird immer etwas abgezogen (außer bei x = 2) – also Maximum.“

**Meinung, nicht geändert:** Viele Aufgaben sagen „damit ein Binom entsteht“, die Karte sagt „vollständiges Quadrat“. Streng genommen ist schon x² + 6x ein Binom; gemeint ist das Quadrat eines Binoms. Das ist im bayerischen Unterricht übliche Sprechweise, darum gelassen – bei einer späteren Überarbeitung einheitlich „vollständiges Quadrat“ sagen.

**Lehrplan:** Annahme (nicht gegen lehrplanplus.bayern.de geprüft): Quadratische Ergänzung und Extremwerte quadratischer Terme ohne Parabeln passen zu RS 8 (Wahlpflichtfächergruppe I); Scheitelpunkt und Parabeln folgen in RS 9 (`funktionen.quadratisch`). Nichts Wesentliches fehlt.

**Nicht geprüft:** Figurenbilder der Karte `ergaenzen` nur über die Koordinaten im JSON. Übungen ohne `g` (27, gesperrt) nur auf Lösung.

Prüfskript: OK, 0 Gruppen „gleich gebaut hintereinander“. Vergleich alt/neu: nur die zwei genannten Aufgaben geändert.

## 2026-11-20 – daten.stichproben (RS 7, IB MYP 2): mit Korrekturen in Ordnung

**Gelesen und nachgerechnet (Fakt):** 5 Lernkarten und alle 188 Aufgaben (128 Übungen, 10 Knobel, 5 Test, 15 Korrektur, 30 Sicherung). Alle 74 Zahl-Aufgaben von Hand nachgerechnet (Hochrechnung, Prozentpunkte, Spannweite, Fang-Wiederfang, geschichtete Stichprobe, Knobel 37 %/43 %/Würfelmethode) – keine falsche Zahl. Alle 114 Auswahl-Aufgaben einzeln auf „genau eine vertretbare Antwort“ gelesen; dabei die Fehler unten gefunden.

**Änderungen je Fehlerart:** a) 10 · b) 3 · c) 0 · d) 2 · e) 7 · f) 2 (in a enthalten)

a) Zweite vertretbare Antwort:
- **Test** `repraesentativ`: „… werden 100 Personen befragt: nur die Besucher des alten Hallenbads. Warum ist das keine geeignete Stichprobe?“ – alte Optionen: „Eine einseitige Gruppe wird befragt.“ / „Fans der Bahn sind zu stark vertreten.“ / „Wer die Kantine meidet, fehlt.“ / richtig „Schwimmer sind eher dafür.“ Die erste Option ist ebenfalls richtig. Neu: „100 Personen sind zu viele.“ / „Verärgerte sind zu stark vertreten.“ / „Man darf nie nur einen Teil befragen, nur alle.“ / richtig „Schwimmer sind eher dafür.“ Ursache im Generator: Falschantworten kamen aus den Gründen anderer Szenen, darunter allgemeine („eine einseitige Gruppe …“, „nur eine Altersgruppe …“), die auf jede schlechte Auswahl passen. Jetzt zwei echte Denkfehler plus ein fremder „… zu stark vertreten“-Grund (betrifft auch 1 Übung und 5 Sicherungen, siehe e).
- „Nur Freiwillige antworten“ (4 Übungen, 1 Korrektur, 1 Sicherung): alt z. B. „Eine Zeitschrift ruft ihre Leser auf, im Internet zum Thema „Handyverbot an Schulen“ abzustimmen. Es kommen 9 000 Antworten. Welche Fehlerquelle liegt vor?“ – „Die Auswahl ist einseitig“ war ebenfalls vertretbar (nur Leser/Hörer/wer an der Schultür vorbeikommt, die Grundgesamtheit war offen). Neu: „Eine Zeitschrift will wissen, was ihre Leser zum Thema „Handyverbot an Schulen“ denken, und ruft sie auf, im Internet abzustimmen. …“ (ebenso Radiosender: „… will wissen, was seine Hörer … denken, und bittet sie anzurufen.“; Schule: „Eine Schule will wissen, was ihre Kinder zum Thema … denken. An der Schultür hängt ein Zettel: Wer möchte, wirft seine Meinung in den Briefkasten.“). Lösung bleibt „Nur Freiwillige antworten.“
- „Wie verbessert man die Umfrage am wirksamsten?“ bei einseitiger Auswahl bzw. Freiwilligen (4 Übungen): Falschoption „Mehr Personen zufällig auswählen.“ war ebenfalls eine Verbesserung. Neu: „Einfach mehr Personen auf dieselbe Art befragen.“ (der echte Denkfehler „größer = besser“). Bei „Stichprobe zu klein“ bleibt „Mehr Personen zufällig auswählen.“ die richtige Antwort.

b) „Es sollen genau 60 Personen werden.“ → „… befragt werden.“; „Finden Sie nicht auch, dass der Spielplatz erneuert wird?“ / „… dass mehr Radwege gebaut werden?“ → „Finden Sie nicht auch, dass es gut wäre, wenn …?“ (Satz war schief, Fehlerquelle bleibt suggestiv).
d) Karte `begriffe`: „Vollerhebung“ kam in 9 Aufgaben (davon 5 Korrektur/Sicherung) vor, wurde aber nicht erklärt → Regel ergänzt: „Befragt man alle, heißt das ⟦Vollerhebung⟧.“ Karte `hochrechnen`: „Prozentpunkte“ in 2 Aufgaben, erklärt erst in der späteren Karte `aussagen` → Wort ergänzt.
e) 6 Auswahl-Aufgaben „Warum ist das keine geeignete Stichprobe?“ hatten Falschantworten ohne Bezug zur Frage („Sie sind gar nicht wahlberechtigt“ bei Busfahrgästen) – siehe a). Knobel „gerundet 43 %“: Lösungsweg nannte 14 % und 29 % als Werte für n ≤ 6 (das sind 1/7 und 2/7) – berichtigt.
f) Schul-Briefkasten mit 9 000 bzw. 3 500 Antworten unrealistisch → 450 bzw. 350.

**Lehrplan:** Passt zu RS 7 („Stichprobeneignung/Repräsentativität beurteilen“, `lehrplan_andere`); die Hochrechnung ist laut `offen` bewusst ergänzt (Meinung: sinnvoll, nicht zu schwer). IB MYP 2: Annahme, nicht gegen das IB-Dokument geprüft. Nichts Wesentliches fehlt.

**Nicht geprüft:** Säulen- und Bruchstreifenbilder nur im JSON gelesen. Übungen ohne `g` (10, gesperrt) nur auf Lösung geprüft.

Nebenwirkung (Fakt, erst beim letzten Thema bemerkt): Das Neuerzeugen hat `klasse` von `{"rs_by": 7}` auf `{"rs_by": 7, "ib_myp": 2}` gesetzt, wie in der Themenliste. Prüfskript: OK, 0 Gruppen „gleich gebaut hintereinander“. Zufallsfolge des Generators beibehalten: Außer den genannten Aufgaben hat sich keine Aufgabe geändert (Vergleich alt/neu).

## 2026-11-20 – abbildungen.determinanten2 (RS 7): mit Korrekturen in Ordnung

**Gelesen und nachgerechnet (Fakt):** 6 Lernkarten (Einstieg, Wörter, Bild, Schritte, Fehler, Regel) und alle 240 Aufgaben (168 Übungen, 12 Knobel, 6 Test, 18 Korrektur, 36 Sicherung). 122 Zahl-Aufgaben mit eigenem Skript aus dem Fragetext nachgerechnet (Determinante, Parallelogramm, Dreieck, Viereck, Vieleck per Gauß-Formel, Maßstab) – 0 Abweichungen. Alle übrigen (Auswahl, Lücken, Parameter, Knobel) von Hand nachgerechnet; zusätzlich geprüft, dass in den Karten parallelogramm/dreieck/viereck/vieleck jede Eckenfolge gegen den Uhrzeigersinn läuft (Betrag wird erst in „umlaufsinn“ erklärt) – stimmt überall. Beispielrechnungen aller 6 Lernkarten stimmen.

**Änderungen je Fehlerart:** a) 0 · b) 2 · c) 1 · d) 0 · e) 0 · f) 0

- c) `det_berechnen`, Stufe 3, parameter: „Für welche Zahlen t hat die Determinante der Vektoren a = (t | 2) und b = (8 | t) den Wert 0?“ verlangte t² = 16 mit Lösungen ±4, also eine reinquadratische Gleichung (RS 9, `gleichungen.reinquadratisch`). Ersetzt durch „… a = (t | 2) und b = (8 | 4) …“ → 4t − 16 = 0, t = 4 (Typ und Stufe gleich). Die Knobel-Karte mit n² = 49 bleibt: n ist natürlich, gesucht ist eine Quadratzahl aus Klasse 5.
- b) Knobel `umlaufsinn`: „C hat ganzzahlige Koordinaten mit −3 ≤ x ≤ 3 …“ – x und y waren nicht an C gebunden. Jetzt „C(x | y) hat …“.
- b) Knobel `umlaufsinn`: „Wie klein kann der Flächeninhalt … höchstens werden“ (dieselbe verwirrende Wendung wie in stufen-kl5 gemeldet). Jetzt „Welchen kleinsten Flächeninhalt kann das Dreieck ABC haben, wenn es ein echtes Dreieck sein soll (Fläche nicht 0)?“

Keine Änderung der Art a) – keine falsche Lösung gefunden.

**Lehrplan:** Passt zu RS 7, Wahlpflichtfächergruppe I (Flächen von Dreiecken, Vierecken und Vielecken mit zweireihigen Determinanten, `lehrplan_andere`); Beleg aus Websuche: ISB-Jahrgangsstufentest 8 I 2022 fragt die Dreiecksfläche mit Determinante aus AB und AC als Vorwissen ab (isb.bayern.de, Abruf 20.11.2026). Nichts Wesentliches fehlt. Annahme (nicht gegen lehrplanplus.bayern.de geprüft): In Bayern kommen Vektoren in RS 7 vor den Determinanten; in `themenliste.json` steht `abbildungen.vektoren` dahinter. Das Thema erklärt „Vektor“ und „Spitze minus Fuß“ selbst, setzt also nichts voraus – nur zur Kenntnis für die Reihenfolge.

**Nicht geprüft / Grenzen:** Zeichnungen nur über die Koordinaten im JSON geprüft, nicht in der App angesehen. Knobel-Karten mit |x + 1| = 5 und „Ausmultiplizieren“ (Determinante von a + b und a − b) sind anspruchsvoll, aber als freiwillige Knobel-Karten mit Beispiel im Lösungsweg vertretbar (Meinung).

Prüfskript: OK, 0 Gruppen „gleich gebaut hintereinander“.
