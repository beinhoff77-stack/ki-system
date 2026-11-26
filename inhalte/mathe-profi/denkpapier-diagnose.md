# Denkpapier: Erkennt die App, was ein Kind nicht verstanden hat?

Mathe-Profi, 25.11.2026. Denkauftrag des Projektleiters, kein Bau. Stand `lernen-app` edb6b86 (enthält d00cf04).
**[G]** gesichert (im Repo gezählt, gerechnet, gelesen; Forschung mit Quelle) · **[A]** Annahme · **[M]** Meinung. Nachweis der Zahlen: `fehlbild_probe.py` (nur Inhalte, keine Lerndaten).

## Kern

1. Typische falsche Ergebnisse lassen sich bei Rechen-Mustern **mitberechnen** – der billigste Hebel der These. [G]
2. Ein falsches Ergebnis ist aber noch kein Denkfehler. Erst **dasselbe Fehlbild bei zwei eigens gewählten Aufgaben** trägt eine Diagnose. [G/M]
3. Der Maßstab (Papier, Zeit, ohne Hilfe) wird heute von nichts gemessen. Das Prüfungssystem ist die Voraussetzung der These, nicht ihr Zusatz. [M]

## 1. Fehlvorstellungen und Fehlbilder

„Fehlbild“ = das Ergebnis, das ein Denkfehler bei genau dieser Aufgabe liefert. Die Denkfehler sind Fachwissen [A]; dass sie sich ausrechnen und trennen lassen, ist gezählt [G]. Auswahl:

| Flug | Denkfehler | Beispiel → Fehlbild |
|---|---|---|
| Ganze Zahlen ± | Beträge addieren, Minus davor (Regel für gleiche Vorzeichen übertragen) | (−7) + 4 → −11 |
| | „Minus und Minus gibt Plus“ aus dem Malnehmen übertragen | (−5) + (−3) → 8 · (−5) − 3 → 8 |
| | Minus-Minus übersehen | 5 − (−3) → 2 |
| Terme umformen | Faktor nur zum ersten Glied | 3(x + 2) → 3x + 2 |
| | Minusklammer: nur erstes Vorzeichen | 5x − (3x − 2) → 2x − 2 |
| | Quadrat gliedweise | (x + 4)² → x² + 16 |
| Prozent | durch den Prozentsatz teilen | 15 % von 240 → 16 |
| | Prozent als Einheit | 80 € − 25 % → 55 € |
| | Prozentwert statt Grundwert (das Ganze wird kleiner) | 30 % sind 12 kg → 3,6 kg |

**Lässt sich das mitberechnen? Ja.** [G] 69 % aller Aufgaben tragen schon den Rechenausdruck `c`. Daneben braucht es je Muster eine Liste `fehlbilder` (Ausdruck + Name des Denkfehlers). Probe an den vorhandenen Aufgaben: Ganze Zahlen addieren/subtrahieren – 59 Aufgaben mit lesbarem Muster, bei **49** ist mindestens ein Fehlbild eindeutig (anders als die Lösung und als jedes andere Fehlbild), bei 9 fallen zwei Denkfehler zusammen. Prozent – 93 von 93 mit eindeutigem Fehlbild. Bei Termen ist das Fehlbild ein Zahlen-Tupel (Minusklammer: richtig [2, 2], Fehlbild [2, −2]).

**Heute** [G]: Der Server erkennt vier allgemeine Muster (Vorzeichen, Komma, gerundet, vertauscht); −11 statt −3 ist keines davon. Die „typischen Fehler“ stehen je Etappe als ein Satz Text, nicht als Rechnung.

**Drei Grenzen**
- „Eindeutig“ gilt nur unter den aufgeschriebenen Denkfehlern; ein Rechenfehler kann dasselbe Ergebnis haben. [G]
- Denkfehler sind nicht stabil: Kinder wechseln zwischen mehreren Reparaturen derselben Lücke („bug migration“). Diagnostiziert wird besser die **Stelle, an der das Kind festhängt**, als der einzelne Fehler. [G, Quelle 1]
- Deshalb **Trennaufgaben**: Zahlen so gewählt, dass jedes Fehlbild ein anderes Ergebnis hat. Regel [M]: erkannt, wenn dasselbe Fehlbild bei 2 von 3 Trennaufgaben auftritt.

## 2. Rückfrage „Wie hast du gerechnet?“

**Taugt, aber nur als zweites Mittel.** [M]
- Dafür: trennt Denkfehler mit gleichem Ergebnis; kostet einen Tipp.
- Dagegen: Wiedererkennen ist nicht Selbermachen. Kommt die Frage nur nach Fehlern, ist sie selbst das Fehlersignal – das Kind tippt den Weg, der richtig aussieht.
- Regeln: nur wenn die Antwort ein Fehlbild trifft; **vor** der Anzeige richtig/falsch; gelegentlich auch nach richtigen Antworten; Wege als Handlung ohne Ergebnis; immer „anders“ und „geraten“; zählt nie als Fehler.

Klasse 5, (−7) + 4: „7 + 4 gerechnet und das Minus davorgesetzt“ · „Von −7 aus 4 Schritte nach rechts“ · „7 − 4 gerechnet, Vorzeichen der größeren Zahl“ · anders · geraten.
Klasse 8, 5x − (3x − 2): „Klammer weggelassen“ · „Beide Zeichen in der Klammer umgedreht“ · „Nur das erste Zeichen umgedreht“ · anders · geraten.

**Besser: Kontrollzahl** (Abschnitt 4) – sie fragt nach einem Zwischenergebnis statt nach einer Selbstauskunft.

## 3. Erklär-Leiter

| Stufe | Auslöser | Was die App tut |
|---|---|---|
| 0 | 1. Fehler | Keine Erklärung. Trifft die Antwort ein Fehlbild: **ein** Satz, der den Widerspruch zeigt („Du bekommst 4 dazu. Kann es dann weniger werden?“). Zweiter Versuch. |
| 1 | 2. Fehler, gleiche Aufgabe | Lösungsweg am Bild. Sofort eine **Zwillingsaufgabe** (gleicher Bau, andere Zahlen) – lesen allein zählt nicht. |
| 2 | gleiches Fehlbild bei einer zweiten Aufgabe der Etappe | Denkfehler angenommen. Die eigene Regel an einem Fall zeigen, bei dem sie Unsinn ergibt; dann **Lückenweg** in drei Stufen (ganz vorgerechnet → letzte Zeile offen → nur der Anfang); 3 Trennaufgaben. |
| 3 | 2 von 3 Trennaufgaben wieder falsch | **Zurück zur Voraussetzung:** 3 Aufgaben aus der Etappe, auf die das Fehlbild zeigt. Sitzt sie nicht → dorthin. Sitzt sie → zweites Modell (Guthaben statt Zahlengerade), Stufe 2 noch einmal. |
| 4 | Stufe 3 ohne Erfolg | Meldung an den Erwachsenen: Fehlbild in einem Satz, zwei Beispiele, Vorschlag für 10 Minuten am Tisch. |

Nötig: **je Fehlbild ein Zeiger auf eine Etappe** – die Voraussetzungen liegen heute nur zwischen Themen vor [G]. Der Lückenweg mit abnehmender Hilfe ist belegt, am besten rückwärts (zuerst die letzten Schritte weglassen). [G, Quelle 3]

**Durchgespielt, Klasse 5.** (−7) + 4, Antwort −11. Stufe 0: Widerspruchs-Satz; zweiter Versuch 11. Stufe 1: Weg an der Zahlengeraden, Zwilling (−9) + 5 richtig. Später 6 + (−10) → −16: dasselbe Fehlbild, Stufe 2. Gegenüberstellung: „Bei (−7) + (−4) stimmt deine Regel. Bei (−7) + 4 gehst du aber in die andere Richtung.“ Der Denkfehler ist eine **richtige Regel am falschen Ort**; die Erklärung muss den Unterschied zeigen, nicht die Regel wiederholen. Lückenweg, dann drei Trennaufgaben. Zwei falsch → Stufe 3: drei Markier-Aufgaben „Starte bei −7, geh 4 nach rechts“. Richtig → es fehlt nur die Verbindung „plus = nach rechts“ → Guthaben-Modell. Falsch → Etappe Zahlengerade.

**Durchgespielt, Klasse 8.** Gleichung 5x − (3x − 2) = 12, Antwort x = 7 (richtig: 5). Zwei verschiedene Denkfehler liefern genau 7 [G, im Skript]: Minusklammer falsch (2x − 2 = 12) **oder** Klammer richtig und danach falsch umgeformt (2x = 12 + 2). Die Voraussetzungen liegen in verschiedenen Flügen (Terme umformen aus Klasse 7 – Gleichungen). Das Ergebnis entscheidet nicht, wohin es zurückgeht. Die Kontrollzahl schon: „Was stand bei dir nach dem Auflösen der Klammer? □x + □ = 12“. [2, −2] → Minusklammer; [2, 2] → Umformen.

## 4. Rechenweg ohne Eintippen

Übertrag auf die Papier-Arbeit: 0 keiner · 3 hoch. [M, wo nicht anders vermerkt]

| Form | Übertrag | Urteil |
|---|---|---|
| Nächsten Schritt aus drei wählen | 1 | Erkennen statt Erzeugen. Nur für den Einstieg in ein Verfahren. |
| Schritte ordnen | 1 | Prüft Lesen eines fertigen Wegs. Auf Papier steht kein fertiger Weg. |
| Fehlerzeile antippen | 2 | Übt das Kontrollieren – in Schulaufgaben viel wert. Erzeugt nichts. |
| Lückenweg mit abnehmender Hilfe | 3 | Beste digitale Form [G, Quelle 3]. Muss bei **leeren Zeilen** enden, sonst bleibt das Kind am Geländer. |
| Mit Finger/Stift schreiben | 3 | Automatische Auswertung unzuverlässig, ohne Netz nicht machbar [A]. Nur als Ablage für die Stichprobe. |
| Sprechen | 0–1 | Unzuverlässig, ohne Netz nicht. Weglassen. |
| Heft + Selbstkontrolle nach Punkteschema | 3 | **Das ist die Prüfungsform.** Schwäche: Kinder bewerten sich zu milde [A]. Braucht Gegenkontrolle. |

**Bessere Formen**
- **Kontrollzahlen.** Das Kind rechnet im Heft, tippt das Ergebnis und wird **danach** nach ein bis zwei Zwischenergebnissen gefragt („Was stand vor dem x nach der zweiten Zeile?“). Welche, weiß es vorher nicht. Geht mit der vorhandenen Lücken-Form. Zwingt zum Aufschreiben und trennt Denkfehler.
- **Erste falsche Zeile.** Bei Termen tippt das Kind je Heft-Zeile die Zahlen vor x und ohne x. Der Server setzt Werte ein und meldet die erste Zeile, die nicht mehr gleichwertig ist. Das Kind sucht seinen Fehler im eigenen Heft.
- **Papier-Runde in Zeit.** 4–6 Aufgaben, Gesamtzeit, kein Tipp, kein zweiter Versuch; danach Punkteschema mit Kontrollzahlen. Jede vierte Runde ein Foto für den Erwachsenen.
- **Begründen ohne Auswahl** (heute 864 von 938): „Nenne eine Zahl, für die die Aussage nicht stimmt“ – der Server prüft die Bedingung.

## 5. Was die Dauer sagt

Heute wird sie nicht gespeichert [G]. Nötig wären drei Zeitpunkte: Anzeige, erste Eingabe, Abgabe – und ob die App im Vordergrund war.

| Dauer + Ergebnis | Deutung | Folge |
|---|---|---|
| sehr kurz, Auswahl | wahrscheinlich geraten [G, Quelle 2] | nicht werten, keine Erklärung, gleiche Karte später |
| lang + falsch | ernsthaft versucht | hier lohnt die Erklär-Leiter |
| lang + richtig | kann es, noch nicht flüssig | mehr üben, nichts erklären |
| kurz + richtig, wiederholt | automatisiert | zählt für „in Zeit“ |

**Was sie nicht sagt:** ob etwas verstanden ist; ob Pause, langer Text, Handy-Tastatur oder das Heft der Grund war. Schwellen für „geraten“ ordnen immer einen Teil falsch zu [G, Quelle 2]. Ohne Vergleichsgruppe: nur das Kind mit sich selbst vergleichen, je Aufgabenmuster. Im Lernen darf lange Dauer nie etwas kosten – wer im Heft rechnet, braucht länger und macht es richtig. Zeit zählt nur in der Papier-Runde, als Gesamtzeit.

## 6. Wo die These zu optimistisch ist

1. **Fehler → Denkfehler ist kein Automatismus.** Viele Fehler sind Ausrutscher, Denkfehler wandern. Bei wenigen Versuchen je Etappe muss Diagnose gebaut werden (Fehlbilder, Trennaufgaben), nicht aus Daten gelesen. [G/M]
2. **„Einfacher erklären“ hat einen Boden.** Einfacher heißt kleinerer Schritt, anderes Bild, selbst tun – nicht mehr Text. Nach zwei Runden braucht es einen Menschen, zehn Minuten lang. „Ohne Lehrer“ ist nicht „ohne Erwachsenen“. [M]
3. **80 % und 89 % sind nicht der Maßstab.** Sie entstehen mit Tipp, zweitem Versuch und meist Zahl oder Auswahl. Auf Papier ist ein Abfall zu erwarten; wie groß, weiß niemand vor der Messung. Stufe 3 ist schon jetzt schwächer – und Stufe 3 **ist** das Schulaufgaben-Niveau. [G Bedingungen, A Abfall]
4. **Schulaufgaben bewerten Darstellung:** Rechenweg, Antwortsatz, Einheiten, Konstruktion, Begründung in Sätzen. Das prüft die App nicht selbst. [A]
5. **Rückmeldung der Kinder** taugt für „Erklärung unverständlich“ und „Aufgabe kaputt“, nicht für „habe ich verstanden“. [A]
6. **Zwei Kinder sind keine Statistik.** Die App kann nicht lernen, welche Erklärung wirkt; Regeln kommen aus der Fachdidaktik. [G]
7. **Die These passt auf Verfahren** (Vorzeichen, Klammern, Prozentformel), kaum auf Sachaufgaben, Begründen und Konstruieren. [M]

**Reihenfolge, wenn daraus Arbeit wird [M]:** (1) Papier-Runde in Zeit – macht die Lücke zum Maßstab sichtbar; (2) Fehlbilder mit Trennaufgaben für die drei Flüge; (3) Kontrollzahlen; (4) Erklär-Leiter Stufen 0–2; (5) Dauer speichern.

**Nicht geprüft:** bayerische Korrekturpraxis; das neue Prüfmaterial im Repo; Vollständigkeit der Denkfehler-Listen.

**Quellen:** (1) Brown & VanLehn 1980, Repair Theory, Cognitive Science 4, https://www.lri.fr/~mbl/Stanford/CS477/papers/RepairTheory-SeelyBrown.pdf · (2) Wise & Kong 2005, Response Time Effort; Wise 2017, https://www.nwea.org/?p=44872 · (3) Renkl, Atkinson, Maier & Staley 2002, Journal of Experimental Education 70, https://escholarship.org/uc/item/81b9j9hs
