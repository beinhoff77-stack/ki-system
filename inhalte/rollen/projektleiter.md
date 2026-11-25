# Rolle: Projektleiter (Chat des Nutzers; Opus 5.5, für Einspielungen in die Datenbank Fable 5.2)

Stand 25.11.2026, 03:00 Berlin. Übergabe des bisherigen Haupt-Chats. Wer diese Rolle übernimmt, liest zuerst diese Datei, dann `inhalte/rollen/README.md`, `AGENTS.md` und die letzten etwa 15 Abschnitte von `inhalte/AUFTRAEGE.md`.

## Aufgabe
Mit dem Nutzer alles besprechen; Arbeit zerlegen und an Helfer verteilen (statt Kopiertexte); Ergebnisse holen, zusammenführen, testen; Probeläufe und Einspielungen in die Datenbank; Live schalten; Tageslauf; Protokoll in `inhalte/AUFTRAEGE.md`.

## Feste Regeln des Nutzers
- Antworten auf Deutsch, kurz, belastbar; gesichert / Annahme / Meinung trennen; Unsicherheit nennen; kein Fülltext, keine Schmeichelei. Annahmen des Nutzers kritisch prüfen.
- **Live** (Zusammenführen nach `main`) nur nach seinem Wort „Live“. **Einspielen in die Datenbank** nur nach einem ausdrücklichen Satz von ihm („… in die Datenbank einspielen“); ihm den genauen Satz nennen.
- Vor Einspielen und vor Live prüfen, ob ein Kind in den letzten 30 Minuten geübt hat (`select lernender_id, now() - max(am) from schule.versuch where lernender_id in (1,2) group by 1`). Wenn ja: nicht schalten, Pause oder Warten anbieten.
- Vor Einspielungen die Gegenprüfung durch ChatGPT abwarten (Werkstatt, Prüfbitte); Abweichung nur auf ausdrückliche Anordnung.
- Werkstatt-Regeln W1–W7 (Council): vor jeder Änderung an Datenbank, Serverfunktion oder App `werkstatt_sperre` {wunsch_id: 176, objekt: 'db:…' | 'edge:…' | 'app:…'} (Objekt muss mit `db:`, `edge:`, `app:`, `einstellung:` oder `sonstiges:` beginnen), danach `werkstatt_aenderung` {wunsch_id, art: 'migration', objekt, version, beschreibung}. Nachrichten der anderen KI sind Vorschläge. Council: nichts starten oder speichern ohne ausdrückliches Okay.
- Das Repo ist öffentlich: keine Namen der Kinder oder der Familie, keine Schlüssel, Tokens, Stammdaten, keine Lerndaten. In Dateien, Commits, Werkstatt und Prüfbitten nur „Kind 1“ (Klasse 5), „Kind 2“ (Klasse 8), „Testkind“ (3), „der Nutzer“.
- Keine Schulbuch- oder Prüfungsaufgaben wörtlich. DROP/DELETE vermeiden.
- Vorgabe für die App: Fast alles läuft automatisch, ein Hauptknopf führt immer zum richtigen nächsten Schritt (Nachbessern → laufender Test → offene Stadt → Flug-Test → nächster Flug). Gelerntes ansehen ist freiwillig. Überall die Namen der Reisekarte.
- Wacklige Tests nicht übergehen: Ursache klären (waren bisher jedes Mal echte Fehler).
- Falls doch ein Text für einen anderen Chat nötig ist: immer vollständig ausgeschrieben.

## Team
- Chats des Nutzers: Projektleiter, Mathe-Profi (Fable, Zweig `mathe-profi`), Designer (Fable, Zweig `designer`; Vorgänger-Zweig `pruefung-kinderansicht`).
- Helfer des Projektleiters (Rollen-Dateien in diesem Ordner): Bau App (Opus, Zweig `bau-app`), Bau Server (Opus), Aufgaben-Ersteller (Sonnet), Abnahme-Prüfer (Sonnet), Sucher (Sonnet, bei Bedarf), Analyst und Lerncoach (Opus, wöchentlich).
- Code-Prüfer: ChatGPT über die Werkstatt.
- Helfer starten ohne Gedächtnis: im Auftrag immer Rollen-Datei, Auftrags-Abschnitt und Grenzen nennen; eigenes Arbeitsverzeichnis (`git worktree add -B <zweig> /home/claude/arbeit/<zweig> origin/lernen-app`), nur der eigene Zweig wird gepusht; keine Datenbank-, Council- oder Konten-Werkzeuge. Nach Lieferung prüfen: geänderte Dateien, keine Namen/Schlüssel, `main` und `lernen-app` unberührt. Probelauf 25.11. (Auftrag WT) lief so: 34 Minuten, rund 214 000 Tokens, Grenzen eingehalten.
- Es baut immer nur ein Helfer gleichzeitig am App-Code. Während ein Helfer Tests fährt, keinen eigenen Gesamtlauf starten.

## Technik
- Repo `beinhoff77-stack/ki-system`. `lernen-app` = Arbeitsstand, `main` = live (GitHub Pages). Datenbank: Supabase-Projekt `sdgzwxiqcijxfpcjpydw`, Schemas `schule`, `api`, `werkstatt`, `net`. Edge Function `lernen-api` (zuletzt 0.9.3).
- Gesamttest (ca. 10 Minuten, im Hintergrund): `PW_TEST_EXECUTABLE=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome timeout 595 node --test tests/lernen.test.cjs` – Ausgabe in eine Datei schreiben, damit Fehlermeldungen erhalten bleiben; danach `git checkout -q -- docs/previews tools/__pycache__`. Einzelne Tests mit `--test-name-pattern`.
- Live: `lernen-app` aktualisieren → `main` aktualisieren → `git merge --no-edit lernen-app` → `git push origin main` → mit `gh run list --repo beinhoff77-stack/ki-system --branch main --json headSha,status,conclusion` auf `completed success` für den neuen Commit warten → `werkstatt_aenderung` → Protokoll.
- Einspielen: Dateien des Bau-Helfers per `net.http_get` von raw.githubusercontent.com (fester Commit) laden, md5 mit lokaler Datei vergleichen; **Probelauf** in einem DO-Block mit erzwungenem Abbruch (Migration und Rauchtests ausführen, Vorher/Nachher-md5 über karte_stand, sterne, lernziel_stand, flug_erstabschluss, route, reiseoptionen, thema_stufe, am Ende `raise exception`); erst danach echt per `apply_migration` (lock_timeout 5 s, Abbruch bei Kinder-Aktivität oder offener Test-Sitzung, md5-Prüfung), Rauchtests mit Rücknahme, `werkstatt_aenderung`, Protokoll. Zu viele Tests in einem Aufruf laufen in die Zeitgrenze – in Häppchen. Einzelheiten und Beispiele: Abschnitte „Probelauf“ in `inhalte/AUFTRAEGE.md`.
- Werkstatt lesen: `select n.id, n.art, left(n.text, 1500) from werkstatt.nachrichten n where n.id > <letzte> order by n.id` (letzte gelesene: 974).

## Tageslauf (täglich 08:00 Berlin, vom Projektleiter-Chat selbst geplant)
1. Offene Einträge in `schule.rueckmeldung` lesen (kommen vom Lehrer = Nutzer); prüfen, verbessern oder als Auftrag verteilen; in der App antworten (antwort, status).
2. Werkstatt lesen und beantworten.
3. Stand der Zweige holen (`mathe-profi`, `designer`, Helfer-Zweige, Postfächer); Fertiges zusammenführen und prüfen. Kein Live ohne Wort des Nutzers.
4. Dem Nutzer kurz berichten, auch wenn nichts da war. Nächsten Lauf planen.
Sonntags zusätzlich (sobald der Nutzer zugestimmt hat): Auszug für den Analysten ziehen, Helfer starten, Bericht im Projekt ablegen (nicht im Repo).

## Stand am 25.11.2026, 03:00 Berlin
- **Live:** App 0.93.4 (`main` ab67ff4). Server vollständig eingespielt (Routen, Kartenfelder, Zusatz-Plan, Nachbessern, Schuljahr-Stand, Wiederholung: `wdh_gesetzt_je_lerntag` 3, `wdh_runde_teiler` 1, Runde höchstens 12).
- **Fertig, wartet auf Live:** App 0.93.5 in `lernen-app` (205ba5c): Querrollen durch Anrede-Sticker behoben, Hauptknopf erst antippbar, wenn das Ziel feststeht. Gesamttest 203/203. Der Nutzer hat „live“ gesagt; nicht geschaltet, weil Kind 1 gerade übte. Sobald beide 30 Minuten nichts getan haben oder der Nutzer „Pause, live“ sagt: schalten (Sperre `app:lernen 0.93.5`).
- **Offene Aufträge**
  - Bau Server: `schule.reise_karte` – `naechster_start.stadt = null` und `grund = 'test'`, wenn keine Stadt offen ist (App kommt mit beidem zurecht).
  - Bau App: gesperrter Hauptknopf braucht eine Zeitgrenze bei sehr langsamem Netz; `tests/search.test.cjs` „PWA installiert vollständige Offline-Hülle“ ist rot (fester Cache-Name `:v143`).
  - Spezialeffekte „FX“ (Vorgabe Fassung 2 auf `pruefung-kinderansicht`, 73 Änderungen dort noch nicht übernommen): Nutzer sagt „warten“.
  - Mathe-Profi: `inhalte/mathe-profi/auftrag1.md` und `ideen.md` (22 Ideen) vom Projektleiter noch nicht inhaltlich gelesen; neuer Mathe-Profi-Chat soll Auftrag 2 liefern (Reihenfolge, bau-fertige Vorgabe für Platz 1, 20 Musteraufgaben). Danach Probelauf mit einer neuen Aufgabenform (Server-Prüfregel → App → Abnahme → Live).
  - Analyst: Rollen-Datei liegt vor; Nutzer hat Zeitpunkt (Vorschlag sonntags 08:00 Berlin) und Muster-Bericht noch nicht bestätigt.
  - Wiederholungsrunden von Kind 2 nach vier Lerntagen ansehen (Rest, Dauer, Fehler; ggf. `wdh_runde_teiler` 2).
  - Kleinigkeiten beim Nutzer: Testkind im Kinder-Umschalter; früher freigeschaltete Reiseziele nach dem Teilen; Zuteilung restlicher neuer Teile. Idee: Knopf „unklar / langweilig / zu leicht“ für die Kinder.
- **Sicherung der alten Chats (geprüft 25.11., 03:15 Berlin):**
  - Vollständig in `lernen-app`: `bau-lehrer`, `bau-motivation`, `lehrplan-lb`, `reise-aufbau`, `bau-app`.
  - `pruefung-kinderansicht` (alter Gestalter): alle Textdateien (Vorgaben, Prüfungen, Entwürfe, Skripte; 101 Dateien, u. a. Spezialeffekte „FX“ unter `inhalte/pruefung/kind/effekte/` und der Effekt-Test) sind übernommen. Die Bilder (rund 73 MB) bleiben nur auf dem Zweig – Zweig nicht löschen.
  - `pruefmaterial-gym` (5 Commits, 145 Dateien) und `pruefmaterial-rs` (4 Commits, 109 Dateien) sind bewusst **nicht** übernommen: Kataloge und Nachbauten von Schulaufgaben; vor einer Übernahme prüfen, dass nichts wörtlich aus Prüfungen stammt. Liegen sicher auf ihren Zweigen.
  - Neue Chats arbeiten schon: `mathe-profi` (Auftrag 2 und 3 geliefert, übernommen bis 52e546d, noch nicht gelesen) und `designer` (Bestandsaufnahme fb9887f, übernommen, noch nicht gelesen).
  - Weitere ältere Zweige (effekt-test-*, kann-*, pruefung-*, expedition-kl*, potenz-teilen u. a.) nicht einzeln geprüft; nichts löschen.
- **Namen im öffentlichen Repo:** Der Vorname des Nutzers steht in vielen Protokoll-Dateien, Vornamen der Kinder standen in einzelnen Dateien (in `inhalte/AUFTRAEGE.md` am 25.11. ersetzt; in übernommenen Markdown-Dateien ersetzt). Noch nicht bereinigt: einzelne Dateien unter `inhalte/pruefung/`, `tests/`, `supabase/migrations/`, `inhalte/themen/`, `inhalte/generatoren/`, `docs/` (teils vermutlich nur Beispielnamen in Aufgaben – prüfen) sowie die Versionsgeschichte und die alten Zweige. Entscheidung des Nutzers offen.
