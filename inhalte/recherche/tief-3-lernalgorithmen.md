# Tiefen-Analyst 3: Lern-Algorithmen von Math Academy, ALEKS, ASSISTments, Alcumus, MATHia, Duolingo, FSRS und Übertrag auf die eigene App

Alle Quellen am 25.11.2026 abgerufen. Nur Websuche und Seitenabruf, nichts angemeldet.
Kennzeichnung: **[G]** gesichert, mit Quelle · **[A]** Annahme oder ungeprüftes Allgemeinwissen · **[M]** meine Meinung oder Ableitung.
Grundlage: Vorbericht `sucher-b-international.md` (gelesen). Was dort schon steht (Preise, Wirkungsstudien Roschelle/RAND), wiederhole ich nur, wenn es nötig ist.

Zur Quellenlage: Das PDF „The Math Academy Way“ (MAW, Arbeitsfassung, rund 1 Mio. Zeichen) konnte ich nicht herunterladen (Proxy-Sperre). Ich habe es abschnittsweise über das Abrufwerkzeug gelesen: Kapitel 4, 13–23, 29–31, FAQ und Glossar. Die Teile zwischen etwa 300.000 und 400.000 Zeichen (Kapitel 8–10) habe ich nicht gelesen. Für diese Fragen sind sie wohl unwichtig. Die Inhalte stammen aus Zusammenfassungen des Abrufwerkzeugs, nicht aus wörtlicher Lektüre. Zahlen, die mir wichtig waren, habe ich wo möglich mit einer zweiten Quelle abgeglichen (mathacademy.com, Blog, Hecker).

Quellenkürzel (alle Abruf 25.11.2026):
- MAW = https://www.justinmath.com/files/the-math-academy-way.pdf
- MA-AI = https://mathacademy.com/how-our-ai-works
- MA-PED = https://mathacademy.com/pedagogy
- MA-FAQ = https://mathacademy.com/faq
- FIRe-Blog = https://justinmath.com/individualized-spaced-repetition-in-hierarchical-knowledge-structures/
- KG-Bau = https://justinmath.com/how-math-academy-creates-its-knowledge-graph/
- KG-Regel = https://justinmath.com/the-most-important-thing-to-understand-about-building-educational-knowledge-graphs/
- Hecker7 = https://frankhecker.com/2025/02/14/math-academy-part-7/ · Hecker11 = https://frankhecker.com/2025/02/18/math-academy-part-11/
- Pershan = https://pershmail.substack.com/p/math-academy-wants-to-supercharge
- Matuschak = https://notes.andymatuschak.org/Math_Academy
- ALEKS-FAQ = https://www.mheducation.com/support/aleks-support-center/knowledge/aleks-what-is-the-difference-between-mastered-and-learned-topics.html
- KST-Kap = https://arxiv.org/pdf/1511.06757 (Falmagne/Doignon u. a., „Knowledge Spaces and Learning Spaces“)
- ALEKS-Assess = https://www.mheducation.com/content/dam/mhe/research/prek-12/essa-tier-4/aleks-assessing-learning-space.pdf
- ALEKS-Stop = https://link.springer.com/article/10.1007/s40593-021-00240-8
- ALEKS-Schwelle = https://jedm.educationaldatamining.org/index.php/JEDM/article/download/900/254
- LearnSeq = https://arxiv.org/pdf/0803.4030
- SB-Lehrer = https://www.assistments.org/blog-posts/how-assistments-skillbuilders-works-in-my-class-and-why-it-will-work-for-you-too
- SB-Testbed = https://sites.google.com/site/assistmentstestbed/description-of-a-skill-builder
- ARRS-RCT = https://www.assistments.org/blog-posts/our-research-reassessing-and-relearning
- ARRS-These = https://digital.wpi.edu/show/h128nh75b
- Kelly2015 = https://www.educationaldatamining.org/EDM2015/proceedings/poster630-631.pdf
- Alcumus = https://artofproblemsolving.com/blog/articles/alcumus-a-peek-under-the-hood-of-our-adaptive-learning-tool · AoPS-Wiki = https://artofproblemsolving.com/wiki/index.php?title=Alcumus
- MATHia-Doku = https://www.stat.cmu.edu/~brian/nynke/726-2021/project%20HCI%20Prereqs%20(Elaine,%20Smeet%20&%20Zhou)/2021-03-09/Carnegie%20Learning%20MATHia%202019-2020%20DataShop%20Documentation.pdf
- BKT-Lehr = https://www.cs.williams.edu/~iris/res/bkt-balloon/index.html
- HLR-Blog = https://blog.duolingo.com/how-we-learn-how-you-learn · HLR-Paper = https://preview.aclanthology.org/fix_video/P16-1174.pdf
- FSRS-100 = https://borretti.me/article/implementing-fsrs-in-100-lines · FSRS-Repo = https://github.com/open-spaced-repetition/fsrs4anki
- Craig-ALEKS = https://digitalcommons.memphis.edu/facpubs/8748 und https://digitalcommons.memphis.edu/facpubs/10611

---

## Kurzfazit (8 Punkte)

1. [G] Der Kern von Math Academy ist ein von Hand gebauter Graph: rund 2.500 Themen mit je 3–4 Wissenspunkten. Es gibt drei für euch wichtige Kantenarten: Voraussetzung (Thema→Thema), Schlüssel-Voraussetzung (Wissenspunkt→Thema, oft mehrere Stufen zurück) und „umfasst“ mit Gewicht 0–1 (KG-Bau, KG-Regel, MAW Kap. 29).
2. [G] FIRe heißt: Eine bestandene Wiederholung schickt Gutschrift *nach unten* (gewichtet, über mehrere Stufen). Eine gescheiterte Wiederholung schickt Strafe *nach oben*. Gutschrift für zu frühe Wiederholungen wird abgewertet. Bei „langsamen“ Kind-Thema-Paaren wird die implizite Gutschrift ganz abgeschaltet (FIRe-Blog, MAW Kap. 18/29).
3. [G] Genaue Formeln veröffentlicht Math Academy nicht; die Umsetzung ist laut Blog proprietär. Veröffentlicht sind nur die Struktur und einzelne Bausteine, zum Beispiel ein Gedächtniswert, der pro Intervall um die Hälfte sinkt.
4. [G] Die Mastery-Regeln sind überall einfach: ASSISTments verlangt 3 richtige in Folge (ein Tipp setzt den Zähler zurück, nach 10 Aufgaben „morgen wieder“). ALEKS verlangt 5 Punkte (+1, +2 bei Serie, −1; Erklärung ansehen streicht den Bonus). MATHia verlangt eine Wahrscheinlichkeit von 0,95 im Bayes-Modell (BKT). Bei Math Academy sind es 2–5 Fragen je Wissenspunkt ohne veröffentlichte Schwelle.
5. [G] Die Eingangsdiagnose ist bei ALEKS ein Wahrscheinlichkeitsverfahren über Wissenszustände: Es fragt jeweils das Item, das das Kind mit einer Wahrscheinlichkeit nahe 50 % löst, und hat höchstens 29 Fragen. Math Academy nutzt eine Plus-Minus-Bilanz entlang des Graphen mit 20–40 Fragen in unteren Klassen. Die Plus-Minus-Logik lässt sich **ohne Statistik** nachbauen, die ALEKS-Logik nicht.
6. [G] Unabhängige Wirkungsbelege gibt es für die Prinzipien (Abstände, Abrufen, Mischen), für ASSISTments (RCT) und eingeschränkt für ALEKS (Craig u. a., RCT, gemischt). Für Math Academy gibt es keine. Die stärksten Einwände: flaches, prozedurales Verständnis, kein Begründen, keine Transferaufgaben (Pershan, Matuschak).
7. [M] Für euch heißt das: Die 15 Grundregeln übernehmen die Rolle der Schlüssel-Voraussetzungen und der „umfasst“-Kanten. Damit bekommt der bisher dünne Graph (137 Kanten auf 105 Flüge) genau die Verbindungen, die FIRe braucht. Der Aufwand liegt bei einmalig etwa 15–30 Stunden Etikettieren.
0. **Math Academy im Detail (Kurse, Ablauf, Preis, AGB, Testmonat-Prüfliste, durchgerechnetes Beispiel): Abschnitt 11.**
8. [M] Am wichtigsten bei unregelmäßigem Lernen: Abstände in **Kalendertagen** rechnen (Vergessen läuft auch an freien Tagen) und die Tageslast in Lerntagen begrenzen. Nach Pausen gibt es einen kurzen Wiedereinstiegs-Check statt eines Wiederholungsstaus.

---

## 1. Wissensgraph

### Math Academy
- **Größe und Feinheit [G]:** „Mehrere tausend“ Themen von Klasse 4 bis Uni (MA-AI). In KG-Bau stehen konkret etwa 2.500 Themen. Jedes Thema hat 3–4 Wissenspunkte (Knowledge Points, KP), die schwerer werden (KG-Bau, MA-PED). Ein KP besteht aus einem Musterbeispiel und 2–5 Übungsfragen (MAW-FAQ). Ein Kurs hat rund 300 Themen, ein Analysis-Kurs also etwa 1.000 Lernschritte statt rund 100 im Lehrbuch (MA-PED).
- **Kantenarten [G]:**
  1. *Direkte Voraussetzung* (Thema→Thema). Faustregel: höchstens 3–4 je Thema, sonst „kognitiver Stau“ (KG-Regel).
  2. *Schlüssel-Voraussetzung* (KP→Thema). Das sind die Voraussetzungen, die ein Wissenspunkt am unmittelbarsten nutzt, höchstens 3–4 je KP. Sie können mehrere Stufen zurückreichen (KG-Regel, MAW Kap. 4).
  3. *Umfasst* (fortgeschrittenes→einfacheres Thema) mit Gewicht 0–1. Das Gewicht schätzt, welcher Anteil des einfachen Themas in einer Aufgabe des schweren Themas mitgeübt wird. „Umfasste“ Themen sind meist Voraussetzungen, aber Voraussetzungen werden oft nicht voll umfasst (MAW Kap. 4/29, FIRe-Blog).
  4. *Nicht-Vorfahren-„umfasst“*: verbindet gleichwertige Themen über Kurse hinweg (MAW Kap. 29).
  5. MAW spricht von „vielen weiteren Arten“, erklärt sie aber nicht [G: nicht gefunden].
  - Außerdem speichert der Graph je Thema die leichteste und die schwerste Aufgabenvariante und das Hintergrundwissen, das ein strauchelndes Kind am dringendsten braucht (MA-AI).
- **Wann ist etwas eine Schlüssel-Voraussetzung? [G]** Ein formales Verfahren gibt es nicht. Es ist Expertenurteil aus Unterrichts- und Tutorenerfahrung; Kriterium ist, was der Wissenspunkt *am unmittelbarsten benutzt* (KG-Bau, KG-Regel).
- **Wann bekommt eine „umfasst“-Kante ein Gewicht? [G]** Nur wenn drei Bedingungen zugleich gelten: (a) das Gewicht ist nicht trivial, (b) es lässt sich nicht aus der Kette ableiten, (c) die Themen liegen im Graphen nah beieinander. Alle anderen Gewichte gelten als 0. Gewicht 0 ist auch richtig, wenn nur begriffliche Vertrautheit nötig ist und keine Beherrschung (MAW Kap. 29, FIRe-Blog). Weit zurückliegende Themen unterhalb der Diagnose gelten automatisch als beherrscht („mastery floor“).
  - Ableitung über die Kette: Hecker rechnet das Beispiel A–B 0,5 und B–C 0,4, also A–C 0,2 (Hecker7). Das ist seine Lesart, die genaue Formel ist nicht veröffentlicht.
- **Aufwand [G]:**
  - Die erste Gewichtungsrunde betraf etwa 1.500 Themen mit je rund 5 Voraussetzungen, bei etwa 2 Minuten je Schätzung. Das waren rund 250 Stunden, einen Monat lang 8 Stunden täglich (KG-Bau).
  - Insgesamt nennt Math Academy „tausende und abertausende Stunden“ (https://justinmath.com/aei-the-report-card-podcast/). Der Lehrplanleiter hat 6–7 Jahre am Graphen gearbeitet (https://justinmath.com/math-academy-podcast-4-part-2/). Alle Inhalte sind handgemacht: 2024 waren es tausende Lektionen, zehntausende Musterbeispiele und hunderttausende Fragen (https://justinmath.com/who-does-what-at-math-academy/).
  - Strauchelt mehr als ein kleiner Anteil der Kinder an einer Lektion, wird der Inhalt umgebaut (mehr Gerüst, Zwischen-KP, Thema teilen); die Messlatte wird nicht gesenkt (MAW Kap. 21).

### ALEKS (Knowledge Space Theory)
- [G] Die Knoten sind Problemtypen („Items“). Beispiele: 370 Items in Grundschulmathe Klasse 3–6 (ALEKS-Assess), bis zu 650 Items in Anfangsalgebra mit vielen Millionen möglichen Wissenszuständen (KST-Kap), in einer anderen Quelle ungefähr 10⁷ Zustände.
- [G] Kanten: Es gibt Voraussetzungsbeziehungen (in KST „Surmise-Relation“). Ein Wissenszustand ist eine Menge von Items, die ein Kind lösen kann. Zulässig sind nur bestimmte Mengen. In einem „Lernraum“ lässt sich jeder Zustand Item für Item erreichen (Axiome in https://link.springer.com/doi/10.1007/s40593-019-00176-0).
- [G] Der *äußere Rand* („outer fringe“) eines Zustands ist die Menge der Items, die das Kind *bereit ist zu lernen* (ALEKS-Assess).
- [G] Aufbau: zuerst Befragung von Fachlehrkräften, dann statistische Verfeinerung an mehreren hundert Lernenden (Falmagne 1990, https://stat.cmu.edu/~brian/nynke/726-2021/project%20HCI%20Prereqs%20(Elaine,%20Smeet%20&%20Zhou)/2021-02-23/Falmagne90.pdf).

### ASSISTments / MATHia
- [G] ASSISTments: Je Fertigkeit gibt es eine „Skill Builder“-Aufgabenmenge mit hunderten Aufgaben (SB-Testbed). Der Datensatz von 2009/10 hat 123 Fertigkeiten (Vorbericht), die ARRS-Vorstellung nennt 130 Mastery-Fertigkeiten für Mittelstufe (https://digitalwpi.wpi.edu/downloads/h989r486d?locale=en). Einen ausgearbeiteten Graphen habe ich nicht gefunden.
- [G] MATHia: Inhalte stecken in „Workspaces“. Jedem Lösungs*schritt* ist eine Wissenskomponente (KC) zugeordnet; ein Workspace ist abgeschlossen, wenn alle zugehörigen KCs gemeistert sind (MATHia-Doku). Ein Beispielkurs hat 223 KCs (CMU-Projektpapier, gleiche Quellsammlung).

### Einordnung für euch [M]
- Rechenbeispiel: 716 Etappen auf 105 Flüge sind rund 6,8 Etappen je Flug, feiner als Math Academy mit 3–4 KP je Thema. Ein Flug entspricht also etwa 1,5–2 MA-Themen. Eure Etappen liegen etwa auf KP-Ebene.
- Rechenbeispiel: 137 Kanten auf 105 Flüge sind rund 1,3 Voraussetzungen je Flug, und auf Etappen-Ebene gibt es gar keine Kanten. Math Academy hat 3–4 Schlüssel-Voraussetzungen *je Wissenspunkt*. Euer Graph ist also vergleichsweise dünn.
- Die 15 Grundregeln schließen genau diese Lücke: Jede Etappe bekommt 0–3 Regel-Kanten. Damit habt ihr ohne neuen Etappen-Graphen das, was bei Math Academy Schlüssel-Voraussetzungen und „umfasst“-Gewichte leisten.

---

## 2. Eingangsdiagnose

### Math Academy [G, MAW Kap. 30, MAW-FAQ, MA-AI]
- **Länge:** etwa 20–40 Fragen bei unteren Kursen (zum Beispiel Prealgebra), 40–60 bei oberen (zum Beispiel Analysis). Ohne Graph wären es über 500, bei vollständiger Genauigkeit bis etwa 1.000.
- **Ergiebigkeit:** Jede Frage liefert im Schnitt eine eindeutige Aussage zu etwa 10 Themen. Je Frage sind höchstens 3 Minuten vorgesehen.
- **Verdichteter Diagnose-Graph:** Ein Thema gilt als „abgedeckt“, wenn es im verdichteten Graphen innerhalb von 3 Voraussetzungskanten einen Vorfahren *und* einen Nachfahren hat, der geprüft wird. Für Blatt-Themen eines Moduls wird aus repräsentativen Fragen geschlossen.
- **Plus-Minus-Bilanz:** Jede Antwort hat Grundgewicht 1.
  - Richtig: plus für das Thema und rekursiv alle Voraussetzungen.
  - Falsch: minus für das Thema und rekursiv alle Nachfolger.
  - Richtig, aber zu langsam: plus mit vermindertem Gewicht. Eine Zeitschwelle ist nicht veröffentlicht.
  - Das Vorzeichen ist die Vorhersage (kann / kann nicht), der Betrag die Sicherheit.
  - Danach bekommen Themen mit positiver Bilanz so viele Wiederholungen gutgeschrieben, wie die Bilanz beträgt.
- **Widersprüche:** Zwei Arten werden ausdrücklich behandelt: (a) das schwere Thema richtig, das leichte falsch; (b) richtig, aber übermäßig langsam.
- **„Bedingt erledigt“:** Knapp positive Themen gelten nur vorläufig. Scheitert das Kind später an etwas, das darauf aufbaut, wird die Gutschrift entfernt und das System geht den Lernpfad zurück.
- **Rand der Beherrschung:** Die Diagnose platziert bewusst *konservativ*. Das Lernen läuft dann am „aggressiven“ Rand.
- **Fragenauswahl:** Es wird die *einfachste* Frage gewählt, die eine Fachperson überzeugen würde *und* alle Voraussetzungen des Themas mitübt. Die schwerste wird vermieden, weil dort Flüchtigkeitsfehler wahrscheinlicher sind.
- **„Weiß nicht“-Knopf:** Er existiert nur in der Diagnose. Übersprungene Fragen zählen als „weiß nicht“.
- **Zeit:** Die Diagnose misst auch Automatisierung. Langsame Antworten bei Dingen, die man „im Schlaf können“ sollte, gelten als Lücke (MA-FAQ).
- **Nachdiagnosen:** kurze Ergänzungsdiagnosen, wenn sich der Graph ändert, nicht wegen schlechter Leistung.
- **Nicht gefunden [G]:** in welcher *Reihenfolge* Math Academy die Fragen stellt (der Auswahl-Algorithmus) und wann genau es aufhört.

### ALEKS [G]
- **Fragewahl („half-split“):** Gefragt wird das Item, das das Kind nach der aktuellen Wahrscheinlichkeitsverteilung über die Zustände mit einer Wahrscheinlichkeit möglichst nahe 0,5 richtig löst. Bei Gleichstand wird zufällig gewählt (KST-Kap). Grundidee: Jede Antwort halbiert ungefähr die verbleibenden Zustände. Dann reichen etwa log₂(Zahl der Zustände) Fragen (LearnSeq).
- **Aktualisierung:** Bayes- oder multiplikative Regel. Eine richtige Antwort erhöht die Wahrscheinlichkeit aller Zustände, die das Item enthalten. Angenommen werden kein Glückstreffer (0, wegen freier Antwortformate) und eine Flüchtigkeitsfehlerrate je Item (Median 19 %). Die Startverteilung war in der Version von 2006 gleichverteilt (ALEKS-Assess, LearnSeq).
- **Ende:** wenn kein Item mehr „unsicher“ ist oder die Höchstzahl erreicht ist. Bei ALEKS PPL sind das 29 Fragen, und etwa 97 % der Tests erreichen diese Grenze. Seit 2023 stoppt ein neuronales Netz früher: im Schnitt 21,3 Fragen, also über 26 % kürzer, Mediandauer 60 statt 82,5 Minuten (ALEKS-Stop).
- **Ergebnis:** Ein Item zählt als gekonnt, wenn die Summe der Wahrscheinlichkeiten der Zustände, die es enthalten, über 0,5 liegt (ALEKS-Assess).
- **Prüfung:** Eine zusätzliche, zufällige Kontrollfrage wird mit dem ermittelten Zustand verglichen (ALEKS-Assess).

### Lässt sich das mit 15 Regeln und 716 Etappen ohne Statistik nachbauen? [M]
- **ALEKS: nein.** Die Zustandsmenge, die Fehlerraten und die Startverteilung brauchen Daten vieler Kinder.
- **Math Academy: ja, in vereinfachter Form.** Die Plus-Minus-Bilanz braucht nur den Graphen und Regeln. Vorschlag in zwei Ebenen:
  1. *Regel-Ebene (15 Knoten):* der „Eingangscheck Werkzeuge“, siehe 9c.
  2. *Flug-Ebene (105 Knoten, 137 Kanten):* Je Flug gibt es eine „Prüf-Aufgabe“ nach Math-Academy-Art: die einfachste Aufgabe, die die Kernidee des Flugs *und* seine Voraussetzungen nutzt.
     - Richtig und ohne Hilfe: +1 für den Flug und alle Vorgänger-Flüge, rekursiv.
     - Falsch oder „weiß nicht“: −1 für den Flug und alle Nachfolger-Flüge.
     - Nächster Prüf-Flug: der unentschiedene Flug, der die meisten unentschiedenen Flüge über *und* unter sich hat. Das ist ein „Halbierungsersatz“ ohne Wahrscheinlichkeiten, nach der ALEKS-Idee.
     - Ende: wenn jeder Flug entschieden ist (|Bilanz| ≥ 1, oder ≥ 2 für „sicher“) oder nach 30 Aufgaben.
     - Etappen eines positiv bewerteten Flugs: alle „bedingt gelandet“ nach Math-Academy-Art. Der Status fällt weg, sobald im Flug oder in einem Nachfolger ein Fehler auftritt.
  - Annahme [A]: Bei Klasse 5 und 8 ist die Spanne klein, die meisten Flüge entscheiden sich über ihre Ketten. 20–30 Aufgaben reichen vermutlich. Das ist ungeprüft und hängt davon ab, wie verzweigt eure 137 Kanten sind.

---

## 3. Mastery („sitzt“): Kriterien je System

| System | Kriterium | Hilfe/Tipp | Raten | Quelle |
|---|---|---|---|---|
| Math Academy, Lektion | Je KP „genügend viele“ richtige mit wenigen Fehlern. Bei Fehlern kommen mehr Fragen, bei hoher Trefferquote weniger. KP nicht in 2–5 Fragen gemeistert: Lektion abgebrochen, später neu. Erstversuch bestanden 93–95 %, im 2. Versuch 98–99 %. **Keine Zahl veröffentlicht.** | Keine Tipps; „die Messlatte wird nicht gesenkt“, stattdessen mehr Übung | Reihenfolge zählt: ✖✔✖✔✔ gilt als gelernt, ✔✔✖✔✖ als Straucheln. Negative XP bei Hinwerfen/Raten. Quiz mit mehreren Fragen je Thema gegen Raten. Kein „weiß nicht“ außer in der Diagnose. | MAW Kap. 13/21/22, MAW-FAQ, MA-FAQ |
| Math Academy, Quiz | Zeitbegrenzt, gemischt, ohne Hilfe. Zu langsam zählt als „noch nicht beherrscht“. Zieltrefferquote 80–85 %. | Keine Nachschlagewerke | Keine Wiederholung sofort; Neuversuch mit anderen Fragen erst nach den Wiederholungen | MA-FAQ, MA-AI, MAW |
| ALEKS | Thema „gelernt“ bei **5 Punkten**: +1 richtig, +2 bei zweiter richtiger in Folge, −1 falsch, nie unter 0. 5 Fehler in Folge sind ein gescheiterter Versuch. „Gemeistert“ erst nach Bestätigung im Wissens-Check. Im Experiment für unsichere Themen 3 Punkte statt 5. | Erklärungsseite angesehen: die nächste richtige zählt nur +1 | „Weiß nicht“ erlaubt; im Check führt falsch oder „weiß nicht“ zum Rückfall auf „offen“ | ALEKS-FAQ, ALEKS-Schwelle |
| ASSISTments Skill Builder | **3 richtige in Folge** | Jeder Tipp setzt die Serie zurück | Nach 10 Aufgaben ohne Erfolg: „morgen wieder“ | SB-Lehrer, SB-Testbed |
| MATHia (Cognitive Tutor) | Je Wissenskomponente BKT-Wahrscheinlichkeit ≥ **0,95** | [A] In der BKT-Praxis zählt ein Tipp meist als „nicht korrekt“ (nicht an Primärquelle geprüft) | Ratewahrscheinlichkeit im Modell, typischerweise auf ≤ 0,3 begrenzt; Flüchtigkeit ≤ 0,1 | MATHia-Doku, BKT-Lehr |
| Alcumus | Themen-„Rating“ 0–100 = Wahrscheinlichkeit, eine Durchschnittsaufgabe des Themas zu lösen. Logistisch: P = 1/(1+e^(Aufgabenwert − Schülerwert)). Grün = bestanden, Blau = gemeistert. **Schwellen nicht veröffentlicht.** Gemeistertes kann wieder herausfallen. | Nicht gefunden | Gesehene Aufgaben werden seltener gezogen | Alcumus, AoPS-Wiki |

BKT-Formeln [A: Standardformeln nach Corbett & Anderson 1995 aus meinem Wissen; die abgerufenen Seiten nennen die Parameter, zeigen die Formeln aber nicht]:
- P(L|richtig) = P(L)(1−S) / [P(L)(1−S) + (1−P(L))G]
- P(L|falsch) = P(L)S / [P(L)S + (1−P(L))(1−G)]
- danach P(L) ← P(L|Beob.) + (1 − P(L|Beob.))·T
- mit G = Raten, S = Flüchtigkeit, T = Lernwahrscheinlichkeit je Gelegenheit

Was über Schwellen belegt ist [G]:
- **Kelly u. a. 2015 (ASSISTments, kleine Stichprobe):** 3 in Folge sagt die *nächste* Aufgabe ebenso gut vorher wie BKT (rund 80 %). Bei einer *Transferaufgabe* erkannte 5 in Folge Beherrschung genauer als 3 in Folge (rund 73 % gegenüber 57 % Trefferquote der Einstufung). Über 90 % derer, die 3 in Folge schafften, erreichten auch 5 (Kelly2015).
- **ALEKS-Experiment 2023–2024 (rund 800.000 Lernende):** Mit 5 statt 3 Punkten wird etwas weniger vergessen. Der Vorsprung ist am Anfang am größten (knapp 0,03–0,04) und schrumpft nach einigen Wochen unter 0,02. Am meisten profitieren schwere Themen und Kinder, die mit einem Fehler beginnen (ALEKS-Schwelle).
- [M] Folgerung: Mehr Wiederholungen *am Stück* bringen wenig und verblassen. Die Abstände über Tage und Wochen sind der stärkere Hebel. Das spricht für euer Merkmal „verteilt über Wochen“.

---

## 4. Verteilte Wiederholung im hierarchischen Fach

### Math Academy: FIRe [G, FIRe-Blog, MAW Kap. 18/29, MA-AI, Hecker7]
- **Größen im Modell:** `repNum` (Zahl der erfolgreichen Wiederholungen), `days` (Tage seit der letzten), `interval` (Sollabstand bis zur nächsten), `memory` (erwartetes Erinnern), `speed` (Lerntempo je Kind und Thema), `failed` (0/1), `rawDelta` (positiv bei bestanden, negativ bei gescheitert, Betrag nach Qualität der Arbeit; Hecker deutet ihn als XP), `decay` (startet bei 1 und wächst, je überfälliger eine Wiederholung ist).
- **Gedächtnis:** memory = max(0, memory + Gutschrift) · 0,5^(days/interval). Nach einem Intervall ist also nur noch die Hälfte übrig, nach zwei Intervallen ein Viertel (FIRe-Blog, Hecker7). Fällig wird ein Thema, wenn memory tief genug gefallen ist. Die Schwelle ist nicht veröffentlicht.
- **Schritt im Wiederholungsplan:** speed · decay^failed · rawDelta. Wer nach langer Überfälligkeit scheitert, fällt weiter zurück; so wird der „Sommerknick“ abgebildet. Frühe Wiederholungen werden abgewertet: Ist memory noch hoch, gibt es weniger Gutschrift. Sie setzen den Plan aber nicht zurück, sondern schieben ihn nur etwas nach hinten (MAW-FAQ).
- **Gutschrift nach unten:**
  - Wird ein schweres Thema bestanden, bekommen die umfassten Themen anteilig Gutschrift, über mehrere Stufen. Volle „umfasst“-Kanten geben ungebremst weiter (der „Stamm“), Teilkanten lassen die Gutschrift verblassen.
  - Bildlich: Gutschrift läuft wie ein Blitz nach unten, Strafe wächst wie ein Baum nach oben.
- **Strafe nach oben:** Wer ein einfaches Thema nicht schafft, bestraft die Themen, die es umfassen.
- **Anpassung an das Kind:**
  - Tempo = (Beschleunigung durch Fähigkeit) / (Bremsung durch Schwierigkeit) als 3×3-Muster (stark/mittel/schwach × leicht/mittel/schwer).
  - Eine Wiederholung bei Tempo 2 zählt als 2, bei 0,5 als 0,5.
  - **Bei Tempo < 1 gibt es keine implizite Gutschrift; dann sind ausdrückliche Wiederholungen Pflicht.**
  - Fähigkeit wird je Thema als Trefferquote gemessen, jüngere Antworten zählen mehr. Richtige Antworten wirken auch nach unten, falsche nach oben.
  - Die Schwierigkeit kommt aus den Daten *aller* ernsthaften Lernenden. Das könnt ihr nicht nachbauen.
- **Abstände:** keine Zahlen veröffentlicht. Sie wachsen bis zu einem Jahr und mehr. Ein leichtes, auf Anhieb bestandenes Thema kann schon bei der 1. Wiederholung einen Abstand bekommen, den ein schweres erst bei der 5. erreicht (MAW-FAQ).
- **Wiederholungen verdichten („Repetition Compression“):**
  1. Aufgaben (Wiederholungen *oder neue Lektionen*) so wählen, dass ihre impliziten Wiederholungen möglichst viele fällige Wiederholungen abdecken.
  2. Wenn nichts fällig ist: Aufgaben wählen, die künftige Wiederholungen vermeiden, und den Graphen gleichmäßig hochsteigen, damit es später viele Möglichkeiten zum Verdichten gibt.
  - **Eine fällige Wiederholung wird nie verfallen gelassen**, nur weil man auf eine implizite Gelegenheit wartet; dann kommt eine ausdrückliche (FIRe-Blog).
  - Ein genauer Algorithmus ist nicht veröffentlicht.
- **Last-Grenzen:** im Mittel etwa eine Lektion auf 3 Wiederholungen, auch bei Rückstand; mindestens rund 25 % neue Lektionen; langfristig ein paar Wiederholungen je Lektion (MAW Kap. 22, FAQ).
- **Lange Pausen:** Der `decay`-Term verstärkt den Rückschritt, wenn nach Überfälligkeit etwas scheitert. Die Diagnose kann wiederholt werden, um den Wissensrand neu zu setzen (FIRe-Blog).
- **Kritik:** Matuschak merkt an, das System sei womöglich zu *zuversichtlich*: Er vergesse schneller als vorhergesagt (Matuschak). [M] Implizite Gutschrift kann also Behalten vortäuschen. Das ist ein Grund für eine Untergrenze ausdrücklicher Wiederholungen.

### ALEKS [G, ALEKS-FAQ]
- Ein Wissens-Check wird ausgelöst nach 20 gelernten Themen *und* 5 Stunden, oder nach 10 Stunden, oder nach 60 Tagen ohne Check.
- Was dort falsch oder mit „weiß nicht“ beantwortet wird, fällt von „gemeistert/gelernt“ auf „offen“ zurück und kommt wieder in den Lernpfad. Der Wiederholungsmodus ändert den Zustand nicht.

### ASSISTments ARRS [G, SB-Lehrer, SB-Testbed]
- Nach bestandenem Skill Builder gibt es **1 Aufgabe nach 7 Tagen**; ist sie richtig, folgen weitere nach **14, 28 und 56 Tagen**, jeweils gezählt ab dem ersten Bestehen.
- Ist sie falsch, muss der Skill Builder neu bearbeitet werden (wieder 3 in Folge).
- Die Nachprüfung ist gemischt und ohne Tutor-Hilfe, je Fertigkeit eine Aufgabe (https://digitalwpi.wpi.edu/downloads/h989r486d?locale=en).

### Duolingo-Halbwertszeit (HLR) [G, HLR-Blog, HLR-Paper]
- p = 2^(−Δ/h): Erinnerungswahrscheinlichkeit nach Δ Tagen bei Halbwertszeit h.
- h = 2^(Θ·x), wobei x Merkmale der Lerngeschichte sind (wie oft richtig oder falsch). Die Gewichte Θ werden aus Massendaten gelernt.
- Geübt wird, wenn p nahe der Hälfte ist.
- A/B-Test des Anbieters: +9,5 % tägliche Rückkehr bei Übungssitzungen, +12 % Gesamtaktivität.

### FSRS (Anki) [G, FSRS-100, FSRS-Repo]
- R(t,S) = (1 + F·t/S)^C mit F = 19/81 und C = −0,5. S ist die „Stabilität“, also die Tage, bis R auf 0,9 fällt.
- Intervall I = (S/F)·(R_soll^(1/C) − 1). Bei R_soll = 0,9 ist I = S.
- Erfolg: S' = S·(1 + e^w8·(11−D)·S^(−w9)·(e^(w10·(1−R))−1)·…). Je später die Wiederholung (kleineres R), desto größer der Zuwachs. Je schwerer die Karte (D), desto kleiner.
- Scheitern: S' = min(w11·D^(−w12)·((S+1)^w13 − 1)·e^(w14·(1−R)), S).
- 19 bis 21 Gewichte (neueste Fassung FSRS-7: 34), aus den eigenen Wiederholungsdaten optimiert. Lizenz MIT.
- [M] Für euch lehrreich: Eine verspätete, aber *bestandene* Wiederholung ist mehr wert als eine pünktliche. Das ist das Gegenstück zur Abwertung früher Wiederholungen bei Math Academy.

### Einordnung eurer 1-3-7-14-30 [M]
- Eure Reihe ähnelt ARRS (7/14/28/56) und den Anfangsabständen von Anki. Sie endet aber bei 30.
- Ohne weitere Stufen (60, 120 …) wachsen entweder die Wiederholungen nie aus oder sie hören ganz auf. Beides passt nicht zu einem Jahr Reise.
- Gerechnet in *Lerntagen*, werden Abstände bei seltenem Lernen in Kalenderzeit sehr lang: Bei jedem 3. Tag Lernen sind 30 Lerntage etwa 90 Tage.

---

## 5. Remediation bei wiederholtem Scheitern

- **Math Academy [G, MAW Kap. 21, MA-AI, MAW-FAQ]:**
  1. Bei Straucheln in einer Lektion kommen mehr Fragen.
  2. Zu viele Fehler: Lektion abgebrochen, **Pause mit nicht verwandten Themen**, Neuversuch einige Tage später. Etwa 80 % bestehen dann ohne weitere Hilfe.
  3. Scheitert das Kind **zweimal am selben Wissenspunkt**, gibt es vor dem nächsten Versuch Hilfs-Wiederholungen zu den **Schlüssel-Voraussetzungen dieses Wissenspunkts**, gegebenenfalls danach die zugehörigen Lektionen. Beispiel: bei (−4)³ zurück zu „negative Zahlen multiplizieren“.
  4. Eine falsche Quizfrage löst sofort eine Wiederholung dieses Themas aus.
  5. Fehlende Grundlagen unterhalb des Kurses werden gefüllt, während das Kind an Kursthemen weiterarbeitet, die nicht davon abhängen.
  - Warnzeichen für Eltern: mehr als 1 von 10 Lektionen gescheitert, negative XP, dauerhaft höchstens die Hälfte der XP pro Minute (MAW-FAQ).
- **ALEKS [G]:**
  - Fällt ein Thema im Check durch, kommt es zurück in den Lernpfad.
  - Lernen ist ein „Zufallsweg“: richtig einen Schritt vor, falsch einen zurück mit Erklärung. Am linken Rand wird das Thema zurückgestellt und der Zustand angepasst (ALEKS-Assess).
  - „Just-in-time“-Wiederholung nach Fortschritts-Checks (https://www.mheducation.com/support/aleks-support-center/knowledge/just-in-time-review-after-a-progress-knowledge-check.html).
- **ASSISTments [G]:** Nach 10 Aufgaben ohne Serie: Stopp, „morgen wieder“. Die Lehrkraft sieht die Betroffenen im Bericht (SB-Lehrer). Ein Rücksprung zu Voraussetzungen ist nicht automatisch dokumentiert [G: nicht gefunden].
- **MATHia [G, MATHia-Doku]:** Schrittweise Hinweise und sofortige Rückmeldung je Schritt. Ein automatischer Rücksprung zu Voraussetzungen ist nicht dokumentiert gefunden.

---

## 6. Mischen und gemischte Prüfungen

- **Math Academy [G]:**
  - Quiz etwa alle 150 XP, also rund 150 Minuten konzentrierter Arbeit (MA-FAQ).
  - Zeitbegrenzt und voll gemischt über *alle* bisher gelernten Themen; vorrangig der eingeschriebene Kurs. Kürzlich geprüfte oder durch andere prüfbare Themen schon abgedeckte Themen werden gemieden (MA-AI, MAW-FAQ).
  - Schwierigkeit so geregelt, dass das Kind im Mittel etwa 80 % schafft: darüber leicht schwerere Varianten, darunter leichtere (MA-AI).
  - Keine Hilfen, kein „weiß nicht“, kein sofortiger Neuversuch. Ein Neuversuch mit anderen Fragen gibt es erst nach den ausgelösten Wiederholungen (MA-FAQ, MAW-FAQ).
  - Die Länge ist nicht veröffentlicht; auf der Übersicht erscheint ein Fenster von rund 30 XP (MAW-FAQ).
  - Wiederholungen sind auch gemischt (Beispiel: 15 Aufgaben als 5 Themen × 3, verteilt auf mehrere Wiederholungen). Aufgaben aus Wiederholungen sind nie identisch mit Lektionsaufgaben. Ähnliche Themen werden zeitlich auseinandergezogen, unähnliche gemischt (MAW Kap. 17/19, MA-AI).
  - Prüfungsvorbereitung: Kurs mindestens 6 Wochen vor der Prüfung beenden, mindestens 6 Probeklausuren auf Zeit; verpasste Aufgaben am Folgetag neu, dann mit wachsendem Abstand (MAW-FAQ).
  - Beleg im Buch: Rohrer u. a. 2015 berichten nach einem Tag 25 % und nach einem Monat 76 % bessere Werte durch Mischen (zitiert in MAW Kap. 19; Originalstudie nicht von mir geprüft).
- **ASSISTments ARRS [G]:** Nachprüfung als gemischte Wiederholung ohne Hilfe, eine Aufgabe je Fertigkeit.
- **Alcumus [G]:** Jede Aufgabe ist ein Zufallszug zwischen „aktuelles Thema“ und „Wiederholung aus bestandenem Thema“. Die Anteile sind nicht veröffentlicht (Alcumus).
- **ALEKS [G]:** Die Wissens-Checks sind der gemischte Test, ausgelöst wie unter 4 beschrieben.

---

## 7. Automatisierung und Rolle der Zeit

- **Math Academy [G]:**
  - Die Diagnose wertet richtige, aber langsame Antworten schwächer (MAW Kap. 30). Langsames Abrufen von Dingen, die man „im Schlaf“ können sollte, gilt als Lücke (MA-FAQ).
  - In Quizzen zählt Überschreiten der Zeit als „nicht beherrscht“ und löst eine Wiederholung aus (MA-FAQ).
  - Reihenfolge: **erst Genauigkeit ohne Zeit**, Zeitdruck erst nach gezeigter Fertigkeit. Zeit dient dem Abrufen von Gelerntem, nicht der Einführung von Neuem (MAW Kap. 18/20, Fuchs u. a. 2021 zitiert).
  - Zeitvorgaben sind in den Einstellungen anpassbar (MA-FAQ). Zahlenwerte für Zeitgrenzen: nicht gefunden.
- **ALEKS, ASSISTments, Alcumus:** keine Zeitregel für Mastery gefunden. ASSISTments-Berichte zeigen die Zeit nur an (SB-Testbed).
- [M] Für euch: Solange die Antwortzeit nicht gespeichert wird, kann „fest genug“ Automatisierung nur über die Papier-Probe *in Zeit* prüfen. Antwortzeit speichern ist billig und für die Grundregeln besonders aussagekräftig: Vorzeichen und Bruchrechnen müssen schnell gehen, damit in der Schulaufgabe Kopf für das Eigentliche bleibt (Arbeitsgedächtnis-Argument in MAW Kap. 15).

---

## 8. Belege und Kritik

### Was unabhängig belegt ist [G]
- **Prinzipien:** Verteiltes Üben, Abrufen (Testen) und Mischen sind in der Lernpsychologie breit belegt. MAW stützt sich darauf, zum Beispiel Rohrer 2015, Bahrick 1993 und eine Metaanalyse mit g = 0,50 für Klassenquizze über 222 Studien (MAW Kap. 18–20). Die Originalstudien habe ich nicht gelesen.
- **ASSISTments:**
  - Großes RCT zu Hausaufgaben mit sofortiger Rückmeldung (Roschelle 2016, WWC ohne Vorbehalt; Vorbericht).
  - ARRS: RCT des Entwicklerteams mit 97 Achtklässlern an einer Schule. Besser auf wiederholt geprüften Fertigkeiten, am meisten bei Schwachen; Effektgrößen auf der Seite nicht genannt (ARRS-RCT).
  - Eine WPI-Abschlussarbeit mit 50 Geometrie-Lernenden über 10 Wochen fand **keinen signifikanten** Effekt der ARRS-Zusatzaufgaben (ARRS-These).
  - Kelly 2015: klein, siehe Abschnitt 3.
- **ALEKS:**
  - Craig u. a. (Universität Memphis, IES-gefördert): RCT im Nachmittagsprogramm für schwache Sechstklässler. Im 1. Jahr war die ALEKS-Gruppe im Landestest besser, *aber nur bei ausreichender Nutzung*. Eine andere Auswertung fand gleiches Niveau wie bei Fachlehrkräften und weniger nötige Hilfe (Craig-ALEKS).
  - Die Diagnose-Validität ist groß untersucht, aber von Mitarbeitenden des Anbieters (ALEKS-Assess; Springer 2019).
- **MATHia:** RAND-RCT gemischt (Vorbericht).

### Was nur Anbieter-Behauptung ist [G]
- Math Academy: „4× effizienter“ ist eine eigene Schätzung (6.000 XP gegenüber rund 24.000 Minuten Unterricht; MA-FAQ). Bestehensquoten 93–95 %. Der Nutzen von FIRe ist nicht unabhängig geprüft. Eine unabhängige Studie habe ich nicht gefunden (auch der Vorbericht nicht).
- ALEKS: Neuronales Netz bringt „9 % mehr Stoff in gleicher Zeit“ (Pressemitteilung McGraw Hill, https://www.mheducation.com/news-media/press-releases/new-ai-enhancement-to-mcgraw-hill-aleks.html).
- Duolingo: A/B-Zahlen aus dem eigenen Blog.
- Alcumus: keine Wirkungsstudie gefunden.

### Stärkste Einwände
1. **Flach und prozedural** (Pershan): Lektionen folgen dem Muster Musterbeispiel und 2–5 meist Multiple-Choice-Fragen. Erklärungen lassen sich überspringen. Übungen ändern nur die Zahlen; unbekannte Aufgaben kamen nicht vor. Die verteilte Wiederholung *festigt ein flaches Verständnis*: Er konnte Formeln abrufen, ohne zu wissen, was eine geometrische Verteilung ist. Sein Urteil: nur als Ergänzung zu einem Kurs mit Lehrkraft.
2. **Kein Begründen, kein Transfer** (Matuschak): Die Erklärungen motivieren und deuten nicht. Begriffe, Namen und Begründungen werden nicht wiederholt. Beweisaufgaben sind Schablonen. Es fehlen Transferaufgaben. Bei Multiple Choice wird ein falsches Ergebnis, das nicht unter den Optionen steht, nicht als falsch gewertet. Die Lernschlange ist eine „Black Box“, die passiv macht.
3. **Tempo vor Tiefe** (Hecker11, Pershan): Die Werbung mit Geschwindigkeit kann Tiefe verdrängen. Hecker zeigt auch, wo das Buch vage bleibt: Gutschriftformel, „nah im Graphen“, „ernsthafte Lernende“ (Hecker7).
4. **Zu zuversichtliches Wiederholungsmodell** (Matuschak): Er vergaß schneller, als das System annahm.
5. **Mastery-Schwellen sind Konventionen:** 3 in Folge ist laut eigener Forschung „ausreichend“, aber beim Transfer schwächer (Kelly2015). Höhere Schwellen bringen nur kleine, schwindende Vorteile (ALEKS-Schwelle).
6. **ALEKS:** Wirkung nur bei ausreichender Nutzung (Craig). Die Diagnose dauert lange: Mediandauer 82,5 Minuten bei 29 Fragen (ALEKS-Stop).
- [M] Für euren Maßstab (Schulaufgabe auf Papier, Textaufgaben, Begründen) wiegen Einwand 1 und 2 schwer. Das Regelwerk unten deckt das *Behalten und Abrufen von Verfahren* ab, nicht Verstehen und Begründen. Dafür braucht ihr eigene Aufgabenformen: Brückenform, Begründungsaufgaben, unbekannte Aufgaben in der Papier-Probe.

---

## 9. Übertrag auf die eigene App: einfaches Regelwerk

Vorbemerkung [M]: Alles unten ist **meine Ableitung**. Bei jedem Punkt steht, worauf er sich stützt. Zahlen ohne Quelle sind Startwerte zum Nachjustieren, keine Befunde.

### 0. Datenmodell (Minimum)
- **Regel-Etikett je Etappe:** höchstens 3 Grundregeln mit Stufe **„trägt“ (1,0)** oder **„nutzt“ (0,5)**. Eine Regel, die nur gestreift wird, bekommt **kein** Etikett (Gewicht 0).
  - *Quelle:* MA „umfasst“-Gewichte 0–1, nur wenn nicht trivial und nah; Gewicht 0 bei bloßer Vertrautheit; höchstens 3–4 Schlüssel-Voraussetzungen je Wissenspunkt (MAW Kap. 29, KG-Regel). *Eigene Ableitung:* nur 2 Stufen statt einer stufenlosen Skala, damit man sie in einer Minute festlegen kann.
  - *Aufwand:* 716 Etappen × etwa 1–2 Minuten ≈ 12–24 Stunden einmalig. Math Academy brauchte für eine größere Aufgabe 250 Stunden (KG-Bau).
- **Fehlbild-Tabelle:** jedes bekannte Fehlbild → genau eine Grundregel (zum Beispiel „Minus vor Klammer nur beim ersten Glied“ → Minusklammer).
- **Je Kind und Regel:** Stufe auf der Leiter, Datum der letzten gezählten Wiederholung, fällig am (Kalenderdatum), Gutschriftkonto g (0 bis unter 1), Status (offen / wackelt / sitzt / fest), Tempo (langsam / normal / schnell), die letzten 10 Erstversuche mit Ergebnis und **Antwortzeit**.
- **Regel-Vorgänger:** ein kleiner Graph mit 15 Knoten und etwa 15–20 Kanten, zum Beispiel Vorzeichen → Minusklammer → Verteilen. *Quelle:* MA-Remediation geht über Schlüssel-Voraussetzungen zurück.
- **Abstände in Kalendertagen, Tageslast in Lerntagen.** *Eigene Ableitung:* Vergessen hängt an der Zeit (MA: Gedächtnis halbiert sich je Intervall in *Tagen*; FSRS: t in Tagen), die Belastbarkeit am Lerntag.

### (a) Gutschrift nach unten, Regel-Fehler nach oben
1. **Gutschrift:** Eine Aufgabe einer Etappe ist *im ersten Versuch, ohne Tipp, richtig*. Für jede etikettierte Regel r:
   - Nur wenn seit der letzten gezählten Wiederholung von r mindestens **die Hälfte des aktuellen Abstands** vergangen ist: g(r) += Gewicht (1,0 oder 0,5). Sonst ist die Gutschrift 0, weil es zu früh ist.
   - **Höchstens 1 Gutschrift je Regel und Lerntag**, damit 10 Aufgaben an einem Tag nicht 10 Stufen bringen.
   - Erreicht g(r) den Wert 1: Regel eine Stufe höher, g(r) = 0, neues Fälligkeitsdatum.
   - Regel im Status *wackelt* oder Tempo *langsam*: **keine** implizite Gutschrift; sie braucht ausdrückliche Werkzeug-Aufgaben.
   - *Quellen:* FIRe (Gutschrift gewichtet nach unten; frühe Wiederholung abgewertet; bei Tempo < 1 keine implizite Gutschrift). *Eigene Ableitung:* „halber Abstand“ als einfacher Ersatz für die Gedächtnisformel; das Tageslimit gegen gehäuftes Üben.
2. **Regel-Fehler:** Ein Fehler zeigt ein bekanntes Fehlbild von Regel r.
   - Er wird auf r gebucht *und* bleibt bei der Etappe. Die bestehende Etappen-Regel (2 Fehler in Folge öffnen die Etappe) gilt weiter.
   - r fällt **eine Stufe** zurück. War r zum Zeitpunkt des Fehlers schon über das Doppelte seines Abstands überfällig, fällt es **zwei Stufen**. Ab Stufe 2 nach unten gilt r als *wackelt*.
   - *Quellen:* MA `decay` (Scheitern nach Überfälligkeit wirft weiter zurück); ALEKS-Check (Fehler → zurück in den Lernpfad); Alcumus (Gemeistertes kann herausfallen).
3. **Wirkung nach oben:** Kippt r auf *wackelt*, werden in den nächsten 2 Lerntagen Etappen-Wiederholungen **bevorzugt**, die r „tragen“ (höchstens 2 zusätzliche je Tag). Deren eigene Fälligkeit wird **nicht** zurückgesetzt; sie kommen nur früher dran.
   - *Quelle:* FIRe (Strafe läuft nach oben).
   - *Eigene Ableitung:* Bei Math Academy läuft die Strafe *nur* vom einfachen zum schweren Thema. Ein Fehler im schweren Thema wird dort **nicht** einer Voraussetzung angelastet, weil unklar ist, welche schuld war. Erst euer Fehlbild-Etikett macht diese Zuordnung möglich. Das ist eine Erweiterung, die eher von Eedi und Graspable Math kommt (Vorbericht), nicht von Math Academy.
4. **Fehler ohne erkanntes Muster** werden nur bei der Etappe gebucht. Keine Regel wird bestraft.

### (b) Weniger, aber wirksamere Wiederholungen
Tagesplan (bei euch höchstens 12 Wiederholungen je Lerntag):
1. Liste der fälligen Etappen (1-3-7-14-30 …) und fälligen Regeln.
2. **Gieriges Abdecken:** Wähle nacheinander die Wiederholungsaufgabe einer fälligen Etappe, deren Regel-Etiketten die meisten fälligen Regeln abdecken. Abgedeckte Regeln werden abgehakt (sie bekommen nach (a) Gutschrift, wenn die Aufgabe gelingt). Weiter, bis die Grenze erreicht ist oder alles abgedeckt ist.
   - *Quelle:* MA Repetition Compression, Schritt 1. *Eigene Ableitung:* gieriges Mengenabdecken statt Optimierung.
3. **Keine Regel verfällt:** Ist eine Regel seit 2 Lerntagen fällig und nicht abgedeckt worden, oder steht sie auf *wackelt*, kommt 1 ausdrückliche Werkzeug-Aufgabe in die „Tägliche Fünf“.
   - *Quelle:* MA („fällige Wiederholung nie verfallen lassen“); MA Tempo < 1.
4. **Neues hat Vorrang vor Rückstau:** Mindestens 1 neue Etappe auf 3 Wiederholungen. Wenn mehr fällig ist als die Grenze erlaubt, gilt als Reihenfolge: Überfälligkeit relativ zum Abstand, dann Zahl der abhängigen Etappen.
   - *Quelle:* MA (eine Lektion etwa alle 3 Wiederholungen, mindestens rund 25 % neu).
5. **Neue Etappen als Wiederholung nutzen:** Ist die nächste neue Etappe so wählbar, dass sie fällige Regeln trägt, wähle sie.
   - *Quelle:* MA (auch neue Lektionen räumen fällige Wiederholungen ab).
6. **Leiter verlängern:** Regeln 1 · 3 · 7 · 14 · 30 · **60 · 120 · 240** Tage. Etappen ebenso, aber ab Stufe 30 nur, solange keine Regel der Etappe *wackelt*. Sonst bleibt die Etappe bei 30.
   - *Quelle:* MA (Abstände bis über ein Jahr); ARRS (bis 56 Tage). *Eigene Ableitung:* Verdopplung.
7. **Tempo je Kind und Regel**, ohne Statistik, aus den letzten 10 Erstversuchen:
   - ≥ 9 richtig → *schnell*: bei Aufstieg eine Leiterstufe überspringen.
   - 7–8 → *normal*.
   - ≤ 6 → *langsam*: keine implizite Gutschrift, ausdrückliche Werkzeug-Aufgaben.
   - *Quelle:* MA (Tempo 2 zählt doppelt, 0,5 halb; unter 1 ausdrücklich). *Eigene Ableitung:* drei Stufen statt eines Faktors; die Schwierigkeit kommt aus euren Etiketten (leicht/mittel/schwer) statt aus Bevölkerungsdaten.
8. **Nach langer Pause (mindestens 14 Kalendertage ohne Lernen): Wiedereinstieg statt Rückstau.**
   - Am ersten Lerntag je Regel mit Status *sitzt* oder *fest* 1 Brückenaufgabe, höchstens 15 Aufgaben, etwa 15–20 Minuten.
   - Richtig: Regel gilt als pünktlich wiederholt (eine Stufe hoch).
   - Falsch: wie in (a).
   - Etappen, die über das Doppelte ihres Abstands überfällig sind, gehen eine Stufe zurück. Abgearbeitet werden sie mit der normalen Grenze, nicht alle auf einmal.
   - *Quellen:* ALEKS (Check nach 60 Tagen ohne Check); MA (Diagnose wiederholbar; `decay`); MA-Gedächtnis nach 2 Intervallen auf ein Viertel.
   - *Eigene Ableitung:* Schwelle 14 Tage und das Format.

### (c) „Eingangscheck Werkzeuge“
- **Aufgabentypen je Regel (3 vorbereiten):**
  - **A** Grundform, nur diese Regel.
  - **B** Brückenform: die Regel eingebettet in eine Etappen-Aufgabe, die *alle* Regel-Vorgänger mitnutzt. Es ist die *einfachste* Aufgabe, die eine Fachperson überzeugt; nicht die schwerste.
  - **C** Fehlerfalle mit typischem Fehlbild.
  - *Quelle:* MA-Fragenauswahl (einfachste überzeugende Frage, die alle Voraussetzungen übt; schwerste meiden).
- **Ablauf je Regel, in Reihenfolge des Regel-Vorgänger-Graphen:**
  1. Zuerst **B**. Richtig und ohne Hilfe: +1 für r *und* alle Regel-Vorgänger (rekursiv). Dann **C**.
  2. B falsch: Fehlbild-Zuordnung. −1 auf die Regel, *zu der das Fehlbild gehört*; ohne erkanntes Muster −1 auf r. Dann **A**.
  3. Schluss für r, sobald |Bilanz| ≥ 2 ist oder 3 Aufgaben gestellt sind.
  4. Regeln, deren Bilanz durch Vererbung schon ≥ +2 ist, bekommen nur noch **C**.
  - *Quellen:* MA Plus-Minus-Bilanz (richtig wirkt nach unten, falsch nach oben); ALEKS-Ende („kein Item mehr unsicher“ oder Höchstzahl).
- **Wertung:**
  - richtig = +1; richtig, aber deutlich über der Zielzeit = +0,5;
  - falsch oder „weiß nicht“ = −1. Den „Weiß nicht“-Knopf gibt es **nur hier**, gegen Raten.
  - *Quelle:* MA (langsam richtig wiegt weniger; „weiß nicht“ nur in der Diagnose; höchstens 3 Minuten je Frage).
- **Ergebnis je Regel:**
  - Bilanz ≥ +2 → *sitzt (bedingt)*. Die Bedingung entfällt beim ersten Regel-Fehler im Alltag, die Regel fällt dann auf *wackelt*.
  - 0 bis +1 → *wackelt*.
  - ≤ −1 → *offen* → Werkzeug-Training vor Etappen, die diese Regel tragen.
  - *Quelle:* MA „bedingt erledigt“ und „konservativer Rand“.
- **Form:**
  - Freie Eingabe des Ergebnisses, Rechnen auf Papier. Auswahlantworten nur mit Fehlbild-Ablenkern und zusätzlich mit Pflicht-Eingabe.
  - *Quelle:* ALEKS (freie Formate, Ratewahrscheinlichkeit nahe 0); Matuschak (Schwäche von Multiple Choice).
- **Umfang:** im Mittel etwa 25–35 Aufgaben, höchstens 45 [A, geschätzt]. Aufgeteilt auf **2 Sitzungen à etwa 25 Minuten**.
- **Wiederholen:** nach jeder Pause von mindestens 14 Tagen in der Kurzform (siehe b8) und sonst etwa alle 8 Wochen.
  - *Quelle:* ALEKS 60-Tage-Regel. *Eigene Ableitung:* die 8 Wochen.

### (d) „Fest genug“ messbar machen
Gezählt werden nur **Erstversuche ohne Tipp**. Bewertet werden **die letzten Vorkommen**, nicht die Summe (MA: ✖✔✖✔✔ ≠ ✔✔✖✔✖).

| Merkmal | Messregel (Startwert) | Stütze |
|---|---|---|
| 1 Erster Versuch ohne Tipp | Nur solche Versuche zählen. Tipp angesehen zählt wie falsch für die Serie. | ASSISTments (Tipp setzt Serie zurück); ALEKS (Erklärung streicht Bonus); Bastani (Vorbericht) |
| 2 Gemischt | Mindestens 2 der richtigen Versuche außerhalb des Etappen-Blocks (Tägliche Fünf, Quiz) | MA-Quiz, Mischen (Rohrer zitiert in MAW) |
| 3 Verteilt über Wochen | Richtig an mindestens 3 verschiedenen Lerntagen über mindestens 21 Kalendertage, der letzte mindestens 7 Tage nach dem vorletzten | ARRS 7/14/28; ALEKS-Schwelle (Abstand wichtiger als Masse) |
| 4 Brückenform | Mindestens 1 richtige Brückenaufgabe (Regel in fremder Etappe) | MA-Diagnosefrage „übt alle Voraussetzungen“; Kelly 2015 (Transfer) |
| 5 Ohne Fehlbild | In den letzten 14 Kalendertagen kein Fehlbild dieser Regel | Eigene Ableitung (Eedi-Prinzip, Vorbericht) |
| 6 Auf Papier | Mindestens 1 richtige Lösung in einer Papier-Probe in Zeit, von einem Elternteil eingetragen | MA-Quiz in Zeit; MAW-Prüfungsvorbereitung |
| (7 Zeit) | Sobald gespeichert: Median der letzten 5 Antwortzeiten unter der Zielzeit der Regel | MA (zu langsam = nicht beherrscht) |

Stufen:
- *gelandet* (eure Landung, 6 Punkte)
- → *sitzt*: Merkmale 1, 2 und 3 in Kurzform (2 Lerntage, mindestens 7 Tage Abstand)
- → *fest*: alle 6 Merkmale
- Ein späterer Fehler mit Fehlbild stuft *fest* auf *sitzt* zurück, ein zweiter auf *wackelt*.
- [M] Bei der Etappe zusätzlich: die „5-in-Folge-Lehre“ von Kelly nicht durch mehr Aufgaben am Stück umsetzen, sondern durch Merkmal 3 und 4.

### (e) Remediation zur Regel statt zur Etappe
1. **Erste Etappen-Öffnung** (2 Fehler in Folge, ohne Fehlbild): keine sofortige Nachhilfe. Wechsel auf ein *nicht verwandtes* Thema, Neuversuch am nächsten Lerntag.
   - *Quelle:* MA (Pause und später neu, rund 80 % bestehen dann).
2. **Fehler mit Fehlbild:** sofort **1 Gegenaufgabe** zur Regel (Grundform), Buchung nach (a).
   - *Quelle:* Eedi (Vorbericht); MA (verpasste Quizfrage löst sofort eine Wiederholung aus).
3. **Regel-Remediation wird ausgelöst**, wenn (i) dieselbe Etappe zum zweiten Mal öffnet oder (ii) dasselbe Fehlbild einer Regel in 2 verschiedenen Etappen innerhalb von 7 Lerntagen auftritt.
   - Ist das Fehlbild bekannt, geht es zur zugehörigen Regel.
   - Sonst: je 1 Brückenaufgabe zu den (höchstens 3) Regel-Etiketten der Etappe. Die erste, die scheitert, wird bearbeitet.
   - Bestehen alle, liegt das Problem *in der Etappe selbst*. Dann die Etappe für die Eltern markieren: mehr Gerüst, Zwischenschritt einfügen, teilen.
   - *Quellen:* MA (zweimal gescheitert → Schlüssel-Voraussetzungen des Wissenspunkts; strauchelt der Inhalt, wird er verbessert, die Messlatte nicht gesenkt).
4. **Werkzeug-Training (Regel-Block):**
   - 1 Erklärkarte der Regel, dann Grundform-Aufgaben bis **3 richtig in Folge ohne Tipp**, dann 2 Brückenaufgaben.
   - Höchstens 10 Aufgaben, sonst „morgen wieder“ und Hinweis an die Eltern.
   - Danach zurück zur Etappe.
   - *Quelle:* ASSISTments Skill Builder (3 in Folge, 10 Aufgaben, „morgen wieder“).
5. **Scheitert das Werkzeug-Training zweimal:** eine Stufe zurück im Regel-Vorgänger-Graphen (zum Beispiel Minusklammer → Vorzeichen), dort gleiches Verfahren.
   - *Quelle:* MA (Remediation kann mehrere Schritte zurückgehen).
6. **Eltern-Hinweis:** bei 3 Öffnungen derselben Etappe, bei 2 gescheiterten Werkzeug-Trainings, oder wenn mehr als 1 von 10 Etappen in 2 Wochen öffnet.
   - *Quelle:* MA-Warnzeichen (über 1 von 10 Lektionen gescheitert).

### (f) Bewusst NICHT nachbauen
- **ALEKS-Wissenszustände und Bayes-Diagnose:** braucht Zustandsmengen und Fehlerraten aus Massendaten. Ersatz: Plus-Minus-Bilanz (siehe 2).
- **BKT mit gefitteten Parametern (MATHia):** Raten, Flüchtigkeit und Lernrate je Fertigkeit lassen sich bei zwei Kindern nicht schätzen. Ersatz: Serien- und Merkmalsregeln. Kelly 2015 fand 3-in-Folge ohnehin gleich gut wie BKT für die nächste Aufgabe.
- **FSRS-Optimierer und Duolingo-HLR:** brauchen viele Wiederholungsdaten je Person. Die FSRS-Standardgewichte stammen von Karteikarten und sind nicht auf Mathe-Regeln übertragbar [A]. Die *Idee* „späte bestandene Wiederholung zählt mehr“ kann man übernehmen, die Formel nicht.
- **Stufenlose „umfasst“-Gewichte zwischen allen Etappen und Weitergabe über viele Stufen:** Das sind 716² mögliche Paare. Ersatz: 0 / 0,5 / 1 nur zu den 15 Regeln, eine Stufe tief.
- **Lerntempo aus der Schwierigkeit aller Lernenden:** keine Bevölkerung. Ersatz: Schwierigkeits-Etikett von euch plus drei Tempostufen je Kind.
- **Vorausschauende Optimierung der Kompression:** gieriges Abdecken reicht.
- **Neuronales Abbruchkriterium, Elo-Werte für Aufgaben (Alcumus):** brauchen kalibrierte Aufgabenwerte aus vielen Antworten.
- **XP, Ligen, negative XP:** Das sind Werkzeuge gegen anonyme „XP-Hacker“ (MAW Kap. 22). Bei zwei Kindern mit Eltern daneben reicht die Absprache [M]. Allenfalls die *Idee* „XP ≈ konzentrierte Minuten“ als Tempomaß übernehmen.

### Erwartbarer Nutzen und Grenzen [M]
- Nutzen: weniger ausdrückliche Wiederholungen, weil Regeln über Etappen „mitlaufen“; ein klarer Rückweg bei Fehlern; Messbarkeit von „fest“.
- Grenze: Verständnis, Begründen, Textaufgaben und unbekannte Aufgaben deckt das Regelwerk nicht ab (Einwände Pershan, Matuschak). Dafür braucht ihr die Papier-Proben im Schulaufgaben-Format mit unbekannten Aufgaben und Begründungsteilen.
- Risiko implizite Gutschrift (Matuschak): Deshalb bekommt jede Regel spätestens **alle 30 Kalendertage 1 ausdrückliche Aufgabe in der Tägliche-Fünf-Mischung**, auch wenn sie implizit „bedient“ wurde [eigene Ableitung].

---

## 10. Rechtliches (nur wiedergegeben, keine Rechtsberatung)

- **The Math Academy Way [G]:** Urheberrecht bei Math Academy LLC. Der Vermerk im PDF erlaubt kurze Zitate in kritischen Besprechungen und bestimmte andere nichtkommerzielle Nutzungen im Rahmen des Urheberrechts; für alles andere ist eine Genehmigung anzufragen (Vermerk im PDF laut Suchtreffer-Auszug, MAW). Eine offene Lizenz gibt es **nicht**. Die FIRe-Umsetzung ist laut Blog proprietär (FIRe-Blog).
- **Patente:**
  - Für Math Academy und für ALEKS/McGraw Hill habe ich in meiner Websuche **kein Patent gefunden**. Das ist keine Patentrecherche: Google Patents, DEPATISnet oder Espacenet habe ich nicht systematisch abgefragt. Das Ergebnis ist also „nicht gefunden“, nicht „nicht vorhanden“.
  - Im Vorbericht ist für Squirrel AI US 12,260,638 B1 erwähnt (nicht von mir geprüft).
- **Offen:**
  - Knowledge Space Theory ist in Fachliteratur veröffentlicht (Doignon/Falmagne 1985, Bücher 1999/2011), und es gibt freie Software dazu (R-Paket kstMatrix auf CRAN, Lizenz nicht geprüft).
  - BKT und HLR sind veröffentlichte Verfahren; der HLR-Code liegt auf GitHub (`duolingo/halflife-regression`, Lizenz nicht geprüft).
  - FSRS (fsrs4anki) steht unter **MIT-Lizenz** (FSRS-Repo).
  - Die ASSISTments-Regeln (3 in Folge, 7/14/28/56) sind in Blogbeiträgen öffentlich beschrieben.
- **Ideen und Texte auseinanderhalten [A, allgemeines Rechtswissen, nicht geprüft]:**
  - Das Urheberrecht schützt die konkrete Formulierung (Texte, Aufgaben, Grafiken, Code), nicht Ideen, Lernprinzipien oder Verfahren an sich. Die Regeln oben in eigenen Worten und mit eigenen Aufgaben umzusetzen, ist etwas anderes, als Texte oder Aufgaben aus MAW oder den Systemen zu übernehmen. Letzteres solltet ihr nicht tun.
  - Verfahren *können* patentiert sein. In Deutschland sind private Handlungen zu nichtgewerblichen Zwecken nach meinem Wissen von der Patentwirkung ausgenommen (§ 11 Nr. 1 PatG). Für eine reine Familien-App wäre das voraussichtlich unkritisch.
  - Sollte die App je verkauft oder öffentlich angeboten werden, wäre eine echte Patent- und Markenrecherche nötig. „ALEKS“, „Math Academy“, „FIRe“ und „Alcumus“ als Namen nicht verwenden.

---

## 11. Math Academy – Vertiefung und Testmonat

Zusatzauftrag. Abruf aller Quellen 25.11.2026. Kennzeichnung wie oben ([G] gesichert, [A] Annahme, [M] Meinung/Ableitung).
Zusätzliche Quellen:
- MA-Kurse = https://mathacademy.com/courses, Kursseiten https://mathacademy.com/courses/5th-grade-math, …/7th-grade-math, …/8th-grade-math, …/prealgebra, …/algebra-i
- MA-Start = https://mathacademy.com/ · MA-HowItWorks = https://mathacademy.com/how-it-works
- MA-AGB = https://mathacademy.com/terms-of-service · MA-Datenschutz = https://mathacademy.com/privacy-notice
- WTM = https://forums.welltrainedmind.com/topic/733445-my-ongoing-review-of-mathacademycom-updated-62824 (Elternbericht, Stand 18.07.2024)
- LW = https://www.lesswrong.com/posts/HxtYuHpa3jzrWsrdm/my-first-month-with-math-academy-an-experience-report-from-a (Erfahrungsbericht eines Erwachsenen, aus dem Chinesischen)
- Multistep = https://justinmath.com/the-future-of-multistep-tasks-on-math-academy/
- LP-Gym5 = https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/5/mathematik · LP-Gym8 = https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/8/mathematik

### 11.1 Kursangebot und Zuordnung zu Gymnasium Bayern

**Kursliste [G, MA-Kurse]**
- *Grundschule:* 4th Grade Math (mehrstellige Rechnungen, Brüche, Dezimalzahlen, Geraden und Winkel; setzt das Einmaleins bis 12 voraus), 5th Grade Math.
- *Mittelstufe:* 6th, 7th und 8th Grade Math sowie Prealgebra. Prealgebra fasst den Stoff von Klasse 6–8 gestrafft zusammen.
- *Oberstufe, klassische Folge:* Algebra I → Geometry → Algebra II → Precalculus.
- *Oberstufe, integrierte Folge:* Integrated Math I–III, auch als „Honors“ (vier Jahre Stoff in drei).
- *Prüfungsvorbereitung und AP:* SAT/ACT Fundamentals/Prep, AP Calculus AB/BC.
- *Für Erwachsene:* Mathematical Foundations I–III, Teil I beginnt bei Brüchen.
- *Universität:* Calculus I/II, Linear Algebra, Multivariable Calculus, Methods of Proof, Differential Equations, Discrete Math, Probability & Statistics, Math for Machine Learning, Math Methods for Physical Sciences I/II, Abstract Algebra („coming soon“).

**Themenzahl und Inhalt der passenden Kurse [G, Kursseiten]**

| Kurs | Themen | Einheiten (Auswahl) |
|---|---|---|
| 5th Grade Math | 133 | Zahlsystem mit Einführung negativer Zahlen und Betrag, ganze Zahlen ×/÷, Brüche (+/−, ×/÷), Dezimalzahlen, Potenzen, Messen und Daten mit Koordinaten, Geometrie (Volumen, ebene Figuren). Teilbarkeit und Primfaktorzerlegung **nicht** genannt. |
| 7th Grade Math | 170 | Verhältnisse/Proportionalität, Zahlsystem (hier erst **Addieren und Multiplizieren negativer Zahlen**), Terme und Gleichungen (auch erste Gleichungssysteme), Geometrie (Kreisumfang und -fläche), Statistik und **Wahrscheinlichkeit** (11 Themen). Keine Konstruktionen. |
| 8th Grade Math | 132 | reelle Zahlen, Potenzen/wissenschaftliche Schreibweise, Wurzeln, Zahlentheorie, lineare Gleichungen mit Gleichungssystemen (Einsetzen, Gleichsetzen/Addition), Funktionen, Abbildungen/Kongruenz/Ähnlichkeit, Pythagoras und Volumen (Zylinder, Kegel, Kugel), bivariate Statistik. **Keine** Wahrscheinlichkeit, **keine** Bruchterme. |
| Prealgebra | 210 | Verhältnisse/Prozent, Zahlsystem, Potenzen/Wurzeln, Terme, Gleichungen/Ungleichungen mit Einführung in Gleichungssysteme, Geometrie (48), Statistik. Keine Wahrscheinlichkeit, keine Kreisfläche. |
| Algebra I | 225 (Summe von mir) | Gleichungen/Ungleichungen, Gleichungen mit zwei Variablen mit 13 Themen Gleichungssysteme, Einheiten, Wurzelterme, Bruchterme und -gleichungen (7), Funktionen, Betrag, Exponentialfunktionen, Polynome, quadratische Gleichungen/Funktionen (37), Folgen, bivariate Statistik. Keine Wahrscheinlichkeit. |

**Gymnasium Bayern zum Vergleich [G, LP-Gym5, LP-Gym8]**
- *Klasse 5:* natürliche und **ganze** Zahlen mit Addition/Subtraktion, Zahlengerade, Betrag, einfache Gleichungen, Klammern (ca. 30 Std.). Geometrische Figuren, Koordinatensystem, Winkel (ca. 14). Multiplikation/Division ganzer Zahlen mit **Vorzeichenregeln**, Primfaktorzerlegung, Teilbarkeit, Zählprinzip/Baumdiagramm, Potenzen, Distributivgesetz (ca. 34). Größen, Dreisatz, Maßstab, Flächeninhalt, Quaderoberfläche (ca. 34). Brüche kommen erst in Klasse 6 [A, Lehrplanwissen; die Seite zu Klasse 6 habe ich nicht abgerufen].
- *Klasse 8:* Funktion und Term (8 Std.), lineare Funktionen mit Ungleichungen (16), gebrochen-rationale Funktionen a/(x+b)+c (13), Bruchterme und Bruchgleichungen mit Potenzen ganzzahliger Exponenten und Formelumstellen (13), Laplace-Experimente mit Baumdiagramm und Zählprinzip (14), lineare Gleichungssysteme (10), Kreis und Zylinder (10).

**Zuordnung [M, nur aus Kurstiteln und Themenlisten abgeleitet, nicht im Produkt geprüft]**
- *Klasse 5 Bayern* entspricht **keinem** Kurs genau. Am nächsten kommt **5th Grade Math**: Zahlsystem, Potenzen, Flächen. Dazu fehlen das Rechnen mit negativen Zahlen (bei MA erst in 7th Grade) sowie Teilbarkeit und Primfaktoren. Umgekehrt ist mit Brüchen und Dezimalzahlen viel Stoff aus Klasse 6 dabei.
- *Klasse 8 Bayern* verteilt sich auf **8th Grade Math** (lineare Funktionen, Gleichungssysteme, Zylinder) und **Algebra I** (lineare Ungleichungen, Bruchterme und -gleichungen, Funktionsbegriff). Laplace-Wahrscheinlichkeit steht bei MA in 7th Grade. Gebrochen-rationale Funktionen mit Asymptoten liegen vermutlich erst in Algebra II/Precalculus [A, nicht geprüft]. Für einen Testmonat mit dem älteren Kind halte ich **Algebra I** für sinnvoll, wenn Klasse 7 (Terme, lineare Gleichungen) sitzt, sonst **8th Grade Math**. Die Diagnose empfiehlt selbst einen Kurs (MA-FAQ).

**Größte Abweichungen zur deutschen Reihenfolge [M, auf Basis der Listen oben]**
1. *Negative Zahlen:* Bayern rechnet damit voll in Klasse 5, MA erst in 7th Grade. 5th Grade führt sie nur ein.
2. *Brüche und Dezimalzahlen:* bei MA in 4th/5th Grade, in Bayern Klasse 6.
3. *Algebra:* Bayern hat Terme und lineare Gleichungen in Klasse 7, Funktionen, Gleichungssysteme und Bruchterme in Klasse 8. In den USA stehen lineare Gleichungen und Systeme in 7th/8th Grade und Algebra I, quadratische Funktionen bereits in Algebra I (Bayern Klasse 9).
4. *Geometrie:* Bayern konstruiert mit Zirkel und Lineal, Dreiecke und Kongruenz in Klasse 7 [A]. MA listet in 7th/8th Grade und Prealgebra **keine Konstruktionen**. Dafür gibt es Abbildungen (Transformations) und einen eigenen Geometry-Kurs nach Algebra I.
5. *Stochastik:* Bayern hat Laplace und Baumdiagramm in Klasse 8, MA Wahrscheinlichkeit in 7th Grade. MA hat mehr beschreibende und bivariate Statistik (Streudiagramme), die in Bayern kaum vorkommt.
6. *Schreibweisen:* Dezimalpunkt statt Komma. Algebra I hat eine eigene Einheit „Units“ mit 13 Themen; ob dort US-Einheiten vorkommen, habe ich nicht geprüft [A].

### 11.2 Ablauf aus Sicht des Kindes

**Diagnose [G]**
- Adaptiv, prüft auch Grundlagen früherer Klassen (MA-AI).
- Umfang: 20–40 Fragen in unteren Kursen, 40–60 in oberen; höchstens etwa 3 Minuten je Frage. „Weiß nicht“ ist erlaubt und erwünscht statt Raten (MAW-FAQ).
- Dauer laut Nutzerberichten: Eine Mutter schätzte eine Neu-Diagnose nach Kurswechsel auf **rund 3 Stunden** (WTM). Im „Holistic Mode“ sind es bis etwa 80 Fragen in 3 Stunden (LW).
- Danach gibt es einen Bericht mit Kursempfehlung und voraussichtlichem Enddatum bei verschiedenen täglichen XP-Mengen (MA-FAQ).
- Ob man die Diagnose unterbrechen kann: **nicht gefunden**.

**Aufgabentafel [G, MA-HowItWorks]**
- Das Kind wählt aus mehreren angebotenen Aufgaben. Sie unterscheiden sich in Thema, Art (Lektion, Wiederholung, Multistep, Quiz) und XP.

**Lektion [G, MAW-FAQ, MA-AI]**
- 3–4 Wissenspunkte. Jeder hat ein Musterbeispiel und dann 2–5 Fragen. Nach Fehlern kommen mehr Fragen, bei hoher Trefferquote weniger.
- Keine Videos; die Lektionen werden gelesen (WTM).
- Keine Tipps. Nach jeder Antwort wird die Lösung erklärt; Pershan beschreibt den Ablauf Einführung → Beispiel → Übung.

**Wiederholung (Review) [G]**
- Gemischte Aufgaben zu fälligen Themen; nie dieselbe Aufgabe wie in der Lektion (MAW-FAQ).
- Gibt etwa 5–10 XP: Heckers veröffentlichtes Aktivitätsprotokoll zeigt 7/5 und 10/8 XP für Reviews und rund 18–25 XP für Lektionen (https://frankhecker.com/assets/texts/math_academy_activity_log_frank_hecker_7-23-2026.pdf).

**Quiz [G, MA-FAQ, MAW-FAQ]**
- Etwa alle 150 XP. Zeitbegrenzt, gemischt über alles Gelernte, ohne Hilfe, kein „weiß nicht“. Zu langsam zählt wie falsch.
- Verpasste Fragen lösen sofort Wiederholungen aus. Ein Neuversuch mit anderen Fragen kommt nach den Wiederholungen.
- Zeitgrenzen sind für Kinder mit Nachteilsausgleich in den Einstellungen anpassbar.
- Beispiel aus einem Bericht: 8 Fragen in 14 Minuten (LW).

**Multistep [G, Multistep]**
- Eine Mini-Projektaufgabe in 8–12 kleinschrittigen Fragen.
- Bisher vor allem in AP Calculus BC und einigen unteren Kursen. Geplant ist etwa eine je 100 XP.

**XP und Tagesziel [G, MA-FAQ, MAW]**
- 1 XP ≈ 1 Minute konzentrierte Arbeit. Empfohlen sind 20–40 XP pro Tag an 3–5 Tagen; weniger als 3 Tage pro Woche wird nicht empfohlen.
- Bonus-XP bei fehlerfreier Arbeit, keine XP bei abgebrochener Lektion, negative XP bei Raten oder Hinwerfen.
- Wöchentliche Ligen sind optional.
- Eine Mutter maß **2–3 Minuten je XP** bei ihrem Sohn (WTM); ein Erwachsener kam auf etwa 0,8 XP pro Minute (LW).

**Eingabe [G]**
- „Größtenteils Multiple Choice“, gelegentlich getippte Antworten (WTM). Pershan: Übung „largely multiple choice“. Skycak selbst sagt sinngemäß, viele Themen hätten noch Auswahlfragen (https://justinmath.com/math-academy-podcast-clip-transcripts/). In LW wird geklickt; ein Fehlklick lässt sich nicht zurücknehmen.

**Rechenweg [G]**
- Es wird **kein** Rechenweg verlangt oder geprüft; das ist mir aus keiner Quelle bekannt.
- Der Anbieter empfiehlt Papier und Bleistift; einen Taschenrechner braucht man erst ab Trigonometrie (MA-FAQ).
- [G, WTM] Warnsignal aus der Praxis: Ein Sohn löste Aufgaben in 30–60 Sekunden, indem er Muster in den Antwortoptionen ausschloss. **Auf Papier konnte er nicht anfangen.** Die Familie wechselte nach einem Monat zurück.

### 11.3 Nach einem Fehler und nach wiederholtem Scheitern [G]
- *Einzelner Fehler in der Lektion:* Erklärung der Lösung, dann eine weitere Frage zu diesem Wissenspunkt (MA-AI).
- *Zu viele Fehler:* Die Lektion bricht ab, ohne XP. Es folgt eine Pause mit anderen Themen; die Lektion kommt nach einigen Tagen wieder, mit vorgezogener Wiederholung der Voraussetzungen (MA-FAQ). Laut MAW bestehen dann etwa 80 % ohne weitere Hilfe.
- *Zweimal am selben Wissenspunkt gescheitert:* Hilfs-Wiederholungen zu den Schlüssel-Voraussetzungen, dann der Neuversuch (MAW Kap. 4/21).
- *Quizfehler:* sofort eine Wiederholung zu diesem Thema (MA-AI).
- *Nutzersicht:* Nach einem Fehler kommen Zusatzaufgaben, XP gibt es aber erst am Ende. Ein Kind kann 30 Minuten arbeiten und 0 XP bekommen; das frustrierte (WTM).

### 11.4 Was Eltern sehen [G]
- **Aufsichtskonto** („oversight account“) für Eltern, Lehrkräfte oder Tutoren: XP-Ziele und Lerntage einstellen, **Ferien und Pausen** eintragen, Fortschritt mit einer Lehrkraft teilen (MA-FAQ).
- Laut Startseite: Tagesaktivität und Gesamtfortschritt verfolgen, tägliche und wöchentliche Benachrichtigungen, Ereignis-Hinweise (MA-Start).
- Wissensgraph: Kinder sehen den Kursgraphen mit etwa 300 Themen, die sich beim Lernen füllen (https://justinmath.com/transcript-cs-primer-show-23). Ob Eltern ihn gesondert sehen: nicht gefunden.
- **Export: nicht gefunden.** Hecker hat ein Aktivitätsprotokoll als PDF veröffentlicht (Link oben). Ob es eine eingebaute Druck- oder Exportfunktion ist oder ein Ausdruck aus dem Browser, ist unklar [A].
- Datenschutz [G, MA-Datenschutz]: Kinder legen beim ersten Login einen **anonymen Benutzernamen** an. **XP und Ranglisten sind für alle Nutzer sichtbar** und können auch außerhalb öffentlich sein. Die Server stehen in den USA.

### 11.5 Geräte
- **Nicht gefunden:** In FAQ und Startseite steht nichts zu App, Handy, Tablet oder Offline-Nutzung. In den App-Stores fand ich nur gleichnamige fremde Apps.
- [A] Die Nutzung läuft nach allen Beschreibungen über den Webbrowser. Eine Drittseite nennt „Computer oder iPad“ als nötige Ausstattung (Suchtreffer think.recess.gg, Seite ließ sich nicht öffnen, ungeprüft). Offline-Nutzung ist nirgends erwähnt; ich gehe davon aus, dass es sie nicht gibt [A]. Für die Reise heißt das: Internet nötig.

### 11.6 Eignung für 11 und 14 Jahre mit Deutsch als Muttersprache
- [G] Alter: Der Anbieter nennt kein Mindestalter. Der Stoff beginnt bei 4th Grade; vorausgesetzt wird das Einmaleins bis 12 (MA-FAQ). Ein Konto muss ein Erwachsener anlegen, Minderjährige nur mit dessen Beteiligung (MA-AGB Abschn. 2/4).
- [G] Textlast: keine Videos, nur gelesene Erklärungen und Musterbeispiele. Ein Kind (15) überflog die Erklärungen, sodass die Mutter mehrmals am Tag helfen musste (WTM). Der Anbieter sieht Hilfe von Erwachsenen anfangs nach jeder Aufgabe, dann ausschleichend bis wöchentlich, und mindestens wöchentliche Kontrolle vor (MAW-FAQ).
- [M] Englisch-Niveau: Ein Sprachniveau nennt keine Quelle. Meine Einschätzung: Musterbeispiele sind kurz und formelnah, aber Fachwörter (quotient, numerator, least common multiple, inequality) und Textaufgaben brauchen etwa **B1**. Für das 14-jährige Kind mit Schulenglisch und einer Fachwort-Liste dürfte das machbar sein. Für das 11-jährige Kind mit voraussichtlich etwa A2 wäre es ohne Elternteil daneben vermutlich zu schwer und würde Englisch statt Mathe üben.
- **Elternberichte (alle [G], einzeln, nicht repräsentativ):**
  - *Positiv:* klare Oberfläche, XP und Ligen motivieren, weniger Klagen über Mathe, Wiederholung hilft beim Behalten. Ein Achtklässler schaffte Integrated Math 1–3 und 790 Punkte in SAT Mathe (WTM, Antwort einer anderen Mutter).
  - *Kritisch:* Raten über Antwortmuster, Papier-Transfer fehlte, kaum Beweise, Geometrie-Lücken (damals Kreisgleichung, HL-Kongruenz), XP-Frust, Fortschrittsfehler im System, eine Diagnose von 3 Stunden (WTM).
  - Ein Schüler aus dem Pasadena-Programm: Das XP-System sei „dumm“ und verleite dazu, XP statt Lernen zu jagen (zitiert bei Pershan).
  - Hecker als erwachsener Nutzer: Die Wiederholungsmenge sei angemessen, die Behauptung weniger Wiederholungen durch die Hierarchie „gerechtfertigt“ (https://frankhecker.com/2025/02/17/math-academy-part-10/, nur Suchtreffer-Auszug).

### 11.7 Preis, Geschwister, Kündigung, Test, Ausland
| Punkt | Stand | Quelle / Sicherheit |
|---|---|---|
| Preis | **49 USD pro Monat und Schüler**, als „Beta“ | MA-Start, abgerufen 25.11.2026 [G] |
| Künftiger Preis | Ein älterer Text der Startseite: Beta-Preis 49 USD, solange man das Abo hält; regulär „79 bis 99 USD/Monat“ | Suchtreffer-Auszug von www.mathacademy.com, Datum unbekannt [unsicher] |
| Jahrespreis | MAW (Arbeitsfassung, Stand 2025) nennt 499 USD/Jahr. Auf der Startseite habe ich keinen Jahrestarif gesehen. Die Preisseite ließ sich nicht abrufen (Fehler). | [unsicher] |
| Geschwister | „Keine Rabatte oder Kaufkraftpreise während der Beta“; ein Geschwisterrabatt ist nicht genannt → 2 Kinder ≈ 98 USD/Monat | MA-FAQ [G]; Rechnung [M] |
| Test | Kein Gratistest gefunden. Stattdessen **30 Tage Geld zurück**: volle, automatische, sofortige Erstattung bei Kündigung in den ersten 30 Tagen | MA-Start, MA-FAQ [G] |
| Nach 30 Tagen | Erstattung nur bei gemeldeten technischen Problemen. Verlängerungen sind „strikt“ nicht erstattbar. Kündigen mindestens 24 Stunden vor Verlängerung, Zugang bis Periodenende. | MA-FAQ; MA-AGB Abschn. 5/6 [G] |
| Pause | Abo **30–90 Tage pausierbar** (Kontoeinstellungen) – für die Reise wichtig | MA-FAQ [G] |
| Zahlung | Kreditkarte über Stripe; kein PayPal; **keine Prepaid-Karten** | MA-FAQ [G] |
| Ausland | Nicht ausdrücklich geregelt. Die Datenschutzerklärung spricht Nutzer aus EWR und UK an (Datenübertragung in die USA). Das deutet auf Nutzbarkeit im Ausland hin. Für einzelne Reiseländer oder einzelne Reiseländer: nicht gefunden. | MA-Datenschutz [G]; Schluss [A] |
| Recht und Streit | Kalifornisches Recht, Schiedsverfahren (JAMS, Los Angeles), keine Sammelklage, Widerspruch gegen das Schiedsverfahren binnen 30 Tagen ab erster Nutzung möglich | MA-AGB Abschn. 20 [G] |

### 11.8 Nutzungsbedingungen zu Inhalten (nur wiedergegeben) [G, MA-AGB]
- **Abschn. 7:** Zugang nur zu Bildungszwecken.
- **Abschn. 8 (verbotene Nutzung):** kein Kopieren, Verändern oder Ableiten von Werken aus dem Dienst; keine Entfernung von Schutzvermerken; keine kommerzielle Nutzung oder Weiterverkauf; **keine automatischen Werkzeuge** (Scraper, Bots, Crawler) zum Zugreifen, Kopieren oder Überwachen.
- **Abschn. 12 (geistiges Eigentum):** Inhalte gehören Math Academy oder Lizenzgebern; alle nicht ausdrücklich gewährten Rechte vorbehalten. Nutzung nur für die eigenen schulischen Zwecke bzw. die des Kindes; kein Vervielfältigen, Verbreiten, Bearbeiten.
- [M] Für euch heißt das: Aufgaben, Erklärtexte oder Musterbeispiele aus Math Academy nicht in die eigene App übernehmen, auch nicht abgewandelt, und keine Bildschirmfotos als Material. Beobachtungen der *Abläufe* (wie viele Fragen, was nach Fehlern passiert) als eigene Notizen festzuhalten, ist etwas anderes. Keine Rechtsberatung.

### 11.9 Belege und Kritik, verdichtet

**Was der Anbieter behauptet [G]**
- „4× schneller als Unterricht“ (MA-Start) und „garantiert“ der effizienteste Weg.
- Rechnung dazu: 6.000 XP AP Calc BC gegenüber 24.000 Minuten Unterricht (MA-FAQ).
- Pasadena: Achtklässler legen AP Calculus BC ab. Nach Einführung des Systems seien die Ergebnisse „in die Höhe geschnellt“ (https://justinmath.com/math-academy-success-stories/, https://www.justinmath.com/math-academys-eurisko-sequence-5-years-later).
- Alpha School nutze Math Academy als Hauptlehrplan für Klasse 4–12.

**Was Dritte berichten (nicht unabhängig geprüft) [G]**
- Das Programm in Pasadena ist ein Begabtenprogramm des Schulbezirks; die Washington Post nannte es 2022 „America’s most advanced math program“ (https://www.pasadenanow.com/main/?p=500360). Es wuchs von 14 auf 175 Kinder (Forumszitat des Post-Artikels, https://giftedissues.davidsongifted.org/bb/ubbthreads.php/topics/250051.html).
- Die erste Gruppe erreichte im PSAT das 98./99. Perzentil (https://outlooknewspapers.com/?p=3944).
- Eine Beratungsfirma nennt 75 % bestandene AP-Prüfungen und 50 % Note 5 in BC, ohne Quelle (https://www.ivyscholars.com/what-is-math-academy/).

**Methodische Einordnung [M]**
- Die Kinder in Pasadena waren ausgewählt; laut MAW war für den Zugang mindestens das 90. Perzentil im Einstufungstest nötig.
- Es gab dazu Lehrkräfte, zum Teil mit Doktortitel (https://sandy-roberts-haje.squarespace.com/faq).
- Eine Vergleichsgruppe fehlt. Was auf das System, was auf die Auswahl und was auf die Lehrkräfte entfällt, ist nicht trennbar.
- **Eine unabhängige, kontrollierte Studie gibt es nicht** (nicht gefunden, auch nicht im Vorbericht).

**Kritik [G, siehe Abschnitt 8]**
- Pershan: prozedural, Auswahlfragen, flaches Verständnis.
- Matuschak: keine Transferaufgaben, Black Box, Schwäche der Auswahlfragen.
- Dan Meyer (nur über Suchtreffer: „Direktunterricht für Verfahren, Entdecken für Begriffe“).
- WTM: Raten über Muster, kein Papier-Transfer.

[M] Für eure Frage (Papier-Schulaufgabe) ist der stärkste Einwand der WTM-Befund. Den Testmonat sollte man genau darauf ausrichten.

### 11.10 Prüfliste für einen Testmonat mit dem älteren Kind (Stand Klasse 8)

Rahmen [M]: Abo erst abschließen, wenn ein zusammenhängender Monat mit verlässlichem Internet bevorsteht. Die 30-Tage-Erstattung zählt ab Kauf. Kündigungsentscheidung spätestens an Tag 27. Täglich 30–40 XP an 5 Tagen. Ein Elternteil führt ein Protokoll (eine Tabelle, siehe unten). Keine Bildschirmfotos von Aufgaben weitergeben (AGB).

**Vorher (Tag 0): Papier-Arbeit A**
- 45 Minuten, ohne Hilfsmittel, Niveau Schulaufgabe Klasse 8.
- Je etwa 1/3:
  - (a) Themen, die Math Academy im Monat voraussichtlich üben wird: nach der Diagnose aus dem Kursplan wählen, zum Beispiel lineare Funktionen, Gleichungssysteme, Bruchterme.
  - (b) Grundregeln aus Klasse 5–7: Vorzeichen, Minusklammer, Bruchrechnen, Waage.
  - (c) Bayern-Themen, die Math Academy **nicht** übt, als Vergleich: zum Beispiel Laplace oder Konstruktion.
- Auf jeder Aufgabe eine Begründungs- oder Textaufgabe.
- Eine zweite, gleichwertige Arbeit **B** vorbereiten: dieselben Aufgabentypen, andere Zahlen und Kontexte.

**Woche 1: Diagnose und Einstieg**
- [ ] Welcher Kurs wurde gewählt bzw. empfohlen? Wie lange dauerte die Diagnose (Minuten), wie viele Fragen? Gab es eine Pause?
- [ ] Welche **Lücken aus Klasse 5–7** fand die Diagnose (Themenliste abschreiben)? Decken sie sich mit Teil (b) der Papier-Arbeit A?
- [ ] Wie oft drückte das Kind „weiß nicht“, und wie oft hat es geraten?
- [ ] Wie viele Fragen hatte eine Lektion im Mittel? Wie viele Wissenspunkte?
- [ ] Antwortform: Wie viel Prozent Auswahl, wie viel getippt (eine Stichprobe von 20 Aufgaben zählen)?
- [ ] Rechnet das Kind auf Papier, oder klickt es direkt? Wie lange braucht es je XP? (Uhr neben das Protokoll, Ziel: Minuten pro XP)
- [ ] Englisch: Wie viele Wörter musste es nachschlagen? Versteht es die Musterbeispiele ohne Hilfe?

**Woche 2: Fehler und Wiederholung**
- [ ] Wie viele Wiederholungen und wie viele neue Lektionen gab es je Tag (Verhältnis; MAW nennt etwa 1 Lektion auf 3 Wiederholungen)?
- [ ] **Derselbe Fehler zweimal:** Gezielt beobachten, was passiert, wenn das Kind am selben Wissenspunkt zweimal scheitert. Kommt eine Voraussetzung? Welche? Ist sie fachlich die richtige (aus Sicht eurer 15 Regeln)?
- [ ] Nach einer abgebrochenen Lektion: Wann kam sie wieder (nach wie vielen Tagen)? Wurde sie dann bestanden?
- [ ] Erstes Quiz: Wie viele Fragen, wie viele Minuten, wie viele in Zeit richtig? Was kam danach?
- [ ] Gab es einen Multistep? Wie viele Teilfragen?
- [ ] Wie fühlt sich das Tempo an (Kind, Skala 1–5: zu langsam … zu schnell)? Wie geht es ihm mit XP und Liga (Liga ggf. ausschalten)?

**Woche 3: Pause und Behalten**
- [ ] Bewusst **7 Tage Pause** (im Aufsichtskonto als Ferien eintragen). Danach festhalten: Wie viele Wiederholungen standen am ersten Tag an? Kam ein neuer Check? Wie war die Trefferquote am ersten Tag nach der Pause im Vergleich zur Woche davor?
- [ ] **Papier-Stichprobe:** 5 Aufgaben aus Themen, die Math Academy in Woche 1–2 als „bestanden“ führte, auf Papier ohne Auswahlantworten. Wie viele gelingen? (Kern-Test zum WTM-Befund.)
- [ ] Sieht man implizite Wiederholung, etwa ein früheres Thema, das nicht mehr als Review kommt, weil ein späteres es geübt hat? (Nur, wenn die Oberfläche es erkennen lässt.)

**Woche 4: Gesamtbild und Entscheidung**
- [ ] Welche Berichte und Benachrichtigungen bekamen die Eltern? Was davon war nützlich? Lässt sich etwas exportieren oder drucken?
- [ ] Summe: XP gesamt, reale Minuten gesamt, Zahl der Lektionen bestanden/abgebrochen, Quiz-Trefferquote.
- [ ] Ende Woche 4 (vor Tag 27): **Papier-Arbeit B** unter denselben Bedingungen wie A.
- [ ] Optional 3 Wochen nach Ende: 10 Aufgaben aus Teil (a), zum Behalten.

**Woran messen, ob es wirkt [M]**
- Vergleich A → B getrennt nach Teil (a) geübt, (b) Grundregeln und (c) nicht geübt. Teil (c) ist die eigene Vergleichsgruppe: Steigt nur (a), spricht das für Math Academy. Steigen alle Teile gleich, eher für Übungs- oder Gewöhnungseffekte.
- Bei einem Kind sind das Hinweise, keine Statistik. Als Faustregel würde ich (a) erst als „wirkt“ werten, wenn es mindestens 2 Aufgaben mehr richtig hat als (c) und die Begründungsaufgaben mitsteigen.
- Die Papier-Stichprobe aus Woche 3 zählt mehr als jede Zahl in der App.

**Entscheidung (a) Zweitsystem? [M]** Ja, wenn alle vier Punkte gelten:
- Papier-Stichprobe mindestens 4 von 5,
- Teil (a) steigt deutlich stärker als (c),
- Englisch ist für das Kind kein Hindernis,
- eine Stunde reale Arbeit bringt etwa 25–40 XP.

Dann mit klarer Rolle einsetzen: Algebra- und Funktionsübung auf Englisch, während eure App Bayern-Lehrplan, Konstruktion, Stochastik und Papierform abdeckt.

**Entscheidung (b) Welche Mechaniken übernehmen? [M]** Je Mechanik notieren: „hat bei uns gewirkt / gestört / nicht sichtbar“:
- Pause und später erneut nach einer abgebrochenen Lektion,
- Rücksprung zur Voraussetzung nach zweimaligem Scheitern,
- Quiz in Zeit mit sofortiger Wiederholung,
- Verhältnis neu zu Wiederholung,
- XP als Zeitmaß,
- Ligen.

### 11.11 Gutschrift nach unten und Strafe nach oben: so genau wie belegt, und vereinfacht durchgerechnet

**Was Math Academy veröffentlicht hat [G, FIRe-Blog, MAW Kap. 29, Hecker7]**
- *Gewichte:* 0–1 je „umfasst“-Kante, von Fachleuten geschätzt. Bedeutung: Anteil des einfachen Themas, der in einer Aufgabe des schweren Themas mitgeübt wird. Gesetzt nur bei Nicht-Trivialität, Nicht-Ableitbarkeit und Nähe; sonst 0.
- *Weitergabe über Stufen:* Volle Kanten (1) geben ungebremst weiter, Teilkanten verblassen.
  - Heckers Lesart der Kette: A→B 0,5 und B→C 0,4 ergibt A→C 0,2, also Produkt entlang des Pfads.
  - Beispiel im Buch: Eine Wiederholung von „partielle Integration“ gibt jedem teilweise umfassten Thema nur einen Bruchteil einer Wiederholung.
- *Abwertung früher Gutschrift:* Ist das Gedächtnis eines Themas noch hoch (Wiederholung zu früh), wird die Gutschrift gekürzt. Eine genaue Formel ist nicht veröffentlicht.
- *Gedächtnis:* memory · 0,5^(Tage/Intervall). Nach 1 Intervall bleibt 0,5, nach 2 Intervallen 0,25 (Hecker7).
- *Tempo:* Gutschrift × speed. Bei speed < 1 gibt es keine implizite Gutschrift.
- *Strafe nach oben:* Scheitert eine Wiederholung des einfachen Themas, erhalten die umfassenden (schwereren) Themen negative Gutschrift. Bei Überfälligkeit wirkt `decay` > 1 verstärkend.
- *Scheitern am schweren Thema:* Belegt ist nur die Strafe für das Thema selbst und für Themen *darüber*. Eine Strafe *nach unten* auf Voraussetzungen ist **nicht** beschrieben. Bei der Fähigkeitsmessung wirken falsche Antworten nach oben, richtige nach unten (MAW Kap. 29).
- **Nicht veröffentlicht:** Gewichtsformeln über mehrere Stufen, Abwertungsfunktion, Intervallfolge, Fälligkeitsschwelle.

**Zahlenbeispiel im Stil von Math Academy [M: eigene Beispielzahlen, nur zur Veranschaulichung der beschriebenen Logik]**
- Thema T3 „lineare Gleichung mit Minusklammer“ umfasst T2 „Minus vor Klammer auflösen“ mit Gewicht 1,0. T2 umfasst T1 „ganze Zahlen subtrahieren“ mit 0,5. T3 umfasst außerdem „Äquivalenzumformung“ mit 1,0.
- T3 wird bestanden (speed 1):
  - T2 bekommt 1,0 Wiederholung;
  - T1 bekommt 1,0 × 0,5 = 0,5;
  - die Äquivalenzumformung bekommt 1,0.
  - Hatte T2 seine letzte Wiederholung erst vor 0,3 Intervallen (Gedächtnis noch etwa 0,8), wird die Gutschrift gekürzt (Faktor unbekannt; nach Heckers Vermutung nahe 0 bei sehr früh).
- Scheitert dagegen eine Wiederholung von T2, bekommen T3 und alle Themen, die T2 umfassen, eine Strafe. T1 bleibt unberührt.

**Vereinfachte Fassung für 15 Grundregeln über 716 Etappen [M, Regeln aus Abschnitt 9a/9b]**

Voreinstellung:
- Regel-Leiter 1 · 3 · 7 · 14 · 30 · 60 · 120 · 240 Kalendertage.
- Gutschrift zählt nur, wenn mindestens die Hälfte des aktuellen Abstands vergangen ist; höchstens 1 je Regel und Lerntag.
- Gewichte „trägt“ = 1,0, „nutzt“ = 0,5.
- Strafe: eine Stufe zurück, zwei bei mehr als doppelter Überfälligkeit; Stufe ≤ 2 heißt *wackelt*, dann keine implizite Gutschrift.

Beispiel-Etappe „Gleichungen mit Klammern“, Aufgabe 3 − (2x − 5) = 4x + 2.
- Richtig: 3 − 2x + 5 = 4x + 2 → 8 − 2x = 4x + 2 → 6 = 6x → **x = 1**.
- Regel-Etiketten: Minusklammer 1,0 · Waage 1,0 · Vorzeichen 0,5.

Stand des Kindes heute (Kalendertag 0):

| Regel | Stufe / Abstand | letzte gezählte Wiederholung | Konto g | Status |
|---|---|---|---|---|
| Minusklammer | Stufe 3 / 7 Tage | vor 5 Tagen | 0 | sitzt |
| Waage | Stufe 5 / 30 Tage | vor 10 Tagen | 0 | fest |
| Vorzeichen | Stufe 4 / 14 Tage | vor 9 Tagen | 0 | sitzt |

**Fall A – im ersten Versuch, ohne Tipp, richtig (x = 1)**
- *Etappe:* gilt als gelöste Aufgabe bzw. Wiederholung nach eurer bestehenden Etappen-Logik.
- *Minusklammer:* 5 ≥ 7/2 = 3,5 → g = 0 + 1,0 = 1 → **Aufstieg auf Stufe 4 (14 Tage)**, g = 0, fällig an Tag 14.
- *Waage:* 10 < 30/2 = 15 → zu früh → **keine Gutschrift**, bleibt fällig an Tag 20.
- *Vorzeichen:* 9 ≥ 14/2 = 7 → g = 0 + 0,5 = **0,5**. Noch kein Aufstieg; die nächste passende Aufgabe (ab morgen, Tageslimit) mit Gewicht ≥ 0,5 hebt die Regel auf Stufe 5.
- *Folge für die Tagesplanung:* Die Minusklammer muss heute und an den nächsten 14 Tagen nicht mehr ausdrücklich wiederholt werden. Hätte das Kind eine Werkzeug-Aufgabe „Minusklammer“ auf dem Plan gehabt, entfällt sie (Verdichtung).

**Fall B – falsch mit erkanntem Fehlbild (x = −2/3)**
- *Rechnung des Kindes:* 3 − 2x − 5 = 4x + 2 → −2 − 2x = 4x + 2 → −6x = 4 → x = −2/3. Fehlbild „Minus vor Klammer nur auf das erste Glied angewendet“ → Regel **Minusklammer**.
- *Etappe:* Fehler 1. War schon der vorige Versuch falsch, öffnet die Etappe wieder (eure Regel).
- *Minusklammer:* nicht überfällig → **eine Stufe zurück: Stufe 3 → 2 (Abstand 3 Tage)**, Status **wackelt**, implizite Gutschrift aus. Sofort **1 Gegenaufgabe** Grundform, zum Beispiel „Löse die Klammer auf: −(2x − 5)“.
- *Waage, Vorzeichen:* **keine Buchung.** Der Fehler ist eindeutig der Minusklammer zuzuordnen; Gutschrift gibt es mangels richtiger Lösung auch nicht. Das entspricht Math Academy: keine Strafe nach unten ohne Grund.
- *Nach oben:* In den nächsten 2 Lerntagen werden höchstens 2 zusätzliche Etappen-Wiederholungen bevorzugt, die die Minusklammer „tragen“, zum Beispiel „Terme mit Klammern vereinfachen“ oder „Bruchgleichungen“. Deren eigene Fälligkeit bleibt.
- *Eskalation:* Tritt dasselbe Fehlbild innerhalb von 7 Lerntagen in einer **anderen** Etappe noch einmal auf, folgt **Werkzeug-Training Minusklammer**: Erklärkarte, Grundform bis 3 richtige in Folge ohne Tipp (höchstens 10 Aufgaben), dann 2 Brückenaufgaben. Scheitert das zweimal, geht es eine Stufe zurück zur Regel **Vorzeichen** (Abschnitt 9e).
- *Ausdrückliche Wiederholung:* Die Minusklammer bekommt in 3 Kalendertagen eine eigene Aufgabe in der Täglichen Fünf. Erst bei Erfolg steigt sie wieder; implizite Gutschrift gibt es erst ab Stufe 3.

**Fall C – falsch ohne erkanntes Muster (zum Beispiel x = 5)**
- Nur die Etappe bucht den Fehler. Keine Regel wird bestraft.
- Bei Wiederholung der Öffnung kommt die Mini-Diagnose aus 9e: je 1 Brückenaufgabe zu Minusklammer, Waage und Vorzeichen. Die erste, die scheitert, bekommt das Werkzeug-Training. Bestehen alle, wird die Etappe zur Überarbeitung markiert.

**Fall D – richtig, aber nach Tipp**
- Keine Regel-Gutschrift, keine Strafe. Für die Etappe zählt der Versuch nicht als „erster Versuch ohne Tipp“ (Merkmal 1 von „fest genug“).

[M] Unterschied zu Math Academy, bewusst gewählt: Math Academy rechnet mit stufenlosen Gewichten über mehrere Graph-Stufen und einer Gedächtnisformel. Die vereinfachte Fassung hat 2 Gewichte, nur eine Stufe (Etappe → Regel), eine Halber-Abstand-Regel statt Gedächtnisformel und eine Fehlerzuordnung über Fehlbilder. Die Fehlbild-Zuordnung hat Math Academy so nicht.

---

## Was ich nicht prüfen konnte
- MAW nur über Zusammenfassungen des Abrufwerkzeugs gelesen, nicht wörtlich. Die Kapitel 8–10 (rund 300.000–400.000 Zeichen) ausgelassen. Das PDF ließ sich nicht herunterladen (Proxy 403).
- Math Academy: genaue Formeln für Gutschrift, Intervall und Tempo, die Fragenreihenfolge und das Abbruchkriterium der Diagnose, eine KP-Schwelle in Zahlen, Quizlänge und Zeitgrenzen: **nicht veröffentlicht oder nicht gefunden**.
- Alcumus: Schwellen für Grün und Blau, Aktualisierungsschritt, Anteil der Wiederholungsaufgaben: nicht gefunden.
- MATHia: Umgang mit Tipps im BKT nur als Annahme. BKT-Formeln aus meinem Wissen, nicht von einer abgerufenen Seite.
- ARRS: Effektgrößen des RCT nicht auf der Seite. Primärpapier (Xiong/Heffernan) nicht gelesen.
- Kritische Texte: Pershan und Matuschak gelesen. Hecker Teil 11 nur aus dem Suchtreffer-Auszug, Teil 7 abgerufen. Dan Meyer und das LessWrong-Erfahrungsbericht nicht gelesen.
- Patente: keine systematische Patentdatenbank-Recherche. Lizenz von kstMatrix und HLR-Code nicht geprüft.
- Originalstudien zu Mischen und Abständen (Rohrer, Bahrick, Metaanalysen) nur als Zitat in MAW.
- Math Academy (Abschnitt 11):
  - Preisseite nicht abrufbar; Jahrestarif und künftiger Normalpreis unsicher.
  - Geräte, App und Offline-Nutzung: nicht gefunden.
  - Elternansicht und Export nur grob beschrieben.
  - Nutzbarkeit vom Ausland aus nicht bestätigt.
  - Ob man die Diagnose unterbrechen kann: nicht gefunden.
  - Englisch-Niveau ist meine Schätzung.
  - Kursinhalte nur aus den öffentlichen Themenlisten, nicht im Produkt gesehen. Algebra II/Precalculus (gebrochen-rationale Funktionen) und Lehrplan Klasse 6/7 Bayern nicht abgerufen.
  - Hecker Teil 9 und die Rezension auf recess.gg nicht abrufbar.
  - Pasadena-Ergebnisse nur aus Presse und Anbieter.
