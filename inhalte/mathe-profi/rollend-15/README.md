# rollend-15 – Klasse 7 und Klasse 9, Aufgaben in neuer Form (Kennungen R15-V001 bis R15-V207)

207 neue Aufgaben in 14 Einheiten (7 in Klasse 7, 7 in Klasse 9) für Etappen, in denen der Vorrat an Aufgaben in neuer Form am dünnsten ist. Auswahl und Zahlen vorher: `auswahl.md`. Alle Aufgaben sind eigene Erfindungen (eigene Zahlen, eigene Einkleidung, neutrale Namen), keine Schul- oder Prüfungsaufgaben. Nichts davon ist eingespielt; nur neue Dateien unter `inhalte/mathe-profi/rollend-15/`.

## Dateien

- `<einheit>.json`: je Einheit eine Datei im Format der Vorrats-Runden (von `bauen.py` erzeugt; nicht von Hand ändern).
- `th_<einheit>.py`: Quelltext der Aufgaben (Frage, Lösung, Tipp, Lösungsweg, Fehlbilder samt Rechnung). `kern.py`: Hilfsfunktionen (aus R14 übernommen und angepasst).
- `bauen.py`: schreibt die JSON-Dateien, `regeln.py` und `regeln-zuordnung.md` und prüft alles (Aufruf `python3 -I inhalte/mathe-profi/rollend-15/bauen.py`, muss mit `OK` enden).
- `regeln.py`, `regeln-zuordnung.md`: Regel-Kennung je Aufgabe (Verteilung, Ausnahmen, Aufgaben ohne Regel, Zweifelsfälle, Gesamtliste).
- `auswahl.md`: Auswahl der Einheiten mit den Zahlen vor Runde 15.

## Zahlen je Einheit

| Einheit | Klasse | Etappen | Aufgaben | davon Lückenweg (zählt nicht) | Stufe 1 / 2 / 3 | Kennungen |
|---|---|---|---|---|---|---|
| `bruch.prozent_grundwert` | 7 | 8 | 16 | 0 | 0 / 8 / 8 | V001 bis V016 |
| `terme.potenzgesetze_natuerlich` | 7 | 5 | 15 | 2 | 2 / 7 / 6 | V017 bis V031 |
| `terme.umformen` | 7 | 5 | 15 | 2 | 2 / 7 / 6 | V032 bis V046 |
| `abbildungen.kongruenz` | 7 | 6 | 14 | 2 | 2 / 6 / 6 | V047 bis V060 |
| `geometrie.winkelsaetze` | 7 | 9 | 18 | 2 | 2 / 9 / 7 | V061 bis V078 |
| `geometrie.konstruktion` | 7 | 5 | 15 | 2 | 2 / 7 / 6 | V079 bis V093 |
| `gleichungen.linear` | 7 | 6 | 17 | 2 | 2 / 7 / 8 | V094 bis V110 |
| `zahlen.wurzeln_basis` | 9 | 6 | 15 | 2 | 2 / 9 / 4 | V111 bis V125 |
| `zahlen.reell` | 9 | 8 | 14 | 2 | 3 / 7 / 4 | V126 bis V139 |
| `gleichungen.quadratisch` | 9 | 8 | 14 | 2 | 2 / 8 / 4 | V140 bis V153 |
| `funktionen.quadratisch` | 9 | 9 | 14 | 3 | 3 / 6 / 5 | V154 bis V167 |
| `trigo.pythagoras` | 9 | 6 | 12 | 2 | 2 / 6 / 4 | V168 bis V179 |
| `trigo.rechtwinklig` | 9 | 7 | 13 | 1 | 2 / 8 / 3 | V180 bis V192 |
| `stochastik.verknuepft` | 9 | 11 | 15 | 2 | 2 / 8 / 5 | V193 bis V207 |
| Summe | | | 207 | 26 | 28 / 103 / 76 | |

## Formen insgesamt

| Form | Aufgaben | Anteil |
|---|---|---|
| Anwenden | 94 | 45 % |
| Umkehren | 28 | 14 % |
| Verfahren wählen | 28 | 14 % |
| Lückenweg | 26 | 13 % |
| Fehler-Detektiv | 24 | 12 % |
| Brücke | 4 | 2 % |
| Zwei Wege | 3 | 1 % |

Lückenwege haben `zaehlt = nein` (Gerüst, Stufe 1), alle anderen `zaehlt = ja`. Je Etappe gibt es mindestens eine zählende Aufgabe auf Stufe 2 oder 3 (von `bauen.py` geprüft); je Einheit mindestens die Hälfte der Etappenzahl Aufgaben auf Stufe 3.

## Übersicht je Einheit und Etappe

Spalten: Aufgaben, Formen (L = Lückenweg, F = Fehler-Detektiv, V = Verfahren wählen, U = Umkehren, A = Anwenden), Stufen.

### bruch.prozent_grundwert (Klasse 7)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| faktor | V001, V002 | A F | 2 3 |
| vermehrt | V003, V004 | A A | 2 3 |
| vermindert | V005, V006 | A Z | 2 2 |
| zurueck | V007, V008 | U A | 2 3 |
| prozentsatz | V009, V010 | A B | 2 3 |
| mehrfach | V011, V012 | A U | 2 3 |
| formel | V013, V014 | Z U | 2 3 |
| argumente | V015, V016 | A V | 3 3 |

### terme.potenzgesetze_natuerlich (Klasse 7)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| mal_gleiche_basis | V017, V018, V019 | L A F | 1 2 3 |
| gleicher_exponent | V020, V021, V022 | A V U | 2 2 3 |
| potenz_von_potenz | V023, V024, V025 | A B U | 2 2 3 |
| geteilt_gleiche_basis | V026, V027, V028 | L A F | 1 2 3 |
| anwenden | V029, V030, V031 | A V A | 2 3 3 |

### terme.umformen (Klasse 7)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| zusammenfassen | V032, V033, V034 | L A F | 1 2 3 |
| produkte | V035, V036, V037 | A U U | 2 2 3 |
| minusklammer | V038, V039, V040 | L A F | 1 2 3 |
| ausmultiplizieren | V041, V042, V043 | A Z U | 2 2 3 |
| aequivalenz | V044, V045, V046 | A U U | 2 3 3 |

### abbildungen.kongruenz (Klasse 7)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| achsenspiegelung | V047, V048, V049 | L A F | 1 2 3 |
| mittelsenkrechte | V050, V051 | A U | 2 3 |
| winkelhalbierende | V052, V053 | A V | 2 3 |
| symmetrie | V054, V055, V056 | L A F | 1 2 3 |
| vierecke_ordnen | V057, V058 | B A | 2 3 |
| eigenschaften | V059, V060 | A F | 2 3 |

### geometrie.winkelsaetze (Klasse 7)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| scheitel_neben | V061, V062 | L A | 1 2 |
| stufen_wechsel | V063, V064 | A F | 2 3 |
| parallel_pruefen | V065, V066 | A U | 2 3 |
| innenwinkelsumme | V067, V068 | A V | 2 3 |
| aussenwinkel | V069, V070 | L A | 1 2 |
| vieleck | V071, V072 | A U | 2 3 |
| parkett | V073, V074 | A V | 2 3 |
| figuren | V075, V076 | A A | 2 3 |
| beweisen | V077, V078 | B F | 2 3 |

### geometrie.konstruktion (Klasse 7)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| gleichschenklig | V079, V080, V081 | L A F | 1 2 3 |
| kongruenzsatz | V082, V083, V084 | A V F | 2 2 3 |
| konstruierbar | V085, V086, V087 | L A V | 1 2 3 |
| planfigur | V088, V089, V090 | A V U | 2 2 3 |
| satz_kehrsatz | V091, V092, V093 | A U A | 2 3 3 |

### gleichungen.linear (Klasse 7)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| waage | V094, V095, V096 | L A F | 1 2 3 |
| beide_seiten | V097, V098, V099 | A V U | 2 2 3 |
| klammern | V100, V101, V102 | L A F | 1 2 3 |
| probe | V103, V104 | A V | 3 3 |
| sonderfaelle | V105, V106, V107 | V U F | 2 3 3 |
| sach | V108, V109, V110 | A A U | 2 2 3 |

### zahlen.wurzeln_basis (Klasse 9)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| quadratwurzel | V111, V112, V113 | L A U | 1 2 2 |
| wurzel_dezimal | V114, V115 | A A | 2 2 |
| kubikwurzel | V116, V117, V118 | L A F | 1 2 3 |
| abschaetzen | V119, V120 | V A | 2 2 |
| wurzel_deuten | V121, V122, V123 | V A F | 3 3 3 |
| wurzel_sache | V124, V125 | A A | 2 2 |

### zahlen.reell (Klasse 9)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| zahlarten | V126, V127 | V A | 1 2 |
| eingrenzen | V128, V129 | L A | 1 2 |
| heron | V130, V131 | A U | 2 2 |
| wurzel_mal | V132, V133 | A V | 2 3 |
| teilweise | V134, V135 | L A | 1 2 |
| zusammenfassen | V136 | F | 3 |
| nenner_rational | V137 | A | 2 |
| irrational_beweis | V138, V139 | V F | 3 3 |

### gleichungen.quadratisch (Klasse 9)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| reinquadratisch | V140, V141 | L A | 1 2 |
| ausklammern | V142, V143 | V F | 2 3 |
| faktorisieren | V144, V145 | A U | 2 3 |
| ergaenzung | V146 | A | 2 |
| loesungsformel | V147, V148 | L A | 1 2 |
| bruchgleichung | V149 | A | 2 |
| diskriminante | V150, V151 | U V | 3 3 |
| sachaufgabe | V152, V153 | A A | 2 2 |

### funktionen.quadratisch (Klasse 9)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| scheitel | V154, V155 | L V | 1 2 |
| parameter | V156 | U | 3 |
| spiegeln | V157, V158 | A V | 2 3 |
| umformen | V159, V160 | A F | 2 3 |
| nullstellen | V161, V162 | L A | 1 2 |
| punkte | V163 | A | 2 |
| bestimmen | V164 | U | 3 |
| schnittpunkte | V165 | A | 2 |
| extremwert | V166, V167 | L A | 1 3 |

### trigo.pythagoras (Klasse 9)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| hypotenuse | V168, V169 | L A | 1 2 |
| kathete | V170, V171 | A V | 2 2 |
| umkehrung | V172, V173 | V U | 3 3 |
| koordinaten | V174, V175 | A U | 2 3 |
| raum | V176, V177 | L A | 1 2 |
| anwendung | V178, V179 | A F | 2 3 |

### trigo.rechtwinklig (Klasse 9)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| seiten | V180, V181 | V V | 1 2 |
| verhaeltnisse | V182, V183 | L A | 1 2 |
| seite | V184, V185 | A U | 2 3 |
| winkel | V186 | A | 2 |
| beziehungen | V187, V188 | A V | 2 3 |
| anwendung | V189, V190 | A F | 2 3 |
| schnittwinkel | V191, V192 | A A | 2 2 |

### stochastik.verknuepft (Klasse 9)

| Etappe | Kennungen | Formen | Stufen |
|---|---|---|---|
| elemente | V193 | A | 2 |
| schnitt | V194 | A | 3 |
| verknuepfen | V195 | A | 2 |
| additionssatz | V196, V197 | L A | 1 2 |
| venn | V198 | A | 2 |
| mengen_verstehen | V199 | V | 3 |
| vierfeld | V200, V201 | L A | 1 2 |
| tafel_wkeit | V202 | A | 2 |
| bedingt | V203, V204 | A A | 2 2 |
| rueckschluss | V205 | U | 3 |
| verstehen | V206, V207 | V F | 3 3 |

## Zweifelsfälle bei der Regel-Kennung

Aufgaben, bei denen die Wahl der Regel nicht eindeutig ist (Kennung, gewählte Regel, Begründung). Die Wahl folgt dem tragenden Lösungsschritt; wo der Katalog keine passende Regel hat, steht die Aufgabe unter „ohne Regel“.

| Aufgabe | Einheit.Lernkarte | gewählt | Bemerkung |
|---|---|---|---|
| R15-V007 | bruch.prozent_grundwert.zurueck | `rr.gegenrechnung` | Rückwärts durch den Faktor teilen: rr.gegenrechnung (Umkehr des Malnehmens); id.verhaeltnisse.prozent wäre ebenfalls vertretbar |
| R15-V008 | bruch.prozent_grundwert.zurueck | `rr.gegenrechnung` | Rückwärts durch den Faktor teilen: rr.gegenrechnung; id.verhaeltnisse.prozent wäre ebenfalls vertretbar |
| R15-V035 | terme.umformen.produkte | `rr.tauschen` | Produkte tauschen und zusammenfassen: rr.tauschen; die Lernkarte nennt rr.vorzeichen, hier kommen aber keine negativen Zahlen vor |
| R15-V037 | terme.umformen.produkte | `rr.tauschen` | Produkt vereinfachen (tauschen) und zurückrechnen; keine Regel des Katalogs für das Umkehren von a² in dieser Klassenstufe |
| R15-V052 | abbildungen.kongruenz.winkelhalbierende | `id.geometrie.winkel` | Winkelsumme im Dreieck trägt die Rechnung (id.geometrie.winkel, Ausnahme der Themenliste); die Lernkarte nennt id.geometrie.abstand |
| R15-V059 | abbildungen.kongruenz.eigenschaften | `id.geometrie.winkel` | Winkelsumme im Dreieck plus Erhaltung der Winkel; Ausnahme der Themenliste (id.geometrie.winkel), die Lernkarte nennt id.geometrie.deckungsgleich |
| R15-V121 | zahlen.wurzeln_basis.wurzel_deuten | `id.zahlen.hoch_zurueck` | Definitionsbereich der Wurzel: hoch_zurueck trägt (Quadrat nie negativ), die Lernkarte nennt sonst keine Regel |
| R15-V122 | zahlen.wurzeln_basis.wurzel_deuten | `id.zahlen.hoch_zurueck` | Definitionsmenge der Wurzel (Radikand ≥ 0); hoch_zurueck trägt nur teilweise |
| R15-V126 | zahlen.reell.zahlarten | `id.zahlen.hoch_zurueck` | Rationale und irrationale Zahlen unterscheiden: hoch_zurueck trägt das Zurückrechnen der Wurzel, die Zahlarten selbst hat keine eigene Regel |
| R15-V127 | zahlen.reell.zahlarten | `id.zahlen.hoch_zurueck` | Zahlen sortieren: hoch_zurueck trägt das Prüfen der Wurzeln |
| R15-V128 | zahlen.reell.eingrenzen | `id.zahlen.hoch_zurueck` | Eingrenzen durch Quadrieren: hoch_zurueck trägt das Rückrechnen |
| R15-V129 | zahlen.reell.eingrenzen | `id.zahlen.hoch_zurueck` | Eingrenzen durch Quadrieren: hoch_zurueck trägt das Rückrechnen |
| R15-V130 | zahlen.reell.heron | `id.zahlen.hoch_zurueck` | Heron-Verfahren (Mittelwert aus Näherung und Quotient): hoch_zurueck trägt nur die Probe |
| R15-V131 | zahlen.reell.heron | `id.zahlen.hoch_zurueck` | Heron-Verfahren als Rechteck: Flächenerhaltung, hoch_zurueck nur als Zielgröße |
| R15-V133 | zahlen.reell.wurzel_mal | `id.zahlen.hoch_zurueck` | Rechengesetze für Wurzeln: hoch_zurueck, aber kein eigener Eintrag für das Zusammenfassen unter einer Wurzel |
| R15-V145 | gleichungen.quadratisch.faktorisieren | `rr.nullprodukt` | Zurück von den Lösungen zur Gleichung: Nullprodukt trägt den Weg rückwärts |
| R15-V148 | gleichungen.quadratisch.loesungsformel | `rr.reihenfolge` | Lösungsformel: tragender Schritt ist die Diskriminante (Klammer, Hoch, Punkt vor Strich); es gibt keine eigene Formelregel im Katalog |
| R15-V149 | gleichungen.quadratisch.bruchgleichung | `rr.waage` | Bruchgleichung: Waage (mit x malnehmen), danach Nullprodukt |
| R15-V151 | gleichungen.quadratisch.diskriminante | `rr.reihenfolge` | Diskriminante bestimmen und deuten: tragend ist die Rechenreihenfolge; die Deutung (Vorzeichen) hat keine eigene Regel |
| R15-V152 | gleichungen.quadratisch.sachaufgabe | `rr.nullprodukt` | Sachaufgabe: Nullprodukt nach dem Umformen; Prüfen der Lösung gegen die Sachlage |
| R15-V153 | gleichungen.quadratisch.sachaufgabe | `rr.reihenfolge` | Sachaufgabe: Lösungsformel (Diskriminante nach Rechenreihenfolge), Prüfen gegen die Sachlage |
| R15-V161 | funktionen.quadratisch.nullstellen | `id.funktionen.zuordnung` | Nullstellen: y = 0 setzen (Zuordnung y zu x), das Lösen selbst gehört zu Nullprodukt, das für diese Einheit nicht im Katalog steht |
| R15-V162 | funktionen.quadratisch.nullstellen | `id.funktionen.zuordnung` | Nullstellen: y = 0 setzen; das Wurzelziehen mit zwei Lösungen hat im Katalog keine eigene Regel für diese Einheit |
| R15-V167 | funktionen.quadratisch.extremwert | `id.funktionen.gleichung_form` | Extremwert: Scheitel der Parabel gesucht; gleichung_form trägt das Lesen der Form, das Aufstellen der Zielfunktion hat keine Regel |
| R15-V182 | trigo.rechtwinklig.verhaeltnisse | `id.geometrie.rechtwinklig` | Sinus, Kosinus, Tangens: die einzige Regel der Einheit im Katalog (rechtwinkliges Dreieck, Lage der Seiten) trägt nur das Zuordnen der Seiten, das Rechnen mit dem Verhältnis nicht |
| R15-V183 | trigo.rechtwinklig.verhaeltnisse | `id.geometrie.rechtwinklig` | Sinus, Kosinus, Tangens: die einzige Regel der Einheit im Katalog (rechtwinkliges Dreieck, Lage der Seiten) trägt nur das Zuordnen der Seiten, das Rechnen mit dem Verhältnis nicht |
| R15-V184 | trigo.rechtwinklig.seite | `id.geometrie.rechtwinklig` | Sinus, Kosinus, Tangens: die einzige Regel der Einheit im Katalog (rechtwinkliges Dreieck, Lage der Seiten) trägt nur das Zuordnen der Seiten, das Rechnen mit dem Verhältnis nicht |
| R15-V185 | trigo.rechtwinklig.seite | `id.geometrie.rechtwinklig` | Sinus, Kosinus, Tangens: die einzige Regel der Einheit im Katalog (rechtwinkliges Dreieck, Lage der Seiten) trägt nur das Zuordnen der Seiten, das Rechnen mit dem Verhältnis nicht |
| R15-V186 | trigo.rechtwinklig.winkel | `id.geometrie.rechtwinklig` | Sinus, Kosinus, Tangens: die einzige Regel der Einheit im Katalog (rechtwinkliges Dreieck, Lage der Seiten) trägt nur das Zuordnen der Seiten, das Rechnen mit dem Verhältnis nicht |
| R15-V189 | trigo.rechtwinklig.anwendung | `id.geometrie.rechtwinklig` | Sinus, Kosinus, Tangens: die einzige Regel der Einheit im Katalog (rechtwinkliges Dreieck, Lage der Seiten) trägt nur das Zuordnen der Seiten, das Rechnen mit dem Verhältnis nicht |
| R15-V190 | trigo.rechtwinklig.anwendung | `id.geometrie.rechtwinklig` | Sinus, Kosinus, Tangens: die einzige Regel der Einheit im Katalog (rechtwinkliges Dreieck, Lage der Seiten) trägt nur das Zuordnen der Seiten, das Rechnen mit dem Verhältnis nicht |
| R15-V202 | stochastik.verknuepft.tafel_wkeit | `id.daten.anteil` | Vierfeldertafel mit Wahrscheinlichkeiten: id.daten.anteil trägt die Deutung als Anteil, das Ausfüllen der Tafel hat keine eigene Regel |
| R15-V203 | stochastik.verknuepft.bedingt | `id.daten.anteil` | Bedingte Wahrscheinlichkeit als Anteil: id.daten.anteil trägt Günstige durch Mögliche |
| R15-V206 | stochastik.verknuepft.verstehen | `id.daten.anteil` | Deutung der bedingten Wahrscheinlichkeit: id.daten.anteil (Anteil von was?) |

## Aufgaben bewusst ohne Regel

Keine Regel des Katalogs trägt den Lösungsweg; die Begründung steht je Aufgabe.

| Aufgabe | Einheit.Lernkarte | Begründung |
|---|---|---|
| R15-V085 | geometrie.konstruktion.konstruierbar | Dreiecksungleichung (zwei Seiten zusammen länger als die dritte): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V086 | geometrie.konstruktion.konstruierbar | Dreiecksungleichung (zwei Seiten zusammen länger als die dritte): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V087 | geometrie.konstruktion.konstruierbar | Dreiecksungleichung (zwei Seiten zusammen länger als die dritte): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V091 | geometrie.konstruktion.satz_kehrsatz | Satz und Kehrsatz (Logik, Gegenbeispiel): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V092 | geometrie.konstruktion.satz_kehrsatz | Satz und Kehrsatz (Logik, Gegenbeispiel): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V093 | geometrie.konstruktion.satz_kehrsatz | Satz und Kehrsatz (Logik, Gegenbeispiel): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V123 | zahlen.wurzeln_basis.wurzel_deuten | Wurzel und Summe (Wurzel verteilt sich nicht auf Summanden): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V136 | zahlen.reell.zusammenfassen | Wurzeln zusammenfassen und umschreiben (a√b): keine Regel des Katalogs trägt genau diesen Schritt |
| R15-V137 | zahlen.reell.nenner_rational | Nenner rational machen (Erweitern mit der Wurzel): keine Regel des Katalogs trägt genau diesen Schritt |
| R15-V138 | zahlen.reell.irrational_beweis | Beweis durch Widerspruch (gerade/ungerade, gekürzter Bruch): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V139 | zahlen.reell.irrational_beweis | Beweis durch Widerspruch (gerade/ungerade, gekürzter Bruch): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V146 | gleichungen.quadratisch.ergaenzung | Quadratische Ergänzung (binomische Formel rückwärts): keine Regel des Katalogs trägt genau diesen Schritt |
| R15-V150 | gleichungen.quadratisch.diskriminante | Diskriminante null (genau eine Lösung): keine Regel des Katalogs trägt genau diesen Schritt |
| R15-V164 | funktionen.quadratisch.bestimmen | Gleichungssystem bzw. Gleichsetzen zweier Funktionsterme: keine Regel des Katalogs trägt den Lösungsweg |
| R15-V165 | funktionen.quadratisch.schnittpunkte | Gleichungssystem bzw. Gleichsetzen zweier Funktionsterme: keine Regel des Katalogs trägt den Lösungsweg |
| R15-V187 | trigo.rechtwinklig.beziehungen | Beziehungen zwischen Sinus, Kosinus und Tangens: keine Regel des Katalogs trägt den Lösungsweg |
| R15-V188 | trigo.rechtwinklig.beziehungen | Beziehungen zwischen Sinus, Kosinus und Tangens: keine Regel des Katalogs trägt den Lösungsweg |
| R15-V191 | trigo.rechtwinklig.schnittwinkel | Steigung und Winkel einer Geraden (Tangens als Steigung): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V192 | trigo.rechtwinklig.schnittwinkel | Steigung und Winkel einer Geraden (Tangens als Steigung): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V193 | stochastik.verknuepft.elemente | Mengen und Mengenoperationen zählen (Elemente, Schnitt, Vereinigung): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V194 | stochastik.verknuepft.schnitt | Mengen und Mengenoperationen zählen (Elemente, Schnitt, Vereinigung): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V195 | stochastik.verknuepft.verknuepfen | Mengen und Mengenoperationen zählen (Elemente, Schnitt, Vereinigung): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V196 | stochastik.verknuepft.additionssatz | Additionssatz für zwei Ereignisse (Schnitt nicht doppelt zählen): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V197 | stochastik.verknuepft.additionssatz | Additionssatz für zwei Ereignisse (Schnitt nicht doppelt zählen): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V198 | stochastik.verknuepft.venn | Mengen und Mengenoperationen zählen (Elemente, Schnitt, Vereinigung): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V199 | stochastik.verknuepft.mengen_verstehen | Mengen und Mengenoperationen zählen (Elemente, Schnitt, Vereinigung): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V200 | stochastik.verknuepft.vierfeld | Vierfeldertafel ausfüllen (Zeilen- und Spaltensummen): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V201 | stochastik.verknuepft.vierfeld | Vierfeldertafel ausfüllen (Zeilen- und Spaltensummen): keine Regel des Katalogs trägt den Lösungsweg |
| R15-V207 | stochastik.verknuepft.verstehen | Unabhängigkeit und Unvereinbarkeit unterscheiden: keine Regel des Katalogs trägt den Lösungsweg |

## Ausnahmen von der Themenliste des Katalogs

- `abbildungen.kongruenz` mit `id.geometrie.winkel`: V052, V059
- `geometrie.konstruktion` mit `id.geometrie.winkel`: V079, V080, V081, V090

## Prüfungen (alle in `bauen.py`, Lauf endet mit `OK`)

- Jede Lösung zweifach nachgerechnet (Rechenanker und unabhängige Zweitrechnung); Zählaufgaben zusätzlich mit einer Zählschleife im Programm bestätigt (48 Aufgaben).
- Jedes Fehlbild ist eine nachgerechnete, typische Fehlrechnung (Rechnung steht im Quelltext) und nie gleich der richtigen Antwort; Fehlbild-Kennungen aus dem Katalog nur, wo der Katalogtext genau passt (47 Fehlbilder mit Kennung).
- Doppelungsprüfung gegen den gesamten Bestand und alle früheren Runden einschließlich R14; Negativproben der Selbstprüfung schlagen an. Viele Entwürfe mussten dafür geändert werden (andere Zahlen, andere Einkleidung).
- `tools/vorrat_pruefen.py` über `rollend-15`: 207 Aufgaben, 0 Meldungen in allen vier Gruppen. `tools/rollend_sql.py --runden 15` (nur Übersicht) liest die Runde ohne Eintrag in eine Rundenliste: 207 Aufgaben, 14 Einheiten.
- Fehler-Detektiv: Fehlerzeile je Zeile {1: 5, 2: 7, 3: 8, 4: 4} bei 24 Aufgaben (Grenze n/3 + 1 je Zeile eingehalten).
- Regel-Kennung: 178 Aufgaben mit, 29 ohne Regel.

## Worauf ein Vorprüfer achten sollte

1. **Regel-Zuordnung bei Sinus/Kosinus/Tangens** (`trigo.rechtwinklig`, 7 Aufgaben mit Zweifel): Die Lernkarten-Vorgabe nennt `id.geometrie.rechtwinklig`, die Regel trägt aber nur die Lage der Seiten. Das Rechnen mit dem Verhältnis hat keine Regel im Katalog. Wer das streng liest, nimmt die Kennung dort heraus.
2. **Zweifelsfälle** (Liste oben): besonders `rr.gegenrechnung` statt `id.verhaeltnisse.prozent` bei Rückwärtsrechnen von Prozent (R15-V007, V008), Nullstellen und Bruchgleichung (`id.funktionen.zuordnung`, `rr.waage`), Wurzeln (`id.zahlen.hoch_zurueck` bei Zahlarten, Eingrenzen, Heron).
3. **Aufgaben ohne Regel** (29): Begründung je Aufgabe oben. Prüfen, ob der Katalog nicht doch eine Regel für Satz/Kehrsatz, Dreiecksungleichung, Mengenaufgaben, Vierfeldertafel, Additionssatz, Wurzelvereinfachen und Diskriminante hat.
4. **Auswahl** (`auswahl.md`): Die Datei wurde nach dem Schreiben angelegt, nicht davor. Die Klasse-7-Wahl folgt dem Kriterium „in R8/9/10/14 nicht bedient“; reiner Anteil würde `daten.boxplot` und `geometrie.kreis` vor `bruch.prozent_grundwert`, `geometrie.winkelsaetze` und `gleichungen.linear` setzen.
5. **Lückenwege:** `bruch.prozent_grundwert` hat keinen Lückenweg (alle 16 zählen), `trigo.rechtwinklig` nur einen; sonst zwei bis drei je Einheit (26 insgesamt, 13 %).
6. **Eindeutigkeit und Zählaufgaben:** Aufgaben mit Zählen (die 48 Kennungen, die `bauen.py` als „mit unabhängiger Zählung bestätigt“ ausgibt, darunter die Mengenaufgaben in `stochastik.verknuepft`) von Hand gegenlesen; die Zahl ist im Programm bestätigt, die Formulierung (zum Beispiel „beide Grenzen eingeschlossen“) sollte ein Mensch lesen.
7. **Rundung:** Aufgaben mit Dezimalantwort haben `toleranz` nur, wo gerundet wird (Winkel, Wurzeln, Heron, Seilbahn, Leuchtturm, Rückschluss). Die Rundung steht jeweils im Fragetext.

