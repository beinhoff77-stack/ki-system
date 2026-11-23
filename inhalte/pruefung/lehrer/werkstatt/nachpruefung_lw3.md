# Prüfung LW-3 / LW-3b „Unser Lehrplan“ – App 0.90.1 (Zweig lernen-app, cfaf70a), 23.11.2026

Geprüft gegen die Vorgabe `lehrer/werkstatt/umsetzung.md` (1a und übrige) und `nachpruefung_lw2.md`; Grundlage Meldungen „FERTIG: LW-3 (0.90.0)“, „FERTIG: LW-3b (0.90.1)“, „FERTIG: LW-2b (0.89.1)“ und AUFTRAEGE.md „Nachtrag LW-3: Kopf der Kind-Seite schlank, Matrix groß“. Bildschirme **1280 × 800, 820 × 900, 400 × 860**; Testkind und erfundene Daten (Testsuite mit nachgebildetem Server). Bilder: `lw3/` (eigene), `docs/previews/la/lw3-*.png`, `lw3b-*.png`.

**Testsuite:** 159 von 159 grün (`PW_TEST_EXECUTABLE=/usr/bin/google-chrome node --test tests/lernen.test.cjs`), darunter alle LW-1-, LW-2-, LW-2b-, LW-3- und LW-3b-Tests.

## Gemessen
| | Kopf | Leiste | Matrix sichtbar | erste Karte |
|---|---|---|---|---|
| 1280 × 800 | 53 px | 82 px (**2 Zeilen**) | 603 px | 219 px |
| 820 × 900 | 103 px (2 Zeilen) | 42 px (1 Zeile) | 693 px | 229 px |
| 400 × 860 | 145 px (4 Zeilen inkl. App-Leiste) | 44 px | – | 314 px |
Hinweis zu Frage 2: Bei 1280 × 800 sind es heute **zwei** Leisten-Zeilen, nicht drei: Zeile 1 „Lehrplan von · Zeigen · Klassen“, Zeile 2 „Einstieg · Suchen · Auswählen · Legende · Gespeichert · ↶“. Eine dritte entsteht, sobald der ⓘ-Hinweis zu „Lehrplan von“ aufgeklappt wird (Leiste dann 157 px) oder die Zähler länger werden.

## Erfüllt (nachgestellt)
1. **Kopf:** ‹ Zurück · Kinder-Umschalter `‹ A Kind A · Gymnasium · Kl. 8 | B Kind B | T Testkind ›` · Reiter Überblick | Was wackelt (rote 2) | Lehrplan · rechts „Lernen starten ›“, ⚙, ⓘ. Reiter bleibt beim Wechsel; Alt+←/→ (Test).
2. **Lehrplan:** Matrix und Fahrplan bis zum unteren Rand, 603 px bei 1280 × 800.
3. **„Lehrplan von:“** mit ⓘ, Standard = Schulart des Kindes.
4. **Überblick:** Gerade dran → „Im Lehrplan öffnen“ (öffnet das Detail), Als Nächstes (Plätze 2–4 wie im Fahrplan) → „Fahrplan ändern“, Zu besprechen → „Zu Was wackelt“, Diese Woche, Stand mit Ringen (gleiche Zahl wie im Lehrplan).
5. **Was wackelt:** Zu besprechen · 2 / Beobachten · 1 / Besprochen · 1, Knöpfe „✓ Besprochen“, „Beobachten“/„Zu besprechen“, „Im Lehrplan“, „Bordkarte und Antwort ▸“, rote Zahl am Reiter sinkt sofort, Meldung „„Natürliche Zahlen“: besprochen · ↶ Rückgängig“.
6. **LW-1/LW-2 nichts verloren:** Ziehen in beide Richtungen, Warnungen (jetzt über dem Blatt, kurze Namen), Auswählen + Sammelaktion, Alle einplanen, Teile – Tests grün; LW-2-Muss M1 und Soll S1 erledigt, K1–K3 erledigt.

## Abweichungen

### Muss
– keine –

### Soll
- **S1 – Leiste am Rechner sicher auf zwei Zeilen (Frage 2). Empfehlung: Ja, Farb-Legende hinter ⓘ – wie auf Tablet und Handy.** Begründung: Die Legende ist Nachschlagewissen (einmal gelernt, dann nicht mehr nötig), braucht aber heute die halbe zweite Zeile; einheitlich auf allen Geräten ist leichter zu erklären; die Farben stehen zusätzlich auf jeder Karte als Text („Platz 3a“, „↻ Wdh 2/5“, „✓ fertig“). **Stelle:** `zeichneLeiste` (Rechner-Zweig) in `lernen.js`. **Änderung – feste Aufteilung:**
  - Zeile 1: `LEHRPLAN VON: [Gymnasium|Realschule|IB MYP] ⓘ · ZEIGEN [Alle | Noch nicht im Plan · n | Im Plan · n] · KLASSEN [5…10]`
  - Zeile 2: `[Bereit für Klasse … ▾] [Suchen] [Auswählen] · [ⓘ Farben] · rechts [↶ Rückgängig]`
  - „Gespeichert“/„Alles gespeichert“ nur zeigen, während gespeichert wird oder bei Fehler (sonst still); der Text kostet heute ~90 px.
  - ⓘ-Hinweis zu „Lehrplan von“ (und die Legende) als **schwebendes Feld** unter dem Knopf, nicht als eingeschobene Zeile – sonst springt die Matrix um 75 px nach unten (gemessen: Leiste 82 → 157 px). Bild `lw3/1280-lehrplan-von-info.png`.
  - Test: Leiste ≤ 90 px bei 1280 × 800 auch mit „Noch nicht im Plan · 145“ und offenem ⓘ.
- **S2 – Überblick doppelt sich (Frage 4).** Unter den fünf neuen Karten stehen die alten fünf; vier davon sagen dasselbe anders – teils mit **widersprüchlichem** Inhalt (nachgestellt, 1280 und 400):
  | alte Karte | doppelt zu | Befund | Änderung |
  |---|---|---|---|
  | „Lernt es?“ | „Diese Woche“ | gleiche Zahlen (0 Lerntage, 30 Bordkarten) | **weg**; „zuletzt 14.11.“ und die rot/grün-Färbung in „Diese Woche“ übernehmen |
  | „Wo hakt es?“ | „Zu besprechen“ | andere Quelle: zeigt „Runden · Rom“, „Zu besprechen“ zeigt „Natürliche Zahlen · Teilbarkeit und Primzahlen“ | **weg** |
  | „Wo steht es?“ | „Stand Kl. n“ | Einstufung je Schulart („Kl. 8 –“) | **weg**; Einstufung als eine Zeile in „Stand“ („Einstufung: Gym Kl. 8 · RS Kl. 8 · MYP 3“) |
  | „Was kommt?“ | „Gerade dran“ + „Als Nächstes“ | **Widerspruch:** „Jetzt: Flug Rom · Natürliche Zahlen (2/4 Etappen)“ gegen „Gerade dran: Lineare Ungleichungen · Etappe 3 von 7“ (alter Orts-Stand gegen Fahrplan) | **weg** |
  | „Zuletzt geschafft“ | – | nicht doppelt | **bleibt**, als kleine Karte neben „Diese Woche“ (dort ist heute rechts leer) |
  Ergebnis: eine Seite ohne Scrollen am Rechner. Stelle: Überblick-Aufbau (`lw-ue` und die alten Karten darunter) in `lernen.js`.
  Ebenso auf „Was wackelt“: die Zeile „Diese Woche: 30 Bordkarten … · 0 Lerntage“ über der Liste **weg** (steht im Überblick) und die Überschrift „Was wackelt?“ (doppelt zum Reiter) weg.
- **S3 – Matrix startet halb verdeckt (nachgestellt, 1280 und 820).** Die Matrix rollt beim Öffnen zur Klasse des Kindes, aber 30 px zu weit: Der Klassen-Kopf „Kl. 8“ und die oberste Kartenreihe liegen unter der klebenden Spaltenzeile (abgeschnittenes „Wdh 2/5“, halbes „KL. 8“). **Stelle:** Einrollen zur Kind-Klasse. **Änderung:** Höhe der Spaltenzeile abziehen (z. B. `scroll-margin-top` = Höhe der Spaltenköpfe + 8 px). Bild `lw3/1280-lehrplan.png`.
- **S4 – Handy-Kopf vierzeilig, Reihenfolge verdreht (400).** Zeile 1 App-Leiste, Zeile 2 Kinder, **Zeile 3 Zurück** + „Lernen starten ›“ + ⚙ ⓘ 🔔, Zeile 4 Reiter – „Zurück“ steht unter dem Kinder-Umschalter. **Änderung:** eine Zeile `‹ · [A Kind A] [B] [T] · ⋯` (⋯ = Lernen starten, Einstellen, So funktioniert’s), darunter die Reiter. Spart ~45 px; erste Karte dann ~270 px. Bild `lw3/400-lehrplan.png`.

### Kann
- **K1 – „Lehrplan von:“ (Frage 3):** richtig platziert (vorne, links von „Zeigen“), Wort verständlich. Hinweistext klarer mit Beispiel: „Nach welchem Lehrplan die Themen den Klassen zugeordnet werden – z. B. steht ‚Satz des Pythagoras‘ im Gymnasium in Kl. 8, in der Realschule in Kl. 9. Gezeigt werden immer alle Themen.“
- **K2 – „Einstieg prüfen …“ umbenennen in „Bereit für Klasse …?“** – der heutige Name verrät nicht, dass er die Lücken bis zu einer Klasse zeigt (Rückfrage Sebastian 23.11.).
- **K3 – Testkind im Kinder-Umschalter** (Annahme des Bau-Chats): für den Alltag ausblenden oder ans Ende mit Marke „Test“ – Entscheidung Sebastian.
- **K4 – Handy „Was wackelt“:** Knöpfe brechen in zwei Zeilen („Im Lehrplan“ allein). Kürzer: „✓ Besprochen“, „Beobachten“, „→ Lehrplan“.
- **K5 – Alte Tabelle „Je Etappe: richtig / falsch …“ und „Alle Etappen mit Stand“** unter der Arbeitsliste: zugeklappt ok; nach Einführung prüfen, ob noch gebraucht.

## Nicht geprüft
Echter Server (`schule_wackelt_lesen`/`_setzen`, Edge Function 0.9.2), echte Geräte, Finger-Ziehen.

FERTIG: Prüfung LW-3 (0.90.1) – 0 Muss, 4 Soll (Leiste 2 Zeilen mit Legende hinter ⓘ, Überblick ohne Doppelungen, Matrix-Einrollen, Handy-Kopf), 5 Kann.
