-- ADVENT-S PROBELAUF (rollt am Ende ALLES zurück, nichts eingespielt). Erzeugt von tools/tests/advent_pakete.py aus 20261209_advent_s.sql.
-- Ein Aufruf, eine Transaktion. Bericht = die abschließende Fehlermeldung: erste Zeile „… bestanden|NICHT bestanden … KURZ {…}“, dann BEFUNDE, HINWEISE, DETAILS.
-- ADVENT-S: Adventskalender (Server). Vorgaben: inhalte/design/advent/entwurf1/konzept.md, umsetzung1.md, entwurf2/grafik-bericht.md, stil.md und die
-- verbindlichen Entscheidungen des Auftraggebers vom 28.11.2026 (stehen in inhalte/design/advent/server.md, Abschnitt 1). Schnittstelle für die App: server.md.
--
-- WAS (nur Zusätze):
--   Tabellen (RLS an, keine Rechte für public/anon/authenticated, KEIN Fremdschlüssel auf eine bestehende Tabelle – kein interner Trigger, keine Sperre
--   auf Bestandstabellen beim Anlegen):
--     schule.advent_teilnahme  wer mitmacht (je Jahr), Familie ('familie' bzw. 'test' fürs Testkind) – Grundlage für den Tausch
--     schule.advent_belegung   Inhalt je Kind und Tür (Art, Variante, Titel, Text, Sterne 0–5000, Motiv-Schlüssel) – nur Eltern lesen/schreiben
--     schule.advent_tuer       geöffnete Türchen: Tag (Ortszeit), Zeitpunkt, auslösende Etappe (Einheit, Lernziel, Landezeit), Schnappschuss des Inhalts
--     schule.advent_gutschein  Gutscheine, Tauschkarten, Krampus-Aufgaben aus geöffneten Türchen; Zustand mit wer/wann
--     schule.advent_tausch     Tausch-Protokoll
--     schule.advent_protokoll  alles, was Kinder und Eltern tun (für die Eltern)
--   Regeln in schule.regel (neu angelegt; eine schon vorhandene advent_*-Regel bricht in der Vorprüfung ab):
--     advent_aktiv 0 (0 aus | 1 an | 2 nur Testkind), advent_start "2026-12-01", advent_nachholen_bis "2027-01-06", advent_sichtbar_bis "2027-01-06",
--     advent_max_pro_tag 2, advent_tausch 0 (0 aus | 1 an)
--   Funktionen schule.advent_* (intern) und 11 Aktionen api.schule_advent_* (security definer, search_path '', execute nur für council_mcp).
--   Prüfregel schule.sterne.sterne_grund_check um 'advent' erweitert (genau die bisherige Definition, sonst Abbruch).
--   Sterne beim Öffnen: insert into schule.sterne (…, 'advent', 'advent:<jahr>:<nr>') on conflict do nothing – genau einmal je Kind und Tür.
-- WAS NICHT: keine Änderung an bestehenden Funktionen, Triggern oder Daten; die Etappe wird nur GELESEN (schule.karte_stand: sitzt, sitzt_am,
--   landung_art, landung.am – eine eigene Landung oder „Sitzt wieder!“ nach dem Nachbessern, siehe schule.advent_landungen).
-- NUR AUF LEEREM AUSGANGSZUSTAND (Urteil 1215, Auflage 3): Gibt es schon irgendein Advent-Objekt (Tabelle/Index/Folge schule.advent_*, Funktion
--   schule.advent_* oder api.schule_advent_*, Regel advent_*, 'advent' in sterne_grund_check), bricht der Lauf mit Liste ab, nichts geändert – kein
--   Weiterlaufen auf einem Mischstand. Ein zweiter Lauf bricht deshalb ebenso ab. Fehlende Voraussetzung oder andere Prüfregel -> Abbruch.
-- Ein Aufruf, eine Transaktion, kein BEGIN/COMMIT. Keine Lernpause nötig (nur neue Objekte; die Prüfregel wird zuletzt ersetzt, Sperre auf schule.sterne
-- nur bis zum Ende dieser kurzen Transaktion; wartet sie länger als lock_timeout, bricht alles ab, nichts geändert, und kann wiederholt werden).
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);

-- ---------- 0. Vorzustand ----------
do $advent_vor$
declare f text[] := '{}'; d text; x record; v_da text[];
  v_alt constant text := $a$CHECK ((grund = ANY (ARRAY['uebung'::text, 'test'::text, 'ort'::text, 'einloesung'::text, 'korrektur_hand'::text, 'bonus'::text, 'expedition'::text, 'wdh'::text, 'etappe_abgelegt'::text, 'flug_abgelegt'::text, 'landung'::text])))$a$;
begin
  foreach d in array array['schule.zugriff(text, bigint)', 'schule.ist_eltern(text)', 'schule.ist_lern(text)', 'schule.lern_ich(text)', 'schule.wer_tn(text)'] loop
    if to_regprocedure(d) is null then f := f || ('Funktion fehlt: ' || d); end if;
  end loop;
  foreach d in array array['schule.lernender', 'schule.regel', 'schule.sterne', 'schule.karte_stand'] loop
    if to_regclass(d) is null then f := f || ('Tabelle fehlt: ' || d); end if;
  end loop;
  if array_length(f, 1) > 0 then raise exception 'ADVENT-S ABBRUCH (Voraussetzung), nichts geändert: %', array_to_string(f, ' | '); end if;
  -- Schon ein Advent-Objekt da? -> Abbruch. Eingespielt wird nur auf leerem Ausgangszustand (kein Wiederanlauf auf einem Mischstand).
  select coalesce(array_agg(q.o order by q.o collate "C"), '{}') into v_da from (
    select format('schule.%s (relkind %s)', c.relname, c.relkind) o from pg_class c join pg_namespace n on n.oid = c.relnamespace
     where n.nspname = 'schule' and c.relname like 'advent\_%'
    union all select format('schule.%s (Typ)', t.typname) from pg_type t join pg_namespace n on n.oid = t.typnamespace
     where n.nspname = 'schule' and t.typname like 'advent\_%' and t.typrelid = 0 and t.typelem = 0
    union all select p.oid::regprocedure::text from pg_proc p join pg_namespace n on n.oid = p.pronamespace
     where (n.nspname = 'schule' and p.proname like 'advent\_%') or (n.nspname = 'api' and p.proname like 'schule\_advent\_%')
    union all select format('schule.regel %s', r.schluessel) from schule.regel r where r.schluessel like 'advent\_%'
    union all select 'schule.sterne.sterne_grund_check enthält advent' from pg_constraint c
     where c.conrelid = 'schule.sterne'::regclass and c.conname = 'sterne_grund_check' and position('''advent''' in pg_get_constraintdef(c.oid)) > 0) q;
  if cardinality(v_da) > 0 then
    raise exception 'ADVENT-S ABBRUCH (schon da: % Advent-Objekte) – nur auf leerem Ausgangszustand einspielen, nichts geändert: %',
      cardinality(v_da), array_to_string(v_da, ' | '); end if;
  for x in select * from (values ('lernender', 'id'), ('lernender', 'zeitzone'), ('lernender', 'ist_test'), ('lernender', 'aktiv'), ('lernender', 'anzeigename'),
                                 ('regel', 'schluessel'), ('regel', 'wert'), ('regel', 'hinweis'),
                                 ('sterne', 'lernender_id'), ('sterne', 'menge'), ('sterne', 'grund'), ('sterne', 'bezug'),
                                 ('karte_stand', 'lernender_id'), ('karte_stand', 'einheit_id'), ('karte_stand', 'lernziel'), ('karte_stand', 'sitzt'),
                                 ('karte_stand', 'sitzt_am'), ('karte_stand', 'landung_art'), ('karte_stand', 'landung')) v(t, s) loop
    if not exists (select 1 from information_schema.columns c where c.table_schema = 'schule' and c.table_name = x.t and c.column_name = x.s) then
      f := f || format('Spalte fehlt: schule.%s.%s', x.t, x.s); end if;
  end loop;
  -- schule.sterne braucht den eindeutigen Schlüssel (lernender_id, grund, bezug) – „on conflict do nothing“ bucht dann genau einmal
  if not exists (select 1 from pg_index i where i.indrelid = 'schule.sterne'::regclass and i.indisunique and i.indpred is null and i.indnatts = 3
                    and (select array_agg(a.attname::text order by a.attname::text collate "C") from pg_attribute a where a.attrelid = i.indrelid and a.attnum = any(i.indkey))
                        = array['bezug', 'grund', 'lernender_id']) then
    f := f || 'schule.sterne: eindeutiger Schlüssel (lernender_id, grund, bezug) fehlt'::text; end if;
  d := (select pg_get_constraintdef(c.oid) from pg_constraint c where c.conrelid = 'schule.sterne'::regclass and c.conname = 'sterne_grund_check');
  if d is distinct from v_alt then f := f || format('sterne_grund_check unerwartet: %s', coalesce(d, 'fehlt')); end if;
  if array_length(f, 1) > 0 then raise exception 'ADVENT-S ABBRUCH (Vorzustand, % Befunde), nichts geändert: %', array_length(f, 1), array_to_string(f, ' | '); end if;
end $advent_vor$;
-- ---------- Probe: Vorher-Stand (nur lesen) ----------
create temp table advent_probe_vorher on commit drop as
  select (select count(*) from pg_class c join pg_namespace n on n.oid = c.relnamespace where n.nspname = 'schule' and c.relname like 'advent\_%' and c.relkind = 'r') tabellen,
         (select count(*) from pg_proc p join pg_namespace n on n.oid = p.pronamespace where (n.nspname = 'schule' and p.proname like 'advent\_%')
             or (n.nspname = 'api' and p.proname like 'schule\_advent\_%')) funktionen,
         (select count(*) from schule.regel r where r.schluessel like 'advent\_%') regeln,
         coalesce((select position('''advent''' in pg_get_constraintdef(c.oid)) > 0 from pg_constraint c where c.conrelid = 'schule.sterne'::regclass and c.conname = 'sterne_grund_check'), false) grund_advent,
         (select count(*) from schule.sterne) sterne_zeilen,
         (select coalesce(sum(menge), 0) from schule.sterne) sterne_summe,
         (select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) from schule.sterne x) sterne_md5,
         (select md5(coalesce(string_agg(x::text, '|' order by x.lernender_id, x.einheit_id, x.lernziel collate "C"), '')) from schule.karte_stand x) karte_md5;

-- ---------- 1. Tabellen ----------
create table schule.advent_teilnahme (
  jahr smallint not null,
  lernender_id bigint not null,          -- bewusst OHNE Fremdschlüssel (wie schule.fehler_erledigt): kein interner Trigger an schule.lernender
  familie text not null check (familie in ('familie', 'test')),
  angelegt_am timestamptz not null default now(),
  primary key (jahr, lernender_id)
);
create table schule.advent_belegung (
  jahr smallint not null,
  lernender_id bigint not null,
  nr smallint not null check (nr between 1 and 24),
  art text not null check (art in ('bild', 'gutschein', 'sterne', 'karte', 'krampus', 'leer')),
  variante text,
  titel text check (char_length(titel) <= 80),
  text text check (char_length(text) <= 300),
  sterne integer not null default 0 check (sterne between 0 and 5000),
  motiv text check (motiv ~ '^[a-z0-9_]{1,40}$'),
  geaendert_am timestamptz not null default now(),
  geaendert_von text not null,
  primary key (jahr, lernender_id, nr),
  constraint advent_belegung_variante check ((art = 'sterne' and variante in ('normal', 'jackpot', 'niete')) or (art = 'gutschein' and variante in ('normal', 'tausch'))
                                            or (art not in ('sterne', 'gutschein') and variante is null)),
  constraint advent_belegung_pflicht check ((art <> 'bild' or motiv is not null) and (art not in ('gutschein', 'krampus') or titel is not null))
);
create table schule.advent_tuer (
  id bigint generated always as identity primary key,
  jahr smallint not null,
  lernender_id bigint not null,
  nr smallint not null check (nr between 1 and 24),
  tag date not null,                     -- Kalendertag in der Lernort-Zeitzone des Kindes beim Öffnen (= Tag der auslösenden Etappe)
  geoeffnet_am timestamptz not null default now(),
  client_id text not null,
  von text not null,
  inhalt jsonb not null,                 -- Schnappschuss {art, variante, titel, text, motiv, sterne}; spätere Belegung ändert Geöffnetes nicht
  sterne integer not null,
  sterne_gebucht boolean not null,
  nachgeholt boolean not null,
  ausl_einheit bigint not null,          -- auslösende Etappe (schule.karte_stand), Landezeit = sitzt_am beim Öffnen
  ausl_lernziel text not null,
  ausl_sitzt_am timestamptz not null,
  ausl_art text,
  unique (jahr, lernender_id, nr),
  unique (lernender_id, client_id),
  unique (lernender_id, ausl_einheit, ausl_lernziel, ausl_sitzt_am),   -- eine Landung öffnet höchstens ein Türchen
  unique (lernender_id, tag, ausl_einheit, ausl_lernziel)              -- dieselbe Etappe am selben Tag höchstens einmal
);
create table schule.advent_gutschein (
  id bigint generated always as identity primary key,
  tuer_id bigint not null unique references schule.advent_tuer(id),
  jahr smallint not null,
  nr smallint not null,
  herkunft_lernender_id bigint not null,
  lernender_id bigint not null,          -- wem er jetzt gehört (ändert sich nur durch den Tausch)
  art text not null check (art in ('gutschein', 'tausch', 'krampus')),
  titel text not null,
  text text,
  motiv text,
  zustand text not null default 'offen',
  eingeloest_am timestamptz, eingeloest_von text,
  zurueckgeholt_am timestamptz, zurueckgeholt_von text,
  erledigt_am timestamptz, erledigt_von text,
  verbraucht_am timestamptz,
  tausch_id bigint,
  getauscht_am timestamptz,
  geaendert_am timestamptz not null default now(),
  constraint advent_gutschein_zustand check ((art = 'gutschein' and zustand in ('offen', 'eingeloest')) or (art = 'tausch' and zustand in ('offen', 'eingeloest', 'verbraucht'))
                                            or (art = 'krampus' and zustand in ('offen', 'erledigt')))
);
create table schule.advent_tausch (
  id bigint generated always as identity primary key,
  am timestamptz not null default now(),
  jahr smallint not null,
  von_lernender_id bigint not null,
  mit_lernender_id bigint not null,
  tauschkarte_id bigint not null,
  gegeben_id bigint not null,
  bekommen_id bigint not null,
  client_id text not null,
  von text not null,
  unique (von_lernender_id, client_id)
);
create table schule.advent_protokoll (
  id bigint generated always as identity primary key,
  am timestamptz not null default now(),
  lernender_id bigint not null,
  aktion text not null,
  nr smallint,
  gutschein_id bigint,
  von text not null,
  daten jsonb
);
create index advent_gutschein_kind on schule.advent_gutschein (lernender_id);
create index advent_protokoll_kind on schule.advent_protokoll (lernender_id, id);
alter table schule.advent_teilnahme enable row level security;
alter table schule.advent_belegung enable row level security;
alter table schule.advent_tuer enable row level security;
alter table schule.advent_gutschein enable row level security;
alter table schule.advent_tausch enable row level security;
alter table schule.advent_protokoll enable row level security;
revoke all on table schule.advent_teilnahme, schule.advent_belegung, schule.advent_tuer, schule.advent_gutschein, schule.advent_tausch, schule.advent_protokoll
  from public, anon, authenticated;
comment on table schule.advent_teilnahme is 'ADVENT-S: Kinder im Adventskalender je Jahr; familie (test = Testkind) begrenzt den Tausch';
comment on table schule.advent_belegung is 'ADVENT-S: Inhalt je Kind und Tür (nur Eltern); geht erst beim Öffnen als Schnappschuss in advent_tuer an das Kind';
comment on table schule.advent_tuer is 'ADVENT-S: geöffnete Türchen (Tag in Lernort-Zeitzone, auslösende Etappe, Schnappschuss); je Kind und Tür einmal';
comment on table schule.advent_gutschein is 'ADVENT-S: Gutscheine (Kind löst selbst ein, Eltern holen zurück), Tauschkarten, Krampus-Aufgaben (nur Eltern haken ab)';
comment on table schule.advent_tausch is 'ADVENT-S: Tausch mit Tauschkarte (zwei offene Gutscheine zwischen Geschwistern, Tauschkarte verbraucht)';
comment on table schule.advent_protokoll is 'ADVENT-S: Protokoll für die Eltern (öffnen, einlösen, zurückholen, erledigt, Tausch, Belegung)';

-- ---------- 2. Regeln (Vorprüfung: es gibt noch keine advent_*-Regel) ----------
insert into schule.regel (schluessel, wert, hinweis)
select x.s, x.w::jsonb, x.h from (values
  ('advent_aktiv', '0', 'ADVENT-S: Adventskalender für die Kinder 0 = aus („nicht aktiv“, bucht nichts), 1 = an, 2 = nur Testkind'),
  ('advent_start', '"2026-12-01"', 'ADVENT-S: erstes Türchen ab diesem Tag (Ortszeit des Kindes); Tür n ist fällig ab Start + n - 1'),
  ('advent_nachholen_bis', '"2027-01-06"', 'ADVENT-S: letzter Tag (einschließlich), an dem Türchen aufgehen/nachgeholt werden; danach verfallen geschlossene'),
  ('advent_sichtbar_bis', '"2027-01-06"', 'ADVENT-S: Kalender bis einschließlich zu sehen; danach nur noch „Meine Gutscheine“, solange einer offen ist'),
  ('advent_max_pro_tag', '2', 'ADVENT-S: höchstens so viele Türchen je Kind und Tag (je Türchen eine eigene Etappe)'),
  ('advent_tausch', '0', 'ADVENT-S: Tauschkarte 0 = aus, 1 = an (Kind tauscht ohne Zustimmung des Geschwisters)')
) x(s, w, h)
where not exists (select 1 from schule.regel r where r.schluessel = x.s);

-- ---------- 3. Hilfsfunktionen ----------
create or replace function schule.advent_jetzt()
 returns timestamptz language sql stable set search_path to ''
as $function$ select now() $function$;
comment on function schule.advent_jetzt() is 'ADVENT-S: Uhrzeit für den Kalender (= now(); im lokalen Testnachbau ersetzt)';

create or replace function schule.advent_einstellung()
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v_a int; v_s date; v_n date; v_v date; v_m int; v_t int;
begin
  begin
    v_a := coalesce((select (r.wert #>> '{}')::int from schule.regel r where r.schluessel = 'advent_aktiv'), 0);
    v_s := coalesce((select (r.wert #>> '{}')::date from schule.regel r where r.schluessel = 'advent_start'), date '2026-12-01');
    v_n := coalesce((select (r.wert #>> '{}')::date from schule.regel r where r.schluessel = 'advent_nachholen_bis'), date '2027-01-06');
    v_v := coalesce((select (r.wert #>> '{}')::date from schule.regel r where r.schluessel = 'advent_sichtbar_bis'), date '2027-01-06');
    v_m := coalesce((select (r.wert #>> '{}')::int from schule.regel r where r.schluessel = 'advent_max_pro_tag'), 2);
    v_t := coalesce((select (r.wert #>> '{}')::int from schule.regel r where r.schluessel = 'advent_tausch'), 0);
  exception when others then
    raise exception 'Adventskalender: Einstellung in schule.regel ungültig (%)', sqlerrm using errcode = 'P0001';
  end;
  if v_a not in (0, 1, 2) or v_t not in (0, 1) or v_m not between 1 and 24 or v_n < v_s or v_v < v_n or v_n > v_s + 60 then
    raise exception 'Adventskalender: Einstellung in schule.regel ungültig (aktiv %, tausch %, max %, start %, nachholen_bis %, sichtbar_bis %)', v_a, v_t, v_m, v_s, v_n, v_v
      using errcode = 'P0001';
  end if;
  return jsonb_build_object('aktiv', v_a, 'start', v_s, 'nachholen_bis', v_n, 'sichtbar_bis', v_v, 'max_pro_tag', v_m, 'tausch', v_t,
                            'jahr', extract(year from v_s)::int);
end $function$;

-- gespeicherte Lernort-Zeitzone des Kindes; null, wenn sie fehlt oder ungültig ist (KEIN Rückfall auf Berlin)
create or replace function schule.advent_tz(p_l bigint)
 returns text language plpgsql stable set search_path to ''
as $function$
declare z text;
begin
  select nullif(btrim(l.zeitzone), '') into z from schule.lernender l where l.id = p_l;
  if z is null then return null; end if;
  begin perform (now() at time zone z); exception when others then return null; end;
  return z;
end $function$;

create or replace function schule.advent_von(p_schluessel text)
 returns text language plpgsql stable security definer set search_path to ''
as $function$
declare r record;
begin
  if not schule.ist_lern(p_schluessel) then return 'eltern:App'; end if;
  select i.rolle, i.name into r from schule.lern_ich(p_schluessel) i;
  return coalesce(r.rolle, '?') || ':' || coalesce(r.name, '?');
end $function$;

create or replace function schule.advent_lock(p_l bigint)
 returns void language sql volatile set search_path to ''
as $function$ select pg_advisory_xact_lock(hashtext('schule.advent'), p_l::int) $function$;

-- Etappen eines Tages: eigene Landung ODER „Sitzt wieder!“ nach dem Nachbessern. Beides setzt in karte_buchen sitzt = true, sitzt_am = Landezeit und
-- (landung_speichern) landung_art und landung mit landung.am = sitzt_am. Eine Setzung („Kann er“) setzt sitzt_am ohne neue landung -> zählt nicht.
create or replace function schule.advent_landungen(p_l bigint, p_tz text, p_tag date)
 returns table (einheit_id bigint, lernziel text, sitzt_am timestamptz, landung_art text, frei boolean)
 language sql stable set search_path to ''
as $function$
  select k.einheit_id, k.lernziel, k.sitzt_am, k.landung_art,
         not exists (select 1 from schule.advent_tuer t where t.lernender_id = p_l and t.ausl_einheit = k.einheit_id and t.ausl_lernziel = k.lernziel
                      and (t.ausl_sitzt_am = k.sitzt_am or t.tag = p_tag)) frei
    from schule.karte_stand k
   where k.lernender_id = p_l and k.sitzt and k.sitzt_am is not null and k.landung_art is not null
     and (k.landung->>'am') is not null and (k.landung->>'am')::timestamptz = k.sitzt_am
     and (k.sitzt_am at time zone p_tz)::date = p_tag
   order by k.sitzt_am, k.einheit_id, k.lernziel collate "C";
$function$;

-- Lage eines Kindes (ohne Inhalte): Schalter, Phase, Tag, Etappen, Grenzen, nächste Tür
create or replace function schule.advent_lage(p_l bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare e jsonb := schule.advent_einstellung(); v_tz text := schule.advent_tz(p_l); v_test boolean; v_jetzt timestamptz := schule.advent_jetzt();
  v_heute date; v_start date := (e->>'start')::date; v_nb date := (e->>'nachholen_bis')::date; v_sb date := (e->>'sichtbar_bis')::date;
  v_jahr int := (e->>'jahr')::int; v_max int := (e->>'max_pro_tag')::int; v_phase text; v_grund text; v_tagnr int; v_faellig int := 0;
  v_offen int[]; v_offen_heute int := 0; v_etappen int := 0; v_frei_et int := 0; v_zu_faellig int := 0; v_naechste int; v_kann boolean := false;
  v_moeglich int := 0; v_frei int := 0; v_schalter boolean;
begin
  select coalesce(l.ist_test, false) into v_test from schule.lernender l where l.id = p_l;
  v_schalter := (e->>'aktiv')::int = 1 or ((e->>'aktiv')::int = 2 and v_test);
  select coalesce(array_agg(t.nr::int order by t.nr), '{}') into v_offen from schule.advent_tuer t where t.lernender_id = p_l and t.jahr = v_jahr;
  if v_tz is null then
    v_grund := 'zeitzone_fehlt';
  else
    v_heute := (v_jetzt at time zone v_tz)::date;
    v_tagnr := v_heute - v_start + 1;
    v_phase := case when v_heute < v_start then 'vor' when v_heute <= v_nb then case when v_tagnr <= 24 then 'laeuft' else 'nachholen' end
                    when v_heute <= v_sb then 'nur_ansehen' else 'vorbei' end;
    v_kann := v_phase in ('laeuft', 'nachholen');
    if v_kann then
      v_faellig := least(24, v_tagnr);
      select count(*) into v_offen_heute from schule.advent_tuer t where t.lernender_id = p_l and t.jahr = v_jahr and t.tag = v_heute;
      select count(*), count(*) filter (where x.frei) into v_etappen, v_frei_et from schule.advent_landungen(p_l, v_tz, v_heute) x;
      select count(*), min(g.n) into v_zu_faellig, v_naechste from generate_series(1, v_faellig) g(n) where not (g.n = any(v_offen));
      v_moeglich := greatest(0, least(v_max - v_offen_heute, v_zu_faellig));
      v_frei := least(v_moeglich, v_frei_et);
    end if;
    v_grund := case when v_phase = 'vor' then 'vor_start' when v_phase = 'vorbei' then 'vorbei' end;
  end if;
  if not v_schalter then v_grund := 'nicht_aktiv'; end if;
  return jsonb_build_object('schalter', v_schalter, 'aktiv', v_grund is null, 'grund', v_grund, 'jahr', v_jahr, 'zeitzone', v_tz,
    'heute', v_heute, 'ortszeit', case when v_tz is not null then to_char(v_jetzt at time zone v_tz, 'YYYY-MM-DD"T"HH24:MI') end,
    'start', v_start, 'nachholen_bis', v_nb, 'sichtbar_bis', v_sb, 'phase', v_phase, 'tag_nr', v_tagnr, 'faellig_bis', v_faellig,
    'kann_oeffnen', v_kann, 'max_pro_tag', v_max, 'offen_heute', v_offen_heute, 'etappen_heute', v_etappen, 'etappen_frei', v_frei_et,
    'moeglich_heute', v_moeglich, 'frei_heute', v_frei, 'naechste_nr', v_naechste, 'offen_nrs', to_jsonb(v_offen), 'ist_test', v_test, 'tausch', (e->>'tausch')::int = 1);
end $function$;

create or replace function schule.advent_gutschein_json(g schule.advent_gutschein, p_eltern boolean)
 returns jsonb language sql stable set search_path to ''
as $function$
  select jsonb_strip_nulls(jsonb_build_object('id', g.id, 'nr', g.nr, 'art', g.art, 'titel', g.titel, 'text', g.text, 'motiv', g.motiv, 'zustand', g.zustand,
    'eingeloest_am', g.eingeloest_am, 'eingeloest_von', case when p_eltern then g.eingeloest_von else split_part(g.eingeloest_von, ':', 1) end,
    'zurueckgeholt_am', g.zurueckgeholt_am, 'zurueckgeholt_von', case when p_eltern then g.zurueckgeholt_von end,
    'erledigt_am', g.erledigt_am, 'erledigt_von', case when p_eltern then g.erledigt_von end, 'verbraucht_am', g.verbraucht_am,
    'getauscht_am', g.getauscht_am, 'getauscht', g.lernender_id <> g.herkunft_lernender_id,
    'herkunft_lernender_id', case when p_eltern then g.herkunft_lernender_id end, 'lernender_id', case when p_eltern then g.lernender_id end,
    'tausch_id', g.tausch_id));
$function$;

-- geöffnetes Türchen als Antwort (nur geöffnete!)
create or replace function schule.advent_tuer_json(t schule.advent_tuer)
 returns jsonb language sql stable set search_path to ''
as $function$
  select jsonb_build_object('nr', t.nr, 'tag', t.tag, 'geoeffnet_am', t.geoeffnet_am, 'nachgeholt', t.nachgeholt,
    'art', t.inhalt->>'art', 'variante', t.inhalt->>'variante', 'titel', t.inhalt->>'titel', 'text', t.inhalt->>'text', 'motiv', t.inhalt->>'motiv',
    'sterne', t.sterne, 'sterne_gutgeschrieben', t.sterne_gebucht,
    'gutschein', (select jsonb_build_object('id', g.id, 'art', g.art, 'zustand', g.zustand) from schule.advent_gutschein g where g.tuer_id = t.id));
$function$;

create or replace function schule.advent_zaehler(p_l bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  select jsonb_build_object('offen', count(*) filter (where g.art in ('gutschein', 'tausch') and g.zustand = 'offen'),
                            'tauschkarten', count(*) filter (where g.art = 'tausch' and g.zustand = 'offen'),
                            'eingeloest', count(*) filter (where g.art in ('gutschein', 'tausch') and g.zustand in ('eingeloest', 'verbraucht')),
                            'krampus_offen', count(*) filter (where g.art = 'krampus' and g.zustand = 'offen'),
                            'krampus_erledigt', count(*) filter (where g.art = 'krampus' and g.zustand = 'erledigt'))
    from schule.advent_gutschein g where g.lernender_id = p_l;
$function$;

create or replace function schule.advent_nicht_aktiv(p_lage jsonb)
 returns jsonb language sql immutable set search_path to ''
as $function$
  select jsonb_build_object('ok', true, 'aktiv', false, 'grund', coalesce(p_lage->>'grund', 'nicht_aktiv'));
$function$;

-- ---------- 4. Kind ----------
create or replace function schule.advent_stand(p_l bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v jsonb := schule.advent_lage(p_l); z jsonb; v_t jsonb; v_menue_g boolean;
begin
  if not (v->>'schalter')::boolean then return schule.advent_nicht_aktiv(v); end if;
  z := schule.advent_zaehler(p_l);
  v_menue_g := coalesce((v->>'phase') in ('laeuft', 'nachholen', 'nur_ansehen'), false) or (z->>'offen')::int + (z->>'krampus_offen')::int > 0;
  if not (v->>'aktiv')::boolean then
    -- vor dem Start, nach dem Sichtbarkeits-Ende, ohne Zeitzone: Kalender weg; „Meine Gutscheine“ bleibt, solange einer offen ist
    return schule.advent_nicht_aktiv(v) || jsonb_build_object('heute', v->'heute', 'start', v->'start', 'sichtbar_bis', v->'sichtbar_bis',
      'gutscheine', z, 'menue', jsonb_build_object('kalender', false, 'gutscheine', v_menue_g and v->>'grund' <> 'vor_start'));
  end if;
  select jsonb_agg(case
           when t.id is not null then jsonb_build_object('nr', n, 'zustand', 'offen', 'art', t.inhalt->>'art', 'variante', t.inhalt->>'variante',
                                                       'titel', t.inhalt->>'titel', 'motiv', t.inhalt->>'motiv', 'sterne', t.sterne, 'nachgeholt', t.nachgeholt, 'tag', t.tag)
           else jsonb_build_object('nr', n, 'zustand', case
             when not (v->>'kann_oeffnen')::boolean then case when v->>'phase' = 'nur_ansehen' then 'verfallen' else 'zu' end
             when n = (v->>'naechste_nr')::int and (v->>'frei_heute')::int > 0 then 'bereit'
             when n = (v->>'tag_nr')::int then 'heute'
             when n < (v->>'tag_nr')::int then 'nachholen'
             when n = (v->>'tag_nr')::int + 1 and (v->>'heute')::date < (v->>'nachholen_bis')::date then 'morgen'
             else 'zu' end) end order by n)
    into v_t
    from generate_series(1, 24) n left join schule.advent_tuer t on t.lernender_id = p_l and t.jahr = (v->>'jahr')::int and t.nr = n;
  return jsonb_build_object('ok', true, 'aktiv', true, 'jahr', v->'jahr', 'heute', v->'heute', 'ortszeit', v->'ortszeit', 'zeitzone', v->'zeitzone',
    'start', v->'start', 'nachholen_bis', v->'nachholen_bis', 'sichtbar_bis', v->'sichtbar_bis', 'phase', v->'phase', 'tag_nr', v->'tag_nr',
    'max_pro_tag', v->'max_pro_tag', 'offen_heute', v->'offen_heute', 'etappen_heute', v->'etappen_heute', 'moeglich_heute', v->'moeglich_heute',
    'frei_heute', v->'frei_heute', 'naechste_nr', v->'naechste_nr', 'bereit', (v->>'frei_heute')::int > 0,
    'braucht_etappe', (v->>'moeglich_heute')::int > 0 and (v->>'frei_heute')::int = 0,
    'tueren', v_t, 'gutscheine', z, 'tausch', v->'tausch', 'menue', jsonb_build_object('kalender', true, 'gutscheine', v_menue_g));
end $function$;

-- p_erwartet (Urteil 1215, Auflage 1): die Tür, die das Gerät angezeigt hat („Tür n öffnen“). Nach der Kind-Sperre: ist sie schon offen (anderes Gerät),
-- kommt ihr Inhalt als schon_offen ohne Buchung; ist eine andere Tür als nächste dran, geht nichts auf (grund andere_tuer + stand). null = wie bisher.
create or replace function schule.advent_oeffnen(p_l bigint, p_cid text, p_von text, p_erwartet int default null)
 returns jsonb language plpgsql volatile set search_path to ''
as $function$
declare v jsonb; t schule.advent_tuer; b schule.advent_belegung; k record; v_nr int; v_heute date; v_inhalt jsonb; v_menge int; v_gid bigint; v_art text;
begin
  if p_erwartet is not null and p_erwartet not between 1 and 24 then raise exception 'erwartet_nr: 1 bis 24' using errcode = 'P0001'; end if;
  perform schule.advent_lock(p_l);                                   -- zwei Geräte / doppelter Klick: nacheinander
  v := schule.advent_lage(p_l);
  if not (v->>'schalter')::boolean then return schule.advent_nicht_aktiv(v); end if;
  select * into t from schule.advent_tuer x where x.lernender_id = p_l and x.client_id = p_cid;
  if t.id is not null then                                           -- Wiederholung desselben Tipps: dieselbe Antwort, nichts gebucht
    return jsonb_build_object('ok', true, 'aktiv', true, 'geoeffnet', true, 'wiederholt', true, 'schon_offen', false, 'tuer', schule.advent_tuer_json(t),
      'frei_heute', v->'frei_heute', 'moeglich_heute', v->'moeglich_heute', 'naechste_nr', v->'naechste_nr');
  end if;
  if not (v->>'aktiv')::boolean then return schule.advent_nicht_aktiv(v); end if;
  v_heute := (v->>'heute')::date;
  if p_erwartet is not null then                                     -- Öffnen an die angezeigte Tür binden
    select * into t from schule.advent_tuer x where x.lernender_id = p_l and x.jahr = (v->>'jahr')::int and x.nr = p_erwartet;
    if t.id is not null then                                         -- schon offen (anderes Gerät / anderer Tipp): Inhalt zeigen, nichts gebucht
      return jsonb_build_object('ok', true, 'aktiv', true, 'geoeffnet', true, 'wiederholt', true, 'schon_offen', true, 'tuer', schule.advent_tuer_json(t),
        'frei_heute', v->'frei_heute', 'moeglich_heute', v->'moeglich_heute', 'naechste_nr', v->'naechste_nr', 'stand', schule.advent_stand(p_l));
    end if;
    if (v->>'kann_oeffnen')::boolean and (v->>'naechste_nr') is not null and (v->>'naechste_nr')::int <> p_erwartet then
      return jsonb_build_object('ok', true, 'aktiv', true, 'geoeffnet', false, 'grund', 'andere_tuer', 'erwartet_nr', p_erwartet,
        'naechste_nr', v->'naechste_nr', 'frei_heute', v->'frei_heute', 'moeglich_heute', v->'moeglich_heute', 'stand', schule.advent_stand(p_l));
    end if;
  end if;
  if not (v->>'kann_oeffnen')::boolean then
    return jsonb_build_object('ok', true, 'aktiv', true, 'geoeffnet', false, 'grund', 'nachholen_vorbei');
  end if;
  if (v->>'naechste_nr') is null then
    return jsonb_build_object('ok', true, 'aktiv', true, 'geoeffnet', false, 'grund', 'alles_offen');
  end if;
  if (v->>'moeglich_heute')::int = 0 then
    return jsonb_build_object('ok', true, 'aktiv', true, 'geoeffnet', false, 'grund', 'limit', 'offen_heute', v->'offen_heute',
      'letzte_nr', (select x.nr from schule.advent_tuer x where x.lernender_id = p_l and x.jahr = (v->>'jahr')::int and x.tag = v_heute order by x.id desc limit 1));
  end if;
  select * into k from schule.advent_landungen(p_l, v->>'zeitzone', v_heute) x where x.frei order by x.sitzt_am, x.einheit_id, x.lernziel collate "C" limit 1;
  if k.einheit_id is null then
    return jsonb_build_object('ok', true, 'aktiv', true, 'geoeffnet', false, 'grund', 'keine_etappe', 'naechste_nr', v->'naechste_nr',
      'letzte_nr', (select x.nr from schule.advent_tuer x where x.lernender_id = p_l and x.jahr = (v->>'jahr')::int and x.tag = v_heute order by x.id desc limit 1));
  end if;
  v_nr := (v->>'naechste_nr')::int;                                  -- immer das älteste geschlossene, fällige
  select * into b from schule.advent_belegung x where x.jahr = (v->>'jahr')::int and x.lernender_id = p_l and x.nr = v_nr;
  v_inhalt := case when b.nr is null then jsonb_build_object('art', 'leer', 'variante', null, 'titel', null, 'text', null, 'motiv', null, 'sterne', 0)
                   else jsonb_build_object('art', b.art, 'variante', b.variante, 'titel', b.titel, 'text', b.text, 'motiv', b.motiv, 'sterne', b.sterne) end;
  insert into schule.advent_tuer (jahr, lernender_id, nr, tag, geoeffnet_am, client_id, von, inhalt, sterne, sterne_gebucht, nachgeholt,
                                  ausl_einheit, ausl_lernziel, ausl_sitzt_am, ausl_art)
  values ((v->>'jahr')::int, p_l, v_nr, v_heute, schule.advent_jetzt(), p_cid, p_von, v_inhalt, (v_inhalt->>'sterne')::int, false,
          v_nr < (v->>'tag_nr')::int, k.einheit_id, k.lernziel, k.sitzt_am, k.landung_art)
  returning * into t;
  if t.sterne > 0 then                                               -- genau einmal je Kind und Tür (eindeutiger Schlüssel in schule.sterne)
    insert into schule.sterne (lernender_id, menge, grund, bezug) values (p_l, t.sterne, 'advent', 'advent:' || t.jahr || ':' || t.nr)
    on conflict do nothing returning menge into v_menge;
    if v_menge is not null then update schule.advent_tuer set sterne_gebucht = true where id = t.id returning * into t; end if;
  end if;
  v_art := case when t.inhalt->>'art' = 'krampus' then 'krampus' when t.inhalt->>'art' = 'gutschein' and t.inhalt->>'variante' = 'tausch' then 'tausch'
                when t.inhalt->>'art' = 'gutschein' then 'gutschein' end;
  if v_art is not null then
    insert into schule.advent_gutschein (tuer_id, jahr, nr, herkunft_lernender_id, lernender_id, art, titel, text, motiv)
    values (t.id, t.jahr, t.nr, p_l, p_l, v_art, coalesce(t.inhalt->>'titel', ''), t.inhalt->>'text', t.inhalt->>'motiv') returning id into v_gid;
  end if;
  insert into schule.advent_protokoll (lernender_id, aktion, nr, gutschein_id, von, daten)
  values (p_l, 'oeffnen', t.nr, v_gid, p_von, jsonb_build_object('tag', t.tag, 'art', t.inhalt->>'art', 'sterne', t.sterne, 'nachgeholt', t.nachgeholt,
          'etappe', jsonb_build_object('einheit_id', t.ausl_einheit, 'lernziel', t.ausl_lernziel, 'sitzt_am', t.ausl_sitzt_am, 'landung_art', t.ausl_art)));
  v := schule.advent_lage(p_l);
  return jsonb_build_object('ok', true, 'aktiv', true, 'geoeffnet', true, 'wiederholt', false, 'schon_offen', false, 'tuer', schule.advent_tuer_json(t),
    'frei_heute', v->'frei_heute', 'moeglich_heute', v->'moeglich_heute', 'naechste_nr', v->'naechste_nr', 'gutscheine', schule.advent_zaehler(p_l));
end $function$;

create or replace function schule.advent_tuer_lesen(p_l bigint, p_nr int)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v jsonb := schule.advent_lage(p_l); t schule.advent_tuer;
begin
  if not (v->>'aktiv')::boolean then return schule.advent_nicht_aktiv(v); end if;
  if p_nr is null or p_nr not between 1 and 24 then raise exception 'nr: 1 bis 24' using errcode = 'P0001'; end if;
  select * into t from schule.advent_tuer x where x.lernender_id = p_l and x.jahr = (v->>'jahr')::int and x.nr = p_nr;
  if t.id is null then raise exception 'Türchen % ist noch zu', p_nr using errcode = 'P0001'; end if;   -- kein Inhalt geschlossener Türen
  return jsonb_build_object('ok', true, 'aktiv', true, 'tuer', schule.advent_tuer_json(t));
end $function$;

create or replace function schule.advent_gutscheine(p_l bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v jsonb := schule.advent_lage(p_l); z jsonb; v_g jsonb; v_k jsonb; v_gesch jsonb := '[]'::jsonb;
begin
  if not (v->>'schalter')::boolean then return schule.advent_nicht_aktiv(v); end if;
  z := schule.advent_zaehler(p_l);
  select coalesce(jsonb_agg(schule.advent_gutschein_json(g, false) order by case g.zustand when 'offen' then 0 else 1 end, g.nr, g.id), '[]'::jsonb) into v_g
    from schule.advent_gutschein g where g.lernender_id = p_l and g.art in ('gutschein', 'tausch');
  select coalesce(jsonb_agg(schule.advent_gutschein_json(g, false) order by case g.zustand when 'offen' then 0 else 1 end, g.nr, g.id), '[]'::jsonb) into v_k
    from schule.advent_gutschein g where g.lernender_id = p_l and g.art = 'krampus';
  if (v->>'tausch')::boolean and (z->>'tauschkarten')::int > 0 then
    select coalesce(jsonb_agg(jsonb_build_object('lernender_id', l.id, 'name', l.anzeigename,
             'gutscheine', (select coalesce(jsonb_agg(jsonb_build_object('id', g.id, 'nr', g.nr, 'titel', g.titel, 'text', g.text, 'motiv', g.motiv) order by g.nr, g.id), '[]'::jsonb)
                              from schule.advent_gutschein g where g.lernender_id = l.id and g.jahr = a.jahr and g.art = 'gutschein' and g.zustand = 'offen')) order by l.id), '[]'::jsonb)
      into v_gesch
      from schule.advent_teilnahme a join schule.advent_teilnahme b on b.jahr = a.jahr and b.familie = a.familie and b.lernender_id <> a.lernender_id
      join schule.lernender l on l.id = b.lernender_id and l.aktiv
     where a.lernender_id = p_l and a.jahr = (v->>'jahr')::int;
  end if;
  return jsonb_build_object('ok', true, 'aktiv', true, 'zaehler', z, 'gutscheine', v_g, 'krampus', v_k,
    'tausch', jsonb_build_object('aktiv', (v->>'tausch')::boolean, 'tauschkarten', z->'tauschkarten', 'geschwister', v_gesch),
    'menue', jsonb_build_object('gutscheine', coalesce((v->>'phase') in ('laeuft', 'nachholen', 'nur_ansehen'), false)
                                               or (z->>'offen')::int + (z->>'krampus_offen')::int > 0));
end $function$;

create or replace function schule.advent_einloesen(p_l bigint, p_g bigint, p_von text)
 returns jsonb language plpgsql volatile set search_path to ''
as $function$
declare v jsonb := schule.advent_lage(p_l); g schule.advent_gutschein; v_wieder boolean := false;
begin
  if not (v->>'schalter')::boolean then return schule.advent_nicht_aktiv(v); end if;
  perform schule.advent_lock(p_l);
  select * into g from schule.advent_gutschein x where x.id = p_g for update;
  if g.id is null or g.lernender_id <> p_l then raise exception 'Gutschein nicht gefunden' using errcode = 'P0001'; end if;
  if g.art = 'krampus' then raise exception 'Krampus-Aufgaben haken nur Mama oder Papa ab' using errcode = 'P0001'; end if;
  if g.art = 'tausch' then raise exception 'Die Tauschkarte wird beim Tauschen verbraucht' using errcode = 'P0001'; end if;
  if g.zustand = 'eingeloest' then v_wieder := true;
  else
    update schule.advent_gutschein set zustand = 'eingeloest', eingeloest_am = schule.advent_jetzt(), eingeloest_von = p_von, geaendert_am = now()
     where id = g.id returning * into g;
    insert into schule.advent_protokoll (lernender_id, aktion, nr, gutschein_id, von, daten) values (p_l, 'einloesen', g.nr, g.id, p_von, jsonb_build_object('titel', g.titel));
  end if;
  return jsonb_build_object('ok', true, 'aktiv', true, 'wiederholt', v_wieder, 'gutschein', schule.advent_gutschein_json(g, false), 'zaehler', schule.advent_zaehler(p_l));
end $function$;

create or replace function schule.advent_tauschen(p_l bigint, p_karte bigint, p_mein bigint, p_fremd bigint, p_cid text, p_von text)
 returns jsonb language plpgsql volatile set search_path to ''
as $function$
declare v jsonb := schule.advent_lage(p_l); x schule.advent_tausch; v_b bigint; tk schule.advent_gutschein; gm schule.advent_gutschein; gf schule.advent_gutschein;
  v_fa text; v_fb text; v_jetzt timestamptz := schule.advent_jetzt();
begin
  if not (v->>'schalter')::boolean then return schule.advent_nicht_aktiv(v); end if;
  if not (v->>'tausch')::boolean then return jsonb_build_object('ok', true, 'aktiv', true, 'getauscht', false, 'grund', 'tausch_aus'); end if;
  select * into x from schule.advent_tausch t where t.von_lernender_id = p_l and t.client_id = p_cid;
  if x.id is not null then
    return jsonb_build_object('ok', true, 'aktiv', true, 'getauscht', true, 'wiederholt', true, 'tausch', to_jsonb(x) - 'von' - 'client_id');
  end if;
  if p_karte is null or p_mein is null or p_fremd is null or p_karte = p_mein or p_karte = p_fremd or p_mein = p_fremd then
    raise exception 'tauschkarte_id, mein_gutschein_id und fremder_gutschein_id: drei verschiedene Gutscheine' using errcode = 'P0001'; end if;
  select g.lernender_id into v_b from schule.advent_gutschein g where g.id = p_fremd;
  if v_b is null or v_b = p_l then raise exception 'Tauschen: Gutschein des Geschwisters nicht gefunden' using errcode = 'P0001'; end if;
  perform schule.advent_lock(least(p_l, v_b)); perform schule.advent_lock(greatest(p_l, v_b));   -- feste Reihenfolge, keine Verklemmung
  select * into x from schule.advent_tausch t where t.von_lernender_id = p_l and t.client_id = p_cid;   -- nach der Sperre noch einmal
  if x.id is not null then
    return jsonb_build_object('ok', true, 'aktiv', true, 'getauscht', true, 'wiederholt', true, 'tausch', to_jsonb(x) - 'von' - 'client_id');
  end if;
  perform 1 from schule.advent_gutschein g where g.id in (p_karte, p_mein, p_fremd) order by g.id for update;
  select * into tk from schule.advent_gutschein g where g.id = p_karte;
  select * into gm from schule.advent_gutschein g where g.id = p_mein;
  select * into gf from schule.advent_gutschein g where g.id = p_fremd;
  if tk.id is null or tk.lernender_id <> p_l or tk.art <> 'tausch' then raise exception 'Tauschen: das ist keine Tauschkarte von dir' using errcode = 'P0001'; end if;
  if tk.zustand <> 'offen' then raise exception 'Tauschen: die Tauschkarte ist schon verbraucht' using errcode = 'P0001'; end if;
  if gm.id is null or gm.lernender_id <> p_l then raise exception 'Tauschen: dein Gutschein wurde nicht gefunden' using errcode = 'P0001'; end if;
  if gf.lernender_id is distinct from v_b then raise exception 'Tauschen: der Gutschein hat gerade den Besitzer gewechselt – bitte neu laden' using errcode = 'P0001'; end if;
  if gm.art <> 'gutschein' or gf.art <> 'gutschein' then raise exception 'Tauschen: nur normale Gutscheine (keine Krampus-Aufgabe, keine Tauschkarte)' using errcode = 'P0001'; end if;
  if gm.zustand <> 'offen' or gf.zustand <> 'offen' then raise exception 'Tauschen: nur offene Gutscheine (nicht eingelöst)' using errcode = 'P0001'; end if;
  select a.familie into v_fa from schule.advent_teilnahme a where a.jahr = (v->>'jahr')::int and a.lernender_id = p_l;
  select a.familie into v_fb from schule.advent_teilnahme a join schule.lernender l on l.id = a.lernender_id and l.aktiv
   where a.jahr = (v->>'jahr')::int and a.lernender_id = v_b;
  if v_fa is null or v_fb is null or v_fa <> v_fb then raise exception 'Tauschen: nur mit dem Geschwister' using errcode = 'P0001'; end if;
  if tk.jahr <> (v->>'jahr')::int or gm.jahr <> (v->>'jahr')::int or gf.jahr <> (v->>'jahr')::int then   -- nur Gutscheine des laufenden Advents
    raise exception 'Tauschen: nur Gutscheine aus diesem Advent' using errcode = 'P0001'; end if;
  insert into schule.advent_tausch (am, jahr, von_lernender_id, mit_lernender_id, tauschkarte_id, gegeben_id, bekommen_id, client_id, von)
  values (v_jetzt, (v->>'jahr')::int, p_l, v_b, p_karte, p_mein, p_fremd, p_cid, p_von) returning * into x;
  update schule.advent_gutschein set zustand = 'verbraucht', verbraucht_am = v_jetzt, tausch_id = x.id, geaendert_am = now() where id = p_karte;
  update schule.advent_gutschein set lernender_id = v_b, getauscht_am = v_jetzt, tausch_id = x.id, geaendert_am = now() where id = p_mein;
  update schule.advent_gutschein set lernender_id = p_l, getauscht_am = v_jetzt, tausch_id = x.id, geaendert_am = now() where id = p_fremd;
  insert into schule.advent_protokoll (lernender_id, aktion, nr, gutschein_id, von, daten) values
    (p_l, 'tausch', tk.nr, p_karte, p_von, jsonb_build_object('tausch_id', x.id, 'mit', v_b, 'gegeben', p_mein, 'gegeben_titel', gm.titel, 'bekommen', p_fremd, 'bekommen_titel', gf.titel)),
    (v_b, 'getauscht_von_geschwister', gf.nr, p_fremd, p_von, jsonb_build_object('tausch_id', x.id, 'mit', p_l, 'abgegeben', p_fremd, 'abgegeben_titel', gf.titel, 'bekommen', p_mein, 'bekommen_titel', gm.titel));
  return jsonb_build_object('ok', true, 'aktiv', true, 'getauscht', true, 'wiederholt', false, 'tausch', to_jsonb(x) - 'von' - 'client_id',
    'zaehler', schule.advent_zaehler(p_l));
end $function$;

-- ---------- 5. Eltern ----------
create or replace function schule.advent_eintrag(p jsonb)
 returns jsonb language plpgsql immutable set search_path to ''
as $function$
declare v_nr int; v_art text; v_var text; v_ti text; v_tx text; v_st int; v_mo text; k text;
begin
  if jsonb_typeof(p) is distinct from 'object' then raise exception 'Türchen: Eintrag muss ein Objekt sein' using errcode = 'P0001'; end if;
  for k in select jsonb_object_keys(p) loop
    if k not in ('nr', 'art', 'variante', 'titel', 'text', 'sterne', 'motiv') then raise exception 'Türchen: unbekanntes Feld „%“', k using errcode = 'P0001'; end if;
  end loop;
  if jsonb_typeof(p->'nr') is distinct from 'number' or (p->>'nr')::numeric <> trunc((p->>'nr')::numeric) or (p->>'nr')::numeric not between 1 and 24 then
    raise exception 'Türchen: nr muss 1 bis 24 sein' using errcode = 'P0001'; end if;
  v_nr := (p->>'nr')::int;
  v_art := lower(btrim(coalesce(p->>'art', '')));
  if v_art not in ('bild', 'gutschein', 'sterne', 'karte', 'krampus', 'leer') then
    raise exception 'Tür %: art muss bild, gutschein, sterne, karte, krampus oder leer sein', v_nr using errcode = 'P0001'; end if;
  v_var := nullif(lower(btrim(coalesce(p->>'variante', ''))), '');
  if v_art = 'sterne' then v_var := coalesce(v_var, 'normal');
    if v_var not in ('normal', 'jackpot', 'niete') then raise exception 'Tür %: variante bei sterne: normal, jackpot oder niete', v_nr using errcode = 'P0001'; end if;
  elsif v_art = 'gutschein' then v_var := coalesce(v_var, 'normal');
    if v_var not in ('normal', 'tausch') then raise exception 'Tür %: variante bei gutschein: normal oder tausch', v_nr using errcode = 'P0001'; end if;
  elsif v_var is not null then raise exception 'Tür %: variante nur bei sterne oder gutschein', v_nr using errcode = 'P0001';
  end if;
  v_ti := nullif(btrim(coalesce(p->>'titel', '')), '');
  v_tx := nullif(btrim(coalesce(p->>'text', '')), '');
  if char_length(v_ti) > 80 then raise exception 'Tür %: titel höchstens 80 Zeichen', v_nr using errcode = 'P0001'; end if;
  if char_length(v_tx) > 300 then raise exception 'Tür %: text höchstens 300 Zeichen', v_nr using errcode = 'P0001'; end if;
  if p ? 'sterne' and jsonb_typeof(p->'sterne') <> 'null' then
    if jsonb_typeof(p->'sterne') <> 'number' or (p->>'sterne')::numeric <> trunc((p->>'sterne')::numeric) or (p->>'sterne')::numeric not between 0 and 5000 then
      raise exception 'Tür %: sterne ganze Zahl 0 bis 5000', v_nr using errcode = 'P0001'; end if;
    v_st := (p->>'sterne')::int;
  else v_st := 0; end if;
  v_mo := nullif(btrim(coalesce(p->>'motiv', '')), '');
  if v_mo is not null and v_mo !~ '^[a-z0-9_]{1,40}$' then raise exception 'Tür %: motiv als Schlüssel (a-z, 0-9, _)', v_nr using errcode = 'P0001'; end if;
  if v_art = 'bild' and v_mo is null then raise exception 'Tür %: bild braucht ein motiv', v_nr using errcode = 'P0001'; end if;
  if v_art in ('gutschein', 'krampus') and v_ti is null then raise exception 'Tür %: % braucht einen titel', v_nr, v_art using errcode = 'P0001'; end if;
  return jsonb_build_object('nr', v_nr, 'art', v_art, 'variante', v_var, 'titel', v_ti, 'text', v_tx, 'sterne', v_st, 'motiv', v_mo);
end $function$;

-- Belegung setzen: nur geschlossene Türchen. p_ueberspringen = true überspringt geöffnete (Werkzeug), sonst Abbruch mit Liste.
create or replace function schule.advent_belegen(p_kinder bigint[], p_tueren jsonb, p_ueberspringen boolean, p_von text)
 returns jsonb language plpgsql volatile set search_path to ''
as $function$
declare e jsonb := schule.advent_einstellung(); v_jahr int := (e->>'jahr')::int; v_l bigint; v_x jsonb; v_e jsonb[] := '{}'; v_nrs int[] := '{}';
  v_offen int[]; v_ges int; v_unv int; v_skip int[]; v_n int; v_erg jsonb := '[]'::jsonb; v_fehl text[] := '{}';
begin
  if p_kinder is null or cardinality(p_kinder) = 0 then raise exception 'Belegung: welche Kinder? (lernender_id oder lernender_ids)' using errcode = 'P0001'; end if;
  if (select count(distinct k) from unnest(p_kinder) k) <> cardinality(p_kinder) then raise exception 'Belegung: Kind doppelt genannt' using errcode = 'P0001'; end if;
  if jsonb_typeof(p_tueren) is distinct from 'array' or jsonb_array_length(p_tueren) = 0 or jsonb_array_length(p_tueren) > 24 then
    raise exception 'Belegung: tueren als Liste mit 1 bis 24 Einträgen' using errcode = 'P0001'; end if;
  for v_x in select x from jsonb_array_elements(p_tueren) x loop
    v_x := schule.advent_eintrag(v_x);
    if (v_x->>'nr')::int = any(v_nrs) then raise exception 'Belegung: Tür % doppelt', v_x->>'nr' using errcode = 'P0001'; end if;
    v_nrs := v_nrs || (v_x->>'nr')::int; v_e := v_e || v_x;
  end loop;
  for v_l in select k from unnest(p_kinder) k order by k loop
    if not exists (select 1 from schule.lernender l where l.id = v_l and l.aktiv) then raise exception 'Belegung: Kind % nicht gefunden', v_l using errcode = 'P0001'; end if;
    perform schule.advent_lock(v_l);
    select coalesce(array_agg(t.nr::int order by t.nr), '{}') into v_offen from schule.advent_tuer t where t.lernender_id = v_l and t.jahr = v_jahr and t.nr = any(v_nrs);
    if cardinality(v_offen) > 0 and not p_ueberspringen then v_fehl := v_fehl || format('Kind %s: %s', v_l, array_to_string(v_offen, ', ')); end if;
  end loop;
  if cardinality(v_fehl) > 0 then
    raise exception 'Belegung: schon offene Türchen bleiben, wie sie sind (%) – nichts geändert; nur_geschlossene: true überspringt sie', array_to_string(v_fehl, '; ')
      using errcode = 'P0001'; end if;
  for v_l in select k from unnest(p_kinder) k order by k loop
    insert into schule.advent_teilnahme (jahr, lernender_id, familie)
    select v_jahr, v_l, case when l.ist_test then 'test' else 'familie' end from schule.lernender l where l.id = v_l
    on conflict do nothing;
    v_ges := 0; v_unv := 0; v_skip := '{}';
    foreach v_x in array v_e loop
      if exists (select 1 from schule.advent_tuer t where t.lernender_id = v_l and t.jahr = v_jahr and t.nr = (v_x->>'nr')::int) then
        v_skip := v_skip || (v_x->>'nr')::int; continue; end if;
      insert into schule.advent_belegung as b (jahr, lernender_id, nr, art, variante, titel, text, sterne, motiv, geaendert_am, geaendert_von)
      values (v_jahr, v_l, (v_x->>'nr')::int, v_x->>'art', v_x->>'variante', v_x->>'titel', v_x->>'text', (v_x->>'sterne')::int, v_x->>'motiv', now(), p_von)
      on conflict (jahr, lernender_id, nr) do update set art = excluded.art, variante = excluded.variante, titel = excluded.titel, text = excluded.text,
        sterne = excluded.sterne, motiv = excluded.motiv, geaendert_am = excluded.geaendert_am, geaendert_von = excluded.geaendert_von
       where (b.art, b.variante, b.titel, b.text, b.sterne, b.motiv) is distinct from (excluded.art, excluded.variante, excluded.titel, excluded.text, excluded.sterne, excluded.motiv);
      get diagnostics v_n = row_count;
      if v_n = 1 then v_ges := v_ges + 1; else v_unv := v_unv + 1; end if;
    end loop;
    if v_ges > 0 or cardinality(v_skip) > 0 then
      insert into schule.advent_protokoll (lernender_id, aktion, von, daten)
      values (v_l, 'belegung', p_von, jsonb_build_object('gesetzt', v_ges, 'unveraendert', v_unv, 'uebersprungen_offen', to_jsonb(v_skip), 'tueren', to_jsonb(v_nrs)));
    end if;
    v_erg := v_erg || jsonb_build_object('lernender_id', v_l, 'gesetzt', v_ges, 'unveraendert', v_unv, 'uebersprungen_offen', to_jsonb(v_skip));
  end loop;
  return jsonb_build_object('ok', true, 'jahr', v_jahr, 'kinder', v_erg);
end $function$;

create or replace function schule.advent_gutschein_eltern(p_g bigint, p_aktion text, p_von text)
 returns jsonb language plpgsql volatile set search_path to ''
as $function$
declare g schule.advent_gutschein; v_l bigint; v_unv boolean := false; v_jetzt timestamptz := schule.advent_jetzt();
begin
  if p_aktion is null or p_aktion not in ('einloesen', 'zurueckholen', 'erledigt', 'noch_nicht') then
    raise exception 'aktion: einloesen, zurueckholen, erledigt oder noch_nicht' using errcode = 'P0001'; end if;
  select x.lernender_id into v_l from schule.advent_gutschein x where x.id = p_g;
  if v_l is null then raise exception 'Gutschein nicht gefunden' using errcode = 'P0001'; end if;
  perform schule.advent_lock(v_l);
  select * into g from schule.advent_gutschein x where x.id = p_g for update;
  if g.lernender_id <> v_l then raise exception 'Gutschein wurde gerade getauscht – bitte neu laden' using errcode = 'P0001'; end if;
  if p_aktion in ('einloesen', 'zurueckholen') and g.art = 'krampus' then raise exception 'Krampus-Aufgabe: erledigt oder noch_nicht' using errcode = 'P0001'; end if;
  if p_aktion in ('erledigt', 'noch_nicht') and g.art <> 'krampus' then raise exception 'erledigt / noch_nicht nur bei Krampus-Aufgaben' using errcode = 'P0001'; end if;
  if g.zustand = 'verbraucht' then raise exception 'Die Tauschkarte ist schon beim Tauschen verbraucht' using errcode = 'P0001'; end if;
  if p_aktion = 'einloesen' then
    if g.zustand = 'eingeloest' then v_unv := true;
    else update schule.advent_gutschein set zustand = 'eingeloest', eingeloest_am = v_jetzt, eingeloest_von = p_von, geaendert_am = now() where id = g.id returning * into g; end if;
  elsif p_aktion = 'zurueckholen' then
    if g.zustand = 'offen' then v_unv := true;
    else update schule.advent_gutschein set zustand = 'offen', zurueckgeholt_am = v_jetzt, zurueckgeholt_von = p_von, eingeloest_am = null, eingeloest_von = null,
           geaendert_am = now() where id = g.id returning * into g; end if;
  elsif p_aktion = 'erledigt' then
    if g.zustand = 'erledigt' then v_unv := true;
    else update schule.advent_gutschein set zustand = 'erledigt', erledigt_am = v_jetzt, erledigt_von = p_von, geaendert_am = now() where id = g.id returning * into g; end if;
  else
    if g.zustand = 'offen' then v_unv := true;
    else update schule.advent_gutschein set zustand = 'offen', erledigt_am = null, erledigt_von = null, geaendert_am = now() where id = g.id returning * into g; end if;
  end if;
  if not v_unv then
    insert into schule.advent_protokoll (lernender_id, aktion, nr, gutschein_id, von, daten)
    values (g.lernender_id, 'eltern_' || p_aktion, g.nr, g.id, p_von, jsonb_build_object('titel', g.titel));
  end if;
  return jsonb_build_object('ok', true, 'unveraendert', v_unv, 'gutschein', schule.advent_gutschein_json(g, true));
end $function$;

create or replace function schule.advent_eltern(p_n int)
 returns jsonb language sql stable set search_path to ''
as $function$
  with e as (select schule.advent_einstellung() ein, (schule.advent_einstellung()->>'jahr')::int j),
  k as (select l.id, l.anzeigename, l.ist_test, a.familie from e, schule.advent_teilnahme a join schule.lernender l on l.id = a.lernender_id and l.aktiv
         where a.jahr = e.j)
  select jsonb_build_object('ok', true, 'einstellung', (select e.ein from e),
    'kinder', coalesce((select jsonb_agg(jsonb_build_object('lernender_id', k.id, 'name', k.anzeigename, 'ist_test', k.ist_test, 'familie', k.familie,
        'lage', schule.advent_lage(k.id) - 'offen_nrs', 'offen', (select count(*) from schule.advent_tuer t, e where t.lernender_id = k.id and t.jahr = e.j),
        'belegt', (select count(*) from schule.advent_belegung b, e where b.lernender_id = k.id and b.jahr = e.j),
        'zaehler', schule.advent_zaehler(k.id),
        'gutscheine', (select coalesce(jsonb_agg(schule.advent_gutschein_json(g, true) order by g.art = 'krampus', case g.zustand when 'offen' then 0 else 1 end, g.nr, g.id), '[]'::jsonb)
                         from schule.advent_gutschein g where g.lernender_id = k.id)) order by k.id) from k), '[]'::jsonb),
    'ohne_teilnahme', coalesce((select jsonb_agg(jsonb_build_object('lernender_id', l.id, 'name', l.anzeigename, 'ist_test', l.ist_test) order by l.id)
                                  from schule.lernender l where l.aktiv and not exists (select 1 from k where k.id = l.id)), '[]'::jsonb),
    'protokoll', coalesce((select jsonb_agg(to_jsonb(p) order by p.id desc) from (select * from schule.advent_protokoll order by id desc limit greatest(least(coalesce(p_n, 10), 100), 0)) p), '[]'::jsonb));
$function$;

create or replace function schule.advent_belegung_lesen(p_l bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  with e as (select (schule.advent_einstellung()->>'jahr')::int j)
  select jsonb_build_object('ok', true, 'jahr', (select j from e), 'kinder', coalesce(jsonb_agg(jsonb_build_object('lernender_id', l.id, 'name', l.anzeigename, 'ist_test', l.ist_test,
    'tueren', (select jsonb_agg(jsonb_build_object('nr', n,
                 'belegung', (select jsonb_build_object('art', b.art, 'variante', b.variante, 'titel', b.titel, 'text', b.text, 'sterne', b.sterne, 'motiv', b.motiv,
                                                        'geaendert_am', b.geaendert_am, 'geaendert_von', b.geaendert_von)
                                from schule.advent_belegung b where b.jahr = e.j and b.lernender_id = l.id and b.nr = n),
                 'offen', t.id is not null, 'geoeffnet_am', t.geoeffnet_am, 'tag', t.tag, 'nachgeholt', t.nachgeholt, 'inhalt_beim_oeffnen', t.inhalt,
                 'sterne_gutgeschrieben', t.sterne_gebucht,
                 'etappe', case when t.id is not null then jsonb_build_object('einheit_id', t.ausl_einheit, 'lernziel', t.ausl_lernziel, 'sitzt_am', t.ausl_sitzt_am, 'landung_art', t.ausl_art) end,
                 'gutschein', (select schule.advent_gutschein_json(g, true) from schule.advent_gutschein g where g.tuer_id = t.id)) order by n)
                 from generate_series(1, 24) n left join schule.advent_tuer t on t.lernender_id = l.id and t.jahr = e.j and t.nr = n)) order by l.id), '[]'::jsonb))
    from e, schule.lernender l
   where l.aktiv and (l.id = p_l or (p_l is null and exists (select 1 from schule.advent_teilnahme a where a.jahr = e.j and a.lernender_id = l.id)));
$function$;

create or replace function schule.advent_protokoll_lesen(p_l bigint, p_n int)
 returns jsonb language sql stable set search_path to ''
as $function$
  select jsonb_build_object('ok', true, 'eintraege', coalesce(jsonb_agg(to_jsonb(q) order by q.id desc), '[]'::jsonb))
    from (select p.*, l.anzeigename as name from schule.advent_protokoll p left join schule.lernender l on l.id = p.lernender_id
           where p_l is null or p.lernender_id = p_l order by p.id desc limit greatest(least(coalesce(p_n, 50), 500), 1)) q;
$function$;

revoke all on function schule.advent_jetzt(), schule.advent_einstellung(), schule.advent_tz(bigint), schule.advent_von(text), schule.advent_lock(bigint),
  schule.advent_landungen(bigint, text, date), schule.advent_lage(bigint), schule.advent_gutschein_json(schule.advent_gutschein, boolean),
  schule.advent_tuer_json(schule.advent_tuer), schule.advent_zaehler(bigint), schule.advent_nicht_aktiv(jsonb), schule.advent_stand(bigint),
  schule.advent_oeffnen(bigint, text, text, integer), schule.advent_tuer_lesen(bigint, integer), schule.advent_gutscheine(bigint), schule.advent_einloesen(bigint, bigint, text),
  schule.advent_tauschen(bigint, bigint, bigint, bigint, text, text), schule.advent_eintrag(jsonb), schule.advent_belegen(bigint[], jsonb, boolean, text),
  schule.advent_gutschein_eltern(bigint, text, text), schule.advent_eltern(integer), schule.advent_belegung_lesen(bigint), schule.advent_protokoll_lesen(bigint, integer)
  from public, anon, authenticated;

-- ---------- 6. Aktionen (lernen-api 0.10.0) ----------
-- gemeinsame Prüfung: angemeldet, Zugriff auf das Kind, Kind aktiv
create or replace function schule.advent_kind_pruefen(p_schluessel text, p_daten jsonb)
 returns bigint language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint;
begin
  if v_l is null then raise exception 'lernender_id fehlt' using errcode = 'P0001'; end if;
  perform schule.zugriff(p_schluessel, v_l);
  if not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return v_l;
end $function$;

-- Kind-Rolle: ein Kind darf öffnen/einlösen/tauschen; Eltern, Lehrer und der App-Zugang nur fürs Testkind (beim Nachsehen geht nichts aus Versehen auf)
create or replace function schule.advent_handelt_als_kind(p_schluessel text, p_l bigint)
 returns void language plpgsql security definer set search_path to ''
as $function$
begin
  if schule.ist_lern(p_schluessel) and exists (select 1 from schule.lern_ich(p_schluessel) i where i.rolle = 'kind' and i.lernender_id = p_l) then return; end if;
  if exists (select 1 from schule.lernender l where l.id = p_l and l.ist_test) then return; end if;
  raise exception 'Das geht nur in der App des Kindes (Eltern: nur fürs Testkind)' using errcode = 'P0001';
end $function$;

create or replace function schule.advent_cid(p_daten jsonb)
 returns text language plpgsql immutable set search_path to ''
as $function$
declare c text := btrim(coalesce(p_daten->>'client_id', ''));
begin
  if c = '' or char_length(c) > 200 then raise exception 'client_id fehlt (1 bis 200 Zeichen)' using errcode = 'P0001'; end if;
  return c;
end $function$;

-- erwartet_nr: fehlt oder null -> null (heutiger App-Stand, Verhalten wie bisher); sonst ganze Zahl 1–24 (Zahl oder Ziffern-Text)
create or replace function schule.advent_erwartet(p_daten jsonb)
 returns int language plpgsql immutable set search_path to ''
as $function$
declare j jsonb := p_daten->'erwartet_nr'; v text;
begin
  if j is null or jsonb_typeof(j) = 'null' then return null; end if;
  v := btrim(j #>> '{}');
  if jsonb_typeof(j) not in ('number', 'string') or v !~ '^[0-9]{1,2}$' or v::int not between 1 and 24 then
    raise exception 'erwartet_nr: 1 bis 24' using errcode = 'P0001'; end if;
  return v::int;
end $function$;

create or replace function api.schule_advent_stand(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$ begin return schule.advent_stand(schule.advent_kind_pruefen(p_schluessel, p_daten)); end $function$;

create or replace function api.schule_advent_oeffnen(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := schule.advent_kind_pruefen(p_schluessel, p_daten);
begin
  perform schule.advent_handelt_als_kind(p_schluessel, v_l);
  return schule.advent_oeffnen(v_l, schule.advent_cid(p_daten), schule.advent_von(p_schluessel), schule.advent_erwartet(p_daten));
end $function$;

create or replace function api.schule_advent_tuer_lesen(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$ begin return schule.advent_tuer_lesen(schule.advent_kind_pruefen(p_schluessel, p_daten), nullif(p_daten->>'nr', '')::int); end $function$;

create or replace function api.schule_advent_gutscheine(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$ begin return schule.advent_gutscheine(schule.advent_kind_pruefen(p_schluessel, p_daten)); end $function$;

create or replace function api.schule_advent_einloesen(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := schule.advent_kind_pruefen(p_schluessel, p_daten);
begin
  perform schule.advent_handelt_als_kind(p_schluessel, v_l);         -- Eltern: schule_advent_gutschein_eltern
  return schule.advent_einloesen(v_l, nullif(p_daten->>'gutschein_id', '')::bigint, schule.advent_von(p_schluessel));
end $function$;

create or replace function api.schule_advent_tauschen(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := schule.advent_kind_pruefen(p_schluessel, p_daten);
begin
  perform schule.advent_handelt_als_kind(p_schluessel, v_l);
  return schule.advent_tauschen(v_l, nullif(p_daten->>'tauschkarte_id', '')::bigint, nullif(p_daten->>'mein_gutschein_id', '')::bigint,
                                nullif(p_daten->>'fremder_gutschein_id', '')::bigint, schule.advent_cid(p_daten), schule.advent_von(p_schluessel));
end $function$;

create or replace function api.schule_advent_eltern(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_eltern(p_schluessel) then raise exception 'Nur Eltern' using errcode = 'P0001'; end if;
  return schule.advent_eltern(nullif(p_daten->>'protokoll', '')::int);
end $function$;

create or replace function api.schule_advent_belegung_lesen(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_eltern(p_schluessel) then raise exception 'Nur Eltern' using errcode = 'P0001'; end if;
  if v_l is not null then perform schule.advent_kind_pruefen(p_schluessel, p_daten); end if;
  return schule.advent_belegung_lesen(v_l);
end $function$;

create or replace function api.schule_advent_belegung_setzen(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_k bigint[]; v_l bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_eltern(p_schluessel) then raise exception 'Nur Eltern' using errcode = 'P0001'; end if;
  if p_daten ? 'lernender_ids' then
    if jsonb_typeof(p_daten->'lernender_ids') <> 'array' then raise exception 'lernender_ids als Liste' using errcode = 'P0001'; end if;
    select array_agg((x #>> '{}')::bigint) into v_k from jsonb_array_elements(p_daten->'lernender_ids') x;
  elsif nullif(p_daten->>'lernender_id', '') is not null then v_k := array[(p_daten->>'lernender_id')::bigint];
  end if;
  foreach v_l in array coalesce(v_k, '{}') loop perform schule.advent_kind_pruefen(p_schluessel, jsonb_build_object('lernender_id', v_l)); end loop;
  return schule.advent_belegen(v_k, p_daten->'tueren', coalesce((p_daten->>'nur_geschlossene')::boolean, false), schule.advent_von(p_schluessel));
end $function$;

create or replace function api.schule_advent_gutschein_eltern(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_eltern(p_schluessel) then raise exception 'Nur Eltern' using errcode = 'P0001'; end if;
  return schule.advent_gutschein_eltern(nullif(p_daten->>'gutschein_id', '')::bigint, p_daten->>'aktion', schule.advent_von(p_schluessel));
end $function$;

create or replace function api.schule_advent_protokoll(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_eltern(p_schluessel) then raise exception 'Nur Eltern' using errcode = 'P0001'; end if;
  return schule.advent_protokoll_lesen(v_l, nullif(p_daten->>'anzahl', '')::int);
end $function$;

revoke all on function schule.advent_kind_pruefen(text, jsonb), schule.advent_handelt_als_kind(text, bigint), schule.advent_cid(jsonb), schule.advent_erwartet(jsonb)
  from public, anon, authenticated;
revoke all on function api.schule_advent_stand(text, jsonb), api.schule_advent_oeffnen(text, jsonb), api.schule_advent_tuer_lesen(text, jsonb),
  api.schule_advent_gutscheine(text, jsonb), api.schule_advent_einloesen(text, jsonb), api.schule_advent_tauschen(text, jsonb), api.schule_advent_eltern(text, jsonb),
  api.schule_advent_belegung_lesen(text, jsonb), api.schule_advent_belegung_setzen(text, jsonb), api.schule_advent_gutschein_eltern(text, jsonb),
  api.schule_advent_protokoll(text, jsonb) from public, anon, authenticated;
do $advent_recht$ begin
  if exists (select 1 from pg_roles where rolname = 'council_mcp') then
    grant execute on function api.schule_advent_stand(text, jsonb), api.schule_advent_oeffnen(text, jsonb), api.schule_advent_tuer_lesen(text, jsonb),
      api.schule_advent_gutscheine(text, jsonb), api.schule_advent_einloesen(text, jsonb), api.schule_advent_tauschen(text, jsonb), api.schule_advent_eltern(text, jsonb),
      api.schule_advent_belegung_lesen(text, jsonb), api.schule_advent_belegung_setzen(text, jsonb), api.schule_advent_gutschein_eltern(text, jsonb),
      api.schule_advent_protokoll(text, jsonb) to council_mcp;
  end if;
end $advent_recht$;

-- ---------- 7. Einstellung prüfen, Sterne-Grund 'advent' (zuletzt: Sperre auf schule.sterne nur bis zum Ende der Transaktion) ----------
do $advent_ende$
declare d text := (select pg_get_constraintdef(c.oid) from pg_constraint c where c.conrelid = 'schule.sterne'::regclass and c.conname = 'sterne_grund_check');
begin
  perform schule.advent_einstellung();                                -- ungültige Regel -> Abbruch, nichts geändert
  if position('''advent''' in d) > 0 then raise exception 'ADVENT-S ABBRUCH: sterne_grund_check enthält schon advent – nichts geändert'; end if;   -- Vorprüfung schließt das aus
  alter table schule.sterne drop constraint sterne_grund_check;
  alter table schule.sterne add constraint sterne_grund_check check (grund = any (array['uebung', 'test', 'ort', 'einloesung', 'korrektur_hand', 'bonus', 'expedition',
                                                                                       'wdh', 'etappe_abgelegt', 'flug_abgelegt', 'landung', 'advent']));
end $advent_ende$;

-- ---------- Probe: Bericht (am Ende absichtlich Fehler -> ALLES zurückgerollt) ----------
do $advent_probe$
declare v record; e jsonb; k jsonb := '[]'::jsonb; r record; befund text[] := '{}'; hinweis text[] := '{}';
  bm jsonb := jsonb_build_object('lern_ich', '87caa4fa1f41b887f077fd2a61ff011b', 'ist_lern', '6ae7797d89a581d2707b6e7c5311de86', 'wer_tn', 'b2aeaeba4d4b9fd46a3d11482605aff7', 'ist_eltern', 'f98748d5c603e5b80a46417d2278f91e', 'sieht', '1482384a60fdc66c83589429ae34a84c', 'zugriff', 'f99e88b5fd488d8d51d2d3e3bc562d24'); b jsonb := '{}'::jsonb;
  n_tab int; n_fn int; n_lan int; n_lan_am int; n_lan_fehlt int; kurz jsonb; f text; m text; n_st bigint; s_st bigint; m_st text; st_ok boolean; ka_ok boolean;
  n_fn_soll constant int := 38;
begin
  select * into v from advent_probe_vorher;
  e := schule.advent_einstellung();
  select count(*) into n_tab from pg_class c join pg_namespace n on n.oid = c.relnamespace where n.nspname = 'schule' and c.relname like 'advent\_%' and c.relkind = 'r';
  select count(*) into n_fn from pg_proc p join pg_namespace n on n.oid = p.pronamespace where (n.nspname = 'schule' and p.proname like 'advent\_%')
     or (n.nspname = 'api' and p.proname like 'schule\_advent\_%');
  if n_tab <> 6 then befund := befund || format('Tabellen %s statt 6', n_tab); end if;
  if n_fn <> n_fn_soll then befund := befund || format('Funktionen %s statt %s', n_fn, n_fn_soll); end if;
  if v.tabellen <> 0 or v.funktionen <> 0 or v.regeln <> 0 or v.grund_advent then
    befund := befund || format('Vorher nicht leer (Tabellen %s, Funktionen %s, Regeln %s, Grund advent %s)', v.tabellen, v.funktionen, v.regeln, v.grund_advent); end if;
  if (e->>'aktiv')::int <> 0 or (e->>'tausch')::int <> 0 then befund := befund || format('Schalter aktiv=%s tausch=%s statt 0/0', e->>'aktiv', e->>'tausch'); end if;
  -- schule.sterne echt vergleichen: Zeilenzahl, Summe und Inhalt (md5) vorher/nachher
  select count(*), coalesce(sum(x.menge), 0), md5(coalesce(string_agg(x::text, '|' order by x.id), '')) into n_st, s_st, m_st from schule.sterne x;
  st_ok := n_st = v.sterne_zeilen and s_st = v.sterne_summe and m_st = v.sterne_md5;
  if not st_ok then befund := befund || format('schule.sterne verändert (Zeilen %s -> %s, Summe %s -> %s, Inhalt %s)', v.sterne_zeilen, n_st, v.sterne_summe, s_st,
                                               case when m_st = v.sterne_md5 then 'gleich' else 'anders' end); end if;
  ka_ok := (select md5(coalesce(string_agg(x::text, '|' order by x.lernender_id, x.einheit_id, x.lernziel collate "C"), '')) from schule.karte_stand x) = v.karte_md5;
  if not ka_ok then befund := befund || 'schule.karte_stand verändert'::text; end if;
  foreach f in array array['lern_ich', 'ist_lern', 'wer_tn', 'ist_eltern', 'sieht', 'zugriff'] loop
    select md5(p.prosrc) into m from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'schule' and p.proname = f;
    b := b || jsonb_build_object(f, case when m = bm->>f then 'wie Repo' else 'ABWEICHEND ' || coalesce(m, 'fehlt') end);
    if m is distinct from bm->>f then befund := befund || format('Bestandsfunktion schule.%s weicht vom Repo ab (Zugriffsprüfung so nicht getestet)', f); end if;
  end loop;
  -- Landungen, die der Kalender erkennt (eigene Landung / „Sitzt wieder!“: landung.am = sitzt_am)
  select count(*) filter (where k2.landung_art is not null and k2.sitzt),
         count(*) filter (where k2.landung_art is not null and k2.sitzt and (k2.landung->>'am')::timestamptz = k2.sitzt_am),
         count(*) filter (where k2.landung_art is not null and k2.sitzt and k2.landung->>'am' is null)
    into n_lan, n_lan_am, n_lan_fehlt from schule.karte_stand k2;
  if n_lan > 0 and n_lan_am = 0 then befund := befund || format('Landungen erkannt 0 von %s – Annahme landung.am = sitzt_am gilt live nicht (STOPP)', n_lan); end if;
  for r in select l.id, l.ist_test, l.zeitzone, schule.advent_tz(l.id) tz from schule.lernender l where l.aktiv order by l.id loop
    k := k || jsonb_build_object('lernender_id', r.id, 'ist_test', r.ist_test, 'zeitzone', r.zeitzone, 'gueltig', r.tz is not null,
      'ortszeit', case when r.tz is not null then to_char(now() at time zone r.tz, 'YYYY-MM-DD HH24:MI') end,
      'lage', case when r.tz is not null then (schule.advent_lage(r.id) - 'offen_nrs' - 'start' - 'nachholen_bis' - 'sichtbar_bis' - 'jahr' - 'zeitzone' - 'max_pro_tag') end,
      'eigene_landungen_gesamt', (select count(*) from schule.karte_stand x where x.lernender_id = r.id and x.sitzt and x.landung_art is not null
                                     and (x.landung->>'am')::timestamptz = x.sitzt_am));
    if r.tz is null then hinweis := hinweis || format('ZEITZONE FEHLT/UNGÜLTIG: lernender %s (%s) – Kalender liefert „zeitzone_fehlt“', r.id, coalesce(r.zeitzone, 'leer')); end if;
  end loop;
  kurz := jsonb_build_object('befunde', cardinality(befund), 'hinweise', cardinality(hinweis), 'tabellen', n_tab, 'funktionen', n_fn, 'funktionen_soll', n_fn_soll,
    'aktiv', (e->>'aktiv')::int, 'tausch', (e->>'tausch')::int, 'sterne_unveraendert', st_ok, 'karte_unveraendert', ka_ok,
    'zeitzone_fehlt', (select coalesce(jsonb_agg((x->>'lernender_id')::int), '[]'::jsonb) from jsonb_array_elements(k) x where not (x->>'gueltig')::boolean),
    'landungen', n_lan_am || '/' || n_lan);
  if cardinality(befund) > 0 or n_tab <> 6 or n_fn <> n_fn_soll or not st_ok or not ka_ok or (e->>'aktiv')::int <> 0 or (e->>'tausch')::int <> 0 then
    raise exception E'ADVENT-S PROBELAUF NICHT bestanden (% Befunde), ALLES zurückgerollt. KURZ %\nBEFUNDE: %\nHINWEISE: %\nDETAILS: %',
      cardinality(befund), kurz::text, array_to_string(befund, ' | '), coalesce(nullif(array_to_string(hinweis, ' | '), ''), 'keine'),
      jsonb_build_object('einstellung', e, 'kinder', k, 'bestand_md5', b, 'landungen_ohne_am', n_lan_fehlt)::text;
  end if;
  raise exception E'ADVENT-S PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt). KURZ %\nBEFUNDE: keine\nHINWEISE: %\nVORHER/NACHHER: %\nDETAILS: %',
    kurz::text, coalesce(nullif(array_to_string(hinweis, ' | '), ''), 'keine'),
    format('Tabellen %s/%s, Funktionen %s/%s, Regeln advent_* %s/%s, Grund advent %s, Start %s, Nachholen bis %s, sichtbar bis %s, max %s/Tag, Sterne Zeilen %s/%s, Summe %s/%s',
      v.tabellen, n_tab, v.funktionen, n_fn, v.regeln, (select count(*) from schule.regel r2 where r2.schluessel like 'advent\_%'),
      case when v.grund_advent then 'schon da' else 'neu' end, e->>'start', e->>'nachholen_bis', e->>'sichtbar_bis', e->>'max_pro_tag', v.sterne_zeilen, n_st, v.sterne_summe, s_st),
    jsonb_build_object('einstellung', e, 'kinder', k, 'bestand_md5', b, 'landungen_ohne_am', n_lan_fehlt, 'lernpause_noetig', false)::text;
end $advent_probe$;
