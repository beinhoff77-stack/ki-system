# Umsetzung Lehrer-Aufbau (Auswahl Sebastian, 2026-11-18)

Grundlage: `bericht.md` (Befunde L1–L9, App 0.78.1) und der Auswahl-Entwurf „Lehrer-Ansicht: neuer Aufbau“ (Artifact).
Auswahl: 1A · 2B · 3B · 4A · 5A · 6B · 7A.

Reisewörter wie gehabt: Flug = Thema, Etappe = Lernkarte, Bordkarte = Aufgabe, Kontinent = Gebiet.

## Zusammenspiel (von mir aufgelöst)

1A sieht eine Kind-Seite mit Reiter „Einstellungen“ vor, 6B ein Zahnrad. Umgesetzt wird: **Kind-Seite mit 4 Reitern** (Überblick · Was wackelt · Stand · Plan), **Einstellungen nur über ⚙**: in der Tabellenzeile des Kindes auf der Startseite und im Kopf der Kind-Seite.

## LA-1 Gliederung (1A)

- Startseite `#/lernen` (Lehrer/Eltern) = „Was ist los?“: Zu tun · Kinder-Tabelle · Zeile „Nachschlagen“.
- Neue Kind-Seite `#/kind/<id>-<reiter>`, Reiter `ueberblick | wackelt | stand | plan`. Bisherige Routen `#/lernstand/<id>`, `#/wackelt/<id>`, `#/plan/<id>` leiten auf den passenden Reiter um (alte Links bleiben gültig).
- Kopf der Kind-Seite: Name, Schulart/Klasse, ⚙, „Lernreise ansehen“ (klein).
- Reiter **Überblick**: die vier Fragen (Lernt es? · Wo hakt es? · Wo steht es? · Was kommt?) und die letzten 3 geschafften Flüge.
- „Alle Kinder im Vergleich“ (`#/schulstand`) entfällt als eigene Karte; der Vergleich steht in der Tabelle der Startseite. Die Seite selbst darf bleiben, wird aber nicht mehr verlinkt.
- Zeile „Nachschlagen“ unten auf der Startseite: Lehrplan · Expeditionen · Meine Aufträge · So funktioniert’s. „So funktioniert’s“ bleibt zusätzlich oben rechts.

## LA-2 Startseite (2B)

- Oben **Zu tun**, Reihenfolge rot → gelb → blau, je Eintrag ein Link:
  - rot: letzter Lerntag liegt 3 oder mehr Kalendertage zurück (außer in eingetragenen Pausen/Reisetagen) → Überblick des Kindes; automatische Rückreise / Nachtest nicht bestanden → Plan des Kindes.
  - gelb: Etappe wackelt und noch nicht „besprochen“ → Reiter „Was wackelt“.
  - blau: neue Antwort auf einen Auftrag → Meine Aufträge.
  - Leer: „Alles ruhig.“
- Darunter **Tabelle**, eine Zeile je Kind: Kind (Name, Schulart Kl.) · Lernt (Lerntage diese Woche, zuletzt) · Wackelt (Anzahl, „Rückreise“) · GYM · RS · IB (Klasse/MYP-Jahr und **Prozent**, Rechenregel wie K3) · Jetzt · ⚙. Zelle rot/gelb/grün wie im Entwurf. Ganze Zeile antippen → Kind-Seite, Reiter Überblick.
- Handy (< 560 px): statt Tabelle je Kind eine kompakte Karte mit denselben Feldern (Tabelle ist dort zu eng – Minus-Punkt aus dem Entwurf).
- „Lernen starten“ entfällt auf der Lehrer-Startseite (bleibt für das Testkind/Kind selbst).
- IB bei Kindern unter Klasse 6: „noch kein MYP-Jahr“ statt „vor MYP-Jahr 1 · 0/0“.

## LA-3 Was wackelt (3B)

- Reiter „Was wackelt“: eine Tabelle über alle Etappen mit Fehlern, sortiert: wackelt zuerst, dann nach Datum.
  Spalten: Etappe (Ort darunter) · richtig / falsch · häufigster Fehler · seit.
- „Häufigster Fehler“ aus dem Feld `grund` der Antworten (vorzeichen, komma, vertauscht, gerundet, falsche_einheit) in Worten, mit Anzahl; ohne `grund`: „–“.
- Zeile antippen klappt auf: die letzten 3 falschen Antworten (Aufgabe · Antwort des Kindes · richtig) **und** der „Kurz gesagt“-Satz der Etappe (gleicht das Minus „Regel fehlt“ aus), dazu „Erklärung ansehen ›“ und „Besprochen ✓“.
- „Besprochen ✓“ (neu, Datenbank nach W1–W7): speichert Datum und Person je Kind + Etappe; die Etappe verschwindet aus „Zu tun“, bleibt in der Tabelle mit „besprochen 18.11.“. Neue falsche Antworten danach holen sie zurück.
- Kopfzeile: „Diese Woche: 30 Bordkarten, 22 richtig · 3 Lerntage“. Der Regelblock „Was kommt wann wieder?“ wandert auf „So funktioniert’s“.

## LA-4 Flugplan (4A) = Reiter „Plan“

- Zwei Spalten ab 700 px (Tablet hochkant eingeschlossen), Handy untereinander.
- Links der Plan: nur offene Orte, eine Zeile je Ort, Griff ⠿, ↑ ↓, Kopf „Gymnasium Kl. 5 · 10 offen · 2 geschafft · Gespeichert · ↶ Rückgängig“.
- Ort aufklappen: eine Zeile je Flug mit „im Plan“ (Häkchen links), Klassen, Stand und rechts **„kann schon“ je Flug** (neu, Datenbank). „Kann schon“ zählt im Stand als gelandet, wie heute beim ganzen Ort. Das bisherige „kann es schon“ für den ganzen Ort bleibt als „alle Flüge: kann schon“.
- Flug einer höheren Klasse in einem Ort (z. B. Zehnerpotenzen Gym 6 in Rom): Hinweis „Gym 6 – höhere Klasse“ in der Flugzeile (L9).
- Rechts der Lehrplan: Reiter Gymnasium · Realschule · IB, Klassen-Knöpfe, vorbelegt mit der Klasse des Kindes; Zeile „Klasse 5: 13 von 14 Flügen im Plan“ mit Balken; alle Orte der Klasse, eingeplante mit ✓ (grau), fehlende mit ⠿ und „+“.
- Vorlage, Klasse, Stufen, Notizen, Verlauf verlassen diese Seite (→ LA-6).

## LA-5 Geschafftes (5A)

- Geschaffte Orte (und Flüge, die alle gelandet oder „kann schon“ sind) stehen nicht mehr im Plan, sondern darunter im zugeklappten Block „Geschafft (n)“.
- Je Eintrag: Ort · Flug · gelandet am · Nachtest (bestanden / fällig in n Lerntagen) · nächste Wiederholung.
- Im Reiter Überblick die letzten 3 geschafften Flüge als Zeile.
- Die Reihenfolge der Lernreise bleibt unverändert; nur die Anzeige im Plan trennt Offen und Geschafft.

## LA-6 Einstellungen (6B)

- ⚙ in der Tabellenzeile (Startseite) und im Kopf der Kind-Seite öffnet ein Blatt (Tablet/Rechner von rechts, Handy von unten), Titel „Kind A einstellen“.
- Drei Karten, alles speichert sofort:
  1. Schule: Hauptschulart (Reiter) und Klasse (Knöpfe). Satz: „Bestimmt seine Klasse in Lernreise und Plan.“
  2. Stand messen gegen …: Stufe je Schulart (Gym, RS, IB MYP); Satz: „Nur für die Anzeige ‚Wo steht es?‘ – ändert nichts an der Lernreise.“ IB unter Klasse 6: „noch kein MYP-Jahr“.
  3. Notizen + Verlauf (zugeklappt).
- „Neuer Plan aus Lehrplan-Vorlage“ ebenfalls im Blatt, als vierte Karte, mit Rückfrage.
- Das ⚙ bekommt Text: „⚙ Einstellen“ (nicht nur das Symbol – das Zahnrad allein wird übersehen, Minus aus dem Entwurf).

## LA-7 Nachschlagen (7A)

- Lehrplan-Übersicht `#/lehrplan` als kompakte Tabelle: oben Reiter Schulart, Klassen-Knöpfe (Klassen der Kinder markiert „A“, „B“), Suche.
- Eine Zeile je Flug: Flug · Ort · andere Schularten · Inhalt (● fertig, ◐ in Prüfung, ○ fehlt) · Stand je Kind. Antippen → „Inhalte ansehen“.
- Vorbelegt mit der Klasse des ersten Kindes; „alle Klassen“ als Knopf.
- Ziel: eine Klasse passt auf einen Tablet-Bildschirm.

## Wer macht was

| Paket | Wer |
|---|---|
| LA-1 bis LA-7 App | Haupt-Chat |
| „Besprochen ✓“ (LA-3), „kann schon“ je Flug (LA-4) | Haupt-Chat, Datenbank nach W1–W7 |
| „Kurz gesagt“ je Etappe vorhanden? (LA-3) | Inhalts-Chats nur, wo er fehlt |

## Fertig, wenn

- Lehrer-Startseite auf dem Tablet: „Zu tun“ und die Kinder-Tabelle ohne Scrollen sichtbar; Kind B mit 0 Lerntagen ist rot.
- Von der Startseite zu den falschen Antworten einer wackelnden Etappe: höchstens 2 Tipps.
- Plan auf dem Tablet (820 px) in zwei Spalten; Abdeckung der Klasse sichtbar; „kann schon“ je Flug zählt im Stand.
- Geschaffte Orte stehen nicht mehr zwischen offenen.
- Klasse, Stufen, Notizen nur noch im ⚙-Blatt.
- Lehrplan Gym 5 passt auf einen Tablet-Bildschirm.
