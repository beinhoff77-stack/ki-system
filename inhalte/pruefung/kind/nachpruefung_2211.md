# Nachprüfung Kinderansicht – App 0.87.0 (main 4e042d1), 22.11.2026

Geprüft gegen die Vorgaben `kind/abgelegt/umsetzung.md` (WD), `kind/faire-punkte/umsetzung.md` (FP) und LM-6 („Meine Route 5–10“). Testumgebung: Testsuite mit nachgebildetem Server, Testkind, erfundene Daten; Chrome, 360/400/820/1280, Tag und Nacht. Bilder: `kind/n087/`.

**Testsuite auf 4e042d1:** 163 von 163 grün (`PW_TEST_EXECUTABLE=/usr/bin/google-chrome node --test tests/lernen.test.cjs`).

## Ergebnis je Punkt
| Punkt | Stand | Bemerkung |
|---|---|---|
| Wiederholungs-Runde am Anfang (Ansage, Check-in, Eingecheckt, Extra) | ✓ mit S1, K1, K2 | Kopf „CHECK-IN · i VON n“, Herkunft „Etappe · aus Rom“, Koffer gold/rötlich, „+10 ★“ nur vom Server, „Kein Problem – …“, Pause und „Check-in fortsetzen“, „Eingecheckt! 2 von 3 richtig · +20 ★“, „Weiter nach Rom ›“, „Noch 3 Extra-Bordkarten?“. Startknopf **und** „EINSTEIGEN“ auf der Abflugtafel führen beide in den Check-in (nachgestellt). |
| Mischkarten | ✓ mit K3 | „BORDKARTE 1 · AUS DEINER REISE“, nach richtig „Das war: Große Zahlen lesen – New York“, „↻ Zählt als Wiederholung dieser Etappe“, Sterne aus dem Serverwert. |
| „abgelegt“ mit goldenem Stempel | ✓ | Etappe abgelegt (Blatt von unten, Siegel, +30, Gold-Leiste, „Weiter einchecken“), Flug abgelegt (ganzer Bildschirm, +100 / +30, Orts-Stempel golden, 360×640 ohne Scrollen), Reisepass „★ ABGELEGT“, „1 von 2 abgelegt“, „noch nichts abgelegt“, Satz „Gold heißt …“. Texte nach Entscheidung 0.86.3 („ABGELEGT“ statt „für immer“) – gewollt. |
| Landungs-Bonus 80/40/10 | ✓ | Kachel unter der Zahl, über dem Knopf; 80 gold, 40/10 mit Rand der Fassung; Sturmflug ohne Fehlerzahl; ohne `landung` keine Kachel; 360×640 ohne Scrollen (Test). |
| Hinweis bei 5 statt 10 Sternen | ✓ mit S2 | Text „Ganz ohne Tipp gibt es 10 ★.“ / „Gleich beim ersten Mal …“, einmal je Etappe und Tag, keine Tadel-Wörter, „+5“ gleiche Farbe. |
| Hinweis zur nachträglichen Gutschrift | ✓ | Karte „★ Geschenk für deine Landungen … +1 620 ★ Landungs-Bonus“, „Super ›“ schließt für immer, ohne Nachbuchung nichts. |
| „Meine Route 5–10“ | ✓ | Link auf der Abflugtafel, Kopf je Klasse, „▶ hier bist du – Etappe 3 von 7“, „Weiter lernen ›“, „Das brauchst du vorher“ / „Danach geht’s weiter mit“ in Kindersprache; ohne Matrix-Daten ehrlicher Hinweis „Die Route ist bald da.“ |

## Abweichungen

### Muss
– keine –

### Sollte
- **S1 – Ansage „Vorher kurz einchecken“ auf dem Handy nicht im Blick (nachgestellt).** Die Ansage steht unter Abflugtafel, Fortschritt, Stempel und „Abflug, wann es dir passt“. 400×860: Kasten beginnt bei 711 px, die Koffer-Leiste (785 px) liegt hinter dem festen Knopf „Weiter geht’s“ (786 px); 360×640: Kasten beginnt bei 734 px, ganz unter dem Bildschirm. Das Kind tippt „Weiter geht’s“, ohne zu wissen, dass erst 9 Bordkarten kommen. Vorgabe 1: „im Kasten ‚Jetzt dran‘ über dem Startknopf“. **Vorschlag:** Ansage direkt unter die Abflugtafel (vor Fortschritt/Stempel) oder als eine Zeile in den festen Knopfbereich: „Erst 9 Bordkarten Check-in · ca. 5 Min.“ über „Weiter geht’s“. Rechner 820/1280: sichtbar, ok. Bild `1-ansage-nacht-400.png`, `1b-ansage-gescrollt-400.png`.
- **S2 – Hinweis bei 5 Sternen eingequetscht (nachgestellt, 400 Tag und Nacht).** Der Satz steht als schmale Mittelspalte zwischen „✓ AN BORD · +5 STERNE“ und „Weg zur Lösung.“ und bricht dreizeilig. Vorgabe 2: „Hinweis **darunter** (klein, grau)“. **Vorschlag:** eigene Zeile unter der Rückmeldung, volle Breite. Bild `10-fuenf-sterne-nacht-400.png`.

### Kann
- **K1** – Ansage-Zeile ohne „· je richtig ★ 5“ (Vorgabe 1). Vertretbar, weil die Sterne vom Server kommen (heute 10); dann aber gar keine Zahl – so umgesetzt. Nur festhalten.
- **K2** – Tag-Gestaltung: Link „Pause – später weiter einchecken“ sehr blass auf Sand (Bild `3-checkin-richtig-tag-400.png`). Kontrast prüfen.
- **K3** – Lange Zahlwörter in Auswahl-Antworten brechen ohne Trennstrich („…einundfünf|zig“, Bild `8-misch-frage-nacht-400.png`). Betrifft alle Auswahl-Aufgaben, nicht nur Mischkarten; `hyphens:auto` mit `lang="de"` würde reichen. (Das „…“ in Antwort 1 stammt aus den Testdaten, kein Fehler.)

## Nicht geprüft
- Echte Server-Antworten (nur nachgebildet), echte Kinderdaten (bewusst nicht), Bewegung im Ablauf (nur Endzustände und „weniger Bewegung“ per Test).
