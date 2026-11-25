# Postfach bau-app

Neueste oben.

## 2026-11-25 – FERTIG: WT (App 0.93.5)

Ausgangsstand `origin/lernen-app` 8ae84ee, Zweig `bau-app`. Nur App und Tests: keine Datenbank, nichts eingespielt, kein Merge. Cache v180.

**Ursache des wackligen Tests „KJ §0: Kinderseite …“**
- Rot war die Prüfung `ohneQuerrollen` bei 400 px (Tag), nicht der Hauptknopf.
- Auslöser ist die Anrede-Sticker („Digga“) auf der Ecke der ersten Karte (unter 600 px, `.lr-jw-ecke`). Ihr Auftauchen („Plopp“, `lrJwPlopp`, 0,35 s Verzögerung + 0,4 s) schwingt über 100 % hinaus. Dabei ragt das „?“ (`.lr-jw-frage`) etwa 0,45–0,6 s nach dem Zeichnen 2–3 px über den rechten Rand: Die Seite ist kurz quer rollbar (scrollWidth 402–403 bei 400 px).
- Der Test prüft nach `waitFor` + 400 ms + den übrigen Prüfungen. Je nach Rechnerlast fällt die Prüfung in dieses Fenster oder nicht. Das ist ein echter, kleiner Fehler der App (kurzes Querrollen auf dem Handy), kein Fehler des Tests.
- Der Verdacht „Hauptknopf wird nachträglich gefüllt“ trifft diesen Test nicht: Die Abflugtafel zeichnet erst, wenn alle Antworten da sind, und `lernSchrittKnopf` kommt dort nicht vor. Mit verzögerter Karte, Übersicht, Konto oder Merkheft (je 800 ms) und mit Zufallsverzögerung blieb Reihenfolge, Text und Ziel immer richtig.

**Fehlermeldung im Wortlaut** (KJ §0 einzeln, 3 von 10 Läufen rot, Zeile 5042 = `ohneQuerrollen` in der Schleife 400/820):
```
not ok 1 - KJ §0: Kinderseite – Nachbessern zuerst (Expedition als Chip), Gerade dran, Zusatz · eingeplant, Mein Schuljahr; Zahlen aus schuljahr_stand; gelber Knopf nie Zusatz (400/820, Tag und Nacht)
  error: |-
    The expression evaluated to a falsy value:

      assert.ok(await ohneQuerrollen(page))

  code: 'ERR_ASSERTION'
```
Messung (alle 40 ms nach dem Zeichnen): 4 von 8 Durchläufen bei 400 px mit `I.lr-jw-frage r=402` zwischen 484 und 565 ms; bei 820 px nie.

**Geändert**
- `style.css`: `.lr-jw-ecke { transform-origin: 100% 100%; }` – der Sticker wächst von seiner rechten unteren Ecke aus nach links. Danach 0 von 8 Messdurchläufen mit Querrollen, KJ §0 einzeln 10 von 10 grün (vorher 7 von 10).
- Wettlauf beim Hauptknopf (Punkt 2/3 des Auftrags), unabhängig vom wackligen Test, aber echt:
  - `lernSchrittKnopf` war sofort mit dem Ziel des Servers (`vorher`, z. B. `#/reise/1` oder `…-erklaeren-1`) antippbar und hatte den Stadtnamen schon im Text. Bis zur Antwort konnte ein Tippen woanders hinführen als der fertige Schritt. Mit verzögerter Karte nachgewiesen: auf 0.93.4 zeigte der Knopf „Weiter“ nach dem Test 43 ms nach dem Start antippbar `#/reise/1` statt `#/lerneinheit/1-2-ueben-2-start`.
  - Neu: Der Knopf steht sofort sichtbar da, aber gesperrt (`lr-schritt-wartet`, `aria-disabled`, ohne `href`, Antippen wird abgefangen), Text nur „Weiter“. Er wird erst mit dem fertigen Ziel frei. Bei Fehler, ohne Stände der Karte oder bei `ohne` gilt wie bisher das Ziel vom Server.
  - `lernReiseKarte`: Antworten älterer Abrufe werden verworfen. Eine Antwort ersetzt die gemerkte Karte nur, wenn seit ihrem Abruf nichts vergessen wurde und keine neuere Antwort da ist. Vorher konnte eine langsame alte Antwort Namen und Stände auf den alten Stand zurücksetzen.
  - Reisekarte und Abflugtafel, die mit der gemerkten (alten) Karte gezeichnet sind: Hauptknopf, „Gerade dran“ und Einsteigen bleiben sichtbar, aber gesperrt und ohne Stadtname (`lr-ziel-offen`), bis die frische Karte da ist. Dann wird neu gezeichnet; kommt keine, wird der Knopf frei. Die Abflugtafel zeichnete vorher mit alter Karte gar nicht neu.
  - Wechsel des Kindes war schon geschützt (`viewGuard`: Hash und Zeichen-Nummer). Geprüft, nichts geändert.
- Version 0.93.5 (`app.js`, `lernen/schule.js`, `index.html`, `lernen/index.html`, `sw.js`, Erwartungen in `tests/search.test.cjs`), Cache v179 → v180.

**Tests**
- Hilfe in `setup`: `verzoegerungJe(aktion, daten)` verzögert einzelne Antworten des nachgestellten Servers.
- Neu: „WT: Hauptknopf erst antippbar, wenn sein Ziel feststeht …“. Ein Beobachter im Browser prüft alle 15 ms jeden Hauptknopf: entweder gesperrt ohne Ziel und ohne Stadtname oder das fertige Ziel. Den ersten wartenden Knopf tippt er an, das darf nicht navigieren.
  - Karte 800 ms und Übersicht 800 ms: Knopf nach bestandenem Test und anschließend die Reisekarte.
  - Wechsel Kind 1 → Kind 2 während Kind 1 lädt (Karte und Konto 900 ms), Reisekarte und Abflugtafel: nie ein Ziel von Kind 1, Kopf von Kind 2.
  - Auf 0.93.4 rot (s. o.), auf 0.93.5 grün.
- KJ §0 unverändert. Der Test hat zu Recht angeschlagen.

**Gesamtläufe** (`node --test tests/lernen.test.cjs`)
- Vor der Änderung (0.93.4): Lauf 1 202/202, Lauf 2 202/202 (parallel zu Messläufen). Lauf 3 202/202, aber während dieses Laufs habe ich `style.css` schon geändert; er zählt nicht sauber als Lauf auf 0.93.4. Im Gesamtlauf kam der Fehler also nicht wieder. Nachgewiesen ist er einzeln (3 von 10, Wortlaut oben).
- Nach der Änderung (0.93.5): zweimal hintereinander 203/203 grün.

**Offen / nicht geprüft**
- `tests/search.test.cjs` „PWA installiert vollständige Offline-Hülle …“ ist rot, auch auf dem unveränderten Stand 8ae84ee: Der Test öffnet fest den Cache `:v143`. Das war schon vorher kaputt, ich habe es nicht behoben. Nur die Versionsnummern darin sind auf 0.93.5 gesetzt.
- Nicht auf echten Geräten geprüft, nur Chromium im Test. Weitere Stellen mit Plopp-Animation am Rand (z. B. Sticker auf der Startkarte der Reisekarte `.rk-schwebe-karte`) bekommen dieselbe Regel, sind aber nicht einzeln vermessen.
- Gesperrter Knopf bei langsamem Netz: Das Kind sieht bis zur Antwort nur „Weiter“ (gedimmt). Bei sehr langsamer Verbindung wirkt das wie ein toter Knopf. Eine Zeitgrenze gibt es nicht; bei Fehler wird er mit dem Server-Ziel frei.
- Keine neuen Vorschau-Bilder.

**Annahmen**
- „Ohne Stadtname“ heißt: Der wartende Knopf zeigt nur „Weiter“; Reisekarte und Tafel blenden die Texte von Startknopf, „Gerade dran“ und Einsteigen aus, die Flächen bleiben sichtbar.
- Der Wackler des Gesamtlaufs vom 24.11. hatte dieselbe Ursache. Die Meldung von damals ist nicht erfasst; belegt ist es nur durch dieselbe Stelle im Test und die Messung.
