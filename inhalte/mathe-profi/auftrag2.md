# Mathe-Profi – Auftrag 2 (25.11.2026)

Ausgangsstand: Zweig `mathe-profi`, zusammengeführt mit `lernen-app` 4351182. Geprüft wurden die Dateien des Vorgängers (`auftrag1.md`, `ideen.md`, `nachrechnen.py`, `entwurf-formen.html`), die Inhaltsdateien `inhalte/themen/*.json`, `lernen.js` und `schule.antwort_bewerten` (Migration 20261116). **Nicht** gelesen: die Datenbank (Stand der Aufgaben, Versuche der Kinder).

Kennzeichnung: **[G]** gesichert (nachgezählt, nachgerechnet oder im Code gelesen) · **[A]** Annahme · **[M]** Meinung.

| Datei | Inhalt |
|---|---|
| `auftrag2.md` | dieser Bericht |
| `nachrechnen2.py` | Referenz der Prüfregel, 20 Musteraufgaben zweifach nachgerechnet, Nachweise zu den Befunden. Lauf: `python3 -I inhalte/mathe-profi/nachrechnen2.py` → „OK“. Schreibt die Aufgabenliste in diesen Bericht, die Daten in den Entwurf und `aufgaben-auftrag2.json`. |
| `aufgaben-auftrag2.json` | die 20 Datensätze (mit Rechenwegen und typischen Fehlern) |
| `entwurf-punkte.html` | Entwurf zum Anklicken für Platz 1, alle 20 Aufgaben, ohne Netz |

## Kurzfassung

1. **Die Arbeit des Vorgängers trägt in der Richtung, aber nicht ungeprüft.** Zahlen stimmen bis auf zwei. Sein Hauptbefund („geschickt rechnen wird nie geprüft“) ist überzogen: 28 von 105 Übungen fragen den Weg schon ab. Drei der zwölf Aufgaben sind so nicht brauchbar (zwei wiederholen das Beispiel der Erklärung, eine hat zwei vertretbare Antworten). Eine Prüfregel ist falsch (Toleranz 0,25 nimmt falsche Punkte an), eine Erklärung enthält eine Formel, die bei negativem Schnittpunkt das falsche Vorzeichen liefert.
2. **Vieles, wofür er neue Formen wollte, geht heute schon** – als Inhalt, ohne Bau: Weg abfragen (`auswahl`, `luecken`), Fehlerzeile finden (`tabelle` + `auswahl`), Überschlag am Zahlenstrahl (`markierung`), frei überschlagen (`zahl` mit `toleranz`).
3. **Gebaut werden soll zuerst, was heute gar nicht geht: Gitterpunkte setzen** (`punkte`). Danach Mehrfach-Antippen, danach „falsche Antwort als Bild“. Dieser Bericht enthält dafür die bau-fertige Vorgabe und 20 Musteraufgaben.

---

## 1. Auftrag 1 neu geprüft

### 1.1 Nachgezählt

| Aussage des Vorgängers | Mein Ergebnis | |
|---|---|---|
| Rom 548 Aufgaben, 379 Übungen, 14 Etappen, 0 mit Bild | stimmt | [G] |
| Lineare Funktionen 445 Aufgaben, 293 Übungen, 35 mit Bild | stimmt | [G] |
| 82 Aufgaben mit „geschickt“, davon 79 als `zahl` | stimmt | [G] |
| „Geschickt rechnen wird **nie** geprüft, nur das Ergebnis“ | **stimmt so nicht.** In den vier Etappen `vorteil`, `differenz_summe`, `verteilen`, `kopfrechnen` sind 28 von 105 Übungen keine Zahl-Aufgaben; sie fragen den Weg ab („Welche zwei Zahlen fasst du zuerst zusammen?“, „Welche Rechnung ist ein geschickter Weg für 19 · 25?“, „Was ist falsch?“). Richtig ist: 73 % prüfen nur das Ergebnis, und „gelandet“ geht ohne eine einzige Weg-Aufgabe. | [G] |
| `ueberschlag`: 19 von 39 schreiben die Rundung vor | 24 von 39 (14 von 27 Übungen). Befund wird dadurch stärker. | [G] |
| `lage`: 19 von 46 mit demselben Vierer | stimmt | [G] |
| Antwortformen: zahl, auswahl, luecken, markierung, text | stimmt (`lernAufgabe`, `antwort_bewerten`) | [G] |
| Entwurf: „≈ 28 px je Kästchen bei 12 Kästchen auf 360 px“ | **falsch.** Das Bild hat 340 Einheiten Breite und 38 Rand je Seite (`lernKoordinaten`), bleiben 264. Bei 12 Kästchen sind das 22 Einheiten, auf dem Handy etwa 19–21 px. | [G] |
| `nachrechnen.py` läuft „OK“ | stimmt; die Rechnungen sind richtig. Das Skript prüft aber nur die Rechnung, nicht ob die Frage eindeutig ist (siehe R1). | [G] |

Zusätzlich gezählt [G]: 1 093 Zahl-Aufgaben nutzen schon `toleranz`, 116 Aufgaben `markierung`. `auswahl` mit 4 Antworten und zweitem Versuch hat eine Rate-Chance von 1/4 + 3/4 · 1/3 = **1/2** (zählt dann nicht für die Folge, kostet aber auch nichts).

### 1.2 Die beiden Flug-Bewertungen

**Klasse 5, Rechengesetze – Urteil des Vorgängers: im Kern richtig, Punkt 1 zu hart, Abhilfe falsch zugeordnet.**

- Punkt 1 (Weg nicht geprüft): Richtung stimmt, „nie“ nicht (siehe oben). Wichtiger: Die Abhilfe braucht **keine neue Aufgabenform**. Seine Aufgabe R1 (Paar antippen) ist dasselbe wie die vorhandene Auswahl-Aufgabe „Welche zwei Zahlen fasst du zuerst zusammen?“. Was fehlt, ist Menge und Regel: mehr solcher Karten und „gelandet erst mit einer Weg-Aufgabe“. [G]/[M]
- Punkt 2 (kein Bild): stimmt [G]. Aber ein Bild hilft hier nur beim Verteilen (Rechteck) und beim Überschlag (Zahlenstrahl). Termbaum zum Ablesen ist Deko, wenn der Term daneben steht. [M]
- Punkt 3 (Überschlag als Regel): stimmt [G]. Geht **heute** besser: „Welcher Strich liegt am nächsten an 487 · 21?“ als `markierung` (eindeutig: Strich 5, Abstand 227 bei 2 000 Strichabstand) und freier Überschlag als `zahl` mit `toleranz`. [G]
- Punkt 4 (Gleichbau) und 5 (Fehler nur als Text): stimmen [G].
- **Fehlt in der Bewertung:** (a) kein Blick auf den Flug-Test (14 Testaufgaben, eine je Etappe – ob die den Weg prüfen, hat er nicht angesehen; ich auch nur gezählt). (b) Kein Wort zur Rate-Chance bei `auswahl` (132 Aufgaben im Flug). (c) Keine Versuchsdaten – alle „häufigsten Fehler“ sind Annahmen.

**Klasse 8, Lineare Funktionen – Urteil des Vorgängers: stimmt, das ist der stärkere Befund.**

- Punkt 1 (Kind zeichnet nie): stimmt [G], die Datei sagt es selbst unter `offen`. Das ist der einzige Befund, den Inhalt allein nicht beheben kann.
- Punkt 2 (Lage-Vierer): stimmt [G]. Abhilfe „Zuordnung“ ist teuer; billiger: Parallele und Senkrechte **zeichnen** lassen (G5, G7 unten).
- Punkt 3 (wenig Bild): stimmt [G].
- Punkt 4 (Schieber versprochen): stimmt als Beobachtung [G]; die Etappe ist Vertiefung, also nachrangig. Ein Schieber, bei dem das Kind so lange klickt, bis die Gerade durch P geht, wird fast immer richtig gelöst und sagt wenig darüber, ob es rechnen kann. [M]
- Punkt 5 (fauler Weg beim Aufstellen): stimmt, B3 ist die beste der vier Erklärungen.

### 1.3 Die 4 Erklärungen

| | Urteil | Was ich ändere |
|---|---|---|
| B1 Überschlag „gegensinnig runden“ | **überarbeiten** | Das Beispiel 487 · 21 → 500 · 20 zeigt die Regel nicht: Das ist gewöhnliches Runden. Auch 48 · 52 → 50 · 50 ist gewöhnliches Runden, der „typische Fehler“ 40 · 50 ist konstruiert. Die Regel braucht ein Beispiel, bei dem gewöhnliches Runden schlecht ist: 45 · 65 (genau 2 925; beide auf: 50 · 70 = 3 500; gegensinnig: 50 · 60 = 3 000). Der Rest der Erklärung steht schon in der vorhandenen Lernkarte (dasselbe Kino-Beispiel). Also: ein zusätzlicher Schritt, keine neue Erklärung. [G] |
| B2 Verteilen am Rechteck | **behalten, Zahlen ändern** | Idee gut (Streifen über alle Reihen). Aber bei 7 · 98 ist der Streifen 2 % der Breite, auf dem Handy etwa 5 px – man sieht ihn nicht. Bild mit 6 · 18 = 6 · 20 − 6 · 2 (Streifen 10 %). Gegenbeispiel „2 · 98 ist nicht 198“ ist gut. [G]/[M] |
| B3 Zurück zur y-Achse | **behalten** | Richtig, kurz, echter fauler Weg (t = y − m · x), gleiche Zahlen wie die vorhandene Lernkarte. Wird in G4, G9, G10 unten geübt. |
| B4 Vorsprung : Aufholen | **Schritt 6 streichen oder genau fassen** | „x = (Unterschied der t) : (Unterschied der m)“ ohne Reihenfolge ist ein Trick ohne Verständnis: y = 2x + 3 und y = x + 1 schneiden sich bei x = −2, die Regel liefert 2 [G, im Skript]. Entweder nur für Sachaufgaben mit x > 0 lassen und so sagen, oder mit Reihenfolge schreiben: x = (t₂ − t₁) : (m₁ − m₂). Schritte 1–5 sind gut. |

### 1.4 Die 12 Aufgaben

| | Urteil | Grund |
|---|---|---|
| R1 Paar antippen | **ändern** | Zwei vertretbare Antworten: Wer zuerst 17 · 3 = 51 rechnet und dann 51 · 100, rechnet genauso geschickt. Frage muss lauten: „Welche zwei Faktoren ergeben zusammen eine glatte Zahl?“ Und: geht als `auswahl` schon heute. [G] |
| R2 Ausklammern mit Lücken | behalten | sauber, geht heute |
| R3 Klammer setzen | behalten, Stufe 2 | vier Terme ausrechnen ist `mehrschritt`, nicht `parameter` [M] |
| R4 Überschlag am Schieber | **streichen/ersetzen** | (1) 487 · 21 ist das Beispiel der Lernkarte, dort steht 10 000 und 10 227 wörtlich. (2) Die Lösung liegt genau in der Skalenmitte – wer ohne Nachdenken die Mitte tippt, hat recht. (3) Der Bereich 8 000–12 000 ist ein Fünftel der Skala, ohne Regel dahinter. [G] |
| R5 Rückwärts-Bausteine | behalten als Brücke | er sagt selbst: wenig eigenes Denken. Nur Stufe 1–2. |
| R6 Fehlerzeile | **behalten, als Muster nehmen** | geht heute, prüft genau das Richtige |
| L1 Gerade zeichnen | behalten, Regel ändern | Toleranz 0,25 muss weg (siehe 2.2) |
| L2 Parameter-Schieber | warten | siehe 1.2, Punkt 4 |
| L3 Steigung aus Tabelle | behalten | geht heute |
| L4 Tarife | **Zahlen ändern** | wörtlich das Beispiel aus B4 (8 €/0,10 € gegen 2 €/0,25 €) – als „schwer/transfer“ nicht haltbar, wenn die Erklärung es vorrechnet [G] |
| L5 Zuordnung Lage | warten | alles-oder-nichts bei 5 Paaren; „3 von 5 stimmen“ plus zweiter Versuch verrät viel |
| L6 t so, dass durch S | behalten | sauber |

Unterm Strich: 7 behalten (R2, R3, R5, R6, L1, L3, L6), 2 mit neuen Zahlen (R1-Frage, L4), 3 zurückstellen oder streichen (R4, L2, L5).

---

## 2. Die 5 Formen und die 22 Ideen

### 2.1 Lernen je Aufwand (Rangfolge, [M] mit Begründung)

Maßstab: Wie viel **eigenes Denken, das heute nicht verlangt wird**, bringt die Idee – geteilt durch Bau- und Pflegeaufwand. Was heute schon mit vorhandenen Formen geht, steht ganz oben, weil der Aufwand nur Inhalt ist.

| Rang | Idee | Warum hier |
|---|---|---|
| 0 | **A5 Korrigiere das Heft, A6 Faulster Weg, A7 Steckbrief, A4 Muster, Lücken im Weg (wie R2), Überschlag an `markierung`/`zahl` mit `toleranz`** | Geht heute. Kein Bau. Größter Hebel für Klasse 5 „geschickt“. Auftrag an den Aufgaben-Ersteller, ich liefere Muster und prüfe Stichproben. |
| 1 | **F3 Punkte setzen** | Einzige Kernhandlung, die heute nicht geht (zeichnen). Dient beiden Kindern: Klasse 5 Koordinaten, Strecken, Parallele, Lot, Vierecke; Klasse 8 Geraden, Schnittpunkte. Rate-Chance 1 von 121. Der Fehler wird von selbst sichtbar (eigene Gerade neben der richtigen). Aufwand mittel. |
| 2 | **F1 Felder antippen – aber als Mehrfach-Auswahl** | Ein einzelnes Feld antippen ist nur `auswahl` in anderem Kleid. Der Gewinn ist „Tippe **alle** an, die …“: Rate-Chance von 1/2 auf 1/64 bei 6 Feldern, und jedes Feld muss geprüft werden. Aufwand klein. |
| 3 | **R1 Fehler sichtbar machen – nur der Teil ohne Inhaltsarbeit** | Nach Platz 1 kann die App Geraden und Punkte über ein Bild legen. Dann für jede vorhandene Lücken-Aufgabe „□x + □“ die Gerade des Kindes neben die richtige zeichnen (im Flug Lineare Funktionen 93 Lücken-Aufgaben) und bei Zahlenstrahl-Aufgaben den Wert des Kindes eintragen. Keine neuen Aufgaben nötig. Der volle R1 („je Thema eine Zeichen-Regel“) ist groß, nicht mittel. |
| 4 | F7 Wertetabelle, Graph wächst mit | billig nach Platz 1, stark für Klasse 8; nichts für Klasse 5 |
| 5 | A8 Erst schätzen, dann rechnen · A5 als Zweiteiler | braucht verkettete Karten (zwei Antworten, eine Karte). Das gibt es bisher nur in den Expeditionen [A, nicht geprüft]. Aufwand unbekannt → Frage an den Projektleiter. |
| 6 | A3 Gegenbeispiel | gut für „Begründen“; braucht je Aufgabe eine Bedingung auf dem Server. Mit Platz 2 teils ersetzbar („Tippe alle Gegenbeispiele an“). |
| 7 | F4 Zuordnung | Lerngewinn mittel, Bewertung unklar (2.2) |
| 8 | F2 Schieber | Schätzen geht heute an `markierung`; der Parameter-Schieber ist hübsch, prüft aber wenig |
| 9 | R3 Eigene Fehler kommen zurück | nur für Fehler mit erkanntem Muster (Vorzeichen, Komma, vertauscht) billig; sonst drei Erklärungen je Aufgabe zu schreiben |
| 10 | A1 Mach 100, A2 Aufgabe erfinden, M2 Knobel | machen Spaß, brauchen einen Term-Rechner auf dem Server; A2-Regel ist lückenhaft (2.2) |
| 11 | R2 Tipp-Treppe, F5 Reihenfolge, F6 Bereich | wenig Denken je Aufwand bzw. Regel unvollständig |
| – | R4 Sicherheits-Wette | **so nicht.** Siehe 2.2. |
| – | M1 Reise-Aufgaben, M3 Foto | Pflege bzw. nicht automatisch prüfbar |

### 2.2 Wo die Prüfregel nicht eindeutig ist [G, soweit nachgerechnet]

1. **F3/D3 `auf_gerade` mit Toleranz 0,25 – falsch.** Punkte rasten auf Gitterpunkte ein; eine Toleranz auf den gespeicherten Wert hat dann nur einen Effekt: Bei flachen Geraden gelten falsche Punkte. y = x/4: (1 | 0) liegt 0,25 daneben und zählt als richtig (4 solche Punkte im Bereich −4…4). → Der Server vergleicht **exakt**. Die Toleranz gehört in den Finger (Einrasten), nicht in die Prüfung.
2. **F3/D3 `folge`** (A′, B′, C′ in Reihenfolge): Ist eine vertauschte Reihenfolge ein Mathe-Fehler oder ein Bedienfehler? Nicht entscheidbar. → in Version 1 nicht bauen.
3. **F1/D1:** kein Fall „keines trifft zu“ (leere Menge ist verboten), keine Aussage zum zweiten Versuch (zeigt die App, welche Felder falsch waren?), R1 mit zwei vertretbaren Antworten.
4. **F2/D2:** Der richtige Bereich ist frei gesetzt. Das Fehlermuster „Faktor 10 → komma“ prüft `v / w ∈ {10, 100, …}` und kann bei einer Schätzung nie anschlagen. Eine lineare Skala kann nur eine Richtung des Stellenfehlers zeigen (1 022 liegt im Bild, 102 270 nicht). Regel, wenn es gebaut wird: richtig = genauer Wert ± 20 %, Lösung nie in der Skalenmitte, typische Fehler müssen im Bild liegen.
5. **F4/D4:** alles-oder-nichts bei 5 Paaren macht aus vier richtigen Zuordnungen einen Fehler; mit „n von 5 stimmen“ und zweitem Versuch lässt sich die fünfte erschließen.
6. **F5/D5 `o.folgen`:** Jede vertauschbare Reihenfolge muss von Hand aufgezählt werden – vergessene richtige Reihenfolgen zählen als Fehler. Nur verwenden, wenn jeder Schritt das Ergebnis des vorigen braucht.
7. **F6 Bereich:** „Welche Zahlen runden auf 3 500?“ – 3 450 bis 3 549 gilt nur für natürliche Zahlen, sonst „bis unter 3 550“; mit dem Finger auf einer Skala nicht einstellbar. Ungleichung „x < 4“: ein Bereich ohne linkes Ende lässt sich mit `{von, bis}` nicht speichern.
8. **A1 Mach 100:** Sind Zwischenergebnisse wie 8 : 3 erlaubt? Zahlen aneinanderhängen (34)? Vorzeichen-Minus? Muss festgelegt werden, sonst rechnet der Server anders als das Kind erwartet.
9. **A2 „Gleichung mit Lösung x = 3“:** „3 erfüllt die Gleichung“ reicht nicht. x = x, 0 · x = 0 und x² = 9 werden von 3 erfüllt und sind keine richtigen Antworten. Regel müsste „genau eine Lösung“ prüfen.
10. **R4 Sicherheits-Wette „nur Bonus“:** Wer immer „sicher“ sagt, verliert nie etwas. Dann sagt die Angabe nichts. Ohne Minuspunkte geht es so: „sicher“ = kein zweiter Versuch, dafür Bonus. Dann kostet falsche Sicherheit etwas, ohne Abzug.

### 2.3 Was ganz fehlt

1. **Zweiter Versuch und Fehlermuster für die neuen Formen.** Die App hat einen festen Ablauf (1. Versuch → Hinweis mit `grund` → 2. Versuch → Lösung). Für keine der fünf Formen ist beschrieben, was beim ersten Fehler bleibt, was gezeigt wird und welche Muster der Server erkennt. Ohne das ist nichts bau-fertig.
2. **Fingergenauigkeit.** Nirgends steht, wie ein Kind einen Punkt trifft, der 20 px vom Nachbarn entfernt ist, und wie es einen Fehltipp ohne Neuanfang korrigiert.
3. **Geometrie Klasse 5.** Alle Beispiele der Formen kommen aus Rechnen und Funktionen. Das Klasse-5-Kind hat vier Geometrie-Flüge (Kairo, Timbuktu, Lima), in denen Zeichnen der Kern ist.
4. **Bruch als Antwort nach Wert.** Heute nur über zwei ganzzahlige Lücken, „gekürzt“ erzwungen, 4/6 statt 2/3 ist schlicht falsch. Eine Regel „gleichwertig, aber noch nicht gekürzt → eigener Hinweis“ wäre klein und trifft das ganze Bruchrechnen der 6. Klasse. Nicht dringend für die jetzigen Flüge. [M]
5. **Verkettete Karten** (schätzen → rechnen, Zeile finden → verbessern) als eigener Baustein.
6. **Daten.** Kein einziger Befund stützt sich auf Versuche der Kinder. Welche Etappen wirklich schwer sind und welche Fehler wirklich vorkommen, weiß bisher niemand in dieser Ablage.

---

## 3. Meine Reihenfolge

**Vorab, ohne Bau (Platz 0):** Weg-Aufgaben mit den vorhandenen Formen in die Etappen `vorteil`, `verteilen`, `kopfrechnen`, `ueberschlag`, `schriftlich_geteilt` – nach den Mustern R2, R6, A6 und „nächster Strich“. Dazu die Regel „gelandet erst, wenn mindestens eine Weg-Aufgabe richtig war“ (das wäre ein kleiner Bau am Server). Das behebt den Hauptbefund für Klasse 5 schneller als jede neue Form.

**Gebaut wird:**

1. **`punkte` – Gitterpunkte setzen.** Begründung: einzige Lücke, die Inhalt nicht schließen kann; beide Kinder; in Klasse 5 vier Flüge, in Klasse 8 Funktionen, Gleichungssysteme (grafisch), Ungleichungen (grafisch), später Parabeln; der Fehler zeigt sich im Bild von selbst. Vorgabe und 20 Aufgaben: Abschnitt 4 und 5.
2. **`markieren` als Mehrfach-Auswahl.** Begründung: kleiner Aufwand; senkt die Rate-Chance dort, wo heute 31 % aller Aufgaben mit 50 % Rate-Chance laufen; passt auf Teilbarkeit, Vierecke, Termarten, „welche Aussagen stimmen“. Vorher zu klären: leere Menge, Anzeige nach dem ersten Fehler.
3. **Falsche Antwort als Bild** (R1, schmal). Begründung: nutzt die Zeichen-Ebene von Platz 1, braucht keine neuen Aufgaben, wirkt sofort auf vorhandene Geraden- und Zahlenstrahl-Aufgaben.

**Bewusst wartet:** Schieber (Schätzen geht heute; Parameter prüft wenig) · Zuordnung und Reihenfolge (Bewertung unklar, wenig Denken) · Term-Rechner mit Mach 100 und „Aufgabe erfinden“ (Regeln lückenhaft, Server-Risiko) · Sicherheits-Wette (erst mit Preis) · verkettete Karten (erst Aufwand klären) · Bruch nach Wert (wenn Klasse 6 ansteht) · Reise-Aufgaben, Foto, Knobel der Woche. **Weiter verworfen:** Waage, Videos, freies Zeichnen, Zeitdruck.

---

## 4. Bau-fertige Vorgabe: Antworttyp `punkte`

Entwurf zum Anklicken: `entwurf-punkte.html`. Referenz der Prüfung: Funktion `bewerte` in `nachrechnen2.py` (läuft gegen alle 20 Lösungen, 39 typische Fehler und je 12–13 Unsinn-Antworten).

### 4.1 Mechanik (was das Kind tut)

- Das Bild ist das vorhandene Koordinatengitter (`f.grafik`, Typ `koordinaten`), **immer mit quadratischen Kästchen**.
- **Tippen** auf das Gitter setzt einen Punkt auf den nächsten Rasterpunkt.
- Tippen auf einen **gesetzten** Punkt wählt ihn aus (er wird nicht gelöscht).
- Sind schon alle Punkte gesetzt, **springt der gewählte Punkt** an die neue Stelle. Umsetzen geht also mit einem Tipp.
- **Vier Pfeil-Knöpfe** (je 48 px) rücken den gewählten Punkt um einen Rasterschritt. Das ist die Korrektur für Fehltipps und ersetzt das Ziehen. „Punkt weg“ löscht den gewählten Punkt. Auf dem Rechner tun es auch die Pfeiltasten.
- Die App verbindet, wenn `verbinden` gesetzt ist: `gerade` (durch die gesetzten Punkte, bis zum Bildrand), `strecke`, `vieleck`. Feste Punkte aus `mit` gehören dazu (Reihenfolge: erst `mit`, dann die gesetzten). Die Gerade erscheint erst, wenn alle Punkte gesetzt sind.
- Gesetzte Punkte bekommen **keine Koordinaten-Beschriftung** (sonst wird „Trage P(−3 | 2) ein“ zum Zahlenvergleich). Erlaubt ist ein Name aus `namen` („P“, „D“).
- Keine Animation. Die einzige Bewegung ist der Punkt, der auf das Raster springt.

### 4.2 Datensatz

Frage `f`:

| Feld | Bedeutung |
|---|---|
| `text` | sagt, **wie viele** Punkte zu setzen sind |
| `grafik` | wie heute: `typ: "koordinaten"`, `x`, `y`, dazu was gegeben ist (`punkte`, `strecken`, `graphen`, `name_x`, `name_y`) |
| `setzen.anzahl` | genaue Zahl der zu setzenden Punkte (Version 1: 1 oder 2) |
| `setzen.raster` | 1 (Vorgabe) oder 0,5 |
| `setzen.verbinden` | fehlt · `gerade` · `strecke` · `vieleck` |
| `setzen.mit` | feste Punkte, die mitverbunden werden, z. B. `[[2, 3]]` |
| `setzen.namen` | Namen der gesetzten Punkte in Setz-Reihenfolge (nur Anzeige) |

Antwort (wird gespeichert): `{"punkte": [[x, y], …]}` in Setz-Reihenfolge.

Lösung `o` – zwei Regeln:

| Regel | Felder | richtig, wenn |
|---|---|---|
| `menge` | `punkte: [[x, y], …]` oder `mengen: [ […], […] ]` | die gesetzten Punkte als **Menge** gleich `punkte` sind (oder gleich einer der `mengen`). Reihenfolge egal. |
| `gerade` | `durch: [[x₁, y₁], [x₂, y₂]]` | alle gesetzten Punkte verschieden sind und **genau** auf der Geraden durch die beiden Punkte liegen: (x₂ − x₁)(y − y₁) − (y₂ − y₁)(x − x₁) = 0. Senkrechte Geraden gehen damit auch. |

Beispiele (erzeugt vom Skript; alle 20 in `aufgaben-auftrag2.json`):

<!-- BEISPIELE:ANFANG -->
```json
{"l": "strecken", "p": "uebung", "s": 1, "g": "direkt", "y": "punkte", "f": {"text": "A(−1 | 2) ist gegeben. Setze B so, dass die Strecke [AB] waagrecht liegt und 3 Einheiten lang ist. Es gibt zwei passende Punkte, einer genügt.", "grafik": {"typ": "koordinaten", "x": [-5, 5], "y": [-5, 5], "punkte": [{"x": -1, "y": 2, "name": "A"}]}, "setzen": {"anzahl": 1, "namen": ["B"], "verbinden": "strecke", "mit": [[-1, 2]]}}, "o": {"regel": "menge", "mengen": [[[2, 2]], [[-4, 2]]]}, "h": "Waagrecht heißt: A und B haben dieselbe y-Koordinate.", "w": "Waagrecht: y bleibt 2. 3 nach rechts: B(2 | 2). 3 nach links geht auch: B(−4 | 2)."}
{"l": "vierecke", "p": "uebung", "s": 2, "g": "umkehr", "y": "punkte", "f": {"text": "ABCD ist ein Parallelogramm mit A(−4 | −2), B(1 | −2) und C(3 | 2). Setze die Ecke D.", "grafik": {"typ": "koordinaten", "x": [-5, 5], "y": [-5, 5], "punkte": [{"x": -4, "y": -2, "name": "A"}, {"x": 1, "y": -2, "name": "B"}, {"x": 3, "y": 2, "name": "C"}], "strecken": [[-4, -2, 1, -2], [1, -2, 3, 2]]}, "setzen": {"anzahl": 1, "namen": ["D"], "verbinden": "vieleck", "mit": [[-4, -2], [1, -2], [3, 2]]}}, "o": {"regel": "menge", "punkte": [[-2, 2]]}, "h": "Wie kommst du von B nach C? Genauso kommst du von A nach D.", "w": "Von B nach C: 2 nach rechts, 4 nach oben. Von A genauso: (−4 + 2 | −2 + 4) = (−2 | 2)."}
{"l": "graph_ablesen", "p": "uebung", "s": 1, "g": "direkt", "y": "punkte", "f": {"text": "Zeichne die Gerade y = (1/2)x − 1. Setze zwei Gitterpunkte der Geraden.", "grafik": {"typ": "koordinaten", "x": [-4, 6], "y": [-5, 5]}, "setzen": {"anzahl": 2, "verbinden": "gerade"}}, "o": {"regel": "gerade", "durch": [[0, -1], [2, 0]]}, "h": "Starte bei t auf der y-Achse. m = 1/2 heißt: 2 nach rechts, 1 nach oben.", "w": "Start (0 | −1). 2 nach rechts, 1 nach oben: (2 | 0). Jeder weitere Schritt gibt wieder einen Gitterpunkt."}
```
<!-- BEISPIELE:ENDE -->

### 4.3 Prüfregel und Toleranz

- **Toleranz am Finger:** Der Tipp darf bis zu einem halben Rasterschritt neben dem Punkt liegen (im Entwurf bei 360 px: 11,5 px). Tipps mehr als einen halben Schritt außerhalb des Gitters werden nicht beachtet.
- **Toleranz auf dem Server: keine.** Verglichen werden die eingerasteten Werte, exakt (in SQL `numeric`, kein Gleitkomma). Grund: Abschnitt 2.2, Punkt 1.
- **Fehlermuster** (`grund`, wie heute bei `zahl` und `luecken`; nur beim Fehler):

| `grund` | Regel | erkannt, wenn | Hinweis an das Kind |
|---|---|---|---|
| `vertauscht` | `menge` | mit x und y vertauscht wäre es richtig | „Fast: x und y sind vertauscht. Die erste Zahl gehört zur x-Achse.“ |
| `vorzeichen` | `menge` | die Beträge aller Koordinaten stimmen | „Fast: Schau auf die Vorzeichen. Minus heißt links oder unten.“ |
| `ein_punkt` | `gerade`, 2 Punkte | genau ein Punkt liegt auf der Geraden | „Ein Punkt passt, der andere nicht. Prüf dein Steigungsdreieck.“ |
| `verschoben` | `gerade`, 2 Punkte | kein Punkt passt, aber die Richtung ist gleich | „Die Richtung stimmt. Aber die Gerade liegt an der falschen Stelle.“ |

  Reihenfolge der Prüfung: erst `vertauscht`, dann `vorzeichen`. Bekannte Unschärfe [G]: `vorzeichen` schlägt auch an, wenn nur eine Koordinate das falsche Vorzeichen hat (K5: (4 | −1) statt (4 | 1)) – der Hinweis passt trotzdem.
- **Zweiter Versuch:** Die Punkte bleiben stehen, das eigene Bild wird rot, das Kind korrigiert. Nach dem zweiten Fehler: Lösung grün gestrichelt **über** dem roten eigenen Bild, darunter der Lösungsweg `w`. Bei `gerade` zeichnet die App die Gerade durch `durch`. Das ist „Fehler sichtbar machen“ ohne Zusatzarbeit.
- **Anzeige für Lehrer** (`lernAntwortText`): „(0 | −1), (2 | 0)“; Lösung bei `gerade`: „Gerade durch (0 | −1) und (2 | 0)“, bei `mengen`: mit „oder“.

### 4.4 Kleinste Breite

- 360 px. Regel für Inhalte: **höchstens 10 Rasterschritte je Achse, beide Achsen gleich lang.** Gemessen im Entwurf [G]: 23 px je Kästchen bei 360 px, 39 px ab 820 px. In der App hängt der Wert vom Innenabstand der Karte ab; Rechnung: 264 von 340 Bild-Einheiten sind Gitter.
- 23 px sind weniger als die 44-px-Tippfläche. Deshalb sind die Pfeil-Knöpfe Pflicht, nicht Zugabe. Alle Knöpfe im Entwurf haben mindestens 44 px [G].
- Raster 0,5 nur bei höchstens 5 Einheiten je Achse (wieder 10 Schritte).
- [A] Wie oft ein Kind danebentippt, ist nicht gemessen. Vorschlag: mit dem Testkind 20 Punkte setzen lassen; liegt die Fehltipp-Quote über 1 von 10, auf 8 Schritte je Achse gehen.

### 4.5 Nichts tun und Unsinn

| Fall | Gerät | Server |
|---|---|---|
| nichts oder zu wenig gesetzt | „Setze noch einen Punkt.“ / „Setze noch 2 Punkte.“ | `format_ok: false`, zählt **nicht** als Versuch |
| mehr Punkte als `anzahl` | geht nicht (der gewählte Punkt springt) | `format_ok: false` |
| zwei Punkte auf derselben Stelle | geht nicht (Antippen wählt aus; Pfeil bleibt stehen) | `format_ok: false` |
| Punkt außerhalb des Bildes | Tipp wird nicht beachtet; Pfeil bleibt am Rand stehen | `format_ok: false` |
| Wert nicht auf dem Raster, kein Zahlenpaar, Text, leer | kann das Gerät nicht erzeugen | `format_ok: false`, Hinweis „Das hat nicht geklappt. Setze die Punkte bitte neu.“ |
| alle Punkte irgendwohin | – | gültige Antwort, einfach falsch |

Die Lösung geht wie bisher erst nach der Prüfung an das Gerät.

### 4.6 Was der Bau-Chat anfassen muss

- `schule.antwort_bewerten`: neuer Zweig für `punkte` (zwei Regeln, vier Fehlermuster; Vorlage `bewerte`). [G: Stelle gelesen]
- `lernen.js`: `lernAufgabe` (Eingabe-Ebene über `lernKoordinaten`, Pfeil-Knöpfe), `lernKoordinaten` (quadratische Kästchen auch mit `graphen`; heute nur ohne), `lernAntwortText`, Anzeige nach dem Prüfen, Rückblick/Testergebnis. [G: Stellen gelesen]
- `tools/inhalt_pruefen.py`: `TYPEN` und die Regeln unten. [G]
- Expeditionen (`v_y`): vom Vorgänger genannt, von mir nicht geprüft. [A]

Regeln für Inhalte (für `inhalt_pruefen.py` und den Aufgaben-Ersteller):

1. Beide Achsen gleich lang, höchstens 10 Rasterschritte.
2. `menge`: Zahl der Lösungspunkte = `anzahl`; alle auf dem Raster und im Bild; keiner ist schon eingezeichnet.
3. `gerade`: mindestens 3 Rasterpunkte der Geraden liegen im Bild; `durch` sind zwei davon.
4. Eindeutigkeit per Programm: alle Rasterpunkte des Bildes gegen die Bedingung der Aufgabe prüfen – es dürfen nur die Lösungen übrig bleiben.
5. Die typische falsche Antwort muss im Bild liegen. Sonst kann das Kind sie nicht setzen und die App sie nicht erkennen. (Bei drei meiner ersten Fassungen lag sie außerhalb; das Skript prüft es jetzt.)
6. Der Tipp enthält keine Lösungskoordinate.
7. Ist die Antwort ein sichtbarer Schnittpunkt gezeichneter Linien, ist es höchstens Stufe 1.

### 4.7 Wofür sich die Form nicht eignet

Krumme Koordinaten (Schnittpunkt bei x = 1,4), Kurven freihand, Konstruktionen mit Zirkel, Winkel messen. Aufgaben mit sehr vielen richtigen Antworten („Zeichne ein Rechteck mit Flächeninhalt 12“) brauchen eine dritte Regel mit Bedingungen – sinnvoll für Klasse 5 (Lima), aber erst Version 2.

---

## 5. 20 Musteraufgaben für `punkte`

Alle Lösungen sind in `nachrechnen2.py` auf zwei Wegen nachgerechnet: Weg 1 rechnet, Weg 2 durchsucht unabhängig alle Rasterpunkte des Bildes (zeigt zugleich die Eindeutigkeit) oder läuft im Gitter. Bei Regel `gerade` ist geprüft, dass **jedes** Paar von Gitterpunkten der Geraden angenommen wird. Etappen-Schlüssel sind die der vorhandenen Dateien. „Häufigste falsche Antwort“ ist durchweg **Annahme**, nicht aus Daten.

Stufen: Klasse 5 – 3 leicht, 4 mittel, 3 schwer; Klasse 8 – 2 leicht, 4 mittel, 4 schwer. Zehn verschiedene Aufgabentypen `g`.

<!-- AUFGABEN:ANFANG -->
### Flug Klasse 5 – „Grundbegriffe und Figuren“ (`geometrie.grundbegriffe`, Kairo)

**K1 · `koordinaten` · leicht (`direkt`) · Regel `menge`**  
Text: „Trage den Punkt P(−3 | 2) ein.“  
Lösung: P(−3 | 2)  
Weg 1: Vom Ursprung 3 nach links, 2 nach oben: (0 − 3 | 0 + 2) = (−3 | 2).  
Weg 2: Alle 121 Gitterpunkte durchsucht: nur einer liegt 3 links der y-Achse und 2 über der x-Achse.  
Häufigste falsche Antwort (Annahme): (2 | −3) – verrät: x und y vertauscht (Fehlermuster `vertauscht`)  
Tipp: Erste Zahl: nach links oder rechts. Zweite Zahl: nach oben oder unten.

**K2 · `koordinaten` · leicht (`erkennen`) · Regel `menge`**  
Text: „Ein Punkt liegt 4 Einheiten unter der x-Achse und 2 Einheiten links von der y-Achse. Setze ihn.“  
Lösung: (−2 | −4)  
Weg 1: links ⇒ x = −2, unten ⇒ y = −4.  
Weg 2: Alle Gitterpunkte durchsucht: nur (−2 | −4) hat Abstand 2 zur y-Achse (links) und 4 zur x-Achse (unten).  
Häufigste falsche Antwort (Annahme): (−4 | −2) – verrät: „unter der x-Achse“ als x-Koordinate gelesen (Fehlermuster `vertauscht`)  
Tipp: Links von der y-Achse: Die x-Koordinate ist negativ. Unter der x-Achse: Die y-Koordinate ist negativ.

**K3 · `koordinaten` · mittel (`einkleidung`) · Regel `menge`**  
Text: „Schatzkarte: Du startest bei S(−4 | 1). Geh 6 Kästchen nach Osten (rechts) und 3 nach Süden (unten). Setze das Kreuz dorthin.“  
Lösung: (2 | −2)  
Weg 1: (−4 + 6 | 1 − 3) = (2 | −2).  
Weg 2: Alle Gitterpunkte durchsucht: nur von (2 | −2) kommt man mit 6 nach links und 3 nach oben zurück zu S.  
Häufigste falsche Antwort (Annahme): (2 | 4) – verrät: nach Norden statt nach Süden gegangen  
Tipp: Rechts ändert nur die erste Zahl, unten nur die zweite.

**K4 · `strecken` · leicht (`direkt`) · Regel `menge`**  
Text: „A(−1 | 2) ist gegeben. Setze B so, dass die Strecke [AB] waagrecht liegt und 3 Einheiten lang ist. Es gibt zwei passende Punkte, einer genügt.“  
Lösung: B(2 | 2) oder B(−4 | 2)  
Weg 1: −1 + 3 = 2 und −1 − 3 = −4, y = 2.  
Weg 2: Alle Gitterpunkte durchsucht: genau (2 | 2) und (−4 | 2) liegen auf Höhe 2 im Abstand 3 von A.  
Häufigste falsche Antwort (Annahme): (−1 | 5) – verrät: senkrecht statt waagrecht  
Tipp: Waagrecht heißt: A und B haben dieselbe y-Koordinate.

**K5 · `strecken` · mittel (`mehrschritt`) · Regel `menge`**  
Text: „M(1 | −1) ist der Mittelpunkt der Strecke [AB]. A(−2 | −3) ist gegeben. Setze B.“  
Lösung: B(4 | 1)  
Weg 1: B = M + (M − A) = (1 + 3 | −1 + 2) = (4 | 1).  
Weg 2: Alle Gitterpunkte durchsucht: nur für (4 | 1) ist die Mitte von A und B genau M (Summe der Koordinaten = 2 · M).  
Häufigste falsche Antwort (Annahme): (−5 | −5) – verrät: von A aus in die falsche Richtung gelaufen (M − A abgezogen statt dazugezählt)  
Tipp: Wie kommst du von A nach M? Denselben Weg gehst du von M aus noch einmal.

**K6 · `lagebeziehungen` · mittel (`darstellung`) · Regel `gerade`**  
Text: „g geht durch A(−4 | −1) und B(2 | 2). Zeichne die Parallele zu g durch P(−2 | 3): Setze zwei Gitterpunkte der Parallelen.“  
Lösung: y = 0,5x + 4 – je zwei verschiedene Gitterpunkte dieser Geraden  
Weg 1: Parallele: y = 0,5x + 4 (Steigung von g: 3 : 6 = 0,5; durch P: 3 = −1 + 4).  
Weg 2: Ab P in Schritten (2 | 1) laufen: (−4 | 2), (−2 | 3), (0 | 4), (2 | 5) – dieselben Punkte wie aus der Gleichung.  
Häufigste falsche Antwort (Annahme): (−2 | 3), (−1 | 5) – verrät: Treppe gekippt: 1 nach rechts, 2 nach oben (Fehlermuster `ein_punkt`)  
Tipp: Wie läuft g von Gitterpunkt zu Gitterpunkt? Dieselbe Treppe startest du bei P.

**K7 · `lagebeziehungen` · schwer (`verknuepfen`) · Regel `menge`**  
Text: „Fälle das Lot von P(−1 | 4) auf die Gerade g. Setze den Punkt, in dem das Lot g trifft.“  
Lösung: F(1 | 0)  
Weg 1: Skalarprodukt: (P − F) · Richtung von g = (−2 | 4) · (2 | 1) = −4 + 4 = 0, F(1 | 0) liegt auf g.  
Weg 2: Unter allen Gitterpunkten von g hat (1 | 0) den kleinsten Abstand zu P; die exakte Projektion von P auf g ist ebenfalls (1 | 0).  
Häufigste falsche Antwort (Annahme): (−1 | −1) – verrät: Lot als „senkrecht nach unten“ verstanden statt senkrecht zu g  
Tipp: g läuft 2 nach rechts, 1 nach oben. Dreh diese Treppe um eine Vierteldrehung: 1 nach rechts, 2 nach unten.

**K8 · `vierecke` · mittel (`umkehr`) · Regel `menge`**  
Text: „ABCD ist ein Parallelogramm mit A(−4 | −2), B(1 | −2) und C(3 | 2). Setze die Ecke D.“  
Lösung: D(−2 | 2)  
Weg 1: D = A + (C − B) = (−4 + 2 | −2 + 4) = (−2 | 2).  
Weg 2: Alle Gitterpunkte durchsucht: nur für (−2 | 2) haben die Diagonalen [AC] und [BD] denselben Mittelpunkt.  
Häufigste falsche Antwort (Annahme): (−4 | 2) – verrät: D senkrecht über A gesetzt (an ein Rechteck gedacht)  
Tipp: Wie kommst du von B nach C? Genauso kommst du von A nach D.

**K9 · `vierecke` · schwer (`transfer`) · Regel `menge`**  
Text: „A, B und C sind drei Ecken eines Quadrats ABCD. Setze die vierte Ecke D.“  
Lösung: D(−3 | 0)  
Weg 1: D = A + (C − B) = (−3 | 0).  
Weg 2: Alle Gitterpunkte durchsucht: nur für (−3 | 0) sind alle vier Seiten gleich lang und beide Diagonalen gleich lang.  
Häufigste falsche Antwort (Annahme): (−3 | 3) – verrät: an ein Quadrat mit waagrechten Seiten gedacht  
Tipp: Das Quadrat steht auf der Spitze. Von B nach C geht es 3 nach links und 3 nach oben – genauso von A nach D.

**K10 · `koordinaten` · schwer (`rueckwaerts`) · Regel `menge`**  
Text: „Ein Punkt wurde erst um 3 nach links und dann um 2 nach oben verschoben. Jetzt liegt er bei Q(−1 | 2). Setze den Punkt dorthin, wo er am Anfang lag.“  
Lösung: (2 | 0)  
Weg 1: Rückwärts von Q: (−1 + 3 | 2 − 2) = (2 | 0).  
Weg 2: Alle Gitterpunkte durchsucht: nur (2 | 0) landet nach „3 links, 2 hoch“ auf Q.  
Häufigste falsche Antwort (Annahme): (−4 | 4) – verrät: die Verschiebung noch einmal in dieselbe Richtung ausgeführt  
Tipp: Geh den Weg von Q aus zurück: Aus links wird rechts, aus oben wird unten.

### Flug Klasse 8 – „Lineare Funktionen“ (`funktionen.linear`, Neumayer-Station III)

**G1 · `graph_ablesen` · leicht (`direkt`) · Regel `gerade`**  
Text: „Zeichne die Gerade y = (1/2)x − 1. Setze zwei Gitterpunkte der Geraden.“  
Lösung: durch (0 | −1) und (2 | 0) – je zwei verschiedene Gitterpunkte dieser Geraden  
Weg 1: Einsetzen: x = 0 ⇒ y = −1; x = 2 ⇒ y = 1 − 1 = 0.  
Weg 2: Ab (0 | −1) im Steigungsdreieck (2 | 1) laufen: (−4 | −3), (−2 | −2), (0 | −1), (2 | 0), (4 | 1), (6 | 2).  
Häufigste falsche Antwort (Annahme): (0 | −1), (1 | 1) – verrät: Steigungsdreieck gekippt: 1 nach rechts, 2 nach oben (Fehlermuster `ein_punkt`)  
Tipp: Starte bei t auf der y-Achse. m = 1/2 heißt: 2 nach rechts, 1 nach oben.

**G2 · `graph_ablesen` · leicht (`erkennen`) · Regel `menge`**  
Text: „Der Graph von f ist gezeichnet. Setze den Punkt des Graphen, der die y-Koordinate −3 hat.“  
Lösung: (4 | −3)  
Weg 1: f(x) = −1,5x + 3 = −3 ⇒ −1,5x = −6 ⇒ x = 4.  
Weg 2: Alle Gitterpunkte durchsucht: nur (4 | −3) liegt auf dem Graphen und hat y = −3. Gelaufen: von (0 | 3) drei Dreiecke „2 rechts, 3 runter“: (2 | 0), (4 | −3).  
Häufigste falsche Antwort (Annahme): (2 | 0) – verrät: die Nullstelle gesetzt (y = 0 statt y = −3)  
Tipp: Such auf der y-Achse die −3 und geh waagrecht bis zum Graphen.

**G3 · `graph_ablesen` · mittel (`mehrschritt`) · Regel `gerade`**  
Text: „Zeichne die Gerade 3x + 2y = 8. Setze zwei Gitterpunkte der Geraden.“  
Lösung: y = −1,5x + 4 – je zwei verschiedene Gitterpunkte dieser Geraden  
Weg 1: Auflösen: y = −(3/2)x + 4; ab (0 | 4) im Dreieck „2 rechts, 3 runter“ laufen.  
Weg 2: Alle Gitterpunkte in 3x + 2y = 8 eingesetzt: (0 | 4), (2 | 1), (4 | −2), (6 | −5) – dieselben Punkte.  
Häufigste falsche Antwort (Annahme): (0 | 4), (3 | 2) – verrät: Steigungsdreieck gekippt: 3 nach rechts, 2 nach unten (Fehlermuster `ein_punkt`)  
Tipp: Löse zuerst nach y auf. Oder such zwei Punkte, bei denen die Rechnung aufgeht, zum Beispiel x = 0.

**G4 · `aufstellen` · mittel (`umkehr`) · Regel `menge`**  
Text: „Eine Gerade hat die Steigung 2 und geht durch P(2 | 3). Setze den Punkt, in dem sie die y-Achse schneidet.“  
Lösung: (0 | −1)  
Weg 1: Einsetzen: 3 = 2 · 2 + t ⇒ t = −1.  
Weg 2: Alle Gitterpunkte durchsucht: nur (0 | −1) liegt auf der y-Achse und hat zu P die Steigung 2. Gelaufen: (2 | 3) → (1 | 1) → (0 | −1).  
Häufigste falsche Antwort (Annahme): (0 | 7) – verrät: nach links gegangen und dabei nach oben gezählt (3 + 4)  
Tipp: Von P zur y-Achse sind es 2 Schritte nach links. Wie weit geht es dabei nach unten?

**G5 · `lage` · mittel (`darstellung`) · Regel `gerade`**  
Text: „g: y = (1/2)x + 1 ist gezeichnet. Zeichne die Parallele zu g durch P(2 | −2): Setze zwei Gitterpunkte.“  
Lösung: y = 0,5x − 3 – je zwei verschiedene Gitterpunkte dieser Geraden  
Weg 1: t = y − m · x = −2 − 0,5 · 2 = −3, also y = 0,5x − 3.  
Weg 2: Ab P im Dreieck (2 | 1) laufen: (−4 | −5), (−2 | −4), (0 | −3), (2 | −2), (4 | −1), (6 | 0).  
Häufigste falsche Antwort (Annahme): (2 | −2), (3 | 0) – verrät: Steigung 2 statt 1/2 (Dreieck gekippt) (Fehlermuster `ein_punkt`)  
Tipp: Parallel heißt: gleiche Steigung. Nimm das Steigungsdreieck von g und starte bei P.

**G6 · `deuten` · mittel (`einkleidung`) · Regel `menge`**  
Text: „Mia hat 9 € Guthaben. Jeden Tag werden 1,50 € abgebucht. Setze den Startpunkt und den Punkt, an dem das Guthaben aufgebraucht ist.“  
Lösung: (0 | 9) und (6 | 0)  
Weg 1: 9 − 1,5x = 0 ⇒ x = 9 : 1,5 = 6.  
Weg 2: Tag für Tag: 9 · 7,50 · 6 · 4,50 · 3 · 1,50 · 0 – nach 6 Tagen leer.  
Häufigste falsche Antwort (Annahme): (9 | 0), (0 | 6) – verrät: Tage und Euro vertauscht (Achsen verwechselt) (Fehlermuster `vertauscht`)  
Tipp: Start: Tag 0. Aufgebraucht heißt: Guthaben 0 €. Nach wie vielen Tagen ist das?

**G7 · `lage` · schwer (`verknuepfen`) · Regel `gerade`**  
Text: „g: y = 2x − 3 ist gezeichnet. Zeichne die Senkrechte zu g durch P(4 | 0): Setze zwei Gitterpunkte.“  
Lösung: y = −0,5x + 2 – je zwei verschiedene Gitterpunkte dieser Geraden  
Weg 1: m₂ = −1 : 2 = −0,5; t = 0 + 0,5 · 4 = 2.  
Weg 2: Richtungen (1 | 2) und (2 | −1): 1 · 2 + 2 · (−1) = 0, also rechter Winkel. Gelaufen ab P: (−4 | 4), (−2 | 3), (0 | 2), (2 | 1), (4 | 0), (6 | −1).  
Häufigste falsche Antwort (Annahme): (4 | 0), (5 | −2) – verrät: nur das Vorzeichen gedreht: Steigung −2 (Fehlermuster `ein_punkt`)  
Tipp: Senkrecht: Die Steigungen ergeben malgenommen −1. Oder: Dreh das Steigungsdreieck von g um eine Vierteldrehung.

**G8 · `schnittpunkte` · schwer (`transfer`) · Regel `menge`**  
Text: „Roller A kostet 3 € Grundpreis und 0,50 € pro Kilometer. Roller B kostet 1 € Grundpreis und 1 € pro Kilometer. Setze den Punkt, bei dem beide gleich viel kosten.“  
Lösung: (4 | 5)  
Weg 1: Vorsprung : Aufholen = (3 − 1) : (1 − 0,5) = 4; Preis 5 €.  
Weg 2: Alle Gitterpunkte durchsucht: nur (4 | 5) erfüllt beide Preisgleichungen y = 3 + 0,5x und y = 1 + x.  
Häufigste falsche Antwort (Annahme): (2 | 3) – verrät: Vorsprung nur durch den Preis von B geteilt (2 : 1)  
Tipp: B ist am Anfang 2 € billiger. Um wie viel holt A pro Kilometer auf?

**G9 · `zwei_punkte` · schwer (`rueckwaerts`) · Regel `gerade`**  
Text: „Eine Gerade schneidet die x-Achse bei x = 6 und hat die Steigung −1/2. Zeichne sie: Setze zwei Gitterpunkte.“  
Lösung: y = −0,5x + 3 – je zwei verschiedene Gitterpunkte dieser Geraden  
Weg 1: 0 = −0,5 · 6 + t ⇒ t = 3; y = −0,5x + 3.  
Weg 2: Ab (6 | 0) im Dreieck (−2 | +1) laufen: (4 | 1), (2 | 2), (0 | 3), (−2 | 4) – dieselben Punkte wie aus der Gleichung.  
Häufigste falsche Antwort (Annahme): (6 | 0), (0 | −3) – verrät: nach links gegangen und nach unten gezählt (Vorzeichen der Steigung) (Fehlermuster `ein_punkt`)  
Tipp: Starte bei (6 | 0). Geh rückwärts: 2 nach links – geht es dann nach oben oder nach unten?

**G10 · `aufstellen` · schwer (`parameter`) · Regel `gerade`**  
Text: „Für welches t geht die Gerade y = −x + t durch P(2 | 3)? Zeichne diese Gerade: Setze zwei Gitterpunkte.“  
Lösung: y = −x + 5 – je zwei verschiedene Gitterpunkte dieser Geraden  
Weg 1: 3 = −2 + t ⇒ t = 5.  
Weg 2: Ab P im Dreieck (1 | −1) laufen: … (0 | 5), (1 | 4), (2 | 3), (3 | 2) … – bei allen ist x + y = 5.  
Häufigste falsche Antwort (Annahme): (0 | 1), (1 | 0) – verrät: t = 3 − 2 = 1 gerechnet (Vorzeichen beim Auflösen) (Fehlermuster `verschoben`)  
Tipp: Von P zur y-Achse: 2 nach links. Bei Steigung −1 geht es dabei 2 nach oben.

<!-- AUFGABEN:ENDE -->

---

## 6. Nicht geprüft, Annahmen, offen

**Nicht geprüft**
- Datenbank: Stand der Aufgaben nach Teilung und Korrekturen; Versuche der Kinder.
- Die 20 Aufgaben mit `tools/inhalt_pruefen.py` (kennt den Typ `punkte` nicht).
- Der Entwurf auf einem echten Handy mit echtem Finger. Getestet im Programm-Browser bei 360, 820 und 1280 px, hell und dunkel: alle 20 Aufgaben je dreimal durchgespielt (Fehler → Hinweis → richtig; zweimal falsch → Lösung; Pfeile), jeder Tipp absichtlich 35 % eines Kästchens daneben, keine Skriptfehler, kein Überlauf.
- Lehrplan: Ob „Lot auf eine schräge Gerade im Gitter“ (K7) und „schräges Quadrat“ (K9) in Klasse 5 Gymnasium Bayern als Stufe 3 passen, habe ich nicht gegen LehrplanPLUS geprüft. Die Etappe `lagebeziehungen` behandelt Lot und Abstand; im Gitter schräg ist anspruchsvoller als mit Geodreieck.
- Aufwand für verkettete Karten und für quadratische Kästchen in `lernKoordinaten` mit Graphen.

**Annahmen**
- Alle „häufigsten falschen Antworten“.
- Inhaltsbreite der Karte am Handy etwa 300 px (daraus 23 px je Kästchen).
- Die Werkstatt-Regeln aus `AGENTS.md` (Wunsch → Sperre im Council) gelten für Änderungen an der App, nicht für Ablage-Dateien einer Rolle im eigenen Ordner; ich habe deshalb keinen Council-Vorgang angelegt.

**Schönheitsfehler im Entwurf (Sache des Designers):** Namen gegebener Punkte können Achsenzahlen überdecken (z. B. „A“ in K6).

**Offene Fragen:** stehen in der Postfach-Meldung und im Chat.
