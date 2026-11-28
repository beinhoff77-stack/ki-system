# Korrektur nach Vorprüfung W1, 3. Durchgang, Runde VT1A

Stand 29.11.2026. Ausgang: `vorpruefung-w1-3.md` (A1–A5, B1–B3). Geändert habe ich nur die genannten Aufgaben; die Kennungen bleiben gleich.

Prüfläufe: `bauen.py` OK; `gegenrechnung.py` 55 Sollantworten, 0 Abweichungen; `tools/vorrat_pruefen.py` 0 Meldungen; `tools/vtest_pruefen.py --runde 1a` nur die 11 erwarteten Pool-Meldungen „2 statt 3“. Ergebnis: Je Lernziel genau eine Schema-Aufgabe (wie in `vorpruefung-w1-3.md` gezählt, ohne die ersetzten Aufgaben), nie im Test.

Jeden Ersatz habe ich gegen drei Fragen geprüft:
1. Lösbar durch Einsetzen weniger Werte, Durchprobieren aller Fälle oder Ausrechnen der genannten Zahlen?
2. Schreibt der Text das Verfahren vor?
3. Ist es ein Format, das im Bestand schon geübt wird?

Bei allen Ersatzaufgaben: dreimal nein.

| Befund | geschlossen wie | warum kein Schema |
|---|---|---|
| A1 zehner 012 | neu: „Eine Zahl hat genau 8 Stellen. Welche Aussage stimmt für jede solche Zahl?“ Richtig: mindestens 10⁷ und kleiner als 10⁸. Ablenker: Grenzen vertauscht, Stellen = Hochzahl, Hochzahl zu klein. | Die Zahl ist beliebig; ein Beispiel entscheidet nicht, ob 10⁷ und 10⁸ selbst dazugehören, dafür braucht man „10ⁿ hat n + 1 Stellen“. Kein Zahlenvergleich mit genannten Zahlen. |
| A2 termaufbau 030 | neu: Welche Aussage über Terme gilt für jeden Term? Richtig: Ganzer Term in Klammer mit „· 2“ dahinter ist immer ein Produkt. Ablenker: „2 ·“ ohne Klammer davor; eine Klammer ändert die Art nie; Malzeichen heißt Produkt. | Kein konkreter Term ist zu benennen (nicht das Bestandsformat). Die richtige Aussage braucht die Begründung über den letzten Rechenschritt; die falschen widerlegt man nur mit selbst gesuchten Gegenbeispielen. |
| A3 ueberschlag Test 046 | neu als Urteil: Lena überschlägt 3 412 · 3 438 mit 3 000 · 3 000 = 9 000 000 und sagt „7 Stellen“. Richtig: 8 Stellen, weil beide Zahlen stark abgerundet sind und schon 3 400 · 3 400 8 Stellen hat. Ablenker: 7 Stellen, 6 Stellen (Überschlag sei immer zu groß), nicht entscheidbar. | Der Text nennt kein Verfahren; das Kind muss selbst erkennen, dass die grobe Schätzung nichts entscheidet, und eine sichere Schranke finden. Vier verschiedene Urteile; genaues Ausrechnen (vierstellig mal vierstellig) ist nicht verlangt und unattraktiv. |
| A4 verteilen 039 | neu als Auswahl: Das Kind rechnet □ · (2 · 7) als □ · 2 · □ · 7. Wievielmal so groß ist sein Ergebnis für eine beliebige Zahl □? Richtig: □-mal. Ablenker: doppelt, 14-mal, um □ größer. | □ ist beliebig; gefragt ist ein Zusammenhang, kein Wert, der aus einem ersten Probierwert folgt. |
| A5 sach 053 | neu: Heft □ €, Stift 3 €; 8 einzeln gegen 8 Päckchen zu je 2 € weniger – um wie viel zahlt Tom weniger, egal welcher Heftpreis? (16 €) | □ ist unbekannt, es gibt keine Fälle zum Durchprobieren; die Lösung trägt das Ausklammern 8 · □ + 8 · 3 = 8 · (□ + 3). |
| B1 umkehraufgabe_mal 045 | neu: „Die Lösung von a · x = b ist immer kleiner als b“ – Antwort: fast immer, nur bei a = 1 gleich. Lösbarkeit (Test 041) kommt nicht mehr vor, auch nicht im Lösungsweg. | a und b sind beliebig; gefragt ist die Größe der Lösung, nicht die Lösbarkeit. Entscheidend ist das Gegenbeispiel a = 1 in einem offenen Suchraum. |
| B2 schreibweise 002 | neu: Potenz mit ungerader Basis und beliebiger Hochzahl – richtig „immer ungerade“. Ablenker: gerade bei gerader Hochzahl, mal so mal so, gerade ab Hochzahl 2. Andere Denkfigur als 003 (Wirkung einer Änderung) und andere Einsicht als Test 001 (keine Zerlegung 4 = 2 · 2). | Basis und Hochzahl sind beliebig; Beispiele widerlegen nur die Ablenker, die richtige Aussage braucht die Begründung „ungerade mal ungerade bleibt ungerade“. |
| B3 Test 016 | Text: „… mehr als in der richtigen Rechnung 2 · 3 · 3 · 3 · 3 · 3 · 3?“ | – |

Technisch:
- `kern.py`: Die Lagenfolge der richtigen Antwort ist verlängert (38 statt 34 Auswahl-Aufgaben); die Lagen der früheren Aufgaben bleiben gleich.
- `gegenrechnung.py`: für die geänderten Aufgaben angepasst.

## Neue oder geänderte Kennungen

002, 012, 016 (nur Text), 030, 039, 045, 046, 053.
