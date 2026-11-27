# Postfach potenz-teilen (Sechsundzwanzigste Runde: Potenzgesetze in zwei eigene Flüge teilen)

Neueste Meldung oben. Zeiten: Sechsundzwanzigste Runde Ortszeit Adelaide (UTC+10:30), ab der Achtundzwanzigsten Runde Europe/Berlin.

## 2026-11-21 01:09 – FERTIG: Potenz Runde 29

Neunundzwanzigste Runde, Zweig `potenz-teilen` (auf den Stand von `lernen-app` 4970b4b gebracht). Grundlage sind Entscheidungen des Nutzers vom 21.11., Punkt 2, und die Nachprüfung (`inhalte/pruefung/potenz/nachpruefung.md`), Kann 2, 4, 6 und 7.

Nichts in die Datenbank, kein App-Code, kein Merge nach `main`. `terme.potenzgesetze` (Gym 6), `terme.umformen`, Themenliste und kann-Texte sind unverändert.

### Alt → neu

| Flug, Karte | Aufgabe / Feld | alt | neu |
|---|---|---|---|
| A, mal_gleiche_basis | Ein Kind rechnet: 3⁴ · 3⁴ = 9⁸. Was ist falsch? | Übung, Stufe 1, erkennen | Übung, Stufe 1, ohne Typ (überzählig) |
| A, mal_gleiche_basis | Ein Kind rechnet: 4⁴ · 4² = 4⁸. Was ist falsch? | Übung, Stufe 1, erkennen | ohne Typ |
| A, mal_gleiche_basis | Ein Kind rechnet: 5⁴ · 5⁴ = 5¹⁶. Was ist falsch? | Übung, Stufe 1, erkennen | ohne Typ |
| A, mal_gleiche_basis | Ein Kind rechnet: 4³ · 4² = 16⁵. Welcher Satz beschreibt den Fehler richtig? | Übung, Stufe 1, erkennen | ohne Typ |
| A, mal_gleiche_basis | Ein Kind rechnet: 4³ · 4³ = 4⁹. Welcher Satz beschreibt den Fehler richtig? | Übung, Stufe 1, erkennen | ohne Typ |
| A, mal_gleiche_basis | Ein Kind rechnet: 4⁴ · 4² = 16⁶. Welcher Satz beschreibt den Fehler richtig? | Übung, Stufe 1, erkennen | ohne Typ |
| A, gleicher_exponent | Ein Kind rechnet: 2² · 5² = 10⁴. Was ist falsch? | Übung, Stufe 1, erkennen | ohne Typ |
| A, gleicher_exponent | Ein Kind rechnet: 2³ · 5³ = 10⁶. Was ist falsch? – falsche Antwort (Kann 2) | Die Exponenten werden addiert, nicht malgenommen: 2⁵. | Die Basen werden addiert: 7³. |
| A, gleicher_exponent | Ein Kind rechnet: 2⁴ · 5⁴ = 10⁸. Was ist falsch? – falsche Antwort (Kann 2) | Die Exponenten werden addiert, nicht malgenommen: 5⁶. | Die Basen werden addiert: 7⁴. |
| A, geteilt_gleiche_basis | 2¹⁰ : 2ⁿ = 16. Wie groß ist n? (Kann 4) | Übung, Stufe 3, rueckwaerts | Übung, Stufe 2, umkehr |
| A, potenz_von_potenz | Lernkarte, Wort „potenziert“ (Kann 6) | mit einem Exponenten versehen, also mehrmals mit sich selbst malgenommen | hoch eine Zahl genommen |
| B, exponent_und_potenz | Lernkarte, `einstieg` (Kann 7) | … Seine Fläche ist (2⁻¹)². Hier wird eine Potenz noch einmal potenziert: eine ⟦Potenz einer Potenz⟧. | … Seine Fläche ist (2⁻¹)². Die ⟦Potenz einer Potenz⟧ kennst du aus Klasse 7. Jetzt rechnest du sie auch mit negativen Exponenten. |
| B, exponent_und_potenz | Lernkarte, Wort „Potenz einer Potenz“ (Kann 7) | eine Potenz in Klammern mit noch einem Exponenten, z. B. (2³)² | kennst du aus Klasse 7: eine Potenz in Klammern mit noch einem Exponenten, z. B. (2³)² |

Bei allen geänderten Aufgaben bleiben der Fragetext und die richtige Antwort gleich. Die neuen falschen Antworten sind wirklich falsch (2³ · 5³ = 1 000 ≠ 7³ = 343; 2⁴ · 5⁴ = 10 000 ≠ 7⁴ = 2 401).

### Mindestmengen und Typ-Mischung danach (Flug A, Übungen)

| Karte | Stufe 1 | Stufe 2 | Stufe 3 |
|---|---|---|---|
| mal_gleiche_basis | direkt 8, erkennen 5 (+ 6 ohne Typ) | mehrschritt 10, umkehr 2, darstellung 1, einkleidung 1 | fehler 3, parameter 2, rueckwaerts 2, verknuepfen 1, begruenden 1, pruefung 1, transfer 1 |
| gleicher_exponent | direkt 4, erkennen 4 (+ 3 ohne Typ) | mehrschritt 8, umkehr 3, einkleidung 1 | fehler 3, transfer 2, begruenden 1, rueckwaerts 1, parameter 1, verknuepfen 1, pruefung 1 |
| potenz_von_potenz | direkt 4, erkennen 2 | mehrschritt 3, umkehr 2, einkleidung 2, darstellung 1 | begruenden 2, fehler 2, parameter 1, rueckwaerts 1, verknuepfen 1, transfer 1, pruefung 1 |
| geteilt_gleiche_basis | direkt 6, erkennen 4 | mehrschritt 14, umkehr 2, einkleidung 1 | fehler 3, transfer 2, verknuepfen 1, begruenden 1, parameter 1, pruefung 1 |
| anwenden | direkt 6, erkennen 1 | mehrschritt 9, darstellung 3, einkleidung 2 | transfer 2, begruenden 2, verknuepfen 1, fehler 1, rueckwaerts 1, parameter 1, pruefung 1 |

- Die Mindestmengen sind überall erfüllt, mit Typen nur gezählt: Stufe 1, 2 und 3 mindestens 4, 6 und 8 Aufgaben mit 2, 3 und 4 Typen. Auf Stufe 3 steht höchstens 3 je Typ.
- In `gleicher_exponent` sind „ohne Typ“ die zwei Spiegelbilder aus Runde 28 und die eine Aufgabe von heute.
- Flug A hat jetzt 167 Aufgaben mit Typ (vorher 174). Flug B ist unverändert bis auf die Karte.

### Prüfung
- **Prüfskript:** `python3 -I tools/inhalt_pruefen.py --alle` meldet **118 × OK**, Rückgabewert 0. Flug A und Flug B haben keine Hinweise zu den Karten, „gleich gebaut hintereinander“ ist 0.
- **Generatoren:** Ein zweiter Lauf ergibt Byte für Byte dieselben Dateien. Der Dateivergleich gegen `lernen-app` zeigt genau die Änderungen der Tabelle oben.
- **Hinweis zu Kann 7:** „kennst du aus Klasse 7“ stimmt für Gymnasium und Realschule. In IB steht Flug A in MYP 3, Flug B in MYP 4. Dort wäre „aus dem Flug ‚Potenzgesetze‘“ genauer. Ich habe trotzdem wie beauftragt „Klasse 7“ geschrieben.

## 2026-11-20 13:58 – FERTIG: Potenz nachgebessert

Achtundzwanzigste Runde (Zweig `potenz-teilen`, vorher auf den Stand von `lernen-app` 72abf97 gebracht). Grundlage: `inhalte/pruefung/potenz/bericht.md`, Auftrag in `AUFTRAEGE.md`, Ja des Nutzers zu Kann 6 (`antworten.md`, 20.11. 14:50). Nichts in die Datenbank, kein App-Code, kein Merge nach `main`.

### Kurz
- **Muss 1 und 2:** erledigt (zwei Tipps).
- **Sollte 1–6:** alle erledigt.
- **Kann 1–5 und 7:** erledigt. Kann 8 bleibt wie verlangt.
- **Kann 6:** neue Pflichtkarte `potenz_von_potenz` in Flug A, mit 35 Aufgaben vollständig nach Bausatz. Die vier alten Schlüssel sind unverändert.
- **Flüge jetzt:** Flug A 226 Aufgaben in 5 Karten, Flug B 177 Aufgaben, Gym 6 109 Aufgaben. `terme.umformen` ist unverändert.
- **Prüfskript:** `python3 -I tools/inhalt_pruefen.py --alle` meldet **118 × OK** mit Rückgabewert 0. Bei den vier Potenz-Flügen gibt es keine Hinweise zu den Karten, „gleich gebaut hintereinander“ ist überall 0. Die Generatoren liefern beim zweiten Lauf Byte für Byte dasselbe.
- **Nachgerechnet:**
  - 126 Aufgaben von Flug A unabhängig per Skript (Terme aus dem Fragetext, zwei Belegungen), dabei 0 Fehler.
  - Die übrigen neuen und geänderten Aufgaben von Hand, nämlich die neue Karte und die Ersatzaufgaben.
  - Bei jeder geänderten Antwortliste habe ich geprüft: Die richtige Antwort bleibt richtig, und die neuen falschen Antworten sind wirklich falsch.

### Entscheidungen, die ich getroffen habe (bitte ansehen)
1. **Sollte 4, Folge:**
   - Nach den verlangten Umstufungen hatte `mal_gleiche_basis` auf Stufe 3 noch 10 von 19 Übungen „fehler“, war also weiter davon beherrscht.
   - Ich habe deshalb je Karte höchstens 3 „fehler“ auf Stufe 3 gelassen. Das ist die Regel der Zwanzigsten Runde, Grund des Nutzers vom 20.11.: keine leichten Aufgaben auf Stufe 3.
   - Die Auswahl-Aufgaben, bei denen das Kind nur benennt, welcher Rechenweg falsch war („Was ist falsch?“, „Welcher Satz beschreibt …“, „Stimmt die Rechnung? 5² · 5³ = 5⁶“), sind jetzt Stufe 1 „erkennen“: 7 in `mal_gleiche_basis`, 1 in `gleicher_exponent`.
   - Auf Stufe 3 bleiben die Aufgaben, bei denen das Kind den richtigen Wert selbst bestimmt, und eine Auswahl-Aufgabe je Karte.
   - Wenn der Nutzer das anders will, lässt es sich in `NB_A` mit einer Zeile je Aufgabe zurückdrehen.
2. **Sollte 4, Aufgabe 43** („2⁵ + 2⁵ = 2¹⁰“): ersetzt statt in den Knobel-Pool gelegt, weil sie zu nah an Knobel 44 liegt. Neu ist eine Aufgabe vom Typ „fehler“: „Ein Kind rechnet 2³ · 2⁴ · 2 = 2¹². Richtig ist 2ᵏ …“.
3. **Sollte 6, Aufgaben 75 und 76:** Mit dem Typ „direkt“ hätten je 3 gleich gebaute Aufgaben auf Stufe 1 gestanden („2² · 50²“ neben „25² · 4²“ und „4² · 25²“). Das verbietet das Prüfskript. Deshalb haben die beiden Spiegelbild-Aufgaben „4² · 25²“ und „2³ · 50³“ ihren Typ verloren: Sie sind überzählig und werden beim Einspielen gesperrt, nicht gelöscht. Die Zahl der aktiven Übungen bleibt gleich.
4. **Sollte 6, Aufgaben 30, 154 und 156:** In `anwenden` ist „27 · 3ᵉ“ die Grundform der Karte und bleibt Stufe 1 „direkt“. In `mal_gleiche_basis` kommt das Umschreiben einer Zahl als Potenz noch dazu. Dort ist „27 · 3⁵“ jetzt Stufe 2 „darstellung“ (vorher Stufe 3 „transfer“). Die Spanne ist damit eine Stufe, und beide Karten folgen ihrem eigenen Beispiel.
5. **Sollte 5 (IB):** Flug A steht jetzt in MYP 3. Die Reihenfolge dort ist: Gym-6-Flug `terme.potenzgesetze` 1, Flug A 2, `terme.umformen` 3, alles Weitere +1.
   - Den Gym-6-Flug habe ich vorgezogen (vorher 2 hinter `terme.umformen`), weil Flug A seinen Potenzbegriff und Hoch 0 voraussetzt.
   - In MYP 4 rücken alle um 1 nach vorn, Flug B ist jetzt 1.
   - Alles bleibt als Annahme gekennzeichnet.
6. **Sollte 2:** Die zwei Aufgaben stehen jetzt in Flug B, Karte `gleiche_basis_ganz`. „Berechne 10⁴ : 10⁴ : 10⁴ · 10⁸.“ ist dort Stufe 2 „mehrschritt“ (vorher Stufe 3 „transfer“), weil das in Flug B die Standardrechnung ist. „2¹⁰ : 2ⁿ = 1/4“ bleibt Stufe 3 „rueckwaerts“. Der Ersatz in Flug A behält Pool, Stufe und Typ.
7. **Kann 1:** In den Auswahl-Aufgaben steht jetzt „Bruch“ statt „Bruchterm“. Das ändert den Fragetext, und das Werkzeug mischt die Antworten nach dem Text. Deshalb ist ihre Reihenfolge neu gemischt; die Antworten selbst und die Lösung sind gleich. Flug B ist noch nicht freigegeben.

### Zählung danach

**terme.potenzgesetze_natuerlich** – 226 Aufgaben

| Lernkarte | P/V | Übung S1 | S2 | S3 | davon „fehler“ in S3 | ohne Typ | Knobel | Test | Korr. | Sich. |
|---|---|---|---|---|---|---|---|---|---|---|
| mal_gleiche_basis | P | 19 | 14 | 11 | 3 | 0 | 2 | 1 | 3 | 6 |
| gleicher_exponent | P | 11 | 12 | 10 | 3 | 2 | 2 | 1 | 3 | 6 |
| potenz_von_potenz | P | 6 | 8 | 9 | 2 | 0 | 2 | 1 | 3 | 6 |
| geteilt_gleiche_basis | V | 10 | 16 | 10 | 3 | 0 | 2 | 1 | 3 | 6 |
| anwenden | V | 7 | 14 | 9 | 1 | 0 | 2 | 1 | 3 | 6 |

**terme.potenzgesetze_ganzzahlig** – 177 Aufgaben

| Lernkarte | P/V | Übung S1 | S2 | S3 | davon „fehler“ in S3 | ohne Typ | Knobel | Test | Korr. | Sich. |
|---|---|---|---|---|---|---|---|---|---|---|
| warum_gilt | P | 5 | 8 | 9 | 2 | 0 | 2 | 1 | 3 | 6 |
| gleiche_basis_ganz | P | 9 | 10 | 9 | 2 | 0 | 2 | 1 | 4 | 10 |
| exponent_und_potenz | P | 6 | 8 | 8 | 2 | 0 | 2 | 1 | 3 | 6 |
| terme_vereinfachen | P | 5 | 7 | 8 | 2 | 0 | 2 | 1 | 3 | 6 |
| fehler_ganz | V | 5 | 6 | 9 | 3 | 0 | 2 | 1 | 3 | 6 |

**terme.potenzgesetze** – 109 Aufgaben

| Lernkarte | P/V | Übung S1 | S2 | S3 | davon „fehler“ in S3 | ohne Typ | Knobel | Test | Korr. | Sich. |
|---|---|---|---|---|---|---|---|---|---|---|
| potenz_begriff | P | 8 | 11 | 8 | 1 | 0 | 2 | 1 | 3 | 6 |
| negativer_exponent | P | 5 | 13 | 8 | 1 | 0 | 2 | 1 | 3 | 6 |
| fehler_finden | V | 4 | 8 | 8 | 3 | 0 | 2 | 1 | 3 | 6 |

### Alt → neu je geänderter Aufgabe
**Gym 6 (`terme.potenzgesetze`)**

| Karte | Aufgabe | was | alt | neu |
|---|---|---|---|---|
| negativer_exponent | Wie viel Mal so groß ist 2² wie 2⁻²? | Tipp | Teile die beiden Potenzen. Exponenten subtrahieren: n − (−n). | Rechne beide Potenzen aus und teile. |
| negativer_exponent | Was ergibt a⁰? | Tipp | Teile z. B. 2³ : 2³ – das ist 1 und auch 2³⁻³ = 2⁰. | Denk an das Muster 2² = 4, 2¹ = 2, 2⁰ = ?: Es wird jedes Mal durch 2 geteilt. |
| negativer_exponent | Was ergibt 12⁰? | Tipp | Teile z. B. 2³ : 2³ – das ist 1 und auch 2³⁻³ = 2⁰. | Denk an das Muster 2² = 4, 2¹ = 2, 2⁰ = ?: Es wird jedes Mal durch 2 geteilt. |

**Flug A (`terme.potenzgesetze_natuerlich`), geänderte Aufgaben**

| Karte | Aufgabe | was | alt | neu |
|---|---|---|---|---|
| mal_gleiche_basis | a⁵ · a¹ = aᵏ. Wie groß ist k? | Tipp | Auch negative Exponenten werden addiert. Achte auf die Vorzeichen. | a¹ ist a mit dem Exponenten 1. Addiere die Exponenten. |
| mal_gleiche_basis | Ein Kind rechnet: 3⁴ · 3⁴ = 9⁸. Was ist falsch? | falsche Antwort | Gleicher Exponent: Basen malnehmen, der Exponent bleibt: 10⁴. | Die Exponenten werden malgenommen: 3¹⁶. |
| mal_gleiche_basis | Ein Kind rechnet: 3⁴ · 3⁴ = 9⁸. Was ist falsch? | falsche Antwort | Exponenten subtrahieren, nicht teilen: 3¹². | Die Exponenten werden subtrahiert: 3⁰. |
| mal_gleiche_basis | Ein Kind rechnet: 4⁴ · 4² = 4⁸. Was ist falsch? | falsche Antwort | Gleicher Exponent: Basen malnehmen, der Exponent bleibt: 10⁴. | Die Exponenten werden subtrahiert: 4². |
| mal_gleiche_basis | Ein Kind rechnet: 5⁴ · 5⁴ = 5¹⁶. Was ist falsch? | falsche Antwort | Gleicher Exponent: Basen malnehmen, der Exponent bleibt: 10⁴. | Die Basen werden addiert: 10⁸. |
| gleicher_exponent | Ein Kind rechnet: 2² · 5² = 10⁴. Was ist falsch? | falsche Antwort | Exponenten subtrahieren, nicht teilen: 5⁴. | Verschiedene Basen darf man nie zusammenfassen. |
| gleicher_exponent | Ein Kind rechnet: 2⁴ · 5⁴ = 10⁸. Was ist falsch? | falsche Antwort | Exponenten subtrahieren, nicht teilen: 5⁶. | Verschiedene Basen darf man nie zusammenfassen. |
| geteilt_gleiche_basis | Ein Kind rechnet: 5⁶ : 5² = 5³. Was ist falsch? | falsche Antwort | Die Exponenten werden addiert, nicht malgenommen: 5⁵. | Die Basen werden geteilt: 1⁴. |
| mal_gleiche_basis | Stimmt die Rechnung? 5² · 5² = 5⁴ | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| mal_gleiche_basis | Stimmt die Rechnung? 4⁴ · 4² = 4⁶ | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| mal_gleiche_basis | Stimmt die Rechnung? 2⁴ · 2³ = 2⁷ | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| geteilt_gleiche_basis | Stimmt die Rechnung? 4⁵ : 4² = 4³ | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| geteilt_gleiche_basis | Stimmt die Rechnung? 4⁷ : 4⁴ = 4³ | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| geteilt_gleiche_basis | Stimmt die Rechnung? 5⁵ : 5² = 5³ | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| mal_gleiche_basis | Die Regel „a² · a³ = a⁶“ ist falsch. Für welche Zahlen a stimmt sie trotzdem? | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 3, parameter |
| mal_gleiche_basis | Ein Kind hat bei aᵏ · a² die Exponenten malgenommen und a¹² erhalten. Was wäre der richtige Exponent gewesen? | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 3, rueckwaerts |
| anwenden | Welche Rechnung ist richtig? | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 3, begruenden |
| mal_gleiche_basis | Ein Kind schreibt 2⁵ + 2⁵ = 2¹⁰. Richtig ist 2ᵏ. Wie groß ist k? | Aufgabe ersetzt | Ein Kind schreibt 2⁵ + 2⁵ = 2¹⁰. Richtig ist 2ᵏ. Wie groß ist k? | Ein Kind rechnet 2³ · 2⁴ · 2 = 2¹². Richtig ist 2ᵏ. Wie groß ist k? |
| mal_gleiche_basis | Stimmt die Rechnung? 5² · 5³ = 5⁶ | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| mal_gleiche_basis | Ein Kind rechnet: 3⁴ · 3⁴ = 9⁸. Was ist falsch? | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| mal_gleiche_basis | Ein Kind rechnet: 4⁴ · 4² = 4⁸. Was ist falsch? | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| mal_gleiche_basis | Ein Kind rechnet: 5⁴ · 5⁴ = 5¹⁶. Was ist falsch? | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| mal_gleiche_basis | Ein Kind rechnet: 4³ · 4² = 16⁵. Welcher Satz beschreibt den Fehler richtig? | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| mal_gleiche_basis | Ein Kind rechnet: 4³ · 4³ = 4⁹. Welcher Satz beschreibt den Fehler richtig? | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| mal_gleiche_basis | Ein Kind rechnet: 4⁴ · 4² = 16⁶. Welcher Satz beschreibt den Fehler richtig? | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| gleicher_exponent | Ein Kind rechnet: 2² · 5² = 10⁴. Was ist falsch? | Stufe/Typ | uebung, Stufe 3, fehler | uebung, Stufe 1, erkennen |
| gleicher_exponent | Berechne geschickt: 2² · 50² | Stufe/Typ | uebung, Stufe 1, ohne Typ | uebung, Stufe 1, direkt |
| gleicher_exponent | Berechne geschickt: 2³ · 5³ | Stufe/Typ | uebung, Stufe 1, ohne Typ | uebung, Stufe 1, direkt |
| gleicher_exponent | Berechne geschickt: 4² · 25² | Stufe/Typ | uebung, Stufe 1, direkt | uebung, Stufe 1, ohne Typ (überzählig) |
| gleicher_exponent | Berechne geschickt: 2³ · 50³ | Stufe/Typ | uebung, Stufe 1, direkt | uebung, Stufe 1, ohne Typ (überzählig) |
| mal_gleiche_basis | 27 · 3⁵ = 3ᵏ. Wie groß ist k? | Stufe/Typ | uebung, Stufe 3, transfer | uebung, Stufe 2, darstellung |
| geteilt_gleiche_basis | – | Lernkarte, regel | Bei ⟦gleicher Basis⟧ subtrahierst du beim Teilen die Exponenten. Die Basis bleibt. | Bei ⟦gleicher Basis⟧ subtrahierst du beim Teilen die Exponenten. Hier ist der erste immer größer; den anderen Fall lernst du später. |

**Flug A → Flug B (Sollte 2), in Flug A an derselben Stelle ersetzt (Pool, Stufe, Typ gleich)**

| Karte | alt (jetzt in Flug B) | neu in Flug A | in Flug B |
|---|---|---|---|
| geteilt_gleiche_basis | 2¹⁰ : 2ⁿ = 1/4. Wie groß ist n? | 2¹⁰ : 2ⁿ = 16. Wie groß ist n? | gleiche_basis_ganz, Übung, Stufe 3 rueckwaerts (vorher Stufe 3 rueckwaerts) |
| geteilt_gleiche_basis | Berechne 10⁴ : 10⁴ : 10⁴ · 10⁸. | Ein Rechner schafft 10⁹ Rechenschritte pro Sekunde. 10³ Programme brauchen je 10⁸ Rechenschritte. Wie lange braucht er für alle? Gib die Zeit als 10ᵏ Sekunden an. Wie groß ist k? | gleiche_basis_ganz, Übung, Stufe 2 mehrschritt (vorher Stufe 3 transfer) |

**Flug A, neue Pflichtkarte `potenz_von_potenz`** (35 Aufgaben)

- uebung, Stufe 1, direkt: (3²)⁴ = 3ᵏ. Wie groß ist k?
- uebung, Stufe 1, direkt: (x³)⁵ = xᵏ. Wie groß ist k?
- uebung, Stufe 1, direkt: (10²)³ = 10ᵏ. Wie groß ist k?
- uebung, Stufe 1, direkt: (a⁴)² = aᵏ. Wie groß ist k?
- uebung, Stufe 1, erkennen: Welche Regel gilt bei (b⁵)²?
- uebung, Stufe 1, erkennen: Welcher Term ist gleich 2³ · 2³ · 2³ · 2³?
- uebung, Stufe 2, mehrschritt: Berechne (2³)² mit dem Potenzgesetz. Gib das Ergebnis als Zahl an.
- uebung, Stufe 2, mehrschritt: (a²)³ · a⁴ = aᵏ. Wie groß ist k?
- uebung, Stufe 2, mehrschritt: (2³)² · 2 = 2ᵏ. Wie groß ist k?
- uebung, Stufe 2, umkehr: (5ᵏ)³ = 5¹². Wie groß ist k?
- uebung, Stufe 2, umkehr: (y²)ᵏ = y¹⁰. Wie groß ist k?
- uebung, Stufe 2, einkleidung: Ein Würfel hat die Kantenlänge 10² cm. Wie groß ist sein Volumen? Gib es als 10ᵏ cm³ an. Wie groß ist k?
- uebung, Stufe 2, einkleidung: Ein quadratisches Feld hat die Seitenlänge 3³ m. Wie groß ist seine Fläche? Gib sie als Zahl an.
- uebung, Stufe 2, darstellung: Ein Würfel hat die Kantenlänge 5² cm. Welcher Term gibt sein Volumen in cm³ an?
- uebung, Stufe 3, begruenden: Stimmt die Aussage? „(2³)² und (2²)³ sind gleich groß.“
- uebung, Stufe 3, begruenden: Warum gilt (a⁴)³ = a¹²? Welche Begründung stimmt?
- uebung, Stufe 3, fehler: Ein Kind rechnet (x⁴)³ = x⁷. Richtig ist xᵏ. Wie groß ist k?
- uebung, Stufe 3, fehler: Ein Kind rechnet (3²)³ = 9⁶. Was ist falsch?
- uebung, Stufe 3, parameter: Für wie viele natürliche Zahlen n von 1 bis 20 ist (2ⁿ)² höchstens 2²⁰?
- uebung, Stufe 3, rueckwaerts: Eine Zahl 2ᵏ wird erst quadriert und das Ergebnis dann hoch 3 genommen. Heraus kommt 2¹⁸. Wie groß ist k?
- uebung, Stufe 3, verknuepfen: Ein Würfel hat 3² cm lange Kanten. Wie viele Würfel mit 1 cm Kantenlänge passen hinein?
- uebung, Stufe 3, transfer: Ein Würfel aus Zuckerstücken hat 2⁴ Stücke an jeder Kante. Aus solchen Würfeln baut man einen großen Würfel mit 2² Würfeln an jeder Kante. Wie viele Zuckerstücke sind es? Gib die Anzahl als 2ᵏ an. Wie groß ist k?
- uebung, Stufe 3, pruefung: a) Vereinfache (x²)⁴ · x³. b) Berechne den Wert für x = 2. Gib den Wert aus b) an.
- bonus, Stufe 3, knobel: Welche Zahl ist größer: (2³)⁴ oder (3²)³? Gib die größere Zahl an.
- bonus, Stufe 3, knobel: Schreibe 9² · 27³ als Dreierpotenz 3ᵏ. Wie groß ist k?
- test, Stufe 2: (7²)³ = 7ᵏ. Wie groß ist k?
- korrektur, Stufe 2: (b³)⁴ = bᵏ. Wie groß ist k?
- korrektur, Stufe 2: (2⁵)² = 2ᵏ. Wie groß ist k?
- korrektur, Stufe 2: Welche Regel gilt bei (y²)⁵?
- sicherung, Stufe 2: (10⁴)² = 10ᵏ. Wie groß ist k?
- sicherung, Stufe 2: (a³)³ = aᵏ. Wie groß ist k?
- sicherung, Stufe 2: (x⁶)² = xᵏ. Wie groß ist k?
- sicherung, Stufe 2: (4²)² = 4ᵏ. Wie groß ist k?
- sicherung, Stufe 2: Berechne (3²)² mit dem Potenzgesetz und gib den Wert an.
- sicherung, Stufe 2: (5²)³ = 5ᵏ. Wie groß ist k?

**Flug B (`terme.potenzgesetze_ganzzahlig`), Kann 1 („Bruch“ statt „Bruchterm“): Fragetext geändert, Lösung und Antworten gleich**

| Karte | alt | neu |
|---|---|---|
| terme_vereinfachen | Welcher Bruchterm ist gleich 4x⁻²? | Welcher Bruch ist gleich 4x⁻²? |


**Flug B (`terme.potenzgesetze_ganzzahlig`), Kann 1 („Bruch“ statt „Bruchterm“): nur der Fragetext geändert; Antworten und Lösung gleich (Reihenfolge der Antworten neu gemischt)**

| Karte | Pool | alt | neu |
|---|---|---|---|
| terme_vereinfachen | uebung | Welcher Bruchterm ist gleich 4x⁻²? | Welcher Bruch ist gleich 4x⁻²? |
| terme_vereinfachen | uebung | Welcher Bruchterm ist gleich 5x⁻³y²? | Welcher Bruch ist gleich 5x⁻³y²? |
| terme_vereinfachen | korrektur | Welcher Bruchterm ist gleich 7y⁻¹? | Welcher Bruch ist gleich 7y⁻¹? |
| terme_vereinfachen | sicherung | Welcher Bruchterm ist gleich 9x⁻⁴? | Welcher Bruch ist gleich 9x⁻⁴? |

Neu in Flug B (aus Flug A, siehe oben): „Berechne 10⁴ : 10⁴ : 10⁴ · 10⁸.“; „2¹⁰ : 2ⁿ = 1/4. Wie groß ist n?“.

Lernkarte `terme_vereinfachen`, Feld `einstieg`: alt "Im Algenmodell rechnest du oft mit Variablen. Terme wie 6x³ · x⁻⁵ fasst du zusammen. Dann schreibst du sie ohne negativen Exponenten als ⟦Bruchterm⟧." → neu "Terme wie 6x³ · x⁻⁵ fasst du mit den Potenzgesetzen zusammen. Dann schreibst du sie ohne negativen Exponenten als ⟦Bruch⟧ mit der Variablen im Nenner."

Lernkarte `terme_vereinfachen`, Feld `woerter`: alt [["Bruchterm", "ein Bruch mit einer Variablen im Nenner, z. B. 6/x²"], ["Koeffizient", "die Zahl vor der Variablen, z. B. die 6 in 6x³"]] → neu [["Bruch", "hier: ein Bruch mit einer Variablen im Nenner, z. B. 6/x²"], ["Koeffizient", "die Zahl vor der Variablen, z. B. die 6 in 6x³"]]

Lernkarte `terme_vereinfachen`, Feld `schritte`: alt [{"text": "Der Koeffizient 6 bleibt. Bei x addierst du: 3 + (−5) = −2.", "bild": {"zeilen": [["Start", "6x³ · x⁻⁵"], ["zusammengefasst", "6x⁻²"]]}}, {"text": "Nur x hat den negativen Exponenten: x⁻² = 1/x²."}, {"text": "Also 6x³ · x⁻⁵ = ⟦6/x²⟧ für x ≠ 0.", "bild": {"zeilen": [["Start", "6x³ · x⁻⁵"], ["zusammengefasst", "6x⁻²"], ["als Bruchterm", "6/x²"]]}}] → neu [{"text": "Der Koeffizient 6 bleibt. Bei x addierst du: 3 + (−5) = −2.", "bild": {"zeilen": [["Start", "6x³ · x⁻⁵"], ["zusammengefasst", "6x⁻²"]]}}, {"text": "Nur x hat den negativen Exponenten: x⁻² = 1/x²."}, {"text": "Also 6x³ · x⁻⁵ = ⟦6/x²⟧ für x ≠ 0.", "bild": {"zeilen": [["Start", "6x³ · x⁻⁵"], ["zusammengefasst", "6x⁻²"], ["als Bruch", "6/x²"]]}}]


**Sonstiges, ohne Aufgaben**
- Gym 6, `offen`: „rationale Exponenten im umfang“ und das Beispiel „2³ · 2⁴ = 2ᵏ“ entfernt (Kann 3). Jetzt: „Rationale Exponenten stehen nicht in diesem Flug …“ und als Beispiel „2ᵏ = 1/16, k = ?“.
- Flug A:
  - Inhalt: Ziel, Merke („Potenz einer Potenz: (aᵐ)ⁿ = aᵐ·ⁿ.“), `offen` und `quellen` angepasst. Abschnitt „Potenzen malnehmen“ = `mal_gleiche_basis`, `gleicher_exponent`, `potenz_von_potenz`. Pflicht: `mal_gleiche_basis`, `gleicher_exponent`, `potenz_von_potenz`.
  - `klasse.ib_myp` 4 → 3.
- Flug B: Ziel und `offen` ohne „Bruchterm“ als Voraussetzung für RS/IB.
- Themenliste:
  - Flug A: `klasse`/`reihenfolge`/`lernbereich` für IB (MYP 3, Nummer 2), `umfang` mit „Potenzen von Potenzen“, `lehrplan_gym` um „M7 1.2 Potenzen von Potenzen mit natürlichen Exponenten zusammenfassen“ ergänzt, `lehrplan_ib` neu als Annahme.
  - Flug B: `umfang` „als Bruch schreiben“.
  - `terme.umformen`: `lehrplan_rs` „Terme vereinfachen; Äquivalenz von Termen begründen (die Potenzgesetze stehen in eigenen Flügen)“ (Kann 4).
  - Reihenfolgen MYP 3 und MYP 4 wie oben.
- kann-Texte: Gym 6, `kurz`: „Du lernst, Potenzen zu berechnen, auch mit Hoch 0 und mit negativen Hochzahlen.“ (Kann 5). Flug A neu `potenz_von_potenz`: „eine Potenz einer Potenz wie (2³)⁴ vereinfachen, indem du die Exponenten malnimmst“.
- **Quelle M7 1.2 („Potenzen von Potenzen“):** LehrplanPLUS Gymnasium 7, https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik, Abschnitt M7 1.2. Abgerufen hat ihn am 20.11.2026 der Chat `lehrplan-lb`; das Zitat steht in `inhalte/pruefung/aufbau/klasse6.json` und im Prüfbericht. Ich selbst habe die Seite nicht geöffnet.

### Selbstprüfung Reihenfolgen
`python3 -I inhalte/generatoren/_potenz_teilen_liste.py`: Alle Schularten und Klassen sind lückenlos und eindeutig (MYP 3: 13 Themen, MYP 4: 28 Themen). Die Lernbereiche hängen zusammen. Die einzige Ausnahme ist der bekannte Befund Gym 6 aus LB-4. Ausgabe: „Selbstprüfung: OK“.

### Nicht geprüft
- Die Anzeige in der App: Tabellenbilder der neuen Karte.
- Die Lehrplantexte im Original.
- Der Lernstand eines Kindes: Für die umgestuften Aufgaben in Flug A gilt beim Einspielen dasselbe wie in der Sechsundzwanzigsten Runde. Gleicher Text heißt gleiche Aufgabe, nur Stufe und Typ sind neu.

## 2026-11-20 22:50 – FERTIG: Potenzgesetze geteilt

Zweig `potenz-teilen` (von `lernen-app`, e71a72d). Commits: Flug A 56cbd40 · Flug B 1e14734 · Themenliste und Texte c13e59d · dieser Bericht. Nichts in die Datenbank geschrieben, kein App-Code, kein Merge, keine Kinderdaten, keine Schulbuchaufgaben.

### Kurz
- **Flug A `terme.potenzgesetze_natuerlich`** (thema_id 102, block_id 62 Samarkand, Gym 7 · RS 7 · MYP 4): die vier Lernkarten aus `terme.umformen` mit **unveränderten Lernziel-Schlüsseln** (`mal_gleiche_basis`, `gleicher_exponent` Pflicht; `geteilt_gleiche_basis`, `anwenden` Vertiefung). Karten (Erklärungen) Zeichen für Zeichen wie bisher. 191 Aufgaben.
- **Flug B `terme.potenzgesetze_ganzzahlig`** (thema_id 103, block_id 60 Mumbai, Gym 8 · RS 7 · MYP 4): neu, 5 Lernkarten (`warum_gilt`, `gleiche_basis_ganz`, `exponent_und_potenz`, `terme_vereinfachen` Pflicht; `fehler_ganz` Vertiefung), Erklärungen nach der Vorgabe vom 16.11. (eine Algenfläche, die sich täglich verdoppelt, als durchgehende Situation). 175 Aufgaben.
- **`terme.umformen`:** die vier Karten (168 Aufgaben) entfallen; die übrigen 8 Karten und ihre 273 Aufgaben sind Zeichen für Zeichen gleich (im Generator geprüft). Ziel und Merke angepasst.
- **`terme.potenzgesetze` (Gym 6):** „Fehler finden“ nur noch zu Potenzbegriff, Hoch 0 und negativem Exponenten; 23 Aufgaben nach Flug A, 14 neu gebaut, Karte neu erklärt. Titel in der Themenliste „Potenzen und negative Exponenten“.
- **Themenliste:** zwei neue Einträge, Reihenfolgen nachgezogen; Selbstprüfung lückenlos und eindeutig (unten). **kann-Texte:** zwei neue Dateien, `terme.umformen` ohne die vier Lernziele, `terme.potenzgesetze` ein Text angeglichen.
- `python3 -I tools/inhalt_pruefen.py --alle`: **118 × OK**, Rückgabewert 0 (vorher 116). Ohne Hinweise zu den Karten der neuen und geänderten Flüge; „gleich gebaut hintereinander“ überall 0.

### Abweichungen vom Auftrag (bitte ansehen)
1. **29 statt 22 Aufgaben nach Flug B.** 22 haben einen negativen Exponenten im Text (wie gezählt). 7 weitere haben ihn im Ergebnis: Das Gesetz liefert aᵐ⁻ⁿ mit m < n (z. B. „3⁴ : 3⁸ = 3ᵏ“, k = −4). Das ist M8-4-Stoff, deshalb auch nach Flug B und in Flug A ersetzt. Zwei weitere Aufgaben gehen auch ohne negativen Exponenten; dort habe ich nur Lösungsweg und Tipp neu geschrieben (Frage und Lösung gleich).
2. **23 statt 19 Aufgaben aus Gym 6 nach Flug A.** Maßgeblich war die Regel der Entscheidung („In Gym 6 bleiben nur Aufgaben zu Potenzbegriff, Hoch 0 und negativem Exponenten“). Vermutlich nicht mitgezählt waren: „Welche Rechnung ist richtig?“ (3² · 3⁴ …), die Parameter-Aufgabe zu „a² · a³ = a⁶“, die Rückwärts-Aufgabe zu aᵏ · a² und die Knobel-Aufgabe 2⁵ + 2⁵. Keine der 23 hat einen negativen Exponenten im Text; nach Flug B ging deshalb keine.
3. **Alle 23 sind jetzt Übungen Stufe 3 vom Typ „fehler“**, wie verlangt – auch die früheren Test-, Korrektur-, Sicherungs- und Knobel-Aufgaben (8 davon bekamen einen Tipp, Übungen brauchen einen). Folge: In `mal_gleiche_basis` hat Stufe 3 jetzt 22 Übungen, davon 15 „fehler“, darunter leichte wie „Stimmt die Rechnung? 4⁴ · 4² = 4⁶“. Das Prüfskript ist zufrieden (je Typ und Satzbau höchstens 2), die Regel „Stufe 3 je Typ höchstens 3“ aus `_bereinigen` gilt hier nur je Satzbau. **Für den Nutzer:** Sollen die vier „Stimmt die Rechnung? …“-Aufgaben lieber Stufe 1 „erkennen“ werden?
4. **Antworten geändert, ohne Frage und richtige Antwort zu ändern:** In 4 umgezogenen Aufgaben (Flug A) stand eine falsche Antwort mit negativem Exponenten („Ein negativer Exponent bedeutet Kehrbruch …“). Sie ist durch einen typischen Fehler mit natürlichen Exponenten ersetzt. In Gym 6 nannten 5 bleibende Aufgaben Potenzgesetze als falsche Antworten („Exponenten subtrahieren, nicht teilen: 4⁸“). Die sind durch typische Fehler beim negativen Exponenten ersetzt („Richtig wäre −12, denn man rechnet 4 · (−3)“, „Richtig wäre 1/12“). Dazu zwei Lösungswege bzw. Tipps in Gym 6 ohne Potenzgesetz.
5. **Themenliste `terme.potenzgesetze`:** Neben Titel, `umfang` und dem dritten Eintrag habe ich auch den **zweiten** Eintrag von `lehrplan_gym` geändert („Potenzen mit gleicher Basis oder gleichem natürlichen Exponenten zusammenfassen“ war ebenfalls ein Gesetzes-Versprechen) sowie `lehrplan_rs` und `lehrplan_ib` (beide nannten Potenzgesetze). Neu: „Potenzen mit rationaler Basis und natürlichen Exponenten berechnen“ (M6 1.4, laut `inhalte/pruefung/aufbau/klasse6.json`), „Typische Fehler bei Potenzen mit einer Zahlenprobe erkennen (Vertiefung)“.
6. **Flug B: Stufe und Typ der 29 übernommenen Aufgaben angepasst** (Text, Antworten, Lösung gleich). Zweierprodukte und -quotienten wie „z³ · z⁻⁵ = zᵏ“ sind in diesem Flug die Grundform → Stufe 1 „direkt“; Dreierprodukte und die Dezimal-Aufgaben → Stufe 2 „mehrschritt“. Test-, Korrektur- und Sicherungsaufgaben blieben in ihrem Pool. Darum hat `gleiche_basis_ganz` 4 Korrektur- und 10 Sicherungsaufgaben.

### Zählung je Flug, Karte, Pool und Stufe

**terme.potenzgesetze_natuerlich** (thema_id 102, block_id 62, klasse {'gym_by': 7, 'rs_by': 7, 'ib_myp': 4}) – 191 Aufgaben

| Lernkarte | P/V | Übung S1 | Übung S2 | Übung S3 | davon ohne Typ | Knobel | Test | Korrektur | Sicherung | zusammen |
|---|---|---|---|---|---|---|---|---|---|---|
| mal_gleiche_basis | P | 9 | 13 | 22 | 0 | 2 | 1 | 3 | 6 | 56 |
| gleicher_exponent | P | 10 | 12 | 11 | 2 | 2 | 1 | 3 | 6 | 45 |
| geteilt_gleiche_basis | V | 7 | 16 | 13 | 0 | 2 | 1 | 3 | 6 | 48 |
| anwenden | V | 7 | 14 | 9 | 0 | 2 | 1 | 3 | 6 | 42 |

**terme.potenzgesetze_ganzzahlig** (thema_id 103, block_id 60, klasse {'gym_by': 8, 'rs_by': 7, 'ib_myp': 4}) – 175 Aufgaben

| Lernkarte | P/V | Übung S1 | Übung S2 | Übung S3 | davon ohne Typ | Knobel | Test | Korrektur | Sicherung | zusammen |
|---|---|---|---|---|---|---|---|---|---|---|
| warum_gilt | P | 5 | 8 | 9 | 0 | 2 | 1 | 3 | 6 | 34 |
| gleiche_basis_ganz | P | 9 | 9 | 8 | 0 | 2 | 1 | 4 | 10 | 43 |
| exponent_und_potenz | P | 6 | 8 | 8 | 0 | 2 | 1 | 3 | 6 | 34 |
| terme_vereinfachen | P | 5 | 7 | 8 | 0 | 2 | 1 | 3 | 6 | 32 |
| fehler_ganz | V | 5 | 6 | 9 | 0 | 2 | 1 | 3 | 6 | 32 |

**terme.potenzgesetze** (thema_id 30, block_id 44, klasse {'gym_by': 6, 'rs_by': 7, 'ib_myp': 3}) – 109 Aufgaben

| Lernkarte | P/V | Übung S1 | Übung S2 | Übung S3 | davon ohne Typ | Knobel | Test | Korrektur | Sicherung | zusammen |
|---|---|---|---|---|---|---|---|---|---|---|
| potenz_begriff | P | 8 | 11 | 8 | 0 | 2 | 1 | 3 | 6 | 39 |
| negativer_exponent | P | 5 | 13 | 8 | 0 | 2 | 1 | 3 | 6 | 38 |
| fehler_finden | V | 4 | 8 | 8 | 0 | 2 | 1 | 3 | 6 | 32 |

**terme.umformen** (thema_id 29, block_id 62, klasse {'gym_by': 7}) – 273 Aufgaben

| Lernkarte | P/V | Übung S1 | Übung S2 | Übung S3 | davon ohne Typ | Knobel | Test | Korrektur | Sicherung | zusammen |
|---|---|---|---|---|---|---|---|---|---|---|
| zusammenfassen | P | 5 | 7 | 8 | 0 | 2 | 1 | 3 | 6 | 32 |
| produkte | P | 5 | 7 | 8 | 1 | 2 | 1 | 3 | 6 | 32 |
| minusklammer | P | 6 | 9 | 8 | 0 | 2 | 1 | 3 | 6 | 35 |
| ausmultiplizieren | P | 6 | 10 | 8 | 2 | 2 | 1 | 3 | 6 | 36 |
| summe_mal_summe | P | 6 | 9 | 8 | 3 | 2 | 1 | 3 | 6 | 35 |
| ausklammern | P | 6 | 8 | 8 | 4 | 2 | 1 | 3 | 6 | 34 |
| aequivalenz | P | 10 | 6 | 8 | 4 | 2 | 1 | 3 | 6 | 36 |
| binomisch | P | 6 | 7 | 8 | 2 | 2 | 1 | 3 | 6 | 33 |

`terme.umformen`: unverändert gegenüber vorher, nur die vier Karten fehlen (vorher 12 Karten, 441 Aufgaben).

### Was wohin umgezogen ist (alt → neu)
**1. terme.umformen → Flug B (29 Aufgaben; Text, Antworten, Lösung gleich)**

| Fragetext | vorher (Karte, Pool, Stufe/Typ) | nachher in Flug B |
|---|---|---|
| z³ · z⁻⁵ = zᵏ. Wie groß ist k? | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| y⁻³ · y⁻¹ = yᵏ. Wie groß ist k? | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| 10⁻¹ · 10⁵ · 10² = 10ᵏ. Wie groß ist k? | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 2/mehrschritt |
| 3⁻² · 3⁻³ · 3⁻¹ = 3ᵏ. Wie groß ist k? | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 2/mehrschritt |
| Berechne 10⁶ · 10⁻⁸ und gib das Ergebnis als Dezimalzahl an. | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 2/mehrschritt |
| Berechne 10² · 10⁻⁸ und gib das Ergebnis als Dezimalzahl an. | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 2/mehrschritt |
| 3⁴ · 3⁻⁶ = 3ᵏ. Wie groß ist k? | mal_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| b³ · b⁻⁵ = bᵏ. Wie groß ist k? | mal_gleiche_basis, Korrektur, 2/– | gleiche_basis_ganz, Korrektur, 2/– |
| a³ · a⁻⁵ = aᵏ. Wie groß ist k? | mal_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| 10³ · 10⁻² · 10⁵ = 10ᵏ. Wie groß ist k? | mal_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| b⁻³ · b⁻¹ = bᵏ. Wie groß ist k? | mal_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| b⁻³ · b⁻⁵ = bᵏ. Wie groß ist k? | mal_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| a⁻² · a⁻² = aᵏ. Wie groß ist k? | mal_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| Berechne geschickt: 2⁻¹ · 5⁻¹ und gib das Ergebnis als Dezimalzahl an. | gleicher_exponent, Übung, 2/mehrschritt | exponent_und_potenz, Übung, 2/mehrschritt |
| Berechne geschickt: 5⁻¹ · 20⁻¹ und gib das Ergebnis als Dezimalzahl an. | gleicher_exponent, Übung, 2/mehrschritt | exponent_und_potenz, Übung, 2/mehrschritt |
| a⁻³ : a³ = aᵏ. Wie groß ist k? | geteilt_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| 3⁴ : 3⁸ = 3ᵏ. Wie groß ist k? | geteilt_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| z⁻² : z⁵ = zᵏ. Wie groß ist k? | geteilt_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| 2¹ : 2⁷ = 2ᵏ. Wie groß ist k? | geteilt_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 1/direkt |
| Berechne 10¹ : 10⁶ und gib das Ergebnis als Dezimalzahl an. | geteilt_gleiche_basis, Übung, 2/mehrschritt | gleiche_basis_ganz, Übung, 2/mehrschritt |
| b⁻² : b⁶ = bᵏ. Wie groß ist k? | geteilt_gleiche_basis, Test, 2/– | gleiche_basis_ganz, Test, 2/– |
| 5⁴ : 5⁶ = 5ᵏ. Wie groß ist k? | geteilt_gleiche_basis, Korrektur, 2/– | gleiche_basis_ganz, Korrektur, 2/– |
| 2¹ : 2⁸ = 2ᵏ. Wie groß ist k? | geteilt_gleiche_basis, Korrektur, 2/– | gleiche_basis_ganz, Korrektur, 2/– |
| y¹ : y⁻² = yᵏ. Wie groß ist k? | geteilt_gleiche_basis, Korrektur, 2/– | gleiche_basis_ganz, Korrektur, 2/– |
| y⁴ : y⁶ = yᵏ. Wie groß ist k? | geteilt_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| a⁻³ : a⁴ = aᵏ. Wie groß ist k? | geteilt_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| y⁷ : y⁻⁴ = yᵏ. Wie groß ist k? | geteilt_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| 10¹ : 10⁹ = 10ᵏ. Wie groß ist k? | geteilt_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |
| x⁻⁴ : x⁷ = xᵏ. Wie groß ist k? | geteilt_gleiche_basis, Sicherung, 2/– | gleiche_basis_ganz, Sicherung, 2/– |

**2. Ersatz in Flug A (an derselben Stelle, gleicher Pool, gleiche Stufe, gleicher Typ)**

| Karte | alt (→ Flug B) | neu |
|---|---|---|
| mal_gleiche_basis | z³ · z⁻⁵ = zᵏ. Wie groß ist k? | x⁴ · x² · x³ = xᵏ. Wie groß ist k? |
| mal_gleiche_basis | y⁻³ · y⁻¹ = yᵏ. Wie groß ist k? | b² · b⁵ · b = bᵏ. Wie groß ist k? |
| mal_gleiche_basis | 10⁻¹ · 10⁵ · 10² = 10ᵏ. Wie groß ist k? | 10³ · 10 · 10⁴ = 10ᵏ. Wie groß ist k? |
| mal_gleiche_basis | 3⁻² · 3⁻³ · 3⁻¹ = 3ᵏ. Wie groß ist k? | 2² · 2³ · 2⁴ = 2ᵏ. Wie groß ist k? |
| mal_gleiche_basis | Berechne 10⁶ · 10⁻⁸ und gib das Ergebnis als Dezimalzahl an. | Berechne 10² · 10⁴ mit dem Potenzgesetz. Gib das Ergebnis als Zahl an. |
| mal_gleiche_basis | Berechne 10² · 10⁻⁸ und gib das Ergebnis als Dezimalzahl an. | Berechne 3² · 3² · 3 mit dem Potenzgesetz. Gib das Ergebnis als Zahl an. |
| mal_gleiche_basis | 3⁴ · 3⁻⁶ = 3ᵏ. Wie groß ist k? | 4³ · 4 · 4² = 4ᵏ. Wie groß ist k? |
| mal_gleiche_basis | b³ · b⁻⁵ = bᵏ. Wie groß ist k? | b⁴ · b³ = bᵏ. Wie groß ist k? |
| mal_gleiche_basis | a³ · a⁻⁵ = aᵏ. Wie groß ist k? | a² · a⁷ = aᵏ. Wie groß ist k? |
| mal_gleiche_basis | 10³ · 10⁻² · 10⁵ = 10ᵏ. Wie groß ist k? | 10² · 10³ · 10⁴ = 10ᵏ. Wie groß ist k? |
| mal_gleiche_basis | b⁻³ · b⁻¹ = bᵏ. Wie groß ist k? | b⁴ · b · b² = bᵏ. Wie groß ist k? |
| mal_gleiche_basis | b⁻³ · b⁻⁵ = bᵏ. Wie groß ist k? | x³ · x⁵ = xᵏ. Wie groß ist k? |
| mal_gleiche_basis | a⁻² · a⁻² = aᵏ. Wie groß ist k? | y⁶ · y⁶ = yᵏ. Wie groß ist k? |
| gleicher_exponent | Berechne geschickt: 2⁻¹ · 5⁻¹ und gib das Ergebnis als Dezimalzahl an. | Berechne geschickt: 0,2⁵ · 50⁵ |
| gleicher_exponent | Berechne geschickt: 5⁻¹ · 20⁻¹ und gib das Ergebnis als Dezimalzahl an. | Berechne geschickt: 2,5² · 4² · 10² |
| geteilt_gleiche_basis | a⁻³ : a³ = aᵏ. Wie groß ist k? | z⁹ : z² : z³ = zᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | 3⁴ : 3⁸ = 3ᵏ. Wie groß ist k? | a⁶ · a⁴ : a⁷ = aᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | z⁻² : z⁵ = zᵏ. Wie groß ist k? | 2⁴ · 2⁵ : 2⁶ = 2ᵉ. Wie groß ist e? |
| geteilt_gleiche_basis | 2¹ : 2⁷ = 2ᵏ. Wie groß ist k? | Berechne 10⁷ : 10³. Gib das Ergebnis als Zahl an. |
| geteilt_gleiche_basis | Berechne 10¹ : 10⁶ und gib das Ergebnis als Dezimalzahl an. | x¹² : x⁵ : x⁴ = xᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | b⁻² : b⁶ = bᵏ. Wie groß ist k? | b⁹ : b³ = bᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | 5⁴ : 5⁶ = 5ᵏ. Wie groß ist k? | 5⁸ : 5³ = 5ᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | 2¹ : 2⁸ = 2ᵏ. Wie groß ist k? | 2⁹ : 2² = 2ᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | y¹ : y⁻² = yᵏ. Wie groß ist k? | y⁷ : y = yᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | y⁴ : y⁶ = yᵏ. Wie groß ist k? | y⁸ : y⁵ = yᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | a⁻³ : a⁴ = aᵏ. Wie groß ist k? | a¹⁰ : a⁴ = aᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | y⁷ : y⁻⁴ = yᵏ. Wie groß ist k? | x⁹ : x² = xᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | 10¹ : 10⁹ = 10ᵏ. Wie groß ist k? | 10⁹ : 10⁵ = 10ᵏ. Wie groß ist k? |
| geteilt_gleiche_basis | x⁻⁴ : x⁷ = xᵏ. Wie groß ist k? | b¹¹ : b³ = bᵏ. Wie groß ist k? |

Nur Lösungsweg und Tipp neu (ohne negativen Exponenten): „2¹⁰ : 2ⁿ = 1/4. Wie groß ist n?“ (geteilt_gleiche_basis); „Berechne 10⁴ : 10⁴ : 10⁴ · 10⁸.“ (geteilt_gleiche_basis).

**3. terme.potenzgesetze/fehler_finden → Flug A (23 Aufgaben, alle als Übung Stufe 3 „fehler“)**

| Fragetext | vorher (Pool, Stufe/Typ) | nachher (Karte) |
|---|---|---|
| Stimmt die Rechnung? 5² · 5² = 5⁴ | Übung, 1/erkennen | mal_gleiche_basis |
| Ein Kind rechnet: 3⁹ : 3³ = 3³. Welcher Satz beschreibt den Fehler richtig? | Übung, 2/mehrschritt | geteilt_gleiche_basis |
| Stimmt die Rechnung? 4⁵ : 4² = 4³ | Übung, 2/mehrschritt | geteilt_gleiche_basis |
| Stimmt die Rechnung? 4⁴ · 4² = 4⁶ | Übung, 1/erkennen | mal_gleiche_basis |
| Stimmt die Rechnung? 2⁴ · 2³ = 2⁷ | Übung, 1/erkennen | mal_gleiche_basis |
| Ein Kind rechnet: 2² · 5² = 10⁴. Was ist falsch? | Übung, 2/mehrschritt | gleicher_exponent |
| Ein Kind rechnet: 2³ · 5³ = 10⁶. Was ist falsch? | Übung, 2/mehrschritt | gleicher_exponent |
| Ein Kind rechnet: 3³ · 3³ = 9⁶. Welcher Satz beschreibt den Fehler richtig? | Übung, 3/fehler | mal_gleiche_basis |
| Ein Kind rechnet: 4³ · 4² = 16⁵. Welcher Satz beschreibt den Fehler richtig? | Übung, 2/mehrschritt | mal_gleiche_basis |
| Stimmt die Rechnung? 5² · 5³ = 5⁶ | Test, 2/– | mal_gleiche_basis |
| Ein Kind rechnet: 3⁴ · 3⁴ = 9⁸. Was ist falsch? | Korrektur, 2/– | mal_gleiche_basis |
| Ein Kind rechnet: 2⁴ · 5⁴ = 10⁸. Was ist falsch? | Korrektur, 2/– | gleicher_exponent |
| Stimmt die Rechnung? 4⁷ : 4⁴ = 4³ | Sicherung, 2/– | geteilt_gleiche_basis |
| Stimmt die Rechnung? 5⁵ : 5² = 5³ | Sicherung, 2/– | geteilt_gleiche_basis |
| Ein Kind rechnet: 4⁴ · 4² = 4⁸. Was ist falsch? | Sicherung, 2/– | mal_gleiche_basis |
| Ein Kind rechnet: 5⁴ · 5⁴ = 5¹⁶. Was ist falsch? | Sicherung, 2/– | mal_gleiche_basis |
| Ein Kind rechnet: 5⁶ : 5² = 5³. Was ist falsch? | Sicherung, 2/– | geteilt_gleiche_basis |
| Ein Kind rechnet: 4³ · 4³ = 4⁹. Welcher Satz beschreibt den Fehler richtig? | Übung, 3/fehler | mal_gleiche_basis |
| Ein Kind rechnet: 4⁴ · 4² = 16⁶. Welcher Satz beschreibt den Fehler richtig? | Übung, 2/mehrschritt | mal_gleiche_basis |
| Welche Rechnung ist richtig? | Übung, 3/begruenden | anwenden |
| Die Regel „a² · a³ = a⁶“ ist falsch. Für welche Zahlen a stimmt sie trotzdem? | Übung, 3/parameter | mal_gleiche_basis |
| Ein Kind hat bei aᵏ · a² die Exponenten malgenommen und a¹² erhalten. Was wäre der richtige Exponent gewesen? | Übung, 3/rueckwaerts | mal_gleiche_basis |
| Ein Kind schreibt 2⁵ + 2⁵ = 2¹⁰. Richtig ist 2ᵏ. Wie groß ist k? | Knobel, 3/knobel | mal_gleiche_basis |

Antwortlisten geändert (eine falsche Antwort mit negativem Exponenten durch einen typischen Fehler mit natürlichen Exponenten ersetzt; Frage und richtige Antwort gleich): „Ein Kind rechnet: 2² · 5² = 10⁴. Was ist falsch?“; „Ein Kind rechnet: 4⁴ · 4² = 4⁸. Was ist falsch?“; „Ein Kind rechnet: 5⁴ · 5⁴ = 5¹⁶. Was ist falsch?“; „Ein Kind rechnet: 5⁶ : 5² = 5³. Was ist falsch?“.

**4. terme.potenzgesetze (Gym 6), fehler_finden: neu (14)**

- Übung, Stufe 3, fehler: Ein Kind rechnet 3⁻² = −9. Wie heißt das richtige Ergebnis?
- Übung, Stufe 3, fehler: Ein Kind rechnet (2/3)² = 4/3. Wie heißt das richtige Ergebnis?
- Übung, Stufe 3, rueckwaerts: Ein Kind sollte 2ⁿ ausrechnen. Es hat aus Versehen 2 · n gerechnet und 10 erhalten. Welches Ergebnis wäre richtig gewesen?
- Übung, Stufe 3, parameter: Für wie viele natürliche Zahlen n von 1 bis 10 ist (−2)ⁿ negativ?
- Übung, Stufe 3, transfer: In einem Datenblatt steht: Dicke 10⁻³ m. Ein Kind meint, das sei eine negative Dicke. Wie viele Millimeter sind 10⁻³ m wirklich?
- Knobel, Stufe 3, knobel: Ein Kind behauptet: (−1)¹⁰⁰ + (−1)¹⁰¹ + 1⁻¹⁰⁰ = 3. Was kommt wirklich heraus?
- Test, Stufe 2: Ein Kind rechnet: 10⁻² = −100. Was ist falsch?
- Korrektur, Stufe 2: Ein Kind rechnet 0,3² = 0,9. Wie heißt das richtige Ergebnis?
- Korrektur, Stufe 2: Stimmt die Rechnung? 7⁰ = 7
- Sicherung, Stufe 2: Ein Kind rechnet 2⁻⁴ = −16. Wie heißt das richtige Ergebnis als Dezimalzahl?
- Sicherung, Stufe 2: Ein Kind rechnet (−3)² = −9. Wie heißt das richtige Ergebnis?
- Sicherung, Stufe 2: Ein Kind rechnet 4³ = 12. Wie heißt das richtige Ergebnis?
- Sicherung, Stufe 2: Stimmt die Rechnung? (−2)³ = −8
- Sicherung, Stufe 2: Ein Kind rechnet −2⁴ = 16. Wie heißt das richtige Ergebnis?

Antwortlisten ohne Potenzgesetze (je 2 falsche Antworten ersetzt, Frage und richtige Antwort gleich): „Ein Kind rechnet: 4⁻³ = −64. Was ist falsch?“; „Ein Kind rechnet: 4⁻⁴ = −256. Was ist falsch?“; „Ein Kind rechnet: 5⁻⁴ = −625. Was ist falsch?“; „Ein Kind rechnet: 5⁻² = −25. Was ist falsch?“; „Ein Kind rechnet: 2⁻³ = −8. Was ist falsch?“.
Nur Lösungsweg bzw. Tipp neu: „Wie viel Mal so groß ist 2² wie 2⁻²?“ (negativer_exponent, w); „Ein Kind rechnet 2³ + 2³ = 2⁶. Welche Zahl ist richtig?“ (fehler_finden, h).

### Einordnung (Themenliste)
| | Flug A | Flug B |
|---|---|---|
| `reihenfolge.gym_by` | 2 (Kl. 7: ab `terme.umformen` alles +1) | 8 (Kl. 8: ab `gleichungen.bruch` alles +1) |
| `reihenfolge.rs_by` | 2 (Kl. 7, hinter `terme.potenzgesetze`) | 3 (direkt hinter A, vor `zahlen.potenzen_zehner`; ab dort alles +2) |
| `reihenfolge.ib_myp` | 1 (MYP 4, alles +2) | 2 |
| `lernbereich` | Gym „M7 1 Terme mit Variablen“ · RS „M7 1 Potenzen“ · IB „MYP 4 Numerical and abstract reasoning (Zahl und Algebra)“ | Gym „M8 4 Bruchterme und Bruchgleichungen“ · RS „M7 1 Potenzen“ · IB wie A |

- **Belegt:** Gym M7 1.2 („Produkte von Potenzen mit natürlichen Exponenten (bei gleicher Basis oder gleichem Exponenten) … zusammenfassen“, auch „Potenzen von Potenzen“); Gym M8 4 („machen die Rechengesetze für Potenzen mit ganzzahligen Exponenten plausibel und wenden diese in einfachen Fällen an“); RS M7 1 Potenzen enthält negative Exponenten und Potenzgesetze; IB: Potenzgesetze mit ganzzahligen/negativen Exponenten = MYP 4–5 Standard.
- **Annahme (so gekennzeichnet):** die Aufteilung der RS-Potenzgesetze auf zwei Flüge und ihre Nummern 2/3 (der Lehrplan gibt die Reihenfolge innerhalb eines Lernbereichs nicht vor); IB-Nummern 1/2 (das MYP gibt keine Reihenfolge vor); IB-Stufe für Flug A und den neuen IB-Text von `terme.potenzgesetze`.
- Selbstprüfung (Skript `inhalte/generatoren/_potenz_teilen_liste.py`, Ausgabe unverändert):
```
Themenliste: schon nachgezogen, nur Prüfung
gym_by  Kl.  5: 14 Themen · Nummern 1–14 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
gym_by  Kl.  6: 11 Themen · Nummern 1–11 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: NEIN (3 Überschriften)
gym_by  Kl.  7: 10 Themen · Nummern 1–10 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (5 Überschriften)
gym_by  Kl.  8: 15 Themen · Nummern 1–15 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (7 Überschriften)
gym_by  Kl.  9: 14 Themen · Nummern 1–14 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (7 Überschriften)
gym_by  Kl. 10:  9 Themen · Nummern 1–9 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (5 Überschriften)
rs_by   Kl.  5: 12 Themen · Nummern 1–12 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (6 Überschriften)
rs_by   Kl.  6: 11 Themen · Nummern 1–11 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (6 Überschriften)
rs_by   Kl.  7: 20 Themen · Nummern 1–20 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (7 Überschriften)
rs_by   Kl.  8:  7 Themen · Nummern 1–7 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
rs_by   Kl.  9: 17 Themen · Nummern 1–17 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (8 Überschriften)
rs_by   Kl. 10: 11 Themen · Nummern 1–11 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (5 Überschriften)
ib_myp  Kl.  1: 15 Themen · Nummern 1–15 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (3 Überschriften)
ib_myp  Kl.  2: 12 Themen · Nummern 1–12 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (3 Überschriften)
ib_myp  Kl.  3: 12 Themen · Nummern 1–12 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
ib_myp  Kl.  4: 29 Themen · Nummern 1–29 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
ib_myp  Kl.  5: 18 Themen · Nummern 1–18 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
terme.potenzgesetze_natuerlich: kurz 91 Zeichen, 4 Etappen, längster kann-Text 75 Zeichen
terme.potenzgesetze_ganzzahlig: kurz 98 Zeichen, 5 Etappen, längster kann-Text 86 Zeichen
terme.umformen: kurz 92 Zeichen, 8 Etappen, längster kann-Text 90 Zeichen
terme.potenzgesetze: kurz 85 Zeichen, 3 Etappen, längster kann-Text 84 Zeichen
Selbstprüfung: OK
```
  Gym 6 „Lernbereiche zusammenhängend: NEIN“ ist der bekannte Befund aus LB-4 (nicht Teil dieses Auftrags, unverändert).
- **Lehrplan-Quellen:** LehrplanPLUS Gymnasium 7 und 8 (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik · …/gymnasium/8/mathematik, Abschnitte M7 1.2 und M8 4), Realschule 7 Gruppe I (…/realschule/7/mathematik/wpfg1, M7 1), IB MYP Mathematics guide 2020 (Framework S. 23–29) – **alle abgerufen am 20.11.2026 durch den Chat `lehrplan-lb`** (Postfach `lehrplan-lb.md`, Abschnitt „Quellen“; Zitat M8 4 dort im Auftragsentwurf; Zitat M7 1.2 in `inhalte/pruefung/aufbau/klasse6.json`). **Ich habe die Seiten nicht selbst geöffnet:** Die Abruf-Freigabe wurde in diesem Chat nicht beantwortet.

### Texte für die Abschluss-Ansichten (`inhalte/kann/`)
- `terme.potenzgesetze_natuerlich.json`: kurz „Du lernst, Potenzen mit gleicher Basis oder gleichem Exponenten geschickt zusammenzufassen.“ (91 Zeichen); die vier kann-Texte unverändert aus `terme.umformen`.
- `terme.potenzgesetze_ganzzahlig.json`: kurz 98 Zeichen, 5 kann-Texte (höchstens 86 Zeichen).
- `terme.umformen.json`: die vier Lernziele gestrichen. `terme.potenzgesetze.json`: `fehler_finden` an den neuen Inhalt angeglichen („Fehler bei Potenzen und negativen Exponenten finden und mit einer Zahlenprobe prüfen“).
- Selbstprüfung: jede Etappe genau ein Eintrag, keine überzähligen, Längen eingehalten, gültiges JSON (siehe Ausgabe oben).

### Nachgerechnet
- Jede Aufgabe mit Zahl- oder Lücken-Lösung wird beim Bauen gegen ihr `c` gerechnet (Generator) und vom Prüfskript noch einmal.
- **Unabhängig von `c`:** Ein eigenes Skript übersetzt die Terme aus dem Fragetext und setzt die Lösung ein (Variablen mit zwei verschiedenen Zahlen belegt): 202 Aufgaben der vier Flüge automatisch, 0 Fehler.
- **Von Hand:** alle 122 übrigen neuen Aufgaben (Sachaufgaben, Auswahl, Muster) einzeln gelesen und nachgerechnet, dazu die geänderten Antwortlisten (richtige Antwort weiter richtig, ersetzte falsche Antworten wirklich falsch). Einen unglücklichen Satz habe ich dabei umformuliert.

### Für den Haupt-Chat
- **Lernstand umhängen:** Die vier Lernziele haben in Flug A dieselben Schlüssel. Achtung: 29 Aufgaben, die bisher zu diesen Karten in Thema 29 gehörten, stehen jetzt in Thema 103 (Liste 1). 29 Aufgaben in Flug A sind neu (Liste 2). Die 23 Aufgaben aus Thema 30 haben jetzt eine andere Karte, einen anderen Pool, Stufe 3 und Typ „fehler“ (Liste 3).
- Expeditionen verweisen auf keine der betroffenen Lernkarten (per Skript geprüft).
- `terme.umformen` behält in der Themendatei `klasse` nur `gym_by` (unverändert). Der `lehrplan_rs`-Text von `terme.umformen` („… auch mit Potenzgesetzen …“) ist unverändert. Er könnte Wortlaut des RS-Lernbereichs M7 6 sein; nicht geprüft.

### Offen / nicht geprüft
- **M7 1.2 „Potenzen von Potenzen“** hat in Flug A keine Karte (in Flug B: `exponent_und_potenz`). Vorschlag: eigene Karte in Flug A – der Nutzer entscheidet. Steht auch unter `offen` in der Themendatei.
- Nicht in der App angesehen: Tabellen als Kartenbild und in einer Aufgabe, Lücken „c = □; n = □“ (Flug B, `terme_vereinfachen`).
- Alte, unveränderte Aufgaben nur über `c` und das Prüfskript nachgerechnet, nicht von Hand.
- Lehrplantexte nicht selbst gelesen (siehe Quellen).

## 2026-11-20 22:41 – STATUS
Flug B `terme.potenzgesetze_ganzzahlig` gebaut, Prüfskript OK (Commit 1e14734). Weiter mit Themenliste und Texten.

## 2026-11-20 22:40 – STATUS
Flug A `terme.potenzgesetze_natuerlich`, `terme.umformen` und `terme.potenzgesetze` umgebaut, Prüfskript OK (Commit 56cbd40). Weiter mit Flug B.
