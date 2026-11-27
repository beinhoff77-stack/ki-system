# Offene Punkte – Merkliste des Projektleiters (nichts davon vergessen)

Stand 27.11.2026, 03:00 (Berlin). Jede Zeile bleibt stehen, bis sie erledigt oder vom Nutzer gestrichen ist. Bei jedem Arbeitsbeginn lesen.

## Entschieden vom Nutzer, noch nicht fertig
| Nr. | Was | Stand | Nächster Schritt |
|---|---|---|---|
| 1 | **Form-Takt:** jede dritte Aufgabe in neuer Form; „sitzt“ nur über zählende Aufgaben; Sachaufgaben-Pflicht (`form-takt.md`) | Datenbank-Teil fertig als Datei, 19 Anker passen zur Live-Fassung, **Probelauf am 27.11. bestanden** (dritter Lauf; zwei Fehler im Prüfpaket behoben). App-Bau läuft (Zweig `helfer-app`, Version 0.94.0, abwärtsverträglich) | Antwort der Gegenprüfung auf Werkstatt 1026/1028 → Satz des Nutzers „Form-Takt einspielen“ → einspielen über den sparsamen Weg (Datei `tools/tests/aus/form_takt_einspielen.sql` per `net.http_get`, Prüfsumme) → App-Lieferung prüfen → „Live“ |
| 2 | **Vorrat neue Formen:** drei je Lernkarte (`rollend-4`) | 255 Aufgaben geliefert und übernommen; Zuordnung aller 16 Flüge steht (22 Einheiten, 574 Aufgaben mit Typ `bedingung`) | Inhaltsprüfung durch die Gegenprüfung (Werkstatt 1027); Befunde von einem Helfer berichtigen lassen; dabei `zaehlt = folge` bei A4-06, GE2-07, GE2-10 auf `ja` oder `nein` setzen; 6 Aufgaben für die zwei Lernkarten „verstehen“ in `ge1` nachliefern; Mischung prüfen (kaum „Zwei Wege“, keine „Brücke“ in rollend-4) |
| 3 | **Vorrats-Aufgaben einspielen** (rollend-1 bis -4, mit `form`/`zaehlt`) | wartet auf 1 | sparsamer Einspielweg (Datei aus dem Repo, Prüfsumme) |
| 4 | **Bruch-Nachbesserung 0.93.8** | dritte Runde fertig im Arbeitsstand (22 Bruch-Tests, Gesamttest 203/203), Werkstatt 1029 | Antwort Gegenprüfung → „Live“ (geht dann zusammen mit 0.94.0 oder vorher allein) |
| 5 | **Tempo auf der Elternseite** (Vorschlag 1 des Mathe-Profis, 27.11.: Sekunden je Aufgabe und Lernkarte im Verlauf, keine Stoppuhr für das Kind) | entschieden: ja | in den App-Bau nach dem Takt |
| 6 | **Eingangsdiagnose für Lücken aus früheren Klassen** (Vorschlag 2): Papier-Blatt | geliefert (`inhalte/mathe-profi/diagnose-1/`), PDFs beim Nutzer (kann nicht drucken: Aufgaben am Bildschirm, 30 Minuten, Strich, Zugabe) | Fotos und Zeiten vom Nutzer auswerten |
| 7 | **13 Aufgaben Wort → Term** für den laufenden Flug (`inhalte/mathe-profi/fachwoerter/`) | geliefert | Inhaltsprüfung, dann mit Punkt 3 einspielen |
| 8 | **Aufgaben mit vielen richtigen Antworten** (80 Stück, Typ `bedingung`) | Datenbank und App sind fertig und live | einspielen zusammen mit Punkt 3 |
| 9 | **Regel-Universum in die App** (Verlinkung mit Erklärungen, Feld Regel-Kennung/Fehlbild) | **Entschieden am 27.11.: Übersicht A „Sonnensystem“** (Liste B liegt hinter der Sonne). Inhalts-Helfer bereitet Texte der 15 Regel-Karten und Zuordnung Regel → Lernkarten vor (Zweig `helfer-regeln`, Ordner `inhalte/regeln/`) | Lieferung prüfen; Bau in zwei Stufen nach dem Form-Takt (Stufe 1 ohne Server: Übersicht + Karten; Stufe 2 mit Server: Stand je Regel, Wege b und c) → Gegenprüfung → „Live“; **Ansicht für Lehrer und Eltern gehört dazu** (einsehen, bewerten, Änderung verlangen, mit Verweisen): Vorgabe `regeln-lehrer.md` |

## Zurückgestellt (vom Nutzer so entschieden) – später wieder vorlegen
- **„Später noch einmal“-Knopf** (Vorschlag 3 des Mathe-Profis): später. Risiko: alles Schwere wird weggeklickt.
- **Alle drei Arten für „sitzt“** (Vorschlag 4: rechnen, verstehen, anwenden je einmal): nach dem Bau des Form-Takts entscheiden.
- Umbau Übungsbildschirm (Vorgabe ÜB), Bruchstrich-Taste, Schalter „am Tisch / nur Handy“, Zeichnen-Aufgaben (Liste des Mathe-Profis über drei Runden), IB-Abweichungen, Brüche mit Zahl vor der Klammer stapeln und die übrigen Schönheitspunkte des Designers zur Bruch-Darstellung.

## Wartet auf den Nutzer
- Blick am echten Gerät auf Brüche und Tabellen (iPhone/iPad), Foto bei Auffälligkeiten.
- Ob `docs/REISEPLAN.md` (private Reise-Einzelheiten) öffentlich bleiben soll.
- Papier-Test: zweiter Durchgang (Blatt B) in vier bis sechs Wochen, mit zwei Wertungen (nach 40 Minuten / mit Zugabe); Nachtrag (Potenzen, binomische Formeln) liegt bereit.

## Stand 27.11., nach Gegenprüfung Werkstatt 1030–1032
- **Brüche 0.93.8: „Muss vorher“.** Rest des Hochzahl-Fehlers bei Zeichen außerhalb der BMP (halbes UTF-16-Paar an den Grenzen). Nachtrag an den App-Helfer; geht mit 0.94.0.
- **FT-S: „Muss vorher“.** Verlangt: zusätzliche Verhaltens-Nachweise im Prüfpaket (fällige sitzende Karte mit `zaehlt = nein`, Filterwirkung, Übergänge), Bearbeitungsstand auch ohne Kartenzeile, abgesicherter Übergang (Pflicht per Schalter aus, bis die App live ist). Helfer auf Zweig `helfer-probe`.
- **Reihenfolge neu:** App 0.94.0 live (abwärtsverträglich) → FT-S einspielen mit Pflicht aus → Pflicht einschalten → Vorrats-Aufgaben einspielen.
- **Sterne bei `zaehlt = nein`:** Gegenprüfung empfiehlt, die normalen Sterne zu lassen (Belohnung getrennt von Nachweis). Entscheidung des Nutzers offen.
- Inhaltsprüfung (1027) noch ohne Antwort. Inhalts-Nachtrag (drei `folge`, sechs Aufgaben ge1, Mischung der Formen) auf Zweig `helfer-inhalt`.
- **Vorrat für alle übrigen Themen (27.11.):** 22 von 95 Einheiten haben Aufgaben in neuer Form. Gemeinsamer Auftrag: `vorrat-auftrag.md` (drei je Lernkarte, Mischung vorgeschrieben, Feld `thema` an jeder Aufgabe). Läuft: Klasse 5 (`helfer-vorrat5`, Ordner `rollend-5`, 58 Lernkarten), Klasse 6 (`helfer-vorrat6`, `rollend-6`, 66), Klasse 8 (`helfer-vorrat7`, `rollend-7`, 65). Beim Mathe-Profi-Chat des Nutzers: Klasse 7 Rest (`rollend-8`, Kürzel K7). Danach offen: Klasse 9, Klasse 10 und IB. Vor dem Einspielen: `rollend-einheiten.json` um diese Einheiten ergänzen (Kennung, höchste Reihenfolge, Lernkarten aus der Datenbank).
- **Entscheidung des Nutzers 27.11.:** Die Gegenprüfung prüft ALLE neuen Aufgaben, nicht nur Stichproben. Deshalb zuerst nur die Jahrgänge, die jetzt gebraucht werden: Klasse 5 (`rollend-5`) und Klasse 8 (`rollend-7`). Klasse 6 angehalten (Zweig `helfer-vorrat6`, nichts übernommen), Klasse 7 nicht an den Mathe-Profi gegeben; Klasse 6, 7, 9, 10 und IB später.
- **Berichtigung Regel-Universum (27.11.):** Dem Nutzer wurden irrtümlich die Bilder der am 26.11. abgelehnten Fassung `regeln-sonnensystem/` als „A/B“ gezeigt; sein „Variante A“ bezog sich darauf und gilt NICHT als Entscheidung. Gültig ist `inhalte/design/gesetzbuch/` (sechste Runde, A „Aufbau von innen nach außen“ / B „Durch die Klassen“). Die Lieferung des Helfers auf `helfer-regeln` (15 Regeln nach der abgelehnten Vorgabe) wird nicht übernommen; brauchbar daraus: Befund zur Rückmeldung (Aufruf ohne Einheit geht, `bezug` nur aus fester Liste → Stufe 1 über „allgemein“ mit Kennung im Text) und die Idee der Zuordnung Regel → Lernkarten. Vor jedem Zeigen von Entwürfen: Kopf der `umsetzung.md` auf „ABGELEHNT“ prüfen.
