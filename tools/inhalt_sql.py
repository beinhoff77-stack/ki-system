#!/usr/bin/env python3
"""Baut aus geprüften Themen-Dateien das SQL zum Einspielen (Werkstatt #150).

Aufruf:  python3 -I tools/inhalt_sql.py inhalte/themen/<datei>.json [...] > einspielen.sql
Nur für den Haupt-Chat (Claude mit DB-Freigabe durch Sebastian). Neue Einheiten kommen als
status 'entwurf' hinein: nur das Testkind sieht sie, Eltern/Lehrer sehen sie als „in Prüfung“.
Gibt es für das Thema schon eine Einheit, bricht das SQL ab (keine stillen Überschreibungen).
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from inhalt_pruefen import pruefe  # noqa: E402

FELDER = ('l', 't', 'p', 's', 'y', 'f', 'a', 'o', 'h', 'w')


def dollar(s, tag):
    assert f'${tag}$' not in s
    return f'${tag}${s}${tag}$'


def sql_fuer(pfad):
    f, _, _ = pruefe(pfad)
    if f: raise SystemExit(f'{pfad}: {len(f)} Fehler – erst inhalt_pruefen.py sauber bekommen')
    d = json.loads(Path(pfad).read_text(encoding='utf-8'))
    inh = dict(d['inhalt'])
    inh.setdefault('quellen', {})
    inh['quellen'].setdefault('aufgaben', f'Programmgesteuert erzeugt, Lösungen berechnet ({d["autor"]}). Fachliche Prüfung durch ChatGPT ausstehend. Keine Schulbuchaufgaben.')
    n = {'uebung': 0, 'test': 100, 'korrektur': 200, 'sicherung': 300}
    rows = []
    for a in d['aufgaben']:
        n[a['p']] += 1
        r = {k: a[k] for k in FELDER if k in a and a[k] is not None}
        r['r'] = n[a['p']]
        rows.append(r)
    return f"""-- {Path(pfad).name}: {d['thema_schluessel']} ({len(rows)} Aufgaben, {len(inh['etappen'])} Lernkarten)
do $einspielen$
declare v_e bigint; v_n int;
begin
  if exists (select 1 from schule.einheit where thema_id = {int(d['thema_id'])} and status <> 'ersetzt') then
    raise exception 'Thema {int(d['thema_id'])} hat schon eine Einheit';
  end if;
  if not exists (select 1 from schule.block_thema where thema_id = {int(d['thema_id'])} and block_id = {int(d['block_id'])}) then
    raise exception 'thema_id/block_id passen nicht zusammen';
  end if;
  insert into schule.einheit (thema_id, block_id, status, inhalt, erstellt_von)
  values ({int(d['thema_id'])}, {int(d['block_id'])}, 'entwurf', {dollar(json.dumps(inh, ensure_ascii=False), 'inh')}::jsonb, {dollar(d['autor'], 'au')})
  returning id into v_e;
  v_n := schule.aufgaben_einfuegen(v_e, {dollar(json.dumps(rows, ensure_ascii=False), 'auf')}::jsonb);
  if v_n <> {len(rows)} then raise exception 'nur %% von {len(rows)} Aufgaben eingefügt', v_n; end if;
  raise notice 'Einheit % angelegt, % Aufgaben', v_e, v_n;
end $einspielen$;
""".replace('%%', '%')


if __name__ == '__main__':
    if len(sys.argv) < 2: print(__doc__); sys.exit(1)
    print('\n'.join(sql_fuer(p) for p in sys.argv[1:]))
