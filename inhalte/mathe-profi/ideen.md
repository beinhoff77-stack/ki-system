# Mathe-Profi – Ideen-Sammlung (Stand 25.11.2026)

Zweck: Grundlage für die Besprechung, was umgesetzt wird. Nichts davon ist beauftragt.
Kennzeichnung: **Lerngewinn** und **Aufwand** sind Einschätzungen (Meinung). „Prüfung“ beschreibt, was gespeichert wird und womit der Server vergleicht – jede Idee hier ist automatisch prüfbar, außer wo „nicht automatisch“ steht.
Ausgearbeitet (mit Datensätzen, Prüfregeln, Entwurf) sind bisher nur die Formen F1–F5, siehe `auftrag1.md` Teil D und `entwurf-formen.html`.

Korrektur zu meiner Chat-Nachricht vom 24.11.: Das Beispiel „Bilde aus 3, 5, 7, 8 die Zahl 100“ hat **keine** Lösung (per Programm alle Terme mit +, −, ·, : und Klammern geprüft). Unten steht ein geprüftes Beispiel.

---

## Übersicht

| Nr | Idee | Gruppe | Lerngewinn | Aufwand | Braucht |
|---|---|---|---|---|---|
| F1 | Felder antippen | Form | hoch | klein | – |
| F2 | Schieber (Zahlenstrahl, Parameter) | Form | hoch | klein–mittel | – |
| F3 | Punkte im Gitter setzen | Form | sehr hoch (Kl. 6–10) | mittel | – |
| F4 | Paare zuordnen | Form | mittel | mittel | – |
| F5 | Rechenweg aus Bausteinen | Form | mittel–niedrig | mittel | – |
| F6 | Bereich markieren (zwei Schieber) | Form | mittel | klein | F2 |
| F7 | Wertetabelle, Graph wächst mit | Form | hoch (Kl. 7–9) | mittel | F3 |
| A1 | Mach 100 – Rechenrätsel | Aufgabenart | hoch | mittel | Term-Rechner |
| A2 | Aufgabe umdrehen – selbst erfinden | Aufgabenart | sehr hoch | mittel | Term-Rechner |
| A3 | Gegenbeispiel finden | Aufgabenart | hoch | klein–mittel | Prüf-Regeln |
| A4 | Muster fortsetzen und vorhersagen | Aufgabenart | hoch | klein–mittel | F1 oder `zahl` |
| A5 | Korrigiere das Heft | Aufgabenart | hoch | klein | geht heute |
| A6 | Faulster Weg gesucht | Aufgabenart | mittel | klein | geht heute |
| A7 | Zahlen-Steckbrief | Aufgabenart | mittel | klein | geht heute |
| A8 | Erst schätzen, dann rechnen | Aufgabenart | hoch | klein | F2 |
| R1 | Fehler sichtbar machen | Rückmeldung | sehr hoch | mittel | – |
| R2 | Tipp-Treppe | Rückmeldung | mittel | klein | – |
| R3 | Die eigenen Fehler kommen zurück | Rückmeldung | hoch | klein | Fehlerdaten (vorhanden) |
| R4 | Sicherheits-Wette | Rückmeldung | mittel–hoch | klein | – |
| M1 | Aufgaben aus der echten Reise | Motivation | mittel | laufend | Pflege |
| M2 | Knobel der Woche für beide | Motivation | mittel | klein | – |
| M3 | Rechenweg-Foto | Lehrer | hoch | groß | nicht automatisch |

Meine Reihenfolge für die Umsetzung (Meinung): **R1, F1, R3, A5, F2 + A8, R4, F3, A3, A1 + A2** (Term-Rechner einmal bauen, zwei Ideen nutzen), dann der Rest.

---

## F – Neue Aufgabenformen (das Kind tut etwas im Bild)

### F1 Felder antippen
Kind tippt Felder an: Zahlen in einem Term, Zeilen einer Rechnung, Kästchen eines Bruchstreifens.
Beispiel: „Rechne 4 · 17 · 25 · 3 geschickt. Tippe die zwei Faktoren an, die du zuerst malnimmst.“ → 4 und 25.
Lernt: Struktur sehen statt ausrechnen. Prüft endlich den Weg bei „geschickt rechnen“.
Prüfung: `{menge:[…]}` gleich Lösungsmenge; oder nur Anzahl (Einfärben: „Färbe ¾ von 8 Feldern“ → 6 beliebige).
Ausgearbeitet: `auftrag1.md` D1.

### F2 Schieber
Kind setzt einen Pfeil auf dem Zahlenstrahl oder stellt einen Parameter ein; beim Parameter dreht sich der Graph mit.
Beispiel: „Wo liegt ungefähr 487 · 21?“ (Strahl 0–20 000, richtig 8 000–12 000).
Lernt: Größenvorstellung, Wirkung eines Parameters.
Prüfung: `{wert}` im Bereich oder mit Toleranz. Ausgearbeitet: D2.

### F3 Punkte im Gitter setzen
Kind tippt Gitterpunkte; bei zwei Punkten zieht die App die Gerade.
Beispiel: „Zeichne y = −⅔x + 2.“ Jede zwei Gitterpunkte der Geraden zählen.
Auch: Spiegeln, Verschieben, Drehen von Figuren; Schnittpunkt antippen.
Prüfung: Punkte gleich / in Reihenfolge / auf der Geraden. Ausgearbeitet: D3.

### F4 Paare zuordnen
Kind tippt links, dann rechts.
Beispiel: Geradenpaar → parallel / senkrecht / identisch / schneiden (5 Paare, 4 Ziele – kein Rest durch Ausschluss).
Auch: Graph ↔ Gleichung, Term ↔ Name, Bruch ↔ Dezimalzahl ↔ Prozent.
Prüfung: `{paare:[…]}` exakt. Ausgearbeitet: D4.

### F5 Rechenweg aus Bausteinen
Kind legt Schritte in Reihenfolge, mit Ablenkern.
Beispiel: Rückwärtsrechnen „·4, −30, :2 ergibt 25“ → ·2, +30, :4.
Ehrlich: Ordnen ist leichter als selbst finden. Nur Stufe 1–2, nicht für Tests. Ausgearbeitet: D5.

### F6 Bereich markieren
Zwei Schieber auf einem Zahlenstrahl: Kind markiert, **für welche Zahlen** etwas stimmt.
Beispiel (Kl. 8, Ungleichungen): „Für welche x gilt 2x − 3 < 5?“ → alles links von 4, Rand offen.
Beispiel (Kl. 5): „Welche Zahlen runden auf 3 500?“ → 3 450 bis 3 549.
Lernt: Lösungen sind oft ein Bereich, nicht eine Zahl.
Prüfung: `{von, bis, rand_links, rand_rechts}`; Grenzen exakt (Raster), Ränder offen/geschlossen als Antippen eines Kreises.
Aufwand: klein, sobald F2 steht.

### F7 Wertetabelle, Graph wächst mit
Kind füllt eine Wertetabelle; jeder richtige Wert erscheint sofort als Punkt im Gitter. Zum Schluss sieht es die Gerade oder Kurve entstehen.
Beispiel: y = x² − 2 für x = −2 … 2 → 2, −1, −2, −1, 2 und die Parabel wird sichtbar.
Lernt: Tabelle und Graph sind dasselbe. Wichtig für Funktionen Kl. 7–9.
Prüfung: `{werte:[…]}` wie heute `luecken`; Bild ist nur Anzeige. Aufwand mittel (Zeichnen in F3 wiederverwenden).

---

## A – Neue Aufgabenarten (mit vorhandenen oder neuen Formen)

### A1 Mach 100 – Rechenrätsel mit offenem Weg
„Bilde aus 3, 4, 5 und 8 einen Term, der 100 ergibt. Jede Zahl genau einmal.“
Lösungen u. a. (3 · 4 + 8) · 5 und (3 · 8 − 4) · 5 (per Programm geprüft).
Lernt: Rechenregeln aktiv anwenden, Klammern gezielt setzen; mehrere Wege, macht Spaß.
Prüfung: Kind baut den Term aus Karten; Server rechnet ihn aus: Ergebnis = 100 und jede Karte genau einmal.
Aufwand: mittel – der Server muss einen Term sicher ausrechnen können (Term-Rechner, eigener kleiner Rechner, kein `eval`).

### A2 Aufgabe umdrehen – das Kind erfindet
„Schreib eine Gleichung, deren Lösung x = 3 ist.“ · „Gib eine Gerade an, die durch (2 | 5) geht.“ · „Nenne einen Bruch zwischen ⅓ und ½.“
Lernt: Wer selbst baut, muss verstehen. Abschreiben unmöglich, jede richtige Erfindung zählt.
Prüfung: Server setzt ein (x = 3 erfüllt die Gleichung? Punkt auf der Geraden? Bruch im Bereich?). Billige Antworten wie „x = 3“ selbst werden abgewiesen (Regel: x muss auf beiden Seiten oder mit Rechenzeichen vorkommen).
Aufwand: mittel, gleicher Term-Rechner wie A1.

### A3 Gegenbeispiel finden
„Stimmt: Jede Zahl, die durch 4 teilbar ist, ist auch durch 8 teilbar? Wenn nein, gib ein Gegenbeispiel.“ → z. B. 12.
Auch: „Ein Viereck mit vier gleich langen Seiten ist ein Quadrat?“ (Raute als Gegenbeispiel, mit F3 zeichnen).
Lernt: Wie man eine Behauptung widerlegt – das Kernstück von „Begründen“.
Prüfung: Server prüft eine Bedingung, z. B. „durch 4 teilbar und nicht durch 8“. Jede passende Zahl zählt.
Aufwand: klein–mittel (je Aufgabe eine einfache Bedingung).

### A4 Muster fortsetzen und vorhersagen
Streichholz-Figuren: 4, 7, 10 Hölzer. Kind baut zuerst Figur 4 (F1: Hölzer antippen), dann: „Wie viele Hölzer braucht Figur 100?“ → 301. Zum Schluss als Term: 3n + 1.
Lernt: der natürlichste Weg von Klasse 5 zur Algebra.
Prüfung: `zahl`, optional Term als Lücke.

### A5 Korrigiere das Heft
Fertige Lösung eines erfundenen Mitschülers mit einem versteckten Fehler. Kind tippt die falsche Zeile an und trägt die richtige Zahl ein.
Beispiel: 2 976 : 12 – Fehler in Zeile 2 (57 − 48 = 7 statt 9), richtig 248.
Lernt: prüfen statt nur rechnen – genau das, was in der Schulaufgabe Punkte rettet.
Prüfung: Zeile (`auswahl`) + Zahl. Geht heute schon mit `tabelle` + `auswahl`, schöner mit F1.

### A6 Faulster Weg gesucht
„Drei Kinder rechnen 36 · 25. Wer ist am schnellsten fertig?“
A: 36 · 25 schriftlich · B: 9 · 4 · 25 = 9 · 100 · C: 30 · 25 + 6 · 25 → B.
Danach: „Rechne 44 · 25 auf diesem Weg“ → 1 100.
Lernt: Wege vergleichen, Abkürzungen wählen.
Prüfung: `auswahl` + `zahl`. Geht heute.

### A7 Zahlen-Steckbrief
„Ich bin zweistellig und kleiner als 50, durch 3 und 4 teilbar, meine Quersumme ist 12. Wer bin ich?“ → 48 (per Programm geprüft: ohne „kleiner als 50“ passt auch 84 – genau solche Doppel-Lösungen muss die Prüfung vor Freigabe finden).
Lernt: Eigenschaften kombinieren, systematisch ausschließen.
Prüfung: `zahl`. Geht heute. Lösung muss eindeutig sein (vor Freigabe per Programm prüfen).

### A8 Erst schätzen, dann rechnen
Vor einer schweren Rechenaufgabe kommt zuerst „Wo liegt das ungefähr?“ (F2), dann die genaue Rechnung. In der Rückmeldung stehen Schätzung und Ergebnis nebeneinander.
Lernt: Plausibilität – fängt den häufigsten Fehler (Stelle vergessen, Komma verrutscht).
Prüfung: zwei Schritte, beide wie bisher.

---

## R – Rückmeldung und Ablauf

### R1 Fehler sichtbar machen
Bei falscher Antwort zeichnet die App, **was die Antwort des Kindes bedeuten würde**:
- Kind sagt Steigung 2 statt −2 → die App zeichnet seine Gerade neben der richtigen; sie steigt statt zu fallen.
- Kind sagt 1 022 statt 10 227 → Pfeil auf dem Zahlenstrahl, weit weg vom Überschlag.
- Kind sagt bei ¾ von 8 = 3 → Bruchstreifen mit 3 von 8 gefärbten Teilen – sichtbar weniger als drei Viertel.
Lernt: Das Kind sieht selbst, warum es falsch ist, statt eine Regel zu lesen.
Prüfung: unverändert; nur die Anzeige danach. Aufwand mittel (je Thema eine Zeichen-Regel, aber nur für die häufigsten Fehler).
Meinung: der größte Hebel ohne neue Antwortform.

### R2 Tipp-Treppe
Statt einem Tipp drei Stufen: 1. Frage („Was kommt zuerst?“) · 2. Bild · 3. erster Schritt vorgerechnet. Jede Stufe kostet etwas von den Sternen.
Lernt: Selbst weiterkommen mit so wenig Hilfe wie nötig.
Aufwand: klein für die App, mittel für die Inhalte (zwei weitere Tipps je Aufgabe – nur für Stufe 2–3 nötig).

### R3 Die eigenen Fehler kommen zurück
In der Wiederholung kommt ein alter Fehler des Kindes: „Vor einer Woche hast du hier 698 geschrieben. Was war falsch?“ – drei Erklärungen zur Auswahl, dann die Aufgabe neu.
Lernt: aus dem eigenen Fehler, nicht aus einem fremden.
Prüfung: `auswahl`. Die falschen Antworten samt Fehlermuster sind schon in der Datenbank.

### R4 Sicherheits-Wette
Vor dem Abschicken: „sicher / ziemlich sicher / geraten“. Richtig + sicher = Bonus-Sterne.
Lernt: ehrliche Selbsteinschätzung; Raten lohnt sich nicht mehr.
Wichtig: **nur Bonus, kein Abzug** – Minuspunkte wurden am 17.11. bewusst abgeschafft. Nebennutzen: Der Lehrer sieht, wo ein Kind sicher, aber falsch ist (das sind die gefährlichen Lücken).

---

## M – Motivation und Lehrer

### M1 Aufgaben aus der echten Reise
Die Etappe ist eine Stadt – also echte Zahlen von dort: Entfernung zur nächsten Etappe, Eintrittspreise, Temperatur, Wechselkurs (Kurs steht in der Aufgabe).
Lernt: Mathe gehört zum eigenen Leben.
Ehrlich: Die Zahlen müssen gepflegt werden. Realistisch 2–3 Karten je Stadt, nicht mehr.

### M2 Knobel der Woche für beide
Ein Rätsel pro Woche in zwei Stufen (Kl. 5 und Kl. 8), gleiche Idee, gleiche Sterne – beide Kinder können gleich viel erreichen.
Beispiel: A1 „Mach 100“ mit vier Karten (leicht) bzw. mit Brüchen oder Potenzen (schwer).
Lernt: Ausdauer, Spaß am Knobeln; Gesprächsstoff zwischen den Kindern.

### M3 Rechenweg-Foto (nicht automatisch)
Kind rechnet eine Schulaufgaben-Aufgabe auf Papier, Foto in die App, Korrektur durch KI oder Lehrer im Lehrer-Bereich.
Lernt: sauberer Rechenweg – zählt in der Schulaufgabe.
Ehrlich: nicht vom Server prüfbar, großer Aufwand, Datenschutz (Fotos). Eher für den großen Test je Ort, nicht für Bordkarten.

---

## Bewusst verworfen (sieht gut aus, bringt wenig)

- **Waage für Gleichungen:** bricht ab negativen Zahlen und Brüchen zusammen; höchstens Klasse 5–6.
- **Erklärvideos / lange Animationen:** teuer, Kind schaut nur zu; widerspricht der Vorgabe „keine Videos“.
- **Freies Zeichnen mit dem Finger:** nicht sauber prüfbar.
- **Zeitdruck / Kopfrechen-Sprint:** Zeitbegrenzung ist nicht gewollt; fördert Raten.
- **Punkte für Menge (Karten zählen):** belohnt Abarbeiten statt Verstehen.

---

## Zur Besprechung

1. Welche Gruppe zuerst: Formen (F), Aufgabenarten (A) oder Rückmeldung (R)?
2. Term-Rechner auf dem Server bauen (trägt A1, A2, teils A3)?
3. Sicherheits-Wette ja/nein – und nur Bonus?
4. Reise-Aufgaben (M1): Wer pflegt die Zahlen?
