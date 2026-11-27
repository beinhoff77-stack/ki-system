"""Einspiel-Paket für RB-S (Regelbezug, Teil Datenbank) – prüft sich selbst. Muster: tools/tests/form_takt_einspielen.py.

EIN SQL für EINEN Aufruf (eine Sitzung, eine Transaktion). Bei der kleinsten Abweichung: Ausnahme -> alles zurück.
Ablauf:
  1. Vorher-Stand: Definition von uebung_pruefen_intern (md5), Prüfsummen über schule.aufgabe und schule.versuch, Antworten an einer bestehenden
     Übungsaufgabe (Typ zahl, freigegebene Einheit) mit dem Testkind: 1. Anlauf falsch, 2. Anlauf falsch, Wiederholung beider Übertragungen,
     richtig – alles in zurückgerollten Untertransaktionen.
  2. Migration ausführen, dann vollständig noch einmal.
  3. Prüfblock:
     · zweiter Lauf ändert nichts (Definitionen, Trigger, Indizes); Tabellen mit RLS und ohne Policy; anon/authenticated ohne Rechte an Tabellen und
       Funktionen; als Rolle authenticated ist Lesen der Fehlbilder verboten (Gegenprobe)
     · Bestand: ohne Daten antwortet dieselbe Übung Zeichen für Zeichen wie vorher (alle fünf Antworten)
     · mit Probe-Daten (zurückgerollt): 1. Anlauf mit Fehlbild-Antwort -> regelbezug nur {regel}; Versuch trägt fehlbild_nr/fehlbild;
       2. Anlauf -> volles Objekt mit Beschreibung; Wiederholung beider Übertragungen antwortet gleich; andere falsche Antwort -> nur regel, kein
       Fehlbild im Versuch; richtig -> kein regelbezug, Antwort wie vorher
     · Erkennen an Auswahl (Index) und Lücken (nur die erste falsche Lücke), richtige Antwort und Unsinn -> null, doppelter Schlüssel abgewiesen
     · Schutz: UPDATE/DELETE an Regel/Fehlbild einer freigegebenen Einheit scheitert; aufgabe_schutz greift weiter (UPDATE an schule.aufgabe scheitert)
     · nur die erwarteten Funktionen lesen die neuen Tabellen; aufgabe_anzeige zeigt keine Beschreibung (kein Weg, Fehlbilder vorab zu sehen)
     · Mischstand: halb umgestellte Funktion wird abgewiesen
     · am Ende: schule.aufgabe unverändert (md5), keine neuen Versuche, neue Tabellen leer
Ausgegeben werden nur Zählungen, Prüfsummen und Prüfergebnisse – keine Namen, keine Lerndaten.

Aufruf:  python3 -I tools/tests/regelbezug_einspielen.py > rb.sql               (Einspielung: Migration bleibt, wenn alles stimmt)
         python3 -I tools/tests/regelbezug_einspielen.py --probe > rb_probe.sql (Probelauf: am Ende wird ALLES zurückgerollt; Bericht in der Meldung)
Danach getrennt die Daten: python3 -I tools/regelbezug_sql.py --runden <R> --sql (je Runde).
Nicht ohne den ausdrücklichen Satz des Nutzers ausführen. Vorher: werkstatt_sperre. Nachher: werkstatt_aenderung. Nur in einer Nutzungspause
(schule.versuch ist bis zum Ende der Transaktion gesperrt).
"""
import sys
from pathlib import Path

MIG = Path(__file__).resolve().parent.parent.parent / 'supabase/migrations/20261204_rb_s_regelbezug.sql'
NEU = ['schule.regelbezug_schutz()', 'schule.fehlbild_finden(schule.aufgabe, jsonb)', 'schule.regelbezug_antwort(schule.aufgabe, jsonb, boolean, boolean)',
       'schule.versuch_fehlbild()', 'schule.versuch_regelbezug(schule.versuch)', 'schule.fehlbild_probeantwort(schule.aufgabe, text, integer, text)']
LESER = {'fehlbild_finden', 'regelbezug_antwort', 'versuch_fehlbild', 'versuch_regelbezug', 'regelbezug_schutz', 'uebung_pruefen_intern'}
A2_NEU = "'hinweis', b->>'hinweis', 'regelbezug', schule.regelbezug_antwort(a, p_daten->'antwort', false, false)));"
A2_ALT = "'hinweis', b->>'hinweis'));"


def F(msg):
    return f'fehler := fehler || ({msg})::text;'


def zurueck(name):
    return (f"    raise exception using errcode = 'RB999', message = 'zurueck';\n  exception\n    when sqlstate 'RB999' then null;\n"
            f"    when others then {F(chr(39) + name + ': ' + chr(39) + ' || sqlerrm')}\n  end;")


def main():
    probe = '--probe' in sys.argv[1:]
    mig = MIG.read_text(encoding='utf-8')
    for marke in ('$rbmig$', '$x$', '$f$', '$p$'):
        assert marke not in mig, marke
    assert mig.count(A2_NEU) == 1
    k = '(select id from schule.lernender where ist_test order by id limit 1)'
    basis = ("(select min(xa.id) from schule.aufgabe xa join schule.einheit xe on xe.id = xa.einheit_id where xa.pool = 'uebung' and xa.antworttyp = 'zahl' "
             "and xa.freigegeben and xe.status = 'freigegeben' and (xa.loesung->>'wert')::numeric <> 987654 and xa.loesung->>'einheit' is null)")
    basis_typ = lambda y: (f"(select min(xa.id) from schule.aufgabe xa join schule.einheit xe on xe.id = xa.einheit_id where xa.pool = 'uebung' and xa.antworttyp = '{y}' "
                           f"and xa.freigegeben and xe.status = 'freigegeben')")
    lauf = f"""do $x$
declare k bigint := {k}; a schule.aufgabe; o jsonb := '{{}}';
begin
  select * into a from schule.aufgabe where id = {basis};
  if k is null or a.id is null then raise exception 'RB-S: Testkind oder Vergleichsaufgabe fehlt'; end if;
  begin
    o := o || jsonb_build_object('falsch-1', pg_temp.rb_ant(k, a.id, '987654', 1, 'rb-p-1'));
    o := o || jsonb_build_object('falsch-1-wdh', pg_temp.rb_ant(k, a.id, '987654', 1, 'rb-p-1'));
    o := o || jsonb_build_object('falsch-2', pg_temp.rb_ant(k, a.id, '987654', 2, 'rb-p-2'));
    o := o || jsonb_build_object('falsch-2-wdh', pg_temp.rb_ant(k, a.id, '987654', 2, 'rb-p-2'));
    o := o || jsonb_build_object('anders', pg_temp.rb_ant(k, a.id, '123457', null, 'rb-p-3'));
    o := o || jsonb_build_object('versuche', (select jsonb_agg(jsonb_build_array(v.client_id, to_jsonb(v) -> 'fehlbild_nr', to_jsonb(v) -> 'fehlbild') order by v.id)
                                               from schule.versuch v where v.lernender_id = k and v.client_id like 'rb-p-%'));
    raise exception using errcode = 'RB999', message = 'zurueck';
  exception when sqlstate 'RB999' then null;
  end;
  begin
    o := o || jsonb_build_object('richtig', pg_temp.rb_ant(k, a.id, replace(a.loesung->>'wert', '.', ','), 1, 'rb-p-4'));
    raise exception using errcode = 'RB999', message = 'zurueck';
  exception when sqlstate 'RB999' then null;
  end;
  insert into rb_aus values ('PHASE', o);
end $x$;"""
    defs = "(select md5(string_agg(coalesce(pg_get_functiondef(to_regprocedure(f)), 'fehlt'), '#' order by f)) from unnest(array[" + \
        ', '.join(f"'{f}'" for f in NEU + ['schule.uebung_pruefen_intern(bigint, jsonb)']) + "]) f)"
    objekte = """(select md5(string_agg(s.x, '#' order by s.x)) from (
       select 'trg:' || tgrelid::regclass::text || ':' || tgname from pg_trigger where tgname in ('aufgabe_regel_schutz', 'aufgabe_fehlbild_schutz', 'versuch_fehlbild', 'aufgabe_schutz')
       union all select 'idx:' || indexrelid::regclass::text from pg_index where indrelid in ('schule.aufgabe_regel'::regclass, 'schule.aufgabe_fehlbild'::regclass)
       union all select 'con:' || conname || ':' || pg_get_constraintdef(oid) from pg_constraint where conrelid in ('schule.aufgabe_regel'::regclass, 'schule.aufgabe_fehlbild'::regclass)
       union all select 'col:' || attname || ':' || format_type(atttypid, atttypmod) || ':' || attnotnull from pg_attribute where attrelid = 'schule.versuch'::regclass and attname in ('fehlbild_nr', 'fehlbild') and not attisdropped) s(x))"""
    stand = ("(select md5(coalesce(string_agg(md5(ag::text), '' order by ag.id), '')) from schule.aufgabe ag), "
             "(select count(*) from schule.versuch), (select coalesce(max(id), 0) from schule.versuch)")
    ende = ("raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): %', (select b::text from rb_bericht);" if probe else
            "raise notice 'RB-S eingespielt: %', (select b::text from rb_bericht);")
    leser = ', '.join(f"'{x}'" for x in sorted(LESER))
    print(f"""-- RB-S Einspiel-Paket (erzeugt von tools/tests/regelbezug_einspielen.py{' --probe' if probe else ''}). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '180s', true);
create temp table rb_mig on commit drop as select $rbmig${mig}$rbmig$::text as sql, $rbmig${lauf}$rbmig$::text as lauf;
create function pg_temp.rb_ant(p_k bigint, p_id bigint, p_wert text, p_anlauf int, p_cid text) returns jsonb language plpgsql as $f$
begin
  return schule.uebung_pruefen_wd(p_k, jsonb_build_object('aufgabe_id', p_id, 'client_id', p_cid, 'antwort', jsonb_build_object('wert', p_wert))
         || case when p_anlauf is null then '{{}}'::jsonb else jsonb_build_object('anlauf', p_anlauf) end);
end $f$;
create temp table rb_aus (phase text, o jsonb) on commit drop;
create temp table rb_stand on commit drop as select row({stand})::text m;
do $p$ begin execute replace((select lauf from rb_mig), 'PHASE', 'vor'); end $p$;
do $p$ begin execute (select sql from rb_mig); end $p$;
create temp table rb_def on commit drop as select 1 lauf, {defs} d, {objekte} o;
do $p$ begin execute (select sql from rb_mig); end $p$;
insert into rb_def select 2, {defs}, {objekte};
do $p$ begin execute replace((select lauf from rb_mig), 'PHASE', 'nach'); end $p$;
create temp table rb_bericht (b jsonb) on commit drop;
do $p$
declare
  fehler text[] := '{{}}'; k bigint := {k}; a schule.aufgabe; aw schule.aufgabe; al schule.aufgabe; r jsonb; vor jsonb; nach jsonb; x text; n int; d text;
  bericht jsonb := '{{}}';
begin
  select * into a from schule.aufgabe where id = {basis};
  select * into aw from schule.aufgabe where id = {basis_typ('auswahl')};
  select * into al from schule.aufgabe where id = {basis_typ('luecken')};
  -- zweiter Lauf ändert nichts
  if (select count(distinct rb_def.d) from rb_def) <> 1 or (select count(distinct rb_def.o) from rb_def) <> 1 then {F("'zweiter Lauf hat Definitionen oder Objekte geändert'")} end if;
  if (select count(*) from pg_trigger where tgname in ('aufgabe_regel_schutz', 'aufgabe_fehlbild_schutz', 'versuch_fehlbild')) <> 3 then {F("'Trigger fehlen oder doppelt'")} end if;
  if (select count(*) from pg_trigger where tgrelid = 'schule.aufgabe'::regclass and tgname = 'aufgabe_schutz' and tgenabled <> 'D') <> 1 then {F("'aufgabe_schutz fehlt oder ist aus'")} end if;
  -- Rechte
  for x in select unnest(array['schule.aufgabe_regel', 'schule.aufgabe_fehlbild']) loop
    if not (select relrowsecurity from pg_class where oid = x::regclass) then {F("x || ': RLS aus'")} end if;
    if exists (select 1 from pg_policy where polrelid = x::regclass) then {F("x || ': hat eine Policy'")} end if;
    if has_table_privilege('anon', x, 'select') or has_table_privilege('authenticated', x, 'select') or has_table_privilege('authenticated', x, 'insert') then {F("x || ': App-Rollen haben Rechte'")} end if;
  end loop;
  for x in select unnest(array[{', '.join(repr(f) for f in NEU)}]) loop
    if has_function_privilege('anon', x, 'execute') or has_function_privilege('authenticated', x, 'execute') then {F("x || ': für App-Rollen aufrufbar'")} end if;
  end loop;
  begin
    execute 'set local role authenticated';
    perform count(*) from schule.aufgabe_fehlbild;
    {F("'authenticated kann schule.aufgabe_fehlbild lesen'")}
    raise exception using errcode = 'RB999', message = 'zurueck';
  exception when sqlstate 'RB999' then null; when insufficient_privilege then null;
    when others then {F("'Gegenprobe Rolle: ' || sqlerrm")}
  end;
  if current_user = 'authenticated' then {F("'Rolle nicht zurückgesetzt'")} end if;
  -- nur erwartete Funktionen lesen die neuen Tabellen / rufen die Rückmeldung
  for x in select p.oid::regprocedure::text from pg_proc p join pg_namespace s on s.oid = p.pronamespace
            where s.nspname not in ('pg_catalog', 'information_schema') and p.prokind = 'f'
              and (p.prosrc like '%aufgabe_fehlbild%' or p.prosrc like '%regelbezug_antwort%' or p.prosrc like '%fehlbild_finden%' or p.prosrc like '%versuch_regelbezug%')
              and p.proname not in ({leser}) and s.nspname <> 'pg_temp' and p.pronamespace <> pg_my_temp_schema() loop
    {F("'unerwarteter Leser der Fehlbilder: ' || x")}
  end loop;
  -- Bestand: ohne Daten gleiche Antworten
  select o into vor from rb_aus where phase = 'vor'; select o into nach from rb_aus where phase = 'nach';
  if vor - 'versuche' is distinct from nach - 'versuche' then {F("'Bestand antwortet anders: vor ' || (vor - 'versuche')::text || ' nach ' || (nach - 'versuche')::text")} end if;
  if exists (select 1 from jsonb_array_elements(nach->'versuche') v where v->1 <> 'null'::jsonb) then {F("'Versuch ohne Daten trägt ein Fehlbild'")} end if;
  bericht := bericht || jsonb_build_object('bestand_gleich', vor - 'versuche' = nach - 'versuche');
  -- mit Probe-Daten
  begin
    insert into schule.aufgabe_regel (aufgabe_id, regel) values (a.id, 'rr.waage');
    insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, wert, beschreibung, fehlbild, regel) values (a.id, 2, 'zahl', '987654', 'RB-Probe Beschreibung', 'fb.probe.eins', 'rr.plusminus');
    begin   -- richtig (eigene Untertransaktion, damit die Karte wie im Vorher-Lauf steht)
      r := pg_temp.rb_ant(k, a.id, replace(a.loesung->>'wert', '.', ','), 1, 'rb-q-4');
      if r ? 'regelbezug' or r is distinct from (select o->'richtig' from rb_aus where phase = 'vor') then {F("'richtig: ' || r::text")} end if;
      raise exception using errcode = 'RB999', message = 'zurueck';
    exception when sqlstate 'RB999' then null;
    end;
    r := pg_temp.rb_ant(k, a.id, '987654', 1, 'rb-q-1');
    if r->'regelbezug' is distinct from '{{"regel": "rr.waage"}}'::jsonb or r->>'nochmal' is distinct from 'true' then {F("'1. Anlauf: ' || r::text")} end if;
    if (select (v.fehlbild_nr, v.fehlbild) is distinct from (2::smallint, 'fb.probe.eins') from schule.versuch v where v.lernender_id = k and v.client_id = 'rb-q-1') then {F("'1. Anlauf: Fehlbild nicht im Versuch'")} end if;
    r := pg_temp.rb_ant(k, a.id, '987654', 1, 'rb-q-1');
    if r->'regelbezug' is distinct from '{{"regel": "rr.waage"}}'::jsonb then {F("'Wiederholung 1. Anlauf: ' || r::text")} end if;
    r := pg_temp.rb_ant(k, a.id, '987 654', 2, 'rb-q-2');
    if r->'regelbezug' is distinct from '{{"regel": "rr.waage", "fehlbild": "fb.probe.eins", "fehlbild_nr": 2, "fehlbild_regel": "rr.plusminus", "text": "RB-Probe Beschreibung"}}'::jsonb
       or r->'loesung' is null then {F("'2. Anlauf: ' || r::text")} end if;
    bericht := bericht || jsonb_build_object('beispiel_antwort', r - 'loesung' - 'loesungsweg' - 'karte');
    if pg_temp.rb_ant(k, a.id, '987654', 2, 'rb-q-2')->'regelbezug' is distinct from r->'regelbezug' then {F("'Wiederholung 2. Anlauf antwortet anders'")} end if;
    r := pg_temp.rb_ant(k, a.id, '123457', null, 'rb-q-3');
    if r->'regelbezug' is distinct from '{{"regel": "rr.waage"}}'::jsonb then {F("'andere falsche Antwort: ' || r::text")} end if;
    if (select v.fehlbild_nr from schule.versuch v where v.lernender_id = k and v.client_id = 'rb-q-3') is not null then {F("'andere falsche Antwort: Fehlbild im Versuch'")} end if;
    if (select schule.versuch_regelbezug(v) from schule.versuch v where v.lernender_id = k and v.client_id = 'rb-q-2') is distinct from r->'regelbezug' || '{{"fehlbild": "fb.probe.eins", "fehlbild_nr": 2, "fehlbild_regel": "rr.plusminus", "text": "RB-Probe Beschreibung"}}'::jsonb then
      {F("'versuch_regelbezug passt nicht'")} end if;
    if position('RB-Probe' in schule.aufgabe_anzeige(a, true)::text) > 0 then {F("'aufgabe_anzeige zeigt die Beschreibung'")} end if;
    -- doppelter Schlüssel
    begin
      insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, wert, beschreibung) values (a.id, 3, 'zahl', '987654', 'doppelt');
      {F("'doppelter Schlüssel angenommen'")}
    exception when unique_violation then null;
    end;
    -- Schutz
    begin update schule.aufgabe_fehlbild set beschreibung = beschreibung where aufgabe_id = a.id; {F("'UPDATE Fehlbild angenommen'")}
    exception when others then if position('unveränderlich' in sqlerrm) = 0 then {F("'UPDATE Fehlbild: ' || sqlerrm")} end if; end;
    begin delete from schule.aufgabe_regel where aufgabe_id = a.id; {F("'DELETE Regel angenommen'")}
    exception when others then if position('unveränderlich' in sqlerrm) = 0 then {F("'DELETE Regel: ' || sqlerrm")} end if; end;
    begin update schule.aufgabe set tipp = tipp where id = a.id; {F("'aufgabe_schutz greift nicht mehr'")}
    exception when others then if position('unveränderlich' in sqlerrm) = 0 then {F("'aufgabe_schutz: ' || sqlerrm")} end if; end;
    -- Auswahl
    if aw.id is not null then
      insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, wert, beschreibung) values (aw.id, 1, 'index', (((aw.loesung->>'index')::int + 1) % jsonb_array_length(aw.antworten))::text, 'RB-Probe Auswahl');
      if schule.fehlbild_finden(aw, jsonb_build_object('index', ((aw.loesung->>'index')::int + 1) % jsonb_array_length(aw.antworten))) is distinct from 1::smallint then {F("'Auswahl nicht erkannt'")} end if;
      if schule.fehlbild_finden(aw, jsonb_build_object('index', (aw.loesung->>'index')::int)) is not null then {F("'Auswahl: richtige Option erkannt'")} end if;
    end if;
    -- Lücken: nur die erste falsche Lücke
    if al.id is not null and jsonb_array_length(al.loesung->'werte') >= 2 then
      insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, luecke, wert, beschreibung) values (al.id, 1, 'luecke', 2, ((al.loesung->'werte'->>1)::numeric + 1)::text, 'RB-Probe Lücke');
      if schule.fehlbild_finden(al, schule.fehlbild_probeantwort(al, 'luecke', 2, ((al.loesung->'werte'->>1)::numeric + 1)::text)) is distinct from 1::smallint then {F("'Lücke 2 nicht erkannt'")} end if;
      if schule.fehlbild_finden(al, jsonb_set(schule.fehlbild_probeantwort(al, 'luecke', 2, ((al.loesung->'werte'->>1)::numeric + 1)::text), '{{werte,0}}', to_jsonb((al.loesung->'werte'->>0)::numeric + 7))) is not null then
        {F("'Lücke 2 erkannt, obwohl Lücke 1 schon falsch'")} end if;
      if schule.fehlbild_finden(al, jsonb_build_object('werte', al.loesung->'werte')) is not null then {F("'Lücken: richtige Antwort erkannt'")} end if;
    end if;
    -- Unsinn
    if schule.fehlbild_finden(a, '"x"'::jsonb) is not null or schule.fehlbild_finden(a, '{{"wert": "abc"}}') is not null or schule.fehlbild_finden(a, null) is not null then {F("'Unsinn erkannt'")} end if;
{zurueck('Probe-Daten')}
  -- Mischstand: eine Stelle zurückgebaut -> Migration muss abbrechen
  begin
    d := pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure);
    execute replace(d, $q${A2_NEU}$q$, $q${A2_ALT}$q$);
    begin
      execute (select sql from rb_mig);
      {F("'Mischstand nicht abgewiesen'")}
    exception when others then if position('halb umgestellt' in sqlerrm) = 0 then {F("'Mischstand: ' || sqlerrm")} end if;
    end;
{zurueck('Mischstand')}
  -- Ende: nichts an Aufgaben und Versuchen geändert, neue Tabellen leer
  if (select m from rb_stand) is distinct from (select row({stand})::text) then {F("'Aufgaben oder Versuche verändert'")} end if;
  if exists (select 1 from schule.aufgabe_regel) or exists (select 1 from schule.aufgabe_fehlbild) then {F("'neue Tabellen nicht leer'")} end if;
  bericht := bericht || jsonb_build_object('basis_aufgabe', a.id, 'auswahl', aw.id, 'luecken', al.id, 'fehler', coalesce(array_length(fehler, 1), 0));
  insert into rb_bericht values (bericht);
  if array_length(fehler, 1) > 0 then raise exception 'RB-S ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
  {ende}
end $p$;""")


if __name__ == '__main__':
    main()
