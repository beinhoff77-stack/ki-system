"""Einspiel-Paket für WW-S („Was wackelt“, Teil Datenbank) – prüft sich selbst. Muster: tools/tests/regelbezug_einspielen.py.

EIN SQL für EINEN Aufruf (eine Transaktion). Bei der kleinsten Abweichung: Ausnahme -> alles zurück.
  1. Migration ausführen, dann vollständig noch einmal (zweiter Lauf ändert nichts: Definitionen, Indizes, Regel).
  2. Prüfblock mit dem Testkind (alles in einer zurückgerollten Untertransaktion): drei Aufgaben einer Lernkarte (Typ zahl, freigegeben, zählend);
     zwei endgültig falsche Antworten -> beide offen in der Analyse, mit Aufgabe, Lösung, Lernkarte, Auswertung je Thema und Lerntag;
     Abhaken -> weg aus „offen“, unter „erledigt“; zweites Abhaken ändert nichts; Rückgängig -> wieder offen; fremder/richtiger Versuch -> übersprungen;
     Nachüben schicken -> andere Aufgabe derselben Lernkarte, zweites Schicken „liegt schon bereit“; Liste fürs Kind ohne Lösung;
     richtig ohne Tipp -> Fehler „nachgeübt“, Liste leer.
  3. Rechte: Tabellen mit RLS ohne Policy, keine Rechte für anon/authenticated; api-Funktionen nicht für anon/authenticated; die drei
     Eltern-Aktionen prüfen ist_leiter; ein unbekannter Schlüssel bekommt nichts.
  4. Ende: neue Tabellen leer, keine neuen Versuche.
Aufruf:  python3 -I tools/tests/wackelt_einspielen.py > ww.sql   |   --probe > ww_probe.sql (rollt am Ende alles zurück)
Nicht ohne den ausdrücklichen Satz des Nutzers ausführen. Vorher: werkstatt_sperre. Nachher: werkstatt_aenderung. Danach lernen-api (Aktionen) ergänzen.
"""
import sys
from pathlib import Path

MIG = Path(__file__).resolve().parent.parent.parent / 'supabase/migrations/20261205_ww_s_wackelt.sql'
NEU = ['schule.ww_fehlerart(schule.versuch, schule.aufgabe)', 'schule.ww_von(text)', 'schule.wackelt_analyse(bigint, integer, boolean)',
       'schule.ww_versuche(bigint, jsonb)', 'schule.fehler_abhaken(bigint, jsonb, boolean, text)', 'schule.nachueben_schicken(bigint, jsonb, boolean, text)',
       'schule.nachueben_liste(bigint)', 'api.schule_wackelt_analyse(text, jsonb)', 'api.schule_fehler_abhaken(text, jsonb)',
       'api.schule_nachueben_schicken(text, jsonb)', 'api.schule_nachueben_lesen(text, jsonb)']


def F(msg):
    return f'fehler := fehler || ({msg})::text;'


def main():
    probe = '--probe' in sys.argv[1:]
    mig = MIG.read_text(encoding='utf-8')
    for m in ('$wwmig$', '$p$', '$f$'):
        assert m not in mig
    k = '(select id from schule.lernender where ist_test order by id limit 1)'
    defs = "(select md5(string_agg(coalesce(pg_get_functiondef(to_regprocedure(f)), 'fehlt'), '#' order by f)) from unnest(array[" + ', '.join(f"'{f}'" for f in NEU) + "]) f)"
    obj = """(select md5(string_agg(s.x, '#' order by s.x)) from (
       select 'idx:' || indexrelid::regclass::text from pg_index where indrelid in ('schule.fehler_erledigt'::regclass, 'schule.nachueben'::regclass)
       union all select 'col:' || attrelid::regclass::text || attname from pg_attribute where attrelid in ('schule.fehler_erledigt'::regclass, 'schule.nachueben'::regclass) and attnum > 0
       union all select 'regel:' || wert::text from schule.regel where schluessel = 'nachueben_je_tag') s(x))"""
    ende = ("raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): %', bericht::text;" if probe else
            "raise notice 'WW-S eingespielt: %', bericht::text;")
    print(f"""-- WW-S Einspiel-Paket (erzeugt von tools/tests/wackelt_einspielen.py{' --probe' if probe else ''}). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);
create temp table ww_mig on commit drop as select $wwmig${mig}$wwmig$::text as sql;
create temp table ww_stand on commit drop as select (select count(*) from schule.versuch) n, (select coalesce(max(id), 0) from schule.versuch) m;
do $p$ begin execute (select sql from ww_mig); end $p$;
create temp table ww_def on commit drop as select 1 lauf, {defs} d, {obj} o;
do $p$ begin execute (select sql from ww_mig); end $p$;
insert into ww_def select 2, {defs}, {obj};
create function pg_temp.ww_ant(p_k bigint, p_id bigint, p_wert text, p_cid text) returns jsonb language plpgsql as $f$
begin
  return schule.uebung_pruefen_wd(p_k, jsonb_build_object('aufgabe_id', p_id, 'client_id', p_cid, 'antwort', jsonb_build_object('wert', p_wert)));
end $f$;
create function pg_temp.ww_ids(r jsonb, p text) returns bigint[] language sql immutable as $f$
  select coalesce(array_agg((e->>'versuch_id')::bigint), '{{}}') from jsonb_array_elements(coalesce(r->p, '[]'::jsonb)) e $f$;
do $p$
declare
  fehler text[] := '{{}}'; k bigint := {k}; v_e bigint; v_lz text; a1 schule.aufgabe; a2 schule.aufgabe; v1 bigint; v2 bigint; r jsonb; x text; b schule.aufgabe;
  bericht jsonb := '{{}}';
begin
  if (select count(distinct ww_def.d) from ww_def) <> 1 or (select count(distinct ww_def.o) from ww_def) <> 1 then {F("'zweiter Lauf hat etwas geändert'")} end if;
  -- Rechte
  for x in select unnest(array['schule.fehler_erledigt', 'schule.nachueben']) loop
    if not (select relrowsecurity from pg_class where oid = x::regclass) then {F("x || ': RLS aus'")} end if;
    if exists (select 1 from pg_policy where polrelid = x::regclass) then {F("x || ': hat eine Policy'")} end if;
    if has_table_privilege('anon', x, 'select') or has_table_privilege('authenticated', x, 'select') or has_table_privilege('authenticated', x, 'insert') then {F("x || ': App-Rollen haben Rechte'")} end if;
  end loop;
  for x in select unnest(array[{', '.join(repr(f) for f in NEU)}]) loop
    if has_function_privilege('anon', x, 'execute') or has_function_privilege('authenticated', x, 'execute') then {F("x || ': für App-Rollen aufrufbar'")} end if;
  end loop;
  for x in select unnest(array['api.schule_wackelt_analyse(text, jsonb)', 'api.schule_fehler_abhaken(text, jsonb)', 'api.schule_nachueben_schicken(text, jsonb)']) loop
    if position('if not schule.ist_leiter(p_schluessel) then raise exception' in pg_get_functiondef(x::regprocedure)) = 0 then {F("x || ': prüft ist_leiter nicht'")} end if;
  end loop;
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
  begin
    perform pg_temp.ww_ant(k, a1.id, '987654', 'ww-1');
    perform pg_temp.ww_ant(k, a2.id, '987654', 'ww-2');
    select id into v1 from schule.versuch where lernender_id = k and client_id = 'ww-1';
    select id into v2 from schule.versuch where lernender_id = k and client_id = 'ww-2';
    r := schule.wackelt_analyse(k, 14, true);
    if not (array[v1, v2] <@ pg_temp.ww_ids(r, 'offen')) then {F("'Analyse: falsche Antworten nicht offen: ' || left(r::text, 300)")} end if;
    if (select e->'aufgabe'->'loesung' is null or e->>'lernziel' is distinct from v_lz or e->>'tag' is null from jsonb_array_elements(r->'offen') e where (e->>'versuch_id')::bigint = v1) then
      {F("'Analyse: Eintrag unvollständig'")} end if;
    if not exists (select 1 from jsonb_array_elements(r->'auswertung'->'themen') t where (t->>'offen')::int >= 2) then {F("'Auswertung je Thema fehlt'")} end if;
    if jsonb_array_length(r->'auswertung'->'lerntage') = 0 then {F("'Lerntage fehlen'")} end if;
    bericht := bericht || jsonb_build_object('mit_fehlbild', r->'mit_fehlbild', 'offen_zahl', r->'offen_zahl',
                 'beispiel', (select e - 'aufgabe' - 'antwort' from jsonb_array_elements(r->'offen') e where (e->>'versuch_id')::bigint = v1));
    -- Abhaken, zweimal, Rückgängig, fremde Versuche
    r := schule.fehler_abhaken(k, jsonb_build_array(v1), false, 'probe');
    if (r->>'geaendert')::int <> 1 then {F("'Abhaken: ' || r::text")} end if;
    if (schule.fehler_abhaken(k, jsonb_build_array(v1), false, 'probe')->>'geaendert')::int <> 0 then {F("'zweites Abhaken ändert etwas'")} end if;
    r := schule.wackelt_analyse(k, 14, true);
    if v1 = any(pg_temp.ww_ids(r, 'offen')) or not v1 = any(pg_temp.ww_ids(r, 'erledigt')) then {F("'abgehakte Antwort noch offen oder nicht erledigt'")} end if;
    if (schule.fehler_abhaken(k, jsonb_build_array(v1), true, 'probe')->>'geaendert')::int <> 1 then {F("'Rückgängig ändert nichts'")} end if;
    if not v1 = any(pg_temp.ww_ids(schule.wackelt_analyse(k, 14, false), 'offen')) then {F("'nach Rückgängig nicht wieder offen'")} end if;
    r := schule.fehler_abhaken(k, jsonb_build_array(0, (select min(id) from schule.versuch where lernender_id <> k)), false, 'probe');
    if (r->>'geaendert')::int <> 0 or jsonb_array_length(r->'uebersprungen') = 0 then {F("'fremde Versuche abgehakt: ' || r::text")} end if;
    -- Nachüben
    r := schule.nachueben_schicken(k, jsonb_build_array(v2), false, 'probe');
    select * into b from schule.aufgabe where id = (r->'geschickt'->0->>'aufgabe_id')::bigint;
    if b.id is null or b.id = a2.id or b.einheit_id <> v_e or b.variante_gruppe <> v_lz then {F("'Nachüben: falsche Aufgabe: ' || r::text")} end if;
    if (schule.nachueben_schicken(k, jsonb_build_array(v2), false, 'probe')->'uebersprungen'->0->>'grund') is distinct from 'liegt schon bereit' then {F("'zweites Schicken nicht erkannt'")} end if;
    r := schule.nachueben_liste(k);
    if jsonb_array_length(r) <> 1 or (r->0->'aufgabe'->>'id')::bigint <> b.id or r->0->'aufgabe' ? 'loesung' or r->0->'aufgabe' ? 'loesungsweg' then {F("'Liste fürs Kind: ' || r::text")} end if;
    if (select e->'nachueben' is null from jsonb_array_elements(schule.wackelt_analyse(k, 14, false)->'offen') e where (e->>'versuch_id')::bigint = v2) then {F("'Analyse zeigt Nachüben nicht'")} end if;
    perform pg_temp.ww_ant(k, b.id, replace(b.loesung->>'wert', '.', ','), 'ww-3');
    r := schule.wackelt_analyse(k, 14, true);
    if v2 = any(pg_temp.ww_ids(r, 'offen')) then {F("'nachgeübte Antwort noch offen'")} end if;
    if (select e->'erledigt'->>'art' from jsonb_array_elements(r->'erledigt') e where (e->>'versuch_id')::bigint = v2) is distinct from 'nachgeuebt' then {F("'nachgeübt nicht unter erledigt'")} end if;
    if jsonb_array_length(schule.nachueben_liste(k)) <> 0 then {F("'Liste fürs Kind nach dem Nachüben nicht leer'")} end if;
    raise exception using errcode = 'WW999', message = 'zurueck';
  exception when sqlstate 'WW999' then null;
    when others then {F("'Prüfblock: ' || sqlerrm")}
  end;
  if exists (select 1 from schule.fehler_erledigt) or exists (select 1 from schule.nachueben) then {F("'neue Tabellen nicht leer'")} end if;
  if (select (n, m) is distinct from ((select count(*) from schule.versuch), (select coalesce(max(id), 0) from schule.versuch)) from ww_stand) then {F("'Versuche verändert'")} end if;
  bericht := bericht || jsonb_build_object('fehler', coalesce(array_length(fehler, 1), 0));
  if array_length(fehler, 1) > 0 then raise exception 'WW-S ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
  {ende}
end $p$;""")


if __name__ == '__main__':
    main()
