# Postfach schwer-kl5 (Zehnte Runde: Durchsicht Klasse 5 + schwerere Aufgaben nach Prüfungsvorbild)

## 2026-11-16 09:30 – FERTIG
**Abschlussbericht Zehnte Runde, Klasse 5 (Zweig schwer-kl5).** 12 Themen mit gym_by 5, je Thema ein Commit. Alle Prüfskripte OK, Unverändert-Nachweis für alle 12 Themen JA
(`python3 -I inhalte/generatoren/_schwer_kl5_nachweis.py <thema …>` gegen origin/lernen-app; lernen-app hat seit meinem Start keine Änderung an inhalte/themen oder inhalte/generatoren).
Ausgelassen (kein Generator / nicht mit gym_by 5 in themenliste.json): zahlen.natuerlich, zahlen.teilbarkeit.

Technik: Hilfsdatei `inhalte/generatoren/_schwer_kl5.py` (Z/A/L/M/wahl; o.wert wird aus „c“ berechnet, Lückenwerte aus der c-Liste, richtige Auswahl über Rechnung oder Prüffunktion,
Anzahlen in der Kombinatorik durch vollständiges Aufzählen). Je Generator ein Abschnitt „SCHWER (Zehnte Runde)“ am Ende mit eigenem Zufallsstart (nur zum Mischen der Antworten);
die neuen Aufgaben werden hinter alle alten gehängt. Lernkarten, Zeichnungen, Test/Korrektur/Sicherung unverändert. Jede neue Aufgabe gelesen und von Hand nachgerechnet.

### (1) Befundliste aus Teil 1 (Durchsicht, je Lernkarte 12 Übungen gelesen; vorhandene Aufgaben NICHT geändert)
Gesamtbild: Keine falsche Lösung gefunden (alle Zahl-Aufgaben rechnet das Prüfskript nach; Auswahl-/Lückenaufgaben stichprobenhaft geprüft). Häufigstes Problem: Stufe 3 ist oft nur
„größere Zahlen“ oder viermal derselbe Aufgabentyp mit anderen Zahlen; einige Stufe-1/2-Einstufungen passen nicht.

#### zahlen.ganz
- addieren, Stufe 3 (z. B. „Berechne 217 + (−285)“, „Berechne (−306) + 205“): nur größere Zahlen, gleicher Gedanke wie Stufe 2 → eher Stufe 2.
- subtrahieren, Stufe 3 („Berechne 146 − (−41)“, „Berechne (−399) − 174“): ebenso nur größere Zahlen → eher Stufe 2.
- ketten, Stufe 3 („Berechne geschickt: 25 − 56 + 56 − 38“): gleicher Gedanke wie Stufe 2 („geschickt: 22 − 32 + 32 − 29“) → eher Stufe 2.
- Lücke laut Lehrplan/Prüfungen: Vorgänger/Nachfolger negativer Zahlen, Lückenaufgaben (□ + (−47) = −12), Fehler finden bei Vorzeichenregeln – jetzt in den neuen Aufgaben.
- Keine falschen Lösungen gefunden (12 Übungen je Lernkarte gelesen, alle Zahl-Aufgaben vom Prüfskript nachgerechnet).
#### zahlen.rechengesetze
- mal_ganz, Stufe 2 („Berechne (−3) · 2“, „Berechne 4 · (−2)“, „Berechne (−3) · 9“): gleich leicht wie Stufe 1 → falsch eingestuft (Stufe 1).
- schriftlich, Stufe 3 („Rechne schriftlich: 865 · 47“): nur größere Zahlen → eher Stufe 2 (gut als Stufe 3 sind die Fälle mit 0 im Ergebnis, z. B. 8 136 : 9 = 904).
- punkt_strich, Stufe 3 („Berechne 81 : 3 : 3 + 5 · 12“): längere Rechnung, kein anderer Gedanke → eher Stufe 2.
- Lücke: Division mit Rest im Sachzusammenhang („Wie viele Pakete höchstens?“), Lückenaufgaben mit Klammern (JT 2019: 3 · (□ − 15) = 18), Fehler beim vorteilhaften Rechnen (JT 2025) – jetzt ergänzt.
- Keine falschen Lösungen gefunden.
#### zahlen.potenzen_basis
- schreibweise, Stufe 3 („Was bedeutet 2⁷?“, „Was bedeutet 5⁴?“, „Was bedeutet 10⁴?“): Grundform direkt nach der Erklärung → falsch eingestuft (Stufe 1).
- quadrat, Stufe 3 („Welche Zahl ist eine Quadratzahl?“ mit 121/22/122 bzw. 124/121/22): leicht und zweimal fast dieselbe Aufgabe (gleiche richtige Antwort 121) → Stufe 1–2, Beinahe-Dublette.
- Lücke: Vorrang „Potenz vor Punkt vor Strich“ (JT 2020: 14² + 4; Fehler 2 · 5² = 10²) kommt in keiner Aufgabe vor; Zahlenfolgen aus Quadrat-/Potenzzahlen fortsetzen (JT 2018) fehlen – beides jetzt ergänzt.
- Keine falschen Lösungen gefunden.
#### groessen.einheiten
- laenge und masse, Stufe 3 („Welche Größe ist am größten: 7 kg, 6 920 g, 6 kg, 5 080 g?“, ebenso 11 kg …, 10 kg …, „6 km, 5 887 m, 5 km, 4 113 m“): Die richtige Antwort ist jedes Mal die einzige „runde“ größte Zahl mit der größeren Einheit – lösbar ohne Umrechnen → zu leicht für Stufe 3 (Stufe 1–2). Echte Prüfungsaufgaben mischen Komma- und Mehrnamenschreibweise (JT 2025: 5 kg 400 g < 5,44 kg < 3 t < 28 000 kg).
- verstehen, Stufe 3 („Stimmt das? Ein Kind wiegt etwa 40 t.“): offensichtlich → Stufe 1.
- masse, Stufe 1/2: reine Anhängen-von-Nullen-Aufgaben in beiden Stufen (z. B. s1 „38 t = ? kg“, s2 „32 t = ? kg“) – Stufen kaum unterscheidbar.
- Lücke: gemischte Einheiten mit „Falle“ (JT 2018: 12 m 6 cm = 1 206 cm), Umwandeln über mehrere Stufen (JT 2024: 671 dm in mm), Fehler beschreiben (JT 2020: 12 m − 50 cm; JT 2019: 2 h = 200 min), fehlende Information (JT 2019) – jetzt ergänzt.
- Keine falschen Lösungen gefunden.
#### groessen.proportional
- sach: Die Eier-Falle („3 Eier kochen 6 Minuten …“) kommt in Stufe 2 und dreimal in Stufe 3 vor, jeweils derselbe Gedanke; die Lied-Falle steht sogar in Stufe 1 („Ein Lied dauert 4 Minuten, wenn 4 Kinder es singen …“) → Stufen uneinheitlich, Stufe-3-Aufgaben nicht schwerer als Stufe 2.
- sach, Stufe 2 („Ein Hahn füllt in 4 Minuten 48 Liter. Ungefähr wie viele Liter laufen in 20 Minuten?“ → „etwa 200 Liter“): Das genaue Ergebnis 240 l ist leicht zu rechnen; „etwa 200“ wirkt dann falsch. Besser genaue Zahl-Aufgabe oder Optionen, bei denen 240 klar „etwa 250“ ist.
- dreisatz, Stufe 3 („20 Hefte kosten 80 €. 11 Hefte kosten wie viel €?“): Standard-Dreisatz → Stufe 2.
- Lücke: Dreisatz mit gesuchter Zeit (JT 2018: Einlass 600 Personen/30 min), nicht-ganze Zwischenwerte (JT 2019: 4 Bücher = 1 200 g), Faustregel Gewitter (JT 2025), Aufrunden im Sachzusammenhang (Farbdosen) – jetzt ergänzt.
- Keine falschen Lösungen gefunden.
#### geometrie.grundbegriffe
- verstehen, Stufe 3 („Stimmt die Aussage? Ein Winkel von 220° ist stumpf.“, „Eine Tangente schneidet den Kreis in zwei Punkten.“): reine Begriffsabfrage wie Stufe 1 („Ein Winkel von 96° ist spitz.“) → eher Stufe 1–2.
- lagebeziehungen, Stufe 3: zwei Aufgaben mit identischem Aufbau („g geht durch A(…) und B(…), h geht durch C(…) und D(…). Wie liegen g und h zueinander?“) und beide Male Antwort „g ⊥ h“ – Beinahe-Dublette; einmal „g ∥ h“ als richtige Antwort wäre besser.
- kreis_lage, Stufe 3: „Zwei Kreise … Radien 7 cm und 4 cm, Abstand 3 cm → 1 gemeinsamer Punkt“ (Berührung von innen) – fachlich richtig, aber die Lernkarte erklärt nur Kreis und Gerade; die Lage zweier Kreise wird nicht erklärt (Erklärung und Aufgabe passen nicht ganz zusammen).
- Lücke: Fehler „x und y vertauscht“ (JT 2020), Symbolschreibweise ∈, ⊥, ∥ (JT 2020), Zaun im Abstand um ein Rechteck (JT 2020), Winkel an der Leiter (JT 2020) – jetzt ergänzt.
- Keine falschen Lösungen gefunden.
#### geometrie.winkel
- verstehen, Stufe 3 („Stimmt die Aussage? Zwei stumpfe Winkel nebeneinander ergeben immer mehr als 180°.“): gleich dem vorgerechneten Beispiel der Lernkarte (dort Schritt für Schritt bewiesen) → keine neue Leistung; widerspricht der Regel „keine Aufgabe gleich dem Beispiel“ (das Prüfskript erkennt es nicht, weil der Wortlaut abweicht).
- drehungen, Stufe 3: viermal dieselbe Karussell-Aufgabe mit anderer Gondelzahl (10, 9, 3, 5 Gondeln) – kein Wechsel des Gedankens.
- ergaenzen, Stufe 2 („α = 241° wird zum Vollwinkel ergänzt“): gleiches Muster wie Stufe 1 → eher Stufe 1.
- Lücke: Winkel bei drei Geraden durch einen Punkt (JT 2018), Begründen mit Winkelbereich (JT 2020 Leiter), Kreisausschnitt (JT 2024), Fehler finden bei 180° statt 360° – jetzt ergänzt.
- Keine falschen Lösungen gefunden (geprüft u. a. „Nordosten + 225° = Westen“, Uhrzeigerwinkel 8:30 und 11:30).
#### geometrie.ortslinien
- Grundsätzlich: In themenliste.json steht gym_by 5, aber lehrplan_gym ist leer. Ortslinien (Mittelsenkrechte, Mittelparallele, Ortsbereiche) stehen im LehrplanPLUS Gymnasium erst in Jahrgangsstufe 7. Die Aufgaben bleiben deshalb bei Kreis/Parallele/Abstand längs einer Linie (ohne Pythagoras). Bitte Einordnung prüfen.
- sachsituationen, Stufe 3: viermal dieselbe Sender-Aufgabe („Zwei Sender … genau 6 km zu A und genau 6 km zu B …“), jedes Mal Antwort 2 – kein Wechsel, Antwort erratbar.
- parallelen, Stufe 3: zweimal „Wie viele Punkte … auf x = 2 … höchstens Abstand 3?“ mit gleichem Ergebnis 7 – Beinahe-Dublette.
- zwei_kreise: Die Lernkarte erklärt nur sich schneidende Kreise; Stufe-3-Aufgaben verlangen die Lage „Kreis im Kreis“ (r₂ − r₁), die nirgends erklärt wird.
- Prüfungsaufgaben: Bayerische Jahrgangsstufentests 6 enthalten keine Ortslinien (passend zum Lehrplan). Vorbilder: Klassenarbeiten Kl. 5 (Parallele mit Abstand, Punkte gleichen Abstands von g und h) und klassische Ortslinien-Aufgaben („Punkte mit Abstand 3 von g und 6 von P“).
- Keine falschen Lösungen gefunden.
#### messen.flaechen
- einheitsquadrate, Stufe 1: Gefragt ist „Wie viele Einheitsquadrate passen hinein?“, die Lösung hat aber die Einheit cm² (z. B. 36 cm²). Anzahl und Flächeninhalt werden vermischt – entweder nach dem Flächeninhalt fragen oder ohne Einheit lösen.
- einheitsquadrate, Stufe 3: „Rechteck aus 5 · 6 …“ und „Rechteck aus 6 · 5 … wird in beiden Richtungen doppelt so lang“ – gleiche Aufgabe mit vertauschten Faktoren, beide Lösung 120 (Beinahe-Dublette).
- rechteck, Stufe 3 („Ein Rechteck ist 3 m lang und 30 cm breit. Fläche in dm²?“ und zwei weitere gleicher Bauart): dreimal derselbe Gedanke in Stufe 3.
- Lücke: Größenvorstellung bei Flächen (JT 2020: 1 ha ≈ Fußballfeld), Rechteck mit vorgegebenem Umfang (JT 2018), Quadrat aus Umfang/Fläche (JT 2025), Umfang zusammengesetzter Figuren bleibt gleich (Känguru-Typ) – jetzt ergänzt.
- Keine falschen Lösungen gefunden.
#### messen.koerper_berechnung
- sachaufgaben, Stufe 1 („Ein Geschenkkarton ist 45 cm lang, 33 cm breit und 14 cm hoch. Wie viel cm² Papier …?“ → 5 154 cm²): vollständige Oberfläche mit großen Zahlen ist für Stufe 1 zu schwer (Stufe 2); die Aquarium-Aufgaben in Stufe 2 sind dagegen anspruchsvoller als manche Stufe-3-Aufgabe.
- oberflaeche, Stufe 3: viermal „Ein Würfel hat die Oberfläche … cm². Wie lang ist eine Kante?“ (384, 1 176, 486, 1 014 cm²) – derselbe Gedanke, nur andere Zahlen.
- zusammengesetzt, Stufe 3: viermal „Zwei gleiche Quader … aneinandergeklebt“ – derselbe Gedanke.
- Lücke: angemalter Würfel aus kleinen Würfeln (JT 2024: Abzählen am Würfel), Körper an Ecken/Kanten erkennen (JT 2018), Oberfläche mit gemischten Einheiten (Bayerischer Mathematik-Test 2000), Würfel in Schachtel packen (nicht Volumen teilen) – jetzt ergänzt. Netze/Schrägbilder (JT 2019, 2020, 2023) sind ohne Zeichenmöglichkeit nicht umsetzbar.
- Keine falschen Lösungen gefunden.
#### stochastik.kombinatorik
- grenzen, Stufe 3 („Wie viele Strecken kann man zwischen 6 Punkten zeichnen …“, ebenso 3, 5, 7 Punkte): derselbe Gedanke wie die Handschlag-Aufgaben in Stufe 1 → falsch eingestuft (Stufe 1–2); einmal mit 3 Punkten (Ergebnis 3) sogar leichter als Stufe 1.
- bedingungen, Stufe 3 („Aus den Ziffern 0, 1, 5, 6 … dreistellige Zahlen ohne doppelte Ziffer“ → 18): identischer Aufgabentyp und gleiches Ergebnis wie Stufe 2 („0, 3, 7, 9“ → 18); in Stufe 3 zweimal vorhanden.
- systematisch, Stufe 3 („Eis: 2 Sorten, 3 Soßen, 2 Streusel“ und „3 Sorten, 2 Soßen, 2 Streusel“): beide Ergebnis 12, Zählprinzip-Grundform → Stufe 1–2.
- Lücke: vierstellige Zahlen aus 4 Ziffernkarten mit Zusatzbedingung (JT 2019), Outfits mit Einschränkung (JT 2022), Färbeprobleme und Türme (Känguru), Rückwärtsfragen (Turnier mit 28 Spielen), „mindestens eine 7“ über das Gegenteil – jetzt ergänzt.
- Keine falschen Lösungen gefunden (u. a. geprüft: „Klassensprecher und Stellvertreter“ richtig als 20 ohne Teilen; Zahlenschloss 1 000 Codes richtig).
#### gleichungen.einfach
- umkehr_mal, Stufe 3 („Löse 9 : x = 3“, „Löse 20 : x = 2“): Der Typ „Zahl : x“ ist der richtige Stufe-3-Gedanke, aber 9 : x = 3 ist im Kopf sofort lösbar → eher Stufe 2.
- probe, Stufe 3: viermal derselbe Typ „x = … getestet, links kommt … heraus. Ist die Lösung größer oder kleiner?“ (Antworten nur „größer“/„kleiner“) – gleiche Idee, Antwort erratbar.
- aufstellen, Stufe 3: zweimal dieselbe Alters-Aufgabe („Mutter 3-mal so alt wie Tochter, zusammen 52 / 36“).
- ohne_loesung, Stufe 3 („0 · x = 1“ und „0 · x = 14“): zweimal derselbe Gedanke.
- Hinweis zur neuen Aufgabe „Für welche der Zahlen 3, 4, 5, 6 gilt 2 · x + 7 = 4 · x − 3?“ (probe, Stufe 3): Variable auf beiden Seiten, aber nur durch Einsetzen/Probe zu lösen – passt zu „Probe machen“, verlangt keine Umformung.
- Lücke: Lückenaufgaben mit Klammer (JT 2019: 3 · (□ − 15) = 18), Gleichungen mit negativen Zahlen (JT 2025: −23 + x = −12; JT 2024: □ : □ = −70), Rückwärts-Sachaufgaben (Känguru: Kinder in Zimmern) – jetzt ergänzt.
- Keine falschen Lösungen gefunden.

### (2) Prüfungsquellen und abgeleitete Aufgabentypen
Ehrlicher Hinweis: Freie Aufgaben des **Gymnasium**-Jahrgangsstufentests 6 habe ich nicht gefunden. Genutzt habe ich die frei veröffentlichten **Jahrgangsstufentests 6 der Realschulen
in Bayern (ISB)** – sie prüfen zu Beginn der 6. Klasse den Stoff der 5. Klasse, der weitgehend dem Gymnasium entspricht. VERA (Kl. 3/8) passt nicht zu Klasse 5. Keine Aufgabe ist wörtlich
oder mit denselben Zahlen übernommen; Vorbild sind Typ, Aufbau und Niveau.

Quellen (Adressen):
- JT 6 Realschule 2018: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2018/2018_jt_mathe_6_loesung.pdf
- JT 6 Realschule 2019: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2019/2019_jt_mathe_6_loesung.pdf
- JT 6 Realschule 2020: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2020/2020_jt_mathe_6_loesung.pdf
- JT 6 Realschule 2021: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2021/2021_jt_mathe_6_angabe.pdf
- JT 6 Realschule 2022: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2022/_A__2022_JT_Mathe_6_Angabe.pdf
- JT 6 Realschule 2024: https://isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/2024_JT_Mathe_6_Loesung.pdf
- JT 6 Realschule 2025: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/2025_JT_Mathematik_6_Loesung.pdf
- JT 6 Realschule 2016 (Textterme): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2016/2016_07_07_jgst_2016_klasse_6_loesung.pdf
- Mathematik-Test 2005 Jgst. 6 (Gleichung, Zebrastreifen): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2005/mt05_aus6.pdf
- SMART-Aufgabensammlung Uni Bayreuth, Gymnasium Jgst. 5 (enthält Aufgaben des Bayerischen Mathematik-Tests 2000/2004): https://btmdx1.mat.uni-bayreuth.de/smart/buch/smart_gym_j05.pdf
- Känguru der Mathematik 2023, Klassenstufen 5/6: https://www.mo-ni.de/fileadmin/user_upload/kaenguru2023_56.pdf
- Mathematik-Olympiade, 64. MO Schulrunde Kl. 5: https://rudolf-hildebrand-schule.de/assets/downloads/a641_05_aufgaben.pdf ; 60. MO Kl. 5: https://ong.berlin/wp-content/uploads/2020/08/Aufgaben-60-Mathematikolympiade-Klasse-5.pdf
- Klassenarbeiten Gymnasium Kl. 5: https://www.klassenarbeiten.de/data/dynamic/pdf/1722.pdf (ganze Zahlen, Zahlengerade) ; https://klassenarbeiten.de/gymnasium/klasse5/mathematik/koordinatensystem/1218.htm (Abstand, Parallele)
- Ortslinien (klassische Aufgaben): https://digital.ub.uni-paderborn.de/download/pdf/7895582.pdf ; https://lehrerfortbildung-bw.de/u_matnatech/mathematik/gym/bp2016/fb5/3_binnen/1_ortslinie/7_blatt_c/bd_ol_07_ab_c.pdf
- LehrplanPLUS Gymnasium Jgst. 5: https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/5/mathematik

Abgeleitete Aufgabentypen je Thema:
| Thema | Prüfungsvorbild → Aufgabentyp (Niveau, Falle) |
|---|---|
| zahlen.ganz | JT 2024 Nachfolger von −999; JT 2018 Mitte zwischen −7 und 5; JT 2025 Temperatur ändert sich regelmäßig; JT 2025 Lücke −23 + □ = −12; Klassenarbeit „zwei Zahlen gleich weit von …“; Känguru „kleinstes Ergebnis“ |
| zahlen.rechengesetze | JT 2019/2024 Punkt vor Strich; JT 2018 Klammern setzen; JT 2016 Textterm berechnen; JT 2020 Term zur Sachsituation ankreuzen; JT 2024 4 · 17 · 250 geschickt; JT 2025 Fehler beim vorteilhaften Rechnen; JT 2020 Division mit Rest im Sachkontext; JT 2019/2020 Runden ankreuzen |
| zahlen.potenzen_basis | JT 2020 14² + 4 (Potenz vor Punkt vor Strich); JT 2018 Folge der Quadratzahlen fortsetzen; JT 2019 Bakterien verdoppeln; BMT 2008 große Zahlen (Geldscheine) |
| groessen.einheiten | JT 2018 12 m 6 cm = … cm; JT 2024 671 dm in mm; JT 2025 Massen gemischt ordnen; JT 2020/2019 Fehler beschreiben (12 m − 50 cm, 2 h = 200 min); JT 2019 fehlende Information; JT 2019/2025 Schätzen mit Bezugsgröße; MT 2005 Zebrastreifen; Känguru Zaunpfähle |
| groessen.proportional | JT 2020 Güterwagen; JT 2024 Gondeln; JT 2025 Gewitter-Faustregel; JT 2018 Einlass-Zeit; JT 2019 Bücher/Gewicht und „ungefähr x-mal so lang“; Knobel Katzen/Mäuse |
| geometrie.grundbegriffe | JT 2020 Koordinaten vertauscht; JT 2020 Symbol D ∈ [EG]; JT 2020 Zaun im Abstand 1 m; JT 2020 Leiter-Winkel; JT 2025/2024 Quadrat aus u und A; JT 2019 Lage von Geraden a, b, c, d |
| geometrie.winkel | JT 2018 drei Geraden durch einen Punkt; JT 2020 Winkelbereich begründen; JT 2024 Kreissektor; Känguru Drehungen/Uhr |
| geometrie.ortslinien | keine bayerische Prüfungsaufgabe Kl. 5 (siehe 4); Klassenarbeit Kl. 5 und klassische Ortslinien-Aufgaben „Abstand 3 von g und 6 von P“ |
| messen.flaechen | JT 2020 1 ha ≈ Fußballfeld; JT 2021 Plakat mit Passfotos; JT 2018 Rechteck mit Umfang 14 cm; JT 2025/2024 Quadrat u/A; JT 2018 Fläche zwischen zwei Quadraten; JT 2020 Zaun im Abstand; Känguru Umfang zusammengesetzter Figuren |
| messen.koerper_berechnung | JT 2018 Körper mit 8 Ecken/12 Kanten; JT 2024 angemalter Würfel / Netz und Höhe; JT 2025 Eigenschaften ankreuzen; BMT 2000 Quaderoberfläche mit gemischten Einheiten; Känguru Würfelbauten |
| stochastik.kombinatorik | JT 2019 vierstellige Zahlen aus 4 Ziffern; JT 2018 Melodien aus Tönen; JT 2022 Outfits aus Hosen/Gürteln/Shirts; JT 2025 Teilbarkeit 789□□; MO 64 Reihenfolgen von Stationen; Känguru Türme und Färben |
| gleichungen.einfach | JT 2019 3 · (□ − 15) = 18; JT 2025 −23 + x = −12; JT 2024 □ : □ = −70; MT 2005 5 · 3 + 4 · x = 35; BMT 2004 „Zahl von 1 000 subtrahieren“; Känguru Kinder in Zimmern |

### (3) Neue Aufgaben je Lernkarte und Stufe
Jede Lernkarte: **2 neue Übungen Stufe 2 + 4 neue Übungen Stufe 3** (davon je Lernkarte mindestens 2 nach Prüfungsvorbild und mindestens 1 Knobel-/Fehler-finden-/Rückwärtsaufgabe).
Insgesamt **522 neue Übungen** (174 × Stufe 2, 348 × Stufe 3) auf 87 Lernkarten. Danach hat jede Lernkarte mindestens 9 Stufe-3-Übungen (vorher 5–6).

```
== zahlen.ganz: 224 alte Aufgaben unverändert: JA; neu: 48
   deuten             neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   zahlengerade       neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   ordnen             neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   betrag             neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   addieren           neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   subtrahieren       neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   ketten             neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   sach               neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
== zahlen.rechengesetze: 250 alte Aufgaben unverändert: JA; neu: 60
   punkt_strich       neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   klammern           neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   termaufbau         neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   vorteil            neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   differenz_summe    neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   verteilen          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   mal_ganz           neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   geteilt_ganz       neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   ueberschlag        neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   schriftlich        neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
== zahlen.potenzen_basis: 175 alte Aufgaben unverändert: JA; neu: 42
   schreibweise       neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   berechnen          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   quadrat            neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   vertauschen        neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   zehner             neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   negativ            neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   sach               neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
== groessen.einheiten: 224 alte Aufgaben unverändert: JA; neu: 48
   schaetzen          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   laenge             neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   masse              neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   zeit               neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   kommaschreibweise  neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   rechnen            neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   massstab           neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   verstehen          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
== groessen.proportional: 175 alte Aufgaben unverändert: JA; neu: 42
   erkennen           neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   vervielfachen      neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   pruefen            neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   einheit            neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   dreisatz           neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   geschickt          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   sach               neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
== geometrie.grundbegriffe: 196 alte Aufgaben unverändert: JA; neu: 42
   koordinaten        neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   strecken           neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   lagebeziehungen    neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   kreis_lage         neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   winkelarten        neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   vierecke           neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   verstehen          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
== geometrie.winkel: 196 alte Aufgaben unverändert: JA; neu: 42
   ergaenzen          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   kreuzung           neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   um_punkt           neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   uhr                neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   drehungen          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   figuren            neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   verstehen          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
== geometrie.ortslinien: 168 alte Aufgaben unverändert: JA; neu: 36
   kreislinie         neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   parallelen         neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   zwei_kreise        neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   verknuepfen        neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   sachsituationen    neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   verstehen          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
== messen.flaechen: 196 alte Aufgaben unverändert: JA; neu: 42
   einheitsquadrate   neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   rechteck           neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   einheiten          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   kommaschreibweise  neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   zerlegen           neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   sachaufgaben       neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   verstehen          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
== messen.koerper_berechnung: 168 alte Aufgaben unverändert: JA; neu: 36
   quader             neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   oberflaeche        neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   sachaufgaben       neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   zusammengesetzt    neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   volumen            neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   verstehen          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
== stochastik.kombinatorik: 196 alte Aufgaben unverändert: JA; neu: 42
   systematisch       neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   zaehlprinzip       neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   reihenfolgen       neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   baumdiagramm       neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   bedingungen        neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   grenzen            neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
   verstehen          neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 10
== gleichungen.einfach: 189 alte Aufgaben unverändert: JA; neu: 42
   waage              neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   umkehr_plus        neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   umkehr_mal         neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   zwei_schritte      neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   probe              neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   aufstellen         neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
   ohne_loesung       neu Stufe 2: 2  Stufe 3: 4  -> Stufe-3-Übungen gesamt: 9
```

### (4) Themen ohne (passende) Prüfungsaufgaben
- **geometrie.ortslinien**: Keine bayerischen Prüfungsaufgaben für Klasse 5 – das Thema steht im LehrplanPLUS Gymnasium erst in Jgst. 7 (lehrplan_gym ist leer). Vorbilder nur aus Klassenarbeiten Kl. 5 und klassischen Ortslinien-Aufgaben. Klassenzuordnung bitte prüfen.
- **Gymnasium-Jahrgangsstufentest 6**: nicht frei gefunden; ersatzweise Realschul-Tests (gleicher Stoff der Jgst. 5).
- **Netze, Schrägbilder, Zeichnen** (JT 2019/2020/2023/2024: Netz falten, Kanten ergänzen, Winkel zeichnen, Parallele zeichnen): ohne passende Zeichenart nicht als App-Aufgabe umsetzbar – App-Wunsch.

Offene Punkte für den Haupt-Chat: Einspielen mit einheit_abgleichen(…, 'lassen'); die Befunde aus (1) betreffen vorhandene Aufgaben und wurden bewusst nicht geändert (Lernstände).

## 2026-11-16 09:10 – STATUS
Thema 12/12 fertig: **gleichungen.einfach** – 42 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 9 Stufe-3-Übungen. Prüfskript OK, Unverändert-Nachweis JA.
Technik-Hinweis: Hier erzeugt baue() die Datei erst unter __main__; die neuen Übungen werden über eine Hülle um baue angehängt. Die Helfer sind als Modul _S eingebunden, damit A und Z aus _nachbau unangetastet bleiben.

## 2026-11-16 08:50 – STATUS
Thema 11/12 fertig: **stochastik.kombinatorik** – 42 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 10 Stufe-3-Übungen; alle Anzahlen durch vollständiges Aufzählen im Generator berechnet. Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 08:30 – STATUS
Thema 10/12 fertig: **messen.koerper_berechnung** – 36 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 10 Stufe-3-Übungen. Prüfskript OK, Unverändert-Nachweis JA.
App-Wunsch (bekannt): Netze und Schrägbilder von Quadern kommen in fast jedem Jahrgangsstufentest 6 vor (Netz falten, fehlende Kanten ergänzen, Würfelnetz-Pfeil) – ohne Zeichenart nicht als Aufgabe umsetzbar.

## 2026-11-16 08:10 – STATUS
Thema 9/12 fertig: **messen.flaechen** – 42 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 10 Stufe-3-Übungen. Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 07:50 – STATUS
Thema 8/12 fertig: **geometrie.ortslinien** – 36 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 10 Stufe-3-Übungen. Prüfskript OK, Unverändert-Nachweis JA.
FRAGE (Annahme getroffen, weitergearbeitet): Das Thema hat gym_by 5, aber lehrplan_gym ist leer – Ortslinien stehen im LehrplanPLUS Gymnasium erst in Jgst. 7. Ich habe die neuen Aufgaben ohne Mittelsenkrechte/Pythagoras gehalten (nur Abstände längs einer Linie). Bitte Klassenzuordnung prüfen.

## 2026-11-16 07:30 – STATUS
Thema 7/12 fertig: **geometrie.winkel** – 42 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 10 Stufe-3-Übungen. Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 07:10 – STATUS
Thema 6/12 fertig: **geometrie.grundbegriffe** – 42 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 10 Stufe-3-Übungen. Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 06:50 – STATUS
Thema 5/12 fertig: **groessen.proportional** – 42 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 9 Stufe-3-Übungen. Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 06:30 – STATUS
Thema 4/12 fertig: **groessen.einheiten** – 48 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 10 Stufe-3-Übungen. Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 06:10 – STATUS
Thema 3/12 fertig: **zahlen.potenzen_basis** – 42 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 9 Stufe-3-Übungen. Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 05:50 – STATUS
Thema 2/12 fertig: **zahlen.rechengesetze** – 60 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 9 Stufe-3-Übungen. Prüfskript OK, Unverändert-Nachweis JA.

## 2026-11-16 05:30 – STATUS
Thema 1/12 fertig: **zahlen.ganz** – 48 neue Übungen (je Lernkarte 2 × Stufe 2, 4 × Stufe 3), danach je Lernkarte 10 Stufe-3-Übungen.
Prüfskript OK, Unverändert-Nachweis JA (`python3 -I inhalte/generatoren/_schwer_kl5_nachweis.py zahlen.ganz`).
Technik: gemeinsame Hilfsdatei `inhalte/generatoren/_schwer_kl5.py` (Lösungen werden aus „c“ bzw. per Prüffunktion berechnet), Abschnitt „SCHWER (Zehnte Runde)“ am Ende des Generators, eigener Zufallsstart.
Themen ohne Generator in Klasse 5: zahlen.natuerlich und zahlen.teilbarkeit stehen nicht mit gym_by 5 in themenliste.json bzw. haben keinen Generator – ausgelassen.
