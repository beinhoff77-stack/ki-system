-- Bau-Auftrag LA-4/LA-5 (Lehrer-Aufbau, Plan): „kann schon“ je Flug und Angaben für den Block „Geschafft“.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE. Pläne und Lernstände bleiben erhalten.
--
-- Neu: route.kann_schon_themen bigint[] (wie ausgelassen) – Flüge eines Ortes, die das Kind schon kann.
--   Zählt wie gelandet in thema_stand (Lehrplan-Übersicht, Stand), ort_stand (Ort-Abschluss), Plan und Abflugtafel – als eigener Zustand „kann schon“,
--   NICHT als karte_stand.sitzt: daraus entstehen keine Mischkarten, Wiederholungen oder Expeditions-Angebote. Rückgängig ohne Verlust (Häkchen weg = Eintrag weg;
--   ein dadurch nicht mehr erledigter Ort wird wie bei „ausgelassen“ wieder offen).
--   Das bisherige „kann schon“ für den ganzen Ort (route.kann_schon) bleibt und setzt alle Flüge.
-- schule_plan_setzen: eintraege[].kann_schon_themen (fehlt es, bleibt die Liste). schule_plan_lesen/schule_uebersicht: route/plan[].kann_schon_themen; plan_lesen themen[].kann_schon.
-- LA-5: schule_lernstand je Etappe wdh_in (Lerntage bis zur nächsten Wiederholung; 0 = fällig; null = nicht gelandet).

alter table schule.route add column if not exists kann_schon_themen bigint[] not null default '{}';
comment on column schule.route.kann_schon_themen is 'LA-4: Flüge (thema_id) dieses Ortes, die das Kind schon kann – zählt wie gelandet, ohne karte_stand';

-- Flug „kann schon“ beim Kind: im Plan einzeln abgehakt oder der ganze Ort „kann schon“ (nicht abgewählt)
create or replace function schule.thema_kann_schon(p_l bigint, p_thema bigint)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.route r join schule.block_thema bt on bt.block_id = r.block_id and bt.thema_id = p_thema
                  where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt' and not (p_thema = any(r.ausgelassen))
                    and (p_thema = any(r.kann_schon_themen) or r.kann_schon));
$function$;

-- thema_stand: „kann schon“ je Flug zählt als erledigt (sonst unverändert)
create or replace function schule.thema_stand(p_l bigint, p_thema bigint)
 returns text
 language sql
 stable
 set search_path to ''
as $function$
  with e as (select id from schule.einheit where thema_id = p_thema and status in ('geprueft','freigegeben') order by version desc limit 1)
  select case when exists (select 1 from schule.route r where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt' and p_thema = any(r.kann_schon_themen)) then 'erledigt' -- LA-4
    when not exists (select 1 from e) then 'keine_einheit'
    when exists (select 1 from schule.lernziel_stand s join e on e.id = s.einheit_id where s.lernender_id = p_l)
      and not exists (select 1 from schule.lernziel_stand s join e on e.id = s.einheit_id where s.lernender_id = p_l and s.pflicht and s.status not in ('nachgewiesen','korrigiert','gesichert'))
      then 'erledigt'
    when exists (select 1 from schule.karte_stand k join e on e.id = k.einheit_id where k.lernender_id = p_l)
      or exists (select 1 from schule.lernziel_stand s join e on e.id = s.einheit_id where s.lernender_id = p_l and s.status <> 'offen') then 'laeuft'
    else 'offen' end;
$function$;

-- ort_stand: Flüge mit „kann schon“ zählen für den Ort-Abschluss als erledigt (sonst unverändert)
create or replace function schule.ort_stand(p_lernender bigint, p_block bigint)
 returns jsonb
 language sql
 stable
 set search_path to ''
as $function$
  with aus as (
    select coalesce((select r.ausgelassen from schule.route r where r.lernender_id = p_lernender and r.block_id = p_block and r.art = 'normal' and r.status <> 'entfernt'
                     order by r.id limit 1), '{}'::bigint[]) as liste,
           coalesce((select r.kann_schon_themen from schule.route r where r.lernender_id = p_lernender and r.block_id = p_block and r.art = 'normal' and r.status <> 'entfernt'
                     order by r.id limit 1), '{}'::bigint[]) as kann
  ), th as (
    select bt.thema_id, t.schluessel, aus.kann,
      (select e.id from schule.einheit e where e.thema_id = bt.thema_id and e.status in ('geprueft','freigegeben') order by e.version desc limit 1) as einheit_id
    from schule.block_thema bt join schule.thema t on t.id = bt.thema_id, aus
    where bt.block_id = p_block and not (bt.thema_id = any(aus.liste))
  ), st as (
    select th.*, case when th.thema_id = any(th.kann) then 'erledigt' -- LA-4
      when th.einheit_id is null then 'keine_einheit'
      when not exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = th.einheit_id) then 'offen'
      when exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = th.einheit_id and s.pflicht and s.status not in ('nachgewiesen','korrigiert','gesichert')) then 'offen'
      else 'erledigt' end as zustand
    from th
  )
  select jsonb_build_object('block_id', p_block, 'abgeschlossen', coalesce(bool_and(zustand = 'erledigt'), false) and count(*) > 0,
    'themen', coalesce(jsonb_agg(jsonb_build_object('thema', schluessel, 'einheit_id', einheit_id, 'zustand', zustand)), '[]'))
  from st;
$function$;

-- LA-5: Lerntage bis zur nächsten Wiederholung (gleiche Zählung wie karte_faellig)
create or replace function schule.karte_wdh_in(k schule.karte_stand)
 returns integer language sql stable set search_path to ''
as $function$
  select case when not coalesce(k.sitzt, false) then null
    when schule.karte_faellig(k) then 0
    when k.wdh_lerntage is null or k.wdh_ab is null then null
    else greatest(1, k.wdh_lerntage - (select (select count(*) from schule.lerntag t where t.lernender_id = k.lernender_id and t.fach = 'Mathematik'
                    and (t.datum::timestamp at time zone t.zeitzone) > k.wdh_ab and t.datum < (now() at time zone z.tz)::date)
                 + case when (now() at time zone z.tz)::date > (k.wdh_ab at time zone z.tz)::date then 1 else 0 end
            from (select coalesce((select l.zeitzone from schule.lernender l where l.id = k.lernender_id), 'UTC') as tz) z)::int) end;
$function$;

do $$
declare d text;
begin
  -- schule_plan_setzen: kann_schon_themen je Eintrag
  d := pg_get_functiondef('api.schule_plan_setzen(text, jsonb)'::regprocedure);
  if position('v_aus bigint[];' in d) = 0
     or position('v_aus := null; -- fehlt „ausgelassen“, bleibt die bisherige Liste' in d) = 0
     or position('insert into schule.route(lernender_id, block_id, position, art, status, kann_schon, ausgelassen, revision, geaendert_von, geaendert_am)' in d) = 0
     or position('coalesce((v_e->>''kann_schon'')::boolean, false), coalesce(v_aus, ''{}''), v_rev + 1, v_akt, now());' in d) = 0
     or position('ausgelassen = coalesce(v_aus, ausgelassen),' in d) = 0
     or position('      if v_r.status = ''fertig'' and v_aus is not null and exists (select 1 from unnest(v_r.ausgelassen) a where not (a = any(v_aus))) then' in d) = 0 then
    raise exception 'Stellen in schule_plan_setzen nicht gefunden'; end if;
  d := replace(d, 'v_aus bigint[];', 'v_aus bigint[]; v_ks bigint[];');
  d := replace(d, 'v_aus := null; -- fehlt „ausgelassen“, bleibt die bisherige Liste', $r$v_aus := null; -- fehlt „ausgelassen“, bleibt die bisherige Liste
    v_ks := null; -- LA-4: fehlt „kann_schon_themen“, bleibt die bisherige Liste
    if v_e ? 'kann_schon_themen' then
      if jsonb_typeof(v_e->'kann_schon_themen') is distinct from 'array' then raise exception 'kann_schon_themen muss eine Liste sein' using errcode = 'P0001'; end if;
      select coalesce(array_agg(distinct x::bigint), '{}') into v_ks from jsonb_array_elements_text(v_e->'kann_schon_themen') x;
      if exists (select 1 from unnest(v_ks) a where not exists (select 1 from schule.block_thema bt where bt.block_id = v_b and bt.thema_id = a)) then
        raise exception 'Ein Flug mit „kann schon“ gehört nicht zu diesem Ort' using errcode = 'P0001';
      end if;
    end if;$r$);
  d := replace(d, 'insert into schule.route(lernender_id, block_id, position, art, status, kann_schon, ausgelassen, revision, geaendert_von, geaendert_am)',
                  'insert into schule.route(lernender_id, block_id, position, art, status, kann_schon, ausgelassen, kann_schon_themen, revision, geaendert_von, geaendert_am)');
  d := replace(d, 'coalesce((v_e->>''kann_schon'')::boolean, false), coalesce(v_aus, ''{}''), v_rev + 1, v_akt, now());',
                  'coalesce((v_e->>''kann_schon'')::boolean, false), coalesce(v_aus, ''{}''), coalesce(v_ks, ''{}''), v_rev + 1, v_akt, now());');
  d := replace(d, 'ausgelassen = coalesce(v_aus, ausgelassen),', 'ausgelassen = coalesce(v_aus, ausgelassen), kann_schon_themen = coalesce(v_ks, kann_schon_themen),');
  d := replace(d, '      if v_r.status = ''fertig'' and v_aus is not null and exists (select 1 from unnest(v_r.ausgelassen) a where not (a = any(v_aus))) then',
    $r$      if v_r.status = 'fertig' and v_ks is not null and exists (select 1 from unnest(v_r.kann_schon_themen) a where not (a = any(v_ks))) then
        v_wieder := v_wieder || v_b; -- LA-4: „kann schon“ zurückgenommen → Ort wird geprüft
      end if;
      if v_r.status = 'fertig' and v_aus is not null and exists (select 1 from unnest(v_r.ausgelassen) a where not (a = any(v_aus))) then$r$);
  execute d;

  -- schule_plan_lesen: plan[].kann_schon_themen, themen[].kann_schon
  d := pg_get_functiondef('api.schule_plan_lesen(text, jsonb)'::regprocedure);
  if position('''kann_schon'', r.kann_schon, ''ausgelassen'', to_jsonb(r.ausgelassen), ''geaendert_von''' in d) = 0
     or position('''stand'', schule.thema_stand(v_l, t.id),' in d) = 0 then raise exception 'Stellen in schule_plan_lesen nicht gefunden'; end if;
  d := replace(d, '''kann_schon'', r.kann_schon, ''ausgelassen'', to_jsonb(r.ausgelassen), ''geaendert_von''',
                  '''kann_schon'', r.kann_schon, ''ausgelassen'', to_jsonb(r.ausgelassen), ''kann_schon_themen'', to_jsonb(r.kann_schon_themen), ''geaendert_von''');
  d := replace(d, '''stand'', schule.thema_stand(v_l, t.id),', '''stand'', schule.thema_stand(v_l, t.id), ''kann_schon'', schule.thema_kann_schon(v_l, t.id),');
  execute d;

  -- schule_uebersicht: route[].kann_schon_themen
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  if position('''art'', r.art, ''ausgelassen'', to_jsonb(r.ausgelassen))' in d) = 0 then raise exception 'Stelle in schule_uebersicht nicht gefunden'; end if;
  d := replace(d, '''art'', r.art, ''ausgelassen'', to_jsonb(r.ausgelassen))', '''art'', r.art, ''ausgelassen'', to_jsonb(r.ausgelassen), ''kann_schon_themen'', to_jsonb(r.kann_schon_themen))');
  execute d;

  -- schule_lernstand: wdh_in je Etappe (LA-5)
  d := pg_get_functiondef('api.schule_lernstand(text, jsonb)'::regprocedure);
  if position('''faellig'', coalesce(schule.karte_faellig(k), false),' in d) = 0 then raise exception 'Stelle in schule_lernstand nicht gefunden'; end if;
  d := replace(d, '''faellig'', coalesce(schule.karte_faellig(k), false),', '''faellig'', coalesce(schule.karte_faellig(k), false), ''wdh_in'', schule.karte_wdh_in(k),');
  execute d;
end $$;
