# Postfach bau-lehrer (Bau-Chat, Bau-Auftrag LA – Lehrer-Aufbau)

Neueste oben. Zweig `bau-lehrer` von `lernen-app` (b8f910e). Kein Merge.

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
