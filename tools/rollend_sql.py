#!/usr/bin/env python3
"""Baut aus den Vorrats-Aufgaben des Mathe-Profis (inhalte/mathe-profi/rollend-*/) das SQL zum Einspielen
in BESTEHENDE, freigegebene Flüge – nur Aufgaben in den alten Antwortformen (ohne den Typ „bedingung“).

Aufruf:  python3 -I tools/rollend_sql.py                 -> Übersicht (prüft alles, schreibt nichts)
         python3 -I tools/rollend_sql.py --sql > x.sql   -> ein SQL für einen Aufruf (eine Transaktion, prüft sich selbst)
Zuordnung Flug -> Einheiten: inhalte/plan/rollend-einheiten.json (aus der Datenbank gelesen, nur Aufbau).
Jede Aufgabe gehört über ihr Lernziel zu genau einer Einheit des Flugs. Nichts wird überschrieben:
schule.aufgaben_einfuegen fügt nur ein, was es (gleiche Frage, gleiche Antworten) in der Einheit noch nicht gibt.
Die Aufgaben kommen als freigegeben hinein (Vorgabe der Tabelle); deshalb: erst Gegenprüfung der Inhalte, dann einspielen.
Nicht ohne den ausdrücklichen Satz des Nutzers ausführen.
"""
import glob
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
FELDER = ('l', 't', 'p', 's', 'g', 'y', 'f', 'a', 'o', 'h', 'w')
ALT = ('auswahl', 'zahl', 'text', 'markierung', 'luecken')


def sammeln():
    plan = json.loads((WURZEL / 'inhalte/plan/rollend-einheiten.json').read_text(encoding='utf-8'))
    je, fehler, zeichn, spaeter = defaultdict(list), [], [], Counter()
    for pfad in sorted(glob.glob(str(WURZEL / 'inhalte/mathe-profi/rollend-*/*.json'))):
        d = json.loads(Path(pfad).read_text(encoding='utf-8'))
        themen = plan['fluege'].get(d['flug'])
        if not themen:
            fehler.append(f'{pfad}: Flug {d["flug"]} ohne Zuordnung'); continue
        for e in d['aufgaben']:
            a, k = e['aufgabe'], e['kennung']
            if a['y'] == 'bedingung':
                spaeter[d['flug']] += 1; continue
            if a['y'] not in ALT: fehler.append(f'{k}: Antworttyp {a["y"]}')
            if a['p'] != 'uebung': fehler.append(f'{k}: Vorrat {a["p"]} statt uebung')
            ziel = [t for t in themen if a['l'] in plan['einheiten'][t]['lz']]
            if len(ziel) != 1:
                fehler.append(f'{k}: Lernziel {a["l"]} passt zu {len(ziel)} Einheiten des Flugs'); continue
            ein = plan['einheiten'][ziel[0]]
            if a['t'] not in ein['tf']: fehler.append(f'{k}: Teilfähigkeit {a["t"]} gibt es in {ziel[0]} nicht')
            if not a.get('h') or not a.get('w'): fehler.append(f'{k}: Tipp oder Lösungsweg fehlt')
            g = a['f'].get('grafik')
            if g is not None:
                zeichn.append((k, ziel[0], g.get('typ')))
                if g.get('typ') not in plan['grafik_typen_bekannt']: fehler.append(f'{k}: Zeichnung vom Typ {g.get("typ")} kennt die App nicht')
            je[ziel[0]].append((k, {f: a[f] for f in FELDER if a.get(f) is not None}))
    doppelt = [k for k, n in Counter(json.dumps(r['f'], sort_keys=True) for v in je.values() for _, r in v).items() if n > 1]
    if doppelt: fehler.append(f'{len(doppelt)} Fragen kommen doppelt vor')
    return plan, je, fehler, zeichn, spaeter


def main():
    plan, je, fehler, zeichn, spaeter = sammeln()
    if fehler:
        print('\n'.join(fehler), file=sys.stderr); sys.exit(1)
    gesamt = sum(len(v) for v in je.values())
    if '--sql' not in sys.argv[1:]:
        for t in sorted(je, key=lambda t: plan['einheiten'][t]['id']):
            print(f'{plan["einheiten"][t]["id"]:>4}  {t:<32} {len(je[t]):>3} Aufgaben  {dict(Counter(r["y"] for _, r in je[t]))}')
        print(f'OK – {gesamt} Aufgaben für {len(je)} Einheiten; {sum(spaeter.values())} des Typs „bedingung“ bleiben liegen; {len(zeichn)} mit Zeichnung:')
        for z in zeichn: print('   ', *z)
        return
    teile = []
    for t in sorted(je, key=lambda t: plan['einheiten'][t]['id']):
        ein, rows = plan['einheiten'][t], []
        for i, (_, r) in enumerate(je[t], 1):
            rows.append(dict(r, r=ein['max_r'] + i))
        js = json.dumps(rows, ensure_ascii=False)
        assert '$auf$' not in js
        teile.append(f"    ({ein['id']}, '{t}', {ein['max_r']}, {len(rows)}, $auf${js}$auf$::jsonb)")
    print(f"""-- Vorrats-Aufgaben (rollend-1, rollend-2) in bestehende Flüge einfügen: {gesamt} Aufgaben, {len(je)} Einheiten. Ein Aufruf, eine Transaktion.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '60s', true);
do $einspielen$
declare e record; n int; vorher int; gesamt int := 0; fehler text[] := '{{}}';
begin
  for e in select * from (values
{(',' + chr(10)).join(teile)}
  ) x(id, schluessel, max_r, soll, aufgaben) loop
    if not exists (select 1 from schule.einheit ei join schule.thema th on th.id = ei.thema_id where ei.id = e.id and th.schluessel = e.schluessel) then
      fehler := fehler || ('Einheit ' || e.id || ' ist nicht ' || e.schluessel)::text; continue; end if;
    if (select coalesce(max(reihenfolge), 0) from schule.aufgabe where einheit_id = e.id and pool = 'uebung') <> e.max_r then
      fehler := fehler || ('Einheit ' || e.id || ': Bestand hat sich seit dem Lesen geändert')::text; continue; end if;
    if exists (select 1 from jsonb_array_elements(e.aufgaben) x where not exists (select 1 from schule.einheit ei, jsonb_array_elements(ei.inhalt->'etappen') et where ei.id = e.id and et->>'lernziel' = x->>'l')) then
      fehler := fehler || ('Einheit ' || e.id || ': Lernziel unbekannt')::text; continue; end if;
    select count(*) into vorher from schule.aufgabe where einheit_id = e.id;
    n := schule.aufgaben_einfuegen(e.id, e.aufgaben);
    if n <> e.soll or (select count(*) from schule.aufgabe where einheit_id = e.id) <> vorher + e.soll then
      fehler := fehler || ('Einheit ' || e.id || ': ' || n || ' statt ' || e.soll || ' eingefügt')::text; end if;
    if exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.reihenfolge > e.max_r and a.pool = 'uebung'
               and not coalesce((schule.antwort_bewerten(a, case a.antworttyp when 'zahl' then jsonb_build_object('wert', '0') else '{{}}'::jsonb end)->>'format_ok') is not null, false)) then
      fehler := fehler || ('Einheit ' || e.id || ': eine neue Aufgabe lässt sich nicht bewerten')::text; end if;
    gesamt := gesamt + n;
  end loop;
  if gesamt <> {gesamt} then fehler := fehler || ('zusammen ' || gesamt || ' statt {gesamt}')::text; end if;
  if array_length(fehler, 1) > 0 then raise exception 'Vorrats-Aufgaben ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
end $einspielen$;
select einheit_id, count(*) filter (where pool = 'uebung') as uebungen from schule.aufgabe where einheit_id in ({', '.join(str(plan['einheiten'][t]['id']) for t in sorted(je, key=lambda t: plan['einheiten'][t]['id']))}) group by 1 order by 1;""")


if __name__ == '__main__':
    main()
