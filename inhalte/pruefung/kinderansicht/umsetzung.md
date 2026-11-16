# Aufbau der Kinderansicht – wer macht was (Stand 2026-11-16)

Grundlage: `bericht.md` (Befunde B1–B14, Vorschläge U1–U13). Alles im Zweig `lernen-app`, kein Merge nach `main` ohne Sebastians „Live“.

| Paket | Wer | Inhalt | Fertig, wenn … |
|---|---|---|---|
| **S1 sofort** | Haupt-Chat (App) | U1 Stempel-Band, U2 Themenname statt Ortsname, U3 „Kommt noch“ wie Abflugtafel, U4 Menü im Reisepass, U5 nur eigene Schulart, U6 ein Fortschrittsmaß oben, U8 Rückreise erklären | Rundgang (`rundgang.test.cjs`): Mein Weg zeigt keinen Ort doppelt; „Kommt noch“ bei Klasse 8 ohne Klasse 5–7 und ohne Orte ohne Klasse; Band zeigt für Rom 44 Karten bzw. „1 von 5 Themen“; Thema-Kopf „Gymnasium · Klasse 5“; Reisepass im Menü markiert; Kind B sieht einen Satz zur Rückreise. |
| **S2 danach** | Haupt-Chat (App) | U7 Fokus „jetzt + als Nächstes“, U9 Merkheft nur Geschafftes nach Thema, U13 Startseite entschlacken | „Gerade dran“ = 1 Thema + höchstens 3 „als Nächstes“; Merkheft enthält keine Karte „noch nicht geübt“; Startseite auf dem Handy ≤ 2 Bildschirme. |
| **S3 Umbau** | Haupt-Chat (App), vorher Entwurf | U10 feste Leiste mit 4 Einträgen in beiden Designs, U11 Weltkarte als Ansicht in Mein Weg (eigene Klasse hervorgehoben, Antarktis mit Karte) | Erst ein klickbarer Entwurf zur Freigabe durch Sebastian, dann Umsetzung. |
| **S4 Daten** | Haupt-Chat (Datenbank, Werkstatt-Regeln) nach Entscheidung Sebastian | U12 Klasse von Ort und Thema angleichen (13 Orte), Reihenfolge der Themen im Ort nach Lehrplan | Liste der 13 Orte mit Vorschlag „Ort umziehen“ oder „Klasse korrigieren“ an Sebastian; nach Freigabe eine Migration. |
| **Begriffe** | Haupt-Chat (App) + Inhalts-README | Ort · Thema · Lernkarte · Aufgabe · Gebiet überall gleich; „Etappe“, „Bordkarte“, „Kontinent“ im Kindertext ersetzen | In den Kinderansichten erscheinen „Etappe“ und „Bordkarte“ nicht mehr. |
| – | Sebastian | Entscheidung S3 (Leiste statt ≡, Weltkarte in Mein Weg) und S4 (Klassen der 13 Orte); drei Fragen mit den Kindern ausprobieren (bericht.md, Abschnitt 6) | – |
| – | Prüf-Chat | Nach S1 und S2 Rundgang neu laufen lassen, Ergebnis ins Postfach | – |

**Zusammenspiel:** S1/S2 berühren andere Stellen als die Pakete aus den Prüfungen Erklärungen (A1–A12) und Rückmeldung (R1–R3). Ausnahme: U9 (Merkheft) und A1 (Übersicht der Lernkarten) sollen dieselbe Gliederung Gebiet → Thema → Lernkarte nutzen. Deshalb beides in einer Hand.
