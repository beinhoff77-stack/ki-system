# Tiefen-Sucher 4: Rechenweg prüfen und KI-Tutor mit Schutzregeln

Abruf aller Quellen: 25.11.2026. Nur Websuche und Seitenabruf; nichts angemeldet, gekauft, abgesendet. Keine persönlichen Daten in Suchanfragen.
Kennzeichnung: **[G]** gesichert (Quelle verlinkt, auf der Seite gelesen oder im Suchausschnitt gesehen), **[A]** Annahme, **[M]** Meinung/Bewertung von mir. "Nicht gefunden" heißt: in dieser Recherche nicht auffindbar, nicht dass es das nicht gibt.
Vorgelesen: sucher-b-international.md und sucher-c-offene-quellen.md (dort schon Gesagtes wird nicht wiederholt, nur ergänzt).

---

## 0. Kurzfassung (12 Sätze)

1. [G] Es gibt zwei Familien der Zeilenprüfung: (a) Rechenregeln als Modell (MATHia, FA-Math, Graspable: nur zulässige Umformungen) und (b) Gleichwertigkeitsprüfung beliebig eingegebener Zeilen (Mathspace, ACE, STACK "Equivalence reasoning"). Für eine eigene Web-App ist (b) mit eigenem kleinen Prüfer die machbare Familie.
2. [G] Das einzige offene, gründlich dokumentierte System mit Zeilenprüfung ist STACK (GPL, braucht Maxima-Server und Moodle/ILIAS). Es ist als Vorbild für Teilpunkte und Fehlertypen sehr gut, aber nicht einbettbar in eine Vanilla-Web-App.
3. [G] Numbas und WeBWorK prüfen Terme durch Einsetzen zufälliger Werte; beide haben bekannte Fallen (Definitionslücken, uneinheitliche Stichproben). Das stützt den Plan "Server setzt Werte ein".
4. [G] Kein gefundenes System bewertet "Kontrollzahlen" oder "Zahlen vor x / ohne x"; Vorbilder gibt es nur für Teilideen (Numbas "steps", ASSISTments Scaffolding, Mathspace Zeile für Zeile). Die Idee ist neu; [A] das heißt Pilotieren, nicht Annehmen.
5. [G] Handschrift per KI: sehr gut bei einfacher Arithmetik mit eindeutigem Ergebnis (95 %, Kappa 0,90, ghanaische Mittelstufe), deutlich schlechter bei fehlerhaftem Schülerwerk; 2026 zeigt eine EMNLP-Studie, dass 42 bis 66 % der Abschriften mindestens einen "ausgebesserten" Schülerfehler enthalten (Fehler verschwindet). [M] KI darf nur abschreiben; das Urteil muss ein deterministischer Prüfer fällen, die Abschrift muss der Mensch bestätigen.
6. [G] Bastani u. a.: Der Tutor mit Schutzregeln erhielt Lösung und typische Fehler im Prompt und gab nur schrittweise Hinweise; Prüfungsleistung ohne KI war nicht besser als Kontrolle (Differenz -0,004, nicht signifikant), der freie Chat -17 %.
7. [G] Der bisher beste Beleg für "KI-Tutor hilft wirklich" ist die Eedi/Google-Studie (N=1179, 12 bis 15 Jahre): Hilfe nach Fehlern = Mensch-Tutor-Niveau bei Folgeaufgaben, aber kein Effekt im Standardtest (Star Maths). Dort prüfte ein Mensch jede Nachricht; 94,7 % wurden unverändert freigegeben.
8. [G] Fehlerquoten: Bastani-Chat ohne Lösung im Prompt (GPT-4, 2023/24) nur 51 % richtig; Eedi-Audit mit Kontext: 0,24 % Kontextfehler je Nachricht. [M] Heißt: Hinterlegte Lösung ist der Hebel, nicht das Modell.
9. [M] Reihenfolge nach Nutzen je Aufwand: Kontrollzahlen, dann "erste falsche Zeile" (zuerst Zahlenterme Klasse 5 und lineare Gleichungen Klasse 8), Lückenweg, Selbstkontrolle als Notlösung, Foto+KI zuletzt als Pilot.
10. [M] "Erste falsche Zeile" braucht keine große Bibliothek: ein 100-Zeilen-Parser, exakte Bruchrechnung (BigInt) und Einsetzen von etwa 20 festen Werten; bei linearen Gleichungen sogar exakt über Lösungsmengen.
11. [G] plv8 (JavaScript in Postgres) ist bei Supabase mit Postgres 17 nicht mehr enthalten; [M] die Prüfung deshalb entweder rein in SQL über Koeffizienten, in plpgsql oder in einer Edge Function mit derselben JS-Datei wie im Browser.
12. [M] KI-Erklärer: nur Umformulierung vorab geprüfter Bausteine, keine freie Chat-Eingabe des Kindes, Zahlen-Weißliste in der Ausgabe, Hinweisstufen mit Zähler, nie im Prüfungsmodus.

---

## A) Systeme mit Rechenweg-Prüfung

### A1 STACK (stack-assessment.org), gründlich

| Frage | Antwort |
|---|---|
| Lizenz | [G] Open Source, GPL ("world-leading open-source (GPL) automatic assessment system", https://moodle-sciences-24.sorbonne-universite.fr/question/type/stack/doc/doc.php). Maxima ist ebenfalls Open Source (CAS im Hintergrund). Ilias-Variante: https://github.com/HochschuleLuzern/assStackQuestion. [A] GPL heißt: Code in eigene App kopieren zieht GPL nach sich; als getrennter Dienst unklar, Rechtsfrage. |
| Technik | [G] Moodle-Fragetyp (https://docs.moodle.org/403/en/STACK_question_type) und ILIAS-Plugin; braucht Maxima auf dem Server (lokal oder GoeMaxima/MaximaPool), GNUplot, MathJax. PHP. Nicht einbettbar in eine Vanilla-JS-App; nicht offline. |
| Eingabe der Zeilen | [G] Beim Eingabetyp "Equivalence reasoning" tippt das Kind Zeile für Zeile in ein Textfeld, Syntax mit `*`, Gleichungen mit "or"-Verknüpfung für mehrere Lösungen; bei Termumformung beginnt jede neue Zeile mit `=` (https://docs.stack-assessment.org/en/Students/Equivalence_reasoning/). Mengen, Listen, Matrizen nicht erlaubt. Formeleditor ist nicht Teil (MathJax nur Anzeige). |
| Gleichwertigkeit prüfen | [G] Computeralgebra (Maxima). Prototyp laut Moodle-Doku: Differenz student minus Lösung vereinfachen und auf 0 prüfen. Bei Zeilenfolge: Benachbarte Zeilen müssen gleichwertig sein; bei Termen = gleicher Wert bei Einsetzen, bei Gleichungen = gleiche Lösungen mit gleicher Vielfachheit (Studentenseite oben). Der Antworttest `EquivFirst` prüft zusätzlich, dass die erste Zeile die Aufgabenzeile ist (https://docs.stack-assessment.org/en/Authoring/Answer_Tests/Results/EquivFirst/). Weitere Tests: AlgEquiv, EqualComAss, CasEqual u. a. (https://docs.stack-assessment.org/en/Authoring/Answer_Tests/Equivalence/). |
| Definitionsbereich | [G] Der Eingabetyp verfolgt "natürliche Definitionsmengen" und zeigt sie in der Rückmeldung; stille Erweiterungen der Definitionsmenge (z. B. Kürzen) lässt er derzeit durchgehen (https://docs.stack-assessment.org/en/Specialist_tools/Equivalence_reasoning/Equivalence_assessment/). |
| Reichweite | [G] "bewusst relativ einfach": Polynome in einer Variablen, sehr einfache Ungleichungen, einfache Gleichungssysteme; keine Logarithmen/Trigonometrie (https://docs.stack-assessment.org/en/Specialist_tools/Equivalence_reasoning/). Das deckt Klasse 5 bis 8 weitgehend ab, [A] Bruchgleichungen Klasse 8 sind Grenzfall. |
| Potential response trees (PRT) | [G] Gerichteter azyklischer Graph aus Knoten. Jeder Knoten vergleicht zwei Ausdrücke mit einem Antworttest; Zweig "wahr/falsch" kann die Punktzahl setzen/addieren/abziehen, Rückmeldung anhängen, einen Antwortvermerk (answer note) für die Lehrkraft erzeugen und den nächsten Knoten benennen. Der Baum läuft nur bei gültiger Eingabe (https://docs.stack-assessment.org/en/Authoring/Potential_response_trees/). |
| Fehlertypen erkennen | [G] Pro erwartetem Fehler ein eigener Knoten, den der Autor schreibt. Beispiel: Knoten 1 `Int` prüft Stammfunktion und liefert automatische Rückmeldung zu typischen Fehlern (fehlende Konstante, differenziert statt integriert), Knoten 2 `FacForm` prüft nur die Form "faktorisiert", ohne Punktabzug (https://docs.stack-assessment.org/en/AbInitio/Authoring_quick_start_3/). Automatische Fehlererkennung gibt es nur in einzelnen Tests, sonst Handarbeit. |
| Teilpunkte | [G] Der Baum liefert Rohpunktzahl 0 bis 1; Zweige können Zwischenwerte setzen (z. B. Teilpunkte bei fehlender Konstante). Summe über alle Bäume. |
| Folgefehler | [G] Nicht eingebaut; Numbas schreibt dazu, bei STACK müsse die Folgefehlerlogik jedes Mal von Hand in die Knoten gebaut werden (https://www.numbas.org.uk/behind-the-design/marking.html). |
| Kosten einer Hilfe | [G] Strafe pro verschiedenem gültigen, nicht vollständig richtigen Versuch, Standard 0,1; Strafen addieren sich, behalten wird der beste strafbereinigte Wert (Potential-response-trees-Seite oben). Eine Hinweis-Kosten-Logik wie in Numbas "steps" habe ich bei STACK nicht gefunden. |
| Ungewöhnliche Wege | [G] Gleichwertigkeitsprüfung akzeptiert jeden gleichwertigen Weg. Einschränkung: Ein "falscher, aber gleichwertiger" Schritt (z. B. beide Seiten radizieren) ist nicht prüfbar; die Doku rät, Wurzelziehen zu vermeiden und `a^2-b^2=0` zu faktorisieren. |
| Bekannte Probleme | [G] Trennung von Gültigkeit und Richtigkeit: Syntaxfehler kosten keine Punkte (Philosophie-Seite, Sorbonne-Spiegel); Lernkurve für Autoren; Eingabe per Tastatur mit Computer-Syntax (`*`). [A] Am Handy zäh; nicht mit Handschrift. |

### A2 Numbas

- [G] Prüfung "mathematical expression": Es werden zufällige Werte für die freien Variablen gewählt und Schüler- und Musterterm dort ausgewertet (https://docs.numbas.org.uk/en/latest/question/parts/mathematical-expression.html). Zusatz: "Pattern restriction" (Form prüfen, z. B. gekürzt/faktorisiert). Die Form wird sonst nicht beurteilt.
- [G] Falle laut Doku: Hat die Musterlösung eine Singularität oder ist für manche Werte nicht definiert, muss der Autor einen sicheren Prüfbereich oder einen eigenen Wertegenerator festlegen. Ein Nutzerforum beschreibt Fehlurteile, wenn zufällige Einsetzungen beide Seiten unbrauchbar machen (https://groups.google.com/g/numbas-users/c/zUH8VG32QMY).
- [G] Hilfe/Schritte: "Steps" sind Unteraufgaben, die das Kind per Knopf aufdeckt; Punkte werden dann skaliert, Beispiel: 6 Punkte mit Abzug 2 und Antwort mit 3 Punkten ergibt 2 Punkte (https://docs.numbas.org.uk/en/latest/question/parts/reference.html).
- [G] Folgefehler: "adaptive marking" ersetzt Fragevariablen durch die Antwort des Kindes aus früherem Teil und markiert den späteren Teil damit; der Autor sagt selbst, was als "Folgefehler" gilt, sei schwer festzulegen, und rät, erwartete Fehler als alternative Antworten einzutragen (https://www.numbas.org.uk/blog/2015/07/adaptive-marking-based-on-answers-to-other-question-parts/, https://numbas.org.uk/behind-the-design/adaptive-marking.html).
- [G] Eingabe: JME-Syntax, Vorschau der Eingabe in Formelschrift. Zeilenweise Gleichwertigkeit eines ganzen Rechenwegs: nicht gefunden.
- Lizenz: **nicht verifiziert** (nicht gelesen). [A] Der Code ist auf GitHub öffentlich (marking_scripts/jme.jme laut Doku), Lizenz vor Nutzung prüfen.
- [M] Als Lesestoff für die eigene Einsetz-Prüfung nützlich; nicht einbinden.

### A3 WeBWorK

- [G] Formelantworten werden durch Auswerten an zufällig gewählten Testpunkten verglichen; sind an allen Testpunkten beide Seiten undefiniert, erscheint "Can't generate enough valid points for comparison", der Autor muss Intervalle setzen (https://webwork.maa.org/wiki/FormulaTestPoints). Anzahl Testpunkte, Grenzen und Toleranz sind einstellbar (https://webwork.maa.org/wiki/Answer_Checkers_and_the_Context).
- [G] Bekannte Falle: In älteren Versionen wurden bei jedem Absenden andere Punkte gezogen, deshalb war dieselbe Antwort mal richtig, mal falsch (https://webwork.maa.org/moodle/mod/forum/discuss.php?d=3508). [M] Lehre: feste, deterministische Testpunkte je Aufgabe.
- Rechenweg Zeile für Zeile: nicht gefunden. Lizenz: nicht gelesen.

### A4 Möbius (früher Maple T.A., DigitalEd)

- [G] Kommerziell. Maple-gestützte Fragen mit "response-equivalence checker", Teilpunkte durch Maple-Code, mehrere oder unendlich viele richtige Antworten (https://www.digitaled.com/support/help/admin/Content/INST-AUTHORING/QUESTION-TYPES/Author-Maple-graded-question.htm). Vorgeführt wird, dass sowohl vereinfachte als auch ausmultiplizierte Form als richtig gilt (https://eams.ncl.ac.uk/sessions/2021/optimising-maths-with-mobius/slides.pdf).
- Preis, Zeilenprüfung, Handy: nicht gefunden. [M] Für eine Familie nicht relevant (Hochschul-Lizenz).

### A5 Mathspace (StepSmart)

- Eingabe [G]: Tastatur oder Handschrifterkennung (App-Beschreibung https://apps.apple.com/app/id1445097311); laut Schülerleitfaden Handschrift nur in der iPad-App (Auszug abgeschnitten, https://content.govdelivery.com/attachments/VAEDUFCPS/2023/06/05/file_attachments/2516566/FCPS%20Student%20Guide%202023.pdf).
- Prüfung: [G] "Math Engine" prüft jeden Schritt; wie (CAS, Regeln, Stichproben), steht nicht auf den Hilfeseiten: **nicht gefunden**.
- Rückmeldung [G] (https://help.mathspace.co/immediate-feedback): hohles grünes Häkchen = richtiger Zwischenschritt auf empfohlenem Weg, punktiertes grünes Häkchen = richtig, aber nicht auf empfohlenem Weg (dann kein schrittbezogener Hinweis, Hinweis fällt auf den letzten empfohlenen Schritt zurück), graues Fragezeichen = mathematisch ungültige Eingabe (kostet keine Punkte), graues Kreuz = gültig, aber falsch (einzige Eingabe, die Punkte kostet), rotes "Schritt übersprungen" = Kind forderte den nächsten Schritt an (kostet Punkte). Ob normale Hinweise Punkte kosten, steht dort nicht.
- Ungewöhnliche Wege [G]: gültige Schritte werden akzeptiert, auch ohne vorgesehenen Weg; gelegentlich wird ein gültiger Schritt fälschlich als falsch markiert (Meldeknopf); Kinder dürfen Zwischenschritte auch weglassen und nur das Endergebnis eingeben, außer wo Zwischenschritte wesentlich sind (https://help.mathspace.co/en/articles/3624564-can-different-methods-be-used-to-answer-questions).
- Prüfungsmodus [G]: "Test Mode" schaltet Hinweise und Schrittrückmeldung ab; nach Abgabe liest eine KI die Zeilen und vergibt Punkte für Methode inklusive Folgefehler-Punkten ("follow-through marks"); Lehrkraft kann jede Entscheidung überschreiben; Begründung je Punktevergabe für Schüler sichtbar; Funktion in Beta (https://help.mathspace.co/test-mode). Genauigkeitsangaben: nicht gefunden. [M] Das ist das nächste Vorbild zum geplanten "Papier-Maßstab".
- Probleme: [G] Abhängigkeit von Schrittrückmeldung (Common Sense, siehe sucher-b). Eingabefrust: ungültige Eingaben werden getrennt gemeldet und nicht bestraft, das mildert ihn.

### A6 Graspable Math

- [G] Eingabe durch Ziehen/Gesten auf dem dargestellten Term oder Tastenfeld; Umformungen sind nur erlaubt, wenn sie gültig sind; Lehrkraft sieht Schritt-für-Schritt-Arbeit live (https://sites.google.com/view/gmactivities). Es wird also nicht eine freie Zeile geprüft, sondern Gleichwertigkeit entsteht durch die Bedienung.
- Teilpunkte, Folgefehler, Hilfe-Kosten: nicht gefunden. Förderung durch IES (SBIR) bestätigt, unabhängige Wirkung: nicht gefunden (https://ies.ed.gov/use-work/awards/graspable-math-activities-increasing-algebra-proficiency-dynamic-notation-technology?ID=3276). Verwandte Studie "From Here to There!" (Ottmar-Gruppe): Beide Gruppen (Notation vs. ASSISTments-Aufgaben) verbesserten ihr Verständnis (https://par.nsf.gov/servlets/purl/10443581); Details nicht gelesen.
- [M] Am Handy gut (Gesten), aber für "Heft + App" unpassend: Das Kind rechnet ja auf Papier.

### A7 ASSISTments (Scaffolding)

- [G] Bei falscher Antwort oder auf Wunsch: Hinweisfolge, deren letzter Hinweis die Antwort nennt ("bottom-out hint"), oder "Scaffolding": das Problem wird in Teilfragen zerlegt, die einzeln beantwortet werden (https://www.cse.unr.edu/~sjose/Papers%20Referenced/Student%20modeling%20in%20an%20Intelligent%20Tutoring%20System.pdf, https://web.cs.wpi.edu/~mfeng/pub/feng_heffernan_JILR.pdf).
- Kosten einer Hilfe [G]: Standardwertung zählt nur den ersten Versuch; wer einen Hinweis anfordert, gilt als falsch (https://web.cs.wpi.edu/~nth/pubs_and_grants/papers/2011/FLAIRS/Wang-24_ITS_draftv8.pdf). In der Hinweisreihe sinkt die Gutschrift mit jedem weiteren Hinweis (https://digital.wpi.edu/downloads/zg64tq423?locale=en). Skill Builder: Meisterschaft = drei richtige in Folge (https://pmc.ncbi.nlm.nih.gov/articles/PMC6310403).
- Eingabe: Antwortfelder/Auswahl; Gleichwertigkeitsprüfung freier Zeilen: nicht gefunden.
- [G] Wirkungsbeleg RCT siehe sucher-b. [M] Die Idee "Hilfe genutzt = Aufgabe zählt nicht als gelöst" ist hier am klarsten belegt als Praxis.

### A8 FA-Math (Singapur, Student Learning Space)

- [G] "Regelbasierte" Engine mit zeilenweisen Hinweisen, Rückmeldung und vorgeschlagenen Punkten; erzeugt zufällige Aufgaben, unterstützt Geometrie und Graphen (https://www.learning.moe.edu.sg/about/ai-in-sls/aied-features/feedback-assistant-mathematics/). Punkte werden auf 0,5 aufgerundet (Teacher-Guide-Auszug, https://www.learning.moe.edu.sg/teacher-user-guide/assess/add-mathematics-feedback-assistant/).
- Eingabe, Gleichwertigkeitsverfahren, Folgefehler, Kosten: **auf den abgerufenen Seiten nicht angegeben**. Zugang nur für Schulen im SLS [A].

### A9 ACE-Learning "Math StepByStep AutoGrading"

- [G] Eingabe per Tastatur oder Handschrifterkennung; jede Zeile wird geprüft und erhält graues Kreuz (falsch), orangenes Häkchen (Zwischenschritt) oder grünes Häkchen (Endergebnis); andere Methoden sind erlaubt; vollständige Musterlösung vorhanden (https://lms.ace-learning.com/app/math-stepbystep-autograding). Die Engine fragt nach "einfachster, ausmultiplizierter oder faktorisierter Form" nach (https://www.asiabusinessoutlook.com/business/vendor/ace-learning-driving-needed-innovation-in-math-learning-deliverability-cid-4238.html).
- Verfahren der Gleichwertigkeitsprüfung, Teilpunkte, Preis: nicht gefunden. Ein Gast-Zugang mit 50 Fragen je Thema existiert (nicht ausprobiert, Anmeldung vermieden).

### A10 Carnegie MATHia (Cognitive Tutor)

- [G] Zwei Mechanismen: "Model tracing" (jedes Kind-Handeln wird gegen ein Regelmodell gedeutet, mit Fehlregeln "buggy rules" für typische Fehler, die Fehlerrückmeldung auslösen; alternative Lösungswege werden durch zusätzliche Regeln abgedeckt) und "Knowledge tracing" (Fertigkeitsstand, Bayes; wählt die nächste Aufgabe) (https://nap.nationalacademies.org/read/10297/chapter/6; Erklärung der Fehlregeln: https://arxiv.org/pdf/1202.4828).
- Eingabe: Felder je Schritt im Aufgabenarbeitsblatt, nicht frei geschriebene Zeilen [A]. Hilfe: mehrere Hinweisebenen, Daten enthalten "Hint Level Change" (DataShop-Dokumentation).
- [M] Aufwand: Regelmodell je Fertigkeit von Experten; für eine Familie nur als Prinzip ("typische Fehler als benannte Regel") übertragbar.

### A11 Mathegym (deutsch)

- [G] Elternflyer: Komplexe Aufgaben können Schritt für Schritt mit Rückmeldung nach jedem Einzelschritt gelöst werden, mit Erklärvideos und Hilfen (https://cdn.mathegym.de/docs/Mathegym-Flyer-Eltern-2023.pdf). Verfahren, Eingabe, Teilpunkte, Preis: nicht gefunden. [A] Zerlegung in vorgegebene Teilaufgaben, nicht freie Zeilen; nicht geprüft.

### A12 Photomath, Mathpix, MyScript (Handschrift zu Formel)

- Photomath: [G, aus sucher-b nur Drittseite] Lösungsanzeige; hier nicht weiter geprüft, widerspricht dem Ziel "ohne Hilfe". Nicht recherchiert.
- Mathpix [G]: OCR-API ab 0,002 USD je Anfrage (Text/Bild und Strichdaten "digital ink" gleicher Satz, https://mathpix.com/pricing/api); Snip-App mit kostenloser Stufe, Pro-Stufe ab 4,99 USD/Monat laut Dritt-Portalen (https://mathpix.com/pricing, https://www.gappsy.com/tools/mathpix/). Im UC-Irvine-Test (Analysis, Studierende) 55 % brauchbare Abschriften auf einer schwierigen Teilmenge, GPT-4.1-mini 84 % (https://arxiv.org/html/2603.00895v1).
- MyScript: SDK-Preis nicht öffentlich gefunden (sucher-c); Offline im Web nicht belegt.
- [M] Beide liefern nur die Abschrift (LaTeX). Prüfung der Gleichwertigkeit müsste die App selbst leisten.

### A-Querschnitt: Wie wird Gleichwertigkeit geprüft? (Tabelle)

| Verfahren | Systeme | Stärke | Schwäche |
|---|---|---|---|
| Computeralgebra (vereinfachen, Differenz = 0) | STACK, Möbius, [A] Mathspace | Exakt, erkennt Form | Server/Lizenz, Fehlentscheidungen bei Definitionslücken |
| Einsetzen zufälliger Werte | Numbas, WeBWorK | Einfach, offline, schnell | Definitionslücken, zufällige Streuung; Gleichungen brauchen Zusatzlogik |
| Regelbaum / Fehlregeln | MATHia, FA-Math | Erklärt den Fehler | Experten-Aufwand je Fertigkeit |
| Zulässige Umformung durch Bedienung | Graspable | Fehler unmöglich | passt nicht zu Papier |
| KI liest Zeilen | Mathspace Test Mode (Beta) | Folgefehler, beliebige Wege | Genauigkeit unbelegt, Datenschutz, Kosten |

---

## B) Technik-Bausteine

| Baustein | Lizenz | Größe | Offline | Reife | Typische Fallen |
|---|---|---|---|---|---|
| **MathLive** `<math-field>` | MIT [G] (https://npmjs.com/package/mathlive) | npm-Paket entpackt 5,52 MB (Version 0.105.2, inkl. Schriften, Töne, Varianten) [G]; Größe nur der min.js: nicht gemessen. Schriften und Töne liegen in eigenen Ordnern, Pfad über `fontsDirectory`/`soundsDirectory`, `null` verhindert Laden [G] (https://mathlive.io/mathfield/guides/integration/) | [A] Ja, wenn Dateien lokal liegen; nicht von mir getestet | Aktiv gepflegt (Versionen 0.105 bis 0.110 in 2025), Version 0.x | Virtuelle Tastatur nimmt auf 360 px viel Platz [A, nicht getestet]; Ausgabe LaTeX/MathJSON, Dezimalkomma-Tastatur eingestellt in 0.98 [G]; Mehrdeutigkeit `3/4x` (Bruch oder Bruch mal x) muss man aus der Struktur lesen, nicht aus LaTeX-Text |
| **CortexJS Compute Engine** | MIT [G] | Laut Paketdienst ca. 1,1 MB minifiziert, ca. 296 KB gzip (Version dort 0.59.0; aktuell lt. jsDelivr 0.136.2, Größe daher [unsicher]) [G] (https://depscope.dev/pkg/npm/%40cortex-js/compute-engine, https://www.jsdelivr.com/package/npm/@cortex-js/compute-engine) | [A] Ja (reines JS) | Version 0.x, Schnittstelle änderte sich merklich [A, aus Versionssprung] | `isEqual()` wertet nur aus und vergleicht Zahlen; `(x+1)^2` gegen `x^2+2x+1` liefert dort `undefined`, "keine Entwicklung, keine Vereinfachung, kein Sampling" [G]; `isIdenticallyEqual()` nutzt Entwicklung, Vereinfachung und Stichproben, nur "starker Hinweis, kein Beweis", ebenfalls dreiwertig [G] (https://epsil.dev/compute-engine/guides/symbolic-computing/). [M] Für Gleichwertigkeit also nicht blind auf `isEqual` verlassen; `undefined` als eigenen Zustand behandeln |
| **math.js** | Apache-2.0 [G] | Voll-Bundle 185 kB min+gzip (v14.3.1); Teil-Bundle über Tree-Shaking möglich [G] (https://mathjs.org/download.html, https://mathjs.org/docs/custom_bundling.html) | [A] Ja | Reif, sehr verbreitet | `simplify` ist nicht kanonisch; `simplify(a-b)==0` darf nicht als Gleichwertigkeitstest dienen [A, aus Doku-Hinweis: Vereinfachung hängt von Regeln ab, https://mathjs.org/docs/expressions/algebra.html]. Für exakte Brüche Datentyp `Fraction` verwenden [A, Datenklasse existiert laut Doku] statt Gleitkomma |
| **Algebrite** | MIT [G] | Repo 3,55 MB (kein Bundle-Maß) [G] | [G] "selbstständig, ohne Server" (sucher-c) | Letzter Push 23.06.2023, 88 offene Issues [G] (https://awesome.ecosyste.ms/projects/github.com%2Fdavidedc%2FAlgebrite): wenig gepflegt | Eigene Ausgabeformen ("cons"-Objekte); Gleichwertigkeitstest nicht vorgesehen |
| **Nerdamer / nerdamer-prime** | MIT [G] | Bundle-Größe: nicht gefunden | [A] Ja | Original archiviert April 2023, Fork "nerdamer-prime" aktiv (https://npmjs.com/package/nerdamer-prime, https://science.ecosyste.ms/projects/38933); Module Algebra, Calculus, Solve, Extra | Zusatzmodule laden; Gleichungslöser kann Teilmengen/Scheinlösungen eigenwillig behandeln [A, nicht geprüft] |
| **SymPy via Pyodide** | SymPy BSD, Pyodide MPL (sucher-c) | Pyodide-Kern ca. 6,4 MB und 4 bis 5 s Start (ältere Roadmap-Angabe) [G, evtl. überholt] (https://pyodide-ryanking13.readthedocs.io/en/stable/project/roadmap.html); SymPy-Wheel 3,9 MB (1.13.3) [G] (https://anaconda.org/pyodide/sympy/files/manage?type=pypi) | Ja bei Selbsthosting [G, Tutorial https://ian-bmj.github.io/bmj-ai-rapid-prototype/tutorial/pyodide-wasm-tutorial.html] | Reif | Zu schwer für Handy und schlechtes Netz [M]; Ladezeit; Zufallswerte nicht nötig |
| **Maxima/STACK-Anbindung** | GPL | Serverdienst | Nein | Reif | Moodle/ILIAS-Abhängigkeit; fertige Web-API für fremde Apps: nicht gefunden |
| **Postgres-seitig** | | | | | siehe unten |

**Postgres-Seite, Möglichkeiten** [G/A]:
1. [G] `plv8` (JavaScript in der Datenbank) ist auf Supabase bei Postgres 17 nicht mehr enthalten und erhält keine Updates; Supabase empfiehlt Edge Functions (https://supabase.com/docs/guides/database/extensions/plv8, https://supabase.com/changelog/35851-forthcoming-postgres-17-release-notes). Neon hat plv8 aus Sicherheitsgründen gesperrt (https://neon.com/docs/extensions/plv8). [M] Nicht darauf bauen.
2. [M] Variante "nur Koeffizienten": Das Kind tippt je Zeile Zahlen (a, b), die Datenbank rechnet nur mit Brüchen (Zähler/Nenner als `bigint`). Kein Parser nötig, volle Prüfung der linearen Fälle in reinem SQL. Siehe Abschnitt 3.
3. [M] Variante "Mini-Parser in plpgsql": Rekursiver Abstieg, 80 bis 150 Zeilen, machbar aber unbequem zu testen.
4. [M] Variante "Edge Function (TypeScript)": Dieselbe JS-Prüfdatei läuft im Browser (sofortige Rückmeldung, offline) und serverseitig (maßgebliches Urteil). Vorteil: ein Code, ein Testsatz.
5. Fallen [A]: `float8`/`double` nie für Gleichheit nutzen; `numeric` rundet Divisionen (Skala) und kann periodische Brüche nicht exakt halten; deshalb Zähler/Nenner getrennt führen.

---

## C) Handschrift und Foto

### C1 Stand der Technik (veröffentlicht)

| Quelle | Daten | Ergebnis |
|---|---|---|
| Ghana, Mittelstufe, Arithmetik mit eindeutigem Ergebnis, 288 handschriftliche Antworten (https://arxiv.org/abs/2510.05538v1) | multimodale Modelle (Namen im Abstract nicht genannt) | ca. 95 % Genauigkeit, Kappa 0,90 gegen Lehrkräfte; gelegentlich Fehler, die ein Mensch nicht machen würde [G] |
| Dieselbe Studie, 150 Zeichnungen US-Grundschule | | direkt Kappa 0,20, mit menschlicher Bildbeschreibung 0,47 [G] |
| UC Irvine, Analysis, ca. 800 Studierende, 3.945 Antworten (https://arxiv.org/html/2603.00895v1) | GPT-4.1-mini, o3-mini | ca. 88 % der Abschriften brauchbar; Bewertung im Mittel 0,40 Punkte unter Hilfskräften; 68 bis 86 % der Bewertungen innerhalb 1 Punkt; Rückmeldung zu 79,8 % ganz richtig, 10,7 % falsch; Probleme: zu strenge Bewertung gültiger, nicht vorgesehener Wege und zu milde bei "glatten" falschen Begründungen; Halluzination bei leeren Feldern; verschachtelte Brüche, Durchgestrichenes [G] |
| Weitere Hochschul-Studie (https://arxiv.org/abs/2605.19043) | Foto-Abschrift plus Rubrik in einem Aufruf | beim besten Modell 87 % der Fehler stammen aus der Abschrift, nicht aus der Bewertung; Fehlerarten: Bildqualität, erfundene Inhalte, falscher Umgang mit gleichwertigen Termen [G, nur Abstract] |
| EMNLP 2026 "When VLMs 'Fix' Students" (https://aclanthology.org/2026.emnlp-main.476.pdf) | 15 Modelle | 42,1 bis 66,2 % der Abschriften mit mindestens einer "ausgebesserten" Stelle (Schülerfehler wird beim Abschreiben korrigiert); GPT-4o 62,3 %; Bewertungsbeispiele springen von 34 auf 99; Zusatzprompt "treu abschreiben" senkt im Schnitt nur um etwa 4 Punkte [G] |
| DrawEduMath, handgezeichnete Schülerantworten (https://arxiv.org/pdf/2603.00925) | u. a. GPT-5, Gemini 2.5 Pro, Claude Sonnet 4.5 | Fragen zu fehlerhaften Antworten 6 bis 10 Prozentpunkte schlechter als zu richtigen; Modelle bei Fehlerurteilen teils nahe Zufall [G] |
| FERMAT, Klasse 7 bis 12 (https://preview.aclanthology.org/landing_page/2025.acl-long.720.pdf) | 9 Modelle, 2.200 handgeschriebene Lösungen mit eingebauten Fehlern | beste Fehlerkorrekturrate 77 % (Gemini-1.5-Pro); Genauigkeit steigt, wenn die Handschrift durch Druckschrift ersetzt wird [G] |

[M] Aus der Summe: Das Sehen von Handschrift ist gut genug für saubere, kurze Rechnungen; das Beurteilen von Fehlern ist schwach. Ausgerechnet der Fall, der für ein Lernsystem zählt (falsche Zeile), ist der, in dem Modelle "helfen" und den Fehler verwischen.

### C2 Dienste und Preise
- Mathpix: siehe A12 (0,002 USD je Anfrage; Snip Pro ab 4,99 USD/Monat Drittangabe). Rechenbeispiel [A]: 2 Kinder, je 5 Heftseiten täglich, jede Seite 1 Anfrage, 30 Tage = 300 Anfragen = ca. 0,60 USD/Monat. Eine Vision-KI-Anfrage (Bild) kostet je Modell anders; Preise der KI-Anbieter habe ich nicht abgerufen.
- MyScript: Preise nicht gefunden.

### C3 Datenschutz bei Kinderhandschrift
- [G] Beispiel Khan Academy: KI-Zugang für Unter-18-Jährige nur über Eltern- oder Schulfreigabe; Chats sind für Eltern sichtbar; bei auffälligem Inhalt geht eine E-Mail an einen verbundenen Erwachsenen (https://support.khanacademy.org/hc/tr/articles/13965308352781, https://support.khanacademy.org/hc/ka/articles/14394814244365).
- Rechtslage DSGVO/Auftragsverarbeitung für Foto-Upload an KI-Anbieter, Speicherung/Training: **nicht recherchiert**. [A] Mindestmaß: Foto auf die Rechnung zuschneiden (kein Name, keine Schule), Anbieter-Einstellung "kein Training", keine Speicherung, Fotos nach Auswertung löschen, Zugriff nur über Eltern-Konto.

### C4 Was ist realistisch?
[M] Ja, Vorkorrektur mit Bestätigung durch Erwachsene, aber so gebaut:
1. Foto je Heftseite oder Zeile, die App schneidet Zeilen aus und lässt die KI nur **abschreiben** (LaTeX/Text je Zeile), nicht bewerten.
2. Das Kind (oder Elternteil) sieht Foto und Abschrift nebeneinander und bestätigt oder korrigiert (Gegenmittel gegen "Ausbessern").
3. Ein deterministischer Prüfer (Abschnitt 3) urteilt über die Zeilen.
4. Zusätzlich Stichprobe: Elternteil sieht pro Woche einige Seiten (Anteil nach Gefühl, [A] 10 bis 20 %).
5. Bei Netzmangel: Fotos in der Warteschlange speichern, später auswerten. Das Kind bekommt dann erst später ein Urteil, im Prüfungsmodus ohnehin gewünscht.
Offene Frage: Reicht Genauigkeit bei Kinderhandschrift der Klasse 5? Dazu fand ich keine Studie (nur Ghana Mittelstufe, Arithmetik).

---

## D) KI-Tutoren mit Schutzregeln

### D1 Bastani u. a. (PNAS 2025): Aufbau des "GPT Tutor"
Quellen: Vorabdruck-PDF https://nmdprojects.net/teaching_resources/bastani_generative_ai_can_harm_learning.pdf; Zusammenfassungen https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/, https://www.psypost.org/unrestricted-generative-ai-harms-high-school-math-learning-by-acting-as-a-crutch/, https://www.edutopia.org/article/ai-tutors-work-guardrails/.
- [G] GPT Base = GPT-4 mit Prompt "wirke als Tutor" plus aktuelle Aufgabe. GPT Tutor = zusätzlich (1) Anweisung, nie die ganze Lösung zu geben, zunächst "so wenig Information wie möglich", schrittweise Hinweise, (2) hinterlegte richtige Lösung(en) und Liste **typischer Fehler und der passenden Reaktion**. Aufgaben, Lösungen und Fehlerlisten schrieben die Lehrkräfte der Schule; die Schüler sahen den Prompt nicht.
- [G] Prompt-Einzelregeln laut Edutopia (Zitat gekürzt): immer nur EINEN Schritt verraten, nie die volle Lösung in einer Nachricht; darf bestätigen, ob die Antwort richtig ist (der Zusatz wird dort abgebrochen, weiterer Wortlaut nicht gelesen).
- [G] Anzahl Hinweise: **nicht festgelegt**; es heißt nur "inkrementell".
- [G] Zahlen: Hauptstichprobe 839 (Tutor 277, Kontrolle 320, Base 242); Übungsleistung Base +48 %, Tutor +127 %; Prüfung ohne KI: Base -0,054 (ca. -17 %, p<0,05), Tutor -0,004 (nicht signifikant) bei Kontrollmittel 0,321.
- [G] Genauigkeit der KI in dieser Studie: Für GPT Base wurde jede der 57 Übungsaufgaben 10-mal gefragt; nur 51 % der Antworten richtig (Denkfehler 42 %, Rechenfehler 8 %). Für GPT Tutor ist keine gemessene Fehlerquote berichtet; die Autoren sagen, der Tutor mache wegen der hinterlegten Lösung "selten" Fehler.
- [G] Grenzen: eine Schule in der Türkei, ein Semester, Klassen 9 bis 11, vier Sitzungen; fünf Sitzungen wichen von der Zuteilung ab (Ergebnis ohne sie gleich); Schüler nutzten auch die Tools oft oberflächlich.
- [M] Lesart: Hinterlegte Lösung und Fehlerliste sind das Kernstück, nicht ein cleverer Prompt. Der Tutor "verhindert Schaden", bewies aber keinen Lerngewinn bei Prüfungsleistung.

### D2 Khanmigo
- [G] Prompt so geschrieben, dass das Modell Fragen stellt, um das Kind durch das Gewusste zu führen; es gibt Unterstützung und eventuell einen Schritt, aber nicht die Antwort (https://blog.khanacademy.org/how-we-built-ai-tutoring-tools). Das Prinzip "Sokratisch/zugeschnitten auf den Lernrand" wird im Blog zu "7-Step Prompt Engineering" beschrieben (https://blog.khanacademy.org/khan-academys-7-step-approach-to-prompt-engineering-for-khanmigo; nur Ausschnitt gelesen).
- [G] Leitplanken außerhalb des Prompts: Moderation erkennt unangemessene Nachrichten und benachrichtigt einen Erwachsenen per E-Mail; Chatverlauf ist für Eltern/Lehrkräfte sichtbar; Hinweis im Produkt, dass die KI falsche Angaben machen kann (https://support.khanacademy.org/hc/ka/articles/14394814244365). Zugang unter 18 nur mit Freigabe (https://support.khanacademy.org/hc/tr/articles/13965308352781).
- [G] Common Sense Media (Datum der Bewertung nicht erfasst): Khanmigos Fähigkeit als sehr genauer Mathe-Tutor sei begrenzt; nimmt keine Bilder an, antwortet nur Text (https://www.commonsensemedia.org/ai-ratings/khanmigo).
- Hinterlegte Musterlösungen/Fehlerlisten bei Khanmigo: nicht gefunden.

### D3 Eedi / Google LearnLM
- Studie 1 (N=165, Alter 13 bis 15, 5 Schulen): 17 Experten-Tutoren prüften jeden Entwurf, 74,4 % der 3.617 Entwürfe unverändert gesendet; 5 Sachfehler (ca. 0,1 %) im Audit, keiner schädlich; Prompt: kurz, Frage für Frage, Antwort nicht verraten, auf die Fehlvorstellung bezogen; Ergebnisse: Wiederholung nach Fehler richtig 93,0 % (LearnLM) gegenüber 91,2 % (Mensch) und 65,4 % (feste Hinweise); Transfer in nächster Einheit 66,2 % gegenüber 60,7 % (Mensch) und 56,2 % [G] (https://arxiv.org/html/2512.23633v1).
- Studie 2 (N=1.179, Alter 12 bis 15, 10 Schulen, 10 Wochen, vorregistriert): Genehmigungsquote 94,7 % unverändert; Audit: 6 von 114.935 Entwürfen mit Problem (4 Mathefehler, keiner erreichte Schüler); Kontextfehler 0,24 % (Experten 0,18 %), richtige Antwort als falsch markiert 0,08 %; Antwort nicht verraten in 98,8 % der KI-Gespräche; Kontrollfrage nach der Klärung in 91,3 %; Folgeaufgaben 56 bis 58 % richtig gegenüber 43 % nach Standardhilfe; **Star Maths ohne Wirkung** (Differenz -0,01 bis +0,02 SD) [G] (https://services.google.com/fh/files/misc/learnlm_oct26.pdf; Presse: https://www.the74million.org/article/five-things-you-should-know-about-new-ai-tutor-study/). Beide Studien mit Beteiligung des Herstellers.

### D4 Harvard Physik (Kestin u. a.)
- [G] 194 Studierende, Crossover: KI-Tutor schlug Präsenz-Active-Learning (Lerngewinn median mehr als doppelt, in weniger Zeit). Design: Systemprompt mit Lernprinzipien; die Plattform führt Teilaufgaben der Reihe nach, weil der Prompt allein die Reihenfolge nicht hielt; **ausführliche Schritt-für-Schritt-Lösungen wurden in die Prompts geschrieben**, damit die Antworten stimmen (https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/). Grenzen: Hochschule, ein Kurs, Erstlernen.

### D5 Carnegie LiveHint
- [G] Eingeführt 2023 als Chat-Tutor auf Basis eines großen Sprachmodells und 25 Jahren MATHia-Daten; Eltern-Abmeldebriefe vor Einführung; Anbindung an die Versuchsplattform UpGrade für kontrollierte Versuche (https://digitalpromise.org/?p=89074). Veröffentlichte Wirkungsstudie: **nicht gefunden** (nur Pressemitteilungen, z. B. https://www.businesswire.com/news/20231130974040/en).

### D6 Weitere kontrollierte Studien (Auswahl)
- [G] IZA-Überblick (https://docs.iza.org/dp19025.pdf): Rori (WhatsApp-Mathe-Tutor, Ghana, Klasse 3 bis 8, 2 mal 30 Min/Woche, 8 Monate, Tutor gibt erst Hinweis vor Lösung): +0,36 SD; Sierra Leone (Gemini, Klasse 7/8, 8 Wochen, Lehrkraft leitet): +0,26 SD, 76 % der Tutor-Nachrichten waren Fragen und 2 % direkte Lösungen; China, adaptive Software Klasse 4 bis 6: -0,04 SD; gepoolter Effekt 0,21 SD (Konfidenz 0,05 bis 0,36, hohe Heterogenität). Die Autoren betonen, dass nicht klar ist, welche Merkmale wirken (zusätzliche Übungszeit, Lehrkraft vor Ort). Zitat sinngemäß: Generative KI kann Schularbeit besser aussehen lassen, ohne dass Schüler besser werden.
- [G] Gupta u. a. 2025 (https://arxiv.org/abs/2503.16460): Sprachmodelle erzeugen häufig Fehler und Ungenauigkeiten bei Nachhilfe-Aufgaben (College-Algebra, ältere Modellgeneration). [A] Für aktuelle Modelle mit hinterlegter Lösung nicht übertragbar.

### D7 Belegte Gestaltungsregeln (mit Stärke des Belegs)

| Regel | Beleg | Stärke |
|---|---|---|
| Lösung und typische Fehler vorab im Prompt | Bastani (Tutor-Arm), Kestin (Lösungen im Prompt), Eedi (Kontext) | mittel: ein RCT plus Fallstudien |
| Nie die Lösung nennen, nur schrittweise Hinweise | Bastani, Eedi (98,8 % keine Antwort verraten), Sierra Leone (2 % Lösungen) | mittel |
| Rückfrage statt Erklärung | Sierra Leone (76 % Fragen), Eedi, Khanmigo | schwach bis mittel |
| Nach Klärung eine Kontrollfrage | Eedi (91,3 %) | schwach |
| Erst eigener Versuch, dann Hilfe | Rori (Hinweis vor Lösung); Bastani-Schaden bei "Krücke" | schwach |
| Mensch prüft/ersetzt KI-Nachricht | Eedi (alle Nachrichten) | schwach für Familie (nicht skalierbar) |
| Leistung nur ohne KI messen | Bastani, IZA-Fazit | stark als Prinzip |
| Begrenzte Hinweiszahl | **keine direkte Studie gefunden**; Praxis: ASSISTments (Hinweis = falsch), Numbas (Punkte skaliert) | Praxis, kein Beleg |
| Feste Reihenfolge von Teilaufgaben durch Plattform | Kestin | schwach |

---

## 2. Bewertung der fünf eigenen Ideen

| Idee | Vorbilder | Belege | Handy-Bau | Aufwand | Nutzen |
|---|---|---|---|---|---|
| **Kontrollzahlen** (Kind rechnet im Heft, App fragt 1 bis 2 Zwischenergebnisse) | Numbas "steps" (Teilaufgaben), ASSISTments-Scaffolds, MATHia-Zwischenschritte (alle zerlegen die Aufgabe, aber als Hilfe, nicht als Prüfstein) | Zur Idee selbst **nichts gefunden**. Allgemein: Sofort-Rückmeldung nach Teilschritten (ASSISTments-RCT, sucher-b). | Reine Zahlenfelder, wenig Eingabe, offline-tauglich; Zwischenwerte vom Generator mitgeliefert (liegt im Bestand: Antwortform Zahl) | niedrig | mittel: erkennt falsche Zwischenwerte, nicht die Methode; Rechner/KI-Abkürzung möglich [A]. Wirksamer mit zufällig gewählten Prüfstellen |
| **Erste falsche Zeile** (Zahlen vor x / ohne x; Server setzt Werte ein) | STACK Equivalence reasoning, Mathspace, ACE, FA-Math (alle Zeile für Zeile); Numbas/WeBWorK (Einsetzen) | Kausale Wirkung des Zeilenprüfens: **nicht gefunden**; Mathspace-Zahlen herstellerseitig/korrelativ. Dependency-Risiko dokumentiert (Common Sense). Einsetzen als Prüftechnik: lange erprobt (WeBWorK/Numbas) | Zwei kleine Zahlenfelder je Zeile statt Formeleditor, Zahlenblock `inputmode="decimal"`; wenig Tipparbeit; im Prüfmodus Ergebnis erst nach Abgabe | mittel (Prüfer, Aufgabenmuster, Anzeige) | hoch für Klasse 8 (Gleichungen), mittel für Klasse 5 (Zahlenterme nur Wertvergleich) |
| **Lückenweg mit abnehmender Hilfe** | Sparx "Bookwork-Check" (sucher-b), MATHia-Hilfestufen, ASSISTments-Hinweisreihe; in der Lernforschung als "faded worked examples" bekannt [A, Allgemeinwissen, in dieser Recherche nicht belegt] | In dieser Recherche kein Beleg abgerufen | Antwortform "Lücken" existiert bereits; Handy gut | niedrig bis mittel (Lösungsweg je Aufgabentyp schreiben, Stufen 3 bis 4) | mittel: hilft beim Lernen neuer Verfahren; zählt nie als "sitzt" |
| **Heft + Selbstkontrolle nach Punkteschema** | Mathspace Test Mode (Begründung je Punkt, Lehrkraft überschreibt), Bayerische Korrekturpraxis [A] | Zur Selbstkorrektur durch Kinder dieser Altersgruppe: **nichts gefunden** | Checkliste: Häkchen je Schemapunkt; sehr wenig Tippen; offline | niedrig | niedrig bis mittel: nur belastbar mit Stichprobe durch Erwachsene; Rückfallebene für Begründungen, Konstruktionen, Textaufgaben |
| **Foto + KI-Vorkorrektur** | Mathspace Test Mode (KI-Bewertung mit Lehrer-Übersteuerung, Beta), MathGPT.ai (Pressemitteilung 07/2026 für Hochschulen), UC-Irvine-System | Siehe C1: sehr gut bei einfacher Arithmetik, schwach bei Fehlerbeurteilung, "Ausbesserungs"-Problem | Kamera, nahezu kein Tippen; Netz nötig, Warteschlange; Foto-Zuschnitt in App | hoch (Kamera, Zuschnitt, Abschrift-Bestätigung, Kosten, Datenschutz) | potenziell hoch (ersetzt Papierkorrektur), aber riskant ohne Erwachsenen |

**Reihenfolge nach Nutzen je Aufwand [M]:**
1. Kontrollzahlen (sofort, bestehende Antwortform).
2. Erste falsche Zeile, Stufe 1: Klasse 5 Zahlenterme (nur Wertgleichheit) und Klasse 8 lineare Gleichungen mit exaktem Lösungsvergleich.
3. Lückenweg mit abnehmender Hilfe (nutzt vorhandene Lücken-Antworten; aufwändig nur beim Schreiben der Wege).
4. Heft + Selbstkontrolle als Auffang für alles, was die Maschine nicht prüfen kann.
5. Foto + KI-Vorkorrektur als Pilot mit Bestätigungsschritt, wenn 1 und 2 laufen.
[A] Entscheidend ist ein Prüfungsmodus: keine Hinweise, keine Zeilenrückmeldung während der Arbeit, Ergebnis erst nach Abgabe, Zeitbegrenzung (Vorbild Mathspace Test Mode, Dr Frost Mock-Prüfungen aus sucher-b).

---

## 3. Vorschlag "erste falsche Zeile" (ohne große Bibliothek)

### 3.1 Grundidee
Jede Heftzeile ist entweder ein **Term** (kein Gleichheitszeichen) oder eine **Gleichung/Ungleichung** `L R`. Geprüft wird nur "Zeile n gleichwertig Zeile n-1", nie gegen die Musterlösung. Dadurch zählt ein Fehler **einmal** (Folgefehler wie bei Folgefehlerregeln, [A] Bayern wendet diese in der Korrektur an, nicht belegt): Spätere Zeilen, die zur fehlerhaften Zeile passen, bleiben "folgerichtig".

### 3.2 Eingabe
- Stufe 1 (am Handy am einfachsten, kein Parser): je Zeile zwei Paare Zahlen "vor x" und "ohne x" für linke und rechte Seite (also a·x + b = c·x + d); Eingabe als ganze Zahl, Bruch `3/4` oder Dezimal mit Komma `2,5`.
- Stufe 2 (freiere Zeilen): ein Textfeld je Zeile mit kleinem Parser (`+ - · * : / ^ ( )`, Bruch `3/4`, Dezimalkomma, `x`, Mal-Punkt unsichtbar `2x`, `2(x+1)`). Zahlenblock oder MathLive nur, wenn der Parser mit LaTeX-Strukturbaum gespeist werden soll [M].

### 3.3 Exakte Zahlen
Brüche aus `BigInt`-Paaren (Zähler/Nenner, gekürzt, Nenner > 0). Dezimalzahlen werden als Brüche gelesen (2,5 = 5/2). Keine Gleitkommazahlen. In SQL: `bigint`-Paare statt `numeric`/`float8`.

### 3.4 Terme: Gleichwertigkeit durch Einsetzen
Feste, deterministische Prüfwerte (nicht zufällig, wegen WeBWorK-Lehre): `P = {-6..6, ±1/2, ±3/2, ±1/3}`, etwa 19 Werte. Für jedes p: werte beide Terme aus (Ergebnis Bruch oder "undefiniert", falls Division durch 0).
- Beide definiert: Werte müssen gleich sein, sonst `FALSCH`.
- Genau einer undefiniert: Marker `DEFINITION` (Definitionsmenge verändert). Je Aufgabe konfigurierbar: bei Bruchtermaufgaben erlaubt oder anzumerken, sonst Fehler.
- Beide undefiniert: ignorieren.
- Mindestens 8 Punkte, an denen beide definiert sind, sonst `UNSICHER`.
Warum das robust ist: Zwei Polynome vom Grad höchstens d, die an d+1 verschiedenen Punkten übereinstimmen, sind gleich. Mit mindestens 8 Punkten ist die Prüfung für Polynome bis Grad 7 ein **Beweis**, nicht nur Stichprobe. Für Bruchterme wird nach Kreuzmultiplizieren der Grad aus Zähler plus Nenner gebildet; bei Klasse 8 liegt er weit unter 8 [A]. Klasse 5: Zahlenterme ohne x; hier genügt eine einzige Auswertung (Wert muss gleich bleiben).

### 3.5 Gleichungen: Lösungsmenge statt Wahrheitswert
Wichtig: Gleichungen sind gleichwertig, wenn sie dieselbe Lösungsmenge haben. Ein Einsetzen zufälliger x liefert fast immer "falsch=falsch" und taugt nicht. Stattdessen mit `f(x) = L(x) - R(x)`:
1. **Linearitätstest**: `f(0), f(1), f(2), f(3)` bilden eine Gerade (zweite Differenz 0)? Dann `f(x) = k·x - m` mit `k = f(1)-f(0)`, `m = -f(0)`.
2. Fälle: `k ≠ 0` → genau eine Lösung `m/k`; `k = 0, m = 0` → alle Zahlen (wahre Aussage); `k = 0, m ≠ 0` → keine Lösung.
3. Zwei Zeilen gleichwertig ⇔ gleicher Fall und (bei Einzellösung) gleiche Lösung (Bruchvergleich exakt).
4. Nichtlinear oder mit Brüchen: **Proportionalitätstest** `f2(p) = λ·f1(p)` für festes λ ≠ 0 an allen Punkten, wo f1(p) ≠ 0 (deckt Addieren/Subtrahieren auf beiden Seiten und Multiplizieren/Dividieren mit einer Zahl ab, auch Ausmultiplizieren, Faktorisieren, weil f gleich bleibt). Besteht der Test nicht, nicht sofort "falsch" rufen, sondern `UNSICHER`, wenn zugleich die bekannte Aufgabenlösung beide Zeilen erfüllt (Einsetzprobe der Lösungen des Generators); sonst `FALSCH`. Wahrscheinlicher Fehlalarm wäre schlimmer als verpasster Fehler [M]: im Zweifel `UNSICHER` und Hinweis an Eltern.
5. Relationszeichen: Zeichen muss zur Umformung passen; Multiplikation mit negativem λ bei Ungleichung verlangt gedrehtes Zeichen (häufiger Schülerfehler, wird so erkannt).

### 3.6 Sonderfälle (Tabelle)

| Fall | Beispiel | Ergebnis |
|---|---|---|
| Multiplikation mit 0 | `x+1=3` zu `0=0` | FALSCH (k=0,m=0 neue Klasse "alle", vorher Einzellösung) |
| Division durch x | `x(x-2)=x` zu `x-2=1` | FALSCH (Lösung x=0 geht verloren, Proportionalität scheitert) |
| Quadrieren | `x=2` zu `x²=4` | nicht gleichwertig (Lösungsmenge wächst); Prüfer sagt FALSCH; Schulstoff Klasse 8: [A] kaum betroffen |
| Termzeile nach Gleichung | `3x=6` dann `x` | Formfehler, Gleichheitszeichen fehlt; UNGÜLTIG, ohne Punktabzug (Muster STACK/Mathspace: ungültig ≠ falsch) |
| Gekürzt: `x/x` zu `1` | | Term: DEFINITION (bei x=0) |
| Identische Zeile | | gleichwertig (Hinweis "unveränderte Zeile") |
| Falsche Startzeile | Zeile 1 ≠ Aufgabenzeile | eigener Fehler "Startzeile" (Muster `EquivFirst`) |
| Rechenfehler beim Vorzeichen | `3x-5=7` zu `3x=2` | Gleichungsfall linear: k=3, m=2 statt 12 → FALSCH an dieser Zeile |
| Dezimal | `0,5x=2` zu `x=4` | gleichwertig (exakt über Brüche) |
| Rundung | `x=3,333` statt 10/3 | in Gleichungswegen verboten; Rundungsaufgaben mit eigener Toleranzregel |
| Mehrere Variablen | | nicht unterstützt (eine Variable je Aufgabe) |

### 3.7 Ausgabe und Punkte
Rückgabe: `{ erste_falsche_zeile: n | null, art: 'Lösung geändert' | 'keine Lösung' | 'alle Zahlen' | 'Faktor 0' | 'Definitionsmenge' | 'Relationszeichen' | 'Startzeile', unsicher: [Zeilen] }`. Fehlerart kommt aus dem Fall (3.5/3.6), nicht aus Rätselraten über die Absicht des Kindes.
Punkteschema [M]: 1 Punkt Startzeile, je 1 Punkt für jede gleichwertige Folgezeile bis zur ersten falschen, nach dem Fehler Prüfung gegen die **eigene** vorige Zeile (Folgefehler) mit z. B. halber Punktzahl, Endergebnis nur bei Übereinstimmung mit der Musterlösung volle Punkte, aber Folgefehlerpunkt wenn folgerichtig. Genaue Gewichtung gehört in Abstimmung mit der bayerischen Korrekturpraxis (nicht recherchiert).

### 3.8 Wo läuft es?
- [M] Browser (sofortige Rückmeldung, offline) **und** serverseitig dieselbe Datei in einer Edge Function (maßgebliches Urteil, Manipulationsschutz), weil plv8 nicht mehr genutzt werden kann.
- [M] Reines SQL reicht, wenn nur Stufe 1 (Koeffizienten) existiert: Fälle aus 3.5 mit `bigint`-Brüchen rechnen.
- Größe: [A] unter 10 KB Code. Kein CAS erforderlich.

### 3.9 Mindesttests (Vorschlag)
Zu jedem Fall in 3.6 mindestens ein richtiges und ein falsches Beispiel; plus Zufallstest: aus jeder Aufgabe aus dem Generator die richtige Musterzeilenfolge und 3 künstliche Fehlerzeilen (Vorzeichen, Klammer, Seitenwechsel) automatisch prüfen.

### 3.10 Was nicht abgedeckt ist
Quadratische Gleichungen mit zwei Lösungen ("oder"-Ketten), Gleichungssysteme, Betrag, Wurzeln: nicht Teil von Stufe 1; STACK zeigt, dass sie ein eigenes Modell brauchen (Vielfachheiten, Mengen). [A] Für Klasse 8 Bayern reichen lineare Gleichungen/Terme, aber ich habe den LehrplanPLUS-Wortlaut hier nicht geprüft.

---

## 4. KI-Erklärer mit Schutzregeln: Regelliste

Ziel: Das Modell **formuliert nur um**, was vorab geprüft wurde. [M] = meine Folgerung; Beleg in Klammern.

**A. Was das Modell bekommt**
1. Pro Aufgabe nur geprüfte Bausteine: Musterlösung in Schritten, Liste typischer Fehler je mit benanntem Denkfehler und passender Reaktion (Bastani-Tutor-Arm; Kestin).
2. Alle Zahlen und Zwischenergebnisse kommen vom Generator, nicht vom Modell (Fehlerquote Chat ohne Lösung 49 %, Bastani).
3. Je erkanntem Fehler (aus Abschnitt 3 oder Antwortwahl) ein vorab geschriebener, von Erwachsenen oder von mir geprüfter **Erklärbaustein** in 3 Stufen: Stufe 1 Frage ("Was passiert mit der 5, wenn sie die Seite wechselt?"), Stufe 2 Teilschritt am **anderen** Beispiel, Stufe 3 Musterbeispiel einer **ähnlichen** Aufgabe mit anderen Zahlen [M; Stufung Bastani "inkrementell", Rori "Hinweis vor Lösung"].
4. Kein Foto, kein Name, kein Alter, kein Standort an das Modell [M, Datensparsamkeit].

**B. Was das Modell tun darf**
5. Nur umformulieren (einfacher, kürzer, anderer Vergleich), nie neue Mathematik erfinden [M].
6. Pro Antwort eine einzige Rückfrage oder ein einziger Schritt (Eedi: eine Frage auf einmal; Bastani: ein Schritt).
7. Nie das Endergebnis der Kinderaufgabe nennen und nie einen Zwischenwert, der die Aufgabe löst (Bastani, Eedi 98,8 %).
8. Nach geklärtem Fehler eine Kontrollfrage stellen, die die App (nicht das Modell) auswertet (Eedi 91,3 %).
9. Deutsch, kurze Sätze, Klasse 5 und 8 getrennt formulieren [M].

**C. Prüfung der Ausgabe (Code, nicht Modell)**
10. Zahlen-Weißliste: Jede Zahl in der Modellantwort muss in den hinterlegten Bausteinen oder in der Aufgabe vorkommen; sonst Ersatz durch den festen Baustein [M].
11. Lösungsfilter: Antwort darf das Endergebnis der Aufgabe weder als Zahl noch als "x = …" enthalten [M].
12. Längenbegrenzung (z. B. 60 Wörter) und feste Struktur [M].
13. Bei Verstoß oder Modellfehler: fester vorgeschriebener Text, nie Fehlermeldung des Anbieters [M].

**D. Wie das Kind fragt**
14. Keine freie Texteingabe des Kindes; nur Knöpfe ("Ich komme nicht weiter", "Ich verstehe den Hinweis nicht", "Noch einmal anders") [M; Bastani-Schaden betrifft den freien Chat, für "nur Knöpfe" aber ungetestet, [A]].
15. Erst eigener Versuch: Hilfe erst nach mindestens einer abgegebenen Antwort oder Zeile (Rori: Hinweis bevor Lösung; [M]).
16. Hinweisstufen zählen: höchstens 3 je Aufgabe, danach Verweis auf Beispielaufgabe und neue Aufgabe (keine Studie zur Zahl; Praxis ASSISTments/Numbas) [M].
17. Jede genutzte Stufe wird gespeichert; Aufgabe mit Hilfe zählt **nicht** als "sitzt" (ASSISTments "Hinweis = falsch"; Bastani-Lehre: Leistung mit Hilfe sagt wenig).
18. Kurze Pause (z. B. 10 s) vor Stufe 2 und 3, damit erst nachgedacht wird [A, ohne Beleg].

**E. Wo es aus ist**
19. Im Prüfungsmodus und bei Kontrollzahlen vor Abgabe: kein Erklärer (Mathspace Test Mode; Messung ohne KI).
20. Chatverlauf und Hinweisnutzung sind für Eltern einsehbar (Khanmigo-Modell).
21. Wöchentlich: Elternteil liest 10 zufällige Erklärungen quer; Fehlermeldung "falsch erklärt" als Knopf im Kind-UI [M; entspricht Eedi-Audit im Kleinen].
22. Zielgröße messen: Anteil Aufgaben mit Hilfe, die beim Wiederholen ohne Hilfe richtig sind; sinkt der Anteil nicht, Erklärer ändern oder ausschalten [M]. Belegte Lernwirkung für 10- bis 15-Jährige ist bisher: gleich gut wie Mensch bei Folgeaufgaben, **kein** Effekt im Standardtest (Eedi) und bei Bastani kein Gewinn bei Prüfung.

[M] Ehrliche Einordnung: Der Erklärer ist ein Komfort, kein Lernbeschleuniger nach heutigem Beleg. Er darf nicht Vorrang vor Zeilenprüfer und Prüfungsmodus bekommen.

---

## 5. Einbinden statt selbst bauen / weglassen [M]

**Einbinden**
- MathLive (MIT) nur dort, wo Brüche/Wurzeln wirklich getippt werden müssen; Schriften lokal, Tastatur am echten Handy (360 px) testen. Für Zahlenfelder native `inputmode="decimal"`-Felder, kein Editor.
- Compute Engine oder math.js: **nicht** als Gleichwertigkeitsrichter. Optional math.js (Apache 2.0, Fractions) als zweite Meinung in Tests; Gleichwertigkeitsprüfer selbst schreiben (Abschnitt 3).
- Eedi-Fehlvorstellungslisten, Serlo-Erklärtexte (siehe sucher-b/c) als Material für die Bausteine in Abschnitt 4.
- Anbieter-KI nur für Umformulierung (Abschnitt 4) und für Foto-Abschrift (Abschnitt C4).

**Selbst bauen**
- Zeilenprüfer (klein, testbar, exakte Brüche), Hilfestufen-Zähler, Prüfungsmodus, Weißliste für KI-Ausgaben.

**Weglassen (zunächst)**
- STACK/Maxima, Möbius, Mathspace-Lizenz: nicht einbettbar oder zu schwer.
- SymPy/Pyodide: zu groß für Handy und schlechtes Netz.
- Algebrite: kaum gepflegt; Nerdamer: nur falls später Gleichungslösen gebraucht wird.
- Freier KI-Chat für Kinder (Bastani: -17 % ohne Schutz).
- Handschrifterkennung in der App (MyScript/Mathpix) für das Bewerten: erst nach Pilot; Abschrift ja, Urteil nein.
- Eigene Selbstkontrolle als alleiniger Maßstab.

---

## Was ich nicht prüfen konnte
- STACK: Eine fertige Web-API/Standalone-Variante für fremde Apps; Lizenzlage bei getrenntem Dienst. Kosten von Maxima-Hosting.
- Numbas: Lizenz; Code von `jme.jme` nicht gelesen. Graspable, ACE, FA-Math, Mathegym: Prüfverfahren nicht dokumentiert gefunden. Möbius: Preis.
- Mathspace: Verfahren der Gleichwertigkeitsprüfung, Genauigkeit des KI-Markings im Test Mode, ob Hinweise Punkte kosten.
- MathLive: Größe der min.js, Test am 360-px-Gerät, Offline-Betrieb praktisch; Compute-Engine-Größe je aktueller Version (Paketdienst zeigt 0.59.0, jsDelivr 0.136.2).
- MyScript-Preise, Photomath-Verhalten, Preise der Vision-KI-Anbieter; Genauigkeit bei Kinderhandschrift Klasse 5 und bei deutscher Schrift/Notation (Doppelpunkt, Dezimalkomma): keine Studie gefunden.
- DSGVO/Auftragsverarbeitung/Kinderdaten bei Foto an KI-Dienste: nicht recherchiert.
- Volltexte: Bastani PNAS nur über Vorabdruck-PDF-Auszug (Anhang A.1 gelesen, Anhang A.2 nicht), Edutopia-Zitat ist abgebrochen; Khanmigo-7-Step-Blog nur Ausschnitt; LearnLM-Studie 2 nur bis Zeichen 100.000 von 156.753 gelesen (Studie 1 bis dort).
- Belege zu "faded worked examples" (Lückenweg), zur Selbstkorrektur von Kindern, zur optimalen Hinweiszahl: nicht abgerufen.
- Bayerische Korrekturpraxis (Folgefehler, Teilpunkte) und LehrplanPLUS-Inhalte Klasse 8 (Bruchterme, Gleichungstypen): nicht geprüft.
- Eigene Vorschläge in Abschnitt 3 und 4 sind nicht programmiert oder getestet.
