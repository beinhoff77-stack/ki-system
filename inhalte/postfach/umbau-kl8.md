# Postfach umbau-kl8 (Achte Runde: Umbau der Lernkarten auf das neue Muster, Klasse 8)

Neueste Meldung oben.

## 2026-11-16 03:09 – FERTIG
Achte Runde, Paket U8 (Klasse 8) abgeschlossen: 15 Themen, 97 Lernkarten auf das neue Muster umgebaut (einstieg ≤ 35 Wörter, woerter ≤ 3, Kartenbild, Schritte als {text, bild}, fehler + fehler_bild wo sinnvoll, regel mit „Kurz gesagt“ ≤ 12 Wörter).

| Thema | Karten | Aufgaben | gleich wie lernen-app | Prüfskript |
|---|---|---|---|---|
| funktionen.grundbegriffe | 8 | 192 | ja | 0 Fehler, 0 Hinweise |
| gleichungen.ungleichungen | 7 | 168 | ja | 0 / 0 |
| zahlen.intervalle | 4 | 96 | ja | 0 / 0 |
| terme.bruchterme | 7 | 168 | ja | 0 / 0 |
| gleichungen.formeln | 5 | 120 | ja | 0 / 0 |
| gleichungen.bruch | 7 | 168 | ja | 0 / 0 |
| gleichungen.lgs2 | 8 | 192 | ja | 0 / 0 |
| funktionen.linear | 7 | 168 | ja | 0 / 0 |
| funktionen.gebrochen | 6 | 144 | ja | 0 / 0 |
| messen.koerper_darstellung | 6 | 144 | ja | 0 / 0 |
| raum.schraegbilder | 6 | 144 | ja | 0 / 0 |
| messen.kreisberechnung | 7 | 168 | ja | 0 / 0 |
| stochastik.grundbegriffe | 6 | 144 | ja | 0 / 0 |
| stochastik.simulation | 6 | 144 | ja | 0 / 0 |
| groessen.indirekt | 7 | 189 | ja | 0 / 0 |

Technik:
- Neue Hilfsdatei inhalte/generatoren/_umbau_kl8.py; je Generator ein Abschnitt UMBAU, der NACH dem Erzeugen der Aufgaben eingesetzt wird. KLAR (Runde 7) bleibt stehen, weil die Generatoren dessen Beispieltexte zum Vermeiden von Dopplungen nutzen – so bleiben alle Aufgaben wörtlich gleich. Die alte „probe“ entfällt (Kontrolle steht, wo nötig, als Schritt).
- Aufgabenvergleich je Thema gegen `git show lernen-app:inhalte/themen/<thema>.json`: alle 2 534 Aufgaben wörtlich gleich.
- Darstellung geprüft: Alle 97 Karten mit lernErklaerung() aus lernen.js in Chromium (390 px) aufgebaut – keine Fehler, kein NaN/undefined in den Zeichnungen. Stichproben als Bild angesehen (graph_lesen, umdrehen, schraegbild, laengen); dabei überlappende Beschriftungen im Schrägbild behoben.
- Alle Zahlen der Situationen nachgerechnet (u. a. Monte-Carlo: 31 von 40 Punkten im Viertelkreis nachgezählt).

Bewusste Entscheidungen / offen:
- fehler_bild fehlt bei Karten, deren Fehler ein reiner Rechen- oder Formelfehler ist (z. B. kreisberechnung, mehrere Gleichungs-Karten). Dort gäbe es kein Bild, das den Fehler zeigt.
- Bei rein algebraischen Karten (z. B. Klammern, Kürzen, Verfahren wählen) ist das Beispiel allgemein, die Situation steht im Einstieg und im Pass auf!. Eine durchgehende Alltagssituation hätte die Rechnung verfälscht.
- Schrägbilder, Netze und Pyramiden sind mit der Zeichnungsart figur gebaut (Hilfspunkte mit _).
- App-Wünsche (unter "offen" in den Dateien): Zahlenstrahl-Bereich mit offenen/geschlossenen Endpunkten und Pfeil bis ∞ (zahlen.intervalle); Urne als Zeichnung (stochastik.simulation, behelfsweise Bruchstreifen).
- Beobachtung zur App: Ein Schrittbild ergänzt den vorigen Zustand nur flach. Wer bei figur Punkte austauscht, muss flaeche/kreise mit leeren, die auf fehlende Punkte zeigen. Sonst wirft lernFigur einen TypeError. Vorschlag: lernFigur überspringt unbekannte Punkte.
- Sätze in raum.schraegbilder und messen.koerper_darstellung sind ≤ 15 Wörter, weil das Prüfskript dort wegen rs_by 5/6 die Grenze für Klasse 5/6 anlegt.
- Noch nicht mit dem Kind getestet.
- Nicht gemergt.

## 2026-11-16 03:07 – STATUS
groessen.indirekt umgebaut (7 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/groessen.indirekt.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Generator heißt groessen_indirekt.py (UMBAU nach dem vorhandenen mit_klar eingesetzt). Ohne fehler_bild: graph, unterscheiden, sach.

## 2026-11-16 03:06 – STATUS
stochastik.simulation umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/stochastik.simulation.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: regel, zufallsziffern, auswerten, monte_carlo, beurteilen. Urne behelfsweise als Bruchstreifen (unter offen).

## 2026-11-16 03:05 – STATUS
stochastik.grundbegriffe umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/stochastik.grundbegriffe.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: rel_haeufigkeit, laplace, gegenereignis, grosse_zahlen. Säulenwerte bei grosse_zahlen sind ein erfundenes, aber typisches Wurfergebnis (im Text als Beispiel gekennzeichnet).

## 2026-11-16 03:04 – STATUS
messen.kreisberechnung umgebaut (7 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/messen.kreisberechnung.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: alle 7 (Fehler sind Formel- bzw. Rechenfehler; Zahlen in den Schritten nachgerechnet).

## 2026-11-16 03:02 – STATUS
raum.schraegbilder umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/raum.schraegbilder.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: pyramide, lage, koordinaten, rotation. Sätze ≤ 15 Wörter (Thema hat rs_by 5).

## 2026-11-16 03:01 – STATUS
messen.koerper_darstellung umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/messen.koerper_darstellung.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: prisma, netz, ansichten. Schrägbilder und Netze sind mit der Zeichnungsart figur gezeichnet (Hilfspunkte mit _). Sätze hier ≤ 15 Wörter, weil das Thema auch rs_by 6 hat.

## 2026-11-16 02:59 – STATUS
funktionen.gebrochen umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/funktionen.gebrochen.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: beurteilen.

## 2026-11-16 02:58 – STATUS
funktionen.linear umgebaut (7 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/funktionen.linear.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: zwei_punkte, deuten.

## 2026-11-16 02:57 – STATUS
gleichungen.lgs2 umgebaut (8 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/gleichungen.lgs2.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: grafisch, einsetzen, gleichsetzen, verfahren, loesbarkeit, sachaufgabe (Fehler ist ein Rechen- bzw. Ablesefehler ohne eigenes Bild).

## 2026-11-16 02:55 – STATUS
gleichungen.bruch umgebaut (7 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/gleichungen.bruch.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: ein_bruch, ueber_kreuz, scheinloesung.

## 2026-11-16 02:54 – STATUS
gleichungen.formeln umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/gleichungen.formeln.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: pruefen.

## 2026-11-16 02:52 – STATUS
terme.bruchterme umgebaut (7 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/terme.bruchterme.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: definitionsmenge, termwert, kuerzen, multiplizieren (Fehler ist ein Rechenschritt ohne sinnvolles Bild).

## 2026-11-16 02:51 – STATUS
zahlen.intervalle umgebaut (4 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/zahlen.intervalle.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: beurteilen. App-Wunsch unter offen: offene/geschlossene Endpunkte beim Zahlenstrahl-Bereich.

## 2026-11-16 02:50 – STATUS
gleichungen.ungleichungen umgebaut (7 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/gleichungen.ungleichungen.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: umformen, klammern, intervall (Rechenfehler lässt sich im Bild nicht sinnvoll zeigen).

## 2026-11-16 02:48 – STATUS
funktionen.grundbegriffe umgebaut (8 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_kl8.py).
Aufgaben-Vergleich gegen `git show lernen-app:inhalte/themen/funktionen.grundbegriffe.json`: alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise.
