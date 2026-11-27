# LP-RS (22.11.): Abgleich je Lehrplan-Punkt. Datenbankstand gelesen 22.11.2026 (schule.eintrag/zuordnung), Original LehrplanPLUS abgerufen 22.11.2026.
# Zeile: pfad | eintrag_id | Zuordnung vorher | Zuordnung nachher (Vorschlag) | Befund | Notiz
# Zuordnung: <thema><h|n>, h = haupt, n = neben. Befund: ok, ergaenzt, umgehaengt, teilweise, luecke.

QUELLEN = {
 7:  dict(kl=5,  gr='alle', url='https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/5/mathematik/mathe'),
 8:  dict(kl=6,  gr='alle', url='https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/6/mathematik/mathe'),
 24: dict(kl=7,  gr='I',    url='https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/7/mathematik/wpfg1'),
 25: dict(kl=7,  gr='II/III', url='https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/7/mathematik/wpfg2-3'),
 12: dict(kl=8,  gr='I',    url='https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/8/mathematik/wpfg1'),
 26: dict(kl=8,  gr='II/III', url='https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/8/mathematik/wpfg2-3'),
 13: dict(kl=9,  gr='I',    url='https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/9/mathematik/wpfg1'),
 14: dict(kl=9,  gr='II/III', url='https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/9/mathematik/wpfg2-3'),
 15: dict(kl=10, gr='I',    url='https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/10/mathematik/wpfg1'),
 16: dict(kl=10, gr='II/III', url='https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/10/mathematik/wpfg2-3'),
 3:  dict(kl=7,  gr='gym',  url='https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik'),
 4:  dict(kl=8,  gr='gym',  url='https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/8/mathematik'),
}

# Lernbereiche: (quelle, pfad, eintrag_id, Titel DB, Titel Original, Std DB, Std Original, Punkte DB, Punkte Original)
LB = [
 (7,'1',290,'Natürliche Zahlen','Natürliche Zahlen',50,50,14,12),
 (7,'1.1',291,'Natürliche Zahlen im Dezimalsystem','Natürliche Zahlen im Dezimalsystem',None,None,4,4),
 (7,'1.2',296,'Andere Zahlensysteme','Andere Zahlensysteme',None,None,2,1),
 (7,'1.3',299,'Grundrechenarten und Rechengesetze','Grundrechenarten und Rechengesetze',None,None,6,6),
 (7,'1.4',306,'Kombinatorik','Kombinatorik',None,None,2,1),
 (7,'2',309,'Ganze Zahlen','Ganze Zahlen',20,20,7,5),
 (7,'3',317,'Geometrische Grundvorstellungen und Grundbegriffe','Geometrische Grundvorstellungen und Grundbegriffe',30,30,9,6),
 (7,'4',327,'Größen','Größen',20,20,6,6),
 (7,'5',334,'Umfang und Flächeninhalt ebener Figuren','Umfang und Flächeninhalt ebener Figuren',15,15,6,6),
 (7,'6',341,'Auswertung von Daten','Auswertung von Daten',5,5,3,3),
 (8,'1',345,'Rationale Zahlen','Rationale Zahlen',68,68,12,10),
 (8,'2',358,'Achsenspiegelung und Symmetrie','Achsenspiegelung und Symmetrie',13,13,5,5),
 (8,'3',364,'Flächeninhalt ebener Figuren','Flächeninhalt ebener Figuren',18,18,6,4),
 (8,'4',371,'Raumgeometrie','Raumgeometrie',14,14,4,2),
 (8,'5',376,'Terme und Gleichungen','Terme und Gleichungen',15,15,7,7),
 (8,'6',384,'Direkte Proportionalität','Direkte Proportionalität',12,12,6,4),
 (24,'1',691,'Potenzrechnung','Potenzen',10,10,3,3),
 (24,'2',693,'Verschiebungen','Parallelverschiebung',23,23,7,7),
 (24,'3',695,'Dreiecksgeometrie','Dreiecke',14,14,4,4),
 (24,'4',697,'Raumdarstellung','Raumgeometrie',10,10,3,3),
 (24,'5',699,'Ortsgeometrie','Geometrische Ortslinien und Ortsbereiche',12,12,5,5),
 (24,'6',701,'Terme und lineare Relationen','Terme, Gleichungen und Ungleichungen',22,22,4,4),
 (24,'7',706,'Proportionalitäten','Proportionalitäten',12,12,5,5),
 (24,'8',708,'Datenanalyse','Auswertung von Daten',9,9,4,4),
 (25,'1',710,'Potenzrechnung','Potenzen',10,10,3,3),
 (25,'2',712,'Verschiebungen','Parallelverschiebung',21,21,7,7),
 (25,'3',714,'Ortsgeometrie','Geometrische Ortslinien und Ortsbereiche',10,10,4,4),
 (25,'4',716,'Terme und lineare Relationen','Terme, Gleichungen und Ungleichungen',22,22,4,4),
 (25,'5',721,'Proportionalitäten','Proportionalitäten',12,12,5,5),
 (25,'6',723,'Datenanalyse','Auswertung von Daten',9,9,4,4),
 (12,'1',492,'Vierecksgeometrie','Vierecke',12,12,2,2),
 (12,'2',493,'Rotationen','Drehung',6,6,5,5),
 (12,'3',494,'Raumdarstellung','Raumgeometrie',13,13,3,3),
 (12,'4',495,'Algebraische Umformungen und lineare Relationen','Terme, Gleichungen und Ungleichungen',40,40,3,3),
 (12,'5',496,'Rationale Terme und Verhältnisgleichungen','Bruchterme und Bruchgleichungen',7,7,2,2),
 (12,'6',497,'Funktionen','Funktionen',26,26,6,6),
 (12,'7',498,'Zufallsversuche','Daten und Zufall',8,8,2,2),
 (26,'1',742,'Dreiecks-/Vierecksgeometrie','Dreiecke und Vierecke',16,16,5,5),
 (26,'2',744,'Raumdarstellung','Raumgeometrie',7,7,2,2),
 (26,'3',746,'Algebraische Umformungen und lineare Gleichungen','Terme und Gleichungen',40,40,3,3),
 (26,'4',750,'Rationale Terme und Verhältnisgleichungen','Bruchterme und Bruchgleichungen',5,5,2,2),
 (26,'5',753,'Funktionen','Funktionen',8,8,5,5),
 (26,'6',755,'Zufallsversuche','Daten und Zufall',8,8,2,2),
 (13,'1',499,'Erweiterung des Zahlbereichs','Reelle Zahlen',10,10,3,3),
 (13,'2',500,'Ähnlichkeitsabbildungen','Zentrische Streckung',17,17,8,8),
 (13,'3',501,'Rechtwinklige Geometrie','Rechtwinklige Dreiecke',20,20,6,6),
 (13,'4',502,'Kreisgeometrie','Kreis',10,10,2,2),
 (13,'5',503,'Körperberechnungen','Raumgeometrie',20,20,4,4),
 (13,'6',504,'Lineare Gleichungssysteme','Systeme linearer Gleichungen',12,12,1,1),
 (13,'7',505,'Parabeln und quadratische Gleichungen','Quadratische Funktionen und quadratische Gleichungen',42,42,9,9),
 (13,'8',506,'Wahrscheinlichkeitsgrundlagen','Daten und Zufall',9,9,5,5),
 (14,'1',507,'Zahlbereich','Reelle Zahlen',7,7,3,3),
 (14,'2',508,'Streckung','Zentrische Streckung',13,13,3,3),
 (14,'3',509,'Rechtwinklige Geometrie','Rechtwinklige Dreiecke',20,20,6,6),
 (14,'4',510,'Kreise','Kreis',10,10,2,2),
 (14,'5',511,'Geradenfunktionen','Lineare Funktionen',15,15,4,4),
 (14,'6',512,'Lineare Gleichungssysteme','Systeme linearer Gleichungen',10,10,1,1),
 (14,'7',513,'Stochastik','Daten und Zufall',9,9,5,5),
 (15,'1',514,'Trigonometrische Verfahren','Trigonometrie',42,42,11,11),
 (15,'2',515,'Koordinatenabbildungen','Abbildungen',30,30,4,4),
 (15,'3',516,'Potenzrechnung und Potenzfunktionen','Potenzen und Potenzfunktionen',16,16,4,4),
 (15,'4',517,'Exponentielle und logarithmische Zusammenhänge','Exponentialfunktionen, Logarithmen und Logarithmusfunktionen',22,22,3,3),
 (15,'5',518,'Mehrstufiger Zufall','Daten und Zufall',10,10,2,2),
 (16,'1',519,'Trigonometrie','Trigonometrie',21,21,6,6),
 (16,'2',520,'Körpergeometrie','Raumgeometrie',20,20,5,5),
 (16,'3',521,'Exponentielle Zusammenhänge','Exponentialfunktionen, Logarithmen',10,10,3,3),
 (16,'4',522,'Parabeln und quadratische Gleichungen','Quadratische Funktionen und quadratische Gleichungen',35,35,6,6),
 (16,'5',523,'Stochastik','Daten und Zufall',10,10,2,2),
 (3,'1',105,'Terme mit Variablen','Terme mit Variablen',37,37,None,None),
 (3,'1.1',106,'Aufstellen und Interpretieren von Termen','Aufstellen und Interpretieren von Termen',13,13,4,4),
 (3,'1.2',111,'Umformen von Termen','Umformen von Termen',24,24,6,5),
 (3,'2',118,'Geometrische Figuren: Symmetrie und Winkel','Geometrische Figuren: Symmetrie und Winkel',21,21,None,None),
 (3,'2.1',119,'Achsen- und punktsymmetrische Figuren','Achsen- und punktsymmetrische Figuren',12,12,5,3),
 (3,'2.2',125,'Winkelbetrachtungen an Figuren','Winkelbetrachtungen an Figuren',9,9,5,4),
 (3,'3',131,'Lineare Gleichungen und Vertiefung der Prozentrechnung','Lineare Gleichungen und Vertiefung der Prozentrechnung',17,17,6,4),
 (3,'4',138,'Kenngrößen von Daten','Kenngrößen von Daten',8,8,4,3),
 (3,'5',143,'Kongruenz, besondere Dreiecke und Dreieckskonstruktionen','Kongruenz, besondere Dreiecke und Dreieckskonstruktionen',29,29,9,9),
 (4,'1',153,'Funktion und Term','Funktion und Term',8,8,6,3),
 (4,'2',160,'Lineare Funktionen','Lineare Funktionen',16,16,8,5),
 (4,'3',169,'Elementare gebrochen-rationale Funktionen','Elementare gebrochen-rationale Funktionen',13,13,4,3),
 (4,'4',174,'Bruchterme und Bruchgleichungen','Bruchterme und Bruchgleichungen',13,13,5,5),
 (4,'5',180,'Laplace-Experimente','Laplace-Experimente',14,14,5,4),
 (4,'6',186,'Lineare Gleichungssysteme','Lineare Gleichungssysteme',10,10,4,3),
 (4,'7',191,'Kreis und Zylinder','Kreis und Zylinder',10,10,7,4),
]

P = {}
P[7] = """
1.1/k1|292|-|15h|ergaenzt|
1.1/k2|293|-|15h|ergaenzt|
1.1/k3|294|-|15h|ergaenzt|
1.1/k4|295|-|15h|ergaenzt|
1.2/k1|297|-|-|luecke|Dualsystem und römische Zahlen: kein Thema
1.2/k2|298|-|-|luecke|Vor- und Nachteile von Zahlensystemen: kein Thema
1.3/k1|300|18h|18h|ok|
1.3/k2|301|18h|18h|ok|
1.3/k3|302|18h|18h|ok|
1.3/k4|303|19h|67h,19n|umgehaengt|große Zahlen in Zehnerpotenzen stehen in 67 (Kl. 5); 19 erst Kl. 7
1.3/k5|304|67h|67h|ok|
1.3/k6|305|17h|17h|ok|
1.4/k1|307|-|60h|ergaenzt|
1.4/k2|308|-|60h|ergaenzt|
2/k1|310|-|16h|ergaenzt|
2/k2|311|-|16h|ergaenzt|
2/k3|312|-|16h|ergaenzt|
2/k4|313|-|16h|ergaenzt|
2/k5|314|-|16h,18n|ergaenzt|
2/k6|315|-|16h,18n|ergaenzt|
2/k7|316|-|16h|ergaenzt|
3/k1|318|42h|42h|ok|
3/k2|319|42h|42h|ok|
3/k3|320|42h|42h|ok|
3/k4|321|42h|42h|ok|
3/k5|322|42h,43n|42h,43n|ok|
3/k6|323|42h,43n|42h,43n|ok|
3/k7|324|52h|52h|ok|
3/k8|325|52h,91n|52h,91n|ok|
3/k9|326|42n,52h|42n,52h|ok|
4/k1|328|25h|25h|ok|
4/k2|329|25h|25h|ok|
4/k3|330|25h|25h|ok|
4/k4|331|-|25h|ergaenzt|Etappe Maßstab auf Karten und Plänen
4/k5|332|25n,26h|25n,26h|ok|Dreisatz schon Kl. 5, Thema 26 steht in Kl. 6
4/k6|333|-|25h|ergaenzt|
5/k1|335|-|50h|ergaenzt|
5/k2|336|-|50h|ergaenzt|
5/k3|337|-|50h|ergaenzt|
5/k4|338|-|50h|ergaenzt|
5/k5|339|-|50h|ergaenzt|
5/k6|340|-|50h|ergaenzt|
6/k1|342|-|57h|ergaenzt|
6/k2|343|-|57h|ergaenzt|
6/k3|344|-|57h|ergaenzt|
"""
P[8] = """
1/k1|346|21h|21h|ok|
1/k2|347|21h|21h|ok|
1/k3|348|21h|21h|ok|
1/k4|349|21h|21h|ok|
1/k5|350|22h|22h|ok|
1/k6|351|22h|22h|ok|
1/k7|352|21n,22h,24n|21n,22h,24n|ok|
1/k8|353|21h,22n|21h,22n|ok|
1/k9|354|21h|21h|ok|
1/k10|355|23h|23h|ok|
1/k11|356|23h|23h|ok|
1/k12|357|23h,25n|23h,25n|ok|
2/k1|359|46h|46h|ok|
2/k2|360|-|46h|ergaenzt|
2/k3|361|44h,46n|46h,44n|umgehaengt|Grundkonstruktionen stehen in 46 (Kl. 6); 44 erst Kl. 7
2/k4|362|46h|46h|ok|
2/k5|363|46h|46h|ok|
3/k1|365|-|99h,50n|ergaenzt|
3/k2|366|-|99h|teilweise|Drachenviereck und Raute ohne eigene Etappe
3/k3|367|-|99h|ergaenzt|
3/k4|368|-|99h|ergaenzt|
3/k5|369|-|99h|ergaenzt|
3/k6|370|50n,53h|53h,50n,99n|ergaenzt|
4/k1|372|-|100h|ergaenzt|
4/k2|373|-|100h|ergaenzt|
4/k3|374|-|100h|ergaenzt|
4/k4|375|-|100h|ergaenzt|
5/k1|377|28h|28h|ok|
5/k2|378|28h|28h|ok|
5/k3|379|28h|28h|ok|
5/k4|380|28h,29n|28h,29n|ok|
5/k5|381|1h|1h|ok|
5/k6|382|1h|1h|ok|
5/k7|383|1h|1h|ok|
6/k1|385|26h|26h|ok|
6/k2|386|26h|26h|ok|
6/k3|387|26h|26h|ok|
6/k4|388|26h|26h|ok|
6/k5|389|24h|24h|ok|
6/k6|390|24h|24h|ok|
"""
P[24] = """
1/K1|864|-|30h|ergaenzt|
1/K2|865|-|102h,103n|ergaenzt|
1/K3|866|19n,30h|19h,30n|umgehaengt|Vorsilben und Zehnerpotenzen sind Kern von 19
2/K1|868|48h|46h|umgehaengt|48 stillgelegt; Verschiebung in 46
2/K2|869|48h|46h|umgehaengt|48 stillgelegt
2/K3|870|48h|46h|umgehaengt|48 stillgelegt; Etappe Gegenvektor in 46
2/K4|871|48h|-|luecke|Vektorkoordinaten: kein freigegebenes Thema (48 stillgelegt)
2/K5|872|50n,74h|50n,74h|ok|
2/K6|873|43h|98h,43n|umgehaengt|Stufen-/Wechselwinkel in 98 (Kl. 7)
2/K7|874|43h|98h,43n|umgehaengt|Winkelsummen und Außenwinkel in 98
3/K1|876|-|44h|ergaenzt|
3/K2|877|-|44h|ergaenzt|
3/K3|878|-|44h|ergaenzt|
3/K4|879|-|44h|ergaenzt|
4/K1|881|91h|91h|ok|91 steht in Kl. 8 (Gruppe II/III), Gruppe I hat es in Kl. 7
4/K2|882|91h|91h,52n|ergaenzt|
4/K3|883|91h|91h|teilweise|wahre Größe ohne eigene Etappe
5/K1|885|-|73h|ergaenzt|
5/K2|886|-|45h|ergaenzt|
5/K3|887|-|73h|ergaenzt|
5/K4|888|-|73h|ergaenzt|
5/K5|889|-|45h,47n|ergaenzt|Schwerpunkt als Etappe in 47 (Kl. 9)
6/K1|702|-|29h,102n|ergaenzt|
6/K2|703|2h|2h|ok|
6/K3|704|3h,69n|3h,69n|ok|
6/K4|705|2h,3n|2h,3n|ok|
7/K1|891|94h|94h|ok|
7/K2|892|24n,71h|24n,71h|ok|
7/K3|893|93h|93h|ok|
7/K4|894|93h|93h|ok|
7/K5|895|26n,93h|26n,93h|ok|
8/K1|897|58h,95n|58h,95n|ok|
8/K2|898|-|95h,58n|ergaenzt|
8/K3|899|81h|81h|ok|
8/K4|900|57h|57h|ok|
"""
P[25] = """
1/K1|902|30h|30h|ok|
1/K2|903|-|102h,103n|ergaenzt|
1/K3|904|19n,30h|19h,30n|umgehaengt|
2/K1|906|48h|46h|umgehaengt|48 stillgelegt
2/K2|907|48h|46h|umgehaengt|48 stillgelegt
2/K3|908|48h|46h|umgehaengt|48 stillgelegt
2/K4|909|48h|-|luecke|Vektorkoordinaten: kein freigegebenes Thema
2/K5|910|50n,74h|50n,74h|ok|
2/K6|911|43h|98h,43n|umgehaengt|
2/K7|912|43h|98h,43n|umgehaengt|
3/K1|914|-|73h,45n|ergaenzt|Thaleskreis in 45
3/K2|915|-|45h|ergaenzt|
3/K3|916|-|73h|ergaenzt|
3/K4|917|-|45h|ergaenzt|
4/K1|717|-|29h,102n|ergaenzt|
4/K2|718|2h|2h|ok|
4/K3|719|3h,69n|3h,69n|ok|
4/K4|720|2h,3n|2h,3n|ok|
5/K1|919|94h|94h|ok|
5/K2|920|24n,71h|24n,71h|ok|
5/K3|921|93h|93h|ok|
5/K4|922|93h|93h|ok|
5/K5|923|26n,93h|26n,93h|ok|
6/K1|925|58h,95n|58h,95n|ok|
6/K2|926|-|95h,58n|ergaenzt|
6/K3|927|81h|81h|ok|
6/K4|928|57h|57h|ok|
"""
P[12] = """
1/K1|930|44h|46h,42n,44n|umgehaengt|Vierecke ordnen in 46, Grundformen in 42
1/K2|931|44h|44h|teilweise|Vierecke konstruieren ohne eigene Etappe (44 behandelt Dreiecke)
2/K1|933|46n,48h|46h|umgehaengt|48 stillgelegt; Etappe Um einen Punkt drehen in 46
2/K2|934|46n,48h|46h|umgehaengt|Etappe An einem Punkt spiegeln in 46
2/K3|935|46n,48h|46h|umgehaengt|
2/K4|936|46n,48h|46h|umgehaengt|
2/K5|937|46n,48h|49n|luecke|Vektoren drehen: nur in 49 (Kl. 10), kein Thema in Kl. 8
3/K1|939|91h|91h|ok|
3/K2|940|91h|91h|ok|
3/K3|941|91h|91h|ok|
4/K1|732|29h|29h|ok|weitergeführt aus Kl. 7
4/K2|733|29n,35n,97h|29n,35n,97h|ok|
4/K3|734|2h,3n|2h,3n|ok|weitergeführt aus Kl. 7
5/K1|736|31h|31h|ok|
5/K2|737|5h|5h|ok|
6/K1|943|32h|32h|ok|
6/K2|944|32n,33h|32n,33h|ok|
6/K3|945|32n,33h|32n,33h|ok|
6/K4|946|32n,33h|32n,33h|ok|
6/K5|947|33h,78n|33h,78n|ok|78 stillgelegt (nur Nebenbezug)
6/K6|948|33h,74n|33h,74n|ok|
7/K1|950|-|61h,60n,63n|ergaenzt|61 steht in Kl. 9; Ergebnis/Ereignis, Baum, Vierfeldertafel schon Kl. 8
7/K2|951|61h|61h|ok|
"""
P[26] = """
1/K1|953|-|44h|ergaenzt|Gruppe II/III: Dreiecke erst Kl. 8 (Gruppe I Kl. 7)
1/K2|954|-|44h|ergaenzt|
1/K3|955|-|44h|ergaenzt|
1/K4|956|44h|46h,42n,44n|umgehaengt|
1/K5|957|44h|44h|teilweise|Vierecke konstruieren ohne eigene Etappe
2/K1|959|91h|91h|ok|
2/K2|960|91h|91h|ok|
3/K1|747|29h|29h|ok|
3/K2|748|29n,35n,97h|29n,35n,97h|ok|
3/K3|749|2h|2h|ok|
4/K1|751|31h|31h|ok|
4/K2|752|5h|5h|ok|
5/K1|962|32h|32h|ok|
5/K2|963|-|32h,33n|ergaenzt|
5/K3|964|-|33h|ergaenzt|Gruppe II/III: nur Ursprungsgeraden in Kl. 8
5/K4|965|-|33h|ergaenzt|
5/K5|966|-|33h|ergaenzt|
6/K1|968|-|61h,60n,63n|ergaenzt|
6/K2|969|61h|61h|ok|
"""
P[13] = """
1/K1|758|20h,68n|20h,68n|ok|
1/K2|759|12h,68n|8h,68n|umgehaengt|12 stillgelegt; Etappe reinquadratisch in 8
1/K3|760|20h|20h|ok|
2/K1|762|47h|47h|ok|
2/K2|763|47h|47h|ok|
2/K3|764|47h|47h|ok|
2/K4|765|47h|47h|ok|
2/K5|766|47n,48h|47h|umgehaengt|48 stillgelegt; Vektorrechnung nur teilweise in 47
2/K6|767|40n,47h|47h|ok|40 stillgelegt (nur Nebenbezug)
2/K7|768|47h|47h|ok|
2/K8|769|47h|47h|ok|
3/K1|771|54h|54h|ok|
3/K2|772|54h|54h|ok|
3/K3|773|48n,54h|54h|ok|48 stillgelegt (nur Nebenbezug)
3/K4|774|54h|54h|ok|
3/K5|775|54h|54h|ok|
3/K6|776|54n,55h|54n,55h|ok|
4/K1|778|-|51h|ergaenzt|
4/K2|779|-|51h|ergaenzt|
5/K1|781|92h|92h|ok|
5/K2|782|52n,92h|52n,92h,101n|ergaenzt|
5/K3|783|51n,53n,92h|51n,53n,92h,101n|ergaenzt|
5/K4|784|92h|92h|ok|
6/K1|786|6h|6h|ok|
7/K1|788|8n,35h,40n|8n,35h|ok|
7/K2|789|8n,35h,40n|8n,35h|ok|
7/K3|790|8n,35h,40n|8n,35h|ok|
7/K4|791|8n,35h,40n|8n,35h|ok|
7/K5|792|35h,78n|35h|ok|
7/K6|793|8h|8h|ok|
7/K7|794|8h|8h|ok|
7/K8|795|8n,35h,78n|8n,35h|ok|
7/K9|796|13h|13h|ok|
8/K1|798|61h,64n|61h,64n|ok|
8/K2|799|-|61h|ergaenzt|
8/K3|800|-|61h|ergaenzt|
8/K4|801|-|61h,63n|ergaenzt|
8/K5|802|-|61h|ergaenzt|
"""
P[14] = """
1/K1|971|20h,68n|20h,68n|ok|
1/K2|804|12h,68n|8h,68n|umgehaengt|12 stillgelegt
1/K3|972|20h|20h|ok|
2/K1|974|-|47h|ergaenzt|
2/K2|975|-|47h|ergaenzt|
2/K3|976|-|47h|ergaenzt|
3/K1|978|54h|54h|ok|
3/K2|979|54h|54h|ok|
3/K3|980|54h|54h|ok|
3/K4|981|54h|54h|ok|
3/K5|982|54h|54h|ok|
3/K6|983|54n,55h|54n,55h|ok|
4/K1|985|-|51h|ergaenzt|
4/K2|986|-|51h|ergaenzt|
5/K1|988|33h|33h|ok|
5/K2|989|33h|33h|ok|
5/K3|990|33h,78n|33h|ok|
5/K4|991|33h,74n|33h,74n|ok|
6/K1|815|6h|6h|ok|
7/K1|993|61h,64n|61h,64n|ok|
7/K2|994|-|61h|ergaenzt|
7/K3|995|-|61h|ergaenzt|
7/K4|996|-|61h,63n|ergaenzt|
7/K5|997|-|61h|ergaenzt|
"""
P[15] = """
1/K1|819|14n,38n,56h|14n,38n,56h|ok|
1/K2|820|14n,33n,38n,56h|14n,33n,38n,56h|ok|Etappe Schnittwinkel liegt in 55 (Kl. 9)
1/K3|821|38h|38h|ok|
1/K4|822|14n,38n,56h|14n,38n,56h|ok|
1/K5|823|38n,56h|38n,56h|ok|
1/K6|824|38n,56h|38n,56h|ok|
1/K7|825|14n,38n,56h|14n,38n,56h|ok|
1/K8|826|14n,38n,56h|14n,38n,56h|ok|
1/K9|827|14h|14h|ok|
1/K10|828|49h,56n|49h,56n|ok|
1/K11|829|49h,56n|49h,56n|ok|
2/K1|831|-|49h|ergaenzt|
2/K2|832|-|49h|ergaenzt|
2/K3|833|40h,49n|37h,36n,49n|umgehaengt|40 stillgelegt; Abbilden von Graphen in 36/37
2/K4|834|-|49h|ergaenzt|
3/K1|836|96h|96h|ok|
3/K2|837|9h,96n|96h,9n|umgehaengt|n-te Wurzel ist Kern von 96
3/K3|838|36h,77n,96n|36h,96n|ok|77 stillgelegt (nur Nebenbezug)
3/K4|839|-|36h,9n|ergaenzt|
4/K1|841|10h,37n|10h,37n|ok|
4/K2|842|37h,77n|37h|ok|77 stillgelegt (nur Nebenbezug)
4/K3|843|-|37h|ergaenzt|
5/K1|845|-|62h|ergaenzt|
5/K2|846|-|62h|ergaenzt|
"""
P[16] = """
1/K1|999|-|56h|ergaenzt|
1/K2|1000|33n,56h|33n,56h|ok|
1/K3|1001|38h|38h|ok|
1/K4|1002|-|56h|ergaenzt|
1/K5|1003|56h|56h|ok|
1/K6|1004|56h|56h|ok|
2/K1|1006|91n,92h|91h,92n|umgehaengt|Achsenschnitte und Rotationskörper sind Etappen von 91
2/K2|1007|92h|92h|ok|
2/K3|1008|52n,92h|52n,92h,101n|ergaenzt|
2/K4|1009|51n,53n,92h|51n,53n,92h,101n|ergaenzt|
2/K5|1010|92h|92h|ok|
3/K1|1012|-|37h|ergaenzt|
3/K2|852|10h|10h|ok|
3/K3|1013|-|37h|ergaenzt|
4/K1|855|-|35h|ergaenzt|Gruppe II/III: quadratische Funktionen erst Kl. 10
4/K2|856|-|35h|ergaenzt|
4/K3|857|-|35h|ergaenzt|
4/K4|858|-|35h,97n|ergaenzt|
4/K5|859|8h|8h|ok|
4/K6|860|8h|8h|ok|
5/K1|1015|-|62h|ergaenzt|
5/K2|1016|-|62h|ergaenzt|
"""
# Gymnasium 7 und 8: nur Bericht (keine Korrektur im SQL)
P[3] = """
1.1/k1|107|-|28h|ergaenzt|
1.1/k2|108|-|28h,30n|ergaenzt|
1.1/k3|109|-|28h|ergaenzt|
1.1/k4|110|-|28h|ergaenzt|
1.2/k1|112|29n,30h|102h,29n|umgehaengt|Potenzgesetze natürliche Exponenten = 102 (Gym 7)
1.2/k2|113|-|29h|ergaenzt|
1.2/k3|114|-|29h|ergaenzt|
1.2/k4|115|-|29h|ergaenzt|
1.2/k5|116|-|29h|ergaenzt|
1.2/k6|117|-|29h|ergaenzt|
2.1/k1|120|-|46h|ergaenzt|
2.1/k2|121|-|46h|ergaenzt|
2.1/k3|122|-|46h|ergaenzt|
2.1/k4|123|-|46h,44n|ergaenzt|
2.1/k5|124|-|46h|ergaenzt|
2.2/k1|126|-|98h|ergaenzt|
2.2/k2|127|-|98h|ergaenzt|
2.2/k3|128|-|98h|ergaenzt|
2.2/k4|129|-|98h|ergaenzt|
2.2/k5|130|-|98h|ergaenzt|
3/k1|132|2h|2h|ok|
3/k2|133|2h|2h|ok|
3/k3|134|2h|2h|ok|
3/k4|135|2h|2h|ok|
3/k5|136|94h|94h|ok|
3/k6|137|2n,94h|2n,94h|ok|
4/k1|139|95h|95h|ok|
4/k2|140|95h|95h|ok|
4/k3|141|95h|95h|ok|
4/k4|142|58n,95h|58n,95h|ok|
5/k1|144|-|44h|ergaenzt|
5/k2|145|-|44h|ergaenzt|
5/k3|146|-|44h|ergaenzt|
5/k4|147|-|44h|ergaenzt|
5/k5|148|44n,45h|44n,45h|ok|
5/k6|149|44n,45h|44n,45h|ok|
5/k7|150|44n,45h|44n,45h|ok|
5/k8|151|-|44h|ergaenzt|
5/k9|152|-|44h|ergaenzt|
"""
P[4] = """
1/k1|154|-|32h|ergaenzt|
1/k2|155|-|32h|ergaenzt|
1/k3|156|-|32h|ergaenzt|
1/k4|157|-|32h|ergaenzt|
1/k5|158|-|32h|ergaenzt|
1/k6|159|-|32h|ergaenzt|
2/k1|161|33h|33h|ok|
2/k2|162|33h|33h|ok|
2/k3|163|33h|33h|ok|
2/k4|164|2n,33h|2n,33h|ok|
2/k5|165|6n,33h|6n,33h|ok|
2/k6|166|33h|33h|ok|
2/k7|167|3h,69n|3h,69n|ok|
2/k8|168|26n,33h|26n,33h|ok|
3/k1|170|34h|34h|ok|
3/k2|171|34h|34h|ok|
3/k3|172|34h|34h|ok|
3/k4|173|93h|93h|ok|93 steht im Gymnasium in Kl. 8
4/k1|175|31h|31h|ok|
4/k2|176|31h|31h|ok|
4/k3|177|30h|103h,30n|umgehaengt|Potenzgesetze ganzzahlige Exponenten = 103 (Gym 8)
4/k4|178|5h|5h|ok|
4/k5|179|4h|4h|ok|
5/k1|181|-|61h|ergaenzt|
5/k2|182|61h,64n|61h,64n|ok|
5/k3|183|-|61h|ergaenzt|
5/k4|184|-|61h|ergaenzt|
5/k5|185|-|61h,60n|ergaenzt|
6/k1|187|6h|6h|ok|
6/k2|188|6h|6h|ok|
6/k3|189|6h|6h|ok|
6/k4|190|6h|6h|ok|
7/k1|192|-|51h|ergaenzt|
7/k2|193|-|51h|ergaenzt|
7/k3|194|-|51h|ergaenzt|
7/k4|195|51n,52h,91n|52h,101n,51n,91n|ergaenzt|
7/k5|196|-|101h|ergaenzt|
7/k6|197|-|101h|ergaenzt|
7/k7|198|-|101h,51n|ergaenzt|
"""
STILL = {12, 27, 40, 41, 48, 72, 77, 78, 82, 83}
