# Dritte Sammelrunde (Kl.-8-Stoff erweitern): bayerische Schulaufgaben von klassenarbeiten.de, ISB-Grundwissentests Realschule Jgst. 9 (WPFG I).
# Wird von _bau.py per exec eingelesen. Nur eigene Worte, keine Aufgabentexte, keine Lösungen.

ISB_GWT = "https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Grundwissenstests_Mathematik/"


def GWT9(jahr, pfad, zeilen, ges=23):
    # ges: Summe der erkennbaren Einzelpunkte; laut Kopfzeile meist 23 (Abweichung im Original nicht eindeutig zuzuordnen)
    A(f"G8-R{jahr}", quelle=ISB_GWT + pfad, titel=f"Grundwissentest Mathematik 9 Realschule {jahr} (WPFG I)", herausgeber="ISB Bayern (Realschule)",
      art="Grundwissentest Realschule Jgst. 9, WPFG I (prüft Kl.-8-Stoff der Realschule)", nummer="Beginn Kl. 9 (Sept.)", jahr=jahr,
      zeit_min=45, punkte_gesamt=ges, hilfsmittel="kein Taschenrechner", frei=True, lizenz=LIZ_ISB, bundesland="Bayern",
      passung="Bayern amtlich, aber Realschule (Kl.-8-Stoff RS: viel Überschneidung mit Gym 8, dazu RS-eigene Themen)", klasse=8, zeilen=zeilen)


QX = "X:quadratische Terme/Gleichungen, Extremwerte (RS Kl. 8, Gym Kl. 9/10)"
DET = "X:Determinante/Vektorrechnung (nur Realschule)"
ROT = "X:Rotationskörper (nur Realschule)"

GWT9(2025, "2025/2025_GWT_Mathematik_9_I_Angabe.pdf", """
1a;1;I;K4;Zeichnen;FLIN:graph_ablesen;Gerade zeichnen;klein;
1b;1;I;K5;Gleichung;FLIN:lage;Parallele angeben;klein;
2;1;II;K3;Gleichung aufstellen;LG:sach;Gleichung für Sparbetrag;Euro;
3a;1;I;K5;Ergänzen;TU:ausmultiplizieren;Term beim Distributivgesetz ergänzen;Variable;
3b;1;I;K5;Ergänzen;TU:ausklammern;Term beim Ausklammern ergänzen;Variable;
4;1;II;K5;Koordinaten;GB:koordinaten;fehlender Streckenendpunkt über Mittelpunkt;klein;
5;1;II;K5;Gleichung;LG:klammern;Lösungsmenge einer Gleichung;klein;
6;1;II;K4;Zeichnen;KON:drehung;Drehzentrum zeichnerisch;–;
7;1;I;K4;Zeichnen;KST:vierecke_konstruieren;Raute vervollständigen;–;
8;1;I;K5;Umformen;TU:binomisch;Klammer auflösen, zusammenfassen;Variable;
9;1;II;K6;Fehler finden;FV:verstehen;Fehler in Flächenaussage;–;
10;1;I;K4;Erkennen;X:Rotationskörper (nur Realschule);Rotationskörper erkennen;–;
11;1;II;K3;Auswahl;LG:sach;Gleichung zu Wiese mit Weg wählen;m;
12;1;II;K4;Zeichnen;X:Determinante/Vektorrechnung (nur Realschule);Hilfspfeile für Flächenberechnung;–;
13;1;II;K5;Auswahl;BT:definitionsmenge;Nenner zu gegebener Definitionsmenge;klein;
14;1;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
15;1;II;K3;Maßstab;GR:massstab;Dreieckshöhe aus Maßstab;cm;
16;1;II;K4;Fläche;FV:trapez;Trapezfläche aus Zeichnung;cm²;
17;1;II;K3;Prozent;PZ:prozentsatz;Füllstand in Prozent;Liter;
18;1;II;K4;Auswahl;IND:graph;Graph bei konstanter Fläche;–;
19a;1;II;K1;Begründen;WS:parallel_pruefen;Nichtparallelität begründen;Grad;
19b;1;II;K5;Winkel;WS:figuren;fehlender Winkel;Grad;
20;1;I;K5;Häufigkeit;STO:rel_haeufigkeit;relative Häufigkeit in Prozent;klein;
""")
GWT9(2024, "2024/2024_GWT_Mathe_9_I_Angabe.pdf", """
1;1;II;K1;Ankreuzen;FLIN:deuten;wahre Aussage zu einer Geraden;klein;
2a;1;I;K5;Nullstelle;FG:nullstellen;Nullstelle einer linearen Funktion;klein;
2b;1;II;K5;Parallele;FLIN:lage;Punkt für Parallele bestimmen;klein;
3;1;I;K5;Ergänzen;TU:ausmultiplizieren;Distributivgesetz ergänzen;Variable;
4;1;II;K4;Drehen;KON:drehung;Pfeil um Punkt drehen, Koordinaten;klein;
5;1;II;K5;Gleichung;LG:beide_seiten;Gleichung, bei der sich x² weghebt;klein;
6;1;I;K4;Zeichnen;KST:vierecke_konstruieren;Parallelogramm aus Seiten und Winkel;cm;
7;1;I;K5;Umformen;TU:summe_mal_summe;Klammern auflösen, zusammenfassen;Variable;
8;1;II;K5;Vektor;KON:vektor_koordinaten;Vektorkoordinaten aus zwei Punkten;klein;
9;1;II;K5;Extremwert;X:quadratische Terme/Gleichungen, Extremwerte (RS Kl. 8, Gym Kl. 9/10);Maximum ablesen;cm²;
10;1;II;K5;Fläche;FL:zerlegen;Fläche zwischen zwei Quadraten;cm²;
11;1;I;K6;Benennen;X:Rotationskörper (nur Realschule);Teile eines Rotationskörpers benennen;–;
12;1;II;K5;Zuordnen;X:Determinante/Vektorrechnung (nur Realschule);Eckpunkte in Flächenformel;–;
13;1;II;K6;Begründen;BT:definitionsmenge;warum ein Bruchterm eine Definitionsmenge braucht;–;
14;1;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung mit zwei Nennern;klein;
15;1;II;K1;Ankreuzen;KON:eigenschaften;falsche Aussage zu Vierecken;–;
16;1;II;K3;Volumen;VOL:liter;Sauerstoffvolumen im Raum;m³;
17;1;II;K3;Schätzen;GR:massstab;Weglänge auf Karte schätzen;km;
18;1;II;K4;Kreisdiagramm;DD:kreisdiagramm;Kreisdiagramm ergänzen;Stimmen;
19a;1;II;K5;Winkel;KR:tangente;Winkel an Tangente;Grad;
19b;1;II;K5;Winkel;WS:stufen_wechsel;Winkel an Parallelen;Grad;
20;1;I;K5;Häufigkeit;DD:absolute_haeufigkeit;absolute Häufigkeit;klein;
""", ges=22)
GWT9(2023, "2023/2023_GWT_Mathe_9_I_Angabe.pdf", """
1a;1;I;K4;Zeichnen;FLIN:graph_ablesen;Gerade zeichnen;klein;
1b;1;II;K5;Gleichung;FLIN:aufstellen;senkrechte Gerade durch Punkt;klein;
1c;1;II;K1;Erkennen;FLIN:lage;Parallele zur Winkelhalbierenden;–;
2;1;I;K5;Ausklammern;TU:ausklammern;gemeinsamen Faktor ausklammern;Variable;
3;1;II;K1;Ankreuzen;TU:aequivalenz;allgemeingültige Aussage erkennen;–;
4;1;II;K5;Gleichung;LG:beide_seiten;Gleichung mit wegfallendem x²;klein;
5;1;I;K4;Zeichnen;KST:vierecke_konstruieren;Raute mit Winkel ergänzen;–;
6;1;I;K5;Umformen;TU:binomisch;binomische Klammer auflösen;Variable;
7;1;II;K5;Vektor;KON:verschiebung;Punkt aus Verschiebung;klein;
8;1;II;K5;Extremwert;X:quadratische Terme/Gleichungen, Extremwerte (RS Kl. 8, Gym Kl. 9/10);Art, Wert und Stelle eines Extremwerts;klein;
9;1;III;K3;Fläche;FL:sachaufgaben;Gehege mit Zaunbedingung;m²;
10;1;II;K6;Fehler finden;KD:schraegbild;Fehler im Schrägbild;–;
11;1;II;K5;Auswahl;X:Determinante/Vektorrechnung (nur Realschule);Flächenansatz mit Determinante;–;
12;1;II;K5;Ergänzen;BT:definitionsmenge;Nenner passend ergänzen;klein;
13;1;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung mit D lösen;klein;
14;1;II;K4;Konstruieren;KR:umkehrung;Dreieck mit Thaleskreis;cm;
15;1;II;K3;Volumen;VOL:zusammengesetzt;Kartonvolumen aus Würfeln;cm³;
16;1;II;K3;Prozent;PGW:zurueck;Preis aus Sparbetrag;Euro;
17;1;II;K3;Maßstab;GR:massstab;Pfeilerhöhe aus Maßstab;m;
18;1;II;K1;Ankreuzen;DD:tabelle_auswerten;falsche Aussage zum Diagramm;–;
19;1;II;K5;Winkel;WS:figuren;Winkel mit Parallelen und gleichschenkligem Dreieck;Grad;
20;1;I;K5;Häufigkeit;STO:rel_haeufigkeit;relative Häufigkeit aus Tabelle;klein;
""", ges=22)
GWT9(2022, "2022/_A__2022_GWT_Mathe_9_I_Angabe.pdf", """
1a;1;I;K4;Ablesen;FLIN:ablesen;Geradengleichung ablesen;klein;
1b;1;I;K4;Zeichnen;FLIN:graph_ablesen;Gerade aus Punkt und Steigung;klein;
1c;1;II;K5;Gleichung;FLIN:zwei_punkte;Gerade aus Achsenschnittpunkten;klein;
2;1;I;K5;Ergänzen;TU:ausmultiplizieren;Distributivgesetz ergänzen;Variable;
3;1;II;K5;Gleichung;LG:beide_seiten;Gleichung mit wegfallendem x²;klein;
4;1;I;K4;Zeichnen;KST:vierecke_konstruieren;gleichschenkliges Trapez vervollständigen;–;
5;1;I;K5;Umformen;TU:summe_mal_summe;Klammer auflösen;Variable;
6;1;I;K5;Koordinaten;GB:vierecke;fehlender Parallelogrammpunkt;klein;
7;1;II;K1;Erkennen;TA:sachsituation;falschen Umfangsterm erkennen;Variable;
8;1;II;K4;Ablesen;KD:schraegbild;Grundfläche aus Schrägbild;cm²;
9;1;II;K5;Fläche;X:Determinante/Vektorrechnung (nur Realschule);Dreiecksfläche mit Determinante;FE;
10;1;I;K5;Definitionsmenge;BT:definitionsmenge;D eines Bruchterms;klein;
11;1;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
12;1;II;K1;Aussage;FL:verstehen;Seitenlänge aus Umfang beurteilen;cm;
13;1;II;K3;Sachaufgabe;FLIN:deuten;Wasserstand nach Zeit;cm;
14;1;II;K4;Erkennen;X:quadratische Terme/Gleichungen, Extremwerte (RS Kl. 8, Gym Kl. 9/10);quadratischer Term mit Minimum;–;
15;1;II;K1;Begründen;PGW:mehrfach;Preisänderungen begründen;Prozent;
16;1;II;K3;Sachaufgabe;GR:massstab;Plattformhöhe;m;
17;1;II;K4;Drehen;KON:drehung;Bildpunkt einer Drehung;–;
18;2;II;K5;Winkel;WS:stufen_wechsel;zwei Winkel an Parallelen;Grad;
19;1;I;K5;Häufigkeit;DD:relative_haeufigkeit;Anzahl aus relativer Häufigkeit;klein;
""", ges=22)
GWT9(2021, "2021/2021_gwt_mathe_9_i_angabe.pdf", """
1a;1;I;K4;Ablesen;FLIN:ablesen;Geradengleichung ablesen;klein;
1b;1;I;K5;Einsetzen;FG:punkt_graph;fehlende Koordinate auf Gerade;klein;
1c;1;II;K5;Gleichung;FLIN:aufstellen;senkrechte Gerade;klein;
2;1;II;K1;Erkennen;FLIN:lage;Geraden durch einen Quadranten;–;
3;1;II;K2;Knobel;TB:quersumme;kleinste dreistellige Zahl mit Quersumme;dreistellig;
4;1;II;K5;Gleichung;LG:beide_seiten;Gleichung mit wegfallendem x²;klein;
5;1;I;K5;Umformen;TU:summe_mal_summe;Klammern auflösen;Variable;
6;1;II;K5;Vektor;KON:verschiebung;Punkt aus Vektorbeziehung;klein;
7;1;II;K1;Auswahl;TA:sachsituation;zwei passende Flächenterme;Variable;
8;1;I;K4;Zeichnen;KST:vierecke_konstruieren;Drachenviereck vervollständigen;–;
9;1;II;K5;Fläche;X:Determinante/Vektorrechnung (nur Realschule);Dreiecksfläche aus Vektoren;FE;
10;1;II;K3;Prozent;PGW:zurueck;Füllmenge vor Aufschlag;g;
11;1;II;K5;Ergänzen;BT:definitionsmenge;Nenner passend ergänzen;klein;
12;1;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
13;1;II;K1;Ankreuzen;BR:anteil_bestimmen;Aussage zur Chorbeteiligung;Anteile;
14;1;I;K4;Zeichnen;KD:schraegbild;Schrägbild eines Quaders;cm;
15;1;II;K1;Begründen;STO:rel_haeufigkeit;Trefferquoten vergleichen;klein;
16;1;II;K3;Volumen;VOL:liter;Wassermenge zum Befüllen;m³;
17;1;II;K3;Zeit;GR:zeit;Reisezeit mit Zuschlägen;h;
18;1;II;K4;Drehen;KON:drehung;Bildpunkt einer Drehung;–;
19α;1;II;K5;Winkel;WS:figuren;Winkel aus Parallelen und Dreieck;Grad;
19β;1;II;K5;Winkel;WS:figuren;zweiter Winkel;Grad;
20;1;II;K5;Fläche;FL:zerlegen;schraffierte Fläche einer Quadratfigur;cm²;
""")
GWT9(2020, "2020/2020_gwt_mathe_9_i_loesung.pdf", """
1a;1;I;K4;Zeichnen;FLIN:graph_ablesen;Gerade zeichnen;klein;
1b;1;I;K5;Prüfen;FG:punkt_graph;liegt Punkt auf Gerade;klein;
1c;1;II;K5;Gleichung;FLIN:lage;Parallele durch Punkt;klein;
2;1;I;K5;Gleichung;LG:klammern;Gleichung mit Klammern;klein;
3;1;III;K2;Knobel;BG:verhaeltnis;Bruch aus Änderung von Zähler und Nenner;klein;
4;1;I;K5;Ergänzen;TU:ausklammern;Ausklammern ergänzen;Variable;
5;1;I;K5;Umformen;TU:summe_mal_summe;Klammern auflösen;Variable;
6;1;II;K1;Auswahl;TA:sachsituation;Flächenterm einer Figur;Variable;
7;1;I;K6;Benennen;KON:vierecke_ordnen;Viereck aus Eigenschaften;–;
8;1;II;K5;Vektor;KON:verschiebung;Punkt mit Vektor berechnen;klein;
9;1;II;K2;Anteil;BR:anteil_bestimmen;Karten entfernen für Anteil;klein;
10;1;II;K5;Extremwert;X:quadratische Terme/Gleichungen, Extremwerte (RS Kl. 8, Gym Kl. 9/10);Extremwert ankreuzen;klein;
11;1;I;K5;Definitionsmenge;BT:definitionsmenge;D eines Bruchterms;klein;
12;1;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
13;1;II;K1;Ankreuzen;DD:tabelle_auswerten;Aussagen zum Wahldiagramm;–;
14;1;I;K5;Wahrscheinlichkeit;STO:laplace;Teilbarkeitsereignis beim Würfeln;klein;
15;1;II;K3;Volumen;VOL:rueckwaerts;fehlendes Maß eines L-Profils;cm;
16;1;II;K3;Fläche;FL:sachaufgaben;Fliesenpakete für Wand mit Aussparungen;m²;
17a;1;II;K5;Winkel;WS:figuren;Winkel mit Parallelen und gleichen Strecken;Grad;
17b;1;II;K5;Winkel;KR:tangente;Winkel an Tangente;Grad;
18;1;II;K5;Fläche;FL:verstehen;Rechteck aus Umfang und Seitenverhältnis;cm²;
19;1;II;K1;Begründen;KST:konstruierbar;Mindestlänge einer Dreiecksseite;cm;
20;1;II;K3;Prozent;PGW:zurueck;Preis vor Erhöhung;Euro;
""")
GWT9(2019, "2019/2019_gwt_mathe_9_i_angabe.pdf", """
1a;1;I;K4;Ablesen;FLIN:ablesen;Geradengleichung ablesen;klein;
1b;1;II;K5;Gleichung;FLIN:aufstellen;Senkrechte durch Punkt;klein;
1c;1;I;K5;Schnittpunkt;FG:nullstellen;Schnitt mit der y-Achse;klein;
2;1;I;K5;Gleichung;LG:klammern;Gleichung mit Klammern;klein;
3;1;II;K1;Beurteilen;X:quadratische Terme/Gleichungen, Extremwerte (RS Kl. 8, Gym Kl. 9/10);Aussagen zu quadratischem Term;–;
4;1;I;K5;Umformen;TU:summe_mal_summe;Klammern auflösen;Variable;
5;1;II;K3;Term;TA:sachsituation;Flächenterm vergrößertes Rechteck;Variable;
6;1;II;K1;Ankreuzen;KON:vierecke_ordnen;Eigenschaften von Rauten;–;
7;1;II;K5;Koordinaten;GB:koordinaten;Mittelpunkt nach Verschieben eines Endpunkts;klein;
8;1;II;K1;Beurteilen;PGW:mehrfach;Prozentzunahme beurteilen;Prozent;
9;1;II;K5;Ergänzen;X:quadratische Terme/Gleichungen, Extremwerte (RS Kl. 8, Gym Kl. 9/10);Aussage über Maximum ergänzen;–;
10a;1;I;K5;Definitionsmenge;BG:definitionsmenge;D einer Bruchgleichung;klein;
10b;1;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
11;1;II;K1;Fehler finden;IND:unterscheiden;falscher Wert in Tabelle;klein;
12;1;I;K5;Ausklammern;TU:ausklammern;Ausklammern ergänzen;Variable;
13;1;II;K4;Diagramm;FG:graph_lesen;Aussagen zu Fahrtdiagramm;–;
14;1;II;K5;Wahrscheinlichkeit;STO:laplace;Wörter aus Karten legen;klein;
15;1;II;K3;Anteil;PZ:prozentsatz;Anteil Tagesbedarf;mg;
16;2;II;K5;Winkel;WS:stufen_wechsel;Winkel an Parallelen;Grad;
17;1;II;K5;Umfang;FL:verstehen;Umfang aus Flächenangaben;cm;
18;1;II;K1;Begründen;KST:konstruierbar;unmögliche Dreiecksseite;cm;
19;1;II;K3;Volumen;VOL:rueckwaerts;Kellerseite aus Wasservolumen;m;
""")
GWT9(2018, "2018/2018_gwt_mathe_9_i_angabe.pdf", """
1a;1;I;K4;Zeichnen;FLIN:graph_ablesen;Gerade zeichnen;klein;
1b;1;I;K5;Ergänzen;FLIN:lage;parallele Gerade ergänzen;klein;
1c;1;II;K2;Angeben;FLIN:lage;Gerade ohne Schnitt mit x-Achse;–;
2;1;I;K5;Einsetzen;FG:punkt_graph;fehlende Koordinate;klein;
3;1;I;K5;Gleichung;LG:klammern;lineare Gleichung;klein;
4;1;II;K1;Ankreuzen;TU:aequivalenz;allgemeingültige Termaussagen;–;
5;1;II;K2;Ergänzen;TU:aequivalenz;Terme äquivalent ergänzen;Variable;
6;1;II;K3;Gleichung aufstellen;LG:sach;Verteilungssituation;klein;
7;1;I;K4;Zeichnen;KST:vierecke_konstruieren;gleichschenkliges Trapez;–;
8;1;II;K5;Koordinaten;GB:koordinaten;Streckenendpunkt aus Mittelpunkt;klein;
9;1;II;K3;Prozent;PZ:prozentsatz;Prozentsatz aus Anteil;klein;
10;1;II;K4;Erkennen;X:quadratische Terme/Gleichungen, Extremwerte (RS Kl. 8, Gym Kl. 9/10);Terme mit Extremwert;–;
11;1;II;K5;Zuordnen;BG:definitionsmenge;Bruchgleichungen zu D;klein;
12;1;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
13;1;I;K5;Ausklammern;TU:ausklammern;gemeinsamer Faktor;Variable;
14;1;II;K1;Ankreuzen;DD:tabelle_auswerten;Aussagen zum Gästediagramm;–;
15;1;III;K5;Wahrscheinlichkeit;X:mehrstufige Zufallsexperimente (Pfadregel, Kl. 9/10);Ziehen ohne Zurücklegen;klein;
16;1;II;K3;Sachaufgabe;LG:sach;Fahrpreis aus Gesamteinnahme;Euro;
17;2;II;K5;Winkel;KR:thales;Winkel im Kreis mit Parallelen;Grad;
18;1;II;K5;Fläche;FL:verstehen;Fläche aus Rechteckumfang;cm²;
19;1;II;K1;Begründen;KST:konstruierbar;unmögliches Dreieck;cm;
20;1;II;K3;Term;TA:sachsituation;Volumenterm mit Ausschnitten;Variable;
""")
GWT9(2017, "2017/2017_gwt_mathematik_9i_loesung.pdf", """
1a;1;I;K4;Ablesen;FLIN:ablesen;Geradengleichung ablesen;klein;
1b;1;I;K5;Prüfen;FG:punkt_graph;Punkt auf Gerade prüfen;klein;
1c;1;II;K5;Gleichung;FLIN:zwei_punkte;Gerade durch zwei Punkte;klein;
2;1;I;K6;Ankreuzen;FLIN:lage;Parallele zur y-Achse;–;
3;1;I;K5;Umformen;TU:binomisch;Klammer quadrieren, zusammenfassen;Variable;
4;1;II;K1;Prüfen;LG:probe;Lösung durch Probe prüfen;klein;
5;1;II;K5;Winkel;WS:figuren;Winkelbeziehungen in Figur;Grad;
6;1;II;K4;Zeichnen;KST:vierecke_konstruieren;Raute mit Seitenabstand;cm;
7;1;II;K5;Koordinaten;GB:vierecke;Diagonalenschnittpunkt Drachenviereck;klein;
8;1;II;K1;Beurteilen;PGW:mehrfach;Aktienwert über ein Jahr;Prozent;
9;1;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung mit D;klein;
10;1;II;K3;Schätzen;GR:schaetzen;Größenordnung eines Terms;groß;
11;1;II;K2;Angeben;X:quadratische Terme/Gleichungen, Extremwerte (RS Kl. 8, Gym Kl. 9/10);Term mit vorgegebenem Minimum;–;
12;1;II;K5;Wahrscheinlichkeit;STO:laplace;Stapelreihenfolge;klein;
13;1;II;K3;Indirekt;IND:dreisatz;Restdauer mit weniger Pumpen;h;
14;1;II;K3;Geschwindigkeit;GR:rechnen;Durchschnittsgeschwindigkeit;km/h;
15;1;II;K3;Volumen;VOL:rueckwaerts;Wasserstand aus Volumen;cm;
16;1;II;K1;Zuordnen;KON:symmetrie;Vierecke und Symmetrie;–;
17;1;I;K4;Konstruieren;KST:planfigur;Dreieck aus Seite und zwei Winkeln;cm;
18;1;II;K5;Winkel;WS:stufen_wechsel;Winkel an Parallelen;Grad;
19;1;II;K1;Begründen;KST:konstruierbar;gleichschenkliges Dreieck möglich?;Grad;
20;1;II;K5;Fläche;FL:verstehen;Fläche aus Umfang;cm²;
""", ges=22)
GWT9(2016, "2016/2016_gwt_rs_mathematik_9i_loesung.pdf", """
1a;1;I;K4;Zeichnen;FLIN:graph_ablesen;Gerade zeichnen;klein;
1b;1;II;K5;Angeben;FLIN:aufstellen;senkrechte Gerade nennen;klein;
1c;1;II;K5;Schnittpunkt;FLIN:schnittpunkte;Schnittpunkt zweier Geraden;klein;
2;1;I;K4;Ablesen;FLIN:ablesen;Steigung und Achsenabschnitt aus Gleichung;klein;
3;1;I;K5;Umformen;TU:summe_mal_summe;zwei Klammern ausmultiplizieren;Variable;
4;1;II;K4;Zuordnen;X:quadratische Terme/Gleichungen, Extremwerte (RS Kl. 8, Gym Kl. 9/10);Extremwerte zuordnen;klein;
5;1;I;K5;Gleichung;LG:klammern;lineare Gleichung mit Klammer;klein;
6;1;II;K4;Zeichnen;KST:vierecke_konstruieren;Viereck ergänzen;cm;
7;1;I;K5;Koordinaten;GB:vierecke;Parallelogrammpunkt;klein;
8;1;II;K1;Begründen;PZ:verstehen;Prozentbehauptung prüfen;Prozent;
9;1;II;K5;Bruchgleichung;BG:hauptnenner;D und L einer Bruchgleichung;klein;
10;1;II;K2;Ergänzen;PGN:mal_gleiche_basis;Zahlen für äquivalente Potenzterme;Variable;
11;1;II;K1;Ankreuzen;STO:laplace;Gewinnchancen beim Losziehen;klein;
12;1;II;K4;Tabellen;IND:unterscheiden;direkte und indirekte Tabelle ergänzen;klein;
13;1;III;K3;Modellieren;FL:sachaufgaben;Zuschauer aus Grundriss abschätzen;m²;
14;1;II;K5;Winkel;KR:thales;Winkel am Kreis;Grad;
15;1;II;K1;Ankreuzen;KON:vierecke_ordnen;Vierecke mit senkrechten Diagonalen;–;
16;1;II;K5;Winkel;WS:stufen_wechsel;Winkel an Parallelen;Grad;
17;1;II;K1;Ankreuzen;VOL:verstehen;Quader-Änderung für größeres Volumen;–;
18;1;II;K2;Fläche;FL:zerlegen;Rechteck aus geteiltem Quadrat;cm²;
19;1;II;K1;Ankreuzen;KST:kongruenzsatz;Kongruenzbedingungen;–;
""", ges=21)
GWT9(2015, "2015/2015_gwt_mathematik_9i_angabe.pdf", """
1a;1;I;K4;Zeichnen;FLIN:graph_ablesen;Gerade aus Steigung und Punkt;klein;
1b;1;I;K4;Ablesen;FLIN:ablesen;Geradengleichung angeben;klein;
2;1;II;K1;Ankreuzen;FLIN:deuten;Eigenschaften einer Geraden;–;
3;1;I;K5;Umformen;TU:summe_mal_summe;Klammern auflösen;Variable;
4;1;II;K5;Extremwert;X:quadratische Terme/Gleichungen, Extremwerte (RS Kl. 8, Gym Kl. 9/10);Extremwert ergänzen;klein;
5;1;I;K5;Gleichung;LG:klammern;lineare Gleichung;klein;
6;1;I;K5;Ausklammern;TU:ausklammern;gemeinsamer Faktor;Variable;
7;1;II;K5;Koordinaten;GB:koordinaten;Streckenendpunkt;klein;
8;1;II;K5;Koordinaten;GB:vierecke;Quadrat-Eckpunkt;klein;
9;1;II;K3;Rückwärts;GR:massstab;Kopiervergrößerung rückgängig;cm;
10;1;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
11;1;II;K5;Winkel;KST:gleichschenklig;Winkel im gleichschenkligen Dreieck;Grad;
12;1;II;K5;Wahrscheinlichkeit;STO:laplace;dritter Kugelzug;klein;
13;1;II;K5;Winkel;WS:stufen_wechsel;Winkel an Parallelen;Grad;
14;1;II;K3;Schätzen;GR:schaetzen;Autos vor der Fähre;m;
15;1;II;K4;Konstruieren;KR:umkehrung;rechtwinkliges Dreieck im Kreis;cm;
16;1;II;K1;Ankreuzen;BG:definitionsmenge;Bruchgleichungen mit gleicher D;–;
17;1;II;K1;Zuordnen;KON:vierecke_ordnen;Eigenschaften zu Vierecken;–;
18;1;II;K3;Indirekt;IND:dreisatz;Produktionszeit mit mehr Maschinen;h;
19;1;II;K3;Term;TA:sachsituation;Quadervolumen als Term;Variable;
20;1;II;K1;Begründen;KST:konstruierbar;Dreieck existiert nicht;cm;
21;1;III;K2;Gleichung;LG:sach;gleiche Flächen;Variable;
""", ges=22)
GWT9(2012, "2012/9i_angabe.pdf", """
1;3;I;K4;Gerade;FLIN:lage;Gerade zeichnen, Koordinate, Parallele;klein;
2;1;II;K6;Beschreiben;FLIN:lage;Gerade mit Steigung null;–;
3;1;II;K4;Ankreuzen;FG:wertetabelle;Term zur Wertetabelle;klein;
4;1;II;K1;Begründen;WS:stufen_wechsel;Winkelbeziehung begründen;Grad;
5;1;II;K5;Fläche;FL:verstehen;Fläche aus Umfang;cm²;
6;1;II;K3;Prozent;PGW:mehrfach;zwei Rabatte nacheinander;Prozent;
7;1;II;K3;Volumen;VOL:zusammengesetzt;gefaltete Schachtel;cm³;
8;2;II;K4;Diagramm;FG:graph_lesen;Fahrzeit ablesen, Fragen ankreuzen;h;
9;1;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
10;1;II;K1;Ankreuzen;TU:aequivalenz;korrekte Umformungen;–;
11;2;II;K5;Wahrscheinlichkeit;STO:laplace;Glücksrad, Teiler;klein;
12;1;II;K5;Ungleichung;UNG:umformen;Lösungsmenge auswählen;klein;
13;1;II;K5;Winkel;WS:figuren;Winkel im Trapez;Grad;
14;1;I;K5;Koordinaten;GB:vierecke;Parallelogrammpunkt;klein;
15;1;II;K2;Tabelle;TA:termwert;Produkt- und Summentabelle;klein;
16;1;II;K3;Umrechnen;GR:rechnen;Körperlängen pro Sekunde;s;
17;1;I;K4;Zeichnen;KON:achsenspiegelung;Drachenviereck an Achse ergänzen;–;
18;1;I;K4;Konstruieren;KST:planfigur;Dreieck aus Seite und Winkeln;cm;
""", ges=22)
# ---- bayerische Schulaufgaben, Exen, Stegreifaufgaben (klassenarbeiten.de)
def KA8(nr, titel, zeilen, nummer="unbekannt", ges=None, zeit=None, jahr=None, bl="Bayern (Annahme: Begriff „Schulaufgabe“)",
        passung="Gym Kl. 8, vermutlich Bayern (älterer G9-Lehrplan: einzelne Themen heute nicht mehr in Kl. 8)"):
    A(f"G8-K{nr}", quelle=KA + f"{nr}.pdf", titel=titel, herausgeber="klassenarbeiten.de (Schule unbekannt)", art=titel.split(" ")[0],
      nummer=nummer, jahr=jahr, zeit_min=zeit, punkte_gesamt=ges, hilfsmittel="nicht angegeben", frei=True, lizenz=LIZ_KA,
      bundesland=bl, passung=passung, klasse=8, zeilen=zeilen)


BET = "X:Betragsgleichungen/-ungleichungen (alter G9-Lehrplan)"
KA8(3795, "Schulaufgabe Proportionalität und Funktionen", """
1;?;I;K3;Tabelle;PROP:sach;Benzinkosten: Tabelle, Faktor, Vorschrift;Euro;
2;?;II;K3;Indirekt;IND:sach;Vorrat und tägliche Brenndauer;Liter;
3;?;II;K5;Funktion;FGB:achsenpunkte;D und Nullstelle einer gebrochen-rationalen Funktion;klein;
4;?;II;K4;Gerade;FLIN:graph_ablesen;Gerade zeichnen, D, Nullstelle;klein;
5;?;II;K5;Gleichung;FLIN:zwei_punkte;Gerade aus zwei Punkten, parallele Ursprungsgerade;klein;
""", nummer="Schulaufgabe (Annahme: 1. SA, Herbst)", bl="Bayern (laut Lösungsteil, G8)", passung="Gym Kl. 8 Bayern G8")
KA8(3809, "Stegreifaufgabe Proportionalität", """
1;2;I;K4;Graph;PROP:erkennen;Graph der Zuordnungsart zuordnen;–;
2;3;II;K1;Prüfen;PROP:pruefen;Tabelle prüfen, Ausreißer korrigieren;klein;
3;3;II;K3;Indirekt;IND:dreisatz;Kosten bei weniger Teilnehmern;Euro;
4;4;III;K3;Indirekt;IND:produkt;Anzahl Stücke bei anderen Maßen;cm²;
""", nummer="1. Stegreifaufgabe", ges=12, zeit=18, bl="Bayern (Annahme: Begriff „Stegreifaufgabe“)", passung="Gym Kl. 8, vermutlich Bayern")
KA8(3794, "Extemporale Proportionalität", """
1;12;II;K3;Indirekt;IND:sach;Vorrat: Reichweite berechnen, Diagramm zeichnen;Tage;
2;6;II;K3;Indirekt;IND:dreisatz;Arbeitszeit bei anderer Personen- und Stundenzahl;h;
3;7;II;K3;Indirekt;IND:erkennen;Druckzeiten berechnen, Zusammenhang beschreiben;min;
4;3;II;K3;Vergleich;PROP:einheit;günstigste Packung über Grundpreis;Euro;
5;3;I;K5;Tabelle;IND:produkt;Tabelle indirekter Proportionalität ergänzen;klein;
6;4;III;K1;Erklären;IND:produkt;Seite und Höhe bei konstanter Dreiecksfläche;cm;
""", nummer="Extemporale", ges=35, bl="Bayern (Annahme: Begriff „Extemporale“)", passung="Gym Kl. 8, vermutlich Bayern")
KA8(3629, "Schulaufgabe Terme und Vierecke (Gruppe A)", """
1;?;II;K5;Faktorisieren;TU:ausklammern;vier Terme vollständig faktorisieren;Variable;
2;?;I;K5;Definitionsmenge;BT:definitionsmenge;D zweier Bruchterme;klein;
3;?;I;K5;Erweitern;BT:erweitern;Brüche auf vorgegebenen Nenner erweitern;Variable;
4;?;II;K6;Benennen;KON:vierecke_ordnen;speziellstes Viereck zu Eigenschaften;–;
5;?;II;K5;Fläche;FV:trapez;Trapezfläche mit Mittenparallele;cm²;
6;?;II;K4;Konstruieren;KST:vierecke_konstruieren;Drachenviereck konstruieren und beschreiben;cm;
""", nummer="Schulaufgabe (Oktober)", jahr=2005)
KA8(3636, "Schulaufgabe Bruchterme und Geometrie", """
1;?;II;K5;Bruchterme;BT:addieren;Bruchterme addieren, dividieren, vereinfachen;Variable;
2;?;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
3;?;III;K3;Textaufgabe;BG:verhaeltnis;gemeinsames Arbeiten als Gleichung;h;
4;?;II;K6;Formulieren;KON:eigenschaften;Diagonaleigenschaften von Vierecken;–;
5;?;III;K1;Beweisen;KST:kongruenzsatz;Winkel und Streckengleichheit mit Kongruenz;–;
""", nummer="Schulaufgabe (Januar)", jahr=2006)
KA8(3635, "2. Schulaufgabe (Gruppe A)", """
1;?;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
2;?;II;K5;Betrag;X:Betragsgleichungen/-ungleichungen (alter G9-Lehrplan);zwei Betragsaufgaben ohne Rechnung;klein;
3;?;III;K5;Ungleichung;X:Betragsgleichungen/-ungleichungen (alter G9-Lehrplan);Bruchungleichung und Betragsgleichung mit Fallunterscheidung;klein;
4;?;II;K6;Formulieren;KST:satz_kehrsatz;Kehrsatz bilden, Aussage verneinen;–;
5;?;III;K1;Beweisen;KST:kongruenzsatz;zwei Lotstrecken gleich lang;–;
""", nummer="2. Schulaufgabe (Januar)", jahr=2005)
KA8(3642, "Schulaufgabe (Gruppe A)", """
1;?;II;K5;Betrag;X:Betragsgleichungen/-ungleichungen (alter G9-Lehrplan);Betragsungleichungen;klein;
2;?;II;K5;Umstellen;FO:zwei_schritte;Bruchgleichungen mit Parametern nach x auflösen;Variable;
3;?;II;K4;Graph;X:Betragsgleichungen/-ungleichungen (alter G9-Lehrplan);Wertetabelle und Graph einer Betragsfunktion;klein;
4;?;III;K4;Konstruieren;KR:tangente;Tangenten von einem Punkt an einen Kreis;cm;
5;?;III;K3;Modellieren;GR:massstab;Zuschauerraum im Grundriss entwerfen;m;
""", nummer="Schulaufgabe (März)", jahr=2006)
KA8(3645, "3. Schulaufgabe (Gruppe A)", """
1a;?;II;K5;Ungleichung;UNG:umformen;Bruchungleichung lösen;klein;
1b;?;II;K5;Betrag;X:Betragsgleichungen/-ungleichungen (alter G9-Lehrplan);Betragsungleichung ohne Rechnung;klein;
2;?;II;K5;Umstellen;FO:zwei_schritte;Formel nach einer Größe umstellen;–;
3a;?;III;K4;Konstruieren;KST:planfigur;Dreieck aus Seite, Gegenwinkel und Höhe;cm;
3b;?;II;K6;Beschreiben;KST:planfigur;Konstruktionsschritte beschreiben;–;
4a;?;II;K5;Fläche;FV:zusammengesetzt;schraffierte Figur;cm²;
4b;?;I;K4;Zeichnen;KD:schraegbild;Schrägbild eines Prismas;cm;
""", nummer="3. Schulaufgabe (März)", jahr=2001)
KA8(3648, "4. Schulaufgabe (Gruppe A)", """
1;?;II;K4;LGS;LGS:grafisch;LGS zeichnerisch und rechnerisch, Gerade aufstellen;klein;
2;?;III;K4;Konstruieren;X:Strecke in wahrer Größe (alter G9-Lehrplan);Raumstrecke im Würfel konstruieren;cm;
3;?;II;K3;Volumen;PZY:prisma_volumen;Deich mit Trapezquerschnitt;m³;
4;?;III;K4;Konstruieren;KR:umkreis_inkreis;Sehnenviereck aus Diagonalen und Winkel;cm;
""", nummer="4. Schulaufgabe (Juni)", jahr=2001)
KA8(3641, "Schulaufgabe Geometrie und Algebra", """
G1;10;III;K3;Vektoren;X:Vektoraddition, Windkorrektur (alter G9-Lehrplan);Flugzeug mit Wind;Grad;
G2;8;II;K5;Verschieben;KON:verschiebung;Dreieck mehrfach verschieben, Gesamtvektor;klein;
A1;10;II;K4;Funktionen;FG:mengen;Wertemengen, Graph zeichnen;klein;
A2;2;II;K5;Punktmengen;FLIN:lage;Punktmengen zu Geradengleichungen;klein;
A3;5;III;K1;Prüfen;PROP:pruefen;Konstanz eines Quotienten prüfen;klein;
""", nummer="Schulaufgabe", ges=35, zeit=90, passung="vermutlich Bayern, Klasse nicht angegeben (Annahme Kl. 8, alter G9-Lehrplan)")
