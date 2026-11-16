# Postfach aufgaben-auffuellen (Neunte Runde: Aufgaben auffüllen)

Neueste Meldung oben.

## 2026-11-16 04:08 – STATUS
finanzen.zinsen fertig: Generator `inhalte/generatoren/finanzen_zinsen.py`. 8 Lernkarten, 184 Aufgaben. Alle Beträge exakte Cent-Beträge, jede Zahl-Aufgabe mit Rechenausdruck (Z = K · p/100, p = Z : K · 100, K = Z · 100 : p, · m/12).
Stufe 3: Kontostand nach einem Jahr, Bankvergleich, Kredit zurückzahlen, Sparziel, Fehler finden (p % ≠ p €, mal 0,025 statt 2,5, falsch herum geteilt, Monate statt Jahre, halbes Jahr · 6). Lernkarten identisch mit der Überlagerung. inhalt_pruefen: OK.
Nachtrag zahlen.teilbarkeit: Zahlen ab 1 000 jetzt mit Leerzeichen wie auf den Lernkarten (3 470), ebenso Beträge in finanzen.zinsen (2 000 €).

## 2026-11-16 04:06 – STATUS
zahlen.teilbarkeit fertig: Generator `inhalte/generatoren/zahlen_teilbarkeit.py`. 8 Lernkarten, 184 Aufgaben (je Karte 13 Übungen 4/5/4, 1 Test, 3 Korrektur, 6 Sicherung).
Zahl-Aufgaben mit Rechenausdruck (ggT/kgV über Quotienten nachgerechnet, Reste mit %, Quersummen als Summe); Ziffer-Lücken (□ am Ende einer Zahl), Primfaktor-Lücken (kleinste zuerst, Hinweis steht dabei).
Stufe 3: Fehler finden (1 ist keine Primzahl, ungerade ≠ prim, Quersumme nur für 3/9, kgV ≠ Produkt …), Sachaufgaben (Gruppen, Packungen, Busse, Bänder, Körbe). Lernkarten identisch mit der Überlagerung. inhalt_pruefen: OK.

## 2026-11-16 04:30 – STATUS
terme.umformen fertig: neuer Generator `inhalte/generatoren/terme_umformen.py` (Hilfen in `_auffuellen.py`). 8 Lernkarten, je 13 Übungen (4/5/4 je Stufe), 1 Test, 3 Korrektur, 6 Sicherung = 184 Aufgaben.
Term-Antworten als Term-Vorlage (□x + □y, □x² + □x + □, □x(□x + □), □(□x + □) …), Stufe 3: Fehler finden, Sachaufgaben (Umfang, Fläche, Garten, Geschenke, Rabatt), Rückwärts (binomische Formel ergänzen), Kopfrechnen mit binomischer Formel.
Lernkarten unverändert aus `inhalte/klar/terme.umformen.json` (geprüft: Felder identisch). inhalt_pruefen: OK, jede Zahl-Aufgabe und jede Lücke beim Bauen nachgerechnet. Beispielzahlen der Karten sind als Aufgabe gesperrt.
