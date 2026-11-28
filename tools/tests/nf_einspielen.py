"""NF-S (Nachtest nur mit freigegebenen Aufgaben): Migration supabase/migrations/20261208_nf_s_nachtest_freigegeben.sql und die Pakete

  tools/tests/aus/nf_s_probe.sql        Probelauf: macht alles, vergleicht, endet IMMER mit „PROBELAUF bestanden, ALLES zurückgerollt …“ (oder „NF-S ABBRUCH …“)
  tools/tests/aus/nf_s_einspielen.sql   dasselbe, bleibt bei Erfolg eingespielt (Hinweis „NF-S eingespielt: …“)
(die Migration ist byteidentisch zur Einspiel-Datei: Einspielen nur über das selbstprüfende Paket).

Gegenstand: schule.nachtest_auswahl(bigint, bigint, text, integer) und schule.nachtest_stand(bigint, bigint) berücksichtigen aufgabe.freigegeben nicht.
Je Funktion genau zwei zulässige Zustände (prosrc-md5): alt (Live-Stand, Hash fest eingetragen) -> ersetzen; neu -> nichts; alles andere -> Abbruch.
Aufruf:  python3 -I tools/tests/nf_einspielen.py            -> schreibt Migration und Pakete, druckt Größe/md5
         python3 -I tools/tests/nf_einspielen.py --pruefen  -> schreibt nichts; Rückgabe 1, wenn eine Datei nicht dem Stand entspricht
"""
import hashlib
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
MIG = WURZEL / 'supabase/migrations'
AUS = WURZEL / 'tools/tests/aus'
MIGRATION = MIG / '20261208_nf_s_nachtest_freigegeben.sql'
STAND_ALT_DATEI = WURZEL / 'tools/tests/nf_nachtest_stand_alt.prosrc.txt'

AUSWAHL_ALT_MD5, AUSWAHL_ALT_LEN = 'f25fab1c1599d980752c87b6849d557f', 1109     # Live-Stand (Projektleiter, lesend) = nachgerechnet aus 20261124_nt_s_nachtest_menge.sql
STAND_ALT_MD5, STAND_ALT_LEN = 'e73af9b462d741de80d4932d8fa7a38a', 3778          # Live-Stand; die Grundfassung steht in keiner Migration -> Datei tools/tests/nf_nachtest_stand_alt.prosrc.txt
EIGENSCHAFTEN = 's|f|f|{"search_path=\\"\\""}'                                  # provolatile | prosecdef | proisstrict | proconfig


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def auswahl_alt():
    s = (MIG / '20261124_nt_s_nachtest_menge.sql').read_text(encoding='utf-8')
    i = s.index('create or replace function schule.nachtest_auswahl(')
    j = s.index('as $function$', i) + len('as $function$')
    b = s[j:s.index('$function$;', j)]
    assert md5(b) == AUSWAHL_ALT_MD5 and len(b) == AUSWAHL_ALT_LEN, 'nachtest_auswahl: Repo-Stand ist nicht der Live-Stand'
    return b


def stand_alt():
    b = STAND_ALT_DATEI.read_bytes().decode('utf-8')
    assert md5(b) == STAND_ALT_MD5 and len(b) == STAND_ALT_LEN, 'nachtest_stand: Datei ist nicht der Live-Stand'
    return b


def ersetzen(b, alt, neu):
    assert b.count(alt) == 1, alt
    return b.replace(alt, neu)


def auswahl_neu(variante=None):
    b = ersetzen(auswahl_alt(), "a.pool = 'sicherung')", "a.pool = 'sicherung' and a.freigegeben)")
    if variante: b = ersetzen(b, 'order by a.gestellt, a.zuletzt nulls first', variante)     # nur für die Gegenprobe im Test
    return b


def stand_neu():
    return ersetzen(stand_alt(), "a.pool = 'sicherung'\n", "a.pool = 'sicherung' and a.freigegeben\n")


def paket(probe, auswahl_variante=None, a_alt=AUSWAHL_ALT_MD5, s_alt=STAND_ALT_MD5):
    an, sn = auswahl_neu(auswahl_variante), stand_neu()
    assert '$function$' not in an + sn
    a_neu, s_neu = md5(an), md5(sn)
    titel = 'Probelauf (rollt am Ende ALLES zurück)' if probe else 'Einspielen'
    ende = ("  raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): %', v_bericht::text;\n" if probe
            else "  raise notice 'NF-S eingespielt: %', v_bericht::text;\n")
    return f"""-- NF-S ({titel}): Nachtest nur mit freigegebenen Aufgaben. schule.nachtest_auswahl und schule.nachtest_stand lassen gesperrte Aufgaben (freigegeben = false) bisher
-- im Vorrat und in der Auswahl; beide werden per create or replace um genau diese eine Bedingung ergänzt – sonst NICHTS (Signatur, Rückgabe, Volatilität, Invoker,
-- search_path, nicht STRICT, Rechte, Kommentare bleiben). VOR der Bestands-Berichtigung 1 einspielen (die bricht ab, wenn NF-S fehlt).
-- Ein Aufruf, eine Transaktion, kein BEGIN/COMMIT. Je Funktion genau zwei zulässige Zustände des Funktionstexts (prosrc-md5): alt (Live-Stand) -> ersetzen, neu -> nichts tun,
-- alles andere -> Abbruch, nichts geändert. Vorher/nachher: Eigenschaften gleich; Ergebnis je Kind × Einheit (nachtest_stand) bzw. je Kind × Einheit/Lernziel × Menge
-- (nachtest_auswahl, deterministisch: Reihenfolge ist durch order by … id festgelegt) vorher = nachher, AUSSER in Einheiten, die schon gesperrte Sicherungs-Aufgaben haben
-- (dort ändert sich das Ergebnis zu Recht; solche Fälle werden gezählt und im Bericht ausgewiesen, kein Abbruch). Aufgaben, die an Sitzungen hängen (testsitzung.aufgaben), bleiben unberührt.
-- alt-md5 auswahl {a_alt} (Länge {AUSWAHL_ALT_LEN}) -> neu {a_neu}; alt-md5 stand {s_alt} (Länge {STAND_ALT_LEN}) -> neu {s_neu}.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '300s', true);
do $nf$
declare v_a constant regprocedure := to_regprocedure('schule.nachtest_auswahl(bigint, bigint, text, integer)');
  v_s constant regprocedure := to_regprocedure('schule.nachtest_stand(bigint, bigint)');
  m_a_alt constant text := '{a_alt}'; m_a_neu constant text := '{a_neu}'; m_s_alt constant text := '{s_alt}'; m_s_neu constant text := '{s_neu}';
  e_soll constant text := '{EIGENSCHAFTEN}';
  fehler text[] := '{{}}'; d text; st_a text; st_s text; ei_a text; ei_s text; ar_a text; ar_s text; ei_a2 text; ei_s2 text; ar_a2 text; ar_s2 text; r record; v text;
  n_a int := 0; n_s int := 0; n_diff int := 0; n_gesperrt int := 0; n_unerw int := 0; n_gesp_live int; v_bericht jsonb; k int;
begin
  if v_a is null or v_s is null or to_regclass('schule.aufgabe') is null or to_regclass('schule.lernender') is null or to_regclass('schule.einheit') is null then
    raise exception 'NF-S ABBRUCH: nachtest_auswahl/nachtest_stand oder die Tabellen fehlen – nichts geändert'; end if;
  -- 1. Zustand je Funktion + Eigenschaften
  select p.prosrc, concat_ws('|', p.provolatile, p.prosecdef, p.proisstrict, coalesce(p.proconfig::text, '')),
         concat_ws('|', pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname) into d, ei_a, ar_a from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = v_a;
  st_a := case md5(d) when m_a_alt then 'alt' when m_a_neu then 'neu' else 'unbekannt' end;
  if st_a = 'unbekannt' then fehler := fehler || format('nachtest_auswahl weicht vom Repo-Stand ab (md5 %s, erwartet %s oder %s)', md5(d), m_a_alt, m_a_neu); end if;
  if ei_a <> e_soll then fehler := fehler || format('nachtest_auswahl: Eigenschaften %s, erwartet %s', ei_a, e_soll); end if;
  select p.prosrc, concat_ws('|', p.provolatile, p.prosecdef, p.proisstrict, coalesce(p.proconfig::text, '')),
         concat_ws('|', pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname) into d, ei_s, ar_s from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = v_s;
  st_s := case md5(d) when m_s_alt then 'alt' when m_s_neu then 'neu' else 'unbekannt' end;
  if st_s = 'unbekannt' then fehler := fehler || format('nachtest_stand weicht vom Repo-Stand ab (md5 %s, erwartet %s oder %s)', md5(d), m_s_alt, m_s_neu); end if;
  if ei_s <> e_soll then fehler := fehler || format('nachtest_stand: Eigenschaften %s, erwartet %s', ei_s, e_soll); end if;
  if array_length(fehler, 1) > 0 then raise exception 'NF-S ABBRUCH, Vorbedingung (% Befunde), nichts geändert: %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;
  select count(*) into n_gesp_live from schule.aufgabe a where a.pool = 'sicherung' and not a.freigegeben;
  -- 2. Vorher-Stand (nur wenn etwas zu ändern ist)
  create temp table nf_v (art text, l bigint, e bigint, lz text, n int, vor text, nach text) on commit drop;
  if st_a = 'alt' then
    insert into nf_v select 'auswahl', l.id, g.e, g.lz, m.n, schule.nachtest_auswahl(l.id, g.e, g.lz, m.n)::text
      from schule.lernender l cross join (select distinct a.einheit_id e, a.variante_gruppe lz from schule.aufgabe a where a.pool = 'sicherung') g
      cross join (values (1), (2), (3), (5)) m(n);
  end if;
  if st_s = 'alt' then
    for r in select l.id l, e.id e from schule.lernender l cross join schule.einheit e loop
      begin v := schule.nachtest_stand(r.l, r.e)::text; exception when others then v := 'FEHLER ' || sqlstate || ' ' || sqlerrm; end;
      insert into nf_v values ('stand', r.l, r.e, null, null, v);
    end loop;
  end if;
  -- 3. Ersetzen
  if st_a = 'alt' then
    execute $a$
create or replace function schule.nachtest_auswahl(p_l bigint, p_e bigint, p_lz text, p_anzahl int)
 returns bigint[] language sql stable set search_path to ''
as $function${an}$function$
$a$;
  end if;
  if st_s = 'alt' then
    execute $s$
create or replace function schule.nachtest_stand(p_lernender bigint, p_einheit bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function${sn}$function$
$s$;
  end if;
  -- 4. Nachher: Zustand, Eigenschaften unverändert
  select p.prosrc, concat_ws('|', p.provolatile, p.prosecdef, p.proisstrict, coalesce(p.proconfig::text, '')), concat_ws('|', pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname)
    into d, ei_a2, ar_a2 from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = v_a;
  if md5(d) <> m_a_neu then fehler := fehler || format('nachtest_auswahl: neuer Funktionstext hat md5 %s, erwartet %s', md5(d), m_a_neu); end if;
  select p.prosrc, concat_ws('|', p.provolatile, p.prosecdef, p.proisstrict, coalesce(p.proconfig::text, '')), concat_ws('|', pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname)
    into d, ei_s2, ar_s2 from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = v_s;
  if md5(d) <> m_s_neu then fehler := fehler || format('nachtest_stand: neuer Funktionstext hat md5 %s, erwartet %s', md5(d), m_s_neu); end if;
  if (ei_a2, ar_a2, ei_s2, ar_s2) is distinct from (ei_a, ar_a, ei_s, ar_s) then fehler := fehler || 'Eigenschaften (Volatilität, Definer/Invoker, STRICT, search_path, Signatur, Rückgabetyp, Sprache) haben sich geändert'; end if;
  if array_length(fehler, 1) > 0 then raise exception 'NF-S ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;
  -- 5. Nachher-Ergebnisse, Vergleich
  if st_a = 'alt' then
    update nf_v x set nach = schule.nachtest_auswahl(x.l, x.e, x.lz, x.n)::text where x.art = 'auswahl';
  end if;
  if st_s = 'alt' then
    for r in select * from nf_v x where x.art = 'stand' loop
      begin v := schule.nachtest_stand(r.l, r.e)::text; exception when others then v := 'FEHLER ' || sqlstate || ' ' || sqlerrm; end;
      update nf_v set nach = v where art = 'stand' and l = r.l and e = r.e;
    end loop;
  end if;
  select count(*) filter (where art = 'auswahl'), count(*) filter (where art = 'stand'), count(*) filter (where vor is distinct from nach),
         count(*) filter (where vor is distinct from nach and exists (select 1 from schule.aufgabe a where a.einheit_id = nf_v.e and a.pool = 'sicherung' and not a.freigegeben)),
         count(*) filter (where vor is distinct from nach and not exists (select 1 from schule.aufgabe a where a.einheit_id = nf_v.e and a.pool = 'sicherung' and not a.freigegeben))
    into n_a, n_s, n_diff, n_gesperrt, n_unerw from nf_v;
  if n_unerw > 0 then
    raise exception 'NF-S ABBRUCH, alles zurückgerollt: % Fälle ändern sich, obwohl in der Einheit keine Sicherungs-Aufgabe gesperrt ist (z. B. %)', n_unerw,
      (select string_agg(format('%s Kind %s Einheit %s %s', art, l, e, coalesce(lz, '')), '; ') from (select * from nf_v where vor is distinct from nach
        and not exists (select 1 from schule.aufgabe a where a.einheit_id = nf_v.e and a.pool = 'sicherung' and not a.freigegeben) limit 5) z); end if;
  v_bericht := jsonb_build_object('nachtest_auswahl', st_a || ' -> neu', 'nachtest_stand', st_s || ' -> neu', 'md5_auswahl_neu', m_a_neu, 'md5_stand_neu', m_s_neu,
    'verglichen_auswahl', n_a, 'verglichen_stand', n_s, 'abweichend_gesamt', n_diff, 'abweichend_wegen_gesperrter_sicherungsaufgaben', n_gesperrt, 'abweichend_unerwartet', n_unerw,
    'gesperrte_sicherungsaufgaben_live', n_gesp_live, 'eigenschaften_gleich', true, 'fehler', 0);
{ende}end $nf$;
"""


def dateien():
    p, e = paket(True), paket(False)
    return [('nf_s_probe.sql', p), ('nf_s_einspielen.sql', e)], e


def main():
    out, einsp = dateien()
    ziele = [(AUS / n, t) for n, t in out] + [(MIGRATION, einsp)]
    for _, t in ziele:
        assert len(t.encode('utf-8')) < 1_500_000 and '\n\\' not in t
    if '--pruefen' in sys.argv:
        alt = [p.name for p, t in ziele if not p.exists() or p.read_text(encoding='utf-8') != t]
        if alt: print('nicht auf dem Stand:', ', '.join(alt), file=sys.stderr); sys.exit(1)
        print('OK'); return
    print('| Datei | Bytes | md5 |\n|---|---|---|')
    for p, t in ziele:
        p.write_text(t, encoding='utf-8')
        print(f'| `{p.relative_to(WURZEL)}` | {len(t.encode("utf-8"))} | `{md5(t)}` |')
    print('md5 auswahl neu', md5(auswahl_neu()), '| md5 stand neu', md5(stand_neu()))


if __name__ == '__main__':
    main()
