# Postfach umbau-kl10 (Achte Runde: Umbau der Lernkarten auf das neue Muster, Klasse 10)

Neueste Meldung oben.


## 2026-11-16 03:15 – FERTIG (Abschlussbericht U10)
Paket U10 (Achte Runde, Klasse 10) ist umgesetzt. Zweig umbau-kl10, kein Merge nach main.

| Thema | Karten | Aufgaben | Aufgaben-Unterschiede | Prüfhinweise | ohne fehler_bild |
|---|---|---|---|---|---|
| gleichungen.exponential | 6 | 168 | 0 | 0 | potenzregel, verstehen |
| gleichungen.polynom | 5 | 140 | 0 | 0 | verstehen |
| funktionen.exponential_log | 6 | 168 | 0 | 0 | graph, logfunktion, zeitpunkt |
| funktionen.trig | 7 | 196 | 0 | 0 | bogenmass, periode, zuordnen |
| funktionen.ganzrational | 7 | 196 | 0 | 0 | randverhalten, term_bestimmen |
| raum.pyramide_kegel_kugel | 7 | 196 | 0 | 0 | kugel |
| stochastik.mehrstufig | 7 | 196 | 0 | 0 | simulation, verstehen |
| **Summe** | **45** | **1 260** | **0** | **0** | **14** |

- Alle Karten: einstieg ≤ 35 Wörter, woerter ≤ 3 (jedes im Text), Kartenbild, Schritte als {text, bild} mit Bild bei jedem Bildwechsel, fehler (+ fehler_bild, wo sinnvoll), regel mit erstem Satz ≤ 12 Wörter („Kurz gesagt“). titel und lernziel unverändert, Aufgaben wörtlich gleich (Vergleich gegen den Stand vor jedem Commit).
- Gründe für fehlende fehler_bild stehen in den STATUS-Meldungen der Themen (meist Denk- oder Rechenfehler ohne sinnvolles Bild).
- Technik: `_kl10.bauen(klar=…)` setzt KLAR nach dem Erzeugen der Aufgaben ein; im neuen Muster entfällt `probe` (die Kontrolle steht als Schritt in der Bildergeschichte). Nur Inhalte und Generatoren geändert; keine Datenbank, keine Serverfunktionen, kein App-Code, keine Tests.
- Neue Kartenbilder, wo vorher keins war: u. a. ganzrational grad/ausmultiplizieren (Tabellen), trig bogenmass/werte (Einheitskreis), raum verstehen (zwei Kegel), stochastik verstehen (Münzbaum).
- funktionen.trig: Der Commit aca25ca hatte noch einen Längenhinweis (Schritt mit 16 Wörtern); behoben in bc36176. Die STATUS-Meldung „0 Hinweise“ gilt ab bc36176. Seitdem bricht das Commit-Skript bei offenen Hinweisen ab.

### offen
- Laut AUFTRAEGE.md sollte die Achte Runde erst nach dem Test mit den Kindern laufen. U10 wurde auf Sebastians ausdrücklichen Auftrag vom 16.11. trotzdem jetzt ausgeführt; Rückmeldungen aus dem Test sind noch nicht eingearbeitet.
- Darstellung in der App nicht im Browser geprüft. Annahme: Ein Schrittbild überschreibt die genannten Felder des Kartenbilds, ein anderer `typ` ersetzt es ganz. Wo ein Schritt zu einem früheren Bild zurückkehrt, ist das Bild vollständig angegeben.
- Baumdiagramme haben keine Markierung von Pfaden; die Schrittbilder zeigen daher gekürzte Bäume (nur der gemeinte Pfad). Falls eine Pfad-Markierung kommt, wären diese Schritte einfacher.
- Merge nach main erst nach Sebastians „Live“.

## 2026-11-16 03:07 – STATUS
stochastik.mehrstufig umgebaut (7 Karten): einstieg (≤ 35 Wörter), woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel (erster Satz = Kurz gesagt). KLAR-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_kl10.bauen(klar=…)); probe entfällt.
Aufgaben-Vergleich gegen `git show HEAD:inhalte/themen/stochastik.mehrstufig.json`: alle 196 wörtlich gleich, titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. simulation (der Fehler ist ein Denkfehler „der Würfel merkt sich etwas“, ein Diagramm würde ihn nicht zeigen) und verstehen (der Fehler ist allgemein „über 1 ist unmöglich“; dasselbe Bild steht schon als fehler_bild bei pfad_mult). Das Baum-Bild hat keine Markierung, daher zeigen die Schrittbilder den Baum stufenweise oder nur mit den gemeinten Pfaden

## 2026-11-16 03:06 – STATUS
raum.pyramide_kegel_kugel umgebaut (7 Karten): einstieg (≤ 35 Wörter), woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel (erster Satz = Kurz gesagt). KLAR-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_kl10.bauen(klar=…)); probe entfällt.
Aufgaben-Vergleich gegen `git show HEAD:inhalte/themen/raum.pyramide_kegel_kugel.json`: alle 196 wörtlich gleich, titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. kugel (der Fehler ist ein Einheitenfehler cm² statt cm³, er steckt in der Formel, nicht in der Zeichnung). Brüche im Text als 1/3 und 2/3 statt Unicode-Bruchzeichen (Prüfhinweis)

## 2026-11-16 03:03 – STATUS
funktionen.ganzrational umgebaut (7 Karten): einstieg (≤ 35 Wörter), woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel (erster Satz = Kurz gesagt). KLAR-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_kl10.bauen(klar=…)); probe entfällt.
Aufgaben-Vergleich gegen `git show HEAD:inhalte/themen/funktionen.ganzrational.json`: alle 196 wörtlich gleich, titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. randverhalten (der Fehler ist ein Rechenvergleich bei x = 100, ein Bild würde nur das Kartenbild wiederholen) und term_bestimmen (der Fehler liegt in der Gleichung 3a = 6, nicht im Graphen)

## 2026-11-16 03:01 – STATUS
funktionen.trig umgebaut (7 Karten): einstieg (≤ 35 Wörter), woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel (erster Satz = Kurz gesagt). KLAR-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_kl10.bauen(klar=…)); probe entfällt.
Aufgaben-Vergleich gegen `git show HEAD:inhalte/themen/funktionen.trig.json`: alle 196 wörtlich gleich, titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: bogenmass (60π = 30 Runden lässt sich nicht sinnvoll zeichnen), periode (1 080° liegt außerhalb der Zeichnung), zuordnen (sin(180x) wäre zu dicht zum Zeichnen). Kartenbilder für bogenmass und werte neu: Einheitskreis (koordinaten mit kreise).

## 2026-11-16 02:59 – STATUS
funktionen.exponential_log umgebaut (6 Karten): einstieg (≤ 35 Wörter), woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel (erster Satz = Kurz gesagt). KLAR-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_kl10.bauen(klar=…)); probe entfällt.
Aufgaben-Vergleich gegen `git show HEAD:inhalte/themen/funktionen.exponential_log.json`: alle 168 wörtlich gleich, titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: graph, logfunktion (Denkfehler „irgendwann 0“ bzw. „für alle x“ – das Kartenbild zeigt es schon), zeitpunkt (Rechenfehler beim Umformen).

## 2026-11-16 02:57 – STATUS
gleichungen.polynom umgebaut (5 Karten): einstieg (≤ 35 Wörter), woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel (erster Satz = Kurz gesagt). KLAR-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_kl10.bauen(klar=…)); probe entfällt.
Aufgaben-Vergleich gegen `git show HEAD:inhalte/themen/gleichungen.polynom.json`: alle 140 wörtlich gleich, titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: verstehen (Denkfehler „Grad = Anzahl“; das Kartenbild zeigt die Lösung schon).

## 2026-11-16 02:56 – STATUS
gleichungen.exponential umgebaut (6 Karten): einstieg (≤ 35 Wörter), woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel (erster Satz = Kurz gesagt). KLAR-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_kl10.bauen(klar=…)); probe entfällt.
Aufgaben-Vergleich gegen `git show HEAD:inhalte/themen/gleichungen.exponential.json`: alle 168 wörtlich gleich, titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: potenzregel (Rechenfehler lg(5x), kein sinnvolles Bild), verstehen (Fehler ist ein Denkfehler; das Kartenbild zeigt die Lösung schon).

