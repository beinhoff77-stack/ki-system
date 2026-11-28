#!/usr/bin/env python3
"""ADVENT-S: Belegungs-Paket (Türinhalte je Kind) aus einer JSON-Datei AUSSERHALB des Repos.

Aufruf:  python3 -I tools/advent_belegung_sql.py <belegung.json>                 -> prüft die Datei, druckt eine Übersicht (keine Texte), schreibt nichts
         python3 -I tools/advent_belegung_sql.py <belegung.json> --aus <ordner>  -> schreibt <ordner>/advent_belegung_probe.sql und _einspielen.sql, druckt Größe/md5

Die persönlichen Türtexte gehören NICHT ins Repo: Eingabe und Ausgabe-Ordner müssen außerhalb des Repos liegen (einzige Ausnahme beim Lesen:
die neutrale Beispiel-Datei inhalte/design/advent/belegung-beispiel.json). Format: inhalte/design/advent/server.md, Abschnitt „Belegungs-Werkzeug“.

Das Paket (ein Aufruf, eine Transaktion, erste Anweisung = Zeitgrenzen) setzt je Kind die genannten Türen über schule.advent_belegen
(dieselben Prüfungen wie die Eltern-Aktion), überschreibt NUR noch geschlossene Türchen (geöffnete werden übersprungen und gemeldet) und ist
wiederholbar (zweiter Lauf: 0 gesetzt). Abbruch ohne Änderung, wenn ADVENT-S fehlt oder eine andere Fassung von schule.advent_belegen eingespielt ist,
das Jahr nicht zur Einstellung passt oder ein Kind fehlt/inaktiv ist. Die Probe endet absichtlich mit einem Fehler (alles zurückgerollt).
NICHT AUSFÜHREN ohne den ausdrücklichen Satz des Nutzers.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
BEISPIEL = WURZEL / 'inhalte/design/advent/belegung-beispiel.json'
MIGRATION = WURZEL / 'supabase/migrations/20261209_advent_s.sql'
MOTIVE_JS = WURZEL / 'inhalte/design/advent/entwurf2/teile/v_motive2.js'
ARTEN = ('bild', 'gutschein', 'sterne', 'karte', 'krampus', 'leer')
FELDER = ('nr', 'fuer', 'art', 'variante', 'titel', 'text', 'sterne', 'motiv')


class Fehler(Exception):
    pass


def motive():
    s = MOTIVE_JS.read_text(encoding='utf-8')
    i = s.index('const M2 = {')
    return set(re.findall(r'(?m)^  ([a-z0-9_]+):', s[i:]))


def belegen_md5():
    """prosrc-md5 von schule.advent_belegen, wie die Migration sie anlegt (das Paket setzt genau diese Fassung voraus)."""
    s = MIGRATION.read_text(encoding='utf-8')
    m = re.search(r'create or replace function schule\.advent_belegen\(.*?\bas \$function\$(.*?)\$function\$;', s, re.S)
    return hashlib.md5(m.group(1).encode('utf-8')).hexdigest()


def im_repo(p):
    try:
        Path(p).resolve().relative_to(WURZEL)
        return True
    except ValueError:
        return False


def lesen(pfad):
    p = Path(pfad).resolve()
    if im_repo(p) and p != BEISPIEL.resolve():
        raise Fehler(f'{pfad}: liegt im Repo – persönliche Türtexte gehören nicht ins Repo (nur die Beispiel-Datei darf hier liegen)')
    try:
        d = json.loads(p.read_text(encoding='utf-8'))
    except (OSError, ValueError) as e:
        raise Fehler(f'{pfad}: nicht lesbar ({e})')
    return d


def pruefen(d):
    """Gibt (jahr, kinder {bezeichnung: id}, je_kind {id: [türen]}) zurück; Fehler bei jeder Unstimmigkeit."""
    if not isinstance(d, dict) or set(d) - {'jahr', 'kinder', 'tueren', 'hinweis'}:
        raise Fehler('oberste Ebene: nur jahr, kinder, tueren (und hinweis)')
    jahr = d.get('jahr')
    if not isinstance(jahr, int) or not 2026 <= jahr <= 2100:
        raise Fehler('jahr: ganze Zahl (z. B. 2026 – Jahr des Starts in schule.regel advent_start)')
    kinder = d.get('kinder')
    if not isinstance(kinder, dict) or not kinder:
        raise Fehler('kinder: Objekt {"Bezeichnung": lernender_id, …}')
    for k, v in kinder.items():
        if not isinstance(k, str) or not k.strip() or k == 'beide' or not isinstance(v, int) or isinstance(v, bool) or v <= 0:
            raise Fehler(f'kinder: „{k}“ braucht eine positive lernender_id (Bezeichnung nicht „beide“)')
    if len(set(kinder.values())) != len(kinder):
        raise Fehler('kinder: eine lernender_id doppelt')
    mot = motive()
    je = {v: {} for v in kinder.values()}
    tueren = d.get('tueren')
    if not isinstance(tueren, list) or not tueren:
        raise Fehler('tueren: Liste')
    for i, t in enumerate(tueren, 1):
        wo = f'tueren[{i}]'
        if not isinstance(t, dict) or set(t) - set(FELDER):
            raise Fehler(f'{wo}: nur die Felder {", ".join(FELDER)}')
        nr = t.get('nr')
        if not isinstance(nr, int) or isinstance(nr, bool) or not 1 <= nr <= 24:
            raise Fehler(f'{wo}: nr 1 bis 24')
        wo = f'Tür {nr}'
        fuer = t.get('fuer', 'beide')
        if fuer == 'beide':
            ziele = list(kinder.values())
        else:
            namen = [fuer] if isinstance(fuer, str) else fuer
            if not isinstance(namen, list) or not namen or any(n not in kinder for n in namen):
                raise Fehler(f'{wo}: fuer = "beide", eine Bezeichnung aus kinder oder eine Liste davon')
            ziele = [kinder[n] for n in namen]
        art = t.get('art')
        if art not in ARTEN:
            raise Fehler(f'{wo}: art {"/".join(ARTEN)}')
        var = t.get('variante')
        if art == 'sterne' and var not in (None, 'normal', 'jackpot', 'niete'): raise Fehler(f'{wo}: variante normal/jackpot/niete')
        if art == 'gutschein' and var not in (None, 'normal', 'tausch'): raise Fehler(f'{wo}: variante normal/tausch')
        if art not in ('sterne', 'gutschein') and var is not None: raise Fehler(f'{wo}: variante nur bei sterne oder gutschein')
        st = t.get('sterne', 0)
        if not isinstance(st, int) or isinstance(st, bool) or not 0 <= st <= 5000: raise Fehler(f'{wo}: sterne ganze Zahl 0 bis 5000')
        ti, tx, mo = t.get('titel'), t.get('text'), t.get('motiv')
        for name, w, n in (('titel', ti, 80), ('text', tx, 300)):
            if w is not None and (not isinstance(w, str) or len(w.strip()) > n): raise Fehler(f'{wo}: {name} Text, höchstens {n} Zeichen')
        if art in ('gutschein', 'krampus') and not (ti or '').strip(): raise Fehler(f'{wo}: {art} braucht einen titel')
        if art == 'bild' and not mo: raise Fehler(f'{wo}: bild braucht ein motiv')
        if mo is not None and mo not in mot: raise Fehler(f'{wo}: motiv „{mo}“ unbekannt (bekannt: {", ".join(sorted(mot))})')
        eintrag = {k: v for k, v in (('nr', nr), ('art', art), ('variante', var), ('titel', ti), ('text', tx), ('sterne', st), ('motiv', mo)) if v is not None}
        for z in ziele:
            if nr in je[z]:
                raise Fehler(f'{wo}: für lernender {z} doppelt belegt')
            je[z][nr] = eintrag
    return jahr, kinder, {k: [v[n] for n in sorted(v)] for k, v in je.items()}


def paket(jahr, kinder, je, probe):
    daten = {'jahr': jahr, 'kinder': [{'bezeichnung': b, 'lernender_id': i, 'tueren': je[i]} for b, i in kinder.items()]}
    js = json.dumps(daten, ensure_ascii=False, sort_keys=True)
    if '$advbel' in js:
        raise Fehler('Text enthält „$advbel“ – bitte umformulieren')
    ende = ("raise exception 'ADVENT-BELEGUNG PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt). KURZ: % | DETAILS: %', kurz, erg::text;" if probe
            else "raise notice 'ADVENT-BELEGUNG eingespielt. KURZ: % | DETAILS: %', kurz, erg::text;")
    art = 'PROBELAUF (rollt am Ende ALLES zurück)' if probe else 'Einspielen'
    return f"""-- ADVENT-BELEGUNG ({art}). Erzeugt von tools/advent_belegung_sql.py – enthält persönliche Türtexte: NICHT ins Repo legen.
-- Ein Aufruf, eine Transaktion, kein BEGIN/COMMIT. Setzt nur noch geschlossene Türchen (geöffnete bleiben, wie sie sind); wiederholbar.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '60s', true);
do $advbel$
declare v_daten constant jsonb := $advbeljson${js}$advbeljson$::jsonb;
  m_soll constant text := '{belegen_md5()}'; m text; k jsonb; r jsonb; erg jsonb := '[]'::jsonb; kurz text := ''; v_l bigint; f text[] := '{{}}';
begin
  if to_regprocedure('schule.advent_belegen(bigint[], jsonb, boolean, text)') is null then
    raise exception 'ADVENT-BELEGUNG ABBRUCH: ADVENT-S ist nicht eingespielt – nichts geändert'; end if;
  select md5(p.prosrc) into m from pg_proc p where p.oid = to_regprocedure('schule.advent_belegen(bigint[], jsonb, boolean, text)');
  if m is distinct from m_soll then raise exception 'ADVENT-BELEGUNG ABBRUCH: schule.advent_belegen ist eine andere Fassung (md5 %, erwartet %) – nichts geändert', m, m_soll; end if;
  if (schule.advent_einstellung()->>'jahr')::int <> (v_daten->>'jahr')::int then
    raise exception 'ADVENT-BELEGUNG ABBRUCH: Jahr % passt nicht zur Einstellung (advent_start %) – nichts geändert', v_daten->>'jahr', schule.advent_einstellung()->>'start'; end if;
  for k in select x from jsonb_array_elements(v_daten->'kinder') x loop
    v_l := (k->>'lernender_id')::bigint;
    if not exists (select 1 from schule.lernender l where l.id = v_l and l.aktiv) then f := f || format('%s (lernender %s) fehlt oder ist nicht aktiv', k->>'bezeichnung', v_l); end if;
  end loop;
  if cardinality(f) > 0 then raise exception 'ADVENT-BELEGUNG ABBRUCH: % – nichts geändert', array_to_string(f, '; '); end if;
  for k in select x from jsonb_array_elements(v_daten->'kinder') x loop
    v_l := (k->>'lernender_id')::bigint;
    r := schule.advent_belegen(array[v_l], k->'tueren', true, 'eltern:Belegungs-Werkzeug')->'kinder'->0;
    r := r || jsonb_build_object('bezeichnung', k->>'bezeichnung', 'zeitzone_ok', schule.advent_tz(v_l) is not null,
      'ohne_inhalt', (select coalesce(jsonb_agg(n order by n), '[]'::jsonb) from generate_series(1, 24) n
                       where not exists (select 1 from schule.advent_belegung b where b.jahr = (v_daten->>'jahr')::int and b.lernender_id = v_l and b.nr = n)));
    erg := erg || r;
    kurz := kurz || format('%s%s: %s gesetzt, %s unverändert, übersprungen (schon offen) %s, ohne Inhalt %s%s', case when kurz = '' then '' else ' | ' end, r->>'bezeichnung',
      r->>'gesetzt', r->>'unveraendert', r->'uebersprungen_offen', r->'ohne_inhalt', case when (r->>'zeitzone_ok')::boolean then '' else ', ZEITZONE FEHLT' end);
  end loop;
  {ende}
end $advbel$;
"""


def main(argv):
    args = [a for a in argv if not a.startswith('--')]
    aus = None
    if '--aus' in argv:
        i = argv.index('--aus')
        if i + 1 >= len(argv): raise Fehler('--aus <ordner>')
        aus = Path(argv[i + 1]).resolve()
        args = [a for a in args if a != argv[i + 1]]
        if im_repo(aus): raise Fehler(f'{aus}: Ausgabe-Ordner liegt im Repo – persönliche Türtexte gehören nicht ins Repo')
        if not aus.is_dir(): raise Fehler(f'{aus}: Ordner fehlt')
    if len(args) != 1: raise Fehler('Aufruf: advent_belegung_sql.py <belegung.json> [--aus <ordner außerhalb des Repos>]')
    jahr, kinder, je = pruefen(lesen(args[0]))
    print(f'Jahr {jahr}: ' + ' | '.join(f'{b} (lernender {i}): {len(je[i])} Türen ({", ".join(str(t["nr"]) for t in je[i])})' for b, i in kinder.items()))
    if aus:
        for name, probe in (('advent_belegung_probe.sql', True), ('advent_belegung_einspielen.sql', False)):
            t = paket(jahr, kinder, je, probe).encode('utf-8')
            (aus / name).write_bytes(t)
            print(f'{aus / name}: {len(t)} Bytes, md5 {hashlib.md5(t).hexdigest()}')


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Fehler as e:
        print('FEHLER: ' + str(e), file=sys.stderr)
        sys.exit(1)
