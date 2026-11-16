# Postfach schwer-kl9 (Zehnte Runde, Klasse 9)

Neueste Meldung oben.

## 2026-11-16 05:06 – FERTIG
**Abschlussbericht Zehnte Runde, Klasse 9 (Zweig schwer-kl9).** 14 Themen, 87 Lernkarten, 522 neue Übungen. Alle Themen: `inhalt_pruefen` OK, Unverändert-Nachweis OK (alle alten Aufgaben Zeichen für Zeichen gleich, gleiche Reihenfolge, Lernkarten unverändert). Kein App-Code, keine Datenbank, keine Tests geändert.

**Technik:** `inhalte/generatoren/_schwer_kl9.py` – `anhaengen(datei, seed, bauplan)` hängt nach `bauen()` die neuen Übungen mit eigenem festem Zufallsstart (9901 … 9914) an (nur Pool uebung, Stufe 2/3, mit Tipp; Dubletten- und Mindestzahl-Prüfung je Lernkarte). Nachweis: `python3 -I inhalte/generatoren/_schwer_kl9.py <thema> …` vergleicht mit origin/lernen-app. Jeder Generator ist wiederholbar (zweiter Lauf erzeugt dieselbe Datei). Neue Aufgaben stehen am Ende von `aufgaben`; Einspielen mit `einheit_abgleichen(…, 'lassen')` sollte daher nur ergänzen.

**(3) Neue Aufgaben je Lernkarte:** überall 4 × Stufe 3 (davon 2 nach Prüfungsvorbild, 1 Knobelaufgabe) + 2 × Stufe 2. Damit hat jede Lernkarte jetzt 10 Stufe-3-Übungen (vorher 6).

| Thema | Lernkarte Stufe 3 + Stufe 2 | neu |
|---|---|---|
| zahlen.wurzeln_basis | abschaetzen 4+2, kubikwurzel 4+2, quadratwurzel 4+2, wurzel_deuten 4+2, wurzel_dezimal 4+2, wurzel_sache 4+2 | 36 |
| zahlen.reell | eingrenzen 4+2, nenner_rational 4+2, teilweise 4+2, wurzel_mal 4+2, zahlarten 4+2, zusammenfassen 4+2 | 36 |
| zahlen.rationale_exponenten | gleichung_exp 4+2, nte_wurzel 4+2, potenz_wert 4+2, umwandeln 4+2, verstehen 4+2, zusammenfassen 4+2 | 36 |
| gleichungen.quadratisch | ausklammern 4+2, diskriminante 4+2, ergaenzung 4+2, faktorisieren 4+2, loesungsformel 4+2, reinquadratisch 4+2, sachaufgabe 4+2 | 42 |
| gleichungen.potenz | anzahl 4+2, gerade 4+2, naeherung 4+2, sachaufgabe 4+2, umformen 4+2, ungerade 4+2 | 36 |
| gleichungen.lgs3 | eliminieren 4+2, loesen 4+2, parabel 4+2, pruefen 4+2, sachaufgabe 4+2, stufenform 4+2 | 36 |
| funktionen.quadratisch | bestimmen 4+2, extremwert 4+2, nullstellen 4+2, parameter 4+2, punkte 4+2, scheitel 4+2, umformen 4+2 | 42 |
| funktionen.potenz | negativ 4+2, parameter 4+2, symmetrie 4+2, verlauf 4+2, werte 4+2, wurzelfunktion 4+2 | 36 |
| abbildungen.aehnlichkeit | aehnlich 4+2, anwendung 4+2, flaeche_volumen 4+2, strahlensatz1 4+2, strahlensatz2 4+2, streckung 4+2 | 36 |
| trigo.pythagoras | anwendung 4+2, hypotenuse 4+2, kathete 4+2, koordinaten 4+2, raum 4+2, umkehrung 4+2 | 36 |
| trigo.rechtwinklig | anwendung 4+2, beziehungen 4+2, seite 4+2, seiten 4+2, verhaeltnisse 4+2, winkel 4+2 | 36 |
| trigo.allgemein | einheitskreis 4+2, flaeche 4+2, kosinussatz_seite 4+2, kosinussatz_winkel 4+2, satz_waehlen 4+2, sinussatz_seite 4+2, sinussatz_winkel 4+2 | 42 |
| gleichungen.trig | anwendung 4+2, anzahl 4+2, kosinus 4+2, sinus 4+2, tangens 4+2, umformen 4+2 | 36 |
| stochastik.verknuepft | additionssatz 4+2, bedingt 4+2, tafel_wkeit 4+2, verknuepfen 4+2, verstehen 4+2, vierfeld 4+2 | 36 |

**(2) Prüfungsquellen je Thema und abgeleitete Aufgabentypen** (Typ, Aufbau, Niveau übernommen; Wortlaut, Einkleidung und Zahlen eigen):
- **zahlen.wurzeln_basis:** BMT10 2023 A (Näherungswert einer Wurzel am Graphen von y = x²; eigene Aufgaben mit √3,2 und √5,5) https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2023/BMT10_2023_Aufgaben_Gruppe_A.pdf; BMT10 2024 B (Terme ohne Taschenrechner) https://isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/BMT10_2024_Aufgaben_Gruppe_B.pdf; Realschule 9 (I) Leistungsaufgaben (Fachbegriffe Radikand/Radizieren) https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Mathematik/Weiterentwicklung_Abschlusspruefung/Exemplarische_Leistungsaufgaben/rs_m_09_leistungsaufgaben_9i.pdf. → Typen: Wurzelterm ohne TR mit Falle (√(a² − b²)), Näherung am Graphen, Fachbegriffe, Einheiten (Liter → m), Rückwärtsrechnen.
- **zahlen.reell:** Realschule 9 (I) Leistungsaufgaben Nr. 2–4 (Behauptung zum Rationalmachen beurteilen, rational/irrational/reell, Lückentexte) – Adresse wie oben; BMT10 2024 B Aufg. 1 (Wurzelterme ohne TR). → Typen: Begriffe/Teilmengen begründen, Lückentext √□ = 5√3, Behauptung beurteilen, Nenner mit Summe rational machen.
- **zahlen.rationale_exponenten:** BMT10 2024 B Aufg. 1 (Potenzterme vereinfachen); BMT10 2009 A Aufg. 2/3 (Terme mit negativen Exponenten, Potenzfunktion mit Exponent 1/5, Gleichsetzen) https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2009/bmt10-2009-aufgaben-gruppe-a.pdf. → Typen: Terme ohne TR, Schnittstelle zweier Potenzgraphen, Aussage mit Gegenbeispiel widerlegen.
- **gleichungen.quadratisch:** BMT10 2023 A/B Aufg. 1 (quadratische Gleichung lösen) https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2023/BMT10_2023_Aufgaben_Gruppe_B.pdf; BMT10 2025 A Aufg. 1 (2x² − 14x = 0; Term ohne reelle Lösung angeben) https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/BMT10_2025_Aufgaben_Gruppe_A.pdf; BMT10 2024 B Aufg. 5d (Anhalteweg, Parameter); Realschule 9 (I) Nr. 20, 22 (Bremsweg, Gehege an der Hauswand). → Typen: offene Konstruktion „keine Lösung“, Gleichung zu gegebenen Lösungen, rechts ≠ 0, Gehege mit Nebenbedingung, Anhalteweg.
- **gleichungen.potenz:** BMT10 2009 A Aufg. 3 (Gleichsetzen zweier Potenzterme, Bedeutung der Lösungen für die Graphen); BMT10 2025 B Aufg. 1a (2x³ − 15x = 0) https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/BMT10_2025_Aufgaben_Gruppe_B.pdf; Abschlussprüfung Realschule Mathematik I 2025 (Runden, Raumgeometrie) https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2025/2025_mi_ht_l.pdf. → Typen: Schnittpunkte, Ausklammern statt Teilen, Lösungsanzahl am Graphen, Volumen/Liter.
- **gleichungen.lgs3:** Keine echten Prüfungsaufgaben speziell zu LGS mit 3 Unbekannten gefunden. Ersatzvorbilder: 65. Mathematik-Olympiade, 1. Runde Kl. 9/10, Aufgabe 651013 (zyklische Summen, Unlösbarkeit) https://www.ghr-bottrop.de/wp-content/uploads/2024/09/05_klasse9-10.pdf; Realschule 9 (I) Nr. 17–19 (LGS mit 2 Unbekannten, Lösungen zweier Schüler beurteilen); LehrplanPLUS-Beispiel „Parabel durch drei Punkte“. → Typen: Lösungen beurteilen, Summe aller Gleichungen, Parameter bestimmen, Parabel im Sachkontext (Brückenbogen), Preis-Sachaufgabe.
- **funktionen.quadratisch:** BMT10 2024 B Aufg. 2 (Nullstellen, Entstehung aus der Normalparabel, Wertemenge) und Aufg. 5 (Bremsweg); BMT10 2025 Aufg. 5b (Funktionswert deuten); Realschule 9 (I) Nr. 20–22 (Parabel aus Eigenschaften, Gehege mit Rundung); Abschlussprüfung Realschule Mathematik I 2024 B 3 (Rechtecke mit Eckpunkt auf Gerade, Extremwert) https://isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2024/2024_mi_ht.pdf; MSA Berlin/Brandenburg (Nullstellen und Scheitel) https://www.ghs-berlin.de/wp-content/uploads/2013/10/MSA2011-Aufgaben.pdf. → Typen: Wertemenge, Verschiebung beschreiben, Bremsweg ×4, Extremwert mit Abrunden, Punkt auf y = x.
- **funktionen.potenz:** BMT10 2009 A Aufg. 3 (Graph über Symmetrie ergänzen, Schnittpunkte); BMT10 2023 A Aufg. 3 (Wertemenge Wurzelfunktion); BMT10 2024 B Aufg. 7 (f(x) = 3/x, Rechteck mit konstanter Fläche, Punkt auf y = x); BMT10 2025 Aufg. 5b (Funktionswert im Sachzusammenhang). → Typen: Symmetrie nutzen, Term zum Graphen mit Punktprobe, Hyperbel-Rechteck, Wertemenge.
- **abbildungen.aehnlichkeit:** BMT10 2009 A Aufg. 6a (Monddistanz mit Perle vor dem Auge); BMT10 2023 A/B Aufg. 7 (DIN-Formate ähnlich, √2); BMT10 2025 Aufg. 6 (Strahlensatz führt auf Gleichung); Realschule 9 (I) Nr. 5, 6, 11 (Streckung: Z und k, Dachschräge, Kreisbogen bei doppeltem Radius); Musterschulaufgaben Kl. 9 laut Inhaltsverzeichnis (Straßensteigung, ähnlich ja/nein) https://www.lehmanns.ch/media/636170/1. → Typen: negative k erkennen, Ähnlichkeit widerlegen (Rahmen), Bruchgleichung aus Strahlensatz, Entfernungsschätzung, Steigung.
- **trigo.pythagoras:** BMT10 2009 A Aufg. 7 (Strecke √n mit Pythagoras); Realschule 9 (I) Nr. 8, 9, 10 (Tangentenabschnitt, Drahtmodell Pyramide, Punkte mit Abstand 5); Abschlussprüfung Realschule Mathematik II 2024 Teil A (rechnerisch zeigen, dass Dreieck rechtwinklig) https://isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2024/2024_mii_ht.pdf; MSA Berlin/Brandenburg 2011 Aufg. 3 (Fähre). → Typen: Tangente, Kantenmodell, Umkehrung im Koordinatensystem, Fähre, Würfeloberfläche (Ameise).
- **trigo.rechtwinklig:** BMT10 2023 A/B Aufg. 6 (sin-Wert aus Abbildung, „kein Winkel ist 30°“ begründen); BMT10 2024 B Aufg. 6b (trigonometrischer Term im Zylinder); BMT10 2025 Aufg. 4a (Parallelogrammfläche 20 · sin α); Abschlussprüfung Realschule Mathematik I 2023/2025 (Winkel mit tan im Quader und Dreieck) https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2023/2023_mi_ht_l.pdf. → Typen: rechtwinkliges Teildreieck im Körper, Begründen mit sin 30°, Flächenterm, Ablesen am Graphen.
- **trigo.allgemein:** BMT10 2025 Aufg. 4 (sin(α + 90°) am Einheitskreis, Flächenterm); Abschlussprüfung Realschule Mathematik I 2023 B 3.4 (Kosinussatz, dann Flächeninhalt mit Sinusformel), 2024 B 2/B 4 (Sinussatz in Figur, Winkel aus Länge). → Typen: Einheitskreis-Symmetrie, Fläche maximal bei 90°, „kein Dreieck“ bei sin > 1, Satzwahl begründen.
- **gleichungen.trig:** Abschlussprüfung Realschule Mathematik I 2023 Teil A (sin x = Wert, Lösungsmenge in [0°; 180°]); 2025 A 2.4/B 2.3 (Term mit sin/tan aufstellen, Winkel zu gegebenem Wert); 2024 B 4.3 (Winkel aus Formel); BMT10 2025 Aufg. 1b (Gleichung ohne Lösung). → Typen: Gleichung ohne TR, Winkel aus Flächen-/Volumenterm, Lösungsanzahl in erweitertem Bereich, Riesenrad.
- **stochastik.verknuepft:** BMT10 2023 A/B Aufg. 2 (Vierfeldertafel, P(A ∪ B) in %, Mengenausdruck ↔ Beschreibung); BMT10 2024 B Aufg. 3 (Kugeln 1–100, A ∩ B, A ∪ B); BMT10 2025 Aufg. 2 (Laplace-Voraussetzung); Abschlussprüfung Realschule Mathematik I 2023 B 2 (Baumdiagramm mit %), 2025 B 1 (Gegenwahrscheinlichkeit, Anteil aus Gleichung); Realschule 9 (I) Nr. 23 („bestimmt 4-mal Rot“); IQB-Lernaufgabe Grippetest https://www.iqb.hu-berlin.de/media/exercise_files/Lernaufgaben_Mathematik_Sek_I/Grippetest_Aufgabe.pdf. → Typen: Tafel aus Randsummen, bedingte Wahrscheinlichkeit beim Test, unmögliche Angaben erkennen.

**(4) Themen ohne echte Prüfungsaufgaben:** gleichungen.lgs3 (LGS mit drei Unbekannten kommt in den gefundenen bayerischen Tests/Abschlussprüfungen nicht vor; Ersatzvorbild Mathematik-Olympiade und Realschul-Aufgaben zu LGS mit 2 Unbekannten). Für alle anderen Themen gab es belastbare Vorbilder; der BMT10 prüft den Stoff der Jahrgangsstufe 9 direkt (Test zu Beginn der 10. Klasse).

**(1) Befundliste aus Teil 1** (vorhandene Aufgaben nicht geändert; Thema, Lernkarte, Aufgabe, Befund):

#### zahlen.wurzeln_basis
- wurzel_dezimal, Übung Stufe 3 „Berechne 4 · √(25/4). Gib das Ergebnis als gekürzten Bruch an.“ – Lösung 10/1: Ergebnis ist eine ganze Zahl, „gekürzter Bruch“ mit Nenner 1 verwirrt. Besser als Zahl-Aufgabe.
- wurzel_dezimal, Stufe 3 „Was ergibt √0,49?“ (Auswahl) – Grundaufgabe, eher Stufe 1.
- kubikwurzel, Stufe 3 „Berechne ∛8 · √4“, „∛27 · √9“ – Grundaufgaben, eher Stufe 1–2.
- abschaetzen, Stufe 3 „√1 605“, „√788“, „√1 291“ – gleicher Typ wie Stufe 1, nur größere Zahlen; falsch eingestuft (Stufe 2).
- Lücke (Schulaufgaben-Typ): √(a²) = |a| (Betrag) kommt nicht vor; Näherung am Graphen von y = x² fehlte (jetzt neu).
#### zahlen.reell
- zahlarten, Stufe 1/3 „Welche Zahl ist irrational?“ (22/7, 3,14, π, 3,1416 bzw. 3,141414…): Der Lösungsweg nennt Zahlen, die in der jeweiligen Auswahl nicht vorkommen („3,1414… ist periodisch“ / „3,1416“) – Lösungsweg und Auswahl passen nicht genau zusammen.
- zahlarten, Stufe 3 „Welche der Zahlen ist irrational? √107, √121, 0,23, −11“ – gleicher Typ wie Stufe 2, falsch eingestuft.
- wurzel_mal, Stufe 3 „√375 : √15“ – Standard (Stufe 2).
- Lücke: Wurzelterme mit Variablen und Definitionsmenge (√(x − 3) definiert für x ≥ 3) fehlen; laut Schulaufgaben Kl. 9 üblich.
#### zahlen.rationale_exponenten
- potenz_wert: Auswahl „Weg A / Weg B“ kommt als Stufe 2 und Stufe 3 im selben Typ vor – Stufe 3 falsch eingestuft.
- potenz_wert, Stufe 3 „64^(−3/2) als Dezimalzahl“ – Lösung 0,001953125 (9 Nachkommastellen): Eingabe unzumutbar; besser Lücke 1/□ wie bei 81^(−5/2).
- gleichung_exp, Stufe 3 „Löse x⁵ = −243“ – passt nicht zur Lernkarte „Gleichungen mit Bruch-Exponent (x > 0)“ (negative Lösung); gehört zu gleichungen.potenz.
- gleichung_exp, Stufe 3 „Löse x^(1/2) = 6“ – Grundaufgabe (Stufe 1–2).
- verstehen, Stufe 3 „x^(3/9) = x^(1/3)“ – gleicher Typ wie Stufe 2.
#### gleichungen.quadratisch
- diskriminante, Stufe 3 „Für welche Zahl c hat x² − 14x + c = 0 genau eine Lösung?“ (und weitere c-Varianten) – derselbe Typ steht auf Stufe 2; falsch eingestuft.
- ausklammern, Stufe 3 „Löse 7x² = 14x.“, „Löse 5x² = 30x.“ – nur ein Umstellschritt mehr als Stufe 2; eher Stufe 2.
- faktorisieren, Stufe 3: fast nur „x² − 7x + 12 = 0 durch Faktorisieren“ – ein Typ; Prüfungstyp „Gleichung zu gegebenen Lösungen angeben“ und „rechts steht nicht 0“ fehlten (jetzt neu).
- Lücke: offene Prüfungsform „Gib eine Gleichung/einen Term an, sodass … keine Lösung hat“ (BMT10 2025) fehlte (jetzt neu).
#### gleichungen.potenz
- gerade, Stufe 3 „Welche Lösungsmenge hat 5x² = 0?“ / „4x⁸ = 0“ – Grundaufgabe, eher Stufe 1–2.
- ungerade, Stufe 3 „Löse x⁵ = −0,03125“ – gleicher Typ wie Stufe 2 („x⁵ = −0,00032“), nur andere Zahl; falsch eingestuft.
- sachaufgabe, Stufe 2 Zinseszins („Guthaben wächst in 2 Jahren … Zinssatz“) – Zinseszins ist laut Themenliste Zusatzstoff Klasse 10 (finanzen.zinseszins); für Kl. 9 prüfen.
- Lücke: Lösungsanzahl am Graphen begründen (LehrplanPLUS „mit Skizzen begründen“) hatte keine Zeichnung (jetzt 2 Aufgaben mit Koordinatensystem).
#### gleichungen.lgs3
- pruefen, Stufe 3: sechs Aufgaben „Ist (… | … | …) Lösung des Systems …?“ – derselbe Typ wie Stufe 2 (Einsetzen); falsch eingestuft.
- eliminieren, Stufe 3 „Berechne (III) − 2 · (I)“ mit Lösung □y + □z = □ → [0, 1, 0]: Die Antwort „0y + 1z = 0“ ist eine ungewöhnliche Schreibweise (eigentlich z = 0); Schablone passt hier nicht.
- loesen, Stufe 3 „Wie viele Lösungen hat das System …?“ (unendlich viele) – über den LehrplanPLUS-Text („aufstellen und lösen“) hinaus; als Vertiefung in Ordnung, aber ohne Erklärung auf der Lernkarte.
- Keine echten Prüfungsaufgaben speziell zu LGS mit 3 Unbekannten gefunden; Vorbild nur MO 651013 (Schulrunde 9/10) und Realschul-Leistungsaufgaben zu LGS mit 2 Unbekannten.
#### funktionen.quadratisch
- extremwert, Stufe 3 „Ein Ball fliegt auf der Bahn h(x) = −0,05x² + 1x + 2“ – Schreibweise „1x“ statt „x“ (Formatierungsfehler im Generator).
- scheitel, Stufe 3 „Gib den Scheitel der Parabel y = −3(x + 3)² an.“ / „y = −0,5(x + 7)²“ – reines Ablesen, eher Stufe 2.
- parameter, Stufe 3: fünf von sechs Aufgaben „Ohne zu rechnen: Wie viele Nullstellen hat …?“ – ein einziger Typ.
- bestimmen, Stufe 3 „Parabel durch drei Punkte“ doppelt sich mit gleichungen.lgs3 (parabel) – kein Fehler, aber Überschneidung.
- Lücke: Wertemenge und „Wie entsteht der Graph aus der Normalparabel?“ (BMT10 2024) fehlten als Aufgabentyp (jetzt neu).
#### funktionen.potenz
- werte, Stufe 3 „Berechne f(−2) für f(x) = −2x³“ steht zweimal (einmal als Zahl-, einmal als Auswahl-Aufgabe) – fast Dublette; außerdem eher Stufe 2.
- verlauf, Stufe 3 „Welcher Graph liegt für 0 < x < 1 weiter oben …“ in vier fast gleichen Varianten – ein Typ.
- negativ, Stufe 3 „Für welche x ist f(x) = x⁻³ definiert?“ – Standard (Stufe 2).
- Lücke: Schnittpunkte zweier Potenzgraphen durch Gleichsetzen und deren Deutung (BMT10 2009) fehlte (jetzt neu).
#### abbildungen.aehnlichkeit
- flaeche_volumen, Stufe 3: alle sechs Übungen sind derselbe Typ („Modell im Maßstab 1 : n … Grundfläche/Volumen des Originals“) – ein Typ.
- streckung, Stufe 3: fünf von sechs Aufgaben „Strecke P mit Z und k“ – Routine, eher Stufe 2; nur „Zentrum aus P und P' bestimmen“ ist Stufe 3.
- Lücke: LehrplanPLUS nennt „entstehende Bruchgleichungen lösen“; eine Aufgabe mit der Unbekannten im Nenner fehlte fast ganz (jetzt neu: Schattenaufgabe, x : (x + 4)).
#### trigo.pythagoras
- anwendung, Stufe 3 „Eine Rampe steigt auf 600 cm waagrechter Länge um 17 cm an. Wie lang ist die Rampe? Runde auf ganze Zentimeter.“ – Lösung 600 cm (√360 289 ≈ 600,2) ist gleich der waagrechten Länge; die Aufgabe wirkt unsinnig bzw. bestätigt die Fehlvorstellung „kein Unterschied“. Zahlen ändern (größere Steigung).
- hypotenuse, Stufe 3 „Katheten 11 cm und 5 cm, Hypotenuse auf eine Nachkommastelle“ – Routine (Stufe 2); Stufe 3 enthält überwiegend Routine.
- Lücke: Prüfungstypen „Tangentenabschnitt am Kreis“, „Drahtmodell/Kantenlänge einer Pyramide“, „Strecke der Länge √n konstruieren“, „rechnerisch zeigen, dass ein Dreieck im Koordinatensystem rechtwinklig ist“ fehlten (jetzt neu).
#### trigo.rechtwinklig
- seiten, Stufe 3: alle sechs Übungen „Im Dreieck … ist der Winkel bei … ein rechter. Welche Strecke ist die Ankathete …?“ – Grundaufgabe mit anderen Buchstaben; falsch eingestuft (Stufe 1–2).
- winkel, Stufe 3: alle sechs „Berechne β aus a und c“ – Routine (Stufe 2).
- seite, Stufe 3: fast nur „Berechne c bzw. b auf eine Nachkommastelle“ – Routine.
- Lücke: Trigonometrie in Körpern (Zylinder, Quader), Begründungsaufgabe „kein Winkel ist 30°“, Flächeninhalt als Term mit sin α (BMT10 2023–2025, Realschul-Abschlussprüfung) fehlten (jetzt neu).
#### trigo.allgemein
- einheitskreis, Stufe 3: fünf fast gleiche Aufgaben „Es gilt sin x ≈ … Wie groß ist sin(180° + x)?“ – nur Vorzeichenwechsel, eher Stufe 2; außerdem „vier Nachkommastellen“ nur Abschreiben.
- kosinussatz_seite, Stufe 3: vier „Schiff fährt … dreht um … nach links“ – gute Einkleidung, aber immer derselbe Typ; der Dreieckswinkel ist 180° minus Drehwinkel – Lernkarte erklärt diesen Schritt nicht.
- sinussatz_seite, Stufe 3: vier gleiche „Zwei Beobachter … Baum auf der anderen Seite eines Sees“.
- Lücke: Flächeninhalt als Term in Abhängigkeit vom Winkel und „bei welchem Winkel maximal“ (BMT10 2025, Realschul-Abschlussprüfung) fehlte (jetzt neu).
#### gleichungen.trig
- sinus, Stufe 3 „Löse sin x = −0,7 …“ und „Löse sin x = −0,69 …“ haben dieselbe gerundete Lösung [224°, 316°] – praktisch Dublette.
- kosinus/sinus, Stufe 3: überwiegend derselbe Typ „Löse … = −0,xx, runde auf ganze Grad“ – Routine (Stufe 2).
- tangens, Stufe 3 „Eine Rampe steigt auf 8 m … Winkel“ / „Ein Weg hat 22 % Steigung“ – gehört inhaltlich zu trigo.rechtwinklig (keine Gleichung im Bereich 0°–360°).
- Lücke: Prüfungsform „Term in Abhängigkeit vom Winkel aufstellen und Winkel zu gegebenem Wert bestimmen“ (Realschul-Abschlussprüfung 2025) fehlte (jetzt neu).
#### stochastik.verknuepft
- **Fehler** verstehen, Übung Stufe 3: „P(A) = 0,6, P(B) = 0,5, P(A ∩ B) = 0,07. Jemand rechnet P(A ∪ B) = 1,1. Was stimmt?“ – Die Angaben sind unmöglich (bei P(A) + P(B) = 1,1 muss P(A ∩ B) ≥ 0,1 sein), und die als richtig markierte Antwort „P(A ∪ B) = 1,03“ ist größer als 1. Aufgabe sollte ersetzt/gesperrt werden; der Generator muss P(A ∩ B) ≥ P(A) + P(B) − 1 sicherstellen.
- verknuepfen, Stufe 3: sechs Aufgaben desselben Typs „Aus den Zahlen 1 bis n … Wie viele Zahlen liegen in …“.
- tafel_wkeit, Stufe 3: alle sechs „Die Tafel zeigt … Mit welcher Wahrscheinlichkeit …“ – Routine.
- Lücke: Laplace-Voraussetzung begründen (BMT10 2025), „bestimmt genau 4-mal“ beurteilen (Realschule 9), Mengenausdruck ↔ Beschreibung (BMT10 2023) fehlten (jetzt neu).


**Offen / Hinweise für den Haupt-Chat:**
- Der einzige echte Rechenfehler: stochastik.verknuepft / verstehen (P(A ∪ B) = 1,03). Bitte Aufgabe sperren oder den Generator korrigieren (P(A ∩ B) ≥ P(A) + P(B) − 1).
- Durchgehendes Muster: Viele alte Stufe-3-Übungen sind derselbe Typ wie Stufe 2 mit größeren Zahlen. Umstufen würde Lernstände berühren; Vorschlag: beim nächsten Umbau Stufe 3 → 2 setzen, wo oben genannt.
- Einheiten in neuen Aufgaben: u. a. „°“, „%“, „km/h“, „Zoll“, „FE“, „l“. Falls die App Einheiten prüft, bitte „FE“, „Zoll“ und „l“ kontrollieren.


## 2026-11-16 05:05 – STATUS
stochastik.verknuepft fertig: 36 neue Übungen, inhalt_pruefen OK, Unverändert-Nachweis OK. Achtung Befund: eine vorhandene Stufe-3-Aufgabe in „verstehen“ hat unmögliche Angaben (siehe Abschlussbericht).

## 2026-11-16 05:02 – STATUS
gleichungen.trig fertig: 36 neue Übungen, inhalt_pruefen OK, Unverändert-Nachweis OK.

## 2026-11-16 05:01 – STATUS
trigo.allgemein fertig: 42 neue Übungen (7 Lernkarten), inhalt_pruefen OK, Unverändert-Nachweis OK.

## 2026-11-16 04:58 – STATUS
trigo.rechtwinklig fertig: 36 neue Übungen, inhalt_pruefen OK, Unverändert-Nachweis OK.

## 2026-11-16 04:56 – STATUS
trigo.pythagoras fertig: 36 neue Übungen, inhalt_pruefen OK, Unverändert-Nachweis OK.

## 2026-11-16 04:54 – STATUS
abbildungen.aehnlichkeit fertig: 36 neue Übungen, inhalt_pruefen OK, Unverändert-Nachweis OK.

## 2026-11-16 04:52 – STATUS
funktionen.potenz fertig: 36 neue Übungen, inhalt_pruefen OK, Unverändert-Nachweis OK.

## 2026-11-16 04:51 – STATUS
funktionen.quadratisch fertig: 42 neue Übungen (7 Lernkarten), inhalt_pruefen OK, Unverändert-Nachweis OK.

## 2026-11-16 04:49 – STATUS
gleichungen.lgs3 fertig: 36 neue Übungen, inhalt_pruefen OK, Unverändert-Nachweis OK. Hinweis: Zu LGS mit drei Unbekannten keine echten Prüfungsaufgaben gefunden; Vorbild Mathematik-Olympiade 651013 und Realschul-Leistungsaufgaben (LGS mit 2 Unbekannten).

## 2026-11-16 04:46 – STATUS
gleichungen.potenz fertig: 36 neue Übungen, inhalt_pruefen OK, Unverändert-Nachweis OK.

## 2026-11-16 04:44 – STATUS
gleichungen.quadratisch fertig: 42 neue Übungen (7 Lernkarten), inhalt_pruefen OK, Unverändert-Nachweis OK.

## 2026-11-16 04:42 – STATUS
zahlen.rationale_exponenten fertig: 36 neue Übungen, inhalt_pruefen OK, Unverändert-Nachweis OK.

## 2026-11-16 04:40 – STATUS
zahlen.reell fertig: 36 neue Übungen (je Lernkarte 4 × Stufe 3 inkl. 2 Prüfungsvorbild + 1 Knobel, 2 × Stufe 2). inhalt_pruefen OK, Unverändert-Nachweis OK.

## 2026-11-16 04:38 – STATUS
zahlen.wurzeln_basis fertig: 36 neue Übungen (je Lernkarte 4 × Stufe 3, davon 2 nach Prüfungsvorbild und 1 Knobel, 2 × Stufe 2). inhalt_pruefen OK, Unverändert-Nachweis OK (168 alte Aufgaben gleich, gleiche Reihenfolge). Technik: inhalte/generatoren/_schwer_kl9.py (anhaengen + Nachweis). Befunde der Durchsicht folgen gesammelt im Abschlussbericht.
