-- ZP-S (Bau-Auftrag ZP, Entscheidung Sebastian 23.11. 02:35; Nachtrag Rückläufer ChatGPT 964): eingeplanter Zusatz-Teil.
-- Zwei getrennte Eigenschaften:
--   1) Pflicht/Kür je Gruppe – unverändert (thema.zusatz, Pflichtlisten der Einheit).
--   2) „von den Eltern eingeplant“ mit eigenem Platz – der Plan-Eintrag bleibt route.art 'normal' an seiner Position (die Eltern-Planung der App
--      kann ihn sehen, verschieben, abwählen); daraus und aus 1) leitet der Server „Zusatz · eingeplant“ ab (schule.zusatz_eingeplant / zusatz_ort).
-- Regeln: kein Pflicht-Weiterflug (Reiseoptionen, nächster Flug, Kinder-Übersicht), nicht für Visum (unverändert), nicht in die Lehrplan-Quote
-- (unverändert); Fortschritt über alle Etappen; kein Flug-Test, keine Nachtests („wie ohne Test“).
-- „Zusatz geschafft“: alle Etappen selbst gelandet → bewusste Buchung schule.zusatz_geschafft_buchen: Zeile in schule.zusatz_geschafft,
-- Stempel (flug_erstabschluss) und 100 Sterne (grund 'ort', bezug 'block:…', Regelwert sterne_ort_geschafft) je genau einmal; danach Ort „fertig“
-- (route_sterne findet die Sterne schon vor und bucht nichts). Nicht eingeplante Zusatz-Teile: freiwillig, ohne Stempel.
-- Gruppenwechsel: wird der Teil Pflicht, gilt die normale Regel (Ort wieder offen, Flug-Test der Pflicht-Etappen); Stempel/Sterne bleiben, nichts doppelt.
-- Baut auf LZ-S auf. Wiederholbar; kein DROP, kein DELETE.

do $$ begin
  if position('-- LZ-S' in pg_get_functiondef('schule.thema_stufe(bigint, bigint)'::regprocedure)) = 0 then
    raise exception 'ZP-S: zuerst 20261126_lz_s_ladezeit.sql einspielen'; end if;
end $$;

-- Reparatur: von Eltern angelegte Plan-Einträge, die auf art 'zusatz' stehen, zurück auf 'normal' (Platz und Absicht bleiben; sonst verwirft die
-- Eltern-Planung den Eintrag). Heute keiner; route 485 ist art 'normal' an Platz 21 und bleibt so. Einträge des Systems (Entdecker-Orte) bleiben 'zusatz'.
do $$ declare v_n int; begin
  update schule.route r set art = 'normal'
   where r.art = 'zusatz' and r.geaendert_von like 'eltern:%' and r.status <> 'entfernt'
     and not exists (select 1 from schule.route x where x.lernender_id = r.lernender_id and x.block_id = r.block_id and x.art = 'normal' and x.id <> r.id);
  get diagnostics v_n = row_count;
  raise notice 'ZP-S: % Eltern-Einträge von art zusatz auf normal zurückgestellt', v_n;
end $$;

-- „Zusatz geschafft“ je Kind und Thema (die bewusste Buchung)
create table if not exists schule.zusatz_geschafft (
  lernender_id bigint not null references schule.lernender (id),
  thema_id     bigint not null references schule.thema (id),
  einheit_id   bigint not null references schule.einheit (id),
  block_id     bigint not null references schule.block (id),
  sterne       integer not null,
  am           timestamptz not null default now(),
  primary key (lernender_id, thema_id)
);
alter table schule.zusatz_geschafft enable row level security;
revoke all on schule.zusatz_geschafft from public, anon, authenticated;

-- Zusatz in der Gruppe des Kindes und von den Eltern eingeplant (Plan-Eintrag art 'normal', nicht abgewählt; ein fertiger Ort bleibt eingeplant)
create or replace function schule.zusatz_eingeplant(p_l bigint, p_thema bigint)
 returns boolean language sql stable set search_path to ''
as $$
  select coalesce((select schule.kind_gruppe(p_l) = any(t.zusatz) from schule.thema t where t.id = p_thema), false)
     and exists (select 1 from schule.route r join schule.block_thema bt on bt.block_id = r.block_id and bt.thema_id = p_thema
                  where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt'
                    and (schule.ist_plan(r) or r.status = 'fertig')
                    and not (p_thema = any(coalesce(r.ausgelassen, '{}'))));
$$;
revoke all on function schule.zusatz_eingeplant(bigint, bigint) from public, anon, authenticated;

-- Ort ist ein eingeplanter Zusatz-Ort: mindestens ein eingeplanter Zusatz-Teil und kein geplanter Pflicht-Flug darin
create or replace function schule.zusatz_ort(p_l bigint, p_block bigint)
 returns boolean language sql stable set search_path to ''
as $$
  select exists (select 1 from schule.block_thema bt where bt.block_id = p_block and schule.zusatz_eingeplant(p_l, bt.thema_id))
     and not exists (select 1 from schule.block_thema bt join schule.thema t on t.id = bt.thema_id
                      where bt.block_id = p_block and schule.thema_einheit(t.id) is not null
                        and not coalesce(schule.kind_gruppe(p_l) = any(t.zusatz), false)
                        and not exists (select 1 from schule.route r where r.lernender_id = p_l and r.block_id = p_block and r.art = 'normal'
                                          and r.status <> 'entfernt' and t.id = any(coalesce(r.ausgelassen, '{}'))));
$$;
revoke all on function schule.zusatz_ort(bigint, bigint) from public, anon, authenticated;

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

-- Ort-Stand: eingeplanter Zusatz ist erledigt, sobald „Zusatz geschafft“ gebucht ist (nicht schon beim bloßen Landen)
do $$
declare d text;
  a text := $a$when th.einheit_id is null then 'keine_einheit'$a$;
  n text := $a$when th.einheit_id is null then 'keine_einheit'
      when schule.zusatz_eingeplant(p_lernender, th.thema_id) then case when exists (select 1 from schule.zusatz_geschafft z
             where z.lernender_id = p_lernender and z.thema_id = th.thema_id) then 'erledigt' else 'offen' end /* ZP-S */$a$;
begin
  d := pg_get_functiondef('schule.ort_stand(bigint, bigint)'::regprocedure);
  if position('ZP-S' in d) > 0 then raise notice 'ort_stand schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'ZP-S: Anker in ort_stand nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;

-- Bewusste Buchung „Zusatz geschafft“: Stempel und 100 Sterne je genau einmal, danach Ort „fertig“. true = jetzt gebucht.
create or replace function schule.zusatz_geschafft_buchen(p_l bigint, p_thema bigint)
 returns boolean language plpgsql security definer set search_path to ''
as $$
declare v_e bigint := schule.thema_einheit(p_thema); v_b bigint; v_s int := schule.sterne_regel('sterne_ort_geschafft'); v_neu boolean := false;
begin
  if v_e is null or not schule.zusatz_eingeplant(p_l, p_thema) then return false; end if;
  select r.block_id into v_b from schule.route r join schule.block_thema bt on bt.block_id = r.block_id and bt.thema_id = p_thema
   where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt' order by r.id limit 1;
  if not exists (select 1 from schule.zusatz_geschafft z where z.lernender_id = p_l and z.thema_id = p_thema) then
    if not schule.zusatz_gelandet(p_l, v_e) then return false; end if;
    insert into schule.zusatz_geschafft (lernender_id, thema_id, einheit_id, block_id, sterne) values (p_l, p_thema, v_e, v_b, v_s)
      on conflict (lernender_id, thema_id) do nothing;
    v_neu := found;
    if v_neu then
      insert into schule.flug_erstabschluss (lernender_id, einheit_id, sitzung_id, am) values (p_l, v_e, null, now())
        on conflict (lernender_id, einheit_id) do nothing;                                       -- Stempel, genau einmal
      insert into schule.sterne (lernender_id, menge, grund, bezug) values (p_l, v_s, 'ort', 'block:' || v_b)
        on conflict do nothing;                                                                   -- 100 Sterne, genau einmal
    end if;
  end if;
  -- Ort „fertig“, wenn alle seine Flüge erledigt sind (Sterne sind schon gebucht; route_sterne bucht nichts doppelt); geaendert_von bleibt
  update schule.route r set status = 'fertig', geaendert_am = now(), revision = r.revision + 1
   where r.lernender_id = p_l and r.block_id = v_b and r.art = 'normal' and r.status not in ('fertig', 'entfernt')
     and coalesce((schule.ort_stand(p_l, v_b)->>'abgeschlossen')::boolean, false);
  return v_neu;
end $$;
revoke all on function schule.zusatz_geschafft_buchen(bigint, bigint) from public, anon, authenticated;

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

-- Stufe: Etappen = alle Etappen; Kennzeichen zusatz, zusatz_eingeplant, zusatz_geschafft
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
    || case when v_zp then jsonb_build_object('zusatz', true, 'zusatz_eingeplant', true,
         'zusatz_geschafft', exists (select 1 from schule.zusatz_geschafft z where z.lernender_id = p_l and z.thema_id = p_thema)) else '{}'::jsonb end; -- ZP-S$a$;
begin
  d := pg_get_functiondef('schule.thema_stufe(bigint, bigint)'::regprocedure);
  if position('ZP-S' in d) > 0 then raise notice 'thema_stufe schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a1, ''))) / length(a1) <> 1 or (length(d) - length(replace(d, a2, ''))) / length(a2) <> 1
     or (length(d) - length(replace(d, a3, ''))) / length(a3) <> 1 then raise exception 'ZP-S: Anker in thema_stufe nicht genau einmal gefunden'; end if;
  execute replace(replace(replace(d, a1, n1), a2, n2), a3, n3);
end $$;

-- Reisekarte: je Flug zusatz_eingeplant/zusatz_geschafft, je Stadt zaehlt; nächster Start bleibt beim Pflicht-Flug
do $$
declare d text;
  a1 text := $a$v_rang int; v_best int := 2147483647; v_offen jsonb;$a$;
  n1 text := $a$v_rang int; v_best int := 2147483647; v_offen jsonb; v_zp boolean; -- ZP-S$a$;
  a2 text := $a$v_stufe := schule.thema_stufe(p_l, v_f.thema_id);$a$;
  n2 text := $a$v_stufe := schule.thema_stufe(p_l, v_f.thema_id); v_zp := coalesce((v_stufe->>'zusatz_eingeplant')::boolean, false); -- ZP-S$a$;
  a3 text := $a$'lernziel', v_s.lernziel, 'titel', v_s.titel, 'pflicht', v_pfl, 'stand', v_stand);$a$;
  n3 text := $a$'lernziel', v_s.lernziel, 'titel', v_s.titel, 'pflicht', v_pfl, 'stand', v_stand)
                                    || case when v_zp then jsonb_build_object('zaehlt', true) else '{}'::jsonb end); -- ZP-S$a$;
  a4 text := $a$v_st := v_st || jsonb_build_object('nr', v_s.nr,$a$;
  n4 text := $a$v_st := v_st || (jsonb_build_object('nr', v_s.nr,$a$;
  a5 text := $a$'plan_platz', v_platz, 'zusatz', v_f.zus,$a$;
  n5 text := $a$'plan_platz', v_platz, 'zusatz', v_f.zus, 'zusatz_eingeplant', v_zp, 'zusatz_geschafft', coalesce((v_stufe->>'zusatz_geschafft')::boolean, false), -- ZP-S
       $a$;
begin
  d := pg_get_functiondef('schule.reise_karte(bigint)'::regprocedure);
  if position('ZP-S' in d) > 0 then raise notice 'reise_karte schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a1, ''))) / length(a1) <> 1 or (length(d) - length(replace(d, a2, ''))) / length(a2) <> 1
     or (length(d) - length(replace(d, a3, ''))) / length(a3) <> 1 or (length(d) - length(replace(d, a4, ''))) / length(a4) <> 1
     or (length(d) - length(replace(d, a5, ''))) / length(a5) <> 1 then raise exception 'ZP-S: Anker in reise_karte nicht genau einmal gefunden'; end if;
  execute replace(replace(replace(replace(replace(d, a1, n1), a2, n2), a3, n3), a4, n4), a5, n5);
end $$;

-- Reiseoptionen: ein eingeplanter Zusatz-Ort ist kein Pflicht-Weiterflug (der nächste Pflicht-Ort des Kontinents bleibt erreichbar)
do $$
declare d text;
  a text := $a$where s.status <> 'fertig' and not s.kann_schon and s.art <> 'zusatz'$a$;
  n text := $a$where s.status <> 'fertig' and not s.kann_schon and s.art <> 'zusatz' and not schule.zusatz_ort(p_lernender, b.id) /* ZP-S */$a$;
begin
  d := pg_get_functiondef('schule.reiseoptionen(bigint)'::regprocedure);
  if position('ZP-S' in d) > 0 then raise notice 'reiseoptionen schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'ZP-S: Anker in reiseoptionen nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;

-- Nächster Flug (nach einem Abschluss): kein eingeplanter Zusatz
do $$
declare d text;
  a text := $a$and schule.thema_einheit(bt.thema_id) is not null and schule.thema_stand(p_l, bt.thema_id) <> 'erledigt'$a$;
  n text := $a$and schule.thema_einheit(bt.thema_id) is not null and schule.thema_stand(p_l, bt.thema_id) <> 'erledigt' and not schule.zusatz_eingeplant(p_l, bt.thema_id) /* ZP-S */$a$;
begin
  if to_regprocedure('schule.naechster_flug(bigint, bigint)') is null then raise notice 'ZP-S: naechster_flug fehlt (nur im Nachbau)'; return; end if;
  d := pg_get_functiondef('schule.naechster_flug(bigint, bigint)'::regprocedure);
  if position('ZP-S' in d) > 0 then raise notice 'naechster_flug schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'ZP-S: Anker in naechster_flug nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;

-- Zusatz-Plan je Kind (eigener Platz, Fortschritt x/y, geschafft): für die kommende App
create or replace function schule.zusatz_plan_json(p_l bigint)
 returns jsonb language sql stable set search_path to ''
as $$
  select coalesce(jsonb_agg(jsonb_build_object('route_id', r.id, 'block_id', r.block_id, 'position', r.position, 'status', r.status,
           'thema_id', bt.thema_id, 'einheit_id', schule.thema_einheit(bt.thema_id),
           'etappen', cardinality(schule.etappen_alle(schule.thema_einheit(bt.thema_id))),
           'gelandet', (select count(*) from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = schule.thema_einheit(bt.thema_id)
                          and k.sitzt and k.lernziel = any(schule.etappen_alle(schule.thema_einheit(bt.thema_id)))),
           'geschafft', z.am is not null, 'geschafft_am', z.am, 'sterne', z.sterne) order by r.position, bt.reihenfolge), '[]'::jsonb)
    from schule.route r join schule.block_thema bt on bt.block_id = r.block_id
    left join schule.zusatz_geschafft z on z.lernender_id = p_l and z.thema_id = bt.thema_id
   where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt' and schule.zusatz_eingeplant(p_l, bt.thema_id);
$$;
revoke all on function schule.zusatz_plan_json(bigint) from public, anon, authenticated;

-- schule_uebersicht (Kinderseite und Überblick, lernReiseDaten der App 0.90.1): offene eingeplante Zusatz-Orte nicht in „route“ (sonst „jetzt“ und
-- nächster Flug, obwohl ohne Pflicht-Etappe nie „geschafft“); der Flug bleibt sichtbar (nach Klasse „zum Auffrischen“/„später“). Geschafft →
-- Eintrag mit status 'fertig' wie bisher („kann“). Neu je Kind: zusatz_plan.
do $$
declare d text;
  a1 text := $a$from schule.route r where r.lernender_id = l.id and (r.art <> 'normal' or schule.ist_plan(r) or r.status = 'fertig' or r.kann_schon)),$a$;
  n1 text := $a$from schule.route r where r.lernender_id = l.id and (r.art <> 'normal' or schule.ist_plan(r) or r.status = 'fertig' or r.kann_schon)
                  and not (r.art = 'normal' and r.status <> 'fertig' and schule.zusatz_ort(l.id, r.block_id))), /* ZP-S */
      'zusatz_plan', schule.zusatz_plan_json(l.id),$a$;
begin
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  if position('ZP-S' in d) > 0 then raise notice 'schule_uebersicht schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a1, ''))) / length(a1) <> 1 then raise exception 'ZP-S: Anker in schule_uebersicht nicht genau einmal gefunden'; end if;
  execute replace(d, a1, n1);
end $$;

-- schule_plan_lesen (Eltern-Planung): Eintrag bleibt art 'normal' (sichtbar, verschiebbar, abwählbar); Kennzeichen zusatz_eingeplant je Plan-Eintrag
do $$
declare d text;
  a text := $a$'geaendert_von', r.geaendert_von, 'geaendert_am', r.geaendert_am)$a$;
  n text := $a$'geaendert_von', r.geaendert_von, 'geaendert_am', r.geaendert_am)
                 || case when r.art = 'normal' and schule.zusatz_ort(v_l, r.block_id) then jsonb_build_object('zusatz_eingeplant', true) else '{}'::jsonb end /* ZP-S */$a$;
begin
  d := pg_get_functiondef('api.schule_plan_lesen(text, jsonb)'::regprocedure);
  if position('ZP-S' in d) > 0 then raise notice 'schule_plan_lesen schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'ZP-S: Anker in schule_plan_lesen nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;

-- Abgleich je Kind: „Zusatz geschafft“ buchen, wo fällig; nach Gruppenwechsel zu Pflicht Ort wieder öffnen
create or replace function schule.zusatz_plan_abgleich(p_l bigint, p_thema bigint default null, p_wieder_auf bigint[] default '{}')
 returns integer language plpgsql security definer set search_path to ''
as $$
declare v_n int := 0; v_t bigint;
begin
  for v_t in select distinct bt.thema_id from schule.route r join schule.block_thema bt on bt.block_id = r.block_id
              where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt' and (p_thema is null or bt.thema_id = p_thema)
                and schule.zusatz_eingeplant(p_l, bt.thema_id) loop
    if schule.zusatz_geschafft_buchen(p_l, v_t) then v_n := v_n + 1; end if;
  end loop;
  if cardinality(p_wieder_auf) > 0 then
    update schule.route r set status = 'offen', geaendert_am = now(), revision = r.revision + 1
     where r.lernender_id = p_l and r.art = 'normal' and r.status = 'fertig' and r.block_id = any(p_wieder_auf)
       and not coalesce((schule.ort_stand(p_l, r.block_id)->>'abgeschlossen')::boolean, false);
  end if;
  return v_n;
end $$;
revoke all on function schule.zusatz_plan_abgleich(bigint, bigint, bigint[]) from public, anon, authenticated;

-- Auslöser 1: Landung (oder Rücknahme von „gesetzt“) einer Etappe
create or replace function schule.zusatz_landung_ausloesen()
 returns trigger language plpgsql security definer set search_path to ''
as $$
declare v_t bigint;
begin
  if new.sitzt and (tg_op = 'INSERT' or old.sitzt is distinct from true or old.gesetzt_am is distinct from new.gesetzt_am) then
    select e.thema_id into v_t from schule.einheit e where e.id = new.einheit_id;
    if schule.zusatz_eingeplant(new.lernender_id, v_t) then perform schule.zusatz_geschafft_buchen(new.lernender_id, v_t); end if;
  end if;
  return null;
end $$;
revoke all on function schule.zusatz_landung_ausloesen() from public, anon, authenticated;

-- Auslöser 2: Plan-Eintrag neu oder geändert (z. B. Zusatz-Teil nach dem Landen eingeplant, Ort wieder geöffnet) – nur erste Ebene, keine Schleife
create or replace function schule.zusatz_route_ausloesen()
 returns trigger language plpgsql security definer set search_path to ''
as $$
begin
  if new.art = 'normal' and new.status <> 'entfernt' and pg_trigger_depth() < 2 then
    perform schule.zusatz_geschafft_buchen(new.lernender_id, bt.thema_id) from schule.block_thema bt
      where bt.block_id = new.block_id and schule.zusatz_eingeplant(new.lernender_id, bt.thema_id);
  end if;
  return null;
end $$;
revoke all on function schule.zusatz_route_ausloesen() from public, anon, authenticated;

-- Auslöser 3: Gruppenwechsel – Zusatz wird Pflicht (Ort wieder offen, Test steht an) bzw. Pflicht wird Zusatz (ggf. schon geschafft)
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
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.route'::regclass and tgname = 'route_zusatz_abschluss') then
    create trigger route_zusatz_abschluss after insert or update of art, status, ausgelassen, geaendert_von on schule.route
      for each row execute function schule.zusatz_route_ausloesen();
  end if;
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.lernender'::regclass and tgname = 'lernender_zusatz_abgleich') then
    -- Name nach lernender_pflicht_abgleich (Auslöser laufen alphabetisch): die Pflicht-Zeilen sind dann schon abgeglichen
    create trigger lernender_zusatz_abgleich after update of schulart, zweig on schule.lernender
      for each row execute function schule.zusatz_gruppe_ausloesen();
  end if;
end $$;

-- bestehende Stände: eingeplante Zusatz-Teile, die schon ganz selbst gelandet sind, jetzt buchen (heute keiner)
do $$ declare v_n int; begin
  select coalesce(sum(schule.zusatz_plan_abgleich(l.id)), 0) into v_n from schule.lernender l where l.aktiv;
  raise notice 'ZP-S: % „Zusatz geschafft“ für bestehende Stände gebucht', v_n;
end $$;
