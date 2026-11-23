-- WD-5 (Entscheidung Sebastian 23.11. 03:37): Zulauf gesetzter Etappen drosseln – 3 statt 6 je Lerntag.
-- NUR nach Probelauf und Sebastians Okay einspielen. Nach WD-S, WD-4b, WD-S 4 (alle live).
--
-- Was passiert – in Worten:
--   1. Regel wdh_gesetzt_je_lerntag = 3. Neu gesetzte Etappen („Kann er – aber wiederholen“) kommen damit nur noch zu 3 je Lerntag in den Takt
--      (schule.wdh_staffel_tag liest die Regel), ebenso wdh_staffel_strecken.
--   2. Einmalige Neuverteilung je Kind (schule.wdh_staffel_drosseln): alle gesetzten Etappen in erster Wiederholung (wdh_gesetzt_am gesetzt, Stufe 0,
--      kein Wiederholungs-Fehler, nicht abgelegt) – heute fällige UND schon für spätere Lerntage eingeplante – werden in Plan-Reihenfolge
--      (Platz im Plan, Einheit, Etappen-Reihenfolge) neu gestaffelt: höchstens 3 je Lerntag, ab heute (Lerntag 0).
--      Etappen der offenen Wiederholungs-Runde von heute bleiben, wie sie sind, und belegen heutige Plätze.
--      Gezählt wird in Lerntagen (wdh_ab + wdh_lerntage wie überall im Takt). Geändert werden nur faellig_am, wdh_ab, wdh_lerntage – und nur,
--      wenn sich der Lerntag ändert. Nicht gesetzte Etappen und höhere Stufen bleiben unverändert. Landung, Stufe, Belege, Sterne, Lernstände,
--      Plan bleiben; das wird am Ende geprüft (sonst Abbruch).
--   3. Alter Stand in schule.wdh_staffel_sicherung (lauf = 'wd5'). Stand dort für eine Etappe schon eine WD-4b-Sicherung, wird sie in der
--      neuen Spalte frueher aufbewahrt (nichts geht verloren) und beim Rückweg wiederhergestellt.
--      Rückweg (nur solange keine dieser Etappen seitdem beantwortet wurde, sonst Ablehnung ohne Änderung):
--        select schule.wdh_drosseln_zurueck();        -- alle Kinder, oder schule.wdh_drosseln_zurueck(<Kind>)
--      Die Regel stellt der Rückweg nicht zurück (bei Bedarf: update schule.regel set wert = '6' where schluessel = 'wdh_gesetzt_je_lerntag').
--      schule.wdh_staffel_zurueck (WD-4b) fasst ab jetzt nur noch WD-4b-Sicherungen an (lauf is null).
--   Einmalig: Ein zweiter Lauf tut nichts (es gibt schon WD-5-Sicherungen). Ausgabe (NOTICE) je Kind nur mit Nummer.
-- Kein DROP, kein DELETE.

do $$ begin
  if to_regclass('schule.wdh_staffel_sicherung') is null or to_regprocedure('schule.wdh_staffel_tag(bigint)') is null
     or to_regprocedure('schule.karte_wdh_in(schule.karte_stand)') is null then
    raise exception 'WD-5: zuerst WD-S/WD-4b/WD-S 4 einspielen'; end if;
end $$;

alter table schule.wdh_staffel_sicherung add column if not exists lauf text;        -- null = WD-4b, 'wd5' = WD-5
alter table schule.wdh_staffel_sicherung add column if not exists frueher jsonb;     -- überschriebene ältere Sicherung derselben Etappe
comment on column schule.wdh_staffel_sicherung.lauf is 'null = WD-4b (Strecken), wd5 = WD-5 (Drosseln auf 3 je Lerntag)';
comment on column schule.wdh_staffel_sicherung.frueher is 'WD-5: ältere Sicherung derselben Etappe (wird beim Rückweg von WD-5 wiederhergestellt)';

-- 1. Regel
update schule.regel set wert = '3'::jsonb, hinweis = 'WD-4/WD-5: gesetzte Etappen, die je Lerntag neu in den Takt kommen (WD-5: 3 statt 6)'
 where schluessel = 'wdh_gesetzt_je_lerntag';
insert into schule.regel (schluessel, wert, hinweis)
select 'wdh_gesetzt_je_lerntag', '3'::jsonb, 'WD-4/WD-5: gesetzte Etappen, die je Lerntag neu in den Takt kommen (WD-5: 3 statt 6)'
 where not exists (select 1 from schule.regel where schluessel = 'wdh_gesetzt_je_lerntag');

-- Gesetzte Erst-Wiederholungen eines Kindes mit Lerntag (0 = heute fällig) und Plan-Reihenfolge
create or replace function schule.wdh_gesetzt_erst(p_l bigint)
 returns table (einheit_id bigint, lernziel text, tag int, in_runde boolean, platz int, etappe_nr int)
 language sql stable set search_path to ''
as $$
  select x.einheit_id, x.lernziel, schule.karte_wdh_in(x),
         exists (select 1 from schule.wdh_runde_etappe r join schule.wdh_runde w on w.lernender_id = r.lernender_id and w.tag = r.tag and w.fertig_am is null
                  where r.lernender_id = x.lernender_id and r.tag = schule.heute_tag(x.lernender_id) and r.einheit_id = x.einheit_id and r.lernziel = x.lernziel),
         coalesce((select min(ro.position) from schule.route ro where ro.lernender_id = x.lernender_id and ro.block_id = e.block_id and ro.art = 'normal'), 2147483647),
         coalesce((select et.nr::int from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality et(y, nr) where et.y->>'lernziel' = x.lernziel), 999)
    from schule.karte_stand x join schule.einheit e on e.id = x.einheit_id
   where x.lernender_id = p_l and x.sitzt and x.wdh_gesetzt_am is not null and x.wdh_stufe = 0 and x.wdh_fehler = 0
     and schule.karte_wdh_in(x) is not null
     and not exists (select 1 from schule.abgelegt g where g.lernender_id = x.lernender_id and g.bezug = 'etappe:' || x.einheit_id || ':' || x.lernziel);
$$;
revoke all on function schule.wdh_gesetzt_erst(bigint) from public, anon, authenticated;

-- 2. Neuverteilung (je Kind oder alle); liefert die Zahl verschobener Etappen
create or replace function schule.wdh_staffel_drosseln(p_l bigint default null)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_je int := greatest(schule.wd_regel('wdh_gesetzt_je_lerntag', 3), 1); v_kind bigint; k record; v_frei int; v_tag int; v_n int := 0; v_alt record;
begin
  for v_kind in select l.id from schule.lernender l where (p_l is null or l.id = p_l) order by l.id loop
    if exists (select 1 from schule.wdh_staffel_sicherung s where s.lernender_id = v_kind and s.lauf = 'wd5') then continue; end if;   -- einmalig
    perform 1 from schule.karte_stand x where x.lernender_id = v_kind order by x.einheit_id, x.lernziel for update;                 -- wie WD-S 4
    v_tag := 0;
    v_frei := v_je - (select count(*) from schule.wdh_gesetzt_erst(v_kind) g where g.in_runde and g.tag = 0);                      -- offene Runde belegt heute
    for k in select g.*, x.faellig_am, x.wdh_ab, x.wdh_lerntage, x.richtig, x.falsch
               from schule.wdh_gesetzt_erst(v_kind) g join schule.karte_stand x on x.lernender_id = v_kind and x.einheit_id = g.einheit_id and x.lernziel = g.lernziel
              where not g.in_runde
              order by g.platz, g.einheit_id, g.etappe_nr, g.lernziel loop
      while v_frei <= 0 loop v_tag := v_tag + 1; v_frei := v_je; end loop;
      v_frei := v_frei - 1;
      if k.tag = v_tag then continue; end if;                                                                                     -- Lerntag bleibt
      select s.* into v_alt from schule.wdh_staffel_sicherung s where s.lernender_id = v_kind and s.einheit_id = k.einheit_id and s.lernziel = k.lernziel;
      insert into schule.wdh_staffel_sicherung (lernender_id, einheit_id, lernziel, faellig_am, wdh_ab, wdh_lerntage, richtig, falsch, wdh_ab_neu, gesichert_am, lauf, frueher)
      values (v_kind, k.einheit_id, k.lernziel, k.faellig_am, k.wdh_ab, k.wdh_lerntage, k.richtig, k.falsch,
              case when v_tag = 0 then null else now() end, now(), 'wd5', null)
      on conflict (lernender_id, einheit_id, lernziel) do update
        set frueher = to_jsonb(v_alt) - 'lernender_id' - 'einheit_id' - 'lernziel' - 'frueher',
            faellig_am = excluded.faellig_am, wdh_ab = excluded.wdh_ab, wdh_lerntage = excluded.wdh_lerntage, richtig = excluded.richtig, falsch = excluded.falsch,
            wdh_ab_neu = excluded.wdh_ab_neu, gesichert_am = excluded.gesichert_am, zurueck_am = null, lauf = 'wd5';
      if v_tag = 0 then   -- heute fällig
        update schule.karte_stand set faellig_am = now(), wdh_ab = null, wdh_lerntage = null
         where lernender_id = v_kind and einheit_id = k.einheit_id and lernziel = k.lernziel;
      else
        update schule.karte_stand set wdh_ab = now(), wdh_lerntage = v_tag, faellig_am = now() + v_tag * interval '1 day'
         where lernender_id = v_kind and einheit_id = k.einheit_id and lernziel = k.lernziel;
      end if;
      v_n := v_n + 1;
    end loop;
  end loop;
  return v_n;
end $function$;
revoke all on function schule.wdh_staffel_drosseln(bigint) from public, anon, authenticated;

-- 3. Rückweg WD-5: nur ohne Zwischenübung; stellt eine überschriebene WD-4b-Sicherung wieder her
create or replace function schule.wdh_drosseln_zurueck(p_l bigint default null)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_geuebt int; v_n int;
begin
  perform 1 from schule.karte_stand k join schule.wdh_staffel_sicherung s on s.lernender_id = k.lernender_id and s.einheit_id = k.einheit_id and s.lernziel = k.lernziel
   where s.lauf = 'wd5' and s.zurueck_am is null and (p_l is null or s.lernender_id = p_l) order by k.lernender_id, k.einheit_id, k.lernziel for update of k, s;
  select count(*) into v_geuebt from schule.wdh_staffel_sicherung s join schule.karte_stand k
      on k.lernender_id = s.lernender_id and k.einheit_id = s.einheit_id and k.lernziel = s.lernziel
   where s.lauf = 'wd5' and s.zurueck_am is null and (p_l is null or s.lernender_id = p_l)
     and (k.richtig is distinct from s.richtig or k.falsch is distinct from s.falsch or k.wdh_ab is distinct from s.wdh_ab_neu);
  if v_geuebt > 0 then
    raise exception 'WD-5 Rückweg abgelehnt: % verschobene Etappen wurden inzwischen geübt', v_geuebt using errcode = 'P0001';
  end if;
  update schule.karte_stand k set faellig_am = s.faellig_am, wdh_ab = s.wdh_ab, wdh_lerntage = s.wdh_lerntage
    from schule.wdh_staffel_sicherung s
   where s.lernender_id = k.lernender_id and s.einheit_id = k.einheit_id and s.lernziel = k.lernziel
     and s.lauf = 'wd5' and s.zurueck_am is null and (p_l is null or s.lernender_id = p_l);
  get diagnostics v_n = row_count;
  -- ältere Sicherung zurück an ihren Platz; ohne ältere: als zurückgenommen markieren
  update schule.wdh_staffel_sicherung s
     set faellig_am = (s.frueher->>'faellig_am')::timestamptz, wdh_ab = (s.frueher->>'wdh_ab')::timestamptz, wdh_lerntage = (s.frueher->>'wdh_lerntage')::smallint,
         richtig = (s.frueher->>'richtig')::int, falsch = (s.frueher->>'falsch')::int, wdh_ab_neu = (s.frueher->>'wdh_ab_neu')::timestamptz,
         gesichert_am = (s.frueher->>'gesichert_am')::timestamptz, zurueck_am = (s.frueher->>'zurueck_am')::timestamptz, lauf = s.frueher->>'lauf', frueher = null
   where s.lauf = 'wd5' and s.zurueck_am is null and s.frueher is not null and (p_l is null or s.lernender_id = p_l);
  update schule.wdh_staffel_sicherung set zurueck_am = now()
   where lauf = 'wd5' and zurueck_am is null and frueher is null and (p_l is null or lernender_id = p_l);
  return v_n;
end $function$;
revoke all on function schule.wdh_drosseln_zurueck(bigint) from public, anon, authenticated;

-- WD-4b-Rückweg nur für WD-4b-Sicherungen (lauf is null); sonst unverändert (Stand WD-S 4)
create or replace function schule.wdh_staffel_zurueck(p_l bigint default null)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_geuebt int; v_n int;
begin
  -- WD-S 4: betroffene Karten (und Sicherungen) in fester Reihenfolge sperren; unter der Sperre prüfen und schreiben
  perform 1 from schule.karte_stand k join schule.wdh_staffel_sicherung s on s.lernender_id = k.lernender_id and s.einheit_id = k.einheit_id and s.lernziel = k.lernziel
   where s.zurueck_am is null and s.lauf is null /* WD-5 */ and (p_l is null or s.lernender_id = p_l) order by k.lernender_id, k.einheit_id, k.lernziel for update of k, s;
  select count(*) into v_geuebt from schule.wdh_staffel_sicherung s join schule.karte_stand k
      on k.lernender_id = s.lernender_id and k.einheit_id = s.einheit_id and k.lernziel = s.lernziel
   where s.zurueck_am is null and s.lauf is null and (p_l is null or s.lernender_id = p_l)
     and (k.richtig is distinct from s.richtig or k.falsch is distinct from s.falsch or k.wdh_ab is distinct from s.wdh_ab_neu);
  if v_geuebt > 0 then
    raise exception 'WD-4b Rückweg abgelehnt: % gestreckte Etappen wurden inzwischen geübt', v_geuebt using errcode = 'P0001';
  end if;
  update schule.karte_stand k set faellig_am = s.faellig_am, wdh_ab = s.wdh_ab, wdh_lerntage = s.wdh_lerntage
    from schule.wdh_staffel_sicherung s
   where s.lernender_id = k.lernender_id and s.einheit_id = k.einheit_id and s.lernziel = k.lernziel and s.zurueck_am is null and s.lauf is null and (p_l is null or s.lernender_id = p_l);
  get diagnostics v_n = row_count;
  update schule.wdh_staffel_sicherung set zurueck_am = now() where zurueck_am is null and lauf is null and (p_l is null or lernender_id = p_l);
  return v_n;
end $function$;
revoke all on function schule.wdh_staffel_zurueck(bigint) from public, anon, authenticated;

-- Lauf: einmalig, mit Prüfsumme über alles außer den drei Fälligkeits-Feldern
do $mig$
declare v_vorher text; v_nachher text; r record; v_n int;
begin
  if exists (select 1 from schule.wdh_staffel_sicherung where lauf = 'wd5') then
    raise notice 'WD-5: schon gelaufen (WD-5-Sicherungen vorhanden) – kein zweiter Lauf'; return;
  end if;
  for r in select l.id, (select string_agg(coalesce(c.n, 0)::text, ' ' order by d) from generate_series(0, 13) d
                           left join (select g.tag, count(*) n from schule.wdh_gesetzt_erst(l.id) g group by 1) c on c.tag = d) v,
                  (select string_agg(coalesce(c.n, 0)::text, ' ' order by d) from generate_series(0, 13) d
                           left join (select schule.karte_wdh_in(k) tag, count(*) n from schule.karte_stand k where k.lernender_id = l.id and k.sitzt group by 1) c on c.tag = d) alle
             from schule.lernender l order by l.id loop
    raise notice 'WD-5 Kind %: gesetzte Erst-Wiederholungen je Lerntag 0–13 vorher: % · alle fälligen Etappen je Lerntag 0–13 vorher: %', r.id, r.v, r.alle;
  end loop;
  select md5(coalesce(string_agg((to_jsonb(k) - 'faellig_am' - 'wdh_ab' - 'wdh_lerntage')::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.lernziel_stand x), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.route x), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.sterne x), ''))
    into v_vorher from schule.karte_stand k;

  v_n := schule.wdh_staffel_drosseln(null);

  select md5(coalesce(string_agg((to_jsonb(k) - 'faellig_am' - 'wdh_ab' - 'wdh_lerntage')::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.lernziel_stand x), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.route x), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.sterne x), ''))
    into v_nachher from schule.karte_stand k;
  if v_nachher <> v_vorher then raise exception 'WD-5: außer der Fälligkeit hat sich etwas geändert – Abbruch'; end if;
  if exists (select 1 from schule.lernender l, lateral (select g.tag, count(*) n from schule.wdh_gesetzt_erst(l.id) g where not g.in_runde group by 1) c
              where c.n > greatest(schule.wd_regel('wdh_gesetzt_je_lerntag', 3), 1)) then
    raise exception 'WD-5: mehr als die erlaubten gesetzten Erst-Wiederholungen an einem Lerntag – Abbruch'; end if;

  for r in select l.id, (select string_agg(coalesce(c.n, 0)::text, ' ' order by d) from generate_series(0, 13) d
                           left join (select g.tag, count(*) n from schule.wdh_gesetzt_erst(l.id) g group by 1) c on c.tag = d) v,
                  (select string_agg(coalesce(c.n, 0)::text, ' ' order by d) from generate_series(0, 13) d
                           left join (select schule.karte_wdh_in(k) tag, count(*) n from schule.karte_stand k where k.lernender_id = l.id and k.sitzt group by 1) c on c.tag = d) alle
             from schule.lernender l order by l.id loop
    raise notice 'WD-5 Kind %: gesetzte Erst-Wiederholungen je Lerntag 0–13 nachher: % · alle fälligen Etappen je Lerntag 0–13 nachher: %', r.id, r.v, r.alle;
  end loop;
  raise notice 'WD-5: % Etappen verschoben; Landungen, Stufen, Belege, Lernstände, Plan, Sterne unverändert', v_n;
end $mig$;
