# Postfach pruefung-neu-2 (Fünfundzwanzigste Runde, unabhängige Prüfung)

Neueste Meldung oben. Dieser Chat hat keines der geprüften Themen geschrieben.

## 2026-11-20 – zahlen.schranken (Schranken und Genauigkeit)

**Urteil: mit Korrekturen in Ordnung.**

### Umfang (Fakt)
- Gelesen: 5 Lernkarten (Einstieg, Wörter, Regel, Schritte, Bild, Fehler) und alle 180 Aufgaben (120 Übungen, 5 Test, 15 Korrektur, 30 Sicherung, 10 Knobel).
- Nachgerechnet: alle 180 Lösungen von Hand (Schranken, Summen/Differenzen, Produkte/Quotienten, Ja/Nein-Entscheidungen über den ungünstigsten Fall); bei Quotienten zusätzlich die Rundung auf zwei Stellen.
- Prüfskript nach der Änderung: OK, 0 Gruppen „gleich gebaut hintereinander“, Mengen unverändert (S1/S2/S3 je Lernkarte wie vorher, Test 5, Korrektur 15, Sicherung 30, Knobel 10).

### Änderungen je Fehlerart (29 Aufgaben)
- **a) falsche Lösung: 0.**
- **b) mehrdeutig: 18.** „Ist die Fahrt sicher erlaubt? / Passt der Schrank sicher? / Reicht das Brett sicher?“ hatte die Antworten „Ja / Nein / Das lässt sich nicht entscheiden.“ In allen Nein-Fällen liegt der wahre Wert beiderseits der Grenze – dann ist „lässt sich nicht entscheiden“ ebenso vertretbar wie „Nein“. Jetzt drei klare Zustände wie bei der Zug-Aufgabe: „Ja, sicher.“ / „Nicht sicher: im ungünstigsten Fall …“ / „Sicher nicht: … auf jeden Fall …“ (Letzteres ist bei den erzeugten Zahlen nie richtig, geprüft: untere Schranke liegt immer unter der Grenze). Betrifft Lernkarte entscheiden (11 Übungen, 1 Test, 2 Korrektur, 4 Sicherung).
- **c) späterer Stoff: 0.**
- **d) Lernkarten-Erklärung: 0.**
- **e) Tipp / Antwortoptionen: 10.**
  - 6× Tipp bei „untere Schranke der Geschwindigkeit“ bzw. „Wie breit ist es mindestens?“ lautete „Für das Maximum durch die kleinste Zahl teilen“ – führt bei einer Minimum-Frage in die falsche Richtung. Jetzt richtungsabhängig („Für das Minimum durch die größte Zahl teilen“).
  - 4× „Wie genau wurde gemessen?“ (3 Übungen, 1 Korrektur): Die falschen Optionen gehörten zu anderen Größen („auf 0,1 kg genau gewogen“ bei einer Zeitmessung) und waren allein an der Einheit auszuschließen. Jetzt in derselben Einheit mit echten Denkfehlern: halbe Breite (0,05 s), zehnfach, ein Zehntel. Lösungsweg ergänzt: „Die halbe Breite ist nur der größte Fehler.“
- **f) Stufe/Typ: 1.** grenzen, Stufe 3 transfer: „Wie viele Teilnehmer waren es mindestens?“ war nur die untere Schranke (Stufe-1-Gedanke). Jetzt: „Wie viele verschiedene Werte sind für die Zahl der Teilnehmer möglich?“ (Lösung 10, Fehlerbereich 885 ≤ n < 895). Typ und Stufe bleiben.

### Nebenwirkung (Fakt)
- Beim Neuerzeugen übernimmt die Datei das Feld `klasse` aus `themenliste.json`: vorher `{"zusatz": 10}`, jetzt `{"ib_myp": 5}`. Die alte Datei war gegenüber der Themenliste veraltet; ich habe das nicht zurückgedreht.

### Nicht geändert, zur Kenntnis (Meinung)
- „höchstens/mindestens“ wird für die nicht angenommene obere Schranke verwendet (z. B. dritte Dreiecksseite „höchstens 13,5 cm“). Das ist die übliche IB/GCSE-Konvention und in der Lernkarte so eingeführt; mathematisch streng wäre „kleiner als“. Belassen.
- Knobel entscheiden „Ja, weil 12 + 27 = 39 t“ hat das richtige Ja mit unzureichender Begründung; die richtige Option ist klar besser begründet. Belassen.

### Lehrplan
- Annahme: Passt zu IB MYP Jahr 5 (Klasse 10), Extended Mathematics. Das offizielle IB-Fachdokument („MYP mathematics guide“) ist nicht frei abrufbar; Sekundärquelle RevisionDojo nennt „bounds“ als üblichen Extended-Inhalt (revisiondojo.com/blog/what-topics-are-in-myp-extended-mathematics, abgerufen 20.11.2026). Kein bayerischer Lehrplanbezug (Datei vermerkt „ohne Lehrplan-Zuordnung“). Wesentliches fehlt nicht; Schranken bei negativen Größen sind bewusst ausgelassen (unter `offen` vermerkt).

### Nicht geprüft
- Darstellung der Bilder in der App (nur die JSON-Angaben gelesen).
