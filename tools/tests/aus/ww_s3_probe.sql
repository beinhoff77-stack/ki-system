-- WW-S3 Einspiel-Paket (erzeugt von tools/tests/wackelt_einspielen.py --ww3 --probe). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);
do $p$ begin
  if to_regclass('schule.fehler_erledigt') is null or to_regprocedure('schule.ww_versuche(bigint, jsonb)') is null
     or to_regprocedure('schule.ww_fehlerart(schule.versuch, schule.aufgabe)') is null or to_regprocedure('schule.ww_von(text)') is null
     or to_regprocedure('schule.wackelt_analyse(bigint, integer, boolean)') is null or to_regprocedure('schule.fehler_abhaken(bigint, jsonb, boolean, text)') is null
     or to_regprocedure('api.schule_fehler_abhaken(text, jsonb)') is null or to_regprocedure('api.schule_wackelt_analyse(text, jsonb)') is null then
    raise exception 'WW-S3 ABBRUCH, Vorbedingung: WW-S2 ist nicht eingespielt (erst ww_s_einspielen.sql) – nichts geändert';
  end if;
end $p$;
create temp table ww3_mig on commit drop as select $ww3mig$-- WW-S3 („Was wackelt“, Folgemigration zu WW-S2, das seit 27.11.2026 eingespielt ist; die WW-S2-Datei bleibt unverändert).
-- Anlass: Gegenprüfung des Clients „Besprochen je Thema“ (Auflagen aus Werkstatt 1162). Plan und Antwortformen: inhalte/plan/wackelt-server.md (Abschnitt WW-S3).
-- Einspielen NUR über tools/tests/wackelt_einspielen.py --ww3 (eine Transaktion, prüft sich selbst; --ww3 --probe rollt alles zurück).
--
-- WAS (nur create or replace der WW-Funktionen und eine neue Funktion; keine Tabelle, keine Spalte, kein Index, kein Trigger):
-- 1. schule.wackelt_analyse: Vergleiche über thema_id und lernziel nullsicher (is not distinct from). Vorher meldete auswertung.themen bei Einheiten
--    ohne Thema offen = 0 (NULL = NULL ist nie wahr), und lagen diese Fehler jenseits der 300 neuesten, fehlte das Thema in der Zählung des Clients.
-- 2. schule.wackelt_analyse: je besprochenem Eintrag erledigt.id (= schule.fehler_erledigt.id, die Markierungs-ID) und erledigt.tag (Kalendertag der
--    Markierung in der Zeitzone des Kindes).
-- 3. Neue Funktion schule.fehler_zurueckholen(kind, markierung_ids, von): nimmt in EINER Anweisung genau die genannten, noch gültigen Markierungen dieses
--    Kindes zurück; überholte (schon zurückgeholt, ggf. inzwischen neu markiert), unbekannte und fremde (anderes Kind) werden übersprungen und gemeldet.
--    Vorher nahm das Zurückholen über versuch_ids JEDE gültige Markierung des Versuchs zurück – auch eine, die nach dem Laden neu gesetzt wurde.
-- 4. schule.fehler_abhaken: nur noch Markieren; Antwort zusätzlich mit stand, geaendert_ids (versuch_ids, die dieser Aufruf wirklich markiert hat)
--    und markierung_ids (IDs der neu angelegten Zeilen). Der alte Rückholweg über versuch_ids ist ENTFERNT (Auflagen aus Werkstatt 1165: er konnte
--    nach „überholt“ die neue Markierung zurücknehmen); mit p_zurueck = true bricht die Funktion ab. Zurückholen gibt es nur über markierung_ids.
-- 5. schule.wackelt_analyse: auswertung.themen[].besprochen {zuletzt, zuletzt_tag, tage, fehler, neu_seit} – ohne 200er-Grenze, nur gültige
--    Markierungen, nur wenn das Thema je besprochen wurde; nullsicher für „ohne Thema“. zuletzt_tag und tage in der Zeitzone des Kindes
--    (wie erledigt.tag); fehler = Zahl der gültig markierten Fehler des Themas insgesamt.
-- 6. Feste Typen: mit_tipp immer Boolean; danach_richtig nur noch true oder fehlt (die Zeitpunkte stehen in danach_richtig_am); Analyse und
--    Abhaken melden stand: 3 (fehlt das Feld, läuft am Server noch WW-S2).
-- 7. api.schule_fehler_abhaken: Markieren {versuch_ids} oder Zurückholen {zurueck: true, markierung_ids}; jede Rücknahme ohne markierung_ids wird
--    abgewiesen („Zurückholen nur mit markierung_ids“), ebenso markierung_ids ohne zurueck und beide Listen zusammen. Rechteprüfung unverändert:
--    wer_tn -> ist_leiter -> zugriff -> Kind aktiv.
--
-- WAS NICHT: keine Änderung an bestehenden Tabellen, Funktionen oder Triggern außerhalb von WW-S2/WW-S3 (auch nicht an ww_fehlerart, ww_von,
-- ww_versuche, api.schule_wackelt_analyse); schreibt ausschließlich schule.fehler_erledigt (und Hilfstabellen der eigenen Sitzung); keine
-- Fremdschlüssel oder Trigger an schule.versuch; kein UPDATE/DELETE von Bestandsdaten, kein DROP. Wiederholbar: ein zweiter Lauf ändert nichts.

select set_config('lock_timeout', '3s', true);

do $$ begin
  if to_regclass('schule.fehler_erledigt') is null or to_regprocedure('schule.ww_versuche(bigint, jsonb)') is null
     or to_regprocedure('schule.ww_fehlerart(schule.versuch, schule.aufgabe)') is null or to_regprocedure('schule.ww_von(text)') is null
     or to_regprocedure('schule.wackelt_analyse(bigint, integer, boolean)') is null or to_regprocedure('schule.fehler_abhaken(bigint, jsonb, boolean, text)') is null
     or to_regprocedure('api.schule_fehler_abhaken(text, jsonb)') is null or to_regprocedure('api.schule_wackelt_analyse(text, jsonb)') is null
  then raise exception 'WW-S3: Voraussetzung fehlt – erst WW-S2 (20261205_ww_s_wackelt.sql) einspielen'; end if;
end $$;

-- 1., 2., 5., 6. Analyse
create or replace function schule.wackelt_analyse(p_l bigint, p_tage integer default 14, p_mit_erledigt boolean default false)
 returns jsonb language plpgsql set search_path to ''   -- volatil nur wegen der Hilfstabellen dieser Sitzung (pg_temp, on commit drop); liest sonst nur
as $function$
declare v_seit timestamptz := case when coalesce(p_tage, 0) <= 0 then null else now() - make_interval(days => p_tage) end;
  v_tz text := coalesce((select l.zeitzone from schule.lernender l where l.id = p_l), 'Europe/Berlin'); r jsonb;
begin
  -- eigene Namen (ww3_*): eine Hilfstabelle der WW-S2-Fassung aus derselben Transaktion hätte andere Spalten
  create temp table if not exists ww3_v (ver schule.versuch, auf schule.aufgabe, id bigint, am timestamptz, richtig boolean, hilfe smallint, anlauf smallint,
    aufgabe_id bigint, einheit_id bigint, lz text, thema_id bigint) on commit drop;
  truncate ww3_v;   -- nur die Hilfstabelle dieser Sitzung
  insert into ww3_v select x, a, x.id, x.am, x.richtig, x.hilfe, x.anlauf, x.aufgabe_id, a.einheit_id, a.variante_gruppe, e.thema_id
    from schule.versuch x join schule.aufgabe a on a.id = x.aufgabe_id join schule.einheit e on e.id = a.einheit_id where x.lernender_id = p_l;
  create temp table if not exists ww3_f (id bigint, am timestamptz, aufgabe_id bigint, einheit_id bigint, lz text, thema_id bigint, im_zeitraum boolean,
    abgehakt_id bigint, abgehakt_am timestamptz, aufgabe_richtig_am timestamptz, lk_richtig_am timestamptz, erst_antwort jsonb, art jsonb, eintrag jsonb) on commit drop;
  truncate ww3_f;
  insert into ww3_f
  select f.id, f.am, f.aufgabe_id, f.einheit_id, f.lz, f.thema_id, v_seit is null or f.am > v_seit,
         fe.id, fe.am,
         (select min(y.am) from ww3_v y where y.aufgabe_id = f.aufgabe_id and y.richtig and (y.am, y.id) > (f.am, f.id)),
         (select min(y.am) from ww3_v y where y.einheit_id = f.einheit_id and y.lz is not distinct from f.lz and y.richtig and coalesce(y.hilfe, 0) = 0
                                          and (y.am, y.id) > (f.am, f.id)),
         case when f.anlauf = 2 then (select (y.ver).antwort from ww3_v y where y.aufgabe_id = f.aufgabe_id and y.anlauf = 1 and not y.richtig and y.am <= f.am
                                       order by y.am desc, y.id desc limit 1) end,
         schule.ww_fehlerart(f.ver, f.auf), null
    from ww3_v f
    left join schule.fehler_erledigt fe on fe.versuch_id = f.id and fe.lernender_id = p_l and fe.zurueckgenommen_am is null
   where not f.richtig and schule.fehler_endgueltig_am(f.ver) is not null;
  update ww3_f w set eintrag = jsonb_strip_nulls(jsonb_build_object(
      'versuch_id', w.id, 'am', w.am, 'tag', (w.am at time zone v_tz)::date, 'thema_id', w.thema_id,
      'thema', (select coalesce(t.unterthema, t.schluessel) from schule.thema t where t.id = w.thema_id),
      'einheit_id', w.einheit_id, 'lernziel', w.lz,
      'lernkarte', (select q->>'titel' from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q where e.id = w.einheit_id and q->>'lernziel' = w.lz limit 1),
      'aufgabe', (select jsonb_strip_nulls(jsonb_build_object('id', (v.auf).id, 'antworttyp', (v.auf).antworttyp, 'form', (v.auf).form, 'typ', (v.auf).typ,
                    'stufe', (v.auf).stufe, 'frage', (v.auf).frage, 'antworten', (v.auf).antworten, 'loesung', schule.loesung_sicht(v.auf), 'loesungsweg', (v.auf).loesungsweg))
                    from ww3_v v where v.id = w.id),
      'antwort', (select (v.ver).antwort from ww3_v v where v.id = w.id), 'erst_antwort', w.erst_antwort,
      'anlauf', (select v.anlauf from ww3_v v where v.id = w.id), 'mit_tipp', coalesce((select coalesce(v.hilfe, 0) > 0 from ww3_v v where v.id = w.id), false),
      'fehlerart', nullif(w.art, '{}'::jsonb),
      'danach_richtig', case when w.aufgabe_richtig_am is not null or w.lk_richtig_am is not null then true end,
      'danach_richtig_am', nullif(jsonb_strip_nulls(jsonb_build_object('aufgabe_am', w.aufgabe_richtig_am, 'lernkarte_am', w.lk_richtig_am)), '{}'::jsonb),
      'erledigt', case when w.abgehakt_id is not null then jsonb_build_object('art', 'abgehakt', 'id', w.abgehakt_id, 'am', w.abgehakt_am,
                                                                              'tag', (w.abgehakt_am at time zone v_tz)::date) end));
  with offen as (select * from ww3_f where im_zeitraum and abgehakt_id is null),
       falsch_z as (select * from ww3_f where im_zeitraum),
       arten as (select f.art->>'schluessel' s, count(*) n, count(*) filter (where o.id is not null) n_offen,
                        min(f.art->>'kennung') kennung, min(f.art->>'text') text, min(f.art->>'grund') grund,
                        jsonb_agg(distinct f.thema_id) themen, max(f.am) zuletzt
                   from falsch_z f left join offen o on o.id = f.id where f.art ? 'schluessel' group by 1),
       wieder as (select * from arten where n >= 2 and n_offen > 0 order by n desc, zuletzt desc limit 3),
       je_lk as (select einheit_id, lz, count(*) n, min(id) id from offen group by 1, 2),
       einmal as (select o.* from je_lk j join offen o on o.id = j.id where j.n = 1
                    and not exists (select 1 from wieder w where w.s = o.art->>'schluessel')),
       -- besprochen je Thema: alle gültigen Markierungen des Kindes (ohne Zeitraum, ohne 200er-Grenze)
       bespr as (select v.thema_id, max(fe.am) zuletzt, count(distinct (fe.am at time zone v_tz)::date) tage, count(*) fehler
                   from schule.fehler_erledigt fe join ww3_v v on v.id = fe.versuch_id
                  where fe.lernender_id = p_l and fe.zurueckgenommen_am is null group by 1)
  select jsonb_build_object(
    'ok', true, 'stand', 3, 'lernender_id', p_l, 'tage', coalesce(nullif(p_tage, 0), 0), 'seit', v_seit, 'heute', (now() at time zone v_tz)::date,
    'mit_fehlbild', to_regprocedure('schule.versuch_regelbezug(schule.versuch)') is not null,
    'offen_zahl', (select count(*) from offen),
    'offen', coalesce((select jsonb_agg(o.eintrag order by o.am desc, o.id desc) from (select * from offen order by am desc, id desc limit 300) o), '[]'::jsonb),
    'auswertung', jsonb_build_object(
      'antworten', (select count(*) from ww3_v v where v_seit is null or v.am > v_seit),
      'richtig', (select count(*) from ww3_v v where (v_seit is null or v.am > v_seit) and v.richtig),
      'themen', coalesce((select jsonb_agg(jsonb_build_object('thema_id', t.thema_id, 'thema', (select coalesce(x.unterthema, x.schluessel) from schule.thema x where x.id = t.thema_id),
                                   'offen', t.offen, 'gesamt', t.gesamt,
                                   'besprochen', (select jsonb_build_object('zuletzt', b.zuletzt, 'zuletzt_tag', (b.zuletzt at time zone v_tz)::date, 'tage', b.tage, 'fehler', b.fehler,
                                                         'neu_seit', (select count(*) from ww3_f f where f.thema_id is not distinct from b.thema_id
                                                                         and f.am > b.zuletzt and f.abgehakt_id is null))
                                                    from bespr b where b.thema_id is not distinct from t.thema_id))
                                 order by t.offen desc, t.gesamt desc, t.thema_id)
                          from (select v.thema_id, count(*) gesamt, (select count(*) from offen o where o.thema_id is not distinct from v.thema_id) offen
                                  from ww3_v v where v_seit is null or v.am > v_seit group by 1) t), '[]'::jsonb),
      'lerntage', coalesce((select jsonb_agg(jsonb_build_object('tag', d.tag, 'richtig', d.r, 'falsch', d.f) order by d.tag)
                            from (select (v.am at time zone v_tz)::date tag, count(*) filter (where v.richtig) r, count(*) filter (where not v.richtig) f
                                    from ww3_v v group by 1 order by 1 desc limit 7) d), '[]'::jsonb),
      'wiederkehrend', coalesce((select jsonb_agg(jsonb_strip_nulls(jsonb_build_object('schluessel', w.s, 'kennung', w.kennung, 'text', w.text, 'grund', w.grund,
                                    'anzahl', w.n, 'offen', w.n_offen, 'themen', w.themen)) order by w.n desc, w.zuletzt desc) from wieder w), '[]'::jsonb),
      'einmal', jsonb_build_object('lernkarten', (select count(*) from einmal), 'danach_richtig', (select count(*) from einmal where lk_richtig_am is not null),
                                   'themen_danach_richtig', coalesce((select jsonb_agg(distinct thema_id) from einmal where lk_richtig_am is not null), '[]'::jsonb))),
    'erledigt', case when p_mit_erledigt then coalesce((select jsonb_agg(f.eintrag order by f.abgehakt_am desc, f.id desc)
                                                         from (select * from ww3_f where im_zeitraum and abgehakt_id is not null
                                                                order by abgehakt_am desc, id desc limit 200) f), '[]'::jsonb) end)
    into r;
  return jsonb_strip_nulls(r);
end $function$;
comment on function schule.wackelt_analyse(bigint, integer, boolean) is 'WW-S3: offene falsche Antworten eines Kindes im Zeitraum mit Aufgabe, Fehlerart, Folge danach; Auswertung mit „besprochen“ je Thema; stand 3 (inhalte/plan/wackelt-server.md). Nur lesend.';

-- 4. Markieren über versuch_ids (Signatur von WW-S2 bleibt; ein Rücknahmezweig existiert nicht mehr)
create or replace function schule.fehler_abhaken(p_l bigint, p_ids jsonb, p_zurueck boolean, p_von text)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare n int := 0; z record; v_nicht jsonb := '[]'; v_ids bigint[] := '{}'; v_mids bigint[] := '{}'; v_m bigint;
begin
  if coalesce(p_zurueck, false) then raise exception 'Zurückholen nur mit markierung_ids' using errcode = 'P0001'; end if;
  for z in select * from schule.ww_versuche(p_l, p_ids) order by 1 loop   -- ww_versuche: jede versuch_id genau einmal (distinct)
    if not z.ok then v_nicht := v_nicht || jsonb_build_object('versuch_id', z.versuch_id, 'grund', z.grund); continue; end if;
    v_m := null;
    insert into schule.fehler_erledigt (lernender_id, versuch_id, von) values (p_l, z.versuch_id, p_von)
      on conflict (versuch_id) where zurueckgenommen_am is null do nothing returning id into v_m;
    if v_m is not null then n := n + 1; v_ids := v_ids || z.versuch_id; v_mids := v_mids || v_m; end if;
  end loop;
  return jsonb_build_object('ok', true, 'stand', 3, 'geaendert', n, 'geaendert_ids', to_jsonb(v_ids), 'markierung_ids', to_jsonb(v_mids), 'uebersprungen', v_nicht);
end $function$;

-- 3. Zurückholen über die Markierungs-IDs: atomar (eine UPDATE-Anweisung), nur gültige Markierungen dieses Kindes
create or replace function schule.fehler_zurueckholen(p_l bigint, p_ids jsonb, p_von text)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_ids bigint[]; v_neu bigint[]; v_nicht jsonb;
begin
  if jsonb_typeof(p_ids) is distinct from 'array' or jsonb_array_length(p_ids) = 0 or jsonb_array_length(p_ids) > 200 then
    raise exception 'markierung_ids: Liste mit 1 bis 200 Einträgen' using errcode = 'P0001'; end if;
  if exists (select 1 from jsonb_array_elements(p_ids) x where jsonb_typeof(x) not in ('number', 'string') or (x #>> '{}') !~ '^\d{1,18}$') then
    raise exception 'markierung_ids: nur Zahlen' using errcode = 'P0001'; end if;
  v_ids := array(select distinct (x #>> '{}')::bigint from jsonb_array_elements(p_ids) x order by 1);   -- doppelte zusammengefasst
  -- Vertrag: jede angefragte ID steht danach GENAU EINMAL in geaendert_ids oder in uebersprungen (v_neu ⊆ v_ids, uebersprungen = v_ids ohne v_neu)
  with u as (update schule.fehler_erledigt fe set zurueckgenommen_am = now(), zurueckgenommen_von = p_von
              where fe.id = any(v_ids) and fe.lernender_id = p_l and fe.zurueckgenommen_am is null returning fe.id)
  select coalesce(array_agg(u.id order by u.id), '{}') into v_neu from u;
  select coalesce(jsonb_agg(jsonb_strip_nulls(jsonb_build_object('markierung_id', i.id, 'versuch_id', fe.versuch_id,
           'grund', case when fe.id is null then 'nicht gefunden'
                         when exists (select 1 from schule.fehler_erledigt g where g.versuch_id = fe.versuch_id and g.lernender_id = p_l
                                         and g.zurueckgenommen_am is null) then 'überholt'
                         else 'schon zurückgeholt' end)) order by i.id), '[]'::jsonb)
    into v_nicht
    from unnest(v_ids) i(id) left join schule.fehler_erledigt fe on fe.id = i.id and fe.lernender_id = p_l
   where not (i.id = any(v_neu));
  return jsonb_build_object('ok', true, 'stand', 3, 'geaendert', cardinality(v_neu), 'geaendert_ids', to_jsonb(v_neu), 'uebersprungen', v_nicht);
end $function$;

revoke all on function schule.wackelt_analyse(bigint, integer, boolean), schule.fehler_abhaken(bigint, jsonb, boolean, text),
  schule.fehler_zurueckholen(bigint, jsonb, text) from public, anon, authenticated;

-- 7. Aktion (Rechteprüfung wie WW-S2: wer_tn -> ist_leiter -> zugriff -> Kind aktiv)
create or replace function api.schule_fehler_abhaken(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint; v_z boolean := coalesce((p_daten->>'zurueck')::boolean, false);
  v_mids jsonb := nullif(p_daten->'markierung_ids', 'null'::jsonb);
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  perform schule.zugriff(p_schluessel, v_l);
  if not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  if v_mids is not null then
    if not v_z then raise exception 'markierung_ids nur mit zurueck: true' using errcode = 'P0001'; end if;
    if nullif(p_daten->'versuch_ids', 'null'::jsonb) is not null then raise exception 'entweder versuch_ids oder markierung_ids' using errcode = 'P0001'; end if;
    return schule.fehler_zurueckholen(v_l, v_mids, schule.ww_von(p_schluessel));
  end if;
  if v_z then raise exception 'Zurückholen nur mit markierung_ids' using errcode = 'P0001'; end if;   -- kein Rückholweg über versuch_ids
  return schule.fehler_abhaken(v_l, p_daten->'versuch_ids', false, schule.ww_von(p_schluessel));
end $function$;

do $$ begin
  if exists (select 1 from pg_roles where rolname = 'council_mcp') then
    grant execute on function api.schule_wackelt_analyse(text, jsonb), api.schule_fehler_abhaken(text, jsonb) to council_mcp;
  end if;
end $$;
revoke all on function api.schule_wackelt_analyse(text, jsonb), api.schule_fehler_abhaken(text, jsonb) from public, anon, authenticated;
$ww3mig$::text as sql;
-- Fingerabdruck des Bestehenden: Funktionen in schule/api (ohne die vier von WW-S3), alle Trigger (auch interne) und Indizes an Tabellen in schule,
-- Spalten (ohne fehler_erledigt)
create function pg_temp.ww3_schema() returns text language sql stable as $f$
  select md5(string_agg(x, '#' order by x)) from (
    select 'f:' || p.oid::regprocedure::text || ':' || pg_get_functiondef(p.oid) || ':' || coalesce(p.proacl::text, '') x from pg_proc p
     where p.pronamespace in ('schule'::regnamespace, 'api'::regnamespace) and p.prokind in ('f', 'p')
       and p.oid not in (select o from (select to_regprocedure(f) o from unnest(array['schule.wackelt_analyse(bigint, integer, boolean)', 'schule.fehler_abhaken(bigint, jsonb, boolean, text)', 'schule.fehler_zurueckholen(bigint, jsonb, text)', 'api.schule_fehler_abhaken(text, jsonb)']) f) q where o is not null)
    union all select 't:' || t.tgrelid::regclass::text || ':' || t.tgname || ':' || t.tgisinternal::text || ':' || pg_get_triggerdef(t.oid)
      from pg_trigger t join pg_class c on c.oid = t.tgrelid where c.relnamespace = 'schule'::regnamespace
    union all select 'c:' || a.attrelid::regclass::text || ':' || a.attname || ':' || format_type(a.atttypid, a.atttypmod)
      from pg_attribute a join pg_class c on c.oid = a.attrelid
     where c.relnamespace = 'schule'::regnamespace and c.relkind in ('r', 'p', 'v') and a.attnum > 0 and not a.attisdropped
       and c.oid is distinct from to_regclass('schule.fehler_erledigt')
    union all select 'i:' || i.indexrelid::regclass::text || ':' || pg_get_indexdef(i.indexrelid)
      from pg_index i join pg_class c on c.oid = i.indrelid where c.relnamespace = 'schule'::regnamespace and c.oid is distinct from to_regclass('schule.fehler_erledigt')) s $f$;
-- Aufbau von fehler_erledigt (Spalten, Indizes, RLS, Rechte, Fremdschlüssel) und ihr Inhalt (jede Zeile)
create function pg_temp.ww3_fe_aufbau() returns text language sql stable as $f$
  select md5(string_agg(s.x, '#' order by s.x)) from (
     select 'idx:' || indexrelid::regclass::text || pg_get_indexdef(indexrelid) x from pg_index where indrelid = 'schule.fehler_erledigt'::regclass
     union all select 'col:' || attname || format_type(atttypid, atttypmod) || attnotnull::text from pg_attribute where attrelid = 'schule.fehler_erledigt'::regclass and attnum > 0 and not attisdropped
     union all select 'con:' || conname || pg_get_constraintdef(oid) from pg_constraint where conrelid = 'schule.fehler_erledigt'::regclass
     union all select 'rls:' || relrowsecurity::text || coalesce(relacl::text, '') || coalesce(obj_description(oid, 'pg_class'), '') from pg_class where oid = 'schule.fehler_erledigt'::regclass) s $f$;
create function pg_temp.ww3_fe() returns text language sql stable as $f$
  select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) || ':' || count(*) from schule.fehler_erledigt x $f$;
-- Fingerabdruck aller Daten im Schema schule außer schule.fehler_erledigt
create function pg_temp.ww3_bestand() returns text language plpgsql as $f$
declare t regclass; h text; a text := '';
begin
  for t in select c.oid::regclass from pg_class c where c.relnamespace = 'schule'::regnamespace and c.relkind in ('r', 'p')
              and c.oid is distinct from to_regclass('schule.fehler_erledigt') order by c.oid::regclass::text loop
    execute format('select md5(coalesce(string_agg(x::text, %L order by x::text), %L)) from %s x', '|', '', t) into h;
    a := a || t::text || '=' || h || ';';
  end loop;
  return md5(a);
end $f$;
create temp table ww3_stand on commit drop as select (select count(*) from schule.versuch) n, (select coalesce(max(id), 0) from schule.versuch) m,
  pg_temp.ww3_schema() s, pg_temp.ww3_bestand() b, pg_temp.ww3_fe() fe, pg_temp.ww3_fe_aufbau() o,
  case when to_regprocedure('schule.fehler_zurueckholen(bigint, jsonb, text)') is null then 2 else 3 end stand_vorher;
do $p$ begin execute (select sql from ww3_mig); end $p$;
create temp table ww3_def on commit drop as select 1 lauf, (select md5(string_agg(coalesce(pg_get_functiondef(to_regprocedure(f)), 'fehlt'), '#' order by f)) from unnest(array['schule.wackelt_analyse(bigint, integer, boolean)', 'schule.fehler_abhaken(bigint, jsonb, boolean, text)', 'schule.fehler_zurueckholen(bigint, jsonb, text)', 'api.schule_fehler_abhaken(text, jsonb)']) f) d, pg_temp.ww3_fe_aufbau() o, pg_temp.ww3_schema() s, pg_temp.ww3_fe() fe;
do $p$ begin execute (select sql from ww3_mig); end $p$;
insert into ww3_def select 2, (select md5(string_agg(coalesce(pg_get_functiondef(to_regprocedure(f)), 'fehlt'), '#' order by f)) from unnest(array['schule.wackelt_analyse(bigint, integer, boolean)', 'schule.fehler_abhaken(bigint, jsonb, boolean, text)', 'schule.fehler_zurueckholen(bigint, jsonb, text)', 'api.schule_fehler_abhaken(text, jsonb)']) f), pg_temp.ww3_fe_aufbau(), pg_temp.ww3_schema(), pg_temp.ww3_fe();
-- Hilfen der Probe (nur pg_temp)
create function pg_temp.ww3_ant(p_k bigint, p_id bigint, p_wert text, p_cid text) returns jsonb language plpgsql as $f$
begin
  return schule.uebung_pruefen_wd(p_k, jsonb_build_object('aufgabe_id', p_id, 'client_id', p_cid, 'antwort', jsonb_build_object('wert', p_wert)));
end $f$;
create function pg_temp.ww3_ids(r jsonb, p text) returns bigint[] language sql immutable as $f$
  select coalesce(array_agg((e->>'versuch_id')::bigint), '{}') from jsonb_array_elements(coalesce(r->p, '[]'::jsonb)) e $f$;
create function pg_temp.ww3_arr(j jsonb) returns bigint[] language sql immutable as $f$
  select coalesce(array_agg((e #>> '{}')::bigint order by o), '{}') from jsonb_array_elements(coalesce(j, '[]'::jsonb)) with ordinality x(e, o) $f$;
create function pg_temp.ww3_eintrag(r jsonb, p text, v bigint) returns jsonb language sql immutable as $f$
  select e from jsonb_array_elements(coalesce(r->p, '[]'::jsonb)) e where (e->>'versuch_id')::bigint = v limit 1 $f$;
create function pg_temp.ww3_thema(r jsonb, p_th bigint) returns jsonb language sql immutable as $f$
  select t from jsonb_array_elements(r->'auswertung'->'themen') t where (t->>'thema_id')::bigint is not distinct from p_th limit 1 $f$;
create function pg_temp.ww3_summe_ok(r jsonb) returns boolean language sql immutable as $f$
  select coalesce(sum((t->>'offen')::bigint), 0) = (r->>'offen_zahl')::bigint from jsonb_array_elements(r->'auswertung'->'themen') t $f$;
-- feste Typen: stand Zahl 3; je Eintrag mit_tipp Boolean, danach_richtig Boolean oder fehlt, erledigt.id Zahl;
-- besprochen: zuletzt Text, zuletzt_tag JJJJ-MM-TT (Pflicht), tage >= 1, fehler >= 1, neu_seit >= 0 (Zahlen)
create function pg_temp.ww3_typen(r jsonb) returns text language sql immutable as $f$
  select coalesce(
    case when jsonb_typeof(r->'stand') is distinct from 'number' or r->>'stand' <> '3' then 'stand: ' || coalesce(r->>'stand', 'fehlt') end,
    (select 'versuch ' || (e->>'versuch_id') || ': mit_tipp ' || coalesce(jsonb_typeof(e->'mit_tipp'), 'fehlt') || ', danach_richtig '
            || coalesce(jsonb_typeof(e->'danach_richtig'), 'fehlt') || ', erledigt.id ' || coalesce(jsonb_typeof(e->'erledigt'->'id'), 'fehlt')
       from jsonb_array_elements(coalesce(r->'offen', '[]') || coalesce(r->'erledigt', '[]')) e
      where jsonb_typeof(e->'mit_tipp') is distinct from 'boolean' or (e ? 'danach_richtig' and jsonb_typeof(e->'danach_richtig') <> 'boolean')
         or (e ? 'erledigt' and jsonb_typeof(e->'erledigt'->'id') is distinct from 'number') limit 1),
    (select 'thema ' || coalesce(t->>'thema_id', 'ohne') || ': besprochen ' || (t->'besprochen')::text from jsonb_array_elements(r->'auswertung'->'themen') t
      where t ? 'besprochen' and (jsonb_typeof(t->'besprochen'->'tage') is distinct from 'number' or jsonb_typeof(t->'besprochen'->'neu_seit') is distinct from 'number'
                                  or jsonb_typeof(t->'besprochen'->'fehler') is distinct from 'number' or jsonb_typeof(t->'besprochen'->'zuletzt') is distinct from 'string'
                                  or coalesce(t->'besprochen'->>'zuletzt_tag', '') !~ '^\d{4}-\d{2}-\d{2}$'
                                  or (t->'besprochen'->>'tage')::numeric < 1 or (t->'besprochen'->>'fehler')::numeric < 1 or (t->'besprochen'->>'neu_seit')::numeric < 0) limit 1)) $f$;
-- unabhängige Nachrechnung von themen[].besprochen (direkt aus den Tabellen, nicht aus der Analyse)
create function pg_temp.ww3_bespr(p_k bigint, p_th bigint) returns jsonb language sql stable as $f$
  select case when count(*) > 0 then jsonb_build_object('zuletzt', max(fe.am),
           'zuletzt_tag', (max(fe.am) at time zone coalesce((select l.zeitzone from schule.lernender l where l.id = p_k), 'Europe/Berlin'))::date,
           'tage', count(distinct (fe.am at time zone coalesce((select l.zeitzone from schule.lernender l where l.id = p_k), 'Europe/Berlin'))::date),
           'fehler', count(*),
           'neu_seit', (select count(*) from schule.versuch x join schule.aufgabe a2 on a2.id = x.aufgabe_id join schule.einheit e2 on e2.id = a2.einheit_id
                         where x.lernender_id = p_k and e2.thema_id is not distinct from p_th and not x.richtig and schule.fehler_endgueltig_am(x) is not null
                           and x.am > max(fe.am)
                           and not exists (select 1 from schule.fehler_erledigt g where g.versuch_id = x.id and g.lernender_id = p_k and g.zurueckgenommen_am is null))) end
    from schule.fehler_erledigt fe join schule.versuch v on v.id = fe.versuch_id join schule.aufgabe a on a.id = v.aufgabe_id join schule.einheit e on e.id = a.einheit_id
   where fe.lernender_id = p_k and fe.zurueckgenommen_am is null and e.thema_id is not distinct from p_th $f$;
create function pg_temp.ww3_bespr_ok(p_k bigint, r jsonb) returns text language sql stable as $f$
  select 'thema ' || coalesce(t->>'thema_id', 'ohne') || ': ' || coalesce((t->'besprochen')::text, 'fehlt') || ' statt ' || coalesce(pg_temp.ww3_bespr(p_k, (t->>'thema_id')::bigint)::text, 'fehlt')
    from jsonb_array_elements(r->'auswertung'->'themen') t where (t->'besprochen') is distinct from pg_temp.ww3_bespr(p_k, (t->>'thema_id')::bigint) limit 1 $f$;
-- Vertrag (Auflagen aus Werkstatt 1165): Zurückholen – jede angefragte markierung_id GENAU EINMAL in geaendert_ids oder uebersprungen[];
-- Markieren – jede angefragte versuch_id höchstens einmal in geaendert_ids bzw. uebersprungen[], nie in beiden, nur angefragte IDs
create function pg_temp.ww3_zh(p_k bigint, p_ids jsonb, p_von text) returns jsonb language plpgsql as $f$
declare r jsonb := schule.fehler_zurueckholen(p_k, p_ids, p_von);
begin
  if exists (with a as (select distinct (x #>> '{}')::bigint id from jsonb_array_elements(p_ids) x),
                  b as (select (e #>> '{}')::bigint id from jsonb_array_elements(r->'geaendert_ids') e
                        union all select (u->>'markierung_id')::bigint from jsonb_array_elements(r->'uebersprungen') u)
             select 1 where (select count(*) from b) <> (select count(*) from a) or exists (select id from a except select id from b)
                         or exists (select id from b group by id having count(*) > 1)) then
    raise exception 'Vertrag Zurückholen verletzt (nicht genau einmal): % -> %', p_ids, r; end if;
  if (r->>'geaendert')::int <> jsonb_array_length(r->'geaendert_ids') then raise exception 'Vertrag Zurückholen: geaendert <> Länge geaendert_ids: %', r; end if;
  return r;
end $f$;
create function pg_temp.ww3_mk(p_k bigint, p_ids jsonb, p_von text) returns jsonb language plpgsql as $f$
declare r jsonb := schule.fehler_abhaken(p_k, p_ids, false, p_von);
begin
  if exists (with a as (select (x #>> '{}')::bigint id from jsonb_array_elements(p_ids) x),
                  g as (select (e #>> '{}')::bigint id from jsonb_array_elements(r->'geaendert_ids') e),
                  u as (select (e->>'versuch_id')::bigint id from jsonb_array_elements(r->'uebersprungen') e)
             select 1 where exists (select id from u group by id having count(*) > 1) or exists (select id from g group by id having count(*) > 1)
                         or exists (select id from g intersect select id from u) or exists (select id from g union select id from u except select id from a)) then
    raise exception 'Vertrag Markieren verletzt: % -> %', p_ids, r; end if;
  if (r->>'geaendert')::int <> jsonb_array_length(r->'geaendert_ids') or jsonb_array_length(r->'markierung_ids') <> jsonb_array_length(r->'geaendert_ids') then
    raise exception 'Vertrag Markieren: Längen passen nicht: %', r; end if;
  if exists (select 1 from jsonb_array_elements(r->'geaendert_ids') with ordinality g(v, o) join jsonb_array_elements(r->'markierung_ids') with ordinality m(id, o2) on o2 = o
              where not exists (select 1 from schule.fehler_erledigt fe where fe.id = (m.id #>> '{}')::bigint and fe.versuch_id = (g.v #>> '{}')::bigint
                                  and fe.lernender_id = p_k and fe.zurueckgenommen_am is null)) then
    raise exception 'Vertrag Markieren: markierung_ids[i] gehört nicht zu geaendert_ids[i]: %', r; end if;
  return r;
end $f$;
do $p$
declare
  fehler text[] := '{}'; k bigint := (select id from schule.lernender where ist_test order by id limit 1); v_e bigint; v_lz text; v_th bigint;
  a1 schule.aufgabe; a2 schule.aufgabe; a3 schule.aufgabe; v1 bigint; v2 bigint; v3 bigint; m1 bigint; m2 bigint; m1b bigint; mf bigint; mid bigint;
  r jsonb; q jsonb; x text; bericht jsonb := '{}'; t0 timestamptz; ms numeric; v_f bigint; v_gross bigint; v_eo bigint; b1 bigint; b2 bigint;
  s_kind text; s_fremd text; s_eltern text; s_lehrer text; v_id bigint; kn jsonb; ko jsonb; kz jsonb; h0 text; v0 bigint; arr bigint[]; n int; i int; vor int; weg text;
begin
  if (select count(distinct ww3_def.d) from ww3_def) <> 1 or (select count(distinct ww3_def.o) from ww3_def) <> 1 then fehler := fehler || ('zweiter Lauf hat etwas geändert')::text; end if;
  if exists (select 1 from ww3_def where ww3_def.s is distinct from (select ww3_stand.s from ww3_stand)) then
    fehler := fehler || ('Migration ändert Funktionen, Trigger, Indizes oder Spalten außerhalb von WW-S3')::text; end if;
  if exists (select 1 from ww3_def where ww3_def.o is distinct from (select ww3_stand.o from ww3_stand)) then fehler := fehler || ('Migration ändert den Aufbau von fehler_erledigt')::text; end if;
  if exists (select 1 from ww3_def where ww3_def.fe is distinct from (select ww3_stand.fe from ww3_stand)) then fehler := fehler || ('Migration ändert Zeilen von fehler_erledigt')::text; end if;
  -- Rechte
  if not (select relrowsecurity from pg_class where oid = 'schule.fehler_erledigt'::regclass) then fehler := fehler || ('fehler_erledigt: RLS aus')::text; end if;
  if exists (select 1 from pg_policy where polrelid = 'schule.fehler_erledigt'::regclass) then fehler := fehler || ('fehler_erledigt: hat eine Policy')::text; end if;
  if has_table_privilege('anon', 'schule.fehler_erledigt', 'select') or has_table_privilege('authenticated', 'schule.fehler_erledigt', 'select')
     or has_table_privilege('authenticated', 'schule.fehler_erledigt', 'update') then fehler := fehler || ('fehler_erledigt: App-Rollen haben Rechte')::text; end if;
  if exists (select 1 from pg_constraint where contype = 'f' and (conrelid = 'schule.fehler_erledigt'::regclass or confrelid = 'schule.fehler_erledigt'::regclass)) then
    fehler := fehler || ('fehler_erledigt: Fremdschlüssel')::text; end if;
  for x in select unnest(array['schule.wackelt_analyse(bigint, integer, boolean)', 'schule.fehler_abhaken(bigint, jsonb, boolean, text)', 'schule.fehler_zurueckholen(bigint, jsonb, text)', 'api.schule_fehler_abhaken(text, jsonb)']) loop
    if has_function_privilege('anon', x, 'execute') or has_function_privilege('authenticated', x, 'execute') then fehler := fehler || (x || ': für App-Rollen aufrufbar')::text; end if;
    if exists (select 1 from pg_proc p where p.oid = x::regprocedure and (p.proacl is null or exists (select 1 from aclexplode(p.proacl) a where a.grantee = 0))) then
      fehler := fehler || (x || ': für PUBLIC aufrufbar')::text; end if;
  end loop;
  for x in select unnest(array['api.schule_wackelt_analyse(text, jsonb)', 'api.schule_fehler_abhaken(text, jsonb)']) loop
    if position('if not schule.ist_leiter(p_schluessel) then raise exception' in pg_get_functiondef(x::regprocedure)) = 0 then fehler := fehler || (x || ': prüft ist_leiter nicht')::text; end if;
  end loop;
  if exists (select 1 from pg_trigger t where t.tgrelid = 'schule.versuch'::regclass and t.tgname ~ '^(ww|fehler)') then fehler := fehler || ('Trigger der WW-Seite an schule.versuch')::text; end if;
  begin
    r := api.schule_wackelt_analyse('ww-unbekannter-schluessel', jsonb_build_object('lernender_id', k));
    fehler := fehler || ('unbekannter Schlüssel bekommt eine Analyse')::text;
  exception when others then null;
  end;
  -- Lernkarte mit mindestens drei zählenden Zahl-Aufgaben (wie WW-S2)
  select x2.einheit_id, x2.variante_gruppe into v_e, v_lz from schule.aufgabe x2 join schule.einheit e on e.id = x2.einheit_id
   where x2.pool = 'uebung' and x2.freigegeben and e.status = 'freigegeben' and x2.antworttyp = 'zahl' and schule.aufgabe_zaehlt(x2)
     and (x2.loesung->>'wert')::numeric <> 987654 and x2.loesung->>'einheit' is null
   group by 1, 2 having count(*) >= 3 order by 1, 2 limit 1;
  if k is null or v_e is null then raise exception 'WW-S3: Testkind oder Lernkarte mit drei Zahl-Aufgaben fehlt'; end if;
  select thema_id into v_th from schule.einheit where id = v_e;
  select * into a1 from schule.aufgabe where einheit_id = v_e and variante_gruppe = v_lz and pool = 'uebung' and antworttyp = 'zahl' and freigegeben and loesung->>'einheit' is null order by id limit 1;
  select * into a2 from schule.aufgabe where einheit_id = v_e and variante_gruppe = v_lz and pool = 'uebung' and antworttyp = 'zahl' and freigegeben and loesung->>'einheit' is null and id > a1.id order by id limit 1;
  select * into a3 from schule.aufgabe where einheit_id = v_e and variante_gruppe = v_lz and pool = 'uebung' and antworttyp = 'zahl' and freigegeben and loesung->>'einheit' is null and id > a2.id order by id limit 1;
  select id into v_f from schule.lernender where id <> k and aktiv order by id limit 1;

  -- 2. Hauptfall: Typen, Markieren, besprochen, Zurückholen über markierung_ids, Parallelfall; dabei bleibt jede andere Tabelle in schule bytegleich
  begin
    perform pg_temp.ww3_ant(k, a1.id, '987654', 'ww3-1');
    perform pg_temp.ww3_ant(k, a2.id, '987654', 'ww3-2');
    perform pg_temp.ww3_ant(k, a3.id, '987654', 'ww3-3');
    select id into v1 from schule.versuch where lernender_id = k and client_id = 'ww3-1';
    select id into v2 from schule.versuch where lernender_id = k and client_id = 'ww3-2';
    select id into v3 from schule.versuch where lernender_id = k and client_id = 'ww3-3';
    r := pg_temp.ww3_ant(k, a1.id, replace(a1.loesung->>'wert', '.', ','), 'ww3-r');   -- danach richtig (Anzeige danach_richtig)
    h0 := pg_temp.ww3_bestand();
    r := schule.wackelt_analyse(k, 14, true);
    x := pg_temp.ww3_typen(r); if x is not null then fehler := fehler || ('Typen: ' || x)::text; end if;
    if not (array[v1, v2, v3] <@ pg_temp.ww3_ids(r, 'offen')) then fehler := fehler || ('Analyse: falsche Antworten nicht offen')::text; end if;
    q := pg_temp.ww3_eintrag(r, 'offen', v1);
    if q->'danach_richtig' is distinct from 'true'::jsonb or not (q->'danach_richtig_am' ? 'aufgabe_am') then
      bericht := bericht || jsonb_build_object('hinweis_danach_richtig', 'richtige Antwort nicht erkannt – danach_richtig nicht beobachtet: ' || left(coalesce(q::text, '-'), 200)); end if;
    if not pg_temp.ww3_summe_ok(r) then fehler := fehler || ('Summe themen[].offen ist nicht offen_zahl')::text; end if;
    -- Markieren (zwei auf einmal)
    r := pg_temp.ww3_mk(k, jsonb_build_array(v2, v1), 'probe');
    if (r->>'geaendert')::int <> 2 or pg_temp.ww3_arr(r->'geaendert_ids') <> array[least(v1, v2), greatest(v1, v2)] or (r->>'stand') is distinct from '3' then
      fehler := fehler || ('Markieren: ' || r::text)::text; end if;
    select id into m1 from schule.fehler_erledigt where versuch_id = v1 and zurueckgenommen_am is null;
    select id into m2 from schule.fehler_erledigt where versuch_id = v2 and zurueckgenommen_am is null;
    if pg_temp.ww3_arr(r->'markierung_ids') is distinct from (select array_agg(z order by z) from unnest(array[m1, m2]) z) then fehler := fehler || ('Markieren: markierung_ids passen nicht ' || r::text)::text; end if;
    r := pg_temp.ww3_mk(k, jsonb_build_array(v1), 'probe');
    if (r->>'geaendert')::int <> 0 or r->'geaendert_ids' <> '[]'::jsonb or r->'markierung_ids' <> '[]'::jsonb then fehler := fehler || ('zweites Markieren ändert etwas: ' || r::text)::text; end if;
    r := schule.wackelt_analyse(k, 14, true);
    q := pg_temp.ww3_eintrag(r, 'erledigt', v1);
    if (q->'erledigt'->>'id')::bigint is distinct from m1 or not (q->'erledigt' ? 'tag') or q->'erledigt'->>'art' is distinct from 'abgehakt' then fehler := fehler || ('erledigt.id/tag fehlt: ' || coalesce(q->>'erledigt', '-'))::text; end if;
    if v1 = any(pg_temp.ww3_ids(r, 'offen')) then fehler := fehler || ('markierte Antwort noch offen')::text; end if;
    x := pg_temp.ww3_typen(r); if x is not null then fehler := fehler || ('Typen (mit erledigt): ' || x)::text; end if;
    -- besprochen je Thema: zwei Gesprächstage, ein neuer Fehler danach
    update schule.fehler_erledigt set am = now() - interval '2 days' where id = m1;   -- nur die eigene Tabelle, in dieser Untertransaktion
    update schule.fehler_erledigt set am = now() - interval '1 hour' where id = m2;
    r := schule.wackelt_analyse(k, 0, false);
    q := pg_temp.ww3_thema(r, v_th);
    if q->'besprochen' is null or (q->'besprochen'->>'tage')::int < 2 or (q->'besprochen'->>'neu_seit')::int < 1 or (q->'besprochen'->>'fehler')::int < 2 then fehler := fehler || ('besprochen fehlt oder falsch: ' || coalesce(q::text, '-'))::text; end if;
    x := pg_temp.ww3_bespr_ok(k, r); if x is not null then fehler := fehler || ('besprochen weicht von der Nachrechnung ab: ' || x)::text; end if;
    bericht := bericht || jsonb_build_object('besprochen_beispiel', q->'besprochen');
    -- Zurückholen über markierung_ids
    r := pg_temp.ww3_zh(k, jsonb_build_array(m1), 'probe');
    if (r->>'geaendert')::int <> 1 or pg_temp.ww3_arr(r->'geaendert_ids') <> array[m1] or r->'uebersprungen' <> '[]'::jsonb then fehler := fehler || ('Zurückholen: ' || r::text)::text; end if;
    r := schule.wackelt_analyse(k, 0, false);
    if not v1 = any(pg_temp.ww3_ids(r, 'offen')) then fehler := fehler || ('nach Zurückholen nicht wieder offen')::text; end if;
    x := pg_temp.ww3_bespr_ok(k, r); if x is not null then fehler := fehler || ('besprochen nach Zurückholen: ' || x)::text; end if;
    if (pg_temp.ww3_thema(r, v_th)->'besprochen'->>'tage')::int is distinct from (pg_temp.ww3_bespr(k, v_th)->>'tage')::int then fehler := fehler || ('besprochen zählt zurückgeholte Markierungen')::text; end if;
    -- PARALLELFALL: v1 ist zurückgeholt und wird neu markiert; ein Klick auf den veralteten Eintrag (m1) darf die neue Markierung nicht entfernen
    r := pg_temp.ww3_mk(k, jsonb_build_array(v1), 'probe');
    m1b := (pg_temp.ww3_arr(r->'markierung_ids'))[1];
    if m1b is null or m1b = m1 or pg_temp.ww3_arr(r->'geaendert_ids') <> array[v1] then fehler := fehler || ('neu markieren: ' || r::text)::text; end if;
    r := pg_temp.ww3_zh(k, jsonb_build_array(m1), 'probe');
    if (r->>'geaendert')::int <> 0 or r->'geaendert_ids' <> '[]'::jsonb
       or r->'uebersprungen' <> jsonb_build_array(jsonb_build_object('markierung_id', m1, 'versuch_id', v1, 'grund', 'überholt')) then fehler := fehler || ('Parallelfall: ' || r::text)::text; end if;
    if not exists (select 1 from schule.fehler_erledigt where id = m1b and zurueckgenommen_am is null) then fehler := fehler || ('Parallelfall: neue Markierung entfernt')::text; end if;
    if v1 = any(pg_temp.ww3_ids(schule.wackelt_analyse(k, 0, false), 'offen')) then fehler := fehler || ('Parallelfall: neu markierte Antwort wieder offen')::text; end if;
    -- Negativprobe Altweg (Auflagen aus Werkstatt 1165): nach „überholt“ darf zurueck + versuch_ids die NEUE Markierung nicht zurücknehmen – auch intern nicht
    begin perform schule.fehler_abhaken(k, jsonb_build_array(v1), true, 'probe'); fehler := fehler || ('Altweg: Rücknahme über versuch_ids angenommen')::text;
    exception when others then if position('Zurückholen nur mit markierung_ids' in sqlerrm) = 0 then fehler := fehler || ('Altweg: falscher Fehler ' || sqlerrm)::text; end if; end;
    if not exists (select 1 from schule.fehler_erledigt where id = m1b and zurueckgenommen_am is null) then fehler := fehler || ('Altweg: neue Markierung zurückgenommen')::text; end if;
    bericht := bericht || jsonb_build_object('parallelfall', jsonb_build_object('veraltet', m1, 'neu', m1b, 'antwort', r));
    -- doppelt genannt, dann schon zurückgeholt
    r := pg_temp.ww3_zh(k, jsonb_build_array(m1b, m1b, m2), 'probe');
    if (r->>'geaendert')::int <> 2 or pg_temp.ww3_arr(r->'geaendert_ids') <> (select array_agg(z order by z) from unnest(array[m1b, m2]) z) then fehler := fehler || ('Zurückholen doppelt: ' || r::text)::text; end if;
    r := pg_temp.ww3_zh(k, jsonb_build_array(m2), 'probe');
    if (r->>'geaendert')::int <> 0 or r->'uebersprungen'->0->>'grund' is distinct from 'schon zurückgeholt' then fehler := fehler || ('schon zurückgeholt: ' || r::text)::text; end if;
    x := pg_temp.ww3_bespr_ok(k, schule.wackelt_analyse(k, 0, false)); if x is not null then fehler := fehler || ('besprochen nach allem Zurückholen: ' || x)::text; end if;
    -- fremde und unbekannte Markierungen: übersprungen, nichts verraten, nichts geändert
    insert into schule.fehler_erledigt (lernender_id, versuch_id, von) values (coalesce(v_f, -1), -987654, 'probe') returning id into mf;
    r := pg_temp.ww3_zh(k, jsonb_build_array(mf, 0), 'probe');
    if (r->>'geaendert')::int <> 0 or jsonb_array_length(r->'uebersprungen') <> 2
       or exists (select 1 from jsonb_array_elements(r->'uebersprungen') u where u->>'grund' <> 'nicht gefunden' or u ? 'versuch_id') then fehler := fehler || ('fremde/unbekannte Markierung: ' || r::text)::text; end if;
    if not exists (select 1 from schule.fehler_erledigt where id = mf and zurueckgenommen_am is null) then fehler := fehler || ('fremde Markierung zurückgeholt')::text; end if;
    -- Eingabeprüfung
    foreach q in array array['[]'::jsonb, '[1.5]'::jsonb, '"7"'::jsonb, '["x"]'::jsonb, to_jsonb(array(select generate_series(1, 201)))] loop
      begin perform schule.fehler_zurueckholen(k, q, 'probe'); fehler := fehler || ('markierung_ids angenommen: ' || left(q::text, 40))::text;
      exception when others then if position('markierung_ids' in sqlerrm) = 0 then fehler := fehler || ('markierung_ids: falscher Fehler ' || sqlerrm)::text; end if; end;
    end loop;
    -- doppelt genannte versuch_id beim Markieren: zusammengefasst; Rücknahme über versuch_ids gibt es nicht mehr (Auflagen aus Werkstatt 1165)
    r := pg_temp.ww3_mk(k, jsonb_build_array(v2, v2), 'probe');
    if (r->>'geaendert')::int <> 1 or pg_temp.ww3_arr(r->'geaendert_ids') <> array[v2] then fehler := fehler || ('Markieren doppelt: ' || r::text)::text; end if;
    begin perform schule.fehler_abhaken(k, jsonb_build_array(v2), true, 'probe'); fehler := fehler || ('Rücknahme über versuch_ids angenommen')::text;
    exception when others then if position('Zurückholen nur mit markierung_ids' in sqlerrm) = 0 then fehler := fehler || ('Rücknahme über versuch_ids: falscher Fehler ' || sqlerrm)::text; end if; end;
    if not exists (select 1 from schule.fehler_erledigt where versuch_id = v2 and zurueckgenommen_am is null) then fehler := fehler || ('Rücknahme über versuch_ids hat zurückgenommen')::text; end if;
    r := pg_temp.ww3_mk(k, jsonb_build_array(0, coalesce((select min(id) from schule.versuch where lernender_id <> k), 0)), 'probe');
    if (r->>'geaendert')::int <> 0 or jsonb_array_length(r->'uebersprungen') = 0 or r->'markierung_ids' <> '[]'::jsonb then fehler := fehler || ('fremde Versuche markiert: ' || r::text)::text; end if;
    if pg_temp.ww3_bestand() is distinct from h0 then fehler := fehler || ('Markieren/Zurückholen verändert Daten außerhalb von fehler_erledigt')::text; end if;
    bericht := bericht || jsonb_build_object('bestand_gleich_beim_markieren', pg_temp.ww3_bestand() = h0, 'typen_ok', true);
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then fehler := fehler || ('Hauptfall: ' || sqlerrm)::text;
  end;

  -- 2b. Zeitzone: Kind in Pacific/Auckland (nur in dieser Untertransaktion), Markierung um 00:05 Ortszeit (in UTC noch der Vortag) ->
  --     besprochen.zuletzt_tag und erledigt.tag sind der Ortstag, nicht der UTC-Tag
  begin
    update schule.lernender set zeitzone = 'Pacific/Auckland' where id = k;
    perform pg_temp.ww3_ant(k, a1.id, '987654', 'ww3-tz');
    select id into v1 from schule.versuch where lernender_id = k and client_id = 'ww3-tz';
    r := pg_temp.ww3_mk(k, jsonb_build_array(v1), 'probe');
    mid := (pg_temp.ww3_arr(r->'markierung_ids'))[1];
    t0 := (date_trunc('day', now() at time zone 'Pacific/Auckland') + interval '5 minutes') at time zone 'Pacific/Auckland';   -- heute 00:05 Ortszeit
    update schule.fehler_erledigt set am = t0 where id = mid;
    if (t0 at time zone 'UTC')::date = (t0 at time zone 'Pacific/Auckland')::date then fehler := fehler || ('Zeitzone: Prüffall trennt Ortstag und UTC-Tag nicht')::text; end if;
    r := schule.wackelt_analyse(k, 0, true);
    q := pg_temp.ww3_thema(r, v_th);
    if (q->'besprochen'->>'zuletzt')::timestamptz = t0 and q->'besprochen'->>'zuletzt_tag' is distinct from ((t0 at time zone 'Pacific/Auckland')::date)::text then
      fehler := fehler || ('Zeitzone: zuletzt_tag ' || coalesce(q->'besprochen'->>'zuletzt_tag', 'fehlt') || ' statt Ortstag ' || (t0 at time zone 'Pacific/Auckland')::date)::text; end if;
    if (q->'besprochen'->>'zuletzt')::timestamptz is distinct from t0 then
      bericht := bericht || jsonb_build_object('hinweis_zeitzone', 'eine spätere Markierung im Thema – zuletzt_tag nur gegen die Nachrechnung geprüft'); end if;
    if pg_temp.ww3_eintrag(r, 'erledigt', v1)->'erledigt'->>'tag' is distinct from ((t0 at time zone 'Pacific/Auckland')::date)::text then
      fehler := fehler || ('Zeitzone: erledigt.tag ist nicht der Ortstag')::text; end if;
    x := pg_temp.ww3_bespr_ok(k, r); if x is not null then fehler := fehler || ('Zeitzone: besprochen weicht von der Nachrechnung ab: ' || x)::text; end if;
    x := pg_temp.ww3_typen(r); if x is not null then fehler := fehler || ('Zeitzone, Typen: ' || x)::text; end if;
    bericht := bericht || jsonb_build_object('zeitzone', jsonb_build_object('zone', 'Pacific/Auckland', 'markiert_utc', (t0 at time zone 'UTC')::text,
                 'zuletzt_tag', q->'besprochen'->'zuletzt_tag', 'utc_tag', (t0 at time zone 'UTC')::date));
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then fehler := fehler || ('Zeitzone: ' || sqlerrm)::text;
  end;

  -- 3. Ohne Thema: zwei offene Fehler, dann 300 neuere – das Thema „ohne“ wird immer gezählt
  begin
    weg := 'vorhanden';
    select a.einheit_id into v_eo from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id where e.thema_id is null and a.pool = 'uebung' and a.freigegeben and e.status = 'freigegeben' and a.antworttyp = 'zahl' and schule.aufgabe_zaehlt(a)
     and (a.loesung->>'wert')::numeric <> 987654 and a.loesung->>'einheit' is null
     group by 1 having count(*) >= 2 order by 1 limit 1;
    if v_eo is null then
      select a.einheit_id into v_eo from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id where a.pool = 'uebung' and a.freigegeben and e.status = 'freigegeben' and a.antworttyp = 'zahl' and schule.aufgabe_zaehlt(a)
     and (a.loesung->>'wert')::numeric <> 987654 and a.loesung->>'einheit' is null group by 1 having count(*) >= 2 order by 1 limit 1;
      begin
        update schule.einheit set thema_id = null where id = v_eo;   -- nur in dieser (zurückgerollten) Untertransaktion
        weg := 'vorübergehend ohne Thema';
      exception when others then weg := 'übersprungen: ' || sqlerrm; v_eo := null;
      end;
    end if;
    if v_eo is not null then
      arr := array(select a.id from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id where a.einheit_id = v_eo and a.pool = 'uebung' and a.freigegeben and e.status = 'freigegeben' and a.antworttyp = 'zahl' and schule.aufgabe_zaehlt(a)
     and (a.loesung->>'wert')::numeric <> 987654 and a.loesung->>'einheit' is null order by a.id limit 2);
      perform pg_temp.ww3_ant(k, arr[1], '987654', 'ww3-o1');
      perform pg_temp.ww3_ant(k, arr[2], '987654', 'ww3-o2');
      select id into b1 from schule.versuch where lernender_id = k and client_id = 'ww3-o1';
      select id into b2 from schule.versuch where lernender_id = k and client_id = 'ww3-o2';
      h0 := pg_temp.ww3_bestand();
      r := schule.wackelt_analyse(k, 14, false);
      q := pg_temp.ww3_thema(r, null);
      if q is null or (q->>'offen')::int < 2 then fehler := fehler || ('ohne Thema: offen nicht gezählt ' || coalesce(q::text, 'Thema fehlt'))::text; end if;
      if not pg_temp.ww3_summe_ok(r) then fehler := fehler || ('ohne Thema: Summe themen[].offen ist nicht offen_zahl')::text; end if;
      x := pg_temp.ww3_typen(r) ; if x is not null then fehler := fehler || ('ohne Thema, Typen: ' || x)::text; end if;
      vor := (r->>'offen_zahl')::int;
      bericht := bericht || jsonb_build_object('ohne_thema', jsonb_build_object('weg', 'vorhanden', 'offen_ohne_thema', q->'offen', 'offen_zahl', vor));
      -- 300 neuere Fehler an Lernkarten mit Thema
      arr := array(select a.id from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id where e.thema_id is not null and a.pool = 'uebung' and a.freigegeben and e.status = 'freigegeben' and a.antworttyp = 'zahl' and schule.aufgabe_zaehlt(a)
     and (a.loesung->>'wert')::numeric <> 987654 and a.loesung->>'einheit' is null order by a.id limit 300);
      n := 0; i := 0;
      while n < 300 and i < 900 and cardinality(arr) > 0 loop
        i := i + 1;
        begin perform pg_temp.ww3_ant(k, arr[1 + (i - 1) % cardinality(arr)], '987654', 'ww3-m' || i); n := n + 1;
        exception when others then null; end;
      end loop;
      r := schule.wackelt_analyse(k, 14, false);
      q := pg_temp.ww3_thema(r, null);
      if q is null or (q->>'offen')::int < 2 then fehler := fehler || ('ohne Thema jenseits der 300: nicht gezählt ' || coalesce(q::text, 'Thema fehlt'))::text; end if;
      if not pg_temp.ww3_summe_ok(r) then fehler := fehler || ('ohne Thema jenseits der 300: Summe themen[].offen ist nicht offen_zahl')::text; end if;
      if (r->>'offen_zahl')::int >= vor + 300 and (b1 = any(pg_temp.ww3_ids(r, 'offen')) or b2 = any(pg_temp.ww3_ids(r, 'offen'))) then
        fehler := fehler || ('ohne Thema: Fehler nicht jenseits der 300 neuesten')::text; end if;
      t0 := clock_timestamp(); perform schule.wackelt_analyse(k, 0, true); ms := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
      bericht := jsonb_set(bericht, '{ohne_thema}', (bericht->'ohne_thema') || jsonb_build_object('weg', weg, 'neue_fehler', n, 'offen_zahl_danach', r->'offen_zahl',
                   'offen_ohne_thema_danach', q->'offen', 'jenseits_300', (r->>'offen_zahl')::int > 300 and not (b1 = any(pg_temp.ww3_ids(r, 'offen'))), 'laufzeit_ms_300', ms));
      if (r->>'offen_zahl')::int < vor + 300 then bericht := bericht || jsonb_build_object('hinweis_ohne_thema', 'weniger als 300 neue offene Fehler angelegt: ' || n); end if;
    else
      bericht := bericht || jsonb_build_object('ohne_thema', jsonb_build_object('weg', weg));
    end if;
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then fehler := fehler || ('Ohne Thema: ' || sqlerrm)::text;
  end;

  -- 4. Rechte mit echten Lern-Schlüsseln (Logins und Sitzungen nur in dieser Untertransaktion): Kind, fremdes Kind, Eltern, Lehrer, unbekannt
  begin
    insert into schule.lern_login (name, rolle, lernender_id, code_hash) values ('WW3-Probe Kind', 'kind', k, md5('ww3-k' || clock_timestamp()::text)) returning id into v_id;
    s_kind := md5('ww3-sk' || clock_timestamp()::text); insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (s_kind, v_id, now() + interval '1 hour'); s_kind := 'lern:' || s_kind;
    insert into schule.lern_login (name, rolle, lernender_id, code_hash) values ('WW3-Probe Eltern', 'eltern', null, md5('ww3-e' || clock_timestamp()::text)) returning id into v_id;
    s_eltern := md5('ww3-se' || clock_timestamp()::text); insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (s_eltern, v_id, now() + interval '1 hour'); s_eltern := 'lern:' || s_eltern;
    insert into schule.lern_login (name, rolle, lernender_id, code_hash) values ('WW3-Probe Lehrer', 'lehrer', null, md5('ww3-l' || clock_timestamp()::text)) returning id into v_id;
    s_lehrer := md5('ww3-sl' || clock_timestamp()::text); insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (s_lehrer, v_id, now() + interval '1 hour'); s_lehrer := 'lern:' || s_lehrer;
    if v_f is not null then
      insert into schule.lern_login (name, rolle, lernender_id, code_hash) values ('WW3-Probe Fremd', 'kind', v_f, md5('ww3-f' || clock_timestamp()::text)) returning id into v_id;
      s_fremd := md5('ww3-sf' || clock_timestamp()::text); insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (s_fremd, v_id, now() + interval '1 hour'); s_fremd := 'lern:' || s_fremd;
    end if;
    perform pg_temp.ww3_ant(k, a1.id, '987654', 'ww3-api');
    select id into v0 from schule.versuch where lernender_id = k and client_id = 'ww3-api';
    insert into schule.fehler_erledigt (lernender_id, versuch_id, von) values (k, v0, 'probe') returning id into mid;   -- für die Zurückhol-Versuche von Kind/Fremd
    h0 := pg_temp.ww3_bestand();
    foreach x in array array[s_kind, s_fremd] loop
      continue when x is null;
      begin r := api.schule_wackelt_analyse(x, jsonb_build_object('lernender_id', k)); fehler := fehler || ('Kind liest die Analyse')::text;
      exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then fehler := fehler || ('Kind/Analyse: falscher Fehler ' || sqlerrm)::text; end if; end;
      begin r := api.schule_fehler_abhaken(x, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0))); fehler := fehler || ('Kind markiert')::text;
      exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then fehler := fehler || ('Kind/Markieren: falscher Fehler ' || sqlerrm)::text; end if; end;
      begin r := api.schule_fehler_abhaken(x, jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid), 'zurueck', true)); fehler := fehler || ('Kind holt zurück')::text;
      exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then fehler := fehler || ('Kind/Zurückholen: falscher Fehler ' || sqlerrm)::text; end if; end;
    end loop;
    if s_fremd is null then bericht := bericht || '{"hinweis_fremdkind": "kein zweites aktives Kind – Fremdkind-Probe übersprungen"}'::jsonb; end if;
    if not exists (select 1 from schule.fehler_erledigt where id = mid and zurueckgenommen_am is null) then fehler := fehler || ('Kind-Sitzung hat zurückgeholt')::text; end if;
    delete from schule.fehler_erledigt where id = mid;   -- nur die eben angelegte Probezeile
    r := api.schule_wackelt_analyse(s_eltern, jsonb_build_object('lernender_id', k, 'tage', 0, 'erledigt', true));
    if r->>'ok' is distinct from 'true' or (r->>'stand') is distinct from '3' then fehler := fehler || ('Eltern lesen die Analyse nicht (stand 3)')::text; end if;
    r := api.schule_fehler_abhaken(s_eltern, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0)));
    mid := (pg_temp.ww3_arr(r->'markierung_ids'))[1];
    if (r->>'geaendert')::int <> 1 or mid is null or pg_temp.ww3_arr(r->'geaendert_ids') <> array[v0] then fehler := fehler || ('Eltern markieren nicht: ' || r::text)::text; end if;
    if (select von from schule.fehler_erledigt where id = mid) is distinct from 'eltern:WW3-Probe Eltern' then fehler := fehler || ('von falsch')::text; end if;
    begin r := api.schule_fehler_abhaken(s_eltern, jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid))); fehler := fehler || ('markierung_ids ohne zurueck angenommen')::text;
    exception when others then if position('markierung_ids nur mit zurueck' in sqlerrm) = 0 then fehler := fehler || ('markierung_ids ohne zurueck: falscher Fehler ' || sqlerrm)::text; end if; end;
    begin r := api.schule_fehler_abhaken(s_eltern, jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid), 'versuch_ids', jsonb_build_array(v0), 'zurueck', true));
      fehler := fehler || ('versuch_ids und markierung_ids zusammen angenommen')::text;
    exception when others then if position('entweder versuch_ids oder markierung_ids' in sqlerrm) = 0 then fehler := fehler || ('beide Listen: falscher Fehler ' || sqlerrm)::text; end if; end;
    r := api.schule_wackelt_analyse(s_lehrer, jsonb_build_object('lernender_id', k, 'tage', 7, 'erledigt', true));
    if (pg_temp.ww3_eintrag(r, 'erledigt', v0)->'erledigt'->>'id')::bigint is distinct from mid then fehler := fehler || ('Lehrer: erledigt.id fehlt')::text; end if;
    r := api.schule_fehler_abhaken(s_lehrer, jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid), 'zurueck', true));
    if (r->>'geaendert')::int <> 1 or pg_temp.ww3_arr(r->'geaendert_ids') <> array[mid] then fehler := fehler || ('Lehrer holen nicht zurück: ' || r::text)::text; end if;
    if (select zurueckgenommen_von from schule.fehler_erledigt where id = mid) is distinct from 'lehrer:WW3-Probe Lehrer' then fehler := fehler || ('zurueckgenommen_von falsch')::text; end if;
    r := api.schule_fehler_abhaken(s_lehrer, jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid), 'zurueck', true));
    if (r->>'geaendert')::int <> 0 or r->'uebersprungen'->0->>'grund' is distinct from 'schon zurückgeholt' then fehler := fehler || ('Lehrer zweimal zurück: ' || r::text)::text; end if;
    -- Negativprobe Altweg über die api: neu markieren, alte ID -> „überholt“, dann zurueck + versuch_ids -> abgewiesen, neue Markierung bleibt
    r := api.schule_fehler_abhaken(s_eltern, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0)));
    v_id := (pg_temp.ww3_arr(r->'markierung_ids'))[1];
    r := api.schule_fehler_abhaken(s_lehrer, jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid), 'zurueck', true));
    if r->'uebersprungen'->0->>'grund' is distinct from 'überholt' or (r->>'geaendert')::int <> 0 then fehler := fehler || ('api: alte Markierung nicht überholt: ' || r::text)::text; end if;
    foreach q in array array[jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0), 'zurueck', true), jsonb_build_object('lernender_id', k, 'zurueck', true)] loop
      begin r := api.schule_fehler_abhaken(s_lehrer, q); fehler := fehler || ('api: Rücknahme ohne markierung_ids angenommen: ' || q::text)::text;
      exception when others then if position('Zurückholen nur mit markierung_ids' in sqlerrm) = 0 then fehler := fehler || ('api: Rücknahme ohne markierung_ids, falscher Fehler ' || sqlerrm)::text; end if; end;
    end loop;
    if not exists (select 1 from schule.fehler_erledigt where id = v_id and zurueckgenommen_am is null) then fehler := fehler || ('api: neue Markierung über den Altweg zurückgenommen')::text; end if;
    begin r := api.schule_wackelt_analyse(s_eltern, jsonb_build_object('lernender_id', k, 'tage', 3)); fehler := fehler || ('tage 3 angenommen')::text;
    exception when others then if position('tage' in sqlerrm) = 0 then fehler := fehler || ('tage: falscher Fehler ' || sqlerrm)::text; end if; end;
    begin r := api.schule_wackelt_analyse('lern:ww3-gibt-es-nicht', jsonb_build_object('lernender_id', k)); fehler := fehler || ('unbekannte Sitzung liest die Analyse')::text;
    exception when others then null; end;
    begin r := api.schule_fehler_abhaken('lern:ww3-gibt-es-nicht', jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0))); fehler := fehler || ('unbekannte Sitzung markiert')::text;
    exception when others then null; end;
    begin r := api.schule_fehler_abhaken('lern:ww3-gibt-es-nicht', jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid), 'zurueck', true)); fehler := fehler || ('unbekannte Sitzung holt zurück')::text;
    exception when others then null; end;
    if pg_temp.ww3_bestand() is distinct from h0 then fehler := fehler || ('api-Aktionen verändern Daten außerhalb von fehler_erledigt')::text; end if;
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then fehler := fehler || ('Rechte: ' || sqlerrm)::text;
  end;

  -- 5. Karte: Markieren, Zurückholen (markierung_ids) und neu Markieren an einer sitzenden, nicht fälligen Lernkarte; ein weiterer Fehler wirkt wie ohne
  if to_regclass('schule.karte_stand') is not null then
    for i in 1 .. 2 loop
      begin
        insert into schule.karte_stand (lernender_id, einheit_id, lernziel) values (k, v_e, v_lz) on conflict do nothing;
        update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '10 days', wdh_stufe = 2, wdh_fehler = 0, wdh_ab = now(), wdh_lerntage = 7,
               faellig_am = now() + interval '7 days' where lernender_id = k and einheit_id = v_e and lernziel = v_lz;
        perform pg_temp.ww3_ant(k, a1.id, '987654', 'ww3-k0');
        execute 'select to_jsonb(x) from schule.karte_stand x where x.lernender_id = $1 and x.einheit_id = $2 and x.lernziel = $3' into ko using k, v_e, v_lz;
        if i = 1 then
          h0 := pg_temp.ww3_bestand();
          r := pg_temp.ww3_mk(k, jsonb_build_array((select id from schule.versuch where lernender_id = k and client_id = 'ww3-k0')), 'probe');
          mid := (pg_temp.ww3_arr(r->'markierung_ids'))[1];
          r := pg_temp.ww3_zh(k, jsonb_build_array(mid), 'probe');
          if (r->>'geaendert')::int <> 1 then fehler := fehler || ('Karte: Zurückholen ' || r::text)::text; end if;
          r := pg_temp.ww3_mk(k, jsonb_build_array((select id from schule.versuch where lernender_id = k and client_id = 'ww3-k0')), 'probe');
          if (r->>'geaendert')::int <> 1 then fehler := fehler || ('Karte: neu Markieren ' || r::text)::text; end if;
          execute 'select to_jsonb(x) from schule.karte_stand x where x.lernender_id = $1 and x.einheit_id = $2 and x.lernziel = $3' into kz using k, v_e, v_lz;
          if kz is distinct from ko then fehler := fehler || ('Karte: Markieren/Zurückholen ändert die Kartenzeile')::text; end if;
          if pg_temp.ww3_bestand() is distinct from h0 then fehler := fehler || ('Karte: Markieren/Zurückholen ändert Daten außerhalb von fehler_erledigt')::text; end if;
        end if;
        r := pg_temp.ww3_ant(k, a2.id, '987654', 'ww3-k' || i);
        if r->>'richtig' is distinct from 'false' then fehler := fehler || ('Karte: Fehlantwort nicht als falsch bewertet ' || r::text)::text; end if;
        execute 'select to_jsonb(x) from schule.karte_stand x where x.lernender_id = $1 and x.einheit_id = $2 and x.lernziel = $3' into r using k, v_e, v_lz;
        kn := coalesce(kn, '{}'::jsonb) || jsonb_build_object(case i when 1 then 'mit_markierung' else 'ohne_markierung' end,
                jsonb_build_object('nach_1_fehler', jsonb_build_object('sitzt', ko->'sitzt', 'wdh_fehler', ko->'wdh_fehler'),
                                   'nach_2_fehler', jsonb_build_object('sitzt', r->'sitzt', 'wdh_fehler', r->'wdh_fehler', 'geoeffnet', r->'geoeffnet_am' <> 'null'::jsonb),
                                   'zeile', r - 'zuletzt' - 'geoeffnet_am' - 'gezaehlt' - 'sitzt_am' - 'wdh_ab' - 'faellig_am'));
        raise exception using errcode = 'WW999', message = 'zurueck';
      exception when sqlstate 'WW999' then null;
        when others then fehler := fehler || ('Karte (' || i || '): ' || sqlerrm)::text;
      end;
    end loop;
    if kn->'mit_markierung'->'zeile' is distinct from kn->'ohne_markierung'->'zeile' then fehler := fehler || ('Markierung wirkt auf die Karte: ' || kn::text)::text; end if;
    bericht := bericht || jsonb_build_object('karte_markierung_ohne_wirkung', jsonb_build_object('mit_markierung', (kn->'mit_markierung') - 'zeile', 'ohne_markierung', (kn->'ohne_markierung') - 'zeile'));
  end if;
  -- 6. Laufzeit der Analyse „alles“ (Testkind und das Kind mit den meisten Versuchen; nur die Zeit wird berichtet)
  t0 := clock_timestamp(); perform schule.wackelt_analyse(k, 0, true); ms := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
  bericht := bericht || jsonb_build_object('laufzeit_ms_testkind', ms);
  select lernender_id into v_gross from schule.versuch group by 1 order by count(*) desc limit 1;
  if v_gross is not null then
    t0 := clock_timestamp(); perform schule.wackelt_analyse(v_gross, 0, true); ms := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
    bericht := bericht || jsonb_build_object('laufzeit_ms_groesstes_kind', ms, 'versuche_groesstes_kind', (select count(*) from schule.versuch where lernender_id = v_gross));
    if ms > 500 then bericht := bericht || jsonb_build_object('warnung', 'Analyse „alles“ braucht über 500 ms'); raise warning 'WW-S3: Analyse „alles“ % ms', ms; end if;
  end if;
  if (bericht->'ohne_thema'->>'laufzeit_ms_300')::numeric > 500 then
    bericht := bericht || jsonb_build_object('warnung_300', 'Analyse mit über 300 offenen Fehlern braucht über 500 ms'); end if;
  if pg_temp.ww3_fe() is distinct from (select ww3_stand.fe from ww3_stand) then fehler := fehler || ('fehler_erledigt nach dem Paket anders als vorher')::text; end if;
  if (select (ww3_stand.n, ww3_stand.m) is distinct from ((select count(*) from schule.versuch), (select coalesce(max(id), 0) from schule.versuch)) from ww3_stand) then fehler := fehler || ('Versuche verändert')::text; end if;
  if (select ww3_stand.b from ww3_stand) is distinct from pg_temp.ww3_bestand() then fehler := fehler || ('Daten im Schema schule nach dem Paket anders als vorher')::text; end if;
  bericht := bericht || jsonb_build_object('stand_vorher', (select stand_vorher from ww3_stand),
                                           'schema_bestehend_gleich', not exists (select 1 from ww3_def where ww3_def.s is distinct from (select ww3_stand.s from ww3_stand)),
                                           'fehler_erledigt_gleich', pg_temp.ww3_fe() = (select ww3_stand.fe from ww3_stand)
                                                                     and not exists (select 1 from ww3_def where ww3_def.o is distinct from (select ww3_stand.o from ww3_stand)),
                                           'fehler_erledigt_zeilen', (select count(*) from schule.fehler_erledigt),
                                           'mit_fehlbild', to_regprocedure('schule.versuch_regelbezug(schule.versuch)') is not null,
                                           'bestand_gleich', (select ww3_stand.b from ww3_stand) = pg_temp.ww3_bestand(),
                                           'fehler', coalesce(array_length(fehler, 1), 0));
  if array_length(fehler, 1) > 0 then raise exception 'WW-S3 ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
  raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): %', bericht::text;
end $p$;
