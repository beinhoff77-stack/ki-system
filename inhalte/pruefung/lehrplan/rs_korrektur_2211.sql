-- LP-RS (22.11.2026, Stand Nachtrag 13:30/13:45): Korrektur der Realschul-Lehrplanzuordnungen nach Punkt-für-Punkt-Abgleich mit LehrplanPLUS (abgerufen 22.11.2026).
-- Maßstab Wahlpflichtfächergruppe I (Entscheidung Sebastian 22.11., 13:45): nur Quellen RS 5, 6 (allgemein) und 7 I, 8 I, 9 I, 10 I (7, 8, 24, 12, 13, 15).
-- Gruppe II/III (25, 26, 14, 16) nur im Bericht und in der JSON (korrektur_sql = false), hier unverändert.
-- Bericht: inhalte/pruefung/lehrplan/rs_pruefung_2211.md, Daten: rs_pruefung_2211.json.
-- Nur INSERT und UPDATE auf schule.zuordnung, schule.eintrag und schule.thema (eine Klasse, Schritt 8); kein DROP, kein DELETE.
-- Veraltete Zuordnungen (stillgelegte Themen) werden nicht gelöscht, sondern auf Nebenbezug mit pruefstatus 'klaerungsbedarf' gesetzt.
-- „neu“/„weitergeführt“ steht in begruendung (das Datenmodell kennt nur haupt/neben, Vorschlag im Bericht).
-- Wiederholt ausführbar; in EINER Transaktion einspielen (Vorherstand für den Rauchtest, transaktionslokal).
-- Klassen: nur Thema 91 rs_by 8 -> 7 (Gruppe I hat Schrägbilder in 7). Alle anderen Klassen unverändert (Rauchtest c); jedes Thema hat klasse_fest.rs_by.

do $$ begin
  perform set_config('lprs.jahrgang_vorher', (select jsonb_object_agg(id::text, schule.thema_jahrgang(id)) from schule.thema)::text, true);
end $$;

-- 1) Hauptbezüge, die nicht Haupt bleiben, zuerst auf Neben (eindeutiger Hauptbezug je Eintrag)
update schule.zuordnung set bezug = 'neben' where eintrag_id = 303 and thema_id = 19 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben', begruendung = 'LP-RS 22.11.2026: neu; große Zahlen in Zehnerpotenzen stehen in 67 (Kl. 5); 19 erst Kl. 7', pruefstatus = 'geprueft' where eintrag_id = 303 and thema_id = 19 and bezug <> 'neben';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 361 and thema_id = 44 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben', begruendung = 'LP-RS 22.11.2026: neu; Grundkonstruktionen stehen in 46 (Kl. 6); 44 erst Kl. 7', pruefstatus = 'geprueft' where eintrag_id = 361 and thema_id = 44 and bezug <> 'neben';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 866 and thema_id = 30 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben', begruendung = 'LP-RS 22.11.2026: neu; Vorsilben und Zehnerpotenzen sind Kern von 19', pruefstatus = 'geprueft' where eintrag_id = 866 and thema_id = 30 and bezug <> 'neben';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 871 and thema_id = 48 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 873 and thema_id = 43 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben', begruendung = 'LP-RS 22.11.2026: nur Nebenbezug; Stufen-/Wechselwinkel in 98 (Kl. 7)', pruefstatus = 'geprueft' where eintrag_id = 873 and thema_id = 43 and bezug <> 'neben';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 874 and thema_id = 43 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben', begruendung = 'LP-RS 22.11.2026: nur Nebenbezug; Winkelsummen und Außenwinkel in 98', pruefstatus = 'geprueft' where eintrag_id = 874 and thema_id = 43 and bezug <> 'neben';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 930 and thema_id = 44 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben', begruendung = 'LP-RS 22.11.2026: neu (Etappen: Winkel in symmetrischen Vierecken); Vierecke ordnen in 46, Grundformen in 42', pruefstatus = 'geprueft' where eintrag_id = 930 and thema_id = 44 and bezug <> 'neben';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 933 and thema_id = 48 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 934 and thema_id = 48 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 935 and thema_id = 48 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 936 and thema_id = 48 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 937 and thema_id = 48 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 766 and thema_id = 48 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 837 and thema_id = 9 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben', begruendung = 'LP-RS 22.11.2026: nur Nebenbezug; n-te Wurzel ist Kern von 96', pruefstatus = 'geprueft' where eintrag_id = 837 and thema_id = 9 and bezug <> 'neben';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 296 and thema_id = 15 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben', begruendung = 'LP-RS 22.11.2026: neu; Zahlensysteme sind nicht Thema 15; Lücke', pruefstatus = 'geprueft' where eintrag_id = 296 and thema_id = 15 and bezug <> 'neben';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 371 and thema_id = 53 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben', begruendung = 'LP-RS 22.11.2026: neu; Raumgeometrie Kl. 6 ist Thema 100', pruefstatus = 'geprueft' where eintrag_id = 371 and thema_id = 53 and bezug <> 'neben';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 494 and thema_id = 52 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben', begruendung = 'LP-RS 22.11.2026: weitergeführt; Schrägbilder/Netze in 91', pruefstatus = 'geprueft' where eintrag_id = 494 and thema_id = 52 and bezug <> 'neben';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 503 and thema_id = 53 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben', begruendung = 'LP-RS 22.11.2026: weitergeführt; Körperberechnung Kl. 9 in 92/101', pruefstatus = 'geprueft' where eintrag_id = 503 and thema_id = 53 and bezug <> 'neben';
update schule.zuordnung set bezug = 'neben' where eintrag_id = 697 and thema_id = 52 and bezug = 'haupt';
update schule.zuordnung set bezug = 'neben', begruendung = 'LP-RS 22.11.2026: weitergeführt; Gruppe I: Schrägbilder in Kl. 7', pruefstatus = 'geprueft' where eintrag_id = 697 and thema_id = 52 and bezug <> 'neben';

-- 2) Weggefallene Zuordnungen auf das richtige Thema umhängen (nur wenn dort noch keine Zuordnung besteht)
update schule.zuordnung z set thema_id = 46, bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: weitergeführt; 48 stillgelegt; Verschiebung in 46', pruefstatus = 'geprueft' where z.eintrag_id = 868 and z.thema_id = 48 and not exists (select 1 from schule.zuordnung y where y.eintrag_id = 868 and y.thema_id = 46);
update schule.zuordnung z set thema_id = 46, bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: weitergeführt; 48 stillgelegt', pruefstatus = 'geprueft' where z.eintrag_id = 869 and z.thema_id = 48 and not exists (select 1 from schule.zuordnung y where y.eintrag_id = 869 and y.thema_id = 46);
update schule.zuordnung z set thema_id = 46, bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: weitergeführt; 48 stillgelegt; Etappe Gegenvektor in 46', pruefstatus = 'geprueft' where z.eintrag_id = 870 and z.thema_id = 48 and not exists (select 1 from schule.zuordnung y where y.eintrag_id = 870 and y.thema_id = 46);
update schule.zuordnung z set thema_id = 49, bezug = 'neben', begruendung = 'LP-RS 22.11.2026: neu; Vektoren drehen: nur in 49 (Kl. 10), kein Thema in Kl. 8', pruefstatus = 'geprueft' where z.eintrag_id = 937 and z.thema_id = 46 and not exists (select 1 from schule.zuordnung y where y.eintrag_id = 937 and y.thema_id = 49);
update schule.zuordnung z set thema_id = 8, bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: neu; 12 stillgelegt; Etappe reinquadratisch in 8', pruefstatus = 'geprueft' where z.eintrag_id = 759 and z.thema_id = 12 and not exists (select 1 from schule.zuordnung y where y.eintrag_id = 759 and y.thema_id = 8);
update schule.zuordnung z set thema_id = 37, bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: neu; 40 stillgelegt; Abbilden von Graphen in 36/37', pruefstatus = 'geprueft' where z.eintrag_id = 833 and z.thema_id = 40 and not exists (select 1 from schule.zuordnung y where y.eintrag_id = 833 and y.thema_id = 37);

-- 3) Veraltete Zuordnungen ohne Ersatz kennzeichnen (kein Löschen)
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 871 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 933 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 934 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 935 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 936 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 937 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 766 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 767 and thema_id = 40 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 773 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 788 and thema_id = 40 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 789 and thema_id = 40 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 790 and thema_id = 40 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 791 and thema_id = 40 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 792 and thema_id = 78 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 795 and thema_id = 78 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 838 and thema_id = 77 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 842 and thema_id = 77 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 493 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 497 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 499 and thema_id = 12 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 500 and thema_id = 40 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 500 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 505 and thema_id = 40 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 514 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 515 and thema_id = 40 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 515 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');
update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = 'LP-RS 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten' where eintrag_id = 693 and thema_id = 48 and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');

-- 4) Nebenbezüge zu Hauptbezügen machen
update schule.zuordnung set bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: neu; Grundkonstruktionen stehen in 46 (Kl. 6); 44 erst Kl. 7', pruefstatus = 'geprueft' where eintrag_id = 361 and thema_id = 46 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: neu; Vorsilben und Zehnerpotenzen sind Kern von 19', pruefstatus = 'geprueft' where eintrag_id = 866 and thema_id = 19 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: neu (Etappen: Um einen Punkt drehen); 48 stillgelegt; Etappe Um einen Punkt drehen in 46', pruefstatus = 'geprueft' where eintrag_id = 933 and thema_id = 46 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: neu (Etappen: An einem Punkt spiegeln); Etappe An einem Punkt spiegeln in 46', pruefstatus = 'geprueft' where eintrag_id = 934 and thema_id = 46 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: neu (Etappen: Um einen Punkt drehen)', pruefstatus = 'geprueft' where eintrag_id = 935 and thema_id = 46 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: neu (Etappen: Um einen Punkt drehen)', pruefstatus = 'geprueft' where eintrag_id = 936 and thema_id = 46 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: neu; 48 stillgelegt; Vektorrechnung nur teilweise in 47', pruefstatus = 'geprueft' where eintrag_id = 766 and thema_id = 47 and bezug <> 'haupt';
update schule.zuordnung set bezug = 'haupt', begruendung = 'LP-RS 22.11.2026: neu; n-te Wurzel ist Kern von 96', pruefstatus = 'geprueft' where eintrag_id = 837 and thema_id = 96 and bezug <> 'haupt';

-- 5) Fehlende Zuordnungen ergänzen
insert into schule.zuordnung (eintrag_id, thema_id, bezug, begruendung, pruefstatus)
select v.e, v.t, v.b, v.g, 'geprueft' from (values
  (292, 15, 'haupt', 'LP-RS 22.11.2026: neu'),
  (293, 15, 'haupt', 'LP-RS 22.11.2026: neu'),
  (294, 15, 'haupt', 'LP-RS 22.11.2026: neu'),
  (295, 15, 'haupt', 'LP-RS 22.11.2026: neu'),
  (303, 67, 'haupt', 'LP-RS 22.11.2026: neu; große Zahlen in Zehnerpotenzen stehen in 67 (Kl. 5); 19 erst Kl. 7'),
  (307, 60, 'haupt', 'LP-RS 22.11.2026: neu'),
  (308, 60, 'haupt', 'LP-RS 22.11.2026: neu'),
  (310, 16, 'haupt', 'LP-RS 22.11.2026: neu'),
  (311, 16, 'haupt', 'LP-RS 22.11.2026: neu'),
  (312, 16, 'haupt', 'LP-RS 22.11.2026: neu'),
  (313, 16, 'haupt', 'LP-RS 22.11.2026: neu'),
  (314, 16, 'haupt', 'LP-RS 22.11.2026: neu'),
  (314, 18, 'neben', 'LP-RS 22.11.2026: neu'),
  (315, 16, 'haupt', 'LP-RS 22.11.2026: neu'),
  (315, 18, 'neben', 'LP-RS 22.11.2026: neu'),
  (316, 16, 'haupt', 'LP-RS 22.11.2026: neu'),
  (331, 25, 'haupt', 'LP-RS 22.11.2026: neu; Etappe Maßstab auf Karten und Plänen'),
  (333, 25, 'haupt', 'LP-RS 22.11.2026: neu'),
  (335, 50, 'haupt', 'LP-RS 22.11.2026: neu'),
  (336, 50, 'haupt', 'LP-RS 22.11.2026: neu'),
  (337, 50, 'haupt', 'LP-RS 22.11.2026: neu'),
  (338, 50, 'haupt', 'LP-RS 22.11.2026: neu'),
  (339, 50, 'haupt', 'LP-RS 22.11.2026: neu'),
  (340, 50, 'haupt', 'LP-RS 22.11.2026: neu'),
  (342, 57, 'haupt', 'LP-RS 22.11.2026: neu'),
  (343, 57, 'haupt', 'LP-RS 22.11.2026: neu'),
  (344, 57, 'haupt', 'LP-RS 22.11.2026: neu'),
  (360, 46, 'haupt', 'LP-RS 22.11.2026: neu'),
  (365, 99, 'haupt', 'LP-RS 22.11.2026: neu'),
  (365, 50, 'neben', 'LP-RS 22.11.2026: weitergeführt'),
  (366, 99, 'haupt', 'LP-RS 22.11.2026: neu; Drachenviereck und Raute ohne eigene Etappe'),
  (367, 99, 'haupt', 'LP-RS 22.11.2026: neu'),
  (368, 99, 'haupt', 'LP-RS 22.11.2026: neu'),
  (369, 99, 'haupt', 'LP-RS 22.11.2026: neu'),
  (370, 99, 'neben', 'LP-RS 22.11.2026: neu'),
  (372, 100, 'haupt', 'LP-RS 22.11.2026: neu'),
  (373, 100, 'haupt', 'LP-RS 22.11.2026: neu'),
  (374, 100, 'haupt', 'LP-RS 22.11.2026: neu'),
  (375, 100, 'haupt', 'LP-RS 22.11.2026: neu'),
  (864, 30, 'haupt', 'LP-RS 22.11.2026: neu'),
  (865, 102, 'haupt', 'LP-RS 22.11.2026: neu'),
  (865, 103, 'neben', 'LP-RS 22.11.2026: nur Nebenbezug'),
  (873, 98, 'haupt', 'LP-RS 22.11.2026: neu; Stufen-/Wechselwinkel in 98 (Kl. 7)'),
  (874, 98, 'haupt', 'LP-RS 22.11.2026: neu; Winkelsummen und Außenwinkel in 98'),
  (876, 44, 'haupt', 'LP-RS 22.11.2026: neu'),
  (877, 44, 'haupt', 'LP-RS 22.11.2026: neu'),
  (878, 44, 'haupt', 'LP-RS 22.11.2026: neu'),
  (879, 44, 'haupt', 'LP-RS 22.11.2026: neu'),
  (882, 52, 'neben', 'LP-RS 22.11.2026: weitergeführt'),
  (885, 73, 'haupt', 'LP-RS 22.11.2026: neu'),
  (886, 45, 'haupt', 'LP-RS 22.11.2026: neu'),
  (887, 73, 'haupt', 'LP-RS 22.11.2026: neu'),
  (888, 73, 'haupt', 'LP-RS 22.11.2026: neu'),
  (889, 45, 'haupt', 'LP-RS 22.11.2026: neu; Schwerpunkt als Etappe in 47 (Kl. 9)'),
  (889, 47, 'neben', 'LP-RS 22.11.2026: neu; Schwerpunkt als Etappe in 47 (Kl. 9)'),
  (702, 29, 'haupt', 'LP-RS 22.11.2026: neu'),
  (702, 102, 'neben', 'LP-RS 22.11.2026: neu'),
  (898, 95, 'haupt', 'LP-RS 22.11.2026: neu'),
  (898, 58, 'neben', 'LP-RS 22.11.2026: neu'),
  (930, 46, 'haupt', 'LP-RS 22.11.2026: weitergeführt; Vierecke ordnen in 46, Grundformen in 42'),
  (930, 42, 'neben', 'LP-RS 22.11.2026: weitergeführt; Vierecke ordnen in 46, Grundformen in 42'),
  (950, 61, 'haupt', 'LP-RS 22.11.2026: neu; 61 steht in Kl. 9; Ergebnis/Ereignis, Baum, Vierfeldertafel schon Kl. 8'),
  (950, 60, 'neben', 'LP-RS 22.11.2026: weitergeführt; 61 steht in Kl. 9; Ergebnis/Ereignis, Baum, Vierfeldertafel schon Kl. 8'),
  (950, 63, 'neben', 'LP-RS 22.11.2026: nur Nebenbezug; 61 steht in Kl. 9; Ergebnis/Ereignis, Baum, Vierfeldertafel schon Kl. 8'),
  (778, 51, 'haupt', 'LP-RS 22.11.2026: neu'),
  (779, 51, 'haupt', 'LP-RS 22.11.2026: neu'),
  (782, 101, 'neben', 'LP-RS 22.11.2026: nur Nebenbezug'),
  (783, 101, 'neben', 'LP-RS 22.11.2026: nur Nebenbezug'),
  (799, 61, 'haupt', 'LP-RS 22.11.2026: neu (Etappen: laplace, laplace_pruefen)'),
  (800, 61, 'haupt', 'LP-RS 22.11.2026: neu (Etappen: begriffe (Ergebnisraum))'),
  (801, 61, 'haupt', 'LP-RS 22.11.2026: neu (Etappen: gegenereignis)'),
  (801, 63, 'neben', 'LP-RS 22.11.2026: nur Nebenbezug'),
  (802, 61, 'haupt', 'LP-RS 22.11.2026: neu (Etappen: laplace)'),
  (831, 49, 'haupt', 'LP-RS 22.11.2026: neu'),
  (832, 49, 'haupt', 'LP-RS 22.11.2026: neu'),
  (833, 36, 'neben', 'LP-RS 22.11.2026: neu; 40 stillgelegt; Abbilden von Graphen in 36/37'),
  (834, 49, 'haupt', 'LP-RS 22.11.2026: neu'),
  (839, 36, 'haupt', 'LP-RS 22.11.2026: neu'),
  (839, 9, 'neben', 'LP-RS 22.11.2026: nur Nebenbezug'),
  (843, 37, 'haupt', 'LP-RS 22.11.2026: neu'),
  (845, 62, 'haupt', 'LP-RS 22.11.2026: neu'),
  (846, 62, 'haupt', 'LP-RS 22.11.2026: neu'),
  (371, 100, 'haupt', 'LP-RS 22.11.2026: neu; Raumgeometrie Kl. 6 ist Thema 100'),
  (494, 91, 'haupt', 'LP-RS 22.11.2026: weitergeführt; Schrägbilder/Netze in 91'),
  (503, 92, 'haupt', 'LP-RS 22.11.2026: neu; Körperberechnung Kl. 9 in 92/101'),
  (503, 101, 'neben', 'LP-RS 22.11.2026: nur Nebenbezug; Körperberechnung Kl. 9 in 92/101'),
  (697, 91, 'haupt', 'LP-RS 22.11.2026: neu; Gruppe I: Schrägbilder in Kl. 7')
) v(e, t, b, g)
where exists (select 1 from schule.eintrag where id = v.e) and exists (select 1 from schule.thema where id = v.t)
on conflict (eintrag_id, thema_id) do nothing;

-- 6) Lernbereich-Titel auf den Originaltitel (Titel sind keine Lehrplantexte im Sinne des Zitierverbots)
update schule.eintrag e set text = v.t, bearbeitung = 'originaltitel'
from (values (691, 'Potenzen'), (693, 'Parallelverschiebung'), (695, 'Dreiecke'), (697, 'Raumgeometrie'), (699, 'Geometrische Ortslinien und Ortsbereiche'), (701, 'Terme, Gleichungen und Ungleichungen'), (708, 'Auswertung von Daten'), (492, 'Vierecke'), (493, 'Drehung'), (494, 'Raumgeometrie'), (495, 'Terme, Gleichungen und Ungleichungen'), (496, 'Bruchterme und Bruchgleichungen'), (498, 'Daten und Zufall'), (499, 'Reelle Zahlen'), (500, 'Zentrische Streckung'), (501, 'Rechtwinklige Dreiecke'), (502, 'Kreis'), (503, 'Raumgeometrie'), (504, 'Systeme linearer Gleichungen'), (505, 'Quadratische Funktionen und quadratische Gleichungen'), (506, 'Daten und Zufall'), (514, 'Trigonometrie'), (515, 'Abbildungen'), (516, 'Potenzen und Potenzfunktionen'), (517, 'Exponentialfunktionen, Logarithmen und Logarithmusfunktionen'), (518, 'Daten und Zufall')) v(id, t)
where e.id = v.id and e.art = 'lernbereich' and (e.text, e.bearbeitung) is distinct from (v.t, 'originaltitel');

-- 7) Geprüft kennzeichnen: alle Lernbereiche (Titel, Stunden, Punktzahl) und die Punkte RS 7–10 (Zählung 1:1, Zuordnung je Punkt geprüft).
--    RS 5/6-Punkte bleiben, wie sie sind (DB teilt feiner als das Original).
update schule.eintrag set pruefstatus = 'geprueft' where id in (702, 703, 704, 705, 732, 733, 734, 736, 737, 758, 759, 760, 762, 763, 764, 765, 766, 767, 768, 769, 771, 772, 773, 774, 775, 776, 778, 779, 781, 782, 783, 784, 786, 788, 789, 790, 791, 792, 793, 794, 795, 796, 798, 799, 800, 801, 802, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 831, 832, 833, 834, 836, 837, 838, 839, 841, 842, 843, 845, 846, 864, 865, 866, 868, 869, 870, 871, 872, 873, 874, 876, 877, 878, 879, 881, 882, 883, 885, 886, 887, 888, 889, 891, 892, 893, 894, 895, 897, 898, 899, 900, 930, 931, 933, 934, 935, 936, 937, 939, 940, 941, 943, 944, 945, 946, 947, 948, 950, 951, 290, 291, 296, 299, 306, 309, 317, 327, 334, 341, 345, 358, 364, 371, 376, 384, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 514, 515, 516, 517, 518, 691, 693, 695, 697, 699, 701, 706, 708) and pruefstatus <> 'geprueft';

-- 8) Klassenlage nach Gruppe I: nur wo die erste Klasse mit Hauptbezug in Gruppe I eindeutig abweicht (91: M7 I LB4 Raumgeometrie)
update schule.thema set klasse_fest = jsonb_set(klasse_fest, '{rs_by}', '7'::jsonb) where id = 91 and klasse_fest ->> 'rs_by' is distinct from '7';

-- 9) Rauchtest (liest nur)
do $$
declare v_txt text; v_n int;
begin
  -- a) jede erwartete Zuordnung ist da, mit erwartetem Bezug
  select string_agg(v.e || '/' || v.t || ':' || v.b, ', ') into v_txt from (values (292,15,'haupt'), (293,15,'haupt'), (294,15,'haupt'), (295,15,'haupt'), (300,18,'haupt'), (301,18,'haupt'), (302,18,'haupt'), (303,67,'haupt'), (303,19,'neben'), (304,67,'haupt'), (305,17,'haupt'), (307,60,'haupt'), (308,60,'haupt'), (310,16,'haupt'), (311,16,'haupt'), (312,16,'haupt'), (313,16,'haupt'), (314,16,'haupt'), (314,18,'neben'), (315,16,'haupt'), (315,18,'neben'), (316,16,'haupt'), (318,42,'haupt'), (319,42,'haupt'), (320,42,'haupt'), (321,42,'haupt'), (322,42,'haupt'), (322,43,'neben'), (323,42,'haupt'), (323,43,'neben'), (324,52,'haupt'), (325,52,'haupt'), (325,91,'neben'), (326,42,'neben'), (326,52,'haupt'), (328,25,'haupt'), (329,25,'haupt'), (330,25,'haupt'), (331,25,'haupt'), (332,25,'neben'), (332,26,'haupt'), (333,25,'haupt'), (335,50,'haupt'), (336,50,'haupt'), (337,50,'haupt'), (338,50,'haupt'), (339,50,'haupt'), (340,50,'haupt'), (342,57,'haupt'), (343,57,'haupt'), (344,57,'haupt'), (346,21,'haupt'), (347,21,'haupt'), (348,21,'haupt'), (349,21,'haupt'), (350,22,'haupt'), (351,22,'haupt'), (352,21,'neben'), (352,22,'haupt'), (352,24,'neben'), (353,21,'haupt'), (353,22,'neben'), (354,21,'haupt'), (355,23,'haupt'), (356,23,'haupt'), (357,23,'haupt'), (357,25,'neben'), (359,46,'haupt'), (360,46,'haupt'), (361,46,'haupt'), (361,44,'neben'), (362,46,'haupt'), (363,46,'haupt'), (365,99,'haupt'), (365,50,'neben'), (366,99,'haupt'), (367,99,'haupt'), (368,99,'haupt'), (369,99,'haupt'), (370,53,'haupt'), (370,50,'neben'), (370,99,'neben'), (372,100,'haupt'), (373,100,'haupt'), (374,100,'haupt'), (375,100,'haupt'), (377,28,'haupt'), (378,28,'haupt'), (379,28,'haupt'), (380,28,'haupt'), (380,29,'neben'), (381,1,'haupt'), (382,1,'haupt'), (383,1,'haupt'), (385,26,'haupt'), (386,26,'haupt'), (387,26,'haupt'), (388,26,'haupt'), (389,24,'haupt'), (390,24,'haupt'), (864,30,'haupt'), (865,102,'haupt'), (865,103,'neben'), (866,19,'haupt'), (866,30,'neben'), (868,46,'haupt'), (869,46,'haupt'), (870,46,'haupt'), (872,50,'neben'), (872,74,'haupt'), (873,98,'haupt'), (873,43,'neben'), (874,98,'haupt'), (874,43,'neben'), (876,44,'haupt'), (877,44,'haupt'), (878,44,'haupt'), (879,44,'haupt'), (881,91,'haupt'), (882,91,'haupt'), (882,52,'neben'), (883,91,'haupt'), (885,73,'haupt'), (886,45,'haupt'), (887,73,'haupt'), (888,73,'haupt'), (889,45,'haupt'), (889,47,'neben'), (702,29,'haupt'), (702,102,'neben'), (703,2,'haupt'), (704,3,'haupt'), (704,69,'neben'), (705,2,'haupt'), (705,3,'neben'), (891,94,'haupt'), (892,24,'neben'), (892,71,'haupt'), (893,93,'haupt'), (894,93,'haupt'), (895,26,'neben'), (895,93,'haupt'), (897,58,'haupt'), (897,95,'neben'), (898,95,'haupt'), (898,58,'neben'), (899,81,'haupt'), (900,57,'haupt'), (930,46,'haupt'), (930,42,'neben'), (930,44,'neben'), (931,44,'haupt'), (933,46,'haupt'), (934,46,'haupt'), (935,46,'haupt'), (936,46,'haupt'), (937,49,'neben'), (939,91,'haupt'), (940,91,'haupt'), (941,91,'haupt'), (732,29,'haupt'), (733,29,'neben'), (733,35,'neben'), (733,97,'haupt'), (734,2,'haupt'), (734,3,'neben'), (736,31,'haupt'), (737,5,'haupt'), (943,32,'haupt'), (944,32,'neben'), (944,33,'haupt'), (945,32,'neben'), (945,33,'haupt'), (946,32,'neben'), (946,33,'haupt'), (947,33,'haupt'), (947,78,'neben'), (948,33,'haupt'), (948,74,'neben'), (950,61,'haupt'), (950,60,'neben'), (950,63,'neben'), (951,61,'haupt'), (758,20,'haupt'), (758,68,'neben'), (759,8,'haupt'), (759,68,'neben'), (760,20,'haupt'), (762,47,'haupt'), (763,47,'haupt'), (764,47,'haupt'), (765,47,'haupt'), (766,47,'haupt'), (767,47,'haupt'), (768,47,'haupt'), (769,47,'haupt'), (771,54,'haupt'), (772,54,'haupt'), (773,54,'haupt'), (774,54,'haupt'), (775,54,'haupt'), (776,54,'neben'), (776,55,'haupt'), (778,51,'haupt'), (779,51,'haupt'), (781,92,'haupt'), (782,52,'neben'), (782,92,'haupt'), (782,101,'neben'), (783,51,'neben'), (783,53,'neben'), (783,92,'haupt'), (783,101,'neben'), (784,92,'haupt'), (786,6,'haupt'), (788,8,'neben'), (788,35,'haupt'), (789,8,'neben'), (789,35,'haupt'), (790,8,'neben'), (790,35,'haupt'), (791,8,'neben'), (791,35,'haupt'), (792,35,'haupt'), (793,8,'haupt'), (794,8,'haupt'), (795,8,'neben'), (795,35,'haupt'), (796,13,'haupt'), (798,61,'haupt'), (798,64,'neben'), (799,61,'haupt'), (800,61,'haupt'), (801,61,'haupt'), (801,63,'neben'), (802,61,'haupt'), (819,14,'neben'), (819,38,'neben'), (819,56,'haupt'), (820,14,'neben'), (820,33,'neben'), (820,38,'neben'), (820,56,'haupt'), (821,38,'haupt'), (822,14,'neben'), (822,38,'neben'), (822,56,'haupt'), (823,38,'neben'), (823,56,'haupt'), (824,38,'neben'), (824,56,'haupt'), (825,14,'neben'), (825,38,'neben'), (825,56,'haupt'), (826,14,'neben'), (826,38,'neben'), (826,56,'haupt'), (827,14,'haupt'), (828,49,'haupt'), (828,56,'neben'), (829,49,'haupt'), (829,56,'neben'), (831,49,'haupt'), (832,49,'haupt'), (833,37,'haupt'), (833,36,'neben'), (833,49,'neben'), (834,49,'haupt'), (836,96,'haupt'), (837,96,'haupt'), (837,9,'neben'), (838,36,'haupt'), (838,96,'neben'), (839,36,'haupt'), (839,9,'neben'), (841,10,'haupt'), (841,37,'neben'), (842,37,'haupt'), (843,37,'haupt'), (845,62,'haupt'), (846,62,'haupt'), (296,15,'neben'), (371,100,'haupt'), (371,53,'neben'), (493,46,'haupt'), (494,91,'haupt'), (494,52,'neben'), (497,32,'neben'), (497,33,'haupt'), (499,20,'haupt'), (500,47,'haupt'), (503,92,'haupt'), (503,53,'neben'), (503,101,'neben'), (505,8,'neben'), (505,13,'neben'), (505,35,'haupt'), (514,14,'neben'), (514,38,'neben'), (514,56,'haupt'), (515,49,'haupt'), (693,43,'neben'), (693,46,'haupt'), (697,91,'haupt'), (697,52,'neben')) v(e, t, b)
   where not exists (select 1 from schule.zuordnung z where z.eintrag_id = v.e and z.thema_id = v.t and z.bezug = v.b);
  if v_txt is not null then raise exception 'Rauchtest a: erwartete Zuordnung fehlt: %', v_txt; end if;
  -- b) Lücken genau wie im Bericht (Kompetenzpunkte ohne Hauptbezug in den geprüften Realschul-Quellen)
  select string_agg(e.id::text, ', ' order by e.id) into v_txt from schule.eintrag e
   where e.quelle_id in (7, 8, 24, 12, 13, 15) and e.art = 'kompetenz' and not e.archiviert
     and not exists (select 1 from schule.zuordnung z where z.eintrag_id = e.id and z.bezug = 'haupt');
  if coalesce(v_txt, '') <> '297, 298, 871, 937' then raise exception 'Rauchtest b: Lücken weichen ab: %', v_txt; end if;
  -- c) Klassen aller Themen unverändert, außer 91 (rs_by 7, Schritt 8)
  if coalesce(current_setting('lprs.jahrgang_vorher', true), '') = '' then raise exception 'Rauchtest c: kein Vorherstand (nicht in einer Transaktion eingespielt)'; end if;
  select string_agg(t.id::text, ', ') into v_txt from schule.thema t
   where schule.thema_jahrgang(t.id) is distinct from
         case when t.id = 91 then (current_setting('lprs.jahrgang_vorher')::jsonb -> '91') || '{"rs_by": 7}'::jsonb
              else current_setting('lprs.jahrgang_vorher')::jsonb -> t.id::text end;
  if v_txt is not null then raise exception 'Rauchtest c: Klasse geändert bei Thema %', v_txt; end if;
  -- d) kein Hauptbezug auf ein stillgelegtes Thema in den geprüften Quellen
  select count(*) into v_n from schule.zuordnung z join schule.eintrag e on e.id = z.eintrag_id
   where e.quelle_id in (7, 8, 24, 12, 13, 15) and z.bezug = 'haupt' and z.thema_id in (12, 27, 40, 41, 48, 72, 77, 78, 82, 83);
  if v_n > 0 then raise exception 'Rauchtest d: % Hauptbezüge auf stillgelegte Themen', v_n; end if;
  raise notice 'Rauchtest LP-RS bestanden';
end $$;
