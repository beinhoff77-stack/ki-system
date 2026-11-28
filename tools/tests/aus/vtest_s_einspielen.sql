-- VTEST-S Verstehen in Tests, Server (Einspielen). Erzeugt von tools/tests/vtest_s_einspielen.py – nicht von Hand ändern.
-- Plan, Fundstellen, Ablauf: inhalte/plan/neuer-stil/server-schritt.md. Einspielen NACH NF-S, TEMPO-S1 und FB-S (deren neue Funktionstexte werden per md5 verlangt).
-- Was (nur bei eingeschaltetem Schalter; Schalter 0 = beim Einspielen = genau das bisherige Verhalten):
--   verstehen_test_an:    erster Flugtest – je Etappe mit freigegebener Verstehens-Testaufgabe genau diese eine statt der Rechen-Testaufgabe(n), Reihenfolge nach Etappen;
--                         Nachtragstest – Verstehens-Etappe zuerst Verstehen; Korrektur – gleiche Art wie die falsche Aufgabe der letzten Testsitzung der Etappe
--                         (Rückfall bei leerem Verstehens-Vorrat: schon gestellte Verstehens-Korrektur, am längsten her; dann wie bisher).
--   verstehen_landung_an: eine nie gelandete Etappe mit freigegebener zählender Verstehens-Übung landet erst, wenn eine Verstehens-Übung selbst gelöst (gezählt) ist;
--                         etappen_stand liefert dann je Etappe verstehen_noetig und verstehen_ok. Gelandete, wieder geöffnete, gesetzte Etappen: unverändert.
-- Geändert: test_starten_intern, etappen_stand, karte_landet (neuer Text = alter Text + Einfügungen). Neu: 7 Hilfsfunktionen, 2 Regeln (Wert 0; ein vorhandener Wert bleibt).
-- Schutz: je Funktion genau zwei Zustände (alt -> ersetzen, neu -> nichts; Hilfen fehlt -> anlegen), jeder Mischstand = Abbruch; Eigenschaften gegen festes Soll;
-- Rechte der ersetzten Funktionen unverändert. Vergleich mit Schalter AUS in je EINER Anweisung: etappen_stand (alle Kinder × Einheiten) und karte_landet (alle Karten,
-- dazu jede Karte als „nie gelandet“) alt gegen neu – jede Abweichung = Abbruch. Danach Schalter AN nur in dieser Transaktion: nur Zahlen, Schalter zurück.
-- Ein Aufruf, eine Transaktion, kein BEGIN/COMMIT, keine Untertransaktion. Keine Tabellen-DDL (nur Funktionen und zwei Regel-Zeilen) – keine Lernpause nötig.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '300s', true);
do $vs$
declare
  fehler text[] := '{}'; r record; d text; v_kurz text; st jsonb := '{}'; acl_vor jsonb := '{}'; n_alt int := 0; n_neu int := 0;
  v_t_vor jsonb; v_l_vor jsonb; n_e int; n_k int; n_abw_es int; n_abw_kl int; n_abw_kl_offen int; n_kinder int; n_einh int; zz jsonb; v_bericht jsonb; t0 timestamptz; ms_aus numeric; ms_an numeric;
begin
  if to_regclass('schule.aufgabe') is null or to_regclass('schule.versuch') is null or to_regclass('schule.karte_stand') is null or to_regclass('schule.lernender') is null
     or to_regclass('schule.testsitzung') is null or to_regclass('schule.regel') is null or to_regclass('schule.einheit') is null or to_regclass('schule.lernziel_stand') is null then
    raise exception 'VTEST-S ABBRUCH, Vorbedingung: eine der Tabellen aufgabe/versuch/karte_stand/lernender/testsitzung/regel/einheit/lernziel_stand fehlt – nichts geändert'; end if;
  for r in select * from (values ('aufgabe', 'typ'), ('aufgabe', 'form'), ('aufgabe', 'zaehlt'), ('aufgabe', 'pool'), ('aufgabe', 'freigegeben'), ('aufgabe', 'variante_gruppe'),
                                 ('aufgabe', 'reihenfolge'), ('versuch', 'testsitzung_id'), ('versuch', 'richtig'), ('versuch', 'am'), ('testsitzung', 'aufgaben'),
                                 ('testsitzung', 'status'), ('testsitzung', 'abgeschlossen_am'), ('testsitzung', 'gestartet_am'), ('karte_stand', 'gezaehlt'),
                                 ('karte_stand', 'sitzt_am'), ('lernender', 'ist_test'), ('einheit', 'inhalt'), ('regel', 'wert'), ('regel', 'hinweis')) x(t, s) loop
    if not exists (select 1 from information_schema.columns c where c.table_schema = 'schule' and c.table_name = r.t and c.column_name = r.s) then
      fehler := fehler || format('Spalte fehlt: schule.%s.%s', r.t, r.s); end if;
  end loop;
  -- 1. Zustand und Eigenschaften
  create temp table if not exists vs_soll (f text primary key, ei text) on commit drop;
  truncate vs_soll;
  insert into vs_soll values
    ('schule.test_starten_intern(bigint, jsonb)', 'p_lernender bigint, p_daten jsonb|jsonb|plpgsql|v|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.etappen_stand(bigint, bigint)', 'p_lernender bigint, p_einheit bigint|jsonb|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.karte_landet(schule.karte_stand)', 'k schule.karte_stand|boolean|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.verstehen_regel(text, integer)', 'p text, p_std integer|integer|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.verstehen_an(bigint, text)', 'p_l bigint, p_schalter text|boolean|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.aufgabe_verstehen(schule.aufgabe)', 'a schule.aufgabe|boolean|sql|i|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.karte_verstehen_noetig(bigint, text)', 'p_einheit bigint, p_lz text|boolean|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.karte_verstehen_pflicht(schule.karte_stand, bigint, bigint, text)', 'k schule.karte_stand, p_l bigint, p_einheit bigint, p_lz text|boolean|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.karte_verstehen_ok(schule.karte_stand)', 'k schule.karte_stand|boolean|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}'),
    ('schule.verstehen_korrektur_art(bigint, bigint, text)', 'p_l bigint, p_e bigint, p_lz text|boolean|sql|s|f|f|f|u|100|0|f|{"search_path=\"\""}');
  create temp table if not exists vs_hilfe (f text primary key, m text) on commit drop;
  truncate vs_hilfe;
  insert into vs_hilfe values
    ('schule.verstehen_regel(text, integer)', '6bd1313358463fdd4ee4aae7d33e0643'),
    ('schule.verstehen_an(bigint, text)', '059e072cc718304153ba38d8bdb41659'),
    ('schule.aufgabe_verstehen(schule.aufgabe)', 'a05aef21d552837a31f91eef732fa21e'),
    ('schule.karte_verstehen_noetig(bigint, text)', '543463ece1851460c7397a6fc338fd86'),
    ('schule.karte_verstehen_pflicht(schule.karte_stand, bigint, bigint, text)', '533b3e8f6574a7b27da460e1d10edf9a'),
    ('schule.karte_verstehen_ok(schule.karte_stand)', '6e1178b4c2108e901ee7f91d0df04ce0'),
    ('schule.verstehen_korrektur_art(bigint, bigint, text)', '5070549145f4d0f4710e763b47640ff1');
  create temp table if not exists vs_geaendert (f text primary key, m_alt text, m_neu text) on commit drop;
  truncate vs_geaendert;
  insert into vs_geaendert values
    ('schule.test_starten_intern(bigint, jsonb)', '7abcd2918f5042142d8720ae044b36c1', '059fb2fe81bd1e5725fddcb6f2f1df8b'),
    ('schule.etappen_stand(bigint, bigint)', '3f49198f8dbf5c822a0be4650a5ebce5', '9e594f546bd2f769374b2c5e3db85a6c'),
    ('schule.karte_landet(schule.karte_stand)', '2c03a8f547fe49e264e12fc6d03fe38b', 'e7b94fe57b34e86b38bd6d417becd488');
  for r in select s.f, s.ei, to_regprocedure(s.f) o from vs_soll s order by s.f collate "C" loop
    if r.o is null then
      if r.f in (select f from vs_hilfe) then st := st || jsonb_build_object(r.f, 'fehlt'); n_alt := n_alt + 1;
      else fehler := fehler || format('Funktion fehlt: %s', r.f); end if;
      continue;
    end if;
    select p.prosrc, concat_ws('|', pg_get_function_arguments(p.oid), pg_get_function_result(p.oid), l.lanname, p.provolatile, p.prosecdef, p.proisstrict, p.proretset,
                     p.proparallel, p.procost, p.prorows, p.proleakproof, coalesce(p.proconfig::text, ''))
      into d, v_kurz from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = r.o;
    acl_vor := acl_vor || jsonb_build_object(r.f, (select concat_ws('|', p.proowner::regrole::text, coalesce(p.proacl::text, '')) from pg_proc p where p.oid = r.o));
    if v_kurz is distinct from r.ei then fehler := fehler || format('%s: Eigenschaften %s, erwartet %s', r.f, v_kurz, r.ei); end if;
    if r.f in (select f from vs_geaendert) then
      if md5(d) = (select m_alt from vs_geaendert where f = r.f) then st := st || jsonb_build_object(r.f, 'alt'); n_alt := n_alt + 1;
      elsif md5(d) = (select m_neu from vs_geaendert where f = r.f) then st := st || jsonb_build_object(r.f, 'neu'); n_neu := n_neu + 1;
      elsif r.f = 'schule.test_starten_intern(bigint, jsonb)' and md5(d) = 'b226ac94131e47a507462e9be303ef8f' then fehler := fehler || 'test_starten_intern: NF-S ist noch nicht eingespielt – erst NF-S';
      elsif r.f = 'schule.etappen_stand(bigint, bigint)' and md5(d) = 'bf3152e9a378a1d4e41c98965acf738e' then fehler := fehler || 'etappen_stand: TEMPO-S1 ist noch nicht eingespielt – erst TEMPO-S1';
      else fehler := fehler || format('%s weicht ab (md5 %s, Länge %s; erwartet %s oder %s)', r.f, md5(d), length(d),
                                      (select m_alt from vs_geaendert where f = r.f), (select m_neu from vs_geaendert where f = r.f)); end if;
    elsif md5(d) = (select m from vs_hilfe where f = r.f) then st := st || jsonb_build_object(r.f, 'neu'); n_neu := n_neu + 1;
    else fehler := fehler || format('%s ist vorhanden, aber nicht im neuen Stand (md5 %s)', r.f, md5(d)); end if;
  end loop;
  if n_alt > 0 and n_neu > 0 then fehler := fehler || format('Mischstand (%s Funktionen alt/fehlend, %s neu) – kein Wiederanlauf auf einem Mischstand: %s', n_alt, n_neu, st::text); end if;
  -- Bezugsfunktionen (unverändert; die Regel stützt sich auf genau diese Fassung)
  for r in select * from (values
    ('schule.aufgabe_zaehlt(schule.aufgabe)', 'd0acd1fcd29eb0ce9e66ed7a7764b3fe'),
    ('schule.karte_anwenden_ok(schule.karte_stand)', 'edf9dc24505dc38c350325c07da8742a'),
    ('schule.karte_anwenden_pflicht(schule.karte_stand, bigint, text)', '898b0fd05ad1623afb913321d3976b05')) x(f, m) loop
    if to_regprocedure(r.f) is null then fehler := fehler || format('Bezugsfunktion fehlt: %s', r.f); continue; end if;
    if (select md5(p.prosrc) from pg_proc p where p.oid = to_regprocedure(r.f)) is distinct from r.m then
      fehler := fehler || format('Bezugsfunktion %s weicht vom Repo-Stand ab (md5 %s, erwartet %s)', r.f, (select md5(p.prosrc) from pg_proc p where p.oid = to_regprocedure(r.f)), r.m); end if;
  end loop;
  -- Voraussetzungen anderer Schritte (FB-S): deren neuer Stand muss stehen
  for r in select * from (values
    ('schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)', '79812f106f135beece303734f68fe351', '7a6d76c619d1edfb6cdd8ee4a4a5cb1f', 'FB-S'),
    ('schule.mischkarten(bigint, bigint, integer)', 'b5674cbb53d0636617275c3b833596d9', '1d8a3466c1698cfe9d4d0dd00d5ca638', 'FB-S')) x(f, m, m_vor, schritt) loop
    if to_regprocedure(r.f) is null then fehler := fehler || format('Voraussetzung fehlt: %s', r.f); continue; end if;
    select md5(p.prosrc) into d from pg_proc p where p.oid = to_regprocedure(r.f);
    if d = r.m_vor then fehler := fehler || format('%s: %s ist noch nicht eingespielt – erst %s', r.f, r.schritt, r.schritt);
    elsif d is distinct from r.m then fehler := fehler || format('Voraussetzung %s (%s) weicht ab (md5 %s, erwartet %s)', r.f, r.schritt, d, r.m); end if;
  end loop;
  -- karte_buchen muss die Landeregel genau an dieser Stelle rufen (sonst wirkt die Pflicht nicht)
  if to_regprocedure('schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)') is null then fehler := fehler || 'karte_buchen fehlt';
  elsif (select (length(p.prosrc) - length(replace(p.prosrc, 'if not v_war_gelandet and schule.karte_landet(k) then', ''))) / length('if not v_war_gelandet and schule.karte_landet(k) then') from pg_proc p
          where p.oid = 'schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)'::regprocedure) <> 1 then
    fehler := fehler || 'karte_buchen: Stelle „if not v_war_gelandet and schule.karte_landet(k) then“ nicht genau einmal'; end if;
  -- Regeln: fehlen oder gültig (ganze Zahl 0–2)
  create temp table if not exists vs_regel (k text primary key, w jsonb, h text) on commit drop;
  truncate vs_regel;
  insert into vs_regel values
    ('verstehen_test_an', '0'::jsonb, 'VTEST-S: Tests – Verstehens-Etappe zieht die Verstehens-Testaufgabe, Korrektur gleicher Art (0 aus, 1 alle, 2 nur Testkinder)'),
    ('verstehen_landung_an', '0'::jsonb, 'VTEST-S: Üben – nie gelandete Etappe landet erst mit einer richtigen Verstehens-Aufgabe (0 aus, 1 alle, 2 nur Testkinder; erst mit App)');
  for r in select g.k, x.wert from vs_regel g join schule.regel x on x.schluessel = g.k loop
    if jsonb_typeof(r.wert) is distinct from 'number' or (r.wert #>> '{}')::numeric not in (0, 1, 2) then
      fehler := fehler || format('Regel %s hat einen ungültigen Wert %s (erlaubt 0, 1, 2)', r.k, r.wert); end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception 'VTEST-S ABBRUCH, Vorbedingung (% Befunde), nichts geändert: %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;

  -- 2. Regeln anlegen (ein vorhandener Wert bleibt); für den Vergleich in dieser Transaktion AUS, danach zurück
  insert into schule.regel (schluessel, wert, hinweis) select g.k, g.w, g.h from vs_regel g order by g.k on conflict (schluessel) do nothing;
  select x.wert into v_t_vor from schule.regel x where x.schluessel = 'verstehen_test_an';
  select x.wert into v_l_vor from schule.regel x where x.schluessel = 'verstehen_landung_an';
  update schule.regel set wert = '0'::jsonb where schluessel in ('verstehen_test_an', 'verstehen_landung_an');
  -- alte Fassungen als Kopie in pg_temp (für den Vergleich in EINER Anweisung)
  execute $vsx$create or replace function pg_temp.vs_es_alt(p_lernender bigint, p_einheit bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  -- TEMPO-S1: gleiches Ergebnis wie die Fassung nach FT-S; je Einheit einmal: flug_nachtest, gesamt/geloest (gruppiert); je Etappe einmal: karte_ziel
  select coalesce(jsonb_object_agg(z.lz, jsonb_build_object('geloest', z.geloest, 'gesamt', z.gesamt,
           'serie', coalesce(k.serie, 0), 'ziel', z.ziel, 'sitzt', coalesce(k.sitzt, false), 'schwer_ok', coalesce(k.schwer_ok, false), 'anwenden_noetig', schule.karte_anwenden_pflicht(k, p_einheit, z.lz), 'anwenden_ok', coalesce(schule.karte_anwenden_ok(k), false),
           'bearbeitungen', schule.karte_bearbeitungen(p_lernender, p_einheit, z.lz), 'schwer_noetig', schule.karte_schwer_noetig(p_einheit, z.lz),
           'faellig', coalesce(schule.karte_faellig(k), false), 'wdh_stufe', coalesce(k.wdh_stufe, 0),
           'eigene_loesungen', coalesce(k.eigene_loesungen, 0), 'folge', coalesce(k.folge, 0), 'folge_ziel', least(3, z.ziel),
           'typen_anzahl', coalesce(array_length(k.typen, 1), 0), 'typen_noetig', schule.karte_typen_noetig(p_einheit, z.lz),
           'fehler_folge', coalesce(k.fehler_folge, 0), 'stufe_senkung', coalesce(k.stufe_senkung, 0), 'sicher', coalesce(schule.karte_sicher(k), false), 'misch_ok', k.misch_ok_am is not null and k.misch_ok_am >= coalesce(k.sitzt_am, k.misch_ok_am), 'flug_nachtest', fn.v,
           'fertig', schule.etappe_fertig(k, s.status), 'test_nachgewiesen', coalesce(s.status in ('nachgewiesen','korrigiert','gesichert'), false), 'wieder_offen', not coalesce(k.sitzt, false) and k.sitzt_am is not null, 'gezaehlt', coalesce((select jsonb_agg(x::bigint) from jsonb_object_keys(k.gezaehlt) x), '[]'::jsonb))), '{}'::jsonb)
  from (select y.lz, coalesce(g.gesamt, 0) gesamt, coalesce(v.geloest, 0) geloest, schule.karte_ziel(p_einheit, y.lz) ziel
          from (select e->>'lernziel' lz, o.nr
                  from schule.einheit x, jsonb_array_elements(coalesce(x.inhalt->'etappen', '[]'::jsonb)) with ordinality o(e, nr) where x.id = p_einheit) y
          left join (select a.variante_gruppe lz, count(*) gesamt from schule.aufgabe a
                      where a.einheit_id = p_einheit and a.pool = 'uebung' and a.freigegeben group by a.variante_gruppe) g on g.lz = y.lz
          left join (select a.variante_gruppe lz, count(distinct v.aufgabe_id) geloest from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                      where v.lernender_id = p_lernender and v.richtig and v.testsitzung_id is null and a.einheit_id = p_einheit and a.pool = 'uebung'
                      group by a.variante_gruppe) v on v.lz = y.lz
         order by y.nr) z
  cross join (select schule.flug_nachtest(p_lernender, p_einheit) v offset 0) fn
  left join schule.lernziel_stand s on s.lernender_id = p_lernender and s.einheit_id = p_einheit and s.lernziel = z.lz
  left join schule.karte_stand k on k.lernender_id = p_lernender and k.einheit_id = p_einheit and k.lernziel = z.lz;
$function$$vsx$;
  execute $vsx$create or replace function pg_temp.vs_kl_alt(k schule.karte_stand)
 returns boolean language sql stable set search_path to ''
as $function$
  select coalesce(k.eigene_loesungen, 0) >= schule.karte_ziel(k.einheit_id, k.lernziel)
     and coalesce(array_length(k.typen, 1), 0) >= schule.karte_typen_noetig(k.einheit_id, k.lernziel)
     and (coalesce(k.schwer_ok, false) or not schule.karte_schwer_noetig(k.einheit_id, k.lernziel))
     and coalesce(k.folge, 0) >= least(3, schule.karte_ziel(k.einheit_id, k.lernziel))
     and (schule.karte_anwenden_ok(k) or not schule.karte_anwenden_pflicht(k, k.einheit_id, k.lernziel)); -- FT-S Regel 6
$function$$vsx$;

  -- 3. Anlegen / ersetzen (nur im Zustand alt)
  if n_alt > 0 then
    execute $vsx$create or replace function schule.verstehen_regel(p text, p_std integer)
 returns integer language sql stable set search_path to ''
as $function$
  select coalesce((select case when length(r.wert #>> '{}') between 1 and 3 and ((r.wert #>> '{}') collate "C") !~ '[^0-9]' then (r.wert #>> '{}')::int end
                     from schule.regel r where r.schluessel = p), p_std);
$function$$vsx$;
    execute $vsx$revoke all on function schule.verstehen_regel(text, integer) from public$vsx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $vsx$revoke all on function schule.verstehen_regel(text, integer) from anon$vsx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $vsx$revoke all on function schule.verstehen_regel(text, integer) from authenticated$vsx$; end if;
    execute $vsx$comment on function schule.verstehen_regel(text, integer) is 'VTEST-S: Einstellwert aus schule.regel (wie fehlerkarte_regel); ein ungültiger Wert gilt als Vorgabe'$vsx$;
    execute $vsx$create or replace function schule.verstehen_an(p_l bigint, p_schalter text)
 returns boolean language sql stable set search_path to ''
as $function$
  select case schule.verstehen_regel(p_schalter, 0)
           when 1 then true
           when 2 then coalesce((select l.ist_test from schule.lernender l where l.id = p_l), false)
           else false end;
$function$$vsx$;
    execute $vsx$revoke all on function schule.verstehen_an(bigint, text) from public$vsx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $vsx$revoke all on function schule.verstehen_an(bigint, text) from anon$vsx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $vsx$revoke all on function schule.verstehen_an(bigint, text) from authenticated$vsx$; end if;
    execute $vsx$comment on function schule.verstehen_an(bigint, text) is 'VTEST-S: Schalter verstehen_test_an / verstehen_landung_an für dieses Kind (0 aus, 1 alle, 2 nur Testkinder)'$vsx$;
    execute $vsx$create or replace function schule.aufgabe_verstehen(a schule.aufgabe)
 returns boolean language sql immutable set search_path to ''
as $function$
  select (coalesce((a.typ collate "C") in ('begruenden', 'fehler', 'darstellung', 'parameter', 'umkehr', 'rueckwaerts', 'transfer'), false)
       or coalesce((a.form collate "C") in ('fehler_detektiv', 'verfahren_waehlen', 'zwei_wege', 'bruecke', 'umkehren', 'viele_antworten'), false))
     and a.form is distinct from 'lueckenweg';
$function$$vsx$;
    execute $vsx$revoke all on function schule.aufgabe_verstehen(schule.aufgabe) from public$vsx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $vsx$revoke all on function schule.aufgabe_verstehen(schule.aufgabe) from anon$vsx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $vsx$revoke all on function schule.aufgabe_verstehen(schule.aufgabe) from authenticated$vsx$; end if;
    execute $vsx$comment on function schule.aufgabe_verstehen(schule.aufgabe) is 'VTEST-S: Verstehens-Aufgabe (Klasse V aus inhalte/plan/neuer-stil/didaktik.md Abschnitt 2 = tools/vtest_pruefen.py); Lückenweg nie; ohne typ/form = Rechnen'$vsx$;
    execute $vsx$create or replace function schule.karte_verstehen_noetig(p_einheit bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.aufgabe a
   where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben and schule.aufgabe_zaehlt(a) and schule.aufgabe_verstehen(a));
$function$$vsx$;
    execute $vsx$revoke all on function schule.karte_verstehen_noetig(bigint, text) from public$vsx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $vsx$revoke all on function schule.karte_verstehen_noetig(bigint, text) from anon$vsx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $vsx$revoke all on function schule.karte_verstehen_noetig(bigint, text) from authenticated$vsx$; end if;
    execute $vsx$comment on function schule.karte_verstehen_noetig(bigint, text) is 'VTEST-S: die Lernkarte hat eine freigegebene, zählende Verstehens-Übung'$vsx$;
    execute $vsx$create or replace function schule.karte_verstehen_pflicht(k schule.karte_stand, p_l bigint, p_einheit bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  select schule.verstehen_an(p_l, 'verstehen_landung_an')
     and k.sitzt_am is null and not coalesce(k.sitzt, false) and schule.karte_verstehen_noetig(p_einheit, p_lz);
$function$$vsx$;
    execute $vsx$revoke all on function schule.karte_verstehen_pflicht(schule.karte_stand, bigint, bigint, text) from public$vsx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $vsx$revoke all on function schule.karte_verstehen_pflicht(schule.karte_stand, bigint, bigint, text) from anon$vsx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $vsx$revoke all on function schule.karte_verstehen_pflicht(schule.karte_stand, bigint, bigint, text) from authenticated$vsx$; end if;
    execute $vsx$comment on function schule.karte_verstehen_pflicht(schule.karte_stand, bigint, bigint, text) is 'VTEST-S: Verstehens-Aufgabe zum Landen nötig – nur bei Schalter verstehen_landung_an, nur nie gelandete Karten, nur mit freigegebener zählender Verstehens-Übung'$vsx$;
    execute $vsx$create or replace function schule.karte_verstehen_ok(k schule.karte_stand)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from jsonb_object_keys(coalesce(k.gezaehlt, '{}'::jsonb)) x join schule.aufgabe a on a.id = x::bigint
                  where schule.aufgabe_verstehen(a) and schule.aufgabe_zaehlt(a));
$function$$vsx$;
    execute $vsx$revoke all on function schule.karte_verstehen_ok(schule.karte_stand) from public$vsx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $vsx$revoke all on function schule.karte_verstehen_ok(schule.karte_stand) from anon$vsx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $vsx$revoke all on function schule.karte_verstehen_ok(schule.karte_stand) from authenticated$vsx$; end if;
    execute $vsx$comment on function schule.karte_verstehen_ok(schule.karte_stand) is 'VTEST-S: unter den gezählten Aufgaben (eigene Lösung) der Karte ist eine Verstehens-Aufgabe'$vsx$;
    execute $vsx$create or replace function schule.verstehen_korrektur_art(p_l bigint, p_e bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  with s as (select t.id, t.aufgaben from schule.testsitzung t
              where t.lernender_id = p_l and t.einheit_id = p_e and t.status = 'abgeschlossen'
                and exists (select 1 from schule.aufgabe a where a.id = any(t.aufgaben) and a.variante_gruppe = p_lz)
              order by t.abgeschlossen_am desc nulls last, t.id desc limit 1)
  select case when bool_or(schule.aufgabe_verstehen(a)) then true when count(*) > 0 then false end
    from s join schule.aufgabe a on a.id = any(s.aufgaben) and a.variante_gruppe = p_lz
   where not exists (select 1 from schule.versuch v where v.testsitzung_id = s.id and v.aufgabe_id = a.id and v.richtig);
$function$$vsx$;
    execute $vsx$revoke all on function schule.verstehen_korrektur_art(bigint, bigint, text) from public$vsx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $vsx$revoke all on function schule.verstehen_korrektur_art(bigint, bigint, text) from anon$vsx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $vsx$revoke all on function schule.verstehen_korrektur_art(bigint, bigint, text) from authenticated$vsx$; end if;
    execute $vsx$comment on function schule.verstehen_korrektur_art(bigint, bigint, text) is 'VTEST-S: Art der falschen (oder unbeantworteten) Aufgabe(n) dieser Etappe in der letzten abgeschlossenen Testsitzung: true Verstehen (auch wenn beide Arten falsch), false Rechnen, null unbekannt'$vsx$;
    execute $vsx$create or replace function schule.test_starten_intern(p_lernender bigint, p_daten jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_einheit bigint := (p_daten->>'einheit_id')::bigint; v_art text := coalesce(p_daten->>'art','blocktest');
  e schule.einheit; t schule.testsitzung; v_ids bigint[] := '{}'; v_leer text[] := '{}'; v_nf jsonb := '[]'; r record; v_aid bigint; v_runde smallint; v_ns jsonb; v_sel bigint[]; v_je int; /* NT-S */ v_vt boolean; v_ev boolean; v_g boolean; /* VTEST-S */
begin
  if v_art not in ('blocktest','korrektur','nachtest') then raise exception 'Unbekannte Testart' using errcode = 'P0001'; end if;
  select * into e from schule.einheit where id = v_einheit;
  if e.id is null then raise exception 'Einheit nicht gefunden' using errcode = 'P0001'; end if;
  perform schule.lernziele_anlegen(p_lernender, v_einheit);
  perform schule.offene_entscheiden(p_lernender); -- I-3/H2: offene erste Anläufe über 30 Minuten entscheiden
  perform pg_advisory_xact_lock(hashtext('schule_test'), p_lernender::int);
  v_vt := schule.verstehen_an(p_lernender, 'verstehen_test_an'); -- VTEST-S: Schalter verstehen_test_an (0 aus, 1 alle, 2 nur Testkind); aus = alles wie bisher

  select * into t from schule.testsitzung where lernender_id = p_lernender and einheit_id = v_einheit and status = 'laeuft' order by id desc limit 1;
  if t.id is null and v_art in ('blocktest', 'nachtest') and schule.flug_ohne_test(p_lernender, v_einheit) then -- LB-3
    return jsonb_build_object('ok', false, 'grund', 'nichts_zu_testen', 'gesetzt', true, 'vorrat_erschoepft', '[]'::jsonb, 'noch_nicht_faellig', '[]'::jsonb);
  end if;
  if t.id is null then
    if v_art = 'blocktest' then
      if exists (select 1 from schule.testsitzung where lernender_id = p_lernender and einheit_id = v_einheit and art = 'blocktest' and status = 'abgeschlossen') then
        -- W177 Nachtragstest: nach dem Flugtest neu hinzugekommene Pflicht-Etappen (Status 'offen') nachträglich testen
        if not exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = v_einheit and s.pflicht and s.status = 'offen') then
          raise exception 'Der Blocktest ist schon abgeschlossen. Weiter mit Korrektur oder Nachtest.' using errcode = 'P0001';
        end if;
        for r in select s.lernziel from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = v_einheit and s.pflicht and s.status = 'offen' order by s.lernziel loop
          if v_vt then -- VTEST-S (a): Verstehens-Etappe = hat eine freigegebene Verstehens-Testaufgabe
            v_ev := exists (select 1 from schule.aufgabe a where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool = 'test' and a.freigegeben
                              and schule.aufgabe_verstehen(a));
            select a.id into v_aid from schule.aufgabe a
              where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool in ('test', 'korrektur') and a.freigegeben
                and not exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id)
                and not exists (select 1 from schule.testsitzung x where x.lernender_id = p_lernender and a.id = any(x.aufgaben))
              order by (v_ev and schule.aufgabe_verstehen(a)) desc, (a.pool = 'test') desc, a.reihenfolge, a.id limit 1;
          else
          select a.id into v_aid from schule.aufgabe a
            where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool in ('test', 'korrektur') and a.freigegeben
              and not exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id)
              and not exists (select 1 from schule.testsitzung x where x.lernender_id = p_lernender and a.id = any(x.aufgaben))
            order by (a.pool = 'test') desc, a.reihenfolge limit 1;
          end if; -- VTEST-S (a) Nachtragstest
          if v_aid is null then v_leer := v_leer || r.lernziel; else v_ids := v_ids || v_aid; end if;
          v_aid := null;
        end loop;
        if cardinality(v_leer) > 0 then
          return jsonb_build_object('ok', false, 'grund', 'vorrat_erschoepft', 'vorrat_erschoepft', to_jsonb(v_leer), 'noch_nicht_faellig', '[]'::jsonb);
        end if;
      else
        if v_vt then -- VTEST-S (a): Verstehens-Etappe -> nur ihre erste Verstehens-Testaufgabe; sonst alle Test-Aufgaben der Etappe wie bisher
          select coalesce(array_agg(q.id order by q.nr, q.reihenfolge, q.id), '{}') into v_ids from (
            select a.id, a.reihenfolge, coalesce(et.nr, 2147483647) nr, schule.aufgabe_verstehen(a) ist_v,
                   bool_or(schule.aufgabe_verstehen(a)) over (partition by a.variante_gruppe) ev,
                   row_number() over (partition by a.variante_gruppe, schule.aufgabe_verstehen(a) order by a.reihenfolge, a.id) rn
              from schule.aufgabe a
              left join (select o.x->>'lernziel' lz, min(o.nr) nr from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality o(x, nr) group by 1) et
                on et.lz = a.variante_gruppe
             where a.einheit_id = v_einheit and a.pool = 'test' and a.freigegeben) q
           where not q.ev or (q.ist_v and q.rn = 1);
        else
        select coalesce(array_agg(a.id order by a.reihenfolge), '{}') into v_ids from schule.aufgabe a where a.einheit_id = v_einheit and a.pool = 'test' and a.freigegeben;
        end if; -- VTEST-S (a) Flugtest
      end if;
    elsif v_art = 'nachtest' then
      v_ns := schule.nachtest_stand(p_lernender, v_einheit);
      if not (v_ns->>'faellig')::boolean then
        return jsonb_build_object('ok', false, 'grund', case v_ns->>'grund' when 'noch_nicht_faellig' then 'noch_nicht_faellig' when 'erst_korrektur' then 'erst_korrektur' else 'nichts_zu_testen' end,
          'nachtest', v_ns, 'vorrat_erschoepft', '[]'::jsonb,
          'noch_nicht_faellig', case when v_ns->>'grund' = 'noch_nicht_faellig' then jsonb_build_array(jsonb_build_object('lernziel', 'einheit',
             'lerntage_seit', v_ns->'lerntage_seit', 'lerntage_noetig', v_ns->'lerntage_noetig')) else '[]'::jsonb end);
      end if;
      v_runde := (v_ns->>'runde')::smallint;
      v_je := schule.nachtest_je_etappe((select count(*)::int from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = v_einheit and s.pflicht)); -- NT-S
      for r in select s.lernziel from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = v_einheit and s.pflicht order by s.lernziel loop
        v_sel := schule.nachtest_auswahl(p_lernender, v_einheit, r.lernziel, v_je); -- NT-S: Menge je Etappe nach der Regel
        if cardinality(v_sel) <> v_je then v_leer := v_leer || r.lernziel; else v_ids := v_ids || v_sel; end if; -- NT-S 2: genau v_je, sonst kein Start
        v_aid := null;
      end loop;
      if cardinality(v_leer) > 0 then
        return jsonb_build_object('ok', false, 'grund', 'vorrat_erschoepft', 'vorrat_erschoepft', to_jsonb(v_leer), 'noch_nicht_faellig', '[]'::jsonb, 'nachtest', v_ns);
      end if;
    else
      for r in select s.lernziel from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = v_einheit and s.status = 'fehler' order by s.lernziel loop
        if v_vt then -- VTEST-S (b): 1. ungesehen und gleiche Art, 2. nur bei Verstehen: schon gestellte Verstehens-Korrektur (am längsten her), 3. ungesehen andere Art
          v_g := schule.verstehen_korrektur_art(p_lernender, v_einheit, r.lernziel);
          select q.id into v_aid from (
            select a.id, a.reihenfolge, schule.aufgabe_verstehen(a) ist_v,
                   not exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id)
                       and not exists (select 1 from schule.testsitzung x where x.lernender_id = p_lernender and a.id = any(x.aufgaben)) neu,
                   greatest((select max(v.am) from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id),
                            (select max(x.gestartet_am) from schule.testsitzung x where x.lernender_id = p_lernender and a.id = any(x.aufgaben))) zuletzt
              from schule.aufgabe a
             where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool = 'korrektur' and a.freigegeben) q
           where q.neu or (v_g and q.ist_v)
           order by case when q.neu and (v_g is null or q.ist_v = v_g) then 0 when not q.neu then 1 else 2 end, q.zuletzt nulls first, q.reihenfolge, q.id limit 1;
        else
        select a.id into v_aid from schule.aufgabe a
          where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool = 'korrektur' and a.freigegeben
            and not exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id)
            and not exists (select 1 from schule.testsitzung x where x.lernender_id = p_lernender and a.id = any(x.aufgaben))
          order by a.reihenfolge limit 1;
        end if; -- VTEST-S (b) Korrektur
        if v_aid is null then v_leer := v_leer || r.lernziel; else v_ids := v_ids || v_aid; end if;
        v_aid := null;
      end loop;
    end if;
    if cardinality(v_ids) = 0 then
      return jsonb_build_object('ok', false, 'grund', case when cardinality(v_leer) > 0 then 'vorrat_erschoepft' else 'nichts_zu_testen' end,
        'vorrat_erschoepft', to_jsonb(v_leer), 'noch_nicht_faellig', v_nf);
    end if;
    insert into schule.testsitzung(lernender_id, art, block_id, thema_id, einheit_id, nachtest_runde, aufgaben, status, punkte_max, regel_version, gestartet_am)
    values (p_lernender, v_art, e.block_id, e.thema_id, v_einheit, v_runde, v_ids, 'laeuft', cardinality(v_ids),
            coalesce((select (wert #>> '{}')::int from schule.regel where schluessel = 'regel_version'), 1), now())
    returning * into t;
  end if;

  return jsonb_build_object('ok', true, 'sitzung_id', t.id, 'art', t.art, 'nachtest_runde', t.nachtest_runde, 'vorrat_erschoepft', to_jsonb(v_leer), 'noch_nicht_faellig', v_nf,
    'aufgaben', (select coalesce(jsonb_agg(schule.aufgabe_anzeige(a, false) order by array_position(t.aufgaben, a.id)), '[]') from schule.aufgabe a where a.id = any(t.aufgaben)),
    'beantwortet', (select coalesce(jsonb_agg(v.aufgabe_id), '[]') from schule.versuch v where v.testsitzung_id = t.id));
end $function$$vsx$;
    execute $vsx$create or replace function schule.etappen_stand(p_lernender bigint, p_einheit bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  -- TEMPO-S1: gleiches Ergebnis wie die Fassung nach FT-S; je Einheit einmal: flug_nachtest, gesamt/geloest (gruppiert); je Etappe einmal: karte_ziel
  select coalesce(jsonb_object_agg(z.lz, jsonb_build_object('geloest', z.geloest, 'gesamt', z.gesamt,
           'serie', coalesce(k.serie, 0), 'ziel', z.ziel, 'sitzt', coalesce(k.sitzt, false), 'schwer_ok', coalesce(k.schwer_ok, false), 'anwenden_noetig', schule.karte_anwenden_pflicht(k, p_einheit, z.lz), 'anwenden_ok', coalesce(schule.karte_anwenden_ok(k), false),
           'bearbeitungen', schule.karte_bearbeitungen(p_lernender, p_einheit, z.lz), 'schwer_noetig', schule.karte_schwer_noetig(p_einheit, z.lz),
           'faellig', coalesce(schule.karte_faellig(k), false), 'wdh_stufe', coalesce(k.wdh_stufe, 0),
           'eigene_loesungen', coalesce(k.eigene_loesungen, 0), 'folge', coalesce(k.folge, 0), 'folge_ziel', least(3, z.ziel),
           'typen_anzahl', coalesce(array_length(k.typen, 1), 0), 'typen_noetig', schule.karte_typen_noetig(p_einheit, z.lz),
           'fehler_folge', coalesce(k.fehler_folge, 0), 'stufe_senkung', coalesce(k.stufe_senkung, 0), 'sicher', coalesce(schule.karte_sicher(k), false), 'misch_ok', k.misch_ok_am is not null and k.misch_ok_am >= coalesce(k.sitzt_am, k.misch_ok_am), 'flug_nachtest', fn.v,
           'fertig', schule.etappe_fertig(k, s.status), 'test_nachgewiesen', coalesce(s.status in ('nachgewiesen','korrigiert','gesichert'), false), 'wieder_offen', not coalesce(k.sitzt, false) and k.sitzt_am is not null, 'gezaehlt', coalesce((select jsonb_agg(x::bigint) from jsonb_object_keys(k.gezaehlt) x), '[]'::jsonb))
           || case when vs.an then jsonb_build_object('verstehen_noetig', schule.karte_verstehen_pflicht(k, p_lernender, p_einheit, z.lz), 'verstehen_ok', coalesce(schule.karte_verstehen_ok(k), false)) else '{}'::jsonb end /* VTEST-S */), '{}'::jsonb)
  from (select y.lz, coalesce(g.gesamt, 0) gesamt, coalesce(v.geloest, 0) geloest, schule.karte_ziel(p_einheit, y.lz) ziel
          from (select e->>'lernziel' lz, o.nr
                  from schule.einheit x, jsonb_array_elements(coalesce(x.inhalt->'etappen', '[]'::jsonb)) with ordinality o(e, nr) where x.id = p_einheit) y
          left join (select a.variante_gruppe lz, count(*) gesamt from schule.aufgabe a
                      where a.einheit_id = p_einheit and a.pool = 'uebung' and a.freigegeben group by a.variante_gruppe) g on g.lz = y.lz
          left join (select a.variante_gruppe lz, count(distinct v.aufgabe_id) geloest from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                      where v.lernender_id = p_lernender and v.richtig and v.testsitzung_id is null and a.einheit_id = p_einheit and a.pool = 'uebung'
                      group by a.variante_gruppe) v on v.lz = y.lz
         order by y.nr) z
  cross join (select schule.flug_nachtest(p_lernender, p_einheit) v offset 0) fn
  cross join (select schule.verstehen_an(p_lernender, 'verstehen_landung_an') an offset 0) vs -- VTEST-S: Schalter einmal je Aufruf
  left join schule.lernziel_stand s on s.lernender_id = p_lernender and s.einheit_id = p_einheit and s.lernziel = z.lz
  left join schule.karte_stand k on k.lernender_id = p_lernender and k.einheit_id = p_einheit and k.lernziel = z.lz;
$function$$vsx$;
    execute $vsx$create or replace function schule.karte_landet(k schule.karte_stand)
 returns boolean language sql stable set search_path to ''
as $function$
  select coalesce(k.eigene_loesungen, 0) >= schule.karte_ziel(k.einheit_id, k.lernziel)
     and coalesce(array_length(k.typen, 1), 0) >= schule.karte_typen_noetig(k.einheit_id, k.lernziel)
     and (coalesce(k.schwer_ok, false) or not schule.karte_schwer_noetig(k.einheit_id, k.lernziel))
     and coalesce(k.folge, 0) >= least(3, schule.karte_ziel(k.einheit_id, k.lernziel))
     and (schule.karte_anwenden_ok(k) or not schule.karte_anwenden_pflicht(k, k.einheit_id, k.lernziel))
     and (schule.karte_verstehen_ok(k) or not schule.karte_verstehen_pflicht(k, k.lernender_id, k.einheit_id, k.lernziel)) /* VTEST-S */; -- FT-S Regel 6
$function$$vsx$;
  end if;
  -- 4. Nachher: Zustand, Eigenschaften, Besitzer/Rechte
  for r in select s.f, s.ei from vs_soll s order by s.f collate "C" loop
    select p.prosrc, concat_ws('|', pg_get_function_arguments(p.oid), pg_get_function_result(p.oid), l.lanname, p.provolatile, p.prosecdef, p.proisstrict, p.proretset,
                     p.proparallel, p.procost, p.prorows, p.proleakproof, coalesce(p.proconfig::text, ''))
      into d, v_kurz from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = to_regprocedure(r.f);
    if v_kurz is distinct from r.ei then fehler := fehler || format('%s: Eigenschaften nachher %s', r.f, v_kurz); end if;
    if md5(d) is distinct from coalesce((select m_neu from vs_geaendert where f = r.f), (select m from vs_hilfe where f = r.f)) then
      fehler := fehler || format('%s: Funktionstext nachher md5 %s', r.f, md5(d)); end if;
    if r.f in (select f from vs_geaendert) and acl_vor->>r.f is distinct from (select concat_ws('|', p.proowner::regrole::text, coalesce(p.proacl::text, '')) from pg_proc p where p.oid = to_regprocedure(r.f)) then
      fehler := fehler || format('%s: Besitzer/Rechte geändert', r.f); end if;
    if r.f in (select f from vs_hilfe) and exists (select 1 from pg_proc p, aclexplode(coalesce(p.proacl, acldefault('f', p.proowner))) a
                                                    where p.oid = to_regprocedure(r.f) and a.grantee = 0) then
      fehler := fehler || format('%s: für alle (public) ausführbar', r.f); end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception 'VTEST-S ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;

  -- 5. Vergleich mit Schalter AUS (je eine Anweisung = ein Schnappschuss)
  t0 := clock_timestamp();
  select count(*), count(*) filter (where pg_temp.vs_es_alt(l.id, e.id) is distinct from schule.etappen_stand(l.id, e.id)), count(distinct l.id), count(distinct e.id)
    into n_e, n_abw_es, n_kinder, n_einh from schule.lernender l cross join schule.einheit e;
  ms_aus := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
  select count(*), count(*) filter (where pg_temp.vs_kl_alt(k) is distinct from schule.karte_landet(k)),
         count(*) filter (where pg_temp.vs_kl_alt(jsonb_populate_record(k, '{"sitzt": false, "sitzt_am": null}')) is distinct from schule.karte_landet(jsonb_populate_record(k, '{"sitzt": false, "sitzt_am": null}')))
    into n_k, n_abw_kl, n_abw_kl_offen from schule.karte_stand k;
  if n_abw_es > 0 or n_abw_kl > 0 or n_abw_kl_offen > 0 then
    raise exception 'VTEST-S ABBRUCH, alles zurückgerollt: mit Schalter AUS weicht ab – etappen_stand % von % (z. B. %), karte_landet % von %, karte_landet als nie gelandet % von %',
      n_abw_es, n_e, (select string_agg(format('Kind %s Einheit %s', q.l, q.e), '; ') from (select l.id l, e.id e from schule.lernender l cross join schule.einheit e
        where pg_temp.vs_es_alt(l.id, e.id) is distinct from schule.etappen_stand(l.id, e.id) order by 1, 2 limit 5) q),
      n_abw_kl, n_k, n_abw_kl_offen, n_k; end if;

  -- 6. Schalter AN (nur in dieser Transaktion): nur Zahlen
  update schule.regel set wert = '1'::jsonb where schluessel in ('verstehen_test_an', 'verstehen_landung_an');
  t0 := clock_timestamp();
  with s as (select l.id l, j.key lz, j.value v from schule.lernender l cross join schule.einheit e cross join lateral jsonb_each(schule.etappen_stand(l.id, e.id)) j)
  select jsonb_build_object(
      'etappen_mit_feldern', count(*) filter (where s.v ? 'verstehen_noetig' and s.v ? 'verstehen_ok'),
      'etappen_ohne_felder', count(*) filter (where not (s.v ? 'verstehen_noetig' and s.v ? 'verstehen_ok')),
      'etappen_verstehen_fehlt_je_kind', coalesce((select jsonb_object_agg(q.l::text, q.n) from (select s2.l, count(*) n from s s2
         where (s2.v->>'verstehen_noetig')::boolean and not (s2.v->>'verstehen_ok')::boolean group by s2.l) q), '{}'::jsonb)) into zz from s;
  ms_an := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
  zz := zz || (select jsonb_build_object(
      'karten_nie_gelandet', count(*) filter (where k.sitzt_am is null and not k.sitzt),
      'davon_mit_verstehens_uebung', count(*) filter (where k.sitzt_am is null and not k.sitzt and schule.karte_verstehen_noetig(k.einheit_id, k.lernziel)),
      'davon_verstehen_schon_ok', count(*) filter (where k.sitzt_am is null and not k.sitzt and schule.karte_verstehen_noetig(k.einheit_id, k.lernziel) and schule.karte_verstehen_ok(k)),
      'landebereit_bis_auf_verstehen', count(*) filter (where k.sitzt_am is null and not k.sitzt and pg_temp.vs_kl_alt(k) and not schule.karte_landet(k)),
      'gelandete_unveraendert', count(*) filter (where (k.sitzt or k.sitzt_am is not null) and pg_temp.vs_kl_alt(k) is not distinct from schule.karte_landet(k)),
      'gelandete_geaendert', count(*) filter (where (k.sitzt or k.sitzt_am is not null) and pg_temp.vs_kl_alt(k) is distinct from schule.karte_landet(k)))
    from schule.karte_stand k);
  zz := zz || (select jsonb_build_object(
      'lernkarten_uebung', count(*), 'lernkarten_ohne_verstehens_uebung', count(*) filter (where not q.v))
    from (select a.einheit_id, a.variante_gruppe, bool_or(schule.aufgabe_zaehlt(a) and schule.aufgabe_verstehen(a)) v from schule.aufgabe a
           where a.pool = 'uebung' and a.freigegeben group by 1, 2) q);
  zz := zz || (select jsonb_build_object(
      'test_etappen', count(*), 'test_etappen_verstehen', count(*) filter (where q.nv > 0), 'test_etappen_verstehen_und_rechnen', count(*) filter (where q.nv > 0 and q.nr > 0),
      'flugtest_aufgaben_bisher', coalesce(sum(q.nv + q.nr), 0), 'flugtest_aufgaben_neu', coalesce(sum(case when q.nv > 0 then 1 else q.nr end), 0))
    from (select a.einheit_id, a.variante_gruppe, count(*) filter (where schule.aufgabe_verstehen(a)) nv, count(*) filter (where not schule.aufgabe_verstehen(a)) nr
            from schule.aufgabe a where a.pool = 'test' and a.freigegeben group by 1, 2) q);
  zz := zz || (with f as (select s.lernender_id l, s.einheit_id e, s.lernziel lz, schule.verstehen_korrektur_art(s.lernender_id, s.einheit_id, s.lernziel) g
                            from schule.lernziel_stand s where s.status = 'fehler'),
    v as (select f.*, (select count(*) filter (where schule.aufgabe_verstehen(a)) from schule.aufgabe a where a.einheit_id = f.e and a.variante_gruppe = f.lz and a.pool = 'korrektur' and a.freigegeben
                         and not exists (select 1 from schule.versuch x where x.lernender_id = f.l and x.aufgabe_id = a.id)
                         and not exists (select 1 from schule.testsitzung x where x.lernender_id = f.l and a.id = any(x.aufgaben))) neu_v,
                      (select count(*) filter (where not schule.aufgabe_verstehen(a)) from schule.aufgabe a where a.einheit_id = f.e and a.variante_gruppe = f.lz and a.pool = 'korrektur' and a.freigegeben
                         and not exists (select 1 from schule.versuch x where x.lernender_id = f.l and x.aufgabe_id = a.id)
                         and not exists (select 1 from schule.testsitzung x where x.lernender_id = f.l and a.id = any(x.aufgaben))) neu_r,
                      (select count(*) filter (where schule.aufgabe_verstehen(a)) from schule.aufgabe a where a.einheit_id = f.e and a.variante_gruppe = f.lz and a.pool = 'korrektur' and a.freigegeben) alle_v
            from f)
    select jsonb_build_object('korrektur_offen', count(*), 'korrektur_art_verstehen', count(*) filter (where g), 'korrektur_art_rechnen', count(*) filter (where not g),
      'korrektur_art_unbekannt', count(*) filter (where g is null),
      'verstehen_neue_da', count(*) filter (where g and neu_v > 0), 'verstehen_wiederholung', count(*) filter (where g and neu_v = 0 and alle_v > 0),
      'verstehen_rueckfall_rechnen', count(*) filter (where g and alle_v = 0 and neu_r > 0), 'rechnen_neue_da', count(*) filter (where not g and neu_r > 0),
      'rechnen_rueckfall_verstehen', count(*) filter (where not g and neu_r = 0 and neu_v > 0)) from v);
  update schule.regel set wert = v_t_vor where schluessel = 'verstehen_test_an';
  update schule.regel set wert = v_l_vor where schluessel = 'verstehen_landung_an';
  if (select x.wert from schule.regel x where x.schluessel = 'verstehen_test_an') is distinct from v_t_vor
     or (select x.wert from schule.regel x where x.schluessel = 'verstehen_landung_an') is distinct from v_l_vor then raise exception 'VTEST-S ABBRUCH: Schalter nicht zurückgesetzt'; end if;

  v_kurz := jsonb_build_object('zustand', case when n_alt > 0 then 'alt -> neu' else 'neu -> neu (schon eingespielt, nichts geändert)' end,
    'kinder', n_kinder, 'einheiten', n_einh, 'etappen_stand_verglichen', n_e, 'karten_verglichen', n_k, 'abweichungen_aus', n_abw_es + n_abw_kl + n_abw_kl_offen,
    'schalter', jsonb_build_object('verstehen_test_an', v_t_vor, 'verstehen_landung_an', v_l_vor),
    'flugtest_aufgaben_bisher_neu', jsonb_build_array(zz->'flugtest_aufgaben_bisher', zz->'flugtest_aufgaben_neu'), 'test_etappen_verstehen', zz->'test_etappen_verstehen',
    'korrektur_offen_v_r_unbekannt', jsonb_build_array(zz->'korrektur_offen', zz->'korrektur_art_verstehen', zz->'korrektur_art_rechnen', zz->'korrektur_art_unbekannt'),
    'landebereit_bis_auf_verstehen', zz->'landebereit_bis_auf_verstehen', 'lernkarten_ohne_verstehens_uebung', zz->'lernkarten_ohne_verstehens_uebung',
    'ms_aus_an', jsonb_build_array(ms_aus, ms_an))::text;
  v_bericht := zz || jsonb_build_object('zustand_vorher', st, 'md5_neu', (select jsonb_object_agg(f, m_neu) from vs_geaendert), 'fehler', 0);
  if (zz->>'etappen_ohne_felder')::int > 0 or (zz->>'gelandete_geaendert')::int > 0 then
    raise exception 'VTEST-S ABBRUCH, alles zurückgerollt: mit Schalter AN fehlen Felder (%) oder eine gelandete Karte ändert ihre Landeregel (%)', zz->>'etappen_ohne_felder', zz->>'gelandete_geaendert'; end if;
  drop function pg_temp.vs_es_alt(bigint, bigint);
  drop function pg_temp.vs_kl_alt(schule.karte_stand);
  raise notice 'VTEST-S eingespielt KURZ % VOLL %', v_kurz::text, v_bericht::text;
end $vs$;
