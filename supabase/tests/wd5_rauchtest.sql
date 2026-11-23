-- Rauchtest WD-5 (Zulauf gesetzter Etappen drosseln, 3 je Lerntag). Alles in einer Transaktion mit Rollback. Ausgabe nur Zahlen.
-- Voraussetzung: WD-S, WD-4b, WD-S 4 eingespielt. Spielt 20261128_wd5_staffel_drosseln.sql selbst ein (zweimal; der zweite Lauf tut nichts)
-- und prüft den echten Bestand vorher/nachher; danach ein Fall am Testkind (offene Runde, Reihenfolge, Rückweg).
-- Aufruf aus dem Repo-Wurzelverzeichnis: psql -v ON_ERROR_STOP=1 -f supabase/tests/wd5_rauchtest.sql
begin;

-- Bestand vorher: Karten (ganz), Lernstände, Plan, Sterne
create temp table wd5_karte_vorher on commit drop as select k.*, schule.karte_wdh_in(k) tag_vorher from schule.karte_stand k;
create temp table wd5_h on commit drop as
  select md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.lernziel_stand x), '')) lz,
         md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.route x), '')) ro,
         md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.sterne x), '')) st;
create temp table wd5_runde_vorher on commit drop as
  select r.lernender_id, r.einheit_id, r.lernziel from schule.wdh_runde_etappe r join schule.wdh_runde w on w.lernender_id = r.lernender_id and w.tag = r.tag and w.fertig_am is null
   where r.tag = schule.heute_tag(r.lernender_id);

\ir ../migrations/20261128_wd5_staffel_drosseln.sql
\ir ../migrations/20261128_wd5_staffel_drosseln.sql

-- Test 1: Regel 3; je Kind höchstens 3 gesetzte Erst-Wiederholungen je Lerntag (ohne offene Runde)
do $$ begin
  if schule.wd_regel('wdh_gesetzt_je_lerntag', 0) <> 3 then raise exception 'FEHLER 1: Regel nicht 3'; end if;
  if exists (select 1 from schule.lernender l, lateral (select g.tag, count(*) n from schule.wdh_gesetzt_erst(l.id) g where not g.in_runde group by 1) c where c.n > 3) then
    raise exception 'FEHLER 1: mehr als 3 gesetzte Erst-Wiederholungen an einem Lerntag'; end if;
  raise notice 'Test 1: Regel 3, höchstens 3 je Lerntag: OK';
end $$;

-- Test 2: Reihenfolge nach Plan (Platz, Einheit, Etappe): Lerntag steigt nicht ab
do $$ begin
  if exists (select 1 from (select g.tag, lag(g.tag) over (partition by l.id order by g.platz, g.einheit_id, g.etappe_nr, g.lernziel) vor
                              from schule.lernender l, schule.wdh_gesetzt_erst(l.id) g where not g.in_runde) q where q.tag < q.vor) then
    raise exception 'FEHLER 2: Reihenfolge nicht nach Plan'; end if;
  raise notice 'Test 2: Reihenfolge nach Plan: OK';
end $$;

-- Test 3: nur die drei Fälligkeits-Felder gesetzter Erst-Wiederholungen geändert; alles andere (andere Etappen, höhere Stufen,
-- offene Runde, Lernstände, Plan, Sterne) unverändert
do $$
declare v_n int;
begin
  if exists (select 1 from wd5_karte_vorher v join schule.karte_stand k using (lernender_id, einheit_id, lernziel)
              where (to_jsonb(k) - 'faellig_am' - 'wdh_ab' - 'wdh_lerntage') is distinct from (to_jsonb(v) - 'faellig_am' - 'wdh_ab' - 'wdh_lerntage' - 'tag_vorher')) then
    raise exception 'FEHLER 3: Karten außerhalb der Fälligkeit verändert'; end if;
  if (select count(*) from schule.karte_stand) <> (select count(*) from wd5_karte_vorher) then raise exception 'FEHLER 3: Zahl der Karten verändert'; end if;
  if exists (select 1 from wd5_karte_vorher v join schule.karte_stand k using (lernender_id, einheit_id, lernziel)
              where (k.faellig_am, k.wdh_ab, k.wdh_lerntage) is distinct from (v.faellig_am, v.wdh_ab, v.wdh_lerntage)
                and not (v.sitzt and v.wdh_gesetzt_am is not null and v.wdh_stufe = 0 and v.wdh_fehler = 0 and v.tag_vorher is not null)) then
    raise exception 'FEHLER 3: nicht gesetzte Etappe oder höhere Stufe verschoben'; end if;
  if exists (select 1 from wd5_runde_vorher r join wd5_karte_vorher v using (lernender_id, einheit_id, lernziel) join schule.karte_stand k using (lernender_id, einheit_id, lernziel)
              where (k.faellig_am, k.wdh_ab, k.wdh_lerntage) is distinct from (v.faellig_am, v.wdh_ab, v.wdh_lerntage)) then
    raise exception 'FEHLER 3: Etappe der offenen Runde verschoben'; end if;
  if (select lz || ro || st from wd5_h) is distinct from
     (md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.lernziel_stand x), ''))
      || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.route x), ''))
      || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.sterne x), ''))) then raise exception 'FEHLER 3: Lernstand/Plan/Sterne verändert'; end if;
  select count(*) into v_n from schule.wdh_staffel_sicherung where lauf = 'wd5';
  raise notice 'Test 3: nur Fälligkeit gesetzter Erst-Wiederholungen geändert (% gesichert); offene Runde, übrige Etappen, Lernstand, Plan, Sterne unverändert: OK', v_n;
end $$;

-- Test 4: Rückweg für den echten Bestand: alle Kinder zurück → Fälligkeit wie in der WD-5-Sicherung (= vor WD-5), übrige Karten unverändert;
-- ältere WD-4b-Sicherungen wieder an ihrem Platz. Danach erneut drosseln (für Test 5 und als Probe, dass es wiederholbar zum selben Ergebnis führt).
do $$
declare v_n int; v_s4b int; v_soll int; v_nach_1 text; v_nach_2 text;
begin
  create temp table wd5_sich on commit drop as select s.lernender_id, s.einheit_id, s.lernziel, s.faellig_am, s.wdh_ab, s.wdh_lerntage
    from schule.wdh_staffel_sicherung s where s.lauf = 'wd5' and s.zurueck_am is null;
  create temp table wd5_vor_rueck on commit drop as select k.* from schule.karte_stand k;
  select count(*), count(*) filter (where frueher is not null) into v_soll, v_s4b from schule.wdh_staffel_sicherung where lauf = 'wd5' and zurueck_am is null;
  select string_agg(k.lernender_id || ':' || k.einheit_id || ':' || k.lernziel || ':' || coalesce(schule.karte_wdh_in(k), -1), '|' order by k.lernender_id, k.einheit_id, k.lernziel)
    into v_nach_1 from schule.karte_stand k;
  v_n := schule.wdh_drosseln_zurueck(null);
  if v_n <> v_soll then raise exception 'FEHLER 4: % statt % zurück', v_n, v_soll; end if;
  if exists (select 1 from wd5_sich s join schule.karte_stand k using (lernender_id, einheit_id, lernziel)
              where (k.faellig_am, k.wdh_ab, k.wdh_lerntage) is distinct from (s.faellig_am, s.wdh_ab, s.wdh_lerntage))
     or exists (select 1 from wd5_vor_rueck v join schule.karte_stand k using (lernender_id, einheit_id, lernziel)
                 where not exists (select 1 from wd5_sich s where s.lernender_id = v.lernender_id and s.einheit_id = v.einheit_id and s.lernziel = v.lernziel)
                   and (k.faellig_am, k.wdh_ab, k.wdh_lerntage) is distinct from (v.faellig_am, v.wdh_ab, v.wdh_lerntage)) then
    raise exception 'FEHLER 4: Rückweg stellt die Fälligkeit nicht her'; end if;
  if exists (select 1 from schule.wdh_staffel_sicherung where lauf = 'wd5' and zurueck_am is null) or exists (select 1 from schule.wdh_staffel_sicherung where frueher is not null) then
    raise exception 'FEHLER 4: Sicherungen nach dem Rückweg nicht abgeschlossen'; end if;
  -- erneut drosseln: gleiches Ergebnis wie vorher
  update schule.wdh_staffel_sicherung set lauf = 'wd5_alt' where lauf = 'wd5';
  perform schule.wdh_staffel_drosseln(null);
  select string_agg(k.lernender_id || ':' || k.einheit_id || ':' || k.lernziel || ':' || coalesce(schule.karte_wdh_in(k), -1), '|' order by k.lernender_id, k.einheit_id, k.lernziel)
    into v_nach_2 from schule.karte_stand k;
  if v_nach_2 is distinct from v_nach_1 then raise exception 'FEHLER 4: erneutes Drosseln gibt eine andere Verteilung'; end if;
  raise notice 'Test 4: Rückweg echter Bestand – % Etappen zurück, % WD-4b-Sicherungen wiederhergestellt; erneut gedrosselt mit gleicher Verteilung: OK', v_n, v_s4b;
end $$;

-- Test 5 (Testkind): offene Runde unberührt, belegt heutige Plätze; 3 je Lerntag in Plan-Reihenfolge; nicht gesetzte und höhere Stufen bleiben;
-- Rückweg nach einer Zwischenübung abgelehnt, sonst zurück; wdh_staffel_tag plant neu gesetzte hinter die gestaffelten
create function pg_temp.wd5_karte(p_l bigint, p_e bigint, p_lz text, p_stufe int, p_tag int, p_gesetzt boolean) returns void language plpgsql as $f$
begin
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel) values (p_l, p_e, p_lz) on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '30 days', wdh_stufe = p_stufe, wdh_fehler = 0,
         wdh_ab = case when p_tag = 0 then null else now() end, wdh_lerntage = case when p_tag = 0 then null else p_tag end,
         faellig_am = case when p_tag = 0 then now() - interval '1 day' else now() + p_tag * interval '1 day' end,
         gesetzt_am = case when p_gesetzt then now() - interval '5 days' end, wdh_gesetzt_am = case when p_gesetzt then now() - interval '5 days' end
   where lernender_id = p_l and einheit_id = p_e and lernziel = p_lz;
end $f$;
create temp table wd5_t on commit drop as
  select row_number() over (order by p.e, p.nr) nr, p.e, p.lz from (
    select e.id e, et.o nr, et.x->>'lernziel' lz from schule.einheit e cross join lateral jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality et(x, o)
     where e.id = schule.thema_einheit(e.thema_id) and e.block_id is not null and et.x->>'lernziel' is not null
     order by e.id, et.o limit 12) p;
do $$
declare v_l bigint := (select id from schule.lernender where ist_test and aktiv order by id limit 1); v_n int; v_x int; v_fehler text; v_e bigint; v_lz text;
begin
  if v_l is null or (select count(*) from wd5_t) < 12 then raise notice 'Test 5: kein Testkind oder zu wenig Etappen – übersprungen'; return; end if;
  update schule.karte_stand set sitzt = false, faellig_am = null, wdh_ab = null, wdh_lerntage = null where lernender_id = v_l;
  -- 1–2: gesetzt, heute fällig, in der offenen Runde; 3–6: gesetzt, heute fällig; 7–8: gesetzt, Lerntag 1; 9: gesetzt Stufe 1; 10: nicht gesetzt, fällig
  perform pg_temp.wd5_karte(v_l, t.e, t.lz, case when t.nr = 9 then 1 else 0 end, case when t.nr in (7, 8) then 1 else 0 end, t.nr <> 10) from wd5_t t where t.nr <= 10;
  insert into schule.wdh_runde (lernender_id, tag) values (v_l, schule.heute_tag(v_l)) on conflict do nothing;
  update schule.wdh_runde set fertig_am = null where lernender_id = v_l and tag = schule.heute_tag(v_l);
  insert into schule.wdh_runde_etappe (lernender_id, tag, nr, einheit_id, lernziel) select v_l, schule.heute_tag(v_l), 900 + t.nr, t.e, t.lz from wd5_t t where t.nr <= 2 on conflict do nothing;
  create temp table wd5_t_vorher on commit drop as select k.* from schule.karte_stand k where k.lernender_id = v_l;
  v_n := schule.wdh_staffel_drosseln(v_l);
  -- erwartet: Runde (1, 2) bleibt; heute 1 Platz frei → 3; Lerntag 1: 4, 5, 6; Lerntag 2: 7, 8; 9 und 10 unverändert
  if exists (select 1 from wd5_t t join schule.karte_stand k on k.lernender_id = v_l and k.einheit_id = t.e and k.lernziel = t.lz
              where t.nr <= 8 and schule.karte_wdh_in(k) <> case when t.nr <= 3 then 0 when t.nr <= 6 then 1 else 2 end) then
    raise exception 'FEHLER 5: Staffel falsch: %', (select string_agg(t.nr || ':' || schule.karte_wdh_in(k), ' ' order by t.nr) from wd5_t t
                                                     join schule.karte_stand k on k.lernender_id = v_l and k.einheit_id = t.e and k.lernziel = t.lz); end if;
  if exists (select 1 from wd5_t t join schule.karte_stand k on k.lernender_id = v_l and k.einheit_id = t.e and k.lernziel = t.lz join wd5_t_vorher v using (lernender_id, einheit_id, lernziel)
              where t.nr in (1, 2, 9, 10) and (k.faellig_am, k.wdh_ab, k.wdh_lerntage) is distinct from (v.faellig_am, v.wdh_ab, v.wdh_lerntage)) then
    raise exception 'FEHLER 5: offene Runde, höhere Stufe oder nicht gesetzte Etappe verschoben'; end if;
  if v_n <> 5 then raise exception 'FEHLER 5: % statt 5 verschoben (3 bleibt heute)', v_n; end if;
  -- neu gesetzte kommen hinter die gestaffelten (Lerntag 2 hat noch 1 Platz)
  if schule.wdh_staffel_tag(v_l) <> 2 then raise exception 'FEHLER 5: wdh_staffel_tag % statt 2', schule.wdh_staffel_tag(v_l); end if;
  -- Rückweg: nach einer Zwischenübung abgelehnt, sonst zurück
  select s.einheit_id, s.lernziel into v_e, v_lz from schule.wdh_staffel_sicherung s where s.lernender_id = v_l and s.lauf = 'wd5' limit 1;
  update schule.karte_stand set falsch = falsch + 1 where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  begin perform schule.wdh_drosseln_zurueck(v_l); v_fehler := 'kein Fehler'; exception when others then v_fehler := sqlerrm; end;
  if v_fehler = 'kein Fehler' then raise exception 'FEHLER 5: Rückweg trotz Zwischenübung'; end if;
  update schule.karte_stand set falsch = falsch - 1 where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  v_x := schule.wdh_drosseln_zurueck(v_l);
  if v_x <> v_n or exists (select 1 from wd5_t_vorher v join schule.karte_stand k using (lernender_id, einheit_id, lernziel)
                            where (k.faellig_am, k.wdh_ab, k.wdh_lerntage) is distinct from (v.faellig_am, v.wdh_ab, v.wdh_lerntage)) then
    raise exception 'FEHLER 5: Rückweg (% verschoben, % zurück)', v_n, v_x; end if;
  -- WD-4b-Rückweg fasst WD-5-Sicherungen nicht an
  if schule.wdh_staffel_zurueck(v_l) <> 0 then raise exception 'FEHLER 5: WD-4b-Rückweg fasst WD-5 an'; end if;
  raise notice 'Test 5: Testkind – offene Runde (2) bleibt und belegt heute, 3 je Lerntag in Plan-Reihenfolge, % verschoben, neu Gesetzte ab Lerntag 2, Rückweg nach Zwischenübung abgelehnt (%), sonst zurück: OK',
    v_n, left(v_fehler, 60);
end $$;

rollback;
