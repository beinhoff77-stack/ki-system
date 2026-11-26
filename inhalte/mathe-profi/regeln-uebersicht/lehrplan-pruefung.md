# Regel-Universum · Klassen am Lehrplan geprüft (Auftrag 15, Teil D)

Mathe-Profi, 27.11.2026. Erzeugt von `klassenleiter.py`.

## Womit geprüft wurde – und womit nicht

- **Im Repo liegen keine Lehrplan-Dateien.** Es gibt nur `inhalte/themenliste.json`: je Thema eine Klasse je Schulart und einige Stichworte aus dem Lehrplan. [G]
- Geprüft habe ich deshalb gegen die **Lehrplan-Kopie in der Datenbank der App** (nur gelesen; 434 Zeilen, abgelegt als `lehrplan-kopie-zuordnung.txt`). Sie sagt je Thema, Schulart, Gruppe und Jahr, ob der Lehrplan das Thema nennt und mit welcher Rolle: „neu“, „weitergeführt“ oder ohne Angabe. [G]
- **Nicht geprüft: LehrplanPLUS an der Quelle.** Ob die Kopie den Lehrplan richtig und vollständig wiedergibt, weiß ich nicht.
- **Die Prüfung reicht nur bis zum Thema, nicht bis zur Regel.** Der Lehrplan ordnet Themen Klassen zu, keine Rechenregeln. Ob etwa „Minus vor der Klammer“ in Klasse 5 Vorwissen oder schon Stoff ist, steht in der Kopie nicht; das bleibt meine Einschätzung.

## 1. Gymnasium: jedes Beispiel der Klassenleitern

Regel der Prüfung: Das Thema muss in der Lehrplan-Kopie in dieser Klasse stehen. Ist das Beispiel als „Einführung“ gesetzt, muss die Kopie das Thema dort als „neu“ führen.

**172 von 172 Beispielen bestehen. 0 Abweichungen:**

| Beispiel | von mir gesetzt | Befund | |
|---|---|---|---|
| – | – | – | – |

## 2. Themenliste gegen Lehrplan-Kopie: Klasse je Thema

Für die 60 Themen, die in den Klassenleitern vorkommen: Stimmt die Klasse der Themenliste mit dem frühesten „neu“ der Lehrplan-Kopie überein? Abweichungen:

| Thema | Schulart | Themenliste | Lehrplan-Kopie |
|---|---|---|---|
| `bruch.prozent_grundwert` | IB | 3 | in der Lehrplan-Kopie kein Eintrag |
| `bruch.rechnen` | IB | 2 | Lehrplan-Kopie: „neu“ in beide Jahr 1 |
| `daten.boxplot` | IB | 4 | Lehrplan-Kopie: „neu“ in beide Jahr 2 |
| `funktionen.exponential_log` | IB | 5 | Lehrplan-Kopie: „neu“ in extended Jahr 4, standard Jahr 4 |
| `funktionen.ganzrational` | IB | 5 | Lehrplan-Kopie: „neu“ in extended Jahr 4 |
| `funktionen.grundbegriffe` | IB | 3 | Lehrplan-Kopie: „neu“ in beide Jahr 1 |
| `funktionen.linear` | IB | 3 | Lehrplan-Kopie: „neu“ in beide Jahr 1 |
| `funktionen.trig` | IB | 5 | Lehrplan-Kopie: erster Eintrag Jahr 4, nirgends als „neu“ |
| `geometrie.konstruktion` | IB | 3 | Lehrplan-Kopie: „neu“ in beide Jahr 1 |
| `geometrie.winkelsaetze` | IB | 2 | Lehrplan-Kopie: „neu“ in beide Jahr 1 |
| `gleichungen.bruch` | IB | 4 | in der Lehrplan-Kopie kein Eintrag |
| `gleichungen.exponential` | IB | 5 | in der Lehrplan-Kopie kein Eintrag |
| `gleichungen.formeln` | IB | 4 | in der Lehrplan-Kopie kein Eintrag |
| `gleichungen.lgs2` | IB | 4 | Lehrplan-Kopie: „neu“ in beide Jahr 3 |
| `gleichungen.ungleichungen` | IB | 4 | Lehrplan-Kopie: „neu“ in beide Jahr 2 |
| `groessen.proportional` | Realschule | 6 | Lehrplan-Kopie: „neu“ in allen Jahr 5 |
| `messen.flaechen_vielecke` | IB | – | Lehrplan-Kopie: ab Jahr 2 |
| `messen.kreisberechnung` | IB | 3 | Lehrplan-Kopie: „neu“ in beide Jahr 2 |
| `messen.prisma_zylinder` | IB | – | Lehrplan-Kopie: ab Jahr 1 |
| `messen.volumen` | IB | – | Lehrplan-Kopie: ab Jahr 1 |
| `stochastik.grundbegriffe` | Realschule | 9 | Lehrplan-Kopie: „neu“ in Gruppe I Jahr 8, Gruppe II_III Jahr 8 |
| `stochastik.mehrstufig` | IB | 4 | Lehrplan-Kopie: erster Eintrag Jahr 1, nirgends als „neu“ |
| `stochastik.verknuepft` | Realschule | 9 | Lehrplan-Kopie: erster Eintrag Jahr 8, nirgends als „neu“ |
| `stochastik.verknuepft` | IB | 4 | Lehrplan-Kopie: „neu“ in beide Jahr 1 |
| `terme.bruchterme` | IB | 4 | in der Lehrplan-Kopie kein Eintrag |
| `terme.potenzgesetze_ganzzahlig` | IB | 4 | in der Lehrplan-Kopie kein Eintrag |
| `terme.potenzgesetze_natuerlich` | IB | 3 | in der Lehrplan-Kopie kein Eintrag |
| `terme.umformen` | IB | 3 | Lehrplan-Kopie: „neu“ in beide Jahr 1 |
| `trigo.rechtwinklig` | IB | 4 | Lehrplan-Kopie: „neu“ in beide Jahr 3 |
| `zahlen.intervalle` | IB | 4 | in der Lehrplan-Kopie kein Eintrag |
| `zahlen.potenzen_zehner` | IB | 4 | Lehrplan-Kopie: „neu“ in beide Jahr 3 |
| `zahlen.rationale_exponenten` | IB | 5 | in der Lehrplan-Kopie kein Eintrag |
| `zahlen.reell` | IB | 4 | Lehrplan-Kopie: „neu“ in beide Jahr 3 |

Zu lesen mit Vorsicht: Beim IB zählt die Kopie Jahre (MYP 1 bis 5), nicht Klassen, und das IB schreibt keine verbindliche Jahresfolge vor. „Nirgends als neu“ kann auch heißen, dass die Rolle in der Kopie nicht gepflegt ist.

## 3. Einführung je Regel und Idee: Gymnasium, Realschule, IB

Erste als „Einführung“ gesetzte Stufe der Klassenleiter; dazu, in welchem Jahr die Lehrplan-Kopie dasselbe Thema an Realschule (Gruppe I, Gruppe II/III) und IB als „neu“ führt.

| Regel oder Idee | Gym. | Thema | RS I | RS II/III | IB (Jahr) | Bemerkung |
|---|---|---|---|---|---|---|
| Stellenwert | 5 | `zahlen.natuerlich` | 5 | 5 | 1 |  |
| Plus und Minus mit negativen Zahlen | 5 | `zahlen.ganz` | 5 | 5 | 2 |  |
| Vorzeichen bei Mal und Geteilt | 5 | `zahlen.rechengesetze` | 5 | 5 | 1 |  |
| Reihenfolge beim Rechnen | 5 | `zahlen.rechengesetze` | 5 | 5 | 1 |  |
| Tauschen, Klammern, Zusammenfassen | 5 | `zahlen.ganz` | 5 | 5 | 2 |  |
| Ausmultiplizieren und Ausklammern | 5 | `zahlen.rechengesetze` | 5 | 5 | 1 |  |
| Minus vor der Klammer | 7 | `terme.umformen` | 7 | – | 1 | Gruppen I und II/III verschieden |
| Potenzen | 5 | `zahlen.potenzen_basis` | 5 | 5 | 1 |  |
| Erweitern und Kürzen | 6 | `bruch.brueche` | 6 | 6 | 1 |  |
| Rechnen mit Brüchen | 6 | `bruch.rechnen` | 6 | 6 | 1 |  |
| Verhältnis (Dreisatz) | 5 | `groessen.proportional` | 5 | 5 | 2 |  |
| Gegenrechnung | 5 | `gleichungen.einfach` | 6 | 6 | 1 | Realschule in anderer Klasse als Gymnasium |
| Gleichung als Waage | 7 | `gleichungen.linear` | 7 | 7 | 2 |  |
| Nullprodukt | 9 | `gleichungen.quadratisch` | 9 | – | – | Gruppen I und II/III verschieden; IB: nicht als „neu“ genannt |
| Zahlengerade | 5 | `zahlen.ganz` | 5 | 5 | 2 |  |
| Bündeln in Zehnern | 5 | `zahlen.natuerlich` | 5 | 5 | 1 |  |
| Bausteine | 5 | `zahlen.teilbarkeit` | 5 | 5 | 1 |  |
| Schreibweisen | 6 | `bruch.prozent` | 6 | 6 | 1 |  |
| Hoch und zurück | 5 | `zahlen.potenzen_basis` | 5 | 5 | 1 |  |
| Term | 7 | `terme.aufstellen` | 6 | 6 | 1 | Realschule in anderer Klasse als Gymnasium |
| Erlaubte Zahlen | 8 | `terme.bruchterme` | 8 | 8 | – | IB: Thema fehlt |
| Gleichung lösen | 5 | `gleichungen.einfach` | 6 | 6 | 1 | Realschule in anderer Klasse als Gymnasium |
| Höherer Grad | 9 | `gleichungen.quadratisch` | 9 | – | – | Gruppen I und II/III verschieden; IB: nicht als „neu“ genannt |
| Größe | 5 | `groessen.einheiten` | 5 | 5 | 2 |  |
| Wert für eins | 5 | `groessen.proportional` | 5 | 5 | 2 |  |
| Prozent als Faktor | 6 | `bruch.prozent` | 6 | 6 | 1 |  |
| Winkel an Geraden | 5 | `geometrie.grundbegriffe` | 5 | 5 | 1 |  |
| Gleicher Abstand | 5 | `geometrie.ortslinien` | 7 | – | – | Gruppen I und II/III verschieden; Realschule in anderer Klasse als Gymnasium; IB: Thema fehlt |
| Deckungsgleich | 7 | `abbildungen.kongruenz` | 6 | 6 | 3 | Realschule in anderer Klasse als Gymnasium |
| Ähnlich | 9 | `abbildungen.aehnlichkeit` | 9 | – | 3 | Gruppen I und II/III verschieden |
| Rechtwinkliges Dreieck | 9 | `trigo.pythagoras` | 9 | 9 | 3 |  |
| Auslegen und zählen | 5 | `messen.flaechen` | 5 | 5 | 1 |  |
| Aus dem Rechteck | 5 | `messen.flaechen` | 5 | 5 | 1 |  |
| Aus dem Quader | 6 | `messen.volumen` | 6 | 6 | – | IB: nicht als „neu“ genannt |
| Haut des Körpers | 5 | `messen.koerper_berechnung` | 6 | 6 | 1 | Realschule in anderer Klasse als Gymnasium |
| Zuordnung | 8 | `funktionen.grundbegriffe` | 8 | 8 | 1 |  |
| Wachstum | 8 | `funktionen.linear` | 8 | – | 1 | Gruppen I und II/III verschieden |
| Gleichung und Form | 8 | `funktionen.linear` | 8 | – | 1 | Gruppen I und II/III verschieden |
| Kennzahl | 6 | `daten.kennwerte` | 7 | 7 | 2 | Realschule in anderer Klasse als Gymnasium |
| Vom Teil aufs Ganze | 8 | `stochastik.grundbegriffe` | 8 | 8 | 2 |  |
| Anteil | 8 | `stochastik.grundbegriffe` | 8 | 8 | 2 |  |
| Stufen | 10 | `stochastik.mehrstufig` | 10 | – | – | Gruppen I und II/III verschieden; IB: nicht als „neu“ genannt |

## Was sich so nicht prüfen lässt

1. **Vorwissen / Einführung / Anwendung auf der Ebene der Regel.** Prüfbar ist nur, ob das *Thema* in der Klasse steht und neu ist.
2. **„Kommt nicht vor“.** Die Kopie kann zeigen, dass ein Thema fehlt – nicht, dass eine Regel in einer Klasse nirgends gebraucht wird.
3. **Realschule Gruppe II/III:** Die Kopie enthält dort an vielen Stellen nur Überschriften; ein fehlendes „neu“ ist kein Beleg.
4. **IB:** Jahre statt Klassen, keine verbindliche Folge.
5. **Die Kopie selbst** gegen LehrplanPLUS.
