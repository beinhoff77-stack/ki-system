# LK-D 4 (B1): inhaltliche Entscheidung für Etappen ohne eigene Zuordnung, je Schulart.
# Format je Zeile: thema lernziel P<punkt> | K  #Grund
# P = Pflicht, integrativ durch den genannten Lehrplanpunkt (Quellen-Punkt, auch aus anderem Thema).
# K = Kür, Grund steht dahinter.
GYM = """
1 waage K #Gym 5 verlangt Probieren/Umkehraufgabe, das Waage-Modell (Äquivalenzumformung) kommt erst mit linearen Gleichungen
1 aufstellen K #Gym 5: Gleichungen nur formal lösen; Aufstellen aus Texten kommt mit Termen/Gleichungen in Kl. 7
1 ohne_loesung K #Lösbarkeit in Grundmengen wird in Gym 5 nicht verlangt
3 klammern P167 #rechnerisch lösen schließt Klammern und x auf beiden Seiten ein
3 pruefen P167 #Lösen schließt die Probe ein
3 sachaufgabe K #Punkt nennt keine Anwendungen
4 pruefen P179 #Auflösen schließt die Kontrolle der Umstellung ein
5 verhaeltnis P178 #Verhältnisgleichung ist die einfachste Bruchgleichung
6 loesung_parameter K #Parameterabhängige Lösungen gehen über „Lösbarkeit begründen“ hinaus
7 parabel P218 #Punkt nennt ausdrücklich „Parabel durch drei Punkte“
7 sachaufgabe P218 #„aufstellen“ verlangt Systeme aus Sachangaben
8 sachaufgabe K #Punkte nennen keine Anwendungen; Extremwertaufgaben liegen bei 35
9 naeherung K #Punkt verlangt exakte Lösungen; Näherung mit dem Taschenrechner nicht genannt
9 sachaufgabe K #Punkt nennt keine Anwendungen
10 wachstum P262 #Wachstumsmodelle (Punkt aus 37) führen auf Exponentialgleichungen
10 verstehen P260 #Logarithmus definieren schließt Aussagen über ihn prüfen ein
11 verstehen P278 #Aussagen über Nullstellen/Vielfachheit
14 tangens K #Gym 9: tan nur für spitze Winkel; Gleichungen tan x = v nicht verlangt
14 umformen K #nicht verlangt
14 anwendung K #Punkt nennt keine Anwendungen
15 dualsystem K #Gym 5 grenzt nur vom römischen System ab; Zweiersystem nicht verlangt
16 umkehraufgabe P13 #Gleichungen durch Umkehraufgabe lösen (Punkt aus 1)
17 vielfache P54 #kgV/Hauptnenner in Kl. 6 setzt Vielfache voraus
17 neunerregel K #Gym verlangt Regeln für 2, 3, 5, 10
18 umkehraufgabe_mal P29 #a·x = b durch Umkehraufgabe (Punkt aus 1)
19 zehnerpotenz P28 #große Zahlen mit Zehnerpotenzen (Gym 5)
19 gross_wissenschaftlich P28 #große Zahlen mit Zehnerpotenzen (Gym 5)
19 vorsilben_gross K #Mega/Giga/Tera nicht verlangt (Kilo steckt in Größen)
19 vergleichen_pruefen P75 #Zehnerpotenzen deuten schließt Vergleichen ein
21 verhaeltnis_kuerzen K #Verhältnisse sind im Gym 6 kein Stoff
21 gleichwertig K #Verhältnisse sind im Gym 6 kein Stoff
21 gemischte_zahlen P56 #Darstellungsvielfalt rationaler Zahlen
21 verstehen P56 #Unterschiede und Zusammenhänge der Zahlbereiche begründen
25 verstehen P39 #Rechnen mit Größen schließt Kontrolle von Maßzahl/Einheit ein
26 vervielfachen P41 #Schlussrechnung arbeitet mit Vervielfachen
26 pruefen P41 #Schlussrechnung setzt das Prüfen der Proportionalität voraus
26 geschickt P41 #geschickte Zwischenschritte sind Teil der Schlussrechnung
26 aenderung K #Änderungsraten sind kein Stoff von Gym 5
28 muster P107 #Zusammenhänge (auch Figurenfolgen) in Terme übersetzen
29 gleichungen_binomisch K #Gym 7 verlangt keine Gleichungen mit binomischen Ausdrücken (Entscheidung 17:05)
30 fehler_finden P74 #Anwenden schließt Fehlerkontrolle ein
31 termwert P175 #Definitionsmenge/Kürzen setzt Termwerte voraus
32 funktionswert P154 #Funktion mit Term beschreiben
32 stelle P158 #Punktlage bestimmen
33 lage P161 #m deuten: gleiche Steigung = parallel (orthogonal geht darüber hinaus)
33 einsetzen P161 #Parameter deuten
33 bueschel P161 #Parameter t bzw. m deuten
35 schnittpunkte P214 #quadratische Gleichungen aus Parabel-Gerade-Schnitt
36 negativ P235 #a·xⁿ mit ganzzahligem n
36 umkehrbar K #Umkehrfunktionen sind im Gym-9-Punkt nicht genannt (Annahme, nicht im Volltext geprüft)
36 linear K #wie umkehrbar
36 wurzelfunktion K #wie umkehrbar
36 quadratisch K #wie umkehrbar
36 spiegeln K #wie umkehrbar
37 punkte P259 #Graphen von b·aˣ deuten
37 logfunktion K #Gym 10 verlangt den Logarithmus als Zahl, nicht als Funktion
39 nullstellen P278 #Nullstellen mit Vielfachheit (Punkt aus 11)
42 verstehen P18 #fachsprachlich benennen schließt Aussagen prüfen ein
44 vierecke K #Gym 7 konstruiert nur Dreiecke; 44 Teil 2 bleibt Zusatz (Entscheidung 16:20)
44 vierecke_konstruieren K #wie vierecke
46 verschiebung K #Gym 7: nur Achsen- und Punktspiegelung
46 gegenvektor K #Vektoren kein Stoff Gym 7
46 drehung K #Gym 7: Punktspiegelung ja, allgemeine Drehung nicht
46 eigenschaften P120 #symmetrische Figuren konstruieren setzt Längen-/Winkeltreue voraus
46 vektor_koordinaten K #Vektoren kein Stoff Gym 7
46 vektor_drehen K #Vektoren kein Stoff Gym 7
47 streckung P230 #Ähnlichkeit über zentrische Streckung
47 bildgerade K #nicht verlangt
47 schwerpunkt K #nicht verlangt
47 streckung_vektor K #nicht verlangt
51 sektor K #Gym 8 nennt nur Umfang und Fläche des ganzen Kreises (Annahme)
51 zusammengesetzt K #wie sektor
52 ansichten K #nicht verlangt
52 beurteilen P195 #Netze/Schrägbilder beurteilen
53 sachaufgaben P48 #zusammengesetzte Körper, Anwendung
53 verstehen P48 #Oberflächen prüfen
55 schnittwinkel K #Steigungswinkel nicht verlangt
56 additionstheoreme K #nicht verlangt
60 reihenfolgen P26 #Zählprinzip
60 bedingungen P26 #Zählprinzip
60 verstehen P26 #prüfen, ob das Zählprinzip anwendbar ist
62 simulation K #nicht verlangt
62 pi_schaetzen K #nicht verlangt
62 verstehen P265 #Pfadregeln plausibel machen
63 bedingt K #bedingte Wahrscheinlichkeit kein Stoff Gym 9
63 rueckschluss K #wie bedingt
67 vertauschen P28 #Potenzschreibweise
67 sach P28 #große Zahlen mit Zehnerpotenzen im Alltag
68 kubikwurzel P236 #allgemeine Wurzel (Punkt aus 9)
68 wurzel_sache K #Punkte nennen keine Anwendungen
73 sachsituationen K #Punkt nennt keine Anwendungen
73 verstehen P19 #Punkte mit Abstandsbedingungen
91 lage K #Gym 10 nennt nur Schrägbilder/Netze und Rotationskörper
91 koordinaten K #wie lage
91 axialschnitt P289 #Körperberechnungen „auch Längen und Winkel“ (Punkt aus 92)
91 wahre_groesse P282 #Schrägbilder zeichnen braucht Verkürzung
91 koerper_symmetrie K #nicht verlangt
91 raumwinkel P289 #Winkel an Körpern (Punkt aus 92)
92 pyr_oberflaeche P289 #Körperberechnungen
93 vervielfachen P173 #indirekte Proportionalität anwenden
93 sach P173 #anwenden
94 formel P136 #komplexere Prozentaufgaben, mehrfache Änderung
96 gleichung_exp P236 #Potenzgleichungen (Punkt aus 9)
96 verstehen P239 #Potenzen und Wurzeln zusammenfassen
98 parkett K #nicht verlangt
98 beweisen P127 #Innenwinkelsumme beweisen
99 drachen_raute K #Gym 6 nennt Parallelogramm, Dreieck, Trapez
103 fehler_ganz P177 #anwenden schließt Fehlerkontrolle ein
43 ergaenzen P20 #Winkel beschreiben (Nebenbezug von 42)
43 kreuzung P126 #Winkel an Geradenkreuzungen (Punkt aus 98)
43 um_punkt P20 #Winkel bis 360°
43 uhr P20 #Winkel bis 360°
43 drehungen P20 #Winkel bis 360°
43 figuren P20 #Winkel beschreiben
43 verstehen P20 #Winkel beschreiben
69 lesen P167 #Intervallschreibweise
69 schreiben P167 #Intervallschreibweise
69 enthalten P167 #Intervallschreibweise
69 beurteilen P167 #Intervallschreibweise
71 begriffe P98 #einfache Zinsaufgaben (Punkt aus 24)
71 rollen P98 #einfache Zinsaufgaben
71 jahreszinsen P98 #einfache Zinsaufgaben
71 jahreszinsen_komma P98 #einfache Zinsaufgaben
71 zinssatz P98 #einfache Zinsaufgaben
71 kapital P98 #einfache Zinsaufgaben
71 monatszinsen K #Zinsen für Teile des Jahres gehen über „einfach“ hinaus
71 zeitanteil K #wie monatszinsen
"""
# RS I und RS II/III: gleiche Entscheidung, Punkt je Gruppe (I/II_III)
RS = """
1 ohne_loesung P382/P382 #Lösungsmenge bei verschiedenen Grundmengen
2 probe P703/P718 #Lösen schließt die Probe ein
2 sonderfaelle P703/P718 #Äquivalenzumformung führt auf Sonderfälle
3 klammern P704/P719 #Lösen von Ungleichungen mit vereinfachten Seiten
3 pruefen P704/P719 #Lösen schließt die Probe ein
3 grafisch K/K #zeichnerisches Lösen nicht genannt
3 sachaufgabe P705/P720 #Gleichungen/Ungleichungen aus Sachsituationen
5 ein_bruch P737/P752 #einfache Bruchgleichung
5 ueber_kreuz P737/P752 #a/b = c/d lösen
5 hauptnenner K/K #über einfache Verhältnisgleichungen hinaus
5 scheinloesung P737/P752 #Definitionsmenge bestimmen
5 graphisch K/K #nicht genannt
6 pruefen P786/P815 #Lösen schließt die Probe ein
6 verfahren P786/P815 #drei Verfahren vergleichen
6 loesbarkeit P786/P815 #zeichnerisch: parallele/identische Geraden
6 loesung_parameter K/K #nicht genannt
6 sachaufgabe P786/P815 #Geometrie- und Sachprobleme
8 ausklammern P793/- #quadratische Gleichungen bearbeiten (II/III schon zugeordnet)
8 faktorisieren P793/- #wie ausklammern
8 bruchgleichung K/K #nicht genannt
8 sachaufgabe P791/P858 #quadratische Modelle (Punkt aus 35)
10 gleiche_basis P841/P852 #Exponentialgleichungen lösen
10 potenzregel -/K #II/III: nur a^x = b mit dem Logarithmus
10 wachstum P843/P1013 #Wachstum (Punkt aus 37)
10 verstehen P841/P852 #Logarithmus verwenden
13 sachaufgabe K/- #Punkt nennt keine Anwendungen
14 anzahl P827/- #trigonometrische Gleichungen lösen
15 zahlwort_zu_ziffern P293/P293 #Stellenwertsystem
15 ziffern_zu_zahlwort P293/P293 #Stellenwertsystem
15 strahl_eintragen P294/P294 #Zahlenstrahl
16 schriftlich_plus_minus P300/P300 #schriftliche Rechenverfahren (Punkt aus 18)
16 umkehraufgabe K/K #Gleichungen erst in Kl. 6
16 verstehen P315/P315 #Rechenregeln begründen
17 endziffer P305/P305 #Teilbarkeit
17 quersumme P305/P305 #Teilbarkeit
17 neunerregel P305/P305 #Teilbarkeit (RS nennt keine Auswahl der Regeln)
17 primzahl P305/P305 #Primfaktoren
18 punkt_strich P316/P316 #gemischte Rechnungen (Punkt aus 16)
18 klammern P316/P316 #gemischte Rechnungen
18 termaufbau P316/P316 #gemischte Rechnungen
18 differenz_summe P302/P302 #Rechengesetze
18 mal_ganz P315/P315 #Vorzeichenregeln
18 geteilt_ganz P315/P315 #Vorzeichenregeln
18 umkehraufgabe_mal K/K #Gleichungen erst in Kl. 6
19 negativer_exponent P866/P904 #10⁻¹⁸ bis 10¹⁸
19 vergleichen_pruefen P866/P904 #darstellen schließt Vergleichen ein
20 eingrenzen P759/P804 #Wurzelwerte näherungsweise einschätzen
20 heron K/K #nicht genannt
20 wurzel_mal -/P972 #Wurzelterme umformen
20 nenner_rational -/K #II/III nennt kein Rationalmachen
21 verhaeltnis_kuerzen P388/P388 #einfache Verhältnisgleichungen (Punkt aus 26)
21 gleichwertig P388/P388 #wie verhaeltnis_kuerzen
21 verstehen P349/P349 #Erweitern/Kürzen begründen
22 vergleichen_ordnen P350/P350 #Dezimalzahlen
22 verstehen P350/P350 #Dezimalzahlen
23 potenzen K/K #nicht genannt
23 gemischt P355/P355 #rechnen mit rationalen Zahlen
23 fehler_finden P356/P356 #Rechenregeln
24 rabatt_aufschlag P390/P390 #Prozentrechnung
24 verstehen P390/P390 #Prozentrechnung
25 verstehen P333/P333 #Größen modellieren
26 geschickt P332/P332 #Dreisatz
26 sach P332/P332 #Dreisatz in Sachsituationen
26 aenderung K/K #nicht genannt
28 muster P377/P377 #Terme aufstellen
30 potenz_begriff P304/P304 #Potenzen (Punkt aus 67)
30 fehler_finden P864/P902 #berechnen schließt Fehlerkontrolle ein
31 termwert P736/P751 #Einsetzbereich
31 kuerzen K/K #RS 8 verlangt nur Einsetzbereich und einfache Verhältnisgleichungen
31 erweitern K/K #wie kuerzen
31 addieren K/K #wie kuerzen
31 multiplizieren K/K #wie kuerzen
31 fehler_finden K/K #wie kuerzen
32 stelle P944/P963 #Werte berechnen, Darstellungen wechseln
32 graph_lesen -/P963 #Darstellungen wechseln
32 punkt_graph P944/P963 #wie stelle
33 proportional P386/- #Halbgerade durch den Ursprung (Punkt aus 26)
33 schnittpunkte P786/P815 #Systeme zeichnerisch lösen (Punkt aus 6)
33 einsetzen -/P988 #Parameter erklären
35 spiegeln P788/P855 #Parameter a < 0
35 nullstellen P793/P859 #quadratische Gleichungen (Punkt aus 8)
35 schnittpunkte -/P860 #Gerade–Parabel
36 werte P838/- #Potenzfunktionen untersuchen
36 symmetrie P838/- #Potenzfunktionen untersuchen
36 linear P838/- #Umkehrfunktion
36 quadratisch P838/- #Umkehrfunktion
36 spiegeln P838/- #Umkehrfunktion
37 werte P842/- #Exponentialfunktion analysieren
37 punkte -/P1012 #y = k·aˣ zeichnen
37 logfunktion -/K #II/III: keine Logarithmusfunktion
38 bogenmass K/K #nicht genannt (Annahme)
38 parameter K/K #Punkt nennt nur periodische Beschreibung (Annahme)
38 verschiebung_x K/K #wie parameter
38 zuordnen P821/P1001 #Graphen beschreiben
38 eigenschaften P821/P1001 #Graphen beschreiben
38 anwendung P827/P1001 #periodische Vorgänge
42 verstehen P320/P320 #Eigenschaften beschreiben
44 gleichschenklig P877/P954 #Dreieckskonstruktionen
44 satz_kehrsatz -/K #II/III: nur Kongruenz prüfen, nicht beweisen
45 thales K/P914 #RS I: kein Punkt zum Thaleskreis gefunden; II/III: Thaleskreis als Ortslinie
45 umkehrung K/P914 #wie thales
45 beweis K/K #nicht genannt
46 punktspiegelung -/K #II/III: Punktspiegelung nicht genannt (46 Teil 3 bleibt dort Zusatz)
46 drehung -/K #wie punktspiegelung
46 vektor_drehen -/K #wie punktspiegelung
47 bildgerade K/K #nicht genannt
47 schwerpunkt K/K #nicht genannt
47 aehnlich -/P974 #Eigenschaften und Verhältnisgleichheit
47 streckung_vektor K/K #nicht genannt
49 inverse K/- #nicht genannt
50 einheitsquadrate P339/P339 #Flächeninhalt
50 kommaschreibweise P338/P338 #Flächeneinheiten
50 verstehen P339/P339 #Fläche und Umfang
51 verstehen -/P985 #Proportionalitäten am Kreis
52 zylinder P324/P324 #Körper erkennen
52 beurteilen P324/P324 #Körper beschreiben
53 zusammengesetzt P370/P370 #Oberflächen aus Quadern
53 verstehen P370/P370 #Oberflächen
55 seiten P776/P983 #Seitenverhältnisse
55 beziehungen K/P999 #RS I 9 nennt keine Grundbeziehungen; II/III in Kl. 10 (Punkt aus 56)
55 anwendung P776/P983 #Aufgaben in Ebene/Raum
55 schnittwinkel K/P1000 #II/III: m = tan α (Punkt aus 56)
56 additionstheoreme -/K #nicht genannt
56 satz_waehlen -/P1003 #Sinus-/Kosinussatz
57 relative_haeufigkeit P951/P969 #relative Häufigkeiten (Punkt aus 61)
57 saeulendiagramm P342/P342 #Diagramme
57 kreisdiagramm P352/P352 #Prozent und Grafik (Punkt aus 22)
58 mittel_tabelle P897/P925 #Mittelwert
58 mittel_rueckwaerts P897/P925 #Mittelwert
60 reihenfolgen P307/P307 #Zählprinzip
60 bedingungen P307/P307 #Zählprinzip
60 grenzen P307/P307 #Zählprinzip
60 verstehen P307/P307 #Zählprinzip
62 ohne_zuruecklegen P845/P1015 #mehrstufige Versuche
62 unabhaengig K/K #nicht genannt
62 gegenereignis -/P1016 #Pfadregeln
62 simulation K/K #nicht genannt
62 pi_schaetzen K/K #nicht genannt
62 verstehen P846/P1016 #Pfadregeln
67 vertauschen P304/P304 #Potenzen
67 negativ K/K #negative Basen nicht genannt
67 sach P304/P304 #exponentielles Wachstum beschreiben
71 begriffe P892/P920 #Zinsrechnung
71 rollen P892/P920 #Zinsrechnung
71 jahreszinsen_komma P892/P920 #Zinsrechnung
71 monatszinsen P892/P920 #Zinsrechnung mit Kapital/Zinssatz/Zinsen
71 zeitanteil P892/P920 #wie monatszinsen
73 verstehen -/P916 #Punkteigenschaften versprachlichen
74 umlaufsinn P872/P910 #Determinanten
74 vieleck -/K #II/III: nur Dreiecke/Vierecke
81 hochrechnen K/K #nicht genannt
81 aussagen P899/P927 #Repräsentativität beurteilen
91 lage -/K #II/III: nicht genannt
91 koordinaten -/K #II/III: nicht genannt
91 koerper_symmetrie -/K #II/III: nicht genannt
91 raumwinkel -/K #II/III: nicht genannt
92 verstehen P783/P1009 #modellierend berechnen
93 sach P894/P921 #Sachsituationen
94 zurueck -/P919 #erhöhter/verringerter Grundwert
94 prozentsatz P891/P919 #vermehrter/verminderter Grundwert
94 mehrfach P891/P919 #vermehrter/verminderter Grundwert
94 formel K/K #nicht genannt
94 argumente P891/P919 #anwenden
95 quartile P898/P926 #Kennwerte
95 boxplot P898/P926 #Kennwerte interpretieren
95 vergleichen P898/P926 #Aussagekraft
96 gleichung_exp P837/- #x^n = a (II/III: Thema ohne Punkt)
96 verstehen P836/- #Potenzgesetze
98 scheitel_neben P323/P323 #Scheitel- und Nebenwinkel (Punkt aus 42)
98 parkett K/K #nicht genannt
98 figuren P874/- #Winkel berechnen
98 beweisen P873/P911 #Parallelität begründen
99 oberflaeche P370/P370 #Oberfläche von Quader und Würfel (Punkt aus 53)
101 prisma_volumen P783/P1009 #Prismen/Zylinder modellieren und berechnen (Punkt aus 92)
101 prisma_oberflaeche P783/P1009 #wie prisma_volumen
101 prisma_umstellen P783/P1009 #wie prisma_volumen
101 zylinder_volumen P783/P1009 #wie prisma_volumen
101 zylinder_oberflaeche P783/P1009 #wie prisma_volumen
101 sach P783/P1009 #wie prisma_volumen
101 verstehen P781/P1007 #Volumenbestimmung erläutern
102 anwenden P865/P903 #Potenzgesetze anwenden
9 gerade P837/- #x^n = a (Nebenbezug)
9 ungerade P837/- #x^n = a
9 anzahl P837/- #x^n = a
9 umformen P837/- #x^n = a
9 naeherung K/- #nicht genannt
9 sachaufgabe P839/- #Anwendungsprobleme (Nebenbezug)
43 ergaenzen P322/P322 #Winkel 0°–360° (Nebenbezug)
43 kreuzung P323/P323 #Scheitel- und Nebenwinkel
43 um_punkt P322/P322 #Winkel 0°–360°
43 uhr P322/P322 #Winkel 0°–360°
43 drehungen P322/P322 #Winkel 0°–360°
43 figuren P874/P912 #Winkel berechnen (Punkt aus 98)
43 verstehen P323/P323 #Winkel begründen
63 elemente P801/- #mengenbasiert (Nebenbezug)
63 schnitt P801/- #mengenbasiert
63 verknuepfen P801/- #mengenbasiert
63 mengen_verstehen P801/- #mengenbasiert
63 venn P801/- #mengenbasiert
63 vierfeld P950/- #Vierfeldertafel (Nebenbezug)
63 additionssatz K/- #nicht genannt
63 tafel_wkeit K/- #nicht genannt
63 bedingt K/- #nicht genannt
63 rueckschluss K/- #nicht genannt
63 verstehen K/- #nicht genannt
64 zufallsgeraet P798/P993 #Simulation (Nebenbezug)
64 regel P798/P993 #Simulation
64 zufallsziffern P798/P993 #Simulation
64 auswerten P798/P993 #Simulation
64 monte_carlo K/K #nicht genannt
64 beurteilen P798/P993 #Simulation
68 quadratwurzel P758/P971 #Quadratwurzel (Nebenbezug)
68 wurzel_dezimal P759/P804 #Wurzelwerte
68 kubikwurzel P837/K #RS I: n-te Wurzel in Kl. 10; II/III nicht genannt
68 abschaetzen P759/P804 #Wurzelwerte einschätzen
68 wurzel_deuten P758/P971 #Quadratwurzel erklären
68 wurzel_sache P759/P804 #x² = a lösen
69 lesen P704/P719 #Intervalle (Nebenbezug)
69 schreiben P704/P719 #Intervalle
69 enthalten P704/P719 #Intervalle
69 beurteilen P704/P719 #Intervalle
103 warum_gilt P865/- #Potenzgesetze (Nebenbezug)
103 gleiche_basis_ganz P865/- #Potenzgesetze
103 exponent_und_potenz P865/- #Potenzgesetze
103 terme_vereinfachen P865/- #Potenzgesetze
103 fehler_ganz P865/- #Potenzgesetze
20 irrational_beweis K/K #RS verlangt Irrationalität nennen/erklären (758/971), keinen Beweis
"""
def lesen():
    E = {}
    for z in GYM.strip().splitlines():
        a, g = z.split('#', 1); t, e, x = a.split()
        E[('gym', int(t), e)] = (x, g.strip())
    for z in RS.strip().splitlines():
        a, g = z.split('#', 1); t, e, x = a.split(); i, ii = x.split('/')
        for sch, v in (('rs_I', i), ('rs_II_III', ii)):
            if v != '-': E[(sch, int(t), e)] = (v, g.strip())
    return E
