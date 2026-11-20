# Nachprüfung 2 Lehrer-Aufbau: Bau-Auftrag I (Teil 1 und 1b), App 0.81.0

Stand 2026-11-20. Geprüft wurde `lernen-app` 68a663d, noch nicht auf `main`.

Grundlagen:
- meine erste Nachprüfung (`nachpruefung.md`)
- `umsetzung.md` Abschnitt LA-8
- der Entwurf `entwurf/lehrplan-spalte.html`
- das Bauprotokoll `inhalte/postfach/bau-lehrer.md`

Ich habe nur gelesen: kein App-Code, keine Datenbank, kein Merge.

## So geprüft

- **Ablauf:** Die App aus `lernen-app` lief lokal. Die lernen-api war mit den erfundenen Daten der App-Tests nachgestellt (`laLage`, `laUebersicht`, `la8Orte`):
  - Kind A: Klasse 5, lernt. „Runden“ wackelt.
  - Kind B: Klasse 7, Rückreise Pisa, heute Reisetag bis 23.11.
  - Dazu ein Testkind. Keine echten Kinderdaten.
- **Rollen und Breiten:** Eltern und Lehrer, je 400 × 860, 820 × 1180 und 1280 × 800.
- **Zusatzlauf:** ohne Pausen-Daten, also so, als wäre die Migration nicht eingespielt.
- **Ablage:**
  - Bilder: `bilder-0810/<rolle>-<schritt>-<breite>.png`
  - Skript: `nachpruefung-2.test.cjs`, läuft aus `pruef/` neben `tests/`
  - Messwerte: `nachpruefung-2-messung.json`
- **Live-Datenbank (nur gelesen):** `schule.pause` gibt es noch nicht, die Migration `20261120_i_pause.sql` ist nicht eingespielt. Das passt zum Bauprotokoll.

## 1 Mängel aus der ersten Nachprüfung

| Punkt | Urteil | Gesehen | Bild |
|---|---|---|---|
| **Muss:** Was wackelt auf dem Handy | **erfüllt** | Unter 560 px eine Karte je Etappe: Kopf, Marke „wackelt“, „richtig / falsch“, „häufigster Fehler“, „seit“. Nichts abgeschnitten, kein Querrollen. Alle vier Reiter passen auf 400 px. Ab 820 px wieder die Tabelle, auch dort nichts abgeschnitten. | `*-2-wackelt-400` |
| Sollte 1: Pausen/Reisetage | **erfüllt** (siehe Abschnitt 3) | | |
| Sollte 2: Wunsch in „Zu tun“ | **erfüllt** | Blauer Eintrag „Kind A möchte ‚Eis‘ einlösen (300 Sterne)“ mit „Bestätigen“ und „Ablehnen“. Kein Kasten „Wartet auf dich“ mehr. Die Tabelle endet auf 1280 × 800 bei 747 px (vorher 1057), also ohne Rollen. Lehrer sehen den Wunsch nicht (richtig). | `eltern-1-start-1280`, `eltern-1-start-820` |
| Sollte 3: Lehrplan auf dem Handy | **erfüllt** | Liste je Flug (fertig, Ort und andere Schularten, je Kind „geschafft/offen“). Kein Querrollen, nichts abgeschnitten. Ab 820 px Tabelle ohne Querrollen. | `*-4-lehrplan-400` |
| Sollte 4: Reisewörter erklärt | **erfüllt** | Zu tun: „Rückreise Pisa (Wiederholung nach nicht bestandenem Nachtest)“. Überblick: „Bordkarten (Aufgabe)“, „Flug (Thema)“, „Etappe (Lernschritt)“. Was wackelt: Spaltenkopf „Etappe (Lernschritt)“. | `*-3-ueberblick-B-*` |
| Sollte 5: Stand-Zellen ohne Ampel | **offen (Entscheidung)** | Bau: „entschieden, nicht gebaut“. Sebastians Bestätigung kenne ich nicht. | – |
| Kann 1: Überblick Kind B | **erfüllt** | „Keine Etappe (Lernschritt) wackelt · Rückreise Pisa offen“ mit Erklärung darunter. | `*-3-ueberblick-B-*` |
| Kann 2: „noch kein Inhalt“ | nicht selbst gesehen | Nur durch den App-Test I-7 belegt. | – |
| Kann 3: Tablet-Tabelle | **erfüllt** | Die ⚙-Zelle sitzt auf der Zeilenlinie, Knöpfe untereinander. IB-Text „– (ab Kl. 6)“; darunter steht noch ein zweites „–“ für die Prozent (Kann). | `*-1-start-820` |
| Kann 4: „AKTIONEN“ | **erfüllt** | Leerer Spaltenkopf. | |
| Kann 5: „über der Klasse“ | **erfüllt** | Auf dem Tablet ganz zu lesen. | `*-7-la8-gebiet-820` |
| Kann 6: „Datenbank“ | **erfüllt** | Ersetzt, zum Beispiel „Die Stufe je Schulart lässt sich hier noch nicht einstellen; gemessen wird an der Klasse.“ | `*-6-einstellen-*` |

## 2 LA-8 Lehrplan nach Themengebiet – teilweise

### „Fertig, wenn“

| Punkt | Urteil | Gesehen |
|---|---|---|
| Plan öffnen zeigt rechts „Nach Themengebiet“ mit dem Gebiet des aktuellen Ortes | **erfüllt** | Umschalter „Nach Themengebiet“ (gedrückt) und „Nach Klasse (Lehrplan)“. Gebiet „Zahlen“ ist vorbelegt (Rom = erster offener Ort), „Sortiert nach Klasse in“ ist auf Gymnasium vorbelegt. Bei beiden Rollen und allen Breiten gleich. |
| Kein Ortsname in einer Überschrift | **erfüllt** | Links zum Beispiel „Zahlen – Natürliche Zahlen und Stellenwertsysteme und Ganze Zahlen“, darunter „Gym 5 · RS 5 · MYP 1 · 0/2 Flüge · *Ort in der Reise: Rom*“. Rechts zum Beispiel „Zahlen – Elementare Wurzeln, Reelle Zahlen …“ (ab 3 Flügen zwei und „…“). |
| Gym-9-Thema mit einem Tipp in den Plan eines Klasse-5-Kindes | **erfüllt** | „+“ bei „Zahlen – Elementare Wurzeln …“ speichert den Plan sofort mit dem neuen Ort am Ende. Links erscheint die Zeile mit „Klasse 9 – über der Klasse des Kindes · Kind sieht ihn unter ‚Später‘“, rechts steht „✓ im Plan“. Bild: `*-8-la8-gym9-*`. |
| Jede Zeile zeigt Kästchen und Rand in der Farbe ihrer Gymnasium-Klasse | **teilweise** | Kästchen und Rand gemessen: 5 #2E7D32, 6 #0277BD, 9 #EF6C00, ohne Gymnasium-Klasse graues „–“. Links und rechts gleich. **Aber:** Der helle Verlauf fehlt links im Plan; dort ist nur der Rand farbig. Rechts ist der Verlauf da. Laut Vorgabe sollten links und rechts gleich aussehen. |

### Weitere Vorgaben aus Abschnitt LA-8 und Entwurf

| Vorgabe | Urteil | Gesehen |
|---|---|---|
| Umschalter oben, Standard links | erfüllt | |
| Gebiet-Knöpfe | erfüllt mit Abweichung | Nur Gebiete mit Orten (im Mock Zahlen · Algebra · Geld). Annehmbar. |
| Sortierung | erfüllt | Klasse der gewählten Schulart, Klasse fett. Orte ohne Klasse ans Ende: Bei Realschule rückt „Prozentrechnung“ (RS 7) vor die Gym-9-Zeile, bei IB steht sie am Ende. |
| Gestrichelte Linie | teilweise | „AB HIER ÜBER KLASSE 5 DES KINDES“, gestrichelt, vor dem ersten Klasse-6-Ort; bei Realschule ebenso. **Bei IB MYP fehlt die Linie** für ein Kind der Klasse 5, das noch kein MYP-Jahr hat. Alle Orte liegen dann darüber; die Linie gehörte an den Anfang. |
| Kopf mit Balken | erfüllt | „Zahlen: 1 von 5 Orten im Plan · von leicht nach schwer“. |
| Eingeplante Orte | erfüllt | Grau mit „✓ im Plan“. |
| Legende | teilweise | Steht unten in der Spalte (Kästchen 5 bis 10 und „–“). Auf Tablet und Rechner hat die Spalte aber eine feste Höhe mit eigenem Rollen. Die Legende und die letzte Zeile sind erst nach Rollen *in* der Spalte sichtbar; im Bild ist die letzte Zeile halb abgeschnitten. Auf dem Handy sichtbar. |
| Nach Klasse (Lehrplan) | erfüllt | „Klasse 5: 2 von 3 Flügen im Plan“, neue Überschriften und Farben. Bild: `*-9-la8-klasse-*`. |
| Info-Seite | erfüllt | Erklärt beide Ansichten und die Farbe. |

### Neue Mängel LA-8 (gesehen)

1. **Tablet 820:** Der Umschalter-Knopf bricht mitten im Wort um: „Nach Themengebie-t“ (`eltern-7-la8-gebiet-820`).
2. **Handy 400:** Links im Plan brechen lange Überschriften mitten im Wort um: „Stellenwertsyste-me“ (`eltern-7-la8-gebiet-400`). Rechts nicht.
3. Der helle Verlauf fehlt links im Plan (siehe oben).
4. Die Linie fehlt bei IB für ein Kind ohne MYP-Jahr.
5. Legende und letzte Zeile sind auf Tablet und Rechner erst nach innerem Rollen sichtbar.

## 3 Reisetage und Pausen – erfüllt (Wirkung nur mit nachgestellten Daten)

**Auffindbar (gesehen)**
- Knopf „+ Reisetag eintragen“ oben rechts in „Zu tun“, bei Eltern und Lehrern, in allen Breiten.
- Karte „Reisetage und Pausen“ im Blatt „⚙ Einstellen“ des Kindes.
- Absatz „Reisetage und Pausen“ auf „So funktioniert’s“.

**Verständlich (gesehen)**
- Blatt „Reisetag eintragen“:
  - von / bis, vorbelegt mit heute
  - Knöpfe Reisetag · krank · Ferien, oder ein eigenes Wort
  - „für: alle Kinder“ vorbelegt, das Testkind steht nicht in der Auswahl
  - Satz: „Eingetragene Tage zählen nicht für ‚Lernt‘ und ‚kein Lerntag seit …‘. Lernregeln, Wiederholungen und Nachtests ändern sich nicht. Ändern und löschen: ‚⚙ Einstellen‘ des Kindes.“
- In der Karte: Eintrag „19.11.–23.11. · Reisetag · Herr Lehrer“ mit „Ändern“ und „Löschen“.
- Bilder: `*-5-reisetag-blatt-*`, `*-6-einstellen-*`.

**Wirkung (gesehen, mit Pause für Kind B heute)**
- Tabelle „Lernt“: blau „Pause bis 23.11. (Reisetag)“ statt rot. Auf dem Handy auf der Karte ebenso.
- „Zu tun“: Der rote Eintrag „Kind B: kein Lerntag in den letzten 4 Wochen“ entfällt; die Rückreise Pisa bleibt rot.
- Überblick Kind B: „Lernt es? Pause bis 23.11. (Reisetag)“.

**Ohne Migration (gesehen):** Der Knopf „+ Reisetag eintragen“ fehlt, und „kein Lerntag“ steht wieder in „Zu tun“. Den Satz im Blatt („… lassen sich hier noch nicht eintragen“) habe ich nicht gesehen: Mein Bild entstand, als das Blatt noch „Lade …“ zeigte.

**Nicht selbst gesehen**
- Dass vergangene Pausentage beim Zählen „seit … kein Lerntag“ ausgelassen werden. Belegt nur durch den App-Test I-10.
- Ob Eintragen, Ändern und Löschen in der Datenbank ankommen: Migration und Rauchtest sind nicht ausgeführt.

## 4 Abweichungen des Bau-Chats

| Abweichung | Bewertung |
|---|---|
| Stand-Zellen ohne Ampelfarbe | Annehmbar fachlich, braucht aber **Sebastians Bestätigung**. Sie war Sollte 5. |
| Orange 9 als Rand 2,98 : 1 (knapp unter 3 : 1) | Annehmbar: Die Klasse steht zusätzlich im Kästchen (≥ 4,5 : 1). |
| Eltern-/Lehrer-Bereich nur hell, keine dunkle Variante | Annehmbar. |
| Tablet links: eine Zeile je Ort mit „…“ | Annehmbar, wegen der Regel aus E-2 (12 Orte, je Zeile höchstens 72 px). Aufgeklappt steht der volle Text. Der Tooltip hilft auf dem iPad nicht (Kann). |
| Lehrplan-Übersicht (LA-7, eigene Seite) unverändert, ohne Gebiet-Überschrift und Farben | Annehmbar: LA-8 verlangt die Überschriften „links im Plan und rechts im Lehrplan“. Farben auch dort wären einheitlicher (Kann). |
| Vorlese-Namen der Knöpfe nennen weiter den Ort („+ Kyoto – Wurzeln“) | Kleiner Mangel: Wer vorlesen lässt, hört etwas anderes als die sichtbare Überschrift (Kann). |
| Gebiet-Knöpfe nur für Gebiete mit Orten | Annehmbar. |
| Pausen über die bestehende Aktion `schule_notiz_setzen` | Annehmbar, technisch. |
| Migration und Rauchtest nicht ausgeführt | Kein Mangel des Baus, aber **Voraussetzung vor dem Merge** (siehe Muss). |
| Pause nach dem Kalender des Geräts, Lerntage aus der Datenbank | Auf der Weltreise mit Zeitzonenwechseln kann ein Tag verrutschen. Annehmbar, wenn es bekannt ist (Kann). |
| Neu: Link „Test zu den neuen Etappen“ (Punkt 5) | Nicht geprüft; im Mock kam der Fall nicht vor. |

## Mängel

### Muss
1. **Vor dem Merge auf `main`:** Migration `20261120_i_pause.sql` einspielen und den Rauchtest `i_pause_rauchtest.sql` ausführen. Sonst fehlt live der Knopf „+ Reisetag eintragen“, und Reisetage bleiben rot. Das betrifft die Auslieferung, nicht den App-Code.

### Sollte
1. Umschalter „Nach Themengebiet“ auf dem Tablet ohne Trennung im Wort, zum Beispiel kürzer („Themengebiet“ | „Klasse“) oder mit `hyphens: manual`.
2. Plan links auf dem Handy: lange Überschriften nicht mitten im Wort trennen. Mögliche Wege: kleinere Schrift, die Pfeile ↑ ↓ unter den Text, oder Kürzen mit „…“ wie auf dem Tablet.
3. Die Ampel in den Stand-Zellen von Sebastian bestätigen lassen.

### Kann
1. Den hellen Verlauf auch links im Plan zeigen, wie rechts und im Entwurf.
2. Die gestrichelte Linie bei IB auch für ein Kind ohne MYP-Jahr zeigen (dann ganz oben).
3. Die Legende auf Tablet und Rechner ohne inneres Rollen sichtbar machen, zum Beispiel über der Liste oder fest am Spaltenende.
4. Die Vorlese-Namen der Knöpfe an die sichtbare Überschrift angleichen.
5. Das doppelte „–“ in der IB-Zelle für Klasse 5 weglassen.
6. Die Pausen-Grenze bei Zeitzonenwechsel im Info-Text kurz erwähnen.

## Nicht geprüft
- **Die echte Seite mit Anmeldung:** Mir fehlt ein Code. Echte Daten mit 66 Orten habe ich nicht im Browser angesehen.
- Reisetage in der Datenbank (Migration nicht eingespielt, Rauchtest nicht ausgeführt).
- **Kopf im Blatt „⚙ Einstellen“:** Für Kind B öffnete es mit „Kind A einstellen“. Vermutlich liefert der Mock immer den Lernstand von Kind A. Ob das live richtig ist, ist offen.
- **Datumsfelder:** Der Testbrowser zeigt sie amerikanisch (11/20/2026). Wie sie auf einem deutschen Gerät aussehen, habe ich nicht gesehen.
- Ziehen mit Finger oder Maus in der Ansicht „Nach Themengebiet“; geprüft habe ich nur „+“.
- Der Link „Test zu den neuen Etappen“ und „noch kein Inhalt“ (nur App-Tests).
- Echte Geräte (iPhone, iPad), Tablet quer.
