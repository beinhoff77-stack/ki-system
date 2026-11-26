# Lehrplan beider Kinder: Entscheidung des Nutzers (26.11.2026)

Vorschlag des Mathe-Profis: `inhalte/mathe-profi/lehrplan-kinder/` auf `origin/mathe-profi` (Commit 24ad0fd3; `nutzer-seite.md`, `route.md`, `einstell-liste.md`, `README.md`, `plan.py`).
**Stand: eingestellt am 26.11.2026 auf den Satz des Nutzers „Lehrplan für beide Kinder einstellen“.**

## Entschieden
1. Die bei Kind 2 herausgenommenen Pflicht-Flüge kommen zurück in den Plan (`r4`, `r2`, `d5`, `ge4`, `ge5`, `d10`).
2. Kind 2 schreibt einen ganzen amtlichen Jahrgangsstufentest der Klasse 8 auf Papier als Eingangsdiagnose für den Stoff der Klassen 5 bis 7. Zweck: Lücken finden, nicht die App messen. (Der zugeschnittene Papier-Test aus Auftrag 5 bleibt daneben bestehen.)
3. Kind 1: Vorgriff auf die drei Themen, die die Realschule früher hat.
4. Kind 2: Klasse 9 steht als Abschnitt 5 am Ende des Plans; er beginnt erst nach dem Abschluss von Klasse 8.
5. Kind 1: Zinsen (`g4`) wird Kür.
6. Grundsatz: Reihenfolge im Wechsel, höchstens zwei Rechen-Flüge hintereinander.

## Vor dem Einstellen
- Gegenprüfung durch ChatGPT (Werkstatt).
- Einstellen über die vorhandene Plan-Funktion der App (`schule.route`, Weg von `api.schule_plan_setzen`), damit Verlauf und Revision stimmen; kein direktes Überschreiben. Probelauf mit Rollback, Vergleich vorher/nachher je Kind.
- Prüfen: Führt die App `r2` mit ausgelassenem Thema sauber? Was geschieht mit laufenden Etappen und Wiederholungen beim Umstellen der Plätze?
- Kein Kind übt in den 30 Minuten davor.
- Ausdrücklicher Satz des Nutzers.

## Getrennt zu klären (ändert die Reihenfolge nicht)
Vier Widersprüche zwischen `inhalte/themenliste.json` und App (`geometrie.winkel`, `finanzen.zinsen`, `zahlen.intervalle`, `stochastik.grundbegriffe`) und die vom Mathe-Profi genannten zweifelhaften Zuordnungen. Sie betreffen die Lehrplan-Übersicht und Pflicht/Kür einzelner Themen.

## Eingestellt (26.11.2026)
- Grundlage: vollständige Soll-Liste des Mathe-Profis nach Auftrag 9 (`origin/mathe-profi` 8aff7f72), nachgebessert nach der Gegenprüfung (Werkstatt 998). Die nachgebesserte Fassung hat ChatGPT nicht noch einmal geprüft; der Nutzer hat das Einstellen ohne weitere Wartezeit angeordnet.
- Weg: `schule.plan_setzen_intern`, je Kind ein Aufruf, eine Transaktion. Vorher Probelauf mit Rollback.
- Kind 1: 23 Einträge, Revision 14 → 15. Laufender Flug bleibt Platz 1. Keine Karten geändert, keine Sterne gebucht.
- Kind 2: 45 Einträge, Revision 60 → 61. Laufender Flug auf Platz 1. `ge3` auf „kann – wiederholen“ (7 Karten gesetzt, eine Buchung +100 Sterne für den fertigen Ort). `ge9` nicht mehr in der normalen Route (bleibt Zusatz). Abschnitt 5 (Klasse 9) nicht eingestellt.
- Versuche, übrige Karten und Sterne unverändert.

## Danach offen
- Eingangsdiagnose Kind 2 (amtlicher Test Klasse 8), dann `ge3` nach `diagnose-regel.md` einordnen.
- Abschnitt 5 für Kind 2 nach dem Abschluss von Klasse 8 einstellen; dabei `a7` ohne Auslassung und `f4` mit `funktionen.quadratisch` statt `funktionen.transformation`.
- Die vier Widersprüche zwischen `themenliste.json` und App klären.
- Prüfen, ob Kind 1 den Flug `r2` mit ausgelassenem Thema sauber abschließen kann, sobald er dran ist.
