# Runde 15: Regel-Kennung je Aufgabe (Selbstkontrolle der Zuordnung)

Maßstab: die Regel, die das Kind zum Lösen braucht (tragender Lösungsschritt), nicht das Thema. Jede Kennung wurde gegen `inhalte/mathe-profi/regeln-uebersicht/kennungen.json` gelesen; `bauen.py` prüft, dass sie im Katalog steht und das Thema in der Themenliste der Regel steht (Ausnahmen unten). Quelle der Daten: die Angaben `regel` / `ohne` / `zweifel` in `th_*.py`; `regeln.py` und diese Tabelle werden von `bauen.py` erzeugt.

**152 Aufgaben mit Regel, 15 ohne.**

## Verteilung

| Regel | Name | Aufgaben |
|---|---|---|
| `id.geometrie.winkel` | Winkel an Geraden | 24 |
| `id.zahlen.hoch_zurueck` | Hoch und zurück | 24 |
| `rr.waage` | Gleichung als Waage | 18 |
| `rr.potenz` | Potenzen | 15 |
| `id.geometrie.deckungsgleich` | Deckungsgleich | 14 |
| `id.verhaeltnisse.prozent` | Prozent als Faktor | 14 |
| `id.funktionen.gleichung_form` | Gleichung und Form | 9 |
| `rr.tauschen` | Tauschen, Klammern, Zusammenfassen | 5 |
| `rr.ausmultiplizieren` | Ausmultiplizieren und Ausklammern | 4 |
| `rr.gegenrechnung` | Gegenrechnung | 4 |
| `rr.reihenfolge` | Reihenfolge beim Rechnen | 4 |
| `id.funktionen.zuordnung` | Zuordnung | 3 |
| `id.geometrie.abstand` | Gleicher Abstand | 3 |
| `rr.minusklammer` | Minus vor der Klammer | 3 |
| `rr.nullprodukt` | Nullprodukt | 3 |
| `id.algebra.hoeherer_grad` | Höherer Grad | 2 |
| `id.algebra.term` | Term | 2 |
| `rr.vorzeichen` | Vorzeichen bei Mal und Geteilt | 1 |
| – (ohne Regel) |  | 15 |

## Ausnahmen von der Themenliste des Katalogs (von Hand gelesen)

- `abbildungen.kongruenz` mit `id.geometrie.winkel`: V052, V059
- `geometrie.konstruktion` mit `id.geometrie.winkel`: V079, V080, V081, V090

## Aufgaben ohne Regel (mit Begründung)

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

## Zweifelsfälle

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

## Alle Aufgaben

| Aufgabe | Einheit.Lernkarte | Regel |
|---|---|---|
| R15-V001 | bruch.prozent_grundwert.faktor | `id.verhaeltnisse.prozent` |
| R15-V002 | bruch.prozent_grundwert.faktor | `id.verhaeltnisse.prozent` |
| R15-V003 | bruch.prozent_grundwert.vermehrt | `id.verhaeltnisse.prozent` |
| R15-V004 | bruch.prozent_grundwert.vermehrt | `id.verhaeltnisse.prozent` |
| R15-V005 | bruch.prozent_grundwert.vermindert | `id.verhaeltnisse.prozent` |
| R15-V006 | bruch.prozent_grundwert.vermindert | `id.verhaeltnisse.prozent` |
| R15-V007 | bruch.prozent_grundwert.zurueck | `rr.gegenrechnung` |
| R15-V008 | bruch.prozent_grundwert.zurueck | `rr.gegenrechnung` |
| R15-V009 | bruch.prozent_grundwert.prozentsatz | `id.verhaeltnisse.prozent` |
| R15-V010 | bruch.prozent_grundwert.prozentsatz | `id.verhaeltnisse.prozent` |
| R15-V011 | bruch.prozent_grundwert.mehrfach | `id.verhaeltnisse.prozent` |
| R15-V012 | bruch.prozent_grundwert.mehrfach | `id.verhaeltnisse.prozent` |
| R15-V013 | bruch.prozent_grundwert.formel | `id.verhaeltnisse.prozent` |
| R15-V014 | bruch.prozent_grundwert.formel | `id.verhaeltnisse.prozent` |
| R15-V015 | bruch.prozent_grundwert.argumente | `id.verhaeltnisse.prozent` |
| R15-V016 | bruch.prozent_grundwert.argumente | `id.verhaeltnisse.prozent` |
| R15-V017 | terme.potenzgesetze_natuerlich.mal_gleiche_basis | `rr.potenz` |
| R15-V018 | terme.potenzgesetze_natuerlich.mal_gleiche_basis | `rr.potenz` |
| R15-V019 | terme.potenzgesetze_natuerlich.mal_gleiche_basis | `rr.potenz` |
| R15-V020 | terme.potenzgesetze_natuerlich.gleicher_exponent | `rr.potenz` |
| R15-V021 | terme.potenzgesetze_natuerlich.gleicher_exponent | `rr.potenz` |
| R15-V022 | terme.potenzgesetze_natuerlich.gleicher_exponent | `rr.potenz` |
| R15-V023 | terme.potenzgesetze_natuerlich.potenz_von_potenz | `rr.potenz` |
| R15-V024 | terme.potenzgesetze_natuerlich.potenz_von_potenz | `rr.potenz` |
| R15-V025 | terme.potenzgesetze_natuerlich.potenz_von_potenz | `rr.potenz` |
| R15-V026 | terme.potenzgesetze_natuerlich.geteilt_gleiche_basis | `rr.potenz` |
| R15-V027 | terme.potenzgesetze_natuerlich.geteilt_gleiche_basis | `rr.potenz` |
| R15-V028 | terme.potenzgesetze_natuerlich.geteilt_gleiche_basis | `rr.potenz` |
| R15-V029 | terme.potenzgesetze_natuerlich.anwenden | `rr.potenz` |
| R15-V030 | terme.potenzgesetze_natuerlich.anwenden | `rr.potenz` |
| R15-V031 | terme.potenzgesetze_natuerlich.anwenden | `rr.potenz` |
| R15-V032 | terme.umformen.zusammenfassen | `rr.tauschen` |
| R15-V033 | terme.umformen.zusammenfassen | `rr.tauschen` |
| R15-V034 | terme.umformen.zusammenfassen | `rr.tauschen` |
| R15-V035 | terme.umformen.produkte | `rr.tauschen` |
| R15-V036 | terme.umformen.produkte | `rr.vorzeichen` |
| R15-V037 | terme.umformen.produkte | `rr.tauschen` |
| R15-V038 | terme.umformen.minusklammer | `rr.minusklammer` |
| R15-V039 | terme.umformen.minusklammer | `rr.minusklammer` |
| R15-V040 | terme.umformen.minusklammer | `rr.minusklammer` |
| R15-V041 | terme.umformen.ausmultiplizieren | `rr.ausmultiplizieren` |
| R15-V042 | terme.umformen.ausmultiplizieren | `rr.ausmultiplizieren` |
| R15-V043 | terme.umformen.ausmultiplizieren | `rr.ausmultiplizieren` |
| R15-V044 | terme.umformen.aequivalenz | `id.algebra.term` |
| R15-V045 | terme.umformen.aequivalenz | `id.algebra.term` |
| R15-V046 | terme.umformen.aequivalenz | `rr.ausmultiplizieren` |
| R15-V047 | abbildungen.kongruenz.achsenspiegelung | `id.geometrie.deckungsgleich` |
| R15-V048 | abbildungen.kongruenz.achsenspiegelung | `id.geometrie.deckungsgleich` |
| R15-V049 | abbildungen.kongruenz.achsenspiegelung | `id.geometrie.deckungsgleich` |
| R15-V050 | abbildungen.kongruenz.mittelsenkrechte | `id.geometrie.abstand` |
| R15-V051 | abbildungen.kongruenz.mittelsenkrechte | `id.geometrie.abstand` |
| R15-V052 | abbildungen.kongruenz.winkelhalbierende | `id.geometrie.winkel` |
| R15-V053 | abbildungen.kongruenz.winkelhalbierende | `id.geometrie.abstand` |
| R15-V054 | abbildungen.kongruenz.symmetrie | `id.geometrie.deckungsgleich` |
| R15-V055 | abbildungen.kongruenz.symmetrie | `id.geometrie.deckungsgleich` |
| R15-V056 | abbildungen.kongruenz.symmetrie | `id.geometrie.deckungsgleich` |
| R15-V057 | abbildungen.kongruenz.vierecke_ordnen | `id.geometrie.deckungsgleich` |
| R15-V058 | abbildungen.kongruenz.vierecke_ordnen | `id.geometrie.deckungsgleich` |
| R15-V059 | abbildungen.kongruenz.eigenschaften | `id.geometrie.winkel` |
| R15-V060 | abbildungen.kongruenz.eigenschaften | `id.geometrie.deckungsgleich` |
| R15-V061 | geometrie.winkelsaetze.scheitel_neben | `id.geometrie.winkel` |
| R15-V062 | geometrie.winkelsaetze.scheitel_neben | `id.geometrie.winkel` |
| R15-V063 | geometrie.winkelsaetze.stufen_wechsel | `id.geometrie.winkel` |
| R15-V064 | geometrie.winkelsaetze.stufen_wechsel | `id.geometrie.winkel` |
| R15-V065 | geometrie.winkelsaetze.parallel_pruefen | `id.geometrie.winkel` |
| R15-V066 | geometrie.winkelsaetze.parallel_pruefen | `id.geometrie.winkel` |
| R15-V067 | geometrie.winkelsaetze.innenwinkelsumme | `id.geometrie.winkel` |
| R15-V068 | geometrie.winkelsaetze.innenwinkelsumme | `id.geometrie.winkel` |
| R15-V069 | geometrie.winkelsaetze.aussenwinkel | `id.geometrie.winkel` |
| R15-V070 | geometrie.winkelsaetze.aussenwinkel | `id.geometrie.winkel` |
| R15-V071 | geometrie.winkelsaetze.vieleck | `id.geometrie.winkel` |
| R15-V072 | geometrie.winkelsaetze.vieleck | `id.geometrie.winkel` |
| R15-V073 | geometrie.winkelsaetze.parkett | `id.geometrie.winkel` |
| R15-V074 | geometrie.winkelsaetze.parkett | `id.geometrie.winkel` |
| R15-V075 | geometrie.winkelsaetze.figuren | `id.geometrie.winkel` |
| R15-V076 | geometrie.winkelsaetze.figuren | `id.geometrie.winkel` |
| R15-V077 | geometrie.winkelsaetze.beweisen | `id.geometrie.winkel` |
| R15-V078 | geometrie.winkelsaetze.beweisen | `id.geometrie.winkel` |
| R15-V079 | geometrie.konstruktion.gleichschenklig | `id.geometrie.winkel` |
| R15-V080 | geometrie.konstruktion.gleichschenklig | `id.geometrie.winkel` |
| R15-V081 | geometrie.konstruktion.gleichschenklig | `id.geometrie.winkel` |
| R15-V082 | geometrie.konstruktion.kongruenzsatz | `id.geometrie.deckungsgleich` |
| R15-V083 | geometrie.konstruktion.kongruenzsatz | `id.geometrie.deckungsgleich` |
| R15-V084 | geometrie.konstruktion.kongruenzsatz | `id.geometrie.deckungsgleich` |
| R15-V085 | geometrie.konstruktion.konstruierbar | – |
| R15-V086 | geometrie.konstruktion.konstruierbar | – |
| R15-V087 | geometrie.konstruktion.konstruierbar | – |
| R15-V088 | geometrie.konstruktion.planfigur | `id.geometrie.deckungsgleich` |
| R15-V089 | geometrie.konstruktion.planfigur | `id.geometrie.deckungsgleich` |
| R15-V090 | geometrie.konstruktion.planfigur | `id.geometrie.winkel` |
| R15-V091 | geometrie.konstruktion.satz_kehrsatz | – |
| R15-V092 | geometrie.konstruktion.satz_kehrsatz | – |
| R15-V093 | geometrie.konstruktion.satz_kehrsatz | – |
| R15-V094 | gleichungen.linear.waage | `rr.waage` |
| R15-V095 | gleichungen.linear.waage | `rr.waage` |
| R15-V096 | gleichungen.linear.waage | `rr.waage` |
| R15-V097 | gleichungen.linear.beide_seiten | `rr.waage` |
| R15-V098 | gleichungen.linear.beide_seiten | `rr.waage` |
| R15-V099 | gleichungen.linear.beide_seiten | `rr.waage` |
| R15-V100 | gleichungen.linear.klammern | `rr.waage` |
| R15-V101 | gleichungen.linear.klammern | `rr.waage` |
| R15-V102 | gleichungen.linear.klammern | `rr.waage` |
| R15-V103 | gleichungen.linear.probe | `rr.waage` |
| R15-V104 | gleichungen.linear.probe | `rr.waage` |
| R15-V105 | gleichungen.linear.sonderfaelle | `rr.waage` |
| R15-V106 | gleichungen.linear.sonderfaelle | `rr.waage` |
| R15-V107 | gleichungen.linear.sonderfaelle | `rr.waage` |
| R15-V108 | gleichungen.linear.sach | `rr.waage` |
| R15-V109 | gleichungen.linear.sach | `rr.waage` |
| R15-V110 | gleichungen.linear.sach | `rr.waage` |
| R15-V111 | zahlen.wurzeln_basis.quadratwurzel | `id.zahlen.hoch_zurueck` |
| R15-V112 | zahlen.wurzeln_basis.quadratwurzel | `id.zahlen.hoch_zurueck` |
| R15-V113 | zahlen.wurzeln_basis.quadratwurzel | `id.zahlen.hoch_zurueck` |
| R15-V114 | zahlen.wurzeln_basis.wurzel_dezimal | `id.zahlen.hoch_zurueck` |
| R15-V115 | zahlen.wurzeln_basis.wurzel_dezimal | `id.zahlen.hoch_zurueck` |
| R15-V116 | zahlen.wurzeln_basis.kubikwurzel | `id.zahlen.hoch_zurueck` |
| R15-V117 | zahlen.wurzeln_basis.kubikwurzel | `id.zahlen.hoch_zurueck` |
| R15-V118 | zahlen.wurzeln_basis.kubikwurzel | `id.zahlen.hoch_zurueck` |
| R15-V119 | zahlen.wurzeln_basis.abschaetzen | `id.zahlen.hoch_zurueck` |
| R15-V120 | zahlen.wurzeln_basis.abschaetzen | `id.zahlen.hoch_zurueck` |
| R15-V121 | zahlen.wurzeln_basis.wurzel_deuten | `id.zahlen.hoch_zurueck` |
| R15-V122 | zahlen.wurzeln_basis.wurzel_deuten | `id.zahlen.hoch_zurueck` |
| R15-V123 | zahlen.wurzeln_basis.wurzel_deuten | – |
| R15-V124 | zahlen.wurzeln_basis.wurzel_sache | `id.zahlen.hoch_zurueck` |
| R15-V125 | zahlen.wurzeln_basis.wurzel_sache | `id.zahlen.hoch_zurueck` |
| R15-V126 | zahlen.reell.zahlarten | `id.zahlen.hoch_zurueck` |
| R15-V127 | zahlen.reell.zahlarten | `id.zahlen.hoch_zurueck` |
| R15-V128 | zahlen.reell.eingrenzen | `id.zahlen.hoch_zurueck` |
| R15-V129 | zahlen.reell.eingrenzen | `id.zahlen.hoch_zurueck` |
| R15-V130 | zahlen.reell.heron | `id.zahlen.hoch_zurueck` |
| R15-V131 | zahlen.reell.heron | `id.zahlen.hoch_zurueck` |
| R15-V132 | zahlen.reell.wurzel_mal | `id.zahlen.hoch_zurueck` |
| R15-V133 | zahlen.reell.wurzel_mal | `id.zahlen.hoch_zurueck` |
| R15-V134 | zahlen.reell.teilweise | `id.zahlen.hoch_zurueck` |
| R15-V135 | zahlen.reell.teilweise | `id.zahlen.hoch_zurueck` |
| R15-V136 | zahlen.reell.zusammenfassen | – |
| R15-V137 | zahlen.reell.nenner_rational | – |
| R15-V138 | zahlen.reell.irrational_beweis | – |
| R15-V139 | zahlen.reell.irrational_beweis | – |
| R15-V140 | gleichungen.quadratisch.reinquadratisch | `rr.gegenrechnung` |
| R15-V141 | gleichungen.quadratisch.reinquadratisch | `rr.gegenrechnung` |
| R15-V142 | gleichungen.quadratisch.ausklammern | `id.algebra.hoeherer_grad` |
| R15-V143 | gleichungen.quadratisch.ausklammern | `id.algebra.hoeherer_grad` |
| R15-V144 | gleichungen.quadratisch.faktorisieren | `rr.nullprodukt` |
| R15-V145 | gleichungen.quadratisch.faktorisieren | `rr.nullprodukt` |
| R15-V146 | gleichungen.quadratisch.ergaenzung | – |
| R15-V147 | gleichungen.quadratisch.loesungsformel | `rr.reihenfolge` |
| R15-V148 | gleichungen.quadratisch.loesungsformel | `rr.reihenfolge` |
| R15-V149 | gleichungen.quadratisch.bruchgleichung | `rr.waage` |
| R15-V150 | gleichungen.quadratisch.diskriminante | – |
| R15-V151 | gleichungen.quadratisch.diskriminante | `rr.reihenfolge` |
| R15-V152 | gleichungen.quadratisch.sachaufgabe | `rr.nullprodukt` |
| R15-V153 | gleichungen.quadratisch.sachaufgabe | `rr.reihenfolge` |
| R15-V154 | funktionen.quadratisch.scheitel | `id.funktionen.gleichung_form` |
| R15-V155 | funktionen.quadratisch.scheitel | `id.funktionen.gleichung_form` |
| R15-V156 | funktionen.quadratisch.parameter | `id.funktionen.gleichung_form` |
| R15-V157 | funktionen.quadratisch.spiegeln | `id.funktionen.gleichung_form` |
| R15-V158 | funktionen.quadratisch.spiegeln | `id.funktionen.gleichung_form` |
| R15-V159 | funktionen.quadratisch.umformen | `id.funktionen.gleichung_form` |
| R15-V160 | funktionen.quadratisch.umformen | `id.funktionen.gleichung_form` |
| R15-V161 | funktionen.quadratisch.nullstellen | `id.funktionen.zuordnung` |
| R15-V162 | funktionen.quadratisch.nullstellen | `id.funktionen.zuordnung` |
| R15-V163 | funktionen.quadratisch.punkte | `id.funktionen.zuordnung` |
| R15-V164 | funktionen.quadratisch.bestimmen | – |
| R15-V165 | funktionen.quadratisch.schnittpunkte | – |
| R15-V166 | funktionen.quadratisch.extremwert | `id.funktionen.gleichung_form` |
| R15-V167 | funktionen.quadratisch.extremwert | `id.funktionen.gleichung_form` |
