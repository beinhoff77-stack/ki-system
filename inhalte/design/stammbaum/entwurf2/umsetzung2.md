# Vorgabe Stammbaum, zweite Runde: nach dem Befund des Mathe-Profis

Designer, 28.11.2026. Entwurf: `index.html` (eine Datei, ohne Netz). `../entwurf1/` bleibt unverändert zum Vergleich. Bilder: `bilder/`.
Adresse (kombinierbar mit `&`): `#g=nacht` · `#k=5…10` · `#auf=<anker>` · **`#frage=an` (Standard) / `#frage=aus`** · `#zeig=1…n|alle` (Schritte aufdecken, nur für Bildschirmfotos).
Bau wie in `../entwurf1/umsetzung1.md` (Datenfelder, `tafeln_bauen.cjs`, `lernen-regeln.js`). Hier steht nur, was neu oder anders ist.

## 1 Was neu ist
1. **Zwei Grundideen statt einer.** Der Leitsatz lautet: „Merken musst du nur: 1. Rechteck = Länge · Breite. 2. Schieben ändert nichts (ab Kl. 6). Alles andere kannst du dir herleiten – beim Kreis brauchst du noch die Zahl π (ab Kl. 8).“ Neben dem Ursprung steht die Karte **Idee 2 „Schieben ändert nichts“**. Sie zeigt drei Parallelogramme und drei Dreiecke zwischen zwei Linien, mit gleichem g und gleichem h. Darunter steht ein sehr schiefes Parallelogramm und ein stumpfwinkliges Dreieck, jeweils mit der Höhe außen. Dazu der Satz „Darum zählt die Höhe, nicht die schräge Seite“. Die Körper-Karte hat dieselbe Idee 2 ab Kl. 8: gerader und schiefer Stapel Bierdeckel.
   - Am Rechner steht Idee 2 rechts neben dem Ursprung. Am Handy steht sie direkt darunter, eingerückt am Stamm.
2. **Frage zuerst (Variante `#frage=an`).** Für Dreieck, Parallelogramm, Trapez, Drachen, Kreis, Pyramide und Kugel beginnt die aufgeklappte Zeile so: „Überleg zuerst“ + Ausgangsbild + Frage, darunter der Knopf **„Zeig mir den Trick ›“**.
   - Jeder Druck deckt einen Schritt auf („Nächster Schritt (2 von 3)“). Der letzte Druck heißt „Und die Formel?“ und zeigt den „weil“-Satz, die Formel und die weiteren Wege. „alles auf einmal“ deckt alles auf.
   - Es ist reines Aufdecken: keine Eingabe, keine Bewertung, keine Punkte, nichts wird gespeichert. An der Lernlogik der App ändert sich nichts.
   - Bezeichnungen und Links stehen immer da.
   - `#frage=aus` zeigt alles offen wie in Entwurf 1, aber mit den neuen Inhalten.
   - Der Schalter steht oben in der Entwurfsleiste. Der Nutzer wählt eine Variante; in der App braucht es dann keinen Schalter.
3. **Körper-Baum neu:** Quader → Würfel. Quader → Prisma · Zylinder → (ein Drittel) Pyramide · Kegel → **(Zylinder minus Kegel) Kugel**. Der Kugel-Ast ist durchgezogen und hat eine echte Herleitung über Cavalieri.

## 2 Befund-Punkte → Stand
### Muss (alle 9 umgesetzt)
| Punkt | Stand |
|---|---|
| M1 Kugel passt nicht in den Zylinder | erledigt: Zylinder-Radius = Kugel-Radius (HER 36/36, Höhe 72); das alte Kantenbild ist ersetzt |
| M2 „keine einfache Idee“ falsch | erledigt: der Satz ist gestrichen. Kugel hat 3 Schritte (passt in den Zylinder; Halbkugel und Zylinder ohne Kegel in Höhe z geschnitten; Kreis π · (r² − z²) = Ring π · r² − π · z² → 2/3 · π · r³ → 4/3 · π · r³), Wortlaut nach Befund. Ast „Zylinder minus Kegel“ unter Pyramide · Kegel, durchgezogen, ab Kl. 10 |
| M3 Kreis benutzt den Umfang zu früh | erledigt: neuer Schritt 1 „Zuerst der Rand … u = π · d = 2 · π · r. Die Hälfte davon ist π · r.“ mit Bild (Umfang abgerollt, gut 3 · d). Der Weg „Umfang“ ist gestrichen |
| M4 Mittellinie „klappen“ | erledigt: „drehst du um die Mitte des Schenkels nach oben (halbe Drehung)“, ebenso im aria-label. Bild größer, mit a, c, m und den zwei Drehpunkten |
| M5 Pyramide h doppelt | erledigt: „Ein Seitendreieck: a · hₛ : 2 – hₛ ist die Höhe des Seitendreiecks, nicht die Körperhöhe h.“ hₛ bei den Bezeichnungen |
| M6 Mantel u · h ohne „gerade“ | erledigt: „Beim geraden Prisma/Zylinder …“ in beiden Wegen und in der Fußzeile; `bed` „h steht senkrecht auf G.“ in beiden Zeilen (auch Pyramide, Kegel) |
| M7 Sinus-Flächenformel Kl. 9 | erledigt: ab Kl. 9 an beiden Stellen, Sternchen weg. Schreibweise „A = a · b · sin γ : 2“ (4a.1) |
| M8 Körper-Leitsatz bei „bis 5“ | erledigt: Leitsatz `data-kl=6`. „Grundfläche aus dem Flächen-Baum“ ab 8, „Körper mit Spitze … ein Drittel“ ab 10 (Bild 11) |
| M9 Flächen-Leitsatz verschweigt π | erledigt: „– beim Kreis brauchst du noch die Zahl π“ ab Kl. 8 |

### Sollte
| Punkt | Stand |
|---|---|
| S1 „Schieben ändert nichts“ | erledigt: als Idee 2 neben dem Ursprung (Flächen ab 6, Körper ab 8), statt nur als Folgerung. Wird in Pyramide Schritt 2, Prisma-Weg „Auch schief“ und „Sehr schief?“ wieder aufgegriffen |
| S2 bequemer Fall | erledigt: Weg „Stumpfer Winkel: Die Höhe liegt außen“ (Bild); Weg „Sehr schief?“ mit (g + s) · h − s · h = g · h (Bild); beides auch in Idee 2 |
| S3 Hälfte zeigen | erledigt: Schritt 3 bei Dreieck und Trapez zeigt das Rechteck mit blauem und gelbem Teil, Text „Blau und Gelb sind gleich groß“ |
| S4 Kreis als Dreieck | erledigt: Weg am Kreis (A = u · r : 2), Weg am Kreisausschnitt (A = b · r : 2), Weg am Kegel (Mantel = π · r · s) |
| S5 Kugel als Ast + Oberfläche | erledigt: Folgerung und Weg „Oberfläche wie der Zylindermantel: 2 · π · r · 2 · r = 4 · π · r²“; 1 : 2 : 3 bleibt |
| S6 Pyramide Sonderfall | erledigt: alle drei Pyramiden gezeigt (je im eigenen Würfel), Schritt 2 „jede andere Pyramide … gleich große Schnitte“, Schritt 3 „Kegel: Pyramide mit sehr vielen Ecken“; Umfüllen als „Versuch zum Nachprüfen“ |
| S7 Trapez enthält Parallelogramm und Dreieck | erledigt: Weg „Eine Formel, drei Figuren“ + Folgerung im Baum |
| S8 Frage vor der Auflösung | erledigt (Abschnitt 1.2), mit den Fragen aus dem Befund. Beim Dreieck leicht erweitert: „Wie wird aus dem Dreieck etwas, das du schon kannst? Tipp: Nimm zwei gleiche Dreiecke.“ **Nicht übernommen:** Klassenfilter beim Öffnen auf die Klasse des Kindes stellen – das ist App-Logik (Profil des Kindes), kein Entwurf; Vorschlag für den Bau: Filter auf `kind.klasse` vorbelegen, „alle“ bleibt wählbar |
| S9 Vorsicht-Kärtchen | erledigt: Dreieck, Trapez, Kreis, Pyramide, Kegel, Kugel; Fußzeile „Zähl die Längen“ in beiden Karten (π-Teil ab 8) |
| S10 Kästchen = cm², Würfel = cm³ | erledigt (Rechteck- und Quader-Schritt) |
| S11 Drachen über zwei Dreiecke | erledigt (Weg mit Bild) |
| S12 „umgedreht“ | erledigt: „auf den Kopf gedreht (halbe Drehung)“ bei Dreieck und Trapez |

### Kann
| Punkt | Stand |
|---|---|
| K1 Sternchen | erledigt |
| K2 gleichseitig | erledigt (leerer Text weg, a beschriftet) |
| K3 zweite Höhe | erledigt: rechter Winkel an beiden Höhen, Beschriftung h<sub>a</sub>, h<sub>b</sub>, h<sub>c</sub> |
| K4 Ausschnitt 90° | erledigt (Viertelkreis mit rechtem Winkel) |
| K5 Prisma-Kante | erledigt (hintere Kante gestrichelt, Kanten- und Zeilenbild) |
| K6 ⅔/4/3 | erledigt (überall „2/3“, „4/3“) |
| K7 Gitter | erledigt („11 Kästchen“, Kästchen 13 px statt 9 px) |
| K8 Ausschnitt-Miniatur | erledigt (Viertelkreis) |
| K9 Beschriftung außerhalb der viewBox | teilweise: Quadrat-Kante, Rechteck „b = 3“ und Quader „c“ verschoben bzw. Bild verbreitert. Die übrigen Bilder sind beim Bau im App-Container zu prüfen (`overflow`) |
| K10 Volumen bei „bis 5“ | erledigt: Die Volumen-Zelle von Quader und Würfel zeigt bei „bis 5“ nur „ab Kl. 6“ |
| K11 Mantel-Wortlaut | erledigt (Wortlaut der App) |
| K12 Druckfarbe | erledigt (`print-color-adjust: exact` für Pillen, Nummern, Knopf) |
| K13 Kreis fast Rechteck | erledigt: in Schritt 4 ist das erste Stück halbiert und ans Ende gesetzt |

### Kann weg (Abschnitt 7)
Folgendes ist gestrichen:
- Heron
- die Weg-Karte „Kreisausschnitt und Kreisring“ in der Kreis-Zeile
- „Jede Seite“ als Folgerung am Dreieck im Baum (bleibt nur am Parallelogramm)
- Sinus und gleichseitig im Baum (nur noch in der Zeile)
- der Satz „keine einfache Umlege-Idee“

## 3 Schreibweisen (Befund 4a)
1. „A = a · b · sin γ : 2“ und „A = a · b · sin α“.
2. Trapez überall „A = (a + c) · h : 2“: in Baum, Zeile und Matrix. **Bau: ff-06 in `formeln-flaechen.json` ändern** (vom Mathe-Profi freigegeben). Die Mittelwert-Lesart steht als Weg „A = m · h mit m = (a + c) : 2“. Der Hinweis „gleich wie in der Tabelle“ entfällt.
3. hₛ als Unicode-Zeichen. h<sub>a</sub>/h<sub>b</sub>/h<sub>c</sub> als HTML-Tiefstellung; im SVG als `<tspan dy="3">` mit 12 px.
4. „2/3“ und „4/3“ (keine ⅔-Glyphe).
5. „M der Mantelflächeninhalt des Körpers“ (App-Wortlaut).
6. Neue Bezeichner ohne Bestand, beim Einspielen in die Tafel-Daten aufnehmen: m (Mittellinie), h<sub>a</sub>, h<sub>b</sub>, h<sub>c</sub>, s (Verschiebung beim schiefen Parallelogramm, nur im Weg „Sehr schief?“), z (Schnitthöhe bei der Kugel), „Dreiecke addieren“ (Vieleck).
7. Fläche und Flächeninhalt: keine Änderung.

## 4 Klassenstufen (nach Tabelle im Befund, Abschnitt 5)
Unverändert gegenüber Entwurf 1, außer: Sinus-Flächenformel **9** (vorher 10). Heron entfällt. Neu:
- „Schieben ändert nichts“ Flächen **6**
- Schieben bei Körpern (Cavalieri) **8** (App-Ergänzung; Lehrplan 10)
- Kreis als Dreieck **8**
- Kegelmantel **10**
- Kugel-Herleitung und Kugel-Oberfläche **10**
- Trapez „eine Formel, drei Figuren“, stumpfwinklig, „Sehr schief?“, Drachen über zwei Dreiecke **6**
Hinweis aus dem Befund für den Bestand: F16 Cavalieri hat `gym: "8"`, aber `schulart: "Gymnasium: 10"` → angleichen (Vorschlag „8–10“).

## 5 Was der Bau zusätzlich braucht (gegenüber umsetzung1.md)
- Datenfelder je Figur zusätzlich:
  - `frage` `{ text, start_bild?, ohne[] }`: `ohne` sind die Schritte, die schon im Ausgangsbild stecken; `start_bild` gibt es nur, wenn es nicht der erste Schritt ist (Kreis: Torte; Pyramide: Würfel mit einer Pyramide).
  - `wege[].vorsicht` (gelbe Kante).
  - `prinzip` je Karte (Idee 2: Titel, Satz, Bilder, `kl`).
  - `leitsatz[]` mit `kl` je Teilsatz.
- Zeichnungs-Bausteine neu:
  - `reihe(…, halb)` (erstes Stück halbiert)
  - `wuerfelPyr` (Würfel mit Pyramide auf Boden-, Rück- oder rechter Fläche, Umriss per konvexer Hülle)
  - `lot`/`RWv` (rechter Winkel an schrägen Höhen)
  - `TI` (Tiefstellung im SVG)
  - Kugel-Schnittbild (Halbkugel neben Zylinder ohne Kegel)
- Aufdecken in `lernen-regeln.js`:
  - nur DOM (`hidden` an `.sb-schritt` und `.sb-ende`), kein Zustand außer „welche Zeile offen“;
  - beim Zuklappen und erneuten Öffnen wieder zu (im Entwurf: bei neuem Aufbau);
  - aus dem Baum geöffnet ebenfalls mit Frage (Befund S8).
- **Druck (nicht ausgearbeitet, nur festgehalten):**
  - Die Matrix immer drucken.
  - Den Baum nur kompakt im Rechner-Layout, quer, eine Seite je Karte: Knoten, Verben, Kantenbilder und Idee 2. Ohne Folgerungen, Wege und aufgeklappte Zeilen.
  - Fragen und Knöpfe nicht drucken.

## 6 Offene Fragen
1. **Welche Variante?** `#frage=an` (Frage, dann Schritt für Schritt) oder `#frage=aus` (alles offen).
2. **Formel in der Matrix-Zeile:** Auch in der Variante „Frage zuerst“ steht die Formel schon in der Zeile der Matrix (Spalte Flächeninhalt/Volumen) und im Knoten des Baums. Die Matrix ist zum Nachschlagen da – so lassen? Andernfalls: Formel im Knoten erst nach dem Aufdecken zeigen.
3. **Idee 2 am Handy:** Sie steht direkt unter dem Ursprung am Stamm und macht den Baum etwa 330 px länger. Alternative: zugeklappt („Idee 2: Schieben ändert nichts ›“).
4. **Pyramiden-Bild:** Die drei Pyramiden stehen nebeneinander in je einem Würfel. Ein auseinandergezogener einzelner Würfel wäre anschaulicher, ist aber im Schrägbild schwer lesbar. Bitte am Bild 10 urteilen.
5. „Mittellinie“ steht als Begriff nicht im Bestand (Befund, Klassen-Tabelle) – aufnehmen oder als „Mitte“ umschreiben?

## 7 Bilder (`bilder/`)
- **Ganze Seite:** 01-390-hell · 02-390-dunkel · 03-1280-hell · 04-1280-dunkel · 08-390-hell-bis-klasse-6 · 11-390-hell-bis-klasse-5
- **Zeilen offen (Variante alles offen):** 05 Dreieck · 06 Trapez · 07 Kreis · 09 Kugel · 10 Pyramide (dunkel) · 17 Parallelogramm (1280)
- **Idee 2 mit stumpfem Dreieck und sehr schiefem Parallelogramm:** 12-390-hell-schieben-stumpfes-dreieck
- **Variante Frage zuerst:** 13 Dreieck zu · 14 Dreieck Schritt 1 · 15 Dreieck aufgedeckt · 16 Kreis nach zwei Schritten (1280)
