# Postfach lehrplan-lb (Bau-Auftrag LB, Paket LB-4)

Neueste Meldung oben.

## 2026-11-21 – MELDUNG Runde 30 c: harte Verbindungen ohne neue Reise-Sperren

Grundlage ist `lernen-app` d463182a. Die Datenbank habe ich nur gelesen, die Migration auf der echten Datenbank **nicht ausgeführt**. Einzelheiten stehen im Bericht `inhalte/pruefung/lehrplan/runde30.md`, Abschnitt 0c.

- **Ursache:** Jede harte Verbindung zwischen zwei Orten ist über `schule.v_ort_visum` eine Reise-Sperre in `schule.reiseoptionen`. Meine Aussage „Plan-Folgen: keine“ war falsch.
- **38 von 39 neuen harten Verbindungen mit neuer Sperre sind jetzt `empfohlen`.** Hart bleibt nur 102 ← 30 (Potenzgesetze braucht Potenzen; Kette laut Auftrag). Das bringt eine neue Visum-Zeile: Ort „Terme umformen“ braucht „Potenzen“. Heute wirkt sie nicht, weil das Kind Klasse 8 beide Orte fertig hat und beim Kind Klasse 5 der Ort entfernt ist. **Entscheidung Sebastian:** hart lassen oder empfohlen.
- **`v_ort_visum`:** vorher 49, nachher 46 Zeilen. Vier Zeilen fallen durch die Löschungen aus 30 b weg; sie betreffen nur die Zusatz-Orte „Zinseszins“ und „Statistik vertieft“.
- **Reiseoptionen je Kind:** Für das Kind Klasse 5, das Kind Klasse 8 und das Testkind Klasse 7 sind vorher und nachher dieselben Orte wählbar und dieselben gesperrt. Die Tabellen dazu stehen im Bericht.
- **Rauchtest j:** vergleicht die Reiseoptionen aller Lernenden vor und nach der Migration und bricht bei jedem Unterschied ab.
- **Lokal auf Postgres 16 ausgeführt** (nachgebaute Tabellen, gelesene Daten):
  - Zwei Läufe hintereinander bestanden.
  - Gegenprobe mit 25 ← 18 hart: Rauchtest j greift, alles wird zurückgerollt.

FERTIG: Lehrplan Runde 30 c

## 2026-11-21 – MELDUNG Runde 30 b: Thema 12 zurückgenommen, aufgelöste Themen entkoppelt

Grundlage ist `lernen-app` 168a744b. Die Datenbank habe ich nur gelesen, die Migration **nicht ausgeführt**. Einzelheiten stehen im Bericht `inhalte/pruefung/lehrplan/runde30.md`, Abschnitt 0.

- **12 ohne Gymnasium-Klasse.** Die Reihenfolge Gym 9 ist wie vorher. Der Stoff steht im Flug 8, Etappe `reinquadratisch`.
- **Zehn aufgelöste Themen** (12, 27, 40, 41, 48, 72, 77, 78, 82, 83) mit `schule.einheit` abgeglichen: Nur diese zehn haben keine freigegebene Einheit. Für jedes nennt der Bericht, in welchem Flug und welcher Etappe der Stoff heute steht.
- **Gezielt gelöscht** in Abschnitt 3c der Migration, einzeln mit Kommentar: 12 Zeilen in `schule.voraussetzung`, nämlich 8←12, 12←68, 49←48, 74←48, 76←41, 72←67, 72←71, 77←32, 78←33, 82←21, 82←23 und 82←61.
- **Ersatz:** 8←68 (hart), 49←46 (empfohlen), 74←46 (empfohlen), 74←50 (hart), 76←28 (hart). Aus den neuen Verbindungen der Runde 30 sind 8 Zeilen gestrichen. Insgesamt bleiben 128 Verbindungen.
- **Neue Rauchtest-Regel i:** keine Verbindung von oder zu einem Thema ohne freigegebene Einheit. Erlaubt ist nur eine Begründung, die mit „Ausnahme:“ beginnt; das kommt derzeit nicht vor. Regel b gilt nur noch für freigegebene Themen. Alle Regeln sind per Skript nachgerechnet.
- **Plan-Folgen:** keine.
- **Befund:** Die aufgelösten Themen tragen weiter Klassen und Reihenfolgen für RS und IB. Das habe ich nicht geändert; die Matrix markiert sie mit `ohne_flug` (Teil B).
- **Lücke:** Vektoren (48) haben für RS 7 keinen freigegebenen Flug. Determinanten (74) nutzen Vektorkoordinaten.

FERTIG: Lehrplan Runde 30 b

## 2026-11-21 – MELDUNG Dreißigste Runde: Lehrplan-Prüfung Zuordnungen und Voraussetzungen

Grundlage ist `lernen-app` e0739529, mit dem Nachtrag des Gestalters. Die Datenbank habe ich nur gelesen, die Migration **nicht ausgeführt**. Aufgaben, Karten und App-Code sind unverändert. Bericht mit Quellen (LehrplanPLUS, abgerufen 21.11.2026) und Annahmen: `inhalte/pruefung/lehrplan/runde30.md`.

**Änderungen**
- **12 Reinquadratische Gleichungen → Gym 9**, M9 2, Stelle 4 vor 8. Beleg: Gym 9 M9 2.1. Ein Gymnasiast bekommt das Thema damit im Plan.
- **4 Formeln umstellen:** Lernbereich Gym berichtigt auf „M8 1 Funktion und Term“ (Beleg: Gym 8 M8 1). Die Reihenfolge bleibt.
- **32 Zuordnung und Funktion → IB MYP 3** vor 33. Grund: Regel „keine Voraussetzung in späterer Klasse“. Das ist eine Annahme. Kein Kind ist betroffen.
- **Ohne Gym-Klasse bleiben** 40, 77 und 13. 4 bleibt bei RS ohne Klasse; das ist eine Annahme, weil ich keine Fundstelle gefunden habe.
- **Klassen RS 7/8:** RS 7 mit 20 Themen ist stimmig. RS 8 mit 7 Themen ist dünn, weil Themen fehlen (Vierecke, Drehung, Baumdiagramm/Vierfeldertafel). Die Zuordnungen sind nicht falsch. Das sind nur Vorschläge.
- **Voraussetzungen:** 73 neue Verbindungen, insgesamt 143.
  - 7 Themen sind eigenständig.
  - Die Kette 30 → 102 → 29 und 102 → 103 ist enthalten.
- **„eigenständig“** steht in der neuen Spalte `schule.thema.eigenstaendig` (`text`, Begründung; `null` = nicht gekennzeichnet; gilt für alle Schularten) und in der Themenliste im Feld `eigenstaendig`. Einzelheiten stehen im Bericht in Abschnitt 3a. 102/103 sind laut Datenbank angelegt; die Migration verknüpft sie.
- **Migration:** `supabase/migrations/20261121_lehrplan_zuordnung_voraussetzungen.sql`.
  - Wiederholt ausführbar, ohne DROP/DELETE.
  - Rauchtest a–h, mit den drei Regeln des Gestalters.

**Folgen für Pläne (ohne Namen)**

Betroffen sind nur die Gym-Kinder: zwei echte und das Testkind.
1. 12 erscheint neu in Klasse 9.
2. In Gym 9 rücken 11 Themen je eine Stelle nach hinten. Ihre Reihenfolge untereinander bleibt gleich.
3. 4 hat einen anderen Lernbereich. Das betrifft möglicherweise eine Gruppierung nach Lernbereich (Annahme).

Die Voraussetzungen ändern keine Reihenfolge.

**Offen für Sebastian:** Soll 32 nach MYP 3 (umgesetzt) oder lieber 33 nach MYP 4? Vorschläge V1–V5 stehen im Bericht.

FERTIG: Lehrplan Runde 30

## 2026-11-20 06:10 – ENTSCHEIDUNG SEBASTIAN zum Auftragsentwurf Potenzgesetze

Sebastian hat am 20.11. im Chat `lehrplan-lb` entschieden:
1. **Klassen der neuen Flüge wie vorgeschlagen:**
   - Flug A „Potenzgesetze“: `gym_by` 7 · `rs_by` 7 · `ib_myp` 4.
   - Flug B „Potenzgesetze mit ganzzahligen Exponenten“: `gym_by` 8 · `rs_by` 7 · `ib_myp` 4.
2. **Die 19 Aufgaben** in „Fehler finden“ von `terme.potenzgesetze` (Gym 6), die ein Potenzgesetz voraussetzen, **ziehen nach Flug A um**. Aufgaben mit negativen Exponenten darunter gehen nach Flug B. In Gym 6 bleiben in „Fehler finden“ nur Aufgaben zu Potenzbegriff, Hoch 0 und negativem Exponenten. Reichen sie danach nicht mehr für Übung, Test, Korrektur und Sicherung, muss der Inhalts-Chat Aufgaben nachbauen.

Umsetzung weiter durch den Haupt-Chat (IDs, Ort, Lernstand) und einen Inhalts-Chat. In diesem Zweig ist nichts davon umgesetzt.

## 2026-11-20 06:00 – AUFTRAGSENTWURF: Potenzgesetze in zwei eigene Flüge teilen (von Sebastian gewählt)

Sebastian will die Potenzgesetze nach Klassen aufteilen. Der Lehrer soll sie dann gebündelt oder einzeln in den Plan nehmen können (LB-1/LB-5: Knöpfe je Flug, Sammelaktion für mehrere Flüge). **Nichts davon ist umgesetzt.** Neue Flüge brauchen `thema_id`, `block_id` und Ort aus der Datenbank. Die vergibt der Haupt-Chat; danach baut ein Inhalts-Chat. Alle Zahlen unten habe ich per Skript aus den Themendateien gezählt (Zweig `lernen-app`, Stand 752acf0).

**Heute (Tatsache):**

| Klasse Gym | Lehrplan | wo heute | Karten |
|---|---|---|---|
| 6 | M6 1.4 negative Exponenten | `terme.potenzgesetze` (id 30, Paris) | Was ist eine Potenz? · Negative Exponenten und Hoch 0 (Pflicht) · Fehler finden (Vertiefung; 19 von 41 Aufgaben nutzen schon Potenzgesetze) |
| 7 | M7 1.2 Potenzgesetze, natürliche Exponenten | 4 von 12 Karten in `terme.umformen` (id 29) | Gleiche Basis: malnehmen · Gleicher Exponent (Pflicht) · Gleiche Basis: teilen · Potenzgesetze geschickt nutzen (Vertiefung). Zusammen 168 Aufgaben, davon 22 mit negativen Exponenten. |
| 8 | M8 4 Potenzgesetze, ganzzahlige Exponenten | kein Flug | – |

**Vorschlag Flug A „Potenzgesetze“ (Gym 7, M7 1.2)** – aus `terme.umformen` herauslösen
- Die vier Karten oben umziehen. Das geht mit dem Werkzeug der Vierundzwanzigsten Runde (`inhalte/generatoren/_aufloesen.py`, Baustein `karte_her`). Pflicht und Vertiefung bleiben wie heute. Die 22 Aufgaben mit negativen Exponenten gehören zu Flug B; in Flug A durch Aufgaben mit natürlichen Exponenten ersetzen (auch die Testaufgabe von „Gleiche Basis: teilen“).
- `terme.umformen`: die vier Lernziele aus `bewertung` streichen. Danach bleiben 8 Karten (Termumformen, binomische Formeln).
- Klasse (Vorschlag, Sebastian entscheidet): `gym_by` 7 · `rs_by` 7 (R7 M7 1 Potenzen) · `ib_myp` 4 (IBG: Potenzgesetze = MYP 4–5 Standard).
- Reihenfolge Gym 7: hinter `terme.aufstellen`, vor `terme.umformen`, Lernbereich „M7 1 Terme mit Variablen“. Der Lehrplan M7 1.2 nennt die Potenzgesetze zuerst (G7). Realschule 7: Lernbereich „M7 1 Potenzen“, hinter `terme.potenzgesetze`.

**Vorschlag Flug B „Potenzgesetze mit ganzzahligen Exponenten“ (Gym 8, M8 4)** – neu bauen
- Lehrplan: „machen die Rechengesetze für Potenzen mit ganzzahligen Exponenten plausibel und wenden diese in einfachen Fällen an“ (G8, M8 4).
- Lernkarten (Vorschlag, Muster wie in der Achten/Zwanzigsten Runde):
  1. Warum die Gesetze auch für negative Exponenten gelten (Muster fortsetzen)
  2. Gleiche Basis malnehmen und teilen mit negativen Exponenten
  3. Gleicher Exponent und Potenz einer Potenz
  4. Terme mit Variablen und negativen Exponenten vereinfachen, auch als Bruchterm schreiben
  5. Fehler finden (Vertiefung)
- Die 22 Aufgaben aus Flug A sind Startbestand.
- Klasse (Vorschlag): `gym_by` 8 · `rs_by` 7 (R7 M7 1 enthält negative Exponenten und Potenzgesetze) · `ib_myp` 4.
- Reihenfolge Gym 8: im Lernbereich „M8 4 Bruchterme und Bruchgleichungen“ hinter `terme.bruchterme`, vor `gleichungen.bruch`. Der Lehrplan nennt die Potenzgesetze dort nach dem Rechnen mit Bruchtermen (G8).

**Folgen, die der Haupt-Chat lösen muss**
- **Lernstand der Kinder:** Fortschritt auf den vier umziehenden Lernzielen (`karte_stand`, Wiederholungen, Sterne) muss in der Datenbank auf Flug A umgehängt werden, ohne Verlust (W1–W7).
- **Reihenfolge Gym:** Die Nummern von `reihenfolge.gym_by` (Gym 7 und 8) verschieben sich. Die habe ich in LB-4 nicht anfassen dürfen.
- **`terme.potenzgesetze` (Gym 6):** Titel „Potenzen und Potenzgesetze“, `umfang` („… rationalen Exponenten, Potenzgesetze“) und der dritte Eintrag in `lehrplan_gym` an den echten Inhalt anpassen. Vorschlag Titel: „Potenzen und negative Exponenten“. Die 19 Aufgaben in „Fehler finden“, die Potenzgesetze nutzen, als Vertiefung lassen oder nach Flug A verschieben (Sebastian).
- Expeditionen verweisen auf keine der betroffenen Lernkarten (per Skript geprüft).

## 2026-11-20 – NACHPRÜFUNG LB-4 (auf Wunsch von Sebastian)

Die vier Lehrplan-Seiten, die vorhin fehlten, habe ich heute gelesen: Gymnasium 8 und 9, Realschule 8 und 9 (I). Dazu kamen die Seiten der Realschule 8–10 (II/III). Danach habe ich jede Zuordnung erneut gegen den Lehrplan geprüft. Ein Skript hat außerdem jeden Lernbereich gegen die Kürzel in `lehrplan_gym` und `lehrplan_andere` abgeglichen.

**Fehler, die ich korrigiert habe:**
1. **Bericht, Gruppe II/III, Klasse 9:** Dort stand, dass „Kreis“ in 9 II/III fehlt. **Das war falsch.** 9 II/III hat Lernbereich 4 „Kreis“ (R9-II). Ich hatte eine Lücke in einem ISB-Auszug als Fehlen gedeutet.
2. **Bericht, Gruppe II/III, Klasse 8:** Dort stand „Lineare Funktionen erst in Klasse 9“. **Zu grob.** 8 II/III hat Lernbereich 5 „Funktionen“ mit Ursprungsgeraden y = mx und linearen Graphen. Erst 9 II/III nennt y = mx + t ausdrücklich, dazu Parallelenscharen (R8-II, R9-II).
3. **`lehrplan_rs` von `abbildungen.aehnlichkeit`:** Dort stand „Ähnlichkeitssätze für Dreiecke“. Das stammte aus dem Verlags-Stoffverteilungsplan, nicht aus dem Lehrplan. Neu steht dort, was R9 nennt: Zahl mal Vektor, Parameterverfahren, Ähnlichkeit von Figuren prüfen.
4. **`lehrplan_rs` von `messen.koerper_darstellung`:** „Netze und Schrägbilder **von Würfel und Quader**“ war eine Einschränkung, die ich auf der Seite R5 nicht belegen konnte. Jetzt steht dort nur „Netze und Schrägbilder“.
5. **`lehrplan_ib` von `groessen.einheiten`:** „Uhrzeit und Zeitspannen“ stand unter dem Zweig Geometrie. Im Guide stehen Uhrzeit, Zeitzonen und Fahrpläne aber unter „Numerical and abstract reasoning“. Der Text ist jetzt korrigiert. Der Zweig des Themas bleibt Geometrie, weil sein Schwerpunkt das Umrechnen von Einheiten ist.

**Bisher Annahme, jetzt belegt** (die Zuordnung bleibt gleich): `zahlen.intervalle` und `gleichungen.ungleichungen` → M8 2 („lineare Ungleichungen … Intervallschreibweise“). `gleichungen.formeln` → M8 4. `gleichungen.potenz` → M9 5. `gleichungen.trig` → M9 7.2. `daten.boxplot` ist jetzt für **alle** RS-Klassen 7–10 geprüft: Quartile und Boxplot kommen nicht vor.

**Befund `terme.potenzgesetze` – berichtigt nach Blick in die Themendateien (20.11., 05:45):** Meine erste Fassung war im Kern falsch. Sie sagte, das Thema in Gym 6 enthalte den Stoff dreier Klassen. Die Themendateien zeigen etwas anderes:
- `terme.potenzgesetze` (Gym 6) hat nur drei Lernkarten: „Was ist eine Potenz?“, „Negative Exponenten und Hoch 0“ (beide Pflicht) und „Fehler bei Potenzen finden“ (Vertiefung). Das passt zu M6 1.4. Das Ziel der Datei sagt selbst: „Die Potenzgesetze folgen in Klasse 7 (Terme umformen).“ Nur Titel („Potenzen und Potenzgesetze“), `umfang` und der dritte Eintrag in `lehrplan_gym` versprechen mehr. Ein Teil der Vertiefungs-Aufgaben („Fehler finden“) nutzt schon Potenzgesetze mit natürlichen Exponenten.
- Die Potenzgesetze mit natürlichen Exponenten (M7 1.2) stehen in `terme.umformen` (Gym 7). Pflicht: „Gleiche Basis: malnehmen“, „Gleicher Exponent“. Vertiefung: „Gleiche Basis: teilen“, „Potenzgesetze geschickt nutzen“.
- Für Potenzgesetze mit ganzzahligen Exponenten (M8 4) gibt es **kein eigenes Thema**. 22 Aufgaben in den vier Potenzgesetz-Karten von `terme.umformen` (Gym 7) nutzen schon negative Exponenten (z. B. „y⁻³ · y⁻¹ = yᵏ“), darunter 1 Testaufgabe.
Die Aufteilung auf Klasse 6 und 7 besteht also schon. Es fehlt ein eigener Flug für M8 4, und die Potenzgesetze sind in Klasse 7 nicht vom Termumformen getrennt. Das Weitere entscheidet Sebastian.

**Geprüft und richtig:** alle Titel der Lernbereiche (Gym 5–10, RS 5–10) gegen die Lehrplan-Seiten. Zahl und Reihenfolge der Lernbereiche passen. Kein Thema hängt an einem Lernbereich, der seinen Kern nicht enthält. Die Selbstprüfung ist unverändert, das Prüfskript meldet 116 × OK. Es bleibt der bekannte Befund Gym 6.

**Was ungeprüft bleibt:**
- Das Abruf-Werkzeug fasst Seiten zusammen. Nummern, Titel und Stichworte stimmen über mehrere Quellen überein. Wörtlich nachgelesen ist nur, was oben in Anführungszeichen steht.
- IB: Die Spalten der Framework-Tabelle sind weiter nicht sicher zugeordnet. Deshalb ist die ganze IB-Reihenfolge Annahme.

## 2026-11-20 – FERTIG: LB-4

Zweig `lehrplan-lb` (von `lernen-app`, Commit 752acf0). Drei Commits, je Schulart einer: Gymnasium 2d24925 · Realschule 908bb12 · IB 34cbe67. Nur `inhalte/themenliste.json` geändert (+ dieser Bericht). Kein App-Code, keine Datenbank, kein Merge. Klassen nicht geändert.

### Kurz
- **Neu in `themenliste.json`:** `lernbereich.gym_by` (71 Themen), `reihenfolge.rs_by` + `lernbereich.rs_by` + `lehrplan_rs` (76 Themen), `reihenfolge.ib_myp` + `lernbereich.ib_myp` + `lehrplan_ib` (84 Themen). Jedes Thema mit Klasse in einer Schulart hat dort Reihenfolge und Lernbereich. Themen ohne Klasse in einer Schulart haben dort keinen Eintrag. `reihenfolge.gym_by`, `lehrplan_gym`, `lehrplan_andere` und `klasse` sind unverändert.
- **Eingefügt, nicht neu formatiert:** Ein Skript hat nur Zeilen eingefügt. Der Diff zeigt neue Zeilen und Kommas am Ende der jeweils vorherigen Zeile (69 so geänderte Zeilen). Geprüft per Skript: Alle alten Werte sind gleich, neu ist nur das Erwartete. `python3 -I tools/inhalt_pruefen.py --alle` ergibt 116 × OK, Rückgabewert 0.
- **Selbstprüfung:** Alles lückenlos und eindeutig. Realschule Klasse 7 hat 18 Themen. **Ein Befund:** Gymnasium Klasse 6 – der Lernbereich M6 1 wird durch die bestehende `reihenfolge.gym_by` unterbrochen (siehe unten, Vorschlag). Den Vorschlag habe ich nicht umgesetzt, weil der Auftrag die Gym-Reihenfolge sperrt.
- **Für Sebastian zu entscheiden:** die Gym-6-Reihenfolge (1 Punkt), 9 Vorschläge zu Klassen (Liste unten, nichts geändert) und ob IB-Überschriften englisch bleiben.

### So habe ich zugeordnet (Festlegungen)
- **Lernbereich = oberste Ebene des Lehrplans**, z. B. „M8 1 Funktion und Term“, „M9 7 Trigonometrie“ (nicht 7.1/7.2). So passt jede Überschrift zu einem zusammenhängenden Block. Die Unterkapitel stehen weiter in `lehrplan_gym`.
- **Realschule:** Die Überschrift hat dieselbe Form wie beim Gymnasium: „M7 2 Parallelverschiebung“. Im Lehrplan heißt sie „M7 Lernbereich 2: Parallelverschiebung“. Ab Klasse 7 gilt **Gruppe I** (Wahlpflichtfächergruppe I). Die Reihenfolge folgt der Nummer des Lernbereichs. **Die Reihenfolge innerhalb eines Lernbereichs gibt der Lehrplan nicht vor.** Ich habe sie nach der Reihenfolge der Stichworte im Lehrplan und nach den Voraussetzungen der Etappen gesetzt (Annahme). Wo eine Etappe Stoff eines späteren Lernbereichs braucht, steht das in der Spalte „Beleg“.
- **IB:** Das MYP schreibt **weder Jahr noch Reihenfolge** vor. Der Guide gliedert in vier Zweige und in Stufen (MYP 1–3, MYP 4–5 Standard/Extended, Enrichment). Ich habe so festgelegt:
  - `lernbereich.ib_myp` = „MYP <Jahr> <Zweig>“. Der Zweig steht englisch wie im Guide, dahinter auf Deutsch, z. B. „MYP 4 Thinking with models (Funktionen und Modelle)“.
  - `reihenfolge.ib_myp` folgt den Zweigen in der Reihenfolge des Guides (Zahl/Algebra → Modelle → Geometrie → Daten). Innerhalb eines Zweigs habe ich nach Voraussetzungen sortiert. Die **ganze IB-Reihenfolge ist Annahme**.
  - Jeder Eintrag in `lehrplan_ib` beginnt mit der Stufe im Framework, z. B. „MYP 4–5 Extended: …“.
- **`lehrplan_rs` / `lehrplan_ib`:** kurz und in eigenen Worten. „kein Beleg“ und „Annahme“ stehen dort, wo der Lehrplan das Thema nicht (vollständig) nennt.
- **Die 10 aufgelösten Themen** (u. a. `groessen.verhaeltnisse`, `mengen.grundbegriffe`, `funktionen.scharen`, `funktionen.folgen`, `abbildungen.vektoren`) stehen noch mit Klasse in der Themenliste. Sie haben deshalb auch Einträge bekommen, sonst wären die Nummern lückenhaft. Die App zeigt sie laut Auftrag nirgends. Die Nummern bleiben trotzdem gültig, weil die App ohnehin nur sortiert.

### Selbstprüfung (Skript, Ausgabe unverändert)
```
gym_by  Kl.  5: 14 Themen · Nummern 1–14 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
gym_by  Kl.  6: 11 Themen · Nummern 1–11 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: NEIN (3 Überschriften)
gym_by  Kl.  7:  9 Themen · Nummern 1–9 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (5 Überschriften)
gym_by  Kl.  8: 14 Themen · Nummern 1–14 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (7 Überschriften)
gym_by  Kl.  9: 14 Themen · Nummern 1–14 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (7 Überschriften)
gym_by  Kl. 10:  9 Themen · Nummern 1–9 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (5 Überschriften)
rs_by   Kl.  5: 12 Themen · Nummern 1–12 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (6 Überschriften)
rs_by   Kl.  6: 11 Themen · Nummern 1–11 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (6 Überschriften)
rs_by   Kl.  7: 18 Themen · Nummern 1–18 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (7 Überschriften)
rs_by   Kl.  8:  7 Themen · Nummern 1–7 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
rs_by   Kl.  9: 17 Themen · Nummern 1–17 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (8 Überschriften)
rs_by   Kl. 10: 11 Themen · Nummern 1–11 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (5 Überschriften)
ib_myp  Kl.  1: 15 Themen · Nummern 1–15 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (3 Überschriften)
ib_myp  Kl.  2: 12 Themen · Nummern 1–12 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (3 Überschriften)
ib_myp  Kl.  3: 12 Themen · Nummern 1–12 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
ib_myp  Kl.  4: 27 Themen · Nummern 1–27 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
ib_myp  Kl.  5: 18 Themen · Nummern 1–18 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
Realschule Klasse 7: 18 Themen (soll 18)
FEHLER:
- gym_by 6: Lernbereich mehrfach unterbrochen: ['M6 1 Rationale Zahlen', 'M6 2 Flächeninhalt und Volumen', 'M6 1 Rationale Zahlen', 'M6 3 Prozentrechnung, Daten und Diagramme']
```

### Befund: Gymnasium Klasse 6 – Lernbereich M6 1 unterbrochen
Die heutige `reihenfolge.gym_by`: 1 `bruch.brueche` · 2 `bruch.dezimal` · 3 `bruch.rechnen` (M6 1) · 4 `messen.flaechen_vielecke` · 5 `messen.volumen` (M6 2) · 6 `zahlen.potenzen_zehner` · 7 `terme.potenzgesetze` (M6 1) · 8–11 (M6 3). Die Überschrift „M6 1 Rationale Zahlen“ käme also zweimal.
**Vorschlag (nicht umgesetzt):** `zahlen.potenzen_zehner` → 4, `terme.potenzgesetze` → 5, `messen.flaechen_vielecke` → 6, `messen.volumen` → 7. Das passt zum Lehrplan, weil negative Exponenten in M6 1.4 stehen und M6 2 danach kommt. Quelle: G6, GSP.

### Vorschläge zu Klassen (nichts geändert)
| Thema | Schulart | heute | Vorschlag | Quelle / Grund |
|---|---|---|---|---|
| `daten.boxplot` | RS | 7 | keine RS-Klasse oder Vertiefung | R7, M7 8: Mittelwert, Zentralwert, Modalwert, Spannweite. Quartile und Boxplot kommen in RS 7 (Gruppe I) nicht vor. Auch in R8 (M8 7), R9 (M9 8) und R10 (M10 5) nicht enthalten (Nachprüfung 20.11.). |
| `funktionen.gebrochen` | RS | – | 10 (Annahme) | R10, M10 3: Potenzfunktionen y = a(x + b)^c + d mit Asymptoten. Die Hyperbel ist der Fall c = −1. |
| `funktionen.linear` | IB | 3 | 4 | IBG: „Thinking with models“ gilt für MYP 1–3 als nicht altersgemäß; lineare Funktionen sind Standard (MYP 4–5). Das Lehrwerk Haese hat sie in Jahr 3 (Bericht vom 17.11.). |
| `stochastik.kombinatorik` | IB | 2 | 5 oder keine IB-Klasse | IBG: Zählprinzipien, Permutationen und Fakultät stehen nur im Enrichment. |
| `mengen.grundbegriffe` | IB | 3 | 4 | IBG: Mengen bis zu drei Mengen = Extended (MYP 4–5). Das Thema ist aufgelöst – nur von Belang, wenn es zurückkommt. |
| `stochastik.simulation` | IB | 2 | 4 (Annahme) | IBG: Theoretische und experimentelle Wahrscheinlichkeit stehen unter Standard (MYP 4–5). Die Spalte war in der Abschrift aber nicht sicher lesbar. |
| `raum.schraegbilder` | IB | 4 | 5 oder keine IB-Klasse | IBG: Dreidimensionale Koordinatengeometrie steht nur im Enrichment. Für Rotationskörper und windschiefe Geraden gibt es keinen Beleg. |
| `abbildungen.matrizen` | IB | 5 | keine IB-Klasse (Annahme) | IBG 2020: Matrizen nicht gefunden, Vektoren nur Enrichment. |
| `sonder.logik` | IB | 4 | keine IB-Klasse (Annahme) | IBG: Aussagenlogik nicht gefunden. |

Hinweis zu IB: In der Abschrift des Framework stehen Terme und Gleichungen (Algebra) unter „MYP 4–5 Standard“. Das betrifft `terme.aufstellen`, `gleichungen.einfach` (MYP 1) und `gleichungen.linear` (MYP 2). Das Werkzeug warnt selbst, dass die Spalten der Tabelle verschoben sein können. Ich schlage deshalb keine Änderung vor und habe die Stufe als „Annahme“ markiert. Vor einer Entscheidung bitte im gedruckten Guide (S. 23–24) nachsehen.

### Abweichungen der Gruppe II/III (Realschule, nur Hinweis; am 20.11. geprüft)
Die App hat nur ein Feld `rs_by`. Alle Angaben oben gelten für Gruppe I. Die Lernbereiche der Gruppe II/III:
- **8 (II/III):** 1 Dreiecke und Vierecke · 2 Raumgeometrie (Schrägbilder von Prismen und Pyramiden) · 3 Terme und Gleichungen · 4 Bruchterme und Bruchgleichungen · 5 Funktionen (Ursprungsgeraden y = mx, lineare Graphen) · 6 Daten und Zufall (R8-II).
- **9 (II/III):** 1 Reelle Zahlen · 2 Zentrische Streckung · 3 Rechtwinklige Dreiecke · 4 Kreis · 5 Lineare Funktionen (y = mx + t, Parallelenscharen, Determinanten) · 6 Systeme linearer Gleichungen · 7 Daten und Zufall (R9-II).
- **10 (II/III):** 1 Trigonometrie · 2 Raumgeometrie · 3 Exponentialfunktionen, Logarithmen · 4 Quadratische Funktionen und quadratische Gleichungen · 5 Daten und Zufall. Abbildungen, Potenzfunktionen, rationale Exponenten, Umkehr- und Logarithmusfunktionen kommen nicht vor (R10-II).

Was das für die Themen heißt (Gruppe I → II/III):
- `geometrie.konstruktion`: 7 → 8
- `raum.schraegbilder`: 8 → Schrägbilder 8, Axialschnitte 10, 3D-Koordinaten nicht enthalten
- `funktionen.linear`: 8 → 9
- `funktionen.scharen`: 8 → 9
- `abbildungen.vektoren`, `abbildungen.determinanten2`: 7 → 7, Determinanten auch 9
- `messen.prisma_zylinder`, `raum.pyramide_kegel_kugel`: 9 → 10
- `funktionen.quadratisch`, `funktionen.transformation`, `gleichungen.quadratisch`: 9 → 10
- `gleichungen.wurzel`: kein Beleg in II/III
- In II/III **nicht enthalten:** `abbildungen.matrizen`, `zahlen.rationale_exponenten`, `gleichungen.potenz`, `funktionen.potenz`, `funktionen.umkehr`. Von `funktionen.exponential_log` nur der Exponentialteil.

Die II/III-Zeilen zu `abbildungen.vektoren` und `gleichungen.wurzel` stützen sich auf den Bericht vom 17.11.; R7-II habe ich heute nicht gelesen.

### Grenzen (bitte lesen)
- Das Abruf-Werkzeug **fasst Seiten zusammen**. Nummern, Titel und Stichworte der Lernbereiche stimmen und decken sich mit mehreren Quellen. Nicht jeder Satz ist wörtlich nachgeprüft.
- Bei der ersten Fassung fehlten die Seiten Gym 8/9 und RS 8/9 (I). Ersatz waren damals ISB-Auszüge und die Stoffverteilungspläne Mathe.Logo. Bei der Nachprüfung habe ich alle vier Seiten gelesen; die Tabellen stützen sich jetzt darauf. Die Zuordnungen sind dadurch nicht anders geworden.
- IB: Der Guide liegt nur als Kopie einer Schule vor (wottonhouseschool.co.uk). Die Spalten der Framework-Tabelle sind laut Werkzeug „stellenweise unsicher“ zugeordnet, vor allem bei „Thinking with models“ und „Spatial reasoning“.

### Tabellen je Schulart und Klasse
Spalte „Beleg“: **belegt** = der Inhalt steht in den Stichworten des Lernbereichs der Quelle. **Annahme** = nicht wörtlich gefunden oder Zuordnung gewählt. Die Reihenfolge innerhalb eines Lernbereichs ist immer Annahme (siehe oben).

### Gymnasium (nur `lernbereich.gym_by`; `reihenfolge.gym_by` unverändert)

**Gymnasium Klasse 5** – Quelle G5 (+ GSP für die Titel)

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `zahlen.natuerlich` | M5 1 Natürliche und ganze Zahlen – Addition und Subtraktion | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 2 | `zahlen.ganz` | M5 1 Natürliche und ganze Zahlen – Addition und Subtraktion | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 3 | `geometrie.grundbegriffe` | M5 2 Geometrische Figuren und Lagebeziehungen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 4 | `geometrie.ortslinien` | M5 2 Geometrische Figuren und Lagebeziehungen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 5 | `geometrie.winkel` | M5 2 Geometrische Figuren und Lagebeziehungen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 6 | `zahlen.rechengesetze` | M5 3 Natürliche und ganze Zahlen – Multiplikation und Division | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 7 | `zahlen.potenzen_basis` | M5 3 Natürliche und ganze Zahlen – Multiplikation und Division | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 8 | `zahlen.teilbarkeit` | M5 3 Natürliche und ganze Zahlen – Multiplikation und Division | belegt (Teilbarkeitsregeln, Primfaktorzerlegung in M5 3.1) – bisher Annahme |
| 9 | `stochastik.kombinatorik` | M5 3 Natürliche und ganze Zahlen – Multiplikation und Division | belegt (Zählprinzip, Baumdiagramm in M5 3.1) – bisher Annahme |
| 10 | `gleichungen.einfach` | M5 3 Natürliche und ganze Zahlen – Multiplikation und Division | belegt: a + x = b in M5 1.2, a · x = b in M5 3.1 – zu M5 3 gesetzt |
| 11 | `groessen.einheiten` | M5 4 Größen und ihre Einheiten | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 12 | `groessen.proportional` | M5 4 Größen und ihre Einheiten | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 13 | `messen.flaechen` | M5 4 Größen und ihre Einheiten | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 14 | `messen.koerper_berechnung` | M5 4 Größen und ihre Einheiten | belegt für Oberfläche (M5 4.2); Volumen steht erst in M6 2.2 |

**Gymnasium Klasse 6** – Quelle G6 (+ GSP für die Titel)

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `bruch.brueche` | M6 1 Rationale Zahlen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 2 | `bruch.dezimal` | M6 1 Rationale Zahlen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 3 | `bruch.rechnen` | M6 1 Rationale Zahlen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 4 | `messen.flaechen_vielecke` | M6 2 Flächeninhalt und Volumen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 5 | `messen.volumen` | M6 2 Flächeninhalt und Volumen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 6 | `zahlen.potenzen_zehner` | M6 1 Rationale Zahlen | belegt (negative Exponenten in M6 1.4) |
| 7 | `terme.potenzgesetze` | M6 1 Rationale Zahlen | belegt für negative Exponenten (M6 1.4); Potenzgesetze mit ganzzahligen Exponenten stehen erst in M8 4 (siehe Befund) |
| 8 | `bruch.prozent` | M6 3 Prozentrechnung, Daten und Diagramme | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 9 | `finanzen.zinsen` | M6 3 Prozentrechnung, Daten und Diagramme | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 10 | `daten.darstellen` | M6 3 Prozentrechnung, Daten und Diagramme | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 11 | `daten.kennwerte` | M6 3 Prozentrechnung, Daten und Diagramme | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |

**Gymnasium Klasse 7** – Quelle G7 (+ GSP für die Titel)

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `terme.aufstellen` | M7 1 Terme mit Variablen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 2 | `terme.umformen` | M7 1 Terme mit Variablen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 3 | `abbildungen.kongruenz` | M7 2 Geometrische Figuren: Symmetrie und Winkel | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 4 | `geometrie.winkelsaetze` | M7 2 Geometrische Figuren: Symmetrie und Winkel | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 5 | `gleichungen.linear` | M7 3 Lineare Gleichungen und Vertiefung der Prozentrechnung | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 6 | `bruch.prozent_grundwert` | M7 3 Lineare Gleichungen und Vertiefung der Prozentrechnung | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 7 | `daten.boxplot` | M7 4 Kenngrößen von Daten | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 8 | `geometrie.konstruktion` | M7 5 Kongruenz, besondere Dreiecke und Dreieckskonstruktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 9 | `geometrie.kreis` | M7 5 Kongruenz, besondere Dreiecke und Dreieckskonstruktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |

**Gymnasium Klasse 8** – Quelle G8 (+ GSP für die Titel)

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `funktionen.grundbegriffe` | M8 1 Funktion und Term | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 2 | `funktionen.linear` | M8 2 Lineare Funktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 3 | `zahlen.intervalle` | M8 2 Lineare Funktionen | belegt (M8 2: Ungleichungen … in Intervallschreibweise) – bisher Annahme |
| 4 | `gleichungen.ungleichungen` | M8 2 Lineare Funktionen | belegt (M8 2: lineare Ungleichungen graphisch und rechnerisch) – bisher Annahme |
| 5 | `groessen.indirekt` | M8 3 Elementare gebrochen-rationale Funktionen | belegt (y = a/x „indirekt proportional“ in M8 3) |
| 6 | `funktionen.gebrochen` | M8 3 Elementare gebrochen-rationale Funktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 7 | `terme.bruchterme` | M8 4 Bruchterme und Bruchgleichungen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 8 | `gleichungen.bruch` | M8 4 Bruchterme und Bruchgleichungen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 9 | `gleichungen.formeln` | M8 4 Bruchterme und Bruchgleichungen | belegt (M8 4: Formeln nach einer Variablen auflösen) – bisher Annahme |
| 10 | `stochastik.grundbegriffe` | M8 5 Laplace-Experimente | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 11 | `gleichungen.lgs2` | M8 6 Lineare Gleichungssysteme | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 12 | `messen.kreisberechnung` | M8 7 Kreis und Zylinder | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 13 | `messen.koerper_darstellung` | M8 7 Kreis und Zylinder | belegt (Schrägbilder, Netze von Prismen/Zylindern in M8 7) |
| 14 | `messen.prisma_zylinder` | M8 7 Kreis und Zylinder | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |

**Gymnasium Klasse 9** – Quelle G9 (+ GSP für die Titel)

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `zahlen.wurzeln_basis` | M9 1 Quadratwurzeln | belegt M9 1; die Etappe zur allgemeinen Wurzel gehört zu M9 5 |
| 2 | `zahlen.reell` | M9 1 Quadratwurzeln | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 3 | `funktionen.quadratisch` | M9 2 Quadratische Funktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 4 | `gleichungen.quadratisch` | M9 2 Quadratische Funktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 5 | `gleichungen.lgs3` | M9 2 Quadratische Funktionen | belegt (M9 2.2) |
| 6 | `stochastik.verknuepft` | M9 3 Wahrscheinlichkeit verknüpfter Ereignisse | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 7 | `abbildungen.aehnlichkeit` | M9 4 Ähnlichkeit und Strahlensatz | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 8 | `zahlen.rationale_exponenten` | M9 5 Potenzfunktionen mit natürlichen Exponenten und Erweiterung des Potenzbegriffs | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 9 | `funktionen.potenz` | M9 5 Potenzfunktionen mit natürlichen Exponenten und Erweiterung des Potenzbegriffs | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 10 | `gleichungen.potenz` | M9 5 Potenzfunktionen mit natürlichen Exponenten und Erweiterung des Potenzbegriffs | belegt (M9 5: Gleichungen xⁿ = c) |
| 11 | `trigo.pythagoras` | M9 6 Satz des Pythagoras | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 12 | `trigo.rechtwinklig` | M9 7 Trigonometrie | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 13 | `trigo.allgemein` | M9 7 Trigonometrie | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 14 | `gleichungen.trig` | M9 7 Trigonometrie | belegt (M9 7.2: Winkel zu gegebenem Sinus- oder Kosinuswert) |

**Gymnasium Klasse 10** – Quelle G10 (+ GSP für die Titel)

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `funktionen.exponential_log` | M10 1 Exponentielles Wachstum und Logarithmus | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 2 | `gleichungen.exponential` | M10 1 Exponentielles Wachstum und Logarithmus | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 3 | `stochastik.mehrstufig` | M10 2 Zusammengesetzte Zufallsexperimente und stochastische Simulationen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 4 | `stochastik.simulation` | M10 2 Zusammengesetzte Zufallsexperimente und stochastische Simulationen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 5 | `funktionen.trig` | M10 3 Sinus- und Kosinusfunktion | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 6 | `funktionen.ganzrational` | M10 4 Ganzrationale Funktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 7 | `gleichungen.polynom` | M10 4 Ganzrationale Funktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 8 | `raum.schraegbilder` | M10 5 Fortführung der Raumgeometrie | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 9 | `raum.pyramide_kegel_kugel` | M10 5 Fortführung der Raumgeometrie | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |

### Realschule (Gruppe I ab Klasse 7)

**Realschule Klasse 5** – Quelle R5

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `zahlen.natuerlich` | M5 1 Natürliche Zahlen | belegt |
| 2 | `zahlen.rechengesetze` | M5 1 Natürliche Zahlen | belegt M5 1.3; Etappen zu ·/: ganzer Zahlen = M5 2 (kommt im Lehrplan danach) |
| 3 | `zahlen.potenzen_basis` | M5 1 Natürliche Zahlen | belegt |
| 4 | `zahlen.teilbarkeit` | M5 1 Natürliche Zahlen | belegt |
| 5 | `stochastik.kombinatorik` | M5 1 Natürliche Zahlen | belegt |
| 6 | `zahlen.ganz` | M5 2 Ganze Zahlen | belegt |
| 7 | `geometrie.grundbegriffe` | M5 3 Geometrische Grundvorstellungen und Grundbegriffe | belegt |
| 8 | `geometrie.winkel` | M5 3 Geometrische Grundvorstellungen und Grundbegriffe | belegt |
| 9 | `messen.koerper_darstellung` | M5 3 Geometrische Grundvorstellungen und Grundbegriffe | belegt M5 3; Etappen zu Prismen-Netzen gehen darüber hinaus |
| 10 | `groessen.einheiten` | M5 4 Größen | belegt |
| 11 | `messen.flaechen` | M5 5 Umfang und Flächeninhalt ebener Figuren | belegt |
| 12 | `daten.darstellen` | M5 6 Auswertung von Daten | belegt |

**Realschule Klasse 6** – Quelle R6

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `bruch.brueche` | M6 1 Rationale Zahlen | belegt |
| 2 | `bruch.dezimal` | M6 1 Rationale Zahlen | belegt |
| 3 | `bruch.rechnen` | M6 1 Rationale Zahlen | belegt |
| 4 | `abbildungen.kongruenz` | M6 2 Achsenspiegelung und Symmetrie | belegt |
| 5 | `messen.flaechen_vielecke` | M6 3 Flächeninhalt ebener Figuren | belegt |
| 6 | `messen.volumen` | M6 4 Raumgeometrie | belegt |
| 7 | `messen.koerper_berechnung` | M6 4 Raumgeometrie | Annahme: Oberfläche = M6 3, Volumen = M6 4 – an das Ende von M6 4 gesetzt |
| 8 | `terme.aufstellen` | M6 5 Terme und Gleichungen | belegt |
| 9 | `gleichungen.einfach` | M6 5 Terme und Gleichungen | belegt |
| 10 | `groessen.proportional` | M6 6 Direkte Proportionalität | belegt |
| 11 | `bruch.prozent` | M6 6 Direkte Proportionalität | belegt |

**Realschule Klasse 7** – Quelle R7

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `terme.potenzgesetze` | M7 1 Potenzen | belegt |
| 2 | `zahlen.potenzen_zehner` | M7 1 Potenzen | belegt |
| 3 | `abbildungen.vektoren` | M7 2 Parallelverschiebung | belegt |
| 4 | `abbildungen.determinanten2` | M7 2 Parallelverschiebung | belegt |
| 5 | `geometrie.winkelsaetze` | M7 2 Parallelverschiebung | belegt |
| 6 | `geometrie.konstruktion` | M7 3 Dreiecke | belegt |
| 7 | `geometrie.ortslinien` | M7 5 Geometrische Ortslinien und Ortsbereiche | belegt |
| 8 | `geometrie.kreis` | M7 5 Geometrische Ortslinien und Ortsbereiche | belegt |
| 9 | `terme.umformen` | M7 6 Terme, Gleichungen und Ungleichungen | belegt (Terme vereinfachen); Etappe binomische Formeln = M8 4 |
| 10 | `gleichungen.linear` | M7 6 Terme, Gleichungen und Ungleichungen | belegt (ax + b = c); Etappen mit x auf beiden Seiten/Klammern = M8 4 |
| 11 | `zahlen.intervalle` | M7 6 Terme, Gleichungen und Ungleichungen | belegt |
| 12 | `gleichungen.ungleichungen` | M7 6 Terme, Gleichungen und Ungleichungen | belegt |
| 13 | `bruch.prozent_grundwert` | M7 7 Proportionalitäten | belegt |
| 14 | `finanzen.zinsen` | M7 7 Proportionalitäten | belegt |
| 15 | `groessen.indirekt` | M7 7 Proportionalitäten | belegt |
| 16 | `daten.kennwerte` | M7 8 Auswertung von Daten | belegt |
| 17 | `daten.boxplot` | M7 8 Auswertung von Daten | Annahme: Quartile/Boxplot weder in M7 8 noch in M8 7, M9 8, M10 5 |
| 18 | `daten.stichproben` | M7 8 Auswertung von Daten | belegt |

**Realschule Klasse 8** – Quelle R8

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `raum.schraegbilder` | M8 3 Raumgeometrie | belegt M8 3; Schrägbilder von Prismen/Pyramiden = M7 4 |
| 2 | `terme.quadratische_extreme` | M8 4 Terme, Gleichungen und Ungleichungen | belegt |
| 3 | `terme.bruchterme` | M8 5 Bruchterme und Bruchgleichungen | belegt |
| 4 | `gleichungen.bruch` | M8 5 Bruchterme und Bruchgleichungen | belegt |
| 5 | `funktionen.grundbegriffe` | M8 6 Funktionen | belegt |
| 6 | `funktionen.linear` | M8 6 Funktionen | belegt |
| 7 | `funktionen.scharen` | M8 6 Funktionen | teilweise: Parallelenscharen belegt (M8 6); Parabelscharen = M9 7 |

**Realschule Klasse 9** – Quelle R9

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `zahlen.wurzeln_basis` | M9 1 Reelle Zahlen | belegt |
| 2 | `zahlen.reell` | M9 1 Reelle Zahlen | belegt (M9 1); Heron-Verfahren steht nicht im RS-Lehrplan |
| 3 | `gleichungen.reinquadratisch` | M9 1 Reelle Zahlen | belegt |
| 4 | `abbildungen.aehnlichkeit` | M9 2 Zentrische Streckung | belegt (M9 2); Zahl mal Vektor und Parameterverfahren hat das Thema laut Bericht 17.11. nicht |
| 5 | `trigo.pythagoras` | M9 3 Rechtwinklige Dreiecke | belegt |
| 6 | `trigo.rechtwinklig` | M9 3 Rechtwinklige Dreiecke | belegt |
| 7 | `messen.kreisberechnung` | M9 4 Kreis | belegt |
| 8 | `messen.prisma_zylinder` | M9 5 Raumgeometrie | belegt |
| 9 | `raum.pyramide_kegel_kugel` | M9 5 Raumgeometrie | belegt |
| 10 | `gleichungen.lgs2` | M9 6 Systeme linearer Gleichungen | belegt |
| 11 | `funktionen.quadratisch` | M9 7 Quadratische Funktionen und quadratische Gleichungen | belegt |
| 12 | `funktionen.transformation` | M9 7 Quadratische Funktionen und quadratische Gleichungen | belegt (Parameter, Parabelscharen M9 7); andere Graphen = M10 2 |
| 13 | `gleichungen.quadratisch` | M9 7 Quadratische Funktionen und quadratische Gleichungen | belegt |
| 14 | `gleichungen.wurzel` | M9 7 Quadratische Funktionen und quadratische Gleichungen | belegt |
| 15 | `stochastik.grundbegriffe` | M9 8 Daten und Zufall | belegt |
| 16 | `stochastik.verknuepft` | M9 8 Daten und Zufall | teilweise: Ereignis/Gegenereignis belegt (M9 8); Additionssatz, bedingte WK, Vierfeldertafel nicht in M9 (Vierfeldertafel: M8 7, M5 6) |
| 17 | `stochastik.simulation` | M9 8 Daten und Zufall | belegt (Gesetz der großen Zahlen, Simulation); Monte-Carlo kein Beleg |

**Realschule Klasse 10** – Quelle R10

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `trigo.allgemein` | M10 1 Trigonometrie | belegt |
| 2 | `funktionen.trig` | M10 1 Trigonometrie | belegt |
| 3 | `gleichungen.trig` | M10 1 Trigonometrie | belegt |
| 4 | `abbildungen.matrizen` | M10 2 Abbildungen | belegt |
| 5 | `zahlen.rationale_exponenten` | M10 3 Potenzen und Potenzfunktionen | belegt |
| 6 | `gleichungen.potenz` | M10 3 Potenzen und Potenzfunktionen | Annahme: aus „n-te Wurzel“ (M10 3) |
| 7 | `funktionen.potenz` | M10 3 Potenzen und Potenzfunktionen | belegt |
| 8 | `funktionen.umkehr` | M10 3 Potenzen und Potenzfunktionen | belegt M10 3 (auch M10 4); eine Etappe braucht Exponentialfunktionen (M10 4) |
| 9 | `funktionen.exponential_log` | M10 4 Exponentialfunktionen, Logarithmen und Logarithmusfunktionen | belegt |
| 10 | `gleichungen.exponential` | M10 4 Exponentialfunktionen, Logarithmen und Logarithmusfunktionen | belegt |
| 11 | `stochastik.mehrstufig` | M10 5 Daten und Zufall | belegt |

### IB MYP (Jahr = Klasse − 5)

**MYP 1** – Quelle IBG (Framework S. 23–29), Zweige IBB

| Nr. | Thema | Zweig (Lernbereich) | Stufe im Framework |
|---|---|---|---|
| 1 | `zahlen.natuerlich` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 2 | `zahlen.rechengesetze` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 3 | `zahlen.potenzen_basis` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 4 | `zahlen.teilbarkeit` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 5 | `zahlen.wurzeln_basis` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 6 | `bruch.brueche` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 7 | `bruch.dezimal` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 8 | `bruch.prozent` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 9 | `terme.aufstellen` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 (Annahme) |
| 10 | `gleichungen.einfach` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 (Annahme) |
| 11 | `geometrie.grundbegriffe` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 12 | `geometrie.winkel` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 13 | `messen.flaechen` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 14 | `messen.koerper_berechnung` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 15 | `daten.darstellen` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 1–3 |

**MYP 2** – Quelle IBG (Framework S. 23–29), Zweige IBB

| Nr. | Thema | Zweig (Lernbereich) | Stufe im Framework |
|---|---|---|---|
| 1 | `zahlen.ganz` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 2 | `bruch.rechnen` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 3 | `gleichungen.linear` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 (Annahme) |
| 4 | `groessen.verhaeltnisse` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 5 | `groessen.proportional` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 6 | `groessen.einheiten` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 7 | `geometrie.winkelsaetze` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 8 | `daten.stichproben` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 1–3 |
| 9 | `daten.kennwerte` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 1–3 |
| 10 | `stochastik.grundbegriffe` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 1–3 / Standard |
| 11 | `stochastik.simulation` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Standard |
| 12 | `stochastik.kombinatorik` | Reasoning with data (Daten und Wahrscheinlichkeit) | Enrichment |

**MYP 3** – Quelle IBG (Framework S. 23–29), Zweige IBB

| Nr. | Thema | Zweig (Lernbereich) | Stufe im Framework |
|---|---|---|---|
| 1 | `terme.umformen` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard (Annahme) |
| 2 | `terme.potenzgesetze` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 3 | `bruch.prozent_grundwert` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 4 | `funktionen.linear` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Standard |
| 5 | `abbildungen.kongruenz` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 / Standard |
| 6 | `geometrie.konstruktion` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 4–5 Standard |
| 7 | `messen.kreisberechnung` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 8 | `messen.koerper_darstellung` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 9 | `raum.pyramide_kegel_kugel` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 / Extended |
| 10 | `abbildungen.aehnlichkeit` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 4–5 Standard |
| 11 | `trigo.pythagoras` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 4–5 Standard |
| 12 | `mengen.grundbegriffe` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Extended |

**MYP 4** – Quelle IBG (Framework S. 23–29), Zweige IBB

| Nr. | Thema | Zweig (Lernbereich) | Stufe im Framework |
|---|---|---|---|
| 1 | `zahlen.potenzen_zehner` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 2 | `zahlen.reell` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 3 | `zahlen.intervalle` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 4 | `gleichungen.ungleichungen` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 5 | `gleichungen.formeln` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 6 | `terme.bruchterme` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard (Annahme) |
| 7 | `gleichungen.bruch` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard (Annahme) |
| 8 | `groessen.indirekt` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 9 | `gleichungen.reinquadratisch` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 10 | `gleichungen.quadratisch` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 11 | `gleichungen.potenz` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard (Annahme) |
| 12 | `finanzen.zinsen` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 (Annahme) |
| 13 | `finanzen.zinseszins` | Numerical and abstract reasoning (Zahl und Algebra) | Annahme |
| 14 | `sonder.logik` | Numerical and abstract reasoning (Zahl und Algebra) | kein Beleg |
| 15 | `funktionen.grundbegriffe` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Standard / Extended |
| 16 | `gleichungen.lgs2` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Standard |
| 17 | `funktionen.quadratisch` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Standard |
| 18 | `funktionen.potenz` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Extended |
| 19 | `funktionen.gebrochen` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Extended |
| 20 | `sonder.graphentheorie` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Extended |
| 21 | `trigo.rechtwinklig` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 4–5 Standard |
| 22 | `trigo.allgemein` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 4–5 Standard |
| 23 | `geometrie.kreis` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 4–5 Extended |
| 24 | `raum.schraegbilder` | Spatial reasoning (Geometrie und Trigonometrie) | Enrichment |
| 25 | `daten.boxplot` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Standard |
| 26 | `stochastik.verknuepft` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Extended |
| 27 | `stochastik.mehrstufig` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Extended |

**MYP 5** – Quelle IBG (Framework S. 23–29), Zweige IBB

| Nr. | Thema | Zweig (Lernbereich) | Stufe im Framework |
|---|---|---|---|
| 1 | `zahlen.schranken` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Extended |
| 2 | `zahlen.rationale_exponenten` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Extended |
| 3 | `gleichungen.exponential` | Numerical and abstract reasoning (Zahl und Algebra) | Extended / Enrichment |
| 4 | `funktionen.folgen` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 5 | `funktionen.reihen` | Numerical and abstract reasoning (Zahl und Algebra) | Enrichment |
| 6 | `funktionen.transformation` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Extended |
| 7 | `funktionen.betrag` | Thinking with models (Funktionen und Modelle) | Annahme Extended |
| 8 | `funktionen.ganzrational` | Thinking with models (Funktionen und Modelle) | Enrichment |
| 9 | `funktionen.exponential_log` | Thinking with models (Funktionen und Modelle) | Extended / Enrichment |
| 10 | `funktionen.umkehr` | Thinking with models (Funktionen und Modelle) | Enrichment |
| 11 | `funktionen.trig` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Extended |
| 12 | `sonder.optimierung` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Extended |
| 13 | `gleichungen.trig` | Spatial reasoning (Geometrie und Trigonometrie) | Annahme Extended |
| 14 | `abbildungen.matrizen` | Spatial reasoning (Geometrie und Trigonometrie) | kein Beleg |
| 15 | `daten.standardabweichung` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Extended |
| 16 | `daten.zweidimensional` | Reasoning with data (Daten und Wahrscheinlichkeit) | Standard / Extended |
| 17 | `stochastik.bedingt` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Extended |
| 18 | `daten.normalverteilung` | Reasoning with data (Daten und Wahrscheinlichkeit) | Annahme |

### Quellen (alle abgerufen am 20.11.2026)
- **G5** LehrplanPLUS Gymnasium Mathematik 5 – https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/5/mathematik (M5 1–4 mit Unterkapiteln)
- **G6** … Gymnasium 6 – https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/6/mathematik (M6 1.1–1.5, 2.1–2.2, 3)
- **G7** … Gymnasium 7 – https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik (M7 1–5)
- **G8 / G9** … Gymnasium 8 bzw. 9 – https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/8/mathematik · …/gymnasium/9/mathematik (M8 1–7; M9 1–7.2; bei der Nachprüfung gelesen)
- **G10** … Gymnasium 10 – https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/10/mathematik (M10 1–5)
- **GSP** ISB, Verbindliche Hinweise zu Schwerpunktsetzungen, Gymnasium Mathematik 5–10, Stand August 2022 (alle Lernbereichs-Titel 5–10) – https://www.distanzunterricht.bayern.de/fileadmin/user_upload/lernenzuhause/Gymnasium/August2022/M_Schwerpunktsetzungen_5_10_neu.pdf
- **GSP8 / GSP9** ISB, Schwerpunktsetzungen Gymnasium Mathematik 8 bzw. 9, Stand August 2021 (Inhalte von M8 3, M8 7, M9 2.2, M9 5, M9 7.2) – https://www.distanzunterricht.bayern.de/fileadmin/user_upload/lernenzuhause/Gymnasium/deutsch_englisch_mathe/M_Schwerpunktsetzungen_8.pdf · …/M_Schwerpunktsetzungen_9.pdf
- **R5 / R6** LehrplanPLUS Realschule Mathematik 5 bzw. 6 – https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/5/mathematik · …/realschule/6/mathematik
- **R7** LehrplanPLUS Realschule Mathematik 7 (I) – https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/7/mathematik/wpfg1 (M7 1–8)
- **R8 / R9** LehrplanPLUS Realschule Mathematik 8 (I) bzw. 9 (I) – https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/8/mathematik/wpfg1 · …/realschule/9/mathematik/wpfg1 (bei der Nachprüfung gelesen)
- **R8-II / R9-II / R10-II** LehrplanPLUS Realschule Mathematik 8, 9, 10 (II/III) – https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/8/mathematik/wpfg2-3 · …/9/mathematik/wpfg2-3 · …/10/mathematik/wpfg2-3
- **R10** LehrplanPLUS Realschule Mathematik 10 (I) – https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/10/mathematik/wpfg1 (M10 1–5)
- **RML8 / RML9** C.C. Buchner, Stoffverteilungsplan Mathe.Logo 8 I bzw. 9 I, Realschule Bayern (Verlagsquelle; nur noch zum Abgleich) – https://www.ccbuchner.de/_files_media/mediathek/downloads/15120.pdf · https://www.ccbuchner.de/_files_media/mediathek/downloads/15129.pdf
- **RSP9 / RSP10** ISB, Schwerpunktsetzungen Realschule Mathematik 9 bzw. 10, Stand 09.08.2022 (Lernbereichs-Titel I und II/III) – https://www.distanzunterricht.bayern.de/fileadmin/user_upload/lernenzuhause/Realschule/August2022/M_Schwerpunktsetzungen_9.pdf · …/M_Schwerpunktsetzungen_10.pdf
- **IBG** IB, Middle Years Programme, Mathematics guide (for use from September 2020/January 2021), Framework S. 23–29 (Kopie einer Schule) – https://wottonhouseschool.co.uk/de/_files/ugd/e64f71_44e88284d1a84f7e8779a8766a508714.pdf
- **IBB** IB, MYP Subject brief Mathematics (vier Zweige; Standard und Extended) – https://www.ibo.org/globalassets/new-structure/brochures-and-infographics/pdfs/myp-brief-mathematics-en.pdf
- Zum Abgleich: `inhalte/pruefung/klassen/vorschlag-rsib.md` (17.11., Haese-Kapitel, Spalte II/III)
