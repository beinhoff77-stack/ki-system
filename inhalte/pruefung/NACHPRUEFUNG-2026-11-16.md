# Nachprüfung lernen-app 0.74.0 (Stand origin/lernen-app 973ac27, 2026-11-16)

**Methode**
- Nachstell-Skripte gegen eine Arbeitskopie von `lernen-app`:
  - `rueckmeldung/nachstellen.test.cjs`, angepasst an die neue Serverlogik: zweiter Versuch, Fehlermuster, 6-Punkte-Regel.
  - `kinderansicht/rundgang.test.cjs`, mit Etappen-Ansicht.
- Testdaten wie in den Prüfrunden, Server nachgebaut, keine echten Kinderdaten.

## Umgesetzt (nachgestellt)

| Paket | Ergebnis |
|---|---|
| Erklärungen A1–A12 | Übersicht der Etappen → eine Etappe. Kurzer Text vor dem Bild. Bildergeschichte mit Thermometer. „Pass auf!“ als letzter Schritt mit Bild. Neue Wörter eingeklappt am Ende. Gelbe Markierung. Üben beim ersten Mal nur die Bordkarte plus „Erklärung ansehen“. Thema-Seite 1 418 px statt 7 000–16 000 px. |
| Rückmeldung R1 | Hunderterfeld deutlich sichtbar. Nach einem Fehler kommt eine andere Bordkarte, nicht dieselbe (Szenario R2 findet keine Wiederholung mehr). Wiederholung mit 0/1: kein Haken mehr, ehrlicher Text. Auswahl markiert. Minuszeichen und „−3x − 1“ korrekt. |
| Rückmeldung R2 | Zweiter Versuch mit passendem Hinweis: Vorzeichen, Komma, Einheit, vertauschte Felder. Ohne erkanntes Muster kommt der Tipp. „Das hakt gerade – Beispiel ansehen“ nach Fehlern. |
| Rückmeldung R3 | „Was kommt wann wieder?“ auf Startseite und Wiederholen. |
| Kinderansicht K1 | Flugnamen statt Ortsnamen in Mein Weg. Etappe/Bordkarte/Flug durchgehend. Stempel-Band „Noch 29 Etappen bis zum Stempel von Rom (5 Flüge)“. Menü markiert richtig. Flug-Kopf „Gymnasium · Klasse 5“. „Kommt noch“ ohne frühere Klassen. Karte „Kurz zurück nach Delhi“ mit Grund. |
| Zusätzlich (nicht aus den Prüfrunden) | Etappe sitzt nach 6 Punkten und einer schweren Bordkarte (Fehler −2). Die Info-Seite (E-1) muss diese Regel übernehmen; der Entwurf `eltern/info-seite.md` sagt noch „2–4“. |

## Noch offen (laut Gesamtauftrag Phase 2/3, nicht als Fehler gewertet)
- K2: Mein Weg nach Kontinenten, Karte in Mein Weg. Merkheft nur Geschafftes; heute noch 13 951 px mit „noch nicht geübt“.
- K3/K4: Stand mit Mini-Linien, Eltern-Ansicht.
- E-1 bis E-4: Eltern- und Lehrerseite.

## Neue Befunde

| Nr. | Befund | Vorschlag |
|---|---|---|
| N1 | **Bildergeschichte wiederholt gleiche Bilder.** Etappe „Was bedeutet eine negative Zahl?“: Einstiegsbild plus drei fast gleiche Thermometer (−3 °C) in Schritt 1–3; Etappe auf dem Handy 3 057 px. | Bild nur zeigen, wenn es sich gegenüber dem vorigen Schritt ändert. Sonst nur der Text mit kleinem Verweis „(Bild wie oben)“. Tablet: Bild links mitlaufend. |
| N2 | **„Kurz gesagt“ in der Übersicht abgeschnitten** („Unter null schreibst du ein Minus…“). | Ganz zeigen (Regel: ≤ 12 Wörter) oder zweizeilig ohne „…“. |
| N3 | **Kurs-Grafik zeigt noch „2 4 ,“** (Komma ohne Nachkommastellen), Rest von V11. | Komma nur zeigen, wenn eine der beiden Zahlen Nachkommastellen hat. |
| N4 | **Startknopf „Erst wiederholen · ROM ›“.** Ziel und Handlung passen nicht zusammen (die Wiederholung kann aus einem anderen Ort stammen). | „Erst 1 Wiederholung ›“, danach „Weiter nach Rom ›“. |
| N5 | **Fehler-Detektiv passt weiter oft nicht** (Kl. 8: Auswahl „parallel“ → Text über „senkrecht“). Bekannt, geplant als R4 nach Auswertung echter Fehler. | Bis dahin den Detektiv nur zeigen, wenn kein Fehlermuster erkannt wurde **und** der Flug in Klasse 5/6 ist (einfache Fehlertexte), oder ganz weglassen. |
