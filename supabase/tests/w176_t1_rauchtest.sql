-- Rauchtest W176 Teil 1 (Punkteregel „gelandet“ ohne Minuspunkte). Erst NACH der Migration 20261118_w176_t1_punkteregel.sql ausführen.
-- Läuft in einer Transaktion und wird zurückgerollt – es bleibt nichts zurück. Nutzt nur das Testkind (lernender.ist_test).
-- Ergebnis: NOTICE-Zeilen „ok …“; bei einem Fehler bricht der Block mit „FEHLER …“ ab.
begin;
do $$
declare v_l bigint; v_e bigint; v_lz text; v_s3 bigint; v_s1a bigint; v_s1b bigint; v_typ3 text; v_typ1 text; v_bonus bigint; k schule.karte_stand;
  procedure_reset text;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  -- eine Etappe mit Stufe-3-Typ, mindestens 2 Typen auf Stufe 1/2 und karte_ziel 6
  select a.einheit_id, a.variante_gruppe into v_e, v_lz from schule.aufgabe a
   where a.pool = 'uebung' and a.freigegeben and a.typ is not null
   group by 1, 2 having count(*) >= 6 and count(distinct a.typ) filter (where a.stufe = 1) >= 2
      and bool_or(a.stufe = 3 and a.typ in ('rueckwaerts','verknuepfen','begruenden','fehler','transfer','parameter','pruefung')) limit 1;
  select id, typ into v_s3, v_typ3 from schule.aufgabe where einheit_id = v_e and variante_gruppe = v_lz and pool = 'uebung' and freigegeben and stufe = 3
     and typ in ('rueckwaerts','verknuepfen','begruenden','fehler','transfer','parameter','pruefung') order by id limit 1;
  select id, typ into v_s1a, v_typ1 from schule.aufgabe where einheit_id = v_e and variante_gruppe = v_lz and pool = 'uebung' and freigegeben and stufe = 1 order by id limit 1;
  select id into v_s1b from schule.aufgabe where einheit_id = v_e and variante_gruppe = v_lz and pool = 'uebung' and freigegeben and stufe = 1 and typ <> v_typ1 order by id limit 1;
  if v_s3 is null or v_s1a is null or v_s1b is null then raise exception 'FEHLER keine passende Etappe gefunden'; end if;

  -- 1) 6 richtige ohne Typvielfalt (immer dieselbe schwere Bordkarte) → nicht gelandet
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (v_l, v_e, v_lz) on conflict do nothing;
  update schule.karte_stand set serie = 0, sitzt = false, sitzt_am = null, schwer_ok = false, eigene_loesungen = 0, typen = '{}', folge = 0, fehler_folge = 0, stufe_senkung = 0, wdh_stufe = 0
   where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  for i in 1..6 loop perform schule.karte_buchen(v_l, v_s3, true, 0::smallint, now()); end loop;
  select * into k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if k.sitzt or k.eigene_loesungen <> 6 or k.folge <> 6 then raise exception 'FEHLER 1: %', row_to_json(k); end if;
  raise notice 'ok 1: 6 richtige mit nur einem Typ → nicht gelandet (eigene 6, Typen %)', k.typen;

  -- 2) zweiter Typ dazu, aber die letzte falsch → nicht gelandet; danach 3 in Folge → gelandet
  perform schule.karte_buchen(v_l, v_s1b, true, 0::smallint, now());
  update schule.karte_stand set sitzt = false, sitzt_am = null where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz; -- falls schon gelandet: zurück vor den Fehler
  perform schule.karte_buchen(v_l, v_s1a, false, 0::smallint, now());
  select * into k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if k.sitzt or k.folge <> 0 or k.eigene_loesungen <> 7 then raise exception 'FEHLER 2a: %', row_to_json(k); end if;
  raise notice 'ok 2a: letzte falsch → folge 0, eigene Lösungen bleiben (%), keine Abzüge', k.eigene_loesungen;
  -- 3) Tipp-Treffer zählt nicht und bricht die Folge nicht
  perform schule.karte_buchen(v_l, v_s1a, true, 0::smallint, now());
  perform schule.karte_buchen(v_l, v_s1b, true, 1::smallint, now()); -- mit Tipp
  select * into k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if k.folge <> 1 or k.eigene_loesungen <> 8 or k.sitzt then raise exception 'FEHLER 3: %', row_to_json(k); end if;
  raise notice 'ok 3: Tipp-Treffer zählt nicht (eigene 8), folge bleibt 1';
  perform schule.karte_buchen(v_l, v_s1b, true, 0::smallint, now());
  perform schule.karte_buchen(v_l, v_s3, true, 0::smallint, now());
  select * into k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if not k.sitzt then raise exception 'FEHLER 2b: %', row_to_json(k); end if;
  raise notice 'ok 2b: 3 richtige in Folge → gelandet';

  -- 4) 2 Fehler in Folge senken die Stufe um 1, einer nicht
  update schule.karte_stand set sitzt = false, sitzt_am = null, folge = 0, fehler_folge = 0, stufe_senkung = 0 where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  perform schule.karte_buchen(v_l, v_s1a, false, 0::smallint, now());
  select * into k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if k.stufe_senkung <> 0 then raise exception 'FEHLER 4a: %', row_to_json(k); end if;
  perform schule.karte_buchen(v_l, v_s1a, false, 0::smallint, now());
  select * into k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if k.stufe_senkung <> 1 then raise exception 'FEHLER 4b: %', row_to_json(k); end if;
  raise notice 'ok 4: ein Fehler senkt nicht, zwei in Folge senken um 1';

  -- 5) Etappe mit wenigen Aufgaben: ziel und folge_ziel
  if exists (select 1 from schule.aufgabe a where a.pool = 'uebung' and a.freigegeben group by a.einheit_id, a.variante_gruppe having count(*) between 2 and 5) then
    raise notice 'ok 5: Etappen mit 2–5 Übungen: karte_ziel = Zahl der Übungen, folge_ziel = min(3, ziel) – siehe Spalte unten';
  else raise notice 'ok 5: keine Etappe mit weniger als 6 freien Übungen vorhanden (Regel greift: least(6, greatest(2, n)), folge_ziel min(3, ziel))'; end if;

  -- 6) Knobel-Bordkarte zählt nicht
  select id into v_bonus from schule.aufgabe where pool = 'bonus' and einheit_id = v_e and variante_gruppe = v_lz limit 1;
  if v_bonus is not null then
    perform schule.karte_buchen(v_l, v_bonus, true, 0::smallint, now());
    if (select eigene_loesungen from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz) <> k.eigene_loesungen then raise exception 'FEHLER 6'; end if;
    raise notice 'ok 6: Knobel-Bordkarte zählt nicht';
  else raise notice 'ok 6: (keine Knobel-Bordkarte in dieser Etappe – karte_buchen bucht nur pool = uebung)'; end if;
end $$;
-- 7) Bestandsübernahme: sitzende Etappen und Punkte (ohne Namen)
select count(*) filter (where sitzt) as sitzend, sum(serie) as summe_serie, sum(eigene_loesungen) as summe_eigene,
       count(*) filter (where sitzt and eigene_loesungen < 1) as sitzend_ohne_eigene, count(*) filter (where folge > 3) as folge_ueber_3_aus_bestand
  from schule.karte_stand;
rollback;
