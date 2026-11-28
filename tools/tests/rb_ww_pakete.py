"""Schreibt die Einspiel-Dateien für RB-S und WW-S nach tools/tests/aus/ (je Schritt EINE Datei, in einem `execute` lauffähig: kein psql-Meta,
kein eigenes BEGIN/COMMIT, unter 1,5 MB; WW-S3 seit 28.11.) und druckt Größe, md5 und erwartete Zahlen (für inhalte/plan/einspiel-reihenfolge-rb-ww.md).

Aufruf:  python3 -I tools/tests/rb_ww_pakete.py            -> schreibt die Dateien, druckt die Tabelle
         python3 -I tools/tests/rb_ww_pakete.py --pruefen  -> schreibt nichts; Rückgabe 1, wenn eine Datei nicht dem Stand entspricht
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
AUS = WURZEL / 'tools/tests/aus'
sys.path.insert(0, str(WURZEL / 'tools'))
import regelbezug_sql as R  # noqa: E402

RUNDEN = tuple(range(1, 15))   # 14: Nachtrag der Regel-Kennungen (Runde 14 ist mit ihren 640 Fehlbildern schon eingespielt)
GRENZE = 1_500_000


def erzeugen(*args):
    p = subprocess.run([sys.executable, '-I', *args], capture_output=True, text=True, cwd=str(WURZEL))
    if p.returncode != 0: raise SystemExit(f'{args}: {p.stderr[-500:]}')
    return p.stdout


def pakete():
    out = [('rb_s_probe.sql', erzeugen('tools/tests/regelbezug_einspielen.py', '--probe'), 'Meldung „PROBELAUF bestanden …“ mit "fehler": 0'),
           ('rb_s_einspielen.sql', erzeugen('tools/tests/regelbezug_einspielen.py'), 'Hinweis „RB-S eingespielt: …“, "fehler": 0')]
    for r in RUNDEN:
        zeilen = R.sammeln((r,))[0]
        n_r, n_f = sum(1 for x in zeilen if x['regel']), sum(len(x['fb']) for x in zeilen)
        erw = (f'{len(zeilen)} Aufgaben, {n_r} Regeln neu, 0 Fehlbilder neu (die {n_f} Fehlbilder stehen mit Runde 14 schon da; zweiter Lauf: 0 und 0)' if r == 14
               else f'{len(zeilen)} Aufgaben, {n_r} Regeln neu, {n_f} Fehlbilder neu (zweiter Lauf: 0 und 0)')
        out.append((f'rb_nachtrag_r{r:02d}.sql', erzeugen('tools/regelbezug_sql.py', '--runden', str(r), '--sql'), erw))
    out += [('ww_s_probe.sql', erzeugen('tools/tests/wackelt_einspielen.py', '--probe'), 'Meldung „PROBELAUF bestanden …“ mit "fehler": 0'),
            ('ww_s_einspielen.sql', erzeugen('tools/tests/wackelt_einspielen.py'), 'Hinweis „WW-S eingespielt: …“, "fehler": 0'),
            ('ww_s3_probe.sql', erzeugen('tools/tests/wackelt_einspielen.py', '--ww3', '--probe'), 'Meldung „PROBELAUF bestanden …“ mit "fehler": 0'),
            ('ww_s3_einspielen.sql', erzeugen('tools/tests/wackelt_einspielen.py', '--ww3'), 'Hinweis „WW-S3 eingespielt: …“, "fehler": 0')]
    for name, text, _ in out:
        assert len(text.encode('utf-8')) < GRENZE, (name, len(text))
        assert not re.search(r'^\s*\\', text, re.M), f'{name}: psql-Meta'
        assert not re.search(r'^\s*(begin|commit|rollback|start transaction)\s*;', text, re.M | re.I), f'{name}: eigenes BEGIN/COMMIT'
        assert '$rbpaket$' not in text, name
    return out


def main():
    out = pakete()
    if '--pruefen' in sys.argv:
        alt = [n for n, t, _ in out if not (AUS / n).exists() or (AUS / n).read_text(encoding='utf-8') != t]
        if alt: print('nicht auf dem Stand:', ', '.join(alt), file=sys.stderr); sys.exit(1)
        print('OK'); return
    print('| Datei | Bytes | md5 | erwartet |\n|---|---|---|---|')
    for n, t, erw in out:
        (AUS / n).write_text(t, encoding='utf-8')
        groesse = f'{len(t.encode("utf-8")):,}'.replace(',', ' ')
        print(f'| `tools/tests/aus/{n}` | {groesse} | `{hashlib.md5(t.encode("utf-8")).hexdigest()}` | {erw} |')


if __name__ == '__main__':
    main()
