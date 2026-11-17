# Nachprüfung lernen-app 0.74.5 (2026-11-17)

Stand geprüft: `origin/main` = `origin/lernen-app` = `e842c07`, App 0.74.5. Datenbank-Migrationen bis `w150_e3_auftraege_bezug` eingespielt.
Annahme: GitHub Pages zeigt `main` – die Live-Seite selbst konnte ich von hier nicht abrufen (Netz gesperrt). Geprüft mit Playwright gegen den Stand von `main` und Testdaten (Mock), nicht mit echten Kinderdaten.

Skripte: `nach-0745/kind-rundgang.test.cjs`, `nach-0745/eltern-rundgang.test.cjs`, `nach/nachstellen-v074.test.cjs`, `rueckmeldung/nachstellen.test.cjs`. Bilder: `nach-0745/bilder/`.

## 1. Umgesetzt (nachgestellt)

| Punkt | Ergebnis |
|---|---|
| A1–A12 Erklärungen | umgesetzt (0.74.0), A2-Nachtrag „Kurz gesagt“ ein Satz (0.74.4) |
| R1–R3 Rückmeldung/zweiter Versuch, 6-Punkte-Regel, Wiederholung | umgesetzt |
| N6 Test-Kopf | „Rom · Natürliche Zahlen“ |
| N7 Testende | „Erst üben: … ›“, „Verbessern ›“, ✓-Marker, „Zum Flug \| Zur Abflugtafel“ |
| N5 Detektiv-Hinweise | wie beauftragt; bei Auswahlaufgaben ohne Fehlermuster weiter allgemeiner Hinweis (siehe M6) |
| K1/K2 Menü + Mein Weg | Menü 4 Einträge (Abflugtafel · Mein Weg · Merkheft · Reisepass), Mein Weg mit Reitern Stand · Kontinente · Karte, Merkheft nur Geschafftes |
| D2 Klassen | Kind A Karte „Klasse 5: 1 von 10 Orten“, Alexandria/Timbuktu stehen auf Gym 5 |
| E-1 Info-Seite | „So funktioniert’s“: 4 erste Schritte + 7 Fragen, von jeder Elternseite oben rechts erreichbar |
| E-1 Flugplan speichert sofort | „Gespeichert“ nach Ziehen, kein Speichern-Knopf mehr, „↶ Rückgängig“ |
| E-2 Startseite je Kind | Karte je Kind mit GYM/RS/IB-Zeilen, „Jetzt: …“, Lernstand · Flugplan · Lernreise ansehen |
| E-2 Flugplan zwei Spalten | links Plan (Griff ⠿, ↑ ↓), rechts Lehrplan nach Schulart/Klasse mit Suche und „+“; auf dem Rechner nebeneinander |
| E-2 Flüge abwählbar | Ort aufklappen → Häkchen je Flug; Kind sieht abgewählte Flüge nicht |
| E-3 Ändern lassen + Meine Aufträge | „✎ Ändern lassen“ im Plan, Startseite zeigt „Neue Antworten auf eure Aufträge“, Liste unter `#/lernauftraege` |

Noch offen laut Plan (kein Fehler): K3 Linienplan/Stand über drei Schularten im Kinder-Reiter „Stand“, K4/K5, E-4.

## 2. Neue Befunde

Fakten = im Test nachgestellt. Vermutung = so gekennzeichnet.

**M1 „Gerade dran“ widerspricht sich (Fakt, Kind A).** Mein Weg · Stand zeigt oben „2 gelandet · 1 unterwegs · 11 warten“, direkt darunter die Kachel „12 gerade dran“ und eine Liste „GERADE DRAN“ mit 12 Orten, darunter Klasse 6 und Cusco Kl. 8 mit „Etappe 1 von 7“ (nicht begonnen). „Gerade dran“ zählt alles Offene im Plan (`dran` in `lernen.js` ~Z.1711).
Vorschlag: „Gerade dran“ = nur der aktuelle Ort (+ höchstens der nächste); Rest unter „Kommt noch“. Kacheln dann z. B. „1 kann ich · 1 gerade dran · 12 kommen noch“.

**M2 Klasse wird noch mit „Speichern“ gesetzt (Fakt).** Im Flugplan steht „Jede Änderung wird sofort gespeichert“, das Feld „Klasse“ darunter hat aber einen eigenen Knopf „Speichern“ (Z.2285). Auf einer Seite zwei Regeln.
Vorschlag: Klasse als Auswahl, speichert sofort wie der Plan.

**M3 Aufgeklappter Ort: Häkchen steht vom Flug getrennt (Fakt, Tablet 820 px).** Beim Aufklappen von Rom steht jedes Häkchen in einer eigenen Zeile über dem Flugnamen; 5 Flüge brauchen ~450 px. Man sieht nicht sicher, welches Häkchen zu welchem Flug gehört.
Vorschlag: Häkchen links in derselben Zeile wie der Flugname, eine Zeile je Flug.

**M4 Klasse-8-Ort im Klasse-5-Plan (Fakt in den Testdaten, Ursache Vermutung).** Kind A (Gym 5) hat „Cusco – Körper und Netze · Gym 8“ an Platz 8 und „Adelaide · Gym 6“ im Plan; im Kinder-Weg stehen sie unter „Gerade dran“. Vermutung: Folge der D2-Umsortierung – die Orte blieben im Plan, obwohl ihre Flüge jetzt höheren Klassen zugeordnet sind.
Vorschlag: Im Flugplan Orte, deren Flüge alle über der Klasse des Kindes liegen, sichtbar markieren („Klasse 8 – über seiner Klasse“) und beim Kind unter „Später“ einsortieren, solange Eltern sie nicht bewusst vorziehen. Mit echten Daten prüfen.

**M5 Abflugtafel: Zielangabe zu groß (Fakt).** „Noch 29 Etappen bis zum Stempel von Rom (5 Flüge)“. Bei 9–14 Bordkarten je Etappe (Schätzung aus der 6-Punkte-Regel) sind das mehrere Wochen – für ein Kind kein greifbares Ziel.
Vorschlag: nächstes Zwischenziel zeigen: „Noch 3 Etappen bis ›Ganze Zahlen‹ gelandet“; Ort-Stempel nur im Reisepass.

**M6 Detektiv-Hinweis bei Auswahlaufgaben (Fakt, aus N5).** Ohne hinterlegtes Fehlermuster erscheint ein allgemeiner Hinweis, der nicht zur gewählten Antwort passt (z. B. R6). Vorschlag: bei Auswahl ohne Muster „Schau dir deine Wahl und die Frage noch einmal an“ statt eines Musters, das nicht zutrifft – und die Inhalts-Chats ergänzen Muster je falscher Option.

**M7 Erklärung: erstes Bild doppelt (Fakt, schwach).** „Worum geht’s“ zeigt das Thermometer ohne Markierung, Schritt 1 direkt danach dasselbe mit −3 °C. Die dritte Darstellung (3 °C gegen −3 °C bei „Pass auf“) ist sinnvoll. Vorschlag: bei „Worum geht’s“ kein Bild, wenn Schritt 1 dasselbe Bild hat.

**M8 Schwebender Menüknopf ≡ verdeckt Inhalt (Vermutung).** Auf den Ganzseiten-Bildern liegt ≡ über „Etappe 1 von …“ und über „Abflug, wann es dir passt“. Ob das beim Scrollen am Gerät stört, ist aus Ganzseiten-Bildern nicht sicher. Am Tablet kurz prüfen.

**M9 „Für deine Klasse ist alles verteilt.“ (Fakt, Text).** Unter „Kommt noch · Klasse 5“ unverständlich für ein Kind. Vorschlag: „Alles aus Klasse 5 steht schon in deinem Plan.“

Nicht nachgestellt / Testartefakt möglich:
- Startseite Eltern: GYM/RS/IB-Balken zeigen „–“. Wahrscheinlich, weil meine Testdaten kein `jahrgang` je Flug liefern. Mit echten Daten anschauen.
- Ziehen im Flugplan klappte im Test auf dem Tablet (Melbourne an Platz 2, „Gespeichert“), auf Handy und Rechner nicht. Vermutlich mein Testskript (langer Zug mit Scrollen), kein App-Fehler belegt. Mit dem Finger am Handy kurz prüfen.

## 3. Wer macht was

| Punkt | Wer |
|---|---|
| M1, M2, M3, M5, M7, M8, M9 | Haupt-Chat (App) |
| M4 | Haupt-Chat (Markierung/Einsortierung) + Sebastian (Plan der Kinder ansehen) |
| M6 | Haupt-Chat (Fallback-Text) + Inhalts-Chats (Fehlermuster je Auswahl-Option) |
