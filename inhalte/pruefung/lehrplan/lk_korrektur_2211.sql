-- LK-D (22.11.2026): Zuordnung Gymnasium 5–10 und IB MYP 1–5 je Lehrplanpunkt, dazu Nachtrag Realschule (Gruppe I, RS 5/6).
-- Bericht: inhalte/pruefung/lehrplan/lk_pruefung_2211.md · Daten je Punkt (rolle, etappen): lk_daten_2211.json.
-- Erst NACH rs_korrektur_2211.sql einspielen (Schritt 0 prüft das). In EINER Transaktion (psql -1).
-- Nur INSERT und UPDATE auf schule.zuordnung und schule.eintrag. Kein DROP, kein DELETE; schule.thema bleibt unverändert.
-- Veraltete Zuordnungen (stillgelegte oder ersetzte Themen) werden auf Nebenbezug mit pruefstatus 'klaerungsbedarf' gesetzt.
-- Rolle (neu/weitergeführt) und Etappen stehen in begruendung der geänderten Zeilen; die Felder rolle/etappen füllt LK-S aus der JSON.
-- Klassen ändern sich nicht (Rauchtest c, simuliert und im Probelauf geprüft) – wichtig, weil die Kinder im Gymnasium lernen.

do $$ begin
  if not exists (select 1 from schule.zuordnung where eintrag_id = 864 and thema_id = 30 and bezug = 'haupt') then
    raise exception 'Schritt 0: rs_korrektur_2211.sql ist noch nicht eingespielt';
  end if;
  perform set_config('lk.jahrgang_vorher', (select jsonb_object_agg(id::text, schule.thema_jahrgang(id)) from schule.thema)::text, true);
end $$;

-- 1) Hauptbezüge, die nicht Haupt bleiben, zuerst auf Neben (eindeutiger Hauptbezug je Eintrag)
update schule.zuordnung set bezug = 'neben' where eintrag_id = 944 and thema_id = 33 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 19 and thema_id = 42 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 73 and thema_id = 67 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 75 and thema_id = 30 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 89 and thema_id = 53 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 112 and thema_id = 30 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 177 and thema_id = 30 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 220 and thema_id = 5 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 282 and thema_id = 92 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 283 and thema_id = 92 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 285 and thema_id = 53 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 552 and thema_id = 43 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 563 and thema_id = 83 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 569 and thema_id = 27 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 570 and thema_id = 27 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 571 and thema_id = 27 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 572 and thema_id = 27 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 573 and thema_id = 27 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 584 and thema_id = 16 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 601 and thema_id = 27 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 604 and thema_id = 27 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 605 and thema_id = 27 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 606 and thema_id = 27 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 624 and thema_id = 51 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 629 and thema_id = 46 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 653 and thema_id = 53 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 656 and thema_id = 41 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 673 and thema_id = 53 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 676 and thema_id = 41 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 680 and thema_id = 83 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 682 and thema_id = 82 and bezug = 'haupt';

-- 2) Veraltete Zuordnungen kennzeichnen (kein Löschen)
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 947 and thema_id = 78 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 563 and thema_id = 83 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 569 and thema_id = 27 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 570 and thema_id = 27 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 571 and thema_id = 27 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 572 and thema_id = 27 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 573 and thema_id = 27 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 601 and thema_id = 27 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 604 and thema_id = 27 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 605 and thema_id = 27 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 606 and thema_id = 27 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 652 and thema_id = 77 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 656 and thema_id = 41 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 672 and thema_id = 77 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 676 and thema_id = 41 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 677 and thema_id = 82 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 680 and thema_id = 83 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 682 and thema_id = 82 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');

-- 3) Nebenbezüge zu Hauptbezügen
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: neu; Etappen: mengen, funktionswert, wertetabelle, nullstellen, graph_lesen; bisher 33 Haupt, 32 Neben; wie 8 II/III 5/K2', pruefstatus = 'geprueft' where eintrag_id = 944 and thema_id = 32 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: neu; Etappen: kreislinie, parallelen, zwei_kreise, verknuepfen; Ortslinien: 73 statt 42', pruefstatus = 'geprueft' where eintrag_id = 19 and thema_id = 73 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: neu; Etappen: negativer_exponent, klein_wissenschaftlich, vorsilben_klein; bisher 30 Haupt, 19 Neben', pruefstatus = 'geprueft' where eintrag_id = 75 and thema_id = 19 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: neu; Etappen: bruchgleichung; bisher 5 Haupt (Gym 8)', pruefstatus = 'geprueft' where eintrag_id = 220 and thema_id = 8 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: neu; Etappen: pyramide; bisher 92 Haupt, 91 Neben', pruefstatus = 'geprueft' where eintrag_id = 282 and thema_id = 91 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: neu; Etappen: rotation; bisher 92 Haupt, 91 Neben', pruefstatus = 'geprueft' where eintrag_id = 283 and thema_id = 91 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: neu; Etappen: pruefen, einheit, dreisatz', pruefstatus = 'geprueft' where eintrag_id = 572 and thema_id = 26 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: neu; Etappen: erkennen, vervielfachen', pruefstatus = 'geprueft' where eintrag_id = 573 and thema_id = 26 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: weitergeführt; Etappen: pyr_volumen, kegel_volumen, kugel; bisher 53 Haupt', pruefstatus = 'geprueft' where eintrag_id = 653 and thema_id = 92 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: neu; Etappen: arithmetisch, geometrisch, summenzeichen, arith, geom; 41 stillgelegt', pruefstatus = 'geprueft' where eintrag_id = 656 and thema_id = 76 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: weitergeführt; Etappen: pyr_volumen, kegel_volumen, kugel; bisher 53 Haupt', pruefstatus = 'geprueft' where eintrag_id = 673 and thema_id = 92 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: neu; Etappen: arithmetisch, geometrisch, summenzeichen, arith, geom', pruefstatus = 'geprueft' where eintrag_id = 676 and thema_id = 76 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LK-D 22.11.2026: weitergeführt; Etappen: elemente, schnitt, verknuepfen, venn', pruefstatus = 'geprueft' where eintrag_id = 680 and thema_id = 63 and bezug <> 'haupt';

-- 4) Fehlende Zuordnungen ergänzen
insert into schule.zuordnung (eintrag_id, thema_id, bezug, begruendung, pruefstatus)
select v.e, v.t, v.b, v.g, 'geprueft' from (values
  (297, 15, 'haupt', 'LK-D 22.11.2026: neu; Etappen: dualsystem, roemisch_schreiben; LP-RS-Lücke geschlossen: Etappen stehen in Thema 15'),
  (298, 15, 'haupt', 'LK-D 22.11.2026: neu; Etappen: roemisch_system; LP-RS-Lücke geschlossen'),
  (871, 46, 'haupt', 'LK-D 22.11.2026: weitergeführt; Etappen: vektor_koordinaten; LP-RS-Lücke geschlossen: neue Etappe vektor_koordinaten in 46'),
  (937, 46, 'haupt', 'LK-D 22.11.2026: weitergeführt; Etappen: vektor_drehen; LP-RS-Lücke geschlossen: neue Etappe vektor_drehen in 46'),
  (820, 55, 'neben', 'LK-D 22.11.2026: Nebenbezug; Steigungswinkel: Etappe schnittwinkel in 55'),
  (9, 16, 'haupt', 'LK-D 22.11.2026: neu; Etappen: verstehen; bisher ohne Zuordnung'),
  (13, 16, 'neben', 'LK-D 22.11.2026: Nebenbezug; Haupt bleibt 1 (Kind in Gym 5); Etappe umkehraufgabe in 16 ist inhaltsgleich'),
  (17, 42, 'haupt', 'LK-D 22.11.2026: neu; Etappen: koordinaten, strecken; bisher ohne Zuordnung'),
  (18, 42, 'haupt', 'LK-D 22.11.2026: neu; Etappen: lagebeziehungen, kreis_lage; bisher ohne Zuordnung'),
  (21, 42, 'haupt', 'LK-D 22.11.2026: neu; Etappen: vierecke; bisher ohne Zuordnung'),
  (29, 18, 'neben', 'LK-D 22.11.2026: Nebenbezug; Haupt bleibt 1; Etappe umkehraufgabe_mal in 18 ist inhaltsgleich'),
  (31, 18, 'haupt', 'LK-D 22.11.2026: neu; Etappen: termaufbau, klammern'),
  (32, 18, 'haupt', 'LK-D 22.11.2026: neu; Etappen: punkt_strich'),
  (33, 18, 'haupt', 'LK-D 22.11.2026: neu; Etappen: verteilen, vorteil, kopfrechnen'),
  (34, 18, 'haupt', 'LK-D 22.11.2026: neu; Etappen: sach'),
  (35, 18, 'haupt', 'LK-D 22.11.2026: neu; Etappen: sach, ueberschlag'),
  (38, 25, 'haupt', 'LK-D 22.11.2026: neu; Etappen: laenge, masse, zeit, kommaschreibweise'),
  (39, 25, 'haupt', 'LK-D 22.11.2026: neu; Etappen: rechnen'),
  (40, 25, 'haupt', 'LK-D 22.11.2026: neu; Etappen: schaetzen'),
  (42, 25, 'haupt', 'LK-D 22.11.2026: neu; Etappen: massstab'),
  (55, 22, 'haupt', 'LK-D 22.11.2026: neu; Etappen: merkwerte; bisher ohne Zuordnung'),
  (55, 24, 'neben', 'LK-D 22.11.2026: Nebenbezug; bisher ohne Zuordnung'),
  (59, 22, 'haupt', 'LK-D 22.11.2026: neu; Etappen: stellenwerte'),
  (60, 22, 'haupt', 'LK-D 22.11.2026: neu; Etappen: runden'),
  (62, 22, 'haupt', 'LK-D 22.11.2026: neu; Etappen: periodisch, bruch_zu_dezimal'),
  (63, 22, 'haupt', 'LK-D 22.11.2026: neu; Etappen: bruch_zu_dezimal, dezimal_zu_bruch, merkwerte'),
  (64, 22, 'haupt', 'LK-D 22.11.2026: neu; Etappen: vergleichen_ordnen, verstehen'),
  (66, 23, 'haupt', 'LK-D 22.11.2026: neu; Etappen: brueche_plus_minus'),
  (67, 23, 'haupt', 'LK-D 22.11.2026: neu; Etappen: brueche_plus_minus, dezimal_plus_minus, vorzeichen'),
  (68, 23, 'haupt', 'LK-D 22.11.2026: neu; Etappen: rechenvorteile'),
  (69, 23, 'haupt', 'LK-D 22.11.2026: neu; Etappen: gemischt'),
  (70, 23, 'haupt', 'LK-D 22.11.2026: neu; Etappen: fehler_finden'),
  (73, 23, 'haupt', 'LK-D 22.11.2026: neu; Etappen: potenzen; bisher 67 (Haupt); Etappe Potenzen von Brüchen in 23'),
  (78, 23, 'haupt', 'LK-D 22.11.2026: neu; Etappen: gemischt'),
  (79, 23, 'haupt', 'LK-D 22.11.2026: neu; Etappen: gemischt'),
  (80, 23, 'haupt', 'LK-D 22.11.2026: neu; Etappen: rechenvorteile'),
  (81, 23, 'haupt', 'LK-D 22.11.2026: neu; Etappen: sach'),
  (82, 23, 'haupt', 'LK-D 22.11.2026: neu; Etappen: sach'),
  (85, 99, 'haupt', 'LK-D 22.11.2026: neu; Etappen: parallelogramm, dreieck, trapez'),
  (86, 99, 'haupt', 'LK-D 22.11.2026: neu; Etappen: rueckwaerts, zusammengesetzt'),
  (87, 99, 'haupt', 'LK-D 22.11.2026: neu; Etappen: zusammengesetzt, verstehen'),
  (88, 99, 'haupt', 'LK-D 22.11.2026: neu; Etappen: verstehen'),
  (89, 99, 'haupt', 'LK-D 22.11.2026: neu; Etappen: oberflaeche; bisher 53 Haupt'),
  (91, 100, 'haupt', 'LK-D 22.11.2026: neu; Etappen: einheitswuerfel, quader'),
  (92, 100, 'haupt', 'LK-D 22.11.2026: neu; Etappen: einheitswuerfel, einheiten'),
  (93, 100, 'haupt', 'LK-D 22.11.2026: neu; Etappen: einheiten, liter'),
  (94, 100, 'haupt', 'LK-D 22.11.2026: neu; Etappen: quader, rueckwaerts'),
  (95, 100, 'haupt', 'LK-D 22.11.2026: neu; Etappen: verstehen'),
  (96, 100, 'haupt', 'LK-D 22.11.2026: neu; Etappen: zusammengesetzt'),
  (99, 24, 'haupt', 'LK-D 22.11.2026: neu; Etappen: verstehen'),
  (100, 24, 'haupt', 'LK-D 22.11.2026: neu; Etappen: prozent_bedeutung'),
  (100, 57, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (107, 28, 'haupt', 'LK-D 22.11.2026: neu; Etappen: uebersetzen, sachsituation, deuten'),
  (108, 28, 'haupt', 'LK-D 22.11.2026: neu; Etappen: termwert'),
  (108, 30, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (109, 28, 'haupt', 'LK-D 22.11.2026: neu; Etappen: termwert'),
  (110, 28, 'haupt', 'LK-D 22.11.2026: neu; Etappen: struktur'),
  (112, 102, 'haupt', 'LK-D 22.11.2026: neu; Etappen: mal_gleiche_basis, gleicher_exponent, potenz_von_potenz, geteilt_gleiche_basis, anwenden; bisher 30 Haupt'),
  (113, 29, 'haupt', 'LK-D 22.11.2026: neu; Etappen: zusammenfassen, produkte, minusklammer, aequivalenz'),
  (114, 29, 'haupt', 'LK-D 22.11.2026: neu; Etappen: aequivalenz'),
  (115, 29, 'haupt', 'LK-D 22.11.2026: neu; Etappen: ausklammern, ausmultiplizieren'),
  (116, 29, 'haupt', 'LK-D 22.11.2026: neu; Etappen: binomisch, summe_mal_summe'),
  (117, 29, 'haupt', 'LK-D 22.11.2026: neu; Etappen: aequivalenz'),
  (117, 28, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (120, 46, 'haupt', 'LK-D 22.11.2026: neu; Etappen: achsenspiegelung, punktspiegelung, symmetrie'),
  (121, 46, 'haupt', 'LK-D 22.11.2026: neu; Etappen: mittelsenkrechte, winkelhalbierende'),
  (122, 46, 'haupt', 'LK-D 22.11.2026: neu; Etappen: mittelsenkrechte'),
  (122, 73, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (123, 46, 'haupt', 'LK-D 22.11.2026: neu; Etappen: vierecke_ordnen'),
  (123, 44, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (124, 46, 'haupt', 'LK-D 22.11.2026: neu; Etappen: symmetrie'),
  (126, 98, 'haupt', 'LK-D 22.11.2026: neu; Etappen: scheitel_neben, stufen_wechsel'),
  (127, 98, 'haupt', 'LK-D 22.11.2026: neu; Etappen: innenwinkelsumme'),
  (128, 98, 'haupt', 'LK-D 22.11.2026: neu; Etappen: vieleck'),
  (129, 98, 'haupt', 'LK-D 22.11.2026: neu; Etappen: figuren, aussenwinkel'),
  (130, 98, 'haupt', 'LK-D 22.11.2026: neu; Etappen: parallel_pruefen'),
  (144, 44, 'haupt', 'LK-D 22.11.2026: neu; Etappen: kongruenzsatz'),
  (145, 44, 'haupt', 'LK-D 22.11.2026: neu; Etappen: kongruenzsatz, konstruierbar'),
  (146, 44, 'haupt', 'LK-D 22.11.2026: neu; Etappen: gleichschenklig'),
  (147, 44, 'haupt', 'LK-D 22.11.2026: neu; Etappen: satz_kehrsatz'),
  (151, 44, 'haupt', 'LK-D 22.11.2026: neu; Etappen: planfigur, konstruierbar'),
  (152, 44, 'haupt', 'LK-D 22.11.2026: neu; Etappen: planfigur'),
  (154, 32, 'haupt', 'LK-D 22.11.2026: neu; Etappen: wertetabelle, mengen, sachzusammenhang'),
  (155, 32, 'haupt', 'LK-D 22.11.2026: neu; Etappen: eindeutig'),
  (156, 32, 'haupt', 'LK-D 22.11.2026: neu; Etappen: eindeutig'),
  (157, 32, 'haupt', 'LK-D 22.11.2026: neu; Etappen: graph_lesen'),
  (158, 32, 'haupt', 'LK-D 22.11.2026: neu; Etappen: nullstellen, punkt_graph'),
  (159, 32, 'haupt', 'LK-D 22.11.2026: neu; Etappen: sachzusammenhang'),
  (177, 103, 'haupt', 'LK-D 22.11.2026: neu; Etappen: warum_gilt, gleiche_basis_ganz, exponent_und_potenz, terme_vereinfachen; bisher 30 Haupt'),
  (181, 61, 'haupt', 'LK-D 22.11.2026: neu; Etappen: begriffe, gegenereignis'),
  (183, 61, 'haupt', 'LK-D 22.11.2026: neu; Etappen: grosse_zahlen'),
  (184, 61, 'haupt', 'LK-D 22.11.2026: neu; Etappen: laplace_pruefen'),
  (185, 61, 'haupt', 'LK-D 22.11.2026: neu; Etappen: laplace'),
  (185, 60, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (192, 51, 'haupt', 'LK-D 22.11.2026: neu; Etappen: umfang, flaeche'),
  (193, 51, 'haupt', 'LK-D 22.11.2026: neu; Etappen: exakt'),
  (194, 51, 'haupt', 'LK-D 22.11.2026: neu; Etappen: verstehen'),
  (196, 101, 'haupt', 'LK-D 22.11.2026: neu; Etappen: zylinder_oberflaeche'),
  (197, 101, 'haupt', 'LK-D 22.11.2026: neu; Etappen: prisma_volumen, zylinder_volumen'),
  (198, 101, 'haupt', 'LK-D 22.11.2026: neu; Etappen: sach, prisma_oberflaeche, prisma_umstellen, verstehen'),
  (198, 51, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (200, 68, 'haupt', 'LK-D 22.11.2026: neu; Etappen: quadratwurzel, wurzel_dezimal'),
  (200, 20, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (201, 68, 'haupt', 'LK-D 22.11.2026: neu; Etappen: abschaetzen'),
  (201, 20, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (202, 20, 'haupt', 'LK-D 22.11.2026: neu; Etappen: zahlarten'),
  (203, 20, 'haupt', 'LK-D 22.11.2026: neu; Etappen: zahlarten'),
  (204, 20, 'haupt', 'LK-D 22.11.2026: neu; Etappen: heron, eingrenzen'),
  (205, 20, 'haupt', 'LK-D 22.11.2026: neu; Etappen: wurzel_mal, zusammenfassen'),
  (206, 20, 'haupt', 'LK-D 22.11.2026: neu; Etappen: nenner_rational, teilweise'),
  (207, 68, 'haupt', 'LK-D 22.11.2026: neu; Etappen: wurzel_deuten'),
  (210, 35, 'haupt', 'LK-D 22.11.2026: neu; Etappen: parameter, spiegeln, scheitel'),
  (212, 35, 'haupt', 'LK-D 22.11.2026: neu; Etappen: umformen'),
  (213, 35, 'haupt', 'LK-D 22.11.2026: neu; Etappen: scheitel, punkte'),
  (216, 35, 'haupt', 'LK-D 22.11.2026: neu; Etappen: bestimmen'),
  (216, 8, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (222, 35, 'haupt', 'LK-D 22.11.2026: neu; Etappen: extremwert'),
  (224, 63, 'haupt', 'LK-D 22.11.2026: neu; Etappen: elemente, schnitt, venn, vierfeld'),
  (225, 63, 'haupt', 'LK-D 22.11.2026: neu; Etappen: verknuepfen, mengen_verstehen'),
  (226, 63, 'haupt', 'LK-D 22.11.2026: neu; Etappen: tafel_wkeit'),
  (227, 63, 'haupt', 'LK-D 22.11.2026: neu; Etappen: additionssatz'),
  (228, 63, 'haupt', 'LK-D 22.11.2026: neu; Etappen: tafel_wkeit, additionssatz, verstehen'),
  (230, 47, 'haupt', 'LK-D 22.11.2026: neu; Etappen: aehnlich'),
  (231, 47, 'haupt', 'LK-D 22.11.2026: neu; Etappen: strahlensatz1, strahlensatz2, anwendung'),
  (233, 47, 'haupt', 'LK-D 22.11.2026: neu; Etappen: flaeche_volumen'),
  (235, 36, 'haupt', 'LK-D 22.11.2026: neu; Etappen: werte, symmetrie, verlauf, parameter'),
  (241, 54, 'haupt', 'LK-D 22.11.2026: neu; Etappen: umkehrung'),
  (242, 54, 'haupt', 'LK-D 22.11.2026: neu; Etappen: hypotenuse, kathete'),
  (243, 54, 'haupt', 'LK-D 22.11.2026: neu; Etappen: anwendung, koordinaten, raum'),
  (246, 55, 'haupt', 'LK-D 22.11.2026: neu; Etappen: seiten, verhaeltnisse'),
  (247, 55, 'haupt', 'LK-D 22.11.2026: neu; Etappen: seite, winkel'),
  (248, 55, 'haupt', 'LK-D 22.11.2026: neu; Etappen: beziehungen'),
  (249, 55, 'haupt', 'LK-D 22.11.2026: neu; Etappen: anwendung'),
  (251, 56, 'haupt', 'LK-D 22.11.2026: neu; Etappen: einheitskreis'),
  (252, 56, 'haupt', 'LK-D 22.11.2026: neu; Etappen: einheitskreis'),
  (254, 56, 'haupt', 'LK-D 22.11.2026: neu; Etappen: sinussatz_seite, sinussatz_winkel'),
  (255, 56, 'haupt', 'LK-D 22.11.2026: neu; Etappen: kosinussatz_seite, kosinussatz_winkel'),
  (256, 56, 'haupt', 'LK-D 22.11.2026: neu; Etappen: satz_waehlen, anwendung, flaeche'),
  (258, 37, 'haupt', 'LK-D 22.11.2026: neu; Etappen: linear_oder_exponentiell, faktor'),
  (259, 37, 'haupt', 'LK-D 22.11.2026: neu; Etappen: graph, werte'),
  (260, 10, 'haupt', 'LK-D 22.11.2026: neu; Etappen: logarithmus'),
  (262, 37, 'haupt', 'LK-D 22.11.2026: neu; Etappen: modell'),
  (262, 10, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (264, 62, 'haupt', 'LK-D 22.11.2026: neu; Etappen: baum_ergaenzen, ohne_zuruecklegen'),
  (265, 62, 'haupt', 'LK-D 22.11.2026: neu; Etappen: pfad_mult, pfad_add, gegenereignis, unabhaengig'),
  (266, 64, 'haupt', 'LK-D 22.11.2026: neu; Etappen: zufallsgeraet, regel, zufallsziffern, auswerten, beurteilen'),
  (266, 62, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (267, 64, 'haupt', 'LK-D 22.11.2026: neu; Etappen: monte_carlo'),
  (267, 62, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (269, 38, 'haupt', 'LK-D 22.11.2026: neu; Etappen: bogenmass'),
  (270, 38, 'haupt', 'LK-D 22.11.2026: neu; Etappen: werte'),
  (270, 14, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (271, 38, 'haupt', 'LK-D 22.11.2026: neu; Etappen: periode'),
  (272, 38, 'haupt', 'LK-D 22.11.2026: neu; Etappen: periode, eigenschaften'),
  (273, 38, 'haupt', 'LK-D 22.11.2026: neu; Etappen: parameter, verschiebung_x'),
  (274, 38, 'haupt', 'LK-D 22.11.2026: neu; Etappen: zuordnen'),
  (275, 38, 'haupt', 'LK-D 22.11.2026: neu; Etappen: anwendung'),
  (277, 39, 'haupt', 'LK-D 22.11.2026: neu; Etappen: grad, randverhalten, ausmultiplizieren'),
  (279, 39, 'haupt', 'LK-D 22.11.2026: neu; Etappen: graph_term, term_bestimmen'),
  (280, 39, 'haupt', 'LK-D 22.11.2026: neu; Etappen: symmetrie'),
  (285, 101, 'haupt', 'LK-D 22.11.2026: weitergeführt; Etappen: prisma_volumen; bisher 53 Haupt (Quader Kl. 5)'),
  (533, 21, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (552, 98, 'haupt', 'LK-D 22.11.2026: neu; Etappen: innenwinkelsumme, aussenwinkel; bisher 43 Haupt; Dreieckswinkel stehen in 98'),
  (563, 63, 'haupt', 'LK-D 22.11.2026: neu; Etappen: elemente, schnitt, venn, mengen_verstehen; 83 stillgelegt, Mengen-Etappen in 63'),
  (565, 100, 'neben', 'LK-D 22.11.2026: Nebenbezug; Volumen-Etappen in 100/101 (ohne IB-Klasse)'),
  (566, 101, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (569, 21, 'haupt', 'LK-D 22.11.2026: weitergeführt; Etappen: verhaeltnis_kuerzen; 27 stillgelegt'),
  (570, 21, 'haupt', 'LK-D 22.11.2026: weitergeführt; Etappen: gleichwertig'),
  (571, 21, 'haupt', 'LK-D 22.11.2026: weitergeführt; Etappen: verhaeltnis_kuerzen, gleichwertig'),
  (584, 18, 'haupt', 'LK-D 22.11.2026: weitergeführt; Etappen: mal_ganz, geteilt_ganz; bisher 16 Haupt'),
  (595, 99, 'neben', 'LK-D 22.11.2026: Nebenbezug; Trapez-Etappe in 99 (ohne IB-Klasse)'),
  (596, 99, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (599, 100, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (600, 101, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (601, 26, 'haupt', 'LK-D 22.11.2026: neu; Etappen: einheit'),
  (604, 26, 'haupt', 'LK-D 22.11.2026: neu; Etappen: einheit, sach'),
  (605, 26, 'haupt', 'LK-D 22.11.2026: neu; Etappen: sach'),
  (606, 26, 'haupt', 'LK-D 22.11.2026: neu; Etappen: aenderung'),
  (624, 52, 'haupt', 'LK-D 22.11.2026: neu; Etappen: zylinder; bisher 51 Haupt'),
  (629, 98, 'haupt', 'LK-D 22.11.2026: weitergeführt; Etappen: parkett; bisher 46 Haupt'),
  (652, 36, 'neben', 'LK-D 22.11.2026: Nebenbezug'),
  (653, 101, 'neben', 'LK-D 22.11.2026: Nebenbezug; bisher 53 Haupt'),
  (677, 62, 'neben', 'LK-D 22.11.2026: Nebenbezug; 82 stillgelegt'),
  (682, 63, 'haupt', 'LK-D 22.11.2026: weitergeführt; Etappen: bedingt, rueckschluss'),
  (682, 62, 'neben', 'LK-D 22.11.2026: Nebenbezug')
) v(e, t, b, g)
where exists (select 1 from schule.eintrag where id = v.e) and exists (select 1 from schule.thema where id = v.t)
on conflict (eintrag_id, thema_id) do nothing;

-- 5) Gymnasium: Lern- und Unterbereiche geprüft (Titel, Stunden gegen LehrplanPLUS vom 22.11.). Punkte nicht (DB teilt feiner als das Original).
update schule.eintrag set pruefstatus = 'geprueft' where id in (1, 2, 10, 16, 22, 23, 30, 36, 37, 43, 49, 50, 58, 65, 71, 77, 83, 84, 90, 97, 105, 106, 111, 118, 119, 125, 131, 138, 143, 153, 160, 169, 174, 180, 186, 191, 199, 208, 209, 217, 223, 229, 234, 240, 244, 245, 250, 257, 263, 268, 276, 281) and pruefstatus <> 'geprueft';

-- 6) Rauchtest (liest nur)
do $$
declare v_txt text; v_n int;
begin
  -- a) jede erwartete Zuordnung mit erwartetem Bezug
  select string_agg(v.e || '/' || v.t || ':' || v.b, ', ') into v_txt from (values (292,15,'haupt'), (293,15,'haupt'), (294,15,'haupt'), (295,15,'haupt'), (297,15,'haupt'), (298,15,'haupt'), (300,18,'haupt'), (301,18,'haupt'), (302,18,'haupt'), (303,67,'haupt'), (303,19,'neben'), (304,67,'haupt'), (305,17,'haupt'), (307,60,'haupt'), (308,60,'haupt'), (310,16,'haupt'), (311,16,'haupt'), (312,16,'haupt'), (313,16,'haupt'), (314,16,'haupt'), (314,18,'neben'), (315,16,'haupt'), (315,18,'neben'), (316,16,'haupt'), (318,42,'haupt'), (319,42,'haupt'), (320,42,'haupt'), (321,42,'haupt'), (322,42,'haupt'), (322,43,'neben'), (323,42,'haupt'), (323,43,'neben'), (324,52,'haupt'), (325,52,'haupt'), (325,91,'neben'), (326,42,'neben'), (326,52,'haupt'), (328,25,'haupt'), (329,25,'haupt'), (330,25,'haupt'), (331,25,'haupt'), (332,25,'neben'), (332,26,'haupt'), (333,25,'haupt'), (335,50,'haupt'), (336,50,'haupt'), (337,50,'haupt'), (338,50,'haupt'), (339,50,'haupt'), (340,50,'haupt'), (342,57,'haupt'), (343,57,'haupt'), (344,57,'haupt'), (346,21,'haupt'), (347,21,'haupt'), (348,21,'haupt'), (349,21,'haupt'), (350,22,'haupt'), (351,22,'haupt'), (352,21,'neben'), (352,22,'haupt'), (352,24,'neben'), (353,21,'haupt'), (353,22,'neben'), (354,21,'haupt'), (355,23,'haupt'), (356,23,'haupt'), (357,23,'haupt'), (357,25,'neben'), (359,46,'haupt'), (360,46,'haupt'), (361,46,'haupt'), (361,44,'neben'), (362,46,'haupt'), (363,46,'haupt'), (365,99,'haupt'), (365,50,'neben'), (366,99,'haupt'), (367,99,'haupt'), (368,99,'haupt'), (369,99,'haupt'), (370,53,'haupt'), (370,50,'neben'), (370,99,'neben'), (372,100,'haupt'), (373,100,'haupt'), (374,100,'haupt'), (375,100,'haupt'), (377,28,'haupt'), (378,28,'haupt'), (379,28,'haupt'), (380,28,'haupt'), (380,29,'neben'), (381,1,'haupt'), (382,1,'haupt'), (383,1,'haupt'), (385,26,'haupt'), (386,26,'haupt'), (387,26,'haupt'), (388,26,'haupt'), (389,24,'haupt'), (390,24,'haupt'), (864,30,'haupt'), (865,102,'haupt'), (865,103,'neben'), (866,19,'haupt'), (866,30,'neben'), (868,46,'haupt'), (869,46,'haupt'), (870,46,'haupt'), (871,46,'haupt'), (872,50,'neben'), (872,74,'haupt'), (873,98,'haupt'), (873,43,'neben'), (874,98,'haupt'), (874,43,'neben'), (876,44,'haupt'), (877,44,'haupt'), (878,44,'haupt'), (879,44,'haupt'), (881,91,'haupt'), (882,91,'haupt'), (882,52,'neben'), (883,91,'haupt'), (885,73,'haupt'), (886,45,'haupt'), (887,73,'haupt'), (888,73,'haupt'), (889,45,'haupt'), (889,47,'neben'), (702,29,'haupt'), (702,102,'neben'), (703,2,'haupt'), (704,3,'haupt'), (704,69,'neben'), (705,2,'haupt'), (705,3,'neben'), (891,94,'haupt'), (892,24,'neben'), (892,71,'haupt'), (893,93,'haupt'), (894,93,'haupt'), (895,26,'neben'), (895,93,'haupt'), (897,58,'haupt'), (897,95,'neben'), (898,95,'haupt'), (898,58,'neben'), (899,81,'haupt'), (900,57,'haupt'), (930,46,'haupt'), (930,42,'neben'), (930,44,'neben'), (931,44,'haupt'), (933,46,'haupt'), (934,46,'haupt'), (935,46,'haupt'), (936,46,'haupt'), (937,49,'neben'), (937,46,'haupt'), (939,91,'haupt'), (940,91,'haupt'), (941,91,'haupt'), (732,29,'haupt'), (733,29,'neben'), (733,35,'neben'), (733,97,'haupt'), (734,2,'haupt'), (734,3,'neben'), (736,31,'haupt'), (737,5,'haupt'), (943,32,'haupt'), (944,32,'haupt'), (944,33,'neben'), (945,32,'neben'), (945,33,'haupt'), (946,32,'neben'), (946,33,'haupt'), (947,33,'haupt'), (948,33,'haupt'), (948,74,'neben'), (950,61,'haupt'), (950,60,'neben'), (950,63,'neben'), (951,61,'haupt'), (758,20,'haupt'), (758,68,'neben'), (759,8,'haupt'), (759,68,'neben'), (760,20,'haupt'), (762,47,'haupt'), (763,47,'haupt'), (764,47,'haupt'), (765,47,'haupt'), (766,47,'haupt'), (767,47,'haupt'), (768,47,'haupt'), (769,47,'haupt'), (771,54,'haupt'), (772,54,'haupt'), (773,54,'haupt'), (774,54,'haupt'), (775,54,'haupt'), (776,54,'neben'), (776,55,'haupt'), (778,51,'haupt'), (779,51,'haupt'), (781,92,'haupt'), (782,52,'neben'), (782,92,'haupt'), (782,101,'neben'), (783,51,'neben'), (783,53,'neben'), (783,92,'haupt'), (783,101,'neben'), (784,92,'haupt'), (786,6,'haupt'), (788,8,'neben'), (788,35,'haupt'), (789,8,'neben'), (789,35,'haupt'), (790,8,'neben'), (790,35,'haupt'), (791,8,'neben'), (791,35,'haupt'), (792,35,'haupt'), (793,8,'haupt'), (794,8,'haupt'), (795,8,'neben'), (795,35,'haupt'), (796,13,'haupt'), (798,61,'haupt'), (798,64,'neben'), (799,61,'haupt'), (800,61,'haupt'), (801,61,'haupt'), (801,63,'neben'), (802,61,'haupt'), (819,14,'neben'), (819,38,'neben'), (819,56,'haupt'), (820,14,'neben'), (820,33,'neben'), (820,38,'neben'), (820,56,'haupt'), (820,55,'neben'), (821,38,'haupt'), (822,14,'neben'), (822,38,'neben'), (822,56,'haupt'), (823,38,'neben'), (823,56,'haupt'), (824,38,'neben'), (824,56,'haupt'), (825,14,'neben'), (825,38,'neben'), (825,56,'haupt'), (826,14,'neben'), (826,38,'neben'), (826,56,'haupt'), (827,14,'haupt'), (828,49,'haupt'), (828,56,'neben'), (829,49,'haupt'), (829,56,'neben'), (831,49,'haupt'), (832,49,'haupt'), (833,37,'haupt'), (833,36,'neben'), (833,49,'neben'), (834,49,'haupt'), (836,96,'haupt'), (837,96,'haupt'), (837,9,'neben'), (838,36,'haupt'), (838,96,'neben'), (839,36,'haupt'), (839,9,'neben'), (841,10,'haupt'), (841,37,'neben'), (842,37,'haupt'), (843,37,'haupt'), (845,62,'haupt'), (846,62,'haupt'), (3,15,'haupt'), (4,15,'haupt'), (5,15,'haupt'), (6,15,'haupt'), (7,16,'haupt'), (7,15,'neben'), (8,16,'haupt'), (9,16,'haupt'), (11,16,'haupt'), (11,18,'neben'), (12,16,'haupt'), (12,18,'neben'), (13,1,'haupt'), (13,16,'neben'), (14,18,'haupt'), (14,16,'neben'), (15,18,'haupt'), (15,16,'neben'), (17,42,'haupt'), (18,42,'haupt'), (19,42,'neben'), (19,73,'haupt'), (20,42,'haupt'), (20,43,'neben'), (21,42,'haupt'), (24,18,'haupt'), (25,17,'haupt'), (26,60,'haupt'), (27,18,'haupt'), (27,16,'neben'), (28,67,'haupt'), (29,1,'haupt'), (29,18,'neben'), (31,18,'haupt'), (32,18,'haupt'), (33,18,'haupt'), (34,18,'haupt'), (35,18,'haupt'), (38,25,'haupt'), (39,25,'haupt'), (40,25,'haupt'), (41,26,'haupt'), (41,25,'neben'), (42,25,'haupt'), (44,50,'haupt'), (45,50,'haupt'), (46,50,'haupt'), (47,50,'haupt'), (48,53,'haupt'), (48,50,'neben'), (51,21,'haupt'), (52,21,'haupt'), (53,21,'haupt'), (54,21,'haupt'), (55,22,'haupt'), (55,24,'neben'), (56,21,'haupt'), (57,21,'haupt'), (59,22,'haupt'), (60,22,'haupt'), (61,21,'haupt'), (61,22,'neben'), (62,22,'haupt'), (63,22,'haupt'), (64,22,'haupt'), (66,23,'haupt'), (67,23,'haupt'), (68,23,'haupt'), (69,23,'haupt'), (70,23,'haupt'), (72,23,'haupt'), (73,67,'neben'), (73,23,'haupt'), (74,30,'haupt'), (75,30,'neben'), (75,19,'haupt'), (76,23,'haupt'), (78,23,'haupt'), (79,23,'haupt'), (80,23,'haupt'), (81,23,'haupt'), (82,23,'haupt'), (85,99,'haupt'), (86,99,'haupt'), (87,99,'haupt'), (88,99,'haupt'), (89,53,'neben'), (89,50,'neben'), (89,99,'haupt'), (91,100,'haupt'), (92,100,'haupt'), (93,100,'haupt'), (94,100,'haupt'), (95,100,'haupt'), (96,100,'haupt'), (98,24,'haupt'), (98,71,'neben'), (99,24,'haupt'), (100,24,'haupt'), (100,57,'neben'), (101,57,'haupt'), (101,24,'neben'), (102,57,'haupt'), (103,57,'haupt'), (104,58,'haupt'), (107,28,'haupt'), (108,28,'haupt'), (108,30,'neben'), (109,28,'haupt'), (110,28,'haupt'), (112,30,'neben'), (112,29,'neben'), (112,102,'haupt'), (113,29,'haupt'), (114,29,'haupt'), (115,29,'haupt'), (116,29,'haupt'), (117,29,'haupt'), (117,28,'neben'), (120,46,'haupt'), (121,46,'haupt'), (122,46,'haupt'), (122,73,'neben'), (123,46,'haupt'), (123,44,'neben'), (124,46,'haupt'), (126,98,'haupt'), (127,98,'haupt'), (128,98,'haupt'), (129,98,'haupt'), (130,98,'haupt'), (132,2,'haupt'), (133,2,'haupt'), (134,2,'haupt'), (135,2,'haupt'), (136,94,'haupt'), (137,94,'haupt'), (137,2,'neben'), (139,95,'haupt'), (140,95,'haupt'), (141,95,'haupt'), (142,95,'haupt'), (142,58,'neben'), (144,44,'haupt'), (145,44,'haupt'), (146,44,'haupt'), (147,44,'haupt'), (148,45,'haupt'), (148,44,'neben'), (149,45,'haupt'), (149,44,'neben'), (150,45,'haupt'), (150,44,'neben'), (151,44,'haupt'), (152,44,'haupt'), (154,32,'haupt'), (155,32,'haupt'), (156,32,'haupt'), (157,32,'haupt'), (158,32,'haupt'), (159,32,'haupt'), (161,33,'haupt'), (162,33,'haupt'), (163,33,'haupt'), (164,33,'haupt'), (164,2,'neben'), (165,33,'haupt'), (165,6,'neben'), (166,33,'haupt'), (167,3,'haupt'), (167,69,'neben'), (168,33,'haupt'), (168,26,'neben'), (170,34,'haupt'), (171,34,'haupt'), (172,34,'haupt'), (173,93,'haupt'), (175,31,'haupt'), (176,31,'haupt'), (177,30,'neben'), (177,103,'haupt'), (178,5,'haupt'), (179,4,'haupt'), (181,61,'haupt'), (182,61,'haupt'), (182,64,'neben'), (183,61,'haupt'), (184,61,'haupt'), (185,61,'haupt'), (185,60,'neben'), (187,6,'haupt'), (188,6,'haupt'), (189,6,'haupt'), (190,6,'haupt'), (192,51,'haupt'), (193,51,'haupt'), (194,51,'haupt'), (195,52,'haupt'), (195,91,'neben'), (195,51,'neben'), (196,101,'haupt'), (197,101,'haupt'), (198,101,'haupt'), (198,51,'neben'), (200,68,'haupt'), (200,20,'neben'), (201,68,'haupt'), (201,20,'neben'), (202,20,'haupt'), (203,20,'haupt'), (204,20,'haupt'), (205,20,'haupt'), (206,20,'haupt'), (207,68,'haupt'), (210,35,'haupt'), (211,35,'haupt'), (211,8,'neben'), (212,35,'haupt'), (213,35,'haupt'), (214,8,'haupt'), (215,8,'haupt'), (216,35,'haupt'), (216,8,'neben'), (218,7,'haupt'), (219,35,'haupt'), (219,7,'neben'), (220,5,'neben'), (220,8,'haupt'), (221,35,'haupt'), (222,35,'haupt'), (224,63,'haupt'), (225,63,'haupt'), (226,63,'haupt'), (227,63,'haupt'), (228,63,'haupt'), (230,47,'haupt'), (231,47,'haupt'), (232,47,'haupt'), (232,5,'neben'), (233,47,'haupt'), (235,36,'haupt'), (236,9,'haupt'), (237,9,'haupt'), (238,96,'haupt'), (239,96,'haupt'), (239,36,'neben'), (241,54,'haupt'), (242,54,'haupt'), (243,54,'haupt'), (246,55,'haupt'), (247,55,'haupt'), (248,55,'haupt'), (249,55,'haupt'), (251,56,'haupt'), (252,56,'haupt'), (253,14,'haupt'), (254,56,'haupt'), (255,56,'haupt'), (256,56,'haupt'), (258,37,'haupt'), (259,37,'haupt'), (260,10,'haupt'), (261,10,'haupt'), (262,37,'haupt'), (262,10,'neben'), (264,62,'haupt'), (265,62,'haupt'), (266,64,'haupt'), (266,62,'neben'), (267,64,'haupt'), (267,62,'neben'), (269,38,'haupt'), (270,38,'haupt'), (270,14,'neben'), (271,38,'haupt'), (272,38,'haupt'), (273,38,'haupt'), (274,38,'haupt'), (275,38,'haupt'), (277,39,'haupt'), (278,11,'haupt'), (279,39,'haupt'), (280,39,'haupt'), (282,92,'neben'), (282,91,'haupt'), (283,92,'neben'), (283,91,'haupt'), (284,92,'haupt'), (285,53,'neben'), (285,101,'haupt'), (286,92,'haupt'), (287,92,'haupt'), (288,92,'haupt'), (289,92,'haupt'), (528,15,'haupt'), (529,15,'haupt'), (529,67,'neben'), (530,15,'haupt'), (531,67,'haupt'), (531,68,'neben'), (532,17,'haupt'), (533,17,'haupt'), (533,21,'neben'), (534,17,'haupt'), (535,18,'haupt'), (536,15,'haupt'), (537,24,'haupt'), (538,21,'neben'), (538,24,'haupt'), (539,22,'neben'), (539,24,'haupt'), (540,24,'haupt'), (541,24,'haupt'), (542,28,'haupt'), (543,29,'haupt'), (544,28,'haupt'), (545,28,'neben'), (545,32,'haupt'), (546,1,'haupt'), (547,28,'haupt'), (548,42,'haupt'), (549,42,'haupt'), (549,43,'neben'), (550,43,'haupt'), (551,42,'haupt'), (552,43,'neben'), (552,98,'haupt'), (553,21,'haupt'), (554,21,'haupt'), (555,23,'haupt'), (556,23,'haupt'), (557,23,'haupt'), (558,57,'haupt'), (559,57,'haupt'), (560,57,'haupt'), (561,57,'haupt'), (562,57,'haupt'), (563,63,'haupt'), (564,50,'haupt'), (565,53,'haupt'), (565,100,'neben'), (566,53,'haupt'), (566,101,'neben'), (567,53,'haupt'), (568,53,'haupt'), (569,21,'haupt'), (570,21,'haupt'), (571,21,'haupt'), (572,26,'haupt'), (573,26,'haupt'), (574,61,'haupt'), (575,60,'neben'), (575,61,'haupt'), (576,61,'haupt'), (577,61,'haupt'), (578,61,'haupt'), (579,61,'haupt'), (580,61,'haupt'), (580,64,'neben'), (581,16,'haupt'), (582,16,'haupt'), (583,42,'haupt'), (584,16,'neben'), (584,18,'haupt'), (585,16,'haupt'), (586,18,'haupt'), (587,28,'haupt'), (588,29,'haupt'), (589,28,'haupt'), (590,2,'haupt'), (591,2,'haupt'), (592,2,'haupt'), (593,3,'haupt'), (594,3,'haupt'), (595,50,'haupt'), (595,99,'neben'), (596,50,'haupt'), (596,99,'neben'), (597,51,'haupt'), (598,53,'haupt'), (599,53,'haupt'), (599,100,'neben'), (600,53,'haupt'), (600,101,'neben'), (601,26,'haupt'), (602,25,'haupt'), (603,25,'haupt'), (604,26,'haupt'), (605,26,'haupt'), (606,26,'haupt'), (607,57,'haupt'), (608,58,'haupt'), (608,95,'neben'), (609,58,'haupt'), (610,95,'haupt'), (611,95,'haupt'), (612,20,'haupt'), (613,20,'haupt'), (614,30,'haupt'), (615,19,'haupt'), (616,33,'haupt'), (617,33,'haupt'), (618,33,'haupt'), (619,6,'haupt'), (620,2,'haupt'), (621,6,'haupt'), (622,6,'haupt'), (623,52,'haupt'), (624,51,'neben'), (624,52,'haupt'), (625,92,'haupt'), (626,92,'haupt'), (627,92,'haupt'), (628,46,'haupt'), (629,46,'neben'), (629,98,'haupt'), (630,46,'haupt'), (631,47,'haupt'), (632,44,'haupt'), (633,44,'haupt'), (634,43,'neben'), (634,54,'haupt'), (635,55,'haupt'), (636,59,'haupt'), (637,59,'haupt'), (638,59,'haupt'), (639,59,'haupt'), (641,17,'neben'), (641,29,'haupt'), (642,32,'haupt'), (643,33,'haupt'), (643,2,'neben'), (643,3,'neben'), (644,6,'haupt'), (645,49,'haupt'), (646,8,'neben'), (646,35,'haupt'), (647,47,'haupt'), (648,46,'neben'), (648,44,'haupt'), (649,42,'neben'), (649,46,'haupt'), (650,45,'haupt'), (651,55,'haupt'), (652,37,'haupt'), (652,36,'neben'), (653,53,'neben'), (653,92,'haupt'), (653,101,'neben'), (654,56,'haupt'), (655,20,'haupt'), (655,29,'neben'), (655,34,'neben'), (656,76,'haupt'), (657,63,'haupt'), (658,59,'haupt'), (658,57,'neben'), (658,58,'neben'), (659,65,'haupt'), (661,17,'neben'), (661,29,'haupt'), (662,32,'haupt'), (663,33,'haupt'), (663,3,'neben'), (663,75,'neben'), (664,6,'haupt'), (664,66,'neben'), (665,6,'neben'), (665,49,'haupt'), (666,39,'haupt'), (666,35,'neben'), (666,29,'neben'), (666,8,'neben'), (667,47,'haupt'), (668,46,'neben'), (668,44,'haupt'), (669,42,'neben'), (669,46,'neben'), (669,49,'haupt'), (670,45,'haupt'), (671,55,'haupt'), (671,47,'neben'), (671,54,'neben'), (672,37,'haupt'), (672,36,'neben'), (673,53,'neben'), (673,91,'neben'), (673,92,'haupt'), (674,56,'haupt'), (674,38,'neben'), (675,20,'haupt'), (675,29,'neben'), (675,34,'neben'), (676,76,'haupt'), (677,63,'haupt'), (677,60,'neben'), (677,62,'neben'), (678,79,'haupt'), (678,59,'neben'), (678,58,'neben'), (679,65,'haupt'), (680,63,'haupt'), (681,63,'haupt'), (682,63,'haupt'), (682,62,'neben'), (683,1,'neben'), (683,28,'haupt'), (684,46,'neben'), (684,44,'haupt'), (685,42,'neben'), (685,33,'haupt')) v(e, t, b)
   where not exists (select 1 from schule.zuordnung z where z.eintrag_id = v.e and z.thema_id = v.t and z.bezug = v.b);
  if v_txt is not null then raise exception 'Rauchtest a: erwartete Zuordnung fehlt: %', v_txt; end if;
  -- b) Punkte ohne Hauptbezug: nur die beiden IB-Wiederholungskapitel (640, 660)
  select string_agg(e.id::text, ', ' order by e.id) into v_txt from schule.eintrag e
   where e.quelle_id in (1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 15, 18, 19, 20, 21, 22, 23, 24) and e.art in ('kompetenz', 'thema') and not e.archiviert
     and not exists (select 1 from schule.zuordnung z where z.eintrag_id = e.id and z.bezug = 'haupt');
  if coalesce(v_txt, '') <> '640, 660' then raise exception 'Rauchtest b: Punkte ohne Hauptthema weichen ab: %', v_txt; end if;
  -- c) Klassen aller Themen unverändert
  if coalesce(current_setting('lk.jahrgang_vorher', true), '') = '' then raise exception 'Rauchtest c: kein Vorherstand (nicht in einer Transaktion)'; end if;
  select string_agg(t.id::text, ', ') into v_txt from schule.thema t
   where schule.thema_jahrgang(t.id) is distinct from (current_setting('lk.jahrgang_vorher')::jsonb -> t.id::text);
  if v_txt is not null then raise exception 'Rauchtest c: Klasse geändert bei Thema %', v_txt; end if;
  -- d) kein Hauptbezug auf stillgelegte Themen in den bearbeiteten Quellen
  select count(*) into v_n from schule.zuordnung z join schule.eintrag e on e.id = z.eintrag_id
   where e.quelle_id in (1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 15, 18, 19, 20, 21, 22, 23, 24) and z.bezug = 'haupt' and z.thema_id in (12, 27, 40, 41, 48, 72, 77, 78, 82, 83);
  if v_n > 0 then raise exception 'Rauchtest d: % Hauptbezüge auf stillgelegte Themen', v_n; end if;
  raise notice 'Rauchtest LK-D bestanden';
end $$;
