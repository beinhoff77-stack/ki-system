-- Rauchtest NB-S (Nachbessern: wieder offene Etappe zuerst). Alles in einer Transaktion mit Rollback; Änderungen nur am Testkind.
-- Voraussetzung: LZ-S eingespielt. Spielt ZP-S und NB-S selbst ein (beide wiederholbar). Ausgabe nur Zahlen.
-- api-Antworten (Konto, Übersicht) als pg_temp-Kopien ohne Schlüssel (nur die Zugriffsprüfung ersetzt, jeder Anker geprüft).
-- Aufruf aus dem Repo-Wurzelverzeichnis: psql -v ON_ERROR_STOP=1 -f supabase/tests/nb_s_rauchtest.sql
begin;

create function pg_temp.nb_h(p_ohne bigint) returns text language sql as $$
  select md5(coalesce((select string_agg(k::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel) from schule.karte_stand k where k.lernender_id is distinct from p_ohne), '')
          || coalesce((select string_agg(s::text, '|' order by s.lernender_id, s.einheit_id, s.lernziel) from schule.lernziel_stand s where s.lernender_id is distinct from p_ohne), '')
          || coalesce((select string_agg(s::text, '|' order by s.id) from schule.sterne s where s.lernender_id is distinct from p_ohne), '')
          || coalesce((select string_agg(f::text, '|' order by f.lernender_id, f.einheit_id) from schule.flug_erstabschluss f where f.lernender_id is distinct from p_ohne), '')
          || coalesce((select string_agg(r::text, '|' order by r.id) from schule.route r where r.lernender_id is distinct from p_ohne), ''));
$$;
-- Wieder offene Etappen je Kind, direkt aus karte_stand (Vergleich für die Liste)
create function pg_temp.nb_roh(p_l bigint) returns bigint language sql as $$
  select count(*) from schule.karte_stand k join schule.einheit e on e.id = k.einheit_id and e.id = schule.thema_einheit(e.thema_id)
   where k.lernender_id = p_l and not k.sitzt and k.sitzt_am is not null
     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) x where x->>'lernziel' = k.lernziel);
$$;
create temp table nb_rt_vorher on commit drop as
  select pg_temp.nb_h(null) h, (select jsonb_object_agg(l.id, pg_temp.nb_roh(l.id)) from schule.lernender l) roh;

-- Test 0 (lesend, vorher): wie viele Etappen sind heute wieder offen?
do $$ begin
  raise notice 'Test 0: wieder offene Etappen je Kind (lesend): %', (select roh from nb_rt_vorher);
end $$;

\ir ../migrations/20261126_zp_s_zusatz_plan.sql
\ir ../migrations/20261127_nb_s_nachbessern.sql
\ir ../migrations/20261127_nb_s_nachbessern.sql

create function pg_temp.nb_ersetzen(d text, a text, n text) returns text language plpgsql as $$
begin
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'NB-Test: Anker nicht genau einmal: %', left(a, 60); end if;
  return replace(d, a, n);
end $$;
do $$
declare d text;
begin
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  d := pg_temp.nb_ersetzen(d, 'FUNCTION api.schule_uebersicht(', 'FUNCTION pg_temp.nb_uebersicht(');
  d := pg_temp.nb_ersetzen(d, 'v_tn := schule.wer_tn(p_schluessel);', 'v_tn := null;');
  d := pg_temp.nb_ersetzen(d, 'v_leiter := schule.ist_leiter(p_schluessel);', 'v_leiter := true;');
  d := pg_temp.nb_ersetzen(d, 'schule.sieht(p_schluessel, l.id)', 'true');
  execute d;
  d := pg_get_functiondef('api.schule_konto(text, jsonb)'::regprocedure);
  d := pg_temp.nb_ersetzen(d, 'FUNCTION api.schule_konto(', 'FUNCTION pg_temp.nb_konto(');
  d := pg_temp.nb_ersetzen(d, 'perform schule.zugriff(p_schluessel, v_l);', '');
  execute d;
end $$;
create function pg_temp.nb_ue(p_l bigint) returns jsonb language sql as $$
  select k->'nachbessern' from jsonb_array_elements(pg_temp.nb_uebersicht('', null)->'lernende') k where (k->>'id')::bigint = p_l;
$$;

-- Test 1: Einspielen ändert nichts; Liste je Kind = wieder offene Etappen; Konto und Übersicht liefern dieselbe Liste
do $$
declare v_l record; v_nb jsonb;
begin
  if pg_temp.nb_h(null) is distinct from (select h from nb_rt_vorher) then raise exception 'FEHLER 1: Einspielen hat Lernstand/Plan/Sterne/Stempel verändert'; end if;
  for v_l in select id from schule.lernender where aktiv loop
    v_nb := schule.nachbessern(v_l.id);
    if jsonb_array_length(v_nb) <> pg_temp.nb_roh(v_l.id) then raise exception 'FEHLER 1: Liste Kind % hat % statt % Einträge', v_l.id, jsonb_array_length(v_nb), pg_temp.nb_roh(v_l.id); end if;
    if pg_temp.nb_konto('', jsonb_build_object('lernender_id', v_l.id))->'nachbessern' is distinct from v_nb then raise exception 'FEHLER 1: schule_konto Kind % weicht ab', v_l.id; end if;
    if pg_temp.nb_ue(v_l.id) is distinct from v_nb then raise exception 'FEHLER 1: schule_uebersicht Kind % weicht ab', v_l.id; end if;
    if jsonb_array_length(v_nb) > 0 and (schule.reise_karte(v_l.id)->'naechster_start'->>'grund') is distinct from 'nachbessern'
       and exists (select 1 from schule.reise_land rl where rl.art = 'flug' and rl.thema_id = (v_nb->0->>'thema_id')::bigint) then
      raise exception 'FEHLER 1: Kind % hat Nachbessern, nächster Start nicht', v_l.id; end if;
  end loop;
  raise notice 'Test 1: Einspielen ohne Änderung; Liste = wieder offene Etappen; Konto/Übersicht/Reisekarte gleich: OK';
end $$;

-- Aufbau am Testkind: eine Etappe eines Flugs auf der Reisekarte, Ort fertig, Etappe gelandet und fällig; mind. 3 Übungsaufgaben
create temp table nb_t on commit drop as
  select l.id l, x.e, x.thema, x.block, x.lz, (select min(a.id) from schule.aufgabe a where a.einheit_id = x.e and a.variante_gruppe = x.lz and a.pool = 'uebung' and a.freigegeben) aufg
    from (select id from schule.lernender where ist_test and aktiv order by id limit 1) l
    cross join lateral (
      select e.id e, e.thema_id thema, e.block_id block, et.x->>'lernziel' lz
        from schule.einheit e cross join lateral jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality et(x, o)
       where e.id = schule.thema_einheit(e.thema_id) and e.block_id is not null and e.status in ('geprueft', 'freigegeben')
         and exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.variante_gruppe = et.x->>'lernziel' and a.pool = 'uebung' and a.freigegeben)
         and exists (select 1 from schule.reise_land rl where rl.art = 'flug' and rl.thema_id = e.thema_id)
         and exists (select 1 from schule.reise_stadt s where s.art = 'etappe' and s.thema_id = e.thema_id and s.lernziel = et.x->>'lernziel')
         and not exists (select 1 from schule.karte_stand k where k.lernender_id = l.id and k.einheit_id = e.id)
         and not exists (select 1 from schule.route r where r.lernender_id = l.id and r.block_id = e.block_id)
         and not exists (select 1 from schule.thema t where t.id = e.thema_id and schule.kind_gruppe(l.id) = any(coalesce(t.zusatz, '{}')))
       order by e.id, et.o limit 1) x;
do $$
declare t record; v_n int;
begin
  select * into t from nb_t;
  if t.l is null or t.e is null then raise exception 'NB-Test: kein Testkind oder keine passende Einheit'; end if;
  -- mind. 3 Übungsaufgaben (Kopien der vorhandenen), damit die Folge 3 beträgt
  select count(*) into v_n from schule.aufgabe a where a.einheit_id = t.e and a.variante_gruppe = t.lz and a.pool = 'uebung' and a.freigegeben;
  while v_n < 3 loop
    execute format('insert into schule.aufgabe(%s) select %s from schule.aufgabe where id = $1',
      (select string_agg(quote_ident(attname), ', ' order by attnum) from pg_attribute where attrelid = 'schule.aufgabe'::regclass and attnum > 0 and not attisdropped and attgenerated = ''),
      (select string_agg(case when attname = 'id' then '(select max(id) + 1 from schule.aufgabe)' else quote_ident(attname) end, ', ' order by attnum)
         from pg_attribute where attrelid = 'schule.aufgabe'::regclass and attnum > 0 and not attisdropped and attgenerated = '')) using t.aufg;
    v_n := v_n + 1;
  end loop;
  insert into schule.route(id, lernender_id, block_id, position, art, status, geaendert_von)
    values ((select coalesce(max(id), 0) + 1 from schule.route), t.l, t.block, (select coalesce(max(position), 0) + 1 from schule.route where lernender_id = t.l), 'normal', 'fertig', 'eltern:Test');
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (t.l, t.e, t.lz);
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '20 days', wdh_stufe = 2, faellig_am = now() - interval '1 day', wdh_ab = null, wdh_lerntage = null,
         wdh_fehler = 0, eigene_loesungen = schule.karte_ziel(t.e, t.lz), folge = 3, fehler_folge = 0, schwer_ok = true, richtig = 6, falsch = 0,
         typen = array(select 'typ' || g from generate_series(1, greatest(schule.karte_typen_noetig(t.e, t.lz), 1)) g)
   where lernender_id = t.l and einheit_id = t.e and lernziel = t.lz;
end $$;
create temp table nb_rt_aufbau on commit drop as select pg_temp.nb_h((select l from nb_t)) h,
  (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = (select l from nb_t)) sterne_t,
  (select count(*) from schule.flug_erstabschluss where lernender_id = (select l from nb_t)) stempel_t,
  (select md5(string_agg((r.id, r.block_id, r.position, r.art, r.status, r.ausgelassen, r.kann_schon_themen, r.kann_wdh_themen)::text, '|' order by r.id))
     from schule.route r where r.lernender_id = (select l from nb_t)) route_t;

create function pg_temp.nb_eintrag() returns jsonb language sql as $$
  select x from nb_t t, jsonb_array_elements(schule.nachbessern(t.l)) x where (x->>'einheit_id')::bigint = t.e and x->>'lernziel' = t.lz;
$$;
create function pg_temp.nb_buche(p_richtig boolean, p_hilfe int) returns void language sql as $$
  select schule.karte_buchen(t.l, t.aufg, p_richtig, p_hilfe::smallint, now()) from nb_t t;
$$;
create function pg_temp.nb_karte() returns schule.karte_stand language sql as $$
  select k from schule.karte_stand k, nb_t t where k.lernender_id = t.l and k.einheit_id = t.e and k.lernziel = t.lz;
$$;

-- Test 2: zwei Fehler in Folge in der fälligen Wiederholung → Eintrag (Ort fertig); Konto, Übersicht, Reisekarte
do $$
declare t record; v jsonb; v_s jsonb; v_rk jsonb;
begin
  select * into t from nb_t;
  if not schule.karte_faellig(pg_temp.nb_karte()) then raise exception 'NB-Test: Aufbau – Etappe nicht fällig'; end if;
  perform pg_temp.nb_buche(false, 0);
  if pg_temp.nb_eintrag() is not null then raise exception 'FEHLER 2: schon nach einem Fehler in der Liste'; end if;
  if not (pg_temp.nb_karte()).sitzt then raise exception 'FEHLER 2: nach einem Fehler nicht mehr gelandet'; end if;
  perform pg_temp.nb_buche(false, 0);
  v := pg_temp.nb_eintrag();
  if v is null then raise exception 'FEHLER 2: nach zwei Fehlern kein Eintrag'; end if;
  if (v->>'thema_id')::bigint <> t.thema or (v->>'block_id')::bigint <> t.block or v->>'etappe' is null or v->>'titel' is null or (v->>'etappe_nr')::int < 1
     or (v->>'folge')::int <> 0 or (v->>'folge_noetig')::int <> 3 or (v->>'noch')::int <> 3 or not (v->>'ort_fertig')::boolean
     or (v->>'wieder_offen_seit')::timestamptz <> now() or v->>'gesetzt' is not null then
    raise exception 'FEHLER 2: Felder falsch: %', v - 'titel' - 'etappe' - 'stadt'; end if;
  if pg_temp.nb_konto('', jsonb_build_object('lernender_id', t.l))->'nachbessern' is distinct from schule.nachbessern(t.l) then raise exception 'FEHLER 2: schule_konto ohne Eintrag'; end if;
  if pg_temp.nb_ue(t.l) is distinct from schule.nachbessern(t.l) then raise exception 'FEHLER 2: schule_uebersicht ohne Eintrag'; end if;
  v_s := schule.thema_stufe(t.l, t.thema);
  v_rk := schule.reise_karte(t.l);
  if (v_rk->'naechster_start'->>'grund') <> 'nachbessern' or (v_rk->'naechster_start'->>'thema_id')::bigint <> (schule.nachbessern(t.l)->0->>'thema_id')::bigint
     or (v_rk->'naechster_start'->'stadt'->>'lernziel') <> (schule.nachbessern(t.l)->0->>'lernziel') or v_rk->'nachbessern' is distinct from schule.nachbessern(t.l) then
    raise exception 'FEHLER 2: nächster Start nicht „nachbessern“: %', v_rk->'naechster_start'; end if;
  if not exists (select 1 from jsonb_array_elements(v_rk->'kontinente') k, jsonb_array_elements(k->'fluege') f, jsonb_array_elements(f->'staedte') s
                  where (f->>'thema_id')::bigint = t.thema and s->>'lernziel' = t.lz and s->>'stand' = 'wieder_offen') then
    raise exception 'FEHLER 2: Stadt nicht als wieder offen markiert'; end if;
  raise notice 'Test 2: zwei Fehler → Eintrag (Folge 0 von 3, Ort fertig), Stufe %, wieder offen %, nächster Start nachbessern: OK', v_s->>'stufe', v_s->>'wieder_offen';
end $$;

-- Test 3: richtig mit Tipp zählt nicht; drei eigene Lösungen in Folge → Eintrag weg, Wiederholung beginnt neu
do $$
declare t record; v jsonb; k schule.karte_stand;
begin
  select * into t from nb_t;
  perform pg_temp.nb_buche(true, 1);
  v := pg_temp.nb_eintrag();
  if v is null or (v->>'folge')::int <> 0 then raise exception 'FEHLER 3: richtig mit Tipp hat gezählt: %', v->'folge'; end if;
  perform pg_temp.nb_buche(true, 0);
  if (pg_temp.nb_eintrag()->>'folge')::int <> 1 then raise exception 'FEHLER 3: 1. eigene Lösung nicht gezählt'; end if;
  perform pg_temp.nb_buche(false, 0);
  if (pg_temp.nb_eintrag()->>'folge')::int <> 0 then raise exception 'FEHLER 3: Fehler setzt Folge nicht zurück'; end if;
  perform pg_temp.nb_buche(true, 0); perform pg_temp.nb_buche(true, 0);
  v := pg_temp.nb_eintrag();
  if v is null or (v->>'folge')::int <> 2 or (v->>'noch')::int <> 1 then raise exception 'FEHLER 3: Folge 2 von 3 erwartet: %', v->'folge'; end if;
  perform pg_temp.nb_buche(true, 0);
  if pg_temp.nb_eintrag() is not null then raise exception 'FEHLER 3: nach drei eigenen Lösungen in Folge noch in der Liste'; end if;
  k := pg_temp.nb_karte();
  if not k.sitzt or k.wdh_stufe <> 0 or k.faellig_am is distinct from now() + interval '1 day' or k.sitzt_am <> now() then
    raise exception 'FEHLER 3: Wiederholung beginnt nicht neu (sitzt %, Stufe %, fällig %)', k.sitzt, k.wdh_stufe, k.faellig_am; end if;
  if (schule.reise_karte(t.l)->'naechster_start'->>'grund') = 'nachbessern' and jsonb_array_length(schule.nachbessern(t.l)) = 0 then
    raise exception 'FEHLER 3: nächster Start bleibt nachbessern'; end if;
  raise notice 'Test 3: Tipp zählt nicht, Fehler setzt zurück, 3 eigene in Folge → weg, Wdh-Stufe 0, fällig in 1 Tag: OK';
end $$;

-- Test 4: „Kann er“-Setzung mit Rückfall: Eintrag mit gesetzt 'komplett', Stufe bleibt ◉ mit Hinweis Rückfall, nächster Start nachbessern
do $$
declare t record; v jsonb; v_s jsonb;
begin
  select * into t from nb_t;
  update schule.route set kann_schon = true where lernender_id = t.l and block_id = t.block;
  update schule.karte_stand set gesetzt_am = now() - interval '5 days', faellig_am = now() - interval '1 day', wdh_ab = null, wdh_lerntage = null, wdh_fehler = 0, wdh_stufe = 3
   where lernender_id = t.l and einheit_id = t.e and lernziel = t.lz;
  perform pg_temp.nb_buche(false, 0); perform pg_temp.nb_buche(false, 0);
  v := pg_temp.nb_eintrag(); v_s := schule.thema_stufe(t.l, t.thema);
  if v is null or v->>'gesetzt' <> 'komplett' then raise exception 'FEHLER 4: kein Eintrag bei Setzung mit Rückfall: %', v; end if;
  if v_s->>'stufe' <> 'komplett' or v_s->>'hinweis' <> 'rueckfall' then raise exception 'FEHLER 4: Stufe %/% statt komplett/rueckfall', v_s->>'stufe', v_s->>'hinweis'; end if;
  if (schule.reise_karte(t.l)->'naechster_start'->>'grund') <> 'nachbessern' then raise exception 'FEHLER 4: nächster Start nicht nachbessern'; end if;
  perform pg_temp.nb_buche(true, 0); perform pg_temp.nb_buche(true, 0); perform pg_temp.nb_buche(true, 0);
  if pg_temp.nb_eintrag() is not null then raise exception 'FEHLER 4: nach drei eigenen Lösungen noch in der Liste'; end if;
  raise notice 'Test 4: Setzung „kann er komplett“ mit Rückfall → Eintrag, ◉ mit Hinweis Rückfall, nach 3 in Folge weg: OK';
end $$;

-- Test 5: Fahrplan, Stempel, andere Kinder unverändert; Sterne des Testkinds gemeldet
do $$
declare t record; v_st bigint;
begin
  select * into t from nb_t;
  if pg_temp.nb_h(t.l) is distinct from (select h from nb_rt_aufbau) then raise exception 'FEHLER 5: Daten anderer Kinder verändert'; end if;
  if (select md5(string_agg((r.id, r.block_id, r.position, r.art, r.status, r.ausgelassen, r.kann_schon_themen, r.kann_wdh_themen)::text, '|' order by r.id))
        from schule.route r where r.lernender_id = t.l) is distinct from (select route_t from nb_rt_aufbau) then raise exception 'FEHLER 5: Fahrplan des Testkinds verändert'; end if;
  if (select count(*) from schule.flug_erstabschluss where lernender_id = t.l) <> (select stempel_t from nb_rt_aufbau) then raise exception 'FEHLER 5: Stempel verändert'; end if;
  select coalesce(sum(menge), 0) into v_st from schule.sterne where lernender_id = t.l;
  -- erlaubt: nur der Landungs-Bonus dieser Etappe (bisherige Regel, je Etappe genau einmal – im Aufbau gab es noch keine Landung)
  if exists (select 1 from schule.sterne s where s.lernender_id = t.l and not (s.grund = 'landung' and s.bezug = 'landung:' || t.e || ':' || t.lz))
     or (select count(*) from schule.sterne s where s.lernender_id = t.l and s.grund = 'landung') > 1 then
    raise exception 'FEHLER 5: unerwartete Sterne: %', (select string_agg(s.grund || ' ' || s.menge, ', ') from schule.sterne s where s.lernender_id = t.l); end if;
  raise notice 'Test 5: Fahrplan (außer bewusster Setzung in Test 4) und Stempel unverändert, andere Kinder unverändert: OK; Sterne Testkind % → % (nur Landungs-Bonus der Etappe, je Etappe einmal – bisherige Regel)',
    (select sterne_t from nb_rt_aufbau), v_st;
end $$;

rollback;
