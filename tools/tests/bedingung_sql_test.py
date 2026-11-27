"""Vergleich Python-Referenz gegen die Datenbank-Fassung des Antworttyps „bedingung“.

Erzeugt ein SQL, das die Funktionen aus der Migration BD-S1 NUR in pg_temp anlegt (nichts bleibt in der Datenbank),
dieselben Antworten bewertet und je Aufgabe eine Prüfsumme liefert. Dieselben Prüfsummen rechnet dieses Skript mit
tools/bedingung.py. Stimmen alle Zeilen überein, liefern beide Fassungen für alle Fälle dasselbe.

Aufruf:  python3 -I tools/tests/bedingung_sql_test.py sql  [alles]  > lauf.sql     (SQL für die Datenbank)
         python3 -I tools/tests/bedingung_sql_test.py soll [alles]                 (Soll-Zeilen der Referenz)
Zeilen:  aufgabe <id> <Anzahl> <Prüfsumme>   Bewertung aller Fälle der Aufgabe und von N Antworten aus einem festen Vorrat
         form <Anzahl> <Prüfsumme>            Urteil „zulässig oder nicht“ für alle Aufgaben und alle unzulässigen Fälle
         zeit <ms je Bewertung>               nur SQL: teuerste zulässige Aufgabe (8 Bedingungen, alle durchlaufen, Hinweis am Ende)
Nicht erfasst: der Einbau in schule.antwort_bewerten, die Rechte, der Constraint – das geht nur mit der echten Migration.
Ohne „alles“ läuft eine Auswahl, in der jede Operation und jeder Sonderfall vorkommt (das SQL bleibt klein genug für einen Aufruf);
mit „alles“ alle Muster-Aufgaben und alle Aufgaben des Typs aus inhalte/mathe-profi/rollend-1.
"""
import hashlib
import json
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
WURZEL = HIER.parent.parent
sys.path.insert(0, str(HIER.parent))
import bedingung  # noqa: E402

N = 400
OHNE = ('6-K8-1', '7-K8-1', '8-K5-1', '8-K5-2')   # im kurzen Lauf weggelassen: gleiche Operationen wie andere Aufgaben
VORRAT = ["0", "1", "-1", "2", "-2", "3", "-3", "4", "5", "-5", "6", "7", "8", "-8", "9", "10", "-10", "12", "15", "20", "-20", "25",
          "50", "100", "-100", "999999", "-999999", "1000", "64", "36", "0,5", "-0,5", "2,5", "0,125", "1,25", "-3,75", "1/2", "-1/2",
          "3/4", "2/3", "-7/3", "10/4", "6/3", "1/7", "5/1000", "+3", " − 4 ", "–2", "1 0", "", " ", "abc", "1.5", "1234567", "1/0",
          "2,", ",5", "1,2345", "--1", "+-3", "1/2/3", "+1/2", "3" + " " * 40, None, True, 7, -3, 2.5, 5.0, [1], {"a": 1}]
GANZE = 31   # die ersten 31 Einträge sind brauchbare ganze Zahlen: zwei von drei Zufallsantworten nehmen nur sie


def baum_ops(b, aus):
    if isinstance(b, list):
        aus.add(b[0])
        for x in b[1:]:
            baum_ops(x, aus)


def ops(a):
    aus = set()
    for b in a['o']['bedingungen']:
        baum_ops(b.get('pruefe'), aus)
        baum_ops(b.get('zeige'), aus)
    return aus


MESS = ["25/2", "7/3", "2,5", "9/4", "5", "11/2"]   # Antwort für die Zeitmessung: sieben Bedingungen bestehen, die achte scheitert


def teuer():
    """Teuerste zulässige Aufgabe: 6 Felder, 8 Bedingungen. Sieben mit 60 Knoten, die achte scheitert bei MESS und rechnet den Hinweis (30 + 30)."""
    block = ["+", ["*", "$1", "$2", "$3", 1, 1, 1], ["+", "$4", "$5", "$6", 1], 1]              # 14 Knoten
    beds = [{"name": f"b{i}", "pruefe": [">", ["+"] + [block] * 4 + [1], -999999]} for i in range(1, 8)]   # je 60 Knoten
    beds.append({"name": "b8", "pruefe": ["<", ["+", block, ["+", ["+", "$1", "$2", "$3", "$4", "$5", "$6"], "$1", "$2", "$3", "$4"], 1], 100],
                 "zeige": ["+", block, block, 1], "hinweis": "Bei dir kommt {} heraus."})
    a = {"id": "teuer", "f": {"felder": [{"art": "rational"}] * 6}, "o": {"bedingungen": beds, "beispiel": [1, 1, 1, 1, 1, 1]}}
    assert [bedingung.knoten(b["pruefe"]) + (bedingung.knoten(b["zeige"]) if "zeige" in b else 0) for b in beds] == [60] * 8
    assert not bedingung.pruefe_aufgabe(a, nur_form=True)
    r = bedingung.bewerte(a, {"werte": MESS})
    assert r.get("verletzt") == "b8" and "hinweis" in r, r
    return a


def aufgaben(alles):
    daten = bedingung.lade_json((HIER / 'bedingung_faelle.json').read_text(encoding='utf-8'))   # exakt, wie die Datenbank
    auf = [{'id': a['id'], 'f': {'felder': a['f']['felder']}, 'o': a['o']} for a in daten['aufgaben'] if alles or a['id'] not in OHNE]
    da = set().union(*[ops(a) for a in auf])
    for datei in sorted((WURZEL / 'inhalte/mathe-profi/rollend-1').glob('*.json')):
        for i, x in enumerate(bedingung.lade_json(datei.read_text(encoding='utf-8'))['aufgaben']):
            a = x['aufgabe']
            if a.get('y') == 'bedingung' and (alles or ops(a) - da):
                da |= ops(a)
                auf.append({'id': f'{datei.stem}-{i}', 'f': {'felder': a['f']['felder']}, 'o': a['o']})
    auf.append(teuer())
    fehlt = set(bedingung.OPS) - set().union(*[ops(a) for a in auf])
    assert not fehlt, f'Operation ohne Prüf-Fall: {fehlt}'
    for a in auf:
        assert not bedingung.pruefe_aufgabe(a, nur_form=a['id'] == 'teuer'), (a['id'], bedingung.pruefe_aufgabe(a))
    extra = {}
    for fall in daten['format']:
        extra.setdefault(fall['aufgabe'], []).append(fall['antwort'])
    for fall in daten['hinweise']:
        extra.setdefault(fall['aufgabe'], []).append({'werte': fall['werte']})
    return auf, extra, [u['aufgabe'] for u in daten['unzulaessig']]


def fest(a):
    o = a['o']
    return [o['beispiel']] + list(o.get('gut') or []) + [g['werte'] for g in o.get('gegenbeispiele') or []]


def antworten(a):
    k = len(a['f']['felder'])
    aus = [{'werte': w} for w in fest(a)]
    for j in range(N):
        aus.append({'werte': [VORRAT[(j * 7 + i * 13 + (j // 5) * (i + 1) * 3 + j * j) % (GANZE if j % 3 else len(VORRAT))] for i in range(k)]})
    return aus + [{'werte': []}, {'werte': ['1'] * (k + 1)}, {}, {'werte': None}, {'werte': '1'}]


def kanon(r):
    return '|'.join([str(r.get('format_ok')).lower(), str(r.get('richtig')).lower() if 'richtig' in r else '', r.get('verletzt', ''), r.get('hinweis', '')])


def main():
    alles = 'alles' in sys.argv[2:]
    auf, extra, unzu = aufgaben(alles)
    unzu = [{'f': {'felder': (u.get('f') or {}).get('felder')}, 'o': {k: v for k, v in (u.get('o') or {}).items() if k in ('bedingungen', 'beispiel')}} for u in unzu]
    form = [{'f': a['f'], 'o': a['o']} for a in auf] + unzu
    if sys.argv[1] == 'soll':
        for a in auf:
            zeilen = [kanon(bedingung.bewerte(a, x)) for x in antworten(a) + extra.get(a['id'], [])]
            print('aufgabe', a['id'], len(zeilen), hashlib.md5('\n'.join(zeilen).encode('utf-8')).hexdigest())
        urteil = ['1' if not bedingung.pruefe_aufgabe(x, nur_form=True) else '0' for x in form]
        # Unzulässige Fälle, die nur an fehlenden Gegenbeispielen scheitern, sind für die Datenbank zulässig (sie prüft nur die Form).
        assert urteil[:len(auf)] == ['1'] * len(auf) and urteil.count('0') >= 15, urteil
        print('form', len(urteil), hashlib.md5(''.join(urteil).encode()).hexdigest())
        return
    mig = (WURZEL / 'supabase/migrations/20261201_bd_s1_bedingung_rechner.sql').read_text(encoding='utf-8')
    funk = mig[mig.index('create or replace function'):mig.index('-- Zweig in schule.antwort_bewerten')]
    funk = '\n'.join(z for z in funk.replace('schule.bed_', 'pg_temp.bed_').split('\n') if not z.lstrip().startswith('--'))
    assert 'schule.' not in funk
    klein = [{'id': a['id'], 'felder': a['f']['felder'], 'bed': a['o']['bedingungen'], 'bsp': a['o']['beispiel'], 'fest': fest(a), 'extra': extra.get(a['id'], [])} for a in auf]
    lit = lambda v: "'" + bedingung.schreibe_json(v).replace("'", "''") + "'::jsonb"   # ohne Verlust (Kommazahlen in ihrer Schreibweise)
    print(funk)
    print(f"""create or replace function pg_temp.messen(p_f jsonb, p_b jsonb, p_a jsonb) returns numeric language plpgsql as $$
declare t0 timestamptz := clock_timestamp(); i int; r jsonb;
begin
  for i in 1 .. 200 loop r := pg_temp.bed_bewerten(p_f, p_b, p_a); end loop;
  return round((extract(epoch from clock_timestamp() - t0) * 1000 / 200)::numeric, 2);
end $$;
with a as (select x, o from jsonb_array_elements({lit(klein)}) with ordinality t(x, o)),
vorrat as (select {lit(VORRAT)} as v),
k as (select a.*, jsonb_array_length(x->'felder') as k from a),
faelle as (
  select k.o, 0 as teil, f.o2 as nr, jsonb_build_object('werte', f.w) as antwort from k, jsonb_array_elements(k.x->'fest') with ordinality f(w, o2)
  union all
  select k.o, 1, j, jsonb_build_object('werte', (select jsonb_agg(v->(((j * 7 + i * 13 + (j / 5) * (i + 1) * 3 + j * j) % (case when j % 3 <> 0 then {GANZE} else jsonb_array_length(v) end))::int) order by i)
                                                  from generate_series(0, k.k - 1) i))
    from k, vorrat, generate_series(0, {N - 1}) j
  union all select k.o, 2, 1, '{{"werte":[]}}'::jsonb from k
  union all select k.o, 2, 2, jsonb_build_object('werte', (select jsonb_agg('1'::text) from generate_series(0, k.k) i)) from k
  union all select k.o, 2, 3, '{{}}'::jsonb from k
  union all select k.o, 2, 4, '{{"werte":null}}'::jsonb from k
  union all select k.o, 2, 5, '{{"werte":"1"}}'::jsonb from k
  union all select k.o, 3, e.o2, e.w from k, jsonb_array_elements(k.x->'extra') with ordinality e(w, o2)),
erg as (select f.o, f.teil, f.nr, pg_temp.bed_bewerten(k.x->'felder', k.x->'bed', f.antwort) as r from faelle f join k using (o)),
zeilen as (
  select k.o::int as o, 'aufgabe ' || (k.x->>'id') || ' ' || count(*) || ' ' ||
         md5(string_agg(concat_ws('|', r->>'format_ok', coalesce(r->>'richtig', ''), coalesce(r->>'verletzt', ''), coalesce(r->>'hinweis', '')), E'\\n' order by teil, nr)) as z
  from erg join k using (o) group by k.o, k.x->>'id'
  union all
  select 1000, 'form ' || count(*) || ' ' || md5(string_agg(case when pg_temp.bed_gueltig(f, l) is null then '1' else '0' end, '' order by o))
  from (select o, jsonb_build_object('felder', x->'felder') as f, jsonb_build_object('bedingungen', x->'bed', 'beispiel', x->'bsp') as l from a
        union all select 1000 + o, x->'f', x->'o' from jsonb_array_elements({lit(unzu)}) with ordinality t(x, o)) q
  union all
  select 1001, 'zeit ' || pg_temp.messen(x->'felder', x->'bed', {lit({'werte': MESS})}) from a where x->>'id' = 'teuer')
select string_agg(z, E'\\n' order by o) as ergebnis from zeilen;""")


if __name__ == '__main__':
    main()
