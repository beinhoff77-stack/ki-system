> **ABGELEHNT am 27.11. („passt mir noch gar nicht“) – Aufbau Liste/Detail falsch, Analyse zu dünn, Fehler erst nach Klick sichtbar, Optik zu grau/technisch und nicht im Stil der App; nicht weiterverwenden.** Nachfolger: `../entwurf3/umsetzung3.md`.

# Vorgabe WK, zweite Runde: „Was wackelt“ als Arbeitswerkzeug

Designer, 27.11.2026. Ersetzt `../entwurf1/` (abgelehnt). Entwurf: `index.html` (eine Datei, ohne Netz), Bilder: `bilder/`.
Übernommen aus `../entwurf1/umsetzung1.md`, ohne Wiederholung: **Regeln R0–R9** (Abschnitt 3), **Zustandsmodell** (Abschnitt 4: offen → besprochen → sitzt wieder, dazu später und wieder offen), **Datenbedarf** und **Schnittfolge Stufe 1/2** (Abschnitte 5 und 7). Offene Fragen 2–5 dort gelten weiter; Frage 1 (nur drei Punkte oben) entfällt – die Liste zeigt alle, die drei dringendsten sind markiert.
Adresse für feste Zustände: `#k=1|2&f=offen|besprochen|erledigt&z=g|w|a&g=hell|nacht&p=<Zeile>&auf=<Aufgabe>&einst=1&pop=info&leer=1`.
**[G]** gebaut und gemessen (Chrome 1440 × 900 und 400 × 860) · **[M]** Meinung.

## 1 Selbstkritik an Entwurf 1
1. **Erzählung statt Übersicht.** Kopfsatz in 22 px und Begründungssätze in jeder Karte. Man musste lesen, um die Lage zu sehen; eine Tabelle zeigt sie auf einen Blick.
2. **Zu viel Farbe und Fläche.** Rote, gelbe und blaue Plaketten, gefüllte rot/grüne Antwortkästen, gelbe Einstiegsfläche, farbige Kartenränder – fünf Signalfarben für eine Arbeitsliste.
3. **Kästen in Kästen, alles offen.** Karte → Abschnitt → Aufgabenkasten → Antwortkasten; ein offener Punkt war 3 400–4 200 px hoch. Die Rangfolge ging im Scrollen verloren.
4. **Bearbeitung versteckt.** „Besprochen“ stand am Ende eines langen Detailstapels und nur dort; der Verlauf hing als Anhang unter der Seite.
5. **Handy zuerst, obwohl am Rechner gearbeitet wird.** Am Rechner war die Liste eine 470-px-Spalte mit Karten; dazu Varianten-Schalter, Zettel-Knopf und Erklärblock in der Hauptansicht.

## 2 Aufbau [G]
Von oben: App-Kopf (‹ · Überblick | **Was wackelt n** | Lehrplan; Zahl = R9, schlicht, nicht rot) → **Zahlenleiste**, eine Zeile 15 px: „3 offen · 1 wieder offen · 0 besprochen · 2 Flüchtigkeit · 10 falsche von 16 Aufgaben · seit 18.11.“ (Zahlen fett, Rest grau), rechts zwei runde Knöpfe 30 px: **i** (Kurzlegende, 4 Sätze) und **⋯** (Gesprächszettel drucken; im Entwurf auch hell/dunkel, leer) → **Filter** als drei Segmente nebeneinander: Status *Offen n · Besprochen n · Erledigt n* · Zeitraum *Seit T.M. · 7 Tage · Alles* · Kind *Kind 1 · Kl. 5 · Kind 2 · Kl. 8* → **Liste**, rechts davon das **Detail**, wenn ein Punkt gewählt ist.

**Liste** (eine Zeile je Punkt, 48 px, Trennlinie 1 px, keine Kästen):
| Spalte | Inhalt | Breite (1440, ohne / mit Detail) |
|---|---|---|
| # | Rang 1, 2, 3 … (nur offene); links davor ein 3-px-Strich in der Akzentfarbe bei Rang 1–3 | 22 |
| Thema | „Terme umformen +1“, wenn eine Fehlvorstellung mehrere Themen trifft | 170 / – (mit Detail ausgeblendet) |
| Punkt | Lernkarte bzw. Kurzname des Fehlbilds; „↺“ davor = wieder offen; „später“ dahinter leise | Rest, mit Auslassungspunkten |
| Art | Punkt-Zeichen + Kürzel: ● Fehlvorst. · ◐ Lücke · ○ Flüchtig / Einmal | 56 / 84 |
| Fehler | „4 von 5“ = endgültig falsche von allen Antworten in den Lernkarten des Punkts im Zeitraum | 70 / 60 |
| Zuletzt | Datum des letzten Fehlers | 62 / 52 |
| Trend | „↑n“ = danach n-mal richtig ohne Tipp · „–“ = seitdem nicht richtig · bei besprochen „1/3“ = Nachüben | 48 / 40 |
| Status | Umschalter *Offen · Besprochen · Sitzt*, **ein Klick** ändert den Status (R0/R4 rechnen sofort neu, 5 s „Rückgängig“ unten) | 238 / 196 |

Reihenfolge: offene Punkte nach R5/R6 (Kopf „Punkt · nach Dringlichkeit ↓“), danach „später“, dann mit Abstand die Zeile „Nicht besprechen · einmal falsch“ und die Flüchtigkeiten in grauer Schrift ohne Status. Spaltenköpfe Thema, Fehler, Zuletzt sortieren um; „Punkt“ setzt auf Dringlichkeit zurück.
Filter **Besprochen**: dieselben Spalten, Trend = „n/3“. Filter **Erledigt** (= Verlauf): ✓ · Thema · Punkt · Art · Besprochen · Sitzt seit · Notiz · „Wieder öffnen“.
**Leer**: eine Zeile „**Nichts offen** seit dem Gespräch am 20.11. · 7 Aufgaben, 6 richtig · 1 Flüchtigkeit.“, darunter die Flüchtigkeiten wie sonst.

**Detail** (ab 900 px rechte Spalte 520 px, Trennlinie links, klebt, Höhe = Fenster − 214 px; die Liste bleibt stehen, gewählte Zeile grau hinterlegt; × oder Esc schließt):
Kopf: Thema › Lernkarte (13 px grau), Titel 17 px. Dann Abschnitte, getrennt nur durch 1-px-Linien, Überschriften 13 px grau:
1. **Befund** – ein Satz nach R8, darunter „Art · n von m falsch · zuletzt T.M.“.
2. **Falsche Aufgaben** – Tabelle *Aufgabe | Eingegeben | Richtig | Datum*, eine Zeile je Antwort, neueste zuerst; eingegeben in gedämpftem Rot (Textfarbe, keine Fläche), richtig in Textfarbe, Werte in Festbreite. Fehler-Detektiv: „Zeile 3 | Zeile 1“. Klick klappt auf: voller Text, Zeilen des Detektivs, Tabelle oder Zeichnung, „Erkannter Fehler · Anlauf · Tipp · später richtig?“, Lösungsweg.
3. **Regel** – ein Link „Regel 7 · Minus vor der Klammer ›“ (Merksatz als Tooltip).
4. **Gesprächseinstieg** – zugeklappt, eine Zeile.
5. **Nachüben** – 2–3 Zeilen *Aufgabe | Lösung*.
6. **Bearbeitung** – immer am unteren Rand der Detailspalte, auch beim Scrollen: Umschalter *Offen · Besprochen · Sitzt wieder*, Knopf „Später“, Zustandstext („Besprochen am 27.11. · Nachüben 0 von 3“, „Wieder offen · besprochen am 18.11.“), Notiz **einzeilig** (speichert beim Verlassen, Meldung „Notiz gespeichert“).

**Handy unter 900 px**: eine Spalte; Zeile = Rang · Titel + graue Zeile „Art · n von m falsch · Datum · Trend“ · rechts Statusknopf „offen ›“ (ein Tipp schaltet weiter: offen → besprochen → sitzt → offen, mit Rückgängig). Ein Tipp auf die Zeile öffnet das Detail als **eigene Ebene** über die ganze Fläche mit „‹ Liste“; Bearbeitung unten. Filter umbrechen in drei Zeilen.

## 3 Optik [G]
- Grautöne + eine Akzentfarbe: das Gelb der App (#FFD23F) **nur** als 3-px-Strich der drei dringendsten Zeilen. Gewählte Zustände: hellgraue Fläche + fette Schrift, kein Schwarz-auf-Weiß-Block. Einzige weitere Farbe: gedämpftes Rot für die eingegebene falsche Antwort (hell #A3392F, dunkel #E58A82).
- Schrift 15 px Fließtext, 13 px Nebentext, darüber nur 17 px (Titel im Detail). Keine Versalien, keine Schatten außer am Ausklapp-Feld von i/⋯, keine Emojis, keine Bilder außer den Aufgaben-Zeichnungen. Zahlen tabellarisch (`tabular-nums`), rechtsbündig.
- Hell: Grund #FAFAF8, Linien #E4E2DC/#EFEEEA, Text #14181F, grau #5E6672/#8C939D. Dunkel: Grund #0E1217, Linien #262E39/#1C232C, Text #E9ECF0.
- Gemessen: bei 1440 × 900 und 400 × 860 nichts breiter als das Fenster; am Rechner passt die ganze Lage (Kind 2: 3 offene + 2 Flüchtigkeiten) in die erste Bildschirmhöhe – Liste endet bei 490 px; 8 Zeilen enden rechnerisch bei rund 650 px. Das Detail scrollt in sich, die Seite nicht.

## 4 Abweichungen und Ergänzungen zu Runde 1
- **Status „Sitzt wieder“ auch von Hand** (Vorgabe des Koordinators). Server: `wackelt_status.status` braucht dafür den Wert `sitzt` (Stufe 2) – oder Stufe 1 bildet ihn auf `besprochen` + Anzeige ab, bis 3 eigene Lösungen da sind. [M] Vorschlag: von Hand erlauben, automatisch bleibt die Regel aus Runde 1.
- **„Fehler: n von m“**: m = alle Antworten in den Lernkarten des Punkts im Zeitraum – braucht die Versuchsfolge aus `schule_wackelt_analyse` (Stufe 1, umsetzung1 Abschnitt 5.2).
- Gesprächszettel nur noch im Menü ⋯ (Druck der Liste); kein eigener Bildschirm.
- Varianten A/B, Erklärblock und Lob-Satz im leeren Zustand entfallen.

## 5 Bilder (`bilder/`)
01/02 Übersicht 1440 hell/dunkel · 03 Detail offen (Fehler-Detektiv aufgeklappt) · 04 Detail dunkel mit Zeichnung · 05 Statuswechsel in der Zeile (Meldung „besprochen“ mit Rückgängig) · 06 Filter Besprochen mit Detail · 07/08 Filter Erledigt hell/dunkel · 09/10 leer hell/dunkel · 11 Kind 1, Detail mit Tabelle · 12 i-Legende · 13 Handy Liste · 14 Handy Detail · 15/16 Handy dunkel Liste/Detail.
