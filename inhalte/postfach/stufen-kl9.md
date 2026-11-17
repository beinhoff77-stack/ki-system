# Postfach stufen-kl9 (Zwanzigste Runde, Klasse 9)

Neueste Meldung oben.

## 2026-11-17 14:29 – STATUS
funktionen.quadratisch fertig: 45 neue Übungen, 16 Knobel-Bordkarten, 23 überzählig (ohne Typ). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:25 – STATUS
zahlen.reell fertig: 37 neue Übungen, 14 Knobel-Bordkarten, 20 umgestuft, 63 überzählig (ohne Typ). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:21 – STATUS
zahlen.wurzeln_basis fertig: 47 neue Übungen, 12 Knobel-Bordkarten, 16 umgestuft, 61 überzählig (ohne Typ). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:21 – FRAGE
Überzählige Übungen (dieselbe Vorlage mehrfach): Das Prüfskript erlaubt je Stufe und Typ höchstens 2 Aufgaben mit gleichem Satzbau. Gibt man allen alten Übungen einen Typ, schlagen die Wiederholungen der alten Vorlagen fehl. Meine Annahme, mit der ich weiterarbeite: Ab der dritten Übung gleicher Vorlage (und auf Stufe 3 ab der vierten desselben Typs) bleibt die Übung Zeichen für Zeichen unverändert und OHNE g in der Datei. Sie wird unter „überzählig“ gemeldet (Liste: /werk-Bericht am Ende), damit der Haupt-Chat sie sperrt. Folge: Lernkarten mit überzähligen Übungen sind im Prüfskript nicht vollständig typisiert, deshalb prüft es dort die strengen Typregeln nicht. Ich prüfe sie mit inhalte/generatoren/_stufen_kl9.py (nachweis) auf den Übungen mit Typ: S1 ≥ 4 mit ≥ 2 Typen, S2 ≥ 6 mit ≥ 3, S3 ≥ 8 mit ≥ 4 und höchstens 3 je Typ, höchstens 2 gleich gebaute je Typ, nie zwei gleiche Typen hintereinander. Die Reihenfolge innerhalb einer Lernkarte mischt die Stufen; das erlaubt erst, dass nie zwei gleiche Typen hintereinander stehen.
