# Vorgabe TF, erste Runde: Tafeln zum Nachschlagen im Regel-Universum

Designer, 27.11.2026. Entwurf: `index.html` (eine Datei, ohne Netz; Ansichten über `#universum`, `#tafeln`, `#einheiten`, `#flaechen`, `#koerper`, `#suche=<Wort>`; Zusätze `&g=nacht`, `&bis=5`, `&offen=volumen`). Bilder: `bilder/`.
Sprache des Universums (entwurf7: Grundfarben Abflug hell/dunkel, Gebietsfarben „Geld und Verhältnisse“ #B4E86A für Einheiten, „Fläche und Raum“ #5AAEFF für Flächen und Körper; Space Grotesk / JetBrains Mono), aber als ruhige Nachschlagekarte: eine Karte je Größe/Figur, keine Bilder außer den Zeichnungen.

## 1 Aufbau
- **Einstieg im Universum:** direkt unter dem Umschalter „Aufbau | Durch die Klassen“ und über der Sonne eine Leiste mit Tinte-Rand: „Tafeln zum Nachschlagen · Alles auf einen Blick“ mit drei Chips („km · m · cm“, „A = a · b“, „V = a · b · c“) und ›. Am Handy im ersten Bildschirm sichtbar (Bild 01). Dazu findet die Suche jede Tafel-Karte („cm“, „umrechnen“, „Kreis“, „Volumen“ …) und springt an die Stelle (Bild 15).
- **Tafel-Übersicht** (`#tafeln`): drei große Kacheln (Maßeinheiten, Flächen und Umfang, Körper), darunter „Bald dazu:“ als gestrichelte Platzhalter (Bruch · Dezimal · Prozent, Quadrat- und Primzahlen, Teilbarkeitsregeln). Weitere Tafeln = weitere Kachel + eine Ansicht nach demselben Muster (Kopf mit Klassen-Filter und „Drucken“, Raster gleich großer Karten).
- **Jede Tafel:** Brotkrumen „‹ Universum › Tafeln“, Titel, Leiste „bis Klasse 5 6 7 8 9 10 alle“ (blendet aus, was noch nicht dran war), rechts „Drucken“ (Druckfassung ohne Kopf, Filter und Knöpfe; Aufklapper werden mitgedruckt). Handy eine Spalte, ab 900 px Raster (Einheiten 3, Flächen/Körper 2–3 Spalten). Kein seitliches Rollen (gemessen bei 400 und 1280 px in allen 17 Bildern).
- **Maßeinheiten:** oben der Leitsatz „abwärts mal, aufwärts geteilt“ mit dem Merksatz der Richtung. Je Größenart eine Karte: echte **Treppe** (jede Stufe 22 px weiter rechts, Faktor „↘ · 1 000“ auf dem Absatz zwischen zwei Stufen), bei Volumen „= 1 l“ / „= 1 ml“ neben dm³/cm³ und die Hohlmaß-Reihe darunter (hl, dl, cl als Zusatz grau), Merksatz, ein Beispiel „von = nach, denn …“. Aufklapper „So geht’s · Beispiele · Stolperstellen“: So geht’s, alle Beispiele, Stolperstellen (Fehler fett, Richtiges dahinter), Gut zu wissen, Warum? (Herleitung), Verweis auf die Regel im Universum. Dichte nur im Aufklapper „ab Klasse 8: Dichte“.
- **Flächen und Umfang:** acht Karten – Zeichnung (108 px, eine Strichstärke 2, Hilfslinien gestrichelt, rechter Winkel markiert, Beschriftung a b c g h r e f α b in Festbreite) · Name · „ab Kl. n“ · Bedingung klein; darunter Formel-Tabelle „Fläche | Umfang“ (bei Kreisausschnitt „Bogen“), Formel 19 px (Handy 17,5 px), Bezeichnungen in einer Spalte; unten „Warum? ‹Einzelregel› ›“.
- **Körper:** sieben Karten wie oben mit Schrägbild (verdeckte Kanten gestrichelt) und „Volumen | Mantel | Oberfläche“.

## 2 Daten
| Element | Quelle | Stand |
|---|---|---|
| Formeln Flächen und Körper | `daten/regeln-universum.json` → `formeln` (`fuer`, `formel`, `bedingung`, `ziel`), wörtlich | vorhanden, 28 Formeln |
| „Warum?“-Verweis | `formeln[].ziel` → Einzelregel `gesetze[]` (F2 … F18), Adresse im Universum `…-regel-f2` | vorhanden |
| „ab Kl. n“ und Klassen-Filter (Flächen, Körper) | erste Zahl von `gesetze[ziel].gym` | vorhanden; nur Gymnasium – für Realschule/IB `rs`/`ib` der Einzelregel bzw. Schulart des Kindes nehmen |
| Maßeinheiten: Treppen, Faktoren, Merksätze, So geht’s, Beispiele, Stolperstellen, Hinweise, Herleitung, Regeln, Klasse | `inhalte/mathe-profi/regeln-uebersicht/einheiten/einheiten.json` (Redakteur, 27.11.), im Entwurf wörtlich eingebettet | vorhanden; für die App nach `daten/` übernehmen (z. B. als `tafeln.einheiten` in `regeln-universum.json` über `tools/regeln_bauen.cjs`) |
| Zeichnungen | neu (SVG im Entwurf, je Figur/Körper ein Schlüssel) | neu – in `regeln_bauen.cjs` als Text übernehmen wie die übrigen Zeichnungen |
| Tafel-Übersicht, Platzhalter, Suchwörter | neu | neu |

## 3 Was fehlt (Inhalt, nicht erfunden; im Entwurf als „Inhalt fehlt“ gezeigt)
- **Umfang:** Quadrat, Parallelogramm, Dreieck, Trapez, Drachenviereck/Raute – in `formeln` steht nur der Umfang von Rechteck, Kreis und die Bogenlänge.
- **Oberfläche der Pyramide** (nur „Mantel = Summe der Seitendreiecke“).
- **Raute** hat keine eigene Zeile (nur „Drachenviereck und Raute“); Quadrat/Würfel teilen sich die Einzelregel mit Rechteck/Quader.
- **Geschwindigkeit, Dichte:** keine Klasse im Bestand (`ab_klasse` leer, Hinweis des Redakteurs) – im Entwurf „Kl. offen“, Dichte nur aufklappbar.
- **Klassen-Filter** gilt im Entwurf für Gymnasium; Werte für Realschule/IB liegen in den Daten, die Schulart des Kindes muss die App mitgeben.
- **Nicht aufgenommen (Redakteur):** Winkel, Temperatur (keine Treppe).
- Die drei Platzhalter-Tafeln haben noch keinen Inhalt (Lückenprüfung läuft).

## 4 Bilder (`bilder/`)
01/06 Einstieg im Universum hell/dunkel · 02/07 Tafel-Übersicht · 03/08 Maßeinheiten (ganz) · 04/09 Flächen und Umfang (ganz) · 05/10 Körper (ganz) · 11–14 dasselbe bei 1280 px hell · 15 Suche „cm“ · 16 Volumen aufgeklappt · 17 Maßeinheiten „bis Klasse 5“.
