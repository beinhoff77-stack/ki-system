"""Vergleich Python-Referenz gegen die Datenbank-Fassung des Antworttyps „bedingung“.

Erzeugt ein SQL, das die Funktionen aus der Migration BD-S1 NUR in pg_temp anlegt (nichts bleibt in der Datenbank),
dieselben Antworten bewertet und je Aufgabe eine Prüfsumme liefert. Dieselben Prüfsummen rechnet dieses Skript mit
tools/bedingung.py. Stimmen alle überein, liefern beide Fassungen für alle Fälle dasselbe.

Aufruf:  python3 -I tools/tests/bedingung_sql_test.py sql   > lauf.sql     (SQL für die Datenbank)
         python3 -I tools/tests/bedingung_sql_test.py soll                 (Prüfsummen der Referenz)
Die Antworten: alle Fälle aus bedingung_faelle.json und je Aufgabe N Antworten aus einem festen Vorrat nach fester Formel.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent))
import bedingung  # noqa: E402

N = 600
VORRAT = ["0", "1", "-1", "2", "-2", "3", "-3", "4", "5", "-5", "6", "7", "8", "-8", "9", "10", "-10", "12", "15", "20", "-20", "25",
          "50", "100", "-100", "999999", "-999999", "1000", "64", "36", "0,5", "-0,5", "2,5", "0,125", "1,25", "-3,75", "1/2", "-1/2",
          "3/4", "2/3", "-7/3", "10/4", "6/3", "1/7", "5/1000", "+3", " − 4 ", "–2", "1 0", "", " ", "abc", "1.5", "1234567", "1/0",
          "2,", ",5", "1,2345", "--1", "1/2/3", None, True, 7, -3, 2.5]


def antworten(a):
    k = len(a['f']['felder'])
    o = a['o']
    aus = [{'werte': w} for w in [o['beispiel']] + list(o.get('gut') or []) + [g['werte'] for g in o.get('gegenbeispiele') or []]]
    for j in range(N):
        aus.append({'werte': [VORRAT[(j * 7 + i * 13 + (j // 5) * (i + 1) * 3 + j * j) % (31 if j % 3 else len(VORRAT))] for i in range(k)]})
    aus += [{'werte': []}, {'werte': ['1'] * (k + 1)}, {}, {'werte': None}, {'werte': '1'}]
    return aus


def kanon(r):
    return '|'.join([str(r.get('format_ok')).lower(), str(r.get('richtig')).lower() if 'richtig' in r else '', r.get('verletzt', ''), r.get('hinweis', '')])


def main():
    daten = json.loads((HIER / 'bedingung_faelle.json').read_text(encoding='utf-8'))
    auf = [{'id': a['id'], 'f': {'felder': a['f']['felder']}, 'o': a['o']} for a in daten['aufgaben']]
    extra = {}
    for fall in daten['format']:
        extra.setdefault(fall['aufgabe'], []).append(fall['antwort'])
    for fall in daten['hinweise']:
        extra.setdefault(fall['aufgabe'], []).append({'werte': fall['werte']})
    if sys.argv[1:] == ['soll']:
        for a in auf:
            zeilen = [kanon(bedingung.bewerte(a, x)) for x in antworten(a) + extra.get(a['id'], [])]
            print(a['id'], len(zeilen), hashlib.md5('\n'.join(zeilen).encode('utf-8')).hexdigest())
        return
    mig = (HIER.parent.parent / 'supabase/migrations/20261201_bd_s1_bedingung_rechner.sql').read_text(encoding='utf-8')
    funk = mig[mig.index('create or replace function'):mig.index('-- Zweig in schule.antwort_bewerten')]
    funk = funk.replace('schule.bed_', 'pg_temp.bed_')
    assert 'schule.' not in funk
    klein = [{'id': a['id'], 'felder': a['f']['felder'], 'bed': a['o']['bedingungen'],
              'fest': [x['werte'] for x in antworten(a)[:-(N + 5)]], 'extra': extra.get(a['id'], [])} for a in auf]
    lit = lambda v: "'" + json.dumps(v, ensure_ascii=False, separators=(',', ':')).replace("'", "''") + "'::jsonb"
    print(funk)
    print(f"""
with a as (select x, o from jsonb_array_elements({lit(klein)}) with ordinality t(x, o)),
vorrat as (select {lit(VORRAT)} as v),
k as (select a.*, jsonb_array_length(x->'felder') as k from a),
faelle as (
  select k.o, 0 as teil, f.o2 as nr, jsonb_build_object('werte', f.w) as antwort from k, jsonb_array_elements(k.x->'fest') with ordinality f(w, o2)
  union all
  select k.o, 1, j, jsonb_build_object('werte', (select jsonb_agg(v->(((j * 7 + i * 13 + (j / 5) * (i + 1) * 3 + j * j) % (case when j % 3 <> 0 then 31 else jsonb_array_length(v) end))::int) order by i)
                                                  from generate_series(0, k.k - 1) i))
    from k, vorrat, generate_series(0, {N - 1}) j
  union all select k.o, 2, 1, '{{"werte":[]}}'::jsonb from k
  union all select k.o, 2, 2, jsonb_build_object('werte', (select jsonb_agg('1'::text) from generate_series(0, k.k) i)) from k
  union all select k.o, 2, 3, '{{}}'::jsonb from k
  union all select k.o, 2, 4, '{{"werte":null}}'::jsonb from k
  union all select k.o, 2, 5, '{{"werte":"1"}}'::jsonb from k
  union all select k.o, 3, e.o2, e.w from k, jsonb_array_elements(k.x->'extra') with ordinality e(w, o2)),
erg as (select f.o, f.teil, f.nr, pg_temp.bed_bewerten(k.x->'felder', k.x->'bed', f.antwort) as r from faelle f join k using (o))
select k.x->>'id' as id, count(*) as n,
       md5(string_agg(concat_ws('|', r->>'format_ok', coalesce(r->>'richtig', ''), coalesce(r->>'verletzt', ''), coalesce(r->>'hinweis', '')), E'\\n' order by teil, nr)) as summe
from erg join k using (o) group by k.o, k.x->>'id' order by k.o;""")


if __name__ == '__main__':
    main()
