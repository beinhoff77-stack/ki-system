# Ist-Zustand: ehrliche Kritik der Optik und Handhabung

- **Stand:** Zweig `lernen-app`, Commit `ab014e1` (App 0.71.0, nach der App-Prüfrunde 2).
- **Nachgestellt** mit den Testdaten aus `tests/lernen.test.cjs` durch `ist/aufnahme.test.cjs`.
- **Bilder in `ist/`:** `handy-*` in 390 × 844, `tablet-*` in 820 × 1180, `rechner-*` in 1280 × 800; `*-ganz.png` ist die ganze Handy-Seite.
- **Kennzeichnung:** **Fakt** = im Bild oder Code nachprüfbar. **Urteil** = meine Gestaltungsmeinung.

## Vorweg: Was seit Runde 1 besser ist (Fakt)

- „Weiter geht’s“ steht jetzt oben auf Heute (`handy-heute.png`).
- Kartenwechsel im Üben mit ‹ ›.
- „Verstanden – los“ führt von der Erklärung direkt zur Aufgabe.
- Fehler-Detektiv an der falschen Antwort.
- Neue Ansicht „Was wackelt?“ für Eltern (`handy-eltern-lernstand-ganz.png`).
- Reisepass und Abmelden sind sortiert.

Die App ist solide. Die folgende Kritik zielt auf das, was sie **nicht** ist: eine App, die man gern in die Hand nimmt.

## 1. Gesamteindruck (Urteil)

Die App sieht aus wie ein ordentliches Verwaltungswerkzeug mit Kinderfarben:
- hellblaue Fläche
- weiße Karten mit 22 px Rundung und hellblauer Unterkante
- orange Hauptknöpfe
- dünne Linien-Icons
- Leiste unten

Das ist die Bauart fast jeder Web-App von 2020–2024. Nichts daran ist falsch, aber nichts ist eigen. Ohne Logo könnte es eine Fitness-, Banking- oder Paket-App sein.

Die Weltreise, die eigentliche Idee, kommt nur als Kartenbild vor. Sie prägt weder Formen noch Schrift noch Abläufe.

## 2. Altbacken, beliebig, überladen

| Stelle | Fakt | Urteil |
|---|---|---|
| Alle Kinderseiten | Jeder Inhalt sitzt in einer weißen Karte mit Rand und Unterkante. Auf Heute sind es vier Karten und drei Zahlenkästen (`handy-heute-ganz.png`). | „Karten-Suppe“: Weil alles gerahmt ist, ist nichts besonders. Das Muster wirkt beliebig. |
| Heute | Unter dem Hauptknopf folgen: Balken, Link „Erst die Erklärungen ansehen“, Kartenausschnitt, drei Zahlenkästen, Link „Reisepass und Belohnungen ansehen“, Karte „Mein Stand“, aufklappbares „Später“. | Sieben Angebote auf einer Seite für ein Kind, das eigentlich nur loslegen will. Die Karte ist ein Bild ohne Funktion: Man kann reinschauen, aber nichts damit tun. |
| Thema – Erklären | Alle drei Lernkarten untereinander, jede mit Status, Bild, Regel, „So geht’s“, Achtung-Kasten, Knopf „Dazu üben ▸“ und gestricheltem Kasten „✎ Anmerkung zu dieser Erklärung“. Seite 2 100 px hoch (`handy-thema-erklaeren-ganz.png`). | Wie ein ausgedrucktes Arbeitsblatt. Man scrollt, statt zu verstehen. |
| Thema – Status | Die zwei Fortschrittskreise stehen ohne Abstand vor „noch nicht geübt“ und lesen sich wie „O Onoch nicht geübt“ (`handy-thema-erklaeren-ganz.png`, unter jeder Kartenüberschrift). | Kleiner Abstandsfehler, wirkt unfertig. Zwei hohle Kreise erklären sich einem Kind auch nicht selbst. |
| Kopfzeile | Beige Kopfzeile der Hauptapp mit grauem Rand über der farbigen Kinderseite; im Look Nacht hart abgesetzt (`handy-heute-nacht.png`). | Zwei Apps übereinander geklebt. |
| Weltkarte | Weltkarte, Legende, drei Gebiets-Knöpfe, zweite Karte (Europa) und Ortsliste untereinander (`handy-weltkarte-ganz.png`). | Zwei Karten auf einer Seite; die zweite zeigt dasselbe wie Heute. |
| Rechner/Tablet | Inhalt in einer 600-px-Spalte; links und rechts je 340 px leer; Leiste unten über die volle Breite, die vier Einträge 320 px auseinander (`rechner-thema-ueben.png`, `tablet-heute.png`). | Handy-Layout aufgeblasen. Am Tablet, dem wahrscheinlichsten Lerngerät unterwegs, wird der Platz nicht genutzt. |
| Eltern | Georgia-Überschriften, beige, braune 10-px-Großbuchstaben; Lernstand als Satz („Letzte 7 Tage: 30 Aufgaben, davon 22 richtig, 4-mal mit Tipp. Lerntage in 4 Wochen: 2 …“, `handy-eltern-lernstand-ganz.png`). | Elegant, aber zum Lesen statt zum Erfassen. Zahlen in Sätzen statt als Bild. |

## 3. Zu kindisch, zu erwachsen

- **Fakt:** Beide Kinder bekommen dieselben Seiten. Unterschiede gibt es nur über die Looks (Ozean/Nacht/Dschungel/Wüste) und „Entdecker/Studio“, das sind Farben und Ecken (`handy-heute.png` und `handy-heute-nacht.png`: gleicher Aufbau, gleiche Texte).
- **Urteil 13-Jähriger:** „Hallo Kind B!“, Sterne-Kästchen, Look „Ozean“ oder „Dschungel“ und runde Knöpfe wirken eher wie Grundschule. Ein 13-Jähriger will Werkzeug, Tempo und Kontrolle: Tastenkürzel, wenig Text, dichte Information.
- **Urteil 10-Jährige:** Für sie ist es zu erwachsen. Es gibt viel Text („Die Punkte fangen wieder bei 0 an. Die Erklärung steht aufgeklappt bei der Aufgabe.“), kaum Bilder für Zustände und keinen spürbaren Erfolgsmoment.

## 4. Rangfolge auf dem Bildschirm

| Bildschirm | Was groß sein müsste | Was heute groß ist (Fakt) |
|---|---|---|
| Heute | „Weiter“ | Weiter-Knopf (gut), danach gleich groß Kartenausschnitt und drei Zahlenkästen |
| Üben (Handy) | Die Aufgabe | Oben Pfad, Titel, Balken, Reiter, Kartenwechsler, die ganze Erklärung der Karte und „Verstanden – los“. Die Aufgabe beginnt erst unter dem Rand (`handy-thema-ueben.png`: auf 844 px ist keine Aufgabe zu sehen) |
| Falsch beantwortet | Was richtig gewesen wäre und **warum** | Rosa Kasten mit vier Textteilen: „Noch nicht. Richtig ist: 2 000“, „So geht’s: …“, Fehler-Detektiv, „Die Punkte fangen wieder bei 0 an …“ (`handy-aufgabe-falsch.png`). Die Antwort des Kindes (200) steht klein und grau im Feld darüber. |
| Eltern-Lernstand | „Was wackelt?“ | Die Antwort ist da, aber als Liste mit Text; der Wochenstand ist ein Satz. |

## 5. Umständliche Handhabung (konkret)

1. **Drei Navigationssysteme gleichzeitig (Fakt):** Zurück-Pfeil oben links, Brotkrumen „Heute › Rom“, Leiste unten, im Thema zusätzlich Reiter. Dazu ‹ › für Karten. Ein Kind muss lernen, welches wofür ist.
2. **Eingabe am Handy (Fakt + Annahme):** Das Antwortfeld ruft die Systemtastatur auf (`inputmode`). Annahme, an keinem Gerät gemessen: Die Zifferntastatur belegt auf einem 844-px-Handy etwa 300 px und schiebt die Aufgabe nach oben aus dem Bild. Die Frage ist dann beim Tippen nicht mehr sichtbar.
3. **Zahlenstrahl:** Man tippt auf Striche. Das Gefühl „die Zahl liegt *zwischen* 0 und 40 000, ungefähr in der Mitte“ wird nicht geübt, weil man nicht schieben kann.
4. **Erklärung:** Bild, Regel und Schritte stehen auf einmal da. Man kann nicht Schritt für Schritt durchtippen, Lesen ist Pflicht.
5. **Richtig:** Grüner Kasten „Richtig!“ und Text. Nach zwei Richtigen erscheint „LERNKARTE SITZT“ als weiterer Kasten unter der Aufgabe; man muss runterscrollen, um ihn ganz zu sehen.
6. **Falsch:** „Die Punkte fangen wieder bei 0 an“ ist für ein Kind eine Strafe in Worten. Die Erklärung klappt zusätzlich über der Aufgabe auf, der Bildschirm springt.
7. **Reisepass:** Er ist nur über einen Textlink auf Heute oder im Weg erreichbar, also zwei Schritte bis zu dem, wofür man Sterne sammelt.
8. **Daumen (Fakt):** Zurück oben links (schwer erreichbar mit rechter Hand), Reiter oben, Kartenwechsel ‹ › oben. Die meisten Bedienelemente liegen in der oberen Hälfte.
9. **Rechner:** Tastatur geht (Tab, Enter prüft inzwischen). Kürzel zum Wechseln von Erklären/Üben/Fehler oder für Tipp/Erklärung gibt es nicht.

## 6. Warum mein erster Stil-Entwurf nicht begeistert hat

Er war eine **Aufräumarbeit am selben Gebäude**:
- Karten, Leiste unten und Spalte blieben.
- Neu waren eine Schrift, ein Farbband, eine Stationenreihe statt Balken und ein Koffer als Figur.
- Dazu eine bessere Rangfolge.

Das löst Probleme, erzeugt aber kein Gefühl. Konkret:
- **Keine neue Leitidee:** „Weltreise als Farbsystem“ ist Dekoration, kein Erlebnis.
- **Handhabung kaum neu:** weiter Systemtastatur, weiter Reiter, weiter Scrollen in der Erklärung.
- **Generische Figur:** Der Koffer mit Gesicht ist das, was jede Lern-App hat.
- **Kein Unterschied 10 / 13:** wieder eine App für ein Durchschnittskind, das es nicht gibt.
- **Keine Mut-Entscheidung:** Ich habe nichts weggelassen.

Die drei Richtungen in diesem Ordner beginnen deshalb nicht bei den heutigen Seiten, sondern bei der Frage: Was ist die eine Sache auf jedem Bildschirm, und welches Bild trägt die ganze App?
