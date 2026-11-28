#!/usr/bin/env python3
"""Paketbau für eine neue Runde (ab Runde 15, Gegenprüfung 1209): vier Dateien unter tools/tests/aus/ nach dem Muster von Runde 14,
aber mit Kopf (Voraussetzungen, Reihenfolge, Lernpause), Zeitgrenzen als ERSTER Anweisung und einem kompakten BERICHT.

  rollend<R>_probe.sql        Aufgaben mit Fehlbildern (wie rollend<R>_einspielen.sql), rollt am Ende absichtlich zurück
  rollend<R>_einspielen.sql   Aufgaben (tools/rollend_sql.py --runden R, ohne Regel) + Fehlbilder (schreibend); Differenzen fest geprüft
  rb_nachtrag_r<R>_probe.sql  Regel-Kennungen der Aufgaben mit Regel (Fehlbilder nur lesend verglichen), rollt am Ende zurück
  rb_nachtrag_r<R>.sql        dasselbe, schreibt die Regeln

Aufruf:  python3 -I tools/rollend_paket_sql.py --runde 15            -> schreibt die vier Dateien, druckt Größe/md5/Erwartung
         python3 -I tools/rollend_paket_sql.py --runde 15 --pruefen  -> schreibt nichts; Rückgabe 1, wenn eine Datei nicht dem Stand entspricht
Kein bestehendes Paket wird erzeugt oder verändert (nur die Dateien dieser Runde).

Eigenschaften der Pakete (je EIN Aufruf, EINE Transaktion, kein BEGIN/COMMIT, kein Savepoint, keine Annahme über Untertransaktionen des Aufrufers):
  - erste Anweisung: lock_timeout 3 s, statement_timeout 120 s (nur für diese Transaktion);
  - Voraussetzungen werden geprüft (RB-S, FT-S); die Bestandszahlen vorher (32 440 Aufgaben, 5 756 Fehlbilder, 2 004 Regelzuordnungen am 28.11.2026)
    sind nur ERWARTET: Abweichung bricht NICHT ab, sie steht im Bericht; fest geprüft werden nur die Differenzen (+Aufgaben, +Fehlbilder, +Regeln);
  - Vergleiche nullsicher (is distinct from, coalesce) und ohne Textsortierung (kollationsunabhängig: gleiches Ergebnis bei C, en-US-ICU und de-DE-ICU);
  - Bericht: Meldung (raise notice) und als letzte Ausgabe eine Zeile „bericht“; in der Probe steht der Bericht am ANFANG der Fehlermeldung.
Nicht ohne den ausdrücklichen Satz des Nutzers ausführen.
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
AUS = WURZEL / 'tools/tests/aus'
sys.path.insert(0, str(WURZEL / 'tools'))
import regelbezug_sql as R  # noqa: E402

ERWARTET_VORHER = (32440, 5756, 2004)   # Aufgaben, Fehlbilder, Regelzuordnungen live am 28.11.2026 (nur Anzeige im Bericht)


def erzeugen(*args):
    p = subprocess.run([sys.executable, '-I', *args], capture_output=True, text=True, cwd=str(WURZEL))
    if p.returncode != 0: raise SystemExit(f'{args}: {p.stderr[-800:]}')
    return p.stdout


def vorher_block(tag):
    return f"""do ${tag}$
declare v_a bigint; v_f bigint; v_r bigint;
begin
  if to_regclass('schule.aufgabe') is null or to_regclass('schule.aufgabe_fehlbild') is null or to_regclass('schule.aufgabe_regel') is null
     or to_regprocedure('schule.aufgaben_einfuegen(bigint, jsonb)') is null or to_regprocedure('schule.antwort_bewerten(schule.aufgabe, jsonb)') is null
     or to_regprocedure('schule.fehlbild_finden(schule.aufgabe, jsonb)') is null
     or to_regprocedure('schule.fehlbild_probeantwort(schule.aufgabe, text, integer, text)') is null then
    raise exception 'ABBRUCH, Voraussetzung: RB-S (20261204_rb_s_regelbezug.sql) und FT-S (20261203_ft_s_form_takt.sql) müssen eingespielt sein – nichts geändert'; end if;
  select count(*) into v_a from schule.aufgabe;
  select count(*) into v_f from schule.aufgabe_fehlbild;
  select count(*) into v_r from schule.aufgabe_regel;
  perform set_config('rollend.vorher', v_a || ' ' || v_f || ' ' || v_r, true);
end ${tag}$;
"""


def nachher_block(tag, name, soll_a, soll_f, soll_r, wiederholung_ok):
    """Differenzen fest prüfen (Abbruch = alles zurück), Bericht bilden. soll_r: Regeln neu beim Erstlauf; wiederholung_ok: auch 0 erlaubt (Nachtrag)."""
    erlaubt_r = f"d_r in (0, {soll_r})" if wiederholung_ok else f"d_r = {soll_r}"
    text_r = f"{soll_r} beim Erstlauf, 0 bei Wiederholung" if wiederholung_ok else f"{soll_r}"
    return f"""do ${tag}$
declare v text[] := string_to_array(current_setting('rollend.vorher', true), ' '); n_a bigint; n_f bigint; n_r bigint; d_a bigint; d_f bigint; d_r bigint; b text; wie text;
begin
  if v is null or array_length(v, 1) is distinct from 3 then
    raise exception 'ABBRUCH: die Zählung vorher fehlt (Paket nicht in EINEM Aufruf ausgeführt?)'; end if;
  select count(*) into n_a from schule.aufgabe;
  select count(*) into n_f from schule.aufgabe_fehlbild;
  select count(*) into n_r from schule.aufgabe_regel;
  d_a := n_a - v[1]::bigint; d_f := n_f - v[2]::bigint; d_r := n_r - v[3]::bigint;
  if d_a is distinct from {soll_a} or d_f is distinct from {soll_f} or not coalesce({erlaubt_r}, false) then
    raise exception 'ABBRUCH, alles zurückgerollt: Differenz Aufgaben % (Soll {soll_a}), Fehlbilder % (Soll {soll_f}), Regelzuordnungen % ({text_r})', d_a, d_f, d_r; end if;
  wie := case when (v[1], v[2], v[3]) is not distinct from ('{ERWARTET_VORHER[0]}', '{ERWARTET_VORHER[1]}', '{ERWARTET_VORHER[2]}') then 'wie erwartet'
              else 'WEICHT AB von den erwarteten {ERWARTET_VORHER[0]} / {ERWARTET_VORHER[1]} / {ERWARTET_VORHER[2]} (nur die Differenzen sind fest geprüft)' end;
  b := format('{name}: %s Aufgaben, %s Fehlbilder, %s Regelzuordnungen neu (Soll {soll_a} / {soll_f} / {text_r}); Bestand vorher %s / %s / %s (Aufgaben / Fehlbilder / Regelzuordnungen), %s; nachher %s / %s / %s',
              d_a, d_f, d_r, v[1], v[2], v[3], wie, n_a, n_f, n_r);
  perform set_config('rollend.bericht', b, true);
  raise notice 'BERICHT %', b;
end ${tag}$;
"""


def ende(probe):
    if probe:
        return """do $rende$ begin
  raise exception 'BERICHT %  |  PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt)', current_setting('rollend.bericht', true);
end $rende$;
"""
    return "select current_setting('rollend.bericht', true) as bericht;\n"


ZEITGRENZEN = "select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);\n"


def kopf(runde, art, probe, soll_a, soll_f, soll_r):
    probe_t = ('PROBELAUF: macht alles wie das echte Paket und rollt am Ende ABSICHTLICH zurück (Fehlermeldung beginnt mit BERICHT …, endet mit PROBELAUF bestanden); '
               'nichts bleibt in der Datenbank.' if probe else 'EINSPIEL-PAKET: schreibt in die Datenbank (nach der Probe, nur auf ausdrücklichen Satz des Nutzers).')
    if art == 'aufgaben':
        was = (f'Runde {runde}: {soll_a} Aufgaben (14 Einheiten, form/zaehlt) über schule.aufgaben_einfuegen und {soll_f} Fehlbilder in schule.aufgabe_fehlbild; '
               f'KEINE Regeln (die kommen mit rb_nachtrag_r{runde}.sql).')
        reihenfolge = f'1. rollend{runde}_probe.sql  2. rollend{runde}_einspielen.sql  3. rb_nachtrag_r{runde}_probe.sql  4. rb_nachtrag_r{runde}.sql (diese Datei ist Schritt {"1" if probe else "2"}).'
        diff = f'+{soll_a} Aufgaben, +{soll_f} Fehlbilder, +0 Regelzuordnungen (fest geprüft)'
        wdh = 'Ein zweiter Lauf bricht ab („Reihenfolge-Nummern des Pakets sind schon belegt“) und ändert nichts.'
    else:
        was = (f'Runde {runde}: {soll_r} Regel-Kennungen (schule.aufgabe_regel) der {soll_a} schon eingespielten Aufgaben; die {soll_f} Fehlbilder werden NUR LESEND '
               f'gegen das Soll verglichen (sie stehen mit dem Aufgaben-Paket schon da; fehlt, zusätzlich oder abweichend = Abbruch).')
        reihenfolge = f'1. rollend{runde}_probe.sql  2. rollend{runde}_einspielen.sql  3. rb_nachtrag_r{runde}_probe.sql  4. rb_nachtrag_r{runde}.sql (diese Datei ist Schritt {"3" if probe else "4"}).'
        diff = f'+0 Aufgaben, +0 Fehlbilder, +{soll_r} Regelzuordnungen beim Erstlauf (0 bei Wiederholung; ein Teilvorbestand bricht ab)'
        wdh = 'Wiederholbar: ein zweiter Lauf fügt nichts hinzu (0 und 0).'
    return f"""-- {'Aufgaben-Paket' if art == 'aufgaben' else 'Regel-Nachtrag'} Runde {runde} ({'Probe' if probe else 'Einspielen'}). Erzeugt von tools/rollend_paket_sql.py – nicht von Hand ändern.
-- {probe_t}
-- WAS: {was}
-- REIHENFOLGE: {reihenfolge}
-- VORAUSSETZUNG: RB-S (Tabellen aufgabe_regel/aufgabe_fehlbild, Funktionen fehlbild_finden/fehlbild_probeantwort) und FT-S (form/zaehlt, aufgaben_einfuegen) eingespielt, sonst Abbruch ohne Änderung.
--   {'Die Aufgaben der Runde müssen schon eingespielt sein (Schritt 2).' if art != 'aufgaben' else 'Bestand wie am 28.11.2026: 32 440 Aufgaben, 5 756 Fehlbilder, 2 004 Regelzuordnungen – nur ERWARTET, Abweichung steht im Bericht und bricht nicht ab.'}
-- FEST GEPRÜFT: {diff}. Jede Abweichung = Abbruch, ALLES zurück.
-- {wdh}
-- LERNPAUSE: nicht nötig. Das Paket ändert keine bestehende Zeile (nur INSERT von Aufgaben/Fehlbildern/Regelzuordnungen), sperrt keine Einheit und setzt keinen Status; Details in inhalte/mathe-profi/rollend-{runde}/einspielen.md.
-- AUFRUF: der gesamte Dateiinhalt in EINEM execute (kein psql-Meta, kein eigenes BEGIN/COMMIT).
"""


def bericht_zahlen(runde):
    """(Aufgaben, Fehlbilder, Regeln) der Runde laut Aufgaben-Paket und Nachtrag."""
    roh = erzeugen('tools/rollend_sql.py', '--runden', str(runde), '--sql')
    m = re.search(r'^-- RB-S Regelbezug: neue Aufgaben rollend-%d: (\d+) Aufgaben, (\d+) Regeln, (\d+) Fehlbilder\.' % runde, roh, re.M)
    assert m and m.group(2) == '0', 'Aufgaben-Paket darf keine Regeln enthalten (REGEL_ERST_IM_NACHTRAG)'
    return roh, int(m.group(1)), int(m.group(3))


def aufgaben_paket(runde, probe):
    roh, n_a, n_f = bericht_zahlen(runde)
    i = roh.index('do $einspielen$')
    j = roh.index('select einheit_id, count(*) filter')
    k = roh.index('do $rbnach$')
    assert roh.count('do $einspielen$') == 1 and roh.count('do $rbnach$') == 1 and i < j < k
    teil_a = roh[i:j]
    teil_b = roh[k:]
    assert not re.search(r'^\s*\\|^\s*(begin|commit|rollback)\s*;', roh, re.M | re.I)
    # zweiter Block (Fehlbilder schreibend): die Probe dieses Blocks gibt es hier nicht (probe = False), die Probe endet nach den Differenzen
    return (kopf(runde, 'aufgaben', probe, n_a, n_f, 0) + ZEITGRENZEN + vorher_block('rvor') + teil_a + teil_b
            + nachher_block('rnach', f'Runde {runde} Aufgaben-Paket', n_a, n_f, 0, False) + ende(probe))


def nachtrag(runde, probe):
    zeilen, abw, fehlt, z, weg, je_typ = R.sammeln((runde,))
    if fehlt: raise SystemExit(f'Nachtrag Runde {runde}: Aufgaben nicht im Paket rollend{runde}_einspielen.sql: {fehlt[:3]}')
    n_r = sum(1 for x in zeilen if x['regel'])
    n_f = sum(len(x['fb']) for x in zeilen)
    b = R.block(zeilen, f'Nachtrag rollend-{runde}', probe=False, fb_lesen=True)
    k = b.index('do $rbnach$')
    return (kopf(runde, 'nachtrag', probe, z['aufgaben'], n_f, n_r) + ZEITGRENZEN + vorher_block('rvor') + b[k:]
            + nachher_block('rnach', f'Runde {runde} Regel-Nachtrag', 0, 0, n_r, True) + ende(probe))


def dateien(runde):
    out = []
    for probe in (True, False):
        out.append((f'rollend{runde}_probe.sql' if probe else f'rollend{runde}_einspielen.sql', aufgaben_paket(runde, probe)))
    return out


def dateien_nachtrag(runde):
    return [(f'rb_nachtrag_r{runde}_probe.sql', nachtrag(runde, True)), (f'rb_nachtrag_r{runde}.sql', nachtrag(runde, False))]


def main():
    argv = sys.argv[1:]
    if '--runde' not in argv: sys.exit('--runde N fehlt')
    runde = int(argv[argv.index('--runde') + 1])
    pruefen = '--pruefen' in argv
    alle = []
    for name, text in dateien(runde):
        if not pruefen: (AUS / name).write_text(text, encoding='utf-8')   # der Nachtrag liest rollend<R>_einspielen.sql von der Platte
        alle.append((name, text))
    for name, text in dateien_nachtrag(runde):
        if not pruefen: (AUS / name).write_text(text, encoding='utf-8')
        alle.append((name, text))
    if pruefen:
        alt = [n for n, t in alle if not (AUS / n).exists() or (AUS / n).read_text(encoding='utf-8') != t]
        if alt: print('nicht auf dem Stand:', ', '.join(alt), file=sys.stderr); sys.exit(1)
        print('OK'); return
    print('| Datei | Bytes | md5 |\n|---|---|---|')
    for n, t in alle:
        print(f'| `tools/tests/aus/{n}` | {len(t.encode("utf-8")):,} | `{hashlib.md5(t.encode("utf-8")).hexdigest()}` |'.replace(',', ' '))


if __name__ == '__main__':
    main()
