# Prüfung der geteilten Potenzgesetz-Flüge (Siebenundzwanzigste Runde)

Prüf-Chat `pruefung-potenz`, 20.11.2026. Stand `lernen-app` 1cc6edc (darin `potenz-teilen` bis cd8926a).

Ich habe nur geprüft: keine Inhalte geändert, nichts in die Datenbank, kein App-Code, keine Kinderdaten.

## Ergebnis in Kürze

- **Rechenfehler:** keiner.
  - Geprüft habe ich 191 Aufgaben in Flug A, 175 in Flug B und alle 32 in Gym 6 „Fehler finden“, je mit Lösung, falschen Antworten, Lösungsweg und Tipp.
  - Keine Lösung ist falsch, und keine falsche Antwort ist versehentlich richtig.
- **Trennung:** fast eingehalten, mit zwei Lücken in Tipps (Muss 1 und 2). Außerdem zwei Aufgaben in Flug A, die nach der eigenen Regel des Inhalts-Chats nach Flug B gehören (Sollte 2).
- **Lehrplan:** Flug B passt zu M8 4. Die Pflichtkarten bleiben bei „einfachen Fällen“, Stufe 3 und Knobel gehen darüber hinaus, wie vorgesehen. Die Erklärungen von Flug B sind fachlich richtig und für Klasse 8 verständlich.
- **Stufe und Typ:** In Flug B stimmig. In Flug A haben die 23 umgezogenen Aufgaben als Stufe 3 „fehler“ teils den falschen Gedanken (Sollte 4). Die ersetzten Ablenker passen in 6 Aufgaben nicht zur Rechnung (Sollte 3).
- **Themenliste und kann-Texte:** Formal richtig, Reihenfolgen lückenlos (Selbstprüfung OK, `inhalt_pruefen.py --alle` 118 × OK). Die Einordnung in IB und Realschule ist teils fraglich (Sollte 5, Kann).
- **`terme.umformen`:**
  - Genau die vier Karten fehlen.
  - Die übrigen 8 Karten und 273 Aufgaben sind gleich wie vorher (per Skript gegen den Stand vor der Teilung verglichen).
  - Ziel, Merke, Abschnitte, Teilfähigkeiten und Bewertung sind passend angepasst.

## So geprüft

1. **Nachrechnen, unabhängig vom Generator**
   - Skript `nachrechnen.py` (in diesem Ordner): übersetzt die Potenzschreibweise aus dem Fragetext selbst. Es setzt bei Variablen zwei verschiedene Zahlenbelegungen ein und vergleicht exakt mit Brüchen.
   - Damit geprüft: 144 Aufgaben der Formen „… = bᵏ. Wie groß ist k?“ und „Berechne …“.
     - Flug A: 99
     - Flug B: 45. Zwei Meldungen des Skripts waren Rundungsfehler meines Skripts (Gleitkomma); von Hand nachgerechnet sind beide richtig.
   - Bei diesen 144 habe ich zusätzlich per Skript geprüft, dass der Lösungsweg das Ergebnis nennt; die Tipps nur per Suchmuster (Schritt 2), nicht einzeln gelesen.
   - **Von Hand:** die übrigen 254 Aufgaben, je mit allen Antworten, Lösungsweg und Tipp. Das sind 92 in Flug A, 130 in Flug B und 32 in Gym 6 „Fehler finden“.
2. **Trennung:** per Suchmuster über Text, Antworten, Lösung, Lösungsweg, Tipp und Erklärungen (hochgestelltes Minus, „negativ“, Kehrbruch, Bruch als Ergebnis, Gesetzesformen wie 2³⁻³), jeder Treffer von Hand bewertet.
3. **Stufe und Typ:** gegen `inhalte/README.md` („Stufe folgt aus dem Typ“), dazu gleiche Fragevorlagen mit verschiedenem Typ.
4. **`terme.umformen`:** Vergleich mit dem Stand vor dem Merge von `potenz-teilen`.
5. **Ausgabe:** `ausgeben.py` gibt die Aufgaben kompakt aus.

## Muss

1. **Gym 6 setzt ein Potenzgesetz mit negativen Exponenten voraus.**
   - Fundstelle: `terme.potenzgesetze`, Karte `negativer_exponent`, Übung „Wie viel Mal so groß ist 2² wie 2⁻²?“ (Aufgabe 35).
   - Der Tipp lautet: „Teile die beiden Potenzen. Exponenten subtrahieren: n − (−n).“ Das ist genau der M8-4-Stoff von Flug B.
   - Der Lösungsweg ist schon ohne Gesetz (4 : 1/4 = 16), nur der Tipp ist stehen geblieben.
   - Vorschlag: „Rechne beide Potenzen aus und teile.“
2. **Flug A nennt negative Exponenten.**
   - Fundstelle: `terme.potenzgesetze_natuerlich`, Karte `mal_gleiche_basis`, Übung „a⁵ · a¹ = aᵏ. Wie groß ist k?“ (Aufgabe 11).
   - Der Tipp lautet: „Auch negative Exponenten werden addiert. Achte auf die Vorzeichen.“ Er passt zur früheren Aufgabe mit negativem Exponenten, nicht zu dieser.
   - Vorschlag: „a hat den Exponenten 1.“

## Sollte

1. **Gym 6, Tipps zu Hoch 0 benutzen das Quotientengesetz.**
   - Fundstelle: `terme.potenzgesetze`, Karte `negativer_exponent`, Übungen „Was ergibt a⁰?“ (31) und „Was ergibt 12⁰?“ (37).
   - Tipp: „Teile z. B. 2³ : 2³ – das ist 1 und auch 2³⁻³ = 2⁰.“ Der Teil „2³⁻³ = 2⁰“ ist das Gesetz aᵐ : aⁿ = aᵐ⁻ⁿ (Klasse 7).
   - Ohne Gesetz geht es über das Muster der Lernkarte, zum Beispiel: „Im Muster 2², 2¹, 2⁰ wird jedes Mal durch 2 geteilt.“
2. **Flug A: zwei Aufgaben mit kleinerem erstem Exponenten.** Der Inhalts-Chat hat solche Aufgaben in seiner Abweichung 1 als M8-4-Stoff nach Flug B verlegt. Diese beiden sind geblieben, nur Lösungsweg und Tipp wurden neu geschrieben.
   - `geteilt_gleiche_basis`, Übung „2¹⁰ : 2ⁿ = 1/4. Wie groß ist n?“ (131): Ergebnis 2¹⁰⁻¹² = 2⁻².
   - `geteilt_gleiche_basis`, Übung „Berechne 10⁴ : 10⁴ : 10⁴ · 10⁸.“ (135): Zwischenergebnis 1/10 000 = 10⁻⁴.
   - Beide sind richtig gerechnet und kommen ohne die Schreibweise aus. Folgerichtiger wäre: nach Flug B oder durch Aufgaben ersetzen, bei denen der erste Exponent nie kleiner ist.
3. **Flug A: ersetzte Ablenker passen nicht zur Rechnung.** Die README verlangt falsche Antworten aus typischen Fehlern; diese hier sind zu leicht auszuschließen. Alle in `mal_gleiche_basis`, `gleicher_exponent` und `geteilt_gleiche_basis`:
   - „Ein Kind rechnet: 3⁴ · 3⁴ = 9⁸“ (14): „Exponenten subtrahieren, nicht teilen: 3¹²“ – beim Malnehmen, und 3¹² passt zu keiner der beiden Regeln.
   - „… 4⁴ · 4² = 4⁸“ (16) und „… 5⁴ · 5⁴ = 5¹⁶“ (18): „Gleicher Exponent: Basen malnehmen, der Exponent bleibt: 10⁴“ – Basis 10 kommt in der Aufgabe nicht vor.
   - „… 2² · 5² = 10⁴“ (68): „Exponenten subtrahieren, nicht teilen: 5⁴“.
   - „… 2⁴ · 5⁴ = 10⁸“ (88): „Exponenten subtrahieren, nicht teilen: 5⁶“.
   - „… 5⁶ : 5² = 5³“ (136): „Die Exponenten werden addiert, nicht malgenommen: 5⁵“ – beim Teilen.
4. **Flug A: Stufe 3 „fehler“ passt bei mehreren der 23 umgezogenen Aufgaben nicht zum Gedanken.** Die README sagt: `fehler` = „Fehler in einer Rechnung finden und deuten“. Laut Auftrag sollten alle Stufe 3 „fehler“ werden; der Haupt-Chat sollte entscheiden.
   - **Ohne Fehler:** Sechs „Stimmt die Rechnung?“ zeigen eine richtige Rechnung, es gibt keinen Fehler zu deuten. Das ist `erkennen`, Stufe 1:
     - `mal_gleiche_basis` 2, 4, 6 („5² · 5² = 5⁴“, „4⁴ · 4² = 4⁶“, „2⁴ · 2³ = 2⁷“)
     - `geteilt_gleiche_basis` 112, 116, 122 („4⁵ : 4² = 4³“, „4⁷ : 4⁴ = 4³“, „5⁵ : 5² = 5³“)
   - **Anderer Typ:** Bei vier Aufgaben ist der Gedanke eigentlich ein anderer:
     - `mal_gleiche_basis` 26 („Für welche Zahlen a stimmt sie trotzdem?“) = `parameter`
     - `mal_gleiche_basis` 31 („… Was wäre der richtige Exponent gewesen?“) = `rueckwaerts`
     - `mal_gleiche_basis` 43 („2⁵ + 2⁵ … Richtig ist 2ᵏ“, früher Knobel) liegt nah an der Knobel-Aufgabe 44 („2¹⁰ + 2¹⁰ = 2ᵏ“)
     - `anwenden` 178 („Welche Rechnung ist richtig?“) = `begruenden`
   - **Folge:** `mal_gleiche_basis` hat auf Stufe 3 jetzt 15 von 22 Übungen vom Typ „fehler“, darunter die leichtesten der Karte.
5. **IB-Reihenfolge widerspricht dem Inhalt** (die IB-Nummern sind laut Bericht eine Annahme).
   - `terme.umformen` steht in MYP 3, Flug A in MYP 4. Die Übung „Welches Vorzeichen hat (−a) · (−a)² · (−a)³ …?“ in `terme.umformen/produkte` (Aufgabe 63) rechnet mit a · a² · a³ = a⁶, also mit dem Gesetz aus Flug A.
   - Flug A sollte in IB vor `terme.umformen` stehen (MYP 3), wie im Gymnasium.
6. **Flug A: zwei Übungen ohne Typ, und gleich gebaute Aufgaben mit verschiedenem Typ.**
   - Ohne Typ: `gleicher_exponent`, „Berechne geschickt: 2² · 50²“ (75) und „… 2³ · 5³“ (76). Beide stammen aus `terme.umformen`.
   - Verschiedener Typ: In `mal_gleiche_basis` ist „27 · 3⁵ = 3ᵏ“ (30) Stufe 3 `transfer`. In `anwenden` sind die gleich gebauten „27 · 3² = 3ᵉ“ (154) und „27 · 3⁴ = 3ᵉ“ (156) Stufe 1 `direkt`.
   - Das ist nicht neu aus dieser Runde, fällt aber jetzt in den neuen Flug.

## Kann

1. **Flug B in Realschule 7 und MYP 4 vor den Bruchtermen** (RS 8; MYP Platz 8). Die Karte `terme_vereinfachen` heißt „… auch als Bruch“ und schreibt c/xⁿ. Der Inhalts-Chat begründet in `offen`, dass nur einzelne Potenzen als Bruch geschrieben werden. Das ist vertretbar. Das Wort „Bruchterm“ in Karte und Aufgaben setzt in RS/IB aber einen Begriff voraus, der dort erst später kommt; dort besser „Bruch“.
2. **Flug A, Karte „Gleiche Basis: teilen“:** kein Hinweis, dass hier immer der erste Exponent größer ist. Ein Satz wie „In diesem Flug ist der erste Exponent immer größer; den anderen Fall lernst du in Klasse 8“ würde die Trennung auch für das Kind sichtbar machen.
3. **Gym 6, `offen` der Themendatei veraltet:** nennt „rationale Exponenten“ im `umfang` (steht dort nicht mehr) und als Beispiel „2³ · 2⁴ = 2ᵏ“, ein Potenzgesetz.
4. **Themenliste `terme.umformen`, `lehrplan_rs`:** „Terme vereinfachen, auch mit Potenzgesetzen …“. Nach der Teilung missverständlich; der Inhalts-Chat hat das selbst als offen gemeldet.
5. **kann-Text Gym 6 (`kurz`):** „Mal-Aufgaben mit immer gleichen Zahlen kurz schreiben …“ verschweigt Hoch 0 und negative Exponenten, die jetzt den halben Flug ausmachen.
6. **Flug A, M7 1.2 „Potenzen von Potenzen“** hat keine Karte; das hat der Inhalts-Chat offen gemeldet, Sebastian entscheidet. Fachlich wäre es eine Pflichtkarte in Flug A: Der Lehrplan nennt es in M7.
7. **Flug B, Einstieg von `terme_vereinfachen`:** „Im Algenmodell rechnest du oft mit Variablen“ wirkt aufgesetzt. Ein direkter Einstieg („Terme wie 6x³ · x⁻⁵ …“) genügt.
8. **Flug B, Knobel `fehler_ganz` „2⁻¹ + 2⁻² + 2⁻³ + …“ (163):** Die Summe 63/64 ist richtig. Die Aussage „Größer als 1 wird die Summe nie“ ist ein Grenzwertgedanke, als Knobel aber in Ordnung.

## Was stimmt (geprüft, ohne Befund)

- **Flug B, alle 175 Aufgaben:** Lösung, falsche Antworten, Lösungsweg und Tipp sind richtig.
  - Stufe und Typ passen überall zur README.
  - Die 29 übernommenen Aufgaben sind sinnvoll umgestuft: Zweierprodukte sind in Flug B die Grundform, also Stufe 1 `direkt`; Dreierprodukte und Dezimalergebnisse Stufe 2 `mehrschritt`.
  - Nichts setzt Stoff voraus, der in Gym 8 nach `terme.bruchterme` kommt. Es gibt nur lineare Gleichungen für Exponenten (Kl. 7), einfache Formeln einsetzen (H = 100 · r⁻², A(t) = 3 · 2ᵗ) und Flächen und Volumen.
- **Erklärungen Flug B (5 Karten):** fachlich richtig; das Algen-Beispiel trägt durch. „Plausibel machen“ geschieht über Muster und Zahlenprobe, wie M8 4 es verlangt.
  - Die typischen Fehler treffen genau:
    - 2³ · 2⁻² = 2⁻⁶ (Exponenten malgenommen)
    - 3 − 5 statt 3 − (−5)
    - (2³)² = 2⁵
    - 6x⁻² = 1/(6x²)
    - (−3) · (−2) = 6
  - Die Beispielrechnungen in Schritten, Bildern und Probe habe ich nachgerechnet.
- **Gym 6 „Fehler finden“, alle 32:** richtig. Kein Potenzgesetz vorausgesetzt (Text, Antworten, Lösungsweg, Tipp). Die neu gebauten 14 Aufgaben sind sinnvoll und richtig.
- **Flug A, 191 Aufgaben:** Lösungen richtig.
  - Kein negativer Exponent in Text, Antworten oder Ergebnis. Ausnahmen sind der Tipp in Muss 2 und die Zwischenergebnisse in Sollte 2.
  - Die 29 Ersatzaufgaben sind gleichwertig (Karte, Pool, Stufe, Typ).
- **Themenliste:**
  - Beide neuen Einträge sind vollständig (alle Felder wie die anderen Themen).
  - Die Reihenfolgen sind lückenlos und eindeutig: Gym 7 (Flug A = 2, `umformen` = 3), Gym 8 (Flug B = 8 hinter `bruchterme`, vor `gleichungen.bruch`), RS 7 (Gym-6-Flug 1, A 2, B 3), MYP 4 (A 1, B 2).
  - Titel und `umfang` treffen den Inhalt; `lehrplan_gym` von Flug A und B entspricht M7 1.2 bzw. M8 4.
- **kann-Texte:** Die zwei neuen Dateien treffen den Inhalt, und die Längen sind eingehalten (geprüft mit `_potenz_teilen_liste.py`). Die vier Texte von Flug A sind unverändert aus `terme.umformen` übernommen, wie für den Lernstand nötig.

## Nicht geprüft

- **Lehrplantexte im Original:** nicht selbst gelesen, nur die Zitate aus dem Bericht und aus `lehrplan-lb.md`.
- **Anzeige in der App:** Tabellen als Kartenbild, Lücken „c = □; n = □“ und Bruch-Lücken.
- **Tipps der 144 per Skript geprüften Aufgaben:** nur per Suchmuster durchsucht, nicht einzeln gelesen.
- **Die übrigen Karten von Gym 6** (`potenz_begriff`, `negativer_exponent`, 77 Aufgaben): nur auf Potenzgesetze durchsucht (Befunde in Muss 1 und Sollte 1), nicht nachgerechnet.
- **Die 8 verbliebenen Karten von `terme.umformen`:** nur auf Gleichheit mit dem Stand vorher geprüft, nicht nachgerechnet. Aufgefallen ist dabei nur die Aufgabe in Sollte 5.
- **Alte Aufgaben in der Datenbank:** Laut `offen` liegen Aufgaben von `terme.umformen` aus der Zeit vor dem Bausatz nur dort, nicht im Repo. Ob die vier Lernziele dort weitere Aufgaben mit negativen Exponenten haben, die beim Umhängen nach Flug A mitkämen, habe ich nicht geprüft; ich habe keine Datenbankabfrage gemacht. Das sollte der Haupt-Chat vor dem Umhängen prüfen.
- **Expeditionen:** Verweise auf die betroffenen Lernkarten habe ich nicht selbst nachgesehen.
