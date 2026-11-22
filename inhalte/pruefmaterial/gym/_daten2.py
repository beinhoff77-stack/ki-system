# Zweite Sammelrunde (Ziel 50 Arbeiten je Klasse), wird von _bau.py per exec eingelesen.
# Format wie in _bau.py. Nur eigene Worte, keine Aufgabentexte, keine Lösungen.

ISB_RS = "https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/"
ZFB = "https://jahrgangsstufenarbeiten.zfb.mwn.de/download/"
ISB_MS = "https://www.isb.bayern.de/fileadmin/user_upload/Mittelschule/Jahrgangsstufenarbeiten/Mathematik/"

def JT6(jahr, url, zeilen):
    A(f"G5-R{jahr}", quelle=url, titel=f"Jahrgangsstufentest Mathematik 6 Realschule {jahr}", herausgeber="ISB Bayern (Realschule)",
      art="Jahrgangsstufentest Realschule Jgst. 6 (prüft Kl.-5-Stoff der Realschule)", nummer="Beginn Kl. 6 (Sept.)", jahr=jahr,
      zeit_min=45, punkte_gesamt=21, hilfsmittel="kein Taschenrechner", frei=True, lizenz=LIZ_ISB, bundesland="Bayern",
      passung="Bayern amtlich, aber Realschule (Stoff ähnlich Gym 5; ältere Jahrgänge mit Brüchen)", klasse=5, zeilen=zeilen)

def MS6(jahr, url, zeilen, schulart="Mittelschule", zeit=45):
    A(f"G5-{schulart[0]}{jahr}", quelle=url, titel=f"Jahrgangsstufenarbeit Mathematik 6 {schulart} {jahr}", herausgeber=f"ISB Bayern ({schulart})",
      art=f"Jahrgangsstufenarbeit {schulart} Jgst. 6 (prüft Kl.-5-Stoff der {schulart})", nummer="Beginn Kl. 6 (Sept./Okt.)", jahr=jahr,
      zeit_min=zeit, punkte_gesamt=24, hilfsmittel="kein Taschenrechner", frei=True, lizenz=LIZ_ISB, bundesland="Bayern",
      passung=f"Bayern amtlich, aber {schulart} (Niveau niedriger als Gym; Brüche enthalten)", klasse=5, zeilen=zeilen)

JT6(2025, ISB_RS+"2025/2025_JT_Mathematik_6_Angabe.pdf", """
1a;1;I;K5;Rechnen;RG:klammern;Term mit Klammer, Mal und Plus;zweistellig;
1b;1;I;K5;Rechnen;RG:schriftlich_geteilt;Division;vierstellig;
2a;1;I;K5;Rechnen;BRR:dezimal_plus_minus;Rechnung mit Bruch-/Dezimalzahlen;klein;Kl.-6-Stoff Gym
2b;1;I;K5;Rechnen;RG:geteilt_ganz;Division;klein;
3;1;II;K2;Zahl bilden;NAT:stellenwert;größte Zahl aus Ziffernkarten;elfstellig;
4;1;II;K1;Fehler finden;RG:termaufbau;Fehler in einer Rechnung beschreiben;klein;
5;1;II;K2;Teilbarkeit;TB:endziffer;Endziffern für zwei Teilbarkeiten wählen;fünfstellig;
6;1;I;K5;Ankreuzen;TB:primzahl;Nicht-Primzahl erkennen;zweistellig;
7;1;I;K4;Zahlenstrahl;NAT:strahl_eintragen;Zahl am Zahlenstrahl markieren;groß;
8;1;II;K5;Ergänzen;GZ:umkehraufgabe;fehlende Zahl ergänzen;klein;
9;1;II;K3;Sachaufgabe;GZ:sach;Temperatur nach Erwärmung;Grad;
10;1;II;K5;Winkel;WI:kreuzung;Winkel in Zeichnung bestimmen;Grad;Nebenwinkel
11;1;I;K4;Messen;GB:winkelarten;Winkel messen;Grad;
12;1;I;K4;Zeichnen;GB:lagebeziehungen;Parallele durch Punkt;–;
13;1;I;K1;Ankreuzen;KB:verstehen;Aussage zu Pyramiden;–;
14;1;II;K5;Ordnen;GR:masse;Massen umrechnen und ordnen;gemischt;
15;1;II;K3;Schätzen;GR:schaetzen;Höhe aus Bild schätzen;m;
16;1;II;K3;Sachaufgabe;PROP:sach;Entfernung nach Faustregel;km;
17;1;II;K5;Fläche;FL:zerlegen;zusammengesetzte Figur;cm²;
18;1;II;K1;Ankreuzen;FL:verstehen;Quadrat aus Umfang und Fläche erkennen;klein;
19;1;II;K4;Diagramm;DD:saeulendiagramm;Säulen passend zur Summe ergänzen;klein;Daten = Kl. 6 Gym
""")
JT6(2024, "https://isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/2024_JT_Mathe_6_Angabe.pdf", """
1a;1;I;K5;Rechnen;RG:punkt_strich;Term mit Plus und Mal;klein;
1b;1;I;K5;Potenz;POT:berechnen;Potenz berechnen;klein;
2a;1;I;K5;Geschickt;RG:vorteil;Produkt aus drei Faktoren geschickt;klein;
2b;1;I;K5;Rechnen;GZ:addieren;Addition mit negativer Zahl;klein;
3;1;III;K2;Zahlenmuster;NAT:vergleichen;kleinste Zahl mit Ziffernmuster im Bereich;groß;
4;1;I;K4;Zahlenstrahl;NAT:strahl_eintragen;große Zahl markieren;Hunderttausender;
5;1;II;K1;Ankreuzen;NAT:runden_regel;korrekt gerundete Zahl;groß;
6;1;II;K5;Ergänzen;GZ:ordnen;nächstgrößere ganze Zahl zu negativer Zahl;klein;
7;1;II;K2;Offen;RG:geteilt_ganz;Division mit negativem Ergebnis bilden;klein;offen
8;1;II;K2;Teilbarkeit;TB:quersumme;vierstellige Zahl teilbar durch 3;vierstellig;offen
9;1;II;K3;Sachaufgabe;KB:quader;Quaderhöhe aus Netzmaßen;cm;
10;1;I;K4;Zeichnen;GB:lagebeziehungen;Senkrechte durch Punkt;–;
11;1;II;K4;Zeichnen;L:GB:Kreissektor mit vorgegebenem Mittelpunktswinkel zeichnen;Kreissektor einzeichnen;Grad;
12;1;III;K2;Zählen;KB:zusammengesetzt;Würfel mit genau einer gefärbten Seite;klein;Raumvorstellung
13;1;I;K5;Umrechnen;GR:laenge;dm in mm;klein;
14;1;II;K3;Sachaufgabe;TB:teiler;passende Brettbreite;cm;
15;1;II;K1;Begründen;GR:rechnen;Fehler beim Rückgeld erklären;Euro;
16;1;II;K3;Hochrechnen;PROP:sach;Plätze aller Gondeln hochrechnen;zweistellig;
17;1;II;K3;Schätzen;FL:einheitsquadrate;Blattfläche über Kästchen schätzen;cm²;
18;1;III;K2;Ankreuzen;FL:verstehen;Quadrat mit gleicher Maßzahl von Umfang und Fläche;klein;
19;1;II;K4;Diagramm;DD:saeulendiagramm;Gesamtzahl aus Balkendiagramm;zweistellig;
""")
JT6(2023, ISB_RS+"2023/2023_JT_Mathe_6_Angabe.pdf", """
1a;1;I;K5;Rechnen;RG:schriftlich_geteilt;Division;vierstellig;
1b;1;II;K5;Ergänzen;GE:zwei_schritte;fehlendes Zeichen bzw. Zahl in Gleichung;klein;
2a;1;I;K5;Rechnen;GZ:schriftlich_plus_minus;Rechnung mit vierstelligen Zahlen;vierstellig;
2b;1;I;K5;Rechnen;RG:mal_ganz;Produkt zweier negativer Zahlen;klein;
3;1;II;K4;Fehler finden;NAT:strahl_ablesen;falsch eingetragene Zahl korrigieren;groß;
4;1;III;K1;Begründen;TB:quersumme;alle Kartenzahlen durch 3 teilbar begründen;vierstellig;
5;1;I;K5;Runden;NAT:runden_regel;auf Tausender runden;sechsstellig;
6;1;II;K5;Ankreuzen;L:GE:Ungleichungen über N über die zugehörige Gleichung lösen;größte Zahl, die Aussage wahr macht;klein;
7;1;II;K3;Sachaufgabe;RG:sach;Fensterzahl aus Stockwerken und Wohnungen;klein;
8;1;III;K1;Fehler finden;GR:schaetzen;Fehler bei Hochrechnung beschreiben;groß;
9;1;II;K6;Ankreuzen;RG:termaufbau;Text zum Term wählen;–;
10;1;I;K4;Messen;GB:lagebeziehungen;Abstand Punkt–Gerade;cm;
11;1;II;K6;Begründen;KB:verstehen;Unterschied Kegel–Pyramide;–;
12;1;II;K4;Zeichnen;L:KB:Netz eines Quaders zeichnen (Kl. 5);Faltlinien für Quader einzeichnen;–;
13;1;I;K4;Zeichnen;GB:winkelarten;stumpfen Winkel zeichnen;Grad;
14;1;II;K5;Ankreuzen;FL:einheiten;Fläche aus gemischten Einheiten;gemischt;
15;1;I;K3;Dreisatz;PROP:dreisatz;Gesamtpreis für größere Gruppe;Euro;
16;1;II;K3;Maßstab;GR:massstab;passenden Maßstab wählen;–;
17;1;II;K4;Zeichnen;FL:rechteck;Rechteck mit vorgegebener Fläche;cm²;
18;1;II;K3;Umfang;FL:verstehen;Umfang eines Teilrechtecks;cm;
19;1;I;K4;Diagramm;DD:saeulendiagramm;Säule halb so hoch ergänzen;–;
""")
JT6(2022, ISB_RS+"2022/_A__2022_JT_Mathe_6_Angabe.pdf", """
1a;1;I;K5;Rechnen;RG:schriftlich_geteilt;Division durch Zweistellige;mehrstellig;
1b;1;I;K5;Rechnen;GZ:ketten;gemischte Rechnung mit Vorzeichen;klein;
2a;1;I;K5;Geschickt;RG:vorteil;drei Faktoren geschickt;klein;
2b;1;I;K5;Rechnen;RG:schriftlich;schriftlich multiplizieren;mehrstellig;
3;1;II;K1;Fehler finden;GZ:verstehen;fehlendes Minus ergänzen;klein;
4;1;II;K2;Offen;RG:mal_ganz;zwei ganze Zahlen mit gegebenem Produkt;klein;offen
5;1;III;K2;Optimieren;NAT:stellenwert;Ziffernkarten für maximale Differenz;mehrstellig;
6;1;I;K5;Zählen;KOMB:zaehlprinzip;Kleidungskombinationen;klein;
7;1;II;K1;Ankreuzen;NAT:runden_regel;größter Wert mit gegebener Rundung;groß;
8;1;II;K5;Winkel;WI:kreuzung;Winkel an Geradenkreuzung;Grad;
9;1;II;K2;Muster;L:RG:Zahlenfolgen – Bildungsregel erkennen und fortsetzen;erstes Folgeglied ergänzen;klein;
10;1;II;K3;Sachaufgabe;GR:zeit;Zeit aus Geschwindigkeit;Minuten;
11;1;I;K4;Zeichnen;GB:winkelarten;Winkel zeichnen;Grad;
12;1;I;K4;Zeichnen;GB:koordinaten;Koordinatensystem, Punkt eintragen;klein;
13;1;II;K5;Ankreuzen;FL:rechteck;Seite aus Breite und Umfang;cm;
14;1;II;K3;Sachaufgabe;RG:sach;Gewicht als Vielfaches;kg;
15;1;II;K3;Schätzen;GR:massstab;Durchmesser auf Karte abschätzen;km;
16;1;II;K4;Diagramm;DD:saeulendiagramm;Balken nach Anteil ergänzen;–;
17;1;I;K5;Ankreuzen;KB:verstehen;Ecken, Kanten, Flächen einer Pyramide;klein;
18;1;II;K5;Maßstab;GR:massstab;längste reale Straße;km;
19;1;III;K1;Fehler finden;FL:zerlegen;Fehler in Flächenzerlegung;cm²;
""")
JT6(2021, ISB_RS+"2021/2021_jt_mathe_6_angabe.pdf", """
1a;1;I;K5;Rechnen;RG:schriftlich_geteilt;Division;mehrstellig;
1b;1;I;K5;Rechnen;GZ:subtrahieren;Differenz;klein;
2a;1;I;K5;Rechnen;RG:mal_ganz;Produkt mit negativer Zahl;klein;
2b;1;I;K5;Rechnen;POT:berechnen;Term mit Quadrat;klein;
3;1;III;K2;Zählen;KOMB:zaehlprinzip;fehlende Anzahl aus Menüzahl rückwärts;klein;umgekehrt
4;1;II;K2;Teilbarkeit;TB:vielfache;Zahl teilbar durch zwei Zahlen im Bereich;zweistellig;
5;1;I;K5;Stellenwert;NAT:zahlwort_zu_ziffern;Zahlwort in Stellenwerttafel;groß;
6;1;II;K3;Sachaufgabe;FL:sachaufgaben;Mindestfläche eines Plakats;cm²;
7;1;II;K3;Maßstab;GR:massstab;Vergrößerungsmaßstab wählen;–;
8;1;I;K4;Zeichnen;GB:lagebeziehungen;Punkt auf einer, nicht auf anderer Geraden;–;
9;1;II;K2;Ergänzen;NAT:runden_uebertrag;Ziffern für korrekte Rundung einsetzen;groß;
10;1;I;K4;Zahlengerade;GZ:zahlengerade;Zahl markieren;klein;
11;1;II;K2;Würfelnetz;L:KB:Würfelnetz – Lage von Markierungen bestimmen;Zahl im Würfelnetz eintragen;klein;
12;1;I;K4;Zeichnen;GB:winkelarten;Winkel zeichnen;Grad;
13;1;II;K3;Zeit;GR:zeit;anderthalbfache Laufzeit;min, s;
14;1;II;K3;Verhältnis;PROP:dreisatz;Pulvermenge für kleinere Menge;ml;
15;1;II;K2;Körper;KB:verstehen;Körper zu Kanten- und Eckenzahl;klein;
16;1;II;K1;Ankreuzen;FL:verstehen;richtige Rechenwege für Schnurumfang;cm;
17;1;II;K1;Ankreuzen;FL:verstehen;Umfang Quadrat vs. Teilfläche;–;
18;1;I;K4;Zeichnen;FL:rechteck;Figur zum Rechteck ergänzen;–;
19;1;III;K1;Begründen;RG:sach;Familienkarte nicht günstiger begründen;Euro;
""")
JT6(2020, ISB_RS+"2020/2020_jt_mathe_6_loesung.pdf", """
1a;1;I;K5;Rechnen;RG:schriftlich_geteilt;Division;mehrstellig;
1b;1;I;K5;Rechnen;POT:berechnen;Quadrat und Verknüpfung;klein;
2a;1;I;K5;Rechnen;GZ:addieren;Addition mit negativen Zahlen;klein;
2b;1;I;K5;Rechnen;RG:mal_ganz;Produkt zweier negativer Zahlen;klein;
3;1;II;K4;Zeichnen;L:KB:Schrägbild eines Quaders zeichnen (Kl. 5);Quader-Schrägbild vervollständigen;–;
4;1;II;K3;Ankreuzen;FL:einheiten;Fläche von etwa einem Hektar;–;Größenvorstellung
5;1;II;K2;Klammern setzen;RG:klammern;Klammern setzen;klein;
6;1;II;K3;Sachaufgabe;RG:sach;Getränke mit Restbetrag;Euro;
7;1;II;K1;Fehler finden;GB:koordinaten;Fehler beim Eintragen beschreiben;–;
8;1;I;K4;Ablesen;DD:tabelle_auswerten;Wert aus Grafik;–;
9;1;I;K4;Ablesen;NAT:strahl_ablesen;Wert auf Skala;–;
10;1;I;K6;Ankreuzen;GB:lagebeziehungen;Symbolschreibweise;–;
11;1;II;K3;Umfang;FL:sachaufgaben;Zaunlänge um Becken;m;
12;1;I;K6;Ankreuzen;RG:termaufbau;Term zu Text;–;
13;1;II;K3;Proportional;PROP:dreisatz;Länge vieler Wagen;m;
14;1;II;K1;Ankreuzen;NAT:runden_regel;Zahl, die auf Wert rundet;groß;
15;1;II;K1;Fehler finden;GR:laenge;Fehler bei Längenumrechnung;–;
16;1;II;K2;Offen;TB:quersumme;vierstellige Zahl ohne doppelte Ziffern teilbar;vierstellig;offen
17;1;III;K1;Begründen;WI:ergaenzen;Leiterwinkel berechnen und beurteilen;Grad;
18;1;II;K5;Ankreuzen;TB:primzahl;Anzahl Primzahlen im Bereich;zweistellig;
19;1;I;K4;Zeichnen;GB:lagebeziehungen;kürzeste Verbindung Punkt–Gerade;–;
""")
JT6(2019, ISB_RS+"2019/2019_jt_mathe_6_angabe.pdf", """
1a;1;I;K5;Rechnen;RG:punkt_strich;Term mit Division und Subtraktion;klein;
1b;1;I;K5;Rechnen;RG:schriftlich_geteilt;Division durch Zweistellige;groß;
2a;1;I;K5;Rechnen;RG:mal_ganz;Produkt mit negativen Faktoren;klein;
2b;1;I;K5;Rechnen;GZ:subtrahieren;Differenz mit negativen Zahlen;klein;
3;1;II;K4;Zeichnen;GR:kommaschreibweise;Füllhöhe auf Messbecher einzeichnen;ml;
4;1;I;K5;Teiler;TB:teiler;mehrere Teiler aufzählen;zweistellig;
5;1;II;K3;Proportional;PROP:dreisatz;Gewicht größerer Stückzahl;g;
6;1;I;K4;Zahlenstrahl;NAT:strahl_ablesen;markierte Stelle ablesen;groß;
7;1;II;K5;Ergänzen;GE:zwei_schritte;fehlende Zahl in Klammerterm;klein;
8;1;II;K4;Zeichnen;FL:verstehen;Rechteck gleicher Fläche;cm²;
9;1;I;K1;Ankreuzen;GB:lagebeziehungen;Aussagen zu Senkrechten;–;
10;1;II;K3;Vergleich;GR:schaetzen;wie oft passt Kürzeres in Längeres;–;
11;1;III;K1;Begründen;DD:irrefuehrend;fehlenden Balken im Diagramm erklären;–;
12;1;II;K3;Verdoppeln;POT:sach;Anzahl nach mehreren Verdopplungen;groß;
13;1;I;K4;Messen;GB:winkelarten;Winkel messen;Grad;
14;1;III;K1;Fehlende Angabe;L:RG:Sachaufgabe – fehlende Angabe erkennen;fehlende Angabe nennen;Euro;
15;1;II;K4;Würfelnetz;L:KB:Würfelnetz – Lage von Markierungen bestimmen;Pfeil im Würfelnetz;–;
16;1;II;K5;Zählen;KOMB:zaehlprinzip;maximale Ziffernkombinationen;groß;
17;1;II;K3;Schätzen;GR:schaetzen;Umfang über Vergleichsobjekt;m;
18;1;III;K1;Fehler finden;GR:zeit;Fehler beim Umrechnen Stunden–Minuten;–;
19;1;II;K1;Ankreuzen;NAT:runden_regel;korrektes Vorgehen beim Runden;fünfstellig;
""")
JT6(2018, ISB_RS+"2018/2018_jt_mathe_6_angabe.pdf", """
1a;1;I;K5;Rechnen;RG:mal_ganz;Produkt mit Vorzeichen;klein;Punkte 1a+1b zusammen 2
1b;1;I;K5;Rechnen;GZ:ketten;Klammerrechnung mit negativen Zahlen;klein;
2a;1;I;K5;Rechnen;RG:schriftlich;Produkt dreier Zahlen;klein;
2b;1;I;K5;Rechnen;RG:schriftlich_geteilt;Division;dreistellig;
3;1;II;K2;Mitte;GZ:zahlengerade;Zahl genau zwischen zwei Zahlen;klein;
4;1;I;K4;Zeichnen;GB:winkelarten;Winkel zeichnen;Grad;
5;1;II;K4;Zeichnen;FL:rechteck;Rechteck mit vorgegebenem Umfang;cm;
6;1;II;K1;Ankreuzen;KB:verstehen;Körper zu Ecken- und Kantenzahl;klein;
7;1;II;K5;ggT;L:TB:ggT zweier Zahlen bestimmen (in der App erst Kl. 6);größter gemeinsamer Teiler;zweistellig;
8;1;II;K5;Fläche;FL:zerlegen;Fläche aus zwei überlappenden Quadraten;cm²;
9;1;II;K5;Winkel;WI:kreuzung;Winkel an Geradenkreuzung;Grad;
10;1;III;K4;Netz;L:KB:Netz eines Quaders zeichnen (Kl. 5);Netzflächen passend einfärben;–;
11;1;II;K2;Muster;L:RG:Zahlenfolgen – Bildungsregel erkennen und fortsetzen;Folgeglieder ergänzen;klein;
12;1;II;K6;Beschreiben;GR:schaetzen;Schätzmethode für eine Länge;–;
13;1;I;K5;Ankreuzen;TB:primzahl;Primzahlen ankreuzen;einstellig;
14;1;II;K2;Klammern setzen;RG:klammern;Klammern setzen, damit Rechnung stimmt;dreistellig;
15;1;I;K5;Umrechnen;GR:kommaschreibweise;Länge aus zwei Einheiten in cm;klein;
16;1;I;K4;Zeichnen;OL:parallelen;Parallele im Abstand;cm;
17;1;II;K3;Dreisatz;PROP:sach;Mindestzeit für mehr Personen;min;
18;1;II;K5;Zählen;KOMB:reihenfolgen;Reihenfolgen dreier Töne;klein;
19;1;II;K1;Ankreuzen;DD:tabelle_auswerten;Aussagen zum Balkendiagramm;–;
""")
JT6(2017, ISB_RS+"2017/2017_jgt_mathematik_6_angabe.pdf", """
1;1;II;K2;Zahl bilden;NAT:stellenwert;kleinste Zahl ohne Ziffernwiederholung;mehrstellig;
2;1;III;K2;Runden rückwärts;NAT:runden_regel;kleinste Zahl mit gegebener Rundung;groß;
3;1;II;K1;Ankreuzen;RG:verteilen;richtige Rechenwege zu einem Produkt;klein;
4;1;II;K6;Beschreiben;GR:schaetzen;Überschlagsvorgehen beschreiben;groß;
5a;1;I;K5;Rechnen;RG:klammern;Term berechnen;klein;
5b;1;I;K5;Rechnen;RG:klammern;Term berechnen;klein;
6;1;II;K3;Sachaufgabe;NAT:vergleichen;letzte fortlaufende Startnummern;dreistellig;
7;1;II;K3;Sachaufgabe;VOL:liter;Gläser aus Flüssigkeitsmenge;Liter;Kl.-6-Stoff Gym
8;1;II;K1;Begründen;PROP:einheit;Strecke pro Minute prüfen;km;
9;1;II;K3;Maßstab;GR:massstab;passenden Maßstab wählen;–;
10;1;II;K2;Offen;VOL:quader;Kantenlängen zu Volumen;cm;offen, Kl.-6-Stoff
11;1;II;K3;Ankreuzen;FL:rechteck;Fläche eines Drahtquadrats;cm;
12;1;I;K4;Zuordnen;KB:quader;Körper benennen;–;
13;1;I;K4;Zeichnen;GB:vierecke;Quadrat ergänzen;–;
14;1;I;K4;Zeichnen;KON:symmetrie;Symmetrieachsen einzeichnen;–;Kl.-7-Stoff Gym
15;1;II;K4;Zeichnen;FL:verstehen;Rechteck gleicher Fläche;cm²;
16;1;II;K5;Zählen;KOMB:zaehlprinzip;Zusammenstellungen zählen;klein;
17;1;III;K1;Begründen;KB:oberflaeche;Oberflächenänderung nach Herausschneiden;–;
18;1;II;K2;Teilbarkeit;TB:neunerregel;Ziffern für Teilbarkeit durch 9;klein;
19a;1;I;K4;Diagramm;DD:saeulendiagramm;Säulen ergänzen;–;
19b;1;I;K4;Tabelle;DD:tabelle_auswerten;Wert in Tabelle ergänzen;–;
""")
JT6(2016, ISB_RS+"2016/2016_07_07_jgst_2016_klasse_6_angabe.pdf", """
1;1;I;K5;Rechnen;RG:punkt_strich;Term mit Mal und Geteilt;mehrstellig;
2;1;I;K5;Rechnen;RG:schriftlich_geteilt;schriftliche Division;groß;
3;1;II;K5;Zählen;KOMB:reihenfolgen;Stapelreihenfolgen;klein;
4;1;II;K3;Wachstum;POT:sach;Punktestand bei Vervielfachung;groß;
5;1;II;K1;Ankreuzen;RG:vorteil;wertgleiche Rechenausdrücke;klein;
6;1;II;K3;Sachaufgabe;GR:masse;Gewichte vergleichen, Differenz;t, kg;
7;1;II;K3;Sachaufgabe;GR:rechnen;wie oft passt kleine Menge in große;Liter;
8;1;I;K6;Ankreuzen;RG:termaufbau;Text in Term übersetzen;dreistellig;
9;1;I;K3;Dreisatz;PROP:dreisatz;Rezept umrechnen;g;
10;1;II;K2;Muster;L:RG:Zahlenfolgen – Bildungsregel erkennen und fortsetzen;Folgeglieder ergänzen;klein;
11;1;II;K2;Offen;RG:termaufbau;Zahl für ungerades Termergebnis;klein;offen
12;1;II;K3;Maßstab;GR:massstab;Maßstab für Zimmerzeichnung;–;
13;1;II;K4;Zeichnen;KON:symmetrie;Figur mit genau zwei Achsen;–;Kl.-7-Stoff Gym
14;1;II;K2;Zählen;KB:zusammengesetzt;Würfel eines Körpers zählen;klein;
15;1;III;K4;Ankreuzen;L:KB:Würfelnetz – Lage von Markierungen bestimmen;Augenzahl nach Kippen;–;
16;1;III;K5;Rechnen;VOL:rueckwaerts;Kantenlänge aus Würfelvolumen, Quaderlänge;cm;Kl.-6-Stoff Gym
17;1;II;K5;Fläche;FL:zerlegen;Rechteck aus Teilrechtecken;cm²;
18;1;III;K1;Begründen;TB:quersumme;alle Kartenzahlen teilbar begründen;dreistellig;
19;1;I;K4;Ankreuzen;KON:achsenspiegelung;Spiegelbild erkennen;–;Kl.-7-Stoff Gym
20;1;II;K4;Netz;L:KB:Würfelnetz – Lage von Markierungen bestimmen;passendes Würfelnetz;–;
21;1;I;K4;Diagramm;DD:saeulendiagramm;Säule aus Tabelle ergänzen;gerundet;
""")
JT6(2014, ISB_RS+"2014/2014_07_17_jahrgangsstufe_6_angabe_geschwaerzt.pdf", """
1;1;I;K5;Potenz;POT:berechnen;Potenz berechnen;klein;
2;1;II;K4;Diagramm;DD:saeulendiagramm;Namen den Balken zuordnen;klein;
3;1;I;K5;Zählen;KOMB:zaehlprinzip;Menüs zählen;klein;
4;1;I;K4;Zeichnen;GB:lagebeziehungen;Geraden nach Lage zeichnen;–;
5;1;II;K1;Ankreuzen;FL:rechteck;Rechteckangaben prüfen;gemischt;Einheiten
6;1;II;K2;Muster;L:RG:Zahlenfolgen – Bildungsregel erkennen und fortsetzen;Folge fortsetzen;klein;
7;1;II;K3;Schätzen;GR:schaetzen;Größenverhältnis einschätzen;–;
8;1;II;K1;Begründen;POT:vertauschen;Potenzbehauptung prüfen;klein;
9;1;I;K5;Rechnen;GZ:addieren;Zahlenmauer;klein;
10;1;I;K3;Zeit;GR:zeit;Zeitspanne abziehen;min;
11;1;II;K3;Sachaufgabe;RG:sach;Gesprächsdauer aus Tarif;Euro;
12;1;II;K1;Fehler finden;RG:termaufbau;Fehlertyp zuordnen;–;
13;1;II;K1;Ankreuzen;DD:tabelle_auswerten;Aussagen zur Tabelle;–;
14;1;II;K5;Ungleichung;L:GE:Ungleichungen über N über die zugehörige Gleichung lösen;Lösungsmenge einer Ungleichung;dreistellig;
15;1;II;K4;Muster;L:RG:Zahlenfolgen – Bildungsregel erkennen und fortsetzen;Figurenmuster fortsetzen;–;
16;1;II;K3;Sachaufgabe;GR:zeit;Alter aus Wachstum, Monate in Jahre;cm;
17;1;II;K1;Begründen;DD:tabelle_auswerten;Behauptung zum Diagramm prüfen;–;
18;1;III;K2;Fläche;FL:zerlegen;inneres Quadrat;cm²;
19;1;II;K3;Maßstab;GR:massstab;reale Länge aus Abbildung;–;
20;1;II;K6;Frage formulieren;GE:aufstellen;Frage zu Text und Rechnung;–;umgekehrt
21;1;III;K2;Zählen;KB:zusammengesetzt;Würfel zum Quader ergänzen;klein;
""")
JT6(2012, ISB_RS+"2012/jgstt_2012_klasse_6_end.pdf", """
1;1;I;K4;Diagramm;DD:saeulendiagramm;häufige Werte ablesen;–;
2;1;II;K3;Ankreuzen;KB:quader;passenden Karton wählen;cm;
3;1;II;K5;Ankreuzen;RG:termaufbau;Ausdruck mit abweichendem Wert;klein;
4;1;III;K2;Rechtecke;TB:primzahl;Zahl mit nur einer Rechteckanordnung;zweistellig;Primzahl verdeckt
5;1;II;K2;Muster;L:RG:Zahlenfolgen – Bildungsregel erkennen und fortsetzen;Folge ergänzen;klein;
6;1;II;K5;Aufzählen;TB:quersumme;Zahlen mit gegebener Quersumme;zweistellig;
7;1;III;K2;Optimieren;NAT:stellenwert;Karten für maximale Differenz;mehrstellig;
8;1;II;K4;Raum;KB:zusammengesetzt;Flächenzahl nach Herausschneiden;–;
9;1;I;K5;Zählen;KOMB:zaehlprinzip;Menükombinationen;klein;
10;1;II;K5;Maßstab;GR:massstab;Plangröße eines Platzes;m;
11;1;II;K5;Ungleichung;L:GE:Ungleichungen über N über die zugehörige Gleichung lösen;gerade Lösungen einer Ungleichung;klein;
12;1;II;K1;Ankreuzen;RG:geteilt_ganz;Quotient bei verdoppeltem Divisor;–;
13;1;I;K6;Notieren;GB:lagebeziehungen;Parallelität notieren;–;
14;1;II;K3;Sachaufgabe;RG:sach;Trainingszeit aus Kalorien;min;
15;1;II;K3;Sachaufgabe;GR:rechnen;Cent in Euro, Scheine;Euro;
16;1;I;K6;Benennen;KB:verstehen;Körper einer Figur benennen;–;
17;1;III;K2;Zahl bilden;NAT:stellenwert;Zahl nahe Zielwert bilden;mehrstellig;
18;1;II;K3;Umfang;KB:sachaufgaben;Schnurlänge um Päckchen;cm;
19;1;II;K3;Zeit;GR:zeit;späteste Abfahrtszeit;min;
20;1;III;K1;Begründen;TB:endziffer;Teilbarkeitsaussagen prüfen;–;
21;1;I;K4;Ankreuzen;KON:symmetrie;Flaggen mit genau einer Achse;–;Kl.-7-Stoff Gym
""")
JT6(2010, ISB_RS+"2010/end_6test2010_ohne-foto.pdf", """
1;1;II;K3;Anteil;BR:bruchteil_von;Bruchteil einer Menge;klein;Brüche = Kl. 6 Gym
2.1;1;I;K5;Rechnen;GZ:schriftlich_plus_minus;fehlende Operation, Subtraktion;mehrstellig;
2.2;1;I;K5;Rechnen;GZ:schriftlich_plus_minus;Addition großer Zahlen;groß;
3;1;III;K3;Proportional;PROP:sach;Sprungweite übertragen;m;
4;1;II;K4;Zählen;KB:zusammengesetzt;Würfelanzahl aus Foto;klein;
5;1;I;K5;Zeit;GR:zeit;Zeitdifferenz in h, min, s;h;
6;1;II;K3;Quader;KB:quader;Höhe aus Kantenlänge;cm;
7;1;II;K3;Sachaufgabe;RG:sach;Gesamtanzahl verschachtelt;klein;
8;1;III;K2;Würfel;L:KB:Würfelnetz – Lage von Markierungen bestimmen;größte Augensumme;klein;
9;1;III;K1;Begründen;TB:vielfache;Nummer in Periodenreihe prüfen;groß;
10;1;II;K5;Volumen;VOL:einheitswuerfel;kleine Quader in Würfel;klein;Kl.-6-Stoff Gym
11;1;II;K5;Aufzählen;KOMB:systematisch;Gewinnsummen auflisten;klein;
12;1;II;K5;Vervielfachen;POT:sach;mehrfaches Vervierfachen;groß;
13;1;I;K5;Fläche;FL:einheitsquadrate;Fläche aus Einheitsquadraten;klein;
14;1;III;K2;Knobel;TB:quersumme;kleinste Zahl mit Quersumme;vierstellig;
15;1;II;K3;Sachaufgabe;RG:sach;Wochenbedarf, Informationen auswählen;klein;
16;1;II;K5;Vergleichen;POT:schreibweise;größte Zahl (Potenzen);groß;
17;1;II;K1;Ankreuzen;X:Wahrscheinlichkeit/Chancen (Gym Kl. 8);wahrscheinlicheres Glücksrad;–;
18.1;1;I;K5;Umrechnen;GR:laenge;Längeneinheit umrechnen;–;
18.2;1;I;K5;Umrechnen;VOL:liter;Liter in cm³;–;Kl.-6-Stoff Gym
19;1;II;K4;Puzzle;FL:zerlegen;zwei Teile zum Rechteck;–;
""")
JT6(2009, ISB_RS+"2009/end_6test2009_ohne-foto.pdf", """
1;1;II;K3;Rückwärts;RG:sach;Vorjahreswert aus Veränderung;groß;
2.1;1;I;K4;Diagramm;DD:absolute_haeufigkeit;fehlende Stimmen;klein;
2.2;1;I;K4;Diagramm;DD:saeulendiagramm;Balken einzeichnen;klein;
3;1;I;K5;Gleichung;GE:zwei_schritte;Zahl, die Gleichung erfüllt;dreistellig;
4.1;1;I;K5;Rechnen;RG:klammern;Term mit Klammern;klein;
4.2;1;I;K5;Rechnen;RG:punkt_strich;Rechenausdruck;klein;
5;1;I;K4;Zeichnen;FL:rechteck;Rechteck mit Umfang;cm;
6.1;1;I;K5;Zählen;KOMB:reihenfolgen;Reihenfolgen dreier Personen;klein;
6.2;1;III;K1;Begründen;KOMB:bedingungen;wenige Reihenfolgen unter Bedingung;klein;
7;1;II;K6;Lückentext;GB:vierecke;Bedingung Rechteck→Quadrat;–;
8;1;II;K2;Muster;POT:sach;Anzahl aus Wachstumsmuster;klein;
9;1;I;K4;Zeichnen;KON:symmetrie;Symmetrieachsen eines Wortes;–;Kl.-7-Stoff Gym
10;1;II;K2;Zählen;KB:quader;Kugeln an Ecken und Kanten;klein;
11;1;II;K3;Volumen;VOL:rueckwaerts;Füllhöhe aus Volumen;cm;Kl.-6-Stoff Gym
12;1;I;K4;Zahlenstrahl;NAT:strahl_eintragen;große Zahl eintragen;groß;
13.1;1;I;K5;Umrechnen;GR:kommaschreibweise;in größere Einheit;–;
13.2;1;I;K5;Umrechnen;GR:laenge;in kleinere Einheit;–;
14.1;1;II;K1;Begründen;X:Wahrscheinlichkeit/Chancen (Gym Kl. 8);Würfel mit größter Chance;–;
14.2;1;II;K4;Ankreuzen;L:KB:Würfelnetz – Lage von Markierungen bestimmen;passendes Netz;–;
15;1;III;K3;Schätzen;VOL:verstehen;Volumen eines großen Würfels schätzen;m³;Kl.-6-Stoff
16;1;III;K2;Textaufgabe;GE:aufstellen;zwei Fahrzeugarten aus Gesamt- und Personenzahl;klein;Probieren
""")
JT6(2008, ISB_RS+"2008/end_6test2008.pdf", """
1.1;1;I;K5;Rechnen;RG:klammern;Term mit Klammern;klein;
1.2;1;I;K5;Rechnen;BRR:brueche_plus_minus;Bruchsubtraktion;klein;Brüche = Kl. 6 Gym
2;1;I;K5;Gleichung;GE:zwei_schritte;natürliche Zahl, die Gleichung erfüllt;klein;
3;1;I;K4;Zeichnen;GB:strecken;Strecke zeichnen, Punkt eintragen;cm;
4;1;II;K4;Zeichnen;FL:verstehen;Rechteck gleicher Fläche wie Stern;–;
5;1;II;K4;Zeichnen;FL:verstehen;Quadrat mit gleichem Umfang;cm;
6;1;I;K4;Tabelle;DD:absolute_haeufigkeit;Tabelle ergänzen;klein;
7;1;II;K3;Sachaufgabe;RG:sach;Handyrechnung;Euro;
8;1;III;K1;Begründen;BR:anteil_bestimmen;Großzügigkeit über Anteile vergleichen;–;Brüche
9.1;1;II;K2;Zuordnen;KB:quader;welcher Würfel unten liegt;–;
9.2;1;II;K3;Sachaufgabe;KB:sachaufgaben;maximale Turmhöhe;cm;
10;1;II;K2;Muster;L:RG:Zahlenfolgen – Bildungsregel erkennen und fortsetzen;Zahl in Folge ergänzen;klein;
11;1;III;K3;Schätzen;GR:schaetzen;Autos im Stau schätzen;km;
12.1;1;II;K2;Münzen;GR:rechnen;kleinste Münzanzahl;Euro;
12.2;1;II;K2;Offen;GR:rechnen;Kombination aus fünf Münzen;Euro;offen
13.1;1;I;K5;Zählen;KOMB:systematisch;alle dreistelligen Zahlen aus Karten;–;
13.2;1;II;K5;Zählen;KOMB:bedingungen;gerade zweistellige Zahlen;–;
14;1;II;K1;Beurteilen;X:Wahrscheinlichkeit/Zufall (Gym Kl. 8);Vorhersagbarkeit eines Wurfs;–;
15.1;1;I;K4;Zeichnen;GB:lagebeziehungen;Parallele durch Punkt;–;
15.2;1;I;K4;Zeichnen;GB:lagebeziehungen;Senkrechte durch Punkt;–;
16;1;II;K2;Offen;FL:rechteck;Seiten zu vorgegebener Fläche;cm²;offen
""")
JT6(2007, ISB_RS+"2007/jahrgangsstufe-6-angaben.pdf", """
1.1;1;I;K5;Rechnen;RG:punkt_strich;Term Punkt vor Strich;klein;
1.2;1;I;K5;Rechnen;BRR:brueche_plus_minus;Bruchausdruck;klein;Brüche = Kl. 6 Gym
2;1;I;K5;Gleichung;GE:zwei_schritte;Unbekannte bestimmen;klein;
3;1;II;K3;Textaufgabe;GE:aufstellen;Teilstrecke aus Gesamtlänge und Differenz;m;
4;1;II;K2;Zählen;KOMB:systematisch;Dreiecke in Zeichnung zählen;–;
5.1;1;II;K4;Zeichnen;GB:lagebeziehungen;drei Geraden ohne gemeinsamen Punkt;–;
5.2;1;II;K4;Zeichnen;GB:lagebeziehungen;drei Geraden durch einen Punkt;–;
6;1;I;K4;Tabelle;DD:absolute_haeufigkeit;Tabelle mit Summen ergänzen;klein;
7.1;1;II;K2;Zuordnen;KB:quader;welcher Quader unten liegt;–;
7.2;1;II;K3;Sachaufgabe;KB:sachaufgaben;maximale Turmhöhe;cm;
8;1;II;K3;Sachaufgabe;VOL:liter;Flaschen aus Gesamtmenge;Liter;Brüche
9;1;II;K3;Sachaufgabe;PROP:einheit;Druckdauer;min;
10;2;II;K3;Fläche;FL:zerlegen;Wandfläche ohne Fenster und Tür;m²;
11;1;III;K2;Zaunpfosten;TB:vielfache;Pfosten bei festem Abstand;m;Zaunpfahlproblem
12;1;I;K5;Auswahl;GZ:zahlengerade;Zahl in der Mitte;klein;
13;1;III;K2;Zählen;KOMB:bedingungen;dreistellige Zahlen mit Quersumme;–;
14;1;II;K5;Potenz;POT:schreibweise;fehlende Zahl in Potenzreihe;–;
15;1;II;K3;Umfang;RG:sach;Radumdrehungen aus Strecke und Umfang;m;
16;1;II;K4;Zeichnen;L:KB:Netz eines Quaders zeichnen (Kl. 5);Würfelnetz zeichnen;cm;
17;1;III;K2;Sachaufgabe;KB:sachaufgaben;Schachtellänge aus Karton;cm;
""")
JT6(2006, ISB_RS+"2006/mt06_06_a.pdf", """
1.1;1;I;K5;Rechnen;RG:punkt_strich;gemischter Term;klein;
1.2;1;I;K5;Rechnen;GZ:schriftlich_plus_minus;Addition und Subtraktion;mehrstellig;
2;1;I;K5;Gleichung;GE:zwei_schritte;Unbekannte bestimmen;klein;
3;1;II;K2;Lücken;RG:schriftlich_geteilt;fehlende Ziffern in Division;mehrstellig;
4;1;II;K2;Zählen;KOMB:systematisch;Dreiecke zählen;–;
5;2;II;K4;Koordinaten;GB:koordinaten;Rechteckeckpunkte im Gitter;klein;
6;2;II;K3;Fläche;FL:zerlegen;Wandfläche ohne Fenster;m²;
7.1;1;I;K3;Zeit;GR:zeit;Ankunftszeit;h;
7.2;1;I;K3;Zeit;GR:zeit;Fahrtdauer;h;
8;1;II;K5;Umfang;FL:rechteck;Umfang zusammengesetzter Figur;m;
9.1;1;I;K4;Zeichnen;GB:lagebeziehungen;Parallele;–;
9.2;1;I;K4;Zeichnen;GB:lagebeziehungen;Senkrechte;–;
10.1;1;II;K5;Würfel;VOL:rueckwaerts;Kantenlänge aus Volumen;cm;Kl.-6-Stoff
10.2;1;I;K5;Würfel;KB:oberflaeche;Würfeloberfläche;cm²;
11;1;II;K3;Maßstab;GR:massstab;reale Entfernung;km;
12.1;1;II;K2;Zählen;NAT:stellenwert;Anzahl zweistelliger Zahlen;–;
12.2;1;II;K2;Zahl bilden;NAT:stellenwert;kleinste vierstellige Zahl mit verschiedenen Ziffern;–;
13;1;II;K4;Ankreuzen;KB:verstehen;Ansicht eines gedrehten Körpers;–;
14;1;III;K1;Begründen;FL:verstehen;Fläche bei verdoppelten Seiten;–;
""")
JT6(2005, ISB_RS+"2005/mt05_6_a.pdf", """
1.1;1;I;K5;Rechnen;GZ:schriftlich_plus_minus;Additionen und Subtraktionen;mehrstellig;
1.2;1;I;K5;Rechnen;RG:schriftlich_geteilt;Division durch Zweistellige;groß;
2.1;1;I;K5;Bruch;BRR:brueche_mal;Bruch mal ganze Zahl;klein;Brüche = Kl. 6 Gym
2.2;1;I;K5;Bruch;BRR:brueche_plus_minus;Brüche subtrahieren;klein;Brüche = Kl. 6 Gym
3;1;II;K2;Klammern setzen;RG:klammern;Klammern setzen;klein;
4;1;I;K5;Gleichung;GE:zwei_schritte;Unbekannte bestimmen;klein;
5;2;II;K2;Teilbarkeit;TB:quersumme;Ziffern für Teilbarkeit durch 3, alle Möglichkeiten;neunstellig;
6;1;II;K3;Sachaufgabe;GR:rechnen;Straßenbreite aus Streifen;m;
7;1;I;K3;Dreisatz;PROP:dreisatz;Zutat für andere Personenzahl;g;
8.1;1;I;K3;Sachaufgabe;RG:sach;Restbetrag;Euro;
8.2;1;I;K3;Sachaufgabe;RG:sach;Anteil pro Person;Euro;
9;1;II;K3;Sachaufgabe;TB:teiler;Stühle neu verteilen;zweistellig;
10;2;II;K1;Ankreuzen;FL:verstehen;Figuren mit gleichem Umfang;cm;
11;1;II;K3;Umfang;FL:rechteck;andere Seite aus Zaunlänge;m;
12;2;II;K5;Fläche;FL:zerlegen;zusammengesetzte Figur;cm²;
13.1;1;II;K5;Würfel;VOL:rueckwaerts;Kantenlänge aus Volumen;cm;Kl.-6-Stoff
13.2;1;I;K5;Würfel;KB:oberflaeche;Würfeloberfläche;cm²;
14;1;II;K4;Würfel;L:KB:Würfelnetz – Lage von Markierungen bestimmen;Augenzahlen gegenüber eintragen;–;
""")

MS6(2012, ZFB+"11980/2012_bma_6_aufgaben.pdf", """
1;1;I;K5;Ergänzen;NAT:stellenwert;Summand zur runden Million;groß;
2;1;I;K5;Zählen;FL:einheitsquadrate;Quadrate auf Millimeterpapier;–;
3a;1;I;K4;Diagramm;DD:saeulendiagramm;Gesamtzahl ablesen;klein;
3b;1;II;K1;Begründen;DD:tabelle_auswerten;meiste Stimmen begründen;klein;
4;1;II;K2;Ordnen;NAT:vergleichen;Personen nach Größe ordnen;–;
5;1;I;K5;Rechnen;GZ:schriftlich_plus_minus;schriftlich addieren;vierstellig;
6;1;II;K3;Vergleichen;PROP:einheit;günstigeres Angebot;Euro;
7;1;III;K2;Rätsel;RG:kopfrechnen;Rechenquadrat füllen;klein;
8;1;II;K4;Fehler finden;L:KB:Schrägbild eines Quaders zeichnen (Kl. 5);falsch benannter Eckpunkt im Schrägbild;–;
9;1;I;K4;Zeichnen;GB:vierecke;Quadrat ergänzen;–;
10;1;II;K3;Maßstab;GR:massstab;Entfernung auf Karte;km;
11;1;I;K4;Karte;GB:koordinaten;Gitterfeld bestimmen;–;
12;1;I;K3;Auswahl;FL:einheiten;passende Flächenangabe;–;
13a;1;I;K4;Skizze;FL:rechteck;Rechteckskizze beschriften;cm;
13b;1;I;K5;Umfang;FL:rechteck;Rahmenlänge;cm;
14;1;I;K5;Ankreuzen;RG:punkt_strich;Term mit Rechenvorrang;klein;
15;1;II;K3;Sachaufgabe;GE:zwei_schritte;Kistenpreis aus Gesamtbetrag;Euro;
16;1;II;K6;Ankreuzen;L:RG:Sachaufgabe – fehlende Angabe erkennen;beantwortbare Frage wählen;–;
17a;1;I;K6;Bruch;BR:anteil_bestimmen;Bruch als Pizzateile;–;Brüche = Kl. 6 Gym
17b;1;I;K6;Bruch;BR:bruchteil_von;Bruch als Verteilung;–;Brüche
18;1;II;K4;Bruch;BR:bruchteil_von;Bruchteil im Messbecher;–;Brüche
19;1;II;K5;Zählen;KOMB:systematisch;weitere Ziffernfolgen;–;offen
20;1;III;K2;Planen;FL:zerlegen;Poster auf Pinnwand anordnen;–;
21;1;II;K1;Fehler finden;GR:zeit;Fehler im Zeitplan;–;
""")
MS6(2013, ZFB+"14359/2013_jgsta_mathematik_ms6_weiterarbeit.pdf", """
1;1;I;K5;Nachbarzahlen;NAT:vergleichen;Vorgänger und Nachfolger;groß;
2;1;I;K1;Ankreuzen;NAT:runden_regel;korrekte Rundungen;groß;
3;1;II;K3;Zeitspanne;GR:zeit;Lebensdauer in Jahren;Jahre;
4;1;I;K4;Zeitleiste;DD:tabelle_auswerten;Jahreszahl ablesen;–;
5;1;I;K5;Rechnen;RG:schriftlich;Produktkette mit Null;klein;
6a;1;II;K5;Lücken;RG:schriftlich;fehlende Ziffern in Multiplikation;mehrstellig;
6b;1;I;K5;Rechnen;RG:schriftlich_geteilt;Division mit Rest;mehrstellig;
7;1;I;K6;Zuordnen;RG:termaufbau;Fachbegriffe zu Rechenzeichen;–;
8;1;II;K4;Ansichten;L:KB:Ansichten von Körpern (in der App erst Kl. 8);Ansichten einer Körperanordnung;–;
9;1;II;K4;Zeichnen;L:KB:Schrägbild eines Quaders zeichnen (Kl. 5);Schrägbild vervollständigen;–;
10;1;I;K4;Koordinaten;GB:koordinaten;Punkte eintragen, Rechteck ergänzen;klein;
11;1;II;K4;Spiegeln;KON:achsenspiegelung;Figur symmetrisch ergänzen;–;Kl.-7-Stoff Gym
12;1;I;K4;Messen;FL:rechteck;Seiten messen, Umfang;cm;
13;1;III;K2;Offen;FL:verstehen;Zaunelemente bei doppelter Fläche;–;
14;1;III;K2;Zerlegen;FL:zerlegen;Mindestzahl an Schnitten;–;
15;1;II;K2;Klammern setzen;RG:klammern;Klammern setzen;klein;
16;1;I;K5;Gleichung;GE:zwei_schritte;Gleichung lösen;klein;
17a;1;II;K3;Preise;GE:aufstellen;Einzelpreis aus Summe und Differenz;Euro;
17b;1;II;K3;Preise;GE:aufstellen;zweiter Einzelpreis;Euro;
18;1;II;K3;Größen;GR:kommaschreibweise;Restmenge in Flasche;Liter;
19;1;I;K5;Geld;GR:rechnen;Gesamtpreis;Euro;
20;1;II;K2;Wochentag;GR:zeit;Wochentag eines Datums;–;
21;1;II;K1;Ankreuzen;X:Wahrscheinlichkeit/Chancen (Gym Kl. 8);größte Gewinnchance;–;
22;1;II;K3;Tabelle;RG:sach;günstigster Eintritt;Euro;
""", zeit=None)
MS6(2014, ZFB+"15841/2014_jgsta6_mathematik_ms_weiterarbeit.pdf", """
1;1;II;K2;Runden;NAT:runden_uebertrag;Ziffern für gerundete Zahl;groß;
2;1;I;K5;Ordnen;NAT:vergleichen;Städte nach Einwohnern ordnen;groß;
3;1;I;K4;Schaubild;DD:tabelle_auswerten;Einwohner aus Symbolbild;–;
4;1;I;K4;Diagramm;DD:saeulendiagramm;Balken ergänzen;–;
5a;1;I;K5;Rechnen;GZ:schriftlich_plus_minus;schriftlich subtrahieren;groß;
5b;1;I;K5;Rechnen;RG:schriftlich;schriftlich multiplizieren;groß;
6;1;III;K2;Kreativ;RG:termaufbau;Aufgaben mit Zielwert finden;–;offen
7;1;II;K4;Auswählen;KB:zusammengesetzt;Würfelgebäude zu Quader kombinieren;–;
8;1;II;K4;Muster;L:RG:Zahlenfolgen – Bildungsregel erkennen und fortsetzen;Figur im Muster ergänzen;–;
9;1;II;K4;Spiegeln;KON:achsenspiegelung;Uhrzeit im Spiegel;–;Kl.-7-Stoff Gym
10a;1;I;K4;Koordinaten;GB:koordinaten;Koordinaten ablesen;klein;
10b;1;I;K4;Messen;GB:strecken;Abstand zweier Punkte;cm;
11;1;II;K3;Maßstab;GR:massstab;Laufstrecke aus Karte;km;
12;1;II;K1;Ankreuzen;FL:verstehen;Verdopplung der Quadratseiten;–;
13;1;II;K4;Ankreuzen;FL:einheitsquadrate;flächengleiche Figuren;–;
14;1;II;K2;Waage;GE:waage;fehlende Sterne für Gleichgewicht;–;
15;1;II;K3;Sachaufgabe;RG:sach;Preisanteil;Euro;
16;1;I;K5;Gleichung;GE:zwei_schritte;Platzhalter berechnen;klein;
17;1;II;K3;Runden;GR:rechnen;Rundenzahl für eine Strecke;m;
18;1;I;K4;Bruch;BR:anteil_bestimmen;Bruchteil einfärben;–;Brüche = Kl. 6 Gym
19;1;II;K1;Begründen;BR:verstehen;falsche Bruchteilung begründen;–;Brüche
20;1;II;K4;Tabelle;DD:tabelle_auswerten;Anzahl aus Tabelle;–;
21;1;II;K5;Paarungen;KOMB:systematisch;fehlende Turnierpaarungen;–;
22;1;II;K3;Füllzeit;PROP:sach;Becken bei Zufluss;Liter;
""", zeit=None)
MS6(2015, ZFB+"16920/2015_jagsta6_mathematik_loesungen_weiterarbeit.pdf", """
1;1;I;K5;Tabelle;DD:absolute_haeufigkeit;fehlende Anzahl in Tabelle;klein;
2;1;I;K4;Ablesen;NAT:strahl_ablesen;Zeigerwert ablesen;–;
3;1;II;K6;Beschreiben;GR:schaetzen;große Menge schätzen;–;
4;1;II;K1;Fehler finden;RG:schriftlich;Fehler in Multiplikation;–;
5;1;I;K5;Teilbarkeit;TB:quersumme;durch 3 teilbare Zahlen markieren;–;
6;1;II;K3;Münzreihe;GR:rechnen;Länge einer Münzreihe;cm;
7;1;II;K2;Würfel;VOL:einheitswuerfel;Würfel bei halber Höhe;klein;Kl.-6-Stoff Gym
8;1;I;K4;Netze;L:KB:Netz eines Quaders zeichnen (Kl. 5);Netze Körpern zuordnen;–;
9;1;I;K4;Zeichnen;FL:rechteck;Rechteck vervollständigen;–;
10a;1;I;K4;Koordinaten;GB:koordinaten;Punkt eintragen und verbinden;klein;
10b;1;I;K4;Koordinaten;GB:koordinaten;Koordinaten ablesen;klein;
11;1;II;K4;Symmetrie;KON:symmetrie;Figur symmetrisch ergänzen;–;Kl.-7-Stoff Gym
12a;1;I;K5;Vergleichen;GR:laenge;größte Länge;gemischt;
12b;1;II;K5;Vergleichen;FL:einheiten;größte Fläche;gemischt;
13;1;II;K3;Schätzen;FL:einheitsquadrate;ungefähre Fläche;–;
14;1;I;K5;Rechnen;RG:klammern;zwei Terme;klein;
15;1;I;K6;Fachbegriffe;RG:termaufbau;Fachbegriffe einsetzen;–;
16;1;II;K2;Unbekannte;GE:waage;Gewicht einer Ladung;kg;
17;1;II;K4;Bruch;BR:anteil_bestimmen;Läufer an Bruchteil;–;Brüche = Kl. 6 Gym
18;1;II;K5;Bruch;BR:bruchteil_von;Anzahl aus Bruchteil;–;Brüche
19;1;I;K5;Zuordnen;GR:masse;gleichwertige Massen;–;
20;1;III;K1;Fehlende Angabe;L:RG:Sachaufgabe – fehlende Angabe erkennen;fehlende Angabe benennen;–;
21;1;III;K2;Termin;TB:vielfache;nächster gemeinsamer Termin;Tage;kgV-Idee
22;1;II;K3;Eintritt;RG:sach;Mindestbetrag aus Preisliste;Euro;
""", zeit=None)
MS6(2016, ZFB+"18555/2016_jagsta6_mathematik_loesungen_weiterarbeit_ms.pdf", """
1;1;III;K2;Zahl bilden;NAT:stellenwert;Zahl nahe Zehntausender aus Karten;fünfstellig;
2;1;I;K1;Ankreuzen;DD:tabelle_auswerten;Aussagen zum Schaubild;–;
3;1;I;K5;Zahlwort;NAT:zahlwort_zu_ziffern;Zahlwort in Ziffern;groß;
4;1;II;K4;Rechenbaum;RG:termaufbau;Term zum Rechenbaum;–;
5;1;III;K2;Zahlenquadrat;RG:kopfrechnen;Zahlenquadrat füllen;klein;
6;1;I;K5;Rechnen;RG:schriftlich_geteilt;schriftliche Division;groß;
7;1;II;K4;Drehen;KB:verstehen;gedrehten Körper erkennen;–;
8;1;I;K4;Zeichnen;GB:lagebeziehungen;kürzeste Verbindung Punkt–Gerade;–;
9;1;I;K4;Zeichnen;FL:rechteck;Rechteck zeichnen;cm;
10a;1;I;K4;Karte;GB:koordinaten;Gitterfeld ablesen;–;
10b;1;I;K4;Karte;GB:koordinaten;Ort im Gitterfeld;–;
11;1;II;K4;Falten;KON:achsenspiegelung;gefaltetes Blatt zuordnen;–;Kl.-7-Stoff Gym
12;1;II;K4;Zeichnen;FL:einheitsquadrate;Figur mit vorgegebener Fläche;–;
13a;1;II;K5;Umfang;FL:zerlegen;Umfang zusammengesetzter Figur;cm;
13b;1;II;K5;Fläche;FL:zerlegen;Fläche zusammengesetzter Figur;cm²;
14;1;II;K3;Gleichung;GE:aufstellen;Zahlenrätsel als Gleichung;klein;
15;1;II;K3;Sachaufgabe;GE:zwei_schritte;Waggongewicht;t;
16;1;II;K2;Klammern;RG:klammern;Klammerpaar einsetzen;klein;
17;1;I;K4;Bruch;BR:anteil_bestimmen;Bruchteil markieren;–;Brüche = Kl. 6 Gym
18a;1;I;K5;Geld;GR:kommaschreibweise;Euro-Cent-Addition;Euro;
18b;1;II;K1;Fehler finden;GR:kommaschreibweise;Fehler beschreiben;Euro;
19;1;II;K4;Höhenprofil;FG:graph_lesen;Höhenprofil zuordnen;–;Graph lesen
20;1;I;K5;Tabelle;GR:zeit;Zeitverschiebung ergänzen;h;
21;1;II;K3;Rezept;PROP:dreisatz;Rezept umrechnen;g;
""", zeit=None)
MS6(2022, ZFB+"28068/2022_jgsta_mathematik_weiterarbeit_final.pdf", """
1;1;I;K5;Stellenwert;NAT:stellenwert;Millionenstelle markieren;groß;
2;1;I;K4;Stellenwerttafel;NAT:stellenwert;Darstellung in Zahl übersetzen;groß;
3;1;I;K4;Zahlenstrahl;NAT:strahl_ablesen;Wert ablesen;groß;
4;1;I;K5;Rechnen;RG:punkt_strich;Punkt vor Strich;klein;
5;1;II;K1;Begründen;RG:umkehraufgabe_mal;verdeckte Ziffer über Umkehraufgabe;klein;
6;1;II;K5;Ankreuzen;RG:kopfrechnen;Kopfrechentrick erkennen;klein;
7;1;I;K5;Offen;GZ:ordnen;kleinere Zahl als negative Zahl;klein;
8;1;I;K5;Lücken;GZ:zahlengerade;Zahlenreihe über Null;klein;
9;1;I;K3;Sachaufgabe;GZ:sach;Temperatur nach Erwärmung;Grad;
10;1;I;K4;Zeichnen;GB:lagebeziehungen;Senkrechte;–;
11;1;I;K4;Zeichnen;GB:strecken;Strecke mit Länge;cm;
12;1;I;K5;Umfang;FL:rechteck;Seiten messen, Umfang;cm;
13;1;II;K4;Ankreuzen;GB:koordinaten;Eckpunkt für Quadrat;klein;
14;1;II;K1;Fehler finden;GB:winkelarten;Messfehler beim Winkel;Grad;
15;1;I;K5;Fläche;FL:rechteck;Kartenfläche;cm²;
16;1;I;K5;Umrechnen;FL:einheiten;Flächeneinheiten;–;
17;1;II;K1;Vergleichen;FL:verstehen;größte Fläche;–;
18;1;II;K4;Zeichnen;FL:einheitsquadrate;Figur mit Fläche;–;
19;1;I;K4;Zeit;GR:zeit;vergangene Zeit an Uhr;min;
20;1;I;K5;Geld;GR:rechnen;Münzen in Euro;Euro;
21;1;II;K3;Dreisatz;PROP:dreisatz;Zutaten umrechnen;g;
22;1;I;K5;Umrechnen;GR:masse;benachbarte Masseeinheiten;–;
23;1;II;K2;Offen;FL:verstehen;anderes Rechteck gleicher Fläche;cm;offen
24;1;II;K1;Ankreuzen;FL:verstehen;Umfang bei verdoppelten Seiten;–;
""", zeit=None)
MS6(2023, ISB_MS+"2023_jahrgangsstufenarbeiten_Mathematik_Weiterarbeit_final.pdf", """
1;1;II;K3;Schätzen;GR:schaetzen;Menge aus Raster schätzen und begründen;groß;
2;1;I;K4;Stellenwert;NAT:stellenwert;Ziffern in Stellenwerttafel;groß;
3;1;I;K5;Zahlwort;NAT:ziffern_zu_zahlwort;Zahlwort erkennen;groß;
4;1;II;K1;Fehler finden;RG:kopfrechnen;falsche Einmaleinszeile;klein;
5;1;II;K2;Runden;NAT:runden_uebertrag;Ziffer für Rundung ergänzen;groß;
6;1;I;K5;Rechnen;RG:punkt_strich;Term mit Rechenreihenfolge;klein;
7;1;I;K4;Zahlenstrahl;GZ:ordnen;Zahlen größer als negative Zahl;klein;
8;1;I;K5;Offen;GZ:ordnen;Zahl zwischen negativ und positiv;klein;
9;1;II;K3;Aufzug;GZ:sach;Stockwerk nach Fahrten;klein;
10;1;II;K3;Umfang;FL:sachaufgaben;Strecke aus Runden und Umfang;m;
11;1;I;K4;Zeichnen;OL:parallelen;Parallele im Abstand;cm;
12;1;II;K1;Begründen;GB:verstehen;Behauptung zu Senkrechten widerlegen;–;
13;1;II;K6;Beschreiben;FL:rechteck;Umfang mit Maßband ermitteln beschreiben;–;
14;1;I;K4;Koordinaten;GB:koordinaten;Punkt ablesen;klein;
15;1;I;K5;Fläche;FL:sachaufgaben;Raumfläche;m²;
16;1;II;K1;Begründen;FL:verstehen;leichter ausmessbare Figur;–;
17;1;II;K4;Zeichnen;FL:rechteck;Rechteck zu einer Multiplikation;–;
18;1;II;K4;Geobrett;FL:einheitsquadrate;Rechteck mit Fläche;–;
19;1;I;K5;Zeit;GR:zeit;Monate in Jahre;–;
20;1;II;K3;Vergleich;GR:laenge;größte Person mit Differenz;cm;
21;1;II;K1;Begründen;GR:schaetzen;Höhenangabe prüfen;m;
22;1;I;K3;Zuordnen;GR:schaetzen;Gewichte zu Tieren;kg;
23;1;II;K4;Daten;DD:relative_haeufigkeit;Glücksrad-Tabelle ergänzen;–;
24;1;II;K3;Gleichung;FL:rechteck;Seite aus Umfang;m;
""", zeit=None)
MS6(2024, "https://isb.bayern.de/fileadmin/user_upload/Mittelschule/Jahrgangsstufenarbeiten/Mathematik/2024_Jahrgangsstufenarbeiten_Mathematik_Weiterarbeit_final.pdf", """
1;1;I;K5;Stellenwert;NAT:stellenwert;Millionenstelle markieren;groß;
2;1;II;K6;Beschreiben;GR:schaetzen;Schätzvorgehen beschreiben;groß;
3;1;I;K5;Nachbarzahlen;NAT:runden_regel;Nachbarzehner bestimmen;groß;
4;1;II;K1;Fehler finden;GZ:schriftlich_plus_minus;Fehler in Subtraktion;mehrstellig;
5;1;I;K5;Umkehraufgabe;GZ:umkehraufgabe;fehlender Summand;mehrstellig;
6;1;I;K3;Geld;GR:rechnen;Geldbetrag berechnen;Euro;
7;1;I;K5;Zahlengerade;GZ:zahlengerade;fehlende Zahlen ergänzen;klein;
8;1;II;K1;Begründen;GZ:verstehen;Aussage zu Zahlen links von Null;–;
9;1;II;K3;Karte;GZ:sach;größter Temperaturunterschied;Grad;
10;1;II;K1;Fehler finden;GB:koordinaten;Fehler beim Punkt einzeichnen;–;
11;1;I;K4;Winkel;GB:winkelarten;stumpfen Winkel markieren;–;
12;1;I;K5;Umrechnen;GR:laenge;Längenangabe umwandeln;–;
13;1;I;K4;Zeichnen;GB:winkelarten;Winkel zeichnen;Grad;
14;1;I;K5;Ankreuzen;FL:rechteck;Umfang eines Rechtecks;cm;
15;1;I;K3;Fläche;FL:sachaufgaben;Zimmerfläche;m²;
16;1;II;K3;Schätzen;FL:einheiten;Fliesenfläche wählen;–;
17;1;II;K4;Zeichnen;FL:verstehen;flächengleiches Rechteck;–;
18;1;II;K1;Begründen;FL:zerlegen;gleich große zusammengesetzte Flächen;–;
19;1;II;K3;Auswahl;GR:schaetzen;passende Abbildung zu Höhen;m;
20;1;II;K3;Zeit;GR:zeit;späteste Abfahrt rückwärts;min;
21;1;I;K3;Rückgeld;GR:rechnen;Rückgeld;Euro;
22;1;I;K3;Gewicht;GR:masse;Gesamtgewicht;kg;
23;1;I;K4;Daten;DD:absolute_haeufigkeit;Häufigkeitstabelle;–;
24;1;II;K3;Gleichung;FL:rechteck;Breite aus Umfang;m;
""", zeit=None)
MS6(2011, ZFB+"9663/2011_loesungen.pdf", """
1;1;III;K2;Zahl bilden;NAT:stellenwert;Zahl nahe Zielzahl aus Karten;vierstellig;
2;1;I;K4;Zahlenstrahl;NAT:strahl_eintragen;Zahlenstrahl zeichnen, markieren;–;
3;1;I;K4;Schaubild;DD:tabelle_auswerten;Aussagen zum Diagramm ergänzen;–;
4;1;I;K5;Runden;NAT:runden_regel;rundbare Zahl;groß;
5;1;II;K3;Schätzen;GR:schaetzen;Länge schätzen, begründen;m;
6;1;I;K6;Zuordnen;RG:termaufbau;Fachbegriffe;–;
7;1;II;K3;Kästen;RG:sach;volle Kästen mit Rest;klein;
8a;1;I;K5;Rechnen;GZ:schriftlich_plus_minus;schriftlich addieren;mehrstellig;
8b;1;I;K5;Rechnen;RG:schriftlich;schriftlich multiplizieren;mehrstellig;
9;1;II;K2;Offen;GB:lagebeziehungen;Punkte auf einer Geraden;–;offen
10;1;I;K4;Senkrecht;GB:lagebeziehungen;senkrechte Strecke angeben;–;
11;1;II;K4;Körper;KB:verstehen;Abdruck, der nicht passt;–;
12;1;II;K4;Drehen;WI:drehungen;Drehfiguren ankreuzen;–;
13;1;II;K4;Maßstab;GR:massstab;Figur verkleinern;–;
14a;1;I;K4;Messen;FL:rechteck;Blatt ausmessen, Umfang;cm;
14b;1;II;K1;Ankreuzen;FL:verstehen;Umfang eines doppelten Blatts;–;
15;1;I;K5;Einheiten;GR:laenge;passende Einheiten;–;
16;1;III;K1;Begründen;RG:punkt_strich;Fehler bei Rechenregel erklären;–;
17;1;II;K3;Gleichung;GE:zwei_schritte;Kinderpreis aus Familienbetrag;Euro;
18;1;I;K4;Bruch;BR:anteil_bestimmen;Bruchteile von Kreisausschnitten;–;Brüche = Kl. 6 Gym
19;1;II;K5;Bruch;BR:bruchteil_von;Anzahl aus Bruchteil;–;Brüche
20;1;II;K1;Ankreuzen;X:Wahrscheinlichkeit/Chancen (Gym Kl. 8);Aussagen zum Ziehen;–;
21;1;III;K3;Preisliste;RG:sach;gebuchte Plätze rekonstruieren;Euro;
22;1;II;K3;Vorsprung;PROP:sach;Vorsprung nach Zeit;m;
""", schulart="Hauptschule", zeit=None)
MS6(2006, ZFB+"5974/2006-test_6_loesungen.pdf", """
1;1;I;K5;Stellenwert;NAT:stellenwert;Stellenwert einer Ziffer;groß;
2;1;I;K5;Stellenwert;NAT:stellenwert;zweite Stellenwertaufgabe;groß;
3;1;I;K5;Vergleichen;NAT:vergleichen;kleinste große Zahl;groß;
4a;1;II;K4;Schaubild;DD:tabelle_auswerten;Schaubild auswerten;–;
4b;1;II;K4;Schaubild;DD:saeulendiagramm;Schaubild ergänzen;–;
5a-d;4;I;K5;Rechnen;RG:schriftlich;vier Rechnungen mit den Grundrechenarten;mehrstellig;
6;1;I;K5;Runden;RG:ueberschlag;Runden und Überschlag;mehrstellig;
7a;1;II;K2;Zerlegen;KB:quader;Schnitte bei Quaderzerlegung;–;
7b;0.5;II;K2;Zählen;KB:zusammengesetzt;Würfel mit einer farbigen Fläche;–;
8;0.5;II;K4;Drehkörper;KB:verstehen;Drehkörper benennen;–;
9a;0.5;I;K4;Messen;GB:strecken;Strecke messen;cm;
9b;0.5;I;K4;Zeichnen;GB:lagebeziehungen;Abstand als Senkrechte;–;
10a;0.5;I;K5;Fläche;FL:rechteck;Flächeninhalt;m²;
10b;0.5;II;K5;Fläche;FL:zerlegen;nicht belegte Teilfläche;m²;
11a;1;I;K3;Gleichung;GE:aufstellen;Sachverhalt als Gleichung;klein;
11b;1;I;K5;Gleichung;GE:zwei_schritte;Gleichung lösen;klein;
12a;1;I;K5;Rechnen;RG:klammern;Klammerregel;klein;
12b;1;I;K5;Rechnen;RG:punkt_strich;Punkt vor Strich;klein;
13a;0.5;II;K4;Bruch;BR:anteil_bestimmen;Anteil als Bruch;–;Brüche = Kl. 6 Gym
13b;0.5;II;K4;Bruch;BR:anteil_bestimmen;zweiter Anteil;–;Brüche
14a;0.5;I;K5;Bruch;BRR:brueche_plus_minus;Bruchrechnung;–;Brüche
14b;0.5;I;K5;Bruch;BRR:brueche_plus_minus;Bruchrechnung;–;Brüche
15;1;II;K3;Rezept;PROP:dreisatz;Rezept umrechnen;g;
16a;1;II;K3;Rechenplan;RG:termaufbau;passenden Rechenplan erkennen;–;
16b;1;II;K3;Preis;RG:sach;Gesamtpreis;Euro;
17;1;II;K3;Karte;GR:rechnen;Streckenlängen addieren;km;
""", schulart="Hauptschule")

# ---- Klasse 5: klassenarbeiten.de (nach Freigabe der Übersicht), weitere Portale/Verlage
KL5b = dict(klasse=5, frei=True, hilfsmittel="nicht angegeben", jahr=None, zeit_min=None)
def KAX(nr, titel, pkt, zeilen, nummer="unbekannt", passung="Gym Kl. 5, Bundesland unbekannt"):
    A(f"G5-K{nr}", quelle=KA+f"{nr}.pdf", titel=titel, herausgeber="klassenarbeiten.de (Schule unbekannt)",
      art="Klassenarbeit/Schulaufgabe", nummer=nummer, punkte_gesamt=pkt, lizenz=LIZ_KA, bundesland="unbekannt",
      passung=passung, zeilen=zeilen, **KL5b)

KAX(1483, "Klassenarbeit Natürliche Zahlen", 38, """
1;5;II;K5;Folge;POT:sach;Folge mit festem Faktor fortsetzen;groß;
2;3;I;K5;Nachbarzahlen;NAT:vergleichen;Nachbarzahlen ergänzen;groß;
3;3;I;K5;Umwandeln;NAT:zahlwort_zu_ziffern;Ziffern, Stellenangaben, Zahlwort;groß;
4;2;III;K2;Runden;NAT:runden_regel;Anzahl Zahlen mit gleicher Rundung;dreistellig;
5;4;I;K5;Runden;NAT:runden_regel;runden und Rundungsfehler angeben;groß;
6;1;III;K2;Knobel;NAT:stellenwert;größte achtstellige Zahl mit Bedingung;achtstellig;
7;10;II;K3;Sachaufgabe;NAT:runden_sinnvoll;Einwohnerzahlen runden, Grenzen, Diagramm erklären;Millionen;10 Punkte
8;6;II;K4;Zahlenstrahl;NAT:strahl_ablesen;ablesen, eintragen, Lösungswege;groß;
9;1;III;K2;Knobel;NAT:stellenwert;kleinste achtstellige Zahl mit Bedingung;achtstellig;
10;3;II;K3;Sachaufgabe;GR:rechnen;Wachstumsdauer mit Einheitenwechsel;cm;Zusatz
""", nummer="September (laut Übersicht; Annahme 1. SA)")
KAX(1047, "Klassenarbeit Geometrie", 33, """
1;?;I;K6;Tabelle;GB:lagebeziehungen;Parallel-/Senkrecht-Symbole eintragen;–;
2;?;I;K4;Konstruieren;GB:lagebeziehungen;Abstand einzeichnen und messen;cm;
3;?;I;K4;Koordinaten;GB:koordinaten;Achsen, Punkte ablesen und eintragen;klein;
4;?;II;K6;Beschreiben;GB:vierecke;Eigenschaften Drachenviereck;–;
5;?;II;K6;Beschreiben;GB:vierecke;Eigenschaften Raute;–;
6;?;II;K4;Zeichnen;L:KB:Netz eines Quaders zeichnen (Kl. 5);Quadernetz;cm;
7;?;II;K1;Ankreuzen;GB:vierecke;Eigenschaften der Vierecke;–;
8;?;II;K4;Zeichnen;L:KB:Schrägbild eines Quaders zeichnen (Kl. 5);Schrägbild, gesamte Kantenlänge;cm;
9;?;I;K4;Zeichnen;GB:vierecke;Parallelogramm zeichnen;cm;
10;?;I;K4;Zeichnen;GB:vierecke;Trapez zeichnen;cm;
""", nummer="November (laut Übersicht)")
KAX(2377, "Klassenarbeit Größen und Maßeinheiten", 37, """
1;?;II;K3;Sachaufgabe;RG:sach;Ratenzahlung berechnen;Euro;Antwortsatz
2;?;I;K5;Rechnen;RG:schriftlich_geteilt;schriftliche Division;groß;
3;?;III;K2;Runden rückwärts;NAT:runden_regel;kleinste/größte Zahl zu einer Rundung;groß;
4;?;I;K5;Umrechnen;GR:kommaschreibweise;Komma durch kleinere Einheit vermeiden;–;
5;?;I;K5;Runden;NAT:runden_regel;auf Tausender und Zehner runden;groß;
6;?;II;K3;Sachaufgabe;GR:laenge;Stücke und Schnitte;m;Zaunpfahlproblem
7;?;II;K3;Textaufgabe;RG:sach;Kosten verteilen;Euro;
8;?;I;K5;Rechnen;GR:rechnen;Größen addieren/subtrahieren;gemischt;
9;?;II;K1;Begründen;GR:verstehen;Plausibilität von Größen prüfen;–;
""", nummer="Oktober (laut Übersicht)")
KAX(1219, "Klassenarbeit Zahlenterme", 35, """
1;6;I;K5;Umrechnen;GR:laenge;Messwerte umrechnen;gemischt;
2;3;I;K5;Lücken;GZ:umkehraufgabe;fehlende Zahl, teils negativ;klein;
3;6;I;K5;Geschickt;RG:vorteil;Summen geschickt umordnen;zweistellig;
4;2;I;K6;Term aufstellen;RG:termaufbau;Wortterm notieren;–;
5;5;II;K6;Term aufstellen;RG:termaufbau;Wortterm mit Klammern notieren;–;
6;5;II;K3;Sachaufgabe;RG:sach;Gesamtstrecke mit Frage, Rechnung, Antwort;m;
7;4;III;K2;Knobel;L:RG:Summe fortlaufender Zahlen geschickt berechnen (Gauß-Idee);Summe einer langen Reihe;dreistellig;
8;2;II;K3;Term;GZ:sach;Ballonhöhen als Term;m;
9;2;I;K5;Rechnen;RG:schriftlich;schriftlich multiplizieren und dividieren;mehrstellig;
""", nummer="November (laut Übersicht)")
KAX(1215, "Klassenarbeit Maßstab", 28, """
1;3;I;K5;Umrechnen;GR:laenge;in nächstgrößere Einheit;–;
2;3;I;K5;Umrechnen;GR:laenge;in nächstkleinere Einheit;–;
3;4;II;K4;Zeichnen;GR:massstab;Rechteck vergrößert zeichnen;cm;
4;4;II;K4;Zeichnen;GR:massstab;Rechteck verkleinert zeichnen;cm;
5;4;II;K5;Tabelle;GR:massstab;Maßstabstabelle ausfüllen;–;
6;4;II;K5;Tabelle;GR:massstab;Maßstabstabelle ausfüllen;–;
7;6;II;K3;Sachaufgabe;GR:rechnen;Wege vergleichen, Gepäck verteilen;km, kg;
""", nummer="November (laut Übersicht)")
KAX(1882, "Klassenarbeit Geometrie (Geraden, Abstände)", None, """
1;?;I;K4;Zeichnen;GB:strecken;Strecke, Gerade, Strahl;–;
2;?;I;K4;Zeichnen;GB:lagebeziehungen;Senkrechte durch Punkte;–;
3;?;I;K6;Notation;GB:lagebeziehungen;Kurzschreibweise;–;
4;?;I;K4;Messen;GB:lagebeziehungen;Abstände messen;cm;
5;?;I;K4;Konstruieren;OL:parallelen;Parallele im Abstand;cm;
6;?;II;K4;Zuordnen;GB:lagebeziehungen;senkrechte und parallele Paare;–;
7;?;II;K4;Ergänzen;GB:vierecke;Quadrat, Rechteck, Parallelogramm ergänzen;–;
8;?;III;K2;Suchen;GB:koordinaten;Quadrate und Rechtecke im Gitter finden;–;
""", nummer="November (laut Übersicht)")
KAX(1167, "Klassenarbeit Zahlensysteme", 30, """
1;2;I;K5;Römisch;NAT:roemisch_schreiben;römisch in dezimal;–;
2;2;I;K5;Vorgänger;NAT:roemisch_schreiben;Vorgänger römisch;–;
3;3;I;K5;Römisch;NAT:roemisch_schreiben;römisch in dezimal;–;
4;4;II;K5;Umrechnen;NAT:roemisch_system;zwischen Systemen umrechnen;–;
5;6;II;K5;Umrechnen;NAT:dualsystem;aus anderen Basen ins Zehnersystem;–;
6;4;II;K5;Umrechnen;NAT:dualsystem;in ein 4er-System umrechnen;–;
7;3;II;K5;Römisch;NAT:roemisch_schreiben;dezimal in römisch;–;Subtraktionsschreibweise
8;6;II;K5;Umrechnen;NAT:dualsystem;in 3er-, 5er-, 7er-System;–;
""", nummer="Oktober (laut Übersicht)")
KAX(1676, "3. Klassenarbeit Geraden und Winkel", 39, """
1;3;I;K6;Benennen;GB:strecken;Linienarten benennen;–;
2a;1;I;K4;Zeichnen;GB:lagebeziehungen;Senkrechte zeichnen;–;
2b;1;I;K4;Zeichnen;OL:parallelen;Parallele im Abstand;cm;
2c;1;I;K4;Messen;GB:lagebeziehungen;Abstand messen;cm;
2d;2;I;K4;Zuordnen;GB:lagebeziehungen;parallele Paare erkennen;–;
3;4;I;K6;Lückentext;GB:winkelarten;Winkelbegriffe ergänzen;–;
4;7;I;K5;Benennen;GB:winkelarten;Winkelarten zu Gradangaben;Grad;
5;6;I;K6;Zuordnen;GB:winkelarten;Winkelbegriffe zuordnen;–;
6;4;I;K4;Messen;GB:winkelarten;zwei Winkel messen;Grad;
7;2;I;K4;Zeichnen;GB:winkelarten;zwei Winkel zeichnen;Grad;
8a-d;?;II;K4;Markieren;WS:scheitel_neben;Scheitel-, Neben-, Stufen-, Wechselwinkel markieren;–;Kl.-7-Stoff Gym, 8 P für 8a–e
8e;?;II;K5;Rechnen;WI:kreuzung;fehlende Winkel ohne Messen;Grad;
""", nummer="3. Klassenarbeit (September laut Übersicht)", passung="Kl. 5, Schulart/Bundesland unbekannt (KlassenarbeitenBoerse)")
KAX(1916, "Klassenarbeit Zahlenterme (Realschule)", 39, """
1;5;II;K3;Sachaufgabe;RG:sach;Klassenkasse: Fehlbetrag verteilen;Euro;
2;3;I;K5;Gleichung;GZ:umkehraufgabe;fehlende Zahl in drei Gleichungen;klein;
3;2;II;K2;Zahlenrätsel;NAT:stellenwert;größte zweistellige Zahlen ohne eine Ziffer;zweistellig;
4;3;I;K3;Sachaufgabe;GZ:schriftlich_plus_minus;mehrere Abgänge abziehen;groß;
5;4;II;K3;Term;RG:termaufbau;Term zu einer Bestellung;klein;
6;3;I;K5;Umkehraufgabe;GZ:umkehraufgabe;fehlender Summand;klein;
7;1;III;K1;Begründen;L:RG:Wie ändert sich der Termwert, wenn man alle Zahlen gleich verändert?;Änderung einer Differenz;–;
8;4;II;K5;Geschickt;RG:vorteil;Summanden geschickt gruppieren;klein;
9;3;I;K5;Rechnen;GZ:schriftlich_plus_minus;schriftlich subtrahieren;groß;
10;4;I;K5;Vergleichen;NAT:vergleichen;Vergleichszeichen setzen;–;
11;1;III;K1;Begründen;L:RG:Wie ändert sich der Termwert, wenn man alle Zahlen gleich verändert?;Summe bei gegenläufiger Änderung;–;
12;6;I;K5;Potenz;POT:schreibweise;Potenzschreibweise und berechnen;klein;
""", passung="Realschule Kl. 5, Bundesland unbekannt")
A("G5-RWTH03", quelle="https://algo.rwth-aachen.de/infoki/Mathe5k/d/Arbeiten/Klassenarbeit03.pdf", titel="Klassenarbeit Nr. 3, Klasse 5 (2004)",
  herausgeber="Unterrichtsmaterial (Hochschulserver, Schule unbekannt)", art="Klassenarbeit (Nr. 3)", nummer="3. Arbeit (Januar)", jahr=2004,
  zeit_min=None, punkte_gesamt=None, lizenz="frei abrufbar; Urheberrecht bei den Autoren – nur verlinkt", bundesland="vermutlich NRW (Annahme)",
  passung="Kl. 5, nicht Bayern", klasse=5, frei=True, hilfsmittel="nicht angegeben", zeilen="""
1a;?;I;K6;Regel;TB:endziffer;Teilbarkeitsregel für 8 aufschreiben;–;
1b;?;I;K6;Wissen;NAT:dualsystem;Ziffern eines anderen Stellenwertsystems;–;
1c;?;II;K5;Umrechnen;NAT:dualsystem;anderes System → Zehnersystem;–;
1d;?;II;K5;Umrechnen;NAT:dualsystem;Zehnersystem → anderes System;–;
1e;?;II;K6;Vergleichen;NAT:roemisch_system;Zahlensysteme vergleichen;–;
2a;?;I;K5;Römisch;NAT:roemisch_schreiben;in römische Zahlen;–;
2b;?;I;K5;Römisch;NAT:roemisch_schreiben;römisch ins Zehnersystem;–;
2c;?;I;K5;Rechnen;NAT:roemisch_system;addieren und prüfen;–;
3;?;III;K1;Begründen;TB:primzahl;ungünstige Anordnung in Kästen begründen;zweistellig;Primzahlen
4a;?;I;K6;Regeln;TB:endziffer;alle Teilbarkeitsregeln;–;
4b;?;I;K5;Teiler;TB:teiler;Zahlen mit gegebenem Teiler;–;
4c;?;II;K5;Teilermenge;TB:teiler;Teilermengen bestimmen;dreistellig;
Z;?;III;K1;Beweis;L:TB:Teilbarkeitsregeln begründen (Quersummenregel);Beweisidee der 3er-/9er-Regel;–;Zusatz
""")
A("G5-WGR12", quelle="https://c.wgr.de/d/b7fb6abdf9cc16e82cfa9fb6ceda3ad5b96b4d42a2cf68dd621c5888601e0923.pdf/23085_klassenarbeiten.pdf",
  titel="Verlagsprobe „Klassenarbeit 1.2“ (natürliche Zahlen und Größen)", herausgeber="Verlag (Leseprobe, Verlag nicht ausgewiesen)",
  art="Klassenarbeit (Verlagsmuster)", nummer="Kapitel 1 – Schuljahresbeginn", jahr=None, zeit_min=45, punkte_gesamt=25,
  lizenz="Verlags-Leseprobe; © Verlag – nur verlinkt", bundesland="unbekannt", passung="Kl. 5, bundesweit", klasse=5, frei=True,
  hilfsmittel="nicht angegeben", zeilen="""
1;?;I;K4;Diagramm;DD:saeulendiagramm;Befragungsergebnis als Diagramm;–;Daten = Kl. 6 Gym
2a;?;I;K5;Vergleichen;NAT:vergleichen;große Zahlen vergleichen;groß;
2b;?;II;K5;Ordnen;NAT:vergleichen;Millionen bis Billionen ordnen;sehr groß;
3a;?;II;K2;Zahl bilden;NAT:stellenwert;kleinste Zahl aus Ziffern;vierstellig;
3b;?;III;K2;Runden rückwärts;NAT:runden_regel;größte Zahl mit gegebener Rundung;groß;
3c;?;I;K5;Runden;NAT:runden_regel;Nachfolger auf Zehner runden;fünfstellig;
4a;?;II;K4;Zahlenstrahl;NAT:strahl_eintragen;Zahlenstrahl zeichnen, eintragen;zweistellig;
4b;?;I;K4;Ablesen;NAT:strahl_ablesen;Punkte ablesen;–;
5a;?;II;K1;Begründen;NAT:runden_sinnvoll;Aussage zu gerundeten Beträgen prüfen;Euro;
5b;?;II;K1;Begründen;GR:massstab;Bildgröße bei zwei Maßstäben prüfen;–;
""")
DUDEN = "https://shop.duden.de/media/24/62/c6/1687426846/Leseprobe_9783411721757_Wissen_–_Üben_–_Testen_Mathematik_5_Klasse.pdf"
A("G5-DUD1", quelle=DUDEN, titel="Duden „Wissen – Üben – Testen 5“, Klassenarbeit 1 (Leseprobe)", herausgeber="Dudenverlag",
  art="Klassenarbeit (Verlagsmuster)", nummer="Kapitel 1 – Zahldarstellungen", jahr=None, zeit_min=45, punkte_gesamt=None,
  lizenz="Verlags-Leseprobe; © Verlag – nur verlinkt", bundesland="bundesweit", passung="Kl. 5, bundesweit", klasse=5, frei=True,
  hilfsmittel="nicht angegeben", zeilen="""
1;?;I;K4;Zahlenstrahl;NAT:strahl_ablesen;fehlende Werte an Zahlenstrahl-Ausschnitten;–;
2;?;II;K5;Umrechnen;NAT:dualsystem;zwischen Zehner-, Zweiersystem und römisch;–;
3;?;II;K3;Textaufgabe;NAT:runden_sinnvoll;Zahlwörter in Ziffern, überschlagen, Rundung begründen;groß;
4;?;II;K1;Fehler finden;NAT:runden_regel;Rundungen prüfen und korrigieren;–;
""")
A("G5-DUD2", quelle=DUDEN, titel="Duden „Wissen – Üben – Testen 5“, Klassenarbeit 2 (Leseprobe)", herausgeber="Dudenverlag",
  art="Klassenarbeit (Verlagsmuster)", nummer="Kapitel 1 – Zahldarstellungen", jahr=None, zeit_min=60, punkte_gesamt=None,
  lizenz="Verlags-Leseprobe; © Verlag – nur verlinkt", bundesland="bundesweit", passung="Kl. 5, bundesweit", klasse=5, frei=True,
  hilfsmittel="nicht angegeben", zeilen="""
1;?;I;K5;Umrechnen;NAT:dualsystem;Dualzahlen ins Zehnersystem;–;
2;?;I;K5;Nachbarzahlen;NAT:vergleichen;Vorgänger, Nachfolger;groß;
3;?;I;K5;Zahlwort;NAT:zahlwort_zu_ziffern;Zahlwörter in Ziffern;groß;
4;?;II;K5;Umrechnen;NAT:dualsystem;Zehner- in Zweiersystem;–;
5;?;II;K5;Römisch;NAT:roemisch_schreiben;Tabelle römisch/dezimal;–;
6;?;II;K3;Überschlag;RG:ueberschlag;Gesamtstrecke überschlagen;km;
7;?;II;K3;Überschlag;RG:ueberschlag;Kosten überschlagen;Euro;
8;?;II;K5;Vergleichen;NAT:dualsystem;Dualzahlen vergleichen, Nachbarn;–;
9;?;II;K6;Runden;NAT:runden_regel;Größen runden, ordnen, Kriterium nennen;groß;
""")
A("G5-DUDTA1", quelle="https://shop.duden.de/media/9c/00/01/1687432547/Leseprobe_9783411727940_Super_Noten_am_Gymnasium_–_Klassenarbeitstrainer_Mathematik_5_Klasse.pdf",
  titel="Duden „Super Noten am Gymnasium 5“, Trainingsarbeit 1 (Leseprobe)", herausgeber="Dudenverlag",
  art="Trainingsarbeit (Verlagsmuster)", nummer="Kapitel 1 – natürliche Zahlen", jahr=None, zeit_min=None, punkte_gesamt=30,
  lizenz="Verlags-Leseprobe; © Verlag – nur verlinkt", bundesland="bundesweit", passung="Gym Kl. 5, bundesweit", klasse=5, frei=True,
  hilfsmittel="nicht angegeben", zeilen="""
1;3;I;K4;Ablesen;NAT:strahl_ablesen;Skala ablesen;–;
2;4;II;K1;Vergleichen;NAT:vergleichen;große Zahlen vergleichen und begründen;groß;
3;4;I;K5;Stellenwert;NAT:stellenwert;Stellenwertangaben in Ziffern;groß;
4;4;II;K5;Ordnen;NAT:vergleichen;unterschiedlich geschriebene Zahlen ordnen;groß;
5;6;I;K5;Nachbarzahlen;NAT:vergleichen;Vorgänger-/Nachfolger-Tabelle;groß;
6;9;II;K5;Runden;NAT:runden_regel;runden und passende Zahlen finden;groß;
""")
A("G5-TUT1", quelle="https://tutory.de/entdecken/dokument/test-klasse-5-naturliche-zahlen.pdf?t=2413", titel="Test Klasse 5: Natürliche Zahlen (tutory)",
  herausgeber="tutory.de (Lehrkraft-Material, Schule unbekannt)", art="Test/Kurzarbeit", nummer="Schuljahresbeginn", jahr=None,
  zeit_min=None, punkte_gesamt=23, lizenz="frei abrufbar auf tutory.de; Lizenz laut Dokument – nur verlinkt", bundesland="unbekannt",
  passung="Kl. 5, Schulart/Bundesland unbekannt", klasse=5, frei=True, hilfsmittel="nicht angegeben", zeilen="""
1;4;I;K5;Lücken;GZ:umkehraufgabe;fehlende Werte in Rechnungen;klein;
2;3;I;K5;Runden;NAT:runden_regel;drei Zahlen runden;groß;
3;3;I;K4;Zahlenstrahl;NAT:strahl_eintragen;Zahlen markieren;–;
4;3;III;K2;Knobel;GE:zwei_schritte;Werte für drei Variablen bestimmen;klein;
5;6;I;K5;Rechnen;RG:klammern;drei Terme mit Rechenweg;klein;
6;4;II;K3;Gleichung;GE:aufstellen;Sachaufgaben als Gleichung;klein;
""")

# ---- Klasse 8: BMT8 2005–2008
BMT(2008, "A", "2008/bmt8_2008_aufgaben_gruppe_a.pdf", """
1;2;II;K5;Volumen;VOL:zusammengesetzt;Quader mit ausgeschnittenem Würfel;cm;
2a;1;I;K3;Auswahl;ZP:gross_wissenschaftlich;Gesamtwert einer Scheinsorte abschätzen;Milliarden;
2b;2;II;K3;Schätzen;PZ:prozentsatz;Anteil einer Sorte überschlagen und begründen;Millionen;
3a;2;II;K5;Gleichung;LG:klammern;Gleichung mit Klammer und Bruch;klein;Punkte 3a/3b, 4a, 8, 9 teils unsicher
3b;1;III;K2;Umkehren;L:LG:Zahl in einer Gleichung so wählen, dass eine vorgegebene Lösung entsteht;Zahl ersetzen, damit eine bestimmte Lösung entsteht;klein;
4a;1;II;K1;Vergleich;PZ:verstehen;häufigsten Mangel über Anteile bestimmen;Prozent/Brüche;
4b;1;III;K1;Begründen;L:DD:Mehrfachnennungen in Umfragen erkennen;Aussage über mehr als die Hälfte widerlegen;–;
5a;1;II;K5;Rechnen;WS:vieleck;Eckenzahl aus Winkelsumme;klein;
5b;1;II;K5;Rechnen;WS:vieleck;Innenwinkel eines regelmäßigen Vielecks;Grad;
6a;1;II;K1;Formel;FV:drachen_raute;Rautenfläche aus Diagonalen;–;
6b;2;II;K4;Konstruieren;KST:vierecke_konstruieren;Raute mit vorgegebenem Winkel konstruieren;–;nur Zirkel und Lineal
7;1;I;K5;Rechnen;BRR:gemischt;Term mit Dezimalzahlen;klein;
8a;1;III;K2;Offen;GZ:zahlengerade;zwei Zahlen verschiedenen Vorzeichens mit gegebener Mitte;zweistellig;offen
8b;1;II;K5;Rechnen;BRR:brueche_plus_minus;Mittelwert zweier Brüche;klein;
9a;2;II;K3;Rechnen;TA:sachsituation;Länge aus Breite in einer Figur;cm;
9b;1;II;K5;Term;TA:sachsituation;Flächenterm aufstellen und vereinfachen;Variable;
""")
BMT(2007, "A", "2007/bmt8_2007_aufgaben_gruppe_a.pdf", """
1;?;II;K3;Maßstab;GR:massstab;Höhe auf vergrößertem Bild;Meter;Punkte 1 und 3 zusammen 2
2a;1;I;K4;Kreisdiagramm;DD:kreisdiagramm;Kreisdiagramm ergänzen und beschriften;Prozent;
2b;1;II;K5;Zählen;KOMB:zaehlprinzip;Färbungen von Sektoren zählen;klein;
3;?;I;K5;Umrechnen;GR:laenge;vier Größen umrechnen (Länge, Masse, Fläche, Zeit);gemischt;
4a;2;I;K4;Konstruieren;KR:thales;Mittelsenkrechte und Thaleskreis konstruieren;–;
4b;1;II;K1;Begründen;KR:thales;rechtwinklig begründen;–;
4c;2;II;K1;Ankreuzen;KST:kongruenzsatz;gültige Kongruenzbegründungen ankreuzen;–;
5a;1;I;K5;Rechnen;BRR:gemischt;Term mit Dezimalzahl, Bruch, Klammern;klein;
5b;1;III;K2;Umkehren;TA:termwert;Zahl ersetzen, damit sich der Termwert verdoppelt;klein;
6a;2;II;K5;Prozent;PGW:prozentsatz;prozentuale Verkürzung einer Fahrzeit;Minuten;
6b;1;II;K3;Auswahl;PROP:sach;Term für Durchschnittsgeschwindigkeit;km, min;
7a;2;II;K5;Umformen;TU:summe_mal_summe;Produkt zweier Klammern ausmultiplizieren;Variable;
7b;1;I;K5;Umformen;PGN:mal_gleiche_basis;Potenzterm vereinfachen;Variable;
8;2;II;K5;Fläche;FV:zusammengesetzt;Vierecksfläche aus Gitterkoordinaten;klein;
9;2;III;K2;Offen;FL:zerlegen;zwei Löcher mit Rand, Fläche halbieren;cm²;offen
""")
BMT(2006, "A", "2006/bmt8-06a.pdf", """
1;2;II;K5;Gleichung;LG:klammern;lineare Gleichung mit Klammern;Dezimal;
2a;2;II;K4;Konstruieren;KON:symmetrie;Symmetrieachse konstruieren;–;
2b;1;I;K4;Ankreuzen;KON:symmetrie;Punkt- und Achsensymmetrie von Figuren;–;
3;1;II;K1;Wahr/falsch;DD:relative_haeufigkeit;Aussagen zu Glücksrad-Ergebnissen;bis 20;Zufall
4;2;I;K5;Rechnen;POT:negativ;Term mit negativen Zahlen und Potenzen;klein;
5a;2;I;K5;Umrechnen;GR:masse;Gewichtszunahme von t in kg;t;
5b;2;II;K5;Prozent;PGW:zurueck;Wert aus 30 % weniger;t;
6a;1;I;K5;Maßstab;GR:massstab;Originallänge aus Modell;m;
6b;1;II;K5;Maßstab;GR:massstab;Höhe und Fläche bei neuem Maßstab;m, m²;Flächenmaßstab
7a;2;II;K5;Fläche;FV:dreieck;Längen messen, Dreiecksfläche;cm;
7b;1;II;K4;Konstruieren;FV:verstehen;rechtwinkliges Dreieck gleicher Fläche;–;
8;1;II;K6;Beschreiben;DK:mittelwert;Vorgehen für Durchschnittsgröße beschreiben;–;
9a;1;II;K3;Muster;TA:muster;Stäbe für ein Geländer zählen;zweistellig;
9b;1;II;K1;Begründen;TA:muster;allgemeine Formel begründen;n;
9c;1;III;K2;Auswahl;TA:muster;Stabzahlen ohne Rest;um 100;
""")
BMT(2005, "A", "2005/bmt8_2005_aufgaben_gruppe_a.pdf", """
1;1;I;K4;Ankreuzen;KON:punktspiegelung;Bildfigur bei Punktspiegelung;–;
2a;1;I;K5;Prozent;PZ:prozentsatz;Saftanteil in Prozent;Liter;
2b;1;II;K5;Dreisatz;PROP:dreisatz;Saftmenge für größere Menge;Liter;
2c;2;II;K3;Sachaufgabe;RG:sach;Einnahmen aus Becherverkauf;Cent;
3;1;III;K2;Rückwärts;BRR:sach;Anfangsmenge aus abgegebenen Anteilen;klein;Rückwärtsrechnen
4a;1;I;K4;Diagramm;DD:saeulendiagramm;Summe aus Säulendiagramm;Hunderter;
4b;2;II;K1;Begründen;DD:tabelle_auswerten;Jahr mit kleinstem Anteil begründen;Hunderter;
5;1;III;K2;Offen;VOL:liter;Kantenlängen für halbes Volumen;cm, Liter;offen
6;1;I;K5;Umformen;TU:minusklammer;Term mit Klammern vereinfachen;klein;
7a;1;II;K5;Potenz;BRR:potenzen;Termwerte mit n im Exponenten;nahe 0;
7b;1;II;K4;Zahlengerade;DEZ:vergleichen_ordnen;Werte auf Zahlengerade eintragen;-1 bis 1;
7c;2;III;K1;Begründen;BRR:potenzen;Lage aufeinanderfolgender Werte beschreiben;n;Muster
8;1;III;K3;Schätzen;GR:massstab;Seefläche aus Karte schätzen;km²;
9a;2;II;K6;Beschreiben;KST:planfigur;Konstruktion eines gleichseitigen Dreiecks beschreiben;–;
9b;1;II;K5;Winkel;WS:figuren;Winkel in Figur aus Quadrat und Dreieck;Grad;
9c;2;III;K1;Winkel;WS:vieleck;Winkel mit Begründung (Fünfeck);Grad;
""")

# ---- Klasse 8: weitere Arbeiten zum Kl.-8-Stoff
A("G8-14", quelle="https://www.lehmanns.ch/media/88672765", titel="STARK Klassenarbeiten Mathe 8 – Klassenarbeit 5 (Leseprobe)",
  herausgeber="STARK Verlag", art="Klassenarbeit (Verlagsmuster)", nummer="Themenbereich 2 (Annahme: 2. SA-Zeitraum)", jahr=None,
  zeit_min=None, punkte_gesamt=40, lizenz=LIZ_STARK, bundesland="Bayern (Annahme: G8-Themenbereiche)", passung="Gym Kl. 8, G8-Lehrplan (Annahme Bayern)",
  klasse=8, frei=True, hilfsmittel="nicht angegeben", zeilen="""
1a;6;II;K4;Zeichnen+Rechnen;FLIN:graph_ablesen;Gerade aus Achsenabschnitt und Steigung zeichnen, Nullstelle, Punktlage;klein;
1b;2;II;K5;Ungleichung;UNG:grafisch;wo der Term nicht negativ ist;klein;
1c;2;II;K4;Spiegeln;L:FLIN:Gerade an einer Achse spiegeln und Gleichung angeben;Gleichung nach Spiegelung an der x-Achse;klein;
2a;6;II;K3;Modellieren;FLIN:deuten;Füllstand modellieren, Funktion aufstellen;Liter;
2b;2;II;K5;Rechnen;FG:stelle;Zeit bis zur vollen Füllung;Liter;
3a;4;III;K4;Zeichnen;L:UNG:Lösungsmenge eines Ungleichungssystems grafisch darstellen;Ungleichungssystem grafisch lösen;klein;
3b;4;II;K5;Ungleichung;UNG:klammern;Ungleichung mit Klammern und Brüchen;klein;
4;4;II;K5;LGS;LGS:addition;LGS mit Additionsverfahren;klein;
5a;5;III;K3;Sachaufgabe;LGS:sachaufgabe;Mischungsaufgabe mit Temperaturen;Liter, °C;
5b;5;III;K3;Sachaufgabe;LGS:sachaufgabe;Einkaufspreise aus Aufschlägen;Euro, Prozent;
""")
A("G8-15", quelle=KA+"3800.pdf", titel="Klassenarbeit Nr. 3 Lineare Gleichungen und Funktionen (ohne 4 P Sprache/Form)",
  herausgeber="klassenarbeiten.de (Schule unbekannt)", art="Klassenarbeit (Nr. 3)", nummer="3. Arbeit (April)", jahr=None, zeit_min=None,
  punkte_gesamt=43, lizenz=LIZ_KA, bundesland="Berlin", passung="Gym Kl. 8, nicht Bayern (Berlin)", klasse=8, frei=True,
  hilfsmittel="nicht angegeben", zeilen="""
1a;2;I;K5;Umformen;TU:binomisch;Binom quadrieren;klein;
1b;1;I;K6;Benennen;TU:binomisch;passende binomische Formel nennen;–;
2a;6;I;K6;Wissen;UNG:umdrehen;erlaubte Umformungen, Besonderheit bei Ungleichungen;–;Wissensfrage
2b;10;II;K5;Gleichung;UNG:klammern;vier Gleichungen/Ungleichungen lösen;klein;
3a;3;I;K5;Formel;FO:einsetzen;Füllmenge mit Formel berechnen;Liter;
3b;5;II;K5;Umstellen;FO:zwei_schritte;Formel umstellen, Zeitpunkt berechnen;Liter;
4a;2;I;K6;Definieren;FG:eindeutig;Funktionsbegriff erklären;–;
4b;8;I;K4;Tabelle+Graph;FG:wertetabelle;Wertetabelle ergänzen und Graph zeichnen;klein;
4c;6;II;K4;Ablesen;FLIN:ablesen;Steigung und Achsenabschnitt ablesen;klein;
""")
A("G8-16", quelle=KA+"4033.pdf", titel="Probearbeit 8. Klasse: Terme, Gleichungen, Formeln",
  herausgeber="klassenarbeiten.de (Schule unbekannt)", art="Probearbeit", nummer="unbekannt", jahr=None, zeit_min=None,
  punkte_gesamt=None, lizenz=LIZ_KA, bundesland="unbekannt", passung="Kl. 8, Schulart/Bundesland unbekannt (Stoff eher Kl. 7)", klasse=8,
  frei=True, hilfsmittel="nicht angegeben", zeilen="""
1;?;I;K5;Umformen;TU:minusklammer;mehrere Terme vereinfachen;klein;
2a;?;II;K5;Ausklammern;TU:ausklammern;größten gemeinsamen Faktor ausklammern;klein;
2b;?;II;K5;Ausklammern;TU:ausklammern;Ausklammern mit Dezimalzahlen;Dezimal;
3a;?;II;K3;Gleichung aufstellen;LG:sach;Gleichung zu einem Text aufstellen;zweistellig;nur aufstellen
3b;?;II;K3;Gleichung aufstellen;LG:sach;Bruchteile einer Zahl;Brüche;
3c;?;II;K3;Gleichung aufstellen;LG:sach;verschachtelte Wortbeschreibung;klein;
4a;?;II;K5;Gleichung;LG:klammern;Gleichung mit Klammern;klein;
4b;?;II;K5;Gleichung;LG:beide_seiten;Gleichung mit Dezimalzahlen;Dezimal;
5a;?;I;K5;Umstellen;FO:geometrie;Umfangsformel nach einer Seite umstellen;–;
5b;?;I;K5;Umstellen;FO:geometrie;Dreiecksfläche nach der Höhe umstellen;–;
""")

def T10(jahr, datei, zeilen):
    m = dict(BMT10); m.pop("art", None)
    A(f"G8-T{jahr}", quelle=ISB+datei, titel=f"BMT10 {jahr} (Auszug)", jahr=jahr, art=BMT10["art"], zeilen=zeilen,
      **{k: v for k, v in m.items() if k != "art"})

T10(2025, "2025/BMT10_2025_Aufgaben_Gruppe_A.pdf", """
2a;1;II;K1;Begründen;STO:laplace_pruefen;Bedingung für ein Laplace-Experiment nennen;–;
3a;1;I;K5;Definitionsmenge;FGB:definitionsmenge;maximale Definitionsmenge;klein;
3b;2;II;K5;Nullstelle;FGB:achsenpunkte;Nullstelle berechnen;klein;
3c;1;I;K5;Asymptote;FGB:asymptoten;waagrechte Asymptote angeben;klein;
5a;1;II;K5;Auswahl;PGW:prozentsatz;Bruch für prozentuale Abnahme wählen;Tausender;Kl.-7-Stoff
5b;2;II;K3;Deuten;FLIN:deuten;Funktionswert berechnen und deuten;Tausender;
5c;1;II;K3;Anpassen;FLIN:wirkung;Funktion mit halber Abnahme;Tausender;
6b;2;III;K5;Gleichung;BG:hauptnenner;Bruchgleichung lösen, Ergebnis zeigen;Variable;
""")
T10(2024, "2024/BMT10_2024_Aufgaben_Gruppe_A.pdf", """
1b;1;I;K5;Umformen;PGZ:terme_vereinfachen;Potenz-Bruchterm vereinfachen;Variable;
3a;1;I;K5;Ereignis;STO:begriffe;Schnittmenge zweier Ereignisse angeben;bis 100;
3b;1;I;K4;Ereignis;STO:begriffe;Vereinigung im Diagramm schraffieren;–;
4b;1;II;K5;Auswahl;BRR:sach;Term für einen Anteil wählen;Millionen;
5a;1;I;K5;Funktionswert;FG:funktionswert;Reaktionsweg berechnen;m;
5c;2;II;K4;Zeichnen;FLIN:schnittpunkte;Gerade zeichnen, Schnittstelle ablesen;km/h;
5d;2;II;K5;Gleichung;FO:einsetzen;Parameter aus Anhalteweg bestimmen;m;
6a;1;I;K5;Auswahl;PZY:zylinder_volumen;Term für Zylindervolumen;cm;
7a;1;I;K5;Rechnen;IND:produkt;Rechteckseiten an einer Hyperbel;klein;
7b;1;II;K1;Zeigen;IND:produkt;konstante Rechteckfläche zeigen;Variable;
7c;1;III;K5;Rechnen;FGB:beurteilen;Schnitt Hyperbel–Gerade exakt;Wurzel;
""")
T10(2023, "2023/BMT10_2023_Aufgaben_Gruppe_A.pdf", """
2a;1;I;K4;Tabelle;L:STO:Vierfeldertafel ergänzen;Vierfeldertafel ergänzen;Tausend;in LehrplanPLUS später
2b;1;II;K5;Wahrscheinlichkeit;STO:gegenereignis;mindestens ein Merkmal;Prozent;
2c;1;II;K6;Auswahl;STO:begriffe;Ereignis in Worten zuordnen;–;
4a;1;I;K1;Begründen;BT:definitionsmenge;Term nicht überall definiert;klein;
4b;2;II;K5;Kürzen;BT:kuerzen;Term kürzen;klein;
5a;1;I;K5;Umrechnen;ZP:vorsilben_klein;Mikrogramm in Gramm;10^-6;
5c;2;II;K5;Rechnen;FLIN:zwei_punkte;Gerade durch zwei Punkte;Jahre, µg;
5d;1;II;K6;Beschreiben;UNG:sachaufgabe;Vorgehen für Unterschreitung beschreiben;–;
""")
T10(2021, "2021/bmt10_2021_aufgaben_gruppe_a.pdf", """
1a;1;I;K5;Bruchgleichung;BG:ein_bruch;einfache Bruchgleichung;klein;
5a;1;I;K6;Lückentext;STO:laplace;Laplace-Begründung fachsprachlich ergänzen;–;
5b;2;III;K5;Wahrscheinlichkeit;STO:gegenereignis;Gegenereignis bei zweimaligem Drehen;Brüche;zweistufig
6a;1;I;K4;Zeichnen;FLIN:graph_ablesen;Gerade mit negativer Steigung zeichnen;klein;
6b;2;III;K2;Rechnen;FLIN:einsetzen;Parameter für vorgegebene Dreiecksfläche;klein;
""")
T10(2018, "2018/bmt10_2018_aufgaben_gruppe_a.pdf", """
1a;1;I;K5;Potenz;PGZ:terme_vereinfachen;Potenzterm vereinfachen;klein;
1b;1;II;K5;Potenz;PGZ:exponent_und_potenz;Klammerpotenz vereinfachen;klein;
4a;2;II;K1;Zeigen;STO:laplace;Wahrscheinlichkeiten beim Würfelspiel zeigen;klein;
4b;1;III;K1;Zeigen;STO:laplace;Behauptung zur Gewinnchance bestätigen;–;
7b;2;III;K1;Herleiten;TU:binomisch;Flächen gleichsetzen und vereinfachen;Variable;Pythagoras-Herleitung
""")
T10(2017, "2017/bmt10_2017_aufgaben_gruppe_a.pdf", """
1a;1;II;K5;Ankreuzen;FO:pruefen;richtige Gleichungen zwischen Größen ankreuzen;–;Kegel (Kl. 10)
1c;1;II;K5;Umstellen;FO:zwei_schritte;Oberflächenformel umstellen;–;
2;2;II;K4;Steigung;FLIN:deuten;Steigung in Prozent aus Figur;Prozent;
4b;1;II;K1;Begründen;STO:laplace_pruefen;kein Laplace-Experiment zeigen;–;
4c;1;III;K2;Ereignis angeben;STO:begriffe;Ereignis mit vorgegebener Wahrscheinlichkeit;Prozent;
4d;1;III;K5;Auswahl;STO:gegenereignis;Term für zweimaliges Gegenereignis;Dezimal;zweistufig
""")
T10(2015, "2015/bmt10_2015_aufgaben_gruppe_a.pdf", """
2b;1;I;K4;Zeichnen;FLIN:graph_ablesen;Gerade mit Bruchsteigung einzeichnen;klein;
3;1;III;K6;Ereignis angeben;STO:begriffe;Ereignis zu einer Wahrscheinlichkeit beschreiben;–;
6a;2;III;K3;Schätzen;KRB:flaeche;überstrichene Kreisfläche schätzen;m;
6c;1;II;K5;Umstellen;FO:zwei_schritte;Formel nach einer Größe auflösen;–;dritte Wurzel
7a;1;II;K4;Zeichnen;KR:umkreis_inkreis;Viereck ohne Umkreis zeichnen;–;
7b;2;III;K1;Beweisen;KR:umkehrung;Umkreis bei zwei rechten Winkeln beweisen;–;
""")
T10(2014, "2014/bmt10_2014_aufgaben_gruppe_a.pdf", """
1c;2;II;K3;Indirekt;IND:dreisatz;Wert bei anderer Auslastung;kg;
2;2;II;K4;Term angeben;FGB:parameter;Term zu verschobener Hyperbel;klein;
8a;1;I;K5;Gegenereignis;STO:gegenereignis;Gegenwahrscheinlichkeit;Prozent;
8b;2;III;K5;Wahrscheinlichkeit;X:mehrstufige Zufallsexperimente (Pfadregel, Kl. 9/10);Wahrscheinlichkeit für drei Orte zugleich;Prozent;
9;2;III;K1;Verallgemeinern;BT:fehler_finden;Muster als Gleichung verallgemeinern und prüfen;n;
""")
T10(2013, "2013/bmt10_2013_aufgaben_gruppe_a.pdf", """
1;2;II;K5;LGS;LGS:verfahren;LGS lösen;klein;
3a;2;II;K6;Beschreiben;KR:tangente;Tangentenkonstruktion beschreiben;–;
3b;1;II;K5;Term;X:Satz des Pythagoras (Kl. 9);Tangentenlänge als Term;r, s;
3c;1;II;K5;Term;FV:drachen_raute;Drachenfläche als Term;r;
4;2;III;K3;Schätzen;PZY:zylinder_volumen;Tankvolumen schätzen;m³;
5a;1;II;K5;Auswahl;BG:verhaeltnis;passende Verhältnisgleichung;–;Strahlensatz
""")
T10(2012, "2012/bmt10_2012_aufgaben_gruppe_a.pdf", """
1a;1;I;K5;Rechnen;FO:geometrie;mittlere Tiefe aus Volumen und Fläche;m;
4;1;II;K1;Gegenbeispiel;UNG:pruefen;Ungleichung für alle reellen Zahlen prüfen;–;
5;2;II;K5;Umformen;PGZ:terme_vereinfachen;Potenz-Bruchterm vereinfachen;Variable;
6a;1;I;K4;Graph;FGB:beurteilen;passenden Graph ankreuzen;–;
6b;2;II;K5;Rechnen;FG:funktionswert;Funktionswerte und prozentuale Abnahme;Faktor;
6c;1;II;K5;Umstellen;FO:zwei_schritte;Gleichung nach dem Abstand auflösen;–;Wurzel
7;2;II;K1;Begründen;FLIN:deuten;Steigungsaussage prüfen;Prozent;
8;2;III;K5;Wahrscheinlichkeit;X:mehrstufige Zufallsexperimente (Pfadregel, Kl. 9/10);Glücksrad dreimal;Brüche;
""")
T10(2011, "2011/bmt10_aufgabe_a.pdf", """
3;2;II;K5;Laplace;STO:laplace;Augensumme bei zwei Würfen;klein;
4a;1;II;K5;Formel;FO:geometrie;Höhenformel ergänzen;–;Pythagoras
6;2;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
""")
A("G8-T2010", quelle=ISB+"2010/bmt10-2010-aufgaben-gruppe-b.pdf", titel="BMT10 2010 Gruppe B (Auszug)", jahr=2010,
  **{k: v for k, v in BMT10.items()}, zeilen="""
3;2;II;K6;Erklären;PZY:zylinder_volumen;zwei Näherungsformeln deuten;–;
4b;1;II;K5;Umformen;BT:kuerzen;Term vereinfachen;klein;Text unklar
4c;1;II;K5;Umformen;PGZ:terme_vereinfachen;Term vereinfachen;klein;Text unklar
6a;2;III;K4;Baumdiagramm;X:mehrstufige Zufallsexperimente (Pfadregel, Kl. 9/10);Baumdiagramm, genau ein Treffer;Prozent;
6b;2;III;K6;Gegenereignis;STO:gegenereignis;Gegenereignis beschreiben und Term angeben;–;
""")
T10(2009, "2009/bmt10-2009-aufgaben-gruppe-a.pdf", """
2a;1;I;K5;Potenz;PGZ:gleiche_basis_ganz;Potenz mit negativem Exponenten;klein;
2b;1;I;K5;Potenz;PGZ:terme_vereinfachen;Potenzausdruck;klein;
3a;1;II;K4;Zeichnen;FGB:beurteilen;Hyperbel symmetrisch ergänzen;–;
3b;1;II;K4;Zeichnen;FGB:parameter;zweiten Graphen zeichnen;–;
3c;2;II;K5;Bruchgleichung;BG:hauptnenner;Gleichung mit Brüchen lösen;klein;
3d;2;II;K6;Deuten;BG:graphisch;Lösungen als Schnittstellen deuten;–;
5a;1;II;K1;Begründen;STO:laplace_pruefen;Augensummen nicht gleich wahrscheinlich;–;
5b;1;I;K5;Laplace;STO:laplace;Wahrscheinlichkeit einer Augensumme;klein;
6b;1;II;K5;Auswahl;KRB:umfang;Bahngeschwindigkeit wählen;km/h;
""")
T10(2008, "2008/bmt10_2008_aufgaben_gruppe_a.pdf", """
1b;1;III;K3;Offen;PZY:prisma_volumen;passende Raumgröße vorschlagen;m³;offen
4a;2;III;K5;Baumdiagramm;X:mehrstufige Zufallsexperimente (Pfadregel, Kl. 9/10);zwei verschiedenfarbige Kugeln;Brüche;
4b;1;II;K1;Begründen;X:Ziehen mit/ohne Zurücklegen (Kl. 9/10);mit oder ohne Zurücklegen begründen;–;
6b;1;II;K2;Term angeben;FGB:definitionsmenge;Term mit Definitionslücke angeben;klein;
7a;1;II;K6;Erklären;PZY:zylinder_oberflaeche;Mantelflächenformel erklären;–;
7b;1;II;K5;Umstellen;FO:zwei_schritte;Oberflächenformel nach der Höhe;–;
8;2;II;K1;Beweisen;KR:beweis;Winkelsumme am Halbkreis beweisen;–;
""")
T10(2005, "2005/bmt10_2005_aufgaben_gruppe_a.pdf", """
1;1;I;K5;Bruchgleichung;BG:ein_bruch;Bruchgleichung lösen;klein;
3a;1;II;K4;Auswahl;KD:schraegbild;senkrechte Gerade im Quader erkennen;–;
3b;1;II;K5;Fläche;PZY:prisma_oberflaeche;Rechteckfläche im Quader;cm²;
3c;2;II;K5;Volumen;PZY:prisma_volumen;Volumenanteil eines Prismas;–;
5b;1;III;K2;Intervall;IV:schreiben;Winkelbereich angeben;Grad;
6a;1;II;K5;Definitionsmenge;IV:lesen;Definitionsbereich ankreuzen;–;Wurzel (Kl. 9)
6b;2;II;K5;Bruchterm;BT:termwert;Termwert zeigen;Dezimal;
6c;2;II;K5;Bruchterm;BT:termwert;Werte in eine Formel einsetzen;Prozent;
""")
