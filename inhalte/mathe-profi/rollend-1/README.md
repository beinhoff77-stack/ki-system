# Rollendes System, Stufe 1 – neue Aufgaben für die nächsten vier Flüge

Mathe-Profi, 26.11.2026 (Auftrag 14, Teil C und D). Erzeugt von `bauen.py`, Lauf „OK“. **Nichts eingespielt.** Keine Namen, keine Lerndaten; keine Aufgabe aus Schulbuch oder Prüfung übernommen.

| Datei | Flug | für | Klasse | ohne Bau | Typ „bedingung“ |
|---|---|---|---|---|---|
| `ge1.json` | Formen und Grundbegriffe | Kind 1 | 5 | 14 | 5 |
| `z2.json` | Teilbarkeit | Kind 1 | 5 | 14 | 5 |
| `ge2.json` | Spiegeln und Symmetrie | Kind 2 | 7 | 14 | 5 |
| `a4.json` | Lineare Ungleichungen | Kind 2 | 8 | 14 | 5 |

Zusammen 76 Aufgaben: 56 in den Antwortformen `zahl`, `auswahl`, `luecken` und 20 des neuen Typs `bedingung`.

## Aufbau einer Datei

Je Aufgabe ein Eintrag mit Zusatzangaben und unter `aufgabe` der Aufgabe im Format von `inhalte/README.md`:

- `kennung` – z. B. `GE1-07`, bei „bedingung“ `GE1-B3`.
- `regel` – Kennung aus `regeln-uebersicht/kennungen.json` (Rechenregel `rr.…` oder tragende Idee `id.…`).
- `fehlbilder` – je falscher Antwort: die Antwort, eine Beschreibung und, **nur wo sicher**, eine Fehlbild-Kennung. Ohne Kennung heißt: Die Antwort ist als typisch falsch bekannt, passt aber zu keinem Fehlbild der Liste. Nichts wurde passend gemacht.
- `typ` – Lückenweg, Fehler-Detektiv, Verfahren wählen, Zwei Wege vergleichen, Umkehren, Anwenden, Viele richtige Antworten.
- `zaehlt` – Vorschlag wie in Schritt 1: `nein` (Lückenweg mit voller Hilfe), `folge` (halbe Hilfe), `ja`.
- Reihenfolge: erst die Aufgaben ohne Bau, dann die des Typs „bedingung“, jeweils Stufe 1 → 3.

## Geprüft [G]

- Jede Rechenaufgabe zweifach: Feld `c` mit dem Rechner aus `tools/inhalt_pruefen.py` und ein zweiter, anders gebauter Weg (65 Rechnungen).
- Jede Auswahl-Aufgabe mit einer Probe; die richtige Antwort steht bei den Aufgaben mit vier Antworten an allen vier Stellen.
- Jedes Fehlbild ergibt eine andere Antwort als die Lösung; jede verwendete Kennung gibt es in `kennungen.json`.
- Jede „bedingung“-Aufgabe: `pruefe_aufgabe` aus `tools/bedingung.py` liefert eine leere Fehlerliste; zu jeder Bedingung mindestens ein Gegenbeispiel; Beispiel und weitere gute Antworten werden als richtig bewertet (auch mit typografischem Minus und Komma eingegeben).
- Alle Aufgaben an eine Kopie ihrer Themen-Datei gehängt: `tools/inhalt_pruefen.py` ohne Fehler (vorher und nachher). Kein Aufgabentext kommt im Bestand schon vor.
- Stufe und Gedanke (`s`, `g`) passen zusammen.

## Was die 20 „bedingung“-Aufgaben von der Sprache brauchen

`und`, `oder`, `nicht`, `teilbar`, `betrag`, `neg`, `anzahl_negativ`, `hoch`, `verschieden`, `summe`. **Sieben davon** (`und`, `oder`, `nicht`, `teilbar`, `betrag`, `neg`, `anzahl_negativ`) sind laut `bedingung-format.md` vom Vergleich Referenz gegen Datenbank noch nicht erfasst. Diese Aufgaben taugen deshalb zugleich als Prüf-Fälle dafür.

Eine Grenze der Sprache ist mir begegnet: „Ist eine Primzahl“ gibt es nicht. In `Z2-B5` steht dafür eine Liste der zehn Primzahlen unter 30 (verschachteltes `oder`, weil es höchstens sechs Glieder nimmt). Das trägt nur, weil die Summe 30 größere Zahlen ausschließt.

## Teil D – Hinweistexte in `tools/tests/bedingung_faelle.json` gegengelesen

Geprüft: Ist jeder Hinweis fachlich richtig, und verrät er die Lösung? Zehn Aufgaben für Kinder (die elfte ist ein Lastfall). **Alle Hinweise sind fachlich richtig.** Vier Änderungen schlage ich vor – als Liste, die Datei ist unverändert:

| Aufgabe | Stelle | Befund | Vorschlag |
|---|---|---|---|
| 3 „a · x + b = 3x − 6 hat keine Lösung“ | Name der Bedingung „x fällt weg“ | **Verrät den Lösungsgedanken.** Der Name wird nach dem ersten Fehlversuch gezeigt; damit steht da, was zu tun ist. | Name „nicht genau eine Lösung“; Hinweis: „Mit deinem a hat die Gleichung genau eine Lösung.“ |
| 3 | Name „es bleibt eine falsche Aussage“ | Verrät den zweiten Lösungsgedanken. Der Hinweis selbst ist richtig – er stimmt aber nur, weil die Bedingung davor a = 3 schon gesichert hat. | Name „nicht jede Zahl ist Lösung“; Hinweis: „Mit deinem b ist jede Zahl eine Lösung.“ |
| 1 „drei Zahlen, Summe 0, genau eine positiv“ | Hinweis „Bei dir sind {} Zahlen positiv.“ | Richtig; bei 0 liest es sich holprig, bei 1 kommt er nie. | „Positiv sind bei dir: {}.“ |
| 8 „Mittelwert 0, Median 1, Abstand 10“ | Hinweis „Dein Abstand ist {}.“ | Richtig, aber „Abstand“ ohne Bezug. | „Zwischen deiner kleinsten und größten Zahl liegen {}.“ |

Ohne Änderung: Aufgaben 2, 4, 5, 6, 7, 9, 10. Die Hinweise nennen dort nur den Wert, den das Kind selbst erzeugt hat („Deine Summe ist …“) – das verrät nichts.
Eine Beobachtung, kein Fehler: In Aufgabe 4 (Bruchterm negativ) nennt der Hinweis zu „Term ist definiert“ die verbotene Stelle x = 2. Das ist dort richtig, weil das Kind sie selbst eingegeben hat.

## Nachtrag 27.11.2026 (Auftrag 18)

- Alle 20 „bedingung“-Aufgaben bestehen `pruefe_aufgabe` aus dem aktuellen `tools/bedingung.py`.
- Sechs Namen von Bedingungen in `GE2-B1`, `GE2-B4`, `GE2-B5` nennen jetzt die Forderung statt des Wegs (Liste in `rollend-2/README.md`, Abschnitt 2). Prüf-Bäume und Hinweise sind unverändert.

## Nicht geprüft

- Keine Aufgabe ist von einem Kind gerechnet worden; Stufen und Zählvorschläge sind Einschätzungen.
- Die „bedingung“-Aufgaben laufen nur gegen die Python-Referenz, nicht gegen die Datenbank-Fassung.
- Ob der Bestand eine inhaltlich gleiche Aufgabe mit anderen Worten enthält: Geprüft ist nur der wörtlich gleiche Text.
- Bedienung von vier Eingabefeldern am Handy (vier Aufgaben haben vier Felder).
- Fehlbilder: aus meiner Fachkenntnis angesetzt, nicht aus den Antworten der Kinder belegt.

## Annahmen

- Aufgaben ohne Grafik, weil „ohne Bau“; Koordinaten und Achsen stehen im Text.
- Die Themen der Flüge wie in `lehrplan-kinder/plan.py`: ge1 = `geometrie.grundbegriffe`, `geometrie.ortslinien`; z2 = `zahlen.teilbarkeit`; ge2 = `abbildungen.kongruenz`; a4 = `gleichungen.ungleichungen`, `zahlen.intervalle`.
- In ge2 sind die zwei Vektor-Lernkarten der Realschule (`vektor_koordinaten`, `vektor_drehen`) ausgelassen.

## Auftrag 20 – Berichtigungen nach der Inhaltsprüfung (27.11.2026)

Alle Änderungen über `bauen.py`, Lauf endet mit „OK“. **Die Kennungen sind unverändert geblieben.** Die Ausgabe wird jetzt stabil nach Stufe sortiert (`sorted(..., key=stufe)`), damit eine Stufen-Änderung die Nummerierung nicht verschiebt.

| Kennung | Befund | Was geändert |
|---|---|---|
| Z2-07 | „kleinste Zahl in beiden Reihen“ lässt die 0 zu | **geändert:** „kleinste Zahl **größer als 0**“; Tipp „Achterreihe **ab der 8**“; Lösungsweg nennt die Ausnahme. Lösung bleibt 24. Neues Fehlbild: Antwort 0. |
| GE1-06 | die gesuchte 6 stand schon in Weg A | **geändert:** Weg A wird nur noch beschrieben („zerlegt die Strecke an der x-Achse“), gefragt ist jetzt die **Länge 15**. Fehlbilder neu: 3 (Minus stehen gelassen), −15. |
| GE1-13 | Stufe 3 zu hoch | **geändert:** Stufe 2, Typ `umkehr` statt `rueckwaerts`. Es ist ein Schritt (Abstand = r), keine Kette rückwärts. |
| GE2-12 | Stufe 3 zu hoch | **geändert:** Stufe 2, Typ `umkehr`. Die Achse ist die Mitte – ein Schritt. |
| A4-06 | zwei Lückenwerte standen später ausgeschrieben in der Frage | **geändert:** Die Folgezeilen nennen die Zahlen nicht mehr, sondern verweisen auf die Lücken: „② · x − ① > 9. Plus ①: ② · x > ③. Geteilt durch ②“. Werte unverändert. |

**Neue Prüfung in `bauen.py`** (in allen drei Runden): Eine Lücke darf nicht unmittelbar hinter einem Komma stehen. Sonst wäre sie eine Ziffernfolge, die App vergleicht aber ganze Zahlen. In Runde 1 gab es keinen solchen Fall.
