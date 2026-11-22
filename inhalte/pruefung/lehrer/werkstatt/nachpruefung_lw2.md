# Prüfung LW-2 „Unser Lehrplan“ Teil 2 – App 0.89.0 (Zweig lernen-app, 00cd00e; LW-2-Stand e20266e ff.), 22.11.2026

Geprüft gegen die Vorgabe `lehrer/werkstatt/umsetzung.md` (Abschnitte 4, 4a, 6, 7, 8, 12, 12.7) und die Nachprüfung `nachpruefung_lw1.md`. Grundlage Meldung `inhalte/postfach/bau-motivation.md` „FERTIG: LW-2“. **Tablet 820 px und Handy 400 px**, Testkind und erfundene Daten (Testsuite mit nachgebildetem Server, Maus statt Finger). Bilder: `lw2/` (eigene) und `docs/previews/la/lw2-400.png`, `lw2-820.png` (Bau-Chat). Hinweis: Den Code fand ich unter `lernen.js` (Wurzel), nicht `docs/lernen.js`.

**Testsuite:** 148 von 148 grün (`PW_TEST_EXECUTABLE=/usr/bin/google-chrome node --test tests/lernen.test.cjs`), davon 7 neue LW-2-Tests.

## Erfüllt (nachgestellt)
- **LW-1-Nacharbeit:** S1 Handy – erste Karte bei **392 px** (vorher 795), eine Leiste `[Fahrplan · 8 | Alle Themen] [Filter ▾] [ⓘ] [↶]`, Filter als Blatt von unten, „Filter · 1“ bei aktivem Filter, Legende hinter ⓘ; K3 Tablet 820 – Leiste einzeilig, erste Karte bei 366 px. S2 – „8 Plätze · 12 Themen“, Platz „3a–3d“, keine Nummer doppelt. K1 – Etappen 1–2 gelandet, 3 gerade dran. K2 – Kopf und Klassen aus derselben Quelle („Klasse 8“, Klassen 8–10).
- **Ziehen (Tablet, Fahrplan-Schublade offen):** Karte → Fahrplan mit blauer Linie und mitlaufendem Schild, „‹Thema› auf Platz 2 eingeplant · ↶ Rückgängig“; Fahrplan → Matrix: Matrix rot gestrichelt, „… aus dem Plan genommen · ↶ Rückgängig“.
- **Warnungen 4a:** alle drei Fälle mit Reparieren-Knopf, ✕, Rückgängig; dauerhafter Hinweis im Fahrplan; „aus dem Plan … ⚠ … baut darauf auf“.
- **Alle einplanen:** „44 Themen (bis Kl. 10) noch nicht im Plan · Alle 44 einplanen (nach Klasse und Lehrplan)“ oben im Fahrplan, ein Schritt.
- **12.7 Teile:** Karte „Terme umformen“ + Marke „2/3“, Untertitel, Familie untereinander mit Klammer, Darüberfahren hebt die anderen Teile hervor; Zusatz mit Marke „Zusatz“, nicht in „Noch nicht im Plan“/„Alle einplanen“; Detail „Terme umformen – Teil 2 von 3“, Untertitel, „TEILE DIESES THEMAS“, „Alle Teile einplanen“ (Zusatz nur mit Haken); Warnung „Teil 1 fehlt“.

## Abweichungen

### Muss
- **M1 – Handy: Reihenfolge-Warnung liegt hinter dem Detail-Blatt (nachgestellt, 400 × 860).** Auf dem Handy plant man nur über das Detail-Blatt. Nach „In den Plan: als Nächstes“ erscheint die Warnung (Fall 3) – aber **unter** dem Blatt: `.lw-toast` z-index 60, `.lw-drawer` z-index 70; an der Mitte der Warnung liegt das Blatt. Sichtbar wird sie erst nach dem Schließen. Damit sieht der Lehrer auf dem Handy die Warnung und den Reparieren-Knopf nicht in dem Moment, in dem er handelt. **Stelle:** Stilregel `.lw-toast` / `.lw-drawer` (style.css). **Änderung:** Einblendung über dem Blatt (z-index > Blatt) und auf dem Handy oberhalb des Blatt-Randes bzw. im Blatt oben angedockt; dasselbe für die normale Meldung „… eingeplant · ↶ Rückgängig“. Bild `lw2/400-7-warnung.png` (Warnung unsichtbar), `lw2/400-7b-warnung-nach-schliessen.png`.

### Soll
- **S1 – Warnungstext zu lang, besonders bei Teilen (nachgestellt, 400 und 820).** Der Text nennt Themen mit vollem Titel **samt Untertitel** – zweimal plus im Knopf: „„Terme umformen – Teil 2 von 3 · Summe mal Summe, Ausklammern, binomische Formeln“ baut auf „Terme umformen – Teil 1 von 3 · zusammenfassen und ausmultiplizieren“ auf …“. Höhe der Einblendung: **281 px** auf dem Handy (ein Drittel des Bildschirms), 221 px auf dem Tablet; Vorspann „… als Nächstes eingeplant ·“ wiederholt den Titel ein drittes Mal. **Stelle:** Text der Warnung/Meldung (4a) in `lernen.js`. **Änderung:** in Einblendungen und Knöpfen nur der Kurzname ohne Untertitel („Terme umformen – Teil 2 von 3“, Vorgabe 12.7: Untertitel nur als zweite Zeile in Karte/Detail); bei Warnung den Vorspann weglassen und als **eine** Aussage formulieren: „⚠ Teil 2 von 3 braucht Teil 1 – nicht gelernt, nicht im Plan“ (gleiches Thema) bzw. „⚠ „B“ braucht „A“ – …“; Knopf „Teil 1 davor einplanen“. Ziel: höchstens 3 Zeilen auf 400 px.
- **S2 – Fall-2-Knopf: Wortlaut bestätigt.** Die Abweichung „„B“ dahinter setzen“ (statt „hinter „B“ setzen“) ist **richtig** – der Lehrer hat die Voraussetzung gerade bewusst nach hinten geschoben; B dahinter zu setzen erhält diese Absicht. Bitte so lassen und in der Vorgabe 4a gilt ab jetzt dieser Wortlaut (wird dort nachgezogen). Kein Bau nötig.

### Kann
- **K1 – Platz-Buchstaben in der Matrix nicht in Reihenfolge (400).** In der Zelle Algebra Kl. 8 stehen 3a, 3b, **3d, 3c** – sortiert nach Lehrplan, nicht nach Platz. **Änderung:** innerhalb eines Orts nach Buchstabe sortieren oder die Buchstaben nach der Anzeige-Reihenfolge vergeben. Bild `lw2/400-1-start.png`.
- **K2 – „Hier loslassen = aus dem Plan nehmen“ beim Zurückziehen nicht zu sehen (820).** Matrix wird rot gestrichelt, aber das Schild unten wird von der vorherigen Meldung („… auf Platz 2 eingeplant · ↶ Rückgängig“) verdeckt. **Änderung:** laufende Meldung beim Ziehen ausblenden. Bild `lw2/820-9-zurueck.png`.
- **K3 – Detail: „TEILE DIESES THEMAS“ steht unter der Etappenliste** (Handy: erst nach Scrollen). Vorgabe 12.7: „ganz oben unter dem Stand“. **Änderung:** Abschnitt direkt unter die Stand-Zeile, vor die Etappen. Bild `lw2/400-6-teile-detail.png`.
- **K4 – Offen laut Bau-Meldung (kein Fehler):** „+ Zusatz“-Bogen am Ring, Hinweis „Stempel nachgetragen“, Kinderseite 12.5 – gehören zu LK-App.

## Nicht geprüft
Rechner 1280 (nur Testsuite), Ziehen mit dem Finger auf echten Geräten, echter Server, LW-3.

FERTIG: Prüfung LW-2 (0.89.0) – 1 Muss (Warnung auf dem Handy hinter dem Detail-Blatt), 2 Soll (Warnungstext kürzen; Fall-2-Wortlaut bestätigt), 4 Kann.
