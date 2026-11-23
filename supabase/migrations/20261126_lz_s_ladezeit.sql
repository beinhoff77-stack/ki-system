-- LZ-S (Bau-Auftrag LZ, 23.11.): Ladezeit der Lehrer-Seiten. Ergebnisse inhaltlich unverändert (Rauchtest lz_s: md5 vorher = nachher).
-- Größte Posten (gemessen lesend auf dem echten Stand, explain analyze):
--  1) stufe_etappen: die Pflichtliste (pflicht_lernziele) wurde je Etappe neu berechnet (CTE eingebettet → je Element von unnest ein Aufruf);
--     thema_stufe ruft stufe_etappen zusätzlich je Karte im WHERE auf. 105 Aufrufe stufe_etappen: 409 ms → 53 ms bei einmaliger Berechnung.
--  2) thema_klassen je Thema über die Sicht thema_lage_klasse (die Sicht rechnet jedes Mal alle Themen): 105 Aufrufe 741 ms; die Sicht einmal: 10 ms.
--  3) thema_jahrgang und „pflicht“ der Matrix: Planer beginnt bei quelle → eintrag → zuordnung (84 630 Schleifen je 105 Themen): 118 ms → 8,5 ms,
--     wenn zuordnung über thema_id zuerst gelesen wird.
-- Wiederholbar; kein DROP, kein DELETE. thema_stufe bleibt als Funktion mit gleichem Ergebnis.

-- 3) Index und Lesereihenfolge für Zuordnungen je Thema
create index if not exists zuordnung_thema_id_idx on schule.zuordnung (thema_id, eintrag_id);

create or replace function schule.thema_jahrgang(p_thema bigint)
 returns jsonb language sql stable set search_path to ''
as $$
  select jsonb_strip_nulls(coalesce((select jsonb_object_agg(x.schulart, x.jahr) from (
    select q.schulart, min(q.jahr_von) jahr
      from (select z0.eintrag_id from schule.zuordnung z0 where z0.thema_id = p_thema offset 0) z   -- LZ-S: Zuordnungen des Themas zuerst
      join schule.eintrag e on e.id = z.eintrag_id join schule.quelle q on q.id = e.quelle_id
     where q.aktiv and q.rolle = 'basis' and not e.archiviert group by q.schulart) x), '{}'::jsonb)
    || coalesce((select t.klasse_fest from schule.thema t where t.id = p_thema), '{}'::jsonb));
$$;

-- 1) Pflichtliste: einmal lesen (Bewertung einmal aus der Einheit), gleiche Reihenfolge Gruppe → Schulart → lernziele_pflicht
create or replace function schule.pflicht_lernziele(p_l bigint, p_e bigint)
 returns text[] language plpgsql stable set search_path to ''
as $$
  -- T2: null = keine Pflichtliste festgelegt (Aufrufer fallen wie bisher auf „alle Etappen“ zurück);
  --     '{}' = ausdrücklich leer: KEINE Pflicht-Etappe (freiwilliger Zusatz, kein Pflicht-Test, kein Stempel, keine 100 Sterne)
declare v_b jsonb; v_k text; v_x jsonb;
begin
  select e.inhalt->'bewertung' into v_b from schule.einheit e where e.id = p_e;
  if not found then return null; end if;
  for v_k in select u.k from unnest(schule.pflicht_schluessel(p_l)) with ordinality u(k, o) order by u.o loop
    v_x := v_b#>array['pflicht_je_schulart', v_k];
    if jsonb_typeof(v_x) = 'array' then return array(select jsonb_array_elements_text(v_x)); end if;
  end loop;
  v_x := v_b->'lernziele_pflicht';
  if jsonb_typeof(v_x) = 'array' then return array(select jsonb_array_elements_text(v_x)); end if;
  return null;
end $$;

-- 1) Etappen der Regel: Pflichtliste einmal statt je Etappe
create or replace function schule.stufe_etappen(p_l bigint, p_e bigint)
 returns text[] language plpgsql stable set search_path to ''
as $$
declare v_kat text[]; v_pf text[];
begin
  v_kat := array(select x->>'lernziel' from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) x where e.id = p_e);
  v_pf := schule.pflicht_lernziele(p_l, p_e);
  if v_pf is null then return v_kat; end if;                                          -- keine Liste festgelegt: alle Etappen
  return array(select x from unnest(v_kat) x where x = any(v_pf));                    -- A2: ausdrücklich leer → keine (Kür zählt nicht)
end $$;

-- 1) thema_stufe: Etappen der Regel einmal je Aufruf statt je Karte (Anker-Änderung, sonst unverändert)
do $$
declare d text;
  a1 text := $a$v_implan boolean; v_stufe text;$a$;
  n1 text := $a$v_implan boolean; v_stufe text; v_et text[]; -- LZ-S$a$;
  a2 text := $a$v_n := cardinality(schule.stufe_etappen(p_l, v_e)); -- TL-S 6: Etappen der Regel$a$;
  n2 text := $a$v_et := schule.stufe_etappen(p_l, v_e); v_n := cardinality(v_et); -- TL-S 6: Etappen der Regel (LZ-S: einmal)$a$;
  a3 text := $a$and k.lernziel = any(schule.stufe_etappen(p_l, v_e)); -- TL-S 6$a$;
  n3 text := $a$and k.lernziel = any(v_et); -- TL-S 6 (LZ-S)$a$;
begin
  d := pg_get_functiondef('schule.thema_stufe(bigint, bigint)'::regprocedure);
  if position('-- LZ-S' in d) > 0 then raise notice 'thema_stufe schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a1, ''))) / length(a1) <> 1 or (length(d) - length(replace(d, a2, ''))) / length(a2) <> 1
     or (length(d) - length(replace(d, a3, ''))) / length(a3) <> 1 then raise exception 'LZ-S: Anker in thema_stufe nicht genau einmal gefunden'; end if;
  execute replace(replace(replace(d, a1, n1), a2, n2), a3, n3);
end $$;

-- 3) lehrplan_matrix: „pflicht“ je Thema mit Zuordnungen des Themas zuerst; 1) thema_stufe je Kind und Thema einmal (Anker-Änderungen)
do $$
declare d text;
  a text := $a$(select coalesce(jsonb_agg(distinct ql.schulart), '[]'::jsonb) from schule.zuordnung z join schule.eintrag e on e.id = z.eintrag_id$a$;
  n text := $a$(select coalesce(jsonb_agg(distinct ql.schulart), '[]'::jsonb) from (select z0.eintrag_id, z0.thema_id from schule.zuordnung z0 where z0.thema_id = t.id offset 0) z /* LZ-S */ join schule.eintrag e on e.id = z.eintrag_id$a$;
  -- thema_stufe je Kind und Thema genau einmal (ohne „offset 0“ zieht der Planer die Unterabfrage hoch und ruft thema_stufe je Verweis auf s.st erneut)
  a2 text := $a$cross join lateral (select schule.thema_stufe(l.id, t.id) st) s$a$;
  n2 text := $a$cross join lateral (select schule.thema_stufe(l.id, t.id) st offset 0) s /* LZ-S: einmal */$a$;
begin
  d := pg_get_functiondef('schule.lehrplan_matrix(bigint[], boolean)'::regprocedure);
  if position('/* LZ-S */' in d) > 0 then raise notice 'lehrplan_matrix schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 or (length(d) - length(replace(d, a2, ''))) / length(a2) <> 1 then
    raise exception 'LZ-S: Anker in lehrplan_matrix nicht genau einmal gefunden'; end if;
  execute replace(replace(d, a, n), a2, n2);
end $$;

-- 2) Klassen je Thema für alle Themen in einem Durchgang (gleicher Aufbau wie thema_klassen, zusätzlich nach Thema gruppiert)
create or replace function schule.thema_klassen_alle(p_schulart text default null, p_zweig text default null, p_kurz boolean default false)
 returns table (thema_id bigint, j jsonb) language sql stable set search_path to ''
as $$
  select s.thema_id, coalesce(jsonb_object_agg(s.schulart, s.j), '{}'::jsonb) from (
    select z.thema_id, z.schulart, jsonb_object_agg(z.zweig, z.j) j from (
      select k.thema_id, k.schulart, k.zweig, jsonb_agg(jsonb_strip_nulls(jsonb_build_object('klasse', k.klasse, 'rolle', k.rolle,
               'route_start', case when k.klasse = k.klasse_route then true end,
               'etappen', to_jsonb(k.etappen),
               'ganzes_thema', case when k.ganzes_thema then true end,
               'etappen_unbekannt', case when k.etappen_unbekannt then true end,
               'rolle_lehrplan', case when not p_kurz then to_jsonb(k.rolle_lehrplan) end,
               'lernbereiche', case when not p_kurz then k.lernbereiche end,
               'stunden', case when not p_kurz then (select sum((l->>'stunden')::numeric) from jsonb_array_elements(k.lernbereiche) l) end,
               'nur_klasse_fest', case when not p_kurz and k.nur_klasse_fest then true end)) order by k.klasse) j
        from schule.thema_lage_klasse k
       where (p_schulart is null or k.schulart = p_schulart) and (p_zweig is null or k.zweig = p_zweig)
       group by 1, 2, 3) z group by 1, 2) s group by 1;
$$;
revoke all on function schule.thema_klassen_alle(text, text, boolean) from public, anon, authenticated;

-- 2) lehrplan_matrix_lk: Klassen je Thema aus einem Durchgang statt thema_klassen je Thema; sonst unverändert
create or replace function schule.lehrplan_matrix_lk(p_r jsonb, p_kind bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $$
declare v_sa text; v_zw text;
begin
  if p_kind is not null then   -- Kindsicht: nur Schulart und Zweig des Kindes, kurz
    select coalesce(l.schulart, 'gym_by'), schule.kind_zweig(coalesce(l.schulart, 'gym_by'), l.zweig) into v_sa, v_zw from schule.lernender l where l.id = p_kind;
    return jsonb_set(p_r, '{themen}', coalesce((select jsonb_agg(t.j || schule.thema_teil_json((t.j->>'thema_id')::bigint) || jsonb_build_object('klassen_kind',
             coalesce(coalesce(tk.j, '{}'::jsonb)->v_sa->v_zw, '[]'::jsonb)) order by t.o)
             from jsonb_array_elements(p_r->'themen') with ordinality t(j, o)
             left join schule.thema_klassen_alle(v_sa, v_zw, true) tk on tk.thema_id = (t.j->>'thema_id')::bigint), '[]'::jsonb))   -- LZ-S
           || jsonb_build_object('zweig', v_zw)
           || jsonb_build_object('verbindungen_kind', (select coalesce(jsonb_agg(jsonb_build_array(o.thema_id, o.braucht_id, case o.art when 'hart' then 'h' else 'e' end)
                                                     order by o.thema_id, o.braucht_id), '[]'::jsonb) from schule.voraussetzung_schulart o where o.gruppe = case when v_sa = 'gym_by' then 'gym_by' else v_zw end));   -- TL-S
  end if;
  return jsonb_set(jsonb_set(p_r, '{themen}', coalesce((select jsonb_agg(t.j || schule.thema_teil_json((t.j->>'thema_id')::bigint) || jsonb_build_object('klassen', coalesce(tk.j, '{}'::jsonb)) order by t.o)
           from jsonb_array_elements(p_r->'themen') with ordinality t(j, o)
           left join schule.thema_klassen_alle(null, null, false) tk on tk.thema_id = (t.j->>'thema_id')::bigint), '[]'::jsonb)),   -- LZ-S
         '{kinder}', coalesce((select jsonb_agg(k.j || jsonb_build_object('zweig', schule.kind_zweig(coalesce(l.schulart, 'gym_by'), l.zweig)) order by k.o)
           from jsonb_array_elements(p_r->'kinder') with ordinality k(j, o) left join schule.lernender l on l.id = (k.j->>'id')::bigint), '[]'::jsonb))
         || jsonb_build_object('lehrplan_zuordnung', schule.lehrplan_zuordnung_json())
         || jsonb_build_object('verbindungen_schulart', (select coalesce(jsonb_agg(jsonb_build_array(o.thema_id, o.braucht_id, o.gruppe, case o.art when 'hart' then 'h' else 'e' end)
                                                         order by o.thema_id, o.braucht_id, o.gruppe), '[]'::jsonb) from schule.voraussetzung_schulart o));   -- TL-S
end $$;
