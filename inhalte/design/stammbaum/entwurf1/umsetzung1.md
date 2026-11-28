# Vorgabe Stammbaum, erste Runde: Stammbaum der Flächen und Körper in „Formeln auf einen Blick“

Designer, 28.11.2026. Entwurf: `index.html` (eine Datei, ohne Netz; Schriften aus `vendor/schriften` über relativen Pfad). Bilder: `bilder/`.
Adresse: `#g=nacht` (dunkel), `#k=6` (Klassenfilter 5…10), `#auf=dreieck` (Zeile aufgeklappt; Kennungen = Anker der Karten: `rechteck`, `quadrat`, `parallelogramm`, `dreieck`, `trapez`, `drachen`, `kreis`, `ausschnitt`, `kreisring`, `quader`, `wuerfel`, `prisma`, `zylinder`, `pyramide`, `kegel`, `kugel`), kombinierbar: `#g=nacht&k=8&auf=kreis`.
Sprache wie die App: Variablen `--ru-*` aus `lernen-regeln.css`, Tafel-Bausteine `ru-tafel-*` (Karte, Matrix mit aufklappbarer Zeile, Klassenfilter), Gebietsfarbe Fläche und Raum (`#5AAEFF`). Neu sind nur Klassen mit Präfix `sb-` (Stammbaum).

## 1 Was der Nutzer wollte
„Nicht jede Formel einzeln lernen, sondern sich das logisch erklären können“ – die Zusammenhänge („zwei Dreiecke ergeben ein Rechteck“) fehlen. Er hat „Stammbaum bauen“ gesagt.

## 2 Aufbau (in der bestehenden Tafel „Formeln auf einen Blick“, kein neuer Reiter)
Karte **Ebene Figuren** (oben, unverändert mit blauer Kante):
1. **Leitsatz** (ruhige Zeile mit gelbem Strich): „Merken musst du nur: Rechteck = Länge · Breite. Alles andere kannst du dir herleiten …“
2. **Stammbaum der Flächen.** Ursprung Rechteck (größer, Gebietsfarbe, Kästchen-Bild „Länge mal Breite – Kästchen zählen“). Vier Äste, jeder mit Verb (schwarze Pille) + Bild des Tricks (vorher → nachher; Ausgangsfigur neutral in der Tafel-Tönung, bewegte/verdoppelte Fläche gelb wie die Markierung „gelb umrahmt“ im Universum) + Knoten (Name, Formel, „ab Kl.“; antippbar → springt zur Zeile der Matrix und klappt sie auf):
   - gleich lang machen → Quadrat (5)
   - Ecke umsetzen → Parallelogramm (6) → verdoppeln → Dreieck (6) → zerlegen → jedes Vieleck (6); verdoppeln → Trapez (6)
   - einrahmen → Drachenviereck und Raute (6)
   - umlegen → Kreis (8); Kreisausschnitt und Kreisring als antippbare Folgerungen am Knoten
   - **Weitere Wege** als gestrichelte Kärtchen am Knoten (Folgerungen): Parallelogramm „jede Seite kann Grundseite sein“; Dreieck rechtwinklig, jede Seite, gleichseitig (9), mit Winkel (10); Trapez „in zwei Dreiecke zerlegen“.
   - Fußzeile: „Umfang: keine Formel nötig – einmal außen herum addieren“ (Satz zu π erst ab Kl. 8).
3. **Alle Formeln** – die bestehende Matrix (Figur | Umfang | Flächeninhalt), Formeln wörtlich aus den Tafel-Daten.
4. **Aufgeklappte Zeile** neu in dieser Reihenfolge: (1) „So kommst du drauf“ – Herleitung in 2–3 nummerierten Schritten mit Bild, (2) Satz „Kommt vom …, weil …“ (blauer Strich), (3) Formel groß, (4) „Weitere Wege“ (je Klasse, Mini-Bild oder eine Zeile Begründung, Heron gestrichelt als „Zusatz“), (5) wie bisher: Bezeichnungen, Bedingung, „Alle Einzelheiten und Beispiele ›“, „Warum? … ›“.

Karte **Körper**: Leitsatz „Merken musst du nur: Volumen = Grundfläche · Höhe.“ Ursprung Quader („V = a · b · c = G · h“, Schichten stapeln). Äste: gleich lang machen → Würfel (6); Grundfläche tauschen → Prisma · Zylinder (8, zwei Knoten nebeneinander) → ein Drittel → Pyramide · Kegel (10); zwei Drittel (gestrichelter Ast, „Zusammenhang – begründet wird er in Klasse 10“) → Kugel (10). Fußzeile Oberfläche: Netz aufklappen (ab Kl. 8 Zylindernetz mit Mantel u · h, darunter Quadernetz). In Klasse 5 steht statt des Baums der Hinweis „Volumen kommt ab Klasse 6“.

**Layout.** Handy (390 px): senkrechter Baum, Stamm links, je Ast Verb + Bild über dem Knoten, Pfeil in den Knoten; Unteräste eingerückt; der Stamm endet am letzten sichtbaren Knoten (per Messung, `--sb-bis`). Rechner (≥ 900 px): Ursprung oben mittig, Äste nebeneinander mit Querbalken (Org-Chart-Linien aus `::before/::after`), Parallelogramm- und Prisma-Ast doppelt breit (`--sb-w: 2`, Kinder nebeneinander). Dafür die Seite der Formel-Tafel am Rechner auf 1 120 px verbreitern (wie Tafel „Figuren“, `lernen-regeln.css` Zeile 752); die Matrix darunter bleibt wie sie ist. Kleinste Schrift 12 px (gemessen, auch in den SVGs: Zeichnungen in Pixelgröße = viewBox, nicht skaliert).

**Klassenfilter.** Jeder Ast, Knoten, jede Folgerung und jeder „weitere Weg“ trägt `data-kl`; „bis Klasse k“ blendet alles darüber aus (wie heute die Zeilen). Danach werden erste/letzte sichtbare Äste neu bestimmt (`sb-erst`, `sb-letzt`, `sb-allein`), damit keine Linie ins Leere läuft. „Zusatz“ (Heron) nur bei „alle“.

## 3 Was der Bau braucht
### Daten (neu je Figur/Körper) – Vorschlag: eigene Quelle `inhalte/mathe-profi/regeln-uebersicht/tafeln/stammbaum/stammbaum.json`
Inhalt vom Mathe-Profi prüfen lassen (Texte im Entwurf sind Designer-Fassung), dann wie die übrigen Tafeln in `tools/tafeln_bauen.cjs` einlesen:
| Feld | Bedeutung | Beispiel Dreieck |
|---|---|---|
| `anker` | Karte in `formeln-flaechen`/`formeln-koerper` | `dreieck` |
| `von` | Elternknoten im Baum (`null` = Ursprung) | `parallelogramm` |
| `verb` | Wort an der Kante | „verdoppeln“ |
| `kante_satz` | kurzer Satz unter dem Kantenbild (optional) | „Zwei gleiche Dreiecke = ein Parallelogramm“ |
| `knoten_formel` | Formel im Knoten (darf von der Matrix-Schreibweise abweichen, s. offene Frage 2) | `A = g · h : 2` |
| `weil` | Satz „Kommt vom …, weil …“ | s. Entwurf |
| `herleitung[]` | 2–3 Schritte: `{ text, bild }` | 3 Schritte |
| `formel_herleitung` | Formel am Ende der Herleitung (+ `formel_hinweis`) | `A = g · h : 2` |
| `wege[]` | `{ titel, formel, satz, kl, bild?, zusatz? }` | 6 Wege |
| `folgerungen[]` | Kurzform der Wege für den Baum `{ text, formel?, kl, ziel? }` | 4 |
| `ehrlich` | Hinweis, wenn keine Anschauung (Kugel) | – |
| `kl` | **nicht neu**: aus `karten[].kl` bzw. Formel-Eintrag (`ab_klasse.gymnasium_by`) | 6 |
Knoten ohne eigene Zeile: „jedes Vieleck“ (springt zum Dreieck). Körper: Knoten „Prisma · Zylinder“ und „Pyramide · Kegel“ sind je zwei Karten mit gemeinsamem Ast (`gruppe`).

### Zeichnungen
Neue SVG-Bausteine in `tools/tafeln_bauen.cjs` neben `BILD` (gleiche Stilregeln: Strich 2, Hilfslinien gestrichelt, Beschriftung Festbreite 13 px). Im Entwurf als kleine Funktionen in `index.html` (`AST` = Kantenbilder, `HER` = Herleitungsschritte, `WEG` = Mini-Bilder, Helfer `torte`, `reihe`, `dreh`, `quader`, `zylinder`, `kegel`) – übertragbar. Alle aus Koordinaten gerechnet: gedrehte Kopien als echte 180°-Drehung um die Seitenmitte, Tortenstücke mit exakten Bögen (Breite der Reihe = n/2 Sehnen ≈ π · r), Höhen senkrecht, Würfelzerlegung mit gemeinsamer Ecke. Neue CSS-Klassen für Flächen: `.f-n` (neutral = `--ru-tafel-tint`), `.f-m` (bewegt = `--ru-marke`), `.f-d`, `.f-o`, `.f-g`, `.f-t` (13 px), `.f-tl` (12 px) – oder auf die bisherigen Attribut-Strings (`F`, `D`, `L` in `tafeln_bauen.cjs`) umstellen und für „bewegt“ `fill="var(--ru-marke)"` ergänzen.

### App (`lernen-regeln.js`)
- `tafelFormeln(t)`: vor `formelMatrix(F, 'Figur')` bzw. `formelMatrix(K, 'Körper')` Leitsatz + `stammbaum(…)` einsetzen; Überschrift „Alle Formeln“ (h3) vor die Matrix.
- `formelZeile(t, k).detail`: neue Reihenfolge Herleitung → `weil` → Formel → Wege → bisheriger Inhalt (Bild/Mantel/Bezeichnungen/Bedingungen/Zusatz/Links). Das große Einzelbild links (`ru-tafel-d-kopf`) entfällt in Zeilen mit Herleitung (die Herleitung zeigt die Figur schon).
- Knoten-Klick: vorhandenen Aufklapp-Mechanismus der Matrix nutzen (`aria-controls`), dazu Sprung mit Versatz unter den festen Kopf (Entwurf: 72 px) und kurze Markierung `ru-tafel-ziel`.
- Klassenfilter: vorhandene Logik über `data-kl` greift; zusätzlich Linien neu setzen (Funktion `linien()` im Entwurf) – auch bei Größenänderung.
- Detailseite „Alle Figuren mit Beispielen“ (`tafelFormelKarten`) bleibt; dort optional dieselbe Herleitung (Abschnitt „So kommst du drauf“).
- Suche: Stichwörter je Knoten ergänzen („halbes Rechteck“ gibt es schon), z. B. „Tortenstücke“, „Mittellinie“, „Heron“, „umfüllen“.
- Druck: Baum am Rechner-Layout drucken oder ausblenden (offen, s. Frage 6).

## 4 Klassenstufen (Gymnasium Bayern) – woher
Aus den Daten übernommen (`daten/regeln-universum.json` → `tafeln[].karten[].kl`, Quelle `formeln-flaechen.json`/`formeln-koerper.json`, `ab_klasse.gymnasium_by`):
Rechteck 5, Quadrat 5, Parallelogramm 6, Dreieck 6, Trapez 6, Drachen/Raute 6, Kreis 8, Kreisausschnitt 8, Kreisring 8; Quader/Würfel 5 (Oberfläche) bzw. 6 (Volumen, im Körper-Baum verwendet), Prisma 8, Zylinder 8, Pyramide 10, Kegel 10, Kugel 10.
**Annahmen des Designers (nicht in den Tafel-Daten, bitte gegen den Lehrplan prüfen):**
- „Jede Seite kann Grundseite sein“, rechtwinkliges Dreieck a · b : 2, Gitter „ergänzen und abziehen“, Trapez „in zwei Dreiecke zerlegen“, Mittellinie: **6** (wie die Figur; F4 „Zerlegen und Ergänzen“ steht bei 5–6).
- Gleichseitiges Dreieck a² · √3 : 4: **9** (braucht Pythagoras, G24 = 9).
- A = ½ · a · b · sin γ und Parallelogramm a · b · sin α: **10** (Annahme; im Entwurf mit * markiert). G25 (Sinus im rechtwinkligen Dreieck) steht bei **9** – für spitze Winkel ginge es schon in 9, für stumpfe braucht man den Sinus über 90° (10).
- Heron: ohne Klasse, „Zusatz, kein Pflichtstoff“, nur bei Filter „alle“.
- Kreis-Abschätzung 2 · r² < A < 4 · r², Umfang π · d: **8**.
- Zusammenhang Kegel : Kugel : Zylinder = 1 : 2 : 3: **10**.
- Pyramide/Kegel: in den Daten 10 (Gymnasium), Realschule 9 – Baum zeigt Gymnasium.

## 5 Offene Fragen
1. **Inhalt prüfen** (Mathe-Profi): Texte der Herleitungen, „weil“-Sätze und Wege sind Designer-Fassung; Rechnungen sind nachgerechnet (Gitter-Beispiel 24 − 3 − 6 − 4 = 11; Trapez-Kopie ergibt Grundseite a + c; Mittellinie m = (a + c) : 2; Würfel = 3 kongruente Pyramiden; ⅔ · π · r² · 2r = 4/3 · π · r³).
2. **Trapez-Schreibweise:** Matrix (Daten) „(a + c) : 2 · h“ (Mittelwert-Lesart, F7), Herleitung über Verdoppeln führt natürlich zu „(a + c) · h : 2“. Entwurf zeigt im Baum die zweite und erklärt die Gleichheit in der Zeile. Eine Schreibweise festlegen?
3. **Kugel:** Ist der Zusammenhang „⅔ vom Zylinder“ (Archimedes) als Ast gewünscht, oder soll die Kugel ohne Ast neben dem Baum stehen? Der Entwurf sagt ehrlich „begründet wird er in Klasse 10“.
4. **Breite 1 120 px** für die Formel-Tafel am Rechner – einverstanden? Bei 760 px müsste der Baum am Rechner wie am Handy senkrecht laufen (funktioniert ohne Änderung, nur Media-Query weglassen).
5. **Klasse 5 bei Körpern:** Volumen ab 6 → Baum ausgeblendet, Hinweis + Quadernetz. Reicht das?
6. **Druck:** Baum mitdrucken (eine Seite quer) oder nur Matrix?
7. **Ausgearbeitet vs. angedeutet:** voll ausgearbeitet (Herleitung in Schritten + Wege): Dreieck, Parallelogramm, Trapez, Kreis; kürzer (ein bis zwei Bilder + Satz): Rechteck, Quadrat, Drachen/Raute, Kreisausschnitt, Kreisring, alle Körper (Pyramide mit Würfelzerlegung und Umfüllversuch). Die „Was man sonst noch braucht“-Karte ist nur als Platzhalter gezeigt.

## 6 Bilder (`bilder/`)
01-390-hell · 02-390-dunkel · 03-1280-hell · 04-1280-dunkel (ganze Seite) · 05-390-hell-dreieck-offen · 06-390-hell-trapez-offen · 07-390-hell-kreis-offen (Ausschnitt ab der Zeile) · 08-390-hell-bis-klasse-6 (ganze Seite) · 09-1280-hell-parallelogramm-offen · 10-390-dunkel-pyramide-offen.
