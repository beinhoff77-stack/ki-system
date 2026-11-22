# LK-D – ein Thema in mehreren Klassen: Daten und Aufbau-Prüfung (22.11.2026)

**Nachtrag 22.11. (LK-D 2):** Audit an den Klassenübergängen mit drei neuen Etappen (101 `cavalieri`, 91 `koerper_symmetrie`, 29 `gleichungen_binomisch`); Zuordnung, JSON und SQL angepasst. Siehe `lk_teilung_2211.md`, Abschnitt 1.

Bau-Auftrag LK, Abschnitt LK-D, mit den Nachträgen „vorhandener Lernstand der Kinder“ (14:20) und „Route: zweiter Teil fliegt ins Nachbarland“ (14:25).

- Datenbank nur gelesen (Stand nach dem Live vom 22.11.), nichts eingespielt.
- Keine Lehrplantexte wörtlich, nur Lernbereichstitel und eigene Kurzbeschreibungen.
- Kinderdaten nur als Nummern.

**Lieferung**
- dieser Bericht;
- `lk_daten_2211.json`: je Punkt Quelle, Lernbereich, Punkt, Thema, Bezug, Rolle, Etappen und neue Etappen. Dazu Lage je Thema und Spur, Aufbau-Ketten, Verstöße, Teilungsliste, Grenzfälle und Stand je Kind;
- `lk_korrektur_2211.sql`: Gymnasium und IB, dazu ein kleiner Nachtrag für die Realschule (nur Gruppe I und RS 5/6). Nur INSERT und UPDATE, Probelauf bestanden;
- neue Lernkarten für die Lücken aus LP-RS: `inhalte/generatoren/_lk_etappen_2211.py`, in fünf Generatoren eingehängt;
- Klassen im Repo nachgezogen (Themendateien und Generatoren).

## Kurzergebnis

| | Gymnasium 5–10 | Realschule 5–10 (I und II/III) | IB MYP 1–5 (Orientierung) |
|---|---|---|---|
| Punkte in der DB | 237 | 297 | 158 Kapitel |
| Punkte mit gültigem Hauptthema vorher | 103 | 292 (Stand LP-RS-Vorschlag) | 142 (dazu 14 auf stillgelegten Themen) |
| Punkte mit Hauptthema nachher | **237** | **297** | 156 (2 Wiederholungskapitel ohne eigenen Inhalt) |
| umgehängt | 10 | 3 Lücken geschlossen, 2 Lücken über Thema 15, 1 Tausch (944) | 6, dazu 14 weg von stillgelegten Themen |
| Lücken nachher | 0 | 0 (alle 5 aus LP-RS geschlossen) | 0; 1 Kapitel nur teilweise (Dreiecksarten) |
| Rolle neu / weitergeführt | 236 / 1 | 251 / 46 | 112 / 44 |
| Voraussetzungs-Verstöße | **0** | Gruppe I: 0 · II/III: 2 (empfohlen) | 10 je Kurs (2 davon hart; berichtigt am 22.11., vorher fälschlich 3) |
| Klassenänderung durch das SQL | keine | keine | keine |

**Wichtigste Befunde**
1. **Im Gymnasium hatte mehr als die Hälfte der Punkte kein Hauptthema (134 von 237).** Die Kinder lernen nach dem Gymnasium, deshalb wiegt das schwer. Jetzt hat jeder Punkt eines; die Klassen ändern sich dadurch nicht (simuliert und im Probelauf geprüft).
2. **Nach der Regel von 14:25 wird kein Thema geteilt.** Maßstab ist das Gymnasium, und dort liegt jedes Thema in genau einer Klasse. Eine Ausnahme ist 101 Prismen und Zylinder mit 8 und 10, aber Klasse 10 bringt keine neue Etappe.
   - Auch das Beispiel „Terme umformen“ (29) liegt im Gymnasium vollständig in Klasse 7.
   - Die drei neuen Etappen in RS 8 sind ein Grenzfall. Meine Empfehlung: nicht teilen (Abschnitt 5).
3. **Die Realschul-Lücken aus LP-RS sind alle geschlossen.**
   - Berichtigung zu LP-RS: Zahlensysteme stehen schon in Thema 15 (`dualsystem`, `roemisch_*`).
   - Für Vektoren in Koordinaten und Vektoren drehen gibt es neue Lernkarten in 46.
   - Dazu vier neue Etappen: Drachen/Raute, wahre Größe, Vierecke konstruieren, Streckung mit Vektoren.
4. **Lernstand der Kinder:**
   - Kein Kind hat ein Thema „geschafft“, bei dem in seiner Spur (Gymnasium) Etappen einer späteren Klasse fehlen.
   - Kein Thema mit Lernstand der Kinder ist im Gymnasium auf mehrere Klassen verteilt.
   - Für die Grenzfälle steht der Stand je Kind in Abschnitt 5.

## 1 Original gegen DB (Gymnasium neu, IB als Orientierung)

**Gymnasium 5–10** (LehrplanPLUS, alle sechs Seiten am 22.11. neu abgerufen; Zählung der Punkte über die Abruf-Zusammenfassung):
- **Stunden:** stimmen in allen Lern- und Unterbereichen.
  - 5: 30 (12/18), 14, 34 (20/14), 34 (18/16).
  - 6: 68 (13/11/15/14/15), 24 (12/12), 20.
  - 7: 37 (13/24), 21 (12/9), 17, 8, 29.
  - 8: 8, 16, 13, 13, 14, 10, 10.
  - 9: 17, 36 (18/18), 8, 14, 9, 11, 17 (9/8).
  - 10: 18, 15, 17, 12, 22.
- **Titel:** Alle Lernbereichstitel stimmen mit dem Original überein; anders als in der Realschule ist hier nichts umbenannt. Das SQL setzt die Lern- und Unterbereiche auf „geprüft“.
- **Zahl der Punkte:** Die DB teilt feiner als das Original (Original/DB): 5: 39/38 · 6: 33/46 · 7: 32/39 · 8: 27/39 · 9: 31/47 · 10: 26/28.
  - Gym 5 3.1 hat in der DB einen Punkt weniger. Der Inhalt „Rechengesetze für Rechenvorteile“ steckt in 3.2/k3, es fehlt also nichts.
  - Je Lernbereich stehen die Zahlen in den Tabellen (Abschnitt 6). Die Punkte selbst setzt das SQL deshalb nicht auf „geprüft“.
- **Zweitquelle:**
  - [mathe.delta 5, Stoffverteilung](https://www.ccbuchner.de/_files_media/mediathek/downloads/2431.pdf) (C.C. Buchner) bestätigt Lernbereiche und Stunden von Gym 5.
  - Für 6–10 sind die zugelassenen Bände mit Zulassungsnummer belegt: [mathe.delta 6](https://www.ccbuchner.de/produkt/mathe-delta-bayern-6-3235) (198/18-G+), [7](https://www.ccbuchner.de/produkt/mathe-delta-bayern-7-3683) (153/19-G+), [8](https://www.ccbuchner.de/produkt/mathe-delta-bayern-8-3684) (71/20-G+).
  - Die Stoffverteilungspläne für 6–10 habe ich nicht gelesen (**offen**). Ein Abruf außerhalb der Suchergebnisse hätte eine Freigabe gebraucht, und die Freigabe blieb unbeantwortet.

**IB MYP 1–5:**
- Es gibt **keinen amtlichen Jahresplan**. Das IB legt nur Rahmen und zwei Niveaus fest (Standard/Extended); die Kurse gestalten die Schulen selbst ([IB, MYP-Kurzinfo Mathematik](https://www.ibo.org/globalassets/new-structure/brochures-and-infographics/pdfs/myp-brief-mathematics-en.pdf)).
- Unsere Quellen sind Schulbuch-Inhaltsverzeichnisse (Oxford MYP 1–3, Pearson 4&5 Standard/Extended) und gelten nur als **Orientierung**.
- Die hinterlegten Verzeichnisse konnte ich nicht neu abrufen (Freigabe für den Abruf offen). Geprüft ist deshalb der DB-Stand: 158 Kapitel, jedes Kapitel ein „Punkt“.

## 2 Zuordnung, Rolle und Etappen je Punkt (alle drei Schularten)

- Jeder Punkt hat jetzt ein Hauptthema und die Etappen, die er verlangt (Lernziel-Schlüssel aus `inhalte/themen`). „Ganzes Thema“ kommt nicht vor.
- Nebenbezüge tragen keine Etappen.
- **Rolle:** „neu“ in der ersten Klasse, in der das Thema in dieser **Spur** ein Hauptthema ist; danach „weitergeführt“. Die Spuren sind:
  - Gymnasium;
  - RS Gruppe I und RS Gruppe II/III, jeweils mit RS 5/6 als gemeinsamem Anfang;
  - IB Standard und IB Extended, jeweils mit MYP 1–3 als gemeinsamem Anfang.
- `etappen_neu_in_dieser_klasse` nennt, was dazukommt.
- **Realschule:** Die Etappenzuordnung ist jetzt für alle 297 Punkte da (bisher nur für Themen mit Klassenwechsel).
  - Hauptthemen wie im LP-RS-Vorschlag, mit sechs Ausnahmen (Nachtrag im SQL, nur Gruppe I und RS 5/6):
    - 297/298 (Zahlensysteme RS 5) → 15 (`dualsystem`, `roemisch_schreiben`, `roemisch_system`); die LP-RS-Meldung „kein Thema“ war falsch;
    - 871 (Vektoren in Koordinaten 7 I) → 46 `vektor_koordinaten` (neu);
    - 937 (Vektoren drehen 8 I) → 46 `vektor_drehen` (neu);
    - 944 (8 I Funktionen, Darstellungswechsel) → 32 statt 33, wie 8 II/III 5/K2;
    - 820 (10 I Steigungswinkel) bekommt 55 als Nebenbezug (Etappe `schnittwinkel`).
  - 909 (7 II/III) → 46 `vektor_koordinaten` nur in der JSON; Gruppe II/III bleibt laut Entscheidung von 13:45 Bericht.
- **Gymnasium:**
  - 134 Punkte bekamen ihr erstes Hauptthema.
  - 10 umgehängt, je mit Grund:
    - Ortslinien → 73;
    - Potenzen von Brüchen → 23;
    - Zehnerpotenzen negativ → 19;
    - Oberfläche Gym 6 → 99;
    - Potenzgesetze 7 → 102;
    - Potenzgesetze 8 → 103;
    - quadratische Bruchgleichungen → 8;
    - Gym 10 Schrägbilder/Rotationskörper → 91;
    - schiefe Prismen → 101 statt 53.
  - Bewusst **nicht** umgehängt: Die Gleichungspunkte in Gym 5 (1.2/k3, 3.1/k6) bleiben bei Thema 1, weil ein Kind in Gym 5 lernt. Die gleichwertigen Etappen `umkehraufgabe` (16) und `umkehraufgabe_mal` (18) stehen als Nebenbezug.
- **IB:**
  - 14 Kapitel hingen an stillgelegten Themen (27 Verhältnisse, 83 Mengen, 41 Folgen, 82 bedingte Wahrscheinlichkeit). Sie hängen jetzt an 21, 26, 63 und 76; die alten Zeilen werden als „klaerungsbedarf“ markiert, nicht gelöscht.
  - 6 umgehängt: Dreieckswinkel → 98, Ganzzahl-Multiplikation → 18, Zylinder → 52, Parkettierung → 98, Körper 4/5 → 92 statt 53 (2×).

## 3 Aufbau: Was baut worauf auf

**a) Voraussetzungen gegen die neue Lage** (`schule.voraussetzung`, 128 Einträge; stillgelegte Themen ausgenommen):
- **Gymnasium: 0 Verstöße. RS Gruppe I: 0.**
- RS II/III, 2 (beide empfohlen), jeweils ist die Voraussetzung in II/III kein Lehrplanstoff:
  - 37 Exponentialfunktionen ← 103 Potenzgesetze ganzzahlig;
  - 92 Pyramide/Kegel/Kugel ← 101 Prismen und Zylinder.
  - Vorschlag: Voraussetzung für II/III auf „empfohlen, wenn vorhanden“ oder die Lage prüfen.
- IB, je Kurs 10; davon 2 hart (63 ← 61, 29 ← 102), siehe Tabelle.

| IB | Thema | braucht | Art | Lage | Vorschlag |
|---|---|---|---|---|---|
| MYP 1 | 63 Verknüpfte Ereignisse (Mengen-Etappen) | 61 Zufall und Laplace (MYP 2) | hart | Voraussetzung später | Mengen-Etappen von 63 hängen nicht an 61 → Voraussetzung nur für die Wahrscheinlichkeits-Etappen (Etappenebene) |
| MYP 1 | 29 Terme umformen | 102 Potenzgesetze (kein IB-Hauptpunkt) | hart | nicht Lehrplanstoff | **Sebastians harte Entscheidung nur melden**; IB-Lage von 102 prüfen |
| MYP 1 | 23 Rechnen mit rationalen Zahlen | 16 Ganze Zahlen (MYP 2) | empfohlen | später | Lage prüfen (Oxford 1 bringt Bruchrechnen vor ganzen Zahlen) |
| MYP 1 | 100 / 101 Volumen | 25, 99, 51 (MYP 2) | empfohlen | später | Lage prüfen; 100/101 haben keine IB-Klasse |
| MYP 2 | 44 Konstruktionen | 46 Kongruenzabbildungen (MYP 3) | empfohlen | später | Voraussetzung ändern (Konstruktion geht ohne Abbildungen) |
| MYP 4 | 34, 37, 45 | 93, 103, 73 | empfohlen | nicht Lehrplanstoff | Voraussetzung für IB weich machen |

**b) Etappen innerhalb eines Themas:**
- Eine „weitergeführt“-Etappe darf nur auf Etappen aufbauen, die früher neu sind. Inhaltliche Abhängigkeiten zwischen Etappen sind im Repo nicht hinterlegt. Geprüft habe ich deshalb die **Reihenfolge der Lernkarten** gegen die Klassenlage.
- 87 Stellen, an denen eine Karte weiter hinten im Thema in einer früheren Klasse verlangt wird (Liste in der JSON). Beispiele in RS Gruppe I:
  - 46: `drehung` (Kl. 8) steht vor `symmetrie` (Kl. 6);
  - 29: `summe_mal_summe` (Kl. 8) vor `aequivalenz` (Kl. 7);
  - 26: `vervielfachen` (Kl. 6) vor `dreisatz` (Kl. 5).
- Das ist kein Fehler im Lernstand. Vorschlag an Gestalter und App: Karten eines Themas in der Klassenzeile nach `klasse_ab` sortieren.

**c) Aufbau-Kette je Thema:** für jede Spur in `aufbau_kette` (JSON), fertig für die Anzeige, z. B. für RS Gruppe I:
- 29 Terme umformen: baut auf Terme aufstellen und deuten (Kl. 6, hart); Potenzgesetze (Kl. 7, hart) · neu in Kl. 7 · wird weitergeführt in Kl. 8: Summe mal Summe, binomische Formeln, Ausklammern.
- 46 Kongruenzabbildungen: baut auf Grundbegriffe (Kl. 5) · neu in Kl. 6 · weitergeführt in Kl. 7: Verschiebung, Gegenvektor, Vektoren in Koordinaten; Kl. 8: Drehung, Punktspiegelung, Vektoren drehen.

**d) Kein Pflichtstoff dieser Schulart oder Gruppe** (kein Hauptpunkt in der Spur; vollständig in `kein_pflichtstoff`):
- **Gymnasium (17):**
  - 13, 49, 59, 65, 66, 70, 74, 75, 76, 79, 80, 81, 84, 97;
  - dazu 43 Mit Winkeln rechnen, 69 Intervalle und 71 Zinsen, die im Gymnasium nur als Nebenbezug vorkommen. Ihre Gym-Klasse (5, 8, 6) kommt allein aus diesem Nebenbezug, und **die Kinder sehen sie heute als Gym-Thema**. Vorschlag: so lassen und als „Vertiefung“ kennzeichnen (Entscheidung Sebastian).
- **RS Gruppe I (22):** u. a. 4, 7, 9, 11, 34, 39, 63, 64, 68, 101, 103.
- **RS II/III (27):** zusätzlich 13, 14, 36, 49, 96.
- **IB:** rund 40 je Kurs. Die Schulbuch-Verzeichnisse sind grob, viele Themen kommen dort nur als Teil eines Kapitels vor. Das ist eine Orientierung, keine Lücke.

## 4 Lücken: neue Inhalte

Alle Inhalte sind selbst formuliert und alle Lösungen berechnet. Das Prüfskript meldet für alle Themendateien OK, die App-Tests laufen mit 164/164.
- Die neuen Lernkarten sind **Vertiefung** (`bewertung.lernziele_vertiefung`). Flug, Flug-Test und Stempel der bestehenden Themen ändern sich nicht.
- Ob eine Karte in einer Klasse Pflicht ist, regelt künftig `zuordnung.etappen` (LK-S).
- Die neuen Karten hängen an der Themendatei; neu erzeugt werden die Dateien über die fünf Generatoren. Die Generatoren erzeugen die Dateien danach unverändert (alle fünf geprüft).

| Thema | neue Lernkarte | für | Aufgaben |
|---|---|---|---|
| 46 Kongruenzabbildungen | `vektor_koordinaten` Vektoren in Koordinaten | RS 7 I 2/K4, 7 II/III 2/K4 (bisher Lücke) | 22 |
| 46 Kongruenzabbildungen | `vektor_drehen` Vektoren um 90° und 180° drehen | RS 8 I 2/K5 (bisher Lücke) | 22 |
| 47 Ähnlichkeit | `streckung_vektor` Strecken mit Vektoren | RS 9 I 2/K5 (teilweise) | 22 |
| 44 Konstruktionen | `vierecke_konstruieren` Vierecke konstruieren | RS 8 I 1/K2, 8 II/III 1/K5 (teilweise) | 22 |
| 99 Flächen von Vielecken | `drachen_raute` Drachenviereck und Raute | RS 6 3/k2 (teilweise) | 22 |
| 91 Schrägbilder | `wahre_groesse` Wahre Größe im Schrägbild | RS 7 I 4/K3, 8 II/III 2/K2 (teilweise) | 22 |

Je Karte gibt es 12 Übungen (Stufe 1–3, alle Aufgabentypen nach Bau-Auftrag F), 1 Test, 3 Korrektur und 6 Sicherung. Die Kann-Sätze stehen in `inhalte/kann`.

**Neue Lücken aus Gymnasium und IB:**
- Gymnasium: keine.
- IB: nur teilweise das Kapitel „Dreiecksarten“ (O1:4.4); es gibt keine eigene Etappe zum Einteilen von Dreiecken. Vorschlag: Etappe in 42 oder 44.
- Klassen-Befund IB: Volumen und Trapez (MYP 1/2) liegen in den Themen 99, 100 und 101, die keine IB-Klasse haben (`ib_myp` = null in `klasse_fest`). Hauptthema bleibt deshalb 53/50, Nebenbezug 99/100/101.

## 5 Teilen nach der Regel von 14:25 und Grenzfälle

**Regel:** Verlangt der Lehrplan in einer späteren Klasse mindestens 3 eigene Etappen, wird das Thema geteilt. Maßstab ist das Gymnasium, ohne Gym-Klasse RS Gruppe I, dann IB.

**Ergebnis: Kein Thema erfüllt die Regel.** Im Gymnasium liegt jedes Thema mit Hauptpunkt in genau einer Klasse; nur 101 hat 8 und 10, aber 10 bringt keine neue Etappe. Zu teilen gibt es also nichts (Potenzgesetze 102/103 sind schon geteilt).

**Grenzfälle** (andere Lage in RS oder IB). Stand je Kind als „erledigt/verlangt“; erledigt heißt gelandet, gesetzt oder nachgewiesen:

| Thema | Gymnasium | Lage anderswo | Kind 1 | Kind 2 | Empfehlung |
|---|---|---|---|---|---|
| 29 Terme umformen | Kl. 7, 8 Etappen | RS I und II/III: 7 (5 Et.) + 8 (3 Et.: Summe mal Summe, binomische Formeln, Ausklammern); IB 1, 2, 4 | 0/8 | 8/8 (Flug geschafft) | **zusammen lassen**: Nach dem Maßstab Gymnasium gibt es keinen zweiten Teil. Bei Teilung nach RS: Teil 1 „Terme umformen“ (7), Teil 2 „Terme multiplizieren und binomische Formeln“ (8), Kind 2 hätte beide Teile vollständig |
| 46 Kongruenzabbildungen | Kl. 7, 6 Et. | RS I: 6 (6) + 7 (3) + 8 (3); II/III: 6 + 7 | 0 | 0 | zusammen lassen; falls RS-Maßstab: Teil 2 „Vektoren und Verschiebung“ (7), Teil 3 „Drehung“ (8) |
| 61 Zufall und Laplace | Kl. 8, 6 Et. | RS: 8 (2) + 9 (4) | 0 | 0 | zusammen lassen (Gym 8 vollständig); RS zeigt „weitergeführt“ |
| 33 Lineare Funktionen | Kl. 8, 8 Et. | RS II/III: 8 (3) + 9 (6) | 0 | 0 | zusammen lassen; Gruppe II/III ist nur Bericht |
| 26 Proportionalität und Dreisatz | Kl. 5, 4 Et. | RS: 5 (2) + 6 (3) | 0 | 0 | zusammen lassen (genau 3 Etappen, nur RS) |
| 91 Schrägbilder | Kl. 10, 2 Et. | RS I: 7 (3) + 8 (3) | 0 | 0 | zusammen lassen; nach Einspielen von LP-RS ist RS 7 die erste Klasse |
| 8 Quadratische Gleichungen | Kl. 9, 7 Et. | RS II/III: 9 (1) + 10 (5) | 0 | 0 | zusammen lassen |
| 63 Verknüpfte Ereignisse | Kl. 9, 9 Et. | IB: 1 (4 Mengen-Etappen) + 4 (4) | 0 | 0 | zusammen lassen; IB-Mengen sind Orientierung |

Sebastian entscheidet die Liste. Bei „teilen“ gilt das Muster vom 21.11. (Lernstand je Etappe umhängen, Vorher/Nachher je Kind).

**Nachtrag Lernstand, Punkt 6** (nur Nummern, lesend, Spur Gymnasium):
- Themen mit Lernstand, die auf mehrere Gym-Klassen verteilt sind: **keine**.
- Kinder mit einem geschafften Thema, bei dem Etappen einer späteren Klasse fehlen: **keine**. Geschafft sind bei Kind 1 die Themen 15 und 16, bei Kind 2 die Themen 2, 29, 31 und 102.
- Hinweis für die Anzeige: Kind 2 hat in Thema 29 auch die drei Etappen, die die Realschule erst in 8 verlangt.

## 6 Tabellen je Schulart und Klasse

Spalten: Lernbereich · Titel · Stunden · Punkte Original/DB · Themen (neu/weiter) · Lücken.
- Gymnasium: Original-Zählung aus LehrplanPLUS 22.11.
- RS: aus LP-RS.
- IB: Kapitel als Punkte, ohne Stunden.

#### Gymnasium 5 (Quelle 1)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1.1 | Natürliche Zahlen und ihre Erweiterung zu den ganzen Zahlen | 12 | 7/7 | 15 Natürliche Zahlen (neu); 16 Ganze Zahlen (neu) | – |
| 1.2 | Addition und Subtraktion ganzer Zahlen | 18 | 5/5 | 16 Ganze Zahlen (neu); 1 Einfache Gleichungen (neu); 18 Grundrechenarten und Rechengesetze (neu) | – |
| 2 | Geometrische Figuren und Lagebeziehungen | 14 | 5/5 | 42 Grundbegriffe und Figuren (neu); 73 Ortslinien und Ortsbereiche (neu) | – |
| 3.1 | Multiplikation und Division ganzer Zahlen | 20 | 7/6 | 18 Grundrechenarten und Rechengesetze (neu); 17 Teilbarkeit (neu); 60 Zählen und Kombinatorik (neu); 67 Potenzen als Schreibweise (neu); 1 Einfache Gleichungen (neu) | – |
| 3.2 | Verbindung der Grundrechenarten bei ganzen Zahlen | 14 | 5/5 | 18 Grundrechenarten und Rechengesetze (neu) | – |
| 4.1 | Geld, Länge, Masse und Zeit | 18 | 5/5 | 25 Größen und Einheiten (neu); 26 Direkte Proportionalität und Dreisatz (neu) | – |
| 4.2 | Flächeninhalt | 16 | 5/5 | 50 Umfang und Flächeninhalt (neu); 53 Volumen und Oberfläche (neu) | – |

#### Gymnasium 6 (Quelle 2)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1.1 | Bruchteile und Bruchzahlen | 13 | 4/7 | 21 Brüche und Anteile (neu); 22 Dezimalzahlen (neu) | – |
| 1.2 | Dezimalbrüche | 11 | 3/6 | 22 Dezimalzahlen (neu); 21 Brüche und Anteile (neu) | – |
| 1.3 | Addition und Subtraktion rationaler Zahlen | 15 | 5/5 | 23 Rechnen mit rationalen Zahlen (neu) | – |
| 1.4 | Multiplikation und Division rationaler Zahlen | 14 | 3/5 | 23 Rechnen mit rationalen Zahlen (neu); 30 Potenzen und negative Exponenten (neu); 19 Zehnerpotenzen und wissenschaftliche Schreibweise (neu) | – |
| 1.5 | Verbindung der Grundrechenarten bei rationalen Zahlen | 15 | 4/5 | 23 Rechnen mit rationalen Zahlen (neu) | – |
| 2.1 | Flächeninhalt | 12 | 4/5 | 99 Flächen von Parallelogramm, Dreieck und Trapez (neu) | – |
| 2.2 | Volumen | 12 | 5/6 | 100 Volumen (neu) | – |
| 3 | Prozentrechnung, Daten und Diagramme | 20 | 5/7 | 24 Prozent- und Zinsrechnung (neu); 57 Daten erfassen und darstellen (neu); 58 Mittelwert und Häufigkeiten (neu) | – |

#### Gymnasium 7 (Quelle 3)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1.1 | Aufstellen und Interpretieren von Termen | 13 | 4/4 | 28 Terme aufstellen und deuten (neu) | – |
| 1.2 | Umformen von Termen | 24 | 5/6 | 102 Potenzgesetze (neu); 29 Terme umformen (neu) | – |
| 2.1 | Achsen- und punktsymmetrische Figuren | 12 | 3/5 | 46 Kongruenzabbildungen (neu) | – |
| 2.2 | Winkelbetrachtungen an Figuren | 9 | 4/5 | 98 Winkelsätze (neu) | – |
| 3 | Lineare Gleichungen und Vertiefung der Prozentrechnung | 17 | 4/6 | 2 Lineare Gleichungen (neu); 94 Vermehrter und verminderter Grundwert (neu) | – |
| 4 | Kenngrößen von Daten | 8 | 3/4 | 95 Median, Quartile, Boxplot (neu) | – |
| 5 | Kongruenz, besondere Dreiecke und Dreieckskonstruktionen | 29 | 9/9 | 44 Konstruktionen, Kongruenz und Beweise (neu); 45 Kreis und Tangenten (neu) | – |

#### Gymnasium 8 (Quelle 4)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1 | Funktion und Term | 8 | 3/6 | 32 Zuordnung und Funktion (neu) | – |
| 2 | Lineare Funktionen | 16 | 5/8 | 33 Lineare Funktionen (neu); 3 Lineare Ungleichungen (neu) | – |
| 3 | Elementare gebrochen-rationale Funktionen | 13 | 3/4 | 34 Gebrochen-rationale Funktionen (neu); 93 Indirekte Proportionalität (neu) | – |
| 4 | Bruchterme und Bruchgleichungen | 13 | 5/5 | 31 Bruchterme (neu); 103 Potenzgesetze mit ganzzahligen Exponenten (neu); 5 Bruch- und Verhältnisgleichungen (neu); 4 Formeln umstellen (neu) | – |
| 5 | Laplace-Experimente | 14 | 4/5 | 61 Zufall und Laplace (neu) | – |
| 6 | Lineare Gleichungssysteme | 10 | 3/4 | 6 Gleichungssysteme mit 2 Unbekannten (neu) | – |
| 7 | Kreis und Zylinder | 10 | 4/7 | 51 Kreisberechnungen (neu); 52 Körper darstellen (neu); 101 Prismen und Zylinder (neu) | – |

#### Gymnasium 9 (Quelle 5)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1 | Quadratwurzeln | 17 | 5/8 | 68 Elementare Wurzeln (neu); 20 Wurzeln und reelle Zahlen (neu) | – |
| 2.1 | Quadratische Funktionen und quadratische Gleichungen | 18 | 5/7 | 35 Quadratische Funktionen (neu); 8 Quadratische Gleichungen (allgemein) (neu) | – |
| 2.2 | Quadratische Funktionen in Anwendungen | 18 | 3/5 | 7 Gleichungssysteme mit 3 Unbekannten (neu); 35 Quadratische Funktionen (neu); 8 Quadratische Gleichungen (allgemein) (neu) | – |
| 3 | Wahrscheinlichkeit verknüpfter Ereignisse | 8 | 2/5 | 63 Verknüpfte Ereignisse (neu) | – |
| 4 | Ähnlichkeit und Strahlensatz | 14 | 3/4 | 47 Ähnlichkeit und Strahlensätze (neu) | – |
| 5 | Potenzfunktionen mit natürlichen Exponenten und Erweiterung des Potenzbegriffs | 9 | 4/5 | 36 Potenzfunktionen (neu); 9 Potenzgleichungen (neu); 96 Rationale Exponenten und n-te Wurzel (neu) | – |
| 6 | Satz des Pythagoras | 11 | 3/3 | 54 Satz des Pythagoras (neu) | – |
| 7.1 | Trigonometrie am rechtwinkligen Dreieck | 9 | 4/4 | 55 Trigonometrie im rechtwinkligen Dreieck (neu) | – |
| 7.2 | Sinus- und Kosinussatz | 8 | 2/6 | 56 Allgemeine Trigonometrie (neu); 14 Trigonometrische Gleichungen (neu) | – |

#### Gymnasium 10 (Quelle 6)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1 | Exponentielles Wachstum und Logarithmus | 18 | 5/5 | 37 Exponential- und Logarithmusfunktionen (neu); 10 Exponentialgleichungen (neu) | – |
| 2 | Zusammengesetzte Zufallsexperimente und stochastische Simulationen | 15 | 4/4 | 62 Mehrstufige Zufallsexperimente (neu); 64 Simulation (neu) | – |
| 3 | Sinus- und Kosinusfunktion | 17 | 7/7 | 38 Sinus- und Kosinusfunktion (neu) | – |
| 4 | Ganzrationale Funktionen | 12 | 3/4 | 39 Ganzrationale Funktionen (neu); 11 Polynomgleichungen (neu) | – |
| 5 | Fortführung der Raumgeometrie | 22 | 7/8 | 91 Schrägbilder und Raumdarstellung (neu); 92 Pyramide, Kegel, Kugel (neu); 101 Prismen und Zylinder (weiter) | – |
#### Realschule 5 (Quelle 7)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1.1 | Natürliche Zahlen im Dezimalsystem | – | 4/4 | 15 Natürliche Zahlen (neu) | – |
| 1.2 | Andere Zahlensysteme | – | 1/2 | 15 Natürliche Zahlen (neu) | – |
| 1.3 | Grundrechenarten und Rechengesetze | – | 6/6 | 18 Grundrechenarten und Rechengesetze (neu); 67 Potenzen als Schreibweise (neu); 17 Teilbarkeit (neu) | – |
| 1.4 | Kombinatorik | – | 1/2 | 60 Zählen und Kombinatorik (neu) | – |
| 2 | Ganze Zahlen | 20 | 5/7 | 16 Ganze Zahlen (neu) | – |
| 3 | Geometrische Grundvorstellungen und Grundbegriffe | 30 | 6/9 | 42 Grundbegriffe und Figuren (neu); 52 Körper darstellen (neu) | – |
| 4 | Größen | 20 | 6/6 | 25 Größen und Einheiten (neu); 26 Direkte Proportionalität und Dreisatz (neu) | – |
| 5 | Umfang und Flächeninhalt ebener Figuren | 15 | 6/6 | 50 Umfang und Flächeninhalt (neu) | – |
| 6 | Auswertung von Daten | 5 | 3/3 | 57 Daten erfassen und darstellen (neu) | – |

#### Realschule 6 (Quelle 8)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1 | Rationale Zahlen | 68 | 10/12 | 21 Brüche und Anteile (neu); 22 Dezimalzahlen (neu); 23 Rechnen mit rationalen Zahlen (neu) | – |
| 2 | Achsenspiegelung und Symmetrie | 13 | 5/5 | 46 Kongruenzabbildungen (neu) | – |
| 3 | Flächeninhalt ebener Figuren | 18 | 4/6 | 99 Flächen von Parallelogramm, Dreieck und Trapez (neu); 53 Volumen und Oberfläche (neu) | – |
| 4 | Raumgeometrie | 14 | 2/4 | 100 Volumen (neu) | – |
| 5 | Terme und Gleichungen | 15 | 7/7 | 28 Terme aufstellen und deuten (neu); 1 Einfache Gleichungen (neu) | – |
| 6 | Direkte Proportionalität | 12 | 4/6 | 26 Direkte Proportionalität und Dreisatz (weiter); 24 Prozent- und Zinsrechnung (neu) | – |

#### Realschule 7 – Gruppe I (Quelle 24)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1 | Potenzen | 10 | 3/3 | 30 Potenzen und negative Exponenten (neu); 102 Potenzgesetze (neu); 19 Zehnerpotenzen und wissenschaftliche Schreibweise (neu) | – |
| 2 | Parallelverschiebung | 23 | 7/7 | 46 Kongruenzabbildungen (weiter); 74 Zweireihige Determinanten (neu); 98 Winkelsätze (neu) | – |
| 3 | Dreiecke | 14 | 4/4 | 44 Konstruktionen, Kongruenz und Beweise (neu) | – |
| 4 | Raumgeometrie | 10 | 3/3 | 91 Schrägbilder und Raumdarstellung (neu) | – |
| 5 | Geometrische Ortslinien und Ortsbereiche | 12 | 5/5 | 73 Ortslinien und Ortsbereiche (neu); 45 Kreis und Tangenten (neu) | – |
| 6 | Terme, Gleichungen und Ungleichungen | 22 | 4/4 | 29 Terme umformen (neu); 2 Lineare Gleichungen (neu); 3 Lineare Ungleichungen (neu) | – |
| 7 | Proportionalitäten | 12 | 5/5 | 94 Vermehrter und verminderter Grundwert (neu); 71 Zinsen (neu); 93 Indirekte Proportionalität (neu) | – |
| 8 | Auswertung von Daten | 9 | 4/4 | 58 Mittelwert und Häufigkeiten (neu); 95 Median, Quartile, Boxplot (neu); 81 Stichproben und Aussagekraft (neu); 57 Daten erfassen und darstellen (weiter) | – |

#### Realschule 7 – Gruppe II/III (Quelle 25)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1 | Potenzen | 10 | 3/3 | 30 Potenzen und negative Exponenten (neu); 102 Potenzgesetze (neu); 19 Zehnerpotenzen und wissenschaftliche Schreibweise (neu) | – |
| 2 | Parallelverschiebung | 21 | 7/7 | 46 Kongruenzabbildungen (weiter); 74 Zweireihige Determinanten (neu); 98 Winkelsätze (neu) | – |
| 3 | Geometrische Ortslinien und Ortsbereiche | 10 | 4/4 | 73 Ortslinien und Ortsbereiche (neu); 45 Kreis und Tangenten (neu) | – |
| 4 | Terme, Gleichungen und Ungleichungen | 22 | 4/4 | 29 Terme umformen (neu); 2 Lineare Gleichungen (neu); 3 Lineare Ungleichungen (neu) | – |
| 5 | Proportionalitäten | 12 | 5/5 | 94 Vermehrter und verminderter Grundwert (neu); 71 Zinsen (neu); 93 Indirekte Proportionalität (neu) | – |
| 6 | Auswertung von Daten | 9 | 4/4 | 58 Mittelwert und Häufigkeiten (neu); 95 Median, Quartile, Boxplot (neu); 81 Stichproben und Aussagekraft (neu); 57 Daten erfassen und darstellen (weiter) | – |

#### Realschule 8 – Gruppe I (Quelle 12)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1 | Vierecke | 12 | 2/2 | 46 Kongruenzabbildungen (weiter); 44 Konstruktionen, Kongruenz und Beweise (weiter) | – |
| 2 | Drehung | 6 | 5/5 | 46 Kongruenzabbildungen (weiter) | – |
| 3 | Raumgeometrie | 13 | 3/3 | 91 Schrägbilder und Raumdarstellung (weiter) | – |
| 4 | Terme, Gleichungen und Ungleichungen | 40 | 3/3 | 29 Terme umformen (weiter); 97 Quadratische Terme und Extremwerte (neu); 2 Lineare Gleichungen (weiter) | – |
| 5 | Bruchterme und Bruchgleichungen | 7 | 2/2 | 31 Bruchterme (neu); 5 Bruch- und Verhältnisgleichungen (neu) | – |
| 6 | Funktionen | 26 | 6/6 | 32 Zuordnung und Funktion (neu); 33 Lineare Funktionen (neu) | – |
| 7 | Daten und Zufall | 8 | 2/2 | 61 Zufall und Laplace (neu) | – |

#### Realschule 8 – Gruppe II/III (Quelle 26)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1 | Dreiecke und Vierecke | 16 | 5/5 | 44 Konstruktionen, Kongruenz und Beweise (neu); 46 Kongruenzabbildungen (weiter) | – |
| 2 | Raumgeometrie | 7 | 2/2 | 91 Schrägbilder und Raumdarstellung (neu) | – |
| 3 | Terme und Gleichungen | 40 | 3/3 | 29 Terme umformen (weiter); 97 Quadratische Terme und Extremwerte (neu); 2 Lineare Gleichungen (weiter) | – |
| 4 | Bruchterme und Bruchgleichungen | 5 | 2/2 | 31 Bruchterme (neu); 5 Bruch- und Verhältnisgleichungen (neu) | – |
| 5 | Funktionen | 8 | 5/5 | 32 Zuordnung und Funktion (neu); 33 Lineare Funktionen (neu) | – |
| 6 | Daten und Zufall | 8 | 2/2 | 61 Zufall und Laplace (neu) | – |

#### Realschule 9 – Gruppe I (Quelle 13)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1 | Reelle Zahlen | 10 | 3/3 | 20 Wurzeln und reelle Zahlen (neu); 8 Quadratische Gleichungen (allgemein) (neu) | – |
| 2 | Zentrische Streckung | 17 | 8/8 | 47 Ähnlichkeit und Strahlensätze (neu) | – |
| 3 | Rechtwinklige Dreiecke | 20 | 6/6 | 54 Satz des Pythagoras (neu); 55 Trigonometrie im rechtwinkligen Dreieck (neu) | – |
| 4 | Kreis | 10 | 2/2 | 51 Kreisberechnungen (neu) | – |
| 5 | Raumgeometrie | 20 | 4/4 | 92 Pyramide, Kegel, Kugel (neu) | – |
| 6 | Systeme linearer Gleichungen | 12 | 1/1 | 6 Gleichungssysteme mit 2 Unbekannten (neu) | – |
| 7 | Quadratische Funktionen und quadratische Gleichungen | 42 | 9/9 | 35 Quadratische Funktionen (neu); 8 Quadratische Gleichungen (allgemein) (neu); 13 Wurzelgleichungen (neu) | – |
| 8 | Daten und Zufall | 9 | 5/5 | 61 Zufall und Laplace (weiter) | – |

#### Realschule 9 – Gruppe II/III (Quelle 14)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1 | Reelle Zahlen | 7 | 3/3 | 20 Wurzeln und reelle Zahlen (neu); 8 Quadratische Gleichungen (allgemein) (neu) | – |
| 2 | Zentrische Streckung | 13 | 3/3 | 47 Ähnlichkeit und Strahlensätze (neu) | – |
| 3 | Rechtwinklige Dreiecke | 20 | 6/6 | 54 Satz des Pythagoras (neu); 55 Trigonometrie im rechtwinkligen Dreieck (neu) | – |
| 4 | Kreis | 10 | 2/2 | 51 Kreisberechnungen (neu) | – |
| 5 | Lineare Funktionen | 15 | 4/4 | 33 Lineare Funktionen (weiter) | – |
| 6 | Systeme linearer Gleichungen | 10 | 1/1 | 6 Gleichungssysteme mit 2 Unbekannten (neu) | – |
| 7 | Daten und Zufall | 9 | 5/5 | 61 Zufall und Laplace (weiter) | – |

#### Realschule 10 – Gruppe I (Quelle 15)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1 | Trigonometrie | 42 | 11/11 | 56 Allgemeine Trigonometrie (neu); 38 Sinus- und Kosinusfunktion (neu); 14 Trigonometrische Gleichungen (neu); 49 Matrizen und Abbildungen mit Matrizen (neu) | – |
| 2 | Abbildungen | 30 | 4/4 | 49 Matrizen und Abbildungen mit Matrizen (neu); 37 Exponential- und Logarithmusfunktionen (neu) | – |
| 3 | Potenzen und Potenzfunktionen | 16 | 4/4 | 96 Rationale Exponenten und n-te Wurzel (neu); 36 Potenzfunktionen (neu) | – |
| 4 | Exponentialfunktionen, Logarithmen und Logarithmusfunktionen | 22 | 3/3 | 10 Exponentialgleichungen (neu); 37 Exponential- und Logarithmusfunktionen (neu) | – |
| 5 | Daten und Zufall | 10 | 2/2 | 62 Mehrstufige Zufallsexperimente (neu) | – |

#### Realschule 10 – Gruppe II/III (Quelle 16)

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| 1 | Trigonometrie | 21 | 6/6 | 56 Allgemeine Trigonometrie (neu); 38 Sinus- und Kosinusfunktion (neu) | – |
| 2 | Raumgeometrie | 20 | 5/5 | 91 Schrägbilder und Raumdarstellung (weiter); 92 Pyramide, Kegel, Kugel (neu) | – |
| 3 | Exponentialfunktionen, Logarithmen | 10 | 3/3 | 10 Exponentialgleichungen (neu); 37 Exponential- und Logarithmusfunktionen (neu) | – |
| 4 | Quadratische Funktionen und quadratische Gleichungen | 35 | 6/6 | 35 Quadratische Funktionen (neu); 8 Quadratische Gleichungen (allgemein) (weiter) | – |
| 5 | Daten und Zufall | 10 | 2/2 | 62 Mehrstufige Zufallsexperimente (neu) | – |
#### IB MYP (Quelle 18, myp_beide) – Orientierung

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| O1:1 |  | – | –/9 | 15 Natürliche Zahlen (neu); 67 Potenzen als Schreibweise (neu); 17 Teilbarkeit (neu); 18 Grundrechenarten und Rechengesetze (neu) | – |
| O1:2 |  | – | –/5 | 24 Prozent- und Zinsrechnung (neu) | – |
| O1:3 |  | – | –/6 | 28 Terme aufstellen und deuten (neu); 29 Terme umformen (neu); 32 Zuordnung und Funktion (neu); 1 Einfache Gleichungen (neu) | – |
| O1:4 |  | – | –/5 | 42 Grundbegriffe und Figuren (neu); 43 Mit Winkeln rechnen (neu); 98 Winkelsätze (neu) | – |
| O1:5 |  | – | –/5 | 21 Brüche und Anteile (neu); 23 Rechnen mit rationalen Zahlen (neu) | – |
| O1:6 |  | – | –/5 | 57 Daten erfassen und darstellen (neu) | – |
| O1:7 |  | – | –/6 | 63 Verknüpfte Ereignisse (neu); 50 Umfang und Flächeninhalt (neu); 53 Volumen und Oberfläche (neu) | – |

#### IB MYP (Quelle 19, myp_beide) – Orientierung

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| O2:1 |  | – | –/5 | 21 Brüche und Anteile (weiter); 26 Direkte Proportionalität und Dreisatz (neu) | – |
| O2:2 |  | – | –/7 | 61 Zufall und Laplace (neu) | – |
| O2:3 |  | – | –/6 | 16 Ganze Zahlen (neu); 42 Grundbegriffe und Figuren (weiter); 18 Grundrechenarten und Rechengesetze (weiter) | – |
| O2:4 |  | – | –/8 | 28 Terme aufstellen und deuten (weiter); 29 Terme umformen (weiter); 2 Lineare Gleichungen (neu); 3 Lineare Ungleichungen (neu) | – |
| O2:5 |  | – | –/6 | 50 Umfang und Flächeninhalt (weiter); 51 Kreisberechnungen (neu); 53 Volumen und Oberfläche (weiter) | – |
| O2:6 |  | – | –/6 | 26 Direkte Proportionalität und Dreisatz (neu); 25 Größen und Einheiten (neu) | – |
| O2:7 |  | – | –/5 | 57 Daten erfassen und darstellen (weiter); 58 Mittelwert und Häufigkeiten (neu); 95 Median, Quartile, Boxplot (neu) | – |

#### IB MYP (Quelle 20, myp_beide) – Orientierung

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| O3:1 |  | – | –/4 | 20 Wurzeln und reelle Zahlen (neu); 30 Potenzen und negative Exponenten (neu); 19 Zehnerpotenzen und wissenschaftliche Schreibweise (neu) | – |
| O3:2 |  | – | –/3 | 33 Lineare Funktionen (neu) | – |
| O3:3 |  | – | –/4 | 6 Gleichungssysteme mit 2 Unbekannten (neu); 2 Lineare Gleichungen (weiter) | – |
| O3:4 |  | – | –/5 | 52 Körper darstellen (neu); 92 Pyramide, Kegel, Kugel (neu) | – |
| O3:5 |  | – | –/4 | 46 Kongruenzabbildungen (neu); 98 Winkelsätze (weiter); 47 Ähnlichkeit und Strahlensätze (neu) | – |
| O3:6 |  | – | –/4 | 44 Konstruktionen, Kongruenz und Beweise (weiter); 54 Satz des Pythagoras (neu); 55 Trigonometrie im rechtwinkligen Dreieck (neu) | – |
| O3:7 |  | – | –/4 | 59 Zweidimensionale Daten (neu) | – |

#### IB MYP (Quelle 21, myp_standard) – Orientierung

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| P45S:1 |  | – | –/1 |  | P45S:1 |
| P45S:2 |  | – | –/1 | 29 Terme umformen (weiter) | – |
| P45S:3 |  | – | –/1 | 32 Zuordnung und Funktion (weiter) | – |
| P45S:4 |  | – | –/1 | 33 Lineare Funktionen (weiter) | – |
| P45S:5 |  | – | –/1 | 6 Gleichungssysteme mit 2 Unbekannten (weiter) | – |
| P45S:6 |  | – | –/1 | 49 Matrizen und Abbildungen mit Matrizen (neu) | – |
| P45S:7 |  | – | –/1 | 35 Quadratische Funktionen (neu) | – |
| P45S:8 |  | – | –/1 | 47 Ähnlichkeit und Strahlensätze (weiter) | – |
| P45S:9 |  | – | –/1 | 44 Konstruktionen, Kongruenz und Beweise (weiter) | – |
| P45S:10 |  | – | –/1 | 46 Kongruenzabbildungen (weiter) | – |
| P45S:11 |  | – | –/1 | 45 Kreis und Tangenten (neu) | – |
| P45S:12 |  | – | –/1 | 55 Trigonometrie im rechtwinkligen Dreieck (weiter) | – |
| P45S:13 |  | – | –/1 | 37 Exponential- und Logarithmusfunktionen (neu) | – |
| P45S:14 |  | – | –/1 | 92 Pyramide, Kegel, Kugel (weiter) | – |
| P45S:15 |  | – | –/1 | 56 Allgemeine Trigonometrie (neu) | – |
| P45S:16 |  | – | –/1 | 20 Wurzeln und reelle Zahlen (weiter) | – |
| P45S:17 |  | – | –/1 | 76 Reihen (neu) | – |
| P45S:18 |  | – | –/1 | 63 Verknüpfte Ereignisse (weiter) | – |
| P45S:19 |  | – | –/1 | 59 Zweidimensionale Daten (weiter) | – |
| P45S:20 |  | – | –/1 | 65 Graphentheorie (neu) | – |

#### IB MYP (Quelle 22, myp_extended) – Orientierung

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| P45E:1 |  | – | –/1 |  | P45E:1 |
| P45E:2 |  | – | –/1 | 29 Terme umformen (weiter) | – |
| P45E:3 |  | – | –/1 | 32 Zuordnung und Funktion (weiter) | – |
| P45E:4 |  | – | –/1 | 33 Lineare Funktionen (weiter) | – |
| P45E:5 |  | – | –/1 | 6 Gleichungssysteme mit 2 Unbekannten (weiter) | – |
| P45E:6 |  | – | –/1 | 49 Matrizen und Abbildungen mit Matrizen (neu) | – |
| P45E:7 |  | – | –/1 | 39 Ganzrationale Funktionen (neu) | – |
| P45E:8 |  | – | –/1 | 47 Ähnlichkeit und Strahlensätze (weiter) | – |
| P45E:9 |  | – | –/1 | 44 Konstruktionen, Kongruenz und Beweise (weiter) | – |
| P45E:10 |  | – | –/1 | 49 Matrizen und Abbildungen mit Matrizen (neu) | – |
| P45E:11 |  | – | –/1 | 45 Kreis und Tangenten (neu) | – |
| P45E:12 |  | – | –/1 | 55 Trigonometrie im rechtwinkligen Dreieck (weiter) | – |
| P45E:13 |  | – | –/1 | 37 Exponential- und Logarithmusfunktionen (neu) | – |
| P45E:14 |  | – | –/1 | 92 Pyramide, Kegel, Kugel (weiter) | – |
| P45E:15 |  | – | –/1 | 56 Allgemeine Trigonometrie (neu) | – |
| P45E:16 |  | – | –/1 | 20 Wurzeln und reelle Zahlen (weiter) | – |
| P45E:17 |  | – | –/1 | 76 Reihen (neu) | – |
| P45E:18 |  | – | –/1 | 63 Verknüpfte Ereignisse (weiter) | – |
| P45E:19 |  | – | –/1 | 79 Standardabweichung (neu) | – |
| P45E:20 |  | – | –/1 | 65 Graphentheorie (neu) | – |

#### IB MYP (Quelle 23, myp_beide) – Orientierung

| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |
|---|---|---|---|---|---|
| O45S:4 |  | – | –/2 | 63 Verknüpfte Ereignisse (weiter) | – |
| O45E:E4 |  | – | –/1 | 63 Verknüpfte Ereignisse (weiter) | – |
| P1:7 |  | – | –/1 | 28 Terme aufstellen und deuten (neu) | – |
| P2:8 |  | – | –/1 | 44 Konstruktionen, Kongruenz und Beweise (neu) | – |
| P3:5 |  | – | –/1 | 33 Lineare Funktionen (neu) | – |

## 7 Korrektur-SQL `lk_korrektur_2211.sql`

- **Reihenfolge:** **nach** `rs_korrektur_2211.sql` einspielen (Schritt 0 bricht sonst ab), in einer Transaktion (`psql -1`).
- **Inhalt:** Gymnasium 5–10 (Quellen 1–6) und IB (18–23), dazu der Realschul-Nachtrag für Gruppe I und RS 5/6 (Quellen 7, 8, 24, 12, 13, 15).
  - 31 Hauptbezüge werden zuerst Neben;
  - 18 veraltete Zuordnungen werden auf Neben mit „klaerungsbedarf“ gesetzt;
  - 13 Nebenbezüge werden zu Hauptbezügen;
  - 185 Zuordnungen kommen neu dazu, mit Rolle und Etappen in `begruendung`;
  - die Gymnasium-Lern- und Unterbereiche werden auf „geprüft“ gesetzt.
- **Erlaubte Befehle:** nur INSERT/UPDATE auf `schule.zuordnung` und `schule.eintrag`, kein DROP, kein DELETE; `schule.thema` bleibt unverändert.
- **Rauchtest** (bricht ab, die Transaktion rollt zurück):
  - a) 796 erwartete Zuordnungen;
  - b) ohne Hauptthema nur 640 und 660 (IB-Wiederholung);
  - c) `thema_jahrgang` aller Themen unverändert;
  - d) kein Hauptbezug auf stillgelegte Themen.
- **Probelauf auf lokalem Postgres 16** mit dem vollständigen echten Stand nach dem Live: alle Quellen, Einträge, Zuordnungen und `klasse_fest`, dazu die echte Funktion `thema_jahrgang`.
  - Die Testkopie liefert für alle 97 Themen dieselbe Klasse wie die DB.
  - Ohne LP-RS bricht Schritt 0 ab. LP-RS und danach LK-D bestanden, LK-D auch im zweiten Lauf (wiederholbar).
  - Gegenprobe mit einer absichtlich geänderten Klasse (Thema 100): Abbruch bei Rauchtest c, nichts geändert.

## 8 Repo-Klassen nachgezogen

- `klasse` in den Themendateien und im `META` der Generatoren entspricht jetzt `themenliste.json`, also der DB.
- Das betrifft 31 Themen, darunter die Widersprüche aus LP-RS:
  - 61 (rs 9);
  - 44 (rs 7);
  - 91 (gym 10, rs 7);
  - 99, 100 (rs 6);
  - 101 (rs 9);
  - 64 (gym 10);
  - 26 (rs 6).
  - Die übrigen bekamen fehlende Schlüssel (`ib_myp`, `rs_by`).
- 91 `rs_by` 7 steht auch in `themenliste.json`. Das folgt aus `rs_korrektur_2211.sql`; bis zum Einspielen weicht die DB (8) hier ab.
- Sieben Generatoren habe ich neu laufen lassen; sie erzeugen die Dateien unverändert. Bei den übrigen ist nur die META-Zeile geändert. Prüfskript OK, App-Tests 164/164.
- **Nicht** geändert: die Themendateien der stillgelegten Themen (12, 27, 40, 41, 48, 72, 77, 78, 82, 83). Das Prüfskript verlangt eine Klasse, und die Liste führt sie leer. Vorschlag: Diese Dateien bei Gelegenheit in einen Archivordner verschieben.

## Gesichert / Annahme / offen

**Gesichert:**
- Gymnasium: Stunden und Titel stimmen mit LehrplanPLUS (22.11.).
- Zahl der Punkte je Lernbereich (Gym aus der Abruf-Zusammenfassung).
- DB-Vorherstand: Zuordnungen, Klassen; die Klassen-Simulation stimmt mit der echten Funktion überein.
- 0 Voraussetzungs-Verstöße in Gymnasium und RS Gruppe I.
- Kein Thema erfüllt die Teilungsregel.
- Lernstand je Kind (lesend): keine Konflikte.
- SQL-Probelauf, Prüfskript und App-Tests grün.

**Annahme:**
- Die Etappen je Punkt beruhen auf meinem inhaltlichen Urteil (Kurzfassung gegen Etappentitel). Die Wahl zwischen sehr ähnlichen Etappen ist diskutierbar.
- Rolle und Teilung: Grundlage ist die erste Klasse mit **Hauptbezug**.
- „Erledigt“ heißt beim Kinderstand: gelandet, gesetzt oder nachgewiesen.
- IB-Kapitel sind grob; die Etappen dort sind eine Näherung.
- Gym-Punktzahl im Original: durch die Abruf-Zusammenfassung gezählt, nicht von Hand.

**Offen:**
- Zweitquellen Gym 6–10 (Inhalt) und neuer Abruf der IB-Verzeichnisse: Die Freigabe für den Abruf blieb unbeantwortet.
- Entscheidungen von Sebastian:
  - Teilungsliste (Empfehlung: nichts teilen);
  - 43/69/71 im Gymnasium als Vertiefung;
  - IB-Voraussetzungen (2 harte; berichtigt, vorher fälschlich 3).
- Gruppe II/III: Etappen in der JSON, kein SQL.
- Archivierung der stillgelegten Themendateien.
- Die Felder `rolle`/`etappen` und die Pflicht je Klasse kommen erst mit LK-S.

## Quellen (abgerufen 22.11.2026)

- LehrplanPLUS Gymnasium Mathematik: [5](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/5/mathematik), [6](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/6/mathematik), [7](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik), [8](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/8/mathematik), [9](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/9/mathematik), [10](https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/10/mathematik)
- [Fachprofil Mathematik Gymnasium](https://www.lehrplanplus.bayern.de/fachprofil/gymnasium/mathematik)
- C.C. Buchner mathe.delta Bayern:
  - [Stoffverteilung 5](https://www.ccbuchner.de/_files_media/mediathek/downloads/2431.pdf)
  - Produktseiten [6](https://www.ccbuchner.de/produkt/mathe-delta-bayern-6-3235), [7](https://www.ccbuchner.de/produkt/mathe-delta-bayern-7-3683), [8](https://www.ccbuchner.de/produkt/mathe-delta-bayern-8-3684)
- [IB, MYP Mathematics brief](https://www.ibo.org/globalassets/new-structure/brochures-and-infographics/pdfs/myp-brief-mathematics-en.pdf)
- Realschule: siehe `rs_pruefung_2211.md`.
