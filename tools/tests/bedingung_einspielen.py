"""Einspiel-Paket für BD-S1 (Antworttyp „bedingung“, Teil 1) – prüft sich selbst.

Erzeugt EIN SQL für EINEN Aufruf (eine Sitzung, eine Transaktion). Ablauf darin:
  1. Vorher-Stand festhalten: Definition und Rechte von schule.antwort_bewerten, Definition des Antworttyp-Constraints,
     Ergebnisse der fünf bisherigen Antworttypen für echte gespeicherte Antworten und für gebaute Fehl-Eingaben.
  2. Die ganze Migration ausführen, dann vollständig noch einmal.
  3. Prüfen (Abschnitt „Prüfblock“). Bei der kleinsten Abweichung: Ausnahme -> die ganze Transaktion wird zurückgerollt,
     in der Datenbank bleibt nichts. Nur wenn alles stimmt, endet der Aufruf ohne Fehler und die Änderung gilt.
Geprüft wird: zweiter Lauf ändert nichts · Mischstände werden abgewiesen (je in eigener Untertransaktion) · der Zweig in
antwort_bewerten liefert für alle Prüf-Fälle dasselbe wie tools/bedingung.py (Prüfsummen) · die fünf alten Antworttypen
liefern dasselbe wie vorher · App-Rollen haben keine Rechte an den neuen Funktionen, Rechte von antwort_bewerten unverändert ·
der Constraint ist unverändert und lässt den neuen Typ nicht zu · Laufzeit.

Aufruf:  python3 -I tools/tests/bedingung_einspielen.py > einspielen.sql
Nicht ohne den ausdrücklichen Satz des Nutzers ausführen. Vorher: werkstatt_sperre. Nachher: werkstatt_aenderung.
"""
import hashlib
import json
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
sys.path.insert(0, str(HIER.parent))
import bedingung  # noqa: E402
import bedingung_sql_test as T  # noqa: E402

MIG = HIER.parent.parent / 'supabase/migrations/20261201_bd_s1_bedingung_rechner.sql'
GROSS = ["999983/999979", "-999961/999959", "999,999", "-999953/7", "999931/11", "13/999907"]   # große Brüche: Lastgrenze oder teure Rechnung
POTENZ = ["7/3", "-5/2", "9/4", "3/7", "2", "-3"]   # Antwort für den dritten Messfall


def teuer_potenz():
    """Dritter Messfall: Potenzen (auch negative), Divisionen und Betrag in sieben Bedingungen; die achte läuft in „nicht definiert“
    (Division durch null) – in pruefe und noch einmal im Hinweis. Alle acht Bedingungen werden durchlaufen."""
    a = ["+", ["hoch", ["/", "$1", "$2"], 6], ["hoch", ["/", "$3", "$4"], -6], ["hoch", "$5", 5], ["betrag", ["hoch", "$6", 3]]]   # 17 Knoten
    beds = [{"name": f"p{i}", "pruefe": [">", ["+", a, a, a, 1], -999999]} for i in range(1, 8)]
    null = ["/", "$1", ["-", "$5", "$5"]]
    beds.append({"name": "p8", "pruefe": [">", null, 0], "zeige": null, "hinweis": "Bei dir kommt {} heraus."})
    aufgabe = {"id": "teuer-potenz", "f": {"felder": [{"art": "rational"}] * 6}, "o": {"bedingungen": beds[:7], "beispiel": [1, 1, 1, 1, 1, 1]}}
    assert not bedingung.pruefe_aufgabe(aufgabe, nur_form=True), bedingung.pruefe_aufgabe(aufgabe, nur_form=True)
    aufgabe["o"]["bedingungen"] = beds          # mit p8 besteht kein Beispiel mehr: p8 ist nie erfüllt – gewollt, nur für die Messung
    r = bedingung.bewerte(aufgabe, {"werte": POTENZ})
    assert r == {"format_ok": True, "richtig": False, "verletzt": "p8"}, r
    return aufgabe


ALT = ['{}', '{"wert":"abc"}', '{"wert":"1.5"}', '{"wert":"-3"}', '{"wert":""}', '{"wert":"12 €"}', '{"index":"x"}', '{"index":0}',
       '{"index":99}', '{"werte":[]}', '{"werte":["1","2"]}', '{"werte":["a"]}', 'null']


def main():
    mig = MIG.read_text(encoding='utf-8')
    assert '$bdmig$' not in mig and '$bdpatch$' not in mig and '$pruef$' not in mig
    i = mig.index('do $$', mig.index('-- Zweig in schule.antwort_bewerten'))
    patch = mig[i:mig.index('end $$;', i) + len('end $$;')]
    auf, extra, unzu = T.aufgaben(False)
    unzu = [{'f': {'felder': (u.get('f') or {}).get('felder')}, 'o': {k: v for k, v in (u.get('o') or {}).items() if k in ('bedingungen', 'beispiel')}} for u in unzu]
    soll = []
    for a in auf:
        zeilen = [T.kanon(bedingung.bewerte(a, x)) for x in T.antworten(a) + extra.get(a['id'], [])]
        soll.append(f"aufgabe {a['id']} {len(zeilen)} {hashlib.md5(chr(10).join(zeilen).encode('utf-8')).hexdigest()}")
    urteil = ['1' if not bedingung.pruefe_aufgabe(x, nur_form=True) else '0' for x in [{'f': a['f'], 'o': a['o']} for a in auf] + unzu]
    assert urteil[:len(auf)] == ['1'] * len(auf) and urteil.count('0') >= 20, urteil
    soll.append(f"form {len(urteil)} {hashlib.md5(''.join(urteil).encode()).hexdigest()}")
    klein = [{'id': a['id'], 'felder': a['f']['felder'], 'bed': a['o']['bedingungen'], 'bsp': a['o']['beispiel'], 'fest': T.fest(a), 'extra': extra.get(a['id'], [])} for a in auf]
    lit = lambda v: "'" + bedingung.schreibe_json(v).replace("'", "''") + "'::jsonb"
    tp = teuer_potenz()
    erste = auf[0]
    alt = ', '.join(f"('{x}'::jsonb)" for x in ALT)
    print(f"""-- BD-S1 Einspiel-Paket (erzeugt von tools/tests/bedingung_einspielen.py). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);
create temp table bd_mig on commit drop as select $bdmig${mig}$bdmig$::text as sql, $bdpatch${patch}$bdpatch$::text as patch;
create temp table bd_vor on commit drop as select
  pg_get_functiondef('schule.antwort_bewerten(schule.aufgabe, jsonb)'::regprocedure) as def,
  (select proacl::text from pg_proc where oid = 'schule.antwort_bewerten(schule.aufgabe, jsonb)'::regprocedure) as acl,
  (select pg_get_constraintdef(oid) from pg_constraint where conname = 'aufgabe_antworttyp_check' and conrelid = 'schule.aufgabe'::regclass) as con;
create temp table bd_fall on commit drop as
  with v as (select v.aufgabe_id, v.antwort, row_number() over (partition by a.antworttyp order by v.id desc) as rn
               from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id where v.antwort is not null),
       s as (select id, antworttyp, loesung, row_number() over (partition by antworttyp order by id) as rn from schule.aufgabe where antworttyp in ('auswahl', 'zahl', 'text', 'markierung', 'luecken'))
  select row_number() over () as nr, q.* from (
    select aufgabe_id, antwort from v where rn <= 500
    union all select s.id, x.a from s cross join (values {alt}) x(a) where s.rn <= 40
    -- gebaut richtig: aus der Lösung
    union all select s.id, case s.antworttyp when 'zahl' then jsonb_build_object('wert', replace(s.loesung->>'wert', '.', ','))
                                             when 'text' then jsonb_build_object('wert', s.loesung->>'text')
                                             when 'luecken' then jsonb_build_object('werte', (select jsonb_agg(x) from jsonb_array_elements_text(s.loesung->'werte') x))
                                             else jsonb_build_object('index', s.loesung->'index') end from s where s.rn <= 40
    -- gebaut falsch
    union all select s.id, case s.antworttyp when 'zahl' then '{{"wert":"987654"}}'::jsonb
                                             when 'text' then '{{"wert":"qqq"}}'::jsonb
                                             when 'luecken' then jsonb_build_object('werte', (select jsonb_agg('98765'::text) from jsonb_array_elements(s.loesung->'werte')))
                                             else jsonb_build_object('index', case when (s.loesung->>'index')::int = 0 then 1 else 0 end) end from s where s.rn <= 40) q;
create temp table bd_alt on commit drop as
  select f.nr, a.antworttyp, schule.antwort_bewerten(a, f.antwort) as r from bd_fall f join schule.aufgabe a on a.id = f.aufgabe_id;
do $$ begin execute (select sql from bd_mig); end $$;
create temp table bd_nach1 on commit drop as select
  pg_get_functiondef('schule.antwort_bewerten(schule.aufgabe, jsonb)'::regprocedure) as def,
  (select proacl::text from pg_proc where oid = 'schule.antwort_bewerten(schule.aufgabe, jsonb)'::regprocedure) as acl;
do $$ begin execute (select sql from bd_mig); end $$;
create temp table bd_ist on commit drop as
with a as (select x, o from jsonb_array_elements({lit(klein)}) with ordinality t(x, o)),
vorrat as (select {lit(T.VORRAT)} as v),
k as (select a.*, jsonb_array_length(x->'felder') as k,
             jsonb_populate_record(null::schule.aufgabe, jsonb_build_object('antworttyp', 'bedingung', 'frage', jsonb_build_object('felder', x->'felder'),
                                   'loesung', jsonb_build_object('bedingungen', x->'bed', 'beispiel', x->'bsp'))) as rec from a),
faelle as (
  select k.o, 0 as teil, f.o2 as nr, jsonb_build_object('werte', f.w) as antwort from k, jsonb_array_elements(k.x->'fest') with ordinality f(w, o2)
  union all
  select k.o, 1, j, jsonb_build_object('werte', (select jsonb_agg(v->(((j * 7 + i * 13 + (j / 5) * (i + 1) * 3 + j * j) % (case when j % 3 <> 0 then {T.GANZE} else jsonb_array_length(v) end))::int) order by i)
                                                  from generate_series(0, k.k - 1) i))
    from k, vorrat, generate_series(0, {T.N - 1}) j
  union all select k.o, 2, 1, '{{"werte":[]}}'::jsonb from k
  union all select k.o, 2, 2, jsonb_build_object('werte', (select jsonb_agg('1'::text) from generate_series(0, k.k) i)) from k
  union all select k.o, 2, 3, '{{}}'::jsonb from k
  union all select k.o, 2, 4, '{{"werte":null}}'::jsonb from k
  union all select k.o, 2, 5, '{{"werte":"1"}}'::jsonb from k
  union all select k.o, 3, e.o2, e.w from k, jsonb_array_elements(k.x->'extra') with ordinality e(w, o2)),
erg as (select f.o, f.teil, f.nr, schule.antwort_bewerten(k.rec, f.antwort) as r from faelle f join k using (o))
select k.o::int as o, 'aufgabe ' || (k.x->>'id') || ' ' || count(*) || ' ' ||
       md5(string_agg(concat_ws('|', r->>'format_ok', coalesce(r->>'richtig', ''), coalesce(r->>'verletzt', ''), coalesce(r->>'hinweis', '')), E'\\n' order by teil, nr)) as z
from erg join k using (o) group by k.o, k.x->>'id'
union all
select 1000, 'form ' || count(*) || ' ' || md5(string_agg(case when schule.bed_gueltig(f, l) is null then '1' else '0' end, '' order by o))
from (select o, jsonb_build_object('felder', x->'felder') as f, jsonb_build_object('bedingungen', x->'bed', 'beispiel', x->'bsp') as l from a
      union all select 1000 + o, x->'f', x->'o' from jsonb_array_elements({lit(unzu)}) with ordinality t(x, o)) q
union all
select 2000, (x->'felder')::text || chr(1) || (x->'bed')::text from a where x->>'id' = 'teuer';
create temp table bd_bericht on commit drop as select null::jsonb as b where false;

-- Prüfblock
do $pruef$
declare
  fehler text[] := '{{}}'; v_vor record; v_n1 record; v_def text; v_acl text; v_con text; v_txt text; v_c text; m int; i int; n int;
  v_soll text[] := array(select jsonb_array_elements_text({lit(soll)}));
  v_ist text[]; v_f jsonb; v_b jsonb; v_r jsonb; t0 timestamptz; ms1 numeric; ms2 numeric; v_alt jsonb; v_rolle text; v_fn text; v_misch text[] := '{{}}'; v_weg text[] := '{{}}'; v_gesperrt text[] := '{{}}'; ms3 numeric; v_r2 jsonb;
  v_e1 constant jsonb := {lit({'felder': erste['f']['felder'], 'bed': erste['o']['bedingungen'], 'bsp': erste['o']['beispiel']})};
  anker constant text := E'begin\\n  if p_aufgabe.antworttyp = ''luecken'' then';
  v_patch text := (select patch from bd_mig);
begin
  select * into v_vor from bd_vor; select * into v_n1 from bd_nach1;
  v_def := pg_get_functiondef('schule.antwort_bewerten(schule.aufgabe, jsonb)'::regprocedure);
  select proacl::text into v_acl from pg_proc where oid = 'schule.antwort_bewerten(schule.aufgabe, jsonb)'::regprocedure;
  select pg_get_constraintdef(oid) into v_con from pg_constraint where conname = 'aufgabe_antworttyp_check' and conrelid = 'schule.aufgabe'::regclass;

  -- 1. Erster Lauf hat eingebaut, zweiter Lauf ändert nichts
  if v_vor.def = v_n1.def then fehler := fehler || 'erster Lauf hat antwort_bewerten nicht geändert'::text; end if;
  if v_n1.def is distinct from v_def then fehler := fehler || 'zweiter Lauf hat die Definition geändert'::text; end if;
  if v_n1.acl is distinct from v_acl or v_vor.acl is distinct from v_acl then fehler := fehler || 'Rechte von antwort_bewerten geändert'::text; end if;
  if (length(v_def) - length(replace(v_def, 'bed_bewerten', ''))) / length('bed_bewerten') <> 1 then fehler := fehler || 'bed_bewerten steht nicht genau einmal in antwort_bewerten'::text; end if;

  -- 2. Mischstände: je in eigener Untertransaktion herstellen, Einbau muss abbrechen; Fall 4 ist die Gegenprobe (alter Stand -> Einbau gelingt)
  for m in 1 .. 4 loop
    begin
      if m = 1 then execute replace(v_vor.def, anker, anker || ' -- bed_bewerten');
      elsif m = 2 then execute replace(v_def, E'begin\\n  if p_aufgabe.antworttyp = ''bedingung'' then', E'begin\\n  -- bed_bewerten\\n  if p_aufgabe.antworttyp = ''bedingung'' then');
      elsif m = 3 then execute replace(v_vor.def, anker, E'begin\\n  if p_aufgabe.antworttyp = ''luecken''  then');
      else execute v_vor.def;
      end if;
      execute v_patch;
      v_txt := pg_get_functiondef('schule.antwort_bewerten(schule.aufgabe, jsonb)'::regprocedure);
      raise exception using errcode = 'BD999', message = case when m = 4 and v_txt = v_def then 'gegenprobe-ok' else 'kein-abbruch' end;
    exception
      when sqlstate 'BD999' then
        if sqlerrm = 'gegenprobe-ok' then v_misch := v_misch || 'Gegenprobe ok'::text;
        else fehler := fehler || ('Mischstand ' || m || ': Einbau wurde nicht abgewiesen oder Gegenprobe falsch')::text; end if;
      when others then
        if m < 4 and sqlerrm like 'BD-S1:%' then v_misch := v_misch || ('Fall ' || m || ' abgewiesen')::text;
        else fehler := fehler || ('Mischstand ' || m || ': unerwartet: ' || sqlerrm)::text; end if;
    end;
  end loop;
  if pg_get_functiondef('schule.antwort_bewerten(schule.aufgabe, jsonb)'::regprocedure) is distinct from v_def then fehler := fehler || 'nach den Mischstand-Proben ist die Definition nicht wieder die neue'::text; end if;

  -- 3. Zweig in antwort_bewerten gegen die Python-Referenz (Prüfsummen), Formurteile
  select array_agg(z order by o) into v_ist from bd_ist where o < 2000;
  if v_ist is distinct from v_soll then
    fehler := fehler || ('Abweichung von der Referenz: ' || coalesce((select string_agg(x, '; ') from unnest(v_ist) x where x <> all (v_soll)), 'Anzahl'))::text;
  end if;

  -- 4. Die fünf alten Antworttypen: dasselbe wie vorher
  select count(*) into n from bd_alt o join bd_fall f using (nr) join schule.aufgabe a on a.id = f.aufgabe_id
   where schule.antwort_bewerten(a, f.antwort) is distinct from o.r;
  if n <> 0 then fehler := fehler || (n || ' alte Bewertungen weichen ab')::text; end if;
  -- Abdeckung: je Typ müssen richtige, falsche und im Format abgewiesene Antworten im Vergleich sein
  select string_agg(t, ', ') into v_txt from unnest(array['auswahl', 'zahl', 'text', 'markierung', 'luecken']) t
   where not exists (select 1 from bd_alt o where o.antworttyp = t and o.r->>'richtig' = 'true')
      or not exists (select 1 from bd_alt o where o.antworttyp = t and o.r->>'richtig' = 'false')
      or not exists (select 1 from bd_alt o where o.antworttyp = t and o.r->>'format_ok' = 'false');
  if v_txt is not null then fehler := fehler || ('Altvergleich ohne richtig/falsch/Formatfehler bei: ' || v_txt)::text; end if;

  -- 5. Rechte: App-Rollen dürfen die neuen Funktionen nicht aufrufen; der Eigentümer der Bewertung darf es
  for v_fn in select p.oid::regprocedure::text from pg_proc p join pg_namespace s on s.oid = p.pronamespace where s.nspname = 'schule' and p.proname like 'bed\\_%' loop
    for v_rolle in select rolname from pg_roles where rolname in ('anon', 'authenticated', 'council_mcp', 'service_role') loop
      if has_schema_privilege(v_rolle, 'schule', 'usage') and has_function_privilege(v_rolle, v_fn, 'execute') then fehler := fehler || (v_rolle || ' darf ' || v_fn || ' aufrufen')::text; end if;
    end loop;
    if coalesce((select proacl::text from pg_proc where oid = v_fn::regprocedure), '{{=X/') ~ '(\\{{|,)=X/' then fehler := fehler || (v_fn || ': PUBLIC darf noch aufrufen')::text; end if;
    if not has_function_privilege('postgres', v_fn, 'execute') then fehler := fehler || ('postgres darf ' || v_fn || ' nicht aufrufen')::text; end if;
  end loop;
  if (select count(*) from pg_proc p join pg_namespace s on s.oid = p.pronamespace where s.nspname = 'schule' and p.proname like 'bed\\_%') <> 9 then fehler := fehler || 'nicht genau neun bed_-Funktionen'::text; end if;
  -- Der Bewertungsweg der App läuft über SECURITY-DEFINER-Einstiege im Schema api. Positiver Nachweis: Im Kontext jedes ihrer
  -- Eigentümer liefert antwort_bewerten für eine gebaute Aufgabe des neuen Typs „richtig“. Die neuen Funktionen gehören demselben Eigentümer.
  n := 0;
  for v_rolle in select distinct pg_get_userbyid(p.proowner) from pg_proc p join pg_namespace s on s.oid = p.pronamespace where s.nspname = 'api' and p.prosecdef loop
    n := n + 1;
    begin
      execute format('set local role %I', v_rolle);
      execute 'select schule.antwort_bewerten(jsonb_populate_record(null::schule.aufgabe, $1), $2)' into v_r
        using jsonb_build_object('antworttyp', 'bedingung', 'frage', jsonb_build_object('felder', v_e1->'felder'), 'loesung', jsonb_build_object('bedingungen', v_e1->'bed')),
              jsonb_build_object('werte', v_e1->'bsp');
      execute 'reset role';
      if v_r is distinct from '{{"format_ok":true,"richtig":true}}'::jsonb then fehler := fehler || ('Bewertungsweg als ' || v_rolle || ' liefert ' || coalesce(v_r::text, 'null'))::text; end if;
      v_weg := v_weg || v_rolle;
    exception when others then fehler := fehler || ('Bewertungsweg als ' || v_rolle || ' scheitert: ' || sqlerrm)::text;
    end;
    if exists (select 1 from pg_proc p join pg_namespace s on s.oid = p.pronamespace where s.nspname = 'schule' and (p.proname like 'bed\\_%' or p.proname = 'antwort_bewerten') and pg_get_userbyid(p.proowner) <> v_rolle)
      then fehler := fehler || ('Eigentümer der Bewertungsfunktionen ist nicht ' || v_rolle)::text; end if;
  end loop;
  if n = 0 then fehler := fehler || 'kein SECURITY-DEFINER-Einstieg in api gefunden'::text; end if;
  -- Negativer Nachweis: Jede App-Rolle wird wirklich angenommen; der direkte Aufruf muss an fehlendem Recht scheitern.
  for v_rolle in select rolname from pg_roles where rolname in ('anon', 'authenticated', 'council_mcp', 'service_role') loop
    begin
      execute format('set local role %I', v_rolle);
      execute 'select schule.bed_bewerten($1, $2, $3)' into v_r using v_e1->'felder', v_e1->'bed', jsonb_build_object('werte', v_e1->'bsp');
      raise exception using errcode = 'BD999', message = 'darf';
    exception
      when insufficient_privilege then v_gesperrt := v_gesperrt || v_rolle;
      when sqlstate 'BD999' then fehler := fehler || (v_rolle || ' kann schule.bed_bewerten direkt aufrufen')::text;
      when others then fehler := fehler || ('Rechteprobe als ' || v_rolle || ' unerwartet: ' || sqlerrm)::text;
    end;
  end loop;

  -- 6. Constraint unverändert und zu
  if v_con is distinct from v_vor.con or v_con like '%bedingung%' then fehler := fehler || 'Constraint geändert oder schon offen'::text; end if;
  begin
    insert into schule.aufgabe (einheit_id, thema_id, teilfaehigkeit, art, stufe, variante_gruppe, antworttyp, frage, antworten, loesung, tipp, loesungsweg,
                                punkte_max, reihenfolge, pool, freigegeben, typ, expedition_id, teil)
    select einheit_id, thema_id, teilfaehigkeit, art, stufe, variante_gruppe, 'bedingung', frage, antworten, loesung, tipp, loesungsweg,
           punkte_max, reihenfolge, pool, false, typ, expedition_id, teil from schule.aufgabe order by id limit 1;
    raise exception using errcode = 'BD999', message = 'offen';
  exception
    when check_violation then get stacked diagnostics v_c = constraint_name;
      if v_c <> 'aufgabe_antworttyp_check' then fehler := fehler || ('neuer Typ scheitert an ' || v_c || ' statt am Antworttyp-Constraint')::text; else v_c := 'abgewiesen'; end if;
    when sqlstate 'BD999' then fehler := fehler || 'Constraint lässt den neuen Typ zu'::text;
    when others then fehler := fehler || ('Constraint-Probe unerwartet: ' || sqlerrm)::text;   -- kein Erfolg ohne nachgewiesenen Abbruch
  end;
  if v_c is distinct from 'abgewiesen' and not ('Constraint lässt den neuen Typ zu' = any (fehler)) and not exists (select 1 from unnest(fehler) f where f like 'neuer Typ scheitert%' or f like 'Constraint-Probe%')
    then fehler := fehler || 'Constraint-Probe ohne Ergebnis'::text; end if;

  -- 7. Laufzeit (Mittel aus 200): Fall mit den meisten Knoten und Fall mit großen Brüchen
  select split_part(z, chr(1), 1)::jsonb, split_part(z, chr(1), 2)::jsonb into v_f, v_b from bd_ist where o = 2000;
  t0 := clock_timestamp(); for i in 1 .. 200 loop v_r := schule.bed_bewerten(v_f, v_b, {lit({'werte': T.MESS})}); end loop;
  ms1 := round((extract(epoch from clock_timestamp() - t0) * 5)::numeric, 2);
  t0 := clock_timestamp(); for i in 1 .. 200 loop v_r := schule.bed_bewerten(v_f, v_b, {lit({'werte': GROSS})}); end loop;
  ms2 := round((extract(epoch from clock_timestamp() - t0) * 5)::numeric, 2);
  v_r2 := v_r;
  t0 := clock_timestamp(); for i in 1 .. 200 loop v_r := schule.bed_bewerten({lit(tp['f']['felder'])}, {lit(tp['o']['bedingungen'])}, {lit({'werte': POTENZ})}); end loop;
  ms3 := round((extract(epoch from clock_timestamp() - t0) * 5)::numeric, 2);
  if v_r is distinct from '{{"format_ok":true,"richtig":false,"verletzt":"p8"}}'::jsonb then fehler := fehler || ('Messfall Potenz liefert ' || v_r::text)::text; end if;
  if ms1 > 200 or ms2 > 200 or ms3 > 200 then fehler := fehler || ('zu langsam: ' || ms1 || ' / ' || ms2 || ' / ' || ms3 || ' ms')::text; end if;

  if array_length(fehler, 1) > 0 then raise exception 'BD-S1 ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
  insert into bd_bericht select jsonb_build_object('ergebnis', 'BD-S1 eingespielt, alle Prüfungen bestanden',
    'referenz_zeilen_gleich', array_length(v_ist, 1), 'alte_bewertungen_verglichen', (select jsonb_object_agg(antworttyp, c) from (select antworttyp, count(*) c from bd_alt group by 1) q),
    'mischstaende', v_misch, 'constraint', v_c, 'bewertungsweg_als', v_weg, 'direktaufruf_gesperrt_fuer', v_gesperrt,
    'ms_meiste_knoten', ms1, 'ms_grosse_brueche', ms2, 'ms_potenzen_und_ausnahme', ms3, 'antwort_grosse_brueche', v_r2);
end $pruef$;
select b from bd_bericht;""")


if __name__ == '__main__':
    main()
