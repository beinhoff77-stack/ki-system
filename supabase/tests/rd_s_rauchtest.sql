-- Rauchtest RD-S (Reise-Aufbau in die Datenbank, Reisekarte je Kind). Läuft vollständig in einer Transaktion mit Rollback.
-- Spielt Migration 20261125_rd_s_reise.sql und inhalte/reise/rd_einspiel_2311.sql (beide wiederholbar) selbst ein – vorher oder schon eingespielt, beides geht.
-- Voraussetzung: Teilung (TL-S 7) eingespielt. Aufruf aus dem Repo-Wurzelverzeichnis: psql -v ON_ERROR_STOP=1 -f supabase/tests/rd_s_rauchtest.sql
-- Ausgabe nur Zahlen, keine Namen, keine Kinderdaten. Änderungen am Testkind (Gruppe, Karten) nur innerhalb dieser Transaktion.
begin;

-- Vorher: Lernstand, Sterne, Stempel, Route, Ortsnamen, Reiseoptionen je Kind
create temp table rd_rt_vorher on commit drop as
  select 'karte_stand' t, md5(coalesce(string_agg(k::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel), '')) h from schule.karte_stand k
  union all select 'lernziel_stand', md5(coalesce(string_agg(s::text, '|' order by s.lernender_id, s.einheit_id, s.lernziel), '')) from schule.lernziel_stand s
  union all select 'lernstand', md5(coalesce(string_agg(s::text, '|' order by s.lernender_id, s.thema_id), '')) from schule.lernstand s
  union all select 'sterne', md5(coalesce(string_agg(s::text, '|' order by s.id), '')) from schule.sterne s
  union all select 'flug_erstabschluss', md5(coalesce(string_agg(f::text, '|' order by f.lernender_id, f.einheit_id), '')) from schule.flug_erstabschluss f
  union all select 'route', md5(coalesce(string_agg(r::text, '|' order by r.id), '')) from schule.route r
  union all select 'block', md5(coalesce(string_agg(b::text, '|' order by b.id), '')) from schule.block b
  union all select 'kontinent', md5(coalesce(string_agg(k::text, '|' order by k.id), '')) from schule.kontinent k
  union all select 'reiseoptionen_' || l.id, md5(schule.reiseoptionen(l.id)::text) from schule.lernender l where l.aktiv;

-- Migration nur, wenn noch nicht eingespielt (sonst würde sie spätere Änderungen an reise_karte, z. B. ZP-S, in diesem Lauf überschreiben)
select to_regclass('schule.reise_land') is null as rd_fehlt \gset
\if :rd_fehlt
\ir ../migrations/20261125_rd_s_reise.sql
\endif
\ir ../../inhalte/reise/rd_einspiel_2311.sql
-- zweimal: wiederholbar, gleiche Zahlen
create temp table rd_rt_zahl on commit drop as
  select (select count(*) from schule.reise_land) l, (select count(*) from schule.reise_stadt) s, (select count(*) from schule.reise_station) st,
         (select md5(string_agg(x::text, '|' order by x.geonames_id)) from schule.reise_stadt x) h;
\ir ../../inhalte/reise/rd_einspiel_2311.sql

do $$
declare v_n int; v_m int; v_x record; v_k jsonb; v_l bigint; v_gr text; v_f jsonb; v_s jsonb; v_e bigint; v_cnt int; v_len int;
begin
  -- 0) wiederholbar
  if (select (l, s, st, h) from rd_rt_zahl) is distinct from
     (select ((select count(*) from schule.reise_land), (select count(*) from schule.reise_stadt), (select count(*) from schule.reise_station),
              (select md5(string_agg(x::text, '|' order by x.geonames_id)) from schule.reise_stadt x))) then
    raise exception 'Test 0: zweites Einspielen ändert die Daten';
  end if;
  raise notice 'Test 0 ok: Einspielen wiederholbar';

  -- 1) jede freigegebene Etappe jedes Mathe-Themas mit Flug hat genau eine Stadt, jede Etappen-Stadt hat ihre Etappe
  select count(*) into v_n
    from schule.thema t join schule.einheit e on e.id = schule.thema_einheit(t.id), jsonb_array_elements(e.inhalt->'etappen') x
   where t.fach = 'Mathematik' and e.status = 'freigegeben'
     and (select count(*) from schule.reise_stadt s where s.art = 'etappe' and s.thema_id = t.id and s.lernziel = x->>'lernziel') <> 1;
  if v_n > 0 then raise exception 'Test 1: % Etappen ohne genau eine Stadt', v_n; end if;
  select count(*) into v_n from schule.thema t where t.fach = 'Mathematik' and exists (select 1 from schule.einheit e where e.thema_id = t.id and e.status = 'freigegeben')
     and not exists (select 1 from schule.reise_land l where l.thema_id = t.id);
  if v_n > 0 then raise exception 'Test 1: % freigegebene Themen ohne Land', v_n; end if;
  select count(*) into v_n from schule.reise_abweichung;
  if v_n > 0 then raise exception 'Test 1: % Abweichungen in reise_abweichung', v_n; end if;
  select count(*) into v_m from schule.reise_stadt where art = 'etappe';
  raise notice 'Test 1 ok: % Etappen-Städte, jede freigegebene Etappe genau eine Stadt, % Flüge', v_m, (select count(*) from schule.reise_land where art = 'flug');

  -- 2) kein Land und keine Stadt doppelt (auch über Flug und Reserve), je Expedition eine Station, Städte im Land ihres Flugs
  if (select count(*) <> count(distinct (iso, region_schluessel)) or count(*) <> count(distinct name) from schule.reise_land) then raise exception 'Test 2: Land doppelt'; end if;
  if (select count(*) <> count(distinct geonames_id) from schule.reise_stadt) then raise exception 'Test 2: Stadt doppelt'; end if;
  if exists (select 1 from schule.reise_stadt s join schule.reise_land l on l.id = s.land_id where s.art = 'etappe' and l.thema_id is distinct from s.thema_id) then
    raise exception 'Test 2: Stadt in fremdem Land'; end if;
  if (select count(*) from schule.expedition) <> (select count(*) from schule.reise_station_expedition) then raise exception 'Test 2: Expedition ohne Station'; end if;
  begin
    insert into schule.reise_stadt (art, land_id, name, breite, laenge, geonames_id, reihenfolge)
    select 'reserve', s.land_id, 'x', 0, 0, s.geonames_id, 999 from schule.reise_stadt s limit 1;
    raise exception 'Test 2: doppelte Stadt wurde angenommen';
  exception when unique_violation then null; end;
  begin
    insert into schule.reise_stadt (art, land_id, thema_id, lernziel, name, breite, laenge, geonames_id, reihenfolge)
    select 'etappe', s.land_id, s.thema_id, s.lernziel, 'x', 0, 0, -1, 998 from schule.reise_stadt s where s.art = 'etappe' limit 1;
    raise exception 'Test 2: zweite Stadt für eine Etappe wurde angenommen';
  exception when unique_violation then null; end;
  begin
    insert into schule.reise_land (art, kontinent_id, name, iso, region, mitte_breite, mitte_laenge, hauptstadt_name, hauptstadt_breite, hauptstadt_laenge, reihenfolge)
    select 'reserve', l.kontinent_id, 'x', l.iso, l.region, 0, 0, 'x', 0, 0, 999 from schule.reise_land l limit 1;
    raise exception 'Test 2: doppeltes Land wurde angenommen';
  exception when unique_violation then null; end;
  raise notice 'Test 2 ok: % Länder, % Städte, % Stationen, keine doppelt; Regeln greifen',
    (select count(*) from schule.reise_land), (select count(*) from schule.reise_stadt), (select count(*) from schule.reise_station);

  -- 4) Stufe/Stempel der Karte = thema_stufe/Erstabschluss, Pflicht = stufe_etappen, Zusatz = thema.zusatz – für jedes Kind (nur lesen)
  for v_x in select id from schule.lernender where aktiv order by id loop
    v_k := schule.reise_karte(v_x.id);
    v_len := length(v_k::text);
    v_cnt := 0;
    for v_f in select f from jsonb_array_elements(v_k->'kontinente') k, jsonb_array_elements(k->'fluege') f loop
      v_cnt := v_cnt + 1;
      v_e := schule.thema_einheit((v_f->>'thema_id')::bigint);
      if v_f->>'stufe' is distinct from schule.thema_stufe(v_x.id, (v_f->>'thema_id')::bigint)->>'stufe' then
        raise exception 'Test 4: Stufe weicht ab (Kind %, Thema %)', v_x.id, v_f->>'thema_id'; end if;
      if (v_f->>'stempel')::boolean is distinct from exists (select 1 from schule.flug_erstabschluss fe where fe.lernender_id = v_x.id and fe.einheit_id = v_e) then
        raise exception 'Test 4: Stempel weicht ab (Kind %, Thema %)', v_x.id, v_f->>'thema_id'; end if;
      if not coalesce((v_f->>'zusatz_eingeplant')::boolean, false)
         and (select array_agg(s->>'lernziel' order by s->>'lernziel') from jsonb_array_elements(v_f->'staedte') s where (s->>'pflicht')::boolean)
         is distinct from (select array_agg(x order by x) from unnest(schule.stufe_etappen(v_x.id, v_e)) x) then
        raise exception 'Test 4: Pflicht/Kür weicht von stufe_etappen ab (Kind %, Thema %)', v_x.id, v_f->>'thema_id'; end if;
      if (v_f->>'zusatz')::boolean is distinct from coalesce((select schule.kind_gruppe(v_x.id) = any(t.zusatz) from schule.thema t where t.id = (v_f->>'thema_id')::bigint), false) then
        raise exception 'Test 4: Zusatz weicht ab (Kind %, Thema %)', v_x.id, v_f->>'thema_id'; end if;
      if (v_f->>'golden')::boolean and v_f->>'stufe' <> 'komplett' then raise exception 'Test 4: golden ohne komplett (Kind %, Thema %)', v_x.id, v_f->>'thema_id'; end if;
      -- RD-S 2: Stand je Stadt und Zähler je Flug nach derselben Regel (karte_sicher / sitzt), golden = alle Etappen der Regel sicher
      if (v_f->>'sicher')::int is distinct from (select count(*)::int from jsonb_array_elements(v_f->'staedte') s where coalesce((s->>'zaehlt')::boolean, (s->>'pflicht')::boolean) and s->>'stand' = 'sicher')
         or (v_f->>'gelandet')::int is distinct from (select count(*)::int from jsonb_array_elements(v_f->'staedte') s where coalesce((s->>'zaehlt')::boolean, (s->>'pflicht')::boolean) and s->>'stand' in ('gelandet', 'sicher'))
         or (v_f->>'sicher')::int is distinct from (schule.thema_stufe(v_x.id, (v_f->>'thema_id')::bigint)->>'sicher')::int
         or (v_f->>'golden')::boolean is distinct from ((v_f->>'etappen')::int > 0 and (v_f->>'sicher')::int = (v_f->>'etappen')::int) then
        raise exception 'Test 4: Stand je Stadt und Zähler sicher/gelandet/golden passen nicht (Kind %, Thema %)', v_x.id, v_f->>'thema_id'; end if;
    end loop;
    if v_cnt <> (select count(*) from schule.reise_land l where l.art = 'flug' and schule.thema_einheit(l.thema_id) is not null) then
      raise exception 'Test 4: Karte zeigt % statt aller Flüge (Kind %)', v_cnt, v_x.id; end if;
    if jsonb_typeof(v_k->'naechster_start') = 'object' and not exists (select 1 from jsonb_array_elements(v_k->'kontinente') k, jsonb_array_elements(k->'fluege') f
                                                        where f->>'thema_id' = v_k->'naechster_start'->>'thema_id' and f->>'stufe' in ('dran', 'kommt')) then
      raise exception 'Test 4: nächster Start ist kein Flug „dran“/„kommt“ (Kind %)', v_x.id; end if;
    raise notice 'Test 4 ok: Kind % – % Flüge, Antwort % Bytes, nächster Start %', v_x.id, v_cnt, v_len, coalesce(v_k->'naechster_start'->>'thema_id', '-');
  end loop;

  -- 5) Zugriff: ungültiger Schlüssel → Fehler
  begin
    perform api.schule_reise_karte('ungueltig', jsonb_build_object('lernender_id', (select min(id) from schule.lernender)));
    raise exception 'Test 5: Zugriff ohne gültigen Schlüssel';
  exception when sqlstate 'P0001' then
    if sqlerrm like 'Test 5%' then raise; end if;
  end;
  raise notice 'Test 5 ok: Aktion prüft den Zugriff';
end $$;

-- 6) unverändert: Lernstand, Sterne, Stempel, Route, Ortsnamen, Reiseoptionen (nach Einspielen und Lesen der Karte für alle Kinder)
do $$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from rd_rt_vorher v
   where v.h is distinct from (case v.t
     when 'karte_stand' then (select md5(coalesce(string_agg(k::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel), '')) from schule.karte_stand k)
     when 'lernziel_stand' then (select md5(coalesce(string_agg(s::text, '|' order by s.lernender_id, s.einheit_id, s.lernziel), '')) from schule.lernziel_stand s)
     when 'lernstand' then (select md5(coalesce(string_agg(s::text, '|' order by s.lernender_id, s.thema_id), '')) from schule.lernstand s)
     when 'sterne' then (select md5(coalesce(string_agg(s::text, '|' order by s.id), '')) from schule.sterne s)
     when 'flug_erstabschluss' then (select md5(coalesce(string_agg(f::text, '|' order by f.lernender_id, f.einheit_id), '')) from schule.flug_erstabschluss f)
     when 'route' then (select md5(coalesce(string_agg(r::text, '|' order by r.id), '')) from schule.route r)
     when 'block' then (select md5(coalesce(string_agg(b::text, '|' order by b.id), '')) from schule.block b)
     when 'kontinent' then (select md5(coalesce(string_agg(k::text, '|' order by k.id), '')) from schule.kontinent k)
     else (select md5(schule.reiseoptionen(substr(v.t, 15)::bigint)::text)) end);
  if v_t is not null then raise exception 'Test 6: verändert: %', v_t; end if;
  raise notice 'Test 6 ok: Lernstand, Sterne, Stempel, Route, Ortsnamen und Reiseoptionen unverändert (% Prüfwerte)', (select count(*) from rd_rt_vorher);
end $$;

-- 3) Karte für das Testkind in jeder der fünf Gruppen; Stand je Etappe (offen · begonnen · gelandet · sicher · wieder offen), golden
do $$
declare v_l bigint; v_sa text; v_zw text; v_g record; v_k jsonb; v_f jsonb; v_e bigint; v_lz text[]; v_t bigint; v_st text; v_gr text[] := '{}';
begin
  select id, schulart, zweig into v_l, v_sa, v_zw from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'Test 3: kein Testkind'; end if;
  for v_g in select * from (values ('gym_by', null::text, 'gym_by'), ('rs_by', 'rs_I', 'rs_I'), ('rs_by', 'rs_II_III', 'rs_II_III'),
                                   ('ib_myp', 'myp_standard', 'myp_standard'), ('ib_myp', 'myp_extended', 'myp_extended')) g(sa, zw, gruppe) loop
    update schule.lernender set schulart = v_g.sa, zweig = v_g.zw where id = v_l;
    if schule.kind_gruppe(v_l) <> v_g.gruppe then raise exception 'Test 3: Gruppe % nicht einstellbar', v_g.gruppe; end if;
    v_k := schule.reise_karte(v_l);
    if v_k->>'gruppe' <> v_g.gruppe or jsonb_array_length(v_k->'kontinente') <> (select count(*) from schule.reise_kontinent) then
      raise exception 'Test 3: Karte in Gruppe % unvollständig', v_g.gruppe; end if;
    for v_f in select f from jsonb_array_elements(v_k->'kontinente') k, jsonb_array_elements(k->'fluege') f loop
      v_e := schule.thema_einheit((v_f->>'thema_id')::bigint);
      if not coalesce((v_f->>'zusatz_eingeplant')::boolean, false)
         and (select array_agg(s->>'lernziel' order by s->>'lernziel') from jsonb_array_elements(v_f->'staedte') s where (s->>'pflicht')::boolean)
         is distinct from (select array_agg(x order by x) from unnest(schule.stufe_etappen(v_l, v_e)) x) then
        raise exception 'Test 3: Pflicht/Kür in Gruppe % weicht ab (Thema %)', v_g.gruppe, v_f->>'thema_id'; end if;
      if jsonb_array_length(v_f->'staedte') <> jsonb_array_length((select e.inhalt->'etappen' from schule.einheit e where e.id = v_e)) then
        raise exception 'Test 3: Städte ≠ Etappen (Gruppe %, Thema %)', v_g.gruppe, v_f->>'thema_id'; end if;
      if v_f->'quellen' is not null then null; end if;
    end loop;
    if jsonb_array_length(v_k->'quellen') < 2 or not exists (select 1 from jsonb_array_elements(v_k->'quellen') q where q->>'lizenz' = 'CC BY 4.0' and q->>'quelle' = 'GeoNames')
       or not exists (select 1 from jsonb_array_elements(v_k->'quellen') q where q->>'quelle' = 'Natural Earth') then
      raise exception 'Test 3: Quellenangabe fehlt'; end if;
    v_gr := v_gr || (v_g.gruppe || ':' || (select count(*) from jsonb_array_elements(v_k->'kontinente') k, jsonb_array_elements(k->'fluege') f, jsonb_array_elements(f->'staedte') s
                                             where not (s->>'pflicht')::boolean) || ' Kür/' ||
                     (select count(*) from jsonb_array_elements(v_k->'kontinente') k, jsonb_array_elements(k->'fluege') f where (f->>'zusatz')::boolean) || ' Zusatz');
  end loop;
  raise notice 'Test 3 ok: Karte in allen fünf Gruppen (%)', array_to_string(v_gr, ', ');

  -- Stand je Etappe: Testkind (gym_by), Thema 15 mit fünf Karten in fünf Zuständen, danach alles sicher → golden
  update schule.lernender set schulart = 'gym_by', zweig = null where id = v_l;
  v_t := 15; v_e := schule.thema_einheit(v_t);
  select array_agg(x->>'lernziel' order by o) into v_lz from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') with ordinality q(x, o) where e.id = v_e;
  -- „sicher“ = schule.karte_sicher (dieselbe Regel wie der Zähler sicher in thema_stufe): live sitzt + wdh_stufe ≥ 4 und Nachweis;
  --   hier über „Kann er – aber wiederholen“ (gesetzt_am, ohne Mischkarte seitdem). Erste Karte sicher, zweite nur gelandet (wdh_stufe 0).
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am, wdh_stufe, richtig, falsch, gesetzt_am, gesetzt_von, misch_ok_am)
  values (v_l, v_e, v_lz[1], true, now(), 4, 5, 0, now(), 'rauchtest', null), (v_l, v_e, v_lz[2], true, now(), 0, 5, 0, null, null, null),
         (v_l, v_e, v_lz[3], false, now(), 0, 5, 1, null, null, null), (v_l, v_e, v_lz[4], false, null, 0, 1, 1, null, null, null),
         (v_l, v_e, v_lz[5], false, null, 0, 0, 0, null, null, null)
  on conflict (lernender_id, einheit_id, lernziel) do update set sitzt = excluded.sitzt, sitzt_am = excluded.sitzt_am, wdh_stufe = excluded.wdh_stufe,
     richtig = excluded.richtig, falsch = excluded.falsch, gesetzt_am = excluded.gesetzt_am, gesetzt_von = excluded.gesetzt_von, misch_ok_am = excluded.misch_ok_am;
  if not schule.karte_sicher((select k from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = v_e and k.lernziel = v_lz[1])) then
    raise exception 'Test 3: Aufbau „sicher“ greift nicht (karte_sicher)'; end if;
  v_k := schule.reise_karte(v_l);
  select string_agg(s->>'stand', ',' order by (s->>'nr')::int) into v_st
    from jsonb_array_elements(v_k->'kontinente') k, jsonb_array_elements(k->'fluege') f, jsonb_array_elements(f->'staedte') s
   where (f->>'thema_id')::bigint = v_t and (s->>'nr')::int <= 5;
  if v_st <> 'sicher,gelandet,wieder_offen,begonnen,offen' then raise exception 'Test 3: Stand je Etappe falsch: %', v_st; end if;
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am, wdh_stufe, richtig, falsch, gesetzt_am, gesetzt_von, misch_ok_am)
  select v_l, v_e, x, true, now(), 4, 5, 0, now(), 'rauchtest', null from unnest(v_lz) x
  on conflict (lernender_id, einheit_id, lernziel) do update set sitzt = true, sitzt_am = now(), wdh_stufe = 4, gesetzt_am = now(), gesetzt_von = 'rauchtest', misch_ok_am = null;
  v_k := schule.reise_karte(v_l);
  select f into v_f from jsonb_array_elements(v_k->'kontinente') k, jsonb_array_elements(k->'fluege') f where (f->>'thema_id')::bigint = v_t;
  if not (v_f->>'golden')::boolean or v_f->>'stufe' <> 'komplett' or v_f->>'stufe' <> schule.thema_stufe(v_l, v_t)->>'stufe' then
    raise exception 'Test 3: golden/komplett falsch (stufe %, golden %)', v_f->>'stufe', v_f->>'golden'; end if;
  raise notice 'Test 3 ok: Stand je Etappe (sicher, gelandet, wieder offen, begonnen, offen) nach karte_sicher und golden = alles sicher';
  update schule.lernender set schulart = v_sa, zweig = v_zw where id = v_l;
end $$;

rollback;
