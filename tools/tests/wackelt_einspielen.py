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
"""
import sys
from pathlib import Path

MIG = Path(__file__).resolve().parent.parent.parent / 'supabase/migrations/20261205_ww_s_wackelt.sql'
NEU = ['schule.ww_fehlerart(schule.versuch, schule.aufgabe)', 'schule.ww_von(text)', 'schule.wackelt_analyse(bigint, integer, boolean)',
       'schule.ww_versuche(bigint, jsonb)', 'schule.fehler_abhaken(bigint, jsonb, boolean, text)',
       'api.schule_wackelt_analyse(text, jsonb)', 'api.schule_fehler_abhaken(text, jsonb)']
API = ['api.schule_wackelt_analyse(text, jsonb)', 'api.schule_fehler_abhaken(text, jsonb)']


def F(msg):
    return f'fehler := fehler || ({msg})::text;'


def main():
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


if __name__ == '__main__':
    main()
