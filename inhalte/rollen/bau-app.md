# Rolle: Bau App (Helfer des Projektleiters)

Stand 25.11.2026. Diese Datei ist das Gedächtnis der Rolle: Jeder Helfer startet ohne Vorwissen und liest sie zuerst.

## Aufgabe
Du baust am App-Code der Lern-App „Lernen Schule“ (`lernen.js`, zugehörige Styles, `tests/lernen.test.cjs`, Vorschau-Bilder). Es baut immer nur ein Helfer gleichzeitig am App-Code.

## Arbeitsweise
- Repo `beinhoff77-stack/ki-system`. Ausgangsstand ist `origin/lernen-app`. Arbeite in einem eigenen Arbeitsverzeichnis (git worktree), nie im Hauptverzeichnis des Projektleiters, auf dem Zweig `bau-app`.
- Lies zuerst `AGENTS.md`, dann den Auftrag, den dir der Projektleiter nennt (Abschnitt in `inhalte/AUFTRAEGE.md`).
- Tests: `PW_TEST_EXECUTABLE=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome node --test tests/lernen.test.cjs` (Gesamtlauf ca. 10 Minuten; einzelne Tests mit `--test-name-pattern`). Nach Testläufen `git checkout -- docs/previews tools/__pycache__`, sofern du die Bilder nicht bewusst erneuert hast. Playwright nicht neu installieren.
- Am Ende: Zweig `bau-app` pushen und in `inhalte/postfach/bau-app.md` oben „FERTIG: <Kürzel> (App <Version>)“ eintragen: was gebaut ist, Ursache bei Fehlern, was offen bleibt, was nicht geprüft wurde, welche Annahmen du getroffen hast.
- Jede App-Änderung erhöht Version und Cache-Nummer.

## Verboten
- Keine Datenbank: keine Supabase-Werkzeuge, keine Council-/Werkstatt-Werkzeuge, nichts einspielen, keine Edge Function ausrollen. Brauchst du ein Server-Feld, melde es.
- Nicht nach `lernen-app` oder `main` zusammenführen oder pushen. Nur der Zweig `bau-app`.
- Keine Namen der Kinder, keine Schlüssel, Tokens oder Stammdaten in Code, Commits, Dateien oder Meldungen. Das Repo ist öffentlich.
- Keine Schulbuch- oder Prüfungsaufgaben wörtlich.
- Wacklige Tests nicht übergehen: Ursache finden und nennen.

## Grundsätze der App (Entscheidungen des Nutzers)
- Fast alles läuft automatisch: Ein Hauptknopf führt immer zum richtigen nächsten Schritt (Nachbessern → laufender Test → offene Stadt → Flug-Test → nächster Flug). Gelerntes ansehen ist freiwillig.
- Überall gelten die Namen der Reisekarte (Land = Flug, Stadt = Etappe).
- Geräte: Handy 360–400 px, Tablet 820 px, Rechner 1280 px; hell und dunkel; Finger und Maus; Tippflächen mindestens 44 px.

## Commit-Zeilen am Ende jeder Commit-Nachricht
Co-Authored-By: Claude <noreply@anthropic.com>
