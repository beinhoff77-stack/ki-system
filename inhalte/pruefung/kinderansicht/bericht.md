# Aufbau der Kinderansicht – Prüfbericht (2026-11-16)

Zweig `pruefung-kinderansicht` (von `lernen-app`, Stand 3f03b8a). Nichts an App, Tests, Datenbank oder Inhalten geändert.

**Grundlage**
- **Code gelesen:** `lernen.js` (alle Kinderansichten, `lernReiseDaten`, `lernRahmen`) und `lernen/schule.js` (Kinder-Anmeldung).
- **Rundgang nachgestellt:** `rundgang.test.cjs`, Kind-Anmeldung auf `/lernen/` mit Lern-Code. Zwei Testkinder, je Handy (390 px) und Tablet (820 px):
  - Kind A: Klasse 5, helle Ansicht.
  - Kind B: Klasse 8, dunkle Ansicht, mit einer „Rückreise“ (Lücke Klasse 7).
- **Echte Lehrstoff-Struktur:** 65 Orte, 8 Gebiete, Einheiten mit Lernkartenzahl. Gelesen aus der Datenbank (`schule.block/kontinent/einheit`, keine Kinderdaten) und abgelegt in `orte.json`. Lernkarten aus `inhalte/themen`.
- **Annahme:** Die Reisepläne (welche Orte geplant, was geschafft) sind **erfunden**. Die echten Pläne der Kinder habe ich nicht gelesen.
- **Ergebnisse:** Bilder in `bilder/` (`k1-…` = Kind A, `k2-…` = Kind B), Messwerte in `messung.json`.

Kennzeichnung: **[nachgestellt]** mit Bild/Messung · **[Code]** aus dem Code · **[Meinung]**.

---

## 1. So ist die App heute gebaut

```
Anmeldung (Lern-Code) ─► ABFLUGTAFEL (#/reise) ── Startseite
                          │  oberste Zeile „EINSTEIGEN“ = nächstes Thema
                          │  gelber Knopf unten: „Erst wiederholen“ / „Einsteigen“
                          │  eingeklappt: Alle offenen Flüge · Gelandet – zum Wiederholen · Frühere Klassen · Später
                          │  ganz unten: „Mein Stand · Gymnasium Klasse 5 – 2 von 14 Themen“
                          │
     Menü ≡ (unten rechts, einziger Weg zu den anderen Seiten im neuen Design)
       ├─ Mein Weg     – Zahlen „kann ich / gerade dran / kommen noch“, Liste je Thema
       ├─ Merkheft     – alle Erklärungen zum Nachlesen, Suche
       ├─ Weltkarte    – „1 von 65 Orten“, Gebiets-Knöpfe, Ortsliste je Gebiet
       └─ Reisepass    – Stempel, Sterne, Lerntage, Belohnungen, Gestaltung, Abmelden

THEMA (#/lerneinheit) – Reiter Erklären | Üben | Fehler; Test/Nachtest unten im Reiter Erklären
WIEDERHOLEN (#/wiederholen) – fällige Aufgaben, über den Startknopf
```

**Bausteine, die das Kind auseinanderhalten muss** [Code]:
- **Ort** (Stadt) enthält 1–5 **Themen**.
- Ein **Thema** hat 4–12 **Lernkarten**. Lernkarten heißen auch „Karte“ oder „Etappe“; eine Aufgabe heißt „Bordkarte“.
- **Gebiet** heißt auch „Kontinent“ bzw. „Erdteil“.
- **Belohnungen und Zähler:** Stempel (alle Themen eines Ortes), Sterne (je Aufgabe), Lerntage.
- **Abläufe:** Test, Verbessern, Nachtest, Rückreise, Wiederholen.

Das sind über 15 Begriffe, mehrere davon doppelt belegt („Karte“ = Lernkarte, Bordkarte oder Weltkarte).

---

## 2. Antworten auf die Fragen

| Frage | Antwort | Beleg |
|---|---|---|
| **Ist es logisch aufgebaut?** | Teilweise. Die Startseite mit **einem** großen Knopf ist gut. Darunter passen drei Ordnungen nicht zusammen: Orte nach **Gebiet** (Weltkarte), Themen nach **Plan-Reihenfolge** (Abflugtafel, Mein Weg) und Klassen nach **Lehrplan**. Ein Ort mischt Klassen: In Rom liegt ein Thema der Klasse 6 im Ort der Klasse 5. Bei 13 von 65 Orten passt die Klasse des Ortes nicht zur Klasse seiner Themen (siehe B8). | [nachgestellt] `k1-handy-1-abflugtafel.png`; Auswertung `orte.json` + `themenliste.json` |
| **Ist klar, wohin man klicken muss?** | Für „weiterlernen“: ja, ein Knopf. Für alles andere: nein. Im neuen Design gibt es keine Leiste. Vier Seiten liegen hinter einem ≡-Knopf unten rechts, der über Inhalten schwebt. Im Reisepass zeigt das Menü „Mein Weg“ als aktuelle Seite an (B6). | [nachgestellt] `k1-handy-2-menue.png`, `k1-handy-3-mein-weg.png`; `messung.json` (menueAktiv) |
| **Sieht das Kind den Fortschritt?** | Ja, aber in **sechs** verschiedenen Zählweisen. Keine davon sagt einfach „Klasse 5: so weit bin ich“. Eine Anzeige ist falsch: „Noch 10 Karten bis zum Stempel“ zählt nur das eine Thema; der Stempel von Rom braucht alle 5 Themen (B2). | [nachgestellt] siehe B1/B2 |
| **Auf welchem Level, für welche Schule?** | Steht da, aber verstreut: „MEIN STAND · GYMNASIUM KLASSE 5“ ganz unten auf der Startseite, „MATHE · KLASSE 5“ in Mein Weg. Im Thema steht „ROM · Gym 5 · RS 5 · IB 1“, also alle drei Schularten statt der eigenen (B7). | [nachgestellt] `k1-handy-7-thema-erster-blick.png` |
| **Gibt es einen klaren Weg?** | Der nächste Schritt ist klar. Der Weg danach nicht: „Gerade dran“ in Mein Weg listet **13 Themen** gleichzeitig (Kind B: 11). Fünfmal steht dort gleich „Rom: Natürliche und ganze Zahlen“, weil der Ortsname statt des Themas gezeigt wird (B3). „Kommt noch“ zeigt Falsches: bei Klasse 5 Themen **ohne** Klasse (Zinseszins, Korrelation …), bei Klasse 8 die Themen der Klassen 5 und 6 als „bereit“ (B4). | [nachgestellt] `k1-handy-3-mein-weg.png`, `k2-handy-3-mein-weg.png` |
| **Kann es Gelerntes schnell nochmal ansehen?** | Es gibt vier Wege, keiner ist schnell: Merkheft (2 Tipps; 11 600 px lang, fünfmal dieselbe Überschrift „ROM · NATÜRLICHE UND GANZE ZAHLEN“, gemischt mit noch nicht Geübtem), „Gelandet – zum Wiederholen“ (eingeklappt), „Kann ich“ in Mein Weg (führt nur an den Anfang des Merkhefts), Weltkarte. Die Suche im Merkheft funktioniert gut. | [nachgestellt] `k1-handy-6-merkheft.png`, `…-6b-merkheft-suche.png`; `messung.json` |
| **Ist die Gliederung nachvollziehbar?** | Für ein Kind kaum [Meinung]. Gründe: zu viele Begriffe (Abschnitt 1); Orte springen zwischen Erdteilen; Funktionen (Klasse 8) liegen in der Antarktis an Forschungsstationen, für die die Weltkarte gar keine Karte zeigt (B9). Die Weltkarte zeigt alle 65 Orte aller Klassen, das Kind steht bei „1 von 65“. | [nachgestellt] `k2-handy-4b-weltkarte-kontinent.png`, `k1-handy-4-weltkarte.png` |
| **Sieht es, was geschafft ist und was noch kommt?** | Geschafft: ja, verteilt auf Stempel, „Gelandet“, „Kann ich“ und Haken in der Weltkarte. Was noch kommt: unzuverlässig (B4) und ohne Bezug zur Klasse (53 Einträge „Später“ bei Klasse 5). | [nachgestellt] |
| **Ist das Handling gut?** | Startknopf im Daumenbereich, große Tippflächen, „Zurück“ im Kopf: gut. Störend: Der ≡-Knopf liegt über Inhalten. Die eingeklappten Gruppen auf der Startseite haben große Lücken. Ein Thema ist auf dem Handy 11 000–12 000 px lang. Das Kind kann im Reisepass auf das „bisherige Design“ umschalten; dort ist die Navigation völlig anders (Leiste mit 4 Reitern, ohne Reisepass) (B10). | [nachgestellt] `messung.json`, `k*-tablet-*.png` |

---

## 3. Befunde

| Nr. | Befund | Beleg | Schwere |
|---|---|---|---|
| B1 | **Sechs Fortschrittsmaße, keines vorn:** „★ 860“ (oben), „1 Stempel“, „2 von 14 Themen“ (ganz unten), „1 von 65 Orten“ (Weltkarte), „1 kann ich · 13 gerade dran · 55 kommen noch“ (Mein Weg, Orte und Themen gemischt), Kartenband „Noch 10 Karten“. | [nachgestellt] Abflugtafel, Weltkarte, Mein Weg | hoch |
| B2 | **„Noch N Karten bis zum Stempel“ ist falsch.** Das Band zählt die Lernkarten des aktuellen Themas (`et.n`), der Stempel verlangt alle Themen des Ortes. In Rom: 10 angezeigt, 44 nötig (10 + 8 + 7 + 7 + 12). | [Code] `lernAbflugtafel`; [nachgestellt] `k1-handy-1-abflugtafel.png` | hoch |
| B3 | **Mein Weg zeigt den Ort statt des Themas.** Die Zeile nimmt `ort_titel`, bei 5 Themen in Rom also fünfmal „Rom: Natürliche und ganze Zahlen“. Dazu „Etappe 4/8“ statt „Karte 4 von 8“. Im Merkheft passiert dasselbe mit den Überschriften. | [nachgestellt] `k1-handy-3-mein-weg.png`, `messung.json` Merkheft | hoch |
| B4 | **„Kommt noch“ falsch gefiltert.** Die Bedingung ist `!ziel_klasse \|\| ziel_klasse <= klasse`. Damit erscheinen Orte ohne Klasse (8 Orte, u. a. Zinseszins, Korrelation) bei Klasse 5, und bei Klasse 8 alle Orte der Klassen 5–7 als „bereit“. Die Abflugtafel ordnet dieselben Orte dagegen „Aus früheren Klassen – zum Auffrischen“ zu. | [Code] `viewWeg`; [nachgestellt] `k2-handy-3-mein-weg.png` | hoch |
| B5 | **„Gerade dran“ ohne Fokus.** Mit Plan gilt jeder Ort im Plan als „jetzt“: 13 Themen „gerade dran“ (Kind A), 11 (Kind B). Ein Kind sieht nicht, was nach dem aktuellen Thema kommt. | [Code] `lernReiseDaten`; [nachgestellt] | mittel |
| B6 | **Menü markiert im Reisepass „Mein Weg“** (`lernRahmen(kind, 'weg', …)` in `viewReisepass`). | [nachgestellt] `messung.json` menueAktiv | niedrig |
| B7 | **Schulart:** Im Thema steht „Gym 5 · RS 5 · IB 1“, alle drei Schularten statt der eigenen. „Gymnasium Klasse 5“ steht nur ganz unten auf der Startseite. | [nachgestellt] `k1-handy-7-thema-erster-blick.png` | mittel |
| B8 | **Klasse von Ort und Thema widersprechen sich bei 13 von 65 Orten.** Beispiele: Cusco gilt als Klasse 5, das Thema „Körper und Netze“ als Klasse 8; Timbuktu als Klasse 7, „Winkel“ als Klasse 5; Rom (5) enthält ein Thema der Klasse 6. Mein Weg und Weltkarte nehmen die Ortsklasse, die Abflugtafel die Themenklasse. Welche Angabe stimmt, ist zu klären (Lehrplan). | Auswertung `orte.json`/`themenliste.json`; [nachgestellt] `k1-handy-3-mein-weg.png` | mittel |
| B9 | **Antarktis ohne Karte:** Für das Gebiet Funktionen (Klasse 8 und höher) blendet die Weltkarte das Kartenbild aus (`erdteil !== 'Antarktis'`). Die Orte sind Forschungsstationen mit langen Namen. Für Kind B ist das der Hauptort der Klasse 8. | [Code]; [nachgestellt] `k2-handy-4b-weltkarte-kontinent.png` | mittel |
| B10 | **Menü-Handling:** Der ≡-Knopf ist der einzige Weg zu 4 Seiten und überdeckt rechts Inhalte (Mein Weg, Weltkarte, Reisepass). Das Kind kann auf das „bisherige Design“ wechseln, mit eigener Leiste und anderen Namen („Heute“, „Karte“). | [nachgestellt] `k1-handy-3…5` | mittel |
| B11 | **Gelerntes nachschlagen ist mühsam:** Das Merkheft enthält auch noch nicht Geübtes, ist 11 600 px lang und nach Ort statt Thema überschrieben. „Kann ich“ in Mein Weg springt an den Anfang des Merkhefts statt zum Thema. | [nachgestellt] | mittel |
| B12 | **Rückreise nicht erklärt:** Kind B (Klasse 8) bekommt „EINSTEIGEN · DELHI · Lineare Gleichungen“ (Klasse 7) als erstes, ohne Hinweis, warum. Der Hinweis „Rückreise …“ steht nur im Testbereich des Themas. | [nachgestellt] `k2-handy-1-abflugtafel.png` | mittel |
| B13 | **Startknopf-Text:** „Erst wiederholen · ROM ›“ führt in die Wiederholung, Ziel steht als „ROM“ daneben. Die Wiederholung kann aus einem anderen Ort stammen. | [nachgestellt] | niedrig |
| B14 | **Zu viel auf der Startseite für Klasse 5:** „Später – für höhere Klassen (53)“, „Alle offenen Flüge (12)“; große Leerräume zwischen den eingeklappten Gruppen. | [nachgestellt] `k1-handy-1-abflugtafel.png` | niedrig |
| – | **Gut:** Ein Startknopf im Daumenbereich. Flugtafel mit Zuständen (EINSTEIGEN, UNTERWEGS, WARTET, GELANDET). Klasse je Zeile. Stempel im Reisepass anschaulich. Suche im Merkheft. Zurück-Pfeil im Kopf. Tablet-Ansicht ruhig und lesbar. | [nachgestellt] | – |

**Nachtrag B8 (Hinweis der Nutzer, Themenplan der Eltern):** Im Plan von Kind A (Klasse 5) stehen:
- **Alexandria** (Ort Klasse 7) mit „Kreis und Tangenten · Gym 7“ und „Ortslinien und Ortsbereiche · Gym 5 · RS 7“.
- **Timbuktu** (Ort Klasse 7) mit „Winkelsätze · Gym 5“.

Ursache: Ein Ort kommt in den Plan, sobald **ein** Thema zur Klasse passt; er bringt seine anderen Themen mit. Zwei Klassenangaben sind vermutlich falsch:
- **Winkelsätze:** Laut LehrplanPLUS gehören Winkel an Geradenkreuzungen und Parallelität in Gym 7; in Gym 5 werden Winkel nur gemessen und gezeichnet. „Gym 5“ ist daher wahrscheinlich falsch.
- **Ortslinien:** Hier fehlt in `themenliste.json` der Lehrplan-Bezug (`lehrplan_gym` leer). Die Angabe „Gym 5“ ist nicht geprüft.

Vorschlag:
- Je Ort nur eine Klasse.
- Die Plan-Ansicht markiert Themen, deren Klasse nicht zur Klasse des Kindes passt.
- Die Klassenangaben aller Themen mit leerem `lehrplan_gym` gegen LehrplanPLUS prüfen. Das sind 16 Themen, darunter `geometrie.winkel`, `geometrie.ortslinien`, `gleichungen.einfach` (je Gym 5), `bruch.dezimal`, `zahlen.potenzen_zehner` (je Gym 6) und `funktionen.grundbegriffe` (Gym 8).

---

## 4. Vorschlag: klarer Aufbau

**Idee [Meinung]:** Eine Frage pro Seite, ein Fortschrittsmaß, Klasse vorn.

| Seite | Frage des Kindes | Inhalt |
|---|---|---|
| **Heute** (Abflugtafel) | Was mache ich jetzt? | Oben: „Gymnasium · Klasse 5 – 4 von 14 Themen“ als **einziges** Fortschrittsmaß, darunter der Ort mit Stempel-Fortschritt („Rom: 1 von 5 Themen“). Ein Knopf. Darunter die nächsten **3** Themen in Reihenfolge („als Nächstes“). Rückreise mit einem Satz Begründung. Alles andere auf „Mein Weg“. |
| **Mein Weg** | Was habe ich geschafft, was kommt? | **Ein** Fahrplan der Klasse, gegliedert nach Lehrplan-Reihenfolge (bzw. Plan der Eltern). Je **Thema** eine Zeile (Themenname, nicht Ortsname) mit Status ✓ / läuft (Karte 3 von 8) / als Nächstes / später. Oben ein Schalter „Liste | Karte“: Die Weltkarte ist eine zweite Ansicht desselben Fahrplans, gefiltert auf die eigene Klasse. „Frühere Klassen“ und „Höhere Klassen“ eingeklappt am Ende. |
| **Merkheft** | Wie ging das nochmal? | Nur **geschaffte** Lernkarten; gegliedert nach Gebiet → Thema → Karte; Suche oben. Aus „Mein Weg“ springt ein ✓-Thema direkt an seine Stelle im Merkheft. |
| **Reisepass** | Was habe ich verdient? | Stempel, Sterne, Belohnungen. Gestaltung und Abmelden in einen eigenen Bereich „Einstellungen“ (für Eltern). |

**Navigation:** Eine feste Leiste unten mit 4 Einträgen (Heute · Mein Weg · Merkheft · Reisepass) in **beiden** Designs statt des schwebenden ≡. Die Weltkarte steckt in „Mein Weg“.

**Begriffe:** Einer pro Sache, überall gleich:

| Sache | Begriff | Ersetzt |
|---|---|---|
| Stadt | Ort | – |
| Lerneinheit | Thema | – |
| Teil eines Themas | Lernkarte | „Etappe“, „Karte“ (allein) |
| Einzelne Übung | Aufgabe | „Bordkarte“ |
| Mathe-Bereich | Gebiet | „Kontinent“ (das Gebiet liegt auf einem Erdteil) |
| Lücke aus einer früheren Klasse | Rückreise (bleibt) | – |

Das Flug-Bild darf bleiben: „Einsteigen“, „Gelandet“ sind gute Zustände.

---

## 5. Vorschläge mit Ort im Code

| Nr. | Vorschlag | Ort | Aufwand |
|---|---|---|---|
| U1 | Stempel-Band richtig zählen (alle Lernkarten aller Themen des Ortes) oder ersetzen durch „Rom: 1 von 5 Themen“ | `lernAbflugtafel` | klein |
| U2 | Mein Weg und Merkheft: Themenname statt Ortsname; „Karte 4 von 8“ statt „Etappe 4/8“ | `viewWeg`, `viewMerkheft` | klein |
| U3 | „Kommt noch“: gleiche Einteilung wie die Abflugtafel (`lernReiseDaten`: jetzt / früher / später); Orte ohne Klasse nur unter „Später/Extras“ | `viewWeg` | klein |
| U4 | Menü im Reisepass richtig markieren (`'reisepass'`) | `viewReisepass` | klein |
| U5 | Im Thema nur die eigene Schulart und Klasse („Gymnasium · Klasse 5“) | `lernThemaSeite` Kopf | klein |
| U6 | Ein Fortschrittsmaß oben auf Heute („Klasse 5: 2 von 14 Themen“), die anderen Zahlen in den Reisepass | `lernAbflugtafel` | klein |
| U7 | „Gerade dran“ = das aktuelle Thema + „als Nächstes“ (die nächsten 2–3); Rest eingeklappt | `viewWeg`, `lernAbflugtafel` | mittel |
| U8 | Rückreise erklären („Kurz zurück nach Delhi: Lineare Gleichungen sitzen noch nicht ganz“) | `lernAbflugtafel` | klein |
| U9 | Merkheft nur mit geschafften Lernkarten, Gliederung Gebiet → Thema; Sprung aus Mein Weg zum Thema | `viewMerkheft`, `viewWeg` | mittel |
| U10 | Feste Leiste unten (4 Einträge) in beiden Designs, ≡ entfällt; Gestaltung und Abmelden nur für Eltern sichtbar oder unter „Einstellungen“ | `lernRahmen`, `viewReisepass` | mittel |
| U11 | Weltkarte als Ansicht in Mein Weg, nur Orte der eigenen Klasse hervorgehoben; Antarktis mit Karte (eigener Ausschnitt um den Südpol) | `viewWeltkarte`, `lernKarte` | mittel |
| U12 | Ort-Klasse und Themen-Klasse angleichen (13 Orte), Reihenfolge der Themen innerhalb eines Ortes nach Lehrplan (heute nach Datenbank-ID) | Daten (`schule.block`, Einheiten), Entscheidung der Nutzer/Haupt-Chat | mittel |
| U13 | Startseite entschlacken: „Später (53)“ in Mein Weg; Abstände der eingeklappten Gruppen | `lernAbflugtafel`, `style.css` | klein |

**Reihenfolge:**
1. Zuerst U1–U6 und U8. Das sind kleine Korrekturen, die falsche oder verwirrende Anzeigen beheben.
2. Danach U7, U9 und U13.
3. Zuletzt U10, U11 und U12, die den Aufbau umstellen. U10/U11 vorher als klickbaren Entwurf zeigen lassen.

## 6. Offen

- Die Reisepläne der Testkinder sind erfunden. Echte Pläne mit weniger Orten machen B5/B14 kleiner, B1–B4 bleiben.
- Zwei ältere Themen (Natürliche Zahlen, Teilbarkeit) stehen nicht in `inhalte/themenliste.json`. Ihre Lernkarten sind im Rundgang durch Nachbarthemen ersetzt (nur Merkheft-Inhalt betroffen).
- Nicht mit den Kindern ausprobiert. Vorschlag: beiden Kindern drei Fragen stellen und zusehen, wohin sie tippen: „Wie weit bist du in Klasse X?“, „Was kommt nach diesem Thema?“, „Wo findest du nochmal, wie Punkt vor Strich ging?“.

---

## 7. Auswahl der Nutzer (2026-11-16)

| Punkt | Gewählt |
|---|---|
| 1 Navigation | **Heute lassen** (Menü ≡) |
| 2 Startseite | offen – Wunsch: Stand je Schulart (Gymnasium, Realschule, IB) und Klasse sichtbar machen, für Kinder, Eltern und Lehrer |
| 3 Fortschritt | offen – wie 2 |
| 4 Mein Weg | **B – nach Gebieten** (Kontinenten) |
| 5 Weltkarte | **A – Ansicht in „Mein Weg“** (nur eigene Klasse, Antarktis von oben) |
| 6 Stempel | **A – Ort = eine Klasse, Stempel je Ort** (13 Orte umziehen, siehe B8) |
| 7 Merkheft | **A – Gebiet → Thema → Lernkarte**, nur Geschafftes |
| 8 Wörter | **B – Reisewörter durchgehend** (Flug = Thema, Etappe = Lernkarte, Bordkarte = Aufgabe, Kontinent = Gebiet) |
| 9 Andere Klassen | Heute lassen (noch unentschieden) |
| 10 Rückreise | **A – eigene Karte „Kurz zurück“** mit Grund |

Zu 2/3: Entwürfe „Stand über Schularten“ (Linienplan, Bordkarten, Höhenmesser; Startseiten-Zeile; Eltern: Lehrplan-Landkarte, Schulwechsel-Check, beide Kinder auf einen Blick) liegen der Nutzer zur Auswahl vor. Grundlage ist die Zuordnung Thema → Klasse je Schulart in `inhalte/themenliste.json` (`klasse.gym_by/rs_by/ib_myp`).

### 7.1 Stand über Schularten (Auswahl 2026-11-16)

- **Startseite:** drei Mini-Linien oben (GYM · RS · IB MYP mit Klasse, Balken, gelandet/gesamt). Antippen öffnet den Stand.
- **Kind: Kombination vom Überblick bis ins Detail:**
  1. Ebene 1: die drei Mini-Linien und der Linienplan. Drei Linien, Haltestellen = Klassen, nach Alter ausgerichtet (MYP 1 ≈ Klasse 6), Ring je Haltestelle, „DU“ an der eigenen Stufe.
  2. Ebene 2 (Haltestelle antippen): Bordkarte der Klasse mit Fortschritt je Kontinent; ‹ › blättert durch die Klassen.
  3. Ebene 3 (Kontinent antippen): die Flüge, jeweils mit „zählt auch für …“.
- **Eltern/Lehrer: Kombination aus Lehrplan-Landkarte und Schulwechsel-Check:**
  1. Ebene 1: beide Kinder × drei Schularten.
  2. Ebene 2: Landkarte (Kontinente × Klassen) mit Schalter „Einstieg prüfen: Klasse X“. Die Klassen ab dem Ziel werden ausgegraut; dazu kommen Ampel und Liste der fehlenden Flüge.
  3. Ebene 3: die Flüge eines Feldes mit dem Stand der Etappen.
- **Entwurf:** klickbare Seite „Wo stehe ich? – kombinierter Entwurf“ (Artifact). Die Rechenlogik dort: Für eine Schulart und Klasse gelten alle Themen mit `klasse.<schulart> = Klasse`. Ein Thema gilt als gelandet, wenn alle seine Lernkarten sitzen bzw. der Test bestanden ist.
- **Voraussetzung:** Die Klassen-Zuordnung muss stimmen (B8, Nachtrag), sonst sind Stand und Einstiegs-Check falsch.
