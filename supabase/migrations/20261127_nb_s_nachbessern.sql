-- NB-S (Entscheidung des Nutzers 23.11. 02:54): eine wieder offene Etappe wird dem Kind immer zuerst vorgelegt – auch bei fertigem Ort und bei
-- „Kann er“-Setzung mit Rückfall.
-- „Wieder offen“ wie bisher (karte_buchen, unverändert): zwei Fehler in Folge in der fälligen Wiederholung → sitzt = false, geoeffnet_am, folge 0;
-- zurück nach Landeregel mit 3 eigenen Lösungen in Folge (Tipp/2. Versuch zählt nicht, folge bleibt) → sitzt, Wiederholung ab Stufe 0.
-- Neu nur lesend:
--   schule.nachbessern(kind)            Liste je Kind (Thema, Einheit, Etappe, Titel, wieder offen seit, Folge x von 3, Ort fertig, Setzung)
--   api.schule_konto                    + 'nachbessern'
--   api.schule_uebersicht (je Kind)     + 'nachbessern'
--   schule.reise_karte                  'naechster_start' mit grund 'nachbessern' vor 'dran'; + 'nachbessern'
-- Fahrplan (route), Stempel, Sterne, Lernstand unverändert: keine Schreib-Funktion, keine Tabelle, kein Trigger.
-- Baut auf LZ-S und ZP-S auf. Wiederholbar; kein DROP, kein DELETE.

do $$ begin
  if position('-- LZ-S' in pg_get_functiondef('schule.thema_stufe(bigint, bigint)'::regprocedure)) = 0 then
    raise exception 'NB-S: zuerst 20261126_lz_s_ladezeit.sql einspielen'; end if;
  if to_regclass('schule.zusatz_geschafft') is null or position('ZP-S' in pg_get_functiondef('schule.reise_karte(bigint)'::regprocedure)) = 0 then
    raise exception 'NB-S: zuerst 20261126_zp_s_zusatz_plan.sql einspielen'; end if;
end $$;

-- Liste „nachbessern“ je Kind. Gleiche Bedingung wie thema_stufe.wieder_offen und reise_etappe_stand 'wieder_offen' (nicht sitzt, schon einmal
-- gelandet), aber über alle Etappen der aktuellen Einheit (auch Kür, auch fertiger Ort, auch gesetzt) – Kennzeichen 'pflicht' zum Sortieren.
-- Älteste zuerst.
create or replace function schule.nachbessern(p_l bigint)
 returns jsonb language sql stable set search_path to ''
as $$
  select coalesce(jsonb_agg(jsonb_build_object(
           'thema_id', e.thema_id, 'titel', t.unterthema, 'einheit_id', k.einheit_id, 'block_id', e.block_id, 'stadt', b.stadt,
           'lernziel', k.lernziel, 'etappe_nr', et.nr, 'etappe', et.titel,
           'pflicht', pf.l is null or k.lernziel = any(pf.l),
           'wieder_offen_seit', coalesce(k.geoeffnet_am, k.zuletzt),
           'folge', least(coalesce(k.folge, 0), n.noetig), 'folge_noetig', n.noetig, 'noch', greatest(n.noetig - coalesce(k.folge, 0), 0),
           'ort_fertig', exists (select 1 from schule.route r where r.lernender_id = p_l and r.block_id = e.block_id and r.art = 'normal' and r.status = 'fertig'),
           'gesetzt', case when schule.thema_kann_schon(p_l, e.thema_id) then 'komplett' when schule.thema_kann_wdh(p_l, e.thema_id) then 'wiederholen'
                           when k.gesetzt_am is not null then 'etappe' end)
           order by coalesce(k.geoeffnet_am, k.zuletzt), e.thema_id, et.nr), '[]'::jsonb)
    from schule.karte_stand k
    join schule.einheit e on e.id = k.einheit_id and e.id = schule.thema_einheit(e.thema_id)
    join schule.thema t on t.id = e.thema_id
    left join schule.block b on b.id = e.block_id
    cross join lateral (select x->>'titel' titel, o::int nr from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality q(x, o)
                         where x->>'lernziel' = k.lernziel limit 1) et
    cross join lateral (select least(3, schule.karte_ziel(k.einheit_id, k.lernziel)) noetig) n
    cross join lateral (select schule.pflicht_lernziele(p_l, k.einheit_id) l) pf
   where k.lernender_id = p_l and not k.sitzt and k.sitzt_am is not null;
$$;
revoke all on function schule.nachbessern(bigint) from public, anon, authenticated;

-- Nächster Start „nachbessern“: erster Eintrag der Liste, dessen Flug auf der Reisekarte liegt; Felder wie bisher (thema_id, kontinent_id, land,
-- iso, titel, grund, stadt, staedte) und dazu etappe, folge, folge_noetig, einheit_id.
create or replace function schule.nachbessern_start(p_kont jsonb, p_nb jsonb)
 returns jsonb language sql immutable set search_path to ''
as $$
  select jsonb_build_object('thema_id', x.f->'thema_id', 'kontinent_id', x.k->'id', 'land', x.f->'land', 'iso', x.f->'iso', 'titel', x.f->'titel',
           'grund', 'nachbessern',
           'stadt', coalesce((select jsonb_build_object('nr', s->'nr', 'name', s->'name', 'lernziel', s->'lernziel', 'pflicht', s->'pflicht')
                                from jsonb_array_elements(x.f->'staedte') s where s->>'lernziel' = nb.n->>'lernziel' limit 1),
                             jsonb_build_object('lernziel', nb.n->'lernziel', 'pflicht', nb.n->'pflicht')),
           'staedte', jsonb_array_length(coalesce(x.f->'staedte', '[]'::jsonb)),
           'einheit_id', nb.n->'einheit_id', 'etappe', nb.n->'etappe', 'folge', nb.n->'folge', 'folge_noetig', nb.n->'folge_noetig')
    from jsonb_array_elements(coalesce(p_nb, '[]'::jsonb)) with ordinality nb(n, o)
    cross join lateral (select k, f from jsonb_array_elements(p_kont) k, jsonb_array_elements(k->'fluege') f
                         where f->>'thema_id' = nb.n->>'thema_id' limit 1) x
   order by nb.o limit 1;
$$;
revoke all on function schule.nachbessern_start(jsonb, jsonb) from public, anon, authenticated;

-- Reisekarte: grund 'nachbessern' vor 'dran'/'kommt'; Liste dazu
do $$
declare d text;
  a text := $a$'naechster_start', v_start,$a$;
  n text := $a$'naechster_start', coalesce(schule.nachbessern_start(v_kont, schule.nachbessern(p_l)), v_start), 'nachbessern', schule.nachbessern(p_l), /* NB-S */$a$;
begin
  d := pg_get_functiondef('schule.reise_karte(bigint)'::regprocedure);
  if position('NB-S' in d) > 0 then raise notice 'reise_karte schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'NB-S: Anker in reise_karte nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;

-- schule_konto: Liste neben dem Konto
do $$
declare d text;
  a text := $a$'konto', schule.konto_wd(v_l),$a$;
  n text := $a$'konto', schule.konto_wd(v_l), 'nachbessern', schule.nachbessern(v_l), /* NB-S */$a$;
begin
  d := pg_get_functiondef('api.schule_konto(text, jsonb)'::regprocedure);
  if position('NB-S' in d) > 0 then raise notice 'schule_konto schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'NB-S: Anker in schule_konto nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;

-- schule_uebersicht: je Kind
do $$
declare d text;
  a text := $a$'expeditionen_stand', schule.expedition_stand(l.id), /* EX-S */$a$;
  n text := $a$'expeditionen_stand', schule.expedition_stand(l.id), /* EX-S */ 'nachbessern', schule.nachbessern(l.id), /* NB-S */$a$;
begin
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  if position('NB-S' in d) > 0 then raise notice 'schule_uebersicht schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'NB-S: Anker in schule_uebersicht nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;
