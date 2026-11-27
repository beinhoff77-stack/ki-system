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


## Berichtigungen nach der Inhaltsprüfung (Auftrag 20)

Stand 27.11.2026. Die Dateien `ge1.json`, `z2.json`, `ge2.json`, `a4.json` sind neu erzeugt (`bauen.py` endet mit „OK“, 76 Aufgaben, 65 Rechnungen zweifach nachgerechnet). Kennungen, Lernziele (`l`) und Teilfähigkeiten (`t`) sind unverändert; keine Aufgabe hinzugefügt oder gelöscht; die 20 `bedingung`-Aufgaben sind nicht angefasst.

| Kennung | Befund | was geändert (oder „bleibt, weil …“) |
|---|---|---|
| `Z2-07` | „kleinste Zahl in beiden Reihen“ lässt die 0 zu (0 steht in jeder Reihe). | Frage: „kleinste Zahl **über 0**“. Tipp: „Die 0 zählt hier nicht.“ Lösungsweg nennt die 0 ausdrücklich. Lösung 24 bleibt. |
| `GE1-06` | Die gesuchte 6 stand schon in Weg A („6 + 9“). | Weg A ohne Zahlen: „von C bis zur x-Achse zählen, dann von der x-Achse bis D“. Tipp fragt nach dem Abstand von C zur x-Achse. Lösungsweg rechnet beide Wege. Lösung 6 bleibt. |
| `GE1-13` | Stufe 3 zu hoch: ein Schritt („Tangente hat den Abstand r“), keine Kette. | Stufe 3 → 2, Typ `rueckwaerts` → `umkehr`. Text unverändert. |
| `GE2-12` | Stufe 3 zu hoch: ein Schritt (Mitte von 7 und −1). | Stufe 3 → 2, Typ `rueckwaerts` → `umkehr`. Text unverändert. |
| `A4-06` | Zwei Lückenwerte standen später ausgeschrieben in der Frage („② · x − 6 > 9“ verrät ① = 6; „−3x > ③“ verrät ② = −3). | Zwischenzeilen neu gefasst: „Bring alle x nach links und alle Zahlen nach rechts: ② · x > ③. Teilst du durch ②, dreht sich das Zeichen um: x < ④.“ Tipp und Lösungsweg angepasst. Werte (6, −3, 15, −5) bleiben. |

**Muster-Suche in dieser Runde (56 Aufgaben in `zahl`, `auswahl`, `luecken`):** Weitere Treffer gab es nicht.
(1) Unbeabsichtigte Lösung 0: keine. `Z2-08` hat 0 als gewollte Lösung (nur die 0 ist durch 2 und 5 teilbar). `Z2-09`, `Z2-10` haben je genau eine Ziffer.
(2) Falsche Auswahl-Antworten einzeln gegengelesen (`A4-03`, `-04`, `-05`, `-08`, `-11`, `-12`, `-14`; `GE1-03`, `-04`, `-05`, `-12`; `GE2-04`, `-05`, `-13`, `-14`; `Z2-04`, `-05`, `-13`): jede falsche Antwort ist falsch. Bei `GE1-05` ist „Trapez“ nach bayerischer Definition zwar auch wahr, die Frage verlangt aber „der genaueste Name“. Das bleibt so.
(3) Komma an einer Lücke: keine (Satzkommas bei `Z2-01`, `Z2-02` stehen mit Leerzeichen).
(4) Fehlende Modellvoraussetzung: keine; `A4-09` (Lastenaufzug) und `GE1-09` nennen alles Nötige.

**Neue automatische Prüfung in `bauen.py`:** Das Programm bricht ab, wenn im Fragetext oder in der Schablone einer Lückenaufgabe ein Komma ohne Leerzeichen an einem Lückenzeichen (① … ⑨, □) steht, etwa „0,②“ oder „①,②“. Satzkommas mit Leerzeichen („①, dann …“) sind erlaubt. Zusätzlich muss jede Lücke eine ganze Zahl sein. Die alten Fassungen von `G1-07`, `G8-01` und `G8-04` würden damit abbrechen (nachgestellt mit der Regel, nicht mit dem Programm selbst).
