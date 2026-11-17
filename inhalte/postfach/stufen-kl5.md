# Postfach stufen-kl5 (Zwanzigste Runde, Klasse 5)

Neueste Meldung oben.

## 2026-11-17 14:31 – STATUS: zahlen.ganz fertig
11 Lernkarten: 64 neue Übungen, 22 Knobel-Bordkarten, 57 umgestuft, 52 überzählig. Prüfskript OK, 0 Gruppen „gleich gebaut hintereinander“, Gegenprobe ohne überzählige OK, Nachweis OK.

## 2026-11-17 14:24 – STATUS: zahlen.natuerlich fertig
12 Lernkarten: 81 neue Übungen, 23 Knobel-Bordkarten, 58 umgestuft, 52 überzählig. Prüfskript OK, 0 Gruppen „gleich gebaut hintereinander“, Gegenprobe ohne überzählige OK, Nachweis OK.

## 2026-11-17 – STATUS: Arbeitsweise
- Werkzeug: `inhalte/generatoren/_stufen_kl5.py` (Typen, neue Übungen, Knobel, Ordnen, Gegenprobe), Daten je Thema in `_st5_<thema>.py`, Nachweis `_stufen_kl5_nachweis.py`.
- **Überzählige Übungen bekommen kein `g`.** Grund: Das Prüfskript zählt alle Übungen; mit `g` würden die überzähligen gegen „höchstens 2 gleich gebaute je Typ und Stufe“ verstoßen. Ohne `g` bleibt die Datei OK, und die App behandelt sie wie bisher, bis der Haupt-Chat sie sperrt.
  Damit trotzdem geprüft ist, dass jede Lernkarte nach dem Sperren alle Regeln erfüllt, läuft je Thema eine **Gegenprobe**: dieselbe Datei ohne überzählige Übungen durch `tools/inhalt_pruefen.py` (muss fehlerfrei sein, alle Übungen dann mit `g`).
- Überzählig wird automatisch die dritte und jede weitere Übung mit gleichem Typ und gleichem Satzbau in derselben Stufe; dazu einzelne von Hand, wo ein Stufe-3-Typ sonst mehr als dreimal vorkäme.
