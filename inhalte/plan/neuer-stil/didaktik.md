# Neuer Stil – Teil 2: Didaktik der Prüfungsformen

Stand 28.11.2026. Kennzeichen wie in `bestand.md`: **[B]** belegt · **[R]** Repo gezählt · **[A]** Annahme · **[S]** Schätzung · **[M]** Meinung (Fachurteil des Helfers in der Rolle Mathe-Didaktiker). Dieser Teil ist überwiegend **[M]**; Zahlen sind belegt, soweit angegeben.

## 1. Was eine Prüfungsaufgabe können muss (Maßstab)

1. **Eindeutig bewertbar** mit den vorhandenen Antworttypen (zahl, auswahl, luecken mit ganzen Zahlen, markierung, text, bedingung) [B] `bestand.md` c).
2. **Nicht erratbar**: Ratewahrscheinlichkeit je Aufgabe höchstens 1/4, besser ≈ 0. Im Test gibt es **keinen** zweiten Versuch [B] – anders als im Üben, wo eine 3er-Auswahl mit zweitem Anlauf zu 2/3 erraten wird (`lernen.js` 4569 `zweiteChance`).
3. **Fair schwer**: Stufe 2 wie der Bestand der Test-Pools [L]; der Lesestoff darf nicht schwerer sein als die Mathematik.
4. **Kein Gerüst**: Kein Lückenweg mit vorgegebenen Schritten, kein Tipp (der Test zeigt ohnehin keinen [B]).
5. **Bekannte Form**: Die Bauart muss das Kind im Üben schon erlebt haben, sonst misst die Aufgabe das Lesen der Bauart, nicht den Stoff.
6. **Nicht schon gesehen**: keine Übungsaufgabe mit anderen Zahlen (Wiedererkennen statt Verstehen).

## 2. Was „Verstehen“ im Test heißen soll – Vorschlag Klasse V

Zwei Sichten liegen vor [B]: Mathe-Profi (`rollend-2/verhaeltnis.md` Z. 62–76) zählt umkehr, rueckwaerts, verknuepfen zu **Rechnen**; der Projektleiter zählt sie (und transfer) zu **verstehensnah**.
[M] Für einen **Prüfungsnachweis** schlage ich eine enge, prüfbare Klasse vor:

- **V (Verstehen nachgewiesen)**, wenn mindestens eins gilt:
  - `form` ∈ fehler_detektiv, verfahren_waehlen, zwei_wege, bruecke, umkehren, viele_antworten;
  - `typ` ∈ begruenden, fehler, darstellung, parameter, umkehr, rueckwaerts, transfer.
- **R (Rechnen)**: `typ` ∈ direkt, mehrschritt, verknuepfen, einkleidung, pruefung, erkennen (sofern keine V-Form).
- `lueckenweg` ist nie Prüfung; `anwenden` ist R, außer mit `typ` transfer (Modell selbst aufstellen).

Begründung: Umkehren/Rückwärts sind zwar „Rechnen“, verlangen aber, die Beziehung zwischen den Größen zu durchschauen – genau das, was der Leitsatz („Zusammenhänge logisch erklären, nicht auswendig“) meint. `erkennen` (ablesen, benennen) bleibt R, weil es meist Wiedererkennen prüft. Diese Klasse muss der Mathe-Profi bestätigen (Frage an ihn, nicht an den Auftraggeber).

## 3. Die acht Formen einzeln

Ratewahrscheinlichkeit nach Antworttyp [R] (`bestand.md` c)). „Ja*“ = ja mit der genannten Bedingung.

| Form | Flugtest | Korrektur | Nachtest (Langzeit) | Begründung / Bedingung |
|---|---|---|---|---|
| **lueckenweg** | nein | nein | nein | Gerüst, zählt schon im Üben nicht; die Schritte sind vorgegeben. Bleibt Übungs- und Hilfsform. |
| **fehler_detektiv** | ja* | **ja** | ja* | Heute 256 von 344 als 3er-Auswahl (33 % Rate), 88 als 4er (25 %). Im Test nur als **„Zeile wählen UND richtig stellen“**: `luecken` mit Schablone „Fehler in Zeile □, richtig ist □“ → Raten praktisch 0. Für die Korrektur besonders passend: sie zielt auf den typischen Fehler, an dem das Kind gescheitert ist. Klasse 5: höchstens 3 Zeilen, ganze Zahlen. |
| **verfahren_waehlen** | ja* | ja* | **ja** | 4er-Auswahl (25 %). Im Test **mit Ausführung koppeln** („Wähle den Weg und rechne“: luecken „Weg □, Ergebnis □“) oder zwei Teilaufgaben, die beide stimmen müssen. Für die Langzeit-Sicherung wertvoll: „wann nehme ich was“ vergisst man zuerst. |
| **zwei_wege** | **ja** | ja | ja | 237 von 252 als `zahl` → kaum erratbar. Prüft, ob das Kind einen zweiten Zugang kennt. Achtung Vorprüfer-Befund „Zwei Wege mit derselben Rechnung“ (`offene-punkte.md`, Erkenntnis Vorprüfung) – im Test nur echte zwei Zugänge. |
| **umkehren** | **ja** | **ja** | **ja** | 307 von 334 als `zahl`. Bester Kandidat: eindeutig, nicht erratbar, prüft Beziehung statt Verfahren, Klasse 5 und 8 gleich gut. |
| **bruecke** | ja* | ja | **ja** | Nur die 87 mit `zahl`/`luecken` ohne Bedingung; die 141 Auswahl-Fassungen nur mit ≥ 4 Möglichkeiten. Prüft Darstellungswechsel (Tabelle ↔ Term ↔ Bild), sehr gut für Langzeit. |
| **anwenden** | ja | ja | ja | 566 von 599 als `zahl`. Fair, aber Lesestoff: in Klasse 5 kurz halten. Zählt als V nur mit `typ` transfer, sonst als R (Sachrechnen). |
| **viele_antworten** (`bedingung`) | ja* | nein | **ja** | Nicht erratbar, technisch im Test geprüft [B] (`tools/tests/bedingung_einspielen2.py` Z. 118–125). Im Flugtest nur, wenn das Kind die Bauart vorher geübt hat (erst 80 Aufgaben). Für die Korrektur ungeeignet, weil die Rückmeldung nur ein Beispiel zeigt und die Korrektur gezielt verbessern soll. |

## 4. Ratewahrscheinlichkeit senken

- **Kopplung** in einer Aufgabe (luecken): Wahl + Wert („Zeile □, richtig □“; „Weg □, Ergebnis □“). Rate ≈ 1/3 × (≈ 0) ≈ 0. **Geht mit heutiger Anzeige und Bewertung** (luecken mit ganzen Zahlen [B] `antwort_bewerten`), solange der berichtigte Wert eine ganze Zahl ist.
- **Mehr Möglichkeiten**: Auswahl mit 4–5 statt 3 (25 % → 20 %).
- **Zwei Aufgaben je Lernziel, beide müssen stimmen** (heute schon so: bool_and je Etappe im Flugtest [B]). Eine 4er-Auswahl allein zu erraten: 25 %; zusammen mit einer Rechenaufgabe: 25 % × (Rate Rechnen ≈ 0) – das Raten hilft nur bei der V-Hälfte.
- **Nicht**: Abzüge für falsche Antworten (versteht ein Kind in Klasse 5 nicht, führt zu Lücken statt Antworten).

## 5. Rechnen und Verstehen je Lernziel getrennt nachweisen?

[M] **Ja, getrennt nachweisen – aber gemeinsam bestehen.**
- Flugtest: je Pflicht-Etappe eine R- und eine V-Aufgabe. Die Etappe ist „nachgewiesen“, wenn **beide** stimmen (das ist die heutige Regel bool_and – sie braucht dafür keine Änderung).
- Ergebnis zeigt getrennt: „Rechnen ✓ · Verstehen ✗“. Das ist für Kind und Eltern die eigentliche Information.
- **„Rechnen richtig, Verstehen falsch“** → Etappe „noch üben“ wie heute; die Korrektur stellt dann **eine neue V-Aufgabe** (nicht irgendeine). Umgekehrt (Verstehen richtig, Rechnen falsch) eine neue R-Aufgabe. Das braucht eine Serveränderung (`konzept.md`).
- **„Sitzt“** (Üben) und **„gesichert“** (Nachtest): Ein Lernziel gilt erst als gesichert, wenn in den drei Nachtest-Runden **mindestens einmal V und einmal R** richtig war. Bei „sitzt“ (Üben) mindestens eine gezählte V-Aufgabe, wenn die Lernkarte eine hat – Pflicht nur für Karten, die noch nicht gelandet sind (wie die Sachaufgaben-Pflicht, FT-S Regel 6), sonst entstehen rückwirkende Hürden.
- Langzeit (Mathe-Profi, `verhaeltnis.md` Z. 52: „nach 14 Tagen trägt nur, was verstanden ist“): im Nachtest mindestens die Hälfte V, in späteren Runden mehr.

## 6. Scheitern an der Form statt am Stoff verhindern

1. **Form-Bekanntheit**: Eine Form darf im Test nur vorkommen, wenn das Kind **diese Bauart** (nicht unbedingt diese Lernkarte) in der Übung schon mindestens zweimal bearbeitet hat, davon einmal richtig. Prüfbar über `schule.versuch` ⋈ `schule.aufgabe.form`. Sonst nimmt der Server eine V-Aufgabe in bekannter Form oder fällt auf R zurück.
2. **Alt-Etappen**: Etappen, die vor dem Einspielen der Formen gelandet sind (Klasse 5 vor 27.11. [B]), bekommen in Nachtests V nur in den Bauarten Umkehren/Zwei Wege/Anwenden (als `zahl`; sehen aus wie gewohnte Aufgaben) – keine Detektiv-/Auswahl-Bauart ohne Vorübung.
3. **Kurze, gleichbleibende Arbeitsanweisung** je Bauart (immer derselbe erste Satz, z. B. „Jemand hat gerechnet. In welcher Zeile steckt der erste Fehler, und was muss dort stehen?“).
4. **Keine Stufe 3** im Test.
5. Die erste V-Aufgabe in einem Flugtest steht nicht an erster Stelle (Einstieg mit Gewohntem).

## 7. Klasse 5 und Klasse 8

| | Klasse 5 | Klasse 8 |
|---|---|---|
| Geeignete V-Formen im Test | Umkehren, Zwei Wege (zahl), Brücke (Zahlenstrahl/Tabelle), Fehler-Detektiv mit 3 Zeilen gekoppelt | alle sechs; Fehler-Detektiv an Termumformungen, Verfahren wählen (Gleichungen, Funktionen), viele_antworten |
| Lesestoff | ein bis zwei Sätze; Sachaufgaben kurz | mehrteilig möglich |
| Anteil V im Test [M] | Hälfte, Nachtest nicht mehr | Hälfte, Nachtest bis zwei Drittel |
| Besonderheit | Testlänge zählt mehr (Ausdauer): Flugtest mit 1 R + 1 V verdoppelt die Länge – große Flüge (bis 14 Etappen [R]) werden mit 28 Karten lang; Unterbrechen geht schon heute („Angefangener Test – Weitermachen“, `lernen.js` 5150) | 2 Einheiten ohne jede Form im Üben (`funktionen.gebrochen`, `gleichungen.formeln` [R]) → dort zuerst Übungsformen, dann Test-V |

## 8. Fazit

[M] Prüfungstauglich ohne Einschränkung: **Umkehren, Zwei Wege (zahl), Anwenden (zahl), Brücke (zahl)**. Mit Kopplung/≥ 4 Möglichkeiten: **Fehler-Detektiv, Verfahren wählen, Brücke (Auswahl)**. Nur für Nachtest: **viele_antworten**. Nur Üben: **Lückenweg**.
