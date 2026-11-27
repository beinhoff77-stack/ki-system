# Auswertung Prüfungsmaterial Mathematik Realschule Bayern, Klasse 7 und 8

Stand 22.11.2026 · Grundlage: `katalog.json` (125 Arbeiten, 1389 Einzelaufgaben + 68 Zeilen nur auf Themenebene; Nachtrag am selben Tag: Ziel auf 50 erhöht) · Kennzahlen mit `_bauen.py` reproduzierbar.
Gezählt wird nach **Stoff-Klasse**. Die Prozentwerte unten beziehen sich nur auf Arbeiten **nach LehrplanPLUS mit Einzelaufgaben**. Arbeiten nach altem Lehrplan oder mit unklarem Lehrplanstand stehen im Katalog, fließen hier aber nicht ein.

Kennzeichnung: **[G]** gesichert (steht so in der Quelle oder ist ausgezählt) · **[A]** Annahme/eigene Einschätzung · **[O]** offen.

## 0 Bestand und Zielerreichung (Ziel: ≥ 50 Arbeiten je Klasse)

| Stoff-Klasse | Gruppe I | Gruppe II/III | Gruppe unbekannt | Summe | davon mit Einzelaufgaben | davon Bayern sicher/wahrscheinlich | davon LehrplanPLUS mit Einzelaufgaben |
|---|---|---|---|---|---|---|---|
| 7 | 16 | 14 | 20 | **50** | 49 | 40 | 15 |
| 8 | 26 | 23 | 24 | **73** | 44 | 51 | 11 |

Zusätzlich gibt es 2 Grundwissentests 7 (geschrieben in Klasse 7, Stoff 5/6).

- [G] **Ziel von 50 erreicht:** Stoff 7 hat 50 Arbeiten, Stoff 8 hat 73. Die Qualität ist aber gemischt:
  - In Klasse 8 sind 29 Arbeiten Verlags-Schulaufgaben, die nur auf Themenebene erfasst sind.
  - 10 Arbeiten in Klasse 7 und 22 in Klasse 8 stammen von klassenarbeiten.de, ohne Angabe des Bundeslands. Bezeichnungen wie „Klassenarbeit“, „Test“ oder „mündliche Note“ sprechen eher gegen Bayern. Gezählt sind sie trotzdem, weil Realschul-Stoff und Themen passen.
  - Rechnet man nur Arbeiten, die sicher oder wahrscheinlich aus Bayern stammen, sind es 40 (Klasse 7) bzw. 51 (Klasse 8).
- [G] **Nachtrag (Quellen):**
  - 18 weitere Arbeiten für Klasse 7 und 21 für Klasse 8 von den Übersichtsseiten von klassenarbeiten.de, im Browser durchgesehen.
  - Ältere ISB-Tests: Jahrgangsstufentest 8 von 2007 I und II/III, 2009 II/III, 2011 II/III, 2016 I und 2017 I; Grundwissentest 9 von 2017 und 2018, jeweils I und II/III.
  - Diese Tests folgen dem alten Lehrplan und sind so gekennzeichnet. Die Prozentangaben unten (nur LehrplanPLUS) ändern sich dadurch nicht.
- [G] Den Kern bilden die amtlichen ISB-Tests:
  - Der Jahrgangsstufentest 8 prüft den Stoff von Klasse 7, der Grundwissentest 9 den Stoff von Klasse 8.
  - Echte Schulaufgaben mit Einzelaufgaben gibt es jetzt 10. Davon sind 3 ausdrücklich „Realschule Bayern“ (KA-3560, KA-3564, KA-4010). Alle stammen von klassenarbeiten.de, keine von einer Schul-Homepage.
- [A] **Klassenarbeiten von klassenarbeiten.de:**
  - Die 316 Aufgaben ohne Gruppenangabe sind zu 51 % reine Rechenaufgaben.
  - Zeichnen/Konstruieren macht nur 6 %, Begründen nur 4 % aus.
  - Lehrergemachte Arbeiten sind also deutlich rechenlastiger als die ISB-Tests. Für unsere App heißt das: Rechentechnik bleibt der größte Block einer echten Schulaufgabe.
- [G] **Lücken:**
  - Keine einzige frei zugängliche Schulaufgabe oder Stegreifaufgabe einer Realschul-Homepage nach LehrplanPLUS gefunden.
  - Keine ISB-Leistungsaufgaben für 7 II/III und 8 II/III.
  - Keine Verlagsprobe mit Einzelaufgaben für 7 II/III.
- [G] **Verteilung über das Schuljahr:** Die ISB-Tests liegen alle am Schuljahresanfang. Die Arbeiten von klassenarbeiten.de verteilen sich über September bis Juli. Schulaufgaben sind belegt für:
  - November/Dezember: KA-3556, KA-3560, KA-3548, KA-3550, 7 I SA1
  - Januar/Februar: KA-3563, KA-3546, KA-4010
  - Juni: 3. Schulaufgabe KA-3564; 8 I SA7
  - In Klasse 7 mischen Schulaufgaben 3–6 Themen. Ein Beispiel ist die 3. Schulaufgabe im Juni mit Ungleichungen, Dreisatz, Prozent, Zinsen und Kreis.

## 1 Typischer Aufbau

| | 7 I | 7 II/III | 8 I | 8 II/III |
|---|---|---|---|---|
| Schulaufgaben im Jahr | 4 [G, Bauer] | 4 [G, Bauer] | 4 [G, Verlag] | 3 [G, Stark] |
| Stegreifaufgaben im Jahr | 7 [G, Bauer] | 6 [G, Bauer] | ? [O] | ? [O] |
| Schulaufgabe: Zeit / Punkte | 45 min / 32 P. [G, 1 Beleg] | ? [O] | 45 min / 29 P. [G, 1 Beleg]; 40 P. (2012, alt) | ? [O] |
| Schulaufgabe: Aufgaben | 6 Haupt-, 9 Teilaufgaben, 5–6 Themen [G] | 5 Haupt-, 10 Teilaufgaben, 5 Themen [G, KA-3548] | 7 Haupt-, 11 Teilaufgaben, 5 Themen [G] | 3–4 Themen je Schulaufgabe [G, Stark-Inhaltsverzeichnis] |
| Stegreifaufgabe | 18 min, 1 Thema [G, Stark] | ? [O] | 1 Thema [G, Verlag] | 1 Thema [G, Stark] |
| ISB-Test (Stoff-Jahr) | 45 min, 21 Items à 1 P. [G] | 45 min, 21 Items à 1 P. [G] | 45 min, 23 Items à 1 P. [G] | 45 min, 23 Items à 1 P. [G] |
| Niveau I/II/III (ausgezählt) | 43/47/10 % | 50/43/7 % | 33/58/9 % | 43/50/7 % |

- [A] Niveau ist eigene Einschätzung je Aufgabe. Die Tendenz: Gruppe I liegt höher (mehr II/III), und Klasse 8 liegt höher als Klasse 7.
- [G] Eine Schulaufgabe mischt fast immer **3–6 Themen**: einen neuen Block (2–3 Themen) plus Wiederholung oder Grundwissen. Das zeigen alle 12 Schulaufgaben mit Einzelaufgaben (10 von klassenarbeiten.de, 2 aus Verlagsleseproben) mit 4–11 Hauptaufgaben, dazu die Inhaltsverzeichnisse der Verlage. Ihre Themen fasst `katalog.md` zusammen. Punkte und Zeit stehen bei klassenarbeiten.de meist nicht dabei.

## 2 Häufigkeit je Thema / Etappe (LehrplanPLUS, Einzelaufgaben)

**Anteil an allen Aufgaben, Top-Themen [G, ausgezählt; Zuordnung A]:**
- **7 I:**
  - geometrie.konstruktion 10 %, raum.schraegbilder 10 %, abbildungen.kongruenz 8 %, geometrie.winkelsaetze 6 %, geometrie.kreis 5 %
  - Gleichungen und Ungleichungen je 5 %, Potenzen 9 %
  - In 7 von 8 Arbeiten kommen vor: Winkelsätze, Schrägbilder, Kreis, Konstruktion, Kongruenz/Vektoren.
- **7 II/III:**
  - geometrie.winkelsaetze 11 %, gleichungen.linear 8 %, gleichungen.ungleichungen 8 %, abbildungen.kongruenz 8 %, geometrie.kreis 7 %
  - groessen.indirekt und finanzen.zinsen in 6 bzw. 5 von 7 Arbeiten.
- **8 I:**
  - abbildungen.kongruenz (Vierecke, Drehung) 13 %, funktionen.linear 13 %, terme.umformen 9 %
  - geometrie.konstruktion, terme.quadratische_extreme und gleichungen.bruch je 6 %
- **8 II/III:**
  - terme.umformen 12 %, geometrie.konstruktion 9 %, funktionen.linear 8 %
  - gleichungen.linear und geometrie.winkelsaetze je 7 %

**Häufigste Etappen (über alle Stoff-7- bzw. Stoff-8-Arbeiten mit Einzelaufgaben, alle Lehrplanstände) [G]:**
- **Stoff 7:**
  - bruch.rechnen·gemischt (30, Grundwissen), abbildungen.kongruenz·vektor_koordinaten (30)
  - terme.potenzgesetze·potenz_begriff (24)
  - bruch.prozent_grundwert·zurueck (17)
  - gleichungen.linear·beide_seiten, geometrie.winkelsaetze·figuren (je 15)
  - gleichungen.ungleichungen·sachaufgabe, gleichungen.linear·sach (je 14)
  - geometrie.konstruktion·kongruenzsatz, geometrie.kreis·umkreis_inkreis (je 12)
- **Stoff 8:**
  - terme.umformen·binomisch (38, vor allem durch die Klassenarbeiten), ·ausklammern (21), ·ausmultiplizieren (15)
  - terme.quadratische_extreme·extremwert, gleichungen.linear·klammern (je 24)
  - geometrie.winkelsaetze·figuren (20)
  - geometrie.konstruktion·vierecke_konstruieren (19)
  - gleichungen.linear·sach (18)
  - gleichungen.bruch·ueber_kreuz (16), funktionen.linear·lage (15)
  - terme.bruchterme·definitionsmenge (13)

**Grundwissen früherer Klassen:** [G] 7–12 % der Aufgaben, vor allem Bruchrechnen, Prozent und Einheiten.

**Etappen-Lücken (Prüfungsinhalt ohne passende Etappe), jeweils mit Vorschlag [A]:**

| Vorkommen | Inhalt | Vorschlag |
|---|---|---|
| 13× | Mittelpunkt einer Strecke berechnen, auch rückwärts | Etappe in `abbildungen.kongruenz` nach `vektor_koordinaten` |
| 6× | Seiten-Winkel-Beziehung im Dreieck (größerer Seite liegt größerer Winkel gegenüber) | Etappe in `geometrie.konstruktion` |
| 4× | Verschiebungen verketten / Vektoren addieren | Etappe in `abbildungen.kongruenz` |
| 3× | Graph eines quadratischen Terms skizzieren (eine Arbeit, Lehrplanstand unklar) | Etappe in `terme.quadratische_extreme` |
| 3× | Teilbarkeit / gerade-ungerade begründen | Grundwissen Klasse 5, z. B. in `zahlen.natuerlich` |
| 2× | Würfelnetz / Würfel kippen / Würfelbau | Grundwissen Klasse 5, Thema `messen.koerper_darstellung` |

## 3 Aufgabentypen, die bei uns fehlen oder selten sind

[G] Unsere Aufgaben in den 26 RS-7/8-Themen haben folgende Antwortformen: zahl 3837, auswahl 2326, luecken 755, markierung 1. Zeichnen, Konstruieren und freies Begründen gibt es nicht.

| Typ in Prüfungen (Anteil an LehrplanPLUS-Aufgaben) | 7 I | 7 II/III | 8 I | 8 II/III | bei uns |
|---|---|---|---|---|---|
| zeichnen / konstruieren (Geodreieck, Zirkel, Koordinatensystem, Schrägbild) | 18 % | 13 % | 9 % | 13 % | **fehlt** |
| begründen / Aussage prüfen mit Begründung | 13 % | 6 % | 6 % | 4 % | nur als Auswahl („stimmt/stimmt nicht“), ohne Begründung |
| Fehler finden und berichtigen | 3 % | 2 % | 7 % | 4 % | vereinzelt (z. B. `terme.potenzgesetze·fehler_finden`) |
| Lücke ergänzen / rückwärts | 19 % | 19 % | 16 % | 18 % | vorhanden (luecken) |
| ankreuzen / zuordnen | 15 % | 14 % | 15 % | 17 % | vorhanden (auswahl) |
| Sachaufgabe mit Lösungsweg | 8 % | 11 % | 13 % | 12 % | nur Endergebnis wird geprüft |

- [A] Ebenfalls selten oder fehlend:
  - Term aus Figur oder Text aufstellen (in Prüfungen 7–13 Fälle je Klasse)
  - offene Aufgaben („Gib ein Beispiel an …“)
  - Mehrschritt-Aufgaben, bei denen Teil b auf dem Ergebnis von Teil a aufbaut
  - Aufgaben, die zwei Themen verbinden (z. B. Winkel in einer Figur, gelöst über eine Gleichung)
- [A] **Konstruktionen** können wir ohne Zeichenwerkzeug nur indirekt prüfen: Lösungsschritte ordnen, Planfigur auswählen, Punkt-Koordinaten des Ergebnisses eingeben.

## 4 Etappen, die in Prüfungen nie vorkommen

[G] Gemeint sind Etappen der Lehrplan-Themen, für die es im ganzen Katalog keine einzige Einzelaufgabe gibt (Grundlage: 95 Arbeiten mit Einzelaufgaben, Stand nach dem Nachtrag).

- **Stoff 7 (beide Gruppen):**
  - abbildungen.determinanten2·umlaufsinn, ·vieleck
  - abbildungen.kongruenz·punktspiegelung
  - bruch.prozent_grundwert·faktor, ·formel
  - daten.boxplot·mittel_median, ·quartile, ·boxplot, ·vergleichen (nur der Median kommt einmal vor, in einer Arbeit ohne Bundeslandangabe)
  - daten.darstellen·absolute_haeufigkeit
  - daten.stichproben·begriffe, ·fehlerquellen
  - finanzen.zinsen·begriffe, ·rollen, ·jahreszinsen_komma
  - geometrie.kreis·beweis, ·lage
  - geometrie.ortslinien·sachsituationen
  - geometrie.winkelsaetze·aussenwinkel, ·parkett
  - gleichungen.ungleichungen·grafisch
  - groessen.indirekt·erkennen
  - nur 7 I: geometrie.konstruktion·satz_kehrsatz, raum.schraegbilder·koordinaten
- **Stoff 8 (beide Gruppen):**
  - abbildungen.kongruenz·punktspiegelung
  - funktionen.linear·schnittpunkte, ·bueschel
  - geometrie.konstruktion·satz_kehrsatz
  - gleichungen.bruch·verhaeltnis, ·graphisch
  - raum.schraegbilder·koordinaten
  - stochastik.grundbegriffe·begriffe, ·gegenereignis
  - terme.bruchterme·termwert, ·erweitern, ·multiplizieren, ·fehler_finden
  - terme.quadratische_extreme·mit_faktor, ·optimierung

Einordnung:
- [A] **Kein Streichkandidat.** „Nie“ heißt nur: nicht in den ISB-Tests und den wenigen Schulaufgaben. Viele dieser Etappen sind Zwischenschritte (Begriffe, Rechentechnik), die in Prüfungen nur eingebettet vorkommen. Ein Beispiel ist Bruchterme kürzen/addieren: das steckt in den Bruchgleichungen.
- [A] Echte **Kandidaten für Abwertung** (nur Übung, kein eigener Testpunkt): Parkettierung, Determinante·Umlaufsinn, Geradenbüschel, Begriffs-Etappen bei Zinsen.
- [G] Durch den Nachtrag kommen jetzt vor: Prozent vermehrt/vermindert, Monats- und Tageszinsen, Ungleichungen umformen/mit Klammern, Vervielfachen bei umgekehrter Proportionalität, Bruchterme kürzen/addieren und Einsetzen bei linearen Funktionen. Die Lücken lagen also am Material, nicht an der Bedeutung der Etappen.
- [O] Boxplot und Quartile fehlen weiter. Klären lässt sich das nur mit echten LehrplanPLUS-Schulaufgaben.

## 5 Abgleich mit unserem Flug-Test

[G] Unser Flug-Test hat je Etappe eine Testaufgabe (26 Themen, 1 bis 12 Testaufgaben je Thema), immer innerhalb eines Themas, Antwortformen nur zahl/auswahl/luecken.

[A] **Als Prüfungsvorbereitung reicht das nicht:**
1. **Mischung fehlt.** Schulaufgaben verbinden 4–6 Themen in 45 Minuten. Der Flug-Test prüft jedes Thema für sich. Das Umschalten zwischen Themen und das Erkennen des Aufgabentyps ohne Themenüberschrift wird nicht geübt.
2. **Zeit und Umfang fehlen.** Eine Prüfung hat etwa 21–32 Teilaufgaben in 45 Minuten. Unser Test ist ungetaktet.
3. **Konstruktion und Begründung fehlen.** Das sind 20–30 % der Punkte in 7 I und 10–20 % in den anderen Gruppen.
4. **Grundwissen fehlt.** 7–12 % der Prüfungsaufgaben kommen aus früheren Klassen, im Flug-Test sind es 0 %.
5. **Mehrschritt-Sachaufgaben** bewerten wir nur nach dem Endergebnis, ohne Teilpunkte für den Lösungsweg.

[G] Gut abgedeckt ist dagegen die Rechentechnik (Niveau I) und das Rückwärtsrechnen mit Lücken. Das sind etwa 40–50 % der Prüfungsaufgaben.

## 6 Vorschlag „Schulaufgaben-Training“ (nur Vorschlag, nichts gebaut)

[Meinung/Vorschlag]
1. **Probe-Schulaufgabe je Schulaufgaben-Block.** 45 Minuten mit Zeitanzeige, etwa 25–30 Punkte, Themenmix nach dem Stoffverteilungsplan der Gruppe (Belege aus Abschnitt 1 und der Spalte „Themen zusammen“ in katalog.md). Verteilung: 40 % Niveau I, 50 % II, 10 % III. Davon 10 % Grundwissen.
2. **Aufgaben aus vorhandenen Pools ziehen** (sicherung/test), aber gemischt und ohne Themen- oder Etappen-Überschrift. Teilpunkte je Teilaufgabe.
3. **Neue Antwortformen in kleinen Schritten**, in dieser Reihenfolge:
   - Begründung als Auswahl aus 3 Begründungen (geht sofort)
   - Konstruktionsschritte in die richtige Reihenfolge bringen
   - Punkt im Koordinatensystem setzen (prüfbar über Koordinaten)
   - Fehler markieren (markierung gibt es schon)
4. **Die drei häufigsten Etappen-Lücken zuerst schließen:** Mittelpunkt einer Strecke, Vektoraddition, Seiten-Winkel-Beziehung.
5. **Auswertung „wie in der Schule“:** Punkte und daraus eine Note nach dem üblichen Notenschlüssel. [O] Welcher Schlüssel genau? Das ist Schulsache, der Nutzer entscheidet.

## Offene Punkte

- [O] Echte LehrplanPLUS-Schulaufgaben von Schulen für die Gruppe II/III und für die Klassenmitte. Möglicher Weg: Eltern oder eine Schule fragen, oder ein Verlagsheft kaufen (Stark 7 II/III, 8 II/III). Das ist nicht frei zugänglich und darf nur als Katalog erfasst werden.
- [O] Zahl der Stegreifaufgaben in Klasse 8 und die Gewichtung von Schulaufgabe zu Stegreifaufgabe. Das regelt jede Schule selbst, die Grundlage ist die RSO.
- [O] Lehrplanstand der klassenarbeiten.de-Arbeiten (keine Jahresangabe).
