# Postfach schwer-kl6 (Zehnte Runde, Klasse 6)

Neueste Meldung oben.

## 2026-11-16 08:20 – FERTIG
Zehnte Runde Klasse 6 abgeschlossen. Alle 8 Themen mit Generator bearbeitet (keins ohne Generator). Je Thema ein Commit auf `schwer-kl6`.
Prüfskript für alle 8 Dateien OK; Unverändert-Nachweis für alle 8 JA (`python3 -I inhalte/generatoren/_schwer_kl6_nachweis.py <thema>`:
alle Aufgaben aus `origin/lernen-app` stehen wörtlich und in gleicher Reihenfolge vorn, Lernkarten/Kopf unverändert, neu nur Pool uebung).
Technik: Abschnitt SCHWER am Ende jedes Generators, eigener Zufallsstart (6019, 6021, 6022, 6023, 6030, 6024, 6057, 6058), Hilfsdatei `_schwer_kl6.py`.
Alle Lösungen vom Programm berechnet (Feld c bei jeder Zahl- und Lücken-Aufgabe, vom Prüfskript nachgerechnet), zusätzlich von Hand nachgerechnet; jede neue Aufgabe gelesen.

### (1) Befundliste aus Teil 1 (Durchsicht; nichts geändert)
Je Lernkarte wurden die Erklärung und mindestens 10 Aufgaben (Übung aller Stufen + Test) gelesen. Falsche Lösungen: keine gefunden.
Auffällig sind vor allem zu hoch eingestufte Stufe-3-Aufgaben (gleiche Grundform wie Stufe 1/2, nur größere Zahlen) und einige mehrdeutige Auswahl-Aufgaben.

| Thema | Lernkarte | Aufgabe | Befund |
|---|---|---|---|
| zahlen.potenzen_zehner | zehnerpotenz | Ü S3 „Wie viele Tausender stecken in 10¹¹?“ (u. ä. 10⁷, 10¹²) | Stufe zu hoch: gleiche Rechnung wie Stufe 2, nur größere Zahl → Stufe 2 |
| zahlen.potenzen_zehner | gross_wissenschaftlich | Ü S3 „Ein Jahr hat etwa 3,15 · 10⁷ Sekunden. Schreibe die Zahl ohne Zehnerpotenz.“ | Grundform (wie Stufe 1) → Stufe 1–2 |
| zahlen.potenzen_zehner | gross_wissenschaftlich | Ü S3 „Licht legt in einer Sekunde etwa 300 000 km zurück … n?“ | Grundform → Stufe 1–2 |
| zahlen.potenzen_zehner | klein_wissenschaftlich | Ü S3 „Ein Kopfhaar ist etwa 7 · 10⁻⁵ m dick. Schreibe die Zahl als Dezimalzahl.“ | Grundform wie Stufe 1 → Stufe 1–2 |
| zahlen.potenzen_zehner | vergleichen_pruefen | Ü S3 „Welche Zahl ist größer: 1,9 · 10⁻² oder 5,3 · 10⁻²?“ | gleicher Exponent, Stufe 1 |
| zahlen.potenzen_zehner | (Lücke) | – | Sachaufgaben „Anzahl · Dicke → Höhe, Einheit wechseln“ (Prüfungstyp BMT8) fehlten; ergänzt |
| bruch.brueche | bruchteil_von | Ü S3 „Wie viele Minuten sind 3/4 Stunde?“, „Wie viele g sind 3/8 kg?“ | Standardumrechnung → Stufe 2 |
| bruch.brueche | erweitern | Ü S3 „Erweitere 1/10 auf den Nenner 100.“ | Stufe 1 |
| bruch.brueche | vergleichen | Ü S3 „Um wie viel ist 5/6 größer als 4/7?“ | verlangt Subtraktion ungleichnamiger Brüche (Thema bruch.rechnen, kommt später) – Lösung 11/42 richtig, aber Stoff vorgezogen |
| bruch.brueche | verstehen | Ü S3 „1/2 ist größer als 1/3.“ / „1/2 ist größer als 1/5.“ | Stufe 1 (Stammbrüche) |
| bruch.brueche | verstehen | Ü S1 „1/9 und 4/12 sind gleich groß.“ | eher Stufe 2–3 (Hauptnenner 36 nötig) |
| bruch.brueche | zahlenstrahl | Markierungen mit Dritteln/Sechsteln (5/3, 2/3, 1/6) | ohne Feld „zahl“, also nicht maschinell nachgerechnet; von Hand geprüft: richtig |
| bruch.brueche | (Lücke) | – | Mischungsaufgaben (Anteil vs. Verhältnis) und „Teil vom Rest“ fehlten; ergänzt |
| bruch.dezimal | verstehen | Ü S3 „Eine Zahl mit drei Nachkommastellen ist immer größer als eine mit einer, z. B. 0,37 > 0,8.“ | **Textfehler**: 0,37 hat nur zwei Nachkommastellen (Beispiel passt nicht zur Aussage). Lösung selbst richtig |
| bruch.dezimal | bruch_zu_dezimal | Ü S3 „Berechne 1 + 0,5 und gib das Ergebnis als Dezimalzahl an.“ (ebenso 1 + 0,4) | enthält keinen Bruch, Stufe 1; passt nicht zur Lernkarte |
| bruch.dezimal | runden | Ü S2 „Runde 2,596 auf Hundertstel.“ (Test „Runde 30,096 auf Hundertstel“) | Lösung als 2,6 bzw. 30,1 gespeichert; fachlich korrekt geschrieben wäre 2,60 / 30,10 – unkritisch, solange die App 2,60 = 2,6 wertet; im Lösungsweg die Endnull nennen |
| bruch.dezimal | periodisch | Ü S1 „Welche Dezimalzahl ist gleich 4/11?“ | verlangt schriftliche Division mit Periode → Stufe 2 |
| bruch.dezimal | stellenwerte | Ü S3 „Schreibe als Dezimalzahl: 5 + 9/100 + 7/1 000“ (4 Varianten) | Standardform → Stufe 2 |
| bruch.dezimal | (Lücke) | – | Platzhalter-/Ziffernkärtchen-Aufgaben, Rundungsfallen (Übertrag, doppeltes Runden, Rückwärtsrunden) fehlten; ergänzt |
| bruch.rechnen | brueche_plus_minus | Ü S2 „Ergänze: 1/2 − □/□ = 1/4“ | **nicht eindeutig**: 2/8, 3/12 … sind ebenso richtig, die Lücke verlangt aber genau 1/4 → Hinweis „vollständig gekürzt“ ergänzen |
| bruch.rechnen | brueche_plus_minus | Ü S3 „Berechne 1/2 + 1/2 − 2/5.“ | Stufe 1–2 |
| bruch.rechnen | vorzeichen | Ü S3 „Berechne (−1/8) + 1/5.“ Antwort „0/13“ | Ablenker „0/13“ ist kein üblich geschriebener Bruch; besser „0“ oder „−1/3“ (Zähler und Nenner addiert) |
| bruch.rechnen | dezimal_mal | Ü S3 „Ein Kilogramm Äpfel kostet 0,28 €…“ | Preis unrealistisch niedrig (Generator wählt Preise ab 0,28 €) |
| bruch.rechnen | gemischt | Ü S3 „Berechne 3/2 · 2/5 − 1/4 · 5/2 …“ = −0,025 | richtig, aber negatives Ergebnis kommt in der Karte unangekündigt; ok, da Vorzeichen-Karte vorher |
| bruch.rechnen | (Lücke) | – | Prüfungstypen „Ergebnis aus bekanntem Produkt“, „Klammern setzen“, „Lücke/Rechenzeichen ergänzen“, „Term zum Text“, „Kassenbon prüfen“ fehlten; ergänzt |
| terme.potenzgesetze | fehler_finden | Ü S3 „Ein Kind rechnet: 4³ · 4³ = 4⁹. Was ist falsch?“ (ebenso „4³ · 4² = 16⁵“, „4⁴ · 4² = 16⁶“, „3³ · 3³ = 9⁶“) | **mehrdeutig**: Zwei Antworten enden mit dem richtigen Ergebnis („Die Basis bleibt …: 4⁶“ und „Die Exponenten werden addiert, nicht malgenommen: 4⁶“); beide Sätze sind wahr. Ablenker so wählen, dass nur eine Antwort zutrifft |
| terme.potenzgesetze | fehler_finden | Ü S2 „Ein Kind rechnet: 3⁹ : 3³ = 3³. Was ist falsch?“ | Ablenker „Die Exponenten werden addiert, nicht malgenommen: 3⁶“ nennt dasselbe Ergebnis wie die richtige Antwort – verwirrend |
| terme.potenzgesetze | potenz_begriff | Ü S3 Würfelvolumen 4³, 6³, 7³, 9³ cm³ | reines Ausrechnen → Stufe 1–2 |
| terme.potenzgesetze | geteilt_gleiche_basis | Ü S3 „Berechne 10⁵ : 10³.“, „Berechne 2⁸ : 2⁶.“, „3⁷ : 3⁵“ | Grundform → Stufe 1–2 |
| terme.potenzgesetze | mal_gleiche_basis | Ü S3 „Berechne 2² · 2² mit dem Potenzgesetz …“ | Stufe 1 |
| terme.potenzgesetze | (Lücke) | – | Prüfungstyp „−3² vs. (−3)²“ (BMT8) fehlte bei den Übungen; ergänzt. Potenz einer Potenz ist nicht im Lehrplan Kl. 6 und wurde nicht verwendet |
| bruch.prozent | verstehen | Ü S3 „Bei 3 % Zinsen bekommt man für 800 € (2 000 €, 5 000 €) … Zinsen.“ | drei fast gleiche Aufgaben, einfache Rechnung → Stufe 2 |
| bruch.prozent | verstehen | Ü S3 „Sinkt ein Preis von 1000 € auf 500 € …“ | Schreibweise: „1 000 €“ (mit Leerzeichen) wie sonst im Bausatz |
| bruch.prozent | prozentsatz | Ü S3 „Wie viel Prozent einer Stunde sind 30 Minuten?“ | Stufe 1–2 |
| bruch.prozent | prozentwert | Ü S3 „Berechne 2,5 % von 320 €.“ | Stufe 2 (Grundform mit Komma) |
| bruch.prozent | (Lücke) | – | Prüfungstypen fehlten: Prozent vom Prozent, „x % weniger als“ (Grundwert erkennen), Prozentpunkte, Veränderung in beide Richtungen, Restprozent (99 %), Rückwärtsrechnen nach Rabatt/Aufschlag, aufeinanderfolgende Rabatte; ergänzt |
| daten.darstellen | absolute_haeufigkeit | Ü S2 „Wie oft wurde „Kunst“ häufiger genannt als „Deutsch“?“ (ebenso Test „Katze“/„Fisch“) | sprachlich missverständlich; besser „Wie viele Nennungen hat „Kunst“ mehr als „Deutsch“?“ |
| daten.darstellen | absolute_haeufigkeit | Ü S3 „In einer Strichliste stehen bei „Hund“: 3 Fünferbündel …“ | Stufe 1 |
| daten.darstellen | kreisdiagramm | Ü S3 „Ein Kreisausschnitt hat einen Winkel von 36°. Wie viel Prozent …?“ | Stufe 2 |
| daten.darstellen | relative_haeufigkeit | Ü S3 „Bei 20 Münzwürfen lag die relative Häufigkeit für „Zahl“ bei 5 % …“ | Stufe 2 |
| daten.darstellen | (Lücke) | – | Prüfungstypen fehlten: Gesamtzahl aus einem Kreis-/Säulenteil, Vierfeldertafel mit Lücken, Anteile zweier Gruppen vergleichen, Diagramm-Aussagen prüfen („verdoppelt“, „ein Drittel“), abgeschnittene Achse mit echter Prozentänderung; ergänzt |
| daten.kennwerte | modal_spannweite, median | ganze Lernkarten | laut themenliste `lehrplan_gym` ist für Kl. 6 nur „Arithmetisches Mittel bestimmen“ vorgesehen; Median/Spannweite kommen im BMT8 (Stoff bis Kl. 7) vor. Nicht geändert, nur zur Entscheidung gemeldet (evtl. als Vertiefung führen) |
| daten.kennwerte | modal_spannweite | Ü S3 „Bestimme die Spannweite von 7, 8, 7, 4, … −5 …“, „Temperaturen … Spannweite“ | Grundform mit negativen Zahlen → Stufe 2 |
| daten.kennwerte | mittel_tabelle | Ü S2/S3 „Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“ …“ | 6 Aufgaben mit wörtlich gleichem Text (nur andere Tabelle); Stufe 2 und 3 nicht unterscheidbar – für das Kind wirkt es wie dieselbe Aufgabe |
| daten.kennwerte | verstehen | Ü S3 Taschengeld-Ausreißer (4 fast gleiche Varianten) | gleiche Aufgabe vierfach, nur Zahlen anders |
| daten.kennwerte | (Lücke) | – | Prüfungstypen fehlten: gewichteter Mittelwert (Gruppen verschieden groß), Median aus Häufigkeitstabelle mit knapper Grenze, Notenspiegel zu vorgegebenem Durchschnitt, Formel ohne Klammern; ergänzt |

### (2) Prüfungsquellen und abgeleitete Aufgabentypen
Hinweis zur Quellenlage: Für das bayerische Gymnasium gibt es in Jgst. 6 keinen veröffentlichten zentralen Test. Genutzt wurden daher
(a) der **Bayerische Mathematik-Test Jgst. 8 (BMT8, ISB)** – er prüft zu Beginn von Kl. 8 den Stoff der Klassen 5–7, darunter Brüche, Prozent, Potenzen, Daten, Mittelwert/Median –,
(b) der **Jahrgangsstufentest Mathematik Jgst. 6 der Realschulen (ISB)** – überwiegend Stoff der 5. Klasse, nützlich für Aufgabenformate (Platzhalter, Zahlenstrahl, Fehler beschreiben, Diagramme),
(c) **Känguru der Mathematik 5/6** (Typen: Anteil einer Fläche, Mischungsverhältnisse, Rezepte skalieren) und die **IQB-VERA-8-Handreichungen** (Falle „Verhältnis statt Anteil“).
Aufgaben wurden nie wörtlich oder mit denselben Zahlen übernommen; Einkleidung und Zahlen sind eigen.

Adressen:
- BMT8 2021 A: https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2021/bmt8_2021_aufgaben_gruppe_a.pdf
- BMT8 2023 A: https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2023/BMT8_2023_Aufgaben_Gruppe_A.pdf
- BMT8 2024 A: https://isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/BMT8_2024_Aufgaben_Gruppe_A.pdf
- BMT8 2025 A: https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/BMT8_2025_Aufgaben_Gruppe_A.pdf
- BMT8 2014 B: https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2014/bmt8_2014_aufgaben_gruppe_b.pdf
- JT Realschule 6, 2024: https://isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/2024_JT_Mathe_6_Angabe.pdf
- JT Realschule 6, 2023: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2023/2023_JT_Mathe_6_Angabe.pdf
- JT Realschule 6, 2019 (Lösung): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2019/2019_jt_mathe_6_loesung.pdf
- JT Realschule 6, 2018 (Lösung): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2018/2018_jt_mathe_6_loesung.pdf
- JT Realschule 6, 2016 (Lösung): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2016/2016_07_07_jgst_2016_klasse_6_loesung.pdf
- JT Realschule 6, 2014 (Angabe): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2014/2014_07_17_jahrgangsstufe_6_angabe_geschwaerzt.pdf
- JT Realschule 6, 2025: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/2025_JT_Mathematik_6_Angabe.pdf
- Känguru 2021, Kl. 5/6: https://www.rudolf-hildebrand-schule.de/assets/downloads/kaenguru2021_56.pdf
- IQB VERA-8 „Anteile in geometrischen Objekten“: https://www.iqb.hu-berlin.de/media/exercise_files/VERA-8_Mathematik/anteileingeometrischenobjekten_Didaktische_Kommentierung.docx
- SMART-Sammlung Univ. Bayreuth Jgst. 5 (Notenverteilung zu Durchschnitt): https://btmdx1.mat.uni-bayreuth.de/smart/buch/smart_gym_j05.pdf

| Thema | genutzte Vorbilder | abgeleitete Aufgabentypen |
|---|---|---|
| zahlen.potenzen_zehner | BMT8 2021 Aufg. 6b, 2023 Aufg. 6, 2024 Aufg. 1b | Stapelhöhe = Anzahl · Dicke mit Einheitenwechsel; Restmenge bei Milliarden; Exponent so wählen, dass das Ergebnis stimmt; Vorsilben in Sachaufgaben (Download, Strom) |
| bruch.brueche | BMT8 2023 5a, 2024 3b/3c, 2025 6d; JT RS 6 2024 Nr. 16; Känguru 2021 A5/A8; IQB VERA-8 | Restanteil, Teil vom Rest, Ganzes aus gleichen Teilen, „mehr als ein Drittel?“, gleicher Anteil – verschiedene Anzahlen, Mischungen (Anteil vs. Verhältnis) |
| bruch.dezimal | JT RS 6 2023 Nr. 6, 2019 Nr. 6/19, 2024 Nr. 5; BMT8 2023 5a, 2024 3b, 2021 6c | größtmögliche Ziffer für einen Platzhalter, Zahlenstrahl mit ungewohnter Einteilung, Rundungsfallen (Übertrag, doppeltes Runden, Rückwärtsrunden), „0,3 ist ein Drittel?“, passenden Bruch wählen |
| bruch.rechnen | BMT8 2024 6a, 2025 Aufg. 5, 2014 B 1c/2, 2023 4b/5a; JT RS 6 2024 Nr. 7/15, 2018 Nr. 14, 2016 | Produkt aus bekanntem Ganzzahlprodukt, Rechner-Eingabe ohne Klammern, Anteil vom Anteil, Bruchterm durch Zahl teilen, Zoll-Umrechnung, Lücken/Rechenzeichen ergänzen, Kassenbon prüfen, Klammern setzen, Term zum Text |
| terme.potenzgesetze | BMT8 2021 Aufg. 1, 2023 1c, 2025 2b, 2021 6b/2023 6; Känguru/MO (Typ) | −3² vs. (−3)², Potenz eines Bruchs, Volumen beim Maßstab 1 : 10, Speicher-/Lichtjahr-Aufgaben, Endziffern, Potenzen ohne Ausrechnen vergleichen |
| bruch.prozent | BMT8 2021 Aufg. 5 und 6c, 2014 B 1c, 2023 5a/6, 2024 3a–c, 2025 6b/6d; IQB VERA-8 „Zwanzig Prozent“ | „20 % weniger als“, Prozentpunkte, Prozent vom Prozent, Restprozent, Gesamtzahl aus Anzahl und Prozentsatz, Veränderung in beide Richtungen, Rückwärts nach Rabatt/Aufschlag, Rabatt auf Rabatt |
| daten.darstellen | JT RS 6 2014 Nr. 2, 2019 Nr. 14, 2024 Nr. 19, 2025; BMT8 2014 B 3, 2021 6a, 2022 Aufg. 5, 2023 Aufg. 5, 2024 Aufg. 3, 2025 6a | Rangfolge aus Aussagen, fehlende Info bei abgeschnittener Achse, Gesamtzahl aus Diagrammteil, relative Häufigkeit eines Buchstabens, Kreisdiagramm in % auswerten, Tabelle mit Anteilen und Beträgen, „verdoppelt?“, Säule mit einem Drittel vergleichen |
| daten.kennwerte | BMT8 2025 Aufg. 5/6c, 2023 5b/5c, 2021 Aufg. 7; JT RS 6 2025; SMART Bayreuth | Mittelwert-Formel ohne Klammern, Median aus Häufigkeiten (knappe Grenze), gewichteter Mittelwert, gleiche Änderungen heben sich nicht auf, Median mit Wiederholungen, Notenspiegel zu vorgegebenem Durchschnitt |

### (3) Neue Aufgaben je Lernkarte und Stufe
Jede Lernkarte aller 8 Themen bekam genau **2 Übungen Stufe 2 + 4 Übungen Stufe 3** (Stufe 1: 0). Danach hat jede Lernkarte **10 Übungen Stufe 3** (vorher 6).
Von den 4 neuen Stufe-3-Aufgaben je Karte sind mindestens 2 nach Prüfungsvorbild und mindestens 1 Knobel-, Rückwärts- oder Fehler-finden-Aufgabe.

| Thema | Lernkarten | neu S2 | neu S3 | neu gesamt | Aufgaben alt → neu |
|---|---|---|---|---|---|
| zahlen.potenzen_zehner | 7 | 14 | 28 | 42 | 196 → 238 |
| bruch.brueche | 8 | 16 | 32 | 48 | 224 → 272 |
| bruch.dezimal | 7 | 14 | 28 | 42 | 196 → 238 |
| bruch.rechnen | 10 | 20 | 40 | 60 | 280 → 340 |
| terme.potenzgesetze | 7 | 14 | 28 | 42 | 196 → 238 |
| bruch.prozent | 7 | 14 | 28 | 42 | 196 → 238 |
| daten.darstellen | 6 | 12 | 24 | 36 | 168 → 204 |
| daten.kennwerte | 6 | 12 | 24 | 36 | 168 → 204 |
| **Summe** | **58** | **116** | **232** | **348** | 1 624 → 1 972 |

### (4) Themen ohne (belastbare) Prüfungsaufgaben
- Kein Thema ganz ohne Vorbild. Schwach belegt (nur indirekt über Sachaufgaben im BMT8, keine eigene Prüfungsaufgabe gefunden):
  **periodische Dezimalzahlen** (bruch.dezimal/periodisch), **Vorsilben Milli/Mikro/Nano** und **negative Exponenten** (zahlen.potenzen_zehner, terme.potenzgesetze).
  Dort sind die Stufe-3-Aufgaben eigene Knobel-/Fehleraufgaben im Prüfungsformat, nicht nach einer konkreten Prüfungsaufgabe.
- Mathematik-Olympiade (Schulrunde Kl. 6): keine frei zugängliche Aufgabe zu diesen Themen gefunden, nicht verwendet.
- Musterschulaufgaben bayerischer Gymnasien: keine frei zugänglichen, verlässlichen gefunden (nur Verlags-/Portalmaterial, nicht genutzt).

Offene Punkte für den Haupt-Chat: Befunde oben (vor allem die mehrdeutigen Auswahl-Aufgaben in terme.potenzgesetze/fehler_finden und bruch.rechnen „1/2 − □/□ = 1/4“,
der Textfehler in bruch.dezimal/verstehen) – Korrektur nur im Generator möglich und ändert Aufgabentexte, daher bewusst nicht angefasst.

## 2026-11-16 08:15 – STATUS
Thema 8/8 fertig: **daten.kennwerte** – 36 neue Übungen (je Lernkarte 2 × S2, 4 × S3). Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 07:55 – STATUS
Thema 7/8 fertig: **daten.darstellen** – 36 neue Übungen (je Lernkarte 2 × S2, 4 × S3). Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 07:30 – STATUS
Thema 6/8 fertig: **bruch.prozent** – 42 neue Übungen (je Lernkarte 2 × S2, 4 × S3). Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 07:10 – STATUS
Thema 5/8 fertig: **terme.potenzgesetze** – 42 neue Übungen (je Lernkarte 2 × S2, 4 × S3). Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 06:50 – STATUS
Thema 4/8 fertig: **bruch.rechnen** – 60 neue Übungen (je Lernkarte 2 × S2, 4 × S3). Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 06:25 – STATUS
Thema 3/8 fertig: **bruch.dezimal** – 42 neue Übungen (je Lernkarte 2 × S2, 4 × S3). Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 06:05 – STATUS
Thema 2/8 fertig: **bruch.brueche** – 48 neue Übungen (je Lernkarte 2 × S2, 4 × S3). Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 05:40 – STATUS
Thema 1/8 fertig: **zahlen.potenzen_zehner** – 42 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 10 Übungen Stufe 3.
Prüfskript OK, Unverändert-Nachweis JA (`python3 -I inhalte/generatoren/_schwer_kl6_nachweis.py zahlen.potenzen_zehner`).
Technik für alle Klasse-6-Themen: Abschnitt SCHWER am Ende des Generators, Hilfsdatei `_schwer_kl6.py` (eigener Zufallsstart, neue Aufgaben hinten angehängt,
nur Pool uebung), Nachweis `_schwer_kl6_nachweis.py` (vergleicht mit `origin/lernen-app`).
