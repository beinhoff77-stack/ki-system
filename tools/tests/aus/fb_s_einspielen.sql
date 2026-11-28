-- FB-S Fehler-Bordkarten (Einspielen). Erzeugt von tools/tests/fb_einspielen.py – nicht von Hand ändern. Regel und Ablauf: inhalte/plan/fehlerkarten.md.
-- Was: Eine Übungsaufgabe, deren jüngste Bearbeitung das Kind nicht selbst gelöst hat (falsch, mit Tipp oder erst im 2. Anlauf), kommt in Wiederholung und
-- Mischkarte zuerst – nach fehlerkarten_pause_lerntage Lerntagen Pause (die Sperre der letzten 3 Lerntage gilt weiter), höchstens fehlerkarten_max-mal in Folge,
-- erledigt nach einer eigenen Lösung. Ohne Kennzeichnung (die App bleibt unverändert). Schalter fehlerkarten_an: 0 aus (beim Einspielen), 1 an, 2 nur Testkinder.
-- Geändert: schule.wdh_aufgabe_waehlen (eine Stelle: erster Sortierschlüssel), schule.mischkarten (eine Stelle: „schon beantwortet“ bei eingeschaltetem
-- Schalter nur seit der Ausgabe – sonst verfiele eine ausgegebene Fehler-Bordkarte beim nächsten Laden). Neu: schule.fehlerkarte_regel/_an/_ab/_serie/_faellig.
-- Schutz: je Funktion genau zwei zulässige Zustände (alt -> ersetzen, neu -> nichts; neue Hilfen: fehlt -> anlegen, neu -> nichts); alles andere, auch ein
-- Zwischenzustand, = Abbruch. Alle Katalogeigenschaften vorher/nachher gegen festes Soll; Rechte der ersetzten Funktionen unverändert. Bezugsfunktionen nur lesend.
-- Vergleich mit Schalter AUS: Kandidatenmenge und Rangfolge (ohne Zufall, Gleichstände nach id auf- und absteigend) alt gegen neu für alle Karten aller
-- Kinder × (Wiederholung, Mischkarte) in EINER Anweisung (ein Schnappschuss – laufende Antworten stören nicht); jede Abweichung = Abbruch.
-- Danach innerhalb der Transaktion Schalter AN: nur Zahlen (keine Lerndaten), Schalter wird auf den vorherigen Wert zurückgesetzt.
-- alt-md5 wdh_aufgabe_waehlen 7a6d76c619d1edfb6cdd8ee4a4a5cb1f (Länge 537) -> neu 79812f106f135beece303734f68fe351 (Länge 592);
-- alt-md5 mischkarten 1d8a3466c1698cfe9d4d0dd00d5ca638 (Länge 5123) -> neu b5674cbb53d0636617275c3b833596d9 (Länge 5261).
-- Ein Aufruf, eine Transaktion, kein BEGIN/COMMIT, keine Untertransaktion. Keine Lernpause nötig (keine Tabellen-DDL, nur Funktionen und drei Regel-Zeilen).
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '300s', true);
do $fb$
declare
  m_w_alt constant text := '7a6d76c619d1edfb6cdd8ee4a4a5cb1f'; m_w_neu constant text := '79812f106f135beece303734f68fe351';
  m_m_alt constant text := '1d8a3466c1698cfe9d4d0dd00d5ca638'; m_m_neu constant text := 'b5674cbb53d0636617275c3b833596d9';
  v_w constant text := 'schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)'; v_m constant text := 'schule.mischkarten(bigint, bigint, integer)';
  fehler text[] := '{}'; r record; d text; st jsonb := '{}'; ei_vor jsonb := '{}'; acl_vor jsonb := '{}'; n_alt int := 0; n_neu int := 0; n_sonst int := 0;
  v_an_vorher jsonb; n_k int; n_e int; n_v int; n_abw int; n_da int; n_kinder int; t0 timestamptz; ms_aus numeric; ms_an numeric; zz jsonb; v_bericht jsonb; v_kurz text;
begin
  if to_regclass('schule.aufgabe') is null or to_regclass('schule.versuch') is null or to_regclass('schule.karte_stand') is null or to_regclass('schule.lernender') is null
     or to_regclass('schule.lerntag') is null or to_regclass('schule.regel') is null or to_regclass('schule.misch_ausgabe') is null or to_regclass('schule.einheit') is null then
    raise exception 'FB-S ABBRUCH, Vorbedingung: eine der Tabellen aufgabe/versuch/karte_stand/lernender/lerntag/regel/misch_ausgabe/einheit fehlt – nichts geändert'; end if;
  for r in select * from (values ('versuch', 'lernender_id'), ('versuch', 'aufgabe_id'), ('versuch', 'am'), ('versuch', 'richtig'), ('versuch', 'hilfe'), ('versuch', 'anlauf'),
                                 ('versuch', 'testsitzung_id'), ('versuch', 'id'), ('aufgabe', 'form'), ('aufgabe', 'zaehlt'), ('aufgabe', 'stufe'), ('lernender', 'ist_test'),
                                 ('lernender', 'zeitzone'), ('misch_ausgabe', 'ausgegeben_am'), ('regel', 'wert')) x(t, s) loop
    if not exists (select 1 from information_schema.columns c where c.table_schema = 'schule' and c.table_name = r.t and c.column_name = r.s) then
      fehler := fehler || format('Spalte fehlt: schule.%s.%s', r.t, r.s); end if;
  end loop;
  -- 1. Zustand und Eigenschaften je Funktion gegen festes Soll
  create temp table if not exists fb_soll (f text primary key, ei text) on commit drop;
  truncate fb_soll;
  insert into fb_soll values
    ('schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)', 'p_l bigint, p_e bigint, p_lz text, p_misch boolean|bigint|sql|v|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.mischkarten(bigint, bigint, integer)', 'p_lernender bigint, p_einheit bigint, p_anzahl integer DEFAULT 8|jsonb|plpgsql|v|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.fehlerkarte_regel(text, integer)', 'p text, p_std integer|integer|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.fehlerkarte_an(bigint)', 'p_l bigint|boolean|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.fehlerkarte_ab(bigint)', 'p_l bigint|date|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.fehlerkarte_serie(bigint, bigint)', 'p_l bigint, p_a bigint|integer|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.fehlerkarte_faellig(bigint, bigint, timestamp with time zone)', 'p_l bigint, p_a bigint, p_zuletzt timestamp with time zone|boolean|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.wdh_sperre_ab(bigint)', 'p_l bigint|date|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.lern_datum(bigint, timestamp with time zone)', 'p_l bigint, p_zeit timestamp with time zone|date|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.heute_tag(bigint)', 'p_l bigint|date|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.wdh_aufgabe_da(bigint, bigint, text)', 'p_l bigint, p_e bigint, p_lz text|boolean|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.misch_gueltig(bigint, schule.aufgabe, jsonb)', 'p_lernender bigint, a schule.aufgabe, p jsonb|boolean|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}');
  create temp table if not exists fb_neu (f text primary key, m text) on commit drop;
  truncate fb_neu;
  insert into fb_neu values
    ('schule.fehlerkarte_regel(text, integer)', '6bd1313358463fdd4ee4aae7d33e0643'),
    ('schule.fehlerkarte_an(bigint)', '87fb083576476efd8c617f7527dd17c0'),
    ('schule.fehlerkarte_ab(bigint)', 'da34692dd14739f2aa1584f102a47ce1'),
    ('schule.fehlerkarte_serie(bigint, bigint)', '92bdf8e958359730a167fe5da504297c'),
    ('schule.fehlerkarte_faellig(bigint, bigint, timestamp with time zone)', '6172975f4fdb19d0017ee2bcbe7208c7');
  for r in select s.f, s.ei, to_regprocedure(s.f) o from fb_soll s order by s.f collate "C" loop
    if r.o is null then
      if r.f in (select f from fb_neu) then st := st || jsonb_build_object(r.f, 'fehlt'); n_alt := n_alt + 1;
      else fehler := fehler || format('Funktion fehlt: %s', r.f); end if;
      continue;
    end if;
    select p.prosrc, concat_ws('|', pg_get_function_arguments(p.oid), pg_get_function_result(p.oid), l.lanname, p.provolatile, p.prosecdef, p.proisstrict, p.proretset,
                     p.proparallel, p.procost, p.prorows, p.proleakproof, coalesce(p.proconfig::text, ''))
      into d, v_kurz from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = r.o;
    ei_vor := ei_vor || jsonb_build_object(r.f, v_kurz);
    acl_vor := acl_vor || jsonb_build_object(r.f, (select coalesce(p.proacl::text, '') from pg_proc p where p.oid = r.o));
    if v_kurz is distinct from r.ei then fehler := fehler || format('%s: Eigenschaften %s, erwartet %s', r.f, v_kurz, r.ei); end if;
    if r.f = v_w then
      if md5(d) = m_w_alt then st := st || jsonb_build_object(r.f, 'alt'); n_alt := n_alt + 1;
      elsif md5(d) = m_w_neu then st := st || jsonb_build_object(r.f, 'neu'); n_neu := n_neu + 1;
      else fehler := fehler || format('%s weicht ab (md5 %s, Länge %s; erwartet %s oder %s)', r.f, md5(d), length(d), m_w_alt, m_w_neu); n_sonst := n_sonst + 1; end if;
    elsif r.f = v_m then
      if md5(d) = m_m_alt then st := st || jsonb_build_object(r.f, 'alt'); n_alt := n_alt + 1;
      elsif md5(d) = m_m_neu then st := st || jsonb_build_object(r.f, 'neu'); n_neu := n_neu + 1;
      else fehler := fehler || format('%s weicht ab (md5 %s, Länge %s; erwartet %s oder %s)', r.f, md5(d), length(d), m_m_alt, m_m_neu); n_sonst := n_sonst + 1; end if;
    elsif r.f in (select f from fb_neu) then
      if md5(d) = (select m from fb_neu where f = r.f) then st := st || jsonb_build_object(r.f, 'neu'); n_neu := n_neu + 1;
      else fehler := fehler || format('%s ist vorhanden, aber nicht im neuen Stand (md5 %s)', r.f, md5(d)); n_sonst := n_sonst + 1; end if;
    end if;
  end loop;
  -- Bezugsfunktionen (werden nicht geändert; die Regel stützt sich auf genau diese Fassung)
  for r in select * from (values
    ('schule.wdh_sperre_ab(bigint)', 'e3b104414d506c83dcd3f84b6d3f2283'),
    ('schule.lern_datum(bigint, timestamp with time zone)', 'b9261f7da175fb15ed4f3fea69009d93'),
    ('schule.heute_tag(bigint)', '830213a58d5fcfc463779b5b13ba9285'),
    ('schule.wdh_aufgabe_da(bigint, bigint, text)', '0ee8e92220272826c52ceb3aa68a4cc0'),
    ('schule.misch_gueltig(bigint, schule.aufgabe, jsonb)', '437509567899b8e75a48ee46c250a537')) x(f, m) loop
    if to_regprocedure(r.f) is null then fehler := fehler || format('Bezugsfunktion fehlt: %s', r.f); continue; end if;
    select md5(p.prosrc) into d from pg_proc p where p.oid = to_regprocedure(r.f);
    if d is distinct from r.m then fehler := fehler || format('Bezugsfunktion %s weicht vom Repo-Stand ab (md5 %s, erwartet %s)', r.f, d, r.m); end if;
  end loop;
  if n_sonst = 0 and n_alt > 0 and n_neu > 0 then
    fehler := fehler || format('Zwischenzustand (%s Funktionen alt/fehlend, %s neu): %s', n_alt, n_neu, st::text); end if;
  -- Regeln: fehlen oder gültig
  create temp table if not exists fb_regel (k text primary key, w jsonb, lo int, hi int, h text) on commit drop;
  truncate fb_regel;
  insert into fb_regel values
    ('fehlerkarten_an', '0'::jsonb, 0, 2, 'FB-S: Fehler-Bordkarten in Wiederholung und Mischkarte bevorzugt (0 aus, 1 an, 2 nur Testkinder)'),
    ('fehlerkarten_pause_lerntage', '2'::jsonb, 0, 30, 'FB-S: so viele Lerntage Pause zwischen Fehler und Wiederkehr (die Sperre wdh_sperre_lerntage gilt zusätzlich)'),
    ('fehlerkarten_max', '3'::jsonb, 0, 20, 'FB-S: höchstens so oft hintereinander bevorzugt zurück (Bearbeitungen ohne eigene Lösung in Folge); danach normale Auswahl');
  for r in select g.k, g.lo, g.hi, x.wert from fb_regel g join schule.regel x on x.schluessel = g.k loop
    if jsonb_typeof(r.wert) is distinct from 'number' or (r.wert #>> '{}')::numeric not between r.lo and r.hi or (r.wert #>> '{}')::numeric <> trunc((r.wert #>> '{}')::numeric) then
      fehler := fehler || format('Regel %s hat einen ungültigen Wert %s (erlaubt ganze Zahl %s–%s)', r.k, r.wert, r.lo, r.hi); end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception 'FB-S ABBRUCH, Vorbedingung (% Befunde), nichts geändert: %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;

  -- 2. Regeln anlegen (ein vorhandener Wert bleibt), Funktionen ersetzen/anlegen (nur im Zustand alt)
  insert into schule.regel (schluessel, wert, hinweis) select g.k, g.w, g.h from fb_regel g order by g.k on conflict (schluessel) do nothing;
  if n_alt > 0 then
    execute $fbx$
create or replace function schule.fehlerkarte_regel(p text, p_std integer)
 returns integer language sql stable set search_path to ''
as $function$
  select coalesce((select case when length(r.wert #>> '{}') between 1 and 3 and ((r.wert #>> '{}') collate "C") !~ '[^0-9]' then (r.wert #>> '{}')::int end
                     from schule.regel r where r.schluessel = p), p_std);
$function$
$fbx$;
    execute $fbx$revoke all on function schule.fehlerkarte_regel(text, integer) from public$fbx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $fbx$revoke all on function schule.fehlerkarte_regel(text, integer) from anon$fbx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $fbx$revoke all on function schule.fehlerkarte_regel(text, integer) from authenticated$fbx$; end if;
    execute $fbx$comment on function schule.fehlerkarte_regel(text, integer) is 'FB-S: Einstellwert aus schule.regel wie wd_regel; ein ungültiger Wert (keine ganze Zahl 0–999) gilt als Vorgabe, bricht also nie die Wiederholung'$fbx$;
    execute $fbx$
create or replace function schule.fehlerkarte_an(p_l bigint)
 returns boolean language sql stable set search_path to ''
as $function$
  select case schule.fehlerkarte_regel('fehlerkarten_an', 0)
           when 1 then true
           when 2 then coalesce((select l.ist_test from schule.lernender l where l.id = p_l), false)
           else false end;
$function$
$fbx$;
    execute $fbx$revoke all on function schule.fehlerkarte_an(bigint) from public$fbx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $fbx$revoke all on function schule.fehlerkarte_an(bigint) from anon$fbx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $fbx$revoke all on function schule.fehlerkarte_an(bigint) from authenticated$fbx$; end if;
    execute $fbx$comment on function schule.fehlerkarte_an(bigint) is 'FB-S: Schalter fehlerkarten_an (0 aus, 1 an, 2 nur Testkinder)'$fbx$;
    execute $fbx$
create or replace function schule.fehlerkarte_ab(p_l bigint)
 returns date language sql stable set search_path to ''
as $function$
  select coalesce((select min(q.datum) from (select t.datum from schule.lerntag t where t.lernender_id = p_l and t.fach = 'Mathematik' and t.datum < schule.heute_tag(p_l)
                                              order by t.datum desc limit greatest(schule.fehlerkarte_regel('fehlerkarten_pause_lerntage', 2), 0)) q), schule.heute_tag(p_l));
$function$
$fbx$;
    execute $fbx$revoke all on function schule.fehlerkarte_ab(bigint) from public$fbx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $fbx$revoke all on function schule.fehlerkarte_ab(bigint) from anon$fbx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $fbx$revoke all on function schule.fehlerkarte_ab(bigint) from authenticated$fbx$; end if;
    execute $fbx$comment on function schule.fehlerkarte_ab(bigint) is 'FB-S: Wartezeit wie wdh_sperre_ab – Fehler-Bordkarte erst, wenn die letzte Bearbeitung vor diesem Lerntag liegt (fehlerkarten_pause_lerntage Lerntage Pause dazwischen)'$fbx$;
    execute $fbx$
create or replace function schule.fehlerkarte_serie(p_l bigint, p_a bigint)
 returns integer language sql stable set search_path to ''
as $function$
  select count(*)::int from schule.versuch v
   where v.lernender_id = p_l and v.aufgabe_id = p_a and v.testsitzung_id is null and coalesce(v.anlauf, 1) <> 2
     and not exists (select 1 from schule.versuch s
                      where s.lernender_id = p_l and s.aufgabe_id = p_a and s.testsitzung_id is null and coalesce(s.anlauf, 1) <> 2
                        and coalesce(s.richtig, false) and coalesce(s.hilfe, 0) = 0 and (s.am, s.id) >= (v.am, v.id));
$function$
$fbx$;
    execute $fbx$revoke all on function schule.fehlerkarte_serie(bigint, bigint) from public$fbx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $fbx$revoke all on function schule.fehlerkarte_serie(bigint, bigint) from anon$fbx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $fbx$revoke all on function schule.fehlerkarte_serie(bigint, bigint) from authenticated$fbx$; end if;
    execute $fbx$comment on function schule.fehlerkarte_serie(bigint, bigint) is 'FB-S: Bearbeitungen (Versuch ohne Test, 2. Anlauf zählt zur Bearbeitung davor) dieser Aufgabe seit der letzten eigenen Lösung (richtig, 1. Anlauf, ohne Tipp); 0 = zuletzt selbst gelöst oder nie bearbeitet'$fbx$;
    execute $fbx$
create or replace function schule.fehlerkarte_faellig(p_l bigint, p_a bigint, p_zuletzt timestamp with time zone)
 returns boolean language sql stable set search_path to ''
as $function$
  select coalesce(case when p_zuletzt is null or not schule.fehlerkarte_an(p_l) then false
                       else schule.lern_datum(p_l, p_zuletzt) < schule.fehlerkarte_ab(p_l)
                            and not exists (select 1 from schule.aufgabe a where a.id = p_a and a.form = 'lueckenweg')
                            and schule.fehlerkarte_serie(p_l, p_a) between 1 and schule.fehlerkarte_regel('fehlerkarten_max', 3) end, false);
$function$
$fbx$;
    execute $fbx$revoke all on function schule.fehlerkarte_faellig(bigint, bigint, timestamp with time zone) from public$fbx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $fbx$revoke all on function schule.fehlerkarte_faellig(bigint, bigint, timestamp with time zone) from anon$fbx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $fbx$revoke all on function schule.fehlerkarte_faellig(bigint, bigint, timestamp with time zone) from authenticated$fbx$; end if;
    execute $fbx$comment on function schule.fehlerkarte_faellig(bigint, bigint, timestamp with time zone) is 'FB-S: fällige Fehler-Bordkarte (Schalter an, Wartezeit vorbei, kein Lückenweg, 1 bis fehlerkarten_max Bearbeitungen ohne eigene Lösung in Folge)'$fbx$;
    execute $fbx$
create or replace function schule.wdh_aufgabe_waehlen(p_l bigint, p_e bigint, p_lz text, p_misch boolean)
 returns bigint language sql volatile set search_path to ''
as $function$
  with c as (
    select a.id, coalesce(a.stufe, 2) stufe, (select max(v.am) from schule.versuch v where v.lernender_id = p_l and v.aufgabe_id = a.id) zuletzt
      from schule.aufgabe a
     where schule.aufgabe_zaehlt(a) and a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung' and a.freigegeben and (not p_misch or a.stufe in (2, 3)))
  select c.id from c
   where c.zuletzt is null or schule.lern_datum(p_l, c.zuletzt) < schule.wdh_sperre_ab(p_l)
   order by schule.fehlerkarte_faellig(p_l, c.id, c.zuletzt) desc, c.zuletzt nulls first, (c.stufe = 1), random() limit 1;
$function$
$fbx$;
    execute $fbx$
create or replace function schule.mischkarten(p_lernender bigint, p_einheit bigint, p_anzahl integer default 8)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_lz text; v_ids bigint[] := '{}'; v_neu jsonb; v_x jsonb; v_etappen text[] := '{}'; v_test boolean;
begin
  select coalesce(l.ist_test, false) into v_test from schule.lernender l where l.id = p_lernender;
  -- 1. verfallen markieren: anderer Flug, älter als 24 Stunden, oder nicht mehr gültig
  update schule.misch_ausgabe m set verfallen_am = now()
   where m.lernender_id = p_lernender and m.eingeloest_am is null and m.verfallen_am is null
     and (m.einheit_id is distinct from p_einheit or m.ausgegeben_am < now() - interval '24 hours'
          or exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = m.aufgabe_id and (not schule.fehlerkarte_an(p_lernender) or v.am >= m.ausgegeben_am)) -- WD-S 3: schon beantwortet; FB-S: bei eingeschalteten Fehler-Bordkarten nur seit der Ausgabe
          or exists (select 1 from schule.aufgabe a where a.id = m.aufgabe_id and schule.etappe_heute_beantwortet(p_lernender, a.einheit_id, a.variante_gruppe)) -- WD-S 3: Etappe heute schon dran
          or not exists (select 1 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
                          join schule.karte_stand k on k.lernender_id = p_lernender and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt
                          where a.id = m.aufgabe_id and a.pool = 'uebung' and a.stufe in (2, 3) and a.freigegeben
                            and (e.status in ('geprueft', 'freigegeben') or (e.status = 'entwurf' and v_test))));
  -- 2. dieselben Karten wieder ausgeben (je Etappe höchstens eine, älteste Ausgabe zuerst)
  select coalesce(array_agg(q.aufgabe_id order by q.ausgegeben_am, q.id), '{}'), coalesce(array_agg(q.etappe order by q.ausgegeben_am, q.id), '{}')
    into v_ids, v_etappen
    from (select distinct on (a.einheit_id, a.variante_gruppe) m.id, m.aufgabe_id, m.ausgegeben_am, a.einheit_id || '/' || a.variante_gruppe etappe
            from schule.misch_ausgabe m join schule.aufgabe a on a.id = m.aufgabe_id
           where m.lernender_id = p_lernender and m.einheit_id = p_einheit and m.eingeloest_am is null and m.verfallen_am is null
           order by a.einheit_id, a.variante_gruppe, m.ausgegeben_am, m.id) q;
  if cardinality(v_ids) > p_anzahl then v_ids := v_ids[1:p_anzahl]; end if;
  -- 3. auffüllen, wenn weniger als gewünscht offen sind – nur aus Etappen, die noch keine offene Karte haben
  if cardinality(v_ids) < p_anzahl then
    v_neu := schule.mischkarten_waehlen(p_lernender, p_einheit, 50);
    select et.x->>'lernziel' into v_lz from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality et(x, nr)
     where e.id = p_einheit and not exists (select 1 from schule.karte_stand k where k.lernender_id = p_lernender and k.einheit_id = e.id and k.lernziel = et.x->>'lernziel' and k.sitzt)
     order by et.nr limit 1;
    for v_x in select y.j from jsonb_array_elements(v_neu) with ordinality y(j, nr) order by y.nr loop
      exit when cardinality(v_ids) >= p_anzahl;
      continue when (v_x->>'id')::bigint = any(v_ids)
        or ((v_x->>'einheit_id') || '/' || (select a.variante_gruppe from schule.aufgabe a where a.id = (v_x->>'id')::bigint)) = any(v_etappen);
      v_ids := v_ids || (v_x->>'id')::bigint;
      v_etappen := v_etappen || ((v_x->>'einheit_id') || '/' || (select a.variante_gruppe from schule.aufgabe a where a.id = (v_x->>'id')::bigint));
      insert into schule.misch_ausgabe(lernender_id, aufgabe_id, einheit_id, lernziel) values (p_lernender, (v_x->>'id')::bigint, p_einheit, v_lz)
      on conflict (lernender_id, aufgabe_id) where eingeloest_am is null
      do update set ausgegeben_am = now(), verfallen_am = null, einheit_id = excluded.einheit_id, lernziel = excluded.lernziel;
    end loop;
  end if;
  -- 4. Antwort wie bisher (Anzeige der Bordkarte + einheit_id, quelle, stadt, etappe), sortiert: dieser Flug, dieser Kontinent, älter
  return (select coalesce(jsonb_agg(z.j order by z.vorrang, z.rang, z.nr), '[]'::jsonb) from (
    select schule.aufgabe_anzeige(a, true) || jsonb_build_object('einheit_id', a.einheit_id,
             'quelle', case when a.einheit_id = p_einheit then 'flug' when b.kontinent_id = (select b2.kontinent_id from schule.einheit e2 join schule.block b2 on b2.id = e2.block_id where e2.id = p_einheit) then 'kontinent' else 'aelter' end,
             'stadt', b.stadt,
             'etappe', (select et->>'titel' from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) et where et->>'lernziel' = a.variante_gruppe limit 1)) j,
           case when a.einheit_id = p_einheit then 1 when b.kontinent_id = (select b2.kontinent_id from schule.einheit e2 join schule.block b2 on b2.id = e2.block_id where e2.id = p_einheit) then 2 else 3 end rang,
           u.nr, case when coalesce((select schule.karte_faellig(k) from schule.karte_stand k
                                       where k.lernender_id = p_lernender and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe), false) then 0 else 1 end vorrang -- WD-3
      from unnest(v_ids) with ordinality u(id, nr) join schule.aufgabe a on a.id = u.id join schule.einheit e on e.id = a.einheit_id join schule.block b on b.id = e.block_id) z);
end $function$
$fbx$;
  end if;

  -- 3. Nachher: alle im neuen Stand, Eigenschaften = Soll, Rechte der ersetzten Funktionen unverändert, neue Hilfen nicht für public/anon/authenticated
  for r in select s.f, s.ei, to_regprocedure(s.f) o from fb_soll s order by s.f collate "C" loop
    if r.o is null then fehler := fehler || format('nachher fehlt: %s', r.f); continue; end if;
    select p.prosrc, concat_ws('|', pg_get_function_arguments(p.oid), pg_get_function_result(p.oid), l.lanname, p.provolatile, p.prosecdef, p.proisstrict, p.proretset,
                     p.proparallel, p.procost, p.prorows, p.proleakproof, coalesce(p.proconfig::text, ''))
      into d, v_kurz from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = r.o;
    if v_kurz is distinct from r.ei then fehler := fehler || format('nachher %s: Eigenschaften %s, erwartet %s', r.f, v_kurz, r.ei); end if;
    if r.f = v_w and md5(d) <> m_w_neu then fehler := fehler || format('nachher %s: md5 %s statt %s', r.f, md5(d), m_w_neu); end if;
    if r.f = v_m and md5(d) <> m_m_neu then fehler := fehler || format('nachher %s: md5 %s statt %s', r.f, md5(d), m_m_neu); end if;
    if r.f in (select f from fb_neu) then
      if md5(d) <> (select m from fb_neu where f = r.f) then fehler := fehler || format('nachher %s: md5 %s', r.f, md5(d)); end if;
      if (select coalesce(p.proacl::text, '') from pg_proc p where p.oid = r.o) ~ '(^|[{,])=' then fehler := fehler || format('nachher %s: für public ausführbar', r.f); end if;
      if exists (select 1 from pg_roles where rolname in ('anon', 'authenticated') and has_function_privilege(rolname, r.o, 'execute')) then
        fehler := fehler || format('nachher %s: für anon/authenticated ausführbar', r.f); end if;
    elsif ei_vor ? r.f and (select coalesce(p.proacl::text, '') from pg_proc p where p.oid = r.o) is distinct from acl_vor->>r.f then
      fehler := fehler || format('nachher %s: Rechte geändert', r.f);
    end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception 'FB-S ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;

  -- 4. Vergleich mit Schalter AUS: alte gegen neue Auswahl ohne Zufall (Probe-Kopien im temporären Schema, aus den geprüften Texten)
  execute $fbx$
create or replace function pg_temp.fb_rang_alt(p_l bigint, p_e bigint, p_lz text, p_misch boolean)
 returns text language sql stable set search_path to ''
as $function$
  with c as (
    select a.id, coalesce(a.stufe, 2) stufe, (select max(v.am) from schule.versuch v where v.lernender_id = p_l and v.aufgabe_id = a.id) zuletzt
      from schule.aufgabe a
     where schule.aufgabe_zaehlt(a) and a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung' and a.freigegeben and (not p_misch or a.stufe in (2, 3)))
  select array(select c.id from c where c.zuletzt is null or schule.lern_datum(p_l, c.zuletzt) < schule.wdh_sperre_ab(p_l) order by c.zuletzt nulls first, (c.stufe = 1), c.id)::text || '|' || array(select c.id from c where c.zuletzt is null or schule.lern_datum(p_l, c.zuletzt) < schule.wdh_sperre_ab(p_l) order by c.zuletzt nulls first, (c.stufe = 1), c.id desc)::text;
$function$
$fbx$;
  execute $fbx$
create or replace function pg_temp.fb_rang_neu(p_l bigint, p_e bigint, p_lz text, p_misch boolean)
 returns text language sql stable set search_path to ''
as $function$
  with c as (
    select a.id, coalesce(a.stufe, 2) stufe, (select max(v.am) from schule.versuch v where v.lernender_id = p_l and v.aufgabe_id = a.id) zuletzt
      from schule.aufgabe a
     where schule.aufgabe_zaehlt(a) and a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung' and a.freigegeben and (not p_misch or a.stufe in (2, 3)))
  select array(select c.id from c where c.zuletzt is null or schule.lern_datum(p_l, c.zuletzt) < schule.wdh_sperre_ab(p_l) order by schule.fehlerkarte_faellig(p_l, c.id, c.zuletzt) desc, c.zuletzt nulls first, (c.stufe = 1), c.id)::text || '|' || array(select c.id from c where c.zuletzt is null or schule.lern_datum(p_l, c.zuletzt) < schule.wdh_sperre_ab(p_l) order by schule.fehlerkarte_faellig(p_l, c.id, c.zuletzt) desc, c.zuletzt nulls first, (c.stufe = 1), c.id desc)::text;
$function$
$fbx$;
  select x.wert into v_an_vorher from schule.regel x where x.schluessel = 'fehlerkarten_an';
  update schule.regel set wert = '0'::jsonb where schluessel = 'fehlerkarten_an';
  create temp table if not exists fb_v (l bigint, e bigint, lz text, misch boolean, sitzt boolean, faellig boolean, alt text, neu text, da boolean, ok_e boolean) on commit drop;
  truncate fb_v;
  insert into fb_v   -- EINE Anweisung = ein Schnappschuss für alt und neu
  select k.lernender_id, k.einheit_id, k.lernziel, m.misch, coalesce(k.sitzt, false), coalesce(schule.karte_faellig(k), false),
         pg_temp.fb_rang_alt(k.lernender_id, k.einheit_id, k.lernziel, m.misch), pg_temp.fb_rang_neu(k.lernender_id, k.einheit_id, k.lernziel, m.misch),
         case when not m.misch then schule.wdh_aufgabe_da(k.lernender_id, k.einheit_id, k.lernziel) end,
         exists (select 1 from schule.einheit e where e.id = k.einheit_id and e.status in ('geprueft', 'freigegeben'))
    from schule.karte_stand k cross join (values (false), (true)) m(misch);
  select count(distinct l), count(distinct (l, e, lz)), count(*), count(*) filter (where alt is distinct from neu),
         count(*) filter (where not misch and da is distinct from (ok_e and neu not like '{}|%'))
    into n_kinder, n_e, n_v, n_abw, n_da from fb_v;
  if n_abw > 0 then
    raise exception 'FB-S ABBRUCH, alles zurückgerollt: mit Schalter AUS weicht die Auswahl in % von % Fällen ab (z. B. %)', n_abw, n_v,
      (select string_agg(format('Kind %s Einheit %s %s %s', l, e, lz, case when misch then 'Mischkarte' else 'Wiederholung' end), '; ')
         from (select * from fb_v where alt is distinct from neu order by l, e, lz collate "C", misch limit 5) z); end if;
  t0 := clock_timestamp();
  perform count(schule.wdh_aufgabe_waehlen(k.lernender_id, k.einheit_id, k.lernziel, false)) from schule.karte_stand k where k.sitzt;
  ms_aus := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);

  -- 5. Schalter AN (nur in dieser Transaktion): nur Zahlen
  update schule.regel set wert = '1'::jsonb where schluessel = 'fehlerkarten_an';
  create temp table if not exists fb_a (l bigint, e bigint, lz text, sitzt boolean, faellig boolean, r0 text, r1 text, da boolean) on commit drop;
  truncate fb_a;
  insert into fb_a
  select k.lernender_id, k.einheit_id, k.lernziel, coalesce(k.sitzt, false), coalesce(schule.karte_faellig(k), false),
         pg_temp.fb_rang_neu(k.lernender_id, k.einheit_id, k.lernziel, false), pg_temp.fb_rang_neu(k.lernender_id, k.einheit_id, k.lernziel, true),
         schule.wdh_aufgabe_da(k.lernender_id, k.einheit_id, k.lernziel)
    from schule.karte_stand k;
  if exists (select 1 from fb_a a join fb_v v on v.l = a.l and v.e = a.e and v.lz = a.lz and not v.misch where a.da is distinct from v.da) then
    raise exception 'FB-S ABBRUCH, alles zurückgerollt: wdh_aufgabe_da ändert sich mit dem Schalter'; end if;
  if exists (select 1 from fb_a a join fb_v v on v.l = a.l and v.e = a.e and v.lz = a.lz and not v.misch
              where (a.r0 like '{}|%') is distinct from (v.neu like '{}|%')) then
    raise exception 'FB-S ABBRUCH, alles zurückgerollt: mit Schalter AN hat eine Etappe eine andere Kandidatenmenge (leer/nicht leer)'; end if;
  with t as (select a.*, (string_to_array(trim(both '{}' from split_part(a.r0, '|', 1)), ','))[1]::bigint t0, (string_to_array(trim(both '{}' from split_part(a.r1, '|', 1)), ','))[1]::bigint t1 from fb_a a),
  f as (select t.*, t.t0 is not null and schule.fehlerkarte_faellig(t.l, t.t0, (select max(v.am) from schule.versuch v where v.lernender_id = t.l and v.aufgabe_id = t.t0)) fb0,
               t.t1 is not null and schule.fehlerkarte_faellig(t.l, t.t1, (select max(v.am) from schule.versuch v where v.lernender_id = t.l and v.aufgabe_id = t.t1)) fb1 from t)
  select jsonb_build_object(
      'etappen_mit_faelliger_fehlerkarte_je_kind', coalesce((select jsonb_object_agg(q.l::text, q.n) from (select l, count(*) n from f where sitzt and fb0 group by l) q), '{}'::jsonb),
      'davon_heute_in_der_wiederholung_faellig_je_kind', coalesce((select jsonb_object_agg(q.l::text, q.n) from (select l, count(*) n from f where sitzt and faellig and fb0 group by l) q), '{}'::jsonb),
      'mischkarten_etappen_mit_fehlerkarte', (select count(*) from f where sitzt and fb1))
    into zz;
  zz := zz || (with p as (
      select v.lernender_id l, v.aufgabe_id a, max(v.am) zuletzt from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
       where a.pool = 'uebung' and a.freigegeben and schule.aufgabe_zaehlt(a) and v.testsitzung_id is null group by v.lernender_id, v.aufgabe_id),
    s as (select p.*, schule.fehlerkarte_serie(p.l, p.a) serie, (select a.form = 'lueckenweg' from schule.aufgabe a where a.id = p.a) lw,
                 (select coalesce(a.stufe, 2) from schule.aufgabe a where a.id = p.a) stufe from p)
    select jsonb_build_object(
      'fehler_aufgaben_offen', count(*) filter (where serie between 1 and schule.fehlerkarte_regel('fehlerkarten_max', 3) and lw is not true),
      'fehler_aufgaben_heute_faellig', count(*) filter (where schule.fehlerkarte_faellig(l, a, zuletzt) and schule.lern_datum(l, zuletzt) < schule.wdh_sperre_ab(l)),
      'davon_stufe_1_nur_wiederholung', count(*) filter (where stufe = 1 and schule.fehlerkarte_faellig(l, a, zuletzt) and schule.lern_datum(l, zuletzt) < schule.wdh_sperre_ab(l)),
      'ueber_obergrenze_normal', count(*) filter (where serie > schule.fehlerkarte_regel('fehlerkarten_max', 3) and lw is not true),
      'lueckenwege_ausgenommen', count(*) filter (where serie >= 1 and lw is true),
      'kinder_mit_fehler_aufgaben', count(distinct l) filter (where serie >= 1 and lw is not true)) from s);
  t0 := clock_timestamp();
  perform count(schule.wdh_aufgabe_waehlen(k.lernender_id, k.einheit_id, k.lernziel, false)) from schule.karte_stand k where k.sitzt;
  ms_an := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
  zz := zz || jsonb_build_object('misch_offen_vorher_beantwortet', (select count(*) from schule.misch_ausgabe m where m.eingeloest_am is null and m.verfallen_am is null
                                   and exists (select 1 from schule.versuch v where v.lernender_id = m.lernender_id and v.aufgabe_id = m.aufgabe_id and v.am < m.ausgegeben_am)));
  update schule.regel set wert = v_an_vorher where schluessel = 'fehlerkarten_an';   -- Schalter zurück (beim ersten Lauf: 0)
  if (select x.wert from schule.regel x where x.schluessel = 'fehlerkarten_an') is distinct from v_an_vorher then raise exception 'FB-S ABBRUCH: Schalter nicht zurückgesetzt'; end if;

  v_kurz := format('Kinder %s, Etappen %s, Vergleiche %s, Abweichungen AUS %s | AN heute: Etappen mit fälliger Fehler-Bordkarte je Kind %s (davon heute fällig %s), Mischkarten-Etappen %s, Fehler-Aufgaben offen %s (heute fällig %s) | Laufzeit %s ms aus / %s ms an | %s',
    n_kinder, n_e, n_v, n_abw, zz->'etappen_mit_faelliger_fehlerkarte_je_kind', zz->'davon_heute_in_der_wiederholung_faellig_je_kind', zz->'mischkarten_etappen_mit_fehlerkarte',
    zz->'fehler_aufgaben_offen', zz->'fehler_aufgaben_heute_faellig', ms_aus, ms_an,
    case when n_alt > 0 then 'alt -> neu' else 'neu -> neu (schon eingespielt, nichts geändert)' end);
  v_bericht := zz || jsonb_build_object('zustand_vorher', st, 'md5_wdh_aufgabe_waehlen_neu', m_w_neu, 'md5_mischkarten_neu', m_m_neu,
    'kinder', n_kinder, 'etappen', n_e, 'vergleiche', n_v, 'abweichungen_aus', n_abw, 'da_ungleich_auswahl_info', n_da,
    'schalter', (select x.wert from schule.regel x where x.schluessel = 'fehlerkarten_an'),
    'regeln', (select jsonb_object_agg(x.schluessel, x.wert) from schule.regel x where x.schluessel in (select k from fb_regel)),
    'ms_auswahl_aus', ms_aus, 'ms_auswahl_an', ms_an, 'eigenschaften_gleich', true, 'fehler', 0);
  drop function pg_temp.fb_rang_alt(bigint, bigint, text, boolean);
  drop function pg_temp.fb_rang_neu(bigint, bigint, text, boolean);
  raise notice 'FB-S eingespielt – % – Details: %', v_kurz, v_bericht::text;
end $fb$;
