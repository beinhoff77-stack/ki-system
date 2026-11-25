# Tiefen-Analyst 10: Erklären und Aufgabenformen (Mathe-App, Klasse 5 und 8, Maßstab Gymnasium Bayern)

Abruf aller Quellen: 25.11.2026. Nur Websuche, Seitenabruf und npm-Paketdaten (Größen selbst gemessen). Nichts angemeldet, gekauft oder abgesendet. Keine persönlichen Daten in Suchanfragen.
Kennzeichnung: **[G]** gesichert (Quelle verlinkt, auf der Seite oder im Suchausschnitt gelesen), **[A]** Annahme oder eigene Ableitung, **[M]** Meinung/Bewertung. „Nicht gefunden“ heißt: in dieser Recherche nicht auffindbar.
Vorher gelesen: tief-1, tief-4, tief-5, tief-6, tief-7 (und sucher-c für Lizenzen). Was dort steht, wiederhole ich nicht. Ich verweise nur darauf (Bar-Model/Bild vor Symbol: tief-6; Kontrollzahlen, erste falsche Zeile, MathLive: tief-4; BMT-Anteile: tief-5; Sparx-Bookwork-Check: tief-7).
Alle Aufgaben- und Erklärbeispiele habe ich selbst gebaut und nachgerechnet. Nichts davon ist von Plattformen oder aus Büchern übernommen.

---

## 0. Kurzfassung (12 Punkte)

1. [G] Die Besten erklären mit **kleinen Schritten, in denen das Kind etwas tut, bevor ein neuer Schritt kommt**. Mathigon zeigt den nächsten Schritt erst nach einer Handlung. Brilliant stellt eine Frage vor dem Verfahren und fängt mit dem einfachsten Fall an. Desmos zeigt, was die Antwort bedeutet, statt nur „richtig/falsch“.
2. [G] Die Forschung stützt **Bild + Wort nah beieinander, nichts Überflüssiges, Gliederung in Abschnitte und Vorab-Begriffe**. Die Mediane nach Mayer liegen bei d ≈ 0,4–1,1. Animationen schlagen Standbilder nur leicht (g ≈ 0,23–0,37). Klar im Vorteil sind sie nur, wenn die *Veränderung selbst* gelernt werden soll.
3. [G] Videos: Ein Video *zusätzlich* zu anderem Material hilft deutlich. Ein Video *statt* anderem hilft nur wenig (Hochschule). Unter 6 Minuten werden Videos häufiger zu Ende gesehen (Guo). Ob Kinder dabei mehr lernen, wurde dort nicht gemessen. Klicks und Likes auf YouTube sagen nichts über die Erklärqualität.
4. [G] Virtuelle Manipulative haben im Mittel eine mäßige Wirkung (≈ 0,34). „Concreteness fading“ (konkret → bildlich → Symbol, *ausdrücklich verbunden*) ist gut begründet, aber nicht für jedes Thema belegt.
5. [G] DragonBox ist kein Selbstläufer. Ein Tutor mit echten Gleichungen schlug DragonBox im Papiertest (Long & Aleven 2017). In einer großen Studie half DragonBox gegenüber Papierarbeit (≈ 0,27 SD). [M] Für die App heißt das: Spielregeln nur als Brücke nutzen, dann schnell zum Symbol.
6. [A] Die heutige Erklärung (Einstieg – Regel – 3 Bildschritte – Fehler – Wörter) ist **„erst lesen, dann tun“**. Die Vorbilder machen es umgekehrt. Vermutlich ist das der Hauptgrund, warum die Funktionen-Erklärung nicht verstanden wurde.
7. [M] Die Muster in Lieferung 1: **6–9 Bildschirme (Kl. 8 eher 2 Einheiten), 6–12 Minuten, höchstens etwa 35 Wörter pro Bildschirm, 10–18 kurze Eingaben des Kindes (je 1 Tipp oder 1 Zahl)**. Die Regel kommt erst nach dem Tun. Dazu gehören ein Fehlerbeispiel und am Ende 3 Prüfaufgaben, bei denen die Hilfe abnimmt.
8. [M] Die zwölf nächsten Aufgabenformen schließen die Lücken zum BMT (Begründen, Zeichnen, Daten, Tabellenkalkulation). Ganz oben stehen **Gegenbeispiel/Beispiel nennen (Einsetzen), Punkte im Gitter setzen, Daten/Diagramm ablesen und ergänzen, Tabellenkalkulations-Formel**. Alle liefern einen einfachen Wert mit klarer Prüfregel.
9. [G] Eingabe am Handy: Die iOS-Dezimaltastatur (`inputmode="decimal"`) hat **kein Minuszeichen**. Gute Systeme werten Formatfehler **nicht als falsch** (STACK: erst „gültig?“, dann bewerten; Pearson korrigiert eindeutige Formate). [M] Deshalb braucht die App eine eigene Tastenleiste (±, Komma, Bruch, Potenz).
10. [G] Gute Übungsaufgaben: pro Aufgabe eine Sache, jeder falsche Auswahlwert steht für einen bestimmten Fehler (Eedi), richtig darf man nicht mit Fehlvorstellung werden. Dazu kommen Folgen mit kontrollierter Variation und gemischtes Üben (Rohrer: d = 0,83). Sparx pflegt rund 50.000 Fragen mit 4 Stufen pro Thema und etwa 3 Varianten pro Frage.
11. [M] Selbst bauen (SVG): Gitterpunkte, Zahlenstrahl, Tippen, Ordnen, Balken, Tabelle. Einbinden nur bei Bedarf: JSXGraph (MIT/LGPL, 259 KB gzip) für Geometrie, MathLive (MIT, 230 KB gzip + Schriften) für Terme. Weglassen: Desmos-API, GeoGebra-Einbettung (Lizenz/online), Perseus und Mafs (React), H5P (prüft im Browser, kaum Mathe).
12. [M] Nur auf Papier gehen echtes Konstruieren mit Zirkel/Geodreieck, längere Begründungen und vollständige Rechenwege. Die App stellt die Aufgabe und prüft über **messbare Kontrollwerte** (z. B. „miss Seite c: … cm ± 0,2“). Dazu kommen ein Bewertungsraster für den Elternteil und eine wöchentliche Papierrunde.

---

## A) ERKLÄREN – Vorbilder und Belege

### A1. Vorbilder im Einzelnen

| Vorbild | Aufbau einer Erklärung | Länge / Textmenge | Interaktion | Sofort-Prüfung | Quelle |
|---|---|---|---|---|---|
| **Brilliant** | [G] Abschnitte mit je **einer** handhabbaren Idee. Es beginnt mit dem einfachsten nützlichen Fall, dann wird es schrittweise schwerer. Oft kommt **eine Frage vor dem Verfahren**, damit die Erklärung einen Zweck hat. Danach Übung ohne Stütze, mit anderen Oberflächen, gemischt, mit Wiederkehr. Am Ende jeder Lektion ein „Skill Check“. | [G] Werbung mit „15 Minuten am Tag“. Laut Selbstbeschreibung „keine Videos, alles interaktiv“. Länge einer Lektion und Wortzahl: **nicht angegeben**. | [G] Ziehbare Diagramme, verstellbare Graphen, Schätzen, Strategie wählen. Bei falscher Antwort bleibt der eigene Ansatz sichtbar, damit das Kind ihn überarbeiten kann. Tutor „Koji“ gibt Leitfragen, hebt Teile hervor, zerlegt in kleinere Schritte. | Jede Seite ist eine Frage. Skill Check pro Lektion, Unit Check mit Altstoff. | [How Brilliant teaches math](https://brilliant.org/resources/choosing-brilliant/how-brilliant-teaches-math/), [llms.txt](https://brilliant.org/llms.txt), [Startseite](https://next.brilliant.org) |
| **Desmos / Amplify Classroom** | [G] Gestaltungsregeln (2021): viele richtige und lehrreiche falsche Antworten zulassen; **interpretierende Rückmeldung** („so verstehen wir deine Antwort“) statt bewertender; erst ein **Bedürfnis** für das neue Werkzeug schaffen; Papier, Material und Gespräch mitnutzen. Ältere Fassung (2016, nur im Suchausschnitt): Abwechslung bei den **Tätigkeiten** (rechnen, skizzieren, Streit schlichten) und bei den **Antwortformen**; **informell vor formal**. | Keine Zahlen zu Text oder Bildschirmzahl im Leitfaden. [G] Ein Webinar empfiehlt höchstens 4 Bausteine pro Bildschirm. | [G] Bausteine: Graph, Tabelle, Skizze, Auswahl/Mehrfachauswahl, geordnete Liste, Kartensortieren, Marbleslides, Polygraph, Geometrie. | [G] Beim Kartensortieren kennt das System die Lösung, **zeigt sie dem Kind aber bewusst nicht**; die Lehrkraft sieht, welche Karte am häufigsten falsch liegt. Rückmeldestufen nach Meyer: (1) nur „falsch“; (2) freundlich falsch; (3) Fehler erklärt (oft in Fachsprache, also neue Hürde); (4) **zurückspiegeln, was gemeint war** und nachfragen. Stufe 4 ist laut Meyer oft *leichter* zu bauen. | [Guide 2021](https://blog.desmos.com/articles/desmos-guide-to-building-great-digital-math-2021/), [Blogarchiv 2016](https://blog.desmos.com/page/71/), [Meyer: Computer Feedback](https://danmeyer.substack.com/p/computer-feedback-that-helps-kids), [Meyer: Card sort](https://danmeyer.substack.com/p/what-students-lose-when-they-know?open=false), [Bausteine](https://my.amplify.com/help/en/articles/6797997-getting-started-activity-builder), [Webinar-PDF](https://ionicviper.org/system/files/Desmos%20VIPEr%20Webinar%20June%202023%20Part%201.pdf) |
| **Mathigon / Polypad** | [G] Kurse sind in **viele kleine Schritte** geteilt. Der nächste Schritt erscheint erst, wenn das Kind gehandelt hat; man kann aber „alles aufdecken“. Erzählerischer Rahmen, farbige Diagramme. Technik: Markdown-Erweiterung mit `---`-getrennten Schritten und eigenem Code pro Schritt. | [G] Ein Banner zeigt die ungefähre Kapitellänge; Zahlen: nicht gefunden. | [G] „Hunderte“ eigene interaktive Bausteine statt Auswahlaufgaben; virtueller Tutor mit Hinweisen. | Jeder Schritt ist zugleich eine Prüfung (Lücke, Ziehen, Antippen). | [FAQ](https://he.mathigon.org/faqs), [Whitepaper](https://static.mathigon.org/whitepaper.pdf), [Quellcode-Struktur](https://github.com/Mathigon/textbooks) (Lizenz: „All rights reserved“) |
| **Khan Academy** | [G] Lektion = Mischung aus Artikel, Video und Übung. Hinweise gibt es **pro Schritt** während der Aufgabe, Begründungen nach der Abgabe. Die Lernchefin schreibt, Video allein sei passiv; gelernt wird erst durch Übung. | [A] Videos meist einige Minuten (nicht gemessen). | [G] Auf dem Handy erscheint automatisch eine Mathe-Tastatur, die **nur die nötigen Symbole** zeigt. | Übung mit sofortiger Rückmeldung und Hinweisen. | [Kursaufbau](https://support.khanacademy.org/hc/tr/articles/18564282990861), [Practice-Blog](https://blog.khanacademy.org/?p=963), [DiCerbo](https://blog.khanacademy.org/how-khan-academy-helps-people-learn), [Tastatur](https://support.khanacademy.org/hc/tr/articles/202896260) |
| **PhET** | [G] „Implizites Gerüst“: Die Oberfläche lenkt durch Angebote, Einschränkungen, Hinweisreize und Rückmeldung, ohne viel Anleitungstext. Laut über 200 Schülerinterviews stört schon wenig überflüssige Information. | Kein Erklärtext im Simulator. | Ziehen, Schieberegler, Schalter. | Durch sichtbare Wirkung im Bild. | [Podolefsky/Moore/Perkins](https://arxiv.org/abs/1306.6544v3), [Adams u. a.](https://phet.colorado.edu/publications/PhET%20Interview%20Paper%20Final.pdf) |
| **Beast Academy** | [G] Pro Einheit ein Comic-„Guide“ (Erklärung durch Figuren) und ein separates Übungsbuch (von leicht bis knifflig). Online-Fassung mit Hinweisen. [G] Rezensionen: herausfordernd, für schwächere Kinder weniger geeignet. | [G] Schriftgrößen im Buch offengelegt; Seitenzahlen pro Lektion nicht gefunden. | Im Buch keine; online Aufgaben mit Hinweisen. | Übungsbuch. | [Buchüberblick](https://help.beastacademy.com/a/1792560), [beastacademy.com/books](https://beastacademy.com/books), [Rezension](https://brighterly.com/blog/beast-academy-reviews), Evaluation WestEd 2022 vorhanden ([Link](https://www.wested.org/resources/evaluation-of-beast-academy/)), **nicht gelesen** |
| **DragonBox** | [G] Gleichung als Spielfeld: Karten so verschieben, dass die „Box“ allein steht. 10 Kapitel à 20 Aufgaben. Symbole ersetzen nach und nach die Bilder. | 25 Min. pro Sitzung (Studienaufbau) | Ziehen, Antippen | Spiel lässt nur erlaubte Züge zu. | [FH2T-Projekt](https://sites.google.com/view/from-here-to-there/project-overview/dragonbox) |
| **Deutsche Erklärvideos** (simpleclub, Daniel Jung, Lehrer Schmidt, DorFuchs) | [G] Analyse von drei Videos zu einem Thema: Länge 4–6,5 Min., 162–178 Wörter/Min. **Nur simpleclub stellt am Ende eine Aufgabe.** simpleclub und Jung geben vor allem Regeln ohne Herleitung; laut Autoren vermittelt das unterschwellig eine negative Haltung zur Mathe. DorFuchs leitet am Beispiel her. | siehe links | keine | keine (außer der Schlussaufgabe) | [Wetzel u. a., BzMU 2020](https://eldorado.tu-dortmund.de/bitstream/2003/39737/1/BzMu2020_WETZEL-id357.pdf) |
| **Serlo, bettermarks-Tafelbilder, GeoGebra, Singapur, Japan** | Serlo/Lizenzen: sucher-c. bettermarks: tief-1 (Tafelbilder = gemeinsame Arbeit ohne Bewertung). Singapur/Japan (Bild vor Symbol, Lösungswege vergleichen): tief-6. 3Blue1Brown/Numberphile: **nicht vertieft** (keine belastbare Quelle zum Aufbau gesucht). | | | | |

**Warum die beliebtesten deutschen Videos beliebt sind (Befunde, nicht Wirkung):**
- [G] Nutzung: Unter Studierenden nennen 73 % „Mathe by Daniel Jung“ und 63 % simpleclub; bei Schülern (Bersch u. a. 2020) 24 % bzw. 43 % ([TU Dortmund](https://eldorado.tu-dortmund.de/server/api/core/bitstreams/7ad61b2c-658b-46a8-b7a8-cb54a512937c/content)).
- [G] Gründe (Umfrage 2019, Teilstichprobe 500 nach Notenverteilung):
  - schlechte Erklärung im Unterricht (n = 275);
  - eigenes Tempo (n = 236).
  - Größter genannter Vorteil: kurz und knapp (n = 85).
  - Größter Nachteil: man kann nicht nachfragen (n = 193).
  - Am häufigsten wird zurückgespult, dann pausiert ([Wetzel](https://eldorado.tu-dortmund.de/bitstream/2003/39737/1/BzMu2020_WETZEL-id357.pdf)).
- [G] Bayern/BW, N = 465:
  - Ob der Erklärende im Bild ist, war den meisten unwichtig.
  - **Schwächere Schüler bevorzugen Formeln, die Schritt für Schritt erscheinen** (p = 0,024) ([Weckerle, BzMU 2022](https://eldorado.tu-dortmund.de/bitstream/2003/41483/1/BzMU22_1353.pdf)).
- [G] Beliebtheit ist kein Qualitätsmaß.
  - Bei Physik-Videos zu Mechanik hingen weder Aufrufe noch Likes mit der Erklärqualität zusammen. Nur die Zahl *inhaltlicher* Kommentare tat es ([Kulgemeyer & Peters 2016](https://iopscience.iop.org/article/10.1088/0143-0807/37/6/065705); Zusammenfassung in [Bitzenbauer u. a.](https://link.springer.com/doi/10.1007/s10763-022-10351-w)).
  - Bei Quantenphysik zeigte sich ein kleiner Zusammenhang mit Likes (r = 0,37) ([Springer](https://link.springer.com/content/pdf/10.1007/s11165-023-10148-z.pdf)).
- [G] Eine Dissertation (Kiel) zum Ableitungsbegriff (44 Videos) stützt, dass Videos mit hoher fachdidaktischer Qualität beim Lernen vorzuziehen sind. Zahlen standen in der Zusammenfassung nicht ([Kiel](https://macau.uni-kiel.de/receive/macau_mods_00008852)).
- [G] **Kulgemeyers Kriterien** (eigene Worte, [PDF](https://ck.kwst.uni-bremen.de/unterrichtsgestaltung-mit-medien-auflage-2/wp-content/uploads/sites/37/2022/10/Kriterien_fuer_gute_Erklaervideos.pdf)):
  - an Vorwissen und Fehlvorstellungen anpassen; passende Sprache und passender Grad an Formalisierung;
  - Beispiele, Analogien/Modelle, Bilder;
  - Bedeutung hervorheben, direkt ansprechen;
  - Regel→Beispiel für Faktenwissen, **Beispiel→Regel für Verfahren**; Zusammenfassung;
  - keine Abschweifungen und nicht zu viele Beispiele; Sätze mit „weil“ verbinden;
  - ein neues Prinzip im Mittelpunkt, das Lernende nicht allein finden;
  - **mit einer Folgeaufgabe enden**.

### A2. Forschung (Kernzahlen)

| Thema | Befund | Quelle | Folgerung für die App |
|---|---|---|---|
| Multimedia-Prinzip | [G] Wort + Bild schlägt Wort allein, Median d = 1,35 (Mayer 2021) | [Mayer, UNH-PDF](https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-research-based-principles-for-designing-multimedia-instruction-mayer.pdf) | [M] Jeder Erklärschritt hat ein Bild, das *die Rechnung trägt* (kein Schmuckbild). |
| Kohärenz | [G] Überflüssiges weglassen: 23 von 23 Tests positiv, Median 0,86 (Handbuch); 0,70 in Mayer 2017 | [Cambridge Handbook](https://resolve-he.cambridge.org/core/books/cambridge-handbook-of-multimedia-learning/principles-for-reducing-extraneous-processing-in-multimedia-learning-coherence-signaling-redundancy-spatial-contiguity-and-temporal-contiguity-principles/CD5B7AE1279A9AB81F8EEBB53DBEC86E), [Mayer 2017](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_journals_1936208032) | [M] Keine Deko-Figuren, keine Zusatzgeschichten im Erklärteil. |
| Signalisierung | [G] Wichtiges hervorheben: 24/28, Median 0,41 (0,46) | ebd. | [M] Farbcode: dieselbe Farbe für „Änderung von y“ im Bild, in der Tabelle und in der Formel. |
| Räumliche Nähe | [G] Wort direkt am Bildteil: 22/22, Median 1,10 (0,79) | [Chartered College](https://my.chartered.college/impact_article/how-multimedia-can-improve-learning-and-instruction/), Mayer 2017 | [M] Beschriftung *im* SVG statt Text darunter – am Handy besonders wichtig. |
| Segmentierung, Vorab-Begriffe | [G] Segmentieren d = 0,70; Vorab-Training (Namen/Eigenschaften der Teile vorher) 0,46 | Mayer 2017 | [M] Ein Bildschirm = ein Gedanke, das Kind tippt „weiter“. Die 2–3 Fachwörter kurz *vor* der Erklärung am Bild zeigen. |
| Vorwissen | [G] Ausgearbeitete Beispiele verlieren mit wachsender Erfahrung an Wirkung (Expertise-Umkehr) | [Wikipedia-Zusammenfassung](https://en.wikipedia.org/wiki/Worked-example_effect), Kalyuga u. a. 2003 dort zitiert | [M] Erklärung überspringbar machen mit Einstiegstest („3 richtig → direkt üben“). |
| Animation vs. Standbild | [G] d = 0,37 (Höffler & Leutner, 76 Vergleiche); bei realistischen/videobasierten 0,76. Neuere Metaanalysen: g = 0,23 (Berney & Bétrancourt, 140; Castro-Alonso u. a., 82). Eine Nachanalyse zeigt: Animation ist deutlich besser, **wenn die Einzelheiten einer Veränderung gelernt werden sollen** | [IPN](https://www.leibniz-ipn.de/en/research/publications/instructional-animation-versus-static-pictures-a-meta-analysis), [Ploetzner u. a. 2021](https://link.springer.com/article/10.1007/s11251-021-09541-w) | [M] Kein Video nötig. Gezielt *vom Kind gesteuerte* Bewegung, wo Veränderung der Inhalt ist (Pfeil auf dem Zahlenstrahl, Steigungsdreieck wandert). |
| Video statt/zusätzlich | [G] Hochschule, 105 RCTs, 7.776 Studierende: Video *statt* anderer Methode kleiner Vorteil, *zusätzlich* deutlicher Vorteil; als Ersatz für Lesetext mäßiger Vorteil | [AERA](https://www.aera.net/Newsroom/Video-Improves-Learning-in-Higher-Education-A-Systematic-Review), [Behavioral Scientist](https://behavioralscientist.org/should-video-lectures-be-the-new-normal-in-higher-ed/) | [A] Übertragbarkeit auf 11–14-Jährige unklar. [M] Video nur als freiwillige Zweit-Erklärung (Link), nicht als Kern. |
| Video-Länge | [G] 6,9 Mio. edX-Sitzungen: kürzer = deutlich mehr Engagement; Empfehlung **unter 6 Minuten**; Tablet-Handzeichnung im Khan-Stil wirkt besser als Folien. Gemessen wurde Engagement, nicht Lernen | [Guo, Kim, Rubin 2014](https://pg.ucsd.edu/publications/edX-MOOC-video-production-and-engagement_LAS-2014.txt) | [M] Falls je Videos: unter 6 Min., Hand-Zeichnung, eine Idee. |
| Virtuelle Manipulative | [G] 32 Berichte/82 Effekte: mäßiger Gesamteffekt 0,34; Folgestudie 104 Berichte bestätigt „mäßig“ | [Moyer-Packenham u. a. 2014](https://core.ac.uk/download/524678999.pdf), [2016](https://digitalcommons.usu.edu/teal_facpub/2399) | [M] Lohnend für Zahlenstrahl, Algebrakacheln, Bruchstreifen – nicht als Dauerzustand. |
| Concreteness fading | [G] Übersicht Fyfe u. a. 2014: konkret → abstrakt mit expliziter Verbindung vereint die Vorteile beider. Experiment (Studierende): Ausblenden ergab die beste Übertragung. Gegenstimme 2020: weniger verallgemeinerbar als behauptet. Konkret-reiche Bilder können bei Brüchen sogar hemmen (1. Klasse) | [Fyfe u. a. 2014](https://pc.cogs.indiana.edu/?p=885), [McNeil & Fyfe 2012](https://pcl.sitehost.iu.edu/rgoldsto/courses/cogscilearning/McNeilFyfe12.pdf), [Kritik 2020](https://link.springer.com/article/10.1007/s10648-020-09581-7), [eScholarship](https://escholarship.org/content/qt7r4080rq/qt7r4080rq.pdf?t=op2lva) | [M] Bild schlicht (Thermometer-*Skala*, nicht Foto), dann Skizze, dann nur Symbol. Den Übergang ausdrücklich zeigen. |
| DragonBox-Übertrag | [G] Long & Aleven (190 Kinder, Kl. 7/8, 5 Stunden): Tutor „Lynnette“ war im **Papiertest besser**; DragonBox-Kinder lösten mehr Aufgaben im Spiel und hatten mehr Spaß. Decker-Woodrow u. a. 2023 (über 3.600 zugeteilt, N = 1.850 ausgewertet, 9 × 30 Min.): FH2T und DragonBox besser als Papier-Kontrolle; Sofort-Rückmeldung (ASSISTments) nicht signifikant. DragonBox-Effekt 0,269 bei 55 $ pro Kind | [Long & Aleven](https://unpaywall.org/10.1145%2F3057889), [AERA Open 2023](https://doaj.org/article/28d05a10d8ea487f80d0c3b6811e3e9d), [Kostenanalyse](https://informahealthcare.com/doi/full/10.1080/19345747.2023.2269918) | [M] Spielregel als Brücke ja, aber das Ziel ist die geschriebene Gleichung. Spaß ist kein Beleg für Übertrag. |
| Beispiele, Selbsterklären, Vergleichen, Fehlerbeispiele | [G] Ausgearbeitete Beispiele in Mathe g = 0,48. Zusätzliche Lehrer-Erklärungen in beispielbasiertem Lernen bringen kaum etwas. Selbsterklär-Aufforderungen g = 0,55 (69 Effekte, meist Studierende). Fallvergleich d = 0,50 (57 Experimente). Lösungswege nebeneinander vergleichen fördert Begriff und Flexibilität. Fehlerbeispiele zu Dezimalzahlen: sofort kein Unterschied, **eine Woche später besser** (d = 0,62 bzw. 0,33); die Gruppe mit normalen Aufgaben war zufriedener | [Barbieri u. a. 2023](https://link.springer.com/content/pdf/10.1007/s10648-023-09745-1.pdf), [Wittwer & Renkl 2010](https://link.springer.com/doi/10.1007/s10648-010-9136-5), [Bisra u. a. 2018](https://doi.org/https://doi.org/10.1007/s10648-018-9434-x), [Alfieri u. a. 2013](https://www.lrdc.pitt.edu/Schunn/papers/ContrastingCasesMeta-AlfieriEtAl2013.pdf), [Rittle-Johnson u. a.](https://journals.sagepub.com/doi/10.1177/0963721420969365), [Adams u. a. 2014](https://dfki.de/web/forschung/projekte-publikationen/publikation/8598), [McLaren u. a. 2015](https://www.bibsonomy.org/bibtex/206672269b36bb928a85bc4d98fd4b3a1/brusilovsky) | [M] In jede Erklärung gehören ein Beispiel-Aufgaben-Paar, eine Selbsterklär-Frage (als Auswahl), ein Fehlerbeispiel und bei Klasse 8 ein Wegevergleich. Erklärtexte kurz halten. |
| Sprache, Fachwörter | [G] Bildungssprachliche Merkmale erhöhen die Leseschwierigkeit von Modellierungsaufgaben (N = 407, Klasse ≥ 7). Fachsprache als „Sprache des Verstandenen“ entsteht am Ende aus der Alltagssprache. Wortspeicher sollen Satzbausteine enthalten, nicht nur Fachwörter. Haag u. a. 2015 (sprachliche Vereinfachung, Deutschland) existiert, **Ergebnis nicht gelesen** | [Heine, Ehmke, Leiss](https://pubdata.leuphana.de/bitstreams/0e1f3069-376f-4ebb-aad1-1e7e98a9dcaa/download), [Meyer/Prediger (Zitat bei TU Dortmund)](https://eldorado.tu-dortmund.de/server/api/core/bitstreams/9c7c5a23-7f2d-426b-b95e-bb8243a6f6fa/content), [Prediger: Sprachschatzarbeit](https://wwwold.mathematik.tu-dortmund.de/~prediger/veroeff/17-Prediger-Sprachschatz_Webversion.pdf), [Haag u. a.](https://www.doi.org/10.1007/S10212-014-0233-6) | [M] Erst Alltagswort („wie schnell steigt es?“), dann Fachwort („Steigung“) am selben Bild. Wörterliste wird zum **Satzbaustein-Speicher** („Wenn x um 1 größer wird, wird y um … größer.“). [A] Kurze Sätze (Richtwert ≤ 12 Wörter für Kl. 5, ≤ 15 für Kl. 8); dafür keinen Beleg gefunden. |

---

## B) AUFGABENFORMEN jenseits von Zahl und Auswahl

### B1. Wer bietet was (Auswahl, belegt)
- [G] **Desmos:** Graph mit ziehbaren Punkten, Tabelle, Skizze, Kartensortieren, geordnete Liste, Polygraph (Ratespiel mit Fachwörtern), Marbleslides (Funktionsparameter so wählen, dass Kugeln Sterne treffen) ([Amplify-Hilfe](https://my.amplify.com/help/en/articles/6797997-getting-started-activity-builder)).
- [G] **Khan/Perseus:**
  - Über 60 Widget-Arten, darunter `radio`, `dropdown`, `categorizer` (Zuordnen), `expression`, `numeric-input`, `interactive-graph` (11 Graphtypen, gezeichnet mit Mafs), `label-image`, `graded-group`.
  - Die Bewertung liegt in einem eigenen Paket ohne React. Terme werden mit „KAS“ auf Gleichwertigkeit geprüft ([DeepWiki-Überblick](https://deepwiki.com/Khan/perseus)).
  - Lizenz MIT ([GitHub](https://github.com/Khan/perseus)). Externe Beiträge werden nicht angenommen ([Readme-Auszug](https://skillsmp.com/creators/khan/perseus)).
  - Die alten Khan-Aufgaben*inhalte* stehen unter CC BY-NC-SA ([khan-exercises](https://www.github.com/Khan/khan-exercises)).
- [G] **PISA 2022:** neue Computer-Aufgaben mit Tabellenkalkulation, Simulatoren, Datengeneratoren und Ziehen/Ablegen. Beispiel aus den veröffentlichten Aufgaben: Planeten nach Tabellenwerten in ein Modell ziehen ([OECD Annex A5](https://www.oecd.org/en/publications/pisa-2022-results-volume-i_53f23881-en/full-report/how-comparable-are-the-pisa-2022-computer-and-paper-based-tests_17307f33.html), [veröffentlichte Aufgaben](https://cdn.edupedu.ro/wp-content/uploads/2023/12/Unit-1-item-1.pdf)).
- [G] **H5P:** Drag and Drop, Drag the Words, Mark the Words, Find the Hotspot, Sort the Paragraphs, Image Sequencing, Fill in the Blanks u. a. ([Liste](https://html5.is.ed.ac.uk/)). Alles textorientiert, ohne Mathe-Prüfung.
- [G] **STACK/Numbas:** Zahl, Term, Matrix, Einheiten, Gleichungskette, Lückentext; Toleranz und Genauigkeit einstellbar (Details in C).
- Mathspace, Sparx, IXL, DeltaMath, Matific, TIMSS-eAufgaben: Typenlisten **nicht systematisch gefunden**.
  - [G] Mathspace: Handschrift-Erkennung nur in der iPad-App.
  - [G] Sparx: Varianten und Bookwork-Check (tief-7).

### B2. Katalog: Was prüft welcher Typ, wie automatisch, geht er bei 360 px?
Legende Aufwand (reines JS + SVG, bestehende App): **k** klein (≤ 2 Tage), **m** mittel (3–7 Tage), **g** groß (> 2 Wochen) [A, grobe Schätzung].

| Typ | prüft vor allem | Antwortwert + Regel (+ Toleranz) | 360 px mit Finger | Aufwand | Vorbild / Beleg |
|---|---|---|---|---|---|
| Punkt(e) im Gitter setzen | Darstellung, Begriff (Koordinaten, Graph) | Liste ganzzahliger Paare; Regel: Menge gleich *oder* „jeder Punkt erfüllt Bedingung“ (z. B. y = 2x − 1) | gut, wenn Punkte **einrasten**; Ziel ≥ 24 px, besser 44 px; Alternative: Tippen statt Ziehen (WCAG 2.5.7) | k | Desmos-Graph, Perseus `interactive-graph` |
| Gerade/Strecke über 2 Punkte | Zeichnen, Funktion | zwei Paare; Regel: beide auf der Zielgeraden und verschieden | gut (2 Taps) | k | Perseus, Desmos |
| Zahl auf Zahlenstrahl platzieren | Größenvorstellung (ganze Zahlen, Brüche) | Zahl; Regel: \|Antwort − Ziel\| ≤ Toleranz (z. B. 3 % der Spannweite) | gut (waagerecht) | k | [G] Leistung am Zahlenstrahl korreliert mit Mathe r = 0,44 ([Schneider u. a. 2018](https://lirias.kuleuven.be/bitstream/123456789/615149/1/Schneideretal2018.pdf)); **aber:** Bruch-Zahlenstrahlspiel ohne Übertrag ([Nuraydin u. a. 2022](https://www.uni-trier.de/fileadmin/fb1/prof/PSY/PAE/Team/Schneider/NuraydinEtAl2022_FractionGame.pdf)) |
| Schätzen mit Toleranz | Größenordnung, Plausibilität | Zahl; Regel: relativer Fehler ≤ x % | sehr gut (Zahlenfeld) | k | Numbas-Bereich, Pearson 2–3 % |
| Schieberegler | Parameter-Wirkung (m, t) | Zahl im Raster; Regel: Gleichheit nach Einrasten | gut mit großem Griff | k | Desmos, PhET |
| Sortieren/Ordnen | Ordnung, Verfahrensschritte | Permutation; Regel: Gleichheit (ggf. Teilpunkte nach Anzahl richtiger Nachbarn) | gut mit **Tippen in Reihenfolge** statt Ziehen | k | Desmos „Ordered List“, H5P |
| Zuordnen (Paare/Karten) | Darstellungswechsel Term–Graph–Tabelle–Text | Paarliste; Regel: Mengengleichheit | mittel: zweispaltig, Tippen-Tippen; Karten max. 2 Zeilen | m | Desmos Card Sort, Perseus `categorizer` |
| Mehrfach-Antippen | Begriff (alle, die …), Fehler markieren | Indexmenge; Regel: Mengengleichheit (Teilpunkte: Treffer − Fehlgriffe) | sehr gut | k | H5P Mark the Words |
| Tabelle ausfüllen | Verfahren, Funktion, Daten | Vektor; Regel je Zelle (Toleranz je Zelle) | gut bis 3 Spalten; sonst quer scrollen vermeiden | k | Desmos-Tabelle, Numbas Matrix |
| Diagramm ergänzen (Balken ziehen/Kreissektor) | Daten darstellen | Zahl je Balken im Raster; Regel: Gleichheit | gut (senkrecht ziehen, auch Tippen auf Rasterstufe) | k–m | PISA Ziehen, BMT Daten |
| Diagramm/Daten ablesen | Daten lesen (Median, Mittelwert, Anteil) | Zahl; Regel mit Toleranz bei Ablesen | gut, wenn Diagramm ≤ 320 px breit lesbar | k | BMT 11 % Daten (tief-5) |
| Term aus Bausteinen bauen | Termaufbau, Übersetzen Text→Term | Tokenfolge → Term; Regel: Gleichwertigkeit durch Einsetzen (tief-4) | mittel: Bausteinleiste + Zeile | m | [A] ähnlich Kartenbausteine; kein konkretes Vorbild geprüft |
| Gleichung per Ziehen umformen | Umformungsregeln | Endzustand; Regel: System lässt nur erlaubte Züge zu | mittel; braucht viel Feinmotorik | g | DragonBox/FH2T (Belege gemischt) |
| Winkel einstellen / messen | Geometrie, Messen | Gradzahl; Regel \|Δ\| ≤ 2–3° | mittel (Drehgriff außen am Schenkel) | m | [A] |
| Konstruieren (Zirkel/Geodreieck) | Konstruktion | Lage der Endpunkte; Regel: Abstand ≤ ε | schwer auf 360 px | g | GeoGebra (Lizenz) – **eher Papier** |
| Immer/manchmal/nie wahr | Begriff, Begründen | Auswahl + bei „manchmal“ je ein Beispiel/Gegenbeispiel (Einsetzen) | sehr gut | k | [A] Malcolm-Swan-Tradition; Quelle nicht gelesen |
| Gegenbeispiel / Beispiel nennen | Begründen, Übertrag | eine oder mehrere Zahlen; Regel: Prädikat per Einsetzen (Server) | sehr gut | k | BMT „mit Beispiel widerlegen“ (tief-5) |
| Lücke in einer Begründung | Begründen | Auswahl je Lücke oder Satzbaustein; Regel: Gleichheit | gut | k | [A] |
| Begründungsschritte ordnen | Begründen, Beweisstruktur | Permutation | gut (Tippen) | k | [G] STACK-Aufgaben mit Beweisstruktur im Online-Test ([arXiv](https://arxiv.org/pdf/2006.01581)) |
| Zwei Lösungswege vergleichen | Flexibilität, Begriff | Auswahl (welcher richtig/geschickter) + Baustein-Grund | gut | k (inhaltlich aufwendig) | Rittle-Johnson & Star (A2) |
| Fehler markieren in Rechnung | Fehlerbewusstsein | Zeilenindex (+ Fehlerart) | sehr gut | k | Fehlerbeispiele (A2) |
| Tabellenkalkulations-Formel | Termaufbau, Rangfolge, Zellbezug | Text `=…`; Regel: parsen, auf 5–10 versteckten Zellwerte-Sätzen auswerten, gleich der Musterformel; Groß-/Kleinschreibung, Leerzeichen, `;`/`,` tolerant | gut (Texteingabe mit Tasten A1, B2, (, ), +, −, *, /) | m | BMT 2022/24/25 (tief-5), PISA 2022 |
| Sicherheits-Abfrage („Wie sicher bist du?“) | Selbsteinschätzung | Stufe 1–3; nicht bewertet, nur Daten | sehr gut | k | [G] Long & Aleven maßen auch Selbsteinschätzung; Ergebnis nicht gelesen |

---

## C) EINGABE AM HANDY

**Befunde [G]**
- **Tastatur des Systems:**
  - iOS-Dezimaltastatur (`inputmode="decimal"`) und `type="number"` auf iPhone haben **kein Minus**. Fehler offen seit 2019 ([WebKit 193825](https://bugs.webkit.org/show_bug.cgi?id=193825), [Apple-Forum](https://developer.apple.com/forums/thread/678224)).
  - Android-Tastaturen setzen Minus und Komma uneinheitlich um ([Filament Group](https://filamentgroup.com/lab/type-number)).
  - Für eine App mit negativen Zahlen ab Klasse 5 ist das ein Muss-Thema.
- **Khan:** eigene Tastatur, die sich pro Aufgabe anpasst und nur die nötigen Tasten zeigt. Mehrseitig, mit Bruch- und Termvorlagen, ziehbarer Cursor ([Support](https://support.khanacademy.org/hc/tr/articles/202896260), [math-input](https://www.npmjs.com/package/math-input-pleduc)). Handschrift auf dem iPad wurde 2018 **durch die Tastatur ersetzt** ([Community](https://support.khanacademy.org/hc/hy/community/posts/115006430527/comments/115003897547)).
- **STACK (Philosophie):**
  - Erst wird geprüft, ob die Eingabe *gültig* ist, dann bewertet. Ungültiges kostet **nie** Punkte.
  - Das Kind kann sehen, wie die Eingabe gelesen wurde („Student must verify“).
  - Eine Syntax-Vorlage mit `?`-Platzhaltern ist möglich. Optionen: „Kommazahlen verbieten“, „gekürzt verlangen“, „Typ prüfen“ ([FAQ](https://moodle-sciences-24.sorbonne-universite.fr/question/type/stack/doc/en/Students/FAQ.md), [Inputs](https://docs.stack-assessment.org/en/Authoring/Inputs/), [Answer assessment](https://docs.stack-assessment.org/en/Students/Answer_assessment/)).
- **Numbas:**
  - Brüche als Antwort erlaubbar. „Muss gekürzt sein“ (dann ist 10/8 statt 5/4 falsch) mit **sichtbarem Hinweis**.
  - Genauigkeit (Stellen) mit **Teilpunkten** bei falscher Rundung.
  - Zulässige Zahlschreibweisen wählbar. Falle: `1.234` ist im Englischen ≈ 1, im Französischen 1234 ([Number entry](https://docs.numbas.org.uk/en/latest/question/parts/numberentry.html), [Notation](https://docs.numbas.org.uk/en/heads/new_layout_2022/number-notation.html)).
- **Kommerzielle Systeme:**
  - Pearson Mastering korrigiert eindeutige Formatfehler und zählt sie nicht als falsch. Unausgeglichene Klammern = neuer Versuch ohne Abzug. Standardtoleranz 2–3 %. Gleichwertige Einheiten (2 V = 2000 mV) werden akzeptiert ([Pearson](https://help.pearsoncmg.com/mastering/instructor/mplus/Topics/grading_what_counts_as_right_ans.htm), [Pearson 2](https://help.pearsoncmg.com/mastering/instructor/standalone/Topics/grading_what_counts_as_right_ans.htm)).
  - WebAssign zählt Syntaxfehler standardmäßig nicht als Versuch ([WebAssign](https://webassign.net/manual/instructor_guide/webassign/t_i_counting_responses_with_syntax_errors_as_incorrect_submissions.htm)).
  - Mathspace zeigt „Input error … Your score will not decrease“ ([Schülerleitfaden](https://content.govdelivery.com/attachments/VAEDUFCPS/2023/06/05/file_attachments/2516566/FCPS%20Student%20Guide%202023.pdf)).
- **Forschungsagenda e-Assessment:** Mathematisch richtige Antworten werden wegen Syntax als falsch gewertet. Eingabefehler unterscheiden sich von Papierfehlern (Beispiel „In“ statt „ln“) ([Q2](https://maths.github.io/e-assessment-research-agenda/questions/Q2), [Q39](https://maths.github.io/e-assessment-research-agenda/questions/Q39)).
- **Zielgrößen:** WCAG 2.2 AA: Tippziele ≥ 24 × 24 CSS-px, AAA 44 × 44. Ziehen braucht eine Ein-Zeiger-Alternative (Tippen) ([W3C 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum), [W3C 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging.html)).

**Wie gute Apps Brüche, Potenzen, Terme, Einheiten lösen [G/A]**
- Brüche:
  - Khan: Vorlage Bruchtaste mit zwei Kästchen.
  - Numbas: Schrägstrich `3/4` erlaubt.
  - [A] Gemischte Zahl als drei Kästchen (ganz, Zähler, Nenner).
- Potenzen: Hochstell-Taste mit Kästchen (Khan, MathLive). Linear `2^3` als Rückfall (STACK, Numbas).
- Terme: Tastatur mit `x`, Klammern, unsichtbarem Mal (`2x`). Prüfung durch Einsetzen (tief-4).
- Einheiten: STACK hat einen eigenen Einheiten-Eingabetyp. [A] Für Kinder besser: Zahl im Feld, Einheit als **Auswahlchip** daneben (mm/cm/m …), getrennt geprüft.

---

## D) QUALITÄT VON AUFGABEN UND AUFGABENFOLGEN

**Befunde [G]**
- **Eedi/Barton, fünf Regeln für Diagnosefragen** ([Medium](https://medium.com/eedi/what-makes-a-good-diagnostic-question-b760a65e0320), [Medium 2](https://medium.com/eedi/what-is-a-diagnostic-question-13bb85c64062)):
  1. eindeutig;
  2. **eine** Fähigkeit;
  3. in etwa 10 Sekunden lösbar;
  4. **jede falsche Option steht für einen bestimmten Fehler**;
  5. **mit der Fehlvorstellung darf man nicht richtig liegen**.
- **Variation (Watson/Mason, Barton):** Möglichst viel konstant halten und **ein** Element verändern. So richtet sich die Aufmerksamkeit auf das, was sich ändert. „Intelligent Practice“ liegt zwischen Flüssigkeitsübung und Methodenwahl ([variationtheory.com](https://variationtheory.com/what-is-variation-theory/), [Barton-Kurs](https://craigbarton.podia.com/view/courses/intelligent-practice), [Cambridge Espresso](https://cambridgemaths.org/Images/espresso_20_variation_theory_in_mathematics_education.pdf)).
- **Mischen:** Interleaving-RCT, 54 Klassen 7, 787 Kinder: unangekündigter Test nach einem Monat 61 % vs. 38 %, d = 0,83 ([IES](https://ies.ed.gov/funding/grantsearch/details.asp?ID=1790), [WWC](https://ies.ed.gov/ncee/wwc/Study/88770)).
- **Sparx** ([Blog](https://sparxmaths.com/blog/sparx-maths-content/)):
  - rund 50.000 Fragen aus 10 Jahren;
  - Beispielthema: 37 Fragen in **4 Schwierigkeitsstufen**, die Fluency und Problemlösen mischen;
  - je Frage etwa **3 „fills“** (gleiches Lernziel, gleiche Schwierigkeit, andere Zahlen/Kontexte);
  - Team aus Lehrkräften, Mathematikern, Datenanalysten und **Linguisten**; Daten aus 650 Mio. Versuchen;
  - Fragen so gebaut, dass man mit Fehlvorstellung nicht richtig liegt.
  - „Second Chance“ (zweiter Versuch an *derselben* Frage) wurde getestet. Ein kleiner Teil der Kinder kam damit ohne Verständnis zur Lösung, daher vorsichtig eingesetzt ([Blog](https://sparxmaths.com/blog/second-chance/)).
- **STACK-Qualitätssicherung** ([Testing](https://docs.stack-assessment.org/en/Authoring/Testing/)):
  - `s_assert` sperrt unbrauchbare Zufallswerte (z. B. Nenner 0);
  - Pro Frage Testfälle für die richtige Antwort, je einen pro Rückmeldezweig, ungültige Eingaben und eine völlig falsche Antwort; automatisch laufen lassen, auch nach Updates;
  - **Varianten werden erst nach Test „freigegeben“ (deployed)**.
- Rückmeldeknöpfe für Lernende („Aufgabe melden“): als Verfahren bei Sparx („Help & Support“) erwähnt, Ablauf **nicht gefunden**.

---

# LIEFERUNGEN

## 1. Muster „So sieht eine sehr gute Erklärung in dieser App aus“

### 1.0 Bauplan (für jedes Lernziel) [M, abgeleitet aus A1/A2]

| # | Baustein | Länge | Was das Kind tut | Beleg/Vorbild |
|---|---|---|---|---|
| 0 | **Einstiegstest** „Kannst du das schon?“ (2–3 Aufgaben) | 1 Min. | lösen; alles richtig → Erklärung überspringen | Expertise-Umkehr |
| 1 | **Alltagsbild + Handlung zuerst** | 1 Bildschirm, ≤ 25 Wörter | im Bild etwas tun (Pfeil setzen, Punkt tippen) | Brilliant „Frage vor Verfahren“, Mathigon, Desmos „Bedürfnis schaffen“ |
| 2 | **2–3 Mini-Fälle**, vom Bild gerechnet; nur *eine* Sache variiert | 2 Bildschirme, je ≤ 35 Wörter | je eine Eingabe; Rückmeldung *im Bild* („du bist bei −4 gelandet“) | Variation, interpretierende Rückmeldung |
| 3 | **Benennen:** Regel in 1–2 kurzen Sätzen + Fachwort am selben Bild, gleiche Farben | 1 Bildschirm, ≤ 35 Wörter | Satzbaustein-Lücke füllen (Auswahl) | Vorab-Begriffe, Signalisierung, „Sprache des Verstandenen“ |
| 4 | **Vorhersage/Selbsterklärung** ohne Rechnen | 1 Bildschirm | Auswahl „größer/kleiner/gleich, weil …“ | Selbsterklären g = 0,55 |
| 5 | **Fehlerbeispiel** einer erfundenen Person | 1 Bildschirm | Fehler antippen + Art wählen + richtig eintippen | Fehlerbeispiele (verzögert besser) |
| 6 | **Ausblenden:** gleiche Aufgabe mit Skizze, dann ohne Bild | 1–2 Bildschirme | 2–3 Eingaben | Concreteness fading, Beispiel-Aufgabe-Paare |
| 7 | **Schlussprüfung:** 3 gemischte Aufgaben, davon 1 Sachaufgabe und 1 andere Form | 1–2 Min. | lösen; 3/3 → „sitzt vorläufig“; sonst zurück zu 2 | Kulgemeyer „Folgeaufgabe“, Brilliant Skill Check |
| 8 | **Satzbaustein-Speicher** statt Wörterliste (aufklappbar, immer erreichbar) | – | – | Prediger |

Rahmen: **6–9 Bildschirme, 6–12 Minuten, 10–18 kurze Eingaben (je 1 Tipp oder 1 Zahl), kein Bildschirm über ~35 Wörter, Bild beschriftet *im* SVG**. Pro Erklärung höchstens 1 bewegtes Element, nur vom Kind gesteuert. Kein Video im Kern; optional ein Link „anders erklärt“ (unter 6 Min.).

### 1.1 Klasse 5: Negative Zahlen addieren

| Bildschirm | Inhalt (selbst gebaut) | Kind tut | Nachgerechnet |
|---|---|---|---|
| 0 Einstiegstest | −4 + 6 = ? · −3 + (−2) = ? · 5 + (−8) = ? | tippen | 2 · −5 · −3 ✓ |
| 1 Bild + Handlung | Senkrechtes Thermometer −10 bis 10 als Zahlenstrahl. „Morgens zeigt es −3 °C. Bis mittags wird es 5 Grad wärmer. Tippe, wo es mittags steht.“ (24 Wörter) | tippt auf Skala; ein Pfeil von −3 nach oben um 5 erscheint | −3 + 5 = 2 ✓ |
| 2 Mini-Fälle (nur Startwert variiert) | „−6 °C, 2 Grad wärmer“ → ? · „−1 °C, 4 Grad wärmer“ → ? | tippen auf Skala, dann Zahl | −4 ✓ · 3 ✓ |
| 2b neue Sache: *kälter* = plus negative Zahl | „4 °C, dann 7 Grad kälter. Das schreibt man 4 + (−7).“ | Pfeil nach unten tippen, Zahl eintippen | −3 ✓ |
| 3 Benennen | „Plus eine positive Zahl: Pfeil nach oben (rechts). Plus eine negative Zahl: Pfeil nach unten (links). Die Zahl ohne Vorzeichen heißt **Betrag**.“ Lücke: „Bei −2 + (−5) zeigt der Pfeil nach ___.“ | Auswahl oben/unten | unten; Ergebnis −7 ✓ |
| 4 Vorhersage | „Ohne zu rechnen: Ist −8 + 3 größer oder kleiner als 0? Weil …“ Bausteine: „der Pfeil ist kürzer als der Weg bis 0“ / „3 ist positiv“ / „−8 ist negativ“ | Auswahl + Baustein | kleiner (−5); richtiger Grund: Pfeil (3) kürzer als Abstand zu 0 (8) ✓ |
| 5 Fehlerbeispiel | „Mia rechnet −6 + 2 = −8.“ Was hat sie gemacht? (a) Beträge addiert und Minus behalten (b) richtig (c) Pfeil falsch herum. Dann richtig eintippen. | Auswahl + Zahl | (a); richtig −4 ✓ (dieselben Zahlen wie in 2, damit der Vergleich trägt) |
| 6 Ausblenden | erst nur waagerechter Strich mit 0, dann ohne Bild: −9 + 4 · −2 + (−5) · 7 + (−10) | tippen | −5 · −7 · −3 ✓ |
| 7 Schlussprüfung | −15 + 15 = ? · „Konto: −20 €. Oma zahlt 35 € ein.“ → ? · **Zahlenstrahl:** setze −12 + 5 auf einen Strahl von −20 bis 20 (Toleranz ±1) | Zahl, Zahl, Platzieren | 0 · 15 € · −7 ✓ |

Länge: 9 Bildschirme inkl. Test, ≈ 7–9 Min., rund 15 kurze Eingaben in der Erklärung plus 3 im Einstiegstest.
Die *Abkürzungsregel* (gleiche Vorzeichen: Beträge addieren; verschiedene: Differenz der Beträge, Vorzeichen der Zahl mit größerem Betrag) kommt [M] erst in einer **zweiten** Mini-Erklärung nach 1–2 Übungstagen. Sonst sind es zwei neue Dinge auf einmal.

### 1.2 Klasse 8: Lineare Funktion – Steigung (Bayern-Schreibweise y = mx + t)

| Bildschirm | Inhalt (selbst gebaut) | Kind tut | Nachgerechnet |
|---|---|---|---|
| 0 Einstiegstest | Steigung der Geraden durch (0\|1) und (2\|5)? · Steigt oder fällt y = −3x + 4? · m aus Tabelle x: 0, 1, 2 / y: 7, 4, 1 | tippen/auswählen | 2 · fällt · −3 ✓ |
| 1 Bild + Handlung | Wassertank: „Am Start 10 cm Wasser. Jede Minute kommen 3 cm dazu.“ Leeres Gitter x = Minuten 0–4, y = cm 0–25. „Setze die Punkte für 0, 1, 2 und 3 Minuten.“ | 4 Punkte tippen (einrastend) | (0\|10) (1\|13) (2\|16) (3\|19) ✓ |
| 2 Sehen, was gleich bleibt | Die App verbindet die Punkte. Zwischen 0 und 1 erscheint ein **farbiges Treppchen**: 1 nach rechts (blau), 3 nach oben (orange). „Wie hoch ist die Stufe zwischen Minute 2 und 3?“ | Zahl | 3 ✓ |
| 2b Treppchen größer (nur Breite variiert) | Kind zieht die rechte Treppenecke von x = 1 nach x = 3 (Tippen-Alternative: x wählen). Die App zeigt „2 nach rechts → 6 nach oben“. Frage: „Nach oben geteilt durch nach rechts = ?“ | Zahl | 6 : 2 = 3 ✓ |
| 2c Vergleich zweiter Tank | „Tank B: Start 10 cm, je Minute 1,5 cm.“ Beide Geraden erscheinen. „Welche ist steiler? Um wie viel steigt B pro Minute?“ | Auswahl + Zahl | A; 1,5 ✓ |
| 3 Benennen | „Die **Steigung m** sagt: Um so viel ändert sich y, wenn x um 1 größer wird. Mit zwei Punkten: m = (Änderung von y) : (Änderung von x).“ Orange/blau wie im Bild. Satzbaustein-Lücke: „Bei Tank A wird y um ___ größer, wenn x um 1 größer wird.“ | Zahl | 3 ✓ |
| 3b negativ (neue Sache) | Kerze: „20 cm hoch, brennt pro Stunde 2 cm ab.“ Punkte (0\|20) und (4\|12) sind gesetzt, Treppe geht *nach unten*. | m eintippen | (12 − 20) : (4 − 0) = −8 : 4 = −2 ✓ |
| 4 Vorhersage | „Gerade durch (0\|1) und (2\|−3): steigt oder fällt sie? Ohne zu rechnen.“ Bausteine: „y wird kleiner, während x größer wird“ / „der zweite Punkt hat ein Minus“ | Auswahl + Baustein | fällt; m = (−3 − 1) : (2 − 0) = −2 ✓; richtiger Grund: erster Baustein |
| 5 Fehlerbeispiel + Wegevergleich | „Tom rechnet für (1\|13) und (3\|19): m = 2 : 6.“ Fehler antippen (Brüche vertauscht). Daneben „Lea“: liest am Gitter 1 nach rechts, 3 nach oben. „Welche Wege sind richtig?“ | Antippen, Auswahl | Tom falsch (1/3), richtig 6 : 2 = 3; Lea richtig ✓ |
| 6 Ausblenden | nur Tabelle x: 0, 2, 4 / y: 5, 8, 11 → m? · nur Gleichung y = −0,5x + 2 → m? | tippen | 3 : 2 = 1,5 · −0,5 ✓ |
| 7 Schlussprüfung | (a) **Gerade zeichnen:** y = −0,5x + 2 durch zwei Gitterpunkte setzen (Regel: beide erfüllen die Gleichung). (b) **Offen:** „Nenne eine Steigung m, für die die Gerade fällt *und* steiler ist als y = 2x + 1.“ Regel: m < −2. (c) Sache: „Taxi: 4 € Grundpreis, 2 € pro km. Wie teuer sind 7 km? Was ist hier m?“ | 2 Taps, Zahl, 2 Zahlen | (a) z. B. (0\|2) und (2\|1) bzw. (4\|0): −0,5·2 + 2 = 1 ✓, −0,5·4 + 2 = 0 ✓ · (b) z. B. −3 ✓ (−2 selbst gilt nicht, \|−2\| = 2 ist nicht steiler) · (c) 4 + 2·7 = 18 €; m = 2 ✓ |

Länge: 12 Bildschirme inkl. Test, ≈ 10–13 Min., 15–18 Eingaben.
[M] Das Lernziel ist zu groß für eine Einheit. Besser teilen in „Steigung positiv“ (0–3) und „Steigung negativ + aus zwei Punkten“ (3b–7), dazwischen einen Tag Übung.

### 1.3 Vergleich mit dem heutigen Stand

| Merkmal | Heute | Muster | Warum (Beleg) |
|---|---|---|---|
| Reihenfolge | Einstieg → **Regel** → 3 Schritte → Fehler → Wörter | Einstieg → **Tun** → Mini-Fälle → Regel → Vorhersage → Fehler → Ausblenden → Prüfung | Brilliant/Mathigon; Beispiel→Regel bei Verfahren (Kulgemeyer); Wegevergleich und Fehlerbeispiel |
| Eingaben in der Erklärung | 0 | 10–18 kurze (plus Test) | Mathigon „bei jedem Schritt aktiv“; Selbsterklären |
| Bild | Standbild, 1 pro Schritt | dasselbe Bild durchgehend, wächst mit; Beschriftung im Bild; 1 vom Kind gesteuerte Bewegung | räumliche Nähe 1,10; Animation nur für Veränderung |
| Regel | 1 Satz | 1–2 kurze Sätze, *nach* dem Tun, mit Fachwort am Bild und gleichen Farben | Signalisierung, Vorab-Begriffe |
| Typischer Fehler | genannt | als **Fehlerbeispiel zum Bearbeiten** mit denselben Zahlen wie vorher | Adams/McLaren |
| Wörterliste | Liste | **Satzbaustein-Speicher** | Prediger |
| Sofort-Prüfung | keine | Einstiegstest + Schlussprüfung (3 Aufgaben, 1 andere Form) | Brilliant Skill Check, Kulgemeyer |
| Überspringen | – | bei 3/3 im Einstiegstest | Expertise-Umkehr |
| Funktionen-Fall | [A] Vermutlich Regel und Fachwörter ohne eigenes Tun; Koordinatensystem als Standbild | Punkte selbst setzen, Treppchen in Farbe, erst dann „Steigung“ | — |

Bau-Hinweis [M]: Der Erklärbaustein braucht nur Bausteine, die ohnehin geplant sind (Gitterpunkte, Tippen, Zahlenfeld) und einen neuen kleinen „Zahlenstrahl-Platzieren“-Baustein. Die Erklärung wird als Liste von Schritten gespeichert: `{bild, text≤35 Wörter, eingabe, prüfregel, rückmeldung_im_bild}`. Das entspricht dem Mathigon-Prinzip.

---

## 2. Rangliste: zwölf Aufgabenformen als Nächstes (Nutzen je Aufwand, Lücken zum BMT)

Lücken laut tief-5: Begründen ≈ 19 %, Zeichnen/Konstruieren ≈ 14 %, Daten lesen ≈ 11 %, Übertrag/Mischaufgaben am schwersten, Tabellenkalkulation in 3 von 4 Jahrgängen. [M] Die Rangfolge gewichtet die Lücke im BMT, den Aufwand und die Wiederverwendbarkeit.

| Rang | Form | schließt Lücke | Kl. 5 Beispiel (nachgerechnet) | Kl. 8 Beispiel (nachgerechnet) | Antwortwert + Prüfregel | Bedienung 360 px | Aufwand | Vorbild |
|---|---|---|---|---|---|---|---|---|
| 1 | **Gegenbeispiel / Beispiel nennen** (offen, per Einsetzen) | Begründen, Übertrag | „Ben sagt: Die Summe zweier ganzer Zahlen ist immer größer als jede der beiden. Gib zwei Zahlen an, für die das nicht stimmt.“ Regel: a + b ≤ a oder a + b ≤ b (⇔ a ≤ 0 oder b ≤ 0). Beispiel 5 und −2: 3 ≤ 5 ✓ | „Behauptung: (a + b)² = a² + b² für alle Zahlen. Widerlege.“ Regel: (a+b)² ≠ a² + b² ⇔ a·b ≠ 0. Beispiel a = b = 1: 4 ≠ 2 ✓ | Zahlenpaar; Prädikat auf dem Server | 2 Zahlenfelder mit ±-Taste | k (in Arbeit beim Mathe-Profi) | BMT „mit Beispiel widerlegen“ |
| 2 | **Punkte im Gitter setzen / Gerade über 2 Punkte / Spiegelpunkt** | Zeichnen, Darstellung | „Setze A(−3\|2) und den an der y-Achse gespiegelten Punkt A′.“ Regel: A′ = (3\|2) ✓ | „Zeichne y = −0,5x + 2.“ Regel: 2 verschiedene Gitterpunkte erfüllen die Gleichung, z. B. (0\|2), (4\|0) ✓ | Liste von Paaren; Menge gleich oder Bedingung | Einrasten, Ziele ≥ 44 px, Gitter max. 10 × 10 auf 340 px (≈ 34 px Abstand); Tippen setzt/entfernt | k–m (in Arbeit) | Desmos, Perseus |
| 3 | **Daten lesen mit echtem Diagramm** (Ablesen + Kennwert) | Daten | Säulendiagramm Niederschlag 5 Monate (12, 30, 25, 8, 15 mm): „In welchem Monat am meisten? Wie viel mehr als im trockensten?“ 30 − 8 = 22 ✓ | Punktwerte 7 Tage (3, 5, 5, 6, 8, 9, 13): „Median? Mittelwert?“ Median 6; Summe 49, Mittelwert 7 ✓ | Zahl (Ablese-Toleranz bei Skalen-Zwischenwerten) | Diagramm ≤ 320 px; Werte durch Antippen hervorheben | k | BMT, PISA |
| 4 | **Diagramm ergänzen** (Balken auf Wert ziehen/tippen) | Daten darstellen, Zeichnen | „Zeichne die fehlende Säule: 35 Kinder.“ Raster 5 → Höhe 35 ✓ | „Ergänze die Säule ‚Fr‘, sodass der Mittelwert von 5 Tagen 12 ist (Mo–Do: 10, 14, 9, 13).“ 60 − 46 = 14 ✓ | Zahl je Balken; Gleichheit im Raster | senkrechtes Ziehen + Tippen auf Rasterstufe; Wert wird angezeigt | k–m | PISA Ziehen |
| 5 | **Tabellenkalkulations-Formel** | Tabellenkalkulation, Termaufbau | Spalte A Anzahl, B Preis: „Formel für den Gesamtpreis in C2?“ Muster `=A2*B2`; geprüft auf 8 Zufallsbelegungen ✓ | „Mittelwert von B2 bis B4 ohne Funktion.“ Muster `=(B2+B3+B4)/3`. Häufiger Fehler `=B2+B3+B4/3` ist bei B = (3, 6, 9) 12 statt 6 → Rückmeldung „Punkt vor Strich?“ ✓ | Text; parsen (+ − * / ^ ( ) Zellbezüge, Zahlen, optional MITTELWERT/SUMME); Gleichheit der Werte auf versteckten Belegungen | eigene Tastenleiste mit `=`, `A2`…, Klammern | m | BMT 2022/24/25, PISA 2022 |
| 6 | **Begründungs-Puzzle**: Schritte ordnen + Lücke in Begründung (Satzbausteine) | Begründen | „Warum ist −3 + 5 positiv?“ Bausteine in Reihenfolge: „Ich starte bei −3.“ → „Ich gehe 5 nach rechts.“ → „Nach 3 Schritten bin ich bei 0.“ → „Es bleiben 2 Schritte, ich lande bei 2 > 0.“ ✓ | „Zeige, dass (1\|1), (3\|5), (4\|7) auf einer Geraden liegen.“ Schritte: m₁₂ = 4 : 2 = 2 → m₂₃ = 2 : 1 = 2 → gleiche Steigung und gemeinsamer Punkt → eine Gerade ✓ | Permutation bzw. Auswahl je Lücke; Gleichheit (Ablenker: „weil es so aussieht“) | Tippen in Reihenfolge, Karten ≤ 2 Zeilen | k | STACK-Beweisaufgaben, BMT-Begründen |
| 7 | **Immer / manchmal / nie wahr + Beleg** | Begriff, Begründen | „Negative + positive Zahl ergibt eine negative Zahl.“ → manchmal; Beleg-Paare: −5 + 2 = −3 (negativ), −2 + 5 = 3 (nicht negativ) ✓ | „Zwei Geraden mit gleicher Steigung haben genau einen Schnittpunkt.“ → nie (parallel: keiner; identisch: unendlich viele) ✓ | Auswahl + bei „manchmal“ je ein Beispiel/Gegenbeispiel (Einsetzen) | 3 große Knöpfe + Zahlenfelder | k | [A] Swan-Tradition |
| 8 | **Fehler markieren** (Zeile antippen + Fehlerart) | Fehlerbewusstsein, Begründen | 3-zeilige Rechnung „−7 + 3 = −10“ in Zeile 2 → Zeile 2, Art „Beträge addiert“; richtig −4 ✓ | Umformung 3x + 5 = 20 → 3x = 25 (Fehler) → x = 25/3: Zeile 2, richtig 3x = 15, x = 5 ✓ | Index + Auswahl + Zahl | Zeilen ≥ 44 px hoch | k | Fehlerbeispiele, bettermarks-Fehlermuster (tief-1) |
| 9 | **Zahl auf Zahlenstrahl platzieren** (Toleranz) | Größenvorstellung, Darstellung | −35 auf Strahl −100 bis 100; Toleranz ±6 (3 % der Spannweite 200) ✓ | 2⁻¹ und 3/4 auf Strahl 0 bis 2; Toleranz ±0,06 ✓ (0,5 bzw. 0,75) | Zahl; \|Δ\| ≤ Toleranz | waagerecht, Tippen + Feinschieben, Lupe | k | Schneider 2018 (Korrelation), Nuraydin 2022 (kein Übertrag) – daher nur als *ein* Baustein |
| 10 | **Wertetabelle ausfüllen** (mehrere Zellen) | Verfahren, Funktion, Daten | Temperaturverlauf: Start −4, stündlich +3 → nach 1, 2, 3 h: −1, 2, 5 ✓ | y = 2x − 3 für x = −1, 0, 2: −5, −3, 1 ✓ | Vektor; Regel je Zelle; Folgefehler sichtbar | max. 4 Spalten, eigene Tastenleiste | k | Desmos-Tabelle |
| 11 | **Zuordnen (Karten-Paare)**: Graph ↔ Gleichung ↔ Tabelle ↔ Text | Darstellungswechsel, Übertrag | Thermometerbild „von −2 auf 3“ ↔ „−2 + 5“; „von 1 auf −4“ ↔ „1 + (−5)“ ✓ | „Start 4, je Schritt −1“ ↔ y = −x + 4 ↔ Tabelle (0\|4),(2\|2) ✓; Ablenker y = x + 4 | Paarliste; Mengengleichheit | Tippen-Tippen, zwei Spalten, 3–4 Paare | m | Desmos Card Sort |
| 12 | **Winkel einstellen / messen** (Geodreieck-leicht) | Zeichnen/Messen (Geometrie Kl. 5) | „Stelle einen Winkel von 135° ein.“ \|Δ\| ≤ 3° ✓ | „Im Dreieck sind α = 47°, β = 68°. Stelle γ ein.“ 180 − 115 = 65°, \|Δ\| ≤ 2° ✓ | Gradzahl; Toleranz | Drehgriff außen am Schenkel; Alternative ±1°-Knöpfe | m | [A] |

Ausdrücklich **nicht** in die Top 12 [M]:
- Gleichung per Ziehen umformen (groß, Belege gemischt);
- freie Konstruktion mit Zirkel (Papier, siehe 6);
- Freitext-Begründung mit KI-Bewertung (siehe tief-4, nur Pilot).

Zwei Wegevergleiche (A2) sind bereits als Inhalt in Form 6/8 enthalten.

---

## 3. Regeln für die Eingabe am Handy und für tolerante Prüfung [M, gestützt auf C]

**Bedienung**
1. **Eigene Tastenleiste** statt Systemtastatur bei allen Zahlen-, Bruch- und Termeingaben. Grund: iOS-Minus-Problem.
   - Tasten passend zur Aufgabe (Khan): Ziffern, `,`, `±` bzw. `−`, `⌫`; bei Bedarf `□/□`, `x`, `( )`, `^□`, `=`, Zellbezüge.
   - Systemtastatur nur für Text.
2. **Höhe:** 4 Tastenreihen × 44 px + Abstände ≈ 190 px ≈ 26 % von 740 px Höhe [A].
   - Während der Eingabe den Kopf (Reiter, Etappenleiste) auf eine Zeile ≤ 40 px einklappen. Die Aufgabe bleibt oben sichtbar.
   - Tablet/Rechner: Tastenleiste rechts neben der Aufgabe oder echte Tastatur.
3. **Tippziele** ≥ 44 × 44 px für Hauptaktionen, nie < 24 px (WCAG). Jede Zieh-Aktion hat eine Tipp-Alternative (WCAG 2.5.7).
4. **Vorlagen** statt Syntax:
   - Bruch = zwei Kästchen; gemischte Zahl = drei Kästchen; Potenz = Hochkästchen;
   - Einheit = Auswahlchip neben dem Zahlenfeld;
   - „x = □“ vorgegeben, wenn eine Lösung gesucht ist.
5. **Zurückspiegeln vor dem Bewerten** (STACK „verify“): die Eingabe in Schulschreibweise anzeigen („Du meinst: −3/4“). Bei Termen immer, bei einfachen Zahlen nur, wenn umgedeutet wurde.

**Tolerante Prüfung (Server)**
6. **Erst „gültig?“, dann „richtig?“.** Ungültige Eingaben (leer, `3--`, unbalancierte Klammern, zwei Kommas) zählen **nie** als Fehlversuch und nie gegen „sitzt“. Rückmeldung nennt das Formproblem, nicht „falsch“.
7. **Zahlnormalisierung:**
   - Leerzeichen und Tausenderpunkte entfernen. `,` und `.` als Dezimaltrenner zulassen, außer es ist mehrdeutig (`1.234` → nachfragen).
   - Minuszeichen-Varianten (− – - ‒) gleich behandeln; führendes `+` erlauben.
   - `0,50` = `0,5`; `,5` = `0,5`; `5,` = `5`.
8. **Brüche:** wertgleich = richtig, *außer* die Aufgabe verlangt ausdrücklich „gekürzt“.
   - Dann: „Richtig gerechnet – noch kürzen“, zählt als *halb* bzw. eigener Fehlerzweig, nicht „falsch“ (Numbas-Hinweis vorher anzeigen).
   - `6/3` bei Ganzzahl-Ergebnis annehmen, wenn nichts verlangt ist.
   - Gemischte Zahl `1 1/2` = `3/2` = `1,5`, wenn die Aufgabe die Form nicht vorschreibt.
9. **Rundung:** Ziel-Stellenzahl im Aufgabentext. Wert mit richtiger Stellenzahl = voll. Richtiger Wert mit falscher Stellenzahl = Teilpunkt + Hinweis (Numbas). Messen/Ablesen mit absoluter Toleranz, Schätzen mit relativer.
10. **Einheiten:** Ist die Einheit nicht Lerngegenstand, gleichwertige Einheiten annehmen (2 m = 200 cm). Ist sie Lerngegenstand, getrennt prüfen und getrennt rückmelden („Zahl stimmt, Einheit fehlt“).
11. **Gleichungen und Mengen:** `x = 3`, `3`, `x=3,0` gleich. Bei mehreren Lösungen Reihenfolge egal. Punkte als `(3|2)`, `(3;2)`, `3/2`? → nur Gitter- oder Zweifeld-Eingabe, keine freie Schreibweise.
12. **Prozent:** `25 %` und `25` gleich, wenn nach Prozent gefragt; `0,25` nur, wenn nach Anteil gefragt. Sonst Hinweis „als Prozent angeben“.
13. **Terme:** Gleichwertigkeit durch Einsetzen (tief-4). Wird eine *Form* verlangt („ausmultipliziert“), zweistufig prüfen: wertgleich? Dann Form-Regel. Rückmeldung getrennt.
14. **Folgefehler:** In Mehrfeld-Aufgaben (Tabelle, Kontrollzahlen) den nächsten Wert *aus dem Kindwert* nachrechnen und als „Folgefehler“ werten (Numbas „adaptive marking“, tief-4).
15. **Protokoll:** Jede als ungültig verworfene oder umgedeutete Eingabe speichern. Wöchentlich ansehen: Häufen sich Formprobleme bei einer Aufgabe, ist die *Aufgabe* fehlerhaft (siehe Checkliste).

---

## 4. Checkliste für den Abnahme-Prüfer

### 4a. Einzelaufgabe (jede Vorlage/Schablone, nicht jede Variante)
- [ ] **Ein Lernziel**: Die Aufgabe prüft genau eine neue Sache (bei Mischaufgaben sind die Teile benannt).
- [ ] **Eindeutig**: genau eine richtige Antwort *oder* eine ausformulierte Prüfregel für offene Antworten; Toleranz angegeben.
- [ ] **Keine Glückstreffer**: Mit der typischen Fehlvorstellung ist man nicht richtig (Eedi-Regel 5). Prüfen: Fehlerregel auf die Zahlen anwenden – kommt zufällig dasselbe heraus? (z. B. −2 · −2 vs. −2 − 2 ≠; aber 2 + 2 = 2 · 2 → solche Zahlen sperren).
- [ ] **Auswahl-Ablenker**: Jede falsche Option ist das Ergebnis eines benannten Fehlers. Keine Zufallszahlen. Mindestens 3 Ablenker oder bewusst 2 (dann begründet).
- [ ] **Begründen-Auswahl**: Der richtige Grund ist nicht der längste oder fachsprachlichste. Mindestens ein Ablenker ist eine *wahre, aber unpassende* Aussage.
- [ ] **Zahlbereich sauber**: Kein Zufallswert erzeugt Nenner 0, „krumme“ Zwischenergebnisse ohne Absicht, negative Längen oder 0 als Steigung, wenn „steigt“ gefragt ist (`s_assert`-Prinzip).
- [ ] **Sachkontext trägt**: Die Rechnung folgt aus dem Kontext. Die Zahlen sind realistisch (Temperatur, Preise). Der Kontext ist nicht austauschbar ohne Folgen. Bei Gleichheit lieber ohne Kontext.
- [ ] **Sprache**: Sätze kurz (Richtwert ≤ 12 Wörter Kl. 5, ≤ 15 Kl. 8, [A]). Fachwörter nur, wenn eingeführt. Keine doppelten Verneinungen. Die Frage steht am Ende.
- [ ] **Handy-Test 360 px**: Aufgabe + Eingabe ohne Scrollen sichtbar. Bild lesbar (Schrift ≥ 14 px). Tippziele ≥ 44 px. Hell und dunkel geprüft.
- [ ] **Eingabe-Test**: 10 Schreibweisen der richtigen Antwort (Komma/Punkt, −/-, ungekürzt, mit Einheit, mit „x =“) → alle wie in Regel 7–13 behandelt. 3 ungültige → nicht als falsch gezählt.
- [ ] **Rückmeldung**: Für die 2–3 häufigsten Fehler gibt es eine eigene Rückmeldung, die *zurückspiegelt* („Du hast die Beträge addiert“). Sonst ein Verweis auf ein Beispiel.
- [ ] **Testfälle hinterlegt** (STACK-Prinzip): richtig, je ein Fehlerzweig, ungültig, völlig falsch → laufen automatisch bei jeder Änderung.
- [ ] **Typ-Etikett stimmt**: „begründen“ verlangt eine Begründung (nicht nur Ergebnis wählen). „transfer“ hat eine neue Oberfläche.

### 4b. Aufgabenfolge (pro Lernziel)
- [ ] **Stufen sind echte Stufen** (wie Sparx' 4 Stufen), nicht größere Zahlen:
  - (1) direkt mit Bild;
  - (2) direkt ohne Bild;
  - (3) Umkehr/Lücke/andere Darstellung;
  - (4) Mischaufgabe/Sachaufgabe/Begründen.
- [ ] **Kontrollierte Variation**: In den ersten 4–6 Aufgaben ändert sich jeweils **eine** Sache (Vorzeichen, Lage des Unbekannten, Darstellung). Die Änderung ist beabsichtigt und benannt.
- [ ] **Mindest-Vielfalt** pro Lernziel: ≥ 3 verschiedene Antwortformen (z. B. Zahl, Gitter/Strahl, Auswahl mit Grund) und ≥ 1 Begründen- oder Gegenbeispiel-Aufgabe. Höchstens 60 % „Zahl eintippen“ [A, abgeleitet aus BMT ≈ 30 % Lücke/Kreuz].
- [ ] **Nicht-Beispiele**: Mindestens eine Aufgabe, bei der die Regel *nicht* gilt oder das Verfahren nicht nötig ist (z. B. −5 + 5 = 0; Gerade mit m = 0).
- [ ] **Mischen**: Nach Einführung kommen ≥ 30 % der Übungsaufgaben aus früheren Lernzielen, ohne Ankündigung (Interleaving).
- [ ] **Varianten**: ≥ 3 gleichwertige Varianten pro Schablone. Stichprobe von 20 Erzeugnissen gelesen; keine zwei aufeinanderfolgenden fast gleich.
- [ ] **Abdeckung BMT-Formen** pro Halbjahr: Begründen, Zeichnen, Daten, Tabellenkalkulation (ab Kl. 7), Sachaufgabe kommen vor.
- [ ] **Daten-Rückschau** nach 2 Wochen Nutzung:
  - Aufgaben mit > 90 % oder < 20 % Erfolg ansehen.
  - Ablenker, die nie gewählt werden, ersetzen.
  - Häufige ungültige Eingaben = Aufgabe unklar.
- [ ] **Melde-Knopf** „Mit dieser Aufgabe stimmt etwas nicht“ (1 Tipp, Grund-Auswahl: Lösung falsch / unklar / Eingabe geht nicht). Gemeldete Aufgaben werden bis zur Prüfung aus dem Prüfungsmodus genommen.

---

## 5. Einbinden statt selbst bauen – und was man weglässt

| Baustein | Lizenz | Größe (selbst gemessen, npm, 25.11.2026) | Handy | Offline | Urteil [M] |
|---|---|---|---|---|---|
| **Eigenes SVG** (Gitter, Zahlenstrahl, Tippen, Ordnen, Balken, Tabelle, Winkel) | eigen | je ~ 5–20 KB [A] | voll steuerbar | ja | **Selbst bauen.** Alle Top-12-Formen außer ggf. Geometrie. Pointer Events + `touch-action: none` auf der Zeichenfläche. |
| **JSXGraph** 1.14.3 | [G] MIT **oder** LGPL-3.0 (frei wählbar) ([npm](https://npmjs.com/package/jsxgraph), [Uni Bayreuth](https://jsxgraph.uni-bayreuth.de/wp/index.html)) | `jsxgraphcore.js` 996 KB, **259 KB gzip** | [G] Multi-Touch, keine Abhängigkeiten | ja (lokal ausliefern) | **Nur bei Bedarf für Geometrie** (Spiegeln, Lot, Kreis-Schnitt). Lazy laden, nur auf Geometrie-Seiten. Uni Bayreuth = bayerische Didaktik. |
| **MathLive** 0.111.4 | [G] MIT | `mathlive.min.js` 848 KB, **230 KB gzip**, Schriften 300 KB | eigene virtuelle Tastatur | ja (Schriften lokal) | Erst ab Klasse 8 für Termeingaben, wenn Vorlagen nicht reichen (siehe tief-4). Sonst eigene Tastenleiste. |
| **D3** 7.9.2 | [G] ISC (npm-Angabe nicht gesondert geprüft) | 281 KB, 92 KB gzip | – | ja | **Weglassen**: Diagramme selbst in SVG schneller und kleiner. |
| **Desmos-API** | [G] API-Schlüssel nötig, Demo-Schlüssel nur für Entwicklung, Produktion „contact us“. Nutzungsbedingungen mit Abschnitt „Personal, Non-Commercial Use Only“ ([API](https://www.desmos.com/api/v1.12/docs/index.html), [Geometry API](https://desmos.com/api/geometry), [Terms](https://desmos.com/terms)) | Skript vom Desmos-Server | gut | **nein** | **Weglassen** (online-pflichtig, Schlüssel, Bedingungen). Als Vorbild für Rückmeldung nutzen. |
| **GeoGebra** | [G] nicht-kommerzielle Lizenz. Selbst-Hosting über „Math Apps Bundle“ möglich. „Selbstprüfende Aufgaben mit Rückmeldung“ und Einbindung in Prüf-Plattformen stehen auf der Lizenzseite unter Software-Lizenzierung, Preise auf Anfrage ([Embedding](https://wiki.geogebra.org/en/Reference:GeoGebra_Apps_Embedding), [License](https://geogebra.org/license), [Licensing](https://geogebra.org/m/yumfrbjr)) | Bundle groß (nicht gemessen) | gut | mit Bundle ja | **Weglassen** für bewertete Aufgaben (Lizenzfrage, Größe). Höchstens als *unbewertete* Entdeck-Seite per Link. Rechtliches nur wiedergegeben. |
| **Perseus (Khan)** | [G] MIT | Monorepo (TypeScript/React), 60+ Widgets | gut | – | **Nicht einbinden** (React, groß, keine externen Beiträge). **Abschauen:** Widget-Liste, Trennung „Anzeige ↔ Bewertung ohne UI“, Rubrik-Format. |
| **Mafs** 0.21.0 | [G] MIT, braucht **React ≥ 18** | – | gut | – | **Weglassen** (Framework). |
| **H5P / h5p-standalone** 3.8.2 | [G] MIT ([Moodle-Doku](https://docs.moodle.org/402/en/Interactive_Content_-_H5P_activity)) | dist 1,4 MB | mittel | ja | **Weglassen**: bewertet im Browser (App braucht Server-Prüfung), textorientiert, kaum Mathe-Typen. |
| **STACK / Numbas** | GPL bzw. (Numbas-Lizenz nicht geprüft) | Server/Moodle | – | – | **Nur Vorbild** für Eingaberegeln, Testfälle, Toleranzen (tief-4). |

**Weglassen insgesamt [M]:** eigene Videos (Aufwand hoch, Belege schwach für Ersatz). DragonBox-artiges Gleichungsspiel. Handschrift-Erkennung (Khan hat sie aufgegeben; Mathspace nur iPad-App). 3D. Freie Konstruktion mit Zirkel am Handy. Punkte-Animationen ohne Lernbezug (Kohärenz).

---

## 6. Was nur auf Papier geht – und wie App und Heft zusammenspielen [M, mit Bezug auf tief-4/tief-5]

**Nur oder besser auf Papier**
1. **Konstruieren** mit Zirkel und Geodreieck: Dreiecke, Mittelsenkrechte, Winkelhalbierende, Thaleskreis. BMT erlaubt diese Hilfsmittel ausdrücklich (tief-5).
2. **Längere Begründungen in eigenen Sätzen**: BMT verlangt sie in rund 24–33 % der BE.
3. **Vollständige Rechenwege** bei mehrschrittigen Sachaufgaben und Termumformungen.
4. **Diagramme von Hand** zeichnen: Achsen wählen, skalieren, beschriften.
5. **Prüfungsbedingungen**: 40–60 Min. ohne Taschenrechner, ohne Hilfen, mit Zeitdruck.

**Zusammenspiel (Vorschlag)**

| Papier-Tätigkeit | Was die App tut | Prüfwert in der App | Wer bewertet den Rest |
|---|---|---|---|
| Konstruktion | stellt die Aufgabe (Maße so gewählt, dass ein Ergebnis messbar ist) | **Messwert** aus der eigenen Zeichnung, z. B. „Miss Seite c.“ Toleranz ± 2 mm bzw. ± 2°. Beispiel: Dreieck a = 6 cm, b = 8 cm, γ = 90° → c = 10 cm ✓ (6² + 8² = 100) | Elternteil mit 3-Punkte-Raster (genau / sauber / beschriftet), Foto optional |
| Begründung schreiben | Aufgabe + **Bewertungsraster** mit 2–4 Merkmalen (z. B. „nennt beide Steigungen“, „verwendet ‚weil‘“, „zieht Schluss“) | Kind hakt selbst ab, welche Bausteine seine Begründung enthält. Danach zeigt die App die Musterbegründung zum Vergleich | Elternteil prüft das Abhaken stichprobenartig |
| Rechenweg | Kontrollzahlen 1–2 Zwischenergebnisse (tief-4) | Zahl(en) | Elternteil sieht Heft bei Abweichung |
| Diagramm von Hand | gibt Daten vor | **Ablese-Kontrolle**: „Wie hoch ist deine Säule für Mai in Kästchen?“ | Raster: Achsen beschriftet / Skala gleichmäßig |
| Wöchentliche Papierrunde (BMT-ähnlich, 30–40 Min.) | stellt aus gesicherten Lernzielen 6–8 gemischte Aufgaben zusammen (Ausdruck) | Endergebnisse werden danach eingetippt | Elternteil korrigiert mit Lösungsblatt; Punkte gehen als „Papierwert“ in die App |
| Tabellenkalkulation | Formel in der App (Form 5) | wie dort | **einmal pro Monat** echte Tabelle am Rechner (LibreOffice/Numbers) [A] |

Regel [M]: Ein Lernziel gilt erst als „sitzt“, wenn es auch in **einer Papierrunde** richtig war. So kommt der Prüfungsmaßstab (tief-5) in die Fortschrittslogik.

---

## Was ich nicht prüfen konnte
- **Demo-Lektionen selbst bedient**: Brilliant, Mathigon, Desmos, Khan, Beast Academy online, simpleclub, Serlo, bettermarks-Tafelbilder, PhET. Ich habe nur Beschreibungen gelesen, nichts angeklickt oder angemeldet. Längen, Wortzahlen und Bildschirmzahlen konkreter Lektionen sind daher **nicht gemessen**.
- Desmos-Leitfaden 2016 im Volltext (Seite nicht abrufbar; nur Suchausschnitt). Seite „my-api“ (lädt nicht ohne Skript), daher Schlüssel-Bedingungen nur indirekt.
- Mathspace, Sparx, IXL, DeltaMath, Matific, TIMSS-eAufgaben: vollständige Listen der Eingabetypen nicht gefunden. Britische Tests (Typen) nicht untersucht.
- Ergebnisse von Haag u. a. 2015 (sprachliche Vereinfachung), WestEd-Evaluation Beast Academy, Fyfe u. a. 2015: nicht gelesen.
- Lesbarkeits-Grenzwerte für 11–14-Jährige (Satzlänge): keine belastbare Quelle gefunden; Richtwerte sind Annahmen.
- 3Blue1Brown/Numberphile, japanische Schulbücher im Original: nicht vertieft (Japan/Singapur siehe tief-6).
- GeoGebra-Bundle-Größe, Numbas-Lizenz, D3-Lizenz im Paket: nicht geprüft.
- Wirkung der meisten neuen Aufgabenformen (Gitter, Ordnen, Zuordnen, Tabellenkalkulation, immer/manchmal/nie) auf Lernerfolg: **keine kausalen Studien gefunden**. Belegt sind nur Nachbarbefunde (Fehlerbeispiele, Vergleichen, Selbsterklären, Mischen, Zahlenstrahl-Korrelation).
- Bauaufwand-Schätzungen sind grobe Annahmen ohne Blick in den App-Code.
- Gerätetest am echten 360-px-Handy (Tastenleiste, Ziehen, iOS-Minus): nicht durchgeführt.
