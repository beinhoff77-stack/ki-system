# Schritt 1: neue Aufgaben ohne Bau (Auftrag 7)

Mathe-Profi, 26.11.2026. Stand `lernen-app` bd2b2391. **Nichts ist eingespielt.** Nur die heutigen Antwortformen `zahl`, `auswahl`, `luecken`.
**[G]** gesichert · **[A]** Annahme · **[M]** Meinung.

## Dateien

| Datei | Inhalt |
|---|---|
| `zahlen.rechengesetze.neu.json`, `zahlen.ganz.neu.json`, `terme.potenzgesetze_ganzzahlig.neu.json`, `gleichungen.bruch.neu.json` | je 13 Aufgaben im Format von `inhalte/README.md`, ohne Zusatzfelder; zum Anhängen an `aufgaben` der Themen-Datei |
| `etiketten.json` | je Aufgabe: Kennung, Typ der Auswahl, Grundregel (Nummer und Name), je falscher Antwort Fehlbild mit Regel, Zählvorschlag |
| `bauen.py` | Quelle aller Aufgaben; rechnet nach, schreibt die Dateien, lässt `tools/inhalt_pruefen.py` laufen. Aufruf: `python3 -I inhalte/mathe-profi/schritt1/bauen.py` → „OK“ |

## Themenwahl

Je Kind die zwei Themen mit den meisten Versuchen der letzten Lerntage (nur Summen gelesen, nichts davon hier):
Klasse 5 `zahlen.rechengesetze` und `zahlen.ganz`; Klasse 8 `terme.potenzgesetze_ganzzahlig` und `gleichungen.bruch`.

## Was geprüft ist [G]

- 52 Aufgaben, jede auf zwei Wegen nachgerechnet: Feld `c` mit dem Rechner aus `tools/inhalt_pruefen.py`, dazu ein zweiter, anders gebauter Ausdruck; bei Termen und Gleichungen zusätzlich eine Probe durch Einsetzen.
- 145 Fehlbilder. Jedes ist als Rechnung hinterlegt; das Skript prüft, dass es eine andere Zahl ergibt als die Lösung und als die anderen Fehlbilder derselben Lücke.
- `tools/inhalt_pruefen.py` über jede Themen-Datei mit angehängten Aufgaben: Code 0, keine Fehler, „gleich gebaut hintereinander“ bleibt 0.
- Kein Tipp enthält das Ergebnis (bei `zahl` vom Skript geprüft); kein Fragetext kommt im Thema schon vor; die richtige Auswahl-Antwort steht an wechselnder Stelle.

## Die Aufgaben

**Klasse 5 · `zahlen.rechengesetze`**

| Kennung | Typ | Lernkarte | Stufe · `g` | Form | Grundregel | Fehlbilder | zählt für „gelandet“ |
|---|---|---|---|---|---|---|---|
| RG-01 | Lückenweg | `mal_ganz` | 1 · `direkt` | `luecken` | 3 Rangfolge | 5 | **nein** |
| RG-02 | Lückenweg | `mal_ganz` | 2 · `mehrschritt` | `luecken` | 2 Zeichen-Paar | 3 | nur Folge |
| RG-03 | Lückenweg | `geteilt_ganz` | 2 · `mehrschritt` | `luecken` | 2 Zeichen-Paar | 3 | nur Folge |
| RG-04 | Brücke: Zahl, aber nicht ausrechnen | `klammern` | 2 · `darstellung` | `luecken` | 5 Minusklammer | 2 | ja |
| RG-05 | Brücke: Zahl, aber nicht ausrechnen | `verteilen` | 2 · `darstellung` | `luecken` | 4 Verteilen | 3 | ja |
| RG-06 | Zwei Wege vergleichen | `verteilen` | 2 · `mehrschritt` | `zahl` | 4 Verteilen | 2 | ja |
| RG-07 | Zwei Wege vergleichen | `klammern` | 2 · `mehrschritt` | `zahl` | 5 Minusklammer | 2 | ja |
| RG-08 | Fehler-Detektiv (einfache Form) | `klammern` | 3 · `fehler` | `auswahl` | 3 Rangfolge | 3 | ja |
| RG-09 | Fehler-Detektiv (einfache Form) | `mal_ganz` | 3 · `fehler` | `zahl` | 2 Zeichen-Paar | 2 | ja |
| RG-10 | Verfahren wählen (einfache Form) | `kopfrechnen` | 1 · `erkennen` | `auswahl` | 6 Tauschen und Bündeln | 3 | ja |
| RG-11 | Verfahren wählen (einfache Form) | `verteilen` | 1 · `erkennen` | `auswahl` | 4 Verteilen | 3 | ja |
| RG-12 | Brücke: Zahl, aber nicht ausrechnen | `vorteil` | 2 · `darstellung` | `luecken` | 6 Tauschen und Bündeln | 3 | ja |
| RG-13 | Lückenweg | `klammern` | 1 · `direkt` | `luecken` | 5 Minusklammer | 2 | **nein** |

**Klasse 5 · `zahlen.ganz`**

| Kennung | Typ | Lernkarte | Stufe · `g` | Form | Grundregel | Fehlbilder | zählt für „gelandet“ |
|---|---|---|---|---|---|---|---|
| GZ-01 | Lückenweg | `subtrahieren` | 1 · `direkt` | `luecken` | 1 Richtung | 3 | **nein** |
| GZ-02 | Lückenweg | `ketten` | 1 · `direkt` | `luecken` | 1 Richtung | 4 | **nein** |
| GZ-03 | Lückenweg | `ketten` | 2 · `mehrschritt` | `luecken` | 1 Richtung | 3 | nur Folge |
| GZ-04 | Lückenweg | `ketten` | 2 · `mehrschritt` | `luecken` | 1 Richtung | 4 | nur Folge |
| GZ-05 | Brücke: Zahl, aber nicht ausrechnen | `subtrahieren` | 2 · `darstellung` | `luecken` | 1 Richtung | 2 | ja |
| GZ-06 | Brücke: Zahl, aber nicht ausrechnen | `addieren` | 2 · `darstellung` | `luecken` | 1 Richtung | 2 | ja |
| GZ-07 | Zwei Wege vergleichen | `ketten` | 2 · `umkehr` | `zahl` | 6 Tauschen und Bündeln | 3 | ja |
| GZ-08 | Zwei Wege vergleichen | `subtrahieren` | 2 · `darstellung` | `zahl` | 1 Richtung | 2 | ja |
| GZ-09 | Fehler-Detektiv (einfache Form) | `ketten` | 3 · `fehler` | `auswahl` | 1 Richtung | 3 | ja |
| GZ-10 | Fehler-Detektiv (einfache Form) | `subtrahieren` | 3 · `fehler` | `zahl` | 1 Richtung | 2 | ja |
| GZ-11 | Verfahren wählen (einfache Form) | `ketten` | 1 · `erkennen` | `auswahl` | 6 Tauschen und Bündeln | 3 | ja |
| GZ-12 | Verfahren wählen (einfache Form) | `umkehraufgabe` | 1 · `erkennen` | `auswahl` | 8 Umkehren | 3 | ja |
| GZ-13 | Brücke: Zahl, aber nicht ausrechnen | `verstehen` | 3 · `begruenden` | `auswahl` | 1 Richtung | 3 | ja |

**Klasse 8 · `terme.potenzgesetze_ganzzahlig`**

| Kennung | Typ | Lernkarte | Stufe · `g` | Form | Grundregel | Fehlbilder | zählt für „gelandet“ |
|---|---|---|---|---|---|---|---|
| PG-01 | Brücke: Zahl, aber nicht ausrechnen | `gleiche_basis_ganz` | 2 · `darstellung` | `luecken` | 12 Potenz | 3 | ja |
| PG-02 | Brücke: Zahl, aber nicht ausrechnen | `exponent_und_potenz` | 2 · `darstellung` | `luecken` | 12 Potenz | 3 | ja |
| PG-03 | Lückenweg | `terme_vereinfachen` | 1 · `direkt` | `luecken` | 12 Potenz | 4 | **nein** |
| PG-04 | Lückenweg | `terme_vereinfachen` | 2 · `mehrschritt` | `luecken` | 12 Potenz | 3 | nur Folge |
| PG-05 | Lückenweg | `gleiche_basis_ganz` | 2 · `mehrschritt` | `luecken` | 12 Potenz | 3 | nur Folge |
| PG-06 | Zwei Wege vergleichen | `gleiche_basis_ganz` | 2 · `umkehr` | `zahl` | 12 Potenz | 2 | ja |
| PG-07 | Zwei Wege vergleichen | `exponent_und_potenz` | 2 · `mehrschritt` | `zahl` | 12 Potenz | 2 | ja |
| PG-08 | Fehler-Detektiv (einfache Form) | `fehler_ganz` | 3 · `fehler` | `auswahl` | 12 Potenz | 3 | ja |
| PG-09 | Fehler-Detektiv (einfache Form) | `fehler_ganz` | 3 · `fehler` | `zahl` | 12 Potenz | 2 | ja |
| PG-10 | Verfahren wählen (einfache Form) | `gleiche_basis_ganz` | 1 · `erkennen` | `auswahl` | 12 Potenz | 3 | ja |
| PG-11 | Verfahren wählen (einfache Form) | `exponent_und_potenz` | 1 · `erkennen` | `auswahl` | 12 Potenz | 3 | ja |
| PG-12 | Lückenweg | `gleiche_basis_ganz` | 1 · `direkt` | `luecken` | 12 Potenz | 3 | **nein** |
| PG-13 | Fehler-Detektiv (einfache Form) | `warum_gilt` | 3 · `fehler` | `zahl` | 12 Potenz | 3 | ja |

**Klasse 8 · `gleichungen.bruch`**

| Kennung | Typ | Lernkarte | Stufe · `g` | Form | Grundregel | Fehlbilder | zählt für „gelandet“ |
|---|---|---|---|---|---|---|---|
| BG-01 | Lückenweg | `ueber_kreuz` | 1 · `direkt` | `luecken` | 14 Verhältnis | 4 | **nein** |
| BG-02 | Lückenweg | `ueber_kreuz` | 2 · `mehrschritt` | `luecken` | 14 Verhältnis | 3 | nur Folge |
| BG-03 | Lückenweg | `hauptnenner` | 1 · `direkt` | `luecken` | 7 Waage | 3 | **nein** |
| BG-04 | Lückenweg | `ein_bruch` | 2 · `mehrschritt` | `luecken` | 7 Waage | 3 | nur Folge |
| BG-05 | Zwei Wege vergleichen | `ueber_kreuz` | 2 · `darstellung` | `zahl` | 10 Wert bleibt | 2 | ja |
| BG-06 | Zwei Wege vergleichen | `hauptnenner` | 2 · `umkehr` | `zahl` | 7 Waage | 2 | ja |
| BG-07 | Fehler-Detektiv (einfache Form) | `hauptnenner` | 3 · `fehler` | `auswahl` | 7 Waage | 3 | ja |
| BG-08 | Fehler-Detektiv (einfache Form) | `hauptnenner` | 3 · `fehler` | `zahl` | 7 Waage | 2 | ja |
| BG-09 | Verfahren wählen (einfache Form) | `ueber_kreuz` | 1 · `erkennen` | `auswahl` | 14 Verhältnis | 3 | ja |
| BG-10 | Verfahren wählen (einfache Form) | `scheinloesung` | 1 · `erkennen` | `auswahl` | 9 Einsetzen und Probe | 3 | ja |
| BG-11 | Formel umkehren | `ein_bruch` | 2 · `umkehr` | `zahl` | 8 Umkehren | 2 | ja |
| BG-12 | Formel umkehren | `verhaeltnis` | 2 · `umkehr` | `zahl` | 8 Umkehren | 2 | ja |
| BG-13 | Brücke: Zahl, aber nicht ausrechnen | `verhaeltnis` | 2 · `darstellung` | `luecken` | 14 Verhältnis | 3 | ja |

## Typen in der einfachen Form

- **Typ 4 Lückenweg**, je Thema drei Hilfestufen: *volle Hilfe* (jede Zeile vorgegeben, je eine Lücke; Stufe 1) · *halbe Hilfe* („Der erste Schritt ist gemacht. Rechne zu Ende“; Stufe 2) · *wenig Hilfe* (nur das Gerüst der letzten Zeilen; Stufe 2). Die Stufe ganz ohne Hilfe sind die vorhandenen Rechenaufgaben des Themas. Die Hilfe verschwindet also von hinten: Zuerst muss das Kind das Ende allein rechnen, dann immer mehr.
- **Typ 14 Zwei Wege vergleichen:** Antwort ist immer eine Zahl aus Weg B, die man nur findet, wenn man beide Wege versteht. Als Fehlbild steht jeweils die Zahl, die man aus Weg A abschreiben würde.
- **Typ 12 Fehler-Detektiv, einfache Form:** zwei getrennte Aufgaben statt einer Doppel-Karte – (a) erste falsche Zeile wählen, (b) „Was kommt richtig heraus?“ als Zahl.
- **Typ 13 Verfahren wählen, einfache Form:** Auswahl des Wegs oder – umgekehrt – der Aufgabe, zu der ein Weg passt. Umständliche, aber richtige Wege sind als solche etikettiert („richtig, aber umständlich“), nicht als Fehler einer Regel.
- **Typ 17 Formel umkehren:** nur in `gleichungen.bruch` (zwei Aufgaben). Die drei anderen Themen haben keine Formel.
- **Brücke „Zahl, aber nicht ausrechnen“:** Zwillingszeilen. Zeile 1 ist nachrechenbar, Zeile 2 hat dieselbe Bauart mit großen Zahlen oder Buchstaben.

## Wo die Aufgaben stehen und ob sie zählen (Vorschlag)

- **Platz:** jeweils in der Lernkarte aus der Tabelle, als Pool `uebung`. Innerhalb der Lernkarte: Lückenweg mit voller Hilfe als **erste** Übung nach der Erklärung; halbe und wenig Hilfe vor den vorhandenen Stufe-2-Aufgaben; Brücke und „Zwei Wege“ in Stufe 2 gemischt; Fehler-Detektiv in Stufe 3.
- **Zählregel** [M]: „ja“ = zählt wie jede Übung der Stufe. „nur Folge“ (halbe und wenig Hilfe) = zählt für „in Folge“, aber nicht als eigene Lösung. „nein“ (volle Hilfe, acht Aufgaben) = zählt gar nicht.
- **Achtung:** Heute zählt jede Übung im Pool `uebung` [G, `inhalte/README.md`]. Würden die acht Aufgaben mit voller Hilfe so eingespielt, zählten sie als eigene Lösung auf Stufe 1. Bis es dafür eine Lösung gibt (siehe Bedarf 2), diese acht **nicht einspielen** – die übrigen 44 gehen ohne sie.

## Bedarf – Felder, die im Format fehlen (nicht erfunden)

1. **Regel und Fehlbild je Aufgabe.** Es gibt kein Feld. Gebraucht wird: je Aufgabe eine Regel-Nummer; je falscher Antwort (bei `zahl` und `luecken`: je Wert, bei `auswahl`: je Index) ein Fehlbild-Text und eine Regel-Nummer. Alles steht fertig in `etiketten.json`.
2. **„Zählt nicht“ / „zählt nur für die Folge“.** Es gibt nur den Pool `bonus` für Knobel-Aufgaben. Gebraucht wird ein Kennzeichen je Aufgabe oder ein eigener Pool für Aufgaben mit Hilfe.
3. **Typ der Auswahl (4, 12, 13, 14, 17, Brücke).** `g` kennt diese Gedanken nicht. Ich habe die nächstliegenden vorhandenen Werte gesetzt (`direkt`, `mehrschritt`, `darstellung`, `umkehr`, `erkennen`, `fehler`, `begruenden`), damit das Prüfskript läuft und die Stufe stimmt. Der eigentliche Typ steht in `etiketten.json`.
4. **Reihenfolge in der Lernkarte.** Der Lückenweg mit voller Hilfe soll vor den freien Aufgaben kommen. Ob die App die Reihenfolge der Datei einhält oder nach Stufe mischt, weiß ich nicht.
5. **Kennung je Aufgabe.** Aufgaben haben kein eigenes Kennzeichen; `etiketten.json` hängt deshalb an der Reihenfolge und am Fragetext.

## Hinweise an den Projektleiter

- **Minus vor der Klammer in Klasse 5:** `zahlen.rechengesetze` erklärt es nicht; bisher gibt es dazu eine einzige Aufgabe (in `klammern`) [G]. RG-04, RG-07 und RG-13 stehen deshalb in `klammern` und sind mit „Klammer zuerst“ nachrechenbar. Sie bereiten die Regel vor, setzen sie aber nicht voraus. Wenn das zu früh ist: diese drei weglassen.
- **Papier-Test zuerst** [M]: Die Aufgaben üben genau die Muster von Teil 2 des Papier-Tests. Blatt A sollte geschrieben sein, bevor Schritt 1 eingespielt wird – sonst fehlt der Ausgangswert.
- Aus der Gegenprüfung übernommen sind 25 − 4 · (3 − 8) (RG-01) und 5/(x + 3) = 2/(x − 3) (BG-01, BG-05). Mit dem Papier-Test habe ich die Zahlen beim Schreiben auseinandergehalten, aber nicht per Skript abgeglichen.

## Nicht geprüft

- **Darstellung in der App:** lange Fragetexte mit Rechenweg in einer Zeile und Lücken ①–⑤; hochgestellte Buchstaben (ᵏ ᵐ ⁿ) auf dem Handy; fünf Zahlenfelder untereinander.
- Ob die App „(1) … (2) …“ in einem Fragetext lesbar umbricht.
- Die „naheliegenden“ falschen Antworten: aus den Fehlbildern abgeleitet, nicht aus Versuchsdaten.
- Sprache nicht von ChatGPT gegengelesen (vorgesehen vor dem Einspielen).
- Lehrplan-Stelle der zwei Formel-Aufgaben (Geschwindigkeit, Preis je Kilogramm) – als Alltagswissen angenommen.

## Annahmen

- Je Klasse lernt ein Kind; „laufend“ heißt: meiste Versuche in den letzten drei Lerntagen.
- Die Zuordnung der neuen Typen zu vorhandenen `g`-Werten ist eine Notlösung (Bedarf 3).
- Halbe Hilfe auf Stufe 2 ist richtig eingestuft; mit dem Kind nicht erprobt.
