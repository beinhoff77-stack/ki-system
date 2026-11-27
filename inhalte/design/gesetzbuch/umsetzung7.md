# Vorgabe GB, siebte Runde: Regel-Universum in Ebenen, gestufte Regelseite

Designer, 27.11.2026. Gilt vor `umsetzung.md` (Fassung 7 / sechste Runde) für Aufbau und Seitenfolge; Zeichenstil, Klassenleiter und Farben aus `umsetzung.md` gelten weiter.
Entwurf: `entwurf7/index.html` (EINE Datei, alle Ansichten, Umschalten über `#`-Sprünge, kein Nachladen, hell und dunkel). Gebaut mit `entwurf7/bauen.py`; Bilder: `entwurf7/bilder/`.
**[G]** gesichert (gebaut und gemessen, Chrome 400 × 860, wenn nicht anders genannt) · **[A]** Annahme · **[M]** Meinung.

## 1 Was sich gegenüber Runde 6 ändert und warum
| Rückmeldung des Nutzers | Antwort in Runde 7 |
|---|---|
| „Alles auf einmal drin“, keine strukturierte Übersicht | Seite in **Ebenen**: jede Ebene zeigt wenig, ein Tipp führt eine Ebene tiefer. Keine Zeichnung, kein Rechenbeispiel, kein Merksatz auf Ebene 0 und auf der Liste der 14 Regeln. |
| „Die einzelnen Universen … tiefer und tiefer“ (Zusatz) | Ebene 0 Universum → Ebene 1 Sonne / ein Gebiet / Arbeitsweisen → Ebene 2 Regel oder Idee → Ebene 3 einzelne Regel eines Gebiets. |
| Gestuft: Kurzbeschreibung → Merksatz → Beispiel → ausführlich | Regelseite mit sieben Stufen; 1–3 offen, 4–7 aufklappbar. |
| Fassung B („Durch die Klassen“) fast besser | Zweite Ansicht „Durch die Klassen“ über den Umschalter; Handy: Klasse wählen, je Regel das Beispiel dieser Klasse; Rechner: volle Tabelle. Dazu Stufe 4 jeder Regelseite. |
Weggefallen gegenüber Runde 6: Sonnenschnitt mit Karten, Planetenbahnen mit Ideen-Karten und Zeichnungen auf der Startseite, Kasten „Dieselbe Regel in 6 Klassen“ oben.
Die abgelehnte Fassung RS-H (`regeln-sonnensystem/`) diente nur als Anregung für das Bild der Ebene 0; übernommen ist allein „Sonne oben, Bahnen darunter“. Keine Kurznamen wie „Waage“ oder „Werkzeug-Gürtel“, keine Monde, kein Lernstand.

## 2 Adressen und Ebenen [G]
| Ebene | Adresse | Inhalt |
|---|---|---|
| 0 | `#universum` (auch leer) | Titel, ein Satz, Umschalter, Sonne, 7 Gebiete, Arbeitsweisen |
| 1 | `#sonne` · `#gebiet-zahlen` … `#gebiet-daten` · `#weisen` | 14 Regeln in 4 Schichten · Ideen eines Gebiets · 8 Arbeitsweisen |
| 2 | `#r1` … `#r14` · `#idee-geo-1` · `#weise-3` | gestufte Seite |
| 3 | `#regel-f17` | einzelne Regel eines Gebiets (Satz, Beispiel, Stufen, soweit Daten da sind) |
| – | `#klassen`, `#klassen-7` · `#suche` · `#lehrer-r6` | Durch die Klassen · Treffer · Lehrer-Blatt |
Brotkrumen auf jeder Ebene ab „‹ Universum“; Titel sagt „Wo bin ich“ (z. B. „Die Sonne / 14 Rechenregeln“, „Gebiet 4 von 7 / Geometrie“, „Rechenregel 6 von 14 · Schicht 2“). Zustand hell/dunkel in einer Variablen, gemerkt nur per try/catch-localStorage; Suchbegriff in einer Variablen. Keine Query-Strings.

## 3 Seiten und Maße (Handy 400 px; Rechner ab 900 px)
**Kopf (alle Seiten):** 60 px, klebend; Marke „Regel-Universum“ (führt zu Ebene 0), Suchfeld 44 px.
**Umschalter** „Aufbau | Durch die Klassen“: zwei Felder je 44 px hoch, aktives Feld Tinte auf Grund. Steht auf Ebene 0 und in „Durch die Klassen“; die Sonne (Ebene 1) hat unten den Verweis „Dieselben Regeln durch die Klassen ›“.

**Ebene 0 Universum.** Sonne: halber Kreis aus vier Ringen (Farben s1–s4), Feld 136 px hoch, ganze Fläche tippbar, Text „Die Sonne · die Grundlage / 14 Rechenregeln / gelten in jedem Gebiet und jeder Klasse“. Darunter „Darum die sieben Gebiete:“ und sieben Bahnen (Bogenlinie 1,5 px, Wölbung 22 px), Planet 44 px abwechselnd links (6 %) und rechts (38 %), Name 18 px fett, „n tragende Ideen“ 15 px; Tippfläche 50 px. Unten die Arbeitsweisen als gestrichelte Kapsel (60 px). Seite 982 px hoch. Rechner: dieselbe Spalte, höchstens 760 px breit, mittig.
**Ebene 1 Sonne.** Kopf mit Sonnen-Scheibe 48 px. Vier Schicht-Kästen (linker Rand 8 px in Schichtfarbe), Kopfzeile „Schicht n · Name“ und rechts die Ziffern 5–10 (12 px) über dem Band. Je Regel eine Zeile ≥ 48 px: Nummer im Kreis 28 px · Name 17 px · Klassenband (6 × 16 × 20 px, Abstand 3; voll = eingeführt, Balken unten = angewendet, gestrichelt = Vorwissen, hellgrau = kommt nicht vor). Legende einmal darunter. **Gemessen: Liste der 14 Regeln 935 px hoch (400 px) = 1,09 Bildschirmhöhen; 1 047 px bei 360 px. Ganze Seite 1 423 px (400), 1 535 px (360).** Ziel „höchstens gut zwei Bildschirmhöhen“ erfüllt.
**Ebene 1 Gebiet.** Kopf mit Planet 48 px, „Gebiet n von 7“, Name 26 px; Satz „n tragende Ideen. Hinter ihnen stehen m einzelne Regeln und Formeln.“ Je Idee eine Karte: Nummer · Kurzname 15 px leise · Merksatz 17 px fett · Band mit Ziffern (24 × 22 px). Unten „‹ Gebiet n | Gebiet n+2 ›“. Zahlen: Liste 675 px, Seite 1 141 px.
**Ebene 1 Arbeitsweisen.** Wie Gebiet, ohne Band (keine Klassendaten). Seite 1 054 px.

**Ebene 2 Regelseite (B).** Reihenfolge:
1. Brotkrumen „‹ Universum › Sonne › Schicht 2“ · Zeile „Rechenregel 6 von 14 · Schicht 2“ (13 px Versalien) · Name 24 px fett.
2. **Kurzbeschreibung** 17 px leise, ein Satz (Quelle Abschnitt 6).
3. **Merksatz** in gelb getönter Fläche (Gelb 22 % auf Fläche, Rand 70 %), Etikett „Merksatz“, Satz 26 px fett (Rechner 32 px).
4. **Beispiel:** das erste Feld der Hauptzeichnung mit Rechnung und Satz (bei allen 14 Regeln und 28 Ideen vorhanden). [A] „Das einfachste“ = Feld 1 der Zeichnung; Feld 1 ist laut Vorgaben des Mathe-Profis immer der Zahlenfall.
5. Stufen als Klappzeilen (54 px hoch, Titel 17 px fett, rechts Hinweis 15 px, Pfeil 24 px): „Dieselbe Regel in Klasse 5 bis 10“ (Hinweis: das Band) · „Genau erklärt“ (warum · wann) · „Typische Fehler“ (Anzahl) · „Worauf sie aufbaut, was auf ihr aufbaut“ (Anzahl Verweise).
6. Unten „‹ Regel 5 Name | Regel 7 Name ›“, je ≥ 64 px.
Inhalt der Stufen: **Klassen** = Band mit Ziffern, Legende, Satz „Gelb umrahmt …“, Klassenleiter aus Runde 6 unverändert. **Genau erklärt** = „Genau gesagt“, „Warum das gilt“, „Wann sie gilt – und wann nicht“ (Feld `voraus`), „Weitere Bilder (n)“ (übrige Felder der Zeichnung), „Verwandt“. **Fehler** = Feld `fehler`, an „Und:“ in Punkte geteilt. **Aufbau** = „Lässt sich erklären über“, „Hilft beim Erklären von“ (Gegenrichtung), Satz „keine Lernvoraussetzung und keine Sperre“, „Darauf bauen auf: n Regeln in m Gebieten“ (Sprung zur Idee).
**Stufe 4 offen oder zu? Gemessen** (Höhe der geöffneten Stufe bei 400 px): Rechenregeln 765 px (R1) bis 1 001 px (R11), Ideen 388 bis 1 053 px. Das ist bei allen Regeln fast oder mehr als eine Bildschirmhöhe → **standardmäßig zu** (Schalter `VERGLEICH_OFFEN` in `app.js`). [M] Das Band in der Klappzeile zeigt auch geschlossen, in welchen Klassen die Regel vorkommt.
**Idee (Ebene 2):** dieselben Stufen; Stufe 6 heißt „Die Regeln und Formeln dahinter (n)“ (Sprung zu Ebene 3), Stufe 7 „Worauf sie aufbaut“ (Rechenregeln, die sie benutzt). Blättern über alle 28 Ideen.
**Arbeitsweise (Ebene 2):** Name, Merksatz, Kasten „Noch offen“ (Abschnitt 6).
**Ebene 3:** Name, Satz, erstes Beispiel; Klappzeilen „In den Klassen“, „Genau erklärt“, „Typische Fehler“, „Worauf sie aufbaut“ nur, wenn Daten da sind (49 von 152 ausgearbeitet).

**Durch die Klassen (C).** Entscheidung: **Handy = eine Klasse wählen, je Regel nur das Beispiel dieser Klasse; Rechner ab 900 px = volle Tabelle 14 × 6.** Begründung: Eine Regel durch alle Klassen steht schon in Stufe 4 jeder Regelseite; die neue Ansicht beantwortet die andere Frage „Was davon kommt in Klasse 7 vor?“ und zeigt beim Wechseln der Klasse, dass dieselben 14 Regeln wiederkehren. Die Tabelle ist am Handy nur mit Querwischen lesbar (Runde 6). [M]
Handy: Satz zur Bedienung; Klassenwahl „Klasse 5 6 7 8 9 10“ (je 44 px, klebt unter dem Kopf); vier Schicht-Kästen; je Regel Nummer · Name 15 px leise · Rechnung 16 px Festbreite mit gelb umrahmter Stelle · Art (Einführung/Anwendung/Vorwissen) 14 px; ohne Beispiel „kommt in Klasse 9 nicht vor“ kursiv. Darunter zugeklappt „Tragende Ideen in Klasse 7“ (nach Gebiet). Wechsel der Klasse lässt die Seite stehen. Seite 2 277 px (Klasse 7). [A] Bei zwei Beispielen einer Klasse steht am Handy nur das erste; die Tabelle zeigt beide.
Rechner: Tabelle, Kopf „Rechenregel | Klasse 5 … 10“, Schicht-Zeilen in Schichtfarbe, Zellen 15 px Festbreite, „–“ wo die Regel nicht vorkommt.

## 4 Was sieht man, ohne zu tippen (400 × 860) [G]
| Seite | Im ersten Bildschirm | Erst nach Wischen / Tippen |
|---|---|---|
| Ebene 0 | Titel, Satz, Umschalter, Sonne „14 Rechenregeln“, alle 7 Gebiete mit Zahl der Ideen, Anfang der Kapsel „8 Arbeitsweisen“ | Kapsel ganz (Seite 982 px); alles Weitere eine Ebene tiefer |
| Sonne | Kopf, Schicht 1 und 2 ganz (8 Regeln), Kopf Schicht 3 | Schicht 3 und 4 (bis 1 222 px), Legende |
| Gebiet | 4 bis 5 Ideen mit Merksatz und Band | Rest, Legende, Blättern |
| Arbeitsweisen | 6 bis 7 von 8 mit Satz | Rest |
| Regel | Name, Kurzbeschreibung, Merksatz, Beispiel-Bild; erste Klappzeile am unteren Rand (R6: ab 780 px) | Stufen 4–7 zu. Bei R2 und R3 (hohe Zeichnung) beginnen die Klappzeilen erst bei 983 / 1 058 px |
| Idee | wie Regel | wie Regel |
| Durch die Klassen | Bedienung, Klassenwahl, Schicht 1 mit 4 Regeln und Beispiel | übrige 10 Regeln (bis 2 068 px), Ideen zugeklappt |
| Lehrer-Blatt | Leiste „Eltern und Lehrer / So sieht es das Kind“, Kopf, Merksatz mit Rückmelde-Knopf | alles offen, Seite 6 259 px |

## 5 Lehrer-Ansicht (E), nach `regeln-lehrer.md` [G als Beispiel-Blatt `#lehrer-r6`]
Wie die Regelseite, aber ohne Klappen, in fünf nummerierten Kästen (Reihenfolge nach `regeln-lehrer.md` Regel 2): **1 Merksatz** (wörtlich wie beim Kind) · **2 Was das Kind sieht** (Beispiel, Klassenvergleich, typische Fehler) · **3 Fachliche Erklärung** (Genau gesagt, Warum, Wann sie gilt, weitere Bilder, Verwandt) · **4 Verweise und Zuordnung**: Lehrplan (Tabelle Gymnasium / Realschule / IB MYP aus `kennungen.json`, darunter offen: „Nicht geprüft: LehrplanPLUS an der Quelle; Realschule und IB nur bis zum Thema“), Themen der App je mit Knopf „Lehrer-Seite ›“, bis zu drei Beispielaufgaben mit Lösung (aus `mathe-profi/schritt1/`, Zuordnung `kennungen-zuordnung.json`; R6: RG-05, RG-06, RG-11), Fehlbilder mit Kennung, Aufbau · **5 Stand je Kind**: „Stand folgt“.
Leiste oben (Tinte, 44 px Knopf) „So sieht es das Kind ›“ öffnet die Regelseite. Knopf „Rückmeldung geben“ (44 px, Rand 1,5 px) im Kopf der Kästen 1–4 = an Merksatz, Karte, Erklärung, Zuordnung. Im Entwurf zeigt er nur den Hinweis mit dem Bezug, z. B. „rr.ausmultiplizieren · Merksatz“; in der App: `schule_rueckmeldung_geben` mit Art Fehler/Vorschlag/Frage. „Lehrer-Seite ›“ hat im Entwurf kein Ziel.
Für die anderen Regeln baut dieselbe Funktion das Blatt (`#lehrer-r1` …); Beispielaufgaben gibt es für 12 von 14 (R10, R14: keine zugeordnet; R9: 1; R1: 2).

## 6 Texte für den Mathe-Profi
**Gekürzt vom Designer, vom Mathe-Profi zu prüfen** (alle in `entwurf7/teile/kurz.json`, mit Quelle):
| Regel | Kurzbeschreibung | gekürzt aus |
|---|---|---|
| 1 | Jede Stelle ist zehnmal so viel wert wie die Stelle rechts von ihr. | Warum, Satz 1 |
| 2 | Plus und Minus sind Schritte auf der Zahlengeraden: nach rechts oder nach links. | Warum |
| 3 | Welches Vorzeichen das Ergebnis bei Mal und Geteilt bekommt. | Genau gesagt |
| 4 | Die Reihenfolge ist eine Vereinbarung, damit jeder dieselbe Rechnung gleich liest. | Warum (wörtlich) |
| 5 | Bei einer Summe und bei einem Produkt kommt es nicht auf die Reihenfolge an. | Warum |
| 6 | Ein Faktor vor einer Klammer: vorwärts ausmultiplizieren, rückwärts ausklammern. | Genau gesagt |
| 7 | Ein Minus vor der Klammer heißt „mal (−1)“. | Warum (wörtlich) |
| 8 | Hoch ist wiederholtes Malnehmen. | Warum von Regel 4 (wörtlich) |
| 9 | Die Menge bleibt gleich, nur die Einteilung wird feiner. | Warum (wörtlich) |
| 10 | Wie man Brüche addiert, subtrahiert, malnimmt und teilt. | Genau gesagt |
| 11 | Wer den Wert für eine Einheit kennt, kennt jeden anderen. | Warum (wörtlich) |
| 12 | Zu jeder umkehrbaren Rechnung gibt es eine Gegenrechnung. | Warum |
| 13 | Das Gleichheitszeichen sagt: Links und rechts steht gleich viel. | Warum (wörtlich) |
| 14 | Eine Gleichung „Produkt = 0“ darf man in einfache Gleichungen zerlegen. | Warum |
- 28 Ideen: Kurzbeschreibung = erster Satz von „Warum“; **gekürzt** bei Zahlen 3, Zahlen 5, Geometrie 2, Fläche und Raum 1, Funktionen 3, Daten und Zufall 3 (umformuliert: „Die Wahrscheinlichkeit eines Ereignisses ist sein Anteil an allen Möglichkeiten.“).
- [A] Bei 1, 3, 10 ist die Kurzbeschreibung eher Thema als Aussage. Bitte prüfen, ob „worum es geht“ so gemeint ist.
**Fehlt (nicht erfunden):** Arbeitsweisen: Kurzbeschreibung, Beispiel, Erklärung, typische Fehler, Klassen. Ebene 3: 103 von 152 Regeln nur mit Name, Satz, Klasse. Beispielaufgaben für R10 und R14.
**Vom Designer** (Bedienungstexte, kein Mathe-Inhalt): „Alle festen Regeln der Mathematik, Klasse 5 bis 10. Tippe auf einen Teil.“, „Die Sonne · die Grundlage“, „gelten in jedem Gebiet und jeder Klasse“, „Darum die sieben Gebiete:“, „wie man vorgeht – gilt überall“, „Keine Rechenregeln, sondern wie man vorgeht.“, Stufen-Titel.

## 7 Geprüft [G]
- Klick-Prüfung (Playwright, 400 × 860, Tippen): 357 von 357 Schritten bestanden, keine Skriptfehler. Ebene 0 → Sonne → jede der 14 Regeln → jede der 4 Stufen auf und zu → Zurück → Brotkrume „Universum“; vorige/nächste; Umschalter beide Richtungen; Klasse 5–10 wählen; Klassenzeile → Regel → zurück; jedes der 7 Gebiete → jede der 28 Ideen → je 4 Stufen auf → zurück; Universum → Gebiet → Idee → Ebene 3 → Brotkrume Idee → Rechenregel → viermal Zurück → Gebiet → Universum; Arbeitsweisen; Suche „Kegelmantel“ → F17; Lehrer-Blatt: 4 Rückmelde-Knöpfe, 3 Aufgaben, „So sieht es das Kind“; hell/dunkel.
- Nichts läuft über den Rand bei 360 und 400 px (alle Stufen offen, 12 Seiten geprüft).
- Tippflächen: kein Knopf, keine Zeile, kein Verweis unter 44 px (8 Seiten). Fließtext ≥ 16 px. Kleiner sind nur Etiketten: Versal-Etiketten 13 px, Ziffern im Band 12–14 px, Legende 14 px, Art/Meta 14–15 px, Namen über Rechnungen 15 px. [M] tragbar, weil daneben immer ein Text ≥ 16 px die Aussage trägt.
- Bilder angesehen: `ebene0-universum-400-hell/-dunkel`, `ebene0-universum-1280-hell`, `ebene1-sonne-400-hell-ganz`, `ebene1-sonne-1280-hell`, `ebene1-gebiet-geometrie-400-hell`, `ebene2-regel6-zu-400-hell`, `ebene2-regel6-klassen-offen-400-hell`, `ebene2-idee-400-hell`, `klassen-7-400-hell`, `klassen-1280-hell`, `lehrer-regel6-400-hell`. Berichtigt dabei: Kopfzeile der Tabelle lag über den Zeilen; Sonnentext dunkel zu schwach; Fehlbild-Kennung lief über den Rand; Ideen-Band ohne Ziffern.

## 8 Nicht geprüft / offen
- Echte Geräte (iPhone Safari, Android); nur Chromium. `<details>` und `color-mix()` brauchen Safari ≥ 16.2.
- Dunkel nur an Ebene 0 und Regel 6 angesehen; die anderen Seiten dunkel nicht.
- Veröffentlichung als Mehrdatei-Vorschau nicht ausprobiert (Datei ist eigenständig, nur `#`-Sprünge).
- Bildschirmleser nicht geprüft (Band hat `aria-label`, Klappen sind `<details>`).
- Ob der Nutzer Ebene 0 „anschaulich genug“ findet: [M] ruhig und verständlich, aber weniger Bild als Runde 2.
- Die Zeichnungen (übernommen aus Runde 6) sind fachlich so geprüft wie dort beschrieben; neu ist nur ihre Stelle.

## 9 Prüfliste für den Bau
**Muss:** Ebenen und Adressen wie Abschnitt 2 · Brotkrumen ab „Universum“ auf jeder Ebene · Regelseite: Stufen 1–3 offen, 4–7 zu, Reihenfolge wie Abschnitt 3 · Liste der 14 Regeln ohne Satz, Bild, Beispiel · Klassenband mit vier Zuständen · Umschalter auf Ebene 0 und in „Durch die Klassen“ · Lehrer-Blatt alle Abschnitte offen, Rückmeldung an 4 Stellen · Tippflächen ≥ 44 px, Fließtext ≥ 16 px · nichts läuft bei 360 px über.
**Soll:** Ebene 0 passt bis auf die Kapsel „Arbeitsweisen“ in 400 × 860 · Klassenwahl klebt · Wechsel der Klasse ohne Sprung nach oben · Blättern auf Regel-, Ideen-, Gebietsseite.
**Kann:** Kurzbeschreibung für Arbeitsweisen, sobald geliefert · Tabelle „Durch die Klassen“ am Rechner mit klebender Kopfzeile (im Entwurf weggelassen, weil sie im Querlauf-Kasten falsch lag).

## 10 Achte Runde (27.11.) – Merksätze in der Liste, stärkeres Bild, Band erklärt sich selbst
Anlass: Der Nutzer hat die Vorschau gesehen: „Ansonsten ist es so, wie ich es mir vorstelle.“ Die Ebenen bleiben. Gilt vor den Abschnitten 3 und 4, wo es abweicht.
**Geändert [G]**
- **Liste der 14 Regeln:** Je Zeile steht oben links der Name (16 px fett) und rechts das Band; darunter steht der Merksatz über die ganze Breite (16 px, leise, wörtlich aus `satz`, bei Regel 10 die drei Sätze in einer Zeile hintereinander). Die ganze Zeile ist tippbar. Entscheidung: Das Band steht neben dem Namen, nicht neben dem Merksatz. Grund: Neben dem Merksatz blieben bei 400 px nur etwa 150 px Text übrig, das ergäbe 4 bis 5 Zeilen. Unter dem Text würde jede Zeile eine Zeile höher. Merksätze werden nicht abgeschnitten: Ein halber Merksatz wäre falsch. Bei 400 px haben 13 von 14 Merksätzen höchstens zwei Zeilen, Regel 10 hat drei.
- **Klassenband vereinfacht:** In jedem Kästchen (20 × 20 px, in der Klappzeile 36 × 30 px) steht die Klasse. Es gibt drei Zustände: **gefüllt = neu** (Einführung), **Rahmen = kommt vor** (Anwendung oder Vorwissen), **blass ohne Rahmen = kommt nicht vor**. Die Legende ist eine Zeile direkt über der Liste (Sonne, Gebiet) und über der Leiter. „Anwendung“ und „Vorwissen“ unterscheidet weiter die Klassenleiter in ihrer Textzeile. Damit ist F6.5 aus `umsetzung.md` ersetzt.
- **Schnitt durch die Sonne** (Ebene 1, über der Liste): Halbkreis mit vier Bändern von innen nach außen (Radien 56, 98, 140, 182 von 400). Jedes Band trägt „n Name der Schicht“ (15 px fett). Ein Tipp auf ein Band scrollt zur Schicht, sanft oder sofort bei `prefers-reduced-motion`. Darunter steht „Schnitt durch die Sonne: innen die Grundlage, außen, was darauf aufbaut. Tippe eine Schicht an.“ Jeder Schicht-Kasten zeigt statt des farbigen Randstreifens ein **Ringbild** (34 px: vier Ringe, die eigene Schicht kräftig mit Rand, die anderen 30 % deckend). Das Ringbild steht auch auf der Regelseite vor „Rechenregel n von 14“.
- **Ebene 0 am Rechner (ab 900 px): echtes Sonnensystem-Bild** (SVG 1100 × 600). Die Sonne mit vier Ringen ist links angeschnitten und trägt „14 Rechenregeln / in vier Schichten“. Die sieben Gebiete liegen von innen nach außen auf Kreisbahnen (Abstand 78), der Planet ist 52 px groß, Name 19 px und „n tragende Ideen“ 15 px stehen auf der Bahn, mit einem Hof in Grundfarbe, damit keine Bahnlinie durch die Schrift läuft. Außen läuft eine gestrichelte Bahn mit der Kapsel „8 Arbeitsweisen“. Jedes Teil ist tippbar. Auf dem Handy bleibt die Fassung gestapelt.
- **Planeten mit Tiefe:** Jede Scheibe hat einen Lichtverlauf (Glanzpunkt oben links, Schatten unten rechts). Farbe und Zeichen bleiben wie in Runde 6.
- **Weltraum (dunkle Fassung):** Auf Ebene 0 und 1 liegt ein tieferes Schwarz (#070A10) mit leisem Sternenfeld (6 Punkte je 280 × 240 px, 30–55 % deckend). Der Kopf ist leicht durchscheinend. Auf Ebene 2 und 3 gibt es keine Sterne, wegen der Lesbarkeit langer Texte.
- **Übergang zwischen Ebenen:** 220 ms, Deckkraft 0 → 1. Beim Weg nach innen wächst die Seite von 96,5 % auf 100 %, beim Weg zurück schrumpft sie von 103,5 % auf 100 %. Kein Übergang innerhalb einer Ebene (Klasse wechseln, blättern) und keiner bei `prefers-reduced-motion: reduce`.
**Bewusst nicht**
- Keine kleine Zeichnung in der Liste. Bei 50 px Breite sind die Zeichnungen (320 Einheiten, mehrere Beschriftungen) nicht zu erkennen und würden jede Zeile höher machen. Erkennen lässt sich eine Regel an Nummer, Name und Merksatz. Die Zeichnung bleibt die Stufe „Beispiel“ der Regelseite.
- Kein „Hineinfliegen“ über mehrere Sekunden und kein Zoomen in den Planeten. [M] Das wirkt beim ersten Mal, stört aber beim zehnten Nachschlagen.
- Keine neuen Namen, keine Monde, keine Bahnen mit Bedeutung. Die Reihenfolge der Bahnen ist die der Daten (von innen nach außen).
**Gebiete und Arbeitsweisen:** Die Ideen-Listen hatten schon den Merksatz, neu sind dort das Band mit Ziffern (unter dem Satz am Handy, rechts ab 640 px) und die Legende über der Liste. Die Arbeitsweisen hatten ihren Satz schon (Feld `satz`); sie haben weiter kein Band, weil es keine Klassendaten gibt.
**Neue Maße bei 400 × 860 [G]:**

| Seite | Höhe |
|---|---|
| Ebene 0 | 982 px (unverändert) |
| Liste der 14 Regeln | 1 602 px = 1,86 Bildschirmhöhen (vorher 935 px); bei 360 px 1 823 px |
| Sonne-Seite ganz | 2 277 px (mit Schnitt-Bild 190 px) |
| Gebiet Zahlen, Liste | 650 px |
| Regel 6 | 1 252 px |

[M] Mit „höchstens gut zwei Bildschirmhöhen“ ist die Liste noch übersichtlich, weil die Schichten sie gliedern und der Schnitt oben zeigt, wohin man springt.
**Geprüft [G]:**
- Klick-Prüfung wie in Abschnitt 7: 357 von 357 Schritten bestanden, keine Skriptfehler.
- Kein Überlauf bei 360 und 400 px.
- Tippflächen sind mindestens 44 px groß, nachgemessen nach dem Übergang.
- Etiketten bis 11 px Größe: nur die Ziffern im Band.
- Angesehene Bilder (`entwurf7/bilder/`, 19 Stück): Ebene 0, Sonne und Regel 6 je bei 400 und 1280 px hell und dunkel; dazu Gebiet, Idee, Klassen (400 und 1280 px), Lehrer-Blatt und Regel 6 mit offenem Vergleich. Berichtigt dabei: Unterzeile der Sonne lag im Dunklen über dem Rand; die Sonne im Rechner-Bild war zu klein für ihre Schrift; Planeten-Namen wurden von Bahnlinien gekreuzt; die Legende brach in zwei Zeilen um.
**Nicht geprüft:**
- Übergang auf echten Handys (Ruckeln).
- Das Sternenfeld auf sehr hellen Bildschirmen.
- Ob Kind 1 und Kind 2 das Ringbild ohne Erklärung als „Schicht n von innen“ lesen.
