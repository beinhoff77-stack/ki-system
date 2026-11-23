-- ZP-S (Bau-Auftrag ZP, Entscheidung Sebastian 23.11. 02:35): eingeplanter Zusatz-Teil.
-- Ein Teil, der in der Gruppe des Kindes Zusatz ist (Gruppe in thema.zusatz), und den die Eltern eingeplant haben (Plan-Eintrag art 'normal',
-- nicht von claude/system, Thema nicht abgewählt), gilt als „Zusatz · eingeplant“:
--   – Fortschritt über alle Etappen (nicht über die leere Pflichtliste), kein Flug-Test, keine Nachtests (Regel wie „ohne Test“),
--   – erledigt, sobald alle Etappen selbst gelandet sind (sitzt, nicht gesetzt) → Ort „fertig“ (100 Sterne über route_sterne, genau einmal)
--     und Erstabschluss (Stempel, genau einmal),
--   – sperrt nichts dahinter (Visum und harte Voraussetzungen der Gruppe nennen Zusatz-Teile schon heute nicht; unverändert).
-- Nicht eingeplante Zusatz-Teile bleiben freiwillig und ohne Stempel. Wird der Teil durch einen Gruppenwechsel Pflicht, gilt die normale Regel:
-- der Ort geht wieder auf „offen“, der Flug-Test über die Pflicht-Etappen steht an; Stempel und Sterne bleiben, nichts doppelt.
-- Plan-Einträge bleiben art 'normal' (die App 0.90 führt den Plan über art 'normal'; 'zusatz' ist den Entdecker-Orten des Systems vorbehalten
-- und taucht weder im Plan noch auf der Abflugtafel auf). „Als Zusatz geführt“ = Kennzeichen zusatz_eingeplant in Stufe, Matrix, Plan, Reisekarte.
-- Eintrag route 485 (Kind 2): keine Datenänderung nötig, er fällt unter die Regel.
-- Baut auf LZ-S auf. Wiederholbar; kein DROP, kein DELETE.

do $$ begin
  if position('-- LZ-S' in pg_get_functiondef('schule.thema_stufe(bigint, bigint)'::regprocedure)) = 0 then
    raise exception 'ZP-S: zuerst 20261126_lz_s_ladezeit.sql einspielen'; end if;
end $$;

-- Zusatz in der Gruppe des Kindes und von den Eltern eingeplant (Plan-Eintrag art 'normal', nicht abgewählt; fertige Orte zählen weiter)
create or replace function schule.zusatz_eingeplant(p_l bigint, p_thema bigint)
 returns boolean language sql stable set search_path to ''
as $$
  select coalesce((select schule.kind_gruppe(p_l) = any(t.zusatz) from schule.thema t where t.id = p_thema), false)
     and exists (select 1 from schule.route r join schule.block_thema bt on bt.block_id = r.block_id and bt.thema_id = p_thema
                  where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt'
                    and (schule.ist_plan(r) or r.status = 'fertig')   -- eingeplant; bleibt es auch, wenn der Ort fertig ist
                    and not (p_thema = any(coalesce(r.ausgelassen, '{}'))));
$$;
revoke all on function schule.zusatz_eingeplant(bigint, bigint) from public, anon, authenticated;

-- alle Etappen der Einheit (Reihenfolge der Einheit)
create or replace function schule.etappen_alle(p_e bigint)
 returns text[] language sql stable set search_path to ''
as $$ select array(select x->>'lernziel' from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) x where e.id = p_e) $$;
revoke all on function schule.etappen_alle(bigint) from public, anon, authenticated;

-- alle Etappen selbst gelandet (sitzt, nicht von Eltern/Lehrer gesetzt)
create or replace function schule.zusatz_gelandet(p_l bigint, p_e bigint)
 returns boolean language sql stable set search_path to ''
as $$
  select cardinality(schule.etappen_alle(p_e)) > 0
     and not exists (select 1 from unnest(schule.etappen_alle(p_e)) x
                      where not exists (select 1 from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = p_e and k.lernziel = x
                                                                            and k.sitzt and k.gesetzt_am is null));
$$;
revoke all on function schule.zusatz_gelandet(bigint, bigint) from public, anon, authenticated;

-- ohne Test (wie „Kann er – aber wiederholen“): kein Flug-Test, kein Nachtest; „sicher“ über Wiederholung und Mischkarte
create or replace function schule.flug_ohne_test(p_l bigint, p_einheit bigint)
 returns boolean language sql stable set search_path to ''
as $$
  select coalesce(schule.thema_kann_wdh(p_l, (select e.thema_id from schule.einheit e where e.id = p_einheit)), false)
      or coalesce(schule.zusatz_eingeplant(p_l, (select e.thema_id from schule.einheit e where e.id = p_einheit)), false);   -- ZP-S
$$;

-- Nachtest-Stand: Grund „zusatz“ statt „gesetzt“ für eingeplanten Zusatz
do $$
declare d text;
  a text := $a$if schule.flug_ohne_test(p_lernender, p_einheit) then return jsonb_build_object('faellig', false, 'grund', 'gesetzt'); end if; -- LB-3$a$;
  n text := $a$if schule.flug_ohne_test(p_lernender, p_einheit) then return jsonb_build_object('faellig', false, 'grund',
    case when schule.zusatz_eingeplant(p_lernender, (select e.thema_id from schule.einheit e where e.id = p_einheit)) then 'zusatz' else 'gesetzt' end); end if; -- LB-3, ZP-S$a$;
begin
  d := pg_get_functiondef('schule.nachtest_stand(bigint, bigint)'::regprocedure);
  if position('ZP-S' in d) > 0 then raise notice 'nachtest_stand schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'ZP-S: Anker in nachtest_stand nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;

-- Ort-Stand: eingeplanter Zusatz ist erledigt, sobald alle Etappen selbst gelandet sind
do $$
declare d text;
  a text := $a$when th.einheit_id is null then 'keine_einheit'$a$;
  n text := $a$when th.einheit_id is null then 'keine_einheit'
      when schule.zusatz_eingeplant(p_lernender, th.thema_id) then case when schule.zusatz_gelandet(p_lernender, th.einheit_id) then 'erledigt' else 'offen' end /* ZP-S */$a$;
begin
  d := pg_get_functiondef('schule.ort_stand(bigint, bigint)'::regprocedure);
  if position('ZP-S' in d) > 0 then raise notice 'ort_stand schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'ZP-S: Anker in ort_stand nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;

-- Stufe: Etappen = alle Etappen, Kennzeichen zusatz / zusatz_eingeplant
do $$
declare d text;
  a1 text := $a$v_stufe text; v_et text[]; -- LZ-S$a$;
  n1 text := $a$v_stufe text; v_et text[]; -- LZ-S
  v_zp boolean := false; -- ZP-S$a$;
  a2 text := $a$v_et := schule.stufe_etappen(p_l, v_e); v_n := cardinality(v_et);$a$;
  n2 text := $a$v_zp := schule.zusatz_eingeplant(p_l, p_thema);   -- ZP-S: eingeplanter Zusatz zählt über alle Etappen
    v_et := case when v_zp then schule.etappen_alle(v_e) else schule.stufe_etappen(p_l, v_e) end; v_n := cardinality(v_et);$a$;
  a3 text := $a$'test_offen', v_test, 'ohne_test', v_ges = 'wiederholen');$a$;
  n3 text := $a$'test_offen', v_test, 'ohne_test', v_ges = 'wiederholen')
    || case when v_zp then jsonb_build_object('zusatz', true, 'zusatz_eingeplant', true) else '{}'::jsonb end; -- ZP-S$a$;
begin
  d := pg_get_functiondef('schule.thema_stufe(bigint, bigint)'::regprocedure);
  if position('ZP-S' in d) > 0 then raise notice 'thema_stufe schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a1, ''))) / length(a1) <> 1 or (length(d) - length(replace(d, a2, ''))) / length(a2) <> 1
     or (length(d) - length(replace(d, a3, ''))) / length(a3) <> 1 then raise exception 'ZP-S: Anker in thema_stufe nicht genau einmal gefunden'; end if;
  execute replace(replace(replace(d, a1, n1), a2, n2), a3, n3);
end $$;

-- Reisekarte: zusatz_eingeplant je Flug, zaehlt je Stadt (alle Etappen zählen), darf nächster Start sein
do $$
declare d text;
  a1 text := $a$v_rang int; v_best int := 2147483647; v_offen jsonb;$a$;
  n1 text := $a$v_rang int; v_best int := 2147483647; v_offen jsonb; v_zp boolean; -- ZP-S$a$;
  a2 text := $a$v_stufe := schule.thema_stufe(p_l, v_f.thema_id);$a$;
  n2 text := $a$v_stufe := schule.thema_stufe(p_l, v_f.thema_id); v_zp := coalesce((v_stufe->>'zusatz_eingeplant')::boolean, false); -- ZP-S$a$;
  a3 text := $a$'lernziel', v_s.lernziel, 'titel', v_s.titel, 'pflicht', v_pfl, 'stand', v_stand);$a$;
  n3 text := $a$'lernziel', v_s.lernziel, 'titel', v_s.titel, 'pflicht', v_pfl, 'stand', v_stand)
                                    || case when v_zp then jsonb_build_object('zaehlt', true) else '{}'::jsonb end); -- ZP-S$a$;
  a6 text := $a$v_st := v_st || jsonb_build_object('nr', v_s.nr,$a$;
  n6 text := $a$v_st := v_st || (jsonb_build_object('nr', v_s.nr,$a$;
  a4 text := $a$if v_rang is not null and not v_f.zus then$a$;
  n4 text := $a$if v_rang is not null and (not v_f.zus or v_zp) then -- ZP-S$a$;
  a5 text := $a$'plan_platz', v_platz, 'zusatz', v_f.zus,$a$;
  n5 text := $a$'plan_platz', v_platz, 'zusatz', v_f.zus, 'zusatz_eingeplant', v_zp, -- ZP-S
       $a$;
begin
  d := pg_get_functiondef('schule.reise_karte(bigint)'::regprocedure);
  if position('ZP-S' in d) > 0 then raise notice 'reise_karte schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a1, ''))) / length(a1) <> 1 or (length(d) - length(replace(d, a2, ''))) / length(a2) <> 1
     or (length(d) - length(replace(d, a3, ''))) / length(a3) <> 1 or (length(d) - length(replace(d, a4, ''))) / length(a4) <> 1
     or (length(d) - length(replace(d, a5, ''))) / length(a5) <> 1 or (length(d) - length(replace(d, a6, ''))) / length(a6) <> 1 then
    raise exception 'ZP-S: Anker in reise_karte nicht genau einmal gefunden'; end if;
  execute replace(replace(replace(replace(replace(replace(d, a1, n1), a2, n2), a3, n3), a4, n4), a5, n5), a6, n6);
end $$;

-- Abschluss: Orte des Kindes, deren eingeplanter Zusatz jetzt erledigt ist, werden „fertig“ (route_sterne bucht 100 Sterne einmal);
-- umgekehrt geht ein „fertiger“ Ort wieder auf, wenn ein Zusatz-Teil durch Gruppenwechsel Pflicht wird und noch nicht bestanden ist.
create or replace function schule.zusatz_plan_abgleich(p_l bigint, p_thema bigint default null, p_wieder_auf bigint[] default '{}')
 returns integer language plpgsql security definer set search_path to ''
as $$
declare v_n int := 0; v_m int := 0;
begin
  -- geaendert_von bleibt (Eintrag der Eltern bleibt Plan-Eintrag)
  update schule.route r set status = 'fertig', geaendert_am = now(), revision = r.revision + 1
   where r.lernender_id = p_l and schule.ist_plan(r) and r.status not in ('fertig', 'entfernt')
     and exists (select 1 from schule.block_thema bt where bt.block_id = r.block_id and (p_thema is null or bt.thema_id = p_thema)
                  and schule.zusatz_eingeplant(p_l, bt.thema_id))
     and coalesce((schule.ort_stand(p_l, r.block_id)->>'abgeschlossen')::boolean, false);
  get diagnostics v_n = row_count;
  if cardinality(p_wieder_auf) > 0 then
    update schule.route r set status = 'offen', geaendert_am = now(), revision = r.revision + 1
     where r.lernender_id = p_l and r.art = 'normal' and r.status = 'fertig' and r.block_id = any(p_wieder_auf)
       and not coalesce((schule.ort_stand(p_l, r.block_id)->>'abgeschlossen')::boolean, false);
    get diagnostics v_m = row_count;
  end if;
  return v_n + v_m;
end $$;
revoke all on function schule.zusatz_plan_abgleich(bigint, bigint, bigint[]) from public, anon, authenticated;

-- Auslöser 1: Landung einer Etappe eines eingeplanten Zusatz-Teils
create or replace function schule.zusatz_landung_ausloesen()
 returns trigger language plpgsql security definer set search_path to ''
as $$
declare v_t bigint;
begin
  if new.sitzt and (tg_op = 'INSERT' or old.sitzt is distinct from true or old.gesetzt_am is distinct from new.gesetzt_am) then
    select e.thema_id into v_t from schule.einheit e where e.id = new.einheit_id;
    if schule.zusatz_eingeplant(new.lernender_id, v_t) then perform schule.zusatz_plan_abgleich(new.lernender_id, v_t); end if;
  end if;
  return null;
end $$;
revoke all on function schule.zusatz_landung_ausloesen() from public, anon, authenticated;

-- Auslöser 2: Ort wird „fertig“ → Erstabschluss (Stempel) für jeden eingeplanten, selbst gelandeten Zusatz-Teil des Orts, genau einmal
create or replace function schule.zusatz_stempel_ausloesen()
 returns trigger language plpgsql security definer set search_path to ''
as $$
begin
  if new.status = 'fertig' and old.status is distinct from 'fertig' and new.art = 'normal' then
    insert into schule.flug_erstabschluss (lernender_id, einheit_id, sitzung_id, am)
    select new.lernender_id, schule.thema_einheit(bt.thema_id), null, now()
      from schule.block_thema bt
     where bt.block_id = new.block_id and schule.thema_einheit(bt.thema_id) is not null
       and schule.zusatz_eingeplant(new.lernender_id, bt.thema_id) and schule.zusatz_gelandet(new.lernender_id, schule.thema_einheit(bt.thema_id))
    on conflict (lernender_id, einheit_id) do nothing;
  end if;
  return null;
end $$;
revoke all on function schule.zusatz_stempel_ausloesen() from public, anon, authenticated;

-- Auslöser 3: Gruppenwechsel – Zusatz wird Pflicht (Ort wieder offen, Test steht an) bzw. Pflicht wird Zusatz (ggf. jetzt erledigt)
create or replace function schule.zusatz_gruppe_ausloesen()
 returns trigger language plpgsql security definer set search_path to ''
as $$
declare v_alt text; v_neu text; v_auf bigint[];
begin
  if new.schulart is distinct from old.schulart or new.zweig is distinct from old.zweig then
    v_alt := case coalesce(old.schulart, 'gym_by') when 'gym_by' then 'gym_by' else schule.kind_zweig(old.schulart, old.zweig) end;
    v_neu := schule.kind_gruppe(new.id);
    select coalesce(array_agg(distinct bt.block_id), '{}') into v_auf from schule.block_thema bt join schule.thema t on t.id = bt.thema_id
     where v_alt = any(t.zusatz) and not (v_neu = any(t.zusatz));
    perform schule.zusatz_plan_abgleich(new.id, null, v_auf);
  end if;
  return null;
end $$;
revoke all on function schule.zusatz_gruppe_ausloesen() from public, anon, authenticated;

do $$ begin
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.karte_stand'::regclass and tgname = 'karte_zusatz_abschluss') then
    create trigger karte_zusatz_abschluss after insert or update of sitzt, gesetzt_am on schule.karte_stand
      for each row execute function schule.zusatz_landung_ausloesen();
  end if;
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.route'::regclass and tgname = 'route_zusatz_stempel') then
    create trigger route_zusatz_stempel after update of status on schule.route
      for each row execute function schule.zusatz_stempel_ausloesen();
  end if;
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.lernender'::regclass and tgname = 'lernender_zusatz_abgleich') then
    -- Name nach lernender_pflicht_abgleich (Auslöser laufen alphabetisch): die Pflicht-Zeilen sind dann schon abgeglichen
    create trigger lernender_zusatz_abgleich after update of schulart, zweig on schule.lernender
      for each row execute function schule.zusatz_gruppe_ausloesen();
  end if;
end $$;

-- bestehende Stände: eingeplante Zusatz-Teile, die schon vollständig selbst gelandet sind, jetzt abschließen (heute keiner)
do $$ declare v_n int; begin
  select coalesce(sum(schule.zusatz_plan_abgleich(l.id)), 0) into v_n from schule.lernender l where l.aktiv;
  raise notice 'ZP-S: % Orte mit eingeplantem Zusatz-Teil abgeschlossen', v_n;
end $$;
