# Seiten und Zustände der Lern-App – Bildschirmfotos für die Durchsicht (28.11.)

Alle Bilder liegen in `bilder/`, Dateiname `<nr>-<seite>-<breite>-<hell|dunkel>.jpg`; Breiten 390 px und 1280 px, ganze Seite (fullPage), außer bei Vollbild-Ansichten (Landung, Menü, Einstellen-Blatt, Expedition freigeschaltet): dort nur der sichtbare Bildschirm.
Aufnahme mit `node inhalte/design/durchsicht-2811/bilder_machen.cjs` (nutzt den Server-Nachbau und die erfundenen Beispieldaten aus `tests/lernen.test.cjs`; Kinder heißen „Kind A“, „Kind B“, „Testkind“). Adressen gelten auf der Lernen-Seite `/lernen/` (außer wo angegeben).

Hinweis hell/dunkel: Kinderseiten folgen der Einstellung „Tag/Nacht“ (`lern.gestaltung`), das Regel-Universum und die Haupt-App dem Farbschema des Geräts. Die Lehrer-/Eltern-Seiten sind im Nachbau immer hell – hell- und dunkel-Bilder sind dort gleich.

| Nr | Seite | Adresse | Dateinamen | Bemerkung |
|---|---|---|---|---|
| 01 | anmeldung | `lernen/ (ohne Anmeldung)` | `01-anmeldung-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lernen-Seite, Lern-Code-Anmeldung |
| 01b | anmeldung-hauptapp | `login (KI-System)` | `01b-anmeldung-hauptapp-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Anmeldung der Haupt-App (Passwort), nicht die Lernen-Seite |
| 02 | lehrer-start | `#/ (= #/lernen)` | `02-lehrer-start-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Startseite „Was ist los?“ |
| 02b | lehrer-start-ruhig | `#/lernen (nichts zu tun)` | `02b-lehrer-start-ruhig-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Startseite „Alles ruhig.“ (Nachbau laLage: keine Einheit offen, Lerntag gestern) |
| 03 | reisekarte | `#/reise/1` | `03-reisekarte-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Reisekarte Europa mit Pins und Startknopf (Nachbau rkServer) |
| 03b | reisekarte-menue | `#/reise/1 + Menü` | `03b-reisekarte-menue-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Reisekarte, Menüblatt (≡) geöffnet |
| 03c | abflugtafel | `#/reise/1 (ohne Kartendaten)` | `03c-abflugtafel-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Abflugtafel (erscheint nur, wenn der Server keine Kartendaten liefert); Abschnitte „Später – für höhere Klassen“ und „Was kommt wann wieder?“ eingeklappt |
| 03d | abflugtafel-aufgeklappt | `#/reise/1 (ohne Kartendaten)` | `03d-abflugtafel-aufgeklappt-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Abflugtafel, alle aufklappbaren Abschnitte offen (der Abschnitt „Auch offen“ erscheint nur bei mehreren gleichzeitig offenen Orten – im Nachbau nicht erreichbar) |
| 03e | abflugtafel-checkin | `#/reise/1 (Check-in fällig)` | `03e-abflugtafel-checkin-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Abflugtafel mit Ansage „Vorher kurz einchecken“ (Nachbau wdhServer) |
| 03f | expedition-freigeschaltet | `#/reise/1 (Expedition neu)` | `03f-expedition-freigeschaltet-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Ansicht „Expedition freigeschaltet“ beim Öffnen der Reisekarte |
| 04a | weg-stand | `#/weg/1` | `04a-weg-stand-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Mein Weg · Reiter Stand |
| 04b | weg-kontinente | `#/weg/1-kontinente` | `04b-weg-kontinente-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Mein Weg · Reiter Kontinente |
| 04c | weg-karte | `#/weg/1-karte` | `04c-weg-karte-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Mein Weg · Reiter Karte |
| 05a | reisepass | `#/reisepass/1` | `05a-reisepass-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Reisepass |
| 05b | route | `#/route/1` | `05b-route-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Meine Route 5–10 (Nachbau lmsAnpassen, Kindsicht). Aufgenommen in der Haupt-App (KI-System), weil die Lernen-Seite mit Kinder-Code #/route auf die Reisekarte umleitet (route fehlt in KIND_ANSICHTEN in lernen/schule.js) |
| 05c | wiederholen | `#/wiederholen/1` | `05c-wiederholen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Wiederholen = Check-in, Bordkarte 1 von 3 |
| 05d | stationen | `#/stationen/1` | `05d-stationen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Expeditionen: Stempel-Sammlung |
| 05e | expedition | `#/expedition/1-7` | `05e-expedition-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Einzelne Expedition „Die Wetterstation“, Teil a offen |
| 05f | merkheft | `#/merkheft/1` | `05f-merkheft-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Merkheft |
| 05g | merkheft-offen | `#/merkheft/1 (aufgeklappt)` | `05g-merkheft-offen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Merkheft, alle Einträge aufgeklappt |
| 06a | einheit-start | `#/lerneinheit/1-1` | `06a-einheit-start-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lerneinheit: Etappen-Weg / Start |
| 06b | einheit-erklaerung | `#/lerneinheit/1-1-erklaeren-1` | `06b-einheit-erklaerung-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Erklärung der Etappe 1 |
| 06b2 | einheit-erklaerung-2 | `#/lerneinheit/1-1-erklaeren-2` | `06b2-einheit-erklaerung-2-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Erklärung der Etappe 2 (mit Zahlenstrahl-Bild) |
| 06c | aufgabe-offen | `#/lerneinheit/1-1-ueben-1` | `06c-aufgabe-offen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Bordkarte (Aufgabe) offen, Zahl mit Tastenfeld |
| 06c2 | aufgabe-zahlenstrahl | `#/lerneinheit/1-1-ueben-2` | `06c2-aufgabe-zahlenstrahl-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Bordkarte mit Zahlenstrahl (Markierung) |
| 06c3 | aufgabe-luecken | `#/lerneinheit/1-1-ueben-3` | `06c3-aufgabe-luecken-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Bordkarte mit Lücken (Binomische Formeln) |
| 06d | aufgabe-tipp | `#/lerneinheit/1-1-ueben-1 + Tipp` | `06d-aufgabe-tipp-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Tipp gezeigt |
| 06e | aufgabe-richtig | `#/lerneinheit/1-1-ueben-1 + richtig` | `06e-aufgabe-richtig-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Richtig beantwortet („An Bord“) |
| 06f | aufgabe-falsch-1 | `#/lerneinheit/1-1-ueben-1 + falsch (1. Versuch)` | `06f-aufgabe-falsch-1-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Falsch beantwortet, Hinweis zum Fehlermuster, zweiter Versuch |
| 06g | aufgabe-falsch-erklaert | `#/lerneinheit/1-1-ueben-1 + falsch (2. Versuch)` | `06g-aufgabe-falsch-erklaert-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Falsch beantwortet mit Lösung und Erklärung („Kurskorrektur“) |
| 06h | landung-direkt | `#/lerneinheit/1-1-ueben-1 (gelandet, Direktflug)` | `06h-landung-direkt-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Landung Etappe: Direktflug (Sterne, Abzeichen) |
| 06i | landung-sauber | `#/lerneinheit/1-1-ueben-1 (gelandet, saubere Landung)` | `06i-landung-sauber-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Landung Etappe: saubere Landung |
| 06j | landung-sturm | `#/lerneinheit/1-1-ueben-1 (gelandet, Sturmflug)` | `06j-landung-sturm-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Landung Etappe: Sturmflug gemeistert |
| 06k | knobel-bordkarte | `#/lerneinheit/1-1-ueben-1 (nach Landung)` | `06k-knobel-bordkarte-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Knobel-Bordkarte nach der Etappe (Aufgabe offen) |
| 06k2 | knobel-geloest | `#/lerneinheit/1-1-ueben-1 (Knobel gelöst)` | `06k2-knobel-geloest-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Knobel-Bordkarte richtig gelöst (+30 Sterne) |
| 06l | mischkarte | `#/lerneinheit/1-1-ueben-1 (Mischkarte)` | `06l-mischkarte-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Mischkarte „Aus deiner Reise“ (Wiederholung aus anderem Flug), Aufgabe offen |
| 06m | checkin-bordkarte | `#/wiederholen/1` | `06m-checkin-bordkarte-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Bordkarten-Check-in (Wiederholung), Bordkarte 2 von 3 nach Fehler (Koffer-Leiste) |
| 06m2 | checkin-fertig | `#/wiederholen/1 (Eingecheckt)` | `06m2-checkin-fertig-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Check-in geschafft: „Eingecheckt!“ |
| 06n | etappe-abgelegt | `#/wiederholen/1 (Etappe abgelegt)` | `06n-etappe-abgelegt-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Blatt „Etappe abgelegt“ nach einer Wiederholung |
| 06o | test-start | `#/lerneinheit/1-1-test` | `06o-test-start-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Flug-Test: Start |
| 06p | test-frage | `#/lerneinheit/1-1-test (Frage)` | `06p-test-frage-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Flug-Test: Frage offen |
| 06q | test-ergebnis | `#/lerneinheit/1-1-test (Ergebnis)` | `06q-test-ergebnis-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Flug-Test: Auswertung (1 von 2 richtig) |
| 06r | landung-flug | `#/lerneinheit/1-1-test (Flug geschafft)` | `06r-landung-flug-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Landung Flug: „Flug geschafft“ mit Sternen |
| 06s | landung-flug-naechstes | `#/lerneinheit/1-1-test (Bordkarte nächstes Thema)` | `06s-landung-flug-naechstes-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Bordkarte zum nächsten Thema nach „Flug geschafft“ |
| 06t | landung-ort-stempel | `#/lerneinheit/1-1-test (Ort geschafft, Stempel)` | `06t-landung-ort-stempel-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Landung Ort: Reisepass-Stempel „Rom ist geschafft“ |
| 06u | landung-ort-bordkarte | `#/lerneinheit/1-1-test (Bordkarte neuer Ort)` | `06u-landung-ort-bordkarte-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Bordkarte „Von Rom nach Athen“ |
| 07a | universum-aufbau | `#/regeln/1-universum` | `07a-universum-aufbau-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Regel-Universum: Sonnensystem „Aufbau“ (mit Link „Mein Merkheft“) |
| 07b | universum-klassen | `#/regeln/1-klassen` | `07b-universum-klassen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Regel-Universum: „Durch die Klassen“ |
| 07c | gebiet | `#/regeln/1-gebiet-fur` | `07c-gebiet-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Ein Gebiet (Fläche und Raum) mit „Auf einen Blick“-Tafeln |
| 07d | arbeitsweisen | `#/regeln/1-weisen` | `07d-arbeitsweisen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Arbeitsweisen |
| 07e | idee | `#/regeln/1-idee-fur-2` | `07e-idee-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Eine Idee/Regelseite (Stufen) |
| 07e2 | einzelregel | `#/regeln/1-regel-f<n>` | `07e2-einzelregel-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Einzelne Regel (Ebene 3), erreicht über Idee → Folge → erste Karte |
| 07f1 | tafel-formeln | `#/regeln/1-tafel-formeln` | `07f1-tafel-formeln-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Tafel formeln |
| 07f2 | tafel-einheiten | `#/regeln/1-tafel-einheiten` | `07f2-tafel-einheiten-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Tafel einheiten |
| 07f3 | tafel-formeln-flaechen | `#/regeln/1-tafel-formeln-flaechen` | `07f3-tafel-formeln-flaechen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Tafel formeln-flaechen |
| 07f4 | tafel-formeln-koerper | `#/regeln/1-tafel-formeln-koerper` | `07f4-tafel-formeln-koerper-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Tafel formeln-koerper |
| 07f5 | tafel-zahlen | `#/regeln/1-tafel-zahlen` | `07f5-tafel-zahlen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Tafel zahlen |
| 07f6 | tafel-stellenwert | `#/regeln/1-tafel-stellenwert` | `07f6-tafel-stellenwert-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Tafel stellenwert |
| 07f7 | tafel-bruch-dezimal-prozent | `#/regeln/1-tafel-bruch-dezimal-prozent` | `07f7-tafel-bruch-dezimal-prozent-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Tafel bruch-dezimal-prozent |
| 07f8 | tafel-figuren | `#/regeln/1-tafel-figuren` | `07f8-tafel-figuren-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Tafel figuren |
| 07f9 | tafel-zeichen-woerter | `#/regeln/1-tafel-zeichen-woerter` | `07f9-tafel-zeichen-woerter-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Tafel zeichen-woerter |
| 07f10 | tafel-formeln-zeile-offen | `#/regeln/1-tafel-formeln (Zeile Kreis aufgeklappt)` | `07f10-tafel-formeln-zeile-offen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Formeln auf einen Blick mit aufgeklappter Zeile „Kreis“ |
| 07f11 | tafel-einheiten-offen | `#/regeln/1-tafel-einheiten (alles aufgeklappt)` | `07f11-tafel-einheiten-offen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Maßeinheiten, alle Abschnitte aufgeklappt |
| 07g | suche-cm | `#/regeln/1-suche („cm“)` | `07g-suche-cm-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Suche mit Treffern für „cm“ (Tafel zuerst) |
| 07g2 | suche-kegelmantel | `#/regeln/1-suche („Kegelmantel“)` | `07g2-suche-kegelmantel-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Suche mit Treffern für „Kegelmantel“ |
| 07h | regeln-aendern-lassen | `#/regeln/kind-tafel-einheiten (Ändern lassen)` | `07h-regeln-aendern-lassen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Erwachsene sehen die Kind-Ansicht; „Ändern lassen“ an der Tafel geöffnet |
| 07i | regeln-liste-lehrer | `#/regeln` | `07i-regeln-liste-lehrer-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lehrer-/Eltern-Liste aller Regeln und Arbeitsweisen |
| 07j | regeln-lehrer-regelblatt | `#/regeln/lehrer-r6` | `07j-regeln-lehrer-regelblatt-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lehrer: Blatt einer Rechenregel (alle Stufen offen) |
| 08a | kind-ueberblick | `#/kind/1-ueberblick` | `08a-kind-ueberblick-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lehrer: Kind-Ansicht, Reiter Überblick |
| 08b | kind-wackelt | `#/kind/1-wackelt` | `08b-kind-wackelt-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lehrer: Reiter „Was wackelt“ (neue Ansicht mit Auswertung) |
| 08c | kind-wackelt-besprochen | `#/kind/1-wackelt (Besprochen)` | `08c-kind-wackelt-besprochen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Was wackelt, alle Themen aufgeklappt und etwas unter „Besprochen“ (Nachbau wwServer, vorher besprochen) |
| 08d | kind-lehrplan | `#/kind/1-lehrplan` | `08d-kind-lehrplan-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lehrer: Kind-Ansicht, Reiter Lehrplan (Fahrplan + Matrix) |
| 08e | lehrplan | `#/lehrplan` | `08e-lehrplan-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lehrer: Lehrplan (Matrix aller Themen) |
| 08f | schulstand | `#/schulstand/1` | `08f-schulstand-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lehrer: Schulstand des Kindes |
| 08f2 | schulstand-alle | `#/schulstand` | `08f2-schulstand-alle-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lehrer: Schulstand, alle Kinder im Vergleich |
| 08g | expeditionen | `#/expeditionen` | `08g-expeditionen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lehrer: Expeditionen, alle Einträge aufgeklappt (Nachbau expKonto) |
| 08h | lernauftraege | `#/lernauftraege` | `08h-lernauftraege-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lehrer: Lernaufträge |
| 08i | info | `#/info` | `08i-info-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Info „So funktioniert’s“ (Fragen eingeklappt, wie beim Öffnen) |
| 08j | zugaenge | `#/zugaenge` | `08j-zugaenge-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Eltern: Zugänge (Lehrer hat keinen Zugang zu dieser Seite) |
| 08k | einstellen | `#/ (Einstellen-Dialog Kind A)` | `08k-einstellen-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Eltern: Blatt „Kind A einstellen“ geöffnet (Lehrer hat dieses Blatt auch) |
| 08l | lernen-eltern | `#/lernen (Eltern)` | `08l-lernen-eltern-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Eltern-Startseite: Zu tun mit Wunsch, Belohnungen |
| 08m | inhalte | `#/inhalte/1` | `08m-inhalte-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lehrer: Inhalte ansehen (Einheit 1, Etappen und Aufgaben) |
| 08n | plan-lernstand | `#/lernstand/1` | `08n-plan-lernstand-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Lehrer: Lernstand des Kindes (leitet auf Kind-Ansicht um, falls veraltet) |
| 09a | zustand-laden | `#/reise/1 (Server antwortet nicht)` | `09a-zustand-laden-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Ladeanzeige: Server antwortet 60 s lang nicht, Aufnahme nach 0,7 s |
| 09a2 | zustand-laden-lehrer | `#/lernen (Server antwortet nicht)` | `09a2-zustand-laden-lehrer-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Ladeanzeige Lehrer-Startseite |
| 09b | zustand-fehler-kind | `#/reise/1 (API-Fehler 500)` | `09b-zustand-fehler-kind-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Fehlermeldung bei API-Fehler, Kinderseite |
| 09b2 | zustand-fehler-lehrer | `#/lernen (API-Fehler 500)` | `09b2-zustand-fehler-lehrer-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Fehlermeldung bei API-Fehler, Lehrer-Startseite |
| 09b3 | zustand-fehler-eingabe | `#/lerneinheit/1-1-ueben-1 (Prüfen schlägt fehl)` | `09b3-zustand-fehler-eingabe-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Fehlermeldung beim Prüfen einer Antwort (Server 500) |
| 09c | zustand-toast | `#/kind/1-lehrplan (Meldung „Gespeichert“)` | `09c-zustand-toast-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Toast-Meldung unten mit „Rückgängig“ nach dem Einplanen eines Themas |
| 09d | zustand-leer-auftraege | `#/lernauftraege (leer)` | `09d-zustand-leer-auftraege-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Leere Liste: keine Lernaufträge |
| 09d2 | zustand-leer-merkheft | `#/merkheft/1 (leer)` | `09d2-zustand-leer-merkheft-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Leere Liste: Merkheft ohne Geschafftes |
| 09d3 | zustand-leer-zugaenge | `#/zugaenge (leer)` | `09d3-zustand-leer-zugaenge-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Leere Liste: keine Zugänge |
| 09d4 | zustand-leer-wackelt | `#/kind/1-wackelt (leer)` | `09d4-zustand-leer-wackelt-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Leere Liste: Was wackelt ohne Fehler |
| 09d5 | zustand-leer-reisepass | `#/reisepass/1 (noch nichts)` | `09d5-zustand-leer-reisepass-{390,1280}-{hell,dunkel}.jpg` (4 von 4) | Leere Liste: Reisepass ohne Stempel/abgelegte Flüge |

## Nicht (oder nur teilweise) erreichbar im Nachbau

- „Auch offen“ auf der Abflugtafel: nur bei mehreren gleichzeitig offenen Orten im Plan – im Nachbau nicht erreichbar.
- „Merkheft im Universum“: ist der Link „Mein Merkheft“ oben im Regel-Universum (zu sehen auf 07a, 07g) und führt zur Seite `05f`/`05g`; eine eigene Merkheft-Ansicht im Universum gibt es nicht.
- Flug-Test „Gleich verbessern“ (Korrektur) und Nachtragstest: nicht aufgenommen.
- Lehrer-/Eltern-Seiten: hell und dunkel sind gleich, weil diese Seiten kein Dunkel kennen (Bereich „Lernen“ ist fest hell).
- Zustand „Ladeanzeige“ ist eine Momentaufnahme nach 0,3–0,7 s bei absichtlich ausbleibender Server-Antwort.
- Einzelne Aufnahmen enthalten Zufalls-Sticker („Yo Digga!“, „GOAT“ …) und Mock-Texte; die Daten sind erfunden.
