# LK-D 2 – Teilungsliste nach der neuen Regel (22.11.2026)

Grundlage: AUFTRAEGE `lernen-app` 367e31e0, also „Teilungsregel NEU“ (15:30), „Berichtigung“ (15:35) und „Ergänzung – Benennung und Aufbau“ (15:40). Daten aus LK-D (`lk_daten_2211.json`, Stand nach dem Live).
- Nichts eingespielt, keine Inhalte ergänzt.
- Kinder nur als Nummern.
- JSON: `lk_teilung_2211.json` (Teile, Grenzfälle, alle Voraussetzungs-Kanten, Verstöße, Aufbau-Kette je Teil).

## Verfahren

- **Klasse einer Etappe je Schulart:** die erste Klasse, in der ein Lehrplanpunkt sie als Hauptthema verlangt (aus LK-D).
- **Teilung:** Etappen mit gleichem Klassenpaar (Gym, RS I) bilden einen Teil, also die feinste gemeinsame Teilung. Sortiert wird nach der Klasse.
  - Hat eine Etappe nur in einer der beiden Schularten eine Klasse, kommt sie zum passenden Teil.
  - Hat sie in keiner eine Klasse, kommt sie zum Teil der Etappe davor in der Themendatei. Das sind 2 Etappen, beide bei 26.
- **Ergebnis:** Jedes Teil-Thema liegt in Gym und RS I in genau einer Klasse.
- **IB und RS II/III** lösen keine Teilung aus. Ihre Klassen sind je Teil angegeben; wo ein Teil dort mehrere Klassen hat, steht er bei den Grenzfällen.

## Ergebnis: 6 Themen werden geteilt, 15 Teile

Kein geteiltes Thema ändert eine Gym-Klasse: Im Gymnasium liegen alle Teile in derselben Klasse und kommen dort als Teil 1, 2, 3 nacheinander. Geteilt wird jeweils, weil die Realschule (Gruppe I) die Etappen auf mehrere Klassen verteilt.


### 26 Direkte Proportionalität und Dreisatz

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/2 | Direkte Proportionalität und Dreisatz – Teil 1 von 2 · Dreisatz | Auf die Einheit schließen, Der Dreisatz, Geschickte Zwischenschritte °, Sachaufgaben mit Dreisatz, Änderungsraten berechnen ° | 5 | 5 | 5 | 2 / 2 | 0/5 | 0/5 |
| 2/2 | Direkte Proportionalität und Dreisatz – Teil 2 von 2 · proportionale Zuordnungen erkennen | Was heißt proportional?, Verdoppeln, verdreifachen, halbieren, Ist die Tabelle proportional? | 5 | 6 | 6 | 2 / 2 | 0/3 | 0/3 |

### 29 Terme umformen · Flug geschafft: Kind 2

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/2 | Terme umformen – Teil 1 von 2 · zusammenfassen und ausmultiplizieren | Gleichartige Glieder zusammenfassen, Produkte vereinfachen, Minus vor der Klammer, Ausmultiplizieren, Äquivalente Terme | 7 | 7 | 7 | 1/2 / 1/2 | 0/5 | 5/5 |
| 2/2 | Terme umformen – Teil 2 von 2 · Summe mal Summe, Ausklammern, binomische Formeln | Summe mal Summe, Gemeinsamen Faktor ausklammern, Binomische Formeln | 7 | 8 | 8 | 4 / 4 | 0/3 | 3/3 |

### 44 Konstruktionen, Kongruenz und Beweise

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/2 | Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 · Dreiecke konstruieren, Kongruenz | Gleichschenklige Dreiecke, Welcher Kongruenzsatz passt?, Ist das Dreieck konstruierbar?, Planfigur und Konstruktionsbeschreibung, Satz und Kehrsatz | 7 | 7 | 8 | 2/3 / 2/3 | 0/5 | 0/5 |
| 2/2 | Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 · Vierecke **(dünn)** | Winkel in symmetrischen Vierecken, Vierecke konstruieren | 7 * | 8 | 8 | – / – | 0/2 | 0/2 |

### 46 Kongruenzabbildungen

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/3 | Kongruenzabbildungen – Teil 1 von 3 · Spiegeln und Symmetrie | An einer Achse spiegeln, Mittelsenkrechte und Lot, Die Winkelhalbierende, Symmetrische Figuren, Symmetrische Vierecke ordnen, Was bleibt bei Abbildungen gleich? | 7 | 6 | 6 | 3 / 3 | 0/6 | 0/6 |
| 2/3 | Kongruenzabbildungen – Teil 2 von 3 · Verschieben und Vektoren | Figuren verschieben, Gegenvektor und Rückweg, Vektoren in Koordinaten | 7 * | 7 | 7 | 3 / 3 | 0/3 | 0/3 |
| 3/3 | Kongruenzabbildungen – Teil 3 von 3 · Drehen und Punktspiegelung | An einem Punkt spiegeln, Um einen Punkt drehen, Vektoren um 90° und 180° drehen | 7 | 8 | – | 3 / 3 | 0/3 | 0/3 |

### 61 Zufall und Laplace

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/2 | Zufall und Laplace – Teil 1 von 2 · Ergebnis, Ereignis, relative Häufigkeit **(dünn)** | Ergebnis, Ergebnisraum, Ereignis, Relative Häufigkeit | 8 | 8 | 8 | 2 / 2 | 0/2 | 0/2 |
| 2/2 | Zufall und Laplace – Teil 2 von 2 · Laplace-Wahrscheinlichkeit | Laplace-Wahrscheinlichkeit, Ist es ein Laplace-Experiment?, Das Gegenereignis, Gesetz der großen Zahlen | 8 | 9 | 9 | 2 / 2 | 0/4 | 0/4 |

### 91 Schrägbilder und Raumdarstellung

| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |
|---|---|---|---|---|---|---|---|---|
| 1/2 | Schrägbilder und Raumdarstellung – Teil 1 von 2 · Schrägbilder und Lage im Raum | Pyramiden: Ecken, Kanten, Flächen, Parallel, schneidend oder windschief?, Wahre Größe im Schrägbild | 10 | 7 | 8 | – / – | 0/3 | 0/3 |
| 2/2 | Schrägbilder und Raumdarstellung – Teil 2 von 2 · Raumkoordinaten und Rotationskörper | Punkte im Raum mit Koordinaten, Rotationskörper, Axialschnitte berechnen | 10 | 8 | 10 | – / – | 0/3 | 0/3 |

Legende:
- `*`: Diese Schulart hat für den Teil keinen eigenen Lehrplanpunkt; die Klasse folgt aus der Reihenfolge (Vertiefung).
- `°`: Etappe ohne Lehrplanpunkt in Gym und RS I.
- „–“: Der Teil ist in dieser Spur kein Lehrplanstoff.
- Stand: erledigt/Etappen des Teils (gelandet, gesetzt oder nachgewiesen).

**Zu dünn (nur gemeldet, nichts ergänzt):**
- 44 Teil 2 „Vierecke“ (2 Etappen) und 61 Teil 1 „Ergebnis, Ereignis, relative Häufigkeit“ (2 Etappen). Vorschlag: Kurzflug mit 1–2 Städten.
- 61 Teil 1 deckt den RS-8-Lernbereich „Daten und Zufall“ (8 Std.) zusammen mit den Nebenbezügen 60/63 ab, ist also nicht zu dünn für den Lehrplan.

**Lernstand (Regel Punkt 6):**
- Nur Kind 2 hat Lernstand in einem geteilten Thema: 29 Terme umformen, Flug geschafft.
- Nach der Teilung sind **beide Teile vollständig** (5/5 und 3/3). Teil 2 gilt als geschafft; der Stempel wird nachgetragen, Sterne gibt es nicht doppelt.
- In den übrigen geteilten Themen hat kein Kind Lernstand.

**Benennung:** überall „‹Titel› – Teil x von y“, Untertitel wie in der Tabelle (Vorschlag).

## Aufbau nach der Teilung

- **Teilung:** Teil n braucht Teil n−1, hart (7 neue Kanten).
- **Bisherige Voraussetzungen** (128, ohne stillgelegte Themen) sind dem richtigen Teil zugeordnet:
  - „braucht“ geht an den ersten Teil, dessen Klasse in Gym und RS I nicht vor der Voraussetzung liegt.
  - „wird gebraucht von“ geht an den letzten Teil, der in Gym und RS I nicht nach dem abhängigen Thema liegt.
  - Drei Fälle sind inhaltlich gesetzt (Annahme): 47 Ähnlichkeit, 44 Konstruktionen und 4 Formeln umstellen brauchen nur Teil 1 von 46 bzw. 29.
- Alle Kanten stehen in der JSON (`kanten`).

**Wichtige Zuordnungen:**
- 29 Terme umformen:
  - Teil 1 braucht 28 Terme aufstellen und 102 Potenzgesetze (hart).
  - Teil 2 wird gebraucht von 8 Quadratische Gleichungen, 31 Bruchterme und 97 Quadratische Terme (hart) sowie 35 Quadratische Funktionen (empfohlen).
  - 4 Formeln umstellen braucht Teil 1.
- 61 Zufall und Laplace:
  - Teil 1 wird gebraucht von 63 Verknüpfte Ereignisse.
  - Teil 2 wird gebraucht von 62 Mehrstufige Zufallsexperimente und 64 Simulation (alle hart).
- 46 Kongruenzabbildungen:
  - Teil 2 (Vektoren) wird gebraucht von 74 Determinanten.
  - Teil 3 (Drehen) wird gebraucht von 49 Matrizen.
  - Teil 1 wird gebraucht von 47 und 44.
- 26 Proportionalität: Teil 1 braucht 25 Größen; Teil 2 wird gebraucht von 93 Indirekte Proportionalität (hart).
- 91 Schrägbilder: Teil 1 braucht 52 Körper darstellen (hart).

**Prüfung der ganzen Kette gegen die Klassenlage (alle 135 Kanten):**
- **Gymnasium: 0 Verstöße. RS Gruppe I: 0 Verstöße.**
- RS II/III: 2, beide empfohlen und schon aus LK-D bekannt; die Voraussetzung ist dort kein Lehrplanstoff:
  - 37 ← 103;
  - 92 ← 101.
  - Vorschlag: für II/III weich machen.
- IB: 10 je Kurs, unverändert gegenüber LK-D. Neu zugeordnet sind nur:
  - 63 ← 61 **Teil 1** (hart; MYP 1 gegen 2);
  - 29 **Teil 1** ← 102 (hart; **Sebastians Entscheidung, bleibt**, nur gemeldet).

**Hinweis zu 46 im Gymnasium (Aufbau-Befund mit Vorschlag):**
- Teil 3 enthält die Punktspiegelung, die das Gymnasium in Klasse 7 verlangt.
- Teil 2 (Verschieben und Vektoren) ist im Gymnasium kein Lehrplanstoff. Die harte Kette Teil 3 ← Teil 2 zwingt Gym-Kinder also durch einen Teil ohne Gym-Punkt.
- Vorschlag:
  - (a) im Gymnasium die Kante Teil 3 ← Teil 2 als „empfohlen“ führen, Teil 3 braucht dann Teil 1 hart; oder
  - (b) die Punktspiegelung in Teil 1 verschieben. Das widerspricht aber der Regel, weil RS I sie erst in Klasse 8 verlangt.
  - Empfehlung: (a). Sebastian entscheidet.
- Dasselbe gilt schwächer für 44 Teil 2 (Vierecke, im Gymnasium ohne eigenen Punkt): Er ist der letzte Teil, nichts hängt im Gymnasium daran.

## Grenzfälle (keine Teilung, nur Anzeige „weitergeführt“)

| Thema | Teil | Spur | Klassen | Empfehlung |
|---|---|---|---|---|
| 2 Lineare Gleichungen | – | IB Std | 2, 3 | nicht teilen |
| 2 Lineare Gleichungen | – | IB Ext | 2, 3 | nicht teilen |
| 6 Gleichungssysteme mit 2 Unbekannten | – | IB Ext | 3, 4 | nicht teilen |
| 8 Quadratische Gleichungen (allgemein) | – | RS II/III | 9, 10 | nicht teilen |
| 18 Grundrechenarten und Rechengesetze | – | IB Std | 1, 2 | nicht teilen |
| 18 Grundrechenarten und Rechengesetze | – | IB Ext | 1, 2 | nicht teilen |
| 20 Wurzeln und reelle Zahlen | – | IB Std | 3, 4 | nicht teilen |
| 20 Wurzeln und reelle Zahlen | – | IB Ext | 3, 4 | nicht teilen |
| 21 Brüche und Anteile | – | IB Std | 1, 2 | nicht teilen |
| 21 Brüche und Anteile | – | IB Ext | 1, 2 | nicht teilen |
| 28 Terme aufstellen und deuten | – | IB Std | 1, 2 | nicht teilen |
| 28 Terme aufstellen und deuten | – | IB Ext | 1, 2 | nicht teilen |
| 29 Terme umformen | 1 | IB Std | 1, 2 | nicht teilen |
| 29 Terme umformen | 1 | IB Ext | 1, 2 | nicht teilen |
| 32 Zuordnung und Funktion | – | IB Std | 1, 4 | nicht teilen |
| 32 Zuordnung und Funktion | – | IB Ext | 1, 4 | nicht teilen |
| 33 Lineare Funktionen | – | RS II/III | 8, 9 | nicht teilen |
| 33 Lineare Funktionen | – | IB Std | 3, 4 | nicht teilen |
| 42 Grundbegriffe und Figuren | – | IB Std | 1, 2 | nicht teilen |
| 42 Grundbegriffe und Figuren | – | IB Ext | 1, 2 | nicht teilen |
| 44 Konstruktionen, Kongruenz und Beweise | 1 | IB Std | 2, 3 | nicht teilen |
| 44 Konstruktionen, Kongruenz und Beweise | 1 | IB Ext | 2, 3 | nicht teilen |
| 47 Ähnlichkeit und Strahlensätze | – | IB Std | 3, 4 | nicht teilen |
| 47 Ähnlichkeit und Strahlensätze | – | IB Ext | 3, 4 | nicht teilen |
| 50 Umfang und Flächeninhalt | – | IB Std | 1, 2 | nicht teilen |
| 50 Umfang und Flächeninhalt | – | IB Ext | 1, 2 | nicht teilen |
| 55 Trigonometrie im rechtwinkligen Dreieck | – | IB Std | 3, 4 | nicht teilen |
| 55 Trigonometrie im rechtwinkligen Dreieck | – | IB Ext | 3, 4 | nicht teilen |
| 63 Verknüpfte Ereignisse | – | IB Std | 1, 4 | nicht teilen |
| 63 Verknüpfte Ereignisse | – | IB Ext | 1, 4 | nicht teilen |
| 98 Winkelsätze | – | IB Std | 1, 3 | nicht teilen |
| 98 Winkelsätze | – | IB Ext | 1, 3 | nicht teilen |

- RS II/III: 8 Quadratische Gleichungen (9 + 10) und 33 Lineare Funktionen (8 + 9). Würde II/III Teilungen auslösen, kämen genau diese zwei Themen dazu.
- IB: Die Schulbuch-Verzeichnisse verteilen viele Themen über 2 Jahre. Das ist Orientierung und kein Teilungsgrund.

## Aufbau-Kette je Teil (für die Anzeige)

| Teil | Baut auf | Geht weiter in |
|---|---|---|
| 26 Direkte Proportionalität und Dreisatz – Teil 1 von 2 | 25 Größen und Einheiten (Gym 5 · RS I 5) (hart) | 26 Direkte Proportionalität und Dreisatz – Teil 2 von 2 (Gym 5 · RS I 6) |
| 26 Direkte Proportionalität und Dreisatz – Teil 2 von 2 | 26 Direkte Proportionalität und Dreisatz – Teil 1 von 2 (Gym 5 · RS I 5) (hart) | 93 Indirekte Proportionalität (Gym 8 · RS I 7) |
| 29 Terme umformen – Teil 1 von 2 | 28 Terme aufstellen und deuten (Gym 7 · RS I 6) (hart); 102 Potenzgesetze (Gym 7 · RS I 7) (hart) | 4 Formeln umstellen (Gym 8 · RS I –); 29 Terme umformen – Teil 2 von 2 (Gym 7 · RS I 8) |
| 29 Terme umformen – Teil 2 von 2 | 29 Terme umformen – Teil 1 von 2 (Gym 7 · RS I 7) (hart) | 8 Quadratische Gleichungen (allgemein) (Gym 9 · RS I 9); 97 Quadratische Terme und Extremwerte (Gym – · RS I 8); 35 Quadratische Funktionen (Gym 9 · RS I 9); 31 Bruchterme (Gym 8 · RS I 8) |
| 44 Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 | 43 Mit Winkeln rechnen (Gym 5 · RS I 5); 98 Winkelsätze (Gym 7 · RS I 7); 46 Kongruenzabbildungen – Teil 1 von 3 (Gym 7 · RS I 6) | 44 Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 (Gym 7 · RS I 8) |
| 44 Konstruktionen, Kongruenz und Beweise – Teil 2 von 2 | 44 Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 (Gym 7 · RS I 7) (hart) | – |
| 46 Kongruenzabbildungen – Teil 1 von 3 | 42 Grundbegriffe und Figuren (Gym 5 · RS I 5) | 47 Ähnlichkeit und Strahlensätze (Gym 9 · RS I 9); 44 Konstruktionen, Kongruenz und Beweise – Teil 1 von 2 (Gym 7 · RS I 7); 46 Kongruenzabbildungen – Teil 2 von 3 (Gym 7 · RS I 7) |
| 46 Kongruenzabbildungen – Teil 2 von 3 | 46 Kongruenzabbildungen – Teil 1 von 3 (Gym 7 · RS I 6) (hart) | 74 Zweireihige Determinanten (Gym – · RS I 7); 46 Kongruenzabbildungen – Teil 3 von 3 (Gym 7 · RS I 8) |
| 46 Kongruenzabbildungen – Teil 3 von 3 | 46 Kongruenzabbildungen – Teil 2 von 3 (Gym 7 · RS I 7) (hart) | 49 Matrizen und Abbildungen mit Matrizen (Gym – · RS I 10) |
| 61 Zufall und Laplace – Teil 1 von 2 | 21 Brüche und Anteile (Gym 6 · RS I 6) (hart) | 63 Verknüpfte Ereignisse (Gym 9 · RS I 8); 61 Zufall und Laplace – Teil 2 von 2 (Gym 8 · RS I 9) |
| 61 Zufall und Laplace – Teil 2 von 2 | 61 Zufall und Laplace – Teil 1 von 2 (Gym 8 · RS I 8) (hart) | 62 Mehrstufige Zufallsexperimente (Gym 10 · RS I 10); 64 Simulation (Gym 10 · RS I 9) |
| 91 Schrägbilder und Raumdarstellung – Teil 1 von 2 | 52 Körper darstellen (Gym 8 · RS I 5) (hart) | 91 Schrägbilder und Raumdarstellung – Teil 2 von 2 (Gym 10 · RS I 8) |
| 91 Schrägbilder und Raumdarstellung – Teil 2 von 2 | 91 Schrägbilder und Raumdarstellung – Teil 1 von 2 (Gym 10 · RS I 7) (hart) | – |

Für alle übrigen Themen steht die Kette in `aufbau_kette` (JSON).

## Gesichert / Annahme / offen

**Gesichert:**
- Teilung nach der Regel aus den LK-D-Daten.
- 0 Verstöße in Gymnasium und RS I nach der Teilung.
- Kind 2: Thema 29 nach der Teilung in beiden Teilen vollständig.
- Keine Gym-Klasse ändert sich.

**Annahme:**
- Die Etappen-Klasse ergibt sich aus meiner Etappenzuordnung in LK-D.
- Zuordnung bisheriger Voraussetzungen zu Teilen: nach Klassenlage, drei Fälle inhaltlich gesetzt.
- 26: Die 2 Etappen ohne Lehrplanpunkt (Geschickte Zwischenschritte, Änderungsraten) gehören zu Teil 1.
- Die Untertitel sind Vorschläge.

**Offen (Sebastian):**
- Liste bestätigen.
- 46 im Gymnasium: (a) oder (b).
- Kurzflüge für 44 Teil 2 und 61 Teil 1.
- Ob II/III jemals teilen soll (8 und 33).
- Danach `bau-lehrer` (Teil-Verfahren, Umhängen des Lernstands Kind 2 in 29) und `reise-aufbau` (Nachbarländer, 9 neue Flüge).
