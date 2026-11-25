# Sucher B: Internationale adaptive und diagnostische Mathe-Systeme

Abrufdatum aller Quellen: 25.11.2026. Nur Websuche und Seitenabruf; nichts angemeldet, nichts gekauft.
Kennzeichnung: **[G]** gesichert (Quelle genannt), **[A]** Annahme, **[M]** Meinung/Einschätzung von mir.
Preise sind in Landeswährung, ohne Steuer, soweit nicht anders genannt. Viele Preisangaben stammen aus Drittseiten (Vergleichsportale) und sind als solche markiert.

## Gesamtbild in fünf Sätzen
- [G] Die stärksten dokumentierten Mechaniken sind: Wissensgraph mit Voraussetzungen (Math Academy, ALEKS, Squirrel AI), Fehlvorstellungen als Distraktoren (Eedi), Schritt-für-Schritt-Prüfung des Rechenwegs (Mathspace, Graspable Math, Carnegie MATHia), Mastery-Schwellen (ASSISTments, Khan, IXL).
- [G] Die belastbarsten unabhängigen Wirkungsbelege betreffen ASSISTments (RCT, WWC ohne Vorbehalt) und Carnegie Cognitive Tutor (RAND-RCT, gemischt). Für Math Academy habe ich keine unabhängige Studie gefunden.
- [G] Kein gefundenes System ist ausdrücklich am bayerischen LehrplanPLUS ausgerichtet; ich habe dazu aber nicht gezielt gesucht, nur bei den einzelnen Systemen auf Hinweise geachtet.
- [G] Für eigene „Fehlbilder“ gibt es offene Daten (Eedi-Datensätze, MIME), aber die Lizenzen sind teils restriktiv (siehe Abschnitt c).
- [M] Die Familie sollte die Mechaniken übernehmen, nicht ein System als Ersatz: kein gefundenes System deckt Papier-Prüfung, deutsche Sprache und bayerischen Lehrplan zugleich ab.

---

## 1. Einzelne Systeme

### Math Academy (mathacademy.com)
1. **Kernmechanik [G]** Wissensgraph mit Voraussetzungen und übergeordneten Themen; Eingangsdiagnose nutzt den Graphen, um mit wenigen Fragen ein Wissensprofil zu schätzen (https://mathacademy.com/how-our-ai-works). Wiederholung über „Fractional Implicit Repetition (FIRe)“: Eine Wiederholung eines schweren Themas gibt Teilgutschrift an enthaltene leichtere Themen, sodass fällige Wiederholungen „mitabgehakt“ werden und weniger Reviews nötig sind (https://justinmath.com/individualized-spaced-repetition-in-hierarchical-knowledge-structures/). Mastery-Learning, Interleaving, gemischte Wiederholung, häufige Mini-Quizze mit Wiederholungsmöglichkeit (https://mathacademy.com/how-it-works). Rechenweg: nach meiner Sicht der Seiten keine Handschriftprüfung; Eingabe ist Antwort-basiert [A, nicht im Detail geprüft].
2. **Übernehmbar [M, abgeleitet aus G]** (a) Regel „Wiederholung auf höherem Thema gutschreiben auf Voraussetzungen“: Bei Bruchgleichung korrekt gelöst, bekommen Bruchrechnen, Vorzeichen und Äquivalenzumformung anteilig Wiederholungsgutschrift. (b) Wiederholungen so wählen, dass eine Aufgabe mehrere fällige Themen abdeckt. (c) Eingangsdiagnose entlang des Graphen: Bei Fehler zuerst Voraussetzungen testen, nicht Aufgabentyp wiederholen.
3. **Belege [G/Lücke]** Eigene Erfolgsgeschichten des Anbieters (https://www.justinmath.com/essays/). Eine unabhängige, kontrollierte Studie habe ich nicht gefunden (Suche „Math Academy independent study efficacy“ lieferte nur andere Produkte). Das Buch ist Selbstdarstellung des Herstellers [G, Autorenangabe im PDF].
4. **Zugang** Preis laut Startseite 49 USD pro Monat und Schüler, 30 Tage Geld-zurück (www.mathacademy.com, abgerufen 25.11.2026). Ältere Suchtreffer sprechen von „Beta-Preis 49, regulär 79-99 USD“; Preis daher [unsicher], Preisseite ließ sich nicht abrufen (Fehler). Kein kostenloser Test gefunden, nur Rückerstattung. Sprache Englisch; Kurse 4. bis 8. Klasse, Algebra I, Geometrie usw. (US-Gliederung); weder IB noch deutscher Lehrplan.
5. **Daten/Technik [G]** Buch „The Math Academy Way“ (Arbeitsfassung, Stand 27.04.2025) frei lesbar: https://www.justinmath.com/files/the-math-academy-way.pdf, Urheberrecht Math Academy LLC, keine offene Lizenz. Kein Quellcode, keine API gefunden. Nacherzählung/Kapitelzusammenfassung unabhängig: https://frankhecker.com/2025/02/14/math-academy-part-7/.
6. **Urteil** Davon lernen (Algorithmen); als Produkt ausprobieren wegen Rückerstattung.

### Eedi / Diagnostic Questions (eedi.com)
1. **Kernmechanik [G]** Multiple-Choice-Diagnosefragen mit vier Antworten, bei denen jede falsche Antwort eine bestimmte Fehlvorstellung verkörpert (https://eedi.com/projects/neurips-education-challenge). Eedi hat nach eigener Angabe 12.000 Fragen mit Konstrukt getaggt und 36.000 Distraktoren Fehlvorstellungen zugeordnet, über 4 Mio. Antworten ausgewertet (https://eedi.substack.com/p/what-do-4-million-students-responses). Danach gezielte Aufarbeitung; LLM-Tutor mit menschlicher Aufsicht in Erprobung.
2. **Übernehmbar [M]** Das „Fehlbild“-Prinzip direkt: Zu jeder Aufgabe 3 falsche Antworten bauen, die je einen benannten Denkfehler zeigen (z. B. 5/7 + 2/7 = 7/14). Wählt das Kind eine, wird nicht „falsch“ gemeldet, sondern der Denkfehler benannt und eine kurze Gegenaufgabe gestellt. Zusatz aus der Eedi-Forschung [G]: auch richtige Antwort kann falsche Begründung haben (siehe „Correct Answer Trap“, https://arxiv.org/pdf/2606.23205): Kinder gelegentlich kurz begründen lassen.
3. **Belege [G]** Google/Eedi-RCT (LearnLM): Erstversuch N=165, 5 britische Schulen, beaufsichtigter KI-Tutor mindestens so gut wie menschlicher Tutor, Transferaufgaben 5,5 Prozentpunkte besser als mit menschlichem Tutor allein (https://arxiv.org/abs/2512.23633v1). Erweiterter RCT N=1.179, 10 Wochen, 10 Schulen: Nach Tutoring jeder Art lösten Schüler ähnliche Folgeaufgaben zu 56-58 % richtig vs. 43 % nach Standard-Aufarbeitung; beim standardisierten Test Star Maths waren die Ergebnisse „flach“ (https://www.the74million.org/article/five-things-you-should-know-about-new-ai-tutor-study/ und https://services.google.com/fh/files/misc/learnlm_oct26.pdf). Beide Studien mit Beteiligung des Herstellers, also nicht unabhängig [G]. Grenze: kurzfristiger Nahtransfer, kein Effekt im Standardtest.
4. **Zugang** Preis für Privatfamilien: nicht gefunden. Eedi ist auf Schulen/Lehrkräfte ausgerichtet [A]. Sprache Englisch; britischer Lehrplan (Primary bis KS4).
5. **Daten [G]** NeurIPS-2020-Datensatz: 27.613 Fragen, 118.971 Schüler, 15.867.850 Antworten (Aufgaben 1 und 2); Lizenz CC BY-NC-ND 4.0 (https://eedi.com/projects/neurips-education-challenge). Laut Seite keine Fehlvorstellungs-Tags erwähnt. Kaggle „Eedi - Mining Misconceptions in Mathematics“ (2024, Preisgeld 55.000 USD): Distraktor-zu-Fehlvorstellung-Zuordnung; Details in Abschnitt c. Eedi nennt „sieben Sets von Fehlvorstellungsdaten“ unter https://www.eedi.com/data-and-competitions (diese Seite habe ich nicht abgerufen).
6. **Urteil** Davon lernen (wichtigstes Vorbild für Bausteine 1 und 3); Daten nutzen mit Lizenzprüfung.

### Khan Academy und Khanmigo
1. **Kernmechanik [G]** Mastery-Lernen mit Fähigkeitsstufen, Übungsaufgaben, Videos. Khanmigo ist ein KI-Tutor, der laut Anbieter nicht die Lösung nennt, sondern Denken anleitet (https://www.khanmigo.ai/parents). Wissensgraph/Wiederholungsplanung im Detail nicht geprüft.
2. **Übernehmbar [M]** „Tutor gibt nie die Lösung, nur die nächste Frage“-Regel (passt zu Bastani, siehe d). Mastery-Stufen mit Rückfall bei Fehlern.
3. **Belege [G]** Herstellerberichte: 30+ Minuten pro Woche verbunden mit ca. 20 % höherem als erwartetem Lernzuwachs (MAP Growth, ca. 350.000 Schüler, Effektstärke 0,36, korrelativ; https://2023-2024.annualreport.khanacademy.org/efficacy-results). Peer-reviewte PNAS-Studie mit statistischer Kontrolle, durchschnittliche Nutzung nur 10-15 Min/Woche (https://blog.khanacademy.org/national-study-in-top-journal-finds-khan-academy-learning-gains-after-accounting-for-key-unmeasured-factors/). RCTs in Brasilien und Deutschland/Schweiz-Kontext vom Hersteller zitiert (https://blog.khanacademy.org/multiple-studies-show-khan-academy-drives-learning-gains-evidence-for-our-platforms-effectiveness). Grenze: Nutzung ohne Betreuung oft gering; meist Beobachtungsstudien.
4. **Zugang [G]** Khan Academy kostenlos. Khanmigo für Familien 4 USD/Monat oder 44 USD/Jahr (https://www.khanmigo.ai/parents). Laut einer Drittseite nur für US-Lernende (https://www.edisonos.com/alternatives/khan-academy-pricing, Stand 25.06.2026) [unsicher, nicht verifiziert]. Deutsche Sprache/bayerischer Lehrplan: nicht geprüft.
5. **Daten** Kein offener Datensatz oder Quellcode gefunden (nicht gezielt gesucht).
6. **Urteil** Direkt nutzen (kostenlos testen), Khanmigo prüfen ob vom Ausland aus nutzbar.

### ALEKS (McGraw Hill)
1. **Kernmechanik [G]** Knowledge Space Theory (Doignon/Falmagne): Menge zulässiger „Wissenszustände“ mit Voraussetzungen; adaptive Eingangsprüfung mit meist 20-30 Fragen; Anzeige als „Kuchen“; Lernmodus bietet nur Themen, für die das Kind „bereit“ ist (https://www.mheducation.co.in/aleks-in). Freie Antwortformate statt Multiple Choice. Wiederholung/Vergessen als Modell untersucht (https://jmatayoshi.github.io/publications/EDM2018_forgetting.pdf).
2. **Übernehmbar [M]** „Bereit-Themen“-Regel: nur Themen anbieten, deren Voraussetzungen alle sitzen. Periodische Neu-Diagnose von 20-30 Fragen als Kontrolle statt nur Fortschrittszähler.
3. **Belege [G]** Reliabilität/Validität der Diagnostik in großen Datenanalysen (über 700.000 Assessments, https://link.springer.com/doi/10.1007/s40593-019-00176-0). Kausale Lernwirkung: unabhängige RCT nicht gefunden. Grenze [G]: überwiegend an US-Lehrplänen kalibriert (Drittseite, https://deepaksood619.github.io/education/competitors/aleks-analysis; nur Sekundärquelle).
4. **Zugang [G]** Familienpreise laut McGraw-Hill-Seite: 12 Monate 1 Kind 179,95 USD, 2 Kinder 305,90 USD; 6 Monate 1 Kind 99,95 USD (https://www.mheducation.com/prek-12/program/microsites/aleks-consumer/choose-subscription.html, Angabe ohne Datum). Testzugang nicht geprüft. Englisch, US-Lehrplan.
5. **Daten** Theorie offen publiziert (Buch/Preprint: https://arxiv.org/pdf/1511.06757); kein offener Quellcode/Datensatz gefunden.
6. **Urteil** Davon lernen (Wissenszustände, Diagnose); als Produkt nur bei US-Lehrplan sinnvoll.

### ASSISTments
1. **Kernmechanik [G]** Lehrkraft vergibt Hausaufgaben, Schüler bekommen sofort Rückmeldung, Hinweise und Tutoring-Schritte; „Skill Builder“ ist Mastery-Set, bei dem ein Fertigkeitsziel meist nach 3 richtigen Antworten in Folge erreicht ist (https://ieee-dataport.org/taxonomy/term/8775). Voraussetzungsstruktur wurde datenbasiert verfeinert (https://ies.ed.gov/use-work/awards/efficacy-study-online-mathematics-homework-support-evaluation-assistments-formative-assessment-and).
2. **Übernehmbar [M]** Einfachste „sitzt“-Regel: 3 richtige in Folge, gestaffelt über mehrere Tage (der Drei-in-Folge-Wert ist nur eine Konvention, kein Beweis für Haltbarkeit [A]). Lehrkraft/Elternteil sieht vor dem nächsten Tag, welche Aufgaben die meisten falsch hatten.
3. **Belege [G]** RCT mit 2.850 Siebtklässlern: signifikanter Zuwachs im Jahrestest, größer bei leistungsschwächeren Schülern (Roschelle u. a. 2016, https://doaj.org/article/dc037532ddfe4002a568a5f14411e4f1; IES: https://ies.ed.gov/use-work/awards/efficacy-study-online-mathematics-homework-support-evaluation-assistments-formative-assessment-and). WWC: erfüllt Standards ohne Vorbehalt (https://ies.ed.gov/ncee/wwc/Study/86375). Aggregation 50 RCTs zu Rückmeldungsformen (https://par.nsf.gov//servlets/purl/10350691).
4. **Zugang** Kostenlos für Lehrkräfte [A, nicht geprüft]; Privatfamilie ohne Klasse: nicht geprüft. Englisch, US-Lehrplan.
5. **Daten [G]** Öffentliche Datensätze: 2009-10 (Skill Builder; ca. 4.200 Schüler, 123 Fertigkeiten, 525.000+ Antworten laut https://arxiv.org/pdf/2208.12651), 2012-13 (ca. 6,1 Mio. Interaktionen, 46.674 Schüler), 2014-15; Download-Seite https://sites.google.com/site/assistmentsdata. Lizenz auf der Seite nicht gefunden [unsicher]; Replikationsdaten der RCT bei OpenICPSR (Projekt 183645). E-TRIALS-Werkzeug für Experimente (https://export.arxiv.org/pdf/2502.10545).
6. **Urteil** Davon lernen (Wirkung von sofortiger Rückmeldung); Daten für Wissensverfolgung nutzbar.

### Carnegie Learning MATHia / Cognitive Tutor
1. **Kernmechanik [G]** Intelligentes Tutorsystem: modelliert Fertigkeiten, gibt Hinweise und Fehlerrückmeldung innerhalb jedes Lösungsschritts, schreitet nach Mastery fort (https://pdf.arxiv.org/pdf/1802.08616 beschreibt Mastery in der Praxis).
2. **Übernehmbar [M]** Schrittweise Aufgaben, bei denen bekannte Fehlerwege eine eigene Rückmeldung auslösen (Fehlbild an Zwischenschritt statt nur am Endergebnis).
3. **Belege [G]** RAND-RCT mit 147 Schulen: Jahr 1 ohne signifikanten Effekt, Jahr 2 laut Bericht etwa +8 Perzentilpunkte (https://edweek.org/education/study-hybrid-algebra-program-nearly-doubled-math-learning/2013/06); kritische Einordnung der Schlagzeile „verdoppelt“ (https://www.edweek.org/education/opinion-the-headlines-versus-the-study-in-blended-algebra-program/2013/08); WWC-Tabelle zeigt für Teilergebnisse keine Signifikanz (https://ies.ed.gov/ncee/WWC/Study/82101). Fazit: gemischt, stark von Umsetzung abhängig.
4. **Zugang** Nur Schulen/Distrikte [A, nicht geprüft]. Englisch.
5. **Daten [G]** PSLC DataShop/KDD-Cup-Datensätze aus Carnegie Learning (http://pslcdatashop.web.cmu.edu/KDDCup/downloads.jsp, via Eedi-Paper zitiert); Lizenz nicht geprüft.
6. **Urteil** Davon lernen (Schrittrückmeldung); nicht direkt nutzbar.

### Mathspace
1. **Kernmechanik [G]** Schüler schreiben jeden Lösungsschritt (Tastatur oder Handschrift), das System prüft Zeile für Zeile und gibt Hinweise, Musterbeispiel (https://apps.apple.com/app/id1445097311; https://content.govdelivery.com/attachments/VAEDUFCPS/2023/06/05/file_attachments/2516566/FCPS%20Student%20Guide%202023.pdf). Adaptive Auswahl nach Fertigkeit.
2. **Übernehmbar [M]** Rechenweg als Zeilenfolge prüfen: jede Zeile muss äquivalent zur vorherigen sein (Äquivalenzprüfung per CAS), Fehler dort markieren, wo die erste ungültige Umformung steht. So braucht nicht jede Rechnung getippt werden, sondern nur Zwischenzeilen an Prüfpunkten [A, eigene Ableitung].
3. **Belege [G/Einschränkung]** Herstellerzitierte „unabhängige“ Studie mit 94.000 Schülern: mehr Nutzung, höhere Wahrscheinlichkeit der Proficiency (korrelativ, https://mathspace.co/us/educators). Common Sense Media: Risiko, dass Schüler von der Schritt-Rückmeldung abhängig werden (https://commonsense.org/education/reviews/mathspace).
4. **Zugang [G]** Schulen ab ca. 5 GBP pro Schüler/Jahr; kostenlose „Personal“-Konten für Einzelne und Eltern, ohne Aufgabenverteilung (https://edtechimpact.com/products/mathspace). Englisch; Australien, USA, UK, IB-nahe Inhalte „World of Maths“ laut App-Text [nicht verifiziert].
5. **Daten** Keine offene API/Daten gefunden.
6. **Urteil** Ausprobieren (kostenloses Konto); Mechanik direkt übertragbar auf Baustein 2.

### Graspable Math
1. **Kernmechanik [G]** Algebra-Terme als anfassbare Objekte: Ziehen und Umformen auf dem Bildschirm; unzulässige Umformungen werden sofort abgewiesen („Term springt zurück“); jede Umformung wird protokolliert und der Lehrkraft gezeigt (https://sites.google.com/view/gmactivities/about-gm).
2. **Übernehmbar [M]** Zulässigkeitsprüfung pro Schritt als Grundregel-Engine: Vorzeichenregel, Klammerregel als prüfbare Umformungsregeln, Zählung je Regel („Vorzeichenregel 14 von 15 korrekt“).
3. **Belege** Von IES-SBIR gefördert, Forschung mit WPI; unabhängige Wirkungsstudie nicht gefunden.
4. **Zugang** Werkzeug laut Presse kostenlos (Stand 2017; https://thejournal.com/articles/2017/08/31/iu-researchers-develop-interactive-tool-to-let-students-play-with-math.aspx); aktuelle Preise nicht geprüft. Englisch.
5. **Daten** Quellcode: nicht gefunden.
6. **Urteil** Davon lernen; ausprobieren für Klasse 8 (Gleichungen).

### Sparx Maths
1. **Kernmechanik [G]** Wöchentliche personalisierte Hausaufgaben, Videos, „Bookwork-Checks“ (Lösung vor Weitergehen eintippen), Wiederholung früherer Themen; ca. 38.000 Aufgaben und 9.000 Videos (https://www.educ.cam.ac.uk/research/programmes/sparx/SparxTechnicalReport.pdf).
2. **Übernehmbar [M]** Bookwork-Check: Kind muss vor der Aufgabe erst die Musterlösung abschreiben/reproduzieren; wöchentlicher Paket-Rhythmus mit festem Wiederholungsanteil.
3. **Belege [G]** RAND Europe/Cambridge, unabhängig, aber korrelativ: 1 Stunde/Woche über ein Jahr verbunden mit rund 0,24 GCSE-Stufen mehr (https://support.sparxmaths.com/en/articles/342375-introducing-sparx-maths; https://www.rand.org/randeurope/research/projects/2021/analysing-the-relationship-between-sparx-maths-and-maths-outcome.html). Kein RCT; Studie war vom Anbieter beauftragt (laut Studienseite „independent evaluation“, Auftraggeber nicht geprüft).
4. **Zugang [G]** Nur über Schule; Schulpreis ab 600 GBP/Jahr (https://edtechimpact.com/products/sparx-maths-homework/). Privatfamilie: nicht möglich laut „School must create the account“. KS3/GCSE (UK).
5. **Daten** Technischer Bericht frei (Link oben); sonst nichts offen.
6. **Urteil** Davon lernen; nicht nutzbar.

### Dr Frost Maths
1. **Kernmechanik [G]** Selbstkorrigierende Aufgaben, Frageschmieden, Videos, Mock-Prüfungen, adaptive Aufgabenzuteilung optional (https://drfrost.org/faqs.php, https://d1ginotxhthqkd.cloudfront.net/products/drfrostmaths).
2. **Übernehmbar [M]** Mock-Prüfungen nach Originalformat und „Shadow Papers“ als Vorbild für den Prüfungsmodus (Zeit, ohne Hilfe).
3. **Belege** Keine unabhängige Wirkungsstudie gefunden.
4. **Zugang [G]** Schülerkonten für unabhängige Lernende kostenlos laut https://www.drfrost.org/students; Schulpreis 650 GBP + MwSt. (https://support.drfrost.org/hc/en-gb/articles/4546170606239). Englisch, UK-Lehrplan.
5. **Daten** Nichts offen gefunden.
6. **Urteil** Ausprobieren für Aufgabenmaterial, falls Niveau passt; sonst davon lernen.

### IXL
1. **Kernmechanik [G]** Fertigkeitenkatalog (19.000+ Fertigkeiten), „Real-Time Diagnostic“ ordnet das Kind auf einer Skala ein und erzeugt Plan (https://www.ixl.com/materials/us/press/Press_Release__LevelUp_Relaunch.pdf). Wiederholungsplanung nicht geprüft.
2. **Übernehmbar [M]** 10 Minuten pro Woche Mini-Diagnose als Dauerprüfung, die den Plan laufend aktualisiert.
3. **Belege [G]** Herstellerzitiert: ESSA-Tier-2-Studie (4.000 Schüler, NWEA MAP, https://www.ixl.com/materials/us/research/ESSA_Research_Report.pdf); RCT Johns Hopkins (Copeland u. a. 2023, über Hersteller zitiert); Heimstudie 5.000+ Kinder, Herstellerdaten (https://www.ixl.com/materials/us/research/The_Impact_of_IXL_on_At-Home_Math_and_ELA_Learning.pdf). Grenze: viele Studien vom Hersteller oder mit Hersteller-Daten; Übungs-Charakter, wenig Erklärung [M].
4. **Zugang [G]** Drittquelle (Stand Juni 2026): 9,95 USD/Monat oder 79 USD/Jahr für ein Fach, 15,95/129 für Mathe + Englisch; weiteres Kind 4 USD/Monat oder 40 USD/Jahr (https://www.thepricer.org/how-much-does-ixl-cost/). Preisseite des Anbieters nicht abgerufen. US-Lehrplan, Englisch.
5. **Daten** Keine.
6. **Urteil** Davon lernen (Diagnose); nicht nötig.

### DeltaMath
Nur kurze Hinweise: Teilweise kostenlos, es existiert eine kostenpflichtige Variante „DeltaMath Plus“ (Forenhinweis in einer Sammelseite, nicht verlässlich). Mechanik, Studien, Daten: **nicht gefunden/nicht geprüft**. Urteil: nicht relevant [M], mangels Belegen.

### Art of Problem Solving: Alcumus und Beast Academy
1. **Kernmechanik [G]** Alcumus: kostenloses adaptives System, über 13.000 Aufgaben mit Lösungen; Aufgaben passen sich der Leistung an; ein bestandenes Thema kann nach Fehlern in Wiederholungsaufgaben wieder „unbestanden“ werden (https://eschoolnews.com/?p=196909; https://freedom251.com/apps/alcumus/, Drittseite). Beast Academy: Comic-Lehrgang für 6-13 Jahre, Online plus Bücher.
2. **Übernehmbar [M]** Rückfall-Regel: Ein Thema gilt nur als „sitzt“, solange Wiederholungsaufgaben richtig bleiben.
3. **Belege** Unabhängige Wirkungsstudie nicht gefunden.
4. **Zugang [G]** Alcumus kostenlos mit kostenlosem Konto (https://artofproblemsolving.com/alcumus). Beast Academy Online 16 USD/Monat oder 100 USD/Jahr, Geschwisterrabatt (https://help.beastacademy.com/a/1792549-ways-to-save-on-subscriptions-and-books; https://www.cuemath.com/blog/cuemath-vs-beast-academy/, geprüft laut Seite am 05.11.2026). Englisch, kein bayerischer Lehrplan.
5. **Daten** Keine offenen Daten gefunden.
6. **Urteil** Alcumus: ausprobieren für starke Kinder (Klasse 8 Enrichment, kostenlos); Beast Academy nicht nötig für Klasse 5 (Preis, Lehrplan [M]).

### Synthesis Tutor
1. **Kernmechanik [G]** Sprachgeführter KI-Tutor für 5-11 Jahre, passt Schwierigkeit an Beherrschung an (https://homeschoolfox.com/curriculum/synthesis-tutor, Drittbeschreibung).
2. **Übernehmbar** Wenig; Altersgruppe unter der Zielgruppe der Familie (Klasse 5 und 8).
3. **Belege** Nur Herstellerdaten bzw. Elternberichte; kritische Nutzerbewertungen (Trustpilot) [G, https://nl-be.trustpilot.com/review/www.synthesis.is]. Unabhängige Studie nicht gefunden.
4. **Zugang** Preise widersprüchlich: 45 USD/Monat oder 300 USD/Jahr, Familienplan bis 7 Kinder 119 USD/Jahr (homeschoolfox) gegenüber 35 USD/Monat und 299 USD/Jahr in anderen Quellen. [unsicher] 7-Tage-Test ohne Karte laut Drittquelle. Englisch.
5. **Daten** Keine.
6. **Urteil** Nicht relevant für diese Altersgruppe [M].

### Photomath, Duolingo Math, DragonBox Algebra, Brilliant
Für diese vier habe ich keine belastbaren Quellen zu Mechanik, Wirkung, Preis und Daten gefunden oder abgerufen. Aus dem Suchtreffer nur: Photomath wird in einer Drittseite als „von Google übernommen, Schritt-für-Schritt-Lösungen, 9,99 USD/Monat“ beschrieben (https://devtoollab.com/ai-tools/synthesis, unzuverlässig). **Nicht geprüft.** [M] Lösungsanzeiger widersprechen dem Ziel „Prüfung ohne Hilfe“; Brilliant/DragonBox/Duolingo sind Einstiegs- bzw. Spielformate. Urteil: nicht relevant (vorläufig, ungeprüft).

### Desmos Classroom (Amplify) und Mathigon/Polypad
1. **Kernmechanik [G]** Desmos Classroom heißt jetzt Amplify Classroom: kostenlose Aktivitäten, Lehrer sieht Schülerantworten live; Polypad: virtuelle Manipulative, kostenlos nutzbar (https://polypad.amplify.com/faqs). Adaptive Diagnose nicht vorhanden [A].
2. **Übernehmbar [M]** Polypad-Algebrakacheln, Brüche, Zahlenstrahl als Veranschaulichung in Erklärungen.
3. **Belege** Nicht geprüft.
4. **Zugang [G]** Polypad kostenlos; Konten für unter 13-Jährige nicht mehr möglich, Lehrkräfte teilen Klassencodes (siehe FAQ). Desmos-Rechner kostenlos für Einzelpersonen (https://amplify.com/topics/technology-in-the-math-classroom/). Mathigon-Inhalte in mehr als 20 Sprachen laut Pressemitteilung (https://uk.mathigon.org/press), ob Deutsch ist nicht geprüft.
5. **Daten** Quellcode/Lizenz Polypad: nicht gefunden.
6. **Urteil** Nutzen als Zeichen-/Veranschaulichungswerkzeug; nicht als Lernsystem.

### Century Tech
1. **Mechanik [G, dünn]** Adaptive UK-Plattform mit Eltern-Dashboard (https://edtechimpact.com/products/century-tech-app/). Details nicht geprüft.
2.-3. Belege: Hersteller-Selbstaussagen; unabhängige Studien nicht gefunden.
4. **Zugang [G]** Schulpreis ab 1.200 GBP/Jahr (edtechimpact), Sekundar ab 1.275 GBP (https://www.century.tech/?p=17893). Privatfamilie nicht geprüft. UK-Lehrplan.
6. **Urteil** Nicht relevant.

### Squirrel AI
1. **Kernmechanik [G, Sekundärquellen]** Extrem feine Wissenspunkte (Mittelstufen-Mathe über 10.000 bis 30.000 Punkte, je nach Quelle), Wissensgraph mit Voraussetzungen, Diagnose am Anfang, System bestimmt Reihenfolge (https://en.wikipedia.org/wiki/Squirrel_AI; https://www.technologyreview.com/2019/08/02/131198/china-squirrel-has-started-a-grand-experiment-in-ai-education-it-could-reshape-how-the/amp/).
2. **Übernehmbar [M]** Feine Zerlegung: Statt Thema „Gleichungen“ Teilfertigkeiten (Term addieren, auf beide Seiten anwenden, Vorzeichenwechsel beim Umstellen), je mit eigenem Stand.
3. **Belege** Nur Herstellerzahlen (z. B. 5,4 vs. 0,7 Punkte Zuwachs in „Mensch-Maschine-Duell“, https://compasslist.com/insights/squirrel-ai-edtechs-ai-based-personalized-tutoring-eases-load-for-students-and-teachers); unabhängig nicht belegt. MIT Technology Review nennt Expertenbedenken.
4. **Zugang** Nicht für Privatfamilien in Europa gefunden. Chinesisch/Englisch.
5. **Daten** Patent erwähnt (US 12,260,638 B1), sonst nichts offen.
6. **Urteil** Davon lernen (Granularität); sonst nicht relevant.

### Area9 (Rhapsode/Lyceum)
Nicht gefunden: Meine Suche lieferte keine verwertbaren Seiten zu Area9. **Nicht geprüft.** [A] Bekannt ist aus allgemeinem Wissen, nicht aus dieser Recherche, dass Area9 mit Vertrauens-Selbsteinschätzung arbeitet; ohne Beleg nicht verwenden.

### Pamoja (IB online)
1. **Mechanik [G]** Keine adaptive Software, sondern lehrerbegleitete Online-Kurse für IB-Diploma-Fächer, auch Mathematik AA und AI, SL/HL, 12 Einheiten, 144 Lektionen, zwei Jahre (https://pamojaeducation.com/course/pt-mathematics-applications-interpretations-sl/). Empfohlen 7-10 Std. pro Woche beim HL.
4. **Zugang [G]** Verträge nur mit IB-Schulen, nicht mit Eltern (https://www.PamojaEducation.com/wp-content/uploads/2023/03/Pamoja-Admissions-23-24-Academic-Year.pdf). Kursgebühren laut einer Schulseite ca. 1.390-1.460 USD (https://sites.google.com/eerdeibs.nl/eerde-ibs-student-site/learning-lessons/supplementary-lesson-payment, älter, Jahr unklar). Nur DP (Klasse 11/12), also für die Kinder nicht jetzt relevant. MYP: nicht gefunden.
6. **Urteil** Nicht relevant für Klasse 5 und 8.

---

## (a) Die zehn wichtigsten übertragbaren Ideen

| # | Idee | Von wem | Umsetzung | Beleg |
|---|---|---|---|---|
| 1 | Falsche Antworten als benannte Fehlvorstellungen bauen („Fehlbild“) | Eedi | Je Aufgabe 3 Distraktoren, jeder = ein Denkfehler mit Kurznamen; bei Wahl sofort Denkfehler benennen plus Gegenaufgabe | Eedi-Seite (NeurIPS) [G]; RCT-Effekte bei Aufarbeitung, aber nur Nahtransfer [G] |
| 2 | Auch richtige Antworten kurz begründen lassen | Eedi-Forschung | Bei 1 von 4 Aufgaben Satz „Warum?“ per Auswahlsätze; falsche Begründung = verstecktes Fehlbild | arXiv 2606.23205 (nur Preprint) [G] |
| 3 | Wiederholung auf Voraussetzungen gutschreiben | Math Academy (FIRe) | Gelöste schwere Aufgabe erhöht anteilig den Stand der Voraussetzungen und verschiebt deren Fälligkeit | justinmath.com [G, Herstellerbeschreibung]; Wirkung unabhängig nicht belegt |
| 4 | Diagnose entlang des Graphen: nur Voraussetzungen testen, die fehlen könnten | Math Academy, ALEKS | Bei Fehler gehe 1-2 Ebenen im Graph zurück, nicht den ganzen Themenbereich | mathacademy.com/how-our-ai-works; ALEKS-Artikel (Springer) [G] |
| 5 | Nur „bereite“ Themen anbieten | ALEKS | Thema freischalten, wenn alle Voraussetzungen auf „sitzt“ | mheducation.co.in/aleks-in [G] |
| 6 | Rechenweg Zeile für Zeile auf Äquivalenz prüfen | Mathspace, Graspable | Jede Zeile CAS-prüfen; erste ungültige Umformung markieren | Mathspace-Dokumente [G]; Abhängigkeit von der Rückmeldung als Risiko (Common Sense) |
| 7 | Regeln als prüfbare Umformungen mit Zähler je Regel | Graspable Math | Regel-Tags (Vorzeichen, Klammer, Bruch) an jeder Zeile; Stand je Regel | about-gm-Seite [G]; eigene Ableitung [M] |
| 8 | Tutor gibt keine Lösung, nur Rückfragen; Hilfe-Nutzung wird mitgezählt | Khanmigo, Bastani GPT Tutor | Hinweisstufen (1: Frage, 2: Teilschritt), nie Endergebnis; Aufgabe mit Hinweis zählt nicht als „sitzt“ | PNAS 2025 [G] |
| 9 | „Sitzt“ = mehrfach richtig, ohne Hilfe, mit Abstand, und Rückfall möglich | ASSISTments, Alcumus | 3 richtig in Folge ohne Hinweis, an 3 verschiedenen Tagen; bei späterem Fehler zurück auf „wackelt“ | Skill-Builder-Beschreibung [G]; Abstandsregel [A] |
| 10 | Prüfungsmodus nach Originalformat und Mini-Diagnose als Dauerkontrolle | Dr Frost, IXL | Wöchentlich 10 Minuten Mixed-Diagnose; alle paar Wochen vollständige Schulaufgabe auf Papier, in Zeit | Dr-Frost-Seiten; IXL-Presse [G]; Papier-Teil ist [M] |

## (b) Welche zwei Systeme sofort ausprobieren
1. **Khan Academy plus Khanmigo**: Plattform kostenlos (https://www.khanmigo.ai/parents für Khanmigo: 4 USD/Monat, 44 USD/Jahr; Verfügbarkeit außerhalb USA nicht verifiziert). Zweck: Mastery-Ablauf und Tutor-Verhalten vergleichen.
2. **Math Academy**: 49 USD/Monat pro Kind laut Startseite (Preis unsicher), 30 Tage Geld-zurück: https://www.mathacademy.com/. Zweck: Wissensgraph, Diagnose und Wiederholungslogik im echten Ablauf sehen; beachte, dass 30 Tage mit zwei Kindern ca. 98 USD kosten [G, einfache Rechnung].
Ergänzend kostenlos: Alcumus (https://artofproblemsolving.com/alcumus) für Klasse 8; Mathspace-Personal-Konto für Schrittprüfung (https://mathspace.co).
[M] Alle sind Englisch; zum Bestehen bayerischer Schulaufgaben dienen sie nur als Mechanik-Vorbild.

## (c) Offene Datensätze und Kataloge von Fehlvorstellungen
| Quelle | Inhalt | Lizenz | Link | Hinweis |
|---|---|---|---|---|
| Eedi NeurIPS 2020 | 27.613 Fragen, 118.971 Schüler, 15,9 Mio. Antworten (Aufg. 1/2); 948 Fragen, 4.918 Schüler, 1,38 Mio. Antworten (Aufg. 3/4) | CC BY-NC-ND 4.0 [G] | https://eedi.com/projects/neurips-education-challenge | Nichtkommerziell, keine Bearbeitungen verbreiten; Fehlvorstellungs-Tags laut Seite nicht erwähnt. Als Analysegrundlage ok, nicht zum Weiterverbreiten umgearbeiteter Inhalte. |
| Eedi „Mining Misconceptions in Mathematics“ (Kaggle 2024) | 1.857 Fragen mit je vier Antworten, Distraktor-Fehlvorstellung-Zuordnung (Zahl laut MISTAKE-Paper, https://arxiv.org/pdf/2510.11502) | Lizenz **nicht verifiziert** (Kaggle-Wettbewerbsregeln prüfen) | https://www.kaggle.com/competitions/eedi-mining-misconceptions-in-mathematics | Beispiel eines Eintrags: „glaubt, die Spannweite ändert sich, wenn man zu allen Zahlen denselben Wert addiert“ [G, HF-Datensatz-Vorschau]. Beste Grundlage für Fehlbild-Katalog. |
| Eedi Misconceptions-Graph | Laut einem Preprint: 19.294 Konstrukt-Fehlvorstellung-Paare, 8.117 Fehlvorstellungs-IDs, „Version 1.0 unter CC BY 4.0“ (https://arxiv.org/pdf/2611.14557) | CC BY 4.0 laut Preprint, **Originalseite nicht geprüft** [unsicher] | über https://www.eedi.com/data-and-competitions (nicht abgerufen) | Wenn bestätigt, wäre dies die freieste Grundlage. Vor Nutzung Lizenz auf Eedi-Seite lesen. |
| MIME / „MAP - Charting Student Math Misunderstandings“ | über 52.000 Schülererklärungen zu 15 Aufgaben (Klasse 4-8), von Experten auf Fehlvorstellungen kodiert | Lizenz **nicht verifiziert**; „nach dem Wettbewerb öffentlich für Forschung und andere Nutzung geteilt“ (https://educationaldatamining.org/data-set-awards/) | https://www.kaggle.com/competitions/map-charting-student-math-misunderstandings; Beschreibung https://aclanthology.org/2025.aimecon-wip.3.pdf | EDM-Preis 2026. Englisch, nur 15 Aufgaben, aber echte Kinderbegründungen. |
| ASSISTments 2009-10, 2012-13, 2014-15 | Antwortprotokolle mit Fertigkeitsnamen | Lizenz **nicht gefunden** | https://sites.google.com/site/assistmentsdata | Gut für Wissensverfolgung, enthält keine benannten Fehlvorstellungen. Zitierpflicht laut Seite. |
| ASSISTments-RCT-Replikationsdaten | Randomisierung, Nutzung, Leistungsdaten | **nicht geprüft** | https://www.openicpsr.org/openicpsr/project/183645/version/V1/view | Für Studienanalyse, nicht für Fehlbilder. |

[M] Empfehlung: Eedi-Misconception-Katalog als Ideengeber; die eigene Fassung für den bayerischen Lehrplan selbst schreiben (Übersetzung und Lehrplanbezug fehlen in allen Quellen), statt fremde Texte zu übernehmen (wegen ND-Klausel).

## (d) Forschung zu KI-Tutoren und Lernerfolg ohne KI in der Prüfung

**Bastani u. a., PNAS 2025 (122(26), e2422633122), DOI 10.1073/pnas.2422633122 [G]**
- Quellen: https://econpapers.repec.org/RePEc:nas:journl:v:122:y:2025:p:e2422633122; Zusammenfassung https://www.psypost.org/unrestricted-generative-ai-harms-high-school-math-learning-by-acting-as-a-crutch/; https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education.
- Design: randomisiertes Feldexperiment, ein großes Gymnasium in der Türkei, Herbst 2023, ca. 1.000 Schüler in etwa 50 Klassen, Jahrgangsstufen 9-11; vier Sitzungen à 90 Minuten, Stoff etwa 15 % des Semesters. Drei Gruppen: Kontrolle (Buch und Notizen), „GPT Base“ (ChatGPT-ähnlich), „GPT Tutor“ (mit Schutzmechanismen, u. a. Hinweise statt Lösungen, Lehrer-Hinweise zu typischen Fehlern).
- Ergebnis in der Übungsphase mit KI: GPT Base +48 %, GPT Tutor +127 % gegenüber Kontrolle.
- Ergebnis in der anschließenden Prüfung ohne KI: GPT Base 17 % schlechter als Kontrolle; GPT Tutor statistisch nicht von der Kontrolle unterscheidbar. Autoren: Schutzmechanismen mildern den Schaden weitgehend, bringen aber keinen Lerngewinn.
- Grenzen [G]: nur Mathematik, eine Schule, kurze Dauer; die Wharton-Zusammenfassung sagt ausdrücklich, ein Teil der Schüler nutze KI als „Krücke“.
- Korrekte Wiedergabe: Die Studie zeigt nicht, dass KI-Tutoren generell schaden, sondern dass freier Zugang zu einem Chat-KI das Lernen ohne KI verschlechtern kann und dass ein gesperrter Hinweis-Tutor diesen Schaden verhindert, aber keine Verbesserung der Prüfungsleistung brachte.
- [M] Folgerung: Übungsleistung mit Hilfe ist kein Beleg für Können. Für die Familie: Fortschritt nur aus Aufgaben ohne Hilfe zählen.

**Weitere Studien [G]**
- Kestin u. a. (Harvard, Scientific Reports 2025): Physik-Einführungskurs, 194 Studierende, speziell gebauter KI-Tutor lieferte mehr als doppelt so viel Lernzuwachs in kürzerer Zeit wie Präsenz-Active-Learning (https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/; https://news.harvard.edu/gazette/story/2024/09/professor-tailored-ai-tutor-to-physics-course-engagement-doubled/). Grenzen: Studierende, Physik, ein Kurs, vom Dozenten selbst gebauter Tutor.
- Eedi/Google LearnLM (siehe oben): Tutoring jeder Art hilft bei Nachfolgeaufgaben, aber beim standardisierten Test (Star Maths) kein Effekt.
- Tutor CoPilot (Stanford): KI unterstützt menschliche Tutoren; ca. 20 USD pro Tutor und Jahr (https://arxiv.org/pdf/2410.03017v1); Wirkung auf Lernen der Schüler laut Studie positiv, Zahlen nicht im Einzelnen geprüft.

## Was ich nicht prüfen konnte
- Preisseite von Math Academy (Abruf fehlgeschlagen); Preis 49 USD aus der Startseite, widerspricht älteren Treffern.
- Einzelne Systeme ohne belastbare Quelle: DeltaMath, Photomath, Duolingo Math, DragonBox Algebra, Brilliant, Area9, Century (nur dünn).
- Lizenzen von ASSISTments-, Kaggle-Eedi- und MIME-Daten; Eedi-Seite „data-and-competitions“ nicht abgerufen; die CC-BY-4.0-Angabe zum Misconception-Graph stammt aus einem Preprint.
- Verfügbarkeit von Khanmigo außerhalb der USA, deutsche Sprache bei allen Systemen, Passung zum LehrplanPLUS und zu IB MYP.
- Unabhängige Wirkungsstudien zu Math Academy, Mathspace (kausal), Graspable Math, Dr Frost.
- Volltexte von Studien (Bastani PNAS-Text, Roschelle, Pane) nicht gelesen; Zahlen stammen aus Zusammenfassungen und Datenbankseiten. Exakte p-Werte nicht erfasst.
- Wirkungsangaben mehrerer Hersteller (Khan, IXL, Squirrel AI, Mathspace) sind Herstellerberichte oder korrelativ.
