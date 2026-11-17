-- W150 Eltern E-2 (Bau-Auftrag Phase 2, Schritt C): Flüge im Ort abwählbar; dazu zwei Befunde der Nachprüfung E-1.
--  1. Je Plan-Eintrag (schule.route, art 'normal') eine Liste ausgelassener Flüge (thema_id). Ein ausgelassener Flug zählt für das Kind
--     weder im Plan noch beim Stempel (schule.ort_stand). Für den Stand je Schulart (konto.jahrgang) zählt er weiter mit.
--  2. Befund 2: „Entfernen“ merkt sich den alten Status (status_vor_entfernen); kommt der Ort zurück (z. B. per „Rückgängig“), bleibt „geschafft“ erhalten.
--     Dazu liefert schule_plan_lesen auch geschaffte Orte, die das System auf „fertig“ gesetzt hat (vorher fehlten sie im Plan der App
--     und wurden beim nächsten Speichern als „nicht genannt“ entfernt).
--  3. Befund 3: Entfernte Einträge wandern nicht mehr bei jedem Speichern um 200 000 weiter, sondern stehen fortlaufend ab 1 000 001.
--  4. schule_uebersicht liefert je Einheit thema_id und reihenfolge (Lehrplan-Reihenfolge im Ort aus schule.block_thema) und je Route-Eintrag ausgelassen.
-- Nur create or replace, gezieltes Ersetzen (wie 20261116_w150_r3_*) und Spalten ergänzen; kein DROP, kein DELETE.

alter table schule.route add column if not exists ausgelassen bigint[] not null default '{}';
alter table schule.route add column if not exists status_vor_entfernen text;
comment on column schule.route.ausgelassen is 'E-2: Flüge (schule.thema.id) dieses Ortes, die Eltern/Lehrer für das Kind abgewählt haben';
comment on column schule.route.status_vor_entfernen is 'Status vor „Entfernen“ – wird beim Zurückholen wiederhergestellt (z. B. fertig)';

-- Einmalig: entfernte Einträge kompakt nummerieren (route_pos ist DEFERRABLE INITIALLY DEFERRED, Zwischenstände dürfen kollidieren).
update schule.route r set position = 1000000 + x.nr
  from (select id, row_number() over (partition by lernender_id order by position, id) as nr
          from schule.route where art = 'normal' and status = 'entfernt') x
 where r.id = x.id and r.position <> 1000000 + x.nr;

-- Stempel: zählt nur die geplanten Flüge des Ortes (ausgelassene nicht).
create or replace function schule.ort_stand(p_lernender bigint, p_block bigint)
 returns jsonb
 language sql
 stable
 set search_path to ''
as $function$
  with aus as (
    select coalesce((select r.ausgelassen from schule.route r where r.lernender_id = p_lernender and r.block_id = p_block and r.art = 'normal' and r.status <> 'entfernt'
                     order by r.id limit 1), '{}'::bigint[]) as liste
  ), th as (
    select bt.thema_id, t.schluessel,
      (select e.id from schule.einheit e where e.thema_id = bt.thema_id and e.status in ('geprueft','freigegeben') order by e.version desc limit 1) as einheit_id
    from schule.block_thema bt join schule.thema t on t.id = bt.thema_id, aus
    where bt.block_id = p_block and not (bt.thema_id = any(aus.liste))
  ), st as (
    select th.*, case when th.einheit_id is null then 'keine_einheit'
      when not exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = th.einheit_id) then 'offen'
      when exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = th.einheit_id and s.pflicht and s.status not in ('nachgewiesen','korrigiert','gesichert')) then 'offen'
      else 'erledigt' end as zustand
    from th
  )
  select jsonb_build_object('block_id', p_block, 'abgeschlossen', coalesce(bool_and(zustand = 'erledigt'), false) and count(*) > 0,
    'themen', coalesce(jsonb_agg(jsonb_build_object('thema', schluessel, 'einheit_id', einheit_id, 'zustand', zustand)), '[]'))
  from st;
$function$;

-- Plan setzen: wie bisher (Reihenfolge = Reihenfolge im Array, revision schützt vor Überschreiben); neu: ausgelassen je Eintrag,
-- alter Status beim Entfernen gemerkt und beim Zurückholen wiederhergestellt, entfernte Positionen wachsen nicht mehr.
create or replace function api.schule_plan_setzen(p_schluessel text, p_daten jsonb)
 returns jsonb
 language plpgsql
 security definer
 set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id','')::bigint; v_rev int; v_akt text; v_e jsonb; v_pos int := 0;
  v_b bigint; v_r schule.route; v_ids bigint[] := '{}'; v_n int; v_aus bigint[];
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  if not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  if jsonb_typeof(p_daten->'eintraege') is distinct from 'array' then raise exception 'eintraege fehlt' using errcode = 'P0001'; end if;
  perform 1 from schule.lernender where id = v_l for update;
  select coalesce(max(revision), 0) into v_rev from schule.route where lernender_id = v_l and art = 'normal';
  if p_daten ? 'revision' and (p_daten->>'revision')::int <> v_rev then
    raise exception 'Der Plan wurde inzwischen geändert. Bitte neu laden.' using errcode = 'P0001';
  end if;
  v_akt := coalesce((select i.rolle || ':' || i.name from schule.lern_ich(p_schluessel) i where schule.ist_lern(p_schluessel)), 'eltern:App');
  -- Positionen: route_pos (lernender_id, position) ist DEFERRABLE INITIALLY DEFERRED – Zwischenstände dürfen kollidieren, am Ende ist alles eindeutig.
  for v_e in select * from jsonb_array_elements(p_daten->'eintraege') loop
    v_b := (v_e->>'block_id')::bigint;
    if not exists (select 1 from schule.block where id = v_b and fach = 'Mathematik') then raise exception 'Unbekannter Ort %', v_b using errcode = 'P0001'; end if;
    if v_b = any(v_ids) then raise exception 'Ort doppelt im Plan' using errcode = 'P0001'; end if;
    v_ids := v_ids || v_b; v_pos := v_pos + 1;
    v_aus := null; -- fehlt „ausgelassen“, bleibt die bisherige Liste
    if v_e ? 'ausgelassen' then
      if jsonb_typeof(v_e->'ausgelassen') is distinct from 'array' then raise exception 'ausgelassen muss eine Liste sein' using errcode = 'P0001'; end if;
      select coalesce(array_agg(distinct x::bigint), '{}') into v_aus from jsonb_array_elements_text(v_e->'ausgelassen') x;
      if exists (select 1 from unnest(v_aus) a where not exists (select 1 from schule.block_thema bt where bt.block_id = v_b and bt.thema_id = a)) then
        raise exception 'Ein abgewählter Flug gehört nicht zu diesem Ort' using errcode = 'P0001';
      end if;
    end if;
    select * into v_r from schule.route where lernender_id = v_l and block_id = v_b and art = 'normal' order by id limit 1;
    if v_r.id is null then
      insert into schule.route(lernender_id, block_id, position, art, status, kann_schon, ausgelassen, revision, geaendert_von, geaendert_am)
      values (v_l, v_b, v_pos, 'normal', 'offen', coalesce((v_e->>'kann_schon')::boolean, false), coalesce(v_aus, '{}'), v_rev + 1, v_akt, now());
    else
      update schule.route set position = v_pos,
        status = case when status = 'entfernt' then coalesce(status_vor_entfernen, 'offen') else status end,
        status_vor_entfernen = null,
        kann_schon = coalesce((v_e->>'kann_schon')::boolean, kann_schon),
        ausgelassen = coalesce(v_aus, ausgelassen),
        revision = v_rev + 1, geaendert_von = v_akt, geaendert_am = now()
       where id = v_r.id;
    end if;
  end loop;
  -- nicht mehr genannte Orte: aus dem Plan nehmen und den alten Status merken
  update schule.route set status_vor_entfernen = status, status = 'entfernt', revision = v_rev + 1, geaendert_von = v_akt, geaendert_am = now()
   where lernender_id = v_l and art = 'normal' and status <> 'entfernt' and not (block_id = any(v_ids));
  get diagnostics v_n = row_count;
  -- entfernte Einträge fortlaufend hinter dem Plan (ab 1 000 001) – die Zahl wächst nicht mit jedem Speichern
  update schule.route r set position = 1000000 + x.nr
    from (select id, row_number() over (order by position, id) as nr from schule.route
           where lernender_id = v_l and art = 'normal' and status = 'entfernt') x
   where r.id = x.id and r.position <> 1000000 + x.nr;
  insert into schule.route_aenderung(lernender_id, route_id, akteur, anlass, ereignis)
  values (v_l, null, v_akt, 'plan', jsonb_build_object('reihenfolge', to_jsonb(v_ids), 'entfernt', v_n, 'revision', v_rev + 1));
  return jsonb_build_object('ok', true, 'revision', v_rev + 1, 'anzahl', cardinality(v_ids));
end $function$;

-- Plan lesen: geschaffte Orte gehören zum Plan, auch wenn das System sie auf „fertig“ gesetzt hat; je Eintrag die ausgelassenen Flüge.
create or replace function api.schule_plan_lesen(p_schluessel text, p_daten jsonb)
 returns jsonb
 language plpgsql
 stable security definer
 set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id','')::bigint; v_k schule.lernender;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  select * into v_k from schule.lernender where id = v_l and aktiv;
  if v_k.id is null then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true, 'kann_abwaehlen', true, -- die App zeigt die Häkchen „im Plan“ erst, wenn die Datenbank „ausgelassen“ speichert
    'kind', jsonb_build_object('id', v_k.id, 'name', v_k.anzeigename, 'klasse', v_k.klasse, 'schulart', v_k.schulart, 'ist_test', v_k.ist_test),
    'revision', (select coalesce(max(r.revision), 0) from schule.route r where r.lernender_id = v_l and r.art = 'normal'),
    'plan', (select coalesce(jsonb_agg(jsonb_build_object('block_id', r.block_id, 'position', r.position, 'art', r.art, 'status', r.status,
                 'kann_schon', r.kann_schon, 'ausgelassen', to_jsonb(r.ausgelassen), 'geaendert_von', r.geaendert_von, 'geaendert_am', r.geaendert_am)
                 order by r.art = 'normal', r.position), '[]'::jsonb)
             from schule.route r where r.lernender_id = v_l
               and (schule.ist_plan(r) or (r.art = 'normal' and r.status = 'fertig') or (r.art = 'rueckreise' and r.status not in ('fertig','entfernt')))),
    'kann_schon', (select coalesce(jsonb_agg(r.block_id), '[]'::jsonb) from schule.route r where r.lernender_id = v_l and r.kann_schon and r.status <> 'entfernt'),
    'orte', (select coalesce(jsonb_agg(jsonb_build_object('block_id', b.id, 'titel', b.titel, 'stadt', b.stadt, 'kontinent', k.titel, 'kontinent_id', k.id,
                 'reihenfolge', b.reihenfolge,
                 'themen', (select coalesce(jsonb_agg(jsonb_build_object('thema_id', t.id, 'titel', t.unterthema, 'jahrgang', schule.thema_jahrgang(t.id),
                                 'stand', schule.thema_stand(v_l, t.id),
                                 'einheit', (select jsonb_build_object('id', e.id, 'status', e.status,
                                                'karten', jsonb_array_length(coalesce(e.inhalt->'etappen','[]'::jsonb)),
                                                'aufgaben', (select count(*) from schule.aufgabe a where a.einheit_id = e.id),
                                                'neu', (select count(*) from schule.aufgabe a where a.einheit_id = e.id and not a.freigegeben))
                                             from schule.einheit e where e.thema_id = t.id order by (e.status in ('geprueft','freigegeben')) desc, e.version desc limit 1))
                               order by bt.reihenfolge, t.reihenfolge), '[]'::jsonb)
                            from schule.block_thema bt join schule.thema t on t.id = bt.thema_id where bt.block_id = b.id))
               order by k.reihenfolge, b.reihenfolge), '[]'::jsonb)
             from schule.block b left join schule.kontinent k on k.id = b.kontinent_id where b.fach = 'Mathematik'),
    'notizen', (select coalesce(jsonb_agg(jsonb_build_object('id', n.id, 'text', n.text, 'von', n.von, 'am', n.am) order by n.am desc), '[]'::jsonb)
                from (select * from schule.notiz where lernender_id = v_l order by am desc limit 30) n),
    'verlauf', (select coalesce(jsonb_agg(jsonb_build_object('akteur', a.akteur, 'anlass', a.anlass, 'ereignis', a.ereignis, 'am', a.am) order by a.am desc), '[]'::jsonb)
                from (select * from schule.route_aenderung where lernender_id = v_l order by am desc limit 20) a));
end $function$;

-- Übersicht: je Einheit thema_id und Lehrplan-Reihenfolge im Ort, je Route-Eintrag die ausgelassenen Flüge (gezieltes Ersetzen in der bestehenden Definition).
do $$
declare d text;
begin
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  if position('''jahrgang'', schule.thema_jahrgang(e.thema_id),' in d) = 0 then raise exception 'Stelle jahrgang in schule_uebersicht nicht gefunden'; end if;
  if position('''kann_schon'', r.kann_schon, ''art'', r.art)' in d) = 0 then raise exception 'Stelle route in schule_uebersicht nicht gefunden'; end if;
  d := replace(d, '''jahrgang'', schule.thema_jahrgang(e.thema_id),',
    '''jahrgang'', schule.thema_jahrgang(e.thema_id), ''thema_id'', e.thema_id, ''reihenfolge'', (select bt.reihenfolge from schule.block_thema bt where bt.block_id = e.block_id and bt.thema_id = e.thema_id),');
  d := replace(d, '''kann_schon'', r.kann_schon, ''art'', r.art)', '''kann_schon'', r.kann_schon, ''art'', r.art, ''ausgelassen'', to_jsonb(r.ausgelassen))');
  execute d;
end $$;
