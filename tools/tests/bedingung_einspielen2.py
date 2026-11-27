"""Einspiel-Paket für BD-S2 (Antworttyp „bedingung“, Teil 2: Schutz der Prüf-Bäume und Öffnung) – prüft sich selbst.

EIN SQL für EINEN Aufruf (eine Sitzung, eine Transaktion). Bei der kleinsten Abweichung: Ausnahme -> alles zurück.
Ablauf:
  1. Vorher-Stand: Definition und Rechte der sechs Ausgaben; die Übung für eine Aufgabe eines alten Typs mit dem Testkind
     (erster Fehlversuch, zweiter Fehlversuch, wiederholte Übertragung, richtig) – je in einer Untertransaktion, die zurückgerollt wird.
  2. Migration ausführen, dann vollständig noch einmal.
  3. Prüfblock:
     · zweiter Lauf ändert nichts; Rechte der sechs Funktionen unverändert; in keiner Funktion der Schemas schule und api wird die
       rohe Lösung noch gesendet; genau sechs Funktionen nutzen schule.loesung_sicht
     · Mischstand wird abgewiesen, Gegenprobe (alte Definitionen -> Einbau) ergibt exakt die neuen Definitionen
     · alter Typ: die vier Antworten der Übung sind nach der Migration Zeichen für Zeichen dieselben wie vorher
     · neuer Typ, mit dem Testkind an einer nur in der Untertransaktion angelegten Aufgabe, deren Prüf-Baum eine Merkzahl enthält:
       Anzeige, erster Fehlversuch, wiederholte Übertragung, zweiter Fehlversuch, wiederholte endgültige Antwort, Formatfehler,
       richtig, Knobel-Aufgabe. Erwartete Felder geprüft; in KEINER Antwort stehen Merkzahl, „pruefe“, „zeige“, „gut“, „gegenbeispiele“
     · Versionsschutz: Änderung einer Aufgabe mit Versuch wird abgewiesen
     · Constraints: neuer Typ zugelassen; unzulässige Aufgabe scheitert an aufgabe_bedingung_gueltig
     · Rechte: App-Rollen können schule.loesung_sicht nicht direkt aufrufen
     · Laufzeit in drei Fällen, diesmal mit Variablen (die Messung aus Teil 1 mit festen Werten war beim dritten Fall ungültig)
Nicht dynamisch geprüft (nur an der Definition): test_abschliessen_intern, expeditionen_kind, expeditionen_alle, api.schule_lernstand,
api.schule_inhalt_lesen – sie brauchen eine Testsitzung, eine Expedition oder einen Zugangsschlüssel.

Aufruf:  python3 -I tools/tests/bedingung_einspielen2.py > einspielen2.sql
Nicht ohne den ausdrücklichen Satz des Nutzers ausführen. Vorher: werkstatt_sperre. Nachher: werkstatt_aenderung.
"""
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
sys.path.insert(0, str(HIER.parent))
import bedingung  # noqa: E402
import bedingung_sql_test as T  # noqa: E402
import bedingung_einspielen as E  # noqa: E402

MIG = HIER.parent.parent / 'supabase/migrations/20261202_bd_s2_bedingung_ausgabe.sql'
MERK = 987123
SECHS = ['schule.uebung_pruefen_intern(bigint, jsonb)', 'schule.test_abschliessen_intern(bigint, jsonb)', 'schule.expeditionen_kind(bigint)',
         'schule.expeditionen_alle()', 'api.schule_lernstand(text, jsonb)', 'api.schule_inhalt_lesen(text, jsonb)']
PROBE = {'f': {'text': 'Nenne drei verschiedene ganze Zahlen mit der Summe 0.', 'felder': [{'art': 'ganz'}] * 3},
         'o': {'bedingungen': [
             {'name': 'drei verschiedene Zahlen', 'pruefe': ['verschieden', '$alle'], 'hinweis': 'Die drei Zahlen sollen verschieden sein.'},
             {'name': 'Summe ist 0', 'pruefe': ['=', ['summe', '$alle'], ['-', MERK, MERK]], 'zeige': ['summe', '$alle'], 'hinweis': 'Deine Summe ist {}.'}],
             'beispiel': [5, -2, -3], 'gut': [[1, 0, -1]], 'gegenbeispiele': [{'werte': [4, -1, -2], 'verletzt': 'Summe ist 0'}, {'werte': [0, 0, 0], 'verletzt': 'drei verschiedene Zahlen'}]}}
SPALTEN = 'einheit_id, thema_id, teilfaehigkeit, art, stufe, variante_gruppe, antworttyp, frage, antworten, loesung, tipp, loesungsweg, punkte_max, reihenfolge, pool, freigegeben, typ, expedition_id, teil'


def main():
    assert not bedingung.pruefe_aufgabe(PROBE), bedingung.pruefe_aufgabe(PROBE)
    assert bedingung.bewerte(PROBE, {'werte': [4, -1, -2]}) == {'format_ok': True, 'richtig': False, 'verletzt': 'Summe ist 0', 'hinweis': 'Deine Summe ist 1.'}
    mig = MIG.read_text(encoding='utf-8')
    for marke in ('$b2mig$', '$b2patch$', '$b2alt$', '$pruef$', '$x$'):
        assert marke not in mig
    i = mig.index('do $$', mig.index('-- Text-Patches.'))
    patch = mig[i:mig.index('end $$;', i) + len('end $$;')]
    assert 'zaehle' in patch
    lit = lambda v: "'" + bedingung.schreibe_json(v).replace("'", "''") + "'::jsonb"
    feld = lambda sp, **neu: ', '.join(neu.get(s, s) for s in SPALTEN.split(', '))
    neu = dict(antworttyp="'bedingung'", frage='v_frage', antworten='null', loesung='v_loesung', tipp='null', loesungsweg="'Probe-Aufgabe des Einspiel-Pakets'", freigegeben='true')
    teuer, tp = T.teuer(), E.teuer_potenz()
    sechs = 'array[' + ', '.join(f"'{f}'" for f in SECHS) + ']'
    print(f"""-- BD-S2 Einspiel-Paket (erzeugt von tools/tests/bedingung_einspielen2.py). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);
create temp table b2_mig on commit drop as select $b2mig${mig}$b2mig$::text as sql, $b2patch${patch}$b2patch$::text as patch,
$b2alt$do $x$
declare k bigint := (select id from schule.lernender where ist_test order by id limit 1); a schule.aufgabe; r1 jsonb; r2 jsonb; r3 jsonb; r4 jsonb;
  falsch constant jsonb := '{{"wert":"987654"}}'; richtig jsonb;
begin
  select * into a from schule.aufgabe where id = (select min(id) from schule.aufgabe where pool = 'uebung' and antworttyp = 'zahl' and freigegeben);
  if k is null or a.id is null then raise exception 'BD-S2: Testkind oder Vergleichsaufgabe fehlt'; end if;
  richtig := jsonb_build_object('wert', replace(a.loesung->>'wert', '.', ','));
  begin
    r1 := schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', a.id, 'antwort', falsch, 'client_id', 'b2-alt-1', 'anlauf', 1));
    r2 := schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', a.id, 'antwort', falsch, 'client_id', 'b2-alt-2', 'anlauf', 2));
    r3 := schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', a.id, 'antwort', falsch, 'client_id', 'b2-alt-1', 'anlauf', 1));
    raise exception using errcode = 'BD999', message = 'zurueck';
  exception when sqlstate 'BD999' then null;
  end;
  begin
    r4 := schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', a.id, 'antwort', richtig, 'client_id', 'b2-alt-3', 'anlauf', 1));
    raise exception using errcode = 'BD999', message = 'zurueck';
  exception when sqlstate 'BD999' then null;
  end;
  insert into b2_aus values ('PHASE', 'falsch-1', r1), ('PHASE', 'falsch-2', r2), ('PHASE', 'wiederholt', r3), ('PHASE', 'richtig', r4);
end $x$;$b2alt$::text as alt;
create temp table b2_aus (phase text, schritt text, r jsonb) on commit drop;
create temp table b2_vor on commit drop as
  select f, pg_get_functiondef(to_regprocedure(f)) as def, (select proacl::text from pg_proc where oid = to_regprocedure(f)) as acl from unnest({sechs}) f;
do $$ begin execute replace((select alt from b2_mig), 'PHASE', 'vor'); end $$;
do $$ begin execute (select sql from b2_mig); end $$;
create temp table b2_nach1 on commit drop as
  select f, pg_get_functiondef(to_regprocedure(f)) as def, (select proacl::text from pg_proc where oid = to_regprocedure(f)) as acl from unnest({sechs}) f;
do $$ begin execute (select sql from b2_mig); end $$;
do $$ begin execute replace((select alt from b2_mig), 'PHASE', 'nach'); end $$;
create temp table b2_bericht on commit drop as select null::jsonb as b where false;

-- Prüfblock
do $pruef$
declare
  fehler text[] := '{{}}'; f record; n int; v_txt text; v_c text; v_id bigint; a schule.aufgabe; i int;
  k constant bigint := (select id from schule.lernender where ist_test order by id limit 1);
  v_basis constant bigint := (select min(id) from schule.aufgabe where pool = 'uebung' and antworttyp = 'zahl' and freigegeben);
  v_frage constant jsonb := {lit(PROBE['f'])};
  v_loesung constant jsonb := {lit(PROBE['o'])};
  v_sicht constant jsonb := {lit({'beispiel': PROBE['o']['beispiel'], 'bedingungen': [b['name'] for b in PROBE['o']['bedingungen']]})};
  falsch constant jsonb := '{{"werte":["4","-1","-2"]}}'; richtig constant jsonb := '{{"werte":["5","−2","-3"]}}';
  o jsonb := '{{}}'; v_schutz text; v_rolle text; v_gesperrt text[] := '{{}}'; v_misch text[] := '{{}}'; v_patch text := (select patch from b2_mig);
  v_f jsonb; v_b jsonb; v_a jsonb; v_r jsonb; t0 timestamptz; ms numeric[] := '{{}}';
  geheim constant text[] := array['{MERK}', '"pruefe"', '"zeige"', '"gegenbeispiele"', '"gut"'];
begin
  -- 1. Zweiter Lauf ändert nichts, Rechte unverändert, alle sechs geändert
  for f in select v.f, v.def as vor, v.acl as acl_vor, n1.def as nach1, n1.acl as acl1, pg_get_functiondef(to_regprocedure(v.f)) as jetzt,
                  (select proacl::text from pg_proc where oid = to_regprocedure(v.f)) as acl_jetzt from b2_vor v join b2_nach1 n1 using (f) loop
    if f.vor = f.nach1 then fehler := fehler || (f.f || ': erster Lauf hat nichts geändert')::text; end if;
    if f.nach1 is distinct from f.jetzt then fehler := fehler || (f.f || ': zweiter Lauf hat die Definition geändert')::text; end if;
    if f.acl_vor is distinct from f.acl_jetzt or f.acl1 is distinct from f.acl_jetzt then fehler := fehler || (f.f || ': Rechte geändert')::text; end if;
    if position('schule.loesung_sicht(a)' in f.jetzt) = 0 then fehler := fehler || (f.f || ': nutzt loesung_sicht nicht')::text; end if;
  end loop;
  select count(*), string_agg(s.nspname || '.' || p.proname, ', ') into n, v_txt from pg_proc p join pg_namespace s on s.oid = p.pronamespace
   where s.nspname in ('schule', 'api') and p.prosrc like '%''loesung'', a.loesung%';
  if n <> 0 then fehler := fehler || ('rohe Lösung wird noch gesendet in: ' || v_txt)::text; end if;
  select count(*) into n from pg_proc p join pg_namespace s on s.oid = p.pronamespace where s.nspname in ('schule', 'api') and p.prosrc like '%loesung_sicht(%' and p.proname <> 'loesung_sicht';
  if n <> 6 then fehler := fehler || ('loesung_sicht wird von ' || n || ' statt 6 Funktionen genutzt')::text; end if;

  -- 2. Mischstand (eine der fünf Stellen der Übung zurückgedreht) muss abgewiesen werden; Gegenprobe: alte Definitionen -> Einbau ergibt die neuen
  begin
    execute regexp_replace((select jetzt.def from (select pg_get_functiondef(to_regprocedure('{SECHS[0]}')) as def) jetzt), '''richtig'', v_alt\\.richtig, ''loesung'', schule\\.loesung_sicht\\(a\\)', '''richtig'', v_alt.richtig, ''loesung'', a.loesung');
    execute v_patch;
    raise exception using errcode = 'BD999', message = 'kein-abbruch';
  exception
    when sqlstate 'BD999' then fehler := fehler || 'Mischstand wurde nicht abgewiesen'::text;
    when others then if sqlerrm like 'BD-S2:%' then v_misch := v_misch || 'Mischstand abgewiesen'::text; else fehler := fehler || ('Mischstand unerwartet: ' || sqlerrm)::text; end if;
  end;
  begin
    for f in select v.def from b2_vor v loop execute f.def; end loop;
    execute v_patch;
    select count(*) into n from b2_nach1 n1 where pg_get_functiondef(to_regprocedure(n1.f)) is distinct from n1.def;
    raise exception using errcode = 'BD999', message = case when n = 0 then 'gegenprobe-ok' else 'gegenprobe-falsch' end;
  exception
    when sqlstate 'BD999' then if sqlerrm = 'gegenprobe-ok' then v_misch := v_misch || 'Gegenprobe ok'::text; else fehler := fehler || 'Gegenprobe: Einbau aus dem alten Stand ergibt nicht die neuen Definitionen'::text; end if;
    when others then fehler := fehler || ('Gegenprobe unerwartet: ' || sqlerrm)::text;
  end;
  select count(*) into n from b2_nach1 n1 where pg_get_functiondef(to_regprocedure(n1.f)) is distinct from n1.def;
  if n <> 0 then fehler := fehler || 'nach den Proben sind die Definitionen nicht wieder die neuen'::text; end if;

  -- 3. Alter Typ: die Übung antwortet Zeichen für Zeichen wie vorher
  select count(*), string_agg(v.schritt, ', ') into n, v_txt from b2_aus v join b2_aus w on w.schritt = v.schritt and w.phase = 'nach' where v.phase = 'vor' and v.r is distinct from w.r;
  if n <> 0 then fehler := fehler || ('alter Typ antwortet anders bei: ' || v_txt)::text; end if;
  if (select count(*) from b2_aus where r is not null) <> 8 then fehler := fehler || 'Vorher-Nachher-Vergleich unvollständig'::text; end if;

  -- 4. Neuer Typ mit dem Testkind, an einer Aufgabe, die nur in dieser Untertransaktion existiert
  begin
    insert into schule.aufgabe ({SPALTEN}) select {feld(SPALTEN, **neu)} from schule.aufgabe where id = v_basis returning id into v_id;
    select * into a from schule.aufgabe where id = v_id;
    o := o || jsonb_build_object('anzeige', schule.aufgabe_anzeige(a, true), 'sicht', schule.loesung_sicht(a),
      'falsch1', schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', v_id, 'antwort', falsch, 'client_id', 'b2-neu-1', 'anlauf', 1)));
    o := o || jsonb_build_object('wiederholt1', schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', v_id, 'antwort', falsch, 'client_id', 'b2-neu-1', 'anlauf', 1)),
      'format', schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', v_id, 'antwort', '{{"werte":["a","1","2"]}}'::jsonb, 'client_id', 'b2-neu-f', 'anlauf', 2)),
      'falsch2', schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', v_id, 'antwort', falsch, 'client_id', 'b2-neu-2', 'anlauf', 2)));
    o := o || jsonb_build_object('wiederholt2', schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', v_id, 'antwort', falsch, 'client_id', 'b2-neu-2', 'anlauf', 2)));
    begin
      update schule.aufgabe set loesung = jsonb_set(loesung, '{{beispiel}}', '[1,0,-1]'::jsonb) where id = v_id;
      v_schutz := 'nicht abgewiesen';
    exception when others then v_schutz := sqlerrm;
    end;
    raise exception using errcode = 'BD999', message = 'zurueck';
  exception
    when sqlstate 'BD999' then null;
    when others then fehler := fehler || ('neuer Typ, Fehlversuche: ' || sqlerrm)::text;
  end;
  begin
    insert into schule.aufgabe ({SPALTEN}) select {feld(SPALTEN, **neu)} from schule.aufgabe where id = v_basis returning id into v_id;
    o := o || jsonb_build_object('richtig', schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', v_id, 'antwort', richtig, 'client_id', 'b2-neu-3', 'anlauf', 1)));
    raise exception using errcode = 'BD999', message = 'zurueck';
  exception
    when sqlstate 'BD999' then null;
    when others then fehler := fehler || ('neuer Typ, richtig: ' || sqlerrm)::text;
  end;
  begin
    insert into schule.aufgabe ({SPALTEN}) select {feld(SPALTEN, **dict(neu, pool="'bonus'", typ="'knobel'", stufe='3'))} from schule.aufgabe where id = v_basis returning id into v_id;
    o := o || jsonb_build_object('knobel', schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', v_id, 'antwort', falsch, 'client_id', 'b2-neu-4')));
    raise exception using errcode = 'BD999', message = 'zurueck';
  exception
    when sqlstate 'BD999' then null;
    when others then fehler := fehler || ('neuer Typ, Knobel: ' || sqlerrm)::text;
  end;
  if (select count(*) from jsonb_object_keys(o)) <> 9 then fehler := fehler || ('neuer Typ: nur ' || (select count(*) from jsonb_object_keys(o)) || ' von 9 Antworten')::text;
  else
    foreach v_txt in array geheim loop
      if position(v_txt in o::text) > 0 then fehler := fehler || ('GEHEIMES in einer Antwort: ' || v_txt || ' in ' || (select string_agg(key, ', ') from jsonb_each(o) where position(v_txt in value::text) > 0))::text; end if;
    end loop;
    if o->'sicht' is distinct from v_sicht then fehler := fehler || ('loesung_sicht liefert ' || (o->'sicht')::text)::text; end if;
    if o->'anzeige'->'frage' is distinct from v_frage then fehler := fehler || 'Anzeige: Frage mit Feldern fehlt oder weicht ab'::text; end if;
    if not (o->'falsch1' @> '{{"format_ok":true,"richtig":false,"nochmal":true,"verletzt":"Summe ist 0","hinweis":"Deine Summe ist 1."}}'::jsonb) or o->'falsch1' ? 'loesung'
      then fehler := fehler || ('erster Fehlversuch: ' || (o->'falsch1')::text)::text; end if;
    if not (o->'wiederholt1' @> '{{"nochmal":true,"wiederholt":true,"verletzt":"Summe ist 0","hinweis":"Deine Summe ist 1."}}'::jsonb) or o->'wiederholt1' ? 'loesung'
      then fehler := fehler || ('wiederholter erster Fehlversuch: ' || (o->'wiederholt1')::text)::text; end if;
    if not (o->'format' @> '{{"format_ok":false}}'::jsonb) or o->'format' ? 'loesung' or coalesce(o->'format'->>'hinweis', '') = '' then fehler := fehler || ('Formatfehler: ' || (o->'format')::text)::text; end if;
    if not (o->'falsch2' @> '{{"format_ok":true,"richtig":false,"verletzt":"Summe ist 0","hinweis":"Deine Summe ist 1."}}'::jsonb) or o->'falsch2'->'loesung' is distinct from v_sicht or o->'falsch2' ? 'nochmal'
      then fehler := fehler || ('zweiter Fehlversuch: ' || left((o->'falsch2')::text, 300))::text; end if;
    if not (o->'wiederholt2' @> '{{"richtig":false,"wiederholt":true}}'::jsonb) or o->'wiederholt2'->'loesung' is distinct from v_sicht then fehler := fehler || ('wiederholte endgültige Antwort: ' || left((o->'wiederholt2')::text, 300))::text; end if;
    if not (o->'richtig' @> '{{"format_ok":true,"richtig":true}}'::jsonb) or o->'richtig'->'loesung' is distinct from v_sicht or o->'richtig' ? 'verletzt' then fehler := fehler || ('richtig: ' || left((o->'richtig')::text, 300))::text; end if;
    if not (o->'knobel' @> '{{"richtig":false,"bonus":true,"verletzt":"Summe ist 0"}}'::jsonb) or o->'knobel'->'loesung' is distinct from v_sicht then fehler := fehler || ('Knobel: ' || left((o->'knobel')::text, 300))::text; end if;
  end if;
  if v_schutz is null or v_schutz not like '%hat schon Versuche%' then fehler := fehler || ('Versionsschutz: ' || coalesce(v_schutz, 'nicht geprüft'))::text; end if;

  -- 5. Constraints: neuer Typ zugelassen (siehe 4), unzulässige Aufgabe scheitert an aufgabe_bedingung_gueltig
  if (select pg_get_constraintdef(oid) from pg_constraint where conname = 'aufgabe_antworttyp_check' and conrelid = 'schule.aufgabe'::regclass) not like '%bedingung%'
     or not exists (select 1 from pg_constraint where conname = 'aufgabe_bedingung_gueltig' and conrelid = 'schule.aufgabe'::regclass and convalidated)
    then fehler := fehler || 'Constraints nicht wie erwartet'::text; end if;
  begin
    insert into schule.aufgabe ({SPALTEN}) select {feld(SPALTEN, **dict(neu, loesung="jsonb_set(v_loesung, '{bedingungen,0,pruefe}', '[\"wurzel\",\"$1\"]'::jsonb)"))} from schule.aufgabe where id = v_basis;
    raise exception using errcode = 'BD999', message = 'offen';
  exception
    when check_violation then get stacked diagnostics v_c = constraint_name;
      if v_c <> 'aufgabe_bedingung_gueltig' then fehler := fehler || ('unzulässige Aufgabe scheitert an ' || v_c)::text; else v_c := 'abgewiesen'; end if;
    when sqlstate 'BD999' then fehler := fehler || 'unzulässige Aufgabe wurde angenommen'::text;
    when others then fehler := fehler || ('Probe unzulässige Aufgabe unerwartet: ' || sqlerrm)::text;
  end;
  if v_c is distinct from 'abgewiesen' and not exists (select 1 from unnest(fehler) x where x like 'unzulässige Aufgabe%' or x like 'Probe unzulässige%') then fehler := fehler || 'Probe unzulässige Aufgabe ohne Ergebnis'::text; end if;

  -- 6. Rechte: App-Rollen können loesung_sicht nicht direkt aufrufen
  for v_rolle in select rolname from pg_roles where rolname in ('anon', 'authenticated', 'council_mcp', 'service_role') loop
    begin
      execute format('set local role %I', v_rolle);
      execute 'select schule.loesung_sicht(jsonb_populate_record(null::schule.aufgabe, $1))' into v_r using jsonb_build_object('antworttyp', 'bedingung', 'loesung', v_loesung);
      raise exception using errcode = 'BD999', message = 'darf';
    exception
      when insufficient_privilege then v_gesperrt := v_gesperrt || v_rolle;
      when sqlstate 'BD999' then fehler := fehler || (v_rolle || ' kann schule.loesung_sicht direkt aufrufen')::text;
      when others then fehler := fehler || ('Rechteprobe als ' || v_rolle || ' unerwartet: ' || sqlerrm)::text;
    end;
  end loop;

  -- 7. Laufzeit (Mittel aus 200), alle Argumente als Variablen, damit wirklich 200 Mal gerechnet wird
  for i in 1 .. 3 loop
    if i = 1 then v_f := {lit(teuer['f']['felder'])}; v_b := {lit(teuer['o']['bedingungen'])}; v_a := {lit({'werte': T.MESS})};
    elsif i = 2 then v_a := {lit({'werte': E.GROSS})};
    else v_f := {lit(tp['f']['felder'])}; v_b := {lit(tp['o']['bedingungen'])}; v_a := {lit({'werte': E.POTENZ})};
    end if;
    t0 := clock_timestamp();
    for n in 1 .. 200 loop v_r := schule.bed_bewerten(v_f, v_b, v_a); end loop;
    ms := ms || round((extract(epoch from clock_timestamp() - t0) * 5)::numeric, 2);
  end loop;
  if v_r is distinct from '{{"format_ok":true,"richtig":false,"verletzt":"p8"}}'::jsonb then fehler := fehler || ('Messfall Potenz liefert ' || v_r::text)::text; end if;
  if ms[1] > 200 or ms[2] > 200 or ms[3] > 200 then fehler := fehler || ('zu langsam: ' || array_to_string(ms, ' / ') || ' ms')::text; end if;

  if array_length(fehler, 1) > 0 then raise exception 'BD-S2 ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
  insert into b2_bericht select jsonb_build_object('ergebnis', 'BD-S2 eingespielt, alle Prüfungen bestanden', 'proben', v_misch, 'alter_typ_gleich', 4,
    'neuer_typ_antworten', (select jsonb_agg(key) from jsonb_object_keys(o) key), 'erster_fehlversuch', o->'falsch1', 'loesung_fuer_das_kind', o->'sicht',
    'versionsschutz', v_schutz, 'unzulaessige_aufgabe', v_c, 'direktaufruf_gesperrt_fuer', v_gesperrt, 'ms_knoten_brueche_potenz', ms,
    'aufgaben_neuer_typ', (select count(*) from schule.aufgabe where antworttyp = 'bedingung'));
end $pruef$;
select b from b2_bericht;""")


if __name__ == '__main__':
    main()
