"""Einspiel-Paket für WW-S2 („Was wackelt“, Teil Datenbank, schlanke Fassung ohne Nachüben) – prüft sich selbst. Muster: tools/tests/regelbezug_einspielen.py.

EIN SQL für EINEN Aufruf (eine Transaktion). Bei der kleinsten Abweichung: Ausnahme -> alles zurück.
  0. Vorher: Fingerabdruck aller bestehenden Funktionen (schule, api), Trigger (auch interne) und Spalten im Schema schule sowie aller Daten
     im Schema schule.
  1. Migration ausführen, dann vollständig noch einmal (zweiter Lauf ändert nichts: Definitionen, Indizes, Spalten). Danach: der Fingerabdruck
     der bestehenden Funktionen/Trigger/Spalten ist unverändert (die Migration legt nur Neues an).
  2. Prüfblock mit dem Testkind (zurückgerollte Untertransaktion): zwei endgültig falsche Antworten -> beide offen in der Analyse, mit Aufgabe, Lösung,
     Lernkarte, Auswertung je Thema und Lerntag; Abhaken -> weg aus „offen“, unter „erledigt“; zweites Abhaken ändert nichts; Rückgängig -> wieder
     offen; fremder Versuch -> übersprungen. Während Analyse, Abhaken und Rückgängig bleiben ALLE Daten im Schema schule außer
     schule.fehler_erledigt bytegleich (Versuche, Karten, Wiederholung, Mischkarten, Lerntage, Sterne …).
  3. Lesevarianten mit echten Lern-Sitzungen (zurückgerollt): Kind -> Analyse und Abhaken „Nur Eltern/Lehrer“ (auch für sich selbst); fremdes Kind
     abgewiesen; Eltern und Lehrer -> Analyse ok, Abhaken und Rückgängig ok; unbekannte Sitzung abgewiesen; Daten außer fehler_erledigt gleich.
  4. Abhaken an einer sitzenden, nicht fälligen Lernkarte: die Kartenzeile ist nach dem Abhaken unverändert, und ein weiterer Fehler wirkt genau
     wie ohne Abhaken (beide Läufe vom selben Ausgangsstand; beobachtete Zustände im Bericht).
  5. Rechte: Tabelle mit RLS ohne Policy, keine Rechte für anon/authenticated; Funktionen nicht für anon/authenticated; beide api-Aktionen prüfen
     ist_leiter; ein unbekannter Schlüssel bekommt nichts.
  6. Ende: neue Tabelle leer, keine neuen Versuche, alle Daten im Schema schule wie vor dem Paket.
Aufruf:  python3 -I tools/tests/wackelt_einspielen.py > ww.sql   |   --probe > ww_probe.sql (rollt am Ende alles zurück)
Nicht ohne den ausdrücklichen Satz des Nutzers ausführen. Vorher: werkstatt_sperre. Nachher: werkstatt_aenderung. Danach lernen-api (Aktionen) ergänzen.

WW-S3 (Folgemigration 20261206_ww_s3_wackelt.sql, setzt auf „WW-S2 eingespielt“ auf):
         python3 -I tools/tests/wackelt_einspielen.py --ww3 > ww3.sql   |   --ww3 --probe > ww3_probe.sql
  Die Ausgabe ohne --ww3 ist unverändert (WW-S2-Pakete bleiben byteidentisch). Inhalt des WW-S3-Pakets: siehe ww3() unten.
"""
import sys
from pathlib import Path

MIG = Path(__file__).resolve().parent.parent.parent / 'supabase/migrations/20261205_ww_s_wackelt.sql'
MIG3 = Path(__file__).resolve().parent.parent.parent / 'supabase/migrations/20261206_ww_s3_wackelt.sql'
# Funktionen, die WW-S3 anlegt oder ersetzt (alles andere in schule/api muss bytegleich bleiben – auch die übrigen WW-S2-Funktionen)
NEU3 = ['schule.wackelt_analyse(bigint, integer, boolean)', 'schule.fehler_abhaken(bigint, jsonb, boolean, text)',
        'schule.fehler_zurueckholen(bigint, jsonb, text)', 'api.schule_fehler_abhaken(text, jsonb)']
NEU = ['schule.ww_fehlerart(schule.versuch, schule.aufgabe)', 'schule.ww_von(text)', 'schule.wackelt_analyse(bigint, integer, boolean)',
       'schule.ww_versuche(bigint, jsonb)', 'schule.fehler_abhaken(bigint, jsonb, boolean, text)',
       'api.schule_wackelt_analyse(text, jsonb)', 'api.schule_fehler_abhaken(text, jsonb)']
API = ['api.schule_wackelt_analyse(text, jsonb)', 'api.schule_fehler_abhaken(text, jsonb)']


def F(msg):
    return f'fehler := fehler || ({msg})::text;'


def main():
    if '--ww3' in sys.argv[1:]:
        print(ww3('--probe' in sys.argv[1:]))
        return
    probe = '--probe' in sys.argv[1:]
    mig = MIG.read_text(encoding='utf-8')
    for m in ('$wwmig$', '$p$', '$f$'):
        assert m not in mig
    k = '(select id from schule.lernender where ist_test order by id limit 1)'
    neu = 'array[' + ', '.join(f"'{f}'" for f in NEU) + ']'
    defs = f"(select md5(string_agg(coalesce(pg_get_functiondef(to_regprocedure(f)), 'fehlt'), '#' order by f)) from unnest({neu}) f)"
    obj = """(select md5(string_agg(s.x, '#' order by s.x)) from (
       select 'idx:' || indexrelid::regclass::text || pg_get_indexdef(indexrelid) from pg_index where indrelid = 'schule.fehler_erledigt'::regclass
       union all select 'col:' || attrelid::regclass::text || attname || format_type(atttypid, atttypmod) from pg_attribute where attrelid = 'schule.fehler_erledigt'::regclass and attnum > 0
       union all select 'rls:' || relrowsecurity::text || coalesce(obj_description(oid, 'pg_class'), '') from pg_class where oid = 'schule.fehler_erledigt'::regclass) s(x))"""
    ende = ("raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): %', bericht::text;" if probe else
            "raise notice 'WW-S eingespielt: %', bericht::text;")
    print(f"""-- WW-S2 Einspiel-Paket (erzeugt von tools/tests/wackelt_einspielen.py{' --probe' if probe else ''}). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);
create temp table ww_mig on commit drop as select $wwmig${mig}$wwmig$::text as sql;
-- Fingerabdruck des Bestehenden: Funktionen in schule/api (ohne die neuen), alle Trigger (auch interne) an Tabellen in schule, Spalten (ohne fehler_erledigt)
create function pg_temp.ww_schema() returns text language sql stable as $f$
  select md5(string_agg(x, '#' order by x)) from (
    select 'f:' || p.oid::regprocedure::text || ':' || pg_get_functiondef(p.oid) x from pg_proc p
     where p.pronamespace in ('schule'::regnamespace, 'api'::regnamespace) and p.prokind in ('f', 'p')
       and p.oid not in (select o from (select to_regprocedure(f) o from unnest({neu}) f) q where o is not null)
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
create temp table ww_def on commit drop as select 1 lauf, {defs} d, {obj} o, pg_temp.ww_schema() s;
do $p$ begin execute (select sql from ww_mig); end $p$;
insert into ww_def select 2, {defs}, {obj}, pg_temp.ww_schema();
create function pg_temp.ww_ant(p_k bigint, p_id bigint, p_wert text, p_cid text) returns jsonb language plpgsql as $f$
begin
  return schule.uebung_pruefen_wd(p_k, jsonb_build_object('aufgabe_id', p_id, 'client_id', p_cid, 'antwort', jsonb_build_object('wert', p_wert)));
end $f$;
create function pg_temp.ww_ids(r jsonb, p text) returns bigint[] language sql immutable as $f$
  select coalesce(array_agg((e->>'versuch_id')::bigint), '{{}}') from jsonb_array_elements(coalesce(r->p, '[]'::jsonb)) e $f$;
do $p$
declare
  fehler text[] := '{{}}'; k bigint := {k}; v_e bigint; v_lz text; a1 schule.aufgabe; a2 schule.aufgabe; v1 bigint; v2 bigint; r jsonb; x text;
  bericht jsonb := '{{}}'; t0 timestamptz; ms numeric; v_f bigint; v_gross bigint; s_kind text; s_fremd text; s_eltern text; s_lehrer text; v_id bigint;
  kn jsonb; ko jsonb; kz jsonb; h0 text; v0 bigint;
begin
  if (select count(distinct ww_def.d) from ww_def) <> 1 or (select count(distinct ww_def.o) from ww_def) <> 1 then {F("'zweiter Lauf hat etwas geändert'")} end if;
  if exists (select 1 from ww_def where ww_def.s is distinct from (select ww_stand.s from ww_stand)) then
    {F("'Migration ändert bestehende Funktionen, Trigger oder Spalten'")} end if;
  -- Rechte
  if not (select relrowsecurity from pg_class where oid = 'schule.fehler_erledigt'::regclass) then {F("'fehler_erledigt: RLS aus'")} end if;
  if exists (select 1 from pg_policy where polrelid = 'schule.fehler_erledigt'::regclass) then {F("'fehler_erledigt: hat eine Policy'")} end if;
  if has_table_privilege('anon', 'schule.fehler_erledigt', 'select') or has_table_privilege('authenticated', 'schule.fehler_erledigt', 'select')
     or has_table_privilege('authenticated', 'schule.fehler_erledigt', 'insert') then {F("'fehler_erledigt: App-Rollen haben Rechte'")} end if;
  if exists (select 1 from pg_constraint where contype = 'f' and (conrelid = 'schule.fehler_erledigt'::regclass or confrelid = 'schule.fehler_erledigt'::regclass)) then
    {F("'fehler_erledigt: Fremdschlüssel (legte Trigger an bestehenden Tabellen an)'")} end if;
  for x in select unnest({neu}) loop
    if has_function_privilege('anon', x, 'execute') or has_function_privilege('authenticated', x, 'execute') then {F("x || ': für App-Rollen aufrufbar'")} end if;
  end loop;
  for x in select unnest(array[{', '.join(repr(f) for f in API)}]) loop
    if position('if not schule.ist_leiter(p_schluessel) then raise exception' in pg_get_functiondef(x::regprocedure)) = 0 then {F("x || ': prüft ist_leiter nicht'")} end if;
  end loop;
  if exists (select 1 from pg_proc p where p.pronamespace in ('schule'::regnamespace, 'api'::regnamespace) and p.proname like '%nachueb%') then
    {F("'Nachüben-Funktion vorhanden (gehört nicht zu WW-S2)'")} end if;
  begin
    r := api.schule_wackelt_analyse('ww-unbekannter-schluessel', jsonb_build_object('lernender_id', k));
    {F("'unbekannter Schlüssel bekommt eine Analyse'")}
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
    if not (array[v1, v2] <@ pg_temp.ww_ids(r, 'offen')) then {F("'Analyse: falsche Antworten nicht offen: ' || left(r::text, 300)")} end if;
    if (select e->'aufgabe'->'loesung' is null or e->>'lernziel' is distinct from v_lz or e->>'tag' is null from jsonb_array_elements(r->'offen') e where (e->>'versuch_id')::bigint = v1) then
      {F("'Analyse: Eintrag unvollständig'")} end if;
    if exists (select 1 from jsonb_array_elements(r->'offen') e where e ? 'nachueben') then {F("'Analyse liefert noch nachueben'")} end if;
    if not exists (select 1 from jsonb_array_elements(r->'auswertung'->'themen') t where (t->>'offen')::int >= 2) then {F("'Auswertung je Thema fehlt'")} end if;
    if jsonb_array_length(r->'auswertung'->'lerntage') = 0 then {F("'Lerntage fehlen'")} end if;
    if not (r->'auswertung' ? 'wiederkehrend' and r->'auswertung' ? 'einmal') then {F("'Auswertung: wiederkehrend/einmal fehlt'")} end if;
    bericht := bericht || jsonb_build_object('mit_fehlbild', r->'mit_fehlbild', 'offen_zahl', r->'offen_zahl',
                 'beispiel', (select e - 'aufgabe' - 'antwort' from jsonb_array_elements(r->'offen') e where (e->>'versuch_id')::bigint = v1));
    -- Abhaken, zweimal, Rückgängig, fremde Versuche
    r := schule.fehler_abhaken(k, jsonb_build_array(v1), false, 'probe');
    if (r->>'geaendert')::int <> 1 then {F("'Abhaken: ' || r::text")} end if;
    if (schule.fehler_abhaken(k, jsonb_build_array(v1), false, 'probe')->>'geaendert')::int <> 0 then {F("'zweites Abhaken ändert etwas'")} end if;
    r := schule.wackelt_analyse(k, 14, true);
    if v1 = any(pg_temp.ww_ids(r, 'offen')) or not v1 = any(pg_temp.ww_ids(r, 'erledigt')) then {F("'abgehakte Antwort noch offen oder nicht erledigt'")} end if;
    if (select e->'erledigt'->>'art' from jsonb_array_elements(r->'erledigt') e where (e->>'versuch_id')::bigint = v1) is distinct from 'abgehakt' then {F("'erledigt.art nicht abgehakt'")} end if;
    if pg_temp.ww_bestand() is distinct from h0 then {F("'Analyse/Abhaken verändert Daten außerhalb von fehler_erledigt'")} end if;
    if (schule.fehler_abhaken(k, jsonb_build_array(v1), true, 'probe')->>'geaendert')::int <> 1 then {F("'Rückgängig ändert nichts'")} end if;
    if not v1 = any(pg_temp.ww_ids(schule.wackelt_analyse(k, 14, false), 'offen')) then {F("'nach Rückgängig nicht wieder offen'")} end if;
    r := schule.fehler_abhaken(k, jsonb_build_array(0, coalesce((select min(id) from schule.versuch where lernender_id <> k), 0)), false, 'probe');
    if (r->>'geaendert')::int <> 0 or jsonb_array_length(r->'uebersprungen') = 0 then {F("'fremde Versuche abgehakt: ' || r::text")} end if;
    begin perform schule.fehler_abhaken(k, '[1.5]'::jsonb, false, 'probe'); {F("'Kommazahl als versuch_id angenommen'")}
    exception when others then if position('versuch_ids' in sqlerrm) = 0 then {F("'Kommazahl: falscher Fehler ' || sqlerrm")} end if; end;
    if pg_temp.ww_bestand() is distinct from h0 then {F("'Rückgängig verändert Daten außerhalb von fehler_erledigt'")} end if;
    bericht := bericht || jsonb_build_object('bestand_gleich_beim_abhaken', pg_temp.ww_bestand() = h0);
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then {F("'Prüfblock: ' || sqlerrm")}
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
    begin r := api.schule_wackelt_analyse(s_kind, jsonb_build_object('lernender_id', k)); {F("'Kind liest die Analyse'")}
    exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then {F("'Kind/Analyse: falscher Fehler ' || sqlerrm")} end if; end;
    begin r := api.schule_fehler_abhaken(s_kind, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0))); {F("'Kind hakt ab'")}
    exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then {F("'Kind/Abhaken: falscher Fehler ' || sqlerrm")} end if; end;
    if v_f is not null then
      begin r := api.schule_wackelt_analyse(s_fremd, jsonb_build_object('lernender_id', k)); {F("'fremdes Kind liest die Analyse'")}
      exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then {F("'Fremdkind/Analyse: falscher Fehler ' || sqlerrm")} end if; end;
      begin r := api.schule_fehler_abhaken(s_fremd, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0))); {F("'fremdes Kind hakt ab'")}
      exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then {F("'Fremdkind/Abhaken: falscher Fehler ' || sqlerrm")} end if; end;
    else bericht := bericht || '{{"hinweis_fremdkind": "kein zweites aktives Kind – Fremdkind-Probe übersprungen"}}'::jsonb;
    end if;
    if exists (select 1 from schule.fehler_erledigt) then {F("'Kind-Sitzung hat etwas abgehakt'")} end if;
    r := api.schule_wackelt_analyse(s_eltern, jsonb_build_object('lernender_id', k, 'tage', 0));
    if r->>'ok' is distinct from 'true' then {F("'Eltern lesen die Analyse nicht'")} end if;
    r := api.schule_wackelt_analyse(s_lehrer, jsonb_build_object('lernender_id', k, 'tage', 7));
    if r->>'ok' is distinct from 'true' then {F("'Lehrer lesen die Analyse nicht'")} end if;
    r := api.schule_fehler_abhaken(s_eltern, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0)));
    if (r->>'geaendert')::int <> 1 then {F("'Eltern haken nicht ab: ' || r::text")} end if;
    if (select von from schule.fehler_erledigt where versuch_id = v0 and zurueckgenommen_am is null) is distinct from 'eltern:WW-Probe Eltern' then {F("'von falsch'")} end if;
    r := api.schule_fehler_abhaken(s_lehrer, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0), 'zurueck', true));
    if (r->>'geaendert')::int <> 1 then {F("'Lehrer nehmen das Abhaken nicht zurück: ' || r::text")} end if;
    begin r := api.schule_wackelt_analyse(s_eltern, jsonb_build_object('lernender_id', k, 'tage', 3)); {F("'tage 3 angenommen'")}
    exception when others then if position('tage' in sqlerrm) = 0 then {F("'tage: falscher Fehler ' || sqlerrm")} end if; end;
    begin r := api.schule_wackelt_analyse('lern:ww-gibt-es-nicht', jsonb_build_object('lernender_id', k)); {F("'unbekannte Sitzung liest die Analyse'")}
    exception when others then null; end;
    begin r := api.schule_fehler_abhaken('lern:ww-gibt-es-nicht', jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0))); {F("'unbekannte Sitzung hakt ab'")}
    exception when others then null; end;
    if pg_temp.ww_bestand() is distinct from h0 then {F("'api-Aktionen verändern Daten außerhalb von fehler_erledigt'")} end if;
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then {F("'Lesevarianten: ' || sqlerrm")}
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
          if (r->>'geaendert')::int <> 1 then {F("'Karte: Abhaken ' || r::text")} end if;
          execute 'select to_jsonb(x) from schule.karte_stand x where x.lernender_id = $1 and x.einheit_id = $2 and x.lernziel = $3' into kz using k, v_e, v_lz;
          if kz is distinct from ko then {F("'Karte: Abhaken ändert die Kartenzeile'")} end if;
          if pg_temp.ww_bestand() is distinct from h0 then {F("'Karte: Abhaken ändert Daten außerhalb von fehler_erledigt'")} end if;
        end if;
        r := pg_temp.ww_ant(k, a2.id, '987654', 'ww-k' || i);   -- zweiter Fehler an derselben Lernkarte
        if r->>'richtig' is distinct from 'false' then {F("'Karte: Fehlantwort nicht als falsch bewertet ' || r::text")} end if;
        execute 'select to_jsonb(x) from schule.karte_stand x where x.lernender_id = $1 and x.einheit_id = $2 and x.lernziel = $3' into r using k, v_e, v_lz;
        kn := coalesce(kn, '{{}}'::jsonb) || jsonb_build_object(case i when 1 then 'mit_abhaken' else 'ohne_abhaken' end,
                jsonb_build_object('nach_1_fehler', jsonb_build_object('sitzt', ko->'sitzt', 'wdh_fehler', ko->'wdh_fehler'),
                                   'nach_2_fehler', jsonb_build_object('sitzt', r->'sitzt', 'wdh_fehler', r->'wdh_fehler', 'geoeffnet', r->'geoeffnet_am' <> 'null'::jsonb),
                                   'zeile', r - 'zuletzt' - 'geoeffnet_am' - 'gezaehlt' - 'sitzt_am' - 'wdh_ab' - 'faellig_am'));
        raise exception using errcode = 'WW999', message = 'zurueck';
      exception when sqlstate 'WW999' then null;
        when others then {F("'Karte (' || i || '): ' || sqlerrm")}
      end;
    end loop;
    if kn->'mit_abhaken'->'zeile' is distinct from kn->'ohne_abhaken'->'zeile' then {F("'Abhaken wirkt auf die Karte: ' || kn::text")} end if;
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
  if exists (select 1 from schule.fehler_erledigt) then {F("'neue Tabelle nicht leer'")} end if;
  if (select (n, m) is distinct from ((select count(*) from schule.versuch), (select coalesce(max(id), 0) from schule.versuch)) from ww_stand) then {F("'Versuche verändert'")} end if;
  if (select ww_stand.b from ww_stand) is distinct from pg_temp.ww_bestand() then {F("'Daten im Schema schule nach dem Paket anders als vorher'")} end if;
  bericht := bericht || jsonb_build_object('schema_bestehend_gleich', not exists (select 1 from ww_def where ww_def.s is distinct from (select ww_stand.s from ww_stand)),
                                           'bestand_gleich', (select ww_stand.b from ww_stand) = pg_temp.ww_bestand(),
                                           'fehler', coalesce(array_length(fehler, 1), 0));
  if array_length(fehler, 1) > 0 then raise exception 'WW-S ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
  {ende}
end $p$;""")


# ---------------------------------------------------------------------------------------------------------------------------------------------
# WW-S3: Paket für die Folgemigration. EIN SQL für EINEN Aufruf (eine Transaktion), prüft sich selbst; bei der kleinsten Abweichung: alles zurück.
#   0. Vorbedingung: WW-S2 ist eingespielt (Tabelle schule.fehler_erledigt und die WW-S2-Funktionen) – sonst Abbruch, bevor etwas geschieht.
#      Fingerabdruck vorher: alle Funktionen in schule/api außer den vier von WW-S3 (also auch die übrigen WW-S2-Funktionen), alle Trigger (auch
#      interne) und Indizes an Tabellen in schule, alle Spalten (außer fehler_erledigt); Aufbau und Inhalt von fehler_erledigt; alle Daten in schule.
#   1. Migration zweimal; danach: Definitionen gleich, Fingerabdruck des Bestehenden gleich, fehler_erledigt (Aufbau und Zeilen) gleich.
#   2. Hauptfall (zurückgerollt): stand 3, feste Typen (mit_tipp/danach_richtig Boolean), Markieren mit geaendert_ids/markierung_ids, erledigt.id/tag,
#      besprochen je Thema (zuletzt, tage, neu_seit – gegen eine unabhängige Nachrechnung), Zurückholen über markierung_ids, PARALLELFALL (zurückgeholt
#      und neu markiert -> veralteter Eintrag übersprungen, neue Markierung bleibt), Doppelte/Überholte/Unbekannte/Fremde, Eingabeprüfung, alter Weg.
#   3. Ohne Thema (zurückgerollt): zwei offene Fehler an einer Lernkarte ohne Thema -> eigenes Thema mit offen >= 2; dann 300 neuere Fehler -> die beiden
#      liegen jenseits der 300, das Thema wird trotzdem gezählt; Summe themen[].offen = offen_zahl. Gibt es keine Einheit ohne Thema, wird eine nur in
#      dieser Untertransaktion ohne Thema gestellt (geht das nicht, steht der Grund im Bericht).
#   4. Rechte mit echten Lern-Sitzungen (zurückgerollt): Kind, fremdes Kind, Eltern, Lehrer, unbekannte Sitzung – Analyse, Markieren, Zurückholen.
#   5. Karte: Markieren, Zurückholen und neu Markieren an einer sitzenden Lernkarte ändern die Kartenzeile nicht; ein weiterer Fehler wirkt wie ohne.
#   6. Laufzeit (Warnung > 500 ms); Ende: fehler_erledigt, Versuche und alle Daten in schule wie vor dem Paket.
def ww3(probe):
    import re
    mig = MIG3.read_text(encoding='utf-8')
    for m in ('$ww3mig$', '$p$', '$f$'):
        assert m not in mig
    neu = 'array[' + ', '.join(f"'{f}'" for f in NEU3) + ']'
    defs = f"(select md5(string_agg(coalesce(pg_get_functiondef(to_regprocedure(f)), 'fehlt'), '#' order by f)) from unnest({neu}) f)"
    ende = ("raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): %', bericht::text;" if probe else
            "raise notice 'WW-S3 eingespielt: %', bericht::text;")
    t = WW3_SQL.replace('__KOPF__', ' --probe' if probe else '').replace('__MIG__', mig).replace('__NEU3__', neu).replace('__DEFS__', defs) \
        .replace('__API__', 'array[' + ', '.join(repr(f) for f in API) + ']').replace('__ENDE__', ende)
    t = re.sub(r'\{\{F:(.*?):F\}\}', lambda m: f'fehler := fehler || ({m.group(1)})::text;', t)
    assert '{{F:' not in t and ':F}}' not in t
    assert not re.search(r'__(KOPF|MIG|NEU3|DEFS|API|ENDE|ZAHL_X2|ZAHL_A)__', t)
    return t


ZAHL = """{a}.pool = 'uebung' and {a}.freigegeben and {e}.status = 'freigegeben' and {a}.antworttyp = 'zahl' and schule.aufgabe_zaehlt({a})
     and ({a}.loesung->>'wert')::numeric <> 987654 and {a}.loesung->>'einheit' is null"""

WW3_SQL = r"""-- WW-S3 Einspiel-Paket (erzeugt von tools/tests/wackelt_einspielen.py --ww3__KOPF__). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);
do $p$ begin
  if to_regclass('schule.fehler_erledigt') is null or to_regprocedure('schule.ww_versuche(bigint, jsonb)') is null
     or to_regprocedure('schule.ww_fehlerart(schule.versuch, schule.aufgabe)') is null or to_regprocedure('schule.ww_von(text)') is null
     or to_regprocedure('schule.wackelt_analyse(bigint, integer, boolean)') is null or to_regprocedure('schule.fehler_abhaken(bigint, jsonb, boolean, text)') is null
     or to_regprocedure('api.schule_fehler_abhaken(text, jsonb)') is null or to_regprocedure('api.schule_wackelt_analyse(text, jsonb)') is null then
    raise exception 'WW-S3 ABBRUCH, Vorbedingung: WW-S2 ist nicht eingespielt (erst ww_s_einspielen.sql) – nichts geändert';
  end if;
end $p$;
create temp table ww3_mig on commit drop as select $ww3mig$__MIG__$ww3mig$::text as sql;
-- Fingerabdruck des Bestehenden: Funktionen in schule/api (ohne die vier von WW-S3), alle Trigger (auch interne) und Indizes an Tabellen in schule,
-- Spalten (ohne fehler_erledigt)
create function pg_temp.ww3_schema() returns text language sql stable as $f$
  select md5(string_agg(x, '#' order by x)) from (
    select 'f:' || p.oid::regprocedure::text || ':' || pg_get_functiondef(p.oid) || ':' || coalesce(p.proacl::text, '') x from pg_proc p
     where p.pronamespace in ('schule'::regnamespace, 'api'::regnamespace) and p.prokind in ('f', 'p')
       and p.oid not in (select o from (select to_regprocedure(f) o from unnest(__NEU3__) f) q where o is not null)
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
create temp table ww3_def on commit drop as select 1 lauf, __DEFS__ d, pg_temp.ww3_fe_aufbau() o, pg_temp.ww3_schema() s, pg_temp.ww3_fe() fe;
do $p$ begin execute (select sql from ww3_mig); end $p$;
insert into ww3_def select 2, __DEFS__, pg_temp.ww3_fe_aufbau(), pg_temp.ww3_schema(), pg_temp.ww3_fe();
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
do $p$
declare
  fehler text[] := '{}'; k bigint := (select id from schule.lernender where ist_test order by id limit 1); v_e bigint; v_lz text; v_th bigint;
  a1 schule.aufgabe; a2 schule.aufgabe; a3 schule.aufgabe; v1 bigint; v2 bigint; v3 bigint; m1 bigint; m2 bigint; m1b bigint; mf bigint; mid bigint;
  r jsonb; q jsonb; x text; bericht jsonb := '{}'; t0 timestamptz; ms numeric; v_f bigint; v_gross bigint; v_eo bigint; b1 bigint; b2 bigint;
  s_kind text; s_fremd text; s_eltern text; s_lehrer text; v_id bigint; kn jsonb; ko jsonb; kz jsonb; h0 text; v0 bigint; arr bigint[]; n int; i int; vor int; weg text;
begin
  if (select count(distinct ww3_def.d) from ww3_def) <> 1 or (select count(distinct ww3_def.o) from ww3_def) <> 1 then {{F:'zweiter Lauf hat etwas geändert':F}} end if;
  if exists (select 1 from ww3_def where ww3_def.s is distinct from (select ww3_stand.s from ww3_stand)) then
    {{F:'Migration ändert Funktionen, Trigger, Indizes oder Spalten außerhalb von WW-S3':F}} end if;
  if exists (select 1 from ww3_def where ww3_def.o is distinct from (select ww3_stand.o from ww3_stand)) then {{F:'Migration ändert den Aufbau von fehler_erledigt':F}} end if;
  if exists (select 1 from ww3_def where ww3_def.fe is distinct from (select ww3_stand.fe from ww3_stand)) then {{F:'Migration ändert Zeilen von fehler_erledigt':F}} end if;
  -- Rechte
  if not (select relrowsecurity from pg_class where oid = 'schule.fehler_erledigt'::regclass) then {{F:'fehler_erledigt: RLS aus':F}} end if;
  if exists (select 1 from pg_policy where polrelid = 'schule.fehler_erledigt'::regclass) then {{F:'fehler_erledigt: hat eine Policy':F}} end if;
  if has_table_privilege('anon', 'schule.fehler_erledigt', 'select') or has_table_privilege('authenticated', 'schule.fehler_erledigt', 'select')
     or has_table_privilege('authenticated', 'schule.fehler_erledigt', 'update') then {{F:'fehler_erledigt: App-Rollen haben Rechte':F}} end if;
  if exists (select 1 from pg_constraint where contype = 'f' and (conrelid = 'schule.fehler_erledigt'::regclass or confrelid = 'schule.fehler_erledigt'::regclass)) then
    {{F:'fehler_erledigt: Fremdschlüssel':F}} end if;
  for x in select unnest(__NEU3__) loop
    if has_function_privilege('anon', x, 'execute') or has_function_privilege('authenticated', x, 'execute') then {{F:x || ': für App-Rollen aufrufbar':F}} end if;
    if exists (select 1 from pg_proc p where p.oid = x::regprocedure and (p.proacl is null or exists (select 1 from aclexplode(p.proacl) a where a.grantee = 0))) then
      {{F:x || ': für PUBLIC aufrufbar':F}} end if;
  end loop;
  for x in select unnest(__API__) loop
    if position('if not schule.ist_leiter(p_schluessel) then raise exception' in pg_get_functiondef(x::regprocedure)) = 0 then {{F:x || ': prüft ist_leiter nicht':F}} end if;
  end loop;
  if exists (select 1 from pg_trigger t where t.tgrelid = 'schule.versuch'::regclass and t.tgname ~ '^(ww|fehler)') then {{F:'Trigger der WW-Seite an schule.versuch':F}} end if;
  begin
    r := api.schule_wackelt_analyse('ww-unbekannter-schluessel', jsonb_build_object('lernender_id', k));
    {{F:'unbekannter Schlüssel bekommt eine Analyse':F}}
  exception when others then null;
  end;
  -- Lernkarte mit mindestens drei zählenden Zahl-Aufgaben (wie WW-S2)
  select x2.einheit_id, x2.variante_gruppe into v_e, v_lz from schule.aufgabe x2 join schule.einheit e on e.id = x2.einheit_id
   where __ZAHL_X2__
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
    x := pg_temp.ww3_typen(r); if x is not null then {{F:'Typen: ' || x:F}} end if;
    if not (array[v1, v2, v3] <@ pg_temp.ww3_ids(r, 'offen')) then {{F:'Analyse: falsche Antworten nicht offen':F}} end if;
    q := pg_temp.ww3_eintrag(r, 'offen', v1);
    if q->'danach_richtig' is distinct from 'true'::jsonb or not (q->'danach_richtig_am' ? 'aufgabe_am') then
      bericht := bericht || jsonb_build_object('hinweis_danach_richtig', 'richtige Antwort nicht erkannt – danach_richtig nicht beobachtet: ' || left(coalesce(q::text, '-'), 200)); end if;
    if not pg_temp.ww3_summe_ok(r) then {{F:'Summe themen[].offen ist nicht offen_zahl':F}} end if;
    -- Markieren (zwei auf einmal)
    r := schule.fehler_abhaken(k, jsonb_build_array(v2, v1), false, 'probe');
    if (r->>'geaendert')::int <> 2 or pg_temp.ww3_arr(r->'geaendert_ids') <> array[least(v1, v2), greatest(v1, v2)] or (r->>'stand') is distinct from '3' then
      {{F:'Markieren: ' || r::text:F}} end if;
    select id into m1 from schule.fehler_erledigt where versuch_id = v1 and zurueckgenommen_am is null;
    select id into m2 from schule.fehler_erledigt where versuch_id = v2 and zurueckgenommen_am is null;
    if pg_temp.ww3_arr(r->'markierung_ids') is distinct from (select array_agg(z order by z) from unnest(array[m1, m2]) z) then {{F:'Markieren: markierung_ids passen nicht ' || r::text:F}} end if;
    r := schule.fehler_abhaken(k, jsonb_build_array(v1), false, 'probe');
    if (r->>'geaendert')::int <> 0 or r->'geaendert_ids' <> '[]'::jsonb or r->'markierung_ids' <> '[]'::jsonb then {{F:'zweites Markieren ändert etwas: ' || r::text:F}} end if;
    r := schule.wackelt_analyse(k, 14, true);
    q := pg_temp.ww3_eintrag(r, 'erledigt', v1);
    if (q->'erledigt'->>'id')::bigint is distinct from m1 or not (q->'erledigt' ? 'tag') or q->'erledigt'->>'art' is distinct from 'abgehakt' then {{F:'erledigt.id/tag fehlt: ' || coalesce(q->>'erledigt', '-'):F}} end if;
    if v1 = any(pg_temp.ww3_ids(r, 'offen')) then {{F:'markierte Antwort noch offen':F}} end if;
    x := pg_temp.ww3_typen(r); if x is not null then {{F:'Typen (mit erledigt): ' || x:F}} end if;
    -- besprochen je Thema: zwei Gesprächstage, ein neuer Fehler danach
    update schule.fehler_erledigt set am = now() - interval '2 days' where id = m1;   -- nur die eigene Tabelle, in dieser Untertransaktion
    update schule.fehler_erledigt set am = now() - interval '1 hour' where id = m2;
    r := schule.wackelt_analyse(k, 0, false);
    q := pg_temp.ww3_thema(r, v_th);
    if q->'besprochen' is null or (q->'besprochen'->>'tage')::int < 2 or (q->'besprochen'->>'neu_seit')::int < 1 or (q->'besprochen'->>'fehler')::int < 2 then {{F:'besprochen fehlt oder falsch: ' || coalesce(q::text, '-'):F}} end if;
    x := pg_temp.ww3_bespr_ok(k, r); if x is not null then {{F:'besprochen weicht von der Nachrechnung ab: ' || x:F}} end if;
    bericht := bericht || jsonb_build_object('besprochen_beispiel', q->'besprochen');
    -- Zurückholen über markierung_ids
    r := schule.fehler_zurueckholen(k, jsonb_build_array(m1), 'probe');
    if (r->>'geaendert')::int <> 1 or pg_temp.ww3_arr(r->'geaendert_ids') <> array[m1] or r->'uebersprungen' <> '[]'::jsonb then {{F:'Zurückholen: ' || r::text:F}} end if;
    r := schule.wackelt_analyse(k, 0, false);
    if not v1 = any(pg_temp.ww3_ids(r, 'offen')) then {{F:'nach Zurückholen nicht wieder offen':F}} end if;
    x := pg_temp.ww3_bespr_ok(k, r); if x is not null then {{F:'besprochen nach Zurückholen: ' || x:F}} end if;
    if (pg_temp.ww3_thema(r, v_th)->'besprochen'->>'tage')::int is distinct from (pg_temp.ww3_bespr(k, v_th)->>'tage')::int then {{F:'besprochen zählt zurückgeholte Markierungen':F}} end if;
    -- PARALLELFALL: v1 ist zurückgeholt und wird neu markiert; ein Klick auf den veralteten Eintrag (m1) darf die neue Markierung nicht entfernen
    r := schule.fehler_abhaken(k, jsonb_build_array(v1), false, 'probe');
    m1b := (pg_temp.ww3_arr(r->'markierung_ids'))[1];
    if m1b is null or m1b = m1 or pg_temp.ww3_arr(r->'geaendert_ids') <> array[v1] then {{F:'neu markieren: ' || r::text:F}} end if;
    r := schule.fehler_zurueckholen(k, jsonb_build_array(m1), 'probe');
    if (r->>'geaendert')::int <> 0 or r->'geaendert_ids' <> '[]'::jsonb
       or r->'uebersprungen' <> jsonb_build_array(jsonb_build_object('markierung_id', m1, 'versuch_id', v1, 'grund', 'überholt')) then {{F:'Parallelfall: ' || r::text:F}} end if;
    if not exists (select 1 from schule.fehler_erledigt where id = m1b and zurueckgenommen_am is null) then {{F:'Parallelfall: neue Markierung entfernt':F}} end if;
    if v1 = any(pg_temp.ww3_ids(schule.wackelt_analyse(k, 0, false), 'offen')) then {{F:'Parallelfall: neu markierte Antwort wieder offen':F}} end if;
    bericht := bericht || jsonb_build_object('parallelfall', jsonb_build_object('veraltet', m1, 'neu', m1b, 'antwort', r));
    -- doppelt genannt, dann schon zurückgeholt
    r := schule.fehler_zurueckholen(k, jsonb_build_array(m1b, m1b, m2), 'probe');
    if (r->>'geaendert')::int <> 2 or pg_temp.ww3_arr(r->'geaendert_ids') <> (select array_agg(z order by z) from unnest(array[m1b, m2]) z) then {{F:'Zurückholen doppelt: ' || r::text:F}} end if;
    r := schule.fehler_zurueckholen(k, jsonb_build_array(m2), 'probe');
    if (r->>'geaendert')::int <> 0 or r->'uebersprungen'->0->>'grund' is distinct from 'schon zurückgeholt' then {{F:'schon zurückgeholt: ' || r::text:F}} end if;
    x := pg_temp.ww3_bespr_ok(k, schule.wackelt_analyse(k, 0, false)); if x is not null then {{F:'besprochen nach allem Zurückholen: ' || x:F}} end if;
    -- fremde und unbekannte Markierungen: übersprungen, nichts verraten, nichts geändert
    insert into schule.fehler_erledigt (lernender_id, versuch_id, von) values (coalesce(v_f, -1), -987654, 'probe') returning id into mf;
    r := schule.fehler_zurueckholen(k, jsonb_build_array(mf, 0), 'probe');
    if (r->>'geaendert')::int <> 0 or jsonb_array_length(r->'uebersprungen') <> 2
       or exists (select 1 from jsonb_array_elements(r->'uebersprungen') u where u->>'grund' <> 'nicht gefunden' or u ? 'versuch_id') then {{F:'fremde/unbekannte Markierung: ' || r::text:F}} end if;
    if not exists (select 1 from schule.fehler_erledigt where id = mf and zurueckgenommen_am is null) then {{F:'fremde Markierung zurückgeholt':F}} end if;
    -- Eingabeprüfung
    foreach q in array array['[]'::jsonb, '[1.5]'::jsonb, '"7"'::jsonb, '["x"]'::jsonb, to_jsonb(array(select generate_series(1, 201)))] loop
      begin perform schule.fehler_zurueckholen(k, q, 'probe'); {{F:'markierung_ids angenommen: ' || left(q::text, 40):F}}
      exception when others then if position('markierung_ids' in sqlerrm) = 0 then {{F:'markierung_ids: falscher Fehler ' || sqlerrm:F}} end if; end;
    end loop;
    -- alter Weg (Verträglichkeit): Zurücknehmen über versuch_ids
    r := schule.fehler_abhaken(k, jsonb_build_array(v2), false, 'probe');
    r := schule.fehler_abhaken(k, jsonb_build_array(v2), true, 'probe');
    if (r->>'geaendert')::int <> 1 or pg_temp.ww3_arr(r->'geaendert_ids') <> array[v2] or r ? 'markierung_ids' then {{F:'alter Weg zurück: ' || r::text:F}} end if;
    r := schule.fehler_abhaken(k, jsonb_build_array(0, coalesce((select min(id) from schule.versuch where lernender_id <> k), 0)), false, 'probe');
    if (r->>'geaendert')::int <> 0 or jsonb_array_length(r->'uebersprungen') = 0 or r->'markierung_ids' <> '[]'::jsonb then {{F:'fremde Versuche markiert: ' || r::text:F}} end if;
    if pg_temp.ww3_bestand() is distinct from h0 then {{F:'Markieren/Zurückholen verändert Daten außerhalb von fehler_erledigt':F}} end if;
    bericht := bericht || jsonb_build_object('bestand_gleich_beim_markieren', pg_temp.ww3_bestand() = h0, 'typen_ok', true);
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then {{F:'Hauptfall: ' || sqlerrm:F}}
  end;

  -- 2b. Zeitzone: Kind in Pacific/Auckland (nur in dieser Untertransaktion), Markierung um 00:05 Ortszeit (in UTC noch der Vortag) ->
  --     besprochen.zuletzt_tag und erledigt.tag sind der Ortstag, nicht der UTC-Tag
  begin
    update schule.lernender set zeitzone = 'Pacific/Auckland' where id = k;
    perform pg_temp.ww3_ant(k, a1.id, '987654', 'ww3-tz');
    select id into v1 from schule.versuch where lernender_id = k and client_id = 'ww3-tz';
    r := schule.fehler_abhaken(k, jsonb_build_array(v1), false, 'probe');
    mid := (pg_temp.ww3_arr(r->'markierung_ids'))[1];
    t0 := (date_trunc('day', now() at time zone 'Pacific/Auckland') + interval '5 minutes') at time zone 'Pacific/Auckland';   -- heute 00:05 Ortszeit
    update schule.fehler_erledigt set am = t0 where id = mid;
    if (t0 at time zone 'UTC')::date = (t0 at time zone 'Pacific/Auckland')::date then {{F:'Zeitzone: Prüffall trennt Ortstag und UTC-Tag nicht':F}} end if;
    r := schule.wackelt_analyse(k, 0, true);
    q := pg_temp.ww3_thema(r, v_th);
    if (q->'besprochen'->>'zuletzt')::timestamptz = t0 and q->'besprochen'->>'zuletzt_tag' is distinct from ((t0 at time zone 'Pacific/Auckland')::date)::text then
      {{F:'Zeitzone: zuletzt_tag ' || coalesce(q->'besprochen'->>'zuletzt_tag', 'fehlt') || ' statt Ortstag ' || (t0 at time zone 'Pacific/Auckland')::date:F}} end if;
    if (q->'besprochen'->>'zuletzt')::timestamptz is distinct from t0 then
      bericht := bericht || jsonb_build_object('hinweis_zeitzone', 'eine spätere Markierung im Thema – zuletzt_tag nur gegen die Nachrechnung geprüft'); end if;
    if pg_temp.ww3_eintrag(r, 'erledigt', v1)->'erledigt'->>'tag' is distinct from ((t0 at time zone 'Pacific/Auckland')::date)::text then
      {{F:'Zeitzone: erledigt.tag ist nicht der Ortstag':F}} end if;
    x := pg_temp.ww3_bespr_ok(k, r); if x is not null then {{F:'Zeitzone: besprochen weicht von der Nachrechnung ab: ' || x:F}} end if;
    x := pg_temp.ww3_typen(r); if x is not null then {{F:'Zeitzone, Typen: ' || x:F}} end if;
    bericht := bericht || jsonb_build_object('zeitzone', jsonb_build_object('zone', 'Pacific/Auckland', 'markiert_utc', (t0 at time zone 'UTC')::text,
                 'zuletzt_tag', q->'besprochen'->'zuletzt_tag', 'utc_tag', (t0 at time zone 'UTC')::date));
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then {{F:'Zeitzone: ' || sqlerrm:F}}
  end;

  -- 3. Ohne Thema: zwei offene Fehler, dann 300 neuere – das Thema „ohne“ wird immer gezählt
  begin
    weg := 'vorhanden';
    select a.einheit_id into v_eo from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id where e.thema_id is null and __ZAHL_A__
     group by 1 having count(*) >= 2 order by 1 limit 1;
    if v_eo is null then
      select a.einheit_id into v_eo from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id where __ZAHL_A__ group by 1 having count(*) >= 2 order by 1 limit 1;
      begin
        update schule.einheit set thema_id = null where id = v_eo;   -- nur in dieser (zurückgerollten) Untertransaktion
        weg := 'vorübergehend ohne Thema';
      exception when others then weg := 'übersprungen: ' || sqlerrm; v_eo := null;
      end;
    end if;
    if v_eo is not null then
      arr := array(select a.id from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id where a.einheit_id = v_eo and __ZAHL_A__ order by a.id limit 2);
      perform pg_temp.ww3_ant(k, arr[1], '987654', 'ww3-o1');
      perform pg_temp.ww3_ant(k, arr[2], '987654', 'ww3-o2');
      select id into b1 from schule.versuch where lernender_id = k and client_id = 'ww3-o1';
      select id into b2 from schule.versuch where lernender_id = k and client_id = 'ww3-o2';
      h0 := pg_temp.ww3_bestand();
      r := schule.wackelt_analyse(k, 14, false);
      q := pg_temp.ww3_thema(r, null);
      if q is null or (q->>'offen')::int < 2 then {{F:'ohne Thema: offen nicht gezählt ' || coalesce(q::text, 'Thema fehlt'):F}} end if;
      if not pg_temp.ww3_summe_ok(r) then {{F:'ohne Thema: Summe themen[].offen ist nicht offen_zahl':F}} end if;
      x := pg_temp.ww3_typen(r) ; if x is not null then {{F:'ohne Thema, Typen: ' || x:F}} end if;
      vor := (r->>'offen_zahl')::int;
      bericht := bericht || jsonb_build_object('ohne_thema', jsonb_build_object('weg', 'vorhanden', 'offen_ohne_thema', q->'offen', 'offen_zahl', vor));
      -- 300 neuere Fehler an Lernkarten mit Thema
      arr := array(select a.id from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id where e.thema_id is not null and __ZAHL_A__ order by a.id limit 300);
      n := 0; i := 0;
      while n < 300 and i < 900 and cardinality(arr) > 0 loop
        i := i + 1;
        begin perform pg_temp.ww3_ant(k, arr[1 + (i - 1) % cardinality(arr)], '987654', 'ww3-m' || i); n := n + 1;
        exception when others then null; end;
      end loop;
      r := schule.wackelt_analyse(k, 14, false);
      q := pg_temp.ww3_thema(r, null);
      if q is null or (q->>'offen')::int < 2 then {{F:'ohne Thema jenseits der 300: nicht gezählt ' || coalesce(q::text, 'Thema fehlt'):F}} end if;
      if not pg_temp.ww3_summe_ok(r) then {{F:'ohne Thema jenseits der 300: Summe themen[].offen ist nicht offen_zahl':F}} end if;
      if (r->>'offen_zahl')::int >= vor + 300 and (b1 = any(pg_temp.ww3_ids(r, 'offen')) or b2 = any(pg_temp.ww3_ids(r, 'offen'))) then
        {{F:'ohne Thema: Fehler nicht jenseits der 300 neuesten':F}} end if;
      t0 := clock_timestamp(); perform schule.wackelt_analyse(k, 0, true); ms := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
      bericht := jsonb_set(bericht, '{ohne_thema}', (bericht->'ohne_thema') || jsonb_build_object('weg', weg, 'neue_fehler', n, 'offen_zahl_danach', r->'offen_zahl',
                   'offen_ohne_thema_danach', q->'offen', 'jenseits_300', (r->>'offen_zahl')::int > 300 and not (b1 = any(pg_temp.ww3_ids(r, 'offen'))), 'laufzeit_ms_300', ms));
      if (r->>'offen_zahl')::int < vor + 300 then bericht := bericht || jsonb_build_object('hinweis_ohne_thema', 'weniger als 300 neue offene Fehler angelegt: ' || n); end if;
    else
      bericht := bericht || jsonb_build_object('ohne_thema', jsonb_build_object('weg', weg));
    end if;
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then {{F:'Ohne Thema: ' || sqlerrm:F}}
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
      begin r := api.schule_wackelt_analyse(x, jsonb_build_object('lernender_id', k)); {{F:'Kind liest die Analyse':F}}
      exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then {{F:'Kind/Analyse: falscher Fehler ' || sqlerrm:F}} end if; end;
      begin r := api.schule_fehler_abhaken(x, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0))); {{F:'Kind markiert':F}}
      exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then {{F:'Kind/Markieren: falscher Fehler ' || sqlerrm:F}} end if; end;
      begin r := api.schule_fehler_abhaken(x, jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid), 'zurueck', true)); {{F:'Kind holt zurück':F}}
      exception when others then if position('Nur Eltern/Lehrer' in sqlerrm) = 0 then {{F:'Kind/Zurückholen: falscher Fehler ' || sqlerrm:F}} end if; end;
    end loop;
    if s_fremd is null then bericht := bericht || '{"hinweis_fremdkind": "kein zweites aktives Kind – Fremdkind-Probe übersprungen"}'::jsonb; end if;
    if not exists (select 1 from schule.fehler_erledigt where id = mid and zurueckgenommen_am is null) then {{F:'Kind-Sitzung hat zurückgeholt':F}} end if;
    delete from schule.fehler_erledigt where id = mid;   -- nur die eben angelegte Probezeile
    r := api.schule_wackelt_analyse(s_eltern, jsonb_build_object('lernender_id', k, 'tage', 0, 'erledigt', true));
    if r->>'ok' is distinct from 'true' or (r->>'stand') is distinct from '3' then {{F:'Eltern lesen die Analyse nicht (stand 3)':F}} end if;
    r := api.schule_fehler_abhaken(s_eltern, jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0)));
    mid := (pg_temp.ww3_arr(r->'markierung_ids'))[1];
    if (r->>'geaendert')::int <> 1 or mid is null or pg_temp.ww3_arr(r->'geaendert_ids') <> array[v0] then {{F:'Eltern markieren nicht: ' || r::text:F}} end if;
    if (select von from schule.fehler_erledigt where id = mid) is distinct from 'eltern:WW3-Probe Eltern' then {{F:'von falsch':F}} end if;
    begin r := api.schule_fehler_abhaken(s_eltern, jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid))); {{F:'markierung_ids ohne zurueck angenommen':F}}
    exception when others then if position('markierung_ids nur mit zurueck' in sqlerrm) = 0 then {{F:'markierung_ids ohne zurueck: falscher Fehler ' || sqlerrm:F}} end if; end;
    begin r := api.schule_fehler_abhaken(s_eltern, jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid), 'versuch_ids', jsonb_build_array(v0), 'zurueck', true));
      {{F:'versuch_ids und markierung_ids zusammen angenommen':F}}
    exception when others then if position('entweder versuch_ids oder markierung_ids' in sqlerrm) = 0 then {{F:'beide Listen: falscher Fehler ' || sqlerrm:F}} end if; end;
    r := api.schule_wackelt_analyse(s_lehrer, jsonb_build_object('lernender_id', k, 'tage', 7, 'erledigt', true));
    if (pg_temp.ww3_eintrag(r, 'erledigt', v0)->'erledigt'->>'id')::bigint is distinct from mid then {{F:'Lehrer: erledigt.id fehlt':F}} end if;
    r := api.schule_fehler_abhaken(s_lehrer, jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid), 'zurueck', true));
    if (r->>'geaendert')::int <> 1 or pg_temp.ww3_arr(r->'geaendert_ids') <> array[mid] then {{F:'Lehrer holen nicht zurück: ' || r::text:F}} end if;
    if (select zurueckgenommen_von from schule.fehler_erledigt where id = mid) is distinct from 'lehrer:WW3-Probe Lehrer' then {{F:'zurueckgenommen_von falsch':F}} end if;
    r := api.schule_fehler_abhaken(s_lehrer, jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid), 'zurueck', true));
    if (r->>'geaendert')::int <> 0 or r->'uebersprungen'->0->>'grund' is distinct from 'schon zurückgeholt' then {{F:'Lehrer zweimal zurück: ' || r::text:F}} end if;
    begin r := api.schule_wackelt_analyse(s_eltern, jsonb_build_object('lernender_id', k, 'tage', 3)); {{F:'tage 3 angenommen':F}}
    exception when others then if position('tage' in sqlerrm) = 0 then {{F:'tage: falscher Fehler ' || sqlerrm:F}} end if; end;
    begin r := api.schule_wackelt_analyse('lern:ww3-gibt-es-nicht', jsonb_build_object('lernender_id', k)); {{F:'unbekannte Sitzung liest die Analyse':F}}
    exception when others then null; end;
    begin r := api.schule_fehler_abhaken('lern:ww3-gibt-es-nicht', jsonb_build_object('lernender_id', k, 'versuch_ids', jsonb_build_array(v0))); {{F:'unbekannte Sitzung markiert':F}}
    exception when others then null; end;
    begin r := api.schule_fehler_abhaken('lern:ww3-gibt-es-nicht', jsonb_build_object('lernender_id', k, 'markierung_ids', jsonb_build_array(mid), 'zurueck', true)); {{F:'unbekannte Sitzung holt zurück':F}}
    exception when others then null; end;
    if pg_temp.ww3_bestand() is distinct from h0 then {{F:'api-Aktionen verändern Daten außerhalb von fehler_erledigt':F}} end if;
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then {{F:'Rechte: ' || sqlerrm:F}}
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
          r := schule.fehler_abhaken(k, jsonb_build_array((select id from schule.versuch where lernender_id = k and client_id = 'ww3-k0')), false, 'probe');
          mid := (pg_temp.ww3_arr(r->'markierung_ids'))[1];
          r := schule.fehler_zurueckholen(k, jsonb_build_array(mid), 'probe');
          if (r->>'geaendert')::int <> 1 then {{F:'Karte: Zurückholen ' || r::text:F}} end if;
          r := schule.fehler_abhaken(k, jsonb_build_array((select id from schule.versuch where lernender_id = k and client_id = 'ww3-k0')), false, 'probe');
          if (r->>'geaendert')::int <> 1 then {{F:'Karte: neu Markieren ' || r::text:F}} end if;
          execute 'select to_jsonb(x) from schule.karte_stand x where x.lernender_id = $1 and x.einheit_id = $2 and x.lernziel = $3' into kz using k, v_e, v_lz;
          if kz is distinct from ko then {{F:'Karte: Markieren/Zurückholen ändert die Kartenzeile':F}} end if;
          if pg_temp.ww3_bestand() is distinct from h0 then {{F:'Karte: Markieren/Zurückholen ändert Daten außerhalb von fehler_erledigt':F}} end if;
        end if;
        r := pg_temp.ww3_ant(k, a2.id, '987654', 'ww3-k' || i);
        if r->>'richtig' is distinct from 'false' then {{F:'Karte: Fehlantwort nicht als falsch bewertet ' || r::text:F}} end if;
        execute 'select to_jsonb(x) from schule.karte_stand x where x.lernender_id = $1 and x.einheit_id = $2 and x.lernziel = $3' into r using k, v_e, v_lz;
        kn := coalesce(kn, '{}'::jsonb) || jsonb_build_object(case i when 1 then 'mit_markierung' else 'ohne_markierung' end,
                jsonb_build_object('nach_1_fehler', jsonb_build_object('sitzt', ko->'sitzt', 'wdh_fehler', ko->'wdh_fehler'),
                                   'nach_2_fehler', jsonb_build_object('sitzt', r->'sitzt', 'wdh_fehler', r->'wdh_fehler', 'geoeffnet', r->'geoeffnet_am' <> 'null'::jsonb),
                                   'zeile', r - 'zuletzt' - 'geoeffnet_am' - 'gezaehlt' - 'sitzt_am' - 'wdh_ab' - 'faellig_am'));
        raise exception using errcode = 'WW999', message = 'zurueck';
      exception when sqlstate 'WW999' then null;
        when others then {{F:'Karte (' || i || '): ' || sqlerrm:F}}
      end;
    end loop;
    if kn->'mit_markierung'->'zeile' is distinct from kn->'ohne_markierung'->'zeile' then {{F:'Markierung wirkt auf die Karte: ' || kn::text:F}} end if;
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
  if pg_temp.ww3_fe() is distinct from (select ww3_stand.fe from ww3_stand) then {{F:'fehler_erledigt nach dem Paket anders als vorher':F}} end if;
  if (select (ww3_stand.n, ww3_stand.m) is distinct from ((select count(*) from schule.versuch), (select coalesce(max(id), 0) from schule.versuch)) from ww3_stand) then {{F:'Versuche verändert':F}} end if;
  if (select ww3_stand.b from ww3_stand) is distinct from pg_temp.ww3_bestand() then {{F:'Daten im Schema schule nach dem Paket anders als vorher':F}} end if;
  bericht := bericht || jsonb_build_object('stand_vorher', (select stand_vorher from ww3_stand),
                                           'schema_bestehend_gleich', not exists (select 1 from ww3_def where ww3_def.s is distinct from (select ww3_stand.s from ww3_stand)),
                                           'fehler_erledigt_gleich', pg_temp.ww3_fe() = (select ww3_stand.fe from ww3_stand)
                                                                     and not exists (select 1 from ww3_def where ww3_def.o is distinct from (select ww3_stand.o from ww3_stand)),
                                           'fehler_erledigt_zeilen', (select count(*) from schule.fehler_erledigt),
                                           'mit_fehlbild', to_regprocedure('schule.versuch_regelbezug(schule.versuch)') is not null,
                                           'bestand_gleich', (select ww3_stand.b from ww3_stand) = pg_temp.ww3_bestand(),
                                           'fehler', coalesce(array_length(fehler, 1), 0));
  if array_length(fehler, 1) > 0 then raise exception 'WW-S3 ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
  __ENDE__
end $p$;""".replace('__ZAHL_X2__', ZAHL.format(a='x2', e='e')).replace('__ZAHL_A__', ZAHL.format(a='a', e='e'))


if __name__ == '__main__':
    main()
