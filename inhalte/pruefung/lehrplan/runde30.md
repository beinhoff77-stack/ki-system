# Dreißigste Runde (21.11.): Lehrplan-Prüfung – Zuordnungen und Voraussetzungen

Grundlage: Zweig `lernen-app` e0739529 (einschließlich Nachtrag des Gestalters), Datenbank nur gelesen. Quelle LehrplanPLUS Bayern, **abgerufen 21.11.2026** über die Suche auf lehrplanplus.bayern.de (Seitenauszüge, keine Volltextabrufe). Unbelegtes ist als **Annahme** gekennzeichnet.

## 0f. Nacharbeit 907 c (22.11., ChatGPT 919, MUSS 4)

Grundlage: `lernen-app` f278a3cf. Die Datenbank habe ich nur gelesen, **nichts ausgeführt**. Geändert ist nur `supabase/migrations/20261122_lehrplan_nacharbeit_907.sql`.

**Gelesen:**
- `schule.einheit.status` kennt die Werte `entwurf`, `geprueft`, `freigegeben` und `ersetzt`.
- Die Migrationen der App behandeln `status in ('geprueft','freigegeben')` als für Kinder sichtbar.
- Heute haben 87 Themen eine freigegebene Einheit. Die zehn stillgelegten Themen haben nur einen Entwurf; `geprueft` kommt nicht vor.

**Löschschutz (Abschnitt 3c):**
- Er bricht jetzt ab, wenn das stillgelegte Thema der Zeile eine Einheit im Status **`geprueft` oder `freigegeben`** hat. Bisher prüfte er nur `freigegeben`.
- Damit Rauchtest m den Schutz aufrufen kann, steckt er in einer Sitzungsfunktion `pg_temp.lb907_loeschen()`. Sie verschwindet mit der Sitzung, ein DROP ist nicht nötig.
- Dieselbe Sichtbarkeitsregel gilt jetzt auch beim Leeren der Klassen (3d) und in den Regeln b und i. Annahme: Ein geprüfter Flug ist für Kinder sichtbar und muss daher wie ein freigegebener behandelt werden. Auf den heutigen Daten ändert das nichts.

**Rauchtest l:** prüft nur noch die zehn stillgelegten Themen 12, 27, 40, 41, 48, 72, 77, 78, 82 und 83, solange sie keine sichtbare Einheit haben. Andere Themen ohne freigegebene Einheit, etwa künftige Entwürfe, prüft er nicht.

**Rauchtest m (neu):**
- m0: Ohne sichtbare Einheit läuft der Löschschutz durch.
- Danach legt der Test für das stillgelegte Thema 48 je eine Test-Einheit mit `geprueft` und mit `freigegeben` an. Er tut das in einem Unterblock und rollt alles zurück.
- Jedes Mal muss der Löschschutz mit „Abbruch vor Löschung …“ abbrechen.
- Am Ende prüft der Test, dass die Zahl der Verbindungen gleich ist und keine Test-Einheit übrig bleibt.

**Lokal auf Postgres 16 geprüft** (Tabelle `einheit` mit Statusprüfung und den eindeutigen Indizes wie auf der echten Datenbank):
- Eingespielte Datei, dann die neue Fassung, zweimal: Rauchtests a–m bestanden; 128 Verbindungen, 97 Einheiten, 3 Lernende.
- Frische Kopie, nur die neue Fassung: bestanden.
- Gegenprobe 1: Mit dem alten Schutz (nur `freigegeben`) schlägt Rauchtest m fehl, mit „greift nicht bei Status geprueft“.
- Gegenprobe 2: Hat 48 schon vor dem Lauf eine Einheit `geprueft`, bricht die Migration vor der Löschung 49 ← 48 ab, und alles wird zurückgerollt (70 Verbindungen).

**Hinweis:** Die Datei muss weiterhin in **einer Transaktion** eingespielt werden. Sonst fehlt der Vorherstand für j, und die Sitzungsfunktion für m ist nicht mehr vorhanden.

## 0e. Nacharbeit 907 b (22.11. abends, „Rückläufer 22.11. abends“, Teil B)

Grundlage: `lernen-app` 6ec1c3ef. Die Datenbank habe ich nur gelesen, **nichts ausgeführt**. Berichtigt ist `supabase/migrations/20261122_lehrplan_nacharbeit_907.sql`; sie war noch nicht eingespielt.

**Fehler „cannot insert a non-DEFAULT value into column id“**
- Tatsache (gelesen): `id` ist in `schule.thema`, `schule.lernender`, `schule.route` und `schule.einheit` jeweils `GENERATED ALWAYS`.
- Die Datei legt kein Thema an. Der Abbruch kam aus Rauchtest k, der den Test-Lernenden und seine Route mit fester `id` einfügte. Lokal nachgestellt: Die alte Fassung bricht genau dort mit dieser Meldung ab.
- Behoben: Die `id` wird jetzt vergeben (`insert … returning id`), ohne feste Werte.
- Nebenwirkung: Die zurückgerollten Einfügungen verbrauchen je Lauf eine Nummer aus der Folge für Lernende und drei für Routen. Das ist harmlos, die Nummern bleiben nur ungenutzt.

**N2: aufgelöste Themen ohne Realschul- und IB-Klasse (Abschnitt 3d)**
- Klasse über `klasse_fest = null` geleert. `thema_jahrgang` legt `klasse_fest` über die Zuordnung und entfernt danach Nullen, so ist die Klasse auch dann leer, wenn eine Zuordnung eine Klasse liefert.
- Den Schlüssel in `lehrplan_reihenfolge` habe ich entfernt.
- Lernbereich- und Lehrplantexte bleiben als Herkunft stehen.
- Das Update greift nur, solange das Thema keine freigegebene Einheit hat.

| Thema | vorher | nachher |
|---|---|---|
| 12 Reinquadratische Gleichungen | RS 9 (Stelle 3), IB 4 (Stelle 10) | – |
| 27 Verhältnisse und Raten | IB 2 (Stelle 4) | – |
| 40 Graphentransformation | RS 9 (Stelle 12), IB 5 (Stelle 6) | – |
| 41 Folgen | IB 5 (Stelle 4) | – |
| 48 Vektoren und Determinanten | RS 7 (Stelle 5) | – |
| 72 Zinseszins | IB 4 (Stelle 14) | – |
| 77 Umkehrfunktionen | RS 10 (Stelle 8), IB 5 (Stelle 10) | – |
| 78 Parameter und Funktionenscharen | RS 8 (Stelle 7) | – |
| 82 Bedingte Wahrscheinlichkeit | IB 5 (Stelle 17) | – |
| 83 Mengen und Venn-Diagramme | IB 3 (Stelle 14) | – |

**Reihenfolgen nachgezogen:** 66 Reihenfolge-Werte in 51 Themen rücken auf; die Reihenfolge untereinander bleibt gleich. Je Klasse geänderte Themen: IB MYP 2: 8, IB MYP 4: 16, IB MYP 5: 11, RS 7: 15, RS 9: 13, RS 10: 3.

Damit hat RS 8 jetzt 6 statt 7 Themen (78 fällt weg). Der Befund „RS 8 dünn“ wird also deutlicher.

**N3:** Bei 83 Mengen ist `eigenstaendig` entfernt, in der Themenliste und in der Migration (`update … set eigenstaendig = null where id = 83`). Eigenständig sind jetzt 6 Themen: 15, 42, 57, 60, 65, 84.

**Rauchtest l (neu):** Kein Thema ohne freigegebene Einheit trägt eine Klasse, einen Reihenfolge-Schlüssel oder `eigenstaendig`. Rauchtest d prüft weiter, dass die Reihenfolge lückenlos ist.

**Folgen für Pläne und Reisen:** keine.
- Betroffen sind nur Realschule und IB; dort gibt es keine Kinder. Das Gymnasium bleibt unverändert.
- Keine Verbindung und keine Visum-Zeile ändert sich. Rauchtest j vergleicht die Reiseoptionen.

**Lokal geprüft auf Postgres 16.** Die Kopie hat `id`-Spalten mit `GENERATED ALWAYS` wie die echte Datenbank; die Zuordnungstabellen sind nicht nachgebaut, `thema_jahrgang` liest dort nur `klasse_fest` (Annahme: wirkt wegen der Null-Überlagerung gleich).
- Eingespielte Datei, dann die alte 907-Fassung: Abbruch „cannot insert a non-DEFAULT value into column id“.
- Eingespielte Datei, dann die neue Fassung, zweimal: Rauchtests a–l bestanden, 128 Verbindungen, 46 Visum-Zeilen, 3 Lernende.
- Frische Kopie, nur die neue Fassung: bestanden.
- Endstand der Kopie = `inhalte/themenliste.json` (Klasse, Reihenfolge, eigenständig): keine Abweichung.

**Tests:** `tests/lernen.test.cjs` mit 150 bestanden, 1 fehlgeschlagen. Das ist „LM-S 2 … eigenständig“, und er schlägt auch ohne meine Änderung fehl (Rückläufer Teil C, `bau-motivation`).

## 0d. Nacharbeit aus ChatGPTs Prüfergebnis 907 (22.11.)

Grundlage: `lernen-app` 986d43e7. Runde 30 c ist eingespielt, 102 ← 30 bleibt hart (Entscheidung Sebastian). Die Datenbank habe ich nur gelesen, **nichts ausgeführt**. Die eingespielte Datei `20261121_lehrplan_zuordnung_voraussetzungen.sql` ist unverändert.

**Neue Datei** `supabase/migrations/20261122_lehrplan_nacharbeit_907.sql`: berichtigte Fassung mit demselben Inhalt.
- Auf der Datenbank mit eingespielter Runde 30 c ändert ein Lauf nichts; der Rauchtest bestätigt das.
- Einzuspielen in **einer Transaktion**.

| Punkt aus 907 | Umsetzung |
|---|---|
| Rauchtest j: fehlender Vorherstand | Ohne Vorherstand jetzt **EXCEPTION** statt Hinweis. Der Vorherstand ist **transaktionslokal** (`set_config(…, true)`), deshalb kann kein veralteter Stand aus einer früheren Sitzung übrig sein. |
| Kopfkommentar „kein DELETE“ | Berichtigt: „Kein DROP. DELETE nur in Abschnitt 3c: genau die zwölf einzeln aufgezählten Verbindungen, jede nur nach Prüfung“. In der eingespielten Datei steht noch „kein DELETE“, weil die Kopfzeile beim Neuerzeugen in 30 c verloren ging. Die Datei bleibt so, wie sie eingespielt wurde. |
| Prüfung vor gezielten Löschungen | Abschnitt 3c ist ein Block mit Schleife über die 12 Paare. Vor jeder Löschung prüft er, dass das aufgelöste Thema der Zeile weiter **keine freigegebene Einheit** hat, sonst Abbruch ohne Löschung. |
| Testfall „Zielort offen, Voraussetzungs-Ort fehlt“ für 102 ← 30 | **Rauchtest k**, siehe unten. |

**Rauchtest k** prüft zuerst, dass `v_ort_visum` die Zeile „Terme umformen“ → „Potenzen“ enthält. Dann legt er einen erfundenen Test-Lernenden an: Klasse 5, `ist_test`, Anzeigename „Rauchtest 102←30“, mit Route. Er läuft in einem Unterblock, der am Ende sicher zurückgerollt wird; danach prüft der Test, dass kein solcher Lernender übrig ist. Echte Kinderdaten sind nicht beteiligt.
- k1: „Terme umformen“ offen, „Potenzen“ nicht auf der Route → Der Ort wird angeboten, `visum_fehlt` nennt „Potenzen“.
- k2: „Potenzen“ offen → ebenso gesperrt.
- k3: „Potenzen“ fertig → Die Sperre durch „Potenzen“ entfällt.

**Lokal auf Postgres 16 geprüft** (nachgebaute Tabellen und Funktionen, Daten aus dem gelesenen Stand):
- Erst die eingespielte, dann die neue Datei, jeweils in einer Transaktion: Alles bestanden. j meldet 46 → 46 Visum-Zeilen, die Verbindungen bleiben bei 128, es bleiben 3 Lernende.
- Auf einer frischen Kopie die neue Datei allein, zweimal hintereinander: bestanden.
- Gegenproben:
  - Ohne Abschnitt 0 bzw. ohne Transaktion bricht j mit „kein Vorherstand“ ab.
  - Wird 48 zum Schein freigegeben, bricht die Migration vor der Löschung 49 ← 48 ab, und alles wird zurückgerollt.
  - Mit 102 ← 30 als `empfohlen` schlägt k fehl.

## Offene Inhaltspunkte

- **Vektorkoordinaten für Determinanten (RS 7)** – offen, kein Bau beauftragt.
  - Thema 74 „Zweireihige Determinante“ (RS 7, Ort „Vektoren, Verschiebung und Drehung“) rechnet mit Vektorkoordinaten.
  - Der Flug dazu (48 Vektoren) ist aufgelöst, seine Etappen „Einen Vektor aus zwei Punkten“ und „Punkte mit Vektoren berechnen“ haben **in keinem freigegebenen Flug ein Gegenstück**.
  - Teilweise abgedeckt ist es durch 46 Kongruenzabbildungen (Verschiebung, Gegenvektor; RS 6) und 49 Matrizen (Bildpunkt; RS 10).
  - Seit 30 b ist die Verbindung 74 ← 48 gelöscht, ersatzweise gibt es 74 ← 46 (empfohlen) und 74 ← 50 (hart).
  - **Vorschlag:** In 46 oder 74 eine Etappe „Vektor aus zwei Punkten / Koordinaten eines Vektors“ ergänzen (Inhaltsauftrag, eigener Prüfgang). Danach prüfen, ob 74 ← 46 hart werden soll; dabei die Reise-Sperre beachten.
- Weitere Lücken aus Runde 30, nur als Vorschläge: RS 8 (Vierecke, Drehung, Baumdiagramm/Vierfeldertafel) und die Etappen der aufgelösten Themen ohne Gegenstück (Abschnitt 0, Tabelle „Wo der Stoff … heute steht“).

## 0c. Runde 30 c (21.11., „Rückläufer 21.11. morgens“, Teil A): harte Verbindungen und Reise-Sperren

Grundlage: `lernen-app` d463182a. Die Datenbank habe ich nur gelesen, die Migration auf der echten Datenbank **nicht ausgeführt**.

**Wie die Sperre entsteht (gelesen)**
- `schule.v_ort_visum` legt für jede **harte** Verbindung eine Zeile an: Ort des Themas braucht Ort der Voraussetzung, sofern es zwei verschiedene Orte sind (`block_thema`). Empfohlene Verbindungen zählen nicht.
- `schule.reiseoptionen(lernender)` nimmt je Kontinent den nächsten Ort der Route, der nicht fertig, nicht „kann schon“ und kein Zusatz-Ort ist. Für jeden Ort meldet sie, welche Visum-Orte des Kindes noch nicht fertig oder „kann schon“ sind (`visum_fehlt`). Gibt es Rückstands-Orte ohne fehlendes Visum, gilt Modus `pflicht` und nur diese Orte werden angeboten.
- Damit gilt: Jede harte Verbindung zwischen zwei Orten ist eine Reise-Sperre. Mein Satz „Plan-Folgen: keine“ aus 30 b war **falsch**.

**Was die Fassung 30 b bewirkt hätte (nachgerechnet)**
- `v_ort_visum` wäre von 49 auf 81 Zeilen gewachsen; das deckt sich mit dem Probelauf.
- Beim Kind Klasse 5 wären zwei Orte der Klasse 5 neu gesperrt worden:
  - „Größen und Einheiten“ (Grund: 25 ← 18 hart, braucht „Natürliche und ganze Zahlen“).
  - „Umfang und Fläche“ (Grund: 50 ← 42 hart, braucht „Formen und Grundbegriffe“).

**Entscheidung je neuer harter Verbindung**
- 39 der neuen harten Verbindungen hätten eine neue Reise-Sperre erzeugt.
- **38 davon sind jetzt `empfohlen`.** Begründung: Der Stoff hilft vorher, eine Sperre ist aber fachlich nicht zwingend. Meist ist es Grundschul- oder Klasse-5-Wissen, oder es sind parallele Orte derselben Klasse, deren Reihenfolge das Kind frei wählen soll. Die Liste steht unten.
- **Hart geblieben: 102 ← 30** (Potenzgesetze braucht Potenzen). Begründung: Ohne Potenzbegriff (Basis, Exponent) sind Potenzgesetze nicht lernbar; die Kette 30 → 102 → 29 verlangt der Auftrag.
  - Folge: Ort „Terme umformen“ braucht künftig das Visum „Potenzen“.
  - Für die heutigen Pläne ändert das nichts. Beim Kind Klasse 8 sind beide Orte fertig. Beim Kind Klasse 5 ist „Terme umformen“ aus der Route entfernt und wird nicht angeboten.
  - **Zur Entscheidung durch Sebastian:** hart lassen (empfohlen) oder auch `empfohlen`.
- Hart geblieben sind außerdem 13 neue Verbindungen ohne neue Sperre. Bei ihnen liegt die Voraussetzung im selben Ort, das Thema hat keinen Ort, oder die Sperre bestand schon.
- **Durch die Löschungen aus 30 b fallen 4 Visum-Zeilen weg.** Betroffen sind nur zwei Zusatz-Orte, „Zinseszins“ und „Statistik vertieft“. Zusatz-Orte bietet `reiseoptionen` nicht an, die heutigen Pläne bleiben gleich.
- Ergebnis: `v_ort_visum` hat **46 statt 49 Zeilen**. Neu ist nur „Terme umformen“ → „Potenzen“.

**Vorher/nachher je Kind (ohne Namen; vorher = heutige Datenbank, nachher = nach dieser Migration)**

**Kind Klasse 5** – Modus vorher `frei`, nachher `frei`.

| Ort (nächster je Kontinent) | vorher | nachher |
|---|---|---|
| Natürliche und ganze Zahlen (49), Klasse 5 | wählbar | wählbar |
| Größen und Einheiten (55), Klasse 5 | wählbar | wählbar |
| Einfache Gleichungen (64), Klasse 5 | gesperrt: Visum fehlt für Natürliche und ganze Zahlen (49) | gesperrt: Visum fehlt für Natürliche und ganze Zahlen (49) |
| Funktionsbegriff (73), Klasse 8 | gesperrt: Visum fehlt für Terme aufstellen (63) | gesperrt: Visum fehlt für Terme aufstellen (63) |
| Formen und Grundbegriffe (83), Klasse 5 | wählbar | wählbar |
| Umfang und Fläche (87), Klasse 5 | wählbar | wählbar |
| Daten darstellen (96), Klasse 6 | wählbar | wählbar |

Alle übrigen Orte der Route (nicht fertig, nicht „kann schon“), Unterschiede im Visum: Terme umformen (62) [7; Status entfernt]: vorher 63, 64 → nachher 44, 63, 64; Zinseszins (50) [Zusatz; Status offen, Zusatz-Ort]: vorher 49 → nachher –; Statistik vertieft (88) [Zusatz; Status offen, Zusatz-Ort]: vorher 45, 47, 92, 94 → nachher 94

**Kind Klasse 8** – Modus vorher `pflicht`, nachher `pflicht`.

| Ort (nächster je Kontinent) | vorher | nachher |
|---|---|---|
| Winkel (81), Klasse 5 | wählbar | wählbar |
| Median, Quartile, Boxplot (111), Klasse 7 | wählbar | wählbar |

Alle übrigen Orte der Route (nicht fertig, nicht „kann schon“), Unterschiede im Visum: Statistik vertieft (88) [Zusatz; Status offen, Zusatz-Ort]: vorher 92 → nachher –

**Testkind Klasse 7** – Modus vorher `frei`, nachher `frei`.

| Ort (nächster je Kontinent) | vorher | nachher |
|---|---|---|
| – keine Optionen (keine offenen Orte auf der Route) | – | – |

Alle übrigen Orte der Route (nicht fertig, nicht „kann schon“), Unterschiede im Visum: keine.

**Rauchtest j (neu)**
- Abschnitt 0 der Migration merkt sich vor allen Änderungen `reiseoptionen` aller Lernenden und die Zeilenzahl von `v_ort_visum` (Sitzungs-Einstellung `lb30.ro_vorher`, nur gelesen).
- Am Ende vergleicht der Rauchtest je Lernendem vorher und nachher. Jeder Unterschied wird mit der Lernenden-ID ausgegeben, die Migration bricht dann ab. Bei Gleichheit meldet er die Visum-Zahlen.
- Laufen Abschnitt 0 und Rauchtest nicht in derselben Sitzung, wird j mit Hinweis übersprungen.

**Geprüft auf einer lokalen Postgres-16-Kopie** (Tabellen und Funktionen `reiseoptionen`/`v_ort_visum` nachgebaut, Daten aus dem gelesenen Stand, keine Namen):
- Die Migration läuft durch, auch zweimal hintereinander. Rauchtest a–j bestanden, „Reiseoptionen unverändert; v_ort_visum vorher 49, nachher 46“.
- Gegenprobe: Mit 25 ← 18 wieder hart bricht Rauchtest j mit „Reiseoptionen geändert“ ab, und alles wird zurückgerollt.
- Das ist auch die Antwort auf den Hinweis zu LM-S: Der Funktionsrumpf ist damit wirklich ausgeführt, nicht nur von pglast gelesen.

**Auf `empfohlen` gesetzt (38)**

| Verbindung | wäre Visum | jetzt |
|---|---|---|
| 2 Lineare Gleichungen ← 16 Ganze Zahlen | Terme umformen → Natürliche und ganze Zahlen | empfohlen |
| 17 Teilbarkeit ← 18 Grundrechenarten und Rechengesetze | Teilbarkeit → Natürliche und ganze Zahlen | empfohlen |
| 21 Brüche und Anteile ← 18 Grundrechenarten und Rechengesetze | Brüche → Natürliche und ganze Zahlen | empfohlen |
| 22 Dezimalzahlen ← 21 Brüche und Anteile | Dezimalzahlen → Brüche | empfohlen |
| 23 Rechnen mit rationalen Zahlen ← 16 Ganze Zahlen | Rechnen mit Brüchen → Natürliche und ganze Zahlen | empfohlen |
| 23 Rechnen mit rationalen Zahlen ← 22 Dezimalzahlen | Rechnen mit Brüchen → Dezimalzahlen | empfohlen |
| 25 Größen und Einheiten ← 18 Grundrechenarten und Rechengesetze | Größen und Einheiten → Natürliche und ganze Zahlen | empfohlen |
| 28 Terme aufstellen und deuten ← 18 Grundrechenarten und Rechengesetze | Terme aufstellen → Natürliche und ganze Zahlen | empfohlen |
| 30 Potenzen und negative Exponenten ← 21 Brüche und Anteile | Potenzen → Brüche | empfohlen |
| 34 Gebrochen-rationale Funktionen ← 32 Zuordnung und Funktion | Hyperbeln → Funktionsbegriff | empfohlen |
| 43 Mit Winkeln rechnen ← 42 Grundbegriffe und Figuren | Winkel → Formen und Grundbegriffe | empfohlen |
| 44 Konstruktionen, Kongruenz und Beweise ← 43 Mit Winkeln rechnen | Dreiecke, Vierecke und Konstruktion → Winkel | empfohlen |
| 45 Kreis und Tangenten ← 42 Grundbegriffe und Figuren | Kreis → Formen und Grundbegriffe | empfohlen |
| 45 Kreis und Tangenten ← 98 Winkelsätze | Kreis → Dreiecke, Vierecke und Konstruktion | empfohlen |
| 46 Kongruenzabbildungen ← 42 Grundbegriffe und Figuren | Spiegeln und Symmetrie → Formen und Grundbegriffe | empfohlen |
| 50 Umfang und Flächeninhalt ← 42 Grundbegriffe und Figuren | Umfang und Fläche → Formen und Grundbegriffe | empfohlen |
| 52 Körper darstellen ← 42 Grundbegriffe und Figuren | Körper und Netze → Formen und Grundbegriffe | empfohlen |
| 59 Zweidimensionale Daten ← 33 Lineare Funktionen | Korrelation → Lineare Funktionen | empfohlen |
| 59 Zweidimensionale Daten ← 57 Daten erfassen und darstellen | Korrelation → Daten darstellen | empfohlen |
| 66 Lineare Optimierung ← 3 Lineare Ungleichungen | Graphen und Optimierung → Lineare Ungleichungen | empfohlen |
| 66 Lineare Optimierung ← 33 Lineare Funktionen | Graphen und Optimierung → Lineare Funktionen | empfohlen |
| 68 Elementare Wurzeln ← 67 Potenzen als Schreibweise | Wurzeln und reelle Zahlen → Natürliche und ganze Zahlen | empfohlen |
| 69 Intervalle ← 16 Ganze Zahlen | Lineare Ungleichungen → Natürliche und ganze Zahlen | empfohlen |
| 70 Schranken und Genauigkeit ← 22 Dezimalzahlen | Logik und Schranken → Dezimalzahlen | empfohlen |
| 74 Zweireihige Determinanten ← 50 Umfang und Flächeninhalt | Vektoren, Verschiebung und Drehung → Umfang und Fläche | empfohlen |
| 75 Betragsfunktion ← 16 Ganze Zahlen | Folgen, Reihen und Betrag → Natürliche und ganze Zahlen | empfohlen |
| 75 Betragsfunktion ← 32 Zuordnung und Funktion | Folgen, Reihen und Betrag → Funktionsbegriff | empfohlen |
| 76 Reihen ← 28 Terme aufstellen und deuten | Folgen, Reihen und Betrag → Terme aufstellen | empfohlen |
| 81 Stichproben und Aussagekraft ← 57 Daten erfassen und darstellen | Stichproben → Daten darstellen | empfohlen |
| 96 Rationale Exponenten und n-te Wurzel ← 103 Potenzgesetze mit ganzzahligen Exponenten | Rationale Exponenten → Bruchterme und Formeln | empfohlen |
| 98 Winkelsätze ← 43 Mit Winkeln rechnen | Dreiecke, Vierecke und Konstruktion → Winkel | empfohlen |
| 99 Flächen von Parallelogramm, Dreieck und Trapez ← 50 Umfang und Flächeninhalt | Flächen und Volumen → Umfang und Fläche | empfohlen |
| 100 Volumen ← 25 Größen und Einheiten | Flächen und Volumen → Größen und Einheiten | empfohlen |
| 100 Volumen ← 50 Umfang und Flächeninhalt | Flächen und Volumen → Umfang und Fläche | empfohlen |
| 101 Prismen und Zylinder ← 51 Kreisberechnungen | Körper und Netze → Kreis und Zylinder | empfohlen |
| 101 Prismen und Zylinder ← 99 Flächen von Parallelogramm, Dreieck und Trapez | Körper und Netze → Flächen und Volumen | empfohlen |
| 101 Prismen und Zylinder ← 100 Volumen | Körper und Netze → Flächen und Volumen | empfohlen |
| 103 Potenzgesetze mit ganzzahligen Exponenten ← 30 Potenzen und negative Exponenten | Bruchterme und Formeln → Potenzen | empfohlen |

Hart geblieben (keine neue Reise-Sperre: gleicher Ort, Thema ohne Ort oder Sperre bestand schon): 8 ← 68, 2 ← 28, 18 ← 15, 19 ← 67, 20 ← 68, 29 ← 102, 31 ← 29, 64 ← 61, 67 ← 18, 73 ← 42, 102 ← 28, 103 ← 102.


## 0. Nachbesserung Runde 30 b (21.11., Auftrag „Nachbesserung Dreißigste Runde und LM-S“, Teil A)

Grundlage: `lernen-app` 168a744b. Datenbank nur gelesen, Migration nicht ausgeführt. Der Rest der Runde 30 ist angenommen.

- **Thema 12 nicht ins Gymnasium.** `gym_by` ist entfernt, die Reihenfolge Gym 9 ist wieder wie vorher (68, 20, 35, 8, 7, …). Der Abschnitt dazu ist aus der Migration gestrichen. Rauchtest a prüft jetzt: 12 hat **keine** Gymnasium-Klasse.
- **Aufgelöste Themen:** genau die zehn aus dem Auftrag. Abgeglichen mit `schule.einheit`: Nur diese zehn haben keine freigegebene Einheit, nur `entwurf`.
- **Gelöscht** (einzeln, Abschnitt 3c der Migration; einzige Ausnahme vom Lösch-Verbot): 12 Zeilen in `schule.voraussetzung`, siehe Tabelle unten.
- **Gestrichen aus den neuen Verbindungen der Runde 30:** 8 Zeilen, die ein aufgelöstes Thema berühren. Das sind 13 ← 12, 27 ← 21, 40 ← 35, 40 ← 33, 41 ← 28, 48 ← 42, 48 ← 46 und 77 ← 36.
- **Ersatz:** 8 ← 68 (hart), 49 ← 46 (empfohlen), 74 ← 46 (empfohlen), 74 ← 50 (hart), 76 ← 28 (hart).
- **Zahlen:** vorher 70 Verbindungen; 12 gelöscht, 70 neu; nachher **128**.
- **Neue Rauchtest-Regel i:** Keine Verbindung darf von oder zu einem Thema ohne freigegebene Einheit gehen. Ausnahme: Die Begründung beginnt ausdrücklich mit „Ausnahme:“. Solche Ausnahmen gibt es derzeit keine.
- **Regel b angepasst:** Sie gilt nur noch für Themen mit freigegebener Einheit. Sonst müssten die aufgelösten Themen eine Verbindung haben und würden Regel i verletzen.
- 83 Mengen ist aufgelöst und trägt trotzdem weiter die Kennzeichnung `eigenstaendig` (aus Runde 30 angenommen). Das ist harmlos, weil das Thema keine Verbindungen hat. Entfernen wäre auch möglich.

### Gelöschte Zeilen

| Zeile (Thema ← braucht) | Art | Grund | Ersatz |
|---|---|---|---|
| 8 Quadratische Gleichungen ← 12 | hart | Stoff von 12 ist Etappe `reinquadratisch` in 8 selbst | 8 ← 68 Elementare Wurzeln (hart) |
| 12 ← 68 | hart | 12 aufgelöst | – |
| 49 Matrizen ← 48 Vektoren | empfohlen | 48 aufgelöst | 49 ← 46 Kongruenzabbildungen (empfohlen: Verschiebung, Gegenvektor) |
| 74 Determinanten ← 48 Vektoren | hart | 48 aufgelöst | 74 ← 46 (empfohlen), 74 ← 50 Umfang und Flächeninhalt (hart) |
| 76 Reihen ← 41 Folgen | hart | Folgen sind jetzt Etappen in 76 selbst | 76 ← 28 Terme aufstellen (hart) |
| 72 ← 67, 72 ← 71 | hart, empfohlen | 72 aufgelöst | – |
| 77 ← 32 | hart | 77 aufgelöst | – |
| 78 ← 33 | empfohlen | 78 aufgelöst | – |
| 82 ← 21, 82 ← 23, 82 ← 61 | hart | 82 aufgelöst | – |

Kein freigegebener Flug braucht danach ein aufgelöstes Thema (Regel i, per Skript nachgerechnet). Die Ersatz-Verbindungen erfüllen auch Regel g: keine Voraussetzung in einer späteren Klasse.

### Wo der Stoff der aufgelösten Themen heute steht

Die Zuordnung habe ich per Skript über die Etappen der Themendateien gefunden, gleicher Etappenschlüssel oder gleicher Titel. Wo nichts passt, ist das vermerkt.

| Aufgelöst | heute im Flug (Etappe) |
|---|---|
| 12 Reinquadratische Gleichungen | 8 `gleichungen.quadratisch` (`reinquadratisch` „Gleichungen ohne x-Glied lösen“) |
| 27 Verhältnisse und Raten | 21 `bruch.brueche` (`verhaeltnis_kuerzen`, `gleichwertig`); 5 `gleichungen.bruch` (`verhaeltnis`); 26 `groessen.proportional` (`aenderung`). Ohne Gegenstück: „Im Verhältnis aufteilen“, „Einheitsraten und Stückpreise“. |
| 40 Graphentransformation | 35 `funktionen.quadratisch` (`parameter`, `spiegeln`); 34 `funktionen.gebrochen` (`parameter`); 38 `funktionen.trig` (`parameter`, `verschiebung_x`) |
| 41 Folgen | 76 `funktionen.reihen` (`rekursiv`, `arithmetisch`, `geometrisch`). Ohne Gegenstück: „Folgenglieder berechnen“ (explizit). |
| 48 Vektoren und Determinanten | 46 `abbildungen.kongruenz` (`verschiebung`, `gegenvektor`); 49 `abbildungen.matrizen` (`bildpunkt`). Ohne Gegenstück: „Einen Vektor aus zwei Punkten“, „Punkte mit Vektoren berechnen“. **Lücke für RS 7**, weil 74 Determinanten Vektorkoordinaten nutzt. |
| 72 Zinseszins | 94 `bruch.prozent_grundwert` (`faktor`, `formel` „Kapital nach n Jahren“, `mehrfach`); 37 `funktionen.exponential_log` (`faktor`) |
| 77 Umkehrfunktionen | 36 `funktionen.potenz` (`umkehrbar`, `linear`, `quadratisch`, `spiegeln`, `wurzelfunktion`). Ohne Gegenstück: „Exponential- und Logarithmusfunktion“; 37 hat nur `logfunktion`. |
| 78 Parameter und Funktionenscharen | 33 `funktionen.linear` (`einsetzen`, `wirkung`, `bueschel`); 6 `gleichungen.lgs2` (`loesung_parameter`) |
| 82 Bedingte Wahrscheinlichkeit | 63 `stochastik.verknuepft` (`vierfeld`, `tafel_wkeit`, `bedingt`, `rueckschluss`); 62 `stochastik.mehrstufig` (`ohne_zuruecklegen`, `unabhaengig`) |
| 83 Mengen und Venn-Diagramme | 63 `stochastik.verknuepft` (`elemente`, `schnitt`, `venn`, `mengen_verstehen`) |

**Befund, nicht geändert:** Die zehn aufgelösten Themen tragen in Themenliste und Datenbank weiter Klassen und Reihenfolgen für RS und IB (12: RS 9 / IB 4; 27: IB 2; 40: RS 9 / IB 5; 41: IB 5; 48: RS 7; 72: IB 4; 77: RS 10 / IB 5; 78: RS 8; 82: IB 5; 83: IB 3). Laut Auftrag kennzeichnet die Matrix sie mit `ohne_flug` (Teil B). Soll das Gymnasium-Prinzip auch für RS/IB gelten, ist das ein eigener Auftrag: Die Reihenfolgen müssten dann neu nummeriert werden.

**Plan-Folgen von Runde 30 b:** ~~keine~~ – **falsch**: Harte Verbindungen erzeugen Reise-Sperren (`v_ort_visum`). Die Berichtigung steht in Abschnitt 0c.

## 1. Themen ohne Klasse (Runde 30)

| Thema | Ergebnis | Beleg / Annahme |
|---|---|---|
| 12 Reinquadratische Gleichungen | ~~Gym 9 neu~~ **zurückgenommen (Runde 30 b)**: für das Gymnasium aufgelöst, Stoff als Etappe in 8 | Tatsache: Gym 9 M9 2.1 „Quadratische Funktionen und quadratische Gleichungen“ verlangt das Lösen quadratischer Gleichungen (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/9/mathematik). Annahme: x² = a ist dort der einfachste Fall; der Lehrplan nennt ihn nicht eigens. |
| 40 Graphentransformation | Gym bleibt ohne Klasse | Tatsache: Parameter der Scheitelform in M9 2.1, a·sin(b(x+c))+d in M10 3; allgemeine Transformationen erst Jgst. 11 (Fachprofil Gymnasium Mathematik; Servicematerial https://www.lehrplanplus.bayern.de/serviceinformation/l338447). Das Thema ist allgemein angelegt → nicht Gym 5–10. |
| 77 Umkehrfunktionen | Gym bleibt ohne Klasse | Tatsache: Term der Umkehrfunktion erst Gym 12 M12 4.2 Wurzelfunktion (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/12/mathematik). |
| 13 Wurzelgleichungen | Gym bleibt ohne Klasse | Tatsache: RS 9 (I) LB 7 „lösen Wurzelgleichungen und beachten dabei die Definitionsmenge“ (https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/9/mathematik/wpfg1). **Annahme:** in Gym 5–10 keine Fundstelle; ein ausdrückliches „nicht“ habe ich nicht gefunden. |
| 4 Formeln umstellen (RS) | RS bleibt ohne Klasse | **Annahme:** keine eigene Kompetenzerwartung in RS 5–10 gefunden; Umstellen kommt in RS 7 LB 6 (Äquivalenzumformungen) und in 101 Prismen und Zylinder (RS 9) vor. |
| 4 Formeln umstellen (Gym) | **Lernbereich berichtigt**: „M8 1 Funktion und Term“ statt „M8 4 Bruchterme …“ | Tatsache: Gym 8 M8 1 „lösen Formeln – insbesondere aus den Naturwissenschaften – nach einer Variablen auf“ (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/8/mathematik). Reihenfolge Gym 8 (Stelle 10) **nicht** geändert, siehe Vorschlag V1. |
| Stichprobe 7 LGS mit 3 Unbekannten | Gym 9 bestätigt | Tatsache: M9 2.2 „stellen lineare Gleichungssysteme mit drei Unbekannten auf …“ (https://www.lehrplanplus.bayern.de/fachlehrplan/lernbereich/217156). |
| Stichprobe 11 Polynomgleichungen | Gym 10 bestätigt | Tatsache: M10 4 Ganzrationale Funktionen, Nullstellen auch über Substitution (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/10/mathematik); laut Servicematerial ohne Polynomdivision (https://www.lehrplanplus.bayern.de/serviceinformation/l301512). |

Ein Gymnasiast lernt den Stoff von 12 im Flug 8, Etappe `reinquadratisch` (Runde 30 b).

## 2. Realschule 7 (20 Themen) und 8 (7 Themen)

- **RS 7 = 20: stimmig.** Alle 8 Lernbereiche von RS 7 (I) sind belegt (https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/7/mathematik/wpfg1). Zwei Auffälligkeiten, nicht geändert:
  - 95 Boxplot (RS 7, Lernbereich „M7 8“) steht nicht im RS-Lehrplan; die Liste nennt es selbst „Annahme Vertiefung“. → Vorschlag V2.
  - 29 Terme umformen (RS 7) enthält Inhalte aus RS 8 LB 4 (Summe mal Summe, Faktorisieren, binomische Formeln). → Vorschlag V3.
- **RS 8 = 7: dünn wegen fehlender Themen, nicht wegen falscher Zuordnung** (https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/8/mathematik/wpfg1). Ohne App-Thema: LB 1 Vierecke, LB 2 Drehung (46 Kongruenz steht in RS 6), LB 7 Daten und Zufall (Ergebnis/Ereignis, Baumdiagramm, Vierfeldertafel). 61 und 63 bleiben RS 9 (Laplace in RS 9 LB 8). → Vorschlag V4.

## 3. Voraussetzungen

- Vorher: 70 Verbindungen, 7 Themen ganz ohne Eintrag mit Klasse und ohne Kennzeichen. Nachher nach Runde 30 b: **128 Verbindungen** (70 neu, 12 gelöscht), 7 Themen ausdrücklich **eigenständig**. Jedes Thema mit Klasse **und freigegebener Einheit** hat danach Voraussetzungen oder „eigenständig“ (Rauchtest b).
- **Ablage „eigenständig“ (Nachtrag Gestalter):**
  - Datenbank: neue Spalte **`schule.thema.eigenstaendig`** (`text`, Begründung). Nicht leer heißt: bewusst ohne Voraussetzung. Leer heißt: nicht gekennzeichnet.
  - Themenliste: Feld **`eigenstaendig`** (Text) an 15, 42, 57, 60, 65, 83, 84.
  - Damit das Übersichtsblatt das anzeigen kann, muss die Lese-Schnittstelle die Spalte mitliefern (LM-S). Das ist hier nicht gebaut.
- **Pflichtkette Potenz:** 30 → 102 → 29 (hart) und 102 → 103 (hart), dazu 30 → 103 (seit 30 c `empfohlen`, sonst neue Reise-Sperre). Fehlen 102/103, überspringt die Migration diese Zeilen (Prüfung `where exists`).
- **Quelle:** Die Abhängigkeiten sind fachliche **Annahmen**, gestützt auf die Reihenfolge der Lernbereiche im LehrplanPLUS. Ausdrücklich belegt sind nur einzelne: 7 ← 6 (Servicematerial https://www.lehrplanplus.bayern.de/serviceinformation/l298115: LGS 3 greift auf M8 6 zurück), 11 ← 8 (l301512: Jgst. 10 baut auf quadratischen Gleichungen aus Jgst. 9 auf).
- **Selbstprüfung im Rauchtest** (Regeln des Gestalters):
  - b) Kein Thema mit Klasse und freigegebener Einheit bleibt ohne Verbindung, außer es ist eigenständig.
  - i) (Runde 30 b) Keine Verbindung geht von oder zu einem Thema ohne freigegebene Einheit, außer die Begründung beginnt mit „Ausnahme:“.
  - g) Keine Voraussetzung (hart oder empfohlen) liegt je Schulart in einer späteren Klasse als das Thema.
  - h) Die Themen 100–103 haben je mindestens eine Voraussetzung.
  - Dazu: a) 12 ohne Gym-Klasse; c) keine Kreise; d) Reihenfolge lückenlos und eindeutig; e) die Kette 30 → 102 → 29 und 102 → 103; f) Lernbereich 4.
  - Alle Regeln sind per Skript auf die Themenliste nachgerechnet und erfüllt.
- Wegen Regel g habe ich fünf zuerst geplante empfohlene Verbindungen weggelassen: 9 ← 96, 47 ← 5, 50 ← 25, 73 ← 46 und 103 ← 31. Die Voraussetzung läge sonst in IB, Gym oder RS eine Klasse später.
- **Geändert wegen Regel g (nur IB):** Die vorhandene harte Verbindung 33 Lineare Funktionen ← 32 Zuordnung und Funktion verstieß gegen die Regel: 32 stand in MYP 4, 33 in MYP 3.
  - Jetzt steht **32 in MYP 3** an Stelle 5, direkt vor 33. MYP 3 und MYP 4 sind neu nummeriert.
  - **Annahme:** Das IB-Framework nennt für die Funktionsschreibweise MYP 4–5. Der Lehrplantext von 32 sagt das jetzt ausdrücklich.
  - Die Alternative wäre, 33 nach MYP 4 hinter 32 zu setzen. Das ist **deine Entscheidung**, falls du es anders willst.
  - Kein Kind ist betroffen.
- **Befund, nicht geändert (alt, nur IB):** Bei 10 ← 37, 26 ← 25 und 92 ← 54 steht die harte Voraussetzung in derselben Klasse weiter hinten. Die Regeln des Gestalters erlauben das, die Reihenfolge ist aber unlogisch. → Vorschlag V5.

## 3a. Ablage „eigenständig“ – genau (Nachtrag des Gestalters)

- **Ort:** Spalte `eigenstaendig` in der Tabelle `schule.thema`. Es gibt keinen Eintrag in `schule.voraussetzung`, denn deren Spalte `braucht_id` muss auf ein anderes Thema zeigen und darf nicht leer sein.
- **Form:** `text`, ohne Vorgabewert. Angelegt in Schritt 1 der Migration mit `alter table schule.thema add column if not exists eigenstaendig text` und einem Spaltenkommentar.
- **Bedeutung:**
  - Nicht leer: Das Thema hat bewusst keine Voraussetzung. Der Text ist die Begründung.
  - `null`: nicht gekennzeichnet.
  - Die Kennzeichnung gilt für alle Schularten.
- **Gefüllt** in Schritt 5 der Migration für 15, 42, 57, 60, 65, 83, 84.
- **Abfrage:** `select id, eigenstaendig from schule.thema where eigenstaendig is not null`.
- **Themenliste:** Feld `"eigenstaendig": "<Begründung>"` am Eintrag. Fehlt das Feld, ist das Thema nicht gekennzeichnet.
- **Anzeige:** Das Übersichtsblatt braucht die Spalte in der Lese-Schnittstelle (LM-S). Heute liefert `api.schule_lehrplan_lesen` sie nicht; das ist hier nicht gebaut.
- **Stand Datenbank (gelesen 21.11.):**
  - 102 und 103 sind angelegt (Gym 7/8, RS 7, IB 3/4) und haben noch keine Voraussetzung.
  - Die Migration legt 102 ← 30, 102 ← 28, 103 ← 102 und 103 ← 30 an, dazu 29 ← 102 und 96 ← 103.
  - Ihr Schutz für fehlende Themen greift damit nicht mehr, schadet aber nicht.

## 4. Was den Plan eines Kindes verschieben würde (ohne Namen)

Betroffen sind nur Gymnasium-Kinder: zwei echte (Klasse 5 und Klasse 8) und das Testkind (Klasse 7). Kinder an RS oder IB gibt es nicht; die IB-Änderung (32 nach MYP 3, Reihenfolge MYP 3/4) trifft also niemanden.

1. ~~Thema 12 bekommt Gym-Klasse 9; Gym 9 neu nummeriert~~ – in Runde 30 b zurückgenommen, entfällt.
2. **Lernbereich von 4** heißt jetzt M8 1 statt M8 4. Die Reihenfolge bleibt gleich. **Annahme:** Gruppiert eine Ansicht nach Lernbereich, wandert das Thema dort in eine andere Gruppe. Für das Kind in Klasse 8 betrifft das die laufende Klasse.
3. **Berichtigt (30 c):** Die Reihenfolge ändern die Voraussetzungen nicht, aber **harte Verbindungen sperren Reisen** über `schule.v_ort_visum` und `schule.reiseoptionen`. Siehe Abschnitt 0c. `eigenstaendig` hat keinen Einfluss.

## 5. Vorschläge (nicht umgesetzt)

- V1: 4 Formeln umstellen in Gym 8 hinter 32 Zuordnung und Funktion setzen. Das passt zu M8 1, verschiebt aber den Plan des Kindes in Klasse 8.
- V2: 95 Boxplot in RS ohne Klasse lassen oder ausdrücklich als Vertiefung kennzeichnen.
- V3: 29 für RS teilen: RS 7 Zusammenfassen, RS 8 Ausmultiplizieren, Faktorisieren und binomische Formeln.
- V4: Neue Flüge für RS 8: Vierecke, Drehung, Baumdiagramm/Vierfeldertafel.
- V5: IB-Reihenfolge in MYP 2, 3 und 5 an die harten Voraussetzungen 26 ← 25, 92 ← 54 und 10 ← 37 anpassen. Kein IB-Kind ist betroffen.

## 6. Dateien

- `inhalte/themenliste.json`: 4 (Lernbereich Gym), Feld `eigenstaendig` an 15, 42, 57, 60, 65, 83, 84; 32 nach IB MYP 3 (Klasse, Lernbereich, `lehrplan_ib`), Reihenfolge IB MYP 3 und 4.
- `supabase/migrations/20261121_lehrplan_zuordnung_voraussetzungen.sql`: wiederholt ausführbar, ohne DROP/DELETE, **nicht ausgeführt**. Mit Rauchtest (a–j), der bei Fehlern abbricht. Löscht nur die 12 aufgezählten Zeilen (3c). Syntax mit pglast geprüft.
- Selbstprüfung: Reihenfolge je Schulart und Klasse lückenlos und eindeutig. Tests `tests/lernen.test.cjs` 135/135 grün. `tools/inhalt_pruefen.py --alle` zeigt nur dieselben Hinweise wie vorher.

## Anhang: Voraussetzungen je Thema (Stand Runde 30 c)

| Nr | Thema | Gym | RS | IB | direkte Voraussetzungen (Art, Begründung) |
|---|---|---|---|---|---|
| 1 | Einfache Gleichungen | 5 | 6 | 1 | 18 Grundrechenarten und Rechengesetze (hart, vorhanden) |
| 2 | Lineare Gleichungen | 7 | 7 | 2 | 1 Einfache Gleichungen (hart, vorhanden); 28 Terme aufstellen und deuten (hart, Gleichungen bestehen aus Termen mit Variablen); 16 Ganze Zahlen (empfohlen, Lösungen und Umformungen mit negativen Zahlen) |
| 3 | Lineare Ungleichungen | 8 | 7 | 4 | 2 Lineare Gleichungen (hart, vorhanden) |
| 4 | Formeln umstellen | 8 | – | 4 | 2 Lineare Gleichungen (hart, vorhanden); 29 Terme umformen (empfohlen, beim Umstellen werden Terme umgeformt) |
| 5 | Bruch- und Verhältnisgleichungen | 8 | 8 | 4 | 2 Lineare Gleichungen (hart, vorhanden); 31 Bruchterme (hart, vorhanden) |
| 6 | Gleichungssysteme mit 2 Unbekannten | 8 | 9 | 4 | 2 Lineare Gleichungen (hart, vorhanden); 33 Lineare Funktionen (empfohlen, graphisches Lösen über den Schnittpunkt zweier Geraden) |
| 7 | Gleichungssysteme mit 3 Unbekannten | 9 | – | – | 6 Gleichungssysteme mit 2 Unbekannten (hart, vorhanden) |
| 8 | Quadratische Gleichungen (allgemein) | 9 | 9 | 4 | 2 Lineare Gleichungen (hart, vorhanden); 29 Terme umformen (hart, vorhanden); 68 Elementare Wurzeln (hart, Etappe reinquadratisch: x² = a mit der Quadratwurzel lösen (Stoff von 12 steht jetzt hier)) |
| 9 | Potenzgleichungen | 9 | 10 | 4 | 20 Wurzeln und reelle Zahlen (hart, vorhanden) |
| 10 | Exponentialgleichungen | 10 | 10 | 5 | 37 Exponential- und Logarithmusfunktionen (hart, vorhanden) |
| 11 | Polynomgleichungen | 10 | – | – | 8 Quadratische Gleichungen (allgemein) (hart, vorhanden); 39 Ganzrationale Funktionen (empfohlen, Nullstellen ganzrationaler Funktionen = Lösungen der Polynomgleichung) |
| 12 | Reinquadratische Gleichungen | – | 9 | 4 | **aufgelöst** (Entwurf ohne freigegebene Einheit) – keine Verbindungen |
| 13 | Wurzelgleichungen | – | 9 | – | 68 Elementare Wurzeln (hart, vorhanden); 8 Quadratische Gleichungen (allgemein) (empfohlen, Wurzelgleichungen führen oft auf quadratische Gleichungen) |
| 14 | Trigonometrische Gleichungen | 9 | 10 | 5 | 56 Allgemeine Trigonometrie (hart, vorhanden) |
| 15 | Natürliche Zahlen | 5 | 5 | 1 | **eigenständig** – Einstieg Klasse 5; setzt nur Grundschulwissen voraus |
| 16 | Ganze Zahlen | 5 | 5 | 2 | 15 Natürliche Zahlen (hart, vorhanden) |
| 17 | Teilbarkeit | 5 | 5 | 1 | 18 Grundrechenarten und Rechengesetze (empfohlen, Teiler und Vielfache beruhen auf Multiplizieren und Dividieren) |
| 18 | Grundrechenarten und Rechengesetze | 5 | 5 | 1 | 15 Natürliche Zahlen (hart, Rechnen im Stellenwertsystem mit natürlichen Zahlen) |
| 19 | Zehnerpotenzen und wissenschaftliche Schreibweise | 6 | 7 | 4 | 67 Potenzen als Schreibweise (hart, Potenzbegriff: Basis und Exponent); 22 Dezimalzahlen (empfohlen, kleine Zahlen als Dezimalzahl und als Zehnerpotenz) |
| 20 | Wurzeln und reelle Zahlen | 9 | 9 | 4 | 68 Elementare Wurzeln (hart, Quadratwurzel als Grundbegriff) |
| 21 | Brüche und Anteile | 6 | 6 | 1 | 18 Grundrechenarten und Rechengesetze (empfohlen, Bruch als Teilen; Kürzen und Erweitern durch Multiplizieren und Dividieren); 17 Teilbarkeit (empfohlen, Kürzen mit gemeinsamen Teilern) |
| 22 | Dezimalzahlen | 6 | 6 | 1 | 21 Brüche und Anteile (empfohlen, Dezimalzahlen als Zehnerbrüche) |
| 23 | Rechnen mit rationalen Zahlen | 6 | 6 | 2 | 21 Brüche und Anteile (hart, vorhanden); 22 Dezimalzahlen (empfohlen, rationale Zahlen auch als Dezimalzahlen); 16 Ganze Zahlen (empfohlen, Vorzeichenregeln der ganzen Zahlen) |
| 24 | Prozent- und Zinsrechnung | 6 | 6 | 1 | 21 Brüche und Anteile (hart, vorhanden); 22 Dezimalzahlen (empfohlen, Prozentsätze als Dezimalzahl) |
| 25 | Größen und Einheiten | 5 | 5 | 2 | 18 Grundrechenarten und Rechengesetze (empfohlen, Umrechnen durch Multiplizieren und Dividieren mit 10, 100, 1000) |
| 26 | Direkte Proportionalität und Dreisatz | 5 | 6 | 2 | 25 Größen und Einheiten (hart, vorhanden) |
| 27 | Verhältnisse und Raten | – | – | 2 | **aufgelöst** (Entwurf ohne freigegebene Einheit) – keine Verbindungen |
| 28 | Terme aufstellen und deuten | 7 | 6 | 1 | 18 Grundrechenarten und Rechengesetze (empfohlen, Rechenarten und Rechengesetze in Termen) |
| 29 | Terme umformen | 7 | 7 | 3 | 28 Terme aufstellen und deuten (hart, vorhanden); 102 Potenzgesetze (hart, Produkte wie a · a² · a³ brauchen das Potenzgesetz) |
| 30 | Potenzen und negative Exponenten | 6 | 7 | 3 | 18 Grundrechenarten und Rechengesetze (hart, vorhanden); 67 Potenzen als Schreibweise (hart, vorhanden); 21 Brüche und Anteile (empfohlen, negativer Exponent bedeutet Kehrbruch) |
| 31 | Bruchterme | 8 | 8 | 4 | 23 Rechnen mit rationalen Zahlen (hart, vorhanden); 29 Terme umformen (hart, Zähler und Nenner werden als Terme umgeformt) |
| 32 | Zuordnung und Funktion | 8 | 8 | 3 | 28 Terme aufstellen und deuten (hart, vorhanden) |
| 33 | Lineare Funktionen | 8 | 8 | 3 | 2 Lineare Gleichungen (hart, vorhanden); 32 Zuordnung und Funktion (hart, vorhanden) |
| 34 | Gebrochen-rationale Funktionen | 8 | – | 4 | 32 Zuordnung und Funktion (empfohlen, Funktionsbegriff, Definitionsmenge); 93 Indirekte Proportionalität (empfohlen, indirekte Proportionalität führt auf die Hyperbel) |
| 35 | Quadratische Funktionen | 9 | 9 | 4 | 29 Terme umformen (empfohlen, vorhanden); 32 Zuordnung und Funktion (hart, vorhanden); 33 Lineare Funktionen (empfohlen, vorhanden) |
| 36 | Potenzfunktionen | 9 | 10 | 4 | 32 Zuordnung und Funktion (hart, vorhanden); 35 Quadratische Funktionen (empfohlen, Parabel als erste Potenzfunktion) |
| 37 | Exponential- und Logarithmusfunktionen | 10 | 10 | 5 | 30 Potenzen und negative Exponenten (hart, vorhanden); 32 Zuordnung und Funktion (hart, vorhanden); 103 Potenzgesetze mit ganzzahligen Exponenten (empfohlen, Potenzgesetze mit ganzzahligen Exponenten) |
| 38 | Sinus- und Kosinusfunktion | 10 | 10 | 5 | 56 Allgemeine Trigonometrie (hart, vorhanden) |
| 39 | Ganzrationale Funktionen | 10 | – | 5 | 35 Quadratische Funktionen (hart, vorhanden) |
| 40 | Graphentransformation | – | 9 | 5 | **aufgelöst** (Entwurf ohne freigegebene Einheit) – keine Verbindungen |
| 41 | Folgen | – | – | 5 | **aufgelöst** (Entwurf ohne freigegebene Einheit) – keine Verbindungen |
| 42 | Grundbegriffe und Figuren | 5 | 5 | 1 | **eigenständig** – Einstieg Geometrie Klasse 5; setzt nur Grundschulwissen voraus |
| 43 | Mit Winkeln rechnen | 5 | 5 | 1 | 42 Grundbegriffe und Figuren (empfohlen, Strahl, Scheitel und Gerade) |
| 44 | Konstruktionen, Kongruenz und Beweise | 7 | 7 | 3 | 43 Mit Winkeln rechnen (empfohlen, Winkel messen und zeichnen); 98 Winkelsätze (empfohlen, Winkelsumme bei Existenz und Konstruktion von Dreiecken); 46 Kongruenzabbildungen (empfohlen, Grundkonstruktionen (Mittelsenkrechte, Lot, Winkelhalbierende)) |
| 45 | Kreis und Tangenten | 7 | 7 | 4 | 42 Grundbegriffe und Figuren (empfohlen, Kreis, Radius, Gerade); 98 Winkelsätze (empfohlen, Satz des Thales wird über die Winkelsumme im Dreieck begründet); 73 Ortslinien und Ortsbereiche (empfohlen, Umkreis und Inkreis über Mittelsenkrechte und Winkelhalbierende) |
| 46 | Kongruenzabbildungen | 7 | 6 | 3 | 42 Grundbegriffe und Figuren (empfohlen, Gerade, Senkrechte, Koordinatensystem) |
| 47 | Ähnlichkeit und Strahlensätze | 9 | 9 | 3 | 46 Kongruenzabbildungen (empfohlen, vorhanden) |
| 48 | Vektoren und Determinanten | – | 7 | – | **aufgelöst** (Entwurf ohne freigegebene Einheit) – keine Verbindungen |
| 49 | Matrizen und Abbildungen mit Matrizen | – | 10 | 5 | 46 Kongruenzabbildungen (empfohlen, Verschiebung und Gegenvektor aus den Kongruenzabbildungen (ersetzt 48)) |
| 50 | Umfang und Flächeninhalt | 5 | 5 | 1 | 42 Grundbegriffe und Figuren (empfohlen, Rechteck, Quadrat und Vielecke) |
| 51 | Kreisberechnungen | 8 | 9 | 3 | 50 Umfang und Flächeninhalt (hart, vorhanden) |
| 52 | Körper darstellen | 8 | 5 | 3 | 42 Grundbegriffe und Figuren (empfohlen, ebene Figuren für Netze und Seitenflächen) |
| 53 | Volumen und Oberfläche | 5 | 6 | 1 | 50 Umfang und Flächeninhalt (hart, vorhanden) |
| 54 | Satz des Pythagoras | 9 | 9 | 3 | 68 Elementare Wurzeln (hart, vorhanden) |
| 55 | Trigonometrie im rechtwinkligen Dreieck | 9 | 9 | 4 | 47 Ähnlichkeit und Strahlensätze (hart, vorhanden); 54 Satz des Pythagoras (empfohlen, fehlende Seiten mit Pythagoras) |
| 56 | Allgemeine Trigonometrie | 9 | 10 | 4 | 55 Trigonometrie im rechtwinkligen Dreieck (hart, vorhanden) |
| 57 | Daten erfassen und darstellen | 6 | 5 | 1 | **eigenständig** – Zählen und Ablesen aus der Grundschule genügen |
| 58 | Mittelwert und Häufigkeiten | 6 | 7 | 2 | 57 Daten erfassen und darstellen (empfohlen, vorhanden); 22 Dezimalzahlen (empfohlen, Mittelwerte sind oft Dezimalzahlen) |
| 59 | Zweidimensionale Daten | – | – | 5 | 57 Daten erfassen und darstellen (empfohlen, Daten erfassen und darstellen); 33 Lineare Funktionen (empfohlen, Trendgerade als lineare Funktion) |
| 60 | Zählen und Kombinatorik | 5 | 5 | 2 | **eigenständig** – systematisches Zählen; setzt nur Grundschulwissen voraus |
| 61 | Zufall und Laplace | 8 | 9 | 2 | 21 Brüche und Anteile (hart, vorhanden) |
| 62 | Mehrstufige Zufallsexperimente | 10 | 10 | 4 | 23 Rechnen mit rationalen Zahlen (hart, vorhanden); 61 Zufall und Laplace (hart, vorhanden) |
| 63 | Verknüpfte Ereignisse | 9 | 9 | 4 | 61 Zufall und Laplace (hart, vorhanden) |
| 64 | Simulation | 10 | 9 | 2 | 61 Zufall und Laplace (hart, Zufallsexperiment und relative Häufigkeit) |
| 65 | Graphentheorie | – | – | 4 | **eigenständig** – Entdecker-Insel mit eigenen Begriffen (Knoten, Kanten) |
| 66 | Lineare Optimierung | – | – | 5 | 3 Lineare Ungleichungen (empfohlen, Bedingungen als lineare Ungleichungen); 33 Lineare Funktionen (empfohlen, Randgeraden zeichnen) |
| 67 | Potenzen als Schreibweise | 5 | 5 | 1 | 18 Grundrechenarten und Rechengesetze (hart, Potenz als wiederholtes Multiplizieren) |
| 68 | Elementare Wurzeln | 9 | 9 | 1 | 67 Potenzen als Schreibweise (empfohlen, Quadratzahlen) |
| 69 | Intervalle | 8 | 7 | 4 | 16 Ganze Zahlen (empfohlen, Zahlengerade mit negativen Zahlen) |
| 70 | Schranken und Genauigkeit | – | – | 5 | 22 Dezimalzahlen (empfohlen, Runden von Dezimalzahlen) |
| 71 | Zinsen | 6 | 7 | 4 | 24 Prozent- und Zinsrechnung (hart, vorhanden) |
| 72 | Zinseszins | – | – | 4 | **aufgelöst** (Entwurf ohne freigegebene Einheit) – keine Verbindungen |
| 73 | Ortslinien und Ortsbereiche | 5 | 7 | – | 42 Grundbegriffe und Figuren (hart, Kreis, Gerade, Abstand) |
| 74 | Zweireihige Determinanten | – | 7 | – | 46 Kongruenzabbildungen (empfohlen, Verschiebung und Gegenvektor aus den Kongruenzabbildungen (ersetzt 48)); 50 Umfang und Flächeninhalt (empfohlen, Determinanten berechnen Flächeninhalte von Parallelogramm und Dreieck) |
| 75 | Betragsfunktion | – | – | 5 | 32 Zuordnung und Funktion (empfohlen, Funktionsbegriff); 16 Ganze Zahlen (empfohlen, Betrag einer ganzen Zahl) |
| 76 | Reihen | – | – | 5 | 28 Terme aufstellen und deuten (empfohlen, Term für das n-te Glied (Folgen stehen jetzt in diesem Flug, ersetzt 41)) |
| 77 | Umkehrfunktionen | – | 10 | 5 | **aufgelöst** (Entwurf ohne freigegebene Einheit) – keine Verbindungen |
| 78 | Parameter und Funktionenscharen | – | 8 | – | **aufgelöst** (Entwurf ohne freigegebene Einheit) – keine Verbindungen |
| 79 | Standardabweichung | – | – | 5 | 58 Mittelwert und Häufigkeiten (hart, vorhanden); 68 Elementare Wurzeln (empfohlen, vorhanden) |
| 80 | Normalverteilung | – | – | 5 | 79 Standardabweichung (hart, vorhanden) |
| 81 | Stichproben und Aussagekraft | – | 7 | 2 | 57 Daten erfassen und darstellen (empfohlen, Daten erheben und darstellen); 58 Mittelwert und Häufigkeiten (empfohlen, Kenngrößen zum Vergleich von Stichproben) |
| 82 | Bedingte Wahrscheinlichkeit | – | – | 5 | **aufgelöst** (Entwurf ohne freigegebene Einheit) – keine Verbindungen |
| 83 | Mengen und Venn-Diagramme | – | – | 3 | **aufgelöst** (Entwurf ohne freigegebene Einheit) – keine Verbindungen; zusätzlich eigenständig gekennzeichnet |
| 84 | Aussagenlogik | – | – | 4 | **eigenständig** – Entdecker-Insel; Aussagen und Wahrheitswerte werden hier eingeführt |
| 91 | Schrägbilder und Raumdarstellung | 10 | 8 | 4 | 52 Körper darstellen (hart, vorhanden) |
| 92 | Pyramide, Kegel, Kugel | 10 | 9 | 3 | 51 Kreisberechnungen (hart, vorhanden); 54 Satz des Pythagoras (hart, vorhanden); 101 Prismen und Zylinder (empfohlen, Pyramide und Kegel im Vergleich zu Prisma und Zylinder) |
| 93 | Indirekte Proportionalität | 8 | 7 | 4 | 26 Direkte Proportionalität und Dreisatz (hart, vorhanden) |
| 94 | Vermehrter und verminderter Grundwert | 7 | 7 | 3 | 24 Prozent- und Zinsrechnung (hart, vorhanden) |
| 95 | Median, Quartile, Boxplot | 7 | 7 | 4 | 58 Mittelwert und Häufigkeiten (hart, vorhanden) |
| 96 | Rationale Exponenten und n-te Wurzel | 9 | 10 | 5 | 30 Potenzen und negative Exponenten (hart, vorhanden; Begründung neu: Potenzbegriff und negative Exponenten); 68 Elementare Wurzeln (hart, vorhanden); 103 Potenzgesetze mit ganzzahligen Exponenten (empfohlen, Potenzgesetze werden auf rationale Exponenten erweitert) |
| 97 | Quadratische Terme und Extremwerte | – | 8 | – | 29 Terme umformen (hart, vorhanden) |
| 98 | Winkelsätze | 7 | 7 | 2 | 43 Mit Winkeln rechnen (empfohlen, Winkel messen, Scheitel- und Nebenwinkel) |
| 99 | Flächen von Parallelogramm, Dreieck und Trapez | 6 | 6 | – | 50 Umfang und Flächeninhalt (empfohlen, Flächeninhalt von Rechteck und Quadrat; Zerlegen) |
| 100 | Volumen | 6 | 6 | – | 50 Umfang und Flächeninhalt (empfohlen, Grundfläche des Quaders); 25 Größen und Einheiten (empfohlen, Einheiten umrechnen) |
| 101 | Prismen und Zylinder | 8 | 9 | – | 99 Flächen von Parallelogramm, Dreieck und Trapez (empfohlen, Grundflächen Dreieck, Trapez, Parallelogramm); 100 Volumen (empfohlen, Volumenbegriff und Volumeneinheiten); 51 Kreisberechnungen (empfohlen, Kreisfläche und -umfang für den Zylinder) |
| 102 | Potenzgesetze | 7 | 7 | 3 | 30 Potenzen und negative Exponenten (hart, Potenzbegriff (Basis, Exponent, Hoch 0)); 28 Terme aufstellen und deuten (hart, Terme mit Variablen) |
| 103 | Potenzgesetze mit ganzzahligen Exponenten | 8 | 7 | 4 | 102 Potenzgesetze (hart, Potenzgesetze mit natürlichen Exponenten); 30 Potenzen und negative Exponenten (empfohlen, negative Exponenten als Kehrbruch) |
