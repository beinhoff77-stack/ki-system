# Vergleich der drei Gestaltungsrichtungen und Empfehlung

Alle drei Entwürfe sind einzelne Dateien und öffnen sich per Doppelklick (`<richtung>/entwurf.html`). Man kann sie wirklich durchspielen:
- Heute → Thema → Erklärung Schritt für Schritt → Aufgabe falsch, dann zweimal richtig → „Lernkarte sitzt“
- Zahlenstrahl ziehen
- Weltkarte, Reisepass, Eltern-Übersicht

Geprüft mit `werkzeug/durchspiel.test.cjs` (6 Durchläufe, Handy und Rechner, alle bestanden). Kontraste und Größen wurden in allen 135 Bildern mit `werkzeug/bilder.cjs` gemessen: kein Text unter 16 px, kein Paar unter 4,5:1, keine Tippfläche unter 44 px, kein waagrechtes Scrollen.

Überblick auf einen Blick: `vergleich-handy.png` (Heute · Üben · falsch · sitzt, je Richtung eine Reihe).

| | **heft** – Das Reiseheft | **abflug** – Abflugtafel & Bordkarte | **linien** – Das Liniennetz |
|---|---|---|---|
| Leitidee | Kariertes Mathe-Reiseheft: blättern, in Kästchen rechnen, Stempel und Klebezettel. | Jede Aufgabe ist eine Bordkarte, groß und allein auf dem Bildschirm; die Abflugtafel zeigt, wohin es geht. | Gebiete sind farbige Linien, Lernkarten Haltestellen. Man sieht immer, wo man steht. |
| Gefühl | warm, greifbar, persönlich | mutig, schnell, „erwachsen“ | klar, ordentlich, systematisch |
| Für wen | stärker für die 10-Jährige; der 13-Jährige bekommt „Skizzenbuch“ (Punktraster, keine Handschrift) | stärker für den 13-Jährigen (Nacht); die 10-Jährige: Tag-Ansicht, weniger Zeilen, Spaltenköpfe | beide gleich; Unterschied über Eingabe (Stellen-Schloss / Zahlenzeile) und Netzumfang |
| Startbildschirm | Heftseite: Ortsname, 3 Lernkarten-Zettel, leeres Stempelfeld, ein Knopf | Abflugtafel, gelber Knopf „Einsteigen ROM“ im Daumenbereich | Haltestellenschild, Linienband bis zum Stempel, ein Knopf |
| Erklärung | Bild für Bild, ein Satz je Bild | Sicherheitskarte: 4 Bildfelder, eins nach dem anderen aufdecken | Halt für Halt auf einer senkrechten Linie |
| Eingabe | eigene Tasten, Ziffern laufen in Stellenwert-Kästchen | eigenes Tastenfeld unten, Ziffern in Klapp-Kacheln | **Stellen-Schloss:** Spalte antippen, Ziffer wählen (5./6. Kl.) |
| Richtig / falsch | Stempel „stimmt!“ / Klebezettel „Fast!“ mit Diagnose | Abriss „AN BORD“ / „Kurskorrektur“: deine Zahl und Ziel untereinander, Abweichung gelb | Haken / „Andere Richtung: 2 bei H → 2 bei T“ |
| Navigation | blättern + 3 Register-Laschen | keine Leiste: Tafel, Stapel hoch/runter, ein Menüknopf | Kopfknöpfe „Netz“ und „★“, Mini-Linie im Thema |
| Tablet / Rechner | echte Doppelseite: Verstehen links, Üben rechts | Sicherheitskarte links, Bordkarte rechts; Tastenkürzel | Verstehen links, Üben rechts; Netzplan daneben |
| Eltern / Lehrkraft | „Lernstand“ auf ruhigem Papier, Kästchen je Lernkarte | „Tower“: Zahlen, Farbband, Wackel-Kasten | „Leitstelle“: dieselbe Linie wie beim Kind mit ●/◐/!/○ |
| Schriften | Caveat + Atkinson Hyperlegible | Space Grotesk + JetBrains Mono | nur Lexend |
| Aufwand (Schätzung) | mittel | groß | mittel |

## Stärken und Schwächen (Urteil)

**heft**
- **Stärken:**
  - Vertrautester Einstieg: Karopapier ist Mathe.
  - Die Stellenwert-Kästchen zeigen beim Tippen, wo die Ziffer steht.
  - Die Doppelseite am Tablet ist die natürlichste Tablet-Lösung der drei.
  - Fehler fühlen sich am freundlichsten an (Klebezettel, Bleistiftgrau).
- **Schwächen:**
  - Handschrift-Optik kippt für den 13-Jährigen schnell ins Kindliche; das Skizzenbuch mildert das, ist aber nur eine Abschwächung.
  - Der Klebezettel bei „falsch“ schiebt den Weiter-Knopf auf dem Handy unter den Rand.
  - Die durchgestrichene Null der Schrift ist ungewohnt.
- **Risiko:** Gemütlich statt mutig – nah an „liebevoll gemacht“, aber nicht neu.

**abflug**
- **Stärken:**
  - Die stärkste, sofort sichtbare Idee.
  - Löst das Hauptproblem am radikalsten: eine Aufgabe pro Bildschirm, Tastenfeld im Daumenbereich, keine Leiste, nichts lenkt ab.
  - Die Kurskorrektur zeigt den Fehler genau an der Stelle, an der er passiert ist.
  - Die Abflugtafel ist als Startseite unverwechselbar.
  - Passt wörtlich zum Leben der Familie: Sie fliegen tatsächlich.
- **Schwächen:**
  - Dunkel als Standard ist für die 10-Jährige kühl (Tag-Ansicht vorhanden).
  - Das Flughafen-Bild ruft „Zeitplan“ auf; Uhrzeiten sind bewusst weggelassen.
  - Die Sicherheitskarte braucht je Erklärschritt ein Bild, das ist Inhaltsarbeit.
  - Größter Umbau.
- **Risiko:** Wenn die Bordkarte nicht wirklich ohne Scrollen auskommt (lange Fragen, Zeichnungen in der Aufgabe), bricht die Idee. Lange Aufgaben brauchen eine Regel, z. B. Zeichnung oben, Tastenfeld einklappbar.

**linien**
- **Stärken:**
  - Beste Orientierung: wo bin ich, was fehlt bis zum Stempel, wie hängen Gebiete zusammen.
  - Das Stellen-Schloss ist die pädagogisch stärkste Eingabe: Die Antwort *ist* die Stellenwert-Entscheidung.
  - Eine einzige Bildsprache für Kind und Erwachsene; die Leitstelle versteht man ohne Legende.
  - Nur eine Schriftfamilie.
- **Schwächen:**
  - Emotional am schwächsten; die Freude kommt nur aus Farbe und Fortschritt.
  - Den Netzplan muss man auf dem Handy seitlich schieben.
  - Feste Netz-Koordinaten je Ort müssen gepflegt werden.
- **Risiko:** Sieht „richtig“ aus, haut aber niemanden vom Hocker – genau der Vorwurf an meinen ersten Entwurf.

## Empfehlung

**Grundlage: `abflug`, ergänzt um zwei Bausteine aus `linien` und einen aus `heft`.**

**Begründung:**
1. Der Auftraggeber will Mut. `abflug` ist die einzige Richtung, die Aufbau *und* Handhabung grundsätzlich ändert und trotzdem ohne Erklärung funktioniert: oben steht, wohin es geht, unten ist der gelbe Knopf.
2. Die größten heutigen Probleme lösen sich direkt: Aufgabe nicht sichtbar, Systemtastatur, drei Navigationssysteme, Strafsatz bei falsch.
3. Die Weltreise ist hier kein Bild, sondern der Ablauf selbst: einsteigen, fliegen, landen, Stempel. Sie lenkt trotzdem nicht vom Rechnen ab, denn in der Aufgabe gibt es nur Frage, Ziffern und Tasten.
4. Die Altersstufen lassen sich gut trennen, ohne zwei Apps: Nacht und dichte Tafel für den 13-Jährigen, Tag, weniger Zeilen und Spaltenköpfe für die 10-Jährige.

**Was woher kommt:**

| Baustein | Herkunft | Wo im Ergebnis |
|---|---|---|
| Abflugtafel als Start, gelber Einsteigen-Knopf, Menüblatt statt Leiste | abflug | Heute |
| Bordkarte: eine Aufgabe pro Bildschirm, eigenes Tastenfeld unten, Perforation, Abriss bei richtig | abflug | Üben |
| Sicherheitskarte (Erklärung in 2 × 2 Bildfeldern zum Aufdecken) | abflug | Erklären |
| Kurskorrektur (DU / ZIEL untereinander, Abweichung markiert) | abflug | falsch |
| Stapel Erklärung · Aufgaben · Fallen, Wischen hoch/runter; Tablet zweispaltig | abflug | Thema |
| Tower, Weltkarte mit Flugbögen, Visa-Pass | abflug | Eltern, Weltkarte, Pass |
| **Stellen-Schloss** für ganze Zahlen der 5./6. Klasse (Spalte antippen, Ziffer wählen; Tippen bleibt möglich) – ersetzt dort die Klapp-Kacheln | linien | Üben (Kind 10) |
| **Linienband „Karten bis zum Stempel“** in der obersten Tafelzeile und auf dem Landebildschirm (statt „3 von 3 Karten offen“) | linien | Heute, sitzt |
| **Tag-Ansicht als Standard für die 10-Jährige**, mit dem warmen Ton der Rückmeldungen aus dem Heft („Fast!“ statt Fachwort, eigene Antwort bleibt sichtbar) | heft (Ton), abflug (Tag-Farben) | ganze Kinderansicht Kind 10 |

**Nicht übernehmen:**
- Handschrift (heft): wirkt für 13 zu kindlich.
- Netzplan als Hauptnavigation (linien): auf dem Handy zu fummelig.

**Vor dem Bau prüfen** (Annahmen, nicht getestet):
- Beide Kinder sollen die drei `entwurf.html` je 5 Minuten durchspielen und sagen, welche sie behalten wollen. Wählt die 10-Jährige deutlich das Heft, ist `heft` mit dem Stellen-Schloss die zweitbeste Lösung, mit geringerem Aufwand.
- Lange Aufgaben und Aufgaben mit Zeichnung (Koordinaten, Figuren) auf der Bordkarte ohne Scrollen nachbauen. Gelingt das nicht, Tastenfeld einklappbar machen.

**Reihenfolge der Umsetzung** (Schätzung, ohne Tage):
1. Bordkarte mit eigenem Tastenfeld und Kurskorrektur. Das ist der größte Gewinn und auch ohne neue Optik nützlich.
2. Stellen-Schloss für Klasse 5/6.
3. Stapel-Navigation und Tablet-Zweispaltigkeit.
4. Abflugtafel als Start.
5. Schriften und Tag/Nacht-Farben.
6. Sicherheitskarte, sobald die Erklärungen Bilder je Schritt haben.
7. Tower, Weltkarte und Pass zuletzt.

## Wichtigste Bilder

- **Vergleich:** `vergleich-handy.png`
- **abflug:**
  - `abflug/handy-heute.png`, `abflug/handy-ueben.png`, `abflug/handy-falsch.png`, `abflug/handy-sitzt.png`
  - `abflug/handy-erklaeren.png`, `abflug/rechner-erklaeren.png`
  - `abflug/handy-eltern.png`, `abflug/handy-hell-heute.png` (Tag-Ansicht)
- **linien:** `linien/handy-ueben.png` (Stellen-Schloss), `linien/handy-falsch.png`, `linien/handy-heute.png`, `linien/rechner-eltern.png`
- **heft:** `heft/handy-heute.png`, `heft/tablet-erklaeren.png` (Doppelseite), `heft/handy-falsch.png`
