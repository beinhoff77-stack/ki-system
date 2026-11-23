-- EX-S (Auftrag EX, 23.11.): Expeditionen dem Kind vor die Nase legen – Serverteil.
-- 1) Sterne: 150 je geschaffter Expedition (Regelwert sterne_expedition_geschafft, bisher 50), 200 bei fehlerfreiem Lösen
--    (neuer Regelwert sterne_expedition_fehlerfrei; fehlerfrei = jeder Teil im ersten Versuch richtig, ohne Tipp). Genau einmal je Kind und Expedition.
-- 2) Je Kind und Expedition: seit wann angeboten (Landung, die die letzte Voraussetzung erfüllt) und „Später“ bis zum nächsten Lerntag.
--    Ausgabe in expeditionen_kind (je Expedition) und als expeditionen_stand (Stationen gesamt/geschafft, oberste Karte) in schule_konto und schule_uebersicht.
-- 3) Aktion api.schule_expedition_spaeter (lernen-api 0.9.3).
-- Sperrt nichts, zählt nicht für „gelandet“, ändert keinen Lernstand. Wiederholbar; kein DROP, kein DELETE.
-- Voraussetzung: 20261125_ex_f_expedition_familie.sql (Familie des Themas, gleiche Regel wie expedition_voraussetzungen_ok).
-- Stand 23.11.: live gibt es noch keine Expeditions-Sterne und keine Antworten auf Expeditionen – keine Nachbuchung nötig (Rauchtest prüft das).

do $$ begin
  if to_regprocedure('schule.thema_familie(bigint)') is null then raise exception 'EX-S: zuerst 20261125_ex_f_expedition_familie.sql einspielen'; end if;
end $$;

-- 1) Regelwerte
insert into schule.regel (schluessel, wert, hinweis) values
  ('sterne_expedition_geschafft', '150'::jsonb, 'EX (23.11.): Expedition geschafft (alle Teile erledigt) – 150 Sterne; bisher 50'),
  ('sterne_expedition_fehlerfrei', '200'::jsonb, 'EX (23.11.): Expedition fehlerfrei – jeder Teil im ersten Versuch richtig, ohne Tipp – 200 statt 150')
on conflict (schluessel) do update set wert = excluded.wert, hinweis = excluded.hinweis;

-- Regelwerte auch in sterne_regeln (für die App)
do $$
declare d text; a text := $a$'sterne_flug_abgelegt', schule.wd_regel('sterne_flug_abgelegt', 100))$a$;
  n text := $a$'sterne_flug_abgelegt', schule.wd_regel('sterne_flug_abgelegt', 100),
    'sterne_expedition_geschafft', schule.wd_regel('sterne_expedition_geschafft', 150), 'sterne_expedition_fehlerfrei', schule.wd_regel('sterne_expedition_fehlerfrei', 200)) /* EX-S */$a$;
begin
  d := pg_get_functiondef('schule.sterne_regeln()'::regprocedure);
  if position('EX-S' in d) > 0 then raise notice 'sterne_regeln schon erweitert'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'EX-S: Anker in sterne_regeln nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;

-- 2) Angebot je Kind und Expedition
create table if not exists schule.expedition_angebot (
  lernender_id  bigint not null references schule.lernender (id),
  expedition_id bigint not null references schule.expedition (id),
  angeboten_am  timestamptz not null,           -- Landung, die die letzte Voraussetzung erfüllt hat
  spaeter_am    timestamptz,                    -- zuletzt „Später“ gedrückt
  spaeter_bis   date,                           -- Lerntag (Ortsdatum des Kindes), an dem „Später“ gedrückt wurde; ab dem nächsten Lerntag wieder vorn
  primary key (lernender_id, expedition_id)
);
alter table schule.expedition_angebot enable row level security;   -- nur über die api-Funktionen (security definer)
revoke all on schule.expedition_angebot from public, anon, authenticated;

-- Ortsdatum des Kindes (gleiche Zeitzone wie schule.lerntag_aus_versuch)
create or replace function schule.kind_heute(p_l bigint)
 returns date language sql stable set search_path to ''
as $$ select (now() at time zone coalesce((select l.zeitzone from schule.lernender l where l.id = p_l), 'UTC'))::date $$;
revoke all on function schule.kind_heute(bigint) from public, anon, authenticated;

-- fehlerfrei: jeder freigegebene Teil – der erste Versuch (außerhalb von Tests) war richtig, ohne Tipp, erster Anlauf
create or replace function schule.expedition_fehlerfrei(p_l bigint, p_x bigint)
 returns boolean language sql stable set search_path to ''
as $$
  select count(*) > 0 and bool_and(coalesce(
           (select v.richtig and coalesce(v.hilfe, 0) = 0 and coalesce(v.anlauf, 1) = 1
              from schule.versuch v where v.lernender_id = p_l and v.aufgabe_id = a.id and v.testsitzung_id is null order by v.am, v.id limit 1), false))
    from schule.aufgabe a where a.expedition_id = p_x and a.freigegeben;
$$;
revoke all on function schule.expedition_fehlerfrei(bigint, bigint) from public, anon, authenticated;

-- Angebot anlegen, sobald alle Voraussetzungen sitzen (nur sichtbare, noch nicht geschaffte Expeditionen). Seit = späteste Landung der Voraussetzungen.
create or replace function schule.expedition_angebot_pruefen(p_l bigint, p_thema bigint default null)
 returns integer language plpgsql security definer set search_path to ''
as $$
declare v_n int;
begin
  insert into schule.expedition_angebot (lernender_id, expedition_id, angeboten_am)
  select p_l, x.id,
         coalesce((select max(k.sitzt_am) from jsonb_array_elements(x.voraussetzungen) v
                     join schule.thema t on coalesce(t.teil_stamm, t.id) = schule.thema_familie((v->>'thema_id')::bigint)   -- RD-S 2: Familie wie expedition_voraussetzungen_ok
                     join schule.einheit e on e.thema_id = t.id
                     join schule.karte_stand k on k.einheit_id = e.id and k.lernender_id = p_l and k.lernziel = v->>'lernziel' and k.sitzt), now())
    from schule.expedition x
   where schule.expedition_sichtbar(p_l, x) and schule.expedition_voraussetzungen_ok(p_l, x)
     and (p_thema is null or exists (select 1 from jsonb_array_elements(x.voraussetzungen) v
                                      where schule.thema_familie((v->>'thema_id')::bigint) = schule.thema_familie(p_thema)))   -- RD-S 2: Familie
     and coalesce(schule.expedition_zustand(p_l, x), '') <> 'geschafft'
  on conflict (lernender_id, expedition_id) do nothing;
  get diagnostics v_n = row_count;
  return v_n;
end $$;
revoke all on function schule.expedition_angebot_pruefen(bigint, bigint) from public, anon, authenticated;

create or replace function schule.expedition_angebot_ausloesen()
 returns trigger language plpgsql security definer set search_path to ''
as $$
begin
  if new.sitzt and (tg_op = 'INSERT' or old.sitzt is distinct from true) then
    perform schule.expedition_angebot_pruefen(new.lernender_id, (select e.thema_id from schule.einheit e where e.id = new.einheit_id));
  end if;
  return null;
end $$;
revoke all on function schule.expedition_angebot_ausloesen() from public, anon, authenticated;
do $$ begin
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.karte_stand'::regclass and tgname = 'karte_expedition_angebot') then
    create trigger karte_expedition_angebot after insert or update of sitzt on schule.karte_stand
      for each row execute function schule.expedition_angebot_ausloesen();
  end if;
end $$;

-- bestehende Stände: Angebote nachtragen, wo die Voraussetzungen schon sitzen (Seit = späteste Landung)
do $$ declare v_n int; begin
  select coalesce(sum(schule.expedition_angebot_pruefen(l.id)), 0) into v_n from schule.lernender l where l.aktiv;
  raise notice 'EX-S: % Angebote für bestehende Stände nachgetragen', v_n;
end $$;

-- Angebot einer Expedition je Kind (für expeditionen_kind und expeditionen_stand)
create or replace function schule.expedition_angebot_json(p_l bigint, p_x bigint)
 returns jsonb language sql stable set search_path to ''
as $$
  select jsonb_build_object('angeboten_am', a.angeboten_am, 'spaeter_am', a.spaeter_am, 'spaeter_bis', a.spaeter_bis,
                            'ausgeblendet', coalesce(a.spaeter_bis >= schule.kind_heute(p_l), false))
    from (select 1) d left join schule.expedition_angebot a on a.lernender_id = p_l and a.expedition_id = p_x;
$$;
revoke all on function schule.expedition_angebot_json(bigint, bigint) from public, anon, authenticated;

-- 1) Buchen: 200 bei fehlerfrei, sonst 150 (Regelwerte); unverändert sonst (Stand live 23.11.)
create or replace function schule.expedition_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_anlauf smallint, p_zeit timestamp with time zone)
 returns void language plpgsql set search_path to ''
as $$
declare a schule.aufgabe; v_e bigint;
begin
  select * into a from schule.aufgabe where id = p_aufgabe;
  if a.id is null or a.pool <> 'expedition' then return; end if;
  v_e := schule.expedition_etappe(p_l, a); -- H11
  if p_richtig then
    if coalesce(p_hilfe, 0) = 0 and coalesce(p_anlauf, 1) = 1 then
      update schule.karte_stand set angewandt_am = p_zeit where lernender_id = p_l and einheit_id = v_e and lernziel = a.variante_gruppe;
    end if;
  else
    perform schule.karte_faellig_machen(p_l, v_e, a.variante_gruppe, p_zeit); -- H8: nur fällig, nie wieder öffnen
  end if;
  if not exists (select 1 from schule.aufgabe t where t.expedition_id = a.expedition_id and t.freigegeben and not schule.expedition_teil_erledigt(p_l, t.id)) then
    insert into schule.sterne(lernender_id, menge, grund, bezug)
    values (p_l, case when schule.expedition_fehlerfrei(p_l, a.expedition_id) then schule.wd_regel('sterne_expedition_fehlerfrei', 200)   -- EX-S
                      else schule.wd_regel('sterne_expedition_geschafft', 150) end, 'expedition', 'expedition:' || a.expedition_id)
    on conflict do nothing;   -- genau einmal je Kind und Expedition (unique lernender_id, grund, bezug)
  end if;
end $$;

-- 2) Ausgabe je Expedition: wie bisher + angeboten_am, spaeter_bis, ausgeblendet, sterne, fehlerfrei; Reihenfolge: begonnen, angeboten (vorn), angeboten (später), geschafft
create or replace function schule.expeditionen_kind(p_lernender bigint)
 returns jsonb language sql stable set search_path to ''
as $$
  select coalesce(jsonb_agg(jsonb_build_object('id', x.id, 'schluessel', x.schluessel, 'titel', x.titel, 'klasse', x.klasse, 'einleitung', x.einleitung, 'grafik', x.grafik,
      'zustand', z.zustand, 'status', x.status,
      'teile', (select coalesce(jsonb_agg(schule.aufgabe_anzeige(a, true) || jsonb_build_object('k', a.teil, 'erledigt', te.erl,
                   'richtig_erst', exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id and v.richtig and coalesce(v.hilfe, 0) = 0 and coalesce(v.anlauf, 1) = 1))
                   || case when te.erl then jsonb_build_object('loesung', a.loesung, 'loesungsweg', a.loesungsweg) else '{}'::jsonb end order by a.reihenfolge, a.id), '[]'::jsonb)
                from schule.aufgabe a cross join lateral (select schule.expedition_teil_erledigt(p_lernender, a.id) erl) te
               where a.expedition_id = x.id and a.freigegeben),
      'teile_gesamt', (select count(*) from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben),
      'teile_selbst', (select count(*) from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben
                        and exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id and v.testsitzung_id is null and v.richtig and coalesce(v.hilfe, 0) = 0 and coalesce(v.anlauf, 1) = 1)),
      'teile_erledigt', (select count(*) from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben and schule.expedition_teil_erledigt(p_lernender, a.id)))
      || an.j   -- EX-S: angeboten_am, spaeter_am, spaeter_bis, ausgeblendet
      || jsonb_build_object('sterne', (select s.menge from schule.sterne s where s.lernender_id = p_lernender and s.grund = 'expedition' and s.bezug = 'expedition:' || x.id),
                            'fehlerfrei', z.zustand = 'geschafft' and schule.expedition_fehlerfrei(p_lernender, x.id),
                            'sterne_geschafft', schule.wd_regel('sterne_expedition_geschafft', 150), 'sterne_fehlerfrei', schule.wd_regel('sterne_expedition_fehlerfrei', 200))
      order by case when z.zustand = 'begonnen' then 1 when z.zustand = 'angeboten' and not (an.j->>'ausgeblendet')::boolean then 2 when z.zustand = 'angeboten' then 3 else 4 end,
               an.j->>'angeboten_am' nulls last, x.id), '[]'::jsonb)
    from schule.expedition x cross join lateral (select schule.expedition_zustand(p_lernender, x) zustand) z
         cross join lateral (select schule.expedition_angebot_json(p_lernender, x.id) j) an
   where schule.expedition_sichtbar(p_lernender, x) and z.zustand is not null;
$$;

-- 2) Stand für Abflugtafel und Stempel-Sammlung: Stationen gesamt/geschafft, offene Angebote, oberste Karte
create or replace function schule.expedition_stand(p_l bigint)
 returns jsonb language sql stable set search_path to ''
as $$
  with x as (select x.id, schule.expedition_zustand(p_l, x) zustand, schule.expedition_angebot_json(p_l, x.id) an
               from schule.expedition x
              where schule.expedition_sichtbar(p_l, x) and exists (select 1 from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben))
  select jsonb_build_object(
    'stationen_gesamt', (select count(*) from x),
    'stationen_geschafft', (select count(*) from x where zustand = 'geschafft'),
    'angeboten', (select count(*) from x where zustand in ('angeboten', 'begonnen')),
    'vorn', (select count(*) from x where zustand in ('angeboten', 'begonnen') and not (an->>'ausgeblendet')::boolean),
    'oben_id', (select id from x where zustand in ('angeboten', 'begonnen') and not (an->>'ausgeblendet')::boolean
                 order by case zustand when 'begonnen' then 1 else 2 end, an->>'angeboten_am' nulls last, id limit 1),
    'heute', schule.kind_heute(p_l),
    'angebote', (select coalesce(jsonb_agg(jsonb_build_object('expedition_id', id, 'zustand', zustand) || an order by id), '[]') from x where an->>'angeboten_am' is not null));
$$;
revoke all on function schule.expedition_stand(bigint) from public, anon, authenticated;

-- 3) „Später“: blendet die Expedition bis zum nächsten Lerntag aus (sperrt nichts)
create or replace function schule.expedition_spaeter(p_l bigint, p_x bigint)
 returns jsonb language plpgsql security definer set search_path to ''
as $$
declare v_h date := schule.kind_heute(p_l);
begin
  update schule.expedition_angebot set spaeter_am = now(), spaeter_bis = v_h where lernender_id = p_l and expedition_id = p_x;
  if not found then raise exception 'Expedition ist nicht angeboten' using errcode = 'P0001'; end if;
  return jsonb_build_object('expedition_id', p_x, 'spaeter_bis', v_h);
end $$;
revoke all on function schule.expedition_spaeter(bigint, bigint) from public, anon, authenticated;

create or replace function api.schule_expedition_spaeter(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint; v_x bigint := nullif(p_daten->>'expedition_id', '')::bigint;
begin
  perform schule.zugriff(p_schluessel, v_l);
  if not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true, 'lernender_id', v_l) || schule.expedition_spaeter(v_l, v_x) || jsonb_build_object('expeditionen_stand', schule.expedition_stand(v_l));
end $$;
grant execute on function api.schule_expedition_spaeter(text, jsonb) to council_mcp;
revoke all on function api.schule_expedition_spaeter(text, jsonb) from public, anon, authenticated;

-- expeditionen_stand in schule_konto (Kinderseite) und je Kind in schule_uebersicht
do $$
declare d text; a text := $a$'expeditionen', schule.expeditionen_kind(v_l),$a$;
  n text := $a$'expeditionen', schule.expeditionen_kind(v_l), 'expeditionen_stand', schule.expedition_stand(v_l), -- EX-S$a$;
begin
  d := pg_get_functiondef('api.schule_konto(text, jsonb)'::regprocedure);
  if position('EX-S' in d) > 0 then raise notice 'schule_konto schon erweitert'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'EX-S: Anker in schule_konto nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;
do $$
declare d text; a text := $a$'route', (select coalesce(jsonb_agg(jsonb_build_object('block_id', r.block_id,$a$;
  n text := $a$'expeditionen_stand', schule.expedition_stand(l.id), /* EX-S */ 'route', (select coalesce(jsonb_agg(jsonb_build_object('block_id', r.block_id,$a$;
begin
  if to_regprocedure('api.schule_uebersicht(text, jsonb)') is null then raise notice 'EX-S: schule_uebersicht fehlt (nur im Nachbau)'; return; end if;
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  if position('EX-S' in d) > 0 then raise notice 'schule_uebersicht schon erweitert'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'EX-S: Anker in schule_uebersicht nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;
