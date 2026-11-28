#!/usr/bin/env python3
"""ADVENT-S: Probe- und Einspiel-Paket aus der Migration supabase/migrations/20261209_advent_s.sql.

Aufruf:  python3 -I tools/tests/advent_pakete.py            -> schreibt tools/tests/aus/advent_s_{probe,einspielen}.sql, druckt Größe/md5
         python3 -I tools/tests/advent_pakete.py --pruefen  -> schreibt nichts; Rückgabe 1, wenn die Dateien nicht dem Stand entsprechen

Einspielen = die Migration byteidentisch (ein Aufruf, eine Transaktion, erste Anweisung = Zeitgrenzen).
Probe     = Kopf + Vorher-Erhebung + dieselbe Migration + Bericht; endet IMMER mit einem Fehler -> alles zurückgerollt: „ADVENT-S PROBELAUF bestanden …
            KURZ {…}“ nur bei 0 Befunden, sonst „ADVENT-S PROBELAUF NICHT bestanden (n Befunde) … KURZ {…}“ und darunter die BEFUNDE.
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


def funktionen_soll():
    """Zahl der Funktionen schule.advent_* und api.schule_advent_*, die die Migration anlegt (die Probe verlangt genau diese Zahl)."""
    s = MIGRATION.read_text(encoding='utf-8')
    return len(set(re.findall(r'(?m)^create or replace function ((?:schule\.advent_|api\.schule_advent_)[a-z_]+)\(', s)))


VORHER = """-- ---------- Probe: Vorher-Stand (nur lesen) ----------
create temp table advent_probe_vorher on commit drop as
  select (select count(*) from pg_class c join pg_namespace n on n.oid = c.relnamespace where n.nspname = 'schule' and c.relname like 'advent\\_%' and c.relkind = 'r') tabellen,
         (select count(*) from pg_proc p join pg_namespace n on n.oid = p.pronamespace where (n.nspname = 'schule' and p.proname like 'advent\\_%')
             or (n.nspname = 'api' and p.proname like 'schule\\_advent\\_%')) funktionen,
         (select count(*) from schule.regel r where r.schluessel like 'advent\\_%') regeln,
         coalesce((select position('''advent''' in pg_get_constraintdef(c.oid)) > 0 from pg_constraint c where c.conrelid = 'schule.sterne'::regclass and c.conname = 'sterne_grund_check'), false) grund_advent,
         (select count(*) from schule.sterne) sterne_zeilen,
         (select coalesce(sum(menge), 0) from schule.sterne) sterne_summe,
         (select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) from schule.sterne x) sterne_md5,
         (select md5(coalesce(string_agg(x::text, '|' order by x.lernender_id, x.einheit_id, x.lernziel collate "C"), '')) from schule.karte_stand x) karte_md5;
"""


def bericht(bm, n_fn_soll):
    """Bericht als abschließende Fehlermeldung (Urteil 1215, Auflage 2). Erste Zeile kompakt:
    „ADVENT-S PROBELAUF bestanden … KURZ {…}“ bzw. „ADVENT-S PROBELAUF NICHT bestanden (n Befunde) … KURZ {…}“, danach BEFUNDE, HINWEISE, DETAILS.
    „bestanden“ NUR bei 0 Befunden, 6 Tabellen, genau n_fn_soll Funktionen, Schaltern 0/0 und unveränderten schule.sterne (Zeilen, Summe, Inhalt) und
    schule.karte_stand. HINWEISE (fehlende/ungültige Zeitzone eines Kindes) halten nicht auf: der Server antwortet dann „zeitzone_fehlt“ – vor dem Einschalten beheben."""
    paare = ', '.join(f"'{k}', '{v}'" for k, v in bm.items())
    return """
-- ---------- Probe: Bericht (am Ende absichtlich Fehler -> ALLES zurückgerollt) ----------
do $advent_probe$
declare v record; e jsonb; k jsonb := '[]'::jsonb; r record; befund text[] := '{}'; hinweis text[] := '{}';
  bm jsonb := jsonb_build_object(""" + paare + """); b jsonb := '{}'::jsonb;
  n_tab int; n_fn int; n_lan int; n_lan_am int; n_lan_fehlt int; kurz jsonb; f text; m text; n_st bigint; s_st bigint; m_st text; st_ok boolean; ka_ok boolean;
  n_fn_soll constant int := """ + str(n_fn_soll) + """;
begin
  select * into v from advent_probe_vorher;
  e := schule.advent_einstellung();
  select count(*) into n_tab from pg_class c join pg_namespace n on n.oid = c.relnamespace where n.nspname = 'schule' and c.relname like 'advent\\_%' and c.relkind = 'r';
  select count(*) into n_fn from pg_proc p join pg_namespace n on n.oid = p.pronamespace where (n.nspname = 'schule' and p.proname like 'advent\\_%')
     or (n.nspname = 'api' and p.proname like 'schule\\_advent\\_%');
  if n_tab <> 6 then befund := befund || format('Tabellen %s statt 6', n_tab); end if;
  if n_fn <> n_fn_soll then befund := befund || format('Funktionen %s statt %s', n_fn, n_fn_soll); end if;
  if v.tabellen <> 0 or v.funktionen <> 0 or v.regeln <> 0 or v.grund_advent then
    befund := befund || format('Vorher nicht leer (Tabellen %s, Funktionen %s, Regeln %s, Grund advent %s)', v.tabellen, v.funktionen, v.regeln, v.grund_advent); end if;
  if (e->>'aktiv')::int <> 0 or (e->>'tausch')::int <> 0 then befund := befund || format('Schalter aktiv=%s tausch=%s statt 0/0', e->>'aktiv', e->>'tausch'); end if;
  -- schule.sterne echt vergleichen: Zeilenzahl, Summe und Inhalt (md5) vorher/nachher
  select count(*), coalesce(sum(x.menge), 0), md5(coalesce(string_agg(x::text, '|' order by x.id), '')) into n_st, s_st, m_st from schule.sterne x;
  st_ok := n_st = v.sterne_zeilen and s_st = v.sterne_summe and m_st = v.sterne_md5;
  if not st_ok then befund := befund || format('schule.sterne verändert (Zeilen %s -> %s, Summe %s -> %s, Inhalt %s)', v.sterne_zeilen, n_st, v.sterne_summe, s_st,
                                               case when m_st = v.sterne_md5 then 'gleich' else 'anders' end); end if;
  ka_ok := (select md5(coalesce(string_agg(x::text, '|' order by x.lernender_id, x.einheit_id, x.lernziel collate "C"), '')) from schule.karte_stand x) = v.karte_md5;
  if not ka_ok then befund := befund || 'schule.karte_stand verändert'::text; end if;
  foreach f in array array['lern_ich', 'ist_lern', 'wer_tn', 'ist_eltern', 'sieht', 'zugriff'] loop
    select md5(p.prosrc) into m from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'schule' and p.proname = f;
    b := b || jsonb_build_object(f, case when m = bm->>f then 'wie Repo' else 'ABWEICHEND ' || coalesce(m, 'fehlt') end);
    if m is distinct from bm->>f then befund := befund || format('Bestandsfunktion schule.%s weicht vom Repo ab (Zugriffsprüfung so nicht getestet)', f); end if;
  end loop;
  -- Landungen, die der Kalender erkennt (eigene Landung / „Sitzt wieder!“: landung.am = sitzt_am)
  select count(*) filter (where k2.landung_art is not null and k2.sitzt),
         count(*) filter (where k2.landung_art is not null and k2.sitzt and (k2.landung->>'am')::timestamptz = k2.sitzt_am),
         count(*) filter (where k2.landung_art is not null and k2.sitzt and k2.landung->>'am' is null)
    into n_lan, n_lan_am, n_lan_fehlt from schule.karte_stand k2;
  if n_lan > 0 and n_lan_am = 0 then befund := befund || format('Landungen erkannt 0 von %s – Annahme landung.am = sitzt_am gilt live nicht (STOPP)', n_lan); end if;
  for r in select l.id, l.ist_test, l.zeitzone, schule.advent_tz(l.id) tz from schule.lernender l where l.aktiv order by l.id loop
    k := k || jsonb_build_object('lernender_id', r.id, 'ist_test', r.ist_test, 'zeitzone', r.zeitzone, 'gueltig', r.tz is not null,
      'ortszeit', case when r.tz is not null then to_char(now() at time zone r.tz, 'YYYY-MM-DD HH24:MI') end,
      'lage', case when r.tz is not null then (schule.advent_lage(r.id) - 'offen_nrs' - 'start' - 'nachholen_bis' - 'sichtbar_bis' - 'jahr' - 'zeitzone' - 'max_pro_tag') end,
      'eigene_landungen_gesamt', (select count(*) from schule.karte_stand x where x.lernender_id = r.id and x.sitzt and x.landung_art is not null
                                     and (x.landung->>'am')::timestamptz = x.sitzt_am));
    if r.tz is null then hinweis := hinweis || format('ZEITZONE FEHLT/UNGÜLTIG: lernender %s (%s) – Kalender liefert „zeitzone_fehlt“', r.id, coalesce(r.zeitzone, 'leer')); end if;
  end loop;
  kurz := jsonb_build_object('befunde', cardinality(befund), 'hinweise', cardinality(hinweis), 'tabellen', n_tab, 'funktionen', n_fn, 'funktionen_soll', n_fn_soll,
    'aktiv', (e->>'aktiv')::int, 'tausch', (e->>'tausch')::int, 'sterne_unveraendert', st_ok, 'karte_unveraendert', ka_ok,
    'zeitzone_fehlt', (select coalesce(jsonb_agg((x->>'lernender_id')::int), '[]'::jsonb) from jsonb_array_elements(k) x where not (x->>'gueltig')::boolean),
    'landungen', n_lan_am || '/' || n_lan);
  if cardinality(befund) > 0 or n_tab <> 6 or n_fn <> n_fn_soll or not st_ok or not ka_ok or (e->>'aktiv')::int <> 0 or (e->>'tausch')::int <> 0 then
    raise exception E'ADVENT-S PROBELAUF NICHT bestanden (% Befunde), ALLES zurückgerollt. KURZ %\\nBEFUNDE: %\\nHINWEISE: %\\nDETAILS: %',
      cardinality(befund), kurz::text, array_to_string(befund, ' | '), coalesce(nullif(array_to_string(hinweis, ' | '), ''), 'keine'),
      jsonb_build_object('einstellung', e, 'kinder', k, 'bestand_md5', b, 'landungen_ohne_am', n_lan_fehlt)::text;
  end if;
  raise exception E'ADVENT-S PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt). KURZ %\\nBEFUNDE: keine\\nHINWEISE: %\\nVORHER/NACHHER: %\\nDETAILS: %',
    kurz::text, coalesce(nullif(array_to_string(hinweis, ' | '), ''), 'keine'),
    format('Tabellen %s/%s, Funktionen %s/%s, Regeln advent_* %s/%s, Grund advent %s, Start %s, Nachholen bis %s, sichtbar bis %s, max %s/Tag, Sterne Zeilen %s/%s, Summe %s/%s',
      v.tabellen, n_tab, v.funktionen, n_fn, v.regeln, (select count(*) from schule.regel r2 where r2.schluessel like 'advent\\_%'),
      case when v.grund_advent then 'schon da' else 'neu' end, e->>'start', e->>'nachholen_bis', e->>'sichtbar_bis', e->>'max_pro_tag', v.sterne_zeilen, n_st, v.sterne_summe, s_st),
    jsonb_build_object('einstellung', e, 'kinder', k, 'bestand_md5', b, 'landungen_ohne_am', n_lan_fehlt, 'lernpause_noetig', false)::text;
end $advent_probe$;
"""


def pakete():
    mig = MIGRATION.read_text(encoding='utf-8')
    kopf = ('-- ADVENT-S PROBELAUF (rollt am Ende ALLES zurück, nichts eingespielt). Erzeugt von tools/tests/advent_pakete.py aus ' + MIGRATION.name + '.\n'
            '-- Ein Aufruf, eine Transaktion. Bericht = die abschließende Fehlermeldung: erste Zeile „… bestanden|NICHT bestanden … KURZ {…}“, dann BEFUNDE, HINWEISE, DETAILS.\n')
    nach_vor = mig.index('end $advent_vor$;\n') + len('end $advent_vor$;\n')     # Vorher-Stand erst nach der Prüfung des Vorzustands
    probe = kopf + mig[:nach_vor] + VORHER + mig[nach_vor:] + bericht(bestand_md5(), funktionen_soll())
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
