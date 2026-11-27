# Umsetzung Lehrplan-Matrix (LM) – Entwurf, vom Nutzer gewünscht

Stand 21.11.2026. Vorlage: `entwurf/lehrplan-matrix.html` (läuft ohne Server, mit erfundenem Lernstand „Kind A“/„Kind B“), live als Artifact „Mathe 5–10 – was gelernt wird“.
Nur Entwurf und Beschreibung. Der Bau-Chat baut, Merge nach main erst nach „Live“ des Nutzers.

## Ziel
Eltern/Lehrer sehen auf einer Seite, was in Mathe von Klasse 5 bis 10 gelernt wird, wie die Themen aufeinander aufbauen und wo jedes Kind steht.

## LM-1 Matrix (ersetzt die Seite „Lehrplan“ unter Nachschlagen)
- Zeilen Klasse 5–10 (Klassenfarben wie LA-8), Spalten die Themengebiete inkl. „Entdecker-Inseln“. Schalter „Klassen als Zeilen / als Spalten“ (Standard: Zeilen).
- **Alle Themen der Themenliste** stehen in der Matrix, nichts wird ausgeblendet. „Einordnen nach Gymnasium / Realschule“ bestimmt nur die Zeile. Fehlt die Schulart: Klasse der anderen Schulart, sonst IB-MYP-Jahr + 5 (Annahme MYP 1 ≈ Kl. 6). Solche Themen gestrichelt.
- An jedem Thema klein: „Gym 8 · RS 7 · IB 4“ (gewählte Schulart dunkel, fehlende durchgestrichen bzw. orange, wenn es die gewählte ist).
- Reihenfolge in der Zelle: Lehrplan-Reihenfolge der Schulart.
- Kopf je Zeile: „n Themen · m Gym-Pflicht“.
- Suche, Schalter „Kurzbeschreibung“ (Umfang unter dem Titel).
- Handy (< 760 px): Liste je Klasse, gruppiert nach Themengebiet; Detail öffnet sich direkt unter dem angetippten Thema.

## LM-2 Detail eines Themas (rechts, auf Handy darunter)
Titel, Themengebiet, Klassen je Schulart, Lernbereich; „Was gefordert ist“ (umfang); „Braucht vorher“ (direkte Voraussetzungen aus `schule.voraussetzung` mit Begründung und Klasse, „empfohlen“ kennzeichnen); „Weiter zurück auf dem Weg“ (alle indirekten Voraussetzungen); „Darauf baut auf“; „Das muss sitzen“ (merke); Beispielaufgabe (erste Aufgabe < 160 Zeichen); „Schritte in der App“ (Etappen); Lehrplan-Wortlaut; ‹ › blättern. Ohne Voraussetzung: „Keine Voraussetzung hinterlegt“ (nicht „eigenständig“, solange die Tabelle lückenhaft ist).

## LM-3 Verbindungen
Thema antippen: direkte Voraussetzungen gelb mit Linie, weiter zurück hellgelb, darauf aufbauend blau mit Linie, alles andere blass; „empfohlen“ gestrichelte Linie. „→ n“ an Themen, die Grundlage für ≥ 2 Themen sind. Linien hinter den Themen-Karten, auf Handy keine Linien (nur Farben).

## LM-4 Lernstand je Kind (neu, Wunsch des Nutzers)
- Leiste „Lernstand: Aus · ‹Kind 1› · ‹Kind 2› · Beide vergleichen“ (echte Namen aus der App, je Kind die eigene Schulart → „Einordnen nach“ springt darauf).
- Ein Kind: Hintergrund je Stufe wie im Plan (LB): ◉ kann (grün), ↻ Wiederholung (gelb, „Wdh n von 5“), ▶ gerade dran (blau, Rahmen, „Etappe x von y · hier ist ‹Name›“), ○ kommt noch, + nicht im Plan (gestrichelt, blass). Beim Einschalten zum ▶-Thema scrollen.
- Beide vergleichen: je Thema eine Zeile „A/B“ mit zwei Punkten in der Stufenfarbe (kommt noch/nicht im Plan: weiß mit Rand).
- Kopf je Klasse: Balken pro Kind (◉ grün, ↻ gelb, ▶ blau) über die Pflichtthemen der Klasse.
- Detail: „Lernstand“ je Kind mit Stufe, nächste Wiederholung, Links „Im Plan öffnen ›“ und „Fehler besprechen ›“ (nur wenn Fehler offen).
- Daten: Stufe je Thema liefert `api.schule_lehrplan_uebersicht` (Felder stufe, etappen, begonnen, wdh_nr, naechste_in). Annahme, nicht geprüft: Für „Etappe x von y“ und beide Kinder in einem Aufruf ggf. kleine Erweiterung – im Bau prüfen, sonst nach W1–W7.
- Nur für eingeloggte Eltern/Lehrer; keine Kinderdaten in Dateien oder Tests (Tests mit Testkind und erfundenen Daten).

## Daten
`inhalte/themenliste.json` (Titel, Gebiet, Klasse/Reihenfolge/Lernbereich je Schulart, umfang, lehrplan_*), Themen-Dateien (merke, etappen, aufgaben), `schule.voraussetzung`. Prüfauftrag an den Lehrplan-Chat (Zuordnungslücken, Voraussetzungen vervollständigen) läuft getrennt; die Ansicht muss mit dem heutigen Stand funktionieren.

## Prüfen
400, 820, 1280 px; keine Wörter mitten im Wort umbrochen (Trennstrich erlaubt); Schalter-Zustände; Lernstand-Modi; Linien liegen hinter den Karten.

## LM-5 Einbau Lehrer/Eltern (Nutzer: „bei den Kindern und beim Lehrer einbauen“)
- **Nachschlagen → „Lehrplan“** öffnet die Matrix (LM-1 bis LM-4), Lernstand-Leiste mit allen Kindern und „Beide vergleichen“.
- **Seite des Kindes, Reiter „Plan“**: oben rechts Link „Als Matrix ansehen ›“. Er öffnet die Matrix mit diesem Kind vorgewählt und dessen Schulart. Kein fünfter Reiter (LA-1: vier Reiter + ⚙).
- **Im Detail eines Themas** für Lehrer/Eltern zusätzlich die Stufen-Knöpfe aus LB Teil 8 (Variante A): „Lernen · Kann er – wiederholen · Kann er komplett“ und rechts „Aus dem Plan nehmen“ bzw. „In den Plan nehmen“. Gleiche Server-Aufrufe und Rückgängig wie im Plan, nur wenn genau ein Kind gewählt ist. Damit kann der Lehrer direkt aus der Übersicht planen.
- „Im Plan öffnen ›“ springt in den Reiter „Plan“ mit diesem Thema aufgeklappt.

## LM-6 Einbau Kinderseite („Meine Route 5–10“)
Gleiche Matrix, für das Kind vereinfacht:
- **Zugang:** auf der Abflugtafel ein Textlink „Meine Route 5–10 ›“ (kein großer Knopf, der große Knopf bleibt „Weiter“).
- **Nur das eigene Kind:** Lernstand immer an, Schulart fest. Keine Leiste für Kinder, kein Vergleich mit Geschwistern, keine Schulart-Kennzeichen („Gym 8 · RS 7“), keine Pflicht-Zählung, kein Lehrplan-Wortlaut, keine Lernbereiche.
- **Reisewörter** (Test der Reisewörter gilt): Flug statt Thema, Kontinent statt Themengebiet, Etappe. Überschrift „Deine Route durch die Mathe-Welt“, Spalten = Kontinente, Zeilen = Klasse 5–10.
- **Je Flug die Stufe** in Kinder-Sprache: ◉ „kannst du“, ↻ „kommt zur Wiederholung“, ▶ „hier bist du – Etappe x von y“, ○ „kommt noch“; nicht im Plan: blass, ohne Text. Beim Öffnen zum ▶-Flug scrollen.
- **Kopf je Klasse:** ein Balken und „Du kannst schon n von m Flügen“.
- **Detail eines Flugs:** „Was du hier lernst“ (umfang), „Das muss sitzen“ (merke), „Das brauchst du vorher“ (mit eigener Stufe ◉/↻/○), „Danach geht’s weiter mit“, Etappen-Liste mit ✓ für gelandete Etappen. Kein Ändern des Plans. Ist es der ▶-Flug: großer Knopf „Weiter lernen ›“ (öffnet die nächste Etappe). Sonst kein Lern-Knopf (Reihenfolge bestimmt der Plan).
- **Verbindungen:** wie LM-3, aber Wörter „brauchst du vorher“ / „baut darauf auf“.
- **Handy/Tablet zuerst:** Liste je Klasse wie LM-1 Handy. Keine Kinderdaten in Tests.

## Reihenfolge
LM-1 bis LM-4 und LM-5 zusammen (Lehrer/Eltern), danach LM-6 (Kinderseite) als eigener Schritt, weil dort Reisewörter und Stufen-Texte für Kinder dazukommen.
