# Individueller Lehrplan beider Kinder (Auftrag 8)

Mathe-Profi, 26.11.2026. Stand `lernen-app` 783cea47. **Nichts ist eingestellt.** Einstellen erst nach Gegenprüfung und ausdrücklichem Satz des Nutzers.
**[G]** gesichert (im Repo oder in der App nachgelesen, gezählt) · **[A]** Annahme · **[M]** Meinung.

| Datei | Inhalt |
|---|---|
| `nutzer-seite.md` | eine Seite in einfacher Sprache: Plan je Kind, Begründung, Entscheidungen |
| `route.md` | beide Routen in Abschnitten: je Flug Themen, Etappen, Schulart, Pflicht oder Kür, Begründung; Umfang |
| `einstell-liste.md` | je Kind Platz und Status jedes Flugs, Änderungen fett |
| `plan.py` | die Routen als Daten; prüft Voraussetzungen und Abschnittsgrößen, zählt, schreibt `route.md` und `einstell-liste.md` |

Gelesen (nur lesend): der heutige Plan beider Kinder in der App und der Stand je Thema. Im Repo steht nur die Einordnung, keine Quote und kein Ergebnis.

## 1. Grundsatz der Reihenfolge

**Im Wechsel, nicht am Stück – aber innerhalb eines Gebiets nie gegen die Voraussetzungen.** [M]

1. **Voraussetzungen zuerst** [G, `plan.py` prüft es]: Kein Flug steht vor einem Flug, den er braucht (Einheiten vor Fläche vor Volumen; Teilbarkeit vor Brüchen; Funktionsbegriff vor linearen Funktionen vor Gleichungssystemen; indirekte Proportionalität vor Hyperbeln).
2. **Regel an Zahlen vor Regel mit x.** Die Brücke liegt für Kind 1 bei `a1` (Waage und Umkehren an Zahlen) und `a2` (Variable einführen); deshalb stehen beide vor dem Bruchrechnen. Für Kind 2 ist die Brücke überschritten; dort zeigen die Kreuzungen (Abschnitt 4), wo dieselbe Regel wiederkehrt.
3. **Höchstens zwei Rechen-Flüge hintereinander,** dann Geometrie, Größen oder Daten. Grund: Im Maßstab (Jahrgangsstufentest 8) kommen Geometrie, Daten und Geld auf zusammen fast zwei Drittel der Punkte (`denkpapier-massstab.md`); in der App lief bisher fast nur Rechnen und Algebra [G].
4. **Am Stück nur, wo ein Flug den nächsten unmittelbar fortsetzt** (Dreisatz Teil 1 und 2; Funktionsbegriff und lineare Funktionen dürfen getrennt sein, weil Wiederholungen mitlaufen).
5. **Wiederholungen ersetzen keinen Wechsel:** Sie halten Gelerntes, bringen aber kein neues Gebiet.
6. **Was die Realschule früher hat, kommt früher** – aber nur, wenn die Voraussetzung da ist (Kind 1: Daten darstellen, Körper darstellen, Terme aufstellen, Spiegeln).
7. **IB läuft nebenbei als Kür** an Stellen, wo der Flug inhaltlich anschließt (Mengen nach Klasse 5; Verhältnisse nach Dreisatz und Brüchen).
8. **Kurze, eigenständige Flüge** (Zählen, Mittelwert, Laplace) stehen am Ende eines Abschnitts oder zwischen zwei schweren Flügen.

## 2. Kind 2: Was ist mit Klasse 7?

**Wichtig vorab [G]:** Die App kann für die meisten Klasse-7-Flüge keine Lücke belegen, weil sie dort nie bearbeitet wurden. „Nicht bearbeitet“ heißt nicht „kann er nicht“. Eine echte Antwort gibt nur eine Probe auf Papier. Dafür gibt es ein fertiges Instrument: **ein ganzer amtlicher Jahrgangsstufentest der Klasse 8** – er prüft genau den Stoff der Klassen 5 bis 7 (40 Minuten, Schema liegt vor). Ich schlage ihn als Eingangsdiagnose vor, zusammen mit Blatt A aus Auftrag 5.

| Einordnung | Flüge | Begründung |
|---|---|---|
| **Vor oder zwischen dem Klasse-8-Stoff** (Abschnitte 1 und 2) | `ge4` Dreiecke, Vierecke, Konstruktion · `g8` Prozent mit verändertem Grundwert · `ge5` Kreis | In der App offen oder aus dem Plan genommen, nie abgeschlossen. Geometrie-Begründungen und Prozent sind feste Teile des Maßstabs. `ge4` ist außerdem Voraussetzung für `ge5`. |
| **Kann er – läuft als Wiederholung nebenher** | `a3` Terme umformen, `a3-teil2` (binomische Formeln) | In der App abgeschlossen; deckt sich mit der Arbeit beim Lehrer. Die Wiederholungen der App halten es. |
| **Kann er – nicht nachholen** | `a2` Terme aufstellen | In der App als „kann schon“ geführt. |
| **Kann warten** (Abschnitte 3 und 4) | `ge2` Spiegeln und Symmetrie (mit Teil 2, 3) · `d10` Boxplot · `d4` Stichproben · `ge9` Determinanten | Keine Voraussetzung für Klasse-8-Stoff. `ge2` rückt vor, falls die Eingangsdiagnose dort eine Lücke zeigt. |
| **Unklar, durch Diagnose zu klären** | `ge3` Winkel (Klasse 5) | Steht heute offen im Plan, ohne „kann schon“. Voraussetzung für `ge4`. |

**Auffällig am heutigen Plan [G]:** Drei Pflicht-Flüge der Klasse 8 Gymnasium sind herausgenommen (`r4` Kreis und Zylinder, `r2` Körper und Netze, `d5` Laplace), ebenso drei der Klasse 7 (`ge4`, `ge5`, `d10`). Ob das Absicht des Lehrers war, weiß ich nicht. Ohne sie fehlt Kind 2 am Ende der Klasse 8 die gesamte Raumgeometrie, die Kreisberechnung und die Wahrscheinlichkeit.

## 3. Umfang

Zahlen je Abschnitt und je Jahrgang stehen in `route.md` (gezählt von `plan.py`). Zusammengefasst [G]:

| | Flüge | Etappen | davon Klasse 5 / 6 / 7 / 8 / 9 (Jahrgang des Flugs in der App) |
|---|---|---|---|
| Kind 1, Route gesamt | 25 | 223 | 112 / 82 / 12 / 6 / – (dazu 11 ohne Jahrgang, IB) |
| Kind 2, Route gesamt | 29 | 230 | – / – / 59 / 108 / 63 |

Das sind **alle** Etappen der Flüge, nicht die noch offenen. Wie viele davon schon gelandet sind, sage ich dem Nutzer direkt, nicht hier.

**Lerntage [A]:** Ich rechne mit 1,5 neuen Etappen je Lerntag, weil zu den neuen Etappen Wiederholungen, die neuen Aufgabentypen und drei Tisch-Sitzungen je Woche kommen. Die Tabellen in `route.md` zeigen daneben 1 und 2 Etappen je Lerntag. Bei 1,5: Kind 1 etwa 75 Lerntage für Klasse 5 (ohne schon Gelandetes weniger), Kind 2 etwa 110 Lerntage für die Abschnitte 1 bis 4. Das ist eine Schätzung aus der Zahl der Etappen, keine Messung.

## 4. Kreuzungen beider Kinder (gemeinsame Tischzeit)

| Regel | Kind 1 | Kind 2 | liegt in |
|---|---|---|---|
| 7 Waage, 8 Umkehren | `a1` Einfache Gleichungen: □ − 38 = −15 | `a5` Bruchgleichungen, Formeln nach einer Größe auflösen | Abschnitt 1 bei beiden |
| 12 Potenz | `z1` Potenzen (Basis, Hochzahl) | `a5` Potenzgesetze mit negativen Hochzahlen | Abschnitt 1 bei beiden |
| 1 Richtung, 2 Zeichen-Paar | `z1` Rechnen mit negativen Zahlen | `a4` Ungleichungen: mal eine negative Zahl dreht das Zeichen | Abschnitt 1 bei beiden |
| Winkel | `ge3` Winkel messen und zeichnen | `ge4` Winkelsätze begründen | Kind 1 Abschnitt 2, Kind 2 Abschnitt 1 |
| 14 Verhältnis | `g2` Dreisatz | `f2` Steigung, `g7` indirekte Proportionalität | Abschnitt 2 bei beiden |
| Formel-Koffer Fläche | `r1` Rechteck | `r4` Kreis | Kind 1 Abschnitt 2, Kind 2 Abschnitt 3 |
| Zählen und Zufall | `d2` Zählen | `d5` Laplace (günstige durch mögliche) | Kind 1 Abschnitt 2, Kind 2 Abschnitt 2 |
| 10 Wert bleibt, 11 Bruchrechnen | `z3`, `z5` Brüche | Bruchterme (Wiederholung) | Kind 1 Abschnitt 4 |

Am besten trifft es sich in Abschnitt 1: Beide arbeiten an Waage und Umkehren. Dort passt, dass das ältere Kind dem jüngeren die Umkehraufgabe erklärt (`denkpapier-grundregeln.md`, Frage 10).

## 5. Prüfpunkte

| Zeitpunkt | Kind 1 | Kind 2 |
|---|---|---|
| vor Abschnitt 1 | Papier-Test Blatt A (Auftrag 5) | Papier-Test Blatt A und ein ganzer amtlicher Jahrgangsstufentest 8 (Eingangsdiagnose Klasse 5 bis 7) |
| nach Abschnitt 1 | **Blatt B** (Auftrag 5) | **Blatt B** (Auftrag 5) |
| nach Abschnitt 2 | Papier-Test „Messen“ – noch zu bauen | zweiter amtlicher Jahrgang, Vergleich mit dem ersten |
| nach Abschnitt 3 | Abschluss-Arbeit Klasse 5 – noch zu bauen | Abschluss-Arbeit Klasse 8 – noch zu bauen |
| nach Abschnitt 4 / 5 | Papier-Tests „Brüche“ und Abschluss Klasse 6 – noch zu bauen | Papier-Test „Wurzeln und quadratische Gleichungen“ – noch zu bauen |

Blatt B deckt die Themen ab, die vor Abschnitt 1 gelernt wurden. Nach Abschnitt 1 ist der Abstand zu Blatt A groß genug, und der Stoff ist nicht mehr frisch – genau das soll Blatt B messen.

## 6. Zweifel an Lehrplan-Zuordnungen

**Widersprüche zwischen `inhalte/themenliste.json` und der App [G]:**
- `geometrie.winkel`: Themenliste Gymnasium 5, App Gymnasium 7 (der Flug `ge3` steht aber als Klasse 5).
- `finanzen.zinsen`: Themenliste Gymnasium 6, App ohne Gymnasium-Zuordnung (Flug `g4` als Klasse 6).
- `zahlen.intervalle`: Themenliste Gymnasium 8, App ohne Gymnasium-Zuordnung.
- `stochastik.grundbegriffe`: Themenliste Realschule 9, App Realschule 8 (Teil 2: 9).

**Zuordnungen, an denen ich zweifle [A – keine an der Quelle nachgeschlagen]:**
- Realschule: `abbildungen.determinanten2` in Klasse 7 · `terme.potenzgesetze_ganzzahlig` in Klasse 7 · `raum.schraegbilder` in Klasse 7 (Gymnasium angeblich erst 10) · `messen.koerper_darstellung` in Klasse 5 bei Gymnasium 8 · `gleichungen.ungleichungen` und `groessen.indirekt` in Klasse 7.
- Gymnasium: `geometrie.ortslinien` in Klasse 5 · `trigo.allgemein` und `funktionen.potenz` in Klasse 9.
- IB: `zahlen.wurzeln_basis` in Jahr 1.

Folge für den Plan: Flüge, die **nur** über eine zweifelhafte Realschul-Zuordnung in den Plan kämen, sind Kür oder stehen hinten (`ge9`, `r5`). Wo Gymnasium und Realschule dieselbe Klasse nennen, hängt der Plan nicht an der Zuordnung.

## Nicht geprüft

- Keine Lehrplan-Stelle an der Quelle (LehrplanPLUS, IB) nachgeschlagen; Klassen laut App.
- Die Voraussetzungen in `plan.py` stammen aus meiner Kenntnis des Stoffs, nicht aus der Tabelle der App.
- Ob „herausgenommen“ beim Lehrer Absicht war.
- Ob die App einen Flug mit ausgelassenem Thema (`r2` ohne `messen.prisma_zylinder`) für Kind 1 sauber führt.
- Die Papier-Tests mit „noch zu bauen“ gibt es nicht.
- Lerntage: Schätzung, nicht gemessen.

## Annahmen

- Je Klasse lernt ein Kind.
- „Kann schon“ und „fertig“ in der App geben den wirklichen Stand wieder.
- IB-MYP-Jahr 1 entspricht etwa Klasse 6; die Kinder brauchen den IB-Stand erst nach Klasse 8.
- Klasse 9 ist für Kind 2 Vorgriff, kein Ziel dieses Schuljahrs.
