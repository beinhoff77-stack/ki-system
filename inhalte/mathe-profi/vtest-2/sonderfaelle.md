# Sonderfälle VT2 (Verstehen in Tests, Stufe 1, Runde 2)

Zu jeder Aufgabe ein Satz: welcher Sonderfall geprüft wurde und wie er behandelt ist.


## finanzen.zinsen / rollen

- VT2-001 (test): Sparzinsen 30 €, Nettozahlung 45 €, also Kreditzinsen 75 € und Kredit 2 500 € (ganzzahlig); Fehlbilder 45 und 15 (Vorzeichen der Sparzinsen), 1 500, 500, 7 500.
- VT2-002 (korrektur): Kredit hat den höchsten Zinssatz, die Familie bekommt trotzdem netto Zinsen (Guthaben sind größer). Die Eingabe 1 oder 2 ist im Text erklärt.
- VT2-003 (korrektur): Nur Zinsen erhalten, nicht zahlen; Optionen mit Kredit sind durch den Klammerhinweis ausgeschlossen. 40 € passt nur zu 2 000 € bei 2 %.
- VT2-004 (korrektur): Fehler in Zeile 3 (Vorzeichen/Rolle); Zeilen 1 und 2 stimmen, damit ist „erste Fehlerzeile“ eindeutig.
- VT2-005 (sicherung): Zinssatz 50 : 2 000 = 2,5 %; Kredit 90 : 0,025 = 3 600 €. Die Rolle wechselt, der Zinssatz bleibt; Fehlbild 1 800 liest 50 als 5 %.
- VT2-006 (sicherung): Kredit 3 000 € zu 8 % bringt 240 € Zinsen; 2 % von G sind 240 €, also G = 12 000 € (ganzzahlig). Der Sparzinssatz (2 %) steht im Text.
- VT2-007 (sicherung): Sparzinsen auf alle 200 000 € (0,5 % → 1 000 €), Kreditzinsen nur auf 150 000 € (5 % → 7 500 €); der Rest im Tresor bleibt unverzinst (steht im Text).

## finanzen.zinsen / jahreszinsen_komma

- VT2-008 (test): Fehler in Zeile 3 (36 € zusätzlich zu den 90 €); die Zeilen 1 und 2 stimmen, Zeile 4 folgt nur aus Zeile 3. Richtig 3 690 €. Fehlerzeile 3, nicht 2.
- VT2-009 (korrektur): Kapital ist nicht genannt (1 % bringen 80 €): 0,25 % → 20 €, 2,5 % → 200 €, 0,05 % → 4 €, alles ganzzahlig, keine Rundung.
- VT2-010 (korrektur): Nur die letzte Zeile ordnet alle drei Zinssätze richtig zu; die Zeilen mit einem richtigen und zwei falschen Paaren sind bewusst gemischt.
- VT2-011 (korrektur): Nur 6 € stimmt; 60 € und 600 € entstehen durch Kommafehler, 0,60 € durch falsche Division durch 1 000.
- VT2-012 (sicherung): Nur 0,25 % liefert 15 € bei 6 000 €; die anderen Optionen unterscheiden sich um Zehnerpotenzen. Optionen aufsteigend geordnet.
- VT2-013 (sicherung): Zwei Sparbücher mit 36 € und 39 €; die Werte sind verschieden, damit das erste Feld das zweite nicht verrät. Das kleinere Kapital bringt mehr, weil sein Zinssatz größer ist.
- VT2-014 (sicherung): Genau eine Rechnung ist falsch (sie addiert 3 % und 5 % statt 3 % und 0,5 %); die anderen sind richtige Zerlegungen von 3,5 %. „NICHT“ steht im Text groß.

## finanzen.zinsen / kapital

- VT2-015 (test): Kapital 6 000 € bei 2 %, 4 000 € bei 3 %, Unterschied 2 000 €; alle ganzzahlig. Kern: Zinsen gleich, Zinssatz größer, Kapital kleiner im Verhältnis 2 : 3, nicht um 1 %.
- VT2-016 (korrektur): Proportionalität nur bei gleichem Zinssatz und gleicher Zeit; Option 1 (andere Zinssätze) ist bewusst falsch.
- VT2-017 (korrektur): Platzhalter □ ist das Kapital; Gleichung □ · 0,04 = 52, nicht □ : 0,04.
- VT2-018 (korrektur): Fehler schon in Zeile 1 (Faktor 4,2 statt 0,042); Zeile 2 und 3 folgen nur daraus. Kapital 1 500 €.
- VT2-019 (sicherung): Vergleich ohne Rechnen: kleinerer Zinssatz heißt mehr Kapital bei gleichen Zinsen; kein Rundungsproblem.
- VT2-020 (sicherung): Zwei Schritte (60 % Teil, dann Ganzes); 54 € bei 3 % ergibt 1 800 €, das sind 60 % von 3 000 €. „Rest unverzinst“ steht im Text.
- VT2-021 (sicherung): Gegenläufigkeit von Kapital und Zinssatz; „größer als 0 %“ schließt Sonderfall 0 aus.

## finanzen.zinsen / zeitanteil

- VT2-022 (test): Frau Berger bekommt 60 € (72 € im Jahr, 10/12 davon); Herr Koch hat 90 € im Jahr, also 7,50 € je Monat, und braucht 8 Monate (ganzzahlig). Zwei Anlagen werden aufeinander abgestimmt, nicht eine Laufzeit bis zu einer Zinssumme gesucht.
- VT2-023 (korrektur): Beide Anlagen bringen 50 €; der höhere Zinssatz wird durch die kürzere Zeit ausgeglichen. Gleiche Lückenwerte sind erlaubt.
- VT2-024 (korrektur): 8 Monate bringen 2 % des Kapitals → Jahreszinssatz 3 %; ganzzahlig. Einheit Prozent.
- VT2-025 (korrektur): Zinssatzwechsel: 3 000 € · 2 % · 4/12 = 20 €, 3 000 € · 3 % · 8/12 = 60 €, zusammen 80 €; der Mittelwert 2,5 % (75 €) wäre falsch.
- VT2-026 (sicherung): Nur die Formel mit : 12 und · 5 stimmt; die anderen drehen Zähler und Nenner.
- VT2-027 (sicherung): Zinsen proportional zur Zeit: 75 € : 10 · 4 = 30 €; Kapital und Zinssatz nicht nötig. Einfache Verzinsung innerhalb eines Jahres.
- VT2-028 (sicherung): Proportionalität der Zeit: 9 : 3 = 3; keine Zinsen auf Zinsen.

## terme.umformen / zusammenfassen

- VT2-029 (test): „für jede positive Zahl x“; für x > 0 sind alle Seiten positiv (Quadratseite 2x + 4). Der Koeffizientenvergleich bleibt gültig, weil die Gleichheit für unendlich viele x gilt; Lösung a = 4 eindeutig.
- VT2-030 (korrektur): Zeilen 1 und 2 stimmen, erster Fehler eindeutig in Zeile 3; jede Möglichkeit nennt eine andere Zeile.
- VT2-031 (korrektur): Jedes mögliche neue Glied ist zu einem vorhandenen gleichartig (a ≠ 0); für alle a von −20 bis 20 und alle drei Arten nachgezählt: 2 bis 3 Glieder.
- VT2-032 (sicherung): Die x-Glieder heben sich für jedes x auf; die große Zahl 987 654 macht Einsetzen von Hand unbequem, ändert aber nichts am Wert 6.
- VT2-033 (sicherung): Änderung −1 für jedes Ausgangspaar (a, b) nachgerechnet; gefragt ist „um wie viel kleiner“, die Antwort 1 ist positiv.

## terme.umformen / minusklammer

- VT2-034 (test): a positiv vorgegeben; der Unterschied 2a gilt für jedes x, nur a = 9 passt. Tims Regel ist im Text an einem eigenen Beispiel (20 − (x − 5)) erklärt, das nicht die gefragte Zahl enthält.
- VT2-035 (korrektur): Erster Fehler in Zeile 2, Zeile 3 enthält nur den Folgefehler; Fehlbild „Zeile 3“ als eigener Fall.
- VT2-036 (korrektur): Das Pfand wird vom Preis abgezogen (steht im Text); für x < 3 bekäme Lisa Geld zurück, auch dann gilt 50 − (x − 3).
- VT2-037 (sicherung): Bildungsregel der Terme ausdrücklich beschrieben; gerade Nummern ergeben 1, ungerade x − 1 (rekursiv nachgerechnet).
- VT2-038 (sicherung): a und b verschieden aus 1 … 5 (steht im Text); alle 20 Paare ergeben 8 Werte von 16 bis 24 ohne 20.

## terme.umformen / aequivalenz

- VT2-039 (test): Beide Terme haben ausdrücklich die Form a · x + b; nur dann genügen zwei Einsetzungen. Der Lösungsweg nennt das Gegenbeispiel x² und 3x − 2 (gleich bei 1 und 2), damit die Einsicht nicht übertragen wird.
- VT2-040 (korrektur): Alle vier Zählweisen zählen richtig (gleichwertige Terme, für n = 1 … 29 geprüft); eindeutig ist nur, welche zum Aufbau 4 + 3 · (n − 1) passt.
- VT2-041 (korrektur): Das Ergebnis (2x + k) : 2 − x = k : 2 hängt nicht von x ab; k = 20 eindeutig, Brüche treten bei ungeraden x nicht auf, weil 2x + 20 gerade ist.
- VT2-042 (sicherung): Fallunterscheidung über (a − 2) · x + (9 − b) für a von −5 bis 5, b von −9 bis 19 und x von −60 bis 60 nachgeprüft; das Beispiel a = 3, b = 4 (x = −5) im Fehlbild ist ganzzahlig.
- VT2-043 (sicherung): sechs Terme, Paare ohne Reihenfolge gezählt (A–B, A–C, B–C, D–E); F ist zu keinem gleichwertig.

## terme.umformen_teil2 / ausklammern

- VT2-050 (test): Genau Nummer 1 ist falsch; Nummer 2 bis 4 sind richtig. Richtige Klammer 3y(3y − 2).
- VT2-051 (korrektur): Beim Ausklammern von −3x aus −6x² − 9x steht in der Klammer 2x + 3, bei 3x steht −2x − 3. Vier Lücken, jedes Fehlbild an der eigenen Lücke.
- VT2-052 (korrektur): Fehler in Zeile 1 (ggT 3 statt 6); Zeile 2 und 3 rechnen mit 3x richtig weiter, aber die Klammer enthält noch den Faktor 2. Richtig 6x(3x − 2).
- VT2-053 (korrektur): Probe durch Ausmultiplizieren: (1), (2), (3) stimmen; (4) gibt 6x² + 90x und (5) gibt 6x² + 10x. Soll 3.
- VT2-054 (sicherung): Nichts außer 1 lässt sich ausklammern (die 5 hat weder die 2 noch ein x). Alle vier Möglichkeiten sind gleich gebaut: „Man kann … ausklammern, denn …“.
- VT2-055 (sicherung): k zwischen 7 und 20, ggT(18, k) = 6: nur k = 12 (k = 18 gäbe 18x); die Zahl 12 steht nicht im Text, die 6 aus 6x ist ausdrücklich falsch (Fehlbild).
- VT2-056 (sicherung): Breite 4x aus 20x² + 12x = (5x + 3) · 4x; ganzzahlige Koeffizienten, Einheit Meter.

## terme.umformen_teil2 / binomisch

- VT2-057 (test): Fehler in Zeile 2 (kein Mittelglied); jede der vier Lücken hat jetzt ein Fehlbild (Zeile 1 und 3, (2x)² als 2x², Mittelglied, 25).
- VT2-058 (korrektur): 25x² − kx + 4 = (5x − 2)² ergibt k = 20; Quadrat einer Differenz, nicht einer Summe.
- VT2-059 (korrektur): Gegenbeispiel mit 3 und 4: 49 gegen 25, Differenz 24 = 2ab.
- VT2-060 (korrektur): Zuwachs 10x + 25 durch (x + 5)² − x²; Einheit cm².
- VT2-061 (sicherung): 50² − 49² = 99; die Aufgabe nennt (50 − 1)² als Hilfe, ohne das Ergebnis zu verraten.
- VT2-062 (sicherung): Fehler in Zeile 2 ((4x)² = 16x²); Zeile 3 ist 24x, damit stimmt die Option „2 · 4x · 3 = 12x“ nicht.
- VT2-063 (sicherung): 9x² + 12x + 4 = (3x + 2)²; Umfang 12x + 8; Einheiten cm.

## geometrie.kreis / umkehrung

- VT2-064 (test): Alle Punkte C mit rechtem Winkel liegen auf dem Kreis um M mit Radius 5 cm; MC bleibt 5 cm. Das Wort „Thales“ steht nirgends in der Frage.
- VT2-065 (korrektur): Koordinatenaufgabe ohne Wurzel: C liegt über dem Mittelpunkt M(2 | 0) im Abstand 4; zweiter möglicher Punkt (2 | −4) ist durch „positive y-Koordinate“ ausgeschlossen.
- VT2-066 (korrektur): Umkreisradius 6 cm → AB = 12 cm; Voraussetzung rechter Winkel bei C steht im Text.
- VT2-067 (korrektur): Fehler in Zeile 3 (Radius = Hälfte von 10 cm = 5 cm); Zeilen 1 und 2 stimmen.
- VT2-068 (sicherung): Thaleskreis ist ein Kreis um M mit Radius 3 cm ohne A und B; die falschen Kreisoptionen haben verschieden gebaute Endungen.
- VT2-069 (sicherung): Umkehrung gilt in jedem rechtwinkligen Dreieck; zwei falsche Optionen haben „Richtig“ mit falscher Begründung.
- VT2-070 (sicherung): Lücke 1 (ACM = 40°) hat jetzt ein Fehlbild (50°, der Nachbarwinkel MCB).

## geometrie.kreis / lage

- VT2-071 (test): r aus „genau vier Passanten“: d = 7, 8, 9, 10 → r = 6; r ganzzahlig im Text, d = 0 ist mitgezählt.
- VT2-072 (korrektur): Zwei Schnittpunkte heißt Abstand kleiner als Radius; r = 7 cm wäre Tangente, deshalb nur r > 7 cm.
- VT2-073 (korrektur): Tangentenabstand r: doppelter Radius → 2 Punkte, halber Radius → 0 Punkte.
- VT2-074 (korrektur): Tangente ⊥ Berührradius: Winkel bei B = 90°, bei M = 35°, bei A = 55°. Der Satz steht in der Merke der Einheit.
- VT2-075 (sicherung): 12 cm Abstand − 9 cm Durchmesser = 3 cm Abstand zwischen h und Kreis, keine gemeinsamen Punkte.
- VT2-076 (sicherung): Zwei Kreise, Gesamtzahl der Punkte: bei d = 3 berührt die Gerade den kleinen Kreis (1) und schneidet den großen zweimal (2), also 3.
- VT2-077 (sicherung): Eine Gerade, die nicht durch M geht, hat höchstens zwei gemeinsame Punkte; Mias Behauptung „immer mehr, ohne Grenze“ ist eindeutig falsch.

## geometrie.kreis / umkreis_inkreis

- VT2-078 (test): α = 70°: außerhalb bei β > 90° (19 Werte) oder γ > 90° (19 Werte); β = 90° und γ = 90° sind Randfälle und zählen nicht. Soll 38, kürzer zu zählen als vorher.
- VT2-079 (korrektur): Fünf Dreiecke: innerhalb A (1), auf einer Seite B und D (2), außerhalb C und E (2); Lösung 1, 2, 2 folgt keiner Reihenfolge im Text.
- VT2-080 (korrektur): γ = 90° (rechter Winkel), der Umkreismittelpunkt liegt auf der Seite AB (Satz des Thales); der dritte Winkel entscheidet.
- VT2-081 (sicherung): Fehler in Zeile 1 (gleich weit von den Seiten statt von den Ecken); Zeile 2 und 3 folgen daraus. Die Nummer 3 (Mittelsenkrechten) steht nur in der Liste der Möglichkeiten und liegt im Pool sicherung.
- VT2-082 (korrektur): Das Urteil „Richtig“ mit Begründung über die Winkelhalbierenden; die falsche Begründung nennt jetzt die Höhen, nicht mehr die Mittelsenkrechten (anders als 081).
- VT2-083 (sicherung): I liegt auf den Winkelhalbierenden: α = 56°, β = 34°, γ = 90° (Probe 180°); das Dreieck ist rechtwinklig, was nicht im Text steht.
- VT2-084 (sicherung): Im gleichseitigen Dreieck fallen Umkreis- und Inkreismittelpunkt zusammen; Begründung über gleiche Geraden.

## zahlen.natuerlich / stellenwert

- VT2-085 (test): Durch Aufzählen aller sechsstelligen Zahlen geprüft: größte Zahl mit genau zwei Vieren im Abstand von drei Stellen und vier verschiedenen übrigen Ziffern ist 984 764 (die Vieren an Stelle 3 und 6).
- VT2-086 (korrektur): Für jedes Ziffernpaar mit Zuwachs 36 000 gilt b − a = 4; es gibt sechs Paare (0/4 … 5/9), deshalb ist „0 und 4“ keine sichere Folgerung.
- VT2-087 (korrektur): Zeile 1 stimmt (die 6 ist wirklich die zweite Ziffer); erster Fehler eindeutig in Zeile 2.
- VT2-088 (sicherung): Jede falsche Möglichkeit lässt eine andere Auswahl der Nullen weg (keine, die mittlere bleibt, die letzte bleibt) und nennt die entstehende Zahl.
- VT2-089 (sicherung): Alle Verteilungen von 12 Plättchen auf vier Spalten mit höchstens 9 aufgezählt: kleinste Zahl 39, größte 9 300; „eine Spalte darf leer bleiben“ steht im Text.

## zahlen.natuerlich / ziffern_zu_zahlwort

- VT2-090 (test): „größer als eine Million und kleiner als zwei Millionen“ schließt beide Ränder aus; mit einem echten Zahlwort-Erzeuger nachgezählt: 999 (1 000 001 … 1 000 999).
- VT2-091 (korrektur): Zahlwörter, die mit „zehn Millionen“ beginnen, gehören zu 10 000 000 … 10 999 999 (alle achtstellig); „elf Millionen“ beginnt anders.
- VT2-092 (korrektur): Zeilen 1 und 2 stimmen; Fehler eindeutig in Zeile 3.
- VT2-093 (sicherung): Einteilung von links und von rechts für 1 000 … 999 999 verglichen: gleich genau bei den sechsstelligen Zahlen (900 000). Tims Regel ist an 45 000 120 gezeigt, nicht an einer Zahl des gefragten Bereichs.
- VT2-094 (sicherung): „hundert“ höchstens einmal je Klasse (für 0 … 999 nachgezählt), drei Klassen unter einer Milliarde; kleinste Zahl 100 100 100.

## zahlen.natuerlich / strahl_eintragen

- VT2-095 (test): „dieselben zwei Zahlen“ steht im Text; der Unterschied 300 ist auf beiden Strahlen gleich, 300 : 4 = 75 ganzzahlig.
- VT2-096 (korrektur): Für 200 Strichzahlen geprüft, dass das Doppelte nie auf einem Strich liegt; die Beschriftung 300, 500, 700, … steht im Text.
- VT2-097 (korrektur): Für alle Zehnerzahlen 10 … 1 000 nachgerechnet: Lenas Marke liegt immer genau 10 zu weit links.
- VT2-098 (sicherung): Ränder 0 und 12 000 ausgeschlossen; gemeinsame Striche alle 600, also 19; Auflisten aller 59 bzw. 79 Striche ist absichtlich unbequem.
- VT2-099 (sicherung): Die Abstände sind gleich groß (steht im Text), die Beschriftung 0, 10, 100, 1 000 wächst „regelmäßig“ um das Zehnfache – genau das ist die Fehlvorstellung.

## zahlen.natuerlich / runden_regel

- VT2-100 (test): Zahlen 1 bis 100 einschließlich; der Hinweis „auch 0 kann herauskommen“ steht im Text (B3); die 5 ergibt 10 gegen 0 und zählt nicht.
- VT2-101 (korrektur): Höchstabweichung 50 bei 4 950 (Aufrunden ab 5), über 0 … 19 999 geprüft.
- VT2-102 (korrektur): Zeile 1 stimmt; erster Fehler in Zeile 2.
- VT2-103 (sicherung): Die drei Fälle stehen in der Frage; ein Ablenker ist ebenfalls eine Sammel-Aussage („Alle drei Fälle … nur über 100 000“), widerlegt an 3 000, 6 000, 10 000.
- VT2-104 (sicherung): Monotonie für a < b < a + 120, a < 2 000 geprüft; zwei Möglichkeiten sind zweiteilig (B6).

## zahlen.natuerlich / runden_sinnvoll

- VT2-105 (test): Länge ganzzahlig in Metern (steht im Text), Bereich 25 … 34 m; Rest unter 3 m zählt nicht.
- VT2-106 (korrektur): 1 000 : 36 = 27 Rest 28 ohne Dezimalbruch; A abrunden, B aufrunden.
- VT2-107 (korrektur): 22 817 auf Tausender 23 000, auf Zehntausender 20 000; beide richtig.
- VT2-108 (sicherung): Keiner der Faktoren ist eine Zehnerzahl (steht im Text), also wird Leas Schätzung sicher größer; für alle Faktoren 11 … 59 geprüft. Tom: Beispiele für zu groß (18 · 11) und zu klein (12 · 19).
- VT2-109 (sicherung): Alle vier Zahlen haben die Hunderterziffer 4 (Abrunden); der Ablenker „verrechnet, 14 000“ hat ein falsches Urteil (B7).

## zahlen.natuerlich / roemisch_schreiben

- VT2-110 (test): Kurzer Text mit Beispielen statt Regelwerk (B1); für 10 … 99 nachgezählt: genau 49 und 94 sparen 5 Zeichen.
- VT2-111 (korrektur): Regeln ausgeschrieben; nur VC verstößt (V darf nicht vor C).
- VT2-112 (korrektur): Gegenbeispiel XVIII → XIX in der richtigen Möglichkeit; auch unter 10 gibt es Fälle (VIII → IX), der Ablenker „recht bei Zahlen unter 10“ ist damit widerlegt.
- VT2-113 (sicherung): Nur Regeln im Text, keine Bauanleitung (A3); „V, L, D höchstens einmal“ und „der Größe nach“ schließen DD und MMMCMM aus. 3 999.
- VT2-114 (sicherung): Regeln ausgeschrieben (B11); ohne „höchstens dreimal“ wäre schon 19 = XVIIII sechsstellig.

## zahlen.natuerlich / dualsystem

- VT2-115 (test): Vorn darf eine 0 stehen (steht im Text), sonst gäbe es keine Gegenzahl; Summe immer 31; einziges Paar mit Unterschied 7: 19 und 12 (nachgeprüft).
- VT2-116 (korrektur): 0111 und 111 beide 7; die richtige Möglichkeit ist keine Sammel-Aussage mehr (B5).
- VT2-117 (korrektur): Für alle Paare 1 … 63 geprüft: mehr Einsen kommt mit größerem und mit kleinerem Wert vor; „nichts Sicheres“ ist hier richtig (B4).
- VT2-118 (sicherung): Die Zahlen 0 bis 31 (einschließlich 0); 16 davon haben an der Vierer-Stelle eine 0.
- VT2-119 (sicherung): zehnstellig im Zweiersystem = 512 … 1 023, also 3 oder 4 Ziffern im Zehnersystem.
