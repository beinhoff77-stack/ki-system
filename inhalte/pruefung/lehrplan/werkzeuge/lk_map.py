# LK-D (22.11.2026): Zuordnung je Lehrplanpunkt mit Etappen (Lernziel-Schlüssel).
# Zeile: eintrag_id  haupt  etappen(komma, '-' = keine)  [+N neben dazu] [-X Zuordnung veraltet (nicht löschen)] [#notiz]
# Bisheriger Hauptbezug, der nicht mehr Haupt ist, wird Neben (ausser mit -X).

RS = """
292 15 unendlich
293 15 stellenwert
294 15 strahl_ablesen,vergleichen
295 15 runden_regel,runden_uebertrag,runden_sinnvoll
297 15 dualsystem,roemisch_schreiben #LP-RS-Lücke geschlossen: Etappen stehen in Thema 15
298 15 roemisch_system #LP-RS-Lücke geschlossen
300 18 schriftlich,schriftlich_geteilt
301 18 sach,ueberschlag
302 18 vorteil,verteilen,kopfrechnen
303 67 zehner
304 67 schreibweise,berechnen,quadrat
305 17 teiler,vielfache,primfaktoren
307 60 zaehlprinzip,systematisch
308 60 baumdiagramm
310 16 deuten
311 16 deuten,sach
312 16 betrag
313 16 zahlengerade,ordnen
314 16 addieren,subtrahieren
315 16 ketten
316 16 sach,ketten
318 42 kreis_lage
319 42 lagebeziehungen
320 42 vierecke
321 42 koordinaten,strecken
322 42 winkelarten
323 42 winkelarten
324 52 prisma
325 52 netz,schraegbild
326 52 ansichten
328 25 schaetzen
329 25 laenge,masse,zeit
330 25 kommaschreibweise
331 25 massstab
332 26 dreisatz,einheit
333 25 rechnen
335 50 rechteck
336 50 sachaufgaben
337 50 zerlegen
338 50 einheiten
339 50 rechteck
340 50 zerlegen
342 57 tabelle_auswerten,absolute_haeufigkeit
343 57 tabelle_auswerten
344 57 irrefuehrend
346 21 zahlbereiche
347 21 gemischte_zahlen,anteil_bestimmen
348 21 bruchteil_von,ganzes_bestimmen
349 21 erweitern,kuerzen,ggt
350 22 stellenwerte,runden
351 22 periodisch
352 22 bruch_zu_dezimal,dezimal_zu_bruch,merkwerte
353 21 vergleichen,kgv
354 21 zahlenstrahl,zahlbereiche
355 23 brueche_plus_minus,dezimal_plus_minus,brueche_mal,brueche_geteilt,dezimal_mal,dezimal_geteilt
356 23 vorzeichen,rechenvorteile
357 23 sach
359 46 achsenspiegelung,eigenschaften
360 46 achsenspiegelung
361 46 mittelsenkrechte,winkelhalbierende
362 46 symmetrie
363 46 symmetrie,vierecke_ordnen
365 99 verstehen
366 99 parallelogramm,dreieck,trapez,drachen_raute #Etappe drachen_raute neu (LK)
367 99 dreieck
368 99 zusammengesetzt
369 99 rueckwaerts,zusammengesetzt
370 53 oberflaeche,quader,sachaufgaben
372 100 einheitswuerfel
373 100 einheiten,liter
374 100 quader,zusammengesetzt
375 100 rueckwaerts,verstehen
377 28 uebersetzen,sachsituation
378 28 deuten,struktur
379 28 termwert
380 28 deuten
381 1 aufstellen,zwei_schritte
382 1 waage
383 1 aufstellen,probe
385 26 erkennen
386 26 pruefen,erkennen
387 26 vervielfachen
388 26 dreisatz,einheit
389 24 prozent_bedeutung
390 24 prozentwert,prozentsatz,grundwert
864 30 negativer_exponent
865 102 mal_gleiche_basis,gleicher_exponent,potenz_von_potenz,geteilt_gleiche_basis
866 19 zehnerpotenz,vorsilben_gross,vorsilben_klein,gross_wissenschaftlich,klein_wissenschaftlich
868 46 eigenschaften,verschiebung
869 46 verschiebung
870 46 gegenvektor
871 46 vektor_koordinaten #LP-RS-Lücke geschlossen: neue Etappe vektor_koordinaten in 46
872 74 det_berechnen,parallelogramm,dreieck,viereck,vieleck
873 98 stufen_wechsel,parallel_pruefen
874 98 aussenwinkel,vieleck,innenwinkelsumme
876 44 konstruierbar
877 44 planfigur
878 44 kongruenzsatz
879 44 satz_kehrsatz
881 91 lage,raumwinkel #Raumwinkel: neue Etappe raumwinkel (LK-D 3, F3)
882 91 pyramide,wahre_groesse #Verzerrung/Verkürzung im Schrägbild steckt in wahre_groesse; Zeichnen selbst nur auf Papier (LK-D 3, F3)
883 91 wahre_groesse #Etappe wahre_groesse neu (LK)
885 73 kreislinie,parallelen,zwei_kreise
886 45 lage,tangente
887 73 sachsituationen,verstehen
888 73 verknuepfen
889 45 umkreis_inkreis
702 29 zusammenfassen,produkte,minusklammer,ausmultiplizieren,aequivalenz
703 2 waage,beide_seiten,klammern
704 3 umformen,umdrehen,intervall
705 2 sach
891 94 vermehrt,vermindert,faktor,zurueck
892 71 jahreszinsen,zinssatz,kapital
893 93 erkennen,graph,produkt
894 93 dreisatz,vervielfachen
895 93 unterscheiden
897 58 mittelwert
898 95 mittel_median,median,kennwerte
899 81 repraesentativ,begriffe,fehlerquellen
900 57 irrefuehrend
902 30 negativer_exponent
903 102 mal_gleiche_basis,gleicher_exponent,potenz_von_potenz,geteilt_gleiche_basis
904 19 zehnerpotenz,vorsilben_gross,vorsilben_klein,gross_wissenschaftlich,klein_wissenschaftlich
906 46 eigenschaften
907 46 verschiebung
908 46 gegenvektor
909 46 vektor_koordinaten #LP-RS-Lücke geschlossen: neue Etappe vektor_koordinaten in 46
910 74 det_berechnen,dreieck,viereck,parallelogramm
911 98 stufen_wechsel,parallel_pruefen
912 98 innenwinkelsumme,aussenwinkel,vieleck,figuren
914 73 kreislinie,parallelen,zwei_kreise
915 45 lage,tangente
916 73 verknuepfen,sachsituationen
917 45 umkreis_inkreis
717 29 zusammenfassen,produkte,minusklammer,ausmultiplizieren,aequivalenz
718 2 waage,beide_seiten,klammern
719 3 umformen,umdrehen,intervall
720 2 sach
919 94 vermehrt,vermindert,faktor
920 71 jahreszinsen,zinssatz,kapital
921 93 erkennen,graph,produkt
922 93 dreisatz,vervielfachen
923 93 unterscheiden
925 58 mittelwert
926 95 median,kennwerte,mittel_median
927 81 repraesentativ,begriffe,fehlerquellen
928 57 irrefuehrend
930 46 vierecke_ordnen
931 44 vierecke,vierecke_konstruieren #Etappe vierecke_konstruieren neu (LK)
933 46 drehung,eigenschaften
934 46 punktspiegelung
935 46 drehung
936 46 drehung,symmetrie
937 46 vektor_drehen #LP-RS-Lücke geschlossen: neue Etappe vektor_drehen in 46
939 91 koerper_symmetrie #Symmetrie von Körpern: neue Etappe (LK-D 2)
940 91 rotation,axialschnitt
941 91 koordinaten
732 29 summe_mal_summe,binomisch,ausmultiplizieren,ausklammern
733 97 ergaenzen,scheitelform,extremwert,mit_faktor,optimierung
734 29 gleichungen_binomisch #Gleichungen mit binomischen Ausdrücken: neue Etappe in 29 (LK-D 2); 2 bleibt Neben
736 31 definitionsmenge
737 5 definitionsmenge,verhaeltnis
943 32 eindeutig,sachzusammenhang
944 32 mengen,funktionswert,wertetabelle,nullstellen,graph_lesen #bisher 33 Haupt, 32 Neben; wie 8 II/III 5/K2
945 33 ablesen,wirkung
946 33 graph_ablesen,ablesen
947 33 aufstellen,zwei_punkte,lage,einsetzen,wirkung,bueschel
948 33 deuten
950 61 begriffe,darstellen #Baumdiagramm/Vierfeldertafel: neue Etappe darstellen (LK-D 3, F3)
951 61 rel_haeufigkeit
953 44 konstruierbar
954 44 planfigur
955 44 kongruenzsatz
956 46 vierecke_ordnen
957 44 vierecke,vierecke_konstruieren
959 91 pyramide,wahre_groesse #Verzerrungswinkel/-maßstab steckt in wahre_groesse (LK-D 3, F3)
960 91 wahre_groesse
747 29 summe_mal_summe,binomisch,ausmultiplizieren,ausklammern
748 97 ergaenzen,scheitelform,extremwert,mit_faktor,optimierung
749 29 gleichungen_binomisch #wie 8 I 4/K3
751 31 definitionsmenge
752 5 definitionsmenge,verhaeltnis
962 32 eindeutig,sachzusammenhang
963 32 mengen,funktionswert,wertetabelle,nullstellen
964 33 proportional
965 33 graph_ablesen
966 33 lage
968 61 begriffe,darstellen #Baumdiagramm/Vierfeldertafel: Etappe darstellen (LK-D 3, F3)
969 61 rel_haeufigkeit
758 20 zahlarten
759 8 reinquadratisch
760 20 teilweise,nenner_rational,zusammenfassen,wurzel_mal
762 47 streckung
763 47 streckung
764 47 flaeche_volumen,streckung
765 47 strahlensatz1,strahlensatz2,anwendung
766 47 streckung_vektor #Etappe streckung_vektor neu (LK)
767 47 bildgerade
768 47 schwerpunkt
769 47 aehnlich
771 54 hypotenuse,kathete,anwendung
772 54 umkehrung
773 54 koordinaten
774 54 anwendung
775 54 raum
776 55 verhaeltnisse,seite,winkel
778 51 umfang,flaeche,verstehen,exakt
779 51 sektor,zusammengesetzt
781 101 cavalieri #Cavalieri: Etappe cavalieri in 101 (LK-D 2); 92 bleibt Neben
782 92 pyr_oberflaeche,kegel_mantel
783 92 pyr_volumen,kegel_volumen,kugel,sachkontext
784 92 sachkontext
786 6 grafisch,einsetzen,gleichsetzen,addition
788 35 scheitel,parameter
789 35 bestimmen,umformen
790 35 scheitel,punkte
791 35 extremwert
792 35 parameter
793 8 loesungsformel,diskriminante,ergaenzung
794 8 loesungsformel
795 35 schnittpunkte
796 13 definitionsmenge,quadrieren,isolieren,probe,zwei_seiten
798 61 grosse_zahlen
799 61 laplace,laplace_pruefen
800 61 begriffe
801 61 gegenereignis
802 61 laplace
971 20 zahlarten
804 8 reinquadratisch
972 20 teilweise,zusammenfassen
974 47 streckung
975 47 streckung,flaeche_volumen
976 47 strahlensatz1,strahlensatz2,anwendung
978 54 hypotenuse,kathete,anwendung
979 54 umkehrung
980 54 koordinaten
981 54 anwendung
982 54 raum
983 55 verhaeltnisse,seite,winkel
985 51 umfang,flaeche,exakt
986 51 sektor,zusammengesetzt
988 33 ablesen,wirkung
989 33 graph_ablesen,aufstellen
990 33 aufstellen,zwei_punkte,lage,bueschel
991 33 deuten
815 6 grafisch,einsetzen,gleichsetzen,addition
993 61 grosse_zahlen
994 61 laplace,laplace_pruefen
995 61 begriffe
996 61 gegenereignis
997 61 laplace
819 56 einheitskreis
820 56 einheitskreis +55 #Steigungswinkel: Etappe schnittwinkel in 55
821 38 werte,periode
822 56 einheitskreis
823 56 einheitskreis
824 56 additionstheoreme
825 56 sinussatz_seite,sinussatz_winkel,kosinussatz_seite,kosinussatz_winkel,flaeche
826 56 anwendung,satz_waehlen
827 14 sinus,kosinus,tangens,umformen,anwendung
828 49 skalarprodukt
829 49 skalarprodukt,abstand
831 49 bildpunkt,abbildungsmatrix,drehung
832 49 bildpunkt
833 37 punkte
834 49 rechnen
836 96 potenz_wert,zusammenfassen
837 96 nte_wurzel,umwandeln
838 36 negativ,verlauf,umkehrbar,wurzelfunktion
839 36 parameter
841 10 logarithmus,mit_log_loesen,potenzregel
842 37 graph,logfunktion
843 37 modell,faktor,linear_oder_exponentiell
845 62 baum_ergaenzen,pfad_mult
846 62 pfad_mult,pfad_add,gegenereignis
999 56 einheitskreis
1000 56 einheitskreis +55 #Steigungswinkel: Etappe schnittwinkel in 55
1001 38 werte,periode
1002 56 einheitskreis
1003 56 sinussatz_seite,sinussatz_winkel,kosinussatz_seite,kosinussatz_winkel,flaeche
1004 56 anwendung
1006 91 rotation,axialschnitt
1007 101 cavalieri #wie 9 I 5/K1
1008 92 pyr_oberflaeche,kegel_mantel
1009 92 pyr_volumen,kegel_volumen,kugel,sachkontext
1010 92 sachkontext
852 10 mit_log_loesen,logarithmus
1012 37 werte,graph,linear_oder_exponentiell
1013 37 modell,faktor
855 35 scheitel,parameter
856 35 bestimmen,umformen
857 35 scheitel,punkte
858 35 extremwert
859 8 loesungsformel,diskriminante,ergaenzung,faktorisieren,ausklammern
860 8 loesungsformel
1015 62 baum_ergaenzen,pfad_mult
1016 62 pfad_mult,pfad_add
"""

GYM = """
3 15 unendlich,ziffern_zu_zahlwort,zahlwort_zu_ziffern
4 15 stellenwert,roemisch_schreiben,roemisch_system
5 15 strahl_ablesen,strahl_eintragen,vergleichen
6 15 runden_regel,runden_uebertrag,runden_sinnvoll
7 16 deuten,sach
8 16 zahlengerade,ordnen,betrag
9 16 verstehen #bisher ohne Zuordnung
11 16 schriftlich_plus_minus
12 16 addieren,subtrahieren,ketten
13 1 zwei_schritte,probe +16 #Haupt bleibt 1 (Kind in Gym 5); Etappe umkehraufgabe in 16 ist inhaltsgleich
14 18 vorteil,differenz_summe
15 18 klammern,termaufbau
17 42 koordinaten,strecken #bisher ohne Zuordnung
18 42 lagebeziehungen,kreis_lage #bisher ohne Zuordnung
19 73 kreislinie,parallelen,zwei_kreise,verknuepfen #Ortslinien: 73 statt 42
20 42 winkelarten
21 42 vierecke #bisher ohne Zuordnung
24 18 schriftlich,schriftlich_geteilt,ueberschlag
25 17 primfaktoren,endziffer,quersumme,teiler,primzahl
26 60 zaehlprinzip,baumdiagramm,systematisch,grenzen
27 18 mal_ganz,geteilt_ganz
28 67 schreibweise,berechnen,quadrat,zehner,negativ
29 1 zwei_schritte,probe +18 #Haupt bleibt 1; Etappe umkehraufgabe_mal in 18 ist inhaltsgleich
31 18 termaufbau,klammern
32 18 punkt_strich
33 18 verteilen,vorteil,kopfrechnen
34 18 sach
35 18 sach,ueberschlag
38 25 laenge,masse,zeit,kommaschreibweise
39 25 rechnen
40 25 schaetzen
41 26 einheit,dreisatz,sach,erkennen
42 25 massstab
44 50 einheitsquadrate,rechteck
45 50 einheiten,kommaschreibweise
46 50 verstehen,sachaufgaben
47 50 zerlegen
48 53 oberflaeche,zusammengesetzt,quader
51 21 anteil_bestimmen,bruchteil_von
52 21 bruchteil_von,ganzes_bestimmen
53 21 erweitern,kuerzen,ggt
54 21 vergleichen,kgv
55 22 merkwerte +24 #bisher ohne Zuordnung
56 21 zahlbereiche
57 21 zahlenstrahl,zahlbereiche
59 22 stellenwerte
60 22 runden
61 21 anteil_bestimmen
62 22 periodisch,bruch_zu_dezimal
63 22 bruch_zu_dezimal,dezimal_zu_bruch,merkwerte
64 22 vergleichen_ordnen,verstehen
66 23 brueche_plus_minus
67 23 brueche_plus_minus,dezimal_plus_minus,vorzeichen
68 23 rechenvorteile
69 23 gemischt
70 23 fehler_finden
72 23 brueche_mal,brueche_geteilt,dezimal_mal,dezimal_geteilt
73 23 potenzen #bisher 67 (Haupt); Etappe Potenzen von Brüchen in 23
74 30 negativer_exponent,potenz_begriff
75 19 negativer_exponent,klein_wissenschaftlich,vorsilben_klein #bisher 30 Haupt, 19 Neben
76 23 rechenvorteile
78 23 gemischt
79 23 gemischt
80 23 rechenvorteile
81 23 sach
82 23 sach
85 99 parallelogramm,dreieck,trapez
86 99 rueckwaerts,zusammengesetzt
87 99 zusammengesetzt,verstehen
88 99 verstehen
89 99 oberflaeche #bisher 53 Haupt
91 100 einheitswuerfel,quader
92 100 einheitswuerfel,einheiten
93 100 einheiten,liter
94 100 quader,rueckwaerts
95 100 verstehen
96 100 zusammengesetzt
98 24 prozentwert,prozentsatz,grundwert,rabatt_aufschlag
99 24 verstehen
100 24 prozent_bedeutung +57
101 57 absolute_haeufigkeit,relative_haeufigkeit
102 57 saeulendiagramm,kreisdiagramm
103 57 irrefuehrend,tabelle_auswerten
104 58 mittelwert,mittel_tabelle,mittel_rueckwaerts
107 28 uebersetzen,sachsituation,deuten
108 28 termwert +30
109 28 termwert
110 28 struktur
112 102 mal_gleiche_basis,gleicher_exponent,potenz_von_potenz,geteilt_gleiche_basis,anwenden #bisher 30 Haupt
113 29 zusammenfassen,produkte,minusklammer,aequivalenz
114 29 aequivalenz
115 29 ausklammern,ausmultiplizieren
116 29 binomisch,summe_mal_summe
117 29 aequivalenz +28
120 46 achsenspiegelung,punktspiegelung,symmetrie
121 46 mittelsenkrechte,winkelhalbierende
122 46 mittelsenkrechte +73
123 46 vierecke_ordnen +44
124 46 symmetrie
126 98 scheitel_neben,stufen_wechsel
127 98 innenwinkelsumme
128 98 vieleck
129 98 figuren,aussenwinkel
130 98 parallel_pruefen
132 2 sach
133 2 waage,beide_seiten,klammern,sonderfaelle
134 2 probe
135 2 sach
136 94 faktor,vermehrt,vermindert,zurueck,prozentsatz,mehrfach
137 94 argumente
139 95 median,mittel_median
140 95 quartile,kennwerte
141 95 boxplot
142 95 vergleichen
144 44 kongruenzsatz
145 44 kongruenzsatz,konstruierbar
146 44 gleichschenklig
147 44 satz_kehrsatz
148 45 beweis,umkreis_inkreis
149 45 thales,umkehrung
150 45 tangente,lage
151 44 planfigur,konstruierbar
152 44 planfigur
154 32 wertetabelle,mengen,sachzusammenhang
155 32 eindeutig
156 32 eindeutig
157 32 graph_lesen
158 32 nullstellen,punkt_graph
159 32 sachzusammenhang
161 33 ablesen,wirkung
162 33 graph_ablesen,ablesen
163 33 aufstellen,zwei_punkte
164 33 schnittpunkte
165 33 schnittpunkte
166 33 deuten
167 3 umformen,umdrehen,intervall,grafisch
168 33 proportional
170 34 definitionsmenge,achsenpunkte
171 34 parameter
172 34 asymptoten,beurteilen
173 93 erkennen,produkt,graph,unterscheiden,dreisatz
175 31 definitionsmenge,kuerzen,erweitern
176 31 addieren,multiplizieren,fehler_finden
177 103 warum_gilt,gleiche_basis_ganz,exponent_und_potenz,terme_vereinfachen #bisher 30 Haupt
178 5 definitionsmenge,ein_bruch,ueber_kreuz,hauptnenner,scheinloesung,graphisch
179 4 ein_schritt,zwei_schritte,einsetzen,geometrie
181 61 begriffe,gegenereignis
182 61 rel_haeufigkeit
183 61 grosse_zahlen
184 61 laplace_pruefen
185 61 laplace,darstellen +60 #Baumdiagramm: Etappe darstellen (LK-D 3, F3)
187 6 sachaufgabe
188 6 grafisch,einsetzen,gleichsetzen,addition
189 6 verfahren
190 6 loesbarkeit,pruefen
192 51 umfang,flaeche
193 51 exakt
194 51 verstehen
195 52 prisma,netz,zylinder,schraegbild
196 101 zylinder_oberflaeche
197 101 prisma_volumen,zylinder_volumen
198 101 sach,prisma_oberflaeche,prisma_umstellen,verstehen +51
200 68 quadratwurzel,wurzel_dezimal +20
201 68 abschaetzen +20
202 20 zahlarten,irrational_beweis #indirekter Beweis √2: neue Etappe irrational_beweis (LK-D 4, A1)
203 20 zahlarten
204 20 heron,eingrenzen
205 20 wurzel_mal,zusammenfassen
206 20 nenner_rational,teilweise
207 68 wurzel_deuten
210 35 parameter,spiegeln,scheitel
211 35 nullstellen
212 35 umformen
213 35 scheitel,punkte
214 8 reinquadratisch,ausklammern,faktorisieren,ergaenzung,loesungsformel
215 8 diskriminante
216 35 bestimmen +8
218 7 pruefen,stufenform,eliminieren,loesen
219 35 bestimmen
220 8 bruchgleichung #bisher 5 Haupt (Gym 8)
221 35 extremwert
222 35 extremwert
224 63 elemente,schnitt,venn,vierfeld
225 63 verknuepfen,mengen_verstehen
226 63 tafel_wkeit
227 63 additionssatz
228 63 tafel_wkeit,additionssatz,verstehen
230 47 aehnlich
231 47 strahlensatz1,strahlensatz2,anwendung
232 47 anwendung
233 47 flaeche_volumen
235 36 werte,symmetrie,verlauf,parameter
236 9 gerade,ungerade,umformen
237 9 anzahl
238 96 umwandeln,potenz_wert,nte_wurzel
239 96 zusammenfassen
241 54 umkehrung
242 54 hypotenuse,kathete
243 54 anwendung,koordinaten,raum
246 55 seiten,verhaeltnisse
247 55 seite,winkel
248 55 beziehungen
249 55 anwendung
251 56 einheitskreis
252 56 einheitskreis
253 14 sinus,kosinus,anzahl
254 56 sinussatz_seite,sinussatz_winkel
255 56 kosinussatz_seite,kosinussatz_winkel
256 56 satz_waehlen,anwendung,flaeche
258 37 linear_oder_exponentiell,faktor
259 37 graph,werte
260 10 logarithmus
261 10 gleiche_basis,mit_log_loesen,potenzregel
262 37 modell +10
264 62 baum_ergaenzen,ohne_zuruecklegen
265 62 pfad_mult,pfad_add,gegenereignis,unabhaengig
266 64 zufallsgeraet,regel,zufallsziffern,auswerten,beurteilen +62
267 64 monte_carlo +62
269 38 bogenmass
270 38 werte +14
271 38 periode
272 38 periode,eigenschaften
273 38 parameter,verschiebung_x
274 38 zuordnen
275 38 anwendung
277 39 grad,randverhalten,ausmultiplizieren
278 11 ausklammern,nullprodukt,substitution,vielfachheit
279 39 graph_term,term_bestimmen
280 39 symmetrie
282 91 pyramide #bisher 92 Haupt, 91 Neben
283 91 rotation #bisher 92 Haupt, 91 Neben
284 92 kegel_mantel
285 101 cavalieri #bisher 53 Haupt; schiefe Prismen/Cavalieri: neue Etappe cavalieri (LK-D 2)
286 92 pyr_volumen
287 92 kegel_volumen
288 92 kugel
289 92 sachkontext,verstehen
"""

IB = """
528 15 stellenwert,zahlwort_zu_ziffern,ziffern_zu_zahlwort,vergleichen
529 15 stellenwert
530 15 dualsystem
531 67 schreibweise,berechnen,quadrat
532 17 teiler,vielfache,primzahl,primfaktoren
533 17 primfaktoren +21
534 17 endziffer,quersumme,neunerregel
535 18 punkt_strich,klammern
536 15 roemisch_schreiben,roemisch_system
537 24 prozent_bedeutung
538 24 prozent_bedeutung
539 24 prozent_bedeutung
540 24 prozentwert,prozentsatz,grundwert
541 24 rabatt_aufschlag
542 28 muster
543 29 zusammenfassen,produkte
544 28 muster,uebersetzen
545 32 wertetabelle,funktionswert
546 1 waage,zwei_schritte,probe,aufstellen
547 28 muster
548 42 lagebeziehungen
549 42 winkelarten
550 43 kreuzung,ergaenzen,um_punkt
551 42 verstehen #teilweise: Dreiecksarten ohne eigene Etappe
552 98 innenwinkelsumme,aussenwinkel #bisher 43 Haupt; Dreieckswinkel stehen in 98
553 21 anteil_bestimmen,bruchteil_von,gemischte_zahlen
554 21 vergleichen,erweitern,kuerzen
555 23 brueche_mal,brueche_geteilt
556 23 brueche_plus_minus
557 23 gemischt
558 57 absolute_haeufigkeit
559 57 tabelle_auswerten,saeulendiagramm
560 57 saeulendiagramm,kreisdiagramm
561 57 tabelle_auswerten
562 57 irrefuehrend
563 63 elemente,schnitt,venn,mengen_verstehen -83 #83 stillgelegt, Mengen-Etappen in 63
564 50 zerlegen,rechteck
565 53 quader +100 #Volumen-Etappen in 100/101 (ohne IB-Klasse)
566 53 quader +101
567 53 oberflaeche,quader
568 53 verstehen
569 21 verhaeltnis_kuerzen -27 #27 stillgelegt
570 21 gleichwertig -27
571 21 verhaeltnis_kuerzen,gleichwertig -27
572 26 pruefen,einheit,dreisatz -27
573 26 erkennen,vervielfachen -27
574 61 begriffe
575 61 begriffe
576 61 laplace
577 61 laplace
578 61 gegenereignis
579 61 rel_haeufigkeit,grosse_zahlen,laplace_pruefen
580 61 grosse_zahlen
581 16 deuten,zahlengerade,ordnen
582 16 betrag
583 42 koordinaten
584 18 mal_ganz,geteilt_ganz #bisher 16 Haupt
585 16 addieren,subtrahieren,ketten
586 18 punkt_strich,klammern
587 28 struktur
588 29 zusammenfassen,produkte,ausmultiplizieren
589 28 uebersetzen,sachsituation
590 2 waage,beide_seiten,klammern
591 2 sach
592 2 sach
593 3 intervall
594 3 umformen,umdrehen
595 50 sachaufgaben +99 #Trapez-Etappe in 99 (ohne IB-Klasse)
596 50 zerlegen +99
597 51 umfang,flaeche
598 53 oberflaeche
599 53 quader +100
600 53 quader +101
601 26 einheit -27
602 25 laenge,masse,zeit
603 25 rechnen
604 26 einheit,sach -27
605 26 sach -27
606 26 aenderung -27
607 57 tabelle_auswerten
608 58 mittelwert
609 58 mittelwert
610 95 quartile,kennwerte
611 95 boxplot
612 20 zahlarten
613 20 zahlarten
614 30 potenz_begriff,negativer_exponent
615 19 gross_wissenschaftlich,klein_wissenschaftlich
616 33 ablesen,graph_ablesen
617 33 zwei_punkte,aufstellen
618 33 schnittpunkte,lage
619 6 pruefen,grafisch
620 2 waage,beide_seiten,klammern,sonderfaelle
621 6 einsetzen,gleichsetzen,addition
622 6 sachaufgabe
623 52 prisma,netz,ansichten
624 52 zylinder #bisher 51 Haupt
625 92 kegel_volumen,kegel_mantel
626 92 pyr_volumen,pyr_oberflaeche
627 92 kugel
628 46 achsenspiegelung,verschiebung,drehung
629 98 parkett #bisher 46 Haupt
630 46 eigenschaften,achsenspiegelung,punktspiegelung,drehung,verschiebung
631 47 streckung,aehnlich
632 44 kongruenzsatz,konstruierbar
633 44 satz_kehrsatz
634 54 hypotenuse,kathete,umkehrung
635 55 seiten,verhaeltnisse,seite,winkel
636 59 ablesen
637 59 zusammenhang
638 59 gerade,ausreisser
639 59 kausal
640 - - #Wiederholung MYP 3, kein eigener Inhalt
641 29 binomisch,ausklammern,summe_mal_summe
642 32 eindeutig,mengen,funktionswert
643 33 aufstellen,schnittpunkte,lage,deuten
644 6 grafisch,einsetzen,addition
645 49 rechnen,inverse
646 35 scheitel,nullstellen,schnittpunkte
647 47 aehnlich,strahlensatz1,strahlensatz2
648 44 kongruenzsatz
649 46 verschiebung,achsenspiegelung,drehung
650 45 thales,tangente,lage
651 55 seite,winkel,anwendung
652 37 werte,graph,logfunktion +36 -77
653 92 pyr_volumen,kegel_volumen,kugel +101 #bisher 53 Haupt
654 56 einheitskreis,flaeche,sinussatz_seite,sinussatz_winkel
655 20 zahlarten,teilweise,nenner_rational
656 76 arithmetisch,geometrisch,summenzeichen,arith,geom -41 #41 stillgelegt
657 63 verknuepfen,additionssatz,vierfeld,tafel_wkeit
658 59 ablesen,zusammenhang,gerade
659 65 grundbegriffe,euler,kuerzester,spannbaum
660 - - #Wiederholung MYP 3, kein eigener Inhalt
661 29 binomisch,ausklammern,summe_mal_summe
662 32 eindeutig,mengen,funktionswert
663 33 aufstellen,lage,schnittpunkte
664 6 einsetzen,addition,loesbarkeit
665 49 rechnen,inverse
666 39 grad,ausmultiplizieren,nullstellen,graph_term
667 47 aehnlich,strahlensatz1,strahlensatz2
668 44 kongruenzsatz
669 49 bildpunkt,abbildungsmatrix,drehung
670 45 thales,tangente,lage,umkreis_inkreis
671 55 seite,winkel,anwendung
672 37 werte,graph,logfunktion -77
673 92 pyr_volumen,kegel_volumen,kugel #bisher 53 Haupt
674 56 einheitskreis,sinussatz_seite,kosinussatz_seite
675 20 zahlarten,teilweise,nenner_rational
676 76 arithmetisch,geometrisch,summenzeichen,arith,geom -41
677 63 bedingt,vierfeld,tafel_wkeit +62 -82 #82 stillgelegt
678 79 abweichung,varianz,sigma,deuten
679 65 grundbegriffe,euler,kuerzester,spannbaum
680 63 elemente,schnitt,verknuepfen,venn -83
681 63 verknuepfen,additionssatz
682 63 bedingt,rueckschluss +62 -82
683 28 uebersetzen,sachsituation
684 44 kongruenzsatz,konstruierbar
685 33 zwei_punkte,aufstellen
"""
