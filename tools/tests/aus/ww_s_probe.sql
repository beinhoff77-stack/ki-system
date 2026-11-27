-- WW-S2 Einspiel-Paket (erzeugt von tools/tests/wackelt_einspielen.py --probe). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);
create temp table ww_mig on commit drop as select $wwmig$-- WW-S2 („Was wackelt“, Teil Datenbank, schlanke Fassung zu Entwurf 4): Analyse der offenen Fehler und Abhaken – NUR LESEN und Abhaken speichern.
-- Entscheidung des Nutzers (27.11.2026): kein „Nachüben schicken“; Wiederholungs- und Mischkarten, Logik und Ablauf bleiben, wie sie sind.
-- Vorgabe: inhalte/design/wackelt/entwurf4/umsetzung4.md (Darstellung), entwurf3/umsetzung3.md Abschnitte 2 und 3 (Regeln fürs Verschwinden, Datenbedarf).
-- Plan, Antwortformen und Nachweis „Berührt die Lernlogik nicht“: inhalte/plan/wackelt-server.md. Einspielen NUR über tools/tests/wackelt_einspielen.py
-- (eine Transaktion, prüft sich selbst). Unabhängig von RB-S: Ist RB-S eingespielt, kommt die Fehlerart aus dem erkannten Fehlbild
-- (schule.versuch_regelbezug), sonst aus dem groben „grund“ von schule.antwort_bewerten (vorzeichen, komma, vertauscht, gerundet, falsche_einheit) oder sie bleibt leer.
--
-- WAS
-- 1. Tabelle (RLS an, keine Policy, keine Rechte für anon/authenticated; nur über die Funktionen):
--      schule.fehler_erledigt (id, lernender_id, versuch_id, am, von, zurueckgenommen_am, zurueckgenommen_von)  – „Abhaken“ je falscher Antwort
--    Rückgängig = zurueckgenommen_am setzen (kein DELETE). Je Versuch höchstens ein gültiger Eintrag (eindeutiger Teilindex).
--    Die Tabelle wird von KEINER Funktion der Lernlogik gelesen (Karte, Wiederholung, Check-in, Mischkarten, Sterne, Auswahl der nächsten Aufgabe).
-- 2. schule.wackelt_analyse(kind, tage, mit_erledigt) -> jsonb (Form in wackelt-server.md). Regeln (umsetzung3 Abschnitt 2, ohne Nachüben):
--      falsch      = endgültig falsche Antwort (schule.fehler_endgueltig_am, wie LW-S 2) – ein falscher 1. Anlauf mit zweiter Chance zählt nicht
--      offen       = falsch, im Zeitraum (am > jetzt − tage; tage 0/leer = alles), nicht abgehakt
--      Auswertung: Fehler je Thema (offen / alle Antworten im Zeitraum), die letzten 7 Lerntage (richtig/falsch, Tag in der Zeitzone des Kindes),
--      wiederkehrende Fehlerarten (≥ 2 falsche im Zeitraum, mindestens eine offen; höchstens 3), „nur einmal passiert“ (Lernkarten mit genau einem
--      offenen Fehler, dessen Fehlerart nicht wiederkehrt; davon danach richtig). „Danach richtig“ ist nur eine Anzeige (beim Lesen ausgewertet).
--    Schreibt nur in eigene Hilfstabellen dieser Sitzung (pg_temp, on commit drop).
-- 3. schule.fehler_abhaken(kind, versuch_ids, zurueck, von): schreibt ausschließlich schule.fehler_erledigt.
-- 4. Aktionen (api, security definer; Muster api.schule_wackelt_lesen):
--      api.schule_wackelt_analyse {lernender_id, tage?, erledigt?}         nur Eltern/Lehrer
--      api.schule_fehler_abhaken  {lernender_id, versuch_ids[], zurueck?}  nur Eltern/Lehrer
--    Rechte: execute nur für council_mcp (wie die übrigen api.schule_*), revoke von public, anon, authenticated.
--
-- WAS NICHT: keine Änderung an bestehenden Funktionen, Tabellen oder Triggern; kein Schreiben in schule.versuch, schule.karte_stand,
-- schule.misch_ausgabe, schule.lerntag, schule.sterne oder eine andere bestehende Tabelle; kein neuer Trigger (auch kein interner: keine Fremdschlüssel
-- auf bestehende Tabellen); keine neue Regel in schule.regel.
-- Kein UPDATE/DELETE von Bestandsdaten, kein DROP. Kein Nachüben (Entscheidung des Nutzers). Wiederholbar: ein zweiter Lauf ändert nichts.

select set_config('lock_timeout', '3s', true);

do $$ begin
  if to_regprocedure('schule.fehler_endgueltig_am(schule.versuch)') is null or to_regprocedure('schule.zugriff(text, bigint)') is null
     or to_regprocedure('schule.ist_leiter(text)') is null or to_regprocedure('schule.wer_tn(text)') is null
     or to_regprocedure('schule.loesung_sicht(schule.aufgabe)') is null or to_regprocedure('schule.antwort_bewerten(schule.aufgabe, jsonb)') is null
  then raise exception 'WW-S: Voraussetzung fehlt (LW-S, BD-S2, Lern-Zugänge)'; end if;
end $$;

-- 1. Tabelle
create table if not exists schule.fehler_erledigt (
  id bigint generated always as identity primary key,
  lernender_id bigint not null,   -- bewusst OHNE Fremdschlüssel: ein Fremdschlüssel legte interne Trigger an schule.versuch/schule.lernender an
  versuch_id bigint not null,     -- und sperrte schule.versuch beim Anlegen. Zugehörigkeit prüft schule.ww_versuche vor jedem Eintrag.
  am timestamptz not null default now(),
  von text not null,
  zurueckgenommen_am timestamptz,
  zurueckgenommen_von text
);
create unique index if not exists fehler_erledigt_gueltig on schule.fehler_erledigt (versuch_id) where zurueckgenommen_am is null;
create index if not exists fehler_erledigt_kind on schule.fehler_erledigt (lernender_id);
alter table schule.fehler_erledigt enable row level security;   -- nur über die security-definer-Funktionen, wie die übrigen schule-Tabellen
revoke all on table schule.fehler_erledigt from public, anon, authenticated;
comment on table schule.fehler_erledigt is 'WW-S: „Abhaken“ einer falschen Antwort auf der Seite „Was wackelt“ (nur Anzeige für Eltern/Lehrer, ohne Wirkung auf Karte, Wiederholung, Mischkarten); Rückgängig = zurueckgenommen_am';

-- 2. Fehlerart einer falschen Antwort: Fehlbild (RB-S, wenn eingespielt) > grober Grund > leer
create or replace function schule.ww_fehlerart(v schule.versuch, a schule.aufgabe)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare r jsonb; g text;
begin
  if to_regprocedure('schule.versuch_regelbezug(schule.versuch)') is not null then   -- RB-S eingespielt
    begin r := schule.versuch_regelbezug(v); exception when others then r := null; end;
  end if;
  begin g := schule.antwort_bewerten(a, v.antwort)->>'grund'; exception when others then g := null; end;
  return jsonb_strip_nulls(jsonb_build_object(
    'quelle', case when r ? 'fehlbild_nr' then 'fehlbild' when g is not null then 'grund' end,
    'schluessel', case when r ? 'fehlbild' then 'fb:' || (r->>'fehlbild') when r ? 'fehlbild_nr' then 'a:' || a.id || ':' || (r->>'fehlbild_nr')
                       when g is not null then 'g:' || g end,
    'kennung', r->>'fehlbild', 'text', r->>'text', 'fehlbild_regel', r->>'fehlbild_regel', 'regel', r->>'regel', 'grund', g));
end $function$;

create or replace function schule.ww_von(p_schluessel text)
 returns text language sql stable security definer set search_path to ''
as $function$
  select coalesce((select i.rolle || ':' || i.name from schule.lern_ich(p_schluessel) i where schule.ist_lern(p_schluessel)), 'eltern:App');
$function$;

-- 2. Analyse
create or replace function schule.wackelt_analyse(p_l bigint, p_tage integer default 14, p_mit_erledigt boolean default false)
 returns jsonb language plpgsql set search_path to ''   -- volatil nur wegen der Hilfstabellen dieser Sitzung (pg_temp, on commit drop); liest sonst nur
as $function$
declare v_seit timestamptz := case when coalesce(p_tage, 0) <= 0 then null else now() - make_interval(days => p_tage) end;
  v_tz text := coalesce((select l.zeitzone from schule.lernender l where l.id = p_l), 'Europe/Berlin'); r jsonb;
begin
  create temp table if not exists ww_v (ver schule.versuch, auf schule.aufgabe, id bigint, am timestamptz, richtig boolean, hilfe smallint, anlauf smallint,
    aufgabe_id bigint, einheit_id bigint, lz text, thema_id bigint) on commit drop;
  truncate ww_v;   -- nur die Hilfstabelle dieser Sitzung
  insert into ww_v select x, a, x.id, x.am, x.richtig, x.hilfe, x.anlauf, x.aufgabe_id, a.einheit_id, a.variante_gruppe, e.thema_id
    from schule.versuch x join schule.aufgabe a on a.id = x.aufgabe_id join schule.einheit e on e.id = a.einheit_id where x.lernender_id = p_l;
  create temp table if not exists ww_f (id bigint, am timestamptz, aufgabe_id bigint, einheit_id bigint, lz text, thema_id bigint, im_zeitraum boolean,
    abgehakt_am timestamptz, abgehakt_von text, aufgabe_richtig_am timestamptz, lk_richtig_am timestamptz, erst_antwort jsonb, art jsonb, eintrag jsonb) on commit drop;
  truncate ww_f;
  insert into ww_f
  select f.id, f.am, f.aufgabe_id, f.einheit_id, f.lz, f.thema_id, v_seit is null or f.am > v_seit,
         fe.am, fe.von,
         (select min(y.am) from ww_v y where y.aufgabe_id = f.aufgabe_id and y.richtig and (y.am, y.id) > (f.am, f.id)),
         (select min(y.am) from ww_v y where y.einheit_id = f.einheit_id and y.lz = f.lz and y.richtig and coalesce(y.hilfe, 0) = 0 and (y.am, y.id) > (f.am, f.id)),
         case when f.anlauf = 2 then (select (y.ver).antwort from ww_v y where y.aufgabe_id = f.aufgabe_id and y.anlauf = 1 and not y.richtig and y.am <= f.am
                                       order by y.am desc, y.id desc limit 1) end,
         schule.ww_fehlerart(f.ver, f.auf), null
    from ww_v f
    left join schule.fehler_erledigt fe on fe.versuch_id = f.id and fe.zurueckgenommen_am is null
   where not f.richtig and schule.fehler_endgueltig_am(f.ver) is not null;
  update ww_f w set eintrag = jsonb_strip_nulls(jsonb_build_object(
      'versuch_id', w.id, 'am', w.am, 'tag', (w.am at time zone v_tz)::date, 'thema_id', w.thema_id,
      'thema', (select coalesce(t.unterthema, t.schluessel) from schule.thema t where t.id = w.thema_id),
      'einheit_id', w.einheit_id, 'lernziel', w.lz,
      'lernkarte', (select q->>'titel' from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q where e.id = w.einheit_id and q->>'lernziel' = w.lz limit 1),
      'aufgabe', (select jsonb_strip_nulls(jsonb_build_object('id', (v.auf).id, 'antworttyp', (v.auf).antworttyp, 'form', (v.auf).form, 'typ', (v.auf).typ,
                    'stufe', (v.auf).stufe, 'frage', (v.auf).frage, 'antworten', (v.auf).antworten, 'loesung', schule.loesung_sicht(v.auf), 'loesungsweg', (v.auf).loesungsweg))
                    from ww_v v where v.id = w.id),
      'antwort', (select (v.ver).antwort from ww_v v where v.id = w.id), 'erst_antwort', w.erst_antwort,
      'anlauf', (select v.anlauf from ww_v v where v.id = w.id), 'mit_tipp', (select coalesce(v.hilfe, 0) > 0 from ww_v v where v.id = w.id),
      'fehlerart', nullif(w.art, '{}'::jsonb),
      'danach_richtig', nullif(jsonb_strip_nulls(jsonb_build_object('aufgabe_am', w.aufgabe_richtig_am, 'lernkarte_am', w.lk_richtig_am)), '{}'::jsonb),
      'erledigt', case when w.abgehakt_am is not null then jsonb_build_object('art', 'abgehakt', 'am', w.abgehakt_am) end));
  with offen as (select * from ww_f where im_zeitraum and abgehakt_am is null),
       falsch_z as (select * from ww_f where im_zeitraum),
       arten as (select f.art->>'schluessel' s, count(*) n, count(*) filter (where o.id is not null) n_offen,
                        min(f.art->>'kennung') kennung, min(f.art->>'text') text, min(f.art->>'grund') grund,
                        jsonb_agg(distinct f.thema_id) themen, max(f.am) zuletzt
                   from falsch_z f left join offen o on o.id = f.id where f.art ? 'schluessel' group by 1),
       wieder as (select * from arten where n >= 2 and n_offen > 0 order by n desc, zuletzt desc limit 3),
       je_lk as (select einheit_id, lz, count(*) n, min(id) id from offen group by 1, 2),
       einmal as (select o.* from je_lk j join offen o on o.id = j.id where j.n = 1
                    and not exists (select 1 from wieder w where w.s = o.art->>'schluessel'))
  select jsonb_build_object(
    'ok', true, 'lernender_id', p_l, 'tage', coalesce(nullif(p_tage, 0), 0), 'seit', v_seit, 'heute', (now() at time zone v_tz)::date,
    'mit_fehlbild', to_regprocedure('schule.versuch_regelbezug(schule.versuch)') is not null,
    'offen_zahl', (select count(*) from offen),
    'offen', coalesce((select jsonb_agg(o.eintrag order by o.am desc, o.id desc) from (select * from offen order by am desc, id desc limit 300) o), '[]'::jsonb),
    'auswertung', jsonb_build_object(
      'antworten', (select count(*) from ww_v v where v_seit is null or v.am > v_seit),
      'richtig', (select count(*) from ww_v v where (v_seit is null or v.am > v_seit) and v.richtig),
      'themen', coalesce((select jsonb_agg(jsonb_build_object('thema_id', t.thema_id, 'thema', (select coalesce(x.unterthema, x.schluessel) from schule.thema x where x.id = t.thema_id),
                                   'offen', t.offen, 'gesamt', t.gesamt) order by t.offen desc, t.gesamt desc, t.thema_id)
                          from (select v.thema_id, count(*) gesamt, (select count(*) from offen o where o.thema_id = v.thema_id) offen
                                  from ww_v v where v_seit is null or v.am > v_seit group by 1) t), '[]'::jsonb),
      'lerntage', coalesce((select jsonb_agg(jsonb_build_object('tag', d.tag, 'richtig', d.r, 'falsch', d.f) order by d.tag)
                            from (select (v.am at time zone v_tz)::date tag, count(*) filter (where v.richtig) r, count(*) filter (where not v.richtig) f
                                    from ww_v v group by 1 order by 1 desc limit 7) d), '[]'::jsonb),
      'wiederkehrend', coalesce((select jsonb_agg(jsonb_strip_nulls(jsonb_build_object('schluessel', w.s, 'kennung', w.kennung, 'text', w.text, 'grund', w.grund,
                                    'anzahl', w.n, 'offen', w.n_offen, 'themen', w.themen)) order by w.n desc, w.zuletzt desc) from wieder w), '[]'::jsonb),
      'einmal', jsonb_build_object('lernkarten', (select count(*) from einmal), 'danach_richtig', (select count(*) from einmal where lk_richtig_am is not null),
                                   'themen_danach_richtig', coalesce((select jsonb_agg(distinct thema_id) from einmal where lk_richtig_am is not null), '[]'::jsonb))),
    'erledigt', case when p_mit_erledigt then coalesce((select jsonb_agg(f.eintrag order by f.abgehakt_am desc, f.id desc)
                                                         from (select * from ww_f where im_zeitraum and abgehakt_am is not null
                                                                order by abgehakt_am desc, id desc limit 200) f), '[]'::jsonb) end)
    into r;
  return jsonb_strip_nulls(r);
end $function$;
comment on function schule.wackelt_analyse(bigint, integer, boolean) is 'WW-S: offene falsche Antworten eines Kindes im Zeitraum mit Aufgabe, Fehlerart, Folge danach; Auswertung (inhalte/plan/wackelt-server.md). Nur lesend.';

-- 3. Abhaken. Prüfung der übergebenen Versuche (gehören dem Kind, endgültig falsch)
create or replace function schule.ww_versuche(p_l bigint, p_ids jsonb)
 returns table (versuch_id bigint, ok boolean, grund text) language plpgsql stable set search_path to ''
as $function$
begin
  if jsonb_typeof(p_ids) is distinct from 'array' or jsonb_array_length(p_ids) = 0 or jsonb_array_length(p_ids) > 200 then
    raise exception 'versuch_ids: Liste mit 1 bis 200 Einträgen' using errcode = 'P0001'; end if;
  if exists (select 1 from jsonb_array_elements(p_ids) x where jsonb_typeof(x) not in ('number', 'string') or (x #>> '{}') !~ '^\d{1,18}$') then
    raise exception 'versuch_ids: nur Zahlen' using errcode = 'P0001'; end if;
  return query
    select i.id, v.id is not null and not v.richtig and schule.fehler_endgueltig_am(v) is not null,
           case when v.id is null then 'nicht gefunden' when v.richtig then 'richtig' when schule.fehler_endgueltig_am(v) is null then 'nicht endgültig falsch' end
      from (select distinct (x #>> '{}')::bigint id from jsonb_array_elements(p_ids) x) i
      left join schule.versuch v on v.id = i.id and v.lernender_id = p_l;
end $function$;

create or replace function schule.fehler_abhaken(p_l bigint, p_ids jsonb, p_zurueck boolean, p_von text)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare n int := 0; c int; z record; v_nicht jsonb := '[]';
begin
  for z in select * from schule.ww_versuche(p_l, p_ids) loop
    if not z.ok then v_nicht := v_nicht || jsonb_build_object('versuch_id', z.versuch_id, 'grund', z.grund); continue; end if;
    if coalesce(p_zurueck, false) then
      update schule.fehler_erledigt set zurueckgenommen_am = now(), zurueckgenommen_von = p_von
       where versuch_id = z.versuch_id and lernender_id = p_l and zurueckgenommen_am is null;
    else
      insert into schule.fehler_erledigt (lernender_id, versuch_id, von) values (p_l, z.versuch_id, p_von)
        on conflict (versuch_id) where zurueckgenommen_am is null do nothing;
    end if;
    get diagnostics c = row_count; n := n + c;
  end loop;
  return jsonb_build_object('ok', true, 'geaendert', n, 'uebersprungen', v_nicht);
end $function$;

revoke all on function schule.ww_fehlerart(schule.versuch, schule.aufgabe), schule.ww_von(text), schule.wackelt_analyse(bigint, integer, boolean),
  schule.ww_versuche(bigint, jsonb), schule.fehler_abhaken(bigint, jsonb, boolean, text)
  from public, anon, authenticated;

-- 4. Aktionen
create or replace function api.schule_wackelt_analyse(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint; v_t int := coalesce(nullif(p_daten->>'tage', '')::int, 14);
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  perform schule.zugriff(p_schluessel, v_l);
  if not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  if v_t not in (0, 7, 14) then raise exception 'tage: 7, 14 oder 0 (alles)' using errcode = 'P0001'; end if;
  return schule.wackelt_analyse(v_l, v_t, coalesce((p_daten->>'erledigt')::boolean, false));
end $function$;

create or replace function api.schule_fehler_abhaken(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  perform schule.zugriff(p_schluessel, v_l);
  if not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return schule.fehler_abhaken(v_l, p_daten->'versuch_ids', coalesce((p_daten->>'zurueck')::boolean, false), schule.ww_von(p_schluessel));
end $function$;

do $$ begin
  if exists (select 1 from pg_roles where rolname = 'council_mcp') then
    grant execute on function api.schule_wackelt_analyse(text, jsonb), api.schule_fehler_abhaken(text, jsonb) to council_mcp;
  end if;
end $$;
revoke all on function api.schule_wackelt_analyse(text, jsonb), api.schule_fehler_abhaken(text, jsonb) from public, anon, authenticated;
$wwmig$::text as sql;
-- Fingerabdruck des Bestehenden: Funktionen in schule/api (ohne die neuen), alle Trigger (auch interne) an Tabellen in schule, Spalten (ohne fehler_erledigt)
create function pg_temp.ww_schema() returns text language sql stable as $f$
  select md5(string_agg(x, '#' order by x)) from (
    select 'f:' || p.oid::regprocedure::text || ':' || pg_get_functiondef(p.oid) x from pg_proc p
     where p.pronamespace in ('schule'::regnamespace, 'api'::regnamespace) and p.prokind in ('f', 'p')
       and p.oid not in (select o from (select to_regprocedure(f) o from unnest(array['schule.ww_fehlerart(schule.versuch, schule.aufgabe)', 'schule.ww_von(text)', 'schule.wackelt_analyse(bigint, integer, boolean)', 'schule.ww_versuche(bigint, jsonb)', 'schule.fehler_abhaken(bigint, jsonb, boolean, text)', 'api.schule_wackelt_analyse(text, jsonb)', 'api.schule_fehler_abhaken(text, jsonb)']) f) q where o is not null)
    union all select 't:' || t.tgrelid::regclass::text || ':' || t.tgname || ':' || t.tgisinternal::text || ':' || pg_get_triggerdef(t.oid)
      from pg_trigger t join pg_class c on c.oid = t.tgrelid where c.relnamespace = 'schule'::regnamespace
    union all select 'c:' || a.attrelid::regclass::text || ':' || a.attname || ':' || format_type(a.atttypid, a.atttypmod)
      from pg_attribute a join pg_class c on c.oid = a.attrelid
     where c.relnamespace = 'schule'::regnamespace and c.relkind in ('r', 'p', 'v') and a.attnum > 0 and not a.attisdropped
       and c.oid is distinct from to_regclass('schule.fehler_erledigt')) s $f$;
-- Fingerabdruck aller Daten im Schema schule außer schule.fehler_erledigt (Versuche, Karten, Wiederholung, Mischkarten, Lerntage, Sterne, Regeln …)
create function pg_temp.ww_bestand() returns text language plpgsql as $f$
declare t regclass; h text; a text := '';
begin
  for t in select c.oid::regclass from pg_class c where c.relnamespace = 'schule'::regnamespace and c.relkind in ('r', 'p')
              and c.oid is distinct from to_regclass('schule.fehler_erledigt') order by c.oid::regclass::text loop
    execute format('select md5(coalesce(string_agg(x::text, %L order by x::text), %L)) from %s x', '|', '', t) into h;
    a := a || t::text || '=' || h || ';';
  end loop;
  return md5(a);
end $f$;
create temp table ww_stand on commit drop as select (select count(*) from schule.versuch) n, (select coalesce(max(id), 0) from schule.versuch) m,
  pg_temp.ww_schema() s, pg_temp.ww_bestand() b;
do $p$ begin execute (select sql from ww_mig); end $p$;
create temp table ww_def on commit drop as select 1 lauf, (select md5(string_agg(coalesce(pg_get_functiondef(to_regprocedure(f)), 'fehlt'), '#' order by f)) from unnest(array['schule.ww_fehlerart(schule.versuch, schule.aufgabe)', 'schule.ww_von(text)', 'schule.wackelt_analyse(bigint, integer, boolean)', 'schule.ww_versuche(bigint, jsonb)', 'schule.fehler_abhaken(bigint, jsonb, boolean, text)', 'api.schule_wackelt_analyse(text, jsonb)', 'api.schule_fehler_abhaken(text, jsonb)']) f) d, (select md5(string_agg(s.x, '#' order by s.x)) from (
       select 'idx:' || indexrelid::regclass::text || pg_get_indexdef(indexrelid) from pg_index where indrelid = 'schule.fehler_erledigt'::regclass
       union all select 'col:' || attrelid::regclass::text || attname || format_type(atttypid, atttypmod) from pg_attribute where attrelid = 'schule.fehler_erledigt'::regclass and attnum > 0
       union all select 'rls:' || relrowsecurity::text || coalesce(obj_description(oid, 'pg_class'), '') from pg_class where oid = 'schule.fehler_erledigt'::regclass) s(x)) o, pg_temp.ww_schema() s;
do $p$ begin execute (select sql from ww_mig); end $p$;
insert into ww_def select 2, (select md5(string_agg(coalesce(pg_get_functiondef(to_regprocedure(f)), 'fehlt'), '#' order by f)) from unnest(array['schule.ww_fehlerart(schule.versuch, schule.aufgabe)', 'schule.ww_von(text)', 'schule.wackelt_analyse(bigint, integer, boolean)', 'schule.ww_versuche(bigint, jsonb)', 'schule.fehler_abhaken(bigint, jsonb, boolean, text)', 'api.schule_wackelt_analyse(text, jsonb)', 'api.schule_fehler_abhaken(text, jsonb)']) f), (select md5(string_agg(s.x, '#' order by s.x)) from (
       select 'idx:' || indexrelid::regclass::text || pg_get_indexdef(indexrelid) from pg_index where indrelid = 'schule.fehler_erledigt'::regclass
       union all select 'col:' || attrelid::regclass::text || attname || format_type(atttypid, atttypmod) from pg_attribute where attrelid = 'schule.fehler_erledigt'::regclass and attnum > 0
       union all select 'rls:' || relrowsecurity::text || coalesce(obj_description(oid, 'pg_class'), '') from pg_class where oid = 'schule.fehler_erledigt'::regclass) s(x)), pg_temp.ww_schema();
create function pg_temp.ww_ant(p_k bigint, p_id bigint, p_wert text, p_cid text) returns jsonb language plpgsql as $f$
begin
  return schule.uebung_pruefen_wd(p_k, jsonb_build_object('aufgabe_id', p_id, 'client_id', p_cid, 'antwort', jsonb_build_object('wert', p_wert)));
end $f$;
create function pg_temp.ww_ids(r jsonb, p text) returns bigint[] language sql immutable as $f$
  select coalesce(array_agg((e->>'versuch_id')::bigint), '{}') from jsonb_array_elements(coalesce(r->p, '[]'::jsonb)) e $f$;
do $p$
declare
  fehler text[] := '{}'; k bigint := (select id from schule.lernender where ist_test order by id limit 1); v_e bigint; v_lz text; a1 schule.aufgabe; a2 schule.aufgabe; v1 bigint; v2 bigint; r jsonb; x text;
  bericht jsonb := '{}'; t0 timestamptz; ms numeric; v_f bigint; v_gross bigint; s_kind text; s_fremd text; s_eltern text; s_lehrer text; v_id bigint;
  kn jsonb; ko jsonb; kz jsonb; h0 text; v0 bigint;
begin
  if (select count(distinct ww_def.d) from ww_def) <> 1 or (select count(distinct ww_def.o) from ww_def) <> 1 then fehler := fehler || ('zweiter Lauf hat etwas geändert')::text; end if;
  if exists (select 1 from ww_def where ww_def.s is distinct from (select ww_stand.s from ww_stand)) then
    fehler := fehler || ('Migration ändert bestehende Funktionen, Trigger oder Spalten')::text; end if;
  -- Rechte
  if not (select relrowsecurity from pg_class where oid = 'schule.fehler_erledigt'::regclass) then fehler := fehler || ('fehler_erledigt: RLS aus')::text; end if;
  if exists (select 1 from pg_policy where polrelid = 'schule.fehler_erledigt'::regclass) then fehler := fehler || ('fehler_erledigt: hat eine Policy')::text; end if;
  if has_table_privilege('anon', 'schule.fehler_erledigt', 'select') or has_table_privilege('authenticated', 'schule.fehler_erledigt', 'select')
     or has_table_privilege('authenticated', 'schule.fehler_erledigt', 'insert') then fehler := fehler || ('fehler_erledigt: App-Rollen haben Rechte')::text; end if;
  if exists (select 1 from pg_constraint where contype = 'f' and (conrelid = 'schule.fehler_erledigt'::regclass or confrelid = 'schule.fehler_erledigt'::regclass)) then
    fehler := fehler || ('fehler_erledigt: Fremdschlüssel (legte Trigger an bestehenden Tabellen an)')::text; end if;
  for x in select unnest(array['schule.ww_fehlerart(schule.versuch, schule.aufgabe)', 'schule.ww_von(text)', 'schule.wackelt_analyse(bigint, integer, boolean)', 'schule.ww_versuche(bigint, jsonb)', 'schule.fehler_abhaken(bigint, jsonb, boolean, text)', 'api.schule_wackelt_analyse(text, jsonb)', 'api.schule_fehler_abhaken(text, jsonb)']) loop
    if has_function_privilege('anon', x, 'execute') or has_function_privilege('authenticated', x, 'execute') then fehler := fehler || (x || ': für App-Rollen aufrufbar')::text; end if;
  end loop;
  for x in select unnest(array['api.schule_wackelt_analyse(text, jsonb)', 'api.schule_fehler_abhaken(text, jsonb)']) loop
    if position('if not schule.ist_leiter(p_schluessel) then raise exception' in pg_get_functiondef(x::regprocedure)) = 0 then fehler := fehler || (x || ': prüft ist_leiter nicht')::text; end if;
  end loop;
  if exists (select 1 from pg_proc p where p.pronamespace in ('schule'::regnamespace, 'api'::regnamespace) and p.proname like '%nachueb%') then
    fehler := fehler || ('Nachüben-Funktion vorhanden (gehört nicht zu WW-S2)')::text; end if;
  begin
    r := api.schule_wackelt_analyse('ww-unbekannter-schluessel', jsonb_build_object('lernender_id', k));
    fehler := fehler || ('unbekannter Schlüssel bekommt eine Analyse')::text;
  exception when others then null;
  end;
  -- Lernkarte mit mindestens drei zählenden Zahl-Aufgaben
  select x2.einheit_id, x2.variante_gruppe into v_e, v_lz from schule.aufgabe x2 join schule.einheit e on e.id = x2.einheit_id
   where x2.pool = 'uebung' and x2.freigegeben and e.status = 'freigegeben' and x2.antworttyp = 'zahl' and schule.aufgabe_zaehlt(x2)
     and (x2.loesung->>'wert')::numeric <> 987654 and x2.loesung->>'einheit' is null
   group by 1, 2 having count(*) >= 3 order by 1, 2 limit 1;
  if k is null or v_e is null then raise exception 'WW-S: Testkind oder Lernkarte mit drei Zahl-Aufgaben fehlt'; end if;
  select * into a1 from schule.aufgabe where einheit_id = v_e and variante_gruppe = v_lz and pool = 'uebung' and antworttyp = 'zahl' and freigegeben and loesung->>'einheit' is null order by id limit 1;
  select * into a2 from schule.aufgabe where einheit_id = v_e and variante_gruppe = v_lz and pool = 'uebung' and antworttyp = 'zahl' and freigegeben and loesung->>'einheit' is null and id > a1.id order by id limit 1;
  -- 2. Analyse und Abhaken; dabei bleibt jede andere Tabelle in schule bytegleich
  begin
    perform pg_temp.ww_ant(k, a1.id, '987654', 'ww-1');
    perform pg_temp.ww_ant(k, a2.id, '987654', 'ww-2');
    select id into v1 from schule.versuch where lernender_id = k and client_id = 'ww-1';
    select id into v2 from schule.versuch where lernender_id = k and client_id = 'ww-2';
    h0 := pg_temp.ww_bestand();
    r := schule.wackelt_analyse(k, 14, true);
    if not (array[v1, v2] <@ pg_temp.ww_ids(r, 'offen')) then fehler := fehler || ('Analyse: falsche Antworten nicht offen: ' || left(r::text, 300))::text; end if;
    if (select e->'aufgabe'->'loesung' is null or e->>'lernziel' is distinct from v_lz or e->>'tag' is null from jsonb_array_elements(r->'offen') e where (e->>'versuch_id')::bigint = v1) then
      fehler := fehler || ('Analyse: Eintrag unvollständig')::text; end if;
    if exists (select 1 from jsonb_array_elements(r->'offen') e where e ? 'nachueben') then fehler := fehler || ('Analyse liefert noch nachueben')::text; end if;
    if not exists (select 1 from jsonb_array_elements(r->'auswertung'->'themen') t where (t->>'offen')::int >= 2) then fehler := fehler || ('Auswertung je Thema fehlt')::text; end if;
    if jsonb_array_length(r->'auswertung'->'lerntage') = 0 then fehler := fehler || ('Lerntage fehlen')::text; end if;
    if not (r->'auswertung' ? 'wiederkehrend' and r->'auswertung' ? 'einmal') then fehler := fehler || ('Auswertung: wiederkehrend/einmal fehlt')::text; end if;
    bericht := bericht || jsonb_build_object('mit_fehlbild', r->'mit_fehlbild', 'offen_zahl', r->'offen_zahl',
                 'beispiel', (select e - 'aufgabe' - 'antwort' from jsonb_array_elements(r->'offen') e where (e->>'versuch_id')::bigint = v1));
    -- Abhaken, zweimal, Rückgängig, fremde Versuche
    r := schule.fehler_abhaken(k, jsonb_build_array(v1), false, 'probe');
    if (r->>'geaendert')::int <> 1 then fehler := fehler || ('Abhaken: ' || r::text)::text; end if;
    if (schule.fehler_abhaken(k, jsonb_build_array(v1), false, 'probe')->>'geaendert')::int <> 0 then fehler := fehler || ('zweites Abhaken ändert etwas')::text; end if;
    r := schule.wackelt_analyse(k, 14, true);
    if v1 = any(pg_temp.ww_ids(r, 'offen')) or not v1 = any(pg_temp.ww_ids(r, 'erledigt')) then fehler := fehler || ('abgehakte Antwort noch offen oder nicht erledigt')::text; end if;
    if (select e->'erledigt'->>'art' from jsonb_array_elements(r->'erledigt') e where (e->>'versuch_id')::bigint = v1) is distinct from 'abgehakt' then fehler := fehler || ('erledigt.art nicht abgehakt')::text; end if;
    if pg_temp.ww_bestand() is distinct from h0 then fehler := fehler || ('Analyse/Abhaken verändert Daten außerhalb von fehler_erledigt')::text; end if;
    if (schule.fehler_abhaken(k, jsonb_build_array(v1), true, 'probe')->>'geaendert')::int <> 1 then fehler := fehler || ('Rückgängig ändert nichts')::text; end if;
    if not v1 = any(pg_temp.ww_ids(schule.wackelt_analyse(k, 14, false), 'offen')) then fehler := fehler || ('nach Rückgängig nicht wieder offen')::text; end if;
    r := schule.fehler_abhaken(k, jsonb_build_array(0, coalesce((select min(id) from schule.versuch where lernender_id <> k), 0)), false, 'probe');
    if (r->>'geaendert')::int <> 0 or jsonb_array_length(r->'uebersprungen') = 0 then fehler := fehler || ('fremde Versuche abgehakt: ' || r::text)::text; end if;
    begin perform schule.fehler_abhaken(k, '[1.5]'::jsonb, false, 'probe'); fehler := fehler || ('Kommazahl als versuch_id angenommen')::text;
    exception when others then if position('versuch_ids' in sqlerrm) = 0 then fehler := fehler || ('Kommazahl: falscher Fehler ' || sqlerrm)::text; end if; end;
    if pg_temp.ww_bestand() is distinct from h0 then fehler := fehler || ('Rückgängig verändert Daten außerhalb von fehler_erledigt')::text; end if;
    bericht := bericht || jsonb_build_object('bestand_gleich_beim_abhaken', pg_temp.ww_bestand() = h0);
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then fehler := fehler || ('Prüfblock: ' || sqlerrm)::text;
  end;

  -- 3. Lesevarianten mit echten Lern-Schlüsseln (Logins und Sitzungen nur in dieser Untertransaktion): Kind, fremdes Kind, Eltern, Lehrer
  select id into v_f from schule.lernender where id <> k and aktiv order by id limit 1;
  begin
    insert into schule.lern_login (name, rolle, lernender_id, code_hash) values ('WW-Probe Kind', 'kind', k, md5('ww-k' || clock_timestamp()::text)) returning id into v_id;
    s_kind := md5('ww-sk' || clock_timestamp()::text); insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (s_kind, v_id, now() + interval '1 hour'); s_kind := 'lern:' || s_kind;
    insert into schule.lern_login (name, rolle, lernender_id, code_hash) values ('WW-Probe Eltern', 'eltern', null, md5('ww-e' || clock_timestamp()::text)) returning id into v_id;
    s_eltern := md5('ww-se' || clock_timestamp()::text); insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (s_eltern, v_id, now() + interval '1 hour'); s_eltern := 'lern:' || s_eltern;
    insert into schule.lern_login (name, rolle, lernender_id, code_hash) values ('WW-Probe Lehrer', 'lehrer', null, md5('ww-l' || clock_timestamp()::text)) returning id into v_id;
    s_lehrer := md5('ww-sl' || clock_timestamp()::text); insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (s_lehrer, v_id, now() + interval '1 hour'); s_lehrer := 'lern:' || s_lehrer;
    if v_f is not null then
      insert into schule.lern_login (name, rolle, lernender_id, code_hash) values ('WW-Probe Fremd', 'kind', v_f, md5('ww-f' || clock_timestamp()::text)) returning id into v_id;
      s_fremd := md5('ww-sf' || clock_timestamp()::text); insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (s_fremd, v_id, now() + interval '1 hour'); s_fremd := 'lern:' || s_fremd;
    end if;
    perform pg_temp.ww_ant(k, a1.id, '987654', 'ww-api');
    select id into v0 from schule.versuch where lernender_id = k and client_id = 'ww-api';
    h0 := pg_temp.ww_bestand();
    -- Kind: keine Analyse, kein Abhaken – auch nicht für sich selbst
    begin r := api.schule_wackelt_analyse(s_kind, jsonb_build_object('lernender_id', k)); fehler := fehler || ('Kind liest die Analyse')::text;
    exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then fehler := fehler || ('Kind/Analyse: falscher Fehler ' || sqlerrm)::text; end if; end;
    begin r := api.schule_fehler_abhaken(s_kind, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0))); fehler := fehler || ('Kind hakt ab')::text;
    exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then fehler := fehler || ('Kind/Abhaken: falscher Fehler ' || sqlerrm)::text; end if; end;
    if v_f is not null then
      begin r := api.schule_wackelt_analyse(s_fremd, jsonb_build_object('lernender_id', k)); fehler := fehler || ('fremdes Kind liest die Analyse')::text;
      exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then fehler := fehler || ('Fremdkind/Analyse: falscher Fehler ' || sqlerrm)::text; end if; end;
      begin r := api.schule_fehler_abhaken(s_fremd, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0))); fehler := fehler || ('fremdes Kind hakt ab')::text;
      exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then fehler := fehler || ('Fremdkind/Abhaken: falscher Fehler ' || sqlerrm)::text; end if; end;
    else bericht := bericht || '{"hinweis_fremdkind": "kein zweites aktives Kind – Fremdkind-Probe übersprungen"}'::jsonb;
    end if;
    if exists (select 1 from schule.fehler_erledigt) then fehler := fehler || ('Kind-Sitzung hat etwas abgehakt')::text; end if;
    r := api.schule_wackelt_analyse(s_eltern, jsonb_build_object('lernender_id', k, 'tage', 0));
    if r->>'ok' is distinct from 'true' then fehler := fehler || ('Eltern lesen die Analyse nicht')::text; end if;
    r := api.schule_wackelt_analyse(s_lehrer, jsonb_build_object('lernender_id', k, 'tage', 7));
    if r->>'ok' is distinct from 'true' then fehler := fehler || ('Lehrer lesen die Analyse nicht')::text; end if;
    r := api.schule_fehler_abhaken(s_eltern, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0)));
    if (r->>'geaendert')::int <> 1 then fehler := fehler || ('Eltern haken nicht ab: ' || r::text)::text; end if;
    if (select von from schule.fehler_erledigt where versuch_id = v0 and zurueckgenommen_am is null) is distinct from 'eltern:WW-Probe Eltern' then fehler := fehler || ('von falsch')::text; end if;
    r := api.schule_fehler_abhaken(s_lehrer, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0), 'zurueck', true));
    if (r->>'geaendert')::int <> 1 then fehler := fehler || ('Lehrer nehmen das Abhaken nicht zurück: ' || r::text)::text; end if;
    begin r := api.schule_wackelt_analyse(s_eltern, jsonb_build_object('lernender_id', k, 'tage', 3)); fehler := fehler || ('tage 3 angenommen')::text;
    exception when others then if position('tage' in sqlerrm) = 0 then fehler := fehler || ('tage: falscher Fehler ' || sqlerrm)::text; end if; end;
    begin r := api.schule_wackelt_analyse('lern:ww-gibt-es-nicht', jsonb_build_object('lernender_id', k)); fehler := fehler || ('unbekannte Sitzung liest die Analyse')::text;
    exception when others then null; end;
    begin r := api.schule_fehler_abhaken('lern:ww-gibt-es-nicht', jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0))); fehler := fehler || ('unbekannte Sitzung hakt ab')::text;
    exception when others then null; end;
    if pg_temp.ww_bestand() is distinct from h0 then fehler := fehler || ('api-Aktionen verändern Daten außerhalb von fehler_erledigt')::text; end if;
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then fehler := fehler || ('Lesevarianten: ' || sqlerrm)::text;
  end;
  -- 4. Abhaken an einer sitzenden, nicht fälligen Lernkarte: Kartenzeile nach dem Abhaken unverändert; ein weiterer Fehler wirkt wie ohne Abhaken
  --    (beide Läufe in eigenen Untertransaktionen vom selben Ausgangsstand; beobachtete Zustände im Bericht)
  if to_regclass('schule.karte_stand') is not null then
    for i in 1 .. 2 loop
      begin
        insert into schule.karte_stand (lernender_id, einheit_id, lernziel) values (k, v_e, v_lz) on conflict do nothing;
        update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '10 days', wdh_stufe = 2, wdh_fehler = 0, wdh_ab = now(), wdh_lerntage = 7,
               faellig_am = now() + interval '7 days' where lernender_id = k and einheit_id = v_e and lernziel = v_lz;
        perform pg_temp.ww_ant(k, a1.id, '987654', 'ww-k0');    -- erster Fehler an der sitzenden Karte
        execute 'select to_jsonb(x) from schule.karte_stand x where x.lernender_id = $1 and x.einheit_id = $2 and x.lernziel = $3' into ko using k, v_e, v_lz;
        if i = 1 then   -- mit Abhaken
          h0 := pg_temp.ww_bestand();
          r := schule.fehler_abhaken(k, jsonb_build_array((select id from schule.versuch where lernender_id = k and client_id = 'ww-k0')), false, 'probe');
          if (r->>'geaendert')::int <> 1 then fehler := fehler || ('Karte: Abhaken ' || r::text)::text; end if;
          execute 'select to_jsonb(x) from schule.karte_stand x where x.lernender_id = $1 and x.einheit_id = $2 and x.lernziel = $3' into kz using k, v_e, v_lz;
          if kz is distinct from ko then fehler := fehler || ('Karte: Abhaken ändert die Kartenzeile')::text; end if;
          if pg_temp.ww_bestand() is distinct from h0 then fehler := fehler || ('Karte: Abhaken ändert Daten außerhalb von fehler_erledigt')::text; end if;
        end if;
        r := pg_temp.ww_ant(k, a2.id, '987654', 'ww-k' || i);   -- zweiter Fehler an derselben Lernkarte
        if r->>'richtig' is distinct from 'false' then fehler := fehler || ('Karte: Fehlantwort nicht als falsch bewertet ' || r::text)::text; end if;
        execute 'select to_jsonb(x) from schule.karte_stand x where x.lernender_id = $1 and x.einheit_id = $2 and x.lernziel = $3' into r using k, v_e, v_lz;
        kn := coalesce(kn, '{}'::jsonb) || jsonb_build_object(case i when 1 then 'mit_abhaken' else 'ohne_abhaken' end,
                jsonb_build_object('nach_1_fehler', jsonb_build_object('sitzt', ko->'sitzt', 'wdh_fehler', ko->'wdh_fehler'),
                                   'nach_2_fehler', jsonb_build_object('sitzt', r->'sitzt', 'wdh_fehler', r->'wdh_fehler', 'geoeffnet', r->'geoeffnet_am' <> 'null'::jsonb),
                                   'zeile', r - 'zuletzt' - 'geoeffnet_am' - 'gezaehlt' - 'sitzt_am' - 'wdh_ab' - 'faellig_am'));
        raise exception using errcode = 'WW999', message = 'zurueck';
      exception when sqlstate 'WW999' then null;
        when others then fehler := fehler || ('Karte (' || i || '): ' || sqlerrm)::text;
      end;
    end loop;
    if kn->'mit_abhaken'->'zeile' is distinct from kn->'ohne_abhaken'->'zeile' then fehler := fehler || ('Abhaken wirkt auf die Karte: ' || kn::text)::text; end if;
    bericht := bericht || jsonb_build_object('karte_abhaken_ohne_wirkung', jsonb_build_object('mit_abhaken', (kn->'mit_abhaken') - 'zeile', 'ohne_abhaken', (kn->'ohne_abhaken') - 'zeile'));
  end if;
  -- Laufzeit der Analyse „alles“ (Testkind und das Kind mit den meisten Versuchen; nur die Zeit wird berichtet)
  t0 := clock_timestamp(); perform schule.wackelt_analyse(k, 0, true); ms := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
  bericht := bericht || jsonb_build_object('laufzeit_ms_testkind', ms);
  select lernender_id into v_gross from schule.versuch group by 1 order by count(*) desc limit 1;
  if v_gross is not null then
    t0 := clock_timestamp(); perform schule.wackelt_analyse(v_gross, 0, true); ms := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
    bericht := bericht || jsonb_build_object('laufzeit_ms_groesstes_kind', ms, 'versuche_groesstes_kind', (select count(*) from schule.versuch where lernender_id = v_gross));
    if ms > 500 then bericht := bericht || jsonb_build_object('warnung', 'Analyse „alles“ braucht über 500 ms'); raise warning 'WW-S: Analyse „alles“ % ms', ms; end if;
  end if;
  if exists (select 1 from schule.fehler_erledigt) then fehler := fehler || ('neue Tabelle nicht leer')::text; end if;
  if (select (n, m) is distinct from ((select count(*) from schule.versuch), (select coalesce(max(id), 0) from schule.versuch)) from ww_stand) then fehler := fehler || ('Versuche verändert')::text; end if;
  if (select ww_stand.b from ww_stand) is distinct from pg_temp.ww_bestand() then fehler := fehler || ('Daten im Schema schule nach dem Paket anders als vorher')::text; end if;
  bericht := bericht || jsonb_build_object('schema_bestehend_gleich', not exists (select 1 from ww_def where ww_def.s is distinct from (select ww_stand.s from ww_stand)),
                                           'bestand_gleich', (select ww_stand.b from ww_stand) = pg_temp.ww_bestand(),
                                           'fehler', coalesce(array_length(fehler, 1), 0));
  if array_length(fehler, 1) > 0 then raise exception 'WW-S ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
  raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): %', bericht::text;
end $p$;
