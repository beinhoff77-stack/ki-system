#!/usr/bin/env python3
"""Baut aus den Vorrats-Aufgaben des Mathe-Profis (inhalte/mathe-profi/rollend-*/) das SQL zum Einspielen
in BESTEHENDE, freigegebene Flüge – Aufgaben in den alten Antwortformen; den Typ „bedingung“ nur mit --mit-bedingung.

Aufruf:  python3 -I tools/rollend_sql.py                 -> Übersicht (prüft alles, schreibt nichts)
         python3 -I tools/rollend_sql.py --sql > x.sql   -> ein SQL für einen Aufruf (eine Transaktion, prüft sich selbst)
         --mit-bedingung                                 -> auch Aufgaben mit y = bedingung (Vorgabe: aus – erst, wenn die App sie anzeigen kann)
         --runden 1,2,3,4 | 5 | 7,8 | alle               -> welche Runden (Vorgabe: 1,2,3,4 = Altbestand, wie bisher); Pakete getrennt einspielen
         --ohne K5A-V009,K8-V070                         -> einzelne Kennungen herausnehmen (unbekannte Kennung = Fehler)
Zwei Dateiformate: Runden 1-4 über den Flug (Kopf „flug“, Zuordnung „fluege“ in rollend-einheiten.json, Lernziel -> Einheit, bei Gleichstand
Feld „thema“); Runden ab 5 über das Feld „thema“ jeder Aufgabe = Schlüssel der Einheit („einheiten“ in rollend-einheiten.json; Lernkarte muss
in „lz“ der Einheit stehen, Teilfähigkeit t in „tf“). „form“: Feld „form“ der Aufgabe, sonst aus „typ“; beides, dann müssen sie zusammenpassen.
Reihenfolge-Nummern (Spalte reihenfolge, Vorrat uebung): Runden 1-4 = max_r + Platz der Aufgabe unter ALLEN Aufgaben der Einheit in den Runden 1-4
(Runde 1, 2, 3, 4, Dateireihenfolge; auch herausgenommene und liegen gebliebene zählen mit – die Nummern ändern sich durch --ohne/--runden nicht);
Runde R ab 5 = max_r + 1000·R + Platz in der Runde. Dadurch überschneiden sich Pakete nie, auch wenn mehrere Runden dieselbe Einheit treffen,
und die Reihenfolge des Einspielens ist egal (das SQL prüft: Bestand bis max_r unverändert, Nummern des Pakets noch frei).
Zuordnung Flug -> Einheiten: inhalte/plan/rollend-einheiten.json (aus der Datenbank gelesen, nur Aufbau). Flüge ohne Zuordnung dort
werden übersprungen und als „ohne Zuordnung“ aufgelistet (kein Abbruch).
Jede Aufgabe gehört über ihr Lernziel zu genau einer Einheit des Flugs; ist das Lernziel in zwei Einheiten gleich benannt (ge1: „verstehen“), entscheidet das Feld „thema“ der Aufgabe. Nichts wird überschrieben:
schule.aufgaben_einfuegen fügt nur ein, was es (gleiche Frage, gleiche Antworten) in der Einheit noch nicht gibt.
FT-S (Form-Takt, inhalte/plan/form-takt.md Regel 1): Feld „typ“ der Dateien -> form (acht Werte), Feld „zaehlt“ -> zaehlt (ja/nein);
beides geht ins JSON für schule.aufgaben_einfuegen (setzt die Migration 20261203_ft_s_form_takt.sql voraus – das SQL prüft das).
zaehlt = folge gibt es nicht mehr: in der Übersicht als OFFEN gemeldet, mit --sql Abbruch mit Meldung, bis ja oder nein gesetzt ist.
Die Aufgaben kommen als freigegeben hinein (Vorgabe der Tabelle); deshalb: erst Gegenprüfung der Inhalte, dann einspielen.
Nicht ohne den ausdrücklichen Satz des Nutzers ausführen.
"""
import glob
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
FELDER = ('l', 't', 'p', 's', 'g', 'y', 'f', 'a', 'o', 'h', 'w')
ALT = ('auswahl', 'zahl', 'text', 'markierung', 'luecken')
ALTRUNDEN = (1, 2, 3, 4)  # Dateiformat mit „flug“; alle anderen Runden: Zuordnung über das Feld „thema“ jeder Aufgabe
BLOCK = 1000              # Runde R >= 5 nummeriert ab max_r + BLOCK * R
FORMEN = ('lueckenweg', 'fehler_detektiv', 'verfahren_waehlen', 'zwei_wege', 'umkehren', 'bruecke', 'anwenden', 'viele_antworten')
FORM = {'Lückenweg': 'lueckenweg', 'Fehler-Detektiv (einfache Form)': 'fehler_detektiv', 'Verfahren wählen (einfache Form)': 'verfahren_waehlen',
        'Fehler-Detektiv': 'fehler_detektiv', 'Verfahren wählen': 'verfahren_waehlen',
        'Zwei Wege vergleichen': 'zwei_wege', 'Umkehren': 'umkehren', 'Brücke': 'bruecke', 'Anwenden': 'anwenden',
        'Viele richtige Antworten (bedingung)': 'viele_antworten'}


def runde_von(pfad):
    m = re.search(r'rollend-(\d+)', pfad)
    return int(m.group(1)) if m else None


def sammeln(mit_bedingung=False, runden=ALTRUNDEN, ohne_kennungen=()):
    """Liest alle Runden (für Doppelt-Prüfung und Nummern), prüft und liefert nur die gewählten.
    Rückgabe: plan, je (Einheit -> [(kennung, zeile)]), fehler, zeichn, spaeter, ohne, folge, stat (je Runde), heraus"""
    plan = json.loads((WURZEL / 'inhalte/plan/rollend-einheiten.json').read_text(encoding='utf-8'))
    je, fehler, zeichn, spaeter, ohne, folge = defaultdict(list), [], [], Counter(), [], []
    stat = {r: {'n': 0, 'einheiten': set(), 'form': Counter(), 'zaehlt': Counter(), 't_abw': [], 'ohne': 0, 'bedingung': 0, 'heraus': 0} for r in runden}
    if mit_bedingung:
        sys.path.insert(0, str(WURZEL / 'tools'))
        import bedingung
    runden, ohne_kennungen = set(runden), set(ohne_kennungen)
    alle_k, alle_f = defaultdict(list), defaultdict(list)  # Kennung / Frage -> [(Runde, Einheit)] über ALLE Runden
    slots = defaultdict(int)     # (Runde, Einheit) -> Zahl aller Aufgaben dort (auch herausgenommene)
    gesehen = set()
    pfade = sorted(glob.glob(str(WURZEL / 'inhalte/mathe-profi/rollend-*/*.json')), key=lambda p: (runde_von(p) or 0, p))
    for pfad in pfade:
        runde = runde_von(pfad)
        if runde is None: continue
        rel = Path(pfad).relative_to(WURZEL).as_posix()
        d = json.loads(Path(pfad).read_text(encoding='utf-8'))
        gewaehlt = runde in runden
        alt = runde in ALTRUNDEN
        flug = d.get('flug') or d.get('thema') or '?'
        themen = plan['fluege'].get(flug) if alt else None
        if alt and not themen:
            if gewaehlt:
                ohne.append((rel, flug, len(d['aufgaben']))); stat[runde]['ohne'] += len(d['aufgaben'])
            continue
        for e in d['aufgaben']:
            a, k = e['aufgabe'], e['kennung']
            gesehen.add(k)
            alle_k[k].append(runde)
            alle_f[json.dumps(a['f'], sort_keys=True)].append((runde, k))
            # Einheit bestimmen (auch für nicht gewählte Aufgaben, damit die Nummern stabil bleiben)
            msg = None
            if alt:
                ziel = [t for t in themen if a['l'] in plan['einheiten'][t]['lz']]
                if len(ziel) > 1 and e.get('thema') in ziel:  # gleiche Lernkarte in zwei Einheiten eines Flugs (ge1: „verstehen“): Feld „thema“ der Aufgabe entscheidet
                    ziel = [e['thema']]
                if len(ziel) != 1: msg = f'{k}: Lernziel {a["l"]} passt zu {len(ziel)} Einheiten des Flugs'
                else: ziel = ziel[0]
            else:
                th = e.get('thema')
                if th not in plan['einheiten']: msg = f'{k}: thema „{th}“ steht nicht in „einheiten“ von rollend-einheiten.json'
                elif a['l'] not in plan['einheiten'][th]['lz']: msg = f'{k}: Lernkarte {a["l"]} gehört nicht zur Einheit {th} (lz: {", ".join(plan["einheiten"][th]["lz"])})'
                else: ziel = th
            if msg is None:
                slots[(runde, ziel)] += 1
                slot = slots[(runde, ziel)]
            if not gewaehlt: continue
            if msg is not None:
                fehler.append(msg); continue
            if k in ohne_kennungen:
                stat[runde]['heraus'] += 1; continue
            if a['y'] == 'bedingung' and not mit_bedingung:
                spaeter[flug] += 1; stat[runde]['bedingung'] += 1; continue
            form = e.get('form') if e.get('form') is not None else FORM.get(e.get('typ'))
            if e.get('form') is None and form is None: fehler.append(f'{k}: Form „{e.get("typ")}“ unbekannt (erlaubt: {", ".join(FORM)})')
            elif form not in FORMEN: fehler.append(f'{k}: form „{form}“ unbekannt (erlaubt: {", ".join(FORMEN)})')
            elif e.get('form') is not None and e.get('typ') in FORM and FORM[e['typ']] != form:
                fehler.append(f'{k}: form „{form}“ passt nicht zu typ „{e["typ"]}“ ({FORM[e["typ"]]})')
            if e.get('zaehlt') == 'folge': folge.append(k)
            elif e.get('zaehlt') not in ('ja', 'nein'): fehler.append(f'{k}: zaehlt „{e.get("zaehlt")}“ (erlaubt: ja, nein)')
            if a['y'] == 'bedingung':
                for f in bedingung.pruefe_aufgabe(a): fehler.append(f'{k}: {f}')
            elif a['y'] not in ALT: fehler.append(f'{k}: Antworttyp {a["y"]}')
            if a['p'] != 'uebung': fehler.append(f'{k}: Vorrat {a["p"]} statt uebung')
            ein = plan['einheiten'][ziel]
            if a['t'] not in ein['tf']:
                fehler.append(f'{k}: Teilfähigkeit {a["t"]} gibt es in {ziel} nicht (tf: {", ".join(ein["tf"])})'); stat[runde]['t_abw'].append(k)
            if not a.get('h') or not a.get('w'): fehler.append(f'{k}: Tipp oder Lösungsweg fehlt')
            g = a['f'].get('grafik')
            if g is not None:
                zeichn.append((k, ziel, g.get('typ')))
                if g.get('typ') not in plan['grafik_typen_bekannt']: fehler.append(f'{k}: Zeichnung vom Typ {g.get("typ")} kennt die App nicht')
            r = {f: a[f] for f in FELDER if a.get(f) is not None}
            r['form'], r['zaehlt'] = form, e.get('zaehlt')
            je[ziel].append((k, r, runde, slot))
            st = stat[runde]; st['n'] += 1; st['einheiten'].add(ziel); st['form'][form] += 1; st['zaehlt'][e.get('zaehlt')] += 1
    for k in ohne_kennungen - gesehen: fehler.append(f'--ohne {k}: Kennung gibt es in keiner Runde')
    for k, rr in alle_k.items():
        if len(rr) > 1 and runden & set(rr): fehler.append(f'Kennung {k} kommt {len(rr)}-mal vor (Runden {sorted(set(rr))})')
    doppelt = [v for v in alle_f.values() if len(v) > 1 and runden & {r for r, _ in v}]
    if doppelt:
        fehler.append(f'{len(doppelt)} Fragen kommen doppelt vor (auch über Runden): ' + '; '.join('/'.join(k for _, k in v) for v in doppelt[:10]))
    # Nummern: Altrunden hinter allen früheren Altrunden derselben Einheit, Runde R >= 5 im eigenen Block
    for t, zeilen in je.items():
        mr = plan['einheiten'][t]['max_r']
        for i, (k, r, runde, slot) in enumerate(zeilen):
            if slot >= BLOCK: fehler.append(f'{k}: mehr als {BLOCK} Aufgaben in einer Runde und Einheit')
            vorher = sum(n for (rr, tt), n in slots.items() if tt == t and rr in ALTRUNDEN and rr < runde) if runde in ALTRUNDEN else BLOCK * runde
            r['r'] = mr + vorher + slot
    return plan, {t: [(k, r) for k, r, _, _ in v] for t, v in je.items()}, fehler, zeichn, spaeter, ohne, folge, stat


def optionen(argv):
    def wert(name):
        for i, x in enumerate(argv):
            if x == name:
                if i + 1 >= len(argv): sys.exit(f'{name} braucht einen Wert')
                return argv[i + 1]
            if x.startswith(name + '='): return x.split('=', 1)[1]
        return None
    rw = wert('--runden')
    if rw is None: runden = ALTRUNDEN
    elif rw == 'alle': runden = tuple(sorted({runde_von(p) for p in glob.glob(str(WURZEL / 'inhalte/mathe-profi/rollend-*/*.json'))} - {None}))
    else:
        try: runden = tuple(sorted({int(x) for x in rw.split(',') if x.strip()}))
        except ValueError: sys.exit(f'--runden: „{rw}“ ist keine Liste von Rundennummern (z. B. 1,2,3,4 oder 5 oder alle)')
        if not runden: sys.exit('--runden: leer')
    ow = wert('--ohne')
    return runden, (tuple(x.strip() for x in ow.split(',') if x.strip()) if ow else ())


def main():
    argv = sys.argv[1:]
    mit_bedingung = '--mit-bedingung' in argv
    sql = '--sql' in argv
    runden, ohne_k = optionen(argv)
    plan, je, fehler, zeichn, spaeter, ohne, folge, stat = sammeln(mit_bedingung, runden, ohne_k)
    gesamt = sum(len(v) for v in je.values())
    aus = sys.stderr if sql else sys.stdout
    if not sql:
        for t in sorted(je, key=lambda t: plan['einheiten'][t]['id']):
            print(f'{plan["einheiten"][t]["id"]:>4}  {t:<32} {len(je[t]):>3} Aufgaben  {dict(Counter(r["y"] for _, r in je[t]))}')
    print(f'Runden {",".join(map(str, runden))}' + (f', ohne {",".join(ohne_k)}' if ohne_k else '') + ':', file=aus)
    for rn in runden:
        st = stat[rn]
        print(f'  Runde {rn}: {st["n"]} Aufgaben, {len(st["einheiten"])} Einheiten; Form {dict(st["form"])}; zaehlt {dict(st["zaehlt"])}; '
              f'Teilfähigkeit nicht in tf: {len(st["t_abw"])}' + (f'; herausgenommen: {st["heraus"]}' if st['heraus'] else '')
              + (f'; „bedingung“ liegen geblieben: {st["bedingung"]}' if st['bedingung'] else '') + (f'; ohne Zuordnung: {st["ohne"]}' if st['ohne'] else ''), file=aus)
        if st['t_abw']: print(f'    t nicht in tf bei: {", ".join(st["t_abw"])}', file=sys.stderr)
    if fehler:
        print('\n'.join(fehler), file=sys.stderr); sys.exit(1)
    if not sql:
        print(f'OK – {gesamt} Aufgaben für {len(je)} Einheiten; '
              + ('Typ „bedingung“ eingeschlossen' if mit_bedingung else f'{sum(spaeter.values())} des Typs „bedingung“ bleiben liegen')
              + f'; {len(zeichn)} mit Zeichnung:')
        for z in zeichn: print('   ', *z)
        alle = [r for v in je.values() for _, r in v]
        print(f'Form: {dict(Counter(r["form"] for r in alle))}')
        print(f'zaehlt: {dict(Counter(r["zaehlt"] for r in alle))}')
        if folge: print(f'OFFEN (vor --sql klären): zaehlt = folge bei {", ".join(folge)} – auf ja oder nein setzen (form-takt.md Regel 1)')
        if ohne:
            print(f'Ohne Zuordnung (übersprungen, Flug fehlt in inhalte/plan/rollend-einheiten.json): {len(ohne)} Flüge, {sum(o[2] for o in ohne)} Aufgaben')
            for o in ohne: print('   ', *o)
        return
    if folge:
        print(f'ABBRUCH: zaehlt = folge gibt es nicht mehr (form-takt.md Regel 1) – erst auf ja oder nein setzen: {", ".join(folge)}', file=sys.stderr)
        sys.exit(1)
    if not gesamt:
        print('ABBRUCH: keine Aufgaben gewählt', file=sys.stderr); sys.exit(1)
    teile = []
    ids = sorted(je, key=lambda t: plan['einheiten'][t]['id'])
    for t in ids:
        ein = plan['einheiten'][t]
        rows = [r for _, r in je[t]]
        js = json.dumps(rows, ensure_ascii=False)
        assert '$auf$' not in js
        teile.append(f"    ({ein['id']}, '{t}', {ein['max_r']}, {len(rows)}, $auf${js}$auf$::jsonb)")
    rset = "(select (x->>'r')::int from jsonb_array_elements(e.aufgaben) x)"
    print(f"""-- Vorrats-Aufgaben (rollend-{','.join(map(str, runden))}) in bestehende Flüge einfügen: {gesamt} Aufgaben, {len(je)} Einheiten, mit form und zaehlt (FT-S). Ein Aufruf, eine Transaktion.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '60s', true);
do $einspielen$
declare e record; n int; vorher int; gesamt int := 0; fehler text[] := '{{}}';
begin
  if (select count(*) from pg_attribute where attrelid = 'schule.aufgabe'::regclass and attname in ('form', 'zaehlt') and not attisdropped) <> 2
     or position('x->>''form''' in pg_get_functiondef('schule.aufgaben_einfuegen(bigint, jsonb)'::regprocedure)) = 0 then
    raise exception 'Vorrats-Aufgaben: erst FT-S einspielen (Spalten form/zaehlt, aufgaben_einfuegen)'; end if;
  for e in select * from (values
{(',' + chr(10)).join(teile)}
  ) x(id, schluessel, max_r, soll, aufgaben) loop
    if not exists (select 1 from schule.einheit ei join schule.thema th on th.id = ei.thema_id where ei.id = e.id and th.schluessel = e.schluessel) then
      fehler := fehler || ('Einheit ' || e.id || ' ist nicht ' || e.schluessel)::text; continue; end if;
    if (select coalesce(max(reihenfolge), 0) from schule.aufgabe where einheit_id = e.id and pool = 'uebung' and reihenfolge <= e.max_r) <> e.max_r then
      fehler := fehler || ('Einheit ' || e.id || ': Bestand hat sich seit dem Lesen geändert')::text; continue; end if;
    if exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'uebung' and a.reihenfolge in {rset}) then
      fehler := fehler || ('Einheit ' || e.id || ': Reihenfolge-Nummern des Pakets sind schon belegt (Paket schon eingespielt?)')::text; continue; end if;
    if exists (select 1 from jsonb_array_elements(e.aufgaben) x where not exists (select 1 from schule.einheit ei, jsonb_array_elements(ei.inhalt->'etappen') et where ei.id = e.id and et->>'lernziel' = x->>'l')) then
      fehler := fehler || ('Einheit ' || e.id || ': Lernziel unbekannt')::text; continue; end if;
    select count(*) into vorher from schule.aufgabe where einheit_id = e.id;
    n := schule.aufgaben_einfuegen(e.id, e.aufgaben);
    if n <> e.soll or (select count(*) from schule.aufgabe where einheit_id = e.id) <> vorher + e.soll then
      fehler := fehler || ('Einheit ' || e.id || ': ' || n || ' statt ' || e.soll || ' eingefügt')::text; end if;
    if (select count(*) from schule.aufgabe a where a.einheit_id = e.id and a.reihenfolge in {rset} and a.pool = 'uebung' and a.form is not null and a.zaehlt is not null) <> e.soll then
      fehler := fehler || ('Einheit ' || e.id || ': form/zaehlt nicht übernommen')::text; end if;
    if exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.reihenfolge in {rset} and a.pool = 'uebung'
               and not coalesce((schule.antwort_bewerten(a, case a.antworttyp when 'zahl' then jsonb_build_object('wert', '0') else '{{}}'::jsonb end)->>'format_ok') is not null, false)) then
      fehler := fehler || ('Einheit ' || e.id || ': eine neue Aufgabe lässt sich nicht bewerten')::text; end if;
    gesamt := gesamt + n;
  end loop;
  if gesamt <> {gesamt} then fehler := fehler || ('zusammen ' || gesamt || ' statt {gesamt}')::text; end if;
  if array_length(fehler, 1) > 0 then raise exception 'Vorrats-Aufgaben ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
end $einspielen$;
select einheit_id, count(*) filter (where pool = 'uebung') as uebungen, count(*) filter (where form is not null) as mit_form from schule.aufgabe where einheit_id in ({', '.join(str(plan['einheiten'][t]['id']) for t in ids)}) group by 1 order by 1;""")


if __name__ == '__main__':
    main()
