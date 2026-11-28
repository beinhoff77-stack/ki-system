-- WW-S3 („Was wackelt“, Folgemigration zu WW-S2, das seit 27.11.2026 eingespielt ist; die WW-S2-Datei bleibt unverändert).
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
-- 4. schule.fehler_abhaken: Antwort zusätzlich mit stand, geaendert_ids (versuch_ids, die dieser Aufruf wirklich geändert hat) und beim Markieren
--    markierung_ids (IDs der neu angelegten Zeilen). Der alte Weg „zurueck über versuch_ids“ bleibt (Verträglichkeit), der Client benutzt ihn nicht mehr.
-- 5. schule.wackelt_analyse: auswertung.themen[].besprochen {zuletzt, tage, neu_seit} – ohne 200er-Grenze, nur gültige Markierungen, nur wenn das
--    Thema je besprochen wurde; nullsicher für „ohne Thema“.
-- 6. Feste Typen: mit_tipp immer Boolean; danach_richtig nur noch true oder fehlt (die Zeitpunkte stehen in danach_richtig_am); Analyse und
--    Abhaken melden stand: 3 (fehlt das Feld, läuft am Server noch WW-S2).
-- 7. api.schule_fehler_abhaken: zusätzlich markierung_ids (nur mit zurueck: true, nicht zusammen mit versuch_ids). Rechteprüfung unverändert:
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
       bespr as (select v.thema_id, max(fe.am) zuletzt, count(distinct (fe.am at time zone v_tz)::date) tage
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
                                   'besprochen', (select jsonb_build_object('zuletzt', b.zuletzt, 'tage', b.tage,
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

-- 4. Markieren / Zurücknehmen über versuch_ids (Zurücknehmen so nur noch aus Verträglichkeit; der Client nimmt markierung_ids)
create or replace function schule.fehler_abhaken(p_l bigint, p_ids jsonb, p_zurueck boolean, p_von text)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare n int := 0; z record; v_nicht jsonb := '[]'; v_ids bigint[] := '{}'; v_mids bigint[] := '{}'; v_m bigint;
begin
  for z in select * from schule.ww_versuche(p_l, p_ids) order by 1 loop
    if not z.ok then v_nicht := v_nicht || jsonb_build_object('versuch_id', z.versuch_id, 'grund', z.grund); continue; end if;
    v_m := null;
    if coalesce(p_zurueck, false) then   -- höchstens eine gültige Zeile je Versuch (eindeutiger Teilindex fehler_erledigt_gueltig)
      update schule.fehler_erledigt set zurueckgenommen_am = now(), zurueckgenommen_von = p_von
       where versuch_id = z.versuch_id and lernender_id = p_l and zurueckgenommen_am is null returning id into v_m;
    else
      insert into schule.fehler_erledigt (lernender_id, versuch_id, von) values (p_l, z.versuch_id, p_von)
        on conflict (versuch_id) where zurueckgenommen_am is null do nothing returning id into v_m;
    end if;
    if v_m is not null then n := n + 1; v_ids := v_ids || z.versuch_id; v_mids := v_mids || v_m; end if;
  end loop;
  return jsonb_build_object('ok', true, 'stand', 3, 'geaendert', n, 'geaendert_ids', to_jsonb(v_ids), 'uebersprungen', v_nicht)
         || case when coalesce(p_zurueck, false) then '{}'::jsonb else jsonb_build_object('markierung_ids', to_jsonb(v_mids)) end;
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
  v_ids := array(select distinct (x #>> '{}')::bigint from jsonb_array_elements(p_ids) x order by 1);
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
  return schule.fehler_abhaken(v_l, p_daten->'versuch_ids', v_z, schule.ww_von(p_schluessel));
end $function$;

do $$ begin
  if exists (select 1 from pg_roles where rolname = 'council_mcp') then
    grant execute on function api.schule_wackelt_analyse(text, jsonb), api.schule_fehler_abhaken(text, jsonb) to council_mcp;
  end if;
end $$;
revoke all on function api.schule_wackelt_analyse(text, jsonb), api.schule_fehler_abhaken(text, jsonb) from public, anon, authenticated;
