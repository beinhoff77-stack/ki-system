# Tiefen-Sucher 11: Bedienung, Aussehen, Ablauf, Eltern-/Lehrerseite, Technik, Tagesstruktur

Abruf aller Links: 25.11.2026. Kennzeichnung: [G] gesichert (Quelle gelesen), [A] Annahme/Schluss von mir, [M] Meinung/Empfehlung, [?] nicht gefunden oder nicht prüfbar. Nichts angemeldet, nichts gekauft, keine Dateien im Projekt verändert. Bereits Recherchiertes (bettermarks/Mathegym, Sparx-Bookwork, Fernschulen) wird nur verwiesen: tief-1-bettermarks-mathegym.md, tief-7-europa-welt.md, sucher-d-fernschule-rueckkehr.md.

Wichtige Grenze vorweg: Von den Vorbildern konnte ich fast nur Hilfeseiten, App-Store-Texte und Fallstudien Dritter lesen, keine eigenen Screenshots der Übungsbildschirme (kein Konto, keine Demo geöffnet). Wo ich Aussehen beschreibe, steht die Quelle dabei; sonst [?].

---

## 0. Die zehn wichtigsten Befunde in Kürze

1. [G] Tippflächen: Das Kinder-Material von Nielsen Norman Group (NN/g) nennt für kleine Kinder mindestens 2 cm × 2 cm (Erwachsene 1 cm); ab etwa 11 Jahren können Kinder dieselben Gesten wie Erwachsene. Für Teenager und 11-Jährige reichen also die üblichen 44 pt (Apple) bzw. 48 dp (Google). Die Zifferntasten der App (ca. 60 px hoch) erfüllen das. Problem ist nicht die Tastengröße, sondern dass das Zahlenfeld die Aufgabe verdeckt (Bild kj-nb-uebung-400).
2. [G] Teenager lehnen kindliche Gestaltung und Ansprache ab, mögen kurze Texte, hassen Warten und kleine Schrift (NN/g). Das trifft den 14-Jährigen; Sticker wie „Yo Digga!“ sind riskant [M].
3. [G] Antwortzeiten (NN/g): bis 0,1 s fühlt sich sofort an; bis 1 s bleibt der Gedankenfluss, darüber braucht es ein Zeichen „arbeitet“; ab etwa 10 s will der Nutzer etwas anderes tun, dann Fortschrittsanzeige und Abbruchmöglichkeit. Das sind die Schwellen für Prüfen und Ansichtswechsel.
4. [G] Brilliant, Duolingo, Desmos: ein Gedanke je Bildschirm, Rückmeldung direkt am Ort der Aufgabe, Fortschritt als eine einzige Leiste. Duolingo zeigt oben eine Leiste, unten eine Rückmeldung mit einem „Weiter“-Knopf.
5. [G] Zeitrichtwerte der Anbieter (alle Anbieter-Studien, beobachtend): Khan Academy 30+ Min./Woche ≈ 20 % mehr Lernzuwachs als erwartet; Math Academy 3 bis 5 Tage/Woche, 20 bis 40 Minuten; My Math Academy (Vorschule) mehrere kurze Einheiten statt einer langen. Für „Schule ersetzen“ ist das Minimum, nicht das Ziel; Bayern-Stundentafel Mathe liegt bei 3 bis 4 Wochenstunden.
6. [G] Lern-Dashboards: Überblicksstudien finden meist Anzeigen zum Bewusstmachen, aber wenig Handlungsempfehlungen; geringe Nutzung, wenig Lehrkräfte in der Gestaltung beteiligt; Wirkung auf Lernergebnisse schwach belegt. Lehre: wenige Angaben, je Angabe eine Handlung.
7. [G] Sparx: wöchentliche Eltern-E-Mail mit Link zu einer Detailseite; Schulen mit aktiven Eltern-Mails haben im Mittel rund 15 % höhere Abschlussquote (Anbieterangabe). Eltern sollen dem Kind nicht beim Lösen helfen, sonst „glaubt“ das System, es könne mehr.
8. [G] Dein eigenes Vorschaubild „Was wackelt?“ (la3-wackelt-400) enthält schon die beste Elternfunktion: echte falsche Antworten, Kurzregel, „Erneut besprochen ✓“. Es ist die Keimzelle der Tischkarte. Es ist am Handy aber kaputt (Spalten brechen Wörter vertikal um).
9. [G] Offline: Eine verbreitete Muster-Empfehlung ist „lokal zuerst, Netz im Hintergrund“ (Service Worker, lokale Warteschlange, Wiederholung mit zunehmenden Abständen). Die deutsche Lern-App Anton verkauft „Offline-Lernen“ als Plus-Funktion, es ist also ein bekannter Bedarf.
10. [M] Größter Hebel bei Bedienung: ein Zähler statt fünf, Aufgabe + Antwortfeld immer sichtbar, ein Hauptknopf je Bildschirm, kurzes „Fertig“ am Ende jeder Sitzung.

---

## A) Bedienung und Ablauf für Kinder und Teenager am Handy

### A1. Kinder und Teenager (Forschung)
- [G] NN/g, Kinder-Körperentwicklung: Für ab ca. 9 Jahren sind feinmotorische Fähigkeiten gut entwickelt, ab ca. 11 Jahren können Kinder dieselben Interaktionen wie Erwachsene. Bei Touch: große, klar sichtbare Tasten; Handlung auf mehr als einem Weg ermöglichen (antippen oder ziehen). https://www.nngroup.com/articles/children-ux-physical-development/
- [G] NN/g, Teenager (13–17): zielstrebig, erwarten Bedienbarkeit wie Erwachsene; lesen ungern lange Texte (jüngere Teens besonders), mögen scannbare Seiten und kurze Sätze, stören sich an kleiner Schrift; sie sind ungeduldig bei Ladezeiten und lehnen Babyhaftes ab; viele nutzen nur das Handy, daher sind Ziehen-und-Ablegen, kleine Ziele und Hover schwierig; ältere Geräte und langsame Verbindungen sind häufig. https://nngroup.com/articles/usability-of-websites-for-teenagers
- [G] Studiengröße: 38 Teilnehmer 13–17 (Erstfassung); die Berichte gibt es in mehreren Auflagen, der Volltext ist kostenpflichtig, ich habe nur die freien Zusammenfassungen gelesen. https://www.nngroup.com/reports/teenagers-on-the-web/ [?] Zahlen zur Lesemenge (Wörter je Bildschirm) stehen im freien Teil nicht.
- [G] NN/g empfiehlt, Kinder und Teenager als getrennte Zielgruppen zu behandeln und Inhalte eng auf die Altersgruppe zuzuschneiden. https://www.nngroup.com/topic/young-users/
- [G] Sesame Workshop (Vorschule, über 50 Touchscreen-Studien): Antippen ist am natürlichsten, Wischen und Ziehen schwieriger; Teilabschluss unterstützen. Nur Vorschulalter; für 11 und 14 Jahre nur begrenzt übertragbar [A]. https://appleinsider.com/articles/12/12/24/sesame-workshop-wants-to-improve-ipad-apps-for-kids-with-free-developer-guidelines ; https://joanganzcooneycenter.org/?p=19607
- [?] Konkrete Sesame-/Cooney-Center-Regeln für 11- bis 14-Jährige: nicht gefunden.
- [M] Folgerung 11 vs. 14: gleiche Bedienlogik, aber zwei Tonlagen. Der 11-Jährige verträgt Maskottchen, Sticker, Sprechblasen; der 14-Jährige braucht nüchterne Sprache, kleinere Belohnungsanimationen, Zahlen statt Sticker. Umsetzbar als Einstellung je Kind („Ton: verspielt / sachlich“) ohne zwei Apps [A].

### A2. Tippflächen, Schrift, Lesemenge
- [G] WCAG 2.2 SC 2.5.8 (AA): Ziele mindestens 24 × 24 CSS-Pixel (Ausnahmen bei Abstand); SC 2.5.5 (AAA): 44 × 44. https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- [G] Apple 44 pt, Google Material 48 dp (ca. 9 mm). https://ixdf.org/literature/article/how-to-use-tappability-affordances ; https://developer.apple.com/design/tips
- [M] Regel für die App: alle Tasten und Knöpfe ≥ 48 px hoch; Abstand ≥ 8 px zwischen Gegensätzen („Prüfen“ und „Löschen“ nicht nebeneinander). Haupttext Aufgabe 18 bis 20 px, Nebentext nie unter 14 px (NN/g: kleine Schrift stört Teens). Konkrete Pixelzahlen sind meine Empfehlung [M], WCAG schreibt keine Schriftgröße vor.
- [?] Wörter je Aufgabenbildschirm als Richtwert: keine seriöse Zahl gefunden. [M] Faustregel: Aufgabe in höchstens 2 bis 3 Zeilen am Handy; mehr nur bei Textaufgaben, dann Aufgabe zum Scrollen, Antwortfeld fest unten.

### A3. Hauptaktion, Zähler, Fortschritt
- [G] Duolingo: Während der Lektion nur eine Leiste oben, Antwort, danach unten ein Rückmeldefeld mit „Weiter“ (Beschreibungen mehrerer Fallstudien und Screenshot-Sammlung). https://screensdesign.com/apps/duolingo-language-lessons/?via=growthgems ; https://squid-kale-yte2.squarespace.com/work/duolingo (Dritte, keine Duolingo-Quelle)
- [G] Duolingo fragt beim Abbrechen einer Lektion nach (Bestätigungsfenster). https://medium.com/@assenavseolb/dissecting-duolingos-design-f1113a1db8cd (Fallstudie Dritter)
- [G] Duolingo hat die Startseite zu einem einzigen Pfad umgebaut, weil Lernende unsicher waren, was „richtig“ zu tun ist; Anbieterblog. https://blog.duolingo.com/new-duolingo-home-screen-design
- [G] Khan Academy hat die Klassenumgebung auf „Tagesmission/Wochenmission“ umgebaut: Lernende sehen, was als Nächstes dran ist; Anbieter. https://support.khanacademy.org/hc/articles/46056261189773 ; https://blog.khanacademy.org/?p=21322
- [G] Khan nutzte früher „N richtig in Folge“, wechselte zu „N Aufgaben, über 70 % richtig“, weil „in Folge“ als zu unnachgiebig galt (Lehrer-, Eltern-, Lernendenrückmeldungen). https://support.khanacademy.org/hc/fr/community/posts/115000834112 Das betrifft direkt „1 von 3 in Folge“ in der App [M]: Die Regel ist für das Kind hart und der Zähler zeigt sie ständig.
- [?] Studie, wie viele gleichzeitige Fortschrittsanzeigen Kinder verkraften: nicht gefunden. [M] Eigene Regel: höchstens eine Fortschrittsanzeige im Übungsbildschirm, höchstens zwei auf dem Startbildschirm (aktuelle Reise, Sterne).

### A4. Rückmeldung, Fehler, Ladezustände
- [G] Desmos (Designleitfaden): Rückmeldung soll deuten statt nur „richtig/falsch“ sagen, also zeigen, wie die Antwort verstanden wurde; Lernende sollen ohne Bewertung neu ansetzen können. https://blog.desmos.com/articles/desmos-guide-to-building-great-digital-math-2021/
- [G] Brilliant: Aufgabe kann mit „Start over“ neu begonnen werden; richtige Antwort färbt das Feld grün mit Haken; Fehler dienen laut Anbieter dazu, die Gedanken sofort zu überarbeiten. https://brilliant.org/help/features/how-do-i-use-interactives-on-brilliant/ ; https://brilliant.org/resources/choosing-brilliant/how-brilliant-teaches-math/
- [G] Duolingo nutzt konsequent Farbe (grün/rot) plus Ton; Fallstudie Dritter. https://uxplanet.org/analyzing-duolingo-from-product-design-perspective-after-400-days-of-non-stop-practice-c4d4809bdb37 [M] Für Farbsehschwäche nie Farbe allein: Symbol und Wort („Richtig“, „Nicht ganz“) zusätzlich (WCAG SC 1.4.1 „Nutzung von Farbe“, nicht abgerufen, [A] aus Kenntnis).
- [G] Photomath klappt Schritte standardmäßig zu und lässt sie aufklappen. https://www.designrush.com/best-designs/apps/photomath (Design-Rezension Dritter) Das passt zu „Erklärung ansehen“ als freiwillig.
- [G] Ladezeiten, NN/g: 0,1 / 1 / 10 Sekunden (siehe Befund 3). https://www.nngroup.com/articles/response-times-3-important-limits/ 2 bis 10 s: kleiner laufender Zähler oder Spinner; über 10 s: Fortschritt in Prozent und Abbrechen.
- [G] Brilliant-App-Store-Rezensionen nennen „Ladeanimation lief ewig“ und abgeschnittene Zahlen/Bilder auf kleinen Bildschirmen als Ärger. https://apps.apple.com/za/app/id913335252 ; https://apps.apple.com/pl/app/id913335252?l=en-gb (Einzelstimmen)
- [?] Schwelle, ab der Kinder in Lern-Apps abbrechen: keine kinderspezifische Zahl gefunden. NN/g sagt nur „Teenager hassen Warten“ ohne Sekundenwert. [M] Ziel: Prüfen-Antwort ≤ 1 s (Server) sichtbar; sonst Spinner.

### A5. Navigation, „Wo bin ich?“, Sitzungsanfang/-ende, Ton, Bewegung, Dunkel, Querformat
- [G] „Wo bin ich?“: Duolingo-Pfad und Khans „Wie passt dies in die Reise“-Ansicht (Mastery und Aufgabenkontext) zeigen Ort im Ganzen: https://support.khanacademy.org/hc/nl/articles/10629803091853 [M] Deine Reisekarte mit Breadcrumb „Welt > Europa“ leistet das schon gut (kj-reisekarte-1280).
- [G] Klares Ende: My Math Academy (Vorschule, Anbieter) nutzt ein Tagesziel von 15 Minuten mit Fortschrittsleiste, die sich füllt, und Pokal am Ende; Wochenziel 60 Minuten in mehreren Einheiten. https://support.aofl.com/hc/en-us/articles/22106927848973-What-does-the-progress-bar-in-My-Math-Academy-and-My-Reading-Academy-track ; https://educate.zendesk.com/hc/en-us/articles/4402719111447-How-much-time-should-students-spend-using-My-Math-Academy [A] Übertragbar als „Tagesziel erfüllt, Schluss für heute“.
- [G] Bewegung: WCAG 2.3.3 (AAA): von Interaktion ausgelöste, nicht notwendige Bewegung muss abschaltbar sein; CSS-Medienabfrage `prefers-reduced-motion`. https://w3.org/WAI/WCAG21/Understanding/animation-from-interactions Flugzeug-Animation, Konfetti, „Flip“-Tafel brauchen diese Abschaltung [M].
- [?] Töne: keine belastbare Studie für 11–14-Jährige gefunden. [M] Standard stumm oder leise, Ton nur einschaltbar; im Zug/Hotel/Unterricht stört Ton.
- [?] Dunkler Modus: kein belastbarer Lernbefund gefunden. [A] Reine Komfortfrage; deine App hat Tag/Nacht bereits (Vorschauen -nacht-).
- [?] Querformat für Rechen-Apps: keine Studie gefunden. [M] Querformat nur sinnvoll mit geteilter Ansicht (Aufgabe links, Zahlenfeld rechts), sonst sehr wenig Höhe; Tablet-Nutzung (820/1280 px) trägt das.
- [G] Farbsehschwäche und Lesetempo: Sparx bietet farbige Overlays für Lesehilfe an (Elternhandbuch einer Schule). https://www.cotham.bristol.sch.uk/_site/data/files/parents/96D916356D23A08A1487C1A222407719.pdf [M] Mindestens: Symbol + Text zusätzlich zur Farbe, genug Kontrast (WCAG 1.4.3 AA 4,5:1, [A] nicht nachgemessen).

---

## B) Vorbilder im Detail

Quellenlage: Beschreibungen aus Hilfeseiten, App-Store-Texten und Fallstudien Dritter. Eigene Screenshot-Sicht: nicht möglich.

| Vorbild | Start | Übungsbildschirm | Rückmeldung | Abschluss/Fortschritt | Eingabe am Handy | Quellen |
|---|---|---|---|---|---|---|
| Duolingo [G, Dritte] | Pfad mit Knoten, ein „Start“ | oben Leiste, eine Aufgabe, unten ein großer Knopf | Feld unten grün/rot mit Wort und Ton, „Weiter“ | Zusammenfassung mit Daten, Serie | Antippen/Wortbausteine statt Tippen (Wortbank) | screensdesign, uxplanet, Duolingo-Blog |
| Brilliant [G] | Kurs/Lektion, Einstiegsaufgabe prüft Niveau | interaktive Grafik, Aufgabe, Antwortfeld | Feld grün + Haken; Neustart-Knopf | XP, Serie, Ligen | Mathetastatur unter der Aufgabe: Ziffern, Rechenzeichen, Bruch, Wurzel, Pfeile; blau umrandetes aktives Feld | Hilfeseite, screensdesign |
| Khan Academy [G] | Tages-/Wochenmission (neu), Kurs, Einheiten | Aufgabe, Hinweis, Lösung zeigen; Mastery-Stufen | Rückmeldung nach jeder Aufgabe | Stufen „Versucht, Vertraut, Fähig, Gemeistert“ | [?] nicht geprüft | Khan-Blog/-Support |
| Sparx Maths [G] | Hausaufgabe der Woche (Pflicht, XP-Boost, Ziel, freies Üben) | Aufgabe, Video-Hilfe unten, Bookwork-Code | sofort; Hilfevideo | Fortschritt gegen 100 % | Eingabe über „Answer“; Form [?] | Schulhandbuch (Cotham), tief-7 |
| Anton [G] | Fach/Klasse, angepinnte Aufgaben | [?] | direkt | Sterne/Spiele | [?] | App-Store, Brandenburg-Folien |
| Photomath [G] | Kamera | Schritte zugeklappt | aufklappbar | – | Foto, Taschenrechner | designrush, App-Store |
| bettermarks, Mathegym | siehe tief-1 | siehe tief-1 | siehe tief-1 | siehe tief-1 | siehe tief-1 | tief-1 |
| Mathspace, Beast Academy, Math Academy, DragonBox | [?] | [?] | [?] | [?] | [?] | nicht belastbar gefunden |

Einzelheiten:
- Brilliant [G]: Die Mathetastatur erscheint unter der Aufgabe; Ziffern 0–9, Plus, Minus, Mal, Bruch- und Wurzeltaste, Pfeile zum Springen, Löschen oben in der Ecke. Aktives Feld blau. Mehrere Felder: erst antippen, dann tippen. Ob die Tastatur Teile der Aufgabe verdeckt, sagt die Seite nicht [?]; Rezensionen nennen abgeschnittene Texte/Widgets auf kleinen Geräten [G, Einzelstimmen]. https://brilliant.org/help/features/how-do-i-use-interactives-on-brilliant/
- Brilliant, Start: Einstieg mit echten Matheaufgaben statt Fragebogen; Ladeanimationen themenbezogen (screensdesign). https://screensdesign.com/showcase/brilliant-learn-by-doing
- Sparx [G]: Eltern können über das Kinderkonto schauen; Parent-Ansicht zeigt Hausaufgaben unter „Compulsory“, Genauigkeit und Themen, bei denen das Kind Mühe hat; Bookwork mit Foto-Upload des Rechenwegs. https://www.cotham.bristol.sch.uk/_site/data/files/parents/96D916356D23A08A1487C1A222407719.pdf
- Sparx-Regel für Eltern [G, Schulbrief]: Kind soll allein arbeiten, nur Videos nutzen; zu viel Hilfe lässt Aufgaben zu schwer werden. https://perins.net/?p=9451
- Anton [G]: gratis und werbefrei; Offline-Lernen, mehr Avatar-Optionen und Spiele sind „Plus“. https://apps.apple.com/DE/app/id1180554775 Lehrkräfte können Übungen „anpinnen“, der Pin erscheint beim Öffnen der App: https://www.friedrich-verlag.de/friedrich-plus/sekundarstufe/mathematik/konzepte-methoden/dezimalzahlen-mit-der-anton-app-13110 [A] Vorbild für „Auftrag vom Lehrer = ein Pin auf dem Start“.
- IXL [G]: Real-Time Diagnostic, Eltern-/Schülerberichte mit „nächsten Schritten“; Live-Klassenbericht warnt Lehrkräfte, wenn Kinder den Test durchklicken. https://blog.ixl.com/?p=19287 ; https://blog.ixl.com/?p=14625
- Was bewusst nicht auf dem Übungsbildschirm steht [A, aus Beschreibungen]: Duolingo und Brilliant zeigen während der Aufgabe keinen Gesamtstand, keine Punktesumme, keine Navigation; Photomath klappt Erklärungen zu. Belastbar nur als Beschreibung Dritter, nicht als Designaussage der Anbieter.
- Zahlen-/Formeleingabe ohne Verdecken [?]: Eine Quelle, die genau das (Layoutregel) beschreibt, habe ich nicht gefunden. [M] Technisch lösbar: Aufgabe und Antwortfeld im sichtbaren Bereich über der Tastatur verankern (visualViewport/`100dvh`), Tastatur nur 4 Reihen, Aufgabentext scrollbar.

---

## C) Seite für Eltern und Lehrkraft

### C1. Was Auswertungen zeigen
- Sparx [G]: wöchentliche E-Mail mit aktuellem Hausaufgabenstand und Link zur Detailseite, Link 21 Tage gültig; Schulen mit Eltern-E-Mail haben im Schnitt etwa 15 % höhere Abschlussquote (Anbieter). https://support.sparxmaths.com/en/articles/342337-why-and-how-we-engage-parents-with-sparx-maths ; die E-Mail sagt dem Elternteil je nach Stand eine von drei Handlungsempfehlungen (Schulbrief, https://docs.google.com/document/d/1IMTgOviFRNjTY8NvHeINhBEjWeb2cJQ7/export?format=pdf).
- bettermarks/Mathegym [G, tief-1]: „Eingaben ansehen“ (Rechenweg des Kindes), Lücken-Liste, Wochenpensum, Statistik per Mail.
- IXL [G]: Diagnostik-Stufen je Thema, Schülerbericht mit nächsten Schritten für Eltern. https://blog.ixl.com/2023/07/17/how-to-track-your-childs-progress-on-ixl/
- Math Academy [G]: Aufsichtsfenster („oversight panel“), Tages- und Wochenmeldungen, Weitergabe an Tutor/Lehrer; Mindestrhythmus 3 bis 5 Tage. https://www.mathacademy.com/faq
- Khan [G, Anbieter]: Lehrkräfte sehen Stufen der Meisterschaft je Fertigkeit; Effekt-Daten nach Minuten pro Woche. https://blog.khanacademy.org/?p=18194
- Mathspace: [?] nicht belastbar gefunden.
- Fernschulen [G, sucher-d]: Einsendeaufgaben mit Lehrerkorrektur und Notenschnitt, Zeugnis auf Anfrage. Kein Dashboard.

### C2. Forschung zu Lern-Dashboards
- [G] Systematische Übersicht von 50 Studien zu lehrerseitigen Dashboards (Kaliisa et al. 2023): Die meisten Dashboards sollen Lehrkräften etwas bewusst machen, bieten aber wenig Handlungsmöglichkeiten; geringe Nutzung in der Praxis; Lehrkräfte werden meist nur früh in der Problemfindung beteiligt. https://link.springer.com/10.1186/s41239-023-00394-6
- [G] Schwendimann et al. 2017 (55 Arbeiten): Forschung noch jung, meist Machbarkeitsstudien; es fehlen Langzeitstudien im echten Einsatz und Vergleiche verschiedener Gestaltungen. https://infoscience.epfl.ch/record/220672
- [G] Kaliisa/Saqr (38 Studien): wenig belastbare Belege, dass Dashboards Lernergebnisse verbessern. https://arxiv.org/pdf/2312.15042
- [?] Studie, welche Angaben Eltern in Heimbeschulung tatsächlich nutzen: nicht gefunden. [A] Die Dashboard-Studien betreffen Hochschule/Schule mit Lehrkräften, nicht Eltern.
- [M] Folgerung: Wenig Zahlen, jede mit klarem „und jetzt?“. Nur so entsteht eine 5-Minuten-Wochenprüfung. Detailansichten (Lehrplan-Matrix) bleiben zweite Ebene für die Lehrerstunde.

### C3. Wie berichten gute Systeme über Fehler, Zeit, Lücken, Prüfungsreife?
- Fehler: bettermarks „Top 5 der fehlerhaften Aufgaben“, „Eingaben ansehen“ [G, tief-1]; Sparx: Themen mit Schwierigkeiten [G]. Deine „Was wackelt?“ mit echten falschen Antworten ist besser als alle Prozentwerte [M].
- Zeit: Khan/MMA zählen Minuten pro Woche; MMA pausiert Zeitzählung nach 5 Minuten Inaktivität [G]. https://support.aofl.com/hc/en-us/articles/24136148512397 [M] Gute Idee: aktive Minuten, nicht Zeit „App offen“.
- Lücken: bettermarks Wissenslücken; IXL Diagnostik [G].
- Prüfungsreife: [?] keine bewährte Darstellung gefunden; Khan nutzt „Skills to Proficient“ als Maß. https://blog.khanacademy.org/?p=13201 [M] Für die Rückkehr nach Bayern ist „Prozent des Lehrplans der Klasse n gesichert“ plus Hinweis „Lücken in Klasse n−1“ die ehrlichste Angabe (hast du bereits: Stand Kl. 7/8/9).

---

## D) Technik-Erwartungen

- [G] Schwellen 0,1 / 1 / 10 s (NN/g); Teens hassen Warten (NN/g Teens). Quellen oben.
- [?] Kinderspezifische Abbruchschwellen: nicht gefunden.
- [G] Muster „offline zuerst“ (Entwicklerberichte, kein Standardwerk): lokal speichern, Oberfläche sofort aktualisieren, Aktion in Warteschlange, Service Worker mit Background Sync, Wiederholung mit zunehmendem Abstand (1, 2, 4, 8, 16 bis max. 30 s). https://blog.logrocket.com/offline-first-frontend-apps-2025-indexeddb-sqlite/ ; https://alamb-hex.github.io/blog/2026/01/21/building-true-offline-first-pwas ; https://dev.to/imamabubakar/building-for-bad-internet-the-architecture-behind-apps-that-still-work-4df4 Beides sind Blog-Beiträge von Praktikern [A: geringe Beweiskraft, aber Technik ist Standard].
- [G, Einzelbericht] Ein Praxisbericht nennt Verlust von 18 % wartender Sync-Aufträge durch Netzwechsel und Nutzer, die Mobilfunk sparen: https://kubaik.github.io/offline-first-apps-what-3g-markets-taught-us/ [?] Quelle schwach, nur als Hinweis auf Risiko.
- [G] Anton: Offline-Lernen existiert als Plus-Funktion; Photomath-Rezensionen beklagen, dass Netz nötig ist. https://apps.apple.com/jo/app/id1180554775 ; https://apps.apple.com/ZA/app/id919087726
- [?] Wie Lern-Web-Apps in Regionen mit schwachem Netz (z. B. Khan Academy Lite, Kolibri) genau vorgehen: nicht geprüft; ich habe sie nicht abgerufen.

---

## E) Selbst organisiertes Lernen: Tag und Woche

- [G] Bayern: In einer Stundentafel-Zeile für ein Gymnasium steht Mathematik 4 4 4 3 4 3 3 (Jgst. 5 bis 11); andere Zweige haben andere Werte, Zuordnung der Zeile nicht eindeutig. https://www.gymnasiale-oberstufe.bayern.de/download/4-23-12/stundentafeln_fr_die_jahrgangsstufen_5_bis_11_gso%20%281%29.pdf ; amtlich: https://www.gesetze-bayern.de/Content/Rtf/BayGSO-ANL_1?all=False [A] 3 bis 4 Wochenstunden zu je 45 Minuten, also 135 bis 180 Minuten Unterricht je Woche.
- [G] Khan: 30+ Minuten/Woche ≈ 20 % mehr Zuwachs als erwartet; nur etwa 9 % der Stichprobe erreichten diese Menge; mittlere Nutzung in einer Studie 10 bis 15 Min./Woche. https://blog.khanacademy.org/?p=18194 ; https://blog.khanacademy.org/national-study-in-top-journal-finds-khan-academy-learning-gains-after-accounting-for-key-unmeasured-factors/ [A] Das ist Ergänzung zum Unterricht, nicht Ersatz.
- [G] Math Academy (Anbieter): 20 bis 40 XP pro Tag, 3 bis 5 Tage; ältere Daten: 50 bis 60 Minuten/Tag als Obergrenze des dauerhaft Machbaren. https://www.mathacademy.com/faq ; https://justinmath.com/what-is-the-highest-sustainable-daily-xp-on-math-academy/
- [G] DreamBox (Anbieter): Klasse 6–8 60 bis 90 Minuten/Woche. https://www.pcsb.org/cms/lib/FL01903687/Centricity/Domain/11500/2019-2020%20Using-DreamBox-At-Home-PI-2018-08.pdf
- [G] Fernschule ILS (aus sucher-d): ZFU-Eintrag Klasse 7: 30 Std./Woche Selbstlernen für alle Fächer. Für nur Mathe nicht aufgeschlüsselt [?].
- [G, Erfahrungsberichte] Reisefamilie: bis zu einer Stunde/Tag Mathe, zeitlich flexibel. https://worldtravelfamily.com/homeschooling-schedules-maths Weltreise-Familie: 10 bis 15 Stunden Wochenpaket je Kind, Mathe als ein Teil. https://mykareinsch.journoportfolio.com/worldschooling/articles/our-favorite-formula-for-worldschooling-time-management/ [?] Seriöse Studien zu Heimbeschulung auf Reisen mit konkreten Mathezeiten: nicht gefunden; nur Erfahrungsberichte.
- [G] Modulares Lernen (Substack, Erfahrung): 1 bis 2 Stunden/Tag für 1:1-Beherrschungsarbeit, Rest freies Lernen. https://teachyourkids.substack.com/p/whats-a-typical-homeschool-day-look

Vorschlag (siehe auch Lieferung 7).

---

## LIEFERUNG 1: Befund zu den Vorschaubildern

Angesehen: 14 Bilder in la/ und ab/: kj-reisekarte-400, kj-reisekarte-1280, kj-nb-uebung-400, kj-nb-fertig-400, kj-start-400-tag, kj-sj-kl8-400, 0872-ansage-360 (dunkel), ab-etappe-direkt-tag-400, ab-flug-tag-400, kj-lehrer-stand-400, kj-lehrer-stand-820, la3-wackelt-400, kj-lehrer-lehrplan-1280, kj2-lehrer-1280. Alles Sicht auf Vorschaubilder, nicht auf die laufende App; Verhalten (Tastatur, Animation) kann abweichen [A].

1. **kj-reisekarte-400** (Handy, Karte)
   - Gut: echte Karte, Flaggen-Pins, Breadcrumb „Welt > Europa“ = klares „Wo bin ich?“ (Duolingo-Pfad/Khan-Kontext). Gelber Hauptknopf groß, dunkle Schrift, gut lesbar.
   - Stört: drei Aktionsleisten verbrauchen rund ein Viertel der Höhe; der orangene „Weiter nachbessern >“ ist fast so wuchtig wie der gelbe, also zwei Hauptknöpfe. Dazu „Weiter in Samarkand >“ als dritter „Weiter“-Knopf. Texte abgeschnitten („Nachbessern: Welc…“, „Zusatz: Terme umf…“).
   - Stört: viele Zusatzzeichen: Zoom +/−, Vollbild, Standort, Info; Abzeichenzahlen an den Pins (2, 3, 4, Haken) und Sterne 340 oben, Kopf mit drei kleinen Symbolen. Fünf bis sieben Zahlen/Symbole gleichzeitig [M: gegen „eine Hauptaktion“].
2. **kj-reisekarte-1280** (Rechner/Tablet)
   - Gut: Karte links, Seitenleiste mit „Nachbessern“, „Gerade dran“, „Zusatz“ lesbar; mehr Platz hilft, Text nicht abgeschnitten.
   - Stört: gleiche zwei Hauptknöpfe (orange über gelb). Reihenfolge: das Nachbessern steht oben und gewinnt optisch, obwohl die Vorgabe „ein Hauptknopf“ heißt.
   - Gut: Erklärsätze am Knopf („Etwa 3 Minuten“, „Deine Sterne bleiben“) senken Abbruchangst; das ist besser als bei Sparx/bettermarks beschrieben [M].
3. **kj-nb-uebung-400** (Übungsbildschirm)
   - Stört stark: Oben fünf Bedienzeilen (Kopf „Rom“, einzelnes Menü, ×, Reiter Erklären|Üben 5|Fehler 1, Etappenleiste mit Pfeilen) bevor die Aufgabe beginnt; die Aufgabe beginnt erst etwa bei der Hälfte der Höhe. Fünf gleichzeitige Zähler: „Üben 5“, „Fehler 1“, „Etappe 1/3“, drei Kreise, „1 von 3 in Folge“, „Bordkarte 1“. Verstoß gegen eine Fortschrittsanzeige (Duolingo/Brilliant).
   - Stört stark: Das Zahlenfeld nimmt rund ein Drittel der Höhe und schneidet die Aufgabenkarte ab (am Rand ragt noch eine Stellenwertzeile „T H Z E“ unter der Tastatur hervor). Das Antwortfeld ist nicht sichtbar [A: könnte unter der Tastatur liegen].
   - Gut: Tasten ≥ 60 px hoch (WCAG/Apple erfüllt), großer gelber „Prüfen“-Knopf in Daumenreichweite, Aufgabe groß.
   - Stört: Minus und Komma auf der Tastatur, obwohl die Aufgabe („Wert der Ziffer 2 in 182 887“) beides nicht braucht; zwei Tasten weniger = größere Ziffern [M].
4. **kj-nb-fertig-400** (Nachbessern geschafft)
   - Gut: ein Ereignis, ein Knopf („Weiter nachbessern: Zahlenstrahl“). Ehrlicher Satz: wird in den nächsten Lerntagen nochmals abgefragt.
   - Stört: Die Mitte des Bildschirms ist leer (großer Verlauf); der weiße Fließtext oben auf hellorangem Grund hat vermutlich zu wenig Kontrast [A: nicht gemessen]. Sticker „Süper repariert!“ mit schrägem Ton und „?“-Zeichen: 11-Jähriger okay, 14-Jähriger eher peinlich (NN/g Teenager).
5. **kj-start-400-tag** (lange Startseite „Abflugtafel“)
   - Stört stark: etwa 2 240 px lang, mehr als zehn Blöcke; mindestens acht Einstiege (Nachbessern, Expedition, Einsteigen, Zusatz, Route, Erklärungen, Karte, Menü). Gegen „eine Hauptaktion“.
   - Stört: Der schwebende gelbe „Einsteigen ROM >“ liegt mitten auf dem Inhalt und überdeckt Text (Karte „Terme umformen“). „Yo Digga!“-Sticker überlappt Titel und Sterne. Vier Fortschrittsarten (Etappenzähler, Prozentring 26 %, „2 von 15 Flügen“, Stempel).
   - Gut: Kachel „Nachbessern“ mit Zeitangabe und Beruhigung; Aufbau oben nach Wichtigkeit.
6. **kj-sj-kl8-400** (Schuljahr-Ansicht, Klasse 8)
   - Gut: kleines nächstes Ziel („Nächstes Ziel: 10 % – nur noch 1 Etappe!“) ist motivierend und konkret (endowed-progress-Prinzip, Fallstudien; [A] keine harte Studie gelesen).
   - Stört: wieder schwebender „Einsteigen“-Knopf, der die Kacheln GYM/RS/MYP verdeckt; drei Schulsysteme (Gymnasium, Realschule, MYP) in Prozent parallel; für ein Kind unnötig.
7. **0872-ansage-360** (dunkel, 360 px)
   - Gut: Dunkelmodus vorhanden, Kontrast hoch, „Erst 9 Bordkarten Check-in · ca. 5 Min.“ = Zeitangabe vorab (gut für Sitzungsbeginn).
   - Stört: Die Tafelschrift „ROM“ ist als „R O“ mit abgeschnittenen Zeichen zu sehen (Animationsmoment oder Fehler) [A]; Knopf „Weiter geht’s >“ unten abgeschnitten (Bildausschnitt, daher offen).
8. **ab-etappe-direkt-tag-400** (Etappe geschafft)
   - Gut: „Du kannst jetzt: Ziffern nach ihrem Stellenwert lesen“ (Kann-Satz statt nur Punkte), ein gelber Knopf mit Unterzeile „Etappe 2 von 3“, kleines „Pause – zur Abflugtafel“ als klarer Ausstieg. Das ist das beste Ende einer Sitzung im Satz.
   - Stört: „Etappe 1 von 3“, „2/2“, „Etappe 2 von 3“, „+10“ Sterne, Abzeichen „Direkt“ = vier Zahlen. Flugzeug-Animation braucht Bewegungsabschaltung (WCAG 2.3.3). Graue Kleinschrift („Neues Abzeichen …“) wirkt klein [A].
9. **ab-flug-tag-400** (Flug geschafft)
   - Gut: Liste „Das kannst du jetzt“ mit drei Haken; „Überspringen“ oben; Knopf „Weiter zum nächsten Thema“ mit Sublabel; Sekundärlink „Test ansehen“.
   - Stört: Die fünf Chips „nach 1 Lerntag · 3 · 7 · 14 · 30“ erklären Wiederholungsplanung, die ein Kind nicht braucht; „820 Sterne“ groß neben „340“ auf der Karte [A: Zahl verwirrt]. Zu viel Text für den Moment nach einem Erfolg.
10. **kj-lehrer-stand-400** (Eltern, Überblick am Handy)
    - Gut: „Gerade dran“ zuerst, „Diese Woche“ mit rotem Streifen: „0 Lerntage, 30 Bordkarten, 73 % richtig, zuletzt am 14.11.“ ist die wichtigste Karte (Rhythmus + Qualität).
    - Stört: Daten wirken widersprüchlich („0 Lerntage“ bei „30 Bordkarten“) [A: Vorschaudaten oder Zählfehler, prüfen]. Leere Karte „Zuletzt geschafft: Noch kein Flug“ frisst Platz. „Stand Kl. 8“ hat 10 Zahlen (3 Ringe, 6 Nebenringe, 3 Textzeilen): Überforderung (Dashboard-Befunde Kaliisa).
    - Stört: Obere Leiste „Council | Reisen | Lernen“ vermischt Entwicklerwerkzeug und Elternseite; vier Reiter (Überblick/Wackelt/Stand/Plan) laufen am Rand ab (Vergleich la3-wackelt-400).
11. **kj-lehrer-stand-820** (Tablet)
    - Gut: Zweispaltige Karten, mehr Überblick; „Zuletzt geschafft“ weiterhin leer.
    - Stört: untere Hälfte leer, während „Was wackelt“ gar nicht im Überblick erscheint. Es müsste die zweite Karte sein [M].
12. **la3-wackelt-400** (Was wackelt?, Handy)
    - Gut: echte falsche Antworten („Runde 929 773 auf Tausender. Antwort 929 000 · richtig: 930 000“), Kurzregel „Ab 5 wird aufgerundet“, „Erneut besprochen ✓“, Satz „Diese Woche: 30 Bordkarten, 22 richtig, 4-mal mit Tipp · 2 Lerntage“. Das ist bettermarks‘ „Eingaben ansehen“ und Sparx‘ Schwierigkeitenliste im Kern.
    - Stört stark: Tabellenspalten brechen Wörter senkrecht („Rund en“, „wac kelt“, „bes pro chen 18.1 1.“); Textkasten ragt am rechten Rand über. Am Handy muss die Tabelle zu Karten werden.
13. **kj-lehrer-lehrplan-1280** (Lehrplan-Matrix)
    - Gut: Thema × Klasse mit Fahrplan links und Detail rechts löst deinen Wunsch „Plan, Stand, Lehrplan an einer Stelle“ größtenteils (Detail zeigt Stand je Etappe).
    - Stört: Spaltenbreite („Fahrpla n“ bricht um), Abzeichen-Wust („Gym 8 · RS 7 · IB 4“, Platz 3a bis 3d), viele Farben (gelb, braun, blau, grün). Für fünf Minuten nicht geeignet; als Lehrerstunden-Werkzeug ja [M].
14. **kj2-lehrer-1280** (gleiche Ansicht mit Detailfeld)
    - Gut: Etappen mit Text „gelandet / offen / freiwillig“ zusätzlich zur Farbe (Farbsehschwäche), Knöpfe „Als Nächstes · Ans Ende · Aus dem Plan“ direkt am Detail.
    - Stört: Detailfeld deckt die Matrix halb zu; Schließen-Knopf klein.

---

## LIEFERUNG 2: Zielbild Übungsbildschirm am Handy (360 bis 400 px), von oben nach unten

Grundregeln [M, begründet]: eine Hauptaktion; ein Fortschrittsanzeiger; Aufgabe und Antwortfeld immer sichtbar; Rückmeldung am Ort der Aufgabe (Duolingo unten, Brilliant im Feld, Desmos deutend); Erklärung freiwillig (Photomath klappt zu).

1. **Kopfzeile (48 px):** links ×-Knopf (Tippfläche 48 px; bei Tipp Rückfrage „Pause? Dein Stand bleibt.“ wie Duolingos Bestätigung); Mitte eine einzige Leiste mit Segmenten (z. B. 5 bis 6 Aufgaben der Etappe); rechts ein „?“-Knopf (Erklärung ansehen, öffnet Bogen). Weg: zweite Zeile mit Hamburger-Menü, Zeile „Rom“, Reiter Erklären|Üben|Fehler, Etappenleiste mit Pfeilen, Link „Erklärung ansehen“.
2. **Kontextzeile (klein, nur Text, 13 bis 14 px):** „Rom · Natürliche Zahlen · Etappe 1/3“. Kein Knopf. Hier darf die Etappen-Info stehen, aber kein weiterer Zähler.
3. **Aufgabenkarte:** Text 18 bis 20 px, höchstens 3 Zeilen sichtbar, danach Scrollen innerhalb der Karte; Bild/Zahlenstrahl darunter, wenn nötig. Kein „Bordkarte 1 · Rom“-Etikett.
4. **Antwortfeld:** direkt unter der Aufgabe, sichtbar umrandet, 56 px hoch, große Ziffern, aktiv hervorgehoben (Brilliant: blauer Rahmen). Nie unter der Tastatur: Layout mit `visualViewport`/`dvh` so bauen, dass Aufgabe + Feld über der Tastatur bleiben [A: technisch machbar, nicht getestet].
5. **Tastatur:** vier Reihen: 1 2 3 / 4 5 6 / 7 8 9 / 0 · ⌫ · Prüfen (Prüfen gelb, doppelt breit). Komma und Minus nur bei Aufgaben, die sie brauchen. Tasten ≥ 48 px, Abstand 8 px; Gesamthöhe ca. 230 bis 250 px (derzeit ca. 280 px bei 5 Reihen). Bruch/Wurzel nur nach Aufgabenart (Brilliant macht das so).
6. **Rückmeldung nach „Prüfen“:** Die Tastatur gleitet nach unten weg; an ihrer Stelle erscheint ein Blatt mit Symbol, Wort und Farbe zugleich:
   - richtig: „Richtig“ (Haken, grün), Knopf „Weiter“;
   - nicht ganz: „Nicht ganz“ (neutral warm, kein Alarmrot), Zeile „Richtig wäre: 930 000“ und eine Kurzregel („Ab 5 wird aufgerundet“, wie in deiner „Was wackelt?“), Knopf „Weiter“. Die Antwort des Kindes bleibt oben sichtbar (Desmos: deuten statt nur werten).
   - Antwortzeit: Prüfen reagiert in ≤ 1 s mit Spinner im Knopf (NN/g); nach 10 s Hinweis „Verbindung langsam. Antwort gespeichert.“
7. **Nachbessern:** Die drei Kreise ersetzen die Segmentleiste an derselben Stelle (kein zusätzlicher Zähler). Regel „3 richtig in Folge“ nur dort; sonst Khans Wechsel auf „N von M richtig“ prüfen [M].
8. **Ende der Etappe:** eigener Abschlussbildschirm (siehe ab-etappe-direkt-tag-400): Kann-Satz, ein gelber Knopf, kleiner Ausstieg „Pause“. Stern-Zahl klein; keine Chips für Wiederholungstage.
9. **Querformat/Tablet:** zweigeteilt: Aufgabe + Feld links, Tastatur rechts, Leiste als dünner Streifen oben.
10. **Ton/Bewegung:** Standard leise; Bewegung beachtet „Bewegung reduzieren“ (WCAG 2.3.3).
11. **Ältere Kinder:** Einstellung „sachlich“: weniger Sticker, kurze Rückmeldewörter, Zahl statt Maskottchen (NN/g Teens).

Begründung nach Vorbild: Duolingo (oben Leiste, unten Rückmeldung + Weiter), Brilliant (Tastatur unter der Aufgabe, aktives Feld sichtbar, Neustart), Desmos (Rückmeldung deutet), Photomath (Erklärung zugeklappt), Khan (Zählregel „in Folge“ wurde entschärft), NN/g (Teens: wenig Text, keine kleine Schrift, kein Kindisches), WCAG/Apple/Google (Tippfläche).

---

## LIEFERUNG 3: Zielbild Start/Reisekarte

- **Eine Startseite: die Reisekarte.** Die Abflugtafel (2 240 px) wird zur Liste „Alle Flüge“ hinter dem Menü; kein schwebender Knopf über Inhalten.
- **Oben (48 px):** Zurück, Breadcrumb „Welt > Europa“, Sterne (klein), Menü.
- **Mitte:** Karte mit Flaggen-Pins; Pins nur drei Zustände (erledigt, jetzt, offen); Abzeichen-Zahlen an Pins nur bei „jetzt“. Zoom per Pinch; Knöpfe +/− nur auf großen Bildschirmen.
- **Unten fest (eine Karte, ca. 120 px):** „Bologna · 3 von 6“ mit sechs Punkten und **ein** gelber Knopf. Beschriftung folgt der Regel „Hauptknopf führt zum richtigen nächsten Schritt“: Ist Nachbessern fällig (kurz, ≤ 3 Min.), heißt er „Weiter: Nachbessern (ca. 3 Min.)“; sonst „Weiter in Bologna“. Es gibt nie zwei große Knöpfe.
- **Nebenwege (eine Zeile aus drei kleinen Knöpfen unter der Karte, nur Text + Symbol, 48 px):** „Extra-Flug (1)“ (früher Zusatz; nur wenn Eltern eingeplant), „Merkheft“, „Mein Weg“. Reisepass/Stempel über „Mein Weg“. Erklärungen ansehen: im Merkheft, nicht auf dem Start.
- **Sitzungsbeginn:** Beim Öffnen steht in der Karte eine Zeitangabe („ca. 20 Min. für heute“), wie bei „Erst 9 Bordkarten … ca. 5 Min.“.
- **Sitzungsende:** Tagesziel erfüllt → Karte wird zu „Fertig für heute“, Hauptknopf wechselt zu „Morgen weiter“ (nicht gesperrt: „Noch eine Etappe“ als kleiner Link). So sieht das Kind ein klares Ende (My Math Academy: Leiste voll + Pokal) [A, übertragen aus Vorschulprogramm].
- **Weg mit:** „Yo Digga!“-Sticker, drei Schulsystem-Prozente (nur Eltern sehen sie), „Was kommt wann wieder?“ (Eltern/Merkheft).

---

## LIEFERUNG 4: Zielbild Eltern-/Lehrerseite

### 4a. Die eine Übersicht je Kind (höchstens sieben Angaben, Handy untereinander, 5 Minuten)
Kopf: Name, Stand „Gym Kl. 8“. Navigation: nur zwei Reiter „Woche“ und „Plan“; „Council/Reisen“ raus aus dieser Leiste.
1. **Lerntage:** „3 von 4 Soll-Tagen“ (Ampel: grün ≥ Soll, gelb −1, rot −2 oder mehr; Ampelschwellen sind Meinung [M]).
2. **Aktive Minuten diese Woche** gegen Ziel (z. B. 128 von 160), ohne Leerlauf (MMA zählt nur aktive Zeit).
3. **Etappen geschafft diese Woche** und was dran ist („Lineare Ungleichungen, Etappe 3/7; danach …“).
4. **Richtig ohne Hilfe** in Prozent mit Pfeil zur Vorwoche (z. B. 73 % ↘ 78 %).
5. **Was wackelt:** Zahl der Themen + das oberste mit echtem Beispiel („Runde 929 773 → 929 000, richtig 930 000“).
6. **Stand im Lehrplan:** eine Zahl (Gym Kl. 8: 9 %) + „Lücken aus Kl. 7: 2 Themen“. Realschule/MYP nur im Detailreiter.
7. **Tempo:** „Kl. 8 fertig am voraussichtlich [Datum]“ bei Wochendurchschnitt; ersetzt vier Zeilen „noch x von y Flügen“.
Darunter ein Knopf „Tischkarte öffnen“ und einer „Plan ändern“. Die Lehrplan-Matrix bleibt Detail (Reiter „Plan“), für die Lehrerstunde. Begründung: Dashboard-Befunde (wenige Angaben, je Angabe eine Handlung), Sparx/Math Academy (Rhythmus + Qualität + Lücken).

### 4b. Wochenbericht per Nachricht (Sonntagabend, ca. 8 Zeilen, ein Link)
```
Woche 47 · Kind A (Kl. 8)
Lerntage 3/4 · 128 Min. · 11 Etappen
Richtig ohne Hilfe: 73 % (Vorwoche 78 %)
Wackelt: Runden (2 von 5 richtig). Beispiel: 929 773 auf Tausender → 929 000, richtig 930 000.
Dran: Lineare Ungleichungen 3/7 · Stand Gym 8: 9 %
Tempo: Kl. 8 fertig ca. 14.06. bei diesem Tempo
Vorschlag: 10 Min. Gespräch (Tischkarte) → [Link]
```
Regeln [M]: höchstens eine Zahl je Zeile, Wörter statt Tabellen, Link statt Anhang. Sparx-Vorbild: Mail mit Handlungsvorschlag und Link zur Detailseite; auch Math Academy mit Tages-/Wochenmeldungen [G, oben].

### 4c. Tischkarte (zehn Minuten Gespräch, von der App vorbereitet)
Aufbau [M]:
1. **2 Min. Kind erzählt:** Frage von der App: „Was war diese Woche leicht, was zäh?“
2. **3 Min. Eine Wackel-Aufgabe:** App zeigt eine echte falsche Antwort des Kindes + richtige Lösung + Kurzregel; Frage an das Kind: „Warum kommt hier 930 000 heraus?“ Elternteil darf nicht vorrechnen, nur nachfragen (Sparx-Prinzip: Hilfe verfälscht die Anpassung [G, Schulbrief]). Nach dem Gespräch „Erneut besprochen ✓“.
3. **3 Min. Erklär-es-mir:** Das Kind erklärt eine neu gelernte Etappe mit eigenen Worten an einem Beispiel; die Karte zeigt die richtige Lösung für den Elternteil.
4. **2 Min. Plan:** Zwei Fragen: „Passt das Tempo?“ und „Wann sind die vier Lernzeiten?“; Knopf „Zeiten eintragen“.
Für Lehrerstunde: Karte „für Lehrkraft“ mit den drei obersten Wacklern (mit echten Antworten), Minuten, Plan-Fragen und Platz für Notizen/Aufträge („Ändern lassen“). Belege: bettermarks „Eingaben ansehen“, Sparx-Elternbrief, vorhandene „Erneut besprochen“-Funktion deiner App [G].

---

## LIEFERUNG 5: Die zehn Änderungen mit größtem Nutzen je Aufwand [M, Reihenfolge nach Nutzen/Aufwand]

| # | Änderung | Nutzen | Aufwand [A] |
|---|---|---|---|
| 1 | Zahlenfeld verdeckt die Aufgabe: Aufgabe + Antwortfeld über die Tastatur verankern, Minus/Komma nur bei Bedarf | sehr hoch | klein bis mittel |
| 2 | Übungsbildschirm entrümpeln: Kopf auf eine Zeile, Reiter und Etappenleiste weg, eine Fortschrittsleiste | sehr hoch | mittel |
| 3 | Nur ein Hauptknopf je Bildschirm (Karte, Start): Nachbessern zum Hauptknopf umlabeln, nicht zwei große Knöpfe | hoch | klein |
| 4 | Schwebenden „Einsteigen“-Knopf nicht über Inhalt legen; Abflugtafel hinter Menü (nur Liste) | hoch | klein bis mittel |
| 5 | „Was wackelt?“ am Handy als Karten statt Tabelle; Reiterleiste ohne Abschnitt am Rand | hoch (Eltern) | klein |
| 6 | Eltern-Übersicht auf sieben Angaben kürzen; „Was wackelt“ in den Überblick; Entwickler-Leiste raus | hoch | mittel |
| 7 | Rückmeldung als Blatt unten: Symbol + Wort + Farbe, Kurzregel bei Fehler; Spinner nach 1 s | hoch | mittel |
| 8 | Tagesziel mit klarem Ende („Fertig für heute“); Abschlussbildschirm schlanker (Kann-Satz, ein Knopf, keine Wiederholungs-Chips) | hoch | klein |
| 9 | Bewegung abschaltbar + Ton standardmäßig aus; Ton der Ansprache je Kind einstellbar (14-Jähriger sachlich) | mittel | klein bis mittel |
| 10 | Eingabe nie verlieren: lokal zwischenspeichern, Wiederholung bei Netzabbruch, Statusanzeige | hoch bei Reise | mittel |

Danach: Wochenbericht + Tischkarte (mittel), Offline-Paket pro Etappe (groß).

---

## LIEFERUNG 6: Empfehlung zum Umgang mit schlechtem Netz [M, Technik nach gängigen Mustern; nicht an deiner App getestet]

Stufen nach Aufwand:
1. **Nichts verlieren (zuerst):** Tippt das Kind „Prüfen“, wird die Antwort sofort lokal gespeichert (inkl. Aufgaben-ID, Zeit) und im Feld sichtbar gelassen. Schlägt die Anfrage fehl: kleine Statusanzeige „Keine Verbindung. Antwort gespeichert, wird gesendet.“ Wiederholung mit wachsendem Abstand (1, 2, 4, 8 … max. 30 s) [G, Muster]. Der Server bleibt Richter; nur „gespeichert“ erscheint, nicht „richtig“.
2. **Reaktionszeit sichtbar machen:** nach 1 s Spinner im Knopf, nach 10 s Text „Langsam. Du kannst weiterüben, wir senden gleich.“ (NN/g Schwellen).
3. **Ansichtswechsel beschleunigen:** letzte Ansicht aus dem Speicher zeigen (Skeleton, dann Aktualisierung); Kartenkacheln und App-Gerüst per Service Worker zwischenspeichern [A: Wechsel waren zeitweise langsam, Ursache unbekannt].
4. **Mini-Offline-Paket (nur wenn nötig):** Beim WLAN-Moment die nächsten 5 bis 8 Aufgaben der aktuellen Etappe samt Prüfregel laden; offline lokal prüfen, Ergebnis in die Warteschlange; Server rechnet später den Stand neu. Preis: Antworten stecken im Gerät. Bei eigenen Kindern geringes Betrugsrisiko [A]; Entscheidung des Vaters, da er „der Server prüft jede Antwort“ als Prinzip hat. Anton verkauft Offline-Lernen als eigene Funktion [G], also ein bekanntes Bedürfnis.
5. **Was offline nicht gehen muss:** Wechsel zur Reisekarte, Statistik, Plan ändern. Hier genügt Hinweis „Zuletzt aktualisiert vor 2 Stunden“.
Quellen: LogRocket (offline-first), Praxisberichte (dev.to, alamb-hex), NN/g Antwortzeiten; Beweiskraft der Blogs gering.

---

## LIEFERUNG 7: Tages- und Wochenablauf Mathe auf Reisen [M; Bausteine aus Quellen, Zahlen als Vorschlag]

Ausgangswerte [G/A]: Stundentafel Bayern 3 bis 4 Wochenstunden (≈ 135 bis 180 Min. bei 45 Min.); Khan-Ergänzung ab 30 Min./Woche wirkt; Math Academy 3 bis 5 Tage, 20 bis 40 Min.; Reisefamilien berichten bis zu 1 Std./Tag. Es gibt keine Studie, die „Schule ersetzen“ in Mathe mit Minutenzahl belegt [?].

**Woche**
- 4 App-Tage à 30 bis 35 Minuten (Kind A, Kl. 5, 11 Jahre) bzw. 40 Minuten (Kind B, Kl. 8, 14 Jahre) = ca. 2 bis 2,7 Std. App.
- 1 Lehrerstunde (60 Min.) in der Wochenmitte.
- 1 Tischkarte (10 bis 15 Min.) am Sonntag, wenn der Wochenbericht kommt.
- 1 Papieraufgabe (10 Min.) pro Woche: Kind rechnet im Heft, Foto an Lehrkraft (Sparx-Bookwork-Idee, tief-7) [A].
- Ein fester Pausentag ohne Mathe; Reisetage mit Flug oder Fahrt gelten als Pausentag [M].

**Tag (Sitzung 30 bis 40 Min.)**
1. Start (2 Min.): Hauptknopf zeigt Zeitangabe; Nachbessern zuerst (≤ 5 Min.).
2. Neuer Stoff (15 bis 25 Min.): Erklärung nur nach Bedarf, dann Üben; Pause nach 20 Min. für Kind A.
3. Ende (1 bis 2 Min.): „Fertig für heute“ mit Kann-Satz; nicht gleich die nächste Etappe anbieten.
Immer zur gleichen Uhrzeit (z. B. nach dem Frühstück) [A; „feste Zeit“ als Gewohnheit, keine eigene Studie gelesen].

**Lehrerstunde (60 Min.):** 10 Min. Tischkarte der Woche prüfen; 30 Min. Wackler mit echten Antworten erklären; 10 Min. Papieraufgabe besprechen; 10 Min. Plan/Prüfungsfragen (Rückkehr Bayern: sucher-d).

**Quellen:** Khan https://blog.khanacademy.org/?p=18194 ; Math Academy https://www.mathacademy.com/faq ; My Math Academy (mehrere kurze Einheiten) https://educate.zendesk.com/hc/en-us/articles/4402719111447-How-much-time-should-students-spend-using-My-Math-Academy ; Stundentafel https://www.gesetze-bayern.de/Content/Rtf/BayGSO-ANL_1?all=False ; Reisefamilie https://worldtravelfamily.com/homeschooling-schedules-maths .

---

## Was ich nicht prüfen konnte

- Screenshots/Demos der Vorbilder (Duolingo, Brilliant, Khan, Sparx, Mathspace, IXL, Anton, Photomath, Beast Academy, Math Academy, DragonBox): nur Text- und Fallstudienquellen; Mathspace, Beast Academy, DragonBox, Math-Academy-Oberfläche und Khan-Übungsbildschirm nicht belastbar gefunden.
- NN/g Voll-Berichte (Kinder, Teenager) sind kostenpflichtig; nur freie Artikel gelesen.
- Sesame/Cooney-Center: nur Vorschul-Leitfaden gefunden, nichts für 11 bis 14 Jahre.
- Kinderspezifische Abbruchschwellen, Wortmenge je Bildschirm, Töne, Dunkelmodus, Querformat: keine belastbaren Studien gefunden.
- Forschung zu Elternnutzung von Dashboards (Heimunterricht): nicht gefunden.
- Offline-/Schwachnetz-Vorgehen bestimmter Lernplattformen (z. B. Kolibri): nicht abgerufen; Technikmuster nur aus Blog-Beiträgen.
- Kontrastwerte und Verhalten der Tastatur auf echten Geräten: nicht gemessen (Vorschaubilder).
- WCAG 1.4.1/1.4.3 nicht neu abgerufen (Kenntnis).
- Vorschaubilder zeigen eventuell Testdaten (z. B. „0 Lerntage, 30 Bordkarten“).
