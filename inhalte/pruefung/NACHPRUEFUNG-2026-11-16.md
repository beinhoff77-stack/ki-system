# Nachprüfung lernen-app 0.74.0 (Stand origin/lernen-app 973ac27, 2026-11-16, ergänzt um Test-Ablauf, Tablet, Klasse 8)

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
| N1 | **Bildergeschichte wiederholt gleiche Bilder; Neues ist nicht hervorgehoben.**<br>• Etappe „Was bedeutet eine negative Zahl?“: Einstiegsbild plus drei fast gleiche Thermometer; 3 057 px auf dem Handy.<br>• Kl. 8 „Kerze“: fünfmal derselbe Graph. Neu ist je Schritt nur ein kleiner Punkt „Start“ oder ein winziges Steigungsdreieck.<br>• Ursache im Code: `lernErklaerung` zeichnet den Bildzustand bei **jedem** Schritt.<br>• Betroffen: 413 von 443 umgebauten Etappen (mindestens ein Schritt ohne Bildänderung).<br>Bilder: `nach/bilder/n1-*.jpg` | • Bild nur zeigen, wenn es sich gegenüber dem zuletzt gezeigten Bild (auch Einstiegsbild) ändert; sonst nur der Text.<br>• Was in diesem Schritt neu ins Bild kommt, in der Akzentfarbe und kräftig zeichnen (Punkte, Bögen, Steigungsdreieck mindestens 2 Einheiten breit). |
| N2 | **„Kurz gesagt“ in der Übersicht abgeschnitten** („Unter null schreibst du ein Minus…“). | Ganz zeigen (Regel: ≤ 12 Wörter) oder zweizeilig ohne „…“. |
| N3 | **Kurs-Grafik zeigt noch „2 4 ,“** (Komma ohne Nachkommastellen), Rest von V11. | Komma nur zeigen, wenn eine der beiden Zahlen Nachkommastellen hat. |
| N4 | **Startknopf „Erst wiederholen · ROM ›“.** Ziel und Handlung passen nicht zusammen (die Wiederholung kann aus einem anderen Ort stammen). | „Erst 1 Wiederholung ›“, danach „Weiter nach Rom ›“. |
| N6 | **Test-Seiten zeigen den Ortstitel statt des Flugs** („Rom: Natürliche und ganze Zahlen“). Ursache: `ctx.titel` nimmt `ort_titel` (`viewLernEinheit`). | Im Kopf „Rom · Flugname“ wie im Erklären-Reiter. |
| N7 | **Testergebnis:**<br>• „Zum Flug“ und „Zur Reise“ erscheinen im neuen Design als ungestaltete Textlinks (Klassen `btn primary/secondary`).<br>• Es gibt keinen Knopf „Verbessern“, obwohl der Text dazu auffordert.<br>• Beim Zahlenstrahl ist die richtige Markierung nicht eingezeichnet.<br>Bild: `nach/bilder/n7-testergebnis-handy.jpg` | • Knöpfe im Abflug-Stil.<br>• Bei „noch üben“ ein Hauptknopf „Erst üben: Zahlenstrahl ›“ und danach „Verbessern ›“.<br>• Richtige Markierung grün einzeichnen. |
| N8 | **Bildergeschichte auf dem Tablet zerfällt:** Nummer links, Bild rechts, der Text steht darunter in einer schmalen Spalte – Bild und Text gehören nicht sichtbar zusammen. Bild: `nach/bilder/n8-bildergeschichte-tablet.jpg` | Tablet/Rechner: je Schritt eine Zeile mit Bild links und Text rechts daneben, oder Bild links mitlaufend und Schritte rechts. |
| N5 | **Fehler-Detektiv passt weiter oft nicht** (Kl. 8: Auswahl „parallel“ → Text über „senkrecht“). Bekannt, geplant als R4 nach Auswertung echter Fehler. | Bis dahin den Detektiv nur zeigen, wenn kein Fehlermuster erkannt wurde **und** der Flug in Klasse 5/6 ist (einfache Fehlertexte), oder ganz weglassen. |

## Zur neuen Regel „6 Punkte + schwere Bordkarte“ (Schätzung, kein Fehler)

Annahme: Eine Bordkarte wird im ersten Versuch zu 70–90 % gelöst, eine schwere zu 50–70 %; der zweite Versuch gelingt in 70 % der Fälle. Mit +1 je Treffer und −2 bei zwei Fehlversuchen ergibt eine einfache Simulation im Mittel **9–14 Bordkarten je Etappe**. Ein Flug mit 7 Etappen kommt damit auf etwa 60–100 Bordkarten (vorher etwa 30–40). Vorschlag: In der Eltern-Ansicht „Bordkarten bis ‚sitzt‘“ je Etappe anzeigen und nach den ersten echten Wochen prüfen, ob es für Klasse 5 zu lang wird.

Skripte dieser Nachprüfung: `inhalte/pruefung/nach/nachstellen-v074.test.cjs` (Rückmeldung, an die neue Serverlogik angepasst) und `inhalte/pruefung/nach/test-ablauf.test.cjs` (Test-Ablauf). Beide sind gegen eine Arbeitskopie von `lernen-app` zu starten.
