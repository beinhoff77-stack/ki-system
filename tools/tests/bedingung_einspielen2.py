"""Einspiel-Paket für BD-S2 (Antworttyp „bedingung“, Teil 2: Schutz der Prüf-Bäume und Öffnung) – prüft sich selbst.

EIN SQL für EINEN Aufruf (eine Sitzung, eine Transaktion). Bei der kleinsten Abweichung: Ausnahme -> alles zurück.
Ablauf:
  1. Vorher-Stand: Definition und Rechte der sechs Ausgaben; die Übung für eine Aufgabe eines alten Typs mit dem Testkind
     (erster Fehlversuch, zweiter Fehlversuch, beide wiederholt übertragen, richtig) – je in einer Untertransaktion, die zurückgerollt wird.
  2. Migration ausführen, dann vollständig noch einmal.
  3. Prüfblock:
     · zweiter Lauf ändert nichts; Rechte der sechs Funktionen unverändert; in keiner Funktion der Schemas schule und api wird die
       rohe Lösung noch gesendet; genau sechs Funktionen nutzen schule.loesung_sicht; die Menge ALLER Funktionen, in denen das Wort
       „loesung“ vorkommt, ist genau die erwartete (eine neue Funktion fällt auf)
     · Mischstand wird abgewiesen, Gegenprobe (alte Definitionen -> Einbau) ergibt exakt die neuen Definitionen
     · alter Typ: die fünf Antworten der Übung sind fachlich die erwarteten UND nach der Migration Zeichen für Zeichen dieselben
     · neuer Typ, mit dem Testkind an einer nur in der Untertransaktion angelegten Aufgabe, deren Prüf-Baum eine Merkzahl enthält:
       Anzeige (ohne „einheit“), erster Fehlversuch, wiederholte Übertragung, zweiter Fehlversuch, wiederholte endgültige Antwort
       (mit derselben Rückmeldung wie das Original), Formatfehler, richtig, Knobel-Aufgabe, client_id einer anderen Aufgabe (abgewiesen)
     · die fünf übrigen Ausgabewege, je ein gezielter Lauf in EINER zurückgerollten Konstellation (Testkind, Probe-Aufgaben,
       Testsitzung, Expedition im Entwurf, Lehrer-Zugang auf Zeit): laufender Test (nur Formatstatus), Test-Abschluss,
       Expedition beim Kind vor und nach dem Erledigen, Expeditionen gesamt, Lernstand, Inhalt. Jeweils erst der Nachweis, dass
       der erwartete Datensatz da ist, dann exakt die öffentliche Lösung, dann die ganze Antwort ohne Merkzahl und interne Felder
     · Versionsschutz: Änderung einer Aufgabe mit Versuch wird abgewiesen
     · Constraints: Typ-Liste exakt die Sollmenge; unzulässiger Baum und zusätzlicher Lösungsschlüssel („einheit“) scheitern
       an aufgabe_bedingung_gueltig
     · Rechte: App-Rollen können schule.loesung_sicht nicht direkt aufrufen (Rollenwechsel getrennt abgesichert)
     · Laufzeit in drei Fällen, mit Variablen
Textsuche nach Internem: Merkzahl, "pruefe", "zeige", "gegenbeispiele". „gut“ wird nicht als Text gesucht (das Wort kann in
anderen Daten vorkommen), sondern über die exakte Gleichheit jeder gesendeten Lösung mit der öffentlichen Fassung ausgeschlossen.

Aufruf:  python3 -I tools/tests/bedingung_einspielen2.py > einspielen2.sql            (Einspielung)
         python3 -I tools/tests/bedingung_einspielen2.py --probe > probelauf.sql       (Probelauf: alles läuft, am Ende wird
                                                                                        ALLES zurückgerollt; der Bericht steht in der Fehlermeldung)
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
TYP_SOLL = "CHECK ((antworttyp = ANY (ARRAY['auswahl'::text, 'zahl'::text, 'text'::text, 'markierung'::text, 'luecken'::text, 'bedingung'::text])))"
# alle Funktionen in schule und api, in denen das Wort „loesung“ vorkommt (27.11. gelesen: elf; dazu die zwei neuen dieser Migration)
LOESUNG_FUNKTIONEN = sorted(['api.schule_inhalt_lesen', 'api.schule_lernstand', 'schule.antwort_bewerten', 'schule.aufgabe_anzeige', 'schule.aufgabe_bedingung_schutz',
                             'schule.aufgaben_einfuegen', 'schule.einheit_abgleichen', 'schule.expedition_importieren', 'schule.expeditionen_alle', 'schule.expeditionen_kind',
                             'schule.loesung_sicht', 'schule.test_abschliessen_intern', 'schule.uebung_pruefen_intern'])
SECHS = ['schule.uebung_pruefen_intern(bigint, jsonb)', 'schule.test_abschliessen_intern(bigint, jsonb)', 'schule.expeditionen_kind(bigint)',
         'schule.expeditionen_alle()', 'api.schule_lernstand(text, jsonb)', 'api.schule_inhalt_lesen(text, jsonb)']
PROBE = {'f': {'text': 'Nenne drei verschiedene ganze Zahlen mit der Summe 0.', 'felder': [{'art': 'ganz'}] * 3},
         'o': {'bedingungen': [
             {'name': 'drei verschiedene Zahlen', 'pruefe': ['verschieden', '$alle'], 'hinweis': 'Die drei Zahlen sollen verschieden sein.'},
             {'name': 'Summe ist 0', 'pruefe': ['=', ['summe', '$alle'], ['-', MERK, MERK]], 'zeige': ['summe', '$alle'], 'hinweis': 'Deine Summe ist {}.'}],
             'beispiel': [5, -2, -3], 'gut': [[1, 0, -1]], 'gegenbeispiele': [{'werte': [4, -1, -2], 'verletzt': 'Summe ist 0'}, {'werte': [0, 0, 0], 'verletzt': 'drei verschiedene Zahlen'}]}}
SPALTEN = 'einheit_id, thema_id, teilfaehigkeit, art, stufe, variante_gruppe, antworttyp, frage, antworten, loesung, tipp, loesungsweg, punkte_max, reihenfolge, pool, freigegeben, typ, expedition_id, teil'


def main():
    probe = '--probe' in sys.argv[1:]
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
    fn_soll = 'array[' + ', '.join(f"'{f}'" for f in LOESUNG_FUNKTIONEN) + ']::text[]'
    typ_soll = "'" + TYP_SOLL.replace("'", "''") + "'"
    feld_baum = feld(SPALTEN, **dict(neu, loesung="jsonb_set(v_loesung, '{bedingungen,0,pruefe}', '[\"wurzel\",\"$1\"]'::jsonb)"))
    feld_einheit = feld(SPALTEN, **dict(neu, loesung="v_loesung || '{\"einheit\":\"cm\"}'::jsonb"))
    ende = ("raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): %', (select b::text from b2_bericht);" if probe else '')
    uebung = lambda aid, cid, antwort='falsch', extra='': f"schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', {aid}, 'antwort', {antwort}, 'client_id', '{cid}'{extra}))"
    teil = lambda quelle, aid: f"(select t from jsonb_array_elements({quelle}) x, jsonb_array_elements(x->'teile') t where (t->>'id')::bigint = {aid})"
    wege = f"""  -- 4b. Die fünf übrigen Ausgabewege: EINE Konstellation, die vollständig zurückgerollt wird
  begin
    select e.id, e.block_id, e.thema_id into v_einheit, v_block, v_thema from schule.aufgabe b join schule.einheit e on e.id = b.einheit_id where b.id = v_basis;
    -- Lehrer-Zugang auf Zeit (nur in dieser Untertransaktion; der Schlüssel wird nirgends ausgegeben)
    insert into schule.lern_login (name, rolle, code_hash) values ('BD-S2 Probe', 'lehrer', 'b2:' || gen_random_uuid()) returning id into v_login;
    v_tok := replace(gen_random_uuid()::text || gen_random_uuid()::text, '-', '');
    insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (v_tok, v_login, now() + interval '5 minutes');
    v_key := 'lern:' || v_tok;
    -- Test: Probe-Aufgabe im Test-Vorrat, eigene Testsitzung
    insert into schule.aufgabe ({SPALTEN}) select {feld(SPALTEN, **dict(neu, pool="'test'"))} from schule.aufgabe where id = v_basis returning id into v_t;
    insert into schule.testsitzung (lernender_id, art, block_id, thema_id, einheit_id, aufgaben, punkte_max) values (k, 'blocktest', v_block, v_thema, v_einheit, array[v_t], 1) returning id into v_s;
    p := p || jsonb_build_object('test_format', schule.test_antwort_intern(k, jsonb_build_object('sitzung_id', v_s, 'aufgabe_id', v_t, 'antwort', '{{"werte":["a","1","2"]}}'::jsonb, 'client_id', 'b2-test-f')));
    p := p || jsonb_build_object('test_antwort', schule.test_antwort_intern(k, jsonb_build_object('sitzung_id', v_s, 'aufgabe_id', v_t, 'antwort', falsch, 'client_id', 'b2-test-1')));
    v_r := schule.test_abschliessen_intern(k, jsonb_build_object('sitzung_id', v_s));
    p := p || jsonb_build_object('test_ende', (select e from jsonb_array_elements(v_r->'ergebnisse') e where (e->>'aufgabe_id')::bigint = v_t), 'test_ende_anzahl', jsonb_array_length(v_r->'ergebnisse'),
                                 'test_ende_geheim', (select coalesce(jsonb_agg(g), '[]'::jsonb) from unnest(geheim) g where position(g in v_r::text) > 0));
    -- Expedition im Entwurf (nur das Testkind sieht sie); ein gespeicherter erster Fehlversuch macht sie „begonnen“
    insert into schule.expedition (schluessel, titel) values ('bd-s2-probe-' || gen_random_uuid(), 'Probe BD-S2') returning id into v_x;
    insert into schule.aufgabe ({SPALTEN}) select {feld(SPALTEN, **dict(neu, pool="'expedition'", expedition_id='v_x', teil="'a'"))} from schule.aufgabe where id = v_basis returning id into v_e;
    insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf) values (k, v_e, 'b2-exp-0', falsch, false, 0, 1, 0, 1, 1);
    v_r := schule.expeditionen_kind(k);
    p := p || jsonb_build_object('exp_vor', {teil('v_r', 'v_e')}, 'exp_vor_geheim', (select coalesce(jsonb_agg(g), '[]'::jsonb) from unnest(geheim) g where position(g in v_r::text) > 0));
    p := p || jsonb_build_object('exp_antwort', {uebung('v_e', 'b2-exp-1', extra=", 'anlauf', 2")});
    v_r := schule.expeditionen_kind(k);
    p := p || jsonb_build_object('exp_nach', {teil('v_r', 'v_e')}, 'exp_nach_geheim', (select coalesce(jsonb_agg(g), '[]'::jsonb) from unnest(geheim) g where position(g in v_r::text) > 0));
    v_r := schule.expeditionen_alle();
    p := p || jsonb_build_object('exp_alle', {teil('v_r', 'v_e')}, 'exp_alle_geheim', (select coalesce(jsonb_agg(g), '[]'::jsonb) from unnest(geheim) g where position(g in v_r::text) > 0));
    -- Lernstand und Inhalt (Eltern/Lehrer): ein endgültiger Fehlversuch an einer Übungsaufgabe desselben Flugs
    insert into schule.aufgabe ({SPALTEN}) select {feld(SPALTEN, **neu)} from schule.aufgabe where id = v_basis returning id into v_u;
    v_r := {uebung('v_u', 'b2-ls-1', extra=", 'anlauf', 2")};
    v_r := api.schule_lernstand(v_key, jsonb_build_object('lernender_id', k));
    p := p || jsonb_build_object('lernstand', (select coalesce(jsonb_agg(f), '[]'::jsonb) from jsonb_path_query(v_r, '$.**.fehler[*]') f where f->>'antworttyp' = 'bedingung'),
                                 'lernstand_geheim', (select coalesce(jsonb_agg(g), '[]'::jsonb) from unnest(geheim) g where position(g in v_r::text) > 0));
    v_r := api.schule_inhalt_lesen(v_key, jsonb_build_object('einheit_id', v_einheit));
    p := p || jsonb_build_object('inhalt', (select coalesce(jsonb_agg(jsonb_build_object('id', a2->'id', 'pool', a2->'pool', 'loesung', a2->'loesung')), '[]'::jsonb) from jsonb_array_elements(v_r->'aufgaben') a2 where a2->>'antworttyp' = 'bedingung'),
                                 'inhalt_ids', jsonb_build_array(v_t, v_u, v_e),
                                 'inhalt_geheim', (select coalesce(jsonb_agg(g), '[]'::jsonb) from unnest(geheim) g where position(g in v_r::text) > 0));
    begin -- ohne Zugang kein Lernstand
      v_r := api.schule_lernstand('lern:' || md5(v_tok), jsonb_build_object('lernender_id', k));
      p := p || jsonb_build_object('ohne_zugang', 'nicht abgewiesen');
    exception when others then p := p || jsonb_build_object('ohne_zugang', sqlerrm);
    end;
    raise exception using errcode = 'BD999', message = 'zurueck';
  exception
    when sqlstate 'BD999' then null;
    when others then fehler := fehler || ('Ausgabewege: ' || sqlerrm || ' (bis dahin: ' || coalesce((select string_agg(key, ', ') from jsonb_object_keys(p) key), 'nichts') || ')')::text;
  end;
  if exists (select 1 from schule.lern_login where name = 'BD-S2 Probe') or exists (select 1 from schule.expedition where titel = 'Probe BD-S2') then fehler := fehler || 'Probe-Zugang oder Probe-Expedition ist nicht zurückgerollt'::text; end if;
  if not p ? 'ohne_zugang' then fehler := fehler || 'Ausgabewege: Lauf unvollständig'::text;
  else
    -- laufender Test: nur der Formatstatus, kein Urteil
    if not (p->'test_format' @> '{{"format_ok":false}}'::jsonb) or p->'test_format' ?| array['loesung', 'richtig', 'verletzt'] then fehler := fehler || ('Test, Formatfehler: ' || (p->'test_format')::text)::text; end if;
    if not (p->'test_antwort' @> '{{"format_ok":true,"gespeichert":true}}'::jsonb) or exists (select 1 from jsonb_object_keys(p->'test_antwort') key where key not in ('ok', 'format_ok', 'gespeichert', 'beantwortet', 'gesamt'))
      then fehler := fehler || ('Test, Antwort: ' || (p->'test_antwort')::text)::text; end if;
    if p->'test_ende' is null or jsonb_typeof(p->'test_ende') <> 'object' then fehler := fehler || 'Test-Abschluss: die Probe-Aufgabe fehlt im Ergebnis'::text;
    elsif not (p->'test_ende' @> '{{"richtig":false,"antworttyp":"bedingung"}}'::jsonb) or p->'test_ende'->'loesung' is distinct from v_sicht or p->'test_ende'->'antwort' is distinct from falsch or (p->>'test_ende_anzahl')::int <> 1
      then fehler := fehler || ('Test-Abschluss: ' || left((p->'test_ende')::text, 300))::text; end if;
    -- Expedition
    if p->'exp_vor' is null or jsonb_typeof(p->'exp_vor') <> 'object' then fehler := fehler || 'Expedition beim Kind (vorher): die Probe-Aufgabe fehlt'::text;
    elsif p->'exp_vor' ?| array['loesung', 'einheit', 'loesungsweg'] or not (p->'exp_vor' @> '{{"erledigt":false,"antworttyp":"bedingung"}}'::jsonb) or p->'exp_vor'->'frage' is distinct from v_frage
      then fehler := fehler || ('Expedition beim Kind (vorher): ' || left((p->'exp_vor')::text, 300))::text; end if;
    if not (p->'exp_antwort' @> '{{"format_ok":true,"richtig":false,"verletzt":"Summe ist 0","hinweis":"Deine Summe ist 1."}}'::jsonb) or p->'exp_antwort'->'loesung' is distinct from v_sicht
      then fehler := fehler || ('Expedition, endgültige Antwort: ' || left((p->'exp_antwort')::text, 300))::text; end if;
    if p->'exp_nach' is null or jsonb_typeof(p->'exp_nach') <> 'object' then fehler := fehler || 'Expedition beim Kind (nachher): die Probe-Aufgabe fehlt'::text;
    elsif not (p->'exp_nach' @> '{{"erledigt":true}}'::jsonb) or p->'exp_nach'->'loesung' is distinct from v_sicht or p->'exp_nach' ? 'einheit'
      then fehler := fehler || ('Expedition beim Kind (nachher): ' || left((p->'exp_nach')::text, 300))::text; end if;
    if p->'exp_alle' is null or jsonb_typeof(p->'exp_alle') <> 'object' then fehler := fehler || 'Expeditionen gesamt: die Probe-Aufgabe fehlt'::text;
    elsif p->'exp_alle'->'loesung' is distinct from v_sicht or p->'exp_alle'->'frage' is distinct from v_frage then fehler := fehler || ('Expeditionen gesamt: ' || left((p->'exp_alle')::text, 300))::text; end if;
    -- Lernstand: mindestens ein Fehler-Eintrag des neuen Typs, jeder exakt mit der öffentlichen Lösung
    if jsonb_array_length(p->'lernstand') = 0 then fehler := fehler || 'Lernstand: kein Fehler-Eintrag des neuen Typs (erwarteter Datensatz fehlt)'::text;
    elsif exists (select 1 from jsonb_array_elements(p->'lernstand') f where f->'loesung' is distinct from v_sicht or f->>'frage' is distinct from v_frage->>'text' or f->'antwort' is distinct from falsch)
      then fehler := fehler || ('Lernstand: ' || left((p->'lernstand')::text, 400))::text; end if;
    -- Inhalt: Test- und Übungsaufgabe erscheinen, jede Aufgabe des neuen Typs exakt mit der öffentlichen Lösung
    if not (select coalesce(jsonb_agg(i2->'id'), '[]'::jsonb) from jsonb_array_elements(p->'inhalt') i2) @> jsonb_build_array(p->'inhalt_ids'->0, p->'inhalt_ids'->1)
      then fehler := fehler || ('Inhalt: Probe-Aufgaben fehlen: ' || left((p->'inhalt')::text, 300))::text;
    elsif exists (select 1 from jsonb_array_elements(p->'inhalt') i2 where i2->'loesung' is distinct from v_sicht) then fehler := fehler || ('Inhalt: ' || left((p->'inhalt')::text, 400))::text; end if;
    if p->>'ohne_zugang' = 'nicht abgewiesen' then fehler := fehler || 'Lernstand ohne gültigen Zugang wurde nicht abgewiesen'::text; end if;
    -- ganze Antworten ohne Internes
    for v_txt in select key from jsonb_each(p) where key like '%\\_geheim' and jsonb_array_length(value) > 0 loop
      fehler := fehler || ('GEHEIMES in ' || v_txt || ': ' || (p->v_txt)::text)::text;
    end loop;
    foreach v_txt in array geheim loop
      if position(v_txt in p::text) > 0 then fehler := fehler || ('GEHEIMES in den Ausgabewegen: ' || v_txt)::text; end if;
    end loop;
  end if;"""
    print(f"""-- BD-S2 Einspiel-Paket (erzeugt von tools/tests/bedingung_einspielen2.py). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);
create temp table b2_mig on commit drop as select $b2mig${mig}$b2mig$::text as sql, $b2patch${patch}$b2patch$::text as patch,
$b2alt$do $x$
declare k bigint := (select id from schule.lernender where ist_test order by id limit 1); a schule.aufgabe; r1 jsonb; r2 jsonb; r3 jsonb; r4 jsonb; r5 jsonb;
  falsch constant jsonb := '{{"wert":"987654"}}'; richtig jsonb;
begin
  select * into a from schule.aufgabe where id = (select min(id) from schule.aufgabe where pool = 'uebung' and antworttyp = 'zahl' and freigegeben);
  if k is null or a.id is null then raise exception 'BD-S2: Testkind oder Vergleichsaufgabe fehlt'; end if;
  richtig := jsonb_build_object('wert', replace(a.loesung->>'wert', '.', ','));
  begin
    r1 := schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', a.id, 'antwort', falsch, 'client_id', 'b2-alt-1', 'anlauf', 1));
    r2 := schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', a.id, 'antwort', falsch, 'client_id', 'b2-alt-2', 'anlauf', 2));
    r3 := schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', a.id, 'antwort', falsch, 'client_id', 'b2-alt-1', 'anlauf', 1));
    r5 := schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', a.id, 'antwort', falsch, 'client_id', 'b2-alt-2', 'anlauf', 2));
    raise exception using errcode = 'BD999', message = 'zurueck';
  exception when sqlstate 'BD999' then null;
  end;
  begin
    r4 := schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', a.id, 'antwort', richtig, 'client_id', 'b2-alt-3', 'anlauf', 1));
    raise exception using errcode = 'BD999', message = 'zurueck';
  exception when sqlstate 'BD999' then null;
  end;
  insert into b2_aus values ('PHASE', 'falsch-1', r1), ('PHASE', 'falsch-2', r2), ('PHASE', 'wiederholt', r3), ('PHASE', 'richtig', r4), ('PHASE', 'wiederholt-endgueltig', r5);
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
  geheim constant text[] := array['{MERK}', '"pruefe"', '"zeige"', '"gegenbeispiele"'];
  p jsonb := '{{}}'; v_t bigint; v_u bigint; v_e bigint; v_s bigint; v_x bigint; v_login bigint; v_tok text; v_key text; v_basis_l jsonb;
  v_einheit bigint; v_block bigint; v_thema bigint; v_andere text; v_zu text[] := '{{}}'; v_rollen int := 0; v_fn text[];
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
  select array_agg(distinct s.nspname || '.' || p.proname order by s.nspname || '.' || p.proname) into v_fn from pg_proc p join pg_namespace s on s.oid = p.pronamespace
   where s.nspname in ('schule', 'api') and p.prosrc ~ '(^|[^_a-z])loesung([^_a-z]|$)';
  if v_fn is distinct from {fn_soll} then fehler := fehler || ('Funktionen mit „loesung“ sind nicht die erwarteten: ' || array_to_string(v_fn, ', '))::text; end if;
  select count(*), string_agg(s.nspname || '.' || p.proname, ', ') into n, v_txt from pg_proc p join pg_namespace s on s.oid = p.pronamespace
   where s.nspname in ('schule', 'api') and p.prosrc ~* '(to_jsonb|row_to_json|to_json)[[:space:]]*[(][[:space:]]*a[[:space:]]*[)]';
  if n <> 0 then fehler := fehler || ('ganze Aufgabenzeile wird gesendet in: ' || v_txt)::text; end if;

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
  if (select count(*) from b2_aus where r is not null) <> 10 then fehler := fehler || 'Vorher-Nachher-Vergleich unvollständig'::text; end if;
  select loesung into v_basis_l from schule.aufgabe where id = v_basis;
  select count(*), string_agg(w.schritt, ', ') into n, v_txt from b2_aus w where w.phase = 'nach' and not case w.schritt
    when 'falsch-1' then w.r @> '{{"format_ok":true,"richtig":false,"nochmal":true}}'::jsonb and not w.r ? 'loesung'
    when 'falsch-2' then w.r @> '{{"format_ok":true,"richtig":false}}'::jsonb and w.r->'loesung' = v_basis_l and not w.r ? 'nochmal'
    when 'wiederholt' then w.r @> '{{"richtig":false,"nochmal":true,"wiederholt":true}}'::jsonb and not w.r ? 'loesung'
    when 'wiederholt-endgueltig' then w.r @> '{{"richtig":false,"wiederholt":true}}'::jsonb and w.r->'loesung' = v_basis_l and not w.r ? 'nochmal'
    when 'richtig' then w.r @> '{{"format_ok":true,"richtig":true}}'::jsonb and w.r->'loesung' = v_basis_l
    else false end;
  if n <> 0 then fehler := fehler || ('alter Typ: fachlich unerwartete Antwort bei: ' || v_txt)::text; end if;

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
    begin -- client_id eines Versuchs an DIESER Aufgabe, aber eine andere Aufgabe genannt: muss abgewiesen werden
      v_r := schule.uebung_pruefen_intern(k, jsonb_build_object('aufgabe_id', v_basis, 'antwort', '{{"wert":"1"}}'::jsonb, 'client_id', 'b2-neu-2', 'anlauf', 2));
      v_andere := 'nicht abgewiesen: ' || left(v_r::text, 200);
    exception when others then v_andere := sqlerrm;
    end;
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
    if o->'anzeige' ? 'einheit' or o->'anzeige' ? 'loesung' then fehler := fehler || ('Anzeige enthält ein Feld aus der Lösung: ' || (o->'anzeige')::text)::text; end if;
    if not (o->'falsch1' @> '{{"format_ok":true,"richtig":false,"nochmal":true,"verletzt":"Summe ist 0","hinweis":"Deine Summe ist 1."}}'::jsonb) or o->'falsch1' ? 'loesung'
      then fehler := fehler || ('erster Fehlversuch: ' || (o->'falsch1')::text)::text; end if;
    if not (o->'wiederholt1' @> '{{"nochmal":true,"wiederholt":true,"verletzt":"Summe ist 0","hinweis":"Deine Summe ist 1."}}'::jsonb) or o->'wiederholt1' ? 'loesung'
      then fehler := fehler || ('wiederholter erster Fehlversuch: ' || (o->'wiederholt1')::text)::text; end if;
    if not (o->'format' @> '{{"format_ok":false}}'::jsonb) or o->'format' ? 'loesung' or coalesce(o->'format'->>'hinweis', '') = '' then fehler := fehler || ('Formatfehler: ' || (o->'format')::text)::text; end if;
    if not (o->'falsch2' @> '{{"format_ok":true,"richtig":false,"verletzt":"Summe ist 0","hinweis":"Deine Summe ist 1."}}'::jsonb) or o->'falsch2'->'loesung' is distinct from v_sicht or o->'falsch2' ? 'nochmal'
      then fehler := fehler || ('zweiter Fehlversuch: ' || left((o->'falsch2')::text, 300))::text; end if;
    if not (o->'wiederholt2' @> '{{"richtig":false,"wiederholt":true,"verletzt":"Summe ist 0","hinweis":"Deine Summe ist 1."}}'::jsonb) or o->'wiederholt2'->'loesung' is distinct from v_sicht
       or o->'wiederholt2'->>'verletzt' is distinct from o->'falsch2'->>'verletzt' or o->'wiederholt2'->>'hinweis' is distinct from o->'falsch2'->>'hinweis' or o->'wiederholt2' ? 'nochmal' then fehler := fehler || ('wiederholte endgültige Antwort: ' || left((o->'wiederholt2')::text, 300))::text; end if;
    if not (o->'richtig' @> '{{"format_ok":true,"richtig":true}}'::jsonb) or o->'richtig'->'loesung' is distinct from v_sicht or o->'richtig' ? 'verletzt' then fehler := fehler || ('richtig: ' || left((o->'richtig')::text, 300))::text; end if;
    if not (o->'knobel' @> '{{"richtig":false,"bonus":true,"verletzt":"Summe ist 0"}}'::jsonb) or o->'knobel'->'loesung' is distinct from v_sicht then fehler := fehler || ('Knobel: ' || left((o->'knobel')::text, 300))::text; end if;
  end if;
  if v_schutz is null or v_schutz not like '%hat schon Versuche%' then fehler := fehler || ('Versionsschutz: ' || coalesce(v_schutz, 'nicht geprüft'))::text; end if;
  if v_andere is null or v_andere not like '%gehört zu einer anderen Aufgabe%' then fehler := fehler || ('client_id einer anderen Aufgabe: ' || coalesce(v_andere, 'nicht geprüft'))::text; end if;

{wege}

  -- 5. Constraints: Typ-Liste exakt die Sollmenge; unzulässiger Baum und zusätzlicher Lösungsschlüssel scheitern an aufgabe_bedingung_gueltig
  select pg_get_constraintdef(oid) into v_txt from pg_constraint where conname = 'aufgabe_antworttyp_check' and conrelid = 'schule.aufgabe'::regclass;
  if v_txt is distinct from {typ_soll} then fehler := fehler || ('aufgabe_antworttyp_check ist nicht exakt die Sollmenge: ' || coalesce(v_txt, 'fehlt'))::text; end if;
  select pg_get_constraintdef(oid) into v_txt from pg_constraint where conname = 'aufgabe_bedingung_gueltig' and conrelid = 'schule.aufgabe'::regclass and convalidated;
  if v_txt is null or v_txt is distinct from (select pg_get_constraintdef(oid) from pg_constraint where conname = 'z_gueltig' and conrelid = to_regclass('pg_temp.bd_s2_zwilling'))
    then fehler := fehler || ('aufgabe_bedingung_gueltig fehlt oder weicht von der Soll-Fassung ab: ' || coalesce(v_txt, 'fehlt'))::text; end if;
  for i in 1 .. 2 loop
    v_c := null;
    begin
      if i = 1 then
        insert into schule.aufgabe ({SPALTEN}) select {feld_baum} from schule.aufgabe where id = v_basis;
      else
        insert into schule.aufgabe ({SPALTEN}) select {feld_einheit} from schule.aufgabe where id = v_basis;
      end if;
      raise exception using errcode = 'BD999', message = 'offen';
    exception
      when check_violation then get stacked diagnostics v_c = constraint_name;
      when sqlstate 'BD999' then v_c := 'angenommen';
      when others then v_c := 'unerwartet: ' || sqlerrm;
    end;
    if v_c is distinct from 'aufgabe_bedingung_gueltig' then fehler := fehler || (case i when 1 then 'unzulässiger Baum' else 'zusätzlicher Lösungsschlüssel „einheit“' end || ': ' || coalesce(v_c, 'ohne Ergebnis'))::text;
    else v_zu := v_zu || case i when 1 then 'unzulässiger Baum abgewiesen'::text else 'Lösungsschlüssel „einheit“ abgewiesen'::text end; end if;
  end loop;

  -- 6. Rechte: App-Rollen können loesung_sicht nicht direkt aufrufen. Der Rollenwechsel selbst wird getrennt abgesichert.
  for v_rolle in select rolname from pg_roles where rolname in ('anon', 'authenticated', 'council_mcp', 'service_role') order by 1 loop
    v_rollen := v_rollen + 1;
    begin
      begin
        execute format('set local role %I', v_rolle);
      exception when others then raise exception using errcode = 'BD998', message = sqlerrm;
      end;
      if current_user <> v_rolle then raise exception using errcode = 'BD998', message = 'current_user ist ' || current_user; end if;
      begin
        execute 'select schule.loesung_sicht(jsonb_populate_record(null::schule.aufgabe, $1))' into v_r using jsonb_build_object('antworttyp', 'bedingung', 'loesung', v_loesung);
        v_txt := 'darf';
      exception when insufficient_privilege then v_txt := 'gesperrt';
      end;
      raise exception using errcode = 'BD999', message = v_txt;
    exception
      when sqlstate 'BD999' then
        if sqlerrm = 'gesperrt' then v_gesperrt := v_gesperrt || v_rolle; else fehler := fehler || (v_rolle || ' kann schule.loesung_sicht direkt aufrufen')::text; end if;
      when sqlstate 'BD998' then fehler := fehler || ('Rollenwechsel zu ' || v_rolle || ' schlug fehl (' || sqlerrm || ') – Sperre nicht nachgewiesen')::text;
      when others then fehler := fehler || ('Rechteprobe als ' || v_rolle || ' unerwartet: ' || sqlerrm)::text;
    end;
  end loop;
  if current_user <> session_user and current_user <> 'postgres' then fehler := fehler || ('nach der Rechteprobe ist die Rolle ' || current_user)::text; end if;
  if coalesce(array_length(v_gesperrt, 1), 0) <> v_rollen or not v_gesperrt @> array['anon', 'authenticated']::text[] then fehler := fehler || ('Rechteprobe unvollständig: ' || array_to_string(v_gesperrt, ', '))::text; end if;

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
  insert into b2_bericht select jsonb_build_object('ergebnis', 'BD-S2 eingespielt, alle Prüfungen bestanden', 'proben', v_misch, 'alter_typ_gleich', 5,
    'neuer_typ_antworten', (select jsonb_agg(key) from jsonb_object_keys(o) key), 'erster_fehlversuch', o->'falsch1', 'loesung_fuer_das_kind', o->'sicht',
    'versionsschutz', v_schutz, 'fremde_client_id', v_andere, 'constraint_proben', v_zu, 'wege', p - 'lernstand_ganz' - 'inhalt_ganz', 'direktaufruf_gesperrt_fuer', v_gesperrt, 'ms_knoten_brueche_potenz', ms,
    'aufgaben_neuer_typ', (select count(*) from schule.aufgabe where antworttyp = 'bedingung'));
  {ende}
end $pruef$;
select b from b2_bericht;""")


if __name__ == '__main__':
    main()
