# Texte, achte Runde (Mathe-Profi, 27.11.2026, berichtigt nach Gegenprüfung Werkstatt 1078/1079 und 1090)

Prüfen: `python3 -I inhalte/mathe-profi/regeln-uebersicht/texte8/pruefen.py` (endet mit „OK“; 269 exakt gerechnete Prüfungen, Pflichtfelder, Längen, Kennungen, Aufgaben-Verweise, Abgleich der Quellen). **[G]** gesichert, **[A]** Annahme.

## Dateien (Kennungen wie `kennungen.json`)
| Datei | Inhalt |
|---|---|
| `kurzbeschreibungen.json` | 42 geprüft: 19 in Ordnung, **23 berichtigt** (Regeln 3, 5, 6, 7, 8, 9, 10, 11 und 15 Ideen). `endfassung` ist der einzige Text, den die App zeigt. |
| `merksaetze.json` | 14 gegengelesen, 25 Lücken in „Genau gesagt / Wann sie gilt / Fehler“ mit fertigem Text; Kurzfassung Regel 10. |
| `arbeitsweisen.json`, `einzelregeln.json` | 8 Arbeitsweisen; 30 Einzelregeln (je 15 für Klasse 5 und 8) mit Beispiel und Grenze. |
| `beispielaufgaben.json` | Aufgaben für Regel 9, 10, 11, 14; Stichprobe der Zuordnung; `umhaengen` (Korrektur der Zuordnung, vom Bau angewendet). |
| `lehrplan.json` | Redaktionelle Einordnung je Rechenregel (kein Nachweis gegen den Fachlehrplan). |
| `abgleich_inhalt.py`, `berichtigung_inhalt.py` | Gleichen `inhalt.json` (Entwurf) mit `klassenleiter.json` ab und berichtigen rund 100 Texte dort (1078, 1090 und eigener Durchgang); wiederholbar. |

## Merksätze (berichtigte Aussage)
- Von 14 Merksätzen der Regelseiten ist **keiner falsch**; **geändert ist nur Regel 10** (Liste und Seite): „Plus/Minus: erst gleiche Nenner. Mal: oben mal oben, unten mal unten. Geteilt: mal Kehrwert.“ (Entscheidung Projektleiter; „erst“ bleibt, sonst bliebe offen, dass man gleichnamig machen muss).
- Mehrere Merksätze sind **nur mit ihrer Grenze richtig**: R4 (Bruch-, Wurzel-, Betragsstriche, Potenzturm), R6 (Plus vor der Klammer, Produkt in der Klammer; Merksatz bleibt), R10 (gemischte Zahlen, welcher Bruch gekehrt wird), R11, R12 (Runden, Betrag), R13 (Quadrieren), R14 (nicht durch x teilen). Diese Grenzen stehen in den Feldern genau/voraus/fehler und damit im aufgeschlagenen Text der Regelseite (Test).
- R11: Der Bestandstext „gilt nur bei direkter Proportionalität“ ist ersetzt (auch umgekehrt proportional lässt sich „erst auf eins“ anwenden, mit umgekehrten Rechenarten).

## Entschieden / berichtigt gegenüber der Arbeitsliste [G]
- **Oberflächen-Beispiele bleiben bei 94 und 84 cm²** (nicht 188/96): 40, 30, 24 sind schon die Flächenpaare (2·20, 2·15, 2·12 am Quader 5 · 4 · 3 cm); beim Prisma (Dreieck 3 · 4 · 5, Höhe 6 cm) sind 12 beide Grundflächen (2 · 6) und 18, 24, 30 die Seiten. Neu: die Rechnung steht ausgeschrieben im Beispiel. Pyramide: 36 + 60 = 96.
- „Über Kreuz“ gehört primär zu Regel 13; BG-01, 02, 05, 09 sind dort eingeordnet, GF-10 bei Regel 12; Regel 9 und 11 bekommen Ersatzaufgaben.
- Lehrplan: überall als „Redaktionelle Einordnung, Fundstelle im Fachlehrplan nicht hinterlegt“ gekennzeichnet.

## Zweite Gegenprüfung (1090)
- Alle Punkte der Arbeitsliste sind in den Quellen und in den angezeigten Daten; geprüft in `tests/lernen-regeln.test.cjs` (Test „1090“) und in `pruefen.py` (gerechnete Aussagen, Pflichtstellen).
- **Kurzsätze haben eingeschränkte Gültigkeit:** Kurzbeschreibung und Merksatz sagen den Kern, die Grenze steht in genau/voraus/fehler (R6 „vor einer Summe“, R7 „Summand der äußeren Klammer“, R3 „ungleich null“, R8 „positive ganze Hochzahl“).
- Eigener Durchgang über alle Merksätze, Kurzbeschreibungen, Ideen-Texte und Einzelregeln: Allaussagen, fehlende Definitionsbereiche (≠ 0, reell, positiv) und überzogene Aussagen sind in `berichtigung_inhalt.py` gesammelt (zweiter und dritter Block).
- Ausschlüsse der Definitionsmenge stehen vor den Aufgaben BG-01, BG-02, BG-03, BG-13, PG-01 bis PG-03 und Stelle 93 (`umhaengen.text_voranstellen`, vom Bau angewendet; die Aufgaben-Dateien bleiben unverändert).
- `kennungen.json` (Merksatz/Genau der Ideen) ist nicht nachgeführt; angezeigt wird `inhalt.json`.

## Annahmen [A]
- Zeilenzahl der Regel-10-Fassung am Handy nicht gemessen.
- Dringlichkeit der 30 Einzelregeln ist meine Einschätzung.
- Kennungen `aw.*` für Arbeitsweisen sind nur Vorschläge; Aufgaben haben keine eigene Kennung (Benennung über Datei, Lernkarte, Stelle).

## Was der Designer-Entwurf übernehmen muss
1. `kurz.json`: alle 42 Texte durch `endfassung` ersetzen (21 weichen ab).
2. `inhalt.json`: Stand nach `abgleich_inhalt.py` und `berichtigung_inhalt.py` übernehmen (Leitern, `regeln[].klassen`, berichtigte Texte); Lücken aus `merksaetze.json` in genau/voraus/fehler; Merksatz Regel 10.
3. Arbeitsweisen, 30 Einzelregeln, Lehrer-Blatt (Lehrplan-Kennzeichnung, Aufgaben R9–R14) aus den Dateien hier.
4. `kennungen-zuordnung.json` (schritt1) ist unverändert; die Korrektur steht in `beispielaufgaben.json` unter `umhaengen`.

## Offene Fragen an den Projektleiter
- Zeilenzahl der Regel-10-Fassung am echten Handy prüfen.
- LehrplanPLUS an der Quelle: wer prüft? Bis dahin bleibt „nicht geprüft“.
- Kennungen für Aufgaben und Arbeitsweisen?
- Einzelregel V7 steht mit Klasse 5 (Satz begrenzt); D9 nennt jetzt Grundgesamtheit und Stichprobe.
