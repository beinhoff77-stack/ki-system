# Mathe-Profi – Auftrag 1 (24.11.2026)

Ausgangsstand: Zweig `lernen-app`, Commit `8b0b83b2` (App 0.93.4). Bewertet wurden die **Inhaltsdateien** unter `inhalte/themen/`, nicht der Stand in der Datenbank (Teilung, Freigaben, spätere Korrekturen dort habe ich nicht gesehen).

Dateien in diesem Ordner:

| Datei | Inhalt |
|---|---|
| `auftrag1.md` | dieser Bericht (Teile 0, A–D, Top 3) |
| `nachrechnen.py` | rechnet jede Lösung auf zwei Wegen nach und erzeugt beim Lauf `aufgaben-auftrag1.json` (die 12 Aufgaben als Datensätze im Generator-Format `l, p, s, g, y, f, a, o, h, w, c`): `python3 -I inhalte/mathe-profi/nachrechnen.py` → „OK“ |
| `entwurf-formen.html` | Entwurf zum Anklicken für die 5 neuen Aufgabenformen (ohne echte Daten, ohne Netz) |
| `rolle.md` | Rollenbeschreibung inkl. Vorgabe „kreative Darstellungen“ |

---

## 0. Was die App heute kann (gesichert, aus Code gelesen)

**Antwortformen, die der Server automatisch prüft** (`schule.antwort_bewerten`, `supabase/migrations/20261116_w150_r2_fehlermuster_zweiter_versuch.sql`; Eingabe in `lernAufgabe`, `lernen.js` ab Zeile 2712):

| `antworttyp` | Kind tut | gespeichert | Prüfung | Anteil an allen 26 458 Aufgaben |
|---|---|---|---|---|
| `zahl` | Zahl tippen (Komma, optional Einheit) | `{wert}` | gleich bis `toleranz`; erkennt Fehlermuster Vorzeichen, Komma verrutscht, gerundet | 54 % |
| `auswahl` | eine von 3–4 Antworten tippen | `{index}` | Index gleich | 31 % |
| `luecken` | je Lücke eine **ganze** Zahl; bei Term-Vorlage (`□x + □`) Term frei tippen | `{werte:[…]}` | alle gleich, Reihenfolge fest; erkennt „vertauscht“, „Vorzeichen“ | 15 % |
| `markierung` | Strich auf dem Zahlenstrahl antippen | `{index}` | Index gleich | 0,4 % |
| `text` | kurzes Wort tippen | `{wert}` | gleich ohne Groß/Klein, ohne Leerzeichen | < 0,1 % |

**Zeichnungen** (`lernBild`, `lernen.js` Zeile 3005): Zahlenstrahl (mit Punkten, Bögen, Bereich), Stellentafel, Koordinatensystem (viele Graph-Arten, Punkte, Strecken, Pfeile, Flächen, Kreise), Figur, Säulen, Kreisdiagramm, Tabelle, Boxplot, Baum, Thermometer, Bruchstreifen. Nur **10,7 %** der Aufgaben nutzen eine Zeichnung.

**Was fehlt:** Das Kind kann in keiner Zeichnung etwas tun – außer einen Strich am Zahlenstrahl antippen. Kein Punkt setzen, kein Schieben, kein Einfärben, kein Ordnen, kein Zuordnen, keine Mehrfach-Markierung. Brüche als Antwort nur über `luecken`, Dezimalzahlen nur über `zahl`.

Wo neue Formen eingetragen werden müssten (für den Bau-Chat): `schule.antwort_bewerten`; `lernAufgabe`, `lernAntwortText` (Zeilen 2882 ff.) und die Lösungsanzeige in `lernen.js`; `TYPEN` in `tools/inhalt_pruefen.py`; `v_y` in der Expeditionen-Funktion (`20261119_w176_h_sollte.sql`).

---

## A. Bewertung

### Wahl
- **Klasse 5: „Grundrechenarten und Rechengesetze“** (`zahlen.rechengesetze`, Ort Rom) – meiste Bordkarten in Klasse 5: 548 (379 Übungen), 14 Etappen.
- **Klasse 8: „Lineare Funktionen“** (`funktionen.linear`, Neumayer-Station III) – meiste Bordkarten in Klasse 8: 445 (293 Übungen), 11 Etappen (3 davon Vertiefung).

### A1 – Klasse 5, Rechengesetze

**Was trägt (gesichert):** Durchgehende Kino-/Einkaufs-Einstiege; Fehler-Texte erklären mit Sinn statt Regel („Das wären 7 Kinokarten – gekauft hast du nur 4“); jede Etappe hat Stufe-3-Typen (`begruenden`, `fehler`, `parameter`).

**Probleme, wichtigstes zuerst:**

1. **„Geschickt rechnen“ wird nie geprüft, nur das Ergebnis.**
   Stelle: Etappen `vorteil`, `verteilen`, `differenz_summe`, `kopfrechnen` – 82 Aufgaben mit „geschickt“, davon 79 als `zahl`.
   Bremst, weil: Wer stur von links rechnet, bekommt dieselben Sterne. Das Lernziel ist der Weg – genau der zählt nicht. Das Kind lernt: „geschickt“ ist Deko.
   Ersatz: Je Etappe 4–6 Übungen, die den Weg abfragen: Paar antippen (Aufgabe R1), Lücke im faulen Weg (R2), „Welcher Weg ist am kürzesten?“ (`auswahl`). Dafür gleich viele „Rechne geschickt: a · b“-Karten streichen.

2. **Keine einzige Aufgabe mit Bild (0 von 548).**
   Stelle: ganzer Flug; Zahlenstrahl und Termbaum stehen nur in den Erklärungen (`mal_ganz`, `ueberschlag`, `termaufbau`).
   Bremst, weil: Die Erklärung zeigt das Bild einmal, geübt wird dann nur noch mit Zeichen. Die Vorstellung bleibt nicht hängen.
   Ersatz: Überschlag am Zahlenstrahl (R4), Termbaum ablesen bei `termaufbau` (geht heute: `grafik` `baum` + `auswahl`), Sprünge am Zahlenstrahl bei `mal_ganz`.

3. **Überschlag als Regel-Abarbeiten.**
   Stelle: `ueberschlag`, 19 von 39 Aufgaben schreiben die Rundung vor („Runde dazu den ersten Faktor auf Hunderter …“) und prüfen eine exakte Zahl.
   Bremst, weil: Ein vernünftiger anderer Überschlag (490 · 20 = 9 800) zählt als falsch. Das Kind lernt Rundungsregeln, nicht Schätzen.
   Ersatz: Bereich prüfen statt Zahl (neue Form Schieber, R4) oder „Welches Ergebnis kann stimmen?“ (gibt es schon, gut).

4. **Viel Gleichbau.**
   Stelle: `verteilen` 10 Übungen mit gleichem Satzbau („Rechne geschickt: a · b“), `schriftlich_geteilt` 8, `umkehraufgabe_mal` 7; 65 von 379 Übungen ohne Typ `g`.
   Bremst, weil: Ab der dritten gleichen Karte wird abgearbeitet, nicht gedacht.
   Ersatz: höchstens 3 gleich gebaute je Etappe; der Rest wird durch Weg-Aufgaben (Punkt 1) ersetzt.

5. **Fehler suchen nur als Text-Auswahl.**
   Stelle: Typ `fehler` (z. B. `verteilen`: „Jemand rechnet 7 · 98 = 7 · 100 − 2 …“).
   Bremst nur leicht: Das Kind liest vier lange Antwortsätze und vergleicht Formulierungen statt die Rechnung zu prüfen.
   Ersatz: Rechnung als Tabelle zeigen, Kind tippt die falsche Zeile (R6, geht heute schon mit `tabelle` + `auswahl`).

**Urteil:** Solide Erklärungen und breite Typen, aber der Flug belohnt Ausrechnen statt Durchschauen – das Herzstück „geschickt rechnen“ ist ungeprüft.

### A2 – Klasse 8, Lineare Funktionen

**Was trägt (gesichert):** Gute Alltags-Einstiege (Taxi, Treppe, Kerze, Wanderweg), Fehler mit Gegenbeispiel, Steigungsdreieck in den Erklärungen als Bild; Stufe 3 abwechslungsreich (Rampe 6 %, Lichtstrahl, Tarife).

**Probleme, wichtigstes zuerst:**

1. **Das Kind zeichnet nie eine Gerade.**
   Stelle: `graph_ablesen`; Lehrplanpunkt „Graphen zeichnen“. Ersatz heute: „Du zeichnest y = 2x … Bei welchem Gitterpunkt kommst du an? (□ | □)“ – das ist Zeichnen in Worten. Die Datei vermerkt es selbst unter `offen`.
   Bremst, weil: Zeichnen ist hier die Kernhandlung; t setzen, Dreieck laufen, Gerade sehen. In Worten bleibt es Rechnen mit Koordinaten.
   Ersatz: neue Form „Punkte setzen“ (L1, D3) – zwei Gitterpunkte setzen, App zieht die Gerade, Kind sieht sofort, ob sie passt.

2. **„Wie liegen die Geraden?“ – 19 von 46 Aufgaben derselbe Vierer.**
   Stelle: `lage`, immer die Antworten „parallel / senkrecht / identisch / schneiden sich“.
   Bremst, weil: 25 % Rate-Chance je Karte, und nach drei Karten ist es ein Steigungsvergleich nach Schema.
   Ersatz: Zuordnung mehrerer Paare auf einmal (L5, D4; Raten fast aussichtslos), dazu die vorhandenen Stufe-3-Aufgaben (rechter Winkel im Dreieck, Spiegel) behalten.

3. **Nur 35 von 445 Aufgaben mit Bild – in einem Thema über Graphen.**
   Stelle: `proportional`, `aufstellen`, `schnittpunkte`, `lage`, `einsetzen`, `bueschel` haben 0 Aufgaben mit Bild.
   Bremst, weil: Funktion = Term + Tabelle + Graph. Geübt wird fast nur der Term.
   Ersatz: Graph ↔ Gleichung zuordnen (D4, Beispiel c), Schnittpunkt im Bild antippen (D3), Steigung aus Tabelle (L3, geht heute).

4. **Schieberegler versprochen, nicht geliefert.**
   Stelle: `wirkung`, Einstieg „Ein Schieberegler in einer Mathe-App verändert die Zahl k …“; alle Aufgaben statisch.
   Bremst, weil: Die Wirkung eines Parameters versteht man durch Bewegen, nicht durch Lesen.
   Ersatz: Parameter-Schieber (L2, D2). Einschränkung: Etappe ist Vertiefung, also nicht testrelevant.

5. **Aufstellen ohne den faulen Weg.**
   Stelle: `aufstellen`, 35 Lückenaufgaben „Steigung m, geht durch P(…) → □x + □“.
   Bremst, weil: Die Erklärung zeigt „einsetzen und nach t auflösen“ – richtig, aber der Gedanke dahinter (von P zur y-Achse zurücklaufen) fehlt. Ohne Bild wird es Formel-Einsetzen.
   Ersatz: Erklärung B3 unten.

**Urteil:** Fachlich sauber und gut eingekleidet, aber ein Graphen-Thema, in dem das Kind nie einen Graphen anfasst – das bremst das Verstehen mehr als jede einzelne Aufgabe.

---

## B. Neue Erklärungen

### B1 – Klasse 5, Etappe `ueberschlag`: Faul überschlagen
**Ziel:** Du schätzt ein Ergebnis so, dass es im Kopf geht – und merkst, wenn eine Rechnung nicht stimmen kann.

1. Runde so, dass du **im Kopf** rechnen kannst. Nicht stur nach einer Stelle.
2. Bei **mal**: Rundest du eine Zahl auf, runde die andere ab. Dann gleicht es sich aus.
3. 487 · 21 → 500 · 20 = 10 000.
4. Genau sind es 10 227. Das liegt nah dran: gut.
5. Kommt bei dir 1 022 heraus, fehlt eine Stelle. Der Überschlag hat dich gerettet.
6. Ein Überschlag ist nie „falsch“, nur gut oder grob.

**Bild:** Zahlenstrahl 0 bis 20 000. Pfeil bei 10 000 (Überschlag), Punkt bei 10 227 (genau), weit links ein roter Punkt bei 1 022 („Stelle vergessen“). Sieht man sofort: 1 022 ist meilenweit weg.

**Fauler Weg:** gegensinnig runden (eine Zahl rauf, eine runter). Warum es stimmt: 500 ist 13 zu viel, 20 ist 1 zu wenig – die Fehler arbeiten gegeneinander. Rundet man beide in dieselbe Richtung, addieren sie sich.

**Typischer Fehler:** beide stark abrunden: 48 · 52 ≈ 40 · 50 = 2 000. **Gegenbeispiel:** genau sind es 2 496. Besser 50 · 50 = 2 500 – eine rauf, eine runter, fast genau.

### B2 – Klasse 5, Etappe `verteilen`: Malnehmen am Rechteck
**Ziel:** Du siehst, warum 7 · 98 = 7 · 100 − 7 · 2 ist – und nicht 7 · 100 − 2.

1. 7 · 98 ist ein Rechteck: 7 Reihen mit je 98 Plätzen.
2. Mach das Rechteck größer: 7 Reihen mit je 100. Das sind 700.
3. Jetzt hast du in **jeder** Reihe 2 Plätze zu viel.
4. Zu viel sind also 7 · 2 = 14, nicht 2.
5. 700 − 14 = 686.
6. Merke: Was vor der Klammer steht, trifft **jeden** Teil in der Klammer.

**Bild:** Rechteck 7 Kästchen hoch, 10 breit (ein Kästchen = 10 Plätze), rechts ein schmaler Streifen 7 hoch, schraffiert, beschriftet „7 · 2 zu viel“. Einzige Bewegung: Der Streifen klappt weg. So sieht man: Der Streifen ist so hoch wie das ganze Rechteck.

**Fauler Weg:** Zahl in „glatt minus klein“ zerlegen (98 = 100 − 2). Warum es stimmt: Das Rechteck zeigt es – das Weggenommene ist ein Streifen über alle 7 Reihen.

**Typischer Fehler:** 7 · 98 = 700 − 2 = 698. **Gegenbeispiel:** 2 · 98 = 196. Nach dem Fehler wäre es 200 − 2 = 198 – zwei Taschen zu 98 € kosten aber sicher nicht 198 €, denn 98 + 98 = 196.

### B3 – Klasse 8, Etappe `aufstellen`: Zurück zur y-Achse laufen
**Ziel:** Du findest t, indem du vom bekannten Punkt zur y-Achse zurückläufst.

1. Gegeben: m = 3 und P(2 | 1). Gesucht: wo die Gerade die y-Achse trifft.
2. P liegt 2 Kästchen rechts von der y-Achse.
3. Geh 2 nach links. Bei m = 3 geht es dabei 2 · 3 = 6 nach **unten**.
4. 1 − 6 = −5. Also t = −5.
5. Gerade: y = 3x − 5.
6. Kurz: t = y − m · x (die y-Koordinate minus „m mal Abstand zur Achse“).

**Bild:** Gitter, Punkt P(2 | 1), gestrichelte Treppe von P nach links-unten: 1 nach links, 3 nach unten, zweimal. Unten Punkt (0 | −5) mit Beschriftung t.

**Fauler Weg:** gar keine Gleichung lösen – einmal rückwärts laufen. Warum es stimmt: Die Steigung sagt, wie viel sich y pro Schritt ändert; vom Punkt zur Achse sind es genau x Schritte. Das ist dieselbe Rechnung wie „1 = 3 · 2 + t“, nur im Bild.

**Typischer Fehler:** nach links gehen und dabei nach **oben** zählen: 1 + 6 = 7. **Gegenbeispiel:** y = 3x + 7 bei x = 2 ergibt 13, nicht 1. Die Gerade verfehlt P.

### B4 – Klasse 8, Etappe `schnittpunkte`: Vorsprung durch Aufholen
**Ziel:** Du findest den Schnittpunkt zweier Geraden mit einer Division statt einer langen Gleichung.

1. Tarif A: 8 € plus 0,10 € pro Minute. Tarif B: 2 € plus 0,25 € pro Minute.
2. Am Anfang ist B um 6 € billiger. Das ist der **Vorsprung**.
3. Jede Minute wird B um 0,15 € teurer als A. Das ist das **Aufholen**.
4. Gleich teuer, wenn der Vorsprung aufgebraucht ist: 6 : 0,15 = 40 Minuten.
5. Probe: A 8 + 4 = 12 €, B 2 + 10 = 12 €.
6. Allgemein: x = (Unterschied der t) : (Unterschied der m).

**Bild:** Beide Geraden im Gitter, senkrechte Strecke zwischen ihnen bei x = 0 (6 €), x = 20 (3 €), x = 40 (0 €). Die Strecke schrumpft gleichmäßig – das ist der Gedanke.

**Fauler Weg:** Vorsprung : Aufholtempo. Warum es stimmt: Gleichsetzen 8 + 0,10x = 2 + 0,25x heißt umgestellt 6 = 0,15x – genau diese Division.

**Typischer Fehler:** 6 : 0,25 = 24 (nur das Tempo von B genommen). **Gegenbeispiel:** Bei 24 min kostet A 10,40 €, B 8 €. Nicht gleich.

---

## C. Neue Aufgaben

Alle Lösungen sind in `nachrechnen.py` je zweimal auf verschiedenen Wegen nachgerechnet (Lauf: „OK: 12 Aufgaben“). Datensätze erzeugt `nachrechnen.py` beim Lauf als `aufgaben-auftrag1.json`. Die Etappen-Schlüssel (`l`) sind die der vorhandenen Dateien.

### Flug Klasse 5 – Rechengesetze

**R1 · `vorteil` · leicht (`erkennen`) · braucht neue Form D1 „markieren“**
Text: „Rechne 4 · 17 · 25 · 3 geschickt. Tippe die zwei Faktoren an, die du zuerst malnimmst.“
Antwort: zwei Felder antippen. Lösung: {4, 25}.
Weg 1: 4 · 25 = 100, 17 · 3 = 51, 100 · 51 = 5 100. Weg 2: stur von links 68 · 25 = 1 700, · 3 = 5 100. (Nur 4 · 25 ergibt ein glattes Produkt, geprüft für alle 6 Paare.)
Häufigste falsche Antwort: {4, 17} – verrät: rechnet von links, sucht kein Paar.
Tipp: Welche zwei Zahlen ergeben zusammen eine Zahl mit Nullen am Ende?

**R2 · `verteilen` · mittel (`umkehr`) · geht mit vorhandener Form `luecken`**
Text: „Rechne faul: Klammere die 17 aus. 17 · 23 + 17 · 77 = 17 · □ = □“
Lösung: 100; 1 700.
Weg 1: 17 · (23 + 77) = 17 · 100. Weg 2: 391 + 1 309 = 1 700.
Häufigste falsche Antwort: 100; 3 400 – verrät: hat die beiden 17 zusammengezählt statt ausgeklammert.
Tipp: Beide Produkte haben einen Faktor gemeinsam. Was bleibt in der Klammer?

**R3 · `klammern` · schwer (`parameter`) · geht mit `auswahl`**
Text: „Wo muss die Klammer hin, damit 33 herauskommt? 3 + 4 · 5 − 2“
Auswahl: 3 + 4 · (5 − 2) | **(3 + 4) · 5 − 2** | 3 + (4 · 5 − 2) | „Ohne Klammer kommt schon 33 heraus.“
Weg 1: 7 · 5 − 2 = 33. Weg 2: rückwärts 33 + 2 = 35 = 7 · 5 und 7 = 3 + 4. (Andere Werte: 15, 21, 21.)
Häufigste falsche Antwort: „ohne Klammer“ – verrät: rechnet 3 + 4 = 7 zuerst, Punkt vor Strich nicht verinnerlicht.
Tipp: Rechne rückwärts: Was muss vor dem „− 2“ stehen?

**R4 · `ueberschlag` · mittel (`darstellung`) · braucht neue Form D2 „schieber“**
Text: „Ohne genau zu rechnen: Wo liegt 487 · 21? Schieb den Pfeil an die Stelle.“ (Strahl 0 bis 20 000)
Lösung: jeder Wert von 8 000 bis 12 000 (genau 10 227).
Weg 1: 500 · 20 = 10 000. Weg 2: 487 · 20 + 487 = 9 740 + 487 = 10 227.
Häufigste falsche Antwort: um 1 000 – verrät: Stellenwert verloren (wie im Fehler-Text der Etappe).
Tipp: Runde beide Zahlen so, dass du im Kopf malnehmen kannst.

**R5 · `sach` · schwer (`rueckwaerts`) · braucht neue Form D5 „reihenfolge“**
Text: „Eine Zahl wird mit 4 malgenommen, dann wird 30 abgezogen, dann durch 2 geteilt. Es kommt 25 heraus. Leg die Schritte zum Rückwärtsrechnen in die richtige Reihenfolge. Zwei Bausteine brauchst du nicht.“ Bausteine: + 30 · · 2 · : 4 · − 30 · : 2
Lösung: · 2 → + 30 → : 4 (Startzahl 20).
Weg 1: 25 · 2 = 50, + 30 = 80, : 4 = 20. Weg 2: Probe vorwärts 20 · 4 = 80, − 30 = 50, : 2 = 25.
Häufigste falsche Antwort: : 4 → + 30 → · 2 – verrät: kehrt die Rechenarten um, aber nicht die Reihenfolge.
Tipp: Den letzten Schritt machst du zuerst rückgängig.

**R6 · `schriftlich_geteilt` · schwer (`fehler`) · geht mit `auswahl` + `grafik` `tabelle`**
Text: „Jemand rechnet 2 976 : 12 und erhält 246 Rest 4. In welcher Zeile steckt der Fehler?“
Tabelle: Zeile 1: 29 : 12 = 2 | 2 · 12 = 24 | Rest 5 · Zeile 2: 57 : 12 = 4 | 4 · 12 = 48 | Rest 7 · Zeile 3: 76 : 12 = 6 | 6 · 12 = 72 | Rest 4
Auswahl: Zeile 1 | **Zeile 2** | Zeile 3 | „Alles richtig“.
Weg 1: 57 − 48 = 9, nicht 7; richtig weiter 96 : 12 = 8, Ergebnis 248. Weg 2: Probe 248 · 12 = 2 976; die falsche Lösung ergibt 246 · 12 + 4 = 2 956.
Häufigste falsche Antwort: Zeile 3 – verrät: sucht den Fehler dort, wo er sichtbar wird (Rest), nicht wo er entsteht.
Tipp: Prüfe in jeder Zeile die Minus-Rechnung.

### Flug Klasse 8 – Lineare Funktionen

**L1 · `graph_ablesen` · leicht (`direkt`) · braucht neue Form D3 „punkte“**
Text: „Zeichne die Gerade y = −(2/3)x + 2. Setze dazu zwei Punkte auf Gitterpunkte.“
Lösung: zwei verschiedene Punkte aus {(−3 | 4), (0 | 2), (3 | 0), (6 | −2)} (alle Gitterpunkte im Ausschnitt, per Programm gesucht).
Weg 1: Start (0 | 2), 3 rechts, 2 runter → (3 | 0). Weg 2: Einsetzen x = 3: −2 + 2 = 0; x = −3: 2 + 2 = 4.
Häufigste falsche Antwort: (0 | 2) und (2 | −1) – verrät: Dreieck gekippt (2 nach rechts, 3 nach unten). Die App zeichnet dann sichtbar eine zu steile Gerade.
Tipp: Starte bei t auf der y-Achse. m = −2/3 heißt: 3 nach rechts, 2 nach unten.

**L2 · `wirkung` (Vertiefung) · mittel (`darstellung`) · braucht neue Form D2 „schieber“ (Parameter)**
Text: „Alle Geraden y = k · x + 1 gehen durch (0 | 1). Stell k so ein, dass die Gerade durch P(4 | −1) geht.“
Lösung: k = −0,5 (Schritt 0,25, Toleranz 0,125; Start bei k = 1).
Weg 1: −1 = 4k + 1 ⇒ k = −0,5. Weg 2: Von (0 | 1) nach P: 4 rechts, 2 runter, −2 : 4.
Häufigste falsche Antwort: k = −2 – verrät: Steigung als „runter : rechts“ gekippt.
Tipp: Von (0 | 1) nach P: wie weit nach rechts, wie weit nach unten?

**L3 · `zwei_punkte` · mittel (`darstellung`) · geht mit `luecken` (`m = □/□`) + `tabelle`**
Text: „Die Tabelle gehört zu einer Geraden. Gib ihre Steigung als gekürzten Bruch an.“ x: 0 | 3 | 6 | 9, y: 7 | 5 | 3 | 1
Lösung: −2/3.
Weg 1: ein Schritt: x + 3, y − 2. Weg 2: ganze Tabelle (1 − 7) : (9 − 0) = −6/9 = −2/3.
Häufigste falsche Antwort: −3/2 – verrät: rechts und oben vertauscht. (Die App meldet „vertauscht“ schon heute.)
Tipp: Schau nur auf einen Schritt der Tabelle.

**L4 · `schnittpunkte` · schwer (`transfer`) · geht mit `zahl`**
Text: „Tarif A: 8 € im Monat plus 0,10 € pro Minute. Tarif B: 2 € im Monat plus 0,25 € pro Minute. Bei wie vielen Minuten kosten beide gleich viel?“
Lösung: 40 min.
Weg 1: 8 + 0,1x = 2 + 0,25x ⇒ 6 = 0,15x ⇒ x = 40. Weg 2: Vorsprung 6 € : Aufholen 0,15 €/min = 40.
Häufigste falsche Antwort: 24 – verrät: nur ein Tempo (6 : 0,25) statt des Unterschieds genommen.
Tipp: B ist am Anfang 6 € billiger. Wie viel holt A pro Minute auf?

**L5 · `lage` · mittel (`erkennen`) · braucht neue Form D4 „zuordnung“**
Text: „Ordne jedem Geradenpaar zu, wie die Geraden liegen.“
Paare: y = 3x + 1 / y = 3x − 2 → parallel · y = 3x + 1 / y = −(1/3)x → senkrecht · y = 2x + 4 / 2y = 4x + 8 → identisch · y = x + 1 / y = 2x + 1 → schneiden sich, nicht senkrecht · y = −2x + 3 / y = 0,5x − 1 → senkrecht.
Weg 1: Steigungen vergleichen, Produkt −1 prüfen. Weg 2: Richtungsvektoren (1 | m): Skalarprodukt 0 ⇒ senkrecht, gleiche Richtung + gemeinsamer Punkt ⇒ identisch.
Fünf Paare auf vier Ziele: Das letzte Paar ergibt sich nicht durch Ausschluss.
Häufigste falsche Antwort: Paar 3 als „parallel“ – verrät: 2y = … nicht erst nach y aufgelöst.
Tipp: Vergleiche zuerst die Steigungen. Bei 2y = … erst nach y auflösen.

**L6 · `schnittpunkte` · schwer (`verknuepfen`) · geht mit `zahl`**
Text: „g: y = x − 1 und h: y = −x + 5 schneiden sich im Punkt S. Für welches t geht y = 0,5x + t durch S?“
Lösung: t = 0,5.
Weg 1: S(3 | 2), 2 = 1,5 + t. Weg 2: von S zur y-Achse zurücklaufen (B3): 3 nach links, 1,5 runter, 2 − 1,5 = 0,5.
Häufigste falsche Antwort: 2 – verrät: y-Wert von S mit t verwechselt.
Tipp: Erst S bestimmen, dann S einsetzen.

Nicht nur Zahl tippen: R1, R3, R4, R5, R6 (Kl. 5) und L1, L2, L5 (Kl. 8).

---

## D. Neue Aufgabenformen

Reihenfolge nach Lerngewinn je Aufwand (**Meinung**, begründet je Form). Alle gehen mit Antippen allein; Ziehen ist nirgends nötig. Entwurf aller fünf: `entwurf-formen.html` (getestet bei 360 und 820 px Breite, alle Beispiele klickbar, keine Skriptfehler).

Gemeinsame Regeln für den Server (Vorschlag für `schule.antwort_bewerten`):
- Leere oder unvollständige Antwort → `format_ok: false` mit Hinweis (wie heute), zählt nicht als Fehler.
- Unsinn (Index außerhalb, nicht-numerischer Wert, falsche Länge) → `format_ok: false`.
- Die Lösung wird nie an das Gerät geschickt, bevor geprüft ist (wie heute).

### D1 `markieren` – Felder antippen (beste: kleiner Aufwand, überall nutzbar)

**Kind tut:** tippt eines oder mehrere Felder an: Zahlen in einem Term, Zeilen einer Rechnung, Kästchen eines Rechtecks oder Bruchstreifens. Nochmals tippen nimmt zurück.
**Lernt:** Struktur sehen statt ausrechnen (welches Paar, welche Zeile, welcher Anteil). Das ist genau das, was „geschickt“ und „Fehler finden“ prüfen sollen.
**Gespeichert:** `{"menge": [0, 2]}` (Indizes, aufsteigend).
**Prüfung:** Regel `menge`: Mengengleichheit mit `o.menge` (oder einer aus `o.mengen`, falls mehrere richtig). Regel `anzahl`: nur die Zahl der markierten Felder zählt (zum Einfärben von Anteilen). Toleranz: keine.
**Darstellung:** `f.anzeige`: `term` (Felder in einer Zeile mit Rechenzeichen dazwischen), `zeilen` (eine Zeile je Feld), `raster` (`f.spalten`). `f.anzahl` begrenzt die Auswahl.
**Kleinste Breite:** 360 px bei höchstens 6 Feldern je Zeile (6 × 48 px + Abstände); `raster` höchstens 6 Spalten.
**Nichts getan:** „Tippe mindestens ein Feld an.“ **Unsinn:** mehr als `anzahl` lässt die App nicht zu; Alles-Markieren ist einfach falsch.
**Aufwand:** klein (Knöpfe + ca. 15 Zeilen Server).
**Nicht geeignet:** wenn man erst jedes Feld ausrechnen muss (dann ist es versteckte Mehrfach-Auswahl mit Rechenarbeit) oder bei mehr als ca. 12 Feldern.

Beispiele:
```json
{"l":"vorteil","p":"uebung","s":1,"g":"erkennen","y":"markieren",
 "f":{"text":"Rechne 4 · 17 · 25 · 3 geschickt. Tippe die zwei Faktoren an, die du zuerst malnimmst.","felder":["4","17","25","3"],"anzahl":2,"anzeige":"term"},
 "o":{"menge":[0,2]},"h":"Welche zwei Zahlen ergeben zusammen eine Zahl mit Nullen am Ende?","w":"4 · 25 = 100, dann 100 · 51 = 5 100."}
{"l":"teilbarkeit","p":"uebung","s":1,"g":"erkennen","y":"markieren",
 "f":{"text":"Tippe alle Zahlen an, die durch 3 teilbar sind.","felder":["51","62","75","88","111","124"],"anzeige":"raster","spalten":3},
 "o":{"menge":[0,2,4]},"h":"Bilde die Quersumme.","w":"Quersummen 6, 8, 12, 16, 3, 7: durch 3 teilbar sind 51, 75, 111."}
{"l":"anteile","p":"uebung","s":1,"g":"darstellung","y":"markieren",
 "f":{"text":"Färbe drei Viertel der Tafel.","felder":["","","","","","","",""],"anzeige":"raster","spalten":4},
 "o":{"regel":"anzahl","anzahl":6},"h":"Wie viele Stücke sind ein Viertel von 8?","w":"8 : 4 = 2, drei Viertel sind 3 · 2 = 6 Stücke."}
```
(Lösungen in `nachrechnen.py`, Abschnitt D, geprüft. Die Etappen-Schlüssel `teilbarkeit`/`anteile` sind Platzhalter.)

### D2 `schieber` – Wert auf einer Skala einstellen

**Kind tut:** tippt auf einen Zahlenstrahl (Pfeil springt hin) oder stellt mit − / + einen Parameter ein; beim Parameter dreht oder verschiebt sich der Graph mit. Das ist die eine Bewegung, die den Gedanken zeigt.
**Lernt:** Größenvorstellung, Schätzen vor dem Rechnen, Wirkung eines Parameters.
**Gespeichert:** `{"wert": 10000}` (auf `schritt` gerundet).
**Prüfung:** `o.von ≤ wert ≤ o.bis` (Schätzen) oder `|wert − o.wert| ≤ o.toleranz` (Einstellen; Toleranz = halber Schritt). Fehlermuster: Wert um Faktor 10 daneben → `grund: komma`.
**Darstellung:** `f.grafik` (vorhandener Zahlenstrahl oder Koordinatensystem; im Graphen steht der Parametername statt einer Zahl, z. B. `"m": "k"`), `f.schieber = {name, start, ende, schritt, anfang}`. `anfang: null` = noch kein Pfeil.
**Kleinste Breite:** 360 px. Regel für Inhalte: Der richtige Bereich ist mindestens 1/12 der Skala breit (sonst nicht mit dem Finger treffbar), Feinstellung über − / +.
**Nichts getan:** ohne Pfeil „Setz den Pfeil an eine Stelle.“ Beim Parameter darf `anfang` nie im richtigen Bereich liegen (prüft `inhalt_pruefen.py`). **Unsinn:** Werte außerhalb der Skala kann die App nicht erzeugen; der Server weist sie ab.
**Aufwand:** klein bis mittel (Zahlenstrahl ist da; Parameter-Graph neu zeichnen bei jedem Schritt).
**Nicht geeignet:** genaue Ergebnisse (dafür `zahl`), Skalen über mehrere Zehnerpotenzen.

Beispiele: R4 und L2 (Datensätze in `aufgaben-auftrag1.json`), dazu:
```json
{"l":"dezimal_mal","p":"uebung","s":2,"g":"darstellung","y":"schieber",
 "f":{"text":"Wo liegt ungefähr 19,8 · 4,9?","grafik":{"typ":"zahlenstrahl","start":0,"ende":1000,"abschnitte":10,"beschriftet":"anfang_ende"},
      "schieber":{"start":0,"ende":1000,"schritt":5,"anfang":null}},
 "o":{"von":80,"bis":120,"wert":97.02},"h":"Runde auf ganze Zahlen.","w":"20 · 5 = 100. Genau: 97,02. Bei 9,7 oder 970 ist das Komma verrutscht."}
```

### D3 `punkte` – Punkte im Koordinatengitter setzen

**Kind tut:** tippt Gitterpunkte an (die App rastet ein, nochmals tippen entfernt). Bei `linie: "gerade"` zieht die App nach zwei Punkten die Gerade – das Kind sieht selbst, ob sie passt.
**Lernt:** Graphen zeichnen, Steigungsdreieck laufen, Spiegeln und Verschieben, Schnittpunkte sehen. In Klasse 6–10 der größte Hebel, weil das heute gar nicht geht.
**Gespeichert:** `{"punkte": [[0, 2], [3, 0]]}` (eingerastete Koordinaten).
**Prüfung:**
- `gleich`: Menge der Punkte = `o.punkte`, Reihenfolge egal.
- `folge`: wie `gleich`, aber Reihenfolge zählt (z. B. A′, B′, C′).
- `auf_gerade`: jeder Punkt erfüllt |m·x + t − y| ≤ `o.toleranz` (0,25), Punkte verschieden; m und t als Bruch `[zähler, nenner]`.
Toleranz beim Tippen: Der Finger darf bis 0,5 Kästchen daneben liegen, die App rastet auf den nächsten Gitterpunkt (`raster` 1 oder 0,5).
**Kleinste Breite:** 360 px bei höchstens 12 Kästchen je Achse (≈ 28 px je Kästchen; das Einrasten ersetzt die 44-px-Tippfläche je Punkt).
**Nichts getan:** „Setze 2 Punkte.“ **Unsinn:** Tippen außerhalb wird ignoriert; zweimal derselbe Punkt geht nicht (Antippen entfernt ihn).
**Aufwand:** mittel (Eingabe-Ebene im vorhandenen `lernKoordinaten`, Rückrechnung Bildschirm → Koordinate, drei Server-Regeln).
**Nicht geeignet:** krumme Koordinaten, Parabeln freihand, Konstruktionen mit Zirkel.

Beispiele: L1 (in `aufgaben-auftrag1.json`), dazu:
```json
{"l":"achsenspiegelung","p":"uebung","s":1,"g":"direkt","y":"punkte",
 "f":{"text":"Spiegle das Dreieck an der y-Achse. Setze A′, B′, C′ in dieser Reihenfolge.",
      "grafik":{"typ":"koordinaten","x":[-5,5],"y":[-1,4],"flaechen":[{"punkte":[[1,1],[4,1],[1,3]]}],"punkte":[{"x":1,"y":1,"name":"A"},{"x":4,"y":1,"name":"B"},{"x":1,"y":3,"name":"C"}]},
      "setzen":{"anzahl":3,"raster":1,"namen":["A′","B′","C′"]}},
 "o":{"regel":"folge","punkte":[[-1,1],[-4,1],[-1,3]]},"h":"Gleich weit von der y-Achse, nur auf der anderen Seite.","w":"Aus x wird −x, y bleibt: A′(−1 | 1), B′(−4 | 1), C′(−1 | 3)."}
{"l":"deuten","p":"uebung","s":2,"g":"einkleidung","y":"punkte",
 "f":{"text":"Eine Kerze ist 18 cm hoch und wird pro Stunde 2 cm kürzer: h(x) = −2x + 18. Tippe den Punkt an, an dem sie abgebrannt ist.",
      "grafik":{"typ":"koordinaten","x":[0,10],"y":[0,20],"schritt_y":2,"graphen":[{"art":"linear","m":-2,"t":18}]},"setzen":{"anzahl":1,"raster":1}},
 "o":{"regel":"gleich","punkte":[[9,0]]},"h":"Abgebrannt heißt: Höhe 0.","w":"−2x + 18 = 0 ⇒ x = 9. Punkt (9 | 0)."}
```

### D4 `zuordnung` – Paare bilden

**Kind tut:** tippt links ein Element an, dann rechts das Ziel. Das Paar wird angezeigt, das nächste offene links ist schon gewählt.
**Lernt:** Darstellungen verbinden (Term ↔ Graph ↔ Tabelle ↔ Satz), Begriffe unterscheiden.
**Gespeichert:** `{"paare": [0, 1, 2, 3, 1]}` (für jedes linke Element der Index rechts).
**Prüfung:** exakt gleich `o.paare`. Rückmeldung darf „3 von 5 stimmen“ sagen, ohne zu verraten, welche. Gegen Raten durch Ausschluss: mehr Ziele als Paare **oder** `mehrfach: true` mit mehr Paaren als Zielen.
**Kleinste Breite:** 360 px, untereinander (erst Liste, dann Ziele als Knöpfe); ab 600 px nebeneinander. Höchstens 6 Paare.
**Nichts getan / unvollständig:** „Ordne alle zu.“ **Unsinn:** nicht möglich.
**Aufwand:** mittel.
**Nicht geeignet:** wenn sich die Paare nur durch Ausrechnen jedes Elements finden lassen (dann sind es versteckte Einzelaufgaben); mehr als 6 Paare.

Beispiele: L5 (in `aufgaben-auftrag1.json`), dazu:
```json
{"l":"termaufbau","p":"uebung","s":1,"g":"erkennen","y":"zuordnung",
 "f":{"text":"Wie heißt der Term? Ordne zu.","links":["3 + 4 · 5","(3 + 4) · 5","20 − 12 : 4","(20 − 12) : 4"],"rechts":["Summe","Differenz","Produkt","Quotient","Potenz"]},
 "o":{"paare":[0,2,1,3]},"h":"Welche Rechnung kommt zuletzt?","w":"Zuletzt plus: Summe; zuletzt mal: Produkt; zuletzt minus: Differenz; zuletzt geteilt: Quotient."}
{"l":"graph_ablesen","p":"uebung","s":2,"g":"darstellung","y":"zuordnung",
 "f":{"text":"Welche Gleichung gehört zu welchem Graphen?","grafik":{"typ":"koordinaten","x":[-3,4],"y":[-3,4],"graphen":[{"art":"linear","m":2,"t":-1,"name":"g"},{"art":"linear","m":-0.5,"t":2,"name":"h"},{"art":"linear","m":0.5,"t":-1,"name":"k"}]},
      "links":["g","h","k"],"rechts":["y = 2x − 1","y = 0,5x − 1","y = −0,5x + 2","y = −2x − 1"]},
 "o":{"paare":[0,2,1]},"h":"Erst t an der y-Achse, dann steigt oder fällt?","w":"g: t = −1, steil steigend. h: t = 2, fallend. k: t = −1, flach steigend."}
```

### D5 `reihenfolge` – Rechenweg aus Bausteinen legen

**Kind tut:** tippt Bausteine der Reihe nach an, sie füllen die Plätze; einen gelegten antippen nimmt ihn zurück. Ablenker sind erlaubt.
**Lernt:** Struktur eines Lösungswegs (Rückwärtsarbeiten, Reihenfolge der Rechenschritte, Ablauf beim Aufstellen).
**Gespeichert:** `{"folge": ["mal2", "plus30", "durch4"]}`.
**Prüfung:** exakt gleich `o.folge` oder eine aus `o.folgen` (wenn zwei Reihenfolgen richtig sind, z. B. vertauschbare Schritte).
**Kleinste Breite:** 360 px, Bausteine höchstens 6, Plätze dürfen umbrechen.
**Nichts getan / zu wenig:** „Lege 3 Bausteine.“ **Unsinn:** nicht möglich.
**Aufwand:** mittel.
**Ehrlich:** Ordnen ist leichter als selbst finden – die Bausteine verraten die Schritte. Lerngewinn deshalb kleiner als bei D1–D4. Gut als Brücke auf Stufe 1–2 und für den ersten Kontakt mit einem Verfahren; nicht als Test-Aufgabe.
**Nicht geeignet:** Verfahren, bei denen die Reihenfolge egal ist; lange Rechnungen (mehr als 5 Schritte).

Beispiele: R5 (in `aufgaben-auftrag1.json`), dazu:
```json
{"l":"klammern","p":"uebung","s":1,"g":"direkt","y":"reihenfolge",
 "f":{"text":"Rechne 48 − (6 + 2) · 5. In welcher Reihenfolge? Ein Baustein bleibt übrig.","bausteine":[{"id":"a","text":"6 + 2 = 8"},{"id":"b","text":"8 · 5 = 40"},{"id":"c","text":"48 − 40 = 8"},{"id":"d","text":"48 − 6 = 42"}],"plaetze":3},
 "o":{"folge":["a","b","c"]},"h":"Klammer zuerst, dann Punkt vor Strich.","w":"(6 + 2) = 8, 8 · 5 = 40, 48 − 40 = 8."}
{"l":"aufstellen","p":"uebung","s":2,"g":"mehrschritt","y":"reihenfolge",
 "f":{"text":"Gerade durch P(2 | 1) und Q(6 | −1). Leg die Schritte in die richtige Reihenfolge. Ein Baustein ist falsch.",
      "bausteine":[{"id":"m","text":"m = (−1 − 1) : (6 − 2) = −0,5"},{"id":"e","text":"P einsetzen: 1 = −0,5 · 2 + t"},{"id":"t","text":"t = 2"},{"id":"g","text":"y = −0,5x + 2"},{"id":"x","text":"Q einsetzen: 6 = −0,5 · (−1) + t"}],"plaetze":4},
 "o":{"folge":["m","e","t","g"]},"h":"Ohne Steigung kannst du nichts einsetzen.","w":"m = −2 : 4 = −0,5; 1 = −1 + t ⇒ t = 2; Probe mit Q: −0,5 · 6 + 2 = −1."}
```

**Warum diese Reihenfolge (Meinung):** D1 kostet am wenigsten und macht sofort die zwei größten Lücken prüfbar (Weg statt Ergebnis, Fehler finden). D2 ist fast so billig und bringt Schätzen und Parameter. D3 hat den größten Einzelgewinn für Klasse 6–10, kostet aber mehr. D4 ersetzt rateanfällige Vierer-Auswahl. D5 sieht nach „Tun“ aus, bringt aber am wenigsten eigenes Denken.

Bewusst **nicht** vorgeschlagen: Waage für Gleichungen (sieht gut aus, aber in Klasse 8 lernen Kinder dort mit negativen Zahlen und Brüchen – die Waage bricht dann zusammen; für Klasse 5–6 einfache Gleichungen eventuell später), freies Zeichnen mit dem Finger (nicht sauber prüfbar).

---

## Top 3: Was ich an der App zuerst ändern würde (Meinung)

1. **Den Weg prüfen, nicht nur das Ergebnis.** In jeder Etappe, deren Lernziel ein Weg ist („geschickt“, „überschlagen“, „Fehler finden“, „ausklammern“), mindestens ein Drittel der Übungen mit Weg-Abfrage (D1, Lücken im Weg wie R2, Fehlerzeile wie R6). Und: „gelandet“ erst, wenn mindestens eine davon richtig war. Sonst übt das Kind Rechnen, wo es Durchschauen üben soll.
2. **Das Kind im Bild handeln lassen.** D3 (Punkte setzen) und D2 (Schieber) bauen, dann in Klasse 6–10 jede Geometrie- und Funktionen-Etappe um wenigstens 3 solcher Übungen ergänzen. Heute haben 89 % aller Aufgaben kein Bild und in keinem einzigen kann das Kind etwas darin tun.
3. **Schätzen vor dem Rechnen als fester Baustein.** Bei Stufe-2/3-Rechenaufgaben gelegentlich zuerst „Wo liegt das ungefähr?“ (D2), danach die genaue Rechnung, und in der Rückmeldung beide nebeneinander zeigen. Das trainiert genau den Fehler, den die Lernkarten selbst als häufigsten nennen (Stelle vergessen, Komma verrutscht), und macht aus „abarbeiten“ ein „Passt das?“.

---

## Nicht geprüft / offen

- Stand in der Datenbank (Teilung, spätere Korrekturen, Freigaben) – bewertet sind die Dateien in `inhalte/themen/`.
- Die neuen Aufgaben habe ich nicht mit `tools/inhalt_pruefen.py` geprüft (das Werkzeug erwartet eine ganze Themen-Datei und kennt die neuen Antworttypen nicht). Nachgerechnet sind sie mit `nachrechnen.py`.
- Lehrplan-Zuordnung von Geradenscharen (`wirkung`, `bueschel`, `einsetzen`) zur 8. Klasse habe ich nicht gegen LehrplanPLUS geprüft; die Datei führt sie als Vertiefung.
- Die Häufigkeiten „häufigste falsche Antwort“ sind **Annahmen** aus typischen Fehlern, nicht aus Daten der Kinder. Mit den Versuchsdaten in der Datenbank ließe sich das prüfen – dafür hatte ich keinen Zugriff.
- Der Entwurf zeigt nur Mechanik; Aussehen, Dunkelmodus-Feinschliff und Bildsprache (Bordkarte) macht der Gestalter.
