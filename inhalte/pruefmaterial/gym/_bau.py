#!/usr/bin/env python3
"""Baut katalog.json und katalog.md (Prüfmaterial Gymnasium Bayern, Kl. 5 und 8).

Nur Katalog-Daten in eigenen Worten: keine Aufgabentexte, keine Lösungen, keine Namen von Personen.
Aufruf aus dem Repo-Wurzelverzeichnis:  python3 inhalte/pruefmaterial/gym/_bau.py
Zeilenformat je Aufgabe:  nr;punkte;niveau;kompetenz;typ;ZUORDNUNG;kurz;groesse;besonderheit
  ZUORDNUNG:  KUERZEL:etappe            -> Thema/Etappe aus inhalte/themen
              L:KUERZEL:Vorschlag       -> Lücke (nächstes Thema + Vorschlag)
              X:Grund                   -> außerhalb unseres Stoffs (anderer Jahrgang)
  punkte '?' = nicht eindeutig zuordenbar.  niveau I/II/III = eigene Einschätzung (Annahme).
  kompetenz K1–K6 (Bildungsstandards) = eigene Einschätzung.
"""
import json, os, collections

ABRUF = "2026-11-22"
HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))

K = {  # Kürzel -> thema_schluessel
 "NAT": "zahlen.natuerlich", "GZ": "zahlen.ganz", "RG": "zahlen.rechengesetze", "POT": "zahlen.potenzen_basis",
 "TB": "zahlen.teilbarkeit", "KOMB": "stochastik.kombinatorik", "GE": "gleichungen.einfach",
 "GR": "groessen.einheiten", "PROP": "groessen.proportional", "GB": "geometrie.grundbegriffe",
 "WI": "geometrie.winkel", "OL": "geometrie.ortslinien", "FL": "messen.flaechen", "KB": "messen.koerper_berechnung",
 "ZP": "zahlen.potenzen_zehner", "BR": "bruch.brueche", "DEZ": "bruch.dezimal", "BRR": "bruch.rechnen",
 "PZ": "bruch.prozent", "DD": "daten.darstellen", "DK": "daten.kennwerte", "FV": "messen.flaechen_vielecke",
 "VOL": "messen.volumen", "TA": "terme.aufstellen", "PGN": "terme.potenzgesetze_natuerlich", "TU": "terme.umformen",
 "KON": "abbildungen.kongruenz", "WS": "geometrie.winkelsaetze", "LG": "gleichungen.linear",
 "PGW": "bruch.prozent_grundwert", "BOX": "daten.boxplot", "KST": "geometrie.konstruktion", "KR": "geometrie.kreis",
 "FG": "funktionen.grundbegriffe", "FLIN": "funktionen.linear", "UNG": "gleichungen.ungleichungen",
 "IND": "groessen.indirekt", "FGB": "funktionen.gebrochen", "BT": "terme.bruchterme",
 "PGZ": "terme.potenzgesetze_ganzzahlig", "BG": "gleichungen.bruch", "FO": "gleichungen.formeln",
 "STO": "stochastik.grundbegriffe", "LGS": "gleichungen.lgs2", "KRB": "messen.kreisberechnung",
 "KD": "messen.koerper_darstellung", "PZY": "messen.prisma_zylinder",
}

ISB = "https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/"
KA = "https://www.klassenarbeiten.de/data/dynamic/pdf/"
LIZ_ISB = "amtlich (ISB), frei abrufbar; Urheberrecht beim ISB – nur verlinkt, nicht kopiert"
LIZ_KA = "frei abrufbar auf klassenarbeiten.de; Urheberrecht beim Anbieter – nur verlinkt"
LIZ_SCHULE = "auf der Schul-Homepage veröffentlicht; Urheberrecht bei der Schule – nur verlinkt"
LIZ_STARK = "Verlags-Leseprobe (STARK); © Verlag – nur verlinkt, Inhalt nur beschrieben"
BMT_META = dict(art="Jahrgangsstufentest BMT8 (Grundwissen Kl. 5–7)", herausgeber="ISB Bayern", klasse=8,
                nummer="Test zu Beginn Kl. 8 (Sept./Okt.)", zeit_min=40, punkte_gesamt=21,
                hilfsmittel="kein Taschenrechner, keine Formelsammlung; Geodreieck/Zirkel", frei=True, lizenz=LIZ_ISB,
                bundesland="Bayern", passung="Bayern, aber Stoff Kl. 5–7 (nicht Kl.-8-Stoff)")

ARBEITEN = []
def A(id, **m):
    m["arbeit_id"] = id
    m["aufgaben"] = [z.strip() for z in m.pop("zeilen").strip().splitlines() if z.strip()]
    ARBEITEN.append(m)

# ---------------------------------------------------------------- Klasse 5
KL5 = dict(klasse=5, frei=True, hilfsmittel="nicht angegeben")
A("G5-01", quelle=KA+"1170.pdf", titel="Klassenarbeit Gleichungen und Terme", herausgeber="klassenarbeiten.de (Schule unbekannt)",
  art="Klassenarbeit/Schulaufgabe", nummer="unbekannt (Annahme: 2./3. SA, Lernbereich M5 3)", jahr=None, zeit_min=None,
  punkte_gesamt=42, lizenz=LIZ_KA, bundesland="unbekannt", passung="Gym Kl. 5, Bundesland unbekannt", **KL5, zeilen="""
1;3;II;K3;Sachaufgabe+Term;RG:termaufbau;Restbetrag nach zwei Käufen, dann allgemeiner Term;Euro, zwei-/dreistellig;Variable im Sachkontext
2;4;II;K5;Gleichung aufstellen+lösen;GE:aufstellen;zwei Sätze in Gleichungen übersetzen und lösen;zweistellig;
3;3;I;K5;Vergleichen;POT:berechnen;Vergleichszeichen zwischen Potenzen und Produkten;bis Tausender;
4;6;II;K5;Term aufstellen;RG:termaufbau;drei Wortterme mit Variable notieren, ohne zu rechnen;zwei-/dreistellig;Variable x
5;4;II;K4;Gleichung lösen;GE:zwei_schritte;zwei Gleichungen über N lösen, mit Pfeilbild;zwei-/dreistellig;Pfeilbild verlangt
6;3;II;K5;Lösungsmenge bestimmen;L:GE:Lösungsmenge in einer vorgegebenen Grundmenge bestimmen (Bedingungen prüfen);Lösungsmenge aus Grundmenge mit drei Bedingungen;Ziffern, bis ca. 40;Mengenschreibweise
7;4;II;K3;Sachaufgabe+Term;RG:sach;Kosten aus Stundenlohn und Pauschale, allgemeiner Rechenausdruck;Euro;
8;5;II;K5;Ungleichung;L:GE:Ungleichungen über N über die zugehörige Gleichung lösen;Ungleichung über die Gleichung lösen;zwei-/dreistellig;Ungleichung in Kl. 5
9;?;I;K5;Teiler bestimmen;TB:teiler;alle Teiler einer dreistelligen Zahl;dreistellig;Punkte 9–11 zusammen 10
10;?;I;K5;Rechnen;RG:klammern;vier Terme mit Klammern und Potenzen;klein bis dreistellig;
11;?;III;K2;Sachaufgabe;TB:teiler;passende Brettbreiten für eine Wand ohne Längsschnitt;cm, dreistellig;Problemlösen
""")
A("G5-02", quelle=KA+"1468.pdf", titel="Klassenarbeit Gleichungen und Terme (2)", herausgeber="klassenarbeiten.de (Schule unbekannt)",
  art="Klassenarbeit/Schulaufgabe", nummer="unbekannt (Annahme: 2. SA, Lernbereich M5 3)", jahr=None, zeit_min=None,
  punkte_gesamt=42, lizenz=LIZ_KA, bundesland="unbekannt", passung="Gym Kl. 5, Bundesland unbekannt", **KL5, zeilen="""
1;3;I;K5;Umschreiben;POT:quadrat;Zahlen als Quadrat einer natürlichen Zahl schreiben;dreistellig;
2;4;I;K5;Gleichung lösen;GZ:umkehraufgabe;vier Einschritt-Gleichungen (alle vier Rechenarten);bis vierstellig;
3;3;I;K5;Zehnerpotenz;POT:zehner;große Zahlen mit Zehnerpotenz schreiben;Millionen;
4;3;II;K5;Potenz bilden;POT:schreibweise;Zahl als Potenz mit kleinster Basis;bis vierstellig;
5;4;II;K5;Geschickt rechnen;RG:verteilen;Distributivgesetz nutzen;zwei- bis vierstellig;
6;5;II;K3;Sachaufgabe;RG:sach;Pfand, Kisten, Wechselgeld mehrschrittig;Euro;mehrschrittig
7;7;I;K5;Rechnen;POT:berechnen;sieben Potenz-/Quadratterme;bis Tausender;
8;5;III;K2;Problemlösen;TB:primfaktoren;drei Alter aus einem Produkt mit Zwillingsbedingung;Produkt dreistellig;Knobelaufgabe
9;4;I;K6;Rechnen+Benennen;RG:termaufbau;Terme berechnen und Termart benennen;vierstellig;Fachbegriffe
10;4;III;K2;Sachaufgabe;POT:sach;fortgesetztes Verdoppeln, Gesamtpreis;Tausender;Zusatzaufgabe
""")
A("G5-03", quelle=KA+"1424.pdf", titel="Klassenarbeit Zahlenterme", herausgeber="klassenarbeiten.de (Schule unbekannt)",
  art="Klassenarbeit/Schulaufgabe", nummer="unbekannt (Annahme: 2./3. SA, M5 3 mit Wiederholung M5 1/4)", jahr=None, zeit_min=None,
  punkte_gesamt=36, lizenz=LIZ_KA, bundesland="unbekannt", passung="Gym Kl. 5, Bundesland unbekannt; Stoff passt zu LehrplanPLUS", **KL5, zeilen="""
1;5;II;K5;Rechnen;RG:klammern;mehrstufiger Term mit Klammern und negativen Zahlen;dreistellig;
2;3;I;K5;Primfaktorzerlegung;TB:primfaktoren;vierstellige Zahl zerlegen;vierstellig;
3;4;II;K5;Geschickt rechnen;RG:verteilen;Distributivgesetz mit negativen Zahlen;zweistellig;
4;5;II;K5;Rechnen;POT:negativ;Term mit Potenzen, Klammern, negativen Zahlen;klein;
5;3;II;K5;Rechnen;POT:negativ;Potenzen negativer Zahlen in verschachtelten Klammern;klein bis dreistellig;
6;5;II;K3;Sachaufgabe;GR:rechnen;Gewicht und Geld mit Einheitenwechsel, Gesamtansatz;t/kg/g, großer Geldbetrag;Gesamtansatz verlangt
7;3;I;K5;Runden;NAT:runden_regel;Größen in verschiedenen Einheiten runden;gemischte Einheiten;Runden von Größen
8;2;I;K5;Umrechnen;GR:kommaschreibweise;dm und cm in m;Dezimalzahlen;
9;4;II;K3;Sachaufgabe;PROP:einheit;Strecke pro Zeit, Minuten in Sekunden;Dezimalzahl, Minuten;Geschwindigkeit
10;2;II;K1;Begründen;RG:mal_ganz;Vorzeichen eines Produkts mit negativem Faktor (Ungleichung);ganze Zahlen;
""")
A("G5-04", quelle=KA+"1722.pdf", titel="Klassenarbeit Zahlenterme (ganze Zahlen)", herausgeber="klassenarbeiten.de (Schule unbekannt)",
  art="Klassenarbeit/Schulaufgabe", nummer="unbekannt (Annahme: 1./2. SA, M5 1/3)", jahr=None, zeit_min=None,
  punkte_gesamt=31, lizenz=LIZ_KA, bundesland="unbekannt", passung="Gym Kl. 5, Bundesland unbekannt; Punkte je Aufgabe unklar", **KL5, zeilen="""
1;?;II;K6;Erklären;RG:termaufbau;in Worten erklären, wie man die Termart bestimmt;keine Rechnung;verbal, ohne Beispiel
2a;?;II;K5;Gliedern;RG:termaufbau;verschachtelten Term gliedern;mehrstellig;Termbaum/Gliederung
2b;?;III;K1;Begründen;L:RG:Wie ändert sich der Termwert, wenn man alle Zahlen gleich verändert?;Wertänderung ohne Rechnung begründen;mehrstellig;
3;?;II;K1;Wahr/falsch + korrigieren;GZ:verstehen;drei Aussagen zu Gegenzahl, Zahlenmengen, Minus negativer Zahlen;klein;falsche Aussagen korrigieren
4;?;I;K4;Zahlengerade;GZ:betrag;Zahlen mit Betrags- und Ordnungsbedingung markieren;-10 bis 10;
5;?;II;K5;Gliedern;RG:termaufbau;Term gliedern und Art angeben, ohne zu rechnen;mehrstellig;
6;?;III;K2;Problemlösen;GZ:zahlengerade;zwei Zahlen mit festem Abstand, symmetrisch zu einer Mitte;klein;
7;?;II;K3;Sachaufgabe;GZ:sach;Höhenänderungen eines Flugzeugs, Differenz zum Start;Tausender m;Rechnung verlangt
""")
A("G5-05", quelle=KA+"861.pdf", titel="Klassenarbeit Umfang, Fläche, Volumen", herausgeber="klassenarbeiten.de (Schule unbekannt)",
  art="Klassenarbeit/Schulaufgabe", nummer="unbekannt (Annahme: 4. SA, M5 4)", jahr=None, zeit_min=None,
  punkte_gesamt=47, lizenz=LIZ_KA, bundesland="unbekannt", passung="Gym Kl. 5, nicht Bayern-konform (Volumen ist in Bayern Kl. 6)", **KL5, zeilen="""
1;6;II;K4;Zeichnen;WI:drehungen;Wegskizze mit Drehungen und Maßstab zeichnen;60–120 m auf cm;Winkel + Maßstab kombiniert
2;3;II;K4;Zeichnen;L:KB:Schrägbild eines Quaders zeichnen (Kl. 5);zwei verschiedene Schrägbilder eines Quaders;cm;Zeichenaufgabe
3;6;II;K4;Zeichnen;L:KB:Netz eines Quaders zeichnen (Kl. 5);Netz desselben Quaders;cm;Zeichenaufgabe
4;3;I;K5;Umrechnen;FL:einheiten;sechs Flächenangaben umrechnen;bis a;
5;4;II;K5;Umrechnen;FL:kommaschreibweise;Kette gleicher Flächenangaben ergänzen;ha bis cm²;
6;3;I;K5;Tabelle;FL:rechteck;Rechteck-Tabelle (Länge, Breite, Umfang, Fläche);m/cm;
7;4;II;K3;Sachaufgabe;FL:sachaufgaben;Farbbedarf für mehrere Türen;unter 20 m²;
8;6;II;K5;Rechnen;KB:oberflaeche;Oberfläche und Volumen eines Quaders mit gemischten Einheiten;Bruchteile von m²/m³;Volumen = Kl. 6 in Bayern
9;2;I;K5;Umrechnen;VOL:einheiten;Volumeneinheiten umrechnen;bis 10^6 mm³;Kl.-6-Stoff in Bayern
10;2;I;K5;Rechnen;POT:quadrat;Quadratzahlen zweistelliger Zahlen;bis ca. 600;
11;2;II;K1;Begründen;KB:verstehen;ist jeder Quader ein Würfel?;–;
12;6;II;K1;Begründen;KB:verstehen;ist jeder Würfel ein Quader?;–;Punkte auffällig hoch
""")
A("G5-06", quelle=KA+"801.pdf", titel="Klassenarbeit Flächenmaße", herausgeber="klassenarbeiten.de (Schule unbekannt)",
  art="Kurzarbeit/Stegreifaufgabe (Umfang 11 P)", nummer="unbekannt (Annahme: vor 4. SA, M5 4)", jahr=None, zeit_min=None,
  punkte_gesamt=11, lizenz=LIZ_KA, bundesland="unbekannt", passung="Gym Kl. 5, Bundesland unbekannt", **KL5, zeilen="""
1;3;I;K5;Umrechnen;FL:einheiten;drei Flächenangaben in nächstkleinere Einheit;gemischt;
2;3;I;K5;Umrechnen;FL:einheiten;drei Flächenangaben in nächstgrößere Einheit;gemischt;
3;5;II;K3;Sachaufgabe;FL:sachaufgaben;Flächen zweier Plakate vergleichen;cm/m;
""")
A("G5-07", quelle=KA+"301.pdf", titel="Klassenarbeit Größen und Maßeinheiten", herausgeber="klassenarbeiten.de (Schule unbekannt)",
  art="Klassenarbeit/Schulaufgabe", nummer="unbekannt (Annahme: 3./4. SA, M5 4)", jahr=None, zeit_min=None,
  punkte_gesamt=40, lizenz=LIZ_KA, bundesland="vermutlich Hessen (Ortsnamen; Annahme)", passung="Gym Kl. 5, wohl nicht Bayern; Punkte unklar", **KL5, zeilen="""
1;?;I;K5;Umrechnen;GR:laenge;zehn Umrechnungen (Länge, Masse, Geld, Zeit, Fläche);gemischt;
2;?;II;K5;Vergleichen;GR:kommaschreibweise;Größen in verschiedenen Einheiten vergleichen;mit Brüchen/Dezimalzahlen;Brüche = Kl. 6 in Bayern
3;?;II;K3;Maßstab;GR:massstab;reale Strecke in Kartenlänge;km -> cm;
4;?;I;K5;Tabelle;GR:zeit;Zeitpunkt/Zeitspanne-Tabelle ergänzen;Uhrzeiten;
5a;?;I;K4;Zeichnen;GB:koordinaten;zehn Punkte eintragen;klein;
5b;?;II;K5;Rechnen;FL:zerlegen;Umfang und Fläche der Figur aus 5a;klein;Figur aus Koordinaten
6;?;I;K3;Sachaufgabe;FL:sachaufgaben;Zaunlänge um quadratische Wiese;m;Umfang
7;?;I;K5;Tabelle;FL:rechteck;Quadrat-Tabelle ergänzen;klein;
8;?;II;K3;Maßstab;GR:massstab;Kartenstrecke in reale Entfernung;großer Maßstab;
9;?;II;K5;Tabelle;FL:rechteck;Rechteck-Tabelle mit gemischten Einheiten;gemischt;
""")
A("G5-08", quelle=KA+"1218.pdf", titel="Klassenarbeit Koordinatensystem", herausgeber="klassenarbeiten.de (Schule unbekannt)",
  art="Klassenarbeit/Schulaufgabe", nummer="unbekannt (Annahme: 1./2. SA, M5 2)", jahr=None, zeit_min=None,
  punkte_gesamt=36, lizenz=LIZ_KA, bundesland="unbekannt", passung="Gym Kl. 5, Bundesland unbekannt", **KL5, zeilen="""
1;9;I;K4;Zeichnen;GB:lagebeziehungen;Gerade und Strecke zeichnen, Lage beschreiben;–;
2;4;II;K4;Konstruieren;OL:verknuepfen;Senkrechte, Parallele, Abstand, Punkte gleich weit von zwei Geraden;Koordinaten klein;mehrschrittig
3;6;II;K4;Zeichnen;L:KB:Netz eines Quaders zeichnen (Kl. 5);Quadernetz mit gegebenen Kanten;cm;
4;8;I;K4;Zeichnen;GB:koordinaten;Koordinatensystem anlegen, Punkte eintragen;klein;
5;6;II;K4;Konstruieren;GB:lagebeziehungen;Parallelität, Orthogonalität, Abstände Punkt–Gerade;klein;
6;3;III;K6;Offen;OL:kreislinie;Geraden mit gleichem Abstand zu einem Punkt, entstehendes Bild beschreiben;–;führt zu Tangenten (Kl. 7)
""")
A("G5-09", quelle="https://klassenarbeiten.de/data/dynamic/pdf/1050.pdf", titel="Klassenarbeit Symmetrie und Spiegelung", herausgeber="klassenarbeiten.de (Schule unbekannt)",
  art="Klassenarbeit/Schulaufgabe", nummer="unbekannt", jahr=None, zeit_min=None,
  punkte_gesamt=33, lizenz=LIZ_KA, bundesland="unbekannt", passung="Gym Kl. 5, nicht Bayern-konform (Spiegelung ist in Bayern Kl. 7)", **KL5, zeilen="""
1;6;I;K4;Zeichnen;KON:symmetrie;alle Symmetrieachsen einzeichnen;–;Kl.-7-Stoff in Bayern
2;8;II;K4;Konstruieren;KON:achsenspiegelung;Figur zu achsensymmetrischer Figur ergänzen;Koordinaten klein;
3;6;I;K4;Spiegeln;KON:achsenspiegelung;Koordinaten ablesen, Rechteck spiegeln, Bildpunkt angeben;klein;
4;8;II;K4;Konstruieren;GB:lagebeziehungen;welche Gerade liegt einem Punkt am nächsten;klein;Abstand Punkt–Gerade
5;5;II;K4;Konstruieren;KON:achsenspiegelung;Dreieck an schräger Gerade spiegeln, Koordinaten angeben;klein;
""")
A("G5-10", quelle="https://www.nuernberg.de/imperia/md/sigena_gymnasium/dokumente/unterricht/mathe/hinweise-gwt_klasse-6-lp-plus.pdf",
  titel="Grundwissentest Beginn Kl. 6 (Stoff Kl. 5), Mustertest", herausgeber="Sigena-Gymnasium Nürnberg (Fachschaft Mathematik)",
  art="Grundwissentest (Mustertest, unverbindlich)", nummer="Beginn Kl. 6 – prüft ganzen Kl.-5-Stoff", jahr=None, zeit_min=25,
  punkte_gesamt=14, lizenz=LIZ_SCHULE, bundesland="Bayern", passung="Bayern, LehrplanPLUS Gym", klasse=5, frei=True,
  hilfsmittel="nicht angegeben (Annahme: ohne Taschenrechner)", zeilen="""
1;2;II;K4;Zahlengerade;GZ:zahlengerade;ganze Zahlen mit höchstens gegebenem Abstand zu einer Zahl;klein;
2;2;I;K5;Rechnen;RG:punkt_strich;Term mit Geteilt, Mal und Plus;vierstellig;
3;2;II;K5;Rechnen;RG:mal_ganz;Produkt zweier Klammern mit negativen Zahlen;dreistellig;
4;2;II;K6;Frage formulieren;GE:aufstellen;Frage zu gegebener Gleichung erfinden und lösen;zweistellig;umgekehrte Richtung
5;2;II;K5;Zählen;KOMB:zaehlprinzip;Auswahl verschiedener Eissorten;klein;Reihenfolge ggf. mehrdeutig
6;2;II;K5;Rechnen;FL:rechteck;Seite und Fläche aus Umfang, Einheiten mischen;m/dm;
7;2;II;K6;Rechengeschichte;L:GR:Rechengeschichte zu einer Größenrechnung erfinden;Sachaufgabe zu einer Division von Größen erfinden;Euro;Text produzieren
""")

# ---------------------------------------------------------------- Klasse 8: Kl.-8-Stoff
A("G8-01", quelle="https://buch-ka.de/media/44/d1/35/1648766582/9kkzw5kc3ryzwftcmvuzg9iagp4cmvmcjagmzk3iaowmdawmdawmdawidy1ntm1igygcjawmdawmdawmtugmdawmdagbiakmdawmdawmda5msawmdawmcbuiaowmdawmdawmji4idawmdawig4gcjawmdawmde2mjigmdawmdagbiakmdawmtgvtvt6qf7zeb.pdf",
  titel="STARK Schulaufgaben Gym Mathe 8 Bayern – Stegreifaufgabe 2 (Leseprobe)", herausgeber="STARK Verlag",
  art="Stegreifaufgabe (Verlagsmuster)", nummer="Zeitraum 1. SA (Funktion und Term)", jahr=None, zeit_min=18, punkte_gesamt=23,
  lizenz=LIZ_STARK, bundesland="Bayern", passung="Bayern, LehrplanPLUS Gym 8", klasse=8, frei=True, hilfsmittel="nicht angegeben", zeilen="""
1a;3;I;K6;Definieren;FG:eindeutig;Funktionsbegriff nennen und definieren;–;Wissensfrage
1b;4;II;K1;Begründen;FG:eindeutig;prüfen, ob eine Zuordnung Funktion ist, mit Gegenbeispiel;–;
2a;3;II;K4;Zuordnen;FLIN:graph_ablesen;drei Graphen den Termen zuordnen und erklären;klein;auch Hyperbel dabei
2b;3;I;K5;Definitionsmenge;FG:mengen;maximale Definitionsmengen dreier Funktionen;klein;auch Wurzel (Kl. 9)
2c;5;II;K5;Rechnen;FG:nullstellen;Achsenschnittpunkte zweier Graphen;klein;
2d;4;II;K5;Rechnen;FG:punkt_graph;liegt ein Punkt über oder unter dem Graphen;klein;
2e;1;II;K5;Ungleichung;UNG:grafisch;wo ist die Funktion nicht negativ;klein;
""")
A("G8-02", quelle="https://buch-ka.de/media/44/d1/35/1648766582/9kkzw5kc3ryzwftcmvuzg9iagp4cmvmcjagmzk3iaowmdawmdawmdawidy1ntm1igygcjawmdawmdawmtugmdawmdagbiakmdawmdawmda5msawmdawmcbuiaowmdawmdawmji4idawmdawig4gcjawmdawmde2mjigmdawmdagbiakmdawmtgvtvt6qf7zeb.pdf",
  titel="STARK Schulaufgaben Gym Mathe 8 Bayern – Schulaufgabe 1 (Leseprobe)", herausgeber="STARK Verlag",
  art="Schulaufgabe (Verlagsmuster)", nummer="1. SA (Funktion und Term, lineare Funktionen)", jahr=None, zeit_min=45, punkte_gesamt=38,
  lizenz=LIZ_STARK, bundesland="Bayern", passung="Bayern, LehrplanPLUS Gym 8", klasse=8, frei=True, hilfsmittel="nicht angegeben", zeilen="""
1a;4;II;K3;Modellieren;FLIN:deuten;Funktionsterm für eine Sachsituation, D und W angeben;klein;Sachkontext
1b;3;I;K6;Benennen;FLIN:proportional;Art der Zuordnung nennen und am Term erkennen;–;
1c;3;II;K5;Gleichung lösen;FG:stelle;Zeitpunkt für vorgegebenen Funktionswert;klein;
1d;3;II;K1;Begründen;FG:eindeutig;warum eine umgekehrte Zuordnung keine Funktion ist;–;
2a;2;I;K4;Zeichnen;FLIN:graph_ablesen;Gerade durch zwei Punkte zeichnen;Dezimalkoordinaten;
2b;7;II;K5;Rechnen;FLIN:zwei_punkte;Geradengleichung aus zwei Punkten;Dezimalzahlen;7 Punkte
2c;3;I;K5;Rechnen;FG:nullstellen;Nullstelle berechnen;Bruch;
2d;7;II;K5;Rechnen;FLIN:schnittpunkte;zweite Gerade zeichnen, Schnittpunkt berechnen;klein;7 Punkte
3a;4;II;K3;Modellieren;FLIN:deuten;Kostenfunktion aufstellen, vorwärts und rückwärts rechnen;Euro;
3b;2;II;K6;Deuten;FLIN:deuten;Bedeutung von Steigung und Achsenabschnitt im Kontext;–;
""")
A("G8-03", quelle=KA+"3793.pdf", titel="Mathematikschulaufgabe Proportionalität, lineare Funktionen", herausgeber="klassenarbeiten.de (Schule unbekannt)",
  art="Schulaufgabe", nummer="unbekannt (Annahme: 1./2. SA)", jahr=None, zeit_min=None, punkte_gesamt=None,
  lizenz=LIZ_KA, bundesland="Bayern (laut Lösungskopf)", passung="Bayern, Klasse nicht angegeben (Annahme Kl. 8)", klasse=8, frei=True,
  hilfsmittel="nicht angegeben", zeilen="""
1;?;I;K6;Wahr/falsch;FLIN:proportional;sieben Aussagen zu Proportionalität, Graph, D, Nullstelle, linearer Funktion;–;Wissensquiz
2a;?;I;K6;Benennen;IND:erkennen;Zusammenhang Zeit–Geschwindigkeit benennen;–;
2b;?;II;K5;Tabelle;IND:produkt;Strecke bestimmen, Tabelle ergänzen;m/s, s;
2c;?;II;K1;Beurteilen;IND:graph;Behauptung zur Graphenform prüfen;–;
3a;?;II;K5;Rechnen;FLIN:zwei_punkte;Geradengleichung durch zwei Punkte;klein, auch negativ;Steigung als Bruch
3b;?;II;K5;Rechnen;FLIN:lage;Parallele durch gegebenen Punkt;klein;
""")
A("G8-04", quelle=KA+"3801.pdf", titel="Klassenarbeit Bruchterme", herausgeber="klassenarbeiten.de (Schule unbekannt)",
  art="Klassenarbeit", nummer="Dezember", jahr=None, zeit_min=None, punkte_gesamt=None,
  lizenz=LIZ_KA, bundesland="Berlin", passung="Gym Kl. 8, nicht Bayern (Berlin) – Stoff passt zu M8 4", klasse=8, frei=True,
  hilfsmittel="nicht angegeben", zeilen="""
1a;?;II;K5;Umformen;BT:multiplizieren;Division zweier Bruchterme mit Faktorisieren;klein;
1b;?;III;K5;Umformen;BT:addieren;Differenz von Brüchen durch Klammerterm, binomische Formel;klein;binomische Formel nötig
1c;?;II;K5;Umformen;BT:addieren;zwei Bruchterme mit binomischen Nennern subtrahieren;klein;
2a;?;II;K5;Bruchgleichung;BG:hauptnenner;Gleichung mit zwei Brüchen;klein;
2b;?;II;K5;Bruchgleichung;BG:hauptnenner;Bruch minus Zahl gleich Bruch;klein;
2c;?;III;K5;Bruchgleichung;BG:hauptnenner;Hauptnenner nach Faktorisieren;klein;
2d;?;III;K5;Bruchgleichung;BG:scheinloesung;Lösung fällt aus D heraus, leere Menge;klein;
3;?;III;K3;Textaufgabe;L:BG:Bruchgleichung aus einem Text über Zähler und Nenner aufstellen;Bruch so verändern, dass Wert gleich bleibt, mit Probe;zweistellig;
""")
A("G8-05", quelle=KA+"3806.pdf", titel="4. Mathematikarbeit 8. Klasse (G8)", herausgeber="klassenarbeiten.de (Schule unbekannt)",
  art="Klassenarbeit (4. Arbeit)", nummer="4. Arbeit", jahr=None, zeit_min=None, punkte_gesamt=None,
  lizenz=LIZ_KA, bundesland="unbekannt (G8)", passung="Kl. 8 G8 – Wurzeln/reelle Zahlen sind in LehrplanPLUS Kl. 9", klasse=8, frei=True,
  hilfsmittel="ohne Taschenrechner", zeilen="""
1a;?;II;K5;Bruchgleichung;BG:hauptnenner;D und Lösungsmenge;klein;
1b;?;II;K5;Bruchgleichung;BG:hauptnenner;Nenner mit 3. binomischer Formel;klein;
1c;?;III;K5;Bruchgleichung;BG:hauptnenner;mit x²-Termen, die wegfallen;klein;
2;?;II;K5;Volumen;PZY:prisma_volumen;zusammengesetztes Prisma;m³;
3;?;I;K5;Wurzel;X:teilweise Wurzelziehen (LehrplanPLUS Kl. 9);drei Radikanden teilweise radizieren;bis vierstellig;
4a-d,f,g;?;II;K5;Wurzel;X:Wurzelgesetze (LehrplanPLUS Kl. 9);sechs Wurzelterme vereinfachen;klein;
4e;?;II;K5;Umformen;PGZ:terme_vereinfachen;Quotient von Potenztermen;klein;
4h;?;II;K5;Umformen;X:binomische Formel mit Wurzeln (Kl. 9);Quadrat einer Summe mit Wurzeln;klein;
5;?;II;K1;Wahr/falsch;X:reelle/irrationale Zahlen (Kl. 9);vier Aussagen zu Zahlbereichen und Wurzeln begründen;–;
6;?;III;K2;Beispiel finden;X:irrationale Zahlen (Kl. 9);zwei irrationale Zahlen mit rationalem Produkt;–;
Z;?;II;K5;Definitionsmenge;BT:definitionsmenge;maximale D eines Bruchs mit Wurzel im Zähler;klein;Zusatz, Wurzel
""")
A("G8-06", quelle="https://www.katharinengymnasium.de/file/212/download", titel="Mathematiktest 8. Jahrgangsstufe (Juni 2012)",
  herausgeber="Katharinen-Gymnasium Ingolstadt", art="schulinterner Jahrgangstest (Ende Kl. 8)", nummer="Ende Schuljahr (Juni)", jahr=2012,
  zeit_min=40, punkte_gesamt=31, lizenz=LIZ_SCHULE, bundesland="Bayern", passung="Bayern, G8-Lehrplan (Punkte ca.)", klasse=8, frei=True,
  hilfsmittel="ohne Taschenrechner", zeilen="""
1;2;II;K1;Begründen;IND:unterscheiden;direkt oder indirekt proportional aus Wertetabelle;klein, auch negativ;
2;2;III;K1;Konstruieren+Begründen;LGS:loesbarkeit;zweite Gleichung so wählen, dass LGS unlösbar ist;klein;offene Aufgabe
3;4;II;K5;Umformen;PGZ:terme_vereinfachen;zwei Terme mit Potenzen, Brüchen, negativen Exponenten;klein;
4;2;II;K3;Gleichung aufstellen;L:BG:Bruchgleichung aus einem Text über Zähler und Nenner aufstellen;Gleichung zu einer Bruch-Textaufgabe, nicht lösen;zweistellig;nur aufstellen
5;4;II;K4;Zeichnen;FLIN:schnittpunkte;zwei Geraden zeichnen, eingeschlossene Fläche mit y-Achse;klein;Fläche zwischen Geraden
6;2;III;K2;Beispiel angeben;FGB:asymptoten;Funktionsterm zu vorgegebenen Asymptoten angeben;klein;Umkehrung der Etappe
7;4;II;K5;D + Kürzen;BT:kuerzen;Definitionsmenge und Kürzen eines Bruchterms;klein;
8;4;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen, D angeben;klein;
9a;2;II;K5;Zählen;KOMB:bedingungen;Anordnungen mit Randbedingung;7 Personen;Kl.-5-Thema in Kl. 8
9b;2;III;K5;Wahrscheinlichkeit;STO:laplace;dreistellige Würfelzahl mit zwei Bedingungen;216 Ergebnisse;
10;3;III;K2;Term aufstellen;KRB:zusammengesetzt;Restfläche nach Ausschneiden zweier Kreise als Term;Variable;
""")
A("G8-07", quelle="https://katharinengymnasium.de/file/213/download", titel="Mathematiktest 8. Jahrgangsstufe (Juli 2013, A)",
  herausgeber="Katharinen-Gymnasium Ingolstadt", art="schulinterner Jahrgangstest (Ende Kl. 8)", nummer="Ende Schuljahr (Juli)", jahr=2013,
  zeit_min=40, punkte_gesamt=27, lizenz=LIZ_SCHULE, bundesland="Bayern", passung="Bayern, G8-Lehrplan", klasse=8, frei=True,
  hilfsmittel="ohne Taschenrechner", zeilen="""
1;2;I;K5;Definitionsmenge;BT:definitionsmenge;nicht erlaubte Werte eines Bruchterms;klein;
2;2;II;K5;LGS lösen;LGS:verfahren;LGS mit zwei Unbekannten, eine Dezimalzahl;klein;
3;2;II;K5;Umformen;BT:kuerzen;Term faktorisieren und kürzen;klein;
4a;2;I;K4;Zeichnen;FLIN:graph_ablesen;Gerade mit negativer Steigung zeichnen;klein;
4b;2;II;K4;Spiegeln;L:FLIN:Gerade an einer Achse spiegeln und Gleichung angeben;Spiegelgerade an x-Achse angeben;klein;
4c;2;II;K5;Rechnen;FLIN:lage;Parallele durch Punkt;klein;
4d;2;I;K5;Prüfen;FG:punkt_graph;Punkt über/unter/auf der Geraden;große Koordinaten;
5a;2;II;K6;Beschreiben;FGB:parameter;Graph aus Grundfunktion durch Verschieben/Strecken;klein;Strecken
5b;2;I;K5;Asymptoten;FGB:asymptoten;alle Asymptoten angeben;klein;
6;2;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
7a;2;III;K2;Wahrscheinlichkeit;STO:laplace;Wahrscheinlichkeit in einer quadratischen Aufstellung;25 Personen;Problemlösen
7b;2;II;K5;Zählen;L:KOMB:Auswahl ohne Reihenfolge (Kombinationen);3 aus 8 ohne Reihenfolge;8 Personen;
8;3;III;K3;Sachaufgabe;KRB:verstehen;Weidefläche bei längerem Seil vergleichen;m;
""")
A("G8-08", quelle="https://www.nuernberg.de/imperia/md/sigena_gymnasium/dokumente/unterricht/mathe/info_gwt_9_homepage_ab_2024.pdf",
  titel="Grundwissentest Beginn Kl. 9 (Stoff bis Kl. 8), Mustertest", herausgeber="Sigena-Gymnasium Nürnberg (Fachschaft Mathematik)",
  art="Grundwissentest (Mustertest)", nummer="Beginn Kl. 9 – prüft Kl.-8-Stoff", jahr=2024, zeit_min=40, punkte_gesamt=18,
  lizenz=LIZ_SCHULE, bundesland="Bayern", passung="Bayern, LehrplanPLUS Gym", klasse=8, frei=True, hilfsmittel="ohne Taschenrechner", zeilen="""
1;2;I;K5;Umformen;TU:ausmultiplizieren;zwei Produkt-/Summenterme vereinfachen;klein;
2;2;I;K4;Ablesen;FG:graph_lesen;alle Stellen mit vorgegebenem Funktionswert am Graphen;klein;Näherungswerte
3;2;II;K5;Gleichung;LG:beide_seiten;lineare Gleichung mit Brüchen und Dezimalzahlen;klein;
4;2;II;K5;Rechnen;FLIN:lage;Parallele durch Punkt, Achsenschnittpunkte;klein;
5;2;II;K5;LGS lösen;LGS:verfahren;LGS lösen;klein;
6;2;II;K4;Skizzieren;FGB:parameter;Graph einer verschobenen Hyperbel skizzieren, D angeben;klein;Skizze
7;2;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung mit x im Nenner;klein;
8;2;II;K6;Erklären;STO:laplace;Weg zur Pasch-Wahrscheinlichkeit in Fachsprache;–;Fachsprache verlangt
9;2;II;K5;Schätzen;PZY:zylinder_volumen;Zylindervolumen mit gemischten Einheiten abschätzen;dm/cm;
""")
A("G8-09", quelle="https://www.nuernberg.de/imperia/md/sigena_gymnasium/dokumente/unterricht/mathe/m9_themen_einstiegstest.pdf",
  titel="Einstiegstest Beginn Kl. 9 – Beispiel 1", herausgeber="Sigena-Gymnasium Nürnberg (Fachschaft Mathematik)",
  art="schulinterner Einstiegstest (Beispiel)", nummer="Beginn Kl. 9 – prüft Kl.-8-Stoff", jahr=None, zeit_min=35, punkte_gesamt=15,
  lizenz=LIZ_SCHULE, bundesland="Bayern", passung="Bayern, LehrplanPLUS Gym", klasse=8, frei=True, hilfsmittel="ohne Taschenrechner", zeilen="""
1a;2;I;K5;Umformen;TU:zusammenfassen;Term vereinfachen;klein;
1b;1;II;K6;Deuten;TA:deuten;erklären, warum ein Term mit Prozentfaktor die Summe beschreibt;Euro;
2a;2;II;K5;Gleichung;LG:beide_seiten;Gleichung lösen;klein;
2b;1;I;K5;Umstellen;FO:ein_schritt;Formel nach einer Größe auflösen;–;
3a;1;I;K4;Zeichnen;FLIN:graph_ablesen;Gerade zeichnen;klein;
3b;2;II;K5;Asymptoten;FGB:asymptoten;Asymptoten angeben, y-Wert eines Graphpunkts;klein;
4;2;III;K6;Ereignis beschreiben;STO:begriffe;Ereignis zu einer gegebenen Rechnung beschreiben (Glücksrad zweimal);10 Felder;Umkehrung
5;2;II;K5;LGS lösen;LGS:verfahren;LGS lösen;klein;
6;2;II;K5;Schätzen;PZY:zylinder_volumen;Zylindervolumen schätzen (π≈3);dm/cm;
""")
A("G8-10", quelle="https://www.nuernberg.de/imperia/md/sigena_gymnasium/dokumente/unterricht/mathe/m9_themen_einstiegstest.pdf",
  titel="Einstiegstest Beginn Kl. 9 – Beispiel 2", herausgeber="Sigena-Gymnasium Nürnberg (Fachschaft Mathematik)",
  art="schulinterner Einstiegstest (Beispiel)", nummer="Beginn Kl. 9 – prüft Kl.-8-Stoff", jahr=None, zeit_min=35, punkte_gesamt=15,
  lizenz=LIZ_SCHULE, bundesland="Bayern", passung="Bayern, LehrplanPLUS Gym", klasse=8, frei=True, hilfsmittel="ohne Taschenrechner", zeilen="""
1a;2;I;K5;Umformen;TU:zusammenfassen;Term vereinfachen;klein;
1b;1;II;K5;Faktorisieren;TU:binomisch;mit binomischer Formel faktorisieren;klein;
2a;2;III;K1;Begründen;LG:sonderfaelle;Lücke so füllen, dass Gleichung allgemeingültig ist, mit Begründung;klein;
2b;1;I;K5;Gleichung;LG:beide_seiten;Gleichung lösen;klein;
3a;2;III;K2;Rechnen;FG:punkt_graph;senkrechter Abstand eines Punkts zur Geraden durch zwei Punkte;klein;Gerade erst aufstellen
3b;1;II;K4;Ablesen;FGB:parameter;Parameter am Graphen ablesen;klein;
4;2;II;K6;Erklären;STO:laplace;Weg zur Wahrscheinlichkeit „Augensumme ungerade“ beschreiben;–;Fachsprache
5;2;II;K5;LGS lösen;LGS:verfahren;LGS lösen;klein;
6;2;II;K5;Rechnen;KRB:zusammengesetzt;Umfang einer Figur mit Halbkreis;zwei Nachkommastellen;
""")
# BMT10: nur Aufgaben mit Kl.-8-Stoff
BMT10 = dict(art="BMT10 – nur Aufgaben mit Kl.-8-Stoff aufgenommen", herausgeber="ISB Bayern", klasse=8,
             nummer="Test zu Beginn Kl. 10 (prüft Kl. 8–9)", zeit_min=40, punkte_gesamt=21,
             hilfsmittel="kein Taschenrechner, keine Formelsammlung", frei=True, lizenz=LIZ_ISB, bundesland="Bayern",
             passung="Bayern; Kl.-10-Test, Auszug")
A("G8-11", quelle=ISB+"2016/bmt10_2016_aufgaben_gruppe_a.pdf", titel="BMT10 2016 Gruppe A (Auszug)", jahr=2016, **BMT10, zeilen="""
2a;1;I;K5;Formel;KRB:umfang;Radius aus Umfang als Formel;~0,5 m;
2b;2;II;K3;Schätzen;PZY:zylinder_volumen;Volumen eines Baumstamms grob schätzen;m³;
5a;1;I;K1;Begründen;BG:definitionsmenge;Wert gehört nicht zur Definitionsmenge;einstellig;
5b;2;II;K5;Bruchgleichung;BG:hauptnenner;Bruchgleichung lösen;klein;
""")
A("G8-12", quelle=ISB+"2019/bmt10_2019_aufgaben_gruppe_a.pdf", titel="BMT10 2019 Gruppe A (Auszug)", jahr=2019, **BMT10, zeilen="""
3a;1;II;K2;Beispiel angeben;FGB:asymptoten;Funktionsterm mit vorgegebener Polstelle;klein;Umkehrung
4a;1;I;K4;Ablesen;FLIN:graph_ablesen;Wert am Umrechnungsgraphen ablesen;°F/°C;
4b;1;II;K4;Ablesen;FLIN:schnittpunkte;Stelle mit gleicher Maßzahl in beiden Skalen;negativ;
4c;2;II;K5;Umstellen;FO:zwei_schritte;Umrechnungsformel umstellen, Steigung angeben;Brüche;
4d;1;III;K1;Begründen;FLIN:deuten;welcher Anstieg größer ist, begründen;klein;
""")
A("G8-13", quelle=ISB+"2022/bmt10_2022_aufgaben_gruppe_a.pdf", titel="BMT10 2022 Gruppe A (Auszug)", jahr=2022, **BMT10, zeilen="""
1b;1;I;K5;Bruchgleichung;BG:ein_bruch;einfache Bruchgleichung;klein;
2a;1;I;K5;Nullstelle;FGB:achsenpunkte;Nullstelle durch Rechnung nachweisen;klein;
2b;2;II;K6;Beschreiben;FGB:parameter;Verschiebung der Hyperbel beschreiben;klein;
6a;1;I;K5;Umstellen;FO:geometrie;Dreieckshöhe aus Fläche und Grundseite;cm;
7;2;III;K1;Zeigen;KRB:zusammengesetzt;Halbkreisflächen vergleichen;symbolisch;braucht Pythagoras (Kl. 9)
""")

# ---------------------------------------------------------------- Klasse 8: BMT8 (Stoff Kl. 5–7)
def BMT(jahr, gruppe, datei, zeilen, **extra):
    m = dict(BMT_META); m.update(extra)
    A(f"G8-B{jahr}", quelle=ISB+datei, titel=f"BMT8 {jahr} Gruppe {gruppe}", jahr=jahr, zeilen=zeilen, **m)

BMT(2025, "A", "2025/BMT8_2025_Aufgaben_Gruppe_A.pdf", """
1a;1;I;K5;Rechnen;BRR:gemischt;Termwert berechnen;klein;
1b;1;I;K5;Rechnen;BRR:gemischt;Termwert berechnen;klein;
2a;2;II;K5;Volumen;VOL:zusammengesetzt;Volumen eines zusammengesetzten Körpers aus Schrägbild;cm³;
2b;1;II;K3;Auswahl;VOL:verstehen;Volumen eines Modells im Maßstab 1:10;–;Volumen skaliert mit k³
3;2;II;K5;Gleichung;L:LG:Ein Produkt ist null (Satz vom Nullprodukt);Gleichung mit Produkt bzw. Potenz lösen;klein;
4;2;II;K5;Umformen;TU:binomisch;Quadrat einer Summe vereinfachen;klein;
5;1;II;K1;Fehler finden;L:DK:Tabellenkalkulation – Formeln lesen und Fehler finden;Fehler in einer Mittelwert-Formel begründen;zweistellig;Tabellenkalkulation
6a;1;I;K4;Diagramm prüfen;DD:saeulendiagramm;Aussage am Diagramm prüfen;zweistellig;
6b;2;II;K5;Prozent;PZ:prozentsatz;Prozentangaben ergänzen;zweistellig;
6c;1;II;K1;Median;BOX:median;Median bestimmen und begründen;klein;
6d;1;III;K1;Begründen;PZ:verstehen;Prozentanteil vs. absolute Anzahl;–;
7a;1;I;K4;Koordinaten;GB:vierecke;fehlenden Parallelogrammpunkt angeben;klein;
7b;1;II;K5;Fläche;FV:parallelogramm;Fläche aus Koordinaten;klein;
7c;1;III;K2;Offen;FV:verstehen;Punkt mit gleicher Dreiecksfläche finden;klein;offen
8a;1;II;K1;Begründen;KST:gleichschenklig;gleichschenklig über Kreisradien begründen;–;
8b;2;III;K1;Beweisen;WS:beweisen;Winkelbeziehung 2:1 beweisen;–;Beweis
""")
BMT(2024, "A", "2024/BMT8_2024_Aufgaben_Gruppe_A.pdf", """
1a;2;II;K5;Gleichung;LG:klammern;lineare Gleichung mit Klammern;klein;
1b;1;III;K2;Umkehren;L:LG:Zahl in einer Gleichung so wählen, dass eine vorgegebene Lösung entsteht;Zahl ersetzen, damit vorgegebene Lösung gilt;klein;
2;2;II;K5;Umformen;TU:binomisch;ausmultiplizieren und vereinfachen;klein;
3a;1;I;K4;Diagramm;DD:saeulendiagramm;Säule ergänzen;Prozent;
3b;2;II;K1;Aussagen prüfen;DD:tabelle_auswerten;drei Aussagen ja/nein zum Diagramm;Prozent;
3c;2;II;K5;Prozent;PZ:grundwert;Grundwert aus Anteil;dreistellig;
4a;1;I;K5;Maßstab;GR:massstab;Kartenstrecke in Meter;km;
4b;1;II;K4;Konstruieren;KON:mittelsenkrechte;Punkt auf der Mittelsenkrechten konstruieren;–;
5a;2;II;K1;Begründen;KR:thales;Winkel über Thales und gleichseitiges Dreieck begründen;–;
5b;1;III;K1;Begründen;FV:verstehen;gleiche Dreiecksflächen begründen;–;
6a;1;II;K5;Rechnen;BRR:dezimal_mal;Dezimalprodukt aus bekanntem Produkt;klein;Kommaverschiebung
6b;1;II;K5;Quadratzahl;POT:quadrat;Quadratwurzel einer Quadratzahl;dreistellig;Wurzelzeichen (Kl. 9)
6c;1;II;K5;Tabellenkalkulation;L:TA:Tabellenkalkulation – Formel aufstellen/ergänzen;Formel in Tabellenkalkulation ergänzen;–;
7a;1;II;K5;Term aufstellen;TA:sachsituation;Umfangsterm einer Figur;Variable;
7b;2;III;K6;Erläutern;TU:binomisch;binomische Formel geometrisch erläutern;Variable;Darstellungswechsel
""")
BMT(2023, "A", "2023/bmt8_2023_aufgaben_gruppe_a.pdf", """
1a;1;I;K5;Umformen;TU:zusammenfassen;Term vereinfachen;klein;
1b;1;I;K5;Umformen;TU:ausmultiplizieren;Term vereinfachen;klein;
1c;1;I;K5;Umformen;TU:produkte;Term vereinfachen;klein;
2a;1;II;K3;Deuten;TA:deuten;Variable im Kontext deuten;–;
2b;2;II;K5;Gleichung;LG:klammern;Gleichung lösen;klein;
3a;1;I;K4;Symmetrie;KON:symmetrie;Symmetrieachsen einer Raute;–;
3b;1;II;K1;Gegenbeispiel;KST:vierecke;Gegenbeispiel zur Kongruenz von Vierecken;–;
4a;1;I;K3;Schätzen;GR:schaetzen;Größe schätzen;–;
4b;1;II;K5;Einheiten;GR:laenge;fremde Längeneinheiten in cm als Term;–;nicht-metrische Einheiten
4c;2;II;K5;Volumen;VOL:rueckwaerts;Quaderhöhe aus Volumen in Litern;Liter;
5a;1;I;K5;Anteil;BR:anteil_bestimmen;Anteil ergänzen;klein;
5b;1;I;K5;Median;BOX:median;Median;klein;
5c;1;II;K1;Auswahl;DK:mittelwert;Änderung des Mittelwerts;klein;
6;2;III;K2;Prozent;PGW:vermindert;99-%-Reduktion einer großen Zahl;Zehnerpotenzen;sehr große Zahlen
7a;1;I;K5;Fläche;FV:dreieck;Dreiecksfläche;klein;
7b;1;I;K4;Zeichnen;FV:dreieck;Höhe einzeichnen;–;
7c;2;III;K1;Begründen;FV:verstehen;maximale Höhe, rechtwinkliger Fall;–;
""")
BMT(2022, "A", "2022/bmt8_2022_aufgaben_gruppe_a.pdf", """
1a;1;I;K4;Konstruieren;KON:mittelsenkrechte;Mittelsenkrechte konstruieren;–;
1b;1;II;K6;Satz ergänzen;GB:lagebeziehungen;Satz zum Abstand Punkt–Gerade ergänzen;–;
1c;2;II;K4;Ortslinien;OL:verknuepfen;Punkte mit Abstand zu Gerade und Punkt;–;
2;2;II;K5;Gleichung;LG:beide_seiten;lineare Gleichung mit Brüchen;klein;
3;1;II;K5;Tabellenkalkulation;L:TA:Tabellenkalkulation – Formel aufstellen/ergänzen;Wert einer Tabellenkalkulationsformel;–;
4a;1;II;K6;Erklären;RG:verteilen;Rechenvorteil mit Distributivgesetz erklären;zweistellig;
4b;2;II;K5;Umformen;TU:ausmultiplizieren;Term vereinfachen;klein;
5a;1;I;K1;Aussage prüfen;DD:saeulendiagramm;Aussage zum Balkendiagramm (Prozent);Prozent;
5b;1;II;K5;Kreisdiagramm;DD:kreisdiagramm;Winkel im Kreisdiagramm;Grad;
5c;1;II;K5;Term;DK:mittel_tabelle;Term für gewichteten Mittelwert;klein;
5d;1;II;K5;Anteil;BR:ganzes_bestimmen;Gesamtzahl aus Anteil;dreistellig;
6a;1;I;K5;Umrechnen;GR:zeit;Stunden in Minuten;Dezimal;
6b;2;II;K5;Auswahl;VOL:einheiten;zwei gleiche Volumenangaben ankreuzen;gemischt;
7a;1;I;K5;Winkel;WS:stufen_wechsel;Winkel an Parallelen;Grad;
7b;1;I;K5;Fläche;FV:parallelogramm;Parallelogrammfläche;klein;
7c;2;III;K1;Begründen;FV:verstehen;Flächenformel über Zerlegung begründen;–;
""")
BMT(2021, "A", "2021/bmt8_2021_aufgaben_gruppe_a.pdf", """
1a;1;I;K5;Potenz;POT:negativ;Potenz mit Vorzeichen;klein;
1b;1;I;K5;Potenz;BRR:potenzen;Potenz mit Vorzeichen;klein;
2a;1;I;K5;Rechenanweisung;TA:termwert;Rechenanweisung ausführen;klein;
2b;2;II;K5;Term;TA:uebersetzen;Anweisung als Term, vereinfachen;Variable;
3;2;II;K5;Gleichung;LG:beide_seiten;Variable auf beiden Seiten, rationale Zahlen;klein;
4a;2;II;K5;Volumen;VOL:liter;Würfelvolumen in Liter;dm;
4b;1;II;K6;Deuten;TA:deuten;Teil eines Terms im Kontext deuten;–;
4c;1;III;K1;Begründen;VOL:verstehen;warum eine Näherung zu groß ist;–;
5;2;II;K3;Ankreuzen;PGW:argumente;zwei passende Prozent-Gleichungen aus acht;–;
6a;1;II;K1;Erklären;DD:irrefuehrend;irreführende Grafik erklären;–;
6b;2;III;K3;Schätzen;GR:schaetzen;Stapelhöhe schätzen, in km;große Zahlen;Fermi-Aufgabe
6c;1;III;K1;Auswahl;PGW:prozentsatz;Bruch zu Prozentanstieg wählen;–;Prozentpunkte vs. Prozent
7;1;I;K4;Boxplot;BOX:boxplot;Median im Boxplot;–;
8a;1;II;K1;Beweis ordnen;KR:beweis;Beweisschritte zum Thalessatz ordnen;–;
8b;2;III;K1;Beweisen;WS:beweisen;Innenwinkel zeigen;–;
""")
BMT(2019, "A", "2019/bmt8_2019_aufgaben_gruppe_a.pdf", """
1a;1;I;K5;Rechnen;BRR:dezimal_mal;Zahlterm mit Dezimalzahl;dreistellig;
1b;1;I;K5;Umformen;TU:zusammenfassen;Term vereinfachen;klein;
2;2;II;K5;Gleichung;LG:klammern;Gleichung mit Klammern über Q;klein;
3;2;II;K5;Zuordnen;DEZ:merkwerte;Bruch, Dezimalzahl, Prozent gleichwertig zuordnen;–;
4a;1;II;K3;Auswahl;PROP:sach;Fahrzeit auswählen;km;
4b;2;II;K4;Konstruieren;KR:umkreis_inkreis;Umkreismittelpunkt auf einer Karte;–;Sachkontext
5a;1;II;K1;Begründen;WS:innenwinkelsumme;existiert das Dreieck?;Grad;
5b;1;III;K6;Beschreiben;WS:figuren;Schnittwinkel bestimmen ohne Verlängern beschreiben;–;Methode beschreiben
6a;1;II;K6;Deuten;PZ:prozentsatz;Prozentterm deuten;–;
6b;1;I;K5;Prozent;PZ:prozentsatz;Prozentanteil;–;
6c;1;II;K1;Diagramm;DD:tabelle_auswerten;ist ein Anteil gestiegen?;–;
6d;1;III;K2;Beispiel;PZ:verstehen;Beispiel mit gleichem Anteil;–;offen
7a;2;III;K2;Formel;TA:muster;Diagonalenanzahl im n-Eck mit Skizze;Variable n;
7b;2;III;K1;Beweisen;L:TA:Mit Termen beweisen (gerade/ungerade, Teilbarkeit);Ganzzahligkeit mit gerade/ungerade beweisen;–;Beweis
8;2;III;K3;Schätzen;GR:schaetzen;Schriftgröße schätzen;–;
""")
BMT(2018, "A", "2018/bmt8_2018_aufgaben_gruppe_a.pdf", """
1a;1;II;K6;Deuten;TA:deuten;Summe im Kontext deuten;–;
1b;1;I;K5;Mittelwert;DK:mittelwert;Mittelwert;klein;
1c;2;II;K3;Volumen;VOL:liter;Regenmenge auf einer Fläche;Liter;
2a;2;II;K1;Winkelbeziehungen;WS:figuren;Winkelbeziehungen im gleichschenkligen Dreieck nennen;–;
2b;2;II;K5;Winkel;WS:figuren;Winkel berechnen;Grad;
3;1;II;K5;Prozent-Gleichung;PGW:mehrfach;Prozentänderungen zur Gleichung ergänzen;–;
4a;1;II;K1;Gegenbeispiel;FV:verstehen;Gegenbeispiel zu Fläche/Umfang zeichnen;–;
4b;1;II;K1;Gegenbeispiel;KST:kongruenzsatz;Gegenbeispiel zur Kongruenz zeichnen;–;
5a;2;I;K5;Termwerte;TA:termwert;Terme auswerten;klein;
5b;2;II;K5;Äquivalenz;TU:aequivalenz;Äquivalenz zeigen;–;
5c;1;III;K2;Beispiel;TU:aequivalenz;nicht äquivalente Terme mit gleichem Wert an einer Stelle;–;offen
6;2;III;K3;Beurteilen;GR:schaetzen;Schätzmethode beurteilen;–;
7a;1;II;K1;Prüfen;TB:teiler;Summe aufeinanderfolgender Zahlen prüfen;klein;
7b;2;III;K1;Beweisen;L:TA:Mit Termen beweisen (gerade/ungerade, Teilbarkeit);Teilbarkeit allgemein beweisen;–;Beweis
""")
BMT(2017, "A", "2017/bmt8_2017_aufgaben_gruppe_a.pdf", """
1a;1;I;K5;Gleichung;LG:beide_seiten;lineare Gleichung mit Dezimalzahlen;klein;
1b;2;II;K5;Umformen;TU:minusklammer;Term mit Klammern und Potenzen;klein;
2;2;III;K3;Schätzen;GR:schaetzen;Anzahl schätzen (Fermi);sehr groß;Fermi-Aufgabe
3;1;I;K5;Zehnerpotenz;ZP:gross_wissenschaftlich;Zahlwort als Produkt mit Zehnerpotenz;Millionen;
4a;1;I;K1;Ankreuzen;DD:tabelle_auswerten;Diagrammaussagen ankreuzen;Prozent;
4b;1;II;K1;Erklären;DD:irrefuehrend;Fehler einer Flächendarstellung erklären;–;
4c;1;II;K6;Erkennen;L:DD:Mehrfachnennungen in Umfragen erkennen;Mehrfachnennungen erkennen;Prozent;
4d;1;II;K5;Auswahl;PGW:mehrfach;prozentuale Gesamtzunahme;–;
5a;2;II;K4;Ortslinien;KR:umkehrung;Thaleskreis und Parallele als Ortslinien;cm;
5b;1;I;K5;Fläche;FV:dreieck;Dreiecksfläche;cm;
5c;1;II;K5;Gleichung;X:Satz des Pythagoras (LehrplanPLUS Kl. 9, Test noch G8);Gleichung mit Pythagoras aufstellen;cm;
6a;1;I;K5;Kürzen;BR:kuerzen;Brüche kürzen;klein;
6b;2;III;K1;Gegenbeispiel;DEZ:verstehen;Gegenbeispiel zu endlichen Dezimalbrüchen;–;
7a;1;I;K5;Zählen;KD:prisma;Kantenzahl eines Prismas;klein;
7b;1;II;K5;Prüfen;L:KD:Eulerscher Polyedersatz;Euler-Formel prüfen;klein;
7c;2;III;K1;Beweisen;L:KD:Eulerscher Polyedersatz;Euler-Formel für Prismen allgemein zeigen;Variable;Beweis
""")
BMT(2016, "B", "2016/bmt8_2016_aufgaben_gruppe_b.pdf", """
1a;1;II;K5;Anteil;BR:anteil_bestimmen;Flächenanteil im Raster als Bruch;klein;
1b;1;I;K4;Symmetrie;KON:symmetrie;Anzahl Symmetrieachsen;–;
2a;1;I;K5;Rechnen;BRR:gemischt;Zahlterm mit Dezimalzahl;klein;
2b;1;I;K5;Umformen;TU:zusammenfassen;Term mit Variable vereinfachen;klein;
3;2;II;K1;Begründen;WS:parallel_pruefen;sind zwei Geraden parallel? mit Rechnung;Grad;
4;2;II;K3;Schätzen;GR:rechnen;Zeit in Sekunden prüfen, Geschwindigkeit schätzen;km, s;
5a;1;II;K6;Erklären;TA:sachsituation;Lösungsansatz eines Schülers (Flächengleichung) erklären;–;
5b;1;II;K4;Markieren;TA:deuten;zweiten Ansatz in der Figur markieren;–;
5c;2;II;K5;Gleichung;X:quadratische Gleichung (LehrplanPLUS Kl. 9, Test noch G8);Gleichung über Q+ lösen;klein;
6a;2;II;K5;Prozent;PZ:prozentwert;Prozent vom Prozent;Mio t;
6b;2;III;K4;Konstruieren;GR:massstab;Rechteck gegebener Fläche maßstäblich auf Karte;km²;Flächenmaßstab
6c;1;II;K5;Zurück;PGW:zurueck;Ausgangswert vor Abnahme;klein;
6d;1;III;K1;Begründen;DK:mittel_tabelle;fehlende Info für gewichteten Mittelwert benennen;groß;
7;1;I;K1;Prüfen;TB:teiler;Zahl gleich Summe ihrer Teiler zeigen;klein;
8;2;III;K2;Konstruieren;FV:verstehen;flächengleiche gleichschenklige Dreiecke konstruieren;–;
""", art="Jahrgangsstufentest BMT8 (Grundwissen Kl. 5–7) – Gruppe B (A nicht gefunden)")
BMT(2015, "A", "2015/bmt8_2015_aufgaben_gruppe_a.pdf", """
1a;1;I;K5;Potenz;POT:berechnen;Potenzterm;klein;
1b;1;II;K5;Umformen;PGN:mal_gleiche_basis;Potenzterm mit Variablen;klein;
2;2;II;K5;Fläche;FV:zusammengesetzt;Vierecksfläche exakt;cm²;
3;2;III;K3;Schätzen;GR:massstab;Radweglänge auf Karte schätzen;km;
4a;1;I;K5;Primzahl;TB:primzahl;drei zweistellige Primzahlen;zweistellig;
4b;1;II;K1;Begründen;TB:primfaktoren;gleiche Produkte begründen;–;
4c;1;II;K1;Widerlegen;TB:primzahl;Behauptung widerlegen;–;
5;2;III;K3;Volumen;VOL:liter;Schneevolumen mit Prozentverlust;m³;mit Prozent
6a;1;I;K6;Formulieren;DD:tabelle_auswerten;Unterschied aus Tabelle formulieren;–;
6b;1;I;K5;Anteil;DD:relative_haeufigkeit;Anteil aus Tabelle;–;
6c;1;II;K5;Kreisdiagramm;DD:kreisdiagramm;Sektorwinkel;Grad;
6d;1;II;K4;Auswahl;DD:kreisdiagramm;passendes Kreisdiagramm;–;
7;1;II;K4;Netz;L:KB:Würfelnetz – Lage von Markierungen bestimmen;Pfeil im Würfelnetz ergänzen;–;Raumvorstellung
8;2;II;K5;Gleichung;LG:beide_seiten;Gleichung über Q+;klein;
9a;1;II;K1;Begründen;KR:thales;rechtwinklig mit Thales begründen;–;
9b;2;III;K1;Begründen;WS:beweisen;Winkelgleichheit begründen;–;
""")
BMT(2014, "B", "2014/bmt8_2014_aufgaben_gruppe_b.pdf", """
1a;1;I;K4;Ablesen;DD:saeulendiagramm;Wert aus kombiniertem Diagramm;Mio;
1b;2;II;K1;Ankreuzen;DD:tabelle_auswerten;mehrere Aussagen zum Diagramm;Mio;
1c;1;II;K5;Prozent;BRR:sach;Anteil von einem Anteil;Prozent;
1d;2;III;K2;Beschreiben;GR:schaetzen;Vorgehen beim Schätzen einer Menschenmenge;sehr groß;Hochrechnen
2;1;I;K5;Rechnen;BRR:gemischt;Bruchterm mit Division;klein;
3;1;II;K6;Erklären;DD:relative_haeufigkeit;relative Häufigkeit eines Buchstabens erklären;–;
4;1;II;K1;Gegenbeispiel;KST:kongruenzsatz;Gegenbeispiel zu Dreiecken mit gleicher Seite und Höhe;–;
5;2;III;K3;Volumen;VOL:rueckwaerts;Absinken des Wasserspiegels;m³, cm;
6a;1;I;K4;Konstruieren;KON:mittelsenkrechte;Mittelsenkrechten zweier Seiten;–;
6b;2;II;K1;Lückentext;KR:umkreis_inkreis;Umkreismittelpunkt begründen;–;
7;2;II;K5;Ausklammern;TU:ausklammern;Ausklammern ergänzen;Potenzen;
8;2;III;K3;Gleichung;LG:sach;Seitenlänge über Flächendifferenz bestimmen;cm;
9a;1;I;K5;Zählen;KOMB:zaehlprinzip;dreistellige Würfelzahlen zählen;Hunderte;
9b;2;III;K2;Zählen;KOMB:bedingungen;Zahlen mit mindestens zwei gleichen Ziffern;Dutzende;Fallunterscheidung
""", art="Jahrgangsstufentest BMT8 (Grundwissen Kl. 5–7) – Gruppe B (A nicht gefunden)")
BMT(2013, "A", "2013/bmt8_2013_aufgaben_gruppe_a.pdf", """
1;1;I;K5;Zehnerpotenz;ZP:zehnerpotenz;Faktor zwischen zwei Zahlen;Tausender;
2;2;II;K1;Begründen;FL:einheiten;Flächeneinheiten mit Skizze begründen;–;
3;2;II;K3;Volumen;VOL:liter;Regenhöhe in Liter pro m²;mm, Liter;
4;2;II;K5;Gleichung;LG:beide_seiten;lineare Gleichung mit Dezimalzahlen;klein;
5a;2;II;K1;Winkel;KR:tangente;zwei Winkel bestimmen, Begründungsstichwort;Grad;
5b;2;II;K1;Lückentext;KR:tangente;Begründung (Thales, Berührradius) ergänzen;–;
6a;1;II;K5;Maßstab;GR:massstab;passenden Maßstab ankreuzen;–;
6b;2;III;K3;Schätzen;PROP:sach;Personen pro Stunde mit Aufzug abschätzen;m/s;
6c;2;II;K5;Prozent;PGW:zurueck;Ausgangspreis vor Senkung;Tausender Euro;
7a;2;II;K1;Zeigen;TA:sachsituation;Flächenterm einer Figur zeigen;Variable;
7b;1;II;K5;Gleichung;X:Gleichung x² = a (Wurzel, LehrplanPLUS Kl. 9);Seitenlänge aus Flächenterm;cm;
8;2;III;K4;Konstruieren;KON:symmetrie;Figur symmetrisch mit Flächenanteil ergänzen;Raster;
""")
BMT(2012, "A", "2012/bmt8_2012_aufgaben_gruppe_a.pdf", """
1a;1;I;K5;Quotient;GR:masse;Quotient zweier Massen;kg, g;
1b;1;II;K6;Text erfinden;L:TA:Rechengeschichte zu einem Term erfinden;Textaufgabe zu einem Term erfinden;–;Text produzieren
2a;1;I;K5;Umformen;TU:zusammenfassen;vereinfachen;klein;
2b;1;I;K5;Umformen;TU:ausmultiplizieren;vereinfachen;klein;
3;2;II;K5;Prozent;PZ:grundwert;Verkaufspreis aus Anteil;Euro;
4a;2;II;K5;Volumen;VOL:zusammengesetzt;Volumen eines L-Körpers;cm;
4b;2;II;K4;Netz;L:KB:Netz eines Quaders zeichnen (Kl. 5);Netz ergänzen;cm;
5;1;II;K1;Wahr/falsch;KST:kongruenzsatz;Kongruenzaussagen bewerten;–;
6a;1;II;K4;Auswahl;PGW:prozentsatz;prozentuale Zunahme aus Diagramm;–;
6b;1;II;K1;Erklären;DD:irrefuehrend;Täuschung durch Piktogramm;–;
6c;2;III;K3;Schätzen;GR:schaetzen;Anzahl Personen um einen Umfang schätzen;–;Fermi-Aufgabe
7;2;II;K3;Maßstab;GR:massstab;passt die Karte auf eine Seite?;km;
8;2;II;K4;Konstruieren;KR:umkehrung;Konstruktion mit Thaleskreis;–;
9;2;III;K1;Begründen;L:TA:Mit Termen beweisen (gerade/ungerade, Teilbarkeit);Gleichstand möglich? mit Parität;–;
""")
BMT(2011, "A", "2011/bmt8_aufgabe_a.pdf", """
1a;1;I;K4;Ablesen;FG:graph_lesen;Wert im Höhenprofil ablesen;km;Sachgraph
1b;2;II;K3;Geschwindigkeit;PROP:sach;Abfahrtszeit aus Durchschnittsgeschwindigkeit;km/h;
1c;1;II;K5;Auswahl;BR:anteil_bestimmen;Anteil des Anstiegs;–;
2a;1;II;K1;Auswahl;WS:stufen_wechsel;Winkelbeziehung im Trapez;–;
2b;2;III;K1;Herleiten;FV:trapez;Trapezformel herleiten;–;Herleitung
3a;2;II;K5;Gleichung;LG:beide_seiten;Gleichung mit Parametern lösen;klein;
3b;1;III;K2;Parameter;L:LG:Zahl in einer Gleichung so wählen, dass eine vorgegebene Lösung entsteht;Parameter für vorgegebene Lösung;klein;
3c;1;III;K2;Parameter;LG:sonderfaelle;Parameter, für den es keine Lösung gibt;klein;
4;2;II;K6;Satz ergänzen;OL:verknuepfen;Satz mit zwei Ortslinien ergänzen;–;
5a;1;I;K5;Umformen;TU:zusammenfassen;vereinfachen;klein;
5b;1;I;K5;Umformen;TU:minusklammer;vereinfachen;klein;
6a;1;II;K5;Zählen;KOMB:systematisch;Gewinnbeträge systematisch;klein;
6b;1;II;K5;Zählen;KOMB:bedingungen;Gewinnbeträge mit Bedingung;klein;
7a;2;II;K5;Formel;FO:einsetzen;Fußlänge aus Schuhgrößenformel;cm;Kl.-8-Thema
7b;2;III;K3;Schätzen;GR:schaetzen;Größe einer Statue schätzen;m;
""")
BMT(2010, "A", "2010/bmt8-2010-aufgaben-gruppe-a.pdf", """
1a;1;I;K5;Umrechnen;GR:masse;Massen addieren, in t;t;
1b;1;II;K5;Umrechnen;FL:einheiten;Länge mal Fläche, Ergebnis in m²;m²;
2;2;II;K1;Winkel;WS:stufen_wechsel;Winkel an Parallelen mit Stichworten;Grad;
3;1;II;K3;Auswahl;KOMB:grenzen;Anzahl Spiele „jeder gegen jeden“;klein;
4a;1;I;K5;Umformen;TU:zusammenfassen;Term mit Bruchkoeffizienten;–;
4b;1;I;K5;Umformen;TU:minusklammer;Term mit Klammern und Quadrat;–;
5a;1;II;K3;Linear;FLIN:deuten;Temperatur bei linearer Zunahme;°C, km;linear, nicht proportional
5b;2;II;K5;Rückwärts;LG:sach;Mindesttiefe für Zieltemperatur;m;
6;1;II;K3;Auswahl;TA:sachsituation;passende Gleichung zur Flächenänderung;–;
7a;1;II;K3;Schätzen;PROP:sach;Zuckerwürfel schätzen;klein;
7b;1;II;K3;Schätzen;PZ:prozentsatz;Prozent vom Tagesbedarf schätzen;–;
8;2;III;K6;Beschreiben;KON:mittelsenkrechte;Kreismittelpunkt über Sehnen – Schritte beschreiben;–;
9a;1;I;K4;Diagramm;DD:relative_haeufigkeit;Prozentanteil einer Note;28 Personen;
9b;2;II;K5;Mittelwert;DK:mittel_tabelle;Notendurchschnitt;–;
9c;1;III;K2;Beispiel;DK:mittel_rueckwaerts;Verteilung zu vorgegebenem Mittelwert;–;offen
10;2;III;K2;Fläche;FV:rueckwaerts;Seitenlänge aus Flächenteilung;cm;
""")
BMT(2009, "A", "2009/bmt8-2009-aufgaben-gruppe-a.pdf", """
1a;1;II;K5;Volumen;VOL:zusammengesetzt;Volumen eines Würfelteils;cm³;
1b;2;II;K4;Netz;L:KB:Netz eines Quaders zeichnen (Kl. 5);maßstäbliches Netz des Teilkörpers;cm;Punkte je Teil unsicher
2;1;III;K2;Beispiel;TB:teiler;Zahlen, für die ein Term natürlich ist;klein;offen
3a;2;II;K1;Erklären;DD:irrefuehrend;Übertreibung durch Säulendiagramm;Tausender;
3b;1;II;K5;Prozent;PGW:zurueck;Vorjahreswert aus 20-%-Abnahme;Tausender;
4a;2;II;K5;Geschickt;RG:verteilen;gemeinsamen Faktor nutzen;klein;
4b;1;II;K5;Rechnen;BRR:potenzen;Bruch-/Potenzterm;klein;
5;1;II;K1;Begründen;BR:zahlbereiche;Aussage über negative Zahl prüfen;–;
6;2;II;K5;Gleichung;LG:klammern;Gleichung mit Klammern;klein;
7a;1;II;K1;Begründen;WS:innenwinkelsumme;kein Dreieck mit zwei stumpfen Winkeln;–;
7b;1;II;K4;Koordinaten;GB:koordinaten;Punkt für symmetrisches Trapez;klein;
7c;1;II;K2;Koordinaten;FV:dreieck;Punkt für doppelte Dreiecksfläche;klein;
8;1;II;K3;Fläche;FL:sachaufgaben;Parkfläche aus Laufstrecke;km, m²;
9a;1;II;K3;Ankreuzen;TA:uebersetzen;Gleichungen zu einem Verhältnis ankreuzen;–;
9b;1;II;K6;Deuten;TA:deuten;Satz zur Gleichung ergänzen;–;
10a;1;II;K1;Winkel;KR:thales;Winkel am Halbkreis begründen;Grad;
10b;1;II;K1;Winkel;WS:figuren;zweiten Winkel begründen;Grad;
""")

# ---------------------------------------------------------------- Aufbau
def laden():
    liste = json.load(open(os.path.join(WURZEL, "inhalte/themenliste.json")))
    themen = {}
    for r in liste:
        d = json.load(open(os.path.join(WURZEL, r["datei"])))
        themen[r["thema_schluessel"]] = dict(
            id=r["thema_id"], titel=r["titel"], klasse=(r["klasse"] or {}).get("gym_by"),
            lernbereich=(r["lernbereich"] or {}).get("gym_by"),
            etappen={e["lernziel"]: e["titel"] for e in d["inhalt"]["etappen"]})
    teil = {}
    tl = json.load(open(os.path.join(WURZEL, "inhalte/pruefung/lehrplan/lk_teilung_2211.json")))
    id2s = {v["id"]: k for k, v in themen.items()}
    for x in tl["teilungsliste"]:
        for p in x["teile"]:
            for e in p["etappen"]:
                teil[(id2s.get(x["thema"]), e["lernziel"])] = f"Teil {p['teil']} von {p['von']} ({p.get('untertitel')})"
    return themen, teil

def main():
    themen, teil = laden()
    zeilen, fehler = [], []
    for a in ARBEITEN:
        for z in a["aufgaben"]:
            t = z.split(";")
            if len(t) != 9:
                fehler.append(f"{a['arbeit_id']}: Feldzahl {len(t)}: {z}"); continue
            nr, pkt, niv, komp, typ, zu, kurz, gr, bes = [s.strip() for s in t]
            r = dict(arbeit_id=a["arbeit_id"], klasse=a["klasse"], aufgabe=nr,
                     punkte=None if pkt == "?" else int(pkt), niveau=niv, kompetenz=komp, typ=typ,
                     kurzbeschreibung=kurz, groessenordnung=gr, besonderheit=bes or None,
                     status="zugeordnet", thema_schluessel=None, thema_klasse=None, etappe=None,
                     etappe_titel=None, teil=None, lernbereich=None, vorschlag=None)
            if zu.startswith("X:"):
                r.update(status="ausserhalb", vorschlag=zu[2:])
            else:
                luecke = zu.startswith("L:")
                if luecke:
                    _, kz, vors = zu.split(":", 2)
                    r.update(status="luecke", vorschlag=vors)
                    s = K[kz]
                else:
                    kz, et = zu.split(":")
                    s = K[kz]
                    if et not in themen[s]["etappen"]:
                        fehler.append(f"{a['arbeit_id']} {nr}: Etappe {et} fehlt in {s}")
                    r.update(etappe=et, etappe_titel=themen[s]["etappen"].get(et), teil=teil.get((s, et)))
                r.update(thema_schluessel=s, thema_klasse=themen[s]["klasse"], lernbereich=themen[s]["lernbereich"])
            zeilen.append(r)
        bek = sum(r["punkte"] or 0 for r in zeilen if r["arbeit_id"] == a["arbeit_id"])
        a["punkte_summe_bekannt"] = bek
        if a.get("punkte_gesamt") and "Auszug" not in a["titel"] and all(r["punkte"] is not None for r in zeilen if r["arbeit_id"] == a["arbeit_id"]) and bek != a["punkte_gesamt"]:
            fehler.append(f"{a['arbeit_id']}: Summe {bek} ≠ {a['punkte_gesamt']}")
    if fehler:
        raise SystemExit("\n".join(fehler))

    meta = []
    for a in ARBEITEN:
        m = {k: v for k, v in a.items() if k != "aufgaben"}
        m["abruf"] = ABRUF
        rs = [r for r in zeilen if r["arbeit_id"] == a["arbeit_id"]]
        m["anzahl_aufgaben"] = len(rs)
        m["themen_gemeinsam"] = sorted({r["thema_schluessel"] for r in rs if r["thema_schluessel"]})
        meta.append(m)
    out = dict(stand=ABRUF, hinweis="Katalog in eigenen Worten; keine Aufgabentexte, keine Lösungen, keine Personennamen. "
               "niveau und kompetenz sind eigene Einschätzung (Annahme). Quelle je Arbeit verlinkt.",
               arbeiten=meta, aufgaben=zeilen)
    json.dump(out, open(os.path.join(HIER, "katalog.json"), "w"), ensure_ascii=False, indent=1)

    md = ["# Prüfmaterial Gymnasium Bayern – Katalog je Arbeit", "",
          f"Stand {ABRUF}. Erzeugt von `_bau.py` – nicht von Hand ändern. Einzelzeilen je Aufgabe: `katalog.json`.",
          "Niveau I/II/III und Kompetenz K1–K6 sind **eigene Einschätzung** (Annahme). „?“ = Punkte nicht eindeutig.", ""]
    for kl in (5, 8):
        md += [f"## Klasse {kl}", ""]
        for m in [x for x in meta if x["klasse"] == kl]:
            rs = [r for r in zeilen if r["arbeit_id"] == m["arbeit_id"]]
            md += [f"### {m['arbeit_id']} – {m['titel']}", "",
                   f"- Quelle: <{m['quelle']}> (abgerufen {ABRUF}) · Herausgeber: {m['herausgeber']} · {m['lizenz']}",
                   f"- Art: {m['art']} · Nummer/Zeitpunkt: {m['nummer']} · Jahr: {m.get('jahr') or 'unbekannt'} · Bundesland: {m['bundesland']}",
                   f"- Zeit: {m.get('zeit_min') or '?'} min · Punkte: {m.get('punkte_gesamt') or '?'} · Hilfsmittel: {m['hilfsmittel']} · frei zugänglich: {'ja' if m['frei'] else 'nein'}",
                   f"- Passung: {m['passung']}",
                   f"- Gemeinsam geprüfte Themen: {', '.join(m['themen_gemeinsam']) or '–'}", "",
                   "| Nr | P | Niv | K | Typ | Inhalt (eigene Worte) | Zuordnung |", "|---|---|---|---|---|---|---|"]
            for r in rs:
                if r["status"] == "zugeordnet":
                    zu = f"{r['thema_schluessel']} › {r['etappe']}" + (f" ({r['teil']})" if r["teil"] else "")
                elif r["status"] == "luecke":
                    zu = f"**Lücke** ({r['thema_schluessel']}): {r['vorschlag']}"
                else:
                    zu = f"außerhalb: {r['vorschlag']}"
                md.append(f"| {r['aufgabe']} | {r['punkte'] if r['punkte'] is not None else '?'} | {r['niveau']} | {r['kompetenz']} | {r['typ']} | {r['kurzbeschreibung']} | {zu} |")
            md.append("")
    open(os.path.join(HIER, "katalog.md"), "w").write("\n".join(md))

    # Kennzahlen für auswertung.md
    for kl in (5, 8):
        print(f"\n===== Klasse {kl}")
        ms = [m for m in meta if m["klasse"] == kl]
        rs = [r for r in zeilen if r["klasse"] == kl]
        print("Arbeiten", len(ms), "Aufgaben", len(rs))
        for gruppe, filt in (("alle", lambda m: True), ("BMT8", lambda m: m["arbeit_id"].startswith("G8-B")),
                             ("ohne BMT8", lambda m: not m["arbeit_id"].startswith("G8-B"))):
            ids = {m["arbeit_id"] for m in ms if filt(m)}
            sub = [r for r in rs if r["arbeit_id"] in ids]
            if not sub: continue
            niv = collections.Counter(r["niveau"] for r in sub)
            pn = collections.Counter();
            for r in sub:
                if r["punkte"]: pn[r["niveau"]] += r["punkte"]
            tp = sum(pn.values())
            print(f" [{gruppe}] n={len(sub)} Niveau-Anzahl {dict(niv)} Niveau-Punkteanteil",
                  {k: round(100 * v / tp) for k, v in pn.items()} if tp else "-",
                  "Kompetenz", dict(collections.Counter(r["kompetenz"] for r in sub)),
                  "Status", dict(collections.Counter(r["status"] for r in sub)))
            print("   Typen:", collections.Counter(r["typ"] for r in sub).most_common(12))
            zeiten = [m.get("zeit_min") for m in ms if filt(m) and m.get("zeit_min")]
            pk = [m.get("punkte_gesamt") for m in ms if filt(m) and m.get("punkte_gesamt")]
            print("   Zeiten", zeiten, "Punkte", pk, "Aufgaben je Arbeit", [m["anzahl_aufgaben"] for m in ms if filt(m)])
        th = collections.Counter(r["thema_schluessel"] for r in rs if r["thema_schluessel"])
        print(" Themen:", th.most_common())
        et = collections.Counter((r["thema_schluessel"], r["etappe"]) for r in rs if r["etappe"])
        print(" Etappen:", et.most_common())
        own = [s for s, v in themen.items() if v["klasse"] == kl]
        for s in own:
            nie = [e for e in themen[s]["etappen"] if not et.get((s, e))]
            print(f"  nie geprüft {s}: {nie}")
        print(" Lücken:", collections.Counter(r["vorschlag"] for r in rs if r["status"] == "luecke").most_common())
        print(" außerhalb:", collections.Counter(r["vorschlag"] for r in rs if r["status"] == "ausserhalb").most_common())

if __name__ == "__main__":
    main()
