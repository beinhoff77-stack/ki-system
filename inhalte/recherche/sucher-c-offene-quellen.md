# Sucher C: Offene Inhalte, Datenquellen, Schnittstellen, Rechtsrahmen (Mathe Sek I, Bayern)

Abrufdatum aller Quellen: 25.11.2026. Methode: nur Websuche und Seitenabruf. Keine Anmeldung, keine Downloads außer Lesen von Webseiten.
Kennzeichnung: **[gesichert]** = auf der genannten Seite gelesen; **[Sekundär]** = nur aus Suchtreffer/Drittseite; **[Annahme]** = meine Schlussfolgerung; **[Meinung]** = Bewertung. Ausdrücklich: **keine Rechtsberatung**.

---

## A) Offene Lerninhalte Mathe Klasse 5-10

### A1 Serlo (de.serlo.org)
- Was: Erklärartikel, Kurse, Videos, interaktive Aufgaben mit Lösungen. Laut Serlo über 18.000 Artikel/Kurse/Videos/Aufgaben für Mathe und andere Fächer [gesichert, https://en.serlo.org/serlo]. Genauer Umfang nur Mathe Klasse 5-10: **nicht gefunden**. Bezug zu LehrplanPLUS Bayern: **nicht gefunden** (Serlo ordnet nach eigener Taxonomie, [Annahme] nicht nach bayerischem Lehrplan).
- Lizenz: Inhalte standardmäßig CC BY-SA 4.0; abweichend lizenzierte Inhalte (Drittmaterial) sind pro Inhalt in einem Lizenz-Element gekennzeichnet [gesichert, https://en.serlo.org/terms]. Eine Zeitung der Fachdidaktik-Szene merkt an, dass es einzelne Ausnahmen auch bei Routineaufgaben gibt (Button "Lizenz" neben der Aufgabe) [Sekundär, friedrich-verlag.de].
- Zugang: GraphQL-Endpunkt `https://api.serlo.org/graphql` (POST), Playground `https://api.serlo.org/___graphql` [gesichert, https://github.com/serlo/documentation/wiki/GraphQL-API]. Einzelne Inhalte per `uuid(id: ...)`.
- Metadata API (über denselben Endpunkt): liefert **nur Metadaten und Links**, keinen Fließtext. Felder u. a. Titel, Autoren, Daten, Lizenz, Fach, Taxonomie-Zuordnung. Max. 1000 Datensätze je Abruf, Cursor-Paginierung, Filter `instance` (de, en, es, ta, hi, fr) und `modifiedAfter`; kein Löschfeed. Die Metadaten selbst stehen unter CC BY-SA 4.0 und die Nutzung ist laut Serlo kostenlos [gesichert, https://github.com/serlo/documentation/wiki/Metadata-API; https://de.serlo.org/metadata].
- Kosten: keine. Einschränkung: Nutzungsbedingungen sagen nichts zu automatisiertem Abruf [gesichert, https://en.serlo.org/terms]; die API ist aber ausdrücklich für Einbindung durch Dritte gedacht.
- Anmerkung: Der Quellcode der API ist öffentlich (https://github.com/serlo/api.serlo.org). Ob der Volltext einer Aufgabe/eines Artikels über `uuid` sauber abrufbar ist (JSON-Format des Serlo-Editors), habe ich **nicht getestet** [Annahme: ja, Struktur muss selbst ausgewertet werden].

### A2 Khan Academy
- Lizenz: Die Support-Seite verweist für Videos und Übungen auf CC BY-NC-SA, mit Pflicht zur Namensnennung; "nicht kommerziell" heißt dort: nicht direkt auf Umsatz/Gewinn gerichtet, Werbung zählt als kommerziell [gesichert, https://support.khanacademy.org/hc/en-us/articles/202262954-Can-I-use-Khan-Academy-s-videos-name-materials-links-]. Widerspruch: Eine Hochschulbibliothek schreibt, Khan habe den CC-Hinweis entfernt und sei kein OER-Repositorium mehr [Sekundär, https://hcc.edu/library/build-your-oer-course/find-oer/oer-videos/khan-academy]. Aktueller Stand für Übungsinhalte daher **unklar**.
- API: Die öffentliche API wurde laut Khan-Mitarbeiter 2020 abgeschaltet [gesichert, https://github.com/Khan/khan-api/issues/149: "will be deprecated ... by July 2020"]; Drittquelle bestätigt: keine aktive öffentliche Inhalts-API [Sekundär, rapidevelopers.com, apis.io].
- Nutzungsbedingungen: Ein Auszug der AGB (Stand Mai 2026) verbietet automatisierte Systeme/Robots zum Zugriff und das Kopieren von Teilen des Dienstes [Sekundär, conductatlas.com]; die Khan-Support-Seite verbietet u. a. Bots/automatisierte Konten und nur persönliche, nicht kommerzielle Nutzung [gesichert, https://support.khanacademy.org/hc/de/articles/42929097425037]. Ergebnis: **Scraping nicht empfehlenswert.**
- Deutsch: Es gibt eine deutsche Fassung (de.khanacademy.org) und den Verein KA Deutsch e. V.; Umfang für Klasse 5-10 **nicht geprüft**.

### A3 OpenStax
- Prealgebra, Elementary Algebra, Intermediate Algebra: CC BY 4.0, kostenlos in Web/PDF [gesichert, https://openstax.org/books/intermediate-algebra/pages/preface; https://math.libretexts.org/Bookshelves/PreAlgebra/Prealgebra_2e_(OpenStax)]. Algebra 1 (2025): CC BY-NC-SA 4.0, nutzt auch IM-Inhalte [gesichert, https://openstax.org/books/algebra-1/pages/about-this-course].
- Einschränkung: Englisch, US-College-Niveau (Prealgebra/Algebra), Bezug zu Bayern: keiner. Kein API-Zugang gefunden; Bücher als PDF/HTML. Bild-Drittmaterial teils eigene Lizenz (Bildunterschrift beachten) [gesichert, Preface Prealgebra 2e].

### A4 Illustrative Mathematics (IM)
- IM K-12 Math (2019-2021, Klassen 6-8 in IM 6-8): CC BY 4.0, kommerziell und nicht kommerziell. Neuauflage IM v.360 (2024): CC BY-NC 4.0 [gesichert, https://illustrativemathematics.org/?p=17146; https://www.illustrativemathematics.org/im-trademark-usage-policy/]. Name/Logo "Illustrative Mathematics" nicht frei nutzbar. Gratis digital über Kendall Hunt (im.kendallhunt.com) bzw. AccessIM.
- Englisch, US-Standards; als Aufgaben- und Aufbau-Inspiration brauchbar. Offizielle Datenschnittstelle: **nicht gefunden**.

### A5 CK-12
- Früher CC BY-NC 3.0 für FlexBooks [Sekundär, Wikipedia]. Inzwischen ersetzt durch "CK-12 Curriculum Materials License" plus Terms of Use; die Seiten nennen persönliche und nicht kommerzielle Bildungsnutzung, Details zur Weitergabe/Bearbeitung habe ich **nicht ausgewertet** [gesichert, https://help.ck12.org/hc/en-us/articles/50990257420955-CK-12-Curriculum-Materials-License, https://help.ck12.org/hc/en-us/articles/53032403416219-Can-I-Use-CK-12-Content-to-Make-Money]. [Meinung] wegen Lizenzwechsel und fehlender offener Lizenz nicht als Übernahmequelle verwenden.

### A6 ZUM-Unterrichten / ZUM-Wiki / Mathematik-digital
- Wikis auf ZUM.de stehen unter CC BY-SA (ältere Seiten 3.0 DE, neuere 4.0) [gesichert, https://www.bildungsserver.de/bildung+innovation/die-idee-der-offenen-bildungsmedien-wird-hier-gelebt-984.html; Kirst 2015 auf Deutsch-Lernen.ZUM.de]. H5P-Inhalte auf apps.zum.de: CC0/CC BY/CC BY-SA, aber eingebettete Drittinhalte können anders lizenziert sein [Sekundär, Vogel OER 2022].
- Technik: MediaWiki-Software [gesichert, Kirst 2008]; eine offizielle MediaWiki-API ist deshalb [Annahme] vorhanden (`api.php`), **nicht geprüft**. Qualität schwankend (Community-Wiki) [Sekundär, ecml.at]. Bezug zu LehrplanPLUS Bayern: **nicht gefunden**.

### A7 MUNDO / WirLernenOnline (WLO) / OER-Portale
- Das sind Aggregatoren (Verweise auf fremde Materialien), keine eigenen Aufgabenbanken. WLO: Lizenzen überwiegend CC BY und CC BY-SA, Filter nach Lizenz, keine Anmeldung [Sekundär, https://www.uni-due.de/ub/oer/oer-suchen-und-finden.php, Stand 02/2025]. WLO/OpenEduHub basiert auf edu-sharing; Serlo-Metadaten fließen ein [gesichert, Serlo Metadata API development]. Öffentliche WLO-API-Dokumentation: **nicht gefunden** (GitHub-Organisation openeduhub existiert) [Sekundär]. MUNDO: "anhand der Bildungsstandards geprüft" [Sekundär, Uni Potsdam OER-Liste]; API: **nicht gefunden**.
- Wichtig: Lizenz steht je Einzelmaterial; Portal-Treffer sind nicht automatisch frei.

### A8 GeoGebra
- Software und Materialien: Nutzung nur nach GeoGebra-Lizenz; Materialien unter CC BY-NC-SA, Software für nicht kommerzielle Nutzung frei, kommerziell nur mit Vertrag [gesichert, https://geogebra.org/license, "last updated November 2025"; https://github.com/geogebra/legal]. Einbettung in eigene Seite ist technisch möglich, Details der Einbettungsbedingungen **nicht geprüft**. Offline-Fähigkeit der Web-Einbettung: **nicht geprüft**.

### A9 Wikibooks "Mathe für Nicht-Freaks"
- Texte CC BY-SA 3.0, kommerzielle Nutzung erlaubt, Namensnennung "Mathe für Nicht-Freaks" nötig; Bilder/Videos unter verschiedenen Lizenzen, die aber mit einer CC-BY-SA-Arbeit verträglich sein sollen [gesichert, https://de.wikibooks.org/wiki/Mathe_f%C3%BCr_Nicht-Freaks:_Kopiere_uns]. Schwerpunkt Hochschul-Analysis/LA [Annahme]; für Sek I wenig. Zugang: MediaWiki, [Annahme] API vorhanden.
- "Mathematrix: BY GYM" (Wikibooks) enthält Aufgaben Klasse 5-12; Lizenz, Herkunft und Bayern-Bezug auf der abgerufenen Seite **nicht erkennbar** [gesichert, https://de.wikibooks.org/wiki/Mathematrix:_BY_GYM/_Aufgaben_alle/_00]. Nicht übernehmen ohne Klärung.

### A10 Mathigon / Polypad
- Polypad ist auf der Website frei für persönliche, schulische, nicht kommerzielle Nutzung; für Einbindung per API gibt es eigene Lizenzbedingungen und API-Key [gesichert, https://polypad.amplify.com/partners]. Mathigon Studio (Quellcode) liegt öffentlich vor; Bilder/Dokumentation CC BY-SA 4.0 [Sekundär, Repo-Lizenzhinweis über whitesource-Index]. Code-Lizenz: **nicht eindeutig geprüft**.

### A11 LearningApps / H5P
- LearningApps: nicht kommerziell, kostenlos für Bildungszwecke; Urheber der einzelnen Bausteine verantwortlich; die Plattform behält sich Einschränkung bei übermäßiger Nutzung vor [gesichert, https://learningapps.org/rechtliches.php]. Eine generelle offene Lizenz für fremde Apps: **nicht gefunden** (also nicht übernehmen).
- H5P als Format: Lizenz je Inhalt; keine zentrale Sammlung geprüft.

### A12 Weitere, im Lauf der Suche gefunden
- **SMART** (Universität Bayreuth, "Sammlung mathematischer Aufgaben als Hypertext mit TeX"), Aufgabenbuch Gymnasium Jahrgangsstufe 5 (Stand 2015): "für private und unterrichtliche Zwecke", kommerziell nur nach Genehmigung [gesichert, https://btmdx1.mat.uni-bayreuth.de/smart/buch/smart_gym_j05.pdf]. Also Bayern-Bezug vorhanden, aber **keine offene Lizenz** (keine Weitergabe-/Bearbeitungsrechte genannt). Es gibt auch eine Realschul-Fassung (smart_rs_j05). Weitere Jahrgänge: nicht geprüft.
- **cosh** (Baden-Württemberg, ZSL): Kopfübungen CC BY 4.0, Bezug BW-Lehrplan [gesichert, https://www.schule-bw.de/.../cosh/kopfuebung_1_cosh]. Nur Hinweis auf offen lizenzierte Aufgabenform; Lehrplan nicht Bayern.

---

## B) Offizielle bayerische Quellen

### B1 LehrplanPLUS (lehrplanplus.bayern.de)
- Nutzungsbedingungen [gesichert, https://www.lehrplanplus.bayern.de/seite/nutzungsbedingungen]: Die **Texte der Lehrpläne unterliegen nicht dem Urheberrechtsschutz**. Für alle weiteren Inhalte der Seite gilt deutsches Urheberrecht. Nicht kommerzielle Nutzung gestattet, soweit keine Rechte Dritter berührt sind; kommerzielle Nutzung nicht gestattet, **ausgenommen die Originaltexte der Lehrpläne**. Quelle immer nennen. Bearbeitung nur für nicht kommerzielle schulische oder wissenschaftliche Zwecke; KI-gestützte Anwendungen dafür zulässig, wenn ausschließlich diesen Zwecken dienend und datenschutzkonform. Das Angebot richtet sich an Lehrkräfte. **Zu automatisiertem Abruf (Crawling/Scraping) steht nichts auf der Seite.**
- Maschinenlesbar: Es gibt eine PDF-Sammlung-Funktion und HTML-Seiten je Jahrgangsstufe/Fach (z. B. https://www.lehrplanplus.bayern.de/schulart/gymnasium/jgs/5/fach/mathematik). Eine offizielle Datenschnittstelle (API, JSON, Open Data): **nicht gefunden**. Grundwissen/Kompetenzerwartungen müssten daher aus HTML/PDF selbst strukturiert werden.
- [Annahme] Eigene Zusammenfassungen/Strukturierung der Kompetenzerwartungen (Stichworte, Themen-IDs) ist der sichere Weg; wörtliche Übernahme der Lehrplantexte ist laut ISB-Aussage urheberrechtlich frei, wegen des Satzes "kommerzielle Nutzung ausgenommen Originaltexte" ist das für den Originaltext auch kommerziell offen. Grenze zwischen "Originaltext" und ISB-Zusatzmaterial (Erläuterungen, Beispiele, Bilder) ist nicht definiert, siehe Rechtsfragen.

### B2 Bayerische Mathematik-Tests (BMT), Gymnasium
- Gymnasium: zentral erstellte Jahrgangsstufentests Mathematik in **Jahrgangsstufe 8 und 10** zu Schuljahresbeginn [gesichert, https://www.isb.bayern.de/schularten/gymnasium/leistungserhebungen/jahrgangsstufentests/]. Für Jahrgangsstufe 5 gibt es keinen BMT.
- Frei abrufbare PDFs auf isb.bayern.de, Muster der Pfade: `.../Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/<Jahr>/BMT8_<Jahr>_Aufgaben_Gruppe_A.pdf` (auch Gruppe B, `..._Loesungen.pdf`, `..._Ergebnisse.pdf`). Gesehen: Jahrgänge 2005 bis 2025 für BMT8 und BMT10 (nicht jedes Jahr einzeln geprüft) [gesichert, Suchtreffer/PDFs, z. B. https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/BMT8_2025_Aufgaben_Gruppe_A.pdf, .../BMT10_2025_Loesungen.pdf].
- Format: 21 Bewertungseinheiten (BE), 4 Seiten, Gruppen A/B; Lösungshinweise ohne vollständige Lösungswege, mit Zuordnung zu allgemeinen mathematischen Kompetenzen K1-K6; Ergebnis-PDFs mit bayernweiten Erfolgsquoten je Teilaufgabe (BMT8 2025: bayernweiter Notendurchschnitt 3,75; BMT10 2025: Erfolgsquote insgesamt 40,9 %) [gesichert, Ergebnis-PDFs]. Zusätzlich "Klassierung der Aufgaben 2005 bis 2019" nach Kompetenzen [gesichert, https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/Lehrerinformation/klassierung_der_aufgaben_der_bayerischen_mathematik_tests.pdf].
- Nutzungsbedingungen für diese PDFs: **nicht gefunden**. Die ISB-Seiten tragen nur "© 2026 Staatsinstitut für Schulqualität und Bildungsforschung" [gesichert]. Die allgemeine Nutzungsordnung von LehrplanPLUS gilt für jene Website, nicht ausdrücklich für diese PDFs.
- Wert für das Projekt: Der **Erfolgsquoten-Datensatz** ist ein realer Schwierigkeitsmaßstab (welche Aufgabentypen wie viel Prozent der Bayern lösen), faktische Zahlen/Statistik, nicht die Aufgabentexte.

### B3 Jahrgangsstufentests Realschule
- Realschule: Jahrgangsstufentests in Jgst 6, 7, 8 zu Schuljahresbeginn; Mathe in zwei dieser Stufen (gesehen: 6 und 8, Jgst 8 getrennt für Wahlpflichtfächergruppe I und II/III); 45 Minuten; 21 Punkte; Note; Aufgaben, Lösungen und Ergebnisse früherer Jahre sind online beim ISB [gesichert, https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Allgemeine_Infos/informationen_zu_den_jahrgangsstufentests.pdf; PDFs z. B. .../Mathematik/2025/2025_JT_Mathematik_6_Angabe.pdf, 2025_JT_Mathematik_8_I_Loesung.pdf].
- Bewertungsmaßstab (Beispiel JT 8 2020): 21-17 Punkte = Note 1, 16-14 = 2, 13-11 = 3, 10-8 = 4, 7-5 = 5, 4-0 = 6 [gesichert, 2020_jt_mathe_8_i_loesung.pdf].
- Hinweis in einem Lösungs-PDF: "Abbildung urheberrechtlich geschützt" (2019 JT 8), d. h. einzelne Bilder haben Drittrechte [gesichert].
- Nutzungsbedingungen: **nicht gefunden**.

### B4 Probeunterricht Gymnasium (Übertritt nach Klasse 4)
- Mathe-Aufgaben und Lösungshinweise (Tag 1 und Tag 2) als PDF für 2015 bis 2023 frei auf isb.bayern.de [gesichert, z. B. https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Probeunterricht/Mathematik/2023/mathematik_aufgaben_erster_tag_2023.pdf]. Niveau: Ende Grundschule, daher nur für die Brücke zu Klasse 5 relevant. Nutzungsbedingungen: **nicht gefunden**.

### B5 Abschlussprüfung Realschule, Prüfungsarchiv mebis/ByCS
- Das Ministerium sagt: Prüfungsaufgaben der Vorjahre stehen im **Prüfungsarchiv von mebis/ByCS** digital; Lehrkräfte haben Zugriff im passwortgeschützten internen Bereich auf alle Aufgaben und Korrekturhinweise [gesichert, https://www.bayern.landtag.de/www/ElanTextAblage_WP19/Drucksachen/Basisdrucksachen/0000002000/0000002318_033.pdf]. Ein ISB-PDF schreibt: Material steht "Lehrkräften im ByCS-Prüfungsarchiv zu unterrichtlichen Zwecken zur Verfügung" [Sekundär, Suchtreffer 2025_JT6_Deutsch_Text.pdf]. Die SPD forderte 2024 ein kostenloses Archiv für alle Schüler, was auf eingeschränkten Zugang hindeutet [Sekundär, news4teachers.de].
- Antwort auf die Frage "für Privatpersonen zugänglich?": **nein bzw. nicht bestätigt**; Zugang nur mit Schul-/Lehrerkonto. Einen Teil der Abschlussprüfungen zeigt eine Schulinformation als vorab/nachträglich über die Schule (FragDenStaat-Dokument, unvollständig gelesen). Frei öffentliche RS-Abschlussprüfung Mathematik Bayern auf isb.bayern.de: **nicht gefunden**.
- Dynamisches-Mathematiksystem-Überblick (Abschlussprüfung 2025 Mathematik I) beim ISB zeigt, dass Grafikrechner (Bayern) in Prüfungen erlaubt ist [gesichert, ISB-PDF]; relevant für den "Papier, ohne Hilfe"-Maßstab: Prüfungen können Hilfsmittel erlauben, Aufgaben der Jahrgangsstufentests sind teils hilfsmittelfrei.

### B6 Grundwissenskataloge, ISB-Materialien allgemein
- Grundwissen Mathematik Gymnasium und ISB-Handreichungen: **nicht geprüft** (keine Seite abgerufen). Bitte als offene Prüfung behandeln.
- Umsetzungshinweise Einführungsklasse (isb.bayern.de/.../Einfuehrungsklasse/mathematik.pdf) existieren, aber nicht relevant für Klasse 5/8.

### B7 VERA (IQB)
- IQB stellt VERA-8-Mathematik-Aufgaben und didaktische Handreichungen (je Jahr, Modul B u. a.) online (https://www.iqb.hu-berlin.de/de/schule/aufgaben/seki/vera-8-mathematik/) [gesichert, Suchtreffer/Handreichungen 2020-2026]. Bayern nimmt an VERA-8 teil (Mittelschule-Handreichung des LAS) [Sekundär].
- Nutzungsbedingungen: eine ältere Handreichung (2009) sagt, die Aufgaben enthalten teils urheberrechtlich geschütztes Material (Fotos, Grafiken, Texte); Haftungsausschluss in aktuellen PDFs [gesichert, Auszüge]. Sachsen-Anhalt gibt VERA-Auswertungen unter CC BY-NC-SA 3.0 weiter [gesichert, bildung-lsa.de, vera14 Auswertung]. Aktuelle IQB-Lizenzbedingungen: **nicht gefunden**.
- Bezug: nationale Bildungsstandards, nicht LehrplanPLUS; ergänzend nützlich für Kompetenzbereiche (Leitideen, K1-K6).

### B8 IB MYP
- Subject Guides und Publikationen: © IBO; Weitergabe/Vervielfältigung nur mit schriftlicher Erlaubnis oder wie gesetzlich zulässig; kommerzielle Nutzung durch Dritte (inkl. Plattformen) verboten ohne Lizenz (copyright@ibo.org) [gesichert, Auszüge aus MYP Mathematics Guide, z. B. https://wottonhouseschool.co.uk/...; Scribd-Kopie]. Spezimen-eAssessment nur über das Resource Centre der Schulen (OCC) [Sekundär, IB FAQ]. Frei nutzbares MYP-Aufgabenmaterial: **nicht gefunden**. [Meinung] nur Kriterien (A-D) als eigene Paraphrase nutzen, nichts übernehmen.

---

## C) Kataloge typischer Fehler/Fehlvorstellungen

| Quelle | Inhalt | Zugang/Lizenz | Bewertung |
|---|---|---|---|
| **Mathe sicher können (MSK)**, DZLM Dortmund/Berlin (Prediger, Selter u. a.) | Diagnose- und Fördermaterial zu Verstehensgrundlagen (Zahl, Brüche, Prozente, Dezimalzahlen u. a.), Klassen 3-7 laut Broschüre; Standortbestimmungen, "Online-Check" mit 45 Kurzdiagnose-Tests | Alles als OER frei zugänglich unter mathe-sicher-koennen.dzlm.de; Bausteine **CC BY-NC-SA 4.0** (Word/PDF) [gesichert, https://mathe-sicher-koennen.dzlm.de/mskfiles/uploads/Dokumente/msk_df_b1abc-brueche-prozente-verstehen_260119.docx; https://www.leibniz-ipn.de/de/forschen/publikationen/mathe-sicher-konnen-online-check-45-digitale-kurzdiagnose-tests] | Beste deutschsprachige freie Quelle für Klasse 5-7; NC und SA beachten |
| Padberg, Prediger (Fachbücher), Malle (Algebra-Fehler) | Fachdidaktische Fehleranalysen Sek I | Bücher/Aufsätze, nicht frei; offener Volltext: **nicht gefunden** | nur als Literatur zum Selbstlesen, nichts übernehmen |
| **Eedi NeurIPS 2020 Education Challenge** | über 20 Mio. Schülerantworten auf Multiple-Choice-Diagnosefragen (UK), Fragemetadaten; Fehlvorstellungen sind dort **nicht** vergeben/verknüpft [gesichert, https://arxiv.org/abs/2007.12061 (Abstract/Text)] | Lizenz **CC BY-NC-ND 4.0** (keine Bearbeitung weitergeben) [gesichert, https://eedi.com/projects/neurips-education-challenge]; Download über die Seite | Für Forschung/Auswertung okay, **nicht** als Quelle zur Übernahme in öffentliches Repo (ND) |
| **Eedi "Mining Misconceptions in Mathematics"** (Kaggle 2024) | 1.857 Fragen, je vier Optionen, falsche Optionen mit Fehlvorstellungs-Label; Liste von Fehlvorstellungen, englisch [Sekundär, arXiv 2510.11502] | Lizenz der Kaggle-Daten: **nicht gefunden**. Ein Preprint nennt für die Fehlvorstellungs-Graphdatei "CC BY 4.0, Version 1.0" laut Eedi-Datenseite, ungeprüft [Sekundär, arXiv 2611.14557] | Potenziell wertvollste Liste von Fehlvorstellungs-Formulierungen; Lizenz vor Nutzung selbst prüfen (Kaggle-Regeln, Account nötig, daher nicht von mir geprüft) |
| **MAP Charting Student Math Misunderstandings** (MIME-Datensatz, Vanderbilt/Learning Agency) | über 52.000 Schülererklärungen zu 15 Fragen, Klassen 4-8, Expertenlabels [gesichert, https://aclanthology.org/2025.aimecon-wip.3.pdf]; 2026 EDM-Preis für den Datensatz | Lizenz: **nicht gefunden** | nur Forschungsbezug; wenig Umfang an Aufgaben |
| **Mathematics Assessment Project (MARS, Shell Centre)** | Classroom Challenges, Lessons zum Aufdecken von Fehlvorstellungen, englisch | Seite nennt "© 2007-2015 MARS, University of Nottingham", **keine Lizenzaussage** [gesichert, https://map.mathshell.org/background.php]. Offen oder nicht: **nicht gefunden** | nur als Ideengeber lesen |
| **NCETM** (UK) "Misconceptions with the Key Objectives" | Tabellen zu Fehlvorstellungen Primary-Niveau (Rechnen, Brüche, Fläche) | frei abrufbares Dokument (ncetm.org.uk/media/cocnx0it/misconceptions-with-the-key-objectives2.doc); Lizenz: **nicht geprüft** | vor allem Primarstufe |
| **Centre for Innovation in Mathematics Teaching** (stem.org.uk) "Mathematical Misconceptions" | acht Ressourcen (negative Zahlen, Division durch Bruch, Dezimalmultiplikation, Runden) | Zugang über STEM Learning; Lizenz **nicht geprüft** | Ideengeber |
| Victoria (AUS) "Common misunderstandings" (education.vic.gov.au) | Hinweisseite zu Fehlern/Fehlvorstellungen | Lizenz nicht geprüft | Hintergrund |

[Meinung] Für die Aufgabe "Fehlvorstellungen in der App erfassen" ist der rechtlich sauberste Weg: eigene Fehlertyp-Liste (kurze Stichworte wie "addiert statt zu multiplizieren", "Vorzeichen vergessen"), inspiriert von MSK und Eedi-Beschreibungen, nicht deren Texte kopieren.

---

## D) Schnittstellen und Werkzeuge (Browser, ohne Framework, offline-fähig)

| Baustein | Lizenz | Kosten | Eignung (Web-App ohne Framework, offline) |
|---|---|---|---|
| **CortexJS Compute Engine** (`@cortex-js/compute-engine`) | MIT [gesichert, https://github.com/cortex-js/compute-engine] | frei | Parsen LaTeX zu MathJSON, `simplify`, `solve`, `expand`, Auswertung; Repo zeigt npm/ESM-Nutzung, UMD/CDN **nicht belegt** [gesichert]. Offline: kein Netz nötig, sobald Datei lokal liegt [Annahme] |
| **MathLive** (`<math-field>`) | MIT [gesichert, https://github.com/arnog/mathlive] | frei | Formeleingabe mit virtueller Tastatur, LaTeX, MathJSON; Einbindung per Script-Tag von jsDelivr ohne Framework; Schriftarten werden zur Laufzeit geladen, **Offline-Bündelung nicht im README erklärt** [gesichert] (Annahme: Dateien lokal hosten möglich) |
| **math.js** | Apache 2.0 (gebündeltes CSparse unter LGPL-2.1+) [gesichert, https://github.com/josdejong/mathjs] | frei | Auswertung, Matrizen, Einheiten; Ableitung vorhanden (`derivative`), `simplify` im README nicht erwähnt; Browser-Bundle über CDN-Download |
| **Algebrite** | MIT [gesichert, javascriptweekly-Seite/Repo davidedc/algebrite] | frei | Eigenständige CAS in JS, "self-contained, doesn't need connection to servers"; Faktorisieren, Integrieren; geeignet für Umformungsprüfung |
| **Nerdamer** | MIT [Sekundär, sourceforge-Mirror] | frei | kleine symbolische Bibliothek, rein JS, kein Server; Funktionsumfang für Gleichungen/Faktorisieren **nicht geprüft** |
| **SymPy via Pyodide** | SymPy modifizierte BSD [Sekundär, Wikipedia]; Pyodide MPL-2.0 [Sekundär, SymPy-Beta-Repo-Hinweis] | frei | Mächtig, läuft komplett im Browser (Beispiel: "SymPy Beta" ohne Backend, https://github.com/eagleoflqj/sympy_beta, dort AGPL für das Projekt); Download-Größe/Ladezeit nicht gemessen [Annahme: groß, mehrere zehn MB] |
| **Giac/Xcas** (giac.js) | GPL3, kommerzielle Dual-Lizenz auf Anfrage [gesichert, https://xcas.univ-grenoble-alpes.fr/en] | frei | "Xcas offline in your browser"; giac.js etwa 12 MB, einmal geladen [gesichert, https://www-fourier.univ-grenoble-alpes.fr/~parisse/giac/xcasenie.html]. GPL-Ansteckung für das Gesamtprojekt prüfen (Rechtsfrage) |
| **MyScript iink** (Handschrift) | proprietär (SDK-Lizenz) | SDK-Pricing laut Anbieter nicht offen; ein Drittbericht nennt Entwickler-Gratisstufe bis 25 Geräte [Sekundär, maqtoob.com, ungeprüft]; Cloud-Erkennung mit eigener Preisliste (https://developer.myscript.com/pricing) | erkennt 250 Mathe-Symbole [gesichert, https://www.myscript.com/education]; Web-Variante nutzt laut Forumstext Cloud-Erkennung [Sekundär, developer-support.myscript.com]; **Offline im Web nicht belegt** |
| **Mathpix** | proprietär | Convert-API ab 0,002 USD pro Anfrage; Snip hat kleine Gratisstufe [gesichert, https://mathpix.com/docs/convert/billing; https://mathpix.com/pricing/snip] | Cloud-OCR, **nicht offline**; Nutzungsbedingungen nicht gelesen |
| Bewertungs-APIs | | | **nicht gefunden** (kein sinnvoller freier Dienst für Umformungsprüfung identifiziert) |

[Meinung] Für den Bedarf "Umformung prüfen" braucht man: (1) Eingabe (MathLive), (2) Parsen (Compute Engine), (3) Äquivalenzprüfung. Die robusteste Äquivalenzprüfung ist [Meinung/Annahme] ein eigener Test durch Einsetzen mehrerer Zufallswerte plus Definitionsbereich-Check, ergänzt durch Struktur-Prüfung (z. B. "vollständig gekürzt/faktorisiert"); das braucht keine Cloud.

---

## E) Rechtlicher Rahmen Deutschland (nur Wiedergabe, keine Rechtsberatung)

1. **CC BY**: Nutzung, Bearbeitung, Weitergabe auch kommerziell, wenn Urheber genannt, Lizenz verlinkt, Änderungen angegeben (Formulierung "Namensnennung" laut ZUM/CC-Deed).
2. **CC BY-SA**: wie BY, aber Bearbeitungen/darauf aufbauende Werke müssen unter derselben oder kompatibler Lizenz weitergegeben werden [gesichert für Serlo und Mathe für Nicht-Freaks, Lizenztexte]. Folge für die App: Wenn Serlo-Text in eigene Inhalte "eingearbeitet" wird, müssten diese Inhalte (nicht automatisch der Programmcode) unter CC BY-SA stehen [Annahme; Abgrenzung Inhalt/Code ist eine Rechtsfrage].
3. **CC BY-NC / BY-NC-SA**: keine kommerzielle Nutzung [gesichert, https://creativecommons.org/licenses/by-nc-sa/3.0/de/]. Was "kommerziell" ist, definieren Anbieter unterschiedlich; Khan nennt: nicht direkt auf Umsatz/Gewinn gerichtet; Werbung zählt als kommerziell [gesichert, Khan-Supportseite]. [Annahme] Eine private, werbefreie, gratis App ohne Einnahmen ist wahrscheinlich nicht kommerziell; ein **öffentliches Repo** bedeutet aber Weitergabe an alle, auch an kommerzielle Nutzer. Bei NC-SA muss der Inhalt im Repo selbst wieder unter NC-SA stehen.
4. **CC BY-NC-ND** (Eedi 2020): keine Bearbeitung weitergeben; abgeleitete Datenbanken, Übersetzungen oder Auszüge in ein öffentliches Repo wären damit [Annahme] nicht erlaubt.
5. **Amtliche Werke § 5 UrhG** [gesichert, https://www.gesetze-im-internet.de/urhg/__5.html]: Gesetze, Verordnungen, Erlasse, Bekanntmachungen, Gerichtsentscheidungen (Abs. 1) und "sonstige amtliche Werke", die im amtlichen Interesse zur allgemeinen Information veröffentlicht werden (Abs. 2), sind nicht geschützt; bei Abs. 2 gelten Änderungsverbot und Quellenangabe (§§ 62, 63). Private Normwerke bleiben geschützt (Abs. 3).
   - **Lehrpläne**: Das ISB erklärt selbst, die Lehrplantexte unterlägen nicht dem Urheberrecht [gesichert, LehrplanPLUS-Nutzungsbedingungen]; welche Rechtsgrundlage das ISB meint, nennt die Seite nicht.
   - **Prüfungsaufgaben (BMT, Jahrgangsstufentests, Probeunterricht, VERA)**: ob diese "amtliche Werke zur allgemeinen Information" sind, ist **nicht geklärt**. Die ISB-PDFs tragen Copyright-Vermerk, enthalten teils Drittbilder, und die Aufgaben sind Leistungserhebungen, keine Informationsveröffentlichung [Annahme]. Auf der sicheren Seite: Aufgaben als Muster nutzen, nicht abdrucken.
6. **Schulbuch- und Verlagsaufgaben**: urheberrechtlich geschützt (Texte, Grafiken; bei sehr kurzen Rechenaufgaben kann die Schöpfungshöhe fehlen, Einzelfrage) [Annahme]. Die Schulschranken (§ 60a UrhG u. a.) gelten für Unterricht an Bildungseinrichtungen und sind für eine private App mit öffentlichem Repo [Annahme] kaum einschlägig; nicht geprüft.
7. **Automatisierter Abruf**: Khan: automatisierte Systeme laut AGB-Auszug verboten [Sekundär]; LehrplanPLUS, Serlo-Terms: keine Aussage [gesichert]; GeoGebra, CK-12, Mathpix, MyScript, mebis: AGB **nicht gelesen**. Zusätzlich kann Datenbankschutz (§ 87a ff. UrhG) und das Text-und-Data-Mining-Recht (§ 44b UrhG) eine Rolle spielen [Annahme, nicht geprüft].
8. **Idee/Aufgabentyp vs. Text**: Urheberrecht schützt die konkrete Ausdrucksform, nicht Ideen, Methoden, mathematische Sachverhalte oder reine Aufgabentypen [Annahme, allgemeiner Grundsatz, keine Quelle abgerufen]. Praktische Konsequenz: Aufgabentyp "Gleichung mit Klammer lösen, ganzzahlige Lösung" selbst programmatisch generieren (die App tut das schon) ist eine andere Sache als einen BMT-Aufgabentext, eine Abbildung oder die Datenreihe eines Diagramms zu kopieren. Grauzone: sehr eng nachgebaute Aufgaben (gleiche Zahlen, gleicher Kontext) [Meinung: vermeiden].

---

## (a) Übersichtstabelle

| Quelle | Was übernehmbar | Lizenz/Bedingung | Zugangsweg | Aufwand |
|---|---|---|---|---|
| Serlo | Erklärtexte, Aufgaben, Metadaten; Verlinkung | CC BY-SA 4.0, Einzel-Ausnahmen markiert | GraphQL `https://api.serlo.org/graphql`; Metadata API | mittel (Format parsen, Attribution speichern) |
| Mathe sicher können | Diagnoseaufgaben, Förderideen, Fehlerkategorien (Kl. 3-7) | CC BY-NC-SA 4.0 | Downloads mathe-sicher-koennen.dzlm.de | mittel |
| Eedi (Kaggle, Misconceptions) | Liste von Fehlvorstellungen (Idee) | Lizenz Kaggle unklar; Graph evtl. CC BY 4.0 | Kaggle (Account) | gering bis mittel; Lizenz klären |
| Eedi NeurIPS 2020 | nichts weitergeben | CC BY-NC-ND 4.0 | Eedi-Seite | nur Analyse |
| LehrplanPLUS | Kompetenzerwartungen als Struktur; Originaltexte frei | Lehrplantext nicht urheberrechtlich geschützt; Rest nicht kommerziell, Quelle nennen | HTML/PDF, keine API | mittel (selbst strukturieren) |
| BMT8/10 (Gym), JT 6/8 (RS), Probeunterricht | als **Maßstab**: Format, BE-Verteilung, Erfolgsquoten, Themenmix; Aufgabentexte nicht kopieren | © ISB, Bedingungen für PDFs nicht gefunden | freie PDFs auf isb.bayern.de | gering (Lesen), mittel (Auswerten) |
| VERA-8 (IQB) | Kompetenzmuster, Aufgabenformate | Bedingungen nicht gefunden; Drittrechte | iqb.hu-berlin.de | gering |
| mebis/ByCS-Prüfungsarchiv | nichts (kein freier Zugang bestätigt) | nur Lehrkräfte-Zugriff | Login | nicht machbar |
| IB MYP | nur eigene Paraphrase der Kriterien | © IBO, Weitergabe nur mit Erlaubnis | Schul-Portal | nicht machbar |
| Khan Academy | nichts übernehmen/scrapen; verlinken | CC BY-NC-SA unklar; AGB gegen Automatisierung | keine aktive API | n. a. |
| OpenStax | Konzept/Aufgaben (Englisch) | CC BY 4.0 (Algebra 1: BY-NC-SA) | Web/PDF | hoch (Übersetzung, andere Lehrpläne) |
| Illustrative Mathematics | Aufgabenideen (Englisch) | CC BY 4.0 (2019-21), BY-NC 4.0 (v.360) | Kendall Hunt/AccessIM | hoch |
| ZUM / Mathe für Nicht-Freaks | Erklärtexte, H5P-Übungen | CC BY-SA (3.0/4.0) | MediaWiki, apps.zum.de | mittel |
| MUNDO / WLO | nur Fundstellen; Lizenz je Treffer | uneinheitlich | Portal, edu-sharing (API-Doku nicht gefunden) | mittel |
| GeoGebra | Einbettung Applets/Materialien | NC, GeoGebra-Lizenz | Website/Embed | gering bis mittel |
| CK-12, Mathigon/Polypad, LearningApps | nicht empfohlen | Sonderlizenzen/NC | n. a. | n. a. |
| MathLive | Formeleingabe | MIT | CDN/npm | gering |
| Compute Engine | Parsen/Vereinfachen/Lösen | MIT | npm | gering bis mittel |
| math.js / Algebrite / Nerdamer | Zusatz-CAS | Apache 2.0 / MIT / MIT | npm/Script | gering |
| SymPy-Pyodide / Giac | schwere Alternative | BSD+MPL / GPL3 | WASM | hoch |
| MyScript / Mathpix | Handschrift | proprietär, kostenpflichtig | Cloud/SDK | hoch, nicht offline |

---

## (b) Die fünf nützlichsten Quellen je Zweck [Meinung auf Grundlage der Funde]

**Erklärungen**: 1. Serlo (CC BY-SA, API). 2. Mathe sicher können (für Grundlagenlücken, NC-SA). 3. ZUM-Unterrichten/Mathematik-digital (CC BY-SA, Qualität schwankend). 4. IM 6-8 bzw. OpenStax (Englisch, nur Struktur/Beispiele). 5. GeoGebra-Materialien (als Einbettung, NC).

**Aufgabenmuster**: 1. BMT8/BMT10 (Muster lesen). 2. Realschul-Jahrgangsstufentests 6/8. 3. Serlo-Aufgaben (offen lizenziert, direkt übernehmbar). 4. SMART Bayreuth (Bayern, nur private/unterrichtliche Nutzung; keine Weitergabe laut Seite) . 5. VERA-8 (Formate, Kompetenzbereiche).

**Fehlvorstellungen**: 1. Mathe sicher können. 2. Eedi Mining Misconceptions (Liste, Lizenz erst klären). 3. NCETM-Misconceptions-Dokument. 4. MAP/Shell Centre (Ideen). 5. MIME/MAP-Charting-Datensatz (Forschung, kleinere Reichweite).

**Prüfungs-Maßstab Bayern**: 1. BMT8/BMT10 mit Ergebnis-PDFs (Erfolgsquoten) und Lösungshinweisen. 2. LehrplanPLUS Fachlehrplan und Jahrgangsstufenprofile. 3. Jahrgangsstufentests Realschule (Notenschlüssel 21 Punkte, 45 Minuten). 4. Probeunterricht (Übergang Klasse 4 nach 5). 5. VERA-8. Hinweis: Reale Schulaufgaben in der Schule sind länger (45-Minuten-Tests wie BMT/JT sind nur ein Teil); frei verfügbare Schulaufgaben-Sammlungen für Bayern habe ich **nicht** gefunden. Das Prüfungsarchiv der Abschlussprüfung ist nur für Lehrkräfte.

---

## (c) Empfehlung: einbinden statt selbst bauen [Meinung]

- **MathLive** für Formeleingabe einbinden (MIT, ohne Framework per Script-Tag, Fonts lokal bündeln und Offline testen).
- **CortexJS Compute Engine** für Parsen/Vereinfachen/Lösen einbinden; **Äquivalenzprüfung** (Zufallswerte, Definitionsbereich, Normalform) selbst als kleine Funktion schreiben, weil sie genau auf die Aufgabenarten zugeschnitten sein muss. Zweite Meinung zur Absicherung: math.js oder Algebrite als Gegenprüfung.
- **Kein** SymPy-Pyodide/Giac, solange nicht ein konkreter Fall (z. B. Gleichungssysteme, Ungleichungen, Stochastik) die kleinen Bibliotheken überfordert; GPL (Giac) vermeiden.
- **Handschrifterkennung nicht einbauen**: MyScript/Mathpix sind Cloud/kostenpflichtig, widersprechen "ohne Netz"; die Prüfung findet auf Papier statt, die App muss nur Ergebnisse/Zwischenschritte per Tastatur prüfen. [Meinung]
- **Serlo** als Inhaltsquelle über GraphQL/Metadata API anbinden: Erklärungen und Übungen zu den eigenen Themen-IDs zuordnen und lokal speichern (Offline!). Pro Inhalt Lizenz-Feld, Autoren, Quell-URL und Abrufdatum mitspeichern. Eigene Aufgaben weiter programmatisch erzeugen.
- **LehrplanPLUS** nicht scrapen, sondern einmalig manuell die Kompetenzerwartungen in eine eigene Themenstruktur überführen (mit Quellenangabe), Rückfrage beim ISB zur Automatisierung wäre sauber.
- **BMT/JT-PDFs**: lokal lesen, daraus eine eigene Kennzahlentabelle ableiten (Themenanteil, BE, Erfolgsquote); die PDFs nicht ins öffentliche Repo legen.

---

## (d) Offene Rechtsfragen für eine Fachperson

1. Gelten ISB-Prüfungsaufgaben (BMT, JT, Probeunterricht) als amtliche Werke nach § 5 Abs. 2 UrhG, oder sind sie geschützt? Sind Auszüge/Abbildungen als Beispiele in einem öffentlichen Repo zulässig?
2. Was genau umfasst "Originaltexte der Lehrpläne" in den LehrplanPLUS-Nutzungsbedingungen (kommerziell frei) gegenüber dem restlichen, nur nicht kommerziell nutzbaren Seiteninhalt? Ist automatisiertes Abrufen/Strukturieren gedeckt?
3. Ist eine private, werbefreie App mit **öffentlichem** Repo "nicht kommerziell" im Sinn von CC BY-NC(-SA) (MSK, GeoGebra, IM v.360)? Wie wirkt die öffentliche Weitergabe an Dritte?
4. Bei CC BY-SA (Serlo, ZUM): Reicht eine Lizenzdatei für den Inhaltsordner, oder zieht Share-Alike den Programmcode mit? Wie sind Inhalte in der Datenbank zu kennzeichnen?
5. Zulässigkeit von Datenbankabruf (§ 87a UrhG) und Text-/Data-Mining (§ 44b UrhG) bei Serlo-GraphQL und beim ISB.
6. Eedi (ND): darf man Fehlvorstellungs-Beschreibungen als eigene Stichworte neu formulieren und veröffentlichen?
7. Lizenzen der Kaggle-Daten (Eedi, MAP Charting) und der Compute-Engine/MathLive-Schriften, wenn Dateien offline gebündelt werden.
8. Datenschutz bei Kinderkonten in externen Diensten (Khan, mebis), falls später genutzt (nur angerissen).

---

## Was ich nicht prüfen konnte

- Ob ISB-PDFs (BMT, JT, Probeunterricht) eigene Nutzungsbedingungen haben (nur Copyright-Vermerk gefunden); das Prüfungsarchiv selbst (Login) und ein öffentliches RS-Abschlussprüfungsarchiv.
- Vollständigkeit der BMT-Jahrgänge (gesehen 2005-2025 in Suchtreffern, nicht jedes Jahr abgerufen); ISB-Grundwissenskataloge.
- Kaggle-Daten-Lizenzen (Eedi 2024, MAP-Charting), MAP/Shell-Centre-Lizenz, NCETM-Lizenz.
- Serlo: Volltext-Abruf per `uuid` und Anzahl Mathe-Aufgaben Klasse 5-10; WLO/MUNDO/ZUM-API-Dokumentation.
- Aktuelle Khan-Übungslizenz und -AGB im Original (nur Support-Seite und Sekundärauszug); AGB von GeoGebra, CK-12, Mathpix, MyScript.
- Offline-Verhalten und Bundle-Größen von MathLive, Compute Engine, Nerdamer, Pyodide; UMD/CDN-Builds der Compute Engine.
- IQB-Nutzungsbedingungen für VERA; IB-Specimen-Material.
