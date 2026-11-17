# Postfach bereinigen (Einundzwanzigste Runde, Teil A)

Neueste Meldung oben.

## 2026-11-18 03:30 – FERTIG: Teil A – Bereinigen (Gymnasium Kl. 5–10)

### Kurz
- Alle Punkte aus A1 (Zusammenlegen) und A2 (Verschieben) sind umgesetzt. 38 Themendateien geändert, alle 95 Themen: Prüfskript **OK**, 0 Gruppen „gleich gebaut hintereinander“.
- Je geänderter Lernkarte gelten die Regeln der Zwanzigsten Runde weiter (ohne überzählige: Stufe 1/2/3 mindestens 4/6/8 Übungen mit 2/3/4 Typen, Stufe 3 je Typ höchstens 3, höchstens 2 gleich gebaute je Typ und Stufe, 1–3 Knobel-Bordkarten). Das prüft der Motor beim Bauen; dazu die Gegenprobe ohne überzählige Übungen.
- **Nachweis** gegen `origin/lernen-app` (`_bereinigen_nachweis.py`): Jede alte Aufgabe ist Zeichen für Zeichen noch da, umgezogen (nur `l` und `t` neu), ersetzt, entfernt oder nur im Lösungsweg umformuliert – jeweils mit Eintrag in den Listen. Ergebnis: **NACHWEIS OK**. Themenschlüssel, `thema_id`, `block_id` und `klasse` unverändert, keine neuen Themen.
- Zahlen: 147 Aufgaben in ein anderes Thema bzw. eine andere Karte umgezogen, 22 innerhalb eines Themas (Neunerregel), 7 ganze Lernkarten umgezogen, 21 Lernkarten entfallen bzw. umgezogen, 5 Karten zur Vertiefung, 1 neue Vertiefungskarte. 53 Fragetexte ersetzt (Lösung gleich), 45 Aufgaben einzeln entfernt, 64 neue Aufgaben (davon 16 Test/Korrektur/Sicherung, 3 Knobel), 9 Lösungswege umformuliert.
- Alle Einzellisten (Umzüge, Ersetzt, Entfernt, Neu, Verworfen): **`inhalte/postfach/bereinigen-listen.md`**.
- Technik: Jeder betroffene Generator hat am Ende einen Abschnitt BEREINIGEN. Er ruft `_bereinigen.py` (Motor) mit den Schritten aus `_br_plan.py` auf – nach allen früheren Runden. Was aus einem anderen Thema übernommen wird, kommt aus dessen Stand **vor** dem Bereinigen (der Motor baut das Quellthema dafür im selben Lauf).
- Commits: je Paar bzw. Punkt einer (11 Commits). Wo ein Umzug zwei Themen betrifft, stehen beide im selben Commit – sonst wäre ein Zwischenstand mit doppeltem oder fehlendem Stoff entstanden (Abweichung von „ein Thema = ein Commit“, Lesart).

### Umzugstabelle (Pflicht) – für die Lernstände

„ganze Karte“: Karte mit allen Pools und gleichem Schlüssel `l` umgezogen – Lernstand 1 : 1 mitnehmen. „entfällt“: Karte gibt es nicht mehr; Lernstand nach der Spalte „Ziel für den Lernstand“ mitnehmen (dort liegt jetzt der Stoff).

| altes Thema / alte Lernkarte | → neues Thema / neue Lernkarte | Art | Aufgaben übernommen |
|---|---|---|---|
| gleichungen.einfach / umkehr_plus | zahlen.ganz / umkehraufgabe | entfällt | 7 |
| gleichungen.einfach / umkehr_mal | zahlen.rechengesetze / umkehraufgabe_mal | entfällt | 6 |
| messen.koerper_berechnung / volumen (Vertiefung) | messen.volumen / quader (1), einheitswuerfel (1) | entfällt | 2 |
| messen.koerper_berechnung / verstehen | messen.volumen / verstehen | Karte bleibt; 8 Volumen-Aufgaben raus, 2 umgezogen | 2 |
| zahlen.teilbarkeit / ggt | bruch.brueche / ggt (vor kuerzen) | ganze Karte | alle 35 |
| zahlen.teilbarkeit / kgv | bruch.brueche / kgv (vor vergleichen) | ganze Karte | alle 35 |
| zahlen.teilbarkeit / quersumme | zahlen.teilbarkeit / neunerregel (neu, Vertiefung) | Karte bleibt (nur 3); 9er-Aufgaben umgezogen | 22 |
| groessen.proportional / erkennen | groessen.proportional / erkennen | Vertiefung | – |
| terme.potenzgesetze / mal_gleiche_basis | terme.umformen / mal_gleiche_basis | ganze Karte | alle 42 |
| terme.potenzgesetze / gleicher_exponent | terme.umformen / gleicher_exponent | ganze Karte | alle 42 |
| terme.potenzgesetze / geteilt_gleiche_basis | terme.umformen / geteilt_gleiche_basis | ganze Karte, dort Vertiefung | alle 43 |
| terme.potenzgesetze / anwenden | terme.umformen / anwenden | ganze Karte, dort Vertiefung | alle 41 |
| terme.potenzgesetze / fehler_finden | terme.potenzgesetze / fehler_finden | Vertiefung | – |
| terme.potenzgesetze / negativer_exponent | terme.potenzgesetze / negativer_exponent | Karte bleibt; 3 Aufgaben mit Basis 10 raus | – |
| bruch.prozent / zinsen | finanzen.zinsen / jahreszinsen (4), jahreszinsen_komma (2), zinssatz (2), kapital (2), monatszinsen (1), zeitanteil (1) | entfällt | 12 |
| daten.kennwerte / modal_spannweite | daten.boxplot / kennwerte | entfällt | 13 |
| daten.kennwerte / median | daten.boxplot / median | entfällt | 11 |
| daten.kennwerte / verstehen | daten.boxplot / mittel_median | entfällt | 14 |
| geometrie.konstruktion / parallelen | geometrie.winkelsaetze / stufen_wechsel | entfällt | 7 |
| geometrie.konstruktion / winkelsumme | geometrie.winkelsaetze / innenwinkelsumme | entfällt | 5 |
| geometrie.konstruktion / satz_kehrsatz | geometrie.kreis / umkehrung | Karte bleibt; Thales-Aufgaben raus | 1 (1 verworfen) |
| geometrie.konstruktion / gleichschenklig | geometrie.kreis / thales | Karte bleibt; 1 Thales-Aufgabe raus | 1 |
| abbildungen.kongruenz / parkett (Vertiefung) | geometrie.winkelsaetze / parkett (nach vieleck) | ganze Karte, bleibt Vertiefung | alle 35 |
| funktionen.gebrochen / indirekt | groessen.indirekt / graph (2), produkt (7) | entfällt | 9 |
| funktionen.gebrochen / indirekt_sach | groessen.indirekt / sach | entfällt | 7 |
| messen.kreisberechnung / zylinder | messen.prisma_zylinder / zylinder_volumen (8), zylinder_oberflaeche (2) | entfällt | 10 |
| gleichungen.formeln / geometrie | messen.prisma_zylinder / prisma_umstellen (3), raum.pyramide_kegel_kugel / pyr_volumen (1) | Karte bleibt; Prisma/Pyramide raus | 4 |
| raum.schraegbilder / laengen | messen.koerper_darstellung / schraegbild (8), raum.schraegbilder / pyramide (2) | entfällt | 10 |
| raum.pyramide_kegel_kugel / pyr_volumen | raum.schraegbilder / pyramide | Karte bleibt; 4 Aufgaben Seitenkante/Höhe raus | 3 |
| funktionen.quadratisch / nullstellen | funktionen.quadratisch / schnittpunkte | Karte bleibt; Parabel–Gerade raus | 1 |
| gleichungen.lgs3 / pruefen, stufenform, eliminieren | (gleich) | Vertiefung | – |
| gleichungen.trig / sinus, kosinus, anzahl | funktionen.trig / periode (3), werte (1) | Karten bleiben; Graphen und Bereiche über 360° raus | 4 |
| funktionen.exponential_log / zeitpunkt | gleichungen.exponential / wachstum (8), mit_log_loesen (2) | entfällt | 10 |
| stochastik.mehrstufig / simulation | stochastik.mehrstufig / pi_schaetzen | Karte bleibt; 2 π-Aufgaben raus | 2 |
| stochastik.simulation / monte_carlo | stochastik.mehrstufig / pi_schaetzen | Karte bleibt; 7 Kreis-Aufgaben raus | 3 |
| funktionen.ganzrational / nullstellen | gleichungen.polynom / substitution | Karte bleibt; 3 Substitutions-Aufgaben raus | 3 |

### Was ich je Punkt gemacht habe (und welche Lesart)

**A1 Zusammenlegen**
- **Kl. 5 Umkehraufgaben:** Stoff bleibt in zahlen.ganz (Plus/Minus) und zahlen.rechengesetze (Mal/Geteilt) – beide kommen vor gleichungen.einfach. gleichungen.einfach behält waage, zwei_schritte, probe, aufstellen, ohne_loesung; zwei_schritte bekommt das Wort „umkehren“ mit Verweis auf die Umkehraufgaben.
- **Kl. 5 Volumen ↔ messen.volumen (Kl. 6):** Volumen steht laut M6 2.2 in Kl. 6. Vertiefung „volumen“ entfällt (messen.volumen deckt sie ab, eine Knobel-Aufgabe war sogar gleich). Aus „verstehen“ gehen die 7 Volumen-Aussagen und eine Volumen-Knobel-Aufgabe raus; 7 neue Aussagen zu Oberfläche und Kanten und eine neue Knobel-Aufgabe füllen auf. Ziel und Merke ohne Volumen.
- **Kl. 6 negativer Exponent:** Lesart: Doppelt war die Basis 10 (10⁰, 1/1 000 = 10⁻³). Die bleibt in zahlen.potenzen_zehner (zuerst). terme.potenzgesetze/negativer_exponent behält die allgemeine Basis, weil M6 1.4 genau das verlangt („negative ganzzahlige Exponenten als Bruch mit Zähler 1“), und verweist im Merksatz auf 10⁻ⁿ. Zwei neue Test-Aufgaben (Basis 7, 6) ersetzen die mit Basis 10.
- **Kl. 6 Zinsen:** Lesart: Der Stoff bleibt im eigenen Flug finanzen.zinsen (direkt nach bruch.prozent, beide Kl. 6). Wörtlich wäre bruch.prozent „zuerst“ – dann müsste aber ein ganzer Flug weg. bruch.prozent/zinsen entfällt; 12 Aufgaben ziehen um.
- **Kl. 7 Winkel an Parallelen, Winkelsumme:** Stoff bleibt in geometrie.winkelsaetze (Reihenfolge 4). Die beiden Karten in geometrie.konstruktion (8) entfallen; 12 Stufe-3- und Knobel-Aufgaben ziehen um.
- **Kl. 7 Boxplot ↔ Kennwerte:** zusammen mit A2 gelöst (siehe dort).
- **Kl. 8 indirekte Proportionalität:** Stoff bleibt in groessen.indirekt (5). funktionen.gebrochen (6) verliert indirekt und indirekt_sach; Ziel und Merke verweisen auf den vorigen Flug.
- **Kl. 8 Schrägbild / Ecken-Kanten-Flächen:** Stoff bleibt in messen.koerper_darstellung (Kl. 8). In raum.schraegbilder entfällt laengen (Schrägbilder von Prismen); die Pyramiden-Schrägbilder bleiben in raum.schraegbilder/pyramide.
- **Kl. 8 Zylinder:** Lesart wie bei den Zinsen: messen.prisma_zylinder ist der eigene Flug (Volumen begründet, Oberfläche über das Netz). Das Netz kommt erst in koerper_darstellung (13), also nach kreisberechnung (12). Deshalb entfällt kreisberechnung/zylinder.
- **Kl. 9 Parabel–Gerade:** die Aufgabe zieht von nullstellen nach schnittpunkte; nullstellen bekommt eine neue Stufe-3-Aufgabe (Parameter c für genau eine Nullstelle).
- **Kl. 10 Logarithmus-Gleichungen:** Lesart: Der Stoff bleibt in gleichungen.exponential, wo das Rechnen mit Logarithmen und die Potenzregel erklärt werden. funktionen.exponential_log/zeitpunkt übte ihn vorher, ohne Erklärung (so auch in durchsicht-kl10). Das ist zugleich ein Fall für A2. Die Karte zeitpunkt entfällt, 10 Aufgaben ziehen um.
- **Kl. 10 π-Schätzung:** Stoff bleibt in stochastik.mehrstufig/pi_schaetzen. Die Kreis-Aufgaben aus mehrstufig/simulation und simulation/monte_carlo ziehen dorthin oder entfallen. monte_carlo bleibt eine Karte zur Flächenschätzung allgemein: 5 neue Aufgaben, simulation 2 neue (Erwartungswert).
- **Kl. 10 Pyramide:** Seitenkante und Höhe der quadratischen Pyramide (Pythagoras) bleiben in raum.schraegbilder/pyramide (8). pyr_volumen (9) verliert diese 4 Aufgaben und bekommt 3 neue zum Volumen. Lesart: Die Durchsicht nannte „Schrägbild der Pyramide“. Eine Schrägbild-Aufgabe gab es in pyr_volumen nicht. Doppelt waren diese Pythagoras-Rechnungen an der Pyramide.

**A2 Verschieben**
- **zahlen.teilbarkeit:** ggT und kgV → bruch.brueche, ganze Karten vor kuerzen bzw. vor vergleichen (M6 1.1: Hauptnenner, auch über die Primfaktorzerlegung). Die **Neunerregel** steht in keiner Klasse des Lehrplans. Deshalb ist sie jetzt eine eigene Vertiefungskarte „neunerregel“ im alten Thema (neuer Kartentext, 11 neue Übungen, 1 Knobel). Die 22 Aufgaben mit 9 zogen aus quersumme dorthin, auch Test, Korrektur und Sicherung („durch 3 oder durch 9?“). quersumme heißt jetzt „Teilbar durch 3“: Kartentext ohne 9, 8 neue Übungen, 1 Knobel und 10 neue Test-, Korrektur- und Sicherungsaufgaben „Ist n durch 3 teilbar?“.
- **geometrie.ortslinien:** „y = 2“ → „waagrechte Gerade durch den Punkt (0 | 2)“, „x = 2“ → „senkrechte Linie durch (2 | 0)“. Ersetzt sind 29 Fragetexte und die Karte parallelen; Antwortschablonen heißen jetzt „(0 | □)“. Lösungen und Grafiken bleiben.
- **geometrie.winkel/uhr:** Statt „0,5° pro Minute“ heißt es „1° in 2 Minuten“, im Merksatz und in 5 Lösungswegen. Alle Ergebnisse waren schon ganzzahlig, Fragetexte bleiben.
- **groessen.proportional/erkennen:** Vertiefung. Gymnasium: das Wort „proportional“ kommt erst mit den Funktionen in Kl. 8. Realschule: M6 Lernbereich 6 (Quelle unten). Ein passendes Thema in Kl. 6/7 gibt es nicht.
- **terme.potenzgesetze:** M7 1.1 verlangt Produkte von Potenzen bei gleicher Basis oder gleichem Exponenten und Potenzen von Potenzen. Deshalb ziehen mal_gleiche_basis und gleicher_exponent als Pflicht nach terme.umformen, neuer Bereich „Potenzen zusammenfassen“. geteilt_gleiche_basis (Quotienten stehen nicht in M7) und anwenden (mit Quotienten gemischt) ziehen mit, dort als Vertiefung. Im Kl.-6-Flug bleiben potenz_begriff und negativer_exponent als Pflicht, fehler_finden als Vertiefung (mischt M6-Grundlagen mit Fehlern bei den Gesetzen). Ziel, Merke und Bereichstitel sind angepasst.
- **daten.kennwerte:** Modalwert, Spannweite und Median stehen nicht in M6, der Median steht in M7. modal_spannweite, median und verstehen (Mittelwert gegen Median) entfallen, 38 Aufgaben ziehen nach daten.boxplot. daten.kennwerte behält die drei Mittelwert-Karten.
- **abbildungen.kongruenz/achsenspiegelung:** Ersetzt sind 24 Fragetexte und die Karte. Die Achse heißt jetzt „senkrechte Achse durch (3 | 0)“, „waagrechte Achse durch (0 | 2)“ oder „Gerade durch (0 | 0) und (1 | 1)“. Antworten „x = □“ werden zu „(□ | 0)“. Geraden in Grafiken heißen „a“ statt „y = x“. 3 Lösungswege sind umformuliert.
- **geometrie.konstruktion/satz_kehrsatz:** Die Thales-Aufgabe zieht nach geometrie.kreis/umkehrung. Die Beweisschritte-Aufgabe passte nicht mehr in kreis/beweis (dort schon 3 × verknuepfen) und entfällt. Neu: 2 Transfer-Aufgaben. Aus gleichschenklig zieht 1 Thales-Aufgabe nach kreis/thales, neu ist 1 Fehler-Aufgabe.
- **abbildungen.kongruenz/parkett:** ganze Karte nach geometrie.winkelsaetze (nach vieleck), bleibt Vertiefung.
- **gleichungen.formeln:** Prisma- und Pyramiden-Aufgaben raus (Prisma kommt erst in prisma_zylinder, Pyramide in Kl. 10); 4 davon ziehen dorthin. Neu: 2 Umkehr-Aufgaben, 1 Prüfungs-Aufgabe, 1 Sicherung.
- **stochastik.verknuepft/bedingt:** war schon Vertiefung – keine Änderung (siehe „Für Sebastian“).
- **gleichungen.lgs3:** pruefen, stufenform, eliminieren → Vertiefung.
- **gleichungen.trig:** Geprüft, was nach der neuen Reihenfolge noch vorgreift: Graphen von sin/cos und Lösungsbereiche über 360° (beides Kl. 10, funktionen.trig). 4 Übungen ziehen nach funktionen.trig, 4 entfallen. Die 3 Test-/Sicherungsaufgaben mit Graph sind durch Fassungen ohne Graph ersetzt (neu, siehe Liste 5).
- **funktionen.ganzrational/nullstellen:** die beiden Substitutions-Aufgaben und eine dritte biquadratische (x⁴ − 5x² + 4) → gleichungen.polynom/substitution; neu: 3 Stufe-3-Aufgaben ohne Substitution.

### Für Sebastian (nur gemeldet, nicht geändert)
1. **Potenzen von Potenzen (M7 1.1)** hat in terme.umformen noch keine Karte. Vorschlag: neue Karte „(aᵐ)ⁿ = aᵐ·ⁿ“ (nur Vorschlag, nicht angelegt).
2. **Kartenzahl:** terme.umformen hat jetzt 12 Karten (10 Pflicht), bruch.brueche 12. Die README nennt 4–10. Andere Flüge haben schon mehr (rechengesetze 14).
3. **terme.potenzgesetze** heißt weiter „Potenzgesetze“, enthält in Kl. 6 aber nur noch Potenzen und negative Exponenten. Ein neuer Titel in der Themenliste wäre eine Planänderung (Teil B).
4. **Neunerregel:** Steht in keinem Gymnasium-Lehrplan 5–10, deshalb ist sie Vertiefung. Falls sie ganz wegsoll: Karte neunerregel streichen.
5. **gleichungen.trig/tangens** löst tan x = v für Winkel über 90°. Der Tangens am Einheitskreis wird in trigo.allgemein nicht erklärt (dort nur Sinus und Kosinus). Das ist ein möglicher Vorgriff; ich habe nichts geändert, weil die ganze Karte betroffen wäre.
6. **stochastik.verknuepft/bedingt:** Ist Vertiefung, die Stufe-3-Aufgaben nutzen aber Baumdiagramme (Kl. 10, stochastik.mehrstufig). Ein Baum-Schritt auf der Karte fehlt weiterhin.
7. **Klasse in der Datei:** raum.schraegbilder und stochastik.simulation tragen in der Datei `gym_by 8`, stehen in der Themenliste aber in Kl. 10. Für Teil B (Mindeststand) entscheidet das, wo der Stoff „zuerst“ ist: Kommt stochastik.simulation nach Kl. 8, gehört die π-Schätzung dorthin.
8. **Kartentexte nach dem Entfernen:** In funktionen.gebrochen, gleichungen.einfach, geometrie.konstruktion, daten.kennwerte, bruch.prozent, messen.kreisberechnung, raum.schraegbilder und terme.potenzgesetze habe ich die übrigen Karten per Suche auf Verweise auf entfallenen Stoff geprüft: keine gefunden. funktionen.gebrochen beginnt jetzt mit definitionsmenge – ob der Einstieg ohne die Karte indirekt gut trägt, bitte bei der Freigabe ansehen.
9. **Verworfene Aufgaben** (Liste 7): Beim Zusammenlegen fielen Aufgaben weg, wenn die Zielkarte schon 3 Aufgaben desselben Stufe-3-Typs oder 3 Knobel-Bordkarten hatte. Sie sind nicht verloren; sie stehen nur nicht mehr in der App.

### Hinweise fürs Einspielen (Haupt-Chat)
- Je Thema `einheit_abgleichen(…, 'lassen')` wie bisher. Zu sperren sind die alten Fragetexte aus Liste 2 (ersetzt), aus Liste 3 (einzeln entfernt) und alle Aufgaben entfallener Karten, die nicht in Liste 1 stehen (Liste 4 zählt sie).
- Umgezogene Aufgaben haben im neuen Thema denselben Fragetext. Beim Abgleich je Thema erscheinen sie dort als neu und müssen im alten Thema gesperrt werden.
- Bei ganzen Karten (ggt, kgv, Potenzgesetze, parkett) ist der Schlüssel `l` gleich geblieben; nur das Thema wechselt.

### Was nicht geprüft werden konnte
- Die Darstellung in der App (neue Karten neunerregel, quersumme, parallelen, achsenspiegelung, Tabellen-Grafik in monte_carlo). Geprüft sind nur die Daten und das Prüfskript.
- Ob die umgezogenen Stufe-3-Aufgaben im neuen Flug alles Vorwissen vorfinden: Ich habe jede Übernahme nach Thema und Reihenfolge gewählt, aber nicht jede einzeln gegen die vorigen Karten gelesen.
- LehrplanPLUS Gymnasium Kl. 7: Die Seite selbst konnte ich nicht öffnen (keine Freigabe). Die Aussagen zu M7 1.1 stammen aus dem Auszug der Websuche. Kl. 5 und Kl. 6: Auszug bzw. Seite gelesen.
- Test-, Korrektur- und Sicherungsaufgaben der Zielkarten habe ich nicht umgestuft (wie in den früheren Runden).

### Tatsachen, Annahmen, Meinung
- **Tatsachen:** alle Zahlen, Listen, Prüfskript und Nachweis. Lehrplan: M5 nennt Teilbarkeitsregeln für 2, 3, 5 und 10 und die Schlussrechnung. M6 nennt den Hauptnenner (auch über die Primfaktorzerlegung), Potenzen mit natürlichen Exponenten, negative ganzzahlige Exponenten als Bruch, das Volumen, Prozent und Zins sowie das arithmetische Mittel. Median, Modalwert, Spannweite und Potenzgesetze nennt M6 nicht. M7 1.1 nennt Produkte von Potenzen und Potenzen von Potenzen, M7 den Median. Realschule M6 Lernbereich 6: direkte Proportionalität.
- **Annahmen:** Die Neunerregel und Quotienten von Potenzen sind vor Kl. 9 nicht im Gymnasium-Lehrplan. Lesarten bei Zinsen, Zylinder und Logarithmus (Stoff bleibt im eigenen Flug); „Schrägbild der Pyramide“ meint die Seitenkanten-Rechnungen.
- **Meinung:** die Auswahl der „besten“ Aufgaben beim Zusammenlegen und die Texte der neuen Aufgaben.

Quellen: LehrplanPLUS Gymnasium Mathematik 5 (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/5/mathematik), 6 (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/6/mathematik), 7 (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik, nur Suchauszug); Realschule Mathematik 6 (https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/6/mathematik).
