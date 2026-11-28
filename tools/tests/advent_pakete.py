#!/usr/bin/env python3
"""ADVENT-S: Probe- und Einspiel-Paket aus der Migration supabase/migrations/20261209_advent_s.sql.

Aufruf:  python3 -I tools/tests/advent_pakete.py            -> schreibt tools/tests/aus/advent_s_{probe,einspielen}.sql, druckt Größe/md5
         python3 -I tools/tests/advent_pakete.py --pruefen  -> schreibt nichts; Rückgabe 1, wenn die Dateien nicht dem Stand entsprechen

Einspielen = die Migration byteidentisch (ein Aufruf, eine Transaktion, erste Anweisung = Zeitgrenzen).
Probe     = Kopf + Vorher-Erhebung + dieselbe Migration + Bericht; endet ABSICHTLICH mit einem Fehler „ADVENT-S PROBELAUF bestanden …“ -> alles zurückgerollt.
NICHT AUSFÜHREN ohne den ausdrücklichen Satz des Nutzers (der Projektleiter spielt ein).
"""
import hashlib
import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
MIGRATION = WURZEL / 'supabase/migrations/20261209_advent_s.sql'
ZUGAENGE = WURZEL / 'supabase/migrations/20261114_w150_lern_zugaenge_plan.sql'
AUS = WURZEL / 'tools/tests/aus'
BESTAND = ('lern_ich', 'ist_lern', 'wer_tn', 'ist_eltern', 'sieht', 'zugriff')


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def bestand_md5():
    """prosrc-md5 der vorausgesetzten Zugangs-Funktionen, wie 20261114_w150_lern_zugaenge_plan.sql sie anlegt (nie wieder ersetzt)."""
    s = ZUGAENGE.read_text(encoding='utf-8')
    out = {}
    for f in BESTAND:
        m = re.search(r'create or replace function schule\.' + f + r'\(.*?\bas \$\$(.*?)\$\$;', s, re.S)
        assert m, f
        out[f] = md5(m.group(1))
    return out


VORHER = """-- ---------- Probe: Vorher-Stand (nur lesen) ----------
create temp table advent_probe_vorher on commit drop as
  select (select count(*) from pg_class c join pg_namespace n on n.oid = c.relnamespace where n.nspname = 'schule' and c.relname like 'advent\\_%' and c.relkind = 'r') tabellen,
         (select count(*) from pg_proc p join pg_namespace n on n.oid = p.pronamespace where (n.nspname = 'schule' and p.proname like 'advent\\_%')
             or (n.nspname = 'api' and p.proname like 'schule\\_advent\\_%')) funktionen,
         (select count(*) from schule.regel r where r.schluessel like 'advent\\_%') regeln,
         coalesce((select position('''advent''' in pg_get_constraintdef(c.oid)) > 0 from pg_constraint c where c.conrelid = 'schule.sterne'::regclass and c.conname = 'sterne_grund_check'), false) grund_advent,
         (select count(*) from schule.sterne) sterne_zeilen,
         (select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) from schule.sterne x) sterne_md5,
         (select md5(coalesce(string_agg(x::text, '|' order by x.lernender_id, x.einheit_id, x.lernziel collate "C"), '')) from schule.karte_stand x) karte_md5;
"""


def bericht(bm):
    paare = ', '.join(f"'{k}', '{v}'" for k, v in bm.items())
    return """
-- ---------- Probe: Bericht (am Ende absichtlich Fehler -> ALLES zurückgerollt) ----------
do $advent_probe$
declare v record; e jsonb; k jsonb := '[]'::jsonb; r record; befund text[] := '{}'; bm jsonb := jsonb_build_object(""" + paare + """); b jsonb := '{}'::jsonb;
  n_tab int; n_fn int; n_lan int; n_lan_am int; n_lan_fehlt int; kurz text; f text; m text;
begin
  select * into v from advent_probe_vorher;
  e := schule.advent_einstellung();
  select count(*) into n_tab from pg_class c join pg_namespace n on n.oid = c.relnamespace where n.nspname = 'schule' and c.relname like 'advent\\_%' and c.relkind = 'r';
  select count(*) into n_fn from pg_proc p join pg_namespace n on n.oid = p.pronamespace where (n.nspname = 'schule' and p.proname like 'advent\\_%')
     or (n.nspname = 'api' and p.proname like 'schule\\_advent\\_%');
  if n_tab <> 6 or n_fn <> 37 then befund := befund || format('Anzahl Tabellen/Funktionen %s/%s statt 6/37', n_tab, n_fn); end if;
  if (select count(*) from schule.sterne) <> v.sterne_zeilen or (select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) from schule.sterne x) <> v.sterne_md5 then
    befund := befund || 'schule.sterne verändert'::text; end if;
  if (select md5(coalesce(string_agg(x::text, '|' order by x.lernender_id, x.einheit_id, x.lernziel collate "C"), '')) from schule.karte_stand x) <> v.karte_md5 then
    befund := befund || 'schule.karte_stand verändert'::text; end if;
  foreach f in array array['lern_ich', 'ist_lern', 'wer_tn', 'ist_eltern', 'sieht', 'zugriff'] loop
    select md5(p.prosrc) into m from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'schule' and p.proname = f;
    b := b || jsonb_build_object(f, case when m = bm->>f then 'wie Repo' else 'ABWEICHEND ' || coalesce(m, 'fehlt') end);
    if m is distinct from bm->>f then befund := befund || format('Bestandsfunktion schule.%s weicht vom Repo ab (nur Hinweis)', f); end if;
  end loop;
  -- Landungen, die der Kalender erkennt (eigene Landung / „Sitzt wieder!“: landung.am = sitzt_am)
  select count(*) filter (where k2.landung_art is not null and k2.sitzt),
         count(*) filter (where k2.landung_art is not null and k2.sitzt and (k2.landung->>'am')::timestamptz = k2.sitzt_am),
         count(*) filter (where k2.landung_art is not null and k2.sitzt and k2.landung->>'am' is null)
    into n_lan, n_lan_am, n_lan_fehlt from schule.karte_stand k2;
  for r in select l.id, l.ist_test, l.zeitzone, schule.advent_tz(l.id) tz from schule.lernender l where l.aktiv order by l.id loop
    k := k || jsonb_build_object('lernender_id', r.id, 'ist_test', r.ist_test, 'zeitzone', r.zeitzone, 'gueltig', r.tz is not null,
      'ortszeit', case when r.tz is not null then to_char(now() at time zone r.tz, 'YYYY-MM-DD HH24:MI') end,
      'lage', case when r.tz is not null then (schule.advent_lage(r.id) - 'offen_nrs' - 'start' - 'nachholen_bis' - 'sichtbar_bis' - 'jahr' - 'zeitzone' - 'max_pro_tag') end,
      'eigene_landungen_gesamt', (select count(*) from schule.karte_stand x where x.lernender_id = r.id and x.sitzt and x.landung_art is not null
                                     and (x.landung->>'am')::timestamptz = x.sitzt_am));
    if r.tz is null then befund := befund || format('ZEITZONE FEHLT/UNGÜLTIG: lernender %s (%s) – Kalender liefert „zeitzone_fehlt“', r.id, coalesce(r.zeitzone, 'leer')); end if;
  end loop;
  kurz := format('Tabellen %s (vorher %s), Funktionen %s (vorher %s), Regeln advent_* %s (vorher %s), Grund advent %s, Schalter aktiv=%s tausch=%s, Start %s, Nachholen bis %s, sichtbar bis %s, max %s/Tag, Kinder %s (Zeitzone fehlt: %s), Landungen erkannt %s von %s',
    n_tab, v.tabellen, n_fn, v.funktionen, (select count(*) from schule.regel r2 where r2.schluessel like 'advent\\_%'), v.regeln,
    case when v.grund_advent then 'schon da' else 'neu' end, e->>'aktiv', e->>'tausch', e->>'start', e->>'nachholen_bis', e->>'sichtbar_bis', e->>'max_pro_tag',
    jsonb_array_length(k), (select count(*) from jsonb_array_elements(k) x where not (x->>'gueltig')::boolean), n_lan_am, n_lan);
  raise exception 'ADVENT-S PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt). KURZ: % | BEFUNDE (%): % | DETAILS: %', kurz, coalesce(array_length(befund, 1), 0),
    coalesce(array_to_string(befund, ' | '), 'keine'),
    jsonb_build_object('einstellung', e, 'kinder', k, 'bestand_md5', b, 'landungen_ohne_am', n_lan_fehlt, 'sterne_unveraendert', true, 'lernpause_noetig', false)::text;
end $advent_probe$;
"""


def pakete():
    mig = MIGRATION.read_text(encoding='utf-8')
    kopf = ('-- ADVENT-S PROBELAUF (rollt am Ende ALLES zurück, nichts eingespielt). Erzeugt von tools/tests/advent_pakete.py aus ' + MIGRATION.name + '.\n'
            '-- Ein Aufruf, eine Transaktion. Bericht = die abschließende Fehlermeldung (vorn KURZ, dann BEFUNDE, dann DETAILS).\n')
    nach_vor = mig.index('end $advent_vor$;\n') + len('end $advent_vor$;\n')     # Vorher-Stand erst nach der Prüfung des Vorzustands
    probe = kopf + mig[:nach_vor] + VORHER + mig[nach_vor:] + bericht(bestand_md5())
    return {'advent_s_probe.sql': probe, 'advent_s_einspielen.sql': mig}


def main():
    pr = '--pruefen' in sys.argv
    ok = True
    for name, text in pakete().items():
        p = AUS / name
        if pr:
            if not p.exists() or p.read_text(encoding='utf-8') != text:
                print(f'{name}: nicht auf dem Stand', file=sys.stderr); ok = False
        else:
            p.write_text(text, encoding='utf-8')
        b = text.encode('utf-8')
        print(f'{name}: {len(b)} Bytes, md5 {hashlib.md5(b).hexdigest()}')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
