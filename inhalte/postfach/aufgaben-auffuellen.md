# Postfach aufgaben-auffuellen (Neunte Runde: Aufgaben auffüllen)

Neueste Meldung oben.

## 2026-11-16 04:08 – FERTIG: Runde 9 (Zweig aufgaben-auffuellen, nicht gemergt)

| Thema | Lernkarten | Aufgaben | zahl / luecken / auswahl | inhalt_pruefen |
|---|---|---|---|---|
| terme.umformen | 8 | 184 | 6 / 147 / 31 | OK |
| zahlen.teilbarkeit | 8 | 184 | 73 / 15 / 96 | OK |
| finanzen.zinsen | 8 | 184 | 140 / 0 / 44 | OK |

- Je Lernkarte 23 neue Aufgaben: 13 Übungen (Stufe 1/2/3: 4/5/4, alle mit Tipp), 1 Test, 3 Korrektur, 6 Sicherung. Vorher: 2 Übungen je Karte.
- Generatoren: `terme_umformen.py`, `zahlen_teilbarkeit.py`, `finanzen_zinsen.py`, gemeinsame Hilfen in `_auffuellen.py` (nutzt `_bausatz.py`). Jede Zahl-Aufgabe und jede Lücke wird beim Bauen nachgerechnet; Dubletten über das ganze Thema ausgeschlossen; Beispielzahlen der Karten gesperrt.
- Lernkarten: Lernziele, Reihenfolge und Titel wie in `inhalte/klar/quelle.md`; Erklärfelder unverändert aus `inhalte/klar/<thema>.json` (per Skript geprüft: identisch). Alle Karten hatten dort schon ein Bild.
- abschnitte, teilfaehigkeiten (je Karte eine) und bewertung angelegt, alle Lernkarten Pflicht.
- Term-Vorlagen (terme.umformen, 145 Aufgaben) mit dem Leser aus lernen.js geprüft: Die richtige Lösung, so getippt wie ein Kind (z. B. „x² + 13x + 40“, „6(x + 7)“), wird für jede Aufgabe richtig erkannt.
- Je Lernkarte mindestens 11 Aufgaben gelesen; dabei gefundene Unschärfen behoben (Vorzeichen im Lösungsweg, „Wie viel Zinsen“, sehr lange Busintervalle).
- Offen / Annahmen (auch im Feld „offen“ der Dateien): Die alten Aufgaben liegen nur in der Datenbank, Dubletten zu ihnen konnte ich nicht prüfen. Beim Einspielen mit einheit_abgleichen(…, 'lassen') kommen die neuen dazu. Primfaktor-Lücken erwarten die Faktoren klein → groß (Hinweis steht in der Aufgabe). Zahlen ab 1 000 mit Leerzeichen wie auf den Karten dieser Themen (sonst im Bausatz erst ab 10 000).
- Kein Merge, keine Datenbank, kein App-Code.

## 2026-11-16 04:08 – STATUS
finanzen.zinsen fertig: Generator `inhalte/generatoren/finanzen_zinsen.py`. 8 Lernkarten, 184 Aufgaben. Alle Beträge exakte Cent-Beträge, jede Zahl-Aufgabe mit Rechenausdruck (Z = K · p/100, p = Z : K · 100, K = Z · 100 : p, · m/12).
Stufe 3: Kontostand nach einem Jahr, Bankvergleich, Kredit zurückzahlen, Sparziel, Fehler finden (p % ≠ p €, mal 0,025 statt 2,5, falsch herum geteilt, Monate statt Jahre, halbes Jahr · 6). Lernkarten identisch mit der Überlagerung. inhalt_pruefen: OK.
Nachtrag zahlen.teilbarkeit: Zahlen ab 1 000 jetzt mit Leerzeichen wie auf den Lernkarten (3 470), ebenso Beträge in finanzen.zinsen (2 000 €).

## 2026-11-16 04:06 – STATUS
zahlen.teilbarkeit fertig: Generator `inhalte/generatoren/zahlen_teilbarkeit.py`. 8 Lernkarten, 184 Aufgaben (je Karte 13 Übungen 4/5/4, 1 Test, 3 Korrektur, 6 Sicherung).
Zahl-Aufgaben mit Rechenausdruck (ggT/kgV über Quotienten nachgerechnet, Reste mit %, Quersummen als Summe); Ziffer-Lücken (□ am Ende einer Zahl), Primfaktor-Lücken (kleinste zuerst, Hinweis steht dabei).
Stufe 3: Fehler finden (1 ist keine Primzahl, ungerade ≠ prim, Quersumme nur für 3/9, kgV ≠ Produkt …), Sachaufgaben (Gruppen, Packungen, Busse, Bänder, Körbe). Lernkarten identisch mit der Überlagerung. inhalt_pruefen: OK.

## 2026-11-16 04:02 – STATUS
terme.umformen fertig: neuer Generator `inhalte/generatoren/terme_umformen.py` (Hilfen in `_auffuellen.py`). 8 Lernkarten, je 13 Übungen (4/5/4 je Stufe), 1 Test, 3 Korrektur, 6 Sicherung = 184 Aufgaben.
Term-Antworten als Term-Vorlage (□x + □y, □x² + □x + □, □x(□x + □), □(□x + □) …), Stufe 3: Fehler finden, Sachaufgaben (Umfang, Fläche, Garten, Geschenke, Rabatt), Rückwärts (binomische Formel ergänzen), Kopfrechnen mit binomischer Formel.
Lernkarten unverändert aus `inhalte/klar/terme.umformen.json` (geprüft: Felder identisch). inhalt_pruefen: OK, jede Zahl-Aufgabe und jede Lücke beim Bauen nachgerechnet. Beispielzahlen der Karten sind als Aufgabe gesperrt.
