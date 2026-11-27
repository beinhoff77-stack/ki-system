# Tiefen-Sucher 2: Quellen zu typischen Fehlern und Fehlvorstellungen, Mathe Klasse 5-10

Abrufdatum aller Quellen: 25.11.2026. Methode: nur Websuche und Seitenabruf (keine Anmeldung, nichts gekauft, keine Datensätze geladen, keine Formulare).
Kennzeichnung: **[G]** gesichert (auf der genannten Seite oder in einem Suchausschnitt gelesen, Link dabei), **[A]** Annahme, **[M]** Meinung/Einschätzung, **nicht gefunden / nicht geprüft** wo es so war. Keine Rechtsberatung, nur Wiedergabe von Lizenzangaben.
Wichtige Einschränkung der Abrufart: Die Seitenabrufe liefern teils nur eine Zusammenfassung durch ein Hilfsmodell, nicht den Volltext; wo ich nur einen Suchausschnitt sah, steht **[Ausschnitt]**. Zwei Seiten waren per robots.txt gesperrt (mathe-sicher-koennen.dzlm.de/themen, btmdx1.mat.uni-bayreuth.de/smart), eine ließ sich nicht laden (huggingface.co/datasets/Eedi/Misconception-Graph).

## Kurzfassung (die wichtigsten Befunde)
- [G] Eedi-Prinzip bestätigt: jede Frage hat eine richtige und drei falsche Antworten, jede falsche ist einer benannten Fehlvorstellung zugeordnet (https://arxiv.org/pdf/2512.23633). Umfang laut Eedi: 12.000 Fragen mit je einem Konstrukt, 36.000 Distraktoren mit Fehlvorstellung, über 4 Mio. Antworten (https://eedi.substack.com/p/what-do-4-million-students-responses).
- [G] Lizenzlage Eedi: NeurIPS-2020-Datensatz **CC BY-NC-ND 4.0** (an der Quelle gelesen). Kaggle-2024-Datensatz: **Lizenz nicht gefunden** (weder auf der Eedi-Seite noch auf der abrufbaren Kaggle-Seite; Regeln liegen hinter Anmeldung). Misconception-Graph: **CC BY 4.0 nur aus einem Preprint**, an der Originalseite nicht bestätigt.
- [G] Mathe sicher können: Diagnose- und Förderbausteine **CC BY-NC-SA 4.0** (im Dokumentkopf des Bausteins B1 gelesen); Online-Check nur über Schul-Zugang mit Auftragsverarbeitungsvertrag, für eine Privatfamilie praktisch nicht nutzbar.
- [G] Die zahlenmäßig belastbarste frei lesbare Fehlerstudie ist Booth u. a. 2014 (565 Schüler, US-Algebra I): Vorzeichenfehler mit Abstand am häufigsten; Variablenfehler früh im Jahr und Eigenschaftsfehler sagen schlechte Testleistung am besten voraus; Bruchfehler waren häufig, aber nicht vorhersagekräftig.
- [G] Das deutsche Standardwerk zu Bruchfehlern (Padberg) ist nur als Buch zugänglich; seine Fehlerliste steht in einem Hochschulskript (Link unten).
- [G] SMART Bayreuth ist nach allem, was ich sah, eine **Aufgabensammlung**, keine Fehleranalyse. Das diagnostische SMART (Stacey, Steinle u. a., Melbourne) ist ein anderes Projekt. Eine ISB-Fehleranalyse zu den Bayerischen Mathematik-Tests habe ich **nicht gefunden**; die ISB-Ergebnis-PDFs enthalten Erfolgsquoten je Teilaufgabe, keine Fehlerarten.
- [M] Katalog unten: 114 Einträge, jedes Zahlenbeispiel per Skript nachgerechnet (richtiges und falsches Ergebnis). Aber: Nur ein Teil der Einträge ist an einer gelesenen Quelle belegt; der Rest ist mit **Lit** markiert, das heißt: aus Fachwissen, in dieser Recherche nicht an einer Quelle geprüft.

---

## 1. Quellen im Einzelnen

### A) Eedi / Diagnostic Questions

**Aufbau einer Diagnose-Frage [G]** Mehrfachwahl mit einer richtigen und drei falschen Antworten; jede falsche Antwort ist einer bestimmten, häufigen Fehlvorstellung zugeordnet; aus der Wahl lässt sich der Denkfehler ohne weitere Erklärung erschließen (https://arxiv.org/pdf/2512.23633, Beschreibung des Eedi-Systems mit "über 60.000 Diagnosefragen"; ebenso https://news.microsoft.com/source/features/ai/eedi-online-math-quiz/).

**Taxonomie [G, teils Ausschnitt]**
- Ebenen laut Eedi-Beitrag: Konstrukt (feinkörniges Lernziel, z. B. Brüche mit gleichem Nenner ordnen) und darunter Fehlvorstellungen; Konstrukte sind unter Überschriften wie "Stellenwert" gruppiert; jede Frage trägt ein Konstrukt, jeder Distraktor eine Fehlvorstellung (https://eedi.substack.com/p/what-do-4-million-students-responses; Definition von Konstrukt/Fehlvorstellung auf https://www.eedi.com/data-and-competitions).
- Umfang: 12.000 Fragen getaggt, 36.000 Distraktoren zugeordnet, über 4 Mio. Antworten (Substack). Die Gesamtzahl der Fehlvorstellungen nennt der Beitrag nicht. Ein Preprint beschreibt die öffentliche Graph-Datei mit 19.294 Konstrukt-Fehlvorstellung-Paaren, 2.258 verknüpften Konstrukten und 8.117 Fehlvorstellungs-IDs (https://arxiv.org/pdf/2611.14557, **[Ausschnitt, Sekundär]**; Identität mit der Originaldatei vom Autor selbst als ungeprüft bezeichnet).
- Granularität: sehr fein (eine Fehlvorstellung gilt für ein Konstrukt; dieselbe Grundidee, z. B. "kleinere von größerer Zahl abziehen", taucht in vielen Konstrukten wieder auf, laut Substack).
- Beispiele für Bezeichnungen in eigenen Worten: kleinere von der größeren Zahl abziehen, egal an welcher Stelle; Minuszeichen als Plus lesen; beim Abziehen die Zehnerstelle nicht umbenennen; Quadrieren mit Verdoppeln verwechseln; x- und y-Wert vertauschen; die 1 für eine Primzahl halten; Spannweite ändere sich, wenn man zu allen Zahlen dasselbe addiert (Letzteres aus dem Kaggle-Datensatz-Eintrag laut Vorgänger-Recherche sucher-b, nicht neu geprüft).

**Lektion nach erkannter Fehlvorstellung [G, grob]** Laut dem Eedi/Google-Studienbericht führt die Plattform nach erkanntem Fehler zu Material zum Gesamtthema der Frage; weitere Bausteine sind kurze Erklärvideos, strukturierte Übung, Folge-Diagnosefragen, Wiederholungsquizze und ein Dialog-Tutor (https://arxiv.org/pdf/2512.23633; https://arxiv.org/pdf/2602.19296). Wie genau die Seite einer Lektion gestaltet ist, konnte ich ohne Konto **nicht sehen**. In der Studie mit Mensch-Tutor: Tutor prüft im Gespräch Frage und gewählte Antwort und beschriftet die vermutete Fehlvorstellung (https://www.eedi.com/news/misconception-diagnosis-from-student-tutor-dialogue-generate-retrieve-rerank).

**Craig Barton: Regeln für gute Diagnose-Fragen [G]** Fünf "goldene Regeln" im Blog von 2017 (https://medium.com/eedi/what-makes-a-good-diagnostic-question-b760a65e0320), in eigenen Worten: (1) klar und eindeutig, genau eine vertretbare richtige Antwort; (2) nur eine Fähigkeit oder ein Konzept; (3) schnell beantwortbar (der Blog nennt etwa 10 Sekunden; eine Hilfevideo-Seite von Barton nennt 20 Sekunden, https://mrbartonmaths.com/teachers/diagnostic-questions-help-videos/pedagogy.html, dort "vier" Regeln); (4) aus jeder falschen Antwort lässt sich etwas lernen; (5) man darf die Frage nicht richtig beantworten können, obwohl man eine zentrale Fehlvorstellung hat. Weitere Hinweise aus Schulnetzwerk-Blogs: Falsche Antworten nicht zufällig wählen, sondern aus erwartbaren Denkfehlern (https://researchschool.org.uk/north-london/news/uncovering-misconceptions-harnessing-diagnostic-questions-for-instant-high-quality-feedback-in-the-classroom); nach der Antwort die falschen Antworten erklären lassen und Folgefrage stellen.

**Datensätze (Lizenz je Datensatz)**
| Datensatz | Lizenz | Geprüft an | Felder / Umfang | Zugang |
|---|---|---|---|---|
| NeurIPS 2020 Education Challenge | **CC BY-NC-ND 4.0** [G] | https://eedi.com/projects/neurips-education-challenge (Wortlaut der Seite) | Aufg. 1/2: 27.613 Fragen, 118.971 Schüler, 15.867.850 Antworten; Aufg. 3/4: 948 Fragen, 4.918 Schüler, 1.382.727 Antworten; "umfangreiche Metadaten zu Fragen, Schülern und Antworten", Feldliste steht im Whitepaper (https://arxiv.org/abs/2007.12061, Abschnitt 3, von mir nicht gelesen) | Link "Download Eedi Dataset"; ob Anmeldung nötig: Seite sagt nichts, **nicht geprüft** |
| Kaggle "Eedi - Mining Misconceptions in Mathematics" (2024) | **nicht gefunden**; Eedi-Seite nennt keine Lizenz, Kaggle-Datenseite lieferte nur Metadaten | https://www.eedi.com/data-and-competitions; https://www.kaggle.com/competitions/eedi-mining-misconceptions-in-mathematics/data | laut Aufgabenbeschreibung: Distraktor + Liste von Fehlvorstellungs-Beschreibungen, Zuordnung vorhersagen; laut Paper 1.857 Fragen mit je vier Antworten, Fehlvorstellungen von Fachlehrkräften geschrieben (https://arxiv.org/pdf/2510.11502, Ausschnitt) | Kaggle-Konto und Regelzustimmung nötig [A, übliches Kaggle-Verfahren]; **nicht geladen** |
| Misconception Graph | Eedi-Seite zeigt "Public (Hugging Face)", **keine Lizenz sichtbar**; ein Preprint behauptet CC BY 4.0, Version 1.0 | https://www.eedi.com/data-and-competitions (Lizenz nicht dort); Hugging-Face-Seite ließ sich nicht abrufen | Konstrukt-Fehlvorstellung-Paare (Zahlen oben, Preprint) | Hugging Face, **nicht geprüft** |
| MAP / MIME (Kaggle 2025) | **nicht gefunden** | https://aclanthology.org/2025.aimecon-wip.3.pdf (nur Beschreibung) | über 52.000 Schülererklärungen zu 15 Aufgaben, Klassen 4-8, von Fachpersonen kodiert | Kaggle, **nicht geladen** |
| Question-Anchored-Tutoring-Dialogues-2k; NeurIPS 2022 CausalML | nicht geprüft | Eedi-Seite | Tutor-Dialoge bzw. A/B-Test-Zeitreihen | Hugging Face / CodaLab |

**Nutzbarkeit [M, ohne Rechtsberatung]**
- Idee übernehmen: Aufbau Konstrukt, Frage, drei benannte Distraktoren, Barton-Regeln (Ideen sind nicht geschützt [A]).
- Mit eigenen Worten neu fassen: Fehlvorstellungs-Bezeichnungen (der NeurIPS-Datensatz verbietet ND-Bearbeitungen in Weitergabe; die Kaggle-Texte sind ohne bekannte Lizenz).
- Mit Namensnennung übernehmen: erst, wenn die CC-BY-4.0-Angabe zum Graphen an der Originalseite gelesen wurde.
- Nicht übernehmen: Eedi-Datensatztexte und -Fragen 2020 (ND); Kaggle-Texte bis Lizenz geklärt.

### B) "Mathe sicher können" (DZLM / TU Dortmund)

- **Träger/Aufbau [G]** Initiative der Deutsche Telekom Stiftung; Leitideen Diagnosegeleitetheit, Verstehensorientierung, Kommunikationsförderung; Materialien für Lernende, Lehrkräfte, Fortbildende, Eltern (https://mathe-sicher-koennen.dzlm.de). Zielgruppe laut Startseite: leistungsschwache Lernende, vor allem nicht-gymnasiale Sek I. Jahrgänge laut Friedrich-Verlag-Beitrag 4 bis 7 [Ausschnitt] (https://www.friedrich-verlag.de/friedrich-plus/sekundarstufe/mathematik/zahlen-groessen/magazin-von-uns-empfohlen-4-1019); Online-Check laut IPN Klassen 3-7, laut Hessen und Kurzanleitung 4-6.
- **Themen [G]** Natürliche Zahlen; Brüche, Prozente, Dezimalzahlen; Sachrechnen (Startseite: für kommende Jahre geplant, nicht entwickelt; ein Beitrag von 2019 nennt Sachrechnen als drittes Paket, das ist ein **Widerspruch**, den ich nicht auflösen konnte).
- **Bausteinstruktur [G]** Je Baustein: Standortbestimmung (Diagnose, 1 Seite) plus Fördereinheiten (meist drei). Beispiel B1 "Brüche und Prozente verstehen": B1A Anteile von einem Ganzen bestimmen und darstellen (6 Seiten Förderung), B1B Prozente bestimmen und darstellen (3 Seiten), B1C Anteile von Mengen nehmen (4 Seiten) (https://mathe-sicher-koennen.dzlm.de/mskfiles/uploads/Dokumente/msk_df_b1abc-brueche-prozente-verstehen_260119.docx). Weitere Bausteine aus Suchtreffern: B2C Brüche und Prozente umwandeln, B3/B4 Rechnen mit Brüchen, D1 Stellenwerte von Dezimalzahlen, D2 Dezimalzahlen ordnen und vergleichen, N2A Zahlen am Zahlenstrahl (Inhaltsverzeichnisse der Cornelsen-Auszüge, [Ausschnitt]). Die vollständige Themenliste der Website konnte ich wegen robots.txt **nicht abrufen**.
- **Verstehensgrundlagen/Fehlvorstellungen [G, Ausschnitt]** Prinzip: Rechnen mit Prozenten setzt Anteilsvorstellung und Bruchverständnis voraus ("wer 3/4 von 12 nicht bestimmen kann, versteht 37 % von 79,95 € nicht") (https://wwwold.mathematik.tu-dortmund.de/~prediger/veroeff/14-MAREN-Paedagogik-fokussierte-Foerderung.pdf). Der didaktische Kommentar zu B4 nennt als häufigsten Fehler das komponentenweise Addieren und Subtrahieren (Zähler plus Zähler, Nenner plus Nenner) und empfiehlt, über Größenordnungen zu hinterfragen und mit Bruchstreifen zu verstehen, warum nur die Zähler addiert werden (https://mathe-sicher-koennen.dzlm.de/mskfiles/uploads/Dokumente/msk_didkomm_b4_260214.pdf, Ausschnitt). Eine vollständige Fehlerliste je Baustein habe ich nicht gelesen.
- **Lizenz [G]** Dokumentkopf von B1 (2. Auflage 2026, Cornelsen, "Open Educational Resources"): Weiterverwendung unter **CC BY-NC-SA 4.0** (Namensnennung, nicht kommerziell, Weitergabe unter gleichen Bedingungen) (PDF 260119 und DOCX, Links wie oben). Für andere Bausteine und für die älteren Cornelsen-Auszüge (2014, z. B. https://mathe-sicher-koennen.dzlm.de/mskfiles/uploads/docs/BausteinD2_S_Dezimalzahlen_ordnen_und_vergleichen.pdf) habe ich die Lizenz **nicht geprüft**.
- **Download [G]** Fördermaterialien "bei Cornelsen kaufen oder frei von der Webseite ziehen" (Kurzanleitung https://mathe-sicher-koennen.dzlm.de/mskfiles/uploads/Dokumente/msk-oc_kurzanleitung_stand260723.pdf); Word und PDF; Erklärvideos unter mathe-sicher-koennen.dzlm.de/erklaervideos; digitale Bruchstreifen https://dzlm.de/vam/msk-bruchstreifen.html. Die Fördermaterialien sind laut Kurzanleitung "nicht zum Selbstlernen", sondern für die gemeinsame Arbeit von Lehrkraft und Lernenden gedacht.
- **Online-Check [G]** 45 digitale Kurzdiagnose-Tests, entwickelt von Prediger, Hankeln, Groß, Kröhne, veröffentlicht 09.2024 (https://www.leibniz-ipn.de/de/forschen/publikationen/mathe-sicher-konnen-online-check-45-digitale-kurzdiagnose-tests); Auswertung verweist auf die Fördermaterialien. Zugang: Selbstregistrierung durch Lehrkraft, vorher Auftragsverarbeitungsvertrag der Schulleitung, Einwilligungen der Eltern (Kurzanleitung); in Hessen über das Schulportal. **Nicht ausprobiert** (Anmeldung nötig).
- **Algebra [G, Titel]** Ein eigener DZLM-Fortbildungsbaustein "Diagnose und Förderung von Verstehensgrundlagen: Algebra (Sekundarstufe)" mit Teil 1 Variable und Terme, Teil 2 Gleichungen, mit Tabelle der Grundvorstellungen (https://maco.dzlm.de/sites/maco/files/material-multi/dzlm_difsek_algebra_steckbrief_220622.pdf; Tabelle https://maco.dzlm.de/sites/maco/files/material-lul/dzlm_difsek_algebra_teil1_am3_tabelle_grundvorstellungen_220803.pdf). Lizenz **nicht geprüft**. [M] Das ist die beste frei zugängliche deutsche Quelle für die Regeln 6 bis 9 und 15 (Terme, Gleichungen), noch nicht ausgewertet.
- **Nutzbarkeit [M]** Ideen und Fehlerkategorien: frei. Wörtliche Aufgaben/Texte: nur mit Namensnennung und unter NC-SA; ein öffentliches Repo oder eine kommerzielle App wären damit unsicher (Rechtsfrage, wie schon in sucher-c). Empfehlung: lesen, in eigenen Worten und mit eigenen Aufgaben neu fassen, Quelle nennen.

### C) Deutschsprachige Fachdidaktik

| Quelle | Inhalt | Frei zugänglich? | Link / Status |
|---|---|---|---|
| Padberg, Wartha: Didaktik der Bruchrechnung (5. Aufl. Springer 2017) | Standardwerk, Fehlerstrategien, Grundvorstellungsumbrüche | **Buch**, nur Inhaltsverzeichnis/Teile frei | https://link.springer.com/book/10.1007/978-3-662-52969-0 |
| Padberg-Fehlerliste im Hochschulskript (HU Berlin) | 13 Fehlermuster Brüche und Dezimalzahlen, paraphrasiert unten | PDF frei, Lizenz unbekannt | https://didaktik.mathematik.hu-berlin.de/user/filler/did_alg_zt/2_Bruchrechnung.pdf [G] |
| Wartha: Fehler in der Bruchrechnung durch Grundvorstellungsumbrüche | Tagungsbeitrag (Regensburg) | frei (eldorado) | https://eldorado.tu-dortmund.de:443/bitstream/2003/30769/1/138.pdf [nur Titel/Ausschnitt] |
| Typische Fehler bei Addition und Subtraktion von Brüchen, Review zu empirischen Fehleranalysen (TU Dresden) | Review | Zugang unklar | https://fis.tu-dresden.de/portal/de/publications/typische-fehler-bei-der-addition-und-subtraktion-von-bruchen--ein-review-zu-empirischen-fehleranalysen(9afee9aa-9529-4407-9845-c426faa8f0de).html [nur Titel] |
| Malle: Didaktische Probleme der elementaren Algebra (1993) | Variablenaspekte (Gegenstands-, Einsetzungs-, Kalkülaspekt), Fehlverständnisse | Buch; Zusammenfassungen frei (Friedrich-Verlag-Hefte teils kostenpflichtig) | über Hamburger Fortbildungsfolien [Ausschnitt]: https://www.teds.uni-hamburg.de/teds-ime/professionalisierung/materialien/files/sitzung4/4-teds-ime-fortbildung-2024-09-pdf.pdf; Buchtitel aus Fachwissen [A], an keiner Seite geprüft |
| Prediger u. a. (Verstehensgrundlagen, Algebra, Bruch) | s. B) | größtenteils frei (MSK, MaCo) | siehe B |
| vom Hofe: Grundvorstellungen | Konzept "Brücke zwischen individuellen Vorstellungen und Mathematik" | Aufsätze/Bücher; Beschreibung frei | https://www.friedrich-verlag.de/friedrich-plus/sekundarstufe/mathematik/algebra/strukturen-als-basis-der-algebra-67 [Ausschnitt] |
| PIKAS, SINUS, ISB-Handreichungen zu Fehlern | **nicht gefunden / nicht geprüft** | n. a. | keine gezielte Seite aufgerufen |

**Zusammenfassung der dort beschriebenen Fehlerstrategien [G wo Quelle, sonst Lit]**
- Brüche (Padberg-Liste im HU-Skript): Zähler und Nenner getrennt addieren; ganze Zahl nur zum Zähler addieren; beim Multiplizieren Nenner beibehalten; bei Ganze mal Bruch den Nenner multiplizieren; beim Dividieren Zähler durch Zähler teilen und Nenner behalten; ganze Zahl durch Bruch falsch teilen.
- Dezimalzahlen: mehr Stellen = größer; Umwandlung Dezimal in Bruch mit falschem Nenner; Addition ohne Kommaausrichtung; ganze Zahl an die Nachkommastellen hängen; Komma im Produkt falsch; Komma bei Division ignoriert (Komma-trennt-Muster, Padberg 2002 laut https://schulentwicklung.nrw.de/materialdatenbank/material/download/2599).
- Algebra (Hamburger Folien nach Malle 1993/Prediger 2022): ungleichartige Terme zusammenfassen ("Obstsalat-Algebra", Buchstabe als Ding statt Zahl); falsche Metaphern verstärken den Fehler eher.
- Variablenbegriff (Friedrich-Verlag): Variable als allgemeine Zahl, als Unbekannte, als Veränderliche; Schwierigkeit beim Festlegen von unabhängiger und abhängiger Variable.
- Fehlermuster gegen Fehlerursachen: Wittmann (Beitrag im Dortmunder Dokument https://eldorado.tu-dortmund.de/bitstreams/c5a89264-d5cf-425d-b00b-af2029d9e2ae/download, Ausschnitt) trennt beides; Mustererkennung allein sagt nicht die Ursache.

### D) Englischsprachige Kataloge

| Quelle | Inhalt | Frei lesbar? | Lizenz |
|---|---|---|---|
| Mathematics Assessment Project (MARS, Shell Centre) https://map.mathshell.org | Classroom Challenges (Diagnose-Lektionen), Tests, Fortbildung | Seite sagt nichts zu Anmeldung; "über 3 Mio. Downloads" | Seite: "Copyright 2007-2015 MARS, University of Nottingham", **keine offene Lizenz genannt** [G] |
| NCETM "Misconceptions with the Key Objectives" (Primary) | Tabellen | Dokument frei laut sucher-c | Lizenz nicht geprüft |
| Brown & VanLehn 1980: Repair Theory, Cognitive Science 4 https://www.lri.fr/~mbl/Stanford/CS477/papers/RepairTheory-SeelyBrown.pdf | Theorie zu "Bugs" im schriftlichen Subtrahieren; Katalog aus BUGGY/DEBUGGY | PDF frei auf Hochschulserver | Urheberrecht Fachzeitschrift, nur zitieren |
| VanLehn-Bericht (DTIC): bei Analyse von tausenden Schülern 76 Arten von Subtraktions-Bugs https://apps.dtic.mil/sti/pdfs/ADA169361.pdf | Befund | frei | Behördenbericht, Lizenz nicht geprüft |
| Sleeman 1984: Mis-generalization (Kognitionswissenschafts-Tagung) https://escholarship.org/content/qt3k96n278/qt3k96n278.pdf | Mal-Regeln in Algebra als Fehlverallgemeinerung korrekter Regeln | frei | eScholarship, Lizenz nicht gelesen |
| Sleeman u. a. 1990, Machine Learning 5 https://link.springer.com/content/pdf/10.1023/A:1022607624441.pdf | Algebra-Operatoren, automatische Suche nach Mal-Regeln | frei | nicht geprüft |
| Matz (Extrapolation von Algebra-Regeln) | **nicht gefunden** | n. a. | n. a. |
| Booth, Barbieri, Eyer, Paré-Blagoev 2014 (J. of Problem Solving 7(1)) https://core.ac.uk/download/77937877.pdf; https://docs.lib.purdue.edu/jps/vol7/iss1/3 | Sechs Fehlerkategorien Algebra, Häufigkeit, Persistenz, Vorhersagekraft | frei | Lizenz auf der CORE-Seite **nicht erkennbar** |
| Swan, Wake, Joubert: Kognitiver Konflikt und Diskussion (FaSMEd) https://research.ncl.ac.uk/fasmed/positionpapers/Cognitive%2bconflict_Nottingham_ude_revised.pdf | Position Paper | frei | nicht geprüft |
| Swan & Burkhardt: Lesson Design for Formative Assessment (Educational Designer) https://educationaldesigner.org/ed/volume2/issue7/article24 | Studienergebnisse zu Diagnose-Unterricht | frei | nicht geprüft |

[M] Matz und die weitere Literatur "Algebra-Fehlerstudien" (außer Booth) habe ich nicht gefunden; für einen Fehlbild-Generator ist die Idee von Brown/VanLehn und Sleeman nützlich: Fehler sind kein Zufall, sondern lassen sich als kleine, systematisch fehlerhafte Regeln beschreiben, die man programmieren kann.

### E) SMART (Bayreuth) und bayerische Quellen
- **SMART Bayreuth [G aus sucher-c, hier nicht neu geprüft]** "Sammlung mathematischer Aufgaben als Hypertext mit TeX", Aufgabenbuch Gymnasium Jgst. 5 (2015) mit Nutzung nur für private und unterrichtliche Zwecke (https://btmdx1.mat.uni-bayreuth.de/smart/buch/smart_gym_j05.pdf). Meine Startseite-Abfrage (https://btmdx1.mat.uni-bayreuth.de/smart/) scheiterte an robots.txt. Eine Fehleranalyse habe ich dort **nicht gefunden**. Nicht verwechseln mit dem diagnostischen SMART (Melbourne): Online-Tests, die Fehlvorstellungen berichten (https://minerva-access.unimelb.edu.au/server/api/core/bitstreams/99ad81dd-b908-535a-a4c6-26b178f62349/content; smartvic.com nicht abgerufen). [G, Ausschnitt] Das Melbourne-System deckt viele Themen für 10- bis 16-Jährige ab und meldet Stufen sowie Fehler und Fehlvorstellungen je Schüler; das Dortmunder Papier zum MSK-Online-Check nennt es ausdrücklich als Vorbild (https://eldorado.tu-dortmund.de/bitstream/2003/41784/1/BzMU22_781.pdf).
- **Bayerische Mathematik-Tests (BMT), ISB [G]** Ergebnis-PDFs je Jahr mit Kurzbeschreibung der Aufgaben und Erfolgsquote je Teilaufgabe, z. B. BMT8 2025: 38.809 Schülerinnen und Schüler, 422 Gymnasien, Durchschnitt 8,71 BE, Erfolgsquote insgesamt 41,5 % (https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/BMT8_2025_Ergebnisse.pdf). Wiederkehrende Aufgabenthemen laut Kurzbeschreibungen: Gleichung lösen, Termumformung, Grundwertberechnung, Dezimalbrüche, Bruch kürzen, endlicher Dezimalbruch, Äquivalenznachweis, prozentuale Änderung, verzerrte Darstellung (BMT8 2017, 2018, 2024). **Typische Fehler sind dort nicht beschrieben**; eine Auswertung der Fehlerarten durch das ISB habe ich nicht gefunden. Einzelne Erfolgsquoten je Aufgabe habe ich nicht ausgelesen. Die Nutzungsbedingungen der PDFs sind weiter unklar (siehe sucher-c).
- **Weitere bayerische Quellen mit Fehleranalyse:** nicht gefunden (ISB-Handreichungen, Grundwissen: nicht abgerufen).

---

## 2. Katalog typischer Denkfehler Klasse 5-10 (eigene Formulierung)

**Lesehilfe.** Alle Beschreibungen und Beispiele sind selbst formuliert; kein Beispiel stammt aus den Quellen (einzelne Muster, z. B. Zähler plus Zähler, sind weit verbreitet und stehen in Quellen, die Zahlen sind aber andere). Jedes Zahlenbeispiel wurde per Skript nachgerechnet: richtiges Ergebnis stimmt, falscher Rechenweg liefert das genannte falsche Ergebnis, beide sind verschieden. Gleichungslösungen sind durch Einsetzen geprüft.
**Klasse** ist meine Annahme nach der üblichen Einführung (LehrplanPLUS Bayern nicht Eintrag für Eintrag geprüft) [A].
**Beleg**: Kurzverweise: **Pad** Padberg-Fehlerliste im HU-Skript; **MSK** Mathe sicher können (Ausschnitt); **Boo** Booth u. a. 2014 (nur Fehlerkategorie belegt, nicht das konkrete Zahlenbeispiel); **Eed** Eedi-Substack-Beispiele; **Mal** Hamburger Folien nach Malle/Prediger; **SM** Melbourne-SMART (Thema Dezimalvergleich); **FV** Friedrich-Verlag-Ausschnitt; **BV** Brown & VanLehn/VanLehn (Kategorie Subtraktions-Bugs); **ISB** Thema kommt in BMT-Aufgaben vor (kein Fehlerbeleg); **Lit** = Fachwissen, in dieser Recherche **an keiner Quelle geprüft** [A].


### Gruppe 1 Richtung / Vorzeichen

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R1-1 | Negativ: Betrag groß = Zahl groß | Beim Ordnen negativer Zahlen gilt die Zahl mit dem größeren Betrag als größer. | -7 und -3: richtig -7 < -3; falsch -7 > -3. | 6-7 | Boo (Kategorie Minuszeichen); Einzelmuster Lit |
| R1-2 | Kleinere von größerer Zahl | Es wird immer die kleinere von der größeren Zahl abgezogen, auch wenn die Reihenfolge das Ergebnis negativ machen müsste. | 3 - 8: richtig -5; falsch 5. | 5-7 | Eed |
| R1-3 | Beträge addiert, Minus übernommen | Bei Zahlen mit verschiedenen Vorzeichen werden die Beträge addiert und das Minus einfach davorgesetzt. | -9 + 4: richtig -5; falsch -13. | 6-7 | Lit |
| R1-4 | Änderung auf dem Zahlenstrahl falsch | Der Abstand zwischen einer negativen und einer positiven Zahl wird ohne Berücksichtigung der Nulllinie bestimmt. | Temperatur von -3 °C auf 5 °C: Anstieg 8 °C; falsch 2 °C. | 6-7 | Lit |
| R1-5 | Koordinaten vertauscht | Rechtswert und Hochwert werden vertauscht, der Punkt landet an der gespiegelten Stelle. | P(2; 5) heißt 2 nach rechts, 5 nach oben; falsch: 5 nach rechts, 2 nach oben (das ist P(5; 2)). | 5-7 | Eed |

### Gruppe 2 Zeichen-Paar

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R2-1 | Minus minus bleibt minus | Das Abziehen einer negativen Zahl wird wie das Abziehen einer positiven behandelt. | 11 - (-4): richtig 15; falsch 7. | 7 | Boo (Kategorie); Beispielmuster Lit |
| R2-2 | Minus mal Minus negativ | Das Produkt zweier negativer Zahlen wird negativ angegeben. | (-6)·(-3): richtig 18; falsch -18. | 7 | Lit |
| R2-3 | Zeichenregel auf Addition übertragen | Die Regel 'Minus und Minus gibt Plus' wird auf die Addition zweier negativer Zahlen angewandt. | (-5) + (-2): richtig -7; falsch 7. | 7 | Lit (klassische Übergeneralisierung) |
| R2-4 | Anzahl der Minuszeichen falsch gezählt | Bei mehreren Faktoren wird nur das Paar-Prinzip beachtet, nicht ob ein Minus übrig bleibt. | (-2)·(-3)·(-4): richtig -24; falsch 24. | 7 | Lit |
| R2-5 | Division gleicher Vorzeichen negativ | Der Quotient zweier negativer Zahlen wird negativ angegeben. | (-20) : (-4): richtig 5; falsch -5. | 7 | Lit |

### Gruppe 3 Rangfolge

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R3-1 | Strich vor Punkt | Es wird streng von links nach rechts gerechnet, Punktrechnung ignoriert. | 4 + 3·5: richtig 19; falsch 35. | 5 | Lit (sehr verbreitet; in gelesenen Quellen nicht ausdrücklich) |
| R3-2 | Mal vor Geteilt | Multiplikation wird vor der Division ausgeführt, obwohl beide gleichrangig von links nach rechts gelten. | 24 : 4 · 2: richtig 12; falsch 3. | 5 | Lit |
| R3-3 | Plus vor Minus | Bei gleichrangigen Plus- und Minusschritten wird zuerst die Addition ausgeführt. | 20 - 8 + 5: richtig 17; falsch 7. | 5 | Lit |
| R3-4 | Potenz vor Vorzeichen | Das Minus vor einer Potenz wird in die Basis gezogen. | -3²: richtig -9; falsch 9. | 7-8 | Lit |
| R3-5 | Bruchstrich ohne Klammer | Beim Übertragen eines Bruchs in eine Zeile fehlen Klammern um den Zähler. | (8 + 4) : 2 als '8 + 4 : 2' getippt: richtig 6; falsch 10. | 7-8 | Lit |
| R3-6 | Koeffizient mitquadriert | Beim Einsetzen in 3x² wird der Faktor 3 mit quadriert. | 3x² für x = 4: richtig 48; falsch 144. | 8 | Lit |

### Gruppe 4 Verteilen

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R4-1 | Nur ersten Summanden verteilt | Der Faktor vor der Klammer wird nur mit dem ersten Glied multipliziert. | 3(x + 4): richtig 3x + 12; falsch 3x + 4. | 7-8 | Boo (Kategorie Rechengesetze falsch angewandt) |
| R4-2 | Binomi ohne Mittelterm | Beim Quadrieren einer Summe wird jedes Glied einzeln quadriert. | (x + 5)²: richtig x² + 10x + 25; falsch x² + 25. | 8 | Boo (Beispielmuster in Kategorie 'property') |
| R4-3 | Kreuzglieder vergessen | Beim Ausmultiplizieren zweier Klammern werden nur die Produkte innen-innen und außen-außen gebildet. | (x + 2)(x + 3): richtig x² + 5x + 6; falsch x² + 6. | 8 | Lit |
| R4-4 | Wurzel aus Summe aufgeteilt | Die Wurzel wird auf die Summanden verteilt. | √(9 + 16): richtig 5; falsch 3 + 4 = 7 (denn 7² = 49, nicht 25). | 9 | Lit |
| R4-5 | Unvollständig ausgeklammert | Beim Ausklammern wird nur ein Summand durch den gemeinsamen Faktor geteilt. | 6x + 9: richtig 3(2x + 3); falsch 3(2x + 9). | 8 | Lit |

### Gruppe 5 Minusklammer

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R5-1 | Minusklammer: nur erstes Glied gedreht | Das Minus vor der Klammer wirkt nur auf das erste Glied. | 10 - (3 + 4): richtig 3; falsch 11. | 7 | Boo (Kategorie Minuszeichen) |
| R5-2 | Minusklammer mit Variable | Beim Auflösen von - (2x - 7) bleibt das Vorzeichen des zweiten Glieds unverändert. | 5x - (2x - 7): richtig 3x + 7; falsch 3x - 7. | 7-8 | Boo (Kategorie Minuszeichen) |
| R5-3 | Plusklammer wie Minusklammer | Vorzeichen in einer Klammer werden gedreht, obwohl ein Plus davor steht. | 8 + (-3 + 2): richtig 7; falsch 9. | 7 | Lit |
| R5-4 | Minusklammer in Gleichung | Der Vorzeichenfehler beim Auflösen der Klammer führt zu einer falschen Lösung der ganzen Gleichung. | 2x - (x - 3) = 7: richtig x = 4; falsch x = 10. | 8 | Lit |

### Gruppe 6 Tauschen und Bündeln

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R6-1 | Subtraktion vertauscht | Ein Term mit Minus wird so umgestellt, als wäre die Subtraktion vertauschbar. | 5 - x: richtig -x + 5; falsch x - 5 (bei x = 2: 3 gegen -3). | 7-8 | Lit |
| R6-2 | Division vertauscht | Es wird immer die größere durch die kleinere Zahl geteilt. | 3 : 12: richtig 0,25; falsch 4. | 5-6 | Lit (verwandt mit Eed-Eintrag zur Subtraktion) |
| R6-3 | Unterschiedliche Terme zusammengefasst | Ein Glied mit Variable und eine Zahl werden zu einem Glied vereinigt ('Obstsalat'). | 5a + 3 bleibt 5a + 3; falsch 8a (bei a = 2: 13 gegen 16). | 7 | Boo (Kategorie Variable); Mal (Obstsalat-Algebra, Hamburg-Folien) |
| R6-4 | Koeffizienten addiert statt multipliziert | Beim Multiplizieren von Termen mit zwei Variablen werden die Zahlen vor den Variablen addiert. | 3a · 4b: richtig 12ab; falsch 7ab. | 8 | Lit |
| R6-5 | Subtraktion assoziativ | Bei mehreren Minusschritten wird, als wäre es eine Summe, beliebig geklammert. | 20 - 7 - 3: richtig 10; falsch 16 (7 - 3 zuerst). | 5-6 | Lit |
| R6-6 | Wiederholtes Plus als Potenz | Aus a + a + a wird a³ statt 3a. | a + a + a: bei a = 2 richtig 6; falsch 8. | 7 | Lit |

### Gruppe 7 Waage

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R7-1 | Nur eine Seite verändert | Die Rechenschritte werden nur links ausgeführt, rechts bleibt die Zahl stehen. | 3x + 2 = 11: richtig x = 3; falsch 3x = 11, also x = 11/3. | 8 | Boo (Kategorie Gleichheit: nur eine Seite verändert) |
| R7-2 | Nicht alle Glieder geteilt | Beim Teilen durch den Faktor wird nur ein Glied geteilt. | 4x + 8 = 20, durch 4: falsch x + 8 = 5, x = -3; richtig x = 3. | 8 | Lit |
| R7-3 | Ungleichung: Umkehr vergessen | Beim Teilen durch eine negative Zahl bleibt das Ungleichheitszeichen stehen. | -2x < 6: richtig x > -3; falsch x < -3 (x = 0 erfüllt die Ausgangsungleichung, die falsche Lösung lässt es aus). | 8-9 | Boo (Kategorie Gleichheit/Ungleichheit) |
| R7-4 | Seitenwechsel ohne Vorzeichenwechsel | Ein Glied wird auf die andere Seite gebracht, ohne dass sich die Rechenart ändert. | x - 4 = 9: richtig x = 13; falsch x = 5. | 7-8 | Lit |
| R7-5 | Variable ohne Vorzeichenwechsel verschoben | Beim Sammeln der Variablen auf eine Seite wird addiert statt subtrahiert. | 5x = 2x + 9: richtig x = 3; falsch 7x = 9, x = 9/7. | 8 | Lit |
| R7-6 | Gleichheitszeichen als Rechenbefehl | Das Gleichheitszeichen wird als 'ergibt' gelesen und in Ketten gesetzt, die nicht stimmen. | 3 + 4 + 2 geschrieben als '3 + 4 = 7 + 2 = 9': die Kette sagt 3 + 4 = 7 + 2, also 7 = 9. | 5-6 | Boo (Kategorie Gleichheit); DZLM-Baustein 'Gleichheitszeichen' (nur Titel gesehen) |

### Gruppe 8 Umkehren

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R8-1 | Falsche Umkehrung bei Division | Aus x : 4 = 3 wird 3 : 4 statt 3 · 4. | x : 4 = 3: richtig x = 12; falsch x = 3/4. | 6-7 | Lit |
| R8-2 | Falsche Umkehrung beim Subtrahenden | Aus 15 - x = 6 wird x = 15 + 6. | 15 - x = 6: richtig x = 9; falsch x = 21. | 6-7 | Lit |
| R8-3 | Falsche Umkehrung beim Divisor | Aus 12 : x = 3 wird x = 12 · 3. | 12 : x = 3: richtig x = 4; falsch x = 36. | 7 | Lit |
| R8-4 | Quadrat durch Halbieren umgekehrt | Das Quadrat wird mit einer Division durch 2 rückgängig gemacht. | x² = 36: richtig x = 6 (oder -6); falsch x = 18. | 9 | Lit |
| R8-5 | Nur eine Lösung beim Wurzelziehen | Bei x² = c wird die negative Lösung vergessen. | x² = 49: richtig 7 und -7; falsch nur 7. | 9 | Lit |

### Gruppe 9 Einsetzen und Probe

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R9-1 | Zahl und Variable als Ziffernfolge | Beim Einsetzen wird 3x für x = 4 als 34 gelesen. | 3x für x = 4: richtig 12; falsch 34. | 7 | Lit |
| R9-2 | Negative Zahl ohne Klammer eingesetzt | Beim Einsetzen negativer Werte in Potenzen geht die Klammer verloren. | x² + 2x für x = -3: richtig 3; falsch -15. | 7-8 | Boo (Kategorie Minuszeichen) |
| R9-3 | Probe im falschen Schritt | Die Lösung wird in die schon (falsch) umgeformte Gleichung eingesetzt statt in die Ausgangsgleichung. | 3(x + 2) = 18 falsch zu 3x + 2 = 18 umgeformt, x = 16/3: Probe passt dort, aber nicht in der Ausgangsgleichung (22 statt 18); richtig x = 4. | 8 | Lit |
| R9-4 | Aufstellen: Umkehrfehler | Beim Aufstellen einer Beziehung 'sechsmal so viele S wie P' wird der Faktor an die falsche Größe geschrieben. | 12 Studierende (S), 2 Lehrende (P): richtig S = 6P (12 = 12); falsch 6S = P (72 = 2). | 8 | Lit (Clement-Studie 'Student-Professor', hier nicht geprüft) |

### Gruppe 10 Wert bleibt / Kürzen

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R10-1 | Kürzen in Summen | Im Bruch wird ein Summand im Zähler gegen den Nenner gekürzt. | (x + 6) / 6: richtig x/6 + 1; falsch x (bei x = 12: 3 gegen 12). | 7-8 | FV (Aussage 'Kürzen in Summen' schwer korrigierbar, Suchausschnitt) |
| R10-2 | Erweitern nur im Zähler | Beim Erweitern wird nur der Zähler mit der Zahl multipliziert. | 2/5 = 6/15; falsch 2/5 = 6/5. | 6 | Lit (Pad nennt nur die Regel 'Zähler und Nenner') |
| R10-3 | Erweitern durch Addition | Beim Erweitern wird zu Zähler und Nenner dieselbe Zahl addiert. | 3/4 = 6/8; falsch 3/4 = 5/6 (0,75 gegen 0,83). | 6 | Lit (verwandt mit Pad-Hinweis 'multiplizieren') |
| R10-4 | Gemischte Zahl falsch umgewandelt | Bei 2¾ werden die Ganzen zum Zähler addiert statt mit dem Nenner verrechnet. | 2¾ = 11/4; falsch 5/4. | 6 | Lit |

### Gruppe 11 Bruchrechnen

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R11-1 | Zähler plus Zähler, Nenner plus Nenner | Brüche mit verschiedenen Nennern werden komponentenweise addiert. | 3/4 + 1/6: richtig 11/12; falsch 4/10. | 6 | Pad; MSK (als häufigster Fehler genannt) |
| R11-2 | Ganze Zahl zum Zähler | Eine ganze Zahl wird nur zum Zähler addiert. | 2/7 + 3: richtig 23/7; falsch 5/7. | 6 | Pad |
| R11-3 | Nenner bei Multiplikation behalten | Beim Multiplizieren gleichnamiger Brüche wird nur der Zähler multipliziert. | 3/5 · 2/5: richtig 6/25; falsch 6/5. | 6 | Pad |
| R11-4 | Ganze mal Bruch: Nenner multipliziert | Beim Multiplizieren mit einer ganzen Zahl wird der Nenner statt des Zählers multipliziert. | 5 · 1/3: richtig 5/3; falsch 1/15. | 6 | Pad (gleiches Muster, anderes Zahlenbeispiel) |
| R11-5 | Zähler durch Zähler, Nenner bleibt | Beim Dividieren gleichnamiger Brüche wird der Nenner beibehalten. | 8/9 : 2/9: richtig 4; falsch 4/9. | 6 | Pad |
| R11-6 | Falschen Bruch umgekehrt | Beim Dividieren durch einen Bruch wird der erste statt der zweite Bruch gekehrt. | 1/2 : 3/4: richtig 2/3; falsch 3/2. | 6 | Lit |
| R11-7 | Gleichnamig, aber Nenner addiert | Bei gleichen Nennern werden die Nenner mitaddiert. | 2/5 + 1/5: richtig 3/5; falsch 3/10. | 5-6 | Lit (Variante des Pad-Eintrags 1) |
| R11-8 | Größerer Nenner, größerer Bruch | Beim Vergleich von Stammbrüchen wird die größere Nennerzahl als größerer Bruch gelesen. | 1/3 und 1/5: richtig 1/3 > 1/5; falsch 1/5 > 1/3. | 5-6 | Lit |
| R11-9 | Gleicher Abstand zur 1 gleich groß | Brüche, denen jeweils ein Stück zum Ganzen fehlt, gelten als gleich groß. | 5/6 und 7/8: richtig 5/6 < 7/8; falsch gleich groß. | 6 | Pad-Skript (Hinweis: Differenzen zu ganzen Zahlen betrachten) |
| R11-10 | Anteil von einer Menge: Zähler und Nenner vertauscht | Beim Berechnen von 'Bruch von Menge' wird durch den Zähler geteilt und mit dem Nenner multipliziert. | 3/4 von 12: richtig 9; falsch 16. | 6 | MSK (Thema 'Anteile von Mengen'); Fehlermuster Lit |
| R11-11 | Gemischte Zahlen komponentenweise | Bei der Multiplikation gemischter Zahlen werden Ganze mit Ganzen und Brüche mit Brüchen verrechnet. | 1½ · 2½: richtig 3¾; falsch 2¼. | 6-7 | Lit |

### Gruppe 12 Potenz

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R12-1 | Potenz als Mal | Der Exponent wird als Faktor gelesen. | 5²: richtig 25; falsch 10. | 7-8 | Eed |
| R12-2 | Basen multipliziert, Exponenten addiert | Beim Multiplizieren gleicher Potenzen wird auch die Basis verrechnet. | 2³ · 2⁴: richtig 2⁷ = 128; falsch 4⁷ = 16384. | 9 | Lit |
| R12-3 | Exponenten multipliziert statt addiert | Beim Multiplizieren gleicher Potenzen werden die Exponenten multipliziert. | 2³ · 2⁴: richtig 128; falsch 2¹² = 4096. | 9 | Lit |
| R12-4 | Potenz einer Potenz: Exponenten addiert | Bei (aᵐ)ⁿ werden die Exponenten addiert statt multipliziert. | (2²)³: richtig 64; falsch 2⁵ = 32. | 9 | Lit |
| R12-5 | Negativer Exponent als negative Zahl | Der Exponent -3 macht aus der Potenz eine negative Zahl. | 2⁻³: richtig 1/8; falsch -8. | 9-10 | Lit |
| R12-6 | Hoch null gleich null | Eine Potenz mit Exponent 0 wird als 0 gelesen. | 7⁰: richtig 1; falsch 0. | 9-10 | Lit |
| R12-7 | x mal x gleich 2x | Das Produkt gleicher Variablen wird als Verdopplung geschrieben. | x · x bei x = 5: richtig 25; falsch 10. | 7-8 | Eed (Quadrieren/Verdoppeln verwechselt) |
| R12-8 | Faktor in Klammer nicht mitquadriert | Beim Quadrieren von (3a) wird nur die Variable quadriert. | (3a)²: richtig 9a²; falsch 3a². | 8 | Lit |
| R12-9 | Zehnerpotenz als Nullen anhängen | Beim Multiplizieren mit 10² wird das Komma ignoriert und Nullen werden angehängt. | 4,5 · 10²: richtig 450; falsch 4500. | 6-7 | Lit |

### Gruppe 13 Stellenwert / Prozent

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R13-1 | Mehr Nachkommastellen = größer | Die Dezimalzahl mit mehr Ziffern wird für größer gehalten. | 0,7 und 0,35: richtig 0,7 > 0,35; falsch 0,35 > 0,7. | 5-6 | Pad; SM |
| R13-2 | Weniger Nachkommastellen = größer | Die Dezimalzahl mit mehr Stellen wird (wegen 'kleinerer Einheiten') für kleiner gehalten. | 0,45 und 0,4: richtig 0,45 > 0,4; falsch 0,4 > 0,45. | 5-6 | SM (Dezimalvergleich als Thema; Muster im Einzelnen Lit) |
| R13-3 | Nachkommastellen wie ganze Zahlen addiert | Beim Addieren werden die Ziffern rechts ausgerichtet statt die Stellenwerte. | 5,36 + 2,4: richtig 7,76; falsch 7,40. | 5-6 | Pad |
| R13-4 | Kommastellen beim Multiplizieren | Das Komma im Produkt wird nach der Stellenzahl eines Faktors gesetzt statt nach der Summe der Stellen. | 0,3 · 0,2: richtig 0,06; falsch 0,6. | 6 | Pad |
| R13-5 | Division durch Dezimalzahl: Komma ignoriert | Beim Teilen durch eine Dezimalzahl wird das Komma übersehen. | 8 : 0,2: richtig 40; falsch 4. | 6 | Pad |
| R13-6 | Teilen macht immer kleiner | Beim Teilen durch eine Zahl kleiner als 1 wird ein kleineres Ergebnis erwartet. | 8 : 0,5: richtig 16; falsch 4. | 6 | Lit (Fischbein, hier nicht geprüft) |
| R13-7 | Prozentzahl als Divisor | Die Prozentzahl wird als Teiler benutzt statt als Anteil. | 50 % von 80: richtig 40; falsch 80 : 50 = 1,6. | 7 | Lit |
| R13-8 | Dezimalzahl in Prozent: Komma falsch | Beim Umwandeln in Prozent wird mit 1000 statt 100 multipliziert. | 0,07 = 7 %; falsch 70 %. | 6-7 | Lit |
| R13-9 | Einheit um Faktor 10 statt 100 | Beim Umrechnen m in cm wird falsch gestuft. | 2,5 m: richtig 250 cm; falsch 25 cm. | 5-6 | Lit |
| R13-10 | Null im Stellenwert vergessen | Eine Stelle ohne Ziffer wird beim Aufschreiben ausgelassen. | 4 H, 0 Z, 7 E: richtig 407; falsch 47. | 5 | Lit |
| R13-11 | Abschneiden statt Runden | Beim Runden wird die nächste Stelle nicht beachtet. | 3,46 auf Zehntel: richtig 3,5; falsch 3,4. | 5-6 | Lit |

### Gruppe 14 Verhältnis

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R14-1 | Additiv statt multiplikativ | Beim Hochrechnen wird der Unterschied addiert statt das Verhältnis beibehalten. | 4 Tassen für 6 Personen; für 9 Personen: richtig 6 Tassen; falsch 7. | 6-7 | Lit |
| R14-2 | Teil:Teil als Anteil gelesen | Beim Verhältnis 2 : 3 wird 2/3 als Anteil am Ganzen angegeben. | Blau : Gelb = 2 : 3: Anteil Blau richtig 2/5; falsch 2/3. | 6-7 | Lit |
| R14-3 | Antiproportional als proportional | Mehr Arbeiter brauchen scheinbar auch mehr Zeit. | 3 Arbeiter 12 Tage; 6 Arbeiter: richtig 6 Tage; falsch 24 Tage. | 7 | Lit |
| R14-4 | Fläche wächst linear mit der Seite | Bei verdoppelter Seitenlänge wird nur die doppelte Fläche erwartet. | Quadrat: Seite 3 hat Fläche 9; Seite 6: richtig 36; falsch 18. | 7-9 | Lit |
| R14-5 | Maßstab: Nullen | Beim Umrechnen von cm in km wird durch eine Zehnerpotenz zu viel geteilt. | Maßstab 1 : 500 000, 3 cm: richtig 15 km; falsch 1,5 km. | 6-7 | Lit |
| R14-6 | Dreisatz verkehrt herum | Der Bezug wird umgekehrt: statt Preis pro Stück zu bilden, wird durch die neue Anzahl geteilt. | 5 Hefte 4 €; 8 Hefte: richtig 6,40 €; falsch 2,50 €. | 6-7 | Lit |

### Gruppe 15 Nullprodukt

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| R15-1 | Nullprodukt bei Produkt ungleich null | Der Satz vom Nullprodukt wird auf eine Gleichung angewendet, deren rechte Seite nicht null ist. | (x - 3)(x - 4) = 12: richtig x = 0 oder 7; falsch x = 15 oder 16. | 9-10 | Lit |
| R15-2 | Vorzeichen der Nullstellen | Aus einem Faktor (x - a) wird x = -a abgelesen. | (x - 4)(x + 2) = 0: richtig 4 und -2; falsch -4 und 2. | 9-10 | Lit |
| R15-3 | Durch x geteilt, Lösung verloren | Beim Teilen durch die Variable geht die Lösung x = 0 verloren. | x² = 5x: richtig x = 0 oder 5; falsch nur 5. | 9-10 | Lit |

### Gruppe 16 Bedeutungsfehler (richtig gerechnet, aber das Falsche)

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| B-1 | Prozent wovon: Hin und zurück | Ein Abschlag und ein gleich großer Aufschlag werden als sich aufhebend betrachtet. | 80 € minus 25 %, dann plus 25 %: richtig 75 €; falsch 80 €. | 7 | Lit |
| B-2 | Prozent vom falschen Grundwert | Beim Rückrechnen vom Endwert wird der Prozentsatz vom Endwert statt vom Anfangswert genommen. | 60 € nach 20 % Aufschlag: Anfangswert richtig 50 €; falsch 48 €. | 7 | Lit |
| B-3 | Prozentpunkte gegen Prozent | Eine Differenz in Prozentpunkten wird als relative Änderung in Prozent genannt. | 20 % auf 25 %: +5 Prozentpunkte, relativ +25 %; falsch 'um 5 %'. | 7-8 | Lit |
| B-4 | Absolute Änderung als Prozent | Die Differenz wird direkt als Prozentzahl geschrieben. | 200 auf 250: richtig +25 %; falsch +50 %. | 7 | ISB (BMT8 2018 Aufgabe 3 'Prozentuale Änderung' nur als Thema); Fehlermuster Lit |
| B-5 | Signalwort bestimmt die Rechenart | Das Wort 'weniger' löst automatisch eine Subtraktion aus, auch wenn die Aufgabe rückwärts gestellt ist. | Tom hat 4 € weniger als Lisa und 9 €. Lisa hat richtig 13 €; falsch 5 €. | 5-6 | Lit |
| B-6 | Rest ignoriert | Beim Sachbezug wird abgerundet, obwohl aufgerundet werden muss. | 25 Personen, 8 Plätze je Bus: richtig 4 Busse; falsch 3. | 5-6 | Lit |
| B-7 | Einheiten nicht umgerechnet | Zahlen mit verschiedenen Einheiten werden direkt addiert. | 1,2 km + 350 m: richtig 1550 m; falsch 351,2. | 5-6 | Lit |
| B-8 | Umfang gegen Flächeninhalt | Für die Fläche wird der Umfang berechnet oder umgekehrt. | Rechteck 7 cm mal 3 cm: Fläche richtig 21 cm²; falsch 20 cm (Umfang). | 5 | Lit |
| B-9 | Mittelwert der Mittelwerte | Zwei Gruppenmittel verschiedener Größe werden ungewichtet gemittelt. | Gruppe A: 2 Personen, Ø 10; Gruppe B: 8 Personen, Ø 20: richtig Ø 18; falsch 15. | 7-8 | Lit |
| B-10 | Median gleich Mittelwert | Die beiden Lagemaße werden verwechselt. | Daten 1, 2, 3, 10, 14: Median 3, Mittelwert 6; falsch Median 6. | 6-7 | Lit |
| B-11 | Alle Ergebnisse gleich wahrscheinlich | Bei der Augensumme zweier Würfel wird jede Summe als gleich wahrscheinlich gesehen. | Summe 7: richtig 6/36 = 1/6; falsch 1/11. | 7-9 | Lit |
| B-12 | Diagramm: Achse beginnt nicht bei 0 | Aus der Höhe der Säulen wird auf das Verhältnis der Werte geschlossen, obwohl die Achse später beginnt. | Werte 52 und 56, Achse ab 50: Säulen wirken 2 gegen 6 (dreimal so hoch); richtig nur etwa 8 % mehr. | 6-8 | ISB (BMT8 2017 4b 'Verzerrte Darstellung' nur als Thema) |
| B-13 | Einmal gleich = immer gleich | Zwei Terme werden nach einer einzigen Probe für äquivalent gehalten. | 2x und x² ergeben bei x = 2 beide 4, bei x = 3 aber 6 und 9: nicht äquivalent. | 8 | ISB (BMT8 2018 5b/5c 'Äquivalenznachweis' nur als Thema) |

### Gruppe 17 Sonstiges

| Nr. | Kurzname | Beschreibung | Beispiel (richtig / falsch) | Kl. | Beleg |
|---|---|---|---|---|---|
| S-1 | Division durch Null | Die Division durch 0 wird als 0 angegeben. | 5 : 0 ist nicht definiert; falsch 0 (denn 0 · 0 = 0, nicht 5). | 6-7 | Lit |
| S-2 | Spaltenweise kleinere von größerer Ziffer | Beim schriftlichen Subtrahieren wird in jeder Spalte die kleinere von der größeren Ziffer abgezogen. | 63 - 28: richtig 35; falsch 45. | 5 | BV (Kategorie 'Subtraktions-Bugs'); Beispielmuster Lit |
| S-3 | Null minus Zahl gleich Zahl | Beim schriftlichen Subtrahieren wird 0 - 4 als 4 gerechnet. | 700 - 4: richtig 696; falsch 704. | 5 | BV (Kategorie); Beispiel Lit |
| S-4 | Stellenversatz fehlt | Beim schriftlichen Multiplizieren wird die zweite Zeile nicht um eine Stelle eingerückt. | 23 · 14: richtig 322; falsch 115. | 5 | Lit |
| S-5 | Null im Quotienten vergessen | Beim schriftlichen Dividieren wird eine Null im Ergebnis ausgelassen. | 4200 : 7: richtig 600; falsch 60. | 5 | Lit |
| S-6 | Eins als Primzahl | Die Zahl 1 wird zu den Primzahlen gezählt. | Primzahlen bis 10: richtig 2, 3, 5, 7; falsch auch 1. | 5-6 | Eed |
| S-7 | kgV und ggT vertauscht | Das kleinste gemeinsame Vielfache wird mit dem größten gemeinsamen Teiler verwechselt. | kgV(4, 6): richtig 12; falsch 2. | 6 | Lit |
| S-8 | Nebenwinkel gleich Ergänzung auf 90° | Die Ergänzung auf 90° wird statt der auf 180° genommen. | Nebenwinkel zu 70°: richtig 110°; falsch 20°. | 5-7 | Lit |
| S-9 | Pythagoras: Wurzel vergessen | Nach dem Addieren der Kathetenquadrate wird die Wurzel nicht gezogen. | a = 3, b = 4: richtig c = 5; falsch c = 25. | 8-9 | Lit |
| S-10 | Steigung als Kehrwert | Bei der Steigung wird Rechtswert durch Hochwert geteilt. | 3 nach oben bei 2 nach rechts: richtig m = 3/2; falsch 2/3. | 8-9 | Lit |
| S-11 | Periodischer Dezimalbruch als endlich | Ein periodischer Dezimalbruch wird auf wenige Stellen gekürzt und dann als exakt behandelt. | 1/3 = 0,333...; falsch 1/3 = 0,3 (0,3 ist 3/10). | 6-8 | ISB (BMT8 2017 6b 'Endlicher Dezimalbruch' nur als Thema); Fehlermuster Lit |

**Zählung:** 114 Einträge. Davon mit ausschließlich "Lit" als Beleg (also in dieser Recherche nicht an einer Quelle geprüft): 79; die übrigen 35 haben mindestens einen Kurzverweis auf eine gelesene Quelle (bei Boo, ISB, SM, BV nur auf Fehlerkategorie oder Thema, nicht auf das genaue Muster).


---

## 3. Welche Fehler laut Forschung besonders häufig und hartnäckig sind, und was hilft

### 3.1 Häufig und hartnäckig (mit Beleg)
1. **Vorzeichen-/Minusfehler in der Algebra.** [G] Booth u. a. 2014 (https://core.ac.uk/download/77937877.pdf): 565 Algebra-I-Schüler (USA, 37 Klassen, 13 Schulen). Minus-Fehler waren mit Abstand die häufigsten (Mittel 1,96 je Schüler gegenüber 0,80 Rechenfehlern und 0,77 Variablenfehlern), in allen sechs Themen und über das Jahr hinweg; sie sagten Testleistung erst spät im Jahr voraus. Grenze: US-Stichprobe, Übungsarbeit, nicht Deutschland.
2. **Variablen- und Eigenschaftsfehler sind am gefährlichsten.** [G] Ebenda: Variablenfehler früh im Jahr sowie Fehler bei Rechengesetzen und Operationswahl früh und mittendrin sagten schlechte Leistung im Jahresendtest vorher; Gleichheits-/Ungleichheitsfehler mittendrin und spät. Bruchfehler waren häufig, aber **kein** signifikanter Vorhersager. [M] Für die App: Fehlbilder zu Variablen, Verteilen und Gleichheitszeichen früh und gründlich behandeln, nicht nur dort, wo am meisten falsch gemacht wird.
3. **Komponentenweise Bruchaddition.** [G, Ausschnitt] Im MSK-Kommentar als häufigster Fehler beim Addieren und Subtrahieren genannt (https://mathe-sicher-koennen.dzlm.de/mskfiles/uploads/Dokumente/msk_didkomm_b4_260214.pdf); ein Friedrich-Verlag-Beitrag nennt Zähler/Nenner-Addition und Kürzen in Summen als später schwer zu korrigieren (https://www.friedrich-verlag.de/friedrich-plus/sekundarstufe/mathematik/konzepte-methoden/fehler-im-ansatz-erkennen-und-vermeiden-11634). Das Muster entsteht laut Wartha/Prediger aus Grundvorstellungsumbrüchen (Rechnen mit natürlichen Zahlen wird auf Brüche übertragen) [Ausschnitt].
4. **Fehler wandern mit dem Alter.** [G] Eedi: Quadrieren mit Verdoppeln verwechseln sinkt mit dem Alter, x/y-Vertauschen **steigt** mit dem Alter, "kleinere von größerer abziehen" taucht über viele Themen wieder auf (https://eedi.substack.com/p/what-do-4-million-students-responses). Der Beitrag nennt keine Gesamthäufigkeit.
5. **"Obstsalat-Algebra".** [G, Ausschnitt] Laut Hamburger Fortbildungsfolien einer der Fehler, "den sehr viele Lernende und auch noch Lehrkräfte" machen (nach Malle 1993, Prediger 2022); Metaphern wie "a = Apfel" verstärken ihn eher.
6. **Richtige Antwort, falsche Begründung.** [G, Preprint] Bei Eedi-Fragen mit Erklärungstext gibt es verdeckte Fehlvorstellungen hinter richtigen Antworten (https://arxiv.org/pdf/2606.23205; https://ceur-ws.org/Vol-4282/short7.pdf, dort: zwei Fragen machen 71 % der verdeckten Fälle aus, weil sich ihre Frage mit falschem Verfahren richtig beantworten lässt). Nicht begutachtet, Fachbeitrag ist ein Preprint bzw. Workshop-Papier.
7. **Systematik statt Zufall.** [G] Fehler beim schriftlichen Subtrahieren folgen festen "Bug"-Regeln; bei tausenden Schülern wurden 76 Arten beobachtet (https://apps.dtic.mil/sti/pdfs/ADA169361.pdf). [M] Rechtfertigt, Fehlbilder als berechenbare Fehlerrechnungen zu führen.

### 3.2 Was über wirksame Gegenmaßnahmen bekannt ist (mit Grenzen)
- **Kognitiver Konflikt plus Diskussion.** [G] Diagnoseunterricht des Shell Centre (Vortest, gezielte Hürde, Material, das Konflikt erzeugt, Erklären und Diskutieren) war in mehreren Vergleichsstudien wirksamer als Vergleichsunterricht; im Beispiel Spiegelung (Birks 1987) gleiche Lerngewinne in der Stunde, aber deutlich bessere Langzeitwirkung bei "Konflikt plus Diskussion" (https://educationaldesigner.org/ed/volume2/issue7/article24; https://ncm.gu.se/wp-content/uploads/2020/06/6_34_007024_swan.pdf). Bell 1993: bessere Behaltensleistung als Heft-Unterricht bei Brüchen (Zusammenfassung https://www.bohrium.com/paper-details/some-experiments-in-diagnostic-teaching/812289745898962945-849). Grenzen: Klassenunterricht mit Gespräch; eine App kann nur Vorhersage-Frage, Gegenbeispiel und Erklärfrage nachbauen [M]. Studien sind älter und teils klein [A].
- **Fehlerhafte Lösungsbeispiele erklären.** [G, Ausschnitt] Adams u. a.: 208 Mittelstufenschüler, Dezimalzahlen; Erklären fiktiver Fehler gegen Aufgabenlösen mit Rückmeldung: kein Unterschied direkt danach, aber besser in der Woche darauf (d = 0,62) (https://dfki.de/web/forschung/projekte-publikationen/publikation/8598, Seite nennt als Jahr 2012 mit Band-Angabe, die ich nicht verifizieren konnte). Booth u. a. 2013 und Barbieri & Booth 2016 untersuchen dasselbe für Algebra (Titel gesehen, Ergebnisse **nicht gelesen**). Durkin & Rittle-Johnson: Vergleich fehlerhafter und richtiger Beispiele half in einer kleinen Studie (N = 74), in der größeren Dissertationsstudie (N = 342, Klasse 4-5) gab es **keine** Haupteffekte, Vergleichen war nicht besser als nacheinander Lernen, bei Schülern mit wenig Vorwissen teils schlechter; die Autorin fordert mehr Anleitung (https://ir.vanderbilt.edu/handle/1803/15069, https://ir.vanderbilt.edu/handle/1803/11934). Fazit [M]: Wirkung bei Schülern mit etwas Vorwissen wahrscheinlich, bei Anfängern unsicher; deshalb erst richtiges Beispiel, dann Fehlerbeispiel, mit Leitfragen.
- **Vergleichen.** [Ausschnitt] Ein Algebra-Aufsatz verweist auf Befunde, dass Erklären von Fehlern plus Erklären von Strategien mehr bringt als nur richtige Beispiele (Durkin & Rittle-Johnson 2009; Siegler & Chen 2008), aus https://escholarship.org/content/qt66v8b7nc/qt66v8b7nc.pdf; Originale nicht gelesen.
- **Verstehen vor Verfahren.** [G, Ausschnitt] MSK: Bruchstreifen und Größenvergleich, um komponentenweises Addieren zu hinterfragen; Aufbau von Grundvorstellungen statt Regeln (MSK-Kommentar, vom Hofe).
- **Sofortige Rückmeldung nach Fehler-Benennung.** [G, Vorgänger-Recherche sucher-b] Eedi/Google-Studien: Tutoring nach erkanntem Fehler hilft bei Folgeaufgaben (ähnliche Aufgaben 56-58 % gegen 43 %), aber **kein Effekt im standardisierten Test**; beide Studien mit Beteiligung des Herstellers. Dort nicht neu geprüft.
- **Nicht belegt:** Die Aussage, "Fehlvorstellung" statt "falsche Antwort" zu sagen senke Angst, steht in einem Nachhilfe-Blog ohne Quelle (https://thirdspacelearning.com/blog/diagnostic-questions/), von mir **nicht verifiziert**.
- **Risiko.** [Ausschnitt] Falsche Antwortoptionen könnten Fehler einprägen; Gegenmittel laut einem Schulnetzwerk-Blog: Optionen besprechen und Fehlvorstellung offen ansprechen (https://researchschool.org.uk/durrington/news/using-diagnostic-questions). Keine Studie dazu gelesen.

---

## 4. Checkliste: gute Diagnose-Aufgaben
Herkunft: **[B]** Craig Barton (Blog 2017), **[M]** meine Ableitung bzw. Meinung, **[A]** Annahme.
1. Genau eine Fähigkeit je Frage; bei mehrschrittigen Aufgaben die Schritte trennen oder nur einen Schritt als Falle bauen. [B]
2. Eindeutig formuliert, genau eine richtige Antwort; Mehrdeutigkeit vorher prüfen (zweiten Leser fragen). [B]
3. Kurz beantwortbar (Barton: etwa 10 bis 20 Sekunden); keine langen Nebenrechnungen, sonst vermischen sich Fähigkeiten. [B]
4. Jede falsche Antwort ist ein **benannter** Denkfehler aus dem Katalog (ID), nie ein zufälliger Wert; drei Distraktoren. [B]
5. Nicht richtig lösbar mit einer zentralen Fehlvorstellung: Zahlen so wählen, dass der Fehlweg nicht zufällig das richtige Ergebnis liefert (Beispiel: Zähler-plus-Zähler-Rechnung darf nicht zufällig stimmen; bei "Kürzen in Summen" kein Fall, in dem es klappt). Per Programm prüfen: Fehlweg-Ergebnis ungleich richtigem Ergebnis. [B, M]
6. Distraktoren voneinander unterscheidbar: jeder Fehlweg liefert ein eigenes Ergebnis (keine zwei Fehler mit derselben Zahl). [M]
7. Reihenfolge der Antworten zufällig; Distraktoren plausibel (ähnliche Größe, gleiche Einheit). [M]
8. Sicherheits-Abfrage: bei einem Teil der Fragen "Wie sicher?" oder kurze Begründung per Auswahl; richtige Antwort mit falscher Begründung zählt als "wackelt" (Eedi-Forschung zu verdeckten Fehlvorstellungen, https://arxiv.org/pdf/2606.23205, Preprint). [M]
9. Rateschwelle senken: bei vier Optionen 25 % Raten; deshalb Wiederholung mit anderen Zahlen und ein Teil ohne Auswahl (freie Eingabe). [M, A]
10. Zwei-Stufen-Auswertung: erst richtig/falsch, dann Distraktor-ID; eine einzelne Wahl ist nur ein Hinweis, erst zweite Bestätigung mit anderer Aufgabe macht aus "Hinweis" ein "Fehlbild". [M]
11. Auch Kenntnis der Voraussetzung testen: bei Fehler in Regel X zuerst die Verstehensgrundlage (z. B. Bruchstreifen-Größenvorstellung) prüfen, wie MSK es beschreibt. [M, MSK]
12. Nach der Antwort Begründung der Fehlwahl zeigen, Gegenaufgabe (Trennaufgabe) stellen; ohne Hilfe wiederholen. [M, Swan/Bell, siehe 3.2]
13. Sprache: "Denkweise" statt "Fehler"; neutral. [A]
14. Fragen vor Einsatz am echten Kind testen und auswerten, welche Distraktoren nie gewählt werden (Eedi tut das mit Millionen Antworten; in der Familie nur grob möglich). [M]

---

## 5. Lücken: wenig belegte Themen

| Thema / Regel | Befund |
|---|---|
| 3 Rangfolge | In den gelesenen Quellen kein ausdrücklicher Fehlerbeleg (Booth hat keine Rangfolge-Kategorie); Fehler sehr plausibel, aber Lit. |
| 8 Umkehren, 9 Einsetzen und Probe | Kaum Quellen gefunden; Booth zählt Operationsfehler (Addieren statt Multiplizieren) als vorhersagekräftig, nicht aber Umkehrfehler im Einzelnen. |
| 10 Wert bleibt/Kürzen | Nur der Ausschnitt "Kürzen in Summen" (Friedrich-Verlag); Erweitern/Kürzen als Konzept sind im Padberg-Skript, die Fehlmuster dort aber nicht ausgelesen. |
| 12 Potenz | Nur Eedi-Beispiel (Quadrieren/Verdoppeln); Potenzgesetze (Kl. 9-10) ohne gelesene Quelle. |
| 14 Verhältnis, Dreisatz, Maßstab | Keine Quelle gelesen. |
| 15 Nullprodukt, Quadratische Gleichungen | Keine Quelle gelesen. |
| Stochastik, Statistik, Diagramme | Nur Aufgabenthemen aus BMT-Beschreibungen, keine Fehlerquellen. |
| Geometrie (Winkel, Pythagoras, Flächen) | Außerhalb der 15 Regeln; Einträge nur als Lit. |
| Deutsch-Bayern-spezifisch | Keine bayerische Fehlerstudie gefunden; ISB liefert Erfolgsquoten ohne Fehlerarten. |
| IB MYP | Kein Fehlerkatalog gefunden (MYP-Guides unter © IBO, siehe sucher-c). |
| Klasse 9-10 allgemein | Quellenlage dünner als für Brüche/Dezimalzahlen/Algebra Grundlagen. |

---

## 6. Was ich nicht prüfen konnte
- Lizenz des Kaggle-Datensatzes "Mining Misconceptions" und des MIME/MAP-Datensatzes (Kaggle-Anmeldung nötig, Eedi-Seite nennt keine); Lizenz des Misconception-Graphen an der Originalseite (Hugging-Face-Abruf scheiterte).
- Feldliste des NeurIPS-2020-Datensatzes (steht im Whitepaper Abschnitt 3, nicht gelesen) und ob der Download Anmeldung braucht.
- Aufbau einer Eedi-Lektion in der Oberfläche (nur Studienbeschreibungen).
- Vollständige Themenliste, Bausteinliste und Lizenz aller MSK-Bausteine (Website per robots.txt gesperrt; nur B1 mit Lizenz gesehen); MSK-Fehlerlisten je Baustein.
- Padberg-Buch, Malle-Buch, vom-Hofe-Texte, PIKAS, SINUS, ISB-Handreichungen (nicht frei oder nicht aufgerufen); Matz.
- SMART Bayreuth Startseite (robots.txt); SMART Melbourne Website; ISB-Einzelquoten je BMT-Aufgabe; mögliche ISB-Fehleranalysen.
- Volltexte der Studien zu fehlerhaften Beispielen (Booth 2013, Barbieri & Booth 2016) und Wirkungsangaben aus Vorgänger-Recherche (sucher-b) nicht neu geprüft.
- Alle Klassenangaben im Katalog sind Annahmen (LehrplanPLUS nicht abgeglichen). Die Einträge mit "Lit" sind nicht an einer Quelle belegt und sollten vor Einsatz am Kind gegen Schulbuch oder Kinderarbeitshefte gegengeprüft werden.
