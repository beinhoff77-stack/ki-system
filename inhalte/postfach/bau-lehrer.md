# Postfach bau-lehrer (Bau-Chat, Bau-Auftrag LA – Lehrer-Aufbau)

Neueste oben. Zweig `bau-lehrer` von `lernen-app` (b8f910e). Kein Merge.

## 2026-11-18 – FERTIG: Auftrag LA (LA-1 bis LA-7) – App 0.80.0

Zweig `bau-lehrer` (von `lernen-app` b8f910e), kein Merge. Reihenfolge wie verlangt: LA-1 → LA-2 → LA-6 → LA-3 → LA-5 → LA-4 → LA-7; je Paket eine Meldung unten.
- **Migrationen** (nur als Datei, nicht ausgeführt, unabhängig von Auftrag H einspielbar – andere Ersetz-Stellen): `20261119_la_3_besprochen.sql`, `20261119_la_4_kann_schon_fluege.sql`;
  Rauchtests `supabase/tests/la_3_rauchtest.sql`, `la_4_rauchtest.sql`. Keine neue Aktion in `lernen-api`, kein DROP, kein DELETE.
- **App 0.80.0**; ohne die Migrationen läuft alles, nur „Besprochen ✓“ meldet „geht, sobald die Datenbank dafür bereit ist“ und „kann schon“ je Flug zeigt einen Hinweis statt Häkchen.
- **Tests:** lernen 80 von 80; Suche: dieselben 9 alten Fehler wie auf lernen-app (Reisen/PWA, nicht Lernen).
- **„Fertig, wenn“:** Tablet-Startseite mit „Zu tun“ und Tabelle ohne Rollen ✓ · Kind B mit 0 Lerntagen rot ✓ · Startseite → falsche Antworten einer wackelnden Etappe: 1 Tipp ✓ ·
  Plan 820 px zweispaltig, Abdeckung sichtbar, „kann schon“ je Flug zählt ✓ · Geschafftes nicht mehr zwischen offenen ✓ · Klasse/Stufen/Notizen nur im ⚙-Blatt ✓ · Lehrplan Gym 5 (14 Flüge) auf einem Tablet-Bildschirm ✓ (je eigener Test).
- **Bilder** (Mock-Daten): `docs/previews/la/` – la2-start-*, la1-ueberblick-*, la6-blatt-*, la3-wackelt-*, la4-plan-*, la5-geschafft-820, la7-lehrplan-* (820 / 400 / 1280).
- **Offen / nicht gebaut:** „Pausen/Reisetage“ als Ausnahme für rot (gibt es noch nicht, Abweichung 4); Ampel für die Stand-Zellen (bewusst weggelassen, s. LA-2);
  „Kurz gesagt“ in allen Themen-Dateien vorhanden? – nicht geprüft (Inhalts-Chats).

## 2026-11-18 – FERTIG: LA-7 Nachschlagen (7A)

- Lehrplan-Übersicht `#/lehrplan` als **kompakte Tabelle**: oben Reiter Gymnasium · Realschule · IB MYP, Klassen-Knöpfe mit Marken der Kinder (Klasse des Kindes: Buchstabe, z. B. „A“, „B“), „alle Klassen“, Suche, „⛰ Expeditionen ansehen“.
- Eine Zeile je Flug: Flug · Ort · andere Schularten · Inhalt (● fertig, ◐ in Prüfung, ○ fehlt; Punkte als Formen, nicht Schriftzeichen) · Stand je Kind (Spalte je Kind, „· im Plan“).
  Zeilen nach Klasse und Kontinent gruppiert. Zeile antippen → „Inhalte ansehen“; fehlt der Inhalt, steht klein „✎ Ändern lassen“ (Auftrag „Neuer Flug“ wie bisher).
- Vorbelegt mit Schulart und Klasse des ersten Kindes; Zähler (Flüge · fertig · in Prüfung · fehlt) sind zugleich Filter.
- Ziel „eine Klasse passt auf einen Tablet-Bildschirm“: Test mit 14 Flügen Gym 5 bei 820 × 1180 ✓. Info-Seite: Abschnitt zur Lehrplan-Übersicht angepasst.
- Bilder: `la7-lehrplan-820.png`, `la7-lehrplan-400.png`, `la7-lehrplan-1280.png`.

## 2026-11-18 – Zwischenmeldung nach LA-4 (Bilder)

`docs/previews/la/`: Plan Tablet 820 px `la4-plan-820.png` (zwei Spalten, Rom aufgeklappt, „kann schon“ je Flug), Handy 400 px `la4-plan-400.png`, Rechner `la4-plan-1280.png`,
Block „Geschafft“ `la5-geschafft-820.png`. Mock-Daten, keine Kinderdaten.
„Fertig, wenn“: Plan auf dem Tablet in zwei Spalten ✓ (Test misst es); Abdeckung der Klasse sichtbar ✓; „kann schon“ je Flug zählt im Stand ✓ (Server: thema_stand/ort_stand; App: Stand-Modell, Abflugtafel);
geschaffte Orte nicht mehr zwischen offenen ✓; Klasse, Stufen, Notizen nur im ⚙-Blatt ✓.

## 2026-11-18 – FERTIG: LA-4 Flugplan (4A)

**Migration** `supabase/migrations/20261119_la_4_kann_schon_fluege.sql` (nicht ausgeführt; pglast ok; alle Ersetz-Stellen im Live-Text je genau einmal; kein DROP, kein DELETE; Kollisions-Prüfung ohne Treffer):
- `route.kann_schon_themen bigint[]` (Abweichung 3), entsprechend `ausgelassen`. `schule_plan_setzen` nimmt `eintraege[].kann_schon_themen` (fehlt es, bleibt die Liste; Flug muss zum Ort gehören);
  wird „kann schon“ in einem fertigen Ort zurückgenommen, prüft der Server den Ort wie bei „ausgelassen“ und macht ihn ggf. wieder offen – **Rückgängig ohne Verlust**.
- Zählt wie gelandet in `thema_stand` (Lehrplan-Übersicht, Konto) und `ort_stand` (Ort-Abschluss → Status „fertig“, Stempel wie bisher), **nicht** als `karte_stand.sitzt` → keine Mischkarten, Wiederholungen, Expeditionen daraus.
  Neue Hilfsfunktion `schule.thema_kann_schon` (Flug einzeln oder ganzer Ort). `schule_plan_lesen`: `plan[].kann_schon_themen`, `themen[].kann_schon`; `schule_uebersicht`: `route[].kann_schon_themen`.
- Das bisherige „kann schon“ des ganzen Orts bleibt („alle Flüge: kann schon“).
- Rauchtest `supabase/tests/la_4_rauchtest.sql` (Rollback, Testkind): ein Flug → thema_stand erledigt; alle Flüge → Ort abgeschlossen, keine Karte angelegt; zurückgenommen → wie vorher; wdh_in.

**App (Reiter „Plan“):**
- Zwei Spalten ab 700 px (Tablet hochkant eingeschlossen), Handy untereinander. Kopf „Gymnasium Kl. 5 · n offen · n geschafft · Gespeichert · ↶ Rückgängig“.
- Links nur offene Orte (Griff ⠿, ↑ ↓; Ziehen/Pfeile bewegen zwischen den offenen, die Lernreise-Reihenfolge der geschafften bleibt).
- Ort aufgeklappt: je Flug „im Plan“ (links), Klassen, Stand, rechts „kann schon“ je Flug (erst wenn die Datenbank das Feld liefert; vorher Hinweis), „ansehen“; Flug einer höheren Klasse: „Gym 6 – höhere Klasse“ (L9).
- Rechts der Lehrplan: Reiter Gymnasium · Realschule · IB MYP, Klassen-Knöpfe (vorbelegt mit Klasse/Stufe des Kindes, „alle“), Zeile „Klasse 5: n von m Flügen im Plan“ mit Balken,
  alle Orte der Klasse: eingeplante mit ✓ (grau, „im Plan“), fehlende mit ⠿ und „+“; Suche bleibt.
- „Kann schon“ je Flug in der App: Stand (Lernstand-Modell, eigener Zustand „kann schon“), Abflugtafel des Kindes (Gruppe „konnte ich schon“), Überblick „Zuletzt geschafft“.
- Tests: LA-4 ×2 (zwei Spalten, Abdeckung, ✓, „kann schon“ speichert `kann_schon_themen`, Hinweis höhere Klasse, Stand-Modell).

## 2026-11-18 – FERTIG: LA-5 Geschafftes (5A)

- Geschaffte Orte (Status „fertig“, ganzer Ort „kann schon“ oder alle geplanten Flüge gelandet/„kann schon“) stehen nicht mehr im Plan, sondern darunter im **zugeklappten** Block „Geschafft (n)“.
- Je Flug: Ort · Flug · gelandet am (letzte Landung, aus `schule_lernstand`; bei „kann schon“ ohne Landung: „kann schon“) · Nachtest (aus `schule_merkheft`: bestanden / fällig / fällig in n Lerntagen)
  · nächste Wiederholung (neu `wdh_in` je Etappe, Migration LA-4; „jetzt fällig“ / „in n Lerntagen“; ohne Migration „–“).
- Überblick: die letzten 3 geschafften Flüge als Zeile (seit LA-1; jetzt mit „kann schon“-Flügen hinten, ohne Datum).
- Reihenfolge der Lernreise unverändert; nur die Anzeige trennt Offen und Geschafft. Als Liste statt Tabelle (in der linken Spalte des Tablets ist eine 5-spaltige Tabelle zu schmal).
- Test LA-5 (Ort fertig → nicht in der Liste, „Geschafft (1)“ zugeklappt, Werte je Flug). Tests gesamt: lernen 79 von 79.

## 2026-11-18 – FERTIG: LA-3 Was wackelt (3B)

**Migration** `supabase/migrations/20261119_la_3_besprochen.sql` (nicht ausgeführt; pglast ok; Ersetz-Stellen im Live-Text je genau einmal geprüft; kein DROP, kein DELETE; Skript-Prüfung auf Variable/Alias-Kollisionen ohne Treffer):
- Neue Tabelle `schule.besprochen` (Kind, Einheit, Lernkarte, von, am; eine Zeile je Kind + Etappe, RLS an wie die übrigen schule-Tabellen).
  `schule.besprochen_aktiv(…)`: gilt, solange danach keine **endgültig** falsche Antwort in der Etappe kam (1. Versuch mit zweiter Chance zählt nicht).
- Setzen über die **bestehende** Aktion `schule_notiz_setzen` mit `{lernender_id, besprochen: {einheit_id, lernziel}}` – keine neue Aktion in `lernen-api`. Lehrer und Eltern (ist_leiter), Zugriff auf das Kind geprüft.
- `schule_lernstand` je Etappe neu: `regel` („Kurz gesagt“), `besprochen_am`/`besprochen_von` (nur gültig), `fehler_gruende` {grund: Anzahl}; in `fehler[]` je Antwort `grund`.
  `grund` wird – wie beim Prüfen – aus der gespeicherten Antwort berechnet (`antwort_bewerten`); in `versuch` gibt es keine Spalte dafür.
- Rauchtest `supabase/tests/la_3_rauchtest.sql` (Rollback, Testkind): besprochen aktiv → 1. Versuch falsch bleibt → endgültig falsch holt zurück; Fehlerarten als Objekt.

**App:** Reiter „Was wackelt“ = Kopfzeile „Diese Woche: n Bordkarten, n richtig · n Lerntage“, dann **eine Tabelle** aller Etappen mit Fehlern (wackelt zuerst, dann nach Datum): Etappe (Ort darunter) · richtig / falsch · häufigster Fehler · seit.
- Häufigster Fehler nur, wenn ein `grund` bei mindestens zwei falschen Antworten vorkommt, sonst „–“ (Abweichung 5). Keine Aussage, wie das Kind gerechnet hat.
- „seit“ = Datum der ältesten der (bis zu 3) gespeicherten letzten falschen Antworten – schlichteste Lösung; die Datenbank liefert keinen „wackelt seit“.
- Zeile antippen: letzte 3 falsche Antworten (Bordkarte · Antwort · richtig), „Kurz gesagt“, „Erklärung ansehen ›“, „Besprochen ✓“. Danach Marke „besprochen 18.11.“, Etappe fällt aus „Zu tun“.
  Ohne Migration meldet der Knopf „‚Besprochen‘ geht, sobald die Datenbank dafür bereit ist.“
- Gelber „Zu tun“-Eintrag öffnet die Etappe schon aufgeklappt → **1 Tipp** von der Startseite zu den falschen Antworten (Ziel: höchstens 2).
- Regelblock „Was kommt wann wieder?“ entfällt hier (steht auf „So funktioniert’s“ unter „Wie wird gelernt?“). Der bisherige Stand je Etappe steht zugeklappt unter „Alle Etappen mit Stand“.
- „Kurz gesagt“ fehlt in keiner Etappe der Themen-Dateien? – nicht geprüft (Inhalts-Chats); fehlt `regel`, entfällt die Zeile.
- Bilder: `docs/previews/la/la3-wackelt-820.png`, `la3-wackelt-400.png`. Info-Seite: Eintrag „Was wackelt“. Tests: lernen 76 von 76.

## 2026-11-18 – FERTIG: LA-6 Einstellungen (6B)

- „⚙ Einstellen“ (mit Text) in der Tabellenzeile/Karte der Startseite und im Kopf der Kind-Seite öffnet ein Blatt „Kind A einstellen“ – Tablet/Rechner von rechts, Handy von unten; Esc, × oder Tippen daneben schließt.
- Karten, alles speichert sofort (`schule_kind_setzen`, `schule_notiz_setzen`, `schule_plan_setzen` – keine neue Aktion, keine Migration):
  1. Schule: Hauptschulart (Knöpfe) und Klasse (Knöpfe 5–10) – „Bestimmt seine Klasse in Lernreise und Plan.“
  2. Stand messen gegen …: Stufe je Schulart (Gym, RS, IB MYP; „aus Klasse (…)“, IB unter Klasse 6 „noch kein MYP-Jahr“) – „Nur für die Anzeige ‚Wo steht es?‘ – ändert nichts an der Lernreise.“
  3. Notizen und Verlauf (zugeklappt).
  4. Neuer Plan aus Lehrplan-Vorlage – **mit Rückfrage** („Ja, Plan ersetzen“ / „Abbrechen“), danach „↶ Rückgängig“ im Blatt.
- Der Plan zeigt Vorlage, Klasse, Stufen, Notizen, Verlauf nicht mehr. Schließen nach einer Änderung zeichnet die Seite neu.
- Schlichteste Lösung, wo der Text offen ist: Klasse als Knöpfe 5–10 (die Datenbank nimmt 1–13; andere Werte bleiben erhalten, solange niemand einen Knopf drückt).
- Bilder: `docs/previews/la/la6-blatt-820.png`, `la6-blatt-400.png`. Info-Seite: Abschnitt „⚙ Einstellen“. Tests: lernen 74 von 74.

## 2026-11-18 – Zwischenmeldung nach LA-2 (Bilder)

Bilder (Mock-Daten, keine Kinderdaten) in `docs/previews/la/`:
- Startseite Tablet 820 px: `la2-start-820.png` · Handy 400 px: `la2-start-400.png` · Rechner 1280 px: `la2-start-1280.png`
- Überblick der Kind-Seite Tablet: `la1-ueberblick-820.png` · Handy: `la1-ueberblick-400.png`

Prüfpunkte aus „Fertig, wenn“: Tablet – „Zu tun“ und Kinder-Tabelle ohne Rollen sichtbar (Test misst es); Kind B mit 0 Lerntagen ist rot (Zeile und „Zu tun“).

## 2026-11-18 – FERTIG: LA-2 Startseite (2B)

- **Zu tun** oben, rot → gelb → blau, je Eintrag ein Link:
  rot = letzter Lerntag ≥ 3 Kalendertage zurück oder keiner in 4 Wochen (→ Überblick), offene automatische Rückreise (= Nachtest unter 60 %, → Plan);
  gelb = Etappe wackelt (≥ 3 falsch und mehr falsch als richtig, oder wieder offen) und nicht besprochen (→ Was wackelt; „besprochen“ kommt mit LA-3);
  blau = Antwort auf einen Auftrag in den letzten 7 Tagen (→ Meine Aufträge). Leer: „Alles ruhig.“
- **Tabelle** je Kind: Kind (Name, Schulart Kl.) · Lernt · Wackelt · GYM · RS · IB (Stufe und Prozent, Rechenregel K3) · Jetzt · Knöpfe. Zeile antippen → Überblick des Kindes.
  Farbe nur bei Lernt (rot ≥ 3 Tage, gelb 2 Tage, sonst grün) und Wackelt (rot Rückreise, gelb offene wackelnde Etappe, sonst grün).
  **Stand-Zellen ohne Ampel** (schlichteste Lösung, Entwurf liegt nicht vor): Mitte des Schuljahrs wären fast alle Prozentwerte „rot“, das wäre irreführend.
- **Handy < 560 px:** je Kind eine Karte mit denselben Feldern.
- **„Lernen starten“** (Abweichung 1): Rolle Eltern – in jeder Zeile/Karte und im Kopf der Kind-Seite; Rolle Lehrer – entfällt, im Kopf klein „Lernreise ansehen ›“.
  Rolle: Lern-Seite aus `schule_ich`; die ganze App ist der Eltern-Zugang.
- **IB unter Klasse 6:** überall „noch kein MYP-Jahr“ (statt „vor MYP-Jahr 1 · 0/0“), auch in Abflugtafel, Stand und Info-Seite.
- „Eingetragene Pausen/Reisetage“ gibt es noch nicht – rot gilt ohne diese Ausnahme (Abweichung 4).
- Daten: je Kind `schule_lernstand` (Lerntage 4 Wochen, Woche, Etappen) – keine neue Aktion, keine Migration.

## 2026-11-18 – FERTIG: LA-1 Gliederung (1A)

- Startseite `#/lernen` (Eltern/Lehrer) = „Was ist los?“: Zu tun · Kinder-Tabelle · Zeile „Nachschlagen“ (Lehrplan · Expeditionen · Meine Aufträge · So funktioniert’s); darunter „Verwalten“
  (Testkind, Zugänge nur Eltern, eigene Lernen-Seite) und für Eltern die Belohnungen. „So funktioniert’s“ zusätzlich oben rechts.
- Neue Kind-Seite `#/kind/<id>-<reiter>` mit Reitern **Überblick · Was wackelt · Stand · Plan**. Kopf: Name, Schulart/Klasse, „⚙ Einstellen“ (bis LA-6: öffnet den Plan),
  „Lernreise ansehen“ (Lehrer) bzw. „Lernen starten“ (Eltern), „So funktioniert’s“.
- Alte Adressen `#/lernstand/<id>[-…]`, `#/wackelt/<id>`, `#/plan/<id>` leiten auf den Reiter um (auch mit Schulart/Ebene: `#/lernstand/1-gym_by-7` → `#/kind/1-stand-gym_by-7`).
- **Überblick:** Lernt es? (Lerntage diese Woche, zuletzt, Bordkarten 7 Tage) · Wo hakt es? (bis 3 wackelnde Etappen, Rückreise) · Wo steht es? (drei Schularten, Prozent) · Was kommt? (Jetzt) · Zuletzt geschafft (3 Flüge mit Datum der letzten Landung).
- „Alle Kinder im Vergleich“ (`#/schulstand`) bleibt erreichbar, ist aber nicht mehr verlinkt.
- Plan-Kopf jetzt eine Zeile („Gymnasium Kl. 5 · 10 offen · 2 geschafft · Gespeichert · ↶ Rückgängig“) – sonst passten 12 Orte unter Kopf und Reitern nicht mehr auf das Tablet.
- Info-Seite: Startseite, Seite des Kindes, „Lernen starten“ je Rolle; Erste Schritte verlinken die Reiter.
- Tests: lernen 73 von 73 (neu LA-1, LA-2 ×4; angepasst: Wege über die Kind-Seite, IB-Beschriftung, Ziehen mit Kopf).
